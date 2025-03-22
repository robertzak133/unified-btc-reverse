	.file	1 "aperture-menu.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	apt_get_cold_item_aperture
	.set	nomips16
	.set	nomicromips
	.ent	apt_get_cold_item_aperture
	.type	apt_get_cold_item_aperture, @function
apt_get_cold_item_aperture:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+57)
	jr	$31
	lbu	$2,%lo(g_ColdItemData+57)($2)

	.set	macro
	.set	reorder
	.end	apt_get_cold_item_aperture
	.size	apt_get_cold_item_aperture, .-apt_get_cold_item_aperture
	.align	2
	.globl	apt_set_cold_item_aperture
	.set	nomips16
	.set	nomicromips
	.ent	apt_set_cold_item_aperture
	.type	apt_set_cold_item_aperture, @function
apt_set_cold_item_aperture:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+57)
	jr	$31
	sb	$4,%lo(g_ColdItemData+57)($2)

	.set	macro
	.set	reorder
	.end	apt_set_cold_item_aperture
	.size	apt_set_cold_item_aperture, .-apt_set_cold_item_aperture
	.align	2
	.globl	apt_set_rtc_extra_aperture
	.set	nomips16
	.set	nomicromips
	.ent	apt_set_rtc_extra_aperture
	.type	apt_set_rtc_extra_aperture, @function
apt_set_rtc_extra_aperture:
	.frame	$sp,40,$31		# vars= 16, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	li	$6,2			# 0x2
	li	$5,6			# 0x6
	sw	$16,32($sp)
	move	$16,$4
	sw	$31,36($sp)
	jal	get_rtc_extra_byte_range
	addiu	$4,$sp,16

	lw	$2,16($sp)
	li	$3,-65536			# 0xffffffffffff0000
	addiu	$3,$3,16383
	sll	$16,$16,14
	and	$2,$2,$3
	andi	$16,$16,0xffff
	or	$16,$2,$16
	addiu	$4,$sp,16
	li	$6,2			# 0x2
	li	$5,6			# 0x6
	jal	set_rtc_extra_byte_range
	sw	$16,16($sp)

	lw	$31,36($sp)
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,40

	.set	macro
	.set	reorder
	.end	apt_set_rtc_extra_aperture
	.size	apt_set_rtc_extra_aperture, .-apt_set_rtc_extra_aperture
	.align	2
	.globl	apt_handle_aperture_menu
	.set	nomips16
	.set	nomicromips
	.ent	apt_handle_aperture_menu
	.type	apt_handle_aperture_menu, @function
apt_handle_aperture_menu:
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

	sb	$0,0($2)
	lui	$2,%hi(g_ColdItemData+57)
	lbu	$2,%lo(g_ColdItemData+57)($2)
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
	lw	$6,4($3)
	lw	$5,0($3)
	lui	$7,%hi(g_menu_root)
	jal	get_next_state_from_menu_enter
	addiu	$7,$7,%lo(g_menu_root)

	move	$4,$2
	li	$2,255			# 0xff
	beq	$4,$2,$L5
	lui	$2,%hi(g_ColdItemData+57)

	lbu	$3,2($16)
	sb	$3,%lo(g_ColdItemData+57)($2)
	sb	$17,6($16)
$L16:
	lw	$31,28($sp)
$L18:
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
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
	nop

$L5:
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
	li	$4,1			# 0x1
	sb	$2,0($16)
	jal	get_next_state_from_menu_mode
	addiu	$5,$5,%lo(g_menu_root)

	move	$4,$2
	li	$2,255			# 0xff
	beql	$4,$2,$L16
	li	$4,32			# 0x20

	b	$L18
	lw	$31,28($sp)

	.set	macro
	.set	reorder
	.end	apt_handle_aperture_menu
	.size	apt_handle_aperture_menu, .-apt_handle_aperture_menu
	.align	2
	.globl	apt_dummy
	.set	nomips16
	.set	nomicromips
	.ent	apt_dummy
	.type	apt_dummy, @function
apt_dummy:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	get_rtc_extra_operation_mode
	nop

	lw	$31,20($sp)
	move	$4,$2
	j	set_rtc_extra_operation_mode
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	apt_dummy
	.size	apt_dummy, .-apt_dummy
	.globl	g_apt_aperture_menu
	.data
	.align	2
	.type	g_apt_aperture_menu, @object
	.size	g_apt_aperture_menu, 112
g_apt_aperture_menu:
	.word	32
	.word	198
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	199
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	200
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	197
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,248,4

	.comm	g_wbwl_camera_setup_menu_item_array,868,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
