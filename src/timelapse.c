//
// timelapse.c
//
// Code for modifying the timelapse behavior of the camera.  This includes
//     1. Adds 1 and 2 Second Intervals to exiting menu
//     2. Adding an "All Day/Night" option to Period to existing menu
//        Night photos at reoughly 1/10 rate of day photos (to start with)

#include "BTC.h"
#include "WBWL.h"
#include "timelapse.h"

//#define DEBUG

// Updated State Machine Table

#if (defined BTC_7E) || (defined BTC_8E)
void (*g_wbwl_TaskTimeLapseFSM_function_array[16])() = {
  TaskTimeLapseFSM_task0,
  TaskTimeLapseFSM_task1,
  TaskTimeLapseFSM_task2,
  TaskTimeLapseFSM_task3_ae_set,
  tlps_TaskTimeLapseFSM_task4,
  TaskTimeLapseFSM_task5,
  TaskTimeLapseFSM_task6,
  TaskTimeLapseFSM_task7,
  TaskTimeLapseFSM_task8_CopyJPGFromRAM,
  TaskTimeLapseFSM_task9,
  TaskTimeLapseFSM_task10_WaitMountSD,
  TaskTimeLapseFSM_task11_openTLfile,
  TaskTimeLapseFSM_task12,
  tlps_TaskTimeLapseFSM_task12a,
  TaskTimeLapseFSM_task13,
  TaskTimeLapseFSM_task14_end
};
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4) 

void (*g_wbwl_TaskTimeLapseFSM_function_array[16])() = {
  TaskTimeLapseFSM_task0,
  TaskTimeLapseFSM_task1,
  TaskTimeLapseFSM_task2,
  TaskTimeLapseFSM_task3_ae_set,
  tlps_TaskTimeLapseFSM_task4,
  TaskTimeLapseFSM_task5,
  TaskTimeLapseFSM_task6,
  TaskTimeLapseFSM_task7,
  TaskTimeLapseFSM_task8_CopyJPGFromRAM,
  TaskTimeLapseFSM_task9,
  TaskTimeLapseFSM_task10_WaitMountSD,
  TaskTimeLapseFSM_task11_openTLfile,
  TaskTimeLapseFSM_task12,
  tlps_TaskTimeLapseFSM_task12a,
  TaskTimeLapseFSM_task13,
  TaskTimeLapseFSM_task14_end
};

#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5) 
void (*g_wbwl_TaskTimeLapseFSM_function_array[16])() = {
  TaskTimeLapseFSM_task0,
  TaskTimeLapseFSM_task1,
  TaskTimeLapseFSM_task2,
  TaskTimeLapseFSM_task3_ae_set,
  TaskTimeLapseFSM_task4,
  TaskTimeLapseFSM_task5,
  TaskTimeLapseFSM_task6,
  TaskTimeLapseFSM_task7,
  TaskTimeLapseFSM_task8_CopyJPGFromRAM,
  TaskTimeLapseFSM_task9,
  TaskTimeLapseFSM_task10_WaitMountSD,
  TaskTimeLapseFSM_task11_openTLfile,
  TaskTimeLapseFSM_task12,
  tlps_TaskTimeLapseFSM_task12a,
  TaskTimeLapseFSM_task13,
  TaskTimeLapseFSM_task14_end
};
#endif


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

// Converts from encoded timelapse frequency to a frequency 
//   (actualy an interval) in seconds
short g_wbwl_timelapse_frequency_lookup_table[12] = {
  1, 2, 5, 10, 20, 30, 60, 120, 300, 600, 1800, 3600
};

#ifdef TLPS_NIGHT_DAY
//  2023-01-12 zak: Tabled for the time being
//       degree of difficulty given complexity of code too high

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



short tlps_encoded_timelapse_frequency_to_seconds(int index) {
  short result;
  result = g_wbwl_timelapse_frequency_lookup_table[index];
  return result;
}



bool tlps_execute_if_not_null(unsigned int index) {
  void (*function_ptr)();
  bool result; 
#ifdef DEBUG
  int start_time_in_ms;
  start_time_in_ms = get_current_operating_time_ms();
#endif

  function_ptr = g_wbwl_TaskTimeLapseFSM_function_array[index];
  result = execute_if_not_null(function_ptr);

#ifdef DEBUG
  int end_time_in_ms;
  end_time_in_ms = get_current_operating_time_ms();

  set_pre_printf_state();
  tty_printf("TaskTimeLapseFSM: 0x%08x : %d : %d\n", 
	     function_ptr, start_time_in_ms, end_time_in_ms);
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
    // We only need to do every minute
    tlps_update_system_measurements();
    //
    set_fsm_state_absolute(1);
    return;
  }
  
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
#elif (defined BTC_7E_HP5) || (defined BTC_7E_HP4) || (defined BTC_7E)
  // update the temperature
  int temperature = temperature_sensor_getReading();
  set_g_temperature_forc(temperature);
#endif
  // update camera's view of sunrise/sunset
  update_timelapse_rise_set_times();
}


// Our own version of TaskTimLapseFSM_task4
//     Developed for debugging only; and not yet ported to HP4 or HP5 cameras
//     Note that this is called in FSM function vector defined at top of this
//     file. 
//     this is a complex function, and we need to:
//         - instrument it to figure out how it works
//         - modify it to corrently handle 1-second timelapse frequency
// 2023-01-18: But first we have to get it to compile

#if (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
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
  current_timelapse_region = get_tod_in_timelapse_region(&short_rtc_time);
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
