// custom-ribbon.c
//     Routines which print the creation date and time of the current image/video
//     on the playback screen so that a person can read them without a magnifying glass

#include "BTC.h"
#include "custom-ribbon.h"
#include "rtc-formats.h"

//#define DEBUG1

#define DEBUG2

// wbwl_custom_ribbon_sprintf
//     replaces a call to "local_sprintf" used to build string printed in the
//     bottom right corner of photo/video review window
//     A hand patch is require to point current call to local_sprintf to this 
//     function
//     This version adds creation date to the bottom ribbon

void wbwl_custom_ribbon_sprintf(char *buffer, char * format, 
				unsigned int current_media_index, 
				unsigned int total_num_media) {

  struct_DateTime creation_date_time;
  struct_CameraConfig *camera_config;

  struct_PosixFinfo finfo; 

  camera_config = getCameraConfigStructPtr();

  // Open the File
  char *filename = camera_config->current_filename;

  // Find the name of the file currently being viewed
#ifdef DEBUG1
  set_pre_printf_state();      
  tty_printf("WBWLDebug:: opening file: %s;\n",filename);
  check_post_printf_state_set_sio_params();
#endif

  if (wbwlFileCTimeGet(filename, &creation_date_time) == 0) {
    // if we successfully got the date/time -- print it out

#ifdef DEBUG1
    set_pre_printf_state();      
    tty_printf("WBWLDebug:: creation_date_time at 0x%08x\n", 0x8047000);
    check_post_printf_state_set_sio_params();
    set_pre_printf_state();      
    tty_printf("WBWLDebug:: creation_date_time %02d/%02d/%04d %02d:%02d:%02d\n",
	       creation_date_time.month + 1, creation_date_time.day, creation_date_time.year + 1900,
	       creation_date_time.hour, creation_date_time.minute, creation_date_time.second);
    check_post_printf_state_set_sio_params();
#endif

    enum_rtc_time_format_options time_format = (enum_rtc_time_format_options) rtc_get_cold_item_time_format();
    enum_rtc_date_format_options date_format = (enum_rtc_date_format_options) rtc_get_cold_item_date_format();
    char time_buffer[32];
  
    int hour;
    char *time_format_string; 

    switch(time_format) {
    case rtc_twelve_hour:
    default:
      if (creation_date_time.hour > 12) {
	time_format_string = "%d:%02d:%02d PM";
	hour = creation_date_time.hour - 12;
      } else {
	hour = creation_date_time.hour;
	if (hour == 0) {
	  hour = 12;
	}
	time_format_string = "%d:%02d:%02d AM";
      }
      break;
    case rtc_twenty_four_hour:
      time_format_string = "%d:%02d:%02d";
      hour = creation_date_time.hour;
      break;
    }
    
    local_sprintf(time_buffer, time_format_string, 
		  hour, creation_date_time.minute, creation_date_time.second);

    
    switch(date_format) {
    case rtc_mm_dd_yyyy:
    default:
      local_sprintf(buffer,"%02d/%02d/%04d %s  %d/%d", 
		    creation_date_time.month + 1, creation_date_time.day, creation_date_time.year + 1900,
		    time_buffer, current_media_index, total_num_media);
      break;
    case rtc_dd_mm_yyyy:
      local_sprintf(buffer,"%02d/%02d/%04d %s  %d/%d", 
		    creation_date_time.day, creation_date_time.month + 1, creation_date_time.year + 1900,
		    time_buffer, current_media_index, total_num_media);
      break;
    case rtc_yyyymmdd:
      local_sprintf(buffer,"%04d%02d%02d %s  %d/%d", 
		    creation_date_time.year + 1900, creation_date_time.month + 1, creation_date_time.day,
		    time_buffer, current_media_index, total_num_media);
      break;
    }

    // fill up the buffer 
    
    return;
    }
#ifdef DEBUG
  set_pre_printf_state();      
  tty_printf("WBWLDebug:: Could not open file %s", camera_config->current_filename);
  check_post_printf_state_set_sio_params();
#endif

  // Else, default to the old string
  local_sprintf(buffer,"%d/%d", current_media_index, total_num_media);
  return;
}

// Take date and time as a packet uint and expand it to a data structure
void cr_expand_date_time(uint compressed_date_time, struct_DateTime *expanded_date_time) {
  expanded_date_time->year = (compressed_date_time >> 0x19) + 0x50;
  expanded_date_time->month = ((compressed_date_time << 7) >> 0x1c) - 1;
  expanded_date_time->day = (compressed_date_time << 0xb) >> 0x1b;
  expanded_date_time->hour = (compressed_date_time << 0x10) >> 0x1b;
  expanded_date_time->minute = (compressed_date_time << 0x15) >> 0x1a;
  expanded_date_time->second = (compressed_date_time & 0x1f) << 1;
  expanded_date_time->unknown1 = 0;
  expanded_date_time->unknown2 = 0;
  expanded_date_time->flag = 0;
}

// like vfsFileCTimeGet, but returning the DateTime structure (in addition to Unix time)
//
int wbwlFileCTimeGet(char *filename, struct_DateTime *creation_date_time) {
  struct_PosixFinfo *finfo;
  int temp; 

  finfo = (struct_PosixFinfo *)memoryAllocate(0x438);
  if (finfo == (struct_PosixFinfo *)0x0) {
    return -1;
  } else {
#ifdef DEBUG1
    set_pre_printf_state();      
    tty_printf("WBWLDebug::  filename= %s ; finfo = 0x%08x\n", filename, finfo);
    check_post_printf_state_set_sio_params();
#endif

    temp = posix_fileinfo(filename,finfo);
    if (-1 < temp) {
      cr_expand_date_time(finfo->created_time, creation_date_time);
#ifdef DEBUG1
      set_pre_printf_state();      
      tty_printf("WBWLDebug:: raw_creation_time = 0x%08x; CDT = %02d/%02d/%04d %02d:%02d:%02d \n", 
		 finfo->created_time,
		 creation_date_time->month, creation_date_time->day, creation_date_time->year, 
		 creation_date_time->hour, creation_date_time->minute, creation_date_time->second);
      check_post_printf_state_set_sio_params();
#endif
      free(finfo);
      return 0;
    }
    free(finfo);
    return -1;
  }
  return -1;
}



// Fix the scroll bar displayed during video review
//     so that it doesn't cover up the new date/time information
//     Just move it up 10 pixels or so

// Hook to redirect call to draw the video scroll bar
//    In HandleReplayMenuVideo()
// Replace
// 80027464 d7 9a 00 08     j          draw_video_scroll_bar
// with bm_draw_video_scroll_bar 
// this function that does the same thing, except moving the whole thing up by 10 pixels
void ld_draw_video_scroll_bar(unsigned int percent_complete)
{
  // We don't want to ever call the real draw_video_scroll_bar but I need it in here
  //    to the tool picks up its symbol.  This statement should never be executed
  if (percent_complete == 0x100) {
    draw_video_scroll_bar(0xfe);
  }

  // back to the real work at hand
  draw_rectangle_wrapper(2,224-20,180,10,13);
  draw_rectangle_wrapper(4,226-20,176,6,0);
  if (percent_complete != 0xff) {
    if (100 < percent_complete) {
      percent_complete = 100;
    }
    draw_rectangle_wrapper(4,226-20,(percent_complete * 0xb0) / 100,6,2);
  }
  return;
}


// Hook to redirect call to draw the video scroll bar
//    In HandleReplayMenuVideo()
// Replace
//  800271b8 52 1c 00 0c     jal        draw_rectangle_wrapper
// with call to function below
//  which does the same thing, but moves the cleared window up 10 pixels
void ld_clear_video_scroll_bar(unsigned int right_x,
			       unsigned int bottom_y,
			       unsigned int width,
			       unsigned int height,
			       char color) {

  draw_rectangle_wrapper(right_x, bottom_y - 20 , width, height, color);
}



// Debugging the case where we get the wrong pressure and temperature on the ribbon
//      on the BTC-8E (Edge SpecOps)
//      2023-09-22: I used this to confirm that two things missing from the BTC-8E code were:
//         - pointed to the wrong I2C address
//         - referenced and internal instaed of external temperature sensor
//      I fixed these both in patches
//         But not before confirming that
//         - the sensor is a Goertek SPL06-007 (device id = 1; rev = 0)
//         - the compensation paramters are correctly read from device
//         - the compensation calculation structure matches the spec
//         - the pressure given on the display is not adjusted for altitude (makes sense)
//      Frustratingly, I was not able to get a spreadsheet version of the compensation
//          algorithm to match the output of the camera; though I was able to confirm
//          that the camera, at least, gets the *right* answer

#ifdef GOERTEK_SPL06_DEBUG

#if (defined BTC_8E) || (defined BTC_8E_HP4)
int cr_Pressure_sensor_getReading(int *pressure, int *temperature) {
  int result;
  // Do we get the right "ID" for this device


  result = Pressure_sensor_getReading(pressure, temperature);

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_Pressure_sensor_getReading: pressure: %d ; temperature: %d  \n", 
	     *pressure, *temperature);
  check_post_printf_state_set_sio_params();

  byte product_id [2];
  product_id[0] = 0x0d;
  product_id[1] = 0x00;

  read_pressure_temperature_device(product_id, sizeof(product_id));

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_Pressure_sensor_getReading: ID = 0x%0x; rev = 0x%0x\n",
	     product_id[1] >> 4, product_id[1] & 0xf);
  check_post_printf_state_set_sio_params();


  // Pressure Rate
  int pm_rate_int = 0;
  byte pm_rate[2];
  pm_rate[0] = 6;
  pm_rate[1] = 0;

  read_pressure_temperature_device(pm_rate, sizeof(pm_rate));

  pm_rate_int = pm_rate[1] >> 4;

  // Temperature Rate
  int temp_rate_int = 0;
  byte temp_rate[2];
  temp_rate[0] = 7;
  temp_rate[1] = 0;

  read_pressure_temperature_device(temp_rate, sizeof(temp_rate));

  temp_rate_int = (temp_rate[1] >> 4) && 0x7;

  // Are the coefficients and temperature ready to be read?
  for (int i = 0; i < 5; i++) {
    byte meas_cfg [2];
    meas_cfg[0] = 0x08;
    meas_cfg[1] = 0x00;
    read_pressure_temperature_device(meas_cfg, sizeof(meas_cfg));

    set_pre_printf_state();      
    tty_printf("WBWLDebug:: cr_Pressure_sensor_getReading:[%d] meas_cfg: 0x%02x  \n", 
	       i, meas_cfg[1]);
    check_post_printf_state_set_sio_params();
    if (meas_cfg[1] == 0xf7) {
      break;
    }
    thread_sleep(times_1000,2);    
  }

  // Temperature
  byte raw_temperature [4];
  raw_temperature[0] = 0x03;
  raw_temperature[1] = 0x00;
  raw_temperature[2] = 0x00;
  raw_temperature[3] = 0x00;

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_Pressure_sensor_getReading: raw_temperature [0] 0x%02x; [1] 0x%02x; [2] 0x%02x; [3] 0x%02x\n",
	     raw_temperature[0], raw_temperature[1], raw_temperature[2], raw_temperature[3]);
  check_post_printf_state_set_sio_params();

  read_pressure_temperature_device(raw_temperature, sizeof(raw_temperature));

  int raw_temperature_int = ((int)raw_temperature[1] << 16) | 
    ((int)raw_temperature[2] << 8) |
    ((int)raw_temperature[3]);

  cr_sign_extend(&raw_temperature_int, 24);

  // Pressure
  byte raw_pressure [4];
  raw_pressure[0] = 0x00;
  raw_pressure[1] = 0x00;
  raw_pressure[2] = 0x00;
  raw_pressure[3] = 0x00;
  read_pressure_temperature_device(raw_pressure, sizeof(raw_pressure));

  int raw_pressure_int = ((int)raw_pressure[1] << 16) | 
    ((int)raw_pressure[2] << 8) |
    ((int)raw_pressure[3]);

  cr_sign_extend(&raw_pressure_int, 24);

  int p_kT = g_SPL06_007_compensation_scale_table[pm_rate_int];
  int t_kT = g_SPL06_007_compensation_scale_table[temp_rate_int];
  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_Pressure_sensor_getReading: raw_temperature [0] 0x%02x; [1] 0x%02x; [2] 0x%02x; [3] 0x%02x\n",
	     raw_temperature[0], raw_temperature[1], raw_temperature[2], raw_temperature[3]);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_Pressure_sensor_getReading: raw_pressure[0] 0x%02x; [1] 0x%02x; [2] 0x%02x; [3] 0x%02x\n",
	     raw_pressure[0], raw_pressure[1], raw_pressure[2], raw_pressure[3]);  
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_Pressure_sensor_getReading\n   Raw Temperature = %d\n   Raw Pressure= %d\n   PM_rate = %d\n   p_kT = %d\n   temp_rate = %d\n   t_kT = %d\n",
	     raw_temperature_int,
	     raw_pressure_int,
	     pm_rate_int,
	     p_kT,
	     temp_rate_int,
	     t_kT);
  check_post_printf_state_set_sio_params();

  cr_read_check_compensation_coefficients(0);

  cr_print_temperature_formula(&g_pressure_temperature_coefficients, raw_temperature_int, t_kT);
  cr_print_pressure_formula(&g_pressure_temperature_coefficients, raw_temperature_int, raw_pressure_int, t_kT, p_kT);

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_Pressure_sensor_getReading: pressure: %d ; temperature: %d  \n", 
	     *pressure, *temperature);
  check_post_printf_state_set_sio_params();


  return(result);
}



// Read the compensation coefficients and print them out

void cr_read_check_compensation_coefficients(int store_flag) {
  struct_i2c_pressure_temperature_coefficients i2c_coefficients;
  struct_pressure_temperature_coefficients unpacked_coefficients;
  i2c_coefficients.address = 0x10;

  cr_print_coefficients("Currently Stored", &g_pressure_temperature_coefficients);

  read_pressure_temperature_device((byte *)&i2c_coefficients, sizeof(i2c_coefficients));

  cr_unpack_pressure_temperature_coefficients(&unpacked_coefficients, &i2c_coefficients);
  cr_print_coefficients("From Device", &unpacked_coefficients);

  cr_sign_extend_coefficients(&unpacked_coefficients);
  cr_print_coefficients("Sign Extended", &unpacked_coefficients);

#ifdef DEBUG3
  if (store_flag == 1) {
    cr_store_coefficients(&unpacked_coefficients);
    cr_print_coefficients("Stored", &g_pressure_temperature_coefficients);
  }
#endif
}

// Pretty print a formula that I can evaluate out of band
void cr_print_temperature_formula(struct_pressure_temperature_coefficients *unpacked_coefficients,  int traw, int kT) {
  
  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_temperature_formuula: (%d * 0.5) + (%d * %d)/%d \n", 
	     unpacked_coefficients->c0, unpacked_coefficients->c1, traw, kT);
  check_post_printf_state_set_sio_params();

}

// Pretty print a formula that I can evaluate out of band
void cr_print_pressure_formula(struct_pressure_temperature_coefficients *unpacked_coefficients, int traw, int praw, int t_kT, int p_kT) {
  
  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_pressure_formula: %d + ((%d/%d) * (%d + (%d/%d) * (%d + (%d/%d)*%d))) + (%d*%d/%d) + (((%d * %d) / (%d * %d)) * (%d + ((%d * %d) / %d))) \n", 
	     unpacked_coefficients->c00, praw, p_kT, 
	     unpacked_coefficients->c10, praw, p_kT, unpacked_coefficients->c20, praw, p_kT, unpacked_coefficients->c30,
	     traw, unpacked_coefficients->c01, t_kT,
	     traw, praw, t_kT, p_kT,
	     unpacked_coefficients->c11, praw, unpacked_coefficients->c21, p_kT);
	     
  check_post_printf_state_set_sio_params();

}

void cr_print_coefficients(char * title, struct_pressure_temperature_coefficients *unpacked_coefficients) {

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients: %s\n", title);
  check_post_printf_state_set_sio_params();
  
  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients= c0 = 0x%08x = %5d\n", unpacked_coefficients->c0, unpacked_coefficients->c0);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients= c1 = 0x%08x = %5d \n", unpacked_coefficients->c1, unpacked_coefficients->c1);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients= c00 = 0x%08x = %5d \n", unpacked_coefficients->c00, unpacked_coefficients->c00);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients= c10 = 0x%08x = %5d \n",  unpacked_coefficients->c10,  unpacked_coefficients->c10);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients= c01 = 0x%08x = %5d \n",  unpacked_coefficients->c01,  unpacked_coefficients->c01);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients= c11 = 0x%08x = %5d \n",  unpacked_coefficients->c11, unpacked_coefficients->c11);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients= c20 = 0x%08x = %5d\n",  unpacked_coefficients->c20, unpacked_coefficients->c20);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients= c21 = 0x%08x = %5d \n",  unpacked_coefficients->c21, unpacked_coefficients->c21);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();      
  tty_printf("WBWLDebug:: cr_print_coefficients= c30 = 0x%08x = %5d \n",  unpacked_coefficients->c30,  unpacked_coefficients->c30);
  check_post_printf_state_set_sio_params();

  }
// Unpack the packed coefficients as they come out of the pressure/temperature sensor
//        into a structure of ints. 
void cr_unpack_pressure_temperature_coefficients(struct_pressure_temperature_coefficients *unpacked_coefficients, 
						 struct_i2c_pressure_temperature_coefficients *packed_coefficients) {

  unpacked_coefficients->c0 = (((int) packed_coefficients->c0_11_4) << 4) |
    (((int) packed_coefficients->c0_3_0_c1_11_8) >> 4);

  unpacked_coefficients->c1 = (((int) packed_coefficients->c0_3_0_c1_11_8 & 0xf) << 8) |
    (((int) packed_coefficients->c1_7_0)) ;

  unpacked_coefficients->c00 = (((int) packed_coefficients->c00_19_12) << 12) |
    (((int) packed_coefficients->c00_11_4) << 4) |
    (((int) packed_coefficients->c00_3_0_c10_19_16) >> 4) ;

  unpacked_coefficients->c10 = (((int) packed_coefficients->c00_3_0_c10_19_16 & 0xf) << 16) |
    (((int) packed_coefficients->c10_15_8) << 8) |
    ((int) packed_coefficients->c10_7_0) ;

  unpacked_coefficients->c01 = (((int) packed_coefficients->c01_15_8) << 8) |
    ((int) packed_coefficients->c01_7_0) ;

  unpacked_coefficients->c11 = (((int) packed_coefficients->c11_15_8) << 8) |
    ((int) packed_coefficients->c11_7_0)  ;

  unpacked_coefficients->c20 = (((int) packed_coefficients->c20_15_8) << 8) |
    ((int) packed_coefficients->c20_7_0)  ;

  unpacked_coefficients->c21 = (((int) packed_coefficients->c21_15_8) << 8) |
    ((int) packed_coefficients->c21_7_0)  ;

  unpacked_coefficients->c30 = (((int) packed_coefficients->c30_15_8) << 8) |
    ((int) packed_coefficients->c30_7_0)  ;
}

void cr_sign_extend_coefficients(struct_pressure_temperature_coefficients *unpacked_coefficients) {
  cr_sign_extend(&unpacked_coefficients->c0, 12);
  cr_sign_extend(&unpacked_coefficients->c1, 12);
  cr_sign_extend(&unpacked_coefficients->c00, 20);
  cr_sign_extend(&unpacked_coefficients->c10, 20);
  cr_sign_extend(&unpacked_coefficients->c01, 16);
  cr_sign_extend(&unpacked_coefficients->c11, 16);
  cr_sign_extend(&unpacked_coefficients->c20, 16);
  cr_sign_extend(&unpacked_coefficients->c21, 16);
  cr_sign_extend(&unpacked_coefficients->c30, 16);
}

void cr_store_coefficients(struct_pressure_temperature_coefficients *unpacked_coefficients) {

  g_pressure_temperature_coefficients.c0 =  unpacked_coefficients->c0;
  g_pressure_temperature_coefficients.c1 =  unpacked_coefficients->c1;
  g_pressure_temperature_coefficients.c00 =  unpacked_coefficients->c00;
  g_pressure_temperature_coefficients.c10 =  unpacked_coefficients->c10;
  g_pressure_temperature_coefficients.c01 =  unpacked_coefficients->c01;
  g_pressure_temperature_coefficients.c11 =  unpacked_coefficients->c11;
  g_pressure_temperature_coefficients.c20 =  unpacked_coefficients->c20;
  g_pressure_temperature_coefficients.c21 =  unpacked_coefficients->c21;
  g_pressure_temperature_coefficients.c30 =  unpacked_coefficients->c30;

}

// Extend the sign bit
void cr_sign_extend(int *n_bit_twos_complement, int num_bits) {
  if (*n_bit_twos_complement > ((1 << (num_bits-1)) - 1)) {
    *n_bit_twos_complement -= (1 << num_bits);
  }
}

void cr_log_printf(uint level, char * string) {

  cr_read_check_compensation_coefficients(0);
  
  log_printf(level, string);
}

#endif // BTC_8E or BTC_8E_HP4

#endif // GOERTEK_SPL06_DEBUG
