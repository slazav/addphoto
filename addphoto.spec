Name: addphoto
Version: 3.0
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
* Sat Nov 18 2023 Vladislav Zavjalov <slazav@altlinux.org> 3.0-alt1
v3.0. Many changes, some are incompatable with previous versions
New features:
- Addphoto generates reasonable html header of the main html file.
- Contexts (\ctx command): adding text to different places (html headers, photo pages).
- Variables (\def command), ${name}, ${name:-...}, ${name:+...} expansions.
- RU{}, EN{}, WWW{}, NOHTM{}, ONLYRU{}, ONLYEN{} expansions.
- Index: collecting information from multiple files, references to other files, \ref command.
- Printing definitions and options, --defs, --opts --expand mode.
- Configuration files (addphoto.cfg or addphoto/addphoto.cfg)
- Add --datadir option (place for css and js files), it can be shared between multiple texts.
- rearrange js/css files, one file per feature.
- Syntax file for mcedit.
- Remove PhotoSwipe support (new version requires different code).
- Some options are removed, renames, changed.
- Html is always located near source file.
- Remove multiple spaces when joining lines.
- fix error with thumbnail dot updating an multi-images.
- use different colors for thumbnail dots (red for marks, magenta for multi-images).
- fix for new ImageMagick (problem with making marks).
- fix error in --html_filter option.
- fix error in --nohtml mode.

* Wed Oct 18 2023 Vladislav Zavjalov <slazav@altlinux.org> 2.3-alt1
- This is a stable version currently used in slazav.xyz site.
  I have added a few new features recently, keeping it
  compatible with old files and parameters. Also it
  is moved to a separate github repo slazab/ph_scripts -> slazav/addphoto
  and renamed addphoto2 -> addphoto.
  I'm planning to start working on incompatible version 3.0.

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
