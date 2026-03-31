---
title: TMP VistA Patch 876 DIBRG
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: TMP
app_name: Telehealth Management Platform
section: CLI
app_status: active
pkg_ns: TMP
patch_ver: 53.876
patch_id: TMP*53.876*876
group_key: "TMP:TMP:53.876"
file_numbers: []
security_keys: []
menu_options: 0
description: The Deployment, Installation, Back-Out and Rollback Guide defines the ordered, technical steps required to install the product, back out the installation (if necessary), and roll back to the previously installed version of the product. It provides installation instructions for the SD\5.3\876 patch
audience: 
keywords: 
  - table
  - contents
  - back
  - installation
  - rollback
  - patch
  - procedure
  - install
  - requirements
  - post
page_count: 0
word_count: 1532
section_count: 26
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2024
revision_count: 1
revision_newest: 3/8/2024
revision_oldest: 3/8/2024
docx_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/SD_53_876_DIBRG.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/SD_53_876_DIBRG.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=231"
---

Scheduling Package EnhancementPatch SD\*5.3\*876

Deployment, Installation, Back-Out, and Rollback Guide

![](tmp-vista-patch-876-dibrg/001.png)

March 2024

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
  - [Post-Install Routine](#post-install-routine)
  - [Post-Install Instructions](#post-install-instructions)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
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
| Date     | Version | Description            | Author |
|----------|---------|------------------------|--------|
| 3/8/2024 | 1.0.0   | Initial Document Draft | TMP    |
Table showing the Revision History.

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the Deployment, Installation, Back-Out, and Rollback Guide for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.
# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Deployment, Installation, Back-Out and Rollback Guide defines the ordered, technical steps required to install the product, back out the installation (if necessary), and roll back to the previously installed version of the product. It provides installation instructions for the SD\*5.3\*876 patch

## Purpose 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Guide is to provide installation steps for the SD\*5.3\*876 patch. The intended audience for this document is the Information Resource Management Systems (IRMS) staff. Some of the main features of this patch are the following:

## Dependencies 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch SD\*5.3\*874 must be installed prior to installing SD\*5.3\*876.

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
1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name (ex. SD\*5.3\*876).
2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup, the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
1.  At the Installation option menu, select Backup a Transport Global.
2.  At the Select INSTALL NAME prompt, enter your build SD\*5.3\*876.
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

## Post-Install Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post-install routine SD53P876 adds the newly updated stop code 355 to the SD TELE HEALTH STOP CODE FILE file (#40.6). It also removes stop code 656 from the SD TELE HEALTH STOP CODE FILE file (#40.6)

## Post-Install Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Details of the changes applied by this patch are provided during the installation and may also be reviewed with the Install File Print option on the Utilities menu on the Kernel Installation and Distribution System menu.

It is important to check the SD TELE HEALTH STOP CODE FILE file (#40.6) post installation to make sure that all of the updates are correctly reflected in the SD TELE HEALTH STOP CODE FILE file (#40.6). If any discrepancies are found, you should enter a ServiceNow ticket.

3\. After the post install has finished running, sites can delete the SD53P876 routine using the Delete Routines \[XTRDEL\] option if they wish.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Section 5.6.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the complexity of this patch, it is not recommended for back-out, and a restore from a backup of the Transport Global should not be attempted. In the event that this patch needs to be backed out the patch installer should enter a ServiceNow Ticket. The development team will need to issue a follow-up patch in order to comprehensively back-out this

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out criteria will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See 5.1

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See 5.2

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback will be done only with the concurrence and participation of the development team and appropriate VA site/region personnel. The decision to back-out or rollback software will be a joint decision between the development team, VA site/region personnel and other appropriate VA personnel.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback criteria will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See 6.1

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the complexity of this patch, it is not recommended for rollback, and a restore from a backup of the Transport Global should not be attempted. In the event that this patch needs to be backed out the patch installer should enter a ServiceNow Ticket. The development team will need to issue a follow-up patch in order to comprehensively back-out this patch.

# Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have any questions concerning the implementation of this application, contact the VA Service Desk at 1-855-673-4357 directly or log a ticket via VA yourIT Service Portal application (https://yourit.va.gov/va).

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No documentation describing the new functionality introduced by this patch is available.