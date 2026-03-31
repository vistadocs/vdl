---
title: LR*5.2*495 Laboratory Deployment, Installation, Back-Out, and Rollback Guide Patch
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Laboratory  Patch
app_code: LR
app_name: Laboratory (LA and LR)
section: CLI
app_status: active
pkg_ns: LR
patch_ver: 5.2
patch_id: LR*5.2*495
group_key: "LR:LR:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - patch
  - installation
  - back
  - routine
  - span
  - deployment
  - rollback
  - procedure
page_count: 0
word_count: 4026
section_count: 32
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lr_5_2_495_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lr_5_2_495_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=71"
---

Collaborative Terminology Tooling & Data Management (CTT&DM)

Native Domain Standardization (NDS)

Laboratory Etiology

Deployment, Installation, Back-Out, and Rollback Guide

Patch LR\*5.2\*495

![](lr-5-2-495-laboratory-deployment-installation-back-out-and-rollback-guide-patch/001.png)

February 2018

Office of Information and Technology (OI&T)

Revision History

| Date    | Version | Description                                            | Author                                           |
|---------|---------|--------------------------------------------------------|--------------------------------------------------|
| 02/2018 | 1.1     | Page <u>[9](#Note)</u> updated the note after Step 20. | ManTech Mission Solutions and Services Group     |
| 01/2018 | 1.0     | Delivery to Customer                                   | ManTech Mission Solutions and Services Group     |
| 01/2018 | 0.2     | Address issues found by Application Coordinator        | DG/ ManTech Mission Solutions and Services Group |
| 10/2017 | 0.1     | Initial draft                                          | DG/ ManTech Mission Solutions and Services Group |

<span id="_Toc506551572" class="anchor"></span>Table : Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Table of Contents

Table of Figures

Table of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Timeline](#timeline)
  - [Site Readiness Assessment](#site-readiness-assessment)
    - [Deployment Topology (Targeted Architecture)](#deployment-topology-targeted-architecture)
    - [Site Information (Locations, Deployment Recipients)](#site-information-locations-deployment-recipients)
    - [Site Preparation](#site-preparation)
  - [Resources](#resources)
    - [Facility Specifics](#facility-specifics)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
    - [Pre/Post Installation Overview](#prepost-installation-overview)
    - [Patch Dependencies](#patch-dependencies)
  - [Pre-Installation Instructions](#pre-installation-instructions)
    - [Creating a Local Patch Backup](#creating-a-local-patch-backup)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
    - [Routines](#routines)
    - [Data Dictionaries](#data-dictionaries)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install Labs Etiology Native Domain Standardization patch LR\*5.2\*495, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Labs Etiology Native Domain Standardization patch LR\*5.2\*495 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Etiology Native Domain Standardization patch LR\*5.2\*495 possesses a direct application dependency on the Laboratory Reports patch LR\*5.2\*468.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Labs Etiology Native Domain Standardization patch LR\*5.2\*495 possesses the following constraints:

- The update to the VistA ETIOLOGY FIELD File (#61.2) shall not affect the current functionality or conflict with applications that utilize this file.
- The field being added to this file should only be visible on the back end and to those requesting the information, not the GUI applications used by clinicians within the VA.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Team                    | Phase / Role                      | Tasks                                                                                                               |
|-------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------|
| OIT Regional Support    | Deployment                        | Plan and schedule deployment (including orchestration with vendors)                                                 |
| CTT&DM NDS Project Team | Deployment                        | Determine and document the roles and responsibilities of those involved in the deployment.                          |
| OIT Regional Support    | Deployment                        | Test for operational readiness                                                                                      |
| OIT Regional Support    | Deployment                        | Execute deployment                                                                                                  |
| OIT Regional Support    | Installation                      | Plan and schedule installation                                                                                      |
| CTT&DM NDS Project Team | Installations                     | Coordinate training                                                                                                 |
| OIT Regional Support    | Back-out                          | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |
| CTT&DM NDS Project Team | Post Deployment – Warranty Period | Hardware, Software and System Support                                                                               |
| OIT Regional Support    | Post Deployment – Post Warranty   | Hardware, Software and System Support                                                                               |

<span id="_Toc506551573" class="anchor"></span>Table : Software Specifications

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a concurrent online rollout. During IOC testing and after national release, patch LR\*5.2\*495 will be distributed via the FORUM Patch Module, and may be deployed at any site without regard to deployment status at other sites.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for a period of thirty days, as depicted in the master deployment schedule.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CTT&DM NDS patch LR\*5.2\*495 deployment.

The LR\*5.2\*495 patch must be manually installed, or manually queued for installation, at each VistA instance at which it is deployed, using the standard Kernel Installation Distribution System (KIDS) software. The LR\*5.2\*495 patch should be installed at all VA VistA instances running the VistA Laboratory v.5.2 application, and will update the M (Mumps) server software in each VistA instance’s Laboratory namespace.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment topology for the CTT&DM NDS patch LR\*5.2\*495, during IOC testing and after national release is described below.

<span id="_Toc506546596" class="anchor"></span>Figure : Patch LR\*5.2\*495 Topology

![](lr-5-2-495-laboratory-deployment-installation-back-out-and-rollback-guide-patch/002.png)

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During IOC testing, CTT&DM NDS patch LR\*5.2\*495 will be deployed at the following sites:

- <span class="mark">REDACTED</span>
- <span class="mark">REDACTED</span>

After national release, CTT&DM NDS patch LR\*5.2\*495 will be deployed at all sites running the VistA Laboratory v.5.2 application.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special preparation is required by the site prior to deployment.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment of CTT&DM NDS patch LR\*5.2\*495 requires a fully patched VistA environment running the Laboratory v.5.2 application, as well as a Health Product Support (HPS) team member available to perform the patch installation.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific deployment or installation features of CTT&DM NDS patch LR\*5.2\*495.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT&DM NDS patch LR\*5.2\*495 requires no site hardware specifications during, or prior to, deployment.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software                        | Make | Version | Configuration | Manufacturer | Other |
|------------------------------------------|------|---------|---------------|--------------|-------|
| VistA Laboratory (LR) patch LR\*5.2\*468 |      | 5.2     | Standard      | VHA          |       |

<span id="_Toc506551574" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in <u>Section 2</u> for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No notifications are required for deployment of CTT&DM NDS patch LR\*5.2\*495.

#### Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

Deployment/Installation/Back-Out Checklist

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that a Local Patch Backup is created that can be re-installed in the event that patch LR\*5.2\*495 must be backed out. The approximate time to create the saved local patch is 30 minutes.

### Patch Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*468 must be installed prior to installing this patch.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Creating a Local Patch Backup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following procedure to create a Local Patch Backup.

1.  From the KIDS (Kernel Installation & Distribution System) Menu, select ‘Edits and Distribution’.
2.  Select ‘Create a Build Using Namespace’.
3.  Enter a local patch name and identifier, suggested name ZLR\*5.2\*00495.
4.  When prompted ‘BUILD PACKAGE FILE LINK:’, press \<Enter\>.
5.  When prompted ‘BUILD TYPE: SINGLE PACKAGE//’, press \<Enter\>.
6.  When prompted ‘BUILD TRACK PACKAGE NATIONALLY: YES//’, enter NO.
7.  When prompted ‘Namespace:’, press \<Enter\>.
8.  When prompted ‘Select Edits and Distribution Option’, select: ‘Edit a Build’.
9.  Enter the local patch name from step 3 (ZLR\*5.2\*00495).
10. For the ‘Description:’ enter the following: “this is a local backup for LR\*5.2\*495. This patch should only be installed in the event that LR\*5.2\*00495 needs to be backed out.”
11. In the ‘COMMAND:’ field, enter ‘Next Page’.
12. For ‘File List’ Enter 61.2 for ETIOLOGY FIELD File.
13. In ‘Send Full or Partial DD’ field, enter FULL.
14. In the ‘Update the Data Dictionary:’ field, enter YES.
15. In the ‘Send Security Code:’ field, enter YES.
16. In the ‘Data Comes With File:’ field, enter NO.
17. In the DD Export Options dialog, move cursor to the COMMAND: prompt, enter ‘Close’
18. In the File List dialog, move cursor to the ‘COMMAND:’ prompt, enter ‘Next Page’.
19. In the Build Components section, move cursor to ROUTINE and press \<Enter\>.
20. In the Build Components section, move cursor to ROUTINE and press \<Enter\>.

<span id="Note" class="anchor"></span><u><span class="mark">\*\*NOTE: If patch LR\*5.2\*495 has not been previously installed, the routines listed in steps 21, 22, 23, and 27 will list as not found, since they are new with this patch</span>.</u>

21. In the first blank row in the ROUTINE dialog, enter LRMIEDIM, and ‘Send To Site’.
22. In the next blank row in the ROUTINE dialog, enter LRMIEDIS, and ‘Send to Site’.
23. In the next blank row in the ROUTINE dialog, enter LRSRVR9B, and ‘Send to Site’.
24. In the next blank row in the ROUTINE dialog, enter LRSRVR, and ‘Send to Site’.
25. In the next blank row in the ROUTINE dialog, enter LRSRVR6, and ‘Send to Site’.
26. In the next blank row in the ROUTINE dialog, enter LRSRVR8, and ‘Send to Site’
27. In the next blank row in the ROUTINE dialog, enter LR495PO, and ‘Send to Site’
28. Move cursor to the ‘COMMAND:’ prompt in the ROUTINE dialog, enter ‘Close’.
29. In the Build Components section, move cursor to OPTION and press \<Enter\>.
30. Enter LRMI and ‘Send to Site’.
31. Enter LR NDS LIM MENU and ‘Send to Site’.
32. Move cursor to the ‘COMMAND:’ prompt in the ROUTINE dialog, enter ‘Close’.
33. Move cursor to the ‘COMMAND:’ prompt in the BUILD COMPONENTS dialog, enter ‘Save’, then enter ‘Exit’.
34. When returned to the Edits and Distribution menu, select option ‘Transport a Distribution’.
35. Enter the ‘local package name and identifier’ that was created in Step 3. (ZLR\*5.2\*00495).
36. At the ‘Another Package Name:’ press \<Enter\>.
37. At the ‘OK to continue? Prompt, select YES//’ press \<Enter\>.
38. If creating a Host File transport, perform the following steps:
    1.  At the ‘Transport through (HF) Host File or (PM) PackMan:’ prompt, enter HF.
    2.  At the ‘Enter a Host File:’ prompt, enter the system file to which the Local Patch Backup will be saved. (ZLR_5_2_00495.KID).
    3.  At the ‘Header Comment:’ Enter ‘Local Backup of LR\*5.2\*495’.
    4.  At the Edits and Distribution Menu, press \<Enter\>.
    5.  At the KIDS Menu press \<Enter\>.
39. If creating a PackMan transport, perform the following steps:
    1.  At the ‘Transport through (HF) Host File or (PM) PackMan:’ enter PM.
    2.  At the ‘Header Comment:’ enter ‘Local Backup of LR\*5.2\*495’
    3.  For the description of Packman Message, Enter: ‘This is a saved backup for the Laboratory Etiology patch install for LR\*5.2\*495. This local build will be used in the event that the above mentioned installs need to be backed out.’
    4.  At ‘EDIT Option:’ press \<Enter\>.
    5.  At the ‘Do you wish to secure this message? NO// prompt, Enter ‘NO’.
    6.  At the ‘Send mail to:’ prompt, Enter your name.
    7.  At the ‘Select basket to send to: IN//’ prompt: press \<Enter\>.
    8.  At the ‘And Send to:’ prompt: Enter any additional persons that may need to have the local patch.
    9.  At The ‘Select Edits and Distribution \<TEST ACCOUNT\> Option:’ press \<Enter\>.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*495 does not require any platform installation or preparation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT&DM NDS patch LR\*5.2\*495 is being released as a FORUM Patch via the Patch Module, therefore, the patch must be downloaded from FORUM, and forwarded to the destination site in the form of a Packman message.

Documentation describing the new functionality introduced by this patch is available. The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

- <span class="mark">REDACTED</span>

The documentation will be in the form of Adobe Acrobat files. Documentation can also be found on the VA Software Documentation Library at: http://www.va.gov/vdl/

Title: Deployment, Installation, Back-Out, Rollback Guide LR\*5.2\*495

File Name: lr_5_2_495_ig.docx

lr_5_2_495_ig.pdf

FTP Mode: Binary

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new database is required for the CTT&DM NDS patch LR\*5.2\*495.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are required for installation of CTT&DM NDS patch LR\*5.2\*495.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No CRON scripts are required for installation of CTT&DM NDS patch LR\*5.2\*495.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to national VA network, as well as the local network of each site to receive CTT&DM NDS patch LR\*5.2\*495 is required to perform the installation, as well as authority to create and install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter the patch LR\*5.2\*495:
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of these patch routines, DDs, templates, etc.
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
1.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
2.  Verify/enter the proper names of the Mail Group coordinator for G.LMI and G.LAB MAPPING when prompted.
3.  When prompted: 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond NO.
4.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
5.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' , respond NO.
6.  If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of routines in CTT&DM NDS patch LR\*5.2\*495 may be verified by running the Kernel checksum tool from the VistA server command line after installation:

D CHECK1^XTSUMBLD

The checksums produced by the checksum tool should match the numeric portion of the “After:” checksums in the CTT&DM NDS patch LR\*5.2\*495 patch description.

<span id="_Toc506546597" class="anchor"></span>Figure : Example, Checksum for routines as displayed by Kernel checksum tool CHECK1^XTSUMBLD

LR495PO value = 2398805

LRMIEDIM value = 2327306

LRMIEDIS value = 3017841

LRSRVR value = 20098567

LRSRVR6 value = 41247527

LRSRVR8 value = 259906666

LRSRVR9B value = 37485068

The “After:” checksum for routines as displayed in the patch description:

Routine Name: LR495PO

Before: n/a After: B2398805 \*\*495\*\*

Routine Name: LRMIEDIM

Before: n/a After: B15137726 \*\*495\*\*

Routine Name: LRMIEDIS

Before: n/a After: B4897577 \*\*495\*\*

Routine Name: LRSRVR

Before: B19202402 After: B20098567 \*\*232,303,346,350,468,495\*\*

Routine Name: LRSRVR6

Before: B37896776 After: B41247527 \*\*346,378,350,425,460,495\*\*

Routine Name: LRSRVR8

Before:B248084471 After:B259906666 \*\*350,495\*\*

Routine Name: LRSRVR9B

Before: n/a After: B47147933 \*\*495\*\*

Installation of Data Dictionaries in CTT&DM NDS patch LR\*5.2\*495 may be verified by running the FileMan Data Listing tool from the VistA server command line after installation. The new fields will print in the output if installation was successful.

<span id="_Toc506546598" class="anchor"></span>Figure : Example, verification of fields installed with LR\*5.2\*495 using FileMan Data Listing

D P^DI

Select OPTION: *<u>DATA DICTIONARY UTILITIES</u>*

Select DATA DICTIONARY UTILITY OPTION: *<u>LIST FILE ATTRIBUTES</u>*

START WITH What File: *<u>ETIOLOGY FIELD//</u>* (1217 entries)

GO TO What File: *<u>ETIOLOGY//</u>* (1217 entries)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD// *<u>BRIEF</u>*

ALPHABETICALLY BY LABEL? No// *<u>(No)</u>*

Start with field: FIRST// *<u>64.9102 INACTIVE DATE</u>*

Go to field: *<u>64.9102 INACTIVE DATE</u>*

DEVICE: ;;9999 DEC Windows Right Margin: 80// <u>132</u>

<span id="_Toc506546599" class="anchor"></span>Figure : OUTPUT, FileMan brief Data Listing verifying successful installation

BRIEF DATA DICTIONARY \#61.2 -- ETIOLOGY FIELD FILE 9/5/17 PAGE 1

SITE: TEST.CHEYENNE.MED.VA.GOV UCI: CHEY59,ROU (VERSION 5.2)

-------------------------------------------------------------------------------

INACTIVE DATE 61.2,64.9102 DATE

Enter the date this ETIOLOGY entry should no longer be considered available.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No System Configuration is required before or after deployment of CTT&DM NDS patch LR\*5.2\*495.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Database Tuning is required before or after deployment of CTT&DM NDS patch LR\*5.2\*495.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out of this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

Perform the back-out procedure to load the locally made patch created in Section 4. The back-out is to be performed by persons with programmer-level access.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-out Strategy is to load the locally made patch that was created in <u>Section 4</u> Installation.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out should only be done in the event that the local facility management determines that the patch LR\*5.2\*495 is not appropriate for that facility, and should only be done as a last resort.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch LR\*5.2\*495.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Facility Management would need to determine patch LR\*5.2\*495 is not appropriate for their facility.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out LR\*5.2\*495, the local facility will not be able to add the INACTIVE DATE to ETIOLOGY FIELD File (#61.2) entries.

The SNOMED updates for files TOPOGRAPHY FIELD (#61), ETIOLOGY FIELD (#61.2), and COLLECTION SAMPLE (#62) files will revert to the current patch update FTP method.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Local Facility Management has the authority to back-out patch LR\*5.2\*495.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

Perform the back-out procedure to load and install the locally made patch created in Section 4.2, delete the new imported routines, and delete the new INACTIVE DATE (#64.9102) field in the Laboratory ETIOLOGY FIELD (#61.2) file.

The following is an example of the steps that would be executed for the fields being removed. The back-out is to be performed by persons with programmer privileges. File Manager should be used to delete the new fields added with LR\*5.2\*495.

Back-Out Procedure

The following will need to be executed from the programmers prompt (User input depicted below in *bold-italicized* and <u>underlined</u> font).

<span id="_Toc506546600" class="anchor"></span>Figure : Delete new routines using ROUTINE DELETE

*<u>D ^%ZTRDEL</u>*

ROUTINE DELETE

All Routines? No =\> *<u>No</u>*

Routine: *<u>LRMIEDIM</u>*

Routine: *<u>LRMIEDIS</u>*

Routine: *<u>LRSRVR9B</u>*

Routine: *<u>LR495PO</u>*

1 routine

3 routines to DELETE, OK: NO// *<u>Y</u>*

LRMIEDIM

LRMIEDIS

LRSRVR9B

LR495PO

Done.

<span id="_Toc506546601" class="anchor"></span>Figure : Delete new field and data from ETIOLOGY FIELD (#61.2) file

*<u>D P^DI</u>*

Select OPTION: *<u>MODIFY FILE ATTRIBUTES</u>*

Do you want to use the screen-mode version? YES// *<u>NO</u>*

MODIFY WHAT FILE: // *<u>61.2</u>* ETIOLOGY FIELD (#61.2)

(2346 entries)

Select FIELD: *<u>INACTIVE DATE</u>*

LABEL: INACTIVE DATE// *<u>@</u>*

SURE YOU WANT TO DELETE THE ENTIRE 'INACTIVE DATE' FIELD? *<u>Y</u>* (Yes)

OK TO DELETE 'INACTIVE DATE' FIELDS IN THE EXISTING ENTRIES? Yes// *<u>Y</u>* (Yes).....

The steps for the load and installation of the locally made patch are very similar to the installation steps listed in <u>Section 4.9</u>.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter the local patch from section 4.8, ZLR\*5.2\*00495.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  <u>Verify/enter the proper names of the Mail Group coordinator for G.LMI and G.LAB MAPPING when prompted.</u>
6.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//'
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//'
9.  If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out patch LR\*5.2\*495 by installing the local patch from section 4.8, routine back-out may be verified by running the Kernel checksum tool from the VistA server command line after installation:

D CHECK1^XTSUMBLD

The checksums produced by the checksum tool should match the numeric portion of the “Before:” checksums in the CTT&DM NDS patch LR\*5.2\*495 patch description.

For patch LR\*5.2\*495, since the routines are new, the “Before:” checksums from the patch description are “n/a”. If routine back-out was successful, the checksum tool will display the message “Routine not in this UCI” in place of a checksum.

<span id="_Toc506546602" class="anchor"></span>Figure : Patch description “Before” checksums are “n/a”

Routine Name: LR495PO

Before: n/a After: B2398805 \*\*495\*\*

Routine Name: LRMIEDIM

Before: n/a After: 2327306 \*\*495\*\*

Routine Name: LRMIEDIS

Before: n/a After: 3017841 \*\*495\*\*

Routine Name: LRSRVR9B

Before: n/a After: 37485068 \*\*495\*\*

<span id="_Toc506546603" class="anchor"></span>Figure : After back-out, checksum tool displays “Routine not in this UCI”

*<u>D CHECK1^XTSUMBLD</u>*

New CheckSum CHECK1^XTSUMBLD:

Select one of the following:

P Package

B Build

Build from: *<u>Build</u>*

This will check the routines from a BUILD file.

Select BUILD NAME: *<u>LR\*5.2\*495</u>* LAB SERVICE

LRMIEDIM value = 15137726 Routine not in this UCI

LRMIEDIS value = 4897577 Routine not in this UCI

LRSRVR9B value = 47147933 Routine not in this UCI

LR495PO value = 2398805 Routine not in this UCI

done

### Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out Patch LR\*5.2\*495, successful back-out of the fields installed by the patch may be verified by running a global listing from the VistA server command line after installation.

The field in the ETIOLOGY FIELD file (#62.1) deleted during back-out is:

> The INACTIVE DATE field (#64.9102).

A global listing should be performed for the following global nodes, after which nothing should be listed if back-out was successful:

> Global ^DD(61.1,64.9102

<span id="_Toc506546604" class="anchor"></span>Figure : Example, global listing of backed out globals

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global *<u>^DD(61.2,64.9102</u>*

\<nothing should print\>

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A