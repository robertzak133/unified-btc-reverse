	.file	1 "capture-timer.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
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

	.comm	g_wbwl_camera_setup_selector_array,248,4

	.comm	g_wbwl_camera_setup_menu_item_array,868,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
