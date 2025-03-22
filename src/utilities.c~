//
// utilities.c
//
// A bunch of utilities to help analyze the runtime environment of 
// the firmware.  

#include "BTC.h"
#include "utilities.h"




int util_set_cold_item_language_id(byte menu_selection) {

  copy_file("D:\\ENGLISH.SST", "A:\\RO_RES\\UI\\SST\\ENGLISH.SST");
  copy_file("D:\\ESPANOL.sst", "A:\\RO_RES\\UI\\SST\\ESPANOL.sst");
  copy_file("D:\\DEUTSCH.sst", "A:\\RO_RES\\UI\\SST\\DEUTSCH.sst");
  copy_file("D:\\DUTCH.sst", "A:\\RO_RES\\UI\\SST\\DUTCH.sst");
  copy_file("D:\\ITALIANO.sst", "A:\\RO_RES\\UI\\SST\\ITALIANO.sst");
  copy_file("D:\\FRANCIS.sst", "A:\\RO_RES\\UI\\SST\\FRANCIS.sst");
  copy_file("D:\\POLISH.sst", "A:\\RO_RES\\UI\\SST\\POLISH.sst");

  return(set_cold_item_language_id(menu_selection));
}



// 2022-09-30
// write_memory_to_file()

// Dumps a region of memory to a file


int   write_memory_to_file(char *memory_start, unsigned int num_bytes, char *filename) {
  unsigned int file_ptr;

  file_ptr = btc_fopen(filename, 4);
  if (file_ptr == 0) {
    tty_printf("Error::write_memory_to_file -- could not open %s\n",
	       filename);
    return(-1);
  } else {
    btc_fwrite(file_ptr, memory_start, num_bytes);
    btc_fclose(file_ptr);
  }
  return(-1);
}



void dump_dram_contents() {
  char * start_address = (char* ) 0x80000000;
  unsigned int num_bytes = 0x31a600 + 0x6ba0;
  char filename[] = "D:/dram_dump.bin";

  tty_printf("info::dump_dram_contents - s");
  write_memory_to_file(start_address, num_bytes, filename);
  tty_printf("info::dump_dram_contents - e");
}

// Copy file on the SD card into the A file system
void copy_file(char *source_filename, char *dest_filename) {
  
  set_pre_printf_state();
  tty_printf("info::copy_file - s\n");
  check_post_printf_state_set_sio_params();

  unsigned int source_fileptr = vfsOpen(source_filename, 0x10);

  if (source_fileptr != 0) {
    unsigned int source_filesize = vfsFileSizeGet(source_fileptr);
    vfsClose(source_fileptr);
    if (source_filesize == 0) {
      set_pre_printf_state();
      tty_printf("error::copy_file - file len zero for %s\n", source_filename);
      check_post_printf_state_set_sio_params();
      return;
    } else {
      set_pre_printf_state();
      tty_printf("info::copy_file - %s size is %d\n", source_filename, source_filesize);
      check_post_printf_state_set_sio_params();
    }
  } else {
    set_pre_printf_state();
    tty_printf("error::copy_file - can't open %s\n", source_filename);
    check_post_printf_state_set_sio_params();
  }
  
  set_pre_printf_state();
  tty_printf("  - deleting %s \n", dest_filename);
  check_post_printf_state_set_sio_params();
  
  vfsFileDel(dest_filename);
  set_pre_printf_state();
  tty_printf("  - copying %s to %s \n", source_filename, dest_filename);
  check_post_printf_state_set_sio_params();
  
  vfsFileCopy(source_filename, dest_filename);

  unsigned int dest_fileptr = vfsOpen(dest_filename, 0x10);
  if (dest_fileptr != 0) {
    unsigned int dest_filesize = vfsFileSizeGet(dest_fileptr);
    vfsClose(dest_fileptr);
    if (dest_filesize == 0) {
      set_pre_printf_state();
      tty_printf("error::copy_file - file len zero for %s\n", dest_filename);
      check_post_printf_state_set_sio_params();
      return;
    } else {
      set_pre_printf_state();
      tty_printf("info::copy_file - %s size is %d\n", dest_filename, dest_filesize);
      check_post_printf_state_set_sio_params();
    }
  } else {
    set_pre_printf_state();
    tty_printf("error::copy_files - can't open %s\n", dest_filename);
    check_post_printf_state_set_sio_params();
  }
  set_pre_printf_state();
  tty_printf("info::copy_file - e \n");
  check_post_printf_state_set_sio_params();
}

void utilities_check_post_printf_hook() {
  //
  //dump_dram_contents();

  //char pmt_source_filename[] = "D:\\PMT_BK.JPG";
  //char pmt_dest_filename[] = "A:\\RO_RES\\UI\\JPG\\PMT_BK.JPG";

  //copy_image_file(pmt_source_filename, pmt_dest_filename);

}
