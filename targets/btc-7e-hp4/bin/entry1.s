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
	.ascii	"Error::WBWL - cmdFPGA_CdspPV() not implemented in this p"
	.ascii	"atched firmware version\000"
	.text
	.align	2
	.globl	cmdFPGA_CdspPV
	.set	nomips16
	.set	nomicromips
	.ent	cmdFPGA_CdspPV
	.type	cmdFPGA_CdspPV, @function
cmdFPGA_CdspPV:
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
	.end	cmdFPGA_CdspPV
	.size	cmdFPGA_CdspPV, .-cmdFPGA_CdspPV
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04) 9.4.0"
