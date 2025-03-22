	.file	1 "dslr-trigger.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	xtrg_Write_LEDOn
	.set	nomips16
	.set	nomicromips
	.ent	xtrg_Write_LEDOn
	.type	xtrg_Write_LEDOn, @function
xtrg_Write_LEDOn:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	Write_LEDOn
	nop

	.set	macro
	.set	reorder
	.end	xtrg_Write_LEDOn
	.size	xtrg_Write_LEDOn, .-xtrg_Write_LEDOn
	.align	2
	.globl	xtrg_Write_LEDOff
	.set	nomips16
	.set	nomicromips
	.ent	xtrg_Write_LEDOff
	.type	xtrg_Write_LEDOff, @function
xtrg_Write_LEDOff:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	Write_LEDOff
	nop

	.set	macro
	.set	reorder
	.end	xtrg_Write_LEDOff
	.size	xtrg_Write_LEDOff, .-xtrg_Write_LEDOff
	.align	2
	.globl	xtrg_flash_trigger_p
	.set	nomips16
	.set	nomicromips
	.ent	xtrg_flash_trigger_p
	.type	xtrg_flash_trigger_p, @function
xtrg_flash_trigger_p:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	apt_get_cold_item_aperture
	nop

	move	$3,$2
	lui	$2,%hi(g_night_mode_p)
	lbu	$4,%lo(g_night_mode_p)($2)
	bne	$4,$0,$L4
	li	$2,1			# 0x1

	li	$4,2			# 0x2
	bne	$3,$4,$L4
	move	$2,$0

	lui	$2,%hi(g_apt_nightmode_threshold_lookup_table)
	lbu	$3,%lo(g_apt_nightmode_threshold_lookup_table)($2)
	lui	$2,%hi(g_photo_sensor_value)
	lw	$2,%lo(g_photo_sensor_value)($2)
	sltu	$2,$2,$3
$L4:
	lw	$31,20($sp)
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	xtrg_flash_trigger_p
	.size	xtrg_flash_trigger_p, .-xtrg_flash_trigger_p
	.align	2
	.globl	dt_cold_item_led_power_blur_reduction_p
	.set	nomips16
	.set	nomicromips
	.ent	dt_cold_item_led_power_blur_reduction_p
	.type	dt_cold_item_led_power_blur_reduction_p, @function
dt_cold_item_led_power_blur_reduction_p:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+66)
	lbu	$2,%lo(g_ColdItemData+66)($2)
	addiu	$sp,$sp,-24
	li	$3,1			# 0x1
	beq	$2,$3,$L16
	sw	$31,20($sp)

	li	$3,2			# 0x2
	beq	$2,$3,$L10
	lw	$31,20($sp)

$L17:
	j	cold_item_led_power_blur_reduction_p
	addiu	$sp,$sp,24

$L10:
	jal	xtrg_flash_trigger_p
	nop

	beq	$2,$0,$L17
	lw	$31,20($sp)

$L16:
	jal	Write_LEDOn
	nop

	b	$L17
	lw	$31,20($sp)

	.set	macro
	.set	reorder
	.end	dt_cold_item_led_power_blur_reduction_p
	.size	dt_cold_item_led_power_blur_reduction_p, .-dt_cold_item_led_power_blur_reduction_p
	.align	2
	.globl	dt_video_log_printf_hook
	.set	nomips16
	.set	nomicromips
	.ent	dt_video_log_printf_hook
	.type	dt_video_log_printf_hook, @function
dt_video_log_printf_hook:
	.frame	$sp,24,$31		# vars= 0, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	lui	$2,%hi(g_ColdItemData+66)
	sw	$16,16($sp)
	lbu	$16,%lo(g_ColdItemData+66)($2)
	sw	$31,20($sp)
	jal	log_printf
	nop

	li	$2,1			# 0x1
	beq	$16,$2,$L26
	li	$2,2			# 0x2

	beq	$16,$2,$L20
	lw	$31,20($sp)

$L27:
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,24

$L20:
	jal	xtrg_flash_trigger_p
	nop

	beq	$2,$0,$L27
	lw	$31,20($sp)

$L26:
	lw	$31,20($sp)
	lw	$16,16($sp)
	j	Write_LEDOn
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	dt_video_log_printf_hook
	.size	dt_video_log_printf_hook, .-dt_video_log_printf_hook
	.align	2
	.globl	dt_IRLedOff
	.set	nomips16
	.set	nomicromips
	.ent	dt_IRLedOff
	.type	dt_IRLedOff, @function
dt_IRLedOff:
	.frame	$sp,24,$31		# vars= 0, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	lui	$2,%hi(g_ColdItemData+66)
	sw	$16,16($sp)
	lbu	$16,%lo(g_ColdItemData+66)($2)
	sw	$31,20($sp)
	jal	IRLedOff
	nop

	li	$2,1			# 0x1
	beq	$16,$2,$L36
	li	$2,2			# 0x2

	beq	$16,$2,$L30
	lw	$31,20($sp)

$L37:
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,24

$L30:
	jal	xtrg_flash_trigger_p
	nop

	beq	$2,$0,$L37
	lw	$31,20($sp)

$L36:
	lw	$31,20($sp)
	lw	$16,16($sp)
	j	Write_LEDOff
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	dt_IRLedOff
	.size	dt_IRLedOff, .-dt_IRLedOff
	.align	2
	.globl	xtrg_get_cold_item_ext_trigger_enum
	.set	nomips16
	.set	nomicromips
	.ent	xtrg_get_cold_item_ext_trigger_enum
	.type	xtrg_get_cold_item_ext_trigger_enum, @function
xtrg_get_cold_item_ext_trigger_enum:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+66)
	jr	$31
	lbu	$2,%lo(g_ColdItemData+66)($2)

	.set	macro
	.set	reorder
	.end	xtrg_get_cold_item_ext_trigger_enum
	.size	xtrg_get_cold_item_ext_trigger_enum, .-xtrg_get_cold_item_ext_trigger_enum
	.align	2
	.globl	xtrg_set_cold_item_ext_trigger_enum
	.set	nomips16
	.set	nomicromips
	.ent	xtrg_set_cold_item_ext_trigger_enum
	.type	xtrg_set_cold_item_ext_trigger_enum, @function
xtrg_set_cold_item_ext_trigger_enum:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+66)
	jr	$31
	sb	$4,%lo(g_ColdItemData+66)($2)

	.set	macro
	.set	reorder
	.end	xtrg_set_cold_item_ext_trigger_enum
	.size	xtrg_set_cold_item_ext_trigger_enum, .-xtrg_set_cold_item_ext_trigger_enum
	.align	2
	.globl	xtrg_handle_led_enable_menu
	.set	nomips16
	.set	nomicromips
	.ent	xtrg_handle_led_enable_menu
	.type	xtrg_handle_led_enable_menu, @function
xtrg_handle_led_enable_menu:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$16,20($sp)
	sw	$31,28($sp)
	jal	getCameraConfigStructPtr
	sw	$17,24($sp)

	move	$16,$2
	lbu	$2,0($2)
	beq	$2,$0,$L41
	lui	$2,%hi(g_ColdItemData+66)

	sb	$0,0($16)
	lbu	$2,%lo(g_ColdItemData+66)($2)
	addiu	$4,$16,2
	lui	$5,%hi(g_menu_root)
	sb	$2,2($16)
	lw	$31,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
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
	beq	$3,$2,$L52
	move	$4,$0

$L42:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	li	$3,1			# 0x1
	bne	$2,$3,$L44
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L43
	li	$4,1			# 0x1

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
	beq	$3,$2,$L56
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
	beq	$4,$2,$L56
	lw	$31,28($sp)

	lbu	$3,2($16)
	lui	$2,%hi(g_ColdItemData+66)
	sb	$3,%lo(g_ColdItemData+66)($2)
	sb	$17,6($16)
$L51:
	lw	$31,28($sp)
$L55:
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L52:
$L43:
	lui	$17,%hi(g_menu_root)
	addiu	$5,$16,2
	addiu	$7,$17,%lo(g_menu_root)
	jal	menu_get_next_menu_selection
	li	$6,1			# 0x1

	lbu	$4,2($16)
	lw	$31,28($sp)
	lw	$16,20($sp)
	addiu	$5,$17,%lo(g_menu_root)
	lw	$17,24($sp)
	j	menu_redraw_items
	addiu	$sp,$sp,32

$L45:
	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L46
	lw	$31,28($sp)

$L56:
	lw	$17,24($sp)
$L57:
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,32

$L50:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L56
	lw	$31,28($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L57
	lw	$17,24($sp)

	lui	$5,%hi(g_menu_root)
	li	$4,1			# 0x1
	sb	$2,0($16)
	jal	get_next_state_from_menu_mode
	addiu	$5,$5,%lo(g_menu_root)

	move	$4,$2
	li	$2,255			# 0xff
	beql	$4,$2,$L51
	li	$4,35			# 0x23

	b	$L55
	lw	$31,28($sp)

	.set	macro
	.set	reorder
	.end	xtrg_handle_led_enable_menu
	.size	xtrg_handle_led_enable_menu, .-xtrg_handle_led_enable_menu
	.globl	g_ext_trigger_enable_menu
	.data
	.align	2
	.type	g_ext_trigger_enable_menu, @object
	.size	g_ext_trigger_enable_menu, 112
g_ext_trigger_enable_menu:
	.word	31
	.word	8
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	201
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	202
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	185
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,240,4

	.comm	g_wbwl_camera_setup_menu_item_array,840,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
