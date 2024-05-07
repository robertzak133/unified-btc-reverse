CDEFS=-DBTC_8E_HP5

IDIR   =../../../include
CIDIR  =../../../include
SRCDIR =../../../src
CC=mips-linux-gnu-gcc-9
AS=mips-linux-gnu-gcc-9
OBJDUMP=mips-linux-gnu-objdump
LD=mips-linux-gnu-ld
OBJCOPY=mips-linux-gnu-objcopy


CFLAGS=-I$(CIDIR) -Os -nostdlib -mno-abicalls -march=r4000 -EL -S
ASFLAGS=-march=r4000 -mno-abicalls  -c -EL
LDFLAGS=--warn-multiple-gp -G65535 --warn-section-align -EL 
OBJCPFLAGS=-S -O binary 

##_DEPS = WBWL.h
_DEPS = WBWL.h BTC.h SST-strings.h battery-monitor.h white-flash.h custom-ribbon.h custom-info-strip.h volume-file-naming.h dslr.h extend-event-SD-card.h rtc-formats.h timelapse.h aperture.h utilities.h aperture.h ir-flash-menu.h custom-set-date-time.h reduce-sd-clock.h 
# Unused Deps
# format-debug.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

##_SRC = entry.c
_SRC = entry0.c entry1.c entry2.c entry3.c entry4.c battery-monitor.c white-flash.c custom-ribbon.c custom-info-strip.c volume-file-naming.c dslr-trigger.c dslr.c no-dslr.c extend-event-SD-card.c rtc-formats.c menus.c timelapse.c utilities.c aperture.c aperture-menu.c ir-flash-menu.c ir-flash-menu-early.c custom-set-date-time.c reduce-sd-clock.c 
# Unused SRC
# format-debug.c
SRC = $(patsubst %,$(SRCDIR)/%,$(_SRC))

_SYMBOLS = $(_SRC:.c=.symbols)
SYMBOLS = $(SRC:.c=.symbols)

_release_OBJ = entry0.o entry1.o entry2.o entry3.o entry4.o custom-ribbon.o custom-info-strip.o volume-file-naming.o extend-event-SD-card.o rtc-formats.o dslr-trigger.o menus.o timelapse.o aperture.o aperture-menu.o ir-flash-menu.o ir-flash-menu-early.o custom-set-date-time.o reduce-sd-clock.o
_test_OBJ = entry0.o entry1.o entry2.o entry3.o entry4.o custom-ribbon.o custom-info-strip.o volume-file-naming.o extend-event-SD-card.o rtc-formats.o dslr-trigger.o menus.o timelapse.o aperture.o aperture-menu.o ir-flash-menu.o ir-flash-menu-early.o custom-set-date-time.o reduce-sd-clock.o 

# Unused Objects
#format-debug.o


# all the different binary bundles

_BIN = release.bin test.bin 

_BYTES = $(_BIN:.bin=.bytes)
_SYM = $(_BIN:.bin=.sym)


## Disable the Implicit rule which doesn't generate assembly code
%.o : %.c

## Explicit rules
## Note the complication introduced by putting all the files downstream
## of the src into the local directory; while fetching the source from 
## a (unidifed) source directory. Hence the magic use of $(@:$(SRCDIR)/%=%)
## for the destnation (vs. $@)
%.s : %.c $(DEPS)
	$(CC) $(CFLAGS) $(CDEFS) -o $(@:$(SRCDIR)/%=%) $<

%.o : %.s
	$(AS) $(ASFLAGS) $(<:$(SRCDIR)/%=%) -o $(@:$(SRCDIR)/%=%)

%.symbols : %.o 
	$(OBJDUMP) -t $(<:$(SRCDIR)/%=%) > $(@:$(SRCDIR)/%=%)

%.bytes : %.bin 
	$(OBJCOPY) $(OBJCPFLAGS) $< $@

%.sym   : %.bin
	$(OBJDUMP) -t $< > $@

## summary targets

part_1: $(SYMBOLS)
	touch part_1

#.PHONY: clean

.SECONDARY: $(OBJ)

## The rest are consolidated into release and test binaries

# Release
release.bin: $(_release_OBJ) general.cmd
	$(LD) $(LDFLAGS) -T general.cmd -o release.bin $(_release_OBJ) 

test.bin: $(_test_OBJ) general.cmd
	$(LD) $(LDFLAGS) -T general.cmd -o test.bin $(_test_OBJ) 

part_2: $(_BIN) $(_BYTES) $(_SYM)
	touch part_2


clean:
	rm -f *.s *.o *.symbols part_1 part_2

