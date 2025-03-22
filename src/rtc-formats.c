//
// rtc-formats.c
//
// Code to support multiple formats for date/time display on image test strip and review screen
//
//

#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "rtc-formats.h"

// Global Variables
// Menus
struct_hp5_menu_item g_rtc_date_format_menu[5] = {
  {no_icon, SST_MM_SLASH_DD_SLASH_YYYY,  0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_DD_SLASH_MM_SLASH_YYYY,  0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_YYYYMMDD,                0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_YYYY_SLASH_MM_SLASH_DD,  0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_DATE_SP_FORMAT,          0x00, 0x00, 0x01, 0x03, 0x03}
};

struct_hp5_menu_item g_rtc_time_format_menu[3] = {
  {no_icon, SST_12_DASH_HOUR,   0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_24_DASH_HOUR,   0x00, 0x01, 0x00, 0x1, 0x1},
  {no_icon, SST_TIME_SP_FORMAT, 0x00, 0x00, 0x01, 0x03, 0x03}
};

// 
byte rtc_get_cold_item_date_format() {
  return g_ColdItemData.date_format;

}

void rtc_set_cold_item_date_format(byte date_format) {
  g_ColdItemData.date_format = date_format;
}


byte rtc_get_cold_item_time_format() {
  return g_ColdItemData.time_format;;
}

void rtc_set_cold_item_time_format(byte time_format) {
  g_ColdItemData.time_format = time_format;
}


void rtc_handle_date_format_menu() {
  byte  date_format;
  struct_CameraConfig *camera_config;
  int iVar1;
  int iVar2;
  uint index;
  
  camera_config = getCameraConfigStructPtr();
  if (camera_config->exit_menu_p_or_ir_led_on != 0) {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    date_format = rtc_get_cold_item_date_format();
    camera_config->menu_selection_1 = date_format;
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(up);
  if (((iVar1 == 1) && (date_format = 0, g_up_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(down), iVar1 == 1 &&
      (date_format = 1, g_down_button_enable == 2)))) {
    menu_get_next_menu_selection(date_format,&camera_config->menu_selection_1,1,&g_menu_root);
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
    rtc_set_cold_item_date_format(camera_config->menu_selection_1);
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
    iVar1 = WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS + 5;
    if (iVar2 == 0xff) goto EXIT1;
  }
  iVar1 = iVar2;
EXIT1:
  set_fsm_state_absolute(iVar1);
  return;
}


void rtc_handle_time_format_menu() {
  byte  time_format;
  struct_CameraConfig *camera_config;
  int iVar1;
  int iVar2;
  uint index;
  
  camera_config = getCameraConfigStructPtr();
  if (camera_config->exit_menu_p_or_ir_led_on != 0) {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    time_format = rtc_get_cold_item_time_format();
    camera_config->menu_selection_1 = time_format;
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(up);
  if (((iVar1 == 1) && (time_format = 0, g_up_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(down), iVar1 == 1 &&
      (time_format = 1, g_down_button_enable == 2)))) {
    menu_get_next_menu_selection(time_format,&camera_config->menu_selection_1,1,&g_menu_root);
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
    rtc_set_cold_item_time_format(camera_config->menu_selection_1);
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
    iVar1 = WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS + 5;
    if (iVar2 == 0xff) goto EXIT2;
  }
  iVar1 = iVar2;
EXIT2:
  set_fsm_state_absolute(iVar1);
  return;
}

