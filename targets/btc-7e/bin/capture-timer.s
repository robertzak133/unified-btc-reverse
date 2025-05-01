	.file	1 "capture-timer.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	ctm_schedule_alarm_global_callback
	.set	nomips16
	.set	nomicromips
	.ent	ctm_schedule_alarm_global_callback
	.type	ctm_schedule_alarm_global_callback, @function
ctm_schedule_alarm_global_callback:
	.frame	$sp,40,$31		# vars= 0, regs= 5/0, args= 16, gp= 0
	.mask	0x800f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	li	$2,1			# 0x1
	beq	$4,$2,$L13
	nop

	addiu	$sp,$sp,-40
	sw	$19,32($sp)
	sw	$18,28($sp)
	sw	$17,24($sp)
	sw	$16,20($sp)
	sw	$31,36($sp)
	move	$16,$4
	move	$17,$5
	move	$18,$6
	jal	get_within_operating_hours_p
	move	$19,$7

	beq	$2,$0,$L12
	lw	$31,36($sp)

	jal	get_cold_item_timelapse_period
	nop

	li	$3,5			# 0x5
	beq	$2,$3,$L1
	lw	$31,36($sp)

	move	$7,$19
	move	$6,$18
	lw	$19,32($sp)
	lw	$18,28($sp)
	move	$5,$17
	move	$4,$16
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	schedule_alarm_global_callback
	addiu	$sp,$sp,40

$L1:
$L12:
	lw	$19,32($sp)
	lw	$18,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,40

$L13:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	ctm_schedule_alarm_global_callback
	.size	ctm_schedule_alarm_global_callback, .-ctm_schedule_alarm_global_callback
	.align	2
	.globl	ctm_tty_printf
	.set	nomips16
	.set	nomicromips
	.ent	ctm_tty_printf
	.type	ctm_tty_printf, @function
ctm_tty_printf:
	.frame	$sp,32,$31		# vars= 8, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$31,28($sp)
	sw	$4,20($sp)
	jal	set_pre_printf_state
	sw	$5,16($sp)

	lw	$5,16($sp)
	jal	tty_printf
	lw	$4,20($sp)

	lw	$31,28($sp)
	j	check_post_printf_state_set_sio_params
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	ctm_tty_printf
	.size	ctm_tty_printf, .-ctm_tty_printf
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"DIGIPIRSPI_SERIN_OUT_L\000"
	.align	2
$LC1:
	.ascii	"DIGIPIRSPI_SERIN_OUT_H\000"
	.align	2
$LC2:
	.ascii	"DigiPIRSpi_Write\000"
	.align	2
$LC3:
	.ascii	"%s_PIR_LOAD_DATA_TIMEOUT_:_%d_u Retry %d\012\000"
	.align	2
$LC4:
	.ascii	"DigiPIRSpi_Write Failed after %d retries\000"
	.align	2
$LC5:
	.ascii	"DigiPIRSpi_Write-e %d retries\000"
	.text
	.align	2
	.globl	ctm_DigiPIRSpi_Write
	.set	nomips16
	.set	nomicromips
	.ent	ctm_DigiPIRSpi_Write
	.type	ctm_DigiPIRSpi_Write, @function
ctm_DigiPIRSpi_Write:
	.frame	$sp,56,$31		# vars= 0, regs= 10/0, args= 16, gp= 0
	.mask	0xc0ff0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-56
	sw	$21,36($sp)
	sw	$20,32($sp)
	lui	$21,%hi($LC0)
	lui	$20,%hi($LC1)
	sw	$23,44($sp)
	sw	$18,24($sp)
	sw	$16,16($sp)
	sw	$31,52($sp)
	sw	$fp,48($sp)
	sw	$22,40($sp)
	sw	$19,28($sp)
	sw	$17,20($sp)
	move	$18,$4
	move	$16,$0
	addiu	$20,$20,%lo($LC1)
	addiu	$21,$21,%lo($LC0)
	lui	$23,%hi($LC2)
	li	$17,25			# 0x19
$L28:
	li	$22,16777216			# 0x1000000
$L21:
	jal	digi_pir_spi_serial_out
	move	$4,$0

	jal	some_sort_of_delay
	li	$4,8			# 0x8

	jal	digi_pir_spi_serial_out
	li	$4,1			# 0x1

	li	$4,8			# 0x8
	jal	some_sort_of_delay
	and	$fp,$22,$18

	jal	get_fine_grained_time
	srl	$22,$22,1

	bne	$fp,$0,$L17
	move	$19,$2

	jal	digi_pir_spi_serial_out
	move	$4,$0

	move	$5,$21
$L18:
	jal	log_printf
	li	$4,4			# 0x4

	jal	some_sort_of_delay
	li	$4,96			# 0x60

	jal	get_fine_grained_time
	addiu	$17,$17,-1

	move	$4,$2
	jal	positive_diff
	move	$5,$19

	move	$19,$2
	sltu	$2,$2,301
	bne	$2,$0,$L19
	nop

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC3)
	move	$7,$16
	move	$6,$19
	addiu	$5,$23,%lo($LC2)
	jal	tty_printf
	addiu	$4,$4,%lo($LC3)

	jal	check_post_printf_state_set_sio_params
	addiu	$16,$16,1

$L20:
	jal	digi_pir_spi_serial_out
	move	$4,$0

	jal	some_sort_of_delay
	li	$4,560			# 0x230

	slt	$2,$16,3
	bne	$2,$0,$L22
	nop

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC4)
	move	$5,$16
	addiu	$4,$4,%lo($LC4)
	jal	tty_printf
	slt	$16,$16,1001

	jal	check_post_printf_state_set_sio_params
	nop

	bne	$16,$0,$L16
	lw	$31,52($sp)

	lw	$fp,48($sp)
	lw	$23,44($sp)
	lw	$22,40($sp)
	lw	$21,36($sp)
	lw	$20,32($sp)
	lw	$19,28($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	move	$4,$18
	lw	$18,24($sp)
	j	DigiPIRSpi_Write
	addiu	$sp,$sp,56

$L17:
	jal	digi_pir_spi_serial_out
	li	$4,1			# 0x1

	b	$L18
	move	$5,$20

$L19:
	bne	$17,$0,$L21
	nop

	b	$L20
	nop

$L22:
	bne	$17,$0,$L28
	li	$17,25			# 0x19

	lw	$31,52($sp)
	lw	$fp,48($sp)
	lw	$23,44($sp)
	lw	$22,40($sp)
	lw	$21,36($sp)
	lw	$20,32($sp)
	lw	$19,28($sp)
	lw	$18,24($sp)
	lw	$17,20($sp)
	move	$6,$16
	lw	$16,16($sp)
	lui	$5,%hi($LC5)
	addiu	$5,$5,%lo($LC5)
	li	$4,4			# 0x4
	j	log_printf
	addiu	$sp,$sp,56

$L16:
	lw	$fp,48($sp)
	lw	$23,44($sp)
	lw	$22,40($sp)
	lw	$21,36($sp)
	lw	$20,32($sp)
	lw	$19,28($sp)
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,56

	.set	macro
	.set	reorder
	.end	ctm_DigiPIRSpi_Write
	.size	ctm_DigiPIRSpi_Write, .-ctm_DigiPIRSpi_Write

	.comm	g_rtc_time_format_menu,84,4

	.comm	g_rtc_date_format_menu,140,4

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,240,4

	.comm	g_wbwl_camera_setup_menu_item_array,840,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
