#
# SDCardLogicAnalyzer.py
#    These utilities read the contents of a Logic Analyzer file in CSV format
#    which has captured the 6 IO signals of an SD card as it is being
#    accessed (e.g. during a boot process, where portions of the SD card are
#    read into SOC memory)
#    It turns these into a listing of commands and data

# 2023-10-12: I think I have this mostly working

import csv

from icecream import ic

## SimulatedBlockStorage
##    a Dictionary to hold a simulated block storage device
##    also to add data to the block storage device from SD Card write operations
##    also to check reads from SD card read operations
class SimulatedBlockStorage:

    c_logfile = None
    c_storage_dict = {}
    c_block_number = 0
    c_block_offset = 0

    def set_log_file(self, log_file):
        self.c_logfile = log_file
        self.c_storage_dict = {}

    # Debug
    def debug_print(self, formatted_string, newline=True):
        if (newline == True):
            print(formatted_string)
            if (self.c_logfile):
                print(formatted_string, file = self.c_logfile)
        else:
            print(formatted_string, end='')
            if (self.c_logfile):
                print(formatted_string, end='', file = self.c_logfile)
        return

    ##
    def post_data(self, command_name, block_number, data):
        self.debug_print(f'DEBUG::post_data -- processing {command_name}, block number 0x{block_number:08x}')
        if (command_name == 'WRITE_BLOCK'):
            self.write_block(block_number, data)
        elif (command_name == 'WRITE_MULTIPLE_BLOCK'):
            self.write_block(block_number + self.c_block_offset , data)
            self.c_block_offset += 1
        elif (command_name == 'READ_SINGLE_BLOCK'):
            self.read_block(block_number, data)
        elif (command_name == 'READ_MULTIPLE_BLOCK'):
            self.read_block(block_number + self.c_block_offset, data)
            self.c_block_offset += 1
        else:
            self.debug_print(f'ERROR::post_data -- unrecognized command {command_name}')
            
    ## write a single block
    def write_block(self, block_number, data):
        self.debug_print(f'DEBUG::write_block: write block 0x{block_number:08x}')
        if block_number in self.c_storage_dict:
            self.c_storage_dict[block_number]['writes'] += 1
        else: 
            self.c_storage_dict[block_number] = {}
            self.c_storage_dict[block_number]['writes'] = 1
            self.c_storage_dict[block_number]['reads'] = 0

        ## we need to copy elements from the data block
        self.c_storage_dict[block_number]['data'] = {}
        for index in data:
            self.c_storage_dict[block_number]['data'][index] = data[index]

        
    def stop_block_transfer(self):
        self.debug_print(f'DEBUG::stop_block_transfer after block 0x{self.c_block_offset:08x}')
        self.c_block_offset = 0
        self.c_block_number = 0

    ## compare a read operation from the logic analzyer trace to what we expect to find there
    def read_block(self, block_number, ref_data):
        self.debug_print(f'DEBUG::read_block: read block 0x{block_number:08x}')
        if block_number in self.c_storage_dict:
            self.c_storage_dict[block_number]['reads'] += 1
            self.compare_block_data(block_number, self.c_storage_dict[block_number]['data'], ref_data)
        else: 
            self.debug_print(f'ERROR::read_block: reading from uninitialized block at 0x{block_number:08x}; setting to ref data')
            self.c_storage_dict[block_number] = {}
            self.c_storage_dict[block_number]['reads'] = 1
            self.c_storage_dict[block_number]['writes'] = 0
            self.c_storage_dict[block_number]['data'] = {} 
            for index in ref_data:
                self.c_storage_dict[block_number]['data'][index] = ref_data[index]

    ## just get the data
    def get_block(self, block_number):
        self.debug_print(f'DEBUG::get_block: read block 0x{block_number:08x}')
        if block_number in self.c_storage_dict:
            return self.c_storage_dict[block_number]['data']
        else: 
            self.debug_print(f'ERROR::get_block: trying to read from uninitialized block at 0x{block_number:08x}')
            return None

    ## Compare two data blocks
    def compare_block_data(self, block, stored_data, ref_data):
        error_detected = False
        num_errors = 0
        max_errors = 16
        for address in range(512):
            s_data = stored_data[address]
            r_data = ref_data[address]
            if  s_data != r_data:
                num_errors += 1
                error_detected = True
                if (num_errors < max_errors):
                    self.debug_print(f'ERROR::compare_data: at 0x{address:03x} :stored_data 0x{s_data:02x} != ref_data 0x{r_data:02x}')
        if (error_detected):
            self.debug_print(f'ERROR:: {num_errors} Mismatches detected in block 0x{block:08x}')
        else:
            self.debug_print(f'Info:: no mismatches in block 0x{block:08x}')
        
            
    ## print block store_meta_data
    def print_block_device_contents(self):
        self.debug_print(f'INFO::print_block_device_contents: Start')
        for block in sorted(self.c_storage_dict.keys()):
            writes = self.c_storage_dict[block]['writes']
            reads = self.c_storage_dict[block]['reads']
            self.debug_print(f'INFO::print_block_device_contents : Block 0x{block:08x}; writes:{writes}; reads:{reads}')
            self.pretty_print_data(self.c_storage_dict[block]['data'])
        return
            
    # Print a 512 byte data block as hex and ascii in canonical format
    def pretty_print_data(self, data): 
        for i in range(32):
            self.debug_print(f'0x{i<<4:03x}: ', newline=False)
            for j in range(16):
                index = (i <<4) + j 
                self.debug_print(f'{data[index]:02x} ', newline=False)
            self.debug_print(' ', newline=False)
            for j in range(16):
                index = (i << 4) + j
                if (data[index] >= 32) and (data[index] < 127):
                    ascii_char = chr(data[index])
                else:
                    ascii_char = '.'
                self.debug_print(f'{ascii_char}', newline=False)
            self.debug_print(" ")



# Implement accessors to an ExFAT file system based on a block
#     storage device
class EXFATFileSystem:
    c_logfile = None
    c_block_device = None

    # Debug
    def debug_print(self, formatted_string, newline=True):
        if (newline == True):
            print(formatted_string)
            if (self.c_logfile):
                print(formatted_string, file = self.c_logfile)
        else:
            print(formatted_string, end='')
            if (self.c_logfile):
                print(formatted_string, end='', file = self.c_logfile)
        return

    def set_log_file(self, log_file):
        self.c_logfile = log_file
      
    def set_block_device(self, block_device):
        self.c_block_device = block_device


    # Simple
    def check_file_system(self):
        # given
        self.debug_print(f'"DEBUG::check_file_system: not yet implemented')
        return



class SDCardLogicAnalyzer:
  c_logfile = None
  c_debug = False
  c_time_value = 0.0
  c_last_CLK_Value = False
  c_cmd_value = 0
  c_command_code = 0
  c_app_command = False
  c_response_format = ''
  c_command_name = ''
  c_bit_count = 0
  c_response_value = 0
  c_card_state = 'idle'
  c_data_width = 1
  c_data_size = 0   # bits
  c_data_format = 'WIDE_DATA'   # vs. 'USUAL_DATA' # 'NO_DATA'
  c_block_size = 512 * 8 # bits
  c_usual_data_read = {}    # an array of bytes
  c_wide_data_read = 0      # a giant integer
  c_data0_read = 0
  c_data1_read = 0
  c_data2_read = 0
  c_data3_read = 0
  c_data_write = 0
  c_data_bit_count = 0
  c_data_state = 'data_init' # data_init, data_rcv, data_crc, data_end_check, data_write_response, data_write_busy, data_write_ready
                             
  c_data0_crc = 0
  c_data1_crc = 0
  c_data2_crc = 0
  c_data3_crc = 0
  c_data_crc_bit_count = 0

  c_data_write_response_bit_count = 0
  c_data_write_response = 0

  c_read_write_block = 0
  
  ## simulated block device
  c_block_device = SimulatedBlockStorage()
  ## ExFat file system
  c_exfat_file_system = EXFATFileSystem()

    # 'rdy', 'ident', 'stby', 'tran', 'data', 'rcv', 'prg', 'dis', 'ina'


  # Master Table
  #                                                                              Current State
  #               CMD-ID    command_name,     reponse_type, data,  'idle',  'rdy', 'ident',   'stby', 'tran', 'data',  'rcv',  'prg',  'dis',  'ina'         DATA FORMAT
  c_command_table = { 0 : ["GO_IDLE_STATE",            '-',    0, ['idle', 'idle',  'idle', 'idle', 'idle', 'idle', 'idle', 'idle', 'idle',   '-'], 'NO_DATA'],
                      1 : ["SEND_OP_COND",             'R1',   0, ['-',       '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      2 : ["ALL_SEND_CID",             'R2',   0, [   '-','ident',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      3 : ["SEND_RELATIVE_ADDR",       'R6',   0, [   '-',    '-',  'stby', 'stby',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      4 : ["SET_DSR",                   '-',   0, [   '-',    '-',     '-', 'stby',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                       6: ["SWITCH_FUNC",              'R1', 512, [   '-',    '-',     '-', 'stby', 'data',    '-',    '-',    '-',    '-',   '-'], 'WIDE_DATA'],
                    'A6': ["SET_BUS_WIDTH",            'R1',   0, [   '-',    '-',     '-',    '-', 'tran',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      7: ["SELECT_DESELECT_CARD",      'R1b',  0, [   '-',    '-',     '-', 'tran',    '-',    '-',    '-',    '-', 'prog',   '-'], 'NO_DATA'],
                      8: ["SEND_IF_COND",              'R7',   0, ['idle',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      9: ["SEND_CSD",                  'R2',   0, [   '-',    '-',     '-', 'stby',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      10: ["SEND_CID",                 'R2',   0, [   '-',    '-',     '-', 'stby',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      11: ["VOLTAGE_SWITCH",           'R1',   0, [   '-','ready',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      12: ["STOP_TRANSMISSION",        'R1b',  0, [   '-',    '-',     '-',    '-', 'tran', 'tran',  'prg',    '-',    '-',   '-'], 'NO_DATA'],
                      13: ["SEND_STATUS",              'R1',   0, [   '-',    '-',     '-', 'stby', 'tran', 'data',  'rcv',  'prg',  'dis',   '-'], 'NO_DATA'],
                   'A13': ["SD_STATUS",                'R1', 512, [   '-',    '-',     '-',    '-', 'data',    '-',    '-',    '-',    '-',   '-'], 'WIDE_DATA'],
                      15: ["GO_INACTIVE_STATE",         '-',   0, [   '-',    '-',     '-',  'ina',  'ina',  'ina',  'ina',  'ina',  'ina',   '-'], 'NO_DATA'],
                      16: ["SET_BLOCKLEN",             'R1',   0, [   '-',    '-',     '-',    '-', 'tran',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      17: ["READ_SINGLE_BLOCK",        'R1', c_block_size, [   '-',    '-',     '-',    '-', 'data',    '-',    '-',    '-',    '-',   '-'], 'USUAL_DATA'],
                      18: ["READ_MULTIPLE_BLOCK",      'R1', c_block_size, [   '-',    '-',     '-',    '-', 'data',    '-',    '-',    '-',    '-',   '-'], 'USUAL_DATA'],
                      19: ["SEND_TUNING_BLOCK",        'R1', 512, [   '-',    '-',     '-',    '-', 'data',    '-',    '-',    '-',    '-',   '-'], 'WIDE_DATA'],
                      20: ["SPEED_CLASS_CONTROL",     'R1b',   0, [   '-',    '-',     '-',    '-',  'prg',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      21: ["CMD21 -- ??",              '??',   0,    ['-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      22: ["ADDRESS_EXTENSION",        'R1',   0, [   '-',    '-',     '-',    '-', 'tran',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      23: ["SET_BLOCK_COUNT",          'R1',   0, [   '-',    '-',     '-',    '-', 'tran',    '-',    'prg',  '-',    '-',   '-'], 'NO_DATA'],
                   'A23': ["SET_WR_BLK_ERASE_COUNT",   'R1',   0, [   '-',    '-',     '-',    '-', 'tran',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      24: ["WRITE_BLOCK",              'R1', c_block_size, [   '-',    '-',     '-',    '-',  'rcv',    '-',    '-',    '-',    '-',   '-'], 'USUAL_DATA'],
                      25: ["WRITE_MULTIPLE_BLOCK",     'R1', c_block_size, [   '-',    '-',     '-',    '-',  'rcv',    '-',    '-',    '-',    '-',   '-'], 'USUAL_DATA'],
                      27: ["PROGRAM_CSD",              'R1',   0, [   '-',    '-',     '-',    '-',  'rcv',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      28: ["SET_WRITE_PROT",          'R1b',   0, [   '-',    '-',     '-',    '-',  'prg',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      29: ["CLR_WRITE_PROT",          'R1b',   0, [   '-',    '-',     '-',    '-',  'prg',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      30: ["SEND_WRITE_PROT",          'R1',   0, [   '-',    '-',     '-',    '-', 'data',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      32: ["ERASE_WR_BLK_START_ADDR",  'R1',   0, [   '-',    '-',     '-',    '-', 'tran',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      33: ["ERASE_WR_BLK_END_ADDR",    'R1',   0, [   '-',    '-',     '-',    '-', 'tran',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      37: ["CMD_37",                   'R1',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      38: ["ERASE",                   'R1b',   0, [   '-',    '-',     '-',    '-',  'prg',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      40: ["DPS40",                    'R1',   0, [   '-',    '-',     '-',    '-', 'data',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      41: ["RSVD",                     'R3',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                  'A41B': ["SD_SEND_OP_COND_BUSY",     'R3',   0, ['idle',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                   'A41': ["SD_SEND_OP_COND",          'R3',   0, ['ready',   '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                'A41OCR': ["SD_SEND_OP_COND_OCR",      'R3',   0, [ 'ina',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                  'A41Q': ["SD_SEND_OP_COND_QUERY",    'R3',   0, ['idle',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      42: ["LOCK_UNLOCK",              'R1',   0, [   '-',    '-',     '-',    '-',  'rcv',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                   'A42': ["SET_CLR_CARD_DETECT",      'R1',   0, [   '-',    '-',     '-',    '-', 'tran',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      51: ["RSVD",                     'R1',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                   'A51': ["SEND_SCR",                 'R1',  64, [   '-',    '-',     '-',    '-', 'data',    '-',    '-',    '-',    '-',   '-'], 'WIDE_DATA'],
                      55: ["APP_CMD",                  'R1',   0, ['idle',    '-',      '-', 'stby','tran',  'data', 'rcv',   'prg',  'dis',  '-'], 'NO_DATA'],
                      56: ['GEN_CMD',                  'R1',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      58: ['READ_OCR',                 'R3',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      59: ['CRC_ON_OFF',               'R1',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      60: ['CMD60_MAN_RSVD',           'R1',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      61: ['CMD61_MAN_RSVD',           'R1',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      62: ['CMD62_MAN_RSVD',           'R1',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA'],
                      63: ['CMD63_MAN_RSVD',           'R1',   0, [   '-',    '-',     '-',    '-',    '-',    '-',    '-',    '-',    '-',   '-'], 'NO_DATA']
                   }



  c_response_table = {
                  'R1' : [48],
                  'R1b' : [48],
                  'R2' : [136],
                  'R3' : [48],
                  'R6' : [48],
                  'R7' : [48]
                  }
  ## States
  # 'sd_idle'
  # 'sd_start
  # 'sd_cmd'
  # 'sd_response'
  # 'sd_voltage_switch'
  # 'sd_read_data'
  # 'sd_write_data'

  # Debug
  def debug_print(self, formatted_string, newline=True):
      if (newline == True):
          print(formatted_string)
          if (self.c_logfile):
              print(formatted_string, file = self.c_logfile)
      else:
          print(formatted_string, end='')
          if (self.c_logfile):
              print(formatted_string, end='', file = self.c_logfile)
      return

  ## Clock Mechanics -- Detect Rising and Falling Clock signals
  def risingCLK(self, CLKValue):
    if (CLKValue == 0):
      return False
    elif (self.c_last_CLK_Value == 0):
      return True
    else:
      return False


  def fallingCLK(self, CLKValue):
    if (CLKValue == 1):
      return False
    elif (self.c_last_CLK_Value == 1):
      ##self.debug_print(f'@{self.c_time_value} debug:: Falling Clock CLKValue: {CLKValue} last clock: {self.c_last_CLK_Value}')
      return True
    else:
      return False


  ## Command Structure Accessors
  def get_command_name(self, command_list):
    return command_list[0]

  def get_command_response_type(self, command_list):
    return command_list[1]

  def get_command_data_size(self, command_list):
    return command_list[2]

  def get_command_data_format(self, command_list):
    return command_list[4]


  ## CRC Calculations -- first the general, then the specific
  def general_crc(self, data, data_size, crc_size, polynomial, seed_value):
    xor_mask = (polynomial & ((1 << crc_size) - 1)) >> 1
    # initialize the CRC register
    crc_register = seed_value
    # Ensure data is within the specified number of bits
    data &= (1 << data_size) - 1
    # Perform CRC calculation
    for i in range(data_size):
      input_bit = (data >> (data_size - i - 1)) & 0x01
      input_xor = input_bit ^ (crc_register >> (crc_size-1))
      if (input_xor == 1):
        crc_register = crc_register ^ xor_mask
      crc_register =  input_xor | (crc_register << 1)
      crc_register = crc_register & (1 << crc_size) - 1
    return crc_register

  def compute_crc7(self, data, num_bits):
    # The CRC7 polynomial used in SD cards is x^7 + x^3 + 1
    polynomial = 0x89
    return(self.general_crc(data, num_bits, 7, polynomial, 0x00))

  def compute_crc16(self, data, num_bits):
    # The CRC16 polynomial used in SD cards is x^16 + x^12 + x^5 + 1
    polynomial = 0x11021
    return(self.general_crc(data, num_bits, 16, polynomial, 0x00))


  # Card State Transitios (not to be confused with command state transitiosn)
  
  ## Handle the state transition for special cases
  def card_state_special_case_a41(self, command_code, r3_value):
    if (self.get_r3_ocr_valid_p(r3_value) == False):
      command_code = 'A41OCR'
    elif(self.get_r3_busy_p(r3_value)):
      command_code = 'A41B'
    elif(self.get_r3_query_p(r3_value)):
      command_code = 'A41Q'
    else:
      command_code = 'A41'
    r3_busy_p = self.get_r3_busy_p(r3_value)
    #self.debug_print(f'card_state_special_case: 2 get_r3_busy_p = {r3_busy_p}, r3_value = 0x{r3_value:08x}')
    #self.debug_print(f'card_state_special_case: command_code = {command_code}')
    return command_code

  def get_next_card_state(self, current_state, command_code, r3_value):
    ## Special Cases
    if (command_code == 'A41'):
      command_code = self.card_state_special_case_a41(command_code, r3_value)
    ## Handle the GO_IDLE_STATE command
    # self.debug_print(f'debug:: get_next_card_state: command_code= {command_code}')
    if (command_code == 0): return 'idle'  # GO_IDLE_STATE
    ## lookup next state in table
    table_entry = self.c_command_table[command_code][3]
    if (current_state == 'idle'): return table_entry[0]
    if (current_state == 'ready'): return table_entry[1]
    if (current_state == 'ident'): return table_entry[2]
    if (current_state == 'stby'):return table_entry[3]
    if (current_state == 'tran'):return table_entry[4]
    if (current_state == 'data'):return table_entry[5]
    if (current_state == 'rcv'):return table_entry[6]
    if (current_state == 'prg'):return table_entry[7]
    if (current_state == 'dis'):return table_entry[8]
    if (current_state == 'ina'):return table_entry[9]
    else: return ('-')

  def set_data_size(self, command_code, command_argument):
    self.c_data_size = self.c_command_table[command_code][2]
    command_name = self.c_command_table[command_code][0]
    if (command_name == 'SET_BUS_WIDTH'):
      if (command_argument & 0x3 == 0):
        self.c_data_width = 1
      elif (command_argument & 0x3 == 2):
        self.c_data_width = 4
      else:
        self.debug_print(f'ERROR::set_data_size -- unrecognized bus width {command_argument & 3}')
      self.debug_print(f'debug::set_datasize -- set c_data_width to {self.c_data_width}')


  # Command Handling
  def process_command(self, command):
    self.c_command_code = (command & 0x3f0000000000) >> 40
    ## This is the basis for an escape into application-specific versions of
    ## commands.  A necessary anathema
    local_app_command = self.c_app_command
    if (self.c_command_code == 55):
      self.c_app_command = True
    else:
      self.c_app_command = False;

    if (local_app_command == True):
      self.c_command_code = 'A' + str(self.c_command_code)
    command_list = self.c_command_table[self.c_command_code]
    self.c_command_name = self.get_command_name(command_list)
    self.c_response_format = self.get_command_response_type(command_list)
    self.c_data_format = self.get_command_data_format(command_list)
    data_size = self.get_command_data_size(command_list)
    command_argument = (command & 0xFFFFFFFF) >> 8
    crc = (command & 0xff) >> 1
    end_bit = command & 0x1
    self.debug_print(f'0x{command:12x} {self.c_command_name}[{self.c_command_code}] (arg: {command_argument:08x} crc: {crc:02x} end_bit: {end_bit} response_format: {self.c_response_format} data_size:{data_size})')
    if (self.c_command_name == 'SD_SEND_OP_COND'):
      self.pretty_print_acmd41_arg(command_argument)
    ## Set the expected data size(if necessary)
    self.set_data_size(self.c_command_code, command_argument)
    ## if there will be no response, handle card state now
    ##    handle car state afer response has been received
    if (self.c_response_format == '-'):
      next_card_state = self.get_next_card_state(self.c_card_state, self.c_command_code, 0)
      self.debug_print(f'Info::process_command: {self.c_card_state} ==> {next_card_state}')
      self.c_card_state = next_card_state
    ## remember the arguments for read and write block operations
    if ((self.c_command_name == 'WRITE_BLOCK') or
        (self.c_command_name == 'WRITE_MULTIPLE_BLOCK') or
        (self.c_command_name == 'READ_SINGLE_BLOCK') or
        (self.c_command_name == 'READ_MULTIPLE_BLOCK')):
        self.c_read_write_block = command_argument
        self.debug_print(f'DEBUG::process_command -- processing {self.c_command_name} arg: 0x{command_argument:08x}')
    elif (self.c_command_name == 'STOP_TRANSMISSION'):
        self.c_block_device.stop_block_transfer()

  def get_response_length_from_cmd(self, cmd_value):
    command_code = (cmd_value & 0x3f0000000000) >> 40
    command_list = self.c_command_table[command_code]
    response_type = self.get_command_response_type(command_list)
    return self.get_response_length_from_type(response_type)

  def get_response_length_from_type(self, response_type):
    return self.c_response_table[response_type][0]

  def pretty_print_card_status(self, card_status_value):
    self.debug_print(f'   OUT_OF_RANGE      : {(card_status_value & 0x80000000)>>31}')
    self.debug_print(f'   ADDRESS_ERROR     : {(card_status_value & 0x40000000)>>30}')
    self.debug_print(f'   BLOCK_LEN_ERROR   : {(card_status_value & 0x20000000)>>29}')
    self.debug_print(f'   ERASE_SEQ_ERROR   : {(card_status_value & 0x10000000)>>28}')
    self.debug_print(f'   ERASE_PARAM       : {(card_status_value & 0x08000000)>>27}')
    self.debug_print(f'   WP_VIOLATION      : {(card_status_value & 0x04000000)>>26}')
    self.debug_print(f'   CARD_IS_LOCKED    : {(card_status_value & 0x02000000)>>25}')
    self.debug_print(f'   LOCK_UNLOCK_FAILED: {(card_status_value & 0x01000000)>>24}')

    self.debug_print(f'   COM_CRC_ERROR     : {(card_status_value & 0x00800000)>>23}')
    self.debug_print(f'   ILLEGAL_COMMAND   : {(card_status_value & 0x00400000)>>22}')
    self.debug_print(f'   CARD_ECC_FAILED   : {(card_status_value & 0x00200000)>>21}')
    self.debug_print(f'   CC_ERROR          : {(card_status_value & 0x00100000)>>20}')
    self.debug_print(f'   ERROR             : {(card_status_value & 0x00080000)>>19}')
    self.debug_print(f'   rsvd              : {(card_status_value & 0x00040000)>>18}')
    self.debug_print(f'   rsvd              : {(card_status_value & 0x00020000)>>17}')
    self.debug_print(f'   CSD_OVERWRITE     : {(card_status_value & 0x00010000)>>16}')

    self.debug_print(f'   WP_ERASE_SKIP     : {(card_status_value & 0x00008000)>>15}')
    self.debug_print(f'   CARD_ECC_DISABLED : {(card_status_value & 0x00004000)>>14}')
    self.debug_print(f'   ERASE_RESET       : {(card_status_value & 0x00002000)>>13}')
    self.debug_print(f'   CURRENT_STATE     : {(card_status_value & 0x00001E00)>>9}')
    self.debug_print(f'   READY_FOR_DATA    : {(card_status_value & 0x00000100)>>8}')

    self.debug_print(f'   rsvd              : {(card_status_value & 0x00000080)>>7}')
    self.debug_print(f'   FX_EVENT          : {(card_status_value & 0x00000040)>>6}')
    self.debug_print(f'   APP_CMD           : {(card_status_value & 0x00000020)>>5}')
    self.debug_print(f'   rsvd              : {(card_status_value & 0x00000010)>>4}')
    self.debug_print(f'   AKE_SEQ_ERROR     : {(card_status_value & 0x00000008)>>3}')
    self.debug_print(f'   rsvd              : {(card_status_value & 0x00000004)>>2}')
    self.debug_print(f'   rsvd              : {(card_status_value & 0x00000002)>>1}')
    self.debug_print(f'   rsvd              : {(card_status_value & 0x00000001)>>0}')
    return

  def pretty_print_r3(self, r3_value):
    self.debug_print(f'   Busy       : {(r3_value & 0x80000000)>>31}')
    self.debug_print(f'   CCS        : {(r3_value & 0x40000000)>>30}')
    self.debug_print(f'   UHS-II     : {(r3_value & 0x20000000)>>29}')
    self.debug_print(f'   RSVD(0)    : {(r3_value & 0x1E000000)>>25}')
    self.debug_print(f'   S18A       : {(r3_value & 0x01000000)>>24}')
    ocr_value = (r3_value & 0x00FFFF00)>>8
    self.debug_print(f'   OCR        : 0x{ocr_value:04x}')
    rsvd_value = (r3_value & 0x000000FF)
    self.debug_print(f'   RVSD(0x00) : 0x{rsvd_value:02x}')

  def pretty_print_acmd41_arg(self, arg_value):
    self.debug_print(f'   Busy       : {(arg_value & 0x80000000)>>31}')
    self.debug_print(f'   HCS        : {(arg_value & 0x40000000)>>30}')
    self.debug_print(f'   FB(0)      : {(arg_value & 0x20000000)>>29}')
    self.debug_print(f'   XPC        : {(arg_value & 0x10000000)>>28}')
    self.debug_print(f'   RSVD(0)    : {(arg_value & 0x0E000000)>>25}')
    self.debug_print(f'   S18R       : {(arg_value & 0x01000000)>>24}')
    ocr_value = (arg_value & 0x00FFFF00)>>8
    self.debug_print(f'   OCR        : 0x{ocr_value:04x}')
    rsvd_value = (arg_value & 0x000000FF)
    self.debug_print(f'   RVSD(0x00) : 0x{rsvd_value:02x}')



  ## Handling Comand Responses

  ## R3 reponse type accessors
  def get_r3_ocr_valid_p(self, r3_value):
    return True

  def get_r3_query_p(self, r3_value):
    if (r3_value == 0):
      return False
    else:
      return False

  def get_r3_busy_p(self, r3_value):
    busy_bit = (r3_value & 0x80000000)>>31
    if (busy_bit == 0):
      return True
    else:
      return False

  def process_response(self, response, format):
    r3_value = 0
    response_length = self.get_response_length_from_type(format)
    if ((format == 'R1') or (format == 'R1b')):
      cmd_index = (response & 0x3f0000000000) >> 40
      card_status_value = (response & 0xFFFFFFFF00) >> 8
      crc7 = (response & 0xFE) >> 1
      self.debug_print(f'  {format} : 0x{response:012x} cmd_idx:{cmd_index}, card_status: 0x{card_status_value:08x}, crc7: 0x{crc7:02x}')
      #self.pretty_print_card_status(card_status_value)
      expected_crc7 = self.compute_crc7(response >> 8, 40)
      if (crc7 != expected_crc7):
        self.c_app_command = False
        self.debug_print(f'@{self.c_time_value} ERROR::process_response -- crc7 expected 0x{expected_crc7:02x}  actual 0x{crc7:02x}')
    elif (format == 'R2'):
      crc7 = response & 0xFE
      self.debug_print(f'  {format} : 0x{response:18x} crc7: 0x{crc7}')
      expected_crc7 = self.compute_crc7((response & 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF) >> 7, 120)
      if (crc7 != expected_crc7):
          self.debug_print(f'@{self.c_time_value} ERROR::process_response -- crc7 expected 0x{expected_crc7:02x}  actual 0x{crc7:02x}')
    elif (format == 'R3'):
      cmd_index = (response & 0x3f0000000000) >> 40
      r3_value = (response & 0xFFFFFFFF00) >> 8
      crc7 = (response & 0xFE) >> 1
      self.debug_print(f'  {format} : 0x{response:12x} cmd_idx:{cmd_index}, r3_value: 0x{r3_value:08x}, crc7: 0x{crc7:02x}')
      expected_crc7 = 0x7f   ## crc of R3 response is hardwired to ones
      if (crc7 != expected_crc7):
          self.debug_print(f'@{self.c_time_value} ERROR::process_response -- crc7 expected 0x{expected_crc7:02x}  actual 0x{crc7:02x}')
      self.pretty_print_r3(r3_value)
    elif (format == 'R6'):
      self.debug_print(f'  {format} : 0x{response:12x}')
    elif (format == 'R7'):
      self.debug_print(f'  {format} : 0x{response:12x}')
    else:
      self.debug_print(f'Warning:: process_reponse: unrecognized_response type {format}')

    # Compute the next card state
    next_card_state = self.get_next_card_state(self.c_card_state, self.c_command_code, r3_value)
    self.debug_print(f'@{self.c_time_value} Info::process_response: {self.c_card_state} ==> {next_card_state}')
    self.c_card_state = next_card_state

    return


  ## Handling Command/Response/Data Transactions
  ## Pretty Print a data block
  def pretty_print_data(self, size, data0, data1, data2, data3, crc0, crc1, crc2, crc3):
    if (self.c_data_format == 'WIDE_DATA') and (size == 64):
      self.debug_print(f'  Data     = 0x{self.c_wide_data_read:016x}')
    elif (self.c_data_format == 'WIDE_DATA') and (size == 512):
      self.debug_print(f'  Data     = 0x{self.c_wide_data_read:0128x}')
    elif (self.c_data_format == 'USUAL_DATA') and (size == 512 * 8):
      for i in range(32):
        self.debug_print(f'0x{i<<4:03x}: ', newline=False)
        for j in range(16):
          index = (i <<4) + j 
          self.debug_print(f'{self.c_usual_data_read[index]:02x} ', newline=False)
        self.debug_print("  ", newline=False)
        for j in range(16):
          index = (i << 4) + j
          if (self.c_usual_data_read[index] >= 32) and (self.c_usual_data_read[index] < 127):
            ascii_char = chr(self.c_usual_data_read[index])
          else:
            ascii_char = '.'
          self.debug_print(f'{ascii_char}', newline=False)
        self.debug_print(" ")
    else: 
      self.debug_print(f'Warning::unsupported format {self.c_data_format} and size {size} options')

    if (self.c_data_width == 1):
      self.debug_print(f'  Data0 CRC = 0x{crc0:04x}')
      expected_crc0 = self.compute_crc16(data0, size)
      if (crc0 != expected_crc0):
        self.debug_print(f'@{self.c_time_value} ERROR::pretty_print_data: expected crc0 {expected_crc0:04x} actual {crc0:04x}')
    elif (self.c_data_width == 4):
      self.debug_print(f'  Data0 CRC = 0x{crc0:04x}')
      self.debug_print(f'  Data1 CRC = 0x{crc1:04x}')
      self.debug_print(f'  Data2 CRC = 0x{crc2:04x}')
      self.debug_print(f'  Data3 CRC = 0x{crc3:04x}')
      expected_crc0 = self.compute_crc16(data0, size >> 2)
      expected_crc1 = self.compute_crc16(data1, size >> 2)
      expected_crc2 = self.compute_crc16(data2, size >> 2)
      expected_crc3 = self.compute_crc16(data3, size >> 2)
      #self.debug_print(f'     data0 = {data0:x}')
      #self.debug_print(f'     data1 = {data1:x}')
      #self.debug_print(f'     data2 = {data2:x}')
      #self.debug_print(f'     data3 = {data3:x}')
      if (crc0 != expected_crc0):
        self.debug_print(f'@{self.c_time_value} ERROR::pretty_print_data: expected crc0 {expected_crc0:04x} actual {crc0:04x}')
        #self.debug_print(f'     data0 = {data0:x}')
      if (crc1 != expected_crc1):
        self.debug_print(f'@{self.c_time_value} ERROR::pretty_print_data: expected crc1 {expected_crc1:04x} actual {crc1:04x}')
        #self.debug_print(f'     data1 = {data1:x}')
      if (crc2 != expected_crc2):
        self.debug_print(f'@{self.c_time_value} ERROR::pretty_print_data: expected crc2 {expected_crc2:04x} actual {crc2:04x}')
        #self.debug_print(f'     data2 = {data0:x}')
      if (crc3 != expected_crc3):
        self.debug_print(f'@{self.c_time_value} ERROR::pretty_print_data: expected crc3 {expected_crc3:04x} actual {crc3:04x}')
        #self.debug_print(f'     data3 = {data3:x}')
    else:
      self.debug_print(f'ERROR::pretty_print_data -- unrecoginzed data_widht {self.c_data_width}')

  # take a new bit, or a new nibble, and add it to the appropriate data structure
  def append_new_data(self, data_width, data, bit_count):
    if (self.c_data_format == 'WIDE_DATA'):
      if (data_width == 1):
        self.c_wide_data_read = (self.c_wide_data_read << 1) | data
      elif (data_width == 4):
        self.c_wide_data_read = (self.c_wide_data_read << 4) | data
      else:
        self.debug_print(f'ERROR::append_new_data: unrecognized data width {data_width}')
    elif (self.c_data_format == 'USUAL_DATA'):
      index = bit_count >> 3
      if (data_width == 1):
        self.c_usual_data_read[index] = (self.c_usual_data_read[index] << 1) | data
      elif (data_width == 4):
        self.c_usual_data_read[index] = (self.c_usual_data_read[index] << 4) | data
        #self.debug_print(f'DEBUG::append_new_data: bit_count = {bit_count} index = {index}; data = 0x{data:01x}')
      else:
        self.debug_print(f'ERROR::append_new_data: unrecognized data width {data_width}')
    else:
      self.debug_print(f'ERROR::append_new_data: unrecognized data format {self.c_data_format}')

  def clear_data(self):
    ## canonical data
    self.c_wide_data_read = 0
    for index in range(1024):
      self.c_usual_data_read[index] = 0
    ## Lanewise data
    self.c_data0_read = 0
    self.c_data1_read = 0
    self.c_data2_read = 0
    self.c_data3_read = 0
    ## Lanewise CRC
    self.c_data0_crc = 0
    self.c_data1_crc = 0
    self.c_data2_crc = 0
    self.c_data3_crc = 0

  ## Grab the data bits as they come in off the wire(s)
  def process_data_transfer(self, data3, data2, data1, data0):
    # We have a start bit
    #self.debug_print(f'@{self.c_time_value} debug::process_data_transfer: c_data_state: {self.c_data_state}')
    if (self.c_data_state == 'data_init'):
      data_bits = data0 | (data1 << 1) | (data2 <<2) | (data3 << 3)
      if ((self.c_data_width == 1) and (data0 == 0)) or ((self.c_data_width == 4) and (data_bits == 0)):
        self.debug_print(f'@{self.c_time_value} debug::process_data_transfer: received start bit {data0}; data_bits 0x{data_bits:01x}')
        self.c_data_state = 'data_rcv'
        self.c_data_bit_count = 0
        self.c_data_crc_bit_count = 0
        self.c_data_write_response = 0
        self.c_data_write_bit_count = 0
    elif (self.c_data_state == 'data_rcv'):
      if (self.c_data_width == 1):
        self.c_data0_read =  (self.c_data0_read << 1) | data0
        self.append_new_data(1, data0, self.c_data_bit_count)
        #self.debug_print(f'@{self.c_time_value} debug::process_data_transfer: processing data_bit {self.c_data_size - self.c_data_bit_count - 1} data: {data0}')
        self.c_data_bit_count += 1
      elif (self.c_data_width == 4):
        self.c_data0_read =  (self.c_data0_read << 1) | data0
        self.c_data1_read =  (self.c_data1_read << 1) | data1
        self.c_data2_read =  (self.c_data2_read << 1) | data2
        self.c_data3_read =  (self.c_data3_read << 1) | data3
        data_bits = data0 | (data1 << 1) | (data2 <<2) | (data3 << 3)
        self.append_new_data(4, data_bits, self.c_data_bit_count)
        #self.debug_print(f'@{self.c_time_value} debug::process_data_transfer: processing data_bit {self.c_data_size - self.c_data_bit_count - 1} data: 0x{data_bits:01x} {data3}{data2}{data1}{data0}')
        self.c_data_bit_count += 4
      else:
        self.debug_print(f'@{self.c_time_value} ERROR::process_data_transfer: unrecognized data width {self.c_data_width}')
        self.c_data_state = 'data_error'

      if (self.c_data_bit_count == self.c_data_size):
        if (self.c_data0_crc + self.c_data1_crc + self.c_data2_crc + self.c_data3_crc != 0):
          self.debug_print(f'ERROR::process_data_transfer::per lane crc not initialized')
        self.c_data_state = 'data_crc'
      elif (self.c_data_bit_count > self.c_data_size):
        self.debug_print(f'@{self.c_time_value} ERROR::process_data_transfer: bit count {self.c_data_bit_count} greater than xaction length {self.c_data_size}')
        self.c_data_state = 'data_error'
      else:
        self.c_data_state = 'data_rcv'
    elif (self.c_data_state == 'data_crc'):
      #self.debug_print(f'info::process_data_transfer: processed {self.c_data_crc_bit_count} crc bits')
      # process the CRC
      if (self.c_data_width == 1):
        self.c_data0_crc = (self.c_data0_crc << 1) | data0
        #self.debug_print(f'@{self.c_time_value} debug::process_data_transfer: processing crc_bit {15 - self.c_data_crc_bit_count} data: {data0}')
        self.c_data_crc_bit_count += 1
      elif (self.c_data_width == 4):
        data_bits = data0 | (data1 << 1) | (data2 <<2) | (data3 << 3)
        self.c_data0_crc = (self.c_data0_crc << 1) | data0
        self.c_data1_crc = (self.c_data1_crc << 1) | data1
        self.c_data2_crc = (self.c_data2_crc << 1) | data2
        self.c_data3_crc = (self.c_data3_crc << 1) | data3
        #self.debug_print(f'@{self.c_time_value} debug::process_data_transfer: processing crc_bit {15 - self.c_data_crc_bit_count} data: 0x{data_bits:01x}')
        self.c_data_crc_bit_count += 1
      else:
        self.debug_print(f'@{self.c_time_value} ERROR::process_data_transfer: unrecognized data width {self.c_data_width}')
      if (self.c_data_crc_bit_count == 16):
        self.c_data_state = 'data_end_check'
      if (self.c_data_crc_bit_count > 16):
        self.debug_print(f'@{self.c_time_value} ERROR::process_data_transfer: crc_bit count {self.c_data_crc_bit_count} greater than 16')
        self.c_data_state = 'data_error'
    elif (self.c_data_state == 'data_end_check'):
      data_bits = data0 | (data1 << 1) | (data2 << 2) | (data3 << 3)
      self.debug_print(f'@{self.c_time_value} debug::process_data_transfer: processing last bit {data0} data_bits 0x{data_bits:01x}')
      if ((self.c_data_width == 1) and (data0 == 1)) or ((self.c_data_width == 4) and (data_bits == 0xf)):
        # we've gotten the end bit; time to reset
        self.c_block_device.post_data(self.c_command_name, self.c_read_write_block,  self.c_usual_data_read)
        if (self.c_card_state == 'data'):
            self.c_data_state = 'data_init'
            self.c_card_state = 'tran'
        elif (self.c_card_state == 'rcv'):
            self.c_data_state = 'data_write_response'
            self.c_card__state = 'rcv' 
        else:
            self.c_data_state = 'data_error'
            self.debug_print(f'@{self.c_time_value} ERROR::process_data_transfer: in state {self.c_card_state}, not data or rcv')
        self.pretty_print_data(self.c_data_size,
                               self.c_data0_read, self.c_data1_read, self.c_data2_read, self.c_data3_read,
                               self.c_data0_crc,  self.c_data1_crc,  self.c_data2_crc,  self.c_data3_crc)
        self.clear_data()
      else:
        self.c_data_state = 'data_error'
        self.debug_print(f'@{self.c_time_value} ERROR:process_data_transfer -- did not get end bit')

    elif (self.c_data_state == 'data_write_response'):
        # self.debug_print(f'@{self.c_time_value} debug:process_data_transfer -- data_write_response state, bit count: {self.c_data_write_response_bit_count}  data0: {data0}')
        self.c_data_write_response = (self.c_data_write_response << 1) | data0
        self.c_data_write_response_bit_count += 1
        if (self.c_data_write_response_bit_count == 8):
            # self.debug_print(f'@{self.c_time_value} debug:process_data_transfer -- data_write_response: {self.c_data_write_response:02x}')
            if (self.c_data_write_response != 0xca):
                self.debug_print(f'@{self.c_time_value} ERROR:process_data_transfer -- data_write_response: {self.c_data_write_response:02x} != 0xca')
            self.c_data_state = 'data_write_busy'
        else:
            self.c_data_state = 'data_write_response'
        
    elif (self.c_data_state == 'data_write_busy'):
        if (data0 == 0):
            self.c_data_state = 'data_write_busy'
        else:
            #self.debug_print(f'@{self.c_time_value} debug:process_data_transfer -- data_write_response state, data_busy -> data_write_ready')
            self.c_data_write_response_bit_count = 0
            self.c_data_write_response = 0
            if (self.c_command_name == 'WRITE_BLOCK'):
                self.c_data_state = 'data_init'
                self.c_card_state = 'tran'
            else:
                ## we're in the middle of a block right -- get ready for next block
                self.c_data_state = 'data_write_ready'
                

    elif (self.c_data_state == 'data_write_ready'):
        #self.debug_print(f'@{self.c_time_value} debug:process_data_transfer -- data_write_response state, data_write_ready, card_state = {self.c_card_state}')
        if (self.c_card_state == 'prg'):
            self.debug_print(f'@{self.c_time_value} debug:process_data_transfer -- data_write_response state, data_write_ready -> data_init')
            self.c_card_state = 'tran'
            self.c_data_state = 'data_init'
        else:
            self.c_data_state = 'data_write_ready'
        
    if (self.c_data_state == 'data_error'):
      return


  def getNextState(self, currentState, current_row, next_row, maxDataBytes):
    TimeValue = float(current_row[0])
    D0_Value = int(current_row[1])
    D1_Value = int(current_row[2])
    D2_Value = int(current_row[3])
    D3_Value = int(current_row[4])
    CMD_Value = int(current_row[5])
    CLK_Value = int(current_row[6])

    if (self.c_debug):
      self.debug_print(f'@T={TimeValue} getNextState: current_state: {currentState}, CLK: {CLK_Value}, CMD: {CMD_Value} , D3: {D3_Value}, D2: {D2_Value}, D1: {D1_Value}, D0:{D0_Value}')

    rising_sclk = self.risingCLK(CLK_Value)
    falling_sclk = self.fallingCLK(CLK_Value)
    self.c_last_CLK_Value = CLK_Value

    ## Data transfers
    if ((self.c_card_state == 'data') and rising_sclk):
      #self.debug_print(f'info::getNextState: process_data_transfer data - D3:0 = {D3_Value}{D2_Value}{D1_Value}{D0_Value}')
      self.process_data_transfer(D3_Value, D2_Value, D1_Value, D0_Value)

    if (((self.c_card_state == 'rcv') or (self.c_card_state == 'prg')) and rising_sclk):
      #self.debug_print(f'info::getNextState: process_data_transfer rcv - D3:0 = {D3_Value}{D2_Value}{D1_Value}{D0_Value}')
      self.process_data_transfer(D3_Value, D2_Value, D1_Value, D0_Value)
        

    ## Command and Responses
    if (currentState == 'sd_idle'):
      self.c_bit_count = 0
      if(rising_sclk):
        if (CMD_Value == 0):
          # we have a start bit
          self.c_bit_count += 1
          return  'sd_start'
        else:
          return  'sd_idle'
      else:
        return  'sd_idle'
    if (currentState == 'sd_start'):
      if (rising_sclk):
        self.c_bit_count += 1
        if (CMD_Value == 1):
          # this is a command
          self.c_cmd_value = 1
          return 'sd_cmd'
        else:
          self.c_response_value = 0
          return 'sd_response'
      else:
        return 'sd_start'

    if (currentState == 'sd_cmd'):
      ## We've already gotten a start bit
      if(rising_sclk):
        self.c_cmd_value = (self.c_cmd_value << 1) | CMD_Value
        self.c_bit_count += 1
        if (self.c_bit_count == 48):
          if (CMD_Value != 1):
            self.debug_print(f'@{self.c_time_value} ERROR: get_next_state: last command bit not 1')
          self.process_command(self.c_cmd_value)

          return 'sd_idle'
        else:
          return 'sd_cmd'
      else:
        return  'sd_cmd'

    if (currentState == 'sd_response'):
      if(rising_sclk):
        self.c_response_value = (self.c_response_value << 1) | CMD_Value
        self.c_bit_count += 1
        response_length = self.get_response_length_from_cmd(self.c_cmd_value)
        # self.debug_print(f'   c_reponse_bit_count: {self.c_response_bit_count}, response_length = {response_length}')
        if (self.c_bit_count == response_length):
          if (CMD_Value != 1):
            self.debug_print(f'@{self.c_time_value} ERROR: get_next_state: last response bit not 1')
          self.process_response(self.c_response_value, self.c_response_format)
          if (self.c_command_name == 'VOLTAGE_SWITCH'):
            self.debug_print(f'get_next_state -> moving to sd_voltage_switch')
            return 'sd_voltage_switch'
          else:
            return 'sd_idle'
        else:
          return 'sd_response'

    if (currentState == 'sd_voltage_switch'):
      if(rising_sclk):
        if (D0_Value == 1) or (D1_Value == 1) or (D2_Value == 1) or (D3_Value == 1):
          return ('sd_idle')
        else:
          return ('sd_voltage_switch')
      else:
        return('sd_voltage_switch')


    return currentState

  def parse_sd_la_trace(self, file_path, input_filename, log_filename,
                        maxCommands=10000000, maxDataBytes=8192000,
                        debug_start = 0.0, debug_end =0.0, card_state ='init', data_width = 1):

    currentState = 'sd_idle'
    timeValue = 0.0

        
    full_input_filename = file_path + input_filename
    print("Opening input filename" +  full_input_filename)

    full_log_filename = file_path + log_filename

    self.c_card_state = card_state
    self.c_data_width = data_width
    self.clear_data()


    self.c_exfat_file_system.set_block_device(self.c_block_device)
    
    with open(full_input_filename, newline='') as csvfile:
        with open(full_log_filename, 'w') as logfile:
            self.c_logfile = logfile
            self.c_exfat_file_system.set_log_file(self.c_logfile)
            self.c_block_device.set_log_file(self.c_logfile)
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
                    timeValue = float(current_row[0])
                    self.c_time_value = timeValue
                    nextState = self.getNextState(currentState, current_row, next_row, maxDataBytes)
                    if (nextState != currentState) :
                        if (False and (timeValue > 0.017480835)):
                            print("Aborted -- timeValue exceeded")
                            break;
                        if (False and (nextState == 'sd_idle')):
                            #print("@T=", timeValue, ":" + currentState + "==> " + nextState + " after " + str(self.c_bit_count) + " bits")
                            self.debug_print(f'@T= {timeValue}:')
                        if (True and (timeValue >= 100.0)):
                            self.debug = True
                        if (True and (currentState == 'sd_idle')):
                            self.debug_print(f'@T= {timeValue}:')
                            # print("@T=", timeValue, ":" + currentState + "==> " + nextState)
                        currentState = nextState
                    maxCommands = maxCommands - 1
                    current_row = next_row
                    if (timeValue > debug_start) and (timeValue < debug_end):
                        self.debug = True
                    else:
                        self.debug = False
                if (maxCommands < 0):
                    self.debug_print("Aborted:: maxCommands exceeded");
                    break;
                if (self.c_card_state == '-') and False:
                    self.debug_print("Aborted:: card_state: -")
                    break
                if (self.c_data_state == 'data_error'):
                    self.debug_print("Aborted:: data_state: data_error")
                    break

            self.c_block_device.print_block_device_contents()
            self.c_exfat_file_system.check_file_system()
    
    return



