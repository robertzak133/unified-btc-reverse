//
// extend-event-SD-card.c
// Per request from James McConnell
// Keep the SD card powered on for some time after the photo/video has been taken


#define EVSD_SD_CARD_DELAY 30000   // 30.000 Seconds at times 1000
//#define DEBUG

typedef enum evsd_extended_sd_power_options {
  evsd_off = 0,
  evsd_on, 
} evsd_extended_sd_power_options;

struct_hp5_menu_item g_evsd_extended_sd_power_menu[3];

void evsd_check_remaining_sd_capacity(void);

byte evsd_get_cold_item_sd_management_p();
void evsd_set_cold_item_sd_management_p(byte);

byte evsd_get_cold_item_extended_sd_power_p();
void evsd_set_cold_item_extended_sd_power_p(byte);

void evsd_handle_extended_sd_power_menu();
