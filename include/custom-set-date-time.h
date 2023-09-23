//
//  Include file for src cod which allows the set date-time menu
//      to use custom date/time formats


void cdt_get_set_date_time_functions (enum_date_time_menu_item selector, 
				      enum_rtc_date_format_options date_format,
				      enum_rtc_time_format_options time_format,
				      struct_menu_functions *menu_functions
				      );

short *cdt_get_date_time_current_field_value(enum_date_time_menu_item selector, 
					     enum_rtc_date_format_options date_format, 
					     enum_rtc_time_format_options time_format);

uint cdt_get_max_hour(void);
uint cdt_get_min_hour(void);

void cdt_menu_draw_selected_item(byte *selected_item,struct_menu_root **menu_root);
void cdt_handleSetTimeMenu(void);
int cdt_check_keyboard(struct_CameraConfig *camera_config);

void cdt_handle_up_down_buttons(struct_CameraConfig *camera_config,
			        int up_button_p);

void cdt_handle_left_right_buttons(struct_CameraConfig *camera_config, int left_button_p);

short cdt_twelve_to_twenty_four(short am_pm_p, short hour);
short cdt_twenty_four_to_twelve(short *am_pm_p, short hour);

void cdt_handle_enter_mode_buttons(struct_CameraConfig *camera_config, 
				   int enter_button_p);

void cdt_draw_set_time_screen(uint selected_item);


void cdt_btc_strcpy(char * dest_string, char * src_string);

