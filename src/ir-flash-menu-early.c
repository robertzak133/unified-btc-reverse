// Time critical (i.e. early in boot process) code for 
//      disable IR LED
// 

#include "BTC.h"
#include "menus.h"
#include "ir-flash-menu.h"

//#define DEBUG


// Once the factory code has done gymnastics figuring out how to
//      set the LED intensity; we're just going to disable it
//      if the menu setting is "off"

void ifm_power_on_IR_LED(void) {
  enum_cold_item_ir_led_intensity cold_led_power;
  enum_cold_item_ir_led_intensity warm_led_power;

  cold_led_power = get_g_cold_item_led_power();

#ifdef DEBUG
  log_printf(3,"ifm c =%d\n", (uint)cold_led_power, );
  set_pre_printf_state();
  tty_printf("ifm c =%d\n", (uint)cold_led_power);
  check_post_printf_state_set_sio_params();
#endif

  if (cold_led_power == off) {
#ifdef DEBUG1
    log_printf(3,"ifm:LEDoff\n");
    set_pre_printf_state();
    tty_printf("ifm:LEDoff\n");
    check_post_printf_state_set_sio_params();
#endif
  } else {
#ifdef DEBUG1
    log_printf(3,"ifm:LEDon\n");
#endif
    power_on_IR_LED();
  } 
}

