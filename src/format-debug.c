//
// format-debug.c
//
// Code to help debug "corrupt SD" card problem
//     wherein camears (HP5s only?) rarely corrupt SD card
//

#include "BTC.h"
#include "format-debug.h"

//#define STATE_PRINT

//#define SD_BLOCKS
//#define FIND_EXFAT

//#define SD_RW_CHECK
#define SD_POWER_CYCLE_TEST

//  
// Hook the call to start the SD Card Format FSm
//     Insead of doing it once, do it many times, looking for a case where the
//     mount fails. 
void fdb_handleDeleteAll_menu(void) {
  // don't accumulate time
  handleDeleteAll_menu();
  return;
}


void fdb_HceTaskFormat_task0(void) {
  set_pre_printf_state();
  tty_printf("DEBUG::fdb_HceTaskFormat_task0 at %d\n", get_current_operating_time_ms());
  check_post_printf_state_set_sio_params();
  HceTaskFormat_task0();
}

void fdb_HceTaskFormat_task1_Mount(void) {
#ifdef STATE_PRINT
  set_pre_printf_state();
  tty_printf("DEBUG::fdb_HceTaskFormat_task1 at %d\n", get_current_operating_time_ms());
  check_post_printf_state_set_sio_params();
#endif
  HceTaskFormat_task1_Mount();
}

void fdb_HceTaskFormat_task2_mount_complete(void) {
#ifdef STATE_PRINT
  set_pre_printf_state();
  tty_printf("DEBUG::fdb_HceTaskFormat_task2 at %d\n", get_current_operating_time_ms());
  check_post_printf_state_set_sio_params();
#endif
  HceTaskFormat_task2_mount_complete();
}

void fdb_HceTaskFormat_task3_format_drive(void) {
#ifdef SD_POWER_CYCLE_TEST
  fdb_sd_power_cycle_test();
#elif SD_RW_CHECK
  fdb_sdtest();
#elif SD_BLOCKS
  fdb_read_blocks();
#elif FIND_EXFAT
  fdb_find_exfat();
#endif

#ifdef STATE_PRINT
  set_pre_printf_state();
  tty_printf("DEBUG::fdb_HceTaskFormat_task3 at %d\n", get_current_operating_time_ms());
  check_post_printf_state_set_sio_params();
#endif
  HceTaskFormat_task3_format_drive();
}

void fdb_HceTaskFormat_task4_Init_DCF(void) {
#ifdef STATE_PRINT
  set_pre_printf_state();
  tty_printf("DEBUG::fdb_HceTaskFormat_task4 at %d\n", get_current_operating_time_ms());
  check_post_printf_state_set_sio_params();
#endif
  HceTaskFormat_task4_Init_DCF();
}

void fdb_HceTaskFormat_task5(void) {
#ifdef STATE_PRINT
  set_pre_printf_state();
  tty_printf("DEBUG::fdb_HceTaskFormat_task5 at %d\n", get_current_operating_time_ms());
  check_post_printf_state_set_sio_params();
#endif
  HceTaskFormat_task5();
}

void fdb_HceTaskFormat_task6(void) {
#ifdef STATE_PRINT
  set_pre_printf_state();
  tty_printf("DEBUG::fdb_HceTaskFormat_task6 at %d\n", get_current_operating_time_ms());
  check_post_printf_state_set_sio_params();
#endif
  HceTaskFormat_task6();
}


void fdb_print_blocks(byte* data_buffer, uint start_block, uint num_blocks) {
  for (int block = 0; block < num_blocks; block++) {
    set_pre_printf_state();
    tty_printf("fdb: 0x%04x :\n", start_block + block);
    check_post_printf_state_set_sio_params();       
    for (int line = 0; line < 32; line++) {
      set_pre_printf_state();
      tty_printf("0x%03x :", (line << 4));
      check_post_printf_state_set_sio_params();       
      for (int item = 0; item < 16; item++) {
	set_pre_printf_state();
	tty_printf("%02x ", data_buffer[(line << 4) + item]);
	check_post_printf_state_set_sio_params();       
      }
      set_pre_printf_state();
      tty_printf("\n");
      check_post_printf_state_set_sio_params();       
    }
  }
}

#ifdef FIND_EXFAT
// Look for EXFAT string
void fdb_find_exfat(void) {
  uint num_blocks;
  uint operation_size = 1; // block or sector
  byte *data_buffer;
  int actual_num_bytes;
  int byte_offset = 3;

  struct_system_device_entry *device_descriptor;
  

  data_buffer = (byte *)memoryAllocate(512);

  if (data_buffer == 0) return;

  device_descriptor = get_system_device_entry(2);
  if (device_descriptor == (struct_system_device_entry *)0x0) {
    debug_printf("NULL_device\n");
    return;
  }

  set_pre_printf_state();
  tty_printf("sect nSect(total=%d)\n",device_descriptor->num_sectors);
  check_post_printf_state_set_sio_params();

  bSet(data_buffer, 512, 0x00);
  num_blocks = device_descriptor->num_sectors;
  num_blocks = 0x8000 + 16;
  for (uint current_block = 0x8000; current_block < num_blocks; current_block++) {
    actual_num_bytes = read_sd_blocks(2,current_block,operation_size,data_buffer);
    if (actual_num_bytes != operation_size << 9) {
      set_pre_printf_state();
      tty_printf("sect nSect(total=%d)\n",device_descriptor->num_sectors);
      check_post_printf_state_set_sio_params();
    }
    fdb_print_blocks(data_buffer, current_block, 1);

    if ((data_buffer[3] == 'E') && (data_buffer[4] == 'X') &&
	(data_buffer[5] == 'F') && (data_buffer[6] == 'A') &&
	(data_buffer[7] == 'T') && (data_buffer[8] == ' ')) {
      break;
    }
    bSet(data_buffer, 512, 0x00);
  }
  free(data_buffer);
}
#endif

#ifdef SD_BLOCKS
void fdb_read_blocks(void) {
  uint num_blocks = 6;
  uint block_list[6] = {0x0000, 0x8000, 0x9800, 0x9a00, 0x9d00, 0x9e00};
  uint operation_size = 1; // block or sector
  byte data_buffer[512];
  int actual_num_bytes;

  struct_system_device_entry *device_descriptor;
  
  device_descriptor = get_system_device_entry(2);
  if (device_descriptor == (struct_system_device_entry *)0x0) {
    debug_printf("NULL_device\n");
    return;
  }

  set_pre_printf_state();
  tty_printf("sect nSect(total=%d)\n",device_descriptor->num_sectors);
  check_post_printf_state_set_sio_params();

  for (uint i = 0; i < num_blocks; i++) {
    uint current_sector = block_list[i];    
    set_pre_printf_state();
    tty_printf("__%d_%d\n",current_sector,operation_size);
    check_post_printf_state_set_sio_params();
    actual_num_bytes = read_sd_blocks(2,current_sector,operation_size,data_buffer);
    if (actual_num_bytes != operation_size << 9) {
      debug_printf("err_read0");
    }
      
    fdb_print_blocks(data_buffer, current_sector, 1);
  }
}
    
#endif


#ifdef SD_RW_CHECK
// Taken from BTC-7A reverse
//       Does a non-destructive alternatving RW/Pattern test 
//       of SD Card


void fdb_sdtest(void) {
  struct_system_device_entry *device_descriptor;
  byte *existing_data_buffer;
  byte *test_buffer;
  uint actual_num_bytes;
  uint current_sector;
  uint num_bytes;
  uint end_sector;
  uint operation_size;
  
  device_descriptor = get_system_device_entry(2);
  if (device_descriptor == (struct_system_device_entry *)0x0) {
    debug_printf("NULL_device\n");
    return;
  }
  existing_data_buffer = (byte *)memoryAllocate(0x20000);
  test_buffer = (byte *)memoryAllocate(0x20000);
  if (existing_data_buffer == (byte *)0x0) {
    if (test_buffer == (byte *)0x0) {
      return;
    }
  }
  else {
    if (test_buffer == (byte *)0x0) goto LAB_8006afe0;
    set_pre_printf_state();
    tty_printf("sect nSect(total=%d)\n",device_descriptor->num_sectors);
    check_post_printf_state_set_sio_params();
    current_sector = 0;
    while( 1 ) {
      g_current_on_time_in_seconds = 0xFFFFFFFF; 
      actual_num_bytes = device_descriptor->num_sectors;
      end_sector = current_sector + 256;
      if (actual_num_bytes <= current_sector) break;
      operation_size = 0x100;
      if (actual_num_bytes <= end_sector) {
        operation_size = actual_num_bytes - current_sector;
      }
      set_pre_printf_state();
      tty_printf("__%d_%d\n",current_sector,operation_size);
      check_post_printf_state_set_sio_params();
      actual_num_bytes = read_sd_blocks(2,current_sector,operation_size,existing_data_buffer);
      num_bytes = operation_size << 9;
      if (actual_num_bytes != num_bytes) {
        debug_printf("err_read0");
      }
      bSet(test_buffer,0x55,num_bytes);
      actual_num_bytes = write_sd_blocks(2,current_sector,operation_size,test_buffer);
      if (actual_num_bytes != num_bytes) {
        debug_printf("err_write1");
      }
      actual_num_bytes = read_sd_blocks(2,current_sector,operation_size,test_buffer);
      if (actual_num_bytes != num_bytes) {
        debug_printf("err_read1");
      }
      fdb_check_buffer_contents(test_buffer,num_bytes,0x55);
      bSet(test_buffer,0xaa,num_bytes);
      actual_num_bytes = write_sd_blocks(2,current_sector,operation_size,test_buffer);
      if (actual_num_bytes != num_bytes) {
        debug_printf("err_write2");
      }
      actual_num_bytes = read_sd_blocks(2,current_sector,operation_size,test_buffer);
      if (actual_num_bytes != num_bytes) {
        debug_printf("err_read2");
      }
      fdb_check_buffer_contents(test_buffer,num_bytes,0xaa);
      actual_num_bytes = write_sd_blocks(2,current_sector,operation_size,existing_data_buffer);
      current_sector = end_sector;
      if (actual_num_bytes != num_bytes) {
        debug_printf("err_write0");
      }
    }
  }
  free(test_buffer);
  if (existing_data_buffer == (byte *)0x0) {
    return;
  }
LAB_8006afe0:
  free(existing_data_buffer);
  return;
}

#endif


#if (defined SD_POWER_CYCLE_TEST) || (defined SD_RW_CHECK)
// Check the contents of a buffer to a single byte 
//       pattern.  Report first error; total errors (if not zero)
bool fdb_check_buffer_contents(byte *buffer,uint num_bytes,uint pattern)
{
  int error_count;
  uint i;
  
  error_count = 0;
  for (i = 0; i != num_bytes; i++) {
    if (buffer[i] != pattern) {
      if (error_count <= 4) {
	set_pre_printf_state();
        tty_printf("ERROR::fdb_check_buffer_contents:err_0x%x:0x%x/0x%x\n",i,(uint)buffer[i],pattern);
	check_post_printf_state_set_sio_params();
      }
      error_count += 1;
    }
  }
  if (error_count != 0) {
    set_pre_printf_state();
    tty_printf("ERROR::fdb_check_buffer_contents:err_cnt=%d\n",error_count);
    check_post_printf_state_set_sio_params();
  }
  return error_count != 0;
}

#endif


#ifdef SD_POWER_CYCLE_TEST

// trying to reproduce a bug in which writes that happen right
//      after powerup can cause data corruption

void fdb_sd_power_cycle_test(void) {
  int pattern_size = 2;
  byte pattern[2] = {0x55, 0xAA};
  uint block_num = 0x80000;
  byte original_data[512];
  byte test_data[512];
  byte actual_data[512];
  int num_bytes; 

  //reduce_SD_clock(&g_sd_card_descriptor);
  // read the orignal data
  RdSdAddr(&g_sd_card_descriptor, block_num, 1, original_data);

  // do a bunch of R/W tests
  for (int sleep = 0; sleep < 4; sleep++) {
    set_pre_printf_state();
    tty_printf("INFO: fdb_power_cycle_test sleep:%d\n",sleep);
    check_post_printf_state_set_sio_params();
    // reduce_SD_clock(&g_sd_card_descriptor);
    for (int i = 0; i < pattern_size; i++) {
      bSet(test_data, pattern[i], 512);
      flush_processor_cache(test_data,0x200);
      // Write
      num_bytes = WrSdAddr(&g_sd_card_descriptor, block_num, 1, test_data);
      if (num_bytes != 0x200) {
	set_pre_printf_state();
	tty_printf("ERROR:fdb_power_cycle_test: result 0x%x; sleep %d, i %d : write error\n", num_bytes, sleep, i);
	check_post_printf_state_set_sio_params();
      }
      // Turn SD card off
      HceFastboot_SDPwrRecycle();
      reduce_SD_clock(&g_sd_card_descriptor);
      //initialize_default_sd_card_to_data();
      //thread_sleep((enum_timer_wait_scale) sleep , 10);
      bSet(actual_data, 0, 512);
      flush_processor_cache2(actual_data,0x200);
      num_bytes = RdSdAddr(&g_sd_card_descriptor, block_num, 1, actual_data);
      if (num_bytes != 0x200) {
	set_pre_printf_state();
	tty_printf("ERROR: fdb_power_cycle_test:result 0x%x; sleep %d, i %d : read error\n", num_bytes, sleep, i);
	check_post_printf_state_set_sio_params();
      }
      //fdb_print_blocks(actual_data, block_num, 1);
      fdb_check_buffer_contents(actual_data,512,pattern[i]);
      // Turn SD card on
      //HceFastboot_SDPwrRecycle();
      //initialize_default_sd_card_to_data();
      //thread_sleep((enum_timer_wait_scale) sleep , 10);
    }
  }

  // Write the original data back

  num_bytes =  WrSdAddr(&g_sd_card_descriptor, block_num, 1, 
		       (byte *)((uint)original_data | 0x20000000));

  set_pre_printf_state();
  tty_printf("INFO: fdb_power_cycle_test end:%d\n", num_bytes);
  check_post_printf_state_set_sio_params();

}


#endif
