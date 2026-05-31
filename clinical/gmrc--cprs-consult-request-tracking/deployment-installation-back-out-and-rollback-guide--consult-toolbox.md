---
title: Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0056
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: null
app_code: GMRC
app_name: 'CPRS: Consult/Request Tracking'
section: CLI
app_status: archive
pkg_ns: GMRC
patch_ver: 1.9.0056
patch_id: GMRC*1.9.0056
group_key: GMRC:GMRC:1.9.0056
file_numbers: []
security_keys: []
menu_options: 0
description: '> This document describes how to deploy and install the One Consult Toolbox client application, as well as how to back-out the product to a previous version or data set. Deployment and installation of the One Consult Toolbox Care Assessment Need (CAN) Score Application Program Interface (API) applic'
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 1923
section_count: 29
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: December 2019
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking_Archive/ctb_dibr_v1_9_0056.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking_Archive/ctb_dibr_v1_9_0056.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=343
audit_applied: '2026-05-31'
master_source: Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0056
master_pub_date: December 2019
consolidated_from: 7 versions
prior_versions:
- Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0054
- Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0063
- Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0065
- Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0071
- Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0072
- Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0076
consolidated_title: consult toolbox deployment, installation, back-out, and rollback guide
---

# Consult Toolbox Software Version 1.9.0056


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Consult Toolbox Software Version 1.9.0056](#consult-toolbox-software-version-190056)
    - [December 2019 Department of Veterans Affairs](#december-2019-department-of-veterans-affairs)
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
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Procedure](#procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out Action Item](#authority-for-back-out-action-item)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
> Deployment, Installation, Back-Out, and Rollback Guide
![](consult-toolbox-deployment-installation-back-out-and-rollback-guide-v1-9-0056/001.png)

### December 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)
> Revision History
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 22%" />
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
<td>12/17/19</td>
<td>1.6</td>
<td>v1.9.0056 Initial Update</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11/21/19</td>
<td>1.5</td>
<td>v1.9.0054 Final Update</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10/02/19</td>
<td>1.4</td>
<td>v1.9.0052 Final Update</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/20/19</td>
<td>1.3</td>
<td>v1.9.0050 Initial Update</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>05/03/19</td>
<td>1.2</td>
<td>v1.9.0004 Final Update</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>02/25/19</td>
<td>1.1</td>
<td>v1.9.0004 Initial Update</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/21/18</td>
<td>1.0</td>
<td>v1.9.02b Update pre-installation</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12/14/18</td>
<td>0.9</td>
<td>v1.9.02a Remediation Updates</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>09/26/18</td>
<td>0.8</td>
<td>v1.9.02 Remediation Updates</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/08/18</td>
<td>0.7</td>
<td>v1.8.02 Release</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>06/29/18</td>
<td>0.6</td>
<td>Response to Comments</td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>03/01/18</td>
<td>0.5</td>
<td>v1.8.01 Release</td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/01/17</td>
<td>0.4</td>
<td>v1.7.01 Release</td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/12/17</td>
<td>0.3</td>
<td>v1.0.6051 Release</td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>08/01/17</td>
<td>0.2</td>
<td>v1.0.6 Release</td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>05/01/17</td>
<td>0.1</td>
<td>Initial Creation</td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
</tbody>
</table>
> Artifact Rationale
> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.
> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes how to deploy and install the One Consult Toolbox client application, as well as how to back-out the product to a previous version or data set. Deployment and installation of the One Consult Toolbox Care Assessment Need (CAN) Score Application Program Interface (API) application is covered in a feature specific guide. This document is a companion to the project charter and management plan for this effort. In cases where a non- developed Commercial-Off-The-Shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the One Consult Toolbox will be deployed and installed, as well as how it is to be backed out, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

> This document describes the content and functionality of the Consult Toolbox installation build created by Enterprise Systems Engineering (ESE), Client Services, and Desktop Technologies.

> Consult toolbox is an AutoHotkey based application that provides standardized processes and procedures for documenting consults.

> Consult Toolbox runs on the following operating systems.

- Windows 7, 64-bit
- Windows 10, 64-bit

> The table below shows the prerequisites for Consult Toolbox. If these applications are not present on the target computer, the Consult Toolbox setup or the application will fail.

> <span id="_bookmark2" class="anchor"></span>Table 1: Prerequisites

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 33%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Product Name</strong></th>
<th><strong>Product Version</strong></th>
<th><strong>How to Check Whether it is Installed</strong></th>
<th><blockquote>
<p><strong>Link for Package Build Document</strong></p>
</blockquote></th>
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

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark4" class="anchor"></span>Table 2: Dependencies

| Release Dependency        | Description  | Status of Dependency | Notes or Concerns (availability, funding, resources, etc.) |
|-------------------------------|------------------|--------------------------|----------------------------------------------------------------|
| Field Implementation Services | Deployment       | Active                   | Upstream                                                       |
| Desktop                       | National Package | Active                   | Upstream                                                       |

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – No Constraints regarding physical environment.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark7" class="anchor"></span>Table 3: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                                                | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|---------------------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
|        | Enterprise Systems Engineering Desktop Technology (ESE) | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                 |                                  |
|        | ESE                                                     | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          |                                  |
|        | Enterprise Service Line Client Technology (ESL)         | Deployment       | Test for operational readiness                                                                                      |                                  |
|        | ESE/ESL                                                 | Deployment       | Execute deployment                                                                                                  |                                  |
|        | ESE/ESL                                                 | Installation     | Plan and schedule installation                                                                                      |                                  |
|        | To Be Determined                                        | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                       |                                  |
|        | Not Applicable                                          | Installation     | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         | No inventory being used          |
|        | Clinical Application                                    | Installations    | Coordinate training                                                                                                 | Application Use Only             |
|        | ESE                                                     | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |                                  |
|        | AbleVets/Config Mgmt                                    | Post Deployment  | Hardware, Software and System Support                                                                               |                                  |

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment is planned as a simultaneous rollout.

> This section provides the schedule and milestones for the deployment.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment and installation is scheduled to run for 15 days, as depicted in the master deployment schedule December 5, 2019 to December 20, 2019.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the One Consult Toolbox deployment. Toolbox is being deployed to all Clinical facilities.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Consult Toolbox will be deployed to all Clinical Workstations.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Consult Toolbox will be deployed to all Clinical Workstations.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes preparation required by the site prior to deployment.

> <span id="_bookmark14" class="anchor"></span>Table 4: Site Preparation

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
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Field Implementation Services

1.  <span id="3.3.1_Facility_Specifics_(optional)" class="anchor"></span>Facility Specifics *(optional)*

> The following table lists facility-specific features required for deployment.

> <span id="_bookmark17" class="anchor"></span>Table 5: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes hardware specifications required at each site prior to deployment.

> <span id="_bookmark19" class="anchor"></span>Table 6: Hardware Specifications

<table style="width:100%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Hardware</strong></th>
<th><blockquote>
<p><strong>Model</strong></p>
</blockquote></th>
<th><strong>Version</strong></th>
<th><strong>Configuration</strong></th>
<th><strong>Manufacturer</strong></th>
<th><strong>Other</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

> Please see the table in the Roles and Responsibilities section of this document for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes software specifications required at each site prior to deployment.

> <span id="_bookmark21" class="anchor"></span>Table 7: Software Specifications

<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Software</strong></th>
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
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Please see the table in the Roles and Responsibilities section of this document for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Deployment/Installation/Back-Out Checklist

> <span id="_bookmark24" class="anchor"></span>Table 8: Deployment/Installation/Back-Out Checklist

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 25%" />
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
<td>Deploy (planned)</td>
<td>1/13/2019</td>
<td><blockquote>
<p>12:00 AM</p>
</blockquote></td>
<td><blockquote>
<p>Field Implementation Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Install (planned)</td>
<td><blockquote>
<p>1/13/2019</p>
</blockquote></td>
<td><blockquote>
<p>12:00 AM</p>
</blockquote></td>
<td><blockquote>
<p>Field Implementation Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Back-Out</td>
<td>TBD</td>
<td><blockquote>
<p>12:00 AM</p>
</blockquote></td>
<td><blockquote>
<p>Field Implementation Services</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Consult Toolbox runs on the following operating systems.

- Windows 7, 64-bit
- Windows 10, 64-bit
- Log Files:
  - %ALLUSERSPROFILE%\DeptOfVeteransAffairs\Logs\VA_ConsultToolbox_1.

> 9.0056.log

- %ALLUSERSPROFILE%\DeptOfVeteransAffairs\Logs\VA_ConsultToolbox_ini

> \_File_Copy.log

- Uninstall any prior version of Consult Toolbox
- Remove all files from the folder %AppData%\ConsultToolbox

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Platform Installation or Preparation required.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For manual installations, execute the following steps in order.

1.  Use dBAT for manual Install.
2.  dBAT website is here for more information and help files.
3.  Once connected to the workstation select the Baseline or Tier 3/4 tab.
4.  Find Consult Toolbox and check the check box next to application name and press

> Install/Uninstall button to initiate installation.

> The Consult Toolbox installation package can be found on the CM central site at the following locations.

> Package Name

> 1VA - VA ConsultToolbox 1.9.0056 *(to be verified with build guide)*

> Application ID N/A

> Package Size

> 3.0 MB

> CM Application Source

> \\ \Software Packages\VA\ConsultToolbox\1.9.0056 *(to be verified with build guide)*

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Cron script required for software installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For manual installations, execute the following steps in order.

1.  Use dBAT for manual Install.
2.  dBAT website is here for more information and help files.
3.  Once connected to the workstation select the Baseline or Tier 3/4 tab.
4.  Find Consult Toolbox and check the check box next to application name and press

> Install/Uninstall button to initiate installation.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For manual installations, execute the following steps in order.

5.  Use dBAT for manual Install.

> dBAT website is here for more information and help files.

6.  Once connected to the workstation select the Baseline or Tier 3/4 tab.
7.  Find Consult Toolbox and check the check box next to application name and press

> Install/Uninstall button to initiate installation.

## Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you experience any issues with this package installation, please follow the procedures found in the [<u>Package Installation Issues Procedures</u>](http://vaww.eie.va.gov/SysDesign/CS/Shared%20Documents/Help/SD%20DDE%20Package%20Installation%20Issues%20Procedures.pdf).

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no system configuration instructions required.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no database tuning information or tips required.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow local established procedures for Un-installing the application or patch that is causing problems, either manually, dBAT or via SCCM. Run back out command line as documented in the build document found by accessing the 'Portal Entry' link from the attachments tab of this change order. From there, follow the link 'Build Document'.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The back-out strategy will follow VA guidelines and best practices as referenced in the Enterprise Operations (EO) National Data Center Hosting Services document.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Back-Out Considerations required.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Load Testing required.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no User Acceptance Testing required.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Back-Out Criteria required.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Back-Out Risks associated.

## Authority for Back-Out Action Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Dr. Clinton Greenstone, Product Owner.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Execute the following steps to uninstall the full Consult Toolbox application.

1.  Launch dBAT.exe and connect to workstation listed in Manual Installation.
2.  In Workstation Detail View and select the Programs & Features tab.
3.  Find Consult Toolbox and check the check box next to application name and press

> Install/Uninstall button to initiate uninstall if installed.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Execute the following steps to uninstall the full Consult Toolbox application.

1.  Launch dBAT.exe and connect to workstation listed in Manual Installation.
2.  In Workstation Detail View and select the Programs & Features tab.
3.  Find Consult Toolbox and check the check box next to application name and press

> Install/Uninstall button to initiate uninstall if installed.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow local established procedures for Un-installing the application or patch that is causing problems, either manually, dBAT or via SCCM. Run back out command line as documented in the build document found by accessing the 'Portal Entry' link from the attachments tab of this change order. From there, follow the link 'Build Document'.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Rollback Considerations required.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Rollback criteria required.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Rollback Risks associated.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Rollback Authority required.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Rollback Procedure required.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not Applicable – no Rollback Verification Procedure required.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0063

### April 2020 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OIT)
> Revision History
| Date   | Version | Description                  | Author |
|------------|-------------|----------------------------------|------------|
| 04/14/2020 | 1.9         | v1.9.0063 Initial Update         | AbleVets   |
| 04/01/2020 | 1.8         | v1.9.0062 Initial Update         | AbleVets   |
| 02/03/2020 | 1.7         | v1.9.0061 Initial Update         | AbleVets   |
| 12/17/2019 | 1.6         | v1.9.0056 Initial Update         | AbleVets   |
| 11/21/2019 | 1.5         | v1.9.0054 Final Update           | AbleVets   |
| 10/02/2019 | 1.4         | v1.9.0052 Final Update           | AbleVets   |
| 08/20/2019 | 1.3         | v1.9.0050 Initial Update         | AbleVets   |
| 05/03/2019 | 1.2         | v1.9.0004 Final Update           | AbleVets   |
| 02/25/2019 | 1.1         | v1.9.0004 Initial Update         | AbleVets   |
| 12/21/2018 | 1.0         | v1.9.02b Update pre-installation | AbleVets   |
| 12/14/2018 | 0.9         | v1.9.02a Remediation Updates     | AbleVets   |
| 09/26/2018 | 0.8         | v1.9.02 Remediation Updates      | AbleVets   |
| 08/08/2018 | 0.7         | v1.8.02 Release                  | AbleVets   |
| 06/29/2018 | 0.6         | Response to Comments             | AbleVets   |
| 03/01/2018 | 0.5         | v1.8.01 Release                  | CC IT PMO  |
| 12/01/2017 | 0.4         | v1.7.01 Release                  | CC IT PMO  |
| 10/12/2017 | 0.3         | v1.0.6051 Release                | CC IT PMO  |
| 08/01/2017 | 0.2         | v1.0.6 Release                   | CC IT PMO  |
| 05/01/2017 | 0.1         | Initial Creation                 | CC IT PMO  |
> Artifact Rationale
> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.
> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

### From: Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0071

### June 2020 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OIT)
> Revision History
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 22%" />
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
<td>06/11/2020</td>
<td>1.10</td>
<td><blockquote>
<p>v1.9.0071 Final Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>05/19/2020</td>
<td>1.9</td>
<td><blockquote>
<p>v1.9.0071 Initial Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>04/01/2020</td>
<td>1.8</td>
<td><blockquote>
<p>v1.9.0062 Initial Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>02/03/2020</td>
<td>1.7</td>
<td><blockquote>
<p>v1.9.0061 Initial Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/17/2019</td>
<td>1.6</td>
<td><blockquote>
<p>v1.9.0056 Initial Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11/21/2019</td>
<td>1.5</td>
<td><blockquote>
<p>v1.9.0054 Final Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10/02/2019</td>
<td>1.4</td>
<td><blockquote>
<p>v1.9.0052 Final Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/20/2019</td>
<td>1.3</td>
<td><blockquote>
<p>v1.9.0050 Initial Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>05/03/2019</td>
<td>1.2</td>
<td><blockquote>
<p>v1.9.0004 Final Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>02/25/2019</td>
<td>1.1</td>
<td><blockquote>
<p>v1.9.0004 Initial Update</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/21/2018</td>
<td>1.0</td>
<td><blockquote>
<p>v1.9.02b Update pre-installation</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12/14/2018</td>
<td>0.9</td>
<td><blockquote>
<p>v1.9.02a Remediation Updates</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>09/26/2018</td>
<td>0.8</td>
<td><blockquote>
<p>v1.9.02 Remediation Updates</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/08/2018</td>
<td>0.7</td>
<td><blockquote>
<p>v1.8.02 Release</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>06/29/2018</td>
<td>0.6</td>
<td><blockquote>
<p>Response to Comments</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>03/01/2018</td>
<td>0.5</td>
<td><blockquote>
<p>v1.8.01 Release</p>
</blockquote></td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/01/2017</td>
<td>0.4</td>
<td><blockquote>
<p>v1.7.01 Release</p>
</blockquote></td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/12/2017</td>
<td>0.3</td>
<td><blockquote>
<p>v1.0.6051 Release</p>
</blockquote></td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>08/01/2017</td>
<td>0.2</td>
<td><blockquote>
<p>v1.0.6 Release</p>
</blockquote></td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>05/01/2017</td>
<td>0.1</td>
<td><blockquote>
<p>Initial Creation</p>
</blockquote></td>
<td><blockquote>
<p>CC IT PMO</p>
</blockquote></td>
</tr>
</tbody>
</table>

### From: Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0072

### July 2020 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OIT)
> Revision History
| Date   | Version | Description                  | Author |
|------------|-------------|----------------------------------|------------|
| 07/10/2020 | 1.11        | v1.9.0072 Final Update           | AbleVets   |
| 06/11/2020 | 1.10        | v1.9.0071 Final Update           | AbleVets   |
| 05/19/2020 | 1.9         | v1.9.0071 Initial Update         | AbleVets   |
| 04/01/2020 | 1.8         | v1.9.0062 Initial Update         | AbleVets   |
| 02/03/2020 | 1.7         | v1.9.0061 Initial Update         | AbleVets   |
| 12/17/2019 | 1.6         | v1.9.0056 Initial Update         | AbleVets   |
| 11/21/2019 | 1.5         | v1.9.0054 Final Update           | AbleVets   |
| 10/02/2019 | 1.4         | v1.9.0052 Final Update           | AbleVets   |
| 08/20/2019 | 1.3         | v1.9.0050 Initial Update         | AbleVets   |
| 05/03/2019 | 1.2         | v1.9.0004 Final Update           | AbleVets   |
| 02/25/2019 | 1.1         | v1.9.0004 Initial Update         | AbleVets   |
| 12/21/2018 | 1.0         | v1.9.02b Update pre-installation | AbleVets   |
| 12/14/2018 | 0.9         | v1.9.02a Remediation Updates     | AbleVets   |
| 09/26/2018 | 0.8         | v1.9.02 Remediation Updates      | AbleVets   |
| 08/08/2018 | 0.7         | v1.8.02 Release                  | AbleVets   |
| 06/29/2018 | 0.6         | Response to Comments             | AbleVets   |
| 03/01/2018 | 0.5         | v1.8.01 Release                  | CC IT PMO  |
| 12/01/2017 | 0.4         | v1.7.01 Release                  | CC IT PMO  |
| 10/12/2017 | 0.3         | v1.0.6051 Release                | CC IT PMO  |
| 08/01/2017 | 0.2         | v1.0.6 Release                   | CC IT PMO  |
| 05/01/2017 | 0.1         | Initial Creation                 | CC IT PMO  |
