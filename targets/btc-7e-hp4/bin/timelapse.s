	.file	1 "timelapse.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
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

	jal	get_tod_in_timelapse_region
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
	beql	$2,$0,$L2
	addiu	$21,$3,20863

$L2:
	lw	$2,32($sp)
	li	$3,65536			# 0x10000
	sll	$19,$2,4
	subu	$19,$19,$2
	sll	$19,$19,2
	addiu	$2,$3,20865
	sltu	$2,$19,$2
	beql	$2,$0,$L3
	addiu	$19,$3,20863

$L3:
	lw	$16,36($sp)
	li	$3,65536			# 0x10000
	addiu	$2,$3,20865
	sll	$20,$16,4
	subu	$20,$20,$16
	sll	$20,$20,2
	sltu	$2,$20,$2
	beql	$2,$0,$L4
	addiu	$20,$3,20863

$L4:
	lw	$2,40($sp)
	li	$3,65536			# 0x10000
	sll	$18,$2,4
	subu	$18,$18,$2
	sll	$18,$18,2
	addiu	$2,$3,20865
	sltu	$2,$18,$2
	beql	$2,$0,$L5
	addiu	$18,$3,20863

$L5:
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
	beql	$2,$0,$L6
	addiu	$16,$3,20863

$L6:
	jal	get_cold_item_timelapse_frequency
	nop

	jal	encoded_timelapse_frequency_to_seconds
	move	$4,$2

	jal	get_cold_item_tod_last_photo_in_seconds
	move	$17,$2

	move	$23,$2
	sltu	$2,$16,$17
	beq	$2,$0,$L28
	li	$2,1			# 0x1

	li	$2,65536			# 0x10000
	addiu	$2,$2,20864
	addu	$16,$16,$2
	li	$2,1			# 0x1
$L28:
	bne	$22,$2,$L8
	nop

	addu	$2,$17,$23
	sltu	$3,$2,$16
	bne	$3,$0,$L29
	addiu	$17,$2,-2

	subu	$3,$2,$16
	sltu	$3,$3,11
	beq	$3,$0,$L10
	nop

$L29:
	sltu	$16,$16,$17
$L11:
	beq	$16,$0,$L10
	nop

	b	$L18
	nop

$L8:
	bne	$fp,$2,$L12
	li	$2,-3			# 0xfffffffffffffffd

	jal	get_cold_item_timelapse_period
	nop

	beq	$2,$0,$L30
	addu	$3,$17,$23

	sltu	$2,$16,$19
	bne	$2,$0,$L15
	subu	$2,$20,$16

	subu	$19,$16,$19
	sltu	$19,$19,121
	bne	$19,$0,$L10
	nop

$L15:
	sltu	$16,$20,$16
	beq	$16,$0,$L16
	sltu	$2,$2,3

$L18:
	jal	set_fsm_state_absolute
	li	$4,12			# 0xc

	lw	$31,84($sp)
$L27:
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

$L16:
	beq	$2,$0,$L18
	nop

$L10:
	jal	set_fsm_state_relative
	li	$4,1			# 0x1

	b	$L27
	lw	$31,84($sp)

$L12:
	and	$2,$fp,$2
	beq	$2,$0,$L13
	addu	$3,$17,$23

	li	$2,3			# 0x3
	bne	$fp,$2,$L18
	sltu	$2,$16,$18

	bne	$2,$0,$L31
	subu	$2,$21,$16

	subu	$18,$16,$18
	sltu	$18,$18,121
	bne	$18,$0,$L10
	nop

$L31:
	b	$L15
	move	$20,$21

$L13:
$L30:
	addiu	$3,$3,-1
	sltu	$3,$16,$3
	beq	$3,$0,$L10
	sltu	$16,$23,$16

	b	$L11
	nop

	.set	macro
	.set	reorder
	.end	tlps_TaskTimeLapseFSM_task4
	.size	tlps_TaskTimeLapseFSM_task4, .-tlps_TaskTimeLapseFSM_task4
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

	jal	temperature_sensor_getReading
	nop

	jal	set_g_temperature_forc
	move	$4,$2

	lw	$31,20($sp)
	j	update_timelapse_rise_set_times
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	tlps_update_system_measurements
	.size	tlps_update_system_measurements, .-tlps_update_system_measurements
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
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
	beq	$2,$0,$L44
	li	$4,12			# 0xc

	jal	get_power_switch_on_p
	nop

	bne	$2,$0,$L38
	lui	$5,%hi($LC0)

	li	$4,12			# 0xc
$L44:
	lw	$31,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L38:
	addiu	$5,$5,%lo($LC0)
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
	beq	$6,$0,$L39
	move	$17,$3

	beq	$4,$0,$L39
	nop

	addu	$5,$5,$16
	subu	$5,$5,$2
	jal	thread_sleep
	li	$4,3			# 0x3

$L39:
	jal	get_current_operating_time_ms
	nop

	jal	tlps_update_system_measurements
	sw	$2,%lo(g_last_timelapse_time_in_ms)($17)

	b	$L44
	li	$4,1			# 0x1

	.set	macro
	.set	reorder
	.end	tlps_TaskTimeLapseFSM_task12a
	.size	tlps_TaskTimeLapseFSM_task12a, .-tlps_TaskTimeLapseFSM_task12a
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
	.word	TaskTimeLapseFSM_task6
	.word	TaskTimeLapseFSM_task7
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
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
