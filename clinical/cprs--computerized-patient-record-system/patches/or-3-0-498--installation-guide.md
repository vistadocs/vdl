---
title: OR*3.0*498 CPRS (v31b followup) Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: CPRS (v31b followup)
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*498
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: CPRS v31b Follow-Up Build is a multi-package build that addresses several defects identified during the deployment of the CPRS v31b series of patches.
audience: 
keywords: 
  - table
  - cprs
  - contents
  - install
  - send
  - site
  - installation
  - build
  - routine
  - follow
page_count: 0
word_count: 7011
section_count: 24
table_count: 1
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: December 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_498_dibr_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_498_dibr_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Computerized Patient Record System (CPRS)  
  Version 31b Follow-Up Build
---

Deployment, Installation, Back Out and Rollback Guide

![](or-3-0-498-cprs-v31b-followup-deployment-installation-back-out-and-rollback-guid/001.png)

December 2021

Office of Information & Technology (OI&T)

Enterprise Program Management Office (EPMO)

Revision History

<table style="width:100%;">
<caption><p>Table 2 - CPRS v31b Follow-Up Build</p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 23%" />
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
<td>12/13/2021</td>
<td>0.12</td>
<td>Redacted for the VDL: removed names and links to software builds</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>12/01/2021</td>
<td>0.11</td>
<td>Added section 8.1.1 (Disable Protocol PSO LM PAT PREG/LACT DISPLAY).<br />
<br />
Renamed Section 5 “"Documentation and Software Retrieval" and moved section 7.1 (Documentation) to 5.1.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>10/5/2021</td>
<td>0.10</td>
<td>Updated all the screenshots in Section 7 (Test System Installation) and Appendices A, B, C, and D.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>9/1/2021</td>
<td>0.09`</td>
<td><p>Updated all the examples in the Test System Installation section and the appendices.</p>
<p>Updated the instructions in the “Install the Build” sub-section (Test System Installation section, instruction #4).</p></td>
<td>CPRS Development team</td>
</tr>
<tr class="odd">
<td>6/16/2021</td>
<td>0.08</td>
<td>Added PXRM*2.0*42 to the list of pre-requisite patches. Updated all of the examples in Section 7 (Test System Installation) and in Appendices A, B, C, and D.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>5/11/2021</td>
<td>0.07</td>
<td>Updated the Test System Installation section and Appendices A, B, C and D. Updated PXRM*2.0*45 to PXRM*2.0*75.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>3/2/2021</td>
<td>0.06</td>
<td>Updated the Overview, Pre-Requisite Patches, Test System Installation Checklist, Software Retrieval and Test System Installation sections.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>12/10/2020</td>
<td>0.05</td>
<td>Removed all the instructions in the pre- and post-installation sections because they are now documented in the “CPRS v31b Follow-Up Build Setup and Configuration Guide”.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>12/4/2020</td>
<td>0.04</td>
<td>Updated the pre-installation steps and the post-installation sections</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>10/16/2020</td>
<td>0.03</td>
<td>Updated the backout and pre- and post-installation sections</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>10/1/2020</td>
<td>0.02</td>
<td>Technical Writer Edits</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>8/31/2020</td>
<td>0.01</td>
<td>Initial Draft</td>
<td>CPRS Development Team</td>
</tr>
</tbody>
</table>

Table 2 - CPRS v31b Follow-Up Build

Table of Contents

# CPRS v31b Follow-Up Build


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [CPRS v31b Follow-Up Build](#cprs-v31b-follow-up-build)
  - [Overview](#overview)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [Document Conventions](#document-conventions)
  - [Related Documents](#related-documents)
- [Pre-requisites](#pre-requisites)
  - [Pre-requisite Patches](#pre-requisite-patches)
- [Reporting Issues](#reporting-issues)
- [Test System Installation Checklist](#test-system-installation-checklist)
- [Documentation and Software Retrieval](#documentation-and-software-retrieval)
  - [Documentation](#documentation)
  - [Software](#software)
- [Test System Pre-Installation Steps](#test-system-pre-installation-steps)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Backup Procedures](#backup-procedures)
    - [Back-Up Globals](#back-up-globals)
- [Test System Installation](#test-system-installation)
- [Test System Post-Installation Tasks (Installation Verification Procedure)](#test-system-post-installation-tasks-installation-verification-procedure)
  - [System Configuration](#system-configuration)
    - [Disable Protocol PSO LM PAT PREG/LACT DISPLAY](#disable-protocol-pso-lm-pat-preglact-display)
  - [Database Tuning](#database-tuning)
- [Testing in the Test Account](#testing-in-the-test-account)
- [Production System Installation Checklist](#production-system-installation-checklist)
- [Production System Pre-Installation Steps](#production-system-pre-installation-steps)
  - [Backup Procedures](#backup-procedures-1)
    - [Back Up Globals](#back-up-globals-1)
- [Production System Installation](#production-system-installation)
- [Production System Post-Installation Tasks](#production-system-post-installation-tasks)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B: Post-Install Checksums](#appendix-b-post-install-checksums)
- [Appendix C: Install File Print Example](#appendix-c-install-file-print-example)
- [Appendix D: Build File Print Example](#appendix-d-build-file-print-example)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31b Follow-Up Build is a multi-package build that addresses several defects identified during the deployment of the CPRS v31b series of patches.

The CPRS v31b Follow-Up build consists of the following patches:

- OR\*3.0\*498
- WV\*1.0\*26
- PXRM\*2.0\*71
- PSO\*7.0\*622
- TIU\*1.0\*341

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) Information Resource Management (IRM) staff.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to install, back-out, and roll-back the CPRS v31b Follow-Up multi-package build.

> This document is a companion to the project charter and management plan for this effort.

> Pre- and Post-installation instructions are not documented in this guide. Instead, they are documented in the “CPRS v31b Follow-Up Build Setup and Configuration Guide”.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Examples of VistA “Roll and Scroll” interface actions will be shown in a box such as this:

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

Emphasis of important points may be displayed in this manner:

> NOTE: This is an important point and must not be omitted.

Call-outs may be used to draw attention to part of a block of text or a table without disrupting the flow of the block or table. For example:  
  
![](or-3-0-498-cprs-v31b-followup-deployment-installation-back-out-and-rollback-guid/002.png)

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents, in addition to this document, will be available on the VA Software Document Library (VDL) when the patch is released:

[CPRS on the VDL](http://www.va.gov/vdl/application.asp?appid=61)

- *CPRS User Guide: GUI Version*
- *CPRS Technical Manual*
- *CPRS Technical Manual: GUI Version*
- *CPRS Release Notes: v31b Follow-Up Build*
- *CPRS v31b Follow-Up Build Setup and Configuration Guide*

# Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the installation processes described in this document, the tasks outlined in this section must be completed.

## Pre-requisite Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31b Follow-Up Build expects a fully patched VistA system.

In addition, these patches are required before the CPRS v31b Follow-Up Build can be installed:

- WV\*1.0\*24
- PXRM\*2.0\*42
- PXRM\*2.0\*75
- PSO\*7.0\*381
- PSO\*7.0\*468
- PSO\*7.0\*504
- PSO\*7.0\*556
- PSO\*7.0\*564
- TIU\*1.0\*120
- TIU\*1.0\*204
- TIU\*1.0\*290
- OR\*3.0\*413
- OR\*3.0\*512
- OR\*3.0\*519
- PSS\*1.0\*238

# Reporting Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To report issues with CPRS v31b Follow-Up build, please enter a ticket with the National Help Desk.

# Test System Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order. Use this checklist and the following sections for both your test/mirror system as well as your production system.

Table 1 Installation Checklist

<table>
<caption><p>Table 1 - CPRS v31b Follow-Up Build files</p></caption>
<colgroup>
<col style="width: 8%" />
<col style="width: 82%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>No.</strong></th>
<th><strong>Task</strong></th>
<th><strong>Done</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li></li>
</ol></td>
<td>Confirm your system is fully patched. (See Section 2.1.)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td>Retrieve the software. (See Section 5.)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Make sure the pre-installation has been completed. (See the “CPRS v31b Follow-Up Build Setup and Configuration Guide”.)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Complete the installation. (See Section 7.)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td>Make sure the post-Installation tasks have been completed. (See the “CPRS v31b Follow-Up Build Setup and Configuration Guide”.)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Verify the installation was successful. (See Section 8.)</td>
<td></td>
</tr>
</tbody>
</table>

Table 1 - CPRS v31b Follow-Up Build files

# Documentation and Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table shows the documentation released with CPRS v31b Follow-Up Build:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 35%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>File Names</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>CPRS v31b Follow-Up Build Deployment, Installation, Back Out and Rollback Guide (DIBORG)</em></td>
<td><p>or_3_0_498_dibr.docx</p>
<p>or_3_0_498_dibr.pdf</p></td>
<td>Primarily for installers. Contains items that must be done during the patch installation.</td>
</tr>
<tr class="even">
<td><em>CPRS v31b Follow-Up Build Setup and Configuration Guide</em></td>
<td><p>or_3_0_498_setup.docx</p>
<p>or_3_0_498_setup.pdf</p></td>
<td>Primarily for CACs. Contains items that must be done before and after the patch installation.</td>
</tr>
</tbody>
</table>

Documentation is available on the VA Software Documentation Library at: https://www.va.gov/vdl/.

Documentation can also be obtained at:  
REDACTED

## Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v31b Follow-Up Build files are listed in Table 1.

| CPRS Version files to be downloaded | File Contents / Supported Functionality                     |
|-----------------------------------------|-----------------------------------------------------------------|
| CPRSV31B_FOLLOW_UP.KID                  | Contains the required patches for the CPRS v31b Follow Up Build |

CPRSV31B_FOLLOW_UP.KID is in the REDACTED directory, which is available on all VistA instances.

# Test System Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre-installation instructions are listed in the “CPRS v31b Follow-Up Build Setup and Configuration Guide”. They must be performed by the Clinical Application Coordinator (CAC).

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backup procedures are listed in the “CPRS v31b Follow-Up Build Setup and Configuration Guide”. These procedures must be performed by the CAC.

### Back-Up Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Test System Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section gives instructions for installing the CPRS v31b Follow-Up build, which includes patches OR\*3.0\*498, WV\*1.0\*26, PXRM\*2.0\*71, PSO\*7.0\*622 and TIU\*1.0\*341.

> NOTE: Installation should be performed by a user with programmer access and knowledge of installing host files using Kernel Installation and Distribution System \[XPD MAIN\].

This patch can be loaded with users on the system, but it should be done during off-hours. Estimated installation time is less than 10 minutes.

1.  Retrieve the file that contains the build:  
    The software for this patch is released using a host file. The host file is available at the following location:  
    REDACTED

> NOTE: For test site installations, please refer to the build announcement for the location and name of the file to install.

2.  Load the Distribution:
    1.  From the Kernel Installation and Distribution System Menu, select the “Installation” menu and then select the option, “Load a Distribution”.
    2.  At the “Enter a Host File” prompt, enter the directory and file name from above.
    3.  At the “Want to Continue with Load? YES//” prompt, press the ENTER key.
    4.  At the “Want to RUN the Environment Check Routine? YES//” prompt, press the ENTER key.

> Example – Load the Distribution

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: REDACTED

KIDS Distribution saved on Sep 29, 2021@15:09:09

Comment: CPRS V31B FOLLOW-UP PATCHES 1.0 v16, WV\*1.0\*26 v16, PXRM\*2.0\*71 v16, PS

O\*7.0\*622 v16, TIU\*1.0\*341 v15, OR\*3.0\*498 v15

This Distribution contains Transport Globals for the following Package(s):

CPRS V31B FOLLOW-UP PATCHES 1.0

WV\*1.0\*26

PXRM\*2.0\*71

PSO\*7.0\*622

TIU\*1.0\*341

OR\*3.0\*498

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

CPRS V31B FOLLOW-UP PATCHES 1.0

WV\*1.0\*26

PXRM\*2.0\*71

PSO\*7.0\*622

TIU\*1.0\*341

OR\*3.0\*498

Use INSTALL NAME: CPRS V31B FOLLOW-UP PATCHES 1.0 to install this Distribution.

3.  From the Installation menu, you may choose any of the following options:
    1.  Backup a Transport Global:
        1.  Use the KIDS Installation option, “Backup a Transport Global \[XPD BACKUP\]”.

> This option creates a KIDS host file that will back up all current routines, data dictionaries and other components on your VistA/M system, which will be replaced by the builds in this transport global.

2.  At the “Select INSTALL NAME:” prompt, enter “CPRS V31B FOLLOW-UP PATCHES 1.0”.
3.  At the “Backup Type: B//” prompt, press the ENTER key.
4.  At the “Enter a Host File:” prompt, enter the path and filename where you want the backup created.
5.  At the “Header Comment:” prompt, press the ENTER key.

Example – Backup a Transport Global

Select Installation \<TEST ACCOUNT\> Option: 5 Backup a Transport Global

Select INSTALL NAME: CPRS V31B FOLLOW-UP PATCHES 1.0 Loaded from Distribut

ion 9/30/21@08:37:05

=\> CPRS V31B FOLLOW-UP PATCHES 1.0 v16, WV\*1.0\*26 v16, PXRM\*2.0\*71 v16, P

This Distribution was loaded on Sep 30, 2021@08:37:05 with header of

CPRS V31B FOLLOW-UP PATCHES 1.0 v16, WV\*1.0\*26 v16, PXRM\*2.0\*71 v16, PSO\*7.0\*

622 v16, TIU\*1.0\*341 v15, OR\*3.0\*498 v15 ;Created on Sep 29, 2021@15:09:09

It consisted of the following Install(s):

CPRS V31B FOLLOW-UP PATCHES 1.0 WV\*1.0\*26 PXRM\*2.0\*71 PSO\*7.0\*622

TIU\*1.0\*341 OR\*3.0\*498

Subject: Backup of CPRS V31B FOLLOW-UP PATCHES 1.0, WV\*1.0\*26, PXRM\*2.0\*

Replace

Select one of the following:

B Build (including Routines)

R Routines Only

Backup Type: B// uild (including Routines)

Enter a Host File: /replace_with_backup_directory/CPRSV31B_FOLLOW_UP_BACKUP.KID

Header Comment: Backup of CPRS V31B FOLLOW-UP PATCHES 1.0, WV\*1.0\*26, PXRM\*2.0\*

Replace

No Package File Link

WV1026P in ROUTINE File \*\* NOT FOUND \*\*

WVRPCGF2 in ROUTINE File \*\* NOT FOUND \*\*

WVUTL12 in ROUTINE File \*\* NOT FOUND \*\*

WV MAIL GROUP ISSUE in PARAMETER DEFINITION File \*\* NOT FOUND \*\*

WV BREAST IMAGE TERM LINKING in PARAMETER DEFINITION File \*\* NOT FOUND \*\*

PXRMDGFC in ROUTINE File \*\* NOT FOUND \*\*

PXRMP71I in ROUTINE File \*\* NOT FOUND \*\*

PSO LM PAT PREG/LACT DISPLAY in PROTOCOL File \*\* NOT FOUND \*\*

Protocol PSO HIDDEN ACTIONS has an Action of 'USE AS LINK FOR MENU ITEMS' and no

'Menu Items' were sent.

Protocol PSO HIDDEN ACTIONS \#1 has an Action of 'USE AS LINK FOR MENU ITEMS' and

no 'Menu Items' were sent.

Protocol PSO HIDDEN ACTIONS \#2 has an Action of 'USE AS LINK FOR MENU ITEMS' and

no 'Menu Items' were sent.

Protocol PSO PMP HIDDEN ACTIONS MENU \#2 has an Action of 'USE AS LINK FOR MENU I

TEMS' and no 'Menu Items' were sent.

Protocol PSO HIDDEN ACTIONS \#3 has an Action of 'USE AS LINK FOR MENU ITEMS' and

no 'Menu Items' were sent.

TIU341P in ROUTINE File \*\* NOT FOUND \*\*

TIUCROBJ in ROUTINE File \*\* NOT FOUND \*\*

ORS100C in ROUTINE File \*\* NOT FOUND \*\*

ORY498 in ROUTINE File \*\* NOT FOUND \*\*

OR CS ORDER ANOMALIES in OPTION File \*\* NOT FOUND \*\*

OR CPRS DEBUG EMAIL in PARAMETER DEFINITION File \*\* NOT FOUND \*\*

Option OR PARAM COORDINATOR MENU has an Action of 'USE AS LINK FOR MENU ITEMS' a

nd no 'Menu Items' were sent.

Package Transported Successfully

2.  Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.)

3.  Verify Checksums in Transport Global

> This option will allow you to ensure the integrity of the routines that are in the transport global.

> NOTE: If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in downloading) and Load the Distribution again.  

> If the problem still exists, log a ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

Example – Verify Checksums in Transport Global

Select Installation \<TEST ACCOUNT\> Option: 2 Verify Checksums in Transport Glob

al

Select INSTALL NAME: CPRS V31B FOLLOW-UP PATCHES 1.0 Loaded from Distribut

ion

9/30/21@08:37:05

=\> CPRS V31B FOLLOW-UP PATCHES 1.0 v16, WV\*1.0\*26 v16, PXRM\*2.0\*71 v16, P

This Distribution was loaded on Sep 30, 2021@08:37:05 with header of

CPRS V31B FOLLOW-UP PATCHES 1.0 v16, WV\*1.0\*26 v16, PXRM\*2.0\*71 v16, PSO\*7.0\*

622 v16, TIU\*1.0\*341 v15, OR\*3.0\*498 v15 ;Created on Sep 29, 2021@15:09:09

It consisted of the following Install(s):

CPRS V31B FOLLOW-UP PATCHES 1.0 WV\*1.0\*26 PXRM\*2.0\*71 PSO\*7.0\*622

TIU\*1.0\*341 OR\*3.0\*498

Want each Routine Listed with Checksums: Yes// YES

DEVICE: HOME// REDACTED Virtual Terminal

4.  Install the Build:

> NOTE: Do not queue the installation. A queued installation will generate an error and will not successfully complete.

1.  From the Kernel Installation and Distribution System (KIDS) menu, select the Installation menu.
2.  When prompted with “Select Installation Option”, select “Install Package(s)”.
3.  When prompted with “Select INSTALL NAME”, select “CPRS V31B FOLLOW-UP PATCHES 1.0”.
4.  Proceed with the install and answer these questions as follows:
    1.  Although the answer is usually “No”, you can answer “Yes”, to the question, “Want KIDS to Rebuild Menu Trees Upon Completion of Install?”

> NOTE: Rebuilding menu trees will increase patch installation time.

2.  When prompted with “Want KIDS to INHIBIT LOGONs during the install?”, select “No”.
3.  When prompted with “Want to DISABLE Scheduled Options, Menu Options and Protocols?”, select “No”.
5.  When prompted with “Device”, press the ENTER key.

> NOTE: Do not queue the installation. A queued installation will generate an error and will not successfully complete.

> Example – Install the Build

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: CPRS V31B FOLLOW-UP PATCHES 1.0 Loaded from Distribu

tion

9/30/21@08:37:05

=\> CPRS V31B FOLLOW-UP PATCHES 1.0 v16, WV\*1.0\*26 v16, PXRM\*2.0\*71 v16, P

This Distribution was loaded on Sep 30, 2021@08:37:05 with header of

CPRS V31B FOLLOW-UP PATCHES 1.0 v16, WV\*1.0\*26 v16, PXRM\*2.0\*71 v16, PSO\*7.0\*

622 v16, TIU\*1.0\*341 v15, OR\*3.0\*498 v15 ;Created on Sep 29, 2021@15:09:09

It consisted of the following Install(s):

CPRS V31B FOLLOW-UP PATCHES 1.0 WV\*1.0\*26 PXRM\*2.0\*71 PSO\*7.0\*622

TIU\*1.0\*341 OR\*3.0\*498

Checking Install for Package CPRS V31B FOLLOW-UP PATCHES 1.0

Install Questions for CPRS V31B FOLLOW-UP PATCHES 1.0

Checking Install for Package WV\*1.0\*26

Install Questions for WV\*1.0\*26

Incoming Files:

790.1 WV PROCEDURE (Partial Definition)

> **NOTE:** You already have the 'WV PROCEDURE' File.

790.4 WV NOTIFICATION (Partial Definition)

> **NOTE:** You already have the 'WV NOTIFICATION' File.

790.403 WV NOTIFICATION TYPE (including data)

> **NOTE:** You already have the 'WV NOTIFICATION TYPE' File.

I will OVERWRITE your data with mine.

790.404 WV NOTIFICATION PURPOSE (including data)

> **NOTE:** You already have the 'WV NOTIFICATION PURPOSE' File.

I will OVERWRITE your data with mine.

790.9 WV PREGNANCY/LACTATION STATUS CONFLICT EVENTS

> **NOTE:** You already have the 'WV PREGNANCY/LACTATION STATUS CONFLICT EVENTS' File

.

Checking Install for Package PXRM\*2.0\*71

Install Questions for PXRM\*2.0\*71

Incoming Files:

801.41 REMINDER DIALOG (Partial Definition)

> **NOTE:** You already have the 'REMINDER DIALOG' File.

811.4 REMINDER COMPUTED FINDINGS (including data)

> **NOTE:** You already have the 'REMINDER COMPUTED FINDINGS' File.

I will OVERWRITE your data with mine.

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Checking Install for Package PSO\*7.0\*622

Install Questions for PSO\*7.0\*622

Checking Install for Package TIU\*1.0\*341

Install Questions for TIU\*1.0\*341

Checking Install for Package OR\*3.0\*498

Install Questions for OR\*3.0\*498

Incoming Files:

100.9 OE/RR NOTIFICATIONS (including data)

> **NOTE:** You already have the 'OE/RR NOTIFICATIONS' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// Virtual Terminal

# Test System Post-Installation Tasks (Installation Verification Procedure)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Post-installation instructions are listed in the “CPRS v31b Follow-Up Build Setup and Configuration Guide”. Post-Installation tasks must be performed by the CAC.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Disable Protocol PSO LM PAT PREG/LACT DISPLAY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*622 is releasing with a known defect. Patch PSO\*7\*441, which is part of the CPRS v32b release, will correct that defect.

To lessen the defect’s impact on end users, disable the new protocol PSO LM PAT PREG/LACT DISPLAY using these instructions:

1.  From the VA FileMan \[DIUSER\] menu, execute the “Enter or Edit File Entries \[DIEDIT\]” option.
2.  When prompted with “Input to what File”, enter “PROTOCOL”.
3.  When prompted with “EDIT WHICH FIELD: ALL//”, enter “2”.
4.  When prompted with “THEN EDIT FIELD”, press the ENTER key.
5.  When prompted with “Select PROTOCOL NAME”, enter “PSO LM PAT PREG/LACT DISPLAY”.
6.  When prompted with “DISABLE”, enter “Action disabled. PSO\*7\*441 will enable” without the quotes.
7.  When prompted with “PROTOCOL NAME”, press the ENTER key.

> Example – Disabling the PSO LM PAT PREG/LACT DISPLAY Protocol

Select VA FileMan Option: Enter or Edit File Entries

Input to what File: WV PATIENT// PROTOCOL (6356 entries)

EDIT WHICH FIELD: ALL// 2 DISABLE

THEN EDIT FIELD:

Select PROTOCOL NAME: PSO LM PAT PREG/LACT DISPLAY Preg/Lact Display

DISABLE: Action disabled. PSO\*7\*441 will enable.

Select PROTOCOL NAME:

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Testing in the Test Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At this point, sites have the chance to test and familiarize themselves with the CPRS v31b Follow-Up Build in their test accounts before proceeding to install in their production accounts.

# Production System Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Production System Installation Checklist is the same as the Test System Installation Checklist. See *Section 4* for more details.

# Production System Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Production Pre-Installation Steps are the same as the Test System Pre-Installation Steps. See *Section 6* for more details.

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Back Up Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Production System Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Production installation steps are the same as the Test System installation steps. See *Section 7* for more details.

# Production System Post-Installation Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Production post-installation steps are the same as the Test System post-installation steps. See *Section 8* for more details.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a major issue occurs with the patch, the Facility Chief Information Officer (FCIO) may decide to do a back-out. However, this decision should include input from both the Health Product Support and the CPRS development team

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back out the changes associated with the CPRS v31b Follow-Up Build, personnel would install patch ZZ_OR_3_498_BACKOUT.KID, which will back out all the patches installed with OR\*3.0\*498.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out should be considered only if the patch causes a catastrophic system failure and all other options have been exhausted. If a back-out is being considered, an email should be sent to the CPRS implementation team at REDACTED.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out the CPRS v31b Follow-Up Build would affect many different parts of CPRS. For more information about these changes, please reference the *CPRS v31b Follow-Up Build Release Notes*, which can be obtained from the [VA Software Document Library](https://www.va.gov/vdl/).  
  
However, back-out risks are minimal since patch ZZ_OR_3_498_BACKOUT.KID should return CPRS to the state it was in prior to installing OR\*3.0\*498.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FCIO has the final authority to back out the CPRS v31b Follow-Up Build and revert to a previous build. The FCIO should consult with the CPRS Development team and Health Product Support Clinical personnel before deciding to back out the patches.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back out the features with the CPRS v31b Follow-Up Build, a back out patch was created to return the system to a previous state.  
  
To back out the CPRS v31b Follow-Up Build, follow these steps:

1.  Install the ZZ_OR_3_498_BACKOUT.KID patch.
2.  At the Reminder Exchange, reinstall the SMART BACKUP. See Section 6.6 - Backup Procedures for more details.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By utilizing the back-out patch and restoring the globals, the system will revert to what it was prior to installing the CPRS v31b Follow-Up Build.

To verify that the patch has been backed out properly:

1.  Verify that the second line of routine ORBSMART looks like this, with 377 as the last patch:  
    ;;3.0;ORDER ENTRY/RESULTS REPORTING;\*\*377\*\*;Dec 17, 1997;Build 519

> **NOTE:** Before the back-out, the second line of ORBSMART will look like this, with 498 in the patch list:  
;;3.0;ORDER ENTRY/RESULTS REPORTING;\*\*377,498\*\*;Dec 17, 1997;Build 519

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback is required for this installation.

# Appendix A: Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a capture of a CPRS V31B FOLLOW-UP PATCHES 1.0 installation that provides details of the install.

Example: First-time Install

Install Started for CPRS V31B FOLLOW-UP PATCHES 1.0 :

Sep 30, 2021@09:12:15

Build Distribution Date: Sep 29, 2021

Installing Routines:

Sep 30, 2021@09:12:15

Install Started for WV\*1.0\*26 :

Sep 30, 2021@09:12:15

Build Distribution Date: Sep 29, 2021

Installing Routines:

Sep 30, 2021@09:12:15

Running Pre-Install Routine: PRE^WV1026P

Removing the data dictionary for the

WV PREGNANCY/LACTATION STATUS CONFLICT EVENTS file (#790.9)...

DONE

Installing Data Dictionaries:

Sep 30, 2021@09:12:15

Installing Data:

Sep 30, 2021@09:12:15

Installing PACKAGE COMPONENTS:

Installing FORM

Installing REMOTE PROCEDURE

Installing PARAMETER DEFINITION

Sep 30, 2021@09:12:15

Running Post-Install Routine: POST^WV1026P

Update Women's Health Patient record that need Next Breast Treatment Date

Find Procedure to review

Find Patients to review

Review Patients record

Rebuilding the APREG index...

DONE

Clearing the CPRS Cover Sheet data cache...

DONE

Updating Routine file...

Updating KIDS files...

WV\*1.0\*26 Installed.

Sep 30, 2021@09:12:16

Not a production UCI

NO Install Message sent

Install Started for PXRM\*2.0\*71 :

Sep 30, 2021@09:12:16

Build Distribution Date: Sep 29, 2021

Installing Routines:

Sep 30, 2021@09:12:16

Running Pre-Install Routine: PRE^PXRMP71I

DISABLE options.

DISABLE protocols.

Repointing Reminder Term: VA-WH BR CA 40-44 WANTS SCREEN TERM

WV PROCEDURE TYPE entries whose 'REMINDER TERM' pointers have been changed

SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

REMINDER ORDER CHECK RULES entries whose 'REMINDER TERM' pointers have been chan

ged SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

REMINDER DIALOG entries whose 'EVALUATION ITEM' pointers have been changed

SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

REMINDER EXTRACT SUMMARY entries whose 'TERM' pointers have been changed

SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

REMINDER EXTRACT SUMMARY entries whose 'FINDING ITEM' pointers have been changed

SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

REMINDER EXTRACT SUMMARY entries whose 'FINDING ITEM' pointers have been changed

SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

REMINDER EXTRACT SUMMARY entries whose 'REMINDER TERM' pointers have been change

d SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

REMINDER LIST RULE entries whose 'REMINDER TERM' pointers have been changed

SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

VA-SMART FR 40-44 WANTS SCREENING FINDING RULE

REMINDER COUNTING GROUP entries whose 'TERM' pointers have been changed

SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

REMINDER DEFINITION entries whose 'FINDING ITEM' pointers have been changed

SEP 30, 2021@09:12 PAGE 1

--------------------------------------------------------------------------------

\*\*\* NO RECORDS TO PRINT \*\*\*

--------------------------------------------------------------------------------

Installing Data Dictionaries:

Sep 30, 2021@09:12:22

Installing Data:

Sep 30, 2021@09:12:25

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Sep 30, 2021@09:12:25

Running Post-Install Routine: POST^PXRMP71I

Removing medications from the VA-WH HIRISK MEDICATIONS (EXTREME RISK) GROUP

reminder order check items group:

ABACAVIR/DOLUTEGRAVIR/LAMIVUDINE

DOLUTEGRAVIR

DOLUTEGRAVIR/RILPIVIRINE

DONE

Removing all items from the VA-WH HIRISK MEDICATIONS (LACTATION LEVEL 2) GROUP

reminder order check items group:

DONE

Deleting the VA-WH TD CLEAR LACTATION ALERT

reminder dialog...

DONE

Deleting the VA-WH TD CLEAR PREGNANCY ALERT

reminder dialog...

DONE

ENABLE options.

ENABLE protocols.

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*71 Installed.

Sep 30, 2021@09:12:29

Not a production UCI

NO Install Message sent

Install Started for PSO\*7.0\*622 :

Sep 30, 2021@09:12:29

Build Distribution Date: Sep 29, 2021

Installing Routines:

Sep 30, 2021@09:12:29

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Located in the PSO (OUTPATIENT PHARMACY) namespace.

Sep 30, 2021@09:12:29

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*622 Installed.

Sep 30, 2021@09:12:29

Not a production UCI

NO Install Message sent

Install Started for TIU\*1.0\*341 :

Sep 30, 2021@09:12:29

Build Distribution Date: Sep 29, 2021

Installing Routines:

Sep 30, 2021@09:12:29

Running Post-Install Routine: POST^TIU341P

PULSE OXIMETRY object created successfully.

VA-WH EXPECTED DUE DATE object created successfully.

Updating Routine file...

Updating KIDS files...

TIU\*1.0\*341 Installed.

Sep 30, 2021@09:12:29

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*498 :

Sep 30, 2021@09:12:29

Build Distribution Date: Sep 29, 2021

Installing Routines:

Sep 30, 2021@09:12:29

Running Pre-Install Routine: PRE^OR498P

Installing Data Dictionaries:

Sep 30, 2021@09:12:30

Installing Data:

Sep 30, 2021@09:12:30

Installing PACKAGE COMPONENTS:

Installing OPTION

Installing PARAMETER DEFINITION

Sep 30, 2021@09:12:30

Running Post-Install Routine: POST^OR498P

Updating Cover Sheet Immunizations Report

Updating ORB URGENCY to Low at PKG level for notification SMART NON-CRITICAL IMA

GING RES

Updating Routine file...

Updating KIDS files...

OR\*3.0\*498 Installed.

Sep 30, 2021@09:12:30

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

CPRS V31B FOLLOW-UP PATCHES 1.0 Installed.

Sep 30, 2021@09:12:30

No link to PACKAGE file

NO Install Message sent

Install Completed

# Appendix B: Post-Install Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Checksums:

\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: WV\*1.0\*26

1 WV\*1.0\*26 WOMEN'S HEALTH WOMEN'S HEALTH

2 WV\*1.0\*26b WOMEN'S HEALTH WOMEN'S HEALTH

CHOOSE 1-2: 1 WV\*1.0\*26 WOMEN'S HEALTH WOMEN'S HEALTH

WV1026P value = 23324867

WVALERTR value = 40984224

WVEXPTRA value = 47275855

WVPKG value = 1398902

WVRALINK value = 89480987

WVRPCGF value = 205155906

WVRPCGF1 value = 117914359

WVRPCGF2 value = 10066909

WVRPCOR value = 91830412

WVRPCOR1 value = 16869001

WVRPCOR2 value = 34827657

WVRPCPR value = 29143724

WVRPCPT value = 158633774

WVRPCPT1 value = 172660673

WVRPCPT2 value = 46072493

WVRPCVPR value = 12966415

WVTDALRT value = 40521827

WVTIU value = 54549941

WVUTL1 value = 46884913

WVUTL11 value = 167515768

WVUTL12 value = 10807548

WVUTL4 value = 12633419

done

\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: PXRM\*2.0\*71

1 PXRM\*2.0\*71 CLINICAL REMINDERS CLINICAL REMINDERS

2 PXRM\*2.0\*71b CLINICAL REMINDERS CLINICAL REMINDERS

CHOOSE 1-2: 1 PXRM\*2.0\*71 CLINICAL REMINDERS CLINICAL REMINDERS

PXRMCALT value = 108062944

PXRMCOPY value = 44260657

PXRMCWH value = 205206809

PXRMCWH1 value = 76553371

PXRMDGFC value = 15804854

PXRMDLED value = 10261556

PXRMDLG4 value = 100687855

PXRMDUTL value = 57754306

PXRMEXU4 value = 135631400

PXRMGEV value = 45380121

PXRMGEVA value = 69344885

PXRMNTFY value = 112290772

PXRMORCH value = 105863585

PXRMP71I value = 77309826

PXRMPLAB value = 30988297

PXRMPRAD value = 42218466

PXRMRPCG value = 132169684

PXRMRUL1 value = 51780833

done

\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: PSO\*7.0\*622

1 PSO\*7.0\*622 OUTPATIENT PHARMACY OUTPATIENT PHARMACY

2 PSO\*7.0\*622b OUTPATIENT PHARMACY OUTPATIENT PHARMACY

CHOOSE 1-2: 1 PSO\*7.0\*622 OUTPATIENT PHARMACY OUTPATIENT PHARMACY

PSODEM value = 23547289

PSOLMPAT value = 6680611

PSOLMUTL value = 14845000

PSOORRL value = 73574968

PSOORRL3 value = 28030432

PSOORRLN value = 48136074

PSOORRLO value = 43646487

PSOORUT2 value = 108723602

PSORXEDT value = 57610892

PSORXVW value = 81376919

done

\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: TIU\*1.0\*341

1 TIU\*1.0\*341 TEXT INTEGRATION UTILITIES TEXT INTEGRATION UTILI

TIES

2 TIU\*1.0\*341b TEXT INTEGRATION UTILITIES TEXT INTEGRATION UTIL

ITIES

CHOOSE 1-2: 1 TIU\*1.0\*341 TEXT INTEGRATION UTILITIES TEXT INTEGRATION U

TILITIES

GMRPNCW value = 32632231

TIU341P value = 4546555

TIUCROBJ value = 8682625

TIULO value = 52832476

TIUUTL value = 25893344

done

\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: OR\*3.0\*498

1 OR\*3.0\*498 ORDER ENTRY/RESULTS REPORTING ORDER ENTRY/RESULTS

REPORTING

2 OR\*3.0\*498b ORDER ENTRY/RESULTS REPORTING ORDER ENTRY/RESULTS

REPORTING

CHOOSE 1-2: 1 OR\*3.0\*498 ORDER ENTRY/RESULTS REPORTING ORDER ENTRY/RESU

LTS REPORTING

OR498P value = 8766942

ORB3U1 value = 72818433

ORB3U2 value = 91861349

ORB3USER value = 74828188

ORBSMART value = 41887919

ORCACT01 value = 114181826

ORDEBUG value = 16554061

ORDV02A value = 13647857

ORDV06B value = 44630064

ORLPREM value = 32531974

ORPDMPNT value = 35626953

ORPDMPWS value = 184364456

ORS100C value = 41802538

ORSMART value = 3089952

ORWDRA32 value = 27726747

ORWDXM1 value = 127137244

ORWDXM3 value = 132401126

ORWORB value = 99052906

ORWPCE3 value = 65944434

ORWPS value = 87678827

ORWRP value = 82715505

ORY498 value = 195772

done

# Appendix C: Install File Print Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

Select Utilities \<TEST ACCOUNT\> Option: Install File Print

Select INSTALL NAME: CPRS V31B FOLLOW-UP PATCHES 1.0 Install Completed

9/30/21@09:12:30

=\> CPRS V31B FOLLOW-UP PATCHES 1.0 v16, WV\*1.0\*26 v16, PXRM\*2.0\*71 v16, P

DEVICE: HOME// ;;999 Virtual Terminal

PACKAGE: CPRS V31B FOLLOW-UP PATCHES 1.0 Sep 30, 2021 9:20 am PAGE 1

COMPLETED ELAPSED

-------------------------------------------------------------------------------

STATUS: Install Completed DATE LOADED: SEP 30, 2021@08:37:05

INSTALLED BY: PROGRAMMER,ONE

NATIONAL PACKAGE:

INSTALL STARTED: SEP 30, 2021@09:12:15 09:12:30 0:00:15

ROUTINES: 09:12:15

INSTALL QUESTION PROMPT ANSWER

XPI1 Want KIDS to INHIBIT LOGONs during the install NO

XPZ1 Want to DISABLE Scheduled Options, Menu Options, and Protocols NO

MESSAGES:

Install Started for CPRS V31B FOLLOW-UP PATCHES 1.0 :

Sep 30, 2021@09:12:15

Build Distribution Date: Sep 29, 2021

Installing Routines:

Sep 30, 2021@09:12:15

Updating Routine file...

Updating KIDS files...

CPRS V31B FOLLOW-UP PATCHES 1.0 Installed.

Sep 30, 2021@09:12:30

No link to PACKAGE file

NO Install Message sent

# Appendix D: Build File Print Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the KIDS Build File Print option to print out the build components. You can select the multi-package build or any of the individual builds included in the multi-package build.

Select Utilities \<TEST ACCOUNT\> Option: Build File Print

Select BUILD NAME: CPRS V31B FOLLOW-UP PATCHES 1.0

1 CPRS V31B FOLLOW-UP PATCHES 1.0

2 CPRS V31B FOLLOW-UP PATCHES 1.0b

CHOOSE 1-2: 1 CPRS V31B FOLLOW-UP PATCHES 1.0 (Multi-Package)

WV\*1.0\*26

PXRM\*2.0\*71

PSO\*7.0\*622

TIU\*1.0\*341

OR\*3.0\*498

DEVICE: HOME// ;;999 Virtual Terminal

PACKAGE: CPRS V31B FOLLOW-UP PATCHES 1.0 Sep 30, 2021 9:21 am PAGE 1

-------------------------------------------------------------------------------

TYPE: MULTI-PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Sep 29, 2021

DESCRIPTION:

SEQUENCE OF BUILDS:

1 WV\*1.0\*26 Required to Continue

2 PXRM\*2.0\*71 Required to Continue

3 PSO\*7.0\*622 Required to Continue

4 TIU\*1.0\*341 Required to Continue

5 OR\*3.0\*498 Not Required to Continue

PACKAGE: WV\*1.0\*26 Sep 30, 2021 9:22 am PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: WOMEN'S HEALTH ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Sep 29, 2021

DESCRIPTION:

This patch modifies the Women's Health package to improve monitoring of

high risk medcations prescribed or administered to women of childbearing

age or women who are lactating. Specifically, the software now tracks a

woman's pregnancy and lacation status and notifies providers of changes in

these statuses. These statuses are used during order checking to remind

providers about the potential harm of such medications.

Please see the accompanying patch description for details and the

Computerized Patient Record System (CPRS) version 31.b installation manual

for installation instructions.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: PRE^WV1026P DELETE PRE-INIT ROUTINE: No

POST-INIT ROUTINE: POST^WV1026P DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

790.1 WV PROCEDURE YES NO NO NO

Partial DD: subDD: 790.1 fld: .14

subDD: 790.23 fld: 5

subDD: 790.24 fld: .01

fld: 1

790.4 WV NOTIFICATION YES NO NO NO

Partial DD: subDD: 790.4 fld: .08

fld: .14

790.403 WV NOTIFICATION TYPE NO NO YES OVER NO NO

DATA SCREEN: I Y=16!(Y=17)

790.404 WV NOTIFICATION PURPOSE NO NO YES OVER NO NO

DATA SCREEN: I \$\$SENDPUR^WV1026P(\$P(^(0),U))

790.9 WV PREGNANCY/LACTATION STATUS CONFLICT EVENTSYESNONO NO

FORM: ACTION:

WV PROC-FORM-1 FILE \#790.1 SEND TO SITE

WV PROC-FORM-2-COLP FILE \#790.1 SEND TO SITE

ROUTINE: ACTION:

WV1026P SEND TO SITE

WVALERTR SEND TO SITE

WVEXPTRA SEND TO SITE

WVPKG SEND TO SITE

WVRALINK SEND TO SITE

WVRPCGF SEND TO SITE

WVRPCGF1 SEND TO SITE

WVRPCGF2 SEND TO SITE

WVRPCOR SEND TO SITE

WVRPCOR1 SEND TO SITE

WVRPCOR2 SEND TO SITE

WVRPCPR SEND TO SITE

WVRPCPT SEND TO SITE

WVRPCPT1 SEND TO SITE

WVRPCPT2 SEND TO SITE

WVRPCVPR SEND TO SITE

WVTDALRT SEND TO SITE

WVTIU SEND TO SITE

WVUTL1 SEND TO SITE

WVUTL11 SEND TO SITE

WVUTL12 SEND TO SITE

WVUTL4 SEND TO SITE

PARAMETER DEFINITION: ACTION:

WV BREAST IMAGE TERM LINKING SEND TO SITE

WV MAIL GROUP ISSUE SEND TO SITE

REMOTE PROCEDURE: ACTION:

WVRPCOR COVER SEND TO SITE

REQUIRED BUILDS: ACTION:

WV\*1.0\*24 Don't install, leave global

PACKAGE: PXRM\*2.0\*71 Sep 30, 2021 9:22 am PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: CLINICAL REMINDERS ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Sep 29, 2021

DESCRIPTION:

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: PRE^PXRMP71I DELETE PRE-INIT ROUTINE: No

POST-INIT ROUTINE: POST^PXRMP71I DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

801.41 REMINDER DIALOG YES YES NO NO

Partial DD: subDD: 801.41143 fld: 1

811.4 REMINDER COMPUTED FINDINGS NO NO YES OVER NO NO

DATA SCREEN: I \$\$INCCF^PXRMP71I(\$P(\$G(^PXRMD(811.4,Y,0)),U,1))

811.8 REMINDER EXCHANGE NO NO YES OVER NO NO

DATA SCREEN: I \$\$EXFINC^PXRMEXSI(Y,"EXARRAY","PXRMP71I")

INPUT TEMPLATE: ACTION:

PXRM EDIT GROUP FILE \#801.41 SEND TO SITE

PXRM EDIT NATIONAL DIALOG FILE \#801.41 SEND TO SITE

ROUTINE: ACTION:

PXRMCALT SEND TO SITE

PXRMCOPY SEND TO SITE

PXRMCWH SEND TO SITE

PXRMCWH1 SEND TO SITE

PXRMDGFC SEND TO SITE

PXRMDLED SEND TO SITE

PXRMDLG4 SEND TO SITE

PXRMDUTL SEND TO SITE

PXRMEXU4 SEND TO SITE

PXRMGEV SEND TO SITE

PXRMGEVA SEND TO SITE

PXRMNTFY SEND TO SITE

PXRMORCH SEND TO SITE

PXRMP71I SEND TO SITE

PXRMPLAB SEND TO SITE

PXRMPRAD SEND TO SITE

PXRMRPCG SEND TO SITE

PXRMRUL1 SEND TO SITE

REQUIRED BUILDS: ACTION:

PXRM\*2.0\*75 Don't install, leave global

PXRM\*2.0\*42 Don't install, leave global

PACKAGE: PSO\*7.0\*622 Sep 30, 2021 9:22 am PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: OUTPATIENT PHARMACY ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Sep 29, 2021

DESCRIPTION:

See the Forum patch description.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE: DELETE POST-INIT ROUTINE:

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

ROUTINE: ACTION:

PSODEM SEND TO SITE

PSOLMPAT SEND TO SITE

PSOLMUTL SEND TO SITE

PSOORRL SEND TO SITE

PSOORRL3 SEND TO SITE

PSOORRLN SEND TO SITE

PSOORRLO SEND TO SITE

PSOORUT2 SEND TO SITE

PSORXEDT SEND TO SITE

PSORXVW SEND TO SITE

PROTOCOL: ACTION:

PSO HIDDEN ACTIONS USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PSO HIDDEN ACTIONS \#1 USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PSO HIDDEN ACTIONS \#2 USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PSO HIDDEN ACTIONS \#3 USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PSO LM PAT PREG/LACT DISPLAY SEND TO SITE

PSO PMP HIDDEN ACTIONS MENU \#2 USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

REQUIRED BUILDS: ACTION:

PSO\*7.0\*381 Don't install, leave global

PSO\*7.0\*564 Don't install, leave global

PSO\*7.0\*468 Don't install, leave global

PSO\*7.0\*504 Don't install, leave global

PSO\*7.0\*556 Don't install, leave global

PACKAGE: TIU\*1.0\*341 Sep 30, 2021 9:22 am PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: TEXT INTEGRATION UTILITIES ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Sep 29, 2021

DESCRIPTION:

This patch addresses issues identified during the CPRS v31b deployment.

Refer to the patch description for a comlete list of issues that are

addressed.

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE: POST^TIU341P DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

ROUTINE: ACTION:

GMRPNCW SEND TO SITE

TIU341P SEND TO SITE

TIUCROBJ SEND TO SITE

TIULO SEND TO SITE

TIUUTL SEND TO SITE

REQUIRED BUILDS: ACTION:

TIU\*1.0\*290 Don't install, leave global

TIU\*1.0\*204 Don't install, leave global

TIU\*1.0\*120 Don't install, leave global

Type \<Enter\> to continue or '^' to exit:

PACKAGE: OR\*3.0\*498 Sep 30, 2021 9:22 am PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: ORDER ENTRY/RESULTS REPORTING ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: Sep 29, 2021

DESCRIPTION:

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: PRE^OR498P DELETE PRE-INIT ROUTINE: No

POST-INIT ROUTINE: POST^OR498P DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

100.9 OE/RR NOTIFICATIONS YES NO YES OVER YES NO

DATA SCREEN: I \$\$SENDNOT^ORY498(\$P(^(0),U))

ROUTINE: ACTION:

ORB3U1 SEND TO SITE

ORB3U2 SEND TO SITE

ORB3USER SEND TO SITE

ORBSMART SEND TO SITE

ORCACT01 SEND TO SITE

ORDEBUG SEND TO SITE

ORDV02A SEND TO SITE

ORDV06B SEND TO SITE

ORLPREM SEND TO SITE

ORPDMPNT SEND TO SITE

ORPDMPWS SEND TO SITE

ORS100C SEND TO SITE

ORSMART SEND TO SITE

ORWDRA32 SEND TO SITE

ORWDXM1 SEND TO SITE

ORWDXM3 SEND TO SITE

ORWORB SEND TO SITE

ORWPCE3 SEND TO SITE

ORWPS SEND TO SITE

ORWRP SEND TO SITE

ORY498 SEND TO SITE

OPTION: ACTION:

OR CS ORDER ANOMALIES SEND TO SITE

OR PARAM COORDINATOR MENU USE AS LINK FOR MENU/ITEM/SUBS

CRIBERS

PARAMETER DEFINITION: ACTION:

OR CPRS DEBUG EMAIL SEND TO SITE

ORQQTIU COPY/PASTE IDENT SEND TO SITE

REQUIRED BUILDS: ACTION:

OR\*3.0\*413 Don't install, leave global

OR\*3.0\*512 Don't install, leave global

OR\*3.0\*519 Don't install, leave global

PSS\*1.0\*238 Don't install, leave global