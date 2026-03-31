---
title: "Kernel 8.0 Developerâ€™s Guide: Host Files User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Host Files"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - host
  - zish
  - table
  - contents
  - example
  - global
  - span
  - files
  - directory
  - open
page_count: 0
word_count: 3280
section_count: 12
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_host_files_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_host_files_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259329" class="anchor"></span>Host Files Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-host-files-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-host-files-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref454199809" class="anchor"></span>Table 1: Host File APIs—Definitions</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/28/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Host Files Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref454199809" class="anchor"></span>Table 1: Host File APIs—Definitions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc206857887" class="anchor"></span>List of Figures

<span id="_Toc206857888" class="anchor"></span>List of Tables

[Table 1: Host File APIs—Definitions [2](#_Ref454199809)](#_Ref454199809)

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-host-files-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [CLOSE^%ZISH(): Close Host File](#closezish-close-host-file)
    - [Example](#example)
  - [\$\$DEFDIR^%ZISH(): Get Default Host File Directory](#defdirzish-get-default-host-file-directory)
  - [\$\$DEL^%ZISH(): Delete Host File](#delzish-delete-host-file)
    - [Example](#example-1)
  - [\$\$FTG^%ZISH(): Load Host File into Global](#ftgzish-load-host-file-into-global)
    - [Example](#example-2)
  - [\$\$GATF^%ZISH(): Copy Global to Host File](#gatfzish-copy-global-to-host-file)
  - [\$\$GTF^%ZISH(): Copy Global to Host File](#gtfzish-copy-global-to-host-file)
    - [Example](#example-3)
  - [\$\$LIST^%ZISH(): List Directory](#listzish-list-directory)
    - [Example](#example-4)
  - [\$\$MV^%ZISH(): Rename Host File](#mvzish-rename-host-file)
    - [Example](#example-5)
  - [OPEN^%ZISH(): Open Host File](#openzish-open-host-file)
    - [Example](#example-6)
  - [\$\$PWD^%ZISH: Get Current Directory](#pwdzish-get-current-directory)
    - [Example](#example-7)
  - [\$\$STATUS^%ZISH: Return End-of-File Status](#statuszish-return-end-of-file-status)
    - [Example](#example-8)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Host Files Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Host Files APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

The traditional method of working with Host File System (HFS) files prior to Kernel 8.0 was to use the Device Handler API ([^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis)). Using several input parameters, you could open a Host file (given a Host file device entry in the DEVICE \[#3.5\] file). For example:

<span id="_Toc200269973" class="anchor"></span>Figure 1: Host Files—Opening a Host File Using the ^%ZIS API

S %ZIS("HFSNAME")="ARCHIVE.DAT"

S %ZIS("HFSMODE")="W"

S IOP="HFS" D ^%ZIS Q:POP

U IO D...

Kernel 8.0 provides a set of APIs for working with Host files. The Host file APIs and Extrinsic Functions are:

- [CLOSE^%ZISH](#closezish-close-host-file) Close Host file opened by OPEN^%ZISH.
- [\$\$DEL^%ZISH](#delzish-delete-host-file) Delete Host file.
- [\$\$FTG^%ZISH](#ftgzish-load-host-file-into-global) Copy lines from a Host file into a global.
- [\$\$GATF^%ZISH](#gatfzish-copy-global-to-host-file) pend records from a global to a Host file.
- [\$\$GTF^%ZISH](#gtfzish-copy-global-to-host-file) Copy records from a global into a Host file.
- [\$\$LIST^%ZISH](#listzish-list-directory) Get a list of files in a directory.
- [\$\$MV^%ZISH](#mvzish-rename-host-file) Rename Host file.
- [OPEN^%ZISH](#openzish-open-host-file) Open Host file (bypass Device Handler).
- [\$\$PWD^%ZISH](#pwdzish-get-current-directory) Get name of current directory.
- [\$\$STATUS^%ZISH](#statuszish-return-end-of-file-status) Return end-of-file status.

<u>Table 1</u> lists definitions that apply for the Host file APIs:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Path:</td>
<td><p>Full path specification up to but <em>not</em> including the filename. This includes any trailing slashes or brackets. If the operating system allows shortcuts, you can use them. Examples of valid paths include:</p>
<ul>
<li><blockquote>
<p>DOS c:\scratch\</p>
</blockquote></li>
<li><blockquote>
<p>UNIX /home/scratch/</p>
</blockquote></li>
<li><blockquote>
<p>VMS USER$:[SCRATCH]</p>
</blockquote></li>
</ul>
<p>To specify the current directory, use a path of <strong>NULL</strong> (“”).</p></td>
</tr>
<tr class="even">
<td>Filename:</td>
<td>Filename of the file only. Do <em>not</em> include device or directory specifications.</td>
</tr>
<tr class="odd">
<td>Access mode:</td>
<td><p>Access mode when opening files. It can be one of the following codes:</p>
<ul>
<li><blockquote>
<p><strong>R—READ</strong>; use the file for <strong>READ</strong>s only.</p>
</blockquote></li>
<li><blockquote>
<p><strong>W—WRITE</strong>; use the file for writing. If the file exists, it is truncated to a length of <strong>Zero</strong> (<strong>0</strong>) first. If the file does <em>not</em> exist, it is created.</p>
</blockquote></li>
<li><blockquote>
<p><strong>A—PEND</strong>; use the file for writing but start writing at the end of the current file. If the file does <em>not</em> exist, it is created.</p>
</blockquote></li>
<li><blockquote>
<p><strong>B—BINARY</strong> file.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

## CLOSE^%ZISH(): Close Host File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The CLOSE^%ZISH API closes a Host file that was opened with the <u>OPEN^%ZISH(): Open Host File</u> API.

Format: CLOSE^%ZISH(handle)

Input Parameters: handle: (required) Handle used when file was opened with the <u>OPEN^%ZISH(): Open Host File</u> API.

Output: none.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200269974" class="anchor"></span>Figure 2: CLOSE^%ZISH API—Example

D OPEN^%ZISH("OUTFILE","USER\$:\[ANONYMOUS\]","ARCHIVE.DAT","W")

Q:POP

U IO F I=1:1:100 W I,": ",ARRAY(I),!

D CLOSE^%ZISH("OUTFILE")

## \$\$DEFDIR^%ZISH(): Get Default Host File Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The \$\$DEFDIR^%ZISH extrinsic function gets the default Host file directory. It has two modes:

- NULL/Missing Parameter—If it is called with a NULL/missing parameter, it returns the “default directory for HFS files” from the KERNEL SYSTEM PARAMETERS (#8989.3) file.
- Directory Parameter—If it is called with a parameter, it *must* be the directory for a file. This parameter is checked to see that it is in the correct format for the operating system in question.

Format: \$\$DEFDIR^%ZISH(\[df\])

Input Parameters: df: (optional) This is the directory path upon which a simple format check is made. For the Windows operating system it changes / to \\ and makes sure that there is a trailing \\. There is no error response.

Output: returns: Returns the default Host file directory.

## \$\$DEL^%ZISH(): Delete Host File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The \$\$DEL^%ZISH extrinsic function deletes Host files. You can delete one or many Host files, depending on how you set up the array whose name you pass as the second input parameter.

Format: \$\$DEL^%ZISH(path,arrname)

Input Parameters: path: (required) Full path, up to but *not* including the filename.

arrname: (required) Fully resolved array name containing the files to delete as subscripts at the next descendent subscript level. For example, to delete two files, FILE1.DAT and FILE2.DAT, set up the array as:

ARRAY("FILE1.DAT")=""

ARRAY("FILE2.DAT")=""

Pass the array name ARRAY as the arrname parameter. Wildcard specifications *cannot* be used with this function.

Output: returns: Returns:

- 1—Success for all deletions.
- 0—Failure on at least one deletion.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950576" class="anchor"></span>Figure 3: \$\$DEL^%ZISH API—Example

\>K FILESPEC

\>S FILESPEC("TMP.DAT")=""

\>S Y=\$\$DEL^%ZISH("\MYDIR\\,\$NA(FILESPEC))

## \$\$FTG^%ZISH(): Load Host File into Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The \$\$FTG^%ZISH extrinsic function loads a Host file into a global. Each line of the Host file becomes the value of one node in the global. You do *not* need to open the Host file before making this call; it is opened and closed by \$\$FTG^%ZISH.

If a line from a Host file exceeds 255 characters in length, the overflows are stored in overflow nodes for that line, as follows:

> <span id="_Toc200269975" class="anchor"></span>Figure 4: Host Files—Overflow Lines in a Host File Sample

> ![](kernel-8-0-developer-s-guide-host-files-user-guide/004.png)

Format: \$\$FTG^%ZISH(path,filename,global_ref,inc_subscr\[,ovfsub\])

Input Parameters: path: (required) Full path, up to but *not* including the filename.

filename: (required) Name of the file to open.

global_ref: (required) Global reference to WRITE Host file to, in fully resolved (closed root) format. This function does *not*KILL the global before writing to it.

At least one subscript *must* be NUMERIC. This is the incrementing subscript (that is the subscript that \$\$FTG^%ZISH increments to store each new global node). This subscript need *not* be the final subscript. For example, to load into a WORD-PROCESSING field, the incrementing node is the second-to-last subscript; the final subscript is always Zero.

inc_subscr: (required) Identifies the incrementing subscript level. For example, if you pass ^TMP(115,1,1,0) as the global_ref parameter and pass 3 as the inc_subscr parameter, \$\$FTG^%ZISH increments the third subscript \[such as ^TMP(115,1,x)\], but WRITEs nodes at the full global reference \[such as ^TMP(115,1,x,0)\].

ovfsub: (optional) Name of subscript level at which overflow nodes for lines (if any) should be stored. Overflows occur if a line is greater than 255 characters. Further overflows occur for every additional 255 characters. The default subscript name at which overflows are stored for a line is “OVF”.

Output: returns: Returns:

- 1—Success.
- 0—Failure.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950578" class="anchor"></span>Figure 5: \$\$FTG^%ZISH API—Example

\>S Y=\$\$FTG^%ZISH("USER\$:\[COMMON\]","MYFILE.DAT",\$NA(^MYGLOBAL(612,1,0)),2)

## \$\$GATF^%ZISH(): Copy Global to Host File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The \$\$GATF^%ZISH extrinsic function is used in the same way as the <u>\$\$GTF^%ZISH(): Copy Global to Host File</u> API. The one difference is that if the file already exists, \$\$GATF^%ZISH appends global nodes to the existing file rather than truncating the existing file first.

![](kernel-8-0-developer-s-guide-host-files-user-guide/005.png) REF: For more information, see the <u>\$\$GTF^%ZISH(): Copy Global to Host File</u> API description.

Format: \$\$GATF^%ZISH(global_ref,inc_subscr,path,filename)

Input Parameters: global_ref: (required) Global to READ lines from, fully resolved in closed root form.

inc_subscr: (required) Identifies the incrementing subscript level. For example, if you pass ^TMP(115,1,1,0) as the global_ref parameter, and pass 3 as the inc_subscr parameter, \$\$GATF^%ZISH increments the third subscript \[such as ^TMP(115,1,x)\], but READs nodes at the full global reference \[such as ^TMP(115,1,x,0)\].

path: (required) Full path, up to but *not* including the filename.

filename: (required) Name of the file to open.

Output: returns: Returns:

- 1—Success.
- 0—Failure.

## \$\$GTF^%ZISH(): Copy Global to Host File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The \$\$GTF^%ZISH extrinsic function WRITEs the values of nodes in a global (at the subscript level you specify) to a Host file. If the Host file already exists, it is truncated to length Zero (0) before the copy. You do *not* need to open the Host file before making this call. The Host file is opened (in WRITE mode) and closed by \$\$GTF^%ZISH.

Format: \$\$GTF^%ZISH(global_ref,inc_subscr,path,filename)

Input Parameters: global_ref: (required) Global to READ lines from, fully resolved in closed root form.

inc_subscr: (required) Identifies the incrementing subscript level. For example, if you pass ^TMP(115,1,1,0) as the global_ref parameter, and pass 3 as the inc_subscr parameter, \$\$GTF^%ZISH increments the third subscript \[such as ^TMP(115,1,x)\], but READs nodes at the full global reference \[such as ^TMP(115,1,x,0)\].

path: (required) Full path, up to but *not* including the filename.

filename: (required) Name of the file to open.

Output: returns: Returns:

- 1—Success.
- 0—Failure.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950579" class="anchor"></span>Figure 6: \$\$GTF^%ZISH API—Example

\>S Y=\$\$GTF^%ZISH(\$NA(^MYGLOBAL(612,1,0)),2,"USER\$:\[COMMON\]","MYFILE.DAT")

## \$\$LIST^%ZISH(): List Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The \$\$LIST^%ZISH extrinsic function returns a list of file names in the current directory. The list is returned in an array in the variable named by the third parameter.

Format: \$\$LIST^%ZISH(path,arrname,retarrnam)

Input Parameters: path: (required) Full path, up to but *not* including any filename. For current directory, pass the NULL string.

arrname: (required) Fully resolved array name containing file specifications to list at the next descendent subscript level.

For example, to list all files, set one node in the named array, at subscript \*, equal to NULL. To list all files beginning with E and L, using the ARRAY array, set the nodes:

ARRAY("E\*")=""

ARRAY("L\*")=""

Pass the name “ARRAY” as the arrname parameter. You can use the asterisk wildcard in the file specification.

retarrnam: (required) Fully resolved array name to return the list of matching filenames. You should ordinarily KILL this array first (it is *not* purged by LIST^%ZISH).

Output Parameters:retarrnam: \$\$LIST^%ZISH populates the array named in the third input parameter with all matching files it finds in the directory you specify. It populates the array in the format:

ARRAY("filename1")=""

ARRAY("filename2")=""

(and so on)

Output: returns: Returns:

- 1—Success.
- 0—Failure.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950580" class="anchor"></span>Figure 7: \$\$LIST^%ZISH API—Example

\>K FILESPEC,FILE

\>S FILESPEC("L\*")="",FILESPEC("P\*")=""

\>S Y=\$\$LIST^%ZISH("","FILESPEC","FILE")

## \$\$MV^%ZISH(): Rename Host File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The \$\$MV^%ZISH extrinsic function renames a Host file. The function performs the renaming, regardless of the underlying operating system, by first copying the file to the new name/location and then deleting the original file at the old name/location.

Format: \$\$MV^%ZISH(\[path1,\]filename1\[,path2\],filename2)

Input Parameters: path1: (optional) Full path of the original file, up to but *not* including the filename. If NULL, it defaults to [\$\$DEFDIR^%ZISH](#defdirzish-get-default-host-file-directory).

filename1: (required) Name of the original file.

path2: (optional) Full path of renamed file, up to but *not* including the filename. If NULL, it defaults to [\$\$DEFDIR^%ZISH](#defdirzish-get-default-host-file-directory).

filename2: (required) Name of the renamed file.

Output: returns: Returns:

- 1—Success.
- 0—Failure.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950581" class="anchor"></span>Figure 8: \$\$MV^%ZISH API—Example

\>S Y=\$\$MV^%ZISH("","TMP.DAT","","ZXG"\_I\_".DAT")

## OPEN^%ZISH(): Open Host File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The OPEN^%ZISH API opens a Host file without using the Device Handler. You can use the device name returned in IO. You can then READ and WRITE from the opened Host file (depending on what access mode you used to open the file).

To close the Host file, use the CLOSE^%ZISH API with the handle you used to open the file.

Format: OPEN^%ZISH(\[handle\]\[,path,\]filename,mode\[,max\]\[,subtype\])

Input Parameters: handle: (optional) Unique name you supply to identify the opened device.

path: (optional) Full directory path, up to but *not* including the filename. If *not* supplied, the default HFS directory is used.

filename: (required) Name of the file to open.

mode: (required) Mode to open file:

- W—WRITE.
- R—READ.
- A—PEND.
- B—BLOCK (fixed record size).

max: (optional) Maximum record size for a new file.

subtype: (optional) File subtype.

Output Variables: POP: Returns the following values:

- Zero (0)—File was opened successfully.
- Positive Value—File was *not* opened.

IO: Name of the opened file in the format to use for M USE and CLOSE commands.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200269977" class="anchor"></span>Figure 9: OPEN^%ZISH API—Example

D OPEN^%ZISH("FILE1","USER\$:\[ANONYMOUS\]","ARCHIVE.DAT","A")

Q:POP

U IO F I=1:1:100 W I,": ",ARRAY(I),!

D CLOSE^%ZISH("FILE1")

## \$\$PWD^%ZISH: Get Current Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The \$\$PWD^%ZISH extrinsic function returns the name of the current working directory.

Format: \$\$PWD^%ZISH

Input Parameters: none.

Output: returns: Returns:

- String—The string representing the current directory specification, including device if any.
- NULL—If a problem occurs while retrieving the current directory.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950583" class="anchor"></span>Figure 10: \$\$PWD^%ZISH API—Example

\>S Y=\$\$PWD^%ZISH()

## \$\$STATUS^%ZISH: Return End-of-File Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Host Files

ICR \#: 2320

Description: The \$\$STATUS^%ZISH extrinsic function returns the current end-of-file status. If end-of-file has been reached, \$\$STATUS^%ZISH returns:

- 1—End-of-file (EOF) has been reached.
- 0—End-of-file (EOF) has *not* been reached.

Format: \$\$STATUS^%ZISH

Input Parameters: none.

Output: returns: Returns:

- 1—End-of-file (EOF) has been reached.
- 0—End-of-file (EOF) has *not* been reached.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200269978" class="anchor"></span>Figure 11: \$\$STATUS^%ZISH API—Example

D OPEN^%ZISH("INFILE","USER\$:\[ANONYMOUS\]","ZXG.DAT","R")

Q:POP

U IO F I=1:1 R X:DTIME Q:\$\$STATUS^%ZISH S ^TMP(\$J,"ZXG",I)=X

D CLOSE^%ZISH("INFILE")

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-host-files-user-guide/006.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-host-files-user-guide/007.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-host-files-user-guide/008.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.