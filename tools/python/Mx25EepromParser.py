#
# Mx25EEpromParser
#    These utilities read the contents of a Logic Analyzer file in CSV format
#    which has captured the 6 IO signals of an Mx25EEPROM as it is being
#    accessed (e.g. during a boot process, where portions of the EEPROM are
#    read into SOC memory)
#    It assembles as full a binary image as possible, regardless of the order
#    in which memory is read from the device
#    The most useful parts of the resulting binary file are the first several
#    KBytes which contain the EEPROM header which is not encoded in the .BRN
#    Image

import csv

class Mx25EepromParser:
  opcode = ""
  old_cs_value = 0
  next_cs_time = 1000
  tSHSL = 12e-9    # 7 ns minium CS active time 
  qpi_mode = False
  data_bit_width = 1
  dummy_cycles = 6     # default
  dummy_cycle_p = False     # per command -- interject address dummy cycles (True)
  dummy_cycle_count = 0
  abortable = False
  read_command = True
  command_byte = 0
  command_bit_count = 0
  address_word = 0
  address_bit_width = 1
  address_bit_count = 0
  address_bytes = 0
  next_data_byte = 0
  data_bit_count = 0
  data_byte_count = 0
  sclk_count = 0
  min_data_bytes = 0
  last_SCLKValue = 0
  read_command_index = 0
  debug = False
  hex_not_ascii = True

  binary_data = bytearray()
  memory_map = {}

  # dictionary for commands
  #   indexed by hex opcode
  #   0: Mnemmonic; Number of address cycles; read_command; min_data bytes; data_bit_width; addr_bit_width, dummy_cycle_p; num_dummy_cyles; abortable
  command_table = {"0x01": ["WRSR1", 0, False, 1, 1, 1, False, 0, False],
                   "0x02": ["PP",   0, False, 1, 1, 1, False, 0, False],
                   "0x03": ["READ", 3, True,  1, 1, 1, False, 0, False],
                   "0x04": ["WRDI", 0, False, 0, 0, 0, False, 0, False],
                   "0x05": ["RDSR1", 0, True,  1, 1, 1, False, 0, True],
                   "0x06": ["WREN", 0, False, 0, 0, 0, False, 0, False],
                   "0x11": ["WRSR3", 0, False, 1, 1, 1, False, 0, False],
                   "0x15": ["RDSR3", 0, True,  1, 1, 1, False, 0, True],
                   "0x31": ["WRSR2", 0, False, 1, 1, 1, False, 0, False],
                   "0x35": ["RDSR2", 0, False, 0, 1, 0, False, 0, False], 
                   "0x38": ["4PP",  3, False, 1, 4, 4, False, 0, False],
		   "0x3b": ["2READ", 3, True, 1, 2, 1, True,  8, False], 
                   "0x6b": ["QREAD",3, True,  1, 4, 1, True,  8, False],
		   "0x66": ["ENRST", 0, False, 0, 0, 0, False, 0, False], 
                   "0x9f": ["RDID", 0, True,  4, 0, 1, False, 0, False],
		   "0x99": ["RESET",0, False,  0, 0, 0, False, 0, False],
                   "0xe1": ["WRDPB",4, False, 1, 1, 1, False, 0, False],
                   "0xeb": ["4READ",3, True,  1, 4, 4, True,  6, False]
                   }
  
  # Initialize binary file
  def init_binary_file(self, binary_file): 
    file_length = 8388608
    initial_value = b'\xff'
    index = 0
    while index < file_length:
      binary_file.write(initial_value)
      index += 1
    return

  def write_file_system(self, file_system_binary, offset, binary_file):
    binary_file.seek(offset)
    data = file_system_binary.read(1)
    print("Writing File System to Binary")
    while data:
      binary_file.write(data)
      data = file_system_binary.read(1)
    print("File System Written")
    return

  # Fill in the binary file based on the stored memory map
  def write_binary_file(self, binary_file):
    print("======= WRITING BINARY FILE ========")
    total_length = 0
    for i in sorted (self.memory_map.keys()) : 
      length = self.memory_map[i]['length']
      total_length += length
      bounds = i + length - 1
      print(f'Overwriting segment 0x{i:06x}, length: 0x{length:06x}, bounds: 0x{bounds:06x}')
      binary_file.seek(i)
      binary_file.write(self.memory_map[i]['binary_data']) 
    print(f'Wrote {total_length} bytes')
    print("=======WRITTEN=========")
    return

  def print_memory_map(self):
    print("======= MEMORY MAP ========")
    for i in sorted (self.memory_map.keys()) :  
      #print(f'0x{i:06x}: 0x{self.memory_map[i]['length']:06x})
      length = self.memory_map[i]['length']
      index = self.memory_map[i]['index']
      binary_data = self.memory_map[i]['binary_data'][0:3]
      print(f'0x{i:06x}:  Len: 0x{length:06x} Index: {index}, Data: {binary_data}')
    print("===========================")

  def update_memory_map(self, address, num_bytes, binary_data):
    self.memory_map[address] = {'length': num_bytes, 'index':self.read_command_index, 'binary_data':binary_data}
    self.read_command_index = self.read_command_index + 1

  def risingSCLK(self, SCLKValue):
    if (SCLKValue ==0):
      return False
    elif (self.last_SCLKValue ==0):
      return True
    else:
      return False

  def fallingSCLK(self, SCLKValue):
    if (SCLKValue ==1):
      return False
    elif (self.last_SCLKValue ==1):
      return True
    else:
      return False

  ## checks on SCLK
  def sclk_check(self, current_command, current_time, rising_sclk):
    if (current_command == "0xeb"):
      if rising_sclk:
        self.sclk_count += 1
        if self.debug:
          print(f'@T = {current_time} : sclk count: {self.sclk_count}, data_bit_count: {self.data_bit_count}, data_byte_count: {self.data_byte_count}')
        if (self.data_bit_count == 4):
          #print(f'sclk_count {self.sclk_count}')
          if (self.sclk_count % 2) != 0:
            print(f'@T = {current_time} : Warning!! sclk count: {self.sclk_count}, data_bit_count: {self.data_bit_count}, data_byte_count: {self.data_byte_count}') 
        
    return

  def deglitchedCSValue(self, old_value, current_value, next_value, current_time, next_time):
    if (current_value == 0):
      return 0
    elif (next_time - current_time < self.tSHSL):
      if self.debug:
        print("@T=", current_time, ": Glitch Detected;", current_value, next_time - current_time)
      return 0
    else:
      return 1

    
  
 
  ## Build a command byte from serial input
  ## return True when we have the whole command_byte
  def update_command_bits(self, SIO3, SIO2, SO_SIO1, SI_SIO0):
    if self.qpi_mode :
      self.command_byte = (self.command_byte << 1) | SIO3
      self.command_byte = (self.command_byte << 1) | SIO2
      self.command_byte = (self.command_byte << 1) | SO_SIO1
      self.command_byte = (self.command_byte << 1) | SI_SIO0 
      self.command_bit_count = self.command_bit_count + 4
    else: 
      self.command_byte = (self.command_byte << 1) | SI_SIO0
      self.command_bit_count = self.command_bit_count + 1
    if (self.command_bit_count == 8):
      return(True)
    else:
      return(False)


  ## Build an Address byte from serial input
  ## Return True when we have the whole address_word
  def update_address_bits(self, SIO3, SIO2, SO_SIO1, SI_SIO0):
    if (self.qpi_mode or (self.address_bit_width == 4)):
      self.address_word = (self.address_word << 1) | SIO3
      self.address_word = (self.address_word << 1) | SIO2
      self.address_word = (self.address_word << 1) | SO_SIO1
      self.address_word = (self.address_word << 1) | SI_SIO0 
      self.address_bit_count = self.address_bit_count + 4
      if self.debug:
        print("update_address_bits: address_bit_count = ", self.address_bit_count)
    elif (self.address_bit_width == 2):
      self.address_word = (self.address_word << 1) | SO_SIO1
      self.address_word = (self.address_word << 1) | SI_SIO0 
      self.address_bit_count = self.address_bit_count + 2
    else: 
      self.address_word = (self.address_word << 1) | SI_SIO0
      self.address_bit_count = self.address_bit_count + 1

    if (self.address_bit_count == (self.address_bytes * 8)):
      return(True)
    else:
      return(False)

  def update_dummy_bits(self):
    if(self.dummy_cycle_p):
      self.dummy_cycle_count = self.dummy_cycle_count + 1
      if (self.dummy_cycle_count == self.dummy_cycles) :
        print("debug::update_dummy_bits -- dummy_cycle_count = ", self.dummy_cycle_count)
        self.dummy_cycle_count = 0
        return(True)
      else:
        return(False)
    else: 
      return(True)
  ## Build an Address byte from serial input
  ## Return True when we have a new byte
  def update_read_data(self, SIO3, SIO2, SO_SIO1, SI_SIO0):
    if (self.qpi_mode or (self.data_bit_width == 4)) :
      self.next_data_byte = (self.next_data_byte << 1) | SIO3
      self.next_data_byte = (self.next_data_byte << 1) | SIO2
      self.next_data_byte = (self.next_data_byte << 1) | SO_SIO1
      self.next_data_byte = (self.next_data_byte << 1) | SI_SIO0 
      self.data_bit_count = self.data_bit_count + 4
    elif (self.data_bit_width == 2):
      self.next_data_byte = (self.command_byte << 1) | SO_SIO1
      self.next_data_byte = (self.command_byte << 1) | SI_SIO0 
      self.data_bit_count = self.data_bit_count + 2
    else: 
      self.next_data_byte = (self.next_data_byte << 1) | SO_SIO1
      self.data_bit_count = self.data_bit_count + 1
    if (self.data_bit_count == 8):
      return(True)
    else:
      return(False)

  def update_write_data(self, SIO3, SIO2, SO_SIO1, SI_SIO0):
    if (self.qpi_mode or (self.data_bit_width == 4)) :
      self.next_data_byte = (self.next_data_byte << 1) | SIO3
      self.next_data_byte = (self.next_data_byte << 1) | SIO2
      self.next_data_byte = (self.next_data_byte << 1) | SO_SIO1
      self.next_data_byte = (self.next_data_byte << 1) | SI_SIO0 
      self.data_bit_count = self.data_bit_count + 4
    elif (self.data_bit_width == 2):
      self.next_data_byte = (self.command_byte << 1) | SO_SIO1
      self.next_data_byte = (self.command_byte << 1) | SI_SIO0 
      self.data_bit_count = self.data_bit_count + 2
    else: 
      self.next_data_byte = (self.next_data_byte << 1) | SI_SIO0
      self.data_bit_count = self.data_bit_count + 1
    if (self.data_bit_count == 8):
      return(True)
    else:
      return(False)

  def getNextState(self, currentState, current_row, next_row, outfile, max_data_bytes):
    offset = 0
    TimeValue = float(current_row[0])
    CSValue = int(current_row[1+offset])
    SO_SIO1Value = int(current_row[2+offset])
    WP_SIO2Value = int(current_row[3+offset]) 
    SI_SIO0Value = int(current_row[4+offset])
    SCLKValue = int(current_row[5+offset])
    RESET_SIO3Value = int(current_row[6+offset])

    next_cs_time = float(next_row[0])
    next_cs_value = int(next_row[1+offset])

    if (self.debug):
      print(f'@T={TimeValue} getNextState: current_state: {currentState}, CS: {CSValue} , SCLK: {SCLKValue} , D3: {RESET_SIO3Value}, D2: {WP_SIO2Value}, D1: {SO_SIO1Value}, D0:{SI_SIO0Value}')

    rising_sclk = self.risingSCLK(SCLKValue)
    falling_sclk = self.fallingSCLK(SCLKValue)

    self.last_SCLKValue = SCLKValue

    CSValue = self.deglitchedCSValue(self.old_cs_value, CSValue, next_cs_value, TimeValue, next_cs_time)

    self.sclk_check(self.opcode, TimeValue, rising_sclk)  

    if (currentState == 'idle'):
      self.dummy_cycle_p = False     # per command -- interject address dummy cycles (True)
      self.dummy_cycle_count = 0
      self.data_bit_width = 1
      self.read_command = True
      self.command_byte = 0
      self.command_bit_count = 0
      self.address_word = 0
      self.address_bit_count = 0
      self.address_bytes = 0
      self.next_data_byte = 0
      self.data_bit_count = 0
      self.data_byte_count = 0
      self.min_data_bytes = 0
      if (CSValue == 1): 
        self.sclk_count = 0
        return 'idle'
      else:
        return 'command'

    if (currentState == 'command'):
      if (CSValue == 1):
        return('idle')
      if (rising_sclk):
        if(self.update_command_bits(RESET_SIO3Value, WP_SIO2Value, SO_SIO1Value, SI_SIO0Value)):
          self.opcode = "{0:#0{1}x}".format(self.command_byte,4)
          if (self.opcode in self.command_table):
              self.mnemonic = self.command_table[self.opcode][0]
              self.address_bytes = self.command_table[self.opcode][1]
              self.read_command = self.command_table[self.opcode][2]
              self.min_data_bytes = self.command_table[self.opcode][3]
              self.data_bit_width = self.command_table[self.opcode][4]
              self.address_bit_width = self.command_table[self.opcode][5]
              self.dummy_cycle_p = self.command_table[self.opcode][6]
              self.dummy_cycles = self.command_table[self.opcode][7]
              self.abortable = self.command_table[self.opcode][8]
              print("@T=", TimeValue, " command: " + self.opcode + " : " + self.mnemonic)
              outfile.write("command: " + self.opcode + " : " + self.mnemonic)
              outfile.write("\n")
          else:
              print("@T=", TimeValue, " opcode not recognized ", self.opcode)
              return('error')
          self.binary_data = bytearray()
          if (self.address_bytes > 0):
            return('address')
          elif (self.min_data_bytes > 0):
            if (self.read_command):
              self.sclk_count = 0
              return('read_data')
            else:
              return('write_data')
          else:  
            return('command_done')
        else:
          return('command')
      else:
        return('command')
      
    if (currentState == 'address'):
      if(rising_sclk): 
        if(self.update_address_bits(RESET_SIO3Value, WP_SIO2Value, SO_SIO1Value, SI_SIO0Value)): 
          print("address: 0x%06x" % self.address_word)
          outfile.write("address: 0x%06x \n" % self.address_word)
          if (self.dummy_cycle_p):
            return('dummy_bits')
          else: 
            if (self.min_data_bytes > 0):
              if(self.read_command):
                return('read_data')
              else:
                return('write_data')
            else: 
              return ('address_done')
        else:
          return('address')      
      else:
        return('address')

    if (currentState == 'dummy_bits'):
      if(rising_sclk):
        if(self.update_dummy_bits()):
          if (self.min_data_bytes > 0):
            if(self.read_command): 
              return('read_data')
            else:
              return('write_data')
          else: 
            return ('address_done')
        else:
          return('dummy_bits')
      else:
        return('dummy_bits')

    if ((currentState == 'command_done') or (currentState== 'address_done')):
      if (CSValue == 1):
        return('idle')
      elif (rising_sclk):
        print("Warning @T=", TimeValue, "-- did not expect rising SCLK in state: ", currentState)
        return(currentState)
      else:
        return(currentState)

    if (currentState == 'read_data'):
      if (CSValue == 1):
        if (self.abortable):
          print("Info: ", self.mnemonic, "aborted on non-byte-boundary with rising CS")
        else:
          print("Warning: @T=", TimeValue, ": In state read_data: not expecting CS to go high on non-byte-boundary; Bit count: " + 
                str(self.data_bit_count) + " Byte count: "+ str(self.data_byte_count) + " Sclk_count: " + str(self.sclk_count))
          outfile.write("\n")
        return 'read_done'
      if(rising_sclk):
        if (self.update_read_data(RESET_SIO3Value, WP_SIO2Value, SO_SIO1Value, SI_SIO0Value)):
          if(self.debug):
            print(f'@T= {TimeValue} read_data: {self.next_data_byte:02x}, data_byte = {self.data_byte_count}')
          if (self.data_byte_count < max_data_bytes):
            self.binary_data.append(self.next_data_byte)
            if (self.hex_not_ascii):
              outfile.write("%02x " % self.next_data_byte)
            else:
              outfile.write(chr(self.next_data_byte))
          self.data_byte_count = self.data_byte_count + 1
          if ((self.data_byte_count % 65536) == 0):
              print('@T=', TimeValue, ' -- read ', self.data_byte_count,  ' bytes')
          if ((self.data_byte_count % 16) == 0) and (self.data_byte_count < max_data_bytes):
            if self.debug:
              print('')
            outfile.write("\n")
          self.next_data_byte = 0;
          self.data_bit_count = 0; 
          return('read_done')
        else:
          return('read_data')
      else:
        return('read_data')

    if (currentState == 'read_done'):
      if (CSValue == 1):
        if (self.mnemonic == 'READ') or (self.mnemonic == '4READ') or (self.mnemonic == 'QREAD'):
          # save the data, re-initialize the data structure
          self.update_memory_map(self.address_word, self.data_byte_count, self.binary_data)
        if (self.data_byte_count > max_data_bytes):
          outfile.write("\n DataBytes: 0x%08x\n" % self.data_byte_count)
        else: 
          outfile.write("\n")
        if (self.debug):
          print(f'@T= {TimeValue} read_done -> idle on CSValue == 1, data_byte_count: {self.data_byte_count}')
        return('idle')
      if(rising_sclk):
        if (self.update_read_data(RESET_SIO3Value, WP_SIO2Value, SO_SIO1Value, SI_SIO0Value)):
          if self.debug:
            print("0x02x " % self.next_data_byte)
          if (self.data_byte_count < max_data_bytes):
            self.binary_data.append(self.next_data_byte)
            if (self.hex_not_ascii):
              outfile.write("%02x " % self.next_data_byte)
            else:
              outfile.write(chr(self.next_data_byte))
          self.data_byte_count = self.data_byte_count + 1
          if ((self.data_byte_count % 65536) == 0):
              print('@T=', TimeValue, ' -- read ', self.data_byte_count, ' bytes')
          if ((self.data_byte_count % 16) == 0) and (self.data_byte_count < max_data_bytes):
            if self.debug:
              print('')
            outfile.write("\n")
          self.next_data_byte = 0;
          self.data_bit_count = 0; 
          return('read_done')
        else:
          return('read_data')
      else:
        return('read_done')
        
    if (currentState == 'write_data'):
      if (CSValue == 1):
        outfile.write("\n")
        return('idle')
      if (falling_sclk): 
        if (self.update_write_data(RESET_SIO3Value, WP_SIO2Value, SO_SIO1Value, SI_SIO0Value)):
          if self.debug:
            print("%02x " % self.next_data_byte, end='')
          if (self.data_byte_count < max_data_bytes):
            outfile.write("%02x " % self.next_data_byte)
          self.data_byte_count = self.data_byte_count + 1
          if ((self.data_byte_count % 16) == 0) and (self.data_byte_count < max_data_bytes):
            if self.debug:
              print('')
            outfile.write("\n")
          self.next_data_byte = 0; 
          self.data_bit_count = 0;
          return('write_done')
        else:
          return('write_data')
      else:
        return('write_done')
    
    if (currentState == 'write_done'):
      if (CSValue == 1):
        outfile.write("\n")
        return('idle')
      if (falling_sclk):
        if (self.update_write_data(RESET_SIO3Value, WP_SIO2Value, SO_SIO1Value, SI_SIO0Value)):
          if self.debug:
            print("%02x " % self.next_data_byte, end='')
          if (self.data_byte_count < max_data_bytes):
            outfile.write("%02x " % self.next_data_byte)
          self.data_byte_count = self.data_byte_count + 1
          if ((self.data_byte_count % 16) == 0) and (self.data_byte_count < max_data_bytes):
            if self.debug:
              print('')
            outfile.write("\n")
          self.next_data_byte = 0; 
          self.data_bit_count = 0;
          return('write_done')
        else:
          return('write_data')
      else:
        return('write_done')

    # Oops -- we should not be here
    print("Error -- unrecognized state: ", currentState)
    return('idle')

  def image_file_from_la_trace(self, file_path, input_filename, output_filename, binary_output_filename,
                               maxCommands=100000000, maxDataBytes=8192000, hex_not_ascii=True,
                               debug_start = 0.0, debug_end =0.0):
    self.qpi_mode = False
    self.read_command = True
    self.command_byte = 0
    self.command_bit_count = 0
    self.address_word = 0
    self.address_bit_count = 0
    self.data_bit_count = 0
    self.max_data_bytes = 0
    self.read_command_index = 0
    self.debug = False
    self.memory_map ={}
    self.hex_not_ascii = hex_not_ascii
    self.binary_data = bytearray()

    currentState = 'idle'
    timeValue = 0.0

    full_input_filename = file_path + input_filename
    print("Opening input filename" +  full_input_filename)
    full_output_filename = file_path + output_filename
    print("Opening input filename" +  full_output_filename)

    with open(full_input_filename, newline='') as csvfile, open(full_output_filename, "w", newline='') as outfile:
      linereader = csv.reader(csvfile, delimiter=',', quotechar='|')
      headerRead = False
      current_row = []
      for next_row in linereader:
        if (not(headerRead)): 
          headerRead = True
          print("Header", next_row)
        elif (current_row == []):
          current_row = next_row 
        else:
          nextState = self.getNextState(currentState, current_row, next_row, outfile, maxDataBytes)
          if (nextState != currentState) : 
            timeValue = float(current_row[0])
            if (False and (timeValue > 0.017480835)):
                print("Aborted -- timeValue exceeded")
                break;
            if (True and (nextState == 'idle')):   
              print("@T=", timeValue, ":" + currentState + "==> " + nextState + " after " + str(self.data_byte_count) + " bytes")    
              if (True and (timeValue >= 100.0)):
                self.debug = True
            currentState = nextState
          maxCommands = maxCommands - 1
          current_row = next_row
          if (timeValue > debug_start) and (timeValue < debug_end):
            self.debug = True
          else:
            self.debug = False
        if (maxCommands < 0):
            print("Aborted:: maxCommands exceeded");
            break;
    
    self.print_memory_map()

    full_binary_filename = file_path + binary_output_filename
    with open(full_binary_filename, "wb") as binary_output_file:
      self.init_binary_file(binary_output_file)
      self.write_binary_file(binary_output_file)
    return    
