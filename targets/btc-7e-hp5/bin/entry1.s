	.file	1 "entry1.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	cli_command_function
	.set	nomips16
	.set	nomicromips
	.ent	cli_command_function
	.type	cli_command_function, @function
cli_command_function:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	cli_command_function
	.size	cli_command_function, .-cli_command_function
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
