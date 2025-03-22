	.file	1 "timelapse.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	tlps_TaskTimeLapseFSM_task6
	.set	nomips16
	.set	nomicromips
	.ent	tlps_TaskTimeLapseFSM_task6
	.type	tlps_TaskTimeLapseFSM_task6, @function
tlps_TaskTimeLapseFSM_task6:
	.frame	$sp,64,$31		# vars= 24, regs= 2/0, args= 32, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+43)
	lbu	$2,%lo(g_ColdItemData+43)($2)
	addiu	$sp,$sp,-64
	sw	$31,60($sp)
	bne	$2,$0,$L2
	sw	$16,56($sp)

	jal	xtrg_get_cold_item_ext_trigger_enum
	nop

	li	$3,1			# 0x1
	bne	$2,$3,$L3
	nop

	jal	xtrg_Write_LEDOn
	nop

$L3:
	jal	TaskTimeLapseFSM_task6
	nop

	lw	$31,60($sp)
$L6:
	lw	$16,56($sp)
	jr	$31
	addiu	$sp,$sp,64

$L2:
	jal	get_photo_size_factor
	move	$4,$0

	jal	get_cold_item_photo_resolution
	move	$16,$2

	lui	$4,%hi(still_low_battery_display_function)
	addiu	$4,$4,%lo(still_low_battery_display_function)
	jal	register_low_battery_display_function
	sw	$2,48($sp)

	lw	$5,48($sp)
	jal	get_camera_photo_resolution
	addiu	$4,$sp,32

	li	$2,1			# 0x1
	sw	$2,24($sp)
	lw	$2,44($sp)
	lw	$7,36($sp)
	lw	$6,32($sp)
	sw	$2,20($sp)
	lw	$2,40($sp)
	move	$5,$16
	li	$4,1			# 0x1
	jal	startHceTaskStill_FSM
	sw	$2,16($sp)

	jal	set_fsm_state_relative
	li	$4,1			# 0x1

	b	$L6
	lw	$31,60($sp)

	.set	macro
	.set	reorder
	.end	tlps_TaskTimeLapseFSM_task6
	.size	tlps_TaskTimeLapseFSM_task6, .-tlps_TaskTimeLapseFSM_task6
	.align	2
	.globl	tlps_TaskTimeLapseFSM_task7
	.set	nomips16
	.set	nomicromips
	.ent	tlps_TaskTimeLapseFSM_task7
	.type	tlps_TaskTimeLapseFSM_task7, @function
tlps_TaskTimeLapseFSM_task7:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+43)
	lbu	$2,%lo(g_ColdItemData+43)($2)
	bne	$2,$0,$L8
	nop

	j	TaskTimeLapseFSM_task7
	nop

$L8:
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	HceTaskStillFSM_valid_p
	nop

	bne	$2,$0,$L7
	lw	$31,20($sp)

	li	$4,13			# 0xd
	j	set_fsm_state_absolute
	addiu	$sp,$sp,24

$L7:
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	tlps_TaskTimeLapseFSM_task7
	.size	tlps_TaskTimeLapseFSM_task7, .-tlps_TaskTimeLapseFSM_task7
	.align	2
	.globl	tlps_get_cold_item_raw_timelapse_period
	.set	nomips16
	.set	nomicromips
	.ent	tlps_get_cold_item_raw_timelapse_period
	.type	tlps_get_cold_item_raw_timelapse_period, @function
tlps_get_cold_item_raw_timelapse_period:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	get_cold_item_timelapse_period
	nop

	lw	$31,20($sp)
	lui	$2,%hi(g_ColdItemData+132)
	lw	$2,%lo(g_ColdItemData+132)($2)
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	tlps_get_cold_item_raw_timelapse_period
	.size	tlps_get_cold_item_raw_timelapse_period, .-tlps_get_cold_item_raw_timelapse_period
	.align	2
	.globl	tlps_get_cold_item_cooked_timelapse_period
	.set	nomips16
	.set	nomicromips
	.ent	tlps_get_cold_item_cooked_timelapse_period
	.type	tlps_get_cold_item_cooked_timelapse_period, @function
tlps_get_cold_item_cooked_timelapse_period:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+132)
	lw	$2,%lo(g_ColdItemData+132)($2)
	li	$3,5			# 0x5
	beql	$2,$3,$L16
	move	$2,$0

$L16:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	tlps_get_cold_item_cooked_timelapse_period
	.size	tlps_get_cold_item_cooked_timelapse_period, .-tlps_get_cold_item_cooked_timelapse_period
	.align	2
	.globl	tlps_get_tod_in_timelapse_region
	.set	nomips16
	.set	nomicromips
	.ent	tlps_get_tod_in_timelapse_region
	.type	tlps_get_tod_in_timelapse_region, @function
tlps_get_tod_in_timelapse_region:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+132)
	lw	$3,%lo(g_ColdItemData+132)($2)
	li	$2,5			# 0x5
	beq	$3,$2,$L18
	nop

	j	get_tod_in_timelapse_region
	nop

$L18:
	jr	$31
	li	$2,1			# 0x1

	.set	macro
	.set	reorder
	.end	tlps_get_tod_in_timelapse_region
	.size	tlps_get_tod_in_timelapse_region, .-tlps_get_tod_in_timelapse_region
	.align	2
	.globl	tlps_encoded_timelapse_frequency_to_seconds
	.set	nomips16
	.set	nomicromips
	.ent	tlps_encoded_timelapse_frequency_to_seconds
	.type	tlps_encoded_timelapse_frequency_to_seconds, @function
tlps_encoded_timelapse_frequency_to_seconds:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_wbwl_timelapse_frequency_lookup_table)
	addiu	$2,$2,%lo(g_wbwl_timelapse_frequency_lookup_table)
	sll	$4,$4,1
	addu	$4,$4,$2
	jr	$31
	lh	$2,0($4)

	.set	macro
	.set	reorder
	.end	tlps_encoded_timelapse_frequency_to_seconds
	.size	tlps_encoded_timelapse_frequency_to_seconds, .-tlps_encoded_timelapse_frequency_to_seconds
	.align	2
	.globl	tlps_execute_if_not_null
	.set	nomips16
	.set	nomicromips
	.ent	tlps_execute_if_not_null
	.type	tlps_execute_if_not_null, @function
tlps_execute_if_not_null:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_wbwl_TaskTimeLapseFSM_function_array)
	sll	$4,$4,2
	addiu	$2,$2,%lo(g_wbwl_TaskTimeLapseFSM_function_array)
	addu	$4,$4,$2
	j	execute_if_not_null
	lw	$4,0($4)

	.set	macro
	.set	reorder
	.end	tlps_execute_if_not_null
	.size	tlps_execute_if_not_null, .-tlps_execute_if_not_null
	.align	2
	.globl	tlps_update_system_measurements
	.set	nomips16
	.set	nomicromips
	.ent	tlps_update_system_measurements
	.type	tlps_update_system_measurements, @function
tlps_update_system_measurements:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	Volt_Calib_Bat
	nop

	jal	temperature_sensor_getReading
	nop

	jal	set_g_temperature_forc
	move	$4,$2

	lw	$31,20($sp)
	j	update_timelapse_rise_set_times
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	tlps_update_system_measurements
	.size	tlps_update_system_measurements, .-tlps_update_system_measurements
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"HceTaskTimeLapse_End\000"
	.text
	.align	2
	.globl	tlps_TaskTimeLapseFSM_task12a
	.set	nomips16
	.set	nomicromips
	.ent	tlps_TaskTimeLapseFSM_task12a
	.type	tlps_TaskTimeLapseFSM_task12a, @function
tlps_TaskTimeLapseFSM_task12a:
	.frame	$sp,32,$31		# vars= 0, regs= 4/0, args= 16, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$31,28($sp)
	sw	$18,24($sp)
	sw	$17,20($sp)
	jal	get_cold_item_timelapse_frequency
	sw	$16,16($sp)

	jal	encoded_timelapse_frequency_to_seconds
	move	$4,$2

	lui	$18,%hi(g_ColdItemData)
	move	$16,$2
	jal	get_cold_item_tod_last_photo_in_seconds
	addiu	$18,$18,%lo(g_ColdItemData)

	jal	get_cold_item_timelapse_period
	move	$17,$2

	lw	$3,132($18)
	li	$2,5			# 0x5
	bnel	$3,$2,$L36
	lbu	$2,43($18)

	li	$2,65536			# 0x10000
	addu	$17,$17,$16
	addiu	$2,$2,20865
	sltu	$17,$17,$2
	bnel	$17,$0,$L36
	lbu	$2,43($18)

	jal	set_cold_item_timelapse_new_file_p
	li	$4,1			# 0x1

	lbu	$2,43($18)
$L36:
	bne	$2,$0,$L37
	sltu	$2,$16,4

	jal	xtrg_get_cold_item_ext_trigger_enum
	nop

	li	$3,1			# 0x1
	bne	$2,$3,$L37
	sltu	$2,$16,4

	jal	xtrg_Write_LEDOff
	nop

	sltu	$2,$16,4
$L37:
	beq	$2,$0,$L35
	li	$4,12			# 0xc

	jal	get_power_switch_on_p
	nop

	bne	$2,$0,$L29
	lui	$5,%hi($LC0)

	li	$4,12			# 0xc
$L35:
	lw	$31,28($sp)
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L29:
	addiu	$5,$5,%lo($LC0)
	jal	HceCommon_SetCaptureImag
	move	$4,$0

	jal	get_current_operating_time_ms
	nop

	li	$6,1000			# 0x3e8
	mult	$16,$6
	mflo	$16
	lui	$3,%hi(g_last_timelapse_time_in_ms)
	lw	$5,%lo(g_last_timelapse_time_in_ms)($3)
	subu	$4,$2,$5
	sltu	$6,$4,$16
	beq	$6,$0,$L30
	move	$17,$3

	beq	$4,$0,$L30
	nop

	addu	$5,$5,$16
	subu	$5,$5,$2
	jal	thread_sleep
	li	$4,3			# 0x3

$L30:
	jal	get_current_operating_time_ms
	nop

	jal	tlps_update_system_measurements
	sw	$2,%lo(g_last_timelapse_time_in_ms)($17)

	b	$L35
	li	$4,1			# 0x1

	.set	macro
	.set	reorder
	.end	tlps_TaskTimeLapseFSM_task12a
	.size	tlps_TaskTimeLapseFSM_task12a, .-tlps_TaskTimeLapseFSM_task12a
	.align	2
	.globl	tlps_get_cold_item_file_type
	.set	nomips16
	.set	nomicromips
	.ent	tlps_get_cold_item_file_type
	.type	tlps_get_cold_item_file_type, @function
tlps_get_cold_item_file_type:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+43)
	jr	$31
	lbu	$2,%lo(g_ColdItemData+43)($2)

	.set	macro
	.set	reorder
	.end	tlps_get_cold_item_file_type
	.size	tlps_get_cold_item_file_type, .-tlps_get_cold_item_file_type
	.align	2
	.globl	tlps_set_cold_item_file_type
	.set	nomips16
	.set	nomicromips
	.ent	tlps_set_cold_item_file_type
	.type	tlps_set_cold_item_file_type, @function
tlps_set_cold_item_file_type:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+43)
	jr	$31
	sb	$4,%lo(g_ColdItemData+43)($2)

	.set	macro
	.set	reorder
	.end	tlps_set_cold_item_file_type
	.size	tlps_set_cold_item_file_type, .-tlps_set_cold_item_file_type
	.align	2
	.globl	tlps_handle_file_type_menu
	.set	nomips16
	.set	nomicromips
	.ent	tlps_handle_file_type_menu
	.type	tlps_handle_file_type_menu, @function
tlps_handle_file_type_menu:
	.frame	$sp,32,$31		# vars= 0, regs= 4/0, args= 16, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$17,20($sp)
	sw	$16,16($sp)
	sw	$31,28($sp)
	jal	getCameraConfigStructPtr
	sw	$18,24($sp)

	lbu	$17,0($2)
	beq	$17,$0,$L41
	move	$16,$2

	sb	$0,0($2)
	lui	$2,%hi(g_ColdItemData+43)
	lbu	$2,%lo(g_ColdItemData+43)($2)
	addiu	$4,$16,2
	lui	$5,%hi(g_menu_root)
	sb	$2,2($16)
	lw	$31,28($sp)
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	addiu	$5,$5,%lo(g_menu_root)
	j	menu_draw_selected_item
	addiu	$sp,$sp,32

$L41:
	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L42
	lui	$2,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L54
	lui	$18,%hi(g_menu_root)

$L42:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L44
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L43
	lui	$18,%hi(g_menu_root)

$L44:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$3,1			# 0x1
	beq	$2,$3,$L45
	lui	$2,%hi(g_left_button_enable)

$L46:
	jal	ui_cursor_key_pressed_p
	li	$4,3			# 0x3

	li	$3,1			# 0x1
	bne	$2,$3,$L48
	lui	$2,%hi(g_right_button_enable)

	lbu	$3,%lo(g_right_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L55
	lw	$31,28($sp)

$L48:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L50
	lui	$2,%hi(g_enter_button_enable)

	lbu	$3,%lo(g_enter_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L50
	lui	$3,%hi(g_wbwl_camera_setup_selector_array)

	lbu	$4,2($16)
	addiu	$3,$3,%lo(g_wbwl_camera_setup_selector_array)
	sll	$2,$4,3
	sb	$17,0($16)
	addu	$3,$3,$2
	lw	$6,4($3)
	lw	$5,0($3)
	lui	$7,%hi(g_menu_root)
	jal	get_next_state_from_menu_enter
	addiu	$7,$7,%lo(g_menu_root)

	move	$4,$2
	li	$2,255			# 0xff
	beq	$4,$2,$L40
	lui	$2,%hi(g_ColdItemData+43)

	lbu	$3,2($16)
	sb	$3,%lo(g_ColdItemData+43)($2)
	sb	$17,6($16)
$L51:
	lw	$31,28($sp)
$L53:
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L43:
$L54:
	addiu	$5,$16,2
	move	$4,$17
	addiu	$7,$18,%lo(g_menu_root)
	jal	menu_get_next_menu_selection
	li	$6,1			# 0x1

	lbu	$4,2($16)
	lw	$31,28($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	addiu	$5,$18,%lo(g_menu_root)
	lw	$18,24($sp)
	j	menu_redraw_items
	addiu	$sp,$sp,32

$L45:
	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L46
	nop

$L40:
	lw	$31,28($sp)
$L55:
	lw	$18,24($sp)
$L56:
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,32

$L50:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L55
	lw	$31,28($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L56
	lw	$18,24($sp)

	lui	$5,%hi(g_menu_root)
	li	$4,1			# 0x1
	sb	$2,0($16)
	jal	get_next_state_from_menu_mode
	addiu	$5,$5,%lo(g_menu_root)

	move	$4,$2
	li	$2,255			# 0xff
	beql	$4,$2,$L51
	li	$4,36			# 0x24

	b	$L53
	lw	$31,28($sp)

	.set	macro
	.set	reorder
	.end	tlps_handle_file_type_menu
	.size	tlps_handle_file_type_menu, .-tlps_handle_file_type_menu
	.align	2
	.globl	tlps_HceIRCut_SetIRCutClosed
	.set	nomips16
	.set	nomicromips
	.ent	tlps_HceIRCut_SetIRCutClosed
	.type	tlps_HceIRCut_SetIRCutClosed, @function
tlps_HceIRCut_SetIRCutClosed:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+43)
	lbu	$2,%lo(g_ColdItemData+43)($2)
	bne	$2,$0,$L59
	nop

	j	HceIRCut_SetIRCutClosed
	nop

$L59:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	tlps_HceIRCut_SetIRCutClosed
	.size	tlps_HceIRCut_SetIRCutClosed, .-tlps_HceIRCut_SetIRCutClosed
	.align	2
	.globl	tls_HceTaskBoot2Cap_Task0
	.set	nomips16
	.set	nomicromips
	.ent	tls_HceTaskBoot2Cap_Task0
	.type	tls_HceTaskBoot2Cap_Task0, @function
tls_HceTaskBoot2Cap_Task0:
	.frame	$sp,40,$31		# vars= 16, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$31,36($sp)
	jal	wfl_spawnIRCutFSM_per_mode
	sw	$16,32($sp)

	jal	checkForSDCard
	nop

	jal	get_within_operating_hours_p
	move	$16,$2

	beq	$16,$0,$L64
	li	$4,7			# 0x7

	bne	$2,$0,$L62
	nop

$L64:
	jal	set_fsm_state_absolute
	nop

	lw	$31,36($sp)
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,40

$L62:
	jal	get_current_date_time_short
	addiu	$4,$sp,16

	jal	set_exif_time_of_capture
	addiu	$4,$sp,16

	jal	get_cold_item_operation_mode
	nop

	beq	$2,$0,$L64
	li	$4,1			# 0x1

	li	$3,1			# 0x1
	beq	$2,$3,$L64
	li	$4,3			# 0x3

	lh	$2,24($sp)
	li	$3,3600			# 0xe10
	li	$16,65536			# 0x10000
	sll	$4,$2,4
	subu	$4,$4,$2
	lh	$2,22($sp)
	sll	$4,$4,2
	mult	$2,$3
	mflo	$2
	addu	$4,$4,$2
	lh	$2,26($sp)
	addu	$4,$4,$2
	ori	$2,$16,0x86a0
	sltu	$2,$4,$2
	bne	$2,$0,$L65
	addiu	$2,$16,20865

	jal	HceTaskBoot2Cap_Task0
	nop

	b	$L66
	addiu	$4,$16,20863

$L65:
	sltu	$2,$4,$2
	beql	$2,$0,$L66
	addiu	$4,$16,20863

$L66:
	jal	set_rtc_extra_current_tod_in_seconds
	nop

	b	$L64
	li	$4,1			# 0x1

	.set	macro
	.set	reorder
	.end	tls_HceTaskBoot2Cap_Task0
	.size	tls_HceTaskBoot2Cap_Task0, .-tls_HceTaskBoot2Cap_Task0
	.globl	g_wbwl_TaskTimeLapseFSM_function_array
	.data
	.align	2
	.type	g_wbwl_TaskTimeLapseFSM_function_array, @object
	.size	g_wbwl_TaskTimeLapseFSM_function_array, 64
g_wbwl_TaskTimeLapseFSM_function_array:
	.word	TaskTimeLapseFSM_task0
	.word	TaskTimeLapseFSM_task1
	.word	TaskTimeLapseFSM_task2
	.word	TaskTimeLapseFSM_task3_ae_set
	.word	TaskTimeLapseFSM_task4
	.word	TaskTimeLapseFSM_task5
	.word	tlps_TaskTimeLapseFSM_task6
	.word	tlps_TaskTimeLapseFSM_task7
	.word	TaskTimeLapseFSM_task8_CopyJPGFromRAM
	.word	TaskTimeLapseFSM_task9
	.word	TaskTimeLapseFSM_task10_WaitMountSD
	.word	TaskTimeLapseFSM_task11_openTLfile
	.word	TaskTimeLapseFSM_task12
	.word	tlps_TaskTimeLapseFSM_task12a
	.word	TaskTimeLapseFSM_task13
	.word	TaskTimeLapseFSM_task14_end
	.globl	g_wbwl_timelapse_frequency_lookup_table
	.align	2
	.type	g_wbwl_timelapse_frequency_lookup_table, @object
	.size	g_wbwl_timelapse_frequency_lookup_table, 24
g_wbwl_timelapse_frequency_lookup_table:
	.half	1
	.half	2
	.half	5
	.half	10
	.half	20
	.half	30
	.half	60
	.half	120
	.half	300
	.half	600
	.half	1800
	.half	3600
	.globl	g_tlps_file_type_menu
	.align	2
	.type	g_tlps_file_type_menu, @object
	.size	g_tlps_file_type_menu, 84
g_tlps_file_type_menu:
	.word	32
	.word	202
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	203
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	201
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3
	.globl	g_wbwl_timelapse_frequency_menu
	.align	2
	.type	g_wbwl_timelapse_frequency_menu, @object
	.size	g_wbwl_timelapse_frequency_menu, 364
g_wbwl_timelapse_frequency_menu:
	.word	32
	.word	12
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	195
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	13
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	14
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	15
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	16
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	17
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	18
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	19
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	20
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	21
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	22
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	59
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3

	.comm	g_ext_trigger_enable_menu,112,4

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,248,4

	.comm	g_wbwl_camera_setup_menu_item_array,868,4
	.globl	g_wbwl_timelapse_period_menu
	.align	2
	.type	g_wbwl_timelapse_period_menu, @object
	.size	g_wbwl_timelapse_period_menu, 196
g_wbwl_timelapse_period_menu:
	.word	32
	.word	27
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	23
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	24
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	25
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	26
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	196
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	60
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
