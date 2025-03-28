import struct 
import snappy

class SST_Parser: 
    ''' Class for parsing and updating iCatchTeck SST file formats
    '''
    chunk_dict = {}

    riff_string = ''
    spst_string = ''
    sunplus_string = ''
    snappy_string = ''
    debug = False
    ##debug = True

    uncompressed_bytes = 0
    unknown = 0
    size_in_short = 0
    num_chunks = 0
    trailer = ''

    def init_chunk_dict(self):
        self.uncompressed_bytes = 0
        self.unknown = 0
        self.size_in_short = 0
        self.num_chunks = 0
        self.trailer = bytes()
        self.chunk_dict = {}
        return 

    def add_chunks_to_sst(self, ascii_string_list, infile, outfile):
        ## Initialize the chunk dictionary
        self.init_chunk_dict()
        ## load the chunk table from the file contents
        self.parse_sst_file(infile)
        chunk_id = self.num_chunks
        if self.debug:
            print(f'info::add_chunks_to_sst -- starting at chunk {chunk_id:02x}')
        ## add a new entries to the chunk table
        for ascii_string in ascii_string_list:
            utf_string = ascii_string.encode('utf_16_le')
            if self.debug:
                print(f'add_chunk_to_sst::ascii string = {ascii_string}; utf_string = {utf_string}')
            len_utf_string = len(utf_string)
            self.chunk_dict[chunk_id] = [len_utf_string, utf_string]
            chunk_id += 1
            self.num_chunks += 1
            self.uncompressed_bytes += 4 + (len_utf_string * 2)
        ## write out the new file from the chunk table
        self.write_sst_file(outfile)
        ## keep track of the number of used chunks
        self.num_chunks -= 1
        return

    def read_header(self, sstf):
        self.riff_string = sstf.read(8)
        self.spst_string = sstf.read(12)
        self.sunplus_string = sstf.read(18)

        self.uncompressed_bytes = int.from_bytes(sstf.read(4), byteorder='little')
        self.unknown = int.from_bytes(sstf.read(2), byteorder= 'little')
        self.size_in_short = int.from_bytes(sstf.read(2), byteorder= 'little')
        self.num_chunks = int.from_bytes(sstf.read(2), byteorder= 'little')

        if self.debug:
            print(f'riff_string: {self.riff_string}')
            print(f'spst_string: {self.spst_string}')
            print(f'sunplus_string = {self.sunplus_string}')
            print(f'uncompressed_bytes: 0x{self.uncompressed_bytes:08x}')
            print(f'unknown : 0x{self.unknown:04x}')
            print(f'size_in_short: 0x{self.size_in_short:04x}')
            print(f'num_chunks: 0x{self.num_chunks:04x}')
        return

    def read_snap(self, sstf):
        snappy_string = sstf.read(4)
        if self.debug:
            print(f'snappy_string: {snappy_string}')
        if (snappy_string == b'SNAP'):
            if self.debug:
                print("SNAPPY!")
            self.snappy_string = bytes('SNAP', 'utf-8')
            buffer = sstf.read(-1)
            buffer = snappy.decompress(buffer)
        else:
            self.snappy_string = bytes()
            sstf.seek(-4,1)
            buffer = sstf.read(-1)
        return buffer

    def read_next_chunk(self, sstf):
        chunk_id = int.from_bytes(sstf.read(2), byteorder='little')
        chunk_length = int.from_bytes(sstf.read(2), byteorder='little')
        chunk =sstf.read(chunk_length)
        decoded_chunk = chunk.decode("utf-16")

        ##print(f'read_next_chunk::chunk_id: {chunk_id:04x}')
        if (chunk_id <0):
            print('read_next_chunk::no chunk_id')
            return False
        if chunk_id >= self.num_chunks - 1 :
            if self.debug:
                print(f'[0x{chunk_id:04x}]:[0x{chunk_length:04x}]: {decoded_chunk}')
                print(f'read_next_chunk::chunk_id 0x{chunk_id:04x} greater equal than 0x{self.num_chunks:04x}')
            if (chunk_length > 0):
                self.chunk_dict[chunk_id] = [chunk_length, chunk]
            else:
                self.chunk_dict[chunk_id] = [chunk_length]   
            return False
        if self.debug:
            print(f'[0x{chunk_id:04x}]:[0x{chunk_length:04x}]: {decoded_chunk}')
        if (chunk_length > 0):
            self.chunk_dict[chunk_id] = [chunk_length, chunk]
        else:
            self.chunk_dict[chunk_id] = [chunk_length]   
        return True

    def read_trailer(self, sstf):
        if self.debug:
            print(f'Reading Trailer')
        self.trailer = sstf.read(44)
        if self.debug:
            print(f'read_trailer::trailer: {self.trailer}')
        return

    ## Parse a given sst file
    ##    uncompress the copressed parts
    ##    build the chunk dict
    ## 
    def parse_sst_file(self, filename):
        buffer = ''
        if self.debug:
            print(f'Opening {filename}')

        with open(filename, 'rb') as sstf:
            self.read_header(sstf)
            buffer = self.read_snap(sstf)

            temp_filename = filename + '.UNC'
            with open(temp_filename, 'wb') as sstf:
                if self.debug:
                    print(f'Writing file: {temp_filename}')
                sstf.write(buffer)

        with open(temp_filename, 'rb') as sstf:
            if self.debug:
                print(f'Reading file: {temp_filename}')
            while(self.read_next_chunk(sstf)):
                continue
            ##sstf.seek(-44, 2)
            ##self.read_trailer(sstf)
        return 

    def write_header(self, sstf):
        if self.debug:
            print('write_header - s')
        sstf.write(self.riff_string)
        sstf.write(self.spst_string)
        sstf.write(self.sunplus_string)

        sstf.write(self.uncompressed_bytes.to_bytes(4, 'little'))
        sstf.write(self.unknown.to_bytes(2, 'little'))
        sstf.write(self.size_in_short.to_bytes(2, 'little'))
        sstf.write(self.num_chunks.to_bytes(2, 'little'))

        if self.debug:
            print(f'  uncompressed_bytes {self.uncompressed_bytes:04x}')
            print(f'  unknown {self.unknown:04x}')
            print(f'  size_in_short {self.size_in_short}')
            print(f'  num_chunks {self.num_chunks:04x}')

        sstf.write(self.snappy_string)
        return

    def write_compressed_chunks(self, sstf):
        if self.debug:
            print('write_compressed_chunks - s')
        buffer = bytearray()
        for key in self.chunk_dict:
            chunk_id = key
            chunk_size = self.chunk_dict[key][0]
            if (chunk_size > 0):
                if self.debug:
                    print(f'[{chunk_id:04x}][{chunk_size:04x}] {self.chunk_dict[key][1]}')
                buffer += chunk_id.to_bytes(2,'little')
                buffer += chunk_size.to_bytes(2, 'little')
                buffer += self.chunk_dict[key][1]
            else:
                if self.debug:
                    print(f'[{chunk_id:04x}][{chunk_size:04x}]')
                chunk_id_bytes = int(chunk_id).to_bytes(2, 'little')
                chunk_size_bytes = int(chunk_size).to_bytes(2, 'little')
                buffer += chunk_id.to_bytes(2, 'little')
                buffer += chunk_size.to_bytes(2, 'little')

        if self.debug:  
            print(f'write_compressed_chunks: uncompressed_buffer = {buffer}')
        compressed_buffer = snappy.compress(buffer)
        if self.debug:  
            print(f'write_compressed_chunks: compressed_buffer = {compressed_buffer}')
        uncompressed_buffer = snappy.uncompress(compressed_buffer)
        if self.debug:  
            print(f'write_compressed_chunks: uncompressed_buffer = {uncompressed_buffer}')
        if (buffer != uncompressed_buffer):
            print(f'write_compressed_chunks -- error -- inconsistent compression buffer')

        sstf.write(compressed_buffer)
        return

    def write_trailer(self, sstf):
        sstf.write(self.trailer)
        return 

    def write_sst_file(self, filename):
        if self.debug:
            print(f'write_sst_file:: {filename}')
        with open(filename, 'wb') as sstf:
            self.write_header(sstf)
            self.write_compressed_chunks(sstf)
            self.write_trailer(sstf)
        return

    def print_language_strings(self, chunk_id, directory, file_list):
        print(f'print_language_strings')
        for file in file_list: 
            self.init_chunk_dict()
            self.parse_sst_file(directory + file)
            string = self.chunk_dict[chunk_id][1]
            decoded_string = string.decode("utf-16")
            print(f'  {file} : {decoded_string}')
        return

    def generate_language_files(self, src_directory, dest_directory, language_file_dict):
        ##self.debug = True
        for language_file in language_file_dict:
            if self.debug:
                print(f"Generating {language_file}")
            ascii_string_list = language_file_dict[language_file]
            src_filename = src_directory + language_file
            dest_filename = dest_directory + language_file
            self.init_chunk_dict()
            self.add_chunks_to_sst(ascii_string_list, src_filename, dest_filename)
        return

    ## write the preamble to our include file
    def get_include_preamble(self, include_f):
        lines = []
        lines.append("// SST String Include file\n");
        lines.append("//    Automatically generated file\n");
        lines.append("//    Includes an enum for naming language specific strings\n")
        lines.append("//\n") 
        return lines

    def generate_enum_lines(self, target, target_list, tool_dir):
        enum_dict = {}
        if 'Strings' in target_list[target]:
            enum_lines = ['typedef enum enum_sst_string {\n']

            target_dir = target_list[target]['Target Directory']
            compressed_filename = tool_dir + "targets/" + target_dir + "/file-system-additions/LanguageSSTFiles/ENGLISH.SST"

            self.init_chunk_dict()
            self.parse_sst_file(compressed_filename)
            index = 0
            for chunk_id in self.chunk_dict:
                decoded_string = ''
                if self.debug:
                    print(f'debug::generate_enum_lines -- chunk_id = {chunk_id:02x}')
                string_length = self.chunk_dict[chunk_id][0]
                if (string_length > 0): 
                    string = self.chunk_dict[chunk_id][1]
                    utf16_string = string.decode(encoding="UTF-16")
                    #print(f'debug::generate_enum_lines: utf16_string = {utf16_string}')
                    decoded_bytes = utf16_string.encode(encoding="ASCII", errors="replace")
                else:
                    utf8_string = "EMPTY_STRING_"
                    #print(f'debug::generate_enum_lines: utf8_string = {utf8_string}')
                    decoded_bytes = utf8_string.encode(encoding="ASCII", errors="replace")

                #print(f'debug::generate_enum_lines: decoded_bytes = {decoded_bytes}')
                decoded_bytes = decoded_bytes.replace(b' ', b'_SP_')
                decoded_bytes = decoded_bytes.replace(b'-', b'_DASH_')
                decoded_bytes = decoded_bytes.replace(b'/', b'_SLASH_')
                decoded_bytes = decoded_bytes.replace(b'.', b'_DOT_')
                decoded_bytes = decoded_bytes.replace(b'%', b'_PERCENT_')
                decoded_bytes = decoded_bytes.replace(b'!', b'_EXCLAMATION_')
                decoded_bytes = decoded_bytes.replace(b'?', b'_QM_')
                decoded_bytes = decoded_bytes.replace(b':', b'_COLON_')
                decoded_bytes = decoded_bytes.replace(b'<', b'_LT_')
                decoded_bytes = decoded_bytes.replace(b'>', b'_GT_')
                decoded_bytes = decoded_bytes.replace(b'[', b'_LB_')
                decoded_bytes = decoded_bytes.replace(b']', b'_RB_')
                decoded_bytes = decoded_bytes.replace(b'+', b'_PLUS_')

                key_string = str(decoded_bytes, 'ASCII')

                ## Check for duplicates, and uniquify them
                kindex = 0;
                while (key_string in enum_dict):
                    key_string = key_string + str(kindex)
                    if (kindex > 10):
                        print(f'Error::generate_enum_lines -- exceeded unique limit on key {key_string}')
                        break;
                    kindex += 1
                enum_dict[key_string] = chunk_id
                
                if (index == 0):
                    decoded_string = '   SST_' + key_string + ' = ' + str(chunk_id)
                else:
                    decoded_string = ',\n   SST_' + key_string  + ' = ' + str(chunk_id)

                if self.debug:
                    print(f'debug::generate_enum_lines:: decoded_string = {decoded_string}')

                enum_lines.append(decoded_string)
                index += 1

            enum_lines.append('\n} enum_sst_string;\n') 
        else:
            enum_lines = ['// No SST Files for this Target\n']

        return enum_lines
    
    ## automatically generate an include file 
    def generate_include_file(self, target_list, tool_dir, include_filename):
        with open(include_filename, 'w') as include_f:
            index = 0

            include_f.writelines(self.get_include_preamble(include_f))
            for target in target_list:
                lines = []

                target_underline = target.replace('-', '_')
                if (index == 0):
                    lines.append('#if (defined ' + target_underline + ')\n')
                else:
                    lines.append('#elif (defined ' + target_underline + ')\n')

                include_f.writelines(lines)
                enum_lines = self.generate_enum_lines(target, target_list, tool_dir)
                include_f.writelines(enum_lines)
                index += 1

            lines = ['#endif']
            include_f.writelines(lines)
        return

