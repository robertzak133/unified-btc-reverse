	.file	1 "aperture.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	apt_get_cold_item_aperture
	.set	nomips16
	.set	nomicromips
	.ent	apt_get_cold_item_aperture
	.type	apt_get_cold_item_aperture, @function
apt_get_cold_item_aperture:
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
	.end	apt_get_cold_item_aperture
	.size	apt_get_cold_item_aperture, .-apt_get_cold_item_aperture
	.align	2
	.globl	apt_set_cold_item_aperture
	.set	nomips16
	.set	nomicromips
	.ent	apt_set_cold_item_aperture
	.type	apt_set_cold_item_aperture, @function
apt_set_cold_item_aperture:
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

	lw	$2,16($sp)
	li	$3,-65536			# 0xffffffffffff0000
	addiu	$3,$3,16383
	sll	$16,$16,14
	and	$2,$2,$3
	andi	$16,$16,0xffff
	or	$16,$2,$16
	addiu	$4,$sp,16
	li	$6,2			# 0x2
	li	$5,6			# 0x6
	jal	set_rtc_extra_byte_range
	sw	$16,16($sp)

	lw	$31,36($sp)
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,40

	.set	macro
	.set	reorder
	.end	apt_set_cold_item_aperture
	.size	apt_set_cold_item_aperture, .-apt_set_cold_item_aperture
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
	sltu	$2,$6,3
	beql	$2,$0,$L6
	move	$6,$0

$L6:
	lui	$2,%hi(g_apt_nightmode_threshold_lookup_table)
	addiu	$2,$2,%lo(g_apt_nightmode_threshold_lookup_table)
	sll	$6,$6,3
	addu	$6,$6,$2
	lw	$2,0($6)
	sw	$2,0($4)
	lw	$2,4($6)
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
	.frame	$sp,48,$31		# vars= 8, regs= 5/0, args= 16, gp= 0
	.mask	0x800f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-48
	sw	$17,32($sp)
	sw	$31,44($sp)
	sw	$19,40($sp)
	sw	$18,36($sp)
	jal	read_photo_sensor_value
	sw	$16,28($sp)

	move	$17,$2
	sltu	$2,$2,1001
	bne	$2,$0,$L8
	lui	$2,%hi(g_photo_sensor_value)

	jal	HceIQ_CheckNightMode
	nop

$L9:
	lw	$31,44($sp)
	lw	$19,40($sp)
	lw	$18,36($sp)
	lw	$17,32($sp)
	lw	$16,28($sp)
	jr	$31
	addiu	$sp,$sp,48

$L8:
	lui	$19,%hi(g_new_check_night_mode_p)
	sw	$17,%lo(g_photo_sensor_value)($2)
	lbu	$2,%lo(g_new_check_night_mode_p)($19)
	bne	$2,$0,$L10
	lui	$18,%hi(g_night_mode_p)

	lbu	$16,%lo(g_night_mode_p)($18)
$L11:
	jal	apt_get_cold_item_aperture
	nop

	move	$6,$2
	addiu	$5,$sp,16
	jal	apt_get_night_mode_threshold_min_max
	addiu	$4,$sp,20

	bne	$16,$0,$L12
	lw	$3,16($sp)

	lw	$3,20($sp)
$L12:
	sltu	$2,$17,$3
	lui	$3,%hi(g_photo_detector_hysteresis)
	sb	$2,%lo(g_night_mode_p)($18)
	b	$L9
	sb	$16,%lo(g_photo_detector_hysteresis)($3)

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
	.size	g_apt_nightmode_threshold_lookup_table, 24
g_apt_nightmode_threshold_lookup_table:
	.word	25
	.word	40
	.word	12
	.word	20
	.word	0
	.word	0

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,248,4

	.comm	g_wbwl_camera_setup_menu_item_array,868,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
