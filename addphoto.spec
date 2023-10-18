Name: addphoto
Version: 2.3
Release: alt1
Group: Graphics
License: GPL3
Packager: Vladislav Zavjalov <slazav@altlinux.org>
BuildArch: noarch

Summary: Scripts for making html photo albums

Source0: %name-%version.tar

%description
Scripts for making html photo albums

%prep
%setup

%build

%install
%makeinstall

%files
%_bindir/*

%changelog
* Wed Oct 18 2023 Vladislav Zavjalov <slazav@altlinux.org> 2.3-alt1
- This is a stable version currently used in slazav.xyz site.
  I have added a few new feactures recently, keeping it
  compatable with old files and parameters. Also it
  is moved to a separate gthub repo slazab/ph_scripts -> slazav/addphoto
  and renamed addphoto2 -> addphoto.
  I'm planning to start working on incompatable version 3.0.

* Mon Dec 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.3-alt1
- renames
- Makefile: fix installation
- ph_update_www:
  - add halo parameter
  - antialiasing in marks
  - name_m.png marks
  - remove old-style gif marks
  - fix work with files without paths
  - fix work with unexistent fields
- ph_resize:
  - fix parameter checking
- ph_exif:
  - human readable Exif.Photo.Flash values
  - more values
- addphoto:
  - add halo by default
  - fix html closing at \\end command
  - redirect output to stdout
- addphoto_cleanup:
  - treat index entries w/o extensions as a jpg-files
  - remove files at depth=1 only

* Fri Nov 13 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt1
- new scripts:
  pd_init, ph_canon_rename, ph_update_www, ph_exif,
  ph_addgeo, addphoto_mkfig, addphoto_cleanup
- rewrite on shell: addphoto, addphoto_ini
- cleanup all ph_* scripts, fix help messages
- add Readme files in core and pd directories
- spec: BuildArch: noarch
- don't use libshell
- fix Makefile

* Thu Oct 22 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt1
- core
  - addphoto
  - addphoto_ini
  - ph_size
  - ph_resize
  - ph_towww
