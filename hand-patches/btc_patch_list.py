## A set of hand-created binary patchs for BTC series trail camears
## To be consumed by codePatcher() functions
## Zak -- 2022-12-10: Updated for menu-based release
## Zak -- 2022-12-20: Updated for Edge (BTC-8E)
## Zak -- 2023-01-31: One file for all targets.  Share where we can; specialize where we must
## Zak -- 2024-10-06: Updated for version M06170F of baseline factory firmawer for BTC-{7,8}-E-HP5
## Zak -- 2025-03-12: Patches that allow a BTC-7A to run with BTC-7E baseline firmware

## Zak -- turning off extended event SD card power 
evsd_active = False

## Firmware Versions
firmware_bundle_a_patch_list = {}
firmware_bundle_a_patch_list['firmware_ID0'] = {}
firmware_bundle_a_patch_list['firmware_ID0']['start_offset'] = {}
firmware_bundle_a_patch_list['firmware_ID0']['start_offset']['BTC-7A'] = 0x03442f8
firmware_bundle_a_patch_list['firmware_ID0']['start_offset']['BTC-7E'] = 0x03442f8
firmware_bundle_a_patch_list['firmware_ID0']['start_offset']['BTC-8E'] = 0x03442f8
firmware_bundle_a_patch_list['firmware_ID0']['start_offset']['BTC-7E-HP4'] = 0x34938c
firmware_bundle_a_patch_list['firmware_ID0']['start_offset']['BTC-8E-HP4'] = 0x34d48c
firmware_bundle_a_patch_list['firmware_ID0']['start_offset']['BTC-7E-HP5'] = 0x02bfb48
firmware_bundle_a_patch_list['firmware_ID0']['start_offset']['BTC-8E-HP5'] = 0x02c1c48
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes'] = {}
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes']['BTC-7A']     = bytes("BTC7E_L02080E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes']['BTC-7E']     = bytes("BTC7E_L02080E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes']['BTC-8E']     = bytes("BTC8E_L02080E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes']['BTC-7E-HP4'] = bytes("BTC7EH4_M02240F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes']['BTC-8E-HP4'] = bytes("BTC8EH4_M02240F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes']['BTC-7E-HP5'] = bytes("BTC7EH5_M06170F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_from_bytes']['BTC-8E-HP5'] =  bytes("BTC8EH5_M06170F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']   = {}
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']['BTC-7A']       = bytes("WWL7A_230409E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']['BTC-7E']       = bytes("WWL7E_230409E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']['BTC-8E']       = bytes("WWL8E_230409E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']['BTC-7E-HP4']   = bytes("WWL7EH4_230409A", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']['BTC-8E-HP4']   = bytes("WWL8EH4_230409A", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']['BTC-7E-HP5']   = bytes("WWL7EH5_230409A", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes']['BTC-8E-HP5']   = bytes("WWL8EH5_240912P", 'utf-8');

firmware_bundle_a_patch_list['firmware_ID1'] = {}
firmware_bundle_a_patch_list['firmware_ID1']['start_offset'] = {}
firmware_bundle_a_patch_list['firmware_ID1']['start_offset']['BTC-7A'] = 0x0364554
firmware_bundle_a_patch_list['firmware_ID1']['start_offset']['BTC-7E'] = 0x0364554
firmware_bundle_a_patch_list['firmware_ID1']['start_offset']['BTC-8E'] = 0x03645b8;
firmware_bundle_a_patch_list['firmware_ID1']['start_offset']['BTC-7E-HP4'] = 0x367388;
firmware_bundle_a_patch_list['firmware_ID1']['start_offset']['BTC-8E-HP4'] = 0x36b5a0;
firmware_bundle_a_patch_list['firmware_ID1']['start_offset']['BTC-7E-HP5'] = 0x02da7ec;
firmware_bundle_a_patch_list['firmware_ID1']['start_offset']['BTC-8E-HP5'] = 0x02dc994
firmware_bundle_a_patch_list['firmware_ID1']['change_from_bytes'] = {}
firmware_bundle_a_patch_list['firmware_ID1']['change_from_bytes']['BTC-7A']     = bytes("BTC7E_L02080E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_from_bytes']['BTC-7E']     = bytes("BTC7E_L02080E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_from_bytes']['BTC-8E']     = bytes("BTC8E_L02080E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_from_bytes']['BTC-7E-HP4'] = bytes("BTC7EH4_M02240F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_from_bytes']['BTC-8E-HP4'] = bytes("BTC8EH4_M02240F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_from_bytes']['BTC-7E-HP5'] = bytes("BTC7EH5_M06170F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_from_bytes']['BTC-8E-HP5'] =  bytes("BTC8EH5_M06170F", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes'] = {}
firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes']['BTC-7A']       = bytes("WWL7A_230409E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes']['BTC-7E']       = bytes("WWL7E_230409E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes']['BTC-8E']       = bytes("WWL8E_230409E", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes']['BTC-7E-HP4']   = bytes("WWL7EH5_230409A", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes']['BTC-8E-HP4']   = bytes("WWL8EH5_230409A", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes']['BTC-7E-HP5']   = bytes("WWL7EH5_230409A", 'utf-8');
firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes']['BTC-8E-HP5']   = bytes("WWL8EH5_230409A", 'utf-8');

firmware_bundle_a_patch_list['firmware_exif_id'] = {}
firmware_bundle_a_patch_list['firmware_exif_id']['start_offset'] = {}
firmware_bundle_a_patch_list['firmware_exif_id']['start_offset']['BTC-7A'] = 0x036b87c
firmware_bundle_a_patch_list['firmware_exif_id']['change_from_bytes'] = {}
firmware_bundle_a_patch_list['firmware_exif_id']['change_from_bytes']['BTC-7A']     = bytes([0x37, 0x45, 0x00, 0x00]); "7E"
firmware_bundle_a_patch_list['firmware_exif_id']['change_to_bytes'] = {}
firmware_bundle_a_patch_list['firmware_exif_id']['change_to_bytes']['BTC-7A']       = bytes([0x37, 0x41, 0x00, 0x00]); "7A"


def set_version_string(build_database):
    for camera_type in build_database:
        if build_database[camera_type].get('Version') is not None:
            version_string = build_database[camera_type]['Version']
            firmware_bundle_a_patch_list['firmware_ID0']['change_to_bytes'][camera_type]  = bytes(version_string, 'utf-8')
            firmware_bundle_a_patch_list['firmware_ID1']['change_to_bytes'][camera_type]  = bytes(version_string, 'utf-8')
    return


############# Feature Patches ################################

#
# Rewrite the call that sprintf()'s the string to the bottom of the ribbon
#    in screenPrintReplayHeaderRibbons()
#    Line 43
custom_ribbon_patch_list = {}
custom_ribbon_patch_list['Custom_Ribbon'] = {}
custom_ribbon_patch_list['Custom_Ribbon']['function'] = 'screenPrintReplayHeaderRibbons'
custom_ribbon_patch_list['Custom_Ribbon']['line_number'] = {}
custom_ribbon_patch_list['Custom_Ribbon']['line_number']['BTC-7A'] = 43
custom_ribbon_patch_list['Custom_Ribbon']['line_number']['BTC-7E'] = 43
custom_ribbon_patch_list['Custom_Ribbon']['line_number']['BTC-8E'] = 43
custom_ribbon_patch_list['Custom_Ribbon']['line_number']['BTC-7E-HP4'] = 43
custom_ribbon_patch_list['Custom_Ribbon']['line_number']['BTC-8E-HP4'] = 43
custom_ribbon_patch_list['Custom_Ribbon']['line_number']['BTC-7E-HP5'] = 43
custom_ribbon_patch_list['Custom_Ribbon']['line_number']['BTC-8E-HP5'] = 43
custom_ribbon_patch_list['Custom_Ribbon']['start_offset'] = {}
custom_ribbon_patch_list['Custom_Ribbon']['start_offset']['BTC-7A'] = 0x01368bc
custom_ribbon_patch_list['Custom_Ribbon']['start_offset']['BTC-7E'] = 0x01368bc
custom_ribbon_patch_list['Custom_Ribbon']['start_offset']['BTC-8E'] = 0x01374b8
custom_ribbon_patch_list['Custom_Ribbon']['start_offset']['BTC-7E-HP4']= 0x0013318c
custom_ribbon_patch_list['Custom_Ribbon']['start_offset']['BTC-8E-HP4']= 0x00135cbc
custom_ribbon_patch_list['Custom_Ribbon']['start_offset']['BTC-7E-HP5']= 0x001161dc
custom_ribbon_patch_list['Custom_Ribbon']['start_offset']['BTC-8E-HP5']= 0x0116b34
custom_ribbon_patch_list['Custom_Ribbon']['change_from_jump'] = 'jal.local_sprintf'
custom_ribbon_patch_list['Custom_Ribbon']['change_to_jump'] = 'jal.wbwl_custom_ribbon_sprintf'

# this in HandleReplayMenuVideo; source line 27
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['function'] = 'HandleReplayMenuVideo'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['line_number'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['line_number']['BTC-7A'] = 28
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['line_number']['BTC-7E'] = 28
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['line_number']['BTC-8E'] = 27
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['line_number']['BTC-7E-HP4'] = 28
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['line_number']['BTC-8E-HP4'] = 28
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['line_number']['BTC-7E-HP5'] = 27
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['line_number']['BTC-8E-HP5'] = 27
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset']['BTC-7A'] = 0x00137218
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset']['BTC-7E'] = 0x00137218
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset']['BTC-8E'] = 0x00137e14
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset']['BTC-7E-HP4'] = 0x00133ae8
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset']['BTC-8E-HP4'] = 0x00136618
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset']['BTC-7E-HP5'] = 0x0116b38
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['start_offset']['BTC-8E-HP5'] = 0x0117490
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['change_from_jump'] = 'j.draw_video_scroll_bar'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook']['change_to_jump'] = 'j.ld_draw_video_scroll_bar'

# this in HandleReplayMenuVideo; source line 78
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['function'] = 'HandleReplayMenuVideo'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['line_number'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['line_number']['BTC-7A'] = 79
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['line_number']['BTC-7E'] = 79
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['line_number']['BTC-8E'] = 78
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['line_number']['BTC-7E-HP4'] = 79
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['line_number']['BTC-8E-HP4'] = 79
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['line_number']['BTC-7E-HP5'] = 78
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['line_number']['BTC-8E-HP5'] = 89
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset'] = {}
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset']['BTC-7A'] = 0x00137168
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset']['BTC-7E'] = 0x00137168
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset']['BTC-8E'] = 0x00137d64
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset']['BTC-7E-HP4'] = 0x00133a38
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset']['BTC-8E-HP4'] = 0x00136568
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset']['BTC-7E-HP5'] = 0x0116a88
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['start_offset']['BTC-8E-HP5'] = 0x01173e0
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['change_from_jump'] = 'jal.draw_video_scroll_bar'
custom_ribbon_patch_list['ld_draw_video_scroll_bar_hook2']['change_to_jump'] = 'jal.ld_draw_video_scroll_bar'
# this in HandleReplayMenuVideo; source line 34
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook'] = {}
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['function'] = 'HandleReplayMenuVideo'
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['line_number'] = {}
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['line_number']['BTC-7A'] = 35
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['line_number']['BTC-7E'] = 35
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['line_number']['BTC-8E'] = 34
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['line_number']['BTC-7E-HP4'] = 35
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['line_number']['BTC-8E-HP4'] = 35
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['line_number']['BTC-7E-HP5'] = 34
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['line_number']['BTC-8E-HP5'] = 41
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset'] = {}
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset']['BTC-7A'] = 0x00136f6c
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset']['BTC-7E'] = 0x00136f6c
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset']['BTC-8E'] = 0x00137b68
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset']['BTC-7E-HP4'] = 0x0013383c
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset']['BTC-8E-HP4'] = 0x0013636c
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset']['BTC-7E-HP5'] = 0x0011688c
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['start_offset']['BTC-8E-HP5'] = 0x01171e4
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['change_from_jump'] = 'jal.draw_rectangle_wrapper'
custom_ribbon_patch_list['ld_clear_video_scroll_bar_hook']['change_to_jump'] = 'jal.ld_clear_video_scroll_bar'


# eliminate the limit check on night time video length by
#   nulling out the store that sets video length to 20 seconds if IR LED on
#   this allows the ribbon display to properly record remaining video lenght
#   special case in HceTaskRecording_RecVideoIninit()
#   replace the code that would otherwise limit the video to 20 seconds with a NOOP
#   ~source line 120
night_video_limit_patch_list = {}
night_video_limit_patch_list['No_Video_Limit_Store'] = {}
night_video_limit_patch_list['No_Video_Limit_Store']['function'] = 'HceTaskRecording_RecVideoInit'
night_video_limit_patch_list['No_Video_Limit_Store']['line_number'] = {}
night_video_limit_patch_list['No_Video_Limit_Store']['line_number']['BTC-7A'] = 120
night_video_limit_patch_list['No_Video_Limit_Store']['line_number']['BTC-7E'] = 120
night_video_limit_patch_list['No_Video_Limit_Store']['line_number']['BTC-8E'] = 120
night_video_limit_patch_list['No_Video_Limit_Store']['line_number']['BTC-7E-HP4'] = 124
night_video_limit_patch_list['No_Video_Limit_Store']['line_number']['BTC-8E-HP4'] = 125
night_video_limit_patch_list['No_Video_Limit_Store']['line_number']['BTC-7E-HP5'] = 146
night_video_limit_patch_list['No_Video_Limit_Store']['line_number']['BTC-8E-HP5'] = 143
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset'] = {}
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset']['BTC-7A'] = 0x00125534
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset']['BTC-7E'] = 0x00125534
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset']['BTC-8E'] = 0x001258ec
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset']['BTC-7E-HP4'] = 0x001214ac
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset']['BTC-8E-HP4'] = 0x001219fc
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset']['BTC-7E-HP5'] = 0x0010496c
night_video_limit_patch_list['No_Video_Limit_Store']['start_offset']['BTC-8E-HP5'] = 0x00104a34
night_video_limit_patch_list['No_Video_Limit_Store']['change_from_bytes'] = bytes([0x14,0x00,0x02,0x24]) 
night_video_limit_patch_list['No_Video_Limit_Store']['change_to_bytes']   = bytes([0x2c,0x01,0x02,0x24])


#
# custom_info_strip patch
# HceStampDraw_draw_info_bar
# ~Source code line 54
custom_info_strip_patch_list = {}
custom_info_strip_patch_list['date_local_sprintf'] = {}
custom_info_strip_patch_list['date_local_sprintf']['function'] = 'HceStampDraw_draw_info_bar'
custom_info_strip_patch_list['date_local_sprintf']['line_number'] = {}
custom_info_strip_patch_list['date_local_sprintf']['line_number']['BTC-7A'] = 40
custom_info_strip_patch_list['date_local_sprintf']['line_number']['BTC-7E'] = 40
custom_info_strip_patch_list['date_local_sprintf']['line_number']['BTC-8E'] = 54
custom_info_strip_patch_list['date_local_sprintf']['line_number']['BTC-7E-HP4'] = 77
custom_info_strip_patch_list['date_local_sprintf']['line_number']['BTC-8E-HP4'] = 113
custom_info_strip_patch_list['date_local_sprintf']['line_number']['BTC-7E-HP5'] = 76
custom_info_strip_patch_list['date_local_sprintf']['line_number']['BTC-8E-HP5'] = 111
custom_info_strip_patch_list['date_local_sprintf']['start_offset'] = {}
custom_info_strip_patch_list['date_local_sprintf']['start_offset']['BTC-7A'] = 0x0011ff50
custom_info_strip_patch_list['date_local_sprintf']['start_offset']['BTC-7E'] = 0x0011ff50
custom_info_strip_patch_list['date_local_sprintf']['start_offset']['BTC-8E'] = 0x001202e4
custom_info_strip_patch_list['date_local_sprintf']['start_offset']['BTC-7E-HP4'] = 0x011bb30
custom_info_strip_patch_list['date_local_sprintf']['start_offset']['BTC-8E-HP4'] = 0x011c05c
custom_info_strip_patch_list['date_local_sprintf']['start_offset']['BTC-7E-HP5'] = 0x000faa60
custom_info_strip_patch_list['date_local_sprintf']['start_offset']['BTC-8E-HP5'] = 0x00faad8
custom_info_strip_patch_list['date_local_sprintf']['change_from_jump'] = 'jal.local_sprintf'
custom_info_strip_patch_list['date_local_sprintf']['change_to_jump']   = 'jal.wbwl_custom_info_strip_date_sprintf'
# HceStampDraw_draw_info_bar
# ~Source code line 67
custom_info_strip_patch_list['time_local_sprintf'] = {}
custom_info_strip_patch_list['time_local_sprintf']['function'] = 'HceStampDraw_draw_info_bar'
custom_info_strip_patch_list['time_local_sprintf']['line_number'] = {}
custom_info_strip_patch_list['time_local_sprintf']['line_number']['BTC-7A'] = 67
custom_info_strip_patch_list['time_local_sprintf']['line_number']['BTC-7E'] = 67
custom_info_strip_patch_list['time_local_sprintf']['line_number']['BTC-8E'] = 67
custom_info_strip_patch_list['time_local_sprintf']['line_number']['BTC-7E-HP4'] = 90
custom_info_strip_patch_list['time_local_sprintf']['line_number']['BTC-8E-HP4'] = 126
custom_info_strip_patch_list['time_local_sprintf']['line_number']['BTC-7E-HP5'] = 89
custom_info_strip_patch_list['time_local_sprintf']['line_number']['BTC-8E-HP5'] = 124
custom_info_strip_patch_list['time_local_sprintf']['start_offset'] = {}
custom_info_strip_patch_list['time_local_sprintf']['start_offset']['BTC-7A'] = 0x0011ffa8
custom_info_strip_patch_list['time_local_sprintf']['start_offset']['BTC-7E'] = 0x0011ffa8
custom_info_strip_patch_list['time_local_sprintf']['start_offset']['BTC-8E'] = 0x0012033c
custom_info_strip_patch_list['time_local_sprintf']['start_offset']['BTC-7E-HP4'] = 0x011bb88
custom_info_strip_patch_list['time_local_sprintf']['start_offset']['BTC-8E-HP4'] = 0x011c0b4
custom_info_strip_patch_list['time_local_sprintf']['start_offset']['BTC-7E-HP5'] =  0x00faab8
custom_info_strip_patch_list['time_local_sprintf']['start_offset']['BTC-8E-HP5'] = 0x00fab30
custom_info_strip_patch_list['time_local_sprintf']['change_from_jump'] = 'jal.local_sprintf'
custom_info_strip_patch_list['time_local_sprintf']['change_to_jump']   = 'jal.wbwl_custom_info_strip_time_sprintf'
# HceStampDraw_draw_info_bar
# ~Source code line 68
custom_info_strip_patch_list['last_strlen'] = {}
custom_info_strip_patch_list['last_strlen']['function'] = 'HceStampDraw_draw_info_bar'
custom_info_strip_patch_list['last_strlen']['line_number'] = {}
custom_info_strip_patch_list['last_strlen']['line_number']['BTC-7A'] = 77
custom_info_strip_patch_list['last_strlen']['line_number']['BTC-7E'] = 77
custom_info_strip_patch_list['last_strlen']['line_number']['BTC-8E'] = 68
custom_info_strip_patch_list['last_strlen']['line_number']['BTC-7E-HP4'] = 115
custom_info_strip_patch_list['last_strlen']['line_number']['BTC-8E-HP4'] = 151
custom_info_strip_patch_list['last_strlen']['line_number']['BTC-7E-HP5'] = 113
custom_info_strip_patch_list['last_strlen']['line_number']['BTC-8E-HP5'] = 148
custom_info_strip_patch_list['last_strlen']['start_offset'] = {}
custom_info_strip_patch_list['last_strlen']['start_offset']['BTC-7A'] = 0x001200c4
custom_info_strip_patch_list['last_strlen']['start_offset']['BTC-7E'] = 0x001200c4
custom_info_strip_patch_list['last_strlen']['start_offset']['BTC-8E'] = 0x00120344
custom_info_strip_patch_list['last_strlen']['start_offset']['BTC-7E-HP4'] = 0x011bca4
custom_info_strip_patch_list['last_strlen']['start_offset']['BTC-8E-HP4'] = 0x011c1d0
custom_info_strip_patch_list['last_strlen']['start_offset']['BTC-7E-HP5'] = 0x00fabd4
custom_info_strip_patch_list['last_strlen']['start_offset']['BTC-8E-HP5'] = 0x00fac4c
custom_info_strip_patch_list['last_strlen']['change_from_jump'] = 'jal.btc_strlen'
custom_info_strip_patch_list['last_strlen']['change_to_jump']   = 'jal.wbwl_custom_info_strip_strlen'
# Intercept calls to draw logo on info strip ("stamp")
# HceStillStampCB
# ~Source code line 99
custom_info_strip_patch_list['still_logo'] = {}
custom_info_strip_patch_list['still_logo']['function'] = 'HceStillStampCB'
custom_info_strip_patch_list['still_logo']['line_number'] = {}
custom_info_strip_patch_list['still_logo']['line_number']['BTC-7A'] = 99
custom_info_strip_patch_list['still_logo']['line_number']['BTC-7E'] = 99
custom_info_strip_patch_list['still_logo']['line_number']['BTC-8E'] = 99
custom_info_strip_patch_list['still_logo']['line_number']['BTC-7E-HP4'] = 99
custom_info_strip_patch_list['still_logo']['line_number']['BTC-8E-HP4'] = 96
custom_info_strip_patch_list['still_logo']['line_number']['BTC-7E-HP5'] = 99
custom_info_strip_patch_list['still_logo']['line_number']['BTC-8E-HP5'] = 99
custom_info_strip_patch_list['still_logo']['start_offset'] = {}
custom_info_strip_patch_list['still_logo']['start_offset']['BTC-7A'] = 0x00120684
custom_info_strip_patch_list['still_logo']['start_offset']['BTC-7E'] = 0x00120684
custom_info_strip_patch_list['still_logo']['start_offset']['BTC-8E'] = 0x00120a18
custom_info_strip_patch_list['still_logo']['start_offset']['BTC-7E-HP4'] = 0x011c264
custom_info_strip_patch_list['still_logo']['start_offset']['BTC-8E-HP4'] = 0x011c790
custom_info_strip_patch_list['still_logo']['start_offset']['BTC-7E-HP5'] = 0x00fb194
custom_info_strip_patch_list['still_logo']['start_offset']['BTC-8E-HP5'] = 0x00fb20c
custom_info_strip_patch_list['still_logo']['change_from_jump'] = 'jal.HceStampDrawLogo'
custom_info_strip_patch_list['still_logo']['change_to_jump']   = 'jal.wbwl_StampDrawLogo'
# HceVideoStampUpdate
# ~Source code line 18
custom_info_strip_patch_list['video_logo'] = {}
custom_info_strip_patch_list['video_logo']['function'] = 'HceVideoStampUpdate'
custom_info_strip_patch_list['video_logo']['line_number'] = {}
custom_info_strip_patch_list['video_logo']['line_number']['BTC-7A'] = 18
custom_info_strip_patch_list['video_logo']['line_number']['BTC-7E'] = 18
custom_info_strip_patch_list['video_logo']['line_number']['BTC-8E'] = 18
custom_info_strip_patch_list['video_logo']['line_number']['BTC-7E-HP4'] = 18
custom_info_strip_patch_list['video_logo']['line_number']['BTC-8E-HP4'] = 18
custom_info_strip_patch_list['video_logo']['line_number']['BTC-7E-HP5'] = 18
custom_info_strip_patch_list['video_logo']['line_number']['BTC-8E-HP5'] = 18
custom_info_strip_patch_list['video_logo']['start_offset'] = {}
custom_info_strip_patch_list['video_logo']['start_offset']['BTC-7A'] = 0x0011fc04
custom_info_strip_patch_list['video_logo']['start_offset']['BTC-7E'] = 0x0011fc04
custom_info_strip_patch_list['video_logo']['start_offset']['BTC-8E'] = 0x0011ff18
custom_info_strip_patch_list['video_logo']['start_offset']['BTC-7E-HP4'] = 0x011b730
custom_info_strip_patch_list['video_logo']['start_offset']['BTC-8E-HP4'] = 0x011bb10
custom_info_strip_patch_list['video_logo']['start_offset']['BTC-7E-HP5'] = 0x00fa668
custom_info_strip_patch_list['video_logo']['start_offset']['BTC-8E-HP5'] = 0x00fa594
custom_info_strip_patch_list['video_logo']['change_from_jump'] = 'jal.HceStampDrawLogo'
custom_info_strip_patch_list['video_logo']['change_to_jump']   = 'jal.wbwl_StampDrawLogo'

# HceStampLoadFont
# Reduce the Height and Width of the ICON font by a factor of 2
#        this is done early, and insures all the downstream settings
#        are correct.  The only thing you have to do is *also* display
#        the logo at half scale. 
# Line 16
custom_info_strip_patch_list['load_font_width'] = {}
custom_info_strip_patch_list['load_font_width']['function'] = 'HceStampLoadFont'
custom_info_strip_patch_list['load_font_width']['line_number'] = {}
custom_info_strip_patch_list['load_font_width']['line_number']['BTC-7A'] = 16
custom_info_strip_patch_list['load_font_width']['line_number']['BTC-7E'] = 16
custom_info_strip_patch_list['load_font_width']['line_number']['BTC-8E'] = 16
custom_info_strip_patch_list['load_font_width']['line_number']['BTC-7E-HP4'] = 16
custom_info_strip_patch_list['load_font_width']['line_number']['BTC-8E-HP4'] = 16
custom_info_strip_patch_list['load_font_width']['line_number']['BTC-7E-HP5'] = 16
custom_info_strip_patch_list['load_font_width']['line_number']['BTC-8E-HP5'] = 14
custom_info_strip_patch_list['load_font_width']['start_offset'] = {}
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-7A']= 0x0011ddbc
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-7E']= 0x0011ddbc
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-8E']= 0x0011e014
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-7E-HP4'] = 0x0119838
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-8E-HP4'] = 0x0119c18
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-7E-HP5'] = 0x00f8764
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-8E-HP5'] = 0x00f8690
custom_info_strip_patch_list['load_font_width']['change_from_bytes'] = bytes([0x30,0x00,0x02,0x24])
custom_info_strip_patch_list['load_font_width']['change_to_bytes']   = bytes([0x16,0x00,0x02,0x24])
# Line 17
custom_info_strip_patch_list['load_font_width'] = {}
custom_info_strip_patch_list['load_font_width']['function'] = 'HceStampLoadFont'
custom_info_strip_patch_list['load_font_width']['linte_number'] = {}
custom_info_strip_patch_list['load_font_width']['linte_number']['BTC-7A'] = 17
custom_info_strip_patch_list['load_font_width']['linte_number']['BTC-7E'] = 17
custom_info_strip_patch_list['load_font_width']['linte_number']['BTC-8E'] = 17
custom_info_strip_patch_list['load_font_width']['linte_number']['BTC-7E-HP4'] = 17
custom_info_strip_patch_list['load_font_width']['linte_number']['BTC-8E-HP4'] = 17
custom_info_strip_patch_list['load_font_width']['linte_number']['BTC-7E-HP5'] = 17
custom_info_strip_patch_list['load_font_width']['linte_number']['BTC-8E-HP5'] = 15
custom_info_strip_patch_list['load_font_width']['start_offset'] = {}
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-7A'] = 0x0011ddc0
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-7E'] = 0x0011ddc0
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-8E'] = 0x0011e018
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-7E-HP4'] = 0x011983c
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-8E-HP4'] = 0x0119c1c
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-7E-HP5'] = 0x00f8768
custom_info_strip_patch_list['load_font_width']['start_offset']['BTC-8E-HP5'] = 0x00f8694
custom_info_strip_patch_list['load_font_width']['change_from_bytes'] = bytes([0x60,0x00,0x03,0x24])
custom_info_strip_patch_list['load_font_width']['change_to_bytes']   = bytes([0x30,0x00,0x03,0x24])


#
# volume and file naming patches
# in Init_DCF
vfn_patch_list = {}
vfn_patch_list['fatVolLabSet'] = {}
vfn_patch_list['fatVolLabSet']['function'] = 'Init_DCF'
vfn_patch_list['fatVolLabSet']['line_number'] = {}
vfn_patch_list['fatVolLabSet']['line_number']['BTC-7A'] = 25
vfn_patch_list['fatVolLabSet']['line_number']['BTC-7E'] = 25
vfn_patch_list['fatVolLabSet']['line_number']['BTC-8E'] = 20
vfn_patch_list['fatVolLabSet']['line_number']['BTC-7E-HP4'] = 25
vfn_patch_list['fatVolLabSet']['line_number']['BTC-8E-HP4'] = 25
vfn_patch_list['fatVolLabSet']['line_number']['BTC-7E-HP5'] = 31
vfn_patch_list['fatVolLabSet']['line_number']['BTC-8E-HP5'] = 20
vfn_patch_list['fatVolLabSet']['start_offset'] = {}
vfn_patch_list['fatVolLabSet']['start_offset']['BTC-7A']     = 0x001226c0
vfn_patch_list['fatVolLabSet']['start_offset']['BTC-7E']     = 0x001226c0
vfn_patch_list['fatVolLabSet']['start_offset']['BTC-8E']     = 0x00122a80
vfn_patch_list['fatVolLabSet']['start_offset']['BTC-7E-HP4'] = 0x011e2d0
vfn_patch_list['fatVolLabSet']['start_offset']['BTC-8E-HP4'] = 0x011e828
vfn_patch_list['fatVolLabSet']['start_offset']['BTC-7E-HP5'] = 0x010145c
vfn_patch_list['fatVolLabSet']['start_offset']['BTC-8E-HP5'] = 0x0101534
vfn_patch_list['fatVolLabSet']['change_from_jump'] = 'jal.fatVolLabSet_wrapper'
vfn_patch_list['fatVolLabSet']['change_to_jump']   = 'jal.wbwl_fatVolLabSet'
# in HceMedia_PreInitDCFFS
vfn_patch_list['dir_file_fix0'] = {}
vfn_patch_list['dir_file_fix0']['function'] = 'HceMedia_PreInitDCFFS'
vfn_patch_list['dir_file_fix0']['line_number'] = {}
vfn_patch_list['dir_file_fix0']['line_number']['BTC-7A'] = 5
vfn_patch_list['dir_file_fix0']['line_number']['BTC-7E'] = 5
vfn_patch_list['dir_file_fix0']['line_number']['BTC-8E'] = 20
vfn_patch_list['dir_file_fix0']['line_number']['BTC-7E-HP4'] = 12
vfn_patch_list['dir_file_fix0']['line_number']['BTC-8E-HP4'] = 12
vfn_patch_list['dir_file_fix0']['line_number']['BTC-7E-HP5'] = 12
vfn_patch_list['dir_file_fix0']['line_number']['BTC-8E-HP5'] = 12
vfn_patch_list['dir_file_fix0']['start_offset'] = {}
vfn_patch_list['dir_file_fix0']['start_offset']['BTC-7A'] = 0x00114a48
vfn_patch_list['dir_file_fix0']['start_offset']['BTC-7E'] = 0x00114a48
vfn_patch_list['dir_file_fix0']['start_offset']['BTC-8E'] = 0x00114ca0
vfn_patch_list['dir_file_fix0']['start_offset']['BTC-7E-HP4'] = 0x0110b10
vfn_patch_list['dir_file_fix0']['start_offset']['BTC-8E-HP4'] = 0x0111010
vfn_patch_list['dir_file_fix0']['start_offset']['BTC-7E-HP5'] = 0x00edd7c
vfn_patch_list['dir_file_fix0']['start_offset']['BTC-8E-HP5'] = 0x00ede38
vfn_patch_list['dir_file_fix0']['change_from_jump'] = 'jal.btc_init_directory_suffix_file_prefix'
vfn_patch_list['dir_file_fix0']['change_to_jump']   = 'jal.wbwl_init_directory_suffix_file_prefix'
# in another_media_init
vfn_patch_list['dir_file_fix1'] = {}
vfn_patch_list['dir_file_fix1']['function'] = 'another_media_init'
vfn_patch_list['dir_file_fix1']['line_number'] = {}
vfn_patch_list['dir_file_fix1']['line_number']['BTC-7E-HP4'] = 5
vfn_patch_list['dir_file_fix1']['line_number']['BTC-8E-HP4'] = 5
vfn_patch_list['dir_file_fix1']['line_number']['BTC-7E-HP5'] = 5
vfn_patch_list['dir_file_fix1']['line_number']['BTC-8E-HP5'] = 5
vfn_patch_list['dir_file_fix1']['start_offset'] = {}
vfn_patch_list['dir_file_fix1']['start_offset']['BTC-7E-HP4'] = 0x011007c
vfn_patch_list['dir_file_fix1']['start_offset']['BTC-8E-HP4'] = 0x011057c
vfn_patch_list['dir_file_fix1']['start_offset']['BTC-7E-HP5'] = 0x00ed2e8
vfn_patch_list['dir_file_fix1']['start_offset']['BTC-8E-HP5'] = 0x00ed3a4
vfn_patch_list['dir_file_fix1']['change_from_jump'] = 'jal.btc_init_directory_suffix_file_prefix'
vfn_patch_list['dir_file_fix1']['change_to_jump']   = 'jal.wbwl_init_directory_suffix_file_prefix'

# in another_media_init
vfn_patch_list['dir_file_fix2'] = {}
vfn_patch_list['dir_file_fix2']['function'] = 'another_media_init'
vfn_patch_list['dir_file_fix2']['line_number'] = {}
vfn_patch_list['dir_file_fix2']['line_number']['BTC-7A'] = 22
vfn_patch_list['dir_file_fix2']['line_number']['BTC-7E'] = 22
vfn_patch_list['dir_file_fix2']['line_number']['BTC-8E'] = 22
vfn_patch_list['dir_file_fix2']['start_offset'] = {}
vfn_patch_list['dir_file_fix2']['start_offset']['BTC-7A']     = 0x0108c50
vfn_patch_list['dir_file_fix2']['start_offset']['BTC-7E']     = 0x0108c50
vfn_patch_list['dir_file_fix2']['start_offset']['BTC-8E']     = 0x0108d94
vfn_patch_list['dir_file_fix2']['change_from_jump'] = 'jal.init_directory_suffix_file_prefix'
vfn_patch_list['dir_file_fix2']['change_to_jump']   = 'jal.wbwl_alt_init_directory_suffix_file_prefix'

# in TaskTimeLapseFSM_task8_CopyJPGFromRAM(void)
# line 16
vfn_patch_list['timelapse_path'] = {}
vfn_patch_list['timelapse_path']['function'] = 'TaskTimeLapseFSM_task8_CopyJPGFromRAM'
vfn_patch_list['timelapse_path']['line_number'] = {}
vfn_patch_list['timelapse_path']['line_number']['BTC-7A'] = 16
vfn_patch_list['timelapse_path']['line_number']['BTC-7E'] = 16
vfn_patch_list['timelapse_path']['line_number']['BTC-8E'] = 16
vfn_patch_list['timelapse_path']['line_number']['BTC-7E-HP4'] = 15
vfn_patch_list['timelapse_path']['line_number']['BTC-8E-HP4'] = 15
vfn_patch_list['timelapse_path']['line_number']['BTC-7E-HP5'] = 16
vfn_patch_list['timelapse_path']['line_number']['BTC-8E-HP5'] = 16
vfn_patch_list['timelapse_path']['start_offset'] = {}
vfn_patch_list['timelapse_path']['start_offset']['BTC-7A'] = 0x00129428
vfn_patch_list['timelapse_path']['start_offset']['BTC-7E'] = 0x00129428
vfn_patch_list['timelapse_path']['start_offset']['BTC-8E'] = 0x001297d0
vfn_patch_list['timelapse_path']['start_offset']['BTC-7E-HP4'] = 0x0125ad4
vfn_patch_list['timelapse_path']['start_offset']['BTC-8E-HP4'] = 0x0126014
vfn_patch_list['timelapse_path']['start_offset']['BTC-7E-HP5'] = 0x0108f50
vfn_patch_list['timelapse_path']['start_offset']['BTC-8E-HP5'] = 0x0109008
vfn_patch_list['timelapse_path']['change_from_jump'] = 'jal.local_sprintf'
vfn_patch_list['timelapse_path']['change_to_jump']   = 'jal.wbwl_temp_file_path_sprintf'


#
# (debug) utilities
# Hce_FWFileChk
# source code line 47
####utilities_patch_list = {}
utilities_patch_list['tty_flush'] = {}
utilities_patch_list['tty_flush']['function'] = 'Hce_FWFileChk'
utilities_patch_list['tty_flush']['line_number'] = {}
utilities_patch_list['tty_flush']['line_number']['BTC-7A'] = 47
utilities_patch_list['tty_flush']['line_number']['BTC-7E'] = 47
utilities_patch_list['tty_flush']['line_number']['BTC-8E'] = 47
utilities_patch_list['tty_flush']['line_number']['BTC-7E-HP4'] = 40
utilities_patch_list['tty_flush']['line_number']['BTC-8E-HP4'] = 40
utilities_patch_list['tty_flush']['line_number']['BTC-7E-HP5'] = 46
utilities_patch_list['tty_flush']['line_number']['BTC-8E-HP5'] = 46
utilities_patch_list['tty_flush']['start_offset'] = {}
utilities_patch_list['tty_flush']['start_offset']['BTC-A'] = 0x012a734
utilities_patch_list['tty_flush']['start_offset']['BTC-7E'] = 0x012a734
utilities_patch_list['tty_flush']['start_offset']['BTC-8E'] = 0x012aad4
utilities_patch_list['tty_flush']['start_offset']['BTC-7E-HP4'] = 0x0126dfc
utilities_patch_list['tty_flush']['start_offset']['BTC-8E-HP4'] = 0x0127334
utilities_patch_list['tty_flush']['start_offset']['BTC-7E-HP5'] = 0x010a2f4
utilities_patch_list['tty_flush']['start_offset']['BTC-8E-HP5'] = 0x010a3a4
utilities_patch_list['tty_flush']['change_from_jump'] = 'jal.check_post_printf_state_set_sio_params'
utilities_patch_list['tty_flush']['change_to_jump']   = 'jal.utilities_check_post_printf_hook'

# handleLanguage_menu
# source code line 38
utilities_patch_list = {}
utilities_patch_list['tty_flush'] = {}
utilities_patch_list['tty_flush']['function'] = 'handleLanguage_menu'
utilities_patch_list['tty_flush']['line_number'] = {}
utilities_patch_list['tty_flush']['line_number']['BTC-7A'] = 37
utilities_patch_list['tty_flush']['line_number']['BTC-7E'] = 37
utilities_patch_list['tty_flush']['line_number']['BTC-8E'] = 38
utilities_patch_list['tty_flush']['line_number']['BTC-7E-HP4'] = 37
utilities_patch_list['tty_flush']['line_number']['BTC-8E-HP4'] = 37
utilities_patch_list['tty_flush']['line_number']['BTC-7E-HP5'] = 36
utilities_patch_list['tty_flush']['line_number']['BTC-8E-HP5'] = 37
utilities_patch_list['tty_flush']['start_offset'] = {}
utilities_patch_list['tty_flush']['start_offset']['BTC-7A'] = 0x0132714
utilities_patch_list['tty_flush']['start_offset']['BTC-7E'] = 0x0132714
utilities_patch_list['tty_flush']['start_offset']['BTC-8E'] = 0x0133310
utilities_patch_list['tty_flush']['start_offset']['BTC-7E-HP4'] = 0x012efc4
utilities_patch_list['tty_flush']['start_offset']['BTC-8E-HP4'] = 0x0131af4
utilities_patch_list['tty_flush']['start_offset']['BTC-7E-HP5'] = 0x0111d4c
utilities_patch_list['tty_flush']['start_offset']['BTC-8E-HP5'] = 0x01126a4
utilities_patch_list['tty_flush']['change_from_jump'] = 'jal.set_cold_item_language_id'
utilities_patch_list['tty_flush']['change_to_jump']   = 'jal.util_set_cold_item_language_id'


############# DSLR Trigger Patches ############################

# Patch to enable dslr trigger (w/o battery monitor)
dslr_trigger_patch_list = {}

# turning LED ON
# in HceTaskStill_task0
dslr_trigger_patch_list['dt_standard_still_start'] = {}
dslr_trigger_patch_list['dt_standard_still_start']['function'] = 'HceTaskStill_task0'
dslr_trigger_patch_list['dt_standard_still_start']['line_number'] = {}
dslr_trigger_patch_list['dt_standard_still_start']['line_number']['BTC-7A'] = 56
dslr_trigger_patch_list['dt_standard_still_start']['line_number']['BTC-7E'] = 56
dslr_trigger_patch_list['dt_standard_still_start']['line_number']['BTC-8E'] = 55
dslr_trigger_patch_list['dt_standard_still_start']['line_number']['BTC-7E-HP4'] = 70
dslr_trigger_patch_list['dt_standard_still_start']['line_number']['BTC-8E-HP4'] = 70
dslr_trigger_patch_list['dt_standard_still_start']['line_number']['BTC-7E-HP5'] = 75
dslr_trigger_patch_list['dt_standard_still_start']['line_number']['BTC-8E-HP5'] = 77
dslr_trigger_patch_list['dt_standard_still_start']['start_offset'] = {}
dslr_trigger_patch_list['dt_standard_still_start']['start_offset']['BTC-7A'] = 0x0126600
dslr_trigger_patch_list['dt_standard_still_start']['start_offset']['BTC-7E'] = 0x0126600
dslr_trigger_patch_list['dt_standard_still_start']['start_offset']['BTC-8E'] = 0x01269b0
dslr_trigger_patch_list['dt_standard_still_start']['start_offset']['BTC-7E-HP4'] = 0x0122cb0
dslr_trigger_patch_list['dt_standard_still_start']['start_offset']['BTC-8E-HP4'] = 0x01231f8
dslr_trigger_patch_list['dt_standard_still_start']['start_offset']['BTC-7E-HP5'] = 0x010612c
dslr_trigger_patch_list['dt_standard_still_start']['start_offset']['BTC-8E-HP5'] = 0x01061ec
dslr_trigger_patch_list['dt_standard_still_start']['change_from_jump'] = 'jal.cold_item_led_power_blur_reduction_p'
dslr_trigger_patch_list['dt_standard_still_start']['change_to_jump'] = 'jal.dt_cold_item_led_power_blur_reduction_p'

# in HceTaskStillBurst_task0
dslr_trigger_patch_list['dt_burst_still_start'] = {}
dslr_trigger_patch_list['dt_burst_still_start']['function'] = 'TaskStillBurstFSM_task0_init'
dslr_trigger_patch_list['dt_burst_still_start']['line_number'] = {}
dslr_trigger_patch_list['dt_burst_still_start']['line_number']['BTC-7A'] = 44
dslr_trigger_patch_list['dt_burst_still_start']['line_number']['BTC-7E'] = 44
dslr_trigger_patch_list['dt_burst_still_start']['line_number']['BTC-8E'] = 44
dslr_trigger_patch_list['dt_burst_still_start']['line_number']['BTC-7E-HP4'] = 49
dslr_trigger_patch_list['dt_burst_still_start']['line_number']['BTC-8E-HP4'] = 49
dslr_trigger_patch_list['dt_burst_still_start']['line_number']['BTC-7E-HP5'] = 52
dslr_trigger_patch_list['dt_burst_still_start']['line_number']['BTC-8E-HP5'] = 48
dslr_trigger_patch_list['dt_burst_still_start']['start_offset'] = {}
dslr_trigger_patch_list['dt_burst_still_start']['start_offset']['BTC-7A'] = 0x012842c
dslr_trigger_patch_list['dt_burst_still_start']['start_offset']['BTC-7E'] = 0x012842c
dslr_trigger_patch_list['dt_burst_still_start']['start_offset']['BTC-8E'] = 0x01287d4
dslr_trigger_patch_list['dt_burst_still_start']['start_offset']['BTC-7E-HP4'] = 0x0124b28
dslr_trigger_patch_list['dt_burst_still_start']['start_offset']['BTC-8E-HP4'] = 0x0125068
dslr_trigger_patch_list['dt_burst_still_start']['start_offset']['BTC-7E-HP5'] = 0x0108028
dslr_trigger_patch_list['dt_burst_still_start']['start_offset']['BTC-8E-HP5'] = 0x01080e0
dslr_trigger_patch_list['dt_burst_still_start']['change_from_jump'] = 'jal.cold_item_led_power_blur_reduction_p'
dslr_trigger_patch_list['dt_burst_still_start']['change_to_jump'] = 'jal.dt_cold_item_led_power_blur_reduction_p'

# HceTaskRecording_RecVideoToRec
dslr_trigger_patch_list['dt_video_start'] = {}
dslr_trigger_patch_list['dt_video_start']['function'] = 'HceTaskRecording_RecVideoToRec'
dslr_trigger_patch_list['dt_video_start']['line_number'] = {}
dslr_trigger_patch_list['dt_video_start']['line_number']['BTC-7A'] = 11
dslr_trigger_patch_list['dt_video_start']['line_number']['BTC-7E'] = 11
dslr_trigger_patch_list['dt_video_start']['line_number']['BTC-8E'] = 10
dslr_trigger_patch_list['dt_video_start']['line_number']['BTC-7E-HP4'] = 13
dslr_trigger_patch_list['dt_video_start']['line_number']['BTC-8E-HP4'] = 13
dslr_trigger_patch_list['dt_video_start']['line_number']['BTC-7E-HP5'] = 33
dslr_trigger_patch_list['dt_video_start']['line_number']['BTC-8E-HP5'] = 31
dslr_trigger_patch_list['dt_video_start']['start_offset'] = {}
dslr_trigger_patch_list['dt_video_start']['start_offset']['BTC-7A'] = 0x01243a0
dslr_trigger_patch_list['dt_video_start']['start_offset']['BTC-7E'] = 0x01243a0
dslr_trigger_patch_list['dt_video_start']['start_offset']['BTC-8E'] = 0x0124760
dslr_trigger_patch_list['dt_video_start']['start_offset']['BTC-7E-HP4'] = 0x011fc80
dslr_trigger_patch_list['dt_video_start']['start_offset']['BTC-8E-HP4'] = 0x01201d8
dslr_trigger_patch_list['dt_video_start']['start_offset']['BTC-7E-HP5'] = 0x0102f88
dslr_trigger_patch_list['dt_video_start']['start_offset']['BTC-8E-HP5'] = 0x0103060
dslr_trigger_patch_list['dt_video_start']['change_from_jump'] = 'jal.log_printf'
dslr_trigger_patch_list['dt_video_start']['change_to_jump'] = 'jal.dt_video_log_printf_hook'

# Turning LED Off
# in HceTaskStill_End
dslr_trigger_patch_list['dt_standard_still_end'] = {}
dslr_trigger_patch_list['dt_standard_still_end']['function'] = 'in HceTaskStill_End'
dslr_trigger_patch_list['dt_standard_still_end']['line_number'] = {}
dslr_trigger_patch_list['dt_standard_still_end']['line_number']['BTC-7A'] = 14
dslr_trigger_patch_list['dt_standard_still_end']['line_number']['BTC-7E'] = 14
dslr_trigger_patch_list['dt_standard_still_end']['line_number']['BTC-8E'] = 14
dslr_trigger_patch_list['dt_standard_still_end']['line_number']['BTC-7E-HP4'] = 17
dslr_trigger_patch_list['dt_standard_still_end']['line_number']['BTC-8E-HP4'] = 18
dslr_trigger_patch_list['dt_standard_still_end']['line_number']['BTC-7E-HP5'] = 17
dslr_trigger_patch_list['dt_standard_still_end']['line_number']['BTC-8E-HP5'] = 18
dslr_trigger_patch_list['dt_standard_still_end']['start_offset'] = {}
dslr_trigger_patch_list['dt_standard_still_end']['start_offset']['BTC-7A'] = 0x00125a80
dslr_trigger_patch_list['dt_standard_still_end']['start_offset']['BTC-7E'] = 0x00125a80
dslr_trigger_patch_list['dt_standard_still_end']['start_offset']['BTC-8E'] = 0x00125e38
dslr_trigger_patch_list['dt_standard_still_end']['start_offset']['BTC-7E-HP4'] = 0x00121a44
dslr_trigger_patch_list['dt_standard_still_end']['start_offset']['BTC-8E-HP4'] = 0x00121f94
dslr_trigger_patch_list['dt_standard_still_end']['start_offset']['BTC-7E-HP5'] = 0x0104ef8
dslr_trigger_patch_list['dt_standard_still_end']['start_offset']['BTC-8E-HP5'] = 0x0104fc0
dslr_trigger_patch_list['dt_standard_still_end']['change_from_jump']  = 'jal.IRLedOff'
dslr_trigger_patch_list['dt_standard_still_end']['change_to_jump'] = 'jal.dt_IRLedOff'

# in HceBurstStill_End
dslr_trigger_patch_list['dt_burst_still_end'] = {}
dslr_trigger_patch_list['dt_burst_still_end']['function'] = 'HceTaskStillBurst_End'
dslr_trigger_patch_list['dt_burst_still_end']['line_number'] = {}
dslr_trigger_patch_list['dt_burst_still_end']['line_number']['BTC-7A'] = 14
dslr_trigger_patch_list['dt_burst_still_end']['line_number']['BTC-7E'] = 14
dslr_trigger_patch_list['dt_burst_still_end']['line_number']['BTC-8E'] = 14
dslr_trigger_patch_list['dt_burst_still_end']['line_number']['BTC-7E-HP4'] = 14
dslr_trigger_patch_list['dt_burst_still_end']['line_number']['BTC-8E-HP4'] = 14
dslr_trigger_patch_list['dt_burst_still_end']['line_number']['BTC-7E-HP5'] = 14
dslr_trigger_patch_list['dt_burst_still_end']['line_number']['BTC-8E-HP5'] = 14
dslr_trigger_patch_list['dt_burst_still_end']['start_offset'] = {}
dslr_trigger_patch_list['dt_burst_still_end']['start_offset']['BTC-7A'] = 0x01274b0
dslr_trigger_patch_list['dt_burst_still_end']['start_offset']['BTC-7E'] = 0x01274b0
dslr_trigger_patch_list['dt_burst_still_end']['start_offset']['BTC-8E'] = 0x0127860
dslr_trigger_patch_list['dt_burst_still_end']['start_offset']['BTC-7E-HP4'] = 0x0123b70
dslr_trigger_patch_list['dt_burst_still_end']['start_offset']['BTC-8E-HP4'] = 0x01240b8
dslr_trigger_patch_list['dt_burst_still_end']['start_offset']['BTC-7E-HP5'] = 0x0106fa0
dslr_trigger_patch_list['dt_burst_still_end']['start_offset']['BTC-8E-HP5'] = 0x0107060
dslr_trigger_patch_list['dt_burst_still_end']['change_from_jump']  = 'jal.IRLedOff'
dslr_trigger_patch_list['dt_burst_still_end']['change_to_jump'] = 'jal.dt_IRLedOff'

# in TaskRecording_FSM_task10
dslr_trigger_patch_list['dt_video_end'] = {}
dslr_trigger_patch_list['dt_video_end']['function'] = {}
dslr_trigger_patch_list['dt_video_end']['function']['BTC-7A'] = 'TaskRecording_FSM_task9'
dslr_trigger_patch_list['dt_video_end']['function']['BTC-7E'] = 'TaskRecording_FSM_task9'
dslr_trigger_patch_list['dt_video_end']['function']['BTC-8E'] = 'TaskRecording_FSM_task10'
dslr_trigger_patch_list['dt_video_end']['function']['BTC-7E-HP4'] = 'TaskRecording_FSM_task9'
dslr_trigger_patch_list['dt_video_end']['function']['BTC-8E-HP4'] = 'TaskRecording_FSM_task10'
dslr_trigger_patch_list['dt_video_end']['function']['BTC-7E-HP5'] = 'TaskRecording_FSM_task10'
dslr_trigger_patch_list['dt_video_end']['function']['BTC-8E-HP5'] = 'TaskRecording_FSM_task10'
dslr_trigger_patch_list['dt_video_end']['line_number'] = {}
dslr_trigger_patch_list['dt_video_end']['line_number']['BTC-7A'] = 78
dslr_trigger_patch_list['dt_video_end']['line_number']['BTC-7E'] = 78
dslr_trigger_patch_list['dt_video_end']['line_number']['BTC-8E'] = 78
dslr_trigger_patch_list['dt_video_end']['line_number']['BTC-7E-HP4'] = 70
dslr_trigger_patch_list['dt_video_end']['line_number']['BTC-8E-HP4'] = 71
dslr_trigger_patch_list['dt_video_end']['line_number']['BTC-7E-HP5'] = 71
dslr_trigger_patch_list['dt_video_end']['line_number']['BTC-8E-HP5'] = 71
dslr_trigger_patch_list['dt_video_end']['start_offset'] = {}
dslr_trigger_patch_list['dt_video_end']['start_offset']['BTC-7A'] = 0x00123e28
dslr_trigger_patch_list['dt_video_end']['start_offset']['BTC-7E'] = 0x00123e28
dslr_trigger_patch_list['dt_video_end']['start_offset']['BTC-8E'] = 0x001241e8
dslr_trigger_patch_list['dt_video_end']['start_offset']['BTC-7E-HP4'] = 0x0011fbfc
dslr_trigger_patch_list['dt_video_end']['start_offset']['BTC-8E-HP4'] = 0x00120154
dslr_trigger_patch_list['dt_video_end']['start_offset']['BTC-7E-HP5'] = 0x0102ea0
dslr_trigger_patch_list['dt_video_end']['start_offset']['BTC-8E-HP5'] = 0x0102f78
dslr_trigger_patch_list['dt_video_end']['change_from_jump']  = 'jal.IRLedOff'
dslr_trigger_patch_list['dt_video_end']['change_to_jump'] = 'jal.dt_IRLedOff'



##########################################################################
################# pressure/temperature sensor patches ####################

pressure_temperature_patch_list = {}

# write_pressure_temperature_sensor()
# line 10
pressure_temperature_patch_list['wr_pt_sensor'] = {}
pressure_temperature_patch_list['wr_pt_sensor']['function'] = 'write_pressure_temperature_sensor'
pressure_temperature_patch_list['wr_pt_sensor']['line_number'] = {}
pressure_temperature_patch_list['wr_pt_sensor']['line_number'] = 10
pressure_temperature_patch_list['wr_pt_sensor']['start_offset'] = {}
pressure_temperature_patch_list['wr_pt_sensor']['start_offset']['BTC-8E'] = 0x12dcb0
pressure_temperature_patch_list['wr_pt_sensor']['change_from_bytes'] = bytes([0xee, 0x00, 0x04, 0x24])
pressure_temperature_patch_list['wr_pt_sensor']['change_to_bytes']   = bytes([0xec, 0x00, 0x04, 0x24])
# write_pressure_temperature_sensor_wait()
# line 7
pressure_temperature_patch_list['wr_pt_sensor_wait'] = {}
pressure_temperature_patch_list['wr_pt_sensor_wait']['function'] = 'write_pressure_temperature_sensor_wait'
pressure_temperature_patch_list['wr_pt_sensor_wait']['line_number'] = {}
pressure_temperature_patch_list['wr_pt_sensor_wait']['line_number']['BTC-8E'] = 7
pressure_temperature_patch_list['wr_pt_sensor_wait']['start_offset'] = {}
pressure_temperature_patch_list['wr_pt_sensor_wait']['start_offset']['BTC-8E'] = 0x12dd54
pressure_temperature_patch_list['wr_pt_sensor_wait']['change_from_bytes'] = bytes([0xee, 0x00, 0x04, 0x24])
pressure_temperature_patch_list['wr_pt_sensor_wait']['change_to_bytes']   = bytes([0xec, 0x00, 0x04, 0x24])
# read_pressure_temperature_device()
# line 7
pressure_temperature_patch_list['rd_pt_sensor'] = {}
pressure_temperature_patch_list['rd_pt_sensor']['function'] = 'read_pressure_temperature_device'
pressure_temperature_patch_list['rd_pt_sensor']['line_number'] = {}
pressure_temperature_patch_list['rd_pt_sensor']['line_number']['BTC-8E'] = 7
pressure_temperature_patch_list['rd_pt_sensor']['start_offset'] = {}
pressure_temperature_patch_list['rd_pt_sensor']['start_offset']['BTC-8E'] = 0x12dd9c
pressure_temperature_patch_list['rd_pt_sensor']['change_from_bytes'] = bytes([0xee, 0x00, 0x04, 0x24])
pressure_temperature_patch_list['rd_pt_sensor']['change_to_bytes']   = bytes([0xec, 0x00, 0x04, 0x24])
# Pressure_sensor_getReading()
# line 43
pressure_temperature_patch_list['p_sensor_get'] = {}
pressure_temperature_patch_list['p_sensor_get']['function'] = 'Pressure_sensor_getReading'
pressure_temperature_patch_list['p_sensor_get']['line_number'] = {}
pressure_temperature_patch_list['p_sensor_get']['line_number']['BTC-8E'] = 43
pressure_temperature_patch_list['p_sensor_get']['start_offset'] = {}
pressure_temperature_patch_list['p_sensor_get']['start_offset']['BTC-8E'] = 0x12de94
pressure_temperature_patch_list['p_sensor_get']['change_from_bytes'] = bytes([0xee, 0x00, 0x04, 0x24])
pressure_temperature_patch_list['p_sensor_get']['change_to_bytes']   = bytes([0xec, 0x00, 0x04, 0x24])
# Pressure_sensor_init()
# line 35
pressure_temperature_patch_list['p_sensor_init'] = {}
pressure_temperature_patch_list['p_sensor_init']['function'] = 'Pressure_sensor_init'
pressure_temperature_patch_list['p_sensor_init']['line_number'] = {}
pressure_temperature_patch_list['p_sensor_init']['line_number']['BTC-8E'] = 35
pressure_temperature_patch_list['p_sensor_init']['start_offset'] = {}
pressure_temperature_patch_list['p_sensor_init']['start_offset']['BTC-8E'] = 0x12e220
pressure_temperature_patch_list['p_sensor_init']['change_from_bytes'] = bytes([0xee, 0x00, 0x04, 0x24])
pressure_temperature_patch_list['p_sensor_init']['change_to_bytes']   = bytes([0xec, 0x00, 0x04, 0x24])

################# Timelapse Patches ######################################
timelapse_patch_list = {}

################# Timelapse Frequency Patches ############################

# in encoded_timelapse_frequency_to_seconds()
# line 5
timelapse_patch_list['decoder_function'] = {}
timelapse_patch_list['decoder_function']['function'] = 'encoded_timelapse_frequency_to_seconds'
timelapse_patch_list['decoder_function']['line_number'] = {}
timelapse_patch_list['decoder_function']['line_number']['BTC-7A'] = 5
timelapse_patch_list['decoder_function']['line_number']['BTC-7E'] = 5
timelapse_patch_list['decoder_function']['line_number']['BTC-8E'] = 5
timelapse_patch_list['decoder_function']['line_number']['BTC-7E-HP4'] = 5
timelapse_patch_list['decoder_function']['line_number']['BTC-8E-HP4'] = 5
timelapse_patch_list['decoder_function']['line_number']['BTC-7E-HP5'] = 5
timelapse_patch_list['decoder_function']['line_number']['BTC-8E-HP5'] = 5
timelapse_patch_list['decoder_function']['start_offset'] = {}
timelapse_patch_list['decoder_function']['start_offset']['BTC-7A'] = 0x0110158
timelapse_patch_list['decoder_function']['start_offset']['BTC-7E'] = 0x0110158
timelapse_patch_list['decoder_function']['start_offset']['BTC-8E'] = 0x0110388
timelapse_patch_list['decoder_function']['start_offset']['BTC-7E-HP4'] = 0x010b574
timelapse_patch_list['decoder_function']['start_offset']['BTC-8E-HP4'] = 0x010ba74
timelapse_patch_list['decoder_function']['start_offset']['BTC-7E-HP5'] = 0x00e7e08
timelapse_patch_list['decoder_function']['start_offset']['BTC-8E-HP5'] = 0x00e7ec4
timelapse_patch_list['decoder_function']['change_from_bytes'] = {}
timelapse_patch_list['decoder_function']['change_from_bytes']['BTC-7A'] = bytes([0x35, 0x80, 0x02, 0x3c])
timelapse_patch_list['decoder_function']['change_from_bytes']['BTC-7E'] = bytes([0x35, 0x80, 0x02, 0x3c])
timelapse_patch_list['decoder_function']['change_from_bytes']['BTC-8E'] = bytes([0x35, 0x80, 0x02, 0x3c])
timelapse_patch_list['decoder_function']['change_from_bytes']['BTC-7E-HP4'] = bytes([0x35, 0x80, 0x02, 0x3c])
timelapse_patch_list['decoder_function']['change_from_bytes']['BTC-8E-HP4'] = bytes([0x36, 0x80, 0x02, 0x3c])
timelapse_patch_list['decoder_function']['change_from_bytes']['BTC-7E-HP5'] = bytes([0x2d, 0x80, 0x02, 0x3c])
timelapse_patch_list['decoder_function']['change_from_bytes']['BTC-8E-HP5'] = bytes([0x2d, 0x80, 0x02, 0x3c])
timelapse_patch_list['decoder_function']['change_to_jump'] = 'j.tlps_encoded_timelapse_frequency_to_seconds'

# in HceTaskTimelapseFSM_iterator(void) ----
# line 23 -- fix the check on FSM state size
timelapse_patch_list['tlps_function_count'] = {}
timelapse_patch_list['tlps_function_count']['function'] = 'TaskTimelapseFSM_iterator'
timelapse_patch_list['tlps_function_count']['line_number'] = {}
timelapse_patch_list['tlps_function_count']['line_number']['BTC-7A'] = 23
timelapse_patch_list['tlps_function_count']['line_number']['BTC-7E'] = 23
timelapse_patch_list['tlps_function_count']['line_number']['BTC-8E'] = 23
timelapse_patch_list['tlps_function_count']['line_number']['BTC-7E-HP4'] = 23
timelapse_patch_list['tlps_function_count']['line_number']['BTC-8E-HP4'] = 23
timelapse_patch_list['tlps_function_count']['line_number']['BTC-7E-HP5'] = 23
timelapse_patch_list['tlps_function_count']['line_number']['BTC-8E-HP5'] = 23
timelapse_patch_list['tlps_function_count']['start_offset'] = {}
timelapse_patch_list['tlps_function_count']['start_offset']['BTC-7A'] = 0x0128804
timelapse_patch_list['tlps_function_count']['start_offset']['BTC-7E'] = 0x0128804
timelapse_patch_list['tlps_function_count']['start_offset']['BTC-8E'] = 0x0128bac
timelapse_patch_list['tlps_function_count']['start_offset']['BTC-7E-HP4'] = 0x0124eb0
timelapse_patch_list['tlps_function_count']['start_offset']['BTC-8E-HP4'] = 0x01253f0
timelapse_patch_list['tlps_function_count']['start_offset']['BTC-7E-HP5'] = 0x0108334
timelapse_patch_list['tlps_function_count']['start_offset']['BTC-8E-HP5'] = 0x01083ec
timelapse_patch_list['tlps_function_count']['change_from_bytes'] = bytes([0x0f, 0x00, 0x42, 0x2c])
timelapse_patch_list['tlps_function_count']['change_to_bytes']   = bytes([0x10, 0x00, 0x42, 0x2c])
# in HceTaskTimelapseFSM_iterator(void)
# source line 28 -- clobber the indirection -- just pass index as argument
timelapse_patch_list['tlps_index_argument'] = {}
timelapse_patch_list['tlps_index_argument']['function'] = 'TaskTimelapseFSM_iterator'
timelapse_patch_list['tlps_index_argument']['line_number'] = {}
timelapse_patch_list['tlps_index_argument']['line_number']['BTC-7A'] = 28
timelapse_patch_list['tlps_index_argument']['line_number']['BTC-7E'] = 28
timelapse_patch_list['tlps_index_argument']['line_number']['BTC-8E'] = 28
timelapse_patch_list['tlps_index_argument']['line_number']['BTC-7E-HP4'] = 28
timelapse_patch_list['tlps_index_argument']['line_number']['BTC-8E-HP4'] = 28
timelapse_patch_list['tlps_index_argument']['line_number']['BTC-7E-HP5'] = 28
timelapse_patch_list['tlps_index_argument']['line_number']['BTC-8E-HP5'] = 28
timelapse_patch_list['tlps_index_argument']['start_offset'] = {}
timelapse_patch_list['tlps_index_argument']['start_offset']['BTC-7A'] = 0x0128818
timelapse_patch_list['tlps_index_argument']['start_offset']['BTC-7E'] = 0x0128818
timelapse_patch_list['tlps_index_argument']['start_offset']['BTC-8E'] = 0x0128bc0
timelapse_patch_list['tlps_index_argument']['start_offset']['BTC-7E-HP4'] = 0x0124ec4
timelapse_patch_list['tlps_index_argument']['start_offset']['BTC-8E-HP4'] = 0x0125404
timelapse_patch_list['tlps_index_argument']['start_offset']['BTC-7E-HP5'] = 0x0108348
timelapse_patch_list['tlps_index_argument']['start_offset']['BTC-8E-HP5'] = 0x0108400
timelapse_patch_list['tlps_index_argument']['change_from_bytes'] = bytes([0x00, 0x00, 0x44, 0x8c])
timelapse_patch_list['tlps_index_argument']['change_to_bytes']   = bytes([0x00, 0x20, 0x40, 0x80])
# in HceTaskTimelapseFSM_iterator(void)
# source line 28 -- replace call to our own execute function
timelapse_patch_list['tlps_fsm'] = {}
timelapse_patch_list['tlps_fsm']['function'] = 'TaskTimelapseFSM_iterator'
timelapse_patch_list['tlps_fsm']['line_number'] = {}
timelapse_patch_list['tlps_fsm']['line_number']['BTC-7A'] = 27
timelapse_patch_list['tlps_fsm']['line_number']['BTC-7E'] = 28
timelapse_patch_list['tlps_fsm']['line_number']['BTC-8E'] = 28
timelapse_patch_list['tlps_fsm']['line_number']['BTC-7E-HP4'] = 28
timelapse_patch_list['tlps_fsm']['line_number']['BTC-8E-HP4'] = 28
timelapse_patch_list['tlps_fsm']['line_number']['BTC-7E-HP5'] = 28
timelapse_patch_list['tlps_fsm']['line_number']['BTC-8E-HP5'] = 28
timelapse_patch_list['tlps_fsm']['start_offset'] = {}
timelapse_patch_list['tlps_fsm']['start_offset']['BTC-7A'] = 0x012881c
timelapse_patch_list['tlps_fsm']['start_offset']['BTC-7E'] = 0x012881c
timelapse_patch_list['tlps_fsm']['start_offset']['BTC-8E'] = 0x0128bc4
timelapse_patch_list['tlps_fsm']['start_offset']['BTC-7E-HP4'] = 0x0124ec8
timelapse_patch_list['tlps_fsm']['start_offset']['BTC-8E-HP4'] = 0x0125408
timelapse_patch_list['tlps_fsm']['start_offset']['BTC-7E-HP5'] = 0x010834c
timelapse_patch_list['tlps_fsm']['start_offset']['BTC-8E-HP5'] = 0x0108404
timelapse_patch_list['tlps_fsm']['change_from_jump'] = 'jal.execute_if_not_null'
timelapse_patch_list['tlps_fsm']['change_to_jump'] = 'jal.tlps_execute_if_not_null'

# fix the next state pointers to go to new end state 14 (now 15)
# in TaskTimeLapseFSM_task0()
# line 40
timelapse_patch_list['tlps_t0_next_state'] = {}
timelapse_patch_list['tlps_t0_next_state']['function'] = 'TaskTimeLapseFSM_task0'
timelapse_patch_list['tlps_t0_next_state']['line_number'] = {}
timelapse_patch_list['tlps_t0_next_state']['line_number']['BTC-7A'] = 40
timelapse_patch_list['tlps_t0_next_state']['line_number']['BTC-7E'] = 40
timelapse_patch_list['tlps_t0_next_state']['line_number']['BTC-8E'] = 40
timelapse_patch_list['tlps_t0_next_state']['line_number']['BTC-7E-HP4'] = 40
timelapse_patch_list['tlps_t0_next_state']['line_number']['BTC-8E-HP4'] = 40
timelapse_patch_list['tlps_t0_next_state']['line_number']['BTC-7E-HP5'] = 40
timelapse_patch_list['tlps_t0_next_state']['line_number']['BTC-8E-HP5'] = 40
timelapse_patch_list['tlps_t0_next_state']['start_offset'] = {}
timelapse_patch_list['tlps_t0_next_state']['start_offset']['BTC-7A'] = 0x0129b88
timelapse_patch_list['tlps_t0_next_state']['start_offset']['BTC-7E'] = 0x0129b88
timelapse_patch_list['tlps_t0_next_state']['start_offset']['BTC-8E'] = 0x0129f28
timelapse_patch_list['tlps_t0_next_state']['start_offset']['BTC-7E-HP4'] = 0x012623c
timelapse_patch_list['tlps_t0_next_state']['start_offset']['BTC-8E-HP4'] = 0x0126774
timelapse_patch_list['tlps_t0_next_state']['start_offset']['BTC-7E-HP5'] = 0x01096c8
timelapse_patch_list['tlps_t0_next_state']['start_offset']['BTC-8E-HP5'] = 0x0109778
timelapse_patch_list['tlps_t0_next_state']['change_from_bytes'] = bytes([0x0e, 0x00, 0x04, 0x24])
timelapse_patch_list['tlps_t0_next_state']['change_to_bytes']   = bytes([0x0f, 0x00, 0x04, 0x24])

# fix the next state pointers to go to new state 12a (now 13)
# in TaskTimeLapseFSM_task7()
# line 58
timelapse_patch_list['tlps_t7_next_state'] = {}
timelapse_patch_list['tlps_t7_next_state']['function'] = 'TaskTimeLapseFSM_task7'
timelapse_patch_list['tlps_t7_next_state']['line_number'] = {}
timelapse_patch_list['tlps_t7_next_state']['line_number']['BTC-7A'] = 58
timelapse_patch_list['tlps_t7_next_state']['line_number']['BTC-7E'] = 58
timelapse_patch_list['tlps_t7_next_state']['line_number']['BTC-8E'] = 58
timelapse_patch_list['tlps_t7_next_state']['line_number']['BTC-7E-HP4'] = 57
timelapse_patch_list['tlps_t7_next_state']['line_number']['BTC-8E-HP4'] = 57
timelapse_patch_list['tlps_t7_next_state']['line_number']['BTC-7E-HP5'] = 58
timelapse_patch_list['tlps_t7_next_state']['line_number']['BTC-8E-HP5'] = 58
timelapse_patch_list['tlps_t7_next_state']['start_offset'] = {}
timelapse_patch_list['tlps_t7_next_state']['start_offset']['BTC-7A'] = 0x0129624
timelapse_patch_list['tlps_t7_next_state']['start_offset']['BTC-7E'] = 0x0129624
timelapse_patch_list['tlps_t7_next_state']['start_offset']['BTC-8E'] = 0x01299cc
timelapse_patch_list['tlps_t7_next_state']['start_offset']['BTC-7E-HP4'] = 0x0125cd0
timelapse_patch_list['tlps_t7_next_state']['start_offset']['BTC-8E-HP4'] = 0x0126210
timelapse_patch_list['tlps_t7_next_state']['start_offset']['BTC-7E-HP5'] = 0x010914c
timelapse_patch_list['tlps_t7_next_state']['start_offset']['BTC-8E-HP5'] = 0x0109204
timelapse_patch_list['tlps_t7_next_state']['change_from_bytes'] = bytes([0x0c, 0x00, 0x04, 0x24])
timelapse_patch_list['tlps_t7_next_state']['change_to_bytes']   = bytes([0x0d, 0x00, 0x04, 0x24])

# fix the next state pointers to go to new state 12a (now 13)
# in TaskTimeLapseFSM_task11()
# line 390
timelapse_patch_list['tlps_t11_next_state'] = {}
timelapse_patch_list['tlps_t11_next_state']['function'] = 'TaskTimeLapseFSM_task11'
timelapse_patch_list['tlps_t11_next_state']['line_number'] = {}
timelapse_patch_list['tlps_t11_next_state']['line_number']['BTC-7A'] = 392
timelapse_patch_list['tlps_t11_next_state']['line_number']['BTC-7E'] = 392
timelapse_patch_list['tlps_t11_next_state']['line_number']['BTC-8E'] = 391
timelapse_patch_list['tlps_t11_next_state']['line_number']['BTC-7E-HP4'] = 386
timelapse_patch_list['tlps_t11_next_state']['line_number']['BTC-8E-HP4'] = 386
timelapse_patch_list['tlps_t11_next_state']['line_number']['BTC-7E-HP5'] = 387
timelapse_patch_list['tlps_t11_next_state']['line_number']['BTC-8E-HP5'] = 402
timelapse_patch_list['tlps_t11_next_state']['start_offset'] = {}
timelapse_patch_list['tlps_t11_next_state']['start_offset']['BTC-7A'] = 0x0129320
timelapse_patch_list['tlps_t11_next_state']['start_offset']['BTC-7E'] = 0x0129320
timelapse_patch_list['tlps_t11_next_state']['start_offset']['BTC-8E'] = 0x01296c8
timelapse_patch_list['tlps_t11_next_state']['start_offset']['BTC-7E-HP4'] = 0x01259cc
timelapse_patch_list['tlps_t11_next_state']['start_offset']['BTC-8E-HP4'] = 0x0125f0c
timelapse_patch_list['tlps_t11_next_state']['start_offset']['BTC-7E-HP5'] = 0x0108e48
timelapse_patch_list['tlps_t11_next_state']['start_offset']['BTC-8E-HP5'] = 0x0108f00
timelapse_patch_list['tlps_t11_next_state']['change_from_bytes'] = bytes([0x01, 0x00, 0x04, 0x24])
timelapse_patch_list['tlps_t11_next_state']['change_to_bytes']   = bytes([0x02, 0x00, 0x04, 0x24])

# fix the next state pointers to skip over new task_12a
# in TaskTimeLapseFSM_task12()
# line 11
timelapse_patch_list['tlps_t12_next_state_0'] = {}
timelapse_patch_list['tlps_t12_next_state_0']['function'] = 'TaskTimeLapseFSM_task12'
timelapse_patch_list['tlps_t12_next_state_0']['line_number'] = {}
timelapse_patch_list['tlps_t12_next_state_0']['line_number']['BTC-7A'] = 11
timelapse_patch_list['tlps_t12_next_state_0']['line_number']['BTC-7E'] = 11
timelapse_patch_list['tlps_t12_next_state_0']['line_number']['BTC-8E'] = 11
timelapse_patch_list['tlps_t12_next_state_0']['line_number']['BTC-7E-HP4'] = 11
timelapse_patch_list['tlps_t12_next_state_0']['line_number']['BTC-8E-HP4'] = 11
timelapse_patch_list['tlps_t12_next_state_0']['start_offset'] = {}
timelapse_patch_list['tlps_t12_next_state_0']['start_offset']['BTC-7A'] = 0x0129c00
timelapse_patch_list['tlps_t12_next_state_0']['start_offset']['BTC-7E'] = 0x0129c00
timelapse_patch_list['tlps_t12_next_state_0']['start_offset']['BTC-8E'] = 0x0129fa0
timelapse_patch_list['tlps_t12_next_state_0']['start_offset']['BTC-7E-HP4'] = 0x01262b4
timelapse_patch_list['tlps_t12_next_state_0']['start_offset']['BTC-8E-HP4'] = 0x01267ec
timelapse_patch_list['tlps_t12_next_state_0']['start_offset']['BTC-7E-HP5'] =  0x0109740
timelapse_patch_list['tlps_t12_next_state_0']['start_offset']['BTC-8E-HP5'] = 0x01097f0
timelapse_patch_list['tlps_t12_next_state_0']['change_from_bytes'] = bytes([0x02, 0x00, 0x04, 0x24])
timelapse_patch_list['tlps_t12_next_state_0']['change_to_bytes']   = bytes([0x03, 0x00, 0x04, 0x24])
# in TaskTimeLapseFSM_task12()
# line 15
timelapse_patch_list['tlps_t12_next_state_1'] = {}
timelapse_patch_list['tlps_t12_next_state_1']['function'] = 'TaskTimeLapseFSM_task12'
timelapse_patch_list['tlps_t12_next_state_1']['line_number'] = {}
timelapse_patch_list['tlps_t12_next_state_1']['line_number']['BTC-7A'] = 15
timelapse_patch_list['tlps_t12_next_state_1']['line_number']['BTC-7E'] = 15
timelapse_patch_list['tlps_t12_next_state_1']['line_number']['BTC-8E'] = 15
timelapse_patch_list['tlps_t12_next_state_1']['line_number']['BTC-7E-HP4'] = 15
timelapse_patch_list['tlps_t12_next_state_1']['line_number']['BTC-8E-HP4'] = 15
timelapse_patch_list['tlps_t12_next_state_1']['line_number']['BTC-7E-HP5'] = 15
timelapse_patch_list['tlps_t12_next_state_1']['line_number']['BTC-8E-HP5'] = 15
timelapse_patch_list['tlps_t12_next_state_1']['start_offset'] = {}
timelapse_patch_list['tlps_t12_next_state_1']['start_offset']['BTC-7A'] = 0x0129c10
timelapse_patch_list['tlps_t12_next_state_1']['start_offset']['BTC-7E'] = 0x0129c10
timelapse_patch_list['tlps_t12_next_state_1']['start_offset']['BTC-8E'] = 0x0129fb0
timelapse_patch_list['tlps_t12_next_state_1']['start_offset']['BTC-7E-HP4'] = 0x01262c4
timelapse_patch_list['tlps_t12_next_state_1']['start_offset']['BTC-8E-HP4'] = 0x01267fc
timelapse_patch_list['tlps_t12_next_state_1']['start_offset']['BTC-7E-HP5'] = 0x0109750
timelapse_patch_list['tlps_t12_next_state_1']['start_offset']['BTC-8E-HP5'] = 0x0109800
timelapse_patch_list['tlps_t12_next_state_1']['change_from_bytes'] = bytes([0x01, 0x00, 0x04, 0x24])
timelapse_patch_list['tlps_t12_next_state_1']['change_to_bytes']   = bytes([0x02, 0x00, 0x04, 0x24])
# in TaskTimeLapseFSM_task12()
# line 17
timelapse_patch_list['tlps_t12_next_state_2'] = {}
timelapse_patch_list['tlps_t12_next_state_2']['function'] = 'TaskTimeLapseFSM_task12'
timelapse_patch_list['tlps_t12_next_state_2']['line_number'] = {}
timelapse_patch_list['tlps_t12_next_state_2']['line_number']['BTC-7A'] = 17
timelapse_patch_list['tlps_t12_next_state_2']['line_number']['BTC-7E'] = 17
timelapse_patch_list['tlps_t12_next_state_2']['line_number']['BTC-8E'] = 17
timelapse_patch_list['tlps_t12_next_state_2']['line_number']['BTC-7E-HP4'] = 17
timelapse_patch_list['tlps_t12_next_state_2']['line_number']['BTC-8E-HP4'] = 17
timelapse_patch_list['tlps_t12_next_state_2']['line_number']['BTC-7E-HP5'] = 17
timelapse_patch_list['tlps_t12_next_state_2']['line_number']['BTC-8E-HP5'] = 17
timelapse_patch_list['tlps_t12_next_state_2']['start_offset'] = {}
timelapse_patch_list['tlps_t12_next_state_2']['start_offset']['BTC-7A'] = 0x0129c14
timelapse_patch_list['tlps_t12_next_state_2']['start_offset']['BTC-7E'] = 0x0129c14
timelapse_patch_list['tlps_t12_next_state_2']['start_offset']['BTC-8E'] = 0x0129fb4
timelapse_patch_list['tlps_t12_next_state_2']['start_offset']['BTC-7E-HP4'] = 0x01262c8
timelapse_patch_list['tlps_t12_next_state_2']['start_offset']['BTC-8E-HP4'] = 0x0126800
timelapse_patch_list['tlps_t12_next_state_2']['start_offset']['BTC-7E-HP5'] = 0x0109754
timelapse_patch_list['tlps_t12_next_state_2']['start_offset']['BTC-8E-HP5'] = 0x0109804
timelapse_patch_list['tlps_t12_next_state_2']['change_from_bytes'] = bytes([0x02, 0x00, 0x04, 0x24])
timelapse_patch_list['tlps_t12_next_state_2']['change_to_bytes']   = bytes([0x03, 0x00, 0x04, 0x24])


## Timelapse file mode patch(es)
# replace call to  handleSetTimeMenu in g_HceTaskMenuMultiItem_fsm_function_array
timelapse_patch_list['hce_task_boot_2_cap_task0'] = {}
timelapse_patch_list['hce_task_boot_2_cap_task0']['function'] = 'g_HceTaskBoot2Cap_FSM_FunctionArray'
timelapse_patch_list['hce_task_boot_2_cap_task0']['line_number'] = {}
timelapse_patch_list['hce_task_boot_2_cap_task0']['line_number']['BTC-7A'] = 0
timelapse_patch_list['hce_task_boot_2_cap_task0']['line_number']['BTC-7E'] = 0
timelapse_patch_list['hce_task_boot_2_cap_task0']['line_number']['BTC-8E'] = 0
timelapse_patch_list['hce_task_boot_2_cap_task0']['line_number']['BTC-7E-HP4'] = 0
timelapse_patch_list['hce_task_boot_2_cap_task0']['line_number']['BTC-8E-HP4'] = 0
timelapse_patch_list['hce_task_boot_2_cap_task0']['line_number']['BTC-7E-HP5'] = 0
timelapse_patch_list['hce_task_boot_2_cap_task0']['line_number']['BTC-8E-HP5'] = 0
timelapse_patch_list['hce_task_boot_2_cap_task0']['start_offset'] = {}
timelapse_patch_list['hce_task_boot_2_cap_task0']['start_offset']['BTC-7A'] = 0x0354b28
timelapse_patch_list['hce_task_boot_2_cap_task0']['start_offset']['BTC-7E'] = 0x0354b28
timelapse_patch_list['hce_task_boot_2_cap_task0']['start_offset']['BTC-8E'] = 0x0354b34
timelapse_patch_list['hce_task_boot_2_cap_task0']['start_offset']['BTC-7E-HP4'] = 0x0357ad0
timelapse_patch_list['hce_task_boot_2_cap_task0']['start_offset']['BTC-8E-HP4'] = 0x035bcb4
timelapse_patch_list['hce_task_boot_2_cap_task0']['start_offset']['BTC-7E-HP5'] = 0x02cd4c8
timelapse_patch_list['hce_task_boot_2_cap_task0']['start_offset']['BTC-8E-HP5'] = 0x02cf63c
timelapse_patch_list['hce_task_boot_2_cap_task0']['change_from_ptr'] = 'HceTaskBoot2Cap_Task0'
timelapse_patch_list['hce_task_boot_2_cap_task0']['change_to_ptr']   = 'tls_HceTaskBoot2Cap_Task0'

# Replace the call to HceIRCut_SetIRCutClosed()
timelapse_patch_list['tlps_HceIRCut'] = {}
timelapse_patch_list['tlps_HceIRCut']['function'] = 'TaskTimelapseFSM_task0'
timelapse_patch_list['tlps_HceIRCut']['line_number'] = {}
timelapse_patch_list['tlps_HceIRCut']['line_number']['BTC-7A'] = 36
timelapse_patch_list['tlps_HceIRCut']['line_number']['BTC-7E'] = 33
timelapse_patch_list['tlps_HceIRCut']['line_number']['BTC-8E'] = 36
timelapse_patch_list['tlps_HceIRCut']['line_number']['BTC-7E-HP4'] = 33
timelapse_patch_list['tlps_HceIRCut']['line_number']['BTC-8E-HP4'] = 33
timelapse_patch_list['tlps_HceIRCut']['line_number']['BTC-7E-HP5'] = 33
timelapse_patch_list['tlps_HceIRCut']['line_number']['BTC-8E-HP5'] = 33
timelapse_patch_list['tlps_HceIRCut']['start_offset'] = {}
timelapse_patch_list['tlps_HceIRCut']['start_offset']['BTC-7A'] = 0x0129b5c
timelapse_patch_list['tlps_HceIRCut']['start_offset']['BTC-7E'] = 0x0129b5c
timelapse_patch_list['tlps_HceIRCut']['start_offset']['BTC-8E'] = 0x0129efc
timelapse_patch_list['tlps_HceIRCut']['start_offset']['BTC-7E-HP4'] = 0x0126210
timelapse_patch_list['tlps_HceIRCut']['start_offset']['BTC-8E-HP4'] = 0x0126748
timelapse_patch_list['tlps_HceIRCut']['start_offset']['BTC-7E-HP5'] = 0x010969c
timelapse_patch_list['tlps_HceIRCut']['start_offset']['BTC-8E-HP5'] = 0x010974c
timelapse_patch_list['tlps_HceIRCut']['change_from_jump'] = 'jal.HceIRCut_SetIRCutClosed'
timelapse_patch_list['tlps_HceIRCut']['change_to_jump']   = 'jal.tlps_HceIRCut_SetIRCutClosed'


#### Support for "All Day/Night" Timelapse
# Replace the call to handleTimelapsePeriod_menu
timelapse_patch_list['tlps_handle_period_menu'] = {}
timelapse_patch_list['tlps_handle_period_menu']['function'] = 'handleTimelapsePeriod_menu'
timelapse_patch_list['tlps_handle_period_menu']['line_number'] = {}
timelapse_patch_list['tlps_handle_period_menu']['line_number']['BTC-7A'] = 15
timelapse_patch_list['tlps_handle_period_menu']['line_number']['BTC-7E'] = 15
timelapse_patch_list['tlps_handle_period_menu']['line_number']['BTC-8E'] = 14
timelapse_patch_list['tlps_handle_period_menu']['line_number']['BTC-7E-HP4'] = 15 
timelapse_patch_list['tlps_handle_period_menu']['line_number']['BTC-8E-HP4'] = 15
timelapse_patch_list['tlps_handle_period_menu']['line_number']['BTC-7E-HP5'] = 14
timelapse_patch_list['tlps_handle_period_menu']['line_number']['BTC-8E-HP5'] = 14 
timelapse_patch_list['tlps_handle_period_menu']['start_offset'] = {}
timelapse_patch_list['tlps_handle_period_menu']['start_offset']['BTC-7A'] = 0x0132ff8
timelapse_patch_list['tlps_handle_period_menu']['start_offset']['BTC-7E'] = 0x0132ff8
timelapse_patch_list['tlps_handle_period_menu']['start_offset']['BTC-8E'] = 0x0133bf4
timelapse_patch_list['tlps_handle_period_menu']['start_offset']['BTC-7E-HP4'] = 0x012f8a8
timelapse_patch_list['tlps_handle_period_menu']['start_offset']['BTC-8E-HP4'] = 0x01323d8
timelapse_patch_list['tlps_handle_period_menu']['start_offset']['BTC-7E-HP5'] = 0x0112630
timelapse_patch_list['tlps_handle_period_menu']['start_offset']['BTC-8E-HP5'] = 0x0112f88
timelapse_patch_list['tlps_handle_period_menu']['change_from_jump'] = 'jal.get_cold_item_timelapse_period'
timelapse_patch_list['tlps_handle_period_menu']['change_to_jump']   = 'jal.tlps_get_cold_item_raw_timelapse_period'


# Replace the get_cold_item_timelapse_period
timelapse_patch_list['tlps_get_timelapse_period'] = {}
timelapse_patch_list['tlps_get_timelapse_period']['function'] = 'get_cold_item_timelapse_period'
timelapse_patch_list['tlps_get_timelapse_period']['line_number'] = {}
timelapse_patch_list['tlps_get_timelapse_period']['line_number']['BTC-7A'] = 5
timelapse_patch_list['tlps_get_timelapse_period']['line_number']['BTC-7E'] = 5
timelapse_patch_list['tlps_get_timelapse_period']['line_number']['BTC-8E'] = 5
timelapse_patch_list['tlps_get_timelapse_period']['line_number']['BTC-7E-HP4'] = 5 
timelapse_patch_list['tlps_get_timelapse_period']['line_number']['BTC-8E-HP4'] = 5
timelapse_patch_list['tlps_get_timelapse_period']['line_number']['BTC-7E-HP5'] = 5
timelapse_patch_list['tlps_get_timelapse_period']['line_number']['BTC-8E-HP5'] = 7
timelapse_patch_list['tlps_get_timelapse_period']['start_offset'] = {}
timelapse_patch_list['tlps_get_timelapse_period']['start_offset']['BTC-7A'] = 0x010e460
timelapse_patch_list['tlps_get_timelapse_period']['start_offset']['BTC-7E'] = 0x010e460
timelapse_patch_list['tlps_get_timelapse_period']['start_offset']['BTC-8E'] = 0x010e5ec
timelapse_patch_list['tlps_get_timelapse_period']['start_offset']['BTC-7E-HP4'] = 0x010903c
timelapse_patch_list['tlps_get_timelapse_period']['start_offset']['BTC-8E-HP4'] = 0x010947c
timelapse_patch_list['tlps_get_timelapse_period']['start_offset']['BTC-7E-HP5'] = 0x00e5738
timelapse_patch_list['tlps_get_timelapse_period']['start_offset']['BTC-8E-HP5'] = 0x00e571c
timelapse_patch_list['tlps_get_timelapse_period']['change_from_bytes'] =  bytes([0x08, 0x00, 0xe0, 0x03])
timelapse_patch_list['tlps_get_timelapse_period']['change_to_jump']   = 'j.tlps_get_cold_item_cooked_timelapse_period'

## Replacing calls to get_tod_in_timelapse_region
## I don't think I need to change the following functions
##    print_timelapse_region_by_hour - this is only a diag print statement
##    HceTaskBoot2Cap_Task -- not necessary because we've already rewritten this function

##  spawnIRCutFSM_per_mode
timelapse_patch_list['tlps_spawnIRCutFSM'] = {}
timelapse_patch_list['tlps_spawnIRCutFSM']['function'] = 'spawnIRCutFSM_per_mode'
timelapse_patch_list['tlps_spawnIRCutFSM']['line_number'] = {}
timelapse_patch_list['tlps_spawnIRCutFSM']['line_number']['BTC-7A'] = 23
timelapse_patch_list['tlps_spawnIRCutFSM']['line_number']['BTC-7E'] = 23
timelapse_patch_list['tlps_spawnIRCutFSM']['line_number']['BTC-8E'] = 24
timelapse_patch_list['tlps_spawnIRCutFSM']['line_number']['BTC-7E-HP4'] = 23
timelapse_patch_list['tlps_spawnIRCutFSM']['line_number']['BTC-8E-HP4'] = 23
timelapse_patch_list['tlps_spawnIRCutFSM']['line_number']['BTC-7E-HP5'] = 24
timelapse_patch_list['tlps_spawnIRCutFSM']['line_number']['BTC-8E-HP5'] = 23 
timelapse_patch_list['tlps_spawnIRCutFSM']['start_offset'] = {}
timelapse_patch_list['tlps_spawnIRCutFSM']['start_offset']['BTC-7A'] = 0x01101e8
timelapse_patch_list['tlps_spawnIRCutFSM']['start_offset']['BTC-7E'] = 0x01101e8
timelapse_patch_list['tlps_spawnIRCutFSM']['start_offset']['BTC-8E'] = 0x0110418
timelapse_patch_list['tlps_spawnIRCutFSM']['start_offset']['BTC-7E-HP4'] = 0x010b60c
timelapse_patch_list['tlps_spawnIRCutFSM']['start_offset']['BTC-8E-HP4'] = 0x010bb0c
timelapse_patch_list['tlps_spawnIRCutFSM']['start_offset']['BTC-7E-HP5'] = 0x00e7ea0
timelapse_patch_list['tlps_spawnIRCutFSM']['start_offset']['BTC-8E-HP5'] = 0x00e7f5c
timelapse_patch_list['tlps_spawnIRCutFSM']['change_from_jump'] = 'jal.get_tod_in_timelapse_region'
timelapse_patch_list['tlps_spawnIRCutFSM']['change_to_jump']   = 'jal.tlps_get_tod_in_timelapse_region'


## HceIQ_PowerOnStateInit
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit'] = {}
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['function'] = 'HceIQ_PowerOnStateInit'
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['line_number'] = {}
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['line_number']['BTC-7A'] = 30
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['line_number']['BTC-7E'] = 30
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['line_number']['BTC-8E'] = 32
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['line_number']['BTC-7E-HP4'] = 26
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['line_number']['BTC-8E-HP4'] = 26
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['line_number']['BTC-7E-HP5'] = 27
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['line_number']['BTC-8E-HP5'] = 27
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['start_offset'] = {}
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['start_offset']['BTC-7A'] = 0x01105bc
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['start_offset']['BTC-7E'] = 0x01105bc
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['start_offset']['BTC-8E'] = 0x01107ec
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['start_offset']['BTC-7E-HP4'] = 0x010b9ec
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['start_offset']['BTC-8E-HP4'] = 0x010beec
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['start_offset']['BTC-7E-HP5'] = 0x00e8280
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['start_offset']['BTC-8E-HP5'] = 0x00e833c
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['change_from_jump'] = 'jal.get_tod_in_timelapse_region'
timelapse_patch_list['tlps_HceIQ_PowerOnStateInit']['change_to_jump']   = 'jal.tlps_get_tod_in_timelapse_region'

## update_timelapse_rise_set_times
timelapse_patch_list['tlps_update_timelapse_rise_set_times'] = {}
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['function'] = 'update_timelapse_rise_set_times'
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['line_number'] = {}
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['line_number']['BTC-7A'] = 20
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['line_number']['BTC-7E'] = 20 
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['line_number']['BTC-8E'] = 22
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['line_number']['BTC-7E-HP4'] = 20
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['line_number']['BTC-8E-HP4'] = 20 
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['line_number']['BTC-7E-HP5'] = 22
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['line_number']['BTC-8E-HP5'] = 21
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['start_offset'] = {}
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['start_offset']['BTC-7A'] = 0x0113154
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['start_offset']['BTC-7E'] = 0x0113154
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['start_offset']['BTC-8E'] = 0x01133ac
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['start_offset']['BTC-7E-HP4'] = 0x010e1f4
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['start_offset']['BTC-8E-HP4'] = 0x010e6f4
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['start_offset']['BTC-7E-HP5'] = 0x00eaff4
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['start_offset']['BTC-8E-HP5'] = 0x00eb0b0
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['change_from_jump'] = 'jal.get_tod_in_timelapse_region'
timelapse_patch_list['tlps_update_timelapse_rise_set_times']['change_to_jump']   = 'jal.tlps_get_tod_in_timelapse_region'


## set_wakeup_alarms0
timelapse_patch_list['tlps_set_wakeup_alarms0'] = {}
timelapse_patch_list['tlps_set_wakeup_alarms0']['function'] = 'set_wakeup_alarms'
timelapse_patch_list['tlps_set_wakeup_alarms0']['line_number'] = {}
timelapse_patch_list['tlps_set_wakeup_alarms0']['line_number']['BTC-7A'] = 116 
timelapse_patch_list['tlps_set_wakeup_alarms0']['line_number']['BTC-7E'] = 116 
timelapse_patch_list['tlps_set_wakeup_alarms0']['line_number']['BTC-8E'] = 117
timelapse_patch_list['tlps_set_wakeup_alarms0']['line_number']['BTC-7E-HP4'] = 110
timelapse_patch_list['tlps_set_wakeup_alarms0']['line_number']['BTC-8E-HP4'] = 110
timelapse_patch_list['tlps_set_wakeup_alarms0']['line_number']['BTC-7E-HP5'] = 109
timelapse_patch_list['tlps_set_wakeup_alarms0']['line_number']['BTC-8E-HP5'] = 112 
timelapse_patch_list['tlps_set_wakeup_alarms0']['start_offset'] = {}
timelapse_patch_list['tlps_set_wakeup_alarms0']['start_offset']['BTC-7A'] = 0x0116da0
timelapse_patch_list['tlps_set_wakeup_alarms0']['start_offset']['BTC-7E'] = 0x0116da0
timelapse_patch_list['tlps_set_wakeup_alarms0']['start_offset']['BTC-8E'] = 0x0116ff8
timelapse_patch_list['tlps_set_wakeup_alarms0']['start_offset']['BTC-7E-HP4'] = 0x01125ac
timelapse_patch_list['tlps_set_wakeup_alarms0']['start_offset']['BTC-8E-HP4'] = 0x0112aa8
timelapse_patch_list['tlps_set_wakeup_alarms0']['start_offset']['BTC-7E-HP5'] = 0x00ef474
timelapse_patch_list['tlps_set_wakeup_alarms0']['start_offset']['BTC-8E-HP5'] = 0x00ef51c
timelapse_patch_list['tlps_set_wakeup_alarms0']['change_from_jump'] = 'jal.get_tod_in_timelapse_region'
timelapse_patch_list['tlps_set_wakeup_alarms0']['change_to_jump']   = 'jal.tlps_get_tod_in_timelapse_region'

## set_wakeup_alarms1
timelapse_patch_list['tlps_set_wakeup_alarms1'] = {}
timelapse_patch_list['tlps_set_wakeup_alarms1']['function'] = 'set_wakeup_alarms'
timelapse_patch_list['tlps_set_wakeup_alarms1']['line_number'] = {}
timelapse_patch_list['tlps_set_wakeup_alarms1']['line_number']['BTC-7A'] = 117
timelapse_patch_list['tlps_set_wakeup_alarms1']['line_number']['BTC-7E'] = 117
timelapse_patch_list['tlps_set_wakeup_alarms1']['line_number']['BTC-8E'] = 119
timelapse_patch_list['tlps_set_wakeup_alarms1']['line_number']['BTC-7E-HP4'] = 111
timelapse_patch_list['tlps_set_wakeup_alarms1']['line_number']['BTC-8E-HP4'] = 111
timelapse_patch_list['tlps_set_wakeup_alarms1']['line_number']['BTC-7E-HP5'] = 111
timelapse_patch_list['tlps_set_wakeup_alarms1']['line_number']['BTC-8E-HP5'] = 113 
timelapse_patch_list['tlps_set_wakeup_alarms1']['start_offset'] = {}
timelapse_patch_list['tlps_set_wakeup_alarms1']['start_offset']['BTC-7E'] = 0x0116db4
timelapse_patch_list['tlps_set_wakeup_alarms1']['start_offset']['BTC-8E'] = 0x011700c
timelapse_patch_list['tlps_set_wakeup_alarms1']['start_offset']['BTC-7E-HP4'] = 0x01125c0
timelapse_patch_list['tlps_set_wakeup_alarms1']['start_offset']['BTC-8E-HP4'] = 0x0112abc
timelapse_patch_list['tlps_set_wakeup_alarms1']['start_offset']['BTC-7E-HP5'] = 0x00ef488
timelapse_patch_list['tlps_set_wakeup_alarms1']['start_offset']['BTC-8E-HP5'] = 0x00ef530
timelapse_patch_list['tlps_set_wakeup_alarms1']['change_from_jump'] = 'jal.get_tod_in_timelapse_region'
timelapse_patch_list['tlps_set_wakeup_alarms1']['change_to_jump']   = 'jal.tlps_get_tod_in_timelapse_region'

## HceTaskBoot2Cap_Task0 is overwritten in elsewhere.

# TaskTimeLapseFSM_task4
# For HP5's only -- we've rewritten the function for Edges and HP4 cameras
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4'] = {}
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4']['function'] = 'TaskTimeLapseFSM_task4'
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4']['line_number'] = {}
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4']['line_number']['BTC-7E-HP5'] = 27
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4']['line_number']['BTC-8E-HP5'] = 26 
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4']['start_offset'] = {}
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4']['start_offset']['BTC-7E-HP5'] = 0x0109830
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4']['start_offset']['BTC-8E-HP5'] = 0x01098e0
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4']['change_from_jump'] = 'jal.get_tod_in_timelapse_region'
timelapse_patch_list['tlps_TaskTimeLapseFSM_task4']['change_to_jump']   = 'jal.tlps_get_tod_in_timelapse_region'

# HandleWaittimeLapseFSM_task0
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0'] = {}
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['function'] = 'HandleWaittimeLapseFSM_task0'
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['line_number'] = {}
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['line_number']['BTC-7A'] = 19
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['line_number']['BTC-7E'] = 19
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['line_number']['BTC-8E'] = 19
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['line_number']['BTC-7E-HP4'] = 19
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['line_number']['BTC-8E-HP4'] = 18
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['line_number']['BTC-7E-HP5'] = 19
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['line_number']['BTC-8E-HP5'] = 19 
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['start_offset'] = {}
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['start_offset']['BTC-7A'] = 0x0137d5c
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['start_offset']['BTC-7E'] = 0x0137d5c
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['start_offset']['BTC-8E'] = 0x0138958
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['start_offset']['BTC-7E-HP4'] = 0x013462c
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['start_offset']['BTC-8E-HP4'] = 0x013715c
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['start_offset']['BTC-7E-HP5'] = 0x01175d4
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['start_offset']['BTC-8E-HP5'] = 0x0117f2c
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['change_from_jump'] = 'jal.get_tod_in_timelapse_region'
timelapse_patch_list['tlps_HandleWaittimeLapseFSM_task0']['change_to_jump']   = 'jal.tlps_get_tod_in_timelapse_region'

# Debugging in update_timelapse_rise_set_times
#timelapse_patch_list['tlps_update_timelapse_rise_set_time_debug'] = {}
#timelapse_patch_list['tlps_update_timelapse_rise_set_time_debug']['function'] = 'update_timelapse_rise_set_times'
# timelapse_patch_list['tlps_update_timelapse_rise_set_time_debug']['line_number'] = {}
# timelapse_patch_list['tlps_update_timelapse_rise_set_time_debug']['line_number']['BTC-7A'] = 33
# timelapse_patch_list['tlps_update_timelapse_rise_set_time_debug']['start_offset'] = {}
# timelapse_patch_list['tlps_update_timelapse_rise_set_time_debug']['start_offset']['BTC-7A'] = 0x00111b8
# timelapse_patch_list['tlps_update_timelapse_rise_set_time_debug']['change_from_jump'] = 'jal.get_next_wake_time'
# timelapse_patch_list['tlps_update_timelapse_rise_set_time_debug']['change_to_jump']   = 'jal.tlps_get_next_wake_time'

# timelapse_patch_list['tlps_set_wakeup_alarms'] = {}
# timelapse_patch_list['tlps_set_wakeup_alarms']['function'] = 'set_wakeup_alarms'
# timelapse_patch_list['tlps_set_wakeup_alarms']['line_number'] = {}
# timelapse_patch_list['tlps_set_wakeup_alarms']['line_number']['BTC-7A'] = 85
# timelapse_patch_list['tlps_set_wakeup_alarms']['start_offset'] = {}
# timelapse_patch_list['tlps_set_wakeup_alarms']['start_offset']['BTC-7A'] = 0x000b520
# timelapse_patch_list['tlps_set_wakeup_alarms']['change_from_jump'] = 'jal.get_g_timelapse_wakeup_time'
# timelapse_patch_list['tlps_set_wakeup_alarms']['change_to_jump']   = 'jal.tlps_get_g_timelapse_wakeup_time'

# Debugging Missing Temperature
# in Unknown_Function()
# unknown line number
#timelapse_patch_list['tlps_temp_bug'] = {}
#timelapse_patch_list['tlps_temp_bug']['function'] = 'Unknown_Function'
#timelapse_patch_list['tlps_temp_bug']['line_number'] = {}
#timelapse_patch_list['tlps_temp_bug']['line_number']['BTC-8E'] = 0
#timelapse_patch_list['tlps_temp_bug']['start_offset'] = {}
#timelapse_patch_list['tlps_temp_bug']['start_offset']['BTC-8E'] = 0x010db18
#timelapse_patch_list['tlps_temp_bug']['change_from_jump'] = 'j.Pressure_sensor_getReading'
#timelapse_patch_list['tlps_temp_bug']['change_to_jump']   = 'j.tlps_Pressure_sensor_getReading'

##################################################################################
# Patches for Aperture selection/photo sensor threshold
##################################################################################

aperture_patch_list = {}

# Splice in a call to apt_HceIQ_CheckNightMode()

# in devInitPrimary()
# line 33
aperture_patch_list['apt_dev_init_primary'] = {}
aperture_patch_list['apt_dev_init_primary']['function'] = 'devInitPrimary'
aperture_patch_list['apt_dev_init_primary']['line_number'] = {}
aperture_patch_list['apt_dev_init_primary']['line_number']['BTC-7A'] = 33
aperture_patch_list['apt_dev_init_primary']['line_number']['BTC-7E'] = 33
aperture_patch_list['apt_dev_init_primary']['line_number']['BTC-8E'] = 33
aperture_patch_list['apt_dev_init_primary']['line_number']['BTC-7E-HP4'] = 43
aperture_patch_list['apt_dev_init_primary']['line_number']['BTC-8E-HP4'] = 43
aperture_patch_list['apt_dev_init_primary']['line_number']['BTC-7E-HP5'] = 40
aperture_patch_list['apt_dev_init_primary']['line_number']['BTC-8E-HP5'] = 40
aperture_patch_list['apt_dev_init_primary']['start_offset'] = {}
aperture_patch_list['apt_dev_init_primary']['start_offset']['BTC-7A']     = 0x000ed04
aperture_patch_list['apt_dev_init_primary']['start_offset']['BTC-7E']     = 0x000ed04
aperture_patch_list['apt_dev_init_primary']['start_offset']['BTC-8E']     = 0x000ed04
aperture_patch_list['apt_dev_init_primary']['start_offset']['BTC-7E-HP4'] = 0x000edbc
aperture_patch_list['apt_dev_init_primary']['start_offset']['BTC-8E-HP4'] = 0x000edbc
aperture_patch_list['apt_dev_init_primary']['start_offset']['BTC-7E-HP5'] =  0x000ed4c
aperture_patch_list['apt_dev_init_primary']['start_offset']['BTC-8E-HP5'] = 0x000ed4c
aperture_patch_list['apt_dev_init_primary']['change_from_jump'] = 'jal.HceIQ_CheckNightMode'
aperture_patch_list['apt_dev_init_primary']['change_to_jump']   = 'jal.apt_HceIQ_CheckNightMode'

## Patch to write the cold_item_aperature to NVM
aperture_patch_list['apt_hce_power_common_power_off'] = {}
aperture_patch_list['apt_hce_power_common_power_off']['function'] = 'HcePower_CommonPowerOff'
aperture_patch_list['apt_hce_power_common_power_off']['line_number'] = {}
aperture_patch_list['apt_hce_power_common_power_off']['line_number']['BTC-7A'] = 46
aperture_patch_list['apt_hce_power_common_power_off']['line_number']['BTC-7E'] = 46
aperture_patch_list['apt_hce_power_common_power_off']['line_number']['BTC-8E'] = 46
aperture_patch_list['apt_hce_power_common_power_off']['line_number']['BTC-7E-HP4'] = 62
aperture_patch_list['apt_hce_power_common_power_off']['line_number']['BTC-8E-HP4'] = 62
aperture_patch_list['apt_hce_power_common_power_off']['line_number']['BTC-7E-HP5'] = 80
aperture_patch_list['apt_hce_power_common_power_off']['line_number']['BTC-8E-HP5'] = 80
aperture_patch_list['apt_hce_power_common_power_off']['start_offset'] = {}
aperture_patch_list['apt_hce_power_common_power_off']['start_offset']['BTC-7A']     = 0x011344c
aperture_patch_list['apt_hce_power_common_power_off']['start_offset']['BTC-7E']     = 0x011344c
aperture_patch_list['apt_hce_power_common_power_off']['start_offset']['BTC-8E']     = 0x01136a4
aperture_patch_list['apt_hce_power_common_power_off']['start_offset']['BTC-7E-HP4'] = 0x010e550
aperture_patch_list['apt_hce_power_common_power_off']['start_offset']['BTC-8E-HP4'] = 0x010ea50
aperture_patch_list['apt_hce_power_common_power_off']['start_offset']['BTC-7E-HP5'] =  0x00eb8dc
aperture_patch_list['apt_hce_power_common_power_off']['start_offset']['BTC-8E-HP5'] = 0x00eb998
aperture_patch_list['apt_hce_power_common_power_off']['change_from_jump'] = 'jal.set_rtc_extra_operation_mode'
aperture_patch_list['apt_hce_power_common_power_off']['change_to_jump']   = 'jal.apt_set_rtc_extra_operation_mode'



## DEBUGGING aperture mode
# Debug
#aperture_patch_list['apt_spawn_ir_cut_fsm'] = {}
#aperture_patch_list['apt_spawn_ir_cut_fsm']['function'] = 'spawnIRCutFSM_per_mode'
#aperture_patch_list['apt_spawn_ir_cut_fsm']['line_number'] = {}
#aperture_patch_list['apt_spawn_ir_cut_fsm']['line_number']['BTC-7A'] = 32
#aperture_patch_list['apt_spawn_ir_cut_fsm']['start_offset'] = {}
#aperture_patch_list['apt_spawn_ir_cut_fsm']['start_offset']['BTC-7A']     = 0x000f6cc
#aperture_patch_list['apt_spawn_ir_cut_fsm']['change_from_jump'] = 'jal.IRCutThreadCreate'
#aperture_patch_list['apt_spawn_ir_cut_fsm']['change_to_jump']   = 'jal.apt_IRCutThreadCreate'

# Debug
#aperture_patch_list['apt_mode_auto2_task5'] = {}
#aperture_patch_list['apt_mode_auto2_task5']['function'] = 'ModeAuto2_FSM_Task5'
#aperture_patch_list['apt_mode_auto2_task5']['line_number'] = {}
#aperture_patch_list['apt_mode_auto2_task5']['line_number']['BTC-7A'] = 30
#aperture_patch_list['apt_mode_auto2_task5']['start_offset'] = {}
#aperture_patch_list['apt_mode_auto2_task5']['start_offset']['BTC-7A'] = 0x0012734
#aperture_patch_list['apt_mode_auto2_task5']['change_from_jump'] = 'jal.get_g_night_mode_p'
#aperture_patch_list['apt_mode_auto2_task5']['change_to_jump']   = 'jal.apt_get_g_night_mode_p'

# Debug
# aperture_patch_list['apt_hce_ir_cut_set'] = {}
# aperture_patch_list['apt_hce_ir_cut_set']['function'] = 'HceIRCut_SetIRCut'
# aperture_patch_list['apt_hce_ir_cut_set']['line_number'] = {}
# aperture_patch_list['apt_hce_ir_cut_set']['line_number']['BTC-7A'] = 25
# aperture_patch_list['apt_hce_ir_cut_set']['start_offset'] = {}
# aperture_patch_list['apt_hce_ir_cut_set']['start_offset']['BTC-7A'] = 0x00090ec
# aperture_patch_list['apt_hce_ir_cut_set']['change_from_jump'] = 'jal.log_printf'
# aperture_patch_list['apt_hce_ir_cut_set']['change_to_jump']   = 'jal.apt_ir_cut_log_printf'

# Debug
# aperture_patch_list['apt_boot2cap_nex_state'] = {}
# aperture_patch_list['apt_boot2cap_nex_state']['function'] = 'HceTaskBoot2Cap_fsm_iterator'
# aperture_patch_list['apt_boot2cap_nex_state']['line_number'] = {}
# aperture_patch_list['apt_boot2cap_nex_state']['line_number']['BTC-7A'] = 15
# aperture_patch_list['apt_boot2cap_nex_state']['start_offset'] = {}
# aperture_patch_list['apt_boot2cap_nex_state']['start_offset']['BTC-7A'] = 0x0020e90
# aperture_patch_list['apt_boot2cap_nex_state']['change_from_jump'] = 'jal.fsm_getCurrentState'
# aperture_patch_list['apt_boot2cap_nex_state']['change_to_jump']   = 'jal.apt_boot2cap_fsm_getCurrentState'

### END DEBUG

# in ModeAuto2_FSM_Task5_prep_for_capture()
# line 28
aperture_patch_list['apt_mode_auto2'] = {}
aperture_patch_list['apt_mode_auto2']['function'] = 'ModeAuto2_FSM_Task5_prep_for_capture'
aperture_patch_list['apt_mode_auto2']['line_number'] = {}
aperture_patch_list['apt_mode_auto2']['line_number']['BTC-7A'] = 28
aperture_patch_list['apt_mode_auto2']['line_number']['BTC-7E'] = 28
aperture_patch_list['apt_mode_auto2']['line_number']['BTC-8E'] = 28
aperture_patch_list['apt_mode_auto2']['line_number']['BTC-7E-HP4'] = 28
aperture_patch_list['apt_mode_auto2']['line_number']['BTC-8E-HP4'] = 28
aperture_patch_list['apt_mode_auto2']['line_number']['BTC-7E-HP5'] = 30
aperture_patch_list['apt_mode_auto2']['line_number']['BTC-8E-HP5'] = 28
aperture_patch_list['apt_mode_auto2']['start_offset'] = {}
aperture_patch_list['apt_mode_auto2']['start_offset']['BTC-7A'] = 0x012df0c
aperture_patch_list['apt_mode_auto2']['start_offset']['BTC-7E'] = 0x012df0c
aperture_patch_list['apt_mode_auto2']['start_offset']['BTC-8E'] = 0x012eae0
aperture_patch_list['apt_mode_auto2']['start_offset']['BTC-7E-HP4'] = 0x012a83c
aperture_patch_list['apt_mode_auto2']['start_offset']['BTC-8E-HP4'] = 0x012d364
aperture_patch_list['apt_mode_auto2']['start_offset']['BTC-7E-HP5'] = 0x010d648
aperture_patch_list['apt_mode_auto2']['start_offset']['BTC-8E-HP5'] = 0x010df98
aperture_patch_list['apt_mode_auto2']['change_from_jump'] = 'jal.HceIQ_CheckNightMode'
aperture_patch_list['apt_mode_auto2']['change_to_jump']   = 'jal.apt_HceIQ_CheckNightMode'

# in ModeAuto_DoCaptureEvent()
# line 34
aperture_patch_list['apt_mode_auto_do_capture'] = {}
aperture_patch_list['apt_mode_auto_do_capture']['function'] = 'ModeAuto_DoCaptureEvent'
aperture_patch_list['apt_mode_auto_do_capture']['line_number'] = {}
aperture_patch_list['apt_mode_auto_do_capture']['line_number']['BTC-7A'] = 34
aperture_patch_list['apt_mode_auto_do_capture']['line_number']['BTC-7E'] = 34
aperture_patch_list['apt_mode_auto_do_capture']['line_number']['BTC-8E'] = 34
aperture_patch_list['apt_mode_auto_do_capture']['line_number']['BTC-7E-HP4'] = 34
aperture_patch_list['apt_mode_auto_do_capture']['line_number']['BTC-8E-HP4'] = 34
aperture_patch_list['apt_mode_auto_do_capture']['line_number']['BTC-7E-HP5'] = 34
aperture_patch_list['apt_mode_auto_do_capture']['line_number']['BTC-8E-HP5'] = 34
aperture_patch_list['apt_mode_auto_do_capture']['start_offset'] = {}
aperture_patch_list['apt_mode_auto_do_capture']['start_offset']['BTC-7A'] = 0x012e228
aperture_patch_list['apt_mode_auto_do_capture']['start_offset']['BTC-7E'] = 0x012e228
aperture_patch_list['apt_mode_auto_do_capture']['start_offset']['BTC-8E'] = 0x012edfc
aperture_patch_list['apt_mode_auto_do_capture']['start_offset']['BTC-7E-HP4'] = 0x012ab60
aperture_patch_list['apt_mode_auto_do_capture']['start_offset']['BTC-8E-HP4'] = 0x012d688
aperture_patch_list['apt_mode_auto_do_capture']['start_offset']['BTC-7E-HP5'] = 0x010d9c0
aperture_patch_list['apt_mode_auto_do_capture']['start_offset']['BTC-8E-HP5'] = 0x010e310
aperture_patch_list['apt_mode_auto_do_capture']['change_from_jump'] = 'jal.HceIQ_CheckNightMode'
aperture_patch_list['apt_mode_auto_do_capture']['change_to_jump']   = 'jal.apt_HceIQ_CheckNightMode'


# in HcePower_CommonPowerOff
# For BTC-7E/8E/7E-HP4/8E-HP4: Change call to set_rtc_extra_operation_mode() to allow for more space 
#
aperture_patch_list['apt_set_operation_mode'] = {}
aperture_patch_list['apt_set_operation_mode']['function'] = 'HcePower_CommonPowerOff'
aperture_patch_list['apt_set_operation_mode']['line_number'] = {}
aperture_patch_list['apt_set_operation_mode']['line_number']['BTC-7A'] = 46
aperture_patch_list['apt_set_operation_mode']['line_number']['BTC-7E'] = 46
aperture_patch_list['apt_set_operation_mode']['line_number']['BTC-8E'] = 46
aperture_patch_list['apt_set_operation_mode']['line_number']['BTC-7E-HP4'] = 63
aperture_patch_list['apt_set_operation_mode']['line_number']['BTC-8E-HP4'] = 62
aperture_patch_list['apt_set_operation_mode']['start_offset'] = {}
aperture_patch_list['apt_set_operation_mode']['start_offset']['BTC-7A'] = 0x011344c
aperture_patch_list['apt_set_operation_mode']['start_offset']['BTC-7E'] = 0x011344c
aperture_patch_list['apt_set_operation_mode']['start_offset']['BTC-8E'] = 0x01136a4
aperture_patch_list['apt_set_operation_mode']['start_offset']['BTC-7E-HP4'] = 0x010e550
aperture_patch_list['apt_set_operation_mode']['start_offset']['BTC-8E-HP4'] = 0x010ea50
aperture_patch_list['apt_set_operation_mode']['change_from_jump'] = 'jal.set_rtc_extra_operation_mode'
aperture_patch_list['apt_set_operation_mode']['change_to_jump']   = 'jal.apt_set_rtc_extra_operation_mode'


# in HceFastCap_PreDo
# For BTC-7E/8E/7E-HP4/8E-HP4: Change call to set_rtc_extra_operation_mode() to allow for more space 
#
aperture_patch_list['apt_get_operation_mode'] = {}
aperture_patch_list['apt_get_operation_mode']['function'] = 'HceFastCap_PreDo'
aperture_patch_list['apt_get_operation_mode']['line_number'] = {}
aperture_patch_list['apt_get_operation_mode']['line_number']['BTC-7A'] = 48
aperture_patch_list['apt_get_operation_mode']['line_number']['BTC-7E'] = 48
aperture_patch_list['apt_get_operation_mode']['line_number']['BTC-8E'] = 50
aperture_patch_list['apt_get_operation_mode']['line_number']['BTC-7E-HP4'] = 50
aperture_patch_list['apt_get_operation_mode']['line_number']['BTC-8E-HP4'] = 50
aperture_patch_list['apt_get_operation_mode']['start_offset'] = {}
aperture_patch_list['apt_get_operation_mode']['start_offset']['BTC-7A'] = 0x007409c
aperture_patch_list['apt_get_operation_mode']['start_offset']['BTC-7E'] = 0x007409c
aperture_patch_list['apt_get_operation_mode']['start_offset']['BTC-8E'] = 0x007409c
aperture_patch_list['apt_get_operation_mode']['start_offset']['BTC-7E-HP4'] = 0x0069f70
aperture_patch_list['apt_get_operation_mode']['start_offset']['BTC-8E-HP4'] = 0x0069e80
aperture_patch_list['apt_get_operation_mode']['change_from_jump'] = 'jal.get_rtc_extra_operation_mode'
aperture_patch_list['apt_get_operation_mode']['change_to_jump']   = 'jal.apt_get_rtc_extra_operation_mode'

##################################################################################
# Patches for creating new menu(s)
#    - menu_handler_function_array
#    - menu_item_array
menus_define_num_btc_setup_functions = {}
menus_define_num_btc_setup_functions['BTC-7A'] = 25
menus_define_num_btc_setup_functions['BTC-7E'] = 25
menus_define_num_btc_setup_functions['BTC-8E'] = 25
menus_define_num_btc_setup_functions['BTC-7E-HP4'] = 25
menus_define_num_btc_setup_functions['BTC-8E-HP4'] = 25
menus_define_num_btc_setup_functions['BTC-7E-HP5'] = 26
menus_define_num_btc_setup_functions['BTC-8E-HP5'] = 26
menus_define_num_wbwl_setup_functions = {}
if evsd_active:
    menus_define_num_wbwl_setup_functions['BTC-7A'] = 6
    menus_define_num_wbwl_setup_functions['BTC-7E'] = 6
    menus_define_num_wbwl_setup_functions['BTC-8E'] = 6
    menus_define_num_wbwl_setup_functions['BTC-7E-HP4'] = 6
    menus_define_num_wbwl_setup_functions['BTC-8E-HP4'] = 6
    menus_define_num_wbwl_setup_functions['BTC-7E-HP5'] = 6
    menus_define_num_wbwl_setup_functions['BTC-8E-HP5'] = 6
else:
    menus_define_num_wbwl_setup_functions['BTC-7A'] = 5
    menus_define_num_wbwl_setup_functions['BTC-7E'] = 5
    menus_define_num_wbwl_setup_functions['BTC-8E'] = 5
    menus_define_num_wbwl_setup_functions['BTC-7E-HP4'] = 5
    menus_define_num_wbwl_setup_functions['BTC-8E-HP4'] = 5
    menus_define_num_wbwl_setup_functions['BTC-7E-HP5'] = 5
    menus_define_num_wbwl_setup_functions['BTC-8E-HP5'] = 5


## Since the advantage, there's a hidden menu item (for capture timer)
#       that we need to special case
menus_define_hidden_menus = {}
menus_define_hidden_menus['BTC-7A'] = 1
menus_define_hidden_menus['BTC-7E'] = 1
menus_define_hidden_menus['BTC-8E'] = 1
menus_define_hidden_menus['BTC-7E-HP4'] = 1
menus_define_hidden_menus['BTC-8E-HP4'] = 1
menus_define_hidden_menus['BTC-7E-HP5'] = 1
menus_define_hidden_menus['BTC-8E-HP5'] = 1


menus_define_setup_function_padding = {}
menus_define_setup_function_padding['BTC-7A'] = 5
menus_define_setup_function_padding['BTC-7E'] = 5
menus_define_setup_function_padding['BTC-8E'] = 5
menus_define_setup_function_padding['BTC-7E-HP4'] = 5
menus_define_setup_function_padding['BTC-8E-HP4'] = 5
menus_define_setup_function_padding['BTC-7E-HP5'] = 5
menus_define_setup_function_padding['BTC-8E-HP5'] = 5

menus_define_expected_setup_menu_items = {}
menus_define_new_setup_menu_items = {}
menus_define_expected_end_state = {}
menus_define_new_end_state = {}
menus_define_expected_function_array_size = {}
menus_define_new_function_array_size = {}

for target in menus_define_num_btc_setup_functions:
    menus_define_expected_setup_menu_items[target] = menus_define_num_btc_setup_functions[target] 
    menus_define_new_setup_menu_items[target] = menus_define_num_btc_setup_functions[target] + menus_define_num_wbwl_setup_functions[target] 
    menus_define_expected_end_state[target] = menus_define_num_btc_setup_functions[target] + menus_define_setup_function_padding[target] + menus_define_hidden_menus[target] - 1
    menus_define_new_end_state[target] = menus_define_num_btc_setup_functions[target] + menus_define_num_wbwl_setup_functions[target] + menus_define_setup_function_padding[target] + menus_define_hidden_menus[target] - 1
    menus_define_expected_function_array_size[target] = menus_define_num_btc_setup_functions[target] + menus_define_setup_function_padding[target] +  menus_define_hidden_menus[target]
    menus_define_new_function_array_size[target] = menus_define_num_btc_setup_functions[target] + menus_define_num_wbwl_setup_functions[target] + menus_define_setup_function_padding[target] + menus_define_hidden_menus[target]




menus_patch_list = {}

# Splice in call to our new lookup table
#    - correct check on array size
#    - change argument from pointer to an index
#    - splice in call to our execute function
# in HceTaskMenuMultiItem_fsm_iterator()
# line 23
menus_patch_list['menu_function_count'] = {}
menus_patch_list['menu_function_count']['function'] = 'HceTaskMenuMultiItem_fsm_iterator'
menus_patch_list['menu_function_count']['line_number'] = {}
menus_patch_list['menu_function_count']['line_number']['BTC-7A'] = 23
menus_patch_list['menu_function_count']['line_number']['BTC-7E'] = 23
menus_patch_list['menu_function_count']['line_number']['BTC-8E'] = 23
menus_patch_list['menu_function_count']['line_number']['BTC-7E-HP4'] = 23
menus_patch_list['menu_function_count']['line_number']['BTC-8E-HP4'] = 23
menus_patch_list['menu_function_count']['line_number']['BTC-7E-HP5'] = 23
menus_patch_list['menu_function_count']['line_number']['BTC-8E-HP5'] = 23
menus_patch_list['menu_function_count']['start_offset'] = {}
menus_patch_list['menu_function_count']['start_offset']['BTC-7A'] = 0x0131c54
menus_patch_list['menu_function_count']['start_offset']['BTC-7E'] = 0x0131c54
menus_patch_list['menu_function_count']['start_offset']['BTC-8E'] = 0x0132850
menus_patch_list['menu_function_count']['start_offset']['BTC-7E-HP4'] = 0x012e518
menus_patch_list['menu_function_count']['start_offset']['BTC-8E-HP4'] = 0x0131048
menus_patch_list['menu_function_count']['start_offset']['BTC-7E-HP5'] =  0x01112a0
menus_patch_list['menu_function_count']['start_offset']['BTC-8E-HP5'] = 0x0111bf8
menus_patch_list['menu_function_count']['change_from_bytes'] = {}
menus_patch_list['menu_function_count']['change_from_bytes']['BTC-7A'] = bytes([menus_define_expected_function_array_size['BTC-7A'], 0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_from_bytes']['BTC-7E'] = bytes([menus_define_expected_function_array_size['BTC-7E'], 0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_from_bytes']['BTC-8E'] = bytes([menus_define_expected_function_array_size['BTC-8E'], 0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_function_array_size['BTC-7E-HP4'], 0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_function_array_size['BTC-8E-HP4'], 0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_function_array_size['BTC-7E-HP5'], 0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_function_array_size['BTC-8E-HP5'], 0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_to_bytes']   = {}
menus_patch_list['menu_function_count']['change_to_bytes']['BTC-7A']     = bytes([menus_define_new_function_array_size['BTC-7A'],      0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_to_bytes']['BTC-7E']     = bytes([menus_define_new_function_array_size['BTC-7E'],      0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_to_bytes']['BTC-8E']     = bytes([menus_define_new_function_array_size['BTC-8E'],      0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_to_bytes']['BTC-7E-HP4'] = bytes([menus_define_new_function_array_size['BTC-7E-HP4'],      0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_to_bytes']['BTC-8E-HP4'] = bytes([menus_define_new_function_array_size['BTC-8E-HP4'],      0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_to_bytes']['BTC-7E-HP5'] = bytes([menus_define_new_function_array_size['BTC-7E-HP5'],      0x00, 0x42, 0x2c])
menus_patch_list['menu_function_count']['change_to_bytes']['BTC-8E-HP5'] = bytes([menus_define_new_function_array_size['BTC-8E-HP5'],      0x00, 0x42, 0x2c])
# replace lw a0,0x0(v0)=> ->handleInit_menu  // g_menu_handler_function_array[index]
# with    lw a0,v0                           // index
# in HceTaskMenuMultiItem_fsm_iterator()
# Line 28
menus_patch_list['index_argument'] = {}
menus_patch_list['index_argument']['function'] = 'HceTaskMenuMultiItem_fsm_iterator'
menus_patch_list['index_argument']['line_number'] = {}
menus_patch_list['index_argument']['line_number']['BTC-7A'] = 28
menus_patch_list['index_argument']['line_number']['BTC-7E'] = 28
menus_patch_list['index_argument']['line_number']['BTC-8E'] = 28
menus_patch_list['index_argument']['line_number']['BTC-7E-HP4'] = 28
menus_patch_list['index_argument']['line_number']['BTC-8E-HP4'] = 28
menus_patch_list['index_argument']['line_number']['BTC-7E-HP5'] = 28
menus_patch_list['index_argument']['line_number']['BTC-8E-HP5'] = 28
menus_patch_list['index_argument']['start_offset'] = {}
menus_patch_list['index_argument']['start_offset']['BTC-7A'] = 0x0131c68
menus_patch_list['index_argument']['start_offset']['BTC-7E'] = 0x0131c68
menus_patch_list['index_argument']['start_offset']['BTC-8E'] = 0x0132864
menus_patch_list['index_argument']['start_offset']['BTC-7E-HP4'] = 0x012e52c
menus_patch_list['index_argument']['start_offset']['BTC-8E-HP4'] = 0x013105c
menus_patch_list['index_argument']['start_offset']['BTC-7E-HP5'] = 0x01112b4
menus_patch_list['index_argument']['start_offset']['BTC-8E-HP5'] = 0x0111c0c
menus_patch_list['index_argument']['change_from_bytes'] = bytes([0x00, 0x00, 0x44, 0x8c])
menus_patch_list['index_argument']['change_to_bytes']   = bytes([0x00, 0x20, 0x40, 0x80])
# replace call to execute_if_not_null
# in HceTaskMenuMultiItem_fsm_iterator()
# Line 28
menus_patch_list['execute_func'] = {}
menus_patch_list['execute_func']['function'] = 'HceTaskMenuMultiItem_fsm_iterator'
menus_patch_list['execute_func']['line_number'] = {}
menus_patch_list['execute_func']['line_number']['BTC-7A'] = 28
menus_patch_list['execute_func']['line_number']['BTC-7E'] = 28
menus_patch_list['execute_func']['line_number']['BTC-8E'] = 28
menus_patch_list['execute_func']['line_number']['BTC-7E-HP4'] = 28
menus_patch_list['execute_func']['line_number']['BTC-8E-HP4'] = 28
menus_patch_list['execute_func']['line_number']['BTC-7E-HP5'] = 28
menus_patch_list['execute_func']['line_number']['BTC-8E-HP5'] = 28
menus_patch_list['execute_func']['start_offset'] = {}
menus_patch_list['execute_func']['start_offset']['BTC-7A'] = 0x0131c6c
menus_patch_list['execute_func']['start_offset']['BTC-7E'] = 0x0131c6c
menus_patch_list['execute_func']['start_offset']['BTC-8E'] = 0x0132868
menus_patch_list['execute_func']['start_offset']['BTC-7E-HP4'] = 0x012e530
menus_patch_list['execute_func']['start_offset']['BTC-8E-HP4'] = 0x0131060
menus_patch_list['execute_func']['start_offset']['BTC-7E-HP5'] = 0x01112b8
menus_patch_list['execute_func']['start_offset']['BTC-8E-HP5'] = 0x0111c10
menus_patch_list['execute_func']['change_from_jump'] = 'jal.execute_if_not_null'
menus_patch_list['execute_func']['change_to_jump'] = 'jal.menus_execute_if_not_null'

#    replace first entry @ 0x802c9e68 g_camera_setup_menu_item_array
#			     w/         g_wbwl_camera_setup_menu_item_array
# in g_main_menu_selector_array[]
# unknown line number
menus_patch_list['setup_items_pointer'] = {}
menus_patch_list['setup_items_pointer']['function'] = 'g_main_menu_selector_array'
menus_patch_list['setup_items_pointer']['line_number'] = {}
menus_patch_list['setup_items_pointer']['line_number']['BTC-7A'] = 0
menus_patch_list['setup_items_pointer']['line_number']['BTC-7E'] = 0
menus_patch_list['setup_items_pointer']['line_number']['BTC-8E'] = 0
menus_patch_list['setup_items_pointer']['line_number']['BTC-7E-HP4'] = 0
menus_patch_list['setup_items_pointer']['line_number']['BTC-8E-HP4'] = 0
menus_patch_list['setup_items_pointer']['line_number']['BTC-7E-HP5'] = 0
menus_patch_list['setup_items_pointer']['line_number']['BTC-8E-HP5'] = 0
menus_patch_list['setup_items_pointer']['start_offset'] = {}
menus_patch_list['setup_items_pointer']['start_offset']['BTC-7A'] = 0x035564c
menus_patch_list['setup_items_pointer']['start_offset']['BTC-7E'] = 0x035564c
menus_patch_list['setup_items_pointer']['start_offset']['BTC-8E'] = 0x03556a4
menus_patch_list['setup_items_pointer']['start_offset']['BTC-7E-HP4'] = 0x03586a4
menus_patch_list['setup_items_pointer']['start_offset']['BTC-8E-HP4'] = 0x035c8d4
menus_patch_list['setup_items_pointer']['start_offset']['BTC-7E-HP5'] = 0x02ce120
menus_patch_list['setup_items_pointer']['start_offset']['BTC-8E-HP5'] = 0x02d02e0
menus_patch_list['setup_items_pointer']['change_from_ptr'] = 'g_camera_setup_menu_item_array'
menus_patch_list['setup_items_pointer']['change_to_ptr'] = 'g_wbwl_camera_setup_menu_item_array'

#    replace second @ 0x802c9e6c  which is  0x19 (25)
#                                w/         0x1d (29) 
# in g_main_menu_selector_array[]
# unknown line number
menus_patch_list['setup_items_number'] = {}
menus_patch_list['setup_items_number']['function'] = 'g_main_menu_selector_array'
menus_patch_list['setup_items_number']['line_number'] = {}
menus_patch_list['setup_items_number']['line_number']['BTC-7A'] = 0
menus_patch_list['setup_items_number']['line_number']['BTC-7E'] = 0
menus_patch_list['setup_items_number']['line_number']['BTC-8E'] = 0
menus_patch_list['setup_items_number']['line_number']['BTC-7E-HP4'] = 0
menus_patch_list['setup_items_number']['line_number']['BTC-8E-HP4'] = 0
menus_patch_list['setup_items_number']['line_number']['BTC-7E-HP5'] = 0
menus_patch_list['setup_items_number']['line_number']['BTC-8E-HP5'] = 0
menus_patch_list['setup_items_number']['start_offset'] = {}
menus_patch_list['setup_items_number']['start_offset']['BTC-7A'] = 0x0355650
menus_patch_list['setup_items_number']['start_offset']['BTC-7E'] = 0x0355650
menus_patch_list['setup_items_number']['start_offset']['BTC-8E'] = 0x03556a8
menus_patch_list['setup_items_number']['start_offset']['BTC-7E-HP4'] = 0x03586a8
menus_patch_list['setup_items_number']['start_offset']['BTC-8E-HP4'] = 0x035c8d8
menus_patch_list['setup_items_number']['start_offset']['BTC-7E-HP5'] = 0x02ce124
menus_patch_list['setup_items_number']['start_offset']['BTC-8E-HP5'] = 0x02d02e4
menus_patch_list['setup_items_number']['change_from_bytes'] = {}
menus_patch_list['setup_items_number']['change_from_bytes']['BTC-7A'] = bytes([menus_define_expected_setup_menu_items['BTC-7A'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_from_bytes']['BTC-7E'] = bytes([menus_define_expected_setup_menu_items['BTC-7E'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_from_bytes']['BTC-8E'] = bytes([menus_define_expected_setup_menu_items['BTC-8E'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_setup_menu_items['BTC-7E-HP4'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_setup_menu_items['BTC-8E-HP4'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_setup_menu_items['BTC-7E-HP5'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_setup_menu_items['BTC-8E-HP5'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_to_bytes'] = {}
menus_patch_list['setup_items_number']['change_to_bytes']['BTC-7A'] = bytes([menus_define_new_setup_menu_items['BTC-7A'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_to_bytes']['BTC-7E'] = bytes([menus_define_new_setup_menu_items['BTC-7E'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_to_bytes']['BTC-8E'] = bytes([menus_define_new_setup_menu_items['BTC-8E'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_to_bytes']['BTC-7E-HP4'] = bytes([menus_define_new_setup_menu_items['BTC-7E-HP4'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_to_bytes']['BTC-8E-HP4'] = bytes([menus_define_new_setup_menu_items['BTC-8E-HP4'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_to_bytes']['BTC-7E-HP5'] = bytes([menus_define_new_setup_menu_items['BTC-7E-HP5'], 0x00, 0x00, 0x00])
menus_patch_list['setup_items_number']['change_to_bytes']['BTC-8E-HP5'] = bytes([menus_define_new_setup_menu_items['BTC-8E-HP5'], 0x00, 0x00, 0x00])

# Hijack call so that we can point to the larger array
# in handleCameraSetup_menu()
# line 35 - 37
menus_patch_list['handleCameraSetup'] = {}
menus_patch_list['handleCameraSetup']['function'] = 'handleCameraSetup_menu'
menus_patch_list['handleCameraSetup']['line_number'] = {}
menus_patch_list['handleCameraSetup']['line_number']['BTC-7A'] = 35
menus_patch_list['handleCameraSetup']['line_number']['BTC-7E'] = 35
menus_patch_list['handleCameraSetup']['line_number']['BTC-8E'] = 35
menus_patch_list['handleCameraSetup']['line_number']['BTC-7E-HP4'] = 33
menus_patch_list['handleCameraSetup']['line_number']['BTC-8E-HP4'] = 33
menus_patch_list['handleCameraSetup']['line_number']['BTC-7E-HP5'] = 34
menus_patch_list['handleCameraSetup']['line_number']['BTC-8E-HP5'] = 35
menus_patch_list['handleCameraSetup']['start_offset'] = {}
menus_patch_list['handleCameraSetup']['start_offset']['BTC-7A'] = 0x013211c
menus_patch_list['handleCameraSetup']['start_offset']['BTC-7E'] = 0x013211c
menus_patch_list['handleCameraSetup']['start_offset']['BTC-8E'] = 0x0132d18
menus_patch_list['handleCameraSetup']['start_offset']['BTC-7E-HP4'] = 0x012e9e0
menus_patch_list['handleCameraSetup']['start_offset']['BTC-8E-HP4'] = 0x0131510
menus_patch_list['handleCameraSetup']['start_offset']['BTC-7E-HP5'] = 0x0111768
menus_patch_list['handleCameraSetup']['start_offset']['BTC-8E-HP5'] = 0x01120c0
menus_patch_list['handleCameraSetup']['change_from_jump'] = 'jal.get_next_state_from_menu_enter'
menus_patch_list['handleCameraSetup']['change_to_jump'] = 'jal.wbwl_get_next_state_from_menu_enter'

#### a whole bunch of hacks to point to a new "end state" in the g_wbwl_HceTaskMenuMultiItem_fsm_function_array
# in handleMainMenu_menu()
# 51
menus_patch_list['handle_main_menu'] = {}
menus_patch_list['handle_main_menu']['function'] = 'handleMainMenu_menu'
menus_patch_list['handle_main_menu']['line_number'] = {}
menus_patch_list['handle_main_menu']['line_number']['BTC-7A'] = 53
menus_patch_list['handle_main_menu']['line_number']['BTC-7E'] = 53
menus_patch_list['handle_main_menu']['line_number']['BTC-8E'] = 51
menus_patch_list['handle_main_menu']['line_number']['BTC-7E-HP4'] = 49
menus_patch_list['handle_main_menu']['line_number']['BTC-8E-HP4'] = 51
menus_patch_list['handle_main_menu']['line_number']['BTC-7E-HP5'] = 51
menus_patch_list['handle_main_menu']['line_number']['BTC-8E-HP5'] = 51
menus_patch_list['handle_main_menu']['start_offset'] = {}
menus_patch_list['handle_main_menu']['start_offset']['BTC-7A'] = 0x01322f8
menus_patch_list['handle_main_menu']['start_offset']['BTC-7E'] = 0x01322f8
menus_patch_list['handle_main_menu']['start_offset']['BTC-8E'] = 0x0132ef4
menus_patch_list['handle_main_menu']['start_offset']['BTC-7E-HP4'] = 0x012ebbc
menus_patch_list['handle_main_menu']['start_offset']['BTC-8E-HP4'] = 0x01316ec
menus_patch_list['handle_main_menu']['start_offset']['BTC-7E-HP5'] = 0x0111944
menus_patch_list['handle_main_menu']['start_offset']['BTC-8E-HP5'] = 0x011229c
menus_patch_list['handle_main_menu']['change_from_bytes'] = {}
menus_patch_list['handle_main_menu']['change_from_bytes']['BTC-7A'] = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_from_bytes']['BTC-7E'] = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_from_bytes']['BTC-8E'] = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_to_bytes']   = {}
menus_patch_list['handle_main_menu']['change_to_bytes']['BTC-7A']     = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_to_bytes']['BTC-7E']     = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_to_bytes']['BTC-8E']     = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_to_bytes']['BTC-7E-HP4'] = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_to_bytes']['BTC-8E-HP4'] = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_to_bytes']['BTC-7E-HP5'] = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_main_menu']['change_to_bytes']['BTC-8E-HP5'] = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleCameraSetup_menu(void)
# 51
menus_patch_list['handle_camera_setup_menu'] = {}
menus_patch_list['handle_camera_setup_menu']['function'] = 'handleCameraSetup_menu'
menus_patch_list['handle_camera_setup_menu']['line_number'] = {}
menus_patch_list['handle_camera_setup_menu']['line_number']['BTC-7A'] = 52
menus_patch_list['handle_camera_setup_menu']['line_number']['BTC-7E'] = 52
menus_patch_list['handle_camera_setup_menu']['line_number']['BTC-8E'] = 51
menus_patch_list['handle_camera_setup_menu']['line_number']['BTC-7E-HP4'] = 49
menus_patch_list['handle_camera_setup_menu']['line_number']['BTC-8E-HP4'] = 49
menus_patch_list['handle_camera_setup_menu']['line_number']['BTC-7E-HP5'] = 51
menus_patch_list['handle_camera_setup_menu']['line_number']['BTC-8E-HP5'] = 51
menus_patch_list['handle_camera_setup_menu']['start_offset'] = {}
menus_patch_list['handle_camera_setup_menu']['start_offset']['BTC-7A'] = 0x0132168
menus_patch_list['handle_camera_setup_menu']['start_offset']['BTC-7E'] = 0x0132168
menus_patch_list['handle_camera_setup_menu']['start_offset']['BTC-8E'] = 0x0132d64
menus_patch_list['handle_camera_setup_menu']['start_offset']['BTC-7E-HP4'] = 0x012ea2c
menus_patch_list['handle_camera_setup_menu']['start_offset']['BTC-8E-HP4'] = 0x013155c
menus_patch_list['handle_camera_setup_menu']['start_offset']['BTC-7E-HP5'] = 0x01117b4
menus_patch_list['handle_camera_setup_menu']['start_offset']['BTC-8E-HP5'] = 0x011210c
menus_patch_list['handle_camera_setup_menu']['change_from_bytes'] = {}
menus_patch_list['handle_camera_setup_menu']['change_from_bytes']['BTC-7A'] = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_from_bytes']['BTC-7E'] = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_from_bytes']['BTC-8E'] = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']   = {}
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_camera_setup_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handlePlayback_menu(void)
# 21
menus_patch_list['handle_playback_menu'] = {}
menus_patch_list['handle_playback_menu']['function'] = 'handlePlayback_menu'
menus_patch_list['handle_playback_menu']['line_number'] = {}
menus_patch_list['handle_playback_menu']['line_number']['BTC-7A'] = 21
menus_patch_list['handle_playback_menu']['line_number']['BTC-7E'] = 21
menus_patch_list['handle_playback_menu']['line_number']['BTC-8E'] = 21
menus_patch_list['handle_playback_menu']['line_number']['BTC-7E-HP4'] = 20
menus_patch_list['handle_playback_menu']['line_number']['BTC-8E-HP4'] = 20
menus_patch_list['handle_playback_menu']['line_number']['BTC-7E-HP5'] = 20
menus_patch_list['handle_playback_menu']['line_number']['BTC-8E-HP5'] = 20
menus_patch_list['handle_playback_menu']['start_offset'] = {}
menus_patch_list['handle_playback_menu']['start_offset']['BTC-7A'] = 0x0134d10
menus_patch_list['handle_playback_menu']['start_offset']['BTC-7E'] = 0x0134d10
menus_patch_list['handle_playback_menu']['start_offset']['BTC-8E'] = 0x013590c
menus_patch_list['handle_playback_menu']['start_offset']['BTC-7E-HP4'] = 0x01315c0
menus_patch_list['handle_playback_menu']['start_offset']['BTC-8E-HP4'] = 0x01340f0
menus_patch_list['handle_playback_menu']['start_offset']['BTC-7E-HP5'] = 0x0114600
menus_patch_list['handle_playback_menu']['start_offset']['BTC-8E-HP5'] = 0x0114f58
menus_patch_list['handle_playback_menu']['change_from_bytes'] = {}
menus_patch_list['handle_playback_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_to_bytes']   = {}
menus_patch_list['handle_playback_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_playback_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleSetTimeMenu(void)
# 90
menus_patch_list['handle_set_time_menu'] = {}
menus_patch_list['handle_set_time_menu']['function'] = 'handleSetTimeMenu'
menus_patch_list['handle_set_time_menu']['line_number'] = {}
menus_patch_list['handle_set_time_menu']['line_number']['BTC-7A'] = 92
menus_patch_list['handle_set_time_menu']['line_number']['BTC-7E'] = 92
menus_patch_list['handle_set_time_menu']['line_number']['BTC-8E'] = 90
menus_patch_list['handle_set_time_menu']['line_number']['BTC-7E-HP4'] = 92
menus_patch_list['handle_set_time_menu']['line_number']['BTC-8E-HP4'] = 92
menus_patch_list['handle_set_time_menu']['line_number']['BTC-7E-HP5'] = 94
menus_patch_list['handle_set_time_menu']['line_number']['BTC-8E-HP5'] = 92
menus_patch_list['handle_set_time_menu']['start_offset'] = {}
menus_patch_list['handle_set_time_menu']['start_offset']['BTC-7A']     = 0x013644c
menus_patch_list['handle_set_time_menu']['start_offset']['BTC-7E']     = 0x013644c
menus_patch_list['handle_set_time_menu']['start_offset']['BTC-8E']     = 0x0137048
menus_patch_list['handle_set_time_menu']['start_offset']['BTC-7E-HP4'] = 0x0132d1c
menus_patch_list['handle_set_time_menu']['start_offset']['BTC-8E-HP4'] = 0x013584c
menus_patch_list['handle_set_time_menu']['start_offset']['BTC-7E-HP5'] = 0x0115d6c
menus_patch_list['handle_set_time_menu']['start_offset']['BTC-8E-HP5'] = 0x01166c4
menus_patch_list['handle_set_time_menu']['change_from_bytes'] = {}
menus_patch_list['handle_set_time_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_to_bytes']   = {}
menus_patch_list['handle_set_time_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['handle_set_time_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleOperationMode_menu()
# 55
menus_patch_list['operation_mode_menu'] = {}
menus_patch_list['operation_mode_menu']['function'] = 'handleOperationMode_menu'
menus_patch_list['operation_mode_menu']['line_number'] = {}
menus_patch_list['operation_mode_menu']['line_number']['BTC-7A'] = 55
menus_patch_list['operation_mode_menu']['line_number']['BTC-7E'] = 55
menus_patch_list['operation_mode_menu']['line_number']['BTC-8E'] = 55
menus_patch_list['operation_mode_menu']['line_number']['BTC-7E-HP4'] = 55
menus_patch_list['operation_mode_menu']['line_number']['BTC-8E-HP4'] = 55
menus_patch_list['operation_mode_menu']['line_number']['BTC-7E-HP5'] = 56
menus_patch_list['operation_mode_menu']['line_number']['BTC-8E-HP5'] = 57
menus_patch_list['operation_mode_menu']['start_offset'] = {}
menus_patch_list['operation_mode_menu']['start_offset']['BTC-7A']     = 0x0134c24
menus_patch_list['operation_mode_menu']['start_offset']['BTC-7E']     = 0x0134c24
menus_patch_list['operation_mode_menu']['start_offset']['BTC-8E']     = 0x0135820
menus_patch_list['operation_mode_menu']['start_offset']['BTC-7E-HP4'] = 0x01314d4
menus_patch_list['operation_mode_menu']['start_offset']['BTC-8E-HP4'] = 0x0134004
menus_patch_list['operation_mode_menu']['start_offset']['BTC-7E-HP5'] = 0x0114514
menus_patch_list['operation_mode_menu']['start_offset']['BTC-8E-HP5'] = 0x0114e6c
menus_patch_list['operation_mode_menu']['change_from_bytes'] = {}
menus_patch_list['operation_mode_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_to_bytes']   = {}
menus_patch_list['operation_mode_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['operation_mode_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handlePhotoQuality_menu()
# 56
menus_patch_list['photo_quality_menu'] = {}
menus_patch_list['photo_quality_menu']['function'] = 'handlePhotoQuality_menu'
menus_patch_list['photo_quality_menu']['line_number'] = {}
menus_patch_list['photo_quality_menu']['line_number']['BTC-7A'] = 56
menus_patch_list['photo_quality_menu']['line_number']['BTC-7E'] = 56
menus_patch_list['photo_quality_menu']['line_number']['BTC-8E'] = 56
menus_patch_list['photo_quality_menu']['line_number']['BTC-7E-HP4'] = 55
menus_patch_list['photo_quality_menu']['line_number']['BTC-8E-HP4'] = 55
menus_patch_list['photo_quality_menu']['line_number']['BTC-7E-HP5'] = 56
menus_patch_list['photo_quality_menu']['line_number']['BTC-8E-HP5'] = 57
menus_patch_list['photo_quality_menu']['start_offset'] = {}
menus_patch_list['photo_quality_menu']['start_offset']['BTC-7A']     = 0x0134a24
menus_patch_list['photo_quality_menu']['start_offset']['BTC-7E']     = 0x0134a24
menus_patch_list['photo_quality_menu']['start_offset']['BTC-8E']     = 0x0135620
menus_patch_list['photo_quality_menu']['start_offset']['BTC-7E-HP4'] = 0x01312d4
menus_patch_list['photo_quality_menu']['start_offset']['BTC-8E-HP4'] = 0x0133e04
menus_patch_list['photo_quality_menu']['start_offset']['BTC-7E-HP5'] = 0x0114314
menus_patch_list['photo_quality_menu']['start_offset']['BTC-8E-HP5'] = 0x0114c6c
menus_patch_list['photo_quality_menu']['change_from_bytes'] = {}
menus_patch_list['photo_quality_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_to_bytes']   = {}
menus_patch_list['photo_quality_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['photo_quality_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])

# in handleVideoLength_menu()
# 57
menus_patch_list['video_length_menu'] = {}
menus_patch_list['video_length_menu']['function'] = 'handleVideoLength_menu'
menus_patch_list['video_length_menu']['line_number'] = {}
menus_patch_list['video_length_menu']['line_number']['BTC-7A'] = 56
menus_patch_list['video_length_menu']['line_number']['BTC-7E'] = 56
menus_patch_list['video_length_menu']['line_number']['BTC-8E'] = 57
menus_patch_list['video_length_menu']['line_number']['BTC-7E-HP4'] = 55
menus_patch_list['video_length_menu']['line_number']['BTC-8E-HP4'] = 56
menus_patch_list['video_length_menu']['line_number']['BTC-7E-HP5'] = 56
menus_patch_list['video_length_menu']['line_number']['BTC-8E-HP5'] = 57
menus_patch_list['video_length_menu']['start_offset'] = {}
#menus_patch_list['video_length_menu']['start_offset']['BTC-7A']     = 0x0025374
menus_patch_list['video_length_menu']['start_offset']['BTC-7A']     = 0x0134858
menus_patch_list['video_length_menu']['start_offset']['BTC-7E']     = 0x0134858
menus_patch_list['video_length_menu']['start_offset']['BTC-8E']     = 0x0135454
menus_patch_list['video_length_menu']['start_offset']['BTC-7E-HP4'] = 0x0131108
menus_patch_list['video_length_menu']['start_offset']['BTC-8E-HP4'] = 0x0133c38
menus_patch_list['video_length_menu']['start_offset']['BTC-7E-HP5'] = 0x0114148
menus_patch_list['video_length_menu']['start_offset']['BTC-8E-HP5'] = 0x0114aa0
menus_patch_list['video_length_menu']['change_from_bytes'] = {}
menus_patch_list['video_length_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_to_bytes']   = {}
menus_patch_list['video_length_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['video_length_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])

# in handleVideoQuality_menu()
# 56
menus_patch_list['video_quality_menu'] = {}
menus_patch_list['video_quality_menu']['function'] = 'handleVideoQuality_menu'
menus_patch_list['video_quality_menu']['line_number'] = {}
menus_patch_list['video_quality_menu']['line_number']['BTC-7A'] = 56
menus_patch_list['video_quality_menu']['line_number']['BTC-7E'] = 56
menus_patch_list['video_quality_menu']['line_number']['BTC-8E'] = 56
menus_patch_list['video_quality_menu']['line_number']['BTC-7E-HP4'] = 55
menus_patch_list['video_quality_menu']['line_number']['BTC-8E-HP4'] = 55
menus_patch_list['video_quality_menu']['line_number']['BTC-7E-HP5'] = 56
menus_patch_list['video_quality_menu']['line_number']['BTC-8E-HP5'] = 56
menus_patch_list['video_quality_menu']['start_offset'] = {}
menus_patch_list['video_quality_menu']['start_offset']['BTC-7A']     = 0x013468c
menus_patch_list['video_quality_menu']['start_offset']['BTC-7E']     = 0x013468c
menus_patch_list['video_quality_menu']['start_offset']['BTC-8E']     = 0x0135288
menus_patch_list['video_quality_menu']['start_offset']['BTC-7E-HP4'] = 0x0130f3c
menus_patch_list['video_quality_menu']['start_offset']['BTC-8E-HP4'] = 0x0133a6c
menus_patch_list['video_quality_menu']['start_offset']['BTC-7E-HP5'] = 0x0113f7c
menus_patch_list['video_quality_menu']['start_offset']['BTC-8E-HP5'] = 0x01148d4
menus_patch_list['video_quality_menu']['change_from_bytes'] = {}
menus_patch_list['video_quality_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_to_bytes']   = {}
menus_patch_list['video_quality_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['video_quality_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handlePhotoDelay_menu()
# 51
menus_patch_list['photo_delay_menu'] = {}
menus_patch_list['photo_delay_menu']['function'] = 'handlePhotoDelay_menu'
menus_patch_list['photo_delay_menu']['line_number'] = {}
menus_patch_list['photo_delay_menu']['line_number']['BTC-7A'] = 51
menus_patch_list['photo_delay_menu']['line_number']['BTC-7E'] = 51
menus_patch_list['photo_delay_menu']['line_number']['BTC-8E'] = 51
menus_patch_list['photo_delay_menu']['line_number']['BTC-7E-HP4'] = 50
menus_patch_list['photo_delay_menu']['line_number']['BTC-8E-HP4'] = 50
menus_patch_list['photo_delay_menu']['line_number']['BTC-7E-HP5'] = 51
menus_patch_list['photo_delay_menu']['line_number']['BTC-8E-HP5'] = 52
menus_patch_list['photo_delay_menu']['start_offset'] = {}
menus_patch_list['photo_delay_menu']['start_offset']['BTC-7A']     = 0x01344bc
menus_patch_list['photo_delay_menu']['start_offset']['BTC-7E']     = 0x01344bc
menus_patch_list['photo_delay_menu']['start_offset']['BTC-8E']     = 0x01350b8
menus_patch_list['photo_delay_menu']['start_offset']['BTC-7E-HP4'] = 0x0130d6c
menus_patch_list['photo_delay_menu']['start_offset']['BTC-8E-HP4'] = 0x013389c
menus_patch_list['photo_delay_menu']['start_offset']['BTC-7E-HP5'] = 0x0113dac
menus_patch_list['photo_delay_menu']['start_offset']['BTC-8E-HP5'] = 0x0114704
menus_patch_list['photo_delay_menu']['change_from_bytes'] = {}
menus_patch_list['photo_delay_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_to_bytes']   = {}
menus_patch_list['photo_delay_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['photo_delay_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleMultiShotMode_menu()
# 57
menus_patch_list['multishot_menu'] = {}
menus_patch_list['multishot_menu']['function'] = 'handleMultiShotMode_menu'
menus_patch_list['multishot_menu']['line_number'] = {}
menus_patch_list['multishot_menu']['line_number']['BTC-7A'] = 56
menus_patch_list['multishot_menu']['line_number']['BTC-7E'] = 56
menus_patch_list['multishot_menu']['line_number']['BTC-8E'] = 57
menus_patch_list['multishot_menu']['line_number']['BTC-7E-HP4'] = 55
menus_patch_list['multishot_menu']['line_number']['BTC-8E-HP4'] = 55
menus_patch_list['multishot_menu']['line_number']['BTC-7E-HP5'] = 56
menus_patch_list['multishot_menu']['line_number']['BTC-8E-HP5'] = 57
menus_patch_list['multishot_menu']['start_offset'] = {}
menus_patch_list['multishot_menu']['start_offset']['BTC-7A']     = 0x01342e0
menus_patch_list['multishot_menu']['start_offset']['BTC-7E']     = 0x01342e0
menus_patch_list['multishot_menu']['start_offset']['BTC-8E']     = 0x0134edc
menus_patch_list['multishot_menu']['start_offset']['BTC-7E-HP4'] = 0x0130b90
menus_patch_list['multishot_menu']['start_offset']['BTC-8E-HP4'] = 0x01336c0
menus_patch_list['multishot_menu']['start_offset']['BTC-7E-HP5'] = 0x0113bcc
menus_patch_list['multishot_menu']['start_offset']['BTC-8E-HP5'] = 0x0114524
menus_patch_list['multishot_menu']['change_from_bytes'] = {}
menus_patch_list['multishot_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_to_bytes']   = {}
menus_patch_list['multishot_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['multishot_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleHDR_menu()
# 52
menus_patch_list['HDR_menu'] = {}
menus_patch_list['HDR_menu']['function'] = 'handleHDR_menu'
menus_patch_list['HDR_menu']['line_number'] = {}
menus_patch_list['HDR_menu']['line_number']['BTC-7E-HP5'] = 76
menus_patch_list['HDR_menu']['line_number']['BTC-8E-HP5'] = 52
menus_patch_list['HDR_menu']['start_offset'] = {}				      
menus_patch_list['HDR_menu']['start_offset']['BTC-7E-HP5'] = 0x01139d8
menus_patch_list['HDR_menu']['start_offset']['BTC-8E-HP5'] = 0x0114330
menus_patch_list['HDR_menu']['change_from_bytes'] = {}
menus_patch_list['HDR_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['HDR_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['HDR_menu']['change_to_bytes']   = {}
menus_patch_list['HDR_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['HDR_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])

# in handleTempUnit_menu()
# 56
menus_patch_list['temp_unit_menu'] = {}
menus_patch_list['temp_unit_menu']['function'] = 'handleTempUnit_menu'
menus_patch_list['temp_unit_menu']['line_number'] = {}
menus_patch_list['temp_unit_menu']['line_number']['BTC-7A'] = 56
menus_patch_list['temp_unit_menu']['line_number']['BTC-7E'] = 56
menus_patch_list['temp_unit_menu']['line_number']['BTC-8E'] = 56
menus_patch_list['temp_unit_menu']['line_number']['BTC-7E-HP4'] = 55
menus_patch_list['temp_unit_menu']['line_number']['BTC-8E-HP4'] = 55
menus_patch_list['temp_unit_menu']['line_number']['BTC-7E-HP5'] = 56
menus_patch_list['temp_unit_menu']['line_number']['BTC-8E-HP5'] = 57
menus_patch_list['temp_unit_menu']['start_offset'] = {}
menus_patch_list['temp_unit_menu']['start_offset']['BTC-7A']     = 0x0134114
menus_patch_list['temp_unit_menu']['start_offset']['BTC-7E']     = 0x0134114
menus_patch_list['temp_unit_menu']['start_offset']['BTC-8E']     = 0x0134d10
menus_patch_list['temp_unit_menu']['start_offset']['BTC-7E-HP4'] = 0x01309c4
menus_patch_list['temp_unit_menu']['start_offset']['BTC-8E-HP4'] = 0x01334f4
menus_patch_list['temp_unit_menu']['start_offset']['BTC-7E-HP5'] = 0x0113744
menus_patch_list['temp_unit_menu']['start_offset']['BTC-8E-HP5'] = 0x011409c
menus_patch_list['temp_unit_menu']['change_from_bytes'] = {}
menus_patch_list['temp_unit_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_to_bytes']   = {}
menus_patch_list['temp_unit_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['temp_unit_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleCameraName_menu()
# 61
menus_patch_list['camera_name_menu'] = {}
menus_patch_list['camera_name_menu']['function'] = 'handleCameraName_menu'
menus_patch_list['camera_name_menu']['line_number'] = {}
menus_patch_list['camera_name_menu']['line_number']['BTC-7A'] = 61
menus_patch_list['camera_name_menu']['line_number']['BTC-7E'] = 61
menus_patch_list['camera_name_menu']['line_number']['BTC-8E'] = 61
menus_patch_list['camera_name_menu']['line_number']['BTC-7E-HP4'] = 60
menus_patch_list['camera_name_menu']['line_number']['BTC-8E-HP4'] = 60
menus_patch_list['camera_name_menu']['line_number']['BTC-7E-HP5'] = 60
menus_patch_list['camera_name_menu']['line_number']['BTC-8E-HP5'] = 61
menus_patch_list['camera_name_menu']['start_offset'] = {}
menus_patch_list['camera_name_menu']['start_offset']['BTC-7E']     = 0x0135958
menus_patch_list['camera_name_menu']['start_offset']['BTC-7E']     = 0x0135958
menus_patch_list['camera_name_menu']['start_offset']['BTC-8E']     = 0x0136554
menus_patch_list['camera_name_menu']['start_offset']['BTC-7E-HP4'] = 0x0132228
menus_patch_list['camera_name_menu']['start_offset']['BTC-8E-HP4'] = 0x0134d58
menus_patch_list['camera_name_menu']['start_offset']['BTC-7E-HP5'] = 0x0115268
menus_patch_list['camera_name_menu']['start_offset']['BTC-8E-HP5'] = 0x0115bc0
menus_patch_list['camera_name_menu']['change_from_bytes'] = {}
menus_patch_list['camera_name_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_to_bytes']   = {}
menus_patch_list['camera_name_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['camera_name_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleImageDataStrip_menu()
# 56
menus_patch_list['info_strip_menu'] = {}
menus_patch_list['info_strip_menu']['function'] = 'handleImageDataStrip_menu'
menus_patch_list['info_strip_menu']['line_number'] = {}
menus_patch_list['info_strip_menu']['line_number']['BTC-7A'] = 56
menus_patch_list['info_strip_menu']['line_number']['BTC-7E'] = 56
menus_patch_list['info_strip_menu']['line_number']['BTC-8E'] = 56
menus_patch_list['info_strip_menu']['line_number']['BTC-7E-HP4'] = 55
menus_patch_list['info_strip_menu']['line_number']['BTC-8E-HP4'] = 55
menus_patch_list['info_strip_menu']['line_number']['BTC-7E-HP5'] = 56
menus_patch_list['info_strip_menu']['line_number']['BTC-8E-HP5'] = 57
menus_patch_list['info_strip_menu']['start_offset'] = {}
menus_patch_list['info_strip_menu']['start_offset']['BTC-7A']     = 0x0133f48
menus_patch_list['info_strip_menu']['start_offset']['BTC-7E']     = 0x0133f48
menus_patch_list['info_strip_menu']['start_offset']['BTC-8E']     = 0x0134b44
menus_patch_list['info_strip_menu']['start_offset']['BTC-7E-HP4'] = 0x01307f8
menus_patch_list['info_strip_menu']['start_offset']['BTC-8E-HP4'] = 0x0133328
menus_patch_list['info_strip_menu']['start_offset']['BTC-7E-HP5'] = 0x0113578
menus_patch_list['info_strip_menu']['start_offset']['BTC-8E-HP5'] = 0x0113ed0
menus_patch_list['info_strip_menu']['change_from_bytes'] = {}
menus_patch_list['info_strip_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_to_bytes']   = {}
menus_patch_list['info_strip_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['info_strip_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleMotionTest_menu()
# 80
menus_patch_list['motion_test_menu'] = {}
menus_patch_list['motion_test_menu']['function'] = 'handleMotionTest_menu'
menus_patch_list['motion_test_menu']['line_number'] = {}
menus_patch_list['motion_test_menu']['line_number']['BTC-7A'] = 80
menus_patch_list['motion_test_menu']['line_number']['BTC-7E'] = 80
menus_patch_list['motion_test_menu']['line_number']['BTC-8E'] = 80
menus_patch_list['motion_test_menu']['line_number']['BTC-7E-HP4'] = 75
menus_patch_list['motion_test_menu']['line_number']['BTC-8E-HP4'] = 75
menus_patch_list['motion_test_menu']['line_number']['BTC-7E-HP5'] = 76
menus_patch_list['motion_test_menu']['line_number']['BTC-8E-HP5'] = 77
menus_patch_list['motion_test_menu']['start_offset'] = {}
menus_patch_list['motion_test_menu']['start_offset']['BTC-7A']     = 0x0133d78
menus_patch_list['motion_test_menu']['start_offset']['BTC-7E']     = 0x0133d78
menus_patch_list['motion_test_menu']['start_offset']['BTC-8E']     = 0x0134974
menus_patch_list['motion_test_menu']['start_offset']['BTC-7E-HP4'] = 0x0130628
menus_patch_list['motion_test_menu']['start_offset']['BTC-8E-HP4'] = 0x0133158
menus_patch_list['motion_test_menu']['start_offset']['BTC-7E-HP5'] = 0x01133a8
menus_patch_list['motion_test_menu']['start_offset']['BTC-8E-HP5'] = 0x0113d00
menus_patch_list['motion_test_menu']['change_from_bytes'] = {}
menus_patch_list['motion_test_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_to_bytes']   = {}
menus_patch_list['motion_test_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['motion_test_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])

# in handlePIRRange_menu()
# 55
menus_patch_list['pir_range_menu'] = {}
menus_patch_list['pir_range_menu']['function'] = 'handlePIRRange_menu'
menus_patch_list['pir_range_menu']['line_number'] = {}
menus_patch_list['pir_range_menu']['line_number']['BTC-7A'] = 55
menus_patch_list['pir_range_menu']['line_number']['BTC-7E'] = 55
menus_patch_list['pir_range_menu']['line_number']['BTC-8E'] = 55
menus_patch_list['pir_range_menu']['line_number']['BTC-7E-HP4'] = 53
menus_patch_list['pir_range_menu']['line_number']['BTC-8E-HP4'] = 53
menus_patch_list['pir_range_menu']['line_number']['BTC-7E-HP5'] = 54
menus_patch_list['pir_range_menu']['line_number']['BTC-8E-HP5'] = 54
menus_patch_list['pir_range_menu']['start_offset'] = {}
menus_patch_list['pir_range_menu']['start_offset']['BTC-7A']     = 0x0133aac
menus_patch_list['pir_range_menu']['start_offset']['BTC-7E']     = 0x0133aac
menus_patch_list['pir_range_menu']['start_offset']['BTC-8E']     = 0x01346a8
menus_patch_list['pir_range_menu']['start_offset']['BTC-7E-HP4'] = 0x013035c
menus_patch_list['pir_range_menu']['start_offset']['BTC-8E-HP4'] = 0x0132e8c
menus_patch_list['pir_range_menu']['start_offset']['BTC-7E-HP5'] = 0x01130dc
menus_patch_list['pir_range_menu']['start_offset']['BTC-8E-HP5'] = 0x0113a34
menus_patch_list['pir_range_menu']['change_from_bytes'] = {}
menus_patch_list['pir_range_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_to_bytes']   = {}
menus_patch_list['pir_range_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['pir_range_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleBatteryType_menu()
# 58
menus_patch_list['battery_type_menu'] = {}
menus_patch_list['battery_type_menu']['function'] = 'handleBatteryType_menu'
menus_patch_list['battery_type_menu']['line_number'] = {}
menus_patch_list['battery_type_menu']['line_number']['BTC-7A'] = 58
menus_patch_list['battery_type_menu']['line_number']['BTC-7E'] = 58
menus_patch_list['battery_type_menu']['line_number']['BTC-8E'] = 58
menus_patch_list['battery_type_menu']['line_number']['BTC-7E-HP4'] = 57
menus_patch_list['battery_type_menu']['line_number']['BTC-8E-HP4'] = 57
menus_patch_list['battery_type_menu']['line_number']['BTC-7E-HP5'] = 59
menus_patch_list['battery_type_menu']['line_number']['BTC-8E-HP5'] = 60
menus_patch_list['battery_type_menu']['start_offset'] = {}
menus_patch_list['battery_type_menu']['start_offset']['BTC-7A']     = 0x01338bc
menus_patch_list['battery_type_menu']['start_offset']['BTC-7E']     = 0x01338bc
menus_patch_list['battery_type_menu']['start_offset']['BTC-8E']     = 0x01344b8
menus_patch_list['battery_type_menu']['start_offset']['BTC-7E-HP4'] = 0x013016c
menus_patch_list['battery_type_menu']['start_offset']['BTC-8E-HP4'] = 0x0132c9c
menus_patch_list['battery_type_menu']['start_offset']['BTC-7E-HP5'] = 0x0112ef4
menus_patch_list['battery_type_menu']['start_offset']['BTC-8E-HP5'] = 0x011384c
menus_patch_list['battery_type_menu']['change_from_bytes'] = {}
menus_patch_list['battery_type_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_to_bytes']   = {}
menus_patch_list['battery_type_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['battery_type_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleTriggerSpeed_menu()
# 57
menus_patch_list['trigger_speed_menu'] = {}
menus_patch_list['trigger_speed_menu']['function'] = 'handleTriggerSpeed_menu'
menus_patch_list['trigger_speed_menu']['line_number'] = {}
menus_patch_list['trigger_speed_menu']['line_number']['BTC-7A'] = 57
menus_patch_list['trigger_speed_menu']['line_number']['BTC-7E'] = 57
menus_patch_list['trigger_speed_menu']['line_number']['BTC-8E'] = 57
menus_patch_list['trigger_speed_menu']['line_number']['BTC-7E-HP4'] = 56
menus_patch_list['trigger_speed_menu']['line_number']['BTC-8E-HP4'] = 56
menus_patch_list['trigger_speed_menu']['line_number']['BTC-7E-HP5'] = 57
menus_patch_list['trigger_speed_menu']['line_number']['BTC-8E-HP5'] = 57
menus_patch_list['trigger_speed_menu']['start_offset'] = {}
menus_patch_list['trigger_speed_menu']['start_offset']['BTC-7A']     = 0x01336e4
menus_patch_list['trigger_speed_menu']['start_offset']['BTC-7E']     = 0x01336e4
menus_patch_list['trigger_speed_menu']['start_offset']['BTC-8E']     = 0x01342e0
menus_patch_list['trigger_speed_menu']['start_offset']['BTC-7E-HP4'] = 0x012ff94
menus_patch_list['trigger_speed_menu']['start_offset']['BTC-8E-HP4'] = 0x0132ac4
menus_patch_list['trigger_speed_menu']['start_offset']['BTC-7E-HP5'] = 0x0112d1c
menus_patch_list['trigger_speed_menu']['start_offset']['BTC-8E-HP5'] = 0x0113674
menus_patch_list['trigger_speed_menu']['change_from_bytes'] = {}
menus_patch_list['trigger_speed_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_to_bytes']   = {}
menus_patch_list['trigger_speed_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['trigger_speed_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleRestoreDefault_menu()
# 58
menus_patch_list['restore_default_menu'] = {}
menus_patch_list['restore_default_menu']['function'] = 'handleRestoreDefault_menu'
menus_patch_list['restore_default_menu']['line_number'] = {}
menus_patch_list['restore_default_menu']['line_number']['BTC-7A'] = 59
menus_patch_list['restore_default_menu']['line_number']['BTC-7E'] = 59 
menus_patch_list['restore_default_menu']['line_number']['BTC-8E'] = 58
menus_patch_list['restore_default_menu']['line_number']['BTC-7E-HP4'] = 56
menus_patch_list['restore_default_menu']['line_number']['BTC-8E-HP4'] = 56
menus_patch_list['restore_default_menu']['line_number']['BTC-7E-HP5'] = 58
menus_patch_list['restore_default_menu']['line_number']['BTC-8E-HP5'] = 58
menus_patch_list['restore_default_menu']['start_offset'] = {}
menus_patch_list['restore_default_menu']['start_offset']['BTC-7A']     = 0x0133514
menus_patch_list['restore_default_menu']['start_offset']['BTC-7E']     = 0x0133514
menus_patch_list['restore_default_menu']['start_offset']['BTC-8E']     = 0x0134110
menus_patch_list['restore_default_menu']['start_offset']['BTC-7E-HP4'] = 0x012fdc4
menus_patch_list['restore_default_menu']['start_offset']['BTC-8E-HP4'] = 0x01328f4
menus_patch_list['restore_default_menu']['start_offset']['BTC-7E-HP5'] = 0x0112b4c
menus_patch_list['restore_default_menu']['start_offset']['BTC-8E-HP5'] = 0x01134a4
menus_patch_list['restore_default_menu']['change_from_bytes'] = {}
menus_patch_list['restore_default_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_to_bytes']   = {}
menus_patch_list['restore_default_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['restore_default_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleTimelapseFreq_menu()
# 57
menus_patch_list['timelapse_freq_menu'] = {}
menus_patch_list['timelapse_freq_menu']['function'] = 'handleTimelapseFreq_menu'
menus_patch_list['timelapse_freq_menu']['line_number'] = {}
menus_patch_list['timelapse_freq_menu']['line_number']['BTC-7A'] = 56
menus_patch_list['timelapse_freq_menu']['line_number']['BTC-7E'] = 56
menus_patch_list['timelapse_freq_menu']['line_number']['BTC-8E'] = 57
menus_patch_list['timelapse_freq_menu']['line_number']['BTC-7E-HP4'] = 55
menus_patch_list['timelapse_freq_menu']['line_number']['BTC-8E-HP4'] = 55
menus_patch_list['timelapse_freq_menu']['line_number']['BTC-7E-HP5'] = 56
menus_patch_list['timelapse_freq_menu']['line_number']['BTC-8E-HP5'] = 57
menus_patch_list['timelapse_freq_menu']['start_offset'] = {}
menus_patch_list['timelapse_freq_menu']['start_offset']['BTC-7A']     = 0x0133340
menus_patch_list['timelapse_freq_menu']['start_offset']['BTC-7E']     = 0x0133340
menus_patch_list['timelapse_freq_menu']['start_offset']['BTC-8E']     = 0x0133f3c
menus_patch_list['timelapse_freq_menu']['start_offset']['BTC-7E-HP4'] = 0x012fbf0
menus_patch_list['timelapse_freq_menu']['start_offset']['BTC-8E-HP4'] = 0x0132720
menus_patch_list['timelapse_freq_menu']['start_offset']['BTC-7E-HP5'] = 0x0112978
menus_patch_list['timelapse_freq_menu']['start_offset']['BTC-8E-HP5'] = 0x01132d0
menus_patch_list['timelapse_freq_menu']['change_from_bytes'] = {}
menus_patch_list['timelapse_freq_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_to_bytes']   = {}
menus_patch_list['timelapse_freq_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_freq_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleTimelapsePeriod_menu()
# 56
menus_patch_list['timelapse_period_menu'] = {}
menus_patch_list['timelapse_period_menu']['function'] = 'handleTimelapsePeriod_menu'
menus_patch_list['timelapse_period_menu']['line_number'] = {}
menus_patch_list['timelapse_period_menu']['line_number']['BTC-7A'] = 56
menus_patch_list['timelapse_period_menu']['line_number']['BTC-7E'] = 56
menus_patch_list['timelapse_period_menu']['line_number']['BTC-8E'] = 56
menus_patch_list['timelapse_period_menu']['line_number']['BTC-7E-HP4'] = 55
menus_patch_list['timelapse_period_menu']['line_number']['BTC-8E-HP4'] = 55
menus_patch_list['timelapse_period_menu']['line_number']['BTC-7E-HP5'] = 56
menus_patch_list['timelapse_period_menu']['line_number']['BTC-8E-HP5'] = 56
menus_patch_list['timelapse_period_menu']['start_offset'] = {}
menus_patch_list['timelapse_period_menu']['start_offset']['BTC-7A']     = 0x0133174
menus_patch_list['timelapse_period_menu']['start_offset']['BTC-7E']     = 0x0133174
menus_patch_list['timelapse_period_menu']['start_offset']['BTC-8E']     = 0x0133d70
menus_patch_list['timelapse_period_menu']['start_offset']['BTC-7E-HP4'] = 0x012fa24
menus_patch_list['timelapse_period_menu']['start_offset']['BTC-8E-HP4'] = 0x0132554
menus_patch_list['timelapse_period_menu']['start_offset']['BTC-7E-HP5'] = 0x01127ac
menus_patch_list['timelapse_period_menu']['start_offset']['BTC-8E-HP5'] = 0x0113104
menus_patch_list['timelapse_period_menu']['change_from_bytes'] = {}
menus_patch_list['timelapse_period_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_to_bytes']   = {}
menus_patch_list['timelapse_period_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['timelapse_period_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in handleDeleteAll_menu()
# 104
menus_patch_list['delete_all_menu'] = {}
menus_patch_list['delete_all_menu']['function'] = 'handleDeleteAll_menu'
menus_patch_list['delete_all_menu']['line_number'] = {}
menus_patch_list['delete_all_menu']['line_number']['BTC-7A'] = 106
menus_patch_list['delete_all_menu']['line_number']['BTC-7E'] = 106
menus_patch_list['delete_all_menu']['line_number']['BTC-8E'] = 104
menus_patch_list['delete_all_menu']['line_number']['BTC-7E-HP4'] = 102
menus_patch_list['delete_all_menu']['line_number']['BTC-8E-HP4'] = 102
menus_patch_list['delete_all_menu']['line_number']['BTC-7E-HP5'] = 103
menus_patch_list['delete_all_menu']['line_number']['BTC-8E-HP5'] = 104
menus_patch_list['delete_all_menu']['start_offset'] = {}
menus_patch_list['delete_all_menu']['start_offset']['BTC-7A']     = 0x0132fa8
menus_patch_list['delete_all_menu']['start_offset']['BTC-7E']     = 0x0132fa8
menus_patch_list['delete_all_menu']['start_offset']['BTC-8E']     = 0x0133ba4
menus_patch_list['delete_all_menu']['start_offset']['BTC-7E-HP4'] = 0x012f858
menus_patch_list['delete_all_menu']['start_offset']['BTC-8E-HP4'] = 0x0132388
menus_patch_list['delete_all_menu']['start_offset']['BTC-7E-HP5'] = 0x01125e0
menus_patch_list['delete_all_menu']['start_offset']['BTC-8E-HP5'] = 0x0112f38
menus_patch_list['delete_all_menu']['change_from_bytes'] = {}
menus_patch_list['delete_all_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_to_bytes']   = {}
menus_patch_list['delete_all_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['delete_all_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in  handleIRLedPower_menu()
# 57
menus_patch_list['ir_led_power_menu'] = {}
menus_patch_list['ir_led_power_menu']['function'] =  'handleIRLedPower_menu'
menus_patch_list['ir_led_power_menu']['line_number'] = {}
menus_patch_list['ir_led_power_menu']['line_number']['BTC-7A'] = 57
menus_patch_list['ir_led_power_menu']['line_number']['BTC-7E'] = 57
menus_patch_list['ir_led_power_menu']['line_number']['BTC-8E'] = 57
menus_patch_list['ir_led_power_menu']['line_number']['BTC-7E-HP4'] = 56
menus_patch_list['ir_led_power_menu']['line_number']['BTC-8E-HP4'] = 56
menus_patch_list['ir_led_power_menu']['line_number']['BTC-7E-HP5'] = 57
menus_patch_list['ir_led_power_menu']['line_number']['BTC-8E-HP5'] = 58
menus_patch_list['ir_led_power_menu']['start_offset'] = {}
menus_patch_list['ir_led_power_menu']['start_offset']['BTC-7A']     = 0x0132cdc
menus_patch_list['ir_led_power_menu']['start_offset']['BTC-7E']     = 0x0132cdc
menus_patch_list['ir_led_power_menu']['start_offset']['BTC-8E']     = 0x01338d8
menus_patch_list['ir_led_power_menu']['start_offset']['BTC-7E-HP4'] = 0x012f58c
menus_patch_list['ir_led_power_menu']['start_offset']['BTC-8E-HP4'] = 0x01320bc
menus_patch_list['ir_led_power_menu']['start_offset']['BTC-7E-HP5'] = 0x0112314
menus_patch_list['ir_led_power_menu']['start_offset']['BTC-8E-HP5'] = 0x0112c6c
menus_patch_list['ir_led_power_menu']['change_from_bytes'] = {}
menus_patch_list['ir_led_power_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_to_bytes']   = {}
menus_patch_list['ir_led_power_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['ir_led_power_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in  handleSmartIRVideo_menu()
# 58
menus_patch_list['smart_ir_video_menu'] = {}
menus_patch_list['smart_ir_video_menu']['function'] =  'handleSmartIRVideo_menu'
menus_patch_list['smart_ir_video_menu']['line_number'] = {}
menus_patch_list['smart_ir_video_menu']['line_number']['BTC-7A'] = 57 
menus_patch_list['smart_ir_video_menu']['line_number']['BTC-7E'] = 57
menus_patch_list['smart_ir_video_menu']['line_number']['BTC-8E'] = 58
menus_patch_list['smart_ir_video_menu']['line_number']['BTC-7E-HP4'] = 56
menus_patch_list['smart_ir_video_menu']['line_number']['BTC-8E-HP4'] = 56 
menus_patch_list['smart_ir_video_menu']['line_number']['BTC-7E-HP5'] = 57
menus_patch_list['smart_ir_video_menu']['line_number']['BTC-8E-HP5'] = 58 
menus_patch_list['smart_ir_video_menu']['start_offset'] = {}
menus_patch_list['smart_ir_video_menu']['start_offset']['BTC-7A']     = 0x0132b0c
menus_patch_list['smart_ir_video_menu']['start_offset']['BTC-7E']     = 0x0132b0c
menus_patch_list['smart_ir_video_menu']['start_offset']['BTC-8E']     = 0x0133708
menus_patch_list['smart_ir_video_menu']['start_offset']['BTC-7E-HP4'] = 0x012f3bc
menus_patch_list['smart_ir_video_menu']['start_offset']['BTC-8E-HP4'] = 0x0131eec
menus_patch_list['smart_ir_video_menu']['start_offset']['BTC-7E-HP5'] = 0x0112144
menus_patch_list['smart_ir_video_menu']['start_offset']['BTC-8E-HP5'] = 0x0112a9c
menus_patch_list['smart_ir_video_menu']['change_from_bytes'] = {}
menus_patch_list['smart_ir_video_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_to_bytes']   = {}
menus_patch_list['smart_ir_video_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['smart_ir_video_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in  handleSDManagement_menu()
# 57
menus_patch_list['sd_management_menu'] = {}
menus_patch_list['sd_management_menu']['function'] =  'handleSDManagement_menu'
menus_patch_list['sd_management_menu']['line_number'] = {}
menus_patch_list['sd_management_menu']['line_number']['BTC-7A'] = 57
menus_patch_list['sd_management_menu']['line_number']['BTC-7E'] = 57
menus_patch_list['sd_management_menu']['line_number']['BTC-8E'] = 57
menus_patch_list['sd_management_menu']['line_number']['BTC-7E-HP4'] = 56
menus_patch_list['sd_management_menu']['line_number']['BTC-8E-HP4'] = 56
menus_patch_list['sd_management_menu']['line_number']['BTC-7E-HP5'] = 57
menus_patch_list['sd_management_menu']['line_number']['BTC-8E-HP5'] = 58
menus_patch_list['sd_management_menu']['start_offset'] = {}
menus_patch_list['sd_management_menu']['start_offset']['BTC-7A']     = 0x013293c
menus_patch_list['sd_management_menu']['start_offset']['BTC-7E']     = 0x013293c
menus_patch_list['sd_management_menu']['start_offset']['BTC-8E']     = 0x0133538
menus_patch_list['sd_management_menu']['start_offset']['BTC-7E-HP4'] = 0x012f1ec
menus_patch_list['sd_management_menu']['start_offset']['BTC-8E-HP4'] = 0x0131d1c
menus_patch_list['sd_management_menu']['start_offset']['BTC-7E-HP5'] = 0x0111f74
menus_patch_list['sd_management_menu']['start_offset']['BTC-8E-HP5'] = 0x01128cc
menus_patch_list['sd_management_menu']['change_from_bytes'] = {}
menus_patch_list['sd_management_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_to_bytes']   = {}
menus_patch_list['sd_management_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['sd_management_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in  handleLanguage_menu()
# 51
menus_patch_list['language_menu'] = {}
menus_patch_list['language_menu']['function'] =  'handleLanguage_menu'
menus_patch_list['language_menu']['line_number'] = {}
menus_patch_list['language_menu']['line_number']['BTC-7A'] = 51
menus_patch_list['language_menu']['line_number']['BTC-7E'] = 51
menus_patch_list['language_menu']['line_number']['BTC-8E'] = 51
menus_patch_list['language_menu']['line_number']['BTC-7E-HP4'] = 50
menus_patch_list['language_menu']['line_number']['BTC-8E-HP4'] = 50
menus_patch_list['language_menu']['line_number']['BTC-7E-HP5'] = 51
menus_patch_list['language_menu']['line_number']['BTC-8E-HP5'] = 58
menus_patch_list['language_menu']['start_offset'] = {}
menus_patch_list['language_menu']['start_offset']['BTC-7A']     = 0x0132768
menus_patch_list['language_menu']['start_offset']['BTC-7E']     = 0x0132768
menus_patch_list['language_menu']['start_offset']['BTC-8E']     = 0x0133364
menus_patch_list['language_menu']['start_offset']['BTC-7E-HP4'] = 0x012f018
menus_patch_list['language_menu']['start_offset']['BTC-8E-HP4'] = 0x0131b48
menus_patch_list['language_menu']['start_offset']['BTC-7E-HP5'] = 0x0111da0
menus_patch_list['language_menu']['start_offset']['BTC-8E-HP5'] = 0x01126f8
menus_patch_list['language_menu']['change_from_bytes'] = {}
menus_patch_list['language_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_to_bytes']   = {}
menus_patch_list['language_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['language_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in  handleCaptureTimerP_menu()
# 62
menus_patch_list['capture_timer_menu'] = {}
menus_patch_list['capture_timer_menu']['function'] =  'handleCaptureTimerP_menu'
menus_patch_list['capture_timer_menu']['line_number'] = {}
menus_patch_list['capture_timer_menu']['line_number']['BTC-7A'] = 54
menus_patch_list['capture_timer_menu']['line_number']['BTC-7E'] = 54
menus_patch_list['capture_timer_menu']['line_number']['BTC-8E'] = 62
menus_patch_list['capture_timer_menu']['line_number']['BTC-7E-HP4'] = 60
menus_patch_list['capture_timer_menu']['line_number']['BTC-8E-HP4'] = 60
menus_patch_list['capture_timer_menu']['line_number']['BTC-7E-HP5'] = 61
menus_patch_list['capture_timer_menu']['line_number']['BTC-8E-HP5'] = 62
menus_patch_list['capture_timer_menu']['start_offset'] = {}
menus_patch_list['capture_timer_menu']['start_offset']['BTC-7A']     = 0x0132590
menus_patch_list['capture_timer_menu']['start_offset']['BTC-7E']     = 0x0132590
menus_patch_list['capture_timer_menu']['start_offset']['BTC-8E']     = 0x013318c
menus_patch_list['capture_timer_menu']['start_offset']['BTC-7E-HP4'] = 0x012ee44
menus_patch_list['capture_timer_menu']['start_offset']['BTC-8E-HP4'] = 0x0131974
menus_patch_list['capture_timer_menu']['start_offset']['BTC-7E-HP5'] = 0x0111bcc
menus_patch_list['capture_timer_menu']['start_offset']['BTC-8E-HP5'] = 0x0112524
menus_patch_list['capture_timer_menu']['change_from_bytes'] = {}
menus_patch_list['capture_timer_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_to_bytes']   = {}
menus_patch_list['capture_timer_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['capture_timer_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in  handleSetCaptureTimerParams_menu()
# 118
menus_patch_list['set_capture_timer_menu'] = {}
menus_patch_list['set_capture_timer_menu']['function'] =  'handleSetCaptureTimerParams_menu'
menus_patch_list['set_capture_timer_menu']['line_number'] = {}
menus_patch_list['set_capture_timer_menu']['line_number']['BTC-7A'] = 115
menus_patch_list['set_capture_timer_menu']['line_number']['BTC-7E'] = 115
menus_patch_list['set_capture_timer_menu']['line_number']['BTC-8E'] = 118
menus_patch_list['set_capture_timer_menu']['line_number']['BTC-7E-HP4'] = 115
menus_patch_list['set_capture_timer_menu']['line_number']['BTC-8E-HP4'] = 115
menus_patch_list['set_capture_timer_menu']['line_number']['BTC-7E-HP5'] = 119
menus_patch_list['set_capture_timer_menu']['line_number']['BTC-8E-HP5'] = 118
menus_patch_list['set_capture_timer_menu']['start_offset'] = {}
menus_patch_list['set_capture_timer_menu']['start_offset']['BTC-7A']     = 0x0136050
menus_patch_list['set_capture_timer_menu']['start_offset']['BTC-7E']     = 0x0136050
menus_patch_list['set_capture_timer_menu']['start_offset']['BTC-8E']     = 0x0136c4c
menus_patch_list['set_capture_timer_menu']['start_offset']['BTC-7E-HP4'] = 0x0132920
menus_patch_list['set_capture_timer_menu']['start_offset']['BTC-8E-HP4'] = 0x0135450
menus_patch_list['set_capture_timer_menu']['start_offset']['BTC-7E-HP5'] = 0x0115960
menus_patch_list['set_capture_timer_menu']['start_offset']['BTC-8E-HP5'] = 0x01162b8
menus_patch_list['set_capture_timer_menu']['change_from_bytes'] = {}
menus_patch_list['set_capture_timer_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_to_bytes']   = {}
menus_patch_list['set_capture_timer_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['set_capture_timer_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
# in  handleFirmwareUpgrade_menu()
# 78
menus_patch_list['firmware_upgrade_menu'] = {}
menus_patch_list['firmware_upgrade_menu']['function'] =  'handleFirmwareUpgrade_menu'
menus_patch_list['firmware_upgrade_menu']['line_number'] = {}
menus_patch_list['firmware_upgrade_menu']['line_number']['BTC-7A'] = 78
menus_patch_list['firmware_upgrade_menu']['line_number']['BTC-7E'] = 78
menus_patch_list['firmware_upgrade_menu']['line_number']['BTC-8E'] = 78
menus_patch_list['firmware_upgrade_menu']['line_number']['BTC-7E-HP4'] = 72
menus_patch_list['firmware_upgrade_menu']['line_number']['BTC-8E-HP4'] = 72
menus_patch_list['firmware_upgrade_menu']['line_number']['BTC-7E-HP5'] = 74
menus_patch_list['firmware_upgrade_menu']['line_number']['BTC-8E-HP5'] = 74
menus_patch_list['firmware_upgrade_menu']['start_offset'] = {}
menus_patch_list['firmware_upgrade_menu']['start_offset']['BTC-7A']     = 0x0131fcc
menus_patch_list['firmware_upgrade_menu']['start_offset']['BTC-7E']     = 0x0131fcc
menus_patch_list['firmware_upgrade_menu']['start_offset']['BTC-8E']     = 0x0132bc8
menus_patch_list['firmware_upgrade_menu']['start_offset']['BTC-7E-HP4'] = 0x012e890
menus_patch_list['firmware_upgrade_menu']['start_offset']['BTC-8E-HP4'] = 0x01313c0
menus_patch_list['firmware_upgrade_menu']['start_offset']['BTC-7E-HP5'] = 0x0111618
menus_patch_list['firmware_upgrade_menu']['start_offset']['BTC-8E-HP5'] = 0x0111f70
menus_patch_list['firmware_upgrade_menu']['change_from_bytes'] = {}
menus_patch_list['firmware_upgrade_menu']['change_from_bytes']['BTC-7A']     = bytes([menus_define_expected_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_from_bytes']['BTC-7E']     = bytes([menus_define_expected_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_from_bytes']['BTC-8E']     = bytes([menus_define_expected_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']   = {}
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']['BTC-7A']       = bytes([menus_define_new_end_state['BTC-7A'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']['BTC-7E']       = bytes([menus_define_new_end_state['BTC-7E'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']['BTC-8E']       = bytes([menus_define_new_end_state['BTC-8E'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([menus_define_new_end_state['BTC-7E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([menus_define_new_end_state['BTC-8E-HP4'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([menus_define_new_end_state['BTC-7E-HP5'], 0x00, 0x04, 0x24])
menus_patch_list['firmware_upgrade_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([menus_define_new_end_state['BTC-8E-HP5'], 0x00, 0x04, 0x24])



if evsd_active:
##################################################################
## Extended SD Card power
  extended_SD_power_patch_list = {}



# in HceTaskRecording_RecVideoEnd()
# source code line 34
  extended_SD_power_patch_list['extend_video'] = {}
  extended_SD_power_patch_list['extend_video']['function'] = 'HceTaskRecording_RecVideoEnd'
  extended_SD_power_patch_list['extend_video']['line_number'] = {}
  extended_SD_power_patch_list['extend_video']['line_number']['BTC-7E'] = 34
  extended_SD_power_patch_list['extend_video']['line_number']['BTC-8E'] = 34
  extended_SD_power_patch_list['extend_video']['line_number']['BTC-7E-HP4'] = 77
  extended_SD_power_patch_list['extend_video']['line_number']['BTC-8E-HP4'] = 77
  extended_SD_power_patch_list['extend_video']['line_number']['BTC-7E-HP5'] = 74
  extended_SD_power_patch_list['extend_video']['line_number']['BTC-8E-HP5'] = 74
  extended_SD_power_patch_list['extend_video']['start_offset'] = {}
  extended_SD_power_patch_list['extend_video']['start_offset']['BTC-7E']     = 0x0124d20
  extended_SD_power_patch_list['extend_video']['start_offset']['BTC-8E']     = 0x01250d8
  extended_SD_power_patch_list['extend_video']['start_offset']['BTC-7E-HP4'] = 0x011f778
  extended_SD_power_patch_list['extend_video']['start_offset']['BTC-8E-HP4'] = 0x011fcd0
  extended_SD_power_patch_list['extend_video']['start_offset']['BTC-7E-HP5'] = 0x0102934
  extended_SD_power_patch_list['extend_video']['start_offset']['BTC-8E-HP5'] = 0x0102a0c
  extended_SD_power_patch_list['extend_video']['change_from_jump'] = 'jal.check_remaining_sd_capacity'
  extended_SD_power_patch_list['extend_video']['change_to_jump']   = 'jal.evsd_check_remaining_sd_capacity'
  # in HceTaskStill_End()
  # source code line 47
  extended_SD_power_patch_list['extend_still'] = {}
  extended_SD_power_patch_list['extend_still']['function'] = 'HceTaskStill_End'
  extended_SD_power_patch_list['extend_still']['line_number'] = {}
  extended_SD_power_patch_list['extend_still']['line_number']['BTC-7E'] = 47
  extended_SD_power_patch_list['extend_still']['line_number']['BTC-8E'] = 47
  extended_SD_power_patch_list['extend_still']['line_number']['BTC-7E-HP4'] = 50
  extended_SD_power_patch_list['extend_still']['line_number']['BTC-8E-HP4'] = 50
  extended_SD_power_patch_list['extend_still']['line_number']['BTC-7E-HP5'] = 56
  extended_SD_power_patch_list['extend_still']['line_number']['BTC-8E-HP5'] = 56
  extended_SD_power_patch_list['extend_still']['start_offset'] = {}
  extended_SD_power_patch_list['extend_still']['start_offset']['BTC-7E']     = 0x0125b40
  extended_SD_power_patch_list['extend_still']['start_offset']['BTC-8E']     = 0x0125ef8
  extended_SD_power_patch_list['extend_still']['start_offset']['BTC-7E-HP4'] = 0x0121b04
  extended_SD_power_patch_list['extend_still']['start_offset']['BTC-8E-HP4'] = 0x0122054
  extended_SD_power_patch_list['extend_still']['start_offset']['BTC-7E-HP5'] = 0x0104fe4
  extended_SD_power_patch_list['extend_still']['start_offset']['BTC-8E-HP5'] = 0x01050ac
  extended_SD_power_patch_list['extend_still']['change_from_jump'] = 'jal.check_remaining_sd_capacity'
  extended_SD_power_patch_list['extend_still']['change_to_jump']   = 'jal.evsd_check_remaining_sd_capacity'

  # in HcePower_CommonPowerOff()
  # line 20
  extended_SD_power_patch_list['power_off'] = {}
  extended_SD_power_patch_list['power_off']['function'] = 'HcePower_CommonPowerOff'
  extended_SD_power_patch_list['power_off']['line_number'] = {}
  extended_SD_power_patch_list['power_off']['line_number']['BTC-7E'] = 20
  extended_SD_power_patch_list['power_off']['line_number']['BTC-8E'] = 20
  extended_SD_power_patch_list['power_off']['line_number']['BTC-7E-HP4'] = 24
  extended_SD_power_patch_list['power_off']['line_number']['BTC-8E-HP4'] = 22
  extended_SD_power_patch_list['power_off']['line_number']['BTC-87E-HP5'] = 24
  extended_SD_power_patch_list['power_off']['line_number']['BTC-8E-HP5'] = 24
  extended_SD_power_patch_list['power_off']['start_offset'] = {}
  extended_SD_power_patch_list['power_off']['start_offset']['BTC-7E']     = 0x0113334
  extended_SD_power_patch_list['power_off']['start_offset']['BTC-8E']     = 0x011358c
  extended_SD_power_patch_list['power_off']['start_offset']['BTC-7E-HP4'] = 0x010e3d8
  extended_SD_power_patch_list['power_off']['start_offset']['BTC-8E-HP4'] = 0x010e8d8
  extended_SD_power_patch_list['power_off']['start_offset']['BTC-7E-HP5'] = 0x00eb6e4
  extended_SD_power_patch_list['power_off']['start_offset']['BTC-8E-HP5'] = 0x00eb7a0
  extended_SD_power_patch_list['power_off']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
  extended_SD_power_patch_list['power_off']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
  # in still_MCUApp_ResetPIRPin()
  # line 60
  extended_SD_power_patch_list['reset_PIR_pin'] = {}
  extended_SD_power_patch_list['reset_PIR_pin']['function'] = 'still_MCUApp_ResetPIRPin'
  extended_SD_power_patch_list['reset_PIR_pin']['line_number'] = {}
  extended_SD_power_patch_list['reset_PIR_pin']['line_number']['BTC-7E'] = 60
  extended_SD_power_patch_list['reset_PIR_pin']['line_number']['BTC-8E'] = 60
  extended_SD_power_patch_list['reset_PIR_pin']['line_number']['BTC-7E-HP4'] = 59
  extended_SD_power_patch_list['reset_PIR_pin']['line_number']['BTC-8E-HP4'] = 59
  extended_SD_power_patch_list['reset_PIR_pin']['line_number']['BTC-7E-HP5'] = 88
  extended_SD_power_patch_list['reset_PIR_pin']['line_number']['BTC-8E-HP5'] = 95
  extended_SD_power_patch_list['reset_PIR_pin']['start_offset'] = {}
  extended_SD_power_patch_list['reset_PIR_pin']['start_offset']['BTC-7E']     = 0x0123b64
  extended_SD_power_patch_list['reset_PIR_pin']['start_offset']['BTC-8E']     = 0x0123f24
  extended_SD_power_patch_list['reset_PIR_pin']['start_offset']['BTC-7E-HP4'] = 0x011f944
  extended_SD_power_patch_list['reset_PIR_pin']['start_offset']['BTC-8E-HP4'] = 0x011fe9c
  extended_SD_power_patch_list['reset_PIR_pin']['start_offset']['BTC-7E-HP5'] = 0x0102b58
  extended_SD_power_patch_list['reset_PIR_pin']['start_offset']['BTC-8E-HP5'] = 0x0102c30
  extended_SD_power_patch_list['reset_PIR_pin']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
  extended_SD_power_patch_list['reset_PIR_pin']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
  # in TaskRecording_FSM_task9()
  # line 55
  extended_SD_power_patch_list['recording_task9'] = {}
  extended_SD_power_patch_list['recording_task9']['function'] = {}
  extended_SD_power_patch_list['recording_task9']['function']['BTC-7E'] = 'TaskRecording_FSM_task9'
  extended_SD_power_patch_list['recording_task9']['function']['BTC-8E'] = 'TaskRecording_FSM_task9'
  extended_SD_power_patch_list['recording_task9']['function']['BTC-7E-HP4'] = 'TaskRecording_FSM_task10'
  extended_SD_power_patch_list['recording_task9']['function']['BTC-8E-HP4'] = 'TaskRecording_FSM_task10'
  extended_SD_power_patch_list['recording_task9']['function']['BTC-7E-HP5'] = 'TaskRecording_FSM_task10'
  extended_SD_power_patch_list['recording_task9']['function']['BTC-8E-HP5'] = 'TaskRecording_FSM_task10'
  extended_SD_power_patch_list['recording_task9']['line_number'] = {}
  extended_SD_power_patch_list['recording_task9']['line_number']['BTC-7E'] = 55
  extended_SD_power_patch_list['recording_task9']['line_number']['BTC-8E'] = 55
  extended_SD_power_patch_list['recording_task9']['line_number']['BTC-7E-HP4'] = 46
  extended_SD_power_patch_list['recording_task9']['line_number']['BTC-8E-HP4'] = 46
  extended_SD_power_patch_list['recording_task9']['line_number']['BTC-7E-HP5'] = 46
  extended_SD_power_patch_list['recording_task9']['line_number']['BTC-8E-HP5'] = 45
  extended_SD_power_patch_list['recording_task9']['start_offset'] = {}
  extended_SD_power_patch_list['recording_task9']['start_offset']['BTC-7E']     = 0x0123d70
  extended_SD_power_patch_list['recording_task9']['start_offset']['BTC-8E']     = 0x0124130
  extended_SD_power_patch_list['recording_task9']['start_offset']['BTC-7E-HP4'] = 0x011fb4c
  extended_SD_power_patch_list['recording_task9']['start_offset']['BTC-8E-HP4'] = 0x01200a4
  extended_SD_power_patch_list['recording_task9']['start_offset']['BTC-7E-HP5'] = 0x0102df0
  extended_SD_power_patch_list['recording_task9']['start_offset']['BTC-8E-HP5'] = 0x0102ec8
  extended_SD_power_patch_list['recording_task9']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
  extended_SD_power_patch_list['recording_task9']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
  # in HceTaskStill_End()
  # line 43
  extended_SD_power_patch_list['still_end'] = {}
  extended_SD_power_patch_list['still_end']['function'] = 'HceTaskStill_End'
  extended_SD_power_patch_list['still_end']['line_number'] = {}
  extended_SD_power_patch_list['still_end']['line_number']['BTC-7E'] = 43
  extended_SD_power_patch_list['still_end']['line_number']['BTC-8E'] = 43
  extended_SD_power_patch_list['still_end']['line_number']['BTC-7E-HP4'] = 46
  extended_SD_power_patch_list['still_end']['line_number']['BTC-8E-HP4'] = 46
  extended_SD_power_patch_list['still_end']['line_number']['BTC-7E-HP5'] = 51
  extended_SD_power_patch_list['still_end']['line_number']['BTC-8E-HP5'] = 52
  extended_SD_power_patch_list['still_end']['start_offset'] = {}
  extended_SD_power_patch_list['still_end']['start_offset']['BTC-7E']     = 0x0125b28
  extended_SD_power_patch_list['still_end']['start_offset']['BTC-8E']     = 0x0125ee0
  extended_SD_power_patch_list['still_end']['start_offset']['BTC-7E-HP4'] = 0x0121aec
  extended_SD_power_patch_list['still_end']['start_offset']['BTC-8E-HP4'] = 0x012203c
  extended_SD_power_patch_list['still_end']['start_offset']['BTC-7E-HP5'] = 0x0104fcc
  extended_SD_power_patch_list['still_end']['start_offset']['BTC-8E-HP5'] = 0x0105094
  extended_SD_power_patch_list['still_end']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
  extended_SD_power_patch_list['still_end']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
  # in HceTaskStillBurst_End()
  # line 39
  extended_SD_power_patch_list['still_burst_end'] = {}
  extended_SD_power_patch_list['still_burst_end']['function'] = 'HceTaskStillBurst_End'
  extended_SD_power_patch_list['still_burst_end']['line_number'] = {}
  extended_SD_power_patch_list['still_burst_end']['line_number']['BTC-7E'] = 39
  extended_SD_power_patch_list['still_burst_end']['line_number']['BTC-8E'] = 39
  extended_SD_power_patch_list['still_burst_end']['line_number']['BTC-7E-HP4'] = 39
  extended_SD_power_patch_list['still_burst_end']['line_number']['BTC-8E-HP4'] = 39
  extended_SD_power_patch_list['still_burst_end']['line_number']['BTC-7E-HP5'] = 44
  extended_SD_power_patch_list['still_burst_end']['line_number']['BTC-8E-HP5'] = 44
  extended_SD_power_patch_list['still_burst_end']['start_offset'] = {}
  extended_SD_power_patch_list['still_burst_end']['start_offset']['BTC-7E']     = 0x0127540
  extended_SD_power_patch_list['still_burst_end']['start_offset']['BTC-8E']     = 0x01278f0
  extended_SD_power_patch_list['still_burst_end']['start_offset']['BTC-7E-HP4'] = 0x0123c00
  extended_SD_power_patch_list['still_burst_end']['start_offset']['BTC-8E-HP4'] = 0x0124148
  extended_SD_power_patch_list['still_burst_end']['start_offset']['BTC-7E-HP5'] = 0x010705c
  extended_SD_power_patch_list['still_burst_end']['start_offset']['BTC-8E-HP5'] = 0x010711c
  extended_SD_power_patch_list['still_burst_end']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
  extended_SD_power_patch_list['still_burst_end']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'
  # in HceTaskTimeLapse_WaitMountSD()
  # line 12
  extended_SD_power_patch_list['timelapse_sd'] = {}
  extended_SD_power_patch_list['timelapse_sd']['function'] = 'TaskTimeLapse_task10_WaitMountSD'
  extended_SD_power_patch_list['timelapse_sd']['line_number'] = {}
  extended_SD_power_patch_list['timelapse_sd']['line_number']['BTC-7E'] = 12
  extended_SD_power_patch_list['timelapse_sd']['line_number']['BTC-8E'] = 12
  extended_SD_power_patch_list['timelapse_sd']['line_number']['BTC-7E-HP4'] = 12
  extended_SD_power_patch_list['timelapse_sd']['line_number']['BTC-8E-HP4'] = 12
  extended_SD_power_patch_list['timelapse_sd']['line_number']['BTC-7E-HP5'] = 12
  extended_SD_power_patch_list['timelapse_sd']['line_number']['BTC-8E-HP5'] = 12
  extended_SD_power_patch_list['timelapse_sd']['start_offset'] = {}
  extended_SD_power_patch_list['timelapse_sd']['start_offset']['BTC-7E'] = 0x0129c44
  extended_SD_power_patch_list['timelapse_sd']['start_offset']['BTC-8E'] = 0x0129fe4
  extended_SD_power_patch_list['timelapse_sd']['start_offset']['BTC-7E-HP4'] = 0x01262f8
  extended_SD_power_patch_list['timelapse_sd']['start_offset']['BTC-8E-HP4'] = 0x0126830
  extended_SD_power_patch_list['timelapse_sd']['start_offset']['BTC-7E-HP5'] = 0x0109784
  extended_SD_power_patch_list['timelapse_sd']['start_offset']['BTC-8E-HP5'] = 0x0109834
  extended_SD_power_patch_list['timelapse_sd']['change_from_jump'] = 'jal.get_cold_item_sd_management_p'
  extended_SD_power_patch_list['timelapse_sd']['change_to_jump']   = 'jal.evsd_get_cold_item_sd_management_p'

## Set IR Flash Power -- Off

ir_flash_power_patch_list = {}


# set_ir_led_power_pwm
ir_flash_power_patch_list['set_ir_led_power_pwm'] = {}
ir_flash_power_patch_list['set_ir_led_power_pwm']['function'] = 'setIRLedOn'
ir_flash_power_patch_list['set_ir_led_power_pwm']['line_number'] = {}
ir_flash_power_patch_list['set_ir_led_power_pwm']['line_number']['BTC-7A'] = 7
ir_flash_power_patch_list['set_ir_led_power_pwm']['line_number']['BTC-7E'] = 7
ir_flash_power_patch_list['set_ir_led_power_pwm']['line_number']['BTC-8E'] = 7
ir_flash_power_patch_list['set_ir_led_power_pwm']['line_number']['BTC-7E-HP4'] = 7
ir_flash_power_patch_list['set_ir_led_power_pwm']['line_number']['BTC-8E-HP4'] = 7
ir_flash_power_patch_list['set_ir_led_power_pwm']['line_number']['BTC-7E-HP5'] = 8
ir_flash_power_patch_list['set_ir_led_power_pwm']['line_number']['BTC-8E-HP5'] = 8
ir_flash_power_patch_list['set_ir_led_power_pwm']['start_offset'] = {}
ir_flash_power_patch_list['set_ir_led_power_pwm']['start_offset']['BTC-7A'] = 0x0111858
ir_flash_power_patch_list['set_ir_led_power_pwm']['start_offset']['BTC-7E'] = 0x0111858
ir_flash_power_patch_list['set_ir_led_power_pwm']['start_offset']['BTC-8E'] = 0x0111ad0
ir_flash_power_patch_list['set_ir_led_power_pwm']['start_offset']['BTC-7E-HP4'] = 0x005e130
ir_flash_power_patch_list['set_ir_led_power_pwm']['start_offset']['BTC-8E-HP4'] = 0x005e100
ir_flash_power_patch_list['set_ir_led_power_pwm']['start_offset']['BTC-7E-HP5'] = 0x005e3d4
ir_flash_power_patch_list['set_ir_led_power_pwm']['start_offset']['BTC-8E-HP5'] = 0x005e3a4
ir_flash_power_patch_list['set_ir_led_power_pwm']['change_from_jump'] = 'jal.power_on_IR_LED'
ir_flash_power_patch_list['set_ir_led_power_pwm']['change_to_jump']   = 'jal.ifm_power_on_IR_LED'


# power_on_IR_LED()
ir_flash_power_patch_list['power_on_IR_LED'] = {}
ir_flash_power_patch_list['power_on_IR_LED']['function'] = 'set_IRLedOn_PweLvl_protected'
ir_flash_power_patch_list['power_on_IR_LED']['line_number'] = {}
ir_flash_power_patch_list['power_on_IR_LED']['line_number']['BTC-7A'] = 11
ir_flash_power_patch_list['power_on_IR_LED']['line_number']['BTC-7E'] = 11
ir_flash_power_patch_list['power_on_IR_LED']['line_number']['BTC-8E'] = 11
ir_flash_power_patch_list['power_on_IR_LED']['line_number']['BTC-7E-HP4'] = 11
ir_flash_power_patch_list['power_on_IR_LED']['line_number']['BTC-8E-HP4'] = 11
ir_flash_power_patch_list['power_on_IR_LED']['line_number']['BTC-7E-HP5'] = 11
ir_flash_power_patch_list['power_on_IR_LED']['line_number']['BTC-8E-HP5'] = 15
ir_flash_power_patch_list['power_on_IR_LED']['start_offset'] = {}
ir_flash_power_patch_list['power_on_IR_LED']['start_offset']['BTC-7A'] = 0x01119e4
ir_flash_power_patch_list['power_on_IR_LED']['start_offset']['BTC-7E'] = 0x01119e4
ir_flash_power_patch_list['power_on_IR_LED']['start_offset']['BTC-8E'] = 0x0111c5c
ir_flash_power_patch_list['power_on_IR_LED']['start_offset']['BTC-7E-HP4'] = 0x005e2bc
ir_flash_power_patch_list['power_on_IR_LED']['start_offset']['BTC-8E-HP4'] = 0x005e28c
ir_flash_power_patch_list['power_on_IR_LED']['start_offset']['BTC-7E-HP5'] = 0x005e56c
ir_flash_power_patch_list['power_on_IR_LED']['start_offset']['BTC-8E-HP5'] = 0x005e53c
ir_flash_power_patch_list['power_on_IR_LED']['change_from_jump'] = 'jal.power_on_IR_LED'
ir_flash_power_patch_list['power_on_IR_LED']['change_to_jump']   = 'jal.ifm_power_on_IR_LED'

# Custom Date/Time Menu formats
cdt_menu_patch_list = {}
# replace call to  handleSetTimeMenu in g_HceTaskMenuMultiItem_fsm_function_array
cdt_menu_patch_list['handle_set_time_menu'] = {}
cdt_menu_patch_list['handle_set_time_menu']['function'] = 'g_HceTaskMenuMultiItem_fsm_function_array'
cdt_menu_patch_list['handle_set_time_menu']['line_number'] = {}
cdt_menu_patch_list['handle_set_time_menu']['line_number']['BTC-7A'] = 5 
cdt_menu_patch_list['handle_set_time_menu']['line_number']['BTC-7E'] = 5
cdt_menu_patch_list['handle_set_time_menu']['line_number']['BTC-8E'] = 5
cdt_menu_patch_list['handle_set_time_menu']['line_number']['BTC-7E-HP4'] = 5
cdt_menu_patch_list['handle_set_time_menu']['line_number']['BTC-8E-HP4'] = 5
cdt_menu_patch_list['handle_set_time_menu']['line_number']['BTC-7E-HP5'] = 5
cdt_menu_patch_list['handle_set_time_menu']['line_number']['BTC-8E-HP5'] = 5
cdt_menu_patch_list['handle_set_time_menu']['start_offset'] = {}
cdt_menu_patch_list['handle_set_time_menu']['start_offset']['BTC-7A'] = 0x0355290
cdt_menu_patch_list['handle_set_time_menu']['start_offset']['BTC-7E'] = 0x0355290
cdt_menu_patch_list['handle_set_time_menu']['start_offset']['BTC-8E'] = 0x03552e8
cdt_menu_patch_list['handle_set_time_menu']['start_offset']['BTC-7E-HP4'] = 0x03582e8
cdt_menu_patch_list['handle_set_time_menu']['start_offset']['BTC-8E-HP4'] = 0x035c518
cdt_menu_patch_list['handle_set_time_menu']['start_offset']['BTC-7E-HP5'] = 0x02cdd58
cdt_menu_patch_list['handle_set_time_menu']['start_offset']['BTC-8E-HP5'] = 0x02cff18
cdt_menu_patch_list['handle_set_time_menu']['change_from_ptr'] = 'handleSetTimeMenu'
cdt_menu_patch_list['handle_set_time_menu']['change_to_ptr']   = 'cdt_handleSetTimeMenu'

cdt_menu_patch_list['cdt_btc_strcpy'] = {}
cdt_menu_patch_list['cdt_btc_strcpy']['function'] = 'draw_set_time_screen'
cdt_menu_patch_list['cdt_btc_strcpy']['line_number'] = {}
cdt_menu_patch_list['cdt_btc_strcpy']['line_number']['BTC-7A'] = 135
cdt_menu_patch_list['cdt_btc_strcpy']['line_number']['BTC-7E'] = 162
cdt_menu_patch_list['cdt_btc_strcpy']['line_number']['BTC-8E'] = 126
cdt_menu_patch_list['cdt_btc_strcpy']['line_number']['BTC-7E-HP4'] = 124
cdt_menu_patch_list['cdt_btc_strcpy']['line_number']['BTC-8E-HP4'] = 124
cdt_menu_patch_list['cdt_btc_strcpy']['line_number']['BTC-7E-HP5'] = 131 
cdt_menu_patch_list['cdt_btc_strcpy']['line_number']['BTC-8E-HP5'] = 124
cdt_menu_patch_list['cdt_btc_strcpy']['start_offset'] = {}
cdt_menu_patch_list['cdt_btc_strcpy']['start_offset']['BTC-7A'] = 0x0135550
cdt_menu_patch_list['cdt_btc_strcpy']['start_offset']['BTC-7E'] = 0x0135550
cdt_menu_patch_list['cdt_btc_strcpy']['start_offset']['BTC-8E'] = 0x013614c
cdt_menu_patch_list['cdt_btc_strcpy']['start_offset']['BTC-7E-HP4'] = 0x0131e20
cdt_menu_patch_list['cdt_btc_strcpy']['start_offset']['BTC-8E-HP4'] = 0x0134950
cdt_menu_patch_list['cdt_btc_strcpy']['start_offset']['BTC-7E-HP5'] = 0x0114e60
cdt_menu_patch_list['cdt_btc_strcpy']['start_offset']['BTC-8E-HP5'] = 0x01157b8
cdt_menu_patch_list['cdt_btc_strcpy']['change_from_jump'] = 'jal.btc_strcpy'
cdt_menu_patch_list['cdt_btc_strcpy']['change_to_jump']   = 'jal.cdt_btc_strcpy'



## Patches to fix access to the pressure/temperature sensor
##   2023-09-17 -- my first hypothesis is that it's somehow at the
##                 wrong I2C address

pt_patch_list = {}

# read in Pressure_sensor_init()
pt_patch_list['pressure_sensor_init'] = {}
pt_patch_list['pressure_sensor_init']['function'] = 'Pressure_sensor_init'
pt_patch_list['pressure_sensor_init']['line_number'] = {}
pt_patch_list['pressure_sensor_init']['line_number']['BTC-8E'] = 33
pt_patch_list['pressure_sensor_init']['start_offset'] = {}
pt_patch_list['pressure_sensor_init']['start_offset']['BTC-8E'] = 0x012e220
pt_patch_list['pressure_sensor_init']['change_from_bytes'] = bytes([0xee,0x00,0x04,0x24])
pt_patch_list['pressure_sensor_init']['change_to_bytes']   = bytes([0xec,0x00,0x04,0x24])

## read in Pressure_sensor_getReading'
pt_patch_list['ps_get_reading'] = {}
pt_patch_list['ps_get_reading']['function'] = 'Pressure_sensor_getReading'
pt_patch_list['ps_get_reading']['line_number'] = {}
pt_patch_list['ps_get_reading']['line_number']['BTC-8E'] = 41
pt_patch_list['ps_get_reading']['start_offset'] = {}
pt_patch_list['ps_get_reading']['start_offset']['BTC-8E'] = 0x012de94
pt_patch_list['ps_get_reading']['change_from_bytes'] = bytes([0xee,0x00,0x04,0x24])
pt_patch_list['ps_get_reading']['change_to_bytes']   = bytes([0xec,0x00,0x04,0x24])

## read in read_pressure_temperature_device'
pt_patch_list['ps_read_pressure'] = {}
pt_patch_list['ps_read_pressure']['function'] = 'read_pressure_temperature_device'
pt_patch_list['ps_read_pressure']['line_number'] = {}
pt_patch_list['ps_read_pressure']['line_number']['BTC-8E'] = 7
pt_patch_list['ps_read_pressure']['start_offset'] = {}
pt_patch_list['ps_read_pressure']['start_offset']['BTC-8E'] = 0x012dd9c
pt_patch_list['ps_read_pressure']['change_from_bytes'] = bytes([0xee,0x00,0x04,0x24])
pt_patch_list['ps_read_pressure']['change_to_bytes']   = bytes([0xec,0x00,0x04,0x24])

## write in write_pressure_temperature_sensor
pt_patch_list['write_pt_sensor'] = {}
pt_patch_list['write_pt_sensor']['function'] = 'write_pressure_temperature_sensor'
pt_patch_list['write_pt_sensor']['line_number'] = {}
pt_patch_list['write_pt_sensor']['line_number']['BTC-8E'] = 10
pt_patch_list['write_pt_sensor']['start_offset'] = {}
pt_patch_list['write_pt_sensor']['start_offset']['BTC-8E'] = 0x012dcb0
pt_patch_list['write_pt_sensor']['change_from_bytes'] = bytes([0xee,0x00,0x04,0x24])
pt_patch_list['write_pt_sensor']['change_to_bytes']   = bytes([0xec,0x00,0x04,0x24])

## write in write_pressure_temperature_sensor
pt_patch_list['write_pt_sensor_wait'] = {}
pt_patch_list['write_pt_sensor_wait']['function'] = 'write_pressure_temperature_sensor_wait'
pt_patch_list['write_pt_sensor_wait']['line_number'] = {}
pt_patch_list['write_pt_sensor_wait']['line_number']['BTC-8E'] = 7
pt_patch_list['write_pt_sensor_wait']['start_offset'] = {}
pt_patch_list['write_pt_sensor_wait']['start_offset']['BTC-8E'] = 0x012dd54
pt_patch_list['write_pt_sensor_wait']['change_from_bytes'] = bytes([0xee,0x00,0x04,0x24])
pt_patch_list['write_pt_sensor_wait']['change_to_bytes']   = bytes([0xec,0x00,0x04,0x24])

## in Pressure_sensor_init() -- select the "external" temp sensor 
##    Select external sensor, and lower sample rate in all cases
pt_patch_list['pt_ext_temp_sensor'] = {}
pt_patch_list['pt_ext_temp_sensor']['function'] = 'Pressure_sensor_init'
pt_patch_list['pt_ext_temp_sensor']['line_number'] = {}
pt_patch_list['pt_ext_temp_sensor']['line_number']['BTC-8E'] = 83
pt_patch_list['pt_ext_temp_sensor']['start_offset'] = {}
pt_patch_list['pt_ext_temp_sensor']['start_offset']['BTC-8E'] = 0x012e4ac
pt_patch_list['pt_ext_temp_sensor']['change_from_bytes'] = bytes([0x31,0x00,0x05,0x24])
pt_patch_list['pt_ext_temp_sensor']['change_to_bytes']   = bytes([0xb1,0x00,0x05,0x24])


## Debug -- in update_global_pressure_temperature()
# pt_patch_list['pt_get_sensor'] = {}
# pt_patch_list['pt_get_sensor']['function'] = 'update_global_pressure_temperature'
# pt_patch_list['pt_get_sensor']['line_number'] = {}
# pt_patch_list['pt_get_sensor']['line_number']['BTC-8E'] = 10
# pt_patch_list['pt_get_sensor']['start_offset'] = {}
# pt_patch_list['pt_get_sensor']['start_offset']['BTC-8E'] = 0x010db18
# pt_patch_list['pt_get_sensor']['change_from_jump'] = 'j.Pressure_sensor_getReading'
# pt_patch_list['pt_get_sensor']['change_to_jump']   = 'j.cr_Pressure_sensor_getReading'


## Debug -- in g_pressure_temperature_functions_B
# pt_patch_list['pt_get_sensor_hp4'] = {}
# pt_patch_list['pt_get_sensor_hp4']['function'] = 'g_pressure_temperature_functions_B'
# pt_patch_list['pt_get_sensor_hp4']['line_number'] = {}
# pt_patch_list['pt_get_sensor_hp4']['line_number']['BTC-8E-HP4'] = 1
# pt_patch_list['pt_get_sensor_hp4']['start_offset'] = {}
# pt_patch_list['pt_get_sensor_hp4']['start_offset']['BTC-8E-HP4'] = 0x035a760
# pt_patch_list['pt_get_sensor_hp4']['change_from_ptr'] = 'Pressure_sensor_getReading'
# pt_patch_list['pt_get_sensor_hp4']['change_to_ptr']   = 'cr_Pressure_sensor_getReading'

## Debug -- in Pressure_sensor_init()
# pt_patch_list['pt_pressure_sensor_init'] = {}
# pt_patch_list['pt_pressure_sensor_init']['function'] = 'Pressure_sensor_init'
# pt_patch_list['pt_pressure_sensor_init']['line_number'] = {}
# pt_patch_list['pt_pressure_sensor_init']['line_number']['BTC-8E'] = 86
# pt_patch_list['pt_pressure_sensor_init']['line_number']['BTC-8E-HP4'] = 88
# pt_patch_list['pt_pressure_sensor_init']['start_offset'] = {}
# pt_patch_list['pt_pressure_sensor_init']['start_offset']['BTC-8E'] = 0x012e4c0
# pt_patch_list['pt_pressure_sensor_init']['start_offset']['BTC-8E-HP4'] = 0x012b764
# pt_patch_list['pt_pressure_sensor_init']['change_from_jump'] = 'jal.log_printf'
# pt_patch_list['pt_pressure_sensor_init']['change_to_jump']   = 'jal.cr_log_printf'

##
## Reduce SD Clock Speed Patches
rsc_patch_list = {}

# Intercept initialize_sd_card_to_data to always slow down SD card
rsc_patch_list['init_sd_to_data0'] = {}
rsc_patch_list['init_sd_to_data0']['function'] = 'initialize_sd_card_to_data'
rsc_patch_list['init_sd_to_data0']['line_number'] = {}
rsc_patch_list['init_sd_to_data0']['line_number']['BTC-7A'] = 267 
rsc_patch_list['init_sd_to_data0']['line_number']['BTC-7E'] = 267 
rsc_patch_list['init_sd_to_data0']['line_number']['BTC-8E'] = 269
rsc_patch_list['init_sd_to_data0']['line_number']['BTC-7E-HP4'] = 273
rsc_patch_list['init_sd_to_data0']['line_number']['BTC-8E-HP4'] = 270 
rsc_patch_list['init_sd_to_data0']['line_number']['BTC-7E-HP5'] = 281
rsc_patch_list['init_sd_to_data0']['line_number']['BTC-8E-HP5'] = 276
rsc_patch_list['init_sd_to_data0']['start_offset'] = {}
rsc_patch_list['init_sd_to_data0']['start_offset']['BTC-7A'] = 0x00630f4
rsc_patch_list['init_sd_to_data0']['start_offset']['BTC-7E'] = 0x00630f4
rsc_patch_list['init_sd_to_data0']['start_offset']['BTC-8E'] = 0x00630f4
rsc_patch_list['init_sd_to_data0']['start_offset']['BTC-7E-HP4'] = 0x02fa268
rsc_patch_list['init_sd_to_data0']['start_offset']['BTC-8E-HP4'] = 0x02fcd98
rsc_patch_list['init_sd_to_data0']['start_offset']['BTC-7E-HP5'] = 0x0272a04
rsc_patch_list['init_sd_to_data0']['start_offset']['BTC-8E-HP5'] = 0x02739e4
rsc_patch_list['init_sd_to_data0']['change_from_bytes'] = bytes([0x04,0x00,0x11,0x24])
rsc_patch_list['init_sd_to_data0']['change_to_bytes']   = bytes([0x00,0x00,0x11,0x24])

# second in init_sd_to_data
rsc_patch_list['init_sd_to_data1'] = {}
rsc_patch_list['init_sd_to_data1']['function'] = 'initialize_sd_card_to_data'
rsc_patch_list['init_sd_to_data1']['line_number'] = {}
rsc_patch_list['init_sd_to_data1']['line_number']['BTC-7A'] = 659
rsc_patch_list['init_sd_to_data1']['line_number']['BTC-7E'] = 659
rsc_patch_list['init_sd_to_data1']['line_number']['BTC-8E'] = 663
rsc_patch_list['init_sd_to_data1']['line_number']['BTC-7E-HP4'] = 666
rsc_patch_list['init_sd_to_data1']['line_number']['BTC-8E-HP4'] = 663
rsc_patch_list['init_sd_to_data1']['line_number']['BTC-7E-HP5'] = 688
rsc_patch_list['init_sd_to_data1']['line_number']['BTC-8E-HP5'] = 666
rsc_patch_list['init_sd_to_data1']['start_offset'] = {}
rsc_patch_list['init_sd_to_data1']['start_offset']['BTC-7A'] = 0x0062e40
rsc_patch_list['init_sd_to_data1']['start_offset']['BTC-7E'] = 0x0062e40
rsc_patch_list['init_sd_to_data1']['start_offset']['BTC-8E'] = 0x0062e40
rsc_patch_list['init_sd_to_data1']['start_offset']['BTC-7E-HP4'] = 0x02f9fb4
rsc_patch_list['init_sd_to_data1']['start_offset']['BTC-8E-HP4'] = 0x02fcae4
rsc_patch_list['init_sd_to_data1']['start_offset']['BTC-7E-HP5'] = 0x0272750
rsc_patch_list['init_sd_to_data1']['start_offset']['BTC-8E-HP5'] = 0x0273730
rsc_patch_list['init_sd_to_data1']['change_from_bytes'] = bytes([0x07,0x00,0x11,0x24])
rsc_patch_list['init_sd_to_data1']['change_to_bytes']   = bytes([0x00,0x00,0x11,0x24])

# third in init_sd_to_data
rsc_patch_list['init_sd_to_data2'] = {}
rsc_patch_list['init_sd_to_data2']['function'] = 'initialize_sd_card_to_data'
rsc_patch_list['init_sd_to_data2']['line_number'] = {}
rsc_patch_list['init_sd_to_data2']['line_number']['BTC-7A'] = 663
rsc_patch_list['init_sd_to_data2']['line_number']['BTC-7E'] = 663
rsc_patch_list['init_sd_to_data2']['line_number']['BTC-8E'] = 667
rsc_patch_list['init_sd_to_data2']['line_number']['BTC-7E-HP4'] = 670
rsc_patch_list['init_sd_to_data2']['line_number']['BTC-8E-HP4'] = 667
rsc_patch_list['init_sd_to_data2']['line_number']['BTC-7E-HP5'] = 686
rsc_patch_list['init_sd_to_data2']['line_number']['BTC-8E-HP5'] = 670
rsc_patch_list['init_sd_to_data2']['start_offset'] = {}
rsc_patch_list['init_sd_to_data2']['start_offset']['BTC-7A'] = 0x0062e54
rsc_patch_list['init_sd_to_data2']['start_offset']['BTC-7E'] = 0x0062e54
rsc_patch_list['init_sd_to_data2']['start_offset']['BTC-8E'] = 0x0062e54
rsc_patch_list['init_sd_to_data2']['start_offset']['BTC-7E-HP4'] = 0x02f9fc8
rsc_patch_list['init_sd_to_data2']['start_offset']['BTC-8E-HP4'] = 0x02fcaf8
rsc_patch_list['init_sd_to_data2']['start_offset']['BTC-7E-HP5'] = 0x0272764
rsc_patch_list['init_sd_to_data2']['start_offset']['BTC-8E-HP5'] = 0x0273744
rsc_patch_list['init_sd_to_data2']['change_from_bytes'] = bytes([0x04,0x00,0x11,0x24])
rsc_patch_list['init_sd_to_data2']['change_to_bytes']   = bytes([0x00,0x00,0x11,0x24])

# Intercept reduce_sd_clock to always slow down SD card
rsc_patch_list['reduce_sd_clock'] = {}
rsc_patch_list['reduce_sd_clock']['function'] = 'reduce_sd_clock'
rsc_patch_list['reduce_sd_clock']['line_number'] = {}
rsc_patch_list['reduce_sd_clock']['line_number']['BTC-7A'] = 32
rsc_patch_list['reduce_sd_clock']['line_number']['BTC-7E'] = 32
rsc_patch_list['reduce_sd_clock']['line_number']['BTC-8E'] = 32
rsc_patch_list['reduce_sd_clock']['line_number']['BTC-7E-HP4'] = 32
rsc_patch_list['reduce_sd_clock']['line_number']['BTC-8E-HP4'] = 32 
rsc_patch_list['reduce_sd_clock']['line_number']['BTC-7E-HP5'] = 32
rsc_patch_list['reduce_sd_clock']['line_number']['BTC-8E-HP5'] = 32
rsc_patch_list['reduce_sd_clock']['start_offset'] = {}
rsc_patch_list['reduce_sd_clock']['start_offset']['BTC-7A'] = 0x0060008
rsc_patch_list['reduce_sd_clock']['start_offset']['BTC-7E'] = 0x0060008
rsc_patch_list['reduce_sd_clock']['start_offset']['BTC-8E'] = 0x0060008
rsc_patch_list['reduce_sd_clock']['start_offset']['BTC-7E-HP4'] = 0x02f717c
rsc_patch_list['reduce_sd_clock']['start_offset']['BTC-8E-HP4'] = 0x02f9cac
rsc_patch_list['reduce_sd_clock']['start_offset']['BTC-7E-HP5'] = 0x026f918
rsc_patch_list['reduce_sd_clock']['start_offset']['BTC-8E-HP5'] = 0x02708f8
rsc_patch_list['reduce_sd_clock']['change_from_bytes'] = bytes([0x04,0x00,0x05,0x24])
rsc_patch_list['reduce_sd_clock']['change_to_bytes']   = bytes([0x00,0x00,0x05,0x24])


# Custom Setting Store/restore

enum_icon_no_icon = {}
enum_icon_no_icon['BTC-7A'] = 31
enum_icon_no_icon['BTC-7E'] = 31
enum_icon_no_icon['BTC-8E'] = 31
enum_icon_no_icon['BTC-7E-HP4'] = 31
enum_icon_no_icon['BTC-8E-HP4'] = 31
enum_icon_no_icon['BTC-7E-HP5'] = 32
enum_icon_no_icon['BTC-8E-HP5'] = 32

# Text IDs are platform specific (sometimes)

sst_no_id = {}
sst_no_id['BTC-7A'] = 10
sst_no_id['BTC-7E'] = 10
sst_no_id['BTC-8E'] = 10
sst_no_id['BTC-7E-HP4'] = 10
sst_no_id['BTC-8E-HP4'] = 10
sst_no_id['BTC-7E-HP5'] = 10
sst_no_id['BTC-8E-HP5'] = 10

sst_yes_id = {}
sst_yes_id['BTC-7A'] = 11
sst_yes_id['BTC-7E'] = 11
sst_yes_id['BTC-8E'] = 11
sst_yes_id['BTC-7E-HP4'] = 11
sst_yes_id['BTC-8E-HP4'] = 11
sst_yes_id['BTC-7E-HP5'] = 11
sst_yes_id['BTC-8E-HP5'] = 11

sst_5_sp_secs_id = {}
sst_5_sp_secs_id['BTC-7A'] = 13
sst_5_sp_secs_id['BTC-7E'] = 13
sst_5_sp_secs_id['BTC-8E'] = 13
sst_5_sp_secs_id['BTC-7E-HP4'] = 13
sst_5_sp_secs_id['BTC-8E-HP4'] = 13
sst_5_sp_secs_id['BTC-7E-HP5'] = 13
sst_5_sp_secs_id['BTC-8E-HP5'] = 13

sst_10_sp_secs_id = {}
sst_10_sp_secs_id['BTC-7A'] = 14
sst_10_sp_secs_id['BTC-7E'] = 14
sst_10_sp_secs_id['BTC-8E'] = 14
sst_10_sp_secs_id['BTC-7E-HP4'] = 14
sst_10_sp_secs_id['BTC-8E-HP4'] = 14
sst_10_sp_secs_id['BTC-7E-HP5'] = 14
sst_10_sp_secs_id['BTC-8E-HP5'] = 14

sst_default_sp_settings_id = {}
sst_default_sp_settings_id['BTC-7A'] = 59
sst_default_sp_settings_id['BTC-7E'] = 59
sst_default_sp_settings_id['BTC-8E'] = 59
sst_default_sp_settings_id['BTC-7E-HP4'] = 61
sst_default_sp_settings_id['BTC-8E-HP4'] = 61
sst_default_sp_settings_id['BTC-7E-HP5'] = 62
sst_default_sp_settings_id['BTC-8E-HP5'] = 62

sst_factory_id = {}
sst_factory_id['BTC-7A'] = 196
sst_factory_id['BTC-7E'] = 196
sst_factory_id['BTC-8E'] = 196
sst_factory_id['BTC-7E-HP4'] = 199
sst_factory_id['BTC-8E-HP4'] = 199
sst_factory_id['BTC-7E-HP5'] = 205
sst_factory_id['BTC-8E-HP5'] = 205

sst_custom_id = {}
sst_custom_id['BTC-7A'] = 197
sst_custom_id['BTC-7E'] = 197
sst_custom_id['BTC-8E'] = 197
sst_custom_id['BTC-7E-HP4'] = 200
sst_custom_id['BTC-8E-HP4'] = 200
sst_custom_id['BTC-7E-HP5'] = 206
sst_custom_id['BTC-8E-HP5'] = 206

sst_save_sp_custom_id = {}
sst_save_sp_custom_id['BTC-7A'] = 198
sst_save_sp_custom_id['BTC-7E'] = 198
sst_save_sp_custom_id['BTC-8E'] = 198
sst_save_sp_custom_id['BTC-7E-HP4'] = 201
sst_save_sp_custom_id['BTC-8E-HP4'] = 201
sst_save_sp_custom_id['BTC-7E-HP5'] = 207
sst_save_sp_custom_id['BTC-8E-HP5'] = 207


## Custom Settings Patches
cst_menu_patch_list = {}

# replace call to  handleSetTimeMenu in g_HceTaskMenuMultiItem_fsm_function_array
cst_menu_patch_list['handle_restore_default_menu'] = {}
cst_menu_patch_list['handle_restore_default_menu']['function'] = 'g_HceTaskMenuMultiItem_fsm_function_array'
cst_menu_patch_list['handle_restore_default_menu']['line_number'] = {}
cst_menu_patch_list['handle_restore_default_menu']['line_number']['BTC-7A'] = 20
cst_menu_patch_list['handle_restore_default_menu']['line_number']['BTC-7E'] = 20
cst_menu_patch_list['handle_restore_default_menu']['line_number']['BTC-8E'] = 20
cst_menu_patch_list['handle_restore_default_menu']['line_number']['BTC-7E-HP4'] = 20
cst_menu_patch_list['handle_restore_default_menu']['line_number']['BTC-8E-HP4'] = 20
cst_menu_patch_list['handle_restore_default_menu']['line_number']['BTC-7E-HP5'] = 20
cst_menu_patch_list['handle_restore_default_menu']['line_number']['BTC-8E-HP5'] = 20
cst_menu_patch_list['handle_restore_default_menu']['start_offset'] = {}
cst_menu_patch_list['handle_restore_default_menu']['start_offset']['BTC-7A'] = 0x03552c8
cst_menu_patch_list['handle_restore_default_menu']['start_offset']['BTC-7E'] = 0x03552c8
cst_menu_patch_list['handle_restore_default_menu']['start_offset']['BTC-8E'] = 0x0355320
cst_menu_patch_list['handle_restore_default_menu']['start_offset']['BTC-7E-HP4'] = 0x0358320
cst_menu_patch_list['handle_restore_default_menu']['start_offset']['BTC-8E-HP4'] = 0x035c550
cst_menu_patch_list['handle_restore_default_menu']['start_offset']['BTC-7E-HP5'] = 0x02cdd94
cst_menu_patch_list['handle_restore_default_menu']['start_offset']['BTC-8E-HP5'] = 0x02cff54
cst_menu_patch_list['handle_restore_default_menu']['change_from_ptr'] = 'handleRestoreDefault_menu'
cst_menu_patch_list['handle_restore_default_menu']['change_to_ptr']   = 'cst_handleRestoreDefault_menu'

## Overwrite g_restore_default_menu to include a couple new entries
##    We need to use this data region because it is writable -- which we need to
##       be able to dynamically disable some menu options
##    It works because we've already replaced the next menu structure. 
cst_menu_patch_list['g_restore_default_menu'] = {}
cst_menu_patch_list['g_restore_default_menu']['function'] = 'g_restore_default_menu'
cst_menu_patch_list['g_restore_default_menu']['line_number'] = {}
cst_menu_patch_list['g_restore_default_menu']['line_number']['BTC-7A'] = 0
cst_menu_patch_list['g_restore_default_menu']['line_number']['BTC-7E'] = 0
cst_menu_patch_list['g_restore_default_menu']['line_number']['BTC-8E'] = 0
cst_menu_patch_list['g_restore_default_menu']['line_number']['BTC-7E-HP4'] = 0
cst_menu_patch_list['g_restore_default_menu']['line_number']['BTC-8E-HP4'] = 0
cst_menu_patch_list['g_restore_default_menu']['line_number']['BTC-7E-HP5'] = 0
cst_menu_patch_list['g_restore_default_menu']['line_number']['BTC-8E-HP5'] = 0
cst_menu_patch_list['g_restore_default_menu']['start_offset'] = {}
cst_menu_patch_list['g_restore_default_menu']['start_offset']['BTC-7E'] = 0x03b3c70
cst_menu_patch_list['g_restore_default_menu']['start_offset']['BTC-7A'] = 0x03b3c70
cst_menu_patch_list['g_restore_default_menu']['start_offset']['BTC-8E'] = 0x03b3e70
cst_menu_patch_list['g_restore_default_menu']['start_offset']['BTC-7E-HP4'] = 0x03b9110 
cst_menu_patch_list['g_restore_default_menu']['start_offset']['BTC-8E-HP4'] = 0x03bd710
cst_menu_patch_list['g_restore_default_menu']['start_offset']['BTC-7E-HP5'] = 0x0314cb4
cst_menu_patch_list['g_restore_default_menu']['start_offset']['BTC-8E-HP5'] = 0x0316eb4
cst_menu_patch_list['g_restore_default_menu']['change_from_bytes'] = {}
cst_menu_patch_list['g_restore_default_menu']['change_from_bytes']['BTC-7A'] = bytes([enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu
									    sst_no_id['BTC-7A'],0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_yes_id['BTC-7A'],0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [2].icon_index
									    sst_default_sp_settings_id['BTC-7A'] ,0x00,0x00,0x00,   ## [2].text_id
    									    0x00,0x00,0x00,0x00,   ## [2].disable_item
    									    0x00,0x00,0x00,0x00,   ## [2].menu_increment
									    0x01,0x00,0x00,0x00,   ## [2].menu_selection
									    0x03,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [0].icon_index for g_timelapse_frequency_menu
									    sst_5_sp_secs_id['BTC-7A'], 0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_10_sp_secs_id['BTC-7A'], 0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    ]) 
cst_menu_patch_list['g_restore_default_menu']['change_from_bytes']['BTC-7E'] = bytes([enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu
									    sst_no_id['BTC-7E'],0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_yes_id['BTC-7E'],0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [2].icon_index
									    sst_default_sp_settings_id['BTC-7E'] ,0x00,0x00,0x00,   ## [2].text_id
    									    0x00,0x00,0x00,0x00,   ## [2].disable_item
    									    0x00,0x00,0x00,0x00,   ## [2].menu_increment
									    0x01,0x00,0x00,0x00,   ## [2].menu_selection
									    0x03,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [0].icon_index for g_timelapse_frequency_menu
									    sst_5_sp_secs_id['BTC-7E'], 0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_10_sp_secs_id['BTC-7E'], 0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    ])
cst_menu_patch_list['g_restore_default_menu']['change_from_bytes']['BTC-8E'] = bytes([enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu
									    sst_no_id['BTC-8E'],0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_yes_id['BTC-8E'],0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [2].icon_index
									    sst_default_sp_settings_id['BTC-8E'] ,0x00,0x00,0x00,   ## [2].text_id
    									    0x00,0x00,0x00,0x00,   ## [2].disable_item
    									    0x00,0x00,0x00,0x00,   ## [2].menu_increment
									    0x01,0x00,0x00,0x00,   ## [2].menu_selection
									    0x03,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [0].icon_index for g_timelapse_frequency_menu
									    sst_5_sp_secs_id['BTC-8E'], 0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_10_sp_secs_id['BTC-8E'], 0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    ])
cst_menu_patch_list['g_restore_default_menu']['change_from_bytes']['BTC-7E-HP4'] = bytes([enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu
									    sst_no_id['BTC-7E-HP4'],0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_yes_id['BTC-7E-HP4'],0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [2].icon_index
									    sst_default_sp_settings_id['BTC-7E-HP4'] ,0x00,0x00,0x00,   ## [2].text_id
    									    0x00,0x00,0x00,0x00,   ## [2].disable_item
    									    0x00,0x00,0x00,0x00,   ## [2].menu_increment
									    0x01,0x00,0x00,0x00,   ## [2].menu_selection
									    0x03,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [0].icon_index for g_timelapse_frequency_menu
									    sst_5_sp_secs_id['BTC-7E-HP4'], 0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_10_sp_secs_id['BTC-7E-HP4'], 0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    ])
cst_menu_patch_list['g_restore_default_menu']['change_from_bytes']['BTC-8E-HP4'] = bytes([enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu
									    sst_no_id['BTC-8E-HP4'],0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_yes_id['BTC-8E-HP4'],0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [2].icon_index
									    sst_default_sp_settings_id['BTC-8E-HP4'] ,0x00,0x00,0x00,   ## [2].text_id
    									    0x00,0x00,0x00,0x00,   ## [2].disable_item
    									    0x00,0x00,0x00,0x00,   ## [2].menu_increment
									    0x01,0x00,0x00,0x00,   ## [2].menu_selection
									    0x03,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [0].icon_index for g_timelapse_frequency_menu
									    sst_5_sp_secs_id['BTC-8E-HP4'], 0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_10_sp_secs_id['BTC-8E-HP4'], 0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    ])
###
cst_menu_patch_list['g_restore_default_menu']['change_from_bytes']['BTC-7E-HP5'] = bytes([enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu
									    sst_no_id['BTC-7E-HP5'],0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_yes_id['BTC-7E-HP5'],0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [2].icon_index
									    sst_default_sp_settings_id['BTC-7E-HP5'] ,0x00,0x00,0x00,   ## [2].text_id
    									    0x00,0x00,0x00,0x00,   ## [2].disable_item
    									    0x00,0x00,0x00,0x00,   ## [2].menu_increment
									    0x01,0x00,0x00,0x00,   ## [2].menu_selection
									    0x03,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [0].icon_index for g_timelapse_frequency_menu
									    sst_5_sp_secs_id['BTC-7E-HP5'], 0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_10_sp_secs_id['BTC-7E-HP5'], 0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    ])
cst_menu_patch_list['g_restore_default_menu']['change_from_bytes']['BTC-8E-HP5'] = bytes([enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu
									    sst_no_id['BTC-8E-HP5'],0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_yes_id['BTC-8E-HP5'],0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [2].icon_index
									    sst_default_sp_settings_id['BTC-8E-HP5'] ,0x00,0x00,0x00,   ## [2].text_id
    									    0x00,0x00,0x00,0x00,   ## [2].disable_item
    									    0x00,0x00,0x00,0x00,   ## [2].menu_increment
									    0x01,0x00,0x00,0x00,   ## [2].menu_selection
									    0x03,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [0].icon_index for g_timelapse_frequency_menu
									    sst_5_sp_secs_id['BTC-8E-HP5'], 0x00,0x00,0x00,   ## [0].text_id
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [1].icon_index
									    sst_10_sp_secs_id['BTC-8E-HP5'], 0x00,0x00,0x00,   ## [1].text_id
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x01,0x00,0x00,0x00,   ## [1].next_state_id
									    ])
###
cst_menu_patch_list['g_restore_default_menu']['change_to_bytes'] = {}
cst_menu_patch_list['g_restore_default_menu']['change_to_bytes']['BTC-7A']   = bytes([enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu "No"
									    sst_no_id['BTC-7A'],0x00,0x00,0x00,   ## [0].text_id  
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [1].icon_index "FACTORY"
									    sst_factory_id['BTC-7A'], 0x00,0x00,0x00,   ## [1].text_id 
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x02,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [2].icon_index   "CUSTOM"
									    sst_custom_id['BTC-7A'], 0x00,0x00,0x00,   ## [2].text_id 
    									    0x01,0x00,0x00,0x00,   ## [2].disable_item
    									    0x01,0x00,0x00,0x00,   ## [2].menu_increment
									    0x00,0x00,0x00,0x00,   ## [2].menu_selection
									    0x01,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [3].icon_index "SAVE CUSTOM"
									    sst_save_sp_custom_id['BTC-7A'], 0x00,0x00,0x00,   ## [3].text_id
    									    0x00,0x00,0x00,0x00,   ## [3].disable_item
    									    0x01,0x00,0x00,0x00,   ## [3].menu_increment
									    0x00,0x00,0x00,0x00,   ## [3].menu_selection
									    0x01,0x00,0x00,0x00,   ## [3].return_state_id
									    0x04,0x00,0x00,0x00,   ## [3].next_state_id
									    enum_icon_no_icon['BTC-7A'],0x00,0x00,0x00,   ## [4].icon_index "DEFAULT SETTINGS"
									    sst_default_sp_settings_id['BTC-7A'], 0x00,0x00,0x00,   ## [4].text_id
    									    0x00,0x00,0x00,0x00,   ## [4].disable_item
    									    0x00,0x00,0x00,0x00,   ## [4].menu_increment
									    0x01,0x00,0x00,0x00,   ## [4].menu_selection
									    0x03,0x00,0x00,0x00,   ## [4].return_state_id
									    0x03,0x00,0x00,0x00,   ## [4].next_state_id
									    ]) 
cst_menu_patch_list['g_restore_default_menu']['change_to_bytes']['BTC-7E']   = bytes([enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu "No"
									    sst_no_id['BTC-7E'],0x00,0x00,0x00,   ## [0].text_id  
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [1].icon_index "FACTORY"
									    sst_factory_id['BTC-7E'], 0x00,0x00,0x00,   ## [1].text_id 
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x02,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [2].icon_index   "CUSTOM"
									    sst_custom_id['BTC-7E'], 0x00,0x00,0x00,   ## [2].text_id 
    									    0x01,0x00,0x00,0x00,   ## [2].disable_item
    									    0x01,0x00,0x00,0x00,   ## [2].menu_increment
									    0x00,0x00,0x00,0x00,   ## [2].menu_selection
									    0x01,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [3].icon_index "SAVE CUSTOM"
									    sst_save_sp_custom_id['BTC-7E'], 0x00,0x00,0x00,   ## [3].text_id
    									    0x00,0x00,0x00,0x00,   ## [3].disable_item
    									    0x01,0x00,0x00,0x00,   ## [3].menu_increment
									    0x00,0x00,0x00,0x00,   ## [3].menu_selection
									    0x01,0x00,0x00,0x00,   ## [3].return_state_id
									    0x04,0x00,0x00,0x00,   ## [3].next_state_id
									    enum_icon_no_icon['BTC-7E'],0x00,0x00,0x00,   ## [4].icon_index "DEFAULT SETTINGS"
									    sst_default_sp_settings_id['BTC-7E'], 0x00,0x00,0x00,   ## [4].text_id
    									    0x00,0x00,0x00,0x00,   ## [4].disable_item
    									    0x00,0x00,0x00,0x00,   ## [4].menu_increment
									    0x01,0x00,0x00,0x00,   ## [4].menu_selection
									    0x03,0x00,0x00,0x00,   ## [4].return_state_id
									    0x03,0x00,0x00,0x00,   ## [4].next_state_id
									    ])
cst_menu_patch_list['g_restore_default_menu']['change_to_bytes']['BTC-8E']   = bytes([enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu "No"
									    sst_no_id['BTC-8E'],0x00,0x00,0x00,   ## [0].text_id  
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [1].icon_index "FACTORY"
									    sst_factory_id['BTC-8E'], 0x00,0x00,0x00,   ## [1].text_id 
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x02,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [2].icon_index   "CUSTOM"
									    sst_custom_id['BTC-8E'], 0x00,0x00,0x00,   ## [2].text_id 
    									    0x01,0x00,0x00,0x00,   ## [2].disable_item
    									    0x01,0x00,0x00,0x00,   ## [2].menu_increment
									    0x00,0x00,0x00,0x00,   ## [2].menu_selection
									    0x01,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [3].icon_index "SAVE CUSTOM"
									    sst_save_sp_custom_id['BTC-8E'], 0x00,0x00,0x00,   ## [3].text_id
    									    0x00,0x00,0x00,0x00,   ## [3].disable_item
    									    0x01,0x00,0x00,0x00,   ## [3].menu_increment
									    0x00,0x00,0x00,0x00,   ## [3].menu_selection
									    0x01,0x00,0x00,0x00,   ## [3].return_state_id
									    0x04,0x00,0x00,0x00,   ## [3].next_state_id
									    enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [4].icon_index "DEFAULT SETTINGS"
									    sst_default_sp_settings_id['BTC-8E'], 0x00,0x00,0x00,   ## [4].text_id
    									    0x00,0x00,0x00,0x00,   ## [4].disable_item
    									    0x00,0x00,0x00,0x00,   ## [4].menu_increment
									    0x01,0x00,0x00,0x00,   ## [4].menu_selection
									    0x03,0x00,0x00,0x00,   ## [4].return_state_id
									    enum_icon_no_icon['BTC-8E'],0x00,0x00,0x00,   ## [4].next_state_id
									    ])
cst_menu_patch_list['g_restore_default_menu']['change_to_bytes']['BTC-7E-HP4']   = bytes([enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu "No"
									    sst_no_id['BTC-7E-HP4'],0x00,0x00,0x00,   ## [0].text_id  
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [1].icon_index "FACTORY"
									    sst_factory_id['BTC-7E-HP4'], 0x00,0x00,0x00,   ## [1].text_id 
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x02,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [2].icon_index   "CUSTOM"
									    sst_custom_id['BTC-7E-HP4'], 0x00,0x00,0x00,   ## [2].text_id 
    									    0x01,0x00,0x00,0x00,   ## [2].disable_item
    									    0x01,0x00,0x00,0x00,   ## [2].menu_increment
									    0x00,0x00,0x00,0x00,   ## [2].menu_selection
									    0x01,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [3].icon_index "SAVE CUSTOM"
									    sst_save_sp_custom_id['BTC-7E-HP4'], 0x00,0x00,0x00,   ## [3].text_id
    									    0x00,0x00,0x00,0x00,   ## [3].disable_item
    									    0x01,0x00,0x00,0x00,   ## [3].menu_increment
									    0x00,0x00,0x00,0x00,   ## [3].menu_selection
									    0x01,0x00,0x00,0x00,   ## [3].return_state_id
									    0x04,0x00,0x00,0x00,   ## [3].next_state_id
									    enum_icon_no_icon['BTC-7E-HP4'],0x00,0x00,0x00,   ## [4].icon_index "DEFAULT SETTINGS"
									    sst_default_sp_settings_id['BTC-7E-HP4'], 0x00,0x00,0x00,   ## [4].text_id
    									    0x00,0x00,0x00,0x00,   ## [4].disable_item
    									    0x00,0x00,0x00,0x00,   ## [4].menu_increment
									    0x01,0x00,0x00,0x00,   ## [4].menu_selection
									    0x03,0x00,0x00,0x00,   ## [4].return_state_id
									    0x03,0x00,0x00,0x00,   ## [4].next_state_id
									    ])
cst_menu_patch_list['g_restore_default_menu']['change_to_bytes']['BTC-8E-HP4']   = bytes([enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu "No"
									    sst_no_id['BTC-8E-HP4'],0x00,0x00,0x00,   ## [0].text_id  
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [1].icon_index "FACTORY"
									    sst_factory_id['BTC-8E-HP4'], 0x00,0x00,0x00,   ## [1].text_id 
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x02,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [2].icon_index   "CUSTOM"
									    sst_custom_id['BTC-8E-HP4'], 0x00,0x00,0x00,   ## [2].text_id 
    									    0x01,0x00,0x00,0x00,   ## [2].disable_item
    									    0x01,0x00,0x00,0x00,   ## [2].menu_increment
									    0x00,0x00,0x00,0x00,   ## [2].menu_selection
									    0x01,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [3].icon_index "SAVE CUSTOM"
									    sst_save_sp_custom_id['BTC-8E-HP4'], 0x00,0x00,0x00,   ## [3].text_id
    									    0x00,0x00,0x00,0x00,   ## [3].disable_item
    									    0x01,0x00,0x00,0x00,   ## [3].menu_increment
									    0x00,0x00,0x00,0x00,   ## [3].menu_selection
									    0x01,0x00,0x00,0x00,   ## [3].return_state_id
									    0x04,0x00,0x00,0x00,   ## [3].next_state_id
									    enum_icon_no_icon['BTC-8E-HP4'],0x00,0x00,0x00,   ## [4].icon_index "DEFAULT SETTINGS"
									    sst_default_sp_settings_id['BTC-8E-HP4'], 0x00,0x00,0x00,   ## [4].text_id
    									    0x00,0x00,0x00,0x00,   ## [4].disable_item
    									    0x00,0x00,0x00,0x00,   ## [4].menu_increment
									    0x01,0x00,0x00,0x00,   ## [4].menu_selection
									    0x03,0x00,0x00,0x00,   ## [4].return_state_id
									    0x03,0x00,0x00,0x00,   ## [4].next_state_id
									    ])

cst_menu_patch_list['g_restore_default_menu']['change_to_bytes']['BTC-7E-HP5']   = bytes([enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu "No"
									    sst_no_id['BTC-7E-HP5'],0x00,0x00,0x00,   ## [0].text_id  
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [1].icon_index "FACTORY"
									    sst_factory_id['BTC-7E-HP5'], 0x00,0x00,0x00,   ## [1].text_id 
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x02,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [2].icon_index   "CUSTOM"
									    sst_custom_id['BTC-7E-HP5'], 0x00,0x00,0x00,   ## [2].text_id 
    									    0x01,0x00,0x00,0x00,   ## [2].disable_item
    									    0x01,0x00,0x00,0x00,   ## [2].menu_increment
									    0x00,0x00,0x00,0x00,   ## [2].menu_selection
									    0x01,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [3].icon_index "SAVE CUSTOM"
									    sst_save_sp_custom_id['BTC-7E-HP5'], 0x00,0x00,0x00,   ## [3].text_id
    									    0x00,0x00,0x00,0x00,   ## [3].disable_item
    									    0x01,0x00,0x00,0x00,   ## [3].menu_increment
									    0x00,0x00,0x00,0x00,   ## [3].menu_selection
									    0x01,0x00,0x00,0x00,   ## [3].return_state_id
									    0x04,0x00,0x00,0x00,   ## [3].next_state_id
									    enum_icon_no_icon['BTC-7E-HP5'],0x00,0x00,0x00,   ## [4].icon_index "DEFAULT SETTINGS"
									    sst_default_sp_settings_id['BTC-7E-HP5'], 0x00,0x00,0x00,   ## [4].text_id
    									    0x00,0x00,0x00,0x00,   ## [4].disable_item
    									    0x00,0x00,0x00,0x00,   ## [4].menu_increment
									    0x01,0x00,0x00,0x00,   ## [4].menu_selection
									    0x03,0x00,0x00,0x00,   ## [4].return_state_id
									    0x03,0x00,0x00,0x00,   ## [4].next_state_id
									    ])
cst_menu_patch_list['g_restore_default_menu']['change_to_bytes']['BTC-8E-HP5']   = bytes([enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [0].icon_index for g_restore_default_menu "No"
									    sst_no_id['BTC-8E-HP5'],0x00,0x00,0x00,   ## [0].text_id  
    									    0x00,0x00,0x00,0x00,   ## [0].disable_item
    									    0x01,0x00,0x00,0x00,   ## [0].menu_increment
									    0x00,0x00,0x00,0x00,   ## [0].menu_selection
									    0x01,0x00,0x00,0x00,   ## [0].return_state_id
									    0x01,0x00,0x00,0x00,   ## [0].next_state_id
									    enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [1].icon_index "FACTORY"
									    sst_factory_id['BTC-8E-HP5'], 0x00,0x00,0x00,   ## [1].text_id 
    									    0x00,0x00,0x00,0x00,   ## [1].disable_item
    									    0x01,0x00,0x00,0x00,   ## [1].menu_increment
									    0x00,0x00,0x00,0x00,   ## [1].menu_selection
									    0x01,0x00,0x00,0x00,   ## [1].return_state_id
									    0x02,0x00,0x00,0x00,   ## [1].next_state_id
									    enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [2].icon_index   "CUSTOM"
									    sst_custom_id['BTC-8E-HP5'], 0x00,0x00,0x00,   ## [2].text_id 
    									    0x01,0x00,0x00,0x00,   ## [2].disable_item
    									    0x01,0x00,0x00,0x00,   ## [2].menu_increment
									    0x00,0x00,0x00,0x00,   ## [2].menu_selection
									    0x01,0x00,0x00,0x00,   ## [2].return_state_id
									    0x03,0x00,0x00,0x00,   ## [2].next_state_id
									    enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [3].icon_index "SAVE CUSTOM"
									    sst_save_sp_custom_id['BTC-8E-HP5'], 0x00,0x00,0x00,   ## [3].text_id
    									    0x00,0x00,0x00,0x00,   ## [3].disable_item
    									    0x01,0x00,0x00,0x00,   ## [3].menu_increment
									    0x00,0x00,0x00,0x00,   ## [3].menu_selection
									    0x01,0x00,0x00,0x00,   ## [3].return_state_id
									    0x04,0x00,0x00,0x00,   ## [3].next_state_id
									    enum_icon_no_icon['BTC-8E-HP5'],0x00,0x00,0x00,   ## [4].icon_index "DEFAULT SETTINGS"
									    sst_default_sp_settings_id['BTC-8E-HP5'], 0x00,0x00,0x00,   ## [4].text_id
    									    0x00,0x00,0x00,0x00,   ## [4].disable_item
    									    0x00,0x00,0x00,0x00,   ## [4].menu_increment
									    0x01,0x00,0x00,0x00,   ## [4].menu_selection
									    0x03,0x00,0x00,0x00,   ## [4].return_state_id
									    0x03,0x00,0x00,0x00,   ## [4].next_state_id
									    ])





#    replace first entry @ 0x802c9e68 g_camera_setup_menu_item_array
#			     w/         g_wbwl_camera_setup_menu_item_array
# in g_main_menu_selector_array[]
# unknown line number
cst_menu_patch_list['setup_items_pointer'] = {}
cst_menu_patch_list['setup_items_pointer']['function'] = 'g_main_menu_selector_array'
cst_menu_patch_list['setup_items_pointer']['line_number'] = {}
cst_menu_patch_list['setup_items_pointer']['line_number']['BTC-7A'] = 0
cst_menu_patch_list['setup_items_pointer']['line_number']['BTC-7E'] = 0
cst_menu_patch_list['setup_items_pointer']['line_number']['BTC-8E'] = 0
cst_menu_patch_list['setup_items_pointer']['line_number']['BTC-7E-HP4'] = 0
cst_menu_patch_list['setup_items_pointer']['line_number']['BTC-8E-HP4'] = 0
cst_menu_patch_list['setup_items_pointer']['line_number']['BTC-7E-HP5'] = 0
cst_menu_patch_list['setup_items_pointer']['line_number']['BTC-8E-HP5'] = 0
cst_menu_patch_list['setup_items_pointer']['start_offset'] = {}
cst_menu_patch_list['setup_items_pointer']['start_offset']['BTC-7A'] = 0x035564c
cst_menu_patch_list['setup_items_pointer']['start_offset']['BTC-7E'] = 0x035564c
cst_menu_patch_list['setup_items_pointer']['start_offset']['BTC-8E'] = 0x03556a4
cst_menu_patch_list['setup_items_pointer']['start_offset']['BTC-7E-HP4'] = 0x03586a4
cst_menu_patch_list['setup_items_pointer']['start_offset']['BTC-8E-HP4'] = 0x035c8d4
cst_menu_patch_list['setup_items_pointer']['start_offset']['BTC-7E-HP5'] = 0x02ce120
cst_menu_patch_list['setup_items_pointer']['start_offset']['BTC-8E-HP5'] = 0x02d02e0
cst_menu_patch_list['setup_items_pointer']['change_from_ptr'] = 'g_camera_setup_menu_item_array'
cst_menu_patch_list['setup_items_pointer']['change_to_ptr'] = 'g_wbwl_camera_setup_menu_item_array'

#    replace second @ 0x802c9e6c  which is  0x19 (25)
#                                w/         0x1d (29) 
# in g_main_menu_selector_array[]
# unknown line number
cst_menu_patch_list['setup_items_number'] = {}
cst_menu_patch_list['setup_items_number']['function'] = 'g_main_menu_selector_array'
cst_menu_patch_list['setup_items_number']['line_number'] = {}
cst_menu_patch_list['setup_items_number']['line_number']['BTC-7A'] = 0
cst_menu_patch_list['setup_items_number']['line_number']['BTC-7E'] = 0
cst_menu_patch_list['setup_items_number']['line_number']['BTC-8E'] = 0
cst_menu_patch_list['setup_items_number']['line_number']['BTC-7E-HP4'] = 0
cst_menu_patch_list['setup_items_number']['line_number']['BTC-8E-HP4'] = 0
cst_menu_patch_list['setup_items_number']['line_number']['BTC-7E-HP5'] = 0
cst_menu_patch_list['setup_items_number']['line_number']['BTC-8E-HP5'] = 0
cst_menu_patch_list['setup_items_number']['start_offset'] = {}
cst_menu_patch_list['setup_items_number']['start_offset']['BTC-7A'] = 0x0355650
cst_menu_patch_list['setup_items_number']['start_offset']['BTC-7E'] = 0x0355650
cst_menu_patch_list['setup_items_number']['start_offset']['BTC-8E'] = 0x03556a8
cst_menu_patch_list['setup_items_number']['start_offset']['BTC-7E-HP4'] = 0x03586a8
cst_menu_patch_list['setup_items_number']['start_offset']['BTC-8E-HP4'] = 0x035c8d8
cst_menu_patch_list['setup_items_number']['start_offset']['BTC-7E-HP5'] = 0x02ce124
cst_menu_patch_list['setup_items_number']['start_offset']['BTC-8E-HP5'] = 0x02d02e4
cst_menu_patch_list['setup_items_number']['change_from_bytes'] = {}
cst_menu_patch_list['setup_items_number']['change_from_bytes']['BTC-7A'] = bytes([menus_define_expected_setup_menu_items['BTC-7A'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_from_bytes']['BTC-7E'] = bytes([menus_define_expected_setup_menu_items['BTC-7E'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_from_bytes']['BTC-8E'] = bytes([menus_define_expected_setup_menu_items['BTC-8E'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_from_bytes']['BTC-7E-HP4'] = bytes([menus_define_expected_setup_menu_items['BTC-7E-HP4'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_from_bytes']['BTC-8E-HP4'] = bytes([menus_define_expected_setup_menu_items['BTC-8E-HP4'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_from_bytes']['BTC-7E-HP5'] = bytes([menus_define_expected_setup_menu_items['BTC-7E-HP5'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_from_bytes']['BTC-8E-HP5'] = bytes([menus_define_expected_setup_menu_items['BTC-8E-HP5'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_to_bytes'] = {}
cst_menu_patch_list['setup_items_number']['change_to_bytes']['BTC-7A'] = bytes([menus_define_new_setup_menu_items['BTC-7A'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_to_bytes']['BTC-7E'] = bytes([menus_define_new_setup_menu_items['BTC-7E'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_to_bytes']['BTC-8E'] = bytes([menus_define_new_setup_menu_items['BTC-8E'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_to_bytes']['BTC-7E-HP4'] = bytes([menus_define_new_setup_menu_items['BTC-7E-HP4'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_to_bytes']['BTC-8E-HP4'] = bytes([menus_define_new_setup_menu_items['BTC-8E-HP4'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_to_bytes']['BTC-7E-HP5'] = bytes([menus_define_new_setup_menu_items['BTC-7E-HP5'], 0x00, 0x00, 0x00])
cst_menu_patch_list['setup_items_number']['change_to_bytes']['BTC-8E-HP5'] = bytes([menus_define_new_setup_menu_items['BTC-8E-HP5'], 0x00, 0x00, 0x00])

##
## Capture Timer for BTC_7A
##
##    Enabling the BTC_7A to use BTC_7E baseline firmware
##    Two big things we have to work around --
##         - gpio for signal that notices aux power plugged in is different
##         - BTC-7A firmware update does not generate the correct checksum;
##                  to BTC-7E boot must be kept from checking
ctm_patch_list = {}

# patch calls to get_power_supply_mode()
ctm_patch_list['ctm_power_supply_tv13'] = {}
ctm_patch_list['ctm_power_supply_tv13']['function'] = 'TaskVerification_FSM_task13_battery_test'
ctm_patch_list['ctm_power_supply_tv13']['line_number'] = {}
ctm_patch_list['ctm_power_supply_tv13']['line_number']['BTC-7A'] = 28
ctm_patch_list['ctm_power_supply_tv13']['start_offset'] = {}
ctm_patch_list['ctm_power_supply_tv13']['start_offset']['BTC-7A'] = 0x01214c8
ctm_patch_list['ctm_power_supply_tv13']['change_from_jump'] = {}
ctm_patch_list['ctm_power_supply_tv13']['change_from_jump']['BTC-7A'] = 'jal.get_power_supply_mode'
ctm_patch_list['ctm_power_supply_tv13']['change_to_jump'] = {}
ctm_patch_list['ctm_power_supply_tv13']['change_to_jump']['BTC-7A'] = 'jal.ctm_get_power_supply_mode'

ctm_patch_list['ctm_upgrade4'] = {}
ctm_patch_list['ctm_upgrade4']['function'] = 'TaskUpgrade_FSM_4_check_power'
ctm_patch_list['ctm_upgrade4']['line_number'] = {}
ctm_patch_list['ctm_upgrade4']['line_number']['BTC-7A'] = 10
ctm_patch_list['ctm_upgrade4']['start_offset'] = {}
ctm_patch_list['ctm_upgrade4']['start_offset']['BTC-7A'] = 0x012a550
ctm_patch_list['ctm_upgrade4']['change_from_jump'] = {}
ctm_patch_list['ctm_upgrade4']['change_from_jump']['BTC-7A'] = 'jal.get_power_supply_mode'
ctm_patch_list['ctm_upgrade4']['change_to_jump'] = {}
ctm_patch_list['ctm_upgrade4']['change_to_jump']['BTC-7A'] = 'jal.ctm_get_power_supply_mode'

ctm_patch_list['ctm_photo_test5'] = {}
ctm_patch_list['ctm_photo_test5']['function'] = 'TaskPhotoTestFSM_task5'
ctm_patch_list['ctm_photo_test5']['line_number'] = {}
ctm_patch_list['ctm_photo_test5']['line_number']['BTC-7A'] = 33
ctm_patch_list['ctm_photo_test5']['start_offset'] = {}
ctm_patch_list['ctm_photo_test5']['start_offset']['BTC-7A'] = 0x012c8ec
ctm_patch_list['ctm_photo_test5']['change_from_jump'] = {}
ctm_patch_list['ctm_photo_test5']['change_from_jump']['BTC-7A'] = 'jal.get_power_supply_mode'
ctm_patch_list['ctm_photo_test5']['change_to_jump'] = {}
ctm_patch_list['ctm_photo_test5']['change_to_jump']['BTC-7A'] = 'jal.ctm_get_power_supply_mode'

ctm_patch_list['ctm_video_test5'] = {}
ctm_patch_list['ctm_video_test5']['function'] = 'TaskPhotoTestFSM_task5'
ctm_patch_list['ctm_video_test5']['line_number'] = {}
ctm_patch_list['ctm_video_test5']['line_number']['BTC-7A'] = 33
ctm_patch_list['ctm_video_test5']['start_offset'] = {}
ctm_patch_list['ctm_video_test5']['start_offset']['BTC-7A'] = 0x012d14c
ctm_patch_list['ctm_video_test5']['change_from_jump'] = {}
ctm_patch_list['ctm_video_test5']['change_from_jump']['BTC-7A'] = 'jal.get_power_supply_mode'
ctm_patch_list['ctm_video_test5']['change_to_jump'] = {}
ctm_patch_list['ctm_video_test5']['change_to_jump']['BTC-7A'] = 'jal.ctm_get_power_supply_mode'

ctm_patch_list['ctm_screen_display'] = {}
ctm_patch_list['ctm_screen_display']['function'] = 'ScreenDisplayBottomRibbonPowerSupply'
ctm_patch_list['ctm_screen_display']['line_number'] = {}
ctm_patch_list['ctm_screen_display']['line_number']['BTC-7A'] = 10
ctm_patch_list['ctm_screen_display']['start_offset'] = {}
ctm_patch_list['ctm_screen_display']['start_offset']['BTC-7A'] = 0x012db20
ctm_patch_list['ctm_screen_display']['change_from_jump'] = {}
ctm_patch_list['ctm_screen_display']['change_from_jump']['BTC-7A'] = 'jal.get_power_supply_mode'
ctm_patch_list['ctm_screen_display']['change_to_jump'] = {}
ctm_patch_list['ctm_screen_display']['change_to_jump']['BTC-7A'] = 'jal.ctm_get_power_supply_mode'

# Find the right bit in the GPIO pins to check the SD card
#      Use the same bit position and shift mask as in the original BTC-7A code
ctm_patch_list['ctm_check_sd_card0'] = {}
ctm_patch_list['ctm_check_sd_card0']['function'] = 'checkForSDCard'
ctm_patch_list['ctm_check_sd_card0']['line_number'] = {}
ctm_patch_list['ctm_check_sd_card0']['line_number']['BTC-7A'] = 7
ctm_patch_list['ctm_check_sd_card0']['start_offset'] = {}
ctm_patch_list['ctm_check_sd_card0']['start_offset']['BTC-7A'] = 0x0114af4
ctm_patch_list['ctm_check_sd_card0']['change_from_bytes'] = {}
ctm_patch_list['ctm_check_sd_card0']['change_from_bytes']['BTC-7A'] = bytes([0x00, 0x02, 0x05, 0x24])  ## li a1, 0x200
ctm_patch_list['ctm_check_sd_card0']['change_to_bytes'] = {}
ctm_patch_list['ctm_check_sd_card0']['change_to_bytes']['BTC-7A'] = bytes([0x00, 0x20, 0x05, 0x24]) ## li a1, 0x2000

ctm_patch_list['ctm_check_sd_card1'] = {}
ctm_patch_list['ctm_check_sd_card1']['function'] = 'checkForSDCard'
ctm_patch_list['ctm_check_sd_card1']['line_number'] = {}
ctm_patch_list['ctm_check_sd_card1']['line_number']['BTC-7A'] = 8
ctm_patch_list['ctm_check_sd_card1']['start_offset'] = {}
ctm_patch_list['ctm_check_sd_card1']['start_offset']['BTC-7A'] = 0x0114b08
ctm_patch_list['ctm_check_sd_card1']['change_from_bytes'] = {}
ctm_patch_list['ctm_check_sd_card1']['change_from_bytes']['BTC-7A'] = bytes([0x00, 0x02, 0x05, 0x24])  ## li a1, 0x200
ctm_patch_list['ctm_check_sd_card1']['change_to_bytes'] = {}
ctm_patch_list['ctm_check_sd_card1']['change_to_bytes']['BTC-7A'] = bytes([0x00, 0x20, 0x05, 0x24]) ## li a1, 0x2000

ctm_patch_list['ctm_check_sd_card2'] = {}
ctm_patch_list['ctm_check_sd_card2']['function'] = 'checkForSDCard'
ctm_patch_list['ctm_check_sd_card2']['line_number'] = {}
ctm_patch_list['ctm_check_sd_card2']['line_number']['BTC-7A'] = 9
ctm_patch_list['ctm_check_sd_card2']['start_offset'] = {}
ctm_patch_list['ctm_check_sd_card2']['start_offset']['BTC-7A'] = 0x0114b20
ctm_patch_list['ctm_check_sd_card2']['change_from_bytes'] = {}
ctm_patch_list['ctm_check_sd_card2']['change_from_bytes']['BTC-7A'] = bytes([0x00, 0x02, 0x05, 0x24])  ## li a1, 0x200
ctm_patch_list['ctm_check_sd_card2']['change_to_bytes'] = {}
ctm_patch_list['ctm_check_sd_card2']['change_to_bytes']['BTC-7A'] = bytes([0x00, 0x20, 0x05, 0x24]) ## li a1, 0x2000

ctm_patch_list['ctm_check_sd_card3'] = {}
ctm_patch_list['ctm_check_sd_card3']['function'] = 'checkForSDCard'
ctm_patch_list['ctm_check_sd_card3']['line_number'] = {}
ctm_patch_list['ctm_check_sd_card3']['line_number']['BTC-7A'] = 10
ctm_patch_list['ctm_check_sd_card3']['start_offset'] = {}
ctm_patch_list['ctm_check_sd_card3']['start_offset']['BTC-7A'] = 0x0114b2c
ctm_patch_list['ctm_check_sd_card3']['change_from_bytes'] = {}
ctm_patch_list['ctm_check_sd_card3']['change_from_bytes']['BTC-7A'] = bytes([0x42, 0x12, 0x02, 0x00])  ## srl v0, v0, 0x9
ctm_patch_list['ctm_check_sd_card3']['change_to_bytes'] = {}
ctm_patch_list['ctm_check_sd_card3']['change_to_bytes']['BTC-7A'] = bytes([0x42, 0x13, 0x02, 0x00]) ## srl v0, v0, 0xd

# change the global variable that enodes the event_numer for the SD_CARD present GPIO
ctm_patch_list['ctm_sd_card_gpio_event_number0'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number0']['function'] = 'g_sd_disk_gpio.event_number[0]'
ctm_patch_list['ctm_sd_card_gpio_event_number0']['line_number'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number0']['line_number']['BTC-7A'] = 0
ctm_patch_list['ctm_sd_card_gpio_event_number0']['start_offset'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number0']['start_offset']['BTC-7A'] = 0x039cd04
ctm_patch_list['ctm_sd_card_gpio_event_number0']['change_from_bytes'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number0']['change_from_bytes']['BTC-7A'] = bytes([0x00, 0x02, 0x00, 0x00])  
ctm_patch_list['ctm_sd_card_gpio_event_number0']['change_to_bytes'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number0']['change_to_bytes']['BTC-7A'] = bytes([0x00, 0x20, 0x00, 0x00]) 

ctm_patch_list['ctm_sd_card_gpio_event_number1'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number1']['function'] = 'g_sd_disk_gpio.event_number[0]'
ctm_patch_list['ctm_sd_card_gpio_event_number1']['line_number'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number1']['line_number']['BTC-7A'] = 1
ctm_patch_list['ctm_sd_card_gpio_event_number1']['start_offset'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number1']['start_offset']['BTC-7A'] = 0x039cd08
ctm_patch_list['ctm_sd_card_gpio_event_number1']['change_from_bytes'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number1']['change_from_bytes']['BTC-7A'] = bytes([0x01, 0x02, 0x00, 0x00])  
ctm_patch_list['ctm_sd_card_gpio_event_number1']['change_to_bytes'] = {}
ctm_patch_list['ctm_sd_card_gpio_event_number1']['change_to_bytes']['BTC-7A'] = bytes([0x01, 0x20, 0x00, 0x00]) 

# change the location of the bit in the csr from 0x9 to 0xd
ctm_patch_list['ctm_sd_card_gpio_bit_number'] = {}
ctm_patch_list['ctm_sd_card_gpio_bit_number']['function'] = 'host_disk_detect'
ctm_patch_list['ctm_sd_card_gpio_bit_number']['line_number'] = {}
ctm_patch_list['ctm_sd_card_gpio_bit_number']['line_number']['BTC-7A'] = 13
ctm_patch_list['ctm_sd_card_gpio_bit_number']['start_offset'] = {}
ctm_patch_list['ctm_sd_card_gpio_bit_number']['start_offset']['BTC-7A'] = 0x000eac8
ctm_patch_list['ctm_sd_card_gpio_bit_number']['change_from_bytes'] = {}
ctm_patch_list['ctm_sd_card_gpio_bit_number']['change_from_bytes']['BTC-7A'] = bytes([0x09, 0x00, 0x02, 0x24])  
ctm_patch_list['ctm_sd_card_gpio_bit_number']['change_to_bytes'] = {}
ctm_patch_list['ctm_sd_card_gpio_bit_number']['change_to_bytes']['BTC-7A'] = bytes([0x0d, 0x00, 0x02, 0x24]) 

# Call a different verson of event_loop_iterator for the 7A
ctm_patch_list['ctm_event_loop_iterator'] = {}
ctm_patch_list['ctm_event_loop_iterator']['function'] = 'host_banner_loop'
ctm_patch_list['ctm_event_loop_iterator']['line_number'] = {}
ctm_patch_list['ctm_event_loop_iterator']['line_number']['BTC-7A'] = 28
ctm_patch_list['ctm_event_loop_iterator']['start_offset'] = {}
ctm_patch_list['ctm_event_loop_iterator']['start_offset']['BTC-7A'] = 0x00e01f4
ctm_patch_list['ctm_event_loop_iterator']['change_from_jump'] = 'jal.event_loop_iterator'
ctm_patch_list['ctm_event_loop_iterator']['change_to_jump'] = 'jal.ctm_event_loop_iterator'

# Fixing a bug with retry of the PIR sensor CSR config
#    Outer "while" loop now includes resetting the bit_selector
ctm_patch_list['ctm_pir_retry_bug_fix'] = {}
ctm_patch_list['ctm_pir_retry_bug_fix']['function'] = 'DigiPIR_SetConfigRegister'
ctm_patch_list['ctm_pir_retry_bug_fix']['line_number'] = {}
ctm_patch_list['ctm_pir_retry_bug_fix']['line_number']['BTC-7A'] = 7
ctm_patch_list['ctm_pir_retry_bug_fix']['line_number']['BTC-7E'] = 7
ctm_patch_list['ctm_pir_retry_bug_fix']['start_offset'] = {}
ctm_patch_list['ctm_pir_retry_bug_fix']['start_offset']['BTC-7A'] = 0x010d86c
ctm_patch_list['ctm_pir_retry_bug_fix']['start_offset']['BTC-7E'] = 0x010d86c
ctm_patch_list['ctm_pir_retry_bug_fix']['change_from_jump'] = 'j.DigiPIRSpi_Write'
ctm_patch_list['ctm_pir_retry_bug_fix']['change_to_jump'] =   'j.ctm_DigiPIRSpi_Write'

# ##############################################################
# ## DEBUG -- No trigger in colde weather bug in BTC-{7,8}E-HP5
# # Call a different verson of get_temperatureForC -- always returns a negative temp
# ctm_patch_list['ctm_get_temperatureForC'] = {}
# ctm_patch_list['ctm_get_temperatureForC']['function'] = 'set_cold_item_overtemp_p'
# ctm_patch_list['ctm_get_temperatureForC']['line_number'] = {}
# ctm_patch_list['ctm_get_temperatureForC']['line_number']['BTC-8E-HP5'] = 12
# ctm_patch_list['ctm_get_temperatureForC']['start_offset'] = {}
# ctm_patch_list['ctm_get_temperatureForC']['start_offset']['BTC-8E-HP5'] = 0x00e71b8
# ctm_patch_list['ctm_get_temperatureForC']['change_from_jump'] = 'jal.get_temperatureForC'
# ctm_patch_list['ctm_get_temperatureForC']['change_to_jump'] = 'jal.ctm_get_temperatureForC'
# # still_MCUApp_ResetPIRPin -- reroute call to set_cold_item_overtemp_p
# ctm_patch_list['ctm_still_MCUApp_ResetPIRPin'] = {}
# ctm_patch_list['ctm_still_MCUApp_ResetPIRPin']['function'] = 'still_MCUApp_ResetPIRPin'
# ctm_patch_list['ctm_still_MCUApp_ResetPIRPin']['line_number'] = {}
# ctm_patch_list['ctm_still_MCUApp_ResetPIRPin']['line_number']['BTC-8E-HP5'] = 39
# ctm_patch_list['ctm_still_MCUApp_ResetPIRPin']['start_offset'] = {}
# ctm_patch_list['ctm_still_MCUApp_ResetPIRPin']['start_offset']['BTC-8E-HP5'] = 0x0102ae0
# ctm_patch_list['ctm_still_MCUApp_ResetPIRPin']['change_from_jump'] = 'jal.set_cold_item_overtemp_p'
# ctm_patch_list['ctm_still_MCUApp_ResetPIRPin']['change_to_jump'] = 'jal.ctm_set_cold_item_overtemp_p'
# # HceTaskRecording_RecVideoToRec -- reroute call to set_cold_item_overtemp_p
# ctm_patch_list['ctm_HceTaskRecording_RecVideoToRec'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoToRec']['function'] = 'HceTaskRecording_RecVideoToRec'
# ctm_patch_list['ctm_HceTaskRecording_RecVideoToRec']['line_number'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoToRec']['line_number']['BTC-8E-HP5'] = 28
# ctm_patch_list['ctm_HceTaskRecording_RecVideoToRec']['start_offset'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoToRec']['start_offset']['BTC-8E-HP5'] = 0x010303c
# ctm_patch_list['ctm_HceTaskRecording_RecVideoToRec']['change_from_jump'] = 'jal.set_cold_item_overtemp_p'
# ctm_patch_list['ctm_HceTaskRecording_RecVideoToRec']['change_to_jump'] = 'jal.ctm_set_cold_item_overtemp_p'
# # HceTskRecordingRecStop -- reroute call to set_cold_item_overtemp_p
# ctm_patch_list['ctm_HceTskRecordingRecStop'] = {}
# ctm_patch_list['ctm_HceTskRecordingRecStop']['function'] = 'HceTskRecordingRecStop'
# ctm_patch_list['ctm_HceTskRecordingRecStop']['line_number'] = {}
# ctm_patch_list['ctm_HceTskRecordingRecStop']['line_number']['BTC-8E-HP5'] = 73
# ctm_patch_list['ctm_HceTskRecordingRecStop']['start_offset'] = {}
# ctm_patch_list['ctm_HceTskRecordingRecStop']['start_offset']['BTC-8E-HP5'] = 0x0103384
# ctm_patch_list['ctm_HceTskRecordingRecStop']['change_from_jump'] = 'jal.set_cold_item_overtemp_p'
# ctm_patch_list['ctm_HceTskRecordingRecStop']['change_to_jump'] = 'jal.ctm_set_cold_item_overtemp_p'
# # HceTaskRecording_RecVideoWaitAE -- reroute call to set_cold_item_overtemp_p
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitAE'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitAE']['function'] = 'HceTaskRecording_RecVideoWaitAE'
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitAE']['line_number'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitAE']['line_number']['BTC-8E-HP5'] = 40
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitAE']['start_offset'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitAE']['start_offset']['BTC-8E-HP5'] = 0x0103af0
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitAE']['change_from_jump'] = 'jal.set_cold_item_overtemp_p'
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitAE']['change_to_jump'] = 'jal.ctm_set_cold_item_overtemp_p'
# # HceTaskRecording_RecVideoWaitLed -- reroute call to set_cold_item_overtemp_p
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitLed'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitLed']['function'] = 'HceTaskRecording_RecVideoWaitLed'
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitLed']['line_number'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitLed']['line_number']['BTC-8E-HP5'] = 25
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitLed']['start_offset'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitLed']['start_offset']['BTC-8E-HP5'] = 0x0103dec
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitLed']['change_from_jump'] = 'jal.set_cold_item_overtemp_p'
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitLed']['change_to_jump'] = 'jal.ctm_set_cold_item_overtemp_p'
# # HceTaskRecording_RecVideoWaitView -- reroute call to set_cold_item_overtemp_p
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitView'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitView']['function'] = 'HceTaskRecording_RecVideoWaitView'
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitView']['line_number'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitView']['line_number']['BTC-8E-HP5'] = 24
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitView']['start_offset'] = {}
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitView']['start_offset']['BTC-8E-HP5'] = 0x0103f44
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitView']['change_from_jump'] = 'jal.set_cold_item_overtemp_p'
# ctm_patch_list['ctm_HceTaskRecording_RecVideoWaitView']['change_to_jump'] = 'jal.ctm_set_cold_item_overtemp_p'

##############################################################


# # DEBUG -- cause a crash in spawn_ModeNoSD2FSM
# ctm_patch_list['ctm_debug_no_sd'] = {}
# ctm_patch_list['ctm_debug_no_sd']['function'] = 'spawn_ModeNoSD2FSM'
# ctm_patch_list['ctm_debug_no_sd']['line_number'] = {}
# ctm_patch_list['ctm_debug_no_sd']['line_number']['BTC-7E'] = 19
# ctm_patch_list['ctm_debug_no_sd']['start_offset'] = {}
# ctm_patch_list['ctm_debug_no_sd']['start_offset']['BTC-7E'] = 0x0130698
# ctm_patch_list['ctm_debug_no_sd']['change_from_jump'] = {}
# ctm_patch_list['ctm_debug_no_sd']['change_from_jump']['BTC-7E'] = 'jal.fsm_spawn'
# ctm_patch_list['ctm_debug_no_sd']['change_to_jump'] = {}
# ctm_patch_list['ctm_debug_no_sd']['change_to_jump']['BTC-7E'] = 'jal.ctm_fsm_spawn'

# Zero out .BRN file checksum.  The BTC-7A firmware does not contain the correct
#      checksum.
ctm_patch_list['ctm_clear_brn_checksum'] = {}
ctm_patch_list['ctm_clear_brn_checksum']['function'] = 'parse_brn_file'
ctm_patch_list['ctm_clear_brn_checksum']['line_number'] = {}
ctm_patch_list['ctm_clear_brn_checksum']['line_number']['BTC-7A'] = 74
ctm_patch_list['ctm_clear_brn_checksum']['start_offset'] = {}
ctm_patch_list['ctm_clear_brn_checksum']['start_offset']['BTC-7A'] = 0x01d2d50
ctm_patch_list['ctm_clear_brn_checksum']['change_from_bytes'] = {}
ctm_patch_list['ctm_clear_brn_checksum']['change_from_bytes']['BTC-7A'] = bytes([0x21, 0x98, 0x62, 0x02])  ## addu s3,s3,v0
ctm_patch_list['ctm_clear_brn_checksum']['change_to_bytes'] = {}
ctm_patch_list['ctm_clear_brn_checksum']['change_to_bytes']['BTC-7A'] = bytes([0x21, 0x98, 0x00, 0x00]) ## addu s3,zero,zero 

# Debug: trying to figure out why video aborts when in IR flash (night) mode
# ctm_patch_list['ctm_check_for_sd_card'] = {}
# ctm_patch_list['ctm_check_for_sd_card']['function'] = 'HceTaskRecordingRecStop'
# ctm_patch_list['ctm_check_for_sd_card']['line_number'] = {}
# ctm_patch_list['ctm_check_for_sd_card']['line_number']['BTC-7A'] = 48
# ctm_patch_list['ctm_check_for_sd_card']['start_offset'] = {}
# ctm_patch_list['ctm_check_for_sd_card']['start_offset']['BTC-7A'] = 0x0123fb4
# ctm_patch_list['ctm_check_for_sd_card']['change_from_jump'] = {}
# ctm_patch_list['ctm_check_for_sd_card']['change_from_jump']['BTC-7A'] = 'jal.checkForSDCard'
# ctm_patch_list['ctm_check_for_sd_card']['change_to_jump'] = {}
# ctm_patch_list['ctm_check_for_sd_card']['change_to_jump']['BTC-7A'] = 'jal.ctm_checkForSDCard'

# ctm_patch_list['ctm_get_power_switch_on_p'] = {}
# ctm_patch_list['ctm_get_power_switch_on_p']['function'] = 'HceTaskRecordingRecStop'
# ctm_patch_list['ctm_get_power_switch_on_p']['line_number'] = {}
# ctm_patch_list['ctm_get_power_switch_on_p']['line_number']['BTC-7A'] = 49
# ctm_patch_list['ctm_get_power_switch_on_p']['start_offset'] = {}
# ctm_patch_list['ctm_get_power_switch_on_p']['start_offset']['BTC-7A'] = 0x0123fc4
# ctm_patch_list['ctm_get_power_switch_on_p']['change_from_jump'] = {}
# ctm_patch_list['ctm_get_power_switch_on_p']['change_from_jump']['BTC-7A'] = 'jal.get_power_switch_on_p'
# ctm_patch_list['ctm_get_power_switch_on_p']['change_to_jump'] = {}
# ctm_patch_list['ctm_get_power_switch_on_p']['change_to_jump']['BTC-7A'] = 'jal.ctm_get_power_switch_on_p'

# ctm_patch_list['ctm_check_hal_low_voltage'] = {}
# ctm_patch_list['ctm_check_hal_low_voltage']['function'] = 'HceTaskRecordingRecStop'
# ctm_patch_list['ctm_check_hal_low_voltage']['line_number'] = {}
# ctm_patch_list['ctm_check_hal_low_voltage']['line_number']['BTC-7A'] = 50
# ctm_patch_list['ctm_check_hal_low_voltage']['start_offset'] = {}
# ctm_patch_list['ctm_check_hal_low_voltage']['start_offset']['BTC-7A'] = 0x0123fd4
# ctm_patch_list['ctm_check_hal_low_voltage']['change_from_jump'] = {}
# ctm_patch_list['ctm_check_hal_low_voltage']['change_from_jump']['BTC-7A'] = 'jal.check_hal_low_voltage'
# ctm_patch_list['ctm_check_hal_low_voltage']['change_to_jump'] = {}
# ctm_patch_list['ctm_check_hal_low_voltage']['change_to_jump']['BTC-7A'] = 'jal.ctm_check_hal_low_voltage'

# Debug
# Figure out where in HceTaskRecordingRecStop were getting aborted

# ctm_patch_list['ctm_get_some_time'] = {}
# ctm_patch_list['ctm_get_some_time']['function'] = 'HceTaskRecordingRecStop'
# ctm_patch_list['ctm_get_some_time']['line_number'] = {}
# ctm_patch_list['ctm_get_some_time']['line_number']['BTC-7A'] = 22
# ctm_patch_list['ctm_get_some_time']['start_offset'] = {}
# ctm_patch_list['ctm_get_some_time']['start_offset']['BTC-7A'] = 0x0123e80
# ctm_patch_list['ctm_get_some_time']['change_from_jump'] = {}
# ctm_patch_list['ctm_get_some_time']['change_from_jump']['BTC-7A'] = 'jal.get_some_system_time'
# ctm_patch_list['ctm_get_some_time']['change_to_jump'] = {}
# ctm_patch_list['ctm_get_some_time']['change_to_jump']['BTC-7A'] = 'jal.ctm_get_some_system_time'

# ctm_patch_list['ctm_get_sd_card_state'] = {}
# ctm_patch_list['ctm_get_sd_card_state']['function'] = 'HceTaskRecordingRecStop'
# ctm_patch_list['ctm_get_sd_card_state']['line_number'] = {}
# ctm_patch_list['ctm_get_sd_card_state']['line_number']['BTC-7A'] = 57
# ctm_patch_list['ctm_get_sd_card_state']['start_offset'] = {}
# ctm_patch_list['ctm_get_sd_card_state']['start_offset']['BTC-7A'] = 0x0124010
# ctm_patch_list['ctm_get_sd_card_state']['change_from_jump'] = {}
# ctm_patch_list['ctm_get_sd_card_state']['change_from_jump']['BTC-7A'] = 'jal.get_SDCardState'
# ctm_patch_list['ctm_get_sd_card_state']['change_to_jump'] = {}
# ctm_patch_list['ctm_get_sd_card_state']['change_to_jump']['BTC-7A'] = 'jal.ctm_get_SDCardState'

# Debug: turn on print statements during firmware load (I hope)

# ctm_patch_list['ctm_icatch_load_fw'] = {}
# ctm_patch_list['ctm_icatch_load_fw']['function'] = 'check_and_load_firmware_file'
# ctm_patch_list['ctm_icatch_load_fw']['line_number'] = {}
# ctm_patch_list['ctm_icatch_load_fw']['line_number']['BTC-7A'] = 11
# ctm_patch_list['ctm_icatch_load_fw']['start_offset'] = {}
# ctm_patch_list['ctm_icatch_load_fw']['start_offset']['BTC-7A'] = 0x01a7050
# ctm_patch_list['ctm_icatch_load_fw']['change_from_jump'] = {}
# ctm_patch_list['ctm_icatch_load_fw']['change_from_jump']['BTC-7A'] = 'j.icatch_isp_load_firmware'
# ctm_patch_list['ctm_icatch_load_fw']['change_to_jump'] = {}
# ctm_patch_list['ctm_icatch_load_fw']['change_to_jump']['BTC-7A'] = 'j.ctm_icatch_isp_load_firmware'


# change the string we check for a valid firmware image; need to change since this
#        is from a BTC-7E baseline
ctm_patch_list['ctm_prometheus_string'] = {}
ctm_patch_list['ctm_prometheus_string']['function'] = 's_Prometheus5BTC70_8036f3b4'   
ctm_patch_list['ctm_prometheus_string']['line_number'] = {}
ctm_patch_list['ctm_prometheus_string']['line_number']['BTC-7A'] = 0
ctm_patch_list['ctm_prometheus_string']['start_offset'] = {}
ctm_patch_list['ctm_prometheus_string']['start_offset']['BTC-7A'] = 0x036f3bc
ctm_patch_list['ctm_prometheus_string']['change_from_bytes'] = {}
ctm_patch_list['ctm_prometheus_string']['change_from_bytes']['BTC-7A'] = bytes([0x75, 0x73, 0x35, 0x42])
ctm_patch_list['ctm_prometheus_string']['change_to_bytes'] = {}
ctm_patch_list['ctm_prometheus_string']['change_to_bytes']['BTC-7A'] = bytes([0x75, 0x73, 0x33, 0x42])

# Hardwire the firmware size into code
ctm_patch_list['ctm_set_g_image_size_512b'] = {}
ctm_patch_list['ctm_set_g_image_size_512b']['function'] = 'load_boot_parameters'   
ctm_patch_list['ctm_set_g_image_size_512b']['line_number'] = {}
ctm_patch_list['ctm_set_g_image_size_512b']['line_number']['BTC-7A'] = 93
ctm_patch_list['ctm_set_g_image_size_512b']['start_offset'] = {}
ctm_patch_list['ctm_set_g_image_size_512b']['start_offset']['BTC-7A'] = 0x0000b4c
ctm_patch_list['ctm_set_g_image_size_512b']['change_from_bytes'] = {}
ctm_patch_list['ctm_set_g_image_size_512b']['change_from_bytes']['BTC-7A'] = bytes([0x00, 0x00, 0x00, 0x00])
ctm_patch_list['ctm_set_g_image_size_512b']['change_to_bytes'] = {}
ctm_patch_list['ctm_set_g_image_size_512b']['change_to_bytes']['BTC-7A'] = bytes([0xf4, 0x1d, 0x00, 0x00])

# Clobber the instruction that would normalize overwrite the loaded verson of firmware size
ctm_patch_list['ctm_store_g_image_size_512b'] = {}
ctm_patch_list['ctm_store_g_image_size_512b']['function'] = 'load_boot_parameters'   
ctm_patch_list['ctm_store_g_image_size_512b']['line_number'] = {}
ctm_patch_list['ctm_store_g_image_size_512b']['line_number']['BTC-7A'] = 93
ctm_patch_list['ctm_store_g_image_size_512b']['start_offset'] = {}
ctm_patch_list['ctm_store_g_image_size_512b']['start_offset']['BTC-7A'] = 0x0930
ctm_patch_list['ctm_store_g_image_size_512b']['change_from_bytes'] = {}
ctm_patch_list['ctm_store_g_image_size_512b']['change_from_bytes']['BTC-7A'] = bytes([0x4c, 0x0b, 0x44, 0xac])
ctm_patch_list['ctm_store_g_image_size_512b']['change_to_bytes'] = {}
ctm_patch_list['ctm_store_g_image_size_512b']['change_to_bytes']['BTC-7A'] = bytes([0x00, 0x00, 0x00, 0x00])

# Hardwire the firmware size into code #
ctm_patch_list['ctm_set_g_image_size_256b'] = {}
ctm_patch_list['ctm_set_g_image_size_256b']['function'] = 'load_boot_parameters'   
ctm_patch_list['ctm_set_g_image_size_256b']['line_number'] = {}
ctm_patch_list['ctm_set_g_image_size_256b']['line_number']['BTC-7A'] = 93
ctm_patch_list['ctm_set_g_image_size_256b']['start_offset'] = {}
ctm_patch_list['ctm_set_g_image_size_256b']['start_offset']['BTC-7A'] = 0x0000b64
ctm_patch_list['ctm_set_g_image_size_256b']['change_from_bytes'] = {}
ctm_patch_list['ctm_set_g_image_size_256b']['change_from_bytes']['BTC-7A'] = bytes([0x00, 0x00, 0x00, 0x00])
ctm_patch_list['ctm_set_g_image_size_256b']['change_to_bytes'] = {}
ctm_patch_list['ctm_set_g_image_size_256b']['change_to_bytes']['BTC-7A'] = bytes([0xe8, 0x3b, 0x00, 0x00])

# Clobber the instruction that would normalize overwrite the loaded verson of raw firmware size
ctm_patch_list['ctm_store_g_image_size_256b'] = {}
ctm_patch_list['ctm_store_g_image_size_256b']['function'] = 'load_boot_parameters'
ctm_patch_list['ctm_store_g_image_size_256b']['line_number'] = {}
ctm_patch_list['ctm_store_g_image_size_256b']['line_number']['BTC-7A'] = 87
ctm_patch_list['ctm_store_g_image_size_256b']['start_offset'] = {}
ctm_patch_list['ctm_store_g_image_size_256b']['start_offset']['BTC-7A'] = 0x0920
ctm_patch_list['ctm_store_g_image_size_256b']['change_from_bytes'] = {}
ctm_patch_list['ctm_store_g_image_size_256b']['change_from_bytes']['BTC-7A'] = bytes([0x64, 0x0b, 0x44, 0xac])
ctm_patch_list['ctm_store_g_image_size_256b']['change_to_bytes'] = {}
ctm_patch_list['ctm_store_g_image_size_256b']['change_to_bytes']['BTC-7A'] = bytes([0x00, 0x00, 0x00, 0x00])

# Use an existing printf to see if we can observe
# g_image_size and g_raw_image_size
ctm_patch_list['ctm_bk_ok_string'] = {}
ctm_patch_list['ctm_bk_ok_string']['function'] = 'handle_firmware_load_exception'
ctm_patch_list['ctm_bk_ok_string']['line_number'] = {}
ctm_patch_list['ctm_bk_ok_string']['line_number']['BTC-7A'] = 109
ctm_patch_list['ctm_bk_ok_string']['start_offset'] = {}
ctm_patch_list['ctm_bk_ok_string']['start_offset']['BTC-7A'] = 0x000064c
ctm_patch_list['ctm_bk_ok_string']['change_from_bytes'] = {}
ctm_patch_list['ctm_bk_ok_string']['change_from_bytes']['BTC-7A'] = bytes([0x09, 0xf8, 0x40, 0x00,
									   0x00, 0x00, 0x00, 0x00,
									   0x21, 0x28, 0x40, 0x00])
ctm_patch_list['ctm_bk_ok_string']['change_to_bytes'] = {}
ctm_patch_list['ctm_bk_ok_string']['change_to_bytes']['BTC-7A'] = bytes([0x00, 0x80, 0x05, 0x3c,
									 0x64, 0x0b, 0xa5, 0x24,
									 0x00, 0x00, 0xa5, 0x8c])

# Clobber the instruction that would normally overwrite the loaded verson of raw firmware size
ctm_patch_list['ctm_bk_ok_string_hex'] = {}
ctm_patch_list['ctm_bk_ok_string_hex']['function'] = '0x80000aa0'
ctm_patch_list['ctm_bk_ok_string_hex']['line_number'] = {}
ctm_patch_list['ctm_bk_ok_string_hex']['line_number']['BTC-7A'] = 4
ctm_patch_list['ctm_bk_ok_string_hex']['start_offset'] = {}
ctm_patch_list['ctm_bk_ok_string_hex']['start_offset']['BTC-7A'] = 0x0aa4
ctm_patch_list['ctm_bk_ok_string_hex']['change_from_bytes'] = {}
ctm_patch_list['ctm_bk_ok_string_hex']['change_from_bytes']['BTC-7A'] = bytes([0x4b, 0x28, 0x25, 0x64])
ctm_patch_list['ctm_bk_ok_string_hex']['change_to_bytes'] = {}
ctm_patch_list['ctm_bk_ok_string_hex']['change_to_bytes']['BTC-7A'] = bytes([0x4b, 0x28, 0x25, 0x78])

# Debug by Crash 

# Place this patch anywhere you want to cause the system to crash by jumping to a null address
# ctm_patch_list['crash_debug'] = {}
# ctm_patch_list['crash_debug']['function'] = 'handle_firmware_load_exception'
# ctm_patch_list['crash_debug']['line_number'] = {}
# ctm_patch_list['crash_debug']['line_number']['BTC-7A'] = 114
# ctm_patch_list['crash_debug']['start_offset'] = {}
# ctm_patch_list['crash_debug']['start_offset']['BTC-7A'] = 0x68c
# ctm_patch_list['crash_debug']['change_from_bytes'] = {}
# ctm_patch_list['crash_debug']['change_from_bytes']['BTC-7A'] = bytes([0xb6, 0x01, 0x00, 0x08])
# ctm_patch_list['crash_debug']['change_to_bytes'] = {}
# ctm_patch_list['crash_debug']['change_to_bytes']['BTC-7A'] = bytes([0x00, 0x00, 0x00, 0x08])

## Native Photo Resolution Setting in Photo Quality Menu
# Patching in the new Menu
npr_patch_list = {}

npr_patch_list['npr_new_resolution_lookup_table'] = {}
npr_patch_list['npr_new_resolution_lookup_table']['function'] = 'draw_photo_resolution_on_screen'
npr_patch_list['npr_new_resolution_lookup_table']['line_number'] = {}
npr_patch_list['npr_new_resolution_lookup_table']['line_number']['BTC-7A'] = 30
npr_patch_list['npr_new_resolution_lookup_table']['line_number']['BTC-7E'] = 30
npr_patch_list['npr_new_resolution_lookup_table']['line_number']['BTC-8E'] = 38
npr_patch_list['npr_new_resolution_lookup_table']['line_number']['BTC-7E-HP4'] = 40
npr_patch_list['npr_new_resolution_lookup_table']['line_number']['BTC-8E-HP4'] = 40
npr_patch_list['npr_new_resolution_lookup_table']['line_number']['BTC-7E-HP5'] = 38
npr_patch_list['npr_new_resolution_lookup_table']['line_number']['BTC-8E-HP5'] = 40
npr_patch_list['npr_new_resolution_lookup_table']['start_offset'] = {}
npr_patch_list['npr_new_resolution_lookup_table']['start_offset']['BTC-7A'] = 0x011f2c0
npr_patch_list['npr_new_resolution_lookup_table']['start_offset']['BTC-7E'] = 0x011f2c0
npr_patch_list['npr_new_resolution_lookup_table']['start_offset']['BTC-8E'] = 0x011f5b8
npr_patch_list['npr_new_resolution_lookup_table']['start_offset']['BTC-7E-HP4'] = 0x011addc
npr_patch_list['npr_new_resolution_lookup_table']['start_offset']['BTC-8E-HP4'] = 0x011b1bc
npr_patch_list['npr_new_resolution_lookup_table']['start_offset']['BTC-7E-HP5'] = 0x00f9d14
npr_patch_list['npr_new_resolution_lookup_table']['start_offset']['BTC-8E-HP5'] = 0x00f9c40
npr_patch_list['npr_new_resolution_lookup_table']['change_from_jump'] = 'jal.draw_sst_string_on_display'
npr_patch_list['npr_new_resolution_lookup_table']['change_to_jump']   = 'jal.npr_draw_sst_string_on_display'

# And the size
npr_patch_list['npr_new_menu_size'] = {}
npr_patch_list['npr_new_menu_size']['function'] = 'g_camera_setup_selector_array'
npr_patch_list['npr_new_menu_size']['line_number'] = {}
npr_patch_list['npr_new_menu_size']['line_number']['BTC-7A'] = 2
npr_patch_list['npr_new_menu_size']['line_number']['BTC-7E'] = 2
npr_patch_list['npr_new_menu_size']['line_number']['BTC-8E'] = 2
npr_patch_list['npr_new_menu_size']['line_number']['BTC-7E-HP4'] = 2
npr_patch_list['npr_new_menu_size']['line_number']['BTC-8E-HP4'] = 2
npr_patch_list['npr_new_menu_size']['line_number']['BTC-7E-HP5'] = 2
npr_patch_list['npr_new_menu_size']['line_number']['BTC-8E-HP5'] = 2
npr_patch_list['npr_new_menu_size']['start_offset'] = {}
npr_patch_list['npr_new_menu_size']['start_offset']['BTC-7A'] = 0x0355440
npr_patch_list['npr_new_menu_size']['start_offset']['BTC-7E'] = 0x0355440
npr_patch_list['npr_new_menu_size']['start_offset']['BTC-8E'] = 0x0355498
npr_patch_list['npr_new_menu_size']['start_offset']['BTC-7E-HP4'] = 0x0358498
npr_patch_list['npr_new_menu_size']['start_offset']['BTC-8E-HP4'] = 0x035c6c8
npr_patch_list['npr_new_menu_size']['start_offset']['BTC-7E-HP5'] = 0x02cdf0c
npr_patch_list['npr_new_menu_size']['start_offset']['BTC-8E-HP5'] = 0x02d00cc
npr_patch_list['npr_new_menu_size']['change_from_bytes']  =  bytes([0x05, 0x00, 0x00, 0x00])
npr_patch_list['npr_new_menu_size']['change_to_bytes']    =  bytes([0x06, 0x00, 0x00, 0x00])

# hijacking the call to get_camera_photo_resolution
npr_patch_list['npr_get_camera_photo_resolution'] = {}
npr_patch_list['npr_get_camera_photo_resolution']['function'] = 'get_camera_photo_resolution'
npr_patch_list['npr_get_camera_photo_resolution']['line_number'] = {}
npr_patch_list['npr_get_camera_photo_resolution']['line_number']['BTC-7A'] = 0
npr_patch_list['npr_get_camera_photo_resolution']['line_number']['BTC-7E'] = 0
npr_patch_list['npr_get_camera_photo_resolution']['line_number']['BTC-8E'] = 0
npr_patch_list['npr_get_camera_photo_resolution']['line_number']['BTC-7E-HP4'] = 0
npr_patch_list['npr_get_camera_photo_resolution']['line_number']['BTC-8E-HP4'] = 0
npr_patch_list['npr_get_camera_photo_resolution']['line_number']['BTC-7E-HP5'] = 0
npr_patch_list['npr_get_camera_photo_resolution']['line_number']['BTC-8E-HP5'] = 0
npr_patch_list['npr_get_camera_photo_resolution']['start_offset'] = {}
npr_patch_list['npr_get_camera_photo_resolution']['start_offset']['BTC-7A'] = 0x010ff9c
npr_patch_list['npr_get_camera_photo_resolution']['start_offset']['BTC-7E'] = 0x010ff9c
npr_patch_list['npr_get_camera_photo_resolution']['start_offset']['BTC-8E'] = 0x01101cc
npr_patch_list['npr_get_camera_photo_resolution']['start_offset']['BTC-7E-HP4'] = 0x010b3b8
npr_patch_list['npr_get_camera_photo_resolution']['start_offset']['BTC-8E-HP4'] = 0x010b8b8
npr_patch_list['npr_get_camera_photo_resolution']['start_offset']['BTC-7E-HP5'] = 0x00e7c4c
npr_patch_list['npr_get_camera_photo_resolution']['start_offset']['BTC-8E-HP5'] = 0x00e7d08
npr_patch_list['npr_get_camera_photo_resolution']['change_from_bytes']  = {}
npr_patch_list['npr_get_camera_photo_resolution']['change_from_bytes']['BTC-7A']     = bytes([0x35, 0x80, 0x03, 0x3c])
npr_patch_list['npr_get_camera_photo_resolution']['change_from_bytes']['BTC-7E']     = bytes([0x35, 0x80, 0x03, 0x3c])
npr_patch_list['npr_get_camera_photo_resolution']['change_from_bytes']['BTC-8E']     = bytes([0x35, 0x80, 0x03, 0x3c])
npr_patch_list['npr_get_camera_photo_resolution']['change_from_bytes']['BTC-7E-HP4'] = bytes([0x35, 0x80, 0x03, 0x3c])
npr_patch_list['npr_get_camera_photo_resolution']['change_from_bytes']['BTC-8E-HP4'] = bytes([0x36, 0x80, 0x03, 0x3c])
npr_patch_list['npr_get_camera_photo_resolution']['change_from_bytes']['BTC-7E-HP5'] = bytes([0x2d, 0x80, 0x03, 0x3c])
npr_patch_list['npr_get_camera_photo_resolution']['change_from_bytes']['BTC-8E-HP5'] = bytes([0x2d, 0x80, 0x03, 0x3c])
npr_patch_list['npr_get_camera_photo_resolution']['change_to_jump']    =  'j.ntvq_get_camera_photo_resolution'

## White flash
##  calls to turn on a white flash when camera is set to "no light" (all color), and not "flash power off"
wfl_patch_list = {}

wfl_patch_list['wfl_hce_task_view_init_photo'] = {}
wfl_patch_list['wfl_hce_task_view_init_photo']['function'] = 'HceTaskView_Init'
wfl_patch_list['wfl_hce_task_view_init_photo']['line_number'] = {}
wfl_patch_list['wfl_hce_task_view_init_photo']['line_number']['BTC-7A'] = 18
wfl_patch_list['wfl_hce_task_view_init_photo']['line_number']['BTC-7E'] = 18
wfl_patch_list['wfl_hce_task_view_init_photo']['line_number']['BTC-8E'] = 18
wfl_patch_list['wfl_hce_task_view_init_photo']['line_number']['BTC-7E-HP4'] = 24
wfl_patch_list['wfl_hce_task_view_init_photo']['line_number']['BTC-8E-HP4'] = 24
wfl_patch_list['wfl_hce_task_view_init_photo']['line_number']['BTC-7E-HP5'] = 24
wfl_patch_list['wfl_hce_task_view_init_photo']['line_number']['BTC-8E-HP5'] = 24
wfl_patch_list['wfl_hce_task_view_init_photo']['start_offset'] = {}
wfl_patch_list['wfl_hce_task_view_init_photo']['start_offset']['BTC-7A'] = 0x012ac28
wfl_patch_list['wfl_hce_task_view_init_photo']['start_offset']['BTC-7E'] = 0x012ac28
wfl_patch_list['wfl_hce_task_view_init_photo']['start_offset']['BTC-8E'] = 0x012afc8
wfl_patch_list['wfl_hce_task_view_init_photo']['start_offset']['BTC-7E-HP4'] = 0x0127354
wfl_patch_list['wfl_hce_task_view_init_photo']['start_offset']['BTC-8E-HP4'] = 0x012788c
wfl_patch_list['wfl_hce_task_view_init_photo']['start_offset']['BTC-7E-HP5'] = 0x010a84c
wfl_patch_list['wfl_hce_task_view_init_photo']['start_offset']['BTC-8E-HP5'] = 0x010a8fc
wfl_patch_list['wfl_hce_task_view_init_photo']['change_from_jump']  =  'jal.setSensorDigitalEffectPhoto'
wfl_patch_list['wfl_hce_task_view_init_photo']['change_to_jump']    =  'jal.wfl_setSensorDigitalEffectPhoto'


wfl_patch_list['wfl_hce_task_view_init_video'] = {}
wfl_patch_list['wfl_hce_task_view_init_video']['function'] = 'HceTaskView_Init'
wfl_patch_list['wfl_hce_task_view_init_video']['line_number'] = {}
wfl_patch_list['wfl_hce_task_view_init_video']['line_number']['BTC-7A'] = 27
wfl_patch_list['wfl_hce_task_view_init_video']['line_number']['BTC-7E'] = 27
wfl_patch_list['wfl_hce_task_view_init_video']['line_number']['BTC-8E'] = 27
wfl_patch_list['wfl_hce_task_view_init_video']['line_number']['BTC-7E-HP4'] = 34
wfl_patch_list['wfl_hce_task_view_init_video']['line_number']['BTC-8E-HP4'] = 34
wfl_patch_list['wfl_hce_task_view_init_video']['line_number']['BTC-7E-HP5'] = 34
wfl_patch_list['wfl_hce_task_view_init_video']['line_number']['BTC-8E-HP5'] = 34
wfl_patch_list['wfl_hce_task_view_init_video']['start_offset'] = {}
wfl_patch_list['wfl_hce_task_view_init_video']['start_offset']['BTC-7A'] = 0x012abe8
wfl_patch_list['wfl_hce_task_view_init_video']['start_offset']['BTC-7E'] = 0x012abe8
wfl_patch_list['wfl_hce_task_view_init_video']['start_offset']['BTC-8E'] = 0x012af88
wfl_patch_list['wfl_hce_task_view_init_video']['start_offset']['BTC-7E-HP4'] = 0x01272f4
wfl_patch_list['wfl_hce_task_view_init_video']['start_offset']['BTC-8E-HP4'] = 0x012782c
wfl_patch_list['wfl_hce_task_view_init_video']['start_offset']['BTC-7E-HP5'] = 0x010a7ec
wfl_patch_list['wfl_hce_task_view_init_video']['start_offset']['BTC-8E-HP5'] = 0x010a89c
wfl_patch_list['wfl_hce_task_view_init_video']['change_from_jump']  =  'jal.setSensorDigitalEffectVideo'
wfl_patch_list['wfl_hce_task_view_init_video']['change_to_jump']    =  'jal.wfl_setSensorDigitalEffectVideo'

wfl_patch_list['wfl_video_configure_sensor'] = {}
wfl_patch_list['wfl_video_configure_sensor']['function'] = 'videoConfigureSensor'
wfl_patch_list['wfl_video_configure_sensor']['line_number'] = {}
wfl_patch_list['wfl_video_configure_sensor']['line_number']['BTC-7A'] = 37
wfl_patch_list['wfl_video_configure_sensor']['line_number']['BTC-7E'] = 37
wfl_patch_list['wfl_video_configure_sensor']['line_number']['BTC-8E'] = 37
wfl_patch_list['wfl_video_configure_sensor']['line_number']['BTC-7E-HP4'] = 37
wfl_patch_list['wfl_video_configure_sensor']['line_number']['BTC-8E-HP4'] = 37
wfl_patch_list['wfl_video_configure_sensor']['line_number']['BTC-7E-HP5'] = 37
wfl_patch_list['wfl_video_configure_sensor']['line_number']['BTC-8E-HP5'] = 37
wfl_patch_list['wfl_video_configure_sensor']['start_offset'] = {}
wfl_patch_list['wfl_video_configure_sensor']['start_offset']['BTC-7A'] = 0x0110eb0
wfl_patch_list['wfl_video_configure_sensor']['start_offset']['BTC-7E'] = 0x0110eb0
wfl_patch_list['wfl_video_configure_sensor']['start_offset']['BTC-8E'] = 0x0111128
wfl_patch_list['wfl_video_configure_sensor']['start_offset']['BTC-7E-HP4'] = 0x010c34c
wfl_patch_list['wfl_video_configure_sensor']['start_offset']['BTC-8E-HP4'] = 0x010c84c
wfl_patch_list['wfl_video_configure_sensor']['start_offset']['BTC-7E-HP5'] = 0x00e8bc4
wfl_patch_list['wfl_video_configure_sensor']['start_offset']['BTC-8E-HP5'] = 0x00e8c80
wfl_patch_list['wfl_video_configure_sensor']['change_from_jump']  =  'jal.setSensorDigitalEffectVideo'
wfl_patch_list['wfl_video_configure_sensor']['change_to_jump']    =  'jal.wfl_setSensorDigitalEffectVideo'


## HceIRCut_SetIRCutOpen() patches
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit'] = {}
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['function'] = 'HceTaskRecording_RecVideoInit'
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['line_number'] = {}
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['line_number']['BTC-7A'] = 98
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['line_number']['BTC-7E'] = 98
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['line_number']['BTC-8E'] = 105
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['line_number']['BTC-7E-HP4'] = 102
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['line_number']['BTC-8E-HP4'] = 109
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['line_number']['BTC-7E-HP5'] = 124
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['line_number']['BTC-8E-HP5'] = 123
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['start_offset'] = {}
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['start_offset']['BTC-7A'] = 0x0125508
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['start_offset']['BTC-7E'] = 0x0125508
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['start_offset']['BTC-8E'] = 0x01258c0
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['start_offset']['BTC-7E-HP4'] = 0x0121480
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['start_offset']['BTC-8E-HP4'] = 0x01219d0
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['start_offset']['BTC-7E-HP5'] = 0x0104940
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['start_offset']['BTC-8E-HP5'] = 0x0104a08
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['change_from_jump']  =  'jal.HceIRCut_SetIRCutOpen'
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit']['change_to_jump']    =  'jal.wfl_HceIRCut_SetIRCutOpen'


## HceIRCut_SetIRCutOpen() patches
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug'] = {}
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['function'] = 'HceTaskRecording_RecVideoInit'
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['line_number'] = {}
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['line_number']['BTC-7A'] = 21
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['line_number']['BTC-7E'] = 21
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['line_number']['BTC-8E'] = 21
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['line_number']['BTC-7E-HP4'] = 16
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['line_number']['BTC-8E-HP4'] = 19
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['line_number']['BTC-7E-HP5'] = 16
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['line_number']['BTC-8E-HP5'] = 15
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['start_offset'] = {}
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['start_offset']['BTC-7A'] = 0x01252e8
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['start_offset']['BTC-7E'] = 0x01252e8
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['start_offset']['BTC-8E'] = 0x01256a0
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['start_offset']['BTC-7E-HP4'] = 0x0121244
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['start_offset']['BTC-8E-HP4'] = 0x0121794
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['start_offset']['BTC-7E-HP5'] = 0x010467c
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['start_offset']['BTC-8E-HP5'] = 0x010474c
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['change_from_jump']  =  'jal.log_printf'
wfl_patch_list['wfl_HceTaskRecording_RecVideoInit_debug']['change_to_jump']    =  'jal.wfl_video_log_printf'

wfl_patch_list['wfl_HceTaskStill_WaitView'] = {}
wfl_patch_list['wfl_HceTaskStill_WaitView']['function'] = 'HceTaskStill_WaitView'
wfl_patch_list['wfl_HceTaskStill_WaitView']['line_number'] = {}
wfl_patch_list['wfl_HceTaskStill_WaitView']['line_number']['BTC-7A'] = 44
wfl_patch_list['wfl_HceTaskStill_WaitView']['line_number']['BTC-7E'] = 44
wfl_patch_list['wfl_HceTaskStill_WaitView']['line_number']['BTC-8E'] = 44
wfl_patch_list['wfl_HceTaskStill_WaitView']['line_number']['BTC-7E-HP4'] = 44
wfl_patch_list['wfl_HceTaskStill_WaitView']['line_number']['BTC-8E-HP4'] = 44
wfl_patch_list['wfl_HceTaskStill_WaitView']['line_number']['BTC-7E-HP5'] = 44
wfl_patch_list['wfl_HceTaskStill_WaitView']['line_number']['BTC-8E-HP5'] = 44
wfl_patch_list['wfl_HceTaskStill_WaitView']['start_offset'] = {}
wfl_patch_list['wfl_HceTaskStill_WaitView']['start_offset']['BTC-7A'] = 0x0126380
wfl_patch_list['wfl_HceTaskStill_WaitView']['start_offset']['BTC-7E'] = 0x0126380
wfl_patch_list['wfl_HceTaskStill_WaitView']['start_offset']['BTC-8E'] = 0x0126730
wfl_patch_list['wfl_HceTaskStill_WaitView']['start_offset']['BTC-7E-HP4'] = 0x0122998
wfl_patch_list['wfl_HceTaskStill_WaitView']['start_offset']['BTC-8E-HP4'] = 0x0122ee0
wfl_patch_list['wfl_HceTaskStill_WaitView']['start_offset']['BTC-7E-HP5'] = 0x0105dfc
wfl_patch_list['wfl_HceTaskStill_WaitView']['start_offset']['BTC-8E-HP5'] = 0x0105ebc
wfl_patch_list['wfl_HceTaskStill_WaitView']['change_from_jump']  =  'jal.HceIRCut_SetIRCutOpen'
wfl_patch_list['wfl_HceTaskStill_WaitView']['change_to_jump']    =  'jal.wfl_HceIRCut_SetIRCutOpen'

wfl_patch_list['wfl_HceTaskStillBurst_task2'] = {}
wfl_patch_list['wfl_HceTaskStillBurst_task2']['function'] = 'HceTaskStillBurst_task2'
wfl_patch_list['wfl_HceTaskStillBurst_task2']['line_number'] = {}
wfl_patch_list['wfl_HceTaskStillBurst_task2']['line_number']['BTC-7A'] = 44
wfl_patch_list['wfl_HceTaskStillBurst_task2']['line_number']['BTC-7E'] = 44
wfl_patch_list['wfl_HceTaskStillBurst_task2']['line_number']['BTC-8E'] = 44
wfl_patch_list['wfl_HceTaskStillBurst_task2']['line_number']['BTC-7E-HP4'] = 45
wfl_patch_list['wfl_HceTaskStillBurst_task2']['line_number']['BTC-8E-HP4'] = 45
wfl_patch_list['wfl_HceTaskStillBurst_task2']['line_number']['BTC-7E-HP5'] = 45
wfl_patch_list['wfl_HceTaskStillBurst_task2']['line_number']['BTC-8E-HP5'] = 45
wfl_patch_list['wfl_HceTaskStillBurst_task2']['start_offset'] = {}
wfl_patch_list['wfl_HceTaskStillBurst_task2']['start_offset']['BTC-7A'] = 0x0126380
wfl_patch_list['wfl_HceTaskStillBurst_task2']['start_offset']['BTC-7E'] = 0x0126380
wfl_patch_list['wfl_HceTaskStillBurst_task2']['start_offset']['BTC-8E'] = 0x0128594
wfl_patch_list['wfl_HceTaskStillBurst_task2']['start_offset']['BTC-7E-HP4'] = 0x01248c8
wfl_patch_list['wfl_HceTaskStillBurst_task2']['start_offset']['BTC-8E-HP4'] = 0x0124e08
wfl_patch_list['wfl_HceTaskStillBurst_task2']['start_offset']['BTC-7E-HP5'] = 0x0107dc4
wfl_patch_list['wfl_HceTaskStillBurst_task2']['start_offset']['BTC-8E-HP5'] = 0x0107e7c
wfl_patch_list['wfl_HceTaskStillBurst_task2']['change_from_jump']  =  'jal.HceIRCut_SetIRCutOpen'
wfl_patch_list['wfl_HceTaskStillBurst_task2']['change_to_jump']    =  'jal.wfl_HceIRCut_SetIRCutOpen'

wfl_patch_list['wfl_ModeAuto2_FSM_Task5'] = {}
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['function'] = 'ModeAuto2_FSM_Task5'
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['line_number'] = {}
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['line_number']['BTC-7A'] = 26
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['line_number']['BTC-7E'] = 26
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['line_number']['BTC-8E'] = 26
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['line_number']['BTC-7E-HP4'] = 28
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['line_number']['BTC-8E-HP4'] = 26
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['line_number']['BTC-7E-HP5'] = 26
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['line_number']['BTC-8E-HP5'] = 26
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['start_offset'] = {}
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['start_offset']['BTC-7A'] = 0x012df2c
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['start_offset']['BTC-7E'] = 0x012df2c
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['start_offset']['BTC-8E'] = 0x012eb00
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['start_offset']['BTC-7E-HP4'] = 0x012a85c
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['start_offset']['BTC-8E-HP4'] = 0x012d384
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['start_offset']['BTC-7E-HP5'] = 0x010d668
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['start_offset']['BTC-8E-HP5'] = 0x010dfb8
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['change_from_jump']  =  'jal.HceIRCut_SetIRCutOpen'
wfl_patch_list['wfl_ModeAuto2_FSM_Task5']['change_to_jump']    =  'jal.wfl_HceIRCut_SetIRCutOpen'

##
## Debugging SD Card Corruption
## These patches are for debugging only; not for release

fdb_patch_list = {}

# Loop through lots of Format/Mount 
fdb_patch_list['format_fsm'] = {}
fdb_patch_list['format_fsm']['function'] = 'g_HceTaskMenuMultiItem_fsm_function_array'
fdb_patch_list['format_fsm']['line_number'] = {}
fdb_patch_list['format_fsm']['line_number']['BTC-8E-HP5'] = 23
fdb_patch_list['format_fsm']['start_offset'] = {}
fdb_patch_list['format_fsm']['start_offset']['BTC-8E-HP5'] = 0x02cff60
fdb_patch_list['format_fsm']['change_from_ptr'] = 'handleDeleteAll_menu'
fdb_patch_list['format_fsm']['change_to_ptr']   = 'fdb_handleDeleteAll_menu'

#Debug -- FSM Start
fdb_patch_list['format_fsm_0'] = {}
fdb_patch_list['format_fsm_0']['function'] = 'g_HCETaskFormat_FunctionArray'
fdb_patch_list['format_fsm_0']['line_number'] = {}
fdb_patch_list['format_fsm_0']['line_number']['BTC-8E-HP5'] = 0
fdb_patch_list['format_fsm_0']['start_offset'] = {}
fdb_patch_list['format_fsm_0']['start_offset']['BTC-8E-HP5'] = 0x02cf69c
fdb_patch_list['format_fsm_0']['change_from_ptr'] = 'HceTaskFormat_task0'
fdb_patch_list['format_fsm_0']['change_to_ptr']   = 'fdb_HceTaskFormat_task0'

#Debug -- FSM Start
fdb_patch_list['format_fsm_1'] = {}
fdb_patch_list['format_fsm_1']['function'] = 'g_HCETaskFormat_FunctionArray'
fdb_patch_list['format_fsm_1']['line_number'] = {}
fdb_patch_list['format_fsm_1']['line_number']['BTC-8E-HP5'] = 1
fdb_patch_list['format_fsm_1']['start_offset'] = {}
fdb_patch_list['format_fsm_1']['start_offset']['BTC-8E-HP5'] = 0x02cf6a0
fdb_patch_list['format_fsm_1']['change_from_ptr'] = 'HceTaskFormat_task1_Mount'
fdb_patch_list['format_fsm_1']['change_to_ptr']   = 'fdb_HceTaskFormat_task1_Mount'

#Debug -- FSM Start
fdb_patch_list['format_fsm_2'] = {}
fdb_patch_list['format_fsm_2']['function'] = 'g_HCETaskFormat_FunctionArray'
fdb_patch_list['format_fsm_2']['line_number'] = {}
fdb_patch_list['format_fsm_2']['line_number']['BTC-8E-HP5'] = 2
fdb_patch_list['format_fsm_2']['start_offset'] = {}
fdb_patch_list['format_fsm_2']['start_offset']['BTC-8E-HP5'] = 0x02cf6a4
fdb_patch_list['format_fsm_2']['change_from_ptr'] = 'HceTaskFormat_task2_mount_complete'
fdb_patch_list['format_fsm_2']['change_to_ptr']   = 'fdb_HceTaskFormat_task2_mount_complete'

#Debug -- FSM Start
fdb_patch_list['format_fsm_3'] = {}
fdb_patch_list['format_fsm_3']['function'] = 'g_HCETaskFormat_FunctionArray'
fdb_patch_list['format_fsm_3']['line_number'] = {}
fdb_patch_list['format_fsm_3']['line_number']['BTC-8E-HP5'] = 3
fdb_patch_list['format_fsm_3']['start_offset'] = {}
fdb_patch_list['format_fsm_3']['start_offset']['BTC-8E-HP5'] = 0x02cf6a8
fdb_patch_list['format_fsm_3']['change_from_ptr'] = 'HceTaskFormat_task3_format_drive'
fdb_patch_list['format_fsm_3']['change_to_ptr']   = 'fdb_HceTaskFormat_task3_format_drive'

#Debug -- FSM Start
fdb_patch_list['format_fsm_4'] = {}
fdb_patch_list['format_fsm_4']['function'] = 'g_HCETaskFormat_FunctionArray'
fdb_patch_list['format_fsm_4']['line_number'] = {}
fdb_patch_list['format_fsm_4']['line_number']['BTC-8E-HP5'] = 4
fdb_patch_list['format_fsm_4']['start_offset'] = {}
fdb_patch_list['format_fsm_4']['start_offset']['BTC-8E-HP5'] = 0x02cf6ac
fdb_patch_list['format_fsm_4']['change_from_ptr'] = 'HceTaskFormat_task4_Init_DCF'
fdb_patch_list['format_fsm_4']['change_to_ptr']   = 'fdb_HceTaskFormat_task4_Init_DCF'

#Debug -- FSM Start
fdb_patch_list['format_fsm_5'] = {}
fdb_patch_list['format_fsm_5']['function'] = 'g_HCETaskFormat_FunctionArray'
fdb_patch_list['format_fsm_5']['line_number'] = {}
fdb_patch_list['format_fsm_5']['line_number']['BTC-8E-HP5'] = 5
fdb_patch_list['format_fsm_5']['start_offset'] = {}
fdb_patch_list['format_fsm_5']['start_offset']['BTC-8E-HP5'] = 0x02cf6b0
fdb_patch_list['format_fsm_5']['change_from_ptr'] = 'HceTaskFormat_task5'
fdb_patch_list['format_fsm_5']['change_to_ptr']   = 'fdb_HceTaskFormat_task5'


#Debug -- FSM End
fdb_patch_list['format_fsm_6'] = {}
fdb_patch_list['format_fsm_6']['function'] = 'g_HCETaskFormat_FunctionArray'
fdb_patch_list['format_fsm_6']['line_number'] = {}
fdb_patch_list['format_fsm_6']['line_number']['BTC-8E-HP5'] = 6
fdb_patch_list['format_fsm_6']['start_offset'] = {}
fdb_patch_list['format_fsm_6']['start_offset']['BTC-8E-HP5'] = 0x02cf6b4
fdb_patch_list['format_fsm_6']['change_from_ptr'] = 'HceTaskFormat_task6'
fdb_patch_list['format_fsm_6']['change_to_ptr']   = 'fdb_HceTaskFormat_task6'

