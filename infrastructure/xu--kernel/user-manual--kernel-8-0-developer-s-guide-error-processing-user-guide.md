---
title: "Kernel 8.0 Developerâ€™s Guide: Error Processing User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Error Processing"
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
  - error
  - kernel
  - guide
  - zter
  - table
  - contents
  - application
  - trap
  - developer
  - processing
page_count: 0
word_count: 1908
section_count: 8
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_error_processing_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_error_processing_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259309" class="anchor"></span>Error Processing Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-error-processing-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-error-processing-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Error Processing Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc206774055" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-error-processing-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Direct Mode Utilities](#direct-mode-utilities)
  - [\>D ^XTER](#d-xter)
  - [\>D ^XTERPUR](#d-xterpur)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$EC^%ZOSV: Get Error Code](#eczosv-get-error-code)
    - [Example](#example)
  - [^%ZTER: Kernel Standard Error Recording Routine](#zter-kernel-standard-error-recording-routine)
    - [Examples](#examples)
  - [APPERR^%ZTER: Set Application Error Name in Kernel Error Trap Log](#apperrzter-set-application-error-name-in-kernel-error-trap-log)
    - [Example](#example-1)
  - [\$\$NEWERR^%ZTER: Verify Support of Standard Error Trapping (Obsolete)](#newerrzter-verify-support-of-standard-error-trapping-obsolete)
  - [UNWIND^%ZTER: Quit Back to Calling Routine](#unwindzter-quit-back-to-calling-routine)
    - [Example](#example-2)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Error Processing Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Error Processing Direct Mode Utilities can be run from Programmer mode. They are *not*, however, APIs and Extrinsic Functions; instead, they are provided for convenience.

## \>D ^XTER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can call the ^XTER direct mode utility from Programmer mode. It is the same as using the Error Trap Display \[XUERTRAP\] option.

## \>D ^XTERPUR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can call the ^XTERPUR direct mode utility from Programmer mode. It is the same as using the Clean Error Trap \[XUERTRP CLEAN\] option.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Error Processing APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## \$\$EC^%ZOSV: Get Error Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The \$\$EC^%ZOSV extrinsic function returns the most recent error message recorded by the operating system.

Format: \$\$EC^%ZOSV

Input Parameters: none.

Output: returns: Returns the most recent error code/message.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\>S X=\$\$EC^%ZOSV

## ^%ZTER: Kernel Standard Error Recording Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Error Processing

ICR \#: 1621

Description: Kernel sets the Error Trap in ZU so that all user errors are trapped. In this context, when an error occurs, the optional %ZT input array is set to indicate the user’s location in the menu system. Then, call ^%ZTER to record this information in the ERROR LOG (#3.075) file.

The application-specific Error Trap routine, when it is called because of an error, can then use the ^%ZTER API to record error information in the ERROR LOG (#3.075) file if it decides that it needs to. ^%ZTER gathers all available information such as local symbols and last global reference and stores that information in an entry in the ERROR LOG (#3.075) file.

The simple example below shows an application that replaces the standard Kernel Error Trap with its own Error Trap. When an error occurs, and the application’s Error Trap routine is called, it calls [\$\$EC^%ZOSV](#eczosv-get-error-code) to see what type of error occurred. If an end-of-file (EOF) error occurs, it lets the application continue. Otherwise, it calls ^%ZTER to record the error and then quits to terminate the application.

![](kernel-8-0-developer-s-guide-error-processing-user-guide/004.png) NOTE: The recording mechanism of ^%ZTER also functions in the absence of an error. In a debug mode, this would enable a developer to record local symbols and global structures at predetermined places within code execution for later checking.

![](kernel-8-0-developer-s-guide-error-processing-user-guide/005.png) NOTE: As of Kernel Patch XU\*8.0\*431, the ^%ZTER error trap routine checks a count (limit) in the ERROR TRAP SUMMARY (#3.077) file and stops recording errors once this limit has been reached. This limit is initialized to 10 but can be changed by the sites. To change the value, use VA FileMan to edit the ERROR LIMIT (#520.1) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file.

Format: ^%ZTER

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
2.  Set all input variables.
3.  Call the API.

Input Variables: %ZT: (optional) The %ZT array can be used to identify a global node whose descendants should be recorded in the error log. When called within the standard Kernel Error Trap, %ZT is set to record the user’s location in the menu system:

\>S %ZT("^TMP(\$J)")=""  
\>D ^%ZTEROutput Variables: %ZTERROR: Calls to the error recorder always return this variable. It has the error name and error type as its first and second caret-delimited (^) pieces, for example, %ZTERROR=UNDEF^P. While the first piece is always defined since it is retrieved from the operating system, the second piece could be missing if unavailable from the ERROR MESSAGES (#3.076) file.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<u>Figure 1</u> is an example of the Error Trap:

<span id="_Ref454198444" class="anchor"></span>Figure 1: Error Trap—Example

ZXGP ; 999/NV - sample routine ; 23-FEB-95

;;1.0;;

;

FILEOPEN ;

;

; This code resets the error trap routine that is stepped to

; when an error occurs.

;

N \$ESTACK,\$ETRAP S \$ETRAP="D ERR^ZXGP"

;

; Open a file, and read lines from it until End-of-file (EOF)

; is reached.

;

K %ZIS S %ZIS=""

S %ZIS("HFSNAME")="MYFILE.DAT",%ZIS("HFSMODE")="RW"

D ^%ZIS Q:POP

F U IO R LINE:DTIME U IO(0) W !,LINE

;

FILECLOS ;

;

D ^%ZISC Q

;

ERR ;

; This is the application specific error trap.

;

I \$\$EC^%ZOSV\["ENDOFILE" S \$ECODE="" G FILECLOS ; continue if EOF error

D ^%ZTER ; record the error if anything other than EOF

D UNWIND^%ZTER ; unwind the stack, return to caller.

Q

;

#### Example 2

To test the error limit set in the ERROR LIMIT (#520.1) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file, run the following:

\>F I=1:1:20 D APPERROR^%ZTER("My Application Error")

Check the error trap and see how many errors with "My Application Error" get recorded in the Kernel error log (that is ERROR LOG \[#3.075\] file). If the value in the ERROR LIMIT (#520.1) field is set to 10, there should just be 10 occurrences of the “My Error” error in the Kernel error log.

![](kernel-8-0-developer-s-guide-error-processing-user-guide/006.png) NOTE: For more information, see the “[APPERROR^%ZTER](#apperrzter-set-application-error-name-in-kernel-error-trap-log)” API.

## APPERR^%ZTER: Set Application Error Name in Kernel Error Trap Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Error Processing

ICR \#: 1621

Description: The APPERR^%ZTER API sets the "application error" text passed in as the error name in the Kernel error trap log (that is ERROR LOG \[#3.075\] file).

![](kernel-8-0-developer-s-guide-error-processing-user-guide/007.png) NOTE: The APPERR^%ZTER API replaces the need to set \$ZE before calling the <u>^%ZTER: Kernel Standard Error Recording Routine</u> API:

Before:

\>S \$ZE="application error" D ^%ZTER

After:

\>D APPERROR^%ZTER("application error")

![](kernel-8-0-developer-s-guide-error-processing-user-guide/008.png) NOTE: This API was released with Kernel Patch XU\*8.0\*431.

Format: APPERROR^%ZTER("application error")

Input Parameters: “application error”: This input parameter is the "application error" name that gets displayed in the Kernel error trap log (that is ERROR LOG \[#3.075\] file).

Output: returns: Displays the "application error" text passed in as the error name in the Kernel error trap log (that is ERROR LOG \[#3.075\] file).

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\>DO APPERROR^%ZTER("My Application Error")

Check the Kernel error trap and see if there is an error called "My Application Error".

## \$\$NEWERR^%ZTER: Verify Support of Standard Error Trapping (Obsolete)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-error-processing-user-guide/009.png) NOTE: The \$\$NEWERR^%ZTER API is obsolete, because all VA systems support the standard error trapping.

Reference Type: Supported

Category: Error Processing

ICR \#: 1621

Description: The \$\$NEWERR^%ZTER extrinsic function reports if the current platform supports the standard error trapping. It returns:

- 1—If the standard error trapping is supported.
- 0—For all other cases.

Format: \$\$NEWERR^%ZTER

Input Parameters: none.

Output: returns: Returns:

- 1—If the standard error trapping is supported.
- 0—For all other cases.

## UNWIND^%ZTER: Quit Back to Calling Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Error Processing

ICR \#: 1621

Description: Use the UNWIND^%ZTER API after a package Error Trap to quit back to the calling routine. Control returns to the level above the one that NEWed \$ESTACK.

Format: UNWIND^%ZTER

Input Parameters: none.

Output: none.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main:

<span id="_Toc200269967" class="anchor"></span>Figure 2: UNWIND^%ZTER API—Main Code Example

S X=1 D SUBW XQ SUB N \$ESTACK,\$ETRAP S \$ETR="D ERROR"S X=1/0Q

Usage:

<span id="_Toc200269968" class="anchor"></span>Figure 3: UNWIND^%ZTER API—Usage

D ^%ZTER ;This will record the error info and clear \$ECODES ^XXX="Incomplete record"G UNWIND^%ZTER

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-error-processing-user-guide/010.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-error-processing-user-guide/011.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-error-processing-user-guide/012.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.