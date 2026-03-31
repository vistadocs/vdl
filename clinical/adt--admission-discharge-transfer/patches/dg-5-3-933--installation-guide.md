---
title: DG*5.3*933 CTT & DM NDS Demographics DIBRG
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: CTT & DM NDS Demographics DIBRG
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: archive
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*933
group_key: "ADT:DG:5.3"
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
  - routine
  - back
  - prompt
  - dgmf
  - procedure
  - global
page_count: 0
word_count: 5547
section_count: 31
table_count: 6
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/dg_5_3_933_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/dg_5_3_933_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=327"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Collaborative Terminology Tooling & Data Management (CTT&DM)

  Native Domain Standardization (NDS)

  Demographics (DG\*5.3\*933)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](dg-5-3-933-ctt-dm-nds-demographics-dibrg/001.png)

February 2018

Office of Information and Technology (OI&T)

Revision History

| Date    | Version | Description          | Author                             |
|---------|---------|----------------------|------------------------------------|
| 02/2018 | 1.0     | Delivery to Customer | <span class="mark">redacted</span> |

Table 1: Deployment, Installation, Back-Out, and Rollback Roles and Responsibilities

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
    - [Patch Dependencies](#patch-dependencies)
    - [Pre-Installation Instructions](#pre-installation-instructions)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [Installation Instructions:](#installation-instructions)
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
    - [Back-Out Procedure](#back-out-procedure-2)
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
    - [Routines](#routines)
    - [Data Dictionaries](#data-dictionaries)
    - [Options](#options)
    - [Input Templates](#input-templates)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Creating a Local Backup Patch File](#creating-a-local-backup-patch-file)
    - [Creating an HF Transport](#creating-an-hf-transport)
    - [Creating a PM Transport](#creating-a-pm-transport)
This document describes how to deploy and install Demographics Native Domain Standardization (NDS) patch DG\*5.3\*933, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.
> **NOTE:** IMPORTANT TECHNICAL NOTE regarding this patch, DG\*5.3\*933, and XINDEX
XINDEX will report the following unfounded error AFTER patch
installation. This error can be ignored.
DGZRT \* \* 139 Lines, 6922 Bytes, Checksum: B36061811
..Q:'@(\$Q(ZZZ(99999999999),-1)) ; Ignore "Invalid or
wrong number of arguments to a function" XINDEX warning.
POST+65 F - Invalid or wrong number of arguments to a function.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Demographics Native Domain Standardization patch DG\*5.3\*933 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Demographics Native Domain Standardization patch DG\*5.3\*933 possesses a direct application dependency on the VistA Admission Discharge Transfer (ADT) / Registration v.5.3 application.

The Demographics Native Domain Standardization patch DG\*5.3\*933 has a direct dependency on patches HDI\*1.0\*19 and DG\*5.3\*782, and an indirect patch dependency on XU\*8.0\*682, which is required by HDI\*1.0\*19.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Demographics Native Domain Standardization patch DG\*5.3\*933 possesses the following constraints:

- The update to the VistA package files RACE (#10), MARITAL STATUS (#11), and RELIGION (#13) shall not affect the current functionality or conflict with applications that utilize these files.
- The new VistA files RACE MASTER (#10.99), MASTER MARITAL STATUS (#11.99), and MASTER RELIGION (#13.99) shall not affect the current functionality or conflict with applications that utilize Demographics files.
- The files and fields being added should only be visible on the back end and to those requesting the information, not the Graphical User Interface (GUI) applications used by clinicians within the VA.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                    | Phase / Role                      | Tasks                                                                                                                | Project Phase (See Schedule) |
|-----|-------------------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------|
|     | OIT Regional Support    | Deployment                        | Plan and schedule deployment (including orchestration with vendors).                                                 |                              |
|     | CTT&DM NDS Project Team | Deployment                        | Determine and document the roles and responsibilities of those involved in the deployment.                           |                              |
|     | OIT Regional Support    | Deployment                        | Test for operational readiness.                                                                                      |                              |
|     | OIT Regional Support    | Deployment                        | Execute deployment.                                                                                                  |                              |
|     | OIT Regional Support    | Installation                      | Plan and schedule installation.                                                                                      |                              |
|     | CTT&DM NDS Project Team | Installations                     | Coordinate training.                                                                                                 |                              |
|     | OIT Regional Support    | Back-Out                          | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out). |                              |
|     | CTT&DM NDS Project Team | Post Deployment – Warranty Period | Hardware, Software and System Support.                                                                               |                              |
|     | OIT Reginal Support     | Post Deployment – Post Warranty   | Hardware, Software and System Support.                                                                               |                              |

Table 2: Software Specifications

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a concurrent online rollout. During Initial Operating Capability (IOC) testing and after National Release, patch DG\*5.3\*933 will be distributed via the FORUM Patch Module, and may be deployed at any site without regard to deployment status at other sites.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for a period of thirty days, as depicted in the master deployment schedule.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CTT&DM NDS patch DG\*5.3\*933 deployment.

The DG\*5.3\*933 patch must be manually installed, or manually queued for installation, at each VistA instance at which it is deployed, using the standard Kernel Installation Distribution System (KIDS) software. The DG\*5.3\*933 patch should be installed at all VA VistA instances running the CPRS and ADT/Registration applications, and will update the M (Mumps) server software in each VistA instance’s DG namespace.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment topology for the CTT&DM NDS patch DG\*5.3\*933, during IOC testing and after national release, is described below.

Figure 1: Patch DG\*5.3\*933 Topology

![](dg-5-3-933-ctt-dm-nds-demographics-dibrg/002.png)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During IOC testing, CTT&DM NDS patch DG\*5.3\*933 will be deployed at the following sites:

- <span class="mark">Sites redacted</span>

After national release, CTT&DM NDS patch DG\*5.3\*933 will be deployed at all sites running the CPRS and ADT/Registration applications.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special preparation is required by the site prior to deployment.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment of CTT&DM NDS patch DG\*5.3\*933 requires an up to date VistA environment running the CPRS v.1.0, ADT/Registration v5.3, and Kernel v.8.0 applications, as well as a Health Product Support (HPS) team member available to perform the patch installation.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific deployment or installation features of CTT&DM NDS patch DG\*5.3\*933.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT&DM NDS patch DG\*5.3\*933 requires no site hardware specifications during, or prior to, deployment.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software | Make | Version | Configuration | Manufacturer | Other                                          |
|-------------------|------|---------|---------------|--------------|------------------------------------------------|
| DG\*5.3\*782      |      | 5.3     | Standard      | VHA          | Direct Dependency                              |
| HDI\*1.0\*19      |      | 1.0     | Standard      | VHA          | Direct Dependency                              |
| XU\*8.0\*682      |      | 8.0     | Standard      | VHA          | Indirect Dependency (required by HDI\*1.0\*19) |

Table 3: DG\*5.3\*933 Required Builds

#### DG\*5.3\*933 Required Builds

| Required Build | Required Build Subject                 | Required Build Release Date |
|--------------------|--------------------------------------------|---------------------------------|
| DG\*5.3\*782       | UPDATE RELIGION FILE                       | 05/20/2008                      |
| HDI\*1.0\*19       | DEMOGRAPHICS NATIVE DOMAIN STANDARDIZATION | 01/19/2018                      |

Table 4: HDI\*1.0\*19 Required Builds

#### HDI\*1.0\*19 Required Builds

| Required Build | Required Build Subject      | Required Build Release Date |
|--------------------|---------------------------------|---------------------------------|
| HDI\*1.0\*6        | NEW API(S) AND BULLETIN CHECKS  | 11/21/2006                      |
| XU\*8.0\*682       | MFS PARAMETERS FOR DEMOGRAPHICS | 01/19/2018                      |

Table 5: Deployment/Installation/Back-Out Checklist

Please see Table 1 in the Roles and Responsibilities section for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No notifications are required for deployment of CTT&DM NDS patch DG\*5.3\*933.

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

It is recommended that a Local Backup Patch be created that can be re-installed in the event that patch DG\*5.3\*933 must be backed out. The approximate time to create the saved local patch is 30 minutes. The Local Backup Patch should include a full Data Definition (DD) for the following files: RACE file (#10), MARITAL STATUS file (#11), and RELIGION file (#13).

See section 7 for guidance on creating a Local Backup Patch

### Patch Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches XU\*8.0\*682 and HDI\*1.0\*19 must be installed prior to installing DG\*5.3\*933. Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx).

### Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Backup Patch Transport Global

<u>NOTE</u>: This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DD’s or templates. All of the routines in DG\*5.3\*933 are new with the patch; therefore, performing a backup and restore does not accomplish the desired result and is not a viable patch back-out strategy.

To back-up the DG\*5.3\*933 transport global, perform the following procedure:

1.  From the Kernel Installation & Distribution System menu, select the Installation menu.
2.  Select the Backup a Transport Global option.
3.  When prompted for INSTALL NAME, enter DG\*5.3\*933.
4.  Accept the default Subject by pressing Return at the “Replace:” prompt.
5.  Enter the appropriate MailMan recipients at the “Send mail to:” prompt.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*933 does not require any platform installation or preparation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT&DM NDS patch DG\*5.3\*933 is being released as a FORUM Patch via the Patch Module.

Documentation describing the new functionality introduced by this patch is available.

<span class="mark">redacted</span>

The documentation will be in the form of Adobe Acrobat files. Documentation can also be found on the VA Software Documentation Library at: https://www.va.gov/vdl/

Title: Patient Information Management System (PIMS) Technical Manual

File Name: pimstm.docx

pimstm.pdf

FTP Mode: Binary

Title: Deployment, Installation, Back-Out, Rollback Guide DG_5_3_933

File Name: dg_5_3_933_ig.docx

dg_5_3_933_ig.pdf

FTP Mode: Binary

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new database is required for the CTT&DM NDS patch DG\*5.3\*933.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are required for installation of CTT&DM NDS patch DG\*5.3\*933.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No CRON scripts are required for installation of CTT&DM NDS patch DG\*5.3\*933.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to national VA network, as well as the local network of each site to receive CTT&DM NDS patch DG\*5.3\*933 is required to perform the installation, as well as authority to create and install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, refer back to the Kernel Installation and Distribution System link found in Section <span class="mark"></span>4.1.2.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Installation Instructions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter the patch DG\*5.3\*933:
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup other changes such as data dictionaries (DD’s) or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD’s, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
6.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
7.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond NO.
8.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
9.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond NO.
10. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of CTT&DM NDS patch DG\*5.3\*933 may be verified by running the Kernel checksum tool from the VistA server command line after installation:

> D CHECK1^XTSUMBLD

The checksums produced by the checksum tool should match the numeric portion of the “After:” checksums in the CTT&DM NDS patch DG\*5.3\*933 patch description.

Example, Checksum for routines as displayed by Kernel checksum tool CHECK1^XTSUMBLD:

Select BUILD NAME: DG\*5.3\*933 REGISTRATION

DG933PO value = 27885525

DGMFA10 value = 14104060

DGMFA11 value = 14590448

DGMFA13 value = 13906961

DGMFASS value = 3776607

DGMFR10 value = 72687376

DGMFR11 value = 68721321

DGMFR13 value = 62970443

DGMFRPT value = 3969553

DGNDSU value = 33380048

DGZRT value = 36061811

\* Values may be different after national release, but should always match Patch Description checksums.

Example, matching routine checksums as displayed in FORUM Patch Description:

Routine Name: DG933PO

Before: n/a After: B27885525 \*\*933\*\*

Routine Name: DGMFA10

Before: n/a After: B14104060 \*\*933\*\*

Routine Name: DGMFA11

Before: n/a After: B14590448 \*\*933\*\*

Routine Name: DGMFA13

Before: n/a After: B13906961 \*\*933\*\*

Routine Name: DGMFASS

Before: n/a After: B3776607 \*\*933\*\*

Routine Name: DGMFR10

Before: n/a After: B72687376 \*\*933\*\*

Routine Name: DGMFR11

Before: n/a After: B68721321 \*\*933\*\*

Routine Name: DGMFR13

Before: n/a After: B62970443 \*\*933\*\*

Routine Name: DGMFRPT

Before: n/a After: B3969553 \*\*933\*\*

Routine Name: DGNDSU

Before: n/a After: B33380048 \*\*933\*\*

Routine Name: DGZRT

Before: n/a After: B36061811 \*\*933\*\*

\* Values may be different after national release, but should always match CHECK1^XTSUMBLD checksums.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration is required before or after deployment of CTT&DM NDS patch DG\*5.3\*933.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning is required before or after deployment of CTT&DM NDS patch DG\*5.3\*933.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

Perform the back-out procedure by deleting individual software components (e.g., data dictionaries, routines, options, templates) manually or via automated back out patch DG\*5.3\*00933, available from the NDS development team. The back-out is to be performed by persons with programmer-level access, and in conjunction with the STS team.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-Out Strategy consists of removing all the software components installed by DG\*5.3\*933, using of the following methods:

1.  Delete individual software components (e.g., data dictionaries, routines, options, templates) manually.

> or

11. Install automated back out KIDS build DG\*5.3\*00933, available from the NDS development team.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-Out should only be done in the event that the local facility management determines that the patch DG\*5.3\*933 is not appropriate for that facility, and should only be done as a last resort.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch DG\*5.3\*933.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Facility Management would need to determine patch DG\*5.3\*933 is not appropriate for their facility.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out DG\*5.3\*933, the local facility will not be able to use the standardized code sets from the respective Standards Development Organizations.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Local Facility Management has the authority to back-out patch DG\*5.3\*933.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

Perform the back-out procedure by deleting the software components installed with DG\*5.3\*933 using one of the following methods:

1.  Load and install the back out patch DG\*5.3\*00933 provided by the development team. This patch automatically deletes the new fields and routine(s) added by DG\*5.3\*933. The back-out is to be performed by persons with programmer-level access, and in conjunction with the STS team.
2.  If installation of back out patch DG\*5.3\*00933 cannot be done for any reason, the patch must be backed out manually by persons with programmer-level access, and in conjunction with the STS team.

The following section lists examples of the steps that would be taken to back out the patch using two methods (only one back out method needs to be executed to back out the patch). Both back out methods must be performed by persons with programmer-level access, and in conjunction with the STS team.

### Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Back Out Method 1 – Load and Install back out patch DG\*5.3\*00933

The following will need to be executed from the programmers prompt. This procedure must be performed by persons with programmer-level access, and in conjunction with the STS team.

1.  Obtain the back out patch DG\*5.3\*00933 from the NDS development team; forward to mailman account on the target VistA environment.
2.  Load patch DG\*5.3\*00933 from mailman message action Xtract KIDS, PackMan function 6 INSTALL/CHECK MESSAGE.
3.  Install back out patch DG\*5.3\*00933 using option Kernel Installation & Distribution System (KIDS) \[XPD MAIN\], Installation \[XPD INSTALLATION MENU\], Install Package(s) \[XPD INSTALL BUILD\]. Do not inhibit logons; do not disable options or protocols.

Example Installation, Back Out Patch DG\*5.3\*00933:

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INSTallation

Select Installation \<TEST ACCOUNT\> Option: INSTall Package(s)

Select INSTALL NAME: DG\*5.3\*00933 6/13/17@15:45:57

=\> DG\*5.3\*00933 backout DG\*5.3\*933

This Distribution was loaded on Jun 13, 2017@15:29:48 with header of

DG\*5.3\*00933 backout DG\*5.3\*933

Checking Install for Package DG\*5.3\*00933

Install Questions for DG\*5.3\*00933

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TERMINAL

DG\*5.3\*00933

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Deleting Option DGMF AMAIN

Deleting Option DGMF MENU

Deleting Option DGMF RMAIN

Deleting Input Template \[DGMF AMREL\]

Deleting Input Template \[DGMF AMSTAT\]

Deleting Input Template \[DGMF ARACE\]

Deleting Field \#90 in File 10

Deleting Field \#90 in File 11

Deleting Field \#90 in File 13

Deleting routine ^DG933PO

Deleting routine ^DGMFA10

Deleting routine ^DGMFA11

Deleting routine ^DGMFA13

Deleting routine ^DGMFASS

Deleting routine ^DGMFR10

Deleting routine ^DGMFR11

Deleting routine ^DGMFR13

Deleting routine ^DGMFRPT

Deleting routine ^DGNDSU

Deleting routine ^DGZRT

Deleting File 10.99

Deleting the DATA DICTIONARY...

Deleting File 11.99

Deleting the DATA DICTIONARY...Deleting File 13.99

Deleting the DATA DICTIONARY...

Updating KIDS files...

DG\*5.3\*00933 Installed.

Jun 13, 2017@15:35:51

−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−

100% . 25 50 75 .

Complete −−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−

Install Completed

#### Back Out Method 2 – Manually delete Patch Software Components

The following involves manual deletion of DD’s and routines, and will need to be executed from the programmers prompt. This procedure must be performed by persons with programmer-level access, and in conjunction with the STS team.

#### Manual Deletion of Data Dictionaries

Use VA FileMan to delete the new fields added with DG\*5.3\*933, using the following general steps:

1.  Select the FileMan option MODIFY FILE ATTRIBUTES.
12. At the prompt “Modify what File:”, enter the file name or number.
13. At the prompt “Select FIELD:”, enter the field name.
14. At the “Label:” prompt, enter “@”.
15. When prompted “OK TO DELETE ‘*FIELD NAME’* FIELD IN EXISTING ENTRIES?” enter YES. This will automatically also remove all sub-fields and data.

Delete the following field from the RACE file (#10):

- RACE MASTER (#99)

Delete the following field from the MARITAL STATUS file (#11):

- MASTER MARITAL STATUS (#99)

Delete the following fields from the RELIGION file (#13):

- MASTER RELIGION (#99)

Example, Manual deletion of DD’s from RACE file (#10) using FileMan. This process must be repeated for MARITAL STATUS file (#11) and RELIGION file (#13), see list of fields to be deleted above:

D P^DI

Select OPTION: MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES// NO

MODIFY WHAT FILE: // RACE (#10) (15 entries)

Select FIELD: RACE MASTER

LABEL: RACE MASTER// @

SURE YOU WANT TO DELETE THE ENTIRE 'RACE MASTER' FIELD? Y (Yes)

OK TO DELETE ‘RACE MASTER' FIELDS IN THE EXISTING ENTRIES? Yes// Y (Yes).....

#### Manual Deletion of Files

VA FileMan cannot be used to delete the files added with DG\*5.3\*933, as the files are protected against deletion using FileMan. Therefore, the files must be deleted from the programmer prompt using the following commands:

#### Commands to delete the new RACE MASTER file (#10.99):

1.  Type the following at the programmer prompt: S FILE=10.99
16. Type the following at the programmer prompt: S DIU=\$G(^DIC(FILE,0,"GL"))
17. Type the following at the programmer prompt: S DIU(0)="DES"
18. Type the following at the programmer prompt: D EN^DIU2

#### Commands to delete the new MASTER MARITAL STATUS file (#11.99):

1.  Type the following at the programmer prompt: S FILE=11.99
19. Type the following at the programmer prompt: S DIU=\$G(^DIC(FILE,0,"GL"))
20. Type the following at the programmer prompt: S DIU(0)="DES"
21. Type the following at the programmer prompt: D EN^DIU2

#### Commands to delete the new MASTER RELIGION file (#13.99):

1.  Type the following at the programmer prompt: S FILE=10.99
22. Type the following at the programmer prompt: S DIU=\$G(^DIC(FILE,0,"GL"))
23. Type the following at the programmer prompt: S DIU(0)="DES"
24. Type the following at the programmer prompt: D EN^DIU2

#### Manual Deletion of Routine(s)

The deletion of a routine is a potentially dangerous activity. This procedure must be performed by persons with programmer-level access, and in conjunction with the STS team.

1.  From the ROUTINE MANAGEMENT MENU \[XUROUTINES\], select the DELETE ROUTINES \[XTRDEL\] option. IMPORTANT: When prompted for ‘All Routines?’ enter NO.
25. At the ‘Routine:’ prompt, enter DG933PO.
26. At the next ‘Routine:’ prompt enter DGMFA10.
27. At the next ‘Routine:’ prompt, enter DGMFA11.
28. At the next ‘Routine:’ prompt, enter DGMFA13.
29. At the next ‘Routine:’ prompt, enter DGMFASS.
30. At the next ‘Routine:’ prompt, enter DGMFR10.
31. At the next ‘Routine:’ prompt, enter DGMFR11.
32. At the next ‘Routine:’ prompt, enter DGMFR13.
33. At the next ‘Routine:’ prompt, enter DGMFRPT.
34. At the next ‘Routine:’ prompt, enter DGNDSU
35. At the next ‘Routine:’ prompt, enter DGZRT.
36. At the next ‘Routine:’ prompt, press \<enter\> (no routine).
37. At the prompt ‘11 routines to DELETE, OK:’ enter YES.

Example, deleting routines using option DELETE ROUTINES \[XTRDEL\]:

Select OPTION NAME: ROUTINE MANAGEMENT MENU XUROUTINES Routine Management Menu

Bring in Sent Routines

Delete Routines

First Line Routine Print

List Routines

Move Routines across Volume Sets

Select OPTION NAME: DELETE ROUTINES XTRDEL Delete Routines

Delete Routines

ROUTINE DELETE

All Routines? No =\> No

Routine: DG933PO

Routine: DGMFA10

Routine: DGMFA11

Routine: DGMFA13

Routine: DGMFASS

Routine: DGMFR10

Routine: DGMFR11

Routine: DGMFR13

Routine: DGMFRPT

Routine: DGNDSU

Routine: DGZRT

Routine:

11 routines

10 routines to DELETE, OK: NO// Y

DG933PO DGMFA10 DGMFA11 DGMFA13 DGMFASS DGMFR10 DGMFR11 DGMFR13

DGMFRPT DGNDSU

Done

#### Manual Deletion of Options

The options installed with patch DG\*5.3\*933 may be deleted using VA FileMan option ENTER OR EDIT FILE ENTRIES, using the following steps:

1.  Select the ENTER OR EDIT FILE ENTRIES option in VA FileMan.
38. At the prompt ‘Input to what File:’, enter OPTION.
39. At the prompt ‘EDIT WHICH FIELD’, accept the default ‘ALL’.
40. At the prompt ‘Select OPTION NAME:’, enter DGMF MENU.
41. At the prompt ‘NAME:’, enter the ‘at’ symbol @.
42. At the prompt ‘SURE YOU WANT TO DELETE THE ENTIRE ‘DGMF MENU’ OPTION?’ enter Y.
43. At the prompt ‘DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)?’, enter N.
44. Repeat steps 1-7 for options DGMF AMAIN and DGMF RMAIN (entered at step 4).

Example, deleting options using FileMan option ENTER OR EDIT FILE ENTRIES:

VA FileMan 22.2

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: OPTION// (11403 entries)

EDIT WHICH FIELD: ALL//

Select OPTION NAME: DGMF MENU Master Demographics Files

NAME: DGMF MENU// @

SURE YOU WANT TO DELETE THE ENTIRE 'DGMF MENU' OPTION? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// (No)

Select OPTION NAME: DGMF AMAIN Master File Association Enter/Edit

NAME: DGMF AMAIN// @

SURE YOU WANT TO DELETE THE ENTIRE 'DGMF AMAIN' OPTION? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// (No)

Select OPTION NAME: DGMF RMAIN Master File Reports

NAME: DGMF RMAIN// @

SURE YOU WANT TO DELETE THE ENTIRE 'DGMF RMAIN' OPTION? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// (No)

#### Manual Deletion of Input Templates

The Input Templates installed with patch DG\*5.3\*933 may be deleted using VA FileMan option ENTER OR EDIT FILE ENTRIES, using the following steps:

1.  Select the ENTER OR EDIT FILE ENTRIES option in VA FileMan.
45. At the prompt ‘Input to what File:’, enter INPUT TEMPLATE.
46. At the prompt ‘EDIT WHICH FIELD’, accept the default ‘ALL’.
47. At the prompt ‘Select OPTION NAME:’, enter DGMF AMREL.
48. At the prompt ‘NAME:’, enter the ‘at’ symbol @.
49. At the prompt ‘SURE YOU WANT TO DELETE THE ENTIRE ‘DGMF AMREL’ INPUT TEMPLATE?’ enter Y.
50. At the prompt ‘DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)?’, enter N.
51. Repeat steps 1-7 for Input Templates DGMF AMSTAT and DGMF ARACE (entered at step 4).

Example, deleting Input Templates using FileMan option ENTER OR EDIT FILE ENTRIES:

VA FileMan 22.2

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: INPUT TEMPLATE// (1843 entries)

EDIT WHICH FIELD: ALL//

Select INPUT TEMPLATE: DGMF AMREL (AUG 15, 2017@16:50) File \#13

NAME: DGMF AMREL// @

SURE YOU WANT TO DELETE THE ENTIRE 'DGMF AMREL' INPUT TEMPLATE? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// (No)

Select INPUTE TEMPLATE: DGMF AMSTAT (AUG 15, 2017@16:49) File \#11

NAME: DGMF AMSTAT// @

SURE YOU WANT TO DELETE THE ENTIRE 'DGMF AMSTAT' OPTION? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// (No)

Select INPUT TEMPLATE: DGMF ARACE (AUG 15, 2017@16:42) File \#10

NAME: DGMF ARACE// @

SURE YOU WANT TO DELETE THE ENTIRE 'DGMF ARACE' OPTION? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// (No)

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out patch DG\*5.3\*933 by installing the local patch from section 4.1, routine back-out may be verified by running the Kernel checksum tool from the VistA server command line after installation:

D CHECK1^XTSUMBLD

1.  At the ‘Build from:’ prompt, enter “Build”.
2.  At the ‘Select BUILD NAME:’ prompt, enter DG\*5.3\*933.

The new routine(s) installed by DG\*5.3\*933 should display the message ‘Routine not in this UCI’.

Example, running CHECK1^XTSUMBLD for build DG\*5.3\*933 to verify back out:

D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: DG\*5.3\*933 REGISTRATION

DG933PO Routine not in this UCI.

DGMFA10 Routine not in this UCI.

DGMFA11 Routine not in this UCI.

DGMFA13 Routine not in this UCI.

DGMFASS Routine not in this UCI.

DGMFR10 Routine not in this UCI.

DGMFR11 Routine not in this UCI.

DGMFR13 Routine not in this UCI.

DGMFRPT Routine not in this UCI.

DGNDSU Routine not in this UCI.

DGZRT Routine not in this UCI.

done

### Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out Patch DG\*5.3\*933, successful deletion of new fields installed by DG\*5.3\*933 may be verified by running a global listing from the VistA server command line. A global listing should be performed for the following global nodes, after which nothing should be listed if back-out was successful:

- Global ^DD(10,90
- Global ^DD(11,90
- Global ^DD(13,90
- Global ^DD(10.99
- Global ^DD(11.99
- Global ^DD(13.99
- Global ^DGRAM
- Global ^DGMMS
- Global ^DGMR

Example, running D ^%G global list to verify new fields have been deleted:

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global ^DD(10,90 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(11,90 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(13,90 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(10.99 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(11.99 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(13.99 – NOTE: translation in effect

\<nothing should print\>

Global ^DGRAM -- NOTE: translation in effect

\<nothing should print\>

Global ^DGMMS -- NOTE: translation in effect

\<nothing should print\>

Global ^DGMR – NOTE: translation in effect

\<nothing should print\>

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out Patch DG\*5.3\*933, successful deletion of new options installed by DG\*5.3\*933 may be verified by using VA FileMan option INQUIRE TO FILE ENTRIES.

The following steps should be taken to verify successful deletion of options:

1.  Select FileMan option INQUIRE TO FILE ENTRIES.
52. At the prompt ‘Output from what File:’ enter OPTION.
53. At the prompt ‘OPTION NAME:’ enter DGMF.
54. Two question marks should display ‘??’, indicating no options beginning with DGMF were found.

Example, running D ^%G global list to verify new options have been deleted:

VA FileMan 22.2

Select OPTION: INQUIRE TO FILE ENTRIES

Output from what File: OPTION// OPTION

1 OPTION (11403 entries)

2 OPTION SCHEDULING (120 entries)

CHOOSE 1-2: 1 OPTION (11403 entries)

Select OPTION NAME: DGMF ??

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out Patch DG\*5.3\*933, successful deletion of new Input Templates installed by DG\*5.3\*933 may be verified using VA FileMan option INQUIRE TO FILE ENTRIES.

The following steps should be taken to verify successful deletion of Input Templates:

1.  Select FileMan option INQUIRE TO FILE ENTRIES.
2.  At the prompt ‘Output from what File:’ enter INPUT TEMPLATE.
3.  At the prompt ‘OPTION NAME:’ enter DGMF.
4.  Two question marks should display ‘??’, indicating no Input Templates beginning with DGMF were found.

Example, running D ^%G global list to verify new Input Templates have been deleted:

VA FileMan 22.2

Select OPTION: INQUIRE TO FILE ENTRIES

Output from what File: INPUT TEMPLATE// INPUT TEMPLATE (2095 entries))

Select INPUT TEMPLATE: DGMF ??

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

# Creating a Local Backup Patch File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following procedure to create a *Local Backup Patch File*.

55. Create a local KIDS patch.
56. From the KIDS (Kernel Installation & Distribution System) menu.
57. Select ‘Edits and Distribution’.
58. Select ‘Create a Build Using Namespace’.
59. Enter a local patch name and identifier; (for example: ZZZ\*1.0\*004).
60. At ‘BUILD PACKAGE FILE LINK:’ press \<enter\>.
61. At ‘BUILD TYPE: SINGLE PACKAGE//’ press \<enter\>.
62. At ‘BUILD TRACK PACKAGE NATIONALLY: YES//’ enter NO.
63. At ‘Namespace:’ press \<enter\>.
64. At the menu select ‘Edit a Build’.
65. Enter the ‘*local package name and identifier*’ that was created in Step 5.
66. For the ‘Description:’ enter the following: “this is a local patch save for DD files 10, 11, and 13. This patch is only to be re-loaded in the event that the DG\*5.3\*933 patch needs to be backed-out.
67. Select ‘Next Page’.
68. For ‘File List’ enter 10 for RACE file (#10)
69. Send Full or Partial DD...: FULL.
70. Update the Data Dictionary: YES.
71. Send Security Code: YES.
72. Data Comes With File...: NO
73. At ‘COMMAND:’ enter ‘Close’
74. Repeat steps 18 – 23 for the MARITAL STATUS file (#11) and RELIGION file (#13).
75. Up arrow to the ‘COMMAND:’ prompt
76. Enter ‘Next Page’.
77. Enter ‘Save’.
78. Enter ‘Exit’ .
79. On the menu select ‘Transport a Distribution’.
80. Enter the ‘local package name and identifier’ that was created in Step 5.
81. At the ‘Another Package Name:’ press \<enter\>.
82. At the ‘OK to continue? YES//’ press \<enter\>.

### Creating an HF Transport

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following procedure to create an ‘*HF’ TRANSPORT*.

1.  At the ‘Transport through (HF) Host File or (PM) PackMan:’ enter HF.
2.  At the ‘Enter a Host File:’ enter the system file name that will hold the local patch; (for example: ZZZ_1-0_004.KID).
3.  At the ‘Header Comment:’ enter Local patch for Demographics.
4.  At the menu press \<enter\>.
5.  At the KIDS menu press \<enter\>.

### Creating a PM Transport

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following procedure to create a‘*PM*’ *TRANSPORT*.

1.  At the ‘Transport through (HF) Host File or (PM) PackMan:’ enter PM.
2.  At the ‘Header Comment:’ enter Local patch for Demographics.
3.  For the description of Packman Message enter:

    ‘This is a saved backup for the Demographics patch install for DG\*5.3\*933. This local build will be used in the event that the above mentioned install needs to be backed off.’
4.  At ‘EDIT Option:’ press \<enter\>.
5.  At the ‘Do you wish to secure this message? NO//’ enter ‘NO’.
6.  At the ‘Send mail to:’ enter your name.
7.  At the ‘Select basket to send to: IN//’ press \<enter\>.
8.  At the ‘And Send to:’ enter any additional persons that may need to have the local patch.

At The ‘Select Edits and Distribution \<TEST ACCOUNT\> Option:’ press \<enter\>.