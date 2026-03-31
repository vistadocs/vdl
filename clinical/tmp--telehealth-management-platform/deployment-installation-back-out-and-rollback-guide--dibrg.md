---
consolidated_title: "tmp dibrg"
app_code: TMP
doc_type: DIBR
master_source: "TMP Version 2.0 Release 4.8 DIBRG"
master_pub_date: June 2020
consolidated_from: 9 versions
prior_versions:
  - "TMP Release 5.0.4 DIBRG"
  - "TMP Release 5.1 DIBRG"
  - "TMP Version 3.0 Release 4.9.0.6 DIBRG"
  - "TMP Version 4.0 Release 4.9.0.8 DIBRG"
  - "TMP Version 6.0 Release 4.9.0.9 DIBRG"
  - "TMP Version 9.1 Release 4.9.0.13 DIBRG"
  - "TMP Version 9.2 Release 4.9.0.14 DIBRG"
  - "TMP Version 9.3 Release 4.9.0.15 DIBRG"
---

Telehealth Management Platform Phase 3

Release 4.8.0

Deployment, Installation, Back-Out, and Rollback Guide

![](tmp-version-2-0-release-4-8-dibrg/001.png)

June 2020

Office of Information and Technology (OI&T)

Revision History

| Date               | Version | Description                                                                      | Author                          |
|--------------------|---------|----------------------------------------------------------------------------------|---------------------------------|
| June 19, 2020      | 4.0     | Added URL to CRM code and deployment instructions for TMP 4.8.0.                 | Redacted                        |
| June 18, 2020      | 3.0     | Added URL to CRM code and deployment instructions for TMP 4.6.10 (Hotfix 10)     | Redacted                        |
| June 17, 2020      | 2.9     | Updated Deployment Date for TMP VistA Patch SD\*5.3\*746v1.                      | Redacted                        |
| May 27, 2020       | 2.8     | Added Deployment instructions for TMP VistA Patch SD\*5.3\*746v1.                | Redacted                        |
| May 27, 2020       | 2.7     | Added URL to CRM code and deployment instructions for TMP 4.6.9 (Hotfix 9)       | Redacted                        |
| May 13, 2020       | 2.6     | TMP D365 Product Upgrade Wave 1                                                  | Redacted                        |
| May 6, 2020        | 2.5     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 8.          | Redacted                        |
| April 3, 2020      | 2.4     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 7.          | Redacted                        |
| March 26, 2020     | 2.3     | Added Deployment instructions for TMP VistA Patch SD\*5.3\*714v4.                | Redacted                        |
| January 21, 2020   | 2.2     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 6.          | Redacted                        |
| November 25, 2019  | 2.1     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 5.          | Redacted                        |
| November 19, 2019  | 2.0     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 4.          | Redacted                        |
| November 6, 2019   | 1.9     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 3.          | Redacted                        |
| October 25, 2019   | 1.8     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 2.          | Redacted                        |
| September 30, 2019 | 1.7     | Added URL to CRM code and deployment instructions for TMP 4.6 Hotfix 1.          | Redacted                        |
| September 2019     | 1.6     | Added URLs to code and updated deployment date                                   | Redacted                        |
| August 2019        | 1.5     | Update with final v4.6 release/roll back info                                    | Redacted                        |
| March 2019         | 1.4     | Update for TMP Phase 2 v4.6                                                      | Redacted                        |
| August 2018        | 1.3     | Reflect information for Telehealth Management Platform (TMP) Phase 2 release 4.6 | Redacted                        |
| February 2018      | 1.2     | Dev Team provided updates to Appendix A and B                                    | Microsoft Development Team      |
| February 2018      | 1.1     | Transitioned information to most recent/VIP approved document template           | ProSphere Tek PMO Support Staff |
| September 2017     | 1.0     | Initial Version                                                                  | ProSphere Tek PMO Support Staff |

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
- [Appendix A – TMP Release 4.8.0 Deployment Instructions](#appendix-a-tmp-release-480-deployment-instructions)
  - [CRM Deployment Instructions](#crm-deployment-instructions)
  - [VEIS Deployment Instructions](#veis-deployment-instructions)
- [Appendix B – O&M Backout and Rollback Plan](#appendix-b-om-backout-and-rollback-plan)
  - [Backout/Rollback Plan](#backoutrollback-plan)
This document describes how to deploy and install the Telehealth Management Platform (TMP) Phase 3 Release 4.8.0, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed COTS product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Telehealth Management Platform (TMP) solution, will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figures 1, 2, and 3 illustrate the systems interfacing with TMP.

![](tmp-version-2-0-release-4-8-dibrg/002.png)

<span id="_Toc43822038" class="anchor"></span>Figure 1: TMP/VIMT/VYOPTA Environment Mapping

![](tmp-version-2-0-release-4-8-dibrg/003.png)

<span id="_Toc43822039" class="anchor"></span>Figure 2: CVT/VIMT/MVI Environment Mapping

![](tmp-version-2-0-release-4-8-dibrg/004.png)

<span id="_Toc43822040" class="anchor"></span>Figure 3: TMP/VIMT/Accenture Environment Mapping

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no additional constraints to this project.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc43822027" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                                    | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|---------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
|        | O&M Team, Project Team and Development Team | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                 | TMP 4.8.0                        |
|        | O&M Team and Development Team               | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          | TMP 4.8.0                        |
|        | Enterprise Operations (EO)                  | Deployment       | Test for operational readiness                                                                                      | TMP 4.8.0                        |
|        | O&M Team                                    | Deployment       | Execute deployment                                                                                                  | TMP 4.8.0                        |
|        | O&M Team and Development Team               | Installation     | Plan and schedule installation                                                                                      | TMP 4.8.0                        |
|        | O&M Team/Hosting Team                       | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                       | TMP 4.8.0                        |
|        | O&M Team/Hosting Team                       | Installation     | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         | TMP 4.8.0                        |
|        | Training                                    | Installations    | Coordinate training                                                                                                 | TMP 4.8.0                        |
|        | O&M Team and Development Team               | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | TMP 4.8.0                        |
|        | O&M Team/Hosting Team                       | Post Deployment  | Hardware, Software and System Support                                                                               | TMP 4.8.0                        |

This section describes the teams who perform the steps described in this Plan. Representatives from the teams listed in the following table perform deployment and installation activities. This phase begins after the solution design (including deployment topology) is complete. Design activities are not included in this phase.

<span id="_Toc43822028" class="anchor"></span>Table 2: General Roles and Responsibilities

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
<td><strong>CRM Cloud Hosting Solution Team</strong></td>
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
<td><strong>Microsoft Development Team</strong></td>
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
<td><strong>O&amp;M Team</strong></td>
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

<span id="_Toc43822029" class="anchor"></span>Table 3: Code Deployment Responsibilities

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
<td><strong>Microsoft Development Team</strong></td>
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
<td><strong>CRM Cloud Hosting Solution Team</strong></td>
<td>Planning</td>
<td><ul>
<li><blockquote>
<p>Review deployment migration request (if needed) and schedule team member to provide support during the deployment</p>
</blockquote></li>
<li><blockquote>
<p>Schedule a deep dive with the Project Team, if necessary</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Microsoft Development Team</strong></td>
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
<tr class="odd">
<td><strong>O&amp;M Team</strong></td>
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
<tr class="even">
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
<tr class="odd">
<td><strong>Microsoft Development Team</strong></td>
<td>Execute Deployment</td>
<td>Work with O&amp;M team to resolve issues, if necessary</td>
</tr>
<tr class="even">
<td><strong>O&amp;M Team</strong></td>
<td>Execute Deployment</td>
<td>Deploy the code into Pre-Prod and Prod</td>
</tr>
<tr class="odd">
<td><strong>TMP Project Team</strong></td>
<td>Validation &amp; Go- Live</td>
<td>Validate that the new environment functions as expected</td>
</tr>
<tr class="even">
<td><strong>CRM Cloud Hosting Solution Team</strong></td>
<td>Validation &amp; Go- Live</td>
<td>Execute roll-back, if necessary</td>
</tr>
</tbody>
</table>

The following table describes the planned deployment environments.

<span id="_Toc43822030" class="anchor"></span>Table 4: Deployment Environments

| Environment                            | Use                               | Involved Parties                |
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

The deployment is planned as a single rollout.

This section provides the schedule and milestones for the deployment.

This Release and Installation Guide identifies processes and procedures to promote the Telehealth Management Platform (TMP) Dynamics Customer Relationship Management (CRM) system into the Production Environment. The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

<span id="_Toc421540861" class="anchor"></span>Redacted

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation will run for approximately 1 day*,* as depicted in the master deployment schedule TMP.

In most Deployment Plans, Enterprise Operations (EO) maintains the master schedule in MS Project Server, Field Operations and Development (FOD) maintains its schedule in Clarity, and FOD provides site scheduling to meet parameters and milestones enumerated above. Given the agile methodology used to develop and deploy TMP, along with the limited scope of this software-only deployment/installation, there is no need for a Master Deployment Schedule. The high-level schedule included below will suffice.

<span id="_Toc43822031" class="anchor"></span>Table 5: High Level Milestones

| Milestones                                                   | Target Date |
|--------------------------------------------------------------|-------------|
| Software Quality Assurance Testing Completed                 | TBD         |
| Section 508 Testing Completed                                | TBD         |
| User Functionality Testing Completed                         | TBD         |
| Software Baseline Defined                                    | TBD         |
| Deployment of TMP to Primary Production Environment          | TBD         |
| Deployment of TMP to Secondary Production Environment        | TBD         |
| Testing of TMP in Primary Production Environment Completed   | TBD         |
| Testing of TMP in Secondary Production Environment Completed | TBD         |
| User Registration Completed (for new users)                  | N/A         |
| User Training Completed (if applicable)                      | NA          |

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the TMP deployment. Topology determinations are made by ESE and vetted with PD, FO, NDCP, and the PMO during the design phase as appropriate. Field site coordination will be completed FO unless otherwise stipulated by FO. The Microsoft team provides input and support to all ESE, PD, FO, NDCP, and the PMO team during the site readiness assessment. TMP is a minor application covered under CRM/UD. Site readiness will be assessed in the hosting environment.

This section discusses the locations that will receive the TMP deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment will be conducted through web client in a QA, PreProd, and Production environment administered by O&M, managed by Cloud Hosting team.

The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP will be accessed using the hosting environment.

<span id="_Toc43822032" class="anchor"></span>Table 6: Site Preparation

| Site/Other | Problem/Change Needed            | Features to Adapt/Modify to New Product | Actions/Steps                            | Owner                                          |
|------------|----------------------------------|-----------------------------------------|------------------------------------------|------------------------------------------------|
| All Sites  | Familiarization with application | N/A                                     | Attend training sessions                 | Rocky Mountain National Training Center        |
| All Sites  | Data Migration                   | N/A                                     | Metadata Import into Production          | Microsoft Development team                     |
| All Sites  | Establish access to TMP URL      | N/A                                     | Grant access to application users of TMP | Will be handled by the appropriate region/site |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes hardware, software, and facilities required for the TMP deployment and installation.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP Release 4.8.0 will deploy on CRM cloud hosted environment. There are no facility-specific features required for deployment.

<span id="_Toc43822033" class="anchor"></span>Table 7: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|------|------------|-----------------|-------|
| None |            |                 |       |

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP Release 4.8.0 will be supported by the existing cloud hosted environment. No hardware specifications exist.

<span id="_Toc43822034" class="anchor"></span>Table 8: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-------------------|-------|---------|---------------|--------------|-------|
| None              |       |         |               |              |       |

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP Release 4.8.0 will be utilizing approved existing software on TRM tools list. No software specifications exist.

<span id="_Toc43822035" class="anchor"></span>Table 9: Software Specifications

| Required Software | Make | Version | Configuration | Manufacturer | Other |
|-------------------|------|---------|---------------|--------------|-------|
| None              |      |         |               |              |       |

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VA Lync meeting will occur for all members involved and/or invested in TMP deployment. All members involved and/or invested in TMP Deployment will receive status emails throughout the deployment activities.

<span id="_Toc43822036" class="anchor"></span>Table 10: Team Support Information/Role

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Team Support Information</th>
<th>Role</th>
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

This section will be completed once each task is complete.

<span id="_Toc43822037" class="anchor"></span>Table 11: Deployment/Installation/Back-Out Checklist

| Activity | Day        | Time | Individual who completed task |
|----------|------------|------|-------------------------------|
| Deploy   | 06/25/2020 | TBD  | VA Tier 2 Team                |
| Install  | 06/25/2020 | TBD  | VA Tier 2 Team                |
| Back-Out | 06/25/2020 | TBD  | VA Tier 2 Team                |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Customer-approved user stories and defects will be stored on the TMP Rational Tools:

[redacted](https://clm.rational.oit.va.gov/ccm/web/projects/TMP%20(CM)#action=com.ibm.team.workitem.runSavedQuery&id=_E4EYZ_slEem2COwW-St7Kw&orderBy=workItemType&direction=ascending)

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP ORG is backed up by a member of the team the night prior to deployment.

Deployment occurs during off hours.

Software installs within 60-120 minutes.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CRM system is web-based and is deployed using files containing configuration information rather than directly from one environment to another.

Table 12: File Inventory List

| Filename                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [redacted](https://dvagov.sharepoint.com/sites/OITEPMOTMP3/Shared%20Documents/Forms/AllItems.aspx?viewid=da348dfd%2Def61%2D4274%2Daede%2D309dab097636&id=%2Fsites%2FOITEPMOTMP3%2FShared%20Documents%2FDeployment%20Code%20Files%2FRelease%204%2E8%2E0) |

File Inventory ListProvides folder locations and filenames for all release and installation files for this system

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Microsoft Dynamics CRM Security Role – System Administrator

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *TMP Release 4.8.0 Deployment Instructions* (Appendix A).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *TMP Release 4.8.0 Deployment Instructions* (Appendix A). Verification/Testing Steps begin on page 1 of Appendix A.

For detailed testing, please also refer to the *TMP Release 4.8.0 Verification Testing Instructions* (Appendix A).

Notification sent to the field via email from National Telehealth Help Desk (NTTHD)

Users provided URL: <http://vaww.infoshare.va.gov/sites/telehealth/Lists/tmpnew/view.aspx>

Users were informed of upcoming changes on a weekly call.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *TMP Release 4.8.0 Deployment-Verification Testing Instructions* (Appendix A).

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *O&M Backout and Rollback Plan* (Appendix B).

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP ORG is backed up the night prior to deployment.

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
- Deployment Date – 06/25/2020
- TMP Production Org will be disabled
- Deployment Date TMP Org backup is restored over deployment Org
- Deployment Date TMP Org will be imported back into TMP Production Org
- TMP Production Org will be re-enabled
- TMP Production will be tested

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Folder          | Filename        |
|-----------------|-----------------|
| See Section 4.6 | See Section 4.3 |

# Appendix A – TMP Release 4.8.0 Deployment Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CRM Deployment Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides steps to deploy the related changes in the Production environment. 

1.  Open Internet Explorer and launch TMP Production instance. 
2.  Navigate to Settings \>\> Solutions and click on Import. 
3.  Browse to the solution \<\<SOLUTION NAME\>\> located at  

[\<\<URL PROVIDED BY VA ON THE VA SP\>\>](https://dvagov.sharepoint.com/sites/OITEPMOTMP3/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FOITEPMOTMP3%2FShared%20Documents%2FDeployments%2F2019%5F08%5F08%20%2D%20D365%20Remediation%2FTMP%204%2E6%20Hotfix%205&viewid=da348dfd%2Def61%2D4274%2Daede%2D309dab097636) 

and progress through the import process.  

4.  Publish All Customizations. 

Post Deployment Steps 

Trigger Facility Approval Review Process 

There is a workflow One Time: Trigger Facility Approval Yearly Review Process, which helps trigger the recursive workflow “Email Automation: Facility Approval Yearly Review". 

  

The following steps must be performed: 

- Navigate to Settings \>\> Processes 
- Deactivate the workflow “One Time: Trigger Facility Approval Yearly Review Process”, if already Activated 
- Set the Timeout until to<u>9:30 AM EST</u> for the next day (*the day following the deployment*) 

![](tmp-version-2-0-release-4-8-dibrg/005.png) 

> **NOTE:** The time zone of the user in TMP, making the change to the workflow must be EST, so that the time set by the user is considered 9:30 AM EST. 

- Save and Activate the Workflow 
- Run the workflow “One Time: Trigger Facility Approval Yearly Review Process” against any Email Automation record (*navigate via Settings \>\> Email Automation*). 

 

To confirm that the “One Time: Trigger Facility Approval Yearly Review Process” did trigger,   

navigate to Settings \>\> System Jobs and check that the “One Time: Trigger Facility Approval Yearly Review Process" system job shows with the Status Reason of “Waiting for timer”. 

 

Workflow Ownership 

Navigate to Settings \>\> Processes and switch to All Processes view. Search for the workflow “Approval Process - Get Owner” and perform the following steps: 

- Check the Owner of the workflow. If the Owner is “VHA, TMP Scheduling”, then skip the following steps 
- If the Owner is not “VHA, TMP Scheduling”, and the workflow is activated, deactivate the workflow 
- Change the Owner to “VHA, TMP Scheduling” 
- Save and Activate the Workflow  

 

Patient Technology Type 

After the Dynamics solution deployment, the Technology Type option set will display the following 5 options (*as shown below*). 

![](tmp-version-2-0-release-4-8-dibrg/006.png) 

 

<u>Update Technology Type for existing Patients</u> 

1.  Create an Advanced Find to search Patients with the Technology Type of either “COTS Tablet” or “CVT Tablet”, as shown below: 

![](tmp-version-2-0-release-4-8-dibrg/007.png) 

  

1.  Edit Columns and add the Technology Type column: 

![](tmp-version-2-0-release-4-8-dibrg/008.png) 

  

1.  Execute the Advanced Find query and export the result to an excel sheet. 
2.  Update the Technology Type field to "SIP Device" for all the records in the excel, and Save the file. 
3.  Import the file to Dynamics using OOB Import Wizard.   

  

  

<u>Remove "CVT Tablet" and "COTS Tablet" options</u> 

 The CVT Tablet and COTS Tablet options must be manually removed. Navigate to the Fields of the Patient entity within the imported solution:  

![](tmp-version-2-0-release-4-8-dibrg/009.png) 

  

Open the Technology Type field, and delete the CVT Tablet and COTS Tablet options.  

![](tmp-version-2-0-release-4-8-dibrg/010.png) 

  

After the deletion, the Technology Type field must only have the following options: 

- Personal Device 
- VA Issued Device 
- SIP Device 

 

TSA Yearly Review Process 

After the Dynamics solution deployment, the workflow Email Automation: Facility Approval Yearly Review must be manually triggered. NOTE: THIS WORKFLOW SHOULD ONLY BE TRIGGERED ONCE. 

 

1.  Open Advanced Find and create a query to retrieve Email Automation. 

![](tmp-version-2-0-release-4-8-dibrg/011.png) 

 

2.  Select Results and open any Email Automation record. Select Run Workflow and make sure that Email Automation: Facility Approval Yearly Review is checked. Select Add, then Ok. 

![](tmp-version-2-0-release-4-8-dibrg/012.png) 

 

 

TSA Review Due Date 

After the Dynamics solution deployment, the Review Due Date must be set for TSAs which are in Approved Status, without a Review Due Date. 

 

<u>Export existing TSAs </u> 

1.   Open Advanced Find and create a query to retrieve TSAs where Review Due Date is set to “Does Not Contain Data”. 

![](tmp-version-2-0-release-4-8-dibrg/013.png) 

 

2.  Edit Columns to contain only Name, Modified On, and Review Due Date. 

![](tmp-version-2-0-release-4-8-dibrg/014.png) 

 

3.  Select Results, then Export TSAs as Static Worksheet. 

 

![](tmp-version-2-0-release-4-8-dibrg/015.png) 

 

4.  Download and open the excel worksheet. Add the following formula: =DATE(YEAR(\[@\[Modified On\]\])+1,MONTH(\[@\[Modified On\]\]),DAY(\[@\[Modified On\]\])+30)+TIME(23,59,59) in the first empty cell below the Review Due Date column (F2). This should populate all cells in the Review Due Date column.  

![](tmp-version-2-0-release-4-8-dibrg/016.png) 

 

5.  Copy all the cells in the Review Due Date column (excluding the Review Due Date header). Then, replace these cells by pasting as Value. NOTE: THE IMPORT WILL FAIL IF THE FORMULAS ARE NOT REPLACED WITH VALUES VIA THIS STEP. 

![](tmp-version-2-0-release-4-8-dibrg/017.png) 

 

6.  Verify that all the cells in the Review Due Date column have now been replaced with the date Value. Save the file. 

![](tmp-version-2-0-release-4-8-dibrg/018.png) 

 

7.  In the TMP Site Map, got to Settings à Data Management 

![](tmp-version-2-0-release-4-8-dibrg/019.png) 

 

8.  Select Imports. 

![](tmp-version-2-0-release-4-8-dibrg/020.png) 

 

9.  Select Import Data.  

![](tmp-version-2-0-release-4-8-dibrg/021.png) 

 

10. Step through the wizard. When you arrive at the below page, ensure that Allow Duplicates is set to No. Click Submit. 

![](tmp-version-2-0-release-4-8-dibrg/022.png) 

 

11. Confirm that the Data Import was able to successfully import all records. 

![](tmp-version-2-0-release-4-8-dibrg/023.png) 

## VEIS Deployment Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Supported Browser 

Internet Explorer (version 11) is the currently supported and tested browser at the time of this document for Kudu. Although other browsers such as Edge may work, it is not fully tested and may have some features that only work in Internet Explorer. 

 

Pre-Requisites 

“ihs-lob-prod-tmp.zip” file is required for deployment. It is included in the “Release 4.8.0” folder located on SharePoint ([here](https://dvagov.sharepoint.com/sites/OITEPMOTMP3/Shared%20Documents/Forms/AllItems.aspx?viewid=da348dfd%2Def61%2D4274%2Daede%2D309dab097636&id=%2Fsites%2FOITEPMOTMP3%2FShared%20Documents%2FDeployment%20Code%20Files%2FRelease%204%2E8%2E0)). 

 

Links to Kudu for Load-Balanced Production Azure Web Apps 

IHS-LOB-PROD-TMP-EAST 

 

<u>https://ihs-lob-prod-tmp-east.scm.prod.vaec.va.gov/DebugConsole</u> 

￼IHS-LOB-PROD-TMP-SOUTH 

 

<u>https://ihs-lob-prod-tmp-south.scm.prod.vaec.va.gov/DebugConsole</u> 

￼Page Break 

Deployment Steps 

This section provides how to deploy the VEIS Component Web App code (.zip file) to the corresponding Azure Web App in the Production Environment. 

Note*: These steps are how to deploy *<u>one</u>* Azure Web App. There is a total of *<u>two</u>* Azure Web Apps. These steps must be implemented *<u>twice</u>* in total. *

1.  Open Internet Explorer and navigate to the named Production Azure Web App resource via the Azure Portal (see <u>“Links to Kudu for both Load-Balanced Production Web Apps”</u> for resource names). 
2.  Stop the Service. 
3.  Navigate to the Azure Web App’s Kudu Console using the provided URL (see <u>“Links to Kudu for both Load-Balanced Production Web Apps”</u>). 
4.  Once in Kudu, navigate to /wwwroot. 
5.  On the computer, open File Explorer and navigate to the location of the “ihs-lob-prod-tmp.zip” file. 
6.  Drag the zip file from File Explorer over to the right-hand side of the table displayed in the Kudu Console. A logo “Drag here to upload and unzip” will display. Drop the zip file on top of this logo. 

![](tmp-version-2-0-release-4-8-dibrg/024.png) 

The contents will automatically unzip and overwrite everything located at /wwwroot. 

7.  Navigate back to the Production Azure Web App resource via the Azure Portal and Start the Service. 

# Appendix B – O&M Backout and Rollback Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Backout/Rollback Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a safeguard approach, an on-demand backup of the Production Dynamics instance must be taken. 

1.  Browse directly to the instance picker URL <https://port.crm9.dynamics.com/G/Instances/InstancePicker.aspx?Redirect=True> and sign in with System Administrator. 
2.  Click the Backup & Restore tab and navigate to either the new Power Platform admin center or use the old backup and restore page. 
3.  Select the VA TMP Prod instance and click on New backup to create a backup.  

 

Please refer to the link <https://docs.microsoft.com/en-us/dynamics365/admin/backup-restore-instances> for additional details, in case a restore would be needed. 

In a scenario where Production instance has to be restored, please ensure that the instance is restored to the settings as depicted in the image below (*this is what Production instance has today*): 

![](tmp-version-2-0-release-4-8-dibrg/025.png)

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: TMP Release 5.1 DIBRG

### Deployment/Installation/Back-Out Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section will be completed once each task is complete.

<span id="_Toc146287295" class="anchor"></span>Table 11: Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | TBD | TBD  |                               |
| Install  | TBD | TBD  |                               |
| Back-Out | TBD | TBD  |                               |

## Wave 2 2023 Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To activate the wave 2 update
2.  Go to
3.  Select Environments in the left-hand navigation.
4.  Select the environment to update in the list.
5.  In the Update box, select Manage.
6.  Select Update Now.
7.  Wait for the update to complete. It may take an hour or two.

## Solution Deployment to hide New Look toggle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To get the solution:

1.  Go to PowerApps:
2.  On the top navigation, select Environment and select VA TMP Dev.
3.  On the left navigation, select Solutions.
4.  Select the New Look solution.
5.  On the ribbon, select Export.
6.  When the export is done, there'll be a green message below the ribbon.

To import the solution

1.  Go to PowerApps:
2.  On the top navigation, select Environment and select the environment you want to import the solution to.
3.  On the left navigation, select Solutions.
4.  On the ribbon, select Import Solution.
5.  Select Browse.
6.  Find the New Look solution on your machine and select it.
7.  Wait for the import to finish - there'll be a green message below the ribbon.
8.  Select Publish All Customizations.
9.  Wait for the publish to finish - there'll be a green message below the ribbon.
10. Select Publish All Customizations a second time.
11. Wait for the publish to finish - there'll be a green message below the ribbon.
12. Go to the environment and confirm the New Look button is gone.

## TSL API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a deployment to nprod, use the correct Publish Profile to publish.

To deploy the TSL API:

1.  Log into Kudu for either the Prod East or Prod South regions for the Telehealth Specialty Location App Service.  If you don't have the Publish Profile(s) for them you'll need to log into Azure and download them, first.  Use the publishUrl, userName and UserPwd values from the Publish Profile to log into Kudu.
2.  Select the CMD option from the Debug console menu.

![](tmp-release-5-1-dibrg/007.png)

3.  Then click on site link, followed by the.
4.  Open Integration Solutions Project in Visual Studio.
5.  Locate the TelehealthSpecialtyLocation API Project in the LOB Api Folder (VA.TMP.Integration.Api.TelehealthSpecialtyLocation).

![](tmp-release-5-1-dibrg/008.png)

6.  Either right-click on the Project and select the Publish option or select the Publish option from the Build Menu.
7.  Select either the Prod East or Prod South Publish Profile from the menu.  If you do not currently have those Profiles as seen here, you'll need to download them from Azure and Import them into Visual Studio, first.

![](tmp-release-5-1-dibrg/009.png)

8.  Click Publish.
9.  Verify Publish.
10. Confirm the correct appSettings.json files were deployed via Kudu.  There should only be 2, one named appSettings.json and one named appSettings.Prod.json.
11. Confirm appSettings.Prod.json values:  both BaseUrl and Scope should contain TMP Prod Url, and the AppId should have the correct AppId for the Production Environment.  This value can be found in several locations such as the Integration Settings in TMP and most, if not all, the App Services TMP uses in their respective Configuration Sections.  Use the value from CrmAppId setting for confirmation.  Update the Default Log Level to "ERROR" in the Logging section.
12. Open the web.config file and confirm the EnvironmentName attribute contains "Prod".  This is used by the App Service to determine the correct appSettings.json to use.
13. Update the Log Level in the log4net.config file.  Set the value for the "level" element in the root section to "ERROR" and Save.
14. Repeat Steps 1 thru 9 for the other remaining Region (i.e., East or South).

## Duplicate Patient records bug fix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a deployment to nprod, use the correct Publish Profile to publish.

To deploy the bug fix:

1.  Log into Kudu for either the Prod East or Prod South regions for the HealthShare App Service.  If you don't have the Publish Profile(s) for them you'll need to log into Azure and download them, first.  Use the publishUrl, userName and UserPwd values from the Publish Profile to log into Kudu.
2.  Select the CMD option from the Debug console menu.

![](tmp-release-5-1-dibrg/010.png)

3.  Then click on site link.
4.  Backup the wwwroot folder by clicking the Download button and saving off to your local machine.

![](tmp-release-5-1-dibrg/011.png)

5.  Open Integration Solutions Project in Visual Studio.
6.  Locate the HealthShare API Project in the LOB Api Folder (VA.TMP.Integration.Api.HealthShare).

![](tmp-release-5-1-dibrg/012.png)

7.  Either right-click on the Project and select the Publish option or select the Publish option from the Build Menu.
8.  Select either the Prod East or Prod South Publish Profile from the menu.  If you do not currently have those Profiles as seen here, you'll need to download them from Azure and Import them into Visual Studio, first.

![](tmp-release-5-1-dibrg/013.png)

9.  Click Publish.
10. Repeat Steps 1 thru 9 for the other remaining Region (i.e., East or South).

## Backup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Navigate to the
2.  Select the production environment “VA TMP Prod”.
3.  Create a manual backup as shown below.

![](tmp-release-5-1-dibrg/014.png)

4.  Wait till you see a message like below.

![](tmp-release-5-1-dibrg/015.png)

## Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Navigate to the
2.  Select the production environment “VA TMP Prod”.
3.  Select Restore or manage under “Backups” link.

![](tmp-release-5-1-dibrg/016.png)

4.  Select the backup created in Backup step \#1 -\> Click Restore.

![](tmp-release-5-1-dibrg/017.png)

### From: TMP Version 9.2 Release 4.9.0.14 DIBRG

### Deployment, Installation, Backup, Restore Instructions for TMP Release 9/24/2021

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### From: TMP Version 4.0 Release 4.9.0.8 DIBRG

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Package                   | Minimum Version Needed |
|-------------------------------|----------------------------|
| VA FileMan                    | 22.0                       |
| Kernel                        | 8.0                        |
| MailMan                       | 8.0                        |
| Health Level 7                | 1.6                        |
| Order Entry/Results Reporting | 3.0                        |
| CMOP                          | 2.0                        |
| NDF                           | 4.0                        |
| Outpatient Pharmacy           | 7.0                        |
| Pharmacy Data Management      | 1.0                        |
| Controlled Substances         | 3.0                        |
| Toolkit                       | 7.3                        |
| Drug Accountability           | 3.0                        |

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation from the Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name (ex. SD\*5.3\*780).
2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup, the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
1.  At the Installation option menu, select Backup a Transport Global.
2.  At the Select INSTALL NAME prompt, enter your build SD\*5.3\*780.
3.  When prompted for the following, enter “R” for Routines or “B” for Build.

> Select one of the following:

> B Build

> R Routines

> Enter response: Build

4.  When prompted “Do you wish to secure your build? NO//”, press \<enter\> and take the default response of “NO”.
5.  When prompted with, “Send mail to: Last Name, First Name”, press \<enter\> to take the default recipient. Add any additional recipients.
6.  When prompted with “Select basket to send to: IN//”, press \<enter\> and take the default IN mailbox or select a different mailbox.
3.  You may also elect to use the following options:
1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
1.  When Prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//" respond Yes.
2.  When Prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond NO.
3.  When Prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.
4.  If prompted 'Delay Install (Minutes): (0-60): 0//' respond 0.

## Post-Install Routine (No Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine will execute as a component of the installation. It performs the following functions:  
- Finds the existing future non-clinic days and sends the to TMP  
- Finds the existing future blocked hours and send them to TMP  
- Rebuilds the menu system to activate the menu changes made in the patch

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Section 5.6.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing will be completed by the time patch SD\*5.3\*780 is released.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out criteria will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will be done only with the concurrence and participation of development team and appropriate VA site/region personnel. The decision to back-out or rollback software will be a joint decision between development team, VA site/region personnel and other appropriate VA personnel.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installing an updated KIDS package, the site/region should have saved a backup of the routines in a mail message using the Backup a Transport Global \[XPD BACKUP\] menu option (this is done at time of install). The message containing the backed-up routines can be loaded with the "Xtract PackMan" function at the Message Action prompt. The Packman function "INSTALL/CHECK MESSAGE" is then used to install the backed up routines onto the VistA System.

If the patch was backed up for the build, from the Kernel Installation and Distribution System Menu, select the Installation Menu. Select the Install Package(s) option and choose the patch (xxx\*x.x\*xxxb) to install.

The back-out plan is to restore the routines from the backup created.

No data was modified by this patch installation and, therefore, no rollback strategy is required.

The Back-out Procedure can be verified by printing the first 2 lines of the routine contained in this patch using the option First Line Routine Print \[XU FIRST LINE PRINT\]. Once the routine contained in the SD\*5.3\*780 patch has been backed out, the first two lines of the routine will no longer contain the designation of this patch in the patch.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this patch is available.

| File Description                            | File Name           |
|---------------------------------------------|---------------------|
| Telehealth Management Platform VistA Manual | SD_5_3_P557_UM.docx |
| PIMS Technical Manual                       |                     |

Documentation describing the new functionality is included in this release. Documentation can be found on the VA Software Documentation Library at: <https://www.va.gov/vdl/>.

Documentation can also be obtained at <https://download.vista.med.va.gov/index.html/SOFTWARE>.
