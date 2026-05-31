---
title: DG*5.3*1057 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*1057
group_key: ADT:DG:5.3
file_numbers: []
security_keys:
- XUPROG
- XUPROGMODE
menu_options: 0
description: Community Care (CC) Integrated Billing (IB) and Accounts Receivable
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 2778
section_count: 31
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: December 2021
revision_count: 1
revision_newest: 12/20/2021
revision_oldest: 12/20/2021
docx_url: https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/dg_5_3_1057_dibr.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/dg_5_3_1057_dibr.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=55
audit_applied: '2026-05-31'
master_source: DG*5.3*1057 Deployment, Installation, Back-Out, and Rollback Guide
master_pub_date: December 2021
consolidated_from: 3 versions
prior_versions:
- DG*5.3*1080 Deployment, Installation, Back-Out, and Rollback Guide
- DG*5.3*1102 Deployment, Installation, Back-out, and Rollback Guide
consolidated_title: deployment, installation, back-out, and rollback guide
---

Community Care (CC) Integrated Billing (IB) and Accounts Receivable (AR)

Registration DG\*5.3\*1057

Deployment, Installation, Back-Out, and Rollback Guide (DIBR)

![](dg-5-3-1057-deployment-installation-back-out-and-rollback-guide/001.png)

December 2021

Office of Information and Technology (OIT)

Revision History

| Date       | Version | Description     | Author                   |
|------------|---------|-----------------|--------------------------|
| 12/20/2021 | 1.0     | Initial release | CC IBAR Development Team |

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

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
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
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
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the Community Care Registration Enhancements patch DG\*5.3\*1057 as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Community Care Registration Enhancements patch DG\*5.3\*1057 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed prior to installing DG\*5.3\*1057:

- DG\*5.3\*884
- DG\*5.3\*912
- DG\*5.3\*1020

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is intended for a fully patched Veterans Health Information Systems and Technology Architecture (VistA) system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment, installation, back-out, and rollback roles and responsibilities are shown in Table 1.

| Team                                                                                                                        | Phase / Role    | Tasks                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|
| Health Product Support                                                                                                      | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                 |
| Health Product Support and existing local VA Medical Center (VAMC) and Consolidated Patient Account Center (CPAC) processes | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                          |
| Health Product Support and Veteran-focused Integrated Process (VIP) Release Agent                                           | Deployment      | Test for operational readiness                                                                                      |
| Health Product Support                                                                                                      | Deployment      | Execute deployment                                                                                                  |
| Designated VistA patch installer for this package                                                                           | Installation    | Plan and schedule installation                                                                                      |
| Designated VistA patch installer for this package and VIP Release Agent                                                     | Installation    | Ensure authority to operate and that certificate authority security documentation is in place                       |
| CPAC Revenue Analysts                                                                                                       | Installations   | Coordinate training                                                                                                 |
| Designated VistA patch installer for this package, and CPAC Revenue Analysts, Health Product Support, and Development Team  | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |
| Product Development Team during warranty period, afterwards (software only) Tier 1, Tier 2, Tier 3 / VistA Maintenance      | Post Deployment | Hardware, Software, and System Support                                                                              |

Table 2: Deployment/Installation/Back-Out Checklist

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a simultaneous national rollout to all 130 VistA production instances. This section provides the schedule and milestones for the deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for two days starting with the National Release date and concluding with the National Compliance date by which time all 130 VistA production instances should have the patch installed.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Community Care Registration patch DG\*5.3\*1057 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment topology (targeted architecture) is not applicable for a VistA patch.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The test sites for IOC testing are:

- Richard L. Roudebush VA Medical Center - Station 583
- VA Western New York Healthcare System - Buffalo - Station 528

Upon national release, all VAMCs are expected to install this patch prior to or on the compliance date. The software will be distributed in FORUM.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch does not require any site preparations other than the prerequisite patch installation as described in the Patch Description and in the National Patch Module (NPM)in Forum.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Community Care Registration patch DG\*5.3\*1057 is a VistA patch and does not require any special or specific resources other than an existing and functional VistA system.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific hardware required other than that which already hosts the VistA system. This is a software enhancement that will not require additional hardware.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific software required other than that which already hosts the VistA system.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA patches are nationally released from the Forum NPM the patch is automatically sent to the targeted VistA systems nationwide. When VistA patches are installed at a site, a notification is sent back to the NPM to track which sites have and have not installed a patch. This is part of the standard VistA patch notifications and communications protocols.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch DG\*5.3\*1057, which is tracked in the NPM in Forum, nationally to all VAMCs. Forum automatically tracks the patches as they are installed in the different VAMC production systems as described in the previous section. One can run a report in Forum to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not installed the patch in their VistA production system as of that moment in time.

Therefore, this information does not need to be manually tracked. The table is included below if manual tracking is desired and because it is part of the VIP document template.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | TBD | TBD  | TBD                           |
| Install  | TBD | TBD  | TBD                           |
| Back-Out | TBD | TBD  | TBD                           |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. The only pre-installation and system requirements for deployment and installation of this patch are the prerequisite patches which need to be installed before this patch can be installed.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch.

Sites should install patches into the test/mirror/pre-prod accounts before the production account as is the normal VistA patch installation standard convention.

When installing any VistA patch, sites should utilize the option "Backup a Transport Global" in order to create a backup message of any routines exported with this patch.

Post-installation checksums are found in the Patch Description and in Forum NPM.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download and extract files are not applicable for this VistA patch.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database creation is not applicable for this VistA patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation scripts are not applicable for this VistA patch.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cron scripts are not applicable for this VistA patch.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install this VistA patch, the patch installer must be an active user on the VistA system and have access to the VistA menu option "Kernel Installation & Distribution System" \[XPD MAIN\] and have VistA security keys XUPROG and XUPROGMODE. Knowledge on how to install VistA patches using the items on this menu option is also a required skill.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch: DG\*5.3\*1057.
    2.  Select the Backup a Transport Global option to create a backup message of any routines exported with this patch. For each patch you can specify what to backup, the entire Build or just Routines. When asked to specify what to backup, select Build. It is NOT recommended to use this backup to restore the system as it will NOT restore your system to pre-patch condition.

> When prompted for a response, select Routines.

> Select one of the following:

> B Build

> R Routines

> Enter response: Routines

> Do you wish to secure this message? NO// NO

3.  You may also elect to use the following options:
    1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
    1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//', answer NO.
    2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
    3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify completed installation by comparing the post-install routine checksums against the published checksums in the Patch Description and in Forum NPM.

Another verification method is to ensure that the build components as listed in the Patch Description have been correctly installed onto the target VistA system.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System configuration is not applicable for this VistA patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database tuning is not applicable for this VistA patch.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installing the updated KIDS package, the site/region should have saved a backup of the routines in a mail message using the Backup a Transport Global \[XPD BACKUP\] menu option. The message containing the backed-up routines can be loaded with the "Xtract PackMan" function at the Message Action prompt. The PackMan function INSTALL/CHECK MESSAGE is then used to install the backed-up routines onto the VistA system.

The development team recommends that sites log a ticket if it is a nationally released patch; otherwise, the site should contact the Enterprise Program Management Office (EPMO) directly for specific solutions to their unique problems.

Although it is unlikely due to care in collecting approved requirements, Software Quality Assurance (SQA) review and multiple testing stages (Unit testing, Component Integration Testing, User Acceptance Testing) a back-out decision due to major issues with this patch could occur during site Mirror Testing, Site Production Testing or after National Release to the Field. The strategy would depend on during which of these stages the decision is made. If during Site Production Testing, unless the patch produces catastrophic problems, the normal VistA response would be for a new version of the test patch correcting defects to be produced, retested and upon successfully passing development team testing would be resubmitted to the site for testing. If the defects were not discovered until after national release but during the 30 days support period, a new patch will be entered into the National Patch Module on Forum and go through all the necessary milestone reviews etc. as an emergency patch.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if a wholesale back-out of the patch DG\*5.3\*1057 is needed or if a better course of action is to correct through a new version of the patch (if prior to national release) or through a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale back-out of the patch will still require a new version (if prior to national release) or a subsequent patch (after national release). If the back-out is post-release of patch DG\*5.3\*1057, this patch should be assigned status of "Entered in Error" in Forum's NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load testing is not applicable for this VistA patch.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is detailed in the User Stories in Rally.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to back-out this VistA patch will be made by Health Product Support, CPAC Revenue System Management staff, and the Development Team. Criteria to be determined based on separate and unique factors and will be evaluated upon post-patch installation use of the product.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out risks are not applicable for this VistA patch.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out authorization will be determined by a consensus consisting of the following individuals:

- Health Product Support Management –
  - Primary: redacted
  - Primary: redacted
  - Secondary: redacted
- CPAC Revenue System Managers –
  - Primary: redacted
  - Secondary: redacted
- Development Team –
  - Primary: redacted
  - Secondary: redacted

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out procedure for VistA applications is complex and not a "one size fits all" solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch. If not, the site should contact the EPMO team directly for specific solutions to their unique problems.

The DG\*5.3\*1057 patch contains the following build components.

- Routines
- Data Dictionaries
- Options

While the VistA installation procedure of the Kernel Installation and Distribution System (KIDS) build allows the installer to back up the modified routines using the 'Backup a Transport Global' action, the back-out procedure for global, data dictionary and other VistA components is more complex and requires issuance of a follow-up patch to ensure all components are properly removed and/or restored. All software components (routines and other items must be restored to their previous state at the same time and in conjunction with the restoration of the data.

Please contact the EPMO team for assistance since this installed patch contains components in addition to routines.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The success of the back-out can be verified by verifying checksums for the routines removed to validate that they reflect the nationally released checksums.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data associated with this patch.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DG*5.3*1080 Deployment, Installation, Back-Out, and Rollback Guide

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site | Space / Room | Features Needed | Other |
|------|--------------|-----------------|-------|
| N/A  | N/A          | N/A             | N/A   |

<span id="_Toc116482107" class="anchor"></span>Table 4: Hardware Specifications
