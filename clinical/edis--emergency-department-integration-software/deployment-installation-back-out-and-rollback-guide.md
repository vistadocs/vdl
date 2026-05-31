---
title: EDP*2*15 EDIS Deployment, Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: active
pkg_ns: EDP
patch_ver: 2
patch_id: EDP*2*15
group_key: EDIS:EDP:2
file_numbers: []
security_keys: []
menu_options: 0
description: '''Table 1: Deployment, Installation, Back-out, and Rollback Roles and'''
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 3523
section_count: 31
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: June 2021
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software/edp_2_2_p15_dibr_r.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software/edp_2_2_p15_dibr_r.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=179
audit_applied: '2026-05-31'
master_source: EDP*2*15 EDIS Deployment, Installation, Back-out, and Rollback Guide
master_pub_date: June 2021
consolidated_from: 3 versions
prior_versions:
- EDP*2*16 EDIS Deployment, Installation, Back-out, and Rollback Guide
- EDP*2*22 EDIS Deployment, Installation, Back-out, and Rollback Guide
consolidated_title: edis deployment, installation, back-out, and rollback guide
---

![](edp-2-15-edis-deployment-installation-back-out-and-rollback-guide/001.png)

VistA EDP\*2.0\*15

EDIS GUI Version 2.2.43

June 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc80894098" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
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
<td>06/23/2021</td>
<td>1.0</td>
<td><p>EDIS 2.2.43/EDP*2.0*15:</p>
<ul>
<li><p><strong>EDIS 2.2.43</strong> (GUI) consists of the deployment of 2 ear files coordinated by the OIT EDIS Sustainment team</p></li>
<li><p><strong>EDP*2.0*15</strong> (VistA) consists of the invoking a PackMan message in FORUM by Regional IT Support</p></li>
<li><p>Reintroduces SSOi for users</p></li>
<li><p>See the non-redacted EDIS_2_2_P15_DIBR on the SOFTWARE library for viewing <mark>REDACTED</mark> information</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
</tbody>
</table>

<span id="_Toc80894098" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Guide for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the *Deployment, Installation, Back-out, and Rollback Guide* is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

1 Introduction [1](#introduction)

1.1 Purpose [1](#purpose)

1.2 Dependencies [1](#dependencies)

1.3 Constraints [1](#constraints)

2 Roles and Responsibilities [2](#roles-and-responsibilities)

3 Deployment [4](#deployment)

3.1 Timeline [4](#timeline)

3.2 Site Readiness Assessment [4](#site-readiness-assessment)

3.2.1 Deployment Topology (Targeted Architecture) [4](#deployment-topology-targeted-architecture)

3.2.2 Site Information (Locations, Deployment Recipients) [4](#site-information-locations-deployment-recipients)

3.2.3 Site Preparation [5](#site-preparation)

3.3 Resources [5](#resources)

3.3.1 Facility Specifics [5](#facility-specifics)

3.3.2 Hardware [5](#hardware)

3.3.3 Software [6](#software)

3.3.4 Communications [6](#communications)

4 Installation [7](#installation)

4.1 Pre-installation and System Requirements [7](#pre-installation-and-system-requirements)

4.2 Platform Installation and Preparation [7](#platform-installation-and-preparation)

4.3 Download and Extract Files [7](#download-and-extract-files)

4.4 Database Creation [8](#database-creation)

4.5 Installation Scripts [8](#installation-scripts)

4.6 Cron Scripts [8](#cron-scripts)

4.7 Access Requirements and Skills Needed for the Installation [8](#access-requirements-and-skills-needed-for-the-installation)

4.8 Installation Procedure [8](#installation-procedure)

4.8.1 KIDS Installation [8](#kids-installation)

4.9 Installation Verification Procedure [9](#installation-verification-procedure)

4.9.1 KIDS Verification [9](#kids-verification)

4.10 System Configuration [9](#system-configuration)

4.11 Database Tuning [9](#database-tuning)

5 Back-Out Procedure [10](#back-out-procedure)

5.1 Back-Out Strategy [10](#back-out-strategy)

5.2 Back-Out Considerations [10](#back-out-considerations)

5.2.1 Load Testing [10](#load-testing)

5.2.2 User Acceptance Testing [10](#user-acceptance-testing)

5.3 Back-Out Criteria [10](#back-out-criteria)

5.4 Back-Out Risks [10](#back-out-risks)

5.5 Authority for Back-Out [10](#authority-for-back-out)

5.6 Back-Out Procedure [11](#back-out-procedure-1)

5.6.1 KIDS Back-Out [11](#kids-back-out)

5.7 Back-out Verification Procedure [11](#back-out-verification-procedure)

5.7.1 KIDS Back-out Verification [11](#kids-back-out-verification)

6 Rollback Procedure [12](#rollback-procedure)

6.1 Rollback Considerations [12](#rollback-considerations)

6.2 Rollback Criteria [12](#rollback-criteria)

6.3 Rollback Risks [12](#rollback-risks)

6.4 Authority for Rollback [12](#authority-for-rollback)

6.5 Rollback Procedure [12](#rollback-procedure-1)

6.6 Rollback Verification Procedure [12](#rollback-verification-procedure)

List of Tables

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities [2](#_Toc80894098)

Table 2: Site Preparation [5](#_Toc80894099)

Table 3: Facility-Specific Features [5](#_Toc80894100)

Table 4: Hardware Specifications [5](#_Toc80894101)

Table 5: Software Specifications [6](#_Toc80894102)

Table 6: Deployment/Installation/Back-Out Checklist [6](#_Ref75328055)

Table 7: Associated Patch Files [7](#_Toc80894104)

Table 8: Routines [9](#_Toc80894105)

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
    - [KIDS Installation](#kids-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
    - [KIDS Verification](#kids-verification)
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
    - [KIDS Back-Out](#kids-back-out)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
    - [KIDS Back-out Verification](#kids-back-out-verification)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
There are 2 parts to this release:
1.  EDIS 2.2.43 refers to the GUI/Web Server version (reintroduces SSOi)
2.  EDP\*2.0\*15 refers to the VistA (KIDS Build) patch
This document will focus on the deployment, installation,and back-out procedures for VistA patch EDP\*2.0\*15. The EDIS 2.2.43 deployment will be completed by the OIT EDIS Sustainment team prior to the procedures outlined in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom EDP\*2.0\*15 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, communications plan, and rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch must be installed after EDP\*2.0\*6.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDP\*2.0\*15 is expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. EDP\*2.0\*15 utilizes existing nationally released security controls to control access.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multiple entities oversee decision making for the deployment, installation, back-out and rollback of EDP\*2.0\*15. Application Coordinators approve deployment and install from an OIT perspective. If an issue with the software arises, then the facility Chief Information Officer (CIO) and other site leadership will meet along with input from Patient Safety, Health Product Support (HPS), and regional leadership to initiate a back out and rollback decision of the software. The following table provides EDP\*2.0\*15 information.

<table>
<caption><p><span id="_Toc80894099" class="anchor"></span>Table 2: Site Preparation</p></caption>
<colgroup>
<col style="width: 36%" />
<col style="width: 19%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enterpirse Operations</td>
<td>Deployment</td>
<td>Deploy the Oracle Weblogic Application Server ear files</td>
</tr>
<tr class="even">
<td>Site personnel in conjunction with information technology (IT) support – which may be local or regional.</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
</tr>
<tr class="odd">
<td>Site personnel in conjunction with IT support – which may be local or regional.</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
</tr>
<tr class="even">
<td>Site personnel.</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="odd">
<td>Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the Kernel Installation and Distribution System (KIDS) build.</td>
<td>Deployment</td>
<td>Execute deployment</td>
</tr>
<tr class="even">
<td>Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the KIDS.</td>
<td>Installation</td>
<td>Plan and schedule installation</td>
</tr>
<tr class="odd">
<td>N/A – will work under the VistA authority to operate (ATO) and security protocols.</td>
<td>Installation</td>
<td>Ensure that ATO and certificate authority security documentation is in place</td>
</tr>
<tr class="even">
<td>N/A – no equipment is being added.</td>
<td>Installation</td>
<td>Validate through facility point of contact (POC) to ensure that IT equipment has been accepted using asset inventory processes</td>
</tr>
<tr class="odd">
<td>N/A – no new functionality is being introduced.</td>
<td>Installations</td>
<td>Coordinate training</td>
</tr>
<tr class="even">
<td>Facility CIO and IT support – which may be local or regional.</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
</tr>
<tr class="odd">
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the HPS Clinical Sustainment team.</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
</tr>
</tbody>
</table>

<span id="_Toc80894099" class="anchor"></span>Table 2: Site Preparation

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 2 components for this release:

1.  EDIS 2.2.43 GUI/Web Server (reintroduces SSOi)
    1.  This ear file deployment is completed by the OIT EDIS Sustainment team.
2.  EDP\*2.0\*15 VistA Patch
    1.  Installed/deployed using a PackMan message in FORUM by Regional IT support.

Deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release EDP\*2.0\*15, the patch will be released via the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing, and deployment to production will be at the site's discretion. It is anticipated that there will be a 30-day compliance period.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific timeline for deployment. This is considered a maintenance release and installation will be at the site's discretion within the contstraints of the compliance period for the release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the EDP\*2.0\*15 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDP\*2.0\*15 will be deployed to each VistA instance and the nationally deployed EDIS Uniform Resource Locater (URL) will be updated to EDIS 2.2.43. That will include local sites as well as regional data processing centers.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, EDP\*2.0\*15 will be deployed to all VistA systems.

The Production IOC testing sites are:

- Boston Health Care System
- VA Long Beach Health Care System
- Greater Los Angeles Health Care System

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for EDP\*2.0\*15. A fully patched VistA system is the only requirement.

It would be beneficial if users have their PIV card linked to their VistA instance prior to installation.

> **NOTE:** Upon installation of EDP\*2.0\*15, sites should be aware that "ghost" patients, patients with a LOC field entry of 0 and a recent visit within 5 days, will appear on their EDIS board in the default room defined by the site. Refer to the patch description for technical details.

The following table describes preparation required by the site prior to deployment.

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            |                           |                                             |                   |           |

<span id="_Toc80894100" class="anchor"></span>Table 3: Facility-Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      |                |                     |           |

<span id="_Toc80894101" class="anchor"></span>Table 4: Hardware Specifications

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   |           |             |                   |                  |           |

<span id="_Toc80894102" class="anchor"></span>Table 5: Software Specifications

Please see the Roles and Responsibilities table in section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software | Make | Version | Configuration | Manufacturer | Other |
|-----------------------|----------|-------------|-------------------|------------------|-----------|
| N/A                   |          |             |                   |                  |           |

<span id="_Ref75328055" class="anchor"></span>Table 6: Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDP\*2.0\*15 will be deployed using the standard method of patch release from the National Patch Module. When EDP\*2.0\*15 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the EDP\*2.0\*15 patch. This patch is tracked nationally for all VA Medical Centers (VAMCs) in the National Patch Module (NPM) in FORUM. FORUM automatically tracks the patches as they are installed in the different VAMC production systems. A report can be executed in FORUM to identify when the patch was installed in VistA production systems at each site. A report can also be run to identify which sites have not currently installed the patch in their VistA production system. Therefore, this information does not need to be manually tracked in Table 6.

EDIS 2.2.43 is Nationally deployed to all sites by updating the existing EDIS URL. Tracking is not necessary.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| N/A      | N/A | N/A  | N/A                           |
| N/A      | N/A | N/A  | N/A                           |
| N/A      | N/A | N/A  | N/A                           |

<span id="_Toc80894104" class="anchor"></span>Table 7: Associated Patch Files

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two parts to the EDP\*2.0\*15 installation.

1.  EDIS 2.2.43 (GUI)
    1.  Deployment and installation of EDIS_EAR_MAIN_2_2_43.ear and EDIS_EAR_BIGBOARD_2_2_43.ear files on the Oracle WebLogic Application Server by the OIT EDIS Sustainment team. This step has been completed.
2.  EDP\*2.0\*15
    1.  Deployment and installation on the site's VistA server via PackMan message.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDP\*2.0\*15 is installable on a fully patched VistA system.

> **NOTE:** It is imperative to perform a back-up of the routines included in this patch prior to installation. This back-up is required if a back-out of EDP\*2.0\*15 is needed.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDP\*2.0\*15 must be installed on the VistA System. This patch must be installed by the compliance date.

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents and files can be obtained from the SOFTWARE library:

REDACTED

| File                  | Description                                         |
|-----------------------|-----------------------------------------------------|
| EDIS_2_2_IG.pdf       | Server Installation Guide with Client Configuration |
| EDIS_2_2_TM.pdf       | Technical Manual                                    |
| EDIS_2_2_UG.pdf       | User Guide                                          |
| EDP_2_2_P15_DIBR.pdf  | Deployment, Installation, Back-out, Rollback guide  |
| EDIS_2_2_GLOSSARY.pdf | Glossary                                            |

<span id="_Toc80894105" class="anchor"></span>Table 8: Routines

The documents are also available on the VistA Documentation Library (VDL), which is located at:

<https://www.va.gov/vdl/application.asp?appid=179>

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of EDP\*2.0\*15 requires the following to install:

- Programmer access to VistA instance.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name (e.g. EDP\*2.0\*15).

> NOTE: Using \<spacebar\>\<enter\> will not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build.

2.  Select the Backup a Transport Global option to create a backup message of any routines exported with this patch. It will not backup any other changes such as data dictionaries or templates.
3.  You may also elect to use the following options:
    1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, data dictionaries, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
    1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
    2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
    3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the routine checksums in the table below.

| Routine | Before Checksum | After Checksum | Patch List   |
|---------|-----------------|----------------|--------------|
| EDP15P  | New             | B2688979       | \*\*15\*\*   |
| EDPQDB  | B56093021       | B57296617      | \*\*6,15\*\* |

RoutinesThis table shows the list of routines and their before checksums, after checksums, and patch list associations.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only reason to consider a back-out of EDP\*2.0\*15 is in the event of a catastrophic failure.

The back-out plan is to restore the routines from the backup created in section 4.8.1, step 2B.

VistA changes in EDP\*2.0\*15 are independent of the GUI changes in EDIS 2.2.43. The VistA patch can be backed out without impact to the GUI.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed for EDP\*2.0\*15. This was a maintenance release to correct defects; there was no additional functionality included.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the test sites listed in section 3.2.2. The sites followed the provided test plan/concurrence form and executed the test cases according to the plan for the first build of EDP\*2.0\*15. The sites either passed or failed any item based on testing. The tests were performed by IT analysts at each site who are familiar with using the application. Any items that failed were then re-developed, sent back to the sites, and tested for the next build following the same process. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application or a significant patient impact issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out EDP\*2.0\*15 would result in the re-instatement of the issues addressed in the previous version of EDIS. In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The facility Chief Information Officer may make the decision to back-out the VistA patch.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrators will need to use the PackMan function INSTALL/CHECK MESSAGE. Check MailMan messages for the backup message sent by the Backup a Transport Global function executed prior to the patch install. (See section 4.8.1, Step 2B; this must be done before the patch is installed).

1.  In VistA MailMan, select the message shown below:
    1.  Backup of EDP\*2.0\*15 install on \<mm, dd, yyyy\> \<user name\>
2.  Select the Xtract PackMan option.
3.  Select the Install/Check Message option.
4.  Enter Yes at the prompt.
5.  Enter No at the backup prompt. There is no need to back up the backup.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS Back-out Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the back-out completed successfully, ensure the routine checksums match the before checksums in section 4.9.1.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for EDP\*2.0\*15.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: EDP*2*22 EDIS Deployment, Installation, Back-out, and Rollback Guide

### Ear File Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  IO team backups the previous ear files.
    1.  EDIS_EAR_MAIN_2_2_42.ear
    2.  EDIS_EAR_BIGBOARD_2_2_42.ear
2.  IO team removes the previous ear files.
3.  IO team deploys the new ear files.
    1.  EDIS_EAR_MAIN_2_2_44.ear
    2.  EDIS_EAR_BIGBOARD_2_2_44.ear

### Ear File Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The bottom right corner of the application login page from the EDIS URL should begin with Build: 2.2.44.

### Ear File Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  IO team removes the new ear files.
    1.  EDIS_EAR_MAIN_2_2_44.ear
    2.  EDIS_EAR_BIGBOARD_2_2_44.ear
2.  IO team deploys the previous ear files.
    1.  EDIS_EAR_MAIN_2_2_42.ear
    2.  EDIS_EAR_BIGBOARD_2_2_42.ear

### Ear File Back-out Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The bottom right corner of the application login page from the EDIS URL should begin with Build: 2.2.42.
