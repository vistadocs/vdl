---
title: OR*3.0*608 (CPRS v33SWD) Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: (CPRS v33SWD)
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*608
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - cprs
  - table
  - contents
  - installation
  - back
  - rollback
  - vista
  - deployment
  - chart
  - procedure
page_count: 0
word_count: 4354
section_count: 33
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_608_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_608_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>CPRS v33SWD Graphical User Interface (OR\*3.0\*608) Deployment, Installation, Back-Out, and Rollback Guide (DIBOR)
---

![](or-3-0-608-cprs-v33swd-deployment-installation-back-out-and-rollback-guide/001.png)

August 2024

Office of Information and Technology (OI&T)

Revision History

| Date    | Version | Description                                                                                                                      | Author            |
|---------|---------|----------------------------------------------------------------------------------------------------------------------------------|-------------------|
| 07/2024 | v33SWD  | Changing version numbers for v33swd 109.1 and updated the CRC to 329DC1A4. Updated the version number for the Mental Health DLL. | CPRS Program Team |
| 07/2024 | v33SWD  | Changing version numbers for v33swd 108.3 and updated the CRC to A23C0028. Added the version number for the Mental Health DLL.   | CPRS Program Team |
| 07/2024 | v33SWD  | Changing version numbers for v33swd 108.2 and updated the CRC to 3AD7D479. Added the version number for the Mental Health DLL.   | CPRS Program Team |
| 06/2024 | v33SWD  | Changing version numbers for v33swd 108.1 and updated the CRC to 2BBC42B4.                                                       | CPRS Program Team |
| 06/2024 | v33SWD  | Changing version numbers for v33swd 107.3 and updated the CRC to F2635DD3.                                                       | CPRS Program Team |
| 05/2024 | v33SWD  | Changing version numbers for v33swd 107.2.                                                                                       | CPRS Program Team |
| 04/2024 | v33SWD  | Changing version numbers for v33swd 107.1.                                                                                       | CPRS Program Team |
| 03/2024 | v33SWD  | Changing version numbers for v33swd 106.3                                                                                        | CPRS Program Team |
| 03/2024 | v33SWD  | Updating for production installations.                                                                                           | CPRS Program Team |
| 01/2023 | v33     | Deployment, Installation, Back-Out, and Rollback Guide (DIBR)                                                                    | CPRS Program Team |

<span id="_Toc175224663" class="anchor"></span>Table : DIBOR Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Table of Contents

List of Tables

[Table 1: DIBOR Roles and Responsibilities [3](#_Toc175224663)](#_Toc175224663)

[Table 3: Deployment/Installation/Back-Out Checklist [6](#_Ref86756345)](#_Ref86756345)

List of Figures

[Figure 1: Example of the Target Field [13](#_Toc161997245)](#_Toc161997245)

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
  - [Resources](#resources)
    - [Software](#software)
    - [Communications](#communications)
  - [Backup Procedures](#backup-procedures)
- [Installation](#installation)
  - [Pre-installation](#pre-installation)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Locking General User Access to CPRS GUI](#locking-general-user-access-to-cprs-gui)
    - [Assigning the OR CPRS TESTER Key](#assigning-the-or-cprs-tester-key)
    - [Locking the OR CPRS GUI CHART Option](#locking-the-or-cprs-gui-chart-option)
  - [Installation](#installation-1)
    - [CPRSV33SWDCOMBINEDBUILD.KID](#cprsv33swdcombinedbuildkid)
    - [CPRS GUI Executable Methods of Installation](#cprs-gui-executable-methods-of-installation)
    - [DLL Installation](#dll-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
  - [Remove Locking of the OR CPRS GUI CHART Option](#remove-locking-of-the-or-cprs-gui-chart-option)
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
The Computerized Patient Record System (CPRS) is part of the Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.
This document describes how to deploy and install the items that comprise the CPRS v33SWD release, consisting of a combined build, a Graphical User Interface (GUI) executable, and a Dynamic Link Library (DLL). The combined build for CPRS v33SWD includes three patches: OR\*3.0\*608, YS\*5.01\*237, and TIU\*1.0\*318. The Mental Health DLL is YS_MHA_A_XE10.dll version 1.0.5.16.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide specific instructions for the CPRS v33SWD installation, back-out, and rollback procedures that describe how, when, where, and to whom CPRS v33SWD will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, the communications plan, and rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v33SWD requires a fully patched VistA system.

The following patches must be installed on the system before CPRS v33SWD is installed:

- OR\*3.0\*560
- OR\*3.0\*588
- TIU\*1.0\*184
- TIU\*1.0\*283
- TIU\*1.0\*289
- YS\*5.01\*211
- YS\*5.01\*223

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v33SWD has a combined multi-patch build, a GUI executable, and the Mental Health DLL. The combined build is installed on the VistA server and the executable and DLL can be placed on a VA Application Consolidated Server (VACS) server, on a Cloud server, a Citrix server, or on local workstations or on a combination of them, depending on site configuration.

CPRS v33SWD is 508 compliant and uses the same security measures as VistA. Users will authenticate using either their Personal Identification Verification (PIV) card or access and verify codes.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref86756345" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 36%" />
<col style="width: 13%" />
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
<td></td>
<td>CPRS Implementation Team</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>CPRS Software Quality Assurance (SQA) team and field test sites</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Application Coordinators</td>
<td><p>Release</p>
<p>Deployment</p></td>
<td>Review patches for release readiness and release patches for deployment.</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>HISM and Local sites</td>
<td>Installation</td>
<td>Health Infrastructure and Systems Management (HISM) installers will coordinate with individual sites on a date and time for each site or groups of sites to install.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Sites</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place. Ensure staff is trained prior to the installation.</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>HISM and CPRS Launcher Developer</td>
<td>Installation</td>
<td>Coordinate to update CPRS Launcher to launch the newly released software.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>CPRS Implementation Team</td>
<td>Installations</td>
<td>Provide national installation and train-the-trainer presentations. Other groups may also provide training.</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>CPRS Implementation Team, HISM, and Area Manager</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>CPRS Implementation, Product Support, and Sustainment Teams</td>
<td>Post Deployment</td>
<td>Software Support will be provided by the CPRS Implementation Team during warranty period, which is 90 days after national release. Support then changes to the normal ticketing process.</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref86756345" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment will be a standard release with a 45-day compliance period.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for 45 days following national release.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v33SWD bundle of patches and the accompanying GUI executable and DLL will be deployed to sites. The patches will be installed on the VistA server and the GUI executable and DLL will be installed on a VACS server, on a Cloud server, a Citrix server, or on local workstations or on a combination of them, depending on site configuration.

This section discusses the locations that will receive the CPRS v33SWD deployment.

In preparation for your installation of CPRS v33SWD, please ensure you have reviewed the [CPRS v33SWD training material](https://dvagov.sharepoint.com/sites/vhaihpcprs/SitePages/CPRS-33SWD.aspx?xsdata=MDV8MDJ8fGM5YzQzZDdmOTk4ODQ5ZjUzZmJhMDhkYzk1M2NkODFmfGU5NWYxYjIzYWJhZjQ1ZWU4MjFkYjdhYjI1MWFiM2JmfDB8MHw2Mzg1NDkzMzU3MzYyNzA3Nzh8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPbTFsWlhScGJtZGZUbFJLYkU1NldtbE5hbU4wV1ZSUmVWcHBNREJPVkdjMVRGZEpNMDlYV1hST2Vra3hUMVJOTkZwcVRUUk5SRlV4UUhSb2NtVmhaQzUyTWk5dFpYTnpZV2RsY3k4eE56RTVNek0yTnpjeU5EQTJ8MjFiYzYxY2M1MjdiNGFkMjNmYmEwOGRjOTUzY2Q4MWZ8MDg2OGVkMzM2OGEyNDY0MmEzZDdkNDk4Njg2Y2NhMTg%3D&sdata=bkZmekxCTnBxWVIvMWEwNzB3SUU4MVA3TzBNVi9Wb3gxVzQyQnl0WERNND0%3D&ovuser=e95f1b23-abaf-45ee-821d-b7ab251ab3bf%2CJamie.Crumley%40va.gov&OR=Teams-HL&CT=1719408403109&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNDA1MTYyMjIyMyIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D). The [Implementation Toolkit](https://dvagov.sharepoint.com/:w:/r/sites/vhaihpcprs/_layouts/15/Doc.aspx?sourcedoc=%7B311AD297-7269-43B7-84BC-588172B6D702%7D&file=IHP_A_Facility_Guide_to_CPRS_V33SWD_Implementation_Toolkit.docx&action=default&mobileredirect=true) provides detailed information on preparing for the installation and the [CAC/HiS Guidance and Set-up document](https://dvagov.sharepoint.com/sites/vhaihpcprs/SitePages/CPRS-33SWD.aspx?xsdata=MDV8MDJ8fGM5YzQzZDdmOTk4ODQ5ZjUzZmJhMDhkYzk1M2NkODFmfGU5NWYxYjIzYWJhZjQ1ZWU4MjFkYjdhYjI1MWFiM2JmfDB8MHw2Mzg1NDkzMzU3MzYyNzA3Nzh8VW5rbm93bnxWR1ZoYlhOVFpXTjFjbWwwZVZObGNuWnBZMlY4ZXlKV0lqb2lNQzR3TGpBd01EQWlMQ0pRSWpvaVYybHVNeklpTENKQlRpSTZJazkwYUdWeUlpd2lWMVFpT2pFeGZRPT18MXxMMk5vWVhSekx6RTVPbTFsWlhScGJtZGZUbFJLYkU1NldtbE5hbU4wV1ZSUmVWcHBNREJPVkdjMVRGZEpNMDlYV1hST2Vra3hUMVJOTkZwcVRUUk5SRlV4UUhSb2NtVmhaQzUyTWk5dFpYTnpZV2RsY3k4eE56RTVNek0yTnpjeU5EQTJ8MjFiYzYxY2M1MjdiNGFkMjNmYmEwOGRjOTUzY2Q4MWZ8MDg2OGVkMzM2OGEyNDY0MmEzZDdkNDk4Njg2Y2NhMTg%3D&sdata=bkZmekxCTnBxWVIvMWEwNzB3SUU4MVA3TzBNVi9Wb3gxVzQyQnl0WERNND0%3D&ovuser=e95f1b23-abaf-45ee-821d-b7ab251ab3bf%2CJamie.Crumley%40va.gov&OR=Teams-HL&CT=1719408403109&clickparams=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiI0OS8yNDA1MTYyMjIyMyIsIkhhc0ZlZGVyYXRlZFVzZXIiOmZhbHNlfQ%3D%3D) discusses post-install steps.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v33SWD will be deployed to all VistA instances. There is a server component and a GUI executable.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional resources are required.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v33SWD requires a fully patched VistA System for installation.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For national release, sites will receive a notification that the release has occurred, which will normally be an Action Item or Bulletin.

Sites will use their internal communications to let their users know about upcoming installations and any associated downtime. This is critical as users can often slow the installation process if they are on the system while installers are trying to get the software installed.

Clinical Application Coordinators (CAC), installers, and other site personnel (as determined by the site) will need to coordinate installation dates and times. In addition, other support personnel may need to be consulted – such as the Citrix support, Cloud support, Client Technologies, or others.

#### Deployment/Installation/Back-Out Checklist

Table 2 captures the coordination effort and documents the day/time when each activity (deploy, install, back-out) is completed for a project. It also lists the individual who performed the task.

| Activity                              | Day | Time | Individual who completed task |
|---------------------------------------|-----|------|-------------------------------|
| Install patches                       |     |      |                               |
| Deploy CPRS GUI and Mental Health DLL |     |      |                               |

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ensure the backup of the combined build has been performed.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\* Installation of these patches must NOT be queued. \*\*\*

There are no specific pre-installation steps required for this release of CPRS, however this release contains an updated CPRS executable and an updated Mental Health Dynamic Link Library (DLL). Please coordinate with the appropriate personnel to ensure the combined build, executable, and DLL are installed at the same time. In addition, coordinate with the appropriate personnel to ensure the current version of the Vitals DLL in use at the site is placed in the same folder as the CPRS executable.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v33SWD should follow a normal CPRS installation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The host file will be available at the following location:

/srv/vista/patches/SOFTWARE/CPRS_V33SWD_COMBINED_BUILD.KID

To download the documentation and other files, such as the GUI executable, use the following location: <https://download.vista.med.va.gov/index.html/SOFTWARE>

These files must be installed in the following order. Detailed instructions are in section 4.8 [Installation](#installation-1).

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 28%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File name</strong></th>
<th><strong>Contents</strong></th>
<th><strong>Retrieval Format</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CPRS_V33SWD_COMBINED_BUILD.KID</td>
<td>CPRS V33SWD COMBINED BUILD</td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>OR_30_608.zip</td>
<td><p>CPRSChart.exe</p>
<p>RoboEx32.dll</p>
<p>borlndmm.dll</p>
<p>CPRSChart.map</p>
<p>CRC.TXT</p>
<p>WebView2Loader.dll</p>
<p>YS_MHA_A_XE10.dll</p>
<p>Help Directory</p></td>
<td>Binary</td>
</tr>
</tbody>
</table>

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- CACs will be available for configuration and troubleshooting.
- Health Infrastructure and Systems Management (HISM) installer with programmer access is available.

## Locking General User Access to CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** When the OR CPRS GUI CHART option is locked, it will prevent users from logging into VistA Read-Only (VistARO). To overcome this login restriction, you can contact the Health Systems team and ask them to turn off shadowing before you lock the option. After the installation, when you remove the lock from the option, you will need to notify the Health Systems team to turn the shadowing on.

When a user launches the CPRS GUI, the underlying VistA system checks to see if the user has access to the OR CPRS GUI CHART entry in the OPTION (#19) file. The ability to run the CPRS GUI can be restricted by adding the OR CPRS TESTER security key to the OR CPRS GUI CHART entry’s LOCK (#3) field in the OPTION (#19) file. Locking an option with a security key is a long-standing feature of VistA. The primary benefit of restricting access to CPRS GUI is reducing the potential for errors from users accessing the software before post-installation configuration has completed.

When the lock is activated in a VistA system, only users who hold either the OR CPRS TESTER or XUPROGMODE security keys will be able to launch the CPRS GUI against that VistA system. Until the lock is deactivated, all other users who attempt to launch the CPRS GUI in that VistA system will receive an “option is locked” error message. Because option locking is a VistA feature, locking access to OR CPRS GUI CHART in a test VistA system has no effect on a user’s ability to access OR CPRS GUI CHART in a production VistA system.

> **IMPORTANT:** Prior to installing CPRS v33SWD, facility staff must create a list of users to whom the OR CPRS TESTER key shall be assigned. Typically, this would be informatics staff involved with testing and configuring a new version of CPRS GUI. These names will be used in section 4.7.1- Assigning the OR CPRS TESTER Key.

### Assigning the OR CPRS TESTER Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To allocate the OR CPRS TESTER key to users identified in the “Locking General User Access to CPRS GUI” section, CACs may use the CPRS Configuration (Clin Coord) \[OR PARAM COORDINATOR MENU\] menu’s Allocate OE/RR Security Keys \[ORCL KEY ALLOCATION\] option.

OR CPRS TESTER will be the last security key presented when using this allocation option.

> **NOTE:** Once the OR CPRS GUI CHART option is locked, some users will not be displayed in the provider selection box(es) in CPRS. Only OR CPRS TESTER key users will be displayed in some places.

### Locking the OR CPRS GUI CHART Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Post-install testers need to know that once the OR CPRS GUI CHART option is locked, some users’ names will not display in the provider selection box(es) in CPRS.

VistA Applications Support--To enact the locking and allow only authorized users to open CPRS GUI:

1.  At the Systems Manager Menu Option prompt, type Menu Management and press \<Enter\>.
2.  At the Select Menu Management Option prompt, type Edit Options and press \<Enter\>.
3.  At the Select OPTION to edit prompt, type OR CPRS GUI CHART and press \<Enter\>.
4.  At the NAME prompt, it should read ‘OR CPRS GUI CHART’. Accept the name by pressing \<Enter\>.
5.  At the MENU TEXT prompt, press \<Enter’\>
6.  At the PACKAGE prompt, press \<Enter\>.
7.  At the OUT OF ORDER MESSAGE prompt, press \<Enter\>.
8.  At the LOCK prompt, type OR CPRS TESTER and press \<Enter\>.

> **NOTE:** Holders of the XUPROGMODE key are exempt from this option file locking mechanism. This is an existing feature of the Kernel Menu Management module.

\<CPM\> Select Systems Manager Menu Option: MENU MANagement

          Edit options

          Key Management ...

          Secure Menu Delegation ...

          Restrict Availability of Options

          Option Access By User

          List Options by Parents and Use

          Fix Option File Pointers

          Help Processor ...

   OPED   Screen-based Option Editor

          Display Menus and Options ...

          Menu Rebuild Menu ...

          Out-Of-Order Set Management ...

          See if a User Has Access to a Particular Option

          Show Users with a Selected primary Menu

\<CPM\> Select Menu Management Option: EDIT OPtions

Select OPTION to edit: OR CPRS GUI CHART       CPRSChart version 1.32.515.2

NAME: OR CPRS GUI CHART//

MENU TEXT: CPRSChart version 1.32.515.2  Replace

PACKAGE:

OUT OF ORDER MESSAGE:

LOCK: OR CPRS TESTER

REVERSE/NEGATIVE LOCK: ^

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CPRS_V33SWD_COMBINED_BUILD.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre-Installation Instructions:

The combined build should not be installed with users on the system. To minimize potential disruptions to users, installation during non-peak hours is recommended. This combined build should take less than five minutes to install.

> **WARNING:** Do not queue the installation. Installation of a CPRS upgrade should not be queued.

Installation Instructions:

1.  From the Kernel Installation and Distribution menu, select the Installation menu.
2.  From this menu, choose to Load a Distribution and enter the location of the Host File CPRS_V33SWD_COMBINED_BUILD.KID.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter CPRS V33SWD COMBINED BUILD 1.0.
1.  Backup a Transport Global -This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.)
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond NO.
8.  If prompted ‘Delay Install (Minutes): (0 – 60): 0//’, respond 0.

### CPRS GUI Executable Methods of Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites are using these three methods to distribute the application:

- Network (shared) Installation:

> The executable is placed on a network drive that is accessed from a shortcut, such as in the “Gold Star” as some sites use. Users should not create a different shortcut on their desktop. Using the correct shortcut will mean that when an update occurs, users will not have to make any changes because the existing shortcut will launch the correct CPRS version. The executable is replaced when no users are accessing the GUI program. There are no changes necessary to this method of installation—local policies and procedures should be followed.

- Citrix Installation:

> The executable is run on a remote workstation and the user views the screen remotely. There are no changes necessary to this method of installation—local policies and procedures should be followed.

- CPRS Launcher:

> Many users use the CPRS Launcher to launch CPRS. The Launcher is updated by another team. Sites and the CPRS implementation team must coordinate to have the CPRS Launcher updated.

- Manual Install:

> This method is used primarily for debug or emergent situations or for specific testing purposes.

#### Manual Installation

Installation Instructions:

1.  Locate OR_30_608.zip and unzip the file.
2.  Copy the CPRSChart.exe to the appropriate folder. You may need to create this new folder.  
    NOTE: A user may need to have Administrator rights to execute these steps.
3.  Create a Shortcut and name it “CPRS v33SWD”.

![](or-3-0-608-cprs-v33swd-deployment-installation-back-out-and-rollback-guide/002.png)

4.  Copy the borlandmm.dll file into the same folder as cprschart.exe. This file should be in the same folder as the CPRSChart.exe for CPRS v33SWD.
5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  On the CPRS v33SWD icon, right-click and select “Properties.”
8.  In the CPRS v33SWD Properties window, do the following:
    1.  Make sure the Shortcut folder is highlighted.
    2.  In the Target field, enter the IP and RPC port (or use ServerList.exe).

![](or-3-0-608-cprs-v33swd-deployment-installation-back-out-and-rollback-guide/003.png)

<span id="_Toc161997245" class="anchor"></span>Figure : Example of the Target Field

In Error! Not a valid bookmark self-reference., the server and port number are not real and are for example only.

### DLL Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v33SWD does NOT redistribute the Vitals DLL, GMV_VitalsViewEnter.dll.

> **IMPORTANT:** Installers MUST copy each site’s current version of the Vitals DLL into the folder where the updated CPRS executable was placed.

The Mental Health DLL (version 1.0.5.16) distributed with CPRS v33SWD should be copied into the same folder as the CPRS executable.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, ensure that you have the updated version of CPRS by checking the splash screen. The correct GUI version should be CPRS OR\*3.0\*608, v33 SWD. The CRC number should be 329DC1A4.

To verify the VistA installation, use FileMan inquiry to the OPTION (#19) file. When prompted for the option, enter OR CPRS GUI CHART. Ensure the MENU TEXT shows the CPRS Chart version as 1.33.109.1.

NAME: OR CPRS GUI CHART MENU TEXT: CPRSChart version 1.33.109.1

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Application Coordinators (CACs) will have two tasks after the installation: setting parameters and acting on the post-installation report that identifies any consult or imaging quick orders that have a default value for Clinically Indicated Date (CID) or Date Desired.

Please refer to the [CPRS v33SWD CAC/HIS Guidance and Set-up document](https://dvagov.sharepoint.com/sites/vhaihpcprs/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2Fvhaihpcprs%2FShared%20Documents%2FCPRS%20Version%2033SWD%2FIHP%5FCPRS%5F33SWD%5FCAC%5FHIS%5FGuidance%5F%20and%5FSet%2Dup%2Edocx%20%281%29%2Epdf&parent=%2Fsites%2Fvhaihpcprs%2FShared%20Documents%2FCPRS%20Version%2033SWD) for detailed information.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Remove Locking of the OR CPRS GUI CHART Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message to the CACs: Once any/all post-install configuration and testing has been completed and you are ready for at-large users to use CPRS, let VistA Applications Support know that the locking can be removed.

VistA Applications Support - To remove the locking and have CPRS GUI opened by all users:

1.  At the Systems Manager Menu Option prompt, type Menu Management and press \<Enter\>. 
9.  At the Select Menu Management Option prompt, type Edit Options and press \<Enter\>.
10. At the Select OPTION to edit prompt, type OR CPRS GUI CHART and press \<Enter\>.
11. At the NAME prompt, it should read OR CPRS GUI CHART. Accept the name by pressing \<Enter\>.
12. At the MENU TEXT prompt, it should read CPRSChart version 1.33.109.1. Accept the menu text by pressing \<Enter\>.
13. At the PACKAGE prompt, press \<Enter\>.
14. At the OUT OF ORDER MESSAGE prompt, press \<Enter\>.
15. At the LOCK prompt, type @ to remove the OR CPRS TESTER and press \<Enter\>.
16. At the SURE YOU WANT TO DELETE? prompt, type YES and press \<Enter\>.

\<CPM\> Select Systems Manager Menu Option: MENU MANagement

          Edit options

          Key Management ...

          Secure Menu Delegation ...

          Restrict Availability of Options

          Option Access By User

          List Options by Parents and Use

          Fix Option File Pointers

          Help Processor ...

   OPED   Screen-based Option Editor

          Display Menus and Options ...

          Menu Rebuild Menu ...

          Out-Of-Order Set Management ...

          See if a User Has Access to a Particular Option

          Show Users with a Selected primary Menu

\<CPM\> Select Menu Management Option: EDIT OPtions

Select OPTION to edit: OR CPRS GUI CHART       CPRSChart version 1.33.109.1

NAME: OR CPRS GUI CHART//

MENU TEXT: CPRSChart version 1.33.109.1  Replace

PACKAGE:

OUT OF ORDER MESSAGE:

LOCK: OR CPRS TESTER// @

SURE YOU WANT TO DELETE? YES

REVERSE/NEGATIVE LOCK: ^

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a catastrophic failure, the Area Manager will discuss with site personnel, product support, patient safety, and the CPRS development team the possibility of backing out the patch and rollback of any necessary database changes. However, the Area Manager will make the final decision about backout and rollback.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out of CPRS GUI is intended to return the VistA system to a running state and permit the use of the previously nationally released version of CPRS GUI. The back-out strategy for CPRS v33SWD is to take the affected VistA system back to using CPRS GUI v32c (1.32.515.2).

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites should consider how backing out CPRS v33SWD might affect the system.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS SQA team tested the CPRS v33SWD software. Test sites will verify that the changes in CPRS also function correctly.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because CPRS is used by clinical staff on a regular basis, backing out CPRS v33SWD should only be considered as a result of a catastrophic error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks are based on the amount of time CPRS v33SWD has been operational.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ultimate authority for backing out CPRS v33SWD lies with the Area Manager.

## Back-Out Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS development team will provide a backout KIDS build to the HISM personnel that will perform the backout steps. Members of the development team will be on hand during the backout. The backout build filename is:

CPRS_V33SWD_COMBINED_BUILD_BACKOUT.KID

To backout the GUI, HISM personnel responsible for deploying the GUI will need to push out the CPRS v32c executable to the locations used by that facility (i.e., VACS servers, Citrix servers, desktops, CPRSLauncher).

Installation Instructions:

1.  From the Kernel Installation and Distribution menu, select the Installation menu.
2.  From this menu, choose to Load a Distribution and enter the location of the Host File CPRS_V33SWD_COMBINED_BUILD_BACKOUT.KID.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. When prompted for the INSTALL NAME, enter CPRS V33SWD COMBINED BUILD 1.0. NOTE: A backout build of CPRS GUI has the same INSTALL NAME as the software being backed out.
1.  Backup a Transport Global - Do not backup the transport global.
2.  Compare Transport Global to Current System – Optional, but not required during a backout.
3.  Verify Checksums in Transport Global – Optional, but not required during a backout.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond NO.
8.  If prompted ‘Delay Install (Minutes): (0 – 60): 0//’, respond 0.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once CPRS v33SWD has been backed out, to verify that the back-out was successful:

Check the OPTION (#19) file for option OR CPRS GUI CHART and ensure the version is set to v32c 1.32.515.2.

1.  In VistA, use FileMan Inquire to check the OPTION (#19) file entry OR CPRS GUI CHART and ensure that the MENU TEXT field reflects version number 1.32.515.2
9.  Launch the CPRS GUI, make sure that it properly connects to VistA, and verify that it is version v32c 1.32.515.2 (Help \| About).

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will automatically rollback data that needs to be rolled back.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A