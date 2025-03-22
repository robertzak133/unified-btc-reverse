// capture-timer.c
//     Adding capture timer functionality to BTC-7A, if we can

#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "capture-timer.h"
#include "rtc-formats.h"
#include "custom-set-date-time.h"

//#define DEBUG_NIGHT_VIDEO
//#define DEBUG_EVENT_ITERATOR
//#define DEBUG_TEMPERATURE_HALT

#if (defined BTC_7A)

// patches required to get baseline BTC_7E firmware to run correctly on 
//      BTC_7A

// The bit that tells us whether we're on external power, or not is in a
//     different spot.  Basedon code from the BTC-7A
bool ctm_get_power_supply_mode(void) {
  uint result_buffer [3];
  bool dummy;

  // dummy call to get the hijacked function in the symbol databse
  dummy = get_power_supply_mode();
  get_device_csr_bit(1,0x4000,result_buffer);
  return (result_buffer[0] & 0x4000) == 0;
}
#endif

#if (defined BTC_7E) && (defined DEBUG_NO_SD)

int ctm_fsm_spawn(byte allocate_p,void *iterator_function,uint param_3,uint param_4,uint param_5, void *memory) {
  int *crash_int; 
  set_pre_printf_state();
  tty_printf("ctm_fsm_spawn: we were called! \n");
  check_post_printf_state_set_sio_params();

  crash_int = (int *) 0x0;
  // reference a null pointer
  set_pre_printf_state();
  tty_printf("ctm_fsm_spawn: crashing on null ptr 0x%0x8x\n", *crash_int);
  check_post_printf_state_set_sio_params();
  return fsm_spawn(allocate_p, iterator_function, param_3, param_4, param_5, memory);
}
#endif

void ctm_tty_printf(char *format_string, uint data) {
  set_pre_printf_state();
  tty_printf(format_string, data);
  check_post_printf_state_set_sio_params();
}

#if (defined BTC_7A)
void ctm_check_event_null_function(int event_number, int event_qualifier) {
}

#endif

#ifdef BTC_7A
// This is the code that handles system events as the occur. It's only
//      here because the events for the SD_INSERT and SD_REMOVE operations
//      need to be shifted from 0x200,0x201 on the BTC-7E baseline code,
///     to 0x2000 and 0x2001 for the BTC-7A.  This because the location 
//      of the gpio has changed by 4 bits between the two camera models. 
// Note the original code may have started out as a well-structured 
//      switch() statement, but if so, Ghidra is not able to unwind it
//      all.  I have done my best match the functionality of the 
//      the decompiled original in a more readable (for me) format.
//      Wish me luck.  
void ctm_event_loop_iterator(uint event_number,uint qualifier) {
  int temp_int;
  uint temp_qualifier_upper_bytes;
  char *debug_string;
  struct_event_descriptor event_descriptor;
  
  event_descriptor_init(&g_event_descriptor);
  event_descriptor.event_number = 0;
  event_descriptor.qualifier_1 = 0;
  event_descriptor.qualifier_2 = 0;
  g_event_descriptor.event_number = event_number;
  g_event_descriptor.qualifier_1 = qualifier;
  temp_int = get_matching_event_descriptor(-1,&event_descriptor);
  // Are there any active events? 
  if (temp_int != 0) {
    switch(event_descriptor.event_number) {
    // Power On Event
    case 0xFFFFFFFF:
      // This should never be called -- just here to get "event_loop_iterator()" into the function table
      return event_loop_iterator(event_number, qualifier);
      break;
    case 0x10:
      debug_print_string(0, "INIT_===============");
      debug_print_string(0, "SP5K_MSG_HOST_TASK_INIT_-_s");
      host_task_init();
      debug_print_string(0, "SP5K_MSG_HOST_TASK_INIT_-_e");
      break;
    // Power Off Event
    case 0x20:
      debug_print_string(0, "===============_OFF");
      break;
    // Button Events
    case 0x100:
    case 0x101:
    case 0x102:
      service_button_event(event_descriptor.event_number,event_descriptor.qualifier_1);
      break;
    // SD Card Events
    case 0x202:
      break;
    case 0x203:
      debug_print_string(0,"MOUNT_COMPLETE");
      break;
    case 0x204:   
      break; // that was almost too easy
    case 0x205:
      debug_print_string(0, "DISK_ERROR_-_%d", event_descriptor.qualifier_1);
      break;
      // I moved the insert/remove events here, to match with BTC-7A GPIO.  
    case 0x2000:
      if (event_descriptor.qualifier_1 != 2) {
	debug_print_string(0,"Disc_Removal_-_%d", event_descriptor.qualifier_1);
      } else {
#ifdef DEBUG_EVENT_ITERATOR
	set_pre_printf_state();
        tty_printf("SD_REMOVAL_-_(%d)\n",2);
	check_post_printf_state_set_sio_params();
#endif
	if (get_SDCardState() == 2) {
          if ((get_g_test_mode() != 0) && (get_g_sd_card_mounted_p() != 0)) {
            vfs_unmount_wrapper2(0x10002);
          }
          set_g_sd_card_mounted_p(0);
        }
        set_sd_card_state_w_init(0xffff);
	initialize_g_mode_change_counter(1);
      }
      break;
    case 0x2001:
      if (event_descriptor.qualifier_1 != 2) {
	debug_print_string(0,"Disc_Insertion_-_%d", event_descriptor.qualifier_1);;
      } else {
#ifdef DEBUG_EVENT_ITERATOR
	set_pre_printf_state();
	tty_printf("SD_INSERT_-_(%d)\n",2);
	check_post_printf_state_set_sio_params();
#endif
	set_sd_card_state_w_init(2);
	temp_int = get_g_sd_card_valid_p();
	if (temp_int != 0) {
	  set_g_sd_card_state_valid_p(0);
	} else {
	  initialize_g_mode_change_counter(1);
	}
      }
      break;
    case 0x51510000:
      serviceEvent_0x5151000(0x51510000,event_descriptor.qualifier_1);
      break;

    // Still capture -- keeping track of stills we've started; and stills we've completed
    case 0x52510507:
      set_g_evt_0x52510507_state_initialized_p(0);
      temp_int = get_g_evt_0x52510507_counter();
      set_g_evt_0x52510507_counter(temp_int + 1);
      break;
    case 0x5251050a:
      temp_int = get_g_evt_0x5251050a_counter();
      set_g_evt_0x5251050a_counter(temp_int + 1);
      break;
    case 0x5251051e:
      set_g_evt_0x52510507_state_initialized_p(0);
      break;
    case 0x5251050f:
      setStillCapDone();
      set_g_evt_0x52510507_state_initialized_p(0);
      temp_int = get_g_evt_0x52510507_counter();
      set_g_evt_0x52510507_counter(temp_int + 1);
      break;
    // ?? 
      break;
    // ?? 
    case 0x54510101:
      g_event_descriptor.qualifier_2 = g_event_descriptor.qualifier_2 & 0xfffffffb;
      break;
    case 0x58510000:
      service_event_0x5851000(event_descriptor.qualifier_1);
      break;
    // USB connector plugged in or out
    case 0x62510005:
      debug_print_string(0, "USB IN");
      initialize_g_mode_change_counter(1);
      break;
    case 0x62510006:
      debug_print_string(0, "USB OUT");
      initialize_g_mode_change_counter(1);
      break;
    // DCF Init
    case 0x64510001:
      debug_print_string(0, "SP5k_MSG_DCF_INIT_START");
      break;
    case 0x64510003:
      debug_print_string(0, "SP5k_MSG_DCF_INIT_FAIL");
      break;
    // Fast Cap
    case 0xf0000000:
      temp_qualifier_upper_bytes = event_descriptor.qualifier_1 >> 8;
      if (temp_qualifier_upper_bytes == 1) {
	serviceSetCurrentMode_event(1,event_descriptor.qualifier_1 & 0xff);
	break;
      }
      if (temp_qualifier_upper_bytes != 7) {
	if ((temp_qualifier_upper_bytes == 8) &&
	    (temp_int = get_g_fast_cap_mount_active_p(), temp_int != 0)) {
	  debug_print_string(0, "FastCap_CST_MSG_ID_MOUNT_FAIL");
	  set_g_info_strip_enabled_p(1);
	  set_fast_cap_mount_active_p(0);
	}
	break;
      }
      if (get_g_fast_cap_mount_active_p() == 0) 
	break;
      debug_print_string(0,"FastCap_CST_MSG_ID_MOUNT_FINISH_s");
      set_g_sd_card_mounted_p(1);
      set_g_some_sd_status_p(1);
      app_init_directory_suffix_file_prefix();
      check_remaining_sd_capacity();
      set_g_info_strip_enabled_p(1);
      set_fast_cap_mount_active_p(0);
      debug_print_string(0, "FastCap_CST_MSG_ID_MOUNT_FINISH_e");
      break;
    case 0x53510516:
    case 0x53510519:
      break;
    case 0x53510517:
    case 0x5351051f:
    case 0x57510518:
    case 0x60510301:
    case 0x61510504:
    case 0x61510510:
    case 0x61510519:
    case 0x61510529:
      g_event_descriptor.qualifier_2 = g_event_descriptor.qualifier_2 & 0xfffffffb;
      break;
    default:
#ifdef DEBUG_EVENT_ITERATOR
      set_pre_printf_state();
      tty_printf("ctm_event_loop_iterator: unrecognized event number 0x%08x\n",
		 event_descriptor.event_number);
      check_post_printf_state_set_sio_params();
#endif
      g_event_descriptor.qualifier_2 = g_event_descriptor.qualifier_2 & 0xfffffffb;
      break;
    }
  }
  fsm_iterate_all_in_g_fsm_descriptor_list();
  return;
}

#endif

#if (defined BTC_7A) || (defined BTC_7E)

// A fix to the factory write to the digipyro CSR.  Two bugs fixed
//   - Resetting the bit_selector on every retry
//   - exiting the function successfully (after 0..3 retries)
//   - exiting the function with an error (after 3 retries)

void ctm_DigiPIRSpi_Write(uint csr_value) {
  int bit_start_time;
  int bit_end_time;
  int temp_int;
  uint uVar1;
  char *message;
  int retry_count;
  uint bit_selector;
  int bit_field_length;
  
  retry_count = 0;
  do {
    bit_selector = 0x1000000;
    bit_field_length = 25;
    do {
      uVar1 = bit_selector & csr_value;
      digi_pir_spi_serial_out(0);
      some_sort_of_delay(8);
      digi_pir_spi_serial_out(1);
      some_sort_of_delay(8);
      bit_selector = bit_selector >> 1;
      bit_start_time = get_fine_grained_time();
      if (uVar1 == 0) {
        digi_pir_spi_serial_out(0);
        message = "DIGIPIRSPI_SERIN_OUT_L";
      }
      else {
        digi_pir_spi_serial_out(1);
        message = "DIGIPIRSPI_SERIN_OUT_H";
      }
      log_printf(4,message);
      some_sort_of_delay(96);
      bit_end_time = get_fine_grained_time();
      temp_int = positive_diff(bit_end_time,bit_start_time);
      bit_field_length = bit_field_length + -1;
      if (300 < (uint)temp_int) {
        set_pre_printf_state();
        tty_printf("%s_PIR_LOAD_DATA_TIMEOUT_:_%d_u Retry %d\n", "DigiPIRSpi_Write" ,temp_int,
                   retry_count);
        retry_count = retry_count + 1;
        check_post_printf_state_set_sio_params();
        break;
      }
    } while (bit_field_length != 0);
    digi_pir_spi_serial_out(0);
    some_sort_of_delay(560);
    if (retry_count > 2) {
      set_pre_printf_state();
      tty_printf("DigiPIRSpi_Write Failed after %d retries", retry_count);
      check_post_printf_state_set_sio_params();
      if (retry_count > 1000) {
	// A dummy call to get the function symbol below into the symbol table
	DigiPIRSpi_Write(csr_value); 
      }
      return;
    }
  } while(bit_field_length != 0);
  log_printf(4, "DigiPIRSpi_Write-e %d retries", retry_count);

  return;
}

#endif




// Debug Patches Only
#if (defined BTC_8E_HP5) && (defined DEBUG_TEMPERATURE_HALT)

// 2025-03-16: My hypothesis is that a negagive value in temperatuer (C or F) 
//             confuses the "set_cold_item_overtemp_p()" function
//     to test -- plumb in a function that always returns a negative temperature
int ctm_get_temperatureForC(void) {
  int dummy = get_temperatureForC();
  int faked = -6;
  set_pre_printf_state();
  tty_printf("ctm_get_temperatureForC: actual= %d; faked = %d\n", 
	     dummy, faked);
  check_post_printf_state_set_sio_params();
  return (faked);
}

void ctm_set_cold_item_overtemp_p(void) {
  set_cold_item_overtemp_p();
  // now we check to see if overtemp was set
  set_pre_printf_state();
  tty_printf("ctm_set_cold_item_overtemp_p: overtemp_p = %d; night_mode_p = %d\n", 
	     g_ColdItemData.over_temp_p, get_g_night_mode_p());
  check_post_printf_state_set_sio_params();
}

#endif
 
#if (defined BTC_7A) && (defined DEBUG_NIGHT_VIDEO)
// Debug

uint ctm_get_some_system_time(int qualifier,uint *time) {
  uint result = get_some_system_time(qualifier,time);
  uint time_in_tenths = *time/100;
  struct_CameraConfig *camera_config;

  if ((time_in_tenths % 2) == 0) {
    camera_config = getCameraConfigStructPtr();
    set_pre_printf_state();
    tty_printf("ctm_get_some_system_time: time %d; current_video_length %d\n",  
	       *time, camera_config->current_video_length);
    check_post_printf_state_set_sio_params();
  }
  return result;
}

uint ctm_get_SDCardState() {
  uint result = get_SDCardState();
  set_pre_printf_state();
  tty_printf("ctm_getSDCardState: returning %d\n",  result);
  check_post_printf_state_set_sio_params();
  return result;
}

bool ctm_checkForSDCard() {
  bool result = checkForSDCard();
  set_pre_printf_state();
  tty_printf("ctm_checkForSDCard: returning %d\n", (int) result);
  check_post_printf_state_set_sio_params();
  return result;
}

uint ctm_get_power_switch_on_p() {
  uint result;
  result = get_power_switch_on_p();
  set_pre_printf_state();
  tty_printf("ctm_get_power_switch_on_p: returning %d\n", result);
  check_post_printf_state_set_sio_params();
  return result;
}

int ctm_check_hal_low_voltage() {
  int result;
  result = check_hal_low_voltage();
  set_pre_printf_state();
  tty_printf("ctm_check_hal_low_voltage: returning %d\n", result);
  check_post_printf_state_set_sio_params();
  return result;
}

int ctm_icatch_isp_load_firmware(void) {
  int return_value; 

  set_pre_printf_state();
  tty_printf("ctm_icatch_isp_load_firmware-s\n");
  return_value = icatch_isp_load_firmware();
  tty_printf("ctm_icatch_isp_load_firmware-e (%d)\n", return_value);
  check_post_printf_state_set_sio_params();
  return return_value;
}
void ctm_load_boot_parameters(void) {

  load_boot_parameters();

  // set_pre_printf_state();
  // tty_printf("cpt_load_boot_parameters:: g_image_size = 0x%08x\n", 0);
  // check_post_printf_state_set_sio_params();
}

#endif
