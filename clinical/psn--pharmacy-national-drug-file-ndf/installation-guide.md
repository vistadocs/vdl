---
title: National Drug File Version 4 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: PSN
app_name: "Pharmacy: National Drug File (NDF)"
section: CLI
app_status: active
pkg_ns: PSN
patch_ver: 4
patch_id: PSN*4
group_key: "PSN:PSN:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - server
  - installation
  - update
  - routine
  - back
  - national
  - site
  - directory
page_count: 0
word_count: 7774
section_count: 31
table_count: 17
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2018
revision_count: 16
revision_newest: 06/12/17
revision_oldest: 6/1/2015
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-National_Drug_File_(NDF)/ndf_4_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-National_Drug_File_(NDF)/ndf_4_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=89"
---

---
title: |
  <span id="_top" class="anchor"></span>Pharmacy Product System (PPS)-N Version 3.0

  PSN\*4\*513

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](national-drug-file-version-4-installation-guide/001.png)

January 2018

Office of Information and Technology (OI&T)

Revision History

| Date   | Version | Description                                                                                            | Author                         |
|------------|-------------|------------------------------------------------------------------------------------------------------------|------------------------------------|
| 06/12/17   | 2.5         | Incorporated review findings – updated table on page 9-10, section 3.3.1, section 4.11.2, section 6 and 7. | <span class="mark">REDACTED</span> |
| 06/09/17   | 2.4         | Updated installation, roll back, and back out sections                                                     | <span class="mark">REDACTED</span> |
| 05/16/2017 | 2.3         | Updated back out plans and POC                                                                             | <span class="mark">REDACTED</span> |
| 04/06/2017 | 2.2         | Updated footer, and additional information                                                                 | <span class="mark">REDACTED</span> |
| 03/17/2017 | 2.1         | Continue updating                                                                                          | <span class="mark">REDACTED</span> |
| 03/09/2017 | 2.0         | Updated prerelease Patch information                                                                       | <span class="mark">REDACTED</span> |
| 03/08/2017 | 1.9         | Updated test site information                                                                              | <span class="mark">REDACTED</span> |
| 03/08/2017 | 1.8         | Updated date                                                                                               | <span class="mark">REDACTED</span> |
| 02/03/2017 | 1.7         | Update deployment information                                                                              | <span class="mark">REDACTED</span> |
| 11/19/2016 | 1.6         | Review of Draft Deployment Plan with PM/IMs                                                                | <span class="mark">REDACTED</span> |
| 11/3/2015  | 1.5         | Review and updated; sent to IMs for review                                                                 | <span class="mark">REDACTED</span> |
| 10/16/2015 | 1.4         | Review and updates                                                                                         | <span class="mark">REDACTED</span> |
| 9/21/2015  | 1.3         | Review and updates                                                                                         | <span class="mark">REDACTED</span> |
| 8/14/2015  | 1.2         | Reviewed Draft Deployment Plan and updated                                                                 | <span class="mark">REDACTED</span> |
| 7/10/2015  | 1.1         | Made changes to Deployment Plan                                                                            | <span class="mark">REDACTED</span> |
| 6/1/2015   | 1.0         | Development of Deployment Plan PPS-N v3.0                                                                  | <span class="mark">REDACTED</span> |

Table : Roles and Descriptions

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
  - [## Site Readiness Assessment](#site-readiness-assessment)
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
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Script](#installation-script)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [Post install procedure](#post-install-procedure)
    - [Web server and service verification](#web-server-and-service-verification)
    - [Post-Install Routine (No Action Required)](#post-install-routine-no-action-required)
    - [New PSN PPS ADMIN Security Key (Action Required)](#new-psn-pps-admin-security-key-action-required)
    - [New PSN PPS COORD Security Key (Action Required)](#new-psn-pps-coord-security-key-action-required)
    - [Open VMS Directory (May Require Action)](#open-vms-directory-may-require-action)
    - [LINUX Directory](#linux-directory)
    - [PPS-N Site Parameters (Enter/Edit) (Action Required)](#pps-n-site-parameters-enteredit-action-required)
    - [Create a new SSH Key Pair (Action Required)](#create-a-new-ssh-key-pair-action-required)
    - [Mail Group](#mail-group)
    - [Auditing](#auditing)
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
This document describes the plan to deploy and install the Pharmacy Product System (PPS) PPS-N v3.0, as managed through the Pharmacy Reengineering (PRE) Program Office, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the full Pharmacy Reengineering (PRE) Project Management Plan. The Pharmacy PPS-N v3.0 is intended to complete the development that was started in PPS-N v1.1 and builds upon the v2.0 system, developed previously, but not released to production. It will add improvements to operations, and correct anomalies, defects, and user interface issues that exist in the PPS-N v1.0 and v2.0 systems. The PPS-N v3.0 effort will focus on constructing functionality to update the local copy of the National Drug File NDF VistA files using the PPS-N3.0 data eliminating the need for National Drug File Management System NDFMS to include the patches. The new functionality will eliminate the need to update the national NDF files, increase the timeliness of the local copy of the NDF Vista files, and increase the efficiency of the NDF/local drug file (#50) matching process. In addition, this effort will correct anomalies, defects, and user interface issues, which are critical or require minimal effort to fix.
PPS-N v3.0 will prerelease three patches to prepare for national release in July 2017, these patches will replace the current National Drug File Management System (NDFMS) monthly update functionality via the FORUM patch process.
The PPS-N v3.0 project will replace the Legacy NDFMS with a system that better meets the current and expected business needs and cost effective technical architecture for the VA with faster updates for patient safety. PPS-N v3.0 will provide pharmacy managers with improved work flow, customization, and processes on a scalable platform aligned to VA target architecture. National and Local drug information will update to local sites including updated industry information that allows for better order checks to increase patient safety.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single common document that describes how, when, where, and to whom the PPS-N v3.0 product will be deployed and installed as well as how it is to be backed out and rolled back, if necessary. Appropriate communications planning has been completed, as well as a rollout schedule. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no dependencies for the release of the PPS-N v3.0 PSN\*4\*513 patch.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints for release of the PPS-N v3.0 PSN\*4\*513 patch.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID  | Team                                                                                   | Phase / Role    | Tasks                                                                                                               | Project Phase (See Schedule) |
|-----|----------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|------------------------------|
|     | FO, EO                                                                                 | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                 |                              |
|     | FO, EO                                                                                 | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                          |                              |
|     | FO, EO                                                                                 | Deployment      | Test for operational readiness                                                                                      |                              |
|     | FO, EO                                                                                 | Deployment      | Execute deployment                                                                                                  |                              |
|     | FO, EO                                                                                 | Installation    | Plan and schedule installation                                                                                      |                              |
|     | Regional PM/Field Implementation Services (FIS)/Office of Policy and Planning (OPP) PM | Installation    | Ensure authority to operate and that certificate authority security documentation is in place                       |                              |
|     | Regional PM/FIS/OPP PM                                                                 | Installation    | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         |                              |
|     |                                                                                        | Installations   | Coordinate training                                                                                                 |                              |
|     | Regional PM/FIS/OPP PM                                                                 | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |                              |
|     | Product Support                                                                        | Post Deployment | Hardware, Software and System Support                                                                               |                              |

Table : Deployment/Installation/Back-Out Checklist

| Role                          | Description                                                                                                                                             | Responsible Party                  |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Program Manager               | Person that has overall responsibility for the successful planning and execution of the PRE Program.                                                    | <span class="mark">REDACTED</span> |
| Project Manager - VA          | Person that has overall responsibility for the Government oversight of successful planning and execution of the project.                                | <span class="mark">REDACTED</span> |
| Stakeholders                  | Persons that hold a stake in a situation in which they may affect or be affected by the outcome.                                                        | <span class="mark">REDACTED</span> |
| SDE FO Implementation Manager | Develops Deployment Plan and Deployment Tracking Schedule, collaborating with SDE FO IM and contractor IM(s) with implementation and deployment issues. | <span class="mark">REDACTED</span> |
| PD Implementation Manager     | Develops Deployment Plan and Deployment Tracking Schedule, collaborating with SDE FO IM and contractor IM(s) with implementation and                    | <span class="mark">REDACTED</span> |

Table : User Acceptance Test Site List and Points of Contact

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PPS will release PSN\*4\*513 on January 2018. This patch follows the release of PSN\*4\*396 and PSS\*1\*195 released in July/August 2017.

PSN\*4\*513 is the latest part of the ongoing effort to replace the current National Drug File Management System (NDFMS) monthly update functionality via the FORUM patch process.

Other tasks to be done during national deployment:

1.  Service Delivery and Engineering (SD&E) will send a bulletin to the field announcing the new PPS-N v3.0 update file process (approximately one (1) month prior to deployment of PPS-N v3.0)
1.  NDFMS generated VistA patches will be produced, released, and archived until NDFMS is retired, which should happen after all VA sites have switched to the new automatic download/install of NDF data directly from PPS-N 3.0.

The deployment will be performed by PPS-N project team members along with representatives from peer organizations, as needed. The installation will be performed by Information Resource Management (IRM) staff responsible for VistA administration at local VA Medical Centers (VAMC) and Regional Data Processing Centers (RDPC) and Regional Operations Centers (ROC), where applicable. Facility preparation work will take place prior to national release. SDE FO will ensure site readiness.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for 3 months, as depicted in the master deployment schedule.

![](national-drug-file-version-4-installation-guide/002.png)

## ## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the PPS-N v3.0 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to section 3.2.2 Site Information.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the initial test sites:

| Test Site                          | Address                            | Pharmacy POC                       |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

User Acceptance Testing Test Site names, IT point of contacts, and Subject Matter Expert point of contacts, with title.

Deployment and installation of the PPS-N v3.0 is planned a standard release to all sites.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](national-drug-file-version-4-installation-guide/003.png)<em><mark><br />
</mark></em></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><strong>Veterans Integrated Service Networks (VISN):</strong>![](national-drug-file-version-4-installation-guide/004.png)<strong><br />
</strong><u><a href="http://www.va.gov/directory/guide/region.asp?ID=1001">VISN 1: VA New England Healthcare System</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1002">VISN 2: VA Health Care Upstate New York</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1003">VISN 3: VA NY/NJ Veterans Healthcare Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1004">VISN 4: VA Healthcare - VISN 4</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1005">VISN 5: VA Capitol Health Care Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1006">VISN 6: VA Mid-Atlantic Health Care Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1007">VISN7: VA Southeast Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1008">VISN 8: VA Sunshine Healthcare Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1009">VISN 9: VA Mid-South Healthcare Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1010">VISN 10: VA Healthcare System of Ohio</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1011">VISN 11: Veterans In Partnership</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1012">VISN 12: VA Great Lakes Health Care System</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1015">VISN 15: VA Heartland Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1016">VISN 16: South Central VA Health Care Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1017">VISN 17: VA Heart of Texas Health Care Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1018">VISN 18: VA Southwest Health Care Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1019">VISN 19: Rocky Mountain Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1020">VISN 20: Northwest Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1021">VISN 21: Sierra Pacific Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1022">VISN 22: Desert Pacific Healthcare Network</a><br />
<a href="http://www.va.gov/directory/guide/region.asp?ID=1023">VISN 23: VA Midwest Health Care Network</a></u></td>
</tr>
</tbody>
</table>

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PPS-N v3.0 will not require site preparation tasks for the pre-release patches.

The following table describes preparation required by the site prior to deployment.

Table 3: Site Preparation

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|------------|-----------------------|-----------------------------------------|---------------|-------|
| N/A        |                       |                                         |               |       |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Resources involved in the release of the VistA MUMPS patch PSN\*4\*513 are the assigned Release Coordinators and the project VistA development team. The team will work in coordination with the test site IRMs to install and verify patches.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

All sites will be polled for site readiness, as listed above, prior to the beginning of deployment.

- Facilities: All VistA parent facilities will be required to install the PPS-N v3.0 Patch PSN\*4\*513.
- Documentation: Essential documentation is included in the PPS-N v3.0 patch. Additional supporting documentation will be made available via the PRE PPS-N Project SharePoint site and TSPR for informal or working documents and Frequently Asked Questions (FAQs).

The following table lists facility-specific features required for deployment.

Table 4: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|------|------------|-----------------|-------|
| N/A  |            |                 |       |

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special requirements regarding new or existing hardware capability. Existing hardware resources will not be impacted by the changes in this project.

The following table describes hardware specifications required at each site prior to deployment.

Table 5: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-------------------|-------|---------|---------------|--------------|-------|
| N/A               |       |         |               |              |       |

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

The existing National Drug File Management System (NDFMS), local sites VistA National Drug File (NDF) V. 4.0 package, and Pharmacy Data Management package must be installed and fully patched prior to deployment.

Table 6: Software Specifications

| Required Software | Make | Version | Configuration | Manufacturer | Other |
|-------------------|------|---------|---------------|--------------|-------|
| N/A               |      |         |               |              |       |

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of PPS-N v3.0 and patch installation guides will be distributed to appropriate site staff. Additionally, sites will be provided guidance, prior to implementation, to assure that required file set ups have been completed. Sites will be provided a checklist of pre-implementation activities which must be completed. No other special requirements are necessary.

#### Deployment/Installation/Back-Out Checklist

Table 7 captures the coordination effort and documents the day/time/individual when each activity (deploy, install, back-out) is completed for a project.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The National Drug file V. 4.0 and Pharmacy Data Management (PDM) V. 1.0 relies on a minimum of external packages to be fully patched:

Package Minimum Version Needed

VA FileMan 22.2

Kernel 8.0

MailMan 8.0

Pharmacy Data Management 1.0

National Drug File 4.0

Web Services Client (HWSC) 1.0 \* XOBW\*1\*4 patch must be installed.

The minimum required version for Pharmacy Product System – National (PPS-N) is 1.4.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. No new hardware or other resources are required.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Make sure that the National Drug File package is fully patched. Refer to the PPS-N v3.0 Installation guide. The PSN\*4\*513 patch is being released as a FORUM Patch via the Patch Module.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. The patch is applied to an existing M(UMPS) VistA database.

## Installation Script

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the PPS-N v3.0 Installation guide and patch documentation in the NPM for installation instructions.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

> **NOTE:** within the VistA environment, the installation is at the user’s discretion and can either be run immediately in foreground or be scheduled using VA Kernel’s Task Manager to execute in background at a selected date and time.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to National VA Network, as well as the local network of each site, is required to receive PPS-N patches PSN\*4\*513 and to perform the installation, as well as to have the authority to create and install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the PSN\*4.0\*513 patch description documentation on the National Patch Module for the detailed installation steps.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the PPS-N v3.0 documentation changes and validate the data dictionary changes:

- A site can verify the installation components by validating the additional data dictionary fields defined by utilizing the FileMan List File Attributes \[DILIST\] option.

Example 1: A high level listing for the PPS-N UPDATE CONTROL file (#57.23):

Select OPTION: 8 DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: 1 LIST FILE ATTRIBUTES

START WITH WHAT FILE: VA PRODUCT// 57.23 PPS-N UPDATE CONTROL

(1 entry)

GO TO WHAT FILE: PPS-N UPDATE CONTROL//

Select SUB-FILE:

Select LISTING FORMAT: STANDARD// GLOBAL MAP

DEVICE: ;;1000 SSH VIRTUAL TERMINAL Right Margin: 80//

GLOBAL MAP DATA DICTIONARY \#57.23 -- PPS-N UPDATE CONTROL FILE

OCT 25,2017@14:07:46 PAGE 1

STORED IN ^PS(57.23, (1 ENTRY) SITE: TROY ISC SUPPORT ACCOUNT UCI: FLD,DDV

(VERSION 4.0)

-------------------------------------------------------------------------------

This file contains configuration and installation information for the Pharmacy

Product System - National (PPS-N) file retrieval and installation process.

CROSS

REFERENCED BY: NAME(B)

^PS(57.23,D0,0)= (#.01) NAME \[1F\] ^ (#1) OPEN VMS LOCAL DIRECTORY \[2F\] ^ (#2)

==\>INSTALL VERSION \[3N\] ^ (#3) UNIX/LINUX LOCAL DIRECTORY \[4F\]

==\>^ ^ (#5) PRIMARY PPS-N MAIL GROUP \[6F\] ^ (#8) DOWNLOAD

==\>VERSION \[7N\] ^ (#9) DOWNLOAD STATUS \[8S\] ^ (#10) INSTALL

==\>STATUS \[9S\] ^ (#45) LEGACY UPDATE PROCESSING \[10S\] ^

^PS(57.23,D0,1)= (#6) SECONDARY MAIL GROUP \[1F\] ^

^PS(57.23,D0,2)= (#20) REMOTE SERVER ADDRESS \[1F\] ^ (#21) REMOTE DIRECTORY

==\>ACCESS \[2F\] ^ (#22) REMOTE SFTP USER ID \[3F\] ^

^PS(57.23,D0,3,0)=^57.24P^^ (#30) SCHEDULED OPTION

^PS(57.23,D0,3,D1,0)= (#.01) SCHEDULE OPTIONS \[1P:19.2\] ^

^PS(57.23,D0,3.1,0)=^57.2331P^^ (#31) MENU OPTIONS

^PS(57.23,D0,3.1,D1,0)= (#.01) MENU OPTIONS \[1P:19\] ^

^PS(57.23,D0,3.2,0)=^57.2332P^^ (#32) PROTOCOLS

^PS(57.23,D0,3.2,D1,0)= (#.01) PROTOCOLS \[1P:101\] ^

^PS(57.23,D0,4,0)=^57.234^^ (#50) DOWNLOAD HISTORY

^PS(57.23,D0,4,D1,0)= (#.01) DOWNLOAD FILE NAME \[1F\] ^ (#1) DOWNLOAD BEGIN

==\>DATE/TIME \[2D\] ^ (#2) DOWNLOAD COMPLETE DATE/TIME \[3D\]

==\>^ (#3) FILE SIZE \[4F\] ^ (#4) DOWNLOAD ERROR MESSAGE

==\>\[5F\] ^

^PS(57.23,D0,5,0)=^57.231^^ (#100) INSTALL HISTORY

^PS(57.23,D0,5,D1,0)= (#.01) UPDATE FILE NAME \[1F\] ^ (#1) INSTALL BEGIN

==\>DATE/TIME \[2D\] ^ (#2) INSTALL COMPLETION DATE/TIME \[3D\]

==\>^ (#3) LAST VISTA FILE PROCESSED \[4F\] ^ (#4) LAST FILE

==\>IEN PROCESSED \[5F\] ^ (#5) LAST TMP FILE SUBSCRIPT \[6F\]

==\>^ (#6) LAST UPDATE FILE SECTION \[7F\] ^ (#7) DISPLAYED

==\>LAST \[8F\] ^

^PS(57.23,D0,5,D1,2,0)=^57.233D^^ (#30) INSTALL ERRORS

^PS(57.23,D0,5,D1,2,D2,0)= (#.01) ERROR DATE/TIME \[1D\] ^ (#1) FILE \[2F\] ^

==\>(#2) INTERNAL ENTRY NUMBER \[3F\] ^ (#3) TMP FILE

==\>SUBSCRIPT \[4F\] ^ (#4) ERROR MESSAGE \[5F\] ^

^PS(57.23,D0,6,0)=^57.236^^ (#70) REJECT HISTORY

^PS(57.23,D0,6,D1,0)= (#.01) REJECT FILE NAME \[1F\] ^ (#1) REJECT BEGIN

==\>DATE/TIME \[2D\] ^ (#2) REJECTED BY \[3P:200\] ^

^PS(57.23,D0,FILE1)= (#39) SFTP SSH KEY FORMAT \[1S\] ^ (#41) SFTP SSH KEY

==\>ENCRYPTION \[2S\] ^

^PS(57.23,D0,PRVKEY,0)=^57.2333^^ (#33) SFTP PRIVATE KEY TEXT

^PS(57.23,D0,PRVKEY,D1,0)= (#.01) SFTP PRIVATE KEY TEXT \[1W\] ^

^PS(57.23,D0,PUBKEY,0)=^57.2334^^ (#34) SFTP PUBLIC KEY TEXT

^PS(57.23,D0,PUBKEY,D1,0)= (#.01) SFTP PUBLIC KEY TEXT \[1W\] ^

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

## Post install procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Web server and service verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During patch install of PSN\*4\*513, the PPS-N Web Server and the UPDATE_STATUS web service is defined. These are used to update the installation compliance report on the PPS-N system once sites have installed the PPS-N Update files.

Depending on user access level, the ADPAC or IRM need to make sure the Web Server and Web Service are updated correctly as shown below. You will need to define the correct SERVER during this verification process. When entering data, please make sure that no extra spaces are entered as this will cause communication problems.

Select the Web Server Manager \[XOBW WEB SERVER MANAGER\] option, and verify the parameters. If a PPSN web server and/or the UPDATE_STATUS web service are not defined, please define them as shown below.

Web Server validation:

Select OPTION NAME: XOBW WEB SERVER MANAGER Web Server Manager

Web Server Manager

<u>Web Server Manager Jul 20, 2017@16:48:36 Page: 1 of 1</u>

HWSC Web Server Manager

Version: 1.0 Build: 9

<u>ID Web Server Name IP Address or Domain Name:Port</u>

1 \*PPSN <span class="mark">REDACTED</span>

Legend: \*Enabled

AS Add Server TS (Test Server)

ES Edit Server WS Web Service Manager

DS Delete Server CK Check Web Service Availability

EP Expand Entry LK Lookup Key Manager

Select Action:Quit// ES Edit Server

Select Web Server: 1

NAME: PPSN//

SERVER: <span class="mark">REDACTED</span> Replace \>\>\> Make sure you have the correct server address.

PORT: 443// \>\>\> Make sure port number is 443.

DEFAULT HTTP TIMEOUT: 30//

STATUS: ENABLED//

Security Credentials

====================

LOGIN REQUIRED:

SSL Setup

=========

SSL ENABLED: TRUE// \>\>\> SSL Setup will not be available unless you have the

XOBW\*1\*4 patch installed.

SSL CONFIGURATION: encrypt_only// \>\>\> The SSL CONFIGURATION must be set to "encrypt_only".

SSL PORT: 443// \>\>\> The SSL PORT must be 443.

Authorize Web Services

======================

Select WEB SERVICE: UPDATE_STATUS//

WEB SERVICE: UPDATE_STATUS//

STATUS: ENABLED//

Web Service validation:

<u>Web Server Manager Jul 20, 2017@16:54:15 Page: 1 of 1</u>

HWSC Web Server Manager

Version: 1.0 Build: 9

<u>ID Web Server Name IP Address or Domain Name:Port</u>

1 \*PPSN <span class="mark">REDACTED</span>

Legend: \*Enabled

AS Add Server TS (Test Server)

ES Edit Server WS Web Service Manager

DS Delete Server CK Check Web Service Availability

EP Expand Entry LK Lookup Key Manager

Select Action:Quit// WS Web Service Manager

<u>Web Service Manager Jul 20, 2017@16:54:18 Page: 1 of 1</u>

HWSC Web Service Manager

Version: 1.0 Build: 9

<u>ID Web Service Name Type URL Context Root</u>

1 UPDATE_STATUS REST /PRE/ndf/update/

Enter ?? for more actions

AS Add Service

ES Edit Service

DS Delete Service

EP Expand Entry

Select Action:Quit// ES Edit Service

Select Web Service: 1

===============================================================================

5 UPDATE_STATUS REST /PRE/ndf/update/

-------------------------------------------------------------------------------

Name: UPDATE_STATUS

Type: REST

Registered Date/Time:

Context Root: /PRE/ndf/update/

Availability Resource: status

----------- Web servers 'UPDATE_STATUS' is authorized to: ---------------------

\- PPSN

-------------------------------------------------------------------------------

NAME: UPDATE_STATUS//

DATE REGISTERED:

TYPE: REST//

CONTEXT ROOT: /PRE/ndf/update///

AVAILABILITY RESOURCE: status//

Exit back to the main screen and select the CK Check Web Service Availability option and the sequence number for the PPSN web server. The HTTP Response Status Code should be 201. If something other than this is displayed, either the PPSN remoter server is down or the parameters are entered incorrectly. <span class="mark">REDACTED</span>

Select OPTION NAME: XOBW WEB SERVER MANAGER Web Server Manager

Web Server Manager

<u>Web Server Manager Jul 20, 2017@16:48:36 Page: 1 of 1</u>

HWSC Web Server Manager

Version: 1.0 Build: 9

<u>ID Web Server Name IP Address or Domain Name:Port</u>

1 \*PPSN <span class="mark">REDACTED</span>

Legend: \*Enabled

AS Add Server TS (Test Server)

ES Edit Server WS Web Service Manager

DS Delete Server CK Check Web Service Availability

EP Expand Entry LK Lookup Key Manager

Select Action:Quit// CK Check Web Service Availability

Select Web Server: (1-1): 1

Web Service Availability Oct 25, 2017@13:37:53 Page: 1 of 1

Web Server:

2 \*PPSN <span class="mark">REDACTED</span> (SSL)

-----------------------------------------------------------------------------

1 Unable to retrieve 'status' for UPDATE_STATUS

o HTTP Response Status Code: 201

----------Enter ?? for more actions---------------------------------------\>\>\>

Select Action:Quit//

### Post-Install Routine (No Action Required) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New PSN PPS ADMIN Security Key (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new Security Key was created to restrict access to the following PPS-N functionalities:

| ![](national-drug-file-version-4-installation-guide/005.png) | Action: The new security key PSN PPS ADMIN should be assigned to the National Drug File user responsible for managing the PPS-N functionalities. |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|

### New PSN PPS COORD Security Key (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new Security Key was created to restrict access to the following PPS-N functionalities:

| ![](national-drug-file-version-4-installation-guide/006.png) | Action: The new security key PSN PPS COORD should be assigned to the National Drug File coordinator at your site responsible for managing the SSH key and some other critical parameters that affect the download process. |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Open VMS Directory (May Require Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](national-drug-file-version-4-installation-guide/007.png) | If your site has fully migrated to Linux skip this step. |
|-------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|

If your site has not fully migrated to Linux you will need a new OpenVMS directory (e.g. USER\$:\[SFTP.PPSN\]) to be used by the data download process. The proposed naming convention is only a recommendation. A more knowledgeable and experienced System Manager may choose to setup the extract directory using existing drives and definitions. The directory name chosen must have the appropriate READ, WRITE, EXECUTE, and DELETE privileges. You must have administrator privileges when you perform this task in order to assure the directory is set up/created with the necessary permissions.

Below is an example that can be followed to create the file transmission directory.

\$ CREATE/DIRECTORY USER\$:\[SFTP.PPSN\] /own=CACHEMGR /PROTECTION=(S:RWED,O:RWED,G:RWED,W:RWED)/LOG

<u>NOTE:</u>

• The owner of the directory should be CACHEMGR.

• Where USER\$=the disk of your choice (e.g. USER\$, PQ\$, etc. - SYS\$ is not recommended).

• Confirm that the extract directory has similar protections and permissions.

\$DIR/PROT/OWNER PPSN.DIR

Directory USER\$:\[000000\]

PPSN.DIR;1 \[CACHEMGR\] (RWED,RWED,RWED,RWED)

| ![](national-drug-file-version-4-installation-guide/008.png) | Action: Once the directory has been created, please pass this directory name (e.g., “USER\$:\[SFTP.PPSN\]”) to the ADPAC/Pharmacy Chief/Pharmacy Informatics. This will be used in the PPS-N Site parameters (Enter/Edit) “Outlined Below”. |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### LINUX Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](national-drug-file-version-4-installation-guide/009.png) | If your site runs on VMS skip this step. |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------|

If you have a LINUX operating system, the PPS-N download process will automatically create a directory to be used by the data download process. However, a more knowledgeable and experienced System Manager may choose to setup the extract directory using existing drives and definitions. The directory name chosen must have the appropriate READ, WRITE, EXECUTE, and DELETE privileges. You must have administrator privileges when you perform this task in order to assure the directory is set up/created with the necessary permissions.

Below is an example that can be followed to create the file transmission directory. Where “directoryPath/Name” is you would enter the path to the directory and the new directory name (i.e. /srv/vista/bham/user/sftp/PPSN/ where bham is the site specific folder).

\$mkdir /srv/vista/bham/user/sftp/PPSN/

\$chmod 777 /srv/vista/bham/user/sftp/PPSN/

\$ls –l

1 drwxrwxrwx. 5 cheyl200 cacheusr 4096 Aug 4 11:13 PPSN

<u>NOTE:</u>

• The owner of the directory should be CACHEMGR.

• Confirm that the extract directory has similar protections and permissions.

| ![](national-drug-file-version-4-installation-guide/010.png) | Action: Once the directory has been created, please pass this directory name (e.g., “USER\$:\[SFTP.PPSN\]”) to the ADPAC/Pharmacy Chief/Pharmacy Informaticist. This will be used in the PPS-N Site parameters (Enter/Edit) “Outlined Below”. |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### PPS-N Site Parameters (Enter/Edit) (Action Required) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Next, you will need to work with the pharmacy ADPAC to correctly enter the PPS-N Site parameters through the PPS-N Site Parameters (Enter/Edit) \[PSN PPS PARAM\] option, located under the PPS-N Menu \[PSN PPS MENU\] which are explained below individually. Sites will be provided with the correct Remote Server information as they are brought on-line with PPS-N processing.

![](national-drug-file-version-4-installation-guide/011.png) The PPS-N Site Parameters (Enter/Edit) \[PSN PPS PARAM\] option requires the PSN PPS ADMIN Security Key for editing the parameters (see step 4.2).

Select PPS-N Menu \<FLD DDEV\> Option: SP PPS-N Site Parameters (Enter/Edit)

Pharmacy Product System-National(PPS-N) Site Parameters

-------------------------------------------------------------------------------

1\. PPS-N Install Version : 29

2\. PPS-N Download Version : 29

3\. \*Open VMS Local Directory : USER\$:\[ABC\]

4\. \*Unix/Linux Local Directory : /xxx/xxxxxx/xxx/xxxx/xxxx/xxx/PPSN/

5\. \*Remote Server Address : xxxxxxxxxxxxxxxx.aac.va.gov

6\. \*Remote Server Directory : /xxxxx/xxxxxxx/xxxxxxxxx/xxxxx/approved

7\. \*Remote SFTP Username : xxxxxxxx

8\. Primary PPS-N Mail Group : local_outlook_mail_GROUP@va.gov

9\. Secondary PPS-N Mail group : FIRST.LAST@VA.GOV

10\. \*PPS-N Account Type : P - Production

11\. \*Legacy Update Processing : NO

12\. \*Download Status : NOT IN PROGRESS

13\. \*Install Status : NOT IN PROGRESS

14\. Disable Menus, Options, etc :

-------------------------------------------------------------------------------

Select field number to Edit:

![](national-drug-file-version-4-installation-guide/012.png) An '\*' (asterisk) before the field name indicates that PSN PPS COORD security key is required for editing these fields/parameters.

Install Version Number

This field contains the current version number of the last successful Pharmacy Product System - National (PPS-N) Update file that was installed. For example if the last PPS-N Update file installed was PPS_25PRV_26NEW.DAT, this field would contain 26. When sites are brought on line with PPS-N, this parameter should equate to the last update file created by PPS-N at the time of configuration.

Download Version Number

This field contains the version number for the last Pharmacy Product System - National (PPS-N) Update file downloaded. For example if the last PPS-N Update file downloaded was PPS_25PRV_26NEW.DAT, this field would contain 26. When sites are brought on line with PPS-N, this parameter should equate to the last update file created by PPS-N at the time of configuration.

OpenVMS Local Directory

This field should only be defined for sites that run on OpenVMS operating system. The example display above shows both OpenVMS and Linux define only as an example. This field contains the full path directory structure where the PPS-N update file will be stored on the local system after download from the PPS-N server (e.g., USER\$:\[SFTP.PPSN\]).

Unix/Linux Local Directory

This field should only be defined for sites that run on a Linux operating system. The example display above shows both OpenVMS and Linux define only as an example. This field contains the name of the local Unix/Linux directory where the Pharmacy Product System - National (PPS-N) Update file will be stored on the local system after download from the PPS-N server (e.g. /user/sftp/PPSN/). The option may prompt you for the following after you enter the data and press \<Enter\> through it:

The directory above could not be found.

Would you like to create it now? N//

Answer YES.

Remote Server Address

This is the secure FTP IP address of the Pharmacy Product System-National (PPS-N) server where the PPS-N NDF Update file will be retrieved.

Remote Server Directory

This is the directory name at the Pharmacy Product System-National (PPS-N) server where the PPS-N NDF Update file will be retrieved.

Remote SFTP User ID

This field contains the secure FTP username at the Pharmacy Product System – National (PPS-N) server where the PPS-N NDF Update file will be retrieved.

Primary PPS-N Mail Group

This field is used to store the MS Outlook email group or individual Outlook email address that will receive a copy of the PPS-N update messages. These messages include download and install information, Data Update for NDF report message, Updated Interactions and FDA Med Guide, Drugs Unmatched from National Drug file, Local Drugs Re-matched to NDF, and error messages. The Interactions and Allergies Updated email report will not be sent to Outlook email as it contains patient information. All users of the PSNMGR key will continue to receive the report emails in MailMan.

Secondary PPS-N Mail group

This field is used to store the secondary MS Outlook email group that will receive a copy of

the PPS-N update messages. These messages include download and install information, Data

Update for NDF report message, Updated Interactions and FDA Med Guide, Drugs Unmatched

from National Drug file, Local Drugs Re-matched to NDF, and error messages. The Interactions and Allergies Updated email report will not be sent to Outlook email as it contains patient information. All users of the PSNMGR key will continue to receive the report emails in MailMan.

PPS-N Account Type

This field defines the type of Pharmacy Product System - National (PPS-N) account. The account type can be one of the following: "Q" for National Test SQA system, "T" for

Test/Mirror account, "S" for Product Support, "N" for QA NDFMS account, or "P" for Production account. Local VA sites will use "P" for their production accounts and "T" for their test/mirror accounts.

Legacy Update

This field denotes YES or NO if the National Drug File will be updated by the legacy FORUM patch release process or the PPS-N 3.0 Update process. When NO is entered, sites will not be allowed to install patches from legacy FORUM patch process. Only PPS-N update files will be allowed.

Download Status

This field is used to track the status of a PPS-N/NDF Update file download from the PPS-N sftp server. The possible values for this field are:

IN PROGRESS – PPS-N/NDF file is currently being downloaded

NOT IN PROGRESS - PPS-N/NDF file is not being downloaded

Install Status

This field is used to track the status of a PPS-N/NDF Update file install into the National Drug file package. The possible values for this field are:

IN PROGRESS – PPS-N/NDF file is currently being installed

NOT IN PROGRESS - PPS-N/NDF file is not being installed

DISABLE Scheduled Options, Menu Options and Protocols

Under this field, the site will select scheduled options, menu options, and protocols that needs be marked out of order during the data file installation process.

### Create a new SSH Key Pair (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the PPS-N parameters have been entered the next step is to create a pair of SSH encryption keys that will be used for authenticating the sFTP connection to the PPS-N server automatically bypassing the need for the user to type in a sFTP password. This will enable the data file download from the server. Use the Manage Secure Shell (SSH) Keys \[PSN PPS SSH KEY MANAGEMENT\] option and follow the steps below:

![](national-drug-file-version-4-installation-guide/013.png) The Manage Secure Shell (SSH) Keys \[PSN PPS SSH KEY MANAGEMENT\] option requires the PSN PPS COORD Security Key for creating or deleting SSH Key pairs.

- Verify that you don’t have an SSH Key pair in place already. You can use the Action ‘V’ (View Public SSH Key) for this purpose, as seen in the example below:

> Select one of the following:

> V View Public SSH Key

> C Create New SSH Key Pair

> D Delete SSH Key Pair

> H Help with SSH Keys

> Action: V// v View Public SSH Key

> \[No SSH Key Pair found\]

> Press Return to continue:

The message \[No SSH Key Pair found\] displayed above indicates that there are no SSH keys meaning that it is okay to proceed with the creation of a new SSH Key Pair.

- If you are not sure how to create and share the Public SSH Key invoke the Action ‘H’ for detailed information to help you successfully create and share the key with the PPS-N server. It is recommended that you use RSA.

> Action: V// h Help with SSH Keys

> Secure Shell (SSH) Encryption Keys are used to allow data file download.

> Follow the steps below to successfully setup data file download from Austin

> server to VistA sites:

> Step 1: Select the 'C' (Create New SSH Key Pair) Action and follow the prompts

> to create a new pair of SSH keys. If you already have an existing SSH

> Key Pair you can skip this step.

> You can check whether you already have an existing SSH Key Pair

> through the 'V' (View Public SSH Key) Action.

> Encryption Type: RSA or DSA?

> ----------------------------

> Rivest, Shamir & Adleman (RSA) and Digital Signature Algorithm (DSA)

> are two of the most common encryption algorithms used in IT industry

> for securely sharing data. The majority of servers can handle either

> type; however there are some servers that accept only one specific type.

> Press Return to continue:

> Step 2: Share the Public SSH Key content with the PPS-N SFTP server (Austin).

> In order to successfully establish the data download files, the SFTP

> server at Austin needs to install/configure the new SSH Key created in

> step 1 for the user id they assigned to your site. Use the 'V' (View

> Public SSH Key) Action to retrieve the content of the Public SSH key.

> The Public SSH Key should not contain line-feed characters, therefore

> after you copy & paste it from the terminal emulator into an email or

> text editor make sure it contains only one line of text (no wrapping).

- Once you have read the Help text above proceed to creating the SSH Key Pair by selecting the Action ‘C’ (Create New SSH Key Pair)

> Action: V// C Create New SSH Key Pair

> Enter your Current Signature Code: SIGNATURE VERIFIED

> Select one of the following:

> RSA Rivest, Shamir & Adleman (RSA)

> DSA Digital Signature Algorithm (DSA)

> SSH Key Encryption Type: RSA// ?

> Rivest, Shamir & Adleman (RSA) and Digital Signature Algorithm

> (DSA) are two of the most common encryption algorithms used by

> the IT industry for securely sharing data. The majority of

> servers can handle either type.

> You will need to contact the Austin SFTP server support to determine which type to select.

> Select one of the following:

> RSA Rivest, Shamir & Adleman (RSA)

> DSA Digital Signature Algorithm (DSA)

> SSH Key Encryption Type: RSA// Rivest, Shamir & Adleman (RSA)

> Confirm Creation of SSH Keys? NO// YES

> Creating New SSH Keys, please wait...Done.

- Once you have created the new SSH Key Pair use the Action ‘V’ (View Public SSH Key) one more time to retrieve the content of the Public SSH Key so that you can share with the sftp server.

> Public SSH Key (RSA) content (does not include dash lines):

> --------------------------------------------------------------------------------

> ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDfdQ3vqmqVKT2V6gn34Q42fGJz7hYgEGaP48Hpxk7u

> ZKid0DkUnk4NKI4bf5uwng2TeT5/fPDAzUuTRJCWwJ2hmpBaUXJ+y9b+E5jXsjk8cWRz4frjGz38PTE1

> J0205eYTwRoAeK9qYxVyBiYd7GJjzZkaNL32P3tfMQfBb09bhdeMwtarkPSo6gh65rXGS+3R4DgU5xFd

> QeUU7SGXaVxTEXAsKQagaPIClXrk4wFZ8Q3JvDviWHrKXGb3gmg5RWXC7pHTuZf7LRzhBaDYUbqXN+6k

> x06CycvB6GanQAf1cf1+AO2O9pdJ1J4DN2lA/HDV3BsjNLI926zgMa7ci8kL

> --------------------------------------------------------------------------------

- Send the key to AITC to be added.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th>![](national-drug-file-version-4-installation-guide/014.png)</th>
<th><p><strong>Action</strong>: You will need to share the text content above (between the dash lines) with Austin SFTP server so they can install it on their server. The Public SSH Key sent to the server should not contain line-feed characters. After you copy &amp; paste it from the terminal emulator into an email or text editor, make sure it contains only one line of text (no wrapping).</p>
<p>The site needs to enter CA Service ticket to the “<strong>EO Linux Sys Admin VHA Team”</strong> group. The SFTP server, <strong>vaausmocftpprd01</strong>, should be entered as the Configuration Item.</p>
<p>The description should be something like this:</p>
<p>Add this key to the authorized_keys file for the presftp user on SFTP server, vaausmocftpprd01:</p>
<p>ssh-rsa AAAAB3Nza AQDgPrxWImr81RLnAZ0AsuGMOk4FinQDgPrx… (rest of key)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](national-drug-file-version-4-installation-guide/015.png)

Figure : Example screen shot of a request

### Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites can set up an Outlook mail group consisting of individuals who need to receive notifications generated during PPS-N Update file processing. Holders of the PSNMGR key will continue to receive email notifications but the Outlook mail group gives flexibility. The Outlook mail group will need to be defined in the PPS-N Site Parameters (Enter/Edit) \[PSN PPS PARAM\] option.

### Auditing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With this patch, the Vista Comparison Report \[PSN PPS VISTA COMPARISON RPT\] option allows the user to view or print a report of the NDF changes for a date range. This report is meant for National SQA use but if a site wants to utilize this report they will need to turn auditing on for the NDF files. This was not done programmatically and the decision is up to the site if they want to turn on auditing for all fields, since doing so would increase disk space usage. The following example shows how to turn auditing on for fields within a file. For multiple fields, you must list each out to see if the fields are audited. Note that word processing fields cannot be audited. The files utilized for NDF are:

50.416 DRUG INGREDIENTS

50.6 VA GENERIC

50.605 VA DRUG CLASS

50.606 DOSAGE FORM

50.607 DRUG UNITS

50.608 PACKAGE TYPE

50.609 PACKAGE SIZE

50.64 VA DISPENSE UNIT

50.67 NDC/UPN

50.68 VA PRODUCT

55.95 DRUG MANUFACTURER

56 DRUG INTERACTION

Auditing is probably turned on for some of the files but for full utilization of the new option, you would need to turn auditing on for all fields.

VA FileMan 22.0

Select OPTION: OTHER OPTIONS

Select OTHER OPTION: ??

Choose from:

1 FILEGRAMS

2 ARCHIVING

3 AUDITING

4 SCREENMAN

5 STATISTICS

6 EXTRACT DATA TO FILEMAN FILE

7 DATA EXPORT TO FOREIGN FORMAT

8 IMPORT DATA

9 BROWSER

Select OTHER OPTION: AUDITING

Select AUDIT OPTION: ??

Choose from:

1 FIELDS BEING AUDITED

2 DATA DICTIONARIES BEING AUDITED

3 PURGE DATA AUDITS

4 PURGE DD AUDITS

5 TURN DATA AUDIT ON/OFF

Select AUDIT OPTION: 5 TURN DATA AUDIT ON/OFF

AUDIT FROM WHAT FILE: VA PRODUCT// 50.68 VA PRODUCT (27674 entries)

Select FIELD: ??

Choose from:

.01 NAME y

.05 VA GENERIC NAME y

1 DOSAGE FORM y

2 STRENGTH y

3 UNITS y

4 NATIONAL FORMULARY NAME y

5 VA PRINT NAME y

6 VA PRODUCT IDENTIFIER y

7 TRANSMIT TO CMOP y

8 VA DISPENSE UNIT y

11 GCNSEQNO n

12 PREVIOUS GCNSEQNO n

13 NDC LINK TO GCNSEQNO y

14 ACTIVE INGREDIENTS (multiple)

15 PRIMARY VA DRUG CLASS y

16 SECONDARY VA DRUG CLASS (multiple)

17 NATIONAL FORMULARY INDICATOR y

19 CS FEDERAL SCHEDULE y

20 SINGLE/MULTI SOURCE PRODUCT y

21 INACTIVATION DATE y

23 EXCLUDE DRG-DRG INTERACTION CK y

25 MAX SINGLE DOSE y

26 MIN SINGLE DOSE y

27 MAX DAILY DOSE y

28 MIN DAILY DOSE y

29 MAX CUMULATIVE DOSE y

30 DSS NUMBER y

31 OVERRIDE DF DOSE CHK EXCLUSION y

32 MAXIMUM DAYS SUPPLY y

40 CREATE DEFAULT POSSIBLE DOSAGE y

41 POSSIBLE DOSAGES TO CREATE y

42 PACKAGE y

43 CODING SYSTEM (multiple)

45 COPAY TIER (multiple)

99.98 MASTER ENTRY FOR VUID y

99.99 VUID y

99.991 EFFECTIVE DATE/TIME (multiple)

100 FDA MED GUIDE y

101 HAZARDOUS TO HANDLE y

102 HAZARDOUS TO DISPOSE y

103 PRIMARY EPA CODE y

104 WASTE SORT CODE y

108 CLINICAL EFFECTS OF DRUG (multiple)

109 FORMULARY DESIGNATOR y

2000 SERVICE CODE y

Select FIELD: 11 GCNSEQNO n

AUDIT: n// YES, ALWAYS

Select FIELD: 12 PREVIOUS GCNSEQNO n

AUDIT: n// YES, ALWAYS

Select FIELD: 45 COPAY TIER (multiple)

Select COPAY TIER SUB-FIELD: ??

Choose from:

.01 COPAY TIER LEVEL y

1 COPAY EFFECTIVE DATE y

2 COPAY END DATE y

Select COPAY TIER SUB-FIELD:

Select AUDIT OPTION:

Select OTHER OPTION:

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration is required before or after deployment of PSN\*4\*513.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. No reconfiguration of the VistA database, memory allocation or other resources is necessary.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

The Back-Out Procedure consists of restoring routines, deleting new menu options and security keys and individually removing each new Data Definitions (DD) introduced by patch PSN\*4\*513.

The back-out is to be performed by persons with programmer-level access, and in conjunction with the PPS-N Team.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA KIDs builds cannot be backed out/restored in totality – only routines are part of a backup transport global. Special care is taken during development of VistA code (routines, files, remote procedures, etc.) to make them backward compatible with newer GUI versions to alleviate the issue and avoid typical critical scenario solutions such as emergency patches.

The decision to back out a specific release needs to be made in a timely manner. Catastrophic failures are usually known early in the testing process – within the first two or three days. Sites are encouraged to perform all test scripts to ensure new code is functioning in their environment, with their data. A back-out should only be considered for critical issues or errors. The normal, or an expedited, issue-focused patch process can correct other bugs.

The general strategy for PPS-N v3.0 VistA functionality rollback will likely be to repair the code with another follow-on patch.

If any issues with PPS-N v3.0 Vista software are discovered after it is nationally released and within the 30 day maintenance window, the PPS-N development team will research the issue and provide guidance for any immediate, possible workaround. After discussing the defect with VA and receiving their approval for the proposed resolution, the PPS-N development team will communicate guidance for the long-term solution to the field.

The long-term solution will likely be the installation of a follow-up patch to correct the defect, a follow-up patch to remove the PPS-N v3.0 updates, or a detailed set of instructions on how the software can be safely backed out of the production system.

In addition, at the time of deployment, local sites can perform the following steps:

1.  At the time of system deployment, create a complete backup of the current system and store it on a separate machine.
2.  Continue with application-specific system deployment steps.
1.  If the system fails during deployment, perform a system rollback using the system backup created in step 1.
3.  Perform thorough and comprehensive testing to ensure the integrity and functionality of the system is intact.
4.  Perform a system backup once the system is deemed stable and ready for users, and store it on a separate machine.
1.  Once users begin working on the system, regularly create system backups and store them on another machine.

If system failure occurs after users are on the system, perform a system rollback using the system backup created in step 4a.

If the site cannot install the PPS-N NDF Update files, the site can revert back to the legacy FORUM deployed KIDS patches after rollback.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back out should only be done in the event that the local facility management determines that the patch PSN\*4.0\*513 is not appropriate for that facility, and should only be done as a last resort.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is not applicable for VistA PPS-N v3.0, the new PPS-N Update Process will replace the legacy FORUM deployed NDF Update KIDS patches.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The development team will work with all of the User Acceptance Testing test sites, answering any questions and resolving any issues until final signoff of all of the participating sites is received. When the results of the User Acceptance Testing are complete, it is documented in the Testing Analysis Report (TAR); the report is located in the Project Notebook for PPS-N v3.0.

| Table 3: IOC Test Site Name        | IT Points of Contact - Installer and Subject Matter Expert (SME)  (Tester) |
|------------------------------------|----------------------------------------------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>                                         |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>                                         |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>                                         |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>                                         |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span>                                         |

User Acceptance Testing Test Site names, IT point of contacts, and Subject Matter Expert point of contacts, with title.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Facility Systems Management would need to determine if patch PSN\*4\*513 is not appropriate for their facility. The HPS Clinical 1 team may be consulted if needed.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out the PSN\*4\*513 patch, the local facility will not be able to transition to the PPS-N NDF Update procedure when it is subsequently released. This patch provides infrastructure for PPS-N v3.0 which will replace the FORUM NDF patch release process.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The order would come from the local facility management, IPT Co-Chairs: Robert Longo and PBM.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out is to be performed by persons with programmer-level access, and in conjunction with the PPS-N Team.

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a ticket; the development team will assist with the process.

To back out the patch PSN\*4\*513 complete the following steps:

1.  Install the backup that you created during installation of the patches.
5.  To remove the data dictionary fields complete the following:
- To delete the PPS-N UPDATE CONTROL file (#57.23), cut and paste the following at the programmers prompt:

> S DIU=“^DIZ(57.23,”,DIU(0)=“DES“ D EN^DIU2

The following is an example of what the screen will look like when running this command:

> \>S DIU="^PS(57.23,",DIU(0)="DES" D EN^DIU2

> Deleting the DATA DICTIONARY...

> \>

- For PHARMACY SYSTEM file (#59.7), remove the PPS-N NATIONAL SQA ACCOUNT field (#17) by cutting and pasting the following at the programmers prompt:

> S DIK=”^DD(59.7,”,DA=17,DA(1)=59.7 D ^DIK

The following is an example of what the screen will look like when running this command:

> \>S DIK="^DD(59.7,",DA=17,DA(1)=59.7 D ^DIK

> \>

6.  Delete all menu options related to PPS-N patch as follows:

> \>D DELETE^XPDMENU("PSN PPS MENU","PSN PPS SCHEDULE DOWNLOAD")

> \>D DELETE^XPDMENU("PSN PPS MENU","PSN PPS MANUAL DOWNLOAD")

> \>D DELETE^XPDMENU("PSN PPS MENU","PSN PPS REJECT FILE")

> \>D DELETE^XPDMENU("PSN PPS MENU","PSN PPS PARAM")

> \>D DELETE^XPDMENU("PSN PPS MENU","PSN PPS SCHEDULE INSTALL")

> \>D DELETE^XPDMENU("PSN PPS MENU","PSN PPS MANUAL INSTALL")

> \>D DELETE^XPDMENU("PSN PPS MENU","PSN PPS VISTA COMPARISON RPT")

> \>D DELETE^XPDMENU("PSN PPS MENU","PSN PPS DNLD/INST STATUS REP")

> \>D DELETE^XPDMENU("PSN PPS MENU","PSN PPS SSH KEY MANAGEMENT")

> \>D DELETE^XPDMENU("PSNMGR","PSN PPS MENU")

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out PSN\*4\*513 , the back-out can be verified by running a global listing from the VistA server command line after installation. Global listings should be performed for the following global nodes, after which nothing should be listed if back-out was successful:

> Global ^PS(57.23

> Global ^DD(57.23

Example:

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global ^ PS(57.23 -- NOTE: translation in effect

\<nothing should print\>

Global ^ DD(59.7,17 -- NOTE: translation in effect

\<nothing should print\>

The following routines are unique to PPS-N processes and can be removed from the system. If the user has access to Cache Cube, bring each routine up in a Workspace window, highlight the routine and select Edit \> Delete. The routine and any generated files are deleted. To delete the routines from programmer’s mode, select menu options EVE then Programmer Options then Routine Tools and then Delete Routines. Below is a list of routines unique to PPS-N processing. Once you navigate to the “Routine:” prompt, you can cut and pasted that list at this prompt so that you don’t have to enter them individually.

Example of deleting routines:

Core Applications ...

Device Management ...

FM VA FileMan ...

Menu Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Systems Manager Menu \<FLD DDEV\> Option: PRogrammer Options

KIDS Kernel Installation & Distribution System ...

NTEG Build an 'NTEG' routine for a package

PG Programmer mode

Calculate and Show Checksum Values

Delete Unreferenced Options

Error Processing ...

Global Block Count

List Global

Map Pointer Relations

Number base changer

Routine Tools ...

Test an option not in your menu

Verifier Tools Menu ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Programmer Options \<FLD DDEV\> Option: ROUTINE Tools

%Index of Routines

Check Routines on Other CPUs

Compare local/national checksums report

Compare routines on tape to disk

Compare two routines

Delete Routines

First Line Routine Print

Flow Chart Entire Routine

Flow Chart from Entry Point

Group Routine Edit

Input routines

List Routines

Load/refresh checksum values into ROUTINE file

Output routines

Routine Edit

Routines by Patch Number

Variable changer

Version Number Update

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Routine Tools \<FLD DDEV\> Option: Delete Routines

ROUTINE DELETE

All Routines? No =\> No

Routine: PSN513PO

Routine: PSNCFINQ

Routine: PSNCLEAN

Routine: PSNFTP

Routine: PSNFTP2

Routine: PSNFTP3

Routine: PSNOSKEY

Routine: PSNPARM

Routine: PSNPPSCL

Routine: PSNPPSDL

Routine: PSNPPSI1

Routine: PSNPPSI2

Routine: PSNPPSI3

Routine: PSNPPSMG

Routine: PSNPPSMS

Routine: PSNPPSNC

Routine: PSNPPSNF

Routine: PSNPPSNK

Routine: PSNPPSNP

Routine: PSNPPSNR

Routine: PSNPPSNU

Routine: PSNPPSNV

Routine: PSNPPSNW

Routine: PSNVCR

Routine: PSNVCR1

Routine: PSNVCR2

Routine:

26 routines

26 routines to DELETE, OK: NO// Y

PSN513PO PSNCFINQ PSNCLEAN PSNFTP PSNFTP2 PSNFTP3

PSNOSKEY PSNPARM PSNPPSCL PSNPPSDL PSNPPSI1 PSNPPSI2 PSNPPSI3 PSNPPSMG PSNPPSMS PSNPPSNC PSNPPSNF PSNPPSNK PSNPPSNP PSNPPSNR PSNPPSNU PSNPPSNV PSNPPSNW PSNPPSME PSNVCR1 PSNVCR2

Done.

List of routines unique to PPS-N processing:

PSN513PO PSNCFINQ PSNCLEAN PSNFTP PSNFTP2 PSNFTP3

PSNOSKEY PSNPARM PSNPPSCL PSNPPSDL PSNPPSI1 PSNPPSI2

PSNPPSI3 PSNPPSMG PSNPPSMS PSNPPSNC PSNPPSNF PSNPPSNK

PSNPPSNP PSNPPSNR PSNPPSNU PSNPPSNV PSNPPSNW

PSNVCR PSNVCR1 PSNVCR2

To validate that the routines have been deleted run the routine first line listing which will show no routines:

DDEVISC1A1:FLD\>D ^%RFIRST

Print first line of selected routines or include files.

Routine(s): PSNPPS\*

Routine(s): PSNOS\*

Routine(s): PSNVC\*

Routine(s): PSNKIDS\*

Routine(s): PSN513\*

Routine(s): PSNCFIN\*

Routine(s): PSNFTP\*

Routine(s): PSNPARM

Routine(s):

DDEVISC1A1:FLD\>

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

Template Revision History

| Date          | Version | Description                                                                                                                                                                                                                              | Author                                 |
|---------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| March 2016    | 2.2     | Changed the title from Installation, Back-Out, and Rollback Guide to Deployment and Installation Guide, with the understanding that Back-Out and Rollback belong with Installation.                                                      | VIP Team                               |
| February 2016 | 2.1     | Changed title from Installation, Back-Out, and Rollback Plan to Installation, Back-Out, and Rollback Guide as recommended by OI&T Documentation Standards Committee                                                                      | OI&T Documentation Standards Committee |
| December 2015 | 2.0     | The OI&T Documentation Standards Committee merged the existing *“Installation, Back-Out, Rollback Plan”* template with the content requirements in the OI&T End-user Documentation Standards for a more comprehensive Installation Plan. | OI&T Documentation Standards Committee |
| February 2015 | 1.0     | Initial Draft                                                                                                                                                                                                                            | Lifecycle and Release Management       |