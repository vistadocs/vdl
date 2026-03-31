---
title: MOCHA Version 2.1b Combined Builds Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: b Combined Builds
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 2.1
patch_id: PSS*2.1
group_key: "PSS:PSS:2.1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - install
  - table
  - mocha
  - contents
  - installation
  - distribution
  - rollback
  - build
  - transport
  - global
page_count: 0
word_count: 6813
section_count: 32
table_count: 10
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: February 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/mocha_2-1b_cb_deploy_install_bo_rb_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/mocha_2-1b_cb_deploy_install_bo_rb_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

---
title: |
  <span id="_top" class="anchor"></span>Medication Order Check Healthcare Application

  (MOCHA v2.1 Build B)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](mocha-version-2-1b-combined-builds-installation-guide/001.png)

February 2018

Office of Information and Technology (OI&T)

Revision History

| Date | Version | Description                                                                                                                                                                                              | Author                         |
|----------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 02/2018  | 1.4         | Updated Rollback and other information to align with final product                                                                                                                                           | <span class="mark">REDACTED</span> |
| 09/2017  | 1.3         | Updated Introduction, Dependencies, Constraints, Install Example, Rollback / Back-Out Considerations, Rollback / Back-Out Criteria, and the Rollback / Back-Out Procedure sections based 2.1b Testing.       | <span class="mark">REDACTED</span> |
| 02/2017  | 1.2         | Updated Introduction, Dependencies, Constraints, Install Example, Rollback / Back-Out Considerations, Rollback / Back-Out Criteria, and the Rollback / Back-Out Procedure sections based on the IOC Testing. | <span class="mark">REDACTED</span> |
| 12/2016  | 1.1         | Inserted Installation, Rollback & Back-Out sections                                                                                                                                                          | <span class="mark">REDACTED</span> |
| 11/2016  | 1.0         | Updated to reflect MOCHA v2.1a                                                                                                                                                                               | <span class="mark">REDACTED</span> |
| 08/2016  | .1          | Initial                                                                                                                                                                                                      | <span class="mark">REDACTED</span> |

Table 5: Deployment/Installation/Back-Out Checklist

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the Department of Veterans Affairs (VA) Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

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
    - [Site Information (Locations, Deployment, Recipients)](#site-information-locations-deployment-recipients)
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
    - [Overview](#overview)
  - [Sequence of Install](#sequence-of-install)
    - [Procedure](#procedure)
    - [Install Examples](#install-examples)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Rollback Procedure / Back-Out Procedure](#rollback-procedure-back-out-procedure)
  - [Rollback / Back-Out Considerations](#rollback-back-out-considerations)
  - [Rollback / Back-Out Criteria](#rollback-back-out-criteria)
  - [Authority for Rollback / Back-Out](#authority-for-rollback-back-out)
  - [Rollback / Back-Out Procedure](#rollback-back-out-procedure)
    - [Overview](#overview-1)
    - [Sequence of Rollback](#sequence-of-rollback)
  - [Rollback / Back-Out Verification Procedure](#rollback-back-out-verification-procedure)
- [Appendix A: Install Examples](#appendix-a-install-examples)
  - [PSS\1\178 Install Example](#pss1178-install-example)
- [## MOCHA 2.1b COMBINED BUILD Install Example](#mocha-21b-combined-build-install-example)
  - [PSS\1.0\206 Install Example](#pss10206-install-example)
- [## MOCHA 2.1B COMBINED FOLLOW UP BUILD Install Example](#mocha-21b-combined-follow-up-build-install-example)
- [Appendix B: Rollback Examples](#appendix-b-rollback-examples)
  - [Follow Up Rollback Example](#follow-up-rollback-example)
  - [Combined Build Rollback Example](#combined-build-rollback-example)
  - [PSS\1\178 Rollback Example](#pss1178-rollback-example)
  - [XXPSS\1\178 Rollback Example](#xxpss1178-rollback-example)
  - [XXMOCHA 2.1 COMBINED BUILD 1.0 Rollback Example](#xxmocha-21-combined-build-10-rollback-example)
  - [Local Routine Backup Rollback Example](#local-routine-backup-rollback-example)
This document describes how to deploy, install and back out the Medication Order Check Healthcare Application (MOCHA) v2.1 Build B, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the Pharmacy Reengineering (PRE) project charter and management plan for this effort.
The software component will be updates to the Veterans Integrated Information Systems and Technology Architecture (VistA) system by a group of builds that is referenced in this Section 1 Introduction and will be referenced as MOCHA v2.1b hereafter for the remainder of this document. The enhancements will be developed in Massachusetts General Hospital Utility Multi-Programming System (MUMPS) and distributed as a group of builds from the National Patch Module. The software changes will be made in the following National Packages:
- Order Entry / Results Reporting, Namespace – OR
- Inpatient Medications, Namespace – PSJ
- Outpatient Pharmacy, Namespace – PSO
- Pharmacy Data Management, Namespace – PSS
Patches to be released are:
- OR\*3\*382
- OR\*3\*469
- PSJ\*5\*256
- PSJ\*5\*347
- PSO\*7\*402
- PSO\*7\*500
- PSS\*1\*178
- PSS\*1\*206

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how and when the MOCHA v2.1b will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. Appropriate communications planning should also be completed, as well as the training plan and the compliance scheduled. The plan also identifies the available resources dedicated to MOCHA v2.1b. No formal training is required for the release of these VistA patches. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A standard, functioning, recently patched legacy VistA system is required for this product.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation and execution of the following application patches must be completed prior to the installation of MOCHA v2.1b:

- OR\*3\*269
- OR\*3\*350
- OR\*3\*421
- OR\*3\*457
- PSJ\*5\*227
- PSJ\*5\*315
- PSJ\*5\*331
- PSJ\*5\*333
- PSJ\*5\*337
- PSJ\*5\*338
- PSJ\*5\*346
- PSO\*7\*436
- PSO\*7\*444
- PSO\*7\*450
- PSO\*7\*455
- PSO\*7\*458
- PSO\*7\*486
- PSO\*7\*442
- PSS\*1\*180
- PSS\*1\*184
- PSS\*1\*195
- PSS\*1\*201

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                                              | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|-------------------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
|        | Product Development (PD) Implementation Team          | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                 | Planning                         |
|        | PD Implementation Team                                | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          | Planning                         |
|        | Software Quality Assurance                            | Deployment       | Test for operational readiness                                                                                      | Build                            |
|        | Health Product Support                                | Deployment       | Execute deployment                                                                                                  | Release Prep Phase               |
|        | PD Implementation Team                                | Installation     | Plan and schedule installation                                                                                      | Build Phase                      |
|        | PD Team                                               | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                       |                                  |
|        | PD Implementation Team / Pharmacy Benefits Management | Installations    | Coordinate training                                                                                                 | Release Prep Phase               |
|        | PD Implementation Team / Development Team             | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Build Phase                      |
|        | SDE Field Operations & Enterprise Operations          | Post Deployment  | Hardware, Software and System Support                                                                               | Post Release                     |

Table 6: System Requirements

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment of this release of MOCHA is planned as a national release of MOCHA v2.1b which includes the VistA patches identified in Section 1 of this document. This group of builds (MOCHA v2.1b) is the follow on of MOCHA v2.1a.

A detailed deployment schedule is stored in Rational Team Concert (RTC) for both the Initial Operation Capability (IOC) and National Deployment and is part of the master project schedule for MOCHA v2.1b. A link to the schedule is provided in Section 3.1 Timeline.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for 30 days, as depicted in the master deployment schedule referenced below.

[MOCHA v2.1 Schedule](http://vaww.oed.portal.va.gov/projects/pre/PRE%20Schedule/Forms/AllItems.aspx?RootFolder=%2Fprojects%2Fpre%2FPRE%20Schedule%2FMOCHA%20Schedules&FolderCTID=0x012000EE60491C0AC8AF479CF3BDF4C570B869&View=%7bA0BD70BE-5A49-4402-9B83-A48F00FD1DF6%7d)

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the MOCHA v2.1b deployment. Topology determinations are made by Enterprise Systems Engineering (ESE) and vetted by Field Office (FO), National Data Center Program (NDCP), and Austin Information Technology Center (AITC) during the design phase as appropriate. Field site coordination is done by FO unless otherwise stipulated by FO.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The package contents for MOCHA v2.1b will be distributed to the Information Resources Management (IRM) staff and/or Enterprise Service Line (ESL) Information Technology (IT) Support personnel responsible for each of the 130 VistA systems.

### Site Information (Locations, Deployment, Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MOCHA v2.1b deployment is planned to take place at all VA Medical Centers (VAMCs) and other VA medical facilities utilizing the Pharmacy Order Check products.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a precursor to the MOCHA v2.1b deployment, patch installation guides, and release notes will be distributed to the appropriate staff at each deployment site at the start of national deployment. Product Development and the business owner Pharmacy Benefits Management (PBM) will provide a brochure and/or a write up as training for MOCHA v2.1b prior to national deployment. Sites will be provided guidance on file setups prior to the start of deployment as appropriate.

The following table describes preparation required by the site prior to deployment.

Table 2: Site Preparation

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            | N/A                       | N/A                                         | N/A               | N/A       |

Table 7: MOCHA 2.1b Enhancements

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hardware, software, systems post-deployment support, and system support roles and responsibilities are defined in both the Project Operations and Maintenance Plan and the Operational Acceptance Plan.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific hardware requirements for installation of MOCHA v2.1b as it runs on existing fielded VistA hardware. There is also no need for specific hardware to assist in the deployment of MOCHA v2.1b.

The following table describes hardware specifications required at each site prior to deployment.

Table 3: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   | N/A       | N/A         | N/A               | N/A              | N/A       |

Table 8: MOCHA 2.1b Install Sequence

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific software requirements for installation or deployment of MOCHA v2.1b.

The following table describes software specifications required at each site prior to deployment.

Table 4: Software Specifications

| Required Software | Make | Version | Configuration | Manufacturer | Other |
|-----------------------|----------|-------------|-------------------|------------------|-----------|
| N/A                   | N/A      | N/A         | N/A               | N/A              | N/A       |

Table 9: MOCHA 2.1b Rollback Sequence

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to the deployment of the MOCHA v2.1b release, a product announcement will be sent via email to current Points Of Contact (POC) on record for each site describing the product and a brief description of the phased deployment and post-deployment support. Included will be links to the MOCHA v2.1b website and Rational site pages which contain further information about the release and the deployment, including the deployment schedule and required pre-installation activities.

The MOCHA v2.1b Implementation Team will respond to email requests for assistance and/or further information and, where appropriate, re-direct these requests to specialist technical staff.

#### Deployment/Installation/Back-Out Checklist

Tracking of installation for MOCHA v2.1b VistA patches will be monitored in FORUM.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

Deployment/Installation/Back-Out ChecklistThis table includes the Deployment/Installation/Back-Out Checklist.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patches described in this installation guide can only be run with a standard Massachusetts General Hospital Utility Multi-Programming System (MUMPS) operating system and require the following VA software packages.

| Package                                 | Minimum Version Needed |
|-----------------------------------------|------------------------|
| Pharmacy Data Management                | 1.0                    |
| VA FileMan                              | 22.0                   |
| Kernel                                  | 8.0                    |
| Health*e*Vet Web Services Client (HWSC) | 1.0                    |
| Outpatient Pharmacy                     | 7.0                    |
| Inpatient Medications                   | 5.0                    |
| Order Entry/Results Reporting           | 3.0                    |

Please see Section 1.3 above for a list of specific application patches which must be installed prior to installing this group of builds.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This group of patches should be installed when Pharmacy applications are not in use, no other pharmacy patches are being installed, and when tasked jobs from Clinical Applications are not running.

Installation should also occur when CPRS usage is at a minimum, particularly medication activities.

\* \* \* Notice \* \* \*

This group of patches should not be installed until the follow on patch PSO\*7.0\*515 has been released and is ready to be immediately installed. PSO\*7.0\*515 must be installed immediately after the successful installation of this group of builds.

\* \* \* Notice \* \* \*

Installation of this group of patches should take no longer than 15 minutes.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The distribution files for this group of builds can be obtained from the ANONYMOUS.SOFTWARE directory at one of the OI Field Offices. The preferred method is to FTP the file from <span class="mark">REDACTED</span>, which will transmit the file from the first available server. Alternatively, sites may elect to retrieve the file from a specific OI Field Office.

<u>OI FIELD OFFICE</u> <u>FTP ADDRESS</u><u>DIRECTORY</u>

<span class="mark">REDACTED</span>

The MOCHA 2.1b ENHANCEMENTS software distribution includes:

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 32%" />
<col style="width: 32%" />
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
<td>PSS_1_178.KID</td>
<td>PSS*1.0*178</td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>MOCHA_2_1_PSO_OR_PSJ_ BUILD.KID</td>
<td>PSJ*5.0*256<br />
PSO*7.0*402<br />
OR*3.0*382</td>
<td>ASCII</td>
</tr>
<tr class="odd">
<td>PSS_1_206.KID</td>
<td>PSS*1.0*206</td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>MOCHA_2_1_FOLLOW_UP_ PSO_OR_PSJ.KID</td>
<td>PSO*7.0*500<br />
OR*3.0*469<br />
PSJ*5.0*347</td>
<td>ASCII</td>
</tr>
</tbody>
</table>

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

Programmer-level VistA access and experience using the Kernel Integrated Distribution System (KIDS) is required.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Builds for MOCHA 2.1b must be installed in the sequence below. They must be installed in their entirety and the sequence must be completed. If you cannot or do not successfully complete the entire sequence you must back out what you have completed or rollback to the condition before the sequence began.

We strongly recommend you make a KIDS backup of every step prior to making that step. This will preserve any potential local modifications you may have and make a back out possible, if needed. If you do not make backups, if there is an issue with the install, you will have to roll back the entire process. You must enter a CA ticket for Health Product Support Pharmacy Data Management to obtain rollback builds and support.

#### Checksum Discrepancies in Patch Descriptions

The 'Before' checksum values for ALL routines in patch PSS\*1.0\*206 will appear incorrect in the patch description. This is because they are components of the preceding patch PSS\*1.0\*178 which is also part of the MOCHA 2.1b group of builds. The FORUM Patch Module uses released checksum values to populate the 'Before' fields. The FORUM Patch Module does not have access to the actual 'Before' checksum values since PSS\*1.0\*178 will be released at the same time.

The 'Before' checksum values for routines PSOBKDE1, PSODEM, PSODOSUN, PSOORED5, PSOORUT2, PSORXEDT, PSOSIG, and PSOVER1 in patch PSO\*7.0\*500 will appear incorrect in the patch description. This is because they are components of the preceding patch PSO\*7.0\*402 which is also part of the MOCHA 2.1b group of builds. The FORUM Patch Module uses released checksum values to populate the 'Before' fields. The FORUM Patch Module does not have access to the actual 'Before' checksum values since PSO\*7.0\*402 will be released at the same time.

The 'Before' checksum values for routines PSGOD, PSGOER, PSGOEV, PSGS0, PSGSICHK, PSIVOCDS, PSIVSP, PSJLIFNI, and PSJOCDSD in patch PSJ\*5.0\*347 will appear incorrect in the patch description. This is because they are components of the preceding patch PSJ\*5.0\*256 which is also part of the MOCHA 2.1b group of builds. The FORUM Patch Module uses released checksum values to populate the 'Before' fields. The FORUM Patch Module does not have access to the actual 'Before' checksum values since PSJ\*5.0\*256 will be released at the same time.

## Sequence of Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the sequence of installation for MOCHA 2.1b.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 32%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Sequence Order</th>
<th>Title</th>
<th>Transport File</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>PSS*1.0*178</td>
<td>PSS_1_178.KID</td>
</tr>
<tr class="even">
<td>2</td>
<td>MOCHA Combined Build 1.0<br />
(Contains: PSJ*5.0*256, PSO*7.0*402 and OR*3.0*382)</td>
<td>MOCHA_2_1_PSO_OR_PSJ_BUILD.KID</td>
</tr>
<tr class="odd">
<td>3</td>
<td>PSS*1.0*206</td>
<td>PSS_1_206.KID</td>
</tr>
<tr class="even">
<td>4</td>
<td>MOCHA Combined Follow Up Build 1.0<br />
(Contains: PSO*7.0*500, OR*3.0*469, and PSJ*5.0*347)</td>
<td>MOCHA_2_1_FOLLOW_UP_PSO_OR_PSJ.KID</td>
</tr>
</tbody>
</table>

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following procedure needs to be implemented for each specific build in the sequence order listed above.

1.  Use Load a Distribution. You may need to prepend a directory name which corresponds to where .KID files have been stored on your system. When prompted for “Enter a Host File:” enter the transport file for the sequence that you are installing.

> Examples: USER\$:\[ABC\]PSS_1_178.KID

> USER\$:\[ABC\]MOCHA_2_1_PSO_OR_PSJ.KID

> USER\$:\[ABC\]PSS_1_206.KID

> USER\$:\[ABC\]MOCHA_2_1_FOLLOW_UP_PSO_OR_PSJ.KID

2.  From this menu, you may then select to use the following options:
    1.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
    2.  Print Transport Global - This option will allow you to view the components of the KIDS build.
    3.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
    4.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
3.  Select the Installation option ‘Install Package(s)’. This is the step to start the installation of this KIDS patch:
4.  Choose the Install Package(s) option to start the patch install and enter the package name you have previously loaded at the INSTALL NAME prompt.
    1.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
    2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
    3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO.
    4.  When prompted ‘Delay Install (Minutes): (0-60): 0//’ press the Enter key.

### Install Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Install Examples please see [Appendix A](#appendix-a-install-examples) in this document.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install verification can be done by using the following VistA option to verify the status of the install is complete.

Select Kernel Installation & Distribution System Option: Utilities

> Build File Print

> Install File Print

> Edit Install Status

> Convert Loaded Package for Redistribution

> Display Patches for a Package

> Purge Build or Install Files

> Rollup Patches into a Build

> Update Routine File

> Verify a Build

> Verify Package Integrity

Select Utilities Option: Install File Print

Select INSTALL NAME: PSS\*1.0\*178

DEVICE: HOME//

PACKAGE: PSS\*1.0\*178 MONTH DAY, YEAR@TIME PAGE 1

COMPLETED ELAPSED

STATUS: Install Completed DATE LOADED: MONTH DAY, YEAR@TIME

Select Utilities Option: Install File Print

Select INSTALL NAME: MOCHA 2.1 COMBINED BUILD 1.0

DEVICE: HOME//

Review the install file build for this patch to ensure the eight file entry modifications executed properly. If any of the eight updates indicate anything other than 'PASSED' enter a CA ticket for Health Product Support Pharmacy Benefits Management for assistance. These would be minor data issues so you may continue installing the remainder of the builds in the sequence.

PACKAGE: MOCHA 2.1 COMBINED BUILD 1.0 MONTH DAY, YEAR@TIME PAGE 1

COMPLETED ELAPSED

STATUS: Install Completed DATE LOADED: MONTH DAY, YEAR@TIME

Select Utilities Option: Install File Print

Select INSTALL NAME: PSS\*1.0\*206

DEVICE: HOME//

PACKAGE: PSS\*1.0\*206 MONTH DAY, YEAR@TIME PAGE 1

COMPLETED ELAPSED

STATUS: Install Completed DATE LOADED: MONTH DAY, YEAR@TIME

Select Utilities Option: Install File Print

Select INSTALL NAME: MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0

DEVICE: HOME//

PACKAGE: MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0 MONTH DAY, YEAR@TIME PAGE 1

COMPLETED ELAPSED

STATUS: Install Completed DATE LOADED: MONTH DAY, YEAR@TIME

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

![](mocha-version-2-1b-combined-builds-installation-guide/002.png) Note: Installation of MOCHA 2.1b is completed. The following procedure is to be followed only if MOCHA 2.1b needs to be backed out.

# Rollback Procedure / Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The last section of this document is only needed if there are major problems (examples include; KIDS notice of incompletion or hard errors) resulting from the installation of this group of patches. You must have concurrence from the Health Product Support before a rollback can occur. Enter a CA ticket to obtain this concurrence. The terms ‘Rollback’ and ‘Back-Out’ are synonymous for the purposes of this group of builds. Rollback is an ‘all or nothing’ exercise as all portions of the group of builds interact with each other.

## Rollback / Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This rollback should occur when Pharmacy applications are not in use, no other pharmacy patches are being installed and when tasked jobs from Clinical Applications are not running.

Rollback should also occur when CPRS usage is at a minimum, particularly medication activities.

The rollback procedure should take no longer than 25 minutes.

## Rollback / Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Make sure you have the following software available for the rollback:

1.  Routine backup from the initial PSS\*1.0\*178 installation at your facility.
2.  Routine backup from the initial MOCHA 2.1b COMBINED BUILD installation at your facility.
3.  Routine backup from the initial PSS\*1.0\*206 installation at your facility.
4.  Routine backup from the initial MOCHA 2.1b COMBINED FOLLOW UP BUILD installation at your facility.

Rollback Builds are available from Health Product Support if local routine back-ups are not available.

5.  XXPSS\*1\*178 (must be obtained from Health Product Support)
6.  XXMOCHA 2.1 COMBINED BUILD 1.0 (must be obtained from Health Product Support)

## Authority for Rollback / Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure for these patches should only occur when there is concurrence from the Health Product Support and MOCHA development teams, because of the complexity and risk involved in a rollback. Normal installation back-ups using KIDS will back up only Mumps routines. Make sure the ‘Backup a Transport Global’ step outlined in Section 4, Installation, of this document is followed, so you do have a backup of all the routines if needed.

## Rollback / Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback / back-out procedure must proceed in the inverse order of the installation. You must use your backups created during installation or obtain rollback builds from Health Product Support to proceed. There are additional steps required for the rollback sequence (removing new routines) than exist for the installation sequence. There are no data conversions or rollback issues to be considered with this group of builds.

\*\*\*Note - If local backups were generated as recommended upon installation of the builds and the rollback plan is to restore from local backups, see Appendix B, Section 7.6, for an example of restoration from PACKMAN.

### Sequence of Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the Rollback sequence for MOCHA 2.1b.

| Sequence Order | Title                          | Transport File                                                                                                                                    |
|----------------|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| 1              | Combined Follow Up Build       | MOCHA_2_1_RESTORE_FOLLOW_UP.KID                                                                                                                   |
| 2              | PSS\*1.0\*206                  | This sequence is covered in sequence 4. There is nothing to do at this sequence. PSS\*1\*178 restore build will recover the PSS\*1\*206 routines. |
| 3              | Combined Build                 | MOCHA_2_1_RESTORE_PSO_OR_PSJ.KID                                                                                                                  |
| 4              | PSS\*1.0\*178                  | PSS_BEFORE_MOCHA_2_1_B.KID                                                                                                                        |
| 5              | XXPSS\*1\*178                  | XXPSS_1_178.KID                                                                                                                                   |
| 6              | XXMOCHA 2.1 COMBINED BUILD 1.0 | XXMOCHA_2_1_PSO_OR_PSJ.KID                                                                                                                        |

#### Combined Follow Up Build

Restore routine backup from the MOCHA_2_1_FOLLOW_UP_PSO_OR_PSJ.KID install. If you do not have one, the Health Product Support team can supply one.

If you used the standard KIDS backup procedure prior to installing the MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0, and took the default name from KIDS for the back-up, the back-up would be called ‘Backup of MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0’.

\*\*\*NOTE - If for some reason the above build was installed multiple times, make sure you restore the back up from the first install.

\*\*\*NOTE - If you did not attempt to install the Combined Follow Up Build, you may skip this step.

#### PSS\*1.0\*206

This restoration is covered by the PSS\*1.0\*178 rollback.

#### Combined Build

Restore the routine backup from the MOCHA_2_1_PSO_OR_PSJ_BUILD.KID install. If you do not have one, the Health Product Support team can supply one.

If you used the standard KIDS backup procedure prior to installing the MOCHA 2.1 COMBINED BUILD 1.0, and took the default name from KIDS for the back-up, the back-up would be called ‘Backup of MOCHA 2.1 COMBINED BUILD 1.0’.

\*\*\*NOTE - If for some reason the above build was installed multiple times, make sure you restore the back up from the first install.

\*\*\*NOTE - If you did not attempt to install the Combined Build, you may skip this step.

#### PSS\*1.0\*178 

Restore the routine backup from the PSS_1_178.KID install. If you do not have one, the Health Product Support team can supply one.

If you used the standard KIDS backup procedure prior to installing the PSS\*1.0\*178, and took the default name from KIDS for the back-up, the back-up would be called ‘Backup of PSS\*1.0\*178’.

\*\*\*NOTE - If for some reason the above build was installed multiple times, make sure you restore the back up from the first install.

#### XXPSS\*1\*178

This build will delete eight new routines, listed below, that were installed with PSS\*1.0\*178 for MOCHA 2.1b.

- PSS1P178
- PSSDSEXD
- PSSDSEXE
- PSSDSUTA
- PSSHRQ24
- PSSHRQ25
- PSSHRQ2D
- PSSSCHMS

Contact Health Product Support to obtain a copy of this build.

1.  Download XXPSS_1_178.KID into your local directory.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File:”, respond with XXPSS_1_178.KID.

> Example: USER\$:\[ABC\]XXPSS_1_178.KID

4.  From this menu, you may then select to use the following options:

| Note:                                                                                                           | The following are OPTIONAL - (When prompted for the INSTALL NAME, enter XXPSS\*1.0\*178). |
|---------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| ![](mocha-version-2-1b-combined-builds-installation-guide/003.png) |                                                                                               |

- Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global - This option will allow you to view the components of the KIDS build.
- Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
- Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
5.  Select the Installation option ‘Install Package(s)’. This is the step to start the installation of this KIDS patch:
- Choose the Install Package(s) option to start the patch install and enter the package name you have previously loaded at the INSTALL NAME prompt.
- When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
- When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
- When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO.
- When prompted ‘Delay Install (Minutes): (0-60): 0//’ press the Enter key.

> **NOTE:** See [Appendix B](#appendix-b-rollback-examples) for Rollback examples.

#### XXMOCHA 2.1 COMBINED BUILD 1.0

This build will delete two new routines, see the list below, that were installed with MOCHA 2.1 COMBINED BUILD 1.0 for MOCHA 2.1b.

- PSO7P402
- PSODOSU4

Download XXMOCHA_2_1_PSO_OR_PSJ.KID into your local directory.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
2.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File:”, respond with XXMOCHA_2_1_PSO_OR_PSJ.KID.

> Example: USER\$:\[ABC\]XXMOCHA_2_1_PSO_OR_PSJ.KID

3.  From this menu, the following four options may be executed, but are not required:
    - Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
    - Print Transport Global - This option will allow you to view the components of the KIDS build.
    - Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
    - Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
4.  Select the Installation option ‘Install Package(s)’. This is the step to start the installation of this KIDS patch:
    - Choose the Install Package(s) option to start the patch install and enter the package name you have previously loaded at the INSTALL NAME prompt.
    - When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
    - When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
    - When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO.
    - When prompted ‘Delay Install (Minutes): (0-60): 0//’ press the Enter key.

> **NOTE:** See [Appendix B](#appendix-b-rollback-examples) for Rollback examples.

## Rollback / Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the Rollback procedure has been successfully completed, use the Install File Print option as shown below to verify that all the rollback builds have been installed.

Select Kernel Installation & Distribution System Option: Utilities

> Build File Print

> Install File Print

> Edit Install Status

> Convert Loaded Package for Redistribution

> Display Patches for a Package

> Purge Build or Install Files

> Rollup Patches into a Build

> Update Routine File

> Verify a Build

> Verify Package Integrity

Select Utilities Option: Install File Print

Select INSTALL NAME: XXPSS\*1.0\*178

DEVICE: HOME//

PACKAGE: XXPSS\*1.0\*178 MONTH DAY, YEAR@TIME PAGE 1

COMPLETED ELAPSED

STATUS: Install Completed DATE LOADED: MONTH DAY, YEAR@TIME

Select INSTALL NAME: XXMOCHA 2.1 COMBINED BUILD 1.0

DEVICE: HOME//

PACKAGE: XXMOCHA 2.1 COMBINED BUILD 1.0 MONTH DAY, YEAR@TIME PAGE 1

COMPLETED ELAPSED

STATUS: Install Completed DATE LOADED: MONTH DAY, YEAR@TIME

Select INSTALL NAME: Backup of PSS\*1.0\*178

DEVICE: HOME//

PACKAGE: Backup of PSS\*1.0\*178 MONTH DAY, YEAR@TIME PAGE 1

COMPLETED ELAPSED

STATUS: Install Completed DATE LOADED: MONTH DAY, YEAR@TIME

Select INSTALL NAME: Backup of MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0

DEVICE: HOME//

PACKAGE: Backup of MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0 MONTH DAY, YEAR@TIME PAGE 1

COMPLETED ELAPSED

STATUS: Install Completed DATE LOADED: MONTH DAY, YEAR@TIME

Select INSTALL NAME: Backup of MOCHA 2.1 COMBINED BUILD 1.0

DEVICE: HOME//

PACKAGE: Backup of MOCHA 2.1 COMBINED BUILD 1.0 MONTH DAY, YEAR@TIME PAGE 1

COMPLETED ELAPSED

STATUS: Install Completed DATE LOADED: MONTH DAY, YEAR@TIME

# Appendix A: Install Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PSS\*1\*178 Install Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select OPTION NAME: Kernel Installation & Distribution System

> Edits and Distribution ...

> Utilities ...

> Installation ...

> Patch Monitor Main Menu ...

> Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: Load a Distribution

> Enter a Host File: USER\$:\[ABC\]PSS_1_178.KID

> KIDS Distribution saved on MONTH DAY, YEAR@TIME

> Comment: PSS\*1\*178

> This Distribution contains Transport Globals for the following Package(s):

> PSS\*1\*178

> OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES//

> Loading Distribution...

> Build PSS\*1.0\*178 has an Environmental Check Routine

> Want to RUN the Environment Check Routine? YES//

> PSS\*1.0\*178

> Will first run the Environment Check Routine, PSS1P178

> Use INSTALL NAME: PSS\*1.0\*178 to install this Distribution.

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: Install Package(s)

> Select INSTALL NAME: PSS\*1.0\*178 MONTH DAY, YEAR@TIME

> =\> PSS\*1\*178 ;Created on MONTH DAY, YEAR@TIME

> This Distribution was loaded on MONTH DAY, YEAR@TIME with header of

> PSS\*1\*178 ;Created on MONTH DAY, YEAR@TIME

> It consisted of the following Install(s):

> PSS\*1.0\*178

> Checking Install for Package PSS\*1.0\*178

> Will first run the Environment Check Routine, PSS1P178

> Install Questions for PSS\*1.0\*178

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME//

> --------------------------------------------------------------------------------

> Install Started for PSS\*1.0\*178 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: MONTH DAY, YEAR

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Running Post-Install Routine: POST^PSS1P178

> Now running Dose Unit and Dose Unit Conversion File updates...

> Update 1 of 8 PASSED

> Update 2 of 8 PASSED

> Update 3 of 8 PASSED

> Update 4 of 8 PASSED

> Update 5 of 8 PASSED

> Update 6 of 8 PASSED

> Update 7 of 8 PASSED

> Update 8 of 8 PASSED

> -- UPDATE COMPLETE --

> Updating Routine file...

> Updating KIDS files...

> PSS\*1.0\*178 Installed.

> MONTH DAY, YEAR@TIME

> Install Completed

# ## MOCHA 2.1b COMBINED BUILD Install Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select OPTION NAME: Kernel Installation & Distribution System

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: Load a Distribution

> Enter a Host File: USER\$:\[ABC\]MOCHA_2_1_PSO_OR_PSJ.KID

> KIDS Distribution saved on MONTH DAY, YEAR@TIME

> Comment: MOCHA 2.1 COMBINED BUILD 1.0

> This Distribution contains Transport Globals for the following Package(s):

> Build MOCHA 2.1 COMBINED BUILD 1.0

> PSO\*7.0\*402

> OR\*3.0\*382

> PSJ\*5.0\*256

> OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES//

> Loading Distribution...

> MOCHA 2.1 COMBINED BUILD 1.0

> Build PSO\*7.0\*402 has an Environmental Check Routine

> Want to RUN the Environment Check Routine? YES//

> PSO\*7.0\*402

> Will first run the Environment Check Routine, PSO7P402

> OR\*3.0\*382

> PSJ\*5.0\*256

> Use INSTALL NAME: MOCHA 2.1 COMBINED BUILD 1.0 to install this Distribution.

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: Install Package(s)

> Select INSTALL NAME: MOCHA 2.1 COMBINED BUILD 1.0 MONTH DAY, YEAR@TIME

> =\> MOCHA 2.1 COMBINED BUILD 1.0 ;Created on MONTH DAY, YEAR@TIME

> This Distribution was loaded on MONTH DAY, YEAR@TIME with header of

> MOCHA 2.1 COMBINED BUILD 1.0 ;Created on MONTH DAY, YEAR@TIME

> It consisted of the following Install(s):

> MOCHA 2.1 COMBINED BUILD 1.0 PSO\*7.0\*402 OR\*3.0\*382 PSJ\*5.0\*256

> Checking Install for Package MOCHA 2.1 COMBINED BUILD 1.0

> Install Questions for MOCHA 2.1 COMBINED BUILD 1.0

> Checking Install for Package PSO\*7.0\*402

> Will first run the Environment Check Routine, PSO7P402

> Install Questions for PSO\*7.0\*402

> Checking Install for Package OR\*3.0\*382

> Install Questions for OR\*3.0\*382

> Checking Install for Package PSJ\*5.0\*256

> Install Questions for PSJ\*5.0\*256

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME//

> --------------------------------------------------------------------------------

> Install Started for MOCHA 2.1 COMBINED BUILD 1.0 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: MONTH DAY, YEAR

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Install Started for PSO\*7.0\*402 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: MONTH DAY, YEAR

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Updating Routine file...

> Updating KIDS files...

> PSO\*7.0\*402 Installed.

> MONTH DAY, YEAR@TIME

> Not a production UCI

> NO Install Message sent

> Install Started for OR\*3.0\*382 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: MONTH DAY, YEAR

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Updating Routine file...

> Updating KIDS files...

> OR\*3.0\*382 Installed.

> MONTH DAY, YEAR@TIME

> Not a production UCI

> NO Install Message sent

> Install Started for PSJ\*5.0\*256 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: MONTH DAY, YEAR

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Updating Routine file...

> Updating KIDS files...

> PSJ\*5.0\*256 Installed.

> MONTH DAY, YEAR@TIME

> Not a production UCI

> NO Install Message sent

> Updating Routine file...

> Updating KIDS files...

> MOCHA 2.1 COMBINED BUILD 1.0 Installed.

> MONTH DAY, YEAR@TIME

> No link to PACKAGE file

> Install Completed

## PSS\*1.0\*206 Install Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select OPTION NAME: Kernel Installation & Distribution System

> Edits and Distribution ...

> Utilities ...

> Installation ...

> Patch Monitor Main Menu ...

> Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: Load a Distribution

> Enter a Host File: USER\$:\[ABC\]PSS_1_206.KID

> KIDS Distribution saved on MONTH DAY, YEAR@TIME

> Comment: PSS\*1.0\*206

> This Distribution contains Transport Globals for the following Package(s):

> PSS\*1.0\*206

> Distribution OK!

> Want to Continue with Load? YES//

> Loading Distribution...

> PSS\*1.0\*206

> Use INSTALL NAME: PSS\*1.0\*206 to install this Distribution.

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: Install Package(s)

> Select INSTALL NAME: PSS\*1.0\*206 MONTH DAY, YEAR@TIME

> =\> PSS\*1.0\*206 ;Created on MONTH DAY, YEAR@TIME

> This Distribution was loaded on MONTH DAY, YEAR@TIME with header of

> PSS\*1.0\*206 ;Created on MONTH DAY, YEAR@TIME

> It consisted of the following Install(s):

> PSS\*1.0\*206

> Checking Install for Package PSS\*1.0\*206

> Install Questions for PSS\*1.0\*206

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME//

> --------------------------------------------------------------------------------

> Install Started for PSS\*1.0\*206 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: MONTH DAY, YEAR

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Updating Routine file...

> Updating KIDS files...

> PSS\*1.0\*206 Installed.

> MONTH DAY, YEAR@TIME

> Not a production UCI

> Install Completed

# ## MOCHA 2.1B COMBINED FOLLOW UP BUILD Install Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select OPTION NAME: Kernel Installation & Distribution System

> Edits and Distribution ...

> Utilities ...

> Installation ...

> Patch Monitor Main Menu ...

> Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: Load a Distribution

> Enter a Host File: USER\$:\[ABC\]MOCHA_2_1_FOLLOW_UP_PSO \_OR_PSJ.KID

> KIDS Distribution saved on MONTH DAY, YEAR@TIME

> Comment: PSO\*500, PSJ\*347, OR\*469 from \[dosp\] ON 1/4/18

> This Distribution contains Transport Globals for the following Package(s):

> PSO\*7.0\*500, PSJ\*5.0\*347, OR\*3.0\*469

> Distribution OK!

> Want to Continue with Load? YES//

> Loading Distribution...

> PSO\*7.0\*500

> Use INSTALL NAME:

> MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0 to install this Distribution.

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

> Select INSTALL NAME: MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0

> =\> PSO\*500, PSJ\*347, OR\*469 from \[dosp\] ON 1/4/18 ;Created on Jan 04, 20

> This Distribution was loaded on Jan 04, 2018@14:23:44 with header of

> PSO\*500, PSJ\*347, OR\*469 from \[dosp\] ON 1/4/18 ;Created on Jan 04, 2018@13:4

> 8:28

> It consisted of the following Install(s):

> MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0 PSO\*7.0\*500 PSJ\*5.0\*347

> OR\*3.0\*469

> Checking Install for Package MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0

> Install Questions for MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0

> Checking Install for Package PSO\*7.0\*500

> Install Questions for PSO\*7.0\*500

> Checking Install for Package PSJ\*5.0\*347

> Install Questions for PSJ\*5.0\*347

> Checking Install for Package OR\*3.0\*469

> Install Questions for OR\*3.0\*469

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// Linux Telnet /SSh

> --------------------------------------------------------------------------------

> Install Started for MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: Jan 04, 2018

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Install Started for PSO\*7.0\*500 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: Jan 04, 2018

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Updating Routine file...

> Updating KIDS files...

> PSO\*7.0\*500 Installed.

> MONTH DAY, YEAR@TIME

> Not a production UCI

> NO Install Message sent

> Install Started for PSJ\*5.0\*347 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: Jan 04, 2018

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Updating Routine file...

> Updating KIDS files...

> PSJ\*5.0\*347 Installed.

> MONTH DAY, YEAR@TIME

> Not a production UCI

> NO Install Message sent

> Install Started for OR\*3.0\*469 :

> MONTH DAY, YEAR@TIME

> Build Distribution Date: Jan 04, 2018

> Installing Routines:

> MONTH DAY, YEAR@TIME

> Updating Routine file...

> Updating KIDS files...

> OR\*3.0\*469 Installed.

> MONTH DAY, YEAR@TIME

> Not a production UCI

> NO Install Message sent

> Updating Routine file...

> Updating KIDS files...

> MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0 Installed.

> MONTH DAY, YEAR@TIME

> No link to PACKAGE file

> Install Completed

# Appendix B: Rollback Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Follow Up Rollback Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: ??

Enter a filename and/or path to input Distribution.

Enter a Host File: USER\$:\[ABC\]MOCHA_2_1_RESTORE_FOLLOW_UP.KID

KIDS Distribution saved on Feb 08, 2018@10:19:41

Comment: MOCHA 2.1B RESTORE FOLLOW UP PSO OR PSJ (2.8.18)

This Distribution contains Transport Globals for the following Package(s):

RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B

Use INSTALL NAME: RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: INSTAll Package(s)

Select INSTALL NAME: RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B 2/8/18@10:21:

29

=\> MOCHA 2.1B RESTORE FOLLOW UP PSO OR PSJ (2.8.18) ;Created on Feb 08,

This Distribution was loaded on Feb 08, 2018@10:21:29 with header of

MOCHA 2.1B RESTORE FOLLOW UP PSO OR PSJ (2.8.18) ;Created on Feb 08, 2018@10

:19:41

It consisted of the following Install(s):

RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B

Checking Install for Package RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B

Install Questions for RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// Linux Telnet /SSh

RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B

--------------------------------------------------------------------------------

Install Started for RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B :

Feb 08, 2018@10:22:24

Build Distribution Date: Feb 08, 2018

Installing Routines:

Feb 08, 2018@10:22:25

Updating Routine file...

Updating KIDS files...

RESTORE FOLLOW UP PSO OR PSJ MOCHA 2.1B Installed.

Feb 08, 2018@10:22:25

No link to PACKAGE file

NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

## Combined Build Rollback Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: USER\$:\[ABC\]PSO_OR_PSJ_BEFORE_MOCHA_2_1_B.KID

KIDS Distribution saved on Sep 28, 2017@12:37:27

Comment: PSO OR PSJ BEFORE MOCHA 2.1B (9.28.17)

This Distribution contains Transport Globals for the following Package(s):

PSO OR PSJ BEFORE MOCHA 2.1B

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

PSO OR PSJ BEFORE MOCHA 2.1B

Use INSTALL NAME: PSO OR PSJ BEFORE MOCHA 2.1B to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: PSO OR PSJ BEFORE MOCHA 2.1B 9/29/17@10:55:35

=\> PSO OR PSJ BEFORE MOCHA 2.1B (9.28.17) ;Created on Sep 28, 2017@12:37

This Distribution was loaded on Sep 29, 2017@10:55:35 with header of

PSO OR PSJ BEFORE MOCHA 2.1B (9.28.17) ;Created on Sep 28, 2017@12:37:27

It consisted of the following Install(s):

PSO OR PSJ BEFORE MOCHA 2.1B

Checking Install for Package PSO OR PSJ BEFORE MOCHA 2.1B

Install Questions for PSO OR PSJ BEFORE MOCHA 2.1B

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;99999 HOME (CRT)

--------------------------------------------------------------------------------

Install Started for PSO OR PSJ BEFORE MOCHA 2.1B :

Sep 29, 2017@10:56:31

Build Distribution Date: Sep 28, 2017

Installing Routines:

Sep 29, 2017@10:56:31

Updating Routine file...

Updating KIDS files...

PSO OR PSJ BEFORE MOCHA 2.1B Installed.

Sep 29, 2017@10:56:31

No link to PACKAGE file

Install Completed

## PSS\*1\*178 Rollback Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INStallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: /home/sftp/patches/PSS_BEFORE_MOCHA_2_1_B.KID

KIDS Distribution saved on Sep 28, 2017@12:29:52

Comment: PSS BEFORE MOCHA 2.1B (9.28.17)

This Distribution contains Transport Globals for the following Package(s):

PSS BEFORE MOCHA 2.1B

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

PSS BEFORE MOCHA 2.1B

Use INSTALL NAME: PSS BEFORE MOCHA 2.1B to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 5 Backup a Transport Global

Select INSTALL NAME: PSS BEFORE MOCHA 2.1B 9/29/17@10:53:18

=\> PSS BEFORE MOCHA 2.1B (9.28.17) ;Created on Sep 28, 2017@12:29:52

This Distribution was loaded on Sep 29, 2017@10:53:18 with header of

PSS BEFORE MOCHA 2.1B (9.28.17) ;Created on Sep 28, 2017@12:29:52

It consisted of the following Install(s):

PSS BEFORE MOCHA 2.1B

Subject: Backup of PSS BEFORE MOCHA 2.1B install on Sep 29, 2017

Replace

Loading Routines for PSS BEFORE MOCHA 2.1B.............

Send mail to: USER,USER//

Select basket to send to: IN//

And Send to:

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: PSS BEFORE MOCHA 2.1B 9/29/17@10:53:18

=\> PSS BEFORE MOCHA 2.1B (9.28.17) ;Created on Sep 28, 2017@12:29:52

This Distribution was loaded on Sep 29, 2017@10:53:18 with header of

PSS BEFORE MOCHA 2.1B (9.28.17) ;Created on Sep 28, 2017@12:29:52

It consisted of the following Install(s):

PSS BEFORE MOCHA 2.1B

Checking Install for Package PSS BEFORE MOCHA 2.1B

Install Questions for PSS BEFORE MOCHA 2.1B

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;99999 HOME (CRT)

--------------------------------------------------------------------------------

Install Started for PSS BEFORE MOCHA 2.1B :

Sep 29, 2017@10:54:25

Build Distribution Date: Sep 28, 2017

Installing Routines:

Sep 29, 2017@10:54:25

Updating Routine file...

Updating KIDS files...

PSS BEFORE MOCHA 2.1B Installed.

Sep 29, 2017@10:54:25

No link to PACKAGE file

Install Completed

## XXPSS\*1\*178 Rollback Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INStallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: USER\$:\[ABC\]XXPSS_1_178.KID

KIDS Distribution saved on Oct 05, 2016@13:41:06

Comment: XXPSS\*1.0\*178 ROLLBACK (9.6.17)

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

XXPSS\*1.0\*178

Use INSTALL NAME: XXPSS\*1.0\*178 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: INStall Package(s)

Select INSTALL NAME: XXPSS\*1.0\*178 9/6/16@13:54:50

=\> XXPSS\*1.0\*178 ROLLBACK (9.6.17) ;Created on Sep 06, 2017@13:41:06

Checking Install for Package XXPSS\*1.0\*178

Install Questions for XXPSS\*1.0\*178

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TERMINAL

--------------------------------------------------------------------------------

Install Started for XXPSS\*1.0\*178 :

Sep 06, 2017@13:55:46

Build Distribution Date: Sep 06, 2017

Installing Routines:

Sep 06, 2017@13:55:46

Updating Routine file...

Updating KIDS files...

XXPSS\*1.0\*178 Installed.

Sep 06, 2017@13:55:47

No link to PACKAGE file

Install Completed

## XXMOCHA 2.1 COMBINED BUILD 1.0 Rollback Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INStallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: USER\$:\[ABC\] XXMOCHA_2_1_PSO_OR_PSJ.KID

KIDS Distribution saved on Sep 06, 2017@13:41:06

Comment: XXMOCHA 2.1 COMBINED BUILD ROLLBACK (9.6.17)

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

XXMOCHA 2.1 COMBINED BUILD 1.0

Use INSTALL NAME: XXMOCHA 2.1 COMBINED BUILD 1.0 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: INStall Package(s)

Select INSTALL NAME: XXMOCHA 2.1 COMBINED BUILD 1.0 9/6/17@13:54:50

=\> XXMOCHA 2.1 COMBINED BUILD 1.0 (9.6.17) ;Created on Sep 06, 2017@13:41:06

Checking Install for Package XXMOCHA 2.1 COMBINED BUILD 1.0

Install Questions for XXMOCHA 2.1 COMBINED BUILD 1.0

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TERMINAL

--------------------------------------------------------------------------------

Install Started for XXMOCHA 2.1 COMBINED BUILD 1.0:

Sep 06, 2017@13:55:46

Build Distribution Date: Sep 06, 2017

Installing Routines:

Sep 06, 2017@13:55:46

Updating Routine file...

Updating KIDS files...

XXMOCHA 2.1 COMBINED BUILD 1.0Installed.

Sep 06, 2017@13:55:47

No link to PACKAGE file

Install Completed

## Local Routine Backup Rollback Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: MAILMan Menu

VA MailMan 8.0 service for USER.USER@SITE.VA.GOV

Select MailMan Menu \<TEST ACCOUNT\> Option: R Read/Manage Messages

Select message reader: Classic//

Read mail in basket: IN// (29 messages, 20 new)

Last message number: 29 Messages in basket: 29 (20 new)

Enter ??? for help.

IN Basket Message: 1// ?

IN Basket, 29 messages (1-29), 20 new

\*=New/!=Priority.......Subject.........................From....................

26\. Backup of MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0 USER,USER

\*27. PSJ\*5.0\*340 Pharmacy Expired Order Status Change POSTMASTER

\*28. Released PSD\*3\*81 SEQ \#67 \<"National Patch Module"

\*29. Released PSD\*3\*79 SEQ \#66 \<"National Patch Module"

IN Basket Message: 1// 26

Subj: Backup of MOCHA 2.1 COMBINED FOLLOW UP BUILD 1.0 install on Jan \[#207452\]

01/04/18@14:26 5723 lines

From: USER.USER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

\$TXT PACKMAN BACKUP Created on Thursday, 1/4/18 at 14:26:06 by USER,USER at

SITE.MED.VA.GOV

\$ROU PSOBKDE1 (PACKMAN_BACKUP)

PSOBKDE1 ;BIR/MR-Sub-routines for Backdoor Rx Order Edit ;11/25/02

;;7.0;OUTPATIENT PHARMACY;\*\*117,133,372,402\*\*;DEC 1997;Build 8

;

LST1 ;

W @IOF

N PSOLCNT,DIRUT,DTOUT,DUOUT,I,PSODOSCT,PSODOSFL,PSOBKDF1

W !,"This is the amount of medication the patient is to receive as one dose"

W !,"for this order. This can be a numeric value, such as 325 or 650 or an"

W !,"amount with a unit of measure such as 325MG or 650MG. You may also enter"

W !,"a free text dosage, such as 1 Tablet or 2 Tablets",!

S PSOLCNT=5,PSOBKDF1=1

;

LST ;

I '\$G(PSOBKDF1) W @IOF S PSOBKDF1=1

N DIR I '\$D(DOSE("DD")) D Q

Type \<Enter\> to continue or '^' to exit: ^

Enter message action (in IN basket): Ignore// Xtract PackMan

Select PackMan function: ?

Answer with PackMan function NUMBER, or NAME

Choose from:

1 ROUTINE LOAD

2 GLOBAL LOAD

3 PACKAGE LOAD

4 SUMMARIZE MESSAGE

5 PRINT MESSAGE

6 INSTALL/CHECK MESSAGE

7 INSTALL SELECTED ROUTINE(S)

8 TEXT PRINT/DISPLAY

9 COMPARE MESSAGE

Select PackMan function: 6 INSTALL/CHECK MESSAGE

> **WARNING:** Installing this message will cause a permanent update of globals

and routines.

Do you really want to do this? NO//YES

..

Select PackMan function:

Template Revision History

| Date          | Version | Description                                                                                                                                                                                                                              | Author                                 |
|---------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| March 2016    | 2.2     | Changed the title from Installation, Back-Out, and Rollback Guide to Deployment and Installation Guide, with the understanding that Back-Out and Rollback belong with Installation.                                                      | VIP Team                               |
| February 2016 | 2.1     | Changed title from Installation, Back-Out, and Rollback Plan to Installation, Back-Out, and Rollback Guide as recommended by OI&T Documentation Standards Committee                                                                      | OI&T Documentation Standards Committee |
| December 2015 | 2.0     | The OI&T Documentation Standards Committee merged the existing *“Installation, Back-Out, Rollback Plan”* template with the content requirements in the OI&T End-user Documentation Standards for a more comprehensive Installation Plan. | OI&T Documentation Standards Committee |
| February 2015 | 1.0     | Initial Draft                                                                                                                                                                                                                            | Lifecycle and Release Management       |