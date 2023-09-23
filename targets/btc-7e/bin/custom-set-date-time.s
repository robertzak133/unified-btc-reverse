	.file	1 "custom-set-date-time.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	cdt_get_max_hour
	.set	nomips16
	.set	nomicromips
	.ent	cdt_get_max_hour
	.type	cdt_get_max_hour, @function
cdt_get_max_hour:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	li	$2,23			# 0x17

	.set	macro
	.set	reorder
	.end	cdt_get_max_hour
	.size	cdt_get_max_hour, .-cdt_get_max_hour
	.align	2
	.globl	cdt_get_min_hour
	.set	nomips16
	.set	nomicromips
	.ent	cdt_get_min_hour
	.type	cdt_get_min_hour, @function
cdt_get_min_hour:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	move	$2,$0

	.set	macro
	.set	reorder
	.end	cdt_get_min_hour
	.size	cdt_get_min_hour, .-cdt_get_min_hour
	.align	2
	.globl	cdt_get_set_date_time_functions
	.set	nomips16
	.set	nomicromips
	.ent	cdt_get_set_date_time_functions
	.type	cdt_get_set_date_time_functions, @function
cdt_get_set_date_time_functions:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	sltu	$2,$4,8
	beq	$2,$0,$L4
	sll	$4,$4,2

	lui	$2,%hi($L6)
	addiu	$2,$2,%lo($L6)
	addu	$4,$2,$4
	lw	$2,0($4)
	jr	$2
	nop

	.rdata
	.align	2
	.align	2
$L6:
	.word	$L10
	.word	$L4
	.word	$L9
	.word	$L4
	.word	$L8
	.word	$L7
	.word	$L4
	.word	$L5
	.text
$L10:
	lui	$2,%hi(get_g_menu_temp_month)
	addiu	$2,$2,%lo(get_g_menu_temp_month)
	sw	$2,0($7)
	lui	$2,%hi(get_min_month)
	addiu	$2,$2,%lo(get_min_month)
	sw	$2,4($7)
	lui	$2,%hi(get_max_month)
	addiu	$2,$2,%lo(get_max_month)
$L13:
	jr	$31
	sw	$2,8($7)

$L9:
	lui	$2,%hi(get_g_temp_day_number)
	addiu	$2,$2,%lo(get_g_temp_day_number)
	sw	$2,0($7)
	lui	$2,%hi(get_min_day)
	addiu	$2,$2,%lo(get_min_day)
	sw	$2,4($7)
	lui	$2,%hi(get_max_day)
	b	$L13
	addiu	$2,$2,%lo(get_max_day)

$L8:
	lui	$2,%hi(get_g_menu_temp_year)
	addiu	$2,$2,%lo(get_g_menu_temp_year)
	sw	$2,0($7)
	lui	$2,%hi(get_min_year)
	addiu	$2,$2,%lo(get_min_year)
	sw	$2,4($7)
	lui	$2,%hi(get_max_year)
	b	$L13
	addiu	$2,$2,%lo(get_max_year)

$L7:
	lui	$2,%hi(get_g_menu_temp_hour)
	addiu	$2,$2,%lo(get_g_menu_temp_hour)
	bne	$6,$0,$L12
	sw	$2,0($7)

	lui	$2,%hi(get_min_hour)
	addiu	$2,$2,%lo(get_min_hour)
	sw	$2,4($7)
	lui	$2,%hi(get_max_hour)
	b	$L13
	addiu	$2,$2,%lo(get_max_hour)

$L12:
	lui	$2,%hi(cdt_get_min_hour)
	addiu	$2,$2,%lo(cdt_get_min_hour)
	sw	$2,4($7)
	lui	$2,%hi(cdt_get_max_hour)
	b	$L13
	addiu	$2,$2,%lo(cdt_get_max_hour)

$L5:
	lui	$2,%hi(get_g_menu_temp_minute)
	addiu	$2,$2,%lo(get_g_menu_temp_minute)
	sw	$2,0($7)
	lui	$2,%hi(get_min_minute)
	addiu	$2,$2,%lo(get_min_minute)
	sw	$2,4($7)
	lui	$2,%hi(get_max_minute)
	b	$L13
	addiu	$2,$2,%lo(get_max_minute)

$L4:
	lui	$2,%hi(get_am_pm_current_value)
	addiu	$2,$2,%lo(get_am_pm_current_value)
	sw	$2,0($7)
	lui	$2,%hi(get_am_pm_min_value)
	addiu	$2,$2,%lo(get_am_pm_min_value)
	sw	$2,4($7)
	lui	$2,%hi(get_am_pm_max_value)
	b	$L13
	addiu	$2,$2,%lo(get_am_pm_max_value)

	.set	macro
	.set	reorder
	.end	cdt_get_set_date_time_functions
	.size	cdt_get_set_date_time_functions, .-cdt_get_set_date_time_functions
	.align	2
	.globl	cdt_handle_left_right_buttons
	.set	nomips16
	.set	nomicromips
	.ent	cdt_handle_left_right_buttons
	.type	cdt_handle_left_right_buttons, @function
cdt_handle_left_right_buttons:
	.frame	$sp,40,$31		# vars= 0, regs= 4/0, args= 24, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$31,36($sp)
	sw	$18,32($sp)
	sw	$17,28($sp)
	sw	$16,24($sp)
	move	$18,$4
	jal	get_g_temp_day_number
	move	$16,$5

	jal	get_max_day
	move	$17,$2

	sltu	$17,$2,$17
	beq	$17,$0,$L17
	xori	$4,$16,0x1

	lui	$3,%hi(g_set_date_time_menu_state+4)
	sh	$2,%lo(g_set_date_time_menu_state+4)($3)
$L17:
	li	$3,10			# 0xa
	lui	$7,%hi(g_set_time_buffer)
	sw	$3,16($sp)
	addiu	$5,$18,2
	addiu	$7,$7,%lo(g_set_time_buffer)
	li	$6,1			# 0x1
	jal	update_time_field
	sltu	$4,$0,$4

	lw	$31,36($sp)
	lw	$18,32($sp)
	lw	$17,28($sp)
	lw	$16,24($sp)
	jr	$31
	addiu	$sp,$sp,40

	.set	macro
	.set	reorder
	.end	cdt_handle_left_right_buttons
	.size	cdt_handle_left_right_buttons, .-cdt_handle_left_right_buttons
	.align	2
	.globl	cdt_twelve_to_twenty_four
	.set	nomips16
	.set	nomicromips
	.ent	cdt_twelve_to_twenty_four
	.type	cdt_twelve_to_twenty_four, @function
cdt_twelve_to_twenty_four:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	move	$2,$5
	bne	$4,$0,$L19
	li	$3,12			# 0xc

	beql	$5,$3,$L23
	move	$2,$0

$L23:
	jr	$31
	nop

$L19:
	beq	$5,$3,$L22
	nop

	addiu	$2,$5,12
	sll	$2,$2,16
	sra	$2,$2,16
$L22:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	cdt_twelve_to_twenty_four
	.size	cdt_twelve_to_twenty_four, .-cdt_twelve_to_twenty_four
	.align	2
	.globl	cdt_menu_draw_selected_item
	.set	nomips16
	.set	nomicromips
	.ent	cdt_menu_draw_selected_item
	.type	cdt_menu_draw_selected_item, @function
cdt_menu_draw_selected_item:
	.frame	$sp,40,$31		# vars= 0, regs= 5/0, args= 16, gp= 0
	.mask	0x800f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$19,32($sp)
	sw	$18,28($sp)
	sw	$17,24($sp)
	sw	$16,20($sp)
	sw	$31,36($sp)
	move	$17,$4
	move	$18,$5
	jal	rtc_get_cold_item_time_format
	lui	$16,%hi(g_set_date_time_menu_state)

	move	$19,$2
	jal	get_current_date_time_short
	addiu	$4,$16,%lo(g_set_date_time_menu_state)

	bne	$19,$0,$L27
	lw	$31,36($sp)

	addiu	$16,$16,%lo(g_set_date_time_menu_state)
	lui	$2,%hi(g_temp_am_pm_p)
	lh	$5,6($16)
	jal	cdt_twelve_to_twenty_four
	lh	$4,%lo(g_temp_am_pm_p)($2)

	sh	$2,6($16)
	lw	$31,36($sp)
$L27:
	lw	$19,32($sp)
	lw	$16,20($sp)
	move	$5,$18
	move	$4,$17
	lw	$18,28($sp)
	lw	$17,24($sp)
	j	menu_draw_selected_item
	addiu	$sp,$sp,40

	.set	macro
	.set	reorder
	.end	cdt_menu_draw_selected_item
	.size	cdt_menu_draw_selected_item, .-cdt_menu_draw_selected_item
	.align	2
	.globl	cdt_twenty_four_to_twelve
	.set	nomips16
	.set	nomicromips
	.ent	cdt_twenty_four_to_twelve
	.type	cdt_twenty_four_to_twelve, @function
cdt_twenty_four_to_twelve:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	slt	$3,$5,12
	beq	$3,$0,$L29
	move	$2,$5

	bne	$5,$0,$L32
	sh	$0,0($4)

$L31:
	jr	$31
	li	$2,12			# 0xc

$L29:
	li	$3,1			# 0x1
	sh	$3,0($4)
	li	$3,12			# 0xc
	beq	$5,$3,$L31
	nop

	addiu	$2,$5,-12
	sll	$2,$2,16
	sra	$2,$2,16
$L32:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	cdt_twenty_four_to_twelve
	.size	cdt_twenty_four_to_twelve, .-cdt_twenty_four_to_twelve
	.align	2
	.globl	cdt_handle_enter_mode_buttons
	.set	nomips16
	.set	nomicromips
	.ent	cdt_handle_enter_mode_buttons
	.type	cdt_handle_enter_mode_buttons, @function
cdt_handle_enter_mode_buttons:
	.frame	$sp,48,$31		# vars= 16, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-48
	li	$2,1			# 0x1
	sw	$31,44($sp)
	sw	$17,40($sp)
	sw	$16,36($sp)
	beq	$5,$0,$L34
	sb	$2,0($4)

	jal	get_g_temp_day_number
	move	$17,$4

	jal	get_max_day
	move	$16,$2

	sltu	$3,$2,$16
	lui	$16,%hi(g_set_date_time_menu_state)
	beq	$3,$0,$L35
	addiu	$16,$16,%lo(g_set_date_time_menu_state)

	sh	$2,4($16)
$L35:
	jal	rtc_get_cold_item_time_format
	nop

	bne	$2,$0,$L46
	move	$4,$16

	lui	$2,%hi(g_temp_am_pm_p)
	lh	$5,6($16)
	jal	cdt_twelve_to_twenty_four
	lh	$4,%lo(g_temp_am_pm_p)($2)

	sh	$2,6($16)
	move	$4,$16
$L46:
	jal	hal_set_rtc
	sh	$0,10($16)

	jal	get_cold_item_capture_timer_p
	nop

	beq	$2,$0,$L47
	li	$2,1			# 0x1

	jal	get_capture_timer_rtc_time
	addiu	$4,$sp,16

	lw	$5,20($sp)
	jal	reset_capture_timer
	lw	$4,16($sp)

	li	$2,1			# 0x1
$L47:
	sb	$2,6($17)
$L34:
	lui	$5,%hi(g_menu_root)
	li	$4,1			# 0x1
	jal	get_next_state_from_menu_mode
	addiu	$5,$5,%lo(g_menu_root)

	move	$4,$2
	li	$2,255			# 0xff
	beql	$4,$2,$L38
	li	$4,31			# 0x1f

$L38:
	jal	set_fsm_state_absolute
	nop

	lw	$31,44($sp)
	lw	$17,40($sp)
	lw	$16,36($sp)
	jr	$31
	addiu	$sp,$sp,48

	.set	macro
	.set	reorder
	.end	cdt_handle_enter_mode_buttons
	.size	cdt_handle_enter_mode_buttons, .-cdt_handle_enter_mode_buttons
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	" \000"
	.text
	.align	2
	.globl	cdt_btc_strcpy
	.set	nomips16
	.set	nomicromips
	.ent	cdt_btc_strcpy
	.type	cdt_btc_strcpy, @function
cdt_btc_strcpy:
	.frame	$sp,32,$31		# vars= 8, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$16,24($sp)
	sw	$4,16($sp)
	sw	$31,28($sp)
	jal	rtc_get_cold_item_time_format
	move	$16,$5

	li	$3,1			# 0x1
	bne	$2,$3,$L49
	lw	$4,16($sp)

	lb	$2,0($16)
	li	$3,65			# 0x41
	beq	$2,$3,$L50
	li	$3,80			# 0x50

	bnel	$2,$3,$L52
	move	$5,$16

$L50:
	lui	$5,%hi($LC0)
	addiu	$5,$5,%lo($LC0)
$L52:
	lw	$31,28($sp)
	lw	$16,24($sp)
	j	btc_strcpy
	addiu	$sp,$sp,32

$L49:
	b	$L52
	move	$5,$16

	.set	macro
	.set	reorder
	.end	cdt_btc_strcpy
	.size	cdt_btc_strcpy, .-cdt_btc_strcpy
	.align	2
	.globl	cdt_get_date_time_current_field_value
	.set	nomips16
	.set	nomicromips
	.ent	cdt_get_date_time_current_field_value
	.type	cdt_get_date_time_current_field_value, @function
cdt_get_date_time_current_field_value:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	sltu	$2,$4,5
	beql	$2,$0,$L54
	li	$2,5			# 0x5

	beq	$4,$0,$L56
	lui	$2,%hi(g_set_date_time_menu_state+2)

	li	$2,2			# 0x2
	bnel	$4,$2,$L57
	lui	$2,%hi(g_set_date_time_menu_state)

	lui	$2,%hi(g_set_date_time_menu_state+4)
	jr	$31
	addiu	$2,$2,%lo(g_set_date_time_menu_state+4)

$L54:
	beq	$4,$2,$L58
	lui	$2,%hi(g_set_date_time_menu_state+6)

	li	$2,7			# 0x7
	bnel	$4,$2,$L59
	lui	$2,%hi(g_temp_am_pm_p)

	lui	$2,%hi(g_set_date_time_menu_state+8)
	jr	$31
	addiu	$2,$2,%lo(g_set_date_time_menu_state+8)

$L56:
	jr	$31
	addiu	$2,$2,%lo(g_set_date_time_menu_state+2)

$L57:
	jr	$31
	addiu	$2,$2,%lo(g_set_date_time_menu_state)

$L58:
	jr	$31
	addiu	$2,$2,%lo(g_set_date_time_menu_state+6)

$L59:
	jr	$31
	addiu	$2,$2,%lo(g_temp_am_pm_p)

	.set	macro
	.set	reorder
	.end	cdt_get_date_time_current_field_value
	.size	cdt_get_date_time_current_field_value, .-cdt_get_date_time_current_field_value
	.align	2
	.globl	cdt_handle_up_down_buttons
	.set	nomips16
	.set	nomicromips
	.ent	cdt_handle_up_down_buttons
	.type	cdt_handle_up_down_buttons, @function
cdt_handle_up_down_buttons:
	.frame	$sp,64,$31		# vars= 24, regs= 3/0, args= 24, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-64
	sw	$31,60($sp)
	sw	$17,56($sp)
	sw	$16,52($sp)
	move	$17,$5
	jal	rtc_get_cold_item_time_format
	move	$16,$4

	jal	rtc_get_cold_item_date_format
	sw	$2,40($sp)

	move	$5,$2
	lbu	$2,3($16)
	lw	$6,40($sp)
	sltu	$4,$2,3
	beq	$4,$0,$L61
	li	$3,3			# 0x3

	addiu	$2,$2,1
	sb	$2,3($16)
	li	$3,1			# 0x1
$L61:
	lbu	$4,2($16)
	jal	cdt_get_date_time_current_field_value
	sw	$6,40($sp)

	lw	$6,40($sp)
	addiu	$7,$sp,24
	jal	cdt_get_set_date_time_functions
	move	$16,$2

	lw	$7,32($sp)
	lw	$6,28($sp)
	lw	$5,24($sp)
	sw	$3,16($sp)
	jal	HceTask_ToNextNChar
	move	$4,$17

	lw	$31,60($sp)
	lw	$17,56($sp)
	sh	$2,0($16)
	lw	$16,52($sp)
	jr	$31
	addiu	$sp,$sp,64

	.set	macro
	.set	reorder
	.end	cdt_handle_up_down_buttons
	.size	cdt_handle_up_down_buttons, .-cdt_handle_up_down_buttons
	.align	2
	.globl	cdt_check_keyboard
	.set	nomips16
	.set	nomicromips
	.ent	cdt_check_keyboard
	.type	cdt_check_keyboard, @function
cdt_check_keyboard:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$16,20($sp)
	move	$16,$4
	move	$4,$0
	sw	$31,28($sp)
	jal	ui_cursor_key_pressed_p
	sw	$17,24($sp)

	li	$4,1			# 0x1
	jal	ui_cursor_key_pressed_p
	move	$17,$2

	li	$3,1			# 0x1
	bne	$17,$3,$L79
	nop

	lui	$3,%hi(g_up_button_enable)
	lbu	$3,%lo(g_up_button_enable)($3)
	addiu	$3,$3,-2
	andi	$3,$3,0x00ff
	sltu	$3,$3,2
	bne	$3,$0,$L67
	li	$3,1			# 0x1

$L79:
	bne	$2,$3,$L68
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	addiu	$3,$3,-2
	andi	$3,$3,0x00ff
	sltu	$3,$3,2
	beq	$3,$0,$L68
	nop

$L67:
	move	$5,$17
	jal	cdt_handle_up_down_buttons
	move	$4,$16

	li	$2,1			# 0x1
$L65:
	lw	$31,28($sp)
$L82:
	lw	$17,24($sp)
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,32

$L68:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$4,3			# 0x3
	jal	ui_cursor_key_pressed_p
	move	$17,$2

	li	$3,1			# 0x1
	bne	$17,$3,$L80
	nop

	lui	$3,%hi(g_left_button_enable)
	lbu	$3,%lo(g_left_button_enable)($3)
	addiu	$3,$3,-2
	andi	$3,$3,0x00ff
	sltu	$3,$3,2
	bne	$3,$0,$L71
	li	$3,1			# 0x1

$L80:
	bne	$2,$3,$L72
	lui	$2,%hi(g_right_button_enable)

	lbu	$3,%lo(g_right_button_enable)($2)
	addiu	$3,$3,-2
	andi	$3,$3,0x00ff
	sltu	$3,$3,2
	beq	$3,$0,$L72
	nop

$L71:
	move	$5,$17
	jal	cdt_handle_left_right_buttons
	move	$4,$16

	b	$L65
	li	$2,1			# 0x1

$L72:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	li	$4,5			# 0x5
	jal	ui_cursor_key_pressed_p
	move	$17,$2

	move	$4,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L81
	li	$3,1			# 0x1

	lui	$2,%hi(g_enter_button_enable)
	lbu	$3,%lo(g_enter_button_enable)($2)
	addiu	$3,$3,-2
	andi	$3,$3,0x00ff
	sltu	$3,$3,2
	bne	$3,$0,$L74
	li	$3,1			# 0x1

$L81:
	bne	$4,$3,$L65
	move	$2,$0

	lui	$3,%hi(g_mode_button_enable)
	lbu	$3,%lo(g_mode_button_enable)($3)
	addiu	$3,$3,-2
	andi	$3,$3,0x00ff
	sltu	$3,$3,2
	beq	$3,$0,$L82
	lw	$31,28($sp)

$L74:
	move	$5,$17
	jal	cdt_handle_enter_mode_buttons
	move	$4,$16

	b	$L65
	li	$2,1			# 0x1

	.set	macro
	.set	reorder
	.end	cdt_check_keyboard
	.size	cdt_check_keyboard, .-cdt_check_keyboard
	.align	2
	.globl	cdt_handleSetTimeMenu
	.set	nomips16
	.set	nomicromips
	.ent	cdt_handleSetTimeMenu
	.type	cdt_handleSetTimeMenu, @function
cdt_handleSetTimeMenu:
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

	bne	$2,$0,$L84
	move	$16,$2

	jal	handleSetTimeMenu
	nop

$L84:
	lbu	$2,0($16)
	bnel	$2,$0,$L85
	lui	$17,%hi(g_set_date_time_menu_state)

	jal	cdt_check_keyboard
	move	$4,$16

$L86:
	jal	draw_set_time_screen
	lbu	$4,2($16)

	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L88
	lui	$3,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($3)
	bne	$3,$2,$L88
	nop

	sb	$0,3($16)
$L95:
	lw	$31,28($sp)
$L93:
	lw	$17,24($sp)
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,32

$L85:
	addiu	$4,$17,%lo(g_set_date_time_menu_state)
	sb	$0,0($16)
	jal	get_current_date_time_short
	sb	$0,2($16)

	jal	rtc_get_cold_item_time_format
	nop

	bne	$2,$0,$L94
	lui	$5,%hi(g_menu_root)

	addiu	$17,$17,%lo(g_set_date_time_menu_state)
	lh	$5,6($17)
	lui	$4,%hi(g_temp_am_pm_p)
	jal	cdt_twenty_four_to_twelve
	addiu	$4,$4,%lo(g_temp_am_pm_p)

	sh	$2,6($17)
	lui	$5,%hi(g_menu_root)
$L94:
	addiu	$5,$5,%lo(g_menu_root)
	jal	menu_draw_selected_item
	addiu	$4,$16,2

	b	$L86
	nop

$L88:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	li	$3,1			# 0x1
	bne	$2,$3,$L90
	lui	$3,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($3)
	beql	$3,$2,$L95
	sb	$0,3($16)

$L90:
	jal	fsm_getNextState
	nop

	jal	fsm_getCurrentState
	move	$17,$2

	bnel	$17,$2,$L95
	sb	$0,3($16)

	b	$L93
	lw	$31,28($sp)

	.set	macro
	.set	reorder
	.end	cdt_handleSetTimeMenu
	.size	cdt_handleSetTimeMenu, .-cdt_handleSetTimeMenu

	.comm	g_rtc_time_format_menu,84,4

	.comm	g_rtc_date_format_menu,112,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
