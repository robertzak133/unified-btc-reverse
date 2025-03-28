//
// Prototype for code to debug SD card corruption
//   issue in some BTC-xx-HP5 cameras

void fdb_handleDeleteAll_menu(void);
void fdb_print_blocks(byte* data_buffer, uint start_block, uint num_blocks);
void fdb_sdtest(void);
void fdb_find_exfat(void);
void fdb_read_blocks(void);
bool fdb_check_buffer_contents(byte *buffer,uint num_bytes,uint pattern);
void fdb_sd_power_cycle_test(void);
