	.file	1 "timelapse.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
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
	beq	$2,$0,$L13
	li	$4,12			# 0xc

	jal	get_power_switch_on_p
	nop

	bne	$2,$0,$L7
	lui	$5,%hi($LC0)

	li	$4,12			# 0xc
$L13:
	lw	$31,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	j	set_fsm_state_absolute
	addiu	$sp,$sp,32

$L7:
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
	beq	$6,$0,$L8
	move	$17,$3

	beq	$4,$0,$L8
	nop

	addu	$5,$5,$16
	subu	$5,$5,$2
	jal	thread_sleep
	li	$4,3			# 0x3

$L8:
	jal	get_current_operating_time_ms
	nop

	jal	tlps_update_system_measurements
	sw	$2,%lo(g_last_timelapse_time_in_ms)($17)

	b	$L13
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
	.word	TaskTimeLapseFSM_task4
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
	.word	32
	.word	12
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	194
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	13
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	14
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	15
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	16
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	17
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	18
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	19
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	20
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	21
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	22
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	32
	.word	59
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
