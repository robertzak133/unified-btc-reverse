	.file	1 "entry1.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"Error::WBWL -  cli_command_function() not implemented in"
	.ascii	" this patched firmware version\000"
	.text
	.align	2
	.globl	cli_command_function
	.set	nomips16
	.set	nomicromips
	.ent	cli_command_function
	.type	cli_command_function, @function
cli_command_function:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC0)
	jal	tty_printf
	addiu	$4,$4,%lo($LC0)

	lw	$31,20($sp)
	j	check_post_printf_state_set_sio_params
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	cli_command_function
	.size	cli_command_function, .-cli_command_function
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
