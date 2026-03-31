---
title: MDT Phase 1 PSJ*5*445, TIU*1*360, and OR*3*618 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: MDT Phase 1 PSJ*5*445, TIU*1*360, and OR*3*618
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5.445
patch_id: PSJ*5.445*445
group_key: "PSJ:PSJ:5.445"
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
  - rollback
  - procedure
  - deployment
  - class
  - team
  - software
page_count: 0
word_count: 2439
section_count: 31
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_445_tiu_1_360_or_3_618_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_445_tiu_1_360_or_3_618_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  MDT Phase 1

  PSJ\*5\*445, TIU\*1\*360, and OR\*3\*618

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](mdt-phase-1-psj-5-445-tiu-1-360-and-or-3-618-deployment-installation-back-out-an/001.png)

March 2025

Office of Information and Technology (OIT)

Revision History

| Date | Version | Description | Author           |
|----------|-------------|-----------------|----------------------|
| 03/2025  |             | Initial Release | MDT Development Team |

Table 2: Deployment/Installation/Back-Out Checklist

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

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
    - [Deployment Topology (Targeted Architecture)](#deployment-topology-targeted-architecture)
  - [Resources](#resources)
    - [Software](#software)
    - [Communications](#communications)
- [Pre-Installation Steps](#pre-installation-steps)
  - [Backup Procedures](#backup-procedures)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation](#installation-1)
    - [Mandatory Pre-Installation Sequence](#mandatory-pre-installation-sequence)
    - [Mandatory Installation Sequence](#mandatory-installation-sequence)
  - [Installation Procedure(s)](#installation-procedures)
    - [PSJ5445TIU1360OR3618.KID](#psj5445tiu1360or3618kid)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Post-Installation](#post-installation)
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
The Methadone Dispensing Treatment (MDT) Phase One project consists of three patches: PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618. This document describes how to deploy, install, and how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 patches will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 require a fully patched VistA system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 are part of a combined multi-patch build (a Kernel Installation and Distribution System or KIDS build). The build is installed on the VistA server.

PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 use the same security measures as VistA. Users will authenticate using either their Personal Identification Verification (PIV) card or access and verify codes.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No one single entity oversees decision making for deployment, installation, back-out, and rollback of the MDT project. The following table provides MDT project information.

Table 1: Roles and Responsibilities

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 18%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MDT Software Quality Assurance (SQA) team and field test sites</td>
<td>Deployment</td>
<td>Test for operational readiness.</td>
</tr>
<tr class="even">
<td>Application Coordinators</td>
<td><p>Release</p>
<p>Deployment</p></td>
<td>Review patches for release readiness and release patches for deployment.</td>
</tr>
<tr class="odd">
<td>Health Infrastructure and Systems Management (HISM) and Local sites</td>
<td>Installation</td>
<td>Based on compliance date, HISM coordinates specific dates and times with sites, VISNs.<br />
HISM will perform the actual installation.</td>
</tr>
<tr class="even">
<td>Sites</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place.</td>
</tr>
<tr class="odd">
<td>MDT Implementation Team</td>
<td>Installation</td>
<td>Provide support, as needed, for installation.</td>
</tr>
<tr class="even">
<td>MDT Implementation Team</td>
<td>Training</td>
<td>Provide national installation and train-the-trainer presentations. Other groups may also provide training.</td>
</tr>
<tr class="odd">
<td>MDT Implementation Team, HISM, and Area Manager</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).</td>
</tr>
<tr class="even">
<td>MDT Implementation Team, Product Support, and CPRS sustainment teams.</td>
<td>Post Deployment</td>
<td>Software Support will be provided by the MDT Implementation Team during warranty period, which is 90 days after national release. Support then changes to the normal ticketing process.</td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment will be nationally released and will adhere to a thirty day compliance timeline for site installation.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After national release, HISM installers will coordinate installation with sites. It will follow the normal release process, with a 30-day compliance period for installation.

This section discusses the locations that will receive the deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 will be deployed to all VistA instances.

Each site needs to follow standard preparation procedures for a new software release.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A fully patched VistA System is required for this installation.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For national release, sites will receive communication that the release has occurred, which will normally be an Action Item or Bulletin.

Sites will use their internal communications to let their users know about upcoming installations and any associated downtime. This is critical as users can often slow the installation process if they are on the system while installers are trying to get the software installed.

Installers and other site personnel (as determined by the site) will need to coordinate installation dates and times.

#### Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|--------------|---------|----------|-----------------------------------|
| Deploy       |         |          |                                   |
| Install      |         |          |                                   |
| Back-Out     |         |          |                                   |

# Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no pre-installation steps.

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special preparation is required. The combined build will follow a normal KIDS installation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The build includes the following patches:

- PSJ\*5.0\*445
- TIU\*1.0\*360
- OR\*3.0\*618

The contents of the build are listed below:

<table style="width:100%;">
<colgroup>
<col style="width: 45%" />
<col style="width: 29%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Contents</th>
<th>Retrieval Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSJ_5_445_TIU_1_360_OR_3_618.KID</td>
<td><p>PSJ*5.0*588</p>
<p>TIU*1.0*360</p>
<p>OR*3.0*618</p></td>
<td>ASCII</td>
</tr>
</tbody>
</table>

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An HISM installer with programmer access needs to be available.

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation sequences must be installed in the order listed in section 5.7.2.

### Mandatory Pre-Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Mandatory Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These files must be installed and distributed in the following order. Detailed instructions are in section 5.8

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>Install PSJ_5_445_TIU_1_360_OR_3_618.KID</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Installation Procedure(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>Install PSJ_5_445_TIU_1_360_OR_3_618.KID</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### PSJ_5_445_TIU_1_360_OR_3_618.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSJ_5_445_TIU_1_360_OR_3_618.KID

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. Installation should take less than five minutes.

Installation Instructions:

1.  From the Kernel Installation and Distribution menu, select the Installation menu.
2.  From the Installation menu, select the Load a Distribution option and enter the location of the Host File, PSJ_5_445_TIU_1_360_OR_3_618.KID.
3.  From the Installation menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter PSJ_5_445_TIU_1_360_OR_3_618.KID.
    1.  Backup a Transport Global - This option creates a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option, and then choose the patch to install.
5.  When prompted with 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', select ‘NO’.
6.  When prompted with ‘Want KIDS to INHIBIT LOGONs during the install? NO//', select ‘NO’.
7.  When prompted with 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', select ‘NO’.
8.  If prompted with ‘Delay Install (Minutes): (0-60):0//’, select ‘0’.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the checksums for the routine(s) in PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 now match the respective post-patch checksums.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a catastrophic failure, the Area Manager will discuss the possibility of backing out the patch and rolling back any necessary database changes with site personnel, product support, patient safety representatives, and the development team. And then, the Area Manager will make the final decision about backout and rollback.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to successfully back-out MDT Phase 1, it is critical that the installer created a backup of the build prior to installation. Please refer to section 5.8.1, step 3a.

If it is necessary to back-out the installation, the HISM team will need to install the back-out build created in section 5.8.1, step 3a.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The site administrator should consider how backing out PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 could affect the system and consult with the development team and support staff.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MDT SQA team tests the software prior to distribution. Test sites will verify that the changes also function correctly in their environment.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because the software is used by clinical staff on a regular basis, backing out PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 should only be considered because of a catastrophic error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks are based on the amount of time PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 have been operational.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ultimate authority for backing out PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 lies with the Area Manager.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To backout the MDT Phase 1 changes, it is imperative that you perform the backup from KIDS in the installation phase. Backout will consist of installing the backout build created at that time.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the checksums for the routine(s) in PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 now match the respective pre-patch checksums.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no data distributed with these patches. However, there were data dictionary changes exported. It is anticipated that, in the event of a need to back-out MDT Phase 1, there will be no need to rollback those data dictionary changes.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because the software is used by clinical staff on a regular basis, backing out PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 should only be considered because of a catastrophic error.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks are based on the amount of time PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 have been operational.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ultimate authority for rolling back PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 lies with the Area Manager.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it becomes necessary to rollback the data dictionary and option changes introduced, the development team will provide a build to rollback the changes.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that the new fields exported by PSJ\*5.0\*445, TIU\*1.0\*360, and OR\*3.0\*618 no longer exist in the data dictionary.