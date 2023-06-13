## A set of hand created binary patches for the BTC-7A.
## To be consumed by codePatcher() functions
    

##
# Patches required to convert BTC-7A to "white flash"
#    Disable "black and white mode"
#    Disable the IR_CUT (filter motor)
##

# Firmware Version Patch
# Overrides the factory firmware string with one that encodes customization

firmware_wf_e_cr_nv_patch_list = {}
firmware_wf_e_cr_nv_patch_list['firmware_ID'] = {}
firmware_wf_e_cr_nv_patch_list['firmware_ID']['start_offset'] = 0x39e740
firmware_wf_e_cr_nv_patch_list['firmware_ID']['change_from_bytes'] = bytes("BTC7A_I04030C", 'utf-8');
firmware_wf_e_cr_nv_patch_list['firmware_ID']['change_to_bytes']   = bytes("wfecrnv      ", 'utf-8');

firmware_wf_e_cr_nv_20s_patch_list = {}
firmware_wf_e_cr_nv_20s_patch_list['firmware_ID'] = {}
firmware_wf_e_cr_nv_20s_patch_list['firmware_ID']['start_offset'] = 0x39e740
firmware_wf_e_cr_nv_20s_patch_list['firmware_ID']['change_from_bytes'] = bytes("BTC7A_I04030C", 'utf-8');
firmware_wf_e_cr_nv_20s_patch_list['firmware_ID']['change_to_bytes']   = bytes("wfecrnv20s   ", 'utf-8');

firmware_wf_d_cr_nv_20s_patch_list = {}
firmware_wf_d_cr_nv_20s_patch_list['firmware_ID'] = {}
firmware_wf_d_cr_nv_20s_patch_list['firmware_ID']['start_offset'] = 0x39e740
firmware_wf_d_cr_nv_20s_patch_list['firmware_ID']['change_from_bytes'] = bytes("BTC7A_I04030C", 'utf-8');
firmware_wf_d_cr_nv_20s_patch_list['firmware_ID']['change_to_bytes']   = bytes("wfdcrnv20s   ", 'utf-8');

firmware_cr_nv_patch_list = {}
firmware_cr_nv_patch_list['firmware_ID'] = {}
firmware_cr_nv_patch_list['firmware_ID']['start_offset'] = 0x39e740
firmware_cr_nv_patch_list['firmware_ID']['change_from_bytes'] = bytes("BTC7A_I04030C", 'utf-8');
firmware_cr_nv_patch_list['firmware_ID']['change_to_bytes']   = bytes("crnv         ", 'utf-8');

firmware_cr_nv_dslr_patch_list = {}
firmware_cr_nv_dslr_patch_list['firmware_ID'] = {}
firmware_cr_nv_dslr_patch_list['firmware_ID']['start_offset'] = 0x39e740
firmware_cr_nv_dslr_patch_list['firmware_ID']['change_from_bytes'] = bytes("BTC7A_I04030C", 'utf-8');
firmware_cr_nv_dslr_patch_list['firmware_ID']['change_to_bytes']   = bytes("crnvdslr     ", 'utf-8');

firmware_wf_e_cr_nv_dslr_patch_list = {}
firmware_wf_e_cr_nv_dslr_patch_list['firmware_ID'] = {}
firmware_wf_e_cr_nv_dslr_patch_list['firmware_ID']['start_offset'] = 0x39e740
firmware_wf_e_cr_nv_dslr_patch_list['firmware_ID']['change_from_bytes'] = bytes("BTC7A_I04030C", 'utf-8');
firmware_wf_e_cr_nv_dslr_patch_list['firmware_ID']['change_to_bytes']   = bytes("wfecrnvdslr  ", 'utf-8');

firmware_bm_wf_e_cr_nv_patch_list = {}
firmware_bm_wf_e_cr_nv_patch_list['firmware_ID'] = {}
firmware_bm_wf_e_cr_nv_patch_list['firmware_ID']['start_offset'] = 0x39e740
firmware_bm_wf_e_cr_nv_patch_list['firmware_ID']['change_from_bytes'] = bytes("BTC7A_I04030C", 'utf-8');
firmware_bm_wf_e_cr_nv_patch_list['firmware_ID']['change_to_bytes']   = bytes("bmwfecrnv    ", 'utf-8');

firmware_bm_wf_e_cr_nv_dslr_patch_list = {}
firmware_bm_wf_e_cr_nv_dslr_patch_list['firmware_ID'] = {}
firmware_bm_wf_e_cr_nv_dslr_patch_list['firmware_ID']['start_offset'] = 0x39e740
firmware_bm_wf_e_cr_nv_dslr_patch_list['firmware_ID']['change_from_bytes'] = bytes("BTC7A_I04030C", 'utf-8');
firmware_bm_wf_e_cr_nv_dslr_patch_list['firmware_ID']['change_to_bytes']   = bytes("bmwfecrnvdslr", 'utf-8');


# Disable the digital_effect_BW mode by substituting pointer to color mode
#   into switch table.

digital_effect_patch_list = {}
digital_effect_patch_list['Digital_Mode_Disable_BW'] = {}
digital_effect_patch_list['Digital_Mode_Disable_BW']['start_offset'] = 0x375e1c
digital_effect_patch_list['Digital_Mode_Disable_BW']['change_from_bytes'] = bytes([0x28, 0x68, 0x06, 0x80])
digital_effect_patch_list['Digital_Mode_Disable_BW']['change_to_bytes']   = bytes([0xa0, 0x65, 0x06, 0x80])

# rewrite argument to IR_CUT routine
ir_cut_disable_config_patch_list = {}
ir_cut_disable_config_patch_list['IR_CUT_Disable_Config'] = {}
ir_cut_disable_config_patch_list['IR_CUT_Disable_Config']['start_offset'] = 0x000944c
ir_cut_disable_config_patch_list['IR_CUT_Disable_Config']['change_from_bytes'] = bytes([0x21, 0x20, 0x00, 0x00])
ir_cut_disable_config_patch_list['IR_CUT_Disable_Config']['change_to_bytes']   = bytes([0x01, 0x00, 0x04, 0x24])

# rewrite argument to IR_CUT routine
ir_cut_disable_on_wake_patch_list = {}
ir_cut_disable_on_wake_patch_list['IR_CUT_Disable_On_Wake'] = {}
ir_cut_disable_on_wake_patch_list['IR_CUT_Disable_On_Wake']['start_offset'] = 0x00093ec
ir_cut_disable_on_wake_patch_list['IR_CUT_Disable_On_Wake']['change_from_bytes'] = bytes([0x21, 0x20, 0x00, 0x00])
ir_cut_disable_on_wake_patch_list['IR_CUT_Disable_On_Wake']['change_to_bytes']   = bytes([0x01, 0x00, 0x04, 0x24])

# Redirect call to setSensorDigitalEffectDayNight
#   so that it goes to cp_setSensorDigitalEffectDayNight
white_flash_awb_patch_list = {}

white_flash_awb_patch_list['setSensorDigitalEffectPhoto'] = {}
white_flash_awb_patch_list['setSensorDigitalEffectPhoto']['start_offset'] = 0x0000fbdc
white_flash_awb_patch_list['setSensorDigitalEffectPhoto']['change_from_bytes'] = bytes([0xd0, 0xff, 0xbd, 0x27])
white_flash_awb_patch_list['setSensorDigitalEffectPhoto']['change_to_jump'] = 'j.cp_setSensorDigitalEffectPhoto'

#   so that it goes to cp_setSensorDigitalEffectDayNight
white_flash_awb_patch_list['setSensorDigitalEffectDayVideo'] = {}
white_flash_awb_patch_list['setSensorDigitalEffectDayVideo']['start_offset'] = 0x0000ff58
white_flash_awb_patch_list['setSensorDigitalEffectDayVideo']['change_from_bytes'] = bytes([0xd0, 0xff, 0xbd, 0x27])
white_flash_awb_patch_list['setSensorDigitalEffectDayVideo']['change_to_jump'] = 'j.cp_setSensorDigitalEffectVideo'

# eliminate the limit check on night time video length by
#   nulling out the store that sets video length to 20 seconds if IR LED on
#   this allows the ribbon display to properly record remaining video lenght
night_video_limit_patch_list = {}
night_video_limit_patch_list['No_Video_Limit_Store'] = {}
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset'] = 0x0020dd4
night_video_limit_patch_list['No_Video_Limit_Store']['change_from_bytes'] = bytes([0x1a,0x00,0x22,0xa6])
night_video_limit_patch_list['No_Video_Limit_Store']['change_to_bytes']   = bytes([0x00,0x00,0x00,0x00])

# this sets the maximum length for a video under IR LED illumination to 300 seconds (5 minutes)
night_video_limit_patch_list['End_Video_Limit_Check'] = {}
night_video_limit_patch_list['End_Video_Limit_Check']['start_offset'] = 0x001fbac
night_video_limit_patch_list['End_Video_Limit_Check']['change_from_bytes'] = bytes([0x14,0x00,0x44,0x2c])
night_video_limit_patch_list['End_Video_Limit_Check']['change_to_bytes']   = bytes([0x2c,0x01,0x44,0x2c])

#
hand_patched_white_flash_patch_list = {}
hand_patched_white_flash_patch_list.update(digital_effect_patch_list)
hand_patched_white_flash_patch_list.update(ir_cut_disable_config_patch_list)
hand_patched_white_flash_patch_list.update(ir_cut_disable_on_wake_patch_list)


#
# Rewrite the call that sprintf()'s the string to the bottom of the ribbon
#    in sceenPrintReplayHeaderRibbons() at 0x800269d8
#    so that at 0x80026b08
#    so that it calls a custom sprintf function we just created at 0x80066ab8
#    instead of to "local_sprintf" at 0x80362354
custom_ribbon_patch_list = {}
custom_ribbon_patch_list['Custom_Ribbon'] = {}
custom_ribbon_patch_list['Custom_Ribbon']['start_offset'] = 0x00026b08
custom_ribbon_patch_list['Custom_Ribbon']['change_from_jump'] = 'jal.local_sprintf'
custom_ribbon_patch_list['Custom_Ribbon']['change_to_jump'] = 'jal.wbwl_custom_ribbon_sprintf'
#
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset'] = 0x00027464
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['change_from_jump'] = 'j.draw_video_scroll_bar'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['change_to_jump'] = 'j.ld_draw_video_scroll_bar'
#
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset'] = 0x000273b4
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['change_from_jump'] = 'jal.draw_video_scroll_bar'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['change_to_jump'] = 'jal.ld_draw_video_scroll_bar'
#
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook'] = {}
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset'] = 0x000271b8
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['change_from_jump'] = 'jal.draw_rectangle_wrapper'
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['change_to_jump'] = 'jal.ld_clear_video_scroll_bar'


# Hooks for stateful Battery Monitor functions
battery_monitor_patch_list = {}
#
battery_monitor_patch_list['HceCommon_InitOptions'] = {}
battery_monitor_patch_list['HceCommon_InitOptions']['start_offset'] = 0x00005d5c
battery_monitor_patch_list['HceCommon_InitOptions']['change_from_jump'] = 'jal.HceCommon_RestoreDefaultColdItem'
battery_monitor_patch_list['HceCommon_InitOptions']['change_to_jump'] = 'jal.bm_HceCommon_RestoreDefaultColdItem_hook'
#
battery_monitor_patch_list['handleRestoreDefaultMenu'] = {}
battery_monitor_patch_list['handleRestoreDefaultMenu']['start_offset'] = 0x00023fb4
battery_monitor_patch_list['handleRestoreDefaultMenu']['change_from_jump'] = 'jal.HceCommon_RestoreDefaultColdItem'
battery_monitor_patch_list['handleRestoreDefaultMenu']['change_to_jump'] = 'jal.bm_HceCommon_RestoreDefaultColdItem_hook'
#
battery_monitor_patch_list['reboot_for_changed_power_switch'] = {}
battery_monitor_patch_list['reboot_for_changed_power_switch']['start_offset'] = 0x0002aec4
battery_monitor_patch_list['reboot_for_changed_power_switch']['change_from_jump'] = 'jal.HceCommon_RestoreDefaultColdItem'
battery_monitor_patch_list['reboot_for_changed_power_switch']['change_to_jump'] = 'jal.bm_HceCommon_RestoreDefaultColdItem_hook'
#
battery_monitor_patch_list['bm_user_set_clock_hook'] = {}
battery_monitor_patch_list['bm_user_set_clock_hook']['start_offset'] = 0x000265f0
battery_monitor_patch_list['bm_user_set_clock_hook']['change_from_jump'] = 'jal.hal_set_rtc'
battery_monitor_patch_list['bm_user_set_clock_hook']['change_to_jump'] = 'jal.bm_hal_set_rtc_hook'
#
battery_monitor_patch_list['bm_HceCommon_SetCaptureImage_hook'] = {}
battery_monitor_patch_list['bm_HceCommon_SetCaptureImage_hook']['start_offset'] = 0x0001d424
battery_monitor_patch_list['bm_HceCommon_SetCaptureImage_hook']['change_from_jump'] = 'jal.HceCommon_SetCaptureImag'
battery_monitor_patch_list['bm_HceCommon_SetCaptureImage_hook']['change_to_jump'] = 'jal.bm_HceCommon_SetCaptureImage_hook'
#
battery_monitor_patch_list['bm_RapidFirePhotos_printf_hook'] = {}
battery_monitor_patch_list['bm_RapidFirePhotos_printf_hook']['start_offset'] = 0x0000f884
battery_monitor_patch_list['bm_RapidFirePhotos_printf_hook']['change_from_jump'] = 'jal.tty_printf'
battery_monitor_patch_list['bm_RapidFirePhotos_printf_hook']['change_to_jump'] = 'jal.bm_RapidFirePhotos_printf_hook'
#
battery_monitor_patch_list['bm_video_log_printf_hook'] = {}
battery_monitor_patch_list['bm_video_log_printf_hook']['start_offset'] = 0x0001fe48
battery_monitor_patch_list['bm_video_log_printf_hook']['change_from_jump'] = 'jal.log_printf'
battery_monitor_patch_list['bm_video_log_printf_hook']['change_to_jump'] = 'jal.bm_video_log_printf_hook'
#
battery_monitor_patch_list['bm_get_current_battery_level1'] = {}
battery_monitor_patch_list['bm_get_current_battery_level1']['start_offset'] = 0x0000c2ec
battery_monitor_patch_list['bm_get_current_battery_level1']['change_from_jump'] = 'jal.get_battery_percent_from_voltage'
battery_monitor_patch_list['bm_get_current_battery_level1']['change_to_jump'] = 'jal.bm_get_current_battery_level'
#
battery_monitor_patch_list['bm_get_current_battery_level2'] = {}
battery_monitor_patch_list['bm_get_current_battery_level2']['start_offset'] = 0x0000c648
battery_monitor_patch_list['bm_get_current_battery_level2']['change_from_jump'] = 'jal.get_battery_percent_from_voltage'
battery_monitor_patch_list['bm_get_current_battery_level2']['change_to_jump'] = 'jal.bm_get_current_battery_level'
#
battery_monitor_patch_list['store_pressure_bm_hook'] = {}
battery_monitor_patch_list['store_pressure_bm_hook']['start_offset'] = 0x0000bf54
battery_monitor_patch_list['store_pressure_bm_hook']['change_from_jump'] = 'jal.store_pressure_trend'
battery_monitor_patch_list['store_pressure_bm_hook']['change_to_jump'] = 'jal.store_pressure_bm_hook'
#
battery_monitor_patch_list['bm_Volt_Calib_Bat_hook'] = {}
battery_monitor_patch_list['bm_Volt_Calib_Bat_hook']['start_offset'] = 0x00011b38
battery_monitor_patch_list['bm_Volt_Calib_Bat_hook']['change_from_jump'] = 'jal.Volt_Calib_Bat'
battery_monitor_patch_list['bm_Volt_Calib_Bat_hook']['change_to_jump'] = 'jal.bm_Volt_Calib_Bat_hook'
#
battery_monitor_patch_list['bm_handleBatteryTypeMenu_hook'] = {}
battery_monitor_patch_list['bm_handleBatteryTypeMenu_hook']['start_offset'] = 0x00024204
battery_monitor_patch_list['bm_handleBatteryTypeMenu_hook']['change_from_bytes']  = bytes([0xe0,0xff,0xbd,0x27])
battery_monitor_patch_list['bm_handleBatteryTypeMenu_hook']['change_to_jump'] = 'j.bm_handleBatteryTypeMenu'
#
battery_monitor_patch_list['bm_burst_mode_off_hook'] = {}
battery_monitor_patch_list['bm_burst_mode_off_hook']['start_offset'] = 0x001ce0c
battery_monitor_patch_list['bm_burst_mode_off_hook']['change_from_jump']  = 'jal.IRLedOff'
battery_monitor_patch_list['bm_burst_mode_off_hook']['change_to_jump'] = 'jal.bm_off_photo_burst_hook'
#
battery_monitor_patch_list['bm_video_off_hook'] = {}
battery_monitor_patch_list['bm_video_off_hook']['start_offset'] = 0x0001f7e8
battery_monitor_patch_list['bm_video_off_hook']['change_from_jump']  = 'jal.IRLedOff'
battery_monitor_patch_list['bm_video_off_hook']['change_to_jump'] = 'jal.bm_video_off_hook'


# Hooks for External Trigger
external_trigger_patch_list = {}
#
external_trigger_patch_list['HceCommon_InitOptions'] = {}
external_trigger_patch_list['HceCommon_InitOptions']['start_offset'] = 0x00005d5c
external_trigger_patch_list['HceCommon_InitOptions']['change_from_jump'] = 'jal.HceCommon_RestoreDefaultColdItem'
external_trigger_patch_list['HceCommon_InitOptions']['change_to_jump'] = 'jal.bm_HceCommon_RestoreDefaultColdItem_hook'


# Patch to enable dslr trigger (w/o battery monitor)
dslr_trigger_patch_list = {}
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook'] = {}
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook']['start_offset'] = 0x0000f884
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook']['change_from_jump'] = 'jal.tty_printf'
dslr_trigger_patch_list['dt_RapidFirePhotos_printf_hook']['change_to_jump'] = 'jal.dt_RapidFirePhotos_printf_hook'
#
dslr_trigger_patch_list['dt_video_log_printf_hook'] = {}
dslr_trigger_patch_list['dt_video_log_printf_hook']['start_offset'] = 0x0001fe48
dslr_trigger_patch_list['dt_video_log_printf_hook']['change_from_jump'] = 'jal.log_printf'
dslr_trigger_patch_list['dt_video_log_printf_hook']['change_to_jump'] = 'jal.dt_video_log_printf_hook'
#
dslr_trigger_patch_list['dt_burst_mode_off_hook'] = {}
dslr_trigger_patch_list['dt_burst_mode_off_hook']['start_offset'] = 0x001ce0c
dslr_trigger_patch_list['dt_burst_mode_off_hook']['change_from_jump']  = 'jal.IRLedOff'
dslr_trigger_patch_list['dt_burst_mode_off_hook']['change_to_jump'] = 'jal.dt_off_photo_burst_hook'
#
dslr_trigger_patch_list['dt_video_off_hook'] = {}
dslr_trigger_patch_list['dt_video_off_hook']['start_offset'] = 0x0001f7e8
dslr_trigger_patch_list['dt_video_off_hook']['change_from_jump']  = 'jal.IRLedOff'
dslr_trigger_patch_list['dt_video_off_hook']['change_to_jump'] = 'jal.dt_video_off_hook'



# Patch to Set the Countdown timer from 30 (0x1e) seconds to 20 (0x14) seconds
countdown_timer_patch_list = {}
countdown_timer_patch_list['set_counter_value'] = {}
countdown_timer_patch_list['set_counter_value']['start_offset'] = 0x00028254
countdown_timer_patch_list['set_counter_value']['change_from_bytes'] = bytes([0x1e,0x00,0x02,0x24])
countdown_timer_patch_list['set_counter_value']['change_to_bytes']   = bytes([0x14,0x00,0x02,0x24])



# Hooks for Custom Trail Camera Environment Initalization
ctc_init_patch_list = {}
ctc_init_patch_list['CTC_init_hook'] = {}
ctc_init_patch_list['CTC_init_hook']['start_offset'] = 0x00011af8
ctc_init_patch_list['CTC_init_hook']['change_from_jump']  = 'jal.HceCommon_InitOptions'
ctc_init_patch_list['CTC_init_hook']['change_to_jump'] = 'jal.ctc_init_hook'

# Redirect the call to setup the CodeSentry
ctc_init_patch_list['CTC_code_sentry_call'] = {}
ctc_init_patch_list['CTC_code_sentry_call']['start_offset'] = 0x0000138c
ctc_init_patch_list['CTC_code_sentry_call']['change_from_jump']  = 'jal.initCodeSentry'
ctc_init_patch_list['CTC_code_sentry_call']['change_to_jump'] = 'jal.ctc_initCodeSentry'

# Redirect the call to startHceTaskMenuMultiItem2_FSM
ctc_init_patch_list['CTC_fsm_get_valid_getHceTaskMenu'] = {}
ctc_init_patch_list['CTC_fsm_get_valid_getHceTaskMenu']['start_offset'] = 0x000266cc
ctc_init_patch_list['CTC_fsm_get_valid_getHceTaskMenu']['change_from_jump']  = 'j.fsm_get_valid'
ctc_init_patch_list['CTC_fsm_get_valid_getHceTaskMenu']['change_to_jump'] = 'j.ctc_fsm_get_valid_HceTaskMenu'

# Redirect the call to fsm_get_valid
ctc_init_patch_list['CTC_fsm_get_valid_HceTaskMenu'] = {}
ctc_init_patch_list['CTC_fsm_get_valid_HceTaskMenu']['start_offset'] = 0x00026734
ctc_init_patch_list['CTC_fsm_get_valid_HceTaskMenu']['change_from_jump']  = 'jal.fsm_get_valid'
ctc_init_patch_list['CTC_fsm_get_valid_HceTaskMenu']['change_to_jump'] = 'jal.ctc_fsm_get_valid_HceTaskMenu'


# Redirect the call to fsm_spawn
ctc_init_patch_list['CTC_fsm_spawn_HceTaskMenu'] = {}
ctc_init_patch_list['CTC_fsm_spawn_HceTaskMenu']['start_offset'] = 0x00026768
ctc_init_patch_list['CTC_fsm_spawn_HceTaskMenu']['change_from_jump']  = 'jal.fsm_spawn'
ctc_init_patch_list['CTC_fsm_spawn_HceTaskMenu']['change_to_jump'] = 'jal.ctc_fsm_spawn_HceTaskMenu'

