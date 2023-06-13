## A set of hand created binary patches for the BTC-7E-HP5
## To be consumed by codePatcher() functions

## BA Bundle
firmware_bundle_a_patch_list = {}
firmware_bundle_a_patch_list['firmware_ID0'] = {}
firmware_bundle_a_patch_list['firmware_ID0']['start_offset'] = 0x2bba68;
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes'] = bytes("BTC7E_M05100F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']   = bytes("WWL7E_230104A", 'utf-8');

firmware_bundle_a_patch_list['firmware_ID1'] = {}
firmware_bundle_a_patch_list['firmware_ID1']['start_offset'] = 0x2d653c;
firmware_bundle_a_patch_list['firmware_ID1']['change_from_bytes'] = bytes("BTC7E_M05100F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes']   = bytes("WWL7E_230104A", 'utf-8');


############# BUNDLE A Patches ################################
#
# Rewrite the call that sprintf()'s the string to the bottom of the ribbon
#    in screenPrintReplayHeaderRibbons() at 0x800269d8
#    so that at 0x80026b08
#    so that it calls a custom sprintf function we just created at 0x80066ab8
#    instead of to "local_sprintf" at 0x80362354
custom_ribbon_patch_list = {}
custom_ribbon_patch_list['Custom_Ribbon'] = {}
custom_ribbon_patch_list['Custom_Ribbon']['start_offset'] = 0x00111980
custom_ribbon_patch_list['Custom_Ribbon']['change_from_jump'] = 'jal.local_sprintf'
custom_ribbon_patch_list['Custom_Ribbon']['change_to_jump'] = 'jal.wbwl_custom_ribbon_sprintf'
# this in HandleReplayMenuVideo; source line 27
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset'] = 0x001122dc
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['change_from_jump'] = 'j.draw_video_scroll_bar'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['change_to_jump'] = 'j.ld_draw_video_scroll_bar'
# this in HandleReplayMenuVideo; source line 78
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset'] = 0x0011222c
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['change_from_jump'] = 'jal.draw_video_scroll_bar'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['change_to_jump'] = 'jal.ld_draw_video_scroll_bar'
# this in HandleReplayMenuVideo; source line 34
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook'] = {}
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset'] = 0x00112030
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['change_from_jump'] = 'jal.draw_rectangle_wrapper'
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['change_to_jump'] = 'jal.ld_clear_video_scroll_bar'



# eliminate the limit check on night time video length by
#   nulling out the store that sets video length to 20 seconds if IR LED on
#   this allows the ribbon display to properly record remaining video lenght
#   special case in HceTaskRecording_RecVideoIniit()
#   replace the code that would otherwise limit the video to 20 seconds with a NOOP
#   ~source line 142
night_video_limit_patch_list = {}
night_video_limit_patch_list['No_Video_Limit_Store'] = {}
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset'] = 0x00100140
night_video_limit_patch_list['No_Video_Limit_Store']['change_from_bytes'] = bytes([0x14,0x00,0x02,0x24])
night_video_limit_patch_list['No_Video_Limit_Store']['change_to_bytes']   = bytes([0x00,0x00,0x00,0x00])

#
# custom_info_strip patch
# HceStampDraw_draw_info_bar
# ~Source code line 71
custom_info_strip_patch_list = {}
custom_info_strip_patch_list['date_local_sprintf'] = {}
custom_info_strip_patch_list['date_local_sprintf']['start_offset'] = 0x00fa4b0
custom_info_strip_patch_list['date_local_sprintf']['change_from_jump'] = 'jal.local_sprintf'
custom_info_strip_patch_list['date_local_sprintf']['change_to_jump']   = 'jal.wbwl_custom_info_strip_date_sprintf'
# HceStampDraw_draw_info_bar
# ~Source code line 84
custom_info_strip_patch_list['time_local_sprintf'] = {}
custom_info_strip_patch_list['time_local_sprintf']['start_offset'] = 0x00fa508
custom_info_strip_patch_list['time_local_sprintf']['change_from_jump'] = 'jal.local_sprintf'
custom_info_strip_patch_list['time_local_sprintf']['change_to_jump']   = 'jal.wbwl_custom_info_strip_time_sprintf'
# HceStampDraw_draw_info_bar
# ~Source code line 108
custom_info_strip_patch_list['last_strlen'] = {}
custom_info_strip_patch_list['last_strlen']['start_offset'] = 0x00fa624
custom_info_strip_patch_list['last_strlen']['change_from_jump'] = 'jal.btc_strlen'
custom_info_strip_patch_list['last_strlen']['change_to_jump']   = 'jal.wbwl_custom_info_strip_strlen'
# Intercept calls to draw logo on info strip ("stamp")
# HceStillStampCB
# ~Source code line 99
custom_info_strip_patch_list['still_logo'] = {}
custom_info_strip_patch_list['still_logo']['start_offset'] = 0x00fabe4
custom_info_strip_patch_list['still_logo']['change_from_jump'] = 'jal.HceStampDrawLogo'
custom_info_strip_patch_list['still_logo']['change_to_jump']   = 'jal.wbwl_StampDrawLogo'
# HceVideoStampUpdate
# ~Source code line 18
custom_info_strip_patch_list['video_logo'] = {}
custom_info_strip_patch_list['video_logo']['start_offset'] = 0x00fa0b0
custom_info_strip_patch_list['video_logo']['change_from_jump'] = 'jal.HceStampDrawLogo'
custom_info_strip_patch_list['video_logo']['change_to_jump']   = 'jal.wbwl_StampDrawLogo'

# HceStampLoadFont
# Reduce the Height and Width of the ICON font by a factor of 2
#        this is done early, and insures all the downstream settings
#        are correct.  The only thing you have to do is *also* display
#        the logo at half scale. 
# Line 16
custom_info_strip_patch_list['load_font_width'] = {}
custom_info_strip_patch_list['load_font_width']['start_offset'] = 0x00f81ac
custom_info_strip_patch_list['load_font_width']['change_from_bytes'] = bytes([0x30,0x00,0x02,0x24])
custom_info_strip_patch_list['load_font_width']['change_to_bytes']   = bytes([0x16,0x00,0x02,0x24])
# Line 17
custom_info_strip_patch_list['load_font_width'] = {}
custom_info_strip_patch_list['load_font_width']['start_offset'] = 0x00f81b0
custom_info_strip_patch_list['load_font_width']['change_from_bytes'] = bytes([0x60,0x00,0x03,0x24])
custom_info_strip_patch_list['load_font_width']['change_to_bytes']   = bytes([0x30,0x00,0x03,0x24])


#
# volume and file naming patches
# in Init_DCF
vfn_patch_list = {}
vfn_patch_list['fatVolLabSet'] = {}
vfn_patch_list['fatVolLabSet']['start_offset'] = 0x000fcd50
vfn_patch_list['fatVolLabSet']['change_from_jump'] = 'jal.fatVolLabSet_wrapper'
vfn_patch_list['fatVolLabSet']['change_to_jump']   = 'jal.wbwl_fatVolLabSet'
# in HceMedia_PreInitDCFFS
# Line 12
vfn_patch_list['dir_file_fix0'] = {}
vfn_patch_list['dir_file_fix0']['start_offset'] = 0x00ed8f0
vfn_patch_list['dir_file_fix0']['change_from_jump'] = 'jal.btc_init_directory_suffix_file_prefix'
vfn_patch_list['dir_file_fix0']['change_to_jump']   = 'jal.wbwl_init_directory_suffix_file_prefix'
# in another_media_init
vfn_patch_list['dir_file_fix1'] = {}
vfn_patch_list['dir_file_fix1']['start_offset'] = 0x00ece5c
vfn_patch_list['dir_file_fix1']['change_from_jump'] = 'jal.btc_init_directory_suffix_file_prefix'
vfn_patch_list['dir_file_fix1']['change_to_jump']   = 'jal.wbwl_init_directory_suffix_file_prefix'


#
# (debug) utilities
# Hce_FWFileChk
# source code line 46
utilities_patch_list = {}
utilities_patch_list['tty_flush'] = {}
utilities_patch_list['tty_flush']['start_offset'] = 0x0105a98
utilities_patch_list['tty_flush']['change_from_jump'] = 'jal.check_post_printf_state_set_sio_params'
utilities_patch_list['tty_flush']['change_to_jump']   = 'jal.utilities_check_post_printf_hook'

# handleLanguage_menu
# source code line 36
utilities_patch_list = {}
utilities_patch_list['tty_flush'] = {}
utilities_patch_list['tty_flush']['start_offset'] = 0x010d4f0
utilities_patch_list['tty_flush']['change_from_jump'] = 'jal.set_cold_item_language_id'
utilities_patch_list['tty_flush']['change_to_jump']   = 'jal.util_set_cold_item_language_id'

############# DSLR Trigger Patches ############################

# Patch to enable dslr trigger (w/o battery monitor)
# in rapidFirePhotos
# Source line number 11
dslr_trigger_patch_list = {}
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook'] = {}
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook']['start_offset'] = 0x000e7cec
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook']['change_from_jump'] = 'jal.tty_printf'
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook']['change_to_jump'] = 'jal.dt_RapidFirePhotos_printf_hook'
# HceTaskRecording_RecVideoToRec1
# Source code line 78
dslr_trigger_patch_list['dt_video_log_printf_hook'] = {}
dslr_trigger_patch_list['dt_video_log_printf_hook']['start_offset'] = 0x000fe8f4
dslr_trigger_patch_list['dt_video_log_printf_hook']['change_from_jump'] = 'jal.log_printf'
dslr_trigger_patch_list['dt_video_log_printf_hook']['change_to_jump'] = 'jal.dt_video_log_printf_hook'
# in HceTaskStill_End
# source line number 18
dslr_trigger_patch_list['dt_burst_mode_off_hook'] = {}
dslr_trigger_patch_list['dt_burst_mode_off_hook']['start_offset'] = 0x001006cc
dslr_trigger_patch_list['dt_burst_mode_off_hook']['change_from_jump']  = 'jal.IRLedOff'
dslr_trigger_patch_list['dt_burst_mode_off_hook']['change_to_jump'] = 'jal.dt_off_photo_burst_hook'
# in TaskRecording_FSM_task9
# Source code Line 71
dslr_trigger_patch_list['dt_video_off_hook'] = {}
dslr_trigger_patch_list['dt_video_off_hook']['start_offset'] = 0x000fe6c8
dslr_trigger_patch_list['dt_video_off_hook']['change_from_jump']  = 'jal.IRLedOff'
dslr_trigger_patch_list['dt_video_off_hook']['change_to_jump'] = 'jal.dt_video_off_hook'

##################################################################################
# Patches for creating new menu(s)
#    - menu_handler_function_array
#    - menu_item_array
menus_patch_list = {}

# Splice in call to our new lookup table
#    - correct check on array size
#    - change argument from pointer to an index
#    - splice in call to our execute function
# in HceTaskMenuMultiItem
# line 23
menus_patch_list['menu_function_count'] = {}
menus_patch_list['menu_function_count']['start_offset'] = 0x010ca44
menus_patch_list['menu_function_count']['change_from_bytes'] = bytes([0x20, 0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_to_bytes']   = bytes([0x24, 0x00, 0x42, 0x2c])
# Line 28
# replace lw a0,0x0(v0)=> ->handleInit_menu  // g_menu_handler_function_array[index]
# with    lw a0,v0                           // index
menus_patch_list['index_argument'] = {}
menus_patch_list['index_argument']['start_offset'] = 0x010ca58
menus_patch_list['index_argument']['change_from_bytes'] = bytes([0x00, 0x00, 0x44, 0x8c])
menus_patch_list['index_argument']['change_to_bytes']   = bytes([0x00, 0x20, 0x40, 0x80])
# Line 28
# replace call to execute_if_not_null
menus_patch_list['execute_func'] = {}
menus_patch_list['execute_func']['start_offset'] = 0x010ca5c
menus_patch_list['execute_func']['change_from_jump'] = 'jal.execute_if_not_null'
menus_patch_list['execute_func']['change_to_jump'] = 'jal.menus_execute_if_not_null'

# in g_main_menu_selector_array
#    replace first entry @ 0x802c9e68 g_camera_setup_menu_item_array
#			     w/         g_wbwl_camera_setup_menu_item_array
menus_patch_list['setup_items_pointer'] = {}
menus_patch_list['setup_items_pointer']['start_offset'] = 0x02c9e68
menus_patch_list['setup_items_pointer']['change_from_ptr'] = 'g_camera_setup_menu_item_array'
menus_patch_list['setup_items_pointer']['change_to_ptr'] = 'g_wbwl_camera_setup_menu_item_array'
#    replace second @ 0x802c9e6c  which is  0x1a (26)
#                                w/         0x1e (30) 
menus_patch_list['setup_items_number'] = {}
menus_patch_list['setup_items_number']['start_offset'] = 0x02c9e6c
menus_patch_list['setup_items_number']['change_from_bytes'] = bytes([0x1a, 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_to_bytes'] = bytes([0x1e, 0x00, 0x00, 0x00])

# in handleCameraSetup_menu()
# line 34 - 37
# Hijack call so that we can point to the larger array
menus_patch_list['handleCameraSetup'] = {}
menus_patch_list['handleCameraSetup']['start_offset'] = 0x010cf0c
menus_patch_list['handleCameraSetup']['change_from_jump'] = 'jal.get_next_state_from_menu_enter'
menus_patch_list['handleCameraSetup']['change_to_jump'] = 'jal.wbwl_get_next_state_from_menu_enter'

# 
# in handleSDManagement_menu
# line 14
# Hijack call so that we can use other bits in this byte
menus_patch_list['getSDManagement'] = {}
menus_patch_list['getSDManagement']['start_offset'] = 0x010d598
menus_patch_list['getSDManagement']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
menus_patch_list['getSDManagement']['change_to_jump'] = 'jal.evsd_get_cold_item_sd_management_p'

# 
# in handleSDManagement_menu
# line 43
# Hijack call so that we can use other bits in this byte
menus_patch_list['setSDManagement'] = {}
menus_patch_list['setSDManagement']['start_offset'] = 0x010d6c4
menus_patch_list['setSDManagement']['change_from_jump'] = 'jal.set_cold_item_sd_management_p'
menus_patch_list['setSDManagement']['change_to_jump'] = 'jal.evsd_set_cold_item_sd_management_p'

#### a whole bunch of hacks to point to a new "end state" in the g_wbwl_HceTaskMenuMultiItem_fsm_function_array
# in handleMainMenu_menu()
# 51
menus_patch_list['handle_main_menu'] = {}
menus_patch_list['handle_main_menu']['start_offset'] = 0x010d0e8
menus_patch_list['handle_main_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleCameraSetup_menu(void)
# 51
menus_patch_list['handle_camera_setup_menu'] = {}
menus_patch_list['handle_camera_setup_menu']['start_offset'] = 0x010cf58
menus_patch_list['handle_camera_setup_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handlePlayback_menu(void)
# 20
menus_patch_list['handle_playback_menu'] = {}
menus_patch_list['handle_playback_menu']['start_offset'] = 0x010fda4
menus_patch_list['handle_playback_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleHandleSetTimeMenu(void)
# 94
menus_patch_list['handle_set_time_menu'] = {}
menus_patch_list['handle_set_time_menu']['start_offset'] = 0x0111510
menus_patch_list['handle_set_time_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# handleOperationMode_menu
# 56
menus_patch_list['operation_mode_menu'] = {}
menus_patch_list['operation_mode_menu']['start_offset'] = 0x010fcb8
menus_patch_list['operation_mode_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# handlePhotoQuality_menu
# 56
menus_patch_list['photo_quality_menu'] = {}
menus_patch_list['photo_quality_menu']['start_offset'] = 0x010fab8
menus_patch_list['photo_quality_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])

# in handleVideoLength_menu()
# 56
menus_patch_list['video_length_menu'] = {}
menus_patch_list['video_length_menu']['start_offset'] = 0x010f8ec
menus_patch_list['video_length_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])

# in handleVideoQuality_menu()
# 56
menus_patch_list['video_quality_menu'] = {}
menus_patch_list['video_quality_menu']['start_offset'] = 0x010f720
menus_patch_list['video_quality_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handlePhotoDelay_menu()
# 51
menus_patch_list['photo_delay_menu'] = {}
menus_patch_list['photo_delay_menu']['start_offset'] = 0x010f550
menus_patch_list['photo_delay_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleMultiShotMode_menu()
# 56
menus_patch_list['multishot_menu'] = {}
menus_patch_list['multishot_menu']['start_offset'] = 0x010f370
menus_patch_list['multishot_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleHDR_menu()
# 76
menus_patch_list['HDR_menu'] = {}
menus_patch_list['HDR_menu']['start_offset'] = 0x010f17c
menus_patch_list['HDR_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['HDR_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleTempUnit_menu()
# 56
menus_patch_list['temp_unit_menu'] = {}
menus_patch_list['temp_unit_menu']['start_offset'] = 0x010eee8
menus_patch_list['temp_unit_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleCameraName_menu()
# 60
menus_patch_list['camera_name_menu'] = {}
menus_patch_list['camera_name_menu']['start_offset'] = 0x0110a0c
menus_patch_list['camera_name_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleImageDataStrip_menu()
# 56
menus_patch_list['info_strip_menu'] = {}
menus_patch_list['info_strip_menu']['start_offset'] = 0x010ed1c
menus_patch_list['info_strip_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleMotionTest_menu()
# 76
menus_patch_list['motion_test_menu'] = {}
menus_patch_list['motion_test_menu']['start_offset'] = 0x010eb4c
menus_patch_list['motion_test_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handlePIRRange_menu()
# 54
menus_patch_list['pir_range_menu'] = {}
menus_patch_list['pir_range_menu']['start_offset'] = 0x010e880
menus_patch_list['pir_range_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleBatteryType_menu()
# 59
menus_patch_list['battery_type_menu'] = {}
menus_patch_list['battery_type_menu']['start_offset'] = 0x010e698
menus_patch_list['battery_type_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleTriggerSpeed_menu()
# 57
menus_patch_list['trigger_speed_menu'] = {}
menus_patch_list['trigger_speed_menu']['start_offset'] = 0x010e4c0
menus_patch_list['trigger_speed_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleRestoreDefault_menu()
# 58
menus_patch_list['restore_default_menu'] = {}
menus_patch_list['restore_default_menu']['start_offset'] = 0x010e2f0
menus_patch_list['restore_default_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleTimelapseFreq_menu()
# 56
menus_patch_list['timelapse_freq_menu'] = {}
menus_patch_list['timelapse_freq_menu']['start_offset'] = 0x010e2f0
menus_patch_list['timelapse_freq_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleTimelapsePeriod_menu()
# 56
menus_patch_list['timelapse_period_menu'] = {}
menus_patch_list['timelapse_period_menu']['start_offset'] = 0x010df50
menus_patch_list['timelapse_period_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in handleDeleteAll_menu()
# 103
menus_patch_list['delete_all_menu'] = {}
menus_patch_list['delete_all_menu']['start_offset'] = 0x010dd84
menus_patch_list['delete_all_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleIRLedPower_menu()
# 57
menus_patch_list['ir_led_power_menu'] = {}
menus_patch_list['ir_led_power_menu']['start_offset'] = 0x010dab8
menus_patch_list['ir_led_power_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleSmartIRVideo_menu()
# 57
menus_patch_list['smart_ir_video_menu'] = {}
menus_patch_list['smart_ir_video_menu']['start_offset'] = 0x010d8e8
menus_patch_list['smart_ir_video_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleSDManagement_menu()
# 57
menus_patch_list['sd_management_menu'] = {}
menus_patch_list['sd_management_menu']['start_offset'] = 0x010d718
menus_patch_list['sd_management_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleLanguage_menu()
# 51
menus_patch_list['language_menu'] = {}
menus_patch_list['language_menu']['start_offset'] = 0x010d718
menus_patch_list['language_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleCaptureTimerP_menu()
# 61
menus_patch_list['capture_timer_menu'] = {}
menus_patch_list['capture_timer_menu']['start_offset'] = 0x010d370
menus_patch_list['capture_timer_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleCaptureTimerP_menu()
# 119
menus_patch_list['set_capture_timer_menu'] = {}
menus_patch_list['set_capture_timer_menu']['start_offset'] = 0x0111104
menus_patch_list['set_capture_timer_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])
# in  handleFirmwareUpgrade_menu()
# 74
menus_patch_list['firmware_upgrade_menu'] = {}
menus_patch_list['firmware_upgrade_menu']['start_offset'] = 0x010cdbc
menus_patch_list['firmware_upgrade_menu']['change_from_bytes'] = bytes([0x1f, 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']   = bytes([0x24, 0x00, 0x04, 0x24])


##################################################################
## Extended SD Card power
# HceTaskRecording_RecVideoEnd
# source code line 74
extended_SD_power_patch_list = {}
extended_SD_power_patch_list['extend_video'] = {}
extended_SD_power_patch_list['extend_video']['start_offset'] = 0x00fe218
extended_SD_power_patch_list['extend_video']['change_from_jump'] = 'jal.check_remaining_sd_capacity'
extended_SD_power_patch_list['extend_video']['change_to_jump']   = 'jal.evsd_check_remaining_sd_capacity'
#
# HceTaskStill_End
# source code line 56
extended_SD_power_patch_list['extend_still'] = {}
extended_SD_power_patch_list['extend_still']['start_offset'] = 0x01007b8
extended_SD_power_patch_list['extend_still']['change_from_jump'] = 'jal.check_remaining_sd_capacity'
extended_SD_power_patch_list['extend_still']['change_to_jump']   = 'jal.evsd_check_remaining_sd_capacity'

# HcePower_CommonPowerOff
# line 24
extended_SD_power_patch_list['power_off'] = {}
extended_SD_power_patch_list['power_off']['start_offset'] = 0x00eb2f4
extended_SD_power_patch_list['power_off']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['power_off']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# still_MCUApp_ResetPIRPin
# line 68
extended_SD_power_patch_list['reset_PIR_pin'] = {}
extended_SD_power_patch_list['reset_PIR_pin']['start_offset'] = 0x00fe410
extended_SD_power_patch_list['reset_PIR_pin']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['reset_PIR_pin']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# TaskRecording_FSM_task10
# line 46
extended_SD_power_patch_list['recording_task9'] = {}
extended_SD_power_patch_list['recording_task9']['start_offset'] = 0x00fe618
extended_SD_power_patch_list['recording_task9']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['recording_task9']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# HceTaskStill_End
# line 52
extended_SD_power_patch_list['still_end'] = {}
extended_SD_power_patch_list['still_end']['start_offset'] = 0x01007a0
extended_SD_power_patch_list['still_end']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['still_end']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# HceTaskStillBurst_End
# line 44
extended_SD_power_patch_list['still_burst_end'] = {}
extended_SD_power_patch_list['still_burst_end']['start_offset'] = 0x0102830
extended_SD_power_patch_list['still_burst_end']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['still_burst_end']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# HceTaskTimeLapse_WaitMountSD
# line 12
extended_SD_power_patch_list['timelapse_sd'] = {}
extended_SD_power_patch_list['timelapse_sd']['start_offset'] = 0x0104f28
extended_SD_power_patch_list['timelapse_sd']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['timelapse_sd']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
# handleSDManagement_menu
# slightly different -- this is for highlighting menu item -- it gets the full encoding
# line 14
extended_SD_power_patch_list['sd_management_menu'] = {}
extended_SD_power_patch_list['sd_management_menu']['start_offset'] = 0x010d598
extended_SD_power_patch_list['sd_management_menu']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
extended_SD_power_patch_list['sd_management_menu']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'

################# Short Range Sensitivity Patches ###########################
## Intercept calls required to expand PIR range to include a "short range" option

short_range_pir_patch_list = {}

# Intercepts setting cold item
# handlePIRRangeMenu
# source line 37
#short_range_pir_patch_list['set_cold_item'] = {}
#short_range_pir_patch_list['set_cold_item']['start_offset'] = 0x010e820
#short_range_pir_patch_list['set_cold_item']['change_from_jump'] = 'jal.set_cold_item_pir_range'
#short_range_pir_patch_list['set_cold_item']['change_to_jump']   = 'jal.lps_set_cold_item_pir_range'

# creating new menu items
# in g_main_menu_item_array[13]
#
short_range_pir_patch_list['menu_item_array'] = {}
short_range_pir_patch_list['menu_item_array']['start_offset'] = 0x002c9ca0
short_range_pir_patch_list['menu_item_array']['change_from_ptr'] = 'g_pir_range_menu'
short_range_pir_patch_list['menu_item_array']['change_to_ptr']   = 'g_lps_pir_range_menu'

short_range_pir_patch_list['menu_item_count'] = {}
short_range_pir_patch_list['menu_item_count']['start_offset'] = 0x02c9ca4
short_range_pir_patch_list['menu_item_count']['change_from_bytes'] = bytes([0x03, 0x00, 0x00, 0x00])
short_range_pir_patch_list['menu_item_count']['change_to_bytes']   = bytes([0x04, 0x00, 0x00, 0x00])

# Intercepts of "set_pir_sensor_range"
# HcePower_CommonPowerOff
# source 28
short_range_pir_patch_list['power_off'] = {}
short_range_pir_patch_list['power_off']['start_offset'] = 0x00eb314
short_range_pir_patch_list['power_off']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['power_off']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'
# HcePower_CommonPowerOn
# source 74
short_range_pir_patch_list['power_on'] = {}
short_range_pir_patch_list['power_on']['start_offset'] = 0x010a6d8
short_range_pir_patch_list['power_on']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['power_on']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'
# handlePIRRangeMenu
# source 38
short_range_pir_patch_list['pir_menu'] = {}
short_range_pir_patch_list['pir_menu']['start_offset'] = 0x010e828
short_range_pir_patch_list['pir_menu']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['pir_menu']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'
# HceTask_WaitPIRTaskEnd
# source 11
short_range_pir_patch_list['pir_task_end'] = {}
short_range_pir_patch_list['pir_task_end']['start_offset'] = 0x0112754
short_range_pir_patch_list['pir_task_end']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['pir_task_end']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'
# TaskPIRTest_FSM_init_task0
# 13
short_range_pir_patch_list['pir_test'] = {}
short_range_pir_patch_list['pir_test']['start_offset'] = 0x01134b0
short_range_pir_patch_list['pir_test']['change_from_jump'] = 'jal.set_pir_sensor_range'
short_range_pir_patch_list['pir_test']['change_to_jump']   = 'jal.lps_set_pir_sensor_range'



################# Fix IR LED Settings Patches ##############################
## Fix the IR LED setting
fix_ir_led_settings_patch_list = {}

# handleIRLedPowerMenu()
# source code line 42
#fix_ir_led_settings_patch_list['set_led_power'] = {}
#fix_ir_led_settings_patch_list['set_led_power']['start_offset'] = 0x010da64
#fix_ir_led_settings_patch_list['set_led_power']['change_from_jump'] = 'jal.set_cold_item_led_power'
#fix_ir_led_settings_patch_list['set_led_power']['change_to_jump']   = 'jal.fils_set_cold_item_led_power'

## Intercept the calls to the set_ir_led_intensity_from_cold_item()
# Cmd_IrLED
# Source line 12
#fix_ir_led_settings_patch_list['cmd_ir_led'] = {}
#fix_ir_led_settings_patch_list['cmd_ir_led']['start_offset'] = 0x00dc558
#fix_ir_led_settings_patch_list['cmd_ir_led']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
#fix_ir_led_settings_patch_list['cmd_ir_led']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'
# HceTaskRecording_RecVideoInit
# Source Line 153
#fix_ir_led_settings_patch_list['rec_video_init'] = {}
#fix_ir_led_settings_patch_list['rec_video_init']['start_offset'] = 0x0100184
#fix_ir_led_settings_patch_list['rec_video_init']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
#fix_ir_led_settings_patch_list['rec_video_init']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'

# HceTaskStill_ToView
# Source Line 28
#fix_ir_led_settings_patch_list['still_to_view'] = {}
#fix_ir_led_settings_patch_list['still_to_view']['start_offset'] = 0x010171c
#fix_ir_led_settings_patch_list['still_to_view']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
#fix_ir_led_settings_patch_list['still_to_view']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'

# TaskStillBurstFSM_still_prev_task1
# Source Line 20
#fix_ir_led_settings_patch_list['burst_still_prev'] = {}
#fix_ir_led_settings_patch_list['burst_still_prev']['start_offset'] = 0x0103630
#fix_ir_led_settings_patch_list['burst_still_prev']['change_from_jump'] = 'jal.set_ir_led_intensity_from_cold_item'
#fix_ir_led_settings_patch_list['burst_still_prev']['change_to_jump']   = 'jal.fils_set_ir_led_intensity_from_cold_item'

## Intercept the calls to set_ir_led_power_pwm(enum_alt_ir_led_intensity alt_ir_led_intensity)
# HceIRLed_IRPWMInit
# Source Line 46
#fix_ir_led_settings_patch_list['hce_ir_led'] = {}
#fix_ir_led_settings_patch_list['hce_ir_led']['start_offset'] = 0x005e530
#fix_ir_led_settings_patch_list['hce_ir_led']['change_from_jump'] = 'jal.set_ir_led_power_pwm'
#fix_ir_led_settings_patch_list['hce_ir_led']['change_to_jump']   = 'jal.fils_set_ir_led_power_pwm'
##
# set_IRLedOn_PwrLvl
# source line 9
#fix_ir_led_settings_patch_list['set_ir_led'] = {}
#fix_ir_led_settings_patch_list['set_ir_led']['start_offset'] = 0x005e3b0
#fix_ir_led_settings_patch_list['set_ir_led']['change_from_jump'] = 'j.set_ir_led_power_pwm'
#fix_ir_led_settings_patch_list['set_ir_led']['change_to_jump']   = 'j.fils_set_ir_led_power_pwm'


# Intercept smart_IR_log_printf
fix_ir_led_settings_patch_list['logprintf1'] = {}
fix_ir_led_settings_patch_list['logprintf1']['start_offset'] = 0x00ec2a0
fix_ir_led_settings_patch_list['logprintf1']['change_from_jump'] = 'jal.debug_print_string'
fix_ir_led_settings_patch_list['logprintf1']['change_to_jump']   = 'jal.fils_debug_print_string'


##
fix_ir_led_settings_patch_list['log_sub_printf1'] = {}
fix_ir_led_settings_patch_list['log_sub_printf1']['start_offset'] = 0x00ec2a0
fix_ir_led_settings_patch_list['log_sub_printf1']['change_from_jump'] = 'jal.debug_print_string'
fix_ir_led_settings_patch_list['log_sub_printf1']['change_to_jump']   = 'jal.fils_debug_print_string'
