---
title: TMP VistA Patch 859 DIBRG
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: TMP
app_name: Telehealth Management Platform
section: CLI
app_status: active
pkg_ns: TMP
patch_ver: 5.3
patch_id: TMP*5.3*859
group_key: "TMP:TMP:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: The Deployment, Installation, Back-Out and Rollback Guide defines the ordered, technical steps required to install the product, back out the installation (if necessary), and roll back to the previously installed version of the product. It provides installation instructions for the SD\5.3\859 patch
audience: 
keywords: 
  - table
  - contents
  - back
  - installation
  - patch
  - install
  - rollback
  - procedure
  - routine
  - stop
page_count: 0
word_count: 2366
section_count: 25
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2023
revision_count: 1
revision_newest: 9/27/2023
revision_oldest: 9/27/2023
docx_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/sd_5_3_859_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/sd_5_3_859_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=231"
---

Scheduling Package EnhancementPatch SD\*5.3\*859

Deployment, Installation, Back-Out, and Rollback Guide

![](tmp-vista-patch-859-dibrg/001.png)

October 2023

Office of Information and Technology (OI&T)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Artifact Rationale](#artifact-rationale)
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [System Requirements](#system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
- [Installation Procedure](#installation-procedure)
  - [Installation from the Patch Description](#installation-from-the-patch-description)
- [Implementation Procedure](#implementation-procedure)
  - [Post-Install Routine (No Action Required)](#post-install-routine-no-action-required)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
- [Additional Information](#additional-information)
  - [Documentation](#documentation)
| Date      | Version | Description            | Author |
|-----------|---------|------------------------|--------|
| 9/27/2023 | 1.0.0   | Initial Document Draft |        |
Table showing the Revision History.

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the Deployment, Installation, Back-Out, and Rollback Guide for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.
# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Deployment, Installation, Back-Out and Rollback Guide defines the ordered, technical steps required to install the product, back out the installation (if necessary), and roll back to the previously installed version of the product. It provides installation instructions for the SD\*5.3\*859 patch

## Purpose 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Guide is to provide installation steps for the SD\*5.3\*859 patch. The intended audience for this document is the Information Resource Management Systems (IRMS) staff. Some of the main features of this patch are the following:

1.  Perform Stop Code maintenance in Scheduling in accordance with the MCAU FY24 (October 2023) updates. These changes need to be moved into the SD TELE HEALTH STOP CODE File (#40.6)
2.  Fixes an error that occurs intermittently when using Clinic Inquiry.
3.  Fixes \<UNDEFINED\>SCH+20^SDHL7APU error that occurs when a new appointment is made in TMP.
4.  Prevents Default Provider Update from updating clinics that should not be updated.
5.  Updates the logic on the 'Provider Add/Edit' and the 'Default Provider Bulk Update' options to prevent a user from editing Provider information if the associated clinic is currently inactive.
6.  The TMP application is sending the cancelation reason to VistA, but VistA is not receiving it properly. Updated several routines to make sure it is received and recorded on the VistA appointment.
7.  Modified TMP to stop the defining of the PARENT variable for TMP appointments, which causes VSE to treat the appointment as though it originated from an MRTC.
8.  Create a post-install cleanup routine to find the corrupted Data from the previous item and erase the PARENT REQUEST field. The post-install will generate a Mailman message and send to the installer with the results of the corrected appointments.
9.  When sending a Cancel Appointment to VistA from TMP, the Cancel Reason field was null which caused an undefined error. Modified to send back a Negative acknowledgement error text to TMP and quit gracefully.

## Dependencies 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Constraints 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Package                   | Minimum Version Needed |
|-------------------------------|----------------------------|
| VA FileMan                    | 22.0                       |
| Kernel                        | 8.0                        |
| MailMan                       | 8.0                        |
| Health Level 7                | 1.6                        |
| Order Entry/Results Reporting | 3.0                        |
| CMOP                          | 2.0                        |
| NDF                           | 4.0                        |
| Outpatient Pharmacy           | 7.0                        |
| Pharmacy Data Management      | 1.0                        |
| Controlled Substances         | 3.0                        |
| Toolkit                       | 7.3                        |
| Drug Accountability           | 3.0                        |

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

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation from the Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name (ex. SD\*5.3\*859).
2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup, the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
1.  At the Installation option menu, select Backup a Transport Global.
2.  At the Select INSTALL NAME prompt, enter your build SD\*5.3\*859.
3.  When prompted for the following, enter “R” for Routines or “B” for Build.

> Select one of the following:

> B Build

> R Routines

> Enter response: Build

4.  When prompted “Do you wish to secure your build? NO//”, press \<enter\> and take the default response of “NO”.
5.  When prompted with, “Send mail to: Last Name, First Name”, press \<enter\> to take the default recipient. Add any additional recipients.
6.  When prompted with “Select basket to send to: IN//”, press \<enter\> and take the default IN mailbox or select a different mailbox.
3.  You may also elect to use the following options:
1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
1.  When Prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//" respond NO.
2.  When Prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond NO.
3.  When Prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.
4.  If prompted 'Delay Install (Minutes): (0-60): 0//' respond 0.

# Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Post-Install Routine (No Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post-install routine SD53P859 adds the newly updated stop codes 129 and 569 to the SD TELE HEALTH STOP CODE FILE (#40.6). It also removes stop codes 290, 291, 292, 293, 296, 297 and 573 from the SD TELE HEALTH STOP CODE FILE (#40.6)

The post-install routine will also cleanup entries in the SDEC APPT REQUEST file (#409.85). A mailman message will be sent to the installer by this post install and this message would need to be forwarded to the schedulers for their awareness of the corrected Appointment Request file entries that are associated with appointments.

The post-install MailMan message lists patient appointment date/times that had an associated Appt Request file entry that was corrupted and blocking TMP canceling these appointments. These appointments are no longer blocked and can now be canceled in TMP if necessary.

Example Post Install Mail Message:

Subj: SD TMP cleanup of MRTC parent field in SDEC APPT REQUEST file

\#409.85

\[#300084\] 07/03/23@11:37 15 lines

From: PATCH,INSTALLER In 'IN' basket. Page 1

-------------------------------------------------------------------------

Patient appointment date/times that were fixed, can now be cancelled via

VSE.

Appt Request CID records that were fixed have no associated appointment

made.

Patient: C1539 Appt: May 17, 2023@14:30 has been fixed.

Patient: C1539 Appt: May 31, 2023@11:45 has been fixed.

Patient: C1539 Appt: Jun 30, 2023@10:00 has been fixed.

Patient: C1539 Appt: Jul 05, 2023@10:00 has been fixed.

Patient: C1539 Appt: Jul 07, 2023@11:00 has been fixed.

Patient: C1539 Req CID: May 11, 2023 has been fixed.

Patient: C1539 Req CID: May 11, 2023 has been fixed.

Patient: C1539 Appt: Jul 11, 2023@10:15 has been fixed.

Patient: C1539 Req CID: Jul 18, 2023 has been fixed.

Patient: C1539 Appt: Jul 19, 2023@10:00 has been fixed.

Patient: C1539 Appt: Jul 21, 2023@10:00 has been fixed.

Patient: C1539 Appt: Jul 25, 2023@10:30 has been fixed.

Enter message action (in IN basket): Ignore//

No manual intervention is necessary.

You may delete the post-install routine SD53P850 if the installation was successful and the mailman message indicates that the post-install was successful.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Section 5.6.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For item 1, the Back-out Procedure can be verified by confirming the values of the affected stop codes using FileMan.

For items 2, 3, 4, 5, 6, 7 and 9 the Back-out Procedure can be verified by printing the first 2 lines of the routine contained in this patch using the option First Line Routine Print \[XU FIRST LINE PRINT\]. Once the routine has been restored, it will no longer display 859 on the second line.This is routine-only patch and can be backed out with the patch backup message. The post-install routine SD53P859 will add the new Stop Code 605 to the SD TELE HEALTH STOP CODE FILE (#40.6). This will need to be deleted manually in FileMan.

For item 8, the data in the PARENT REQUEST field (#43) in the SDEC APPT REQUEST file (#409.85) will be modified by erasing the invalid pointer found in this field, which should not have been there for this non-MRTC appointment type. There is no rollback strategy required for this field being erased.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing will be completed by the time patch SD\*5.3\*859 is released.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out criteria will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will be done only with the concurrence and participation of development team and appropriate VA site/region personnel. The decision to back-out or rollback software will be a joint decision between development team, VA site/region personnel and other appropriate VA personnel.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installing an updated KIDS package, the site/region should have saved a backup of the routines in a mail message using the Backup a Transport Global \[XPD BACKUP\] menu option (this is done at time of install). The message containing the backed-up routines can be loaded with the "Xtract PackMan" function at the Message Action prompt. The Packman function "INSTALL/CHECK MESSAGE" is then used to install the backed up routines onto the VistA System.

If the patch was backed up for the build, from the Kernel Installation and Distribution System Menu, select the Installation Menu. Select the Install Package(s) option and choose the patch (xxx\*x.x\*xxxb) to install.

The back-out plan is to restore the routines from the backup created.

The Back-out Procedure can be verified by printing the first 2 lines of the routine contained in this patch using the option First Line Routine Print \[XU FIRST LINE PRINT\]. Once the routine contained in the SD\*5.3\*859 patch has been backed out, the first two lines of the routine will no longer contain the designation of this patch in the patch.

To back out item 1, it is necessary to use FileMan to manually edit the stop codes in SD TELE HEALTH STOP CODE File (#40.6).

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a routine-only patch. Note: This patch modifies the SD TELE HEALTH STOP CODE FILE (#40.6). The post-install routine SD53P859 will both add and delete Stop Codes. The stop code changes will need to be removed manually using FileMan.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback criteria will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority for rollback would come from the project IPT, the VA project manager, and other relevant stakeholders, where applicable.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two aspects to rolling back this patch.

For item 1, the backout process would be accomplished by editing the SD TELE HEALTH STOP CODE FILE (#40.6) in FileMan to back out the changes to that global with the assistance of the development team.

For item 8, the data in the PARENT REQUEST field (#43) in the SDEC APPT REQUEST file (#409.85) will be modified by erasing the invalid pointer found in this field, which should not have been there for this non-MRTC appointment type. There is no rollback strategy required for this field being erased.

There are no data dictionary or additional data changes in this patch.

# Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have any questions concerning the implementation of this application, contact the VA Service Desk at 1-855-673-4357 directly or log a ticket via VA yourIT Service Portal application (https://yourit.va.gov/va).

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No documentation describing the new functionality introduced by this patch is available.