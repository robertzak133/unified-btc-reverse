
//
// rtc-formats.h 
// Prototypes for RTC format menus
//


typedef enum enum_rtc_date_format_options {
  rtc_mm_dd_yyyy = 0,
  rtc_dd_mm_yyyy,
  rtc_yyyymmdd,
  rtc_yyyy_mm_dd
} enum_rtc_date_format_options;

typedef enum enum_rtc_time_format_options {
  rtc_twelve_hour = 0,
  rtc_twenty_four_hour
} enum_rtc_time_format_options;

// Global Variables
// Menus
struct_hp5_menu_item g_rtc_date_format_menu[5];
struct_hp5_menu_item g_rtc_time_format_menu[3];

// 
byte rtc_get_cold_item_date_format();

void rtc_set_cold_item_date_format(byte date_format);

byte rtc_get_cold_item_time_format();

void rtc_set_cold_item_time_format(byte date_format);

void rtc_handle_date_format_menu();

void rtc_handle_time_format_menu();

