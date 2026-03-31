---
title: IVMB*2*453 Priority Letters Phase 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Priority Letters Phase 1
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*453
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 3
description: "- [Installation Instructions](#installation-instructions) This patch can be loaded with users on the system. Installation will take less than 5 minutes. However, the post install will task two jobs: > Job Purpose > EN^IVMB453A Calculates sub-priorities > POST3A^IVMB453 Builds AF New-Style Index Thes"
audience: 
keywords: 
  - letter
  - installation
  - patch
  - enrollment
  - install
  - ivmb
  - blockquote
  - letters
  - table
  - aycb
page_count: 0
word_count: 607
section_count: 1
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/pl_pivmb_2_453_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/pl_pivmb_2_453_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

![](ivmb-2-453-priority-letters-phase-1-installation-guide/001.png)

Priority Letters Phase I

Installation Guide

Health Eligibility Center (HEC)  
Module

Patch IVMB\*2\*453

October 2000

*VISTA* Technical Services

# Installation Instructions


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Installation Instructions](#installation-instructions)
This patch can be loaded with users on the system. Installation will take less than 5 minutes. However, the post install will task two jobs:
> Job Purpose
> EN^IVMB453A Calculates sub-priorities
> POST3A^IVMB453 Builds AF New-Style Index
These jobs will take several days to run.
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>IMPORTANT!</strong></td>
<td><p>This patch MUST NOT be installed if any of the following tasks are running:</p>
<ul>
<li><blockquote>
<p>Determine veteran letter requirements<br />
[AYCB DETERMINE VETERANS LETTER]</p>
</blockquote></li>
<li><blockquote>
<p>Generate Enrollment Letter File [AYCB FILE ENROLLMENT LETTER]</p>
</blockquote></li>
<li><blockquote>
<p>Resend Enrollment Correspondence [AYCBLTR5 RESEND LETTERS]</p>
</blockquote></li>
</ul>
<p>Check TaskMan's scheduled and current task list for the listed tasks. If any of the listed tasks are scheduled to be run while the patch is being installed, either remove the tasks from the schedule, or wait to install this patch later.</p></td>
</tr>
</tbody>
</table>
|             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Warning | After installation of patch IVMB\*2.0\*453, KIDS will attempt to rebuild all user menus whenever an Option is added via KIDS. This can be a lengthy process (several hours). If you are running the install interactively, you will be prompted for a start time for the menu rebuild. However, if you are not running this installation interactively, KIDS will start the menu rebuild immediately after the installation completes. Therefore, you may wish to queue the installation to run at a time of low system activity to accommodate the menu rebuild. |
To install the patch
1.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu  
    \[Note: TEXT PRINT/DISPLAY option in the PackMan menu will display the patch text only\].
2.  Review your mapped set. If any of the routines listed in the ROUTINE SUMMARY section are mapped, they should be removed from the mapped set at this time.
3.  From the Kernel Installation and Distribution System (KIDS) menu, select the Installation menu.
4.  From Installation menu, you may elect to use the following options: (when prompted for INSTALL NAME, enter IVMB\*2.0\*453)
    1.  Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.
    2.  Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  Verify Checksums in Transport Global - this option will allow you to ensure the integrity of the routines that are in the transport global.
    4.  Print Transport Global - this option will allow you to view the components of the KIDS build.
5.  Use the Install Package(s) option and select the package IVMB\*2.0\*453.
6.  When prompted Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//, respond YES. When prompted to select the options you would like to place out of order, enter the following:
1.  Determine veteran letter requirements \[AYCB DETERMINE VETERANS LETTER\]
2.  Generate Enrollment Letter File \[AYCB FILE ENROLLMENT LETTER\]
3.  Resend Enrollment Correspondence \[AYCBLTR5 RESEND LETTERS\]
4.  Mail/Remail Enrollment Letter \[AYCB MAIL/REMAIL LETTER\]
7.  When prompted Run the process to calculate sub-priorities? YES//, respond YES. This will task the process to calculate sub-priorities to run immediately after installation has completed.
8.  If routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has run to completion.
9.  When the post install initiated task EN^IVMB453A (calculates sub-priorities) and POST3A^IVMB453 (builds AF New-Style Index) finish, notify HEC system personnel. They should be informed that they can now initiate the Notify Enrollee Of Priority (600B) Letter \[AYCBLTRA ENROLLMENT 600B LTR\] option, which will generate the VMS file(s) with the data for the 600B letters. Note that for the previously tasked options that were unscheduled or stopped, they should not be rescheduled until after the Notify Enrollee of Priority (600B) Letter process has successfully terminated.
