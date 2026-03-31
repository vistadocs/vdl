---
title: MOCHA Version 2 Combined Builds Enhancements 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Combined Builds Enhancements 2
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 2
patch_id: PSO*2
group_key: "PSO:PSO:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - install
  - table
  - contents
  - installation
  - order
  - mocha
  - rollback
  - patch
  - routines
  - build
page_count: 0
word_count: 3347
section_count: 11
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/pss_1_psj_5_pso_7_mocha_e2_cb_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/pss_1_psj_5_pso_7_mocha_e2_cb_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

> ![](mocha-version-2-combined-builds-enhancements-2-installation-guide/001.png)

Medication Order Check Healthcare Application(MOCHA) Enhancements 2Combined Build 1.0Installation Guide(Rollback Plan)

GMRA\*4\*46, OR\*3\*269, PSJ\*5\*281 and PSO\*7\*411  
(MOCHA Enhancements 2 Combined Build 1.0)

PSS\*1\*175 (Stand Alone)

April 2016

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
- [Important: Recently released patch GMRA\4\48 contains an Allergy](#important-recently-released-patch-gmra448-contains-an-allergy)
- [Installation Considerations/Restrictions](#installation-considerationsrestrictions)
- [Installation Order](#installation-order)
- [Rollback Preparation](#rollback-preparation)
- [Installation of PSS\1\175](#installation-of-pss1175)
  - [Installation Steps](#installation-steps)
    - [Install Example:](#install-example)
- [Installation of MOCHAENH2GMRAORPSJPSO.KID](#installation-of-mochaenh2gmraorpsjpsokid)
  - [Pre-Installation Instructions](#pre-installation-instructions)
  - [Installation Steps](#installation-steps-1)
    - [Install Example:](#install-example-1)
  - [Routine Deletions](#routine-deletions)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Requirements](#rollback-requirements)
    - [Software Required for Rollback](#software-required-for-rollback)
    - [Overview of Rollback Build](#overview-of-rollback-build)
  - [Rollback Considerations/Restrictions](#rollback-considerationsrestrictions)
  - [Rollback Steps](#rollback-steps)
- [Appendix: Acronyms](#appendix-acronyms)
Medication Order Check Healthcare Application (MOCHA) Enhancements (Enh) 2 provides additional functionality for the existing MOCHA 1.0 drug interaction and duplicate therapy enhanced order check functionality. In addition, modifications have been made for Clinical Reminder Order Checks (CROC) and allergy functionality.
The following patches make up the release of MOCHA Enh 2:
<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 12%" />
<col style="width: 52%" />
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
<td><strong>PSS_1_175.KID</strong></td>
<td>Host File</td>
<td>MOCHA UFT ENHANCEMENTS 2 PSS - Pharmacy Data Management patch PSS*1*175</td>
</tr>
<tr class="even">
<td><strong>MOCHA_ENH_2_GMRA_OR_PSJ_PSO.KID</strong></td>
<td>Host File</td>
<td><p>MOCHA UFT ENHANCEMENTS 2 combined build that contains the following patches:</p>
<ul>
<li><blockquote>
<p>GMRA*4*46 - Adverse Reaction Tracking patch</p>
</blockquote></li>
<li><blockquote>
<p>OR*3*269 - Computerized Patient Record System(CPRS) patch</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>PSJ*5*281 - Inpatient Medications patch</p>
</blockquote></li>
<li><blockquote>
<p>PSO*7*411 - Outpatient Pharmacy patch</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide installation steps for MOCHA Enhancements 2. The intended audience for this document is the Information Resources Management Service (IRMS) staff responsible for installing these patches.

# Pre-Requisite Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No pre-requisite considerations.

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
- GMRA\*4\*10
- GMRA\*4\*44
- OR\*3\*286
- OR\*3\*306
- OR\*3\*311
- OR\*3\*346
- OR\*3\*352
- OR\*3\*395
- PSJ\*5\*160
- PSJ\*5\*199
- PSJ\*5\*278
- PSJ\*5\*286
- PSJ\*5\*299
- PSJ\*5\*305
- PSJ\*5\*309
- PSJ\*5\*320
- PSO\*7\*294
- PSO\*7\*313
- PSO\*7\*372
- PSO\*7\*390
- PSO\*7\*416
- PSO\*7\*429
- PSO\*7\*436
- PSO\*7\*438
- PSS\*1\*169

# Important: Recently released patch GMRA\*4\*48 contains an Allergy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assessment Clean Up utility tool that produces a report that identifies

discrepancies between the ADVERSE REACTION ASSESSMENT file (#120.86) and

the PATIENT ALLERGIES file (#120.8). It is imperative that GMRA\*4\*48 be

installed prior to the installation of these MOCHA Enhancements 2 patches,

and that all data discrepancies identified by GMRA\*4\*48 have been

corrected. If not, then installing the MOCHA Enhancements 2 patches

may result in drug allergy order checks not displaying in CPRS and pharmacy during

the medication order entry processes.

# Installation Considerations/Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches should be installed when Pharmacy applications are not in use, no other pharmacy patches are being installed and when tasked jobs from Clinical Applications are not running.

Installation should also occur when CPRS usage is at a minimum, particularly medication activities and when allergy data is not being entered or edited in CPRS.

The length of time for the install is dependent upon the number of entries in the ORDER CHECK INSTANCES (#100.05) file that will be converted and could range from five to thirty minutes.

Do not queue the installation of this patch.

Failure to heed this warning may result in 'source routine edited' errors during a database update. Edits may be lost and records may be left in an inconsistent state.

# Installation Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Enh 2 patches should be installed in the following order and should be installed consecutively together. Please review individual patch install information in the following sections for pre and post installation instructions.

1.  PSS_1_175.KID – HOST file with patch name:

> PSS\*1.0\*175

2.  MOCHA_ENH_2_GMRA_OR_PSJ_PSO.KID – HOST file with patch name:

> MOCHA Enh 2 COMBINED BUILD 1.0

# Rollback Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure for these patches should only occur when there is concurrence from the Enterprise Product Support and MOCHA development teams, because of the complexity and risk involved in a rollback. Normal installation back-ups using KIDS will back up only Mumps routines. For all non-routine components of these builds, Enterprise Product Support will have a build available if needed. Make sure the ‘Backup a Transport Global’ step in sections 6 and 7 of this document is followed, so you do have a backup of all the routines if needed.

If your site has any local modifications to any of the following non-routine components of the builds, they will need to be backed up locally. Please contact Enterprise Product Support prior to installing if there are questions.

- ORDER CHECK INSTANCES (#100.05) File Data Dictionary
- PSJ DISPLAY DRUG ALLERGIES Protocol

# Installation of PSS\*1\*175

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download PSS_1_175.KID into your local directory.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File:”, respond with PSS_1_175.KID.

> Example: USER\$:\[ABC\]PSS_1_175.KID

4.  From this menu, you may then select to use the following options:

| Note:                                             | The following are OPTIONAL - (When prompted for the INSTALL NAME, enter PSS\*1.0\*175). |
|---------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](mocha-version-2-combined-builds-enhancements-2-installation-guide/002.png) |                                                                                         |

- Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global - This option will allow you to view the components of the KIDS build.
- Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
5.  Select the installation option Backup a Transport Global. This option will create a backup message of any routines exported with this patch in case you need to backout this patch. It will not backup any other changes such as Data Dictionaries (DD’s) or templates. It is important this step be followed, because if backout of this patch is necessary, having this backup will make the process much easier.
6.  Select the Installation option Install Package(s). This is the step to start the installation of this KIDS patch:
1.  Choose the Install Package(s) option to start the patch install and enter PSS\*1.0\*175 at the INSTALL NAME prompt.
2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO.

### Install Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

> Select INSTALL NAME: PSS\*1.0\*175 5/20/14@15:13:40

> =\> PSS\*1\*175

> This Distribution was loaded on May 20, 2014@15:13:40 with header of

> PSS\*1\*175

> It consisted of the following Install(s):

> PSS\*1.0\*175

> Checking Install for Package PSS\*1.0\*175

> Install Questions for PSS\*1.0\*175

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// SSH VIRTUAL TERMINAL

> PSS\*1.0\*175

> Install Started for PSS\*1.0\*175 :

> May 20, 2014@15:26:49

> Build Distribution Date: May 20, 2014

> Installing Routines:

> May 20, 2014@15:26:49

> Updating Routine file...

> Updating KIDS files...

> PSS\*1.0\*175 Installed.

> May 20, 2014@15:26:50

> Not a production UCI

> NO Install Message sent

> Install Completed

# Installation of MOCHA_ENH_2_GMRA_OR_PSJ_PSO.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSS\*1.0\*175 must have been successfully installed prior to installation of this host file.

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download MOCHA_ENH_2_GMRA_OR_PSJ_PSO.KID into your local directory.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File:”, respond with MOCHA_ENH_2_GMRA_OR_PSJ_PSO.KID.

> Example: USER\$:\[ABC\]MOCHA_ENH_2_GMRA_OR_PSJ_PSO.KID

4.  From this menu, you may then select to use the following options:

| Note:                                             | The following are OPTIONAL - (When prompted for the INSTALL NAME, enter MOCHA ENH 2 COMBINED BUILD 1.0). |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![](mocha-version-2-combined-builds-enhancements-2-installation-guide/003.png) |                                                                                                          |

- Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global - This option will allow you to view the components of the KIDS build.
- Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
5.  Select the installation option Backup a Transport Global. This option will create a backup message of any routines exported with this patch in case you need to backout this patch. It will not backup any other changes such as Data Dictionaries (DD’s) or templates. It is important this step be followed, because if backout of this patch is necessary, having this backup will make the process much easier.
6.  Select the Installation option Install Package(s). This is the step to start the installation of this KIDS patch:
    1.  Choose the Install Package(s) option to start the patch install and enter MOCHA ENH 2 COMBINED BUILD 1.0 at the INSTALL NAME prompt.
    2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
    3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
    4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer YES.
    5.  When prompted ‘Enter options you wish to mark as 'Out Of Order':’ answer GMRA PATIENT A/AR EDIT.
    6.  When prompted ‘Enter protocols you wish to mark as 'Out Of Order':’ press the Enter key.
    7.  When prompted ‘Delay Install (Minutes): (0-60): 0//’ press the Enter key.

        Please note that because the installation process of this build will run the CPRS Order Check routine complier, the patch installer will receive a VistA mail message similar to this mail message indicating the Order Check compiler has run to completion:

Subj: Order Check Compiler Status  \[#77714\] 03/24/16@15:23  14 lines

From: POSTMASTER  In 'IN' basket.   Page 1

---------------------------------------------------------------------------

The Order Check routine compiler has completed normally

on MAR 24,2016 at 15:23 by \[nnnnnn\]  INSTALLER,PATCH.

ORDER CHECK EXPERT version 1.01 released OCT 29,1998

                    Elapsed time: 0 minutes 7 seconds

                            Automatic Mode

           Execution Trace Mode: OFF

      Elapsed time Logging Mode: 

           Raw Data Logging Mode: OFF

         Lines of code generated: No longer tracked

### Install Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME:    MOCHA ENH 2 COMBINED BUILD 1.0    8/11/15@15:05:30

     =\> MOCHA ENH 2 COMBINED BUILD (8.11.15)  ;Created on Aug 11, 2015@14:

This Distribution was loaded on Aug 11, 2015@15:05:30 with header of

   MOCHA ENH 2 COMBINED BUILD (8.11.15)  ;Created on Aug 11, 2015@14:14:04

   It consisted of the following Install(s):

MOCHA ENH 2 COMBINED BUILD 1.0    GMRA\*4.0\*46     OR\*3.0\*269    PSJ\*5.0\*281

    PSO\*7.0\*411

Checking Install for Package MOCHA ENH 2 COMBINED BUILD 1.0

Install Questions for MOCHA ENH 2 COMBINED BUILD 1.0

Checking Install for Package GMRA\*4.0\*46

Install Questions for GMRA\*4.0\*46

Checking Install for Package OR\*3.0\*269

Install Questions for OR\*3.0\*269

Incoming Files:

   100.05    ORDER CHECK INSTANCES

> **NOTE:** You already have the 'ORDER CHECK INSTANCES' File.

Checking Install for Package PSJ\*5.0\*281

Install Questions for PSJ\*5.0\*281

Checking Install for Package PSO\*7.0\*411

Install Questions for PSO\*7.0\*411

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// YES

Enter options you wish to mark as 'Out Of Order': GMRA PATIENT A/AR EDIT E

nter/Edit Patient Reaction Data

Enter options you wish to mark as 'Out Of Order':

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;99999  HOME  (CRT)

--------------------------------------------------------------------------------

 Install Started for MOCHA ENH 2 COMBINED BUILD 1.0 :

               Aug 11, 2015@15:07:15

Build Distribution Date: Aug 11, 2015

 Installing Routines:

               Aug 11, 2015@15:07:15

 Install Started for GMRA\*4.0\*46 :

               Aug 11, 2015@15:07:15

Build Distribution Date: Aug 11, 2015

 Installing Routines:

               Aug 11, 2015@15:07:15

 Running Post-Install Routine: POST^GMRAY46

 Updating Routine file...

 Updating KIDS files...

 GMRA\*4.0\*46 Installed.

               Aug 11, 2015@15:07:15

 Not a production UCI

 NO Install Message sent

 

 Install Started for OR\*3.0\*269 :

               Aug 11, 2015@15:07:15

Build Distribution Date: Aug 11, 2015

 Installing Routines:

               Aug 11, 2015@15:07:15

 Running Pre-Install Routine: PRE^ORY269

Deleting existing ORDER CHECK INSTANCES data dictionary while preserving data...

DONE

 Installing Data Dictionaries:

               Aug 11, 2015@15:07:15

 Running Post-Install Routine: POST^ORY269 .

Order Check Expert System Rule Transporter

Created: JUL 26,2013 at 06:56  at  CPRS30.FO-SLC.MED.VA.GOV

Current Date: AUG 11,2015 at 15:07  at  CHEYL37.FO-BAYPINES.MED.VA.GOV

Loading Data  . . . . .

  Installing '863.8  OCX MDD PARAMETER' records...  . . . . . . . . . .

. . . . . . . .

  Installing '864.1  OCX MDD DATATYPE' records...  . .

  Installing '863.4  OCX MDD ATTRIBUTE' records...  . . . .

  Installing '863.2  OCX MDD SUBJECT' records...  .

  Installing '863.3  OCX MDD LINK' records...  . . . . .

  Installing '860.9  ORDER CHECK NATIONAL TERM' records...  . . . . . .

. . . . . . . . .

  Installing '860.8  ORDER CHECK COMPILER FUNCTIONS' records...  . . . .

. . . . . . . .

  Installing '860.6  ORDER CHECK DATA CONTEXT' records...  . . .

  Installing '860.5  ORDER CHECK DATA SOURCE' records...  . . .

  Installing '860.4  ORDER CHECK DATA FIELD' records...  .

      No data filing errors.

Transport Finished...

---Creating Order Check Routines-----------------------------------

Build list of Active Rules, Elements and Datafields...

     96 DATA FIELDS

     81 ELEMENTS

     39 RULES

Compile DataField Navigation code...

    101 DataField Navigation Code Arrays

Compile Element Evaluation code...

     75 Event Evaluation Code Arrays

Compile Element MetaCode...

     81 Element Metacode Arrays

Get Compiler Function Code...

     51 Compiler Include Functions

Compile Rule Element Relation code...

     56 Rule Element Relation Code Arrays

Construct Decision Tree...

    716 Sub-Routines

Optimize Sub-Routines...

    287 Sub-Routines

  60% Optimization

Assemble Routines...

     39 OCXOZ\* Routines

Converting existing data in the ORDER CHECK INSTANCES file...

DONE

 Updating Routine file...

 Updating KIDS files...

 OR\*3.0\*269 Installed.

               Aug 11, 2015@15:07:26

 Not a production UCI

 NO Install Message sent

 

 Install Started for PSJ\*5.0\*281 :

               Aug 11, 2015@15:07:26

Build Distribution Date: Aug 11, 2015

 Installing Routines:

               Aug 11, 2015@15:07:26

 Installing PACKAGE COMPONENTS:

 

 Installing PROTOCOL

               Aug 11, 2015@15:07:26

 Updating Routine file...

 Updating KIDS files...

 PSJ\*5.0\*281 Installed.

               Aug 11, 2015@15:07:26

 Not a production UCI

 NO Install Message sent

 

 Install Started for PSO\*7.0\*411 :

               Aug 11, 2015@15:07:26

Build Distribution Date: Aug 11, 2015

 Installing Routines:

               Aug 11, 2015@15:07:26

 Running Post-Install Routine: ADDCR^PSOCROC

 Updating Routine file...

 Updating KIDS files...

 PSO\*7.0\*411 Installed.

               Aug 11, 2015@15:07:26

 Not a production UCI

 NO Install Message sent

 

 Updating Routine file...

 Updating KIDS files...

 MOCHA ENH 2 COMBINED BUILD 1.0 Installed.

               Aug 11, 2015@15:07:26

 No link to PACKAGE file

Install Completed

## Routine Deletions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the patch is successfully installed, KIDS will automatically delete

the main post-install routine ORY269. Sites may safely delete the

following remaining post-install routines using the Delete Routines

\[XTRDEL\] option:

ORY2690

ORY26901

ORY26902

ORY26903

ORY26904

ORY26905

ORY2691

ORY2692

ORY2693

ORY2694

ORY269ES

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This last section of the document is only needed if there are major problems resulting from the installation of these patches, and there is concurrence from the Enterprise Product Support and MOCHA Development Teams that a rollback must occur.

If you are a CMOP (Consolidated Mail Outpatient Pharmacy), and the only build you installed was the PSS\*1.0\*175 build, all you will need to do is restore your routine backup made of that install. Then you can delete the routines PSSCKOS and PSSDIUTX, which were new with PSS\*1.0\*175, and you are done.

If a rollback occurs, entries created in the ORDER CHECK INSTANCES file (#100.05) while ME2 (MOCHA Enhancements 2) was installed are retained. However, data in fields that are new with ME2 is lost and unrecoverable.

The CLINICAL REMINDER entry that was added to the APSP INTERVENTION TYPE file (#9009032.3) in the PSO\*7.0\*411 Post-Init routine will remain in the file.

## Rollback Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the requirements for rollback.

### Software Required for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Make sure you have the following software available for the rollback:

1.  Routine backup from PSS\*1.0\*175 Install
2.  Routine backup from MOCHA_ENH_2_GMRA_OR_PSJ_PSO install
3.  MOCHA \_ENH_2_ROLLBACK.KID Host File
4.  (Local) Your local backups of the ORDER CHECK INSTANCES (#100.05) File Data Dictionary and the PSJ DISPLAY DRUG ALLERGIES Protocol from Section 5, if a backup was made for local modifications.

> \*\*\*Note – The MOCHA \_ENH \_2_ROLLBACK.KID build is available from Enterprise Product Support upon request. Enterprise Product Support can also supply the routine backups if needed.

### Overview of Rollback Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MOCHA_ENH_2_ROLLBACK combined build is made up of the following single builds:

1.  ORZ\*3.0\*269
- Requires OR\*3.0\*352, OR\*3.0\*306, OR\*3.0\*311, OR\*3.0\*346, OR\*3.0\*286, GMRA\*4.0\*46, OR\*3.0\*395
- ORDER CHECK INSTANCES (#100.05) File Data Dictionary restores the data dictionary for the ORDER CHECK INSTANCES file (#100.05) back to its pre-OR\*3\*269 state.
- Converts existing data in the ORDER CHECK INSTANCES file (#100.05) into a pre-OR\*3\*269 format. Data in new fields is deleted.
- Restores the ALLERGY - CONTRAST MEDIA REACTION order check back to its pre-OR\*3\*269 state.
- ORY269 conversion routines that will be deleted after patch installation
- Instruction provided in section 8.6 of this guide on other routines to delete
2.  PSJZ\*5.0\*281
- Requires PSJ\*5.0\*281
- PSJ DISPLAY DRUG ALLERGIES Protocol to restore the Protocol without the EXIT ACTION Field data.
- Deletes the following routines that were new with the Mocha Enhancements 2 install:
  - PSJCROC
  - PSJNEWOA
  - PSJNEWOC
3.  PSOZ\*7.0\*411
- Requires PSO\*7.0\*411
- Deletes the following routines that were new with the Mocha Enhancements 2 install:
  - PSOCROC
  - PSODGAL3
  - PSONEWOA
  - PSONEWOC
  - PSOOCKV1
4.  PSSZ\*1.0\*175
- Requires PSS\*1.0\*175
- Deletes the following routines that were new with the PSS\*1.0\*175 install:
  - PSSCKOS
  - PSSDIUTX

## Rollback Considerations/Restrictions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback should occur when Pharmacy applications are not in use, no other pharmacy patches are being installed and when tasked jobs from Clinical Applications are not running.

Rollback should also occur when CPRS usage is at a minimum, particularly Pharmacy activities. Rollback should occur when allergy data is not being entered or edited in CPRS.

The length of time for the rollback is dependent upon the number of entries in the ORDER CHECK INSTANCES (#100.05) file that will be converted and could range from five to thirty minutes.

Do not queue any of the rollback process.

Failure to heed this warning may result in 'source routine edited' errors during a database update. Edits may be lost and records may be left in an inconsistent state.

## Rollback Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Restore the routine backup from the patch PSS\*1.0\*175 install.
2.  Restore the routine backup from the MOCHA_ENH_2_GMRA_OR_PSJ_PSO install.

> \*\*\*Note - if for some reason the MOCHA_ENH_2_GMRA_OR_PSJ_PSO build was installed multiple times, make sure you restore the back up from the first install.

3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File:”, respond with MOCHA \_ENH_2 \_ROLLBACK.KID.

> Example: USER\$:\[ABC\]MOCHA \_ENH_2 \_ROLLBACK.KID

4.  From this menu, you may then select to use the following options:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><blockquote>
<p>The following are OPTIONAL - (When prompted for the INSTALL NAME, enter MOCHA_ENH_2_ROLLBACK 1.0).</p>
</blockquote></th>
</tr>
<tr class="odd">
<th>![](mocha-version-2-combined-builds-enhancements-2-installation-guide/004.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global - This option will allow you to view the components of the KIDS build.
- Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
- Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
5.  Select the Installation option Install Package(s). This is the step to start the installation of this KIDS patch:
    1.  Choose the Install Package(s) option to start the patch install and enter MOCHA_ENH_2_ROLLBACK 1.0 at the INSTALL NAME prompt.
    2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
    3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
    4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer YES.
    5.  When prompted ‘Enter options you wish to mark as 'Out Of Order':’ answer GMRA PATIENT A/AR EDIT.
    6.  When prompted ‘Enter protocols you wish to mark as 'Out Of Order':’ press the Enter key.
    7.  When prompted ‘Delay Install (Minutes): (0-60): 0//’ press the Enter key.
6.  Local Modifications (If Applicable):

> Install your local backups of the ORDER CHECK INSTANCES (#100.05) File Data Dictionary and the PSJ DISPLAY DRUG ALLERGIES Protocol from Section 5, if a backup was made.

> If either of the 2 routine backups (PSS\*1.0\*175 or MOCHA_ENH_2_GMRA_OR_PSJ_PSO) had to be retrieved from Enterprise Product Support, any local modifications can now be re-entered.

7.  Patch Installation Tracking:

> The site will need to work with the Enterprise Product Support and MOCHA Development Teams to make the necessary changes to the PACKAGE (#9.4) File to accurately reflect the current state of the account in regards to the patches installed.

> The MOCHA Development Team will provide instructions for this step to Enterprise Product Support in the ‘ME2 Rollback - Update Patch Application Tracking’ document.

8.  Routine Deletions:

> After the patch is successfully installed, KIDS will automatically delete the main post-install routine ORY269. Sites may safely delete the following remaining post-install routines using the Delete Routines \[XTRDEL\] option:

> ORY2690

> ORY26901

> ORY26902

> ORY26903

> ORY26904

> ORY26905

> ORY26906

> ORY26907

> ORY2691

> ORY2692

> ORY2693

> ORY2694

> ORY269ES

> Note: If the Kernel parameter XPD NO_EPP_DELETE is set to 1 in the account, the routines ORY269, ORZY269, ORZY269E and GMRAY46 will *not* be deleted by KIDS during the installation. For purposes of rollback however; they can be deleted using this option.

# Appendix: Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term  | Definition                                                      |
|-------|-----------------------------------------------------------------|
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