---
title: VistA Package Size Reporting Tool (VPSRT) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG) (XT*7.3*143)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: 
app_code: XT
app_name: Kernel Toolkit
section: INF
app_status: active
pkg_ns: XT
patch_ver: 7.3
patch_id: XT*7.3
group_key: "XT:XT:7.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - patch
  - xtvs
  - vista
  - installation
  - back
  - kernel
  - package
  - deployment
page_count: 0
word_count: 5599
section_count: 37
table_count: 6
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2021
revision_count: 1
revision_newest: 04/19/2021
revision_oldest: 04/19/2021
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Toolkit/xtvs_vpsrt_dibrg_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Toolkit/xtvs_vpsrt_dibrg_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=12"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>VistA Package Size Reporting Tool (VPSRT)

  Kernel Toolkit Patch XT\*7.3\*143

  Deployment, Installation, Back-Out, and Rollback Guide (DIBRG) (REDACTED)
---

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/001.png)

April 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

VistA Infrastructure (VI)

<span id="revision_history" class="anchor"></span>Revision History

| Date       | Revision | Description                                                                                                                                                                       | Author                                                                        |
|------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 04/19/2021 | 1.0      | Initial *VistA Package Size Reporting Tool (VPSRT) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)* based on the VIP template Version 2.2, released on March 2016. | VistA Infrastructure (VI) / VistA Kernel Development Team: Patch XU\*8.0\*143 |

<span id="_Ref473643111" class="anchor"></span>Table 1: Roles and Responsibilities

Table of Contents

<span id="_Toc69115389" class="anchor"></span>List of Figures

<span id="_Toc69115390" class="anchor"></span>List of Tables

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
    - [Load and Install KIDS File](#load-and-install-kids-file)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
    - [Allocate XTVS EDITOR Security Key](#allocate-xtvs-editor-security-key)
    - [Review Configure XTVS PKG EXTRACT SERVER Option Configuration](#review-configure-xtvs-pkg-extract-server-option-configuration)
    - [Set Default Directory](#set-default-directory)
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
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Appendix A—Possible Installation Report Errors](#appendix-apossible-installation-report-errors)
  - [Package File Extract Not Included in Patch Distribution](#package-file-extract-not-included-in-patch-distribution)
  - [Package File Extract Data Stored in ^XTMP](#package-file-extract-data-stored-in-xtmp)
  - [Failure to Load Package File Extract into a PackMan Message](#failure-to-load-package-file-extract-into-a-packman-message)
  - [PARAMETER TEMPLATE File Entry Failure](#parameter-template-file-entry-failure)
  - [PARAMETER TEMPLATE Parameters Sub-file Entry Failure](#parameter-template-parameters-sub-file-entry-failure)
  - [Patch Previously Installed](#patch-previously-installed)
This document describes how to deploy and install the VistA Package Size Reporting Tool (VPSRT) released with Kernel Toolkit Patch XT\*7.3\*143*,* as well as how to back out the product and roll back to a previous version or data set. This software will be installed on FORUM and all VistA instances to provide support staff with a package configuration check tool.
This document includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the VPS software.
![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/002.png) NOTE: Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the VPS software will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists and describes all application, system, financial, and other dependencies for this deployment, including upstream processing.

Kernel Toolkit Patch XT\*7.3\*143 does *not* have any other patch dependencies.

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/003.png) REF: For a list of minimum software requirements, see <u>Table 5</u>.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the target physical environment for deployment. The Kernel security controls are operationally capable within full implementation of National Institute of Standards and Technology (NIST) controls. It is in compliance with Directive 6500, Section 508 compliance, and performance impacts of the deployment environment.

There are no constraints for Kernel Toolkit Patch XT\*7.3\*143 release other than the operating system and software dependencies described in Section <u>3.3.2</u>, “<u>Software</u>.”

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the teams that will perform the steps described in this guide.

<u>Table 1</u> identifies the technical and support personnel who are involved in the deployment, installation, back-out, and rollback of the Veterans Health Information Systems and Technology Architecture (VistA) Kernel Toolkit Patch XT\*7.3\*143 release.

<table>
<caption><p><span id="_Toc23255471" class="anchor"></span>Table 2: Deployment Timeline</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 36%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>ID</th>
<th>Team</th>
<th>Phase / Role</th>
<th>Tasks</th>
<th>Project Phase (See Schedule)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Enterprise Program Management Office (EPMO) Implementation Team</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors).</td>
<td>Planning</td>
</tr>
<tr class="even">
<td>2</td>
<td>EPMO Implementation Team</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
<td>Planning</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Software Quality Assurance (SQA)</td>
<td>Deployment</td>
<td>Test for operational readiness.</td>
<td>Build</td>
</tr>
<tr class="even">
<td>4</td>
<td>Product Support (PS)</td>
<td>Deployment</td>
<td>Execute deployment.</td>
<td>Release Prep Phase</td>
</tr>
<tr class="odd">
<td>5</td>
<td>EPMO Implementation Team</td>
<td>Installation</td>
<td>Plan and schedule installation.</td>
<td>Build Phase</td>
</tr>
<tr class="even">
<td>6</td>
<td>EPMO Implementation Team</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place.</td>
<td>Release Prep Phase</td>
</tr>
<tr class="odd">
<td>8</td>
<td>EPMO Implementation Team<br />
VistA Infrastructure (VI) Development Team</td>
<td>Installations</td>
<td>Coordinate training.</td>
<td>Release Prep Phase</td>
</tr>
<tr class="even">
<td>9</td>
<td>EPMO Implementation Team<br />
VistA Infrastructure (VI) Development Team</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).</td>
<td>Build Phase</td>
</tr>
<tr class="odd">
<td>10</td>
<td>SDE Field Operations (FO)<br />
Enterprise Operations (EO)</td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support.</td>
<td>Post Release</td>
</tr>
</tbody>
</table>

<span id="_Toc23255471" class="anchor"></span>Table 2: Deployment Timeline

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the schedule and milestones for the Kernel Toolkit Patch XT\*7.3\*143 deployment.

Kernel Toolkit Patch XT\*7.3\*143 deployment is planned as a simultaneous rollout. National release date is scheduled for the week of 04/20/2021.

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/004.png) NOTE: This is just a *proposed* National release date. Other *proposed* dates include:

- Software Quality Assurance (SQA) review from 10/5/2020 through 3/26/2021
- Initial Operating Capabilities (IOC) site testing would run from 11/06/2020 through 3/26/2021.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*143 deployment and installation is scheduled to run for 30 days from release, which is the typical Veterans Health Information Systems and Technology Architecture (VistA) national patch rollout schedule.

| Deployment                                                                    | Start                  | Finish                 |
|-------------------------------------------------------------------------------|------------------------|------------------------|
| Patch Development and Debug Phase                                             | 10/05/2018             | 10/02/2020             |
| Documentation and Software Quality Assurance (SQA)                            | 10/05/2020             | 03/26/2021             |
| Health Product Support (HPS) and Initial Operating Capabilities (IOC) Testing | 12/14/2020             | 03/26/2021             |
| FORUM and National Release: Site Installation and Deployment                  | 04/20/2021 (projected) | 04/24/2021 (projected) |
| Warranty                                                                      | 04/25/2021 (projected) | 05/25/2021 (projected) |
| Sustainment                                                                   | 05/26/2020 (projected) | Ongoing                |

<span id="_Ref473643192" class="anchor"></span>Table 3: Site Preparation

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Site Readiness Assessment for the locations that will receive Kernel Toolkit Patch XT\*7.3\*143 deployment. This will be a national release of a VistA patch for FORUM and all VistA Production sites.

Topology determinations are made by Enterprise Systems Engineering (ESE) and vetted by Enterprise Service Line (ESL), Field Office (FO), National Data Center Program (NDCP), and Austin Information Technology Center (AITC) during the design phase as appropriate. Field site coordination is done by ESL unless otherwise stipulated by ESL.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the deployment topology (local sites, etc.) for Kernel Toolkit Patch XT\*7.3\*143.

Kernel Toolkit Patch XT\*7.3\*143 will be distributed to FORUM and local and regional system administrators and support personnel responsible for each of the 130 VistA parent systems. The VistA M Server code will be available to developers from the Product Support (PS) Anonymous Directories.

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/005.png) NOTE: The code will be available to developers from secure file transfer \[SFTP) sites listed in the patch description.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*143 VistA M Server code is directly deployed to FORUM and all VA sites following the standard deployment procedure used for all VistA patches.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the preparation required for the site at which the system will operate.

There are no special site preparations or changes that *must* occur to the operational site and no specific features or items that need to be modified to adapt to Kernel Toolkit Patch XT\*7.3\*143.

As a precursor to Kernel Toolkit Patch XT\*7.3\*143 deployment, the Kernel documentation set (including this Deployment, Installation, Back-Out, and Rollback Guide \[DIBRG\]) will be added to the [Kernel Toolkit application on the VA Software Document Library (VDL)](https://www.va.gov/vdl/application.asp?appid=12).

<u>Table 3</u> describes preparation required by the site prior to deployment.

| Site/Other           | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------------|-----------------------|-----------------------------------------|---------------|-------|
| Not Applicable (N/A) | N/A                   | N/A                                     | N/A           | N/A   |

<span id="_Ref470091986" class="anchor"></span>Table 4: Hardware Specifications

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the hardware, software, facilities, documentation, and any other resources, other than personnel, required for the deployment and installation of Kernel Toolkit Patch XT\*7.3\*143.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific hardware requirements for installation of Kernel Toolkit Patch XT\*7.3\*143 as it runs in a typical VistA M Server environment. There is also no need for specific hardware to assist in the deployment of Kernel Toolkit Patch XT\*7.3\*143.

<u>Table 4</u> describes hardware specifications required at each site prior to deployment of Kernel Toolkit Patch XT\*7.3\*143.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-------------------|-------|---------|---------------|--------------|-------|
| N/A               | N/A   | N/A     | N/A           | N/A          | N/A   |

<span id="_Ref373317182" class="anchor"></span>Table 5: VistA M Server—Minimum Software Requirements

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/006.png) REF: For details about who is responsible for preparing the site to meet these hardware specifications, see <u>Table 1</u>.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of Kernel Toolkit Patch XT\*7.3\*143 is a typical Kernel Installation & Distribution System (KIDS) install of a VistA patch in the VistA M Server environment.

<u>Table 5</u> lists the *minimum* software requirements for the VistA M Server in order to install and use Kernel Toolkit Patch XT\*7.3\*143:

| Software       | Version | Description                                                                             |
|----------------|---------|-----------------------------------------------------------------------------------------|
| Kernel         | 8.0     | VistA Legacy Software [<sup>\*</sup>Fully Patched M Accounts](#fully_patched_note). |
| Kernel Toolkit | 7.3     | VistA Legacy Software [<sup>\*</sup>Fully Patched M Accounts](#fully_patched_note). |
| VA FileMan     | 22.2    | VistA Legacy Software [<sup>\*</sup>Fully Patched M Accounts](#fully_patched_note). |
| MailMan        | 8.0     | VistA Legacy Software [<sup>\*</sup>Fully Patched M Accounts](#fully_patched_note). |

<span id="_Ref473643112" class="anchor"></span>Table 6: Deployment/Installation/Back-Out Checklist

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/007.png) <span id="fully_patched_note" class="anchor"></span><sup>\*</sup>NOTE: All software listed in <u>Table 5</u> *must* be fully patched, which means that all patches *must* be installed up to the most recent patch released at the time of the installation of Kernel Toolkit Patch XT\*7.3\*143.

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/008.png) REF: For details about who is responsible for preparing the site to meet these software specifications, see <u>Table 1</u>.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes any notifications activities and how they will occur.

Prior to the deployment of Kernel Toolkit Patch XT\*7.3\*143, a product announcement will be sent via email to current Points of Contact (POC) on record for each site describing the product and a brief description of the deployment and post-deployment support. Included will be links to the Kernel Toolkit 7.3 VA Software Document Library (VDL) and Rational repositories, which contain further information about the release and the deployment, including the deployment schedule and required pre-installation activities.

Kernel Toolkit Patch XT\*7.3\*143 Implementation Team will respond to email requests for assistance and further information and, where appropriate, re-direct these requests to specialist technical staff.

#### Deployment/Installation/Back-Out Checklist

Tracking of installation for VistA Kernel patches is monitored in FORUM.

<u>Table 6</u> provides a checklist to be used to capture the coordination effort and document the day/time/individual when each activity (deploy, install, back-out) is completed for standard Kernel Toolkit 7.3 patch releases.

| Activity                                     | Day | Time | Individual who completed task |
|----------------------------------------------|-----|------|-------------------------------|
| Deploy                                       |     |      |                               |
| Install Patch XT\*7.3\*143 on VistA M Server |     |      |                               |
| Back-Out                                     |     |      |                               |

<span id="_Ref373317540" class="anchor"></span>Table 7: Patch XT\*7.3\*143—VistA M Server Distribution Files

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the minimum requirements for the product to be installed.

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/009.png) REF: For a list of the minimum hardware and software requirements, including platform, Operating System (OS), and storage requirements required for Kernel Toolkit Patch XT\*7.3\*143, see the following:

- Section <u>3.3.1</u>, “<u>Hardware</u>”
- Section <u>3.3.2</u>, “<u>Software</u>”

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*143 should be installed on FORUM and all VistA M Servers.

All VistA Infrastructure patches *must* be installed within 30 days of national release.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 7</u> lists the Kernel Toolkit Patch XT\*7.3\*143 distribution files related to the patch installation:

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 10%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>xt_7_3_143.pd</strong></td>
<td>ASCII</td>
<td><p><strong>Patch Description (PD)</strong>. This provides any pre-installation instructions, instructions, and additional information to install the patch.</p>
<p>Follow all patch installation instructions.</p></td>
</tr>
<tr class="even">
<td><strong>xt_7_3_dibrg.pdf</strong></td>
<td>Binary</td>
<td><strong>Installation Guide</strong> (manual). Use this manual in conjunction with the Patch Description document on FORUM and any additional Readme text files.</td>
</tr>
</tbody>
</table>

All Kernel software can be downloaded from the Product Support (PS) Anonymous Directories. Also, all Kernel documentation is available in Adobe<sup>®</sup> Acrobat PDF format and can be downloaded from the [Kernel Toolkit application on the VA Software Document Library (VDL)](https://www.va.gov/vdl/application.asp?appid=12).

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/010.png) NOTE: For all patches, first read the patch installation instructions in the patch description located in National Patch Module (NPM) on FORUM.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is *not* applicable (N/A). Kernel Toolkit Patch XT\*7.3\*143 does *not* create any required databases. It uses the already installed VA FileMan database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is *not* applicable (N/A). Kernel Toolkit Patch XT\*7.3\*143 does *not* create any separate installation scripts. It is a typical VistA installation that uses Kernel Installation & Distribution System (KIDS) to install the patch.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is *not* applicable (N/A). Kernel Toolkit Patch XT\*7.3\*143 does *not* provide any cron scripts[^1].

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General skills required to perform the Kernel Toolkit Patch XT\*7.3\*143 installation are listed below:

- Back up the system  
    
  *\[VistA M Server\]*
- Copy files using commands  
    
  *\[VistA M Server\]*
- Run a Kernel Installation & Distribution System (KIDS) installation  
  *  
  \[VistA M Server\]*

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/011.png) REF: Instructions for performing these functions are provided in vendor-supplied operating system manuals as well as other VA and VistA publications.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install Kernel Toolkit Patch XT\*7.3\*143 from the VistA MailMan message per directions in the Kernel Toolkit Patch XT\*7.3\*143 Patch Description (PD) document located on FORUM.

### Load and Install KIDS File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Load and install the following Kernel Installation & Distribution System (KIDS) file:

XT_7_3_143.KID

1.  Follow the install prompts.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the installation of Kernel Toolkit Patch XT\*7.3\*143 on the VistA M Server, perform the following procedure:

1.  Verify the installation using the KIDS Install File Print \[XPD PRINT INSTALL FILE\] option, located under the Utilities \[XPD UTILITY\] menu.
1.  At the “Select INSTALL NAME:” prompt, enter XT\*7.3\*143.
2.  Confirm that the STATUS field is “Install Completed”, as shown in <u>Figure 1</u>:

> <span id="_Ref479168911" class="anchor"></span>Figure 1: Verify the Kernel Toolkit Patch XT\*7.3\*143 Installation was Completed on the VistA M Server (Excerpt)

Select Utilities Option: <span class="mark">INSTALL FILE PRINT</span>

Select INSTALL NAME: <span class="mark">XT\*7.3\*143 \<Enter\></span> <span class="mark">Install Completed</span> 10/30/19@08:10:34

=\> XT\*7.3\*143 TEST v1

DEVICE: HOME// <span class="mark">\<Enter\></span>

PACKAGE: XT\*7.3\*143 Oct 30, 2019 8:10 am PAGE 1

COMPLETED ELAPSED

----------------------------------------------------------------------------

STATUS: <span class="mark">Install Completed</span> DATE LOADED: OCT 30, 2019@08:09:32

INSTALLED BY: XUUSER,ONE

NATIONAL PACKAGE: KERNEL

INSTALL STARTED: OCT 30, 2019@08:10:34 08:10:34

ROUTINES: 08:10:34

…

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/012.png) REF: For a list of possible installation report errors, see “<u>Appendix A—Possible Installation Report Errors</u>.”

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Allocate XTVS EDITOR Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Allocation of Security Keys \[XUKEYALL\] option to allocate the XTVS EDITOR security key to the users who manage package parameters used to create the package size reports. Users that only need to create package size reports do *not* need this security key.

To allocate the XTVS EDITOR security key, do the following:

1.  Select the System Manager Menu \[EVE\].
2.  Select the Menu Management \[XUMAINT\] menu.
3.  Select the Key Management \[XUKEYMGMT\] menu.
4.  Select the Allocation of Security Keys \[XUKEYALL\] option.
5.  At the “Allocate key:” prompt enter XTVS EDITOR.

### Review Configure XTVS PKG EXTRACT SERVER Option Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Process XTVS Request Message \[XTVS PKG EXTRACT SERVER\] option responds to remote VistA requests to return size reports; and on FORUM, PACKAGE (#9.4) file extracts. System administrators can decide to prevent a remote user from running a report on the VistA and returning it to the requester. This option can help remote support staff assist the site.

The SERVER ACTION (#221) field in the OPTION (#19) file is set to “RUN IMMEDIATELY” for the XTVS PKG EXTRACT SERVER option when the patch is installed. Configuration of this option allows remote support staff to receive requested size messages (or in the case of FORUM, PACKAGE \[#9.4\] file extract messages in addition to package size messages).

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/013.png) CAUTION: Production system administrators should review the setting and determine whether to leave the option to configured to “RUN IMMEDIATELY” or change the configuration. The SERVER ACTION (#221) field can be set to one of the following:

- R—RUN IMMEDIATELY
- Q—QUEUE SERVER ROUTINE
- N—NOTIFY MAIL GROUP (DO NOT RUN)
- I—IGNORE REQUESTS

To change the SERVER ACTION (#221) field on the XTVS PKG EXTRACT SERVER option:

Use the FileMan ENTER OR EDIT FILE ENTRIES \[DIEDIT\] option to change the value of the SERVER ACTION (#221) field in the OPTION (#19) file.

### Set Default Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the “VistA Package Size Analysis Manager” screen, set the Package Parameter file (i.e., XTMPSIZE\*.DAT) default directory as follows:

1.  Invoke the VistA Package Extract Manager \[XTVS VISTA PACKAGE EXTRACT MGR\] option.
2.  At the “Do you want to Display XTMPSIZE\*.BAK (backup files)? NO//” prompt, press Enter to accept the NO default response.
3.  From the “VistA Package Size Analysis Manager” screen, select the CHD—Change Host Directory action, as shown in <u>Figure 2</u>.

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/014.png) NOTE: The CHD—Change Host Directory action is locked with the XTVS EDITOR security key.

4.  Set the “VistA Package Size default directory” to a directory on the VistA server host system that the user, who will be managing package parameters and creating package size reports, has READ and WRITE privileges.

<span id="_Ref480957390" class="anchor"></span>Figure 2: CHD—Change Host Directory Action: Example

Vista Package Size Manager Apr 14, 2017@14:07:44 Page: 3 of 4

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 1 Build: 0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

22\) XTMPSIZE_GTS2-9-17_1627.DAT;1

23\) XTMPSIZE_GTS3-6-17_0922.DAT;1

24\) XTMPSIZE_GTS4-10-17_0839.DAT;1

25\) XTMPSIZE_GTS7-26-16_1054.DAT;1

26\) XTMPSIZE_GTS7-26-16_1119.DAT;1

27\) XTMPSIZE_GTS7-26-16_1527.DAT;1

28\) XTMPSIZE_GTS7-26-16_1531.DAT;1

29\) XTMPSIZE_GTS7-27-16_1016.DAT;1

30\) XTMPSIZE_GTS8-11-16_0838.DAT;1

31\) XTMPSIZE_GTS8-18-16_1014.DAT;1

32\) XTMPSIZE_GTS8-3-16_1545.DAT;1

33\) XTMPSIZE_GTS8-4-16_1321.DAT;1

34\) XTMPSIZE_GTS8-8-16_1532.DAT;1

\+ Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters <span class="mark">CHD Change Host Directory</span>

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Next Screen// <span class="mark">CHD \<Enter\></span> Change Host Directory

Package Size Parameter Edit for System: REDACTED.VA.GOV

--------------------------------------------------------------------------

VistA Package Size default directory VA3\$:\[XUUSER\]

--------------------------------------------------------------------------

VistA Package Size default directory: VA3\$:\[XUUSER\]//

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is *not* applicable (N/A). Kernel Toolkit Patch XT\*7.3\*143 does *not* require any database tuning.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the back-out strategy for Kernel Patch XT\*7.3\*143, including the established time limits or other parameters that comprise the rationale for the strategy.

Because all software and VistA Kernel structures installed with this patch are new (XTVS namespace), the entire patch can be removed without affecting any existing VistA applications. Specifically, Kernel Toolkit functionality existing prior to installing this patch will *not* be affected by its removal.

The need for a back-out would be determined by all affected organizations. This would primarily include representatives from Veterans Health Administration (VHA) and Enterprise Program Management (EPMO). In the case of the initial release, a back-out would include removal of data, files, and routines. In the case of future patches and releases, the back-out strategy would be dependent on the contents of the released functionality and could include restoration of file definitions, routines, or data.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations would include impact on production Veterans Health Information Systems and Technology Architecture (VistA) M servers.

Kernel Patch XT\*7.3\*143 is server software that involves installation in the following environment:

VistA M Servers: FORUM and at all VistA sites

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for Kernel Patch XT\*7.3\*143. There are no resources or standards set for Kernel load testing, and a load testing environment is *not* available.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) for the Kernel Patch XT\*7.3\*143 was performed by test sites and Software Quality Assurance (SQA) during the development and testing phase.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XT\*7.3\*143 VistA M Server back-out criteria follow existing VistA patch back-out procedures.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XT\*7.3\*143 VistA M Server back-out risks are the same risks established with existing VistA back-out procedures.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority for the need of back-out would reside with Veterans Health Administration (VHA), Office of Information and Technology (OIT), and Enterprise Program Management Office (EPMO) representatives.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XT\*7.3\*143 installation adds the XT73P143 routine and other new XTVS\* routines, options, protocols, security keys, parameters, and templates on the VistA M Servers. There are no other VistA M Server software updates.

To back-out Kernel Patch XT\*7.3\*143 from the VistA M Server, do the following:

1.  Open the VistA MailMan message created during the “Backup a Transport Global” step of the patch installation process (i.e.,* Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*, Section 24.7.8, “Backing Up Transport Globals”).

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/015.png) NOTE: A full restore of all components requires that prior to the installation the Backup a Transport Global \[XPD BACKUP\] option was used with the “Backup Type: B//” prompt set to “B” (Build).

1.  Follow the installation sequence (i.e.,* Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*, Section 24.7.1, “Installation Sequence”) to load and install a patch from a PackMan message. This installation restores the original (pre-patch) VistA components and deletes any new components added with the patch (e.g., routines, options, protocols, parameters, security keys).

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the back-out of Kernel Patch XT\*7.3\*143 from the VistA M Server, do the following:

1.  Verify that the following routines were removed:
- XT73P143
- XTVSCP
- XTVSHELP
- XTVSHLP1
- XTVSHLP2
- XTVSLAPI
- XTVSLDE
- XTVSLM
- XTVSLN
- XTVSLNA1
- XTVSLP
- XTVSLPC
- XTVSLPD1
- XTVSLPD2
- XTVSLPDC
- XTVSLPER
- XTVSLPR1
- XTVSLR
- XTVSRFL
- XTVSRFL1
- XTVSSVR
2.  Verify the following options were removed:
- XTVS PKG EXTRACT SERVER
- XTVS PKG MGR EXT PACKAGE MSG
- XTVS VISTA PACKAGE EXTRACT MGR
3.  Verify the following protocols were removed:
- XTVS PACKAGE MANAGER MENU
- XTVS PKG EXT CRT PARAM ACTION
- XTVS PKG EXT DISP CORRECTIONS ACTION
- XTVS PKG EXT DISP DEL ACTION
- XTVS PKG EXT EMAIL ACTION
- XTVS PKG EXT PARAM WRT ACTION
- XTVS PKG EXT QUERY REMOTE ACTION
- XTVS PKG EXT REDISP PARAM ACTION
- XTVS PKG EXTRACT CREATE ACTION
- XTVS PKG EXTRACT DEL ACTION
- XTVS PKG MGR DEL PACKAGE PARM ACTION
- XTVS PKG MGR EDIT PACKAGE PARM ACTION
- XTVS PKG MGR EMAIL OVRLAP RPT ACTION
- XTVS PKG MGR EXT DISP ACTION
- XTVS PKG MGR EXT DISP MENU
- XTVS PKG MGR EXT MNGR ACTION
- XTVS PKG MGR EXTRACT MENU
- XTVS PKG MGR FILE OVERLAP ACTION
- XTVS PKG MGR NEW PARAM MAIL ACTION
- XTVS PKG MGR NEW PARAM MENU
- XTVS PKG MGR PARAM CMPR MENU
- XTVS PKG MGR PARAM COMPARE ACTION
- XTVS PKG MGR PARAM COMPR MAIL ACTION
- XTVS PKG MGR PARAM DATA MAP HELP ACTION
- XTVS PKG MGR PARAM DISP CAPTION ACTION
- XTVS PKG MGR PARAM DISP CAPTN MENU
- XTVS PKG MGR PARAM DISP MENU
- XTVS PKG MGR PARAM DISP/EDIT ACTION
- XTVS PKG MGR PARAM ERR DISP ACTION
- XTVS PKG MGR PARAM ERROR MENU
- XTVS PKG MGR PARAM FILE DELETE ACTION
- XTVS PKG MGR PARAM OVRLP REDISP ACTION
- XTVS PKG MGR PARAM UNLOCK ACTION
- XTVS PKG MGR PREFIX OVERLAP ACTION
- XTVS PKG MGR RPT MAIL ACTION
- XTVS PKG MGR RPT MENU
- XTVS PKG MGR RPT QUERY REMOTE ACTION
- XTVS PKG MGR RPT WRT ACTION
- XTVS PKG MGR SAVE PACKAGE PARM ACTION
- XTVS PKG MGR VISTA SIZE RPT
- XTVS PKG QUERY REMOTE VISTA SIZE ACTION
- XTVS PKG RPT SWAP HEADER ACTION
- XTVS SITE PARAMETERS
4.  Verify the following security key was removed:

XTVS EDITOR

5.  Verify the following LIST templates were removed:
- XTVS PACKAGE MANAGER
- XTVS PKG EXT CRT PARAM
- XTVS PKG MGR EXT DISP
- XTVS PKG MGR EXTRACT MNGR
- XTVS PKG MGR PARAM CAPTN DISP
- XTVS PKG MGR PARAM COMPARE
- XTVS PKG MGR PARAM DISPLAY
- XTVS PKG MGR PARAM ERROR DISP
- XTVS PKG MGR VISTA SIZE RPT
2.  Verify the following PARAMETER template was removed:

XTVS PKG MGT PARAMETERS

3.  Verify the following parameter was removed:

XTVS PACKAGE MGR DEFAULT DIR

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. This section includes the specific steps to roll back to the previous state of the data and platform settings, if required. It includes the order of restoration for multiple interdependent systems.

Kernel Patch XT\*7.3\*143 does *not* export any data, so no database rollback is required.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is *not* applicable (N/A). Kernel Patch XT\*7.3\*143 does *not* export any data, so there are no rollback considerations required.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is *not* applicable (N/A). Kernel Patch XT\*7.3\*143 does *not* export any data, so there are no rollback criteria required.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is *not* applicable (N/A). Kernel Patch XT\*7.3\*143 does *not* export any data, so there are no rollback risks.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback *can* be authorized by system administrators once a problem has been identified. Office of Information and Technology (OIT) and Enterprise Program Management Office (EPMO) VistA Infrastructure (VI) Development Team should be informed immediately via a MailMan message sent to the following mail group:

REDACTED

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is *not* applicable (N/A). Kernel Patch XT\*7.3\*143 release does *not* export any data, so no rollback procedure is required.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is *not* applicable (N/A). Kernel Patch XT\*7.3\*143 release does *not* export any data, so no rollback verification procedure is required.

# Appendix A—Possible Installation Report Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Package File Extract Not Included in Patch Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Package File extract from FORUM was *not* included in the Patch Distribution:

<span id="_Toc63865726" class="anchor"></span>Figure 3: FORUM Package File Extract *Not* Included in Patch Distribution—Sample Error Message

\*\* ERROR: Forum File extract global \[^XTMP("XTSIZE")\] was

\*\* NOT INCLUDED in KIDS Transport! \*\*

\*\* CONTACT THE PATCH DEVELOPER!!! \*\*

## Package File Extract Data Stored in ^XTMP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Package file extract data is stored in the ^XTMP global on the VistA System; the patch was installed and used previously:

<span id="_Toc63865727" class="anchor"></span>Figure 4: Patch Installed Previously—Sample Message

 o Deleting any existing global extract files \[^XTMP(""XTSIZE"")\]

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/016.png) NOTE: A list of deleted ^XTMP(“XTSIZE”,PID) is provided.

## Failure to Load Package File Extract into a PackMan Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Package file extract was loaded into ^XTMP but the installation failed to load it into a PackMan message and send it to the installer:

<span id="_Toc63865728" class="anchor"></span>Figure 5: Failure to Load Package File Extract into a PackMan Message—Sample Error Message

   ...Error: ^XTMP(""XTSIZE"","\_XDOLRJ\_") not sent in Packman.

          ^XTMP(""XTSIZE"","\_XDOLRJ\_") global was not deleted.

      Use VistA Package Size Extract Manager to send in a Packman message.

![](vista-package-size-reporting-tool-vpsrt-deployment-installation-back-out-and-rol/017.png) ATTENTION: The ^XTMP global is available in the VistA Package Size Manager “Extract Manager” user interface, where it can be forwarded to anyone (including the installer).

## PARAMETER TEMPLATE File Entry Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The addition of the XTVS PKG MGT PARAMETERS template failed upon addition to the PARAMETER TEMPLATE (#8989.52) file:

<span id="_Toc63865729" class="anchor"></span>Figure 6: Failure to Add XTVS PKG MGT PARAMETERS to PARAMETER TEMPLATE (#8989.52) File—Sample Error Message

o 'XTVS PKG MGT PARAMETERS' addition to PARAMETER TEMPLATE file (#8989.52) failed.

Error: PARAMETER TEMPLATE file entry failure!

## PARAMETER TEMPLATE Parameters Sub-file Entry Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The addition of the XTVS PKG MGT PARAMETERS template failed upon addition of the XTVS PACKAGE MGR DEFAULT DIR to the PARAMETER (#8989.521) Multiple field:

<span id="_Toc63865730" class="anchor"></span>Figure 7: Failure to Add XTVS PKG MGT PARAMETERS to XTVS PACKAGE MGR DEFAULT DIR PARAMETER (#8989.521) Multiple Field—Sample Error Message

o 'XTVS PKG MGT PARAMETERS' addition to PARAMETER TEMPLATE file (#8989.52) failed.

Error: PARAMETER TEMPLATE Parameters Sub-file entry failure!

## Patch Previously Installed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The addition of the XTVS PKG MGT PARAMETERS template to the PARAMETER TEMPLATE (#8989.52) file is *not* necessary; the patch was previously installed:

<span id="_Toc63865731" class="anchor"></span>Figure 8: Unnecessary to Add XTVS PKG MGT PARAMETERS to PARAMETER TEMPLATE (#8989.52) File—Sample Patch Previously Installed Message

o 'XTVS PKG MGT PARAMETERS' Parameter Template entry exists.

       ...no need to add 'XTVS PKG MGT PARAMETERS' to file \#8989.52.

[^1]: Cron is a time-based job scheduler in Unix-like computer operating systems. People who set up and maintain software environments use cron to schedule jobs (commands or shell scripts) to run periodically at fixed times, dates, or intervals. It typically automates system maintenance or administration. These scripts are suitable for scheduling repetitive tasks: Wikipedia; <https://en.wikipedia.org/wiki/Cron>