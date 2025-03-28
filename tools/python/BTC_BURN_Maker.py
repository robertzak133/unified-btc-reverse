import math
import os
import shutil
import numpy as np
import copy

from Struct import Struct
from carve_BTC_BRN import carveBTCBRN
from combineFirmware import combineFirmware
from codePatcher import codePatcher
from BTC_EEPROM_Parser import BTC_EEPROM_Parser

class BTC_BURN_Maker:
    ''' A class for gathering up all the pieces and producing a .BRN file
    '''
    prometheus_trailer_filename = "prometheus_trailer"
    

    default_ref_brn_directory = "/content/drive/MyDrive/local_repositories/BTC-Reverse/targets/btc-7a/created-burn-images/Synthesized-Manufacturer-Baseline/"
    default_ref_brn_filename = "brnbtc70.BRN"
    default_dest_directory = "/content/drive/MyDrive/local_repositories/BTC-Reverse/targets/btc-7a/created-burn-images/HandPatchedExample/"
    default_ref_eeprom_filename = "manufacturer-baseline-BTC-7A_I04030C.bin"
    default_ref_eeprom_dir = "/content/drive/MyDrive/local_repositories/BTC-Reverse/targets/btc-7a/eeprom-images/"

    camera_target = ""
    
    # update the component offsets based on new size information
    def update_sphost_sizes(self, header, size_map):
        root = header.ldata
        # update filesize
        filesize = 0;
        for filename in size_map.keys():
            filesize += size_map[filename]
        root['filesize'] = filesize;
        print(f'Debug::update_sphost_sizes:Updated filesize to 0x{filesize:04x}')
        # update offsets
        offset = size_map['SPHOST.header']; 
        for index in root['offset']:
            offset_name = 'offset' + chr(0x30 + index)
            if (index == 2):
                size = size_map['offset2.header'] + size_map['offset2.A'] + size_map['offset2.B']
            else:
                if (offset_name in size_map):  
                    size = size_map[offset_name]
                    print(f'Debug::offset {offset_name} is in size map -- setting to 0x{size:04x}')
                else:
                    print(f'Debug::offset {offset_name} not in size_map -- setting to zero')
                    size = 0;

            if (size == 0):
                root['offset'][index] = 0
                print(f'Debug::update_sphost_sizes:Updated {offset_name} to 0x0')
            else:
                root['offset'][index] = offset
                print(f'update_sphost_sizes:Updated {offset_name} to 0x{offset:04x}')
                offset += size
                
        return 

    # set the target trail camera
    #   Our growing list of supported camera types
    def set_camera_target(self, target):
        if ((target == 'BTC-7A') or (target == 'BTC-8A') or
            (target == 'BTC-7E') or (target == 'BTC-8E') or
            (target == 'BTC-7E-HP4') or (target == 'BTC-8E-HP4') or
            (target == 'BTC-7E-HP5') or (target == 'BTC-8E-HP5')):
            self.camera_target = target
        else:
            print(f'Error::set_camera_target: unrecognized target device {target}')
        return

    
    # update_filesystem_size
    # Recalculate sizes of filesystems A & B stored in offset2
    def update_filesystem_size(self, header, size_map, index):
        size = size_map['offset2.' + index]
        bytes_per_sector = header.ldata['bytes_per_sector']
        if ((size % bytes_per_sector) != 0):
            print(f'Warning::update_file_system_sizes -- file system {index} size {size} not a multiple of sector size {bytes_per_sector}')
        sectors = math.ceil(size / bytes_per_sector)

        header.ldata['sectors'] = sectors;
        return

    # fprint_sphost_header
    # create a new SPHOST.header, print it to a file
    def fprint_sphost_header(self, header, binary_file, checksum, endianness):
        root = header.ldata
        # write magic sequence
        address = 0;
        magic = root['magic']
        print(f'Debug::fprint_sphost_header:writing magic of {magic} to {address:04x}')
        binary_file.write(magic)
        # write file_length
        address += 16;
        filesize = root['filesize']
        print(f'Debug::fprint_sphost_header:writing filesize of 0x{filesize:04x} to 0x{address:04x}')
        binary_file.write(filesize.to_bytes(4, byteorder = 'little', signed = False))
        address += 4;
        # write offsets
        for index in root['offset']:
            if (index == 0): continue   ## offset0 is assumed
            offset = root['offset'][index]
            print(f'Debug::fprint_sphost_header:writing offset{index} of 0x{offset:04x} to file address 0x{address:04x}')
            binary_file.write(offset.to_bytes(4, byteorder = 'little', signed = False))
            address += 4
        # write crc
        address = root['offset'][0] - 4
        print(f'Debug::fprint_sphost_header:writing checksum of  0x{checksum:08x} to 0x{address:08x}')
        binary_file.seek(root['offset'][0] - 4)

        temp_array = np.array(checksum, dtype='<u4')
        binary_file.write(temp_array.tobytes())
        return

    # utility function.  Does a bytewise xor of the contents of a byte buffer with
    #      argument
    #      (this to duplicate a step in the BURN file creation process 
    def xor_buffer(self, in_buffer, xor_value):
        out_buffer = bytearray(in_buffer)
        for i in range(len(in_buffer)):
            out_buffer[i] = in_buffer[i] ^ xor_value
        return(bytes(out_buffer))

    # fix_offset2_header
    # by this time, assume that offset2.A and .B offsets and sizes are correct
    # but we still need to reflect these sizes in the offset2_header file, otherwise
    # it will not load correctly. 
    def fix_offset2_header(self, offset2_header_filename, a_offset, a_size, b_offset, b_size):
        with open(offset2_header_filename, 'rb+') as f:
            # invert the contents of the file
            buffer = f.read(0x20)
            xored_buffer = self.xor_buffer(f.read(0x100), 0x7a)
  
            offset2header = Struct([
                ('header_string', '16s'),

                ('num_images', '1s'),
                ('header_padding', '15s'),
                ('drive_a_id_string', '20s'),
                ('drive_a_zeros', '92s'),
                ('drive_a_offset', 'I'),
                ('drive_a_size',  'I'),
                ('drive_a_padding', '8s'),
                ('drive_b_id_string', '20s'),
                ('drive_b_zeros', '92s'),
                ('drive_b_offset', 'I'),
                ('drive_b_size',  'I'),
                ('drive_b_padding', '8s')
                ], buffer + xored_buffer)
            #offset2header.pretty_print()
            ##print('Debug::fix_offset2_header:changing values')
            # change values
            offset2header.ldata['drive_a_offset'] = a_offset
            offset2header.ldata['drive_a_size'] = a_size
            offset2header.ldata['drive_b_offset'] = b_offset
            offset2header.ldata['drive_b_size'] = b_size
            ##print("Debug::fix_offset2_header:---------------------")
            ##offset2header.pretty_print()
            ##print("Debug::fix_offset2_header:---------------------")
            buffer = offset2header.pack_to_buffer()
            xored_buffer = self.xor_buffer(buffer[0x20:], 0x7a)
            f.seek(0)
            f.write(buffer[0:0x20])
            f.write(xored_buffer)
        return

    def create_prometheus_trailer(self, dest_directory):
	## Creates a file with the right string in it to pass
	## firmware laod consistancey checks
	## this file is concatenated to the end of the "standard"
	## .brn file
        if self.camera_target == 'BTC-7A' :
            magic_string = 'Prometheus3BTC70'
        elif self.camera_target == 'BTC-8A':
            magic_string = 'Prometheus3BTC80'
        elif self.camera_target == 'BTC-7E':
            magic_string = 'Prometheus5BTC70'
        elif self.camera_target == 'BTC-8E':
            magic_string = 'Prometheus5BTC80'
        elif self.camera_target == 'BTC-7E-HP4':
            magic_string = 'Prometheus5BTC71'
        elif self.camera_target == 'BTC-8E-HP4':
            magic_string = 'Prometheus5BTC81'
        elif self.camera_target == 'BTC-7E-HP5':
            magic_string = 'Prometheus5BTC72'
        elif self.camera_target == 'BTC-8E-HP5':
            magic_string = 'Prometheus5BTC82'
        else:
            print(f'Error::create_prometheus_trailer: unrecognized target device {self.camera_target}')
            magic_string = ''

        prometheus_filename = os.path.join(dest_directory, self.prometheus_trailer_filename)
	
        with open(prometheus_filename, "wb") as fp :
            fp.write(bytes(magic_string, 'utf-8'))
        return
	
    ## Copy over file system images
    def copy_file_system_image(self, fs_directory_name, dest_directory, fs_name):
        if not fs_directory_name:
            return
    
        src_filename = fs_directory_name
        dest_filename = os.path.join(dest_directory, fs_name)
        src_size = os.stat(src_filename).st_size
        dest_size = os.stat(dest_filename).st_size
        if (src_size != dest_size):
            ## 2025-02-02: Zak -- convert this to a warning (from an error).  In the case of the BTC-7A hack, I'm stealing
            ##             the A: and B: file systems from the BTC-7E, which has a different (smaller) 
            print(f'Warning: copy_file_system_images -- {fs_name} src size {src_size} not equal to dest size {dest_size}')
        shutil.copy(src_filename, dest_filename)

        return

    ## Checksum Utilities

    # Calculate checksum of a single file
    #   if buffer_size == -1; checksum the whole file
    #      else Only calculate first buffer_size bytes, 
    def calculate_file_checksum(self, filename, buffer_size=-1):
        checksum = 0

        if (buffer_size == -1):
            file_size = os.path.getsize(filename)
        else:
            file_size = file_len
            
        if (file_size %4) != 0:
            print(f'File {filename} length is {file_size}')
            padded_filename = filename + ".padded"
            shutil.copy(filename, padded_filename)
            with open(padded_filename, 'rb+') as fptr:
                fptr.seek(0,2)
                for i in range(0, 4 - file_size%4):
                    fptr.write(b'\x00')
                    print(f'{i} writing 0x00')
                    pfile_size = os.path.getsize(padded_filename)
                    print(f'File {padded_filename} length is {pfile_size}')
                    file_size = pfile_size
                    adjusted_filename = padded_filename
        else:
            adjusted_filename = filename

        with open (adjusted_filename, 'rb') as fptr:
            array_of_ints = np.fromfile(fptr, dtype='<u4')

        checksum = np.sum(array_of_ints, dtype='<u4')
        num_elements = len(array_of_ints)
        print(f'Checksum for {filename} is {checksum:08X}; FileSize = {file_size} Num elements = {num_elements}; Size/4 = {file_size/4}')
        return checksum

    # Calculate Checksum of a list of files
    def calculate_file_list_checksum(self, directory, file_list):
        print(f'Debug:: calculate_file_list_checksum: {file_list}')
        list_checksum = 0;
        offset_dict = {}
        for file in file_list:
            file_checksum = self.calculate_file_checksum(directory + file)
            offset_dict[file] = file_checksum
            list_checksum = np.add(list_checksum, file_checksum, dtype='u4')
        print(f'File List Checksum is {list_checksum:08X}')
        return list_checksum

    ## The Main Event
    def make_burn_file(self, size_files=None,
                       target='BTC-7A',
                       ref_brn_directory=None, ref_brn_filename=None, dest_directory=None, 
                       dest_file=None, ref_eeprom_directory=None, ref_eeprom_filename=None,
                       fsa_directory_name=None, fsb_directory_name=None, list_of_patch_lists=None, patch_directory=None,
		       list_of_patch_bases=None, command_file_base="general", cmd_directory=None,
		       offset2a_source='HAND_PATCH', offset2b_source='BRN_FILE'
                       ):
        '''Combine offset components into a single firmware file
        Parameters
        ----------
        size_files: list(str)
            List of chunks that go into the "size" field in the header
        target: str
            Target for firmware, defaults to 'BTC-7A'
        ref_brn_directory : str 
            Directory where the refernce copy of chunks are located
        ref_brn_filename: str
	    Name of file with the BRN file to use as a reference in creating new brn file
        dest_directory : str
            Directory to put the resulting, modified chunks
        dest_file : str
            Name of resulting .BRN file
        ref_eeprom_directory : str
	    Location of an EEPROM image to grab binary data from
        ref_eeprom_filenamename : str
            Name of EEPROM binary image
        fsa_directory_name : str
	    Name of directory and file containing a modified file system image
        fsb_directory_name : str
	    Name of directory and file containing a modified file system image
        list_of_patch_lists : list of str
	    a list of hand patch lists
        patch_directory : str
	    Name of directory containing patches
        cmd_directory : str
            Name of direcotry containing Ghidra-generated .cmd file with symbol locations
        command_file_base : .cmd file generated by  ghidra
        list_of_patch_bases : a list of root names for source-based patch files
        offset2a_source : specifies where to get the A file system from.  Defaults to "BRN_FILE"
            Which is directly from the factory firmware image; the "HAND_PATCH" option selects
            a file system which has been hand-modified for new content (e.g. new images, or new
            string files)
        offset2b_source : specifies where to get the B file system from.  Defaults to "BRN_FILE"
            Which is directly from the factory firmware image; the "HAND_PATCH" option selects
            a file system which has been hand-modified for new content or size
            string files)
        '''
        self.set_camera_target(target);

        # Don't count the "prometheus" file when calculating file sizes
        if (self.camera_target == 'BTC-7A') or \
	   (self.camera_target == 'BTC-7E') or (self.camera_target == 'BTC-8E') or \
           (self.camera_target == 'BTC-7E-HP4') or (self.camera_target == 'BTC-8E-HP4'):
            size_files = ["SPHOST.header", "offset0", "offset1", "offset2.header", "offset2.A",
			  "offset2.B", "offset3", "offset5"]
                
        else:
            size_files = ["SPHOST.header", "offset0", "offset1", "offset2.header", "offset2.A",
                              "offset2.B", "offset3", "offset5", "offset6"]
                

        # Do include prometheus_trailer in the list of all the files that
        # go into the final .BRN file
        all_files = size_files.copy()
        all_files.append(self.prometheus_trailer_filename)

        if not ref_brn_directory:
            ref_brn_directory = self.default_ref_brn_directory

        # Do nothing if ref_brn_directory not valid
        if not os.path.isdir(ref_brn_directory):
            print(f'Error::combine_firmware -- ref_brn_directory: {ref_brn_directory} not valid') 
            return

        if not dest_directory:
            dest_directory = self.default_dest_directory
        # Do nothing if directory or outfile are not valid
        if not os.path.isdir(dest_directory):
            print(f"Error::combine_firmware -- dest_directory not valid: {dest_directory}") 
            return

        if not ref_eeprom_directory:
            ref_eeprom_directory = self.default_eeprom_dir

        if not ref_eeprom_filename:
            ref_eeprom_filename = self.default_eeprom_filename

        # Get the baseline brn image

        if not ref_brn_filename:
            ref_brn_filename = self.default_ref_brn_filename

        brn_filename = os.path.join(ref_brn_directory, ref_brn_filename)

        # Create a the promethues_trailer in the dest directory
        self.create_prometheus_trailer(dest_directory)

        # Carve an image from the ref_brn_directory into the destination directory
        # Do this before extracting files from EEPROM so they overwrite
        brn_carver = carveBTCBRN()
        brn_carver.carve_firmware(FILENAME=brn_filename, out_directory=dest_directory)

        # Option to get the the A-file system (contained in offset 2) from the eeprom
        # file.  This is only required if adding files via PowerISO doesn't work
        if (offset2a_source == 'EEPROM'):
            # Get the EEPROM data (this will overwrite some files, above)
            eeprom_parser = BTC_EEPROM_Parser()
            eeprom_parser.set_segment_properties(self.camera_target)
            eeprom_parser.update_all_eeprom_files(EEPROM_FILE=ref_eeprom_filename ,EEPROM_DIR=ref_eeprom_directory,
                                                  OFFSET_DIR=dest_directory)
        elif (offset2a_source == 'BRN_FILE'):
            # we don't need to do anything
            print("Info::make_burn_file:getting A file system from BRN File");
        elif (offset2a_source == 'HAND_PATCH'):
            print(f"Info::make_burn_file: getting A file system from {fsa_directory_name}")
            self.copy_file_system_image(fsa_directory_name, dest_directory, 'offset2.A')
        else:
            print(f"Error::make_burn_file: unrecognized offset2a_source: {offset2a_source}")

	# Option to get the B-File system (contained in offset 2) directly from the .BRN file
        if (offset2b_source == 'BRN_FILE'):
            # we don't need to do anything
            print("Info::make_burn_file:getting B file system from BRN File");
        elif (offset2b_source == 'HAND_PATCH'):
            print(f"Info::make_burn_file: getting A file system from {fsb_directory_name}")
            self.copy_file_system_image(fsb_directory_name, dest_directory, 'offset2.B')
        else:
            print(f"Error::make_burn_file: unrecognized offset2b_source: {offset2b_source}")

        # Rewrite offset2.header
        # Handle Patches
        patcher = codePatcher()
        # now -- time to patch the offset3 (application binary) file

        patcher.init_dicts()

        # First, any hand patches
	# 2023-02-07 -- because I modify the dictionaries as I process them, I need to
	#   create a deep copy for every camera_target
        if list_of_patch_lists:
            for patch_list in list_of_patch_lists:
                print(f'Info::make_burn_file: adding patch_list: {patch_list.keys()}')
                patch_list_copy = copy.deepcopy(patch_list)
                patcher.add_to_internal_patch_list(patch_list_copy)
            
        # Second, any compiled patches
        if cmd_directory:
            patcher.set_cmd_symbol_table(cmd_directory, command_file_base)

        if patch_directory: 
            if list_of_patch_bases:
                for patch_base in list_of_patch_bases:
                    entry_offset_filename = command_file_base + '.entry'
                    new_bytes_filename = patch_base + '.bytes'
                    old_bytes_filename = command_file_base + '.old-bytes'
                    patcher.add_bytes_file_to_patch_list(patch_base, cmd_directory, new_bytes_filename, old_bytes_filename, entry_offset_filename)
                    patcher.set_obj_symbol_table(cmd_directory, patch_base)

        # If any patches, apply them!
        if patch_directory:
            file_to_patch_filename = os.path.join(dest_directory, 'offset3')
            patcher.patch_binary(file_to_patch_filename, self.camera_target)

        SPHOST_FAT_INDEX = 2
        SPHOST_FAT_HEADER = 0x120
        # Read and parse all the headers SPHOST.BRN header
        with open(brn_filename, 'rb') as f:
            header = Struct([
                ('magic', '16s'),
                ('filesize', 'I'),
                ('offset', [
                    (0, 0x200),
                    (1, 'I'),
                    (2, 'I'),
                    (3, 'I'),
                    (4, 'I'),
                    (5, 'I'),
                    (6, 'I')
                    ]),
                ('crc', 'I')
                ], f.read(0x200))
        ##print("Debug::make_burn_file:Baseline SPHOST Structure")
        ##print(header.ldata)
        ##header.pretty_print()
        ##print('Debug::make_burn_file:-----------------------')
        # Loop over files to get their sizes
        size_map = {}
        total_size = 0;
        for filename in size_files:
            long_filename = os.path.join(dest_directory, filename)
            try:
                # Copy file contents to firmware file
                with open(long_filename, 'rb') as infile:
                    size = os.path.getsize(long_filename)
                    print(f'Debug::make_burn_file:{filename} size is 0x{size:04x}')
                    size_map[filename] = size
                    total_size += size
            except FileNotFoundError:
                print(f'Error::make_burn_file:File {filename} not found.')
                break
    
        print(f'Debug::make_burn_file:Total size is 0x{total_size:04x}')

        self.update_sphost_sizes(header, size_map)
        print("Debug::make_burn_file:Updated SPHOST Structure")
        header.pretty_print()

        # fix up the offset2.header file with actual sizes of the A and B images
        ##print(f'Debug::make_burn_file:header.ldata[keys] = {header.ldata.keys()}')
        filename = os.path.join(dest_directory, "offset2.header")
        a_size = size_map['offset2.A']
        a_offset = header.ldata['offset'][2] + size_map['offset2.header']
        b_size = size_map['offset2.B']
        b_offset = a_offset + a_size
        self.fix_offset2_header(filename, a_offset, a_size, b_offset, b_size)

        # build the SPHOST.header file -- this is the last thing we do
        #     because we must have all the other files to calculate the
        #     proper checksum
        filename = os.path.join(dest_directory, "SPHOST.header")
        checksum = 0x0; # first write it out with no checksum
        with open(filename, 'wb') as header_file:
            self.fprint_sphost_header(header, header_file, checksum, '<')

        # now calculate the checksum of all the files
        if (self.camera_target == 'BTC-7A') or \
           (self.camera_target == 'BTC-7E') or (self.camera_target == 'BTC-8E') or \
           (self.camera_target == 'BTC-7E-HP4') or (self.camera_target == 'BTC-8E-HP4'):
            file_list = [ "offset0", "offset1", "offset2.A", "offset2.B", "offset2.header",
                          "offset3", "offset5", "SPHOST.header"]
        else:
            file_list = [ "offset0", "offset1", "offset2.A", "offset2.B", "offset2.header",
                          "offset3", "offset5", "offset6", "SPHOST.header"]
        total_checksum = self.calculate_file_list_checksum(dest_directory, file_list) 

        checksum = np.subtract(0, total_checksum, dtype='u4')
        # now write the file with the new checksum
        with open(filename, 'wb') as header_file:
            self.fprint_sphost_header(header, header_file, checksum, '<')
        # And do a sanity check
        total_checksum = self.calculate_file_list_checksum(dest_directory, file_list)
        if (total_checksum != 0):
            print(f'Error::make_burn_file:: total_checksum is {total_checksum:08x}; should be 0x0')
        

        # Combine files into a bundle
        brn_file = os.path.join(dest_directory, dest_file)
        brn_combiner = combineFirmware()
        ##print(f'Debug::make_burn_file:debug::combine_firmware: brn_file = {brn_file}')
        print(f'Debug::make_burn_file:debug::combine_firmware: all_files = {all_files}')
        brn_combiner.combine_firmware(outfile=brn_file, files=all_files, directory=dest_directory)
  
        print('Done!')
        return
