// 
// BTC.h
// Structures, typedefs, and function prototypes found
// in the binary (as reflected by Ghidra).

// Imported (manually) from Ghidra
// 

typedef unsigned char    bool;
typedef unsigned char    byte;
typedef unsigned int     uint;

// Enums w/ typedefs

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

typedef enum enum_battery_type {
  lithium = 0,
  alkaline = 1
} enum_battery_type;


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


typedef enum enum_menu_selection_action {
  not_known = 0,
  back_to_parent = 1,
  new_child = 2
} enum_menu_selection_action;


typedef enum enum_cold_item_ir_led_intensity {
  economy = 0,
  long_range,
  blur_reduction
} enum_cold_item_ir_led_intensity;

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

// Structures w/ typedefs


// Menu-related structures


typedef struct struct_hp5_menu_item {
  enum_jpg_icon_index   icon_index;
  uint   text_id;
  uint   foreground_color;
  uint   background_color;
  enum_menu_selection_action menu_selection_action;
  uint   return_state_id;
  uint   next_state_id;
} struct_hp5_menu_item;


typedef struct struct_menu_selections_descriptor {
  struct_hp5_menu_item  *menu_item_array;
  unsigned int  num_array_entries;
} struct_menu_selections_descriptor;


typedef struct struct_menu_root {
  byte current_selection;
  byte next_selection;
  byte field_0x2;
  byte field_0x3;
  struct_hp5_menu_item *menu_item_array;
  unsigned int num_items_and_title;
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

typedef struct struct_mpu_spi_data {
  byte data0;
  byte data1;
  byte data2;
} struct_mpu_spi_data;

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

typedef struct struct_DateTime {
  unsigned int second;
  unsigned int minute;
  unsigned int hour;
  unsigned int day;
  unsigned int month;
  unsigned int year;
  unsigned int unknown1;
  unsigned int unknown2;
  int flag;
} struct_DateTime;


// Camera config -- go-to structure with everything but the kitchen sink

typedef struct struct_CameraConfig {
  char exit_menu_p_or_ir_led_on;
  char field_1;
  char menu_selection_1;
  char menu_selection_2;
  // a bunch of unknown ints
  char commit_menu_change;
  char unknown_char_5;
  char field_6;
  char unknown_char_7;
  unsigned int unknown_uint_8;
  unsigned int unknown_uint_12;
  unsigned int unknown_uint_16;
  unsigned int unknown_uint_20;
  unsigned int unknown_uint_24;
  unsigned int unknown_uint_28;
  char unknown_byte_32;
  char still_flash_on;
  char unknown_byte_34;
  char unknown_byte_35;
  unsigned int unknown_uint_36;
  unsigned int unknown_uint_40;
  unsigned int unknown_uint_44;
  unsigned int unknown_uint_48;
  unsigned int unknown_uint_52;
  unsigned int unknown_uint_56;
  unsigned int unknown_uint_60;
  unsigned int unknown_uint_64;
  unsigned int still_led_turned_on_time_us;
  unsigned int unknown_uint_72;
  int total_images;
  int current_image;
  char current_filename[200];
} struct_CameraConfig;

typedef struct struct_PosixFinfo {
  char filename[512];
  char backup_filename[512];
  unsigned int field_1024;
  unsigned int field_1028;
  unsigned int file_mode;
  unsigned int field_1036;
  unsigned int field_1040;
  unsigned int field_1044;
  unsigned int field_1048;
  unsigned int field_1052;
  unsigned int file_size_low;
  unsigned int file_size_high;
  unsigned int date_only_created_time;
  unsigned int some_time;
  unsigned int created_time;
  unsigned int attributes;
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
typedef struct struct_ColdBinData {
  short                file_length;
  short                field_02_2;
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
  byte                 field_43_1;
  unsigned int         mult_shot_mode;
  enum_cold_item_ir_led_intensity led_power;
  byte                 field_52_1;
  byte                 field_53_1;
  byte                 field_54_1;
  byte                 field_55_1;
  byte                 image_data_strip_p;
  byte                 field_57_1;
  byte                 field_58_1;
  byte                 field_59_1;
  unsigned int         temperature_unit_celsius_p;
  byte                 field_64_1;
  byte                 field_65_1;
  byte                 field_66_1;
  byte                 field_67_1;
  unsigned int         pir_range;
  enum_battery_type    battery_type;
  unsigned int         trigger_speed;
  byte                 smart_ir_video_p;
  byte                 sd_management_p;
  byte                 field_82_1;
  byte                 field_83_1;
  short                AELGLib_Params;
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
  byte                 field_124_1;
  byte                 field_125_1;
  byte                 field_126_1;
  byte                 field_127_1;
  unsigned int         timelapse_frequency;
  unsigned int         timelapse_period;
  byte                 field_136_1;
  byte                 field_137_1;
  byte                 field_138_1;
  byte                 field_139_1;
  byte                 field_140_1;
  byte                 field_141_1;
  byte                 field_142_1;
  byte                 field_143_1;
  byte                 field_144_1;
  byte                 field_145_1;
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

// External Global Variables

extern struct_ColdBinData g_ColdItemData;

// Menu Item Arrays
extern struct_hp5_menu_item g_set_date_time_menu[1];
extern struct_hp5_menu_item g_operation_mode_menu[4];
extern struct_hp5_menu_item g_photo_quality_menu[5];
extern struct_hp5_menu_item g_video_length_menu[7];
extern struct_hp5_menu_item g_video_quality_menu[3];
extern struct_hp5_menu_item g_photo_delay_menu[11];
extern struct_hp5_menu_item g_multi_shot_mode_menu[16];
extern struct_hp5_menu_item g_hdr_menu[3];
extern struct_hp5_menu_item g_temp_unit_menu[3];
extern struct_hp5_menu_item g_camera_name_menu[1];
extern struct_hp5_menu_item g_image_data_strip_menu[3];
extern struct_hp5_menu_item g_motion_test_menu[3];
extern struct_hp5_menu_item g_pir_range_menu[3];
extern struct_hp5_menu_item g_battery_type_menu[4];
extern struct_hp5_menu_item g_trigger_speed_menu[3];
extern struct_hp5_menu_item g_restore_default_menu[3];
extern struct_hp5_menu_item g_timelapse_frequency_menu[11]; 
extern struct_hp5_menu_item g_timelapse_period_menu[6];
extern struct_hp5_menu_item g_delete_all_menu[3];
extern struct_hp5_menu_item g_ir_led_power_menu[4];
extern struct_hp5_menu_item g_smart_ir_video_menu[3];
extern struct_hp5_menu_item g_sd_management_menu[3];
extern struct_hp5_menu_item g_language_menu[8];
extern struct_hp5_menu_item g_capture_timer_menu[3];
extern struct_hp5_menu_item g_firmware_upgrade_menu[4];


extern byte g_dcfapi_loaded_p;


//extern uint         DAT_803733d8;

extern uint         DAT_80000370;
extern uint         DAT_800006c0;
extern uint         DAT_8036fe00;

extern void *       DAT_80373d3c;


extern char         DAT_8034e820;

extern char         DAT_8034e821;

extern uint         DAT_80313770;
extern uint         DAT_8043997c;

extern struct_menu_root                    *g_menu_root;
extern struct_menu_selections_descriptor    g_camera_setup_menu_item_array[26];
extern void        (*g_HceTaskMenuMultiItem_fsm_function_array[32])();

extern char         s_Digital_Effect_BW_803abe48;

extern uint         g_night_mode_p;
extern char         g_photo_mode_p;
extern byte         g_up_button_enable;
extern byte         g_down_button_enable;
extern byte         g_left_button_enable;
extern byte         g_right_button_enable;
extern byte         g_enter_button_enable;
extern byte         g_mode_button_enable;

extern byte         g_sensor_config_table_A[4];
extern byte         g_sensor_config_table_B[4];

extern void *       PTR_DAT_80373d38;
extern void         (*g_btc_init_directory_suffix_prefix_dyn)(char *, char*, unsigned int);


extern enum_alt_ir_led_intensity g_ir_led_power_alt_encoding;

// External Functions
// These are arranged in alphabetical order, for now

extern int           appAWBALGLib_WBParamSet(uint param_1, uint param_2);

extern void *        bSet(void * base, uint value, uint num_bytes);
extern int           btc_fclose(unsigned int file_ptr);
extern unsigned int  btc_fopen(char* filename, unsigned int flags);
extern unsigned int  btc_fread(unsigned int file_ptr, void * buffer, unsigned int size);
extern unsigned int  btc_fwrite(unsigned int file_ptr, void *buffer, unsigned int size);

extern void *        btc_malloc(unsigned int size);

extern void          btc_init_directory_suffix_file_prefix(void);
extern void          init_directory_suffix_file_prefix(char* directory_suffix, char *file_prefix,
						       unsigned int param3);

extern int           check_event_0x58510000_qualifier1(uint qualifier1);
extern void          check_post_printf_state_set_sio_params();
extern void          check_remaining_sd_capacity(void);

extern unsigned int  debug_printf(char *);
extern void          debug_print_string(uint, char *);
extern void          dispatch_IQ_function(int, uint, uint, ...);
extern void          draw_rectangle_wrapper(unsigned int right_x,
					    unsigned int bottom_y,
					    unsigned int width,
					    unsigned int height,
					    char color);

extern void          draw_video_scroll_bar(unsigned int percent_complete);

extern bool          fatVolLabSet(char *drive_letter,char *volume_name);
extern bool          fatVolLabSet_wrapper(char* drive_letter, char* volume_name);

extern void          free(void *ptr);
extern void          free_fsm_descriptor_on_error(void * iterator_function);

extern uint          fsm_getCurrentState(void);
extern byte          fsm_getNextState(void);
extern int           fsm_get_valid(void *fsm_function);
extern uint          fsm_setNextStateRelative(uint); 
extern uint          fsm_set_next_state(uint param_1);
extern void          fsm_setCurrentState(byte state);
extern int           fsm_spawn(byte initialize_fsm_p,void *fsm_iterator_function,uint ref_count,uint fsm_active,
			       uint param_5);


//extern uint          FUN_8000a508(void);
//extern int           FUN_800c0004(int param_1,int param_2,int param_3);
//extern int           FUN_800d0ba0(unsigned char);
extern void          FUN_80136a94(unsigned char);
extern void          FUN_80136ae0(unsigned char);

extern bool          execute_if_not_null(void *function_ptr);
extern void          exif_remove_and_add_wrapper(int param_1);

extern struct struct_CameraConfig *getCameraConfigStructPtr(void);
extern int           getMCURegisterByte(uint param_1,byte *data);


extern void          get_cold_item_camera_name(char * camera_name);
extern byte          get_cold_item_sd_management_p();
extern enum_battery_type  get_g_cold_item_battery_type(void);
extern char          get_cold_item_112(void);
extern unsigned int  get_battery_percent();
extern unsigned int  get_battery_percent_from_voltage(unsigned int voltage);
extern short unsigned int get_battery_voltage_x100();
extern unsigned int  get_current_operating_time_ms(void);
extern void          get_directory_suffix_file_prefix(char *directory_suffix, char *file_prefix);
extern void          get_directory_suffix_file_prefix_indirect(char *directory_suffix, char *file_prefix);

//extern int           getHceTaskMenuMultiItem2_FSM_valid(void);
extern short unsigned int get_g_cold_item_video_duration(void);
extern int           get_g_cold_item_led_power(void);
extern unsigned int  get_gTemperatureUnitCelsiusP(void);
extern int           get_g_temperature_value(void);
extern unsigned char get_DAT_80357b60_at_global_index(void);
extern void          get_cold_item_short_rtc_time(struct_short_RTCTime *short_rtc_time);
extern int           get_power_supply_mode(void);
extern void          get_rtc_time_or_alarm(int flag, struct_RTCTime *current_rtc_time);
extern void          get_rtc_time(struct_RTCTime *current_rtc_time);
extern void          get_short_rtc_time(struct_short_RTCTime *short_rtc_time);
extern int           get_temperatureForC(void); // this version actually reads the register
extern unsigned int  get_unix_time(unsigned int ms_date_time, struct_DateTime *expanded_date_time);
extern short         get_current_video_duration_in_seconds(void);
extern unsigned long long get_64_bit_date_time_in_seconds(struct_DateTime *current_date_time);

extern void          hal_set_rtc(struct_short_RTCTime *short_rtc_time);
extern void          HceCommon_InitOptions();
extern void          HceCommon_SetCaptureImag(unsigned int param_1,char *param_2);
extern void          HceCommon_RestoreDefaultColdItem(char preserve_rtc_p);

extern int           HceStampLoadFont(unsigned int font_id,
				      unsigned short *large_width, unsigned short *large_height,
				      unsigned short *small_width, unsigned short *small_height,
				      unsigned int font_scale);

extern void          HceStampDrawLogo(struct_video_page_descriptor *video_page_desciptor, 
				      unsigned int font_scale);

extern void          initCodeSentry(uint);
extern void          IRLedOff(void);

extern void          PV_RAW_ImageWrite(int param_1,char *param_2);
extern uint          get_next_state_from_menu_enter(uint param_1,struct_hp5_menu_item *param_2 ,uint param_3, struct_menu_root **param_4);

extern int           local_sprintf(char*, char*, ...);
extern void          log_printf(unsigned int, char *, ...);

extern void *        memcpy(void *__dest,void *__src,uint __n); // don't change the name -- C needs this
                                                                // just the way it is

extern void*         memoryAllocate(unsigned int size);

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

extern unsigned int  positive_diff(unsigned int end_time_ms, unsigned int start_time_ms);
extern int           posix_finfo(unsigned int file_ptr, struct_PosixFinfo *finfo);

extern int           seekToSpecifiedFileLocation(unsigned int file_ptr, unsigned int offset, unsigned int whence);

extern int           set_aaa_ae_pipeline_wrapper(int param_1);
extern int           set_aaa_awb_pipeline_wrapper(int param_1);

extern void          setBatteryCalibConfig(void);

extern void          setCodeSentryCSR(int address,int flag);
extern void          setCodeSentryAddressRegion(int filter_index,int dev_type,void *base,void *bounds);

extern void          set_cold_item_led_power(unsigned int);
extern int           set_cold_item_language_id(byte param_1);
extern void          set_g_ae_parameter(byte ae_parameter);
extern void          set_g_cold_item_battery_type(unsigned int battery_type);
extern void          set_cold_item_pir_range(enum_pir_range_options pir_range_option);
extern void          set_cold_item_sd_management_p(byte param_1);
extern void          set_pir_sensor_range(enum_pir_range_options pir_range_option);
extern void          set_pre_printf_state(void);

extern void          set_ir_led_power_pwm(enum_alt_ir_led_intensity);
extern void          set_ir_led_intensity_from_cold_item(enum_cold_item_ir_led_intensity ir_led_intensity);
extern void          smart_IR_log_printf(char * format_string, unsigned int arg1);
extern void          smart_IR_log_sub_printf(char *format_string, unsigned int arg1);
extern void          sp5kIqBlockEnable(char, ...);
extern void          sp5kIqCfgSet(unsigned int, unsigned int);
extern int           sp5kModeSet(int next_mode);

extern void          store_pressure_trend(void);

extern unsigned int  btc_strlen(char* string);
extern char *        btc_strcpy(char *dest, char *source);

extern void          function_with_syscall_zero(char *sys_file, unsigned int line_number,int param_3);

extern int           thread_sleep(enum_timer_wait_scale , uint);
extern void          tty_printf(char *, ...);
extern void          tty_printf_battery_stats();

extern bool          ui_cursor_key_pressed_p(enum_ui_cursor_button button_code);
extern unsigned int  vfsClose(unsigned int file_ptr);
extern unsigned int  vfsFileCTimeGet(unsigned int file_ptr, unsigned int *ms_like_modified_date_time, unsigned int *ms_like_created_date_time);
extern unsigned int  vfsOpen(char *filename, unsigned int flags);
extern unsigned int  vfsFileSizeGet(unsigned int file_ptr);
extern void          vfsFileDel(char *filename);
extern void          vfsFileCopy(char *source_filename, char *dest_filename);

extern void          Volt_Calib_Bat(void);


extern int          Write_LEDOn();
extern int          Write_LEDOff();

extern int          WrappedMPUSpi_WriteNPacketByManualPWM(struct_mpu_spi_address *mpu_spi_address,
							  struct_mpu_spi_data *mpu_spi_data,
							  uint num_bytes);


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
extern void handleHDR_menu();
extern void handleImageDataStrip_menu();
extern void handleMotionTest_menu();
extern void handleMotionDetection_menu();
extern void handlePIRRange_menu();
extern void handleBatteryType_menu();
extern void handleTriggerSpeed_menu();
extern void handleRestoreDefault_menu();
extern void handleTimelapseFreq_menu();
extern void handleTimelapsePeriod_menu();
extern void handleDeleteAll_menu();
extern void handleEraseSDCard_menu();
extern void handleTVOut_menu();
extern void handleLanguage_menu();
extern void handleIRLedPower_menu();
extern void handleCaptureTimerP_menu();
extern void handleSetCaptureTimerP_menu();
extern void handleSmartIRVideo_menu();
extern void handleSDManagement_menu();
extern void handleFirmwareUpgrade_menu();
extern void tmmi2_final_state();


extern void handleCommitUpdates_menu();
