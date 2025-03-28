// 
// battery-monitor.h
// 
// Prototypes for functions defined in battery-monitor.c


// Battery Log filename

#define BATTERY_LOG_FILENAME "D:\\BatLog.txt"

// Fixed Point
//   To avoid floating point operations, while still handling standard units (Joules)
//      and a wide range of values between the small amount of energy consumed in 
//      single photos and videos, to the lage capacity of batteries, I am using
//      a fixed point format wherein the top 24 bits is the integer components; and the 
//      the bottom 8 bits of an unsigned int the fractional component. 

// 2022-01-16 Zak: Updated to use power values measured for White Flash converted
//      cameras. 

#define JOULES_2_FXP_UINT(joules) (unsigned int) (joules * 256)
#define WATTS_2_FXP_UINT(watts)   (unsigned int) (watts * 256)
#define ADJ_2_FXP_UINT(alpha)     (unsigned int) (alpha * 256)
#define JPH_2_FSP_UINT(jph)       (unsigned int) (jph * 256)

#define JOULES_INT(joules)        (unsigned int) (joules >> 8)
#define JOULES_DECIMAL(joules)    (unsigned int) (((joules & 0xff) * 1000) >> 8)
#define WATTS_INT(watts)          (unsigned int) (watts >> 8)
#define WATTS_DECIMAL(watts)      (unsigned int) (((watts & 0xff) * 1000) >> 8)
#define ADJ_INT(alpha)            (unsigned int) (alpha >> 8)
#define ADJ_DECIMAL(alpha)        (unsigned int) (((alpha & 0xff) * 1000) >> 8)

// It takes this much energy to turn the camera on and then off
#define ENERGY_ON_OFF           JOULES_2_FXP_UINT(0.25)

// These are in Joules
#define ENERGY_PHOTO_COLOR_OFF  JOULES_2_FXP_UINT(0.5)
#define ENERGY_PHOTO_COLOR_LOW  JOULES_2_FXP_UINT(1.5)
#define ENERGY_PHOTO_COLOR_HIGH JOULES_2_FXP_UINT(2.5) 
#define ENERGY_PHOTO_BW_OFF     JOULES_2_FXP_UINT(0.30)
#define ENERGY_PHOTO_BW_LOW     JOULES_2_FXP_UINT(1.30) 
#define ENERGY_PHOTO_BW_HIGH    JOULES_2_FXP_UINT(2.30)

// These are in Watts
#define POWER_VIDEO_COLOR_OFF   WATTS_2_FXP_UINT(2.31)
#define POWER_VIDEO_COLOR_LOW   WATTS_2_FXP_UINT(4.88)
#define POWER_VIDEO_COLOR_HIGH  WATTS_2_FXP_UINT(7.00)
#define POWER_VIDEO_BW_OFF      WATTS_2_FXP_UINT(1.5)
#define POWER_VIDEO_BW_LOW      WATTS_2_FXP_UINT(4.5)
#define POWER_VIDEO_BW_HIGH     WATTS_2_FXP_UINT(6.0)

#define POWER_UI_ACTIVE         WATTS_2_FXP_UINT(1.8)

// These are in Joules/Day
#define POWER_JPH_STANDBY       JPH_2_FSP_UINT(5.44)
  

// Timely constants
#define BM_SECONDS_PER_YEAR     31556926
#define BM_SECONDS_PER_MONTH    2629743
#define BM_SECONDS_PER_DAY      86400 
#define BM_SECONDS_PER_HOUR     3600
#define BM_SECONDS_PER_MINUTE   60

// Dimensions of lookup table for thermal adjustment
//    of energy consumed
#define POWER_DIM               5
#define TEMPERATURE_DIM         11



// Enumerations
//   a hack so I can fit battery type into a short
#define   LITHIUM_BAT_TYPE  0
#define   ALKALINE_BAT_TYPE 1



// Structures
typedef struct struct_byte_RTCTime {
  byte  year_from_2000; 
  byte  month;
  byte  day;
  byte  hour;
  byte  minute;
  byte  second;
} struct_byte_RTCTime;


// Structure for storing battery telemetry
typedef struct struct_BatteryTelemetry {
  unsigned int energy_consumed;                        // 4
  unsigned int cold_battery_energy_lost;               // 4
  // 
  unsigned short photos_taken_this_uptime_no_flash;    // 2
  unsigned short photos_taken_this_uptime_low_flash;   // 2
  unsigned short photos_taken_this_uptime_hi_flash;    // 2
  unsigned short video_taken_this_uptime_no_flash;     // 2
  unsigned short video_taken_this_uptime_low_flash;    // 2
  unsigned short video_taken_this_uptime_hi_flash;     // 2
  //
  unsigned short total_photos_taken_no_flash;          // 2
  unsigned short total_photos_taken_low_flash;         // 2
  unsigned short total_photos_taken_hi_flash;          // 2
  unsigned short total_video_taken_no_flash;           // 2
  unsigned short total_video_taken_low_flash;          // 2
  unsigned short total_video_taken_hi_flash;           // 2
  // 
  struct_byte_RTCTime install_time;                 //  6
  struct_byte_RTCTime awake_time;                   //  6
  struct_byte_RTCTime asleep_time;                  //  6
  short battery_type;                               //  2
} struct_BatteryTelemetry;





// Function Prototypes

// Hook Functions
void bm_hal_set_rtc_hook(struct_short_RTCTime *short_rtc_time);
void bm_HceCommon_SetCaptureImage_hook(unsigned int id, char * string);
void store_pressure_bm_hook(void);
void bm_Volt_Calib_Bat_hook(void);

void bm_RapidFirePhotos_printf_hook(char * format_string, unsigned int delay_ms,
				    unsigned int image_width, unsigned int image_height,
				    unsigned int burst_size);





// Battery monitor Functions

void bm_initialize(enum_battery_type battery_type);
void bm_on_photo();
void bm_on_photo_burst(unsigned int burst_size);
void bm_off_photo_burst();
void bm_on_video();
void bm_off_video();
unsigned int bm_get_current_battery_level(unsigned int voltage);

int bm_StoreBatteryMonitorFile();
int bm_LoadBatteryMonitorFile();


// private

unsigned int  bm_bilinear_interpolate(int temperature, unsigned int power, 
				     int temperature_indices[11], unsigned int power_indices[5],
				     unsigned int lookup_table[11][5]);
void          bm_get_photo_flash_intensity_color_p(enum_flash_intensity *flash_intensity, int *color_p);
void          bm_get_video_flash_intensity_color_p(enum_flash_intensity *flash_intensity, int *color_p);
unsigned int  bm_get_initial_battery_capacity(enum_battery_type battery_type);
unsigned int  bm_accrue_cold_battery_energy(unsigned int nominal_energy, int temp_in_f, unsigned int power, enum_battery_type battery_type);
void          bm_increment_energy_consumed(unsigned int incremental_energy, unsigned int power);
void          bm_increment_photos(unsigned short num_photos, enum_flash_intensity flash_intensity);
void          bm_increment_video(unsigned short video_duration, enum_flash_intensity flash_intensity);
int           bm_get_delta_short_time(struct_short_RTCTime *end_time, struct_short_RTCTime *start_time);
int           bm_get_delta_byte_time(struct_byte_RTCTime *end_time, struct_byte_RTCTime *start_time);
void          bm_get_byte_rtc_time(struct_byte_RTCTime *byte_time);
unsigned int  bm_get_ui_energy(int elapsed_time_in_seconds);
void          bm_seconds_to_hms(unsigned int input_seconds, int * hour, int *minute, int *second);
void          bm_short_to_byte_rtc_time(struct_byte_RTCTime *byte_time, struct_short_RTCTime *short_time);
void          bm_write_summary_file(void);
void          bm_fprint_battery_telemetry(unsigned int fptr);
void          bm_print_battery_telemetry(void);



