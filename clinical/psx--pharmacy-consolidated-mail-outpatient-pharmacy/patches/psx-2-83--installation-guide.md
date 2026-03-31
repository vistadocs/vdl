---
title: PSX*2*83 PSO*7*513 Installation Guide for MCCF, EDI, TAS
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: PSO*7*513  for MCCF, EDI, TAS
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2*83
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document describes how to deploy and install multi-build PSX PSO BUNDLE 1.0 (which includes PSX\2.0\83 and PSO\7.0\513) and how to back-out the product and rollback to a previous version or data set.
audience: 
keywords: 
  - table
  - contents
  - back
  - strong
  - installation
  - procedure
  - rollback
  - blockquote
  - deployment
  - testing
page_count: 0
word_count: 2149
section_count: 31
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_0_p83_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_0_p83_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

# Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePharmacy Build 2 Warranty


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePharmacy Build 2 Warranty](#medical-care-collection-fund-mccf-electronic-data-interchange-edi-transaction-applications-suite-tas-epharmacy-build-2-warranty)
- [Deployment, Installation, Back-Out, and Rollback Guide](#deployment-installation-back-out-and-rollback-guide)
    - [March 2018 Department of Veterans Affairs](#march-2018-department-of-veterans-affairs)
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
> Consolidated Mail Outpatient Pharmacy PSX\*2.0\*83 Outpatient Pharmacy PSO\*7.0\*513

# Deployment, Installation, Back-Out, and Rollback Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 1.0

![](psx-2-83-pso-7-513-installation-guide-for-mccf-edi-tas/001.png)

### March 2018 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date     | Version | Description | Author                         |
|--------------|-------------|-----------------|------------------------------------|
| January 2018 | 1.0         | Initial Version | <span class="mark">REDACTED</span> |

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

1.  [Introduction 1](#introduction)
    1.  [Purpose 1](#purpose)
    2.  [Dependencies 1](#dependencies)
    3.  [Constraints 1](#1.3_Constraints)
2.  [Roles and Responsibilities 1](#2_Roles_and_Responsibilities)
3.  [Deployment 2](#deployment)
    1.  [Timeline 2](#timeline)
    2.  [Site Readiness Assessment 2](#site-readiness-assessment)
        1.  [Deployment Topology (Targeted Architecture) 3](#3.2.1_Deployment_Topology_(Targeted_Arch)
        2.  [Site Information (Locations, Deployment Recipients) 3](#site-information-locations-deployment-recipients)
        3.  [Site Preparation 3](#site-preparation)
    3.  [Resources 3](#resources)
        1.  [Facility Specifics 3](#facility-specifics)
        2.  [Hardware 3](#hardware)
        3.  [Software 3](#software)
        4.  [Communications 4](#communications)
            1.  [Deployment/Installation/Back-Out Checklist 4](#deploymentinstallationback-out-checklist)
4.  [Installation 5](#installation)
    1.  [Pre-installation and System Requirements 5](#pre-installation-and-system-requirements)
    2.  [Platform Installation and Preparation 5](#platform-installation-and-preparation)
    3.  [Download and Extract Files 5](#download-and-extract-files)
    4.  [Database Creation 5](#database-creation)
    5.  [Installation Scripts 5](#installation-scripts)
    6.  [Cron Scripts 5](#4.6_Cron_Scripts)
    7.  [Access Requirements and Skills Needed for the Installation 5](#4.7_Access_Requirements_and_Skills_Neede)
    8.  [Installation Procedure 6](#installation-procedure)
    9.  [Installation Verification Procedure 6](#4.9_Installation_Verification_Procedure)
    10. [System Configuration 6](#4.10_System_Configuration)
    11. [Database Tuning 6](#4.11_Database_Tuning)
5.  [Back-Out Procedure 6](#back-out-procedure)
    1.  [Back-Out Strategy 6](#back-out-strategy)
        1.  [Mirror Testing or Site Production Testing 6](#mirror-testing-or-site-production-testing)
        2.  [After National Release but During the Designated Support Period 6](#5.1.2_After_National_Release_but_During_)
        3.  [After National Release and Warranty Period 7](#after-national-release-and-warranty-period)
    2.  [Back-Out Considerations 7](#back-out-considerations)
        1.  [Load Testing 7](#load-testing)
        2.  [User Acceptance Testing 7](#5.2.2_User_Acceptance_Testing)
    3.  [Back-Out Criteria 7](#back-out-criteria)
    4.  [Back-Out Risks 7](#5.4_Back-Out_Risks)
    5.  [Authority for Back-Out 8](#authority-for-back-out)
    6.  [Back-Out Procedure 8](#5.6_Back-Out_Procedure)
    7.  [Back-out Verification Procedure 8](#5.7_Back-out_Verification_Procedure)
6.  [Rollback Procedure 8](#6_Rollback_Procedure)
    1.  [Rollback Considerations 8](#rollback-considerations)
    2.  [Rollback Criteria 8](#rollback-criteria)
    3.  [Rollback Risks 8](#rollback-risks)
    4.  [Authority for Rollback 8](#authority-for-rollback)
    5.  [Rollback Procedure 9](#rollback-procedure-1)
    6.  [Rollback Verification Procedure 9](#6.6_Rollback_Verification_Procedure)

# Table of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities 1](#_bookmark5)

> [Table 2: Site Preparation 3](#_bookmark13)

> [Table 3: Facility-Specific Features 3](#_bookmark16)

> [Table 4: Hardware Specifications 3](#_bookmark18)

> [Table 5: Software Specifications 4](#_bookmark20)

> [Table 6: Deployment/Installation/Back-Out Checklist 4](#_bookmark23)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes how to deploy and install multi-build PSX PSO BUNDLE 1.0 (which includes PSX\*2.0\*83 and PSO\*7.0\*513) and how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the multi-build PSX PSO BUNDLE 1.0 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSX\*2.0\*81 must be installed BEFORE PSX\*2\*83.<span id="1.3_Constraints" class="anchor"></span> PSO\*7.0\*478 must be installed BEFORE PSO\*7.0\*513.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="2_Roles_and_Responsibilities" class="anchor"></span>This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark5" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

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
<th><strong>Tasks</strong></th>
<th><strong>Project Phase (See Schedule)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>VA OI&amp;T, VA OI&amp;T</p>
<p>Health Product Support, and PMO (Leidos)</p></td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
<td>Planning</td>
</tr>
<tr class="even">
<td>2</td>
<td>Local VAMC and CPAC processes</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
<td>Planning</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Field Testing (Initial Operating Capability - IOC), Health Product Support Testing &amp; VIP Release Agent Approval</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
<td>Testing</td>
</tr>
<tr class="even">
<td>4</td>
<td>Health product Support and Field Operations</td>
<td>Deployment</td>
<td>Execute deployment</td>
<td>Deployment</td>
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
<th><strong>Tasks</strong></th>
<th><strong>Project Phase (See Schedule)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5</td>
<td>Individual Veterans Administration Medical Centers (VAMCs)</td>
<td>Installation</td>
<td>Plan and schedule installation</td>
<td>Deployment</td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>VIP Release Agent</p>
</blockquote></td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
<td>Deployment</td>
</tr>
<tr class="odd">
<td>7</td>
<td></td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
<td>N/A; only existing VistA system will be used</td>
</tr>
<tr class="even">
<td>8</td>
<td>VA’s eBusiness team</td>
<td>Installations</td>
<td>Coordinate training</td>
<td>Deployment</td>
</tr>
<tr class="odd">
<td>9</td>
<td>VIP release Agent, Health Product Support &amp; the development team</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
<td>Deployment</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>VA OI&amp;T, VA OI&amp;T</p>
<p>Health Product Support, and MCCF EDI TAS</p>
<p>Development Team (Halfaker)</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
<td>Warranty</td>
</tr>
</tbody>
</table>

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment is planned as a national rollout.

> This section provides the schedule and milestones for the deployment.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The duration of deployment and installation is 30 days, as depicted in the master deployment schedule[<sup>1</sup>](#_bookmark9).

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the deployment of multi-build PSX PSO BUNDLE 1.0.

> <span id="_bookmark9" class="anchor"></span><sup>1</sup> Project schedule (right click and select open hyperlink to access) <span id="3.2.1_Deployment_Topology_(Targeted_Arch" class="anchor"></span><span class="mark">REDACTED</span>Deployment Topology (Targeted Architecture)

> Multi-build PSX PSO BUNDLE 1.0 is to be nationally released to all VAMCs.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IOC sites are:<span class="mark">REDACTED</span>

> Upon national release all VAMCs are expected to install this patch prior to or on the compliance date.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes preparation required by the site prior to deployment.

> <span id="_bookmark13" class="anchor"></span>Table 2: Site Preparation

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site/Other</strong></th>
<th><blockquote>
<p><strong>Problem/Change Needed</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Features to Adapt/Modify to New Product</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Actions/Steps</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Owner</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
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

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table lists facility-specific features required for deployment.

> <span id="_bookmark16" class="anchor"></span>Table 3: Facility-Specific Features

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
<th><strong>Space/Room</strong></th>
<th><strong>Features Needed</strong></th>
<th><strong>Other</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes hardware specifications required at each site prior to deployment.

> <span id="_bookmark18" class="anchor"></span>Table 4: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| Existing VistA system | N/A       | N/A         | N/A               | N/A              | N/A       |

> Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes software specifications required at each site prior to deployment.

> <span id="_bookmark20" class="anchor"></span>Table 5: Software Specifications

| Required Software                                                    | Make | Version                 | Configuration | Manufacturer | Other |
|--------------------------------------------------------------------------|----------|-----------------------------|-------------------|------------------|-----------|
| Fully patched Consolidated Mail Outpatient Pharmacy package within VistA | N/A      | 2.0                         | N/A               | N/A              | N/A       |
| Fully patched Outpatient Pharmacy package within VistA                   | N/A      | 7.0                         | N/A               | N/A              | N/A       |
| Prerequisite patches in PSX and PSO namespaces                           | N/A      | Nationally released version | N/A               | N/A              | N/A       |

> Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The sites that are participating in field testing (IOC) will use the “Patch Tracking” message in Outlook to communicate with the ePharmacy eBusiness team, the developers, and product support personnel.

#### Deployment/Installation/Back-Out Checklist

> The Release Management team will deploy multi-build PSX PSO BUNDLE 1.0, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in Forum. Forum will automatically track the patch as it is installed in the different VAMC production systems. One can run a report in Forum to identify when and by whom the patch was installed into the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch into their VistA production system. Therefore, this information does not need to be manually tracked in the chart below.

> <span id="_bookmark23" class="anchor"></span>Table 6: Deployment/Installation/Back-Out Checklist

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Activity</strong></th>
<th><blockquote>
<p><strong>Day</strong></p>
</blockquote></th>
<th><strong>Time</strong></th>
<th><blockquote>
<p><strong>Individual who completed task</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Deploy</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Install</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Back-Out</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Multi-build PSX PSO BUNDLE 1.0 is installable on a fully patched M(UMPS) VistA system and operates on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities which communicate with the underlying operating system and hardware, thereby providing each VistA package independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the PSX\*2.0\*83 patch description on the NPM in Forum for the detailed installation instructions. These instructions include any pre-installation steps if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The patch descriptions for PSX\*2.0\*83 and PSO\*7.0\*513 are on FORUM. When released, the patch description of each patch will be transmitted as a MailMan message to the G.PATCHES mailgroup. Each patch description contains the location where this Installation Guide can be downloaded. The patches themselves are bundled together into the multi-build PSX PSO BUNDLE 1.0. The host file containing these patches must be downloaded separately. The file name is PSX_2_83_PSO.KID and it can be found on the ANONYMOUS.SOFTWARE directory on any of the VistA SFTP servers (Hines, Salt Lake City).

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Multi-build PSX PSO BUNDLE 1.0 does not make changes to the VistA database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="4.6_Cron_Scripts" class="anchor"></span>No installation scripts are needed for multi-build PSX PSO BUNDLE 1.0 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="4.7_Access_Requirements_and_Skills_Neede" class="anchor"></span>No Cron scripts are needed for multi-build PSX PSO BUNDLE 1.0 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Staff performing the installation of this patch will need access to FORUM’s NPM to view both patch descriptions. Staff will also need access and ability to download the host file from one of

> the VA’s SFTP servers. The software is to be installed by each site’s or region’s designated VA OI&T IT OPERATIONS SERVICE, Enterprise Service Lines, VistA Applications Division[<sup>2</sup>](#_bookmark40).

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Detailed instructions for installing the multi-build PSX PSO BUNDLE 1.0 (which includes PSX\*2.0\*83 and PS0\*7.0\*513) can be found on the patch description for PSX\*2.0\*83, which can be found on the NPM. Installing the multi-build PSX PSO BUNDLE 1.0 will install both<span id="4.9_Installation_Verification_Procedure" class="anchor"></span> component patches (PSX\*2.0\*83 and PSO\*7.0\*513).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the PSX\*2.0\*83 documentation on the NPM for detailed installation instructions. These<span id="4.10_System_Configuration" class="anchor"></span> instructions include any post installation steps if applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="4.11_Database_Tuning" class="anchor"></span>No system configuration changes are required for this patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No reconfiguration of the VistA database, memory allocations or other resources is necessary.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A decision to back out could be made during Site Mirror Testing, during Site Production Testing, or after National Release to the field (VAMCs). The best strategy decision is dependent on the stage of testing during which the decision is made.

### Mirror Testing or Site Production Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a decision to back out is made during Mirror Testing or Site Production Testing, a new version<span id="5.1.2_After_National_Release_but_During_" class="anchor"></span> of the patch can be used to restore the build components to their pre-patch condition.

### After National Release but During the Designated Support Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a decision to back out is made after national release and within the designated support period, a new patch will be entered into the NPM in Forum and will go through all the necessary milestone reviews, etc., as a patch for a patch. This patch could be defined as an emergency

> <span id="_bookmark40" class="anchor"></span><sup>2</sup> “Enterprise service lines, VAD” for short. Formerly known as the IRM (Information Resources Management) or IT support.

> patch, and it could be used to address specific issues pertaining to the original patch or it could be used to restore the build components to their original pre-patch condition.

### After National Release and Warranty Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the support period, the VistA Maintenance Program will produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Changes implemented with multi-build PSX PSO BUNDLE 1.0 could be backed out via a new version of multi-build PSX PSO BUNDLE 1.0 if before national release or a new patch(es) if after national release.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A. The back-out process will be executed at normal rather than raised job priority and is expected to have no significant effect on total system performance. Subsequent to the reversion,<span id="5.2.2_User_Acceptance_Testing" class="anchor"></span> the performance demands on the system will be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below are the acceptance criteria for the one story in multi-build PSX PSO BUNDLE 1.0.

> DE453

- When the CMOP process runs, non-billable TRICARE/CHAMPVA prescriptions must receive the appropriate eT or eC reject code and be sent to the pharmacy worklist. If a prescription receives that reject and the reject is ignored by a user or resolved to a payable claim, then the prescription is sent to CMOP on the next scheduled transmission; otherwise the reject remains on the worklist and the prescription is not sent to CMOP. If the prescriptions do not receive eT or eC reject codes, the prescriptions are allowed to be transmitted to CMOP without any intervention by the pharmacist.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It may be decided to back out this patch if the project is canceled, the requested changes implemented by multi-build PSX PSO BUNDLE 1.0 are no longer desired by VA OI&T and the<span id="5.4_Back-Out_Risks" class="anchor"></span> ePharmacy eBusiness team, or the patch produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since the ePharmacy software is tightly integrated with external systems, any attempt at a back- out should include close consultation with the external trading partners such as the Financial Services Center (FSC) and the Health Care Clearing House (HCCH) to determine risk.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The order would come from: release coordinator (product support), portfolio director, and health product support. The order should be done in consultation with the development team and external trading partners such as FSC and the HCCH to determine the appropriate course of action. ePharmacy is tightly integrated with these external partners and a decision to back-out<span id="5.6_Back-Out_Procedure" class="anchor"></span> should not be made without their consultation.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Backing out enhancements to a VistA application is often complex. Normally, defects are repaired via a follow-up patch. The development team recommends that sites log a ticket if they wish to consider backing out a nationally released patch or contact the Enterprise Program Management Office (EPMO) team directly for specific solutions to their unique problems.

> Multi-build PSX PSO BUNDLE 1.0 contains the following build components:

- Routines

> The VistA KIDS installation procedure allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action. Restoring each of the routines to its previous version will successfully back out this build. This should not be performed while CMOP batch<span id="5.7_Back-out_Verification_Procedure" class="anchor"></span> processing is being performed.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Successful back-out is confirmed either by verification that the back-out patch was successfully<span id="6_Rollback_Procedure" class="anchor"></span> installed or that all routines were restored to their previous versions.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Rollback pertains to data. No data will be changed as part of this patch, therefore data rollback would never be necessary.

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

> <span id="6.6_Rollback_Verification_Procedure" class="anchor"></span>Not applicable.

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