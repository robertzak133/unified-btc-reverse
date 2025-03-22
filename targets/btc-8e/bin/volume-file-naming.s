	.file	1 "volume-file-naming.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	wbwl_fatVolLabSet
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_fatVolLabSet
	.type	wbwl_fatVolLabSet, @function
wbwl_fatVolLabSet:
	.frame	$sp,40,$31		# vars= 16, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$16,32($sp)
	move	$16,$4
	sw	$5,44($sp)
	sw	$31,36($sp)
	jal	get_cold_item_camera_name
	addiu	$4,$sp,16

	lb	$2,16($sp)
	bne	$2,$0,$L2
	lw	$5,44($sp)

	jal	fatVolLabSet
	move	$4,$16

	lw	$31,36($sp)
$L5:
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,40

$L2:
	addiu	$5,$sp,16
	move	$4,$16
	jal	fatVolLabSet_wrapper
	sb	$0,26($sp)

	b	$L5
	lw	$31,36($sp)

	.set	macro
	.set	reorder
	.end	wbwl_fatVolLabSet
	.size	wbwl_fatVolLabSet, .-wbwl_fatVolLabSet
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"_BTCF\000"
	.align	2
$LC1:
	.ascii	"IMG_\000"
	.text
	.align	2
	.globl	vfn_get_dir_suffix_file_prefix_from_camera_name
	.set	nomips16
	.set	nomicromips
	.ent	vfn_get_dir_suffix_file_prefix_from_camera_name
	.type	vfn_get_dir_suffix_file_prefix_from_camera_name, @function
vfn_get_dir_suffix_file_prefix_from_camera_name:
	.frame	$sp,32,$31		# vars= 0, regs= 3/0, args= 16, gp= 0
	.mask	0x80030000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lb	$2,0($6)
	addiu	$sp,$sp,-32
	sw	$17,24($sp)
	sw	$16,20($sp)
	sw	$31,28($sp)
	move	$17,$4
	beq	$2,$0,$L25
	move	$16,$5

	move	$4,$0
	li	$8,32			# 0x20
	li	$9,95			# 0x5f
	li	$7,5			# 0x5
	addu	$2,$6,$4
$L28:
	lb	$5,0($2)
	bne	$5,$8,$L8
	addu	$3,$17,$4

	sb	$9,0($3)
$L9:
	lb	$2,0($2)
	beql	$2,$0,$L27
	addu	$17,$17,$4

	addiu	$4,$4,1
	bne	$4,$7,$L28
	addu	$2,$6,$4

	addu	$17,$17,$4
$L27:
	sb	$0,0($17)
	move	$5,$0
	li	$8,32			# 0x20
	li	$9,95			# 0x5f
	li	$7,4			# 0x4
	addu	$2,$6,$5
$L30:
	lb	$4,0($2)
	bne	$4,$8,$L11
	addu	$3,$16,$5

	sb	$9,0($3)
$L12:
	lb	$2,0($2)
	beql	$2,$0,$L29
	addu	$5,$16,$5

	addiu	$5,$5,1
	bne	$5,$7,$L30
	addu	$2,$6,$5

	addu	$5,$16,$5
$L29:
	sb	$0,0($5)
	lw	$31,28($sp)
	lw	$17,24($sp)
	lw	$16,20($sp)
	jr	$31
	addiu	$sp,$sp,32

$L25:
	jal	btc_init_directory_suffix_file_prefix
	nop

	lui	$5,%hi($LC0)
	move	$4,$17
	jal	btc_strcpy
	addiu	$5,$5,%lo($LC0)

	lw	$31,28($sp)
	lw	$17,24($sp)
	move	$4,$16
	lw	$16,20($sp)
	lui	$5,%hi($LC1)
	addiu	$5,$5,%lo($LC1)
	j	btc_strcpy
	addiu	$sp,$sp,32

$L8:
	b	$L9
	sb	$5,0($3)

$L11:
	b	$L12
	sb	$4,0($3)

	.set	macro
	.set	reorder
	.end	vfn_get_dir_suffix_file_prefix_from_camera_name
	.size	vfn_get_dir_suffix_file_prefix_from_camera_name, .-vfn_get_dir_suffix_file_prefix_from_camera_name
	.section	.rodata.str1.4
	.align	2
$LC2:
	.ascii	"dcfapi.c\000"
	.text
	.align	2
	.globl	wbwl_init_directory_suffix_file_prefix
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_init_directory_suffix_file_prefix
	.type	wbwl_init_directory_suffix_file_prefix, @function
wbwl_init_directory_suffix_file_prefix:
	.frame	$sp,72,$31		# vars= 48, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-72
	sw	$31,68($sp)
	jal	get_cold_item_camera_name
	addiu	$4,$sp,16

	addiu	$6,$sp,16
	addiu	$5,$sp,32
	jal	vfn_get_dir_suffix_file_prefix_from_camera_name
	addiu	$4,$sp,48

	lui	$2,%hi(g_dcfapi_loaded_p)
	lbu	$3,%lo(g_dcfapi_loaded_p)($2)
	li	$2,1			# 0x1
	beq	$3,$2,$L38
	lui	$2,%hi(g_active_dcfapi_functions+16)

	lui	$4,%hi($LC2)
	move	$6,$0
	li	$5,173			# 0xad
	jal	function_with_syscall_zero
	addiu	$4,$4,%lo($LC2)

	lui	$2,%hi(g_active_dcfapi_functions+16)
$L38:
	lw	$2,%lo(g_active_dcfapi_functions+16)($2)
	beq	$2,$0,$L31
	move	$6,$0

	addiu	$5,$sp,32
	jalr	$2
	addiu	$4,$sp,48

$L31:
	lw	$31,68($sp)
	jr	$31
	addiu	$sp,$sp,72

	.set	macro
	.set	reorder
	.end	wbwl_init_directory_suffix_file_prefix
	.size	wbwl_init_directory_suffix_file_prefix, .-wbwl_init_directory_suffix_file_prefix
	.align	2
	.globl	wbwl_alt_init_directory_suffix_file_prefix
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_alt_init_directory_suffix_file_prefix
	.type	wbwl_alt_init_directory_suffix_file_prefix, @function
wbwl_alt_init_directory_suffix_file_prefix:
	.frame	$sp,40,$31		# vars= 16, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$16,32($sp)
	move	$16,$4
	addiu	$4,$sp,16
	sw	$31,36($sp)
	sw	$5,44($sp)
	jal	get_cold_item_camera_name
	sw	$6,48($sp)

	lb	$2,16($sp)
	bne	$2,$0,$L40
	lw	$6,48($sp)

	lw	$5,44($sp)
	jal	init_directory_suffix_file_prefix
	move	$4,$16

	lw	$31,36($sp)
$L43:
	lw	$16,32($sp)
	jr	$31
	addiu	$sp,$sp,40

$L40:
	jal	wbwl_init_directory_suffix_file_prefix
	nop

	b	$L43
	lw	$31,36($sp)

	.set	macro
	.set	reorder
	.end	wbwl_alt_init_directory_suffix_file_prefix
	.size	wbwl_alt_init_directory_suffix_file_prefix, .-wbwl_alt_init_directory_suffix_file_prefix
	.align	2
	.globl	wbwl_temp_file_path_sprintf
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_temp_file_path_sprintf
	.type	wbwl_temp_file_path_sprintf, @function
wbwl_temp_file_path_sprintf:
	.frame	$sp,96,$31		# vars= 48, regs= 5/0, args= 24, gp= 0
	.mask	0x800f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-96
	sw	$19,88($sp)
	sw	$16,76($sp)
	addiu	$19,$sp,40
	move	$16,$4
	addiu	$4,$sp,24
	sw	$31,92($sp)
	sw	$18,84($sp)
	sw	$17,80($sp)
	move	$18,$6
	jal	get_cold_item_camera_name
	move	$17,$5

	addiu	$6,$sp,24
	move	$5,$19
	jal	vfn_get_dir_suffix_file_prefix_from_camera_name
	addiu	$4,$sp,56

	lw	$2,116($sp)
	sw	$19,16($sp)
	addiu	$7,$sp,56
	sw	$2,20($sp)
	move	$6,$18
	move	$5,$17
	jal	local_sprintf
	move	$4,$16

	lw	$31,92($sp)
	lw	$19,88($sp)
	lw	$18,84($sp)
	lw	$17,80($sp)
	lw	$16,76($sp)
	jr	$31
	addiu	$sp,$sp,96

	.set	macro
	.set	reorder
	.end	wbwl_temp_file_path_sprintf
	.size	wbwl_temp_file_path_sprintf, .-wbwl_temp_file_path_sprintf

	.comm	g_wbwl_timelapse_frequency_lookup_table,24,4

	.comm	g_tlps_file_type_menu,84,4

	.comm	g_wbwl_timelapse_frequency_menu,364,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
