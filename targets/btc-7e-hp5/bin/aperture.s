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
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+27)
	lbu	$2,%lo(g_ColdItemData+27)($2)
	jr	$31
	andi	$2,$2,0x3

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
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$3,%hi(g_ColdItemData)
	addiu	$3,$3,%lo(g_ColdItemData)
	lbu	$2,27($3)
	andi	$4,$4,0x3
	andi	$2,$2,0xfc
	or	$2,$2,$4
	jr	$31
	sb	$2,27($3)

	.set	macro
	.set	reorder
	.end	apt_set_cold_item_aperture
	.size	apt_set_cold_item_aperture, .-apt_set_cold_item_aperture
	.align	2
	.globl	apt_get_night_mode_theshold_min_max
	.set	nomips16
	.set	nomicromips
	.ent	apt_get_night_mode_theshold_min_max
	.type	apt_get_night_mode_theshold_min_max, @function
apt_get_night_mode_theshold_min_max:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	sltu	$2,$6,3
	beql	$2,$0,$L4
	move	$6,$0

$L4:
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
	.end	apt_get_night_mode_theshold_min_max
	.size	apt_get_night_mode_theshold_min_max, .-apt_get_night_mode_theshold_min_max
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"PhotoSensor ADC = %d\000"
	.align	2
$LC1:
	.ascii	"apt_HceIQ_CheckNightMode: PhotoSensor ADC = %d\012\000"
	.align	2
$LC2:
	.ascii	"apt_HceIQ_CheckNightMode: Encoded Aperture = %d\012\000"
	.align	2
$LC3:
	.ascii	"apt_HceIQ_CheckNightMode:  min = %d; max = %d\012\000"
	.align	2
$LC4:
	.ascii	"aptHceIQ_CheckNightMode : Value = %d \012\000"
	.align	2
$LC5:
	.ascii	"aptCNMode:V %d;E %d;R %d\012\000"
	.text
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
	sw	$16,28($sp)
	sw	$31,44($sp)
	sw	$19,40($sp)
	sw	$18,36($sp)
	jal	read_photo_sensor_value
	sw	$17,32($sp)

	move	$16,$2
	sltu	$2,$2,10001
	bne	$2,$0,$L6
	lui	$5,%hi($LC0)

	jal	HceIQ_CheckNightMode
	nop

$L7:
	lw	$31,44($sp)
	lw	$19,40($sp)
	lw	$18,36($sp)
	lw	$17,32($sp)
	lw	$16,28($sp)
	jr	$31
	addiu	$sp,$sp,48

$L6:
	move	$6,$16
	lui	$17,%hi(g_photo_sensor_value)
	addiu	$5,$5,%lo($LC0)
	move	$4,$0
	jal	log_printf
	sw	$16,%lo(g_photo_sensor_value)($17)

	jal	set_pre_printf_state
	lui	$19,%hi(g_night_mode_p)

	lw	$5,%lo(g_photo_sensor_value)($17)
	lui	$4,%hi($LC1)
	addiu	$4,$4,%lo($LC1)
	jal	tty_printf
	lui	$17,%hi(g_new_check_night_mode_p)

	jal	check_post_printf_state_set_sio_params
	nop

	lbu	$2,%lo(g_new_check_night_mode_p)($17)
	bne	$2,$0,$L8
	nop

	lbu	$18,%lo(g_night_mode_p)($19)
$L9:
	lui	$2,%hi(g_ColdItemData+27)
	jal	set_pre_printf_state
	lbu	$17,%lo(g_ColdItemData+27)($2)

	lui	$4,%hi($LC2)
	andi	$17,$17,0x3
	move	$5,$17
	jal	tty_printf
	addiu	$4,$4,%lo($LC2)

	jal	check_post_printf_state_set_sio_params
	nop

	move	$6,$17
	addiu	$5,$sp,16
	jal	apt_get_night_mode_theshold_min_max
	addiu	$4,$sp,20

	jal	set_pre_printf_state
	nop

	lw	$6,16($sp)
	lw	$5,20($sp)
	lui	$4,%hi($LC3)
	jal	tty_printf
	addiu	$4,$4,%lo($LC3)

	jal	check_post_printf_state_set_sio_params
	nop

	bne	$18,$0,$L10
	lw	$2,16($sp)

	lw	$2,20($sp)
$L10:
	sltu	$2,$16,$2
	lui	$4,%hi($LC4)
	move	$5,$16
	addiu	$4,$4,%lo($LC4)
	sb	$2,%lo(g_night_mode_p)($19)
	lui	$2,%hi(g_photo_detector_hysteresis)
	jal	tty_printf
	sb	$18,%lo(g_photo_detector_hysteresis)($2)

	jal	set_pre_printf_state
	nop

	lbu	$7,%lo(g_night_mode_p)($19)
	lui	$4,%hi($LC5)
	move	$6,$17
	move	$5,$16
	jal	tty_printf
	addiu	$4,$4,%lo($LC5)

	jal	check_post_printf_state_set_sio_params
	nop

	b	$L7
	lbu	$2,%lo(g_night_mode_p)($19)

$L8:
	jal	photo_sensor_hysteresis
	nop

	move	$18,$2
	b	$L9
	sb	$0,%lo(g_new_check_night_mode_p)($17)

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

	.comm	g_apt_aperture_menu,112,4

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,248,4

	.comm	g_wbwl_camera_setup_menu_item_array,868,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04) 9.4.0"
