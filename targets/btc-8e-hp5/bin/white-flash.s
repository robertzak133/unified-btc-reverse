	.file	1 "white-flash.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	wfl_setSensorDigitalEffectPhoto
	.set	nomips16
	.set	nomicromips
	.ent	wfl_setSensorDigitalEffectPhoto
	.type	wfl_setSensorDigitalEffectPhoto, @function
wfl_setSensorDigitalEffectPhoto:
	.frame	$sp,24,$31		# vars= 0, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$16,16($sp)
	sw	$31,20($sp)
	jal	apt_get_cold_item_aperture
	move	$16,$4

	li	$3,2			# 0x2
	beql	$2,$3,$L2
	move	$16,$0

$L2:
	lw	$31,20($sp)
	move	$4,$16
	lw	$16,16($sp)
	j	setSensorDigitalEffectPhoto
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	wfl_setSensorDigitalEffectPhoto
	.size	wfl_setSensorDigitalEffectPhoto, .-wfl_setSensorDigitalEffectPhoto
	.align	2
	.globl	wfl_setSensorDigitalEffectVideo
	.set	nomips16
	.set	nomicromips
	.ent	wfl_setSensorDigitalEffectVideo
	.type	wfl_setSensorDigitalEffectVideo, @function
wfl_setSensorDigitalEffectVideo:
	.frame	$sp,24,$31		# vars= 0, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$16,16($sp)
	sw	$31,20($sp)
	jal	apt_get_cold_item_aperture
	move	$16,$4

	li	$3,2			# 0x2
	beql	$2,$3,$L5
	move	$16,$0

$L5:
	lw	$31,20($sp)
	move	$4,$16
	lw	$16,16($sp)
	j	setSensorDigitalEffectVideo
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	wfl_setSensorDigitalEffectVideo
	.size	wfl_setSensorDigitalEffectVideo, .-wfl_setSensorDigitalEffectVideo
	.align	2
	.globl	wfl_HceIRCut_SetIRCutOpen
	.set	nomips16
	.set	nomicromips
	.ent	wfl_HceIRCut_SetIRCutOpen
	.type	wfl_HceIRCut_SetIRCutOpen, @function
wfl_HceIRCut_SetIRCutOpen:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	apt_get_cold_item_aperture
	nop

	li	$3,2			# 0x2
	beq	$2,$3,$L7
	lw	$31,20($sp)

	j	HceIRCut_SetIRCutOpen
	addiu	$sp,$sp,24

$L7:
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	wfl_HceIRCut_SetIRCutOpen
	.size	wfl_HceIRCut_SetIRCutOpen, .-wfl_HceIRCut_SetIRCutOpen
	.align	2
	.globl	wfl_video_log_printf
	.set	nomips16
	.set	nomicromips
	.ent	wfl_video_log_printf
	.type	wfl_video_log_printf, @function
wfl_video_log_printf:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	log_printf
	nop

	.set	macro
	.set	reorder
	.end	wfl_video_log_printf
	.size	wfl_video_log_printf, .-wfl_video_log_printf
	.align	2
	.globl	wfl_spawnIRCutFSM_per_mode
	.set	nomips16
	.set	nomicromips
	.ent	wfl_spawnIRCutFSM_per_mode
	.type	wfl_spawnIRCutFSM_per_mode, @function
wfl_spawnIRCutFSM_per_mode:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$31,28($sp)
	sw	$17,24($sp)
	jal	apt_get_cold_item_aperture
	sw	$16,20($sp)

	jal	get_cold_item_operation_mode
	move	$17,$2

	jal	tlps_get_cold_item_raw_timelapse_period
	move	$16,$2

	move	$3,$2
	lui	$2,%hi(g_night_mode_p)
	lbu	$5,%lo(g_night_mode_p)($2)
	li	$2,1			# 0x1
	bne	$5,$2,$L12
	move	$4,$0

	li	$5,2			# 0x2
	beq	$17,$5,$L12
	sltu	$2,$16,2

	bne	$2,$0,$L12
	li	$4,1			# 0x1

	bne	$16,$5,$L12
	move	$4,$0

	xori	$3,$3,0x5
	sltu	$4,$3,1
$L12:
	lw	$31,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	IRCutThreadCreate
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	wfl_spawnIRCutFSM_per_mode
	.size	wfl_spawnIRCutFSM_per_mode, .-wfl_spawnIRCutFSM_per_mode

	.comm	g_wbwl_timelapse_frequency_lookup_table,24,4

	.comm	g_tlps_file_type_menu,84,4

	.comm	g_wbwl_timelapse_frequency_menu,364,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
