---
title: OR*3.0*405 (CPRS v32b) Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: (CPRS v32b)
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*405
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
  - install
  - patch
  - deployment
  - rollback
  - options
page_count: 0
word_count: 5797
section_count: 34
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2022
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_405_dibr_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_405_dibr_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_top" class="anchor"></span>CPRS v32b (OR\*3.0\*405)

  Deployment, Installation, Back-Out, and Rollback Guide (DIBOR)
---

![](or-3-0-405-cprs-v32b-deployment-installation-back-out-and-rollback-guide/001.png)

September 2022

Office of Information and Technology (OI&T)

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

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
    - [Site Preparation](#site-preparation)
  - [Resources](#resources)
    - [Software](#software)
    - [Communications](#communications)
- [Pre-Installation Steps](#pre-installation-steps)
  - [Backup Procedures](#backup-procedures)
  - [Locking General User Access to CPRS GUI](#locking-general-user-access-to-cprs-gui)
    - [Assigning the OR CPRS TESTER Key](#assigning-the-or-cprs-tester-key)
    - [Locking the OR CPRS GUI CHART Option](#locking-the-or-cprs-gui-chart-option)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation](#installation-1)
    - [Mandatory Pre-Installation Sequence](#mandatory-pre-installation-sequence)
    - [Mandatory Installation Sequence](#mandatory-installation-sequence)
  - [Installation Procedure(s) for 32b software](#installation-procedures-for-32b-software)
    - [PSS\1\187](#pss1187)
    - [XU\8\662](#xu8662)
    - [CPRSV32BCOMBINEDBUILD.KID](#cprsv32bcombinedbuildkid)
    - [OR\3.0\405.zip](#or30405zip)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Post-Installation](#post-installation)
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
The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) application package. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.
This document describes how to deploy and install CPRS v32b, which includes several patches in a combined build, two independent patches, and a graphical user interface (GUI) executable. It also describes how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CPRS v32b will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies the resources, communications plan, and rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32b requires a fully patched VistA system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32b has a combined multi-patch build (a Kernel Installation and Distribution System or KIDS build), two individual builds and a GUI executable. The builds are installed on the server and the executable can be placed on individual workstations, a VA Application Consolidated Server (VACS), and/or a Citrix server.

CPRS v32b is 508 compliant and uses the same security measures as VistA. Users will authenticate using either their Personal Identification Verification (PIV) card or access and verify codes.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table>
<caption><blockquote>
<p>Table : Deployment/Installation/Back-Out Checklist</p>
</blockquote></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 29%" />
<col style="width: 14%" />
<col style="width: 36%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
<th><strong>Project Phase (See Schedule)</strong></th>
</tr>
<tr class="odd">
<th></th>
<th>Pharmacy Administrator</th>
<th>Pre-Installation</th>
<th>Ensure that all immunization lot numbers have been entered into the system before CPRS v32b is installed. See Section 4 - Pre-Installation Steps.</th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th>CPRS Implementation Team</th>
<th>Deployment</th>
<th>Create an overall deployment schedule</th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th>CPRS Implementation Team</th>
<th>Deployment</th>
<th>Determine and document the roles and responsibilities of those involved in the deployment.</th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th>CPRS Software Quality Assurance (SQA) team and field test sites</th>
<th>Deployment</th>
<th>Test for operational readiness.</th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th>Application Coordinators</th>
<th><p>Release</p>
<p>Deployment</p></th>
<th>Review patches for release readiness and release patches for deployment.</th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th>ITOPS and Local sites</th>
<th>Installation</th>
<th>Based on deployment waves agreed upon with the CPRS implementation team, ITOPS coordinates specific dates and times with sites, VISNs.<br />
ITOPS will perform the actual installation.</th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th>Sites</th>
<th>Installation</th>
<th>Ensure authority to operate and that certificate authority security documentation is in place.</th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th>CPRS Implementation Team</th>
<th>Installation</th>
<th>Provide support, as needed, for installation.</th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th>CPRS Implementation Team</th>
<th>Training</th>
<th>Provide national installation and train-the-trainer presentations. Other groups may also provide training.</th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th>CPRS Implementation Team, ITOPS, and Area Manager</th>
<th>Back-out</th>
<th>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).</th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th>CPRS Implementation Team, Product Support, and CPRS sustainment teams.</th>
<th>Post Deployment</th>
<th>Software Support will be provided by the CPRS Implementation Team during warranty period, which is 90 days after national release. Support then changes to the normal ticketing process.</th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Table : Deployment/Installation/Back-Out Checklist

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment will be a staggered or wave release consisting of three waves lasting a total of 45 days.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for 45 days following national release, as depicted in the deployment schedule on the CPRS v32b SharePoint.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v32b bundle of patches and the accompanying GUI executable will be deployed to all VistA instances. The patches will be installed on the server and the GUI executable will be installed on a VACS server, a Citrix server, or on local workstations or on a combination of them, depending on how the site is set up.

This section discusses the locations that will receive the CPRS v32b deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32b will be deployed to all VistA instances. There is a server component and a GUI executable.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

Table 2: Site Preparation

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
|                |                           |                                             |                   |           |
|                |                           |                                             |                   |           |
|                |                           |                                             |                   |           |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional resources are required.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32b requires a fully patched VistA System for installation.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For national release, sites will receive communication that the release has occurred, which will normally be an Action Item or Bulletin.

Sites will use their internal communications to let their users know about upcoming installations and any associated downtime. This is critical as users can often slow the installation process if they are on the system while installers are trying to get the software installed.

Clinical Application Coordinators (CACs), installers, and other site personnel (as determined by the site) will need to coordinate installation dates and times. In addition, other support personnel need to be consulted – such as the Citrix support, Client Technologies (if required).

#### Deployment/Installation/Back-Out Checklist

Table [3](#deployment) captures the coordination effort and documents the day/time when each activity (deploy, install, back-out) is completed for a project. It also lists the individual who performed the task.

| Activity | Day | Time | Individual who completed task |
|--------------|---------|----------|-----------------------------------|
| Deploy       |         |          |                                   |
| Install      |         |          |                                   |
| Back-Out     |         |          |                                   |

# Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before this installation proceeds, several steps need to be accomplished. Many of these steps need to be done by CACs, Information Technology Operations and Support (ITOPS), and other groups. Once those setup items are completed, installation can proceed.

Refer to the CPRS v32b Setup Guide for pre-installation steps.

> **WARNING:** In CPRS v32b, a user must select a lot number from a pre-populated list when documenting a VA-administered immunization. A pharmacy administrator must populate the immunization lots BEFORE CPRS v32b is installed. If the lots are not pre-populated, a user will not be able to document VA-administered immunizations in CPRS.

> For more information on how to pre-populate vaccine lots, refer to Sections 6.2 (‘LOT Immunization Lot Add/Edit/Display’) and 6.3 (‘Key Concepts’) in the Patient Care Encounter (PCE) User Manual on the [VA Software Document Library (VDL)](http://www.va.gov/vdl).

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps must be taken just in case the CPRS v32b release needs to be backed out.

Backup Instructions:

1.  Use your standard procedure to back up the following globals (for example, using a Linux utilities menu, or entering D GOGEN^%ZSPECIAL, or D ^%GOGEN in programmer mode):
    1.  ^PXRMD(801.41
    2.  ^ORD(101.41

> NOTE: Make sure to backup each global to its own file.

## Locking General User Access to CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user launches the CPRS GUI, the underlying VistA system checks to see if the user has access to the OR CPRS GUI CHART entry in the OPTION (#19) file. If the user has access to the option, they can continue opening the CPRS GUI. Locking an option with a security key is a long-standing VistA feature that is applied to the usage of OR CPRS GUI CHART, released previously under CPRS v32a.

The ability to run the CPRS GUI can be restricted by adding the OR CPRS TESTER security key to the OR CPRS GUI CHART entry’s LOCK (#3) field in the OPTION (#19) file. The primary benefit of restricting access to CPRS GUI is reducing the potential for errors from users accessing the software before post-installation configuration has completed. 

When the lock is activated in a VistA system, only users who hold either the OR CPRS TESTER or XUPROGMODE security keys will be able to launch the CPRS GUI against that VistA system. Until the lock is deactivated, all other users who attempt to launch the CPRS GUI in that VistA system will receive an “option is locked” error message. Since option locking is a VistA feature, locking access to OR CPRS GUI CHART in a test VistA system has no effect on a user’s ability to access OR CPRS GUI CHART in a production VistA system.

> **IMPORTANT:** Prior to installing CPRS v32b, facility staff must create a list of users to whom the OR CPRS TESTER key shall be assigned. Typically, this would be informatics staff involved with testing and configuring a new version of CPRS GUI. These names will be used in section 4.2.1- Assigning the OR CPRS TESTER Key.

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

Select OPTION to edit: OR CPRS GUI CHART       CPRSChart version 1.32.220.1

NAME: OR CPRS GUI CHART//

MENU TEXT: CPRSChart version 1.32.220.1  Replace

PACKAGE:

OUT OF ORDER MESSAGE:

LOCK: OR CPRS TESTER

REVERSE/NEGATIVE LOCK: ^

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32b should not require any changes to the current environment. Pre-installation instructions are in section 4.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32b should follow a normal CPRS installation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v32b multi-package build (CPRS_V32B_COMBINED_BUILD.KID) includes several patches that will be installed in the following order:

- TIU\*1.0\*289
- PSO\*7.0\*441
- PXRM\*2.0\*65
- GMRA\*4.0\*51
- GMTS\*2.7\*115
- PX\*1.0\*217
- PSB\*3.0\*93
- OR\*3.0\*405
- PSJ\*5.0\*399
- YS\*5.01\*211

The contents of the OR\*3.0\*405 ZIP files and CPRS V32B COMBINED BUILD KID file are listed below:

<table style="width:100%;">
<colgroup>
<col style="width: 45%" />
<col style="width: 30%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Contents</th>
<th>Retrieval Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR_30_405.ZIP</td>
<td><p>CPRSChart.exe</p>
<p>YS_MHA_A_XE10.dll</p>
<p>RoboEx32.dll</p>
<p>borlndmm.dll</p>
<p>CPRSChart.map</p>
<p>HELP Directory</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>OR_30_405_SRC.ZIP</td>
<td>CPRS v32b Source</td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>CPRS_V32B_COMBINED_BUILD.KID</td>
<td>CPRS V32B COMBINED</td>
<td>ASCII</td>
</tr>
</tbody>
</table>

The CPRS v32b files can be downloaded using the following steps:

1.  Go to REDACTED.
2.  Download the following:
    1.  PSS_1_187.KID
    2.  XU_8_662.KID
    3.  CPRS_V32B_COMBINED_BUILD.KID
    4.  OR_30_405.zip

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Clinical Application Coordinators (CACs) will be available for configuration and troubleshooting.
- ITOPS installer with programmer access is available.

## Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation sequences must be installed in the order listed in sections 5.8.1 through 5.8.4.2.

### Mandatory Pre-Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. Pre-installation instructions are in section 4.

### Mandatory Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These files must be installed in the following order. Detailed instructions are in section 5.8.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>PSS*1*187</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol start="2" type="1">
<li><p>XU*8*662</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li><p>CPRS_V32B_COMBINED_BUILD.KID</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li><p>OR_30_405</p></li>
</ol></td>
</tr>
</tbody>
</table>

> **WARNING:** Do not queue the installation. A queued installation will generate an error and will not successfully complete.

> **NOTE:** If CPRS v32b gets installed before your site installs GMRV\*5.0\*40, you will see this message during the initial Options installation:  
RPC GMV WEIGHT ALERT in Option OR CPRS GUI CHART \*\*NOT FOUND\*\*  
No action is required on your part. This message will not appear if your site installs GMRV\*5.0\*40 before CPRS v32b.

## Installation Procedure(s) for 32b software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PSS\*1\*187

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSS\*1\*187 may be installed with users on the system. However, it is STRONGLY recommended that you install the patch during non-peak hours to minimize system load and any potential disruption to users. This patch should take less than five minutes to install.

This patch contains pre-install code, which will re-index the INDICATIONS FOR USE (#13) and OTHER LANGUAGE INDICATIONS (#14.2) fields of the PHARMACY ORDERABLE ITEM (#50.7) file. The five-minute installation time estimate includes this re-indexing operation.

Installation Instructions:

1.  From the Kernel Installation and Distribution menu, select the Installation menu.
2.  From the Installation menu, select the Load a Distribution option and enter the location of the Host File, PSS_1_187.KID.
3.  From the Installation menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter PSS\*1\*187.
    1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  If prompted with 'Want KIDS to Rebuild Menu Trees Upon Completion of install? NO//', select 'NO'.
6.  When prompted with 'Want KIDS to INHIBIT LOGONs during the install? NO//', select 'NO'. NOTE: This patch does not required logons to be inhibited.
7.  When prompted with 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', select 'NO'.  
    NOTE: This patch does not require any items to be disabled.

### XU\*8\*662

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XU\*8\*662 may be installed with users on the system. However, it is STRONGLY recommended that you install during non-peak hours to minimize system load and any potential disruption to users. Excluding the background job described below, this patch should take less than five minutes to install.

This patch contains post-installation cod,e which creates a background job to establish the New Style ‘PAR’ cross reference in the ALERT TRACKING (#8992.1) file. The time for this job to complete will vary with the number of entries in ALERT TRACKING. The expected run time can be anywhere from a few hours up to two days. Upon successful completion, the background job will send a VistA MailMan message to the person who installed the patch. If the background job is unsuccessful, it will send a VistA MailMan message to the installer and several members of the CPRS development team.

Example of successful completion message sent to installer:

Subj: XU\*8.0\*662 post install has run to completion.  \[#285646\] 07/21/22@09:25

5 lines

From: PATCH XU\*8.0\*662  In 'IN' basket.   Page 1  \*New\*

-------------------------------------------------------------------------------

Creation of 'PAR' X-Ref for ALERT TRACKING file Started Jul 21, 2022@09:25:07.

Creation of 'PAR' X-Ref Completed

Background Task Finished Jul 21, 2022@09:25:07.

 

Example of an error message sent to installer:

Subj: XU\*8.0\*662 post install has run to completion.  \[#285648\] 07/21/22@09:26

8 lines

From: PATCH XU\*8.0\*662  In 'IN' basket.   Page 1  \*New\*

-------------------------------------------------------------------------------

Creation of 'PAR' X-Ref for ALERT TRACKING file Started Jul 21, 2022@09:26:43.

Creation of 'PAR' X-Ref Completed With Errors

Background Task Finished Jul 21, 2022@09:26:43.

 

The CPRS Development team has already been contacted to assist with the errors

You will be contacted as soon as possible by a CPRS Developer

Installation Instructions:

1.  From the Kernel Installation and Distribution menu, select the Installation menu.
2.  From this menu, choose the Load a Distribution option and enter the location of the Host File, XU_8_662.KID.
3.  From the Installation menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter XU\*8\*662.
    1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of install? NO//', select 'NO'.
6.  When prompted with 'Want KIDS to INHIBIT LOGONs during the install? NO//', select 'NO'.  
    NOTE: This patch does not require logons to be inhibited.
7.  When prompted with 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', select 'NO'.  
    NOTE: This patch does not require any items to be disabled.

### CPRS_V32B_COMBINED_BUILD.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS_V32B_COMBINED_BUILD.KID should not be installed with users on the system. It is recommended that you install it during non-peak hours to minimize potential disruptions to users. This patch should take less than twenty minutes to install.

> **WARNING:** Do not queue the installation. A queued installation will generate an error and will not successfully complete.

Several of the patches in the combined build have pre-installation code, post-installation code, or both. Some of the patches initiate background jobs to complete these tasks. The time for any background jobs to complete is not included in the twenty-minute installation estimate. The following is an overview of those activities:

- TIU\*1.0\*289:
  - Pre-installation:
    - Deletes the New Style “VS” cross reference in the TIU DOCUMENT (#8925) file.
  - Post-installation
    - Creates a background task that will examine the TIU DOCUMENT file and add any necessary entries to the “VS” cross reference. The installer will receive a VistA MailMan message when the task has completed. The message subject will be:

> \[TIU\*1.0\*289\] TIU "VS" Index Complete for \<site name\>

- PSO\*7.0\*441:
  - Post-Installation:
    - Removes the ^XUTL entry for PSO HIDDEN ACTIONS.
    - Deletes field \#2009 from file OUTPATIENT SITE (#59).
    - Sets the default value for the PSO PARK ON parameter to NO.
    - Enables the PSO LM PAT PREG/LACT DISPLAY protocol.
- PXRM\*2.0\*65:
  - Pre-installation:
    - Disables several options related to Clinical Reminders.
    - Removes Data Dictionaries being updated by the patch.
    - Removes any previous Reminder Exchange files being installed by the patch.
  - Post-installation:
    - Converts existing Reminder Dialog entries to new data structure.
    - Silently installs several Reminder Exchange files.
    - Sets the Edit History for Reminder Computed Findings VA-IMMUNIZATION AND LOCATION LOT INFO and VA-REMINDER DEFINITION.
    - Enables options previously disabled in the during the pre-installation.
- GMRA\*4.0\*51 – None
- GMTS\*2.7\*115 – None
- PX\*1.0\*217:
  - Pre-installation:
    - Removes the Data Dictionaries being updated by the patch.
  - Post-installation:
    - Updates ACR and AH cross references on V SKIN TEST (#9000010.12) file.
    - Sets the parameter values for PXV SKIN TEST READING CPT and PXV IMM INVENTORY ALERTS.
    - Creates the PXV IMM INVENTORY ALERTS mail group.
    - Updates the IMM DEFAULT RESPONSES (#920.05) file for Immunizations and Contraindications/Refusals.
    - Corrects VISIT file Service Categories from HF to H - A problem was discovered where third party software was saving a Visit with a Service Category of “HF”. This value is incorrect and was causing problems in Patient Care Encounter (PCE). While this issue was corrected in 2020, the PX\*1\*217 patch post-install will initiate a background task that will update those past incorrect entries. Those entries that have an incorrect Service Category of “HF” will be changed to “H”. These entries will be logged to ^XTMP("PXVP217-CHFSCAT").
- PSB\*3.0\*93 – None
- OR\*3.0\*405:
  - Pre-installation:
    - Removes several options from ORCM MGMT that will be placed under the new ORCM REPORT/CONV UTILITIES option.
    - Adds OR GTX INDICATIONS to the ORDER DIALOG (#101.41) file.
  - Post-installation:
    - Adds ‘Allergy/Adverse Drug Reaction’ to the ORDER REASON (#100.3) file.
    - Adds/Updates several entries in the ORDER CHECK OVERRIDE REASON (#100.04) file.
    - Updates the ORDER DIALOG (#101.41) file:
      - Updates several prompts in PSH OERR.
      - Adds OR GTX INDICATION prompt to the PSH OERR and PSO SUPPLY.
      - Removes OR GTX DAYS SUPPLY and OR GTX ROUTING prompts from PSJ OR CLINIC OE.
    - Adds options removed from ORCM MGMT into ORCM REPORT/CONV UTILITIES
    - Adds new options to OR VIMMM MENU
    - Sets PARAMETER VALUES for OR IMM REMINDER DIALOG and OR RTN PROCESSED ALERTS
    - Re-indexes the SCHEDULED ALERTS (#100.97) file
- PSJ\*5.0\*399-None
- YS\*5.01\*211:
  - Post=installation:
    - Updates the YS BROKER1 entry in the OPTION (#19) file to 1.0.5.12

Installation Instructions:

1.  From the Kernel Installation and Distribution menu, select the Installation menu.
2.  From the Installation menu, select the Load a Distribution option and enter the location of the Host File, CPRS_V32B_COMBINED_BUILD.KID.
3.  From the Installation menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter ‘CPRS V32B COMBINED BUILD 1.0’.
    1.  Backup a Transport Global -This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted with 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', select ‘NO’.
6.  When prompted with ‘Want KIDS to INHIBIT LOGONs during the install? NO//', select ‘NO’.
7.  When prompted with 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', select ‘NO’.
8.  If prompted with ‘Delay Install (Minutes): (0 – 60): 0//’, select ‘0’.

### OR\*3.0\*405.zip

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR_30_405.zip contains the CPRS GUI executable file and the following DLL files for v32: YS_MHA_A_XE10.dll and RoboEx32.dll for v32. Download the ZIP file and extract all the files in it.

#### CPRS GUI Executable Methods of Installation

Sites are using these four methods to distribute the application:

- Network (shared) Installation:  
  The executable is placed on a network drive, with a shortcut on users’ desktops. The executable is replaced when no users are accessing the GUI program. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Citrix Installation:  
  The executable is run on a remote workstation and the user views the screen remotely. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Manual Install:  
  This method is used primarily for debugging purposes, or for emergency or specific testing situations.

#### Manual Installation

Installation Instructions:

1.  Locate OR_30_405.ZIP and unzip the file.
2.  Copy the CPRSChart.exe to a test directory, for example, REDACTED. You may need to create this new directory.  
    NOTE: A user may need to have Administrator rights to execute these steps.
3.  Create a Shortcut and name it “Test CPRSv32”. That name will give the user another visual cue that this is not the normal CPRS icon.  
    ![](or-3-0-405-cprs-v32b-deployment-installation-back-out-and-rollback-guide/002.png)
4.  Copy the borlandmm.dll file into the same directory as cprschart.exe (for example, REDACTED). This file should be in the same directory as the CPRSChart.exe for CPRS v.32.
5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  On the TestCPRSv32 icon, right-click “Properties”.
8.  In the CPRS V32 Properties window, do the following:
    1.  Make sure the Shortcut folder is highlighted.
    2.  In the Target field, enter the IP and RPC port (or use ServerList.exe).

> Figure : Example of the Target Field

![](or-3-0-405-cprs-v32b-deployment-installation-back-out-and-rollback-guide/003.png)

In Figure 1, the server and port number are fictitious and are for example only.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, you can check that you have the updated version of CPRS by checking the splash screen. The correct GUI version should be CPRS 1.32.220.1. The CRC number should be 4F9470CC.

To verify the VistA installation, use FileMan inquiry to the OPTION (#19) file. When prompted for the option, enter OR CPRS GUI CHART. Ensure the CPRS Chart version is: 1.32.220.1.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Remove Locking of the OR CPRS GUI CHART Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message to the CACs: Once any/all post-install configuration and testing has completed and you are ready for at-large users for use CPRS, let VistA Applications Support know that the locking can be removed.

VistA Applications Support - To remove the locking and have CPRS GUI opened by all users:  

1.  At the Systems Manager Menu Option prompt, type Menu Management and press \<Enter\>. 
9.  At the Select Menu Management Option prompt, type Edit Options and press \<Enter\>.
10. At the Select OPTION to edit prompt, type OR CPRS GUI CHART and press \<Enter\>.
11. At the NAME prompt, it should read OR CPRS GUI CHART. Accept the name by pressing \<Enter\>.
12. At the MENU TEXT prompt, it should read CPRSChart version 1.32.220.1. Accept the menu text by pressing \<Enter\>.
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

Select OPTION to edit: OR CPRS GUI CHART       CPRSChart version 1.32.220.1

NAME: OR CPRS GUI CHART//

MENU TEXT: CPRSChart version 1.32.220.1  Replace

PACKAGE:

OUT OF ORDER MESSAGE:

LOCK: OR CPRS TESTER// @

SURE YOU WANT TO DELETE? YES

REVERSE/NEGATIVE LOCK: ^

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a catastrophic failure, the Area Manager will discuss with site personnel, product support, patient safety representatives, and the development team the possibility of backing out the patch and rollback of any necessary database changes. However, the Area Manager will make the final decision about backout and rollback.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If backing out CPRS v32b becomes necessary, sites can use the build created by the CPRS Development Team to back out the patches and return the system to the pre-installation state. The backout patch ID is CPRS_V32B_COMBINED_BUILD_BACKOUT.KID.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites should consider how backing out CPRS v32b might affect the system. Sites should consult with the development team and support staff.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS SQA team tests the CPRS v32b software prior to distribution. Test sites will verify that the changes in CPRS also function correctly in their environment.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because CPRS is used by clinical staff on a regular basis, backing out CPRS v32b should only be considered because of a catastrophic error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks are based on the amount of time CPRS v32b has been operational.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ultimate authority for backing out CPRS v32b lies with the Area Manager.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To backout the CPRS v32b changes, the CPRS development team will make these backout builds available to sites for installation:

- CPRS_V32B_COMBINED_BUILD_BACKOUT.KID
- XU_8_662_BACKOUT.KID
- PSS_1_187_BACKOUT.KID

To backout the GUI, the ITOPS personnel responsible for deploying the GUI will need to push out the CPRS v32a executable to the locations where the software is located (i.e., VACS servers, Citrix servers, desktops).

Installation Instructions:

1.  Install CPRS_V32B_COMBINED_BUILD_BACKOUT.KID.
2.  Install XU_8_662_BACKOUT.KID.
3.  Install PSS_1_187_BACKOUT.KID.
4.  Restore the globals that were backed up prior to installation:
    1.  ^PXRMD(801.41
    2.  ^ORD(101.41

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the back-out was successful:

1.  Check the OPTION (#19) file for option OR CPRS GUI CHART and ensure the version is set to 1.32.114.1.
2.  Launch the CPRS GUI, make sure that it properly connects to VistA, and verify that it is version 1.32.114.1.

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

N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A