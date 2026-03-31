---
title: "Kernel 8.0 Developerâ€™s Guide: Operating System Interface User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Operating System Interface"
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
  - strong
  - class
  - zosv
  - table
  - contents
  - operating
  - guide
  - returns
  - kernel
  - span
page_count: 0
word_count: 4548
section_count: 19
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_os_interface_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_os_interface_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259493" class="anchor"></span>Operating System (OS) Interface Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref59870602" class="anchor"></span>Table 1: ^%ZOSF API—Global Nodes</p></caption>
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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Operating System (OS) Interface Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref59870602" class="anchor"></span>Table 1: ^%ZOSF API—Global Nodes

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc234301876" class="anchor"></span>List of Figures

<span id="_Toc207254986" class="anchor"></span>List of Tables

[Table 1: ^%ZOSF API—Global Nodes [4](#_Ref59870602)](#_Ref59870602)

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Direct Mode Utilities](#direct-mode-utilities)
  - [\>D ^%ZTBKC: Global Block Count](#d-ztbkc-global-block-count)
  - [\>D ^ZTMGRSET: Update ^%ZOSF Nodes](#d-ztmgrset-update-zosf-nodes)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$CPUTIME^XLFSHAN: Return System and User CPU Time](#cputimexlfshan-return-system-and-user-cpu-time)
  - [\$\$ETIMEMS^XLFSHAN(): Return Elapsed Time in Milliseconds](#etimemsxlfshan-return-elapsed-time-in-milliseconds)
  - [^%ZOSF(): Operating System-dependent Logic Global](#zosf-operating-system-dependent-logic-global)
  - [\$\$ACTJ^%ZOSV: Number of Active Jobs](#actjzosv-number-of-active-jobs)
  - [\$\$AVJ^%ZOSV: Number of Available Jobs](#avjzosv-number-of-available-jobs)
  - [DOLRO^%ZOSV: Display Local Variables](#dolrozosv-display-local-variables)
    - [Example](#example)
  - [GETENV^%ZOSV: Current System Information](#getenvzosv-current-system-information)
  - [\$\$LGR^%ZOSV: Last Global Reference](#lgrzosv-last-global-reference)
    - [Example](#example-1)
  - [LOGRSRC^%ZOSV(): Record Resource Usage (RUM)](#logrsrczosv-record-resource-usage-rum)
  - [\$\$OS^%ZOSV: Get Operating System Information](#oszosv-get-operating-system-information)
    - [Example](#example-2)
  - [SETENV^%ZOSV: Set VMS Process Name (Caché/OpenVMS Systems)](#setenvzosv-set-vms-process-name-cachéopenvms-systems)
  - [SETNM^%ZOSV(): Set VMS Process Name (Caché/OpenVMS Systems)](#setnmzosv-set-vms-process-name-cachéopenvms-systems)
  - [T0^%ZOSV: Start RT Measure (Obsolete)](#t0zosv-start-rt-measure-obsolete)
  - [T1^%ZOSV: Stop RT Measure (Obsolete)](#t1zosv-stop-rt-measure-obsolete)
  - [\$\$VERSION^%ZOSV(): Get OS Version Number or Name](#versionzosv-get-os-version-number-or-name)
    - [Examples](#examples)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Operating System (OS) Interface Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel and Kernel Toolkit provides several utilities to work with the underlying operating system. In addition, Kernel’s ^%ZOSF global holds operating system-dependent logic so that application programs can be written independently of any specific operating system. Each CPU or node in a system should have its own copy of the ^%ZOSF global; the ^%ZOSF global should *not* be translated.

# Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## \>D ^%ZTBKC: Global Block Count

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can count the data blocks in a global using the ^%ZTBKC direct mode utility. An entire global or a subscripted section can be measured, such as ^DIC or ^DIC(9.2). There is a corresponding option that can be used from the Programmer Options menu, called the Global Block Count \[XU BLOCK COUNT\] option.

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/004.png) REF: For more information on the Global Block Count \[XU BLOCK COUNT\] option, see the “Global Block Count Option” section in the [*Kernel 8.0 Developer’s Guide: Miscellaneous Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_miscellaneous_ug.pdf#Global_Block_Count_Option).

## \>D ^ZTMGRSET: Update ^%ZOSF Nodes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^ZTMGRSET direct mode utility is only available from the manager’s account. It is ordinarily run during Kernel installations to initialize Kernel in the manager’s account. It can be used later, however, to update an account’s ^%ZOSF nodes with new UCI and Volume Set information. The ^%ZOSF nodes that ^ZTMGRSET updates are:

- ^%ZOSF(“MGR”)
- ^%ZOSF(“PROD”)
- ^%ZOSF(“VOL”)

An example of a use for re-running ^ZTMGRSET would be when creating a new print, compute, file, or shadow server by copying an existing server’s account. Although Kernel is already set up in the copied account, the new server’s UCI and Volume Set ^%ZOSF nodes would need to be updated from their old values to the values needed for the new server. Re-running ^ZTMGRSET allows these values to be updated.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Operating System (OS) Interface APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## \$\$CPUTIME^XLFSHAN: Return System and User CPU Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 6157

Description: The \$\$CPUTIME^XLFSHAN extrinsic function returns two comma-delimited pieces:

- “system” CPU time.
- “user” CPU time (except on VMS where no separate times are available).

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/005.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$CPUTIME^XLFSHAN

Input Parameters: none.

Output: returns: The value returned is time measured as milliseconds of CPU time.

## \$\$ETIMEMS^XLFSHAN(): Return Elapsed Time in Milliseconds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 6157

Description: The \$\$ETIMEMS^XLFSHAN extrinsic function calculates the elapsed time in milliseconds. It is intended to be used with [\$\$CPUTIME^XLFSHAN](#cputimexlfshan-return-system-and-user-cpu-time) API to evaluate the performance of a process.

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/006.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$ETIMEMS^XLFSHAN(start,end)

Input Parameters: start: (required) The starting CPU time; set by calling the [\$\$CPUTIME^XLFSHAN](#cputimexlfshan-return-system-and-user-cpu-time) API.

end: (required) The ending CPU time; set by calling the [\$\$CPUTIME^XLFSHAN](#cputimexlfshan-return-system-and-user-cpu-time) API.

Output: returns: The value returned is elapsed time measured as milliseconds of CPU time.

## ^%ZOSF(): Operating System-dependent Logic Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^%ZOSF global holds operating system-dependent logic so that application programs can be written independently of any specific operating system.

Most of the nodes contain logic that *must* be executed to return a value, for example:

X ^%ZOSF("SS")

Those prefaced with one asterisk in <u>Table 1</u>, however, are reference values. For example, to WRITE the operating system, use:

W ^%ZOSF("OS")

The nodes prefaced with two asterisks in <u>Table 1</u> should be used with the DO command, as in the following:

\>D @^%ZOSF("ERRTN")

Table Key:

\* indicates those nodes that hold reference values.

\*\* indicates those nodes that are invoked with a DO statement (D).

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Node</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>ACTJ</strong></td>
<td>Return in <strong>Y</strong> the number of active jobs on the system.</td>
</tr>
<tr class="even">
<td><strong>AVJ</strong></td>
<td>Return in <strong>Y</strong> the number of jobs that can be started. The number of available jobs is the maximum number less the number of active jobs.</td>
</tr>
<tr class="odd">
<td><strong>BRK</strong></td>
<td>Allow the user to break the running of a routine.</td>
</tr>
<tr class="even">
<td><strong>DEL</strong></td>
<td>Delete the routine named in <strong>X</strong> from the UCI.</td>
</tr>
<tr class="odd">
<td><strong>EOFF</strong></td>
<td>Turn off echo to the <strong>$I</strong> device.</td>
</tr>
<tr class="even">
<td><strong>EON</strong></td>
<td>Turn on echo to the <strong>$I</strong> device.</td>
</tr>
<tr class="odd">
<td><strong>EOT</strong></td>
<td>Returns <strong>Y = 1</strong> if Magtape end-of-tape mark is detected.</td>
</tr>
<tr class="even">
<td><strong><sup></sup>ERRTN</strong></td>
<td><p>This node is set to the name of the routine that should be used to record errors. For most systems this is the KERNEL error recording routine (<strong>%ZTER</strong>):</p>
<blockquote>
<p>&gt;<strong>D @^%ZOSF("ERRTN")</strong></p>
</blockquote>
<p>To initially set the Error Trap:</p>
<blockquote>
<p>&gt;<strong>S X=^%ZOSF("ERRTN"),@^%ZOSF("TRAP")</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>ETRP</strong></td>
<td>Obsolete.</td>
</tr>
<tr class="even">
<td><strong>GD</strong></td>
<td>Display the global directory.</td>
</tr>
<tr class="odd">
<td><strong>GSEL</strong></td>
<td><p>Returns the user’s selection of globals as follows:</p>
<blockquote>
<p><strong>^UTILITY($J,"global name")</strong></p>
</blockquote>
<p>![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/007.png) <strong>NOTE:</strong> This is only supported for Caché currently.</p></td>
</tr>
<tr class="even">
<td><strong>JOBPARAM</strong></td>
<td>When passed the job in <strong>X</strong>, it returns the UCI for that job in <strong>Y</strong>. It determines whether the job is valid on the system.</td>
</tr>
<tr class="odd">
<td><strong>LABOFF</strong></td>
<td>Turn off echo to the <strong>IO</strong> device.</td>
</tr>
<tr class="even">
<td><strong>LOAD</strong></td>
<td>Load routine <strong>X</strong> into <strong>@(DIF_”XCNP,0)</strong>”.</td>
</tr>
<tr class="odd">
<td><strong>LPC</strong></td>
<td>Returns in <strong>Y</strong> the longitudinal parity check of the string in <strong>X</strong>.</td>
</tr>
<tr class="even">
<td><strong>MAGTAPE</strong></td>
<td><p>Sets the <strong>%MT</strong> local variable to hold magtape functions. Issue the backspace command as follows:</p>
<blockquote>
<p>&gt;<strong>W @%MT("BS")</strong></p>
</blockquote>
<p>The full list of functions are:</p>
<ul>
<li><blockquote>
<p><strong>BS—</strong>Back Space</p>
</blockquote></li>
<li><blockquote>
<p><strong>FS—</strong>Forward Space</p>
</blockquote></li>
<li><blockquote>
<p><strong>WTM—WRITE</strong> Tape Mark</p>
</blockquote></li>
<li><blockquote>
<p><strong>WB—WRITE</strong> Block</p>
</blockquote></li>
<li><blockquote>
<p><strong>REW—</strong>Rewind</p>
</blockquote></li>
<li><blockquote>
<p><strong>RB—READ</strong> Block</p>
</blockquote></li>
<li><blockquote>
<p><strong>REL—READ</strong> Label</p>
</blockquote></li>
<li><blockquote>
<p><strong>WHL—WRITE</strong> <strong>HDR</strong> Label</p>
</blockquote></li>
<li><blockquote>
<p><strong>WEL—WRITE</strong> <strong>EOF</strong> Label</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>MAXSIZ</strong></td>
<td>For M/SQL-VAX only. Sets the partition size to <strong>X</strong>.</td>
</tr>
<tr class="even">
<td><strong><sup>*</sup>MGR</strong></td>
<td>Holds the name of the <strong>MGR</strong> account (UCI, Volume Set).</td>
</tr>
<tr class="odd">
<td><strong>MTBOT</strong></td>
<td>Returns <strong>Y = 1</strong> if the magtape is at <strong>BOT</strong>.</td>
</tr>
<tr class="even">
<td><strong>MTERR</strong></td>
<td>Returns <strong>Y = 1</strong> if a magtape error is detected.</td>
</tr>
<tr class="odd">
<td><strong>MTONLINE</strong></td>
<td>Returns <strong>Y = 1</strong> if the magtape is online.</td>
</tr>
<tr class="even">
<td><strong>MTWPROT</strong></td>
<td>Returns <strong>Y = 1</strong> if the magtape is <strong>WRITE</strong> Protected.</td>
</tr>
<tr class="odd">
<td><strong>NBRK</strong></td>
<td>Do <em>not</em> allow the user to break a routine.</td>
</tr>
<tr class="even">
<td><strong>NO-PASSALL</strong></td>
<td>Sets device <strong>$I</strong> to interpret tabs, carriage returns, line feeds, or control characters (normal text mode).</td>
</tr>
<tr class="odd">
<td><strong>NO-TYPE-AHEAD</strong></td>
<td>Turn off the TYPE-AHEAD for the device <strong>$I</strong>.</td>
</tr>
<tr class="even">
<td><strong><sup>*</sup>OS</strong></td>
<td>In the first <strong>^</strong> piece, holds the type of MUMPS (such as Caché, VAX DSM, GT.M).</td>
</tr>
<tr class="odd">
<td><strong>PASSALL</strong></td>
<td>Sets device <strong>$I</strong> to pass all codes, allow tabs, carriage returns, and other control characters to be passed (binary transfer).</td>
</tr>
<tr class="even">
<td><strong>PRIINQ</strong></td>
<td>Returns <strong>Y</strong> with the current priority of the job.</td>
</tr>
<tr class="odd">
<td><strong>PRIORITY</strong></td>
<td>Sets the priority of the job to <strong>X</strong> (<strong>1</strong> is low, <strong>10</strong> is high).</td>
</tr>
<tr class="even">
<td><strong><sup>*</sup>PROD</strong></td>
<td>Holds the name of the Production account (UCI, Volume Set).</td>
</tr>
<tr class="odd">
<td><strong>PROGMODE</strong></td>
<td>Returns <strong>Y = 1</strong> if the user is in <strong>Programmer</strong> mode.</td>
</tr>
<tr class="even">
<td><strong>RD</strong></td>
<td>Displays the routine directory.</td>
</tr>
<tr class="odd">
<td><strong>RESJOB</strong></td>
<td>References the operating system routine for restoring a job.</td>
</tr>
<tr class="even">
<td><strong>RM</strong></td>
<td>Sets the <strong>$I</strong> width to <strong>X</strong> characters. If <strong>X=0</strong>, then the line in set to no wrap.</td>
</tr>
<tr class="odd">
<td><strong>RSEL</strong></td>
<td><p>Returns the user’s selection of routines as follows:</p>
<blockquote>
<p><strong>^UTILITY($J,"routine name")</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>RSUM</strong></td>
<td>Passes a routine name in <strong>X</strong>, and it returns the checksum in <strong>Y</strong>. Used by <strong>CHECK^XTSUMBLD</strong>. The second line and comments are <em>not</em> included in the total.</td>
</tr>
<tr class="odd">
<td><strong>RSUM1</strong></td>
<td>Passes a routine name in <strong>X</strong>, and it returns the checksum in <strong>Y</strong>. Used by <strong>CHECK1^XTSUMBLD</strong>. The second line and comments are <em>not</em> included in the total.</td>
</tr>
<tr class="even">
<td><strong>SAVE</strong></td>
<td>Saves the code in <strong>@(DIE_”XCN,0)”)</strong> as routine <strong>X</strong>.</td>
</tr>
<tr class="odd">
<td><strong>SIZE</strong></td>
<td>Returns <strong>Y=size</strong> (in bytes) of the current routine.</td>
</tr>
<tr class="even">
<td><strong>SS</strong></td>
<td>Displays the system status.</td>
</tr>
<tr class="odd">
<td><strong>TEST</strong></td>
<td>Returns <strong>$T = 1</strong> if routine <strong>X</strong> exists.</td>
</tr>
<tr class="even">
<td><strong>TMK</strong></td>
<td>Returns <strong>Y = 1</strong> if a tape mark was detected on the last <strong>READ</strong>.</td>
</tr>
<tr class="odd">
<td><strong>TRAP</strong></td>
<td><p>To set the Error Trap:</p>
<blockquote>
<p>&gt;<strong>S X="error routine",@^%ZOSF("TRAP")</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>TRMOFF</strong></td>
<td>Resets terminators to normal.</td>
</tr>
<tr class="odd">
<td><strong>TRMON</strong></td>
<td>Turns on all controls as terminators.</td>
</tr>
<tr class="even">
<td><strong>TRMRD</strong></td>
<td>Returns in <strong>Y</strong> what terminated the last <strong>READ</strong>.</td>
</tr>
<tr class="odd">
<td><strong>TYPE-AHEAD</strong></td>
<td>Allow <strong>TYPE-AHEAD</strong> for the device <strong>$I</strong>.</td>
</tr>
<tr class="even">
<td><strong>UCI</strong></td>
<td>Returns <strong>Y</strong> with the current account (UCI, Volume Set).</td>
</tr>
<tr class="odd">
<td><strong>UCICHECK</strong></td>
<td>Returns <strong>Y’=“”</strong> if <strong>X</strong> is a valid UCI name.</td>
</tr>
<tr class="even">
<td><strong>UPPERCASE</strong></td>
<td>Converts lowercase to uppercase. Setting <strong>X=“User Name”</strong> returns <strong>Y=“USER NAME”</strong>. Applications can gain efficiency by executing this node rather than performing checks within the application program.</td>
</tr>
<tr class="odd">
<td><strong><sup>*</sup>VOL</strong></td>
<td>Contains the current Volume Set (CPU) name.</td>
</tr>
<tr class="even">
<td><strong>XY</strong></td>
<td>Sets <strong>$X=DX</strong> and <strong>$Y=DY</strong> (may <em>not</em> work on all systems).</td>
</tr>
<tr class="odd">
<td><strong>ZD</strong></td>
<td>Given <strong>X</strong> in <strong>$H</strong> format, returns the printable form of <strong>X</strong> in <strong>Y</strong>.</td>
</tr>
</tbody>
</table>

## \$\$ACTJ^%ZOSV: Number of Active Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The \$\$ACTJ^%ZOSV extrinsic function returns the number of active jobs in the scope of this process. It is the same as ^%ZOSF(“ACTJ”).

Format: \$\$ACTJ^%ZOSV

Input Parameters: none.

Output: returns: Returns the number of active jobs.

## \$\$AVJ^%ZOSV: Number of Available Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The \$\$AVJ^%ZOSV extrinsic function returns the best effort on the number of available jobs (that is number of new jobs that could be started). It is the same as ^%ZOSF(“AVJ”).

Format: \$\$AVJ^%ZOSV

Input Parameters: none.

Output: returns: Returns the number of available jobs.

## DOLRO^%ZOSV: Display Local Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Operating System Interface

ICR \#: 3883

Description: The DOLRO^%ZOSV API saves all local variables. It stores all local variables in the global storage location specified by the X input variable.

Format: DOLRO^%ZOSV

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
2.  Set all input variables.
3.  Call the API.

Input Variables: X: (required) When this variable is set to an open global reference, \[such as ’^XTMP(“ZZHL”,25,’\], all local variables existent when DOLRO^%ZOSV is called are stored in the location specified by the open global reference. These variables, now stored in the X-specified global location, can be listed and examined by application developers.

Output: returns: Local variables are stored in the global specified by the X input variable.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950688" class="anchor"></span>Figure 1: DOLRO^%ZOSV API—Example

\><span class="mark">S X="^%ZTSK(ZTSKm.3," D DOLRO^%ZOSV</span>

## GETENV^%ZOSV: Current System Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The GETENV^%ZOSV API returns environment information about the current system.

Format: GETENV^%ZOSV

Input Parameters: none.

Output Variables: Y: Returns a string in the following format:

UCI^VOL/DIR^NODE^BOX LOOKUP

## \$\$LGR^%ZOSV: Last Global Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The \$\$LGR^%ZOSV extrinsic function returns the last global reference.

Format: \$\$LGR^%ZOSV

Input Parameters: none.

Output: returns: Returns the string set to the last full global reference.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950689" class="anchor"></span>Figure 2: \$\$LGR^%ZOSV API—Example

\><span class="mark">S X=\$\$LGR^%ZOSV</span>

## LOGRSRC^%ZOSV(): Record Resource Usage (RUM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The LOGRSRC^%ZOSV API records resource usage in ^XTMP(“KMPR” through the Resource Usage Monitor (RUM) software.

Format: LOGRSRC^%ZOSV(opt,type,status)

Input Parameters: opt: (required) Name of option, protocol, Remote Procedure Call (RPC) or Health Level Seven (HL7). This is a FREE TEXT parameter.

type: (required) Type of option:

- 0—Option
- 1—Protocol
- 2—Remote Procedure Call (RPC)
- 3—Health Level Seven (HL7)

status: (optional) Reserved for future use.

Output: returns: This API saves RUM-related data for each option/type into a file. This file is then downloaded weekly to the Capacity Planning National Database. The data is then available to all sites through the Capacity Planning Service VA Intranet Website.

## \$\$OS^%ZOSV: Get Operating System Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The \$\$OS^%ZOSV extrinsic function returns the underlying operating system (such as VMS on OpenVMS, NT on Windows, Unix on Linux). It is only available under Caché/OpenVMS M systems.

Format: \$\$OS^%ZOSV

Input Parameters: none.

Output: returns: Returns the underlying operating system information (such as VMS on OpenVMS, NT on Windows, Unix on Linux).

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950690" class="anchor"></span>Figure 3: \$\$OS^%ZOSV API—Example

I ^%ZOSF("OS")\["OpenM" S Y=\$\$OS^%ZOSV

## SETENV^%ZOSV: Set VMS Process Name (Caché/OpenVMS Systems)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The SETENV^%ZOSV API sets the VMS process name. It only has meaning on Caché/OpenVMS systems; otherwise, it just quits.

Format: SETENV^%ZOSV

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
4.  Set all input variables.
5.  Call the API.

Input Variables: X: (required) This is a 1-15 character name to be given to the process at the VMS level.

Output: none.

## SETNM^%ZOSV(): Set VMS Process Name (Caché/OpenVMS Systems)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The SETNM^%ZOSV API sets the VMS process name. It only has meaning on Caché/OpenVMS systems; otherwise, it just quits. It is the parameter-passing version of the <u>SETENV^%ZOSV: Set VMS Process Name (Caché/OpenVMS Systems)</u> API.

Format: SETNM^%ZOSV(name)

Input Parameters: name: (required) This is a 1-15 character name to be given to the process at the VMS level.

Output: none.

## T0^%ZOSV: Start RT Measure (Obsolete)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/008.png) NOTE: The T0^%ZOSV API is obsolete as of the release of Kernel Toolkit patch XT\*7.3\*102 and Kernel Patch XU\*8.0\*425.

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The T0^%ZOSV API starts RT Measure. The Kernel site parameter flag to enable RT logging *must* be set for the volume set. The setting of this flag defines the XRTL variable. The call to this API should, thus, include a check for the existence of XRTL, such as the following:

\>D:\$D(xrtl) T0^%ZOSV

This API should be placed just before a process that may take a few seconds before the system responds with another prompt. If the minimal pause is at least a half second, there is enough variability to notice changes as the load on the system is increased or decreased. There should be no terminal IOs between the T0 start point and the T1 stop point.

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/009.png) REF: For more information on RT measure, see the Resource Usage Monitor (RUM) documentation, located on the [RUM application on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=130).

Format: T0^%ZOSV

Input Parameters: none.

> Output Variables: XRT0: Output variable (start time).

> The T0 call sets the XRT0 variable to the start time. To discard a sample, the XRT0 variable should be KILLed. Such a KILL would be appropriate if there is an exit path between the T0 and T1 checkpoints that is circuitous or otherwise irrelevant to the normal execution of the code in question.

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/010.png) NOTE: On Caché systems, it only records to the nearest second.

## T1^%ZOSV: Stop RT Measure (Obsolete)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/011.png) NOTE: The T1^%ZOSV API is obsolete as of the release of Kernel Toolkit patch XT\*7.3\*102 and Kernel Patch XU\*8.0\*425.

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The T1^%ZOSV API stops RT Measure. This API logs the elapsed time into the ^%ZRTL global (obsolete). The API should include a check for the existence of the XRT0 variable to confirm that the start time is available.

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/012.png) REF: For more information on RT measure, see the Resource Usage Monitor (RUM) documentation, located on the [RUM application on the VDL](http://www.va.gov/vdl/application.asp?appid=130).

Format: T1^%ZOSV

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
6.  Set all input variables.
7.  Call the API.

Input Variables: XRTN: (required) Routine name.

The XRTN variable is normally set to the name of the routine being monitored using the following command:

\>S XRTN=\$T(+0)

To log more than one stop point in the same routine, a number or other characters can be concatenated (such as XRTN_1) so that a separate entry is made in the ^%ZRTL global (obsolete), since the global is subscripted by routine name:

\>S:\$D(XRT0) XRTN=\$T(+0) D:\$D(XRT0) T1^%ZOSVOutput: returns: Logs elapsed time into the ^%ZRTL global (obsolete).

## \$\$VERSION^%ZOSV(): Get OS Version Number or Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Operating System Interface

ICR \#: 10097

Description: The \$\$VERSION^%ZOSV extrinsic function returns the operating system version number or name.

Format: \$\$VERSION^%ZOSV(\[flag\])

Input Parameters: flag: (optional) If you pass a value of 1, the operating system name is returned instead of the version number.

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/013.png) NOTE: The name is as defined by the vendor and does *not* necessarily correspond with the OS name stored in ^%ZOSF(“OS”).

Output: returns: Returns the operating system version number or name, depending on the (optional) flag input parameter.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<span id="_Toc199950691" class="anchor"></span>Figure 4: \$\$VERSION^%ZOSV API—Example 1

\><span class="mark">W \$\$VERSION^%ZOSV(1)</span>

Cache for OpenVMS/ALPHA V7.x (Alpha)

#### Example 2

<span id="_Toc199950692" class="anchor"></span>Figure 5: \$\$VERSION^%ZOSV API—Example 2

\><span class="mark">W \$\$VERSION^%ZOSV</span>

4.1.16

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/014.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/015.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-operating-system-interface-user-guide/016.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.