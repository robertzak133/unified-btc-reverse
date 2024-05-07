//
// reduce-sd-clock.c
//  
// intercept the call to initialize the default SD card
//    if the speed mode is 100 MHz
//       reduce the speed to 50 MHz 
//      


#include "BTC.h"

//#define DEBUG

int rsc_initialize_sd_card_to_data(uint device_number) {

  int return_value;
  int sd_clock_kHz;
  int *error_ptr = 0;

#ifdef BTC_7E_HP5
#ifdef DEBUG
  uint time = get_current_operating_time_ms();
  set_pre_printf_state();
  tty_printf("DEBUG: rsc_initialize_sd_card_to_data -- about to init sd card at %d ms\n", time);
  check_post_printf_state_set_sio_params();
#endif
#endif

  return_value = initialize_sd_card_to_data(2);

#ifdef BTC_7E_HP5
#ifdef DEBUG
  time = get_current_operating_time_ms();
  sd_clock_kHz = get_sd_clock_kHz(); 
  set_pre_printf_state();
  tty_printf("DEBUG: rsc_initialize_sd_card_to_data -- sd_clk_kHz = %d at %d ms\n", sd_clock_kHz, time);
  check_post_printf_state_set_sio_params();
#endif
#endif
  reduce_SD_clock(&g_sd_card_descriptor);

#ifdef BTC_7E_HP5  
#ifdef DEBUG
  sd_clock_kHz = get_sd_clock_kHz(); 
  time = get_current_operating_time_ms();
  set_pre_printf_state();
  tty_printf("DEBUG: rsc_initialize_sd_card_to_data -- sd_clk_kHz = %d at %d ms\n", sd_clock_kHz, time);
  check_post_printf_state_set_sio_params();
#endif
#endif
  //return_value = *error_ptr;

  return return_value;
}



void rsc_log_printf(uint debug_level, char* format_string, int sd_clock, int sd_bus_width, int sd_mtype) {
#ifdef DEBUG
  uint time = get_current_operating_time_ms();
  set_pre_printf_state();
  tty_printf("DEBUG: rsc_set_sd_iface_clock -- sd_clk = %d, sd_bus_width = %d, sd_mtype = %d at %d ms\n", sd_clock, sd_bus_width, sd_mtype, time);
  check_post_printf_state_set_sio_params();
#endif
}

