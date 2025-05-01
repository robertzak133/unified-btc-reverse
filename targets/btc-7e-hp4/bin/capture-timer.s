	.file	1 "capture-timer.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	ctm_schedule_alarm_global_callback
	.set	nomips16
	.set	nomicromips
	.ent	ctm_schedule_alarm_global_callback
	.type	ctm_schedule_alarm_global_callback, @function
ctm_schedule_alarm_global_callback:
	.frame	$sp,40,$31		# vars= 0, regs= 5/0, args= 16, gp= 0
	.mask	0x800f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	li	$2,1			# 0x1
	beq	$4,$2,$L13
	nop

	addiu	$sp,$sp,-40
	sw	$19,32($sp)
	sw	$18,28($sp)
	sw	$17,24($sp)
	sw	$16,20($sp)
	sw	$31,36($sp)
	move	$16,$4
	move	$17,$5
	move	$18,$6
	jal	get_within_operating_hours_p
	move	$19,$7

	beq	$2,$0,$L12
	lw	$31,36($sp)

	jal	get_cold_item_timelapse_period
	nop

	li	$3,5			# 0x5
	beq	$2,$3,$L1
	lw	$31,36($sp)

	move	$7,$19
	move	$6,$18
	lw	$19,32($sp)
	lw	$18,28($sp)
	move	$5,$17
	move	$4,$16
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	schedule_alarm_global_callback
	addiu	$sp,$sp,40

$L1:
$L12:
	lw	$19,32($sp)
	lw	$18,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,40

$L13:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	ctm_schedule_alarm_global_callback
	.size	ctm_schedule_alarm_global_callback, .-ctm_schedule_alarm_global_callback
	.align	2
	.globl	ctm_tty_printf
	.set	nomips16
	.set	nomicromips
	.ent	ctm_tty_printf
	.type	ctm_tty_printf, @function
ctm_tty_printf:
	.frame	$sp,32,$31		# vars= 8, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$31,28($sp)
	sw	$4,20($sp)
	jal	set_pre_printf_state
	sw	$5,16($sp)

	lw	$5,16($sp)
	jal	tty_printf
	lw	$4,20($sp)

	lw	$31,28($sp)
	j	check_post_printf_state_set_sio_params
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	ctm_tty_printf
	.size	ctm_tty_printf, .-ctm_tty_printf

	.comm	g_rtc_time_format_menu,84,4

	.comm	g_rtc_date_format_menu,140,4

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,240,4

	.comm	g_wbwl_camera_setup_menu_item_array,840,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
