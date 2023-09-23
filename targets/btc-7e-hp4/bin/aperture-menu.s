	.file	1 "aperture-menu.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
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
	beq	$17,$0,$L2
	move	$16,$2

	jal	apt_get_cold_item_aperture
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

$L2:
	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L3
	lui	$2,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L15
	lui	$18,%hi(g_menu_root)

$L3:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L5
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L4
	lui	$18,%hi(g_menu_root)

$L5:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$3,1			# 0x1
	beq	$2,$3,$L6
	lui	$2,%hi(g_left_button_enable)

$L7:
	jal	ui_cursor_key_pressed_p
	li	$4,3			# 0x3

	li	$3,1			# 0x1
	bne	$2,$3,$L9
	lui	$2,%hi(g_right_button_enable)

	lbu	$3,%lo(g_right_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L16
	lw	$31,28($sp)

$L9:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	move	$18,$2
	li	$2,1			# 0x1
	bne	$18,$2,$L11
	lui	$2,%hi(g_enter_button_enable)

	lbu	$3,%lo(g_enter_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L11
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
	beq	$17,$2,$L16
	lw	$31,28($sp)

	jal	apt_set_cold_item_aperture
	lbu	$4,2($16)

	sb	$18,4($16)
$L12:
	lw	$31,28($sp)
$L14:
	lw	$18,24($sp)
	lw	$16,16($sp)
	move	$4,$17
	lw	$17,20($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L4:
$L15:
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

$L6:
	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L7
	lw	$31,28($sp)

$L16:
	lw	$18,24($sp)
$L17:
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,32

$L11:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L16
	lw	$31,28($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L17
	lw	$18,24($sp)

	lui	$5,%hi(g_menu_root)
	sb	$2,0($16)
	addiu	$5,$5,%lo(g_menu_root)
	jal	get_next_state_from_menu_mode
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,255			# 0xff
	beql	$17,$2,$L12
	li	$17,31			# 0x1f

	b	$L14
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
	.word	31
	.word	191
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	192
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	193
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	190
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,240,4

	.comm	g_wbwl_camera_setup_menu_item_array,840,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
