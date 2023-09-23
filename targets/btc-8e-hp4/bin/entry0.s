	.file	1 "entry0.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	get_VideoFormatStructure
	.set	nomips16
	.set	nomicromips
	.ent	get_VideoFormatStructure
	.type	get_VideoFormatStructure, @function
get_VideoFormatStructure:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	move	$2,$0

	.set	macro
	.set	reorder
	.end	get_VideoFormatStructure
	.size	get_VideoFormatStructure, .-get_VideoFormatStructure
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
