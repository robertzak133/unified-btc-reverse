//
// fix-ir-led-settings.c
//    In the BTC HP5, there are three IR settings in the menu (L, M, H)
//    but they only seem to result in two IR LED setting (L, L, H)
//    this file attempts to fix this

#define DEBUG

void fils_set_cold_item_led_power(uint setting);

void fils_set_ir_led_intensity_from_cold_item(enum_cold_item_ir_led_intensity ir_led_intensity);

void fils_set_ir_led_power_pwm(enum_alt_ir_led_intensity alt_ir_led_intensity);

void fils_smart_IR_log_printf(char * format_string, uint arg1);

void fils_smart_IR_log_sub_printf(char * format_string, uint arg1);

void fils_debug_print_screen(uint level, char *string);
