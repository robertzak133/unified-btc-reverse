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

	jal	get_sd_clock_kHz
	move	$16,$2

	li	$3,65536			# 0x10000
	ori	$3,$3,0x86a0
	sltu	$2,$2,$3
	bne	$2,$0,$L4
	lw	$31,20($sp)

	lui	$4,%hi(g_sd_card_descriptor)
	jal	reduce_SD_clock
	addiu	$4,$4,%lo(g_sd_card_descriptor)

	lw	$31,20($sp)
$L4:
	move	$2,$16
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	rsc_initialize_sd_card_to_data
	.size	rsc_initialize_sd_card_to_data, .-rsc_initialize_sd_card_to_data
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
