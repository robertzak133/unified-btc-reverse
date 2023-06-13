import os
import re
from datetime import date

class UCTC_Symbol_Maker:
    '''
    A class to create a list of symbols from CTC trail camera environment
    for system services
    '''
    

    # String containing active cmd file (used to dereference symbols)
    symbol_table = {}


    #   Given a symbol file and a .h file with furnction prototypes
    #   output a .cmd file for loader with symbols resolved
    def create_ld_file(self, esymbol_directory, esymbol_filename, h_directory, h_filename,
                       ld_directory, ld_filename, old_bytes_directory, old_bytes_filename):
        self.load_symbols_from_h_file(h_directory, h_filename)
        self.resolve_symbols(esymbol_directory, esymbol_filename)
        self.write_ld_file(ld_directory, ld_filename, old_bytes_directory, old_bytes_filename)
        return

    # load the symbols we're interested in based on the function prototypes in the .h file
    def load_symbols_from_h_file(self, directory, h_filename):
        with open(os.path.join(directory, h_filename), "r") as h_file:
            Lines = h_file.readlines()
            for line in Lines:
                if not(self.is_comment(line)):
                   symbol = self.get_function_name(line)
                   self.symbol_table[symbol] = {}
                   self.symbol_table[symbol]['value'] = "not defined"
        return

    # figure out where the symbols are base on the symbol file
    def resolve_symbols(self, directory, esymbol_filename):
        with open(os.path.join(directory, esymbol_filename), "r") as esym_file:
            Lines = esym_file.readlines()
            for symbol in self.symbol_table.keys():
                for line in Lines:
                    if line.startswith("80") or line.startswith("00"):
                        [address, local_global, type, rest] = line.split(maxsplit=3)
                        if (local_global == 'g') and (type == 'F') :
                            [seg_type, offset, function] = rest.split(maxsplit=3)
                            if (seg_type == ".text"):
                                if symbol == function:
                                    self.symbol_table[symbol]['value'] = address
                        else:
                            if (local_global == 'g') and (type == 'O'):
                                print(rest.split())
                                [seg_type, size, variable] = rest.split()
                                if (seg_type == ".rodata"):
                                    print(f'Debug::resolve_symbols: variable = {variable} ;symbol = {symbol}; address = {address}')
                                    if symbol == variable:
                                        self.symbol_table[symbol]['value'] = address
        return

    # write the command file for the loader to use when linking UCTC files
    def write_ld_file(self, directory, ld_filename, old_bytes_directory, old_bytes_filename):
        with open(os.path.join(directory, ld_filename), "w") as ld_file:
            # Write the header
            ld_file.write("/* Command File for Gcc Loader */\n");
            ld_file.write("/*    Created automatically by UTC_Symbol_Maker.py */\n");
            today = date.today();
            ld_file.write("/*    " + today.strftime("%Y-%m-%d") + " */\n");
            #
            ld_file.write("ENTRY (uctc_init)\n");
            ld_file.write("SECTIONS {\n");
            # Write the symbols
            ld_file.write("  /* Symbol Definitions */\n");
            for symbol in self.symbol_table.keys():
                value = self.symbol_table[symbol]['value']
                print(f'Debug::write_ld_file: symbol: {symbol} = value: {value}')
                ld_file.write("  " + symbol + " = 0x" + value + ";\n")
            # write the symbol for the size CTC_MAX_SIZE
            max_size = os.path.getsize(os.path.join(old_bytes_directory, old_bytes_filename))
            ld_file.write("  CTC_MAX_SIZE = " + str(max_size) + ";\n")
            #
            ld_file.write("\n  /* start by setting the _gp pointer to what the base firmware needs */\n")
            ld_file.write("   _gp = 0x8042bc20;\n\n")
            # Here's where we put the code and data
            ld_file.write("  . = ctc_user_code_base" + ";\n")

            # write the trailer
            ld_file.write("  /* Initialized Data comes first; by convention the relocation table is at the */\n")
            ld_file.write("  /*      start of the binary */\n")
            ld_file.write("  .data : { *(.data) }\n")
            ld_file.write("  /* then uninitialized data */\n");
            ld_file.write("  .bss : {*(.bss)} \n");
            ld_file.write("  /* finally text */\n");
            ld_file.write("  .text : {*(.text)}\n");
            ld_file.write("}\n");
        return


    # World's most minimal comment line checker
    def is_comment(self, line):
        if line.startswith('//'): return True
        if line.startswith('\n'): return True
        return False

    # World's most minimal function prototype parser
    # 2021-10-11 -- added support for "const" keyword; slightly more sophisticated
    def get_function_name(self, line):
        print(line.split(maxsplit=3))
	## get the extern
        [extern, rest] = line.split(maxsplit=1);
        if (extern == 'extern'):
            ## maybe const
            [const_or_type, rest] = rest.split(maxsplit=1);
            if (const_or_type == 'const'):
                print(rest.split());
                [type, function_name] = rest.split();
            else:
                [function_name, rest] = rest.split(maxsplit=1);    
        else:
            print("error -- could not find extern");

        print(re.split(r"\(|\[", function_name, maxsplit=1))
        [function_name, rest] = re.split(r"\(|\[", function_name, maxsplit=1);
        return function_name
