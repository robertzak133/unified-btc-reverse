//
// extend-event-SD-card.c
// Per request from James McConnel
// Keep the SD card powered on for some time after the photo/video has been taken
// 
// The easy way to do this is to just put a "thread-sleep" at the tail end of the 
//     photo or video FSM
//     This will have desired (undesired?) effect of preventing a retrigger 
//     Let's start here
// 2022-11-27: Make this a user-selectable option in the "SD Mangement" menu
//     Shows up as "Extended Power"




#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "extend-event-SD-card.h"

// 2024-10-07 Zak: Removed  -- this is not strictly an automatic process,
//                 as it needs to be from other places, as well.  
// #define EVSD_ACTIVE
//    

#ifdef EVSD_ACTIVE
//#define DEBUG

// Global Constants
struct_hp5_menu_item g_evsd_extended_sd_power_menu[3] = {
  { no_icon, SST_OFF,                     0x00, 0x01, 0x00, 0x1, 0x1 },
  { no_icon, SST_ON ,                     0x00, 0x01, 0x00, 0x1, 0x1 },
  { no_icon, SST_EXTENDED_SP_SD_SP_POWER, 0x00, 0x00, 0x01, 0x03, 0x03}
};


// Video Entry Point and Still Entry Point
// Turns out they both call the same function

void evsd_check_remaining_sd_capacity(void) {

foo my BAR
#ifdef DEBUG
    set_pre_printf_state();
    tty_printf("evsd_check_remaining_sd_capacity - s\n");
    check_post_printf_state_set_sio_params();
#endif

  check_remaining_sd_capacity();

  // If extended_sd_power is enabled, just go to sleep
  if (evsd_get_cold_item_extended_sd_power_p() == 1) {
#ifdef DEBUG
    unsigned int start_time; 
    start_time = get_current_operating_time_ms();
    set_pre_printf_state();
    tty_printf("evsd_delay -- start of wait\n");
    check_post_printf_state_set_sio_params();
#endif
    thread_sleep(times_1000, EVSD_SD_CARD_DELAY);
    // And when we're awake, we'll return to shutting down the camera

#ifdef DEBUG
    unsigned int end_time;
    end_time = get_current_operating_time_ms();
    set_pre_printf_state();
    tty_printf("evsd_delay -- end of wait after %d\n", end_time - start_time);
    check_post_printf_state_set_sio_params();
#endif
  }

#ifdef DEBUG
    set_pre_printf_state();
    tty_printf("evsd_check_remaining_sd_capacity - e\n");
    check_post_printf_state_set_sio_params();
#endif

}

// We need to steal some bits out of the cold.bin file
//    Since sd_management_p only needs one bit, we'll take it from there 
void evsd_set_cold_item_sd_management_p(byte sd_management_p) {
  set_cold_item_sd_management_p((g_ColdItemData.sd_management_p & 0xfe) | (sd_management_p & 1));
}

byte evsd_get_cold_item_sd_management_p() {
  byte sd_management_p = get_cold_item_sd_management_p();
  return (sd_management_p & 0x1);
}


void evsd_set_cold_item_extended_sd_power_p(byte extended_sd_power_p) {
  byte temp_byte = g_ColdItemData.sd_management_p;
  temp_byte = SET_BYTE_N_BIT(temp_byte, extended_sd_power_p, 
			     WBWL_EXTENDED_SD_POWER_N_BITS,
			     WBWL_EXTENDED_SD_POWER_LSBIT);

  set_cold_item_sd_management_p(temp_byte);

}


byte evsd_get_cold_item_extended_sd_power_p() {
  byte result = g_ColdItemData.sd_management_p;
  result = GET_BYTE_N_BIT(result,
			  WBWL_EXTENDED_SD_POWER_N_BITS,
			  WBWL_EXTENDED_SD_POWER_LSBIT);
  return(result);
}


void evsd_handle_extended_sd_power_menu() {
  byte  extended_sd_power_p;
  struct_CameraConfig *camera_config;
  int iVar1;
  int iVar2;
  uint index;
  
  camera_config = getCameraConfigStructPtr();
  if (camera_config->exit_menu_p_or_ir_led_on != 0) {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    extended_sd_power_p = evsd_get_cold_item_extended_sd_power_p();
    camera_config->menu_selection_1 = extended_sd_power_p;
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(up);
  if (((iVar1 == 1) && (extended_sd_power_p = 0, g_up_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(down), iVar1 == 1 &&
      (extended_sd_power_p = 1, g_down_button_enable == 2)))) {
    menu_get_next_menu_selection(extended_sd_power_p,&camera_config->menu_selection_1,1,&g_menu_root);
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
					   g_wbwl_camera_setup_selector_array[index].num_array_entries,&g_menu_root);
    if (iVar2 == 0xff) {
      return;
    }
    evsd_set_cold_item_extended_sd_power_p(camera_config->menu_selection_1);
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
    if (iVar2 == 0xff) goto EXIT;
  }
  iVar1 = iVar2;
EXIT:
  set_fsm_state_absolute(iVar1);
  return;
}


#endif
