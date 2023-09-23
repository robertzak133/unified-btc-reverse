	.file	1 "entry0.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"WBWL\000"
	.text
	.align	2
	.globl	MakeShortNameByLongName
	.set	nomips16
	.set	nomicromips
	.ent	MakeShortNameByLongName
	.type	MakeShortNameByLongName, @function
MakeShortNameByLongName:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$5,%hi($LC0)
	addiu	$sp,$sp,-24
	move	$4,$6
	sw	$31,20($sp)
	jal	btc_strcpy
	addiu	$5,$5,%lo($LC0)

	lw	$31,20($sp)
	li	$2,1			# 0x1
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	MakeShortNameByLongName
	.size	MakeShortNameByLongName, .-MakeShortNameByLongName
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
