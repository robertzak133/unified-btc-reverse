	.file	1 "dslr-trigger.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	dslr_get_cold_item_dslr_trigger_p
	.set	nomips16
	.set	nomicromips
	.ent	dslr_get_cold_item_dslr_trigger_p
	.type	dslr_get_cold_item_dslr_trigger_p, @function
dslr_get_cold_item_dslr_trigger_p:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+81)
	lbu	$2,%lo(g_ColdItemData+81)($2)
	srl	$2,$2,5
	jr	$31
	andi	$2,$2,0x1

	.set	macro
	.set	reorder
	.end	dslr_get_cold_item_dslr_trigger_p
	.size	dslr_get_cold_item_dslr_trigger_p, .-dslr_get_cold_item_dslr_trigger_p
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
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	dslr_get_cold_item_dslr_trigger_p
	li	$3,1			# 0x1

	bne	$2,$3,$L5
	lw	$31,20($sp)

	jal	Write_LEDOn
	nop

	lw	$31,20($sp)
$L5:
	j	cold_item_led_power_blur_reduction_p
	addiu	$sp,$sp,24

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
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	log_printf
	nop

	jal	dslr_get_cold_item_dslr_trigger_p
	li	$3,1			# 0x1

	bne	$2,$3,$L6
	lw	$31,20($sp)

	j	Write_LEDOn
	addiu	$sp,$sp,24

$L6:
	jr	$31
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
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	IRLedOff
	nop

	jal	dslr_get_cold_item_dslr_trigger_p
	li	$3,1			# 0x1

	bne	$2,$3,$L9
	lw	$31,20($sp)

	j	Write_LEDOff
	addiu	$sp,$sp,24

$L9:
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	dt_IRLedOff
	.size	dt_IRLedOff, .-dt_IRLedOff
	.align	2
	.globl	dslr_set_cold_item_dslr_trigger_p
	.set	nomips16
	.set	nomicromips
	.ent	dslr_set_cold_item_dslr_trigger_p
	.type	dslr_set_cold_item_dslr_trigger_p, @function
dslr_set_cold_item_dslr_trigger_p:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$3,%hi(g_ColdItemData)
	addiu	$3,$3,%lo(g_ColdItemData)
	lbu	$2,81($3)
	sll	$4,$4,5
	andi	$4,$4,0x20
	andi	$2,$2,0xdf
	or	$2,$2,$4
	jr	$31
	sb	$2,81($3)

	.set	macro
	.set	reorder
	.end	dslr_set_cold_item_dslr_trigger_p
	.size	dslr_set_cold_item_dslr_trigger_p, .-dslr_set_cold_item_dslr_trigger_p
	.align	2
	.globl	dslr_handle_led_enable_menu
	.set	nomips16
	.set	nomicromips
	.ent	dslr_handle_led_enable_menu
	.type	dslr_handle_led_enable_menu, @function
dslr_handle_led_enable_menu:
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
	beq	$17,$0,$L14
	move	$16,$2

	jal	dslr_get_cold_item_dslr_trigger_p
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

$L14:
	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L15
	lui	$2,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L27
	lui	$18,%hi(g_menu_root)

$L15:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L17
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L16
	lui	$18,%hi(g_menu_root)

$L17:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$3,1			# 0x1
	beq	$2,$3,$L18
	lui	$2,%hi(g_left_button_enable)

$L19:
	jal	ui_cursor_key_pressed_p
	li	$4,3			# 0x3

	li	$3,1			# 0x1
	bne	$2,$3,$L21
	lui	$2,%hi(g_right_button_enable)

	lbu	$3,%lo(g_right_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L28
	lw	$31,28($sp)

$L21:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L23
	lui	$2,%hi(g_enter_button_enable)

	lbu	$3,%lo(g_enter_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L23
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
	beq	$5,$2,$L28
	lw	$31,28($sp)

	jal	dslr_set_cold_item_dslr_trigger_p
	lbu	$4,2($16)

	sb	$17,6($16)
$L24:
	lw	$31,28($sp)
$L26:
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	move	$4,$5
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L16:
$L27:
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

$L18:
	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L19
	lw	$31,28($sp)

$L28:
	lw	$18,24($sp)
$L29:
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,32

$L23:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L28
	lw	$31,28($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L29
	lw	$18,24($sp)

	lui	$5,%hi(g_menu_root)
	addiu	$5,$5,%lo(g_menu_root)
	sb	$2,0($16)
	jal	get_next_state_from_menu_mode
	li	$4,1			# 0x1

	move	$5,$2
	li	$2,255			# 0xff
	beql	$5,$2,$L24
	li	$5,37			# 0x25

	b	$L26
	lw	$31,28($sp)

	.set	macro
	.set	reorder
	.end	dslr_handle_led_enable_menu
	.size	dslr_handle_led_enable_menu, .-dslr_handle_led_enable_menu
	.globl	g_dlsr_led_enable_menu
	.data
	.align	2
	.type	g_dlsr_led_enable_menu, @object
	.size	g_dlsr_led_enable_menu, 84
g_dlsr_led_enable_menu:
	.word	32
	.word	8
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	9
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	193
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3

	.comm	g_wbwl_menu_handler_function_array_extensions,28,4

	.comm	g_wbwl_camera_setup_selector_array,256,4

	.comm	g_wbwl_camera_setup_menu_item_array,896,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
