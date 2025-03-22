//
// Include file for ir-flash-menu.c

// typedefs, constants, and function prototypes for IR-flash related
//     feature enhancement.  E.g.
//     2023-03-17: "Off" menu setting;  No IR LED

//
#if (defined BTC_7A_OLD)
struct_hp5_menu_item g_ifm_ir_led_power_menu[5];
#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) 
struct_hp5_menu_item g_ifm_ir_led_power_menu[4];
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
struct_hp5_menu_item g_ifm_ir_led_power_menu[5];
#endif

typedef enum enum_ir_led_power_menu_items {
  e_economy = 0,
  e_long_range,
  e_blur_reduction,
  e_off,
  e_invalid
} enum_ir_led_power_menu_items;

