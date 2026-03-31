---
title: PRCA*4.5*345 and IB*2.0*639 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: and IB*2.0*639
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5*345
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document describes how to deploy and install the multi-build (which includes patches PRCA\4.5\345 and IB\2.0\639) as well as how to back-out the product and rollback to a previous version or data set.
audience: 
keywords: 
  - table
  - contents
  - blockquote
  - strong
  - back
  - style
  - width
  - installation
  - deployment
  - class
page_count: 0
word_count: 2816
section_count: 31
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p345_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p345_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

# Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePayments Build 9


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePayments Build 9](#medical-care-collection-fund-mccf-electronic-data-interchange-edi-transaction-applications-suite-tas-epayments-build-9)
- [Deployment, Installation, Back-Out and Rollback Guide](#deployment-installation-back-out-and-rollback-guide)
    - [October 2020 Department of Veterans Affairs](#october-2020-department-of-veterans-affairs)
- [Artifact Rationale](#artifact-rationale)
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
    - [Template Revision History](#template-revision-history)
> Accounts Receivable PRCA\*4.5\*345 Integrated Billing IB\*2.0\*639 Version 1.0

# Deployment, Installation, Back-Out and Rollback Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-345-and-ib-2-0-639-deployment-installation-back-out-and-rollback-guide/001.png)

### October 2020 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date     | Version | Description | Author |
|--------------|-------------|-----------------|------------|
| October 2020 | 1.0         | Initial Version | REDACTED   |

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.
# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes how to deploy and install the multi-build (which includes patches PRCA\*4.5\*345 and IB\*2.0\*639) as well as how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the multi-build PRCA IB EPAYMENTS BUNDLE 5.0 (which includes patches PRCA\*4.5\*345 and IB\*2.0\*639) will be deployed and installed, as well as how the patches are to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following patches must be installed before PRCA\*4.5\*345 and IB\*2.0\*639:

- PRCA\*4.5\*211
- PRCA\*4.5\*332
- IB\*2.0\*488
- IB\*2.0\*633

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch is intended for a fully patched VistA system.

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
<th><blockquote>
<p><strong>Team</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Phase / Role</strong></p>
</blockquote></th>
<th><strong>Tasks</strong></th>
<th><strong>Project Phase (See Schedule)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>VA OI&amp;T, VA OI&amp;T</p>
<p>Health Product Support&amp; PMO (Leidos)</p>
</blockquote></td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
<td>Planning</td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>Local VAMC and CPAC processes</p>
</blockquote></td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
<td>Planning</td>
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
<th><strong>Tasks</strong></th>
<th><strong>Project Phase (See Schedule)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>Field Testing (Initial Operating Capability - IOC), Health Product Support Testing &amp; VIP Release Agent Approval</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td>Test for operational readiness</td>
<td>Testing</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>Health Product Support and Field Operations</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td>Execute deployment</td>
<td>Deployment</td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>Individual Veterans Administration Medical Centers (VAMCs)</p>
</blockquote></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td>Plan and schedule installation</td>
<td>Deployment</td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>VIP Release Agent</p>
</blockquote></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
<td>Deployment</td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>N/A for this patch as we are using only the existing VistA system</p>
</blockquote></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>VA’s eBusiness team</p>
</blockquote></td>
<td><blockquote>
<p>Installations</p>
</blockquote></td>
<td>Coordinate training</td>
<td>Deployment</td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>VIP release Agent, Health Product Support &amp; the development team</p>
</blockquote></td>
<td><blockquote>
<p>Back-out</p>
</blockquote></td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
<td>Deployment</td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>No changes to current process – we are using the existing VistA system</p>
</blockquote></td>
<td><blockquote>
<p>Post Deployment</p>
</blockquote></td>
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

> The deployment and installation is scheduled to run for 30 days, as depicted in the master deployment schedule<sup>1</sup>.

> 1 Project schedule (right click and select open hyperlink to access) [<u>MCCF TAS IMS Schedule.zip</u>](https://vaww.vashare.oit.va.gov/sites/mccf/Schedules/MCCF%20TAS%20IMS%20Schedule.zip)

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the deployment of multi-build build PRCA IB EPAYMENTS BUNDLE 5.0 (which includes PRCA\*4.5\*345 and IB\*2.0\*639).

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This multi-build build PRCA IB EPAYMENTS BUNDLE 5.0 (which includes PRCA\*4.5\*345 and IB\*2.0\*639) is to be nationally released to all VAMCs.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The test sites for IOC testing are:

> ASHVILLE, NC CHARLESTON, SC NORTHPORT, NY

> Upon national release, all VAMCs are expected to install this patch by the compliance date.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes preparation required by the site prior to deployment.

> <span id="_bookmark12" class="anchor"></span>Table 2: Site Preparation

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

> <span id="_bookmark15" class="anchor"></span>Table 3: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes hardware specifications required at each site prior to deployment.

> <span id="_bookmark17" class="anchor"></span>Table 4: Hardware Specifications

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

> <span id="_bookmark19" class="anchor"></span>Table 5: Software Specifications

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Software</strong></th>
<th><strong>Make</strong></th>
<th><strong>Version</strong></th>
<th><strong>Configuration</strong></th>
<th><strong>Manufacturer</strong></th>
<th><blockquote>
<p><strong>Other</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Fully patched Accounts Receivable package within VistA</td>
<td>N/A</td>
<td>4.5</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PRCA*4.5*211</td>
<td>N/A</td>
<td>Nationally released version</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PRCA*4.5*332</td>
<td>N/A</td>
<td>Nationally released version</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Fully patched Integrated Billing package within VistA</td>
<td>N/A</td>
<td>2.0</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB*2.0*488</td>
<td>N/A</td>
<td>Nationally released version</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB*2.0*633</td>
<td>N/A</td>
<td>Nationally released version</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The sites that are participating in field testing (IOC) will use the “Patch Tracking” message in Outlook to communicate with the ePayments eBusiness team, the developers, and product support personnel.

#### Deployment/Installation/Back-Out Checklist

> The Release Management team will deploy the multi-build PRCA IB EPAYMENTS BUNDLE 5.0, which is tracked in the NPM in Forum, nationally to all VAMCs. Forum automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in Forum to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run to identify which sites have not installed the patch in their VistA production system as of that moment in time.

> Therefore, this information does not need to be manually tracked in the chart below.

> <span id="_bookmark22" class="anchor"></span>Table 6: Deployment/Installation/Back-Out Checklist

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
<th><blockquote>
<p><strong>Time</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Individual who completed task</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Deploy</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Install</td>
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

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PRCA\*4.5\*345 and IB\*2.0\*639 patches to the existing VistA Accounts Receivable 4.5 packages, are installable on a fully patched M(UMPS) VistA system and operate on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities which communicate with the underlying operating system and hardware, thereby providing Integrated Billing and Accounts Receivable independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to PRCA\*4.5\*345 and IB\*2.0\*639 documentation on the National Patch Module (NPM) on Forum for the detailed installation instructions. These instructions would include any pre- installation steps if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the PRCA\*4.5\*345 and IB\*2.0\*639 documentation on the NPM to find the location of related documentation that can be downloaded. PRCA\*4.5\*345 and IB\*2.0\*639 will be distributed via host file PRCA_IB_EPAYMENTS_BUNDLE_5_0.KID.

> The host file is available at the following location:

> /srv/vista/patches/SOFTWARE/PRCA_IB_EPAYMENTS_BUNDLE_5_0.KID

> If the above link is not functional to retrieve the host file, this URL can be used: REDACTED

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Multi-build build PRCA IB EPAYMENTS BUNDLE 5.0 modifies the VistA database. All changes can be found on the NPM documentation for these patches.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No installation scripts are needed for multi-build build PRCA IB EPAYMENTS BUNDLE 5.0 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No Cron scripts are needed for multi-build build PRCA IB EPAYMENTS BUNDLE 5.0 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following staff will need access to the host file PRCA_IB_EPAYMENTS_BUNDLE_5_0.KID containing the PRCA\*4.5\*345 and IB\*2.0\*639 patches. The software is to be installed by the site’s or region’s designated: VA OI&T IT OPERATIONS SERVICE, Enterprise Service Lines, VistA Applications Division<sup>2</sup>.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to PRCA\*4.5\*345 and IB\*2.0\*639 documentation on the NPM for the detailed installation instructions.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to PRCA\*4.5\*345 and IB\*2.8\*639 documentation on the NPM for the detailed installation instructions. These instructions would include any post installation steps if applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No system configuration changes are required for this patch.

> <sup>2</sup> “Enterprise service lines, VAD” for short. Formerly known as the IRM (Information Resources Management) or IT support.

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

> If a decision to back out is made after national release and within the designated support period, a new patch will be entered into the NPM in Forum and will go through all the necessary milestone reviews, etc. as a patch for a patch. This patch could be defined as an emergency patch, and it could be used to address specific issues pertaining to the original patch or it could be used to restore the build components to their original pre-patch condition.

### After National Release and Warranty Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the support period, the VistA Maintenance Program will produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Changes implemented with multi-build PRCA IB EPAYMENTS BUNDLE 5.0 can be backed out in their entirety or on an enhancement-by-enhancement basis. Either could be accomplished via a new version of multi-build PRCA IB EPAYMENTS BUNDLE 5.0 if before national release or a new multi-build if after national release.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A. The back-out process would be executed at normal, rather than raised job priority, and is expected to have no significant effect on total system performance. Subsequent to the reversion, the performance demands on the system would be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Transfer Language removed from the EDI Lockbox 3rd Party Exceptions (EXC) data transmissions worklist \[RCDPE EXCEPTION PROCESSING\]. Previous software updates removed the functionality in the Exceptions worklist to ‘transfer’ EEOB data to a different site. However, references to this previous functionality still existed on the worklist. This enhancement removed any references to the previous ‘transfer’ functionality.
2.  Deposit number was added to the detail lines in the Auto-Post Report \[RCDPE AUTO-POST REPORT\]. The deposit number was added to the second line of detail information for a receipt in front of the trace number. with payments to be auto-decreased by the Nightly AR Process. This resulted in changes to the following areas:
3.  Ability to auto-decrease pharmacy claims with payments. New site parameter questions were added to allow pharmacy claims
    1.  New site parameter questions were added to the EDI Lockbox Parameters \[RCDPE EDI LOCKBOX PARAMETERS\] option.
    2.  The Auto-Parameter History Report \[RCDPE AUTO PARAM HIST REPORT\] was modified to include changes to pharmacy auto-decrease parameters.
    3.  The EDI Lockbox Parameters Report \[RCDPE SITE PARAMETER REPORT\] was modified to include pharmacy auto-decrease parameters.
    4.  The EDI Lockbox Exclusion Report Audit Report \[\[RCDPE EXCLUSION AUDIT REPORT\] was modified to include changes to payer exclusions for pharmacy claims with payments.
    5.  The EDI Lockbox Parameters Audit Report \[RCDPE PARAMETER AUDIT REPORT\] was modified to include changes to site parameters for pharmacy claims with payments.
    6.  The Nightly AR Process was modified to auto-decrease pharmacy claims with payments that meet site parameter criteria.
4.  Ability to auto-decrease first party claims when payments have been posted to the corresponding 3rd party claim. The Nightly AR Process will now auto-decrease 1st party claims that are released to the veteran and the entire balance is still open including any claims that are already released and claims that the system needs to release and credit. This resulted in changes to the following areas:
    1.  A new site parameter was added to the AR SITE PARAMETER File (#342) to enable/disable 1st party auto-decrease.
    2.  The Nightly AR Process was modified to auto-decrease 1st party claims that meet the site parameter settings.
    3.  A new Report 1st Party Auto-Decrease Adjustment Report \[RCDPE AUTO-DECREASE 1ST\] was added to the EDI LOCKBOX REPORTS MENU \[RCDPE EDI LOCKBOX REPORTS MENU\] to display the 1st party auto-decreases done by the Nightly AR Process.
    4.  A new Report, First Party COPAY Manual vs Auto-Decrease Report \[RCDPE 1ST PARTY AUTO VS MAN\] was added to the Audit Reports \[RCDPE EDI LOCKBOX AUDIT RPRTS\] sub-menu of the EDI LOCKBOX Reports Menu \[RCDPE EDI LOCKBOX REPORTS MENU\]

> to display statistics about first party claims that were manually decreased versus ones that auto- decreased by the Nightly AR Process.

5.  Fixed an issue with TRICARE EFT lock-outs which was preventing medical EFT Lock-outs from being processed if TRICARE ERAs aged beyond the NUMBER OF DAYS (AGE) OF UNPOSTED TRICARE EFTS TO PREVENT POSTING site parameter setting.
6.  Added a notification e[mail to the REDACTED](mailto:vha835payerinquiry@va.gov) outlook mail group to make sure the ePayments eBusiness group is aware of site transmission errors in a timely manner.
7.  Added the display of the Patient name a claim was originally assigned to in the Third Party Joint Inquiry Option (TPJI) \[IBJ THIRD PARTY JOINT INQUIRY\] if the claim was the result of a split/edit.
8.  In the AR EDI LOCKBOX MESSAGES file (#344.5), the SEQUENCE RECIEVED is now allowed to be up to 999, where previously it was a maximum of 99.
9.  Electronic Explanation of Benefits (EEOB) will now auto-verify if the billed amount on the EEOB does not match the billed amount in VistA. Existing checks on patient name and service date remain in place. This change was made to allow pharmacy claims to auto-verify when the billed amount on the EEOB is a penny less than the billed amount on the claim in VistA.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The project is canceled or the requested changes implemented by multi-build build PRCA IB EPAYMENTS BUNDLE 5.0 are no longer desired by VA OI&T and the ePayments eBusiness team, or the patch produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since the ePayments software is tightly integrated with external systems, any attempt at a back- out should include close consultation with the external trading partners such as the Financial Services Center (FSC), the Health Care Clearing House (HCCH), the VA 3rd Party Lockbox bank, and the Financial Management System (FMS) to determine risk.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Any back-out decision should be a joint decision of the Business Owner (or their representative) and the Program Manager with input from the Health Product Support (HPS) Application Coordinator, developers (both project and Tier 3 HPS), and if appropriate, external trading partners such as the VA Financial Service Center (FSC), the Health Care Clearing House (HCCH), VA 3<sup>rd</sup> Party Lockbox bank, and the FMS to determine the appropriate course of action. ePayments is tightly integrated with these external partners and a back-out of the patch<span id="_bookmark46" class="anchor"></span> should not be a standalone decision.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The back-out plan for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA rollback is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch.

> Back-Out Procedure prior to National Release. If it is prior to national release, the site will be already working directly with the development team daily and should contact that team. The development team members will have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that development team can quickly address via a new software version. If the site is unsure who to contact they may log a ticket of contact Health Product Support - Management Systems Team. Please contact the EPMO development team for assistance since this installed patch contains components in addition to routines.

> The Multi-build build PRCA IB EPAYMENTS BUNDLE 5.0 contains the following build components.

- Data Dictionary Changes
- Options
- Routines
- Templates
- Modifications to the following files:
  - AR SITE PARAMETER File \[#342\]
  - ELECTRONIC REMITTANCE ADVICE \[#344.4\]
  - AR EDI LOCKBOX MESSAGES \[#344.5\]
  - RCDPE AUTO-PAY EXCLUSION File \[#344.6\]
  - RCDPE PARAMETER File \[#344.61\]
  - RCDPE CARC-RARC AUTO DEC File \[#344.62\]
  - AR TRANSACTION File \[#433\]
  - EXPLANATION OF BENEFITS \[361.1\]

> While the VistA installation procedure of the KIDS build allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action, due to the complexity of this patch, it is not recommended for back-out, and a restore from a backup of the Transport Global should not be attempted. In the event that a site decides to back out this patch, the site should contact the National Service Desk (NSD) to submit a help desk ticket. The development team will need to issue a follow-on patch in order to comprehensively back-out this patch and/or to clean up corrupted data/remove data dictionary changes, if needed and restore the system to a functioning state.

> Please contact the EPMO team for assistance since this installed patch contains components in addition to routines.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Successful back-out is confirmed by verification that the back-out patch was successfully implemented. This includes successful installation and testing that the back-out it acted as expected, as defined together with the team the site contacted in section 5.5.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Rollback pertains to data. PRCA\*4.5\*345 and IB\*2.0\*639 do impact the data in the Integrated Billing and Accounts Receivable packages. Therefore, to roll back the patches one will need to install new patches to roll back the database changes and restore the system back to its prior

> state. In the case where a rollback is needed, refer to the Back-Out procedures detailed elsewhere within this document.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark51" class="anchor"></span>Not applicable.

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