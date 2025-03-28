// The menu handling code for aperture (now "Day Threshold")
//     see aperture.c for the control code itself

#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "aperture.h"

//#define DEBUG

// Global Variables
// Menus

struct_hp5_menu_item g_apt_aperture_menu[4] = {
  {no_icon, SST_STANDARD,                0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_LOW_SP_LIGHT,            0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_ALWAYS_SP_COLOR,         0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_DAY_SP_THRESHOLD,        0x00, 0x00, 0x01, 0x03, 0x03}
};


enum_aperture_encoding apt_get_cold_item_aperture() {
  return (enum_aperture_encoding) g_ColdItemData.aperture;
}

void apt_set_cold_item_aperture(enum_aperture_encoding aperture) {
  g_ColdItemData.aperture = (byte) aperture;
}

void apt_set_rtc_extra_aperture(enum_aperture_encoding aperture) {
  uint buffer [4];
  get_rtc_extra_byte_range((byte *)buffer,6,2);
  buffer[0] = buffer[0] & 0xffff3fff | (aperture & 3) << 14;
  set_rtc_extra_byte_range((byte *)buffer,6,2);
}


void apt_handle_aperture_menu() {
  byte  encoded_aperture;
  struct_CameraConfig *camera_config;
  int iVar1;
  int iVar2;
  uint index;
  
  camera_config = getCameraConfigStructPtr();
  if (camera_config->exit_menu_p_or_ir_led_on != 0) {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    encoded_aperture = apt_get_cold_item_aperture();
    camera_config->menu_selection_1 = encoded_aperture;
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(up);
  if (((iVar1 == 1) && (encoded_aperture = 0, g_up_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(down), iVar1 == 1 &&
      (encoded_aperture = 1, g_down_button_enable == 2)))) {
    menu_get_next_menu_selection(encoded_aperture,&camera_config->menu_selection_1,1,&g_menu_root);
    menu_redraw_items(camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(left);
  if (((iVar1 == 1) && (g_left_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(right), iVar1 == 1 && (g_right_button_enable == 2)))) {
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(enter);
  if ((iVar1 == 1) && (g_enter_button_enable == 2)) {
    index = (uint)camera_config->menu_selection_1;
    camera_config->exit_menu_p_or_ir_led_on = 1;
    iVar2 = get_next_state_from_menu_enter(index,
					   g_wbwl_camera_setup_selector_array[index].menu_item_array,
					   g_wbwl_camera_setup_selector_array[index].num_array_entries,
					   &g_menu_root);
    if (iVar2 == 0xff) {
      return;
    }
    apt_set_cold_item_aperture(camera_config->menu_selection_1);
    camera_config->commit_menu_change = 1;
  }
  else {
    iVar1 = ui_cursor_key_pressed_p(mode);
    if (iVar1 != 1) {
      return;
    }
    if (g_mode_button_enable != 2) {
      return;
    }
    camera_config->exit_menu_p_or_ir_led_on = 1;
    iVar2 = get_next_state_from_menu_mode(1,&g_menu_root);
    iVar1 = WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS +1;
    if (iVar2 == 0xff) goto EXIT1;
  }
  iVar1 = iVar2;
EXIT1:
  set_fsm_state_absolute(iVar1);
  return;
}

// Never called, but here to get some local functions in the lookup table
void apt_dummy(void) {
  byte result;
#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
  result = get_rtc_extra_operation_mode();
  set_rtc_extra_operation_mode(result);
#endif
}
