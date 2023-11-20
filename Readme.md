## addphoto -- Script for generating html with photos (for slazav.xyz site)

link: https://github.com/slazav/addphoto

author: Vladislav Zavjalov (vl.zavjalov at gmail.com), 2004?-2023

### Usage

`addphoto [options] [source file]`

Program reads a source file and creates html.


### How to start

* Make a folder (`mytext`) and put some photos there.
* Run `addphoto -I mytext` to create template of a source file `mytxt.ph`
* Edit source file and run `addphoto mytxt.ph`

To run the scripts one should have following programs:

* `perl`
* `exiv2`
* `identify`, `mogrify`, `convert` from ImageMagick
* `fig2dev` from xfig -- if fig marks are used

Script `ph_resize` from this package is also needed. Normally it should be
installed in system path. If not, `--ph_resize` option can be used to
set path to this program.

### List of all options

Command line options:

*  `h|help`            -- print help message
*  `I|init=s`          -- INIT MODE. Create a new source file. Argument is a folder with photos.
*  `J|init_only`       -- Same, but stop after creating the source file, do not make html.
*  `O|opts:1`          -- Read file, print options and exit
*  `D|defs:1`          -- Read file, dum definitions and exit
*  `E|expand=s`        -- expand a string using variables defined in the file and exit
*  `C|cleanup`         -- CLEANUP MODE: remove unused files and exit
*  `index_only:1` -- stop after updating index (default: 0)

Other options can be set from command line, in configuration file
(see `--cfg` option) or in the input file (`\set` command).

*  `v|verbose:1`       -- be verbose
*  `T|init_tsort:1`    -- init mode: sort photos by time
*  `d|init_days:1`     -- init mode: add day headers
*  `r|init_rec:1`      -- init mode: find files recursively
*  `w|page_width=i`    -- Width of the main page. In the init mode images are arranged to
                          fit this width; max-width property of body of the main html page is
                          set to this value + 50px. If zet to 0, then page can be expanded to
                          any width. Default: 800.
*  `init_img_mask=s`   -- init mode: regular expression for finding filenames with images.
                          Default: `(.jpe?g$)|(.png$)|(.tiff?$)|(.gif)$`
*  `f|force:1`         -- cleanup mode: do not ask before deleting files
*  `dryrun:1`          -- cleanup mode: do not delete files

*  `imgdir=s` -- Image dir, relative to source file location, default:
source file name without last extension.

*  `datadir=s` -- data dir (for *.js, *.css files), relative to source
file location, default: same as imgdir. If you have many texts it could be
better to use same datadir for all of them.

* `c|cfg=s` -- Configuration file name. This is used to read some options
before reading the source file. If empty, then `addphoto.cfg` or
`addphoto/addphoto.cfg` is used. The file should contain lines in the
form `[/<reg.ex.>/ ]<option name>[ <option value>]`. If regular
expression exists then the option is used only if source file name is matching.

*  `ph_resize=s` -- path to `ph_resize` program. Default: `ph_resize`.

*  `H|html=s`  -- Name of html file, without any subdirectories.
Default: source file name with last extension replaced with `.htm`.

*  `html_filter=s` -- Filter for the main html file, for example `m4 defs.m4 -`

*  `html_stdout:1` -- Print the main html page to stdout instead of writing to
file. Name of the final file should be set anyway with html option, it
will be used for references in photo pages.

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
*  `quality=i`         -- Jpeg quality for thumbnails (default 90)
*  `map_ref=s`         -- Map link style (gmap, nakarte)
*  `map_zoom=i`        -- Map link zoom (default 6)
*  `fig_lang=s`        -- fig language
*  `fig_res=f`         -- fig resolution
*  `html_headers:1`    -- generate html headers in the main page (default: 1)
*  `html_charset=s`    -- add meta charset tag in html pages
*  `html_viewport:1`   -- add meta viewport tag in html pages
*  `html_screen_sw:1`  -- add "fit to screen" switch to html pages
*  `html_arrows:1`     -- add navigation (ctrl-left/ctrl-right/esc buttons) to html pages
*  `html_resize:1`     -- resizable images in html pages (default state of "size" button)
*  `index:1`           -- Use index (default: 0)

### File and directories

* Source file. It contains the album structure: list of images,
text, configuration. Name of the source file is taken from an argument
of the program. In init mode (-I,--init option) source file is created
(old one is moved to *.bak if it exists). In other modes the source file
should exist.

* HTML-file. File for the main html page, always located in the same
folder with source file. Specified by --html option. Default name is
created from the source file name by removing last extension (if it
exists) and adding '.htm' instead.

* Image folder. Folder for all album images and other files. It is
specified by --imgdir option as a relative path from location of the
source file. Default value is the source file name without extension.

* Data folder. Folder for js and css files. It is specified by --datadir
option as a relative path from location of the source file. Default
value is the source file name without extension. It could be reasonable
to share data folder between multiple texts, for example use `addphoto`
folder.

* Image files. In init mode (-I,--init option) program finds and
write into the source file all image files located in the image folder
(default) and in all subfolders (with -r, --recursive option). In the
source file one can use any path to the image, relative to the image
folder.

* Thumbnails. There are two sizes of thumbnail images. Names for
thumbnail images are made from image names by adding a prefix which can
be set by options --th1_pref (for small thumbnails), --th2_pref (for
large thumbnails). If the prefix ends with '/' then thumbnails are
located in a subfolder. Sizes of thumbnails are set by --th1_size and
--th2_size options (in W1:W2:W3 format, see ph_resize script).

* Marks. Marks are made from a fig file located near the image
file. Names for a mark image is made from the image name by adding a
prefix which can be set by options --mark_pref. If the prefix ends with
'/' then marks are locates in a subfolder.


### Source file syntax

Commands are started at the beginning of line with '\' symbol. Symbol '\' in
the beginning can be protected by putting another '\' in front of it.
Line can be joined with the next one by putting '\' at the end.
Other lines copied without changes. Commands:

* `\photo <file(s)> <title>` --
Insert an image. A thumbnail with caption is inserted in the text, with
a link to a separate html file with the full-size image. If a few
`\photo` lines are located together then thumbnails are aligned
horizontally. If there is an empty line or any other text, then a new
row of thumbnails is started. Filenames can not contain commas or
spaces. Relative paths are allowed if files are located in subfolders,
except paths with `..` components. A few filenames can be separated with commas,
to have switchable images.

* `\photo[r|l] <file(s)> <title>` -- Same, but thumbnail will be align to the right or left.

* `\h(1|2|3|4) <title>` -- Add header which will be used for making table of contents.

* `\h(1|2|3|4)r <title>` -- Add header with a ruler. This is equivalent to the previous command preceeded by `<hr>`.

* `\toc` -- Create table of contents using headers defined by `\h*` commands.

* `\end` -- Do not read rest of the file.

* `\#` -- Ignore the line.

* `\set` `<name>` `<value>` -- Set an option.

* `\keep <file pattern> ...` -- Keep additional files in the cleanup mode.

* `\def <name> <text>` -- Define a variable.

* `\inc <file_name>` -- Include a file.

* `\ifdef <var_name> <text>` -- Print the text if the variable is defined.

* `\ifndef <var_name> <text>` --- Print the text if the variable is not defined.

* `\ifeq <word1> <word2> <text>` -- Print the text if two words (without spaces) are equal.

* `\ifneq <word1> <word2> <text>` -- Print the text if two words (without spaces) are not equal.

* `\ctx [<name>]` -- Switch context (see Contexts section below).

* `\ref <html_name> <text>` -- reference to another file (see Index section below).


### Init mode

One can start working with addphoto by creating a folder with photos,
running `addphoto -I <folder>` to create a source file, and then editing
it.

Related options:

*  `I|init=s` -- Create a new source file, and make html page from it.
*  `J|init_only=s` -- Same, but exit after creating the source file.
*  `T|init_tsort:1`    -- init mode: sort photos by time
*  `d|init_days:1`     -- init mode: add day headers
*  `r|init_rec:1`      -- init mode: find files recursively
*  `w|init_width=i`    -- init mode: max page width
*  `init_img_mask=s`   -- init mode: regular expression for finding filenames with images.
                          Default: `(.jpe?g$)|(.png$)|(.tiff?$)|(.gif)$`

Argument of `--init` and `--init_only` is a folder with photos (imgdir).
In init mode giving name of source file is optional, its default value
is `<imgdir>.ph`.

### Cleanup mode

If `C|cleanup` option is given, the cleanup mode is activated:
After reading the source file addphoto calculates which files should exist
in the image folder and deletes all other files. By default, a list of files
is printed and confirmation is needed to delete them.

A usual workflow is to start with all photos, then remove unneeded lines
in the source file, then run `addphoto -C <file>` to remove photos which
are not used.

Related options:
- `f|force:1` -- do not ask before deleting files
*  `dryrun:1` -- do not delete files

Files can be protected with `\keep <pattern> ...` command.
Patters are parsed with perl glob command. It can contain `*`, `?`, `{...}`.


### Headers and table of content

Headers are inserted with `\h(1|2|3|4) <title>` and `\h(1|2|3|4)r <title>` commands.
The second variant (header with a ruler) is equivalent to the first one preceeded by `<hr>`.

Table of content is generated with `\toc` command.

If you want to exclude a header from the table of content, use plain html, e.g `<h3>...</h3>`

Example:
```
<h3>Table of Content</h3>
\toc
\h3r Header1
...
\h3r Header2
\h4 Header2.1
\h4 Header2.2
...
```

### Language support

Addphoto supports two languages, Russian and English. This includes
translation of the interface and some tools for switching languages. In
html switching is done by having `<span class=ru>...</span>` and `<span
class=en>...</span>` blocks and a javascript code (located in
`addphoto_lang.js`) for switching their visibility. "ru/en" switch is
located at the top of each page, key 't' can be also used for switching.

The option `lang` can have one of three values:

- `ru`: Interface is in Russian, no tools for switching languages are available.
- `en`: Same for English.
- `select`: Switching RU/EN languages, file `addphoto_lang.js` is included.

You can use `RU{TEXT}` and `EN{TEXT}` macros to insert blocks of texts.


### Contexts

Sometimes it is needed to add text to a certain part of html page.
This is done with context mechanism.

Context is switched with `\ctx [<name>]` command.

Possible context names:
  - (empty) - default context
  - `head`  - head section of the main html file,
  - `begin` - beginning of html body in the main file,
  - `end`   - end of html body in the main file,
  - `photo_head`  - head section of photo html pages
  - `photo_begin` - beginning of html body in photo pages
  - `photo_end`   - end of html body in photo pages
  - `none` - skip the text

Commands `\photo*`, `\h*`, `\toc`, `\inc` `\ref` are allowed only in the default context.


### Including files

It is possible to include files with `\inc <file_name>` command. Usually
it is useful to keep html headers and some definitions in a separate
file.

For example, one can have multiple texts starting with
```
\def title ...
\def author ...
\inc addphoto/headers.ph
...
```

And common file `addphoto/headers.ph` with
```
\ctx head
<title>NOHTML{${title}${author:+, }${author}}</title>
\ifdef auth <meta name="Author" content="NOHTML{${author}}">
...

\ctx begin
<h2 align=center>${title}</h2>
\ifdef auth <h3 align=right>${auth}</h3>
```

### Definitions and text expansions

Variables can be defined with `\def <name> <value>` command.

After the definition following expansions are done:
- `${<name>}` expands to `<text>` if variable is defined and to empty string if not.
- `${<name>:-<word>}` expands to `<text>` if variable is defined and to `<word>` if not.
- `${<name>:+<word>}` expands to `<word>` if variable is defined and to empty string if not.

Pre-defined variables:
- `${SRC_FILE}` -- name (without directories) of the source file
- `${SRC_BASE}` -- base name (without directories and last extension) of the source file

Variable names are used in `\ifdef <var_name> <text>` and `\ifndef
<var_name> <text>` commands.

Variables are used in indices (see Index section below).

There are a few additional expansions:
- `WWW{TEXT}` is expanded to `<a href="TEXT">TEXT</a>`
- `RU{TEXT}` is expanded to `<span class=ru>TEXT</span>`
- `EN{TEXT}` is expanded to `<span class=en>TEXT</span>`
- `ONLYRU{TEXT}`, `ONLYEN{TXT}` will remove all `<span class=ru>...</span>` constractions with non-ru/non-en languages.
- `NOHTML{TEXT}` will remove all html tags as well as angle brackets and single qoutes.

Note that order is important: `WWW` should be inside `RU`/`EN`, inside `ONLYRU`/`ONLYEN`, inside `NOHTML`.

Example:
```
\def title RU{...}EN{...}
\ctx head
<title>NOHTM{ONLYRU{${title}}</title>
\ctx
```

### Index

Index mechanism can be used to collect information about multiple html
pages and to make links between them.

If option `index:1` is set, then the index is updated: each time
addphoto creates an html page, it adds all variables defined in the
source file to the index file `addphoto.idx` which is located in the
same folder with html.

If option `index_only:1` is set, addphoto only updates index, without
generating html pages.

The `\ref <html_name> <text>` command will be replaced with `<text>`
expanded using definitions from external html file. `<html_name>` can
contain folders, in this case index file from this folder will be
loaded.   Symbol `@` is used instead of `$` for variable expansions,
`@{HTML}` will be replaced with `<html_name>`.

Example:
```
\def title ...
\def date ...
...
\def ref <a href="@{HTML}">@{title}@{date:+, }@{date}</a>
\ref file1.htm          <br>${ref}
\ref dir2/file2.htm     <br>${ref}
\ref ../dir3/file3.htm  <br>${ref}
```


### Additional scripts

* `addphoto_mkfig` -- Wrap image in a FIG file (useful for drawing marks
on the picture in xfig program). If file exists it is not modified. I
use this script togeter with `gqview` image viewer by adding to `.gqviewrc`
something like this:   `external_8: "fig" "file=%p; addphoto_mkfig $file;
xfig ${file%.*}.fig &"`

* `ph_resize` -- resize images

### mcedit syntax file

A syntax file for mcedit is available.

Add
```
file .\*\\.ph addphoto
include addphoto.syntax
```
to `Syntax` file in `~/.local/share/mc/syntax/` (copy from `/usr/share/mc/syntax/` if missing).

Put `addphoto.syntax` file to the same folder, edit it if needed.


