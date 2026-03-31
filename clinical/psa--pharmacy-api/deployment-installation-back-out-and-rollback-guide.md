---
consolidated_title: "drug accountability/inventory interface dibr"
app_code: PSA
doc_type: DIBR
master_source: "Drug Accountability/Inventory Interface Version 3 DIBR (PSA*3*83)"
master_pub_date: December 2021
consolidated_from: 3 versions
prior_versions:
  - "Drug Accountability/Inventory Interface Version 3 DIBR (PSA*3*85)"
  - "Drug Accountability/Inventory Interface Version 3 DIBR (PSA*3*86)"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Drug Accountability Upload 3.0

  Deployment, Installation, Back-Out, and Rollback Guide (DIBR)
---

![](drug-accountability-inventory-interface-version-3-dibr-psa-3-83/001.png)

December 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc88057296" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
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
<td>12/09/2021</td>
<td>1.0</td>
<td><p>PSA*3.0*83:</p>
<ul>
<li><p>Addresses the defects pertaining to failed invoice uploads from McKesson</p></li>
<li><p>The unredacted version of this document is available in the SOFTWARE library for viewing <mark>REDACTED</mark> information</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
</tbody>
</table>

<span id="_Toc88057296" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Guide for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the *Deployment, Installation, Back-out, and Rollback Guide* is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

List of Tables

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
This document describes how to deploy and install the Drug Accountability Upload (DAU) PSA_MCKESSON_UPLOAD.exe Version 3.0.83.1, Veterans Information Systems Technology and Architecture (VistA) informational patch PSA\*3.0\*83, as well as how to back-out the product and rollback to a previous state.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the DAU application will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, and communication methods. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Drug Accountability Upload (DAU) is dependent on a VistA instance to upload data to. PSA\*3.0\*26 and PSA\*3.0\*41 must be installed.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 identifies the technical and support personnel who are involved in the deployment of PSA\*3.0\*83. The VIP Triad (commonly referred to as the three in a box) will meet and approve deployment and installation.

| Team                                                                                                            | Phase / Role    | Tasks                                                                                                               | Project Phase (See Schedule) |
|-----------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|------------------------------|
| Veterans Affairs (VA) Office of Information and Technology (OIT), VA OIT Health Product Support, and developers | Deployment      | Plan and schedule deployment                                                                                        | Planning                     |
| Site personnel in conjunction with local or regional Information Technology (IT) support                        | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment                           | Planning                     |
| Field Testing (Initial Operating Capability (IOC), Health Product Support Testing and VIP Triad                 | Deployment      | Test for operational readiness                                                                                      | Testing                      |
| Health Product Support and Field Operations                                                                     | Deployment      | Execute deployment                                                                                                  | Deployment                   |
| Site personnel in conjunction with local or regional OIT support                                                | Installation    | Plan and schedule installation                                                                                      | Deployment                   |
| Facility Chief Information Officer (CIO) and OIT support, which may be local or regional                        | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                   |
| VA OIT, VA OIT Product Support, and Governent Chief Information Office (GCIO) Development Team                  | Post Deployment | Hardware, Software and System Support                                                                               | Warranty                     |

<span id="_Toc88057297" class="anchor"></span>Table 2: Site Preparation

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard national release in support of the Drug Accountability program.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is considered a mandatory release and installation at the site will be required within the constraints of the compliance period for the release.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the deployment of the PSA_MCKESSON_UPLOAD.exe (which is included in VistA informational patch PSA\*3.0\*83).

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PSA_MCKESSON_UPLOAD.exe graphic user interface (GUI) Version 3.0.83.1 included with PSA\*3.0\*83 is to be nationally released to all Veterans Affairs medical centers (VAMCs) and will be deployed to each requesting client as an executable.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IOC sites are:

- Southern Arizona VA Health Care System (Tucson, AZ)
- St. Cloud VA Medical Center (St. Cloud, MN)

Upon national release all VAMCs will receive PSA\*3.0\*83 VistA Informational Patch, which will contain specific information for the location and retrieval of the executable.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for PSA\*3.0\*83. A fully patched VistA system is the only requirement.

The following table describes preparation required by the site prior to deployment.

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|------------|-----------------------|-----------------------------------------|---------------|-------|
| N/A        |                       |                                         |               |       |

<span id="_Toc88057298" class="anchor"></span>Table 3: Facility-Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site | Space/Room | Features Needed | Other |
|------|------------|-----------------|-------|
| N/A  |            |                 |       |

<span id="_Toc88057299" class="anchor"></span>Table 4: Hardware Specifications

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware      | Model | Version | Configuration | Manufacturer | Other |
|------------------------|-------|---------|---------------|--------------|-------|
| Existing VistA systems |       |         |               |              |       |

<span id="_Toc88057300" class="anchor"></span>Table 5: Software Specifications

Please see the Roles and Responsibilities table in [Section 2](#roles-and-responsibilities) for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software                                      | Make | Version | Configuration | Manufacturer | Other |
|--------------------------------------------------------|------|---------|---------------|--------------|-------|
| Fully patched Drug Accountability Package within VistA |      | 3.0     |               |              |       |

<span id="_Toc88057301" class="anchor"></span>Table 6: Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in [Section 2](#roles-and-responsibilities) above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites that are participating in initial operating capability (IOC) testing will use the Patch Tracking message in Outlook to communicate with the developers and product support personnel.

#### Deployment/Installation/Back-Out Checklist

Table 6 provides a checklist to be used to capture the coordination effort and document the day/time/individual when each activity is completed. The deployment and installation will be performed by on-site support personnel once PSA\*3.0\*83 is nationally released.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

<span id="_Toc88057302" class="anchor"></span>Table 7: Associated Patch Files

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download and extract the executable to an accessible folder. Create a shortcut of the executable, and place it on the user’s desktop.

A fully patched VistA Drug Accountability Package is required.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PSA\*3.0\*83.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PSA\*3.0\*83 patch description will be transmitted as a MailMan message from the National Patch Module (NPM) and this message can be pulled from there. The Zip file contains the executable and can be found, along with the end-user documentation, on the SOFTWARE directory.

https://<span class="mark">REDACTED</span>/SOFTWARE/

Redacted versions of the PSA\*3.0\*83 end-user documentation will be available on the VistA Document Library (VDL).

<https://www.va.gov/vdl/application.asp?appid=87>

| File                        | Description                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------|
| PSA_MCKESSON_UPLOAD_P83.ZIP | Contains the executable                                                                           |
| PSA_MCKESSON_UPLOAD.exe     | PSA\*3.0\*83 GUI Version 3.0.83.1                                                                 |
| PSA_3_P83_DIBR.DOCX         | Microsoft Word version of the Deployment, installation, back-out, roll back guide                 |
| PSA_3_P83_DIBR.PDF          | Portable document format (PDF) version of the Deployment, installation, back-out, roll back guide |
| PSA_3_P83_UM.DOCX           | Microsoft Word version of the User Manual                                                         |
| PSA_3_P83_UM.PDF            | PDF version of the User Manual                                                                    |

Associated Patch FilesThis table shows the list of patch files by file name and description.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to DAU.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to DAU.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to DAU.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff will need access to FORUM’s NPM to view the patch description. Staff will also need access and the ability to download the zip file from the SOFTWARE directory. The executable is to be installed by each site’s or region’s designated VA OIT IT Operations Service, Enterprise Service Lines, or VistA Applications Division.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DAU is a standalone application.

To install the application:

> **NOTE:** For backup purposes, users can retrieve a backup copy of the previous PSA_MCKESSON_UPLOAD.exe Version 3.0.79.7 from the PSA_MCKESSON_UPLOAD_P79.ZIP file located on the SOFTWARE directory.

1.  Extract the PSA_MCKESSON_UPLOAD_P83.ZIP file. Refer to [Section 4.3](#download-and-extract-files) for the Zip file location.
2.  Create a shortcut of the PSA_MCKESSON_UPLOAD.exe Version 3.0.83.1. Set specific server and port information to the target properties. For example:

    C:\\folder location%\PSA_MCKESSON_UPLOAD.exe s=xxx-sup.vha.med.va.gov p=190xxx
3.  Place a copy of the shortcut on the user’s desktop.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Execute the application. Users may be prompted to confirm their Personal Identification Verification (PIV) card by entering their Personal Identification Number (PIN). Upon successful login, the user should be presented with the application option for uploading an invoice. Select an invoice to begin the upload process. The application should return a successful upload message to the user. Login to VistA and verify the invoice has been uploaded.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to DAU.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to DAU.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to returning to the last known good operational state of the software and appropriate settings. Retrieve the backup copy of the PSA_MCKESSON_UPLOAD.exe Version 3.0.79.7 from [Section 4.8](#installation-procedure) and restore the version to the C:\\ drive.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A decision to back out could be made during Site Mirror Testing, during Site Production Testing, or after National Release to the field (VAMCs). The best strategy decision is dependent on the stage of testing during which the decision is made.

If a decision to back out is made after national release and within the designated support period a notification will be disseminated through the NPM in Forum and will list all the necessary steps.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes implemented with PSA_MCKESSON_UPLOAD.exe Version 3.0.83.1 distributed in VistA Informational Patch PSA\*3.0\*83 will be reverted by restoring the executable to the previous version, 3.0.79.7.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to DAU.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing for DAU is performed during the development of the DAU application. Testing will be conducted with a test user.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will be considered if there is a catastrophic failure that causes loss of function for the DAU.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no back-out risks.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to proceed with the back-out and accepts the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DAU is a standalone executable and does not require any special modification for removal. To remove DAU, delete the executable off of the user’s desktop and restore the PSA_MCKESSON_UPLOAD.exe Version 3.0.79.7 in the C:/. Create a new shortcut and copy to the user’s desktop, verify that the Version is 3.0.79.7.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ensure the executable or shortcut on the user’s desktop for Version 3.0.83.1 is removed and PSA_MCKESSON_UPLOAD.exe Version 3.0.79.7 has been restored.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PSA\*3.0\*83.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PSA\*3.0\*83.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PSA\*3.0\*83.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PSA\*3.0\*83.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PSA\*3.0\*83.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PSA\*3.0\*83.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PSA\*3.0\*83.