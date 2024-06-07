	.file	1 "timelapse.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	tlps_TaskTimeLapseFSM_task6
	.set	nomips16
	.set	nomicromips
	.ent	tlps_TaskTimeLapseFSM_task6
	.type	tlps_TaskTimeLapseFSM_task6, @function
tlps_TaskTimeLapseFSM_task6:
	.frame	$sp,64,$31		# vars= 24, regs= 2/0, args= 32, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+51)
	lbu	$2,%lo(g_ColdItemData+51)($2)
	addiu	$sp,$sp,-64
	sw	$31,60($sp)
	bne	$2,$0,$L2
	sw	$16,56($sp)

	jal	TaskTimeLapseFSM_task6
	nop

	lw	$31,60($sp)
$L5:
	lw	$16,56($sp)
	jr	$31
	addiu	$sp,$sp,64

$L2:
	jal	get_photo_size_factor
	move	$4,$0

	jal	get_cold_item_photo_resolution
	move	$16,$2

	lui	$4,%hi(still_low_battery_display_function)
	addiu	$4,$4,%lo(still_low_battery_display_function)
	jal	register_low_battery_display_function
	sw	$2,48($sp)

	lw	$5,48($sp)
	jal	set_camera_photo_resolution
	addiu	$4,$sp,32

	li	$2,1			# 0x1
	sw	$2,24($sp)
	lw	$2,44($sp)
	lw	$7,36($sp)
	lw	$6,32($sp)
	sw	$2,20($sp)
	lw	$2,40($sp)
	move	$5,$16
	li	$4,1			# 0x1
	jal	startHceTaskStill_FSM
	sw	$2,16($sp)

	jal	set_fsm_state_relative
	li	$4,1			# 0x1

	b	$L5
	lw	$31,60($sp)

	.set	macro
	.set	reorder
	.end	tlps_TaskTimeLapseFSM_task6
	.size	tlps_TaskTimeLapseFSM_task6, .-tlps_TaskTimeLapseFSM_task6
	.align	2
	.globl	tlps_TaskTimeLapseFSM_task7
	.set	nomips16
	.set	nomicromips
	.ent	tlps_TaskTimeLapseFSM_task7
	.type	tlps_TaskTimeLapseFSM_task7, @function
tlps_TaskTimeLapseFSM_task7:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+51)
	lbu	$2,%lo(g_ColdItemData+51)($2)
	bne	$2,$0,$L7
	nop

	j	TaskTimeLapseFSM_task7
	nop

$L7:
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	HceTaskStillFSM_valid_p
	nop

	bne	$2,$0,$L6
	lw	$31,20($sp)

	li	$4,13			# 0xd
	j	set_fsm_state_absolute
	addiu	$sp,$sp,24

$L6:
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	tlps_TaskTimeLapseFSM_task7
	.size	tlps_TaskTimeLapseFSM_task7, .-tlps_TaskTimeLapseFSM_task7
	.align	2
	.globl	tlps_get_cold_item_raw_timelapse_period
	.set	nomips16
	.set	nomicromips
	.ent	tlps_get_cold_item_raw_timelapse_period
	.type	tlps_get_cold_item_raw_timelapse_period, @function
tlps_get_cold_item_raw_timelapse_period:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+144)
	jr	$31
	lw	$2,%lo(g_ColdItemData+144)($2)

	.set	macro
	.set	reorder
	.end	tlps_get_cold_item_raw_timelapse_period
	.size	tlps_get_cold_item_raw_timelapse_period, .-tlps_get_cold_item_raw_timelapse_period
	.align	2
	.globl	tlps_get_cold_item_cooked_timelapse_period
	.set	nomips16
	.set	nomicromips
	.ent	tlps_get_cold_item_cooked_timelapse_period
	.type	tlps_get_cold_item_cooked_timelapse_period, @function
tlps_get_cold_item_cooked_timelapse_period:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+144)
	lw	$2,%lo(g_ColdItemData+144)($2)
	li	$3,5			# 0x5
	beql	$2,$3,$L14
	move	$2,$0

$L14:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	tlps_get_cold_item_cooked_timelapse_period
	.size	tlps_get_cold_item_cooked_timelapse_period, .-tlps_get_cold_item_cooked_timelapse_period
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"tlps_get_tod_in_timelapse_region: at %02d:%02d:%02d retu"
	.ascii	"rning: %d\012\000"
	.text
	.align	2
	.globl	tlps_get_tod_in_timelapse_region
	.set	nomips16
	.set	nomicromips
	.ent	tlps_get_tod_in_timelapse_region
	.type	tlps_get_tod_in_timelapse_region, @function
tlps_get_tod_in_timelapse_region:
	.frame	$sp,40,$31		# vars= 0, regs= 3/0, args= 24, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+144)
	lw	$3,%lo(g_ColdItemData+144)($2)
	addiu	$sp,$sp,-40
	li	$2,5			# 0x5
	sw	$17,32($sp)
	sw	$16,28($sp)
	sw	$31,36($sp)
	move	$17,$4
	beq	$3,$2,$L16
	li	$16,1			# 0x1

	jal	get_tod_in_timelapse_region
	nop

	move	$16,$2
$L16:
	jal	set_pre_printf_state
	nop

	lh	$7,10($17)
	lh	$6,8($17)
	lh	$5,6($17)
	lui	$4,%hi($LC0)
	sw	$16,16($sp)
	jal	tty_printf
	addiu	$4,$4,%lo($LC0)

	jal	check_post_printf_state_set_sio_params
	nop

	lw	$31,36($sp)
	lw	$17,32($sp)
	move	$2,$16
	lw	$16,28($sp)
	jr	$31
	addiu	$sp,$sp,40

	.set	macro
	.set	reorder
	.end	tlps_get_tod_in_timelapse_region
	.size	tlps_get_tod_in_timelapse_region, .-tlps_get_tod_in_timelapse_region
	.align	2
	.globl	tlps_TaskTimeLapseFSM_task4
	.set	nomips16
	.set	nomicromips
	.ent	tlps_TaskTimeLapseFSM_task4
	.type	tlps_TaskTimeLapseFSM_task4, @function
tlps_TaskTimeLapseFSM_task4:
	.frame	$sp,88,$31		# vars= 32, regs= 10/0, args= 16, gp= 0
	.mask	0xc0ff0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-88
	sw	$31,84($sp)
	sw	$fp,80($sp)
	sw	$22,72($sp)
	sw	$21,68($sp)
	sw	$23,76($sp)
	sw	$20,64($sp)
	sw	$19,60($sp)
	sw	$18,56($sp)
	sw	$17,52($sp)
	jal	getCameraConfigStructPtr
	sw	$16,48($sp)

	addiu	$4,$sp,16
	jal	get_current_date_time_short
	lbu	$22,39($2)

	jal	tlps_get_tod_in_timelapse_region
	addiu	$4,$sp,16

	addiu	$5,$sp,32
	addiu	$4,$sp,28
	jal	update_timelapse_sunrise
	move	$fp,$2

	addiu	$5,$sp,40
	jal	update_timelapse_sunset
	addiu	$4,$sp,36

	lw	$2,28($sp)
	li	$3,65536			# 0x10000
	sll	$21,$2,4
	subu	$21,$21,$2
	sll	$21,$21,2
	addiu	$2,$3,20865
	sltu	$2,$21,$2
	beql	$2,$0,$L21
	addiu	$21,$3,20863

$L21:
	lw	$2,32($sp)
	li	$3,65536			# 0x10000
	sll	$19,$2,4
	subu	$19,$19,$2
	sll	$19,$19,2
	addiu	$2,$3,20865
	sltu	$2,$19,$2
	beql	$2,$0,$L22
	addiu	$19,$3,20863

$L22:
	lw	$16,36($sp)
	li	$3,65536			# 0x10000
	addiu	$2,$3,20865
	sll	$20,$16,4
	subu	$20,$20,$16
	sll	$20,$20,2
	sltu	$2,$20,$2
	beql	$2,$0,$L23
	addiu	$20,$3,20863

$L23:
	lw	$2,40($sp)
	li	$3,65536			# 0x10000
	sll	$18,$2,4
	subu	$18,$18,$2
	sll	$18,$18,2
	addiu	$2,$3,20865
	sltu	$2,$18,$2
	beql	$2,$0,$L24
	addiu	$18,$3,20863

$L24:
	lhu	$2,24($sp)
	li	$3,3600			# 0xe10
	sll	$16,$2,4
	subu	$16,$16,$2
	lhu	$2,22($sp)
	sll	$16,$16,2
	mult	$2,$3
	mflo	$2
	li	$3,65536			# 0x10000
	addu	$16,$16,$2
	lhu	$2,26($sp)
	addu	$16,$16,$2
	addiu	$2,$3,20865
	sltu	$2,$16,$2
	beql	$2,$0,$L25
	addiu	$16,$3,20863

$L25:
	jal	get_cold_item_timelapse_frequency
	nop

	jal	encoded_timelapse_frequency_to_seconds
	move	$4,$2

	jal	get_cold_item_tod_last_photo_in_seconds
	move	$17,$2

	move	$23,$2
	sltu	$2,$16,$17
	beq	$2,$0,$L47
	li	$2,1			# 0x1

	li	$2,65536			# 0x10000
	addiu	$2,$2,20864
	addu	$16,$16,$2
	li	$2,1			# 0x1
$L47:
	bne	$22,$2,$L27
	nop

	addu	$2,$17,$23
	sltu	$3,$2,$16
	bne	$3,$0,$L48
	addiu	$17,$2,-2

	subu	$3,$2,$16
	sltu	$3,$3,11
	beq	$3,$0,$L29
	nop

$L48:
	sltu	$16,$16,$17
$L30:
	beq	$16,$0,$L29
	nop

	b	$L37
	nop

$L27:
	bne	$fp,$2,$L31
	li	$2,-3			# 0xfffffffffffffffd

	jal	get_cold_item_timelapse_period
	nop

	beq	$2,$0,$L49
	addu	$3,$17,$23

	sltu	$2,$16,$19
	bne	$2,$0,$L34
	subu	$2,$20,$16

	subu	$19,$16,$19
	sltu	$19,$19,121
	bne	$19,$0,$L29
	nop

$L34:
	sltu	$16,$20,$16
	beq	$16,$0,$L35
	sltu	$2,$2,3

$L37:
	jal	set_fsm_state_absolute
	li	$4,12			# 0xc

	lw	$31,84($sp)
$L46:
	lw	$fp,80($sp)
	lw	$23,76($sp)
	lw	$22,72($sp)
	lw	$21,68($sp)
	lw	$20,64($sp)
	lw	$19,60($sp)
	lw	$18,56($sp)
	lw	$17,52($sp)
	lw	$16,48($sp)
	jr	$31
	addiu	$sp,$sp,88

$L35:
	beq	$2,$0,$L37
	nop

$L29:
	jal	set_fsm_state_relative
	li	$4,1			# 0x1

	b	$L46
	lw	$31,84($sp)

$L31:
	and	$2,$fp,$2
	beq	$2,$0,$L32
	addu	$3,$17,$23

	li	$2,3			# 0x3
	bne	$fp,$2,$L37
	sltu	$2,$16,$18

	bne	$2,$0,$L50
	subu	$2,$21,$16

	subu	$18,$16,$18
	sltu	$18,$18,121
	bne	$18,$0,$L29
	nop

$L50:
	b	$L34
	move	$20,$21

$L32:
$L49:
	addiu	$3,$3,-1
	sltu	$3,$16,$3
	beq	$3,$0,$L29
	sltu	$16,$23,$16

	b	$L30
	nop

	.set	macro
	.set	reorder
	.end	tlps_TaskTimeLapseFSM_task4
	.size	tlps_TaskTimeLapseFSM_task4, .-tlps_TaskTimeLapseFSM_task4
	.section	.rodata.str1.4
	.align	2
$LC1:
	.ascii	"tlps_get_next_wake_time: at %02d:%02d:%02d in region %d;"
	.ascii	" tod_last_photo: %d; returning: %d\012\000"
	.text
	.align	2
	.globl	tlps_get_next_wake_time
	.set	nomips16
	.set	nomicromips
	.ent	tlps_get_next_wake_time
	.type	tlps_get_next_wake_time, @function
tlps_get_next_wake_time:
	.frame	$sp,56,$31		# vars= 0, regs= 5/0, args= 32, gp= 0
	.mask	0x800f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-56
	sw	$18,44($sp)
	sw	$16,36($sp)
	move	$18,$5
	move	$16,$4
	sw	$31,52($sp)
	sw	$19,48($sp)
	jal	get_cold_item_tod_last_photo_in_seconds
	sw	$17,40($sp)

	move	$5,$18
	move	$4,$16
	jal	get_next_wake_time
	move	$19,$2

	jal	set_pre_printf_state
	move	$17,$2

	lh	$7,10($16)
	lh	$6,8($16)
	lh	$5,6($16)
	lui	$4,%hi($LC1)
	sw	$17,24($sp)
	sw	$19,20($sp)
	sw	$18,16($sp)
	jal	tty_printf
	addiu	$4,$4,%lo($LC1)

	jal	check_post_printf_state_set_sio_params
	nop

	lw	$31,52($sp)
	lw	$19,48($sp)
	lw	$18,44($sp)
	lw	$16,36($sp)
	move	$2,$17
	lw	$17,40($sp)
	jr	$31
	addiu	$sp,$sp,56

	.set	macro
	.set	reorder
	.end	tlps_get_next_wake_time
	.size	tlps_get_next_wake_time, .-tlps_get_next_wake_time
	.align	2
	.globl	tlps_encoded_timelapse_frequency_to_seconds
	.set	nomips16
	.set	nomicromips
	.ent	tlps_encoded_timelapse_frequency_to_seconds
	.type	tlps_encoded_timelapse_frequency_to_seconds, @function
tlps_encoded_timelapse_frequency_to_seconds:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_wbwl_timelapse_frequency_lookup_table)
	addiu	$2,$2,%lo(g_wbwl_timelapse_frequency_lookup_table)
	sll	$4,$4,1
	addu	$4,$4,$2
	jr	$31
	lh	$2,0($4)

	.set	macro
	.set	reorder
	.end	tlps_encoded_timelapse_frequency_to_seconds
	.size	tlps_encoded_timelapse_frequency_to_seconds, .-tlps_encoded_timelapse_frequency_to_seconds
	.align	2
	.globl	tlps_execute_if_not_null
	.set	nomips16
	.set	nomicromips
	.ent	tlps_execute_if_not_null
	.type	tlps_execute_if_not_null, @function
tlps_execute_if_not_null:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_wbwl_TaskTimeLapseFSM_function_array)
	sll	$4,$4,2
	addiu	$2,$2,%lo(g_wbwl_TaskTimeLapseFSM_function_array)
	addu	$4,$4,$2
	j	execute_if_not_null
	lw	$4,0($4)

	.set	macro
	.set	reorder
	.end	tlps_execute_if_not_null
	.size	tlps_execute_if_not_null, .-tlps_execute_if_not_null
	.align	2
	.globl	tlps_TaskTImeLapseFSM_task6
	.set	nomips16
	.set	nomicromips
	.ent	tlps_TaskTImeLapseFSM_task6
	.type	tlps_TaskTImeLapseFSM_task6, @function
tlps_TaskTImeLapseFSM_task6:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	tlps_TaskTImeLapseFSM_task6
	.size	tlps_TaskTImeLapseFSM_task6, .-tlps_TaskTImeLapseFSM_task6
	.align	2
	.globl	tlps_update_system_measurements
	.set	nomips16
	.set	nomicromips
	.ent	tlps_update_system_measurements
	.type	tlps_update_system_measurements, @function
tlps_update_system_measurements:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	sw	$31,20($sp)
	jal	Volt_Calib_Bat
	nop

	jal	update_global_pressure_temperature
	nop

	jal	store_pressure_trend
	nop

	lw	$31,20($sp)
	j	update_timelapse_rise_set_times
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	tlps_update_system_measurements
	.size	tlps_update_system_measurements, .-tlps_update_system_measurements
	.section	.rodata.str1.4
	.align	2
$LC2:
	.ascii	"HceTaskTimeLapse_End\000"
	.text
	.align	2
	.globl	tlps_TaskTimeLapseFSM_task12a
	.set	nomips16
	.set	nomicromips
	.ent	tlps_TaskTimeLapseFSM_task12a
	.type	tlps_TaskTimeLapseFSM_task12a, @function
tlps_TaskTimeLapseFSM_task12a:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$31,28($sp)
	sw	$16,20($sp)
	jal	get_cold_item_timelapse_frequency
	sw	$17,24($sp)

	jal	encoded_timelapse_frequency_to_seconds
	move	$4,$2

	move	$16,$2
	sltu	$2,$2,4
	beq	$2,$0,$L66
	li	$4,12			# 0xc

	jal	get_power_switch_on_p
	nop

	bne	$2,$0,$L60
	lui	$5,%hi($LC2)

	li	$4,12			# 0xc
$L66:
	lw	$31,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L60:
	addiu	$5,$5,%lo($LC2)
	jal	HceCommon_SetCaptureImag
	move	$4,$0

	jal	get_current_operating_time_ms
	nop

	li	$6,1000			# 0x3e8
	mult	$16,$6
	mflo	$16
	lui	$3,%hi(g_last_timelapse_time_in_ms)
	lw	$5,%lo(g_last_timelapse_time_in_ms)($3)
	subu	$4,$2,$5
	sltu	$6,$4,$16
	beq	$6,$0,$L61
	move	$17,$3

	beq	$4,$0,$L61
	nop

	addu	$5,$5,$16
	subu	$5,$5,$2
	jal	thread_sleep
	li	$4,3			# 0x3

$L61:
	jal	get_current_operating_time_ms
	nop

	jal	tlps_update_system_measurements
	sw	$2,%lo(g_last_timelapse_time_in_ms)($17)

	b	$L66
	li	$4,1			# 0x1

	.set	macro
	.set	reorder
	.end	tlps_TaskTimeLapseFSM_task12a
	.size	tlps_TaskTimeLapseFSM_task12a, .-tlps_TaskTimeLapseFSM_task12a
	.align	2
	.globl	tlps_Pressure_sensor_getReading
	.set	nomips16
	.set	nomicromips
	.ent	tlps_Pressure_sensor_getReading
	.type	tlps_Pressure_sensor_getReading, @function
tlps_Pressure_sensor_getReading:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	j	Pressure_sensor_getReading
	nop

	.set	macro
	.set	reorder
	.end	tlps_Pressure_sensor_getReading
	.size	tlps_Pressure_sensor_getReading, .-tlps_Pressure_sensor_getReading
	.align	2
	.globl	tlps_get_cold_item_file_type
	.set	nomips16
	.set	nomicromips
	.ent	tlps_get_cold_item_file_type
	.type	tlps_get_cold_item_file_type, @function
tlps_get_cold_item_file_type:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+51)
	jr	$31
	lbu	$2,%lo(g_ColdItemData+51)($2)

	.set	macro
	.set	reorder
	.end	tlps_get_cold_item_file_type
	.size	tlps_get_cold_item_file_type, .-tlps_get_cold_item_file_type
	.align	2
	.globl	tlps_set_cold_item_file_type
	.set	nomips16
	.set	nomicromips
	.ent	tlps_set_cold_item_file_type
	.type	tlps_set_cold_item_file_type, @function
tlps_set_cold_item_file_type:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+51)
	jr	$31
	sb	$4,%lo(g_ColdItemData+51)($2)

	.set	macro
	.set	reorder
	.end	tlps_set_cold_item_file_type
	.size	tlps_set_cold_item_file_type, .-tlps_set_cold_item_file_type
	.align	2
	.globl	tlps_handle_file_type_menu
	.set	nomips16
	.set	nomicromips
	.ent	tlps_handle_file_type_menu
	.type	tlps_handle_file_type_menu, @function
tlps_handle_file_type_menu:
	.frame	$sp,32,$31		# vars= 0, regs= 4/0, args= 16, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$17,20($sp)
	sw	$16,16($sp)
	sw	$31,28($sp)
	jal	getCameraConfigStructPtr
	sw	$18,24($sp)

	lbu	$17,0($2)
	beq	$17,$0,$L71
	move	$16,$2

	sb	$0,0($2)
	lui	$2,%hi(g_ColdItemData+51)
	lbu	$2,%lo(g_ColdItemData+51)($2)
	addiu	$4,$16,2
	lui	$5,%hi(g_menu_root)
	sb	$2,2($16)
	lw	$31,28($sp)
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	addiu	$5,$5,%lo(g_menu_root)
	j	menu_draw_selected_item
	addiu	$sp,$sp,32

$L71:
	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L72
	lui	$2,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L84
	lui	$18,%hi(g_menu_root)

$L72:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L74
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L73
	lui	$18,%hi(g_menu_root)

$L74:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$3,1			# 0x1
	beq	$2,$3,$L75
	lui	$2,%hi(g_left_button_enable)

$L76:
	jal	ui_cursor_key_pressed_p
	li	$4,3			# 0x3

	li	$3,1			# 0x1
	bne	$2,$3,$L78
	lui	$2,%hi(g_right_button_enable)

	lbu	$3,%lo(g_right_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L85
	lw	$31,28($sp)

$L78:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L80
	lui	$2,%hi(g_enter_button_enable)

	lbu	$3,%lo(g_enter_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L80
	lui	$3,%hi(g_wbwl_camera_setup_selector_array)

	lbu	$4,2($16)
	addiu	$3,$3,%lo(g_wbwl_camera_setup_selector_array)
	sll	$2,$4,3
	sb	$17,0($16)
	addu	$3,$3,$2
	lw	$6,4($3)
	lw	$5,0($3)
	lui	$7,%hi(g_menu_root)
	jal	get_next_state_from_menu_enter
	addiu	$7,$7,%lo(g_menu_root)

	move	$4,$2
	li	$2,255			# 0xff
	beq	$4,$2,$L70
	lui	$2,%hi(g_ColdItemData+51)

	lbu	$3,2($16)
	sb	$3,%lo(g_ColdItemData+51)($2)
	sb	$17,4($16)
$L81:
	lw	$31,28($sp)
$L83:
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L73:
$L84:
	addiu	$5,$16,2
	move	$4,$17
	addiu	$7,$18,%lo(g_menu_root)
	jal	menu_get_next_menu_selection
	li	$6,1			# 0x1

	lbu	$4,2($16)
	lw	$31,28($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	addiu	$5,$18,%lo(g_menu_root)
	lw	$18,24($sp)
	j	menu_redraw_items
	addiu	$sp,$sp,32

$L75:
	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L76
	nop

$L70:
	lw	$31,28($sp)
$L85:
	lw	$18,24($sp)
$L86:
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,32

$L80:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L85
	lw	$31,28($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L86
	lw	$18,24($sp)

	lui	$5,%hi(g_menu_root)
	li	$4,1			# 0x1
	sb	$2,0($16)
	jal	get_next_state_from_menu_mode
	addiu	$5,$5,%lo(g_menu_root)

	move	$4,$2
	li	$2,255			# 0xff
	beql	$4,$2,$L81
	li	$4,36			# 0x24

	b	$L83
	lw	$31,28($sp)

	.set	macro
	.set	reorder
	.end	tlps_handle_file_type_menu
	.size	tlps_handle_file_type_menu, .-tlps_handle_file_type_menu
	.align	2
	.globl	tlps_HceIRCut_SetIRCutClosed
	.set	nomips16
	.set	nomicromips
	.ent	tlps_HceIRCut_SetIRCutClosed
	.type	tlps_HceIRCut_SetIRCutClosed, @function
tlps_HceIRCut_SetIRCutClosed:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$2,%hi(g_ColdItemData+51)
	lbu	$2,%lo(g_ColdItemData+51)($2)
	bne	$2,$0,$L89
	nop

	j	HceIRCut_SetIRCutClosed
	nop

$L89:
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	tlps_HceIRCut_SetIRCutClosed
	.size	tlps_HceIRCut_SetIRCutClosed, .-tlps_HceIRCut_SetIRCutClosed
	.align	2
	.globl	tls_HceTaskBoot2Cap_Task0
	.set	nomips16
	.set	nomicromips
	.ent	tls_HceTaskBoot2Cap_Task0
	.type	tls_HceTaskBoot2Cap_Task0, @function
tls_HceTaskBoot2Cap_Task0:
	.frame	$sp,48,$31		# vars= 16, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-48
	sw	$31,44($sp)
	sw	$16,36($sp)
	jal	spawnIRCutFSM_per_mode
	sw	$17,40($sp)

	jal	checkForSDCard
	nop

	jal	get_within_operating_hours_p
	move	$16,$2

	beq	$16,$0,$L99
	li	$4,7			# 0x7

	bne	$2,$0,$L92
	nop

$L99:
	jal	set_fsm_state_absolute
	nop

	lw	$31,44($sp)
	lw	$17,40($sp)
	lw	$16,36($sp)
	jr	$31
	addiu	$sp,$sp,48

$L92:
	jal	get_current_date_time_short
	addiu	$4,$sp,16

	jal	set_exif_time_of_capture
	addiu	$4,$sp,16

	jal	get_cold_item_operation_mode
	nop

	beq	$2,$0,$L94
	li	$4,1			# 0x1

	li	$3,1			# 0x1
	beq	$2,$3,$L94
	li	$4,3			# 0x3

	lh	$2,24($sp)
	li	$3,3600			# 0xe10
	li	$17,65536			# 0x10000
	sll	$16,$2,4
	subu	$16,$16,$2
	lh	$2,22($sp)
	sll	$16,$16,2
	mult	$2,$3
	mflo	$2
	addu	$16,$16,$2
	lh	$2,26($sp)
	addu	$16,$16,$2
	ori	$2,$17,0x86a0
	sltu	$2,$16,$2
	bne	$2,$0,$L95
	addiu	$2,$17,20865

	jal	HceTaskBoot2Cap_Task0
	nop

	b	$L96
	addiu	$16,$17,20863

$L95:
	sltu	$2,$16,$2
	beql	$2,$0,$L112
	addiu	$16,$17,20863

$L96:
$L112:
	jal	tlps_get_tod_in_timelapse_region
	addiu	$4,$sp,16

	jal	get_cold_item_timelapse_period
	move	$17,$2

	li	$3,1			# 0x1
	beq	$17,$3,$L97
	nop

	li	$2,-3			# 0xfffffffffffffffd
	and	$17,$17,$2
	bne	$17,$0,$L109
	li	$4,5			# 0x5

$L94:
	lui	$2,%hi(g_ColdItemData+51)
	lbu	$3,%lo(g_ColdItemData+51)($2)
	li	$2,1			# 0x1
	bne	$3,$2,$L99
	li	$2,5			# 0x5

	beql	$4,$2,$L99
	li	$4,1			# 0x1

	b	$L99
	nop

$L97:
	beq	$2,$0,$L94
	li	$4,5			# 0x5

$L109:
	jal	set_cold_item_current_tod_in_seconds
	move	$4,$16

	b	$L94
	li	$4,1			# 0x1

	.set	macro
	.set	reorder
	.end	tls_HceTaskBoot2Cap_Task0
	.size	tls_HceTaskBoot2Cap_Task0, .-tls_HceTaskBoot2Cap_Task0
	.globl	g_wbwl_TaskTimeLapseFSM_function_array
	.data
	.align	2
	.type	g_wbwl_TaskTimeLapseFSM_function_array, @object
	.size	g_wbwl_TaskTimeLapseFSM_function_array, 64
g_wbwl_TaskTimeLapseFSM_function_array:
	.word	TaskTimeLapseFSM_task0
	.word	TaskTimeLapseFSM_task1
	.word	TaskTimeLapseFSM_task2
	.word	TaskTimeLapseFSM_task3_ae_set
	.word	tlps_TaskTimeLapseFSM_task4
	.word	TaskTimeLapseFSM_task5
	.word	tlps_TaskTimeLapseFSM_task6
	.word	tlps_TaskTimeLapseFSM_task7
	.word	TaskTimeLapseFSM_task8_CopyJPGFromRAM
	.word	TaskTimeLapseFSM_task9
	.word	TaskTimeLapseFSM_task10_WaitMountSD
	.word	TaskTimeLapseFSM_task11_openTLfile
	.word	TaskTimeLapseFSM_task12
	.word	tlps_TaskTimeLapseFSM_task12a
	.word	TaskTimeLapseFSM_task13
	.word	TaskTimeLapseFSM_task14_end
	.globl	g_wbwl_timelapse_frequency_lookup_table
	.align	2
	.type	g_wbwl_timelapse_frequency_lookup_table, @object
	.size	g_wbwl_timelapse_frequency_lookup_table, 24
g_wbwl_timelapse_frequency_lookup_table:
	.half	1
	.half	2
	.half	5
	.half	10
	.half	20
	.half	30
	.half	60
	.half	120
	.half	300
	.half	600
	.half	1800
	.half	3600
	.globl	g_tlps_file_type_menu
	.align	2
	.type	g_tlps_file_type_menu, @object
	.size	g_tlps_file_type_menu, 84
g_tlps_file_type_menu:
	.word	31
	.word	195
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	196
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	194
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3
	.globl	g_wbwl_timelapse_frequency_menu
	.align	2
	.type	g_wbwl_timelapse_frequency_menu, @object
	.size	g_wbwl_timelapse_frequency_menu, 364
g_wbwl_timelapse_frequency_menu:
	.word	31
	.word	12
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	188
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	13
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	14
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	15
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	16
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	17
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	18
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	19
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	20
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	21
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	22
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	58
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3

	.comm	g_wbwl_menu_handler_function_array_extensions,28,4

	.comm	g_wbwl_camera_setup_selector_array,248,4

	.comm	g_wbwl_camera_setup_menu_item_array,868,4
	.globl	g_wbwl_timelapse_period_menu
	.align	2
	.type	g_wbwl_timelapse_period_menu, @object
	.size	g_wbwl_timelapse_period_menu, 196
g_wbwl_timelapse_period_menu:
	.word	31
	.word	27
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	23
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	24
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	25
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	26
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	189
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	59
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
