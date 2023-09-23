	.file	1 "no-dslr.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	dslr_LEDOn
	.set	nomips16
	.set	nomicromips
	.ent	dslr_LEDOn
	.type	dslr_LEDOn, @function
dslr_LEDOn:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	dslr_LEDOn
	.size	dslr_LEDOn, .-dslr_LEDOn
	.align	2
	.globl	dslr_LEDOff
	.set	nomips16
	.set	nomicromips
	.ent	dslr_LEDOff
	.type	dslr_LEDOff, @function
dslr_LEDOff:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	dslr_LEDOff
	.size	dslr_LEDOff, .-dslr_LEDOff
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
