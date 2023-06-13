//
// fix-ir-led-settings.c
//    In the BTC HP5, there are three IR settings in the menu (L, M, H)
//    but they only seem to result in two IR LED setting (L, L, H)
//    this file attempts to fix this

#include "BTC.h"
#include "fix-ir-led-settings.h"


// for now, let's just undertand what's working and what ain't
// intercept call to set_led_power and print out what's being set
// 
void fils_set_cold_item_led_power(uint setting) {

#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("fils_set_cold_item_led_power: %d\n", setting);
  check_post_printf_state_set_sio_params();
#endif
  set_cold_item_led_power(setting);
}


// This function translates from one representation of 
//  IR LED intesnity to another.  I think the original gets it wrong
// (at least I don't understand how the code could work).  Replace
//  it with your very basic switch statement

void fils_set_ir_led_intensity_from_cold_item(enum_cold_item_ir_led_intensity ir_led_intensity) {
  int which_case = 0;

  switch(ir_led_intensity) {
  case economy: 
    g_ir_led_power_alt_encoding = low_25_pct;
    which_case = 0;
    break;
  case long_range: 
    g_ir_led_power_alt_encoding = med_50_pct;
    which_case = 1;
    break;
  case blur_reduction:
    g_ir_led_power_alt_encoding = high_80_pct;
    which_case = 2;
    break;
  default:
    g_ir_led_power_alt_encoding = med_50_pct;
    which_case = 3;
    // this is an error case -- but due to limitation in my current tools, I need
    // to put this (never used in runtime) call in the code to add this symbol
    // to my lookup table.  A hack.  I know. 
    set_ir_led_intensity_from_cold_item(ir_led_intensity);
    break;
  }

#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("fils_set_ir_led_intensity_from_cold_item: in %d; out: %d; case: %d\n", 
	     ir_led_intensity, g_ir_led_power_alt_encoding, which_case);
  check_post_printf_state_set_sio_params();
#endif

  fils_set_ir_led_power_pwm(g_ir_led_power_alt_encoding);

}



void fils_set_ir_led_power_pwm(enum_alt_ir_led_intensity alt_ir_led_intensity) {
  // just hard wire

  enum_alt_ir_led_intensity forced_ir_led_intensity = high_80_pct;
#ifdef DEBUG
  set_pre_printf_state();
//  tty_printf("fils_set_ir_power_pwm: in %d; out %d\n", alt_ir_led_intensity, forced_ir_led_intensity);
  tty_printf("fils_set_ir_power_pwm: setting to %d; \n", alt_ir_led_intensity);
  check_post_printf_state_set_sio_params();
#endif
  
  set_ir_led_power_pwm(alt_ir_led_intensity);
}



void fils_smart_IR_log_printf(char * format_string, uint arg1) {
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf(format_string, arg1);
  tty_printf("\n");
  check_post_printf_state_set_sio_params();
#endif
  
  smart_IR_log_printf(format_string, arg1);
}



void fils_smart_IR_log_sub_printf(char * format_string, uint arg1) {
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("-->");
  tty_printf(format_string, arg1);
  tty_printf("\n");
  check_post_printf_state_set_sio_params();
#endif
  
  smart_IR_log_sub_printf(format_string, arg1);
}


void fils_debug_print_screen(uint level, char *string) {
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf(string);
  check_post_printf_state_set_sio_params();
#endif
  debug_print_string(level, string);
}
