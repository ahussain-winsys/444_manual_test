Q               := @
CC              := gcc -std=gnu99
SRCS            := $(wildcard *.c)
#OBJS_32         := $(SRCS:.c=.o32)
OBJS_64         := $(SRCS:.c=.o64)
#TARGET_32       := emuc_32
TARGET_64       := emuc_64
#LIBS_32         := lib_emuc2_32.a -m32 -lpthread -lm
LIBS_64         := lib_emuc2_64.a -march=armv8-a -lpthread -lm
#CFLAGS_32       := -m32 -Wall -I ./include
CFLAGS_64       := -march=armv8-a -Wall -I ./include
#LDFLAGS_32      := $(LIBS_32)
LDFLAGS_64      := $(LIBS_64)

############################################
LBITS           := $(shell getconf LONG_BIT)

.PHONY: all both clean

ifeq ($(LBITS),64)
    all: .depend $(TARGET_64)
else
    all: .depend $(TARGET_32)
endif

both: .depend $(TARGET_32) $(TARGET_64)
############################################

#%.o32: %.c Makefile
#	$(Q)echo "  Compiling '$<' ..."
#	$(Q)$(CC) $(CFLAGS_32) -o $@ -c $<

%.o64: %.c Makefile
	$(Q)echo "  Compiling '$<' ..."
	$(Q)$(CC) $(CFLAGS_64) -o $@ -c $<

#$(TARGET_32): $(OBJS_32)
#	$(Q)echo "  $(COLOR_G)Building '$@' VER=$(AP_VER)... $(COLOR_W)"
#	$(Q)$(CC) -o $@ $(OBJS_32) $(LDFLAGS_32)

$(TARGET_64): $(OBJS_64)
	$(Q)echo "  $(COLOR_G)Building '$@' VER=$(AP_VER)... $(COLOR_W)"
	$(Q)$(CC) -o $@ $(OBJS_64) $(LDFLAGS_64)

clean:
	$(Q)rm -f .depend *~ *.bak *.res *.o32 *.o64
	$(Q)echo "  Cleaning '$(TARGET_32)' ..."
	$(Q)rm -f $(TARGET_32)
	$(Q)echo "  Cleaning '$(TARGET_64)' ..."
	$(Q)rm -f $(TARGET_64)

.depend dep depend:
	$(Q)echo "  Generating '$@' ..."
#	$(Q)$(CC) $(CFLAGS_32) -M *.c > $@
	$(Q)$(CC) $(CFLAGS_64) -M *.c > $@

ifeq (.depend, $(wildcard .depend))
	include .depend
endif