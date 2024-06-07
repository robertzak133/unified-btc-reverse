//
// menus.c
//    A place for the global structure which holds all the available menus
//

#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "extend-event-SD-card.h"
#include "rtc-formats.h"
#include "dslr-trigger.h"
#include "timelapse.h"
#include "aperture.h"
#include "ir-flash-menu.h"

//#define DEBUG

#if (defined BTC_7E) || (defined BTC_8E)
struct_hp5_menu_item g_wbwl_camera_setup_menu_item_array[WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 
							 WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS] = {
  { datetime,        SST_SETUP_SP_DATE_SLASH_TIME, 0x00, 0x01, 0x00, 0x02, 0x05 }, //0
  { opmode  ,        SST_OPERATION_SP_MODE,        0x00, 0x01, 0x00, 0x02, 0x06 }, //1
  { photo_quality,   SST_PHOTO_SP_QUALITY,         0x00, 0x01, 0x00, 0x02, 0x07 }, //2
  { video_length,    SST_VIDEO_SP_LENGTH,          0x00, 0x01, 0x00, 0x02, 0x08 }, //3
  { video_quality,   SST_VIDEO_SP_QUALITY,         0x00, 0x01, 0x00, 0x02, 0x09 }, //4
  { photo_delay,     SST_PHOTO_SP_DELAY,           0x00, 0x01, 0x00, 0x02, 0x0a }, //5
  { multishot,       SST_MULTI_SP_SHOT_SP_MODE,    0x00, 0x01, 0x00, 0x02, 0x0b }, //6
  { temp_unit,       SST_TEMP_SP_UNIT,             0x00, 0x01, 0x00, 0x02, 0x0c }, //7
  { camera_name,     SST_CAMERA_SP_NAME,           0x00, 0x01, 0x00, 0x02, 0x0d }, //8
  { stamp,           SST_IMAGE_SP_DATA_SP_STRIP,   0x00, 0x01, 0x00, 0x02, 0x0e }, //9
  { motion_test,     SST_MOTION_SP_TEST,           0x00, 0x01, 0x00, 0x02, 0x0f }, //10
  { pir_range,       SST_MOTION_SP_DETECTION,      0x00, 0x01, 0x00, 0x02, 0x10 }, //11
  { battery_type,    SST_BATTERY_SP_TYPE,          0x00, 0x01, 0x00, 0x02, 0x11 }, //12
  { trigger_speed,   SST_TRIGGER_SP_SPEED,         0x00, 0x01, 0x00, 0x02, 0x12 }, //13
  { restore_default, SST_DEFAULT_SP_SETTINGS,      0x00, 0x01, 0x00, 0x02, 0x13 }, //14
  { plot_frequency,  SST_TIMELAPSE_SP_FREQ,        0x00, 0x01, 0x00, 0x02, 0x14 }, //15
  { plot_period,     SST_TIMELAPSE_SP_PERIOD,      0x00, 0x01, 0x00, 0x02, 0x15 }, //16
  { delete_all,      SST_DELETE_SP_ALL,            0x00, 0x01, 0x00, 0x02, 0x16 }, //17
  { ir_flash_power,  SST_IR_SP_FLASH_SP_POWER,     0x00, 0x01, 0x00, 0x02, 0x17 }, //18
  { smart_ir,        SST_SMART_SP_IR_SP_VIDEO,     0x00, 0x01, 0x00, 0x02, 0x18 }, //19
  { sd_management,   SST_SD_SP_MANAGEMENT,         0x00, 0x01, 0x00, 0x02, 0x19 }, //20
  { set_language,    SST_LANGUAGE,                 0x00, 0x01, 0x00, 0x02, 0x1a }, //21
  { capture_timer,   SST_CAPTURE_SP_TIMER,         0x00, 0x01, 0x00, 0x02, 0x1b }, //22
  { firmware_upgrade,SST_FW_SP_UPGRADE,            0x00, 0x01, 0x00, 0x02, 0x1d }, //23
  // New Menus
  { sd_management,   SST_EXTENDED_SP_SD_SP_POWER,  0x00, 0x01, 0x00, 0x02, 0x1e }, //24 -- extended_sd_power
  { datetime,        SST_DATE_SP_FORMAT,           0x00, 0x01, 0x00, 0x02, 0x1f }, //25 -- date format
  { datetime,        SST_TIME_SP_FORMAT,           0x00, 0x01, 0x00, 0x02, 0x20 }, //26 -- time format
  { motion_test,     SST_DSLR_SP_TRIGGER,          0x00, 0x01, 0x00, 0x02, 0x21 }, //27 -- dslr_trigger
  { ir_flash_power,  SST_DAY_SP_THRESHOLD,         0x00, 0x01, 0x00, 0x02, 0x22 }, //28 -- aperture
  { plot_frequency,  SST_TIMELAPSE_SP_FILE,        0x00, 0x01, 0x00, 0x02, 0x23 }, //29 -- timelapse file type
  // Last entry is menu title
  { no_icon,         SST_CAMERA_SP_SETUP,          0x00, 0x00, 0x01, 0x03, 0x03 }  //30 -- Menu title "Camera Setup"
};

#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
struct_hp5_menu_item g_wbwl_camera_setup_menu_item_array[WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 
							 WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS] = {
  { datetime,        SST_SETUP_SP_DATE_SLASH_TIME, 0x00, 0x01, 0x00, 0x02, 0x05 }, //0
  { opmode  ,        SST_OPERATION_SP_MODE,        0x00, 0x01, 0x00, 0x02, 0x06 }, //1
  { photo_quality,   SST_PHOTO_SP_QUALITY,         0x00, 0x01, 0x00, 0x02, 0x07 }, //2
  { video_length,    SST_VIDEO_SP_LENGTH,          0x00, 0x01, 0x00, 0x02, 0x08 }, //3
  { video_quality,   SST_VIDEO_SP_QUALITY,         0x00, 0x01, 0x00, 0x02, 0x09 }, //4
  { photo_delay,     SST_PHOTO_SP_DELAY,           0x00, 0x01, 0x00, 0x02, 0x0a }, //5
  { multishot,       SST_MULTI_SP_SHOT_SP_MODE,    0x00, 0x01, 0x00, 0x02, 0x0b }, //6
  { temp_unit,       SST_TEMP_SP_UNIT,             0x00, 0x01, 0x00, 0x02, 0x0c }, //7
  { camera_name,     SST_CAMERA_SP_NAME,           0x00, 0x01, 0x00, 0x02, 0x0d }, //8
  { stamp,           SST_IMAGE_SP_DATA_SP_STRIP,   0x00, 0x01, 0x00, 0x02, 0x0e }, //9
  { motion_test,     SST_MOTION_SP_TEST,           0x00, 0x01, 0x00, 0x02, 0x0f }, //10
  { pir_range,       SST_MOTION_SP_DETECTION,      0x00, 0x01, 0x00, 0x02, 0x10 }, //11
  { battery_type,    SST_BATTERY_SP_TYPE,          0x00, 0x01, 0x00, 0x02, 0x11 }, //12
  { trigger_speed,   SST_TRIGGER_SP_SPEED,         0x00, 0x01, 0x00, 0x02, 0x12 }, //13
  { restore_default, SST_DEFAULT_SP_SETTINGS,      0x00, 0x01, 0x00, 0x02, 0x13 }, //14
  { plot_frequency,  SST_TIMELAPSE_SP_FREQ,        0x00, 0x01, 0x00, 0x02, 0x14 }, //15
  { plot_period,     SST_TIMELAPSE_SP_PERIOD,      0x00, 0x01, 0x00, 0x02, 0x15 }, //16
  { delete_all,      SST_DELETE_SP_ALL,            0x00, 0x01, 0x00, 0x02, 0x16 }, //17
  { ir_flash_power,  SST_IR_SP_FLASH_SP_POWER,     0x00, 0x01, 0x00, 0x02, 0x17 }, //18
  { smart_ir,        SST_SMART_SP_IR_SP_VIDEO,     0x00, 0x01, 0x00, 0x02, 0x18 }, //19
  { sd_management,   SST_SD_SP_MANAGEMENT,         0x00, 0x01, 0x00, 0x02, 0x19 }, //20
  { set_language,    SST_LANGUAGE,                 0x00, 0x01, 0x00, 0x02, 0x1a }, //21
  { capture_timer,   SST_CAPTURE_SP_TIMER,         0x00, 0x01, 0x00, 0x02, 0x1b }, //22
  { firmware_upgrade,SST_FW_SP_UPGRADE,            0x00, 0x01, 0x00, 0x02, 0x1d }, //23
  // New Menus
  { sd_management,   SST_EXTENDED_SP_SD_SP_POWER,  0x00, 0x01, 0x00, 0x02, 0x1e }, //24 -- extended_sd_power
  { datetime,        SST_DATE_SP_FORMAT,           0x00, 0x01, 0x00, 0x02, 0x1f }, //25 -- date format
  { datetime,        SST_TIME_SP_FORMAT,           0x00, 0x01, 0x00, 0x02, 0x20 }, //26 -- time format
  { motion_test,     SST_DSLR_SP_TRIGGER,          0x00, 0x01, 0x00, 0x02, 0x21 }, //27 -- dslr_trigger
  { ir_flash_power,  SST_DAY_SP_THRESHOLD,         0x00, 0x01, 0x00, 0x02, 0x22 }, //28 -- aperture
  { plot_frequency,  SST_TIMELAPSE_SP_FILE,        0x00, 0x01, 0x00, 0x02, 0x23 }, //29 -- timelapse file type
  // Last entry is menu title
  { no_icon,         SST_CAMERA_SP_SETUP,          0x00, 0x00, 0x01, 0x03, 0x03 }  //30 -- Menu title "Camera Setup"
};

#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
struct_hp5_menu_item g_wbwl_camera_setup_menu_item_array[WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 
							 WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS] = {
  { datetime,        SST_SETUP_SP_DATE_SLASH_TIME, 0x00, 0x01, 0x00, 0x02, 0x05 }, //0
  { opmode  ,        SST_OPERATION_SP_MODE,        0x00, 0x01, 0x00, 0x02, 0x06 }, //1
  { photo_quality,   SST_PHOTO_SP_QUALITY,         0x00, 0x01, 0x00, 0x02, 0x07 }, //2
  { video_length,    SST_VIDEO_SP_LENGTH,          0x00, 0x01, 0x00, 0x02, 0x08 }, //3
  { video_quality,   SST_VIDEO_SP_QUALITY,         0x00, 0x01, 0x00, 0x02, 0x09 }, //4
  { photo_delay,     SST_PHOTO_SP_DELAY,           0x00, 0x01, 0x00, 0x02, 0x0a }, //5
  { multishot,       SST_MULTI_SP_SHOT_SP_MODE,    0x00, 0x01, 0x00, 0x02, 0x0b }, //6
  { hdr,             SST_HDR,                      0x00, 0x01, 0x00, 0x02, 0x0c }, //7
  { temp_unit,       SST_TEMP_SP_UNIT,             0x00, 0x01, 0x00, 0x02, 0x0d }, //8
  { camera_name,     SST_CAMERA_SP_NAME,           0x00, 0x01, 0x00, 0x02, 0x0e }, //9
  { stamp,           SST_IMAGE_SP_DATA_SP_STRIP,   0x00, 0x01, 0x00, 0x02, 0x0f }, //10
  { motion_test,     SST_MOTION_SP_TEST,           0x00, 0x01, 0x00, 0x02, 0x10 }, //11
  { pir_range,       SST_MOTION_SP_DETECTION,      0x00, 0x01, 0x00, 0x02, 0x11 }, //12
  { battery_type,    SST_BATTERY_SP_TYPE,          0x00, 0x01, 0x00, 0x02, 0x12 }, //13
  { trigger_speed,   SST_TRIGGER_SP_SPEED,         0x00, 0x01, 0x00, 0x02, 0x13 }, //14
  { restore_default, SST_DEFAULT_SP_SETTINGS,      0x00, 0x01, 0x00, 0x02, 0x14 }, //15
  { plot_frequency,  SST_TIMELAPSE_SP_FREQ,        0x00, 0x01, 0x00, 0x02, 0x15 }, //16
  { plot_period,     SST_TIMELAPSE_SP_PERIOD,      0x00, 0x01, 0x00, 0x02, 0x16 }, //17
  { delete_all,      SST_DELETE_SP_ALL,            0x00, 0x01, 0x00, 0x02, 0x17 }, //18
  { ir_flash_power,  SST_IR_SP_FLASH_SP_POWER,     0x00, 0x01, 0x00, 0x02, 0x18 }, //19
  { smart_ir,        SST_SMART_SP_IR_SP_VIDEO,     0x00, 0x01, 0x00, 0x02, 0x19 }, //20
  { sd_management,   SST_SD_SP_MANAGEMENT,         0x00, 0x01, 0x00, 0x02, 0x1a }, //21
  { set_language,    SST_LANGUAGE,                 0x00, 0x01, 0x00, 0x02, 0x1b }, //22
  { capture_timer,   SST_CAPTURE_SP_TIMER,         0x00, 0x01, 0x00, 0x02, 0x1c }, //23
  { firmware_upgrade,SST_FW_SP_UPGRADE,            0x00, 0x01, 0x00, 0x02, 0x1e }, //24
  // New Menus
  { sd_management,   SST_EXTENDED_SP_SD_SP_POWER,  0x00, 0x01, 0x00, 0x02, 0x1f }, //25 -- extended_sd_power
  { datetime,        SST_DATE_SP_FORMAT,           0x00, 0x01, 0x00, 0x02, 0x20 }, //26 -- date format
  { datetime,        SST_TIME_SP_FORMAT,           0x00, 0x01, 0x00, 0x02, 0x21 }, //27 -- time format
  { motion_test,     SST_DSLR_SP_TRIGGER,          0x00, 0x01, 0x00, 0x02, 0x22 }, //28 -- dslr_trigger
  { ir_flash_power,  SST_DAY_SP_THRESHOLD,         0x00, 0x01, 0x00, 0x02, 0x23 }, //29 -- aperture
  { plot_frequency,  SST_TIMELAPSE_SP_FILE,        0x00, 0x01, 0x00, 0x02, 0x24 }, //30 -- timelapse file type
  // Last entry is menu title
  { no_icon,         SST_CAMERA_SP_SETUP,          0x00, 0x00, 0x01, 0x03, 0x03 }  //31 -- Menu title "Camera Setup"
};
#endif



#if (defined BTC_7E) || (defined BTC_8E)
struct_menu_selections_descriptor g_wbwl_camera_setup_selector_array[WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 
								     WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS] = 
  {
    { g_set_date_time_menu,          1 }, //0x00
    { g_operation_mode_menu,         4 }, //0x01
    { g_photo_quality_menu,          5 }, //0x02
    { g_video_length_menu,           7 }, //0x03
    { g_video_quality_menu,          3 }, //0x04
    { g_photo_delay_menu,           11 }, //0x05
    { g_multi_shot_mode_menu,       16 }, //0x06
    { g_temp_unit_menu,              3 }, //0x07
    { g_camera_name_menu,            1 }, //0x08
    { g_image_data_strip_menu,       3 }, //0x09
    { g_motion_test_menu,            3 }, //0x0a
    { g_pir_range_menu,              3 }, //0x0b
    { g_battery_type_menu,           3 }, //0x0c
    { g_trigger_speed_menu,          3 }, //0x0d
    { g_restore_default_menu,        3 }, //0x0e
    { g_wbwl_timelapse_frequency_menu,  13 }, //0x0f
    { g_wbwl_timelapse_period_menu,      7 }, //0x10
    { g_delete_all_menu,             3 }, //0x11
    { g_ifm_ir_led_power_menu,       4 }, //0x12
    { g_smart_ir_video_menu,         3 }, //0x13
    { g_sd_management_menu,          3 }, //0x14
    { g_language_menu,               8 }, //0x15
    { g_capture_timer_menu,          3 }, //0x16
    { g_firmware_upgrade_menu,       4 }, //0x17
    // WBWL-Specfic menus
    { g_evsd_extended_sd_power_menu, 3 }, //0x18
    { g_rtc_date_format_menu,        4 }, //0x19
    { g_rtc_time_format_menu,        3 }, //0x1a
    { g_dlsr_led_enable_menu,        3 }, //0x1b
    { g_apt_aperture_menu,           4 }, //0x1c
    { g_tlps_file_type_menu,         3 }, //0x1d
    // Null Terminator
    { 0,                             0 }  //0x1e
  };
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4) 
struct_menu_selections_descriptor g_wbwl_camera_setup_selector_array[WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 
									    WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS] = 
  {
    { g_set_date_time_menu,          1 }, //0x00
    { g_operation_mode_menu,         4 }, //0x01
    { g_photo_quality_menu,          5 }, //0x02
    { g_video_length_menu,           7 }, //0x03
    { g_video_quality_menu,          3 }, //0x04
    { g_photo_delay_menu,           11 }, //0x05
    { g_multi_shot_mode_menu,       16 }, //0x06
    { g_temp_unit_menu,              3 }, //0x07
    { g_camera_name_menu,            1 }, //0x08
    { g_image_data_strip_menu,       3 }, //0x09
    { g_motion_test_menu,            3 }, //0x0a
    { g_pir_range_menu,              3 }, //0x0b
    { g_battery_type_menu,           4 }, //0x0c
    { g_trigger_speed_menu,          3 }, //0x0d
    { g_restore_default_menu,        3 }, //0x0e
    { g_wbwl_timelapse_frequency_menu,   13 }, //0x0f
    { g_wbwl_timelapse_period_menu,       7 }, //0x10
    { g_delete_all_menu,             3 }, //0x11
    { g_ifm_ir_led_power_menu,       5 }, //0x12
    { g_smart_ir_video_menu,         3 }, //0x13
    { g_sd_management_menu,          3 }, //0x14
    { g_language_menu,               8 }, //0x15
    { g_capture_timer_menu,          3 }, //0x16
    { g_firmware_upgrade_menu,       4 }, //0x17
    // WBWL-Specfic menus
    { g_evsd_extended_sd_power_menu, 3 }, //0x18
    { g_rtc_date_format_menu,        4 }, //0x19
    { g_rtc_time_format_menu,        3 }, //0x1a
    { g_dlsr_led_enable_menu,        3 }, //0x1b
    { g_apt_aperture_menu,           4 }, //0x1c
    { g_tlps_file_type_menu,         3 }, //0x1d
    // Null Terminator
    { 0,                             0 }  //0x1e
  };

#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
struct_menu_selections_descriptor g_wbwl_camera_setup_selector_array[WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 
									    WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS] = 
  {
    { g_set_date_time_menu,          1 }, //0x00
    { g_operation_mode_menu,         4 }, //0x01
    { g_photo_quality_menu,          5 }, //0x02
    { g_video_length_menu,           7 }, //0x03
    { g_video_quality_menu,          3 }, //0x04
    { g_photo_delay_menu,           11 }, //0x05
    { g_multi_shot_mode_menu,       16 }, //0x06
    { g_hdr_menu,                    3 }, //0x07
    { g_temp_unit_menu,              3 }, //0x08
    { g_camera_name_menu,            1 }, //0x09
    { g_image_data_strip_menu,       3 }, //0x0a
    { g_motion_test_menu,            3 }, //0x0b
    { g_pir_range_menu,              3 }, //0x0c
    { g_battery_type_menu,           4 }, //0x0d
    { g_trigger_speed_menu,          3 }, //0x0e
    { g_restore_default_menu,        3 }, //0x0f
    { g_wbwl_timelapse_frequency_menu,   13 }, //0x10
    { g_wbwl_timelapse_period_menu,       7 }, //0x11
    { g_delete_all_menu,             3 }, //0x12
    { g_ifm_ir_led_power_menu,       5 }, //0x13
    { g_smart_ir_video_menu,         3 }, //0x14
    { g_sd_management_menu,          3 }, //0x15
    { g_language_menu,               8 }, //0x16
    { g_capture_timer_menu,          3 }, //0x17
    { g_firmware_upgrade_menu,       4 }, //0x1c
    // WBWL-Specfic menus
    { g_evsd_extended_sd_power_menu, 3 }, //0x18
    { g_rtc_date_format_menu,        4 }, //0x19
    { g_rtc_time_format_menu,        3 }, //0x1a
    { g_dlsr_led_enable_menu,        3 }, //0x1b
    { g_apt_aperture_menu,           4 }, //0x1c
    { g_tlps_file_type_menu,         3 }, //0x1d
   // Null Terminator
    { 0,                             0 }  //0x1e
  };
#endif

void *g_wbwl_menu_handler_function_array_extensions[WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS+1] = {
  evsd_handle_extended_sd_power_menu,
  rtc_handle_date_format_menu,
  rtc_handle_time_format_menu,
  dslr_handle_led_enable_menu,
  apt_handle_aperture_menu,
  tlps_handle_file_type_menu, 
  menus_handleCommitUpdates_menu
};


void menus_handleCommitUpdates_menu() {
  handleCommitUpdates_menu();
}


// menus_execute_if_not_null()
//    this is the way we execute a menu handler function from our new array
//    vs. the factory standard array
//    Note that I had to hack in a change in argument for this function so
//    that it calls my new function with an index (not the function pointer,
//    itself)

bool menus_execute_if_not_null(unsigned int index) {
  void (*new_menu_function)();
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("m: i %d\n", index);
  check_post_printf_state_set_sio_params();
#endif

  if (index < WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 5) {
    new_menu_function = g_HceTaskMenuMultiItem_fsm_function_array[index];
  } else {
    index -= (WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 5);
    new_menu_function = g_wbwl_menu_handler_function_array_extensions[index];
  }

  return(execute_if_not_null(new_menu_function));
}



// Replaces call in handleCameraSetupMenu
// Line 34
// substitutes in new array arguments

unsigned int wbwl_get_next_state_from_menu_enter(unsigned int index,
						 struct_hp5_menu_item *menu_item_array,
						 uint num_array_entries,
						 struct_menu_root **menu_root) {
  unsigned int return_value; 

  return_value = get_next_state_from_menu_enter(index,
						g_wbwl_camera_setup_selector_array[index].menu_item_array,
						g_wbwl_camera_setup_selector_array[index].num_array_entries,
						menu_root);
  return return_value;
}
