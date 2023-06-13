//
// low-pir-senstivity.h
// 
// 2022-11-12 Zak: Created
// code that adds a "short range" setting below "normal" and "long" range PIR sensitivyt
//      setting.


#define DEBUG

// global variables
struct_hp5_menu_item g_lps_pir_range_menu[4];


// function calls
void lps_handlePIRRangeMenu(void);

void lps_set_cold_item_pir_range(enum_pir_range_options pir_range);

void lps_set_pir_sensor_range(enum_pir_range_options pir_range_option);
