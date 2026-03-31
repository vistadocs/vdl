---
title: "Kernel 8.0 Developerâ€™s Guide: Spooling User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Spooling"
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
  - guide
  - kernel
  - developer
  - spooling
  - table
  - span
  - contents
  - ztio
  - spool
  - document
page_count: 0
word_count: 1008
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_spooling_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_spooling_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259569" class="anchor"></span>Spooling Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-spooling-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-spooling-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Spooling Developer Tools User Guide</em>.</p>
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

<span id="_Toc234301876" class="anchor"></span>List of Figures

[Figure 1: Spooling—Sending Output to the Spooler (and Pre-defining ZTIO) [2](#_Toc200270033)](#_Toc200270033)

[Figure 2: Spooling—Allowing Output to Go the Spooler (*without* Pre-defining ZTIO) [2](#_Toc200270034)](#_Toc200270034)

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-spooling-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [DSD^ZISPL: Delete Spool Data File Entry](#dsdzispl-delete-spool-data-file-entry)
  - [DSDOC^ZISPL: Delete Spool Document File Entry](#dsdoczispl-delete-spool-document-file-entry)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide:* Spooling Developer Tools *User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For an application to spool reports, the application *must* call the Device Handler to open the spool device. If the application fails to close the device, the spool document is *not* accessible. The application should close the spool device by using the following:

\>D ^%ZISC

Furthermore, queuing to the spooler requires that the application invoke [^%ZTLOAD](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.pdf#ztload) with the proper variables defined.

The ZTIO input variable can be set to identify how the device should be opened. If incorrectly set up, the queued task could fail to send results to the spooler. If you have any doubt about how to set ZTIO, you should leave it undefined. [^%ZTLOAD](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.pdf#ztload) can define ZTIO with the appropriate variables from symbols left in the current partition following the last call to the Device Handler.

![](kernel-8-0-developer-s-guide-spooling-user-guide/004.png) NOTE: The following code samples are *not* complete. They do *not* contain code to issue form feeds between pages of output.  
  
REF: For the details of issuing form feeds, see the “Form Feeds” section in the “Special Device Issues” section in the [*Kernel 8.0 Developer’s Guide: Device Handler Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#Form_Feeds).

<span id="_Toc200270033" class="anchor"></span>Figure 1: Spooling—Sending Output to the Spooler (and Pre-defining ZTIO)

SAMPLE ;SAMPLE ROUTINE

;

S %ZIS="QM" D ^%ZIS G EXIT:POP

I \$D(IO("Q")) D D ^%ZTLOAD D HOME^%ZIS K IO("Q") Q

.S ZTRTN="DQ^SAMPLE",ZTDESC="Sample Test routine"

.S ZTIO=ION\_";"\_IOST

.I \$D(IO("DOC"))#2,IO("DOC")\]"" S ZTIO=ZTIO\_";"\_IO("DOC") Q

.I IOM S ZTIO=ZTIO\_";"\_IOM

.I IOSL S ZTIO=ZTIO\_";"\_IOSL

DQ U IO W !,"THIS IS YOUR REPORT"

W !,"LINE 2"

W !,"LINE 3"

D ^%ZISC

EXIT S:\$D(ZTQUEUED) ZTREQ="@" K VAR1,VAR2,VAR3 Q

<span id="_Toc200270034" class="anchor"></span>Figure 2: Spooling—Allowing Output to Go the Spooler (*without* Pre-defining ZTIO)

SAMPLE ;SAMPLE ROUTINE

;

S %ZIS="QM" D ^%ZIS G EXIT:POP

I \$D(IO("Q")) D Q

.S ZTRTN="DQ^SAMPLE",ZTDESC="Sample Test routine"

.D ^%ZTLOAD D HOME^%ZIS K IO("Q") Q

DQ U IO W !,"THIS IS YOUR REPORT"

W !,"LINE 2"

W !,"LINE 3"

D ^%ZISC

EXIT S:\$D(ZTQUEUED) ZTREQ="@" K VAR1,VAR2,VAR3 Q

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Spooling APIs are available for developers. These APIs are described below.

## DSD^ZISPL: Delete Spool Data File Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Spooling

ICR \#: 1092

Description: The DSD^ZISPL API deletes SPOOL DATA (#3.519) file entry following transfer of data, to minimize consumption of data.

Format: DSD^ZISPL

Input Parameters: none.

Output: none.

## DSDOC^ZISPL: Delete Spool Document File Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Spooling

ICR \#: 1092

Description: The DSDOC^ZISPL API deletes the SPOOL DOCUMENT (#3.51) file entry following transfer of data, to minimize consumption of disk space.

Format: DSDOC^ZISPL

Input Parameters: none.

Output: none.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-spooling-user-guide/005.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-spooling-user-guide/006.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-spooling-user-guide/007.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.