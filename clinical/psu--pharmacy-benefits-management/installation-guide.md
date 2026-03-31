---
title: Benefits Management Version 4 Install Guide_Extract Enhancements Phases I thru II
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Install Guide_Extract Enhancements Phases I thru II
app_code: PSU
app_name: "Pharmacy: Benefits Management"
section: CLI
app_status: active
pkg_ns: PSU
patch_ver: 4
patch_id: PSU*4
group_key: "PSU:PSU:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - install
  - contents
  - installation
  - class
  - strong
  - routines
  - protocols
  - pharmacy
  - software
page_count: 0
word_count: 2462
section_count: 11
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=91"
---

> ![](benefits-management-version-4-install-guide-extract-enhancements-phases-i-thru-i/001.png)

PHARMACY BENEFITS MANAGEMENT (PBM)EXTRACT ENHANCEMENTS

####### INSTALLATION GUIDE 

June 2005

VistA Health Systems Design & Development  

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [Dependencies and Constraints](#dependencies-and-constraints)
- [Pre-Installation](#pre-installation)
  - [Minimum Required Packages](#minimum-required-packages)
  - [Required Setup](#required-setup)
- [Installation Instructions](#installation-instructions)
- [Post-Installation](#post-installation)
  - [Required Tasks](#required-tasks)
  - [After Checksums](#after-checksums)
    - [PSO\7\165 Routines](#pso7165-routines)
    - [PSU 4.0 Routines](#psu-40-routines)
- [Appendix: Reinstallation Requirements](#appendix-reinstallation-requirements)
  - [Add Child Protocols to Parent Protocols](#add-child-protocols-to-parent-protocols)
  - [Delete ^PSULRHL1 and ^PSULRHLI](#delete-psulrhl1-and-psulrhli)
  - [Install PSU 4.0 Software](#install-psu-40-software)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To meet the reporting requirements placed on the Pharmacy Benefits Management (PBM) Strategic Healthcare Group (SHG) by external bodies such as the General Accounting Office (GAO), the Institute of Medicine (IOM), as well as congressional oversight bodies, PBMSHG requested enhancements to the Veterans Health Information Systems and Technology Architecture (VistA) PBM V. 4.0 application. PBM V. 4.0 extracts medication dispensing data, procurement data, and clinical data from multiple files in VistA and electronically exports the data via MailMan to the PBM national database.

The data set captured by the PBM V. 4.0 application will be expanded and enhanced to support the Veterans Affairs National Formulary (VANF) disease management issues and patient safety initiatives. The intended audiences for this document are PBM SHG, PBM Extract Enhancement workgroup, Provider Systems Health Systems Design and Development (HSD&D) staff, National VistA support staff, technical writers, and Software Quality Assurance (SQA) staff.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PBM V. 4.0 is a new enhanced version of the software and replaces PBM V. 3.0. In a series of three enhancements, new extracts and reports were created, existing extracts were modified, and some options were modified to increase the functionality of this software package. For more detail, refer to the *Pharmacy Benefits Management V. 4.0 Release Notes* document.

## Dependencies and Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** PSO\*7\*165 is a required patch for PSU 4.0, and both have been bundled together in a master build. Implementation of enhancements is dependant on installing the patches listed in the Pre-Installation section.

The recent enhancements allow users to map pharmacy-defined locations from the Automatic Replenishment/Ward Stock (AR/WS) Stats, Controlled Substances (CS), and Drug Accountability applications to a specific Medical Center Division or Outpatient Pharmacy Site.

*(This page included for two-sided copying.)*

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists packages that are required and setup activities that must be performed prior to installing the new PBM software.

![](benefits-management-version-4-install-guide-extract-enhancements-phases-i-thru-i/002.png)

PSU 4.0 and PSO\*7\*165 should not be installed while the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option or a *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option is running. Installation may cause the tasked job to error out and not complete.

## Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product shall run on standard hardware platforms used by the Department of Veterans Affairs Healthcare facilities. These systems consist of standard or upgraded Alpha AXP clusters and run VMS DSM, Cache NT, or Cache VMS.

|                                                              |                            |
|--------------------------------------------------------------|----------------------------|
| Package                                                  | Minimum Version Needed |
| Adverse Reaction Tracking (ART)                              | 4.0                        |
| Auto Replenishment/Ward Stock (AR/WS)                        | 2.3                        |
| Controlled Substances                                        | 3.0                        |
| Drug Accountability                                          | 3.0                        |
| Inpatient Medications                                        | 5.0                        |
| Integrated Funds Control, Accounting and Procurement (IFCAP) | 5.1                        |
| Kernel                                                       | 8.0                        |
| Laboratory                                                   | 5.2                        |
| MailMan                                                      | 8.0                        |
| National Drug File (NDF)                                     | 4.0                        |
| Outpatient Pharmacy                                          | 7.0                        |
| Patient Care Encounter (PCE)                                 | 1.0                        |
| Patient Information Management System (PIMS)                 | 5.3                        |
| Pharmacy Data Management (PDM)                               | 1.0                        |
| VA FileMan                                                   | 22.0                       |
| Visit Tracking                                               | 2.0                        |

The above software is not included in this build and must be installed before this build is completely functional.

## Required Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installing PSU 4.0 and PSO\*7\*165, sites must perform the activities listed below.

- Install patch DG\*5.3\*575.
- Confirm that the Automatic Pharmacy Statistics \[PSU PBM AUTO\] option has run for the previous month and that all the MailMan messages generated have successfully transmitted to the PBM national database at Hines.
- Set up parameters for the new global ^PSUDEM using the steps outlined below. Default values can be used. Only sites running DSM need to set the global protection.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>Set Journaling:</p>
<ul>
<li><p>Verify that Journaling is enabled, or</p></li>
<li><p>Change the setting to “Enabled”.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>2</td>
<td><p>Set Access Privileges:</p>
<ul>
<li><p>Verify that the access privileges are set as listed below, or</p></li>
<li><p>Set the following access privileges:</p>
<ul>
<li><blockquote>
<p>System = RWP</p>
</blockquote></li>
<li><blockquote>
<p>World = RW</p>
</blockquote></li>
<li><blockquote>
<p>Group = RW</p>
</blockquote></li>
<li><blockquote>
<p>UCI = RWP</p>
</blockquote></li>
</ul></li>
</ul></td>
</tr>
</tbody>
</table>

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains detailed steps to install PSU 4.0 and PSO\*7\*165.

![](benefits-management-version-4-install-guide-extract-enhancements-phases-i-thru-i/003.png)

If PBM V. 4.0 has been previously installed in your test or live account, please proceed to the Appendix in this document (section 5, page 13), and follow the instructions to reinstall PBM V. 4.0.

![](benefits-management-version-4-install-guide-extract-enhancements-phases-i-thru-i/004.png) Note: Only follow these instructions in accounts where PBM V. 4.0 was previously installed. The requirements described in the Appendix must be fulfilled in order to complete the installation of PBM V. 4.0 in those areas.

![](benefits-management-version-4-install-guide-extract-enhancements-phases-i-thru-i/005.png)Note: Installation MUST be queued during off hours (for example, at night).

The table below contains the steps necessary to install the software.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>Data for this patch is being distributed in a kids host file:</p>
<p>Filename FTP Protocol</p>
<p>------------ ---------------</p>
<p>PSU_4_0.KID ASCII</p>
<p>The preferred method is to FTP this file from <mark>REDACTED</mark>, which will transmit the file from the first available FTP server.</p>
<p>This file may also be downloaded directly from a particular FTP location at the following locations:</p>
<p><mark>REDACTED</mark></p>
<p>The file is available in the ANONYMOUS.SOFTWARE directory.</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time. Currently there are no routines that are recommended by the package to be placed into the mapped set.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>From the <em>Kernel Installation &amp; Distribution System</em> menu, select the <em>Installation</em> menu.</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>From this menu, select the Load a Distribution option and select</p>
<p>PSU_4_0.KID.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>5</th>
<th><p>From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter PSU 4.0):</p>
<ol type="a">
<li><p><em>Backup a Transport Global</em> - This option will create a backup message of any routines exported with the build. It will not back up any other changes, such as DDs or templates.</p></li>
<li><p><em>Compare Transport Global to Current System</em> - This option will allow you to view all changes that will be made when the build is installed. It compares all components of the release (routines, DDs, templates, etc.).</p></li>
<li><p><em>Verify Checksums in Transport Global</em> - This option will ensure the integrity of the routines that are in the transport global.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>6</td>
<td>Use the <em>Install Package(s)</em> option and select the package PSU 4.0.</td>
</tr>
<tr class="even">
<td>7</td>
<td>Install Questions for PSU 4.0:</td>
</tr>
<tr class="odd">
<td>8</td>
<td>When prompted, “Enter the Coordinator for Mail Group 'PSU PBM':”, please respond with <strong>the name of your site’s PSU PBM Mail Group Coordinator</strong>.</td>
</tr>
<tr class="even">
<td>9</td>
<td>When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//", respond <strong>NO</strong>.</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Install Questions for PSO*7.0*165:</td>
</tr>
<tr class="even">
<td>11</td>
<td>When prompted "Want KIDS to INHIBIT LOGONs during the install? YES//", respond <strong>NO</strong>.</td>
</tr>
<tr class="odd">
<td>12</td>
<td>When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//", respond <strong>NO</strong>.</td>
</tr>
<tr class="even">
<td>13</td>
<td>If any routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has run to completion.</td>
</tr>
</tbody>
</table>

Example: Screen Display During Installation of PSU 4.0 and PSO\*7\*165

Select Installation Option: LOad a Distribution

Enter a Host File: PSU_4_0.KID

KIDS Distribution saved on Jun 22, 2005@14:17:32

Comment: PSU 4.0 - 06/22/2005

This Distribution contains Transport Globals for the following Package(s):

PSU 4.0

PSO\*7.0\*165

Distribution OK!

Want to Continue with Load? YES// \<Enter\>

Loading Distribution...

PSU 4.0

PSO\*7.0\*165

Use INSTALL NAME: PSU 4.0 to install this Distribution.

Select Installation Option: INstall Package(s)

Select INSTALL NAME: PSU 4.0 Loaded from Distribution 6/23/05@07:43:38

=\> PSU 4.0 - 06/22/2005 ;Created on Jun 22, 2005@14:17:32

This Distribution was loaded on Jun 23, 2005@07:43:38 with header of

PSU 4.0 - 06/22/2005 ;Created on Jun 22, 2005@14:17:32

It consisted of the following Install(s):

PSU 4.0 PSO\*7.0\*165

Checking Install for Package PSU 4.0

Install Questions for PSU 4.0

Incoming Files:

59.7 PHARMACY SYSTEM (Partial Definition)

> **NOTE:** You already have the 'PHARMACY SYSTEM' File.

59.9 PBM PATIENT DEMOGRAPHICS

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'PSU PBM': \<Enter Coordinator here.\>

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Checking Install for Package PSO\*7.0\*165

Install Questions for PSO\*7.0\*165

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter device here.\>

\- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - continued - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
Example: Screen Display During Installation of PSU 4.0 and PSO\*7\*165 (continued)

Install Started for PSU 4.0 :

Jun 23, 2005@08:28:39

Build Distribution Date: Jun 22, 2005

Installing Routines:

Jun 23, 2005@08:28:44

Installing Data Dictionaries: .

Jun 23, 2005@08:28:46

Installing PACKAGE COMPONENTS:

Installing MAIL GROUP

Installing PROTOCOL

Installing OPTION

Jun 23, 2005@08:28:47

Updating Routine file...

Updating KIDS files...

PSU 4.0 Installed.

Jun 23, 2005@08:28:50

Install Message sent \# 32156897

PSO\*7.0\*165

────────────────────────────────────────────────────────────────────────────────

Install Started for PSO\*7.0\*165 :

Jun 23, 2005@08:28:50

Build Distribution Date: Jun 22, 2005

Installing Routines:

Jun 23, 2005@08:28:50

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*165 Installed.

Jun 23, 2005@08:28:50

Install Message sent \# 32156898

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the tasks that have to be performed after the new PBM software is installed.

## Required Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing PSU 4.0 and PSO\*7\*165, sites must ensure that the following tasks are performed:

- If you did not name a coordinator for the Mail Group ‘PSU PBM’, use VA FileMan to enter the coordinator’s name.
- Pharmacy locations can be mapped using the new *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option in order to receive a breakdown of data from those mapped sites for the AR/WS, CS, and Procurement extracts. If the locations are not mapped, the data on those extracts will be included in data from the parent facility.
- Confirm that the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option is scheduled correctly for the next month’s transmission.

> <span class="mark">REDACTED</span>

> Example Email Message to Hines PBM Group

> <span class="mark">REDACTED</span>

## After Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the routines and related checksums for PSO\*7\*165 and PSU 4.0 after the installation process.

### PSO\*7\*165 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSOORDER value = 38147160

### PSU 4.0 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSUAA1 value = 5004740

> PSUAA2 value = 2048002

> PSUALERT value = 2451350

> PSUAMC value = 1435929

> PSUAR0 value = 2539270

> PSUAR1 value = 6597726

> PSUAR2 value = 4029683

> PSUAR3 value = 3301995

> PSUAR4 value = 4559435

> PSUAR5 value = 2705021

> PSUAR6 value = 15918574

> PSUAR7 value = 10780321

> PSUCP value = 19771114

> PSUCP1 value = 17802546

> PSUCP2 value = 6628603

> PSUCP3 value = 266373

> PSUCS0 value = 1105018

> PSUCS1 value = 2690675

> PSUCS17 value = 1182805

> PSUCS2 value = 1760097

> PSUCS3 value = 1807764

> PSUCS4 value = 2023448

> PSUCS5 value = 1715619

> PSUCSR0 value = 4822512

> PSUCSR1 value = 6560340

> PSUCSR2 value = 5639812

> PSUDBQUE value = 11635692

> PSUDEM0 value = 6311295

> PSUDEM1 value = 7925968

> PSUDEM2 value = 6722886

> PSUDEM3 value = 2240229

> PSUDEM4 value = 10782922

> PSUDEM5 value = 8224573

> PSUDEM6 value = 1246268

> PSUDEM7 value = 4510645 continued . . .

> PSUDEM8 value = 6660546

> PSUDEM9 value = 2831680

> PSUENV value = 2337736

> PSUHL value = 3698103

> PSULR0 value = 3357916

> PSULR1 value = 2109050

> PSULR2 value = 2242423

> PSULR3 value = 2259242

> PSULR4 value = 3433569

> PSULR5 value = 6545368

> PSULR6 value = 1738680

> PSUMAP0 value = 10846239

> PSUMAPR value = 8795474

> PSUOP0 value = 2639829

> PSUOP1 value = 4220637

> PSUOP2 value = 8813762

> PSUOP3 value = 13796489

> PSUOP4 value = 6248132

> PSUOP5 value = 9056798

> PSUOP6 value = 5380760

> PSUOP7 value = 5382491

> PSUOP8 value = 14667137

> PSUOPAM value = 3339220

> PSUOPMD value = 8613833

> PSUPR0 value = 4023661

> PSUPR1 value = 4340187

> PSUPR2 value = 9531754

> PSUPR3 value = 3440365

> PSUPR4 value = 3448048

> PSUPR5 value = 8260662

> PSUPR6 value = 1813032

> PSURT1 value = 8587609

> PSURT2 value = 2926788

> PSURTQ value = 241328

> PSUSUM1 value = 5954587

> PSUSUM2 value = 11457848

> PSUSUM3 value = 12119964

> PSUSUM4 value = 13648090

> PSUSUM5 value = 9189658

> PSUSUM6 value = 12857626

> PSUSUM7 value = 14299810

> PSUTL value = 4583242

> PSUTL1 value = 1238679

> PSUUD0 value = 1564960 continued . . .

> PSUUD1 value = 5681173

> PSUUD2 value = 7162225

> PSUUD3 value = 5907013

> PSUUD4 value = 2603802

> PSUUD5 value = 4159672

> PSUUD6 value = 7640357

> PSUUD7 value = 5347664

> PSUV0 value = 1980215

> PSUV1 value = 13627369

> PSUV10 value = 7002558

> PSUV11 value = 1038711

> PSUV12 value = 12399968

> PSUV2 value = 13953791

> PSUV3 value = 3638955

> PSUV4 value = 6627596

> PSUV5 value = 3907420

> PSUV6 value = 6845919

> PSUV7 value = 6773340

> PSUV8 value = 6994421

> PSUV9 value = 7069860

> PSUVIT value = 1714

> PSUVIT0 value = 2469

> PSUVIT1 value = 10457162

> PSUVIT2 value = 2058126

# Appendix: Reinstallation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites that have previously installed PSU 4.0 software and are reinstalling it must fulfill the three requirements described below.

## Add Child Protocols to Parent Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first requirement is to add the child protocols listed below to the appropriate parent protocol. This requirement may be met either before or after the PSU 4.0 reinstall as long as it is completed before going into Production.

![](benefits-management-version-4-install-guide-extract-enhancements-phases-i-thru-i/006.png)Note: If PSU PATIENT DEMOGRAPHIC CHANGE is already attached to the DG FIELD MONITOR protocol, leave it attached.

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parent Protocol</strong></th>
<th><strong>Associated Child Protocols</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LR7O ALL EVSEND RESULTS</td>
<td><p>1) LA7 LAB RESULTS ACTION</p>
<p>2) ROR EVENT LAB</p>
<p>3) RG LAB EVENT</p>
<p>4) RG MICRO EVENT</p></td>
</tr>
<tr class="even">
<td>DG FIELD MONITOR</td>
<td><p>1) PSU PATIENT DEMOGRAPHIC CHANGE</p>
<p>2) SCMC PCMM INACTIVATE ON DATE OF DEATH</p>
<p>3) ROR EVENT LAB</p>
<p>4) RG LAB EVENT</p>
<p>5) RG MICRO EVENT</p></td>
</tr>
</tbody>
</table>

If your site does not have a child protocol listed above, it simply means that your site does not use that protocol.  
Example: Adding child protocols or items to a parent protocol using VA FileMan.

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: INSTALL// PROTOCOL (4900 entries)

EDIT WHICH FIELD: ALL// NAME

THEN EDIT FIELD: ITEM

1 ITEM (multiple)

2 ITEM TEXT

CHOOSE 1-2: 1 ITEM (multiple)

EDIT WHICH ITEM SUB-FIELD: ALL// .01 ITEM

THEN EDIT ITEM SUB-FIELD: \<Enter\>

THEN EDIT FIELD: \<Enter\>

Adding child protocols to the parent protocol LR7O ALL EVSEND RESULTS:

Select PROTOCOL NAME: LR7O ALL EVSEND RESULTS LAB RESULTS =\> EXTERNAL PACKAGE

NAME: LR7O ALL EVSEND RESULTS Replace

Select ITEM: ROR EVENT LAB LAB RESULTS =\> ROR PENDING PATIENT // \<Enter\>

ITEM: ROR EVENT LAB LAB RESULTS =\> ROR PENDING PATIENT// \<Enter\>

Select ITEM: LA7 LAB RESULTS ACTION LAB RESULTS =\> EXTERNAL PACKAGE

Select ITEM: RG LAB EVENT Lab --\> CIRN

Select ITEM: RG MICRO EVENT Micro --\> CIRN

Select ITEM:\<Enter\>

\>

Adding child protocols to the parent protocol DG FIELD MONITOR:

Select PROTOCOL NAME: DG FIELD MONITOR DG Field Monitor

Select ITEM: PSU PATIENT DEMOGRAPHIC CHANGE// \<Enter\>

ITEM: PSU PATIENT DEMOGRAPHIC CHANGE // \<Enter\>

Select ITEM: SCMC PCMM INACTIVATE ON DATE OF DEATH

Select ITEM: SPN REG STATUS UPDATE

Select ITEM: SPN REG STATUS DELETE

Select ITEM: FB PATIENT DATA CHANGE

Select ITEM: VAFC MPIPD FIELD TRIGGER

Select ITEM: \<Enter\>

\>

## Delete ^PSULRHL1 and ^PSULRHLI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please delete ^PSULRHL1 and ^PSULRHLI from your test and/or production area(s).

## Install PSU 4.0 Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once your protocols are restored and the ^PSULRHL1 and ^PSULRHLI routines are deleted, please return to section 3 of these Installation Instructions and complete the reinstallation of the PSU 4.0 software.