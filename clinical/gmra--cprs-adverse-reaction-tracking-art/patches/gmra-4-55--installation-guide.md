---
title: GMRA*4*55 Deployment, Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: GMRA
app_name: "CPRS: Adverse Reaction Tracking (ART)"
section: CLI
app_status: active
pkg_ns: GMRA
patch_ver: 4
patch_id: GMRA*4*55
group_key: "GMRA:GMRA:4"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - contents
  - patch
  - installation
  - gmra
  - back
  - allergies
  - deployment
  - procedure
  - rollback
page_count: 0
word_count: 3295
section_count: 30
table_count: 4
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Advrs_Reaction_Trk_(ART)/gmra455_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Advrs_Reaction_Trk_(ART)/gmra455_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=57"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Collaborative Terminology Tooling & Data Management (CTT & DM)

  Native Domain Standardization (NDS)

  Allergies (GMRA\*4\*55)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](gmra-4-55-deployment-installation-back-out-and-rollback-guide/001.png)

April 2017

Office of Information and Technology (OI&T)

Revision History

<table>
<caption><p>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>04/2017</td>
<td>1.0</td>
<td><p>Updates per Release Coordinator Request Date changed to April.</p>
<p>Delivery to Customer</p></td>
<td>Mantech Mission, Solutions and Services Management REDACTED</td>
</tr>
<tr class="even">
<td>03/2017</td>
<td>0.5</td>
<td>Update Back out Procedure</td>
<td>Mantech Mission Solutions and Services</td>
</tr>
<tr class="odd">
<td>12/2016</td>
<td>0.4</td>
<td>Delivery to Customer</td>
<td>Mantech Mission Solutions and Services Management</td>
</tr>
<tr class="even">
<td>12/2016</td>
<td>0.3</td>
<td>Address Tech Writer Review issues</td>
<td>Mantech Mission Solutions and Services</td>
</tr>
<tr class="odd">
<td>12/19/2016</td>
<td>0.2</td>
<td>Technical Writer Review</td>
<td>REDACTED - Mantech Mission Solutions and Services</td>
</tr>
<tr class="even">
<td>12/18/2016</td>
<td>0.1</td>
<td>Initial Draft</td>
<td>REDACTED - Mantech Mission Solutions and Services</td>
</tr>
</tbody>
</table>

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Table of Contents

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
    - [Pre-Installation Instructions](#pre-installation-instructions)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [Installation Instructions](#installation-instructions)
  - [Installation Verification Procedure](#installation-verification-procedure)
    - [ROUTINES](#routines)
    - [GLOBALS / DATA DEFINITIONS](#globals-data-definitions)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure Overview](#back-out-procedure-overview)
    - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install Collaborative Terminology Tooling & Data Management (CTT & DM) Native Domain Standardization (NDS) Allergies patch GMRA\*4\*55, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CTT & DM NDS Allergies patch GMRA\*4\*55 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CTT & DM NDS Allergies patch GMRA\*4\*55 possesses a direct application dependency on the VistA Adverse Reaction Tracking (ART) v.4.0 application, and an indirect application dependency on Computerized Patient Record System (CPRS) v.1.0.

The CTT & DM NDS Allergies patch GMRA\*4\*55 possesses a specific patch dependency on Kernel patch XU\*8\*676.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT & DM NDS Allergies patch GMRA\*4\*55 possesses the following constraints:

- The update to the Adverse Reaction Tracking (ART) v.4.0 package files \#120.82 and \#120.83 shall not affect the current functionality or conflict with applications that utilize these files.
- The field being added to these files should only be visible within VistA and to those requesting the information. No GUI applications will be modified or affected in this effort.
- The new field in each respective file is designed to utilize a name-value pair structure with the respective term and its corresponding code in order to operate with current STS maintenance practices.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                               | Phase / Role  | Tasks                                                                                                       | Project Phase (See Schedule) |
|-----|----------------------------------------------------|---------------|-------------------------------------------------------------------------------------------------------------|------------------------------|
| 1   | STS Team                                           | Deployment    | Plan and schedule deployment (including orchestration with vendors)                                         |                              |
| 2   | STS Team                                           | Deployment    | Develop O&M Plan                                                                                            |                              |
| 3   | FO                                                 | Deployment    | Test for operational readiness                                                                              |                              |
| 4   | STS Team / FO                                      | Deployment    | Execute deployment                                                                                          |                              |
| 5   | STS Team / FO                                      | Installation  | Plan and schedule installation                                                                              |                              |
| N/A | Regional PM/FIS/OPP PM                             | Installation  | Ensure authority to operate and that certificate authority (CA)/security documentation is in place          |                              |
| N/A | Regional PM/FIS/OPP PM/                            | Installation  | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes |                              |
| N/A | Regional PM/FIS/OPP PM/ Nat’l Education & Training | Installations | Coordinate training                                                                                         |                              |

Table 2: Software Specifications

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a concurrent online rollout. During IOC testing and after national release, patch GMRA\*4\*55 will be distributed via the FORUM Patch Module, and may be deployed at any site without regard to deployment status at other sites.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for a period of thirty days, as depicted in the master deployment schedule.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CTT & DM NDS patch GMRA\*4\*55 deployment.

The GMRA\*4\*55 Patch must be manually installed, or manually queued for installation, at each VistA instance at which it is deployed, using the standard Kernel Installation Distribution System (KIDS) software. The GMRA\*4\*55 patch should be installed at all VA VistA instances running the Computerized Patient Record System (CPRS) v.1.0 and Adverse Reaction Tracking (ART) v.4.0 applications, and will update the M (Mumps) server software in each VistA instance’s GMRA namespace.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment topology for the CTT & DM NDS Allergies Patch GMRA\*4\*55, during IOC testing and after national release is described in Figure 1. CTT & DM NDS Allergies Patch GMRA\*4\*55 Deployment Topology.

Figure 1. CTT & DM NDS Allergies Patch GMRA\*4\*55 Deployment Topology

![](gmra-4-55-deployment-installation-back-out-and-rollback-guide/002.png)

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During IOC testing, CTT & DM NDS Allergies Patch GMRA\*4\*55 will be deployed at the following sites:

- Central Plains HCS
- Oklahoma City, OK

After national release, CTT & DM NDS Allergies Patch GMRA\*4\*55 will be deployed at all sites running the CPRS v.1.0 and ADVERSE REACTION TRACKING (ART) v.4.0 applications.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special preparation is required by the site prior to deployment.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment of CTT & DM NDS Allergies Patch GMRA\*4\*55 requires an up-to-date VistA environment running the CPRS v.1.0, Adverse Reaction Tracking (ART) v.4.0, and Kernel v.8.0 applications.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific deployment or installation features of CTT & DM NDS Allergies Patch GMRA\*4\*55.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT & DM NDS Allergies Patch GMRA\*4\*55 requires no site hardware specifications during, or prior to deployment.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software               | Make | Version | Configuration | Manufacturer | Other |
|---------------------------------|------|---------|---------------|--------------|-------|
| CPRS                            | VHA  | 1.0     | Standard      | VHA          | N/A   |
| ADVERSE REACTION TRACKING (ART) | VHA  | 4.0     | Standard      | VHA          | N/A   |
| Kernel patch XU\*8.0\*676       | VHA  | 8.0     | Standard      | VHA          | N/A   |

Table 3: Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in <u>Section 2</u> for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No notifications are required for deployment of CTT & DM NDS Allergies patch GMRA\*4\*55.

#### Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | TBD | TBD  | TBD                           |
| Install  | TBD | TBD  | TBD                           |
| Back-Out | TBD | TBD  | TBD                           |

| Deploy   | \-  | The Deploy task is performed when the patch is sent to test site(s) by the development team.                        |
|----------|-----|---------------------------------------------------------------------------------------------------------------------|
| Install  | \-  | The Install task is performed when the patch is installed at the test site(s).                                      |
| Back-Out | \-  | The optional Back-Out task is performed in the event the patch must be uninstalled, or removed, from the test site. |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that a *“Back-up” Local Patch File* is created that can be re-installed in the event that patch GMRA\*4\*55 must be backed out. However, this method does not back out Database Definitions (DDs). It will only delete the new routine added by GMRA\*4\*55.

The following patches must be installed in the following order before this patch may be installed.

XU\*8.0\*676

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

### Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the patch is loaded a backup of the patch needs to be created.

1.  Go to the ‘Kernel Installation & Distribution System’
2.  Select option ‘Installation’
3.  Select option ‘5 Backup a Transport Global’
4.  At the ‘Select INSTALL NAME:’ prompt enter GMRA\*4\*55.
5.  At the ‘Subject:’ prompt you can accept the default subject or enter your own subject. The subject should be easily recognizable in case the GMRA\*4\*55 Patch needs to be backed off.
6.  At the ‘Send mail to:’ prompt you should send to yourself at a minimum. You may create a folder to place the backup in so that in the event the GMRA\*4\*55 patch needs to be backed off you can find it easily.

You may also send the backup to others, as needed.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch GMRA\*4\*55 does not require any platform installation or preparation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT & DM NDS Allergies patch GMRA\*4\*55 is being released as a FORUM Patch by means of the Patch Module, therefore, the patch must be downloaded from FORUM, and forwarded to the destination site, in the form of a Packman message.

There is no new functional documentation available.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new database is required for the CTT & DM NDS Allergies Patch GMRA\*4\*55.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are required for installation of CTT & DM NDS Allergies Patch GMRA\*4\*55.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No CRON scripts are required for installation of CTT & DM NDS Allergies Patch GMRA\*4\*55.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to national VA network, as well as the local network of each site to receive CTT & DM NDS Allergies Patch GMRA\*4\*55 is required to perform the installation, as well as authority to create and install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of this patch (GMRA\*4.0\*55) will modify the GMR ALLERGIES file (#120.82) and the SIGNS/SYMPTOMS FILE (#120.83) by adding the CODING SYSTEM multiple fields. This patch also adds a routine that will assist in the parsing of the HL7 message from STS with file updates.

1.  Choose the PackMan message containing Patch GMRA\*4.0\*55.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
7.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the patch name GMRA\*4.0\*55.
8.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
9.  Compare Transport Global to Current System - This option will (allow you to view all changes that will be made when this patch is installed. It compares all components of the patch routines, DDs, templates, etc.)
10. Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
11. From the Installation Menu, select the Install Package(s) option and choose the patch to install.
12. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' respond NO.
13. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
14. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' respond NO.
15. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ROUTINES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of CTT & DM NDS Allergies Patch GMRA\*4\*55 may be verified by running the Kernel checksum tool from the VistA server command line after installation:

D CHECK1^XTSUMBLD

The checksums produced by the checksum tool should match the numeric portion of the “After:” checksums in the CTT & DM NDS Allergies Patch GMRA\*4\*55 patch description.

<u>Example</u>:

Checksum for routine GMRAVZRT as displayed by Kernel checksum tool CHECK1^XTSUMBLD:

GMRAVZRT value = B24863008

The “After:” checksum for routine GMRAVZRT as displayed in the patch description:

Routine Name: GMRAVZRT

Before: n/a After: B24863008 \*\*55\*\*

### GLOBALS / DATA DEFINITIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of CTT & DM NDS Allergies patch GMRA\*4\*55 may be verified by running global listings from the VistA server command line after installation:

D ^%G

Global listings should be performed for the following global nodes:

Global ^DD(120.82,6,0

Global ^DD(120.83,3,0

Example:

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global ^DD(120.82,6,0 -- NOTE: translation in effect

^DD(120.82,6,0)="CODING SYSTEM^120.822A^^1;0"

Global ^DD(120.83,3,0 -- NOTE: translation in effect

^DD(120.83,3,0)="CODING SYSTEM^120.833A^^1;0"

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No System Configuration is required before or after deployment of CTT & DM NDS Allergies patch GMRA\*4\*55.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Database Tuning is required before or after deployment of CTT & DM NDS Allergies patch GMRA\*4\*55.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the back-out procedure:

1.  Since there is other software components (routines.) contained in the patch, the ‘restore’ or backout process involving Kernel Installation and Distribution System (KIDS) be deployed by loading the “Back-up” Local Patch File as mentioned in Section 4.1.1. This will delete the routine installed by patch GMRA\*4\*55.
16. The Backout Procedure ALSO consists of individually removing each new Data Definition (DD) introduced by the Patch GMRA\*4\*55 as mentioned in Section 5.5.

The back-out is to be performed by persons with programmer-level access, and in conjunction with the STS team.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out strategy is to:

1.  The restore or backout process involving Kernel Installation and Distribution System (KIDS) is deployed by loading the “Back-up” Local Patch File as mentioned in Section 4.1.1.
17. The Backout Strategy is to manually delete the new Data Definitions (DDs) introduced with this patch.

The back-out should only be done in the event that the local facility management determines that the patch GMRA\*4\*55 is not appropriate for that facility, and should only be done as a last resort.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch GMRA\*4\*55.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Facility Management would need to determine patch GMRA\*4\*55 is not appropriate for their facility.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out GMRA\*4\*55, the local facility will not be able to use the Adverse Reaction Tracking package to update VistA allergies and allergy symptoms with standard terminology codes from the respective Standards Development Organizations.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Local Facility Management has the authority to back-out CTT & DM NDS Allergies Patch GMRA\*4\*55.

## Back-Out Procedure Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The backout is to be performed by persons with programmer-level access and in conjunction with the STS Team. File Manager should be used to delete the new CODING SYSTEM multiple added with GMRA\*4\*55, which will automatically also remove sub-fields and data.

### Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

USE THESE STEPS TO INSTALL THE BACK UP MESSAGE CREATED IN SECTION 4.1.2 AND SAVED AS 'PM' (PACK MAN) Mail Message.

1.  At the 'Select Systems Manager Menu' enter 'MAIL'
18. At the 'Select MailMan Menu' enter 'RML'
19. At the 'Select message reader: Classic//' prompt press \<enter\>
20. At the 'Read mail in basket: IN//' prompt press (or enter the basket that you placed the backup message in)\<enter\>
21. At the 'IN Basket Message:' prompt enter the message number for the previously created “Back-up” Local Patch File in step 4.1.1.
22. Read the message and make sure that this is the PackMan message containing the previously saved “Back-up” Local Patch File.
23. After reading the message, at the 'Enter message action (in IN basket): Ignore//' prompt enter 'X' (Xtract KIDS)
24. At the 'Select PackMan function:' prompt enter '6' (INSTALL/CHECK MESSAGE)
25. Warning: Installing this message will cause a permanent update of globals and routines.
26. At the ‘Do you really want to do this? NO//’ prompt enter YES.
27. At the ‘Shall I preserve the routines on disk in a separate back-up message? YES//’ prompt enter ‘NO.’
28. The install displays the routines being unloaded.
29. At the ‘Select PackMan function:’ enter \<CR\>
30. At the ‘Enter message action (in IN basket): Ignore//’ prompt enter ‘^’
31. Enter ‘\<CR\>’ to return to your starting menu.

The following will need to be executed from the programmers prompt (User input depicted below in *bold italicized* font):

Delete CODING SYSTEM multiple and data from GMR ALLERGIES (#120.82) file:

> *D P^DI*

> Select OPTION: *MODIFY FILE ATTRIBUTES*

> Do you want to use the screen-mode version? YES// *NO*

> MODIFY WHAT FILE: HDIS FILE/FIELD// *120.82* GMR ALLERGIES

> (4951 entries)

> Select FIELD: *CODING SYSTEM* (multiple)

> LABEL: CODING SYSTEM// *@*

> SURE YOU WANT TO DELETE THE ENTIRE 'CODING SYSTEM' FIELD? *Y* (Yes)

> OK TO DELETE 'CODING SYSTEM' FIELDS IN THE EXISTING ENTRIES? Yes// *Y* (Yes).....

Delete Coding System multiple and data from SIGNS/SYMPTOMS (120.83) file:

> *D P^DI*

> Select OPTION: *MODIFY FILE ATTRIBUTES*

> Do you want to use the screen-mode version? YES// *NO*

> MODIFY WHAT FILE: HDIS FILE/FIELD// *120.83* SIGNS/SYMPTOMS

> (4948 entries)

> Select FIELD: *CODING SYSTEM* (multiple)

> LABEL: CODING SYSTEM// *@*

> SURE YOU WANT TO DELETE THE ENTIRE 'CODING SYSTEM' FIELD? *Y* (Yes)

> OK TO DELETE 'CODING SYSTEM' FIELDS IN THE EXISTING ENTRIES? Yes// *Y* (Yes).....

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out CTT & DM NDS Allergies patch GMRA\*4\*55 by installing the local patch from Section 4.8, back-out may be verified by running the Kernel checksum tool from the VistA server command line after installation:

D CHECK1^XTSUMBLD

The checksums produced by the checksum tool should match the numeric portion of the “Before:” checksums in the CTT & DM NDS Allergies patch GMRA\*4\*55 patch description.

DATA DICTIONARIES

After backing out Patch GMRA\*4.0\*55, successful back-out of the CODING SYSTEM (#6) multiple field in the GMR ALLERGIES (#120.82) and the CODING SYSTEM (#3) multiple field in the SIGNS/SYMPTOMS (120.83) may be verified by running a global listing from the VistA server command line after installation. A global listing should be performed for the following global nodes, after which nothing should be listed if back-out was successful:

Global ^DD(120.82,6,0

Global ^DD(120.83,3,0

Example:

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global ^DD(120.82,6,0 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(120.83,3,0 -- NOTE: translation in effect

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