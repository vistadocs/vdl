---
title: Electronic Health Modernization IFC (GMRC*3.0*189) Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
section: CLI
app_status: active
pkg_ns: GMRC
patch_ver: 3.0
patch_id: GMRC*3.0*189
group_key: "GMRC:GMRC:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - back
  - patch
  - deployment
  - rollback
  - vista
  - procedure
  - build
page_count: 0
word_count: 2819
section_count: 32
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/gmrc_3_189_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/gmrc_3_189_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

Electronic Health Modernization

IFC Proxy Add/Order Resubmission 1.0

Deployment, Installation, Back-Out, and Rollback Guide

![](electronic-health-modernization-ifc-gmrc-3-0-189-deployment-installation-back-ou/001.png)

November 2024

Office of Information and Technology

Revision History

| Date    | Version | Description   | Author  |
|---------|---------|---------------|---------|
| 11/2024 | 1.0     | Initial draft | EHRM-IO |

<span id="_Ref12518168" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback (DIBR) Guide for new products going into the Department of Veterans Affairs (VA) Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single location or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the DIBR Guide is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

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
    - [Deployment/Installation/Back-Out Checklist](#deploymentinstallationback-out-checklist)
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
  - [Post-Installation Instructions](#post-installation-instructions)
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
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document is intended to guide the VA Medical Center (VAMC) Information Resources Management (IRM) Specialist or VA Testing Center engineer in the installation of the IFC Proxy Add/Order Resubmission multi-build. The build consists of four (4) patches: 1) DG\*5.3\*1096, 2) EHM\*1\*10, 3) GMRC\*3\*189 and 4) DG\*5.3\*1091. DG\*5.3\*1096 and DG\*5.3\*1091 are components of the Registration (DG) package. EHM\*1\*10 is a component of the Electronic Health Modernization (EHM) package. GMRC\*3\*189 is a component of the Consult/Request Tracking (GMRC) package.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to describe how, when, where, and to whom the IFC Proxy Add/Order Resubmission multi-build is deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The document also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc411336919" class="anchor"></span>The following patches must be installed before proceeding with installation of this multi-build:

- GMRC\*3\*169, GMRC\*3\*185, GMRC\*3\*202
- DG\*5.3\*1005, DG\*5.3\*1037

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints for this patch.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment, installation, back-out, and rollback roles and responsibilities are shown in Table 1.

<table>
<caption><p><span id="_Toc2267867" class="anchor"></span>Table 2: Deployment/Installation/Back-Out Checklist</p></caption>
<colgroup>
<col style="width: 36%" />
<col style="width: 18%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>Team</th>
<th>Phase / Role</th>
<th>Tasks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EHRM-IO Deployment Team, VistA Team</td>
<td>Deployment</td>
<td>Plan and schedule deployment</td>
</tr>
<tr class="even">
<td>EHRM-IO Deployment Team, VistA Team</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
</tr>
<tr class="odd">
<td>EHRM-IO Deployment Team, VistA Team</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="even">
<td>EHRM-IO Deployment Team, VistA Team</td>
<td>Deployment</td>
<td>Execute deployment</td>
</tr>
<tr class="odd">
<td>Site-specific Regional IT Team</td>
<td>Installation</td>
<td>Plan and schedule installation</td>
</tr>
<tr class="even">
<td>Site-specific Regional IT Team</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
</tr>
<tr class="odd">
<td>Site-specific Regional IT Team</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
</tr>
<tr class="even">
<td><p>EHRM-IO Deployment Team, VistA Team</p>
<p>Product Development Team during warranty period, afterwards (software only) Tier 1, Tier 2, Tier 3 / VistA Maintenance</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
</tr>
</tbody>
</table>

<span id="_Toc2267867" class="anchor"></span>Table 2: Deployment/Installation/Back-Out Checklist

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch will be released nationally subject to the standard patching procedures.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TBD

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch will be deployed to all Veterans Health Information Systems and Technology Architecture (VISTA) production instances. The IOC test sites are the Chalmers P. Wylie Ambulatory Care Center (Columbus, Ohio) and VA Portland Health Care System (Portland, Oregon and Vancouver, Washington).

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IFC Proxy Add/Order Resubmission multi-build does not require any special or specific resources at a VistA system. The EHM\*1\*10 patch adds a new file – EHRM HL7 Message (#1609). This will have no measurable impact on database size, and older records will be regularly purged. The GMRC\*3\*189 patch expands the size of the REMOTE RESULT FILE ENTRY field (#.06) to the REQUEST/CONSULTATION file (#123) from 12 to 20 characters. This will have no measurable impact on database size.

## Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific hardware required other than that which already hosts the VistA system. This is a software enhancement that will not require additional hardware.

## Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific software required other than that which already hosts the VistA system.

## Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch changes the content of selected HL7 messages but does not impact the manner that these messages are sent or received.

### Deployment/Installation/Back-Out Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release Management team will deploy the IFC Proxy Add/Order Resubmission multi-build.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | TBD | TBD  | TBD                           |
| Install  | TBD | TBD  | TBD                           |
| Back-Out | TBD | TBD  | TBD                           |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software for this build is being released in a host file named IFC_PROXY_ADD_ORDER_RESUBMISSION.KID. There are no pre-installation actions required of the installer. There is one post-installation action required of the installer. It is detailed below.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patches listed below are required builds for the IFC Proxy Add/Order Resubmission multi-build. They are already installed at all production sites.

1.  <span id="_Toc89853119" class="anchor"></span>GMRC\*3\*169
2.  GMRC\*3\*185
3.  GMRC\*3\*202
4.  DG\*5.3\*1005
5.  DG\*5.3\*1037

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a set of VistA patches. Sites should install the build into the test/mirror/pre-prod accounts before the production account as is the normal VistA patch installation standard convention.

When installing any VistA patch, sites should utilize the option “Backup a Transport Global” to create a backup message of any routines exported with this patch.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install this VistA patch, the patch installer must be an active user on the VistA system and have access to the VistA menu option, “Kernel Installation & Distribution System” \[XPD MAIN\] and have VistA security keys XUPROG and XUPROGMODE. Knowledge on how to install VistA patches using the items on this menu option is also a required skill.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 30 minutes to install. This patch should not be queued.

Installation Instructions:

1.  Use the Load a Distribution option contained on the Kernel Installation

and Distribution System Menu to load the Host file.

When prompted to "Enter a Host File:" enter /srv/vista/patches/SOFTWARE/IFC_PROXY_ADD_ORDER_RESUBMISSION.KID

2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name IFC PROXY ADD/ORDER RESUBMISSION 1.0.
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option for each patch contained in the Host File. For each patch you can specify what to backup, the entire Build or just Routines. The backup message can be used to restore just the routines or everything that will restore your system to pre-patch condition.
    3.  You may also elect to use the following options:
        1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all the components of this patch, such as routines, DDs, templates, etc.
    4.  Select the Install Package(s) option and choose the patch to install.
1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
3.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify completed installation by checking that the build components as listed in the patch description have been correctly installed onto the target VistA system.

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After patch installation has completed, restart the HL7 incoming filers.

Use the Monitor, Start, Stop Filers \[HL FILER MONITOR\] option on the Filer and Link Management Options \[HL MENU FILER LINK MGT\] menu on the HL7 Main Menu \[HL MAIN MENU\].

In TaskMan, schedule the EHMHL7 PURGE option to run daily during

off-peak hours. Retention periods are initially set during patch load to 30 days but can be customized at each VistA site by editing the RETENTION field (#1) for the EHRM HL7 Message file (#1609) using FileMan.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out procedures pertain to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-Out Strategy for VistA applications is complex and is not able to be a “one size fits all” strategy. The general strategy for VistA software back-out is to repair the code with a follow-up patch. The site should contact the Enterprise Program Management Office (EPMO) directly for specific solutions to their unique problems. 

Although it is unlikely due to care in collecting approved requirements, software quality analyst (SQA) review and multiple testing stages (Primary Developer, Secondary Developer, and Component Integration Testing) a back-out decision due to major issues with this patch could occur during site Mirror Testing, Site Production Testing or after Release to the Field. The strategy would depend on during which of these stages the decision is made. If the decision is made during Site Production Testing, the normal VistA response would be for a new version of the test patch to be produced to correct defects, unless the patch produces catastrophic problems. The test patch would be retested and upon successfully passing development team testing would be resubmitted to the site for testing.  If the defects were not discovered until after release, OEHRM would produce the new patch, either to correct the defective components or to back-out. 

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if a wholesale back-out of the build is needed or if correcting through a new version of the build is a better course of action. A wholesale back-out of the patch will still require a new version.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to back-out this VistA multi-build will be made by the Business Sponsor, EHRM-IO VA Leadership, VA OIT IT Program Manager, and the Development Team. Criteria will be determined based on separate and unique factors and will be evaluated upon post-patch installation use of the product.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on authority provided by the Business Sponsor, EHRM-IO VA Leadership and VA OIT IT Program Manager, the build can be backed out in accordance to their approval.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*WARNING: Use caution in performing these steps. Deletions cannot be undone!There is no harm in leaving the build installed. As long as no other application calls the new API, then the routine will never be run.  
*

Removing the build from a site can be done by installing the backups of the four (4) patches created during patch installation.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routines listed in the patch descriptions can be checked to see that the associated patch number is not present in line 2 of each routine. File \#1609 can be checked to see that it is not present using FileMan to list the data dictionary.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data associated with this patch.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch does not supply or convert any data.

The decision to rollback this VistA patch will be made by the Business Sponsor, Electronic Health Record Modernization – Integration Office (EHRM-IO) VA Leadership, VA OIT IT Program Manager, and the Development Team. Criteria will be determined based on separate and unique factors and will be evaluated upon post-patch installation use of the product.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback risks include being able to restore the database to how it looked before this patch was installed without introducing database corruption.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on authority provided by the Business Sponsor, EHRM-IO VA Leadership and VA OIT IT Program Manager, the build can be rolled back in accordance to their approval.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new build to fix the problems should be developed.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that all the above data components have been removed from the system as described in the previous section.