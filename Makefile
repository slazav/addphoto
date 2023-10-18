bindir?=/usr/bin
INSTALL?=/usr/bin/install

SCRIPTS=\
  addphoto\
  addphoto_mkfig\
  ph_resize

all:

install:
	mkdir -p -- "$(bindir)"
	$(INSTALL) -Dpm 755 $(SCRIPTS) "$(bindir)"

