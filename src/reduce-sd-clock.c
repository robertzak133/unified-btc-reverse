//
// reduce-sd-clock.c
//  
// intercept the call to initialize the default SD card
//    if the speed mode is 100 MHz
//       reduce the speed to 50 MHz 
//      


#include "BTC.h"


int rsc_initialize_sd_card_to_data(uint device_number) {

  int return_value;

  return_value = initialize_sd_card_to_data(2);

  if (get_sd_clock_kHz() >= 100000) {
    reduce_SD_clock(&g_sd_card_descriptor);
  }
  return return_value;
}
