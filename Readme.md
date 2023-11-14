## addphoto -- Script for generating html with photos (for slazav.xyz site)

### Usage

`addphoto [options] [input file]`

Program reads input file and creates html.

link: https://github.com/slazav/addphoto

author: Vladislav Zavjalov (vl.zavjalov at gmail.com), 2004?-2023

### Options

Options can be used in command line or set in the input file by `\set` command.

*  `h|help`            -- print help message
*  `v|verbose:1`       -- be verbose

Init mode.

*  `I|init` --
  INIT MODE. In this mode a new index file is created with all images
  located in the image folder. Then the normal mode is started.
*  `J|init_only` --
  INIT MODE. Same as --init, but exit after creating the index file.
*  `T|init_tsort:1`    -- init mode: sort photos by time
*  `d|init_days:1`     -- init mode: add day headers
*  `r|init_rec:1`      -- init mode: find files recursively
*  `w|init_width=i`    -- init mode: max page width
*  `init_img_mask=s`   -- init mode: regular expression for finding filenames with images.
                          Default: `(.jpe?g$)|(.png$)|(.tiff?$)|(.gif)$`

Dump mode. Read a file and print different information. This could be
useful for collecting meta information from texts (if it is defined with
`\def` command), or for debugging.

*  `dump_opts:1`       -- DUMP options and exit
*  `dump_defs:1`       -- DUMP definitions and exit
*  `dump_inp:1`        -- DUMP input files and exit
*  `expand=s`          -- expand a string using variables defined in the file

Cleanup mode:

*  `C|cleanup`         -- CLEANUP MODE: remove unused files and exit
*  `f|force:1`         -- cleanup mode: do not ask before deleting files
*  `dryrun:1`          -- cleanup mode: do not delete files

Folders and output file

*  `D|imgdir=s` -- image dir, relative to index file location, default:
input file name without last extension.

* `c|cfg=s` -- Configuration file name. This is used to read some options
before reading the input file. If empty, then `.addphoto.cfg` or
`addphoto/addphoto.cfg` is used. The file should contain lines in the
form `<option name>[ <option value>]`.

*  `datadir=s` -- data dir (for *.js, *.css files), relative to index
file location, default: same as imgdir. If you have many texts it could be
better to use same datadir for all of them.

*  `H|html=s`  -- Name of html file, relative to index file location,
can contain folders. Default: input file name with last extension
replaces with `.htm`.

*  `html_filter=s` -- Filter for index html, for example `m4 defs.m4 -`

*  `html_stdout:1` -- Print index html to stdout instead of writing to
file. html option is still needed.

Other options

*  `th1_pref=s`        -- Small thumbnail prefix (can end with /), empty for no thumbnails
*  `th1_size=s`        -- Small thumbnail size (S1:S2:S3, see ph_resize)
*  `th1_rm_exif:1`     -- Remove exif-data from small thumbnails (default)
*  `th2_pref=s`        -- Large thumbnail prefix (can and with /), empty for no thumbnails
*  `th2_size=s`        -- Large thumbnail size (S1:S2:S3, see ph_resize)
*  `th2_rm_exif:1`     -- Remove exif-data from large thumbnails (default)
*  `mark_pref=s`       -- Image marks prefix (can contain /), empty for no marks
*  `html_pref=s`       -- Image marks prefix (can contain /), empty for no marks
*  `nohtml:1`          -- Do not generate hmtl pages for images
*  `mstyle=s`          -- Mark style
*  `l|lang=s`          -- Language (ru, en, select)
*  `pswp:1`            -- PhotoSwipe support
*  `quality=i`         -- Jpeg quality for thumbnails (default 90)
*  `map_ref=s`         -- Map link style (gmap, nakarte)
*  `map_zoom=i`        -- Map link zoom (default 6)
*  `fig_lang=s`        -- fig language
*  `fig_res=f`         -- fig resolution
*  `html_headers:1`    -- generate html headers in the index file (default: 1)
*  `html_charset=s`    -- add meta charset tag in html pages
*  `html_viewport:1`   -- add meta viewport tag in html pages
*  `html_screen_sw:1`  -- add "fit to screen" switch to html pages
*  `html_arrows:1`     -- add navigation (ctrl-left/ctrl-right/esc buttons) to html pages
*  `html_resize:1`     -- resizable images in html pages (default state of "size" button)

### File and directories

* Index file. It contains the album structure: list of images,
text, configuration. Name of index file is taken from an argument
of the program. In init mode (-I,--init option) index file is created
(old one is moved to *.bak if it exists). In other modes the index file
should exist.

* Image folder. Folder for all album images and other files. It is
specified in --imgdir option as a relative path from location of the
index file. Default value is '.'. Paths of all album images are counted
from this folder.

If a folder name is given to a program instead of index file the Image
folder is set to this name and Index file name is foremed by adding .txt
to this name.

* HTML-file. File for html code of the album. File is always overwritten
by the program. Specified by I<--html option as a relative path counted
from location of the index file. Default name is created from the index
file name by removing last extension (if it exists) and adding '.htm'
instead.

* Image files. In init mode (-I,--init option) program finds and
write into the index file all image files located in the image folder
(default) and in all subfolders (with -r, --recursive option). In the
index file one can use any path to the image, relative to the image
folder.

* Thumbnails. There are two sizes of thumbnail images. Names for
thumbnail images are made from image names by adding a prefix which can
be set by options --th1_pref (for small thumbnails), --th2_pref (for
large thumbnails). If the prefix ends with '/' then thumbnails are
locates in a subfolder. Sizes of thumbnails are set by --th1_size and
--th2_size options (in W1:W2:W3 format, see elsewhere).

* Marks. Marks are made from a fig file located near the image
file. Names for a mark image is made from the image name by adding a
prefix which can be set by options --mark_pref. If the prefix ends with
'/' then marks are locates in a subfolder.

### Input file syntax:

Commands are started at the beginning of line with '\' symbol. Symbol '\' in
the beginning can be protected by putting another '\' in front of it.
Line can be joined with the next one by putting '\' at the end.
Other lines copied without changes. Commands:

* `\photo` `<file(s)>` `<title>` --
Insert an image. A thumbnail with caption is inserted in the text, with
a link to a separate html file with the full-size image. If a few
`\photo` lines are located together then thumbnails are aligned
horizontally. If there is an empty line or any other text, then a new
row of thumbnails is started. Filenames can not contain commas or
spaces. Relative paths are allowed if files are located in subfolders,
except paths with `..` components. A few filenames can be separated with commas,
to have switchable images.

* `\photo[r|l]` `<file(s)>` `<title>` -- Same, but thumbnail
will be align to the right or left.

* `\h(1|2|3|4)` `<title>` --
Add header which will be used for making table of contents.

* `\h(1|2|3|4)r` `<title>` --
Add header with a ruler. This is equivalent to the previous command preceeded by `<hr>`.

* `\toc` --
Create table of contents using headers defined by `\h*` commands.

* `\end` --
Do not read rest of the file.

* `\#` --
Ignore the line.

* `\set` `<name>` `<value>` --
Set an option.

* `\keep` `<file pattern>` `...` --
Keep additional files in the cleanup mode.
patters are parsed with perl glob command. It can contain `*`, `?`, `{...}`.

* `\def` `<name>` `<text>` --
Define a variable. Later in the text following constructions can be used:
  - `${<name>}` expands to `<text>` if variable is defined and to empty string if not.
  - `${<name>:-<word>}` expands to `<text>` if variable is defined and to `<word>` if not.
  - `${<name>:+<word>}` expands to `<word>` if variable is defined and to empty string if not.
Pre-defined variables:
  - `${INNAME}` -- name (without path) of the input file
  - `${INBASE}` -- base name (without path and extension) of the input file

* `\inc` `<file name>` --
Include a file.

* `\ifdef` `<var_name>` `<text>` --
Put text if the variable is defined.

* `\ifndef` `<var_name>` `<text>` ---
Put text if the variable is not defined.

* `\ifeq` `<word1>` `<word2>` `<text>` --
Put text if two words (without spaces) are equal.

* `\ifneq` `<word1>` `<word2>` `<text>` --
Put text if two words (without spaces) are not equal.

* `ctx` `[<name>]` -- switch context. By using this command
you can put text into different parts of html. Possible context names:
  - (empty) - default context
  - `index_head`  - head section of the index file,
  - `index_begin` - beginning of html body in the index file,
  - `index_end`   - end of html body in the index file,
  - `photo_head`  - head section of photo pages
  - `photo_begin` - beginning of html body in photo pages
  - `photo_end`   - end of html body in photo pages
  - `none` - skip the text

Commands `\photo*`, `\h*`, `\toc`, `\inc` are allowed only in the default context.


### PhotoSwipe support

There is a possibility to use PhotoSwipe library for making
photo albums, but these options are not fully tested.

### Dependencies

To run the scripts one should have following programs:

* `perl`
* `exiv2`
* `identify`, `mogrify`, `convert` from ImageMagick
* `fig2dev` from xfig -- if fig marks are used

### Additional scripts

* `addphoto_mkfig` -- Wrap image in a FIG file (useful for drawing marks
on the picture in xfig program). If file exists it is not modified. I
use this script togeter with `gqview` image viewer by adding to `.gqviewrc`
something like this:   `external_8: "fig" "file=%p; addphoto_mkfig $file;
xfig ${file%.*}.fig &"`

* `ph_resize` -- resize images
