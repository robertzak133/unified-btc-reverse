	.file	1 "white-flash.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	wf_setDigitalEffect
	.set	nomips16
	.set	nomicromips
	.ent	wf_setDigitalEffect
	.type	wf_setDigitalEffect, @function
wf_setDigitalEffect:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_run_iq_init_function_p)
	lbu	$3,%lo(g_run_iq_init_function_p)($2)
	addiu	$sp,$sp,-32
	sw	$16,20($sp)
	sw	$31,28($sp)
	sw	$17,24($sp)
	beq	$3,$0,$L2
	move	$16,$2

	jal	get_DAT_80357b60_at_global_index
	lui	$17,%hi(g_iq_init_function_param)

	move	$4,$2
	jal	setSensor_configB
	sb	$2,%lo(g_iq_init_function_param)($17)

	li	$7,131072			# 0x20000
	li	$4,35			# 0x23
	addiu	$7,$7,8193
	li	$6,1			# 0x1
	jal	dispatch_IQ_function
	move	$5,$0

	jal	setSensor_configA
	lbu	$4,%lo(g_iq_init_function_param)($17)

$L2:
	li	$4,131072			# 0x20000
	move	$5,$0
	addiu	$4,$4,8193
	jal	sp5kIqCfgSet
	sb	$0,%lo(g_run_iq_init_function_p)($16)

	move	$5,$0
	li	$4,43			# 0x2b
	jal	sp5kIqBlockEnable
	li	$16,262144			# 0x40000

	move	$5,$0
	jal	sp5kIqBlockEnable
	li	$4,44			# 0x2c

	addiu	$4,$16,8192
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8193
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8194
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8195
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8196
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8197
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8198
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8217
	jal	sp5kIqCfgSet
	li	$5,1			# 0x1

	addiu	$4,$16,8218
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8219
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8220
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8221
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8199
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8200
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8201
	jal	sp5kIqCfgSet
	li	$5,3			# 0x3

	addiu	$4,$16,8202
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8203
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8204
	jal	sp5kIqCfgSet
	li	$5,7			# 0x7

	addiu	$4,$16,8205
	jal	sp5kIqCfgSet
	li	$5,7			# 0x7

	addiu	$4,$16,8206
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8207
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8208
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8209
	jal	sp5kIqCfgSet
	li	$5,128			# 0x80

	addiu	$4,$16,8210
	jal	sp5kIqCfgSet
	li	$5,128			# 0x80

	addiu	$4,$16,8211
	jal	sp5kIqCfgSet
	li	$5,128			# 0x80

	addiu	$4,$16,8212
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8213
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8214
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8215
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8216
	jal	sp5kIqCfgSet
	li	$5,255			# 0xff

	addiu	$4,$16,8222
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8223
	jal	sp5kIqCfgSet
	li	$5,1			# 0x1

	addiu	$4,$16,8224
	jal	sp5kIqCfgSet
	li	$5,1			# 0x1

	lui	$5,%hi(g_iq_init_color_param)
	addiu	$4,$16,8225
	jal	sp5kIqCfgSet
	addiu	$5,$5,%lo(g_iq_init_color_param)

	addiu	$4,$16,8226
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8227
	jal	sp5kIqCfgSet
	move	$5,$0

	addiu	$4,$16,8228
	jal	sp5kIqCfgSet
	li	$5,1			# 0x1

	addiu	$4,$16,8229
	jal	sp5kIqCfgSet
	move	$5,$0

	lw	$31,28($sp)
	lw	$17,24($sp)
	addiu	$4,$16,8230
	lw	$16,20($sp)
	move	$5,$0
	j	sp5kIqCfgSet
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	wf_setDigitalEffect
	.size	wf_setDigitalEffect, .-wf_setDigitalEffect
	.align	2
	.globl	cp_setSensorDigitalEffectPhoto
	.set	nomips16
	.set	nomicromips
	.ent	cp_setSensorDigitalEffectPhoto
	.type	cp_setSensorDigitalEffectPhoto, @function
cp_setSensorDigitalEffectPhoto:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	li	$3,1			# 0x1
	lui	$2,%hi(g_photo_mode_p)
	sb	$3,%lo(g_photo_mode_p)($2)
	lui	$2,%hi(g_night_mode_p)
	addiu	$sp,$sp,-24
	sb	$4,%lo(g_night_mode_p)($2)
	sw	$31,20($sp)
	jal	set_aaa_ae_pipeline_wrapper
	li	$4,2			# 0x2

	jal	set_aaa_awb_pipeline_wrapper
	li	$4,2			# 0x2

	li	$5,64			# 0x40
	jal	appAWBALGLib_WBParamSet
	li	$4,8			# 0x8

	jal	set_g_ae_parameter
	move	$4,$0

	jal	exif_remove_and_add_wrapper
	move	$4,$0

	jal	get_cold_item_sensor_digital_effect
	nop

	sltu	$3,$2,2
	beq	$3,$0,$L8
	li	$5,64			# 0x40

	lui	$3,%hi(g_sensor_config_table_A)
	addiu	$3,$3,%lo(g_sensor_config_table_A)
	addu	$2,$2,$3
	lbu	$5,0($2)
$L8:
	li	$6,1			# 0x1
	jal	dispatch_IQ_function
	li	$4,30			# 0x1e

	jal	setSensor_configA
	li	$4,17			# 0x11

	jal	setDigitalEffect
	move	$4,$0

	li	$5,1			# 0x1
	jal	sp5kIqBlockEnable
	li	$4,14			# 0xe

	jal	setSensor_configB
	li	$4,17			# 0x11

	jal	setSensor_configA
	li	$4,19			# 0x13

	jal	setDigitalEffect
	move	$4,$0

	li	$5,1			# 0x1
	jal	sp5kIqBlockEnable
	li	$4,14			# 0xe

	jal	setSensor_configB
	li	$4,19			# 0x13

	li	$7,131072			# 0x20000
	li	$6,1			# 0x1
	move	$5,$0
	jal	dispatch_IQ_function
	li	$4,35			# 0x23

	lw	$31,20($sp)
	li	$7,14			# 0xe
	move	$6,$0
	move	$5,$0
	li	$4,35			# 0x23
	j	dispatch_IQ_function
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	cp_setSensorDigitalEffectPhoto
	.size	cp_setSensorDigitalEffectPhoto, .-cp_setSensorDigitalEffectPhoto
	.align	2
	.globl	cp_setSensorDigitalEffectVideo
	.set	nomips16
	.set	nomicromips
	.ent	cp_setSensorDigitalEffectVideo
	.type	cp_setSensorDigitalEffectVideo, @function
cp_setSensorDigitalEffectVideo:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_photo_mode_p)
	sb	$0,%lo(g_photo_mode_p)($2)
	lui	$2,%hi(g_night_mode_p)
	addiu	$sp,$sp,-24
	sb	$4,%lo(g_night_mode_p)($2)
	sw	$31,20($sp)
	jal	set_aaa_ae_pipeline_wrapper
	li	$4,2			# 0x2

	jal	set_aaa_awb_pipeline_wrapper
	li	$4,2			# 0x2

	li	$5,255			# 0xff
	jal	appAWBALGLib_WBParamSet
	li	$4,8			# 0x8

	jal	set_g_ae_parameter
	move	$4,$0

	jal	exif_remove_and_add_wrapper
	move	$4,$0

	jal	get_cold_item_sensor_digital_effect
	nop

	sltu	$3,$2,2
	beq	$3,$0,$L13
	li	$5,64			# 0x40

	lui	$3,%hi(g_sensor_config_table_A)
	addiu	$3,$3,%lo(g_sensor_config_table_A)
	addu	$2,$2,$3
	lbu	$5,0($2)
$L13:
	li	$6,1			# 0x1
	jal	dispatch_IQ_function
	li	$4,30			# 0x1e

	jal	setSensor_configA
	li	$4,33			# 0x21

	jal	setDigitalEffect
	move	$4,$0

	li	$5,1			# 0x1
	jal	sp5kIqBlockEnable
	li	$4,14			# 0xe

	jal	setSensor_configB
	li	$4,33			# 0x21

	li	$7,131072			# 0x20000
	li	$6,1			# 0x1
	move	$5,$0
	jal	dispatch_IQ_function
	li	$4,35			# 0x23

	lw	$31,20($sp)
	li	$7,14			# 0xe
	move	$6,$0
	move	$5,$0
	li	$4,35			# 0x23
	j	dispatch_IQ_function
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	cp_setSensorDigitalEffectVideo
	.size	cp_setSensorDigitalEffectVideo, .-cp_setSensorDigitalEffectVideo
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
