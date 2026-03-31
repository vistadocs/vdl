---
title: National Clozapine Registry Deployment, Installation, Back-out, and Rollback Guide (YS*5.01*227)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: 
app_code: NCR
app_name: "Registry: National Clozapine Coordination"
section: CLI
app_status: active
pkg_ns: NCR
patch_ver: 5.01
patch_id: NCR*5.01
group_key: "NCR:NCR:5.01"
file_numbers: []
security_keys: []
menu_options: 0
description: This document describes how to deploy and install the National Clozapine Registry (NCR) VistA patch YS\5.01\277, as well as how to back-out the product and rollback to a previous version or data set.
audience: 
keywords: 
  - table
  - contents
  - back
  - installation
  - rollback
  - deployment
  - patch
  - procedure
  - class
  - span
page_count: 0
word_count: 2703
section_count: 33
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Registries_National_Clozapine_Coordination/ys_5_01_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Registries_National_Clozapine_Coordination/ys_5_01_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=236"
---

---
title: |
  National Clozapine Registry

  VistA Mental Health Package

  Deployment, Installation, Back-out,  
  and Rollback Guide

  YS\*5.01\*227
---

![](national-clozapine-registry-deployment-installation-back-out-and-rollback-guide-/001.png)

# April 2024


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [April 2024](#april-2024)
- [Department of Veterans Affairs](#department-of-veterans-affairs)
- [Office of Information and Technology](#office-of-information-and-technology)
- [Revision History](#revision-history)
- [Artifact Rationale](#artifact-rationale)
- [List of Tables](#list-of-tables)
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
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Deployment Download and Extract Files](#deployment-download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills for Installation](#access-requirements-and-skills-for-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Publishing the NCR Application to Production](#publishing-the-ncr-application-to-production)
  - [Database Tuning](#database-tuning)
- [Back-out Procedure](#back-out-procedure)
  - [Back-out Strategy](#back-out-strategy)
  - [Back-out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-out Criteria](#back-out-criteria)
  - [Back-out Risks](#back-out-risks)
  - [Authority for Back-out](#authority-for-back-out)
  - [Back-out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Appendix A: Acronyms](#appendix-a-acronyms)

# Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Office of Information and Technology 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc160094841" class="anchor"></span>Table 1: Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 56%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
<tr class="odd">
<th>April 2024</th>
<th>1.0</th>
<th><p>Initial Document for NCR VistA system</p>
<p>Patch YS*5.01.227, in support of NCR VistA Wishlist.</p></th>
<th>Liberty Team</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc160094841" class="anchor"></span>Table 1: Roles and Responsibilities

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software and should be structured appropriately to reflect particulars of these procedures at a single or at multiple locations.

Per the *Veteran-focused Integrated Process (VIP) Guide*, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2, with the expectation it will be updated throughout the lifecycle of the project for each build, as needed.
# List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install the National Clozapine Registry (NCR) VistA patch YS\*5.01\*277, as well as how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a document that describes how, when, where, and to whom the NCR YS\*5.01\*227 patch will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This DIBRG assumes the YS\*5.01\*227 patch is being deployed in a fully patched VistA system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref116043626" class="anchor"></span>Table 2: Timeline Overview</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 20%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>Team </th>
<th>Phase/Role </th>
<th>Tasks </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Project Manager </td>
<td>Pre- Deployment </td>
<td>Plan and schedule deployment (to include coordination with vendors) </td>
</tr>
<tr class="even">
<td><p>Software Quality Assurance (SQA),  </p>
<p>Test Sites </p></td>
<td>Deployment </td>
<td>Test for operational readiness </td>
</tr>
<tr class="odd">
<td><p>Project Manager, </p>
<p>Release Manager, </p>
<p>OIT/Software Product Management Support </p></td>
<td>Deployment </td>
<td>Execute deployment </td>
</tr>
<tr class="even">
<td><p>Release Manager, </p>
<p>NCR Team, </p>
<p>VistA Sites </p></td>
<td>Installation </td>
<td><p>Plan, schedule, and implement installation  </p>
<p> </p></td>
</tr>
<tr class="odd">
<td><p>Release Manager, </p>
<p>NCR Development Team </p></td>
<td>Back-out </td>
<td>Confirm availability of back-out instructions and back-out strategy (i.e., what criteria may prompt a requested back-out) </td>
</tr>
<tr class="even">
<td>NCR Development Team </td>
<td>Post- Deployment </td>
<td>Software and System Support </td>
</tr>
</tbody>
</table>

<span id="_Ref116043626" class="anchor"></span>Table 2: Timeline Overview

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch YS\*5.01\*227 will be released as a Packman message to all sites.

The deployment is planned as a simultaneous (National Release) rollout. Once approval has been given to nationally release, YS\*5.01\*227 will be available for installation and deployment at all sites.

Scheduling of test installs, testing and production deployment will be at the site’s discretion. A 30-day compliance period is anticipated.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to Table 2 for specifics.

| Task Name                         | Start   | Finish  |
|-----------------------------------|---------|---------|
| Installation into PROD            | 3/14/24 | 3/18/24 |
| Release VistA Patch YS\*5.01\*227 | 4/16/24 | 4/16/24 |
| Compliance Period                 | 4/17/24 | 5/17/24 |

<span id="_Toc160094843" class="anchor"></span>Table 3 NCR Resources

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capability (IOC) sites for verification of functionality. Once testing is complete and approval is given for national release, YS\*5.01\*227 will be deployed to all VistA systems.

The IOC test sites are:

- Hines VAMC, Hines, IL
- West Haven VAMC, West Haven, CT

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS\*5.01\*227 requires a fully patched VistA system.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Name      | Document Name                                                        | Location                                                                                             |
|--------------------|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| YS_1.05_227_TM.pdf | National Clozapine Registry Technical Manual (YS\*1.05\*227)             | [VA Software Documentation Library (VDL)](https://www.va.gov/vdl/search.asp?group=application&terms=NCR) |
| YS_1.05_227_PD.pdf | National Clozapine Registry Patch Description (YS\*1.05\*227)            | NCR GitHub Repository                                                                                    |
| YS_1.05_227_VDD    | National Clozapine Registry Version Description Document (YS\*1.05\*227) | NCR GitHub Repository                                                                                    |

<span id="_Ref149058471" class="anchor"></span>Table 4 Release Deployment POC Information

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Configuration Management team will use email and conference calls for communication during the deployment. Email will be utilized to notify stakeholders of the successful product release.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

The software for this patch is being released in a PackMan message.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Deployment Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch YS\*5.01\*227 will be released as a Packman message to all sites.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills for Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch requires installers to have access to the KIDS options to load and install builds.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu.

From this menu:

1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name. (ex. YS\*5.01\*227)

> NOTE: Using \<spacebar\>\<enter\> will not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build.

3.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup, the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
1.  At the Installation option menu, select Backup a Transport Global
2.  At the Select INSTALL NAME prompt, enter your build YS\*5.01\*227
3.  When prompted for the following, enter "B" for Build.

> Select one of the following:

> B Build (including Routines)

> R Routines Only

> Backup Type: B// B

4.  When prompted "Do you wish to secure your build?

> NO//", press \<enter\> and take the default response of "NO".

5.  When prompted with, "Send mail to: Last name, First Name", press \<enter\> to take default recipient. Add any additional recipients.
6.  When prompted with "Select basket to send to: IN//", press \<enter\> and take the default IN mailbox or select a different mailbox.
4.  You may also elect to use the following options:
1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
7.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all the components of this patch, such as routines, DDs, templates, etc.
5.  Select the Install Package(s) option and choose the patch to install.
1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
8.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
9.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Application Coordinator (AC) is responsible for coordinating the activities for the national release of the product or patch, representing VistA Support as a member of the project team for the product or patch release.

Verification and validation are performed to ensure that the processes executed meet the needs of the development effort and the execution of this process satisfies the certification requirements of the organization requesting the activity.

Successful installation can be verified by reviewing the first 2 lines of the routines contained in the patch. The second line will contain patch number 227 in the \[PATCH LIST\] section.

;;5.01;MENTAL HEALTH;\*\*\[Patch List\]\*\*;Dec 30, 1994;Build 17

Table 4 lists the release deployment Point of Contact (POC) information for YS\*5.01\*227.

<table>
<caption><p><span id="_Toc47089566" class="anchor"></span>Table 5: Acronyms List</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 32%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Release Identification</strong></th>
<th><strong>Release Package POC</strong></th>
<th><strong>Release Package POC Email</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS*5.01*227</td>
<td>VistA Support Application Coordinator(s) / Validators</td>
<td><p>Elizabeth.Griffith2@va.gov</p>
<p>Alan.Montgomery@va.gov</p></td>
</tr>
</tbody>
</table>

<span id="_Toc47089566" class="anchor"></span>Table 5: Acronyms List

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Publishing the NCR Application to Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out procedure returns the NCR software to the last known good operational state of the software and appropriate platform settings.

## Back-out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will be done only with the concurrence and participation of development team and appropriate VA site/region personnel. The decision to back-out or rollback software will be a joint decision between development team, VA site/region personnel and other appropriate VA personnel.

## Back-out Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the YS\*5.01\*227 patch is backed out, there should be minimal impact to users.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) will occur according to scheduled dates. If a back-out is required, UAT will be performed in the environment to ensure proper functionality by the NCCC. The NCCC will be notified and consulted for testing if a back-out is required.

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NCR application version may be rolled back if it is decided that the project is canceled, the software is not functioning as expected, or the requested changes implemented by the NCR application are no longer desired.

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the YS\*5.01\*227 patch is backed out, there should be minimal impact to users.

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Concurrence from the VA Product Owner and VA Business Sponsor are required for back-out. The VA Product Owner and VA Business Sponsor will provide the authorization and rationale for back-out and can be contacted at vhaclozapine@va.gov.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will be done only with the concurrence and participation of development team and appropriate VA site/region personnel. The decision to back-out or rollback software will be a joint decision between development team, VA site/region personnel and other appropriate VA personnel.

Prior to installing an updated KIDS package, the site/region should have saved a backup of the routines in a mail message using the Backup a Transport Global \[XPD BACKUP\] menu option (this is done at time of install). The message containing the backed-up routines can be loaded with the "Xtract PackMan" function at the Message Action prompt. The Packman function "INSTALL/CHECK MESSAGE" is then used to install the backed-up routines onto the VistA System.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-out procedure can be verified by printing the first 2 lines of the routines contained in this patch using the option First Line Routine Print \[XU FIRST LINE PRINT\]. Once the routines contained in the YS\*5.01\*227 patch have been rolled back, the first two lines of the routines will no longer contain 227 in the patch list section on line 2.

;;5.01;MENTAL HEALTH;\*\*\[Patch List\]\*\*;Dec 30, 1994;Build 17

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No data was modified by this patch installation and, therefore, no rollback strategy is required.

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

# Appendix A: Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Description                                                     |
|---------|-----------------------------------------------------------------|
| AC      | Application Coordinator                                         |
| App     | Application                                                     |
| ATO     | Authority to Operate                                            |
| CDT     | Contractor Development Team                                     |
| CMT     | Configuration Management Team                                   |
| CONUS   | Contiguous United States                                        |
| DevOps  | Development Operations                                          |
| DIBRG   | Deployment, Installation, Back-out, and Rollback Guide          |
| DMA     | Data Migration Application                                      |
| IOC     | Initial Operating Capability                                    |
| KIDS    | Kernel Installation & Distribution System                       |
| MVC     | Model View Controller                                           |
| NCR     | National Clozapine Registry                                     |
| NCCC    | National Clozapine Coordinating Center                          |
| OIT     | Office of Information & Technology                              |
| POC     | Point of Contact                                                |
| SQL     | Structured Query Language                                       |
| UAT     | User Acceptance Testing                                         |
| VA      | Department of Veterans Affairs                                  |
| VAEC    | VA Enterprise Cloud                                             |
| VDD     | Version Description Document                                    |
| VIP     | Veteran-focused Integrated Process                              |
| VistA   | Veterans Health Information Systems and Technology Architecture |
| VM      | Virtual Machine                                                 |