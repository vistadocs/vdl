---
consolidated_title: "deployment, installation, back-out/rollback guide"
app_code: IB
doc_type: DIBR
master_source: "IB*2*608 Deployment, Installation, Back-out/Rollback Guide"
master_pub_date: April 2019
consolidated_from: 12 versions
prior_versions:
  - "IB*2*618 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*623 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*645 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*646 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*651 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*660 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*663 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*671 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*678 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*682 Deployment, Installation, Back-out/Rollback Guide"
  - "IB*2*698 Deployment, Installation, Back-out/Rollback Guide"
---

# Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) eBilling Build 5/6


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Medical Care Collection Fund (MCCF) Electronic Data Interchange (EDI) Transaction Applications Suite (TAS) eBilling Build 5/6](#medical-care-collection-fund-mccf-electronic-data-interchange-edi-transaction-applications-suite-tas-ebilling-build-56)
- [Deployment, Installation, Back-Out, and Rollback Guide](#deployment-installation-back-out-and-rollback-guide)
    - [April 2019 Department of Veterans Affairs](#april-2019-department-of-veterans-affairs)
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
> Integrated Billing IB\*2.0\*608 Version 2.0

# Deployment, Installation, Back-Out, and Rollback Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ib-2-608-deployment-installation-back-out-rollback-guide/001.png)

### April 2019 Department of Veterans Affairs

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
<td><blockquote>
<p>April 2019</p>
</blockquote></td>
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
<tr class="even">
<td><blockquote>
<p>April 2019</p>
</blockquote></td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td><blockquote>
<p>IOC completed updates</p>
</blockquote></td>
<td><blockquote>
<p>MCCF EDI TAS</p>
<p>eBilling Development Team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
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
2.  [Roles and Responsibilities 1](#roles-and-responsibilities)
3.  [Deployment 2](#deployment)
    1.  [Timeline 2](#timeline)
    2.  [Site Readiness Assessment 2](#site-readiness-assessment)
        1.  [Deployment Topology (Targeted Architecture) 2](#deployment-topology-targeted-architecture)
        2.  [Site Information (Locations, Deployment Recipients) 2](#site-information-locations-deployment-recipients)
        3.  [Site Preparation 3](#site-preparation)
    3.  [Resources 4](#resources)
        1.  [Facility Specifics 4](#facility-specifics)
        2.  [Hardware 4](#hardware)
        3.  [Software 4](#software)
        4.  [Communications 5](#communications)
            1.  [Deployment/Installation/Back-Out Checklist 5](#deploymentinstallationback-out-checklist)
4.  [Installation 5](#installation)
    1.  [Pre-installation and System Requirements 5](#pre-installation-and-system-requirements)
    2.  [Platform Installation and Preparation 5](#platform-installation-and-preparation)
    3.  [Download and Extract Files 5](#download-and-extract-files)
    4.  [Database Creation 5](#database-creation)
    5.  [Installation Scripts 6](#installation-scripts)
    6.  [Cron Scripts 6](#cron-scripts)
    7.  [Access Requirements and Skills Needed for the Installation 6](#access-requirements-and-skills-needed-for-the-installation)
    8.  [Installation Procedure 6](#installation-procedure)
    9.  [Installation Verification Procedure 6](#installation-verification-procedure)
    10. [System Configuration 6](#system-configuration)
    11. [Database Tuning 6](#database-tuning)
5.  [Back-Out Procedure 6](#back-out-procedure)
    1.  [Back-Out Strategy 7](#back-out-strategy)
        1.  [Mirror Testing or Site Production Testing 7](#mirror-testing-or-site-production-testing)
        2.  [After National Release but During the Designated Support Period 7](#after-national-release-but-during-the-designated-support-period)
        3.  [After National Release and Warranty Period 7](#after-national-release-and-warranty-period)
    2.  [Back-Out Considerations 7](#back-out-considerations)
        1.  [Load Testing 7](#load-testing)
        2.  [User Acceptance Testing 7](#user-acceptance-testing)
    3.  [Back-Out Criteria 10](#back-out-criteria)
    4.  [Back-Out Risks 10](#back-out-risks)
    5.  [Authority for Back-Out 10](#authority-for-back-out)
    6.  [Back-Out Procedure 10](#back-out-procedure-1)
    7.  [Back-out Verification Procedure 11](#back-out-verification-procedure)
6.  [Rollback Procedure 11](#rollback-procedure)
    1.  [Rollback Considerations 11](#rollback-considerations)
    2.  [Rollback Criteria 11](#rollback-criteria)
    3.  [Rollback Risks 11](#rollback-risks)
    4.  [Authority for Rollback 11](#authority-for-rollback)
    5.  [Rollback Procedure 11](#rollback-procedure-1)
    6.  [Rollback Verification Procedure 11](#rollback-verification-procedure)

# Table of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities 1

> Table 2: TEST Site Preparation 3

> Table 3: Site Preparation 3

> Table 4: Facility-Specific Features 4

> Table 5: Hardware Specifications 4

> Table 6: Software Specifications 4

> Table 7: Deployment/Installation/Back-Out Checklist 5

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes how to deploy and install the patch IB\*2.0\*608 and how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the IB\*2.0\*608 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IB\*2.0\*592 and IB\*2.0\*621 must be installed before IB\*2.0\*608.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch is intended for a fully patched VistA system.

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
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>VA OI&amp;T, VA OI&amp;T</p>
<p>Health Product Support &amp; PMO (Leidos)</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Plan and schedule deployment (including orchestration with vendors)</p>
</blockquote></td>
<td><blockquote>
<p>Planning</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Local VAMC and CPAC processes</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Determine and document the roles and responsibilities of those involved in the deployment.</p>
</blockquote></td>
<td><blockquote>
<p>Planning</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Field Testing (Initial Operating Capability - IOC), Health Product Support Testing &amp; VIP Release Agent Approval</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Test for operational readiness</p>
</blockquote></td>
<td><blockquote>
<p>Testing</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
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
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
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
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>6</p>
</blockquote></td>
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
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>N/A for this patch as we are using only the existing VistA system</p>
</blockquote></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td><blockquote>
<p>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
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
<td><blockquote>
<p>9</p>
</blockquote></td>
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
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>No changes to current process – we are using the existing VistA system</p>
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

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the IB\*2.0\*608 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch IB\*2.0\*608 is to be nationally released to all VAMCs.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The test sites for IOC testing are:

- REDACTED

> <sup>1</sup> Project schedule (right click and select open hyperlink to access) REDACTED

> Upon national release all VAMCs are expected to install this patch prior to or on the compliance date.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes preparation required by the “TEST” site prior to deployment.

> Table 2: TEST Site Preparation

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 20%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Site/Other</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>Testers need to</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>Grant the</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>obtain access to</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>assigned testers</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>the Test</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>the necessary</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Environment(s)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>access to the</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Test</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Environment(s)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>Testers need to</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>Grant the</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>obtain access to</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>assigned testers</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>the Test</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>the necessary</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Environments</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>access to the</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Test</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Environment(s)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>Testers need to</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>Grant the</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>obtain access to</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>assigned testers</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>the Test</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>the necessary</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Environments</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>access to the</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Test</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Environment(s)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>Testers need to</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>Grant the</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>obtain access to</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>assigned testers</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>the Test</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>the necessary</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Environments</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>access to the</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Test</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Environment(s)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> The following table describes preparation required by the site prior to deployment.

> Table 3: Site Preparation

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
<th><blockquote>
<p><strong>Site/Other</strong></p>
</blockquote></th>
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

> Table 4: Facility-Specific Features

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Site</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Space/Room</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Features Needed</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Other</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
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

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes hardware specifications required at each site prior to deployment.

> Table 5: Hardware Specifications

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
<th><blockquote>
<p><strong>Required Hardware</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Model</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>Existing VistA system</p>
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

> Table 6: Software Specifications

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Required Software</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Make</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>Fully patched Integrated Billing package within VistA</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>2.0</p>
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
<tr class="even">
<td><blockquote>
<p>IB*2.0*592</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>Nationally released version</p>
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
<tr class="odd">
<td><blockquote>
<p>IB*2.0*621</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>Nationally released version</p>
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

> Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The sites that are participating in field testing (IOC) will use the “Patch Tracking” message in Outlook to communicate with the eBilling eBusiness team, the developers, and product support personnel.

#### Deployment/Installation/Back-Out Checklist

> The Release Management team will deploy the patch IB\*2.0\*608, which is tracked nationally for all VAMCs in the NPM in Forum. Forum automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in Forum to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not currently installed the patch in their VistA production system.

> Therefore, this information does not need to be manually tracked in the chart below.

> Table 7: Deployment/Installation/Back-Out Checklist

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Activity</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Day</strong></p>
</blockquote></th>
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
<td><blockquote>
<p>Deploy</p>
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
<tr class="even">
<td><blockquote>
<p>Install</p>
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

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IB\*2.0\*608, a patch to the existing VistA Integrated Billing 2.0 package, is installable on a fully patched M(UMPS) VistA system and operates on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities which communicate with the underlying operating system and hardware, thereby providing Integrated Billing independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the IB\*2.0\*608 documentation on the National Patch Module (NPM) in Forum for the detailed installation instructions. These instructions would include any pre-installation steps if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the IB\*2.0\*608 documentation on the NPM to find related documentation that can be downloaded. IB\*2.0\*608 will be transmitted via a PackMan message and can be pulled from the NPM. It is not a host file, and therefore does not need to be downloaded separately.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IB\*2.0\*608 modifies the VistA database. All changes can be found on the NPM documentation for this patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No installation scripts are needed for IB\*2.0\*608 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No Cron scripts are needed for IB\*2.0\*608 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following staff will need access to the PackMan message containing the IB\*2.0\*608 patch or to Forum’s NPM for downloading the nationally released IB\*2.0\*608 patch. The software is to be installed by the site’s or region’s designated: VA OI&T IT OPERATIONS SERVICE, Enterprise Service Lines, Vista Applications Division<sup>2</sup>.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the IB\*2.0\*608 documentation on the NPM for detailed installation instructions.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the IB\*2.0\*608 documentation on the NPM for specific and detailed installation instructions. These instructions include any post installation steps if applicable. The post installation routine will accomplish the following:

- The Post-install (IBY608PO) will automatically generate the one-time Insurance Company EDI Parameter Report and send an email to the eBiz Rapid Response Group, (“REDACTED”). This report will list all of the insurance companies that have the current setting for the Transmit Electronically parameter set to ZERO which equals 'NO'.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No system configuration changes are required for this patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No reconfiguration of the VistA database, memory allocations or other resources is necessary.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

> <sup>2</sup> “Enterprise service lines, VAD” for short. Formerly known as the IRM (Information Resources Management) or IT support.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Although it is unlikely due to care in collecting, elaborating, and designing approved user stories, followed by multiple testing stages (Developer Unit Testing, Component Integration Testing, SQA Testing, and User Acceptance Testing), a back-out decision due to major issues with this patch could occur. A decision to back out could be made during site Mirror Testing, Site Production Testing or after National Release to the field (VAMCs). The best strategy decision is dependent on the stage of testing during which the decision is made.

### Mirror Testing or Site Production Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If during Mirror testing or Site Production Testing, a new version of a defect correcting test patch is produced, retested and successfully passes development team testing, it will be resubmitted to the site for testing. If the patch produces catastrophic problems, a new version of the patch can be used to restore the build components to their pre-patch condition.

### After National Release but During the Designated Support Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the defect(s) were not discovered until after national release but during the designated support period, a new patch will be entered into the National Patch Module in Forum and will go through all the necessary milestone reviews etc., as a patch for a patch. It is up to VA OI&T and product support whether this new patch would be defined as an emergency patch or not. This new patch could be used to address specific issues pertaining to the original patch or be used to restore the build components to their original pre- patch condition.

### After National Release and Warranty Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the support period, the VistA Maintenance Program would produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is necessary to determine if a wholesale back-out of the patch IB\*2.0\*608 is needed or if a better course of action is needed to correct through a new version of the patch (if prior to national release) or a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale back-out of the patch will still require a new version (if prior to national release) or a subsequent patch (after national release). If the back-out is post-release of patch IB\*2.0\*608, this patch should be assigned status of “Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A. The back-out process would be executed at normal, rather than raised job priority, and is expected to have no significant effect on total system performance. Subsequent to the reversion, the performance demands on the system would be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Transmitting SNF Claims with Appropriate Revenue Codes:

- The user should be able to create and transmit a Skilled Nursing Facility (SNF) Institutional claim for Medicare as a primary payer.
- The System should automatically add the new 2400 loop(s) and related segments to the flat file (This should not involve the user; there should be no change for the user).
- The flat file transmission from VistA to FSC should contain Health Insurance Prospective Payment System (HIPPS) Skilled Nursing Facility Rate Code information in the 2400 Loop segment SV202-1.
- The user should be able to see the HP information in the View/Print EDI Bill Extract Data \[IBCE EDI VIEW/PRINT EXTRACT\] (VPE) option under the INS record ID.
- The Claim should be able to pass the validator at the Financial Service Center (FSC).
- The Claim should be able to process at Medicare with the receipt of an electronic MRA back into the facilities VistA account.

> Add T for Transmitted to RCB Screen:

- The user should be able select the option RCB (View/Resubmit Claims - Live or Test \[IBCE PREV TRANSMITTED CLAIMS\]) to generate a list of previously printed claims for a specified date range.
- The System should show “\*\* T = Test Claim” in the legend at the top of the displayed screen.

> Remove Ability to Define Insurance Company as non-EDI:

- The user should be able to select the option EI - "Insurance Company Entry/Edit" \[IBCN INSURANCE CO EDIT\] to update the Billing/EDI Parameters.

> The available answers for the EDI - Transmit?: prompt should be: YES-LIVE

> YES-TEST

> (the choice NO should no longer be available)

- The existing HELP Text should display: “This field determines whether an electronic claim to this insurance Company is sent as a test or a production claim.”
- When the IB\*2.0\*608 patch is installed at a site, a report should be generated and sent to the eBiz Rapid Response group (REDACTED).
- The report should contain the Site Name, Site ID, Date of Report, the Insurance Company Name, the Insurance Company Address, the current setting for the Transmit Electronically field (#3.01) in Insurance Company file (#36) for those payers that have the Transmit Electronically field set to NO.

> RCB View/Resubmit Claims - Live or Test \[IBCE PREV TRANSMITTED CLAIMS\] Screen – Match COB Data to Payer Sequence:

- The user should be able to select the "View/Resubmit Claims - Live or Test" \[IBCE PREV TRANSMITTED CLAIMS\] (RCB) option.
- The user should be able to select one or more claim entries for resubmission to the Test queue.
- If the user selects a Primary claim to resubmit and the claim has received an EOB/MRA from the primary payer, VistA should not send the COB data from the EOB/MRA and the amount billed should not be offset by previous payments from the primary payer.
- If the user selects a Secondary claim to resubmit and the claim has received an EOB/MRA from the secondary payer, VistA should not send the COB data from the EOB/MRA and the amount billed should not be offset by previous payments from the secondary payer.
- If the user selects a Tertiary claim to resubmit and the claim has received an EOB/MRA from the tertiary payer, VistA should not send the COB data from the EOB/MRA and the amount billed should not be offset by previous payments from the tertiary payer.
- If the user attempts to resubmit a claim(s) with EOB data in VistA to the Production queue, the system should filter out and display the claim number(s) and not transmit it/them.

> Non-MCCF Unbilled Amounts Report:

- The user should be able to select the "Re-Generate Unbilled Amounts Report" \[IBT RE-GEN UNBILLED REPORT\] option.
- The Integrated Billing software should provide the ability for the user to specify the following *additional* search criteria when re-generating the Unbilled Amounts Report and not saving the results:

> CPAC Claims Only

> Non-CPAC Claims (CHAMPVA/TRICARE/INTERAGENCY/INELIGIBLE)

> Both

- CHAMPVA should include the Rate Types equal to “CHAMPVA” and “CHAMPVA REIMB. INS”.
- TRICARE should include the Rate Types equal to “TRICARE” and “TRICARE REIMB. INS”.

> Non-MCCF Pay-To Address Rate Types:

- The Integrated Billing software should provide the ability for an authorized user with access to the IB Site Parameters and the TRICARE Pay-to security key, to add a Rate Type for which claims with that Rate Type will use the non-MCCF Pay-To Address data.
- The Integrated Billing software should provide the ability for an authorized user with access to the IB Site Parameters and the TRICARE Pay-to security key, to delete a Rate Type for which claims with that Rate Type will use the non-MCCF Pay-To Address data.
- The Integrated Billing software should use the non-MCCF Pay-To Address data on claims with specified Rate Types only when the non-MCCF Pay-To Address is not exactly the same as the Billing Provider Name and Address.
- The Integrated Billing software should transmit the TRICARE Pay-To Address data on claims with specified Rate Types in the 837-I, 837-P or 837-D when the non-MCCF Pay-To Address is not exactly the same as the Billing Provider Name and Address.
- The Integrated Billing software should print the non-MCCF Pay-To Address data on Institutional claims with specified Rate Types on the UB04 form (FL2) when the TRICARE Pay-To Address is not exactly the same as the Billing Provider Name and Address.
- The Integrated Billing software should print the non-MCCF Pay-To Address data on Professional claims with specified Rate Types on the CMS 1500 form (Box 33) when the non-MCCF Pay-To Address is not exactly the same as the Billing Provider Name and Address.

> Remove Fatal Error – Rendering Provider CMS 1500:

- The Integrated Billing software should no longer require a Rendering Provider on Professional claims.
- The Integrated Billing software should display a non-fatal warning message to the user when a Professional claim does not contain a Rendering Provider.

> CMN Oxygen and EPN Nutrition:

- The Enter/Edit Billing Information \[IB EDIT BILLING INFO\] option – The System should conditionally prompt the user for the need on a CMN form for a procedure, based upon those CPTs that are entered into the new “CMN CPT CODE INCLUSIONS” site parameter.
- The Enter/Edit Billing Information \[IB EDIT BILLING INFO\] option – The System should prompt the user for the type of CMN form when a biller indicates a need for a CMN form (Only

> 484.3 and 10126 will be available at this time).

- The Enter/Edit Billing Information \[IB EDIT BILLING INFO\] option – The System should prompt the user for the data elements required to complete the type of CMN form selected.
- Transmit 837-P Transaction – The System should include the CMN related data elements in the outbound Professional 837 transaction.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The project is canceled, the requested changes implemented by IB\*2.0\*608 are no longer desired by VA OI&T and the Integrated Billing eBusiness team, or the patch produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since the eBilling software is tightly integrated with external systems, any attempt at a back-out should include close consultation with the external trading partners such as the Financial Services Center (FSC) and the Health Care Clearing House (HCCH) to determine risk.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Any back-out decision should be a joint decision of the Business Owner (or their representative) and the Program Manager with input from the Health Product Support (HPS) Application Coordinator, developers (both project and Tier 3 HPS), and if appropriate, external trading partners such as the VA FSC or HCCH.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The back-out procedure for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch.

> Back-Out Procedure prior to National Release. If it is prior to national release, the site will be already working directly with the development team daily and should contact that team. The development team members will have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that development team can quickly address via a new software version. If the site is unsure who to contact, they may log a ticket of contact Health Product Support - Management Systems Team.

> The IB\*2.0\*608 patch contains the following build components.

- Routines
- Protocols
- Modifications to the following files:
  - Insurance File \[#36\]
  - IB Error File \[#350.8\]
  - IB Site Parameters File \[#350.9\]
  - IB Data Element Definition File \[#364.5\]
  - IB Form Skeleton Definition File \[#364.6\]
  - IB Form Field Content File \[#364.7\]
  - Bill/Claims File \[#399\]
- Data Dictionary Changes
- Modifications to Templates:
  - Input Templates
  - List Templates

> While the VistA installation procedure of the KIDS build allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action, due to the complexity of this patch, it is not

> recommended for back-out, and a restore from a backup of the Transport Global should not be attempted. In the event that a site decides to back out this patch, the site should contact the National Service Desk (NSD) to submit a help desk ticket. The development team will need to issue a follow-on patch in order to comprehensively back-out this patch and/or to clean up corrupted data/remove data dictionary changes, if needed and restore the system to a functioning state.

> Please contact the EPMO team for assistance since this installed patch contains components in addition to routines.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Successful back-out is confirmed by verification that the back-out patch was successfully implemented. This includes successful installation and testing that the back-out acted as expected, as defined together with the team the site contacted in section 5.7.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Rollback pertains to data. The only data changes in this patch are specific to the operational software and platform settings. These data changes are covered in the Back-out procedures detailed elsewhere in this document.

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

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: IB*2*663 Deployment, Installation, Back-out/Rollback Guide

### March 2020 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OIT)

> Revision History

| Date   | Version | Description | Author |
|------------|-------------|-----------------|------------|
| 03/10/2020 | 1.0         | Initial draft   | AbleVets   |

### From: IB*2*623 Deployment, Installation, Back-out/Rollback Guide

### January 2020 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date     | Version | Description             | Author                         |
|--------------|-------------|-----------------------------|------------------------------------|
| January 2020 | 1.0         | Nationally released version | TAS MCCF eBilling Development Team |
|              |             |                             |                                    |
|              |             |                             |                                    |
|              |             |                             |                                    |

### From: IB*2*682 Deployment, Installation, Back-out/Rollback Guide

### October 2020 Department of Veterans Affairs

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
<td>10/19/2020</td>
<td>1.0</td>
<td>Initial release</td>
<td><blockquote>
<p>CC IBAR</p>
<p>Development Team</p>
</blockquote></td>
</tr>
</tbody>
</table>

### From: IB*2*660 Deployment, Installation, Back-out/Rollback Guide

### November 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OIT)

> Revision History

| Date   | Version | Description                                                         | Author |
|------------|-------------|-------------------------------------------------------------------------|------------|
| 11/14/2019 | 1.0         | Initial Documentation Release for Integrated Billing Patch IB\*2.0\*660 | AbleVets   |

### From: IB*2*678 Deployment, Installation, Back-out/Rollback Guide

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
<td>09/08/2020</td>
<td>1.0</td>
<td>Initial release</td>
<td><p>CC IBAR</p>
<p>Development Team</p></td>
</tr>
</tbody>
</table>

### From: IB*2*651 Deployment, Installation, Back-out/Rollback Guide

### September 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OIT)

> Revision History

| Date   | Version | Description | Author |
|------------|-------------|-----------------|------------|
| 09/30/2019 | 1.0         | Initial draft   | AbleVets   |

### From: IB*2*618 Deployment, Installation, Back-out/Rollback Guide

### August 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Revision History

| Date   | Version | Description           | Author |
|------------|-------------|---------------------------|------------|
| 08/01/2019 | 1.0         | Initial document creation | AbleVets   |
