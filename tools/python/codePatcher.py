import os

class codePatcher:
    '''
    A class to apply patches from a patch list to a given binary file
    patch list  contains:
	'start_offset' -- relative to the start of program memory (e.g. 0x80000000)
	'change_from_bytes'  -- an array of bytes we expect to find at the given offset
	'change_from_jump'  -- a jump type {j, jal}, with target symbol
	'change_from_ptr'   -- a pointer with a symbolic value
        'change_from_ptr_hi -- high 2-byte of pointer with symbolic valuue
        'change_from_ptr_lo -- low 2-byte of pointer with symbolic valuue
	'change_to_bytes'    -- an array of bytes we will replace what's there with
        'change_to_jump'    -- a jump type {j, jal}, with target symbol
	'change_to_ptr'     -- a new pointer with a symbolic value
        'change_to_ptr_hi -- a new top two bytes of a pointer
        'change_to_ptr_lo -- a new bottom two bytes of a pointer
    '''

    # Debug Switch
    debug = False
    #debug = True
    
    # Data structure to accumulate patches
    internal_patch_list = {}

    # String containing active cmd file (used to dereference symbols)
    symbol_table = {}

    # Register Table
    register_table = {"zero": 0,
                      "at": 1,
                      "v0": 2, "v1": 3,
                      "a0": 4, "a1": 5, "a2": 6, "a3": 7,
                      "t0": 8, "t1": 9, "t2": 10, "t3": 11, "t4": 12, "t5": 13, "t6": 14, "t7": 15,
                      "t8": 24, "t9": 25,
                      "s0": 16, "s1": 17, "s2": 18, "s3": 19, "s4": 20, "s5": 21, "s6": 22, "s7": 23,
                      "k0": 26, "k1": 27,
                      "gp": 28, "sp": 29, "fp": 30, "ra": 31}
                      
    # Entry Address
    entry_address = "uninitialized"


    #
    # Dictionaries are somehow class owned (and not instance owned)
    #   this function allows us to explicitly clear them out
    #
    def init_dicts(self):
        self.internal_patch_list = {}
        self.symbol_table = {}
        return

    # Check to see whether keys in a given dict are unique
    def check_for_uniqueness(self, patch_name, patch_dict, key):
        equivalence_list = [['BTC-7A', 'BTC-8E', 'BTC-7E'],
                            ['BTC-8E-HP4', 'BTC-7E-HP4'],
                            ['BTC-8E-HP5', 'BTC-7E-HP5']]
        if key in patch_dict:
            dict_or_value = patch_dict[key]
            if (type(dict_or_value) is dict):
                family_value_dict = {}
                # first check to see that all the targets in a family list have the same value
                for target_family in equivalence_list:
                    if target_family[0] in dict_or_value:
                        family_value = dict_or_value[target_family[0]]
                        for target in target_family:
                            if target in dict_or_value:
                                if dict_or_value[target] != family_value:
                                    print(f'Warning::consistency_check:: in patch {patch_name} {key} : {dict_or_value[target]} not equal to {family_value}')
                # now make sure that all the targets that are not in the same fmily have different values
                for target_family in equivalence_list:
                    if (target_family[0] in family_value_dict) and (target_family[0] in dict_or_value):
                        family_value_dict[target_family[0]] = dict_or_value[target_family[0]]

                for target_family in family_value_dict:
                    for inner_family in family_value_dict:
                        if target_family == innner_family:
                            continue
                        else:
                            if (target_family in dict_or_value) and (inner_family in dict_or_value):
                                if dict_or_value[target_family] == dict_or_value[inner_family]:
                                    print(f'Warning::consistency_check:: in patch {patch_name} {key} : in {target_family} {dict_or_value[target_family]} equal to in {inner_family} {dict_or_value[inner_family_value]}')
        return

    # perform a series of consistency checks on the patch list database
    def consistency_check(self, patch_list):
        # if different offsets, are they all unique
        for patch_name in patch_list:
            self.check_for_uniqueness(patch_name, patch_list[patch_name], 'start_offset')
            
        # if different from_xxx are they all unique
        for patch_name in patch_list:
            from_type_list = ['change_from_bytes', 'change_from_ptr', 'change_from_jump']
            for from_type in from_type_list:
                self.check_for_uniqueness(patch_name, patch_list[patch_name], from_type)

        # if different from_xxx are they all unique
        for patch_name in patch_list:
            to_type_list = ['change_to_bytes', 'change_to_ptr', 'change_to_jump']
            for to_type in to_type_list:
                self.check_for_uniqueness(patch_name, patch_list[patch_name], to_type)
        
        return

    
    # given a target address in hex, produce a series of bytecodes
    #   corresponding to "jal <target_address>" -- some MIPS instruction
    #   munging. 
    def assemble_jxx(self, jump_string):

        jump_type, target_symbol = jump_string.split('.');
        format = 'j'
        
        if (jump_type == 'j'):
            format = 'j'
            target_address = self.resolve_jump_target(target_symbol)
            jump_opcode = 0x2
        elif (jump_type == 'jal'):
            format = 'j'
            target_address = self.resolve_jump_target(target_symbol)
            jump_opcode = 0x3
        elif (jump_type == 'jalr'):
            format = 'r'
            target_register = self.resolve_register_symbol(target_symbol)
            jump_opcode = 0x9
        elif (jump_type == 'jr'):
            format = 'r'
            target_register = self.resolve_register_symbol(target_symbol)
            jump_opcode = 0x8
        else:
            format = 'j'
            jump_opcode = 0x3
            print(f'Error::assemble_jxx: unrecognized jump type {jump_type} -- assuming jal')

        # There are two types of jumps -- and we need to encode both
        if (format == 'j'):
            if (isinstance(target_address, str)):
                if self.debug:
                    print(f'Debug::assemble_jal: converting string: {target_address} to long: {int(target_address,16):08x}')
                target_address = int(target_address,16);
            ## by the time we get here, target address is an integer type
            long_output = (jump_opcode << 26) | ((target_address & 0x0FFFFFFF) >> 2)
            if self.debug:
                print(f'Debug::assemble_jxx::j: long_output = 0x{long_output:08x}')
            result = long_output.to_bytes(4, byteorder='little')
        elif (format == 'r'):
            ## in this format, the jump opcode goes at the bottom in the "function" spot
            destination_register = self.resolve_register_symbol("ra")
            long_output = jump_opcode | (target_register << 21) | (destination_register << 11)
            if self.debug:
                print(f'Debug::assemble_jxx::r: long_output = 0x{long_output:08x}')
            result = long_output.to_bytes(4, byteorder='little')
        else:
            print(f'Error:assemble_jxx: unrecognized jump format {format} -- returning 0')
            long_output = 0x0
            result = long_output.to_bytes(4, byteorder='little')

        if self.debug:
            print(f'Debug::assemble_jxx::as bytes = {result}')
            
        return result



    # given a target address in hex, produce a series of bytecodes
    #   corresponding to "jal <target_address>" -- some MIPS instruction
    #   munging. 
    def assemble_ptr(self, ptr_string):
        ptr_symbol = ptr_string
        ptr_address = self.resolve_ptr(ptr_symbol)

        if self.debug:
            print(f'Debug::assemble_ptr::as bytes = {ptr_address}')
        if (isinstance(ptr_address, str)):
            ptr_address = ptr_address.replace('0x','')
            ptr_address = int(ptr_address,16);

        result = ptr_address.to_bytes(4, byteorder='little')
        return result

    # given a target address in hex, produce a series of bytecodes
    #   corresponding to "jal <target_address>" -- some MIPS instruction
    #   munging. 
    def assemble_ptr_hi(self, ptr_string):
        ptr_symbol = ptr_string
        ptr_address = self.resolve_ptr(ptr_symbol)

        if (isinstance(ptr_address, str)):
            ptr_address = ptr_address.replace('0x','')
            ptr_address = int(ptr_address,16);

        ptr_address = ptr_address >> 16
        if self.debug:        
            print(f'Debug::assemble_ptr_hi::ptr_address = 0x{ptr_address:04x}')

        result = ptr_address.to_bytes(2, byteorder='little')
        return result

    # given a target address in hex, produce a series of bytecodes
    #   corresponding to "jal <target_address>" -- some MIPS instruction
    #   munging. 
    def assemble_ptr_lo(self, ptr_string):
        ptr_symbol = ptr_string
        ptr_address = self.resolve_ptr(ptr_symbol)

        if (isinstance(ptr_address, str)):
            ptr_address = ptr_address.replace('0x','')
            ptr_address = int(ptr_address,16);

        ptr_address = ptr_address & 0xffff
        if self.debug:
            print(f'Debug::assemble_ptr_lo::ptr_address = 0x{ptr_address:04x}')
        result = ptr_address.to_bytes(2, byteorder='little')
        return result



    # A function to add patches from source compiled lineage to patch list
    def add_bytes_file_to_patch_list(self, patch_name, directory, new_bytes_filename,
				     old_bytes_filename, entry_list_filename):
	## Get the entry_adress from file at the start_address_filename
        entry_list_filepath = os.path.join(directory, entry_list_filename)

        new_bytes_filepath = os.path.join(directory, new_bytes_filename)
        old_bytes_filepath = os.path.join(directory, old_bytes_filename)
        with open(new_bytes_filepath, 'rb') as new_bytes_f:
            with open(old_bytes_filepath, 'rb') as old_bytes_f:

                index = 0
                with open(entry_list_filepath, 'r') as entry_list_f:
                ## Open a file containing one line with start (in hex) and length (in hex) of each segment
                ## in the given binary file
                    base_offset = 0
                    print(f'Info::add_bytes_file_to_patch_list -- entry_list files {entry_list_f}')
                    for entry_list_string in entry_list_f:
                        start_address_string, length_string = entry_list_string.split()
                        start_address = int(start_address_string, 16)
                        start_offset = start_address & 0x7FFFFFFF
                        if (index == 0):
                            base_offset = start_offset
                        length = int(length_string, 16)
                        new_patch_name = patch_name + str(index);
                        print(f'debug::add_bytes_file_to_patch_list[{new_patch_name}]: start_offset = 0x{start_offset:08x}; length = 0x{length:08x}')
                        print(f'Info::add_bytes_file_to_patch_list -- creating patch named: {new_patch_name}')

                        self.internal_patch_list[new_patch_name] = {}
                        self.internal_patch_list[new_patch_name]['start_offset'] = start_offset
                        ## entry point code regions stacked on top of each other, starting at beginning of file
                        old_bytes = old_bytes_f.read(length)
                        ## entry point code regions start at zero, but are packed with filler in between unused address space
                        print(f'Debug: add_bytes_to_patch_list: start_offset = 0x{start_offset:8x}; base_offset = 0x{base_offset:8x}')
                        new_bytes_f.seek(start_offset - base_offset)
                        new_bytes = new_bytes_f.read(length)
                        self.internal_patch_list[new_patch_name]['change_from_bytes'] = old_bytes
                        self.internal_patch_list[new_patch_name]['change_to_bytes'] = new_bytes
                        index += 1
        return

    def add_to_internal_patch_list(self, patch_list):
        self.internal_patch_list.update(patch_list)
        return

    def patch_binary (self, binary_filename, camera_target):
        ##print(f'Debug: patch_code -- opening {binary_filename} for patching')
        with open(binary_filename, "rb+") as binary_f:
            data = self.apply_patches(binary_f, camera_target)
        return

    # I cannot figure out how to get the gcc tool chain to align
    #   the start of the binary to anything other than 16-byte boundaries.
    #   this function is a hack around that -- returning the right
    #   adjustment value to add to the offset from the aligned entry
    #   function 
    def get_alignment_pad(self, entry_address):
        if ((entry_address & 0xf) == 0): return(0x0)
        if ((entry_address & 0xf) == 4): return(0xc)
        if ((entry_address & 0xf) == 8): return(0x8)
        return(0x4)

    ## set the name of the file we will use to resolve symbolic names
    ##     first we look at the .cmd file
    def set_cmd_symbol_table(self, directory, base_filename):
        ##print(f'Debug::set_symbol_table: filename: {base_filename}')
        ## Open up the .cmd file containing all the symbols we might be interested in
        with open(os.path.join(directory, base_filename+".cmd"), "r") as cmd_f:
            ## look for the target symbol
            Lines = cmd_f.readlines()
            found_symbol_table_p = False;
            for line in Lines:
                if (not found_symbol_table_p):
                    if(line.find("Symbol Definitions") != -1):
                        found_symbol_table_p = True
                    else:
                        if(line.find(". =") != -1):
                            line = line.replace('.', '');
                            line = line.replace(';', '');
                            line = line.replace('=', '');
                            [self.entry_address] = line.split()
                            print(f'Debug::set_symbol_table: found entry address: {self.entry_address}');
                    continue
                if (len(line) < 3):
                    continue
                if (line.find("Memory") != -1):
                    break
                line = line.replace(';', '');
                line = line.replace('=', '');
                ## print(f'Debug::set_cmd_symbol_table -- line: {line.split()}')
                [symbol, address] = line.split()
                if (len(symbol) > 0):
                    if self.debug:
                        print(f'Debug::set_cmd_filename: adding {symbol} @{address} to symbol_table')
                    self.symbol_table[symbol] = address
        return

    ## set the name of the file we will use to resolve symbolic names
    ##     first we look at the .obj files
    def set_obj_symbol_table(self, directory, base_filename):
        ## Open up the .symbols file containing all the symbols from the current patch
        if self.debug:
            print(f'Debug::set_obj_symbol_table -- opening file {base_filename}')
        with open(os.path.join(directory, base_filename+".sym"), "r") as symbols_f:
            ## look for the target symbol
            Lines = symbols_f.readlines()
            found_symbol_table_p = False;
            for line in Lines:
                if (not found_symbol_table_p):
                    if(line.find("SYMBOL TABLE") != -1):
                        found_symbol_table_p = True
                    continue
                if (len(line) < 3):
                    continue
                if self.debug:
                    print(f'Debug::set_obj_symbol_table -- 1 symbol file line: {line.split()}')
                if ((line.find("F entry") == -1) and (line.find("O entry") == -1)):
                    if self.debug:
                        print(f'Debug::set_obj_symbol_table -- skipping not function at symbol file line: {line.split()}')
                    continue
                ## we have a line which contains a F(unction) or O(data) and offset
                [address, _, _, _, length, symbol] = line.split()
                ##
                ##alignment_pad = self.get_alignment_pad(int(self.entry_address,16))
                ##address = int(offset,16) + int(self.entry_address,16) + alignment_pad
                ##address = hex(address)
                if (len(symbol) > 0):
                    if self.debug:
                        print(f'Debug::set_obj_symbol_table: adding {symbol} @{address} to symbol_table')
                    self.symbol_table[symbol] = address
        
        return
        
    def symbolic_reference_p(self, symbol_name):
        ##print(f'Debug::symbolic_reference_p: symbol_name: {symbol_name}')
        if (symbol_name != Null):
            return True
        else:
            return False

    def resolve_ptr(self, ptr_symbol):
        if (ptr_symbol in self.symbol_table):
            if self.debug:
                print(f'Debug::resolve_ptr: {ptr_symbol} @ {self.symbol_table[ptr_symbol]}')
            return self.symbol_table[ptr_symbol]
        print(f'Error::resolve_ptr: target_symbol:{ptr_symbol} not found in symbol_table')
        return("ptr_symbol not found")


    def resolve_jump_target(self, target_symbol):
        if (target_symbol in self.symbol_table):
            if self.debug:
                print(f'Debug::resolve_jump_target symbol: {target_symbol} @ {self.symbol_table[target_symbol]}')
            return self.symbol_table[target_symbol]
        print(f'Error::resolve_jump_target: target_symbol:{target_symbol} not found in symbol_table')
        return("target_symbol not found")

    def resolve_register_symbol(self, register_symbol):
        if (register_symbol in self.register_table):
            if self.debug:
                print(f'Debug::resolve_register_symbol: {register_symbol} @ {self.register_table[register_symbol]}')
            return self.register_table[register_symbol]
        print(f'Error::resolve_register_symbols: register_symbol:{register_symbol} not found in register_table')
        return("register_symbol not found")

    ## 2023-02-04: Patch list dictionaries may have camera-target-specific values
    ##  this function extracts these if they exist
    def get_target_value(self, dict_or_value, camera_target):
        if(type(dict_or_value) is dict):
            ##print(f'get_target_value:: {dict_or_value}')
            return dict_or_value[camera_target]
        else:
            return dict_or_value

    ## does a given patch apply to this platform
    ##      if no camera-specific optins
    ##      or our camera-specific option
    def patch_applies_to_camera(self, patch, camera_target):
        if (type(patch['start_offset']) is dict):
            if camera_target in patch['start_offset']:
                return True
            else:
                return False
        else:
            return True
	
    def apply_patches(self,  binary_f, camera_target):
        error = False
        # first check all the patches are pointing to the right (matching) binary
        for patch in self.internal_patch_list.keys():
            ## Maybe this patch doesn't apply to this camera
            if (self.patch_applies_to_camera(self.internal_patch_list[patch], camera_target) == False):
                continue
            offset = self.get_target_value(self.internal_patch_list[patch]['start_offset'], camera_target)
            ##print(f'Debug::apply_patches: working on patch:{patch} at offset:0x{offset:x}')
            binary_f.seek(offset)
            ## Assemble all the potentially camera-specific symbolic values into 'change_from_bytes'
            if ('change_from_jump' in self.internal_patch_list[patch]):
                ## if this is a symbolic reference, resolve it from the symbol table
                self.internal_patch_list[patch]['change_from_bytes'] = self.assemble_jxx(self.get_target_value(self.internal_patch_list[patch]['change_from_jump'], camera_target))
            if ('change_from_ptr' in self.internal_patch_list[patch]):
                ## if this is a symbolic reference to a ptr, resolve it from the symbol table
                self.internal_patch_list[patch]['change_from_bytes'] = self.assemble_ptr(self.get_target_value(self.internal_patch_list[patch]['change_from_ptr'], camera_target))
            if ('change_from_ptr_hi' in self.internal_patch_list[patch]):
                self.internal_patch_list[patch]['change_from_bytes'] =  self.assemble_ptr_hi(self.get_target_value(self.internal_patch_list[patch]['change_from_ptr_hi'], camera_target))
            if ('change_from_ptr_lo' in self.internal_patch_list[patch]):
                self.internal_patch_list[patch]['change_from_bytes'] =  self.assemble_ptr_lo(self.get_target_value(self.internal_patch_list[patch]['change_from_ptr_lo'], camera_target))
            change_from_bytes = self.internal_patch_list[patch]['change_from_bytes']
            ## print(f'apply_patches::patch {patch}[change_from_bytes] = {change_from_bytes}, target = {camera_target}')

            self.internal_patch_list[patch]['change_from_bytes'] = self.get_target_value(self.internal_patch_list[patch]['change_from_bytes'], camera_target)
            ##change_from_bytes = self.internal_patch_list[patch]['change_from_bytes']
            ##print(f'apply_patches::patch {patch}[change_from_bytes] = {change_from_bytes}, target = {camera_target}')
                        
            from_length = len(self.internal_patch_list[patch]['change_from_bytes'])

            ## Assemble all the potentially camera-specific symbolic values into 'change_to_bytes'
            if ('change_to_jump' in self.internal_patch_list[patch]):
                ## if this is a symbolic reference, resolve it from the symbol table
                self.internal_patch_list[patch]['change_to_bytes'] = self.assemble_jxx(self.get_target_value(self.internal_patch_list[patch]['change_to_jump'], camera_target))
            if ('change_to_ptr' in self.internal_patch_list[patch]):
                ## if this is a symbolic reference to a ptr, resolve it from the symbol table
                self.internal_patch_list[patch]['change_to_bytes'] = self.assemble_ptr(self.get_target_value(self.internal_patch_list[patch]['change_to_ptr'], camera_target))
            if ('change_to_ptr_hi' in self.internal_patch_list[patch]):
                ## if this is a symbolic reference to a ptr, resolve it from the symbol table
                self.internal_patch_list[patch]['change_to_bytes'] = self.assemble_ptr_hi(self.get_target_value(self.internal_patch_list[patch]['change_to_ptr_hi'], camera_target))
            if ('change_to_ptr_lo' in self.internal_patch_list[patch]):
                ## if this is a symbolic reference to a ptr, resolve it from the symbol table
                self.internal_patch_list[patch]['change_to_bytes'] = self.assemble_ptr_lo(self.get_target_value(self.internal_patch_list[patch]['change_to_ptr_lo'], camera_target))

            self.internal_patch_list[patch]['change_to_bytes'] = self.get_target_value(self.internal_patch_list[patch]['change_to_bytes'], camera_target)
            to_length = len(self.internal_patch_list[patch]['change_to_bytes'])
            if from_length < to_length:
                print(f'Error: apply_patches -- patch {patch} : available from len {from_length} is less than patch len {to_length}')
                error=True
            if from_length > to_length:
                print(f'Warning::apply_patches -- patch {patch} : from len {from_length} to not the same as to len {to_length} -- padding zeros to_length')
                self.internal_patch_list[patch]['change_to_bytes'] = self.internal_patch_list[patch]['change_to_bytes'].ljust(from_length, b'0')
                new_to_length = len(self.internal_patch_list[patch]['change_to_bytes'])
                if self.debug:
                    print(f'Debug::apply_patches -- old to_length = {to_length} -- new to_length = {new_to_length}')
		
            actual_data = binary_f.read(to_length)
            ## truncate expected data to to_length -- only compare what we're replacing
            expected_data = self.internal_patch_list[patch]['change_from_bytes']
            if expected_data[:to_length] != actual_data:
                print(f'Error: apply_patches -- patch {patch} : at {offset:06x} Expected {expected_data}; Actual {actual_data}')
                error=True

        if (error):
            print("Errors -- aborting Patch")
            return
        # Now time to actually apply patches
        for patch in self.internal_patch_list.keys():
            # skip any patches that don't apply to this camera
            if (self.patch_applies_to_camera(self.internal_patch_list[patch], camera_target) == False):
                continue
            offset = self.get_target_value(self.internal_patch_list[patch]['start_offset'], camera_target)
            change_to_data = self.internal_patch_list[patch]['change_to_bytes']
            ##print(f'Debug: apply_patches -- patching location {offset:06x} to {change_to_data}')
            binary_f.seek(offset)
            binary_f.write(change_to_data)

        return
