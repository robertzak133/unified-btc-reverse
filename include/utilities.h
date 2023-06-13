//
// utilities.h
//
// A bunch of utilities to help analyze the runtime environment of 
// the firmware.  

int  util_set_cold_item_language_id(byte menu_selection);

void copy_file(char *source_filename, char *dest_filename);

int   write_memory_to_file(char *memory_start, uint num_bytes, char *filename);
void  dump_dram_contents(void);

void utilities_check_post_printf_hook();

