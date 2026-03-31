---
title: PSB*3*83 Clinical Ancillary Services (CAS) Inpatient Medication Administration - Transdermal Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Clinical Ancillary Services (CAS) Inpatient Medication Administration - Transdermal
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*83
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - install
  - patch
  - installation
  - table
  - contents
  - bcma
  - pssjxr
  - installing
  - transport
  - global
page_count: 0
word_count: 6164
section_count: 21
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2016
revision_count: 8
revision_newest: 12/6/16
revision_oldest: 11/12/15
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p83_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p83_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

Clinical Ancillary Services (CAS)Development – Delivery of Pharmacy Enhancements (DDPE)

Inpatient Medication Administration - Transdermal

Installation Guide

![](psb-3-83-clinical-ancillary-services-cas-inpatient-medication-administration-tra/001.png)

December 2016

Revision History

| Date     | Version | Description                                                               | Author                             |
|----------|---------|---------------------------------------------------------------------------|------------------------------------|
| 12/6/16  | 0.8     | Added updated Backout steps for PSB\*3\*83 and PSB\*3\*87.                | <span class="mark">REDACTED</span> |
| 07/29/16 | 0.7     | Accepted track changes and added install instructions for OR\*3\*417.     | <span class="mark">REDACTED</span> |
| 03/10/16 | 0.6     | Multiple modifications for content and appearance/clarification purposes. | <span class="mark">REDACTED</span> |
| 03/03/16 | 0.5     | Updated one roll back step                                                | <span class="mark">REDACTED</span> |
| 03/03/16 | 0.4     | Updating install routine sections                                         | <span class="mark">REDACTED</span> |
| 03/02/16 | 0.3     | More major modifications to content and TOC                               | <span class="mark">REDACTED</span> |
| 01/13/16 | 0.2     | Some more modifications                                                   | <span class="mark">REDACTED</span> |
| 11/12/15 | 0.1     | Initial draft.                                                            | <span class="mark">REDACTED</span> |

Revision History includes date of changes, version number, description of changes, and author of revisions.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [System Requirements](#system-requirements)
  - [Pre-Installation](#pre-installation)
  - [Patch Installations](#patch-installations)
    - [Installation Instructions Overview](#installation-instructions-overview)
    - [Installing PSS\1\191](#installing-pss1191)
    - [Installing PSJ\5\315](#installing-psj5315)
    - [Installing PSB\3\83](#installing-psb383)
    - [Installing OR\3\417](#installing-or3417)
    - [Installing PSB\3\87 (BCBU)](#installing-psb387-bcbu)
  - [Download and Extract Procedure](#download-and-extract-procedure)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Implementation](#implementation)
- [Backout Procedure](#backout-procedure)
  - [Backout Strategy](#backout-strategy)
  - [Backout Considerations](#backout-considerations)
  - [User Acceptance Testing](#user-acceptance-testing)
  - [Backout Criteria](#backout-criteria)
  - [Authority for Backout](#authority-for-backout)
  - [Automated Backout Steps](#automated-backout-steps)
  - [Manual Backout Steps for PSB\3\83 and PSB\3\87](#manual-backout-steps-for-psb383-and-psb387)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
This document provides installation instructions for Clinical Ancillary Services (CAS) Development Delivery of Pharmacy enhancements (DDPE) Inpatient Medications Administration – Transdermal patches.

# System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the software elements for Inpatient Medications.

Inpatient Medication Software Elements

| Application                        | Version |
|----------------------------------------|-------------|
| Adverse Reaction Tracking              | 4.0         |
| Decision Support System                | 3.0         |
| Inpatient Medications                  | 5.0         |
| Kernel                                 | 8.0         |
| Laboratory                             | 5.2         |
| Mailman                                | 8.0         |
| National Drug File                     | 4.0         |
| Nursing                                | 4.0         |
| Order Entry/Results Reporting          | 3.0         |
| Outpatient Pharmacy                    | 7.0         |
| Patient Information Management Systems | 5.3         |
| Pharmacy Data Management               | 1.0         |
| RPC Broker (32-bit)                    | 1.1         |
| Toolkit                                | 7.3         |
| VA FileMan                             | 22.0        |

## Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The associated patches are the following and should be installed in the following order:

- PSS\*1\*191
- PSJ\*5\*315
- PSB\*3\*83
- OR\*3\*417
- PSB\*3\*87 (BCBU)

\*\*\*  WARNING FOR ALL SITES CURRENTLY USING WMA  \*\*\*

                  (Wireless Medication Administration)

                            From CareFusion

The below 15 VAMC sites should not install patch PSB\*3\*83 until the site has confirmed they have received CareFusion's software update:

Pyxis Med Administration Verification VA v. 5.1

 

<span class="mark">REDACTED</span>

Installation of BCMA Patch PSB\*3.0\*83 may cause your WMA application to stop functioning as you would expect it to. In order for the WMA devices to work properly with PSB\*3.0\*83 installed, you must contact CareFusion, the WMA vendor, to obtain the most current version of the WMA software.

## Patch Installations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of this project, as defined by the PWS, is as follows:

1.  The Clinical Ancillary Services Development – Delivery of Pharmacy Enhancements (CAS DDPE) Inpatient Medications Administration – Transdermal project provides a solution to address the errors in transdermal medication administration processes that have led to adverse patient events. The following features related to transdermal medications are needed by the business to avert these errors in the future by implementing the following capabilities within Inpatient Medications Administration/VistA:
    1.  Create a mechanism to remind the user to “follow-up” on certain medications requiring additional steps in administration or assessment, e.g., alert the user to remove a transdermal medication at a specified time.
    2.  Ensure previous statuses of multi-step medications appear in the Medication Administration History reports, e.g., the date and time a transdermal medication was applied or an intravenous fluid marked ‘infusing’ will remain visible after it has been marked ‘removed’ or ‘completed’, respectively.
    3.  Enhance the current mechanism used to document and display the anatomic location of injectable medications to support transdermal medications. Implementation includes changing the terminology of “Injection site” throughout the applications including Inpatient Medication Administration and VistA. Any field names used to store or refer to “location” data within VistA shall be evaluated as to whether or not the terminology needs to be changed. For example, if the field in VistA is named “IV Location,” the name of the field is changed to simply “Location” so that when data from the field are pulled into reports, the field name will adequately reflect the updated contents.
    4.  A change to any order involving a transdermal medication forces a misleading “remove patch” alert to appear. The Contractor shall change the software to differentiate between a change and a discontinued order and display an appropriate, corresponding alert.

### Installation Instructions Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ATTENTION \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Clinical Ancillary Services (CAS) Development-Delivery of Pharmacy

Enhancements (DDPE) VA Inpatient Medication Administration - Transdermal

enhancement includes 5 patches, which must be installed in the following

order:

1.  PSS\*1\*191
2.  PSJ\*5\*315
3.  PSB\*3\*83
4.  OR\*3\*417
5.  PSB\*3\*87

ATTENTION: This enhancement also includes a new Graphical User Interface (GUI) executable, BCMA GUI PSB3_P083.EXE. Installation of this GUI is required immediately after the KIDS install for the Patch to function.

For retrieval and installation instructions, please see the [Client Installation Instructions](#Client_Install) section.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

### Installing PSS\*1\*191

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software being released as a host file and/or documentation describing the new functionality introduced by this patch are available, as follows.

The preferred method is to retrieve files from <span class="mark">REDACTED</span> . This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

<span class="mark">REDACTED</span>

The following documentation should be available at these sites:

PHARMACY DATA MANAGEMENT RELEASE NOTES

pss_1_p191_rn.pdf Binary

PHARMACY DATA MANAGEMENT TECHNICAL MANUAL/SECURITY GUIDE

pss_1_tm_r0316_Inpatient_Medications_Transdermal.pdf Binary

PHARMACY DATA MANAGEMENT USER MANUAL

pss_1_um_r0316_Inpatient_Medications_Transdermal\_.pdf Binary

Patch Installation:Pre/Post-Installation Overview:

A post-installation routine PSS1P191 will run with this install and will be automatically deleted after installation. A second post-installation routine PSSP191A may be deleted after install, but will not delete automatically.

Pre-Installation Instructions:

This patch may be installed with users on the system, although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

Installation Instructions:

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME, enter the patch

PSS\*1.0\*191:

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4.  From the Installation Menu, select the Install Package(s) option and

choose patch PSS\*1.0\*191 to install.

5.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of

Install? NO//,” Respond Yes

6.  When prompted “Want KIDS to INHIBIT LOGONs during the install?

NO//,” Respond No

7.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//,” Respond No

Post-Installation Instructions

Check installing users email account. The post-install routine PSS1P191 will provide a list of Orderable Items that were updated during this process. This message will also be sent to all users holding the PSJI MGR and PSJU MGR keys. The update will note which Orderable Items with a Dosage Form that contains the word "PATCH" will be updated to a Prompt For Removal in BCMA value of 1 in order to preserve legacy behavior. The routine PSS1P191 will

be deleted after installation.

The post-install via routine PSSP191A will also provide a list of orders tied to users holding the keys PSJ RPH and PSJU RPHARM in addition to the MGR keys. These Orderable Items indicate the approximate number of orders that will eventually need to be discontinued and

re-created when the PSJ\*5.0\*315 patch is finally installed. No action should be taken on these orders until patch PSJ\*5.0\*315 is installed.

Another version of this report will be available on the Pharmacy Data Management \[PSS MGR\] menu. The routine PSSP191A should be deleted after the install. The recommendation is to edit the Orderable Items for Medications that Require Removal and set the appropriate value for the

field Prompt for Removal in BCMA (#12). The new report installed on the Orderable Item Management \[PSS ORDERABLE ITEM MANAGEMENT\] menu will aid this process. Once this is done, a more accurate representation will be available of the number and type of orders that will need to be addressed upon install of PSJ\*5.0\*315.

Example of PSS\*1\*191 Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: PSS\*1.0\*191 12/1/15@10:54:33

=\> PSS\*1\*191 TEST

This Distribution was loaded on Dec 01, 2015@10:54:33 with header of

PSS\*1\*191 TEST

It consisted of the following Install(s):

PSS\*1.0\*191

Checking Install for Package PSS\*1.0\*191

Install Questions for PSS\*1.0\*191

Incoming Files:

50.7 PHARMACY ORDERABLE ITEM (Partial Definition)

> **NOTE:** You already have the 'PHARMACY ORDERABLE ITEM' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999 SSH VIRTUAL TERMINAL

--------------------------------------------------------------------------------

Install Started for PSS\*1.0\*191 :

Dec 01, 2015@10:56:06

Build Distribution Date: Nov 23, 2015

Installing Routines:

Dec 01, 2015@10:56:06

Installing Data Dictionaries:

Dec 01, 2015@10:56:06

Installing PACKAGE COMPONENTS:

Installing OPTION

Dec 01, 2015@10:56:06

Running Post-Install Routine: ^PSS1P191

=============================================================

Queuing background job for PSS\*1\*191 Post Install Diagnostic Report...

Start time: Dec 01, 2015@10:56:08

A MailMan message will be sent to the installer upon Post

Install Completion. This may take an hour.

==============================================================

\*\*\* Task \#8953082 Queued! \*\*\*

Updating Routine file...

Updating KIDS files...

PSS\*1.0\*191 Installed.

Dec 01, 2015@10:56:08

Not a production UCI

NO Install Message sent

Call MENU rebuild

Starting Menu Rebuild: Dec 01, 2015@10:56:10

Collecting primary menus in the New Person file...

Primary menus found in the New Person file

------------------------------------------

OPTION NAME MENU TEXT \# OF LAST LAST

USERS USED BUILT

XMUSER MailMan Menu 9 10/24/97 12/01/15

EVE Systems Manager Menu 214 11/30/15 12/01/15

PSO MANAGER Outpatient Pharmacy Manager 2 08/18/15 12/01/15

PSO USER1 Pharmacist Menu 1 12/01/15

PSO USER2 Pharmacy Technician's Menu 3 07/26/96 12/01/15

PSO SUPERVISOR Supervisor Functions 1 12/01/15

DGMGR MAS MANAGER 1 12/11/96 12/01/15

PSJU MGR Unit Dose Medications 2 05/03/05 12/01/15

NURS-SYS-MGR Nursing System Manager's ... 1 11/18/98 12/01/15

NURS-ADM Administrator's Menu 2 12/01/15

NURS-HN Head Nurse's Menu 1 11/30/90 12/01/15

LRLIASON Lab liaison menu 1 09/15/92 12/01/15

LRMENU Laboratory DHCP Menu 2 12/11/97 12/01/15

LRWARDM Ward lab menu 1 05/06/99 12/01/15

YSUSER Mental Health 2 10/07/97 12/01/15

RA TECHMENU Rad/Nuc Med Technologist ... 1 10/16/90 12/01/15

MCARCATH Cath Lab Menu 1 12/01/15

RT OVERALL Record Tracking Total Sys... 2 05/25/94 12/01/15

ZZWARD LAB/PHARM USER

WARD LAB/PHARMACY USER 1 07/18/94 12/01/15

FBAA MAIN MENU Fee Basis Main Menu 5 09/19/94 12/01/15

A3FSMBMGR FSMB RD Menu 1 12/01/15

ZZCPTEST CASTLE POINT PSO ACTION P... 1 08/11/89 12/01/15

SROMENU Surgery Menu 15 10/22/15 12/01/15

ORMGR CPRS Manager Menu 2 12/28/98 12/01/15

DVBA REGIONAL OFFICE MENU

A.M.I.E Regional Office M... 1 10/30/95 12/01/15

DVBA MASTER MENU AMIE MASTER MENU 1 12/01/15

GECO GECS MAIN MENU Miscellaneous Code Sheet ... 1 11/29/90 12/01/15

OE/RR MASTER MENU OE/RR MASTER MENU 1 05/03/95 12/01/15

PHARMACY MASTER MENUPHARMACY MASTER MENU 1 10/16/15 12/01/15

IB MANAGER MENU Integrated Billing Master... 1 12/01/15

OR MAIN MENU NURSE Nurse Menu 1 02/23/99 12/01/15

OR MAIN MENU WARD CLERK

Ward Clerk Menu 3 02/26/99 12/01/15

OR MAIN MENU CLINICIAN

Clinician Menu 5 08/05/05 12/01/15

ARZ MASTER Accounts Receivable Maste... 2 10/26/95 12/01/15

VAQ (MENU) MAIN Patient Data Exchange 1 12/22/95 12/01/15

PRSA EMP MENU Employee Menu 1 04/07/94 12/01/15

ZZCLIMAP Clinical Applications Mai... 7 11/08/05 12/01/15

ESP POLICE CHIEF MENU

Police Chief 1 07/15/94 12/01/15

ZCLIN2MISC2 Discharge Summary/Problem... 1 10/23/95 12/01/15

ZCLINMAP1 CLINICAL 1 APPLICATIONS 1 09/08/97 12/01/15

EEO COUNSELORS MENU Counselor's Menu 1 08/21/95 12/01/15

PLW MAIN MENU PLW MAIN MENU 1 03/19/96 12/01/15

ZZ TRAINING MENU Training Menu 30 08/29/96 12/01/15

TIU MAIN MENU MRT Text Integration Utilitie... 2 02/07/95 12/01/15

TIU MAIN MENU MGR Text Integration Utilitie... 1 11/01/94 12/01/15

TIU MAIN MENU TRANSCRIPTION

Text Integration Utilitie... 1 09/11/96 12/01/15

TIU MAIN MENU REMOTE USER

Text Integration Utilitie... 1 02/27/95 12/01/15

TIU MAIN MENU PN CLINICIAN

Progress Notes User Menu 1 12/01/15

TIU MAIN MENU CLINICIAN

Progress Notes/Discharge ... 1 03/11/94 12/01/15

TIU IRM MAINTENANCE MENU

TIU Maintenance Menu 1 12/01/15 12/01/15

Building secondary menu trees....

Merging.... done.

Install Completed

Example Mailman Messages Sent by Pre/post-Install Routine to Certain Keyholders:First mail message sent:

Subj: PHARMACY ORDERABLE ITEM MANAGEMENT \[#169339\] 12/01/15@10:56 15 lines

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The following Orderable Items have the Dosage Form Patch and

the Prompt for Removal in BCMA field was updated to a value

of 1 by Patch PSS\*1\*191

ORDERABLE ITEM INACTIVE DISPENSE DRUG

NAME - DOSAGE FORM DATE NAME IEN

------------------------------ ------------ ------------------------- ------

NICOTINE - PATCH NONE NICOTINE PAD 42

NITROGLYCERIN - PATCH NONE NITROGLYCERIN PATCHES 10M 2313

NITROGLYCERIN PATCHES 15M 5029

NITROGLYCERIN PATCHES 5MG 3785

NITROGLYCERIN 0.6MG S.L.T. - P NONE NITROGLYCERIN 0.6MG S.L.T 247

Enter message action (in IN basket): Ignore//

Second mail message sent:

Subj: PHARMACY ORDERABLE ITEM MANAGEMENT \[#169340\] 12/01/15@10:56 14 lines

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Active Orders for Medications Requiring Removal (MRR).

Prior to Installation of PSJ\*5\*315 these orders should be

reviewed for planning purposes, but no action taken.

Once PSJ\*5\*315 is installed they will need to be Discontinued

and re-entered after coordinating with your Pharmacy ADPAC.

This report can be recalled from the PSS MGR Menu.

Sorted by Patient within Ward

Pat Patient Orderable Ordr MRR

ID Loc Item Name Sts Val

----- -------------------- -------------------- ---- ---

B5555 7A GEN MED NICOTINE PAD A 1

Total Orders found: 1

Enter message action (in IN basket): Ignore//

### Installing PSJ\*5\*315

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software being released as a host file and/or documentation describing the new functionality introduced by this patch are available as follows. The preferred method is to retrieve files from <span class="mark">REDACTED</span>. This transmits the files from the first available server. Sites may

also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

<span class="mark">REDACTED</span>

The following documentation should be available at these sites:

INPATIENT MEDICATIONS NURSE'S USER MANUAL

psj_5_nurse_um_r0416.pdf Binary

INPATIENT MEDICATIONS PHARMACIST'S USER MANUAL

psj_5_phar_um_r0416.pdf Binary

INPATIENT MEDICATIONS TECHNICAL MANUAL/ SECURITY GUIDE

psj_5_tm_r0416.pdf Binary

Patch Installation:Pre/Post-Installation Overview:

A post-installation routine PSJ15P315 will run with this install and will be automatically deleted after installation.

Pre-Installation Instructions:

This patch may be installed with users on the system, although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than five minutes to install. Patch PSS\*1.0\*191 is required to install this patch.

Installation Instructions:

1.  Choose the PackMan message containing this patch PSJ\*5.0\*315.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter the patch

PSJ\*5.0\*315:

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4.  From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5.  When prompted “Want KIDS to INHIBIT LOGONs during the install?

NO//,” respond Yes

6.  When prompted “Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//,” respond No

Post-Installation Instructions:

Post-install routine QUE^PSJ5P315 checks for active MRR orders generated for Inpatient Medications and creates a report. This report will show orders that have been created for Orderable items with the "Prompt for removal in BCMA" value set to 1 or greater, but do not have the new File 55 fields containing removal information. <u>This indicates that the orders are legacy orders and must be cancelled and re-ordered after the install of PSJ\*5\*315</u>. This process is needed because, although the BCMA GUI application can display legacy orders as well as the new format, the combination of both displaying simultaneously on the same patient may cause confusion and should be avoided.

This report will be sent to all Pharmacists holding the keys PSJ RPH and PSJU RPHARM as well as the PSS MGR keys and can also be called manually from the PSS MGR menu using the "Orders for MRRs With Removal Properties" option.

Example of PSJ\*5\*315 Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: PSJ\*5.0\*315 1/8/16@10:41:56

=\> PSJ\*5\*315 TEST

This Distribution was loaded on Jan 08, 2016@10:41:56 with header of

PSJ\*5\*315 TEST

It consisted of the following Install(s):

PSJ\*5.0\*315

Checking Install for Package PSJ\*5.0\*315

Install Questions for PSJ\*5.0\*315

Incoming Files:

53.1 NON-VERIFIED ORDERS (Partial Definition)

> **NOTE:** You already have the 'NON-VERIFIED ORDERS' File.

55 PHARMACY PATIENT (Partial Definition)

> **NOTE:** You already have the 'PHARMACY PATIENT' File.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999 SSH VIRTUAL TERMINAL

----------------------------------------------------------------------------

Install Started for PSJ\*5.0\*315 :

Jan 08, 2016@10:43:57

Build Distribution Date: Jan 05, 2016

Installing Routines:

Jan 08, 2016@10:43:58

Running Pre-Install Routine: QUE^PSJ5P315

=============================================================

Queuing background job for PSJ\*5\*315 Pre Install Diagnostic Report...

Start time: Jan 08, 2016@10:43:58

A MailMan message will be sent to the installer upon Post

Install Completion. This may take an hour.

==============================================================

\*\*\* Task \#213887 Queued! \*\*\*

Installing Data Dictionaries: ..

Jan 08, 2016@10:44

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Jan 08, 2016@10:44

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

PSJ\*5.0\*315 Installed.

Jan 08, 2016@10:44:01

Not a production UCI

Install Completed

Example Mailman Messages Sent by Pre/post-Install Routine to Certain Keyholders:Mail message sent:

Subj: Pharmacy Data Management \[#170758\] 03/02/16@14:55 12 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Orders for Medications Requiring Removal (MRR) ACTIVE PRIOR to

Installation of PSJ\*5\*315. These orders will need to be Discontinued

and re-entered after coordinating with your Pharmacy ADPAC.

This report can be recalled from the PSS MGR Menu.

Sorted by Patient within Ward

Pat Patient Orderable Ordr MRR

ID Loc Item Name Sts Val

----- -------------------- -------------------- ---- ---

Total Orders found: 0

Enter message action (in IN basket): Ignore//

### Installing PSB\*3\*83

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software being released and/or documentation that describes the new functionality introduced by this patch are available from the below sites.

The preferred method is to retrieve files from <span class="mark">REDACTED</span>.

This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

<span class="mark">REDACTED</span>

Patch Installation:Pre-Installation Instructions:

\*\*IMPORTANT\*\* Inpatient menu options listed in the Installation Instructions section should be exited by all users prior to the install of the patches listed at the top of this Patch Description. Also, these menu options should be disabled during these installs.

This patch may be installed with users on the system, although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

Installation Instructions:

<span id="Client_Install" class="anchor"></span><u>Client Installation Instructions:</u>

The software distribution includes these modified files:

FILE NAME DESCRIPTION FILE VERSION BYTES FTP MODE

----------- ---------------------- ------------ -------- --------

BCMA.CHM Client help file 1,192 KB binary

BCMA.EXE Client 3.0.83.42 3,112 KB binary

BCMAPar.CHM Parameters Client help 376 KB binary

BCMApar.EXE Parameters Client 3.0.83.13 1,676 KB binary

1\. Prior client compatible with patch: NO

2\. Client can be copied instead of installed: YES

3\. Is your site running the CareFusion Wireless Medication

Administration (WMA) software? If YES, please contact CareFusion to

ensure your site has the latest compatible WMA patch.

If BCMA is currently running, please exit BCMA. This client installation patch file can be used to upgrade an existing version of BCMA, or can be used for a brand new installation.

1.  Double Click on PSB3_0P83.EXE, which will launch the InstallShield

Wizard.

2.  When the “InstallShield Wizard Welcome” screen is displayed, click

"Next".

3.  On the “Choose Destination Location” screen, simply click "Next"
4.  If you would like to change the destination folder to one other than default, click "Browse" to navigate to the folder of your choice. Click "Next".
5.  On the "Setup Type" screen, select one of the following options:
    1.  Typical - installs only the BCMA client program,

> which is necessary for medication administration.

2.  Complete - installs the BCMA client and the

> GUI BCMA site parameters definition program.

3.  Custom - allows you to select which programs to install.

> Typical is selected by default. Click "Next."

6.  The “InstallShield Wizard Ready to Install the Program” screen will display. Click "Install" to proceed with the installation.
7.  The “InstallShield Wizard Complete” screen will be displayed.
8.  Click "Finish" and the BCMA installation is now complete.

<u>VistA Patch Install Instructions</u>

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter PSB\*3.0\*83.

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

1.  From the Installation Menu, select the Install Package(s) option and enter the patch PSB\*3.0\*83.
2.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//," respond NO.
3.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//," respond NO.
4.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//," respond YES.
5.  Disable the below menu option:
    1.  PSJ OE.
6.  If prompted "Delay Install (Minutes): (0 - 60): 0//," respond 0.

Post-Installation Instructions:\*\*Important\*\*

Before running BCMA in a division, the user should run BCMA Site Parameters program.  Specifically:

- Start BCMA Parameters client
- Menu File \| Open
- Select Division
- The program will silently load the body chart background image to VistA for this Division. This image will be used by BCMA when the user is in the Dermal Site Needed / Injection Site Needed window and clicks Select from Body Diagram.

After these steps are completed, the user can run BCMA in that division.

Example of PSB\*3\*83 MUMPS Patch Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: PSB\*3.0\*83 3/2/16@17:01:48

=\> PSB\*3\*83 TEST

This Distribution was loaded on Mar 02, 2016@17:01:48 with header of

PSB\*3\*83 TEST

It consisted of the following Install(s):

PSB\*3.0\*83

Checking Install for Package PSB\*3.0\*83

Install Questions for PSB\*3.0\*83

Incoming Files:

53.78 BCMA MEDICATION VARIANCE LOG (Partial Definition)

> **NOTE:** You already have the 'BCMA MEDICATION VARIANCE LOG' File.

53.79 BCMA MEDICATION LOG (Partial Definition)

> **NOTE:** You already have the 'BCMA MEDICATION LOG' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TERMINAL

-----------------------------------------------------------------------------

Install Started for PSB\*3.0\*83 :

Mar 02, 2016@17:03:25

Build Distribution Date: Mar 02, 2016

Installing Routines:

Mar 02, 2016@17:03:26

Installing Data Dictionaries:

Mar 02, 2016@17:03:26

Installing PACKAGE COMPONENTS:

Installing FORM

Installing REMOTE PROCEDURE

Installing OPTION

Installing PARAMETER DEFINITION

Installing PARAMETER TEMPLATE

Mar 02, 2016@17:03:27

Running Post-Install Routine: EN^PSB3P83

Updating Routine file...

Updating KIDS files...

PSB\*3.0\*83 Installed.

Mar 02, 2016@17:03:27

Install Completed

### Installing OR\*3\*417

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The change made by OR\*3\*417 is in support of requirements for patch PSB\*3.0\*83. All the patches in this group should be installed prior to patch OR\*3.0\*417.

The change will add a line to the Order Details report and the Medication Administration History Report in the Computerized Patient Record System (CPRS). These reports will display the Removal times for Medications that Require Removal (MRRs).

Documentation and Software Retrieval Instructions:

Updated documentation describing the new functionality and installation

instructions introduced by this patch are available.

Files can be obtained from the ANONYMOUS.SOFTWARE directory at one of the

OI Field Offices. The preferred method is to retrieve the file using Secure File Transfer Protocol (SFTP) from <span class="mark">REDACTED</span>, which will transmit the file from the first available server. Alternatively, sites may elect to retrieve the file from a specific OI Field Office.

OI FIELD OFFICE FTP ADDRESS DIRECTORY

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library

at: http://www4.va.gov/vdl/

Patch Installation:Pre/Post Installation Overview:Pre-Installation Instructions:

This patch may be installed with users on the system, although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install. Patches PSS\*1.0\*191, PSJ\*5.0\*315 and PSB\*3.0\*83 should all be

installed in listed order prior to install of OR\*3.0\*417. Patch PSB\*3.0\*87 is an optional patch for Barcode Medication Administration Backup sites.

Installation Instructions:

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the patch OR\*3.0\*417:
    1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  If prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", Respond "No"
6.  If prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//", Respond "No"
7.  If prompted "Delay Install (Minutes): (0 - 60): 0//", Respond "0"

Post-Installation Instructions:

There are no installation routines with this patch. No further action

required.

Routine Information:

The second line of each of these routines now looks like:

;;3.0;ORDER ENTRY/RESULTS REPORTING;\*\*\[Patch List\]\*\*;Dec 17, 1997;Build 10

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: ORQ21

Before: B35534512 After: B37800373 \*\*141,190,195,215,243,361,350,417\*\*

Routine list of preceding patches: 350

### Installing PSB\*3\*87 (BCBU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software being released as a host file introduced by this patch is available from the below sites.

The preferred method is to retrieve files from <span class="mark">REDACTED</span>. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices when patch is released.

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

The KIDS build is distributed by the host file named:

PSB_3_87.KID

Patch Installation:Pre-Installation Instructions:Installation Instructions:

Do not queue this patch to install at a later time nor install this patch while BCMA users are on the system. Installation will take no longer than five minutes.

Suggested time to install: non-peak requirement hours.

1.  From the Kernel Installation & Distribution System menu, select

the LOAD DISTRIBUTION option and load the host file PSB_3_87.KID

2.  From the Kernel Installation & Distribution System Menu, select the

INSTALLATION Menu. From this menu, you may elect to use the following

options. When prompted for the INSTALL NAME, enter PSB\*3\*87.

a\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

b\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

c\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this

patch is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

d\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

3.  Use the Install Package(s) option and select the package PSB\*3.0\*87.
4.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion

of Install? NO//,” respond NO.

5.  When Prompted "Want KIDS to INHIBIT LOGONs during the install?

NO//," respond NO.

6.  When Prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//," respond NO.

Post-Installation Instructions

It is recommended that the backup system workstations be re-initialized after the install of this patch. It is also recommended to limit the number of workstations being initialized to no more than 4 at a time, so as to limit the impact to your network’s speed.

Use one of the below VistA menu options, depending on your Site’s configuration, for the BCMA Backup System.

Select OPTION NAME: PSB BCBU VISTA MAIN BCMA Backup System (VISTA)

PSB BCBU VISTA MAIN BCMA Backup System (VISTA)

DFT Default Workstation Initialize

DIV Divisional Workstation Initialize

USR Initialize a Backup Workstation with BCMA Users

## Download and Extract Procedure

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

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation steps and procedures were described above by installing the patches in the order referenced and following each patches specific installation instructions.

<u>Important reminders:</u>

The post install mailman messages sent by patch PSS\*1\*191 point to Orderable items that need file maintenance prior to implementing the full functionality of this project.

The post install mailman message sent by PSJ \*5\*315 post install also lists Orders that need to be re-entered to work correctly with the new functionality in BCMA Client.

# Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backout pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Backout Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 4.6.

## Backout Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing is in progress.

## Backout Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The project is canceled and the implemented features are no longer wanted by the stakeholders.

## Authority for Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority would come from the IPT and the VA project manager.

## Automated Backout Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The normal recommended process for backout is an automated process to enforce section 4.4 Backout Criteria requirements.

In the event that a backout of code was needed for all Transdermal patches, a patch would be developed to remove all components added by patches PSS\*1\*191 , PSJ\*5\*315, PSB\*3\*83 and PSB\*3\*87. This patch would restore existing routines to their prior state.

The following components would be backed out by the new patch:

Menu Options:

Option Name                      Type               New/Modified/Deleted

Orderable Item Management

\[PSS ORDERABLE ITEM MANAGEMENT\]   Menu                     Modified

Orderable Items that Require  
Removal Report \[PSS MRR

ORDERABLE ITEMS RPT\]              Rout                     New

Orderable Items Report for High

Risk\High Alert \[PSS HR/HA

ORDERABLE ITEMS RPT\]              Rout                     New

Pharmacy Data Management

\[PSS MGR\]                         Menu                     Modified

Orders for MRRs With Removal

Properties \[PSS MRR ORDERS

DIAGNOSTIC RPT\]                   Rout                     New

Files & Fields Associated: 

File Name (#)                    Field Name (#)       New/Modified/Deleted

ORDERABLE ITEM (#50.7) PROMPT FOR REMOVAL IN BCMA (#12) New

NON-VERIFIED ORDERS(#53.1) DURATION OF ADMINISTRATION (#137) New

NON-VERIFIED ORDERS(#53.1) REMOVE TIMES (#138) New

NON-VERIFIED ORDERS(#53.1) REMOVE PERIOD (#139) New

NON-VERIFIED ORDERS(#53.1) BCMA PROMPT FOR REMOVAL FLAG (#140) New

PHARMACY PATIENT(#55)

UNIT DOSE(#62) DURATION OF ADMINISTRATION (#137) New

PHARMACY PATIENT(#55)

UNIT DOSE(#62) REMOVE TIMES (#138) New

PATIENT PHARMACY(#55)

> UNIT DOSE(#62) REMOVE PERIOD (#139) New

PHARMACY PATIENT(#55)

UNIT DOSE(#62) BCMA PROMPT FOR REMOVAL FLAG (#140) New

BCMA MEDICATION LOG (53.79) SCHEDULED REMOVAL TIME (.17) New

DERMAL SITE (.18) New

ACTION DATE/TIME (.06) Mod

SCHEDULED ADMINISTRATION TIME (.13) Mod

Subfile:

DISPENSE DRUG (53.795) PROMPT FOR REMOVAL IN BCMA (.06) New

BCMA MEDICATION VARIANCE LOG EVENT(.05) Mod

(53.78)

Add a new code to the set

of codes for the EVENT field: 4:EARLY/LATE REMOVE New

BCMA BACKUP DATA (#53.7) ORDER NUMBER (#9) Modified

ORDER NUMBER (#53.702) REMOVE TIMING (#7.4) New

DURATION OF ADMINISTRATION (#7.5) New

MED LOG DATE/TIME ASSOC. MED LOG GIVE DATE/TIME (#4) New

(#53.70213) ASSOC. MED LOG GIVE ENTERED BY (#5) New

ASSOC. MED LOG GIVE STATUS MSG (#6) New 

Remote Procedure Calls Associated:

RPC Name New/Modified/Deleted

PSB COVERSHEET1 Modified

PSB GETINJECTIONSITE Modified

PSB GETORDERTAB Modified

PSB GETSETWP New

PSB MED LOG LOOKUP Modified

PSB TRANSACTION Modified

PSB VALIDATE ORDER Modified

Parameters Associated:

Parameter Name New/Modified/Deleted

PSB AL GROUPS New

PSB AL IMAGE GENERAL New

PSB AL IMAGES New

PSB AL MASTER LIST New

PSB LIST ANATOMIC LOCATIONS New

PSB LIST BODY SITES New

Templates Associated:

Template Name Type File Name (Number) New/Modified/Deleted

PSB DIVISION Kernel PARAMETER TEMPLATE (#8989.52) Modified

## Manual Backout Steps for PSB\*3\*83 and PSB\*3\*87

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Class 3 GUI software (Pyxis Med Administration Verification VA v. 5.1) updates are not available at National Release for PSB\*3\*83 and PSB\*3\*87 and if sites running Wireless Medication Administration (WMA) software inadvertently install PSB\*3\*83 and PSB\*3\*87, please follow the steps in the below process documents:

> **NOTE:** in the .pdf version of this document, click the attachments icon (paperclip) at the top left of the navigation pane in Adobe Reader to view these attachments.

![](psb-3-83-clinical-ancillary-services-cas-inpatient-medication-administration-tra/002.png)![](psb-3-83-clinical-ancillary-services-cas-inpatient-medication-administration-tra/003.png)

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data and elements other than routines.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A follow-up patch for each namespace would be needed to delete/modify that namespace’s data dictionary entries that were added/modified and other non-routine components added/modified by this projects patches and would follow the basic logic flow below.

<u>Logic flow using FileMan API calls as much as possible for the below actions</u>

1.  New data fields would need to be erased that were likely populated by the new functionality, while the new data fields are still valid in the data dictionary.
2.  New file cross references would now need to be deleted.
3.  New fields need to be deleted out of the data dictionary.
4.  Modified data dictionary fields would need to be restored.
5.  Existing REMOTE PROCEDURE file (#8994) entries would need to be restored while new file entries would need to be deleted from the site.
6.  Existing PROTOCOL file (#101) entries would need to be restored while new file entries would be deleted from the site.
7.  Existing OPTION file (#19) entries would need to be restored while new file entries would be deleted from the site.
8.  Existing PARAMETERS file (#8989.5) entries would need to be restored while new file entries would be erased and then deleted from the Kernel Parameter Definition file at the site.
9.  Existing PARAMETER DEFINITION file (#8989.51) entries would need to be restored while new file entries would be erased and then deleted from the PARAMETER DEFINITION file at the site.
10. Existing PARAMETER TEMPLATE file (#8989.52) entries would need to be restored.

> **NOTE:** These new data entries are the result of a new field added to the data dictionary or the modification of an existing field in the data dictionary.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <u>back-out</u> of INPATIENT MEDICATION ADMINISTRATION - TRANSDERMAL patches that modified existing fields, and established new fields would be justification for rollback.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority would come from the IPT and the VA project manager.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 5.1.