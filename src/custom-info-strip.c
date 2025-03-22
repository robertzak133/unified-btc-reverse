// custom-ribbon.c
//     Routines which print the creation date and time of the current image/video
//     on the playback screen so that a person can read them without a magnifying glass

#include "BTC.h"
#include "custom-info-strip.h"
#include "capture-timer.h"
#include "rtc-formats.h"

//#define DEBUG

// wbwl_custom_info_strip_date_sprintf
//     replaces a call to "local_sprintf"
//     creates a string with the right date format
//
int wbwl_custom_info_strip_date_sprintf(char *buffer, char *format_string, 
					int month, int day, int year) {

    enum_rtc_date_format_options date_format = (enum_rtc_date_format_options) rtc_get_cold_item_date_format();

    switch(date_format) {
    case rtc_mm_dd_yyyy:
    default:
      local_sprintf(buffer,"%02d/%02d/%04d ", month, day, year);
      break;
    case rtc_dd_mm_yyyy:
      local_sprintf(buffer,"%02d/%02d/%04d ", day, month, year);
      break;
    case rtc_yyyymmdd:
      local_sprintf(buffer,"%04d%02d%02d ", year, month, day);
      break;
    case rtc_yyyy_mm_dd:
      local_sprintf(buffer,"%04d/%02d/%02d ", year, month, day);
      break;
    }
#ifdef DEBUG
    set_pre_printf_state();      
    tty_printf("wbwl_custom_info_strip_date_sprintf -e \n");
    check_post_printf_state_set_sio_params();
#endif

}

// wbwl_custom_info_strip_time_sprintf
//     replaces a call to "local_sprintf" used to build string printed in the
//     info strip.  Add the "seconds" field, from the clock
//     Awkwardly, we have to recreate the rtc structure because the original 
//        call that we're hijacking doesn't pass "seconds" as an argument
//        2023-07-08: On the other hand, since rtc_time is natively 24 hour format
//        we can just use it directly in 24 hour mode. 

int wbwl_custom_info_strip_time_sprintf(char *buffer, char *format_string, 
					int hour, int minute, char* am_pm_string) { 
  

  int second;
  struct_RTCTime rtc_time;
  get_rtc_time_or_alarm(0, &rtc_time);
  second = rtc_time.second;

  enum_rtc_time_format_options time_format = (enum_rtc_time_format_options) rtc_get_cold_item_time_format();

  switch(time_format) {
  case rtc_twelve_hour:
  default:
    local_sprintf(buffer, "%02d:%02d:%02d %s ", hour, minute, second, am_pm_string);
    break;
  case rtc_twenty_four_hour:
    local_sprintf(buffer, "%02d:%02d:%02d ", rtc_time.hour, rtc_time.minute, second);
    break;
  }

#ifdef DEBUG
    set_pre_printf_state();      
    tty_printf("wbwl_custom_info_strip_time_sprintf -e \n");
    check_post_printf_state_set_sio_params();
#endif

}
  

// Replaces the last call to strlen, called with the contents of the 
//     fully filled out contents of buffer
//     We're going to add a battery value
//     Then return as if nothing had happened. 

int wbwl_custom_info_strip_strlen(char *buffer) {

  int starting_length;
  int power_supply_mode;

  starting_length = btc_strlen(buffer);

#if (defined BTC_7A)
  power_supply_mode = ctm_get_power_supply_mode();
#else
  power_supply_mode = get_power_supply_mode();
#endif

  if (power_supply_mode == 0) {
    uint bytes_written;
    unsigned int battery_reading;
    battery_reading = get_battery_percent();
    bytes_written = local_sprintf(&buffer[starting_length], " B:%3d ", battery_reading);
  } else {
    local_sprintf(&buffer[starting_length], " B:EXT ");
  }

#ifdef DEBUG
    set_pre_printf_state();      
    tty_printf("wbwl_custom_info_strip_strlen -e \n");
    check_post_printf_state_set_sio_params();
#endif


  return(btc_strlen(buffer));
}


// Draw the logo at half size
//      note that you also have to set the expect size to be half size so the video buffer
//      is also halved in each dimension.  See hand patches. 
void wbwl_StampDrawLogo(struct_video_page_descriptor *video_page_descriptor, unsigned int font_scale){
  // halve the font scale
  unsigned int half_font_scale = font_scale >> 1;

  HceStampDrawLogo(video_page_descriptor, half_font_scale);

#ifdef DEBUG
  set_pre_printf_state();      
  tty_printf("wbwl_StampDrawLogo -e \n");
  check_post_printf_state_set_sio_params();
#endif

}
