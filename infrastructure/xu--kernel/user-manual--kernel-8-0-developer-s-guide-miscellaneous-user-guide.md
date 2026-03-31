---
title: "Kernel 8.0 Developerâ€™s Guide: Miscellaneous User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Miscellaneous"
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
menu_options: 0
description: 
audience: 
keywords: 
  - span
  - table
  - class
  - contents
  - date
  - xuworkdy
  - guide
  - kernel
  - mark
  - miscellaneous
page_count: 0
word_count: 4077
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_miscellaneous_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_miscellaneous_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259460" class="anchor"></span>Miscellaneous Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref152655622" class="anchor"></span>Table 1: Miscellaneous Tools—Direct Mode Utilities</p></caption>
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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Miscellaneous Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref152655622" class="anchor"></span>Table 1: Miscellaneous Tools—Direct Mode Utilities

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc234301876" class="anchor"></span>List of Figures

<span id="_Toc207254781" class="anchor"></span>List of Tables

[Table 1: Miscellaneous Tools—Direct Mode Utilities [1](#_Ref152655622)](#_Ref152655622)

<span id="_Ref38421374" class="anchor"></span>

Orientation

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Developer Tools](#developer-tools)
  - [Direct Mode Utilities](#direct-mode-utilities)
  - [Programmer Options Menu](#programmer-options-menu)
    - [Delete Unreferenced Options](#delete-unreferenced-options)
    - [Global Block Count Option](#global-block-count-option)
    - [Listing Globals Option](#listing-globals-option)
    - [Test an option not in your menu Option](#test-an-option-not-in-your-menu-option)
  - [^%Z Editor](#z-editor)
    - [User Interface](#user-interface)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [Progress Bar Emulator](#progress-bar-emulator)
    - [INIT^XPDID: Progress Bar Emulator: Initialize Device and Draw Box Borders](#initxpdid-progress-bar-emulator-initialize-device-and-draw-box-borders)
    - [TITLE^XPDID(): Progress Bar Emulator: Display Title Text](#titlexpdid-progress-bar-emulator-display-title-text)
    - [EXIT^XPDID(): Progress Bar Emulator: Restore Screen, Clean Up Variables, and Display Text](#exitxpdid-progress-bar-emulator-restore-screen-clean-up-variables-and-display-text)
  - [Lookup Utility](#lookup-utility)
    - [\$\$EN^XUA4A71(): Convert String to Soundex](#enxua4a71-convert-string-to-soundex)
  - [Date Conversions and Calculations](#date-conversions-and-calculations)
    - [^XQDATE: Convert \$H to VA FileMan Format (Obsolete)](#xqdate-convert-h-to-va-fileman-format-obsolete)
    - [^XUWORKDY: Workday Calculation (Obsolete)](#xuworkdy-workday-calculation-obsolete)
    - [\$\$EN^XUWORKDY: Number of Workdays Calculation](#enxuworkdy-number-of-workdays-calculation)
    - [\$\$WORKDAY^XUWORKDY: Workday Validation](#workdayxuworkdy-workday-validation)
    - [\$\$WORKPLUS^XUWORKDY: Workday Offset Calculation](#workplusxuworkdy-workday-offset-calculation)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Miscellaneous Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Developer Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Kernel Toolkit direct mode utilities are available for developers to use at the M prompt, usually involving the DO command. They are *not* APIs and *cannot* be used in software application routines.

Many of the options on the Programmer Options menu can also be run as direct mode utilities. Some are *not* available as options, but only as direct mode utilities callable at the M prompt. <u>Table 1</u> lists examples on how to run these utilities when working in Programmer mode.

| Direct Mode Utility | Description                                  |
|---------------------|----------------------------------------------|
| \>D ^%G         | List the contents of a global to the screen. |

## Programmer Options Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181930" class="anchor"></span>Figure 1: Programmer Options Menu Options—Toolkit Miscellaneous Tools

SYSTEMS MANAGER MENU ... \[EVE\]

Programmer Options ... \<locked with XUPROG\> \[XUPROG\]

KIDS Kernel Installation & Distribution System ... \[XPD MAIN\]

\<locked with XUPROG\>

PG Programmer mode \<locked with XUPROGMODE\> \[XUPROGMODE\]

Calculate and Show Checksum Values \[XTSUMBLD-CHECK\]

<span class="mark">Delete Unreferenced Options \[XQ UNREF'D OPTIONS\]</span>

Error Processing ... \[XUERRS\]

General Parameter Tools ... \[XPAR MENU TOOLS\]

<span class="mark">Global Block Count \[XU BLOCK COUNT\]</span><span class="mark">List Global \<locked with XUPROGMODE\> \[XUPRGL\]</span>

Routine Tools ... \[XUPR-ROUTINE-TOOLS\]

<span class="mark">Test an option not in your menu \<locked with XUMGR\> \[XT-OPTION TEST\]</span>

### Delete Unreferenced Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete Unreferenced Options \[XQ UNREF’D OPTIONS\] option examines those options that are *not*:

- Located on any menu.
- Used as primary or secondary options.
- Tasked to run.

The user can then decide in each case whether to delete the unreferenced option.

### Global Block Count Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Global Block Count \[XU BLOCK COUNT\] option can be used to count the number of data blocks in a global.

### Listing Globals Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Global \[XUPRGL\] option is found on the Programmer Options menu, locked with the XUPROG security key. This option is also locked with the XUPROGMODE security key as an extra level of security.

It can be used to list the contents of a global to the screen. It makes use of operating system-specific utilities such as %G, the Global Lister.

The option is locked with the XUPROGMODE security key.

The corresponding direct mode utility can be used in Programmer mode. For example:

\>D ^%G (OS-specific)

### Test an option not in your menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Test an option *not* in your menu \[XT-OPTION TEST\] option for in-house testing of options only. It allows the selection of an option from the OPTION (#19 file) and then executes it. This option is locked with the XUMGR security key.

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/004.png) CAUTION: No security checks are performed in the XT-OPTION TEST option; therefore, it should only be given to programmers.

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/005.png) REF: Kernel Toolkit Application Programming Interfaces (APIs) are documented in the “<u>Toolkit: Developer Tools</u>” section. Kernel and Kernel Toolkit APIs are also available in HTML format on the VA Intranet website.

## ^%Z Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^%Z Editor (routine editor) is installed in the Manager account as the ^%Z global by ZTMGRSET during installation. (It can also be installed with D ^ZTEDIT.) To use the editor, load the routine (it *must* pre-exist) and then X ^%Z. The example in <u>Figure 148</u> creates a one-line routine in Caché and then calls the ^%Z Editor.

<span id="_Ref502841518" class="anchor"></span>Figure 2: Calling the ^%Z Editor—Sample User Entries

\><span class="mark">ZR \<Enter\></span>

\><span class="mark">ZZTEST \<Enter\></span> ;ID/SITE;test routine;

\><span class="mark">ZS ZZTEST \<Enter\></span>

\><span class="mark">ZL ZZTEST X ^%Z \<Enter\></span>

%Z Editing: ZZTEST Terminal type: C-VT100

Edit:

Enter .F (dot-file) at the edit prompt to change files. When saving with dot-file, an edit comment can be entered. This text is stored in the EDIT HISTORY (#23) Multiple field in the ROUTINE (#9.8) file as programmer documentation. <u>Figure 149</u> shows how an entire routine can be displayed by entering the ZP print command followed by a space at the M prompt. Dot-file (.File) is then used to file. A dot is then used to exit. (The dot exit does *not* automatically file changes.)

<span id="_Ref478386902" class="anchor"></span>Figure 3: ^%Z Editor—Displaying a Routine Using the ZP Command

\><span class="mark">ZL ZZTEST X ^%Z \<Enter\></span>

%Z Editing: ZZTEST Terminal type: C-VT100

Edit: <span class="mark">ZP\<SPACE\> \<Enter\></span>

ZZTEST ;test routine

Length: <span class="mark">20 \<Enter\></span> Line: <span class="mark">ZZTEST \<Enter\></span>

ZZTEST ;test routine

Edit: .Insert after: ZZTEST// <span class="mark">\<Enter\></span>

Line: <span class="mark">;NEXT LINE \<Enter\></span>

Line: <span class="mark">Q \<Enter\></span>

Line: <span class="mark">\<Enter\></span>

Edit: <span class="mark">.FILE ZZTEST \<Enter\></span>

Edit comment:

1\> <span class="mark">This text is stored in the Routine file's Edit History multiple. \<Enter\></span>

2\> <span class="mark">\<Enter\></span>

EDIT Option: <span class="mark">\<Enter\></span>

Edit: . <span class="mark">\<Enter\></span>

\>

Routines are filed by the name used when loading, *not* by the first line tag. If a ROUTINE (#9.8) file exists, then the routine is added if *not* already there, and an entry is made of the DATE/TIME and DUZ of the user that filed it. When filing, the editor updates the third piece of the first line of the routine with the DATE/TIME.

When editing, a question mark (?) can be entered to provide help. The dot commands are listed first. They provide the usual break, join, insert, and remove functions. The +n method of selecting lines to edit is also noted. The line tag can be used along with a number (such as TAG+3) to reach a particular line. A minus sign (-) backs up lines. And the asterisk (\*) can be entered to reach the last line.

<span id="_Toc193181933" class="anchor"></span>Figure 4: ^%Z Editor—Listing Edit Commands

\><span class="mark">X ^%Z \<Enter\></span>

Edit: <span class="mark">? \<Enter\></span>

.ACTION menu .BREAK line .CHANGE every

.FILE routine .INSERT after .JOIN lines

.MOVE lines .REMOVE lines .SEARCH for

.TERMinal type .XY change to/from replace-with

. -TO EXIT THE EDITOR

""+n Absolute line n +n To advance n lines -n To backup n lines\_

use '\*' to get last line

^NAME - to edit a GLOBAL node \*NAME - to edit a LOCAL variable

MUMPS command line (mumps command \<space\> or Z command \<space\>)

Help displays information about editing in line mode. A complete line is displayed, and various keys can be used to navigate. The \<Spacebar\> moves forward by words, the period moves forward by characters, and the \<CTRL H\> command key sequence moves backwards by characters. Upon reaching the desired location, the \<Delete\> key can be used to remove characters. To enter characters, the character E *must* first be entered as an insert/delete toggle. Pressing the \<Enter\> key reverses the toggle and allows navigation. Pressing the \<Enter\> key again moves back to the beginning of the line.

<span id="_Toc193181934" class="anchor"></span>Figure 5: ^%Z Editor—Line Mode Help Information

In the line mode,

Spacebar moves to the next space or comma. Dot to the next char.

'\>' To move forward 80 char or to end of line.

Backspace to back up one char. E to enter new char's at the cursor.

CR to exit enter mode, return to start of line or EDIT prompt.

D to delete from the cursor to the next space or comma.

Delete (Rub) to delete the char under the cursor.

CTRL-R to restore line and start back at the beginning.

Replace mode editing can be invoked by entering dot-XY at the edit prompt. This method allows easy string substitution, as in VA FileMan’s Line Editor. Entering a question mark at the next edit prompt displays the following help:

<span id="_Toc193181935" class="anchor"></span>Figure 6: ^%Z Editor—Replace Mode Editing Help Information

In the replace/with mode,

SPECIAL \<REPLACE\> STRINGS:

END -to add to the END of a line

... -to replace a line

A...B -to specify a string that begins with "A" and ends with "B"

A... -to specify a string that begins with "A" to the end of the line

CTRL-R to restore line.

The ACTION menu provides additional functions. Save and restore lines can be used to move lines within one routine or from one routine to another. To copy lines to another routine, first save the lines, then load and edit the other routine, and restore the lines.

When patching a routine, the ACTION menu can be used to calculate checksums. Before filing changes, the new checksum can be displayed and compared with the patch report for verification of editing. <u>Figure 7</u> shows how to reach the ACTION menu with dot-A (.A).

<span id="_Ref332260294" class="anchor"></span>Figure 7: ACTION Menu—Sample User Entries

Edit: <span class="mark">.A \<Enter\></span>

Action: <span class="mark">? \<Enter\></span>

Bytes in routine Checksum Restore lines

Save lines Version \#

Action: <span class="mark">C \<Enter\></span>

Checksum is 4971725

Action: <span class="mark">\<Enter\></span>

Edit: <span class="mark">\<Enter\></span>

Global nodes and local variables may also be edited with the ^%Z Editor. Editing occurs directly, so the idea of filing does *not* apply. The editor *must* then be exited with a dot, *not* with a dot-file, since filing should *not* take place.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are miscellaneous Kernel and Kernel Toolkit APIs and Extrinsic Functions available for developers. These APIs and Extrinsic Functions are described below.

## Progress Bar Emulator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following APIs can be used to emulate a KIDS Progress Bar outside of KIDS. To create the progress bar, you *must* first call the <u>INIT^XPDID: Progress Bar Emulator: Initialize Device and Draw Box Borders</u> API, and when you are finished, you *must* call the <u>EXIT^XPDID(): Progress Bar Emulator: Restore Screen, Clean Up Variables, and Display Text</u> API.

### INIT^XPDID: Progress Bar Emulator: Initialize Device and Draw Box Borders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Miscellaneous

ICR \#: 2172

Description: The INIT^XPDID API initializes the device, draws the borders for the progress bar box, and draws the progress bar. When you are finished, you *must* call the <u>EXIT^XPDID(): Progress Bar Emulator: Restore Screen, Clean Up Variables, and Display Text</u> API.

Format: INIT^XPDID

Input Parameters: none.

Output: returns: Returns XPDIDVT:

- 1—If output device supports graphics.
- 0—If output device does *not* support graphics.

### TITLE^XPDID(): Progress Bar Emulator: Display Title Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Miscellaneous

ICR \#: 2172

Description: The TITLE^XPDID API displays the text in the x input parameter as a title at the top of the progress bar box.

Format: TITLE^XPDID(x)

Input Parameters: x: (required) Title text to be displayed at the top of the box.

Output: none.

### EXIT^XPDID(): Progress Bar Emulator: Restore Screen, Clean Up Variables, and Display Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Miscellaneous

ICR \#: 2172

Description: The EXIT^XPDID API restores the screen to normal, cleans up all variables, and displays the text in the x input parameter.

Format: EXIT^XPDID(x)

Input Parameters: x: (required) Text to display on screen after removing box and progress bar.

Output: none.

## Lookup Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \$\$EN^XUA4A71(): Convert String to Soundex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Miscellaneous

ICR \#: 3178

Description: The \$\$EN^XUA4A71 extrinsic function converts a string into a NUMERIC representation of the string, using soundex methods. Soundex represents the phonetic properties of a string; its chief feature is that it assigns similar strings the same soundex representation.

Format: \$\$EN^XUA4A71(string)

Input Parameters: string: (required) String to convert into soundex form.

Output: returns: Returns the soundex version of the string.

## Date Conversions and Calculations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ^XQDATE: Convert \$H to VA FileMan Format (Obsolete)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/006.png) NOTE: The ^XQDATE API is obsolete. You should use either of the following APIs instead:

- [\$\$FMTE^XLFDT(): Convert VA FileMan Date to External Format](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xlf_fl_ug.pdf#fmte_xlfdt)
- [\$\$HTFM^XLFDT(): Convert \$H to VA FileMan Date Format](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xlf_fl_ug.pdf#htfm_xlfdt)

Reference Type: Supported

Category: Miscellaneous

ICR \#: 10079

Description: The ^XQDATE API converts \$H formatted input date to a VA FileMan formatted date in %, and in human readable format (such as Jan. 9, 1990 1:37 PM) in %Y variable.

Format: ^XQDATE

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
2.  Set all input variables.
3.  Call the API.

Input Variable s: XQD1: (optional) If this variable is *not* set, the system uses \$H.

Output Variables: %: Returns the converted \$H date in VA FileMan format.

%Y: Returns the converted \$H date, in human readable format.

### ^XUWORKDY: Workday Calculation (Obsolete)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/007.png) NOTE: Calling the XUWORKDY routine from the top is obsolete. The ^XUWORKDY API was replaced by the [\$\$EN^XUWORKDY](#enxuworkdy-number-of-workdays-calculation) API. This API is dependent on the HOLIDAY (#40.5) file being updated by the sites.

Reference Type: Supported

Category: Miscellaneous

ICR \#: 10046

Description: To use the ^XUWORKDY APIs, you *must* make sure that HOLIDAY (#40.5) file is populated with each year’s holidays for the workday calculation to work correctly. If it is *not* populated, you need to populate it yourself (Kernel distributes this file without data). Only enter holidays that fall on weekdays, however.

You can call the ^XUWORKDY routine to calculate the number of workdays between two dates (X, X1). It returns a positive value if X\<X1 and a negative value if X\>X1. If either date is imprecisely specified, or if the HOLIDAY global is empty, then ^XUWORKDY returns a NULL string.

- The first FOR loop in ^XUWORKDY checks the HOLIDAY global and sets %H equal to the number of holidays between the two dates. It is assumed that the HOLIDAY global contains only weekday holidays.
- The second FOR loop (F %J=%J:1 ... ) steps forward from the earliest date and stops at the first Sunday or at the ending date (whichever comes first) counting the number of workdays.
- The third FOR loop (F %K=%K:-1 ... ) steps backward from the latest date and stops at the first Sunday or at the beginning date (whichever comes first), counting the workdays.
- Then %I is set equal to the number of days between the two Sundays.
- Finally, X is set equal to the total counted days minus the number of weekend days between the two Sundays ( -(%I\7\*2) ).

Format: ^XUWORKDY

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
4.  Set all input variables.
5.  Call the API.

Input Variables: X: (required) Starting date in VA FileMan internal format (such as 2850420).

X1: (required) Ending date in VA FileMan internal format (such as 2850707).

Output: X: The number of workdays in the interval.

#### Example

<span id="_Toc199950656" class="anchor"></span>Figure 8: ^XUWORKDY API—Example

\><span class="mark">S X=2850420,X1=2850707 D ^XUWORKDY W X</span>

55

### \$\$EN^XUWORKDY: Number of Workdays Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/008.png) NOTE: This API is dependent on the HOLIDAY (#40.5) file being updated by the sites.

Reference Type: Supported

Category: Miscellaneous

ICR \#: 10046

Description: To use the ^XUWORKDY APIs, you *must* make sure that HOLIDAY (#40.5) file is populated with each year’s holidays for the workday calculation to work correctly. If it is *not* populated, you need to populate it yourself (Kernel distributes this file without data). Only enter holidays that fall on weekdays, however.

The \$\$EN^XUWORKDY extrinsic function calculates the number of workdays between two dates (date1, date2). It returns:

- Positive Value—If date1\<date2.
- Negative Value—If date1\>date2.
- NULL String—If either date is imprecisely specified, or if the HOLIDAY global is empty.

The first FOR loop in ^XUWORKDY checks the HOLIDAY global and sets %H equal to the number of holidays between the two dates. It is assumed that the HOLIDAY global contains only weekday holidays.

The second FOR loop (F %J=%J:1 ... ) steps forward from the earliest date and stops at the first Sunday or at the ending date (whichever comes first) counting the number of workdays.

The third FOR loop (F %K=%K:-1 ... ) steps backward from the latest date and stops at the first Sunday or at the beginning date (whichever comes first), counting the workdays.

Then %I is set equal to the number of days between the two Sundays.

Finally, the return value is set equal to the total counted days minus the number of weekend days between the two Sundays \[ -(%I\7\*2) \].

Format: \$\$EN^XUWORKDY(date1,date2)

Input Parameters: date1: (required) Starting date in VA FileMan internal format (such as 2850420).

date2: (required) Ending date in VA FileMan internal format (such as 2850707).

Output: returns: Returns the number of workdays in the interval.

#### Example

<span id="_Toc199950657" class="anchor"></span>Figure 9: \$\$EN^XUWORKDY API—Example

\><span class="mark">W \$\$EN^XUWORKDY(3090102,3090108)</span>

4

### \$\$WORKDAY^XUWORKDY: Workday Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/009.png) NOTE: This API is dependent on the HOLIDAY (#40.5) file being updated by the sites.

Reference Type: Supported

Category: Miscellaneous

ICR \#: 10046

Description: To use the ^XUWORKDY APIs, you *must* make sure that HOLIDAY (#40.5) file is populated with each year’s holidays for the workday calculation to work correctly. If it is *not* populated, you need to populate it yourself (Kernel distributes this file without data). Only enter holidays that fall on weekdays, however.

The \$\$WORKDAY^XUWORKDY extrinsic function returns:

- 1—If the date submitted is a workday.
- 0—If the date submitted is *not* a workday.

If the date is imprecisely specified, or if the HOLIDAY global is empty, then \$\$WORKDAY^XUWORKDY returns a NULL string.

Format: \$\$WORKDAY^XUWORKDY(date)

Input Parameters: date: (required) Starting date in VA FileMan internal format returns: (such as 2850420).

Output: returns: Returns:

- 1—Workday
- 0—*Non*-Workday

#### Examples

#### Example 1

Figure 10 shows the return value when a workday in VA FileMan internal format is input:

<span id="_Ref499818297" class="anchor"></span>Figure 10: \$\$WORKDAY^XUWORKDY API—Example 1

\><span class="mark">W \$\$WORKDAY^XUWORKDY(3090102)</span>

1

#### Example 2

<u>Figure 11</u> shows the return value when a *non*-workday in VA FileMan internal format is input:

<span id="_Ref499818309" class="anchor"></span>Figure 11: \$\$WORKDAY^XUWORKDY API—Example 2

\><span class="mark">W \$\$WORKDAY^XUWORKDY(3090103)</span>

0

### \$\$WORKPLUS^XUWORKDY: Workday Offset Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/010.png) NOTE: This API is dependent on the HOLIDAY (#40.5) file being updated by the sites.

Reference Type: Supported

Category: Miscellaneous

ICR \#: 10046

Description: To use the ^XUWORKDY APIs, you *must* make sure that HOLIDAY (#40.5) file is populated with each year’s holidays for the workday calculation to work correctly. If it is *not* populated, you need to populate it yourself (Kernel distributes this file without data). Only enter holidays that fall on weekdays, however.

The \$\$WORKPLUS^XUWORKDY extrinsic function returns the date that is n working days (that is offset) +/- of the input date. If the date is imprecisely specified, or if the HOLIDAY global is empty, then \$\$WORKPLUS^XUWORKDY returns a NULL string.

Format: \$\$WORKPLUS^XUWORKDY(date,offset)

Input Parameters: date: (required) Starting date in VA FileMan internal format (such as 2850420).

offset: (required) The number of days to offset.

Output: returns: Returns the date in VA FileMan internal format that is n working days (that is offset) +/- of the input date.

#### Example

<span id="_Toc199950660" class="anchor"></span>Figure 12: \$\$WORKPLUS^XUWORKDY API—Example

\><span class="mark">W \$\$WORKPLUS^XUWORKDY(3090108,3)</span>

3090113

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/011.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/012.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-miscellaneous-user-guide/013.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.