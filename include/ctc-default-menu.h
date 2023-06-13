// ctc-default-menu.h
// 
// Prototypes and Variables
// 2021-10-20 zak: created


#define CTC_MAX_FSM_RETRY (100)
#define CTC_NUM_MAIN_MENU_FUNCTIONS (30)
#define CTC_NUM_EXTENSIONS_MENU_FSM_STATES (6)

// Variables 

// FSM Template
extern struct_fsm_template g_ctc_extensions_fsm_template;

// Extensions Menus

extern struct_menu_descriptor *g_ctc_extensions_menu_root;

extern char g_ctc_extensions_menu_name[];

extern struct_menu_item_collection_0 g_ctc_load_user_fw_menu_descriptor;
extern struct_menu_item_collection_0 g_ctc_user_func1_menu_descriptor;
extern struct_menu_item_collection_0 g_ctc_user_func2_menu_descriptor;
extern struct_menu_item_collection_and_size g_ctc_extensions_menu_item_array[];

extern void * g_ctc_extensions_menu_state_function_array[];

extern struct_menu_item_collection_4 g_ctc_extensions_menu_descriptors;

extern struct_menu_item_collection_4 g_ctc_config_playback_home_menu;

// Menu Functions

void ctc_handleMainMenuExtensions(void);

void ctc_build_extensions_menu();
void ctc_extensions_menu_set_default_menu_item();
// Stubs for now
void ctc_handle_user_fw_upgrade_menu();
void ctc_handle_func1_menu();
void ctc_handle_func2_menu();
void ctc_extensions_menu_final_state();

// FSM Functions
void ctc_HceTaskMenuMultiItem2_FSM(void);
void ctc_extensions_menu_FSM_change_state(void);
void start_ctc_extensions_menu_FSM(void);





// Hooks
uint ctc_build_root_menu (byte initial_selection, byte next_selection,
			  struct_menu_descriptor **arg_root_menu_descriptor,
			  struct_menu_item_collection_4 *menu_item_collection,
			  int num_items_and_title,
			  char *menu_item_name);

int ctc_fsm_get_valid_HceTaskMenu(void *fsm_function);
int ctc_fsm_spawn_HceTaskMenu(byte initialize_fsm_p,
			      void *fsm_iterator_function,
			      uint ref_count,uint fsm_active,
			      uint param_5);
