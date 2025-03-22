	.file	1 "battery-monitor.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	bm_off_photo_burst_hook
	.set	nomips16
	.set	nomicromips
	.ent	bm_off_photo_burst_hook
	.type	bm_off_photo_burst_hook, @function
bm_off_photo_burst_hook:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	IRLedOff
	nop

	lw	$31,20($sp)
	j	dslr_LEDOff
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	bm_off_photo_burst_hook
	.size	bm_off_photo_burst_hook, .-bm_off_photo_burst_hook
	.align	2
	.globl	bm_off_photo_burst
	.set	nomips16
	.set	nomicromips
	.ent	bm_off_photo_burst
	.type	bm_off_photo_burst, @function
bm_off_photo_burst:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	dslr_LEDOff
	nop

	.set	macro
	.set	reorder
	.end	bm_off_photo_burst
	.size	bm_off_photo_burst, .-bm_off_photo_burst
	.align	2
	.globl	bm_HceCommon_SetCaptureImage_hook
	.set	nomips16
	.set	nomicromips
	.ent	bm_HceCommon_SetCaptureImage_hook
	.type	bm_HceCommon_SetCaptureImage_hook, @function
bm_HceCommon_SetCaptureImage_hook:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	HceCommon_SetCaptureImag
	nop

	.set	macro
	.set	reorder
	.end	bm_HceCommon_SetCaptureImage_hook
	.size	bm_HceCommon_SetCaptureImage_hook, .-bm_HceCommon_SetCaptureImage_hook
	.align	2
	.globl	bm_get_video_flash_intensity_color_p
	.set	nomips16
	.set	nomicromips
	.ent	bm_get_video_flash_intensity_color_p
	.type	bm_get_video_flash_intensity_color_p, @function
bm_get_video_flash_intensity_color_p:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$17,24($sp)
	sw	$16,20($sp)
	sw	$31,28($sp)
	move	$16,$4
	jal	getCameraConfigStructPtr
	move	$17,$5

	lbu	$2,0($2)
	bne	$2,$0,$L6
	nop

	sw	$0,0($16)
$L7:
	lw	$31,28($sp)
	li	$2,1			# 0x1
	lw	$16,20($sp)
	sw	$2,0($17)
	lw	$17,24($sp)
	jr	$31
	addiu	$sp,$sp,32

$L6:
	jal	get_g_cold_item_led_power
	sw	$0,0($17)

	bne	$2,$0,$L11
	li	$2,2			# 0x2

	li	$2,1			# 0x1
$L10:
$L11:
	b	$L7
	sw	$2,0($16)

	.set	macro
	.set	reorder
	.end	bm_get_video_flash_intensity_color_p
	.size	bm_get_video_flash_intensity_color_p, .-bm_get_video_flash_intensity_color_p
	.align	2
	.globl	bm_get_photo_flash_intensity_color_p
	.set	nomips16
	.set	nomicromips
	.ent	bm_get_photo_flash_intensity_color_p
	.type	bm_get_photo_flash_intensity_color_p, @function
bm_get_photo_flash_intensity_color_p:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$17,24($sp)
	sw	$16,20($sp)
	sw	$31,28($sp)
	move	$16,$4
	jal	getCameraConfigStructPtr
	move	$17,$5

	lbu	$2,33($2)
	bne	$2,$0,$L13
	nop

	sw	$0,0($16)
$L14:
	lw	$31,28($sp)
	li	$2,1			# 0x1
	lw	$16,20($sp)
	sw	$2,0($17)
	lw	$17,24($sp)
	jr	$31
	addiu	$sp,$sp,32

$L13:
	jal	get_g_cold_item_led_power
	sw	$0,0($17)

	bne	$2,$0,$L18
	li	$2,2			# 0x2

	li	$2,1			# 0x1
$L17:
$L18:
	b	$L14
	sw	$2,0($16)

	.set	macro
	.set	reorder
	.end	bm_get_photo_flash_intensity_color_p
	.size	bm_get_photo_flash_intensity_color_p, .-bm_get_photo_flash_intensity_color_p
	.align	2
	.globl	bm_video_off_hook
	.set	nomips16
	.set	nomicromips
	.ent	bm_video_off_hook
	.type	bm_video_off_hook, @function
bm_video_off_hook:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	bm_off_photo_burst_hook
	nop

	.set	macro
	.set	reorder
	.end	bm_video_off_hook
	.size	bm_video_off_hook, .-bm_video_off_hook
	.align	2
	.globl	bm_off_video
	.set	nomips16
	.set	nomicromips
	.ent	bm_off_video
	.type	bm_off_video, @function
bm_off_video:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	dslr_LEDOff
	nop

	.set	macro
	.set	reorder
	.end	bm_off_video
	.size	bm_off_video, .-bm_off_video
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC4:
	.ascii	"WBWL Error::get_initial_battery_capacity -- unrecognized"
	.ascii	" battery type %d\012\000"
	.text
	.align	2
	.globl	bm_get_initial_battery_capacity
	.set	nomips16
	.set	nomicromips
	.ent	bm_get_initial_battery_capacity
	.type	bm_get_initial_battery_capacity, @function
bm_get_initial_battery_capacity:
	.frame	$sp,24,$31		# vars= 0, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	beq	$4,$0,$L23
	li	$2,37879808			# 0x2420000

	addiu	$sp,$sp,-24
	li	$2,1			# 0x1
	sw	$16,16($sp)
	sw	$31,20($sp)
	beq	$4,$2,$L24
	move	$16,$4

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC4)
	move	$5,$16
	jal	tty_printf
	addiu	$4,$4,%lo($LC4)

	jal	check_post_printf_state_set_sio_params
	nop

	li	$2,37879808			# 0x2420000
	addiu	$2,$2,18432
$L21:
	lw	$31,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,24

$L23:
	jr	$31
	addiu	$2,$2,18432

$L24:
	li	$2,28704768			# 0x1b60000
	b	$L21
	ori	$2,$2,0xc000

	.set	macro
	.set	reorder
	.end	bm_get_initial_battery_capacity
	.size	bm_get_initial_battery_capacity, .-bm_get_initial_battery_capacity
	.align	2
	.globl	bm_get_current_battery_level
	.set	nomips16
	.set	nomicromips
	.ent	bm_get_current_battery_level
	.type	bm_get_current_battery_level, @function
bm_get_current_battery_level:
	.frame	$sp,40,$31		# vars= 0, regs= 5/0, args= 16, gp= 0
	.mask	0x800f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$16,20($sp)
	lui	$16,%hi(setDigitalEffectswitchdataD_table)
	sw	$19,32($sp)
	addiu	$19,$16,%lo(setDigitalEffectswitchdataD_table)
	sw	$18,28($sp)
	move	$18,$4
	lh	$4,50($19)
	sw	$31,36($sp)
	jal	bm_get_initial_battery_capacity
	sw	$17,24($sp)

	move	$17,$2
	move	$4,$18
	lw	$16,%lo(setDigitalEffectswitchdataD_table)($16)
	jal	get_battery_percent_from_voltage
	lw	$19,4($19)

	beq	$17,$0,$L30
	move	$2,$0

	addu	$3,$16,$19
	li	$2,100			# 0x64
	subu	$3,$17,$3
	mult	$3,$2
	mflo	$3
	nop
	nop
	divu	$0,$3,$17
	nop
	teq	$17,$0,7
	mflo	$2
$L30:
	lw	$31,36($sp)
	lw	$19,32($sp)
	lw	$18,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,40

	.set	macro
	.set	reorder
	.end	bm_get_current_battery_level
	.size	bm_get_current_battery_level, .-bm_get_current_battery_level
	.align	2
	.globl	bm_bilinear_interpolate
	.set	nomips16
	.set	nomicromips
	.ent	bm_bilinear_interpolate
	.type	bm_bilinear_interpolate, @function
bm_bilinear_interpolate:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lw	$3,0($6)
	slt	$8,$4,$3
	bne	$8,$0,$L36
	lw	$10,16($sp)

	lw	$3,40($6)
	slt	$8,$4,$3
	bnel	$8,$0,$L36
	move	$3,$4

$L36:
	move	$4,$6
	move	$8,$0
	li	$13,10			# 0xa
$L40:
	lw	$9,0($4)
	slt	$9,$3,$9
	bne	$9,$0,$L38
	addiu	$12,$8,1

	lw	$9,4($4)
	slt	$9,$9,$3
	bnel	$9,$0,$L50
	move	$8,$12

	move	$2,$12
	lw	$4,0($7)
$L48:
	sltu	$9,$5,$4
	bne	$9,$0,$L51
	move	$9,$7

	lw	$4,16($7)
	sltu	$9,$5,$4
	bnel	$9,$0,$L41
	move	$4,$5

$L41:
	move	$9,$7
$L51:
	move	$5,$0
	li	$14,4			# 0x4
$L45:
	lw	$12,0($9)
	sltu	$12,$4,$12
	bne	$12,$0,$L43
	addiu	$13,$5,1

	lw	$12,4($9)
	sltu	$12,$12,$4
	bnel	$12,$0,$L52
	move	$5,$13

	move	$11,$13
	sll	$12,$8,2
$L49:
	sll	$9,$2,2
	addu	$8,$12,$8
	addu	$2,$9,$2
	sll	$13,$11,2
	sll	$2,$2,2
	sll	$8,$8,2
	addu	$8,$10,$8
	sll	$5,$5,2
	addu	$10,$10,$2
	addu	$9,$6,$9
	addu	$2,$7,$13
	addu	$6,$6,$12
	lw	$12,0($6)
	lw	$11,0($2)
	lw	$9,0($9)
	addu	$2,$8,$5
	addu	$7,$7,$5
	addu	$5,$10,$5
	lw	$2,0($2)
	lw	$5,0($5)
	subu	$6,$9,$3
	subu	$3,$3,$12
	mult	$3,$5
	mflo	$5
	addu	$8,$8,$13
	addu	$10,$10,$13
	lw	$7,0($7)
	mult	$6,$2
	mflo	$2
	addu	$2,$2,$5
	subu	$5,$11,$4
	mult	$2,$5
	mflo	$2
	lw	$5,0($8)
	subu	$4,$4,$7
	mult	$6,$5
	mflo	$6
	lw	$5,0($10)
	nop
	mult	$3,$5
	mflo	$3
	addu	$3,$6,$3
	nop
	mult	$3,$4
	mflo	$3
	subu	$4,$11,$7
	addu	$3,$2,$3
	subu	$2,$9,$12
	mult	$2,$4
	mflo	$2
	nop
	nop
	divu	$0,$3,$2
	nop
	teq	$2,$0,7
	mflo	$2
	jr	$31
	nop

$L38:
	move	$8,$12
$L50:
	bne	$12,$13,$L40
	addiu	$4,$4,4

	b	$L48
	lw	$4,0($7)

$L43:
	move	$5,$13
$L52:
	bne	$13,$14,$L45
	addiu	$9,$9,4

	b	$L49
	sll	$12,$8,2

	.set	macro
	.set	reorder
	.end	bm_bilinear_interpolate
	.size	bm_bilinear_interpolate, .-bm_bilinear_interpolate
	.section	.rodata.str1.4
	.align	2
$LC5:
	.ascii	"INFO::bm_accrue_cold_battery_energy: temperature = %d; p"
	.ascii	"ower = %d.%03d; adjustment factor = %d.%03d; cold_batter"
	.ascii	"y_energy = %d.%03d \012\000"
	.rdata
	.align	2
$LC0:
	.word	-58
	.word	-40
	.word	-22
	.word	-4
	.word	14
	.word	32
	.word	50
	.word	68
	.word	86
	.word	104
	.word	122
	.align	2
$LC1:
	.word	0
	.word	84
	.word	345
	.word	844
	.word	3379
	.align	2
$LC2:
	.word	0
	.word	12
	.word	280
	.word	1024
	.word	2304
	.word	0
	.word	8
	.word	104
	.word	313
	.word	1024
	.word	0
	.word	6
	.word	34
	.word	69
	.word	280
	.word	0
	.word	4
	.word	14
	.word	24
	.word	101
	.word	0
	.word	2
	.word	5
	.word	8
	.word	52
	.word	0
	.word	0
	.word	3
	.word	6
	.word	33
	.word	0
	.word	0
	.word	0
	.word	0
	.word	24
	.word	0
	.word	0
	.word	0
	.word	0
	.word	24
	.word	0
	.word	0
	.word	0
	.word	0
	.word	24
	.word	0
	.word	0
	.word	0
	.word	0
	.word	24
	.word	0
	.word	0
	.word	0
	.word	0
	.word	24
	.align	2
$LC3:
	.word	3648
	.word	3648
	.word	12757
	.word	129877
	.word	256000
	.word	2867
	.word	2867
	.word	5570
	.word	43121
	.word	256000
	.word	2867
	.word	2867
	.word	4949
	.word	15360
	.word	256000
	.word	1305
	.word	1305
	.word	2146
	.word	4949
	.word	81933
	.word	264
	.word	264
	.word	579
	.word	1854
	.word	15360
	.word	62
	.word	62
	.word	239
	.word	859
	.word	2997
	.word	44
	.word	44
	.word	134
	.word	301
	.word	1189
	.word	44
	.word	44
	.word	91
	.word	154
	.word	720
	.word	53
	.word	30
	.word	71
	.word	124
	.word	524
	.word	13
	.word	13
	.word	54
	.word	109
	.word	394
	.word	0
	.word	0
	.word	41
	.word	98
	.word	315
	.text
	.align	2
	.globl	bm_accrue_cold_battery_energy
	.set	nomips16
	.set	nomicromips
	.ent	bm_accrue_cold_battery_energy
	.type	bm_accrue_cold_battery_energy, @function
bm_accrue_cold_battery_energy:
	.frame	$sp,568,$31		# vars= 512, regs= 6/0, args= 32, gp= 0
	.mask	0x801f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-568
	sw	$18,552($sp)
	move	$18,$5
	lui	$5,%hi($LC0)
	sw	$17,548($sp)
	sw	$16,544($sp)
	addiu	$5,$5,%lo($LC0)
	move	$16,$4
	move	$17,$6
	addiu	$4,$sp,472
	li	$6,44			# 0x2c
	sw	$31,564($sp)
	sw	$20,560($sp)
	sw	$19,556($sp)
	jal	memcpy
	move	$19,$7

	lui	$5,%hi($LC1)
	li	$6,20			# 0x14
	addiu	$5,$5,%lo($LC1)
	jal	memcpy
	addiu	$4,$sp,516

	addiu	$20,$sp,252
	lui	$5,%hi($LC2)
	li	$6,220			# 0xdc
	addiu	$5,$5,%lo($LC2)
	jal	memcpy
	move	$4,$20

	lui	$5,%hi($LC3)
	addiu	$4,$sp,32
	li	$6,220			# 0xdc
	jal	memcpy
	addiu	$5,$5,%lo($LC3)

	bnel	$19,$0,$L57
	sw	$2,16($sp)

	sw	$20,16($sp)
$L57:
	addiu	$7,$sp,516
	addiu	$6,$sp,472
	move	$5,$17
	jal	bm_bilinear_interpolate
	move	$4,$18

	mult	$2,$16
	mflo	$4
	li	$6,1000			# 0x3e8
	andi	$3,$2,0xff
	andi	$7,$17,0xff
	sw	$2,536($sp)
	srl	$16,$4,8
	mult	$3,$6
	mflo	$3
	andi	$5,$16,0xff
	srl	$4,$4,16
	sw	$4,24($sp)
	lui	$4,%hi($LC5)
	addiu	$4,$4,%lo($LC5)
	mult	$5,$6
	mflo	$5
	srl	$3,$3,8
	sw	$3,20($sp)
	srl	$3,$2,8
	sw	$3,16($sp)
	mult	$7,$6
	mflo	$7
	srl	$5,$5,8
	sw	$5,28($sp)
	srl	$6,$17,8
	move	$5,$18
	jal	tty_printf
	srl	$7,$7,8

	lui	$3,%hi(setDigitalEffectswitchdataD_table)
	addiu	$3,$3,%lo(setDigitalEffectswitchdataD_table)
	lw	$4,4($3)
	lw	$31,564($sp)
	lw	$2,536($sp)
	addu	$4,$4,$16
	lw	$20,560($sp)
	lw	$19,556($sp)
	lw	$18,552($sp)
	lw	$17,548($sp)
	lw	$16,544($sp)
	sw	$4,4($3)
	jr	$31
	addiu	$sp,$sp,568

	.set	macro
	.set	reorder
	.end	bm_accrue_cold_battery_energy
	.size	bm_accrue_cold_battery_energy, .-bm_accrue_cold_battery_energy
	.section	.rodata.str1.4
	.align	2
$LC6:
	.ascii	"INFO::bm_increment_energy_consumed: increment = %d.%03d;"
	.ascii	" total = %d.%03d \012\000"
	.align	2
$LC7:
	.ascii	"Info::bm_increment_energy_consumed: consumed %u.%03d bey"
	.ascii	"ond battery capacity\012\000"
	.align	2
$LC8:
	.ascii	"Info::bm_increment_energy_consumed: no battery energy co"
	.ascii	"nsumed -- EXT BATT mode\012\000"
	.text
	.align	2
	.globl	bm_increment_energy_consumed
	.set	nomips16
	.set	nomicromips
	.ent	bm_increment_energy_consumed
	.type	bm_increment_energy_consumed, @function
bm_increment_energy_consumed:
	.frame	$sp,56,$31		# vars= 8, regs= 6/0, args= 24, gp= 0
	.mask	0x801f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-56
	sw	$19,44($sp)
	sw	$16,32($sp)
	sw	$31,52($sp)
	sw	$20,48($sp)
	sw	$18,40($sp)
	sw	$17,36($sp)
	move	$16,$4
	jal	get_power_supply_mode
	move	$19,$5

	bne	$2,$0,$L59
	nop

	lui	$17,%hi(setDigitalEffectswitchdataD_table)
	addiu	$18,$17,%lo(setDigitalEffectswitchdataD_table)
	jal	get_cold_item_temperature_unit_celsius_p
	lh	$20,50($18)

	bne	$2,$0,$L60
	nop

	jal	get_temperatureForC
	nop

	move	$5,$2
$L61:
	move	$7,$20
	move	$6,$19
	jal	bm_accrue_cold_battery_energy
	move	$4,$16

	lw	$7,%lo(setDigitalEffectswitchdataD_table)($17)
	li	$3,1000			# 0x3e8
	andi	$6,$16,0xff
	addu	$7,$16,$7
	andi	$2,$7,0xff
	mult	$2,$3
	mflo	$2
	lui	$4,%hi($LC6)
	srl	$5,$16,8
	sw	$7,%lo(setDigitalEffectswitchdataD_table)($17)
	addiu	$4,$4,%lo($LC6)
	srl	$7,$7,8
	sw	$5,24($sp)
	mult	$6,$3
	mflo	$6
	srl	$2,$2,8
	sw	$2,16($sp)
	srl	$6,$6,8
	jal	tty_printf
	sw	$6,28($sp)

	jal	bm_get_initial_battery_capacity
	lh	$4,50($18)

	lw	$3,%lo(setDigitalEffectswitchdataD_table)($17)
	sltu	$3,$2,$3
	beq	$3,$0,$L58
	lw	$31,52($sp)

	jal	set_pre_printf_state
	sw	$2,%lo(setDigitalEffectswitchdataD_table)($17)

	lw	$6,28($sp)
	lw	$5,24($sp)
	lui	$4,%hi($LC7)
	jal	tty_printf
	addiu	$4,$4,%lo($LC7)

	lw	$31,52($sp)
$L65:
	lw	$20,48($sp)
	lw	$19,44($sp)
	lw	$18,40($sp)
	lw	$17,36($sp)
	lw	$16,32($sp)
	j	check_post_printf_state_set_sio_params
	addiu	$sp,$sp,56

$L60:
	jal	get_temperatureForC
	nop

	sll	$3,$2,3
	addu	$2,$3,$2
	li	$5,5			# 0x5
	div	$0,$2,$5
	nop
	teq	$5,$0,7
	mflo	$2
	b	$L61
	addiu	$5,$2,32

$L59:
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC8)
	jal	tty_printf
	addiu	$4,$4,%lo($LC8)

	b	$L65
	lw	$31,52($sp)

$L58:
	lw	$20,48($sp)
	lw	$19,44($sp)
	lw	$18,40($sp)
	lw	$17,36($sp)
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,56

	.set	macro
	.set	reorder
	.end	bm_increment_energy_consumed
	.size	bm_increment_energy_consumed, .-bm_increment_energy_consumed
	.section	.rodata.str1.4
	.align	2
$LC9:
	.ascii	"Info::bm_increment_photos: no photos counted -- EXT BATT"
	.ascii	" mode\012\000"
	.text
	.align	2
	.globl	bm_increment_photos
	.set	nomips16
	.set	nomicromips
	.ent	bm_increment_photos
	.type	bm_increment_photos, @function
bm_increment_photos:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$17,24($sp)
	sw	$16,20($sp)
	sw	$31,28($sp)
	move	$16,$4
	jal	get_power_supply_mode
	move	$17,$5

	bne	$2,$0,$L67
	lui	$2,%hi(setDigitalEffectswitchdataD_table)

	beq	$17,$0,$L68
	addiu	$2,$2,%lo(setDigitalEffectswitchdataD_table)

	li	$3,1			# 0x1
	beql	$17,$3,$L69
	lhu	$3,10($2)

	lhu	$3,12($2)
	lhu	$4,24($2)
	addu	$3,$16,$3
	addu	$16,$16,$4
	sh	$3,12($2)
	b	$L66
	sh	$16,24($2)

$L68:
	lhu	$3,8($2)
	lhu	$4,20($2)
	addu	$3,$16,$3
	addu	$16,$16,$4
	sh	$3,8($2)
	sh	$16,20($2)
$L66:
	lw	$31,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,32

$L69:
	lhu	$4,22($2)
	addu	$3,$16,$3
	addu	$16,$16,$4
	sh	$3,10($2)
	b	$L66
	sh	$16,22($2)

$L67:
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC9)
	jal	tty_printf
	addiu	$4,$4,%lo($LC9)

	lw	$31,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	check_post_printf_state_set_sio_params
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	bm_increment_photos
	.size	bm_increment_photos, .-bm_increment_photos
	.section	.rodata.str1.4
	.align	2
$LC10:
	.ascii	"Info::bm_on_photo_burst: burst_size: %d; energy_consumed"
	.ascii	" = %u.%03d; pv this uptime = %d; pv total = %d\012\000"
	.align	2
$LC11:
	.ascii	"Info::bm_on_photo_burst:flash_intensity: %d; color_p: %d"
	.ascii	"; energy: %u\012\000"
	.text
	.align	2
	.globl	bm_on_photo_burst
	.set	nomips16
	.set	nomicromips
	.ent	bm_on_photo_burst
	.type	bm_on_photo_burst, @function
bm_on_photo_burst:
	.frame	$sp,48,$31		# vars= 8, regs= 3/0, args= 24, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-48
	addiu	$5,$sp,24
	sw	$16,36($sp)
	move	$16,$4
	addiu	$4,$sp,28
	sw	$31,44($sp)
	jal	bm_get_photo_flash_intensity_color_p
	sw	$17,40($sp)

	beql	$16,$0,$L75
	li	$16,1			# 0x1

$L75:
	lw	$4,24($sp)
	li	$3,1			# 0x1
	bne	$4,$3,$L76
	lw	$2,28($sp)

	beq	$2,$0,$L77
	li	$17,128			# 0x80

	bne	$2,$4,$L77
	li	$17,640			# 0x280

	li	$17,384			# 0x180
$L77:
	mult	$17,$16
	mflo	$4
	jal	bm_increment_energy_consumed
	move	$5,$17

	lw	$5,28($sp)
	jal	bm_increment_photos
	andi	$4,$16,0xffff

	jal	dslr_LEDOn
	nop

	jal	set_pre_printf_state
	nop

	lui	$2,%hi(setDigitalEffectswitchdataD_table)
	lw	$6,%lo(setDigitalEffectswitchdataD_table)($2)
	li	$3,1000			# 0x3e8
	addiu	$2,$2,%lo(setDigitalEffectswitchdataD_table)
	andi	$7,$6,0xff
	lhu	$4,22($2)
	mult	$7,$3
	mflo	$7
	lhu	$3,20($2)
	move	$5,$16
	srl	$6,$6,8
	addu	$3,$3,$4
	lhu	$4,24($2)
	addu	$3,$3,$4
	sw	$3,20($sp)
	lhu	$4,10($2)
	lhu	$3,8($2)
	lhu	$2,12($2)
	srl	$7,$7,8
	addu	$3,$3,$4
	addu	$2,$3,$2
	lui	$4,%hi($LC10)
	sw	$2,16($sp)
	jal	tty_printf
	addiu	$4,$4,%lo($LC10)

	jal	check_post_printf_state_set_sio_params
	nop

	jal	set_pre_printf_state
	nop

	lw	$6,24($sp)
	lw	$5,28($sp)
	lui	$4,%hi($LC11)
	move	$7,$17
	jal	tty_printf
	addiu	$4,$4,%lo($LC11)

	jal	check_post_printf_state_set_sio_params
	nop

	lw	$31,44($sp)
	lw	$17,40($sp)
	lw	$16,36($sp)
	jr	$31
	addiu	$sp,$sp,48

$L76:
	beq	$2,$0,$L77
	li	$17,76			# 0x4c

	bne	$2,$3,$L77
	li	$17,588			# 0x24c

	b	$L77
	li	$17,332			# 0x14c

	.set	macro
	.set	reorder
	.end	bm_on_photo_burst
	.size	bm_on_photo_burst, .-bm_on_photo_burst
	.align	2
	.globl	bm_RapidFirePhotos_printf_hook
	.set	nomips16
	.set	nomicromips
	.ent	bm_RapidFirePhotos_printf_hook
	.type	bm_RapidFirePhotos_printf_hook, @function
bm_RapidFirePhotos_printf_hook:
	.frame	$sp,32,$31		# vars= 0, regs= 2/0, args= 24, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$16,24($sp)
	lw	$16,48($sp)
	sw	$31,28($sp)
	jal	tty_printf
	sw	$16,16($sp)

	lw	$31,28($sp)
	move	$4,$16
	lw	$16,24($sp)
	j	bm_on_photo_burst
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	bm_RapidFirePhotos_printf_hook
	.size	bm_RapidFirePhotos_printf_hook, .-bm_RapidFirePhotos_printf_hook
	.section	.rodata.str1.4
	.align	2
$LC12:
	.ascii	"Info::bm_on_photo: energy_consumed = %u.%03d; photos thi"
	.ascii	"s uptime = %d; photos total = %d\012\000"
	.align	2
$LC13:
	.ascii	"Info::bm_on_photo: flash_intensity: %d; color_p: %d; ene"
	.ascii	"rgy: %u\012\000"
	.text
	.align	2
	.globl	bm_on_photo
	.set	nomips16
	.set	nomicromips
	.ent	bm_on_photo
	.type	bm_on_photo, @function
bm_on_photo:
	.frame	$sp,40,$31		# vars= 8, regs= 2/0, args= 24, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	addiu	$4,$sp,28
	addiu	$5,$sp,24
	sw	$31,36($sp)
	jal	bm_get_photo_flash_intensity_color_p
	sw	$16,32($sp)

	lw	$4,24($sp)
	li	$3,1			# 0x1
	bne	$4,$3,$L86
	lw	$2,28($sp)

	beq	$2,$0,$L87
	li	$16,128			# 0x80

	bne	$2,$4,$L87
	li	$16,640			# 0x280

	li	$16,384			# 0x180
$L87:
	move	$5,$16
	jal	bm_increment_energy_consumed
	move	$4,$16

	lw	$5,28($sp)
	jal	bm_increment_photos
	li	$4,1			# 0x1

	jal	set_pre_printf_state
	nop

	lui	$2,%hi(setDigitalEffectswitchdataD_table)
	lw	$5,%lo(setDigitalEffectswitchdataD_table)($2)
	li	$3,1000			# 0x3e8
	addiu	$2,$2,%lo(setDigitalEffectswitchdataD_table)
	andi	$6,$5,0xff
	mult	$6,$3
	mflo	$6
	lhu	$7,10($2)
	lhu	$4,8($2)
	lhu	$8,22($2)
	lhu	$3,20($2)
	addu	$4,$4,$7
	lhu	$7,12($2)
	lhu	$2,24($2)
	addu	$3,$3,$8
	addu	$7,$4,$7
	addu	$2,$3,$2
	lui	$4,%hi($LC12)
	sw	$2,16($sp)
	srl	$6,$6,8
	srl	$5,$5,8
	jal	tty_printf
	addiu	$4,$4,%lo($LC12)

	jal	check_post_printf_state_set_sio_params
	nop

	jal	set_pre_printf_state
	nop

	lw	$6,24($sp)
	lw	$5,28($sp)
	lui	$4,%hi($LC13)
	move	$7,$16
	jal	tty_printf
	addiu	$4,$4,%lo($LC13)

	jal	check_post_printf_state_set_sio_params
	nop

	lw	$31,36($sp)
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,40

$L86:
	beq	$2,$0,$L87
	li	$16,76			# 0x4c

	bne	$2,$3,$L87
	li	$16,588			# 0x24c

	b	$L87
	li	$16,332			# 0x14c

	.set	macro
	.set	reorder
	.end	bm_on_photo
	.size	bm_on_photo, .-bm_on_photo
	.align	2
	.globl	bm_increment_video
	.set	nomips16
	.set	nomicromips
	.ent	bm_increment_video
	.type	bm_increment_video, @function
bm_increment_video:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$17,24($sp)
	sw	$16,20($sp)
	sw	$31,28($sp)
	move	$16,$4
	jal	get_power_supply_mode
	move	$17,$5

	bne	$2,$0,$L100
	lw	$31,28($sp)

	lui	$2,%hi(setDigitalEffectswitchdataD_table)
	beq	$17,$0,$L95
	addiu	$2,$2,%lo(setDigitalEffectswitchdataD_table)

	li	$3,1			# 0x1
	beql	$17,$3,$L96
	lhu	$3,16($2)

	lhu	$3,18($2)
	lhu	$4,30($2)
	addu	$3,$16,$3
	addu	$16,$16,$4
	sh	$3,18($2)
	b	$L93
	sh	$16,30($2)

$L95:
	lhu	$3,14($2)
	lhu	$4,26($2)
	addu	$3,$16,$3
	addu	$16,$16,$4
	sh	$3,14($2)
	sh	$16,26($2)
$L93:
	lw	$31,28($sp)
$L100:
	lw	$17,24($sp)
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,32

$L96:
	lhu	$4,28($2)
	addu	$3,$16,$3
	addu	$16,$16,$4
	sh	$3,16($2)
	b	$L93
	sh	$16,28($2)

	.set	macro
	.set	reorder
	.end	bm_increment_video
	.size	bm_increment_video, .-bm_increment_video
	.section	.rodata.str1.4
	.align	2
$LC14:
	.ascii	"Info::bm_on_video: duration: %d; flash_intensity: %d; co"
	.ascii	"lor_p: %d; energy: %u; video_this_uptime %d; total video"
	.ascii	": %d\012\000"
	.text
	.align	2
	.globl	bm_on_video
	.set	nomips16
	.set	nomicromips
	.ent	bm_on_video
	.type	bm_on_video, @function
bm_on_video:
	.frame	$sp,56,$31		# vars= 8, regs= 3/0, args= 32, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-56
	sw	$31,52($sp)
	sw	$16,44($sp)
	jal	get_current_video_duration_in_seconds
	sw	$17,48($sp)

	addiu	$4,$sp,36
	addiu	$5,$sp,32
	jal	bm_get_video_flash_intensity_color_p
	move	$16,$2

	lw	$4,32($sp)
	li	$3,1			# 0x1
	bne	$4,$3,$L102
	lw	$2,36($sp)

	beq	$2,$0,$L103
	li	$5,591			# 0x24f

	bne	$2,$4,$L103
	li	$5,1792			# 0x700

	li	$5,1249			# 0x4e1
$L103:
	mult	$16,$5
	mflo	$17
	jal	bm_increment_energy_consumed
	move	$4,$17

	lw	$5,36($sp)
	jal	bm_increment_video
	andi	$4,$16,0xffff

	jal	dslr_LEDOn
	nop

	jal	set_pre_printf_state
	nop

	lui	$3,%hi(setDigitalEffectswitchdataD_table)
	addiu	$3,$3,%lo(setDigitalEffectswitchdataD_table)
	lhu	$4,28($3)
	lhu	$2,26($3)
	lw	$7,32($sp)
	lw	$6,36($sp)
	addu	$2,$2,$4
	lhu	$4,30($3)
	move	$5,$16
	addu	$2,$2,$4
	sw	$2,24($sp)
	lhu	$4,16($3)
	lhu	$2,14($3)
	lhu	$3,18($3)
	sw	$17,16($sp)
	addu	$2,$2,$4
	addu	$2,$2,$3
	lui	$4,%hi($LC14)
	sw	$2,20($sp)
	jal	tty_printf
	addiu	$4,$4,%lo($LC14)

	jal	check_post_printf_state_set_sio_params
	nop

	lw	$31,52($sp)
	lw	$17,48($sp)
	lw	$16,44($sp)
	jr	$31
	addiu	$sp,$sp,56

$L102:
	beq	$2,$0,$L103
	li	$5,384			# 0x180

	bne	$2,$3,$L103
	li	$5,1536			# 0x600

	b	$L103
	li	$5,1152			# 0x480

	.set	macro
	.set	reorder
	.end	bm_on_video
	.size	bm_on_video, .-bm_on_video
	.align	2
	.globl	bm_video_log_printf_hook
	.set	nomips16
	.set	nomicromips
	.ent	bm_video_log_printf_hook
	.type	bm_video_log_printf_hook, @function
bm_video_log_printf_hook:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	log_printf
	nop

	lw	$31,20($sp)
	j	bm_on_video
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	bm_video_log_printf_hook
	.size	bm_video_log_printf_hook, .-bm_video_log_printf_hook
	.section	.rodata.str1.4
	.align	2
$LC15:
	.ascii	"Info::bm_get_ui_energy: elapsed time = %d seconds; accru"
	.ascii	"ing %u.%03d J\012\000"
	.text
	.align	2
	.globl	bm_get_ui_energy
	.set	nomips16
	.set	nomicromips
	.ent	bm_get_ui_energy
	.type	bm_get_ui_energy, @function
bm_get_ui_energy:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$16,20($sp)
	li	$16,460			# 0x1cc
	mult	$4,$16
	mflo	$16
	sw	$31,28($sp)
	sw	$17,24($sp)
	jal	set_pre_printf_state
	move	$17,$4

	li	$2,1000			# 0x3e8
	lui	$4,%hi($LC15)
	move	$5,$17
	addiu	$4,$4,%lo($LC15)
	andi	$7,$16,0xff
	mult	$7,$2
	mflo	$7
	srl	$6,$16,8
	jal	tty_printf
	srl	$7,$7,8

	jal	check_post_printf_state_set_sio_params
	nop

	lw	$31,28($sp)
	lw	$17,24($sp)
	move	$2,$16
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	bm_get_ui_energy
	.size	bm_get_ui_energy, .-bm_get_ui_energy
	.section	.rodata.str1.4
	.align	2
$LC16:
	.ascii	"Warning::bm_get_delta_short_time: result_delta_seconds w"
	.ascii	"as negative!\012\000"
	.text
	.align	2
	.globl	bm_get_delta_short_time
	.set	nomips16
	.set	nomicromips
	.ent	bm_get_delta_short_time
	.type	bm_get_delta_short_time, @function
bm_get_delta_short_time:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lh	$2,0($4)
	lh	$3,0($5)
	lh	$6,2($5)
	subu	$2,$2,$3
	li	$3,31522816			# 0x1e10000
	ori	$3,$3,0x853e
	mult	$2,$3
	mflo	$3
	lh	$2,2($4)
	subu	$2,$2,$6
	li	$6,2621440			# 0x280000
	addiu	$6,$6,8303
	mult	$2,$6
	mflo	$2
	lh	$6,4($5)
	addu	$2,$2,$3
	lh	$3,4($4)
	subu	$3,$3,$6
	li	$6,65536			# 0x10000
	addiu	$6,$6,20864
	mult	$3,$6
	mflo	$3
	lh	$6,6($5)
	addu	$2,$3,$2
	lh	$3,6($4)
	subu	$3,$3,$6
	li	$6,3600			# 0xe10
	mult	$3,$6
	mflo	$3
	lh	$6,8($5)
	addu	$3,$3,$2
	lh	$2,8($4)
	subu	$6,$2,$6
	sll	$2,$6,4
	subu	$2,$2,$6
	sll	$2,$2,2
	addu	$3,$2,$3
	lh	$2,10($4)
	lh	$4,10($5)
	subu	$2,$2,$4
	addu	$2,$2,$3
	bgez	$2,$L119
	nop

	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC16)
	jal	tty_printf
	addiu	$4,$4,%lo($LC16)

	jal	check_post_printf_state_set_sio_params
	nop

	lw	$31,20($sp)
	move	$2,$0
	jr	$31
	addiu	$sp,$sp,24

$L119:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	bm_get_delta_short_time
	.size	bm_get_delta_short_time, .-bm_get_delta_short_time
	.align	2
	.globl	bm_short_to_byte_rtc_time
	.set	nomips16
	.set	nomicromips
	.ent	bm_short_to_byte_rtc_time
	.type	bm_short_to_byte_rtc_time, @function
bm_short_to_byte_rtc_time:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lbu	$2,0($5)
	addiu	$2,$2,48
	sb	$2,0($4)
	lhu	$2,2($5)
	sb	$2,1($4)
	lhu	$2,4($5)
	sb	$2,2($4)
	lhu	$2,6($5)
	sb	$2,3($4)
	lhu	$2,8($5)
	sb	$2,4($4)
	lhu	$2,10($5)
	jr	$31
	sb	$2,5($4)

	.set	macro
	.set	reorder
	.end	bm_short_to_byte_rtc_time
	.size	bm_short_to_byte_rtc_time, .-bm_short_to_byte_rtc_time
	.align	2
	.globl	bm_get_byte_rtc_time
	.set	nomips16
	.set	nomicromips
	.ent	bm_get_byte_rtc_time
	.type	bm_get_byte_rtc_time, @function
bm_get_byte_rtc_time:
	.frame	$sp,40,$31		# vars= 16, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$16,32($sp)
	move	$16,$4
	sw	$31,36($sp)
	jal	get_short_rtc_time
	addiu	$4,$sp,16

	addiu	$5,$sp,16
	jal	bm_short_to_byte_rtc_time
	move	$4,$16

	lw	$31,36($sp)
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,40

	.set	macro
	.set	reorder
	.end	bm_get_byte_rtc_time
	.size	bm_get_byte_rtc_time, .-bm_get_byte_rtc_time
	.align	2
	.globl	bm_hal_set_rtc_hook
	.set	nomips16
	.set	nomicromips
	.ent	bm_hal_set_rtc_hook
	.type	bm_hal_set_rtc_hook, @function
bm_hal_set_rtc_hook:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	hal_set_rtc
	nop

	lw	$31,20($sp)
	lui	$4,%hi(setDigitalEffectswitchdataD_table+38)
	addiu	$4,$4,%lo(setDigitalEffectswitchdataD_table+38)
	j	bm_get_byte_rtc_time
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	bm_hal_set_rtc_hook
	.size	bm_hal_set_rtc_hook, .-bm_hal_set_rtc_hook
	.align	2
	.globl	bm_get_delta_byte_time
	.set	nomips16
	.set	nomicromips
	.ent	bm_get_delta_byte_time
	.type	bm_get_delta_byte_time, @function
bm_get_delta_byte_time:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lbu	$2,0($4)
	lbu	$3,0($5)
	lbu	$6,1($5)
	subu	$2,$2,$3
	li	$3,31522816			# 0x1e10000
	ori	$3,$3,0x853e
	mult	$2,$3
	mflo	$3
	lbu	$2,1($4)
	subu	$2,$2,$6
	li	$6,2621440			# 0x280000
	addiu	$6,$6,8303
	mult	$2,$6
	mflo	$2
	lbu	$6,2($5)
	addu	$2,$2,$3
	lbu	$3,2($4)
	subu	$3,$3,$6
	li	$6,65536			# 0x10000
	addiu	$6,$6,20864
	mult	$3,$6
	mflo	$3
	lbu	$6,3($5)
	addu	$2,$3,$2
	lbu	$3,3($4)
	subu	$3,$3,$6
	li	$6,3600			# 0xe10
	mult	$3,$6
	mflo	$3
	lbu	$6,4($5)
	addu	$3,$3,$2
	lbu	$2,4($4)
	subu	$6,$2,$6
	sll	$2,$6,4
	subu	$2,$2,$6
	sll	$2,$2,2
	addu	$3,$2,$3
	lbu	$2,5($4)
	lbu	$4,5($5)
	subu	$2,$2,$4
	addu	$2,$2,$3
	bgez	$2,$L131
	nop

	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC16)
	jal	tty_printf
	addiu	$4,$4,%lo($LC16)

	jal	check_post_printf_state_set_sio_params
	nop

	lw	$31,20($sp)
	move	$2,$0
	jr	$31
	addiu	$sp,$sp,24

$L131:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	bm_get_delta_byte_time
	.size	bm_get_delta_byte_time, .-bm_get_delta_byte_time
	.align	2
	.globl	bm_seconds_to_hms
	.set	nomips16
	.set	nomicromips
	.ent	bm_seconds_to_hms
	.type	bm_seconds_to_hms, @function
bm_seconds_to_hms:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	li	$2,60			# 0x3c
	divu	$0,$4,$2
	nop
	teq	$2,$0,7
	mfhi	$3
	sw	$3,0($7)
	mflo	$3
	nop
	nop
	divu	$0,$3,$2
	nop
	teq	$2,$0,7
	mfhi	$3
	sw	$3,0($6)
	li	$3,3600			# 0xe10
	divu	$0,$4,$3
	nop
	teq	$3,$0,7
	mflo	$4
	nop
	nop
	divu	$0,$4,$2
	nop
	teq	$2,$0,7
	mfhi	$4
	jr	$31
	sw	$4,0($5)

	.set	macro
	.set	reorder
	.end	bm_seconds_to_hms
	.size	bm_seconds_to_hms, .-bm_seconds_to_hms
	.section	.rodata.str1.4
	.align	2
$LC17:
	.ascii	"Lithium \000"
	.align	2
$LC18:
	.ascii	"Alkaline\000"
	.align	2
$LC19:
	.ascii	"WBWL Trail Camera Battery Report\012\012\000"
	.align	2
$LC20:
	.ascii	"Current Battery Voltage: %d.%02d Volts\012\000"
	.align	2
$LC21:
	.ascii	"Install Date/Time: %02d/%02d/%04d %02d:%02d:%02d\012\000"
	.align	2
$LC22:
	.ascii	"Removal Date/Time: %02d/%02d/%04d %02d:%02d:%02d\012\012"
	.ascii	"\000"
	.align	2
$LC23:
	.ascii	"Battery Type: %s\012\012\000"
	.align	2
$LC24:
	.ascii	"Total Init Batt Energy: %6d.%03d Joules\012\000"
	.align	2
$LC25:
	.ascii	"       Energy Consumed: %6d.%03d Joules\012\000"
	.align	2
$LC26:
	.ascii	"   Cold Battery Energy: %6d.%03d Joules\012\000"
	.align	2
$LC27:
	.ascii	"      Remaining Energy: %6d.%03d Joules\012\000"
	.align	2
$LC28:
	.ascii	"    Fraction Available: %d percent\012\012\000"
	.align	2
$LC29:
	.ascii	"Total Photos Taken    : %d \012\000"
	.align	2
$LC30:
	.ascii	"   - No Flash         : %d \012\000"
	.align	2
$LC31:
	.ascii	"   - LowFlash         : %d \012\000"
	.align	2
$LC32:
	.ascii	"   - HiFlash          : %d \012\012\000"
	.align	2
$LC33:
	.ascii	"Total Video Taken     : %02d:%02d:%02d \012\000"
	.align	2
$LC34:
	.ascii	"   - No Flash         : %02d:%02d:%02d \012\000"
	.align	2
$LC35:
	.ascii	"   - LowFlash         : %02d:%02d:%02d \012\000"
	.align	2
$LC36:
	.ascii	"   - HiFlash          : %02d:%02d:%02d \012\000"
	.align	2
$LC37:
	.ascii	"Error::bm_print_summary_file -- write failure 14\012\000"
	.text
	.align	2
	.globl	bm_fprint_battery_telemetry
	.set	nomips16
	.set	nomicromips
	.ent	bm_fprint_battery_telemetry
	.type	bm_fprint_battery_telemetry, @function
bm_fprint_battery_telemetry:
	.frame	$sp,344,$31		# vars= 280, regs= 7/0, args= 32, gp= 0
	.mask	0x803f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-344
	lui	$5,%hi($LC19)
	addiu	$5,$5,%lo($LC19)
	sw	$16,316($sp)
	move	$16,$4
	addiu	$4,$sp,32
	sw	$17,320($sp)
	sw	$31,340($sp)
	sw	$21,336($sp)
	sw	$20,332($sp)
	sw	$19,328($sp)
	jal	local_sprintf
	sw	$18,324($sp)

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$17,$2

	bne	$17,$2,$L134
	nop

	jal	get_battery_voltage_x100
	nop

	li	$6,100			# 0x64
	divu	$0,$2,$6
	nop
	teq	$6,$0,7
	lui	$5,%hi($LC20)
	addiu	$5,$5,%lo($LC20)
	addiu	$4,$sp,32
	mflo	$6
	mfhi	$7
	jal	local_sprintf
	andi	$6,$6,0xffff

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$17,$2

	bne	$17,$2,$L134
	lui	$19,%hi(setDigitalEffectswitchdataD_table)

	addiu	$17,$19,%lo(setDigitalEffectswitchdataD_table)
	lbu	$2,37($17)
	lui	$5,%hi($LC21)
	addiu	$5,$5,%lo($LC21)
	sw	$2,28($sp)
	lbu	$2,36($17)
	addiu	$4,$sp,32
	sw	$2,24($sp)
	lbu	$2,35($17)
	sw	$2,20($sp)
	lbu	$2,32($17)
	addiu	$2,$2,2000
	sw	$2,16($sp)
	lbu	$6,33($17)
	jal	local_sprintf
	lbu	$7,34($17)

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	nop

	jal	bm_get_byte_rtc_time
	addiu	$4,$sp,288

	lbu	$2,293($sp)
	lbu	$6,289($sp)
	lbu	$7,290($sp)
	sw	$2,28($sp)
	lbu	$2,292($sp)
	lui	$5,%hi($LC22)
	addiu	$5,$5,%lo($LC22)
	sw	$2,24($sp)
	lbu	$2,291($sp)
	addiu	$4,$sp,32
	sw	$2,20($sp)
	lbu	$2,288($sp)
	addiu	$2,$2,2000
	jal	local_sprintf
	sw	$2,16($sp)

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	nop

	lh	$2,50($17)
	beq	$2,$0,$L138
	lui	$6,%hi($LC17)

	lui	$6,%hi($LC18)
	addiu	$6,$6,%lo($LC18)
$L135:
	lui	$5,%hi($LC23)
	addiu	$5,$5,%lo($LC23)
	jal	local_sprintf
	addiu	$4,$sp,32

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	nop

	lh	$4,50($17)
	jal	bm_get_initial_battery_capacity
	li	$21,1000			# 0x3e8

	andi	$7,$2,0xff
	mult	$7,$21
	mflo	$7
	lui	$5,%hi($LC24)
	srl	$6,$2,8
	addiu	$5,$5,%lo($LC24)
	addiu	$4,$sp,32
	move	$18,$2
	jal	local_sprintf
	srl	$7,$7,8

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$20,$2

	bne	$20,$2,$L134
	lw	$6,%lo(setDigitalEffectswitchdataD_table)($19)

	lui	$5,%hi($LC25)
	addiu	$5,$5,%lo($LC25)
	andi	$7,$6,0xff
	mult	$7,$21
	mflo	$7
	srl	$6,$6,8
	addiu	$4,$sp,32
	jal	local_sprintf
	srl	$7,$7,8

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$20,$2

	bne	$20,$2,$L134
	lui	$5,%hi($LC26)

	lw	$6,4($17)
	addiu	$5,$5,%lo($LC26)
	andi	$7,$6,0xff
	mult	$7,$21
	mflo	$7
	srl	$6,$6,8
	addiu	$4,$sp,32
	jal	local_sprintf
	srl	$7,$7,8

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$20,$2

	bne	$20,$2,$L134
	lw	$2,%lo(setDigitalEffectswitchdataD_table)($19)

	lw	$3,4($17)
	addu	$2,$2,$3
	sltu	$3,$18,$2
	bne	$3,$0,$L136
	move	$19,$0

	subu	$19,$18,$2
$L136:
	li	$2,1000			# 0x3e8
	andi	$7,$19,0xff
	mult	$7,$2
	mflo	$7
	lui	$5,%hi($LC27)
	srl	$6,$19,8
	addiu	$5,$5,%lo($LC27)
	addiu	$4,$sp,32
	jal	local_sprintf
	srl	$7,$7,8

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$20,$2

	bne	$20,$2,$L134
	li	$6,100			# 0x64

	mult	$19,$6
	mflo	$6
	lui	$5,%hi($LC28)
	addiu	$5,$5,%lo($LC28)
	divu	$0,$6,$18
	nop
	teq	$18,$0,7
	mflo	$6
	jal	local_sprintf
	addiu	$4,$sp,32

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	lui	$5,%hi($LC29)

	lhu	$6,22($17)
	lhu	$2,20($17)
	addiu	$5,$5,%lo($LC29)
	addu	$2,$2,$6
	lhu	$6,24($17)
	addiu	$4,$sp,32
	jal	local_sprintf
	addu	$6,$2,$6

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	lui	$5,%hi($LC30)

	lhu	$6,20($17)
	addiu	$5,$5,%lo($LC30)
	jal	local_sprintf
	addiu	$4,$sp,32

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	lui	$5,%hi($LC31)

	lhu	$6,22($17)
	addiu	$5,$5,%lo($LC31)
	jal	local_sprintf
	addiu	$4,$sp,32

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	lui	$5,%hi($LC32)

	lhu	$6,24($17)
	addiu	$5,$5,%lo($LC32)
	jal	local_sprintf
	addiu	$4,$sp,32

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	addiu	$7,$sp,296

	lhu	$4,28($17)
	lhu	$2,26($17)
	addiu	$6,$sp,300
	addu	$2,$2,$4
	lhu	$4,30($17)
	addiu	$5,$sp,304
	jal	bm_seconds_to_hms
	addu	$4,$2,$4

	lw	$2,296($sp)
	lw	$6,304($sp)
	lw	$7,300($sp)
	lui	$5,%hi($LC33)
	addiu	$5,$5,%lo($LC33)
	addiu	$4,$sp,32
	jal	local_sprintf
	sw	$2,16($sp)

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	addiu	$7,$sp,296

	lhu	$4,26($17)
	addiu	$6,$sp,300
	jal	bm_seconds_to_hms
	addiu	$5,$sp,304

	lw	$2,296($sp)
	lw	$6,304($sp)
	lw	$7,300($sp)
	lui	$5,%hi($LC34)
	addiu	$5,$5,%lo($LC34)
	addiu	$4,$sp,32
	jal	local_sprintf
	sw	$2,16($sp)

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	addiu	$7,$sp,296

	lhu	$4,28($17)
	addiu	$6,$sp,300
	jal	bm_seconds_to_hms
	addiu	$5,$sp,304

	lw	$2,296($sp)
	lw	$6,304($sp)
	lw	$7,300($sp)
	lui	$5,%hi($LC35)
	addiu	$5,$5,%lo($LC35)
	addiu	$4,$sp,32
	jal	local_sprintf
	sw	$2,16($sp)

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$18,$2

	bne	$18,$2,$L134
	addiu	$7,$sp,296

	lhu	$4,30($17)
	addiu	$6,$sp,300
	jal	bm_seconds_to_hms
	addiu	$5,$sp,304

	lw	$2,296($sp)
	lw	$6,304($sp)
	lw	$7,300($sp)
	lui	$5,%hi($LC36)
	addiu	$5,$5,%lo($LC36)
	addiu	$4,$sp,32
	jal	local_sprintf
	sw	$2,16($sp)

	move	$6,$2
	addiu	$5,$sp,32
	move	$4,$16
	jal	btc_fwrite
	move	$17,$2

	bne	$17,$2,$L134
	nop

	jal	btc_fclose
	move	$4,$16

	lw	$31,340($sp)
$L141:
	lw	$21,336($sp)
	lw	$20,332($sp)
	lw	$19,328($sp)
	lw	$18,324($sp)
	lw	$17,320($sp)
	lw	$16,316($sp)
	jr	$31
	addiu	$sp,$sp,344

$L138:
	b	$L135
	addiu	$6,$6,%lo($LC17)

$L134:
	jal	btc_fclose
	move	$4,$16

	lui	$4,%hi($LC37)
	jal	tty_printf
	addiu	$4,$4,%lo($LC37)

	b	$L141
	lw	$31,340($sp)

	.set	macro
	.set	reorder
	.end	bm_fprint_battery_telemetry
	.size	bm_fprint_battery_telemetry, .-bm_fprint_battery_telemetry
	.section	.rodata.str1.4
	.align	2
$LC38:
	.ascii	"%s\000"
	.align	2
$LC39:
	.ascii	"Total Energy Available: %d.%03d Joules\012\000"
	.align	2
$LC40:
	.ascii	"       Energy Consumed: %d.%03d Joules\012\000"
	.align	2
$LC41:
	.ascii	"   Cold Battery Energy: %d.%03d Joules\012\000"
	.align	2
$LC42:
	.ascii	"      Remaining Energy: %d.%03d Joules\012\000"
	.align	2
$LC43:
	.ascii	"  - no Flash          : %d \012\000"
	.align	2
$LC44:
	.ascii	"  - low Flash         : %d \012\000"
	.align	2
$LC45:
	.ascii	"  - hi Flash          : %d \012\012\000"
	.align	2
$LC46:
	.ascii	"Total Video Taken    %d seconds;  %02d:%02d:%02d \012\000"
	.align	2
$LC47:
	.ascii	"  - no Flash           : %02d:%02d:%02d \012\000"
	.align	2
$LC48:
	.ascii	"  - low Flash          : %02d:%02d:%02d \012\000"
	.align	2
$LC49:
	.ascii	"  - hi Flash           : %02d:%02d:%02d \012\000"
	.text
	.align	2
	.globl	bm_print_battery_telemetry
	.set	nomips16
	.set	nomicromips
	.ent	bm_print_battery_telemetry
	.type	bm_print_battery_telemetry, @function
bm_print_battery_telemetry:
	.frame	$sp,336,$31		# vars= 280, regs= 6/0, args= 32, gp= 0
	.mask	0x801f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-336
	lui	$5,%hi($LC19)
	addiu	$5,$5,%lo($LC19)
	sw	$17,316($sp)
	addiu	$4,$sp,32
	lui	$17,%hi($LC38)
	sw	$31,332($sp)
	sw	$19,324($sp)
	sw	$16,312($sp)
	sw	$20,328($sp)
	jal	local_sprintf
	sw	$18,320($sp)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	jal	get_battery_voltage_x100
	lui	$19,%hi(setDigitalEffectswitchdataD_table)

	sll	$2,$2,16
	sra	$2,$2,16
	li	$6,100			# 0x64
	div	$0,$2,$6
	nop
	teq	$6,$0,7
	lui	$5,%hi($LC20)
	addiu	$5,$5,%lo($LC20)
	addiu	$4,$sp,32
	mfhi	$7
	mflo	$6
	jal	local_sprintf
	addiu	$16,$19,%lo(setDigitalEffectswitchdataD_table)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	jal	tty_printf_battery_stats
	nop

	lbu	$2,37($16)
	lbu	$7,34($16)
	lbu	$6,33($16)
	sw	$2,28($sp)
	lbu	$2,36($16)
	lui	$5,%hi($LC21)
	addiu	$5,$5,%lo($LC21)
	sw	$2,24($sp)
	lbu	$2,35($16)
	addiu	$4,$sp,32
	sw	$2,20($sp)
	lbu	$2,32($16)
	addiu	$2,$2,2000
	jal	local_sprintf
	sw	$2,16($sp)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	jal	get_short_rtc_time
	addiu	$4,$sp,288

	lh	$2,298($sp)
	lh	$7,292($sp)
	lh	$6,290($sp)
	sw	$2,28($sp)
	lh	$2,296($sp)
	lui	$5,%hi($LC22)
	addiu	$5,$5,%lo($LC22)
	sw	$2,24($sp)
	lh	$2,294($sp)
	addiu	$4,$sp,32
	sw	$2,20($sp)
	lh	$2,288($sp)
	jal	local_sprintf
	sw	$2,16($sp)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lh	$2,50($16)
	beq	$2,$0,$L145
	lui	$6,%hi($LC17)

	lui	$6,%hi($LC18)
	addiu	$6,$6,%lo($LC18)
$L143:
	lui	$5,%hi($LC23)
	addiu	$5,$5,%lo($LC23)
	jal	local_sprintf
	addiu	$4,$sp,32

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lh	$4,50($16)
	jal	bm_get_initial_battery_capacity
	li	$20,1000			# 0x3e8

	andi	$7,$2,0xff
	mult	$7,$20
	mflo	$7
	lui	$5,%hi($LC39)
	srl	$6,$2,8
	addiu	$5,$5,%lo($LC39)
	addiu	$4,$sp,32
	move	$18,$2
	jal	local_sprintf
	srl	$7,$7,8

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lw	$6,%lo(setDigitalEffectswitchdataD_table)($19)
	lui	$5,%hi($LC40)
	addiu	$5,$5,%lo($LC40)
	andi	$7,$6,0xff
	mult	$7,$20
	mflo	$7
	srl	$6,$6,8
	addiu	$4,$sp,32
	jal	local_sprintf
	srl	$7,$7,8

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lw	$6,4($16)
	lui	$5,%hi($LC41)
	addiu	$5,$5,%lo($LC41)
	andi	$7,$6,0xff
	mult	$7,$20
	mflo	$7
	srl	$6,$6,8
	addiu	$4,$sp,32
	jal	local_sprintf
	srl	$7,$7,8

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lw	$2,%lo(setDigitalEffectswitchdataD_table)($19)
	lw	$3,4($16)
	addu	$2,$2,$3
	sltu	$3,$18,$2
	bne	$3,$0,$L144
	move	$19,$0

	subu	$19,$18,$2
$L144:
	andi	$7,$19,0xff
	li	$2,1000			# 0x3e8
	mult	$7,$2
	mflo	$7
	lui	$5,%hi($LC42)
	srl	$6,$19,8
	addiu	$4,$sp,32
	addiu	$5,$5,%lo($LC42)
	jal	local_sprintf
	srl	$7,$7,8

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	li	$6,100			# 0x64
	mult	$19,$6
	mflo	$6
	lui	$5,%hi($LC28)
	addiu	$4,$sp,32
	divu	$0,$6,$18
	nop
	teq	$18,$0,7
	mflo	$6
	jal	local_sprintf
	addiu	$5,$5,%lo($LC28)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lhu	$6,22($16)
	lhu	$2,20($16)
	lui	$5,%hi($LC29)
	addiu	$4,$sp,32
	addu	$2,$2,$6
	lhu	$6,24($16)
	addiu	$5,$5,%lo($LC29)
	jal	local_sprintf
	addu	$6,$2,$6

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lhu	$6,20($16)
	lui	$5,%hi($LC43)
	addiu	$4,$sp,32
	jal	local_sprintf
	addiu	$5,$5,%lo($LC43)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lhu	$6,22($16)
	lui	$5,%hi($LC44)
	addiu	$4,$sp,32
	jal	local_sprintf
	addiu	$5,$5,%lo($LC44)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lhu	$6,24($16)
	lui	$5,%hi($LC45)
	addiu	$4,$sp,32
	jal	local_sprintf
	addiu	$5,$5,%lo($LC45)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lhu	$4,28($16)
	lhu	$8,26($16)
	addiu	$7,$sp,300
	addiu	$6,$sp,304
	addu	$8,$8,$4
	lhu	$4,30($16)
	addiu	$5,$sp,308
	addu	$8,$8,$4
	jal	bm_seconds_to_hms
	move	$4,$8

	lw	$2,300($sp)
	lw	$7,308($sp)
	lui	$5,%hi($LC46)
	sw	$2,20($sp)
	lw	$2,304($sp)
	move	$6,$8
	addiu	$4,$sp,32
	sw	$2,16($sp)
	jal	local_sprintf
	addiu	$5,$5,%lo($LC46)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lhu	$4,26($16)
	addiu	$7,$sp,300
	addiu	$6,$sp,304
	jal	bm_seconds_to_hms
	addiu	$5,$sp,308

	lw	$2,300($sp)
	lw	$7,304($sp)
	lw	$6,308($sp)
	lui	$5,%hi($LC47)
	addiu	$4,$sp,32
	sw	$2,16($sp)
	jal	local_sprintf
	addiu	$5,$5,%lo($LC47)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lhu	$4,28($16)
	addiu	$7,$sp,300
	addiu	$6,$sp,304
	jal	bm_seconds_to_hms
	addiu	$5,$sp,308

	lw	$2,300($sp)
	lw	$7,304($sp)
	lw	$6,308($sp)
	lui	$5,%hi($LC48)
	addiu	$4,$sp,32
	sw	$2,16($sp)
	jal	local_sprintf
	addiu	$5,$5,%lo($LC48)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lhu	$4,30($16)
	addiu	$7,$sp,300
	addiu	$6,$sp,304
	jal	bm_seconds_to_hms
	addiu	$5,$sp,308

	lw	$2,300($sp)
	lw	$7,304($sp)
	lw	$6,308($sp)
	lui	$5,%hi($LC49)
	addiu	$4,$sp,32
	sw	$2,16($sp)
	jal	local_sprintf
	addiu	$5,$5,%lo($LC49)

	addiu	$5,$sp,32
	jal	tty_printf
	addiu	$4,$17,%lo($LC38)

	lw	$31,332($sp)
	lw	$20,328($sp)
	lw	$19,324($sp)
	lw	$18,320($sp)
	lw	$17,316($sp)
	lw	$16,312($sp)
	jr	$31
	addiu	$sp,$sp,336

$L145:
	b	$L143
	addiu	$6,$6,%lo($LC17)

	.set	macro
	.set	reorder
	.end	bm_print_battery_telemetry
	.size	bm_print_battery_telemetry, .-bm_print_battery_telemetry
	.section	.rodata.str1.4
	.align	2
$LC50:
	.ascii	"WBWL Info::bm_initialize:\000"
	.text
	.align	2
	.globl	bm_initialize
	.set	nomips16
	.set	nomicromips
	.ent	bm_initialize
	.type	bm_initialize, @function
bm_initialize:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$17,24($sp)
	sw	$16,20($sp)
	move	$17,$4
	lui	$16,%hi(setDigitalEffectswitchdataD_table)
	lui	$4,%hi(setDigitalEffectswitchdataD_table+32)
	sw	$0,%lo(setDigitalEffectswitchdataD_table)($16)
	addiu	$4,$4,%lo(setDigitalEffectswitchdataD_table+32)
	addiu	$16,$16,%lo(setDigitalEffectswitchdataD_table)
	sw	$31,28($sp)
	sw	$0,4($16)
	sw	$0,8($16)
	sw	$0,12($16)
	sw	$0,16($16)
	sw	$0,20($16)
	sw	$0,24($16)
	jal	bm_get_byte_rtc_time
	sw	$0,28($16)

	lui	$4,%hi(setDigitalEffectswitchdataD_table+38)
	jal	bm_get_byte_rtc_time
	addiu	$4,$4,%lo(setDigitalEffectswitchdataD_table+38)

	lui	$4,%hi(setDigitalEffectswitchdataD_table+44)
	jal	bm_get_byte_rtc_time
	addiu	$4,$4,%lo(setDigitalEffectswitchdataD_table+44)

	lui	$4,%hi($LC50)
	addiu	$4,$4,%lo($LC50)
	jal	tty_printf
	sh	$17,50($16)

	lw	$31,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	bm_print_battery_telemetry
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	bm_initialize
	.size	bm_initialize, .-bm_initialize
	.align	2
	.globl	bm_set_g_cold_item_battery_type
	.set	nomips16
	.set	nomicromips
	.ent	bm_set_g_cold_item_battery_type
	.type	bm_set_g_cold_item_battery_type, @function
bm_set_g_cold_item_battery_type:
	.frame	$sp,24,$31		# vars= 0, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$16,16($sp)
	sw	$31,20($sp)
	jal	set_g_cold_item_battery_type
	move	$16,$4

	lw	$31,20($sp)
	move	$4,$16
	lw	$16,16($sp)
	j	bm_initialize
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	bm_set_g_cold_item_battery_type
	.size	bm_set_g_cold_item_battery_type, .-bm_set_g_cold_item_battery_type
	.align	2
	.globl	bm_HceCommon_RestoreDefaultColdItem_hook
	.set	nomips16
	.set	nomicromips
	.ent	bm_HceCommon_RestoreDefaultColdItem_hook
	.type	bm_HceCommon_RestoreDefaultColdItem_hook, @function
bm_HceCommon_RestoreDefaultColdItem_hook:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	HceCommon_RestoreDefaultColdItem
	nop

	lw	$31,20($sp)
	move	$4,$0
	j	bm_initialize
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	bm_HceCommon_RestoreDefaultColdItem_hook
	.size	bm_HceCommon_RestoreDefaultColdItem_hook, .-bm_HceCommon_RestoreDefaultColdItem_hook
	.section	.rodata.str1.4
	.align	2
$LC51:
	.ascii	"Info::bm_StoreBatteryMonitorFile: Elapsed time in second"
	.ascii	"s: %d \012\000"
	.align	2
$LC52:
	.ascii	"Info::bm_StoreBatteryMonitorFile: Sleeping at %d/%d/%d %"
	.ascii	"02d:%02d:%02d\012\000"
	.align	2
$LC53:
	.ascii	"B:\\USER_RES\\BMON.BIN\000"
	.align	2
$LC54:
	.ascii	"Error::bm_StoreBatteryMonitorFile: failed to open BMON.B"
	.ascii	"IN\000"
	.align	2
$LC55:
	.ascii	"Info::bm_StoreBatteryMonitorFile:_%d/%d_<%dms>\012\000"
	.text
	.align	2
	.globl	bm_StoreBatteryMonitorFile
	.set	nomips16
	.set	nomicromips
	.ent	bm_StoreBatteryMonitorFile
	.type	bm_StoreBatteryMonitorFile, @function
bm_StoreBatteryMonitorFile:
	.frame	$sp,64,$31		# vars= 8, regs= 5/0, args= 32, gp= 0
	.mask	0x800f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-64
	sw	$18,52($sp)
	sw	$17,48($sp)
	lui	$18,%hi(setDigitalEffectswitchdataD_table+44)
	lui	$17,%hi(setDigitalEffectswitchdataD_table)
	sw	$16,44($sp)
	addiu	$4,$18,%lo(setDigitalEffectswitchdataD_table+44)
	addiu	$16,$17,%lo(setDigitalEffectswitchdataD_table)
	sw	$31,60($sp)
	jal	bm_get_byte_rtc_time
	sw	$19,56($sp)

	lhu	$3,10($16)
	lhu	$2,8($16)
	sw	$0,8($16)
	addu	$2,$2,$3
	lhu	$3,12($16)
	addu	$2,$2,$3
	lhu	$3,14($16)
	sw	$0,12($16)
	addu	$2,$2,$3
	lhu	$3,16($16)
	addu	$2,$2,$3
	lhu	$3,18($16)
	addu	$2,$2,$3
	bne	$2,$0,$L155
	sw	$0,16($16)

	lui	$5,%hi(setDigitalEffectswitchdataD_table+38)
	addiu	$4,$18,%lo(setDigitalEffectswitchdataD_table+44)
	jal	bm_get_delta_byte_time
	addiu	$5,$5,%lo(setDigitalEffectswitchdataD_table+38)

	jal	set_pre_printf_state
	move	$18,$2

	lui	$4,%hi($LC51)
	move	$5,$18
	jal	tty_printf
	addiu	$4,$4,%lo($LC51)

	jal	check_post_printf_state_set_sio_params
	nop

	jal	bm_get_ui_energy
	move	$4,$18

	move	$4,$2
	jal	bm_increment_energy_consumed
	li	$5,460			# 0x1cc

$L155:
	jal	set_pre_printf_state
	lui	$19,%hi($LC53)

	lbu	$2,49($16)
	lbu	$7,44($16)
	lui	$4,%hi($LC52)
	sw	$2,24($sp)
	lbu	$2,48($16)
	addiu	$7,$7,2000
	addiu	$4,$4,%lo($LC52)
	sw	$2,20($sp)
	lbu	$2,47($16)
	sw	$2,16($sp)
	lbu	$6,46($16)
	jal	tty_printf
	lbu	$5,45($16)

	jal	check_post_printf_state_set_sio_params
	nop

	jal	bm_print_battery_telemetry
	nop

	jal	get_current_operating_time_ms
	nop

	li	$5,32			# 0x20
	addiu	$4,$19,%lo($LC53)
	jal	btc_fopen
	move	$18,$2

	bne	$2,$0,$L156
	move	$16,$2

	li	$5,36			# 0x24
	jal	btc_fopen
	addiu	$4,$19,%lo($LC53)

	bne	$2,$0,$L156
	move	$16,$2

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC54)
	jal	tty_printf
	addiu	$4,$4,%lo($LC54)

	jal	check_post_printf_state_set_sio_params
	nop

	move	$2,$0
$L154:
	lw	$31,60($sp)
	lw	$19,56($sp)
	lw	$18,52($sp)
	lw	$17,48($sp)
	lw	$16,44($sp)
	jr	$31
	addiu	$sp,$sp,64

$L156:
	move	$7,$0
	move	$6,$0
	move	$5,$0
	move	$4,$16
	jal	seekToSpecifiedFileLocation
	sw	$0,16($sp)

	li	$6,52			# 0x34
	addiu	$5,$17,%lo(setDigitalEffectswitchdataD_table)
	jal	btc_fwrite
	move	$4,$16

	move	$4,$16
	jal	btc_fclose
	move	$17,$2

	jal	get_current_operating_time_ms
	nop

	move	$4,$2
	jal	positive_diff
	move	$5,$18

	jal	set_pre_printf_state
	sw	$2,32($sp)

	lw	$7,32($sp)
	lui	$4,%hi($LC55)
	li	$6,52			# 0x34
	move	$5,$17
	jal	tty_printf
	addiu	$4,$4,%lo($LC55)

	jal	check_post_printf_state_set_sio_params
	nop

	b	$L154
	li	$2,1			# 0x1

	.set	macro
	.set	reorder
	.end	bm_StoreBatteryMonitorFile
	.size	bm_StoreBatteryMonitorFile, .-bm_StoreBatteryMonitorFile
	.align	2
	.globl	store_pressure_bm_hook
	.set	nomips16
	.set	nomicromips
	.ent	store_pressure_bm_hook
	.type	store_pressure_bm_hook, @function
store_pressure_bm_hook:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	store_pressure_trend
	nop

	lw	$31,20($sp)
	j	bm_StoreBatteryMonitorFile
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	store_pressure_bm_hook
	.size	store_pressure_bm_hook, .-store_pressure_bm_hook
	.section	.rodata.str1.4
	.align	2
$LC56:
	.ascii	"WBWL Info::bm_on_power_up - e\012\000"
	.align	2
$LC57:
	.ascii	"bm_LoadBatteryMonitorFile\000"
	.align	2
$LC58:
	.ascii	"Error:: %s Cannot open B:\\USER_RES\\BMON.BIN\012\000"
	.align	2
$LC59:
	.ascii	"Info::bm_LoadBatteryMonitorFile: Elapsed time in hours s"
	.ascii	"ince last asleep %d\012\000"
	.align	2
$LC60:
	.ascii	"Info::bm_LoadBatteryMonitorFile: Awake at %d/%d/%d %02d:"
	.ascii	"%02d:%02d\012\000"
	.text
	.align	2
	.globl	bm_LoadBatteryMonitorFile
	.set	nomips16
	.set	nomicromips
	.ent	bm_LoadBatteryMonitorFile
	.type	bm_LoadBatteryMonitorFile, @function
bm_LoadBatteryMonitorFile:
	.frame	$sp,56,$31		# vars= 8, regs= 4/0, args= 32, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-56
	sw	$31,52($sp)
	sw	$18,48($sp)
	sw	$17,44($sp)
	jal	set_pre_printf_state
	sw	$16,40($sp)

	lui	$4,%hi($LC56)
	jal	tty_printf
	addiu	$4,$4,%lo($LC56)

	jal	check_post_printf_state_set_sio_params
	nop

	lui	$4,%hi($LC53)
	li	$5,16			# 0x10
	jal	btc_fopen
	addiu	$4,$4,%lo($LC53)

	bne	$2,$0,$L162
	lui	$18,%hi(setDigitalEffectswitchdataD_table)

	jal	set_pre_printf_state
	nop

	lui	$5,%hi($LC57)
	lui	$4,%hi($LC58)
	addiu	$5,$5,%lo($LC57)
	jal	tty_printf
	addiu	$4,$4,%lo($LC58)

	jal	check_post_printf_state_set_sio_params
	nop

	jal	bm_initialize
	move	$4,$0

	move	$2,$0
$L161:
	lw	$31,52($sp)
	lw	$18,48($sp)
	lw	$17,44($sp)
	lw	$16,40($sp)
	jr	$31
	addiu	$sp,$sp,56

$L162:
	move	$4,$2
	li	$6,52			# 0x34
	addiu	$5,$18,%lo(setDigitalEffectswitchdataD_table)
	jal	btc_fread
	sw	$2,32($sp)

	lw	$4,32($sp)
	move	$16,$2
	jal	btc_fclose
	sltu	$16,$16,52

	beq	$16,$0,$L166
	lui	$17,%hi(setDigitalEffectswitchdataD_table+38)

	jal	bm_initialize
	move	$4,$0

	lui	$17,%hi(setDigitalEffectswitchdataD_table+38)
$L166:
	jal	bm_get_byte_rtc_time
	addiu	$4,$17,%lo(setDigitalEffectswitchdataD_table+38)

	lui	$5,%hi(setDigitalEffectswitchdataD_table+44)
	addiu	$5,$5,%lo(setDigitalEffectswitchdataD_table+44)
	jal	bm_get_delta_byte_time
	addiu	$4,$17,%lo(setDigitalEffectswitchdataD_table+38)

	li	$16,3600			# 0xe10
	div	$0,$2,$16
	nop
	teq	$16,$0,7
	mflo	$16
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC59)
	move	$5,$16
	jal	tty_printf
	addiu	$4,$4,%lo($LC59)

	jal	check_post_printf_state_set_sio_params
	nop

	li	$5,64			# 0x40
	jal	bm_increment_energy_consumed
	sll	$4,$16,6

	li	$4,1392			# 0x570
	mult	$16,$4
	mflo	$4
	jal	bm_increment_energy_consumed
	move	$5,$0

	jal	bm_get_byte_rtc_time
	addiu	$4,$17,%lo(setDigitalEffectswitchdataD_table+38)

	jal	set_pre_printf_state
	nop

	addiu	$2,$18,%lo(setDigitalEffectswitchdataD_table)
	lbu	$3,43($2)
	lbu	$7,38($2)
	lui	$4,%hi($LC60)
	sw	$3,24($sp)
	lbu	$3,42($2)
	addiu	$7,$7,2000
	addiu	$4,$4,%lo($LC60)
	sw	$3,20($sp)
	lbu	$3,41($2)
	sw	$3,16($sp)
	lbu	$6,40($2)
	jal	tty_printf
	lbu	$5,39($2)

	jal	check_post_printf_state_set_sio_params
	nop

	jal	bm_print_battery_telemetry
	nop

	b	$L161
	li	$2,1			# 0x1

	.set	macro
	.set	reorder
	.end	bm_LoadBatteryMonitorFile
	.size	bm_LoadBatteryMonitorFile, .-bm_LoadBatteryMonitorFile
	.align	2
	.globl	bm_Volt_Calib_Bat_hook
	.set	nomips16
	.set	nomicromips
	.ent	bm_Volt_Calib_Bat_hook
	.type	bm_Volt_Calib_Bat_hook, @function
bm_Volt_Calib_Bat_hook:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	Volt_Calib_Bat
	nop

	lw	$31,20($sp)
	j	bm_LoadBatteryMonitorFile
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	bm_Volt_Calib_Bat_hook
	.size	bm_Volt_Calib_Bat_hook, .-bm_Volt_Calib_Bat_hook
	.section	.rodata.str1.4
	.align	2
$LC62:
	.ascii	"Info::bm_write_summary_file: writing summary to %s \012\000"
	.align	2
$LC63:
	.ascii	"Error::bm_write_summary_file -- could not open: %s for w"
	.ascii	"riting\012\000"
	.align	2
$LC61:
	.ascii	"D:\\BatLog.txt\000"
	.text
	.align	2
	.globl	bm_write_summary_file
	.set	nomips16
	.set	nomicromips
	.ent	bm_write_summary_file
	.type	bm_write_summary_file, @function
bm_write_summary_file:
	.frame	$sp,40,$31		# vars= 16, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	lui	$5,%hi($LC61)
	li	$6,14			# 0xe
	addiu	$5,$5,%lo($LC61)
	sw	$31,36($sp)
	jal	memcpy
	addiu	$4,$sp,16

	lui	$4,%hi($LC62)
	addiu	$5,$sp,16
	jal	tty_printf
	addiu	$4,$4,%lo($LC62)

	jal	bm_print_battery_telemetry
	nop

	li	$5,32			# 0x20
	jal	btc_fopen
	addiu	$4,$sp,16

	bnel	$2,$0,$L172
	move	$4,$2

	addiu	$4,$sp,16
	jal	btc_fopen
	li	$5,36			# 0x24

	bne	$2,$0,$L170
	move	$4,$2

	lui	$4,%hi($LC63)
	addiu	$5,$sp,16
	jal	tty_printf
	addiu	$4,$4,%lo($LC63)

	lw	$31,36($sp)
$L174:
	jr	$31
	addiu	$sp,$sp,40

$L172:
$L170:
	jal	bm_fprint_battery_telemetry
	nop

	b	$L174
	lw	$31,36($sp)

	.set	macro
	.set	reorder
	.end	bm_write_summary_file
	.size	bm_write_summary_file, .-bm_write_summary_file
	.align	2
	.globl	bm_handleBatteryTypeMenu
	.set	nomips16
	.set	nomicromips
	.ent	bm_handleBatteryTypeMenu
	.type	bm_handleBatteryTypeMenu, @function
bm_handleBatteryTypeMenu:
	.frame	$sp,32,$31		# vars= 0, regs= 4/0, args= 16, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$16,16($sp)
	sw	$31,28($sp)
	sw	$18,24($sp)
	jal	getCameraConfigStructPtr
	sw	$17,20($sp)

	move	$16,$2
	lbu	$2,0($2)
	beq	$2,$0,$L176
	nop

	jal	get_g_cold_item_battery_type
	sb	$0,0($16)

	sb	$2,2($16)
	lw	$31,28($sp)
	lw	$18,24($sp)
	lw	$17,20($sp)
	addiu	$4,$16,2
	lw	$16,16($sp)
	lui	$5,%hi(g_menu_root)
	addiu	$5,$5,%lo(g_menu_root)
	j	menu_draw_selected_item
	addiu	$sp,$sp,32

$L176:
	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L177
	lui	$2,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L187
	move	$4,$0

$L177:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	li	$3,1			# 0x1
	bne	$2,$3,$L179
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L178
	li	$4,1			# 0x1

$L179:
	jal	ui_cursor_key_pressed_p
	li	$4,3			# 0x3

	li	$3,1			# 0x1
	beq	$2,$3,$L180
	lui	$2,%hi(g_right_button_enable)

$L181:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$3,1			# 0x1
	bne	$2,$3,$L182
	lui	$2,%hi(g_left_button_enable)

	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L191
	lw	$31,28($sp)

$L182:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	move	$18,$2
	li	$2,1			# 0x1
	bne	$18,$2,$L184
	lui	$2,%hi(g_enter_button_enable)

	lbu	$3,%lo(g_enter_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L184
	lui	$3,%hi(g_camera_setup_menu_item_array)

	lbu	$4,2($16)
	addiu	$3,$3,%lo(g_camera_setup_menu_item_array)
	sll	$2,$4,3
	sb	$18,0($16)
	addu	$3,$3,$2
	lw	$6,4($3)
	lw	$5,0($3)
	lui	$7,%hi(g_menu_root)
	jal	get_next_state_from_menu_enter
	addiu	$7,$7,%lo(g_menu_root)

	move	$17,$2
	li	$2,255			# 0xff
	beq	$17,$2,$L191
	lw	$31,28($sp)

	jal	bm_set_g_cold_item_battery_type
	lbu	$4,2($16)

	jal	setBatteryCalibConfig
	nop

	sb	$18,4($16)
$L186:
	lw	$31,28($sp)
$L190:
	lw	$18,24($sp)
	lw	$16,16($sp)
	move	$4,$17
	lw	$17,20($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L187:
$L178:
	lui	$17,%hi(g_menu_root)
	addiu	$5,$16,2
	addiu	$7,$17,%lo(g_menu_root)
	jal	menu_get_next_menu_selection
	li	$6,1			# 0x1

	lbu	$4,2($16)
	lw	$31,28($sp)
	lw	$18,24($sp)
	lw	$16,16($sp)
	addiu	$5,$17,%lo(g_menu_root)
	lw	$17,20($sp)
	j	menu_redraw_items
	addiu	$sp,$sp,32

$L180:
	lbu	$3,%lo(g_right_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L181
	lw	$31,28($sp)

	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	j	bm_write_summary_file
	addiu	$sp,$sp,32

$L184:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L191
	lw	$31,28($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L192
	lw	$18,24($sp)

	lui	$5,%hi(g_menu_root)
	sh	$2,0($16)
	addiu	$5,$5,%lo(g_menu_root)
	jal	get_next_state_from_menu_mode
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,255			# 0xff
	beql	$17,$2,$L186
	li	$17,31			# 0x1f

	b	$L190
	lw	$31,28($sp)

$L191:
	lw	$18,24($sp)
$L192:
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	bm_handleBatteryTypeMenu
	.size	bm_handleBatteryTypeMenu, .-bm_handleBatteryTypeMenu
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
