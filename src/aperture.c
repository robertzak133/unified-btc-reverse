//
// aperture.c
//
// Code to support different aperture lenses by changing the threshold at which
//      day and night mode is detected.  Larger aperture means lower theshold 
//      (and more opportunity for color shots)
//      2023-07-07: terminology changed to "Daylight threshold", which allows
//      easy inclusione "no light" (awkwardly an infinite aperture)
//
//

#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "aperture.h"

//#define DEBUG
//#define DEBUG1
//#define DEBUG2
//#define DEBUG_FLASH
//#define DEBUG_7A

// Global Variables

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
  struct_night_mode_min_max g_apt_nightmode_threshold_lookup_table[3] = {
    {90, 190},  // Standard
    {45, 95 },  // Low Light
    {90, 190 }   // No Light -- switch over to (white) flash sooner rather than later
  };
#elif (defined BTC_8E_HP5) || (defined BTC_7E_HP5) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
// The HP4 & HP5 have a more light sensitive sensor?
  struct_night_mode_min_max g_apt_nightmode_threshold_lookup_table[3] = {
    {25, 40},   // Standard
    {12, 20 },  // Low Light
    {25, 40 }   // No Light -- switch over to (white) flash sooner rather than later
  };
#endif
// Look table to map an aperture ind

// Returns the current value of aperture (daylight threshold)
//      In subsequent cameras, this data is shadows in NVRAM, which has much less space
//      Note that because we need this information quickly,
//      we can't wait for the ColdItem file to be read in
//      This means we need to store the 2-bit encoded state
//      in an area of NVRAM.  This is a little tricky, since
//      we have to find two bits that aren't already being used
//      
//      Note -- future factory firmware may wreck this hack
//      by actually using the bits I've borrowed


enum_aperture_encoding apt_get_rtc_extra_aperture() {
  uint buffer[4];
  get_rtc_extra_byte_range((byte *)buffer,6,2);
  return (buffer[0] << 16) >> 30;
}


// Hook that allows us to keep the non-volatile 
// Intercept call that writes operation to NVM on power down
//     to also write out aperture encoding from cold.bin

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
// Need to carve out bit field for aperture setting
byte apt_get_rtc_extra_operation_mode(void) {
  byte buffer [16];
  
  get_rtc_extra_byte_range(buffer,7,1);
  return buffer[0] & 0x3f;
}
#endif

// Set operation mode nvm, and then set aperture in nvm
//     this is only called at power_off, so could be pushed into later modules
void apt_set_rtc_extra_operation_mode(byte operation_mode) {
#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
  // for targets above, we have to tuck the operation_mode into a smaller field
  ushort buffer [8]; // 8 shorts
  
  get_rtc_extra_byte_range((byte *)buffer,6,2);
  if ((buffer[0] && 0xff) > 1000) {
    // never executed -- just here to get the function into the symbol library
    set_rtc_extra_operation_mode(operation_mode);
  }
  buffer[0] = buffer[0] & 0xc0ff | (operation_mode & 0x3f) << 8;
  set_rtc_extra_byte_range((byte *)buffer,6,2);
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
  // For the HP5, we can just call the factory function
  set_rtc_extra_operation_mode(operation_mode);
#else
    **** ERROR: Unrecognized Target ****
#endif

  // Move the cold_item version of aperture into NVM
  enum_aperture_encoding aperture_encoding = apt_get_cold_item_aperture();
  apt_set_rtc_extra_aperture(aperture_encoding);
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("apt_set_rtc_extra_operation_mode: operation_mode = %d; aperature = %d\n", 
	     operation_mode, (int) aperture_encoding);
  check_post_printf_state_set_sio_params();
#endif
}




// get_night_mode_threhold_mix_max

void apt_get_night_mode_threshold_min_max(uint *min, uint *max, 
					 enum_aperture_encoding encoded_aperture) {

// this check does not fit in the avaialble code space :(
/*  if ((encoded_aperture >= invalid) || (encoded_aperture < standard)) { */
/*     encoded_aperture = standard; */
/*   } */

  *min = (int)g_apt_nightmode_threshold_lookup_table[(uint) encoded_aperture].min;
  *max = (int)g_apt_nightmode_threshold_lookup_table[(uint) encoded_aperture].max;
  return;
}


bool apt_HceIQ_CheckNightMode(void) {

  uint photo_sensor_value;
  uint hysteresis;
  uint threshold;
  uint min_threshold;
  uint max_threshold;
  uint encoded_aperture;
  
  photo_sensor_value = read_photo_sensor_value();

  // dummy call to get this in to the symbol table
  //       HceIQ_CheckNightMode should never be called
  if (photo_sensor_value > 1000) {
    return(HceIQ_CheckNightMode());
  }

  g_photo_sensor_value = photo_sensor_value;
#ifdef DEBUG1
  log_printf(0,"PhotoSensor ADC = %d", photo_sensor_value);
  set_pre_printf_state();
  tty_printf("apt_HceIQ_CheckNightMode: PhotoSensor ADC = %d\n", 
	     g_photo_sensor_value);
  check_post_printf_state_set_sio_params();
#endif // DEBUG1
  if (g_new_check_night_mode_p == 0) {
    hysteresis = (uint)g_night_mode_p;
  }
  else {
    hysteresis = photo_sensor_hysteresis();
    g_new_check_night_mode_p = 0;
  }
 
  encoded_aperture = (uint) apt_get_rtc_extra_aperture();
#ifdef DEBUG1
  set_pre_printf_state();
  tty_printf("apt_HceIQ_CheckNightMode: Encoded Aperture = %d\n", 
	     encoded_aperture);
  check_post_printf_state_set_sio_params();
#endif  // DEBUG1
  apt_get_night_mode_threshold_min_max(&min_threshold, &max_threshold, encoded_aperture);

#ifdef DEBUG1
  set_pre_printf_state();
  tty_printf("apt_HceIQ_CheckNightMode:  min = %d; max = %d\n", 
	     min_threshold, max_threshold);
  check_post_printf_state_set_sio_params();
#endif // DEBUG1
 
  threshold = max_threshold;
  if (hysteresis == 0) {
    threshold = min_threshold;
  }
  g_night_mode_p = photo_sensor_value < threshold;
  g_photo_detector_hysteresis = (byte)hysteresis;
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("apt%d,%d\n", photo_sensor_value, g_night_mode_p);
  check_post_printf_state_set_sio_params();
#endif // DEBUG
  return (bool)g_night_mode_p;
}





#ifdef DEBUG_FLASH
// Debug Patch -- is this where we're setting the IR Cut

void apt_IRCutThreadCreate(uint value){

  IRCutThreadCreate(value);
#ifdef DEBUG2
  set_pre_printf_state();
  tty_printf("apt_IRCutThreadCreate:Value = %d \n", value);
  check_post_printf_state_set_sio_params();
#endif

}

// Debug Patch -- are we getting the right value for night mode?

uint apt_get_g_night_mode_p (void) {
  uint return_value;
  return_value = get_g_night_mode_p();
#ifdef DEBUG2
  set_pre_printf_state();
  tty_printf("apt_get_g_night_mode_p : Return Value = %d \n", return_value);
  check_post_printf_state_set_sio_params();
#endif
  return return_value;
}

// Debug Patch
void apt_ir_cut_log_printf(uint level, char* format_string, char * title, uint value) {
  log_printf(level, format_string, title, value);
#ifdef DEBUG2
  set_pre_printf_state();
  tty_printf("apt_ir_cut_log_printf 0x%08x, vaulue = %d \n",  (uint) title, value);
  check_post_printf_state_set_sio_params();
#endif
}


// Debug Patch
uint apt_boot2cap_fsm_getCurrentState() {
  uint return_value = fsm_getCurrentState();
#ifdef DEBUG2
  set_pre_printf_state();
  tty_printf("apt_boot2cap_fsm_getCurrentState: %d \n",  return_value);
  check_post_printf_state_set_sio_params();
#endif
  return return_value;
}

#endif
