---
title: MOCHA Version 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 2
patch_id: PSS*2*160
group_key: "PSS:PSS:2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - install
  - installation
  - mocha
  - table
  - patch
  - routine
  - contents
  - build
  - patches
  - message
page_count: 0
word_count: 8786
section_count: 25
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p160_mocha_cb_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p160_mocha_cb_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

> ![](mocha-version-2-installation-guide/001.png)

Medication Order Check Healthcare Application (MOCHA) v2.0Combined BuildInstallation Guide

PSJ\*5\*252, PSO\*7\*372, and OR\*3\*345  
(MOCHA 2.0 Combined Build 1.0)

PSJ\*5\*257, PSO\*7\*416, OR\*3\*311, and GMRA\*4\*47  
(MOCHA 2.0 FOLLOW UP Combined Build 1.0)

PSS\*1\*160, PSS\*1\*173, and OR\*3\*381 (Stand Alone)

PSJ\*5\*299 and PSO\*7\*431

(MOCHA 2.0 FAST TRACK BUILDS 1.0)

March 2014

Product Development

*(This page included for two-sided copying.)*

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
- [Pre-Requisite Considerations](#pre-requisite-considerations)
  - [Minimum Required Packages](#minimum-required-packages)
  - [Required Patches](#required-patches)
- [Installation Order](#installation-order)
- [Installation of PSS\1\160](#installation-of-pss1160)
  - [Installation Considerations](#installation-considerations)
  - [Pre-Installation Instructions](#pre-installation-instructions)
  - [Installation Steps](#installation-steps)
  - [Post Install Instructions](#post-install-instructions)
    - [Verify PSS\1\160 Install MAILMAN Message is Received](#verify-pss1160-install-mailman-message-is-received)
    - [Verify Web Services are Enabled](#verify-web-services-are-enabled)
    - [Re-Attach any Locally Added Options](#re-attach-any-locally-added-options)
- [Installation of PSS\1\173](#installation-of-pss1173)
  - [Installation Considerations](#installation-considerations-1)
  - [Pre-Installation Instructions](#pre-installation-instructions-1)
  - [Installation Steps](#installation-steps-1)
- [Installation of MOCHA 2.0 COMBINED BUILD](#installation-of-mocha-20-combined-build)
  - [Installation Considerations](#installation-considerations-2)
  - [Pre-Installation Instructions](#pre-installation-instructions-2)
  - [Installation Steps](#installation-steps-2)
- [Installation of MOCHA 2.0 FOLLOW UP COMBINED BUILD](#installation-of-mocha-20-follow-up-combined-build)
  - [Installation Considerations](#installation-considerations-3)
  - [Pre-Installation Instructions](#pre-installation-instructions-3)
  - [Installation Steps](#installation-steps-3)
  - [Post Installation Instructions](#post-installation-instructions)
    - [Verify Post Install MAILMAN Message is Received](#verify-post-install-mailman-message-is-received)
- [Installation of OR\3\381](#installation-of-or3381)
  - [Installation Considerations](#installation-considerations-4)
  - [Pre-Installation Instructions](#pre-installation-instructions-4)
  - [Installation Steps](#installation-steps-4)
- [Installation of MOCHA 2.0 FAST TRACK BUILDS 1.0](#installation-of-mocha-20-fast-track-builds-10)
  - [Installation Considerations](#installation-considerations-5)
  - [Pre-Installation Instructions](#pre-installation-instructions-5)
  - [Installation Steps](#installation-steps-5)
- [Verify Dosing Checks are Enabled](#verify-dosing-checks-are-enabled)
  - [Post Installation Instructions](#post-installation-instructions-1)
Medication Order Check Healthcare Application (MOCHA) v2.0 provides a Maximum Single Dose Order Check to the current existing Veterans Health Information Systems and Technology Architecture (VistA) medication order checking system that uses the First Databank (FDB) business logic and database. FDB is the clearing house that the Department of Veterans Affairs (VA) uses for Dosing Order Checks. Pharmacy Enterprise Customization System (PECS) application is a Graphical User Interface (GUI) application that was developed for customization of FDB dosing records. A process to automatically update the standard and custom FDB data at each instance of the Cache’ database was also provided.
The following patches make up the release of MOCHA v2.0:
<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Patch</strong></th>
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PSS_1_160.KID</strong></td>
<td>Host File</td>
<td>Pharmacy Data Management (PDM) Dosing patch</td>
</tr>
<tr class="even">
<td><strong>PSS_1_173.KID</strong></td>
<td>Host file</td>
<td>PDM Dosing follow up patch to PSS*1*160</td>
</tr>
<tr class="odd">
<td><strong>MOCHA_2_0.KID</strong></td>
<td>Host File</td>
<td><p>MOCHA 2.0 combined build that contains dosing patches:</p>
<p>PSJ*5*252 - Inpatient Medications patch PSO*7*372 - Outpatient Pharmacy patch OR*3*345 - Computerized Patient Record System(CPRS) patch</p></td>
</tr>
<tr class="even">
<td><strong>MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID</strong></td>
<td>Host File</td>
<td><p>MOCHA 2.0 combined build that contains dosing patches:</p>
<p>PSJ*5*257 - Inpatient Medications patch PSO*7*416 - Outpatient Pharmacy patch OR*3*311 - CPRS patch</p>
<p>GMRA*4*47 - Adverse Reaction Tracking patch</p></td>
</tr>
</tbody>
</table>
The following patches will require installation following the successful installation of MOCHA v2.0 patches:
<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 15%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Patch</strong></th>
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>OR*3*381</strong></td>
<td>Host File</td>
<td>CPRS follow up patch</td>
</tr>
<tr class="even">
<td><strong>MOCHA_2_0_FAST_TRACK_BUILDS.KID</strong></td>
<td>Host File</td>
<td><p>MOCHA 2.0 FAST TRACK PATCHES 1.0 contains the following patches:</p>
<p>PSJ*5*299</p>
<p>PSO*7*431</p></td>
</tr>
</tbody>
</table>
These patches will introduce the first increment of a new Dosing Order Check system that utilizes data and logic from FDB. The new Maximum Single Dose Order Checks will occur in Outpatient Pharmacy, Inpatient Medications, and CPRS.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide installation steps for MOCHA v2.0. The intended audience for this document is the Information Resources Management Service (IRMS) staff and Pharmacy staff responsible for installing and maintaining the Pharmacy files required for drug selection through Pharmacy and CPRS.

MOCHA v2.0 will integrate the existing Veterans Health Information Systems and Technology Architecture (VistA) Pharmacy applications with the new Maximum Single Dose Order Check.

# Pre-Requisite Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before continuing any further, you should have previously installed OR\*3\*366 which provides reports for potential issues for Quick Orders concerning free text dosage and mixed-case drug names. Additionally, modifications should have been made based on these reports to the quick orders to eliminate unnecessary Dosing Order Check error messages.

## Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patches described in this installation guide can only be run with a standard Massachusetts General Hospital Utility Multi-Programming System (MUMPS) operating system and require the following Department of Veterans Affairs (VA) software packages.

| Package                                 | Minimum Version Needed |
|-----------------------------------------|------------------------|
| Pharmacy Data Management                | 1.0                    |
| VA FileMan                              | 22.0                   |
| Kernel                                  | 8.0                    |
| Health*e*Vet Web Services Client (HWSC) | 1.0                    |
| Outpatient Pharmacy                     | 7.0                    |
| Inpatient Medications                   | 5.0                    |
| Order Entry/Results Reporting           | 3.0                    |
| Adverse Reaction Tracking               | 4.0                    |

The above software must be installed for these patches to be completely functional.

## Required Patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches should already be installed on your system:

- 
- GMRA\*4\*45
- OR\*3\*337
- OR\*3\*357
- OR\*3\*371
- OR\*3\*346
- OR\*3\*380
- OR\*3\*383
- PSJ\*5\*195
- PSJ\*5\*267
- PSJ\*5\*268
- PSJ\*5\*270
- PSJ\*5\*271
- PSJ\*5\*285
- PSJ\*5\*288
- PSJ\*5\*292
- PSJ\*5\*295
- PSO\*7\*378
- PSO\*7\*379
- PSO\*7\*386
- PSO\*7\*387
- PSO\*7\*390
- PSO\*7\*391
- PSO\*7\*396
- PSO\*7\*413
- PSS\*1\*117
- PSS\*1\*151
- PSS\*1\*157
- PSS\*1\*163
- PSS\*1\*164
- PSS\*1\*168
- PSS\*1\*169

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>IMPORTANT: Please ensure OR*3*380 and OR*3*383 are installed prior to the installation of the MOCHA v2.0 patches.</p>
<p>When OR*3*311 is installed during installation step #4, the ‘before’ checksum and second line of routine ORCMED, listed below, will not match what is in the patch description since patch OR*3*311 does not include patch OR*3*380 or OR*3*383. The functionality of patch OR*3*380 and OR*3*383 is overwritten by patch OR*3*311. However, when patch OR*3*381 is installed during installation step #5, the second line of routine ORCMED is corrected and the functionality introduced with patch OR*3*380 and OR*3*383 is restored.</p>
<p>Before checksum: 62390463</p>
<p>Before patch list: 4,7,38,48,94,141,178,190,195,243,306,371,380</p>
<p>Please ensure OR*3*380 and OR*3*383 are installed prior to the installation of the MOCHA v2.0 patches.</p></th>
</tr>
<tr class="odd">
<th>![](mocha-version-2-installation-guide/002.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Once all the patches in the section have been completed and validated, you may proceed to the installation of PSS\*1\*160.

# Installation Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Note:                                             | The person installing the builds will receive warning(s) related to the second lines of several routines; this is due to the sequence of released patches prior to MOCHA v2.0. Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately. These discrepancies are noted for each host file installed. |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-2-installation-guide/003.png) |                                                                                                                                                                                                                                                                                                                                                           |

MOCHA v2.0 patches should be installed in the following order and should be installed consecutively together. Please review individual patch install information in the following sections for pre and post installation instructions.

1.  PSS_1_160.KID – HOST file with patch name PSS\*1\*160.
2.  PSS_1_173.KID – HOST file with patch name PSS\*1\*173.
3.  MOCHA_2_0.KID - HOST file with patch name MOCHA 2.0 Combined Build 1.0.
4.  MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID - HOST file with patch name MOCHA 2.0 FOLLOW UP BUILD Combined Build 1.0.
5.  OR_3_381.KID – HOST file with patch name OR\*3\*381.
6.  MOCHA_2_0_FAST_TRACK_BUILDS.KID – HOST file with patches: PSJ\*5.0\*299 and PSO\*7\*431.

# Installation of PSS\*1\*160

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*160 should not be installed when PDM options or National Drug File (NDF) options are being used. Also, it should not be installed at the same time any NDF patches are being installed, including DATA UPDATES patches, Patient Medication Information (PMI) Sheet MAPPING patches, and PMI UPDATES patches. Since this patch exports so many PDM components that could be invoked from other Clinical Applications, we recommend it be installed during Non-Peak hours for all Clinical Applications, including tasked jobs from Clinical Applications. Do not queue the installation of this patch. Failure to heed this warning may result in 'source routine edited' errors during a database update. Edits may be lost and records may be left in an inconsistent state.

Installation should take no longer than ten minutes.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inquire into the *Dosages* \[PSS DOSAGES MANAGEMENT\] Menu Option and make note of any locally added options under this menu, since the *Lookup Dosing Check Info for Drug* \[PSS DRUG DOSING LOOKUP\] and *Drug Names with Trailing Spaces Report* \[PSS TRAILING SPACES REPORT\] options are being added to this menu during the POST-INSTALL.

The Environment Check routine PSS160EN will perform the following:

- Checks to see if any entries in the MEDICATION ROUTES (#51.2) File remain unmapped to an entry in the STANDARD MEDICATION ROUTES (#51.23) File. It also checks to see if there are any entries in the LOCAL POSSIBLE DOSAGE (#50.0904) Subfile of the DRUG (#50) File that do not have data populated for either the DOSE UNIT (#4) Field or NUMERIC DOSE (#5) Field. If either of these are true, the patch installer will be given a prompt to either continue with the install, or abort the install.
- It should be noted that not all Medication Routes can be mapped at this time. For a few Medication Routes (Intrathoracic, Intrafollicular), it was recommended that they be left unmapped. Because of this, all sites should see a warning message stating that not all Medication Routes have been mapped during the install, and the installer will be prompted to continue. Below is an example of the warning message text:

  *If there are still local Medication Routes marked for 'ALL PACKAGES' not yet mapped, any orders containing an unmapped Medication Route will not have dosage checks performed. Please refer to the 'Medication Route Mapping Report' \[PSS MED ROUTE MAPPING REPORT\] option for more details.*
- If the Pharmacy Automated Data Processing Application Coordinator (ADPAC) has completed the rest of the required mapping, then the installer should continue with the installation.

The Post-Init routine PSS160PO will perform the following:

- Attach the *Lookup Dosing Check Info for Drug* \[PSS DRUG DOSING LOOKUP\] option to the *Dosages* \[PSS DOSAGES MANAGEMENT\] Menu Option.
- Attach the *Drug Names with Trailing Spaces Report* \[PSS TRAILING SPACES REPORT\] option to the *Dosages* \[PSS DOSAGES MANAGEMENT\] Menu Option.
- Verify that the entries FILM(S) and ELISA UNIT(S) were added to the DOSE UNITS File (#51.24) properly, and verify that the two new synonyms were added to the MILLIONUNIT(S) entry. If a problem is detected with any of these entries, that problem will be noted in the VistA mail message that is generated upon completion of the patch install, and a Remedy ticket should be created for assistance.
- Turn the Dosing Order Checks functionality on.
- Send a mail message to the patch installer and to the members of the PSS ORDER CHECKS Mail Group indicating that the install is complete.

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download PSS_1_160.KID into your local directory.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File: “, respond with PSS_1_160.KID

> Example: USER\$:\[ABC\]PSS_1_160.KID

4.  If given the option to run any Environment Check Routine(s), answer "YES”.
5.  From this menu, you may then select to use the following options:

| Note:                                             | The following are OPTIONAL - (When prompted for the INSTALL NAME, enter PSS\*1.0\*160) |
|---------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](mocha-version-2-installation-guide/004.png) |                                                                                        |

- Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as Data Dictionaries (DD) or templates.
- Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file PSS_1_160.KID you will see the following warnings on certain routines:</p>
<p><u>PSS*1*160:</u></p>
<p>Routine: PSSHRVL1</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>This warning is due to the sequence of released patches prior to MOCHA v2.0.  Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th>![](mocha-version-2-installation-guide/005.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global - This option will allow you to view the components of the KIDS build.
6.  Select the Installation option Install Package(s). This is the step to start the installation of this KIDS patch:
1.  Choose the Install Package(s) option to start the patch install and enter "PSS\*1.0\*160" at the INSTALL NAME prompt.
2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO
3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO
4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO
7.  Install Example:

Select Installation \<TEST ACCOUNT\> Option:  Load a Distribution

Enter a Host File: ANON\$:\[ANONYMOUS\]PSS_1_160.KID

KIDS Distribution saved on May 03, 2013@14:08:02

Comment: PSS\*1\*160   5/3/13

This Distribution contains Transport Globals for the following Package(s):

Build PSS\*1.0\*160 has been loaded before, here is when:

      PSS\*1.0\*160   Install Completed

                    was loaded on Jan 17, 2013@16:51

      PSS\*1.0\*160   Install Completed

                    was loaded on Jan 25, 2013@09:11:34

      PSS\*1.0\*160   Install Completed

                    was loaded on Feb 14, 2013@14:47:50

      PSS\*1.0\*160   Install Completed

                    was loaded on May 03, 2013@14:45:57

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES// YES

Loading Distribution...

   PSS\*1.0\*160

Use INSTALL NAME: PSS\*1.0\*160 to install this Distribution.

   1      Load a Distribution

   2      Verify Checksums in Transport Global

   3      Print Transport Global

   4      Compare Transport Global to Current System

   5      Backup a Transport Global

   6      Install Package(s)

          Restart Install of Package(s)

          Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME: PSS\*1.0\*160      6/11/13@09:47:12

     =\> PSS\*1\*160 HOST FILE  5/3/13  ;Created on May 03, 2013@14:32:51

This Distribution was loaded on Jun 11, 2013@09:47:12 with header of

   PSS\*1\*160 V13 HOST FILE  5/3/13  ;Created on May 03, 2013@14:32:51

   It consisted of the following Install(s):

    PSS\*1.0\*160

Checking Install for Package PSS\*1.0\*160

Will first run the Environment Check Routine, PSS160EN

Checking for any remaining unmapped Local Medication Routes...

There are still local Medication Routes marked for 'ALL PACKAGES' not yet

mapped. Any orders containing an unmapped medication route will not have

dosage checks performed. Please refer to the 'Medication Route Mapping Report'

option for more details.

Checking for any remaining Local Possible Dosages missing data...

There are still local possible dosages eligible for dosage checks that have

missing data in the Numeric Dose and Dose Unit fields. Any orders containing

such local possible dosages may not have dosage checks performed. Please

refer to the 'Local Possible Dosages Report' option for more details.

Do you want to continue to install this patch? Y// ES

Install Questions for PSS\*1.0\*160

Incoming Files:

   51.1      ADMINISTRATION SCHEDULE  (Partial Definition)

> **NOTE:** You already have the 'ADMINISTRATION SCHEDULE' File.

   51.24     DOSE UNITS  (including data)

> **NOTE:** You already have the 'DOSE UNITS' File.

I will REPLACE your data with mine.

   59.7      PHARMACY SYSTEM  (Partial Definition)

> **NOTE:** You already have the 'PHARMACY SYSTEM' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   SSH VIRTUAL TERMINAL

Install Started for PSS\*1.0\*160 :

               Jun 11, 2013@09:47:41

Build Distribution Date: May 03, 2013

 Installing Routines:

               Jun 11, 2013@09:47:42

 Installing Data Dictionaries: .

               Jun 11, 2013@09:47:43

 Installing Data:

               Jun 11, 2013@09:47:43

 Installing PACKAGE COMPONENTS:

 

 Installing SECURITY KEY

 Installing INPUT TEMPLATE

 Installing OPTION

               Jun 11, 2013@09:47:43

 Running Post-Install Routine: ^PSS160PO

Validating new Dose Unit File (#51.24) entries.

DOSE UNITS File (#51.24) entries are correct.

Linking New PSS DRUG DOSING LOOKUP Option....

New PSS DRUG DOSING LOOKUP option linked successfully...

Linking New PSS TRAILING SPACES REPORT Option....

New PSS TRAILING SPACES REPORT option linked successfully...

Beginning DOSING_INFO Web Service definition for PEPS web server:

 

     DOSING_INFO web service was previously defined.  No action taken.

                                  PSS\*1.0\*160                                   

-------------------------------------------------------------------------------

     DOSING_INFO web service was previously enabled.  No action taken.

Web Service definition process is complete for PEPS web server.

Generating Mail Message....

Mail message sent.

 Updating Routine file...

 Updating KIDS files...

 PSS\*1.0\*160 Installed.

               Jun 11, 2013@09:47:43

 Not a production UCI

 NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

## Post Install Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Verify PSS\*1\*160 Install MAILMAN Message is Received

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please verify that the VistA mail message indicating the POST-INIT has run to completion has been received. If this message is not received, please log a Remedy ticket.

The receipt of this VistA mail message will verify the POST-INIT has run to completion. It is important that you read the entire message. If there were any problems with tasks performed by the Environment Check routine or the POST-INIT routine, they will be explained in this mail message, and some may come with instructions to log a Remedy ticket for assistance.

The message subject will be: PSS\*1\*160 Installation Complete. The message text will begin with: Installation of Patch PSS\*1.0\*160 has been completed!

The following is an example of the install MAILMAN message:

Subj: PSS\*1\*160 Installation Complete \[#154914\] 12/21/12@17:31 16 lines

From: PSS\*1\*160 INSTALL In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Installation of Patch PSS\*1.0\*160 has been completed!

There are still local Medication Routes marked for 'ALL PACKAGES' not yet

mapped. Any orders containing an unmapped medication route will not have

dosage checks performed. Please refer to the 'Medication Route Mapping Report'

option for more details.

There are still local possible dosages eligible for dosage checks that have

missing data in the Numeric Dose and Dose Unit fields. Any orders containing

such local possible dosages may not have dosage checks performed. Please

refer to the 'Local Possible Dosages Report' option for more details.

Beginning DOSING_INFO Web Service definition:

DOSING_INFO web service has been defined.

Web Service definition process is complete.

Enter message action (in IN basket): Ignore//

### Verify Web Services are Enabled

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Log into the WEB SERVER MANAGER \[XOBW WEB SERVER MANAGER\] option, select the EP for EXPAND ENTRY action and select the PEPS web server. If the ORDER_CHECKS, DRUG_INFO and/or DOSING_INFO web service are not defined and enabled, please log a Remedy ticket.

Example:

\>D ^XUP

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT100

You have 619 new messages.

Select OPTION NAME: WEB SERVER MANAGER XOBW WEB SERVER MANAGER Web Server Manager

Web Server Manager

<u>Web Server Manager Jan 10, 2013@17:47:44 Page: 1 of 1</u>

HWSC Web Server Manager

Version: 1.0 Build: 31

<u>ID Web Server Name IP Address or Domain Name:Port</u>

1 \*PEPS xx.x.xxx.x:port#

Legend: \*Enabled

AS Add Server TS (Test Server)

ES Edit Server WS Web Service Manager

DS Delete Server CK Check Web Service Availability

EP Expand Entry LK Lookup Key Manager

Select Action:Quit// EP Expand Entry

Select Web Server: (1-1): 1

===============================================================================

1 \*PEPS xx.x.xxx.xx:port#

-------------------------------------------------------------------------------

NAME: PEPS PORT: nnnn

SERVER: nn.n.nnnn.nn STATUS: ENABLED

DEFAULT HTTP TIMEOUT: 30

WEB SERVICE: ORDER_CHECKS STATUS: ENABLED

WEB SERVICE: DRUG_INFO STATUS: ENABLED

WEB SERVICE: DOSING_INFO STATUS: ENABLED

-------------------------------------------------------------------------------

Lookup keys associated with server:

\<No lookup keys associations\>

===============================================================================

Enter RETURN to continue or '^' to exit:

### Re-Attach any Locally Added Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a follow-up to the installation instructions if you had any locally added options under the *Dosages* \[PSS DOSAGES MANAGEMENT\] menu option, please check to see if they need to be re-attached, once the POST-INSTALL is complete and the VistA mail message indicating this has been received.

# Installation of PSS\*1\*173

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should not be installed when PDM options and NDF options are being used. Since this patch exports so many PDM routines that could be invoked from other Clinical Applications, it is recommended that the patch be installed during non-peak hours for all Clinical Applications, and that includes tasked jobs from Clinical Applications. Do not queue the installation of this patch. Failure to heed this warning may result in 'source routine edited' errors during a database update. Edits may be lost and records may be left in an inconsistent state.

This installation should take no longer than five minutes.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSS\*1\*160 must have been installed and the post-install MailMan message should have been received prior to installation of this patch.

## Installation Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download PSS_1_173.KID into your local directory.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for "Enter a Host File:”, respond with PSS_1_173.KID.

> Example: USER\$:\[ABC\]PSS_1_173.KID

4.  If given the option to run any Environment Check Routine(s), answer "YES."
5.  From this menu, you may then select to use the following options:

| Note:                                             | The following are OPTIONAL - (When prompted for the INSTALL NAME, enter PSS\*1.0\*173). |
|---------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](mocha-version-2-installation-guide/006.png) |                                                                                         |

- Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
- Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file PSS_1_173.KID you will see the following warnings on certain routines:</p>
<p><u>PSS*1*173:</u></p>
<p>Routine: PSS551</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>Routine: PSSHRVL1</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p>These warnings are due to the sequence of released patches prior to MOCHA v2.0.  Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th>![](mocha-version-2-installation-guide/007.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global - This option will allow you to view the components of the KIDS build.
6.  Select the Installation option Install Package(s). This is the step to start the installation of this KIDS patch:
1.  Choose the Install Package(s) option to start the patch install and enter "PSS\*1.0\*173" at the INSTALL NAME prompt.
2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO
3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO
7.  Install Example:

Select Installation \<TEST ACCOUNT\> Option:  Load a Distribution

Enter a Host File: ANON\$:\[ANONYMOUS\]PSS_1_173.KID

KIDS Distribution saved on May 03, 2013@14:08:02

Comment: PSS\*1\*173   5/3/13

This Distribution contains Transport Globals for the following Package(s):

Build PSS\*1.0\*173 has been loaded before, here is when:

      PSS\*1.0\*173   Install Completed

                    was loaded on Jan 17, 2013@16:51

      PSS\*1.0\*173   Install Completed

                    was loaded on Jan 25, 2013@09:11:34

      PSS\*1.0\*173   Install Completed

                    was loaded on Feb 14, 2013@14:47:50

      PSS\*1.0\*173   Install Completed

                    was loaded on May 03, 2013@14:45:57

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES// YES

Loading Distribution...

   PSS\*1.0\*173

Use INSTALL NAME: PSS\*1.0\*173 to install this Distribution.

   1      Load a Distribution

   2      Verify Checksums in Transport Global

   3      Print Transport Global

   4      Compare Transport Global to Current System

   5      Backup a Transport Global

   6      Install Package(s)

          Restart Install of Package(s)

          Unload a Distribution

You have PENDING ALERTS

          Enter  "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME:    PSS\*1.0\*173    6/11/13@09:51:54

     =\> PSS\*1\*173 V8  5/3/13  ;Created on May 03, 2013@14:08:02

This Distribution was loaded on Jun 11, 2013@09:51:54 with header of

   PSS\*1\*173 V8  5/3/13  ;Created on May 03, 2013@14:08:02

   It consisted of the following Install(s):

    PSS\*1.0\*173

Checking Install for Package PSS\*1.0\*173

Install Questions for PSS\*1.0\*173

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   SSH VIRTUAL TERMINAL

                                  PSS\*1.0\*173                                  

-------------------------------------------------------------------------------

Install Started for PSS\*1.0\*173 :

               Jun 11, 2013@09:52:06

Build Distribution Date: May 03, 2013

 Installing Routines:

               Jun 11, 2013@09:52:06

 Updating Routine file...

 Updating KIDS files...

 PSS\*1.0\*173 Installed.

               Jun 11, 2013@09:52:06

 Not a production UCI

 NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

# Installation of MOCHA 2.0 COMBINED BUILD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not install these bundles while Pharmacy or Adverse Reaction Tracking users are on the system or when Medication orders are being entered and signed or when allergy updates are being made through CPRS. Do not queue the installation of this bundle. Failure to heed this warning may result in 'source routine edited' errors during a database update. Edits may be lost and records may be left in an inconsistent state. An error that occurs before a cross-reference is executed, for example, may lead to corrupted data or hard errors in the future.

Installation will take no longer than five minutes.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSS\*1\*160 and PSS\*1\*173 must be installed prior to MOCHA_2_0.KID.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><p>The OR*3.0*345 released mail message, from the National Patch Module, displays</p>
<p>some of the routines listed with patches after the 345 patch designation. The checksums displayed for these routines will not match the checksums of the OR*3*345 build, with the exception of routine ORWDXR01. After the first build is installed in the MOCHA v2.0 install (MOCHA Combined Build 1.0), containing patch OR*3*345, if you check the second lines and checksums against that released patch message, the discrepancies will be displayed. However, these discrepancies can be ignored and the installation can continue.</p></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/008.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download MOCHA_2_0.KID into your local directory.
2.  From the Kernel Installation & Distribution System (KIDS) menu, select Installation.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for "Enter a Host File:" respond with MOCHA_2_0.KID.

> Example: USER\$:\[ABC\]MOCHA_2_0.KID

4.  From the KIDS menu, select Installation.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2">The following are OPTIONAL - (When prompted for the INSTALL NAME, enter MOCHA 2.0 Combined Build 1.0)</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/009.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as Data Dictionaries or templates.
2.  Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, data dictionaries (DD), templates, etc.).

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file MOCHA_2_0.KID you will see the following warnings on certain routines:</p>
<p>Host file: MOCHA_2_0.KID contains: PSO*7*372, PSJ*5*252, and OR*3*345</p>
<p><u>PSO*7*372:</u></p>
<p>Routine: PSOCAN</p>
<p>* WARNING, your routine has more patches than the incoming routine *</p>
<p>Routine: PSOCAN2, PSODDPR2, PSODDPR4, PSODDPR5, PSODDPRE, PSOORED3, PSOORED5, PSOORNEW, PSORXEDT, PSOVER1</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p><u>PSJ*5*252:</u></p>
<p>Routine: PSJBLDOC</p>
<p>* WARNING, your routine has more patches than the incoming routine *</p>
<p>Routine: PSJGMRA, PSJOC, PSJOCDI</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p><u>OR*3*345:</u></p>
<p>Routine: ORCHECK, ORDSGCHK, ORKPS1</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>Routine: ORWDXR01</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p>These warnings are due to the sequence of released patches prior to MOCHA v2.0. Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/010.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
4.  Print Transport Global - this option will allow you to view the components of the KIDS build.
5.  Use the Install Package(s) option and select the package MOCHA 2.0 Combined Build 1.0.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond NO.
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.
8.  Install Example:

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME:    MOCHA 2.0 Combined Build 1.0    6/11/13@09:54

     =\> MOCHA 2.0   10/10/12  ;Created on Oct 10, 2012@15:15:20

This Distribution was loaded on Jun 11, 2013@09:54 with header of

   MOCHA 2.0 T10  10/10/12  ;Created on Oct 10, 2012@15:15:20

   It consisted of the following Install(s):

MOCHA 2.0 Combined Build 1.0    PSO\*7.0\*372    PSJ\*5.0\*252     OR\*3.0\*345

Checking Install for Package MOCHA 2.0 Combined Build 1.0

Install Questions for MOCHA 2.0 Combined Build 1.0

Checking Install for Package PSO\*7.0\*372

Install Questions for PSO\*7.0\*372

Incoming Files:

   52.4      RX VERIFY  (Partial Definition)

> **NOTE:** You already have the 'RX VERIFY' File.

Checking Install for Package PSJ\*5.0\*252

Install Questions for PSJ\*5.0\*252

Checking Install for Package OR\*3.0\*345

Install Questions for OR\*3.0\*345

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   SSH VIRTUAL TERMINAL

Install Started for MOCHA 2.0 Combined Build 1.0 :

               Jun 11, 2013@09:54:29

Build Distribution Date: Oct 10, 2012

 Installing Routines:

               Jun 11, 2013@09:54:29

 Install Started for PSO\*7.0\*372 :

               Jun 11, 2013@09:54:29

Build Distribution Date: Oct 10, 2012

 Installing Routines:

               Jun 11, 2013@09:54:30

 Installing Data Dictionaries:

               Jun 11, 2013@09:54:30

 Updating Routine file...

 Updating KIDS files...

 PSO\*7.0\*372 Installed.

               Jun 11, 2013@09:54:31

 Not a production UCI

 NO Install Message sent

 

 Install Started for PSJ\*5.0\*252 :

               Jun 11, 2013@09:54:31

Build Distribution Date: Oct 10, 2012

 Installing Routines:

               Jun 11, 2013@09:54:31

 Updating Routine file...

 Updating KIDS files...

 PSJ\*5.0\*252 Installed.

               Jun 11, 2013@09:54:32

 Not a production UCI

 NO Install Message sent

 

 Install Started for OR\*3.0\*345 :

               Jun 11, 2013@09:54:32

Build Distribution Date: Oct 10, 2012

 Installing Routines:

               Jun 11, 2013@09:54:32

 Updating Routine file...

 Updating KIDS files...

                                   OR\*3.0\*345                                  

-------------------------------------------------------------------------------

 OR\*3.0\*345 Installed.

               Jun 11, 2013@09:54:32

 Not a production UCI

 NO Install Message sent

 

 Updating Routine file...

 Updating KIDS files...

 MOCHA 2.0 Combined Build 1.0 Installed.

               Jun 11, 2013@09:54:32

 No link to PACKAGE file

 NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

# Installation of MOCHA 2.0 FOLLOW UP COMBINED BUILD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not install these bundles while Pharmacy or Adverse Reaction Tracking users are on the system or when Medication orders are being entered and signed or when allergy updates are being made through CPRS. Do not queue the installation of this bundle. Failure to heed this warning may result in 'source routine edited' errors during a database update. Edits may be lost and records may be left in an inconsistent state. An error that occurs before a cross-reference is executed, for example, may lead to corrupted data or hard errors in the future.

Installation will take no longer than five minutes. However, there is an Inpatient Medications post install routine PSJ257PO that creates new cross references for NON-VERIFIED ORDERS file (#53.1) and PHARMACY PATIENT file (#55) that could take 2-3 hours to complete. This routine will be queued during install and MAILMAN message will be sent to the installer once the process is complete.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSS\*1\*160, PSS\*1\*173 and MOCHA_2_0.KID must be installed prior to MOCHA 2.0 Follow Up Combined Build.

The Post-Init routine PSJ257PO will be queued to run in the background and will create five new cross references for use during drug interaction processing for clinic orders. Messaging will be displayed during install to indicate that the post install was queued. After completion, a MAILMAN message will be sent to the patch installer. This process could take 2-3 hours to complete depending upon the size of the site installing the patch.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><p>Post-Init routine ORY311 as part of patch OR*3.0*311 (MOCHA 2.0 FOLLOW UP Combined Build 1.0): This process will only take a few seconds to run, and then the routine is deleted from the system. After the install, running checksums on this routine will show that the routine does not exist on the system.</p>
<p>Post-Init routine PSJ257PO is part of patch PSJ*5*257 (MOCHA 2.0 FOLLOW UP Combined Build 1.0): This post install builds new cross references to facilitate the display of clinic order information during the order entry process. The cross references are also created as orders are placed. This Post-Init process can take up to three hours to run, and a mail message will be sent upon completion, but you do not have to wait for receipt of this mail message to continue with the rest of the patch installs. Additionally, users can be on the system while this post-init is running.</p></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/011.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID into your local directory.
2.  From the Kernel Installation & Distribution System (KIDS) menu, select Installation.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File: “, respond with MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID

> Example: USER\$:\[ABC\]MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID

4.  From the KIDS menu, select Installation.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2">The following are OPTIONAL - (When prompted for the INSTALL NAME, enter MOCHA 2.0 FOLLOW UP BUILD Combined Build 1.0). Refer to the note on page 3 for an explanation on the ‘before’ checksum inconsistencies with patch OR*3*311.</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/012.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as Data Dictionaries or templates.
2.  Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, data dictionaries (DD), templates, etc.).

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD you will see the following warnings on certain routines:</p>
<p>Host file: MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID contains: PSO*7*416, PSJ*5*257, GMRA*4*47, and OR*3*311</p>
<p><u>PSO*7*416:</u></p>
<p>Routine: PSOCAN, PSOCAN2, PSODDPR2, PSODDPR4, PSODDPR5, PSODDPRE, PSOORED3, PSOORED5, PSOORNEW, PSORXEDT, PSOVER1</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p><u>PSJ*5*257:</u></p>
<p>Routine: PSIVORFB</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>Routine: PSJBLDOC, PSJGMRA, PSJOC, PSJOCDI, PSJOEA2</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p><u>OR*3*311:</u></p>
<p>Routine: ORCHECK, ORDSGCHK, ORKPS1</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p>Routine: ORCMED</p>
<p>* WARNING, your routine has more patches than the incoming routine *</p>
<p>Routine: ORWDXR01</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>These warnings are due to the sequence of released patches prior to MOCHA v2.0. Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/013.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
4.  Print Transport Global - this option will allow you to view the components of the KIDS build.
5.  Use the Install Package(s) option and select the package MOCHA 2.0 FOLLOW UP Combined Build 1.0.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond "NO".
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond "YES".
1.  When prompted "Enter options you wish to mark as 'Out Of Order':", select the following option: Allergy clean up utility \[GMRA FREE TEXT UTILITY\].
2.  When prompted "Enter protocols you wish to mark as 'Out Of Order':", press Enter.
8.  If prompted "Delay Install (Minutes): (0 - 60): 0//", respond 0.
9.  Example of Install:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>Where it is shown that the background job is queued, there is a typographical error for the patch number (PSJ*5*297), which should have stated PSJ*5*257. The correct background job is queued.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/014.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: MOCHA 2.0 FOLLOW UP Combined Build 1.0 7/1/13@14:15:09

=\> MOCHA 2.0 Follow Up Combined Build ;Created on Jul 01, 2013@14:13

This Distribution was loaded on Jul 01, 2013@14:15:09 with header of

MOCHA 2.0 Follow Up Combined Build v12 ;Created on Jul 01, 2013@14:13:47

It consisted of the following Install(s):

MOCHA 2.0 FOLLOW UP Combined Build 1.0 PSJ\*5.0\*257 PSO\*7.0\*416

GMRA\*4.0\*47 OR\*3.0\*311

Checking Install for Package MOCHA 2.0 FOLLOW UP Combined Build 1.0

Install Questions for MOCHA 2.0 FOLLOW UP Combined Build 1.0

Checking Install for Package PSJ\*5.0\*257

Install Questions for PSJ\*5.0\*257

Incoming Files:

53.1 NON-VERIFIED ORDERS (Partial Definition)

> **NOTE:** You already have the 'NON-VERIFIED ORDERS' File.

53.46 CLINIC DEFINITION (Partial Definition)

> **NOTE:** You already have the 'CLINIC DEFINITION' File.

55 PHARMACY PATIENT (Partial Definition)

> **NOTE:** You already have the 'PHARMACY PATIENT' File.

Checking Install for Package PSO\*7.0\*416

Install Questions for PSO\*7.0\*416

Checking Install for Package GMRA\*4.0\*47

Install Questions for GMRA\*4.0\*47

Checking Install for Package OR\*3.0\*311

Install Questions for OR\*3.0\*311

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TERMINAL

Install Started for MOCHA 2.0 FOLLOW UP Combined Build 1.0 :

Jul 01, 2013@14:17:01

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:01

Install Started for PSJ\*5.0\*257 :

Jul 01, 2013@14:17:01

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:02

Installing Data Dictionaries: .

Jul 01, 2013@14:17:05

Running Post-Install Routine: ^PSJ257PO

=============================================================

Queuing background job for PSJ\*5\*297 Post Install...

Start time: Jul 01, 2013@14:17:05

A MailMan message will be sent to the installer upon Post

Install Completion. This may take 2-3 hours.

==============================================================

\*\*\* Task \#3364273 Queued! \*\*\*

Updating Routine file...

The following Routines were created during this install:

PSGXR3

PSGXR31

PSGXR310

PSGXR311

PSGXR312

PSGXR313

PSGXR314

PSGXR32

PSGXR33

PSGXR34

PSGXR35

PSGXR36

PSGXR37

PSGXR38

PSGXR39

PSSJXR

PSSJXR1

PSSJXR10

PSSJXR11

PSSJXR12

PSSJXR13

PSSJXR14

PSSJXR15

PSSJXR16

PSSJXR17

PSSJXR18

PSSJXR19

PSSJXR2

PSSJXR20

PSSJXR21

PSSJXR22

PSSJXR23

PSSJXR24

PSSJXR25

PSSJXR26

PSSJXR27

PSSJXR28

PSSJXR29

PSSJXR3

PSSJXR30

PSSJXR31

PSSJXR32

PSSJXR33

PSSJXR34

PSSJXR4

PSSJXR5

PSSJXR6

PSSJXR7

PSSJXR8

PSSJXR9

Updating KIDS files...

PSJ\*5.0\*257 Installed.

Jul 01, 2013@14:17:06

Not a production UCI

NO Install Message sent

Install Started for PSO\*7.0\*416 :

Jul 01, 2013@14:17:06

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:07

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*416 Installed.

Jul 01, 2013@14:17:07

Not a production UCI

NO Install Message sent

Install Started for GMRA\*4.0\*47 :

Jul 01, 2013@14:17:07

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:07

Updating Routine file...

Updating KIDS files...

GMRA\*4.0\*47 Installed.

Jul 01, 2013@14:17:07

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*311 :

Jul 01, 2013@14:17:07

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:08

Running Post-Install Routine: POST^ORY311

Setting the dosage order check to mandatory...

DONE

Updating Routine file...

Updating KIDS files...

OR\*3.0\*311

-------------------------------------------------------------------------------

OR\*3.0\*311 Installed.

Jul 01, 2013@14:17:08

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

MOCHA 2.0 FOLLOW UP Combined Build 1.0 Installed.

Jul 01, 2013@14:17:08

No link to PACKAGE file

NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

## Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Verify Post Install MAILMAN Message is Received

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation, the Inpatient Medications patch queues a post install routine (PSJ257PO) that creates new cross references for NON-VERIFIED ORDERS file (#53.1) and PHARMACY PATIENT file (#55). Depending on the size of your facility, this post install can take up to three hours to run. Upon completion the following message will be sent to the patch installer.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>In the subject line of the email, there is a typographical error for the patch number (PSJ*5*297) which should have stated PSJ*5*257. The message is otherwise correct.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/015.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Subj: Background job for PSJ\*5\*297 Post Install \[#179515\] 07/01/13@14:17

7 lines

From: INPT PHARMACY In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The new cross references for clinic orders have been created:

File 53.1 - CIMO

File 55 - CIMOU and CIMOCLU for Unit Dose Sub-file.

File 55 - CIMOI AND CIMOCLI for IV Sub-file.

The background job 3364273 began Jul 01, 2013@14:17:06 and

ended Jul 01, 2013@14:17:08.

Enter message action (in IN basket): Ignore//

# Installation of OR\*3\*381

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system, although, it is recommended that it be installed during non-peak hours to minimize potential disruption to users. Do not queue the installation of this patch. Failure to heed this warning may result in 'source routine edited' errors during a database update. Edits may be lost and records may be left in an inconsistent state. This will be installed immediately following the MOCHA v2.0 application installation.

This patch should take less than five minutes to install.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSS\*1\*160, PSS\*1\*173 and MOCHA_2_0.KID and MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID must be installed prior to installing OR\*3\*381.

## Installation Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download OR_3_381.KID into your local directory.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File: “, respond with OR_3_381.

> Example: USER\$:\[ABC\]OR_3_381.KID

4.  From the KIDS menu, select Installation.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>The following are OPTIONAL - (When prompted for the INSTALL NAME, enter OR*3.0*381).</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/016.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file OR_3_381.KID you will see the following warnings on certain routines:</p>
<p><u>OR*3*381:</u></p>
<p>Routine: ORCMED</p>
<p>* WARNING, you are missing one or more Patches *</p>
</blockquote>
<p>This warning is due to the sequence of released patches prior to MOCHA v2.0. Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-installation-guide/017.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  Print Transport Global - This option will allow you to view the components of the KIDS build.
5.  From the Installation Menu, select the Install Package(s) option and choose OR\*3.0\*381 to install.
6.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.
9.  The following is an example of install:

OR\*3\*381 T3

Select Installation \<TEST ACCOUNT\> Option: LOAD a Distribution

Enter a Host File: VA4\$:\[ANONYMOUS.ANONYMOUS\]OR_30_381_TEST_V3.KID;1

KIDS Distribution saved on Sep 30, 2013@06:34:44

Comment: OR\*3\*381 TEST V3

This Distribution contains Transport Globals for the following Package(s):

Build OR\*3.0\*381 has been loaded before, here is when:

OR\*3.0\*381 Install Completed

was loaded on Sep 20, 2013@16:48:04

OR\*3.0\*381 Install Completed

was loaded on Sep 27, 2013@16:25:14

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

OR\*3.0\*381

Use INSTALL NAME: OR\*3.0\*381 to install this Distribution.

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Installation \<TEST ACCOUNT\> Option: INStall Package(s)

Select INSTALL NAME: OR\*3.0\*381 9/30/13@11:03:08

=\> OR\*3\*381 TEST V3 ;Created on Sep 30, 2013@06:34:44

This Distribution was loaded on Sep 30, 2013@11:03:08 with header of

OR\*3\*381 TEST V3 ;Created on Sep 30, 2013@06:34:44

It consisted of the following Install(s):

OR\*3.0\*381

Checking Install for Package OR\*3.0\*381

Install Questions for OR\*3.0\*381

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TERMINAL

OR\*3.0\*381

--------------------------------------------------------------------------------

Install Started for OR\*3.0\*381 :

Sep 30, 2013@11:03:46

Build Distribution Date: Sep 30, 2013

Installing Routines:

Sep 30, 2013@11:03:46

Updating Routine file...

Updating KIDS files...

OR\*3.0\*381 Installed.

Sep 30, 2013@11:03:46

Not a production UCI

NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Installation \<TEST ACCOUNT\> Option:

# Installation of MOCHA 2.0 FAST TRACK BUILDS 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not install this patch while Inpatient Pharmacy users are on the system or when Inpatient orders are being entered and signed through CPRS.

Do not install this patch while Outpatient Pharmacy users are on the system, during CMOP processing, or when orders are being entered and signed through CPRS.

This patch should be installed after OR\*3\*381 patch, this should take less than five minutes to install.

| Note:                                             | After install of this patch, the 2nd line of PSJLIACT routine will not contain patch number 257, and 257 will be re-added with patch PSJ\*5\*296. |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-2-installation-guide/018.png) |                                                                                                                                                   |

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be installed after the MOCHA v2.0 and OR\*3\*381 patches, this should take less than five minutes to install.

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download MOCHA_2_0_FAST_TRACK_BUILDS.KID into your local directory.
2.  From the Kernel Installation & Distribution System (KIDS) menu, select Installation.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File: “, respond with MOCHA_2_0_FAST_TRACK_BUILDS.KID.

> Example: USER\$:\[ABC\]MOCHA_2_0_FAST_TRACK_BUILDS.KID

4.  From the KIDS menu, select Installation.
1.  Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as Data Dictionaries or templates.
2.  Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, data dictionaries (DD), templates, etc.).

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file MOCHA_2_0_FAST_TRACK_BUILDS you will see the following warnings on certain routines:</p>
<p>Host file: MOCHA_2_0_FAST_TRACK_BUILDS.KID contains: PSO*7*431, PSJ*5*299</p>
<p><u>PSJ*5*299:</u></p>
<p>Routine: PSIVORFB</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p>Routine: PSJLIACT</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>These warnings are due to the sequence of released patches prior to MOCHA v2.0.  Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th>![](mocha-version-2-installation-guide/019.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
4.  Print Transport Global - this option will allow you to view the components of the KIDS build.
5.  Use the Install Package(s) option and select the package MOCHA 2.0 FAST TRACK Builds 1.0.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond "NO".
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond "NO".
8.  If prompted "Delay Install (Minutes): (0 - 60): 0//", respond 0.
9.  The following is an example of install:

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME:    MOCHA 2.0 FAST TRACK BUILDS 1.0    2/12/14@15:40:50

     =\> MOCHA 2.0 FAST TRACK BUILDS V4  ;Created on Feb 12, 2014@15:39:13

This Distribution was loaded on Feb 12, 2014@15:40:50 with header of

   MOCHA 2.0 FAST TRACK BUILDS V4  ;Created on Feb 12, 2014@15:39:13

   It consisted of the following Install(s):

MOCHA 2.0 FAST TRACK BUILDS 1.0    PSJ\*5.0\*299    PSO\*7.0\*431

Checking Install for Package MOCHA 2.0 FAST TRACK BUILDS 1.0

Install Questions for MOCHA 2.0 FAST TRACK BUILDS 1.0

Checking Install for Package PSJ\*5.0\*299

Install Questions for PSJ\*5.0\*299

Checking Install for Package PSO\*7.0\*431

Install Questions for PSO\*7.0\*431

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   SSH VIRTUAL TERMINAL

Install Started for MOCHA 2.0 FAST TRACK BUILDS 1.0 :

               Feb 12, 2014@15:42:16

Build Distribution Date: Feb 12, 2014

 Installing Routines:

               Feb 12, 2014@15:42:16

 Install Started for PSJ\*5.0\*299 :

               Feb 12, 2014@15:42:16

Build Distribution Date: Feb 12, 2014

 Installing Routines:

               Feb 12, 2014@15:42:16

 Running Post-Install Routine: ^PSJ299PO

=============================================================

Queuing background job for PSJ\*5\*299 Post Install...

Start time: Feb 12, 2014@15:42:16

A MailMan message will be sent to the installer upon Post

Install Completion.  This may take 2-3 hours.

==============================================================

\*\*\* Task \#12305 Queued! \*\*\*

\*\*\* Task \#12305 Queued! \*\*\*

 Updating Routine file...

 Updating KIDS files...

 PSJ\*5.0\*299 Installed.

               Feb 12, 2014@15:42:16

 Not a production UCI

 NO Install Message sent

 

 Install Started for PSO\*7.0\*431 :

               Feb 12, 2014@15:42:16

Build Distribution Date: Feb 12, 2014

 Installing Routines:

               Feb 12, 2014@15:42:16

 Updating Routine file...

 Updating KIDS files...

PSO\*7.0\*431

--------------------------------------------------------------------------------

 PSO\*7.0\*431 Installed.

               Feb 12, 2014@15:42:16

 Not a production UCI

 NO Install Message sent

 

 Updating Routine file...

 Updating KIDS files...

 MOCHA 2.0 FAST TRACK BUILDS 1.0 Installed.

               Feb 12, 2014@15:42:16

 No link to PACKAGE file

NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

# Verify Dosing Checks are Enabled

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log onto VistA and navigate to Patient Prescription Processing option.
2.  Select a Test Patient and place an order where the dosage will exceed the maximum daily dose.
3.  Navigate to the Inpatient Order Entry option and place an order where the dosage will exceed the maximum daily dose.
4.  The following is an example of the order check if 120 milligrams are ordered for Simvastatin.

SIMVASTATIN 40MG TAB: Single dose amount of 120 MILLIGRAMS exceeds the

maximum single dose amount of 80 MILLIGRAMS.

Do you want to Continue? Y//

If the dosing checks are not displayed, please log a Remedy ticket.

1.  <span id="_Toc287867276" class="anchor"></span>Appendix: Acronyms

| Term  | Definition                                                      |
|-------|-----------------------------------------------------------------|
| ADPAC | Automated Data Processing Application Coordinator               |
| CPRS  | Computerized Patient Record System                              |
| DD    | Data Dictionaries                                               |
| FDB   | First Databank                                                  |
| FTP   | File Transfer Protocol                                          |
| HWSC  | Heath*<u>e</u>*Vet Web Services Client                          |
| IRMS  | Information Resources Management Service                        |
| KIDS  | Kernel Installation and Distribution System                     |
| MOCHA | Medication Order Check Healthcare Application                   |
| MUMPS | Massachusetts General Hospital Utility Multi-Programming System |
| NDF   | National Drug File                                              |
| PDM   | Pharmacy Data Management                                        |
| PECS  | Pharmacy Enterprise Customization System                        |
| PEPS  | Pharmacy Enterprise Product System                              |
| PMI   | Patient Medication Information                                  |
| VA    | Department of Veterans Affairs                                  |
| VDL   | VA Software Document Library                                    |
| VISTA | Veterans Health Information Systems and Technology Architecture |