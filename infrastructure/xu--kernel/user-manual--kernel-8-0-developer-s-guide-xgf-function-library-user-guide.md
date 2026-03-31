---
title: "Kernel 8.0 Developerâ€™s Guide: XGF Function Library User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: XGF Function Library"
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
  - function
  - table
  - guide
  - contents
  - library
  - class
  - example
  - keyboard
  - kernel
page_count: 0
word_count: 6179
section_count: 18
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xgf_fl_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xgf_fl_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259749" class="anchor"></span>XGF Function Library Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref503172049" class="anchor"></span>Table 1: XGF Function Library—Minimum M Implementation Features Required</p></caption>
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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: XGF Function Library Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref503172049" class="anchor"></span>Table 1: XGF Function Library—Minimum M Implementation Features Required

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc207256157" class="anchor"></span>List of Figures

<span id="_Toc207256158" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Direct Mode Utilities](#direct-mode-utilities)
  - [^XGFDEMO: Demo Program](#xgfdemo-demo-program)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [CHGA^XGF(): Screen Change Attributes](#chgaxgf-screen-change-attributes)
    - [Examples](#examples)
  - [CLEAN^XGF: Screen/Keyboard Exit and Cleanup](#cleanxgf-screenkeyboard-exit-and-cleanup)
  - [CLEAR^XGF(): Screen Clear Region](#clearxgf-screen-clear-region)
    - [Examples](#examples-1)
  - [FRAME^XGF(): Screen Frame](#framexgf-screen-frame)
    - [Example](#example)
  - [INITKB^XGF(): Keyboard Setup Only](#initkbxgf-keyboard-setup-only)
  - [IOXY^XGF(): Screen Cursor Placement](#ioxyxgf-screen-cursor-placement)
    - [Example](#example-1)
  - [PREP^XGF(): Screen/Keyboard Setup](#prepxgf-screenkeyboard-setup)
  - [\$\$READ^XGF(): Read Using Escape Processing](#readxgf-read-using-escape-processing)
    - [Examples](#examples-2)
  - [RESETKB^XGF: Exit XGF Keyboard](#resetkbxgf-exit-xgf-keyboard)
  - [RESTORE^XGF(): Screen Restore](#restorexgf-screen-restore)
    - [Example](#example-2)
  - [SAVE^XGF(): Screen Save](#savexgf-screen-save)
    - [Example](#example-3)
  - [SAY^XGF(): Screen String](#sayxgf-screen-string)
    - [Examples](#examples-3)
  - [SAYU^XGF(): Screen String with Attributes](#sayuxgf-screen-string-with-attributes)
    - [Example](#example-4)
  - [SETA^XGF(): Screen Video Attributes](#setaxgf-screen-video-attributes)
    - [Example](#example-5)
  - [WIN^XGF(): Screen Text Window](#winxgf-screen-text-window)
    - [Examples](#examples-4)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: XGF Function Library Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XGF Function Library supports developers designing text-based applications. The functions in this library support cursor positioning, overlapping text windows, video attribute control, and keyboard escape processing, all in a text-mode environment.

If you intend to make simple interface enhancements for an existing text-mode application, then you may find the XGF Function Library useful. The XGF Function Library provides the following functionality:

- Text-mode overlapping windows.
- Text-mode cursor positioning by screen coordinate.
- Text-mode video attribute control (bold, blink, and so on).
- Keyboard reader using M escape processing (thereby making use of keystrokes like \<UP-ARROW\> (“↑”), \<DOWN-ARROW\> (“↓”), \<PREV\> (“←”), \<NEXT\> (“→”), and so on).

The XGF Function Library may *not* be appropriate if you need:

- A full graphical user interface (GUI) front end for your application.
- Support for *non*-ANSI VT-compatible display devices.

To use the XGF Function Library, your system *must* use an M implementation that complies with the 1995 ANSI M standard. At a minimum, the M implementation *must* support the features listed in <u>Table 1</u> to use the XGF Function Library:

| Feature                     | Example                                      |
|-----------------------------|----------------------------------------------|
| SET into \$EXTRACT  | S X="this is a string",\$E(X,1,4)="that" |
| Reverse \$ORDER         | S X=\$O(^TMP(""),-1)                     |
| Two argument \$GET      | K Y S X=\$G(Y,"DEFAULT")                 |
| Skipping parameters         | D TAG^ROUTINE(,P2,,P4)                   |
| \$NAME                  | W \$NA(^TMP(\$J))                        |
| SET\$X and \$Y | S \$X=10                                 |

<span id="_Toc200270063" class="anchor"></span>Table 2: XGF Function Library—Demo Functional Division

This XGF Function Library supports terminals that are ANSI-compatible and at least VT100-compatible. As a result, this software does *not* support QUME QVT102/QVT102A terminals.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/004.png) REF: Kernel and Kernel Toolkit APIs are also available in HTML format on the VA Intranet Website.

# Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several XGF Function Library direct mode utilities are available for developers to use at the M prompt. They are *not* APIs and *cannot* be used in software application routines. These direct mode utilities are described below.

## ^XGFDEMO: Demo Program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run an interactive demonstration showing the capabilities provided by the XGF Function Library, you can run the XGF demo program. From the Programmer prompt, type the following:

\>D ^XGFDEMO

<table>
<caption><blockquote>
<p><span id="_Ref502655836" class="anchor"></span>Table 3: XGF Function Library—Mnemonics for Keys that Terminate READs</p>
</blockquote></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Demo Function</th>
<th>Associated Direct Mode Utility</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Cursor/Text Output</td>
<td><p><strong>IOXY^XGF</strong></p>
<p><strong>SAY^XGF</strong></p>
<p><strong>SAYU^XGF</strong></p></td>
</tr>
<tr class="even">
<td>Video Attributes</td>
<td><p><strong>CHGA^XGF</strong></p>
<p><strong>SETA^XGF</strong></p></td>
</tr>
<tr class="odd">
<td>Text Windows</td>
<td><p><strong>CLEAR^XGF</strong></p>
<p><strong>FRAME^XGF</strong></p>
<p><strong>RESTORE^XGF</strong></p>
<p><strong>SAVE^XGF</strong></p>
<p><strong>WIN^XGF</strong></p></td>
</tr>
<tr class="even">
<td>Keyboard Reader</td>
<td><strong>$$READ^XGF</strong></td>
</tr>
<tr class="odd">
<td>Setup/Cleanup</td>
<td><p><strong>CLEAN^XGF</strong></p>
<p><strong>INITKB^XGF</strong></p>
<p><strong>PREP^XGF</strong></p>
<p><strong>RESETKB^XGF</strong></p></td>
</tr>
</tbody>
</table>

<span id="_Ref502655836" class="anchor"></span>Table 3: XGF Function Library—Mnemonics for Keys that Terminate READs

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several XGF Function Library APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## CHGA^XGF(): Screen Change Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The CHGA^XGF API changes individual video attributes for subsequent screen WRITEs.

Use this API to change individual video attributes for subsequent output. This API is different from <u>SETA^XGF</u> in that individual video attributes can be set without affecting all video attributes at once.

A call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point prior to calling CHGA^XGF.

The attribute codes are *not* case sensitive. You can append them if you want to set more than one attribute. If you include more than one attribute, their order is *not* important:

- B0 and B1 turn off and on the blink attribute.
- I0 and I1 turn off and on the intensity attribute.
- R0 and R1 turn off and on the reverse attribute.
- U0 and U1 turn off and on the underline attribute.
- E1 turns off all attributes.
- G0 and G1 turn off and on recognition of an alternate graphics character set, so that you can use special graphic characters, particularly those set up by Kernel’s [GSET^%ZISS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#gset_ziss) API. To use graphics characters, be sure you turn on graphics first (with G1) and turn graphics off afterwards (with G0).

The change in attribute remains in effect until another CHGA^XGF, <u>PREP^XGF(): Screen/Keyboard Setup</u>, or <u>SETA^XGF(): Screen Video Attributes</u> API call is made. If you want only a temporary change in attribute, <u>SAY^XGF</u> may be a better function to use.

Format: CHGA^XGF(atr_codes)

Input Parameters: atr<u>\_</u>codes: (required) Codes are as follows:

- B1—Blink on.  
  > B0—Blink off.
- E1—Turn all off.
- G1—Graphics on.  
  > G0—Graphics off.
- I1—Intensity high.  
  > I0—Intensity normal.
- R1—Reverse video on.  
  > R0—Reverse video off.
- U1—Underline on.  
  > U0—Underline off.

Output Parameters: xgcuratr: This variable always holds the current screen attribute coded as a single character and is updated when you call CHGA^XGF.

\$x,\$y: Left unchanged.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/005.png) REF: See also: <u>SETA^XGF(): Screen Video Attributes</u> API.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

To clear the screen in blinking, reverse video and high intensity, do the following:

<span id="_Toc199950816" class="anchor"></span>Figure 1: CHGA^XGF API—Example 1

\><span class="mark">D CHGA^XGF("R1B1I1"),CLEAR^XGF(0,0,23,79)</span>

#### Example 2

To print Hello World, do the following:

<span id="_Toc199950817" class="anchor"></span>Figure 2: CHGA^XGF API—Example 2

\><span class="mark">D CHGA^XGF("I1"),SAY^XGF(,,"Hello ")</span>

\><span class="mark">D CHGA^XGF("U1"),SAY^XGF(,,"World")</span>

#### Example 3

To draw the bottom of a small box, do the following:

<span id="_Toc199950818" class="anchor"></span>Figure 3: CHGA^XGF API—Example 3

\><span class="mark">D CHGA^XGF("G1")</span>

\><span class="mark">D SAY^XGF(,,IOBLC_IOHL_IOHL_IOBRC)</span>

\><span class="mark">D CHGA^XGF("G0")</span>

## CLEAN^XGF: Screen/Keyboard Exit and Cleanup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The CLEAN^XGF API exits the XGF screen and keyboard environments. It does the following:

- Removes XGF screen and keyboard variables and tables.
- Turns all video attributes off.
- Turns echo on.
- Turns the cursor on.
- Sets the keypad to numeric mode.

In addition, CLEAN^XGF does everything that the <u>RESETKB^XGF: Exit XGF Keyboard</u> API does to exit the XGF keyboard environment, including turning terminators and escape processing off. Subsequent READs are processed normally. If you call CLEAN^XGF, a separate call to the <u>RESETKB^XGF: Exit XGF Keyboard</u> API is *not* necessary.

Format: CLEAN^XGF

Input Parameters: none.

Output: none.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/006.png) REF: See also: <u>PREP^XGF(): Screen/Keyboard Setup</u> API.

## CLEAR^XGF(): Screen Clear Region

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The CLEAR^XGF API clears a rectangular region of the screen. It is useful to clear a portion of the screen.

The CLEAR function works by printing spaces using the current screen attribute in the specified region. If the screen attribute is changed and then the CLEAR function is used, the rectangular region is cleared in the new attribute.

A call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point prior to calling CLEAR^XGF.

Acceptable values for the top and bottom parameters range from 0 to IOSL-1. Acceptable values for the left and right parameters range from 0 to IOM-1.

Format: CLEAR^XGF(top,left,bottom,right)

Input Parameters: top: (required) Top screen coordinate for box.

left: (required) Left screen coordinate for box.

bottom: (required) Bottom screen coordinate for box.

right: (required) Right screen coordinate for box.

Output Parameters: \$x and \$y: Set to the right and bottom specified as parameters.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/007.png) REF: See also: <u>RESTORE^XGF(): Screen Restore</u>, <u>SAVE^XGF(): Screen Save</u>, and <u>WIN^XGF(): Screen Text Window</u> APIs.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

For example, to clear the entire screen, do the following:

<span id="_Toc199950819" class="anchor"></span>Figure 4: CLEAR^XGF API—Example 1

\><span class="mark">D CLEAR^XGF(0,0,23,79)</span>

#### Example 2

To clear a rectangular region in the center of the screen, do the following:

<span id="_Toc199950820" class="anchor"></span>Figure 5: CLEAR^XGF API—Example 2

\><span class="mark">D CLEAR^XGF(5,20,15,60)</span>

## FRAME^XGF(): Screen Frame

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The FRAME^XGF API draws a box frame on the screen. It displays boxes on the screen.

The FRAME function does *not* clear or otherwise change the region that it encompasses. If you need to open an empty framed window you should use the <u>WIN^XGF(): Screen Text Window</u> API instead.

A call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point prior to calling FRAME^XGF.

Acceptable values for the top and bottom parameters range from 0 to IOSL-1. Acceptable values for the left and right parameters range from 0 to IOM-1.

Format: FRAME^XGF(top,left,bottom,right)

Input Parameters: top: (required) Top screen coordinate for box.

left: (required) Left screen coordinate for box.

bottom: (required) Bottom screen coordinate for box.

right: (required) Right screen coordinate for box.

Output Parameters: \$x and \$y: Set to the right and bottom specified as parameters.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/008.png) REF: See also: <u>RESTORE^XGF(): Screen Restore</u> and <u>WIN^XGF(): Screen Text Window</u> APIs.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For example, to draw a box in the center of the screen, do the following:

<span id="_Toc199950821" class="anchor"></span>Figure 6: FRAME^XGF API—Example

\><span class="mark">D FRAME^XGF(5,20,15,60)</span>

## INITKB^XGF(): Keyboard Setup Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The INITKB^XGF API sets up the XGF keyboard environment only. You should call INITKB^XGF once, before you start making calls to the <u>\$\$READ^XGF</u> function. This API turns on escape processing and any terminators that are passed.

Use this API only if you are using XGF’s Keyboard Reader independently from XGF’s screen functions. Otherwise, a call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API does everything to set up keyboard processing that INITKB^XGF does, and a separate call to INITKB^XGF is *not* necessary.

Unlike the <u>PREP^XGF(): Screen/Keyboard Setup</u> API, INITKB^XGF does *not* set the keypad to application mode.

INITKB *does not call*%ZISS. Thus, documented Kernel variables, such as IOKPAM and IOKPNM, are *not* available for use without a separate call to the [ENS^%ZISS: Set Up Screen-handling Variables](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#ens_ziss) API.

Format: INITKB^XGF(\[term_str\])

Input Parameters: term_str: (optional) String of characters that should terminate the READ.

This parameter can be one of two forms:

- A single asterisk (\*) character turns on all terminators.
- The string of terminating characters, such as \$C(9,13,127).

If this parameter is *not* passed, or if it is an empty string, the terminators are *not* turned on.

Output: none.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/009.png) REF: See also: <u>RESETKB^XGF: Exit XGF Keyboard</u> API.

## IOXY^XGF(): Screen Cursor Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The IOXY^XGF API positions the cursor on the screen at a screen coordinate. This API is like Kernel’s X IOXY function:

- The row parameter *must* be between 0 and IOSL-1.
- The column parameter *must* be between 0 and IOM- 1.

A call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point prior to calling IOXY^XGF.

You can specify row and column parameters relative to the current \$X and \$Y by specifying + or - to increment or decrement \$X or \$Y by 1. You can increment or decrement by more than one if you add a number as well, such as “-5” or “+10”.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/010.png) NOTE: You *must* use quotes to pass a “+” or “-”. Otherwise, to specify exact locations for row and column, pass numbers.

Format: IOXY^XGF(row,column)

Input Parameters: row: (required) Row position to which the cursor is moved.

column: (required) Column position to which the cursor is moved.

Output Variables: \$X and \$Y: Set to the row and column specified as parameters.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/011.png) REF: See also: <u>SAY^XGF(): Screen String</u> and <u>SAYU^XGF(): Screen String with Attributes</u> APIs.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For example, to position the cursor at row 12, column 39, do the following:

<span id="_Toc199950822" class="anchor"></span>Figure 7: IOXY^XGF API—Example

\><span class="mark">D IOXY^XGF(12,39)</span>

## PREP^XGF(): Screen/Keyboard Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The PREP^XGF API sets up the XGF screen and keyboard environments.

Before using any XGF screen functions, you *must* call the PREP^XGF API. PREP^XGF does the following:

- Sets up screen control variables and tables.
- Turns off all video attributes.
- Turns echo off.
- Turns the cursor off.
- Sets the keypad to application mode.
- Clears the screen.

In addition, PREP^XGF does everything that the <u>INITKB^XGF(): Keyboard Setup Only</u> API does to set up the XGF keyboard environment, including turning escape processing and terminators on.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/012.png) NOTE: If you call PREP^XGF, a call to the <u>INITKB^XGF(): Keyboard Setup Only</u> API would be redundant.

Format: PREP^XGF(xgcuratr)

Input Parameters: none.

Output Parameters: xgcuratr: One-character parameter containing the state of the current video attribute.

Also, the [GSET^%ZISS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#gset_ziss) API is called, so all output variables for screen graphics from [GSET^%ZISS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#gset_ziss) are defined.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/013.png) REF: See also: <u>CLEAN^XGF: Screen/Keyboard Exit and Cleanup</u> API.

## \$\$READ^XGF(): Read Using Escape Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The \$\$READ^XGF extrinsic function provides a way to perform READs using escape processing. READs, when escape processing is turned on, are terminated by:

- \<UP-ARROW\> (“↑”)
- \<DOWN-ARROW\> (“↓”)
- \<PREV\> (“←”)
- \<NEXT\> (“→”)
- \<TAB\>
- Other special keystrokes

\$\$READ^XGF is a low-level reader compared to the VA FileMan reader. In some respects, it is as simple as using the M READ command. This READ function incorporates escape processing, which puts the burden on the operating system to READ the arrow, function, and all other keys.

A call to [INITKB^XGF](#initkb_xgf) or [PREP^XGF](#prepxgf-screenkeyboard-setup) *must* be made at some point *prior* to calling \$\$READ^XGF.

If the number of characters you request with the first parameter is *not* entered, the READ does *not* terminate until some terminating character is pressed (or the timeout period is reached).

If you do *not* pass the timeout parameter, DTIME is used for the timeout period. If the READ times out, caret (^) is returned and DTOUT is left defined.

The list of mnemonics for keys that can terminate READs is:

| Key Type | Mnemonic                                                                                                                                                                                                                      |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Control  | ^A, ^B, ^C, ^D, ^E, ^F, ^G, ^H, ^J, ^K, ^L, ^N, ^O, ^P, ^Q, ^R, ^S, ^T, ^U, ^V, ^W, ^X, ^Y, ^Z, ^\\, ^\], ^6, ^\_ |
| Cursor   | UP, DOWN, RIGHT, LEFT, PREV, NEXT                                                                                                                                                                     |
| Editing  | FIND, INSERT, REMOVE, SELECT                                                                                                                                                                                  |
| Function | F6 to F14, HELP, DO, F17 to F20                                                                                                                                                                       |
| Keyboard | TAB, CR                                                                                                                                                                                                               |
| Keypad   | KP0 to KP9, KP-, KP+, KP., KPENTER                                                                                                                                                                    |
| PF       | PF1, PF2, PF3, PF4                                                                                                                                                                                            |

Format: \$\$READ^XGF(\[no_of_char\]\[,timeout\])

Input Parameters: no_of_char: (optional) Maximum number of characters to READ.

timeout: (optional) Maximum duration of READ, in seconds.

Output Variables: XGRT: Set to the mnemonic of the key that terminated the READ.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/014.png) REF: For a list of possible values, see the list in <u>Table 3</u> or the table in routine XGKB.

DTOUT: If defined, it signifies that the READ timed out.

Output: returns: Returns the string READ from the user.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

To READ a name (with a maximum length of 30) from input and display that name on the screen, do the following:

<span id="_Toc200270065" class="anchor"></span>Figure 8: \$\$READ^XGF API—Example 1: READ a Name

D INITKB^XGF("\*")W "Name: " S NM=\$\$READ^XGF(30)D SAY^XGF(10,20,"Hello " NM)

#### Example 2

To accept only \<Up-Arrow\> (“↑”) or \<Down-Arrow\> (“↓”) keys to exit a routine, do the following:

<span id="_Toc200270066" class="anchor"></span>Figure 9: \$\$READ^XGF API—Example 2: Accept Only Up-Arrow (“↑”) and Down-Arrow (“↓”) Keys

;Only accept UP or DOWN arrow keys

F S %=\$\$READ^XGF(1) Q:XGRT="UP"!(XGRT="DOWN")

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/015.png) NOTE: When you set up the XGF keyboard environment using [INITKB^XGF](#initkb_xgf) rather than [PREP^XGF](#prepxgf-screenkeyboard-setup), the keypad is *not* automatically set to application mode. For READs to be terminated by the keypad keys (\<KP0\> to \<KP9\>, \<KPENTER\>, \<KP+\>, \<KP-\>, and \<KP.\>), the keypad *must* be in application mode. You can put the keypad in application mode by using an M WRITE statement (W IOKPAM to set application mode, IOKPNM to set numeric mode). Take care to preserve the value of \$X when using a direct M WRITE, so that relative positioning in XGF cursor/text output calls is *not* thrown off:  
  
X=\$X W IOKPAM S \$X=X

## RESETKB^XGF: Exit XGF Keyboard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The RESETKB^XGF API exits the XGF keyboard environment. You should use the RESETKB^XGF call once you finish making calls to the <u>\$\$READ^XGF(): Read Using Escape Processing</u> function. The RESETKB^XGF API turns terminators and escape processing off and removes any XGF keyboard environment variables. Subsequent READs are processed normally.

Use this API only if you are using XGF’s Keyboard Reader independently from XGF’s screen functions. Otherwise, a call to the <u>CLEAN^XGF: Screen/Keyboard Exit and Cleanup</u> API does everything to clean up keyboard processing that the RESETKB^XGF API does, and a separate call to the RESETKB^XGF API is *not* necessary.

Unlike the <u>CLEAN^XGF: Screen/Keyboard Exit and Cleanup</u> API, the RESETKB^XGF API *does not set* the keypad to numeric mode.

Format: RESETKB^XGF

Input Parameters: none.

Output: none.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/016.png) REF: See also: <u>INITKB^XGF(): Keyboard Setup Only</u> API.

## RESTORE^XGF(): Screen Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The RESTORE^XGF API restores a previously saved screen region. You can save screen regions using the <u>WIN^XGF(): Screen Text Window</u> and <u>SAVE^XGF(): Screen Save</u> APIs. RESTORE^XGF restores the saved screen region in the same screen position as the screen region was saved from.

A call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point prior to calling RESTORE^XGF.

Specify the array node under which to save the overlaid screen region in closed root and fully resolved form (that is closed right parenthesis and with variable references such as \$J fully resolved). Using M \$NAME function is a quick way to pass fully resolved node specifications.

Format: RESTORE^XGF(save_root)

Input Parameters: save_root: (required) Global/local array node, closed root form.

Output Variables: \$X and \$Y: Set to the bottom right coordinate of the restored window.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/017.png) REF: See also: <u>CLEAR^XGF(): Screen Clear Region</u>, <u>SAVE^XGF(): Screen Save</u>, and <u>WIN^XGF(): Screen Text Window</u> APIs.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To restore the screen contents saved to the local array SELECT to their original position, do the following:

<span id="_Toc199950825" class="anchor"></span>Figure 10: RESTORE^XGF API—Example

\><span class="mark">D RESTORE^XGF("SELECT")</span>

## SAVE^XGF(): Screen Save

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The SAVE^XGF API saves a screen region. To save and restore screen regions, you *must* do all screen output using calls in the XGF Function Library output. If you use the M WRITE command for output, the screen contents *cannot* be saved and restored. Also, a call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point prior to calling SAVE^XGF.

Specify the array node under which to save the overlaid screen region in closed root and fully resolved form (that is closed right parenthesis and with variable references such as \$J fully resolved). Using M \$NAME function is a quick way to pass fully resolved node specifications.

Format: SAVE^XGF(top,left,bottom,right,save_root)

Input Parameters: top: (required) Top screen coordinate for box.

left: (required) Left screen coordinate for box.

bottom: (required) Bottom screen coordinate for box.

right: (required) Right screen coordinate for box.

save_root: (required) Global/local array node, closed root form.

Output Variables: \$X and \$Y: Left unchanged.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/018.png) REF: See also: <u>CLEAR^XGF(): Screen Clear Region</u>, <u>RESTORE^XGF(): Screen Restore</u>, and <u>WIN^XGF(): Screen Text Window</u> APIs.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For example, to save the screen contents between rows 5 and 15 and columns 20 and 60 in the SELECT local array, do the following:

<span id="_Toc199950826" class="anchor"></span>Figure 11: SAVE^XGF API—Example

\><span class="mark">D SAVE^XGF(5,20,15,60,"SELECT")</span>

## SAY^XGF(): Screen String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The SAY^XGF API outputs a string to the screen (with optional positioning and attribute control).

Use this API rather than the M WRITE command to output strings to the screen. The row and column parameters specify where to print the string:

- If omitted, the current row and column positions are used.
- If specified, the row *must* be between 0 and IOSL-1, and the column *must* be between 0 and IOM-1.

A call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point *prior* to calling SAY^XGF.

You can specify row and column parameters relative to the current \$X and \$Y by specifying + or - to increment or decrement \$X or \$Y by 1. You can increment or decrement by more than 1 if you add a number as well (such as “-5” or “+10”).

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/019.png) NOTE: You *must* use quotes to pass a “+” or “-”; otherwise, to specify exact locations for row and column, pass numbers.

Without the fourth argument for video attribute, SAY^XGF displays the string using the current video attribute. With the fourth argument, SAY^XGF displays the string using the attributes you specify. SAY^XGF changes the video attribute only for the output of the string; upon termination of the function, it restores video attributes to their state *prior* to the function call.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/020.png) REF: For a discussion of valid video attribute codes for the video attribute parameter, see the <u>SETA^XGF(): Screen Video Attributes</u> API.

Format: SAY^XGF(\[row\]\[,column,\]str\[,atr\])

Input Parameters: row: (optional) Row position to start WRITE.

column: (optional) Column position to start WRITE.

str: (required) String to WRITE.

atr: (optional) Video attribute with which to WRITE string.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/021.png) REF: For description of atr codes, see the <u>\$\$READ^XGF(): Read Using Escape Processing</u> API.

Output Variables: \$X and \$Y: Set to position of the last character output.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/022.png) REF: See also: <u>IOXY^XGF(): Screen Cursor Placement</u> and <u>SAYU^XGF(): Screen String with Attributes</u> APIs.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

For example, to print “Hello, World” in the center of the screen, in the current video attribute, do the following:

<span id="_Toc199950827" class="anchor"></span>Figure 12: SAY^XGF API—Example 1

\><span class="mark">D SAY^XGF(11,35,"Hello World")</span>

#### Example 2

To print “ERROR!” at (row,col) position (\$X+1,\$Y+5), in reverse and bold video attributes, do the following:

<span id="_Toc199950828" class="anchor"></span>Figure 13: SAY^XGF API—Example 2

\><span class="mark">D SAY^XGF("+","+5","ERROR!","R1B1")</span>

#### Example 3

To print “...” at the current cursor position, in the current video attribute, do the following:

<span id="_Toc199950829" class="anchor"></span>Figure 14: SAY^XGF API—Example 3

\><span class="mark">D SAY^XGF(,,"...")</span>

## SAYU^XGF(): Screen String with Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The SAYU^XGF API outputs a string to the screen (with optional position and attribute control), including the ability to underline an individual character.

This API is like [SAY^XGF](#sayxgf-screen-string). The difference is that the first ampersand (&) character has a special meaning in the output string; it acts as a flag to indicate that the next character should be underlined. You are only allowed one underlined character per call. Typically, you would use SAYU^XGF when writing a menu option’s text, to underline that option’s speed key.

A call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point prior to calling SAYU^XGF.

You can specify row and column parameters relative to the current \$X and \$Y by specifying + or - to increment or decrement \$X or \$Y by 1. You can increment or decrement by more than 1 if you add a number as well (such as “-5” or “+10”).

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/023.png) NOTE: You *must* use quotes to pass a “+” or “-”. Otherwise, to specify exact locations for row and column, pass numbers.

If the first ampersand is followed by another ampersand, this initial && is interpreted and displayed as one ampersand character, &, and you still can use a single ampersand as an underlining flag.

Format: SAYU^XGF(\[row\]\[,column,\]str\[,atr\])

Input Parameters: row: (optional) Row position to start WRITE.

column: (optional) Column position to start WRITE.

str: (required) String to WRITE (& underlines next character).

atr: (optional) Video attribute with which to WRITE a string.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/024.png) REF: For a description of atr codes, see the <u>\$\$READ^XGF(): Read Using Escape Processing</u> API.

Output Variables: \$X,\$Y: Set to the position of the last character output.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/025.png) REF: See also: <u>IOXY^XGF(): Screen Cursor Placement</u> and <u>SAY^XGF(): Screen String</u> APIs.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For example, to print <u>S</u>ave at row 5, column 10, do the following:

<span id="_Toc199950830" class="anchor"></span>Figure 15: SAYU^XGF API—Example

\><span class="mark">D SAYU^XGF(5,10,"&Save")</span>

## SETA^XGF(): Screen Video Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The SETA^XGF API sets all video attribute simultaneously, for subsequent screen output. This API is different from the <u>\$\$READ^XGF(): Read Using Escape Processing</u> API in that it takes a different form of the attribute argument, and, unlike the <u>CHGA^XGF(): Screen Change Attributes</u> API, it sets all attributes. The change in attribute remains in effect until you make another <u>CHGA^XGF(): Screen Change Attributes</u>, <u>CLEAN^XGF: Screen/Keyboard Exit and Cleanup</u>, or SETA^XGF API call. If you want only a temporary change in attribute, the <u>SAY^XGF(): Screen String</u> API might be a better function to use.

A call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point prior to calling the SETA^XGF API.

The value of the attribute parameter uses one bit for the value of each video attribute. The format of the bits is *not* documented. The current setting of all video attributes is accessible through the xgcuratr parameter, however. Rather than trying to use the SETA^XGF API to control an individual video attribute’s setting, you should use it mainly to restore the screen attributes based on a previously saved value of xgcuratr.

Format: SETA^XGF(atr_code)

Input Parameters: atr_code: (required) Single character containing the states of all video attributes as the bit values. This argument itself should be derived from a previous call to the <u>PREP^XGF(): Screen/Keyboard Setup</u>, <u>CHGA^XGF(): Screen Change Attributes</u>, or SETA^XGF APIs.

Output Variables: XGCURATR: This variable always holds the current screen attribute coded as a single character and is updated when you call SETA^XGF.

\$X and \$Y: Left unchanged.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/026.png) REF: See also: <u>\$\$READ^XGF(): Read Using Escape Processing</u> API.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To save the initial screen attribute settings to variable SAVEATR, do a function called SOME^THING, and then reset all the video attributes to their initial state, do the following:

<span id="_Toc199950831" class="anchor"></span>Figure 16: SETA^XGF API—Example

\><span class="mark">D PREP^XGF S SAVEATR=XGCURATR</span>

\><span class="mark">D SOME^THING</span>

\><span class="mark">D SETA^XGF(SAVEATR)</span>

## WIN^XGF(): Screen Text Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XGF Function Library

ICR \#: 3173

Description: The WIN^XGF API opens a text window on the screen and optionally remember what it overlays. If the save<u>\_</u>root parameter is *not* passed, you *cannot* restore the screen behind the window.

To save the screen region that the window overlays it is necessary that screen output is done using only the functions in the XGF Function library. If you use the M WRITE command for output, the screen contents *cannot* be saved.

A call to the <u>PREP^XGF(): Screen/Keyboard Setup</u> API *must* be made at some point prior to calling WIN^XGF.

Specify the array node under which to save the overlaid screen region in closed root and fully resolved form (that is closed right parenthesis and with variable references such as \$J fully resolved). Using the M \$NAME function is a quick way to pass fully resolved node specifications.

To restore screens, you save with the WIN^XGF function, use the <u>RESTORE^XGF(): Screen Restore</u> API.

Format: WIN^XGF(top,left,bottom,right\[,save_root\])

Input Parameters: top: (required) Top screen coordinate for box.

left: (required) Left screen coordinate for box.

bottom: (required) Bottom screen coordinate for box.

right: (required) Right screen coordinate for box.

save_root: (optional) Global/local array node, closed root form.

Output Parameters: save_root: If you specify a node as a fifth parameter for save_root, WIN^XGF saves the screen region you overlay in an array at that node.

Output Variables:\$X and \$Y: Set to the right and bottom coordinates you specify as parameters.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/027.png) REF: See also: <u>CLEAR^XGF(): Screen Clear Region</u>, <u>FRAME^XGF(): Screen Frame</u>, <u>RESTORE^XGF(): Screen Restore</u>, and <u>SAVE^XGF(): Screen Save</u> APIs.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

To draw an empty box in the center of the screen (and save the underlying screen region under array SELECT), do the following:

<span id="_Toc500397604" class="anchor"></span>Figure 17: WIN^XGF API—Example 1

\><span class="mark">D WIN^XGF(5,20,15,60,"SELECT")</span>

#### Example 2

To save the same window to a global array (to illustrate the use of \$NAME to specify a fully resolved root), do the following:

<span id="_Toc500397605" class="anchor"></span>Figure 18: WIN^XGF API—Example 2

\><span class="mark">D WIN^XGF(5,20,15,60,\$NA(^TMP(\$J)))</span>

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/028.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/029.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-xgf-function-library-user-guide/030.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.