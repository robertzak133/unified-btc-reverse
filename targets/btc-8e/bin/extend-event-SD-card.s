	.file	1 "extend-event-SD-card.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	evsd_set_cold_item_sd_management_p
	.set	nomips16
	.set	nomicromips
	.ent	evsd_set_cold_item_sd_management_p
	.type	evsd_set_cold_item_sd_management_p, @function
evsd_set_cold_item_sd_management_p:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+93)
	lbu	$2,%lo(g_ColdItemData+93)($2)
	andi	$4,$4,0x1
	andi	$2,$2,0xfe
	j	set_cold_item_sd_management_p
	or	$4,$2,$4

	.set	macro
	.set	reorder
	.end	evsd_set_cold_item_sd_management_p
	.size	evsd_set_cold_item_sd_management_p, .-evsd_set_cold_item_sd_management_p
	.align	2
	.globl	evsd_get_cold_item_sd_management_p
	.set	nomips16
	.set	nomicromips
	.ent	evsd_get_cold_item_sd_management_p
	.type	evsd_get_cold_item_sd_management_p, @function
evsd_get_cold_item_sd_management_p:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	get_cold_item_sd_management_p
	nop

	lw	$31,20($sp)
	andi	$2,$2,0x1
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	evsd_get_cold_item_sd_management_p
	.size	evsd_get_cold_item_sd_management_p, .-evsd_get_cold_item_sd_management_p
	.align	2
	.globl	evsd_set_cold_item_extended_sd_power_p
	.set	nomips16
	.set	nomicromips
	.ent	evsd_set_cold_item_extended_sd_power_p
	.type	evsd_set_cold_item_extended_sd_power_p, @function
evsd_set_cold_item_extended_sd_power_p:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+93)
	lbu	$2,%lo(g_ColdItemData+93)($2)
	sll	$4,$4,1
	andi	$4,$4,0x2
	andi	$2,$2,0xfd
	j	set_cold_item_sd_management_p
	or	$4,$2,$4

	.set	macro
	.set	reorder
	.end	evsd_set_cold_item_extended_sd_power_p
	.size	evsd_set_cold_item_extended_sd_power_p, .-evsd_set_cold_item_extended_sd_power_p
	.align	2
	.globl	evsd_get_cold_item_extended_sd_power_p
	.set	nomips16
	.set	nomicromips
	.ent	evsd_get_cold_item_extended_sd_power_p
	.type	evsd_get_cold_item_extended_sd_power_p, @function
evsd_get_cold_item_extended_sd_power_p:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+93)
	lbu	$2,%lo(g_ColdItemData+93)($2)
	srl	$2,$2,1
	jr	$31
	andi	$2,$2,0x1

	.set	macro
	.set	reorder
	.end	evsd_get_cold_item_extended_sd_power_p
	.size	evsd_get_cold_item_extended_sd_power_p, .-evsd_get_cold_item_extended_sd_power_p
	.align	2
	.globl	evsd_check_remaining_sd_capacity
	.set	nomips16
	.set	nomicromips
	.ent	evsd_check_remaining_sd_capacity
	.type	evsd_check_remaining_sd_capacity, @function
evsd_check_remaining_sd_capacity:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	check_remaining_sd_capacity
	nop

	jal	evsd_get_cold_item_extended_sd_power_p
	li	$3,1			# 0x1

	bne	$2,$3,$L6
	lw	$31,20($sp)

	li	$5,30000			# 0x7530
	li	$4,3			# 0x3
	j	thread_sleep
	addiu	$sp,$sp,24

$L6:
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	evsd_check_remaining_sd_capacity
	.size	evsd_check_remaining_sd_capacity, .-evsd_check_remaining_sd_capacity
	.align	2
	.globl	evsd_handle_extended_sd_power_menu
	.set	nomips16
	.set	nomicromips
	.ent	evsd_handle_extended_sd_power_menu
	.type	evsd_handle_extended_sd_power_menu, @function
evsd_handle_extended_sd_power_menu:
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
	beq	$17,$0,$L10
	move	$16,$2

	jal	evsd_get_cold_item_extended_sd_power_p
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

$L10:
	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L11
	lui	$2,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L23
	lui	$18,%hi(g_menu_root)

$L11:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L13
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L12
	lui	$18,%hi(g_menu_root)

$L13:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$3,1			# 0x1
	beq	$2,$3,$L14
	lui	$2,%hi(g_left_button_enable)

$L15:
	jal	ui_cursor_key_pressed_p
	li	$4,3			# 0x3

	li	$3,1			# 0x1
	bne	$2,$3,$L17
	lui	$2,%hi(g_right_button_enable)

	lbu	$3,%lo(g_right_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L24
	lw	$31,28($sp)

$L17:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	move	$18,$2
	li	$2,1			# 0x1
	bne	$18,$2,$L19
	lui	$2,%hi(g_enter_button_enable)

	lbu	$3,%lo(g_enter_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L19
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
	beq	$17,$2,$L24
	lw	$31,28($sp)

	jal	evsd_set_cold_item_extended_sd_power_p
	lbu	$4,2($16)

	sb	$18,6($16)
$L20:
	lw	$31,28($sp)
$L22:
	lw	$18,24($sp)
	lw	$16,16($sp)
	move	$4,$17
	lw	$17,20($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L12:
$L23:
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

$L14:
	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L15
	lw	$31,28($sp)

$L24:
	lw	$18,24($sp)
$L25:
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,32

$L19:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L24
	lw	$31,28($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L25
	lw	$18,24($sp)

	lui	$5,%hi(g_menu_root)
	sb	$2,0($16)
	addiu	$5,$5,%lo(g_menu_root)
	jal	get_next_state_from_menu_mode
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,255			# 0xff
	beql	$17,$2,$L20
	li	$17,35			# 0x23

	b	$L22
	lw	$31,28($sp)

	.set	macro
	.set	reorder
	.end	evsd_handle_extended_sd_power_menu
	.size	evsd_handle_extended_sd_power_menu, .-evsd_handle_extended_sd_power_menu
	.globl	g_evsd_extended_sd_power_menu
	.data
	.align	2
	.type	g_evsd_extended_sd_power_menu, @object
	.size	g_evsd_extended_sd_power_menu, 84
g_evsd_extended_sd_power_menu:
	.word	31
	.word	8
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	9
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	176
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,240,4

	.comm	g_wbwl_camera_setup_menu_item_array,840,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
