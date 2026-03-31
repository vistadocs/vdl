---
title: Drug Accountability/Inventory Interface Version 3 Installation Guide (Updated PSA*3*79)
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: (Updated PSA*3*79)
app_code: PSA
app_name: "Pharmacy: Drug Accountability"
section: CLI
app_status: active
pkg_ns: PSA
patch_ver: 3
patch_id: PSA*3
group_key: "PSA:PSA:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - strong
  - back
  - deployment
  - style
  - width
  - installation
  - class
page_count: 0
word_count: 3030
section_count: 28
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Drug_Accountability/PSA_3_P79_IG.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Drug_Accountability/PSA_3_P79_IG.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=87"
---

> Drug Accountability UploadDeployment, Installation, Back-Out, and Rollback Guide

> ![](drug-accountability-inventory-interface-version-3-installation-guide-updated-psa/001.png)

> August 2018 Version 2.0

> Department of Veterans Affairs

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
<td>08/01/2018</td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td><blockquote>
<p>Revised content</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/24/2017</td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>Revised content</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/27/2017</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Additional content</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/1/2017</td>
<td><blockquote>
<p>0.1</p>
</blockquote></td>
<td><blockquote>
<p>Initial draft</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> Artifact Rationale

This document describes the Deployment, Installation, Roll-Back, and Back-Out Guide for new products going into the VA Enterprise. The plan includes information about system support, roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect deployment planning of these procedures for a single location or multiple locations, a single-phase deployment or a multiphase deployment, and should identify the requirements and responsible party for each process step.

The Veteran-focused Integrated Process (VIP) Guide, cites Deployment, Installation, Back-Out, and Rollback Guide is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

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
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the Drug Accountability Upload (DAU) PSA_MCKESSON_UPLOAD.EXE Version 3.0.79 (VistA informational patch PSA\*3\*79, as well as how to back-out the product and rollback to a previous state.

## Purpose 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the DAU application will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, and communication methods. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSA\*3\*26 and PSA\*3\*41 must be installed.

DAU is dependent on a VistA instance available to upload data to.

## Constraints 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 identifies the technical and support personnel who are involved in the deployment of the DAU release. The VIP Triad (commonly referred to as the three in a box) under the Veterans In Process will meet and approve deployment and install from an OI&T perspective.

> Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 15%" />
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
<p><strong>Project</strong></p>
<p><strong>Phase (See</strong></p>
<p><strong>Schedule)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>VA OI&amp;T, VA OI&amp;T Health Product Support, and developers</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Plan and schedule deployment</p>
</blockquote></td>
<td><blockquote>
<p><strong>Planning</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>Site personnel in conjunction with local or regional IT support</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Determine and document the roles and responsibilities of those involved in the deployment.</p>
</blockquote></td>
<td><blockquote>
<p><strong>Planning</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>Field Testing (Initial</p>
<p>Operating Capability</p>
<p>(IOC), Health Product</p>
<p>Support Testing &amp; VIP</p>
<p>TRIAD</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Test for operational readiness</p>
</blockquote></td>
<td><blockquote>
<p><strong>Testing</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>ID</strong></td>
<td><blockquote>
<p><strong>Team</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Phase / Role</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Tasks</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Project</strong></p>
<p><strong>Phase (See</strong></p>
<p><strong>Schedule)</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>Health Product Support and Field Operations.</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Execute deployment</p>
</blockquote></td>
<td><blockquote>
<p><strong>Deployment</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>Site personnel in conjunction with local or regional OI&amp;T support</p>
</blockquote></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td><blockquote>
<p>Plan and schedule installation</p>
</blockquote></td>
<td><blockquote>
<p><strong>Deployment</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>Facility CIO and OI&amp;T support, which may be local or regional</p>
</blockquote></td>
<td><blockquote>
<p>Back-out</p>
</blockquote></td>
<td><blockquote>
<p>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</p>
</blockquote></td>
<td><blockquote>
<p><strong>Deployment</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td><blockquote>
<p>VA OI&amp;T, VA OI&amp;T</p>
<p>Product Support, and</p>
<p>GCIO Development</p>
<p>Team</p>
</blockquote></td>
<td><blockquote>
<p>Post</p>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Hardware, Software and System Support</p>
</blockquote></td>
<td><blockquote>
<p><strong>Warranty</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a Standard National release in support of the Drug Accountability program.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is considered a mandatory release and installation at the site will be required, within the constraints of the compliance period for the release

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the deployment of the PSA_MCKESSON_UPLOAD.EXE (which is included in VistA informational patch PSA\*3\*79).

### Deployment Topology (Targeted Architecture) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PSA_MCKESSON_UPLOAD.EXE GUI Version 3.0.79 (released in PSA\*3\*79 VistA Informational Patch) is to be nationally released to all VAMCs.

The DAU application will be deployed to each requesting client as an executable.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IOC sites are:

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

Upon national release all VAMCs will receive PSA\*3\*79 VistA Informational Patch which will contain specific information for the location and retrieval of the .EXE.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Resources 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to the DAU.

> Table 2: Facility-Specific Features

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 24%" />
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

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment. Table 4: Hardware Specifications

<table>
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
<td><p>Existing</p>
<p>VistA system</p></td>
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

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

> Table 5: Software Specifications

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 15%" />
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
<th><strong>Configuration</strong></th>
<th><blockquote>
<p><strong>Manufacturer</strong></p>
</blockquote></th>
<th><strong>Other</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Fully patched</p>
<p>Drug</p>
<p>Accountability package</p>
<p>within VistA</p></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
<td>N/A</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td>N/A</td>
</tr>
</tbody>
</table>

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Patch Tracking 

The sites that are participating in field testing (IOC) will use the “Patch Tracking” message in Outlook to communicate with the developers and product support personnel.

#### Deployment/Installation/Back-Out Checklist 

Table 6 provides a checklist to be used to capture the coordination effort and document the day/time/individual when each activity is completed. The deployment and installation will be performed by on-site support personnel once the DAU is nationally released.

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
<th>Activity</th>
<th><blockquote>
<p>Day</p>
</blockquote></th>
<th>Time</th>
<th>Individual who completed task</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Install</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Back-Out</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download and extract the EXE to an accessible folder. Create a shortcut of the .EXE, and place it on the user’s desktop.

A fully patched VistA Drug Accountability Package is required.

## Platform Installation and Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None are required.

## Download and Extract Files 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the PSA\*3\*79 Informational VistA Patch to find related documentation that can be downloaded. The patch description will be transmitted as a MailMan message from the National Patch Module (NPM) and this message can be pulled from the NPM. The patch is informational; however, contains information about retrieval of files. The file name is:

PSA_MCKESSON_UPLOAD_P79.ZIP and contains the PSA_MCKESSON_UPLOAD.exe Version 3.0.79. <span class="mark">REDACTED</span>.

Associated documentation will also be available on the VistA Document Library (VDL). The online versions will be updated as needed. Please look for the latest version on the VDL: [*<u>https://www.va.gov/vdl</u>*](https://www.va.gov/vdl)

## Database Creation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to DAU.

## Installation Scripts 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to DAU.

## Cron Scripts 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to DAU.

## Access Requirements and Skills Needed for the Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff will need access to FORUM’s NPM to view the patch description. Staff will also need access and ability to download the host file from one of the VA’s SFTP servers. The executable is to be installed by each site’s or region’s designated VA OI&T IT Operations Service, Enterprise Service Lines, VistA Applications Division.

## Installation Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions may be found in the PSA\*3\*79 Informational VistA Patch found on the FORUM NPM. DAU is a standalone application.

To install the application:

> \*\*\*Note for backup purposes, users can retrieve a backup copy of the previous

> PSA_MCKESSON_UPLOAD.exe Version 3.0.0.41 from the FTP site that is labeled PSA_MCKESSON_UPLOAD_41.ZIP \*\*\*

- Extract the PSA_MCKESSON_UPLOAD_P79.ZIP file.
- Create a shortcut of the PSA_MCKESSON_UPLOAD.EXE Version 3.0.79.Specific server and port information to the target properties. For example:

> C:\\folder location%\PSA_MCKESSON_UPLOAD.exe s=xxx-sup.vha.med.va.gov p=190xxx

- Place a copy of the shortcut on the user’s desktop.
  9.  Installation Verification Procedure

Execute the application and login using your PIV card. Upon successfully login, the user should be presented with application option for uploading an invoice. Select an invoice and press the upload button. The application should return a successfully upload message to the user. Login to VistA and verify the invoice has been uploaded.

10. System Configuration

This section is not applicable to DAU.

11. Database Tuning

This section is not applicable to DAU.

# Back-Out Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known good operational state of the software and appropriate settings. Retrieve the copy of the old PSA_MCKESSON_UPLOAD Version 3.0.0.41 and restore the version to the C:\\

## Back-Out Strategy 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A decision to back out could be made during Site Mirror Testing, during Site Production Testing, or after National Release to the field (VAMCs). The best strategy decision is dependent on the stage of testing during which the decision is made.

If a decision to back out is made after national release and within the designated support period a notification will be disseminated through the NPM in Forum and will list all the necessary steps.

## Back-Out Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes implemented with PSA_MCKESSON_UPLOADEXE Version 3.0.79 distributed in VistA Informational Patch PSA\*3\*79 back-out could be accomplished by restoring the previous .EXE to version 3.0.0.41.

### Load Testing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to DAU.

### User Acceptance Testing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing for DAU is performed during the development of the DAU application. Testing will be conducted with a test user.

## Back-Out Criteria 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will be considered if there is a catastrophic failure that causes loss of function for the DAU.

## Back-Out Risks 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Back-Out 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DAU is a standalone executable and does not require any special modification for removal. To remove DAU, delete the exe off of the user’s desktop and restore the

PSA_MCKESSON_UPLOAD.EXE Version 3.0.0.41 in the C:/. Create a new shortcut and copy to the user’s desktop, verify that the version is 3.0.0.41.

## Back-Out Verification Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ensure the executable or shortcuts on the user’s desktop is removed and

PSA_MCKESSON_UPLOAD.EXE Version 3.0.0.41 has been restored.

# Rollback Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to DAU.

## Rollback Criteria 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to DAU.

## Rollback Risks 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to DAU.

## Authority for Rollback 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to DAU.

## Rollback Verification Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to DAU.