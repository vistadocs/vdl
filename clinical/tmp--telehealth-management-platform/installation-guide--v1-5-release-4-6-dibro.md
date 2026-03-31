---
title: TMP Version 1.5 Release 4.6 DIBRO
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: Release 4.6 DIBRO
app_code: TMP
app_name: Telehealth Management Platform
section: CLI
app_status: active
pkg_ns: TMP
patch_ver: 1.5
patch_id: TMP*1.5
group_key: "TMP:TMP:1.5"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document describes how to deploy and install the Telehealth Management Platform (TMP) Phase 2 release 4.6, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases w
audience: 
keywords: 
  - table
  - contents
  - strong
  - deployment
  - team
  - application
  - class
  - rollback
  - installation
  - procedure
page_count: 0
word_count: 2681
section_count: 24
table_count: 12
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: August 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_deployment_installation_rollback_backout_guide_tmp_4-6.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_deployment_installation_rollback_backout_guide_tmp_4-6.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=231"
---

# Telehealth Management Platform (TMP) Phase 2 Release 4.6


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Telehealth Management Platform (TMP) Phase 2 Release 4.6](#telehealth-management-platform-tmp-phase-2-release-46)
    - [August 2019 Department of Veterans Affairs](#august-2019-department-of-veterans-affairs)
- [Artifact Rationale](#artifact-rationale)
    - [Table of Figures](#table-of-figures)
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
- [Appendix A – TMP Release 4.6 Deployment Instructions](#appendix-a-tmp-release-46-deployment-instructions)
  - [TMP Web Application Deployment](#tmp-web-application-deployment)
  - [Release 4.6 Verification Testing Instructions](#release-46-verification-testing-instructions)
- [Appendix B – O&M Backout and Rollback Plan](#appendix-b-om-backout-and-rollback-plan)
  - [Web Application Backout/Rollback](#web-application-backoutrollback)
  - [Vista Patches Backout](#vista-patches-backout)
> Deployment, Installation, Back-Out, and Rollback Guide
![](tmp-version-1-5-release-4-6-dibro/001.png)

### August 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)
> Revision History
| Date       | Version | Description                                                        | Author                                                                                  |
|----------------|-------------|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| August 2019    | 1.5         | Update with final v4.6 release/roll back info                          | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |
| March 2019     | 1.4         | Update for TMP Phase 2 v4.6                                            | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |
| August 2018    | 1.3         | Reflect information for TMP Phase 2 release 4.6                        | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |
| February 2018  | 1.2         | Dev Team provided updates to Appendix A and B                          | Microsoft Development Team                                                                  |
| February 2018  | 1.1         | Transitioned information to most recent/VIP approved document template | ProSphere Tek PMO Support Staff                                                             |
| September 2017 | 1.0         | Initial Version                                                        | PMO Support/ Microsoft Development Team/ O&M Team/ Hosting Team                             |

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.
### Table of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Figure 1: TMP/VIMT/VYOPTA Environment Mapping 5](#_bookmark3)

> [Figure 2: CVT/VIMT/MVI Environment Mapping 6](#_bookmark4)

> [Figure 3: TMP/VIMT/Accenture Environment Mapping 6](#_bookmark5)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes how to deploy and install the Telehealth Management Platform (TMP) Phase 2 release 4.6, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed COTS product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Telehealth Management Platform (TMP) solution, will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figures 1, 2, and 3 illustrate the systems interfacing with TMP.

![](tmp-version-1-5-release-4-6-dibro/003.png)

> <span id="_bookmark3" class="anchor"></span>Figure 1: TMP/VIMT/VYOPTA Environment Mapping

> ![](tmp-version-1-5-release-4-6-dibro/004.png)

> <span id="_bookmark4" class="anchor"></span>Figure 2: CVT/VIMT/MVI Environment Mapping

![](tmp-version-1-5-release-4-6-dibro/005.png)

> <span id="_bookmark5" class="anchor"></span>Figure 3: TMP/VIMT/Accenture Environment Mapping

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no additional constraints to this project.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark8" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                                    | Phase / Role | Tasks                                                                                                             | Project Phase (See Schedule) |
|--------|---------------------------------------------|------------------|-----------------------------------------------------------------------------------------------------------------------|----------------------------------|
|        | O&M Team, Project Team and Development Team | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                   | Build 4.6                        |
|        | O&M Team and Development Team               | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                            | Build 4.6                        |
|        | Enterprise Operations (EO)                  | Deployment       | Test for operational readiness                                                                                        | Build 4.6                        |
|        | O&M Team                                    | Deployment       | Execute deployment                                                                                                    | Build 4.6                        |
|        | O&M Team and Development Team               | Installation     | Plan and schedule installation                                                                                        | Build 4.6                        |
|        | O&M Team/Hosting Team                       | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                         | Build 4.6                        |
|        | O&M Team/Hosting Team                       | Installation     | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes           | Build 4.6                        |
|        | Training                                    | Installations    | Coordinate training                                                                                                   | Build 4.6                        |
|        | O&M Team and Development Team               | Back-out         | Confirm availability of back- out instructions and back-out strategy (what are the criteria that trigger a back- out) | Build 4.6                        |
|        | O&M Team/Hosting Team                       | Post Deployment  | Hardware, Software and System Support                                                                                 | Build 4.6                        |

> This section describes the teams who perform the steps described in this Plan. Representatives from the teams listed in the following table perform deployment and installation activities. This phase begins after the solution design (including deployment topology) is complete. Design activities are not included in this phase.

> <span id="_bookmark9" class="anchor"></span>Table 2: General Roles and Responsibilities

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team</strong></th>
<th><strong>Tasks / Responsibilities</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CRM Cloud Hosting Solution Team</strong></td>
<td><ul>
<li><p>Deploy code during migrations from lower environments into pre-prod and prod</p></li>
<li><p>Coordinate with VA Project Team members, VA NSOC, and Microsoft Support team</p></li>
<li><p>Receive and process incoming incidents via Cloud Ticket Determine incident types and capture all relevant incident data Create developer user accounts</p></li>
<li><p>Diagnose infrastructure issues</p></li>
<li><p>Troubleshoot basic and complex issues Resolve issues</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>VA Project Team</strong></td>
<td><ul>
<li><p>Liaison between the project teams and team members to capture incidents</p></li>
<li><p>Submit incident requests using the Cloud Ticket tool</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Microsoft Development Team</strong></td>
<td><ul>
<li><p>Communicate with CRM Cloud Solution team to provide additional information, if necessary</p></li>
<li><p>Identify and submits issues to the VA project POC</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>O&amp;M Team</strong></td>
<td><ul>
<li><p>Deploy solutions provided by Microsoft Development Team from lower environments into pre-prod and prod</p></li>
<li><p>Coordinate with VA Project Team members, VA NSOC, and Microsoft Support team</p></li>
<li><p>Receive and process incoming incidents</p></li>
<li><p>Determine incident types and capture all relevant incident data</p></li>
<li><p>Diagnose incident issues Troubleshoot basic and complex issues Resolve issues</p></li>
</ul></td>
</tr>
</tbody>
</table>

> <span id="_bookmark10" class="anchor"></span>Table 3: Code Deployment Responsibilities

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team</strong></th>
<th><strong>Phase</strong></th>
<th><strong>Role</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Microsoft Development Team</strong></td>
<td>Planning</td>
<td><ul>
<li><p>Finalize Development Build and Code Compilation Instructions</p></li>
<li><p>Provide listing of developer accounts</p></li>
<li><p>Schedule deployment with the CRM Cloud Hosting team via Cloud Ticket</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>TMP Project Team</strong></td>
<td>Planning</td>
<td><ul>
<li><p>Schedule UAT testers and support</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CRM Cloud Hosting Solution Team</strong></td>
<td>Planning</td>
<td><ul>
<li><p>Review deployment migration request (if needed) and schedule team member to provide support during the deployment</p></li>
<li><p>Schedule a deep dive with the Project Team, if necessary</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team</strong></th>
<th><strong>Phase</strong></th>
<th><strong>Role</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Microsoft Development Team</strong></td>
<td>Prepare for Deployment</td>
<td><ul>
<li><p>Provide O&amp;M Team with all relevant data/code including: solution extract for CRM, Compiled Code, and ISV Folder, utilizing a method approved by the Project Team (e.g. FTP, Secure Server, or other)</p></li>
<li><p>Freeze all development activities</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>O&amp;M Team</strong></td>
<td>Prepare for Deployment</td>
<td><ul>
<li><p>Review Code Compilation instructions for completion</p></li>
<li><p>Work with project teams if compilation instructions are unclear or incomplete</p></li>
<li><p>Replicate the existing environment configuration and code</p></li>
<li><p>Perform database back-ups</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>TMP Project Team</strong></td>
<td>Execute Deployment</td>
<td><ul>
<li><p>Coordinate deployment support by maintaining the bridge and managing all involved stakeholders</p></li>
<li><p>Conduct UAT testing activities</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Microsoft Development Team</strong></td>
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
<td><strong>CRM Cloud Hosting Solution Team</strong></td>
<td>Validation &amp; Go- Live</td>
<td>Execute roll-back, if necessary</td>
</tr>
</tbody>
</table>

> The following table describes the planned deployment environments.

> <span id="_bookmark11" class="anchor"></span>Table 4: Deployment Environments

| Environment                        | Use                           | Involved Parties            |
|----------------------------------------|-----------------------------------|---------------------------------|
| Developer Workstations                 | Development, Unit Testing         | Microsoft                       |
| Microsoft PSSC Development Environment | Development, Unit Testing         | Microsoft                       |
| VA Hosted (NWA) Dev                    | Development, Unit Testing         | Microsoft                       |
| VA Hosted (NWA) INT                    | Unit Testing, Integration Testing | Microsoft, VA (Integration)     |
| VA Hosted (NWA) QA                     | User Acceptance Testing           | Microsoft, VA                   |
| VA Hosted (NWA) Pre- Prod              | Fallback for Production           | Microsoft, VA, Hosting Provider |
| VA Hosted (NWA) Prod                   | Production                        | Microsoft, VA, Hosting Provider |

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment is planned as a single rollout.

> This section provides the schedule and milestones for the deployment.

> This Release and Installation Guide identifies processes and procedures to promote the Telehealth Management Platform (TMP) Dynamics Customer Relationship Management (CRM) system into the Production Environment. The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

- [<u>TMP Development (Dev) Environment</u>](https://internalcrm.tmp.dev.crm.vrm.vba.va.gov/cvt15)
- [<u>TMP Integration (INT) Environment</u>](https://internalcrm.np15.crm.vrm.vba.va.gov/INTTMP)
- [<u>TMP Quality Assurance (QA) Environment</u>](https://internalcrm.np15.crm.vrm.vba.va.gov/QATMP)
- [<u>TMP Pre-Production (Pre-Prod) Environnent</u>](https://internalcrm.np15.crm.vrm.vba.va.gov/PRETMP)
- [<u>TMP Production (Prod) Environment</u>](https://internalcrm.crm15.xrm.va.gov/TMP)

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment and installation will run for approximately 1 day*,* as depicted in the master deployment schedule TMP.

> In most Deployment Plans, Enterprise Operations (EO) maintains the master schedule in MS Project Server, Field Operations and Development (FOD) maintains its schedule in Clarity, and FOD provides site scheduling to meet parameters and milestones enumerated above. Given the agile methodology used to develop and deploy TMP, along with the limited scope of this software-only deployment/installation, there is no need for a Master Deployment Schedule. The high-level schedule included below will suffice.

> <span id="_bookmark14" class="anchor"></span>Table 5: High Level Milestones

| Milestones                                               | Target Date |
|--------------------------------------------------------------|-----------------|
| Software Quality Assurance Testing Completed                 | March 15, 2019  |
| Section 508 Testing Completed                                | March 15, 2019  |
| User Functionality Testing Completed                         | March 15, 2019  |
| Software Baseline Defined                                    | March 15, 2019  |
| Deployment of TMP to Primary Production Environment          | March 30, 2019  |
| Deployment of TMP to Secondary Production Environment        | March 30, 2019  |
| Testing of TMP in Primary Production Environment Completed   | March 30, 2019  |
| Testing of TMP in Secondary Production Environment Completed | March 30, 2019  |
| User Registration Completed (for new users)                  | N/A             |
| User Training Completed (if applicable)                      | NA              |

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the TMP deployment. Topology determinations are made by ESE and vetted with PD, FO, NDCP, and the PMO during the design phase as appropriate. Field site coordination will be completed FO unless otherwise stipulated by FO. The Microsoft team provides input and support to all ESE, PD, FO, NDCP, and the PMO team during the site readiness assessment. TMP is a minor application covered under CRM/UD. Site readiness will be assessed in the hosting environment.

> This section discusses the locations that will receive the TMP deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Deployment will be conducted through web client in a QA, PreProd, and Production environment administered by O&M, managed by Cloud Hosting team.

> The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TMP will be accessed using the hosting environment.

> <span id="_bookmark19" class="anchor"></span>Table 6: Site Preparation

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes hardware, software, and facilities required for the TMP deployment and installation.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TMP Phase 2 release 4.6 will deploy on CRM cloud hosted environment. There are no facility- specific features required for deployment.

> <span id="_bookmark22" class="anchor"></span>Table 7: Facility-Specific Features

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 30%" />
<col style="width: 38%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
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
<td>None</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TMP Phase 2 release 4.6 will be supported by the existing cloud hosted environment. No hardware specifications exist.

> <span id="_bookmark24" class="anchor"></span>Table 8: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| None                  |           |             |                   |                  |           |

> Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TMP Phase 2 release 4.6 will be utilizing approved existing software on TRM tools list. No software specifications exist.

> <span id="_bookmark26" class="anchor"></span>Table 9: Software Specifications

| Required Software | Make | Version | Configuration | Manufacturer | Other |
|-----------------------|----------|-------------|-------------------|------------------|-----------|
| None                  |          |             |                   |                  |           |

> Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A VA Lync meeting will occur for all members involved and/or invested in TMP deployment. All members involved and/or invested in TMP Deployment will receive status emails throughout the deployment activities.

> <span id="_bookmark28" class="anchor"></span>Table 10: Team Support Information/Role

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team Support Information</strong></th>
<th><strong>Role</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Communication Lead</p>
<p><em>Scheduled</em></p></td>
<td>Serves as the main communication and coordination POC on behalf of the application to provide regular status updates and issue escalation.</td>
</tr>
<tr class="even">
<td><p>Functional Tester(s)</p>
<p><em>Scheduled</em></p></td>
<td>Performs testing to verify that application is functioning as expected.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team Support Information</strong></th>
<th><strong>Role</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Development</p>
<p><em>On Call</em></p></td>
<td>Development resources are typically on-call for production deployments, unless they are required to serve as advisory resources during the release activities.</td>
</tr>
<tr class="even">
<td><p>VA OIT</p>
<p><em>On Call</em></p></td>
<td>Engage OIT contacts if decisions need to be made on behalf of the application and as voting members on the Go/No Go calls.</td>
</tr>
<tr class="odd">
<td><p>VA Business / TDD</p>
<p><em>On Call</em></p></td>
<td>Engage Business Contacts if decisions need to be made on behalf of the application and as voting members on the Go/No Go calls.</td>
</tr>
<tr class="even">
<td><p>Application Support</p>
<p><em>Scheduled</em></p></td>
<td>Application Support contacts are scheduled to perform Production code releases and infrastructure changes.</td>
</tr>
<tr class="odd">
<td><p>Hosting Support</p>
<p><em>On Call</em></p></td>
<td>Hosting Support contacts are scheduled to perform infrastructure changes or otherwise scheduled to be on call.</td>
</tr>
<tr class="even">
<td><p>Integration Partners</p>
<p><em>Scheduled</em></p></td>
<td>Typically, on-call support for the implementation or update of web service partner connections.</td>
</tr>
</tbody>
</table>

#### Deployment/Installation/Back-Out Checklist

> This section will be completed once each task is complete.

> <span id="_bookmark30" class="anchor"></span>Table 11: Deployment/Installation/Back-Out Checklist

| Activity | Day      | Time | Individual who completed task                                                           |
|--------------|--------------|----------|---------------------------------------------------------------------------------------------|
| Deploy       | Mar 30, 2019 | TBD      | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |
| Install      | Mar 30, 2019 | TBD      | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |
| Back-Out     | Mar 30, 2019 | TBD      | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Customer-approved user stories will be stored on the TMP Rational Tools: [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp)

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TMP ORG is backed up by a member of the team the night prior to deployment. Deployment occurs during off hours.

> Software installs within 60-120 minutes.

> Related VistA patches SD\*5.3\*704v9 and OR\*3.0\*496v3 must be installed in each VistA production system prior to user access of TMP v4.6. Patches will be released as “Emergency” patches and distributed by the Health Product Support Team through established FORUM National Patch Module emergency release procedures.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

> Table 12: File Inventory List

| Folder   | Filename                                                                                |
|--------------|---------------------------------------------------------------------------------------------|
| CRM_solution | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |
| CRM_solution | [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) |

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Microsoft Dynamics CRM Security Role – System Administrator BAH CRM Cloud – Deployment Administrator

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TMP Web Application: Refer to the *Release 4.6 Deployment Instructions* (Appendix A). VistA Patches: Pre-installation and installation instructions are contained in the Patch

> Description included with the deployment of each patch to the FORUM National Patch Module System. When each VistA site downloads and the KIDS Build for each patch, the installation instructions are displayed to the installer during the installation process in real time.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Web Application</u>: Refer to the *Release 4.6 Deployment Instructions* (Appendix A). Verification/Testing Steps begin on page 1 of Appendix A.

> For detailed testing, please also refer to the *Release 4.6 Verification Testing Instructions*

> (Appendix A).

> Notification sent to the field via email from National Telehealth Help Desk (NTTHD) Users provided URL[: http://vaww.infoshare.va.gov/sites/telehealth/Lists/tmpnew/view.aspx](http://vaww.infoshare.va.gov/sites/telehealth/Lists/tmpnew/view.aspx) Users were informed of upcoming changes on a weekly call.

> <u>VistA Patches</u>: When each patch is installed, a validation is automatically performed by the VistA Operating System and any errors are displayed to the installer in real time. If the patch does not install successfully, local installers are directed to reply with a patch update message through FORUM, which is then evaluated by the patch developers and specific instructions for re-installation are returned through FORUM.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the *Release 4.6 Deployment-Verification Testing Instructions* (Appendix A).

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Web Application: Refer to the *O&M Backout and Rollback Plan* (Appendix B). VistA Patches: Refer to *Patch Description Rollback Procedures* (Appendix B).

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TMP ORG is backed up the night prior to deployment.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Go/No-Go meeting will enable a decision to provide viability to proceed.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Restore backup of Production environment taken prior to deployment.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No risks exist.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TMP Web Application: Refer to the *O&M Backout and Rollback Plan* (Appendix B). VistA Patches: Refer to Patch Description Rollback Procedures (Appendix B).

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Web Application</u>: A member of the Development Team will be assigned to this deployment.

- Evening prior to deployment – Approximately 10 pm a backup of TMP Production Environment
- Deployment Date– Upon completion of deployment activities (Installation, Verification, Testing), Go/No Go meeting will take place involving Stakeholders listed in 6.4. If decision of No Go is made, Rollback procedure will commence.
- Deployment Date – 10/29/2018
  - TMP Production Org will be disabled
  - Deployment Date TMP Org backup is restored over deployment Org
  - Deployment Date TMP Org will be imported back into TMP Production Org
  - TMP Production Org will be re-enabled
  - TMP Production will be tested

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Folder      | Filename    |
|-----------------|-----------------|
| See Section 4.6 | See Section 4.3 |
|                 |                 |
|                 |                 |

# Appendix A – TMP Release 4.6 Deployment Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## TMP Web Application Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enable the Application User form and View in 9.0:
    1.  Go to the TMP Production instance
    2.  Navigate to Settings-\>Customizations-\>Customize the System-\>Entities-\>User
    3.  Enable the "Application User" System Form if not active:
        1.  Go to User-\>Forms
        2.  Verify whether the "Application User" form is under Inactive Forms. If so:
            1.  Select "Application User"
            2.  Click on Activate
    4.  Enable the System View
        1.  Go to User-\>Views
        2.  Verify whether the "Application User" form is under Inactive Public Views. If so:
            1.  Select "Application User"
            2.  Click on More Actions -\> Activate
    5.  Deactivate the System View
        1.  Go to Reserve Resource-\>Views -\>All Active Views.
        2.  Select "My Draft Appointments"
        3.  Click on More Actions -\> Deactivate
    6.  Deactivate the following views:

| Entity         | View                                     |
|----------------|------------------------------------------|
| Resource: User | @Me                                      |
|                | By Me                                    |
|                | Users Assigned to Mobile Offline Profile |
|                | Users Being Followed                     |
|                | Users I Follow                           |
|                | Users in this position                   |
|                | Users who follow you                     |
|                | Users: Influenced Deals That We Won      |

2.  Creating an Application User
    1.  In TMP go to Settings \> Security \>Users, Select Users

> ![](tmp-version-1-5-release-4-6-dibro/006.png)

2.  On the user’s screen switch the view to “Application Users”

> ![](tmp-version-1-5-release-4-6-dibro/007.png)

3.  Click +New to create a new application user, a user form will open.
4.  Switch the view to “Application User”

> ![](tmp-version-1-5-release-4-6-dibro/008.png)

5.  The follow field are required to create an application user:
1.  Application ID – This value is the Azure App ID
2.  Full Name – First Name and Last Name (will become value of “User Name”)
3.  Primary Email – Email address of the service account

> ![](tmp-version-1-5-release-4-6-dibro/009.png)

3.  Assigning a Security Role to the Application User: Application users are required to have a security role in Dynamics 365. It is recommended that a custom security role be created for each application user. Having a dedicated role will ensure the application functionality will not be changed inadvertently via a shared security role. *NOTE:* If you already have a security role, skip to step 5
    1.  To create a security role, go to Dynamics CRM \> Settings \> Security \> Security Roles
    2.  Click New to add a security role
    3.  Assign the required permissions
    4.  Go to the App User record you created in the earlier steps, Settings \> Security \> Users
    5.  Switch the view to *“Application Users”* and locate the user you created
    6.  In the ribbon click Manage Roles
    7.  A new window will open, select the role you want to add and click OK. The application user is now created, associated to the custom application and has the correct permissions.
4.  Unregister *<span class="mark"><u>REDACTED</u></span>* and all it steps
    1.  Go to Settings \> Customizations \> Customize the System
    2.  On the left navigation bar click “SDK Message Processing Step”
    3.  Find the *[<span class="mark">REDACTED</span>](http://vaww.telehealth.va.gov/quality/tmp/index.asp)* steps and un-register them
5.  Delete the duplicate views in the following entities. If you see multiple views with the same name, delete both/all of them.
    1.  Scheduling Package
    2.  TMP Resource
6.  The following solutions need to be imported in the order listed:
    1.  Plugin Profiler – *only if not installed in the target environment*
    2.  Dynamics365Remediation
    3.  UIUpdates
    4.  IntegrationPlugins

> To import the solution in TMP PROD follow the following steps:

1.  Go to Settings\>Import
2.  A new window will open, select the solution to import. Click Next\>Next
3.  The solution will begin to import, click publish when it is done importing
7.  Import the Integration Settings.
    1.  Export all the existing “Integration Settings” records and save it in an Excel file
    2.  Delete all the existing “Integration Settings” records
    3.  Locate the Integration Settings file, ensure it is in CSV format
    4.  In TMP PROD go to Settings\>Data Management\>Imports
    5.  Click Import Data in the ribbon
    6.  Choose the mapping file and select Next
    7.  Select the “Integration Settings” entity
    8.  Make sure the name and value pairs map
    9.  Click Next, the import process will begin
8.  Update Theme
    1.  Go to Settings \> Customizations\>Themes
    2.  Clone an existing theme and name it TMP
    3.  Match the color coding to the screenshot below

> ![](tmp-version-1-5-release-4-6-dibro/010.png)

4.  Publish the theme
9.  Update System Settings
    1.  Go to Settings \>Administration\>System Settings and update the below settings

> ![](tmp-version-1-5-release-4-6-dibro/011.png)

> To turn on the TMP Switches, please refer to the “TMP Switch Settings” document.

## Release 4.6 Verification Testing Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark50" class="anchor"></span>Click on the icon to open and view the testing instructions.

![](tmp-version-1-5-release-4-6-dibro/012.png)

> <span id="_bookmark51" class="anchor"></span>D365 IOC Test

> Scripts.docx

# Appendix B – O&M Backout and Rollback Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Web Application Backout/Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Click on the attachment icon to open and view the *O&M Backout and Rollback Plan* document*.*

![](tmp-version-1-5-release-4-6-dibro/013.png)

> OM_Backout_And\_ Rollback_Plan.docx

## Vista Patches Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>SD\*5.3\*704</u>

> Patch Back out Instructions:

> In the event of a catastrophic failure, the Facility CIO may make the decision to back-out the patch.

> It is imperative that you have performed a backup of the routines included in this patch prior to installation.

> The back-out plan is to restore the routines from the backup created. No data was modified by this patch installation and, therefore, no rollback strategy is required.

> Prior to installing an updated KIDS package, the site/region should have saved a backup of the routines in a mail message using the Backup a Transport Global \[XPD BACKUP\] menu option (this is done at time of install). The message containing the backed-up routines can be loaded with the "Xtract PackMan" function at the Message Action prompt. The Packman

> function "INSTALL/CHECK MESSAGE" is then used to install the backed up routines onto the VistA System.

> After installing the backed-up routines, the site will need to use the HL7/HLO options to edit the HL Logical Links and either delete these entries or delete the IP and Port information.

> The site will need to use FileMan to delete the new indices on the Patient File (#2), Appointment Multiple field (#2.98) and to delete the new index on the Hospital Location File (#44). These new indices are triggers that cause HL7 messages to be sent out of VistA to the TMP application. If this patch is backed out, these new indices need to be deleted to prevent the triggers from firing and creating the HL7

> messages.

> The other database changes do not need to be deleted as they do not impact any code or other functionality.

> VA FileMan 22.2

> Select OPTION: UTILITY FUNCTIONS

> Select UTILITY OPTION: CROSS-REFERENCE A FIELD OR FILE

> What type of cross-reference (Traditional or New)? Traditional// NEW

> Modify what File: HL7 APPLICATION PARAMETER// 44 HOSPITAL LOCATION

> (930 entries)

> Select Subfile:

> Current Indexes on file \#44:

> 445 'ACST' index

> 446 'AST' index 1346 'AG' index 1478 'ATMP1' index

> Choose E (Edit)/D (Delete)/C (Create): DELETE Which Index do you wish to delete? 1478 ATMP1

> Are you sure you want to delete the index definition? NO// YES Index definition deleted.

> Do you want to execute the old kill logic now? NO

> Compiling SDB Input Template of File 44.........................................

> ..

> 'SDBT' ROUTINE FILED...

> 'SDBT1' ROUTINE FILED...

> 'SDBT2' ROUTINE FILED.. 'SDBT3' ROUTINE FILED.. 'SDBT4' ROUTINE FILED. 'SDBT5' ROUTINE FILED.

> Current Indexes on file \#44:

> 445 'ACST' index

> 446 'AST' index 1346 'AG' index

> Choose E (Edit)/D (Delete)/C (Create):

> Select UTILITY OPTION: CROSS-REFERENCE A FIELD OR FILE

> What type of cross-reference (Traditional or New)? Traditional// new NEW

> Modify what File: HOSPITAL LOCATION// 2 PATIENT (1755 entries) Select Subfile: APPOINTMENT (Subfile \#2.98)

> Current Indexes on subfile \#2.98:

> 1333 'AX' whole file index (resides on file \#2) 1477 'AY' whole file index (resides on file \#2)

> Choose E (Edit)/D (Delete)/C (Create): DELETE Which Index do you wish to delete? 1333 AX

> Are you sure you want to delete the index definition? NO// YES

> Index definition deleted.

> Do you want to execute the old kill logic now? NO Current Indexes on subfile \#2.98:

> 1477 'AY' whole file index (resides on file \#2) Choose E (Edit)/D (Delete)/C (Create): DELETE

> Which Index do you wish to delete? 1477// AY

> Are you sure you want to delete the index definition? NO// YES Index definition deleted.

> Do you want to execute the old kill logic now? NO

> There are no INDEX file cross-references defined on subfile \#2.98. Want to create a new index for this file? No// NO

> Select UTILITY OPTION: <u>OR\*3.0\*496</u>

> Backout:

> Subj: Backup of OR\*3.0\*496 install on Jul 23, 2019 \[#363726\] 252 lines

> From: INSTALLER,PATCH In 'IN' basket. Page 1

> \$TXT PACKMAN BACKUP Created on Tuesday, 7/23/19 at 15:46:29 by INSTALLER,PATCH at CHY0035D.FO-BAYPINES.MED.VA.GOV

> \$ROU ORWCV (PACKMAN_BACKUP)

> ORWCV ; SLC/KCM,MS/PB - Background Cover Sheet Load; ; 06/10/09

> ;;3.0;ORDER ENTRY/RESULTS REPORTING;\*\*10,85,109,132,209,214,195,215,260,243,28 2,302,280,496\*\*;Nov 19, 2018;Build 1

> ;

> ;

> ; DBIA 1096 Reference to ^DGPM("ATID1"

> ; DBIA 1894 Reference to GETENC^PXAPI

> ; DBIA 1895 Reference to APPT2VST^PXAPI

> ; DBIA 2096 Reference to ^SD(409.63

> ; DBIA 2437 Reference to ^DGPM(

> ; DBIA 2965 Reference to ^DIC(405.1

> ; DBIA 4011 Access ^XWB(8994)

> ; DBIA 4313 Direct R/W permission to capacity mgmt global

> ^KMPTMP("KMPDT")

> ; DBIA 4325 References to AWCMCPR1

> ; DBIA 10061 Reference to ^UTILITY Type \<Enter\> to continue or '^' to exit: ^

> Enter message action (in IN basket): Ignore// Xtract PackMan Select PackMan function: IN

1.  INSTALL SELECTED ROUTINE(S)
2.  INSTALL/CHECK MESSAGE

> CHOOSE 1-2: 2 INSTALL/CHECK MESSAGE

> Warning: Installing this message will cause a permanent update of globals and routines.

> Do you really want to do this? NO// YES

> Routines are the only parts that are backed up. NO other parts

> are backed up, not even globals. You may use the 'Summarize Message' option of PackMan to see what parts the message contains.

> Those parts that are not routines should be backed up separately if they need to be preserved.

> Shall I preserve the routines on disk in a separate back-up message? YES// NO

> No backup message built.

> Line 2 Message \#363726 Unloading Routine ORWCV (PACKMAN_BACKUP) Select PackMan function:

> Enter message action (in IN basket): Ignore//