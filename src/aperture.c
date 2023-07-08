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

// Global Variables

// Look table to map an aperture ind

#if (defined BTC_8E_HP5) || (defined BTC_7E_HP5) 
struct_night_mode_min_max g_apt_nightmode_threshold_lookup_table[3] = {
  {25, 40},   // Standard
  {12, 20 },  // Low Light
  { 0,  0 }   // No Light
};
#elif (defined BTC_8E_HP4) || (defined BTC_7E_HP4) 
struct_night_mode_min_max g_apt_nightmode_threshold_lookup_table[3] = {
  {90, 190},  // Standard
  {45, 95 },  // Low Light
  { 0,  0 }   // No Light
};
#elif (defined BTC_8E) || (defined BTC_7E) 
struct_night_mode_min_max g_apt_nightmode_threshold_lookup_table[3] = {
  {90, 190},  // Standard
  {45, 95 },  // Low Light
  { 0,  0 }   // No Light
};
#endif


// Returns the current value of aperture (daylight threshold)
//      Note that because we need this information quickly,
//      we can't wait for the ColdItem file to be read in
//      This means we need to store the 2-bit encoded state
//      in an area of NVRAM.  This is a little tricky, since
//      we have to find two bits that aren't already being used
//      
//      Note -- future factory firmware may wreck this
 
uint apt_get_cold_item_aperture() {
  byte result = apt_get_rtc_extra_short3_bits15_14();
  return(result);

}

void apt_set_cold_item_aperture(uint aperture) {
  apt_set_rtc_extra_short3_bits15_14(aperture);
}


// Setting bits 15:14 in the short 3 of the non-volatile
//     RAM associated with RTC
void apt_set_rtc_extra_short3_bits15_14(uint param_1)
{
  uint buffer [2];
  
  buffer[0] = buffer[0] & 0xffff0000;
  get_rtc_extra_byte_range((byte *)buffer,6,2);
  buffer[0] = buffer[0] & 0xffff3fff | (param_1 & 3) << 14;
  set_rtc_extra_byte_range((byte *)buffer,6,2);
  return;
}

// Getting bits 15:14 in the short 3 of the non-volatile
//     RAM associated with RTC
uint apt_get_rtc_extra_short3_bits15_14(void)
{
  uint buffer[2];
  
  buffer[0] = buffer[0] & 0xffff0000;
  get_rtc_extra_byte_range((byte *)buffer,6,2);
  return (buffer[0] << 16) >> 30;
}


// get_night_mode_threhold_mix_max

void apt_get_night_mode_theshold_min_max(uint *min, uint *max, uint aperture) {
  enum_aperture_encoding encoded_aperture = (enum_aperture_encoding) aperture;

  if (encoded_aperture >= invalid) {
    encoded_aperture = standard;
    aperture = (byte)encoded_aperture;
  }

  *min = g_apt_nightmode_threshold_lookup_table[aperture].min;
  *max = g_apt_nightmode_threshold_lookup_table[aperture].max;
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
  if (photo_sensor_value > 10000) {
    return(HceIQ_CheckNightMode());
  }

  g_photo_sensor_value = photo_sensor_value;
  log_printf(0,"PhotoSensor ADC = %d", photo_sensor_value);
#ifdef DEBUG1
  set_pre_printf_state();
  tty_printf("apt_HceIQ_CheckNightMode: PhotoSensor ADC = %d\n", 
	     g_photo_sensor_value);
  check_post_printf_state_set_sio_params();
#endif
  if (g_new_check_night_mode_p == 0) {
    hysteresis = (uint)g_night_mode_p;
  }
  else {
    hysteresis = photo_sensor_hysteresis();
    g_new_check_night_mode_p = 0;
  }
 
  encoded_aperture = (uint) apt_get_cold_item_aperture();
#ifdef DEBUG1
  set_pre_printf_state();
  tty_printf("apt_HceIQ_CheckNightMode: Encoded Aperture = %d\n", 
	     encoded_aperture);
  check_post_printf_state_set_sio_params();
#endif
  apt_get_night_mode_theshold_min_max(&min_threshold, &max_threshold, encoded_aperture);

#ifdef DEBUG1
  set_pre_printf_state();
  tty_printf("apt_HceIQ_CheckNightMode:  min = %d; max = %d\n", 
	     min_threshold, max_threshold);
  check_post_printf_state_set_sio_params();
#endif
 
  threshold = max_threshold;
  if (hysteresis == 0) {
    threshold = min_threshold;
  }
  g_night_mode_p = photo_sensor_value < threshold;
  g_photo_detector_hysteresis = (byte)hysteresis;
  tty_printf("aptHceIQ_CheckNightMode : Value = %d \n", photo_sensor_value);
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("aptCNMode:V %d;E %d;R %d\n", photo_sensor_value, encoded_aperture, (uint)g_night_mode_p);
  check_post_printf_state_set_sio_params();
#endif
  return (bool)g_night_mode_p;
}

