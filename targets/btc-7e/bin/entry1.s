	.file	1 "entry1.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	print_SD_CSD
	.set	nomips16
	.set	nomicromips
	.ent	print_SD_CSD
	.type	print_SD_CSD, @function
print_SD_CSD:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	print_SD_CSD
	.size	print_SD_CSD, .-print_SD_CSD
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
