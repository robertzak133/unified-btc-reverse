## A set of hand created binary patches for the BTC-8E-HP5.
## To be consumed by codePatcher() functions
## Zak -- 2022-12-10: Updated for menu-based release

## BA
firmware_bundle_a_patch_list = {}
firmware_bundle_a_patch_list['firmware_ID0'] = {}
firmware_bundle_a_patch_list['firmware_ID0']['start_offset'] = 0x2bdb68;
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes'] = bytes("BTC8EH5_L10200F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']   = bytes("WWL8EH5_230104A", 'utf-8');

firmware_bundle_a_patch_list['firmware_ID0'] = {}
firmware_bundle_a_patch_list['firmware_ID0']['start_offset'] = 0x2d86dc;
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes'] = bytes("BTC8EH5_L10200F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']   = bytes("WWL8EH5_230104A", 'utf-8');


############# BUNDLE A Patches ################################
#
# Rewrite the call that sprintf()'s the string to the bottom of the ribbon
#    in screenPrintReplayHeaderRibbons() at 0x800269d8
#    so that at 0x80026b08
#    so that it calls a custom sprintf function we just created at 0x80066ab8
#    instead of to "local_sprintf" at 0x80362354
custom_ribbon_patch_list = {}
custom_ribbon_patch_list['Custom_Ribbon'] = {}
custom_ribbon_patch_list['Custom_Ribbon']['start_offset'] = 0x00112194
custom_ribbon_patch_list['Custom_Ribbon']['change_from_jump'] = 'jal.local_sprintf'
custom_ribbon_patch_list['Custom_Ribbon']['change_to_jump'] = 'jal.wbwl_custom_ribbon_sprintf'
# this in HandleReplayMenuVideo; source line 27
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset'] = 0x00112af0
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['change_from_jump'] = 'j.draw_video_scroll_bar'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['change_to_jump'] = 'j.ld_draw_video_scroll_bar'
# this in HandleReplayMenuVideo; source line 78
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset'] = 0x00112a40
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['change_from_jump'] = 'jal.draw_video_scroll_bar'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['change_to_jump'] = 'jal.ld_draw_video_scroll_bar'
# this in HandleReplayMenuVideo; source line 34
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook'] = {}
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset'] = 0x00112844
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['change_from_jump'] = 'jal.draw_rectangle_wrapper'
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['change_to_jump'] = 'jal.ld_clear_video_scroll_bar'



# eliminate the limit check on night time video length by
#   nulling out the store that sets video length to 20 seconds if IR LED on
#   this allows the ribbon display to properly record remaining video lenght
#   special case in HceTaskRecording_RecVideoIninit()
#   replace the code that would otherwise limit the video to 20 seconds with a NOOP
#   ~source line 140
night_video_limit_patch_list = {}
night_video_limit_patch_list['No_Video_Limit_Store'] = {}
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset'] = 0x001001a4
night_video_limit_patch_list['No_Video_Limit_Store']['change_from_bytes'] = bytes([0x14,0x00,0x02,0x24])
night_video_limit_patch_list['No_Video_Limit_Store']['change_to_bytes']   = bytes([0x00,0x00,0x00,0x00])

#
# custom_info_strip patch
# HceStampDraw_draw_info_bar
# ~Source code line 110
custom_info_strip_patch_list = {}
custom_info_strip_patch_list['date_local_sprintf'] = {}
custom_info_strip_patch_list['date_local_sprintf']['start_offset'] = 0x00fa550
custom_info_strip_patch_list['date_local_sprintf']['change_from_jump'] = 'jal.local_sprintf'
custom_info_strip_patch_list['date_local_sprintf']['change_to_jump']   = 'jal.wbwl_custom_info_strip_date_sprintf'
# HceStampDraw_draw_info_bar
# ~Source code line 123
custom_info_strip_patch_list['time_local_sprintf'] = {}
custom_info_strip_patch_list['time_local_sprintf']['start_offset'] = 0x00fa5a8
custom_info_strip_patch_list['time_local_sprintf']['change_from_jump'] = 'jal.local_sprintf'
custom_info_strip_patch_list['time_local_sprintf']['change_to_jump']   = 'jal.wbwl_custom_info_strip_time_sprintf'
# HceStampDraw_draw_info_bar
# ~Source code line 148
custom_info_strip_patch_list['last_strlen'] = {}
custom_info_strip_patch_list['last_strlen']['start_offset'] = 0x00fa6c4
custom_info_strip_patch_list['last_strlen']['change_from_jump'] = 'jal.btc_strlen'
custom_info_strip_patch_list['last_strlen']['change_to_jump']   = 'jal.wbwl_custom_info_strip_strlen'
# Intercept calls to draw logo on info strip ("stamp")
# HceStillStampCB
# ~Source code line 96
custom_info_strip_patch_list['still_logo'] = {}
custom_info_strip_patch_list['still_logo']['start_offset'] = 0x00fac84
custom_info_strip_patch_list['still_logo']['change_from_jump'] = 'jal.HceStampDrawLogo'
custom_info_strip_patch_list['still_logo']['change_to_jump']   = 'jal.wbwl_StampDrawLogo'
# HceVideoStampUpdate
# ~Source code line 14
custom_info_strip_patch_list['video_logo'] = {}
custom_info_strip_patch_list['video_logo']['start_offset'] = 0x00fa004
custom_info_strip_patch_list['video_logo']['change_from_jump'] = 'jal.HceStampDrawLogo'
custom_info_strip_patch_list['video_logo']['change_to_jump']   = 'jal.wbwl_StampDrawLogo'

# HceStampLoadFont
# Reduce the Height and Width of the ICON font by a factor of 2
#        this is done early, and insures all the downstream settings
#        are correct.  The only thing you have to do is *also* display
#        the logo at half scale. 
# Line 14
custom_info_strip_patch_list['load_font_width'] = {}
custom_info_strip_patch_list['load_font_width']['start_offset'] = 0x00f8100
custom_info_strip_patch_list['load_font_width']['change_from_bytes'] = bytes([0x30,0x00,0x02,0x24])
custom_info_strip_patch_list['load_font_width']['change_to_bytes']   = bytes([0x16,0x00,0x02,0x24])
# Line 15
custom_info_strip_patch_list['load_font_width'] = {}
custom_info_strip_patch_list['load_font_width']['start_offset'] = 0x00f8104
custom_info_strip_patch_list['load_font_width']['change_from_bytes'] = bytes([0x60,0x00,0x03,0x24])
custom_info_strip_patch_list['load_font_width']['change_to_bytes']   = bytes([0x30,0x00,0x03,0x24])


#
# volume and file naming patches
# in Init_DCF
vfn_patch_list = {}
vfn_patch_list['fatVolLabSet'] = {}
vfn_patch_list['fatVolLabSet']['start_offset'] = 0x000fcdc4
vfn_patch_list['fatVolLabSet']['change_from_jump'] = 'jal.fatVolLabSet_wrapper'
vfn_patch_list['fatVolLabSet']['change_to_jump']   = 'jal.wbwl_fatVolLabSet'
# in HceMedia_PreInitDCFFS
vfn_patch_list['dir_file_fix0'] = {}
vfn_patch_list['dir_file_fix0']['start_offset'] = 0x00ed9d4
vfn_patch_list['dir_file_fix0']['change_from_jump'] = 'jal.btc_init_directory_suffix_file_prefix'
vfn_patch_list['dir_file_fix0']['change_to_jump']   = 'jal.wbwl_init_directory_suffix_file_prefix'
# in another_media_init
vfn_patch_list['dir_file_fix1'] = {}
vfn_patch_list['dir_file_fix1']['start_offset'] = 0x00ecf40
vfn_patch_list['dir_file_fix1']['change_from_jump'] = 'jal.btc_init_directory_suffix_file_prefix'
vfn_patch_list['dir_file_fix1']['change_to_jump']   = 'jal.wbwl_init_directory_suffix_file_prefix'

#
# (debug) utilities
# Hce_FWFileChk
# source code line 46
utilities_patch_list = {}
utilities_patch_list['tty_flush'] = {}
utilities_patch_list['tty_flush']['start_offset'] = 0x0105ae4
utilities_patch_list['tty_flush']['change_from_jump'] = 'jal.check_post_printf_state_set_sio_params'
utilities_patch_list['tty_flush']['change_to_jump']   = 'jal.utilities_check_post_printf_hook'

# handleLanguage_menu
# source code line 39
utilities_patch_list = {}
utilities_patch_list['tty_flush'] = {}
utilities_patch_list['tty_flush']['start_offset'] = 0x010dde4
utilities_patch_list['tty_flush']['change_from_jump'] = 'jal.set_cold_item_language_id'
utilities_patch_list['tty_flush']['change_to_jump']   = 'jal.util_set_cold_item_language_id'


############# DSLR Trigger Patches ############################

# Patch to enable dslr trigger (w/o battery monitor)
# in rapidFirePhotos
# Source line number 11
dslr_trigger_patch_list = {}
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook'] = {}
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook']['start_offset'] = 0x000e7da8
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook']['change_from_jump'] = 'jal.tty_printf'
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook']['change_to_jump'] = 'jal.dt_RapidFirePhotos_printf_hook'
# HceTaskRecording_RecVideoToRec1
# Source code line 78
dslr_trigger_patch_list['dt_video_log_printf_hook'] = {}
dslr_trigger_patch_list['dt_video_log_printf_hook']['start_offset'] = 0x000fe968
dslr_trigger_patch_list['dt_video_log_printf_hook']['change_from_jump'] = 'jal.log_printf'
dslr_trigger_patch_list['dt_video_log_printf_hook']['change_to_jump'] = 'jal.dt_video_log_printf_hook'
# in HceTaskStill
# source line number 18
dslr_trigger_patch_list['dt_burst_mode_off_hook'] = {}
dslr_trigger_patch_list['dt_burst_mode_off_hook']['start_offset'] = 0x00100730
dslr_trigger_patch_list['dt_burst_mode_off_hook']['change_from_jump']  = 'jal.IRLedOff'
dslr_trigger_patch_list['dt_burst_mode_off_hook']['change_to_jump'] = 'jal.dt_off_photo_burst_hook'
# in TaskRecording_FSM_task9
# Source code Line 71
dslr_trigger_patch_list['dt_video_off_hook'] = {}
dslr_trigger_patch_list['dt_video_off_hook']['start_offset'] = 0x000fe73c
dslr_trigger_patch_list['dt_video_off_hook']['change_from_jump']  = 'jal.IRLedOff'
dslr_trigger_patch_list['dt_video_off_hook']['change_to_jump'] = 'jal.dt_video_off_hook'


################# SD Card Power Patches ##############################
## Post event SD Card power
# HceTaskRecording_RecVideoEnd
# source code line 74
extend_event_SD_card_patch_list = {}
extend_event_SD_card_patch_list['extend_video'] = {}
extend_event_SD_card_patch_list['extend_video']['start_offset'] = 0x00fe28c
extend_event_SD_card_patch_list['extend_video']['change_from_jump'] = 'jal.check_remaining_sd_capacity'
extend_event_SD_card_patch_list['extend_video']['change_to_jump']   = 'jal.evsd_check_remaining_sd_capacity'
#
# HceTaskStill_End
# source code line 56
extend_event_SD_card_patch_list['extend_still'] = {}
extend_event_SD_card_patch_list['extend_still']['start_offset'] = 0x010081c
extend_event_SD_card_patch_list['extend_still']['change_from_jump'] = 'jal.check_remaining_sd_capacity'
extend_event_SD_card_patch_list['extend_still']['change_to_jump']   = 'jal.evsd_check_remaining_sd_capacity'


################# Fix IR LED Settings Patches ##############################
## Fix the IR LED setting
# handleIRLedPowerMenu()
# source code line 42
fix_ir_led_settings_patch_list = {}
fix_ir_led_settings_patch_list['extend_video'] = {}
fix_ir_led_settings_patch_list['extend_video']['start_offset'] = 0x010e358
fix_ir_led_settings_patch_list['extend_video']['change_from_jump'] = 'jal.set_cold_item_led_power'
fix_ir_led_settings_patch_list['extend_video']['change_to_jump']   = 'jal.fils_set_cold_item_led_power'

## Intercept the calls to the set_ir_led_intensity_from_cold_item()
# Cmd_IrLED
# Source line 12
fix_ir_led_settings_patch_list['cmd_ir_led'] = {}
fix_ir_led_settings_patch_list['cmd_ir_led']['start_offset'] = 0x00dc4f4
fix_ir_led_settings_patch_list['cmd_ir_led']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
fix_ir_led_settings_patch_list['cmd_ir_led']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'
# HceTaskRecording_RecVideoInit
# Source Line 153
fix_ir_led_settings_patch_list['rec_video_init'] = {}
fix_ir_led_settings_patch_list['rec_video_init']['start_offset'] = 0x01001e8
fix_ir_led_settings_patch_list['rec_video_init']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
fix_ir_led_settings_patch_list['rec_video_init']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'

# HceTaskStill_ToView
# Source Line 28
fix_ir_led_settings_patch_list['still_to_view'] = {}
fix_ir_led_settings_patch_list['still_to_view']['start_offset'] = 0x0101778
fix_ir_led_settings_patch_list['still_to_view']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
fix_ir_led_settings_patch_list['still_to_view']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'

# TaskStillBurstFSM_still_prev_task1
# Source Line 20
fix_ir_led_settings_patch_list['burst_still_prev'] = {}
fix_ir_led_settings_patch_list['burst_still_prev']['start_offset'] = 0x0103684
fix_ir_led_settings_patch_list['burst_still_prev']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
fix_ir_led_settings_patch_list['burst_still_prev']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'

##################################################################################
# Patches for creating new menu(s)
#    - menu_handler_function_array
#    - menu_item_array
menus_patch_list = {}

# Splice in call to our new lookup table
#    - correct check on array size
#    - change argument from pointer to an index
#    - splice in call to our execute function
# in HceTaskMenuMultiItem_fsm_iterator
# line 23
menus_patch_list['menu_function_count'] = {}
menus_patch_list['menu_function_count']['start_offset'] = 0x010d338
menus_patch_list['menu_function_count']['change_from_bytes'] = bytes([0x20, 0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_to_bytes']   = bytes([0x24, 0x00, 0x42, 0x2c])
# Line 28
# replace lw a0,0x0(v0)=> ->handleInit_menu  // g_menu_handler_function_array[index]
# with    lw a0,v0                           // index
menus_patch_list['index_argument'] = {}
menus_patch_list['index_argument']['start_offset'] = 0x010d34c
menus_patch_list['index_argument']['change_from_bytes'] = bytes([0x00, 0x00, 0x44, 0x8c])
menus_patch_list['index_argument']['change_to_bytes']   = bytes([0x00, 0x20, 0x40, 0x80])
# Line 28
# replace call to execute_if_not_null
menus_patch_list['execute_func'] = {}
menus_patch_list['execute_func']['start_offset'] = 0x010d350
menus_patch_list['execute_func']['change_from_jump'] = 'jal.execute_if_not_null'
menus_patch_list['execute_func']['change_to_jump'] = 'jal.menus_execute_if_not_null'

# in g_main_menu_selector_array
#    replace first entry @ 0x802c9e68 g_camera_setup_menu_item_array
#			     w/         g_wbwl_camera_setup_menu_item_array
menus_patch_list['setup_items_pointer'] = {}
menus_patch_list['setup_items_pointer']['start_offset'] = 0x02cc020
menus_patch_list['setup_items_pointer']['change_from_ptr'] = 'g_camera_setup_menu_item_array'
menus_patch_list['setup_items_pointer']['change_to_ptr'] = 'g_wbwl_camera_setup_menu_item_array'
#    replace second @ 0x802c9e6c  which is  0x1a (26)
#                                w/         0x1e (30) 
menus_patch_list['setup_items_number'] = {}
menus_patch_list['setup_items_number']['start_offset'] = 0x02cc024
menus_patch_list['setup_items_number']['change_from_bytes'] = bytes([0x1a, 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_to_bytes'] = bytes([0x1e, 0x00, 0x00, 0x00])

# in handleCameraSetup_menu()
# line 34 - 37
# Hijack call so that we can point to the larger array
menus_patch_list['handleCameraSetup'] = {}
menus_patch_list['handleCameraSetup']['start_offset'] = 0x010d800
menus_patch_list['handleCameraSetup']['change_from_jump'] = 'jal.get_next_state_from_menu_enter'
menus_patch_list['handleCameraSetup']['change_to_jump'] = 'jal.wbwl_get_next_state_from_menu_enter'

# 
# in handleSDManagement_menu
# line 15
# Hijack call so that we can use other bits in this byte
menus_patch_list['getSDManagement'] = {}
menus_patch_list['getSDManagement']['start_offset'] = 0x010de8c
menus_patch_list['getSDManagement']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
menus_patch_list['getSDManagement']['change_to_jump'] = 'jal.evsd_get_cold_item_sd_management_p'

# 
# in handleSDManagement_menu
# line 44
# Hijack call so that we can use other bits in this byte
menus_patch_list['setSDManagement'] = {}
menus_patch_list['setSDManagement']['start_offset'] = 0x010dfb8
menus_patch_list['setSDManagement']['change_from_jump'] = 'jal.set_cold_item_sd_management_p'
menus_patch_list['setSDManagement']['change_to_jump'] = 'jal.evsd_set_cold_item_sd_management_p'

#### a whole bunch of hacks to point to a new "end state" in the g_wbwl_HceTaskMenuMultiItem_fsm_function_array
# in handleMainMenu_menu()
# 51
menus_patch_list['handle_main_menu'] = {}
menus_patch_list['handle_main_menu']['start_offset'] = 0x010d9dc
menus_patch_list['handle_main_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleCameraSetup_menu(void)
# 51
menus_patch_list['handle_camera_setup_menu'] = {}
menus_patch_list['handle_camera_setup_menu']['start_offset'] = 0x010d84c
menus_patch_list['handle_camera_setup_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handlePlayback_menu(void)
# 20
menus_patch_list['handle_playback_menu'] = {}
menus_patch_list['handle_playback_menu']['start_offset'] = 0x01105b8
menus_patch_list['handle_playback_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleHandleSetTimeMenu(void)
# 92
menus_patch_list['handle_set_time_menu'] = {}
menus_patch_list['handle_set_time_menu']['start_offset'] = 0x0111d24
menus_patch_list['handle_set_time_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# handleOperationMode_menu
# 57
menus_patch_list['operation_mode_menu'] = {}
menus_patch_list['operation_mode_menu']['start_offset'] = 0x01104cc
menus_patch_list['operation_mode_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# handlePhotoQuality_menu
# 57
menus_patch_list['photo_quality_menu'] = {}
menus_patch_list['photo_quality_menu']['start_offset'] = 0x01102cc
menus_patch_list['photo_quality_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])

# in handleVideoLength_menu()
# 57
menus_patch_list['video_length_menu'] = {}
menus_patch_list['video_length_menu']['start_offset'] = 0x0110100
menus_patch_list['video_length_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])

# in handleVideoQuality_menu()
# 56
menus_patch_list['video_quality_menu'] = {}
menus_patch_list['video_quality_menu']['start_offset'] = 0x010ff34
menus_patch_list['video_quality_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handlePhotoDelay_menu()
# 52
menus_patch_list['photo_delay_menu'] = {}
menus_patch_list['photo_delay_menu']['start_offset'] = 0x010fd64
menus_patch_list['photo_delay_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleMultiShotMode_menu()
# 57
menus_patch_list['multishot_menu'] = {}
menus_patch_list['multishot_menu']['start_offset'] = 0x010fb88
menus_patch_list['multishot_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleHDR_menu()
# 52
menus_patch_list['HDR_menu'] = {}
menus_patch_list['HDR_menu']['start_offset'] = 0x010f9b8
menus_patch_list['HDR_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['HDR_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleTempUnit_menu()
# 57
menus_patch_list['temp_unit_menu'] = {}
menus_patch_list['temp_unit_menu']['start_offset'] = 0x010f7dc
menus_patch_list['temp_unit_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleCameraName_menu()
# 60
menus_patch_list['camera_name_menu'] = {}
menus_patch_list['camera_name_menu']['start_offset'] = 0x0111220
menus_patch_list['camera_name_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleImageDataStrip_menu()
# 57
menus_patch_list['info_strip_menu'] = {}
menus_patch_list['info_strip_menu']['start_offset'] = 0x010f610
menus_patch_list['info_strip_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleMotionTest_menu()
# 77
menus_patch_list['motion_test_menu'] = {}
menus_patch_list['motion_test_menu']['start_offset'] = 0x010f440
menus_patch_list['motion_test_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handlePIRRange_menu()
# 54
menus_patch_list['pir_range_menu'] = {}
menus_patch_list['pir_range_menu']['start_offset'] = 0x010f174
menus_patch_list['pir_range_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleBatteryType_menu()
# 60
menus_patch_list['battery_type_menu'] = {}
menus_patch_list['battery_type_menu']['start_offset'] = 0x010ef8c
menus_patch_list['battery_type_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleTriggerSpeed_menu()
# 58
menus_patch_list['trigger_speed_menu'] = {}
menus_patch_list['trigger_speed_menu']['start_offset'] = 0x010edb4
menus_patch_list['trigger_speed_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleRestoreDefault_menu()
# 58
menus_patch_list['restore_default_menu'] = {}
menus_patch_list['restore_default_menu']['start_offset'] = 0x010ebe4
menus_patch_list['restore_default_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleTimelapseFreq_menu()
# 57
menus_patch_list['timelapse_freq_menu'] = {}
menus_patch_list['timelapse_freq_menu']['start_offset'] = 0x010ea10
menus_patch_list['timelapse_freq_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleTimelapsePeriod_menu()
# 57
menus_patch_list['timelapse_period_menu'] = {}
menus_patch_list['timelapse_period_menu']['start_offset'] = 0x010e844
menus_patch_list['timelapse_period_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleDeleteAll_menu()
# 104
menus_patch_list['delete_all_menu'] = {}
menus_patch_list['delete_all_menu']['start_offset'] = 0x010e678
menus_patch_list['delete_all_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleIRLedPower_menu()
# 58
menus_patch_list['ir_led_power_menu'] = {}
menus_patch_list['ir_led_power_menu']['start_offset'] = 0x010e3ac
menus_patch_list['ir_led_power_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleSmartIRVideo_menu()
# 58
menus_patch_list['smart_ir_video_menu'] = {}
menus_patch_list['smart_ir_video_menu']['start_offset'] = 0x010e1dc
menus_patch_list['smart_ir_video_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleSDManagement_menu()
# 58
menus_patch_list['sd_management_menu'] = {}
menus_patch_list['sd_management_menu']['start_offset'] = 0x010e00c
menus_patch_list['sd_management_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleLanguage_menu()
# 52
menus_patch_list['language_menu'] = {}
menus_patch_list['language_menu']['start_offset'] = 0x010de38
menus_patch_list['language_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleCaptureTimerP_menu()
# 62
menus_patch_list['capture_timer_menu'] = {}
menus_patch_list['capture_timer_menu']['start_offset'] = 0x010dc64
menus_patch_list['capture_timer_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleCaptureTimerP_menu()
# 118
menus_patch_list['set_capture_timer_menu'] = {}
menus_patch_list['set_capture_timer_menu']['start_offset'] = 0x0111918
menus_patch_list['set_capture_timer_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleFirmwareUpgrade_menu()
# 74
menus_patch_list['firmware_upgrade_menu'] = {}
menus_patch_list['firmware_upgrade_menu']['start_offset'] = 0x010d6b0
menus_patch_list['firmware_upgrade_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])


##################################################################
## Extended SD Card power
# HceTaskRecording_RecVideoEnd
# source code line 74
extended_SD_power_patch_list = {}
extended_SD_power_patch_list['extend_video'] = {}
extended_SD_power_patch_list['extend_video']['start_offset'] = 0x00fe28c
extended_SD_power_patch_list['extend_video']['change_from_jump'] = 'jal.check_remaining_sd_capacity'
extended_SD_power_patch_list['extend_video']['change_to_jump']   = 'jal.evsd_check_remaining_sd_capacity'
#
# HceTaskStill_End
# source code line 56
extended_SD_power_patch_list['extend_still'] = {}
extended_SD_power_patch_list['extend_still']['start_offset'] = 0x010081c
extended_SD_power_patch_list['extend_still']['change_from_jump'] = 'jal.check_remaining_sd_capacity'
extended_SD_power_patch_list['extend_still']['change_to_jump']   = 'jal.evsd_check_remaining_sd_capacity'

# HcePower_CommonPowerOff
# line 24
extended_SD_power_patch_list['power_off'] = {}
extended_SD_power_patch_list['power_off']['start_offset'] = 0x00eb3d8
extended_SD_power_patch_list['power_off']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['power_off']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# still_MCUApp_ResetPIRPin
# line 65
extended_SD_power_patch_list['reset_PIR_pin'] = {}
extended_SD_power_patch_list['reset_PIR_pin']['start_offset'] = 0x00fe484
extended_SD_power_patch_list['reset_PIR_pin']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['reset_PIR_pin']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# TaskRecording_FSM_task10
# line 45
extended_SD_power_patch_list['recording_task9'] = {}
extended_SD_power_patch_list['recording_task9']['start_offset'] = 0x00fe68c
extended_SD_power_patch_list['recording_task9']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['recording_task9']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# HceTaskStill_End
# line 42
extended_SD_power_patch_list['still_end'] = {}
extended_SD_power_patch_list['still_end']['start_offset'] = 0x0100804
extended_SD_power_patch_list['still_end']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['still_end']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# HceTaskStillBurst_End
# line 44
extended_SD_power_patch_list['still_burst_end'] = {}
extended_SD_power_patch_list['still_burst_end']['start_offset'] = 0x010288c
extended_SD_power_patch_list['still_burst_end']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['still_burst_end']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# HceTaskTimeLapse_WaitMountSD
# line 12
extended_SD_power_patch_list['timelapse_sd'] = {}
extended_SD_power_patch_list['timelapse_sd']['start_offset'] = 0x0104f74
extended_SD_power_patch_list['timelapse_sd']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['timelapse_sd']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# handleSDManagement_menu
# slightly different -- this is for highlighting menu item -- it gets the full encoding
# line 15
extended_SD_power_patch_list['sd_management_menu'] = {}
extended_SD_power_patch_list['sd_management_menu']['start_offset'] = 0x010de8c
extended_SD_power_patch_list['sd_management_menu']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['sd_management_menu']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'

################# Short Range Sensitivity Patches ###########################
## Intercept calls required to expand PIR range to include a "short range" option

short_range_pir_patch_list = {}

# Intercepts setting cold item
# handlePIRRangeMenu
# source line 39
#short_range_pir_patch_list['set_cold_item'] = {}
#short_range_pir_patch_list['set_cold_item']['start_offset'] = 0x010f114
#short_range_pir_patch_list['set_cold_item']['change_from_jump'] = 'jal.set_cold_item_pir_range'
#short_range_pir_patch_list['set_cold_item']['change_to_jump']   = 'jal.lps_set_cold_item_pir_range'

# creating new menu items
# in g_camera_selector_array[13]
#
short_range_pir_patch_list['menu_item_array'] = {}
short_range_pir_patch_list['menu_item_array']['start_offset'] = 0x002cbe58
short_range_pir_patch_list['menu_item_array']['change_from_ptr'] = 'g_pir_range_menu'
short_range_pir_patch_list['menu_item_array']['change_to_ptr']   = 'g_lps_pir_range_menu'

short_range_pir_patch_list['menu_item_count'] = {}
short_range_pir_patch_list['menu_item_count']['start_offset'] = 0x02cbe5c
short_range_pir_patch_list['menu_item_count']['change_from_bytes'] = bytes([0x03, 0x00, 0x00, 0x00])
short_range_pir_patch_list['menu_item_count']['change_to_bytes']   = bytes([0x04, 0x00, 0x00, 0x00])

# Intercepts of "set_pir_sensor_range"
# HcePower_CommonPowerOff
# source 27
short_range_pir_patch_list['power_off'] = {}
short_range_pir_patch_list['power_off']['start_offset'] = 0x00eb3f8
short_range_pir_patch_list['power_off']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['power_off']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'
# HcePower_CommonPowerOn
# source 75
short_range_pir_patch_list['power_on'] = {}
short_range_pir_patch_list['power_on']['start_offset'] = 0x010afcc
short_range_pir_patch_list['power_on']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['power_on']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'
# handlePIRRangeMenu
# source 40
short_range_pir_patch_list['pir_menu'] = {}
short_range_pir_patch_list['pir_menu']['start_offset'] = 0x010f11c
short_range_pir_patch_list['pir_menu']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['pir_menu']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'
# HceTask_WaitPIRTaskEnd
# source 11
short_range_pir_patch_list['pir_task_end'] = {}
short_range_pir_patch_list['pir_task_end']['start_offset'] = 0x0112f68
short_range_pir_patch_list['pir_task_end']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['pir_task_end']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'
# TaskPIRTest_FSM_init_task0
# 13
short_range_pir_patch_list['pir_test'] = {}
short_range_pir_patch_list['pir_test']['start_offset'] = 0x0113cc4
short_range_pir_patch_list['pir_test']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['pir_test']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'



################# Fix IR LED Settings Patches ##############################
## Fix the IR LED setting
fix_ir_led_settings_patch_list = {}

# handleIRLedPowerMenu()
# source code line 43
#fix_ir_led_settings_patch_list['set_led_power'] = {}
#fix_ir_led_settings_patch_list['set_led_power']['start_offset'] = 0x010e358
#fix_ir_led_settings_patch_list['set_led_power']['change_from_jump'] = 'jal.set_cold_item_led_power'
#fix_ir_led_settings_patch_list['set_led_power']['change_to_jump']   = 'jal.fils_set_cold_item_led_power'

## Intercept the calls to the set_ir_led_intensity_from_cold_item()
# Cmd_IrLED
# Source line 12
#fix_ir_led_settings_patch_list['cmd_ir_led'] = {}
#fix_ir_led_settings_patch_list['cmd_ir_led']['start_offset'] = 0x00dc4f4
#fix_ir_led_settings_patch_list['cmd_ir_led']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
#fix_ir_led_settings_patch_list['cmd_ir_led']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'
# HceTaskRecording_RecVideoInit
# Source Line 153
#fix_ir_led_settings_patch_list['rec_video_init'] = {}
#fix_ir_led_settings_patch_list['rec_video_init']['start_offset'] = 0x01001e8
#fix_ir_led_settings_patch_list['rec_video_init']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
#fix_ir_led_settings_patch_list['rec_video_init']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'

# HceTaskStill_ToView
# Source Line 29
#fix_ir_led_settings_patch_list['still_to_view'] = {}
#fix_ir_led_settings_patch_list['still_to_view']['start_offset'] = 0x0101778
#fix_ir_led_settings_patch_list['still_to_view']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
#fix_ir_led_settings_patch_list['still_to_view']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'

# TaskStillBurstFSM_still_prev_task1
# Source Line 20
#fix_ir_led_settings_patch_list['burst_still_prev'] = {}
#fix_ir_led_settings_patch_list['burst_still_prev']['start_offset'] = 0x0103684
#fix_ir_led_settings_patch_list['burst_still_prev']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
#fix_ir_led_settings_patch_list['burst_still_prev']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'

## Intercept the calls to set_ir_led_power_pwm(enum_alt_ir_led_intensity alt_ir_led_intensity)
# init_IR_LED()
# Source Line 12
#fix_ir_led_settings_patch_list['hce_ir_led'] = {}
#fix_ir_led_settings_patch_list['hce_ir_led']['start_offset'] = 0x005e420
#fix_ir_led_settings_patch_list['hce_ir_led']['change_from_jump'] = 'jal.set_ir_led_power_pwm'
#fix_ir_led_settings_patch_list['hce_ir_led']['change_to_jump']   = 'jal.fils_set_ir_led_power_pwm'
##
# set_IRLedOn_PwrLvl
# source line 9
#fix_ir_led_settings_patch_list['set_ir_led'] = {}
#fix_ir_led_settings_patch_list['set_ir_led']['start_offset'] = 0x005e380
#fix_ir_led_settings_patch_list['set_ir_led']['change_from_jump'] = 'j.set_ir_led_power_pwm'
#fix_ir_led_settings_patch_list['set_ir_led']['change_to_jump']   = 'j.fils_set_ir_led_power_pwm'


# Intercept smart_IR_log_printf
#fix_ir_led_settings_patch_list['logprintf1'] = {}
#fix_ir_led_settings_patch_list['logprintf1']['start_offset'] = 0x00e
#fix_ir_led_settings_patch_list['logprintf1']['change_from_jump'] = 'jal.debug_print_string'
#fix_ir_led_settings_patch_list['logprintf1']['change_to_jump']   = 'jal.fils_debug_print_string'


##
#fix_ir_led_settings_patch_list['log_sub_printf1'] = {}
#fix_ir_led_settings_patch_list['log_sub_printf1']['start_offset'] = 0x00e
#fix_ir_led_settings_patch_list['log_sub_printf1']['change_from_jump'] = 'jal.debug_print_string'
#fix_ir_led_settings_patch_list['log_sub_printf1']['change_to_jump']   = 'jal.fils_debug_print_string'
