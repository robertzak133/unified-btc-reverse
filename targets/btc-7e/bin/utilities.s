	.file	1 "utilities.c"
	.section .mdebug.abi32
	.previous
	.nan	legacy
	.module	fp=xx
	.module	nooddspreg
	.text
	.section	.rodata.str1.4,"aMS",@progbits,1
	.align	2
$LC0:
	.ascii	"Error::write_memory_to_file -- could not open %s\012\000"
	.text
	.align	2
	.globl	write_memory_to_file
	.set	nomips16
	.set	nomicromips
	.ent	write_memory_to_file
	.type	write_memory_to_file, @function
write_memory_to_file:
	.frame	$sp,40,$31		# vars= 8, regs= 4/0, args= 16, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$18,32($sp)
	sw	$17,28($sp)
	move	$18,$5
	move	$17,$4
	li	$5,4			# 0x4
	move	$4,$6
	sw	$16,24($sp)
	sw	$31,36($sp)
	jal	btc_fopen
	move	$16,$6

	bnel	$2,$0,$L2
	move	$4,$2

	lui	$4,%hi($LC0)
	move	$5,$16
	jal	tty_printf
	addiu	$4,$4,%lo($LC0)

	lw	$31,36($sp)
$L5:
	lw	$18,32($sp)
	lw	$17,28($sp)
	lw	$16,24($sp)
	li	$2,-1			# 0xffffffffffffffff
	jr	$31
	addiu	$sp,$sp,40

$L2:
	move	$6,$18
	move	$5,$17
	jal	btc_fwrite
	sw	$2,16($sp)

	jal	btc_fclose
	lw	$4,16($sp)

	b	$L5
	lw	$31,36($sp)

	.set	macro
	.set	reorder
	.end	write_memory_to_file
	.size	write_memory_to_file, .-write_memory_to_file
	.section	.rodata.str1.4
	.align	2
$LC2:
	.ascii	"info::dump_dram_contents - s\000"
	.align	2
$LC3:
	.ascii	"info::dump_dram_contents - e\000"
	.align	2
$LC1:
	.ascii	"D:/dram_dump.bin\000"
	.text
	.align	2
	.globl	dump_dram_contents
	.set	nomips16
	.set	nomicromips
	.ent	dump_dram_contents
	.type	dump_dram_contents, @function
dump_dram_contents:
	.frame	$sp,48,$31		# vars= 24, regs= 1/0, args= 16, gp= 0
	.mask	0x80000000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-48
	lui	$5,%hi($LC1)
	li	$6,17			# 0x11
	addiu	$5,$5,%lo($LC1)
	sw	$31,44($sp)
	jal	memcpy
	addiu	$4,$sp,16

	lui	$4,%hi($LC2)
	jal	tty_printf
	addiu	$4,$4,%lo($LC2)

	li	$5,3276800			# 0x320000
	addiu	$6,$sp,16
	addiu	$5,$5,4512
	jal	write_memory_to_file
	li	$4,-2147483648			# 0xffffffff80000000

	lui	$4,%hi($LC3)
	jal	tty_printf
	addiu	$4,$4,%lo($LC3)

	lw	$31,44($sp)
	jr	$31
	addiu	$sp,$sp,48

	.set	macro
	.set	reorder
	.end	dump_dram_contents
	.size	dump_dram_contents, .-dump_dram_contents
	.section	.rodata.str1.4
	.align	2
$LC4:
	.ascii	"info::copy_file - s\012\000"
	.align	2
$LC5:
	.ascii	"error::copy_file - file len zero for %s\012\000"
	.align	2
$LC6:
	.ascii	"info::copy_file - %s size is %d\012\000"
	.align	2
$LC7:
	.ascii	"error::copy_file - can't open %s\012\000"
	.align	2
$LC8:
	.ascii	"  - deleting %s \012\000"
	.align	2
$LC9:
	.ascii	"  - copying %s to %s \012\000"
	.align	2
$LC10:
	.ascii	"error::copy_files - can't open %s\012\000"
	.align	2
$LC11:
	.ascii	"info::copy_file - e \012\000"
	.text
	.align	2
	.globl	copy_file
	.set	nomips16
	.set	nomicromips
	.ent	copy_file
	.type	copy_file, @function
copy_file:
	.frame	$sp,40,$31		# vars= 8, regs= 4/0, args= 16, gp= 0
	.mask	0x80070000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-40
	sw	$31,36($sp)
	sw	$17,28($sp)
	sw	$16,24($sp)
	move	$17,$4
	move	$16,$5
	jal	set_pre_printf_state
	sw	$18,32($sp)

	lui	$4,%hi($LC4)
	jal	tty_printf
	addiu	$4,$4,%lo($LC4)

	jal	check_post_printf_state_set_sio_params
	nop

	li	$5,16			# 0x10
	jal	vfsOpen
	move	$4,$17

	beq	$2,$0,$L9
	nop

	move	$4,$2
	jal	vfsFileSizeGet
	sw	$2,16($sp)

	lw	$4,16($sp)
	jal	vfsClose
	move	$18,$2

	bne	$18,$0,$L10
	nop

	jal	set_pre_printf_state
	nop

	move	$5,$17
$L19:
	lui	$4,%hi($LC5)
	jal	tty_printf
	addiu	$4,$4,%lo($LC5)

	lw	$31,36($sp)
$L20:
	lw	$18,32($sp)
	lw	$17,28($sp)
	lw	$16,24($sp)
	j	check_post_printf_state_set_sio_params
	addiu	$sp,$sp,40

$L10:
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC6)
	move	$6,$18
	move	$5,$17
	jal	tty_printf
	addiu	$4,$4,%lo($LC6)

$L16:
	jal	check_post_printf_state_set_sio_params
	nop

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC8)
	move	$5,$16
	jal	tty_printf
	addiu	$4,$4,%lo($LC8)

	jal	check_post_printf_state_set_sio_params
	nop

	jal	vfsFileDel
	move	$4,$16

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC9)
	move	$6,$16
	move	$5,$17
	jal	tty_printf
	addiu	$4,$4,%lo($LC9)

	jal	check_post_printf_state_set_sio_params
	nop

	move	$5,$16
	jal	vfsFileCopy
	move	$4,$17

	move	$4,$16
	jal	vfsOpen
	li	$5,16			# 0x10

	beq	$2,$0,$L12
	move	$4,$2

	jal	vfsFileSizeGet
	sw	$2,16($sp)

	lw	$4,16($sp)
	jal	vfsClose
	move	$17,$2

	bne	$17,$0,$L13
	nop

	jal	set_pre_printf_state
	nop

	b	$L19
	move	$5,$16

$L9:
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC7)
	move	$5,$17
	jal	tty_printf
	addiu	$4,$4,%lo($LC7)

	b	$L16
	nop

$L13:
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC6)
	move	$6,$17
	move	$5,$16
	jal	tty_printf
	addiu	$4,$4,%lo($LC6)

$L17:
	jal	check_post_printf_state_set_sio_params
	nop

	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC11)
	jal	tty_printf
	addiu	$4,$4,%lo($LC11)

	b	$L20
	lw	$31,36($sp)

$L12:
	jal	set_pre_printf_state
	nop

	lui	$4,%hi($LC10)
	move	$5,$16
	jal	tty_printf
	addiu	$4,$4,%lo($LC10)

	b	$L17
	nop

	.set	macro
	.set	reorder
	.end	copy_file
	.size	copy_file, .-copy_file
	.section	.rodata.str1.4
	.align	2
$LC12:
	.ascii	"A:\\RO_RES\\UI\\SST\\ENGLISH.SST\000"
	.align	2
$LC13:
	.ascii	"D:\\ENGLISH.SST\000"
	.align	2
$LC14:
	.ascii	"A:\\RO_RES\\UI\\SST\\ESPANOL.sst\000"
	.align	2
$LC15:
	.ascii	"D:\\ESPANOL.sst\000"
	.align	2
$LC16:
	.ascii	"A:\\RO_RES\\UI\\SST\\DEUTSCH.sst\000"
	.align	2
$LC17:
	.ascii	"D:\\DEUTSCH.sst\000"
	.align	2
$LC18:
	.ascii	"A:\\RO_RES\\UI\\SST\\DUTCH.sst\000"
	.align	2
$LC19:
	.ascii	"D:\\DUTCH.sst\000"
	.align	2
$LC20:
	.ascii	"A:\\RO_RES\\UI\\SST\\ITALIANO.sst\000"
	.align	2
$LC21:
	.ascii	"D:\\ITALIANO.sst\000"
	.align	2
$LC22:
	.ascii	"A:\\RO_RES\\UI\\SST\\FRANCIS.sst\000"
	.align	2
$LC23:
	.ascii	"D:\\FRANCIS.sst\000"
	.align	2
$LC24:
	.ascii	"A:\\RO_RES\\UI\\SST\\POLISH.sst\000"
	.align	2
$LC25:
	.ascii	"D:\\POLISH.sst\000"
	.text
	.align	2
	.globl	util_set_cold_item_language_id
	.set	nomips16
	.set	nomicromips
	.ent	util_set_cold_item_language_id
	.type	util_set_cold_item_language_id, @function
util_set_cold_item_language_id:
	.frame	$sp,24,$31		# vars= 0, regs= 2/0, args= 16, gp= 0
	.mask	0x80010000,-4
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	addiu	$sp,$sp,-24
	lui	$5,%hi($LC12)
	sw	$16,16($sp)
	move	$16,$4
	lui	$4,%hi($LC13)
	addiu	$5,$5,%lo($LC12)
	sw	$31,20($sp)
	jal	copy_file
	addiu	$4,$4,%lo($LC13)

	lui	$5,%hi($LC14)
	lui	$4,%hi($LC15)
	addiu	$5,$5,%lo($LC14)
	jal	copy_file
	addiu	$4,$4,%lo($LC15)

	lui	$5,%hi($LC16)
	lui	$4,%hi($LC17)
	addiu	$5,$5,%lo($LC16)
	jal	copy_file
	addiu	$4,$4,%lo($LC17)

	lui	$5,%hi($LC18)
	lui	$4,%hi($LC19)
	addiu	$5,$5,%lo($LC18)
	jal	copy_file
	addiu	$4,$4,%lo($LC19)

	lui	$5,%hi($LC20)
	lui	$4,%hi($LC21)
	addiu	$5,$5,%lo($LC20)
	jal	copy_file
	addiu	$4,$4,%lo($LC21)

	lui	$5,%hi($LC22)
	lui	$4,%hi($LC23)
	addiu	$5,$5,%lo($LC22)
	jal	copy_file
	addiu	$4,$4,%lo($LC23)

	lui	$5,%hi($LC24)
	lui	$4,%hi($LC25)
	addiu	$4,$4,%lo($LC25)
	jal	copy_file
	addiu	$5,$5,%lo($LC24)

	lw	$31,20($sp)
	move	$4,$16
	lw	$16,16($sp)
	j	set_cold_item_language_id
	addiu	$sp,$sp,24

	.set	macro
	.set	reorder
	.end	util_set_cold_item_language_id
	.size	util_set_cold_item_language_id, .-util_set_cold_item_language_id
	.align	2
	.globl	utilities_check_post_printf_hook
	.set	nomips16
	.set	nomicromips
	.ent	utilities_check_post_printf_hook
	.type	utilities_check_post_printf_hook, @function
utilities_check_post_printf_hook:
	.frame	$sp,0,$31		# vars= 0, regs= 0/0, args= 0, gp= 0
	.mask	0x00000000,0
	.fmask	0x00000000,0
	.set	noreorder
	.set	nomacro
	jr	$31
	nop

	.set	macro
	.set	reorder
	.end	utilities_check_post_printf_hook
	.size	utilities_check_post_printf_hook, .-utilities_check_post_printf_hook
	.ident	"GCC: (Ubuntu 9.4.0-1ubuntu1~20.04) 9.4.0"
