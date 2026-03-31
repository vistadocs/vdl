---
title: MOCHA Version 2.1 Installation Guide-Dosing Infrastructure
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Dosing Infrastructure
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 2.1
patch_id: PSS*2.1*201
group_key: "PSS:PSS:2.1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - rollback
  - backout
  - transport
  - global
  - required
  - rollbackbackout
  - install
page_count: 0
word_count: 1186
section_count: 8
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p201_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p201_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

> ![](mocha-version-2-1-installation-guide-dosing-infrastructure/001.png)

> Medication Order Check Healthcare Application (MOCHA)

> MOCHA 2.1 Dosing Infrastructure

> Installation Guide

> (Rollback/Backout Plan)

> PSS\*1.0\*201 (Stand Alone) May 2017

> Department of Veterans Affairs Product Development

> *(This page included for two-sided copying.)*

1.  [Introduction 1](#introduction)
    1.  [Purpose 1](#purpose)
2.  [Pre-Requisite Considerations 1](#pre-requisite-considerations)
    1.  [Minimum Required Packages 1](#minimum-required-packages)
    2.  [Required Patches 1](#required-patches)
3.  [Installation Considerations/Restrictions 2](#installation-considerationsrestrictions)
4.  [Installation Order 2](#installation-order)
5.  [Rollback/Backout Preparation 2](#rollbackbackout-preparation)
6.  [Installation of PSS\*1.0\*201 2](#6._Installation_of_PSS*1.0*201)
    1.  [Installation Steps 2](#installation-steps)
        1.  [Install Example 4](#install-example)
7.  [Rollback/Backout Procedure 7](#rollbackbackout-procedure)
    1.  [Rollback/Backout Requirements/Overview 7](#rollbackbackout-requirementsoverview)
        1.  [Cross Reference check prior to rollback/backout installation 7](#cross-reference-check-prior-to-rollbackbackout-installation)
        2.  [Software Required for Rollback/Backout 8](#software-required-for-rollbackbackout)
        3.  [Overview of Rollback/Backout Build 8](#overview-of-rollbackbackout-build)
    2.  [Rollback/Backout Considerations/Restrictions 9](#rollbackbackout-considerationsrestrictions)
    3.  [Rollback/Backout Steps 9](#rollbackbackout-steps)

[Appendix: Acronyms 16](#appendix-acronyms)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
- [Pre-Requisite Considerations](#pre-requisite-considerations)
  - [Minimum Required Packages](#minimum-required-packages)
  - [Required Patches](#required-patches)
- [Installation Considerations/Restrictions](#installation-considerationsrestrictions)
- [Installation Order](#installation-order)
- [Rollback/Backout Preparation](#rollbackbackout-preparation)
  - [Installation Steps](#installation-steps)
    - [Install Example:](#install-example)
- [Rollback/Backout Procedure](#rollbackbackout-procedure)
  - [Rollback/Backout Requirements/Overview](#rollbackbackout-requirementsoverview)
    - [Cross Reference check prior to rollback/backout installation](#cross-reference-check-prior-to-rollbackbackout-installation)
    - [Software Required for Rollback/Backout](#software-required-for-rollbackbackout)
    - [Overview of Rollback/Backout Build](#overview-of-rollbackbackout-build)
  - [Rollback/Backout Considerations/Restrictions](#rollbackbackout-considerationsrestrictions)
  - [Rollback/Backout Steps](#rollbackbackout-steps)
- [Appendix: Acronyms](#appendix-acronyms)
> MOCHA 2.1 Dosing Infrastructure exports new components and enter/edit functionality to prepare for the Daily Dose checks coming in a future patch. In addition, enhancements have been made to the current Single Dose order checks.
> The following patch makes up the release of MOCHA 2.1 Dosing Infrastructure:
| Patch         | Type | Description                 |
|-------------------|----------|---------------------------------|
| PSS\*1.0\*201 | PackMan  | MOCHA 2.1 DOSING INFRASTRUCTURE |

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this Installation Guide is to provide installation steps for MOCHA 2.1 Dosing Infrastructure. The intended audience for this document is the Information Resources Management Service (IRMS) staff responsible for installing these patches.

# Pre-Requisite Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No pre-requisite considerations.

## Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The patches described in this installation guide can only be run with a standard Massachusetts General Hospital Utility Multi-Programming System (MUMPS) operating system and require the following Department of Veterans Affairs (VA) software packages.

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Package</strong></th>
<th><strong>Minimum Version Needed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Pharmacy Data Management</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td><blockquote>
<p>22.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Health<em>e</em>Vet Web Services Client (HWSC)</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Outpatient Pharmacy</td>
<td><blockquote>
<p>7.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Inpatient Medications</td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Order Entry/Results Reporting</td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The above software must be installed for these patches to be completely functional.

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following patches must already be installed on your system: PSS\*1.0\*189

> PSS\*1.0\*173

> PSS\*1.0\*119 PSS\*1.0\*175 PSS\*1.0\*184

# Installation Considerations/Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch should be installed when Pharmacy applications are not in use, no other pharmacy patches are being installed, and when tasked jobs from Clinical Applications are not running.

> Installation should also occur when CPRS usage is at a minimum, particularly medication activities. Installation of this patch should take no longer than 5 minutes.

# Installation Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\) PSS\*1.0\*201

# Rollback/Backout Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The rollback/backout procedure for these patches should only occur when there is concurrence from the Enterprise Product Support and MOCHA development teams, because of the complexity and risk involved in a rollback/backout. Normal installation back-ups using KIDS will back up only Mumps routines. For all non-routine components of these builds, Enterprise Product Support will have a build available if needed. Make sure the ‘Backup a Transport Global’ step in section 6 of this document is followed, so you do have a backup of all the routines if needed.

> If your site has local modifications to any of the following non-routine components of the builds, they will need to be backed up locally. Please contact Enterprise Product Support prior to installing if there are questions:

> PSSJ SCHEDULE EDIT Input Template from the ADMINISTRATION SCHEDULE (#51.1) File NAME (#.01) Field Data dictionary definition of the MEDICATION INSTRUCTION (#51) File SYNONYM (#.5) Field Data dictionary definition of the MEDICATION INSTRUCTION (#51) File

1.  <span id="6._Installation_of_PSS*1.0*201" class="anchor"></span>Installation of PSS\*1.0\*201

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  LOAD TRANSPORT GLOBAL

> Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option to unload the build.

2.  Start up the Kernel Installation and Distribution System Menu \[XPD MAIN\]:

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

> ---

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

3.  From the Installation menu, you may elect to use the following options (When prompted for the INSTALL NAME, enter PSS\*1.0\*201):
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will

> not backup any other changes such as DD's or templates.

2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  Use the Install Package(s) option and select the package PSS\*1.0\*201.
1.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', answer NO.
2.  When prompted 'Want to DISABLE Scheduled Options and Menu Options and Protocols? YES//', answer NO.

### Install Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Programmer Options \<TEST ACCOUNT\> Option: KI Kernel Installation & Distribution System

> Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: Installation

> Select Installation \<TEST ACCOUNT\> Option: Install Package(s) Select INSTALL NAME: PSS\*1.0\*201 11/28/16@12:01:14

> =\> PSS\*1.0\*201

> This Distribution was loaded on Nov 28, 2016@12:01:14 with header of PSS\*1.0\*201

> It consisted of the following Install(s): PSS\*1.0\*201

> Checking Install for Package PSS\*1.0\*201

> Will first run the Environment Check Routine, PSS1P201

> Install Questions for PSS\*1.0\*201

> Incoming Files:

51. MEDICATION INSTRUCTION (Partial Definition) Note: You already have the 'MEDICATION INSTRUCTION' File.
    1.  ADMINISTRATION SCHEDULE (Partial Definition) Note: You already have the 'ADMINISTRATION SCHEDULE' File.
24. DOSE UNITS (including data)

> Note: You already have the 'DOSE UNITS' File. I will OVERWRITE your data with mine.

25. DOSE UNIT CONVERSION (including data)

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// SSH VIRTUAL TERMINAL

> Install Started for PSS\*1.0\*201 : Nov 28, 2016@12:01:51

> Build Distribution Date: Nov 28, 2016

> Installing Routines:

> Nov 28, 2016@12:01:51

> Installing Data Dictionaries:

> Nov 28, 2016@12:01:51

> Installing Data:

> Nov 28, 2016@12:01:52

> Installing PACKAGE COMPONENTS: Installing INPUT TEMPLATE

> Nov 28, 2016@12:01:52

> Running Post-Install Routine: POST^PSS1P201 Adding entries to APSP Intervention Type file Updating Routine file...

> Updating KIDS files...

> PSS\*1.0\*201 Installed.

> Nov 28, 2016@12:01:53

> Not a production UCI Install Completed

> ![](mocha-version-2-1-installation-guide-dosing-infrastructure/002.png) Note: Installation of PSS\*1.0\*201 is completed. The following procedure is to be followed only if PSS\*1.0\*201 needs to be backed out.

# Rollback/Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This last section of the document is only needed if there are major problems resulting from the installation of PSS\*1.0\*201, and there is concurrence from the Enterprise Product Support and MOCHA Development Teams that a rollback/backout must occur.

## Rollback/Backout Requirements/Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the requirements for rollback/backout, along with an overview of the rollback build.

### Cross Reference check prior to rollback/backout installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following two global listings must be done from programmer mode, along with the verification checks for each. If either of these verification checks fail, you must stop the rollback/backout process and contact Enterprise Product Support for assistance before continuing.

> Global Listing 1:

> Run the global lister from programmer mode as follows and verify that only 2 entries are returned, and that the first entry has a subscript ending in 1,0), and is equal to “51.113^B”, and that the next entry’s subscript ends in 3,0), and is equal to “51.1^D”:

> Note: There are consecutive comma’s just before the last ‘0’ in the global listing

> D ^%G

> For help on global specifications DO HELP^%G Global ^DD(51.113,.01,1,,0

> ^DD(51.113,.01,1,1,0)="51.113^B"

> ^DD(51.113,.01,1,3,0)="51.1^D"

> Global Listing 2:

> Run the global lister from programmer mode as follows and verify that only 2 entries are returned, and that the first entry has a subscript ending in 1,0), and is equal to “51.33^B”, and that the next entry’s subscript ends in 3,0), and is equal to “51^D”:

> Note: There are consecutive comma’s just before the last ‘0’ in the global listing

> D ^%G

> For help on global specifications DO HELP^%G

> Global ^DD(51.33,.01,1,,0

> ^DD(51.33,.01,1,1,0)="51.33^B"

> ^DD(51.33,.01,1,3,0)="51^D"

### Software Required for Rollback/Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Make sure you have the following software available for the rollback/backout:

1.  Routine backup from PSS\*1.0\*201 Install. This is not needed if you had no local mods to the routines in PSS\*1\*201, since the PSS\*1.0\*202 Rollback/Backout patch will contain these routines.
2.  Your local backups (if backups were made for local modifications from section 5) of the PSSJ SCHEDULE EDIT Input Template, the Data Dictionary NAME (#.01) Field from the MEDICATION INSTRUCTION (#51) File, and the SYNONYM (#.5) Field from the MEDICATION INSTRUCTION (#51) File.
3.  Rollback/Backout Patch PSS\*1.0\*202. This patch is available from Enterprise Product Support upon request.

### Overview of Rollback/Backout Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PSS\*1.0\*202 Rollback/Backout patch will do the following:

> PSS\*1.0\*202 will restore the following routines to their pre-PSS\*1.0\*201 state: PSSDDUT

> PSSDSAPD PSSDSAPL PSSDSAPM PSSFDBDI PSSFDBRT PSSFILED PSSJEEU PSSJSV PSSMIRPT PSSSCHRP

> PSS\*1.0\*202 will restore the following ADMINISTRATION SCHEDULE (#51.1) File Input Template to its pre-PSS\*1.0\*201 state:

> PSSJ SCHEDULE EDIT

> PSS\*1.0\*202 will delete the following routines since they were new with PSS\*1.0\*201: PSS1P201

> PSSDSUTL PSSOAS

> PSS\*1.0\*202 will remove the "AF" cross reference from the NAME (#.01) Field of the MEDICATION INSTRUCTION (#51) File.

> PSS\*1.0\*202 will restore the Input Transform and Executable Help of the NAME (#.01) Field of the MEDICATION INSTRUCTION (#51) File.

> PSS\*1.0\*202 will restore the Input Transform and Executable Help of the SYNONYM (#.5) Field of the MEDICATION INSTRUCTION (#51) File.

> PSS\*1.0\*202 will remove the Data Dictionaries and data of the DOSING CHECK FREQUENCY (#32) field, the DRUG(S) FOR DOSING CHK FREQ Fields (#51.321) SubFile, and OLD MED INSTRUCTION NAME(S) (#51.33) Subfile from the MEDICATION INSTRUCTION (#51) File.

> PSS\*1.0\*202 will remove the Data Dictionaries and data of the DOSING CHECK FREQUENCY (#11) field, the DRUG(S) FOR DOSING CHK FREQ Fields (#51.111) SubFile, and OLD SCHEDULE NAME(S) (#51.113) Subfile from the ADMINISTRATION SCHEDULE (#51.1) File.

> PSS\*1.0\*202 will delete the DOSE UNIT CONVERSION (#51.25) File Data Dictionary and data. PSS\*1.0\*202 will revert the data stored in the first entry of the DOSE UNITS (#51.24) File.

> Note: PSS\*1.0\*201 added new entries to the APSP INTERVENTION TYPE (#9009032.3) File, but PSS\*1.0\*202 will not delete these entries since entries in other files may already point to these new entries.

## Rollback/Backout Considerations/Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This rollback/backout should occur when Pharmacy applications are not in use, no other pharmacy patches are being installed and when tasked jobs from Clinical Applications are not running.

> Rollback/Backout should also occur when CPRS usage is at a minimum, particularly medication activities.

> The rollback/backout procedure should take no longer than 15 minutes.

## Rollback/Backout Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Install the PSS\*1.0\*202 RollBack/Backout patch as follows:

1.  LOAD TRANSPORT GLOBAL

> Choose the PackMan message containing PSS\*1.0\*202 and invoke the INSTALL/CHECK MESSAGE PackMan option to unload the build.

2.  Start up the Kernel Installation and Distribution System Menu \[XPD MAIN\]:

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

> ---

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

3.  From the Installation menu, you may elect to use the following options (When prompted for the INSTALL NAME, enter PSS\*1.0\*202):
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will

> not backup any other changes such as DD's or templates.

2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
    1.  Use the Install Package(s) option and select the package

> PSS\*1.0\*202.

1.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', answer NO.
2.  When prompted 'Want to DISABLE Scheduled Options and Menu Options and Protocols? YES//', answer NO.

> PSS\*1.0\*202 installation capture:

> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s) Select INSTALL NAME: PSS\*1.0\*202 2/17/17@13:54:22

> =\> PSS\*1\*202 TEST v4

> This Distribution was loaded on Feb 17, 2017@13:54:22 with header of PSS\*1\*202 TEST v4

> It consisted of the following Install(s):

> PSS\*1.0\*202

> Checking Install for Package PSS\*1.0\*202

> Will first run the Environment Check Routine, PSS202EN

> Are you sure you want to install PSS\*1\*202 to rollback patch PSS\*1\*201? NO// YES Install Questions for PSS\*1.0\*202

> Incoming Files:

> 51 MEDICATION INSTRUCTION (Partial Definition) Note: You already have the 'MEDICATION INSTRUCTION' File.

> 51.24 DOSE UNITS (including data)

> Note: You already have the 'DOSE UNITS' File.

> I will REPLACE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages. Enter a '^' to abort the install.

> DEVICE: HOME// ;;99999 HOME (CRT)

> Install Started for PSS\*1.0\*202 : Feb 17, 2017@13:55:07

> Build Distribution Date: Feb 17, 2017

> Installing Routines:

> Feb 17, 2017@13:55:07

> Installing Data Dictionaries:

> Feb 17, 2017@13:55:07

> Installing Data:

> Feb 17, 2017@13:55:07

> Installing PACKAGE COMPONENTS: Installing INPUT TEMPLATE

> Feb 17, 2017@13:55:07

> Running Post-Install Routine: POST^PSS202RB

> \*\*Deleting executable help from NAME and SYNONYM fields in MEDICATION INSTRUCTIO

> N (#51) File\*\*

> \*\*Removing the 'AF' cross reference from the .01 field of the MEDICATION INSTRUC TION (#51) File\*\*

> Done!

> \*\*Removing DOSING CHECK FREQUENCY (#32) field and data from the MEDICATION INSTR

> UCTION (#51) file\*\* Done!

> \*\*Removing DRUG(S) FOR DOSING CHK FREQ (#51.321) multiple and OLD MED INSTRUCTIO

> N NAME(S) (#51.33) multiple from the MEDICATION INSTRUCTION (#51) file\*\* Done!

> Removing DOSING CHECK FREQUENCY (#11) field and data from the ADMINISTRATION SCH

> EDULE (#51.1) file\*\* Done!

> \*\*Removing DRUG(S) FOR DOSING CHK FREQ (#51.111) multiple and OLD MED INSTRUCTIO

> N NAME(S) (#51.113) multiple from the ADMINISTRATION SCHEDULE (#51.1) file\*\* Done!

> Removing the DOSE UNIT CONVERSION (#51.25) file and data from system\*\* Done!

> Updating Routine file... Updating KIDS files...

> PSS\*1.0\*202 Installed.

> Feb 17, 2017@13:55:07

> No link to PACKAGE file Install Completed

> 51 MEDICATION INSTRUCTION (Partial Definition)

> Note: You already have the 'MEDICATION INSTRUCTION' File.

#### If you had local modifications to the PSSJ SCHEDULE EDIT Input Template, or the Data Dictionary NAME (#.01) Field from the MEDICATION INSTRUCTION (#51) File, or the Data Dictionary SYNONYM (#.5) Field from the MEDICATION INSTRUCTION (#51) File, from Section 5, restore them now.

#### If you had local modifications to any of the routines exported in PSS\*1.0\*201, restore that backup now. If you did not have local modifications, no action is required for this step.

> \*\*\*Reminder - If you are restoring your back-up, if for some reason the PSS\*1.0\*201 build was installed multiple times, make sure you restore the back up from the first install.

#### An Environment Check routine (PSS202EN) and an init routine (PSS202RB) came with the PSS\*1.0\*202 Rollback/Backout patch, and were marked to delete after install, but that deletion may be overridden by a Kernel parameter. So you may use the following option to verify that these routines have been deleted, and subsequently deleted them if desired, if they do still exist:

> Select Systems Manager Menu \<TEST ACCOUNT\> Option: PRogrammer Options Select Programmer Options \<TEST ACCOUNT\> Option: ROutine Tools

> Select Routine Tools \<TEST ACCOUNT\> Option: DElete Routines ROUTINE DELETE

> All Routines? No =\> No

> Routine: PSS202EN Routine: PSS202RB Routine:

> 2 routines

> 2 routines to DELETE, OK: NO// Y PSS202EN PSS202RB

> Done.

#### Patch Installation Tracking:

> Access VA FileMan and then follow these bolded steps to update the PACKAGE (#9.4) File to accurately reflect the current state of the account in regards to the PSS\*1.0\*201 patch.

> VA FileMan 22.0

> Select OPTION: ENTER OR EDIT FILE ENTRIES \<Enter\>

> INPUT TO WHAT FILE: OPTION// 9.4 \<Enter\> PACKAGE (441 entries)

> EDIT WHICH FIELD: ALL// VERSION \<Enter\> (multiple)

> EDIT WHICH VERSION SUB-FIELD: ALL// PATCH APPLICATION HISTORY \<Enter\>

> (multiple)

> EDIT WHICH PATCH APPLICATION HISTORY SUB-FIELD: ALL// .01\<Enter\> PATCH APPLICATION HISTORY

> THEN EDIT PATCH APPLICATION HISTORY SUB-FIELD: \<Enter\>

> THEN EDIT VERSION SUB-FIELD: \<Enter\>

> THEN EDIT FIELD: \<Enter\>

> Select PACKAGE NAME: PSS \<Enter\> PHARMACY DATA MANAGEMENT PSS

> Select VERSION: 1.0// \<Enter\>

> Select PATCH APPLICATION HISTORY: 201// @ \<Enter\> {Note: If 201 is not the default patch number, enter 201. Once 201 is selected, delete the 201 entry.}

> SURE YOU WANT TO DELETE THE ENTIRE '201' PATCH APPLICATION HISTORY? Y

> \<Enter\> (Yes)

> {Note: The next 2 lines will not display if the default above had to be changed.}

> Select PATCH APPLICATION HISTORY: 193 SEQ \#174// \<Enter\>

> PATCH APPLICATION HISTORY: 193 SEQ \#174// \<Enter\>

> Select PATCH APPLICATION HISTORY: \<Enter\>

> Verify the Patch Application History was removed using the function identified below. If anything other than a ‘0’ is displayed after any the command, please contact Enterprise Product Support.

> CDEVISC1A2:MDEVC\>W \$\$PATCH^XPDUTL("PSS\*1.0\*201") \<Enter\>

> 0

# Appendix: Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term | Definition                                                  |
|----------|-----------------------------------------------------------------|
| CPRS     | Computerized Patient Record System                              |
| DD       | Data Dictionaries                                               |
| FDB      | First Databank                                                  |
| FTP      | File Transfer Protocol                                          |
| HWSC     | Heath*<u>e</u>*Vet Web Services Client                          |
| IRMS     | Information Resources Management Service                        |
| KIDS     | Kernel Installation and Distribution System                     |
| MOCHA    | Medication Order Check Healthcare Application                   |
| MUMPS    | Massachusetts General Hospital Utility Multi-Programming System |
| NDF      | National Drug File                                              |
| PDM      | Pharmacy Data Management                                        |
| PECS     | Pharmacy Enterprise Customization System                        |
| PEPS     | Pharmacy Enterprise Product System                              |
| PMI      | Patient Medication Information                                  |
| VA       | Department of Veterans Affairs                                  |
| VDL      | VA Software Document Library                                    |
| VISTA    | Veterans Health Information Systems and Technology Architecture |