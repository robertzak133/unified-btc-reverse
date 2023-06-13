//
// aperture.h
// 
// Prototype declaration for timelapse additions

// 


// External Global Variables


typedef struct struct_night_mode_min_max {
  int min;
  int max;
} struct_night_mode_min_max;

typedef enum enum_aperature_encoding {
  standard = 0,
  low_light, 
  no_light,
  invalid
} enum_aperture_encoding;



struct_hp5_menu_item g_apt_aperture_menu[4];
struct_night_mode_min_max g_apt_nightmode_threshold_lookup_table[3];


byte apt_get_cold_item_aperture();

void apt_set_cold_item_aperture(byte aperture);

void apt_handle_aperture_menu();

void apt_get_night_mode_theshold_min_max(uint *min, uint *max, uint aperture);
bool apt_HceIQ_CheckNightMode(void);



