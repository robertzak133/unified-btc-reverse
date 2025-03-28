// 
// BTC.h
// Structures, typedefs, and function prototypes found
// in the binary (as reflected by Ghidra).

#include "SST-strings.h"


// Handy Constants

#define COLD_ITEM_SIGNATURE  0x5a3c

// Imported (manually) from Ghidra
// 

typedef unsigned char    bool;
typedef unsigned char    byte;
typedef unsigned int     uint;
typedef unsigned short   ushort;

// Enums w/ typedefs



typedef enum enum_tod_in_timelapse {
  daylight_post_sunrise_region = 0,
  daylight_no_photo_region,
  daylight_pre_sunset_region,
  night_no_photo_region
//  night_photo_region
} enum_tod_in_timelapse;

typedef enum enum_timelapse_period_encoding {
  all_day = 0,
  one_hour,
  two_hours,
  three_hours,
  four_hours,
  all_day_night
} enum_timelapse_period_encoding;

typedef enum enum_pir_range_options {
  pir_normal_range = 0,
  pir_long_range, 
  pir_short_range
} enum_pir_range_options;

typedef enum enum_digital_effect {
 color = 0,
 bw,
 unknown_effect,
 vivid,
 natural,
 negative,
 warm,
 cold,
 red,
 breen,
 blue,
 brightness,
 hue
} enum_digital_effect;

typedef enum enum_ui_cursor_button {
  up = 0,
  down,
  left,
  right,
  enter,
  mode
} enum_ui_cursor_button;

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
typedef enum enum_battery_type {
  lithium = 0,
  alkaline = 1
} enum_battery_type;
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
typedef enum enum_battery_type {
  lithium = 0,
  alkaline = 1,
  nimh     = 2
} enum_battery_type;
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
typedef enum enum_battery_type {
  lithium = 0,
  alkaline = 1,
  nimh     = 2
} enum_battery_type;
#endif

// Photo Quality Settings
typedef enum enum_photo_quality {
  low_4MP = 0,
  medium_8MP,
  high_12MP,
  ultra_20MP,
  native_2MP
} enum_photo_quality;

// Time scaler for thread_sleep function
typedef enum enum_timer_wait_scale {
  divide_by_10 = 0,
  times_1,
  times_10,
  times_1000
} enum_timer_wait_scale;

// Flash intensity (including "no flash")
typedef enum enum_flash_intensity {
  flash_off = 0,
  flash_low,
  flash_high
} enum_flash_intensity;

#if (defined BTC_7A_OLD) 
typedef enum enum_jpg_icon_index {
  setup	= 0x0, 
  playback, 
  home, 
  datetime,
  opmode, 
  photo_quality, 
  video_length, 
  video_quality,
  photo_delay,
  multishot,
  temp_unit,
  camera_name,
  stamp,
  motion_test,
  pir_range,
  battery_type,
  trigger_speed,
  restore_default,
  plot_frequency,
  plot_period,
  timelapse_quality,
  delete_one,
  delete_all,
  tv_out,
  sd_management,
  smart_ir,
  ir_flash_power,
  firmware_upgrade,
  no_icon
} enum_jpg_icon_index;

#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
typedef enum enum_jpg_icon_index {
  setup	= 0x0, 
  playback, 
  home, 
  datetime,
  opmode, 
  photo_quality, 
  video_length, 
  video_quality,
  photo_delay,
  multishot,
  temp_unit,
  camera_name,
  stamp,
  motion_test,
  pir_range,
  battery_type,
  trigger_speed,
  restore_default,
  plot_frequency,
  plot_period,
  timelapse_quality,
  delete_one,
  delete_all,
  tv_out,
  sd_management,
  smart_ir,
  ir_flash_power,
  set_language,
  set_sd_power_down,
  capture_timer,
  firmware_upgrade,
  no_icon
} enum_jpg_icon_index;
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
typedef enum enum_jpg_icon_index {
  setup	= 0x0, 
  playback, 
  home, 
  datetime,
  opmode, 
  photo_quality, 
  video_length, 
  video_quality,
  photo_delay,
  multishot,
  temp_unit,
  camera_name,
  stamp,
  motion_test,
  pir_range,
  battery_type,
  trigger_speed,
  restore_default,
  plot_frequency,
  plot_period,
  timelapse_quality,
  delete_one,
  delete_all,
  tv_out,
  sd_management,
  smart_ir,
  ir_flash_power,
  set_language,
  set_sd_power_down,
  capture_timer,
  firmware_upgrade,
  no_icon
} enum_jpg_icon_index;
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
typedef enum enum_jpg_icon_index {
  setup	= 0x0, 
  playback, 
  home, 
  datetime,
  opmode, 
  photo_quality, 
  video_length, 
  video_quality,
  photo_delay,
  multishot,
  temp_unit,
  camera_name,
  stamp,
  motion_test,
  pir_range,
  battery_type,
  trigger_speed,
  restore_default,
  plot_frequency,
  plot_period,
  timelapse_quality,
  delete_one,
  delete_all,
  tv_out,
  sd_management,
  smart_ir,
  ir_flash_power,
  set_language,
  set_sd_power_down,
  capture_timer,
  hdr, 
  firmware_upgrade,
  no_icon
} enum_jpg_icon_index;
#endif


typedef enum enum_menu_selection_action {
  not_known = 0,
  back_to_parent = 1,
  new_child = 2
} enum_menu_selection_action;

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
typedef enum enum_cold_item_ir_led_intensity {
  economy = 0,
  long_range,
  off
} enum_cold_item_ir_led_intensity;

#elif  (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
typedef enum enum_cold_item_ir_led_intensity {
  economy = 0,
  long_range,
  blur_reduction,
  off
} enum_cold_item_ir_led_intensity;

#elif (defined BTC_7A) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
typedef enum enum_cold_item_ir_led_intensity {
  economy = 0,
  long_range,
  blur_reduction,
  off,
  overflow
} enum_cold_item_ir_led_intensity;
#endif

typedef enum enum_alt_ir_led_intensity {
  high_80_pct = 0,
  med_50_pct,
  low_25_pct,
  very_high_90_pct
} enum_alt_ir_led_intensity;

typedef enum enum_operation_mode {
  trail_camera = 0,
  video,
  timelapse
} enum_operation_mode;

typedef enum enum_tls_file_type {
  tls_file_type_tls = 0,
  tls_file_type_jpg,
  tls_file_type_mp4
} enum_tls_file_type;


typedef enum enum_video_length {
  vl_two_minutes = 0,
  vl_one_minute, 
  vl_thirty_seconds,
  vl_twenty_seconds,
  vl_ten_seconds,
  vl_five_seconds
} enum_video_length;

typedef enum enum_photo_delay_encoding {
  pd_one_second = 0,
  pd_five_seconds,
  pd_ten_seconds,
  pd_twenty_seconds,
  pd_thirty_seconds,
  pd_one_minute,
  pd_five_minutes,
  pd_ten_minutes,
  pd_thirty_minutes,
  pd_sixty_minutes
} enum_photo_delay_encoding;

typedef enum enum_multi_shot_encoding {
  ms_8_shot_standard = 0,
  ms_7_shot_standard,
  ms_6_shot_standard,
  ms_5_shot_standard,
  ms_4_shot_standard,
  ms_3_shot_standard,
  ms_2_shot_standard,
  ms_single_shot,
  ms_8_shot_rapid,
  ms_7_shot_rapid,
  ms_6_shot_rapid,
  ms_5_shot_rapid,
  ms_4_shot_rapid,
  ms_3_shot_rapid,
  ms_2_shot_rapid
} enum_multi_shot_encoding;

// Structures w/ typedefs

typedef struct struct_event_descriptor {
  int event_number;
  int qualifier_1;
  int qualifier_2;
} struct_event_descriptor;


typedef struct struct_dcfapi_functions {
  uint library_id;
  void (*unknown11)();
  void (*unknown10)();
  void (*unknown9)();
  void (*set_dir_suffix_image_prefix)();
  void (*get_dir_suffix_image_prefix)();
  void (*set_dir_image_indices)();
  void (*get_dir_image_indices)();
  void (*unknown8)();
  void (*unknown7)();
  void (*unknown6)();
  void (*unknown5)();
  void (*del_file_helper)();
  void (*get_dcf_index)();
  void (*set_next_dcf)();
  void (*get_next_dcf)();
  void (*set_next_image_path)();
  void (*get_next_image_path)();
  void (*set_alt2_dir_image_indices)();
  void (*get_alt2_dir_image_indices)();
  void (*unknown12)();
  void (*func_0x54)();
  void (*func_0x58)();
  void (*func_0x5c)();
  void (*media_trim)();
  void (*func_0x64)();
  void (*set_alt_dir_image_indices)();
  void (*get_alt_dir_image_indices)();
  void (*func_0x70)();
  void (*unknown14)();
  void (*func_0x78)();
  void (*func_0x7c)();
  void (*func_0x80)();
  void (*func_0x84)();
  void (*func_0x88)();
  void (*recover_fun)();
  void (*unknown15)();
  void (*unknown16)();
  void (*unknown17)();
  void (*func_0x9c)();
  void (*func_0xa0)();
} struct_dcfapi_functions;

typedef struct struct_photo_dimensions_int {
  uint width;
  uint height;
  uint width_hi;
  uint height_hi;
} struct_photo_dimensions_int;

typedef struct struct_photo_dimensions_short {
  ushort width;
  ushort height;
} struct_photo_dimensions_short;

typedef struct struct_image_descriptor {
  uint field0x0;
  uint rounded_width;
  uint rounded_height;
  uint field0xc;
  uint field0x10;
  uint alt_width;
  uint alt_height;
  uint jpg_width;
  uint jpg_height;
  uint field_0x24;
  uint field_0x28;
  uint field_0x2c;
  uint field_0x30;
  uint width;
  uint height;
  uint field_0x3c;
  uint field_0x40;
  uint num_ushort_pixels;
} struct_image_descriptor;


typedef struct struct_system_device_entry {
  uint field_0;
  uint field_4;
  uint field_8;
  uint num_sectors;
} struct_system_device_entry;

typedef struct struct_pressure_temperature_coefficients {
  uint c0;
  uint c1;
  uint c00;
  uint c10;
  uint c01;
  uint c11;
  uint c20;
  uint c21;
  uint c30;
} struct_pressure_temperature_coefficients;

typedef struct struct_i2c_pressure_temperature_coefficients {
  byte address;
  byte c0_11_4;            // 0x10
  byte c0_3_0_c1_11_8;     // 0x11
  byte c1_7_0;             // 0x12
  byte c00_19_12;          // 0x13
  byte c00_11_4;           // 0x14
  byte c00_3_0_c10_19_16;  // 0x15
  byte c10_15_8;           // 0x16
  byte c10_7_0;            // 0x17
  byte c01_15_8;           // 0x18
  byte c01_7_0;            // 0x19
  byte c11_15_8;           // 0x1a
  byte c11_7_0;            // 0x1b
  byte c20_15_8;           // 0x1c
  byte c20_7_0;            // 0x1d
  byte c21_15_8;           // 0x1e
  byte c21_7_0;            // 0x1f
  byte c30_15_8;           // 0x20
  byte c30_7_0;            // 0x21
} struct_i2c_pressure_temperature_coefficients;
// Menu-related structures

typedef enum enum_date_time_menu_item {
  dtm_nominal_month = 0,
  dtm_nominal_day   = 2,
  dtm_nominal_year  = 4,
  dtm_nominal_hour  = 5,
  dtm_nominal_minute = 7,
  dtm_nominal_am_pm = 9
}  enum_date_time_menu_item;

typedef enum enum_capture_timer_menu_item {
  ctm_nominal_start_hour = 0,
  ctm_nominal_start_minute = 2,
  ctm_nominal_start_am_pm = 4,
  ctm_nominal_end_hour  = 5,
  ctm_nominal_end_minute = 7,
  ctm_nominal_end_am_pm = 9
} enum_capture_timer_menu_item;


typedef struct struct_capture_menu_display_state{
  short start_hour;
  short start_minute;
  short start_am_pm;
  short end_hour;
  short end_minutes;
  short end_am_pm;
} struct_capture_menu_display_state;

typedef struct struct_capture_menu_internal_state{
  short start_hour;
  short start_minute;
  short end_hour;
  short end_minutes;
} struct_capture_menu_internal_state;


typedef struct struct_menu_functions {
  uint (*current_value_function)();
  uint (*min_value_function)();
  uint (*max_value_function)();
} struct_menu_functions;

#if (defined BTC_7A_OLD)
typedef struct struct_hp5_menu_item {
  enum_jpg_icon_index   icon_index;
  char  *text_ptr;
  uint   disable_item; 
  uint   menu_increment;
  enum_menu_selection_action menu_selection_action;
  uint   return_state_id;
  uint   next_state_id;
} struct_hp5_menu_item;
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7A)
typedef struct struct_hp5_menu_item {
  enum_jpg_icon_index   icon_index;
  enum_sst_string   text_id;
  uint   disable_item; 
  uint   menu_increment;
  enum_menu_selection_action menu_selection_action;
  uint   return_state_id;
  uint   next_state_id;
} struct_hp5_menu_item;
#endif

typedef struct struct_menu_selections_descriptor {
  struct_hp5_menu_item  *menu_item_array;
  uint  num_array_entries;
} struct_menu_selections_descriptor;


typedef struct struct_menu_root {
  byte current_selection;
  byte next_selection;
  byte field_0x2;
  byte field_0x3;
  struct_hp5_menu_item *menu_item_array;
  uint num_items_and_title;
  char *       menu_item_name;
  struct struct_menu_root *child_menu_root;
  struct struct_menu_root *parent_menu_root;
} struct_menu_root;

typedef struct struct_menu_descriptor {
  byte next_state_id;
  byte next_selection;
  byte field_0x2;
  byte field_0x3;
  void *menu_item_collection;
  byte num_item_and_title;
  byte field_0x9;
  byte field_0xa;
  byte field_0xb;
  struct_hp5_menu_item *menu_item_array;
  struct struct_menu_descriptor *child_menu_descriptor;
  struct struct_menu_descriptor *parent_menu_descriptor;
} struct_menu_descriptor;

// MPU SPI Access structures
typedef struct struct_mpu_spi_address {
  byte addr0;
  byte addr1;
  byte addr2;
} struct_mpu_spi_address;

typedef struct struct_mpu_spi_addr {
  byte addr0;
  byte addr1;
} struct_mpu_spi_addr;

typedef struct struct_mpu_spi_data {
  byte data0;
  byte data1;
  byte data2;
} struct_mpu_spi_data;

typedef struct struct_mpu_spi_data_2B {
  byte data0;
  byte data1;
} struct_mpu_spi_data_2B;

// Real Time Clock Structures
typedef struct struct_RTCTime {
  int  second;
  int  minute;
  int  hour;
  int  day;
  int  month;
  int  year_from_1900; 
  int  unknown_a;
  int  day_of_the_year;
  int  unknown_b;
} struct_RTCTime;

typedef struct struct_short_RTCTime {
  short  year; 
  short  month;
  short  day;
  short  hour;
  short  minute;
  short  second;
} struct_short_RTCTime;

typedef struct struct_short_RTC_as_uints {
  uint year_month;
  uint day_hour;
  uint minute_second;
} struct_short_RTC_as_uints;

typedef struct struct_DateTime {
  uint second;
  uint minute;
  uint hour;
  uint day;
  uint month;
  uint year;
  uint unknown1;
  uint unknown2;
  int flag;
} struct_DateTime;


// Camera config -- go-to structure with everything but the kitchen sink
//    These are my nemesis in as much as they can change gen-on-gen in a difficult
//    to track way :(
#if (defined BTC_7A_OLD)
typedef struct struct_CameraConfig {
  byte exit_menu_p_or_ir_led_on; // 0
  byte video_p;
  byte menu_selection_1;         // 2
  byte menu_selection_2;         // 3
  // a bunch of unknown ints
  byte commit_menu_change;       // 4
  byte field_05_1;               // 5
  byte field_06_1;               // 6
  byte field_07_1;               // 7
  byte field_08_1;               // 8
  byte field_09_1;               // 9
  byte field_10_1;               // 10
  byte field_11_1;               // 11
  byte field_12_1;               // 12
  byte field_13_1;               // 13
  byte field_14_1;               // 14
  byte field_15_1;               // 15
  byte field_16_1;               // 16
  byte field_17_1;               // 17
  byte field_18_1;               // 18
  byte field_19_1;               // 19
  byte field_20_1;               // 20
  byte field_21_1;               // 21
  byte field_22_1;               // 22
  byte field_23_1;               // 23
  short current_video_runtime;   // 24
  short current_video_length;    // 26
  short video_length;            // 28
  byte fileld_30_1;              // 30
  byte fileld_31_1;              // 30
  byte fileld_32_1;              // 32
  byte still_flash_on;           // 33
  byte field_34_1;               // 34
  byte field_35_1;               // 35
  byte field_36_1;               // 36
  byte some_timelapse_field;    // 37
  byte field_38_1;              // 38
  byte abort_current_image_p;   // 39
  uint jpg_file_id;             // 40
  uint jpg_file_size;           // 44
  byte unknown_byte_48;
  byte unknown_byte_49;
  byte unknown_byte_50;
  byte unknown_byte_51;
  byte unknown_byte_52;
  byte unknown_byte_53;
  byte unknown_byte_54;
  byte unknown_byte_55;
  byte unknown_byte_56;
  byte unknown_byte_57;
  byte unknown_byte_58;
  byte unknown_byte_59;
  byte unknown_byte_60;
  byte unknown_byte_61;
  short video_end_time_us; // 62
  short photo_end_time_us; // 64
  short unknown_short_66; 
  uint still_led_turned_on_time_us; // 68
  uint unknown_uint_72;
  int total_images; // 76
  int current_image; //80
  char current_filename[200]; //84
} struct_CameraConfig;

#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) 
typedef struct struct_CameraConfig {
  byte exit_menu_p_or_ir_led_on; // 0
  byte video_p;
  byte menu_selection_1;         // 2
  byte menu_selection_2;         // 3
  // a bunch of unknown ints
  byte unknown_byte_5;           // 4
  byte ae_value0;                // 5
  byte commit_menu_change;       // 6
  byte ae_value1;                // 7
  byte field_8;                  // 8
  byte ae_value2;                // 9
  byte field_10;                 // 10
  byte field_11;                 // 11
  uint unknown_uint_12;          // 12
  uint unknown_uint_16;          // 16
  byte field_20;                 // 20
  byte field_21;                 // 21
  byte field_22;                 // 22
  byte field_23;                 // 23
  byte current_video_runtime;    // 24
  byte field_25;                 // 25
  byte current_video_length;     // 26
  byte field_27;                 // 27
  uint video_length;             // 28
  byte unknown_byte_32;          // 32
  byte still_flash_on;           // 33
  byte unknown_byte_34;          // 34
  byte unknown_byte_35;          // 35
  byte unknown_byte_36;          // 36
  byte image_strip_enable_p;    // 37
  byte some_timelapse_field;    // 38
  byte abort_current_image_p;   // 39
  uint jpg_file_id;             // 40
  uint jpg_file_size;           // 44
  byte unknown_byte_48;
  byte unknown_byte_49;
  byte unknown_byte_50;
  byte unknown_byte_51;
  byte unknown_byte_52;
  byte unknown_byte_53;
  byte unknown_byte_54;
  byte unknown_byte_55;
  byte unknown_byte_56;
  byte unknown_byte_57;
  byte unknown_byte_58;
  byte unknown_byte_59;
  byte unknown_byte_60;
  byte unknown_byte_61;
  short video_end_time_us; // 62
  short photo_end_time_us; // 64
  short unknown_short_66; 
  uint still_led_turned_on_time_us; // 68
  uint unknown_uint_72;
  byte total_still_burst_images;  // 76
  byte total_to_view_images;      // 77
  byte unknown_byte_78;           // 78
  byte unknown_byte_79;           // 79
  int current_image; //80
  char current_filename[200]; //84
} struct_CameraConfig;
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
typedef struct struct_CameraConfig {
  byte exit_menu_p_or_ir_led_on;
  byte video_p;
  byte menu_selection_1;
  byte menu_selection_2;
  // a bunch of unknown ints
  byte commit_menu_change;
  byte unknown_byte_5;
  byte unknown_byte_6;
  byte unknown_byte_7;
  byte unknown_byte_8;
  byte unknown_byte_9;
  byte unknown_byte_10;
  byte unknown_byte_11;
  byte unknown_byte_12;
  byte unknown_byte_13;
  byte unknown_byte_14;
  byte unknown_byte_15;
  byte unknown_byte_16;
  byte unknown_byte_17;
  byte unknown_byte_18;
  byte unknown_byte_19;
  byte unknown_byte_20;
  byte unknown_byte_21;
  byte unknown_byte_22;
  byte unknown_byte_23;
  short current_video_runtime;
  short current_video_length;
  short video_length;
  byte unknown_byte_30;
  byte unknown_byte_31;
  byte unknown_byte_32;
  byte still_flash_on;
  byte unknown_byte_34;
  byte unknown_byte_35;
  byte unknown_byte_36;
  byte unknown_byte_37;
  byte unknown_byte_38;
  byte abort_current_image_p; // 39
  byte unknown_byte_40;
  byte unknown_byte_41;
  byte unknown_byte_42;
  byte unknown_byte_43;
  byte unknown_byte_44;
  byte unknown_byte_45;
  byte unknown_byte_46;
  byte unknown_byte_47;
  byte unknown_byte_48;
  byte unknown_byte_49;
  byte unknown_byte_50;
  byte unknown_byte_51;
  byte unknown_byte_52;
  byte unknown_byte_53;
  byte unknown_byte_54;
  byte unknown_byte_55;
  byte unknown_byte_56;
  byte unknown_byte_57;
  byte unknown_byte_58;
  byte unknown_byte_59;
  byte unknown_byte_60;
  byte smart_ir_video_p;
  byte unknown_byte_62;
  byte unknown_byte_63;
  short photo_end_time_in_us;
  byte unknown_byte_66;
  byte unknown_byte_67;
  byte unknown_byte_68;
  byte unknown_byte_69;
  byte still_led_turned_on_time_us;
  byte unknown_byte_71;
  byte unknown_byte_72;
  byte unknown_byte_73;
  byte unknown_byte_74;
  byte unknown_byte_75;
  uint total_images;
  uint current_image;
  char current_filename[200];
} struct_CameraConfig;

#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
typedef struct struct_CameraConfig {
  byte exit_menu_p_or_ir_led_on;
  byte video_p;
  byte menu_selection_1;
  byte menu_selection_2;
  byte pir_detector_triggered;
  byte field_0x05;
  byte commit_menu_change;
  byte field_0x07;
  byte field_0x08;
  byte field_0x09;
  byte field_0x0a;
  byte field_0x0b;
  byte field_0x0c;
  byte field_0x0d;
  byte field_0x0e;
  byte field_0x0f;
  byte field_0x10;
  byte field_0x11;
  byte field_0x12;
  byte field_0x13;
  byte field_0x14;
  byte field_0x15;
  byte field_0x16;
  byte field_0x17;
  byte current_video_runtime;
  byte field_0x19;
  byte current_video_length;
  byte field_0x1b;
  short video_length;
  byte field_0x1e;
  byte field_0x1f;
  byte field_0x20;
  byte still_flash_on;
  byte field_0x22;
  byte field_0x23;
  byte new_tlps_file_p;
  byte sd_card_mounted;
  byte field_0x26;
  byte abort_current_image_p;
  uint tls_jpg_file_ptr;
  uint jpg_file_size;
  byte *jpg_file_buffer;
  byte field_0x34;
  byte field_0x35;
  byte field_0x36;
  byte field_0x37;
  byte field_0x38;
  byte field_0x39;
  byte field_0x3a;
  byte field_0x3b;
  byte field_0x3c;
  byte field_0x3d;
  short video_end_time_us;
  short photo_end_time_in_us;
  byte field_0x42;
  byte field_0x43;
  uint still_led_turned_on_time_us;
  byte field_0x48;
  byte field_0x49;
  byte field_0x4a;
  byte field_0x4b;
  int  total_images;
  int current_image;
  char current_filename[200];
} struct_CameraConfig;
#endif

typedef struct struct_PosixFinfo {
  char filename[512];
  char backup_filename[512];
  uint field_1024;
  uint field_1028;
  uint file_mode;
  uint field_1036;
  uint field_1040;
  uint field_1044;
  uint field_1048;
  uint field_1052;
  uint file_size_low;
  uint file_size_high;
  uint date_only_created_time;
  uint some_time;
  uint created_time;
  uint attributes;
} struct_PosixFinfo;



typedef struct struct_fsm_template {
  void * fsm_iterator_function;
  uint ref_count;
  int fsm_active;
  uint state_vector;
  struct_CameraConfig *camera_config;
} struct_fsm_template;



typedef struct struct_video_page_descriptor {
  void * stamp_buffer;
  uint unknown_04;
  uint unknown_08;
  uint unknown_12;
  uint unknown_16;
  int  background_width;
  uint background_height;
  uint unknown_28;
  uint unknown_32;
  uint unknown_36;
  uint unknown_40;
  uint unknown_44;
  uint unknown_48;
  int  fg_width;
  uint fg_height;
  uint unknown_60;
  uint unknown_64;
  uint unknown_68;
  uint unknown_72;
  uint unknown_76;
  uint unknown_80;
  uint unknown_84;
  uint unknown_88;
  uint unknown_92;
  uint unknown_96;
  uint unknown_100;
  uint unknown_104;
  uint unknown_108;
  uint unknown_112;
  uint unknown_116;
  uint unknown_120;
  uint unknown_124;
} struct_video_page_descriptor;


// Cold storage Data structure

//      Edge-Specific
#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
typedef struct struct_ColdBinData {
  short                file_length;
  byte                 busy_p;
  byte                 field_03_1;
  struct_short_RTCTime short_RTC_time;
  short                previous_MCU;
  short                current_MCU;
  enum_operation_mode  operation_mode;
  uint                 field_20_4;
  uint                 photo_resolution;
  byte                 video_resolution;
  byte                 field_33_1;
  byte                 field_34_1;
  byte                 field_35_1;
  enum_video_length    video_duration;
  short                field_40_2;
  byte                 field_42_1;
  byte                 field_43_1;
  enum_photo_delay_encoding photo_delay;
  short                photo_delay_in_seconds;
  byte                 field_50_1;
  byte                 timelapse_file_type;
  uint         multi_shot_encoding;
  enum_cold_item_ir_led_intensity led_power;
  byte                 field_60_1;
  byte                 field_61_1;
  byte                 field_62_1;
  byte                 field_63_1;
  byte                 image_data_strip_p;
  byte                 aperture;
  byte                 external_trigger;
  byte                 date_format;
  uint         temperature_unit_celsius_p;
  byte                 field_72_1;
  byte                 field_73_1;
  byte                 field_74_1;
  byte                 field_75_1;
  uint         pir_range;
  enum_battery_type    battery_type;
  uint         trigger_speed;
  byte                 field_88_1;
  byte                 field_89_1;
  byte                 field_90_1;
  byte                 field_91_1;
  byte                 smart_ir_video_p;
  byte                 sd_management_p;
  byte                 field_94_1;
  byte                 time_format;
  byte                 field_96_1;
  byte                 field_97_1;
  byte                 field_98_1;
  byte                 night_mode;
  short                pressure_trend_array[6];
  short                pressure_trend_time;
  byte                 pressure_trend_index;
  byte                 field_115_1;
  byte                 field_116_1;
  byte                 field_117_1;
  byte                 field_118_1;
  byte                 field_119_1;
  byte                 field_120_1;
  byte                 field_121_1;
  byte                 field_122_1;
  byte                 field_123_1;
  byte                 field_124_1;
  byte                 field_125_1;
  byte                 field_126_1;
  byte                 field_127_1;
  byte                 field_128_1;
  byte                 field_129_1;
  byte                 field_130_1;
  byte                 field_131_1;
  byte                 field_132_1;
  byte                 field_133_1;
  byte                 field_134_1;
  byte                 field_135_1;
  uint                 rsvd;
  uint         timelapse_frequency;
  uint         timelapse_period;
  uint         timelapse_rsvd;
  byte                 field_152_1;
  byte                 field_153_1;
  byte                 field_154_1;
  byte                 field_156_1;
  byte                 field_157_1;
  byte                 field_158_1;
  byte                 field_159_1;
  byte                 field_160_1;
  byte                 field_161_1;
  byte                 field_162_1;
  byte                 field_163_1;
  byte                 field_164_1;
  byte                 field_165_1;
  byte                 field_166_1;
  byte                 field_167_1;
  byte                 field_168_1;
  byte                 field_169_1;
  byte                 field_170_1;
  byte                 field_171_1;
  byte                 field_172_1;
  byte                 field_173_1;
  byte                 field_174_1;
  byte                 field_175_1;
  byte                 field_176_1;
  byte                 field_177_1;
  byte                 field_178_1;
  byte                 field_179_1;
  byte                 field_180_1;
  byte                 field_181_1;
  byte                 field_182_1;
  byte                 field_183_1;
  byte                 field_184_1;
  char                 camera_name[11];
  byte                 field_196_1;
  byte                 field_197_1;
  byte                 field_198_1;
  byte                 field_199_1;
  byte                 field_200_1;
  byte                 field_201_1;
  byte                 field_202_1;
  byte                 field_203_1;
  byte                 field_204_1;
  byte                 field_205_1;
  byte                 field_206_1;
  byte                 field_207_1;
  byte                 field_208_1;
  byte                 field_209_1;
  byte                 field_210_1;
  byte                 field_211_1;
  byte                 field_212_1;
  byte                 field_213_1;
  byte                 field_214_1;
  byte                 field_215_1;
  byte                 field_216_1;
  byte                 field_217_1;
  byte                 field_218_1;
  byte                 field_219_1;
  byte                 field_220_1;
  byte                 field_221_1;
  byte                 field_222_1;
  byte                 field_223_1;
  byte                 field_224_1;
  byte                 field_225_1;
  byte                 field_226_1;
  byte                 field_227_1;
  byte                 field_228_1;
  byte                 field_229_1;
  byte                 field_230_1;
  byte                 field_231_1;
  byte                 field_232_1;
  byte                 field_233_1;
  byte                 field_234_1;
  byte                 field_235_1;
  byte                 field_236_1;
  byte                 field_237_1;
  byte                 field_238_1;
  byte                 field_239_1;
  byte                 field_240_1;
  byte                 field_241_1;
  byte                 field_242_1;
  byte                 field_243_1;
  byte                 field_244_1;
  byte                 field_245_1;
  byte                 field_246_1;
  byte                 field_247_1;
  byte                 field_248_1;
  byte                 field_249_1;
  byte                 field_250_1;
  byte                 field_251_1;
  byte                 field_252_1;
  byte                 field_253_1;
  byte                 field_254_1;
  byte                 field_256_1;
  byte                 field_257_1;
  byte                 field_258_1;
  byte                 field_259_1;
  byte                 field_260_1;
  byte                 field_261_1;
  byte                 field_262_1;
  byte                 field_263_1;
  byte                 field_264_1;
  byte                 field_265_1;
  byte                 field_266_1;
  byte                 field_267_1;
  byte                 field_268_1;
  byte                 field_269_1;
  byte                 field_270_1;
  byte                 field_271_1;
  byte                 field_272_1;
  byte                 field_273_1;
  byte                 field_274_1;
  byte                 field_275_1;
  byte                 field_276_1;
  byte                 field_277_1;
  byte                 field_278_1;
  byte                 field_279_1;
  byte                 field_280_1;
  byte                 field_281_1;
  byte                 field_282_1;
  byte                 field_283_1;
  byte                 field_284_1;
  byte                 field_285_1;
  byte                 field_286_1;
  byte                 field_287_1;
  byte                 field_288_1;
  byte                 field_289_1;
  byte                 field_290_1;
  byte                 field_291_1;
  byte                 field_292_1;
  byte                 field_293_1;
  byte                 field_294_1;
  byte                 field_295_1;
  byte                 field_296_1;
  byte                 field_297_1;
  byte                 field_298_1;
  byte                 field_299_1;
  byte                 field_300_1;
  byte                 field_301_1;
  byte                 field_302_1;
  byte                 field_303_1;
  byte                 field_304_1;
  byte                 field_305_1;
  byte                 field_306_1;
  byte                 field_307_1;
  byte                 langauge_id;
  byte                 field_309_1;
  byte                 field_310_1;
  byte                 field_311_1;
  byte                 field_312_1;
  byte                 field_313_1;
  byte                 capture_timer_p;
  byte                 capture_timer_menu_active_p;
  byte                 field_316_1;
  byte                 field_317_1;
  byte                 field_318_1;
  byte                 field_319_1;
  byte                 field_320_1;
  byte                 field_321_1;
  byte                 field_322_1;
  byte                 field_323_1;
  short                signature;
  byte                 field_326_1;
  byte                 field_327_1;
} struct_ColdBinData;
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
typedef struct struct_ColdBinData {
  short                file_length;
  byte                 busy_p;
  byte                 field_03_1;
  struct_short_RTCTime short_RTC_time;
  byte                 field_16_1;
  byte                 field_17_1;
  byte                 field_18_1;
  byte                 field_19_1;
  enum_operation_mode  operation_mode;
  byte                 field_24_1;
  byte                 field_25_1;
  byte                 field_26_1;
  byte                 field_27_1;
  unsigned int         photo_resolution;
  byte                 video_resolution;
  byte                 field_33_1;
  byte                 field_34_1;
  byte                 field_35_1;
  enum_video_length    video_length;
  byte                 field_40_1;
  byte                 field_41_1;
  byte                 field_42_1;
  byte                 field_43_1;
  enum_photo_delay_encoding encoded_photo_delay;
  short                photo_delay_in_seconds;
  byte                 field_50_1;
  byte                 timelapse_file_type;
  unsigned int         burst_size_index;
  enum_cold_item_ir_led_intensity led_power;
  byte                 field_60_1;
  byte                 field_61_1;
  byte                 field_62_1;
  byte                 field_63_1;
  byte                 image_data_strip_p;
  byte                 aperture;
  byte                 external_trigger;
  byte                 date_format;
  unsigned int         temperature_unit_celsius_p;
  byte                 field_72_1;
  byte                 field_73_1;
  byte                 field_74_1;
  byte                 field_75_1;
  unsigned int         pir_range;
  enum_battery_type    battery_type;
  unsigned int         trigger_speed;
  byte                 field_88_1;
  byte                 field_89_1;
  byte                 field_90_1;
  byte                 field_91_1;
  byte                 smart_ir_video_p;
  byte                 sd_management_p;
  byte                 field_94_1;
  byte                 time_format; 
  byte                 field_96_1;
  byte                 field_97_1;
  byte                 field_98_1;
  byte                 field_99_1;
  short                pressure_trend_array[6];
  short                pressure_trend_time;
  byte                 pressure_trend_index;
  byte                 night_mode;
  byte                 field_116_1;
  byte                 field_117_1;
  byte                 field_118_1;
  byte                 field_119_1;
  byte                 field_120_1;
  byte                 field_121_1;
  byte                 field_122_1;
  byte                 field_123_1;
  uint                 sensor_digital_effect;
  byte                 field_128_1;
  byte                 field_129_1;
  byte                 field_130_1;
  byte                 field_131_1;
  byte                 field_132_1;
  byte                 field_133_1;
  byte                 field_134_1;
  byte                 field_135_1;
  unsigned int         rsvd;
  unsigned int         timelapse_frequency;
  unsigned int         timelapse_period;
  unsigned int         timelapse_rsvd;
  byte                 field_152_1;
  byte                 field_153_1;
  byte                 field_154_1;
  byte                 field_155_1;
  byte                 field_156_1;
  byte                 field_157_1;
  byte                 field_158_1;
  byte                 field_159_1;
  byte                 field_160_1;
  byte                 field_161_1;
  byte                 field_162_1;
  byte                 field_163_1;
  uint                 current_tod_in_seconds;
  byte                 field_168_1;
  byte                 field_169_1;
  byte                 field_170_1;
  byte                 field_171_1;
  byte                 field_172_1;
  byte                 field_173_1;
  byte                 field_174_1;
  byte                 field_175_1;
  byte                 field_176_1;
  byte                 field_177_1;
  byte                 field_178_1;
  byte                 field_179_1;
  byte                 field_180_1;
  byte                 field_181_1;
  byte                 field_182_1;
  byte                 field_183_1;
  byte                 field_184_1;
  char                 camera_name[8];
  byte                 field_193_1;
  byte                 field_194_1;
  byte                 field_195_1;
  byte                 field_196_1;
  byte                 field_197_1;
  byte                 field_198_1;
  byte                 field_199_1;
  byte                 field_200_1;
  byte                 field_201_1;
  byte                 field_202_1;
  byte                 field_203_1;
  byte                 field_204_1;
  byte                 field_205_1;
  byte                 field_206_1;
  byte                 field_207_1;
  byte                 field_208_1;
  byte                 field_209_1;
  byte                 field_210_1;
  byte                 field_211_1;
  byte                 field_212_1;
  byte                 field_213_1;
  byte                 field_214_1;
  byte                 field_215_1;
  byte                 field_216_1;
  byte                 field_217_1;
  byte                 field_218_1;
  byte                 field_219_1;
  byte                 field_220_1;
  byte                 field_221_1;
  byte                 field_222_1;
  byte                 field_223_1;
  byte                 field_224_1;
  byte                 field_225_1;
  byte                 field_226_1;
  byte                 field_227_1;
  byte                 field_228_1;
  byte                 field_229_1;
  byte                 field_230_1;
  byte                 field_231_1;
  byte                 field_232_1;
  byte                 field_233_1;
  byte                 field_234_1;
  byte                 field_235_1;
  byte                 field_236_1;
  byte                 field_237_1;
  byte                 field_238_1;
  byte                 field_239_1;
  byte                 field_240_1;
  byte                 field_241_1;
  byte                 field_242_1;
  byte                 field_243_1;
  byte                 field_244_1;
  byte                 field_245_1;
  byte                 field_246_1;
  byte                 field_247_1;
  byte                 field_248_1;
  byte                 field_249_1;
  byte                 field_250_1;
  byte                 field_251_1;
  byte                 field_252_1;
  byte                 field_253_1;
  byte                 field_254_1;
  byte                 field_255_1;
  byte                 field_256_1;
  byte                 field_257_1;
  byte                 field_258_1;
  byte                 field_259_1;
  byte                 field_260_1;
  byte                 field_261_1;
  byte                 field_262_1;
  byte                 field_263_1;
  byte                 field_264_1;
  byte                 field_265_1;
  byte                 field_266_1;
  byte                 field_267_1;
  byte                 field_268_1;
  byte                 field_269_1;
  byte                 field_270_1;
  byte                 field_271_1;
  byte                 field_272_1;
  byte                 field_273_1;
  byte                 field_274_1;
  byte                 field_275_1;
  byte                 field_276_1;
  byte                 field_277_1;
  byte                 field_278_1;
  byte                 field_279_1;
  byte                 field_280_1;
  byte                 field_281_1;
  byte                 field_282_1;
  byte                 field_283_1;
  byte                 field_284_1;
  byte                 field_285_1;
  byte                 field_286_1;
  byte                 field_287_1;
  byte                 field_288_1;
  byte                 field_289_1;
  byte                 field_290_1;
  byte                 field_291_1;
  byte                 field_292_1;
  byte                 field_293_1;
  byte                 field_294_1;
  byte                 field_295_1;
  byte                 field_296_1;
  byte                 field_297_1;
  byte                 field_298_1;
  byte                 field_299_1;
  byte                 field_300_1;
  byte                 field_301_1;
  byte                 field_302_1;
  byte                 field_303_1;
  byte                 field_304_1;
  byte                 field_305_1;
  byte                 field_306_1;
  byte                 field_307_1;
  byte                 language_id;
  byte                 field_309_1;
  byte                 field_310_1;
  byte                 field_311_1;
  byte                 field_312_1;
  byte                 field_313_1;
  byte                 capture_timer_p;
  byte                 capture_timer_menu_active_p;
  byte                 field_316_1;
  byte                 field_317_1;
  byte                 field_318_1;
  byte                 field_319_1;
  byte                 field_320_1;
  byte                 field_321_1;
  byte                 field_322_1;
  byte                 field_323_1;
  byte                 field_324_1;
  byte                 field_325_1;
  byte                 field_326_1;
  byte                 field_327_1;
  short                signature;
  byte                 field_330_1;
  byte                 field_331_1;
} struct_ColdBinData;
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
typedef struct struct_ColdBinData {
  short                file_length;
  byte                 busy_p;
  byte                 field_03_1;
  struct_short_RTCTime short_RTC_time;
  enum_operation_mode  operation_mode;
  unsigned int         photo_resolution;
  byte                 video_resolution;
  byte                 field_25_1;
  byte                 field_26_1;
  byte                 field_27_1;
  enum_video_length    video_length;
  byte                 field_32_1;
  byte                 field_33_1;
  byte                 field_34_1;
  byte                 field_35_1;
  enum_photo_delay_encoding encoded_photo_delay;
  short                photo_delay_in_seconds;
  byte                 field_42_1;
  byte                 timelapse_file_type;
  unsigned int         mult_shot_mode;
  enum_cold_item_ir_led_intensity led_power;
  byte                 field_52_1;
  byte                 field_53_1;
  byte                 field_54_1;
  byte                 field_55_1;
  byte                 image_data_strip_p;
  byte                 aperture;
  byte                 external_trigger;
  byte                 date_format;
  unsigned int         temperature_unit_celsius_p;
  byte                 field_64_1;
  byte                 field_65_1;
  byte                 field_66_1;
  byte                 field_67_1;
  unsigned int         pir_range;
  enum_battery_type    battery_type;
  byte                 trigger_speed;
  byte                 time_format;
  byte                 field_78_1;
  byte                 field_79_1;
  byte                 smart_ir_video_p;
  byte                 sd_management_p;
  short                AEGLib_Params_A;
  short                AELGLib_Params_B;
  short                pressure_trend_array[6];
  short                pressure_trend_time;
  byte                 pressure_trend_index;
  byte                 field_101_1;
  byte                 field_102_1;
  byte                 night_mode;
  byte                 field_104_1;
  byte                 field_105_1;
  byte                 field_106_1;
  byte                 field_107_1;
  byte                 field_108_1;
  byte                 field_109_1;
  byte                 field_110_1;
  byte                 field_111_1;
  byte                 field_112_1;
  byte                 field_113_1;
  byte                 field_114_1;
  byte                 field_115_1;
  byte                 field_116_1;
  byte                 field_117_1;
  byte                 field_118_1;
  byte                 field_119_1;
  byte                 field_120_1;
  byte                 field_121_1;
  byte                 field_122_1;
  byte                 field_123_1;
  unsigned int         rsvd;
  unsigned int         timelapse_frequency;
  unsigned int         timelapse_period;
  unsigned int         timelapse_rsvd;
  byte                 field_140_1;
  byte                 field_141_1;
  byte                 new_timelapse_file_p;
  byte                 field_143_1;
  ushort               tls_jpg_suffix_number;
  char                 camera_name[8];
  byte                 field_154_1;
  byte                 field_155_1;
  byte                 field_156_1;
  byte                 field_157_1;
  byte                 field_158_1;
  byte                 field_159_1;
  byte                 field_160_1;
  byte                 field_161_1;
  byte                 field_162_1;
  byte                 field_163_1;
  byte                 field_164_1;
  byte                 field_165_1;
  byte                 field_166_1;
  byte                 field_167_1;
  byte                 field_168_1;
  byte                 field_169_1;
  byte                 field_170_1;
  byte                 field_171_1;
  byte                 field_172_1;
  byte                 field_173_1;
  byte                 field_174_1;
  byte                 field_175_1;
  byte                 field_176_1;
  byte                 field_177_1;
  byte                 field_178_1;
  byte                 field_179_1;
  byte                 field_180_1;
  byte                 field_181_1;
  byte                 field_182_1;
  byte                 field_183_1;
  byte                 field_184_1;
  byte                 field_185_1;
  byte                 field_186_1;
  byte                 field_187_1;
  byte                 field_188_1;
  byte                 field_189_1;
  byte                 field_190_1;
  byte                 field_191_1;
  byte                 field_192_1;
  byte                 field_193_1;
  byte                 field_194_1;
  byte                 field_195_1;
  byte                 field_196_1;
  byte                 field_197_1;
  byte                 field_198_1;
  byte                 field_199_1;
  byte                 field_200_1;
  byte                 field_201_1;
  byte                 field_202_1;
  byte                 field_203_1;
  byte                 field_204_1;
  byte                 field_205_1;
  byte                 field_206_1;
  byte                 field_207_1;
  byte                 langauge_id;
  byte                 field_209_1;
  byte                 field_210_1;
  byte                 field_211_1;
  byte                 field_212_1;
  byte                 field_213_1;
  byte                 capture_timer_p;
  byte                 capture_timer_menu_active_p;
  byte                 field_216_1;
  byte                 field_217_1;
  byte                 field_218_1;
  byte                 field_219_1;
  byte                 field_220_1;
  byte                 field_221_1;
  byte                 field_222_1;
  byte                 field_223_1;
  byte                 field_224_1;
  byte                 field_225_1;
  byte                 field_226_1;
  byte                 hdr_mode_p;
  byte                 field_228_1;
  byte                 field_229_1;
  byte                 over_temp_p;
  byte                 field_231_1;
  short                signature;
  byte                 field_234_1;
  byte                 field_235_1;
} struct_ColdBinData;
#endif
// External Global Variables

#if (defined BTC_7A_OLD)
// BTC_7A has string constants for menus in the program data segment 
extern char g_SST_ECONOMY_string[sizeof("ECONOMY")];
extern char g_SST_LONG_SP_RANGE_string[sizeof("LONG RANGE")];
extern char g_SST_BLUR_SP_REDUCTION_string[sizeof("BLUR REDUCTION")];
extern char g_SST_SETUP_SP_DATE_SLASH_TIME_string[sizeof("SETUP DATE/TIME")];
extern char g_SST_OPERATION_SP_MODE_string[sizeof("OPERATION MODE")];
extern char g_SST_PHOTO_SP_QUALITY_string[sizeof("PHOTO QUALITY")];
extern char g_SST_VIDEO_SP_LENGTH_string[sizeof("VIDEO LENGTH")];
extern char g_SST_VIDEO_SP_QUALITY_string[sizeof("VIDEO QUALITY")];
extern char g_SST_PHOTO_SP_DELAY_string[sizeof("PHOTO DELAY")];
extern char g_SST_MULTI_SP_SHOT_SP_MODE_string[sizeof("MULTI SHOT MODE")];
extern char g_SST_TEMP_SP_UNIT_string[sizeof("TEMP UNIT")];
extern char g_SST_CAMERA_SP_NAME_string[sizeof("CAMERA NAME")];
extern char g_SST_IMAGE_SP_DATA_SP_STRIP_string[sizeof("IMAGE DATA STRIP")];
extern char g_SST_MOTION_SP_TEST_string[sizeof("MOTION TEST")];
extern char g_SST_MOTION_SP_DETECTION_string[sizeof("MOTION DETECTION")];
extern char g_SST_BATTERY_SP_TYPE_string[sizeof("BATTERY TYPE")];
extern char g_SST_TRIGGER_SP_SPEED_string[sizeof("TRIGGER SPEED")];
extern char g_SST_DEFAULT_SP_SETTINGS_string[sizeof("DEFAULT SETTINGS")];
extern char g_SST_TIMELAPSE_SP_FREQ_string[sizeof("TIMELAPSE FREQ")];
extern char g_SST_TIMELAPSE_SP_PERIOD_string[sizeof("TIMELAPSE PERIOD")];
extern char g_SST_DELETE_SP_ALL_string[sizeof("DELETE ALL")];
extern char g_SST_TV_SP_OUT_string[sizeof("TV OUT")];
extern char g_SST_IR_SP_FLASH_SP_POWER_string[sizeof("IR FLASH POWER")];
extern char g_SST_SMART_SP_IR_SP_VIDEO_string[sizeof("SMART IR VIDEO")];
extern char g_SST_SD_SP_MANAGEMENT_string[sizeof("SD MANAGEMENT")];
extern char g_SST_FW_SP_UPGRADE_string[sizeof("FW UPGRADE")];

extern char g_SST_CAMERA_SP_SETUP_string[sizeof("CAMERA SETUP")];

extern char g_SST_1_SP_SEC_string[sizeof("1 SEC")];
extern char g_SST_5_SP_SECS_string[sizeof("5 SECS")];
extern char g_SST_10_SP_SECS_string[sizeof("10 SECS")];
extern char g_SST_20_SP_SECS_string[sizeof("20 SECS")];
extern char g_SST_30_SP_SECS_string[sizeof("30 SECS")];
extern char g_SST_1_SP_MIN_string[sizeof("1 MIN")];
extern char g_SST_2_SP_MINS_string[sizeof("2 MINS")];
extern char g_SST_5_SP_MINS_string[sizeof("5 MINS")];
extern char g_SST_10_SP_MINS_string[sizeof("10 MINS")];
extern char g_SST_30_SP_MINS_string[sizeof("30 MINS")];
extern char g_SST_60_SP_MINS_string[sizeof("60 MINS")];
extern char g_SST_TIMELAPSE_SP_FREQ_string[sizeof("TIMELAPSE FREQ")];

extern char g_SST_ALL_SP_DAY_string[sizeof("_ALL DAY")];
extern char g_SST_1_SP_HOUR_string[sizeof("1 HOUR")];
extern char g_SST_2_SP_HOURS_string[sizeof("2 HOURS")];
extern char g_SST_3_SP_HOURS_string[sizeof("3 HOURS")];
extern char g_SST_4_SP_HOURS_string[sizeof("4 HOURS")];
extern char g_SST_TIMELAPSE_SP_PERIOD_string[sizeof("TIMELAPSE PERIOD")];
extern char g_SST_CAPTURE_SP_TIMER_string[sizeof("CAPTURE TIMER")];

#endif

extern struct_ColdBinData g_ColdItemData;
extern struct_ColdBinData g_ReferenceColdItemData;
extern byte g_cold_item_signature_valid_p;

extern void * g_sd_card_descriptor;  // this is not really a void*, but I don't understand the data structure well enough to put in here

extern struct_pressure_temperature_coefficients g_pressure_temperature_coefficients;
// Menu Item Arrays
extern struct_hp5_menu_item g_set_date_time_menu[1];
extern struct_hp5_menu_item g_operation_mode_menu[4];
extern struct_hp5_menu_item g_photo_quality_menu[5];
extern struct_hp5_menu_item g_video_length_menu[7];
extern struct_hp5_menu_item g_video_quality_menu[3];
extern struct_hp5_menu_item g_photo_delay_menu[11];
extern struct_hp5_menu_item g_multi_shot_mode_menu[16];
#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
extern struct_hp5_menu_item g_hdr_menu[3];
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
extern struct_hp5_menu_item g_hdr_menu[3];
#endif
extern struct_hp5_menu_item g_temp_unit_menu[3];
extern struct_hp5_menu_item g_camera_name_menu[1];
extern struct_hp5_menu_item g_image_data_strip_menu[3];
extern struct_hp5_menu_item g_motion_test_menu[3];
extern struct_hp5_menu_item g_pir_range_menu[3];

#if (defined BTC_7A_OLD)
extern struct_hp5_menu_item g_battery_type_menu[3];
extern struct_hp5_menu_item g_tv_out_menu[3];
#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
extern struct_hp5_menu_item g_battery_type_menu[3];
#elif (defined BTC_7E_HP4) || (defined BTC_8E_HP4)
extern struct_hp5_menu_item g_battery_type_menu[4];
#elif (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
extern struct_hp5_menu_item g_battery_type_menu[4];
#endif

extern struct_hp5_menu_item g_trigger_speed_menu[3];

// Size of factory menu is only 3 items; but I've expanded it to 5
//      to support custom-settings
extern struct_hp5_menu_item g_restore_default_menu[5];

extern struct_hp5_menu_item g_timelapse_frequency_menu[11]; 
extern struct_hp5_menu_item g_timelapse_period_menu[6];
extern struct_hp5_menu_item g_delete_all_menu[3];
extern struct_hp5_menu_item g_ir_led_power_menu[4];
extern struct_hp5_menu_item g_smart_ir_video_menu[3];
extern struct_hp5_menu_item g_sd_management_menu[3];
extern struct_hp5_menu_item g_language_menu[8];
extern struct_hp5_menu_item g_capture_timer_menu[3];
extern struct_hp5_menu_item g_firmware_upgrade_menu[4];


extern uint                 g_current_on_time_in_seconds;

extern byte g_dcfapi_loaded_p;
extern struct_dcfapi_functions g_active_dcfapi_functions; 

extern struct_short_RTCTime g_set_date_time_menu_state;

// White Flash Unlabeled Data Items
extern byte           g_run_iq_init_function_p;
extern char           g_iq_init_function_param;
extern uint           g_iq_init_color_param;

extern struct_menu_root                    *g_menu_root;
extern struct_menu_selections_descriptor    g_camera_setup_menu_item_array[26];
extern void        (*g_HceTaskMenuMultiItem_fsm_function_array[32])();

extern char         s_Digital_Effect_BW_803abe48;

extern byte         g_night_mode_p;
extern byte         g_photo_sensor_night_mode_p;
extern byte         g_photo_mode_p;
extern byte         g_up_button_enable;
extern byte         g_down_button_enable;
extern byte         g_left_button_enable;
extern byte         g_right_button_enable;
extern byte         g_enter_button_enable;
extern byte         g_mode_button_enable;

extern byte         g_sensor_config_table_A[4];
extern byte         g_sensor_config_table_B[4];


extern struct_photo_dimensions_short g_image_resolution_lookup_table[4];

extern int          g_SPL06_007_compensation_scale_table[8];

extern byte         g_set_time_buffer[10];

extern short        g_temp_am_pm_p;

extern short        g_timelapse_frequency_lookup_table[11];
extern struct_hp5_menu_item g_timelapse_frequency_menu[11];
extern struct_hp5_menu_item g_timelapse_period_menu[6];

extern byte         g_new_check_night_mode_p;
extern byte         g_photo_detector_hysteresis;
extern uint         g_photo_sensor_value;

extern byte         g_wakeup_alarm_mask_A;
extern byte         g_wakeup_alarm_mask_B;

extern uint         g_image_size;


extern enum_alt_ir_led_intensity g_ir_led_power_alt_encoding;

extern byte          g_ir_led_intensity_set_p;

// External Functions
// These were once arranged in alphabetical order, but they are higgly piggly now

// Threadx

extern uint          tx_queue_send(void *queue, void *message, int option);

// event_loop_iterator
extern void          event_loop_iterator(uint event_number,uint qualifier);
extern void          event_descriptor_init(struct_event_descriptor *event_descriptor);
extern int           get_matching_event_descriptor(int event_number,struct_event_descriptor *event_descriptor);
extern void          set_g_evt_0x52510507_state_initialized_p(byte param_1);
extern int           get_g_evt_0x52510507_counter(void);
extern void          set_g_evt_0x52510507_counter(int param_1);
extern void          set_sd_card_state_w_init(uint param_1);
extern byte          get_g_sd_card_valid_p();
extern void          set_g_sd_card_state_valid_p(byte param_1);
extern void          initialize_g_mode_change_counter(byte param_1);
extern void          service_button_event(int param_1,uint param_2);
extern void          host_task_init(void);
extern byte          get_g_test_mode(void);
extern int           get_g_sd_card_mounted_p(void);
extern void          set_g_sd_card_mounted_p(byte param_1);
extern void          serviceEvent_0x5151000(int param_1,int param_2);
extern void          service_event_0x5851000(int qualifier);
extern void          set_g_evt_0x52510507_state_initialized_p(byte param_1);
extern int           get_g_evt_0x5251050a_counter(void);
extern void          set_g_evt_0x5251050a_counter(int param_1);
extern void          setStillCapDone(void);
extern void          serviceSetCurrentMode_event(int param_1,int param_2);
extern void          set_g_info_strip_enabled_p(byte param_1);
extern void          set_fast_cap_mount_active_p(byte param_1);
extern byte          get_g_fast_cap_mount_active_p(void);
extern bool          vfs_unmount_wrapper2(int param_1);
extern void          set_g_some_sd_status_p(byte param_1);
extern void          app_init_directory_suffix_file_prefix(void);
extern void          fsm_iterate_all_in_g_fsm_descriptor_list(void);

extern struct_event_descriptor g_event_descriptor;

// Digi Pyro Related Routines
extern void          DigiPIRSpi_Write(uint csr_value);
extern void          digi_pir_spi_serial_out(int param_1);
extern void          some_sort_of_delay(uint param_1);
extern int           get_fine_grained_time(void);

// string constants
extern char*        s_FastCap_CST_MSG_ID_MOUNT_FINISH_e_8036c7c4;


extern int           appAWBALGLib_WBParamSet(uint param_1, uint param_2);

extern void *        bSet(void * base, uint value, uint num_bytes);
extern int           btc_fclose(uint file_ptr);
extern uint          btc_fopen(char* filename, uint flags);
extern uint          btc_fread(uint file_ptr, void * buffer, uint size);
extern uint          btc_fwrite(uint file_ptr, void *buffer, uint size);

extern void *        btc_malloc(uint size);
extern void *        malloc_3(uint size);

extern void          btc_init_directory_suffix_file_prefix(void);

extern void          init_directory_suffix_file_prefix(char* directory_suffix, char *file_prefix,
						       uint param3);

extern void          init_IR_LED(void);

extern bool          checkForSDCard();
extern int           check_event_0x58510000_qualifier1(uint qualifier1);
extern void          check_event_null_function(int, int);
extern void          check_post_printf_state_set_sio_params();
extern void          check_remaining_sd_capacity(void);
extern int           check_hal_low_voltage(void); 

extern bool          cold_item_led_power_blur_reduction_p();
extern uint          debug_printf(char *);
extern void          debug_print_string(uint, char *, ...);
extern void          dispatch_IQ_function(int, uint, uint, ...);
extern void          draw_jpg_on_screen(uint index);
extern void          draw_rectangle_wrapper(uint right_x,
					    uint bottom_y,
					    uint width,
					    uint height,
					    char color);

extern void          draw_set_time_screen(uint selected_item);
extern void          draw_video_scroll_bar(uint percent_complete);
extern void          draw_sst_string_on_display (int param_1,int param_2,void *param_3,int *param_4,int param_5,char *format_string,
						 int param_7,int param_8);


extern uint          encoded_timelapse_frequency_to_seconds(uint);
extern bool          fatVolLabSet(char *drive_letter,char *volume_name);
extern bool          fatVolLabSet_wrapper(char* drive_letter, char* volume_name);

extern void          free(void *ptr);
extern void          free_fsm_descriptor_on_error(void * iterator_function);

extern int           fsize(uint file_ptr);

extern uint          fsm_getCurrentState(void);
extern byte          fsm_getNextState(void);
extern int           fsm_get_valid(void *fsm_function);
extern void          fsm_setCurrentState(byte state);
extern  int          fsm_spawn(byte allocate_p,void *iterator_function,uint param_3,uint param_4,uint param_5, void *memory);

extern void          set_fsm_state_absolute(int);
extern void          set_fsm_state_relative(int);

extern void          setSensor_configA(unsigned char);
extern void          setSensor_configB(unsigned char);

#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E)
extern void           set_some_sd_global(uint);
#endif

extern bool          execute_if_not_null(void *function_ptr);
extern void          exif_remove_and_add_wrapper(int param_1);

extern struct struct_CameraConfig *getCameraConfigStructPtr(void);
extern int           getMCURegisterByte(uint param_1,byte *data);
extern int           MPUSpi_WriteNPacketByManualPWM(byte *address,byte *data,uint num_bytes);
extern void          MCU_SPI_mutex_get(uint wait_option);
extern void          MCU_Read_waiting_on_some_event(void);
extern void          MCU_SPI_mutex_put(void);

extern struct_menu_selections_descriptor *getCurrentMenuCollectionAndSize(struct_menu_selections_descriptor *menu_selections,struct_menu_root **menu_root);

extern enum_cold_item_ir_led_intensity get_extra_rtc_alt_ir_led_intensity();

extern void          get_capture_timer_rtc_time(struct_short_RTCTime *short_rtc_time);

extern uint          get_some_system_time(int qualifier,uint *time);
extern uint          get_SDCardState();


extern uint          getCountdownDelay();
extern uint          get_mcu_csr();
extern uint          get_g_timelapse_wakeup_time_qualifier();
extern void          get_multi_shot_photo_dimensions(struct_photo_dimensions_int *);
extern void          mcu_rtc_test();
extern void          set_mcu_pir_pin(uint);
extern void          set_g_reset_pir_trigger_count(uint);
extern void          MCUApp_ForcePIROutputHigh();
extern void          set_some_mcu_pir_reset_value(uint);
extern void          check_mcu_register_10(uint, uint);
extern void          check_mcu_register_12(uint);
extern void          check_mcu_register_25(uint, uint);
extern void          set_mcu_wakeup_mask(uint);
extern void          set_mcu_wakeup_time(uint);
extern void          set_mcu_register_masks(uint);
extern void          write_wakeup_4_spi();
extern void          set_wakeup_alarms();
extern bool          HceTaskMount_FSM_valid_p(void);
extern bool          HceTaskStillBurstFSM_valid_p(void);
extern bool          HceTaskRecording_FSM_valid_p(void);
extern bool          checkHceTaskTimeLapse_valid(void);
extern byte          get_menu_button_enable(uint button_index);
extern bool          check_sd_capacity_to_complete_burst(void);
extern void          ModeAuto_DoCaptureEvent(int param_1);
extern void          register_Timelapse_completion_function(void *completion_function);
extern void          startHceWaitTimeLapse_FSM(byte param_1);
extern void          ModeAuto2_FSM_Task11(void);
extern byte          g_mcu_reboot_on_power_switch;
extern byte          g_mcu_ver;
extern byte          g_mcu_sub_ver;



extern void          get_cold_item_camera_name(char * camera_name);
extern byte          get_cold_item_capture_timer_p(void);
extern byte          get_cold_item_sd_management_p();
extern uint          get_g_low_battery_off_1();
extern enum_battery_type  get_g_cold_item_battery_type(void);
extern uint          get_g_current_MCU(void);
extern uint          get_g_sio_params_set(void);
extern void          set_sio_params(uint);
extern uint          disable_hang_reboot(void);
extern void          Read_MCU_Ver(uint);
extern void          Read_MCU_SubVer(uint);
extern char          get_cold_item_sensor_digital_effect(void);
extern uint          get_cold_item_timelapse_frequency(void);
extern uint          get_cold_item_tod_last_photo_in_seconds(void);
extern enum_timelapse_period_encoding get_cold_item_timelapse_period(void);
extern uint          get_cold_item_photo_resolution(void);
extern enum_multi_shot_encoding get_cold_item_multi_shot_encoding(void);

extern uint          get_battery_percent();
extern uint          get_battery_percent_from_voltage(uint voltage);
extern ushort        get_battery_voltage_x100();
extern byte          get_create_command_thread_p();
extern void          get_current_date_time_short(struct_short_RTCTime *return_date_time);
extern uint  get_current_operating_time_ms(void);
extern void          get_directory_suffix_image_prefix(char *directory_suffix, char *image_prefix);
extern void          get_directory_suffix_image_prefix_indirect(char *directory_suffix, char *image_prefix);

extern struct_system_device_entry *get_system_device_entry(uint dev_id);
//extern int           getHceTaskMenuMultiItem2_FSM_valid(void);
extern ushort        get_g_cold_item_video_duration(void);
extern int           get_g_cold_item_led_power(void);
extern uint          get_cold_item_temperature_unit_celsius_p(void);
extern byte          get_cold_item_info_strip_enable_p(void);
extern uint          get_g_menu_temp_minute(void);
extern uint          get_g_menu_temp_hour(void);
extern uint          get_g_menu_temp_month(void);
extern uint          get_g_menu_temp_year(void);
extern uint          get_am_pm_current_value(void);
extern uint          get_am_pm_max_value(void);
extern uint          get_am_pm_min_value(void);
extern uint          get_max_minute(void);
extern uint          get_min_minute(void);
extern uint          get_max_hour(void);
extern uint          get_min_hour(void);
extern uint          get_max_day(void);
extern uint          get_min_day(void);
extern uint          get_max_month(void);
extern uint          get_min_month(void);
extern uint          get_max_year(void);
extern uint          get_min_year(void);
extern uint          get_g_temp_day_number(void);

extern ushort        get_g_timelapse_wakeup_time();

extern ushort        get_photo_size_factor(int table_index);

extern byte          get_g_night_mode_p(void);
extern int           get_g_temperature_value(void);
extern byte          get_DAT_80357b60_at_global_index(void);
extern uint          get_cold_item_operation_mode(void);
extern void          get_cold_item_short_rtc_time(struct_short_RTCTime *short_rtc_time);
extern int           get_power_supply_mode(void);
extern uint          get_power_switch_on_p();
extern void          get_rtc_extra_byte_range(byte *buffer, uint start_byte, uint size);          
extern byte          get_rtc_extra_operation_mode(void);
extern void          get_rtc_time_or_alarm(int flag, struct_RTCTime *current_rtc_time);
extern void          get_rtc_time(struct_RTCTime *current_rtc_time);
extern void          get_short_rtc_time(struct_short_RTCTime *short_rtc_time);
extern int           get_temperatureForC(void); // this version actually reads the register
extern enum_tod_in_timelapse get_tod_in_timelapse_region(struct_short_RTCTime *short_rtc_time);
extern uint  get_unix_time(uint ms_date_time, struct_DateTime *expanded_date_time);
extern short         get_current_video_duration_in_seconds(void);
extern unsigned long long get_64_bit_date_time_in_seconds(struct_DateTime *current_date_time);

extern uint          get_VideoFormatStructure(int param_1, void* unknown_structure_pointer);

extern bool          get_within_operating_hours_p();


extern void          get_dir_image_indices(uint *,uint *);
extern void          set_dir_image_indices(uint ,uint );

extern bool          get_device_csr_bit(uint, uint, void*);
extern void          hal_set_rtc(struct_short_RTCTime *short_rtc_time);
extern void          hal_IRLedOff(void);
extern void          hal_IRLedOff_pre_work(void);
extern void          HceCommon_InitOptions();
extern void          HceCommon_SetCaptureImag(uint param_1,char *param_2);
extern void          HceCommon_RestoreDefaultColdItem(char preserve_rtc_p);

extern bool          HceIQ_CheckNightMode(void);
extern void          HceIQ_PowerOnStateInit();
extern void          HceIRCut_SetIRCutClosed(void);
extern void          HceIRCut_SetIRCutOpen(void);
extern int           HceStampLoadFont(uint font_id,
				      ushort *large_width, ushort *large_height,
				      ushort *small_width, ushort *small_height,
				      uint font_scale);

extern void          HceStampDrawLogo(struct_video_page_descriptor *video_page_desciptor, 
				      uint font_scale);

extern uint          HceTask_ToNextNChar(int up_button_p,
					 uint (*current_value_function)(), 
					 uint (*min_value_function)(), 
					 uint (*max_value_function)(),
					 ushort some_value);
extern void          HceTaskBoot2Cap_Task0();
extern void          HceTaskUnMount_fsm_iterator(void);
extern void          HceTaskFormat_fsm_iterator(void);
extern void          HceTaskFormat_task0(void);
extern void          HceTaskFormat_task1_Mount(void);
extern void          HceTaskFormat_task2_mount_complete(void);
extern void          HceTaskFormat_task3_format_drive(void);
extern void          HceTaskFormat_task4_Init_DCF(void);
extern void          HceTaskFormat_task5(void);
extern void          HceTaskFormat_task6(void);
extern bool          HceTaskStillFSM_valid_p();
extern void          used_jfif_function(void);
extern void          hijacked_digital_zoom_function(void);
extern void          initCodeSentry(uint);
extern void          IRLedOff(void);
extern void          setIRLedOn(void);
extern void          set_IRLedOn_PwrLvl(uint ir_led_intensity);
extern void          set_ir_led_intensity_from_cold_item(uint cold_led_power);
extern bool          set_pwm_device_percent(uint device_id, uint denominator_divisor, uint percent);

extern int           icatch_isp_load_firmware(void);
extern bool          initSmartIRQueueThread(void);

extern void          PV_RAW_ImageWrite(int param_1,char *param_2);
extern uint          get_next_state_from_menu_enter(uint param_1,struct_hp5_menu_item *param_2 ,uint param_3, struct_menu_root **param_4);
extern int           get_next_wake_time(struct_short_RTCTime *short_rtc_time, enum_tod_in_timelapse timelapse_region);

extern  void         load_boot_parameters();
extern int           local_sprintf(char*, char*, ...);
extern void          log_printf(uint, char *, ...);


extern uint          MakeShortNameByLongName(char *, int *, char *, char *);        
extern void *        memcpy(void *__dest,void *__src,uint __n); // don't change the name -- C needs this
                                                                // just the way it is

extern void*         memoryAllocate(uint size);

extern void          menu_draw_selected_item(byte *menu_selection,struct_menu_root **menu_descriptor);
extern void          menu_get_current_menu_selection(char param_1,byte *param_2,char param_3,struct_menu_root **param_4);
extern byte          menu_get_current_selection(struct_menu_root **root_menu_descriptor);
extern void          menu_get_next_menu_selection(byte menu_selection,
						       byte *next_menu_selection,byte menu_wrap,
						       struct_menu_root **menu_descriptor);
extern uint          get_next_state_from_menu_mode(byte num_levels,struct_menu_root **current_menu_descriptor);
extern void          menu_pop_current_menu(void *menu_selection, struct_menu_root **menu_descriptor);
extern void          menu_redraw_items(uint menu_selection,struct_menu_root **menu_descriptor);


extern void          noop_function(void);

extern byte          photo_sensor_hysteresis(void);

extern uint          positive_diff(uint end_time_ms, uint start_time_ms);
extern int           posix_fileinfo(char * filename, struct_PosixFinfo *finfo);
extern void          power_on_IR_LED(void);

extern uint          read_photo_sensor_value();
extern int           read_pressure_temperature_device(byte *, byte);
extern int           read_sd_blocks(uint dev_id,uint current_sector,uint operation_size, byte *buffer);
extern bool          reset_capture_timer(uint start_hour_minute, uint end_hour_minute);
extern int           seekToSpecifiedFileLocation(uint file_ptr, uint file_mode, uint offset, uint whence, uint);

extern void          register_low_battery_display_function(void (*func)(int));
extern void          still_low_battery_display_function(int);

#if (defined BTC_8E) || (defined BTC_8E_HP4) || (defined BTC_8E_HP5)
extern int           Pressure_sensor_getReading(int *pressure,int *temperature);
#elif (defined BTC_7A) || (defined BTC_7E) || (defined BTC_7E_HP4) || (defined BTC_7E_HP5)
extern int           temperature_sensor_getReading(void);
extern void          set_g_temperature_forc(int temperature);
#endif

extern int           set_aaa_ae_pipeline_wrapper(int param_1);
extern int           set_aaa_awb_pipeline_wrapper(int param_1);

extern void          setBatteryCalibConfig(void);

extern void          setCodeSentryCSR(int address,int flag);
extern void          setCodeSentryAddressRegion(int filter_index,int dev_type,void *base,void *bounds);

extern void          setSensorDigitalEffectPhoto(byte night_p);
extern void          setSensorDigitalEffectVideo(byte night_p);

extern void          set_exif_time_of_capture(struct_short_RTCTime *);
extern void          set_rtc_extra_current_tod_in_seconds(int);
extern void          set_cold_item_current_tod_in_seconds(int);
extern void          set_cold_item_timelapse_new_file_p(byte param_1);

extern int           sdRead(void *param_1,uint start_block,uint num_blocks,byte *buffer);
extern int           RdSdAddr(void *param_1,uint start_block,uint num_blocks,byte *buffer);
extern int           sdWrite(void *param_1,uint start_block,uint num_blocks,byte *buffer);
extern int           WrSdAddr(void *param_1,uint start_block,uint num_blocks,byte *buffer);
extern void          HceFastboot_SDPwrRecycle(void);
extern int           initialize_sd_card_to_data(uint device_id);
extern bool          initialize_default_sd_card_to_data(void);
extern int           reduce_SD_clock(void*);
extern void          put_fmDma1_semaphore(void);
extern void          get_fmDma1_semaphore(void);
extern void          flush_processor_cache(byte *buffer,uint size);
extern void          flush_processor_cache2(byte *buffer,uint size);
extern uint          get_sd_clock_kHz(void);

extern void          set_cold_item_led_power(uint);
extern int           set_cold_item_language_id(byte param_1);
extern void          set_cold_item_new_timelapse_file_p(byte);
extern void          set_cold_item_137_1(byte param_1);
extern void          set_g_ae_parameter(byte ae_parameter);
extern void          set_g_cold_item_battery_type(uint battery_type);
extern void          set_cold_item_pir_range(enum_pir_range_options pir_range_option);
extern void          set_cold_item_sd_management_p(byte param_1);
extern void          set_cold_item_overtemp_p(void);
extern void          set_pir_sensor_range(enum_pir_range_options pir_range_option);
extern void          set_pre_printf_state(void);

extern void          set_ir_led_power_pwm(enum_alt_ir_led_intensity);
extern void          set_ir_led_intensity_from_cold_item(enum_cold_item_ir_led_intensity ir_led_intensity);
extern void          set_rtc_extra_byte_range(byte *buffer, uint start_byte, uint size);
extern void          set_rtc_extra_operation_mode(byte);

extern void          set_g_flash_on_check_battery(int);
extern void          set_sd_iface_clock(uint);

extern struct_photo_dimensions_int *get_camera_photo_resolution(struct_photo_dimensions_int *param_1,int encoded_photo_resolution);


extern void          smart_IR_log_printf(char * format_string, uint arg1);
extern void          smart_IR_log_sub_printf(char *format_string, uint arg1);
extern int           snapYuv2ExifJpgWrite (void *image_descriptor,uint jpg_width,uint jpg_height,
					   char *filename,uint param_5,uint param_6);
extern void          sp5kIqBlockEnable(char, ...);
extern void          sp5kIqCfgSet(uint, uint);
extern int           sp5kModeSet(int next_mode);

extern void          spawnIRCutFSM_per_mode();
extern void          IRCutThreadCreate(uint value);

extern void          startHceTaskUnMount_FSM(uint param_1,uint param_2);
extern void          startHceTaskFormat_FSM(int param_1, uint param_2);
extern void          store_pressure_trend(void);

extern void          startHceTaskStill_FSM(uint burst_size,ushort size_factor,uint width,uint height,uint param_5,uint param_6,
					   byte trigger_delay);

extern void          TaskTimeLapseFSM_task11_openTLfile();

extern uint          btc_strlen(char* string);
extern char *        btc_strcpy(char *dest, char *source);

extern void          function_with_syscall_zero(char *sys_file, uint line_number,int param_3);

extern int           thread_sleep(enum_timer_wait_scale , uint);
extern void          tty_printf(char *, ...);
extern void          tty_printf_battery_stats();

extern bool          ui_cursor_key_pressed_p(enum_ui_cursor_button button_code);

extern void          update_current_MCU(uint);
extern void          update_timelapse_sunset(int *pre_sunset_start_time_in_minutes,uint *sunset_time_in_minutes);
extern void          update_timelapse_sunrise(int *sunrise_time_in_minutes,int *post_sunrise_time_in_minutes);

extern void          update_global_pressure_temperature();
extern void          update_timelapse_rise_set_times();
extern void          update_time_field(byte right_p,byte *menu_selection,byte one,byte *buffer,byte menu_fields);
extern void          store_pressure_trend();

extern uint          vfsClose(uint file_ptr);
extern uint          vfsFileCTimeGet(uint file_ptr, uint *ms_like_modified_date_time, uint *ms_like_created_date_time);
extern uint          vfsOpen(char *filename, uint flags);
extern uint          vfsFileSizeGet(uint file_ptr);
extern void          vfsFileDel(char *filename);
extern void          vfsFileCopy(char *source_filename, char *dest_filename);

extern void          Volt_Calib_Bat(void);

extern int           write_sd_blocks(uint dev_id,uint current_sector,uint operation_size, byte *buffer);
extern int           Write_LEDOn();
extern int           Write_LEDOff();

extern int           WrappedMPUSpi_WriteNPacketByManualPWM(byte *data0, byte *data1, uint num_bytes);


// Menu Constructors
// uint build_root_menu (byte initial_selection, byte next_selection,
//		      struct_menu_root **arg_root_menu_descriptor,
//		      struct_menu_item_collection_4 *menu_item_collection,
//		      int num_items_and_title,
//		      char *menu_item_name);

// Menu functions


extern void build_main_menu();


extern void tmmi2_set_initial_menu_state();
extern void handleInit_menu();
extern void handle_splash_screen_menu();
extern void handle_home_screen_menu();
extern void handleCameraSetup_menu();
extern void handlePlayback_menu();
extern void handleSetTimeMenu();
extern void handleOperationMode_menu();
extern void handlePhotoQuality_menu();
extern void handleVideoLength_menu();
extern void handleVideoQuality_menu();
extern void handlePhotoDelay_menu();
extern void handleMultiShotMode_menu();
extern void handleTempUnit_menu();
extern void handleCameraName_menu();
#if (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
extern void handleHDR_menu();
#endif
extern void handleImageDataStrip_menu();
extern void handleMotionTest_menu();
extern void handlePIRRange_menu();
extern void handleBatteryType_menu();
extern void handleTriggerSpeed_menu();
extern void handleRestoreDefault_menu();
extern void handleTimelapseFreq_menu();
extern void handleTimelapsePeriod_menu();
extern void handleDeleteAll_menu();
extern void handleEraseSDCard_menu();
extern void handleLanguage_menu();
extern void handleIRLedPower_menu();
extern void handleCaptureTimerP_menu();
extern void handleSetCaptureTimerP_menu();
extern void handleSmartIRVideo_menu();
extern void handleSDManagement_menu();
extern void handleFirmwareUpgrade_menu();
extern void tmmi2_final_state();


extern void handleCommitUpdates_menu();
