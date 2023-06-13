//CreateLdScript
//    given a file of symbols from gnu-objutils -t
//    find the undefined symbols
//    resolve the undefined symbols based on current Ghidra project
//    create a command script for linker with all of the symbols defined
//    or die trying
//@author Robert Zak
//@category _BTC_
//@keybinding 
//@menupath 
//@toolbar 

import java.text.DateFormat;  
import java.text.SimpleDateFormat;  
import java.util.Date;  
import java.util.Calendar;  

import java.util.*;
import java.io.IOException;
import java.nio.charset.*;
import java.nio.file.*;
//import java.nio.file.Files;
//import java.nio.file.Path;
//import java.nio.file.Paths;

import ghidra.app.script.GhidraScript;
import ghidra.program.flatapi.*;
import ghidra.program.model.util.*;
import ghidra.program.model.reloc.*;
import ghidra.program.model.data.*;
import ghidra.program.model.block.*;
import ghidra.program.model.symbol.*;
import ghidra.program.model.scalar.*;
import ghidra.program.model.mem.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.lang.*;
import ghidra.program.model.pcode.*;
import ghidra.program.model.address.*;

public class CreateLdScript extends GhidraScript {

    public void run() throws Exception {
        String patch_directory;
	String patch_root_name;

	if (isRunningHeadless()) {
	    String[] args = getScriptArgs();
	    patch_directory = "./";
	    patch_root_name = args[0];
	} else {
	    // Open Symbol File
	    patch_directory = "C:\\Users\\rober\\Google Drive\\local_repositories\\BTC-Reverse\\targets\\btc-7a\\source-code-patches\\custom-function-example\\";
            patch_root_name = "patch";
        }
                                       
	String symbol_filename = patch_root_name + ".symbols";
	String ld_script_filename = patch_root_name + ".cmd";

	// Hash table to store symbols and values
	Hashtable<String, String> symbol_ht;
	// List to store function names
	List<String> function_list;

	// Get a list of undefined symbols
	println("Getting symbols from:" + symbol_filename); 
	
	Path symbol_path = Paths.get(patch_directory, symbol_filename);
	symbol_ht = parse_symbol_file_for_undef(symbol_path);
	println("Debug: symbol file: " + symbol_filename + " parsed");
	// Get Functions defined in patch
	function_list = parse_symbol_file_for_functions(symbol_path);
		
	// Resolve symbols based on Ghidra symbol table
	// Write the symbols in a format and in a template loader understands
	println("Debug: Writing symbol defs to:" + ld_script_filename);
	Path ld_script_path = Paths.get(patch_directory, ld_script_filename);
	write_ld_script(ld_script_path, function_list, symbol_ht);
			
	println("Debug: ld-script : " + ld_script_filename + " written");
    }

    // Sift through the .symbols file looking for undefined symbols;
    //      create a hash table with pairs of symbol_name and symbol_value
    //      get symbol value from Ghidra. 
    private Hashtable<String, String> parse_symbol_file_for_undef(Path symbol_path) throws Exception {
	println("Debug::parse_symbol_file_for_undef: " + symbol_path);
	Hashtable<String, String> symbol_ht = new Hashtable<String, String>();
	List<String> list_of_lines = Files.readAllLines(symbol_path);
	for(String line : list_of_lines) {
	    if(line.contains("*UND*")) {
		String symbol_name = parse_symbol_name(line);
		String symbol_value = resolve_symbol_adddress(symbol_name);
		symbol_ht.put(symbol_name, symbol_value);
                }
	}	
	return(symbol_ht);
    }

    // Sift through the symbols file for function names and addresses
    private List<String> parse_symbol_file_for_functions(Path symbol_path) throws Exception {
	println("Debug::parse_symbol_file_for_functions: " + symbol_path);
	List<String> function_list = new ArrayList<>();
	List<String> list_of_lines = Files.readAllLines(symbol_path);
	for(String line : list_of_lines) {
	    if(line.contains("F .text")) {
		String function_name = parse_function_name(line);
		function_list.add(function_name);
            }
        }
	return(function_list);
    }	


    // Pull a function name from a line with ".text" in .symbols file
    private String parse_function_name(String line) {
        // 00000000 g     F .text	00000548 setDigitalEffect
	String[] split_line = line.split("\\s+");
	  
	if (split_line[2].compareTo("F") != 0) {
	    println("Error::parse_function_name: not sure line: <" + line + "> contains a function");
	    return("Not a Function");
        } else {
	    println("Debug::parse_function_name: returning: " + split_line[5]);
	    return (split_line[5]);
        }
    }

    // 
    // Pull a symbol name from a line with *UND* in .symbols file
    private String parse_symbol_name(String line) {
	// 00000000  <WS> *UND* <WS> 00000000 <symbol_name>
	String[] split_line = line.split("\\s+");
	return (split_line[3]);
    }

    // Fill symbol address from Ghidra Symbol Library for current project
    private String resolve_symbol_adddress(String symbol_name) {
	SymbolTable st = state.getCurrentProgram().getSymbolTable();

	List<Symbol> symbol_list = st.getGlobalSymbols(symbol_name);
	if (symbol_list.isEmpty()) {
	     println("Error::resolve_symbol_address: can't find symbol:" + symbol_name);
	     return("Not Found");
        } else {
	     if (symbol_list.size() > 1) {
		 println("Warning:: multiple symbols [" + symbol_list.size() + "] for name:" + symbol_name);
             }
	     Address address = symbol_list.get(0).getAddress();
	     if (address == null) {
		 println("Error::resolve_symbol_address: can't find address for symbol:" + symbol_name);
                 return("No Address Found");
             } else {
		 return(address.toString("0x"));
             }
         }
	 //return("program error");
    }

    // Write 
    private void write_ld_script (Path ld_script_path,
			          List<String> function_list,  
				  Hashtable<String, String> symbol_dict) throws Exception {
        Date date = Calendar.getInstance().getTime();
	DateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
	String strDate = dateFormat.format(date);

	Charset charset = Charset.forName("UTF-8");
	OpenOption create_mode = StandardOpenOption.CREATE;
	OpenOption truncate_mode = StandardOpenOption.TRUNCATE_EXISTING;
	OpenOption [] create_truncate_modes = new OpenOption[] {create_mode, truncate_mode};

	println("Debug::write_ld_script 1");
	// Start out with the general format
	List<String> lines = new ArrayList<String>();

        lines.add("/* Command File for Gcc Loader */");
	lines.add("/*    Created automaticaly by Ghidra.CreateLdScript.java */");
	lines.add("/*    " + strDate + " */");

	// Now Set the Entrypoint -- by convention, the first function declared in the patch
        String entry_function_name = function_list.get(0);

	println("Debug::write_ld_script: function_name: " + entry_function_name);
	String entry_function_address = resolve_symbol_adddress(entry_function_name);
	println("Debug::write_ld_script entry_function_address: " + entry_function_address);
	lines.add("ENTRY ("+ entry_function_name + ")");

	// Now find the gp register value
	String gp_address = "0x8042bc20";
	gp_address = get_gp_address_string(entry_function_address);

	// Sections
        lines.add("SECTIONS {");
	lines.add("  /* Start of Entry Function:" + entry_function_name + "*/");
	lines.add("  . = " + entry_function_address + ";");
	// Symbol Definitions
	lines.add("");
	lines.add("  /* Symbol Definitions */");
	for (Map.Entry<String, String> e : symbol_dict.entrySet())
            lines.add("   " + e.getKey() + " " + e.getValue()+";");
	lines.add("");
	// Rest of file
	lines.add("  .text . :");
	lines.add("     {");
	lines.add("     *(.text)");
	lines.add("     }");
	lines.add("   .data :");
	lines.add("     {");
	lines.add("     _gp = " + gp_address + ";");
	lines.add("     *(.sdata)");
	lines.add("     *(.sdata.)");
	lines.add("     }");

	// Write all the lines out
	Files.write(ld_script_path, lines, charset, create_truncate_modes);	
    }

    // Find the GP address to use in context of entry_function 
    // 
    private String get_gp_address_string(String entry_function_address_string) {
	SymbolTable st = state.getCurrentProgram().getSymbolTable();

	String gp_1_name = "_gp_1";
	String gp_2_name = "_gp_2";

	List<Symbol> gp_1_list = st.getGlobalSymbols(gp_1_name);
	if (gp_1_list.isEmpty()) {
	     println("Error::get_gp_address_string: can't find symbol:" + gp_1_name);
	     println("     -- look at analysis of 0x8000 0030 -- should be where gp is set");
	     return("Symbol Not Found");
        }
	// We only handle the case of a single gp register value (apprpriate for the 
        //    BTC-7A an 8A); so if there is a second gp_2 symbol, we're confused
	List<Symbol> gp_2_list = st.getGlobalSymbols(gp_2_name);
	if (!gp_2_list.isEmpty()) {
	    // We're confused
	    printf("Warning::get_gp_address_string: found more than one _gp_x symbol; using first");
        }
	
	if (gp_1_list.size() > 1) {
	    println("Warning::get_gp_address_string: multiple symbols [" + gp_1_list.size() + "] for name:" + gp_1_name);
        }
	Address address = gp_1_list.get(0).getAddress();
	if (address == null) {
	    println("Error::get_gp_address_string: can't find address for:" + gp_1_name);
            return("Address Not Found");
        } else {
	    return(address.toString("0x"));
        }
    }
}
