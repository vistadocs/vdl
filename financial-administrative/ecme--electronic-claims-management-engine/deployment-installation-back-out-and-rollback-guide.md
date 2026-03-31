---
consolidated_title: "ecme deploy install rollback guide"
app_code: ECME
doc_type: DIBR
master_source: "BPS*1*24 ECME Deploy Install Rollback Guide"
master_pub_date: January 2019
consolidated_from: 11 versions
prior_versions:
  - "BPS*1.0*28 ECME Deploy Install Rollback Guide"
  - "BPS*1*21 ECME Deploy Install Rollback Guide"
  - "BPS*1*22 ECME Deploy Install Rollback Guide"
  - "BPS*1*23 ECME Deploy Install Rollback Guide"
  - "BPS*1*25 ECME Deploy Install Rollback Guide"
  - "BPS*1*26 ECME Deploy Install Rollback Guide"
  - "BPS*1*27 ECME Deploy Install Rollback Guide"
  - "BPS*1*29 ECME Deploy Install Rollback Guide"
  - "BPS*1*30 ECME Deploy Install Rollback Guide"
  - "BPS*1*31 ECME Deploy Install Rollback Guide"
---

# Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePharmacy Build 5 & 6


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePharmacy Build 5 & 6](#medical-care-collection-fund-mccf-electronic-data-interchange-edi-transaction-applications-suite-tas-epharmacy-build-5-6)
- [Integrated Billing IB\2.0\617 Pharmacy Data Management PSS\1.0\214](#integrated-billing-ib20617-pharmacy-data-management-pss10214)
- [Version 1.0](#version-10)
    - [January 2019 Department of Veterans Affairs](#january-2019-department-of-veterans-affairs)
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
> Electronic Claims Management Engine BPS\*1.0\*24 Outpatient Pharmacy PSO\*7.0\*512

# Integrated Billing IB\*2.0\*617 Pharmacy Data Management PSS\*1.0\*214

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Deployment, Installation, Back-Out, and Rollback Guide

# Version 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bps-1-24-ecme-deploy-install-rollback-guide/001.png)

### January 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 40%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>January 2019</td>
<td>1.0</td>
<td>Initial Version</td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

1.  [Introduction 1](#introduction)
    1.  [Purpose 1](#purpose)
    2.  [Dependencies 1](#dependencies)
    3.  [Constraints. 1](#constraints)

This patch is intended for a fully patched VistA system 1

2.  [Roles and Responsibilities 1](#roles-and-responsibilities)
3.  [Deployment 2](#deployment)
    1.  [Timeline 2](#timeline)
    2.  [Site Readiness Assessment 3](#site-readiness-assessment)
        1.  [Deployment Topology (Targeted Architecture) 3](#deployment-topology-targeted-architecture)
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
    6.  [Cron Scripts 6](#cron-scripts)
    7.  [Access Requirements and Skills Needed for the Installation 6](#access-requirements-and-skills-needed-for-the-installation)
    8.  [Installation Procedure 6](#installation-procedure)
    9.  [Installation Verification Procedure 6](#installation-verification-procedure)
    10. [System Configuration 6](#system-configuration)
    11. [Database Tuning 6](#database-tuning)
5.  [Back-Out Procedure 6](#back-out-procedure)
    1.  [Back-Out Strategy 6](#back-out-strategy)
        1.  [Mirror Testing or Site Production Testing 7](#mirror-testing-or-site-production-testing)
        2.  [After National Release but During the Designated Support Period 7](#after-national-release-but-during-the-designated-support-period)
        3.  [After National Release and Warranty Period 7](#after-national-release-and-warranty-period)
    2.  [Back-Out Considerations 7](#back-out-considerations)
        1.  [Load Testing 7](#load-testing)
        2.  [User Acceptance Testing 7](#user-acceptance-testing)
    3.  [Back-Out Criteria 12](#back-out-criteria)
    4.  [Back-Out Risks 12](#back-out-risks)
    5.  [Authority for Back-Out 12](#authority-for-back-out)
    6.  [Back-Out Procedure 12](#back-out-procedure-1)
    7.  [Back-out Verification Procedure 13](#back-out-verification-procedure)
6.  [Rollback Procedure 13](#rollback-procedure)
    1.  [Rollback Considerations 13](#rollback-considerations)
    2.  [Rollback Criteria 13](#rollback-criteria)
    3.  [Rollback Risks 13](#rollback-risks)
    4.  [Authority for Rollback 13](#authority-for-rollback)
    5.  [Rollback Procedure 13](#rollback-procedure-1)
    6.  [Rollback Verification Procedure 13](#rollback-verification-procedure)

# Table of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities 1

Table 2: Site Preparation 3

Table 3: Facility-Specific Features 3

Table 4: Hardware Specifications 4

Table 5: Software Specifications 4

Table 6: Deployment/Installation/Back-Out Checklist 5

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes how to deploy and install the multi-build BPS PSO IB PSS BUNDLE

> 12.0 (which includes BPS\*1.0\*24, PSO\*7.0\*512, IB\*2.0\*617, PSS\*1.0\*214) and how to back- out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the multi-build BPS PSO IB PSS BUNDLE 12.0 (which includes BPS\*1.0\*24, PSO\*7.0\*512, IB\*2.0\*617, PSS\*1.0\*214) will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BPS\*1.0\*23 must be installed BEFORE BPS\*1.0\*24.

PSO\*7.0\*408 and PSO\*7.0\*482 must be installed BEFORE PSO\*7\*512. IB\*2.0\*550 and IB\*2.0\*592 must be installed BEFORE IB\*2.0\*617.

PSS\*1.0\*220 must be installed BEFORE PSS\*1.0\*214.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

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
<th><blockquote>
<p><strong>Team</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Phase / Role</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>VA OI&amp;T, VA OI&amp;T</p>
<p>Health Product Support, and PMO (Leidos)</p>
</blockquote></td>
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
<td><blockquote>
<p>Local VAMC and CPAC processes</p>
</blockquote></td>
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
<td><blockquote>
<p>Field Testing (Initial Operating Capability - IOC), Health Product Support Testing &amp; VIP Release Agent Approval</p>
</blockquote></td>
<td>Deployment</td>
<td><blockquote>
<p>Test for operational readiness</p>
</blockquote></td>
<td><blockquote>
<p>Testing</p>
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
<th><blockquote>
<p><strong>Team</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Phase / Role</strong></p>
</blockquote></th>
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
<td>4</td>
<td><blockquote>
<p>Health product Support and Field Operations</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Execute deployment</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>Individual Veterans Administration Medical Centers (VAMCs)</p>
</blockquote></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td><blockquote>
<p>Plan and schedule installation</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>VIP Release Agent</p>
</blockquote></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td><blockquote>
<p>Ensure authority to operate and that certificate authority security documentation is in place</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td><blockquote>
<p>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</p>
</blockquote></td>
<td><blockquote>
<p>N/A; only existing VistA system will be used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>8</td>
<td><blockquote>
<p>VA’s eBusiness team</p>
</blockquote></td>
<td><blockquote>
<p>Installations</p>
</blockquote></td>
<td><blockquote>
<p>Coordinate training</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>9</td>
<td><blockquote>
<p>VIP release Agent, Health Product Support &amp; the development team</p>
</blockquote></td>
<td><blockquote>
<p>Back-out</p>
</blockquote></td>
<td><blockquote>
<p>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10</td>
<td><blockquote>
<p>VA OI&amp;T, VA OI&amp;T</p>
<p>Health Product Support, and MCCF EDI TAS</p>
<p>Development Team (Halfaker)</p>
</blockquote></td>
<td><blockquote>
<p>Post Deployment</p>
</blockquote></td>
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

> <sup>1</sup> Project schedule (right click and select open hyperlink to access) REDACTED

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the deployment of the multi-build BPS PSO IB PSS BUNDLE 12.0 (which includes BPS\*1.0\*24, PSO\*7.0\*512, IB\*2.0\*617, PSS\*1.0\*214).

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This multi-build BPS PSO IB PSS BUNDLE 12.0 (which includes BPS\*1.0\*24, PSO\*7.0\*512, IB\*2.0\*617, PSS\*1.0\*214) is to be nationally released to all VAMCs.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IOC sites are:

- Birmingham
- Eastern Kansas
- Little Rock
- Richmond

Upon national release all VAMCs are expected to install this patch prior to or on the compliance date.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes preparation required by the site prior to deployment.

> Table 2: Site Preparation

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
<th><strong>Problem/Change Needed</strong></th>
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
</tr>
</tbody>
</table>

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table lists facility-specific features required for deployment.

> Table 3: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes hardware specifications required at each site prior to deployment.

> Table 4: Hardware Specifications

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
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
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
<td>Existing VistA system</td>
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

> Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes software specifications required at each site prior to deployment.

> Table 5: Software Specifications

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
<th><blockquote>
<p><strong>Make</strong></p>
</blockquote></th>
<th><strong>Version</strong></th>
<th><strong>Configuration</strong></th>
<th><strong>Manufacturer</strong></th>
<th><strong>Other</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Fully patched Electronic Claims Management Engine package within VistA</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>1.0</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Fully patched Integrated Billing package within VistA</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>2.0</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Fully patched Outpatient Pharmacy package within VistA</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>7.0</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Fully patched Pharmacy Data Management package within VistA</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>1.0</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td><p>Prerequisite patches in BPS, PSO, IB, PSS yet to</p>
<p>be determined</p></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>Nationally released version</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

> Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The sites that are participating in field testing (IOC) will use the “Patch Tracking” message in Outlook to communicate with the ePharmacy eBusiness team, the developers, and product support personnel.

#### Deployment/Installation/Back-Out Checklist

> The Release Management team will deploy the multi-build BPS PSO IB PSS BUNDLE 12.0, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in Forum.

> Forum automatically tracks the patches as they are installed in the different VAMC production

> systems. One can run a report in Forum to identify when and by whom the patch was installed into the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch into their VistA production system. Therefore, this information does not need to be manually tracked in the chart below.

> Table 6: Deployment/Installation/Back-Out Checklist

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
<th><strong>Day</strong></th>
<th><strong>Time</strong></th>
<th><blockquote>
<p><strong>Individual who completed task</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Deploy</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Install</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Multi-build BPS PSO IB PSS BUNDLE 12.0 is installable on a fully patched M(UMPS) VistA system and operates on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities which communicate with the underlying operating system and hardware, thereby providing each VistA package independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the BPS\*1.0\*24 documentation on the NPM in Forum for the detailed installation instructions. These instructions include any pre-installation steps if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the BPS\*1.0\*24, PSO\*7.0\*512, IB\*2.0\*617, PSS\*1.0\*214 documentation on the NPM to find related documentation that can be downloaded. The patch description of each patch will be transmitted as a MailMan message from the NPM. This message can also be pulled from the NPM. The patches themselves are bundled together into the multi-build BPS PSO IB PSS BUNDLE 12.0. The host file containing these patches must be downloaded separately. The file name is BPS_1_24_PSO_IB_PSS.KID and it can be found on the ANONYMOUS.SOFTWARE directory on any of the VistA SFTP servers (REDACTED).

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Multi-build BPS PSO IB PSS BUNDLE 12.0 modifies the VistA database. All changes can be found on the NPM documentation for this patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No installation scripts are needed for multi-build BPS PSO IB PSS BUNDLE 12.0 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No Cron scripts are needed for multi-build BPS PSO IB PSS BUNDLE 12.0 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Staff performing the installation of this multi-build will need access to FORUM’s NPM to view all patch descriptions. Staff will also need access and ability to download the host file from one of the VA’s SFTP servers. The software is to be installed by each site’s or region’s designated VA OI&T IT OPERATIONS SERVICE, Enterprise Service Lines, Vista Applications Division<sup>2</sup>.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Detailed instructions for installing the multi-build BPS PSO IB PSS BUNDLE 12.0 (which includes BPS\*1.0\*24, PSO\*7.0\*512, IB\*2.0\*617, PSS\*1.0\*214) can be found on the patch description for BPS\*1.0\*24, which can be found on the NPM. Installing the multi-build BPS PSO IB PSS BUNDLE 12.0 will install all four component patches (BPS\*1.0\*24, PSO\*7.0\*512, IB\*2.0\*617, PSS\*1.0\*214).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the BPS\*1.0\*24 documentation on the NPM for detailed installation instructions. These instructions include any post installation steps if applicable.

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

> <sup>2</sup> “Enterprise service lines, VAD” for short. Formerly known as the IRM (Information Resources Management) or IT support.

### Mirror Testing or Site Production Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a decision to back out is made during Mirror Testing or Site Production Testing, a new version of the patch can be used to restore the build components to their pre-patch condition.

### After National Release but During the Designated Support Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a decision to back out is made after national release and within the designated support period, a new patch will be entered into the NPM in Forum and will go through all the necessary milestone reviews, etc. as a patch for a patch. This patch could be defined as an emergency patch, and it could be used to address specific issues pertaining to the original patch or it could be used to restore the build components to their original pre-patch condition.

### After National Release and Warranty Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the support period, the VistA Maintenance Program will produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Changes implemented with multi-build BPS PSO IB PSS BUNDLE 12.0 can be backed out in their entirety or on an enhancement-by-enhancement basis. Either could be accomplished via a new version of multi-build BPS PSO IB PSS BUNDLE 12.0 if before national release or a new multi-build if after national release.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A. The back-out process will be executed at normal rather than raised job priority and is expected to have no significant effect on total system performance. After the reversion, the performance demands on the system will be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below are the acceptance criteria for each story included in BPS PSO IB PSS BUNDLE 12.0.

US177

- Add new hidden action of ECS Edit Claim Submitted to the Reject Information screen and OP Medication screen (available on both Third Party Payer Rejects - Worklist and Third Party Payer Rejects - View/Process).
- The new ECS Edit Claim Submitted action can be used for both rejected and payable claims.
- Prompt for the Date of Service, only for released prescriptions.
- Date of Service will allow users to enter the fill date, any previous date of service and the release date when the prescription is released.
- Prompt for NCPDP fields that are not on a payer sheet and that are not stubs.
- Data in the transaction reflects the value entered by the user.
- "^" will allow the user to leave the action and return to the main screen.
- A date of service override displays in the ECME log.

US211

- Pharmacist can enter information from any action for a *TRICARE* dual-eligible patient from the Third Party Payer Rejects – *Worklist*. The claim transmits.
- Pharmacist can enter information from any action for a *CHAMPVA* dual-eligible patient from the Third Party Payer Rejects – *Worklis*t. The claim transmits.
- Pharmacist can enter information from any action for a *TRICARE* dual-eligible patient from the Third Party Payer Rejects - *View/Process* option. The claim transmits.
- Pharmacist can enter information from any action for a *CHAMPVA* dual-eligible patient from the Third Party Payer Rejects - *View/Process* option. The claim transmits.
- When the *TRICARE* dual-eligible claim is resubmitted using any action from the reject information screen, the coordination of benefit (e.g. primary or secondary), Rate Type and insurance company on the resubmitted claim should be the same as what was selected when the previous claim was submitted.
- When the *CHAMPVA* dual-eligible claim is resubmitted using any action from the reject information screen, the coordination of benefit (e.g. primary or secondary), Rate Type and insurance company on the resubmitted claim should be the same as what was selected when the previous claim was submitted.
- Verify that this change does not affect the OP Medications screen.

US582

- In the activity log section of View Prescription, the ECME Log label of “BILLING QUANTITY submitted” is replaced with “QUANTITY SUBMITTED ON CLAIM”.
- On the claim log, accessed from the ECME User Screen action of LOG, the label of “NCPDP Qty” is replaced with “Quantity Submitted on Claim”.
- On the claim log, accessed from the ECME User Screen action of LOG, the label of “Billed Qty” is replaced with “Rx Qty”.
- Verify the quantity submitted on the claim is calculated correctly (regression testing of current functionality).

US584

- The help text below the selection of the bingo board display refers to “a locally filled or CMOP Rx”.
- The help text for action EA Edit All Parameters, before the prompt “TRANSFER REJECT CODE:”, refers to “a locally filled or CMOP Rx”.
- The help text for action ET Edit Transfer Reject Code, before the prompt “TRANSFER REJECT CODE:”, refers to “a locally filled or CMOP Rx”.

US586

- The PRESCRIPTION filter question for option Third Party Payer Rejects – View/Process \[PSO REJECTS VIEW/PROCESS\] will accept an ECME number with a prefix of “E.” or “e.”. The next three acceptance criteria refer to the same prescription filter question.
- The ECME number is acceptable with or without leading zeros.
- An entry of “?” or “??” displays help text that matches the help text for option View ePharmacy Rx \[BPS RPT VIEW ECME RX\].
- Model the display of any error message after option View ePharmacy Rx \[BPS RPT VIEW ECME RX\].
- The option Third Party Payer Rejects – View/Process \[PSO REJECTS VIEW/PROCESS\] displays the correct prescription number that matches the ECME number entered by the user.

US601

- The wording of the informational line and prompt for OCN Open/Close Non-Billable Entry reflect the possibility of multiple selection.
- A user is able to select a range of entries (3.1-3.2).
- A user is able to select comma separated entries (3.1,4.2).
- A user is able to select a combination of ranges and comma separated entries (3.1-3.2,4.2).
- A user is able to select a single entry.

US1668

- In option Lookup into Dispense Drug File \[PSS LOOK\], the value for NCPDP QUANTITY MULTIPLIER displays up to five decimal places.

US2540

- Insert an additional line with Matched by, and the date and time the plan was matched information.

US2542

- The label of “Insurance:” and the insurance name displays under the prescription number.
- The label of “Reject:” displays under the label of “Insurance:”.
- Ignored rejects display with the label of “Reject:” and each reject code is on a separate entry. The reject code and description are displayed.

US2601

- The following filter questions have been added: Patient Name, Billed Amount.
- The following filter questions allow selection of one, many or all: CMOP/Mail/Window, Billing Type (Real time, etc.), Eligibility, Drug/Drug Class, Patient Name.
- Billed Amount can be selected for all amounts or a range.
- The report displays information that matches the answers to the filter questions.
- The report heading has changed: the following labels have a value of ALL or SELECTED: Insurance and Drugs/Classes.
- Excel capture instructions have been reworded as per the functional design.
- In the Excel version, the following headings have been abbreviated as per functional design: Eligibility, Released On, Fill Location, Fill Type, Rx COB, VA Ingredient Cost, VA Dispensing Fee, and Patient Name.
- In the Excel version, remove the parentheses around the Patient ID.
- In the Excel version, truncate the following fields: Division(12), Insurance Name(21), Patient Name(13), Patient ID(4), and Drug(15).

US2603

- The following filter questions have been added: Patient Name and Billed Amount.
- The following filter questions allow selection of one, many or all: CMOP/Mail/Window, Billing Type (Real time, etc.), Eligibility, Drug/Drug Class, and Patient Name.
- Billed Amount can be selected for all amounts or a range.
- The report displays information that matches the answers to the filter questions.
- The report heading has changed. The following labels have a value of ALL or SELECTED: Insurance and Drugs/Classes.
- Excel capture instructions have been reworded as per the functional design.
- In the Excel version, the following headings have been abbreviated as per functional design: Eligibility, Released On, Fill Location, Fill Type, Rx COB, VA Ingredient Cost, VA Dispensing Fee, Patient Name, Ingredient Cost Paid, and Dispensing Fee Paid.
- In the Excel version, remove the parentheses around the Patient ID.
- In the Excel version, truncate the following fields: Division(12), Insurance Name(21), Patient Name(13), Patient ID(4), and Drug(15).
- In the Excel version, evaluate the length of the line after truncating specified values. If the length exceeds 255 characters, truncate the Reason field to reduce the line length to 255 characters.

US2604

- The following filter questions have been added: Patient Name, and Billed Amount.
- The following filter questions allow selection of one, many or all: CMOP/Mail/Window, Billing Type (Real time, etc.), Eligibility, Drug/Drug Class, and Patient Name.
- Billed Amount can be selected for all amounts or a range.
- The report heading has changed: the following labels have a value of ALL or SELECTED: Insurance, Patient Name, and Drugs/Classes.
- The report heading has been changed to include ELIG as a column heading and the data displays on the report.
- Excel capture instructions have been reworded as per the functional design.
- In the Excel version, the following headings have been abbreviated as per functional design: Fill Location, Fill Type, Rx COB, VA Ingredient Cost, VA Dispensing Fee, and Patient Name.
- In the Excel version, remove the parentheses around the Patient ID.
- The Excel version has been changed to include ELIG as a column heading and the data displays on the report.
- In the Excel version, truncate the following fields: Division(12), Insurance Name(21), Patient Name(13), Patient ID(4), and Drug(15).

US2607

- The following filter question has been added: Patient Name and Closed Claim Reason.
- The following filter questions allow selection of one, many or all: CMOP/Mail/Window, Billing Type (Real time, etc.), Eligibility, Drug/Drug Class, Patient, and Closed Claim Reason.
- The report displays information that matches the answers to the filter questions.
- Excel capture instructions have been reworded as per the functional design.
- An informational message has been added above the Excel capture question.
- The report heading has changed. The following labels have a value of ALL or SELECTED: Insurance, Close Claim Reason, Drugs/Classes, Patient Name. Add Close Claim Reason after Insurance.
- Excel capture instructions have been reworded as per the functional design.
- In the Excel version, the following headings have been abbreviated as per functional design: Eligibility, Fill Location, Fill Type, and Patient Name.
- In the Excel version, remove Cardholder ID from the column heading and the data.
- In the Excel version, remove Reject Codes from the column heading and replace with MULT REJ. The data changes to Y or N depending on whether there are multiple rejects.
- In the Excel version, remove the parentheses around the Patient ID.
- In the Excel version, truncate the following fields: Division(12), Insurance Name(21), Patient Name(13), Patient ID(4), and Drug(15).
- In the Excel version, evaluate the length of the line after truncating specified values. If the length exceeds 255 characters, truncate the Reject Explanation to reduce the line length to 255 characters.

US2608

- The following filter questions have been added: Patient Name, and Billed Amount.
- The following filter questions allow selection of one, many or all: CMOP/Mail/Window, Eligibility, Drug/Drug Class, and Patient Name.
- Billed Amount can be selected for all amounts or a range.
- The report heading has changed. The following labels have a value of ALL or SELECTED: Insurance, Patient Name, and Drugs/Classes.
- Eligibility and Patient Name have been added to the report heading.
- Excel capture instructions have been reworded as per the functional design.
- In the Excel version, the following headings have been abbreviated as per functional design: Eligibility, Fill Location and Patient Name.
- In the Excel version, remove the parentheses around the Patient ID.
- In the Excel version, truncate the following fields: Division(12), Insurance Name(21), Patient Name(13), Patient ID(4), and Drug(15).
- The filter question for Billing Type (Real time, etc.) has been removed.

US2823

- The NPI number displays for all Pharmacy claims in TPJI, in the Claim Information section of the Claim Information screen.

US3529

- New fields are in VistA file BPS NCPDP FIELD DEFS \#9002313.91.
- Updated fields have the correct name in VistA file BPS NCPDP FIELD DEFS \#9002313.91.
- Developed fields can be transmitted on an outgoing claim.
- TPJI displays the additional field.
- The reject information screen displays additional fields.
- The ECME User Screen claim log displays additional fields.
- The testing tool allows a tester to specify values for additional fields.
- New incoming claim response fields are stored in VistA and can be viewed via CRI.

US3682

- Edit an active drug that does not have a value for any of the ePharmacy Billable fields. Enter “^” to exit. Verify that the message is displayed, a response is required, and there is no default.
- Edit an active drug that does not have a value for any of the ePharmacy Billable fields. Enter “^” to exit. Verify that the message is displayed, a response is required, and there is no default.
- Edit an active drug that does not have a value for any of the ePharmacy Billable fields. Enter “^” to exit. Verify that the message is displayed, a response is required, and there is no default.
- If the user answers YES to mark it, the three ePharmacy Billable fields are displayed.
- After answering YES, the user can enter through the three ePharmacy Billable fields, either answering the fields or not, and then return to the prompt to select the next name for editing.
- After answering YES, the user can enter “^” at any of the three ePharmacy Billable fields and then return to the prompt to select the next name for editing.
- If the user answers NO to mark it, the user is able to exit and is returned to the prompt to select the next name for editing.
- If the drug is inactive, the message does not display.

US4039

- The prompt for Drug/Drug Class will allow a drug to be deleted.
- The prompt for Drug/Drug Class will allow a drug class to be deleted.
- The prompt for Reject Codes will allow a reject code to be deleted.
- The prompt for Prescribers will allow a prescriber to be deleted.
- The prompt for Patients will allow a patient to be deleted.
- The prompt for Close Claim Reason will allow a close claim reason to be deleted.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It may be decided to back out this patch if the project is canceled, the requested changes implemented by multi-build BPS PSO IB PSS BUNDLE 12.0 are no longer desired by VA OI&T and the ePharmacy eBusiness team, or the patch produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since the ePharmacy software is tightly integrated with external systems, any attempt at a back- out should include close consultation with the external trading partners such as the Financial Services Center (FSC) and the Health Care Clearing House (HCCH) to determine risk.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Any back-out decision should be a joint decision of the Business Owner (or their representative) and the Program Manager with input from the Health Product Support (HPS) Application Coordinator, developers (both project and Tier 3 HPS), and if appropriate, external trading partners such as the VA Financial Service Center (FSC), Change Healthcare, or Transunion.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The back-out plan for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch.

> Back-Out Procedure prior to National Release

> If it is prior to national release, the site will be already working directly with the development team daily and should contact that team. The development team members have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that development team can quickly address via a new software version. If the site is unsure who to contact they may log a ticket of contact Health Product Support - Management Systems Team.

> Multi-build BPS PSO IB PSS BUNDLE 12.0 contains the following build components:

- Routines
- File entries in multiple files
- Data Dictionary Changes
- Protocols
- List Templates
- Menu Options

> While the VistA KIDS installation procedure allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action, the back-out procedure for global, data

> dictionary and other VistA components is more complex and requires issuance of a follow-up patch to ensure all components are properly removed and/or restored. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with the restoration of the data.

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

> Template Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 45%" />
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
<td>March 2016</td>
<td>2.2</td>
<td>Changed the title from Installation, Back- Out, and Rollback Guide to Deployment and Installation Guide, with the understanding that Back-Out and Rollback belong with Installation.</td>
<td>VIP Team</td>
</tr>
<tr class="even">
<td>February 2016</td>
<td>2.1</td>
<td>Changed title from Installation, Back-Out, and Rollback Plan to Installation, Back- Out, and Rollback Guide as recommended by OI&amp;T Documentation Standards Committee</td>
<td>OI&amp;T Documentation Standards Committee</td>
</tr>
<tr class="odd">
<td>December 2015</td>
<td>2.0</td>
<td><p>The OI&amp;T Documentation Standards Committee merged the existing</p>
<p><em>“Installation, Back-Out, Rollback Plan”</em> template with the content requirements in the OI&amp;T End-user Documentation Standards for a more comprehensive Installation Plan.</p></td>
<td>OI&amp;T Documentation Standards Committee</td>
</tr>
<tr class="even">
<td>February 2015</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td>Initial Draft</td>
<td>Lifecycle and Release Management</td>
</tr>
</tbody>
</table>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: BPS*1*23 ECME Deploy Install Rollback Guide

### August 2018 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date    | Version | Description | Author |
|-------------|-------------|-----------------|------------|
| August 2018 | 1.0         | Initial Version | REDACTED   |

### From: BPS*1*27 ECME Deploy Install Rollback Guide

### December 2020 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 40%" />
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
<td>December 2020</td>
<td>1.0</td>
<td>Initial Version</td>
<td><p>MCCF EDI TAS</p>
<p>ePharmacy Development Team</p></td>
</tr>
</tbody>
</table>

### Template Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date   | Version | Description                                                                                                                                                                      | Author |
|------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| March 2016 | 2.2         | Changed the title from Installation, Back- Out, and Rollback Guide to Deployment and Installation Guide, with the understanding that Back-Out and Rollback belong with Installation. | VIP Team   |

| Date      | Version | Description                                                                                                                                                                                                                          | Author                             |
|---------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| February 2016 | 2.1         | Changed title from Installation, Back-Out, and Rollback Plan to Installation, Back- Out, and Rollback Guide as recommended by OI&T Documentation Standards Committee                                                                     | OI&T Documentation Standards Committee |
| December 2015 | 2.0         | The OI&T Documentation Standards Committee merged the existing *“Installation, Back-Out, Rollback Plan”* template with the content requirements in the OI&T End-user Documentation Standards for a more comprehensive Installation Plan. | OI&T Documentation Standards Committee |
| February 2015 | 1.0         | Initial Draft                                                                                                                                                                                                                            | Lifecycle and Release Management       |

### From: BPS*1*22 ECME Deploy Install Rollback Guide

### November 2017 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date     | Version | Description                          | Author |
|--------------|-------------|------------------------------------------|------------|
| July 2017    | 1.0         | Initial Version                          | REDACTED   |
| August 2017  | 2.0         | Updated Acceptance Criteria              | REDACTED   |
| August 2017  | 3.0         | Changed two instances of “FTP” to “SFTP” | REDACTED   |
| October 2017 | 4.0         | Updated acceptance criteria for US576    | REDACTED   |
| October 2017 | 5.0         | Removed reference to Albany FTP site     | REDACTED   |

### From: BPS*1*26 ECME Deploy Install Rollback Guide

### April 2020 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date   | Version | Description | Author |
|------------|-------------|-----------------|------------|
| April 2020 | 1.0         | Initial Version | REDACTED   |

### From: BPS*1*21 ECME Deploy Install Rollback Guide

### August 2017 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date   | Version | Description | Author |
|------------|-------------|-----------------|------------|
| April 2017 | 1.0         | Initial Version | REDACTED   |

### From: BPS*1*25 ECME Deploy Install Rollback Guide

### March 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 40%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>March 2019</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Initial Version</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>
