//
// dslr-trigger.c
// 
// Using trail camera to trigger a DSLR camera by activatiung "aim" 
//       LED after trigger, while photos/videos are taken

//       2025-02-24: Generalizing to "External Trigger": AimTest LED
//         turned on:
//           DLSR: on every trigger
//           Flash: on night triggers only

#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "aperture.h"
#include "dslr-trigger.h"

// DSLR Enable Menu

// Include debug print statements
//#define DEBUG
// force on for test without menu
//#define DEBUG_FORCE_ON  

//#define DEBUG_NO_LED
//#define DEBUG_ENABLE_RMW_MUTEX
//   #define DEBUG_WRITE_LED_RMW



struct_hp5_menu_item g_ext_trigger_enable_menu[4] = {
  { no_icon, SST_OFF,             0x00, 0x01, 0x00, 0x1, 0x1},
  { no_icon, SST_DSLR,            0x00, 0x01, 0x00, 0x1, 0x1},
  { no_icon, SST_FLASH,           0x00, 0x01, 0x00, 0x1, 0x1},
  { no_icon, SST_EXT_SP_TRIGGER, 0x00, 0x00, 0x01, 0x03, 0x03}
};


// When we turn the LED on and off, which requires a RMW, we're going to grab
//      the mutex for the entire RMW to keep from colliding with another write
//      (something which "works", but which produces CRC errors on the itnerface)
//   If this works, seems like not wrapping the RMW in a mutex is a bug in the factory code
void xtrg_Write_LEDOn() {
#ifdef DEBUG_ENABLE_RMW_MUTEX
  int return_value;
  byte read_data [4];
  byte write_data [4];
  byte address [4];
  
  address[0] = 0x11;
  address[1] = 0x12;
  address[2] = 14;
  write_data[0] = 0xff;
  write_data[1] = 0;
  write_data[2] = 0x88;

#ifdef DEBUG_WRITE_LED_RMW
  set_pre_printf_state();
  tty_printf("xtrg_Write_LEDOn -s \n");
  check_post_printf_state_set_sio_params();
#endif

  MCU_SPI_mutex_get(0xffffffff);    // We can wait forever...
  return_value = getMCURegisterByte(14,read_data);
  if (return_value != 0) {
    write_data[2] = read_data[0] & 0xf | 0x80;
  }
  MCU_Read_waiting_on_some_event(); // not sure what this does, but it's before every MCUSPI access.
  return_value = MPUSpi_WriteNPacketByManualPWM(address,write_data,3);
  thread_sleep(3,2);
  MCU_SPI_mutex_put();
#ifdef DEBUG_WRITE_LED_RMW
  set_pre_printf_state();
  tty_printf("xtrg_Write_LEDOn-e:_%d\n" ,return_value);
  check_post_printf_state_set_sio_params();
#endif
#else   // DEBUG_ENABLE_RMW_MUTEX
  Write_LEDOn();
#endif  // DEBUG_ENABLE_RMW_MUTEX
}

void xtrg_Write_LEDOff() {
#ifdef DEBUG_ENABLE_RMW_MUTEX
  int return_value;
  byte read_data [4];
  byte write_data [4];
  byte write_address [4];
  
  write_address[0] = 0x11;
  write_address[1] = 0x12;
  write_address[2] = 0xe;
  write_data[1] = 0xff;
  write_data[0] = 0;
  write_data[2] = 0x88;
  // Grab the mutex
#ifdef DEBUG_WRITE_LED_RMW
  set_pre_printf_state();
  tty_printf("xtrg_Write_LEDOff -s \n");
  check_post_printf_state_set_sio_params();
#endif

  MCU_SPI_mutex_get(0xffffffff);    // We can wait forever...
  // do the read
  return_value = getMCURegisterByte(14,read_data);
  if (return_value != 0) {
    write_data[2] = read_data[0] & 0xf | 0x80;
  }
  MCU_Read_waiting_on_some_event(); // not sure what this does, but it's after every mutex get
  return_value = MPUSpi_WriteNPacketByManualPWM(write_address,write_data,3);
  // Return the mutex
  thread_sleep(3,2);
  MCU_SPI_mutex_put();
#ifdef DEBUG_WRITE_LED_RMW
  set_pre_printf_state();
  tty_printf("xtrg_Write_LEDOff-e:_%d\n" ,return_value);
  check_post_printf_state_set_sio_params();
#endif
#else // DEBUG_ENABLE_RMW_MUTEX
  Write_LEDOff();
#endif
}

//
// For still photos (including various burst sizes) -- aim led is on in
//     HceTaskStill_task0


// Returns true if we should need to turn on/off the Aim-test LED 
//     in xtrg_flash mode. 
bool xtrg_flash_trigger_p() {
    enum_aperture_encoding encoded_aperture = apt_get_cold_item_aperture();
    uint default_low_light = g_apt_nightmode_threshold_lookup_table[0].min;

    // check to see whether we're in night mode
    //       this is a little tricky, since we clobber g_night_mode_p when the aperture
    //       is active
    return (g_night_mode_p || ((encoded_aperture == no_light) && (g_photo_sensor_value < default_low_light)));
  }


bool dt_cold_item_led_power_blur_reduction_p(void) {

  enum_ext_trigger ext_trigger = xtrg_get_cold_item_ext_trigger_enum();
  switch(ext_trigger) {
  case xtrg_dslr:
    xtrg_Write_LEDOn();
    break;
  case xtrg_flash:
    // check to see whether we're taking an image at night
    if (xtrg_flash_trigger_p()) {
      xtrg_Write_LEDOn();
    }
  case xtrg_off:
  default:
    break;
  }
  // Do what we are supposed to do in the original function
  return cold_item_led_power_blur_reduction_p();
}

// Hook for calling bm_on_video whenever a video is taken
// replace
// call to 
//    8001fe48 0d 4e 0d 0c     jal        log_printf
//
// 
//
void dt_video_log_printf_hook(unsigned int level, char * format_string, char * function_name) {
  enum_ext_trigger ext_trigger = xtrg_get_cold_item_ext_trigger_enum();
  // do the existing function
  log_printf(level, format_string, function_name);
  // turn on LED
  switch(ext_trigger) {
  case xtrg_dslr:
    xtrg_Write_LEDOn();
    break;
  case xtrg_flash:
    if (xtrg_flash_trigger_p()) {
      xtrg_Write_LEDOn();
    }
    break;
  case xtrg_off:
  default:
    break;
  }
}


// hook for turning *off* the AIM LED

void dt_IRLedOff(void) {
  enum_ext_trigger ext_trigger = xtrg_get_cold_item_ext_trigger_enum();
  // This is called instead of IRLedOff
  // First call the function we hooked
  IRLedOff();

  switch(ext_trigger) {
  case xtrg_dslr:
    xtrg_Write_LEDOff();
    break;
  case xtrg_flash:
    // check to see whether we're in night mode
    if (xtrg_flash_trigger_p()) {
      xtrg_Write_LEDOff();
    }
    break;
  case xtrg_off:
  default:
    break;
  }
}

//
enum_ext_trigger xtrg_get_cold_item_ext_trigger_enum() {
#ifdef DEBUG_FORCE_ON
  return(xtrg_dslr);
#else
  return (enum_ext_trigger)g_ColdItemData.external_trigger;
#endif
}

void xtrg_set_cold_item_ext_trigger_enum(enum_ext_trigger ext_trigger_enum) {
  g_ColdItemData.external_trigger = (byte) ext_trigger_enum;
}

// Function for handling DLSR LED Enable menu

void  xtrg_handle_led_enable_menu(void) {
  enum_ext_trigger  ext_trigger_enum;
  struct_CameraConfig *camera_config;
  int iVar1;
  int iVar2;
  uint index;
  
  camera_config = getCameraConfigStructPtr();
  if (camera_config->exit_menu_p_or_ir_led_on != 0) {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    ext_trigger_enum = xtrg_get_cold_item_ext_trigger_enum();
    camera_config->menu_selection_1 = (byte) ext_trigger_enum;
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  iVar1 = ui_cursor_key_pressed_p(up);
  if (((iVar1 == 1) && (ext_trigger_enum = xtrg_off, g_up_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(down), iVar1 == 1 &&
      (ext_trigger_enum = 1, g_down_button_enable == 2)))) {
    menu_get_next_menu_selection(ext_trigger_enum,&camera_config->menu_selection_1,1,&g_menu_root);
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
    xtrg_set_cold_item_ext_trigger_enum(camera_config->menu_selection_1);
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
