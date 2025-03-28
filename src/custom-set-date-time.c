//
// custom-set-date-time.c
//
// A new version of the date/time menu that allows time to be set using 24-hour clock (vs. AM/PM)
//       as controlled by the "Time Format" menu selection
// 
//       This code is a little hairy because of the original :(
//    2023-09-14
//       Change in requirements -- all I really need to do is to get the 
//       time in 12 or 24 hour format.  This does not require moving around any of the 
//       field locations, which is a vast simplification. 


#include "BTC.h"
#include "WBWL.h"
#include "rtc-formats.h"
#include "capture-timer.h"
#include "custom-set-date-time.h"

//#define DEBUG
// 
// Menu Item Order
// 
//                 Date
// Field    MM-DD-YYYY    
// 0        MM            
// 1        -NA-
// 2        DD
// 3        -NA-  
// 4        YYYY
//                 Time
//          12-Hour       24-Hour
// 5        HH < 13       HH < 24
// 6             -- NA --
// 7        MM < 60       MM < 60
// 8             -- NA --
// 9        AM/PM         NA



#if (defined BTC_7A_OLD) 
byte g_cst_set_time_buffer[10] = {0x1f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
#endif

void cdt_get_set_date_time_functions (enum_date_time_menu_item selector, 
				      enum_rtc_date_format_options date_format,
				      enum_rtc_time_format_options time_format,
				      struct_menu_functions *menu_functions
				      ) {
  switch(selector) {
  case dtm_nominal_month:
    menu_functions->current_value_function = get_g_menu_temp_month;
    menu_functions->min_value_function = get_min_month;
    menu_functions->max_value_function = get_max_month;
    break;
  case dtm_nominal_day:
    menu_functions->current_value_function = get_g_temp_day_number;
    menu_functions->min_value_function = get_min_day;
    menu_functions->max_value_function = get_max_day;
    break;
  case dtm_nominal_year:
    menu_functions->current_value_function = get_g_menu_temp_year;
    menu_functions->min_value_function = get_min_year;
    menu_functions->max_value_function = get_max_year;
    break;
  case dtm_nominal_hour:
    menu_functions->current_value_function = get_g_menu_temp_hour;   
    if (time_format == rtc_twelve_hour) {
      menu_functions->min_value_function = get_min_hour;
      menu_functions->max_value_function = get_max_hour;
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
  default:
    menu_functions->current_value_function = get_am_pm_current_value;
    menu_functions->min_value_function = get_am_pm_min_value;
    menu_functions->max_value_function = get_am_pm_max_value;
    break;
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

  get_current_date_time_short(&g_set_date_time_menu_state);

  // check to see whether we're in 24 hour mode:
  if(time_format == rtc_twelve_hour) {
    g_set_date_time_menu_state.hour = cdt_twelve_to_twenty_four(g_temp_am_pm_p, g_set_date_time_menu_state.hour);
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

    enum_rtc_time_format_options time_format = (enum_rtc_time_format_options) rtc_get_cold_item_time_format();
    if (time_format ==  rtc_twelve_hour) {
      // need to convert internal 24-hour state to 
      g_set_date_time_menu_state.hour = cdt_twenty_four_to_twelve(&g_temp_am_pm_p, g_set_date_time_menu_state.hour);
    }
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
  } 

  // Now Display the menu
#ifdef DEBUG_VERBOSE
  set_pre_printf_state();
  tty_printf("cdt_handleSetTimeMenu : drawing screen \n");
  check_post_printf_state_set_sio_params();
#endif
  draw_set_time_screen(camera_config->menu_selection_1);
  // cdt_draw_set_time_screen(camera_config->menu_selection_1);
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

#if (defined BTC_7A_OLD) 
uint cdt_HceTask_ToNextNChar(int up_button_p,uint current_value_function(), uint min_value_function(), uint max_value_function(),ushort next_item)
{
  uint max_value;
  int iVar2;
  uint current_value;
  uint uVar4;
  uint min_value;
  uint l_next_item;
  
  l_next_item = (uint)next_item;
  current_value = 0;
  if (up_button_p == 0) {
    if (current_value_function != (void *)0x0) {
      current_value = (*current_value_function)();
    }
    min_value = 0;
    if (min_value_function != (void *)0x0) {
      min_value = (*min_value_function)();
    }
    max_value = 0xffff;
    if (max_value_function == (void *)0x0) {
      iVar2 = 0xffff - min_value;
    }
    else {
      max_value = (*max_value_function)();
      if (max_value < min_value) {
        return current_value;
      }
      iVar2 = max_value - min_value;
    }
    if (iVar2 < 0) {
      iVar2 = iVar2 + 3;
    }
    uVar4 = (uint)(iVar2 << 0xe) >> 0x10;
    if (uVar4 == 0) {
      uVar4 = 1;
    }
    if (uVar4 < l_next_item) {
      //set_pre_printf_state();
      //tty_printf(s_%s_Menu_Speed_Ctrl,_max_speed_@_%_8036f924,s_HceTask_ToPrevNChar_8035539c,l_next_item,
      //           uVar4);
      //check_post_printf_state_set_sio_params();
      l_next_item = uVar4;
    }
    if ((int)current_value < (int)(min_value + l_next_item)) {
      current_value = max_value + ((current_value + 1) - min_value);
    }
    current_value = current_value - l_next_item;
  }
  else {
    if (current_value_function != (void *)0x0) {
      current_value = (*current_value_function)();
    }
    min_value = 0;
    if (min_value_function != (void *)0x0) {
      min_value = (*min_value_function)();
    }
    if (max_value_function == (void *)0x0) {
      max_value = 0xffff;
      iVar2 = 0xffff - min_value;
    }
    else {
      max_value = (*max_value_function)();
      if (max_value < min_value) {
        return current_value;
      }
      iVar2 = max_value - min_value;
    }
    if (iVar2 < 0) {
      iVar2 = iVar2 + 3;
    }
    uVar4 = (uint)(iVar2 << 0xe) >> 0x10;
    if (uVar4 == 0) {
      uVar4 = 1;
    }
    if (uVar4 < l_next_item) {
      //set_pre_printf_state();
      //tty_printf(s_%s_Menu_Speed_Ctrl,_max_speed_@_%_8036f924,s_HceTask_ToNextNChar_803553b0,l_next_item,
      //           uVar4);
      //check_post_printf_state_set_sio_params();
      l_next_item = uVar4;
    }
    if ((int)(max_value - l_next_item) < (int)current_value) {
      current_value = (min_value + (current_value - 1)) - max_value;
    }
    current_value = current_value + l_next_item;
  }
  return current_value & 0xffff;
}
#endif
  
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

#if (defined BTC_7A_OLD) 
  *current_field_value = cdt_HceTask_ToNextNChar(up_button_p,
					     date_time_menu_functions.current_value_function,
					     date_time_menu_functions.min_value_function,
					     date_time_menu_functions.max_value_function, 
					     next_item);

#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5) 
  *current_field_value = HceTask_ToNextNChar(up_button_p,
					     date_time_menu_functions.current_value_function,
					     date_time_menu_functions.min_value_function,
					     date_time_menu_functions.max_value_function, 
					     next_item);
#endif
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
#if (defined BTC_7A_OLD) 
  //update_time_field(right_p,&camera_config->menu_selection_1,1,g_cst_set_time_buffer,10);
  update_time_field(right_p,&camera_config->menu_selection_1,1,g_set_time_buffer,10);
#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
  update_time_field(right_p,&camera_config->menu_selection_1,1,g_set_time_buffer,10);
#endif
}



// Convert an hour in 24-hour to 12 + AM/PM format (native)
//     12A        0        1
//      1A        1        1
//      :
//     11A        11       1
//     12P        12       0
//      1PM       13       0
//      :
//     11PM       23       0
short cdt_twelve_to_twenty_four(short am_pm_p, short hour) {
  short return_hour;
  if (am_pm_p == 0) {
    // It's AM
    if (hour == 12) {
      return_hour = 0;
    } else {
      return_hour = hour;
    }
  } else {
    // It's PM
    if(hour == 12) {
      return_hour = hour;
    } else {
      return_hour = 12 + hour;
    }
  }
  return return_hour;
}

short cdt_twenty_four_to_twelve(short *am_pm_p, short hour) {
  short return_hour;
  if (hour < 12) {
    *am_pm_p = 0;
    if (hour == 0) {
      return_hour = 12;
    } else {
      return_hour = hour;
    }
  } else {
    *am_pm_p = 1;
    if (hour == 12) {
      return_hour = hour;
    } else {
      return_hour = hour - 12;
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
#if (defined BTC_7A_OLD)
    uint capture_timer_p  = ctm_get_cold_item_capture_timer_p();
#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
    uint capture_timer_p  = get_cold_item_capture_timer_p();
#else
    *** ERROR *** Invalid Target
#endif
    if (capture_timer_p != 0) {
      struct_short_RTCTime short_rtc_time;
      struct_short_RTC_as_uints *rtc_as_uints = (struct_short_RTC_as_uints *)&short_rtc_time;

#if (defined BTC_7A_OLD)
      ctm_get_capture_timer_rtc_time(&short_rtc_time);
      ctm_reset_capture_timer(rtc_as_uints->year_month,
			  rtc_as_uints->day_hour);

#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
      get_capture_timer_rtc_time(&short_rtc_time);
      reset_capture_timer(rtc_as_uints->year_month,
			  rtc_as_uints->day_hour);
#endif
    }
#if (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
    set_cold_item_timelapse_new_file_p(1);
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


// Patched into draw_set_time_screen()
//  in place of btc_strcopy() near line 159
//  if we're in 24 hour mode, and the string contains AM or PM, then
//  substitute in a blank

void cdt_btc_strcpy(char * dest_string, char * src_string) {
  enum_rtc_time_format_options time_format = (enum_rtc_time_format_options) rtc_get_cold_item_time_format();

  // take control if necessary to null out AM/PM field in 24-hour mode
  if ((time_format == rtc_twenty_four_hour) &&
      ((src_string[0] == 'A') || (src_string[0] == 'P'))) {
      btc_strcpy(dest_string, " ");
      return;
  }
  btc_strcpy(dest_string, src_string);
}

short *cdt_get_date_time_current_field_value(enum_date_time_menu_item selector, 
					    enum_rtc_date_format_options date_format, 
					    enum_rtc_time_format_options time_format) {

  if (selector <= dtm_nominal_year) {
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

