//
// aperture.h
// 
// Prototype declaration for timelapse additions

// 


// External Global Variables


typedef struct struct_night_mode_min_max {
  byte min;
  byte max;
} struct_night_mode_min_max;

typedef enum enum_aperture_encoding {
  standard = 0,
  low_light, 
  no_light,
  invalid
} enum_aperture_encoding;


#if (defined BTC_7A_OLD) 
char  g_SST_STANDARD_string[sizeof("STANDARD")];
char  g_SST_LOW_SP_LIGHT_string[sizeof("LOW LIGHT")];
char  g_SST_NO_SP_LIGHT_string[sizeof("NO LIGHT")];
char  g_SST_DAY_SP_THRESHOLD_string[sizeof("DAY THRESHOLD")];
#endif

extern struct_hp5_menu_item g_apt_aperture_menu[4];
extern struct_night_mode_min_max g_apt_nightmode_threshold_lookup_table[3];


enum_aperture_encoding apt_get_rtc_extra_aperture();
void apt_set_rtc_extra_aperture(enum_aperture_encoding aperture);

enum_aperture_encoding apt_get_cold_item_aperture();
void apt_set_cold_item_aperture(enum_aperture_encoding aperture);

void apt_set_rtc_extra_short3_bits15_14(uint param_1);
uint apt_get_rtc_extra_short3_bits15_14(void);

void apt_handle_aperture_menu();

void apt_get_night_mode_threshold_min_max(uint *min, uint *max, 
					 enum_aperture_encoding encoded_aperture);

bool apt_HceIQ_CheckNightMode(void);



