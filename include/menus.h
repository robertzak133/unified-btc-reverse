//
// Prototype for functions and globals associated with WBWL
//    menus extensions

#include "WBWL.h"

// Globals

struct_hp5_menu_item g_wbwl_timelapse_period_menu[7];

struct_hp5_menu_item g_wbwl_camera_setup_menu_item_array[WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 
							 WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS];

struct_menu_selections_descriptor g_wbwl_camera_setup_selector_array[WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + 
								     WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS];

void *g_wbwl_menu_handler_function_array_extensions[WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS+1];

uint wbwl_get_next_state_from_menu_enter(uint index,
					 struct_hp5_menu_item *menu_item_array,
					 uint num_array_entries,
					 struct_menu_root **menu_root);
// Functions
bool menus_execute_if_not_null(uint index);

void menus_handleCommitUpdates_menu();

