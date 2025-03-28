//
// custom-settings.c
//
// Functions that allow the saving and restoring of custom 
//      settings

#include "BTC.h"
#include "WBWL.h"
#include "menus.h"
#include "custom-settings.h"

// This is the structure of this menu, which, unfortunately, I need
//    to patch in by hand to put into a r/w area of memory
//    a real hack
//struct_hp5_menu_item g_cst_restore_default_menu[5] = {
//  { no_icon, SST_NO,                    0x00, 0x01, 0x00, 0x1, 0x1},
//  { no_icon, SST_FACTORY,               0x00, 0x01, 0x00, 0x1, 0x2},
//  { no_icon, SST_CUSTOM,                0x01, 0x01, 0x00, 0x1, 0x3},
//  { no_icon, SST_SAVE_SP_CUSTOM,        0x00, 0x01, 0x00, 0x1, 0x4},
//  { no_icon, SST_DEFAULT_SP_SETTINGS,   0x00, 0x00, 0x01, 0x03, 0x03}
//};


//#define DEBUG


// Global Variables


// Functions
// Returns 0 if there is no valid custom cold item; 1 if there is
int cst_custom_cold_item_valid_p() {
  return 0;
}

// Returns 0 if there is no valid custom config file; 1 if there is
int cst_valid_custom_config_p() {
  uint file_mode;
  uint file_ptr;

  file_mode = 0x10;
  file_ptr = btc_fopen(CST_CUSTOM_CONFIG_FILENAME, file_mode);
  if (file_ptr == 0) {
    return 0;
  }
  vfsClose(file_ptr);
  return 1; 
}

// Load custom cold item file from SD card
int cst_RestoreCustomColdItem() {

  uint file_ptr;
  char *error_message;
  uint file_mode;
  uint file_size;
  uint error_num0; 
  uint error_num1;
  int return_value;

#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("cst_RestoreCustomColdItem - e\n");
  check_post_printf_state_set_sio_params();
#endif
  
  g_ColdItemData.busy_p = 1;
  file_mode = 0x10;
  file_ptr = btc_fopen(CST_CUSTOM_CONFIG_FILENAME, file_mode);
  if (file_ptr == 0) {
    set_pre_printf_state();
    tty_printf("%s_failed to open config file %s!\n",
	       "cst_RestoreCustomColdItem", CST_CUSTOM_CONFIG_FILENAME);
    check_post_printf_state_set_sio_params();
    return 0;
  }
  seekToSpecifiedFileLocation(file_ptr,file_mode,0,0,0);
  file_size = fsize(file_ptr);
  if (file_size < sizeof(g_ColdItemData)) {
    error_num0 = file_size;
    set_pre_printf_state();
    error_message = "COLD.BIN size invalid[%d/%d]";
LAB_8005b1d8:
    error_num1 = sizeof(g_ColdItemData);
  }
  else {
    file_size = btc_fread(file_ptr,&g_ColdItemData,sizeof(g_ColdItemData));
    if (file_size != sizeof(g_ColdItemData)) {
      error_num0 = file_size;
      set_pre_printf_state();
      error_message = "%read size invalid [%d/%d]";
      goto LAB_8005b1d8;
    }
    if (g_ColdItemData.file_length != sizeof(g_ColdItemData)) {
      set_pre_printf_state();
      error_message = "%recorded size invalid[%d/%d]";
      error_num0 = (uint)(ushort)g_ColdItemData.file_length;
      goto LAB_8005b1d8;
    }
    if (g_ColdItemData.signature == COLD_ITEM_SIGNATURE) {
      g_cold_item_signature_valid_p = 1;
      return_value = 1;
      goto LAB_8005b1ec;
    }
    set_pre_printf_state();
    error_message = "%s data signature invalid_[0x%x_/_%d]";
    error_num0 = (uint)(ushort)g_ColdItemData.signature;
    error_num1 = COLD_ITEM_SIGNATURE;
  }
  return_value = 0;
  tty_printf(error_message, "cst_RestoreCustomColdItem" ,error_num0, error_num1);
  check_post_printf_state_set_sio_params();
LAB_8005b1ec:
  btc_fclose(file_ptr);
#if (defined BTC_7A) || (defined BTC_7E) || (defined BTC_8E) || (defined BTC_7E_HP4) || (defined BTC_8E_HP4) || (defined BTC_7E_HP5) || (defined BTC_8E_HP5)
  memcpy(&g_ReferenceColdItemData,&g_ColdItemData,sizeof(g_ColdItemData));
#endif
  return return_value;
}


// Save custom cold itme file to SD card
void cst_SaveCustomColdItem() {

  uint file_ptr; 
  uint file_mode; 
  uint bytes_written;

#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("cst_SaveCustomColdItem - s\n");
  check_post_printf_state_set_sio_params();
#endif

  file_mode = 0x20;
  file_ptr = btc_fopen(CST_CUSTOM_CONFIG_FILENAME,file_mode);
  if (file_ptr == 0) {
    file_mode = 0x24;
    file_ptr = btc_fopen(CST_CUSTOM_CONFIG_FILENAME,file_mode);
    if (file_ptr == 0) {
      set_pre_printf_state();
      tty_printf("failed_to_open_COLD.BIN!");
      check_post_printf_state_set_sio_params();
      return;
    }
  }
  // We succussfulely opened the file for writing
  seekToSpecifiedFileLocation(file_ptr, file_mode,0,0,0);
  bytes_written = btc_fwrite(file_ptr, &g_ColdItemData,sizeof(g_ColdItemData));
  btc_fclose(file_ptr);

#ifdef DEBUG
  set_pre_printf_state();
  tty_printf("cst_SaveCustomColdItem - e ; expected/actual bytes %d/%d\n",
	     sizeof(g_ColdItemData),
	     bytes_written);
  check_post_printf_state_set_sio_params();
#endif  
}

#ifdef FOO
// Function to highlight or blank out the (load) "custom" menu item
//    depending on whether a custom param file exists, or not

void highlight_load_custom_item__menu(uint param_1)
{
  byte bVar1;
  
  bVar1 = 154;
  // if (param_1 < 4) {
  //  bVar1 = BYTE_ARRAY_802cddc4[param_1];
  // }
  menu_draw_menu_name(&g_menu_root);
  HceMenuMultiItem_DrawItem_Wrapper(0x20,bVar1,2,1,0,0,1,&g_menu_root);
  return;
}
#endif

// This function replaced the factory function for restoring defeaults
//      Handles two more cases: loading custom config from SD card and
//      storing custom config to SD card
void cst_handleRestoreDefault_menu(void) {
  struct_CameraConfig *camera_config;
  int iVar1;
  int iVar2;
  byte up_p;
  uint index;
  uint valid_custom_config_file;
  struct_menu_selections_descriptor menu_selections;
  
  camera_config = getCameraConfigStructPtr();

  // This check is here to get handleRestoreDefault_menu()
  //      function in the symbol table
  if (camera_config == (struct_CameraConfig *) 0) {
    handleRestoreDefault_menu();
    return;
  }

  if (camera_config->exit_menu_p_or_ir_led_on != 0) {
    // this clause is done on entry to function
    camera_config->exit_menu_p_or_ir_led_on = 0;
    camera_config->menu_selection_1 = 0;  // default menu selection is "NO" -- do not load new config

    valid_custom_config_file = cst_valid_custom_config_p();

    if (valid_custom_config_file == 1) {
      getCurrentMenuCollectionAndSize(&menu_selections,&g_menu_root);
      if (menu_selections.num_array_entries > 1) {
	menu_selections.menu_item_array[2].disable_item = 0;
#ifdef DEBUG
	set_pre_printf_state();
	tty_printf("cst_handleRestoreDefault_menu: num_entries = %d; menu_item_array address = 0x%08x; text_id = %d; disable_item = 0x%08x\n",
		   menu_selections.num_array_entries, 
		   menu_selections.menu_item_array, 
		   menu_selections.menu_item_array[2].text_id, 
		   menu_selections.menu_item_array[2].disable_item);
	check_post_printf_state_set_sio_params();
#endif  
	}
    }
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
    return;
  }

  // Up/Down Buttons -- scroll up or down
  iVar1 = ui_cursor_key_pressed_p(up);
  if (((iVar1 == 1) && (up_p = 0, g_up_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(down), iVar1 == 1 && (up_p = 1, g_down_button_enable == 2))))
  {
    menu_get_next_menu_selection(up_p,&camera_config->menu_selection_1,1,&g_menu_root);
    menu_redraw_items(camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  // Left/Right buttons -- Noop
  iVar1 = ui_cursor_key_pressed_p(left);
  if (((iVar1 == 1) && (g_left_button_enable == 2)) ||
     ((iVar1 = ui_cursor_key_pressed_p(right), iVar1 == 1 && (g_right_button_enable == 2)))) {
    return;
  }
  // Enter Button
  iVar1 = ui_cursor_key_pressed_p(enter);
  if ((iVar1 == 1) && (g_enter_button_enable == 2)) {
    index = (uint)camera_config->menu_selection_1;
    camera_config->exit_menu_p_or_ir_led_on = 1;
    iVar2 = get_next_state_from_menu_enter
                      (index,g_wbwl_camera_setup_selector_array[index].menu_item_array,
                       g_wbwl_camera_setup_selector_array[index].num_array_entries,
                       (struct_menu_root **)&g_menu_root);
    if (iVar2 == 0xff) {
      return;
    }
    iVar1 = iVar2;
    switch(camera_config->menu_selection_1) {
    case 0: // Escape
      goto LAB_8010e2fc;
      break;
    case 1: // Load Factory Defaults
      HceCommon_RestoreDefaultColdItem(1);
      camera_config->commit_menu_change = 1;
      break;
    case 2: // Load Custom Defaults (if available)
      cst_RestoreCustomColdItem();
      camera_config->commit_menu_change = 1;
      break;
    case 3: // Save Custom Defaults
      cst_SaveCustomColdItem();
      camera_config->commit_menu_change = 1;
      break;
    default: // should never get here
      goto LAB_8010e2fc;
      break;
    }
  }
  else {
    iVar1 = ui_cursor_key_pressed_p(mode);
    if (iVar1 != 1) {
      return;
    }
    if (g_mode_button_enable != 2) {
      return;
    }
    camera_config->exit_menu_p_or_ir_led_on = 1;
    camera_config->video_p = 0;
    iVar2 = get_next_state_from_menu_mode(1,(struct_menu_root **)&g_menu_root);
    iVar1 = WBWL_NUM_BTC_SETUP_MENU_FUNCTIONS + WBWL_NUM_WBWL_SETUP_MENU_FUNCTIONS + 5;
    if (iVar2 == 0xff) goto LAB_8010e2fc;
  }
  iVar1 = iVar2;
LAB_8010e2fc:
  set_fsm_state_absolute(iVar1);
  return;
}




#ifdef FOO
void handleFirmwareUpgrade_menu(void)

{
  struct_CameraConfig *camera_config;
  int iVar1;
  uint uVar2;
  byte up_p;
  struct_menu_selections_descriptor menu_selections;
  
  camera_config = getCameraConfigStructPtr();
  if (camera_config->exit_menu_p_or_ir_led_on != 0) {
    camera_config->exit_menu_p_or_ir_led_on = 0;
    camera_config->menu_selection_1 = 1;
    iVar1 = Hce_FWFileChk(0);
    if (iVar1 != 0) {
      getCurrentMenuCollectionAndSize(&menu_selections,&g_menu_root);
      uVar2 = 0;
      if (1 < (byte)menu_selections.num_array_entries) {
        for (; (int)uVar2 < (int)((byte)menu_selections.num_array_entries - 1);
            uVar2 = uVar2 + 1 & 0xff) {
          if (*(short *)&menu_selections.menu_item_array[uVar2].text_id == 0xb) {
            menu_selections.menu_item_array[uVar2].foreground_color = 0;
          }
        }
      }
    }
    menu_draw_selected_item(&camera_config->menu_selection_1,&g_menu_root);
    return;
  }
  if (camera_config->video_p == 0) {
    iVar1 = ui_cursor_key_pressed_p(up);
    if ((iVar1 == 1) && (g_up_button_enable == 2)) {
      iVar1 = get_hce_task_upgrade_fsm_valid_bool();
      up_p = 0;
      if (iVar1 == 0) {
LAB_8010cc54:
        menu_get_next_menu_selection(up_p,&camera_config->menu_selection_1,1,&g_menu_root);
        menu_redraw_items(camera_config->menu_selection_1,&g_menu_root);
        return;
      }
    }
    else {
      iVar1 = ui_cursor_key_pressed_p(down);
      if ((iVar1 == 1) && (g_down_button_enable == 2)) {
        iVar1 = get_hce_task_upgrade_fsm_valid_bool();
        if (iVar1 == 0) {
          up_p = 1;
          goto LAB_8010cc54;
        }
      }
      else {
        iVar1 = ui_cursor_key_pressed_p(left);
        if (((iVar1 != 1) || (g_left_button_enable != 2)) &&
           ((iVar1 = ui_cursor_key_pressed_p(right), iVar1 != 1 || (g_right_button_enable != 2)))) {
          iVar1 = ui_cursor_key_pressed_p(enter);
          if ((iVar1 == 1) && (g_enter_button_enable == 2)) {
            iVar1 = get_hce_task_upgrade_fsm_valid_bool();
            if (iVar1 == 0) {
              getCurrentMenuCollectionAndSize(&menu_selections,&g_menu_root);
              if (*(short *)&menu_selections.menu_item_array[camera_config->menu_selection_1].
                             text_id == 11) {
                camera_config->video_p = 1;
                FUN_80105994(highlight_load_firmware_menu);
                startHceTaskUpgrade_FSM(0);
                return;
              }
              camera_config->exit_menu_p_or_ir_led_on = 1;
              iVar1 = get_next_state_from_menu_enter
                                ((uint)camera_config->menu_selection_1,(struct_hp5_menu_item *)0x0,0
                                 ,(struct_menu_root **)&g_menu_root);
LAB_8010cdb4:
              if (iVar1 == 0xff) {
                iVar1 = 31;
              }
              set_fsm_state_absolute(iVar1);
              return;
            }
          }
          else {
            iVar1 = ui_cursor_key_pressed_p(mode);
            if ((iVar1 == 1) &&
               ((g_mode_button_enable == 2 &&
                (iVar1 = get_hce_task_upgrade_fsm_valid_bool(), iVar1 == 0)))) {
              camera_config->exit_menu_p_or_ir_led_on = 1;
              iVar1 = get_next_state_from_menu_mode(1,(struct_menu_root **)&g_menu_root);
              goto LAB_8010cdb4;
            }
          }
        }
      }
    }
  }
  else {
    iVar1 = get_hce_task_upgrade_fsm_valid_bool();
    if (iVar1 == 0) {
      camera_config->video_p = 0;
      camera_config->exit_menu_p_or_ir_led_on = 1;
    }
  }
  return;
}

#endif
