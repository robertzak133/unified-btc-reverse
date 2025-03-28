// 
// (Stateful) Battery Monitor for BTC-7A
// 2021-04-22 Zak: Created
// 
// Manufacturer battery monitor is a stateless affair that 
//    uses the current voltage of the battery pack as the 
//    indicator of battery state of charge.  A simple linear
//    function maps the voltage to a % battery available, which
//    is displayed as a stylized bar graph and a % in text
//    at the bottom of the screen.  Unfortunately, the open
//    circuit (or slighly loaded) voltage of a set of EUL AA
//    batteries in series (typically installed in these cameras)
//    is known to be a poor indicator of battery state of charge.
//    making the manufacturer battery monitor all but useless for 
//    EUL batteries. 

// This patch to the firmaware of the BTC-7A is intended to fix this. 
//    This file contains code which impelements a *stateful* estimator
//    of the current state of charge of the battery.  It works like this
//      - the program is told when a new set of batteries is installed
//        in the camera, and the type of battery (E.g. EUL).  From this
//        the program knows a baseline energy capacity for the battery pack. 
//      - the program keeps track of energy consumed by the camera
//        - taking photos and/or videos in color, with different amount
//        - reviewing photos and/or videos 
//        - sitting in "sleep" mode
//        - in view of current temperature (at lower temperature, additional
//          energy is consumed in the batery itself
//      - the program creates a % charge remaining estimate by comparing
//        energy consumed, vs. energy available. 
//      - Since memory is not maintained when the camera is sleeping, we must
//        store the current estimate of consumed energy, as well as original 
//        battery capacity in a file which is stored when camera goes to 
//        sleep, and loaded when camera wakes up. A new file, BMON.BIN in the 
//        B:\USER_RES\ directory is used for this purpose. 

//  As with other examples, we will use "function scavenging" to make room for
//       the patches, rewriting setDigitalEffect to be much smaller, and using
//       freed portion of the address space for new code and data. 


// 2021-08-22 zak
//       added support for remote DSLR trigger.  When photos or videos are
//       taken, turns on the test led
//

// 2022-01-16 zak
//       Updated camera power consuption. 

// 2022-01-18 zak
//       Re-partitioned some of the source code to support modular build 
//       environment

#include "../include/BTC.h"
#include "../include/battery-monitor.h"
#include "../include/white-flash.h"
#include "../include/dslr.h"

#define WBWL_WHITE_FLASH
#define WBWL_BATTERY_STATS

#define INFO_PRINT
//#define UI_ACTIVE_PRINT
#define ERROR_PRINT
#define WARNING_PRINT
#define DEBUG_PRINT

//#define BILINEAR_DEBUG
#define BILINEAR_CODE
#define ENABLE_HOOKS


// Global Variables
extern struct_BatteryTelemetry setDigitalEffectswitchdataD_table;

#define WBWL_GLOBAL_STRUCT setDigitalEffectswitchdataD_table

// Battery Monitor Functions

// This function is called when user hits "enter" button
//   after setting clock and hardware real time clock is updated
void bm_hal_set_rtc_hook(struct_short_RTCTime *short_rtc_time) {
  // First call the function that we are hooking
  hal_set_rtc(short_rtc_time);
  // now call bm_initialize
#ifdef ENABLE_HOOKS
  // don't put any print statements here -- 
  //       this function gets called as long as the set RTC menu is 
  //       active. 
  bm_get_byte_rtc_time(&WBWL_GLOBAL_STRUCT.awake_time);
#endif
}






// Hook for initializing battery values
// Replace call to set_g_cold_item_battery_type
//   80024360 d8 11 00 0c     jal        set_g_cold_item_battery_type
// this function called when user sets battery type from display
void bm_set_g_cold_item_battery_type(unsigned int battery_type) {
  // First call the function that we are hooking
  set_g_cold_item_battery_type(battery_type);
  // now call bm_initialize
#ifdef ENABLE_HOOKS
  bm_initialize(battery_type);
#endif
}


// hook for resetting WBWL_GLOBAL_STRUCT to it's default value
//   need to replace 3 calls:
//   HceCommon_InitOptions
//        80005d5c 70 14 00 0c     jal        HceCommon_RestoreDefaultColdItem
//   handleRestoreDefaultMenu
//        80023fb4 70 14 00 0c     jal        HceCommon_RestoreDefaultColdItem
//   reeboot_for_changed_power_switch
//        8002aec4 70 14 00 0c     jal        HceCommon_RestoreDefaultColdItem
// 
void bm_HceCommon_RestoreDefaultColdItem_hook(char preserve_rtc_p) {
  // Do what this function used to do
  HceCommon_RestoreDefaultColdItem(preserve_rtc_p);
  // Now initialize WBWL_GLOBAL_STRUCT
#ifdef ENABLE_HOOKS
  bm_initialize(lithium);
#endif
}

// reset the available battery charge 
void bm_initialize(enum_battery_type battery_type) {

  WBWL_GLOBAL_STRUCT.energy_consumed = JOULES_2_FXP_UINT(0.0); // Joules
  WBWL_GLOBAL_STRUCT.cold_battery_energy_lost = JOULES_2_FXP_UINT(0.0); // Joules

  WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_no_flash = 0;
  WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_low_flash = 0;
  WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_hi_flash = 0;
  WBWL_GLOBAL_STRUCT.video_taken_this_uptime_no_flash = 0;
  WBWL_GLOBAL_STRUCT.video_taken_this_uptime_low_flash = 0;
  WBWL_GLOBAL_STRUCT.video_taken_this_uptime_hi_flash = 0;
  WBWL_GLOBAL_STRUCT.total_photos_taken_no_flash = 0;
  WBWL_GLOBAL_STRUCT.total_photos_taken_low_flash = 0;
  WBWL_GLOBAL_STRUCT.total_photos_taken_hi_flash = 0;
  WBWL_GLOBAL_STRUCT.total_video_taken_no_flash = 0;
  WBWL_GLOBAL_STRUCT.total_video_taken_low_flash = 0;
  WBWL_GLOBAL_STRUCT.total_video_taken_hi_flash = 0;

  // Initialize time counters
  bm_get_byte_rtc_time(&WBWL_GLOBAL_STRUCT.install_time);
  bm_get_byte_rtc_time(&WBWL_GLOBAL_STRUCT.awake_time);
  bm_get_byte_rtc_time(&WBWL_GLOBAL_STRUCT.asleep_time);

  WBWL_GLOBAL_STRUCT.battery_type = (short)battery_type;

#ifdef INFO_PRINT
  tty_printf("WBWL Info::bm_initialize:");
  bm_print_battery_telemetry();
#endif
}  


// Burst Photos
// Rapid Fire Burst Mode Have a different code path 
//     Need to grab that one, too
// replace         
//      8000f884 65 89 0d 0c     jal        tty_printf 


void bm_RapidFirePhotos_printf_hook(char * format_string, unsigned int delay_ms,
				    unsigned int image_width, unsigned int image_height,
				    unsigned int burst_size) {
  // Do what we are supposed to do
  tty_printf(format_string, delay_ms, image_width, image_height, burst_size);
#ifdef ENABLE_HOOKS
  bm_on_photo_burst(burst_size);
#endif
}


void bm_on_photo_burst(unsigned int burst_size) {
  enum_flash_intensity flash_intensity;
  int color_p; 

  bm_get_photo_flash_intensity_color_p(&flash_intensity, &color_p);

  unsigned int energy_per_photo = 0;

  if (burst_size == 0) {
    burst_size = 1;
  }

  if (color_p == 1) {
    switch (flash_intensity) {
      case flash_off:
	energy_per_photo = ENERGY_PHOTO_COLOR_OFF;
	break;
      case flash_low:
	energy_per_photo = ENERGY_PHOTO_COLOR_LOW;
	break;
      case flash_high:
      default:
	energy_per_photo = ENERGY_PHOTO_COLOR_HIGH;
	break;
      } 
  } else {
    switch (flash_intensity) {
      case flash_off:
	energy_per_photo = ENERGY_PHOTO_BW_OFF;
	break;
      case flash_low:
	energy_per_photo = ENERGY_PHOTO_BW_LOW;
	break;
      case flash_high:
      default:
	energy_per_photo = ENERGY_PHOTO_BW_HIGH;
	break;
      } 
  }

  unsigned int power = energy_per_photo;
  bm_increment_energy_consumed(energy_per_photo * burst_size, power);
  bm_increment_photos(burst_size, flash_intensity);

  dslr_LEDOn();

#ifdef INFO_PRINT
  set_pre_printf_state();
  tty_printf("Info::bm_on_photo_burst: burst_size: %d; energy_consumed = %u.%03d; pv this uptime = %d; pv total = %d\n",
	     burst_size, 
	     JOULES_INT(WBWL_GLOBAL_STRUCT.energy_consumed),
	     JOULES_DECIMAL(WBWL_GLOBAL_STRUCT.energy_consumed),
	     (int)WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_no_flash +
	     (int)WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_low_flash +
	     (int)WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_hi_flash,
	     (int)WBWL_GLOBAL_STRUCT.total_photos_taken_no_flash +
	     (int)WBWL_GLOBAL_STRUCT.total_photos_taken_low_flash +
	     (int)WBWL_GLOBAL_STRUCT.total_photos_taken_hi_flash);
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();
  tty_printf("Info::bm_on_photo_burst:flash_intensity: %d; color_p: %d; energy: %u\n",
	     flash_intensity, color_p, energy_per_photo);
  check_post_printf_state_set_sio_params();
#endif
}


// hook for calling on photo burst done
//
//   In HceTaskStill_end()
//        replace call to IRLedOff()
//        8001ce0c 69 23 00 0c     jal        IRLedOff

void bm_off_photo_burst_hook() {
  // First call the function we hooked
  IRLedOff();
  // then the function we want to call
  bm_off_photo_burst();
}


// After we're done taking a burst of photos, turn the indicator LED off
void bm_off_photo_burst() {
  dslr_LEDOff();
}

// Hook for calling bm_on_photo whenever a photo is taken
// replace
// call to tty_printf
//  80005f78 65 89 0d 0c     jal        tty_printf
// 
//
void bm_HceCommon_SetCaptureImage_hook(unsigned int id, char * string) {
  // call the function we're stealing
  HceCommon_SetCaptureImag(id, string);
  // now accrue photo cost
  // 2021-06-02 Zak: Disabled -- just need hook for "bm_on_photo_burst"
//#ifdef ENABLE_HOOKS
//  bm_on_photo();
//#endif
} 


// accrue a number of joules for a "still" photo -- called
//     on each photo (i.e. below the mechanism which aggregates
//     photos into bursts)
// TODO: there is a "fast burst" and a "slow burst" -- not sure if they are really
//     same energy.  Assuming for now they are.  Fortunately, the call 
//     we're intercepting also has time information in it, so we could figure
//     it out if it matters.  
void bm_on_photo() {
  enum_flash_intensity flash_intensity;
  int color_p; 

  bm_get_photo_flash_intensity_color_p(&flash_intensity, &color_p);

  unsigned int energy_per_photo = 0;

  if (color_p == 1) {
    switch (flash_intensity) {
      case flash_off:
	energy_per_photo = ENERGY_PHOTO_COLOR_OFF;
	break;
      case flash_low:
	energy_per_photo = ENERGY_PHOTO_COLOR_LOW;
	break;
      case flash_high:
      default:
	energy_per_photo = ENERGY_PHOTO_COLOR_HIGH;
	break;
      } 
  } else {
    switch (flash_intensity) {
      case flash_off:
	energy_per_photo = ENERGY_PHOTO_BW_OFF;
	break;
      case flash_low:
	energy_per_photo = ENERGY_PHOTO_BW_LOW;
	break;
      case flash_high:
      default:
	energy_per_photo = ENERGY_PHOTO_BW_HIGH;
	break;
      } 
  }

  unsigned int power = energy_per_photo;
  bm_increment_energy_consumed(energy_per_photo, power);
  bm_increment_photos(1, flash_intensity);

#ifdef INFO_PRINT
  set_pre_printf_state();
  tty_printf("Info::bm_on_photo: energy_consumed = %u.%03d; photos this uptime = %d; photos total = %d\n",
	     JOULES_INT(WBWL_GLOBAL_STRUCT.energy_consumed),
	     JOULES_DECIMAL(WBWL_GLOBAL_STRUCT.energy_consumed),
	     (int)WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_no_flash + 
	     (int)WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_low_flash + 
	     (int)WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_hi_flash,
	     (int)WBWL_GLOBAL_STRUCT.total_photos_taken_no_flash +
	     (int)WBWL_GLOBAL_STRUCT.total_photos_taken_low_flash +
	     (int)WBWL_GLOBAL_STRUCT.total_photos_taken_hi_flash
	     );
  check_post_printf_state_set_sio_params();

  set_pre_printf_state();
  tty_printf("Info::bm_on_photo: flash_intensity: %d; color_p: %d; energy: %u\n",
	     flash_intensity, color_p, energy_per_photo);
  check_post_printf_state_set_sio_params();
#endif
}


// Figure out the flash intensity and whether camera is taking a color
// or black and white image.  If this is a white flash camera, it always
// takes color photos

void bm_get_video_flash_intensity_color_p(enum enum_flash_intensity *flash_intensity, int *color_p) {
  struct_CameraConfig *camera_config;
  camera_config = getCameraConfigStructPtr();

  if (camera_config->exit_menu_p_or_ir_led_on == 0) {
    *color_p = 1;
    *flash_intensity = flash_off;
  } else {
    *color_p = 0;
    if (get_g_cold_item_led_power() == 0) {
      *flash_intensity = flash_low;
    } else {
      *flash_intensity = flash_high;
    }
  }
#ifdef WBWL_WHITE_FLASH
  // if we are a white flash camera, all photos are in color
  *color_p = 1; 
#endif 

}



void bm_get_photo_flash_intensity_color_p(enum enum_flash_intensity *flash_intensity, int *color_p) {
  struct_CameraConfig *camera_config;
  camera_config = getCameraConfigStructPtr();

  if (camera_config->still_flash_on == 0) {
    *color_p = 1;
    *flash_intensity = flash_off;
  } else {
    *color_p = 0;
    if (get_g_cold_item_led_power() == 0) {
      *flash_intensity = flash_low;
    } else {
      *flash_intensity = flash_high;
    }
  }
#ifdef WBWL_WHITE_FLASH
  // if we are a white flash camera, all photos are in color
  *color_p = 1; 
#endif 

}


// Hook for calling bm_on_video whenever a video is taken
// replace
// call to 
//    8001fe48 0d 4e 0d 0c     jal        log_printf
//
// 
//
void bm_video_log_printf_hook(unsigned int level, char * format_string, char * function_name) {
  // do the existing function
  log_printf(level, format_string, function_name);
#ifdef ENABLE_HOOKS
  // now accrue photo cost
  bm_on_video();
#endif
} 


// accrue energy associated with video
void bm_on_video(void) {
  enum_flash_intensity flash_intensity;
  int color_p;

  short video_duration;

  unsigned int power  = WATTS_2_FXP_UINT(0.0);

  video_duration = get_current_video_duration_in_seconds(); 

  bm_get_video_flash_intensity_color_p(&flash_intensity, &color_p);

  if (color_p == 1) {
    switch (flash_intensity) {
      case flash_off:
	power = POWER_VIDEO_COLOR_OFF;
	break;
      case flash_low:
	power = POWER_VIDEO_COLOR_LOW;
	break;
      case flash_high:
      default:
	power = POWER_VIDEO_COLOR_HIGH;
	break;
      } 
  } else {
    switch (flash_intensity) {
      case flash_off:
	power = POWER_VIDEO_BW_OFF;
	break;
      case flash_low:
	power = POWER_VIDEO_BW_LOW;
	break;
      case flash_high:
      default:
	power = POWER_VIDEO_BW_HIGH;
	break;
      } 
  }

  unsigned int incremental_energy = power * (unsigned int)video_duration;

  bm_increment_energy_consumed(incremental_energy, power);
  bm_increment_video((int)video_duration, flash_intensity);

  dslr_LEDOn();

#ifdef INFO_PRINT
  set_pre_printf_state();
  tty_printf("Info::bm_on_video: duration: %d; flash_intensity: %d; color_p: %d; energy: %u; video_this_uptime %d; total video: %d\n",
	     (int)video_duration, flash_intensity, color_p, incremental_energy,
	     WBWL_GLOBAL_STRUCT.video_taken_this_uptime_no_flash + 
	     WBWL_GLOBAL_STRUCT.video_taken_this_uptime_low_flash + 
	     WBWL_GLOBAL_STRUCT.video_taken_this_uptime_hi_flash,
	     WBWL_GLOBAL_STRUCT.total_video_taken_no_flash + 
	     WBWL_GLOBAL_STRUCT.total_video_taken_low_flash + 
	     WBWL_GLOBAL_STRUCT.total_video_taken_hi_flash
	     );
  check_post_printf_state_set_sio_params();
#endif
}


// hook for calling on photo burst done
//
//   In TaskRecording_FSM_task9

//       8001f7e8 69 23 00 0c     jal        IRLedOff

void bm_video_off_hook() {
  // First call the function we hooked
  IRLedOff();
  // then the function we want to call
  bm_off_video();
}


// Call this function when video is over
//      not really a battery monitor function
//      turns off test LED
void bm_off_video() {
  dslr_LEDOff();
}

// Call this function instead of the current function
// max_battercapacity - c_joules_consumed / max_battery_capacity
//   As an integer, in percent
// Substitute a call to this function for:
// 8000c2ec 85 30 00 0c     jal        get_battery_percent_from_voltage
unsigned int bm_get_current_battery_level(unsigned int voltage) {
  int result;
  
  unsigned int battery_capacity = 
    bm_get_initial_battery_capacity((enum_battery_type)WBWL_GLOBAL_STRUCT.battery_type);
  unsigned int energy_consumed = 
    WBWL_GLOBAL_STRUCT.energy_consumed +
    WBWL_GLOBAL_STRUCT.cold_battery_energy_lost;

  unsigned int factory_percent = get_battery_percent_from_voltage(voltage);
  // Don't crash if battery_capacity is somehow zero
  if (battery_capacity != 0) {
    result = (100 * (battery_capacity - energy_consumed))/ battery_capacity;
  } else {
    result = 0;
  }
#ifdef UI_ACTIVE_PRINT
  set_pre_printf_state();
  tty_printf("Info::bm_get_current_battery_level: capacity = %u.%03d; consumed =%u.%03d; result = %d; voltage = %d; factory: %d \n", 
	     JOULES_INT(battery_capacity), 
	     JOULES_DECIMAL(battery_capacity), 
	     JOULES_INT(energy_consumed), 
	     JOULES_DECIMAL(energy_consumed), 
	     result, voltage, factory_percent);
  check_post_printf_state_set_sio_params();
#endif
  return result;
}

// Replace call to "store_pressure_trend" in HcePower_CommonPowerOff()
//    jal store_pressure_trend at 80000bf54 (c1 14 00 0c)
//    with this call
void store_pressure_bm_hook(void) {
  // This is the call we're replacing -- need to do it
  store_pressure_trend();
#ifdef ENABLE_HOOKS
  // Now we can do the work we want to
  bm_StoreBatteryMonitorFile();
#endif
}


// store state to file system
//   modeled on HceCommon_StoreColdItemFile
int bm_StoreBatteryMonitorFile() {
  unsigned int file_ptr;
  unsigned int start_time_ms, end_time_ms, elapsed_time_ms;
  int return_value;

  bm_get_byte_rtc_time(&WBWL_GLOBAL_STRUCT.asleep_time);

  unsigned int photos_or_videos_taken_this_uptime = 
    WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_no_flash + 
    WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_low_flash + 
    WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_hi_flash +
    WBWL_GLOBAL_STRUCT.video_taken_this_uptime_no_flash + 
    WBWL_GLOBAL_STRUCT.video_taken_this_uptime_low_flash + 
    WBWL_GLOBAL_STRUCT.video_taken_this_uptime_hi_flash;

  WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_no_flash = 0;
  WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_low_flash = 0; 
  WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_hi_flash = 0;
  WBWL_GLOBAL_STRUCT.video_taken_this_uptime_no_flash = 0;
  WBWL_GLOBAL_STRUCT.video_taken_this_uptime_low_flash = 0; 
  WBWL_GLOBAL_STRUCT.video_taken_this_uptime_hi_flash = 0;

  // If no photos or videos were taken, assumed that time spent between cold bin time
  //    and now was taken messing with the UI, and account for appropriately
  if (photos_or_videos_taken_this_uptime == 0) {
    int elapsed_time_in_seconds = bm_get_delta_byte_time(&WBWL_GLOBAL_STRUCT.asleep_time,
							  &WBWL_GLOBAL_STRUCT.awake_time);
#ifdef INFO_PRINT
    set_pre_printf_state();
    tty_printf("Info::bm_StoreBatteryMonitorFile: Elapsed time in seconds: %d \n",
	       elapsed_time_in_seconds);
    check_post_printf_state_set_sio_params();
#endif
    
    bm_increment_energy_consumed(bm_get_ui_energy(elapsed_time_in_seconds), POWER_UI_ACTIVE);
  } 

#ifdef INFO_PRINT
  set_pre_printf_state();
  tty_printf("Info::bm_StoreBatteryMonitorFile: Sleeping at %d/%d/%d %02d:%02d:%02d\n",
	     (int)WBWL_GLOBAL_STRUCT.asleep_time.month,
	     (int)WBWL_GLOBAL_STRUCT.asleep_time.day,
	     (int)WBWL_GLOBAL_STRUCT.asleep_time.year_from_2000 + 2000,
	     (int)WBWL_GLOBAL_STRUCT.asleep_time.hour,
	     (int)WBWL_GLOBAL_STRUCT.asleep_time.minute,
	     (int)WBWL_GLOBAL_STRUCT.asleep_time.second);
  check_post_printf_state_set_sio_params();

  bm_print_battery_telemetry();
#endif

  // Now the WBWL global structure contains all the data we need to save; save it!

  start_time_ms = get_current_operating_time_ms();
  // Open file to write
  file_ptr = btc_fopen("B:\\USER_RES\\BMON.BIN", 0x20);

  if ((file_ptr == 0) && 
      (file_ptr = btc_fopen("B:\\USER_RES\\BMON.BIN", 0x24), file_ptr == 0)) {
#ifdef ERROR_PRINT
    set_pre_printf_state();
    tty_printf("Error::bm_StoreBatteryMonitorFile: failed to open BMON.BIN");
    check_post_printf_state_set_sio_params();
#endif
    return_value = 0;
  } else {
    // write file with data
    seekToSpecifiedFileLocation(file_ptr, 0, 0, 0, 0);
    unsigned int fwrite_result = btc_fwrite(file_ptr, &WBWL_GLOBAL_STRUCT, sizeof (WBWL_GLOBAL_STRUCT));
    btc_fclose(file_ptr);
    end_time_ms = get_current_operating_time_ms();
    elapsed_time_ms = positive_diff(end_time_ms, start_time_ms);
#ifdef INFO_PRINT
    set_pre_printf_state();
    tty_printf("Info::bm_StoreBatteryMonitorFile:_%d/%d_<%dms>\n", fwrite_result, sizeof(WBWL_GLOBAL_STRUCT),elapsed_time_ms);
    check_post_printf_state_set_sio_params();
#endif
    return_value = 1;
  }
  return return_value;
}


// Replace call to "Volt_Calib_Bat" in HcePower_CommonPowerOn
//    jal HcePower_Init at 80011b38 (e7 31 00 0c)
//    with this call

void bm_Volt_Calib_Bat_hook(void) {
  // call Hce_Power_Init, as we promised
  Volt_Calib_Bat();

#ifdef ENABLE_HOOKS
  // then call our own function
  bm_LoadBatteryMonitorFile();
#endif

}

// load state from file system
//     modeled after COLD.BIN code.
//     return 1 on sucess; 0 on failure
int bm_LoadBatteryMonitorFile() {
#ifdef INFO_PRINT
  set_pre_printf_state();
  tty_printf("WBWL Info::bm_on_power_up - e\n");
  check_post_printf_state_set_sio_params();
#endif
  unsigned int file_ptr;

  file_ptr = btc_fopen("B:\\USER_RES\\BMON.BIN" ,0x10);
  if (file_ptr == 0x0) {
#ifdef ERROR_PRINT
    set_pre_printf_state();
    tty_printf("Error:: %s Cannot open B:\\USER_RES\\BMON.BIN\n" ,"bm_LoadBatteryMonitorFile");
    check_post_printf_state_set_sio_params();
#endif
    // now we need to restore defaults
    bm_initialize(lithium);
    return(0);
  } else {
    unsigned int bytes_read = btc_fread(file_ptr, &WBWL_GLOBAL_STRUCT, sizeof (WBWL_GLOBAL_STRUCT));
    btc_fclose(file_ptr);
    if (bytes_read < sizeof(WBWL_GLOBAL_STRUCT)) {
      // oops
      bm_initialize(lithium);
    }
  }
  // We're only here if we could read the struct containing the last stored values
 
  // Calculate the number of hours that have gone by since we went to sleep
  bm_get_byte_rtc_time(&WBWL_GLOBAL_STRUCT.awake_time);

  int elapsed_hours = bm_get_delta_byte_time(&WBWL_GLOBAL_STRUCT.awake_time,
					      &WBWL_GLOBAL_STRUCT.asleep_time) / (3600);
 
#ifdef INFO_PRINT
  set_pre_printf_state();
  tty_printf("Info::bm_LoadBatteryMonitorFile: Elapsed time in hours since last asleep %d\n", (int)elapsed_hours);
  check_post_printf_state_set_sio_params();
#endif
  unsigned int power = ENERGY_ON_OFF; // one second
  bm_increment_energy_consumed(ENERGY_ON_OFF * elapsed_hours, power);

  // Effectively zero power -- for calculating temperature
  bm_increment_energy_consumed(POWER_JPH_STANDBY * elapsed_hours, WATTS_2_FXP_UINT(0.0)); 
  // Set the time at which the camera came on -- awake time
  //     this value used to calculate the amount of time the UI is on
  bm_get_byte_rtc_time(&WBWL_GLOBAL_STRUCT.awake_time);

#ifdef INFO_PRINT
  set_pre_printf_state();
  tty_printf("Info::bm_LoadBatteryMonitorFile: Awake at %d/%d/%d %02d:%02d:%02d\n",
	     (int)WBWL_GLOBAL_STRUCT.awake_time.month,
	     (int)WBWL_GLOBAL_STRUCT.awake_time.day,
	     (int)WBWL_GLOBAL_STRUCT.awake_time.year_from_2000 + 2000,
	     (int)WBWL_GLOBAL_STRUCT.awake_time.hour,
	     (int)WBWL_GLOBAL_STRUCT.awake_time.minute,
	     (int)WBWL_GLOBAL_STRUCT.awake_time.second);
  check_post_printf_state_set_sio_params();

  bm_print_battery_telemetry();
#endif
  return(1); // Success
}


// Private
      
unsigned int bm_get_initial_battery_capacity(enum_battery_type battery_type) {
  unsigned int return_value; 
  switch (battery_type) {
    case alkaline:
      return_value =  JOULES_2_FXP_UINT(8.0 * 14040.0);
      break;
    case lithium: 
      return_value =  JOULES_2_FXP_UINT(8.0 * 18505.0);
      break;
    default:
      // Default to lithium
#ifdef ERROR_PRINT
      set_pre_printf_state();
      tty_printf("WBWL Error::get_initial_battery_capacity -- unrecognized battery type %d\n",
		 battery_type);
      check_post_printf_state_set_sio_params();
#endif
      return_value =  JOULES_2_FXP_UINT(8.0 * 18505.0);
      break;
    } 
  return return_value;
}


// Accrue temperature related "energy" tax
//      we account for this separately
//      returns adjustment factor (tax to be added to nominal energy)
unsigned int bm_accrue_cold_battery_energy(unsigned int nominal_energy, int temp_in_f, unsigned int power, enum_battery_type battery_type) {
  unsigned int adjustment_factor = ADJ_2_FXP_UINT(0.0); // A FXP8 number > 0.0 
#ifdef BILINEAR_CODE
  unsigned int cold_battery_energy;
  // TODO -- perform a calculation!
  // For now don't adjust

  int temperature_indices[TEMPERATURE_DIM] = {-58, -40, -22, -4, 14, 32, 50, 68, 86, 104, 122};
  unsigned int power_indices[POWER_DIM] = {WATTS_2_FXP_UINT(0), WATTS_2_FXP_UINT(0.33), WATTS_2_FXP_UINT(1.35),
					   WATTS_2_FXP_UINT(3.3), WATTS_2_FXP_UINT(13.2)};
  // lookup_table[temperature][power]
  unsigned int lithium_lookup_table[TEMPERATURE_DIM][POWER_DIM] = {
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.047), ADJ_2_FXP_UINT(1.094), ADJ_2_FXP_UINT(4.0),   ADJ_2_FXP_UINT(9.0)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.032), ADJ_2_FXP_UINT(0.410), ADJ_2_FXP_UINT(1.225), ADJ_2_FXP_UINT(4.0)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.025), ADJ_2_FXP_UINT(0.135), ADJ_2_FXP_UINT(0.271), ADJ_2_FXP_UINT(1.0941)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.019), ADJ_2_FXP_UINT(0.056), ADJ_2_FXP_UINT(0.095), ADJ_2_FXP_UINT(0.396)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.011), ADJ_2_FXP_UINT(0.022), ADJ_2_FXP_UINT(0.032), ADJ_2_FXP_UINT(0.207)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.003), ADJ_2_FXP_UINT(0.014), ADJ_2_FXP_UINT(0.025), ADJ_2_FXP_UINT(0.130)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.095)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.095)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.095)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.095)},
			     {ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0),   ADJ_2_FXP_UINT(0.0), ADJ_2_FXP_UINT(0.095)}
			     };

  unsigned int alkaline_lookup_table[TEMPERATURE_DIM][POWER_DIM] = {
			     {ADJ_2_FXP_UINT(14.250), ADJ_2_FXP_UINT(14.250), ADJ_2_FXP_UINT(49.833), ADJ_2_FXP_UINT(507.333), ADJ_2_FXP_UINT(1000.0)},
			     {ADJ_2_FXP_UINT(11.200), ADJ_2_FXP_UINT(11.200), ADJ_2_FXP_UINT(21.761), ADJ_2_FXP_UINT(168.444), ADJ_2_FXP_UINT(1000.0)},
			     {ADJ_2_FXP_UINT(11.200), ADJ_2_FXP_UINT(11.200), ADJ_2_FXP_UINT(19.333), ADJ_2_FXP_UINT(60.000),  ADJ_2_FXP_UINT(1000.0)},
			     {ADJ_2_FXP_UINT(5.100),  ADJ_2_FXP_UINT(5.100),  ADJ_2_FXP_UINT(8.385),  ADJ_2_FXP_UINT(19.333),  ADJ_2_FXP_UINT(320.053)},
			     {ADJ_2_FXP_UINT(1.033),  ADJ_2_FXP_UINT(1.033),  ADJ_2_FXP_UINT(2.262),  ADJ_2_FXP_UINT(7.243),   ADJ_2_FXP_UINT(60.000)},
			     {ADJ_2_FXP_UINT(0.245),  ADJ_2_FXP_UINT(0.245),  ADJ_2_FXP_UINT(0.937),  ADJ_2_FXP_UINT(3.357), ADJ_2_FXP_UINT(11.708)},
			     {ADJ_2_FXP_UINT(0.173),  ADJ_2_FXP_UINT(0.173),   ADJ_2_FXP_UINT(0.525), ADJ_2_FXP_UINT(1.179), ADJ_2_FXP_UINT(4.648)},
			     {ADJ_2_FXP_UINT(0.173),  ADJ_2_FXP_UINT(0.173),   ADJ_2_FXP_UINT(0.356), ADJ_2_FXP_UINT(0.605), ADJ_2_FXP_UINT(2.813)},
			     {ADJ_2_FXP_UINT(0.210),  ADJ_2_FXP_UINT(0.121),   ADJ_2_FXP_UINT(0.279), ADJ_2_FXP_UINT(0.488), ADJ_2_FXP_UINT(2.050)},
			     {ADJ_2_FXP_UINT(0.052),  ADJ_2_FXP_UINT(0.052),   ADJ_2_FXP_UINT(0.212), ADJ_2_FXP_UINT(0.429), ADJ_2_FXP_UINT(1.542)},
			     {ADJ_2_FXP_UINT(0.000),  ADJ_2_FXP_UINT(0.000),   ADJ_2_FXP_UINT(0.162), ADJ_2_FXP_UINT(0.386), ADJ_2_FXP_UINT(1.234)}
			     };


  if (battery_type == lithium) {
    adjustment_factor = bm_bilinear_interpolate(temp_in_f, power, temperature_indices, power_indices, lithium_lookup_table);
  } else {
    adjustment_factor = bm_bilinear_interpolate(temp_in_f, power, temperature_indices, power_indices, alkaline_lookup_table);
  }

  cold_battery_energy = ADJ_INT(adjustment_factor * nominal_energy);

#ifdef INFO_PRINT
  tty_printf("INFO::bm_accrue_cold_battery_energy: temperature = %d; power = %d.%03d; adjustment factor = %d.%03d; cold_battery_energy = %d.%03d \n",
	     temp_in_f, WATTS_INT(power), WATTS_DECIMAL(power), ADJ_INT(adjustment_factor), ADJ_DECIMAL(adjustment_factor),
	     JOULES_INT(cold_battery_energy), JOULES_DECIMAL(cold_battery_energy));
#endif
     
  WBWL_GLOBAL_STRUCT.cold_battery_energy_lost += cold_battery_energy;                                  ;
#endif
  return adjustment_factor;
}

// Given a 2D table, with 
// https://en.wikipedia.org/wiki/Bilinear_interpolation

unsigned int bm_bilinear_interpolate(int input_x, unsigned input_y, 
				    int x_indices[TEMPERATURE_DIM], unsigned int y_indices[POWER_DIM],
				    unsigned int xy_lookup_table[TEMPERATURE_DIM][POWER_DIM]) {

  // Find X indices
  int x1_index, x2_index;

  // Limit ourselves to values in the table
  if (input_x < x_indices[0]) {
    input_x = x_indices[0];
  } else {
    if (input_x > x_indices[TEMPERATURE_DIM - 1]) {
      input_x = x_indices[TEMPERATURE_DIM -1];
    }
  }

  for (x1_index = 0; x1_index < TEMPERATURE_DIM - 1; x1_index++) {
    if ((input_x >= x_indices[x1_index]) && (input_x <= x_indices[x1_index + 1])) {
      x2_index = x1_index + 1;
      break;
    }
  }

  // Find Y indices
  int y1_index, y2_index;
  // Limit ourselves to values in the table
  if (input_y < y_indices[0]) {
    input_y = y_indices[0];
  } else {
    if (input_y > y_indices[POWER_DIM - 1]) {
      input_y = y_indices[POWER_DIM -1];
    }
  }

  for (y1_index = 0; y1_index < POWER_DIM - 1; y1_index++) {
    if ((input_y >= y_indices[y1_index]) && (input_y <= y_indices[y1_index + 1])) {
      y2_index = y1_index + 1;
      break;
    }
  }

  // Perform the bilinear interpolation
  unsigned int fQ11 = xy_lookup_table[x1_index][y1_index];
  unsigned int fQ12 = xy_lookup_table[x1_index][y2_index];
  unsigned int fQ21 = xy_lookup_table[x2_index][y1_index];
  unsigned int fQ22 = xy_lookup_table[x2_index][y2_index];

  unsigned int denominator = (x_indices[x2_index] - x_indices[x1_index]) * (y_indices[y2_index] - y_indices[y1_index]);

  unsigned int result = 
    (fQ11 * (x_indices[x2_index] - input_x) * (y_indices[y2_index] - input_y)) +
    (fQ21 * (input_x - x_indices[x1_index]) * (y_indices[y2_index] - input_y)) +
    (fQ12 * (x_indices[x2_index] - input_x) * (input_y - y_indices[y1_index])) +
    (fQ22 * (input_x - x_indices[x1_index]) * (input_y - y_indices[y1_index]));

#ifdef BILINEAR_DEBUG_PRINT
  tty_printf("DEBUG::bm_bilinear_interpolate: x1_index = %d; x2_index = %d; y1_index = %d; y2_index =%d; pre_normal result: %d.%03d \n",
	     x1_index, x2_index, y1_index, y2_index, ADJ_INT(result), ADJ_DECIMAL(result));
#endif

  result = result/denominator;

  return result; 
}


// Increment the amount of energy we consumed
//     the battery capacity should be at least as big
//     as the energy consumed. 
void bm_increment_energy_consumed(unsigned int incremental_energy, unsigned int power) {
  int ext_battery_p;

  ext_battery_p = get_power_supply_mode();

  if (ext_battery_p == 0) {
    int temp_in_f;
    enum_battery_type battery_type = WBWL_GLOBAL_STRUCT.battery_type;

    if (get_cold_item_temperature_unit_celsius_p() == 0) {
      temp_in_f = get_temperatureForC(); // this version actually reads the register
    } else {
      temp_in_f = ((get_temperatureForC() * 9) / 5) + 32; 
    }

    bm_accrue_cold_battery_energy(incremental_energy, temp_in_f, power, battery_type);
    WBWL_GLOBAL_STRUCT.energy_consumed += incremental_energy;

#ifdef INFO_PRINT
    tty_printf("INFO::bm_increment_energy_consumed: increment = %d.%03d; total = %d.%03d \n",
	       JOULES_INT(incremental_energy), JOULES_DECIMAL(incremental_energy),
	       JOULES_INT(WBWL_GLOBAL_STRUCT.energy_consumed), JOULES_DECIMAL(WBWL_GLOBAL_STRUCT.energy_consumed));
#endif

    unsigned int battery_capacity = 
      bm_get_initial_battery_capacity((enum_battery_type)WBWL_GLOBAL_STRUCT.battery_type);

    if (WBWL_GLOBAL_STRUCT.energy_consumed > battery_capacity) {
      WBWL_GLOBAL_STRUCT.energy_consumed = battery_capacity;

#ifdef INFO_PRINT
      set_pre_printf_state();
      tty_printf("Info::bm_increment_energy_consumed: consumed %u.%03d beyond battery capacity\n",
		 JOULES_INT(incremental_energy),
		 JOULES_DECIMAL(incremental_energy));
      check_post_printf_state_set_sio_params();
#endif
    }
  } else {
#ifdef INFO_PRINT
      set_pre_printf_state();
      tty_printf("Info::bm_increment_energy_consumed: no battery energy consumed -- EXT BATT mode\n");
      check_post_printf_state_set_sio_params();
#endif
  }
}


// increment the global structures for photos and video seconds taken

void bm_increment_photos(unsigned short num_photos, enum_flash_intensity flash_intensity) {
  
  int ext_battery_p = get_power_supply_mode();

  if (ext_battery_p == 0) {
    // Only accrue photos and videos if we are on battery power
    switch (flash_intensity) {
    case flash_off:
      WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_no_flash += num_photos;
      WBWL_GLOBAL_STRUCT.total_photos_taken_no_flash += num_photos;

      break;
    case flash_low:
      WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_low_flash += num_photos;
      WBWL_GLOBAL_STRUCT.total_photos_taken_low_flash += num_photos;
      break;
    case flash_high:
    default:
      WBWL_GLOBAL_STRUCT.photos_taken_this_uptime_hi_flash += num_photos;
      WBWL_GLOBAL_STRUCT.total_photos_taken_hi_flash += num_photos;
      break;
    }
  } else {
#ifdef INFO_PRINT
      set_pre_printf_state();
      tty_printf("Info::bm_increment_photos: no photos counted -- EXT BATT mode\n");
      check_post_printf_state_set_sio_params();
#endif
  }
}


void bm_increment_video(unsigned short video_seconds, enum_flash_intensity flash_intensity) {
  
  int ext_battery_p = get_power_supply_mode();

  if (ext_battery_p == 0) {
    // Only accrue video if we are on battery power
    switch (flash_intensity) {
    case flash_off:
      WBWL_GLOBAL_STRUCT.video_taken_this_uptime_no_flash += video_seconds;
      WBWL_GLOBAL_STRUCT.total_video_taken_no_flash += video_seconds;
      break;
    case flash_low:
      WBWL_GLOBAL_STRUCT.video_taken_this_uptime_low_flash += video_seconds;
      WBWL_GLOBAL_STRUCT.total_video_taken_low_flash += video_seconds;
      break;
    case flash_high:
    default:
      WBWL_GLOBAL_STRUCT.video_taken_this_uptime_hi_flash += video_seconds;
      WBWL_GLOBAL_STRUCT.total_video_taken_hi_flash += video_seconds;
      break;
    }
  }
}

// Get the amount of energy consumed by the User Interface
// If we're called, we can assume that between the time of 
// the last cold_item store, and now that we've been using the UI the
// whole time at some constant power

unsigned int bm_get_ui_energy(int elapsed_time_in_seconds) {

  unsigned int consumed_power = elapsed_time_in_seconds * POWER_UI_ACTIVE;
#ifdef INFO_PRINT
  set_pre_printf_state();
  tty_printf("Info::bm_get_ui_energy: elapsed time = %d seconds; accruing %u.%03d J\n", elapsed_time_in_seconds,
	     JOULES_INT(consumed_power), JOULES_DECIMAL(consumed_power));
  check_post_printf_state_set_sio_params();
#endif

  return consumed_power; 

}  

// get the difference between two RTC times in seconds
// TODO: this is an approximate function that has trouble with months and years of different
//       lengths which could, on certain corners, lead to a negative difference
//       for now -- I just detect this condition and return a delta of zero (which isn't right)
//       -- fix to provide an accurate difference in seconds. 
int bm_get_delta_short_time(struct_short_RTCTime *end_time, struct_short_RTCTime *start_time) {
  int delta_year, delta_month, delta_day, delta_hour, delta_minute, delta_second;
  int result_delta_seconds;

  delta_year = (int)end_time->year - (int)start_time->year;
  result_delta_seconds = delta_year * BM_SECONDS_PER_YEAR;

  delta_month = (int)end_time->month - (int)start_time->month;
  result_delta_seconds += delta_month * BM_SECONDS_PER_MONTH;

  delta_day = (int)end_time->day - (int)start_time->day;
  result_delta_seconds += delta_day * BM_SECONDS_PER_DAY;

  delta_hour = (int)end_time->hour - (int)start_time->hour;
  result_delta_seconds += delta_hour * BM_SECONDS_PER_HOUR;

  delta_minute = (int)end_time->minute - (int)start_time->minute;
  result_delta_seconds += delta_minute * BM_SECONDS_PER_MINUTE;

  delta_second = (int)end_time->second - (int)start_time->second;

  result_delta_seconds += delta_second;

  if (result_delta_seconds < 0) {
#ifdef WARNING_PRINT
    set_pre_printf_state();
    tty_printf("Warning::bm_get_delta_short_time: result_delta_seconds was negative!\n");
    check_post_printf_state_set_sio_params();
#endif
    result_delta_seconds = 0;
  }
  return(result_delta_seconds);
}


void bm_short_to_byte_rtc_time(struct_byte_RTCTime *byte_time, struct_short_RTCTime *short_time) {
  byte_time->year_from_2000 = (byte) (short_time->year - 2000);
  byte_time->month = (byte) short_time->month;
  byte_time->day = (byte) short_time->day;
  byte_time->hour = (byte) short_time->hour;
  byte_time->minute = (byte) short_time->minute;
  byte_time->second = (byte) short_time->second;
}


void bm_get_byte_rtc_time(struct_byte_RTCTime *byte_time) {
  struct_short_RTCTime short_time;

  get_short_rtc_time(&short_time);  
  bm_short_to_byte_rtc_time(byte_time, &short_time);
 
}



// get the difference between two RTC times in seconds
// TODO: this is an approximate function that has trouble with months and years of different
//       lengths which could, on certain corners, lead to a negative difference
//       for now -- I just detect this condition and return a delta of zero (which isn't right)
//       -- fix to provide an accurate difference in seconds. 
int bm_get_delta_byte_time(struct_byte_RTCTime *end_time, struct_byte_RTCTime *start_time) {
  int delta_year, delta_month, delta_day, delta_hour, delta_minute, delta_second;
  int result_delta_seconds;

  delta_year = (int)end_time->year_from_2000 - (int)start_time->year_from_2000;
  result_delta_seconds = delta_year * BM_SECONDS_PER_YEAR;

  delta_month = (int)end_time->month - (int)start_time->month;
  result_delta_seconds += delta_month * BM_SECONDS_PER_MONTH;

  delta_day = (int)end_time->day - (int)start_time->day;
  result_delta_seconds += delta_day * BM_SECONDS_PER_DAY;

  delta_hour = (int)end_time->hour - (int)start_time->hour;
  result_delta_seconds += delta_hour * BM_SECONDS_PER_HOUR;

  delta_minute = (int)end_time->minute - (int)start_time->minute;
  result_delta_seconds += delta_minute * BM_SECONDS_PER_MINUTE;

  delta_second = (int)end_time->second - (int)start_time->second;

  result_delta_seconds += delta_second;

  if (result_delta_seconds < 0) {
#ifdef WARNING_PRINT
    set_pre_printf_state();
    tty_printf("Warning::bm_get_delta_short_time: result_delta_seconds was negative!\n");
    check_post_printf_state_set_sio_params();
#endif
    result_delta_seconds = 0;
  }
  return(result_delta_seconds);
}

void bm_write_summary_file(void) {
  unsigned int file_ptr;
  unsigned int fopen_result;
  char filename[] = BATTERY_LOG_FILENAME;

#ifdef INFO_PRINT
  tty_printf("Info::bm_write_summary_file: writing summary to %s \n", filename);
  bm_print_battery_telemetry();
#endif

  // Open up the file for output

  file_ptr = btc_fopen(filename, 0x20);

  if ((file_ptr == 0) && 
      (file_ptr = btc_fopen(filename, 0x24), file_ptr == 0)) {     
#ifdef ERROR_PRINT
    tty_printf("Error::bm_write_summary_file -- could not open: %s for writing\n",
	       filename);
#endif
    return;
  }
  bm_fprint_battery_telemetry(file_ptr);
}


void bm_fprint_battery_telemetry(unsigned int fptr) {
  char buffer[256];
  int num_bytes;
  // 


  num_bytes = local_sprintf(buffer, "WBWL Trail Camera Battery Report\n\n");
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

#ifdef WBWL_BATTERY_STATS
  ushort battery_voltage_x100;

  battery_voltage_x100 = get_battery_voltage_x100();

  num_bytes = local_sprintf(buffer,"Current Battery Voltage: %d.%02d Volts\n", 
			    (uint) (battery_voltage_x100 / 100), 
			    (uint) (battery_voltage_x100 % 100));
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 
#endif


  num_bytes = local_sprintf(buffer, "Install Date/Time: %02d/%02d/%04d %02d:%02d:%02d\n",
			    (int)WBWL_GLOBAL_STRUCT.install_time.month, (int)WBWL_GLOBAL_STRUCT.install_time.day,
			    (int)WBWL_GLOBAL_STRUCT.install_time.year_from_2000 + 2000,
			    (int)WBWL_GLOBAL_STRUCT.install_time.hour, (int)WBWL_GLOBAL_STRUCT.install_time.minute, 
			    (int)WBWL_GLOBAL_STRUCT.install_time.second);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

  struct_byte_RTCTime current_time;
  bm_get_byte_rtc_time(&current_time);

  num_bytes = local_sprintf(buffer, "Removal Date/Time: %02d/%02d/%04d %02d:%02d:%02d\n\n", 
			    (int)current_time.month, (int)current_time.day, (int)current_time.year_from_2000 + 2000,
			    (int)current_time.hour, (int)current_time.minute, (int)current_time.second);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

  enum_battery_type battery_type = (enum_battery_type)WBWL_GLOBAL_STRUCT.battery_type;
  char* battery_type_string = "Lithium ";

  if (battery_type != lithium) {
    battery_type_string = "Alkaline";
  }

  num_bytes = local_sprintf(buffer, "Battery Type: %s\n\n", battery_type_string );
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

  unsigned int battery_capacity = 
    bm_get_initial_battery_capacity((enum_battery_type)WBWL_GLOBAL_STRUCT.battery_type);

  num_bytes = local_sprintf(buffer, "Total Init Batt Energy: %6d.%03d Joules\n", 
			    JOULES_INT(battery_capacity),
			    JOULES_DECIMAL(battery_capacity));
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 
  
  num_bytes = local_sprintf(buffer, "       Energy Consumed: %6d.%03d Joules\n", 
			    JOULES_INT(WBWL_GLOBAL_STRUCT.energy_consumed), 
			    JOULES_DECIMAL(WBWL_GLOBAL_STRUCT.energy_consumed));
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

  num_bytes = local_sprintf(buffer, "   Cold Battery Energy: %6d.%03d Joules\n", 
  			    JOULES_INT(WBWL_GLOBAL_STRUCT.cold_battery_energy_lost), 
  			    JOULES_DECIMAL(WBWL_GLOBAL_STRUCT.cold_battery_energy_lost));
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 
  
  unsigned int energy_available;

  if ((WBWL_GLOBAL_STRUCT.energy_consumed + WBWL_GLOBAL_STRUCT.cold_battery_energy_lost) > battery_capacity) {
    energy_available = JOULES_2_FXP_UINT(0.0);
  } else {
    energy_available = battery_capacity - 
      WBWL_GLOBAL_STRUCT.energy_consumed - WBWL_GLOBAL_STRUCT.cold_battery_energy_lost;
  }
 
  num_bytes = local_sprintf(buffer, "      Remaining Energy: %6d.%03d Joules\n", 
			    JOULES_INT(energy_available),
			    JOULES_DECIMAL(energy_available));
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 
  
  num_bytes = local_sprintf(buffer, "    Fraction Available: %d percent\n\n", 
			    (100 * energy_available) / battery_capacity);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 
  
  unsigned int total_photos_taken;
  total_photos_taken = 
    WBWL_GLOBAL_STRUCT.total_photos_taken_no_flash + 
    WBWL_GLOBAL_STRUCT.total_photos_taken_low_flash +
    WBWL_GLOBAL_STRUCT.total_photos_taken_hi_flash;
  num_bytes = local_sprintf(buffer, "Total Photos Taken    : %d \n", 
			    total_photos_taken);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 
  
  num_bytes = local_sprintf(buffer, "   - No Flash         : %d \n", 
			    WBWL_GLOBAL_STRUCT.total_photos_taken_no_flash);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 
  
  num_bytes = local_sprintf(buffer, "   - LowFlash         : %d \n", 
			    WBWL_GLOBAL_STRUCT.total_photos_taken_low_flash);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

  num_bytes = local_sprintf(buffer, "   - HiFlash          : %d \n\n", 
			    WBWL_GLOBAL_STRUCT.total_photos_taken_hi_flash);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

  unsigned int total_video_taken;
  total_video_taken = 
    WBWL_GLOBAL_STRUCT.total_video_taken_no_flash + 
    WBWL_GLOBAL_STRUCT.total_video_taken_low_flash +
    WBWL_GLOBAL_STRUCT.total_video_taken_hi_flash;

  int hours, minutes, seconds;

  bm_seconds_to_hms(total_video_taken, &hours, &minutes, &seconds);
  num_bytes = local_sprintf(buffer, "Total Video Taken     : %02d:%02d:%02d \n", 
			    hours, minutes, seconds);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 
   
  bm_seconds_to_hms(WBWL_GLOBAL_STRUCT.total_video_taken_no_flash, &hours, &minutes, &seconds);
  num_bytes = local_sprintf(buffer, "   - No Flash         : %02d:%02d:%02d \n", 
			    hours, minutes, seconds);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

  bm_seconds_to_hms(WBWL_GLOBAL_STRUCT.total_video_taken_low_flash, &hours, &minutes, &seconds);
  num_bytes = local_sprintf(buffer, "   - LowFlash         : %02d:%02d:%02d \n",
			    hours, minutes, seconds);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

  bm_seconds_to_hms(WBWL_GLOBAL_STRUCT.total_video_taken_hi_flash, &hours, &minutes, &seconds);
  num_bytes = local_sprintf(buffer, "   - HiFlash          : %02d:%02d:%02d \n",
			    hours, minutes, seconds);
  if (btc_fwrite(fptr, buffer, num_bytes) != num_bytes) goto error; 

  btc_fclose(fptr);
  return;
 error: 
  btc_fclose(fptr);
  tty_printf("Error::bm_print_summary_file -- write failure 14\n");
  return;
}


void bm_print_battery_telemetry(void) {
  char buffer[256];
  int num_bytes; 
  // 
  num_bytes = local_sprintf(buffer, "WBWL Trail Camera Battery Report\n\n");
  tty_printf("%s", buffer);

#ifdef WBWL_BATTERY_STATS
  short battery_voltage_x100;

  battery_voltage_x100 = get_battery_voltage_x100();

  num_bytes = local_sprintf(buffer,"Current Battery Voltage: %d.%02d Volts\n", 
			    (uint) (battery_voltage_x100 / 100), 
			    (uint) (battery_voltage_x100 % 100));
  tty_printf("%s", buffer);
  tty_printf_battery_stats();
#endif


  num_bytes = local_sprintf(buffer, "Install Date/Time: %02d/%02d/%04d %02d:%02d:%02d\n",
			    (int)WBWL_GLOBAL_STRUCT.install_time.month, (int)WBWL_GLOBAL_STRUCT.install_time.day,
			    (int)WBWL_GLOBAL_STRUCT.install_time.year_from_2000 + 2000,
			    (int)WBWL_GLOBAL_STRUCT.install_time.hour, (int)WBWL_GLOBAL_STRUCT.install_time.minute, 
			    (int)WBWL_GLOBAL_STRUCT.install_time.second);
  tty_printf("%s", buffer);

  struct_short_RTCTime current_time;
  get_short_rtc_time(&current_time);

  num_bytes = local_sprintf(buffer, "Removal Date/Time: %02d/%02d/%04d %02d:%02d:%02d\n\n", 
			    (int)current_time.month, (int)current_time.day, (int)current_time.year,
			    (int)current_time.hour,  (int)current_time.minute, (int)current_time.second);
  tty_printf("%s", buffer);

  enum_battery_type battery_type = (enum_battery_type)WBWL_GLOBAL_STRUCT.battery_type;
  char* battery_type_string = "Lithium ";
  if (battery_type != lithium) {
    battery_type_string = "Alkaline";
  }

  num_bytes = local_sprintf(buffer, "Battery Type: %s\n\n", battery_type_string );
  tty_printf("%s", buffer);

  unsigned int battery_capacity = 
    bm_get_initial_battery_capacity((enum_battery_type)WBWL_GLOBAL_STRUCT.battery_type);

  num_bytes = local_sprintf(buffer, "Total Energy Available: %d.%03d Joules\n", 
			    JOULES_INT(battery_capacity),
			    JOULES_DECIMAL(battery_capacity));
  tty_printf("%s", buffer);
  
  num_bytes = local_sprintf(buffer, "       Energy Consumed: %d.%03d Joules\n", 
			    JOULES_INT(WBWL_GLOBAL_STRUCT.energy_consumed), 
			    JOULES_DECIMAL(WBWL_GLOBAL_STRUCT.energy_consumed));
  tty_printf("%s", buffer);

  num_bytes = local_sprintf(buffer, "   Cold Battery Energy: %d.%03d Joules\n", 
  			    JOULES_INT(WBWL_GLOBAL_STRUCT.cold_battery_energy_lost), 
  			    JOULES_DECIMAL(WBWL_GLOBAL_STRUCT.cold_battery_energy_lost));
  tty_printf("%s", buffer);
  
  unsigned int energy_available;

  if ((WBWL_GLOBAL_STRUCT.energy_consumed + WBWL_GLOBAL_STRUCT.cold_battery_energy_lost) > battery_capacity) {
    energy_available = JOULES_2_FXP_UINT(0.0);
  } else {
    energy_available = battery_capacity - 
      WBWL_GLOBAL_STRUCT.energy_consumed - WBWL_GLOBAL_STRUCT.cold_battery_energy_lost;
  }

  num_bytes = local_sprintf(buffer, "      Remaining Energy: %d.%03d Joules\n", 
			    JOULES_INT(energy_available),
			    JOULES_DECIMAL(energy_available));
  tty_printf("%s", buffer);
  
  num_bytes = local_sprintf(buffer, "    Fraction Available: %d percent\n\n", 
			    (100 * energy_available) / battery_capacity);
  tty_printf("%s", buffer);
  
  unsigned int total_photos_taken;
  total_photos_taken = 
    WBWL_GLOBAL_STRUCT.total_photos_taken_no_flash + 
    WBWL_GLOBAL_STRUCT.total_photos_taken_low_flash +
    WBWL_GLOBAL_STRUCT.total_photos_taken_hi_flash;
  num_bytes = local_sprintf(buffer, "Total Photos Taken    : %d \n", 
			    total_photos_taken);
  tty_printf("%s", buffer);
  
  num_bytes = local_sprintf(buffer, "  - no Flash          : %d \n", 
			    WBWL_GLOBAL_STRUCT.total_photos_taken_no_flash);
  tty_printf("%s", buffer);
  
  num_bytes = local_sprintf(buffer, "  - low Flash         : %d \n", 
			    WBWL_GLOBAL_STRUCT.total_photos_taken_low_flash);
  tty_printf("%s", buffer);

  num_bytes = local_sprintf(buffer, "  - hi Flash          : %d \n\n", 
			    WBWL_GLOBAL_STRUCT.total_photos_taken_hi_flash);
  tty_printf("%s", buffer);
  
  unsigned int total_video_taken;
  total_video_taken = 
    WBWL_GLOBAL_STRUCT.total_video_taken_no_flash + 
    WBWL_GLOBAL_STRUCT.total_video_taken_low_flash +
    WBWL_GLOBAL_STRUCT.total_video_taken_hi_flash;

  int hours, minutes, seconds;

  bm_seconds_to_hms(total_video_taken, &hours, &minutes, &seconds);
  num_bytes = local_sprintf(buffer, "Total Video Taken    %d seconds;  %02d:%02d:%02d \n", 
			    total_video_taken, hours, minutes, seconds);
  tty_printf("%s", buffer);
  
  bm_seconds_to_hms(WBWL_GLOBAL_STRUCT.total_video_taken_no_flash, &hours, &minutes, &seconds);
  num_bytes = local_sprintf(buffer, "  - no Flash           : %02d:%02d:%02d \n", 
			    hours, minutes, seconds);
  tty_printf("%s", buffer);

  bm_seconds_to_hms(WBWL_GLOBAL_STRUCT.total_video_taken_low_flash, &hours, &minutes, &seconds);
  num_bytes = local_sprintf(buffer, "  - low Flash          : %02d:%02d:%02d \n",
			    hours, minutes, seconds);
  tty_printf("%s", buffer);

  bm_seconds_to_hms(WBWL_GLOBAL_STRUCT.total_video_taken_hi_flash, &hours, &minutes, &seconds);
  num_bytes = local_sprintf(buffer, "  - hi Flash           : %02d:%02d:%02d \n",
			    hours, minutes, seconds);
  tty_printf("%s", buffer);


#ifdef BILINEAR_DEBUG_PRINT
  // Testing the bilinear lookup
  tty_printf("DEBUG::bm_print_battery_telemetry: Testing series of inputs \n");
  for(int temperature = -10; temperature < 80; temperature += 10) {
    tty_printf("temperature = %d -------------------\n", temperature);
    for(unsigned int power = WATTS_2_FXP_UINT(0.0); power < WATTS_2_FXP_UINT(10.0); power += WATTS_2_FXP_UINT(2.0)) {
      unsigned int adjustment_factor;
      adjustment_factor = bm_accrue_cold_battery_energy(0, temperature, power, battery_type);
      tty_printf("    power = %d.%03d; adjustment_factor = %d.%03d \n", 
		 WATTS_INT(power), WATTS_DECIMAL(power),
		 ADJ_INT(adjustment_factor), ADJ_DECIMAL(adjustment_factor));
    }
  }
#endif
}


// Convert a time in seconds to hours, minutes, seconds
void bm_seconds_to_hms(unsigned int input_seconds, int * hour, int *minute, int *second) {

  *second = input_seconds % 60;
  
  *minute = (input_seconds / 60) % 60;

  *hour = (input_seconds / 3600) % 60; 
}


// Hijack the function that handles the battery menu
//   This so we can do something when user presses the "right" button 
//   e.g. store the current battery telemetry

void bm_handleBatteryTypeMenu(void)
{
  struct_CameraConfig *camera_config;
  enum_battery_type battery_type;
  int temp_int;
  int menu_offset;
  uint temp_uint;
  uint menu_selection;
  
  camera_config = getCameraConfigStructPtr();
  if (camera_config->exit_menu_p_or_ir_led_on != 0) {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    battery_type = get_g_cold_item_battery_type();
    camera_config->menu_selection_1 = (byte)battery_type;
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  temp_int = ui_cursor_key_pressed_p(up);
  if (((temp_int == 1) && (temp_uint = 0, g_up_button_enable == 2)) ||
     ((temp_int = ui_cursor_key_pressed_p(down), temp_int == 1 &&
      (temp_uint = 1, g_down_button_enable == 2)))) {
    menu_get_next_menu_selection(temp_uint,&camera_config->menu_selection_1,1,&g_menu_root);
    menu_redraw_items(camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  temp_int = ui_cursor_key_pressed_p(right);
  if ((temp_int ==1) && (g_right_button_enable == 2)) {
    bm_write_summary_file();
    return; 
  }

  temp_int = ui_cursor_key_pressed_p(left);
  if ((temp_int == 1) && (g_left_button_enable == '\x02')) {
    // NO-OP
    return;
  }

  temp_int = ui_cursor_key_pressed_p(enter);
  if ((temp_int == 1) && (g_enter_button_enable == 2)) {
    menu_selection = (uint)camera_config->menu_selection_1;
    camera_config->exit_menu_p_or_ir_led_on = 1;
    menu_offset = get_next_state_from_menu_enter(menu_selection, 
						 g_camera_setup_menu_item_array[menu_selection].menu_item_array,
						 g_camera_setup_menu_item_array[menu_selection].num_array_entries,
						 &g_menu_root);
    if (menu_offset == 0xff) {
      return;
    }
    // Replace previous call with hook that allows us to do our initialization
    bm_set_g_cold_item_battery_type(camera_config->menu_selection_1);
    setBatteryCalibConfig();
    camera_config->commit_menu_change = 1;
  }
  else {
    temp_int = ui_cursor_key_pressed_p(mode);
    if (temp_int != 1) {
      return;
    }
    if (g_mode_button_enable != 2) {
      return;
    }
    camera_config->exit_menu_p_or_ir_led_on = 1;
    camera_config->video_p = 0;
    menu_offset = get_next_state_from_menu_mode(1,&g_menu_root);
    temp_int = 0x1f;
    if (menu_offset == 0xff) goto LAB_8010ef94;
  }
  temp_int = menu_offset;
LAB_8010ef94:
  set_fsm_state_absolute(temp_int);
  return;
}





