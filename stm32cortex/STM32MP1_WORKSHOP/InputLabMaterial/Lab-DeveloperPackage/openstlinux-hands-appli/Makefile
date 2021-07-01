PROG = openstlinux-hands
SRCS = openstlinux-hands.c
OBJS = $(SRCS:.c=.o)

CLEANFILES = $(PROG)
DESTDIR ?= ./kernel_install_dir
bindir ?= /usr/local/bin

# Add / change option in CFLAGS if needed
# CFLAGS += <new option>

$(PROG): $(OBJS)
	$(CC) $(CFLAGS) -o $(PROG) $(OBJS)

.c.o:
	$(CC) $(CFLAGS) -c $< -o $@

all: $(PROG)

clean:
	rm -f $(CLEANFILES) $(patsubst %.c,%.o, $(SRCS)) *~

install: $(PROG)
	mkdir -p $(DESTDIR)$(bindir)
	install $(PROG) $(DESTDIR)$(bindir)
