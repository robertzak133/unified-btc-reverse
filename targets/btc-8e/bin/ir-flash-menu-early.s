	.file	1 "ir-flash-menu-early.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	ifm_power_on_IR_LED
	.set	nomips16
	.set	nomicromips
	.ent	ifm_power_on_IR_LED
	.type	ifm_power_on_IR_LED, @function
ifm_power_on_IR_LED:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	get_g_cold_item_led_power
	nop

	li	$3,2			# 0x2
	beq	$2,$3,$L1
	lw	$31,20($sp)

	j	power_on_IR_LED
	addiu	$sp,$sp,24

$L1:
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	ifm_power_on_IR_LED
	.size	ifm_power_on_IR_LED, .-ifm_power_on_IR_LED

	.comm	g_ifm_ir_led_power_menu,112,4

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,240,4

	.comm	g_wbwl_camera_setup_menu_item_array,840,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
