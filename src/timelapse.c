//
// timelapse.c
//
// Code for modifying the timelapse behavior of the camera.  This includes
//     1. Adds 1 and 2 Second Intervals to exiting menu
//     2. Adding an "All Day/Night" option to Period to existing menu
//        Night photos at reoughly 1/10 rate of day photos (to start with)

#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "volume-file-naming.h"
#include "capture-timer.h"
#include "white-flash.h"
#include "dslr-trigger.h"
#include "timelapse.h"

//#define DEBUG
//#define DEBUG1
//#define DEBUG2
//#define DEBUG3
//#define DEBUG5
//#define DEBUG6
//#define DEBUG7
//#define DEBUG_NEW_TLS_FILE


// TaskTimeLapseFSM
// Updated State Machine Table
//[0] Task 0: get snap buffer (a buffer to hold current JPG image?
//     - snap buffer available: Goto Task1
//     - snap buffer not available: Goto Task 14 [15]
//[1] Task 1: start HCETaskView_FSM
//     - Goto Task2 [2]
//[2] Task 2: Stop Task View
//     - if camera_config->field31_0x26 != 0: Goto Task 12 [12]
//     - Goto Task 3 [3]
//[3] Task 3: Set Auto Exposure
//     - if camera_config->field31_0x26 == 0: Goto Task 4 [4]
//     - else Goto Task 12 [12]
//[4] Task 4: Calculate when to take the next photo
//     - if uVar4 > 2: Goto Task12 [12]
//     - else: Goto Task 5 [5]
//[5] Task 5: more tod calculations
//     - Goto 6 [6]
//[6] Task 6: final AE; read env sensors; Snap a photo -- right here is where we snap the photo
//     - Goto 7: [7]
//[7] Task 7: Mount RAM Drive
//     - Ram Drive Mounted: Goto 8 [8]
//     - else: Goto 12a [13]
//[8] task 8: open JPG FIle: H:\DCIM\%03d%s\%s%04d.jpg
//     - JPG file opened: Goto 9 [9]
//     - else: Goto 12 [12]
//[9] task 9: spawn Mount of SD Card
//     - Goto 10 [10]
//[10] task 10: check free space on SD Card
//     - space Available: Goto 11 [11]
//     - else:            Goto 12 [12]
//[11] task 11: append JPG file to TLS file
//     - Goto 12a [13]
//[12] task 12: change mode?
//     - One Mode goto 13 [14]
//     - Another mode goto 14 [15]
//[13] task 12a: Can we go to sleep between triggers?
//     - yes -- goto 14 [15]
//     - no  -- goto 1 [1]
//[14] Task 13: Mode switch complete? 
//     - yes -- Goto 14 [15]
//[15] Task 14: End State
// 
#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) 
void (*g_wbwl_TaskTimeLapseFSM_function_array[16])() = {
  TaskTimeLapseFSM_task0,                // 0
  TaskTimeLapseFSM_task1,                // 1
  TaskTimeLapseFSM_task2,                // 2
  TaskTimeLapseFSM_task3_ae_set,         // 3
  tlps_TaskTimeLapseFSM_task4,           // 4
  TaskTimeLapseFSM_task5,                // 5
  tlps_TaskTimeLapseFSM_task6,           // 6
  tlps_TaskTimeLapseFSM_task7,           // 7
  TaskTimeLapseFSM_task8_CopyJPGFromRAM, // 8
  TaskTimeLapseFSM_task9,                // 9
  TaskTimeLapseFSM_task10_WaitMountSD,   // 10
  TaskTimeLapseFSM_task11_openTLfile,    // 11
  TaskTimeLapseFSM_task12,               // 12
  tlps_TaskTimeLapseFSM_task12a,         // 13
  TaskTimeLapseFSM_task13,               // 14
  TaskTimeLapseFSM_task14_end            // 15
};
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5) 
void (*g_wbwl_TaskTimeLapseFSM_function_array[16])() = {
  TaskTimeLapseFSM_task0,                // 0
  TaskTimeLapseFSM_task1,                // 1
  TaskTimeLapseFSM_task2,                // 2
  TaskTimeLapseFSM_task3_ae_set,         // 3
  TaskTimeLapseFSM_task4,                // 4
  TaskTimeLapseFSM_task5,                // 5
  tlps_TaskTimeLapseFSM_task6,           // 6
  tlps_TaskTimeLapseFSM_task7,           // 7
  TaskTimeLapseFSM_task8_CopyJPGFromRAM, // 8
  TaskTimeLapseFSM_task9,                // 9
  TaskTimeLapseFSM_task10_WaitMountSD,   // 10
  TaskTimeLapseFSM_task11_openTLfile,    // 11
  TaskTimeLapseFSM_task12,               // 12
  tlps_TaskTimeLapseFSM_task12a,         // 13
  TaskTimeLapseFSM_task13,               // 14
  TaskTimeLapseFSM_task14_end            // 15
};
#endif


#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5) 
struct_hp5_menu_item g_wbwl_timelapse_frequency_menu[13] = {
  { no_icon, SST_1_SP_SEC,           0, 1, 0, 1, 1},    // 1 SEC
  { no_icon, SST_2_SP_SECS,          0, 1, 0, 1, 1},    // 2 SECS
  { no_icon, SST_5_SP_SECS,          0, 1, 0, 1, 1},    // 5 SECS
  { no_icon, SST_10_SP_SECS,         0, 1, 0, 1, 1},    // 10 SECS
  { no_icon, SST_20_SP_SECS,         0, 1, 0, 1, 1},    // 20 SECS
  { no_icon, SST_30_SP_SECS,         0, 1, 0, 1, 1},    // 30 SECS
  { no_icon, SST_1_SP_MIN,           0, 1, 0, 1, 1},    // 1 MIN
  { no_icon, SST_2_SP_MINS,          0, 1, 0, 1, 1},    // 2 MINS
  { no_icon, SST_5_SP_MINS,          0, 1, 0, 1, 1},    // 5 MINS
  { no_icon, SST_10_SP_MINS,         0, 1, 0, 1, 1},    // 10 MINS
  { no_icon, SST_30_SP_MINS,         0, 1, 0, 1, 1},    // 30 MINS
  { no_icon, SST_60_SP_MINS,         0, 1, 0, 1, 1},    // 60 MINS
  { no_icon, SST_TIMELAPSE_SP_FREQ , 0, 0, 1, 3, 3}     // TIMELAPSE_FREQUENCY
};

struct_hp5_menu_item g_tlps_file_type_menu[3] = {
  { no_icon, SST__DOT_TLS,             0x00, 0x01, 0x00, 0x1, 0x1},
  { no_icon, SST__DOT_JPG,             0x00, 0x01, 0x00, 0x1, 0x1},
  { no_icon, SST_TIMELAPSE_SP_FILE,    0x00, 0x00, 0x01, 0x03, 0x03}
};

struct_hp5_menu_item g_wbwl_timelapse_period_menu[7] = {
  {no_icon, SST_ALL_SP_DAY,             0, 1, 0, 1, 1},//  ALL DAY
  {no_icon, SST_1_SP_HOUR,              0, 1, 0, 1, 1}, // 1 HOUR
  {no_icon, SST_2_SP_HOURS,             0, 1, 0, 1, 1}, // 2 HOURS
  {no_icon, SST_3_SP_HOURS,             0, 1, 0, 1, 1}, // 3 HOURS
  {no_icon, SST_4_SP_HOURS,             0, 1, 0, 1, 1}, // 4 HOURS
  {no_icon, SST_ALL_SP_DAY_SLASH_NIGHT, 0, 1, 0, 1, 1}, // ALL DAY/NIGHT
  {no_icon, SST_TIMELAPSE_SP_PERIOD,    0, 0, 1, 3, 3}  // Timelapse Period
};

#endif

// Converts from encoded timelapse frequency to a frequency 
//   (actualy an interval) in seconds
short g_wbwl_timelapse_frequency_lookup_table[12] = {
  1, 2, 5, 10, 20, 30, 60, 120, 300, 600, 1800, 3600
};

// All Day/Night Support



enum_timelapse_period_encoding tlps_get_cold_item_raw_timelapse_period(void)
{
  // Dummy function to load function below into symbol table
  get_cold_item_timelapse_period();
  // the real work. 
  return g_ColdItemData.timelapse_period;
}

enum_timelapse_period_encoding tlps_get_cold_item_cooked_timelapse_period(void)
{
  if (g_ColdItemData.timelapse_period == all_day_night) {
    return all_day;
  }
  return g_ColdItemData.timelapse_period;
}


enum_tod_in_timelapse tlps_get_tod_in_timelapse_region(struct_short_RTCTime *short_rtc_time) {
  enum_tod_in_timelapse return_value;

  if (g_ColdItemData.timelapse_period == all_day_night) {
    // This should still take photos, since we're in "all_day_mode" to the rest of the firmware
    return_value =   daylight_no_photo_region; // daylight_post_sunrise_region;
  } else {
    return_value =  get_tod_in_timelapse_region(short_rtc_time);
  }
#ifdef DEBUG3
  set_pre_printf_state();
  tty_printf("tlps_get_tod_in_timelapse_region: at %02d:%02d:%02d returning: %d\n", 
	     (int)short_rtc_time->hour, (int)short_rtc_time->minute, (int)short_rtc_time->second,
	     (int) return_value);
  check_post_printf_state_set_sio_params();  
#endif
  return return_value;
}


#ifdef DEBUG6
int tlps_get_next_wake_time(struct_short_RTCTime *short_rtc_time, enum_tod_in_timelapse timelapse_region) {
  int tod_last_photo_in_seconds = get_cold_item_tod_last_photo_in_seconds();
  int return_value = get_next_wake_time(short_rtc_time, timelapse_region);
	
#ifdef DEBUG3
  set_pre_printf_state();
  tty_printf("tlps_get_next_wake_time: at %02d:%02d:%02d in region %d; tod_last_photo: %d; returning: %d\n", 
	     (int)short_rtc_time->hour, (int)short_rtc_time->minute, (int)short_rtc_time->second,
	     (int)timelapse_region, tod_last_photo_in_seconds,
	     (int) return_value);
  check_post_printf_state_set_sio_params();  
#endif
  return return_value; 
}

ushort tlps_get_g_timelapse_wakeup_time() {
  ushort wakeup_time;
  // call internal function
  wakeup_time = get_g_timelapse_wakeup_time();

#ifdef DEBUG3
  set_pre_printf_state();
  tty_printf("tlps_get_g_timelapse_wakeup_time: returning: %d\n", 
	     (int) wakeup_time);
  check_post_printf_state_set_sio_params();  
#endif

  return wakeup_time;
}
#endif

short tlps_encoded_timelapse_frequency_to_seconds(int index) {
  short result;
  result = g_wbwl_timelapse_frequency_lookup_table[index];
  return result;
}




bool tlps_execute_if_not_null(unsigned int index) {
  void (*function_ptr)();
  bool result; 
#ifdef DEBUG5
  int start_time_in_ms;
  start_time_in_ms = get_current_operating_time_ms();
#endif

  function_ptr = g_wbwl_TaskTimeLapseFSM_function_array[index];
  result = execute_if_not_null(function_ptr);

#ifdef DEBUG5
  int end_time_in_ms;
  end_time_in_ms = get_current_operating_time_ms();
  set_pre_printf_state();
  tty_printf("TaskTimeLapseFSM: [%d] 0x%08x : %d : %d\n", 
	     index, function_ptr, start_time_in_ms, end_time_in_ms);
  check_post_printf_state_set_sio_params();
#endif

  return result;
}


void tlps_TaskTimeLapseFSM_task12a(void) {
  unsigned int encoded_timelapse_frequency;
  unsigned int timelapse_frequency_in_seconds;
  unsigned int timelapse_frequency_in_ms;
  int power_switch_on_p;

  unsigned int current_time_in_ms;
  unsigned int delta_time_in_ms;

  unsigned int sleep_time_in_ms;

  encoded_timelapse_frequency = get_cold_item_timelapse_frequency();
  timelapse_frequency_in_seconds = encoded_timelapse_frequency_to_seconds(encoded_timelapse_frequency);

  // If the next timelapse capture will be past midnight, and we're in "all day/night" mode, then create a new TLS file
  int  tod_last_photo_in_seconds = get_cold_item_tod_last_photo_in_seconds();
  enum_timelapse_period_encoding timelapse_period = tlps_get_cold_item_raw_timelapse_period();
#ifdef DEBUG_NEW_TLS_FILE
  set_pre_printf_state();
  tty_printf("tlps_TaskTimeLapseFSM_task12a:: tod_last_photo_in_seconds = %d; tlps_freq = %d; tlps_period = %d \n", 
	     tod_last_photo_in_seconds, timelapse_frequency_in_seconds, timelapse_period);
  check_post_printf_state_set_sio_params();  
#endif
  if ((timelapse_period == all_day_night) && 
      ((tod_last_photo_in_seconds + timelapse_frequency_in_seconds) > 86400)) {
#ifdef DEBUG_NEW_TLS_FILE
    set_pre_printf_state();
    tty_printf("tlps_TaskTimeLapseFSM_task12a:: creating new tls file \n", tod_last_photo_in_seconds);
    check_post_printf_state_set_sio_params();  
#endif
    set_cold_item_timelapse_new_file_p(1);
  }

  // We only want to do this once -- and by this time, we're leaving this state one way, or another
  enum_tls_file_type tls_file_type = (enum_tls_file_type) tlps_get_cold_item_file_type();
  if (tls_file_type == tls_file_type_tls) {
    // external DSLR LED off if necessary
    enum_ext_trigger ext_trigger = xtrg_get_cold_item_ext_trigger_enum();
    if (ext_trigger == xtrg_dslr) {
      xtrg_Write_LEDOff();
    }
  }
  // if the timelapse frequency is less than 4 seconds, just stay on all the time
  if (timelapse_frequency_in_seconds < 4) {
    // Escape if the switch is in the "off" state 
    power_switch_on_p = get_power_switch_on_p();
    if (power_switch_on_p == 0) {
      set_fsm_state_absolute(12);
      return;
    }

    // Go back to the beginning after inserting a delay 
    HceCommon_SetCaptureImag(0,"HceTaskTimeLapse_End");

    current_time_in_ms = get_current_operating_time_ms();
    // Wait til the frequency period has expired
    delta_time_in_ms = current_time_in_ms - g_last_timelapse_time_in_ms;
    timelapse_frequency_in_ms = timelapse_frequency_in_seconds * 1000;
    if ((delta_time_in_ms < timelapse_frequency_in_ms) && 
	(delta_time_in_ms > 0)){
      // Sleep for remaining time in this period
      sleep_time_in_ms = timelapse_frequency_in_ms - delta_time_in_ms;

#ifdef DEBUG
      set_pre_printf_state();
      tty_printf("TimelapseTask14:: Sleeping for %d ms\n", sleep_time_in_ms);
      check_post_printf_state_set_sio_params();  
#endif

      thread_sleep(times_1000, sleep_time_in_ms); 
    } 
    g_last_timelapse_time_in_ms = get_current_operating_time_ms();

    // Now we need to do some book keeping
    // We only need to do every minute -- keeps track of current temperature/pressure, etc.
    tlps_update_system_measurements();
    //
    set_fsm_state_absolute(1);
    return;
  }

  // Check to see whether we're in all-day-night mode; and if so, if we are at the start of a new day
  //       if so, set to create a new TLPS file
  
  // The usual end of things -- on the way to exiting the FSM and going to sleep
  set_fsm_state_absolute(12);

}


// tlps_update_system_measurements()
//     Since we're not allowing the camera to go to sleep when operating at
//     short timelapse interval, we need to periodicaly update these time
//     varying system paramters ourselves
void tlps_update_system_measurements() {
  // update the battery voltage
  Volt_Calib_Bat();
#if (defined BTC_8E_HP5) || (defined BTC_8E_HP4) || (defined BTC_8E)
  // update the temperature
  update_global_pressure_temperature();
  // update the pressure
  store_pressure_trend();
#elif (defined BTC_7E_HP5) || (defined BTC_7E_HP4) || (defined BTC_7E) || (defined BTC_7A)
  // update the temperature
  int temperature = temperature_sensor_getReading();
  set_g_temperature_forc(temperature);
#endif
  // update camera's view of sunrise/sunset
  update_timelapse_rise_set_times();
}


// Our own version of TaskTimLapseFSM_task4
//     Developed for debugging only; and not yet ported to HP5 cameras
//     Note that this is called in FSM function vector defined at top of this
//     file. 
//     this is a complex function, and we need to:
//         - instrument it to figure out how it works
//         - modify it to corrently handle 1-second timelapse frequency
// 2023-01-18: But first we have to get it to compile

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
void tlps_TaskTimeLapseFSM_task4(void)
{
  struct_CameraConfig *camera_config;
  enum_tod_in_timelapse current_timelapse_region;
  uint tod_last_photo_in_seconds;
  uint encoded_timelapse_frequency;
  enum_timelapse_period_encoding timelapse_encoding;
  uint current_tod_in_seconds;
  uint sunrise_time_in_seconds;
  uint sunset_time_in_seconds;
  uint pre_sunset_time_in_seconds;
  uint post_sunrise_time_in_seconds;
  int sunset_time_in_minutes;
  int pre_sunset_time_in_minutes;
  int post_sunrise_time_in_minutes;
  int sunrise_time_in_minutes;
  struct_short_RTCTime short_rtc_time;
  uint timelapse_frequency_in_seconds;
  byte abort_current_image;
  bool tod_outside_timelapse_region_p;
  
  camera_config = getCameraConfigStructPtr();
  abort_current_image = camera_config->abort_current_image_p;
  get_current_date_time_short(&short_rtc_time);
  current_timelapse_region = tlps_get_tod_in_timelapse_region(&short_rtc_time);
  update_timelapse_sunrise(&sunrise_time_in_minutes,&post_sunrise_time_in_minutes);
  update_timelapse_sunset(&pre_sunset_time_in_minutes,&sunset_time_in_minutes);
  tod_last_photo_in_seconds = 86399;
  sunrise_time_in_seconds = sunrise_time_in_minutes * 60;
  if (86400 < (uint)(sunrise_time_in_minutes * 60)) {
    sunrise_time_in_seconds = tod_last_photo_in_seconds;
  }
  post_sunrise_time_in_seconds = post_sunrise_time_in_minutes * 60;
  if (86400 < (uint)(post_sunrise_time_in_minutes * 60)) {
    post_sunrise_time_in_seconds = tod_last_photo_in_seconds;
  }
  pre_sunset_time_in_seconds = pre_sunset_time_in_minutes * 60;
  if (86400 < (uint)(pre_sunset_time_in_minutes * 60)) {
    pre_sunset_time_in_seconds = tod_last_photo_in_seconds;
  }
  sunset_time_in_seconds = sunset_time_in_minutes * 60;
  if (86400 < (uint)(sunset_time_in_minutes * 60)) {
    sunset_time_in_seconds = tod_last_photo_in_seconds;
  }
  current_tod_in_seconds =
       (uint)(ushort)short_rtc_time.minute * 60 + (uint)(ushort)short_rtc_time.hour * 3600 +
       (uint)(ushort)short_rtc_time.second;
  if (86400 < current_tod_in_seconds) {
    current_tod_in_seconds = tod_last_photo_in_seconds;
  }
  encoded_timelapse_frequency = get_cold_item_timelapse_frequency();
  timelapse_frequency_in_seconds =
       encoded_timelapse_frequency_to_seconds(encoded_timelapse_frequency);
  tod_last_photo_in_seconds = get_cold_item_tod_last_photo_in_seconds();
#ifdef DEBUG
    // 
    set_pre_printf_state();
    tty_printf("TimelapseTask4:: Prework -- tod_last_photo_in_seconds = %d \n", tod_last_photo_in_seconds);
    check_post_printf_state_set_sio_params();  
#endif
  if (current_tod_in_seconds < timelapse_frequency_in_seconds) {
    current_tod_in_seconds = current_tod_in_seconds + 86400;
  }
  if (abort_current_image == 1) {
    tod_last_photo_in_seconds = timelapse_frequency_in_seconds + tod_last_photo_in_seconds;
    if ((current_tod_in_seconds <= tod_last_photo_in_seconds) &&
	(10 < tod_last_photo_in_seconds - current_tod_in_seconds)) {
#ifdef DEBUG
    // Path (1A)
    set_pre_printf_state();
    tty_printf("TimelapseTask4:: to 5 via 1A \n");
    check_post_printf_state_set_sio_params();  
#endif
      goto LAB_8012a244;
    }
#ifdef DEBUG
    // Path (1B)
    set_pre_printf_state();
    tty_printf("TimelapseTask4:: to 12 via 1B \n");
    check_post_printf_state_set_sio_params();  
#endif
    tod_outside_timelapse_region_p = current_tod_in_seconds < tod_last_photo_in_seconds - 2;
  }
  else {
    if (current_timelapse_region == daylight_no_photo_region) {
      timelapse_encoding = get_cold_item_timelapse_period();
      if (timelapse_encoding != all_day) {
        if ((post_sunrise_time_in_seconds <= current_tod_in_seconds) &&
	    (current_tod_in_seconds - post_sunrise_time_in_seconds < 121)) {
#ifdef DEBUG
	  // Path (2B)
	  set_pre_printf_state();
	  tty_printf("TimelapseTask4:: to 5 via 2B \n");
	  check_post_printf_state_set_sio_params();  
#endif

	  goto LAB_8012a244;
	}
        tod_last_photo_in_seconds = pre_sunset_time_in_seconds - current_tod_in_seconds;
joined_r0x8012a230:
        if ((pre_sunset_time_in_seconds < current_tod_in_seconds) || (2 < tod_last_photo_in_seconds)
           ) goto LAB_8012a254;
#ifdef DEBUG
	// Path (3B)
	set_pre_printf_state();
	tty_printf("TimelapseTask4:: to 5 via 3B \n");
	check_post_printf_state_set_sio_params();  
#endif
        goto LAB_8012a244;
      }
    }
    else if ((current_timelapse_region != daylight_post_sunrise_region) &&
            (current_timelapse_region != daylight_pre_sunset_region)) {
      if (current_timelapse_region != night_no_photo_region) {
	goto LAB_8012a254;
      }
      if ((sunset_time_in_seconds <= current_tod_in_seconds) &&
         (current_tod_in_seconds - sunset_time_in_seconds < 121)) goto LAB_8012a244;
      tod_last_photo_in_seconds = sunrise_time_in_seconds - current_tod_in_seconds;
      pre_sunset_time_in_seconds = sunrise_time_in_seconds;
      goto joined_r0x8012a230;
    }
    // this is the path we're taking

    tod_outside_timelapse_region_p = tod_last_photo_in_seconds < current_tod_in_seconds;
    // 2023-01-18 -- Zak -- would you believe changing the first clause in expression below from
    //      (tod_last_photo_in_seconds - 2) to
    //      (tod_last_photo_in_seconds - 1) fixes the 1 second interval problem, for now, as this 
    //      expression is zero for time_lapse_frequency = 1 second and tod_last_photo is 0 (initial
    //      value.  
    //      I could hack this into the binary with a hand patch, but I have a feeling I may be back
    //      into this hairiest of logic fur balls. 
    if ((tod_last_photo_in_seconds - 1) + timelapse_frequency_in_seconds <= current_tod_in_seconds) {
#ifdef DEBUG
      // Path (5)
      set_pre_printf_state();
      tty_printf("TimelapseTask4::  to 5 via 5: tod_outside = %d; last_photo = %d; tod  = %d;\n",
		 tod_outside_timelapse_region_p,
		 tod_last_photo_in_seconds,
		 current_tod_in_seconds
		 );
      check_post_printf_state_set_sio_params();  
#endif
      goto LAB_8012a244;
    }
#ifdef DEBUG
    // Path (2)
    set_pre_printf_state();
    tty_printf("TimelapseTask4:: tod_outside_timelapse_region_p = %d; tod_last_photo = %d; current_tod = %d \n",
	       tod_outside_timelapse_region_p,
	       tod_last_photo_in_seconds,
	       current_tod_in_seconds
	       );
    check_post_printf_state_set_sio_params();  
#endif
  }
  if (tod_outside_timelapse_region_p) {
LAB_8012a254:
    set_fsm_state_absolute(12);
    return;
  }
#ifdef DEBUG
  // Path (4B)
  set_pre_printf_state();
  tty_printf("TimelapseTask4:: to 5 via 4B \n");
  check_post_printf_state_set_sio_params();  
#endif
LAB_8012a244:
  set_fsm_state_relative(1);
  return;
}

#endif


// Only the SpecOps models have a pressure sensor
#if (defined BTC_8E_HP5) || (defined BTC_8E_HP4) || (defined BTC_8E)

int tlps_Pressure_sensor_getReading(int * pressure, int * temperature) {
  int result;
  result = Pressure_sensor_getReading(pressure, temperature);
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("tlps__update_global_pressure_tempearture:: P=0x%08x; T=0x%08x \n",
	     *pressure, *temperature);
  check_post_printf_state_set_sio_params();  
#endif
  return(result);
}

#endif

// Timelapse File Type Support
//    - Processes a new Menu for Timelapse File type -- (default, standard) .TLS, or new ".JPG"
//    

uint tlps_get_cold_item_file_type() {
  byte result = g_ColdItemData.timelapse_file_type;
  return (uint) result;
}

void tlps_set_cold_item_file_type(uint file_type) {
  g_ColdItemData.timelapse_file_type = (byte) file_type;
}

void tlps_handle_file_type_menu() {
  byte  encoded_file_type;
  struct_CameraConfig *camera_config;
  int iVar1;
  int iVar2;
  uint index;
  
  camera_config = getCameraConfigStructPtr();
  if (camera_config->exit_menu_p_or_ir_led_on != 0) {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    encoded_file_type = tlps_get_cold_item_file_type();
    camera_config->menu_selection_1 = encoded_file_type;
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(up);
  if (((iVar1 == 1) && (encoded_file_type = 0, g_up_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(down), iVar1 == 1 &&
      (encoded_file_type = 1, g_down_button_enable == 2)))) {
    menu_get_next_menu_selection(encoded_file_type,&camera_config->menu_selection_1,1,&g_menu_root);
    menu_redraw_items(camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(left);
  if (((iVar1 == 1) && (g_left_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(right), iVar1 == 1 && (g_right_button_enable == 2)))) {
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(enter);
  if ((iVar1 == 1) && (g_enter_button_enable == 2)) {
    index = (uint)camera_config->menu_selection_1;
    camera_config->exit_menu_p_or_ir_led_on = 1;
    iVar2 = get_next_state_from_menu_enter(index,
					   g_wbwl_camera_setup_selector_array[index].menu_item_array,
					   g_wbwl_camera_setup_selector_array[index].num_array_entries,
					   &g_menu_root);
    if (iVar2 == 0xff) {
      return;
    }
    tlps_set_cold_item_file_type(camera_config->menu_selection_1);
    camera_config->commit_menu_change = 1;
  }
  else {
    iVar1 = ui_cursor_key_pressed_p(mode);
    if (iVar1 != 1) {
      return;
    }
    if (g_mode_button_enable != 2) {
      return;
    }
    camera_config->exit_menu_p_or_ir_led_on = 1;
    iVar2 = get_next_state_from_menu_mode(1,&g_menu_root);
    iVar1 = WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS + 5;
    if (iVar2 == 0xff) goto EXIT1;
  }
  iVar1 = iVar2;
EXIT1:
  set_fsm_state_absolute(iVar1);
  return;
}


// Intercept the call to HceIRCut_SetIRCutClosed()
//     if in .TLS mode -- call the native function
//     else ignore (the capture still image will 
//     set IR filter accordingly
void tlps_HceIRCut_SetIRCutClosed() {
 enum_tls_file_type tls_file_type = (enum_tls_file_type) tlps_get_cold_item_file_type();

#ifdef DEBUG7
  set_pre_printf_state();
  tty_printf("tlps_HceIRCut_SetIRCutClose() :: file_type = %d \n",
	     (uint)tls_file_type);
  check_post_printf_state_set_sio_params();  
#endif

 if (tls_file_type == tls_file_type_tls) {
   HceIRCut_SetIRCutClosed();
 }
}

// Intercept the state in the TimeLapse FSM where
//     it usually captures an image.  If not in .JPG mode
//     spawn a state machine that takes and stores a photo
//     instead
void tlps_TaskTimeLapseFSM_task6() {
  struct_photo_dimensions_int photo_dimensions; 
  int burst_size = 1; // in timelapse mode, we only take one photo
  int size_factor;
  int resolution;
  enum_tls_file_type tls_file_type = (enum_tls_file_type) tlps_get_cold_item_file_type();
  if (tls_file_type == tls_file_type_tls) {
    // external DSLR LED on if necessary
    enum_ext_trigger ext_trigger = xtrg_get_cold_item_ext_trigger_enum();
    if (ext_trigger == xtrg_dslr) {
      xtrg_Write_LEDOn();
    }
    // Then Just do the regular thing
    TaskTimeLapseFSM_task6();
  } else {
#ifdef DEBUG7
    set_pre_printf_state();
    tty_printf("tlps_TaskTimeLapseFSM_task6 :: file_type = %d ; starting photo\n",
	       (uint)tls_file_type);
  check_post_printf_state_set_sio_params();  
#endif

    // Spawn the single photo FSM
    size_factor = get_photo_size_factor(0);
    resolution = get_cold_item_photo_resolution();
    register_low_battery_display_function(still_low_battery_display_function);
    get_camera_photo_resolution(&photo_dimensions, resolution);
    startHceTaskStill_FSM
      (burst_size,size_factor,photo_dimensions.width,photo_dimensions.height,
       photo_dimensions.width_hi,photo_dimensions.height_hi, 1);
    set_fsm_state_relative(1);
  }
}

// Intercept the state in the TimeLapse FSM where
//     it usually cleans up after image cp.  If not in .JPG mode
//     spawn a state machine that takes and stores a photo
//     instead

void tlps_TaskTimeLapseFSM_task7() {
  enum_tls_file_type tls_file_type = (enum_tls_file_type) tlps_get_cold_item_file_type();
  if (tls_file_type == tls_file_type_tls) {
    // do the regular thing
    TaskTimeLapseFSM_task7();
  } else {
    // if still_fsm is complete, goto 12a (index 13)
    if (!HceTaskStillFSM_valid_p()) {
#ifdef DEBUG7
      set_pre_printf_state();
      tty_printf("tlps_TaskTimeLapseFSM_task7 :: photo complete\n");
      check_post_printf_state_set_sio_params();  
#endif
      set_fsm_state_absolute(13);
    }
  }
}

// This handles the PIR triggered photos/videos/timelapse
//      note that in my firmware, we always tread PIR triggers as things to be stored in JPG
//      which allows them to be separated from file in a TLS file
void tls_HceTaskBoot2Cap_Task0(void) {
  bool sd_card_present;
  int within_operating_hours;
  enum_timelapse_period_encoding timelapse_period;
  enum_tod_in_timelapse timelapse_region;
  enum_operation_mode operation_mode;
  uint tod_in_seconds;
  int next_state = 7; // Abort by default
  struct_short_RTCTime current_time;

  wfl_spawnIRCutFSM_per_mode();

// Call to HceIQ_PowerOnStateInit in BTC-7A moved to HceModeInitFSM_task0, as per other models
//      HceIQ_PowerOnStateInit();

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
  set_some_sd_global(1);
#endif
  sd_card_present = checkForSDCard();

  within_operating_hours = get_within_operating_hours_p();

#ifdef DEBUG1
  set_pre_printf_state();
  tty_printf("tls_HceTaskBoot2Cap_task0: sd_card_present = %d; within_operating_hours = %d \n",
	     sd_card_present, within_operating_hours);
  check_post_printf_state_set_sio_params();  
#endif
  
  // If sd card is not present,
  // or.. If we're not in the given operating hours, abort
  if ((sd_card_present == 0) || (within_operating_hours == 0)) {  
    set_fsm_state_absolute(7);  // 7 is the finish state
    return;
  }

  get_current_date_time_short(&current_time);
  set_exif_time_of_capture(&current_time);

  // Next action depends on the operating mode
  operation_mode = (enum_operation_mode) get_cold_item_operation_mode();
  switch(operation_mode) {
  case trail_camera:
    next_state = 1;
    break;
  case video:
    next_state = 3;
    break;
  case timelapse:
  default:
    // Else, invoke the standard still state machine
    next_state = 1;
   // do some timelapse book keeping
    tod_in_seconds =
      (uint)current_time.minute * 60 + (uint)current_time.hour * 3600 +
      (uint)current_time.second;
    if (tod_in_seconds >= 100000) {
      // Dummy call to get function into symbol list
      HceTaskBoot2Cap_Task0();
    }
    if (86400 < tod_in_seconds) {
      tod_in_seconds = 86399;
    }
#if (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
    set_rtc_extra_current_tod_in_seconds(tod_in_seconds);
#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
    set_cold_item_current_tod_in_seconds(tod_in_seconds);
#endif
    break;
  }

#ifdef DEBUG3
  set_pre_printf_state();
  tty_printf("tls_HceTaskBoot2Cap_task0: next_state = %d \n", next_state);
  check_post_printf_state_set_sio_params();  
#endif
  set_fsm_state_absolute(next_state);
  return;
}








