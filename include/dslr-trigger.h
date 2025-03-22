//
// dslr-trigger.h
//      Constants and function prototypes for 
//      code which triggers DSLR by illuminating
//      "aim" LED after trigger, while photos/videos
//      are being taken
// 2022-12-03 zak: added menu for enabling


struct_hp5_menu_item g_ext_trigger_enable_menu[4];

typedef enum enum_ext_trigger {
  xtrg_off = 0,
  xtrg_dslr = 1,
  xtrg_flash = 2
} enum_ext_trigger;

void xtrg_Write_LEDOn();
void xtrg_Write_LEDOff();

void dt_RapidFirePhotos_printf_hook(char * format_string, unsigned int delay_ms,
				    unsigned int image_width, unsigned int image_height,
				    unsigned int burst_size);

void dt_off_photo_burst_hook();

void dt_video_log_printf_hook(unsigned int level, char * format_string, char * function_name);

void dt_IRLedOff(void);

void xtrg_handle_led_enable_menu(void);

enum_ext_trigger xtrg_get_cold_item_ext_trigger_enum();

void xtrg_set_cold_item_ext_trigger_enum(enum_ext_trigger ext_trigger_enum);


