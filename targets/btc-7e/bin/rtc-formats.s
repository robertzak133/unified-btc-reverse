	.file	1 "rtc-formats.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	rtc_get_cold_item_date_format
	.set	nomips16
	.set	nomicromips
	.ent	rtc_get_cold_item_date_format
	.type	rtc_get_cold_item_date_format, @function
rtc_get_cold_item_date_format:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+93)
	lbu	$2,%lo(g_ColdItemData+93)($2)
	srl	$2,$2,2
	jr	$31
	andi	$2,$2,0x3

	.set	macro
	.set	reorder
	.end	rtc_get_cold_item_date_format
	.size	rtc_get_cold_item_date_format, .-rtc_get_cold_item_date_format
	.align	2
	.globl	rtc_set_cold_item_date_format
	.set	nomips16
	.set	nomicromips
	.ent	rtc_set_cold_item_date_format
	.type	rtc_set_cold_item_date_format, @function
rtc_set_cold_item_date_format:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$3,%hi(g_ColdItemData)
	addiu	$3,$3,%lo(g_ColdItemData)
	lbu	$2,93($3)
	sll	$4,$4,2
	andi	$4,$4,0xc
	andi	$2,$2,0xf3
	or	$2,$2,$4
	jr	$31
	sb	$2,93($3)

	.set	macro
	.set	reorder
	.end	rtc_set_cold_item_date_format
	.size	rtc_set_cold_item_date_format, .-rtc_set_cold_item_date_format
	.align	2
	.globl	rtc_get_cold_item_time_format
	.set	nomips16
	.set	nomicromips
	.ent	rtc_get_cold_item_time_format
	.type	rtc_get_cold_item_time_format, @function
rtc_get_cold_item_time_format:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+93)
	lbu	$2,%lo(g_ColdItemData+93)($2)
	srl	$2,$2,4
	jr	$31
	andi	$2,$2,0x1

	.set	macro
	.set	reorder
	.end	rtc_get_cold_item_time_format
	.size	rtc_get_cold_item_time_format, .-rtc_get_cold_item_time_format
	.align	2
	.globl	rtc_set_cold_item_time_format
	.set	nomips16
	.set	nomicromips
	.ent	rtc_set_cold_item_time_format
	.type	rtc_set_cold_item_time_format, @function
rtc_set_cold_item_time_format:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+93)
	lbu	$2,%lo(g_ColdItemData+93)($2)
	sll	$4,$4,4
	andi	$4,$4,0x10
	andi	$2,$2,0xef
	j	set_cold_item_sd_management_p
	or	$4,$2,$4

	.set	macro
	.set	reorder
	.end	rtc_set_cold_item_time_format
	.size	rtc_set_cold_item_time_format, .-rtc_set_cold_item_time_format
	.align	2
	.globl	rtc_handle_date_format_menu
	.set	nomips16
	.set	nomicromips
	.ent	rtc_handle_date_format_menu
	.type	rtc_handle_date_format_menu, @function
rtc_handle_date_format_menu:
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
	beq	$17,$0,$L6
	move	$16,$2

	jal	rtc_get_cold_item_date_format
	sb	$0,0($2)

	sb	$2,2($16)
	lw	$31,28($sp)
	lw	$18,24($sp)
	lw	$17,20($sp)
	addiu	$4,$16,2
	lw	$16,16($sp)
	lui	$5,%hi(g_menu_root)
	addiu	$5,$5,%lo(g_menu_root)
	j	menu_draw_selected_item
	addiu	$sp,$sp,32

$L6:
	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L7
	lui	$2,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L19
	lui	$18,%hi(g_menu_root)

$L7:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L9
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L8
	lui	$18,%hi(g_menu_root)

$L9:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$3,1			# 0x1
	beq	$2,$3,$L10
	lui	$2,%hi(g_left_button_enable)

$L11:
	jal	ui_cursor_key_pressed_p
	li	$4,3			# 0x3

	li	$3,1			# 0x1
	bne	$2,$3,$L13
	lui	$2,%hi(g_right_button_enable)

	lbu	$3,%lo(g_right_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L20
	lw	$31,28($sp)

$L13:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L15
	lui	$2,%hi(g_enter_button_enable)

	lbu	$3,%lo(g_enter_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L15
	lui	$3,%hi(g_wbwl_camera_setup_selector_array)

	lbu	$4,2($16)
	addiu	$3,$3,%lo(g_wbwl_camera_setup_selector_array)
	sll	$2,$4,3
	sb	$17,0($16)
	addu	$3,$3,$2
	lw	$5,0($3)
	lw	$6,4($3)
	lui	$7,%hi(g_menu_root)
	jal	get_next_state_from_menu_enter
	addiu	$7,$7,%lo(g_menu_root)

	move	$5,$2
	li	$2,255			# 0xff
	beq	$5,$2,$L20
	lw	$31,28($sp)

	jal	rtc_set_cold_item_date_format
	lbu	$4,2($16)

	sb	$17,6($16)
$L16:
	lw	$31,28($sp)
$L18:
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	move	$4,$5
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L8:
$L19:
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

$L10:
	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L11
	lw	$31,28($sp)

$L20:
	lw	$18,24($sp)
$L21:
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,32

$L15:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L20
	lw	$31,28($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L21
	lw	$18,24($sp)

	lui	$5,%hi(g_menu_root)
	addiu	$5,$5,%lo(g_menu_root)
	sb	$2,0($16)
	jal	get_next_state_from_menu_mode
	li	$4,1			# 0x1

	move	$5,$2
	li	$2,255			# 0xff
	beql	$5,$2,$L16
	li	$5,36			# 0x24

	b	$L18
	lw	$31,28($sp)

	.set	macro
	.set	reorder
	.end	rtc_handle_date_format_menu
	.size	rtc_handle_date_format_menu, .-rtc_handle_date_format_menu
	.align	2
	.globl	rtc_handle_time_format_menu
	.set	nomips16
	.set	nomicromips
	.ent	rtc_handle_time_format_menu
	.type	rtc_handle_time_format_menu, @function
rtc_handle_time_format_menu:
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
	beq	$17,$0,$L23
	move	$16,$2

	jal	rtc_get_cold_item_time_format
	sb	$0,0($2)

	sb	$2,2($16)
	lw	$31,28($sp)
	lw	$18,24($sp)
	lw	$17,20($sp)
	addiu	$4,$16,2
	lw	$16,16($sp)
	lui	$5,%hi(g_menu_root)
	addiu	$5,$5,%lo(g_menu_root)
	j	menu_draw_selected_item
	addiu	$sp,$sp,32

$L23:
	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L24
	lui	$2,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L36
	lui	$18,%hi(g_menu_root)

$L24:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L26
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L25
	lui	$18,%hi(g_menu_root)

$L26:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$3,1			# 0x1
	beq	$2,$3,$L27
	lui	$2,%hi(g_left_button_enable)

$L28:
	jal	ui_cursor_key_pressed_p
	li	$4,3			# 0x3

	li	$3,1			# 0x1
	bne	$2,$3,$L30
	lui	$2,%hi(g_right_button_enable)

	lbu	$3,%lo(g_right_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L37
	lw	$31,28($sp)

$L30:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	move	$18,$2
	li	$2,1			# 0x1
	bne	$18,$2,$L32
	lui	$2,%hi(g_enter_button_enable)

	lbu	$3,%lo(g_enter_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L32
	lui	$3,%hi(g_wbwl_camera_setup_selector_array)

	lbu	$4,2($16)
	addiu	$3,$3,%lo(g_wbwl_camera_setup_selector_array)
	sll	$2,$4,3
	sb	$18,0($16)
	addu	$3,$3,$2
	lw	$6,4($3)
	lw	$5,0($3)
	lui	$7,%hi(g_menu_root)
	jal	get_next_state_from_menu_enter
	addiu	$7,$7,%lo(g_menu_root)

	move	$17,$2
	li	$2,255			# 0xff
	beq	$17,$2,$L37
	lw	$31,28($sp)

	jal	rtc_set_cold_item_time_format
	lbu	$4,2($16)

	sb	$18,6($16)
$L33:
	lw	$31,28($sp)
$L35:
	lw	$18,24($sp)
	lw	$16,16($sp)
	move	$4,$17
	lw	$17,20($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L25:
$L36:
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

$L27:
	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L28
	lw	$31,28($sp)

$L37:
	lw	$18,24($sp)
$L38:
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,32

$L32:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L37
	lw	$31,28($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L38
	lw	$18,24($sp)

	lui	$5,%hi(g_menu_root)
	sb	$2,0($16)
	addiu	$5,$5,%lo(g_menu_root)
	jal	get_next_state_from_menu_mode
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,255			# 0xff
	beql	$17,$2,$L33
	li	$17,36			# 0x24

	b	$L35
	lw	$31,28($sp)

	.set	macro
	.set	reorder
	.end	rtc_handle_time_format_menu
	.size	rtc_handle_time_format_menu, .-rtc_handle_time_format_menu
	.globl	g_rtc_time_format_menu
	.data
	.align	2
	.type	g_rtc_time_format_menu, @object
	.size	g_rtc_time_format_menu, 84
g_rtc_time_format_menu:
	.word	31
	.word	179
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	178
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	177
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3
	.globl	g_rtc_date_format_menu
	.align	2
	.type	g_rtc_date_format_menu, @object
	.size	g_rtc_date_format_menu, 112
g_rtc_date_format_menu:
	.word	31
	.word	181
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	182
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	183
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	180
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3

	.comm	g_wbwl_menu_handler_function_array_extensions,28,4

	.comm	g_wbwl_camera_setup_selector_array,248,4

	.comm	g_wbwl_camera_setup_menu_item_array,868,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
