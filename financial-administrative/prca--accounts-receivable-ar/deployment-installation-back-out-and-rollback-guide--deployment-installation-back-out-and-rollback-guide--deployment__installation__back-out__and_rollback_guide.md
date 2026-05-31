---
title: PRCA*4.5*326 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5*326
group_key: PRCA:PRCA:4.5
file_numbers:
- '344.41'
- '344.6'
security_keys:
- PROVIDER
menu_options: 0
description: '> This document describes how to deploy and install the multi-build (which includes IB\2.0\609 and PRCA\4.5\326) as well as how to back-out the product and rollback to a previous version or data set.'
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 4033
section_count: 31
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: November 2018
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_326_ig.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_326_ig.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=29
audit_applied: '2026-05-31'
master_source: PRCA*4.5*326 Deployment, Installation, Back-Out, and Rollback Guide
master_pub_date: November 2018
consolidated_from: 49 versions
prior_versions:
- PRCA*4.5*318 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*321 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*332, IB*2.0*633 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*338 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*340 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*347 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*349 Deployment, Installation, Back-out, and Rollback Guide
- PRCA*4.5*351 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*355 Deployment, Installation, Back-out, and Rollback Guide
- PRCA*4.5*357 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*361 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*362 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*365 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*367 Deployment, Installation, Back-out, and Rollback Guide
- PRCA*4.5*371 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*373 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*375 Deployment, Installation, Back-out, and Rollback Guide
- PRCA*4.5*377 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*378 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*379 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*380 Deployment, Installation, Back-out, and Rollback Guide
- PRCA*4.5*381 Deployment, Installation, Back-out, and Rollback Guide
- PRCA*4.5*382 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*383 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*384 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*387 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*388 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*390 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*391 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*392 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*393 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*396 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*397 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*400 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*401 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*403 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*404 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*405 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*406 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*409 Deployment, Installation, Back-out, and Rollback Guide
- PRCA*4.5*415 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*416 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*418 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*420 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*421 Deployment, Installation, Back-Out, and Rollback Guide
- PRCA*4.5*439 Deployment, Installation, Back-out, and Rollback Guide
- PRCA*4.5*446 Deployment, Installation, Back-out, and Rollback Guide
- PRCA*4.5*450 Deployment, Installation, Back-out, and Rollback Guide
consolidated_title: deployment, installation, back-out, and rollback guide
---

# Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePayments Build 4 & 5


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) ePayments Build 4 & 5](#medical-care-collection-fund-mccf-electronic-data-interchange-edi-transaction-applications-suite-tas-epayments-build-4-5)
- [Deployment, Installation, Back-Out, and Rollback Guide](#deployment-installation-back-out-and-rollback-guide)
    - [November 2018 Department of Veterans Affairs](#november-2018-department-of-veterans-affairs)
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
> Accounts Receivable PRCA\*4.5\*326 Integrated Billing IB\*2.0\*609 Version 1.1

# Deployment, Installation, Back-Out, and Rollback Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prca-4-5-326-deployment-installation-back-out-and-rollback-guide/001.png)

### November 2018 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date      | Version | Description      | Author |
|---------------|-------------|----------------------|------------|
| March 2018    | 1.0         | Initial Version      | REDACTED   |
| November 2018 | 1.1         | Updated for IOC Exit | REDACTED   |

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.
# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes how to deploy and install the multi-build (which includes IB\*2.0\*609 and PRCA\*4.5\*326) as well as how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the multi-build build PRCA IB EPAYMENTS BUNDLE 3.0 (which includes IB\*2.0\*609 and PRCA\*4.5\*326) will be deployed and installed, as well as how the patches are to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following patches must be installed before IB\*2.0\*609 and PRCA\*4.5\*326:

- IB\*2.0\*530
- PRCA\*4.5\*315
- PRCA\*4.5\*321

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
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>Field Testing (Initial Operating Capability - IOC), Health Product Support Testing &amp; VIP Release Agent Approval</p>
</blockquote></td>
<td>Deployment</td>
<td>Test for operational readiness</td>
<td>Testing</td>
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
<tr class="even">
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
<tr class="odd">
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
<tr class="even">
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
<tr class="odd">
<td>8</td>
<td><blockquote>
<p>VA's eBusiness team</p>
</blockquote></td>
<td><blockquote>
<p>Installations</p>
</blockquote></td>
<td>Coordinate training</td>
<td>Deployment</td>
</tr>
<tr class="even">
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
<tr class="odd">
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

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the deployment of multi-build build PRCA IB EPAYMENTS BUNDLE 3.0 (which includes IB\*2.0\*609 and PRCA\*4.5\*326).

> <sup>1</sup> Project schedule (right click and select open hyperlink to access) REDACTED

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This multi-build build PRCA IB EPAYMENTS BUNDLE 3.0 (which includes IB\*2.0\*609 and PRCA\*4.5\*326) is to be nationally released to all VAMCs.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The test sites for IOC testing are: FRESNO, CA

> WHITE CITY, OR (DOM) LONG BEACH, CA

> LAS VEGAS, NV

- These sites will not be defined here until the sites have signed the Memorandum of Understanding (MOUs) and testing has completed as sometimes a site has to stop testing prior to the end of IOC.

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
<td>PRCA*4.5*315</td>
<td>N/A</td>
<td>Nationally released version</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PRCA*4.5*321</td>
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
<td>IB*2.0*530</td>
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

> The sites that are participating in field testing (IOC) will use the "Patch Tracking" message in Outlook to communicate with the ePayments eBusiness team, the developers, and product support personnel.

#### Deployment/Installation/Back-Out Checklist

> The Release Management team will deploy the multi-build build PRCA IB EPAYMENTS BUNDLE 3.0, which is tracked in the National Patch Module (NPM) in Forum, nationally to all VAMCs. Forum automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in Forum to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run to identify which sites have not installed the patch in their VistA production system as of that moment in time.

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

> IB\*2.0\*609 and PRCA\*4.5\*326, patches to the existing VistA Integrated Billing 2.0 and Accounts Receivable 4.5 packages, are installable on a fully patched M(UMPS) VistA system and operate on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities which communicate with the underlying operating system and hardware, thereby providing Integrated Billing and Accounts Receivable independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to IB\*2.0\*609 and PRCA\*4.5\*326 documentation on the National Patch Module (NPM) on Forum for the detailed installation instructions. These instructions would include any pre- installation steps if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to IB\*2.0\*609 and PRCA\*4.5\*326 documentation on the NPM to find the location of related documentation that can be downloaded. IB\*2.0\*609 and PRCA\*4.5\*326 will be distributed via host file PRCA_IB_EPAYMENTS_BUNDLE_3_0.KID.

> Sites can retrieve VistA software from REDACTED. This transmits the file from the first available server. Sites may also select to retrieve this file directly from a specific server.

> Sites may retrieve software directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

> Hines REDACTED

> Salt Lake City REDACTED

> The PRCA_IB_EPAYMENTS_BUNDLE_3_0.KID host file is located in the anonymous.software directory. Use the American Standard Code for Information Interchange (ASCII) Mode when downloading the file.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Multi-build build PRCA IB EPAYMENTS BUNDLE 3.0 modifies the VistA database. All changes can be found on the NPM documentation for these patches.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No installation scripts are needed for multi-build build PRCA IB EPAYMENTS BUNDLE 3.0 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No Cron scripts are needed for multi-build build PRCA IB EPAYMENTS BUNDLE 3.0 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following staff will need access to the host file PRCA_IB_EPAYMENTS_BUNDLE_3_0.KID containing the IB\*2.0\*609 and PRCA\*4.5\*326 patches. The software is to be installed by the site's or region's designated: VA OI&T IT OPERATIONS SERVICE, Enterprise Service Lines, VistA Applications Division<sup>2</sup>.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to IB\*2.0\*609 and PRCA\*4.5\*326 documentation on the NPM for the detailed installation instructions.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to IB\*2.0\*609 and PRCA\*4.5\*326 documentation on the NPM for the detailed installation instructions. These instructions would include any post installation steps if applicable.

> <sup>2</sup> "Enterprise service lines, VAD" for short. Formerly known as the IRM (Information Resources Management) or IT support.

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

> If a decision to back out is made after national release and within the designated support period, a new patch will be entered into the NPM in Forum and will go through all the necessary milestone reviews, etc. as a patch for a patch. This patch could be defined as an emergency patch, and it could be used to address specific issues pertaining to the original patch or it could be used to restore the build components to their original pre-patch condition.

### After National Release and Warranty Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the support period, the VistA Maintenance Program will produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Changes implemented with multi-build PRCA IB EPAYMENTS BUNDLE 3.0 can be backed out in their entirety or on an enhancement-by-enhancement basis. Either could be accomplished via a new version of multi-build PRCA IB EPAYMENTS BUNDLE 3.0 if before national release or a new multi-build if after national release.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A. The back-out process would be executed at normal, rather than raised job priority, and is expected to have no significant effect on total system performance. Subsequent to the reversion, the performance demands on the system would be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below are the acceptance criteria for each story included in build PRCA IB EPAYMENTS BUNDLE 3.0.

1.  Unique Electronic Transfer Funds (EFT) Identifiers

> Prior to this patch all detail lines belonging to an EFT were

> displayed using the same EFT number. Following this patch, each EFT detail line will be displayed with a unique identifier consisting of

> the EFT number, followed by a period and the sequence number of the EFT detail line. The following reports and worklists will show the unique EFT identifier:

1.  EFT Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\]
2.  EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]
3.  Unapplied EFT Deposits Report \[RCDPE UNAPPLIED EFT DEP REPORT\]
4.  Duplicate EFT Deposits Audit Report \[RCDPE EFT AUDIT REPORT\]
5.  EFT Transaction Audit Report \[RCDPE EFT TRANSACTION AUD REP\]
6.  Manual Match EFT-ERA \[RCDPE MANUAL MATCH EFT-ERA\] when looking up an EFT to manual match
7.  Mark 0-Balance EFT Matched \[RCDPE MARK 0-BAL EFT MATCHED\] when looking up an EFT to match
8.  Remove Duplicate Deposits \[RCDPE REMOVE DUP DEPOSITS\] when displayed for a lookup
9.  ERA Worklist \[RCDPE EDI LOCKBOX WORKLIST\]
10. Auto-Post Awaiting Resolution \[RCDPE APAR\]
11. Receipt Profile \[RCDP RECEIPT PROCESSING\]
12. Unmatch an ERA \[RCDPE UNMATCH ERA\]
2.  Filter by Receipt Number on Link Payment Tracking Report \[RCDPE SUSPENSE AUDIT REPORT\]
    1.  The Link Payment Tracking Report prompts the user for a single receipt number to include on the report.
    2.  If no single receipt number is chosen, the user is prompted for a date range and selected users as per existing report functionality.
    3.  The report will now be available in Excel format and the user will be prompted for this option.
3.  ERA/EFT 'matched' date added to the ERA Worklist \[RCDPE EDI LOCKBOX WORKLIST\]
    1.  The header on the ERA worklist for payer name and match status will now read "PAYER NAME/MATCH STATUS & DATE".
    2.  The ERA Worklist will display the date an EFT or a check was matched to an ERA.
    3.  The Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\] will show the date an EFT or check was matched to an ERA.
4.  EDI Lockbox 3rd Party Exceptions \[RCDPE EXCEPTION PROCESSING\] The Data Exceptions filter was altered so that:
    1.  The filter will now show results when a user elects to include only pharmacy exceptions.
    2.  The pharmacy flag allocated to a payer via the 'Identify payers' option \[RCDPE PAYER IDENTIFY\] will be used to determine which entries are pharmacy exceptions.
5.  Updated Display Language in the Link Payment Tracking Report \[RCDPE SUSPENSE AUDIT REPORT\]
    1.  An additional header line will appear on the Link Payment Tracking Report. It will contain the column headers 'REASON' and 'CLAIMS'.
    2.  The Disposition Reason for receipts will be displayed in the 'REASON' column on a second row below the receipt row.
    3.  Receipts with multiple split transactions will display 'Multi-Trans Split' in the 'REASON' column on a second row below the receipt row.
    4.  Each transaction in a multi-transaction split receipt will be displayed on its own line in the 'CLAIMS' column below the 'Multi-Trans Split' reason.
6)  Changes to the Auto-Posting logic in the Nightly AR Process \[PRCA NIGHTLY PROCESS\]
    1.  Check type ERAs that match to EFTs will auto-post during the nightly process.
    2.  Non-payment type ERAs that match to EFTs will auto-post during the nightly process.
    3.  Balance of Payment (BOP) type ERAs that match to EFTs will auto-post during the nightly process.
5)  The Manual Match EFT-ERA \[RCDPE EFT ERA MANUAL MATCH\] on the Clerk's AR Menu will allow non-payment type ERAs to be marked for auto-post.
6)  The Manual Match Option \[RCDPE MANUAL MATCH EFT-ERA\] in the ERA Worklist will allow balance of payment type ERAs to be marked for auto-post.
7.  Allow for Negative Distributions to 'Claim not Found in AR'
    1.  The ERA Worklist Scratchpad Screen action 'Distribute Adj Amts' \[protocol RCDPE EOB WORKLIST DIST ADJ\] will allow PLB adjustments to be distributed to lines which have no valid claim.
8.  Display the user who marked a claim for auto-posting in the ERA

> Worklist \[RCDPE EDI LOCKBOX WORKLIST\] or in the Auto-Post Awaiting Resolution option \[RCDPE APAR\]. The user who marked the claim for auto-posting will be displayed in the following places:

1.  List of Receipts Report \[RCDP LIST OF RECEIPTS REPORT\]
2.  Receipt Processing \[RCDP RECEIPT PROCESSING\]
3.  Auto-Posted Receipts Report \[RCDPE AUTO-POST RECEIPT REPORT\]
4.  Third Party Joint Inquiry (TPJI) \[IBJ THIRD PARTY JOINT INQUIRY\]

> Within TPJI in the Transaction Profile \[RCDP TRANSACTIONS LIST TRANSACTION PROFILE\] and Profile of Accounts Receivable \[RCDP RECEIPT PROFILE ACCOUNT PROFILE\] actions.

9.  Auto-Post Report \[RCDPE AUTO-POST REPORT\] filter and sort modifications
    1.  When running this report, users will have the option of selecting payers to include either by payer name or by payer Tax Identification Number (TIN).
    2.  Users will have the option to sort the report by payer name or payer TIN.
    3.  The report header will reflect the new filter and sort criteria.
    4.  Display of payers in the report will show NAME/TIN when the report is sorted by payer name and TIN/NAME when the report is sorted by payer TIN.
10. ERA Worklist Manual Match Action \[RCDPE EFT ERA MANUAL MATCH\]
    1.  When running the Manual Match action in the ERA Worklist and selecting an ERA that is ALREADY matched, the error message 'ERA is already matched please select another ERA...' will only appear once.
11. ERA Worklist \[RCDPE EDI LOCKBOX WORKLIST\] filter modification
    1.  The ERA Worklist will show an additional prompt for entries to include in the list, based on the auto-post status of the ERA.
    2.  The auto-post status of a worklist entry will be indicated.
    3.  The system will warn the user if they select an invalid combination of ERA Worklist filters.
12. The EDI LOCKBOX Parameters \[RCDPE EDI LOCKBOX PARAMETERS\] modifications
    1.  The EDI LOCKBOX Parameters option was modified to send notifications when Auto- Post and/or Auto-Decrease are turned on or off.
    2.  Additionally, notifications are also sent when the auto-post or auto-decrease payer exclusion list is modified or list of auto-decrease CARCs is modified in any way.
    3.  The existing prompt 'ENABLE AUTO-DECREASE OF MEDICAL CLAIMS' was modified to 'ENABLE AUTO-DECREASE OF MEDICAL CLAIMS WITH PAYMENTS'.
    4.  A new prompt was 'ENABLE AUTO-DECREASE OF MEDICAL CLAIMS NO PAYMENTS' to allow the site to turn auto-decrease on/off for claims with zero dollar claim lines that are reversals.
    5.  A new prompt 'AUTO-DECREASE NO-PAY MEDICAL CLAIMS FOR THE FOLLOWING CARC/AMOUNTS ONLY:' was added to allow the site to specify a list of CARCs (and their maximum amounts) to be used when auto-decreasing claims with zero dollar claim lines that are reversals.
    6.  A new prompt 'NUMBER OF DAYS TO WAIT BEFORE NO-PAY AUTO-DECREASE' was added to allow the site to specify when to begin auto-decreasing claim with zero dollar claim lines that are reversals.
    7.  A new prompt 'MAXIMUM DOLLAR AMOUNT TO AUTO-DECREASE PER CLAIM' was added to allow the site to set a maximum per claim auto-decrease amount which is not to exceed 99,999 dollars. If the user enters a maximum dollar amount that is less than

> ANY of the site defined CARCs for claims with payments OR claims with no payments, a warning message is displayed and the maximum amount for these CARCs will automatically be reduced to the per claim limit.

13. The Exclusion Name/TIN Report \[RCDPE PAYER EXCLUSION NAME TIN\] was renamed to be the Payer Implementation Report.
14. Third Party Joint Inquiry (TPJI) \[IBJ THIRD PARTY JOINT INQUIRY\] modifications
    1.  The ERA/835 \[IBJT ERA 835 INFORMATION\] action was modified to display the claims collected percentage in the CLAIM LEVEL PAY STATUS section.
    2.  The CR/TR numbers and FMS document numbers will be displayed on the Transaction Profile \[RCDP TRANSACTIONS LIST TRANSACTION PROFILE\] action from the Account Profile \[RCDP RECEIPT PROFILE ACCOUNT PROFILE MENU\] action.
15. Unmatch an ERA \[RCDPE UNMATCH ERA\] modification
    1.  When using the Unmatch An ERA option \[RCDPE UNMATCH ERA\], the user was asked whether they wanted to delete the worklist entry, when it is the scratch pad entry that is being deleted.

> c\) The prompt will now read: "THIS ERA ALREADY HAS A SCRATCH PAD ENTRY AND MUST BE DELETED BEFORE IT CAN BE UNMATCHED. DO YOU WANT TO DELETE THE SCRATCH PAD ENTRY FOR THIS ERA NOW?"

16. Changes to the Auto-Decrease logic in the Nightly AR Process \[PRCA NIGHTLY PROCESS\]
    1.  If the new site parameter 'ENABLE AUTO-DECREASE OF MEDICAL CLAIMS NO PAYMENTS' is set to 'YES', claims with zero dollar claim lines that are that match site parameter settings are auto-decreased.
    2.  The maximum auto-decrease amount for a claim now cannot exceed the maximum amount per claim entered in the new site parameter prompt.
17. ERA WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] Verify action modification
    1.  The Verify action \[RCDPE EOB WORKLIST VERIFY\] on the ERA Worklist Scratchpad was modified to allow the printing of a new report of verify discrepancies for ERAs that were auto-posted.
18. Modifications to Unmatched ERAs\>30 days, Paper Matched/Not Posted ERA\> 30 days, and the EFT Matched/Not Posted ERA\>30 days bulletins
    1.  The above bulletins generated by the Nightly AR Process \[PRCA NIGHTLY PROCESS\] were modified to include trace numbers.
19. ERA WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] Administrative Cost Adjustment action modification
    1.  The Admin Cost Adj \[RCDPE EOB WORKLIST ADMIN COST ADJ\] action on the Research action for the ERA Worklist was modified to adjust the balance AND be recognized on payments in the Auto-Post Awaiting Resolution (APAR) Worklist,

> the same way it currently works on payments that are not on the APAR worklist.

20. Standardization of EDI Lockbox Report and Worklist filters
    1.  A new 'Medical, Pharmacy, Tricare or All' (M/P/T) filter was added to EDI Lockbox reports.
    2.  The new filter above uses the Medical, Pharmacy, Tricare settings from the Identify Payers \[RCDPE PAYER IDENTIFY\] option to do the appropriate filtering.
    3.  If a report or worklist already had a filter that was similar to the new M/P/T filter it was replaced by the new M/T/P filter. In addition, if the report had a Payer Name/TIN filter, the M/P/T filter will be asked prior to the Payer Name/TIN filter and the Payer Name/TIN filter will not display any Payer Names/TINs that don't match the M/P/T filter selection.
    4.  Any 'CHAMPVA' existing on reports were removed.
    5.  The following reports and worklists were modified
        1.  Active Bills With EEOB \[RCDPE ACTIVE WITH EEOB REPORT\]
        2.  Auto-Post Awaiting Resolution \[RCDPE APAR\]
        3.  Auto-Decrease Adjustment report \[RCDPE AUTO-DECREASE REPORT\]
        4.  Auto-Posted Receipt Report \[RCDPE AUTO-POST RECEIPT REPORT\]
        5.  Auto-Post Report \[RCDPE AUTO-POST REPORT\]
        6.  835 CARC Data Report \[RCDPE CARC CODE PAYER REPORT\]
        7.  EFT Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\]
        8.  EEOB Move/Copy/Remove Audit Report \[RCDPE EEOB MOVE/COPY/RMOVE RPT\]
        9.  EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]
        10. Duplicate EFT Deposits Audit Report \[RCDPE EFT AUDIT REPORT\]
        11. EFT/ERA TRENDING Report \[RCDPE EFT-ERA TRENDING REPORT\]
        12. ERA Unmatched Aging Report \[RCDPE ERA AGING REPORT\]
        13. ERA Status Change Audit Report \[RCDPE ERA STATUS CHNG AUD REP\]
        14. ERAs Posted with Paper EOB Audit Report \[RCDPE ERA W/PAPER EOB REPORT\]
        15. EDI Lockbox 3rd Party Exceptions \[RCDPE EXCEPTION PROCESSING\]
        16. Payer Implementation Report \[RCDPE PAYER EXCLUSION NAME TIN\]
        17. Provider Level Adjustments (PLB) Report \[RCDPE PROVIDER LVL ADJ REPORT\]
        18. Remove ERA from Active Worklist Audit Report \[RCDPE PROVIDER LVL ADJ REPORT\]
        19. Unapplied EFT Deposits Report \[RCDPE UNAPPLIED EFT DEP REPORT\]
    6.  When prompting for the M/P/T filter in any of the above reports,

> or in the ERA Worklist, a warning message will be given if the user selects pharmacy or Tricare and there are no payers flagged

> as that type in the identify payers option.

7.  The AR Nightly process was changed to detect if new Payer Name/TINs are detecting in incoming EFTs. If found, these Payers will be added to the exclusion file (#344.6) and can then be

> flagged in the Identify Payers \[RCDPE PAYER IDENTIFY\] OPTION.

21. ERA WORKLIST \[RCDPE EDI LOCKBOX WORKLIST\] modification
    1.  Security key RCDPEAR was added to the Admin Cost Adj \[RCDPE EOB WORKLIST

> ADMIN COST ADJ\] action and the action was moved from the Research \[RCDPE EOB WORKLIST RESEARCH MENU\] protocol menu to the first page of protocol actions on ERA Worklist.

22. Duplicate EFT Deposits Audit Report \[RCDPE EFT AUDIT REPORT\] modification.
    1.  The date range filter was modified such that all the duplicate EFT Deposits for the selected range are displayed (inclusively). Prior to this modification, any duplicate EFT Deposits found on the last day of the date range were not displayed.
23. Auto-Audit processing in the Nightly AR Process \[\[PRCA NIGHTLY PROCESS\]\] modification
    1.  ERAs with a rate type of 'FEE REIMB INS' are now included in the Auto-Auditing process.
24. Decrease Adjustment \[PRCAC TR DECREASE\] modification
    1.  A warning will now display if the user attempts to enter a decrease adjustment for an ERA that has pending payments.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The project is canceled or the requested changes implemented by multi-build build PRCA IB EPAYMENTS BUNDLE 3.0 are no longer desired by VA OI&T and the ePayments eBusiness team, or the patch produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since the ePayments software is tightly integrated with external systems, any attempt at a back- out should include close consultation with the external trading partners such as the Financial Services Center (FSC), the Health Care Clearing House (HCCH), the VA 3rd Party Lockbox bank, and the Financial Management System (FMS) to determine risk.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Any back-out decision should be a joint decision of the Business Owner (or their representative) and the Program Manager with input from the Health Product Support (HPS) Application Coordinator, developers (both project and Tier 3 HPS), and if appropriate, external trading partners such as the VA Financial Service Center (FSC), the Health Care Clearing House (HCCH), VA 3<sup>rd</sup> Party Lockbox bank, and the FMS to determine the appropriate course of action. ePayments is tightly integrated with these external partners and a back-out of the patch should not be a standalone decision.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The back-out plan for VistA applications is complex and not a "one size fits all" solution. The general strategy for a VistA rollback is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch. If not,

> the site should contact the Enterprise Program Management Office (EPMO) team directly for specific solutions to their unique problems.

> Back-Out Procedure prior to National Release. If it is prior to national release, the site will be already working directly with the development team daily and should contact that team. The development team members will have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that development team can quickly address via a new software version. If the site is unsure who to contact they may log a ticket of contact Health Product Support - Management Systems Team

> The Multi-build build PRCA IB EPAYMENTS BUNDLE 3.0 contains the following build components.

- Data Dictionary Changes
- Options
- Routines
- Templates
- Protocols
- Modifications to the following files:
  - AR BATCH PAYMENT File \[#344\]
  - EDI THIRD PARTY EFT DETAIL \[#344.31\]
  - ELECTRONIC REMITTANCE ADVICE \[#344.4 and sub-file 344.41\]
  - RCDPE PARAMETER File \[#344.61\]
  - RCDPE CARC-RARC AUTO DEC File \[#344.62\]
  - RCDPE SUSPENSE AUDIT Sub-file \[344.711\]

> While the VistA installation procedure of the KIDS build allows the installer to back up the modified routines using the 'Backup a Transport Global' action, due to the complexity of this

> patch, it is not recommended for back-out, and a restore from a backup of the Transport Global should not be attempted. In the event that a site decides to back out this patch, the site should contact the Enterprise Service Desk (ESD) to submit a help desk ticket. The development team will need to issue a follow-on patch in order to comprehensively back-out this patch and/or to clean up corrupted data/remove data dictionary changes, if needed and restore the system to a functioning state.

> Please contact the EPMO development team for assistance since this installed patch contains components in addition to routines.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Successful back-out is confirmed by verification that the back-out patch was successfully implemented. This includes successful installation and testing that the back-out acted as expected, as defined together with the team the site contacted in section 5.5.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Rollback pertains to data. IB\*2.0\*609 and Patch PRCA\*4.5\*326 do impact the data in the Integrated Billing and Accounts Receivable packages. Therefore, to roll back the patches one

> will need to install new patches to roll back the database changes and restore the system back to its prior state. In the case where a rollback is needed, refer to the Back-Out procedures detailed elsewhere within this document.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark52" class="anchor"></span>Not applicable.

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
| December 2015 | 2.0         | The OI&T Documentation Standards Committee merged the existing *"Installation, Back-Out, Rollback Plan"* template with the content requirements in the OI&T End-user Documentation Standards for a more comprehensive Installation Plan. | OI&T Documentation Standards Committee |
| February 2015 | 1.0         | Initial Draft                                                                                                                                                                                                                            | Lifecycle and Release Management       |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PRCA*4.5*321 Deployment, Installation, Back-Out, and Rollback Guide

### June 2018 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date       | Version | Description                                                                                                                               | Author |
|----------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------|
| July 2017      | 1.0         | Initial Version                                                                                                                               | REDACTED   |
| September 2017 | 2.0         | Incorporated the additional items to this document as the scope of work (VistA enhancements) increased when we combined Build 2 with Build 3. | REDACTED   |
| March 2018     | 3.0         | Updated section 5.5.2 (User Acceptance Testing) from modified patch description. Changed release month.                                       | REDACTED   |
| June 2018      | 4.0         | Updated section 5.5.2 (User Acceptance Testing) from modified patch description. Changed release month.                                       | REDACTED   |

### From: PRCA*4.5*361 Deployment, Installation, Back-Out, and Rollback Guide

### September 2020 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OIT)

> Revision History

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 45%" />
<col style="width: 23%" />
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
<td>09/30/2020</td>
<td>1.0</td>
<td>Initial release</td>
<td><p>CC IBAR</p>
<p>Development Team</p></td>
</tr>
</tbody>
</table>

### From: PRCA*4.5*318 Deployment, Installation, Back-Out, and Rollback Guide

### October 2017 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>May 2017</p>
</blockquote></td>
<td>1.0</td>
<td><blockquote>
<p>Initial Version</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>May 22, 2017</p>
</blockquote></td>
<td>2.0</td>
<td><blockquote>
<p>Incorporated Feedback from eBusiness. Section 5.2.2 updated US30 acceptance criteria.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>September 2017</p>
</blockquote></td>
<td>3.0</td>
<td><blockquote>
<p>Updating document for IOC exit which will occur in October 2017.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

### From: PRCA*4.5*332, IB*2.0*633 Deployment, Installation, Back-Out, and Rollback Guide

### June 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date      | Version | Description                        | Author |
|---------------|-------------|----------------------------------------|------------|
| December 2018 | 1.0         | Initial Version                        | REDACTED   |
| March 2019    | 1.1         | Updated after Technical Review         | REDACTED   |
| June 2019     | 1.2         | Updated footers with new release month | REDACTED   |

### From: PRCA*4.5*379 Deployment, Installation, Back-Out, and Rollback Guide

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install the Veterans Information Systems and Technology Architecture (VistA) Accounts Receivable patch PRCA\*4.5\*379, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

The SHRPE product makes enhancements to the Accounts Receivable application to implement a new billing Consolidated Patient Account Center (CPAC) High Risk Veteran Reconciliation Report \[PRCA HRFS RECONCILIATION RPT\] report that allows Veterans' Health Administration (VHA) CPAC users to view first party charges for patients with the High Risk for Suicide (HRFS) flag in order to improve efficiency and accountability in revenue operations.

The PRCA\*4.5\*379 patch adds new routines RCHRFS, RCHRFS1, RCHRFS2, and RCHRFSUT that implement CPAC High Risk Veteran Reconciliation Report \[PRCA HRFS RECONCILIATION RPT\].

Additionally, this patch makes changes to the First Party Veteran Charge Report (VCR). When using the option PRCA FP VETERAN CHRG RPT to display the VCR, after selecting the other filter prompts, the prompt that asked to display LETTERS has been changed. The patch modifies two routines RCVCR1 and RCVCR2 to implement these changes.

### After National Release but During Designated Support Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to back out a specific release needs to be made in a timely manner. Catastrophic failures are usually known early in the testing process—within the first two or three days. Sites are encouraged to perform all test scripts to ensure new code is functioning in their environment, with their data. A back-out should only be considered for critical issues or errors. The normal or an expedited, issue-focused patch process can correct other bugs.

The general strategy for SHRPE VistA functionality rollback will likely be to repair the code with another follow-on patch.

If any issues with SHRPE VistA software are discovered after it is nationally released and within the 90-day warranty period window, the SHRPE development team will research the issue and provide guidance for any immediate, possible workaround. After discussing the defect with VA and receiving their approval for the proposed resolution, the SHRPE development team will communicate guidance for the long-term solution.

The long-term solution will likely be the installation of a follow-up patch to correct the defect, a follow-up patch to remove the SHRPE updates, or a detailed set of instructions on how the software can be safely backed out of the production system.

### From: PRCA*4.5*340 Deployment, Installation, Back-Out, and Rollback Guide

## Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

### From: PRCA*4.5*446 Deployment, Installation, Back-out, and Rollback Guide

## Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install and how to back-out the product and rollback to a previous version or data set.

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the patch will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

### Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PRCA\*4.5\*439

### Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched Veterans Health Information Systems and Technology Architecture (VistA) system.

## Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                                                                                                                  | Phase / Role    | Tasks                                                                                                               | Project Phase (See Schedule)                 |
|-----|---------------------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| 1   | VA OIT, VHA Finance Financial Management VistA Support, and PMO                                                                       | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                 | Planning                                     |
| 2   | Local VAMC and CPAC processes                                                                                                         | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                          | Planning                                     |
| 3   | Field Testing (Initial Operating Capability - IOC), VHA Finance Financial Management VistA Support Testing, and VistA Office Approval | Deployment      | Test for operational readiness                                                                                      | Testing                                      |
| 4   | VHA Finance Financial Management VistA Support and Field Operations                                                                   | Deployment      | Execute deployment                                                                                                  | Deployment                                   |
| 5   | Individual Veterans Administration Medical Centers (VAMCs)                                                                            | Installation    | Plan and schedule installation                                                                                      | Deployment                                   |
| 6   | VistA Office                                                                                                                          | Installation    | Ensure proper change management approval obtained in support of national release                                    | Deployment                                   |
| 7   | N/A                                                                                                                                   | Installation    | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         | N/A; only existing VistA system will be used |
| 8   | VA's eBusiness team                                                                                                                   | Installations   | Coordinate training                                                                                                 | Deployment                                   |
| 9   | VHA Finance Financial Management VistA Support Verifier and Development team                                                          | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                                   |
| 10  | VA OIT, VHA Finance Financial Management VistA Support, and Development Team                                                          | Post Deployment | Hardware, Software and System Support                                                                               | Warranty                                     |

<span id="_Toc205792424" class="anchor"></span>Table 2: Site Preparation

## Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national rollout.

This section provides the schedule and milestones for the deployment.

### Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for days starting with the day after national release.

### Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the deployment of patch .

#### Deployment Topology (Targeted Architecture)

This section discusses the locations that will receive deployment of patch .

#### Site Information (Locations, Deployment Recipients) 

The IOC sites are:

- VA Western New York Healthcare System (528 – Buffalo, NY)
- VA NY Harbor Healthcare System (630– New York, NY)
- Beckley VA Medical Center (571– Beckley, WV)
- VA Sierra Nevada Healthcare System (654– Reno, NV)

#### Site Preparation 

The following table describes preparation required by the site prior to deployment.

| Site / Other | Problem / Change Needed | Features to Adapt / Modify to New Product | Actions / Steps | Owner |
|--------------|-------------------------|-------------------------------------------|-----------------|-------|
| N/A          | N/A                     | N/A                                       | N/A             | N/A   |

<span id="_Toc205792425" class="anchor"></span>Table 3: Facility-Specific Features

### Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Facility Specifics

The following table lists facility-specific features required for deployment.

| Site | Space / Room | Features Needed | Other |
|------|--------------|-----------------|-------|
| N/A  | N/A          | N/A             | N/A   |

<span id="_Toc205792426" class="anchor"></span>Table 4: Hardware Specifications

#### Hardware 

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware     | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-------|---------|---------------|--------------|-------|
| Existing VistA system | N/A   | N/A     | N/A           | N/A          | N/A   |

<span id="_Toc205792427" class="anchor"></span>Table 5: Software Specifications

Please see the Roles and Responsibilities Table 1 in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

#### Software 

The following table describes software specifications required at each site prior to deployment.

| Required Software                                      | Make | Version | Configuration | Manufacturer | Other |
|--------------------------------------------------------|------|---------|---------------|--------------|-------|
| Fully patched Accounts Receivable package within VistA | N/A  | 4.5     | N/A           | N/A          | N/A   |

Please see the Roles and Responsibilities Table 1 in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

#### Communications 

The sites that are participating in field testing (IOC) will use the "Patch Tracking" message in Outlook to communicate with the eBusiness team, developers, and product support personnel.

#### Deployment / Installation / Back-out Checklist

The Release Management team will deploy the patch, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in Forum. Forum automatically tracks the patches as they are installed in the different VAMC Production systems. One can run a report in Forum to identify when and by whom the patch was installed into the VistA Production at each site. A report can also be run to identify which sites have not currently installed the patch into their VistA Production system. Therefore, this information does not need to be manually tracked in the chart below.

Table 6: Deployment / Installation / Back-out Checklist

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | N/A | N/A  | N/A                           |
| Install  | N/A | N/A  | N/A                           |
| Back-out | N/A | N/A  | N/A                           |

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch is installable on a fully patched M(UMPS) VistA system and operates on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities that communicate with the underlying operating system and hardware, thereby providing each VistA package independence from variations in hardware and operating system.

### Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the documentation on the NPM in Forum for the detailed installation instructions. These instructions include any pre-installation steps if applicable.

### Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the documentation on the NPM to find related documentation that can be downloaded. The patch description will be transmitted as a MailMan message from the NPM. These messages can also be pulled from the NPM.

### Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch modifies the VistA database. All changes can be found on the NPM documentation for this patch.

### Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are needed for installation of .

### Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for installation of .

### Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff performing the installation of this multi-build will need access to FORUM's NPM to view all patch descriptions. Staff will also need access and ability to download the host file from the VistA software download site. The software is to be installed by each site's or region's designated VA OIT IT Operations Service, Enterprise Service Lines, VistA Applications Division[^1].

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detailed instructions for installing patch can be found on the NPM.

### Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the documentation on the NPM for detailed installation instructions. These instructions include any post installation steps if applicable.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required for this patch.

### Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocations, or other resources is necessary.

### From: PRCA*4.5*338 Deployment, Installation, Back-Out, and Rollback Guide

### August 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date   | Version | Description           | Author |
|------------|-------------|---------------------------|------------|
| 08/01/2019 | 1.0         | Initial Document Creation | AbleVets   |

### From: PRCA*4.5*365 Deployment, Installation, Back-Out, and Rollback Guide

### May 2020

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs

### Office of Information and Technology (OI&T)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Revision History

| Date   | Version | Description  | Author |
|------------|-------------|------------------|------------|
| 05/18/2020 | 1.0         | Initial Delivery | AbleVets   |

### From: PRCA*4.5*357 Deployment, Installation, Back-Out, and Rollback Guide

### September 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OIT)

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date   | Version | Description | Author |
|------------|-------------|-----------------|------------|
| 09/13/2019 | 1.0         | Initial draft   | AbleVets   |

> Artifact Rationale

> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

1.  [Introduction 1](#introduction)
    1.  [Purpose 1](#purpose)
    2.  [Dependencies 1](#dependencies)
    3.  [Constraints 1](#constraints)
2.  [Roles and Responsibilities 1](#roles-and-responsibilities)
3.  [Deployment 2](#deployment)
    1.  [Timeline 2](#timeline)
    2.  [Site Readiness Assessment 2](#site-readiness-assessment)
        1.  [Deployment Topology (Targeted Architecture) 2](#deployment-topology-targeted-architecture)
        2.  [Site Information (Locations, Deployment Recipients) 2](#site-information-locations-deployment-recipients)
        3.  [Site Preparation 2](#site-preparation)
    3.  [Resources 2](#resources)
        1.  [Hardware 3](#hardware)
        2.  [Software 3](#software)
        3.  [Communications 3](#communications)
            1.  [Deployment/Installation/Back-Out Checklist 3](#deploymentinstallationback-out-checklist)
4.  [Installation 3](#installation)
    1.  [Pre-installation and System Requirements 3](#pre-installation-and-system-requirements)
    2.  [Platform Installation and Preparation 3](#platform-installation-and-preparation)
    3.  [Download and Extract Files 4](#download-and-extract-files)
    4.  [Database Creation 4](#database-creation)
    5.  [Installation Scripts 4](#installation-scripts)
    6.  [Cron Scripts 4](#cron-scripts)
    7.  [Access Requirements and Skills Needed for the Installation 4](#access-requirements-and-skills-needed-for-the-installation)
    8.  [Installation Procedure 4](#installation-procedure)
    9.  [Installation Verification Procedure 5](#installation-verification-procedure)
    10. [System Configuration 5](#system-configuration)
    11. [Database Tuning 5](#database-tuning)
5.  [Back-Out Procedure 5](#back-out-procedure)
    1.  [Back-Out Strategy 5](#back-out-strategy)
    2.  [Back-Out Considerations 6](#back-out-considerations)
        1.  [Load Testing 6](#load-testing)
        2.  [User Acceptance Testing 6](#user-acceptance-testing)
    3.  [Back-Out Criteria 6](#back-out-criteria)
    4.  [Back-Out Risks 6](#back-out-risks)
    5.  [Authority for Back-Out 6](#authority-for-back-out)
    6.  [Back-Out Procedure 7](#back-out-procedure-1)
    7.  [Back-out Verification Procedure 7](#back-out-verification-procedure)
6.  [Rollback Procedure 7](#rollback-procedure)
    1.  [Rollback Considerations 8](#rollback-considerations)
    2.  [Rollback Criteria 8](#rollback-criteria)
    3.  [Rollback Risks 8](#rollback-risks)
    4.  [Authority for Rollback 8](#authority-for-rollback)
    5.  [Rollback Procedure 8](#rollback-procedure-1)
    6.  [Rollback Verification Procedure 8](#rollback-verification-procedure)
