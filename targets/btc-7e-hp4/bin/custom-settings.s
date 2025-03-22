	.file	1 "custom-settings.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	cst_custom_cold_item_valid_p
	.set	nomips16
	.set	nomicromips
	.ent	cst_custom_cold_item_valid_p
	.type	cst_custom_cold_item_valid_p, @function
cst_custom_cold_item_valid_p:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	move	$2,$0

	.set	macro
	.set	reorder
	.end	cst_custom_cold_item_valid_p
	.size	cst_custom_cold_item_valid_p, .-cst_custom_cold_item_valid_p
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"D:\\CUSTOM781.BIN\000"
	.text
	.align	2
	.globl	cst_valid_custom_config_p
	.set	nomips16
	.set	nomicromips
	.ent	cst_valid_custom_config_p
	.type	cst_valid_custom_config_p, @function
cst_valid_custom_config_p:
	.frame	$sp,24,$31		# vars= 0, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lui	$4,%hi($LC0)
	addiu	$sp,$sp,-24
	addiu	$4,$4,%lo($LC0)
	sw	$31,20($sp)
	jal	btc_fopen
	li	$5,16			# 0x10

	move	$4,$2
	beq	$4,$0,$L2
	move	$2,$0

	jal	vfsClose
	nop

	li	$2,1			# 0x1
$L2:
	lw	$31,20($sp)
	jr	$31
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	cst_valid_custom_config_p
	.size	cst_valid_custom_config_p, .-cst_valid_custom_config_p
	.section	.rodata.str1.4
	.align	2
$LC1:
	.ascii	"%read size invalid [%d/%d]\000"
	.align	2
$LC2:
	.ascii	"%s data signature invalid_[0x%x_/_%d]\000"
	.align	2
$LC3:
	.ascii	"COLD.BIN size invalid[%d/%d]\000"
	.align	2
$LC4:
	.ascii	"%recorded size invalid[%d/%d]\000"
	.align	2
$LC5:
	.ascii	"cst_RestoreCustomColdItem\000"
	.align	2
$LC6:
	.ascii	"%s_failed to open config file %s!\012\000"
	.text
	.align	2
	.globl	cst_RestoreCustomColdItem
	.set	nomips16
	.set	nomicromips
	.ent	cst_RestoreCustomColdItem
	.type	cst_RestoreCustomColdItem, @function
cst_RestoreCustomColdItem:
	.frame	$sp,48,$31		# vars= 0, regs= 6/0, args= 24, gp= 0
	.mask	0x801f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-48
	sw	$19,36($sp)
	sw	$16,24($sp)
	lui	$19,%hi(g_ColdItemData)
	lui	$16,%hi($LC0)
	sw	$20,40($sp)
	sw	$18,32($sp)
	li	$20,1			# 0x1
	addiu	$18,$19,%lo(g_ColdItemData)
	li	$5,16			# 0x10
	addiu	$4,$16,%lo($LC0)
	sw	$31,44($sp)
	sw	$17,28($sp)
	jal	btc_fopen
	sb	$20,2($18)

	bne	$2,$0,$L9
	move	$17,$2

	jal	set_pre_printf_state
	nop

	lui	$5,%hi($LC5)
	lui	$4,%hi($LC6)
	addiu	$6,$16,%lo($LC0)
	addiu	$5,$5,%lo($LC5)
	jal	tty_printf
	addiu	$4,$4,%lo($LC6)

	jal	check_post_printf_state_set_sio_params
	move	$16,$0

	lw	$31,44($sp)
$L18:
	lw	$20,40($sp)
	lw	$19,36($sp)
	lw	$18,32($sp)
	lw	$17,28($sp)
	move	$2,$16
	lw	$16,24($sp)
	jr	$31
	addiu	$sp,$sp,48

$L9:
	move	$7,$0
	move	$6,$0
	li	$5,16			# 0x10
	move	$4,$2
	jal	seekToSpecifiedFileLocation
	sw	$0,16($sp)

	jal	fsize
	move	$4,$17

	move	$16,$2
	sltu	$2,$2,332
	beq	$2,$0,$L11
	li	$6,332			# 0x14c

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC3)
	li	$7,332			# 0x14c
	addiu	$4,$4,%lo($LC3)
$L12:
	lui	$5,%hi($LC5)
	move	$6,$16
	jal	tty_printf
	addiu	$5,$5,%lo($LC5)

	jal	check_post_printf_state_set_sio_params
	move	$16,$0

	b	$L16
	nop

$L11:
	move	$5,$18
	jal	btc_fread
	move	$4,$17

	move	$16,$2
	li	$2,332			# 0x14c
	beq	$16,$2,$L13
	lh	$2,%lo(g_ColdItemData)($19)

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC1)
	li	$7,332			# 0x14c
	b	$L12
	addiu	$4,$4,%lo($LC1)

$L13:
	beql	$2,$16,$L14
	lh	$3,328($18)

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC4)
	lhu	$16,%lo(g_ColdItemData)($19)
	li	$7,332			# 0x14c
	b	$L12
	addiu	$4,$4,%lo($LC4)

$L14:
	li	$2,23100			# 0x5a3c
	bne	$3,$2,$L15
	lui	$2,%hi(g_cold_item_signature_valid_p)

	sb	$20,%lo(g_cold_item_signature_valid_p)($2)
	li	$16,1			# 0x1
$L16:
	jal	btc_fclose
	move	$4,$17

	lui	$4,%hi(g_ReferenceColdItemData)
	li	$6,332			# 0x14c
	move	$5,$18
	jal	memcpy
	addiu	$4,$4,%lo(g_ReferenceColdItemData)

	b	$L18
	lw	$31,44($sp)

$L15:
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC2)
	lhu	$16,328($18)
	li	$7,23100			# 0x5a3c
	b	$L12
	addiu	$4,$4,%lo($LC2)

	.set	macro
	.set	reorder
	.end	cst_RestoreCustomColdItem
	.size	cst_RestoreCustomColdItem, .-cst_RestoreCustomColdItem
	.section	.rodata.str1.4
	.align	2
$LC7:
	.ascii	"failed_to_open_COLD.BIN!\000"
	.text
	.align	2
	.globl	cst_SaveCustomColdItem
	.set	nomips16
	.set	nomicromips
	.ent	cst_SaveCustomColdItem
	.type	cst_SaveCustomColdItem, @function
cst_SaveCustomColdItem:
	.frame	$sp,40,$31		# vars= 0, regs= 3/0, args= 24, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$17,32($sp)
	lui	$17,%hi($LC0)
	li	$5,32			# 0x20
	addiu	$4,$17,%lo($LC0)
	sw	$31,36($sp)
	jal	btc_fopen
	sw	$16,28($sp)

	bne	$2,$0,$L21
	move	$16,$2

	li	$5,36			# 0x24
	jal	btc_fopen
	addiu	$4,$17,%lo($LC0)

	move	$16,$2
	bne	$2,$0,$L20
	li	$5,36			# 0x24

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC7)
	jal	tty_printf
	addiu	$4,$4,%lo($LC7)

	lw	$31,36($sp)
	lw	$17,32($sp)
	lw	$16,28($sp)
	j	check_post_printf_state_set_sio_params
	addiu	$sp,$sp,40

$L21:
	li	$5,32			# 0x20
$L20:
	move	$4,$16
	sw	$0,16($sp)
	move	$7,$0
	jal	seekToSpecifiedFileLocation
	move	$6,$0

	lui	$5,%hi(g_ColdItemData)
	move	$4,$16
	li	$6,332			# 0x14c
	jal	btc_fwrite
	addiu	$5,$5,%lo(g_ColdItemData)

	lw	$31,36($sp)
	lw	$17,32($sp)
	move	$4,$16
	lw	$16,28($sp)
	j	btc_fclose
	addiu	$sp,$sp,40

	.set	macro
	.set	reorder
	.end	cst_SaveCustomColdItem
	.size	cst_SaveCustomColdItem, .-cst_SaveCustomColdItem
	.align	2
	.globl	cst_handleRestoreDefault_menu
	.set	nomips16
	.set	nomicromips
	.ent	cst_handleRestoreDefault_menu
	.type	cst_handleRestoreDefault_menu, @function
cst_handleRestoreDefault_menu:
	.frame	$sp,48,$31		# vars= 8, regs= 6/0, args= 16, gp= 0
	.mask	0x801f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-48
	sw	$31,44($sp)
	sw	$20,40($sp)
	sw	$19,36($sp)
	sw	$18,32($sp)
	sw	$17,28($sp)
	jal	getCameraConfigStructPtr
	sw	$16,24($sp)

	bnel	$2,$0,$L25
	lbu	$17,0($2)

	jal	handleRestoreDefault_menu
	nop

	lw	$31,44($sp)
$L44:
	lw	$20,40($sp)
$L47:
	lw	$19,36($sp)
	lw	$18,32($sp)
	lw	$17,28($sp)
	lw	$16,24($sp)
	jr	$31
	addiu	$sp,$sp,48

$L25:
	beq	$17,$0,$L27
	move	$16,$2

	sb	$0,0($2)
	jal	cst_valid_custom_config_p
	sb	$0,2($2)

	li	$3,1			# 0x1
	bne	$2,$3,$L29
	lui	$17,%hi(g_menu_root)

	addiu	$5,$17,%lo(g_menu_root)
	jal	getCurrentMenuCollectionAndSize
	addiu	$4,$sp,16

	lw	$2,20($sp)
	sltu	$2,$2,2
	bne	$2,$0,$L29
	lw	$2,16($sp)

	sw	$0,64($2)
$L29:
	addiu	$5,$17,%lo(g_menu_root)
	jal	menu_draw_selected_item
	addiu	$4,$16,2

	b	$L44
	lw	$31,44($sp)

$L27:
	jal	ui_cursor_key_pressed_p
	move	$4,$0

	li	$3,1			# 0x1
	bne	$2,$3,$L31
	lui	$2,%hi(g_up_button_enable)

	lbu	$3,%lo(g_up_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L46
	lui	$18,%hi(g_menu_root)

$L31:
	jal	ui_cursor_key_pressed_p
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,1			# 0x1
	bne	$17,$2,$L33
	lui	$2,%hi(g_down_button_enable)

	lbu	$3,%lo(g_down_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L32
	lui	$18,%hi(g_menu_root)

$L33:
	jal	ui_cursor_key_pressed_p
	li	$4,2			# 0x2

	li	$3,1			# 0x1
	beq	$2,$3,$L34
	lui	$2,%hi(g_left_button_enable)

$L35:
	jal	ui_cursor_key_pressed_p
	li	$4,3			# 0x3

	li	$3,1			# 0x1
	bne	$2,$3,$L36
	lui	$2,%hi(g_right_button_enable)

	lbu	$3,%lo(g_right_button_enable)($2)
	li	$2,2			# 0x2
	beq	$3,$2,$L44
	lw	$31,44($sp)

$L36:
	jal	ui_cursor_key_pressed_p
	li	$4,4			# 0x4

	move	$18,$2
	li	$2,1			# 0x1
	bne	$18,$2,$L38
	lui	$2,%hi(g_enter_button_enable)

	lbu	$20,%lo(g_enter_button_enable)($2)
	li	$2,2			# 0x2
	bne	$20,$2,$L38
	lui	$2,%hi(g_wbwl_camera_setup_selector_array)

	lbu	$4,2($16)
	addiu	$2,$2,%lo(g_wbwl_camera_setup_selector_array)
	sll	$3,$4,3
	sb	$18,0($16)
	addu	$2,$2,$3
	lw	$6,4($2)
	lw	$5,0($2)
	lui	$7,%hi(g_menu_root)
	jal	get_next_state_from_menu_enter
	addiu	$7,$7,%lo(g_menu_root)

	move	$17,$2
	li	$2,255			# 0xff
	beq	$17,$2,$L44
	lw	$31,44($sp)

	lbu	$19,2($16)
	beq	$19,$20,$L39
	li	$2,3			# 0x3

	beq	$19,$2,$L40
	nop

	bne	$19,$18,$L41
	nop

	jal	HceCommon_RestoreDefaultColdItem
	li	$4,1			# 0x1

	sb	$19,4($16)
$L41:
$L45:
	jal	set_fsm_state_absolute
	move	$4,$17

	b	$L44
	lw	$31,44($sp)

$L32:
$L46:
	addiu	$5,$16,2
	move	$4,$17
	addiu	$7,$18,%lo(g_menu_root)
	jal	menu_get_next_menu_selection
	li	$6,1			# 0x1

	lbu	$4,2($16)
	jal	menu_redraw_items
	addiu	$5,$18,%lo(g_menu_root)

	b	$L44
	lw	$31,44($sp)

$L34:
	lbu	$3,%lo(g_left_button_enable)($2)
	li	$2,2			# 0x2
	bne	$3,$2,$L35
	lw	$31,44($sp)

	b	$L47
	lw	$20,40($sp)

$L39:
	jal	cst_RestoreCustomColdItem
	nop

	b	$L41
	sb	$18,4($16)

$L40:
	jal	cst_SaveCustomColdItem
	nop

	b	$L45
	sb	$18,4($16)

$L38:
	jal	ui_cursor_key_pressed_p
	li	$4,5			# 0x5

	li	$3,1			# 0x1
	bne	$2,$3,$L44
	lw	$31,44($sp)

	lui	$3,%hi(g_mode_button_enable)
	lbu	$4,%lo(g_mode_button_enable)($3)
	li	$3,2			# 0x2
	bne	$4,$3,$L47
	lw	$20,40($sp)

	lui	$5,%hi(g_menu_root)
	sh	$2,0($16)
	addiu	$5,$5,%lo(g_menu_root)
	jal	get_next_state_from_menu_mode
	li	$4,1			# 0x1

	move	$17,$2
	li	$2,255			# 0xff
	beql	$17,$2,$L41
	li	$17,35			# 0x23

	b	$L41
	nop

	.set	macro
	.set	reorder
	.end	cst_handleRestoreDefault_menu
	.size	cst_handleRestoreDefault_menu, .-cst_handleRestoreDefault_menu

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,240,4

	.comm	g_wbwl_camera_setup_menu_item_array,840,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
