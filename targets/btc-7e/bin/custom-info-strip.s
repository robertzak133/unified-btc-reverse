	.file	1 "custom-info-strip.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"%02d/%02d/%04d \000"
	.align	2
$LC1:
	.ascii	"%04d%02d%02d \000"
	.text
	.align	2
	.globl	wbwl_custom_info_strip_date_sprintf
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_custom_info_strip_date_sprintf
	.type	wbwl_custom_info_strip_date_sprintf, @function
wbwl_custom_info_strip_date_sprintf:
	.frame	$sp,40,$31		# vars= 8, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$17,32($sp)
	sw	$16,28($sp)
	sw	$4,20($sp)
	move	$16,$6
	lw	$17,56($sp)
	sw	$31,36($sp)
	jal	rtc_get_cold_item_date_format
	sw	$7,16($sp)

	li	$3,1			# 0x1
	lw	$6,16($sp)
	beq	$2,$3,$L2
	lw	$4,20($sp)

	li	$3,2			# 0x2
	beq	$2,$3,$L3
	lui	$5,%hi($LC1)

	move	$7,$6
	sw	$17,56($sp)
	move	$6,$16
$L6:
	lui	$5,%hi($LC0)
	addiu	$5,$5,%lo($LC0)
$L5:
	lw	$31,36($sp)
	lw	$17,32($sp)
	lw	$16,28($sp)
	j	local_sprintf
	addiu	$sp,$sp,40

$L2:
	sw	$17,56($sp)
	b	$L6
	move	$7,$16

$L3:
	sw	$6,56($sp)
	move	$7,$16
	move	$6,$17
	b	$L5
	addiu	$5,$5,%lo($LC1)

	.set	macro
	.set	reorder
	.end	wbwl_custom_info_strip_date_sprintf
	.size	wbwl_custom_info_strip_date_sprintf, .-wbwl_custom_info_strip_date_sprintf
	.section	.rodata.str1.4
	.align	2
$LC2:
	.ascii	"%02d:%02d:%02d %s \000"
	.align	2
$LC3:
	.ascii	"%02d:%02d:%02d \000"
	.text
	.align	2
	.globl	wbwl_custom_info_strip_time_sprintf
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_custom_info_strip_time_sprintf
	.type	wbwl_custom_info_strip_time_sprintf, @function
wbwl_custom_info_strip_time_sprintf:
	.frame	$sp,80,$31		# vars= 40, regs= 3/0, args= 24, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-80
	addiu	$5,$sp,24
	sw	$16,68($sp)
	move	$16,$4
	move	$4,$0
	sw	$31,76($sp)
	sw	$17,72($sp)
	sw	$6,88($sp)
	jal	get_rtc_time_or_alarm
	sw	$7,92($sp)

	jal	rtc_get_cold_item_time_format
	lw	$17,24($sp)

	li	$3,1			# 0x1
	beq	$2,$3,$L8
	lw	$7,92($sp)

	lw	$2,96($sp)
	lw	$6,88($sp)
	lui	$5,%hi($LC2)
	sw	$2,20($sp)
	sw	$17,16($sp)
	addiu	$5,$5,%lo($LC2)
	jal	local_sprintf
	move	$4,$16

	lw	$31,76($sp)
$L11:
	lw	$17,72($sp)
	lw	$16,68($sp)
	jr	$31
	addiu	$sp,$sp,80

$L8:
	lw	$7,28($sp)
	lw	$6,32($sp)
	lui	$5,%hi($LC3)
	sw	$17,16($sp)
	addiu	$5,$5,%lo($LC3)
	jal	local_sprintf
	move	$4,$16

	b	$L11
	lw	$31,76($sp)

	.set	macro
	.set	reorder
	.end	wbwl_custom_info_strip_time_sprintf
	.size	wbwl_custom_info_strip_time_sprintf, .-wbwl_custom_info_strip_time_sprintf
	.section	.rodata.str1.4
	.align	2
$LC4:
	.ascii	"B:%3d \000"
	.align	2
$LC5:
	.ascii	"B:EXT \000"
	.text
	.align	2
	.globl	wbwl_custom_info_strip_strlen
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_custom_info_strip_strlen
	.type	wbwl_custom_info_strip_strlen, @function
wbwl_custom_info_strip_strlen:
	.frame	$sp,40,$31		# vars= 8, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$31,36($sp)
	sw	$17,32($sp)
	sw	$16,28($sp)
	jal	btc_strlen
	move	$17,$4

	jal	get_power_supply_mode
	move	$16,$2

	bne	$2,$0,$L13
	addu	$4,$17,$16

	jal	get_battery_percent
	sw	$4,16($sp)

	lw	$4,16($sp)
	lui	$5,%hi($LC4)
	move	$6,$2
	jal	local_sprintf
	addiu	$5,$5,%lo($LC4)

	lw	$31,36($sp)
$L16:
	lw	$16,28($sp)
	move	$4,$17
	lw	$17,32($sp)
	j	btc_strlen
	addiu	$sp,$sp,40

$L13:
	lui	$5,%hi($LC5)
	jal	local_sprintf
	addiu	$5,$5,%lo($LC5)

	b	$L16
	lw	$31,36($sp)

	.set	macro
	.set	reorder
	.end	wbwl_custom_info_strip_strlen
	.size	wbwl_custom_info_strip_strlen, .-wbwl_custom_info_strip_strlen
	.align	2
	.globl	wbwl_StampDrawLogo
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_StampDrawLogo
	.type	wbwl_StampDrawLogo, @function
wbwl_StampDrawLogo:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	HceStampDrawLogo
	srl	$5,$5,1

	.set	macro
	.set	reorder
	.end	wbwl_StampDrawLogo
	.size	wbwl_StampDrawLogo, .-wbwl_StampDrawLogo

	.comm	g_rtc_time_format_menu,84,4

	.comm	g_rtc_date_format_menu,112,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
