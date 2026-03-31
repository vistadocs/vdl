---
title: CPRS v32.221.1 EMERGENCY GUI (OR*3.0*598) Deployment, Installation, Back-Out, and Rollback Guide (DIBOR)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: EMERGENCY GUI (OR*3.0*598)  (DIBOR)
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: CPRS
patch_ver: 32.221.1
patch_id: CPRS*32.221.1*598
group_key: "CPRS:CPRS:32.221.1"
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
  - emergency
  - back
  - rollback
  - vista
  - chart
  - deployment
page_count: 0
word_count: 4193
section_count: 31
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_598_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_598_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598)

  Deployment, Installation, Back-Out, and Rollback Guide (DIBOR)
---

![](cprs-v32-221-1-emergency-gui-or-3-0-598-deployment-installation-back-out-and-rol/001.png)

March 2023

Office of Information and Technology (OI&T)

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

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
  - [Locking General User Access to CPRS GUI](#locking-general-user-access-to-cprs-gui)
    - [VistA Read Only and Locking CPRS](#vista-read-only-and-locking-cprs)
    - [Assigning the OR CPRS TESTER Key](#assigning-the-or-cprs-tester-key)
    - [Locking the OR CPRS GUI CHART Option](#locking-the-or-cprs-gui-chart-option)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure for CPRS v32.221.1 EMERGENCY GUI (OR\3.0\598) Software](#installation-procedure-for-cprs-v322211-emergency-gui-or30598-software)
    - [OR30598.KID](#or30598kid)
    - [OR30598.ZIP](#or30598zip)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Post-Installation](#post-installation)
  - [Remove Locking of the OR CPRS GUI CHART Option](#remove-locking-of-the-or-cprs-gui-chart-option)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
    - [Back-Out Instructions](#back-out-instructions)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) application package. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.
This document describes how to deploy and install CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598), which includes the OR\*3.0\*598 patch and a graphical user interface (GUI) executable. It also describes how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CPRS v32.221.1 EMERGENCY GUI and patch OR\*3.0\*598 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies the resources, a communications plan, and a rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) requires a fully patched VistA system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) is a single patch build (a Kernel Installation and Distribution System or KIDS build) and a GUI executable. The build is installed on the server and the executable can be placed on individual workstations, on a VA Application Consolidated Server (VACS), on a Cloud Server, or on a Citrix server.

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) is 508 compliant and uses the same security measures as VistA. Users will authenticate using either their Personal Identification Verification (PIV) card or access and verify codes.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table>
<caption><blockquote>
<p>Table : Deployment/Installation</p>
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
<th>CPRS Software Quality Assurance (SQA) team and field test sites</th>
<th>Deployment</th>
<th>Test for operational readiness.</th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th>Application Coordinators</th>
<th><p>Release</p>
<p>Deployment</p></th>
<th>Review patches for release readiness and release patches for deployment.</th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th>Health Infrastructure and Systems Management (HISM) and Local sites</th>
<th>Installation</th>
<th>Based on deployment date, HISM coordinates specific dates and times with sites, VISNs.<br />
HISM will perform the actual installation.</th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th>Sites</th>
<th>Installation</th>
<th>Ensure authority to operate and that certificate authority security documentation is in place.</th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th>CPRS Implementation Team</th>
<th>Installation</th>
<th>Provide support, as needed, for installation.</th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th>CPRS Implementation Team, HISM, and Area Manager</th>
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

Table : Deployment/Installation

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) will be an emergency release and will follow the procedures for an emergency patch. There will be both a graphical user interface (GUI) component and a Kernel Installation & Distribution System (KIDS) file.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is anticipated that CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) will be released as an emergency patch that will need to be installed within 15 days of national release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) and the accompanying GUI executable will be deployed to all VistA instances. The patches will be installed on the server and the GUI executable will be installed on a VACS server, on a Citrix server, in the cloud, or on local workstations or on a combination of them, depending on how the site is set up.

This section discusses the locations that will receive the CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) will be deployed to all VistA instances. There is a server component and a GUI executable.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) does not require any special site preparation.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional resources are required.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) requires a fully patched VistA System for installation.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For national release, sites will receive communication that the release has occurred, which will normally be an Action Item or Bulletin.

Sites will use their internal communications to let their users know about upcoming installations and any associated downtime. This is critical as users can often slow the installation process if they are on the system while installers are trying to get the software installed.

Clinical Application Coordinators (CACs), installers, and other site personnel (as determined by the site) will need to coordinate installation dates and times. In addition, other support personnel need to be consulted – such as the Citrix support, Cloud support, and Client Technologies (if required).

#### Deployment/Installation Checklist

Table [3](#deployment) captures the coordination effort and documents the day/time when each activity (deploy and install) is completed for a project. It also lists the individual who performed the task.

| Activity     | Day | Time | Individual who completed task |
|------------------|---------|----------|-----------------------------------|
| Install OR Patch |         |          |                                   |
| Deploy CPRS GUI  |         |          |                                   |

# Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release should not require any changes to the current environment.

## Locking General User Access to CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user launches the CPRS GUI, the underlying VistA system checks to see if the user has access to the OR CPRS GUI CHART entry in the OPTION (#19) file. If the user has access to the option, they can continue opening the CPRS GUI. Locking an option with a security key is a long-standing VistA feature that is applied to the usage of OR CPRS GUI CHART, released previously under CPRS v32a.

The ability to run the CPRS GUI can be restricted by adding the OR CPRS TESTER security key to the OR CPRS GUI CHART entry’s LOCK (#3) field in the OPTION (#19) file. The primary benefit of restricting access to CPRS GUI is reducing the potential for errors from users accessing the software before post-installation configuration has completed. 

When the lock is activated in a VistA system, only users who hold either the OR CPRS TESTER or XUPROGMODE security keys will be able to launch the CPRS GUI against that VistA system. Until the lock is deactivated, all other users who attempt to launch the CPRS GUI in that VistA system will receive an “option is locked” error message. Since option locking is a VistA feature, locking access to OR CPRS GUI CHART in a test VistA system has no effect on a user’s ability to access OR CPRS GUI CHART in a production VistA system.

> **IMPORTANT:** Prior to installing CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598), facility staff must create a list of users to whom the OR CPRS TESTER key shall be assigned. Typically, this would be informatics staff involved with testing and configuring a new version of CPRS GUI. These names will be used in section 4.1.2 - Assigning the OR CPRS TESTER Key.

### VistA Read Only and Locking CPRS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** If sites choose to lock CPRS GUI as described in this section 4.1, users will also be prevented from accessing VistA Read Only. During the CPRS v32b deployment, it was discovered that locking the CPRS GUI chart option also locked VistA Read Only. This was unexpected and caused problems for sites that were going to use VistA Read Only as their contingency plan for the CPRS downtime.

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

Select OPTION to edit: OR CPRS GUI CHART       CPRSChart version 1.32.221.1

NAME: OR CPRS GUI CHART//

MENU TEXT: CPRSChart version 1.32.221.1  Replace

PACKAGE:

OUT OF ORDER MESSAGE:

LOCK: OR CPRS TESTER

REVERSE/NEGATIVE LOCK: ^

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) should not require any changes to the current environment. Pre-installation instructions are in section 4.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) should follow a normal CPRS installation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598), installers should download the following files:

- OR_30_598.ZIP
- OR_30_598_SRC.ZIP
- OR_30_598.KID

> **NOTE:** The “SRC” zip file is an optional download only used by select VAMC facilities and is not required for installation of CPRS GUI.

The contents of the files are listed below:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
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
<td>OR_30_598.ZIP</td>
<td><p>CPRSChart.exe</p>
<p>RoboEx32.dll</p>
<p>borlndmm.dll</p>
<p>CPRSChart.map</p>
<p>CRC.TXT YS_MHA_A_XE10.dll HELP Directory</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>OR_30_598_SRC.ZIP</td>
<td>CPRS 32.221.1 Source</td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>OR_30_598.KID</td>
<td>CPRS Version Update</td>
<td>ASCII</td>
</tr>
</tbody>
</table>

The DLLs, YS_MHA_A_XE10.dll, RoboEx32.dll, borlndmm.dll, and the Help content were not changed since CPRS v32b (version 220.1, OR\*3.0\*405) was released, but they are included in the downloaded files. However the Vitals DLL is not. Someone will need to Copy your site’s current version of the Vitals DLL into the directory/folder where you placed the CPRS executable. The current version is GMV_VitalsViewEnter.dll version 5.0.43.2. This is covered in section [5.7.2.3 DLL Installation](#dll-installation).

The CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) files can be downloaded using the following steps:

1.  Download the CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) host file using the following path: /srv/vista/patches/SOFTWARE/OR_30_598.KID
2.  To download the documentation and other files, such as the GUI executable, use the following location: https://download.vista.med.va.gov/index.html/SOFTWARE

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Clinical Application Coordinators (CACs) will be available for configuration, testing, and troubleshooting.
- HISM installer with programmer access is available.

## Installation Procedure for CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### OR_30_598.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR_30_598.KID should not be installed with CPRS users on the system. It is recommended that you install it during non-peak hours to minimize potential disruptions to users. This patch should take less than 5 minutes to install.

> **WARNING:** Do not queue the installation. Installation of a CPRS upgrade should not be queued.

Installation Instructions:

1.  From the Kernel Installation and Distribution menu, select the Installation menu.
2.  From the Installation menu, select the Load a Distribution option and enter the location of the Host File, /srv/vista/patches/SOFTWARE/OR_30_598.KID.
3.  From the Installation menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter ‘OR\*3.0\*598’.

> **NOTE:** For this release of CPRS, creating a backup build is required.

1.  Backup a Transport Global - Create a complete backup Build that will include any/all files, fields, routines, components, etc.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted with 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', select ‘NO’.
6.  When prompted with ‘Want KIDS to INHIBIT LOGONs during the install? NO//', select ‘NO’.
7.  When prompted with 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', select ‘NO’.
8.  If prompted with ‘Delay Install (Minutes): (0 – 60): 0//’, select ‘0’.

### OR_30_598.ZIP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR_30_598.ZIP contains the CPRS GUI executable file and the following DLL files for CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598): YS_MHA_A_XE10.dll, RoboEx32.dll, and Borlndmm.dll for CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598). Download the ZIP file and extract all the files in it.

#### CPRS GUI Executable Methods of Installation

> **NOTE:** CPRS works with the RPC Broker client to auto select the correct PIV certificate, so the selection dialog no longer displays. However, if there are multiple certificates on a machine, the wrong one may be auto selected. To alleviate this issue, add SHOWCERTS to the end of the CPRS Shortcut properties’ Target field of the CPRS Shortcut as shown below. SHOWCERTS will force the display of the certificate selection window.

> Figure 1: Example of the Target Field with SHOWCERTS

![](cprs-v32-221-1-emergency-gui-or-3-0-598-deployment-installation-back-out-and-rol/002.png)

Sites are using these methods to distribute the application:

- Network (shared) Installation:  
  The executable is placed on a network drive, with a shortcut on users’ desktops. The executable is replaced when no users are accessing the GUI program. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Citrix Installation:  
  The executable is run on a remote workstation and the user views the screen remotely. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Manual Install:  
  This method is used primarily for debugging purposes, or for emergency or specific testing situations.

#### Manual Installation

Installation Instructions:

1.  Locate OR_30_598.ZIP and unzip the file.
2.  Copy the CPRSChart.exe to the appropriate directory. You may need to create this new directory.  
    NOTE: A user may need to have Administrator rights to execute these steps.
3.  Create a Shortcut and name it “CPRS 32.221.1”. That name will give the user another visual cue that this is not the normal CPRS icon.  
    ![](cprs-v32-221-1-emergency-gui-or-3-0-598-deployment-installation-back-out-and-rol/003.png)
4.  Copy the DLL files into the same directory as cprschart.exe. This file should be in the same directory as the CPRSChart.exe for CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598).
5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  On the CPRS 32.221.1 icon, right-click “Properties”.
8.  In the CPRS 32.221.1 EMERGENCY GUI (OR\*3.0\*598) Properties window, do the following:
    1.  Make sure the Shortcut folder is highlighted.
    2.  In the Target field, enter the IP and RPC port (or use ServerList.exe).

> Figure : Example of the Target Field

![](cprs-v32-221-1-emergency-gui-or-3-0-598-deployment-installation-back-out-and-rol/004.png)

In Figure 1, the server and port number are fictitious and are for example only.

#### DLL Installation

CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) does NOT distribute the Vitals DLL.

> **IMPORTANT:** Copy your site’s current version of the Vitals DLL into the directory/folder where you placed the CPRS executable. The current version is GMV_VitalsViewEnter.dll version 5.0.43.2.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, you can check that you have the updated version of CPRS by checking the splash screen. The correct GUI version should be CPRS 1.32.221.1. The CRC number should be 1036EC12.

To verify the VistA installation, use FileMan inquiry to the OPTION (#19) file. When prompted for the option, enter OR CPRS GUI CHART. Ensure the CPRS Chart version is: 1.32.221.1.

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

A message to the CACs: Once any/all post-install configuration and testing has completed and you are ready to let at-large users into CPRS, let VistA Applications Support know that the locking can be removed.

VistA Applications Support - To remove the locking and have CPRS GUI opened by all users:  

1.  At the Systems Manager Menu Option prompt, type Menu Management and press \<Enter\>. 
9.  At the Select Menu Management Option prompt, type Edit Options and press \<Enter\>.
10. At the Select OPTION to edit prompt, type OR CPRS GUI CHART and press \<Enter\>.
11. At the NAME prompt, it should read OR CPRS GUI CHART. Accept the name by pressing \<Enter\>.
12. At the MENU TEXT prompt, it should read CPRSChart version 1.32.221.1. Accept the menu text by pressing \<Enter\>.
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

Select OPTION to edit: OR CPRS GUI CHART       CPRSChart version 1.32.221.1

NAME: OR CPRS GUI CHART//

MENU TEXT: CPRSChart version 1.32.221.1  Replace

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

If backing out CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) becomes necessary, sites can use the backout Packman build created during installation to back out the patch, edit the OR CPRS GUI Chart option, and restore the previous GUI executable to return the system to the pre-installation state.

### Back-Out Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Install the PackMan backout build created during installation.
2.  Edit the MENU TEXT of the OR CPRS GUI CHART VistA option – the text should be updated to read “CPRSChart version 1.32.220.1”. See example that follows
3.  Make the previous executable, CPRS GUI v32b, 1.32.220.1, available.

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

Select OPTION to edit: OR CPRS GUI CHART       CPRSChart version 1.32.221.1

NAME: OR CPRS GUI CHART//

MENU TEXT: CPRSChart version 1.32.221.1 Replace 221.1 With 220.1

Replace

CPRSChart version 1.32.220.1

PACKAGE: ^

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites should consider how backing out CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) might affect the system. Sites should consult with the development team and support staff.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS SQA team tests the CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) software prior to distribution. Test sites will verify that the changes in CPRS also function correctly in their environment.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because CPRS is used by clinical staff on a regular basis, backing out CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) should only be considered because of a catastrophic error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks are based on the amount of time CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) has been operational.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ultimate authority for backing out CPRS v32.221.1 EMERGENCY GUI (OR\*3.0\*598) lies with the Area Manager.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the back-out was successful:

1.  Check the OPTION (#19) file for option OR CPRS GUI CHART and ensure the version is set to 1.32.220.1.
2.  Launch the CPRS GUI, make sure that it properly connects to VistA, and verify that it is version 1.32.220.1.

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