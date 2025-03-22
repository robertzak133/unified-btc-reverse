// 
// White Flash and Large Type for Date on Review for BTC-7A
// 2025-02-26 Zak: Created

// Enable white flash 

// We want the flash to come on when the camera is in "no light" mode
//    and the FLASH_POWER isn't set to "Off".  
//    This involves intercepting the functions where the flash would have
//    been turned on, and doing it. 

#include "BTC.h"
#include "aperture.h"
#include "timelapse.h"
#include "white-flash.h"



//#define DEBUG

// Intercept call to setSensorDigitalEffect{Photo,Video} to check whether we want
//     a color photo/video at night

void wfl_setSensorDigitalEffectPhoto(byte night_p) {
  enum_aperture_encoding encoded_aperture = (enum_aperture_encoding) apt_get_cold_item_aperture();
  // if it's at night, an we're only taking color photos,
  //    then flip night_p so that we take a color photo instead of B&W
  if ((encoded_aperture ==  no_light) && (night_p != 0)) {
    night_p = 0;
  } 
  setSensorDigitalEffectPhoto(night_p);
}

void wfl_setSensorDigitalEffectVideo(byte night_p) {
  enum_aperture_encoding encoded_aperture = (enum_aperture_encoding) apt_get_cold_item_aperture();
  // if it's at night, an we're only taking color photos,
  //    then flip night_p so that we take a color photo instead of B&W
  if ((encoded_aperture ==  no_light) && (night_p != 0)) {
    night_p = 0;
  } 
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("wfl_setSensorDigitalEffectVideo: night_p = %d; encoded_aperture = %d\n",
	     night_p, encoded_aperture);
  check_post_printf_state_set_sio_params();  
#endif
  setSensorDigitalEffectVideo(night_p);
}

// Intercept calls to HceIRCut_SetIRCutOpen()
//    (what is normally used for night time photos)
//    and if we're only taking color photos, don't open the filter
void wfl_HceIRCut_SetIRCutOpen() {
  enum_aperture_encoding encoded_aperture = (enum_aperture_encoding) apt_get_cold_item_aperture();
  // if it's at night, an we're only taking color photos,
  //    then flip night_p so that we take a color photo instead of B&W
  if (encoded_aperture !=  no_light) {
    HceIRCut_SetIRCutOpen();
  }
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("wfl_HceIRCut_SetIRCutOpen: encoded_aperture = %d;\n",
	     encoded_aperture);
  check_post_printf_state_set_sio_params();  
#endif
}



void wfl_video_log_printf(uint level, char* format_string, char* first_arg) {
  log_printf(level, format_string, first_arg);
#ifdef DEBUG
  struct_CameraConfig *camera_config = getCameraConfigStructPtr();
  set_pre_printf_state();
  tty_printf("wfl_video_log_printf: ir_led_on = %d ;\n",
	     camera_config->exit_menu_p_or_ir_led_on);
  check_post_printf_state_set_sio_params();  
#endif
}


// Here's where we figure out how to set the IRCut Filter.  
//    This now depends on:
//    - operating modes {Trail Camera, Video, Timelapse+}
//    - g_night_mode_p {0, 1}
//    - timelapse tod_in_timelapse_region {daylight_post_sunrise_region, 
//                                         daylight_no_photo_region,
//                                         daylight_pre_sunset_region,
//                                         night_no_photo_region}
//    - Daylight Threshold {standard, low light, no light}

void wfl_spawnIRCutFSM_per_mode() {
  uint ir_cut_value = 0;

  enum_aperture_encoding encoded_aperture = (enum_aperture_encoding) apt_get_cold_item_aperture();
  enum_operation_mode operation_mode = (enum_operation_mode) get_cold_item_operation_mode(); 
  enum_timelapse_period_encoding timelapse_period = tlps_get_cold_item_raw_timelapse_period();

  if ((g_night_mode_p == 1) && (encoded_aperture != no_light) &&
      ((operation_mode == trail_camera) || 
       (operation_mode == video) || 
       ((operation_mode == timelapse) && (timelapse_period == all_day_night)))) {
    ir_cut_value = 1;
  } else {
    ir_cut_value = 0;
  }
  
  IRCutThreadCreate(ir_cut_value);
}

