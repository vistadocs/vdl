---
title: PRS*4*132/133 Upgrade ETA for Telework Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Upgrade ETA for Telework
app_code: PRS
app_name: Personnel and Accounting Integrated Data (PAID)
section: FIN
app_status: active
pkg_ns: PRS
patch_ver: 4
patch_id: PRS*4*132
group_key: "PRS:PRS:4"
file_numbers: []
security_keys: []
menu_options: 0
description: This patch introduces the functionality changes that must be made to the VistA Personnel and Accounting Integrated Data/Enhanced Time and Attendance (PAID/ETA) software to support the Telework Enhancement Act of 2010 (Public Law 111-292), approved by President Barack Obama on December 9, 2010. The a
audience: 
keywords: 
  - installation
  - time
  - table
  - patch
  - contents
  - install
  - options
  - paid
  - kids
  - transport
page_count: 0
word_count: 1281
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_4_p132_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_4_p132_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=51"
---

Upgrade ETA For Telework

Installation Guide

![](prs-4-132-133-upgrade-eta-for-telework-installation-guide/001.png)

For Patches PRS\*4.0\*132, PRS\*4.0\*133

July 2012

Product Development (PD)

Revision History

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 39%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>7/31/12</td>
<td>1.0</td>
<td>This first draft is based on the FORUM patch description and information This covers Patch PRS*4.0*133 and PRS*4.0*132.</td>
<td><p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

# PRS\*4.0\*132 (Telework Tracking)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [PRS\4.0\132 (Telework Tracking)](#prs40132-telework-tracking)
  - [Introduction](#introduction)
    - [Installation Time](#installation-time)
    - [Installation Procedure](#installation-procedure)
- [PRS\4.0\133 (Comp Time Expiration Updates)](#prs40133-comp-time-expiration-updates)
  - [Introduction](#introduction-1)
    - [Installation Time](#installation-time-1)
    - [Installation Procedure](#installation-procedure-1)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch introduces the functionality changes that must be made to the VistA Personnel and Accounting Integrated Data/Enhanced Time and Attendance (PAID/ETA) software to support the Telework Enhancement Act of 2010 (Public Law 111-292), approved by President Barack Obama on December 9, 2010. The act provides the Federal Government with improved flexibility in managing its workforce through the use of telework. The Act directs federal agencies to satisfy mandatory data collection and reporting requirements beginning with the first report to Congress not later than 18 months from enactment (June 2012) and on an annual basis thereafter. This includes identifying and reporting the number of hours their employees telework. Specifically, this patch introduces functionality updates to account for scheduled, unscheduled, and medical telework hours performed by Veterans Affairs employees.

This patch may be installed with users on the system, however, it should be installed at a non-peak time to minimize disruption to the users. It is strongly recommended that all the PAID ETA options in the OPTION (#19) file be disabled to prevent possible conflicts while running the KIDS install. All the ETA options can be selected by using the PAID ETA namespace of PRS and the asterisk. As shown in step 4d. of the installation instructions, type PRS\*, to disable all PAID ETA options. Other VISTA users will not be affected.

### Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This procedure takes less than five minutes to complete.

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. LOAD TRANSPORT GLOBAL

Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.

2\. START UP KIDS

Start up the Kernel Installation and Distribution System Menu

\[XPD MAIN\]:

> Edits and Distribution ...

> Utilities ...

> Installation ...

Select the Kernel Installation & Distribution System Option: INStallation

> Load a Distribution

> Print Transport Global

> Compare Transport Global to Current System

> Verify Checksums in Transport Global

> Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Backup a Transport Global

3\. Select Installation Option:

> **NOTE:** The following are OPTIONAL: (When prompted for the INSTALL NAME, enter PRS\*4.0\*132):

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch.
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

4\. Select Installation Option: Install Package(s)

This is the step to start the installation of this KIDS patch:

1.  Choose the Install Package(s) option to start the patch install.
2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//' Answer NO.
3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//' answer NO.
4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//' answer YES.
5.  When prompted 'Enter options you wish to mark as 'Out Of Order':' Answer: PRS\*
6.  When prompted 'Enter protocols you wish to mark as 'Out Of Order':' Press Return.

# PRS\*4.0\*133 (Comp Time Expiration Updates)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The provisions for the expiration of Comp Time and Credit Hours were revised effective February 18, 2007. The time period in which an employee may use earned compensatory time was revised from 8 pay periods to 26 periods. The time limit on the use of earned Credit Hours was eliminated. However, the restriction on carrying no more than 24 credit hours into the next pay period continues to apply.

Compensatory Time and Credit Hours will continue to be stored in the same balance and if necessary, ETA users will continue to manually track the portion of the balances that are credit hours.

Since the revision to the expiration of comp time rules, the Austin Automation Technology Center (AITC) was updated to support storing 26 pay periods of comp time which is reported to the AITC each pay period from VistA PAID/ETA.

AITC was also updated to maintain the total balance of an employee's COMPTIME/CREDIT HOURS and transmit that to VISTA PAID ETA in the existing COMPTIME download field. The value transmitted from AITC to VistA PAID ETA each pay period is the current unused balance of COMPTIME/CREDIT HRS earned over the last 26 pay periods and ETA stores this balance in the PAID EMPLOYEE file (#450) in the COMPTIME/CREDIT HRS BALANCE field (#496).

This patch updates the following options in VistA PAID ETA to use the correct total comp time/credit hours balance and to extend the expiration of comp time from 8 to 26 pay periods from when it was earned.

This patch may be installed with users on the system, however, it should be installed at a non-peak time to minimize disruption to the users. It is strongly recommended that all the PAID ETA options in the OPTION (#19) file be disabled to prevent possible conflicts while running the KIDS install. All the ETA options can be selected by using the PAID ETA namespace of PRS and the asterisk. As shown in step 4d. of the installation instructions, type PRS\*, to disable all PAID ETA options. Other VISTA users will not be affected.

### Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This procedure takes less than five minutes to complete.

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. LOAD TRANSPORT GLOBAL

Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.

2\. START UP KIDS

Start up the Kernel Installation and Distribution System Menu

\[XPD MAIN\]:

> Edits and Distribution ...

> Utilities ...

> Installation ...

Select Kernel Installation & Distribution System Option: INStallation

> Load a Distribution

> Print Transport Global

> Compare Transport Global to Current System

> Verify Checksums in Transport Global

> Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Backup a Transport Global

3\. Select Installation Option:

> **NOTE:** The following are OPTIONAL: (When prompted for the INSTALL NAME, enter PRS\*4.0\*133):

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch.
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

4\. Select Installation Option: Install Package(s)

This is the step to start the installation of this KIDS patch:

1.  Choose the Install Package(s) option to start the patch install.
2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//' Answer NO.
3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//' answer NO.
4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//' answer YES.
5.  When prompted 'Enter options you wish to mark as 'Out Of Order':'

> Answer:

> Leave Balances \[PRSA LV BAL-EMP\]

> Employee Leave Balances \[PRSA LV BAL-TK\]

> Employee Leave Balances \[PRSA LV BAL-SUP\]

> Supervisory Approvals \[PRSA SUP CERT\]

f\. When prompted 'Enter protocols you wish to mark as 'Out Of Order':' Press Return.