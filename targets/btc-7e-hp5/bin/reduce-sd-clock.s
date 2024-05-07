	.file	1 "reduce-sd-clock.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	rsc_initialize_sd_card_to_data
	.set	nomips16
	.set	nomicromips
	.ent	rsc_initialize_sd_card_to_data
	.type	rsc_initialize_sd_card_to_data, @function
rsc_initialize_sd_card_to_data:
	.frame	$sp,24,$31		# vars= 0, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	li	$4,2			# 0x2
	sw	$31,20($sp)
	jal	initialize_sd_card_to_data
	sw	$16,16($sp)

	lui	$4,%hi(g_sd_card_descriptor)
	addiu	$4,$4,%lo(g_sd_card_descriptor)
	jal	reduce_SD_clock
	move	$16,$2

	lw	$31,20($sp)
	move	$2,$16
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	rsc_initialize_sd_card_to_data
	.size	rsc_initialize_sd_card_to_data, .-rsc_initialize_sd_card_to_data
	.align	2
	.globl	rsc_log_printf
	.set	nomips16
	.set	nomicromips
	.ent	rsc_log_printf
	.type	rsc_log_printf, @function
rsc_log_printf:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	rsc_log_printf
	.size	rsc_log_printf, .-rsc_log_printf
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
