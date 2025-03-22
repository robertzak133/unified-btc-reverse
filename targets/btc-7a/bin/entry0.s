	.file	1 "entry0.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	print_disk_handle
	.set	nomips16
	.set	nomicromips
	.ent	print_disk_handle
	.type	print_disk_handle, @function
print_disk_handle:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	print_disk_handle
	.size	print_disk_handle, .-print_disk_handle
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
