---
title: TMP Release 5.0.4.1 Hotfix DIBRG
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: Hotfix DIBRG
app_code: TMP
app_name: Telehealth Management Platform
section: CLI
app_status: active
pkg_ns: TMP
patch_ver: 5.0.4.1
patch_id: TMP*5.0.4.1
group_key: "TMP:TMP:5.0.4.1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - deployment
  - mark
  - blockquote
  - installation
  - class
  - rollback
  - team
  - span
page_count: 0
word_count: 3262
section_count: 20
table_count: 12
figure_count: 2
appendix_count: 2
has_toc: False
is_stub: False
pub_date: August 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_dibrg_5_0_4_1.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_dibrg_5_0_4_1.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=231"
---

Telehealth Management Platform

Deployment, Installation, Back-Out, and Rollback Guide

![](tmp-release-5-0-4-1-hotfix-dibrg/001.png)

August 2023

Office of Information and Technology (OI&T)

Revision History

| Date               | Version | Description                                                                                  | Author |
|--------------------|---------|----------------------------------------------------------------------------------------------|--------|
| April 29, 2022     | 7.1     | Renamed release 4.9.0.10 to \<FUTURE RELEASE\>                                               |        |
| Jan 11, 2021       | 7.0     | Added URL to CRM code and deployment instructions for VVS version upgrade                    |        |
| September 25, 2020 | 6.0     | Added URL to CRM code and deployment instructions for combined releases TMP 4.8.1 and 4.8.2. |        |
| August 4, 2020     | 5.0     | Updated Deployment Date for TMP VistA Patch SD\*5.3\*754.                                    |        |
| June 19, 2020      | 4.0     | Added URL to CRM code and deployment instructions for TMP 4.8.0.                             |        |
| June 18, 2020      | 3.0     | Added URL to CRM code and deployment instructions for TMP 4.6.10 (Hotfix 10)                 |        |
| June 17, 2020      | 2.9     | Updated Deployment Date for TMP VistA Patch SD\*5.3\*746v1.                                  |        |
| May 27, 2020       | 2.8     | Added Deployment instructions for TMP VistA Patch SD\*5.3\*746v1.                            |        |
| May 27, 2020       | 2.7     | Added URL to CRM code and deployment instructions for TMP 4.6.9 (Hotfix 9)                   |        |
| May 13, 2020       | 2.6     | TMP D365 Product Upgrade Wave 1                                                              |        |
| May 6, 2020        | 2.5     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 8.                      |        |
| April 3, 2020      | 2.4     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 7.                      |        |
| March 26, 2020     | 2.3     | Added Deployment instructions for TMP VistA Patch SD\*5.3\*714v4.                            |        |
| January 21, 2020   | 2.2     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 6.                      |        |
| November 25, 2019  | 2.1     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 5.                      |        |
| November 19, 2019  | 2.0     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 4.                      |        |
| November 6, 2019   | 1.9     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 3.                      |        |
| October 25, 2019   | 1.8     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 2.                      |        |
| September 30, 2019 | 1.7     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 1.                      |        |

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

Table of Tables

Table of Figures

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
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
- [Back-Out Procedure](#back-out-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [### Deployment, Installation, Backup, Restore Instructions for TMP Release 5.0.4.1 Hotfix](#deployment-installation-backup-restore-instructions-for-tmp-release-5041-hotfix)
- [Appendix A – TMP Release Deployment Instructions](#appendix-a-tmp-release-deployment-instructions)
- [Deployment Instructions:](#deployment-instructions)
- [Backup:](#backup)
- [Installation Instructions:](#installation-instructions)
- [Appendix B – TMP Release Backout and Rollback Plan](#appendix-b-tmp-release-backout-and-rollback-plan)
- [Restore](#restore)
This document describes how to deploy and install the Telehealth Management Platform (TMP) Phase 3 Release 5.0.4.1 Hotfix, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed COTS product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Telehealth Management Platform (TMP) solution, will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figures 1, 2, 3, 4 and 5 illustrate the systems interfacing with TMP.

![](tmp-release-5-0-4-1-hotfix-dibrg/002.png)

Figure 1: TMP/VEIS (LOB & EC) Environment Mapping

![](tmp-release-5-0-4-1-hotfix-dibrg/003.png)

<span id="_Toc52275551" class="anchor"></span>Figure 2: TMP/VEIS/MVI Environment Mapping

![](tmp-release-5-0-4-1-hotfix-dibrg/004.png)

Figure 3: TMP/VEIS/ HealthShare Environment Mapping

<span id="_Toc52275508" class="anchor"></span>![](tmp-release-5-0-4-1-hotfix-dibrg/005.png)Figure 4: TMP/VEIS/VVS Environment Mapping

![](tmp-release-5-0-4-1-hotfix-dibrg/006.png)Figure 5: TMP/VEIS/VVS Environment Mapping

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no additional constraints to this project.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc52275540" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                                    | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|---------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
|        | O&M Team, Project Team and Development Team | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                 | TMP Release                      |
|        | O&M Team and Development Team               | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          | TMP Release                      |
|        | Enterprise Operations (EO)                  | Deployment       | Test for operational readiness                                                                                      | TMP Release                      |
|        | O&M Team                                    | Deployment       | Execute deployment                                                                                                  | TMP Release                      |
|        | O&M Team and Development Team               | Installation     | Plan and schedule installation                                                                                      | TMP Release                      |
|        | O&M Team/Hosting Team                       | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                       | TMP Release                      |
|        | O&M Team/Hosting Team                       | Installation     | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         | TMP Release                      |
|        | Training                                    | Installations    | Coordinate training                                                                                                 | TMP Release                      |
|        | O&M Team and Development Team               | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | TMP Release                      |

This section describes the teams who perform the steps described in this Plan. Representatives from the teams listed in the following table perform deployment and installation activities. This phase begins after the solution design (including deployment topology) is complete. Design activities are not included in this phase.

<span id="_Toc52275541" class="anchor"></span>Table 2: General Roles and Responsibilities

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Team</th>
<th>Tasks / Responsibilities</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>D365 Product Team</strong></td>
<td><ul>
<li><blockquote>
<p>Deploy code during migrations from lower environments into pre-prod and prod</p>
</blockquote></li>
<li><blockquote>
<p>Coordinate with VA Project Team members, VA NSOC, and Microsoft Support team</p>
</blockquote></li>
<li><blockquote>
<p>Receive and process incoming incidents via Cloud Ticket Determine incident types and capture all relevant incident data Create developer user accounts</p>
</blockquote></li>
<li><blockquote>
<p>Diagnose infrastructure issues</p>
</blockquote></li>
<li><blockquote>
<p>Troubleshoot basic and complex issues Resolve issues</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>VA Project Team</strong></td>
<td><ul>
<li><blockquote>
<p>Liaison between the project teams and team members to capture incidents</p>
</blockquote></li>
<li><blockquote>
<p>Submit incident requests using the Cloud Ticket tool</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Liberty Development Team</strong></td>
<td><ul>
<li><blockquote>
<p>Communicate with CRM Cloud Solution team to provide additional information, if necessary</p>
</blockquote></li>
<li><blockquote>
<p>Identify and submits issues to the VA project POC</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Liberty Development Team</strong></td>
<td><ul>
<li><blockquote>
<p>Deploy solutions provided by Microsoft Development Team from lower environments into pre-prod and prod</p>
</blockquote></li>
<li><blockquote>
<p>Coordinate with VA Project Team members, VA NSOC, and Microsoft Support team</p>
</blockquote></li>
<li><blockquote>
<p>Receive and process incoming incidents</p>
</blockquote></li>
<li><blockquote>
<p>Determine incident types and capture all relevant incident data</p>
</blockquote></li>
<li><blockquote>
<p>Diagnose incident issues Troubleshoot basic and complex issues Resolve issues</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc52275542" class="anchor"></span>Table 3: Code Deployment Responsibilities

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Team</th>
<th>Phase</th>
<th>Role</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Liberty Development Team</strong></td>
<td>Planning</td>
<td><ul>
<li><blockquote>
<p>Finalize Development Build and Code Compilation Instructions</p>
</blockquote></li>
<li><blockquote>
<p>Provide listing of developer accounts</p>
</blockquote></li>
<li><blockquote>
<p>Schedule deployment with the CRM Cloud Hosting team via Cloud Ticket</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>TMP Project Team</strong></td>
<td>Planning</td>
<td><ul>
<li><blockquote>
<p>Schedule UAT testers and support</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Liberty Development Team</strong></td>
<td>Prepare for Deployment</td>
<td><ul>
<li><blockquote>
<p>Provide O&amp;M Team with all relevant data/code including: solution extract for CRM, Compiled Code, and ISV Folder, utilizing a method approved by the Project Team (e.g. FTP, Secure Server, or other)</p>
</blockquote></li>
<li><blockquote>
<p>Freeze all development activities</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Liberty Development Team</strong></td>
<td>Prepare for Deployment</td>
<td><ul>
<li><blockquote>
<p>Review Code Compilation instructions for completion</p>
</blockquote></li>
<li><blockquote>
<p>Work with project teams if compilation instructions are unclear or incomplete</p>
</blockquote></li>
<li><blockquote>
<p>Replicate the existing environment configuration and code</p>
</blockquote></li>
<li><blockquote>
<p>Perform database back-ups</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>TMP Project Team</strong></td>
<td>Execute Deployment</td>
<td><ul>
<li><blockquote>
<p>Coordinate deployment support by maintaining the bridge and managing all involved stakeholders</p>
</blockquote></li>
<li><blockquote>
<p>Conduct UAT testing activities</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Liberty Development Team</strong></td>
<td>Execute Deployment</td>
<td>Work with O&amp;M team to resolve issues, if necessary</td>
</tr>
<tr class="odd">
<td><strong>O&amp;M Team</strong></td>
<td>Execute Deployment</td>
<td>Deploy the code into Pre-Prod and Prod</td>
</tr>
<tr class="even">
<td><strong>TMP Project Team</strong></td>
<td>Validation &amp; Go- Live</td>
<td>Validate that the new environment functions as expected</td>
</tr>
<tr class="odd">
<td><strong>O&amp;M Team</strong></td>
<td>Validation &amp; Go- Live</td>
<td>Execute roll-back, if necessary</td>
</tr>
</tbody>
</table>

The following table describes the planned deployment environments.

<span id="_Toc52275543" class="anchor"></span>Table 4: Deployment Environments

| Environment               | Use                               | Involved Parties       |
|---------------------------|-----------------------------------|------------------------|
| Developer Workstations    | Development, Unit Testing         | LITS                   |
| VA Hosted (NWA) Dev       | Development, Unit Testing         | LITS                   |
| VA Hosted (NWA) INT       | Unit Testing, Integration Testing | LITS, VA (Integration) |
| VA Hosted (NWA) QA        | User Acceptance Testing           | LITS, VA               |
| VA Hosted (NWA) Pre- Prod | Fallback for Production           | LITS, VA               |
| VA Hosted (NWA) Prod      | Production                        | LITS, VA               |

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a single rollout.

This section provides the schedule and milestones for the deployment.

This Release and Installation Guide identifies processes and procedures to promote the Telehealth Management Platform (TMP) Dynamics Customer Relationship Management (CRM) system into the Production Environment. The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

- TMP Dev
- TMP QA
- TMP Pre-Prod
- TMP Prod
- Git Hub

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation will run for approximately 1 day*,* as depicted in the master deployment schedule TMP.

In most Deployment Plans, Enterprise Operations (EO) maintains the master schedule in MS Project Server, Field Operations and Development (FOD) maintains its schedule in Clarity, and FOD provides site scheduling to meet parameters and milestones enumerated above. Given the agile methodology used to develop and deploy TMP, along with the limited scope of this software-only deployment/installation, there is no need for a Master Deployment Schedule. The high-level schedule included below will suffice.

<span id="_Toc52275544" class="anchor"></span>Table 5: High Level Milestones

| Milestones                                   | Target Date |
|----------------------------------------------|-------------|
| Unit Testing Completed                       |             |
| Software Quality Assurance Testing Completed |             |
| Pre-Production Testing Completed             |             |

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the TMP deployment. Topology determinations are made by ESE and vetted with PD, FO, NDCP, and the PMO during the design phase as appropriate. Field site coordination will be completed FO unless otherwise stipulated by FO. The Microsoft team provides input and support to all ESE, PD, FO, NDCP, and the PMO team during the site readiness assessment. TMP is a minor application covered under CRM/UD. Site readiness will be assessed in the hosting environment.

This section discusses the locations that will receive the TMP deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment will be conducted through web client in a QA, Pre-Prod, and Production environment administered by O&M, managed by Microsoft.

The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP will be accessed using the browser.

<span id="_Toc52275545" class="anchor"></span>Table 6: Site Preparation

| Site/Other | Problem/Change Needed            | Features to Adapt/Modify to New Product | Actions/Steps                            | Owner                                             |
|------------|----------------------------------|-----------------------------------------|------------------------------------------|---------------------------------------------------|
| All Sites  | Familiarization with application | N/A                                     | Attend training sessions                 | Office of Connected Care-Telehealth Training Team |
| All Sites  | Data Migration                   | N/A                                     | Metadata Import into Production          | Liberty Development team                          |
| All Sites  | Establish access to TMP URL      | N/A                                     | Grant access to application users of TMP | Will be handled by the appropriate region/site    |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes hardware, software, and facilities required for the TMP deployment and installation.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Current TMP release will deploy on CRM cloud hosted environment. There are no facility-specific features required for deployment.

<span id="_Toc52275546" class="anchor"></span>Table 7: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|------|------------|-----------------|-------|
| None |            |                 |       |

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Current TMP release will be supported by the existing cloud hosted environment. No hardware specifications exist.

<span id="_Toc52275547" class="anchor"></span>Table 8: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-------------------|-------|---------|---------------|--------------|-------|
| None              |       |         |               |              |       |

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Current TMP release will be utilizing approved existing software on TRM tools list. No software specifications exist.

<span id="_Toc52275548" class="anchor"></span>Table 9: Software Specifications

| Required Software | Make | Version | Configuration | Manufacturer | Other |
|-------------------|------|---------|---------------|--------------|-------|
| None              |      |         |               |              |       |

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VA Teams meeting will occur for all members involved and/or invested in TMP deployment. All members involved and/or invested in TMP Deployment will receive status emails throughout the deployment activities.

<span id="_Toc52275549" class="anchor"></span>Table 10: Team Support Information/Role

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 39%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><mark>Team Support Information</mark></th>
<th><mark>Role</mark></th>
<th><mark>POC</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><mark>Communication Lead</mark></p>
<p><em><mark>Scheduled</mark></em></p></td>
<td><mark>Serves as the main communication and coordination POC on behalf of the application to provide regular status updates and issue escalation.</mark></td>
<td></td>
</tr>
<tr class="even">
<td><p><mark>Functional Tester(s)</mark></p>
<p><em><mark>Scheduled</mark></em></p></td>
<td><mark>Performs testing to verify that application is functioning as expected.</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><p><mark>Development</mark></p>
<p><em><mark>On Call</mark></em></p></td>
<td><mark>Development resources are typically on-call for production deployments, unless they are required to serve as advisory resources during the release activities.</mark></td>
<td></td>
</tr>
<tr class="even">
<td><p><mark>VA OIT</mark></p>
<p><em><mark>On Call</mark></em></p></td>
<td><mark>Engage OIT contacts if decisions need to be made on behalf of the application and as voting members on the Go/No Go calls.</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><p><mark>VA Business / TDD</mark></p>
<p><em><mark>On Call</mark></em></p></td>
<td><mark>Engage Business Contacts if decisions need to be made on behalf of the application and as voting members on the Go/No Go calls.</mark></td>
<td></td>
</tr>
<tr class="even">
<td><p><mark>Application Support</mark></p>
<p><em><mark>Scheduled</mark></em></p></td>
<td><mark>Application Support contacts are scheduled to perform Production code releases and infrastructure changes.</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><p><mark>Hosting Support</mark></p>
<p><em><mark>On Call</mark></em></p></td>
<td><mark>Hosting Support contacts are scheduled to perform infrastructure changes or otherwise scheduled to be on call.</mark></td>
<td></td>
</tr>
<tr class="even">
<td><p><mark>Integration Partners</mark></p>
<p><em><mark>Scheduled</mark></em></p></td>
<td><mark>Typically, on-call support for the implementation or update of web service partner connections.</mark></td>
<td></td>
</tr>
</tbody>
</table>

#### Deployment/Installation/Back-Out Checklist

This section will be completed once each task is complete.

<span id="_Toc52275550" class="anchor"></span>Table 11: Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task                          |
|----------|-----|------|--------------------------------------------------------|
| Deploy   | TBD | TBD  | All Nationwide VistA Production Sites Patch Installers |
| Install  | TBD | TBD  | All Nationwide VistA Production Sites Patch Installers |
| Back-Out | TBD | TBD  | All Nationwide VistA Production Sites Patch Installers |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Customer-approved user stories and defects will be stored on the TMP JIRA:

TMP Requirements  
  

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP ORG is backed up by a member of the team the night of deployment.

Deployment occurs during off hours.

Software installs within 60-120 minutes.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

Table 12: File Inventory List

| Filename |
|----------|
|          |

File Inventory ListProvides folder locations and filenames for all release and installation files for this system

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Microsoft Dynamics CRM Security Role – System Administrator

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *TMP\<FUTURE RELEASE\> Deployment Instructions* (Appendix A).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *TMP Releases Deployment Instructions* (Appendix A). Verification/Testing Steps begin on page 1 of Appendix A.

For detailed testing, please also refer to the *TMP Releases Verification Testing Instructions* (Appendix A).

Notification sent to the field via email from Office of Connected Care Help Desk (OCCHD).

Users were informed of upcoming changes on a weekly call.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *TMP Combined Releases \<FUTURE RELEASE\> Deployment-Verification Testing Instructions* (Appendix A).

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *O&M Backout and Rollback Plan* (Appendix B).

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP ORG is backed up the night of deployment.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go/No-Go meeting will enable a decision to provide viability to proceed.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restore backup of Production environment taken prior to deployment.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No risks exist.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *O&M Backout and Rollback Plan* (Appendix B).

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A member of the Development Team will be assigned to this deployment.
- Evening prior to deployment – Approximately 10 pm a backup of TMP Production Environment
- Deployment Date– Upon completion of deployment activities (Installation, Verification, Testing), Go/No Go meeting will take place involving Stakeholders listed in 6.4. If decision of No Go is made, Rollback procedure will commence.
- Deployment Date – 11/26/2021

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Folder          | Filename        |
|-----------------|-----------------|
| See Section 4.6 | See Section 4.3 |

# ### Deployment, Installation, Backup, Restore Instructions for TMP Release 5.0.4.1 Hotfix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Appendix A – TMP Release Deployment Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides steps to deploy the TMP related changes in the Production environment:

# Deployment Instructions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides steps to deploy the TMP related changes in the Production environment:

1.  Begin Implementation for Change Request

# Backup: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Navigate to the
2.  Select the production environment “VA TMP Prod”.
3.  Create a manual backup as shown below:
4.  Please wait till you see a message like below:

# Installation Instructions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Solution Deployment:

1.  Download the following solutions from GitHub here:
2.  Import the solution using <u>Power Apps \| Solutions \| Link</u> è Publish all customizations twice.

> TMP Release 5.0.4.1Manual Configuration:

1.  Please click Confluence Link below and refer to all JIRA items that have DIBR Updates.

# Appendix B – TMP Release Backout and Rollback Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Navigate to the
2.  Select the production environment “VA TMP Prod”.
3.  Select Restore or manage under “Backups” link:
4.  Select the backup created in Backup step \#1 -\> Click Restore