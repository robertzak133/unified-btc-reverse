	.file	1 "custom-ribbon.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.align	2
	.globl	cr_expand_date_time
	.set	nomips16
	.set	nomicromips
	.ent	cr_expand_date_time
	.type	cr_expand_date_time, @function
cr_expand_date_time:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	srl	$2,$4,25
	addiu	$2,$2,80
	sw	$2,20($5)
	sll	$2,$4,7
	srl	$2,$2,28
	addiu	$2,$2,-1
	sw	$2,16($5)
	sll	$2,$4,11
	srl	$2,$2,27
	sw	$2,12($5)
	sll	$2,$4,16
	srl	$2,$2,27
	sw	$2,8($5)
	sll	$2,$4,21
	sll	$4,$4,1
	srl	$2,$2,26
	andi	$4,$4,0x3e
	sw	$2,4($5)
	sw	$4,0($5)
	sw	$0,24($5)
	sw	$0,28($5)
	jr	$31
	sw	$0,32($5)

	.set	macro
	.set	reorder
	.end	cr_expand_date_time
	.size	cr_expand_date_time, .-cr_expand_date_time
	.align	2
	.globl	wbwlFileCTimeGet
	.set	nomips16
	.set	nomicromips
	.ent	wbwlFileCTimeGet
	.type	wbwlFileCTimeGet, @function
wbwlFileCTimeGet:
	.frame	$sp,32,$31		# vars= 0, regs= 4/0, args= 16, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	sw	$18,24($sp)
	move	$18,$4
	li	$4,1080			# 0x438
	sw	$17,20($sp)
	sw	$16,16($sp)
	sw	$31,28($sp)
	jal	memoryAllocate
	move	$17,$5

	move	$16,$2
	beq	$16,$0,$L2
	li	$2,-1			# 0xffffffffffffffff

	move	$5,$16
	jal	posix_fileinfo
	move	$4,$18

	bltz	$2,$L4
	nop

	lw	$4,1072($16)
	jal	cr_expand_date_time
	move	$5,$17

	jal	free
	move	$4,$16

	move	$2,$0
$L2:
	lw	$31,28($sp)
	lw	$18,24($sp)
	lw	$17,20($sp)
	lw	$16,16($sp)
	jr	$31
	addiu	$sp,$sp,32

$L4:
	jal	free
	move	$4,$16

	b	$L2
	li	$2,-1			# 0xffffffffffffffff

	.set	macro
	.set	reorder
	.end	wbwlFileCTimeGet
	.size	wbwlFileCTimeGet, .-wbwlFileCTimeGet
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"%d:%02d:%02d AM\000"
	.align	2
$LC1:
	.ascii	"%d:%02d:%02d\000"
	.align	2
$LC2:
	.ascii	"%d:%02d:%02d PM\000"
	.align	2
$LC3:
	.ascii	"%02d/%02d/%04d %s  %d/%d\000"
	.align	2
$LC4:
	.ascii	"%04d%02d%02d %s  %d/%d\000"
	.align	2
$LC5:
	.ascii	"%d/%d\000"
	.text
	.align	2
	.globl	wbwl_custom_ribbon_sprintf
	.set	nomips16
	.set	nomicromips
	.ent	wbwl_custom_ribbon_sprintf
	.type	wbwl_custom_ribbon_sprintf, @function
wbwl_custom_ribbon_sprintf:
	.frame	$sp,128,$31		# vars= 72, regs= 6/0, args= 32, gp= 0
	.mask	0x801f0000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-128
	sw	$18,112($sp)
	sw	$17,108($sp)
	sw	$16,104($sp)
	sw	$31,124($sp)
	sw	$20,120($sp)
	sw	$19,116($sp)
	move	$18,$4
	move	$16,$6
	jal	getCameraConfigStructPtr
	move	$17,$7

	addiu	$4,$2,84
	jal	wbwlFileCTimeGet
	addiu	$5,$sp,32

	bne	$2,$0,$L8
	lui	$5,%hi($LC5)

	jal	rtc_get_cold_item_time_format
	nop

	jal	rtc_get_cold_item_date_format
	move	$20,$2

	move	$19,$2
	li	$2,1			# 0x1
	beq	$20,$2,$L9
	lw	$3,40($sp)

	sltu	$2,$3,13
	bne	$2,$0,$L10
	lui	$5,%hi($LC0)

	lui	$5,%hi($LC2)
	addiu	$3,$3,-12
	addiu	$5,$5,%lo($LC2)
$L11:
	lw	$2,32($sp)
	lw	$7,36($sp)
	move	$6,$3
	addiu	$4,$sp,68
	jal	local_sprintf
	sw	$2,16($sp)

	li	$4,1			# 0x1
	lw	$6,44($sp)
	lw	$2,48($sp)
	beq	$19,$4,$L12
	lw	$3,52($sp)

	li	$4,2			# 0x2
	sw	$17,28($sp)
	beq	$19,$4,$L13
	sw	$16,24($sp)

	addiu	$4,$sp,68
	addiu	$3,$3,1900
	move	$7,$6
	sw	$4,20($sp)
	sw	$3,16($sp)
	addiu	$6,$2,1
$L19:
	lui	$5,%hi($LC3)
	addiu	$5,$5,%lo($LC3)
$L18:
	jal	local_sprintf
	move	$4,$18

	lw	$31,124($sp)
$L20:
	lw	$20,120($sp)
	lw	$19,116($sp)
	lw	$18,112($sp)
	lw	$17,108($sp)
	lw	$16,104($sp)
	jr	$31
	addiu	$sp,$sp,128

$L10:
	bne	$3,$0,$L11
	addiu	$5,$5,%lo($LC0)

	b	$L11
	li	$3,12			# 0xc

$L9:
	lui	$5,%hi($LC1)
	b	$L11
	addiu	$5,$5,%lo($LC1)

$L12:
	addiu	$4,$sp,68
	addiu	$3,$3,1900
	sw	$17,28($sp)
	sw	$16,24($sp)
	sw	$4,20($sp)
	sw	$3,16($sp)
	b	$L19
	addiu	$7,$2,1

$L13:
	addiu	$4,$sp,68
	lui	$5,%hi($LC4)
	sw	$6,16($sp)
	sw	$4,20($sp)
	addiu	$7,$2,1
	addiu	$6,$3,1900
	b	$L18
	addiu	$5,$5,%lo($LC4)

$L8:
	move	$7,$17
	move	$6,$16
	addiu	$5,$5,%lo($LC5)
	jal	local_sprintf
	move	$4,$18

	b	$L20
	lw	$31,124($sp)

	.set	macro
	.set	reorder
	.end	wbwl_custom_ribbon_sprintf
	.size	wbwl_custom_ribbon_sprintf, .-wbwl_custom_ribbon_sprintf
	.align	2
	.globl	ld_draw_video_scroll_bar
	.set	nomips16
	.set	nomicromips
	.ent	ld_draw_video_scroll_bar
	.type	ld_draw_video_scroll_bar, @function
ld_draw_video_scroll_bar:
	.frame	$sp,32,$31		# vars= 0, regs= 2/0, args= 24, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-32
	li	$2,256			# 0x100
	sw	$16,24($sp)
	sw	$31,28($sp)
	bne	$4,$2,$L22
	move	$16,$4

	jal	draw_video_scroll_bar
	li	$4,254			# 0xfe

$L22:
	li	$2,13			# 0xd
	sw	$2,16($sp)
	li	$7,10			# 0xa
	li	$6,180			# 0xb4
	li	$5,204			# 0xcc
	jal	draw_rectangle_wrapper
	li	$4,2			# 0x2

	sw	$0,16($sp)
	li	$7,6			# 0x6
	li	$6,176			# 0xb0
	li	$5,206			# 0xce
	jal	draw_rectangle_wrapper
	li	$4,4			# 0x4

	li	$2,255			# 0xff
	beq	$16,$2,$L26
	lw	$31,28($sp)

	sltu	$2,$16,101
	beql	$2,$0,$L24
	li	$16,100			# 0x64

$L24:
	li	$6,176			# 0xb0
	mult	$16,$6
	mflo	$16
	li	$6,100			# 0x64
	li	$2,2			# 0x2
	sw	$2,16($sp)
	li	$7,6			# 0x6
	li	$5,206			# 0xce
	divu	$0,$16,$6
	nop
	teq	$6,$0,7
	mflo	$6
	jal	draw_rectangle_wrapper
	li	$4,4			# 0x4

	lw	$31,28($sp)
$L26:
	lw	$16,24($sp)
	jr	$31
	addiu	$sp,$sp,32

	.set	macro
	.set	reorder
	.end	ld_draw_video_scroll_bar
	.size	ld_draw_video_scroll_bar, .-ld_draw_video_scroll_bar
	.align	2
	.globl	ld_clear_video_scroll_bar
	.set	nomips16
	.set	nomicromips
	.ent	ld_clear_video_scroll_bar
	.type	ld_clear_video_scroll_bar, @function
ld_clear_video_scroll_bar:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	lb	$2,16($sp)
	addiu	$5,$5,-20
	j	draw_rectangle_wrapper
	sw	$2,16($sp)

	.set	macro
	.set	reorder
	.end	ld_clear_video_scroll_bar
	.size	ld_clear_video_scroll_bar, .-ld_clear_video_scroll_bar

	.comm	g_rtc_time_format_menu,84,4

	.comm	g_rtc_date_format_menu,112,4
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1) 9.4.0"
