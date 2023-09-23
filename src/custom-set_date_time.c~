//
// custom-set-date-time.c
//
// A new version of the date/time menu that allows time to be set using 24-hour clock (vs. AM/PM)
//       as controlled by the "Time Format" menu selection
// 
//       This code is a little hairy because of the original :(
//    2023-09-14
//       This version, which envisioned changing both the date format and the time format
//       on the menu screen is now "old" 
//       New version just does the time.  (12 hour vs. 24 hour)
//       Which is a lot easier, and addresses the primary ask, I believe. 


#include "BTC.h"
#include "WBWL.h"
#include "rtc-formats.h"
#include "custom-set-date-time.h"

#define DEBUG
// 
// Menu Item Order
// 
//                    Date
// Field    MM-DD-YYYY    DD-MM-YYYY    YYYYMMDD
// 0        MM            DD            YYYY
// 1                   -- NA --
// 2        DD            MM            MM
// 3                   -- NA -- 
// 4        YYYY          YYYY          DD
//                    Time
//          12-Hour       24-Hour
// 5        HH < 13       HH < 24
// 6                   -- NA --
// 7        MM < 60       MM < 60
// 8                   -- NA --
// 9        AM/PM         NA



void cdt_get_set_date_time_functions (enum_date_time_menu_item selector, 
				      enum_rtc_date_format_options date_format,
				      enum_rtc_time_format_options time_format,
				      struct_menu_functions *menu_functions
				      ) {
  switch(selector) {
  case dtm_nominal_month:
    switch (date_format) {
    case rtc_mm_dd_yyyy:
      menu_functions->current_value_function = get_g_menu_temp_month;
      menu_functions->min_value_function = get_min_month;
      menu_functions->max_value_function = get_max_month;
      break;
    case rtc_dd_mm_yyyy:
      menu_functions->current_value_function = get_g_temp_day_number;
      menu_functions->min_value_function = get_min_day;
      menu_functions->max_value_function = get_max_day;
      break;
    case rtc_yyyymmdd:
    default:
      menu_functions->current_value_function = get_g_menu_temp_year ;
      menu_functions->min_value_function = get_min_year;
      menu_functions->max_value_function = get_max_year;
      break;
    }
    break;
  case dtm_nominal_day:
    switch (date_format) {
      case rtc_dd_mm_yyyy:
      case rtc_yyyymmdd:
	menu_functions->current_value_function = get_g_menu_temp_month;
	menu_functions->min_value_function = get_min_month;
	menu_functions->max_value_function = get_max_month;
	break;
      case rtc_mm_dd_yyyy:
	menu_functions->current_value_function = get_g_temp_day_number;
	menu_functions->min_value_function = get_min_day;
	menu_functions->max_value_function = get_max_day;
	break;
    }
    break;
  case dtm_nominal_year:
    switch (date_format) {
    case rtc_mm_dd_yyyy:
    case rtc_dd_mm_yyyy:
      menu_functions->current_value_function = get_g_menu_temp_year ;
      menu_functions->min_value_function = get_min_year;
      menu_functions->max_value_function = get_max_year;
      break;
    case rtc_yyyymmdd:
    default:    
      menu_functions->current_value_function = get_g_temp_day_number;
      menu_functions->min_value_function = get_min_day;
      menu_functions->max_value_function = get_max_day;
      break;
    }
    break;
  case dtm_nominal_hour:
    menu_functions->current_value_function = get_g_menu_temp_hour;   
    if (time_format == rtc_twelve_hour) {
      menu_functions->min_value_function = get_min_month;
      menu_functions->max_value_function = get_max_month;
    } else {
      menu_functions->min_value_function = cdt_get_min_hour;
      menu_functions->max_value_function = cdt_get_max_hour;
    } 
    break;
  case dtm_nominal_minute:
    menu_functions->current_value_function = get_g_menu_temp_minute;   
    menu_functions->min_value_function = get_min_minute;
    menu_functions->max_value_function = get_max_minute;
    break;
  case dtm_nominal_am_pm:
    if (time_format == rtc_twelve_hour) {
      menu_functions->current_value_function = get_am_pm_current_value;
      menu_functions->min_value_function = get_am_pm_min_value;
      menu_functions->max_value_function = get_am_pm_max_value;
    }
    break;
  default:
    menu_functions->current_value_function = 0;
    menu_functions->min_value_function = 0;
    menu_functions->max_value_function = 0;
  }
}

// 
// 
uint cdt_get_max_hour(void) {
  return 23;
}
uint cdt_get_min_hour(void) {
  return 0;
}

// Handling the menu

// In handleSetTimeMenu() 
//    Line 134
//    put this function in the place of
//         menu_draw_selected_item(selected_item, menu_root);
//         
void cdt_menu_draw_selected_item(byte *selected_item,struct_menu_root **menu_root) {
  enum_rtc_time_format_options time_format = (enum_rtc_time_format_options) rtc_get_cold_item_time_format();

  // check to see whether we're in 24 hour mode:
  if(time_format == rtc_twenty_four_hour) {
    // If so, we have some cleaning up to do
    //    the internal format is already 24 hours, so we just need to keep it that way
    get_current_date_time_short(&g_set_date_time_menu_state);
  }
  // Now just draw it as we usually would
  menu_draw_selected_item(selected_item, menu_root);
}


// This function get's called to handle the button actions on the 
//      set date/time menu.  The original is a bit of a mess.
//      we need to pretty much rewrite it so that we can give the
//      right format for date and time, per date and time format
//      menu settings

void cdt_handleSetTimeMenu(void) {
  // Handle the keyboard
  int button_pressed_p;
  struct_CameraConfig *camera_config;

  camera_config = getCameraConfigStructPtr();

  // Dummy call to force inclusion of symbol
  //     handleSetTimeMenu() should never be called
  if (camera_config == (struct_CameraConfig *) 0) {
    handleSetTimeMenu();
  }

#ifdef DEBUG_VERBOSE
  set_pre_printf_state();
  tty_printf("cdt_handleSetTimeMenu -s\n");
  check_post_printf_state_set_sio_params();
#endif

  if (camera_config->exit_menu_p_or_ir_led_on == 0) {
    // We are in menu mode; check the buttons
    button_pressed_p = cdt_check_keyboard(camera_config);
  } else {
    // We are leaving menu mode; store the temporary values
    //    for RTC
    camera_config->exit_menu_p_or_ir_led_on = 0;
    camera_config->menu_selection_1 = 0;
    get_current_date_time_short(&g_set_date_time_menu_state);
    g_temp_am_pm_p = (ushort)g_set_date_time_menu_state.hour < 12 ^ 1;
    if (g_set_date_time_menu_state.hour == 0) {
      g_set_date_time_menu_state.hour = 12;
    }
    else if (12 < (ushort)g_set_date_time_menu_state.hour) {
      g_set_date_time_menu_state.hour = g_set_date_time_menu_state.hour + -0xc;
    }
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
  } 

  // Now Display the menu
#ifdef DEBUG_VERBOSE
  set_pre_printf_state();
  tty_printf("cdt_handleSetTimeMenu : drawing screen \n");
  check_post_printf_state_set_sio_params();
#endif
  // draw_set_time_screen(camera_config->menu_selection_1);
  cdt_draw_set_time_screen(camera_config->menu_selection_1);
  // Just return if neither up nor down button are pressed
  int key_pressed_p = ui_cursor_key_pressed_p(up);
  if (((key_pressed_p != 1) || (g_up_button_enable != 1)) &&
     ((key_pressed_p = ui_cursor_key_pressed_p(down), key_pressed_p != 1 || (g_down_button_enable != 1)))) {
    int next_state = fsm_getNextState();
    int current_state = fsm_getCurrentState();
    if (next_state == current_state) {
#ifdef DEBUG_VERBOSE
      set_pre_printf_state();
      tty_printf("cdt_handleSetTimeMenu -e: fsm\n");
      check_post_printf_state_set_sio_params();
#endif
      return;
    }
  }

  // 
  camera_config->menu_selection_2 = 0;
#ifdef DEBUG_VERBOSE
  set_pre_printf_state();
  tty_printf("cdt_handleSetTimeMenu -e: eof\n");
  check_post_printf_state_set_sio_params();
#endif

  return;
}

// Check the Keyboard in the Set Date-Time Menu
//       
int cdt_check_keyboard(struct_CameraConfig *camera_config) {
  // Check Up/Down Buttons
  int buttons_pressed_p = 0;
  int up_button_p = ui_cursor_key_pressed_p(up);
  int down_button_p = ui_cursor_key_pressed_p(down);

  if (((up_button_p == 1) &&((byte)(g_up_button_enable - 2) < 2)) ||
      ((down_button_p == 1) &&((byte)(g_down_button_enable - 2) < 2))) {
#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("cdt_check_keyboard: up_button_p = %d; down_button_p = %d \n",
	     up_button_p, down_button_p);
  check_post_printf_state_set_sio_params();
#endif
    cdt_handle_up_down_buttons(camera_config, up_button_p);
    buttons_pressed_p = 1;
  } else {
    // Check for Left/Right Button
    int left_button_p = ui_cursor_key_pressed_p(left);
    int right_button_p = ui_cursor_key_pressed_p(right);

    if (((left_button_p == 1) &&((byte)(g_left_button_enable - 2) < 2)) ||
	((right_button_p == 1) &&((byte)(g_right_button_enable - 2) < 2))) {
#ifdef DEBUG
      set_pre_printf_state();
      tty_printf("cdt_check_keyboard: left_button_p = %d; right_button_p = %d \n",
		 left_button_p, right_button_p);
  check_post_printf_state_set_sio_params();
#endif
      cdt_handle_left_right_buttons(camera_config, left_button_p);
      buttons_pressed_p = 1;
    } else {
      // Check for Enter/Mode Button
      int enter_button_p = ui_cursor_key_pressed_p(enter);
      int mode_button_p = ui_cursor_key_pressed_p(mode);

      if (((enter_button_p == 1) &&((byte)(g_enter_button_enable - 2) < 2)) ||
	  ((mode_button_p == 1) &&((byte)(g_mode_button_enable - 2) < 2))) {
	cdt_handle_enter_mode_buttons(camera_config, enter_button_p);
#ifdef DEBUG
	set_pre_printf_state();
	tty_printf("cdt_check_keyboard: enter_button_p = %d; mode_button_p = %d \n",
		   enter_button_p, mode_button_p);
	check_post_printf_state_set_sio_params();
#endif

	buttons_pressed_p = 1;
      } else {
	int buttons_pressed_p = 0;
      }
    }
  }
  return buttons_pressed_p;
}

  
// The up/down buttons change the temporary value of the date or time
//     There is a generic function which 
void cdt_handle_up_down_buttons(struct_CameraConfig *camera_config,
			        int up_button_p) {
  struct_menu_functions date_time_menu_functions;
  enum_date_time_menu_item selector;
  short *current_field_value;
  short field_value;

  enum_rtc_time_format_options time_format = (enum_rtc_time_format_options) rtc_get_cold_item_time_format();
  enum_rtc_date_format_options date_format = (enum_rtc_date_format_options) rtc_get_cold_item_date_format();

  uint next_item = 3;

  if (camera_config->menu_selection_2 < 3) {
    camera_config->menu_selection_2 = camera_config->menu_selection_2 + 1;
    next_item = 1;
  }

  selector = (enum_date_time_menu_item)camera_config->menu_selection_1;
  current_field_value = cdt_get_date_time_current_field_value(selector, date_format, time_format);

  cdt_get_set_date_time_functions (selector, 
				   date_format, time_format,
				   &date_time_menu_functions);

  *current_field_value = HceTask_ToNextNChar(up_button_p,
					     date_time_menu_functions.current_value_function,
					     date_time_menu_functions.min_value_function,
					     date_time_menu_functions.max_value_function, 
					     next_item);
}

void cdt_handle_left_right_buttons(struct_CameraConfig *camera_config, int left_button_p) {
  byte right_p;
  uint menu_days_in_month, days_in_month; 

  // New month may have fewer days than max
  menu_days_in_month = get_g_temp_day_number();
  days_in_month     =  get_max_day();
  if (days_in_month < menu_days_in_month) {
    g_set_date_time_menu_state.day = (short)days_in_month;
  }
  
  if (left_button_p == 1) {
    right_p = 0;
  } else {
    right_p = 1;
  }
  update_time_field(right_p,&camera_config->menu_selection_1,1,g_set_time_buffer,10);

}



// Convert an hour in 12-hour + AM/PM to 24 hour format
//     12A        0        1
//      1A        1        1
//      :
//     11A        11       1
//     12P        12       0
//      1PM       13       0
//      :
//     11PM       23       0
short cdt_twelve_to_twenty_four(uint am_pm_p, short hour) {
  short return_hour;
  if (am_pm_p == 1) {
    if (hour != 12) {
      return_hour = hour + 12;
    }
  } else {
    if (hour == 12) {
      return_hour = 0;
    } else {
      return_hour = hour;
    }
  }
  return return_hour;
		  
}

// Handle the Mode and Enter buttons
//        When storing the current time, we may need to adjust the hours
//        so that thye reflect the canonical internal 24 hour format
// 
void cdt_handle_enter_mode_buttons(struct_CameraConfig *camera_config, 
				   int enter_button_p) {

  uint temp_days_in_month, days_in_month;

  enum_rtc_time_format_options time_format;
  // We're leaving the setup menu one way or antoher
  camera_config->exit_menu_p_or_ir_led_on = 1;

  if (enter_button_p) {
    // Enter Button
    temp_days_in_month = get_g_temp_day_number();
    days_in_month = get_max_day();
    if (days_in_month < temp_days_in_month) {
      g_set_date_time_menu_state.day = (short)days_in_month;
    }
    time_format = (enum_rtc_time_format_options) rtc_get_cold_item_time_format();
    if (time_format == rtc_twelve_hour) {
      g_set_date_time_menu_state.hour = cdt_twelve_to_twenty_four(g_temp_am_pm_p, g_set_date_time_menu_state.hour);
    }
    g_set_date_time_menu_state.second = 0;
    hal_set_rtc(&g_set_date_time_menu_state);
    uint capture_timer_p  = get_cold_item_capture_timer_p();
    if (capture_timer_p != 0) {
      struct_short_RTCTime short_rtc_time;
      get_capture_timer_rtc_time(&short_rtc_time);
      struct_short_RTC_as_uints *rtc_as_uints = (struct_short_RTC_as_uints *)&short_rtc_time;
      reset_capture_timer(rtc_as_uints->year_month,
			  rtc_as_uints->day_hour);
    }
#if (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
    set_cold_item_rtc_device_set_p(1);
    set_cold_item_137_1(0);
#endif
    camera_config->commit_menu_change = 1;
  } else {
    // Mode button
  }

  int exit_state = get_next_state_from_menu_mode(1,(struct_menu_root **)&g_menu_root);
  if (exit_state == 0xff) {
    exit_state = 0x1f;
  }
  set_fsm_state_absolute(exit_state);
}


// Drawing the menu on the screen
//     We need to draw things differently depending on the date and time format
void cdt_draw_set_time_screen(uint selected_item) {
  enum_rtc_time_format_options time_format = (enum_rtc_time_format_options) rtc_get_cold_item_time_format();
  enum_rtc_date_format_options date_format = (enum_rtc_date_format_options) rtc_get_cold_item_date_format();
  
  // Draw Date in top row

  // Scale appropriately

  // Draw Rectangle Wrappers


  // Draw Time in bottom row


  // Scale appropriately

  // Draw Rectangle Wrappers

  // Draw Contents
}

short *cdt_get_date_time_current_field_value(enum_date_time_menu_item selector, 
					    enum_rtc_date_format_options date_format, 
					    enum_rtc_time_format_options time_format) {

  if (selector <= dtm_nominal_year) {
    switch (date_format) {
    case   rtc_mm_dd_yyyy:
    default: 
      switch(selector) {
      case dtm_nominal_month:
	return &g_set_date_time_menu_state.month;
	break;
      case dtm_nominal_day:
	return &g_set_date_time_menu_state.day;
	break;
      case dtm_nominal_year:
      default:
	return &g_set_date_time_menu_state.year;
	break;
      }
      break;
    case   rtc_dd_mm_yyyy:
      switch(selector) {
      case dtm_nominal_month:
	return &g_set_date_time_menu_state.day;
	break;
      case dtm_nominal_day:
	return &g_set_date_time_menu_state.month;
	break;
      case dtm_nominal_year:
      default:
	return &g_set_date_time_menu_state.year;
	break;
      }
      break;
    case   rtc_yyyymmdd:
      switch(selector) {
      case dtm_nominal_month:
	return &g_set_date_time_menu_state.year;
	break;
      case dtm_nominal_day:
	return &g_set_date_time_menu_state.month;
	break;
      case dtm_nominal_year:    
      default:
	return &g_set_date_time_menu_state.day;
	break;
      }
      break;
    } 
  } else {
    switch(selector) {
    case dtm_nominal_hour: // Hour
      return &g_set_date_time_menu_state.hour;   
      break;
    case dtm_nominal_minute: // Minute
      return &g_set_date_time_menu_state.minute;   
      break;
    case dtm_nominal_am_pm: // AM/PM
    default:
      return &g_temp_am_pm_p;   
      break;
    }
  } 
  // We should never get here
  return &g_set_date_time_menu_state.hour;   
}


#ifdef CDT_FACTORY_FUNCTIONS


void cdt_handleSetTimeMenu(void)

{
  short sVar1;
  struct_CameraConfig *camera_config;
  uint uVar2;
  int iVar3;
  int iVar4;
  uint selected_time_date_field;
  byte bVar5;
  undefined4 uVar6;
  undefined4 up_button_p;
  undefined *current_value_function;
  undefined *min_value_function;
  undefined *max_value_function;
  short *current_field_value;
  undefined4 local_18;
  undefined4 local_14;
  
  camera_config = getCameraConfigStructPtr();
  if (camera_config->exit_menu_p_or_ir_led_on == 0) {
    iVar3 = ui_cursor_key_pressed_p(up);
    if ((iVar3 == 1) && ((byte)(g_up_button_enable - 2) < 2)) {
      uVar6 = 3;
      if (camera_config->menu_selection_2 < 3) {
        camera_config->menu_selection_2 = camera_config->menu_selection_2 + 1;
        uVar6 = 1;
      }
      selected_time_date_field = (uint)camera_config->menu_selection_1;
      if (selected_time_date_field < 10) {
        current_field_value = g_current_time_menu_value_lookup_table[selected_time_date_field];
      }
      else {
        current_field_value = &g_enu_temp_short_RTC_time.day;
      }
      up_button_p = 1;
      current_value_function =
           g_set_time_functions_array[selected_time_date_field].get_current_value;
      min_value_function = g_set_time_functions_array[selected_time_date_field].get_min_value;
      max_value_function = g_set_time_functions_array[selected_time_date_field].get_max_value;
    }
    else {
      iVar3 = ui_cursor_key_pressed_p(down);
      if ((iVar3 != 1) || (1 < (byte)(g_down_button_enable - 2))) {
        iVar3 = ui_cursor_key_pressed_p(left);
        if ((iVar3 == 1) && (g_left_button_enable == 2)) {
          selected_time_date_field = get_g_temp_day_number();
          uVar2 = get_num_days_in_new_month();
          if (uVar2 < selected_time_date_field) {
            g_menu_temp_short_RTC_time.day = (short)uVar2;
          }
          bVar5 = 0;
        }
        else {
          iVar3 = ui_cursor_key_pressed_p(right);
          if ((iVar3 != 1) || (g_right_button_enable != 2)) {
            iVar3 = ui_cursor_key_pressed_p(enter);
            if ((iVar3 == 1) && (g_enter_button_enable == 2)) {
              camera_config->exit_menu_p_or_ir_led_on = 1;
              selected_time_date_field = get_g_temp_day_number();
              uVar2 = get_num_days_in_new_month();
              if (uVar2 < selected_time_date_field) {
                g_menu_temp_short_RTC_time.day = (short)uVar2;
              }
              if (g_temp_am_pm_p == 1) {
                sVar1 = g_menu_temp_short_RTC_time.hour + 12;
                if ((ushort)g_menu_temp_short_RTC_time.hour < 12) {
LAB_80111484:
                  g_menu_temp_short_RTC_time.hour = sVar1;
                }
              }
              else if ((g_temp_am_pm_p == 0) &&
                      (sVar1 = g_menu_temp_short_RTC_time.hour + -0xc,
                      11 < (ushort)g_menu_temp_short_RTC_time.hour)) goto LAB_80111484;
              g_menu_temp_short_RTC_time.second = 0;
              hal_set_rtc(&g_menu_temp_short_RTC_time);
              iVar3 = get_cold_item_capture_timer_p();
              if (iVar3 != 0) {
                FUN_800e6a0c(&local_18);
                FUN_800e4e04(local_18,local_14);
              }
              set_cold_item_rtc_device_set_p(1);
              FUN_800e5d1c(0);
              camera_config->commit_menu_change = 1;
            }
            else {
              iVar3 = ui_cursor_key_pressed_p(mode);
              if ((iVar3 != 1) || (g_mode_button_enable != 2)) goto LAB_8011151c;
              camera_config->exit_menu_p_or_ir_led_on = 1;
            }
            iVar3 = get_next_state_from_menu_mode(1,(struct_menu_root **)&g_menu_root);
            if (iVar3 == 0xff) {
              iVar3 = 0x1f;
            }
            set_fsm_state_absolute(iVar3);
            goto LAB_8011151c;
          }
          selected_time_date_field = get_g_temp_day_number();
          uVar2 = get_num_days_in_new_month();
          if (uVar2 < selected_time_date_field) {
            g_menu_temp_short_RTC_time.day = (short)uVar2;
          }
          bVar5 = 1;
        }
        update_time_field(bVar5,&camera_config->menu_selection_1,1,&DAT_8030fb68,10);
        goto LAB_801113ec;
      }
      uVar6 = 3;
      if (camera_config->menu_selection_2 < 3) {
        camera_config->menu_selection_2 = camera_config->menu_selection_2 + 1;
        uVar6 = 1;
      }
      selected_time_date_field = (uint)camera_config->menu_selection_1;
      if (selected_time_date_field < 10) {
        current_field_value = g_current_time_menu_value_lookup_table[selected_time_date_field];
      }
      else {
        current_field_value = &g_menu_temp_short_RTC_time.day;
      }
      up_button_p = 0;
      current_value_function =
           g_set_time_functions_array[selected_time_date_field].get_current_value;
      min_value_function = g_set_time_functions_array[selected_time_date_field].get_min_value;
      max_value_function = g_set_time_functions_array[selected_time_date_field].get_max_value;
    }
    sVar1 = HceTask_ToNextNChar(up_button_p,current_value_function,min_value_function,
                                max_value_function,uVar6);
    *current_field_value = sVar1;
  }
  else {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    camera_config->menu_selection_1 = 0;
    get_current_date_time_short(&g_menu_temp_short_RTC_time);
    g_temp_am_pm_p = (ushort)g_menu_temp_short_RTC_time.hour < 12 ^ 1;
    if (g_menu_temp_short_RTC_time.hour == 0) {
      g_menu_temp_short_RTC_time.hour = 12;
    }
    else if (12 < (ushort)g_menu_temp_short_RTC_time.hour) {
      g_menu_temp_short_RTC_time.hour = g_menu_temp_short_RTC_time.hour + -0xc;
    }
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
  }
LAB_801113ec:
  draw_set_time_screen(camera_config->menu_selection_1);
LAB_8011151c:
  iVar3 = ui_cursor_key_pressed_p(up);
  if (((iVar3 != 1) || (g_up_button_enable != 1)) &&
     ((iVar3 = ui_cursor_key_pressed_p(down), iVar3 != 1 || (g_down_button_enable != 1)))) {
    iVar3 = fsm_getNextState();
    iVar4 = fsm_getCurrentState();
    if (iVar3 == iVar4) {
      return;
    }
  }
  camera_config->menu_selection_2 = 0;
  return;
}
#endif


#ifdef CDT_FACTORY_FUNCTIONS
// Argh -- I'm going to need to change this too, to work with 
//         different time formats.  
//      -- existing code here as a placeholder while I figure
//         out how this function is supposed to work. 
void cdt_handleSetCaptureTimerParams_menu(void) {
  short sVar1;
  char cVar2;
  undefined2 uVar3;
  struct_CameraConfig *camera_config;
  uint uVar4;
  int iVar5;
  int iVar6;
  uint uVar7;
  byte right_p;
  undefined4 uVar8;
  undefined4 uVar9;
  undefined *puVar10;
  undefined *puVar11;
  undefined *puVar12;
  undefined2 *puVar13;
  
  camera_config = getCameraConfigStructPtr();
  cVar2 = DAT_803183f8;
  if (camera_config->exit_menu_p_or_ir_led_on == 0) {
    if (camera_config->field10_0xa != 0) {
      if (camera_config->menu_selection_2 == 0) {
        iVar5 = event_match_0x5051000_qualifier(3);
        if (iVar5 != 0) {
          camera_config->menu_selection_2 = camera_config->menu_selection_2 + 1;
        }
      }
      else {
        camera_config->exit_menu_p_or_ir_led_on = 1;
        camera_config->menu_selection_2 = 0;
        camera_config->field10_0xa = 0;
        DAT_803183f8 = '\x01';
        draw_rectangle_wrapper(0,0,0x140,0xf0,1);
      }
      goto LAB_80111110;
    }
    iVar5 = ui_cursor_key_pressed_p(up);
    if ((iVar5 == 1) && ((byte)(g_up_button_enable - 2) < 2)) {
      uVar8 = 3;
      if (camera_config->menu_selection_2 < 3) {
        camera_config->menu_selection_2 = camera_config->menu_selection_2 + 1;
        uVar8 = 1;
      }
      uVar4 = (uint)camera_config->menu_selection_1;
      puVar13 = &DAT_803183fe;
      if (uVar4 < 10) {
        puVar13 = (undefined2 *)(&PTR_DAT_802c9b10)[uVar4];
      }
      uVar9 = 1;
      puVar10 = (&PTR_FUN_802c9b38)[uVar4 * 3];
      puVar11 = (&PTR_get_min_month_802c9b3c)[uVar4 * 3];
      puVar12 = (&PTR_get_max_month_802c9b40)[uVar4 * 3];
    }
    else {
      iVar5 = ui_cursor_key_pressed_p(down);
      if ((iVar5 != 1) || (1 < (byte)(g_down_button_enable - 2))) {
        iVar5 = ui_cursor_key_pressed_p(left);
        if ((iVar5 == 1) && (g_left_button_enable == 2)) {
          uVar4 = FUN_8010c9ac();
          uVar7 = get_max_month();
          if (uVar7 < uVar4) {
            _DAT_803183fc = _DAT_803183fc & 0xffff0000 | uVar7 & 0xffff;
          }
          right_p = 0;
        }
        else {
          iVar5 = ui_cursor_key_pressed_p(right);
          if ((iVar5 != 1) || (g_right_button_enable != 2)) {
            iVar5 = ui_cursor_key_pressed_p(enter);
            if ((iVar5 == 1) && (g_enter_button_enable == 2)) {
              uVar4 = FUN_8010c9ac();
              uVar7 = get_max_month();
              if (uVar7 < uVar4) {
                _DAT_803183fc = _DAT_803183fc & 0xffff0000 | uVar7 & 0xffff;
              }
              uVar4 = _DAT_803183fc & 0xffff;
              if ((_DAT_80318400 & 0xffff) == uVar4) {
                if ((DAT_803183fe == DAT_80318402) && (DAT_80316f10 == DAT_80316f12)) {
                  camera_config->field10_0xa = 1;
                  thunk_FUN_800e0588();
                  draw_jpg_image_on_screen(error);
                  goto LAB_80111110;
                }
              }
              camera_config->exit_menu_p_or_ir_led_on = 1;
              if (DAT_80316f10 == 1) {
                sVar1 = 0xc;
                if (uVar4 < 0xc) {
LAB_8011105c:
                  _DAT_803183fc = _DAT_803183fc & 0xffff0000 | (uint)(ushort)(DAT_803183fc + sVar1);
                }
              }
              else if ((DAT_80316f10 == 0) && (sVar1 = -0xc, 0xb < uVar4)) goto LAB_8011105c;
              if (DAT_80316f12 == 1) {
                if (DAT_80318400 < 0xc) {
                  _DAT_80318400 = _DAT_80318400 & 0xffff0000 | (uint)(ushort)(DAT_80318400 + 0xc);
                }
              }
              else if ((DAT_80316f12 == 0) && (0xb < DAT_80318400)) {
                _DAT_80318400 = _DAT_80318400 & 0xffff0000 | (uint)(ushort)(DAT_80318400 - 0xc);
              }
              FUN_8005c824(&DAT_803183fc);
              set_cold_item_capture_timer_p(1);
              FUN_800e4e04(_DAT_803183fc,_DAT_80318400);
              camera_config->commit_menu_change = 1;
            }
            else {
              iVar5 = ui_cursor_key_pressed_p(mode);
              if ((iVar5 != 1) || (g_mode_button_enable != 2)) goto LAB_80111110;
              camera_config->exit_menu_p_or_ir_led_on = 1;
            }
            iVar5 = get_next_state_from_menu_mode(1,(struct_menu_root **)&g_menu_root);
            if (iVar5 == 0xff) {
              iVar5 = 0x1f;
            }
            set_fsm_state_absolute(iVar5);
            goto LAB_80111110;
          }
          uVar4 = FUN_8010c9ac();
          uVar7 = get_max_month();
          if (uVar7 < uVar4) {
            _DAT_803183fc = _DAT_803183fc & 0xffff0000 | uVar7 & 0xffff;
          }
          right_p = 1;
        }
        update_time_field(right_p,&camera_config->menu_selection_1,1,&DAT_8030f938,10);
        goto LAB_80110f88;
      }
      uVar8 = 3;
      if (camera_config->menu_selection_2 < 3) {
        camera_config->menu_selection_2 = camera_config->menu_selection_2 + 1;
        uVar8 = 1;
      }
      uVar4 = (uint)camera_config->menu_selection_1;
      puVar13 = &DAT_803183fe;
      if (uVar4 < 10) {
        puVar13 = (undefined2 *)(&PTR_DAT_802c9b10)[uVar4];
      }
      uVar9 = 0;
      puVar10 = (&PTR_FUN_802c9b38)[uVar4 * 3];
      puVar11 = (&PTR_get_min_month_802c9b3c)[uVar4 * 3];
      puVar12 = (&PTR_get_max_month_802c9b40)[uVar4 * 3];
    }
    uVar3 = HceTask_ToNextNChar(uVar9,puVar10,puVar11,puVar12,uVar8);
    *puVar13 = uVar3;
  }
  else {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    camera_config->menu_selection_1 = 0;
    if (cVar2 == '\0') {
      FUN_800e6a0c(&DAT_803183fc);
      uVar7 = _DAT_803183fc & 0xffff;
      DAT_80316f10 = uVar7 < 0xc ^ 1;
      uVar4 = _DAT_80318400 & 0xffff;
      DAT_80316f12 = uVar4 < 0xc ^ 1;
      if (uVar7 == 0) {
        DAT_803183fc = 0xc;
      }
      else if (0xc < uVar7) {
        DAT_803183fc = DAT_803183fc - 0xc;
      }
      _DAT_803183fc = _DAT_803183fc & 0xffff0000 | (uint)DAT_803183fc;
      if (uVar4 == 0) {
        DAT_80318400 = 0xc;
      }
      else if (0xc < uVar4) {
        DAT_80318400 = DAT_80318400 - 0xc;
      }
      _DAT_80318400 = _DAT_80318400 & 0xffff0000 | (uint)DAT_80318400;
    }
    else {
      DAT_803183f8 = '\0';
    }
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
  }
LAB_80110f88:
  SetCaptureTimerParams_helper_function(camera_config->menu_selection_1);
LAB_80111110:
  iVar5 = ui_cursor_key_pressed_p(up);
  if (((iVar5 != 1) || (g_up_button_enable != 1)) &&
     ((iVar5 = ui_cursor_key_pressed_p(down), iVar5 != 1 || (g_down_button_enable != 1)))) {
    iVar5 = fsm_getNextState();
    iVar6 = fsm_getCurrentState();
    if (iVar5 == iVar6) {
      return;
    }
  }
  camera_config->menu_selection_2 = 0;
  return;
}
#endif
