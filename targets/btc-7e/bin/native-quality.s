	.file	1 "native-quality.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	ntvq_get_camera_photo_resolution
	.set	nomips16
	.set	nomicromips
	.ent	ntvq_get_camera_photo_resolution
	.type	ntvq_get_camera_photo_resolution, @function
ntvq_get_camera_photo_resolution:
	.frame	$sp,24,$31		# vars= 0, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	sltu	$2,$5,1001
	bne	$2,$0,$L2
	sltu	$2,$5,4

	j	get_camera_photo_resolution
	nop

$L2:
	addiu	$sp,$sp,-24
	sw	$16,16($sp)
	sw	$31,20($sp)
	beq	$2,$0,$L3
	move	$16,$4

	sll	$3,$5,2
	lui	$5,%hi(g_image_resolution_lookup_table)
	addiu	$5,$5,%lo(g_image_resolution_lookup_table)
	addu	$3,$3,$5
	lhu	$2,0($3)
	sw	$2,0($4)
	lhu	$2,2($3)
	sw	$0,8($4)
	sw	$0,12($4)
	sw	$2,4($4)
	lw	$31,20($sp)
$L7:
	move	$2,$16
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,24

$L3:
	jal	get_multi_shot_photo_dimensions
	nop

	b	$L7
	lw	$31,20($sp)

	.set	macro
	.set	reorder
	.end	ntvq_get_camera_photo_resolution
	.size	ntvq_get_camera_photo_resolution, .-ntvq_get_camera_photo_resolution
	.align	2
	.globl	npr_draw_sst_string_on_display
	.set	nomips16
	.set	nomicromips
	.ent	npr_draw_sst_string_on_display
	.type	npr_draw_sst_string_on_display, @function
npr_draw_sst_string_on_display:
	.frame	$sp,48,$31		# vars= 0, regs= 8/0, args= 16, gp= 0
	.mask	0x807f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-48
	sw	$22,40($sp)
	sw	$21,36($sp)
	sw	$20,32($sp)
	sw	$19,28($sp)
	sw	$18,24($sp)
	sw	$17,20($sp)
	sw	$16,16($sp)
	lw	$19,64($sp)
	lw	$20,68($sp)
	lw	$21,72($sp)
	sw	$31,44($sp)
	move	$16,$4
	move	$17,$5
	move	$18,$6
	jal	get_cold_item_multi_shot_encoding
	move	$22,$7

	sltu	$3,$2,8
	beq	$3,$0,$L9
	li	$2,4			# 0x4

	jal	get_cold_item_photo_resolution
	nop

$L9:
	lui	$3,%hi(g_npr_photo_resolution_string_lookup_table)
	sll	$2,$2,1
	addiu	$3,$3,%lo(g_npr_photo_resolution_string_lookup_table)
	addu	$2,$2,$3
	lhu	$2,0($2)
	lw	$31,44($sp)
	sw	$21,72($sp)
	sw	$20,68($sp)
	sw	$19,64($sp)
	lw	$21,36($sp)
	lw	$20,32($sp)
	lw	$19,28($sp)
	move	$7,$22
	move	$6,$18
	lw	$22,40($sp)
	lw	$18,24($sp)
	move	$5,$17
	move	$4,$16
	lw	$17,20($sp)
	lw	$16,16($sp)
	sw	$2,76($sp)
	j	draw_sst_string_on_display
	addiu	$sp,$sp,48

	.set	macro
	.set	reorder
	.end	npr_draw_sst_string_on_display
	.size	npr_draw_sst_string_on_display, .-npr_draw_sst_string_on_display
	.globl	g_npr_photo_resolution_string_lookup_table
	.data
	.align	2
	.type	g_npr_photo_resolution_string_lookup_table, @object
	.size	g_npr_photo_resolution_string_lookup_table, 10
g_npr_photo_resolution_string_lookup_table:
	.half	120
	.half	121
	.half	122
	.half	123
	.half	200
	.globl	g_ntvq_photo_quality_menu
	.align	2
	.type	g_ntvq_photo_quality_menu, @object
	.size	g_ntvq_photo_quality_menu, 168
g_ntvq_photo_quality_menu:
	.word	31
	.word	38
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	39
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	40
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	41
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	199
	.word	0
	.word	1
	.word	0
	.word	1
	.word	1
	.word	31
	.word	42
	.word	0
	.word	0
	.word	1
	.word	3
	.word	3

	.comm	g_wbwl_menu_handler_function_array_extensions,24,4

	.comm	g_wbwl_camera_setup_selector_array,240,4

	.comm	g_wbwl_camera_setup_menu_item_array,840,4

	.comm	g_wbwl_timelapse_period_menu,196,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
