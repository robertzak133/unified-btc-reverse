	.file	1 "aperture.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	apt_get_rtc_extra_aperture
	.set	nomips16
	.set	nomicromips
	.ent	apt_get_rtc_extra_aperture
	.type	apt_get_rtc_extra_aperture, @function
apt_get_rtc_extra_aperture:
	.frame	$sp,40,$31		# vars= 16, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	addiu	$4,$sp,16
	li	$6,2			# 0x2
	sw	$31,36($sp)
	jal	get_rtc_extra_byte_range
	li	$5,6			# 0x6

	lw	$2,16($sp)
	lw	$31,36($sp)
	addiu	$sp,$sp,40
	sll	$2,$2,16
	jr	$31
	srl	$2,$2,30

	.set	macro
	.set	reorder
	.end	apt_get_rtc_extra_aperture
	.size	apt_get_rtc_extra_aperture, .-apt_get_rtc_extra_aperture
	.align	2
	.globl	apt_get_rtc_extra_operation_mode
	.set	nomips16
	.set	nomicromips
	.ent	apt_get_rtc_extra_operation_mode
	.type	apt_get_rtc_extra_operation_mode, @function
apt_get_rtc_extra_operation_mode:
	.frame	$sp,40,$31		# vars= 16, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	addiu	$4,$sp,16
	li	$6,1			# 0x1
	sw	$31,36($sp)
	jal	get_rtc_extra_byte_range
	li	$5,7			# 0x7

	lbu	$2,16($sp)
	lw	$31,36($sp)
	addiu	$sp,$sp,40
	jr	$31
	andi	$2,$2,0x3f

	.set	macro
	.set	reorder
	.end	apt_get_rtc_extra_operation_mode
	.size	apt_get_rtc_extra_operation_mode, .-apt_get_rtc_extra_operation_mode
	.align	2
	.globl	apt_set_rtc_extra_operation_mode
	.set	nomips16
	.set	nomicromips
	.ent	apt_set_rtc_extra_operation_mode
	.type	apt_set_rtc_extra_operation_mode, @function
apt_set_rtc_extra_operation_mode:
	.frame	$sp,40,$31		# vars= 16, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	li	$6,2			# 0x2
	li	$5,6			# 0x6
	sw	$16,32($sp)
	move	$16,$4
	sw	$31,36($sp)
	jal	get_rtc_extra_byte_range
	addiu	$4,$sp,16

	lhu	$2,16($sp)
	sll	$16,$16,8
	andi	$16,$16,0x3f00
	andi	$2,$2,0xc0ff
	or	$16,$2,$16
	addiu	$4,$sp,16
	li	$6,2			# 0x2
	li	$5,6			# 0x6
	jal	set_rtc_extra_byte_range
	sh	$16,16($sp)

	jal	apt_get_cold_item_aperture
	nop

	jal	apt_set_rtc_extra_aperture
	move	$4,$2

	lw	$31,36($sp)
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,40

	.set	macro
	.set	reorder
	.end	apt_set_rtc_extra_operation_mode
	.size	apt_set_rtc_extra_operation_mode, .-apt_set_rtc_extra_operation_mode
	.align	2
	.globl	apt_get_night_mode_threshold_min_max
	.set	nomips16
	.set	nomicromips
	.ent	apt_get_night_mode_threshold_min_max
	.type	apt_get_night_mode_threshold_min_max, @function
apt_get_night_mode_threshold_min_max:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_apt_nightmode_threshold_lookup_table)
	addiu	$2,$2,%lo(g_apt_nightmode_threshold_lookup_table)
	sll	$6,$6,1
	addu	$6,$6,$2
	lbu	$2,0($6)
	sw	$2,0($4)
	lbu	$2,1($6)
	jr	$31
	sw	$2,0($5)

	.set	macro
	.set	reorder
	.end	apt_get_night_mode_threshold_min_max
	.size	apt_get_night_mode_threshold_min_max, .-apt_get_night_mode_threshold_min_max
	.align	2
	.globl	apt_HceIQ_CheckNightMode
	.set	nomips16
	.set	nomicromips
	.ent	apt_HceIQ_CheckNightMode
	.type	apt_HceIQ_CheckNightMode, @function
apt_HceIQ_CheckNightMode:
	.frame	$sp,40,$31		# vars= 0, regs= 5/0, args= 16, gp= 0
	.mask	0x800f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$17,24($sp)
	sw	$31,36($sp)
	sw	$19,32($sp)
	sw	$18,28($sp)
	jal	read_photo_sensor_value
	sw	$16,20($sp)

	move	$17,$2
	sltu	$2,$2,1001
	bne	$2,$0,$L9
	lui	$2,%hi(g_photo_sensor_value)

	lw	$31,36($sp)
	lw	$19,32($sp)
	lw	$18,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	HceIQ_CheckNightMode
	addiu	$sp,$sp,40

$L9:
	lui	$19,%hi(g_new_check_night_mode_p)
	sw	$17,%lo(g_photo_sensor_value)($2)
	lbu	$2,%lo(g_new_check_night_mode_p)($19)
	bne	$2,$0,$L10
	lui	$18,%hi(g_night_mode_p)

	lbu	$16,%lo(g_night_mode_p)($18)
$L11:
	jal	apt_get_rtc_extra_aperture
	nop

	sll	$3,$2,1
	lui	$2,%hi(g_apt_nightmode_threshold_lookup_table)
	addiu	$2,$2,%lo(g_apt_nightmode_threshold_lookup_table)
	addu	$3,$3,$2
	lbu	$2,0($3)
	bne	$16,$0,$L12
	lbu	$3,1($3)

	move	$3,$2
$L12:
	lw	$31,36($sp)
	sltu	$2,$17,$3
	lui	$3,%hi(g_photo_detector_hysteresis)
	lw	$19,32($sp)
	lw	$17,24($sp)
	sb	$2,%lo(g_night_mode_p)($18)
	sb	$16,%lo(g_photo_detector_hysteresis)($3)
	lw	$18,28($sp)
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,40

$L10:
	jal	photo_sensor_hysteresis
	nop

	move	$16,$2
	b	$L11
	sb	$0,%lo(g_new_check_night_mode_p)($19)

	.set	macro
	.set	reorder
	.end	apt_HceIQ_CheckNightMode
	.size	apt_HceIQ_CheckNightMode, .-apt_HceIQ_CheckNightMode
	.globl	g_apt_nightmode_threshold_lookup_table
	.data
	.align	2
	.type	g_apt_nightmode_threshold_lookup_table, @object
	.size	g_apt_nightmode_threshold_lookup_table, 6
g_apt_nightmode_threshold_lookup_table:
	.byte	90
	.byte	-66
	.byte	45
	.byte	95
	.byte	90
	.byte	-66

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,240,4

	.comm	g_wbwl_camera_setup_menu_item_array,840,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
