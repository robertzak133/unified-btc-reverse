	.file	1 "menus.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	menus_handleCommitUpdates_menu
	.set	nomips16
	.set	nomicromips
	.ent	menus_handleCommitUpdates_menu
	.type	menus_handleCommitUpdates_menu, @function
menus_handleCommitUpdates_menu:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	handleCommitUpdates_menu
	nop

	.set	macro
	.set	reorder
	.end	menus_handleCommitUpdates_menu
	.size	menus_handleCommitUpdates_menu, .-menus_handleCommitUpdates_menu
	.align	2
	.globl	menus_execute_if_not_null
	.set	nomips16
	.set	nomicromips
	.ent	menus_execute_if_not_null
	.type	menus_execute_if_not_null, @function
menus_execute_if_not_null:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	sltu	$2,$4,30
	beql	$2,$0,$L3
	addiu	$4,$4,-30

	lui	$2,%hi(g_HceTaskMenuMultiItem_fsm_function_array)
	sll	$4,$4,2
	addiu	$2,$2,%lo(g_HceTaskMenuMultiItem_fsm_function_array)
$L5:
	addu	$4,$4,$2
	j	execute_if_not_null
	lw	$4,0($4)

$L3:
	lui	$2,%hi(g_wbwl_menu_handler_function_array_extensions)
	sll	$4,$4,2
	b	$L5
	addiu	$2,$2,%lo(g_wbwl_menu_handler_function_array_extensions)

	.set	macro
	.set	reorder
	.end	menus_execute_if_not_null
	.size	menus_execute_if_not_null, .-menus_execute_if_not_null
	.align	2
	.globl	wbwl_get_next_state_from_menu_enter
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_get_next_state_from_menu_enter
	.type	wbwl_get_next_state_from_menu_enter, @function
wbwl_get_next_state_from_menu_enter:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$3,%hi(g_wbwl_camera_setup_selector_array)
	sll	$2,$4,3
	addiu	$3,$3,%lo(g_wbwl_camera_setup_selector_array)
	addu	$2,$3,$2
	lw	$6,4($2)
	j	get_next_state_from_menu_enter
	lw	$5,0($2)

	.set	macro
	.set	reorder
	.end	wbwl_get_next_state_from_menu_enter
	.size	wbwl_get_next_state_from_menu_enter, .-wbwl_get_next_state_from_menu_enter

	.comm	g_ifm_ir_led_power_menu,140,4

	.comm	g_wbwl_timelapse_frequency_lookup_table,24,4

	.comm	g_tlps_file_type_menu,84,4

	.comm	g_wbwl_timelapse_frequency_menu,364,4

	.comm	g_dlsr_led_enable_menu,84,4

	.comm	g_rtc_time_format_menu,84,4

	.comm	g_rtc_date_format_menu,112,4

	.comm	g_evsd_extended_sd_power_menu,84,4
	.globl	g_wbwl_menu_handler_function_array_extensions
	.data
	.align	2
	.type	g_wbwl_menu_handler_function_array_extensions, @object
	.size	g_wbwl_menu_handler_function_array_extensions, 28
g_wbwl_menu_handler_function_array_extensions:
	.word	evsd_handle_extended_sd_power_menu
	.word	rtc_handle_date_format_menu
	.word	rtc_handle_time_format_menu
	.word	dslr_handle_led_enable_menu
	.word	apt_handle_aperture_menu
	.word	tlps_handle_file_type_menu
	.word	menus_handleCommitUpdates_menu
	.globl	g_wbwl_camera_setup_selector_array
	.align	2
	.type	g_wbwl_camera_setup_selector_array, @object
	.size	g_wbwl_camera_setup_selector_array, 248
g_wbwl_camera_setup_selector_array:
	.word	g_set_date_time_menu
	.word	1
	.word	g_operation_mode_menu
	.word	4
	.word	g_photo_quality_menu
	.word	5
	.word	g_video_length_menu
	.word	7
	.word	g_video_quality_menu
	.word	3
	.word	g_photo_delay_menu
	.word	11
	.word	g_multi_shot_mode_menu
	.word	16
	.word	g_temp_unit_menu
	.word	3
	.word	g_camera_name_menu
	.word	1
	.word	g_image_data_strip_menu
	.word	3
	.word	g_motion_test_menu
	.word	3
	.word	g_pir_range_menu
	.word	3
	.word	g_battery_type_menu
	.word	4
	.word	g_trigger_speed_menu
	.word	3
	.word	g_restore_default_menu
	.word	3
	.word	g_wbwl_timelapse_frequency_menu
	.word	13
	.word	g_timelapse_period_menu
	.word	6
	.word	g_delete_all_menu
	.word	3
	.word	g_ifm_ir_led_power_menu
	.word	5
	.word	g_smart_ir_video_menu
	.word	3
	.word	g_sd_management_menu
	.word	3
	.word	g_language_menu
	.word	8
	.word	g_capture_timer_menu
	.word	3
	.word	g_firmware_upgrade_menu
	.word	4
	.word	g_evsd_extended_sd_power_menu
	.word	3
	.word	g_rtc_date_format_menu
	.word	4
	.word	g_rtc_time_format_menu
	.word	3
	.word	g_dlsr_led_enable_menu
	.word	3
	.word	g_apt_aperture_menu
	.word	4
	.word	g_tlps_file_type_menu
	.word	3
	.word	0
	.word	0
	.globl	g_wbwl_camera_setup_menu_item_array
	.align	2
	.type	g_wbwl_camera_setup_menu_item_array, @object
	.size	g_wbwl_camera_setup_menu_item_array, 868
g_wbwl_camera_setup_menu_item_array:
	.word	3
	.word	31
	.word	0
	.word	1
	.word	0
	.word	2
	.word	5
	.word	4
	.word	37
	.word	0
	.word	1
	.word	0
	.word	2
	.word	6
	.word	5
	.word	43
	.word	0
	.word	1
	.word	0
	.word	2
	.word	7
	.word	6
	.word	45
	.word	0
	.word	1
	.word	0
	.word	2
	.word	8
	.word	7
	.word	44
	.word	0
	.word	1
	.word	0
	.word	2
	.word	9
	.word	8
	.word	46
	.word	0
	.word	1
	.word	0
	.word	2
	.word	10
	.word	9
	.word	86
	.word	0
	.word	1
	.word	0
	.word	2
	.word	11
	.word	10
	.word	89
	.word	0
	.word	1
	.word	0
	.word	2
	.word	12
	.word	11
	.word	90
	.word	0
	.word	1
	.word	0
	.word	2
	.word	13
	.word	12
	.word	91
	.word	0
	.word	1
	.word	0
	.word	2
	.word	14
	.word	13
	.word	47
	.word	0
	.word	1
	.word	0
	.word	2
	.word	15
	.word	14
	.word	50
	.word	0
	.word	1
	.word	0
	.word	2
	.word	16
	.word	15
	.word	54
	.word	0
	.word	1
	.word	0
	.word	2
	.word	17
	.word	16
	.word	57
	.word	0
	.word	1
	.word	0
	.word	2
	.word	18
	.word	17
	.word	61
	.word	0
	.word	1
	.word	0
	.word	2
	.word	19
	.word	18
	.word	58
	.word	0
	.word	1
	.word	0
	.word	2
	.word	20
	.word	19
	.word	59
	.word	0
	.word	1
	.word	0
	.word	2
	.word	21
	.word	22
	.word	69
	.word	0
	.word	1
	.word	0
	.word	2
	.word	22
	.word	26
	.word	65
	.word	0
	.word	1
	.word	0
	.word	2
	.word	23
	.word	25
	.word	66
	.word	0
	.word	1
	.word	0
	.word	2
	.word	24
	.word	24
	.word	67
	.word	0
	.word	1
	.word	0
	.word	2
	.word	25
	.word	27
	.word	100
	.word	0
	.word	1
	.word	0
	.word	2
	.word	26
	.word	29
	.word	116
	.word	0
	.word	1
	.word	0
	.word	2
	.word	27
	.word	30
	.word	92
	.word	0
	.word	1
	.word	0
	.word	2
	.word	29
	.word	24
	.word	179
	.word	0
	.word	1
	.word	0
	.word	2
	.word	30
	.word	3
	.word	183
	.word	0
	.word	1
	.word	0
	.word	2
	.word	31
	.word	3
	.word	180
	.word	0
	.word	1
	.word	0
	.word	2
	.word	32
	.word	13
	.word	187
	.word	0
	.word	1
	.word	0
	.word	2
	.word	33
	.word	26
	.word	190
	.word	0
	.word	1
	.word	0
	.word	2
	.word	34
	.word	18
	.word	194
	.word	0
	.word	1
	.word	0
	.word	2
	.word	35
	.word	31
	.word	110
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
