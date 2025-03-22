// ir-flash-menu.c
// 
//    Code to manage the IR flash menu
//         adds a new feature in which there is a "no flash" setting
// 



#include "BTC.h"
#include "menus.h"
#include "ir-flash-menu.h"

char g_SST_OFF_string[sizeof("OFF")];

// Global Variables
// Menus

#if (defined BTC_7A_OLD) 
struct_hp5_menu_item g_ifm_ir_led_power_menu[5] = {
  {no_icon, g_SST_ECONOMY_string,              0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, g_SST_LONG_SP_RANGE_string,        0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, g_SST_BLUR_SP_REDUCTION_string,    0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, g_SST_OFF_string,                  0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, g_SST_IR_SP_FLASH_SP_POWER_string, 0x00, 0x00, 0x01, 0x03, 0x03}
};
#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) 
struct_hp5_menu_item g_ifm_ir_led_power_menu[4] = {
  {no_icon, SST_ECONOMY,           0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_LONG_SP_RANGE0,    0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_OFF,               0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_IR_SP_FLASH_SP_POWER, 0x00, 0x00, 0x01, 0x03, 0x03}
};
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
struct_hp5_menu_item g_ifm_ir_led_power_menu[5] = {
  {no_icon, SST_ECONOMY,           0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_LONG_SP_RANGE0,     0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_BLUR_SP_REDUCTION, 0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_OFF,               0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_IR_SP_FLASH_SP_POWER, 0x00, 0x00, 0x01, 0x03, 0x03}
};
#endif










