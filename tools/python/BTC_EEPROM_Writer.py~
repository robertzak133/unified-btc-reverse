from Struct import Struct

class BTC_EEPROM_Writer:
    ''' Class for writing binary information inot BTC EEPROM binary file
    these include:
	the dram parameter block (offset 6)
	the default application (offset 3)
	the A and B local file systems
    Writes the data from EEPROM into offset{6,3, 2.A, 2.B, 1} files
    '''

    ### Take the binary pieces and put them together into an eeprom image
    def write_eeprom_binary(self, eeprom_in_filename, offset_directory, eeprom_out_filename, camera_type):
      ## Let's assume that we know the structure of the .BRN file segments
      dram_par_filename = offset_directory + "offset6"
      app_filename = offset_directory + "offset3"
      file_systemA_filename = offset_directory + "offset2.A"
      file_systemB_filename = offset_directory + "offset2.B"
      ##offset1_filename = offset_directory + "offset1"
      ## Fill up the EEPROM with binary data from teh offset files
      with open(eeprom_out_filename, 'wb+') as epo_file:
        ## write the eeprom
        dram_offset, app_offset, fsa_offset, fsb_offset = self.write_eeprom_header(eeprom_in_filename, epo_file, camera_type)
        ## now the dram segment
        self.write_segment(dram_offset, dram_par_filename, epo_file)
        ## then the code
        print(f'info::write_eeprom_binary: writing app from {app_filename} to address 0x{app_offset:08x}')
        self.write_segment(app_offset, app_filename, epo_file)
        ## file system a
        print(f'info::write_eeprom_binary: writing a file system from {file_systemA_filename} to address 0x{fsa_offset:08x}')
        self.write_segment(fsa_offset, file_systemA_filename, epo_file)
        ## file system b
        print(f'info::write_eeprom_binary: writing b file system from {file_systemB_filename} to address 0x{fsb_offset:08x}')
        self.write_segment(fsb_offset, file_systemB_filename, epo_file)
        
            
      return


    ### write the eeprom header
    def write_eeprom_header(self, eeprom_input_filename, epo_file_ptr, camera_type):
        eeprom_header_length = 0x3000
        with open(eeprom_input_filename, 'rb') as epi_file:
          print(f'eeprom_header_length = {eeprom_header_length}')
          epi_file.seek(0) 
          eeprom_header = epi_file.read(eeprom_header_length)
          epo_file_ptr.write(eeprom_header)
          ## patch up the device id
          device_id_offset = 0x40
          device_id = bytearray([0x18, 0x20, 0xc2, 0x00])
          epo_file_ptr.seek(device_id_offset)
          epo_file_ptr.write(device_id)
          ## parse the header to figure out where the segments go
          epo_file_ptr.seek(0,2)
          print(f'eeprom output filelen = {epo_file_ptr.tell()}')
          ## hardwire these for now
          dram_par_offset = 0x100
          if (camera_type == 'BTC-7E-HP5') or (camera_type == 'BTC-8E-HP5'):
            app_offset = 0x3000 
            fsa_offset  = 0x744000
            fsb_offset  = 0x7F6000
          elif (camera_type == 'BTC-7E-HP4') or (camera_type == 'BTC-8E-HP4'):
            app_offset = 0x3000 
            fsa_offset  = 0x680000
            fsb_offset  = 0x7e0000
          elif (camera_type == 'BTC-7E') or (camera_type == 'BTC-8E'):
            app_offset = 0x3000 
            fsa_offset  = 0x680000
            fsb_offset  = 0x7e0000
          elif (camera_type == 'BTC-7A') or (camera_type == 'BTC-8A'):
            app_offset = 0x303000
            fsa_offset = 0x3000
            fsb_offset = 0x283000
          else:
            print(f'write_eeprom_header::Error -- unrecognized camera {camera_type}')
            
        return dram_par_offset, app_offset, fsa_offset, fsb_offset

    def write_segment(self, offset, input_filename, epo_file_ptr):
        ## seek to offset
        epo_file_ptr.seek(offset);
        try:
          with open (input_filename, 'rb') as input_fptr:
            segment_data = input_fptr.read(-1) ## read it all
            print(f'info::write_segment: writing {len(segment_data)} bytes to offset 0x{offset:08x}')
            epo_file_ptr.write(segment_data)
        except:
          print(f'warning::write_segment -- ignoring filename {input_filename}')
        return
