	.file	1 "capture-timer.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	ctm_get_power_supply_mode
	.set	nomips16
	.set	nomicromips
	.ent	ctm_get_power_supply_mode
	.type	ctm_get_power_supply_mode, @function
ctm_get_power_supply_mode:
	.frame	$sp,40,$31		# vars= 16, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$31,36($sp)
	jal	get_power_supply_mode
	nop

	addiu	$6,$sp,16
	li	$5,16384			# 0x4000
	jal	get_device_csr_bit
	li	$4,1			# 0x1

	lw	$2,16($sp)
	lw	$31,36($sp)
	addiu	$sp,$sp,40
	srl	$2,$2,14
	xori	$2,$2,0x1
	jr	$31
	andi	$2,$2,0x1

	.set	macro
	.set	reorder
	.end	ctm_get_power_supply_mode
	.size	ctm_get_power_supply_mode, .-ctm_get_power_supply_mode
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
	.align	2
	.globl	ctm_check_event_null_function
	.set	nomips16
	.set	nomicromips
	.ent	ctm_check_event_null_function
	.type	ctm_check_event_null_function, @function
ctm_check_event_null_function:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	ctm_check_event_null_function
	.size	ctm_check_event_null_function, .-ctm_check_event_null_function
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"INIT_===============\000"
	.align	2
$LC1:
	.ascii	"SP5K_MSG_HOST_TASK_INIT_-_s\000"
	.align	2
$LC2:
	.ascii	"SP5K_MSG_HOST_TASK_INIT_-_e\000"
	.align	2
$LC3:
	.ascii	"===============_OFF\000"
	.align	2
$LC4:
	.ascii	"MOUNT_COMPLETE\000"
	.align	2
$LC5:
	.ascii	"DISK_ERROR_-_%d\000"
	.align	2
$LC6:
	.ascii	"Disc_Removal_-_%d\000"
	.align	2
$LC7:
	.ascii	"Disc_Insertion_-_%d\000"
	.align	2
$LC8:
	.ascii	"USB IN\000"
	.align	2
$LC9:
	.ascii	"USB OUT\000"
	.align	2
$LC10:
	.ascii	"SP5k_MSG_DCF_INIT_START\000"
	.align	2
$LC11:
	.ascii	"SP5k_MSG_DCF_INIT_FAIL\000"
	.align	2
$LC12:
	.ascii	"FastCap_CST_MSG_ID_MOUNT_FAIL\000"
	.align	2
$LC13:
	.ascii	"FastCap_CST_MSG_ID_MOUNT_FINISH_s\000"
	.align	2
$LC14:
	.ascii	"FastCap_CST_MSG_ID_MOUNT_FINISH_e\000"
	.text
	.align	2
	.globl	ctm_event_loop_iterator
	.set	nomips16
	.set	nomicromips
	.ent	ctm_event_loop_iterator
	.type	ctm_event_loop_iterator, @function
ctm_event_loop_iterator:
	.frame	$sp,48,$31		# vars= 16, regs= 4/0, args= 16, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-48
	sw	$16,32($sp)
	lui	$16,%hi(g_event_descriptor)
	sw	$17,36($sp)
	move	$17,$4
	addiu	$4,$16,%lo(g_event_descriptor)
	sw	$18,40($sp)
	sw	$31,44($sp)
	jal	event_descriptor_init
	move	$18,$5

	sw	$17,%lo(g_event_descriptor)($16)
	addiu	$5,$sp,16
	addiu	$16,$16,%lo(g_event_descriptor)
	li	$4,-1			# 0xffffffffffffffff
	sw	$0,16($sp)
	sw	$0,20($sp)
	sw	$0,24($sp)
	jal	get_matching_event_descriptor
	sw	$18,4($16)

	beq	$2,$0,$L8
	li	$2,1364262912			# 0x51510000

	lw	$4,16($sp)
	beq	$4,$2,$L9
	addiu	$2,$2,1

	slt	$2,$4,$2
	beq	$2,$0,$L10
	li	$2,1481703424			# 0x58510000

	slt	$2,$4,259
	beq	$2,$0,$L11
	slt	$2,$4,256

	beq	$2,$0,$L12
	li	$2,16			# 0x10

	beq	$4,$2,$L13
	slt	$2,$4,17

	beq	$2,$0,$L14
	li	$2,32			# 0x20

	li	$2,-268435456			# 0xfffffffff0000000
	beq	$4,$2,$L15
	li	$2,-1			# 0xffffffffffffffff

	beq	$4,$2,$L16
	move	$5,$18

$L17:
	lw	$2,8($16)
$L66:
	li	$3,-5			# 0xfffffffffffffffb
	and	$2,$2,$3
	b	$L8
	sw	$2,8($16)

$L14:
	bne	$4,$2,$L17
	lui	$5,%hi($LC3)

	b	$L60
	addiu	$5,$5,%lo($LC3)

$L11:
	li	$2,517			# 0x205
	beq	$4,$2,$L19
	slt	$2,$4,518

	beq	$2,$0,$L20
	li	$2,8192			# 0x2000

	li	$2,515			# 0x203
	beq	$4,$2,$L21
	lui	$5,%hi($LC4)

	addiu	$4,$4,-514
	li	$2,-3			# 0xfffffffffffffffd
	and	$4,$4,$2
	bnel	$4,$0,$L66
	lw	$2,8($16)

$L8:
	jal	fsm_iterate_all_in_g_fsm_descriptor_list
	nop

	b	$L65
	lw	$31,44($sp)

$L20:
	beq	$4,$2,$L22
	li	$2,8193			# 0x2001

	bne	$4,$2,$L17
	lw	$6,20($sp)

	li	$2,2			# 0x2
	beq	$6,$2,$L42
	lui	$5,%hi($LC7)

	b	$L61
	addiu	$5,$5,%lo($LC7)

$L10:
	beq	$4,$2,$L24
	addiu	$2,$2,1

	slt	$2,$4,$2
	beq	$2,$0,$L25
	li	$2,1683030016			# 0x64510000

	li	$2,1381040128			# 0x52510000
	addiu	$3,$2,1295
	beq	$4,$3,$L26
	addiu	$3,$2,1296

	slt	$3,$4,$3
	beql	$3,$0,$L27
	addiu	$2,$2,1310

	addiu	$3,$2,1287
	beq	$4,$3,$L63
	addiu	$2,$2,1290

	bnel	$4,$2,$L66
	lw	$2,8($16)

	jal	get_g_evt_0x5251050a_counter
	nop

	jal	set_g_evt_0x5251050a_counter
	addiu	$4,$2,1

	b	$L8
	nop

$L27:
	beq	$4,$2,$L30
	slt	$2,$4,$2

	bnel	$2,$0,$L66
	lw	$2,8($16)

	li	$2,1397817344			# 0x53510000
	addiu	$2,$2,1302
	beq	$4,$2,$L8
	li	$2,1397817344			# 0x53510000

	addiu	$2,$2,1305
	beq	$4,$2,$L8
	nop

	b	$L66
	lw	$2,8($16)

$L25:
	addiu	$3,$2,1
	beq	$4,$3,$L31
	addiu	$3,$2,2

	slt	$3,$4,$3
	beq	$3,$0,$L32
	addiu	$2,$2,3

	li	$2,1649475584			# 0x62510000
	addiu	$3,$2,5
	beq	$4,$3,$L33
	addiu	$2,$2,6

	bne	$4,$2,$L17
	lui	$5,%hi($LC9)

	b	$L64
	addiu	$5,$5,%lo($LC9)

$L32:
	bne	$4,$2,$L17
	lui	$5,%hi($LC11)

	b	$L60
	addiu	$5,$5,%lo($LC11)

$L16:
	jal	event_loop_iterator
	move	$4,$17

	lw	$31,44($sp)
$L65:
	lw	$18,40($sp)
	lw	$17,36($sp)
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,48

$L13:
	lui	$5,%hi($LC0)
	addiu	$5,$5,%lo($LC0)
	jal	debug_print_string
	move	$4,$0

	lui	$5,%hi($LC1)
	addiu	$5,$5,%lo($LC1)
	jal	debug_print_string
	move	$4,$0

	jal	host_task_init
	nop

	lui	$5,%hi($LC2)
	addiu	$5,$5,%lo($LC2)
$L60:
	jal	debug_print_string
	move	$4,$0

	b	$L8
	nop

$L12:
	jal	service_button_event
	lw	$5,20($sp)

	b	$L8
	nop

$L21:
	b	$L60
	addiu	$5,$5,%lo($LC4)

$L19:
	lw	$6,20($sp)
	lui	$5,%hi($LC5)
	addiu	$5,$5,%lo($LC5)
$L61:
	jal	debug_print_string
	move	$4,$0

	b	$L8
	nop

$L22:
	lw	$16,20($sp)
	li	$2,2			# 0x2
	beq	$16,$2,$L37
	lui	$5,%hi($LC6)

	move	$6,$16
	b	$L61
	addiu	$5,$5,%lo($LC6)

$L37:
	jal	get_SDCardState
	nop

	bne	$2,$16,$L38
	nop

	jal	get_g_test_mode
	nop

	beq	$2,$0,$L40
	nop

	jal	get_g_sd_card_mounted_p
	nop

	beq	$2,$0,$L40
	nop

	li	$4,65536			# 0x10000
	jal	vfs_unmount_wrapper2
	addiu	$4,$4,2

$L40:
	jal	set_g_sd_card_mounted_p
	move	$4,$0

$L38:
	jal	set_sd_card_state_w_init
	li	$4,65535			# 0xffff

$L62:
	jal	initialize_g_mode_change_counter
	li	$4,1			# 0x1

	b	$L8
	nop

$L42:
	jal	set_sd_card_state_w_init
	li	$4,2			# 0x2

	jal	get_g_sd_card_valid_p
	nop

	beq	$2,$0,$L62
	nop

	jal	set_g_sd_card_state_valid_p
	move	$4,$0

	b	$L8
	nop

$L9:
	lw	$5,20($sp)
	jal	serviceEvent_0x5151000
	li	$4,1364262912			# 0x51510000

	b	$L8
	nop

$L30:
	jal	set_g_evt_0x52510507_state_initialized_p
	move	$4,$0

	b	$L8
	nop

$L26:
	jal	setStillCapDone
	nop

$L63:
	jal	set_g_evt_0x52510507_state_initialized_p
	move	$4,$0

	jal	get_g_evt_0x52510507_counter
	nop

	jal	set_g_evt_0x52510507_counter
	addiu	$4,$2,1

	b	$L8
	nop

$L24:
	jal	service_event_0x5851000
	lw	$4,20($sp)

	b	$L8
	nop

$L33:
	lui	$5,%hi($LC8)
	addiu	$5,$5,%lo($LC8)
$L64:
	jal	debug_print_string
	move	$4,$0

	b	$L62
	nop

$L31:
	lui	$5,%hi($LC10)
	b	$L60
	addiu	$5,$5,%lo($LC10)

$L15:
	lw	$5,20($sp)
	li	$3,1			# 0x1
	sra	$2,$5,8
	bne	$2,$3,$L44
	li	$3,7			# 0x7

	andi	$5,$5,0x00ff
	jal	serviceSetCurrentMode_event
	li	$4,1			# 0x1

	b	$L8
	nop

$L44:
	beq	$2,$3,$L45
	li	$3,8			# 0x8

	bne	$2,$3,$L8
	nop

	jal	get_g_fast_cap_mount_active_p
	nop

	beq	$2,$0,$L8
	lui	$5,%hi($LC12)

	addiu	$5,$5,%lo($LC12)
	jal	debug_print_string
	move	$4,$0

	jal	set_g_info_strip_enabled_p
	li	$4,1			# 0x1

	jal	set_fast_cap_mount_active_p
	move	$4,$0

	b	$L8
	nop

$L45:
	jal	get_g_fast_cap_mount_active_p
	nop

	beq	$2,$0,$L8
	lui	$5,%hi($LC13)

	addiu	$5,$5,%lo($LC13)
	jal	debug_print_string
	move	$4,$0

	jal	set_g_sd_card_mounted_p
	li	$4,1			# 0x1

	jal	set_g_some_sd_status_p
	li	$4,1			# 0x1

	jal	app_init_directory_suffix_file_prefix
	nop

	jal	check_remaining_sd_capacity
	nop

	jal	set_g_info_strip_enabled_p
	li	$4,1			# 0x1

	jal	set_fast_cap_mount_active_p
	move	$4,$0

	lui	$5,%hi($LC14)
	b	$L60
	addiu	$5,$5,%lo($LC14)

	.set	macro
	.set	reorder
	.end	ctm_event_loop_iterator
	.size	ctm_event_loop_iterator, .-ctm_event_loop_iterator
	.section	.rodata.str1.4
	.align	2
$LC15:
	.ascii	"DIGIPIRSPI_SERIN_OUT_L\000"
	.align	2
$LC16:
	.ascii	"DIGIPIRSPI_SERIN_OUT_H\000"
	.align	2
$LC17:
	.ascii	"DigiPIRSpi_Write\000"
	.align	2
$LC18:
	.ascii	"%s_PIR_LOAD_DATA_TIMEOUT_:_%d_u Retry %d\012\000"
	.align	2
$LC19:
	.ascii	"DigiPIRSpi_Write Failed after %d retries\000"
	.align	2
$LC20:
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
	lui	$21,%hi($LC15)
	lui	$20,%hi($LC16)
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
	addiu	$20,$20,%lo($LC16)
	addiu	$21,$21,%lo($LC15)
	lui	$23,%hi($LC17)
	li	$17,25			# 0x19
$L79:
	li	$22,16777216			# 0x1000000
$L72:
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

	bne	$fp,$0,$L68
	move	$19,$2

	jal	digi_pir_spi_serial_out
	move	$4,$0

	move	$5,$21
$L69:
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
	bne	$2,$0,$L70
	nop

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC18)
	move	$7,$16
	move	$6,$19
	addiu	$5,$23,%lo($LC17)
	jal	tty_printf
	addiu	$4,$4,%lo($LC18)

	jal	check_post_printf_state_set_sio_params
	addiu	$16,$16,1

$L71:
	jal	digi_pir_spi_serial_out
	move	$4,$0

	jal	some_sort_of_delay
	li	$4,560			# 0x230

	slt	$2,$16,3
	bne	$2,$0,$L73
	nop

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC19)
	move	$5,$16
	addiu	$4,$4,%lo($LC19)
	jal	tty_printf
	slt	$16,$16,1001

	jal	check_post_printf_state_set_sio_params
	nop

	bne	$16,$0,$L67
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

$L68:
	jal	digi_pir_spi_serial_out
	li	$4,1			# 0x1

	b	$L69
	move	$5,$20

$L70:
	bne	$17,$0,$L72
	nop

	b	$L71
	nop

$L73:
	bne	$17,$0,$L79
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
	lui	$5,%hi($LC20)
	addiu	$5,$5,%lo($LC20)
	li	$4,4			# 0x4
	j	log_printf
	addiu	$sp,$sp,56

$L67:
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
