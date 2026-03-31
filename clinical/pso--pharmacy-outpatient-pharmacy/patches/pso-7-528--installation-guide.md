---
title: PSO*7*528 MCCF EDI TAS Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: MCCF EDI TAS
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*528
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document describes how to deploy and install the multi-build PSO IB BUNDLE 10.0 (which includes PSO\7.0\528, IB\2.0\624) and how to back-out the product and rollback to a previous version or data set.
audience: 
keywords: 
  - table
  - contents
  - blockquote
  - back
  - installation
  - strong
  - procedure
  - rollback
  - deployment
  - style
page_count: 0
word_count: 2723
section_count: 31
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p528_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_0_p528_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

# Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePharmacy Build 10


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePharmacy Build 10](#medical-care-collection-fund-mccf-electronic-data-interchange-edi-transaction-applications-suite-tas-epharmacy-build-10)
- [Deployment, Installation, Back-Out, and Rollback Guide](#deployment-installation-back-out-and-rollback-guide)
    - [July 2019 Department of Veterans Affairs](#july-2019-department-of-veterans-affairs)
- [Artifact Rationale](#artifact-rationale)
- [Table of Tables](#table-of-tables)
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Timeline](#timeline)
  - [Site Readiness Assessment](#site-readiness-assessment)
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
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
    - [Mirror Testing or Site Production Testing](#mirror-testing-or-site-production-testing)
    - [After National Release but During the Designated Support Period](#after-national-release-but-during-the-designated-support-period)
    - [After National Release and Warranty Period](#after-national-release-and-warranty-period)
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
    - [Template Revision History](#template-revision-history)
> Outpatient Pharmacy PSO\*7.0\*528 Integrated Billing IB\*2.0\*624

# Deployment, Installation, Back-Out, and Rollback Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 1.0

![](pso-7-528-mccf-edi-tas-installation-guide/001.png)

### July 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date  | Version | Description | Author                         |
|-----------|-------------|-----------------|------------------------------------|
| July 2019 | 1.0         | Initial Version | <span class="mark">REDACTED</span> |

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

1.  [Introduction 1](#introduction)
    1.  [Purpose 1](#purpose)
    2.  [Dependencies 1](#dependencies)
    3.  [Constraints 1](#constraints)

[This patch is intended for a fully patched VistA system 1](#_bookmark4)

2.  [Roles and Responsibilities 1](#roles-and-responsibilities)
3.  [Deployment 2](#deployment)
    1.  [Timeline 2](#timeline)
    2.  [Site Readiness Assessment 2](#site-readiness-assessment)
        1.  [Deployment Topology (Targeted Architecture) 3](#_bookmark10)
        2.  [Site Information (Locations, Deployment Recipients) 3](#site-information-locations-deployment-recipients)
        3.  [Site Preparation 3](#site-preparation)
    3.  [Resources 3](#resources)
        1.  [Facility Specifics 3](#facility-specifics)
        2.  [Hardware 3](#hardware)
        3.  [Software 4](#software)
        4.  [Communications 4](#communications)
            1.  [Deployment/Installation/Back-Out Checklist 4](#deploymentinstallationback-out-checklist)
4.  [Installation 5](#installation)
    1.  [Pre-installation and System Requirements 5](#pre-installation-and-system-requirements)
    2.  [Platform Installation and Preparation 5](#platform-installation-and-preparation)
    3.  [Download and Extract Files 5](#download-and-extract-files)
    4.  [Database Creation 5](#database-creation)
    5.  [Installation Scripts 5](#installation-scripts)
    6.  [Cron Scripts 5](#cron-scripts)
    7.  [Access Requirements and Skills Needed for the Installation 5](#access-requirements-and-skills-needed-for-the-installation)
    8.  [Installation Procedure 6](#installation-procedure)
    9.  [Installation Verification Procedure 6](#installation-verification-procedure)
    10. [System Configuration 6](#system-configuration)
    11. [Database Tuning 6](#database-tuning)
5.  [Back-Out Procedure 6](#back-out-procedure)
    1.  [Back-Out Strategy 6](#back-out-strategy)
        1.  [Mirror Testing or Site Production Testing 6](#mirror-testing-or-site-production-testing)
        2.  [After National Release but During the Designated Support Period 6](#after-national-release-but-during-the-designated-support-period)
        3.  [After National Release and Warranty Period 6](#_bookmark40)
    2.  [Back-Out Considerations 7](#back-out-considerations)
        1.  [Load Testing 7](#load-testing)
        2.  [User Acceptance Testing 7](#user-acceptance-testing)
    3.  [Back-Out Criteria 8](#back-out-criteria)
    4.  [Back-Out Risks 8](#back-out-risks)
    5.  [Authority for Back-Out 8](#authority-for-back-out)
    6.  [Back-Out Procedure 9](#back-out-procedure-1)
    7.  [Back-out Verification Procedure 9](#back-out-verification-procedure)
6.  [Rollback Procedure 9](#rollback-procedure)
    1.  [Rollback Considerations 9](#rollback-considerations)
    2.  [Rollback Criteria 10](#rollback-criteria)
    3.  [Rollback Risks 10](#rollback-risks)
    4.  [Authority for Rollback 10](#authority-for-rollback)
    5.  [Rollback Procedure 10](#rollback-procedure-1)
    6.  [Rollback Verification Procedure 10](#rollback-verification-procedure)

# Table of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities 1](#_bookmark6)

> [Table 2: Site Preparation 3](#_bookmark13)

> [Table 3: Facility-Specific Features 3](#_bookmark16)

> [Table 4: Hardware Specifications 3](#_bookmark18)

> [Table 5: Software Specifications 4](#_bookmark20)

> [Table 6: Deployment/Installation/Back-Out Checklist 4](#_bookmark23)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes how to deploy and install the multi-build PSO IB BUNDLE 10.0 (which includes PSO\*7.0\*528, IB\*2.0\*624) and how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the multi-build PSO IB BUNDLE 10.0 (which includes PSO\*7.0\*528, IB\*2.0\*624) will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSO\*7.0\*512 and PSO\*7.0\*442 must be installed BEFORE PSO\*7.0\*528. IB\*2.0\*550 must be installed BEFORE IB\*2.0\*624.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark4" class="anchor"></span>This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark6" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><blockquote>
<p><strong>Tasks</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Project Phase (See Schedule)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>VA OI&amp;T, VA OI&amp;T</p>
<p>Health Product Support, and PMO (Leidos)</p></td>
<td>Deployment</td>
<td><blockquote>
<p>Plan and schedule deployment (including orchestration with vendors)</p>
</blockquote></td>
<td><blockquote>
<p>Planning</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>Local VAMC and CPAC processes</td>
<td>Deployment</td>
<td><blockquote>
<p>Determine and document the roles and responsibilities of those involved in the deployment.</p>
</blockquote></td>
<td><blockquote>
<p>Planning</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>Field Testing (Initial Operating Capability - IOC), Health Product Support Testing &amp; VIP Release Agent Approval</td>
<td>Deployment</td>
<td><blockquote>
<p>Test for operational readiness</p>
</blockquote></td>
<td><blockquote>
<p>Testing</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>Health product Support and Field Operations</td>
<td>Deployment</td>
<td><blockquote>
<p>Execute deployment</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><blockquote>
<p><strong>Tasks</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Project Phase (See Schedule)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5</td>
<td>Individual Veterans Administration Medical Centers (VAMCs)</td>
<td>Installation</td>
<td><blockquote>
<p>Plan and schedule installation</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>VIP Release Agent</p>
</blockquote></td>
<td>Installation</td>
<td><blockquote>
<p>Ensure authority to operate and that certificate authority security documentation is in place</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td></td>
<td>Installation</td>
<td><blockquote>
<p>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</p>
</blockquote></td>
<td><blockquote>
<p>N/A; only existing VistA system will be used</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>VA’s eBusiness team</td>
<td>Installations</td>
<td><blockquote>
<p>Coordinate training</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>VIP release Agent, Health Product Support &amp; the development team</td>
<td>Back-out</td>
<td><blockquote>
<p>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><p>VA OI&amp;T, VA OI&amp;T</p>
<p>Health Product Support, and MCCF EDI TAS</p>
<p>Development Team (Halfaker)</p></td>
<td>Post Deployment</td>
<td><blockquote>
<p>Hardware, Software and System Support</p>
</blockquote></td>
<td><blockquote>
<p>Warranty</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment is planned as a national rollout.

> This section provides the schedule and milestones for the deployment.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The duration of deployment and installation is 30 days, as depicted in the master deployment schedule<sup>1</sup>.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the deployment of the multi-build PSO IB BUNDLE 10.0 (which includes PSO\*7.0\*528, IB\*2.0\*624).

> <sup>1</sup> Project schedule (right click and select open hyperlink to access) <span id="_bookmark10" class="anchor"></span><span class="mark">REDACTED</span>

> Deployment Topology (Targeted Architecture)

> This multi-build PSO IB BUNDLE 10.0 (which includes PSO\*7.0\*528, IB\*2.0\*624) is to be nationally released to all VAMCs.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IOC sites are:

<span class="mark">REDACTED</span>

> Upon national release all VAMCs are expected to install this patch prior to or on the compliance date.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes preparation required by the site prior to deployment.

> <span id="_bookmark13" class="anchor"></span>Table 2: Site Preparation

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            | N/A                       | N/A                                         | N/A               | N/A       |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table lists facility-specific features required for deployment.

> <span id="_bookmark16" class="anchor"></span>Table 3: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes hardware specifications required at each site prior to deployment.

> <span id="_bookmark18" class="anchor"></span>Table 4: Hardware Specifications

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Hardware</strong></th>
<th><strong>Model</strong></th>
<th><strong>Version</strong></th>
<th><strong>Configuration</strong></th>
<th><blockquote>
<p><strong>Manufacturer</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Other</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Existing VistA system</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes software specifications required at each site prior to deployment.

> <span id="_bookmark20" class="anchor"></span>Table 5: Software Specifications

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Software</strong></th>
<th><strong>Make</strong></th>
<th><strong>Version</strong></th>
<th><blockquote>
<p><strong>Configuration</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Manufacturer</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Other</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Fully patched Outpatient Pharmacy package within VistA</td>
<td>N/A</td>
<td>7.0</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Fully patched Integrated Billing package within VistA</td>
<td>N/A</td>
<td>2.0</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The sites that are participating in field testing (IOC) will use the “Patch Tracking” message in Outlook to communicate with the ePharmacy eBusiness team, the developers, and product support personnel.

#### Deployment/Installation/Back-Out Checklist

> The Release Management team will deploy the multi-build PSO IB BUNDLE 10.0, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in Forum. Forum automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in Forum to identify when and by whom the patch was installed into the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch into their VistA production system. Therefore, this information does not need to be manually tracked in the chart below.

> <span id="_bookmark23" class="anchor"></span>Table 6: Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|--------------|---------|----------|-----------------------------------|
| Deploy       | N/A     | N/A      | N/A                               |
| Install      | N/A     | N/A      | N/A                               |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Multi-build PSO IB BUNDLE 10.0 is installable on a fully patched M(UMPS) VistA system and operates on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities which communicate with the underlying operating system and hardware, thereby providing each VistA package independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the PSO\*7.0\*528 documentation on the NPM in Forum for the detailed installation instructions. These instructions include any pre-installation steps if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the PSO\*7.0\*528, IB\*2.0\*624 documentation on the NPM to find related documentation that can be downloaded. The patch description of each patch will be transmitted as a MailMan message from the NPM. This message can also be pulled from the NPM. The patches themselves are bundled together into the multi-build PSO IB BUNDLE 10.0. The host file containing these patches must be downloaded separately. The file name is PSO_7_528_IB.KID and it can be found on the ANONYMOUS.SOFTWARE directory on any of the VistA SFTP servers (Hines, Salt Lake City).

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Multi-build PSO IB BUNDLE 10.0 modifies the VistA database. All changes can be found on the NPM documentation for this patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No installation scripts are needed for multi-build PSO IB BUNDLE 10.0 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No Cron scripts are needed for multi-build PSO IB BUNDLE 10.0 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Staff performing the installation of this multi-build will need access to FORUM’s NPM to view all patch descriptions. Staff will also need access and ability to download the host file from one of the VA’s SFTP servers. The software is to be installed by each site’s or region’s designated VA OI&T IT OPERATIONS SERVICE, Enterprise Service Lines, Vista Applications Division<sup>2</sup>.

> <sup>2</sup> “Enterprise service lines, VAD” for short. Formerly known as the IRM (Information Resources Management) or IT support.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Detailed instructions for installing the multi-build PSO IB BUNDLE 10.0 (which includes PSO\*7.0\*528, IB\*2.0\*624) can be found on the patch description for PSO\*7.0\*528, which can be found on the NPM. Installing the multi-build PSO IB BUNDLE 10.0 will install both component patches (PSO\*7.0\*528, IB\*2.0\*624).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the PSO\*7.0\*528 documentation on the NPM for detailed installation instructions. These instructions include any post installation steps if applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No system configuration changes are required for this patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No reconfiguration of the VistA database, memory allocations or other resources is necessary.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A decision to back out could be made during Site Mirror Testing, during Site Production Testing, or after National Release to the field (VAMCs). The best strategy decision is dependent on the stage during which the decision is made.

### Mirror Testing or Site Production Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a decision to back out is made during Mirror Testing or Site Production Testing, a new version of the patch can be used to restore the build components to their pre-patch condition.

### After National Release but During the Designated Support Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a decision to back out is made after national release and within the designated support period, a new patch will be entered into the NPM in Forum and will go through all the necessary milestone reviews, etc. as a patch for a patch. This patch could be defined as an emergency patch, and it could be used to address specific issues pertaining to the original patch or it could<span id="_bookmark40" class="anchor"></span> be used to restore the build components to their original pre-patch condition.

### After National Release and Warranty Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the support period, the VistA Maintenance Program will produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Changes implemented with multi-build PSO IB BUNDLE 10.0 can be backed out in their entirety or on an enhancement-by-enhancement basis. Either could be accomplished via a new version of multi-build PSO IB BUNDLE 10.0 if before national release or a new multi-build if after national release.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A. The back-out process will be executed at normal rather than raised job priority and is expected to have no significant effect on total system performance. After the reversion, the performance demands on the system will be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below are the acceptance criteria for each story included in PSO IB BUNDLE 10.0.

> US4165

- The TRICARE CHAMPVA Bypass/Override Report \[PSO TRI CVA OVERRIDE REPORT\] has been renamed to TRICARE CHAMPVA Override Report \[PSO TRI CVA OVERRIDE REPORT\].
- The TRICARE CHAMPVA Override Report \[PSO TRI CVA OVERRIDE REPORT\] shows a quantity for a partial fill that matches the quantity entered by the user when partially filling the prescription.
- The TRICARE CHAMPVA Override Report \[PSO TRI CVA OVERRIDE REPORT\] shows a cost in the \$BILLED column that is correct for the partial fill.
- The TRICARE CHAMPVA Override Report \[PSO TRI CVA OVERRIDE REPORT\] shows all overrides even if multiple overrides occur on the same day.
- The TRICARE CHAMPVA Override Report \[PSO TRI CVA OVERRIDE REPORT\] shows cost in \$BILLED column even though a claim is not submitted to bill.

> US4946

- For any patient with a primary commercial insurance and a billing eligibility of TRICARE or CHAMPVA, a non-billable prescription with a pseudo-reject of eT and eC displays on the Third Party Payer Rejects – Worklist.
- For any patient with a primary commercial insurance and a billing eligibility of TRICARE or CHAMPVA, a non-billable prescription with a pseudo-reject of eT and eC displays on the ECME User Screen.
- For any patient with a primary commercial insurance and a billing eligibility of TRICARE or CHAMPVA, a non-billable prescription with an ignored pseudo-reject of eT and eC displays on the Override Report.

> US4947

- If a patient has a billing eligibility of TRICARE or CHAMPVA, Non-billable rejects trigger the display of the Reject Notification screen with actions Ignore, Discontinue and Quit.

> Note: The Ignore action is only available if the user has PSO TRICARE/CHAMPVA security key.

- The Ignore action works as it currently works.
- The Discontinue action discontinues the prescription.
- The Quit action quits and sends the prescription to the worklist.

> US4948

- For a patient *with a primary commercial insurance,* the ignored reject is stored in the prescription file as a closed NCPDP reject, as it would if the reject had been ignored from the reject information screen.
- For a patient *with a primary commercial insurance,* the prescription is displayed on the ECME User Screen. The display indicates the reject is ignored and the comment displays.
- For a patient *without a primary commercial insurance,* the ignored reject is stored in the prescription file as a closed NCPDP reject, as it would if the reject had been ignored from the reject information screen.
- For a patient *without a primary commercial insurance,* the prescription is displayed on the ECME User Screen. The display indicates the reject is ignored and the comment displays.

> US4949

- A non-billable TRICARE eligible prescription that is ignored from the Reject Notification Screen will cause an entry in the ECME Reject Log.
- A non-billable CHAMPVA eligible prescription that is ignored from the Reject Notification Screen will cause an entry in the ECME Reject Log.

> US4989

- For a date of service prior to DATE, prescriptions for sensitive drugs will only be billable if active unexpired ROI is on file (assuming other non-ROI checks don’t make it non-billable).
- For a date of service on or after DATE, prescriptions for sensitive drugs will not become non- billable because an active unexpired ROI is not on file.
- A prescription for a sensitive drug can be non-billable, for reasons unrelated to the sensitive field, with a date of service on or after DATE. For example, the drug can be marked as non-billable in drug enter/edit or the patient insurance can be expired.
- Regression: Billable status of prescriptions with non-sensitive drugs is not impacted by this enhancement.
- Regression: ROI can be entered or edited for a patient, regardless of the expiration date. Date can be before, on or after DATE.
- Regression: ROI report can be run regardless of the requested date range. Dates can be before, on or after DATE.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It may be decided to back out this patch if the project is canceled, the requested changes implemented by multi-build PSO IB BUNDLE 10.0 are no longer desired by VA OI&T and the ePharmacy eBusiness team, or the patch produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since the ePharmacy software is tightly integrated with external systems, any attempt at a back- out should include close consultation with the external trading partners such as the Financial Services Center (FSC) and the Health Care Clearing House (HCCH) to determine risk.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Any back-out decision should be a joint decision of the Business Owner (or their representative) and the Program Manager with input from the Health Product Support (HPS) Application

> Coordinator, developers (both project and Tier 3 HPS), and if appropriate, external trading partners such as the VA Financial Service Center (FSC), Change Healthcare, or Transunion.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The back-out plan for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch.

> Back-Out Procedure prior to National Release

> If it is prior to national release, the site will be already working directly with the development team daily and should contact that team. The development team members will have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that development team can quickly address via a new software version. If the site is unsure whom to contact, they may log a ticket or contact Health Product Support - Management Systems Team.

> Multi-build PSO IB BUNDLE 10.0 contains the following build components:

- Routines
- Menu Options

> While the VistA KIDS installation procedure allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action, the back-out procedure for global, data dictionary and other VistA components is more complex and requires issuance of a follow-up patch to ensure all components are properly removed and/or restored. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with the restoration of the data.

> Please contact the EPMO team for assistance since this installed patch contains components in addition to routines.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Successful back-out is confirmed by verification that the back-out patch was successfully implemented. This includes successful installation and testing that the back-out it acted as expected, as defined together with the team the site contacted in section 5.5.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Rollback pertains to data. The data changes in this patch are specific to the operational software and platform settings. These data changes are covered in the Back-out procedures detailed elsewhere in this document.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

### Template Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date      | Version | Description                                                                                                                                                                                                                          | Author                             |
|---------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| March 2016    | 2.2         | Changed the title from Installation, Back- Out, and Rollback Guide to Deployment and Installation Guide, with the understanding that Back-Out and Rollback belong with Installation.                                                     | VIP Team                               |
| February 2016 | 2.1         | Changed title from Installation, Back-Out, and Rollback Plan to Installation, Back- Out, and Rollback Guide as recommended by OI&T Documentation Standards Committee                                                                     | OI&T Documentation Standards Committee |
| December 2015 | 2.0         | The OI&T Documentation Standards Committee merged the existing *“Installation, Back-Out, Rollback Plan”* template with the content requirements in the OI&T End-user Documentation Standards for a more comprehensive Installation Plan. | OI&T Documentation Standards Committee |
| February 2015 | 1.0         | Initial Draft                                                                                                                                                                                                                            | Lifecycle and Release Management       |