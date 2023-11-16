## addphoto -- Script for generating html with photos (for slazav.xyz site)

### Usage

`addphoto [options] [source file]`

Program reads a source file and creates html.

link: https://github.com/slazav/addphoto
author: Vladislav Zavjalov (vl.zavjalov at gmail.com), 2004?-2023

### Options

Options can be set in the command line, in configuration file
(see `--cfg` option) or in the input file (`\set` command).

*  `h|help`            -- print help message
*  `v|verbose:1`       -- be verbose
*  `I|init=s`          -- INIT MODE. Create a new source file. Argument is a folder with photos.
*  `J|init_only`       -- Same, but stop after creating the source file, do not make html.
*  `T|init_tsort:1`    -- init mode: sort photos by time
*  `d|init_days:1`     -- init mode: add day headers
*  `r|init_rec:1`      -- init mode: find files recursively
*  `w|init_width=i`    -- init mode: max page width
*  `init_img_mask=s`   -- init mode: regular expression for finding filenames with images.
                          Default: `(.jpe?g$)|(.png$)|(.tiff?$)|(.gif)$`
*  `O|opts:1`          -- Read file, print options and exit
*  `D|defs:1`          -- Read file, dum definitions and exit
*  `E|expand=s`        -- expand a string using variables defined in the file and exit
*  `C|cleanup`         -- CLEANUP MODE: remove unused files and exit
*  `f|force:1`         -- cleanup mode: do not ask before deleting files
*  `dryrun:1`          -- cleanup mode: do not delete files

Folders and files

*  `imgdir=s`        -- image dir, relative to source file location, default:
            input file name without last extension.
* `c|cfg=s` -- Configuration file name. This is used to read some options
before reading the input file. If empty, then `addphoto.cfg` or
`addphoto/addphoto.cfg` is used. The file should contain lines in the
form `[/<reg.ex.>/ ]<option name>[ <option value>]`. Ir regular
expression exists then the option is used only if sorce file name is matching.

*  `datadir=s` -- data dir (for *.js, *.css files), relative to source
file location, default: same as imgdir. If you have many texts it could be
better to use same datadir for all of them.

*  `H|html=s`  -- Name of html file, relative to source file location,
can contain folders. Default: input file name with last extension
replaces with `.htm`.

*  `html_filter=s` -- Filter for the main html file, for example `m4 defs.m4 -`

*  `html_stdout:1` -- Print the main html page to stdout instead of writing to
file. Name of the final file sould be anyway set with --html option, it
will be used for references in photo pages.

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
*  `html_headers:1`    -- generate html headers in the main page (default: 1)
*  `html_charset=s`    -- add meta charset tag in html pages
*  `html_viewport:1`   -- add meta viewport tag in html pages
*  `html_screen_sw:1`  -- add "fit to screen" switch to html pages
*  `html_arrows:1`     -- add navigation (ctrl-left/ctrl-right/esc buttons) to html pages
*  `html_resize:1`     -- resizable images in html pages (default state of "size" button)

*  `index_file=s` -- index file location (default: do not make index)
*  `index_only:1` -- stop after updating index
*  `index_ref=s`  -- string to be used in \ref, variables will be expanded using values from index

### File and directories

* Source file. It contains the album structure: list of images,
text, configuration. Name of the source file is taken from an argument
of the program. In init mode (-I,--init option) source file is created
(old one is moved to *.bak if it exists). In other modes the source file
should exist.

* Image folder. Folder for all album images and other files. It is
specified in --imgdir option as a relative path from location of the
source file. Default value is '.'. Paths of all album images are counted
from this folder.

If a folder name is given to a program instead of source file the Image
folder is set to this name and Index file name is foremed by adding .txt
to this name.

* HTML-file. File for html code of the album. File is always overwritten
by the program. Specified by --html option as a relative path counted
from location of the source file. Default name is created from the source
file name by removing last extension (if it exists) and adding '.htm'
instead.

* Image files. In init mode (-I,--init option) program finds and
write into the source file all image files located in the image folder
(default) and in all subfolders (with -r, --recursive option). In the
source file one can use any path to the image, relative to the image
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

* `\ctx [<name>]` -- Switch context.

### Init mode

A usual operation is to create folder with photos, run `addphoto -I <folder>`
to create a source file, and then edit it.

Related options:

Init mode.

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
are not needed.

Related options:
- `f|force:1` -- do not ask before deleting files
*  `dryrun:1` -- do not delete files

Files can be protected with `\keep <pattern> ...` command.
Patters are parsed with perl glob command. It can contain `*`, `?`, `{...}`.


### Headers and table of content

Headers are inserted with `\h(1|2|3|4) <title>` and `\h(1|2|3|4)r <title>` commands.
The second version (header with a ruler) is equivalent to the first one preceeded by `<hr>`.

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

- `ru`: Interface is in Russian, no tools for translation are available.
- `en`: Same for English.
- `select`: Switching RU/EN languages, file `addphoto_lang.js` is included.

You can use `RU{TEXT}` and `EN{TEXT}` macros to insert blocks of texts.

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
<title>${title}${author:+, }${author}</title>
\ifdef auth <meta name="Author" content="${author}">
...

\ctx begin
<div align=right>
  <u><span class="ru_control" id=lang_ru onclick="lang_set('ru')">ru</span></u>
  <u><span class="en_control" id=lang_en onclick="lang_set('en')">en</span></u>
</div>
<h2 align=center>${title}</h2>
\ifdef auth <h3 align=right>${auth}</h3>
```


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


### Definitions and text expansions

Variables can be defined with `\def <name> <value>` command.

After the definition following expansions are done:
- `${<name>}` expands to `<text>` if variable is defined and to empty string if not.
- `${<name>:-<word>}` expands to `<text>` if variable is defined and to `<word>` if not.
- `${<name>:+<word>}` expands to `<word>` if variable is defined and to empty string if not.

Pre-defined variables:
- `${INNAME}` -- name (without path) of the source file
- `${INBASE}` -- base name (without path and extension) of the source file

There are a few additional expansions:
- `WWW{TEXT}` is expanded to `<a href="TEXT">TEXT</a>`
- `RU{TEXT}` is expanded to `<span class=ru>TEXT</span>`
- `EN{TEXT}` is expanded to `<span class=en>TEXT</span>`

Variable names are used in `\ifdef <var_name> <text>` and `\ifndef
<var_name> <text>` commands.

Variables are used in indices (see below).


### Index

Index mechanism can be used to quickly obtain information about multiple
texts and to make links between them. There are three options which
control it:

* `index_file`. If it is empty (default) index is not used. Otherwise each
time addphoto process a text, it adds all variables defined in this text
to the index file.

* `index_only`. If set, then addphoto only updates index, without generating html pages.

* `index_ref`. It is a string which will be expanded in the `\ref` command.

If index is used, then `\ref <html_name>` command will be replaced with
`index_ref` string, expanded using definitions from the text
correspoinding to the html file.

Example. We have a few texts where we use some definitions, something
like `\def title ...`. We set `index_file index.txt`. When addphoto
processes each text, all definitions are added to the index file. We
also set `index_ref <li><a href="${INBASE}">${title}</a>` (it's
better to do in config file to prevent expansion of variables) and then
use `\ref <html_name>` if we want to put a link link to other text.


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
