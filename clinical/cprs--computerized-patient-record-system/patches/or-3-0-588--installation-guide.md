---
title: OR*3.0*588 (CPRS v32c) Deployment, Installation, Back-Out and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: (CPRS v32c)
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*588
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - cprs
  - contents
  - installation
  - back
  - rollback
  - chart
  - procedure
  - deployment
  - vista
page_count: 0
word_count: 4203
section_count: 34
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_588_dibr_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_588_dibr_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_top" class="anchor"></span>CPRS v32c (OR\*3.0\*588)

  Deployment, Installation, Back-Out, and Rollback Guide (DIBOR)
---

![](or-3-0-588-cprs-v32c-deployment-installation-back-out-and-rollback-guide/001.png)

October 2023

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
  - [Backup Procedures](#backup-procedures)
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
  - [Installation Procedure(s) for 32c software](#installation-procedures-for-32c-software)
    - [CPRSV32CCOMBINEDBUILD.KID](#cprsv32ccombinedbuildkid)
    - [Lock General User Access to the CPRS GUI](#lock-general-user-access-to-the-cprs-gui)
    - [OR\3.0\588.zip](#or30588zip)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Post-Installation](#post-installation)
  - [Executing the Routine to Remove Erroneous Entries](#executing-the-routine-to-remove-erroneous-entries)
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
This document describes how to deploy and install CPRS v32c, which includes several patches in a combined build, and a Graphical User Interface (GUI) executable. It also describes how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CPRS v32c will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies the resources, communications plan, and rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32c requires a fully patched VistA system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32c has a combined multi-patch build (a Kernel Installation and Distribution System or KIDS build) and a GUI executable. The build is installed on the server and the executable can be placed on individual workstations, a VA Application Consolidated Server (VACS), and/or a Citrix server.

CPRS v32c is 508 compliant and uses the same security measures as VistA. Users will authenticate using either their Personal Identification Verification (PIV) card or access and verify codes.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table>
<caption><blockquote>
<p>Table 3: Deployment/Installation/Back-Out Checklist</p>
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
<th>Based on compliance date, HISM coordinates specific dates and times with sites, VISNs.<br />
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
<th>CPRS Implementation Team</th>
<th>Training</th>
<th>Provide national installation and train-the-trainer presentations. Other groups may also provide training.</th>
<th></th>
</tr>
<tr class="odd">
<th></th>
<th>CPRS Implementation Team, HISM, and Area Manager</th>
<th>Back-out</th>
<th>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).</th>
<th></th>
</tr>
<tr class="header">
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

Table 3: Deployment/Installation/Back-Out Checklist

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32c will be nationally released and will adhere to a forty-five day compliance timeline for site installation.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After CPRS v32c is nationally released, HISM installers will coordinate installation with sites. Because CPRS v32c is less complex than other CPRS releases, it will not follow a wave deployment. Rather, it will follow the normal release process, with a 45-day compliance period for installation.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v32c bundle of patches and the accompanying GUI executable will be deployed to all VistA instances. The patches will be installed on the server and the GUI executable will be installed on a VACS server, a Citrix server, or on local workstations or on a combination of them, depending on how the site is set up.

This section discusses the locations that will receive the CPRS v32c deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32c will be deployed to all VistA instances. There is a server component and a GUI executable.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each site needs to follow standard preparation procedures for a new software release.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional resources are required.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32c requires a fully patched VistA System for installation.

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

# Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no pre-installation steps.

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre-installation instructions are in Section 4.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32c should follow a normal CPRS installation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v32c build includes the following patches:

- OR\*3\*588
- PXRM\*2.0\*82
- TIU\*1.0\*353

The contents of CPRS v32c are listed below:

<table style="width:100%;">
<colgroup>
<col style="width: 45%" />
<col style="width: 29%" />
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
<td>OR_30_588.ZIP</td>
<td><p>CPRSChart.exe</p>
<p>RoboEx32.dll</p>
<p>borlndmm.dll</p>
<p>CPRSChart.map</p>
<p>CRC.TXT</p>
<p>WebView2Loader.dll</p>
<p>HELP Directory</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>CPRS_V32C_COMBINED_BUILD.KID</td>
<td>CPRS V32C COMBINED BUILD</td>
<td>ASCII</td>
</tr>
</tbody>
</table>

> **NOTE:** The Mental Health DLL file is not included in the OR_30_588.zip file. You will need to copy your site’s current version of the Mental Health DLL into the directory/folder where you placed the CPRS executable.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Clinical Application Coordinators (CACs) needs to be available for configuration and troubleshooting.
- An HISM installer with programmer access needs to be available.

## Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation sequences must be installed in the order listed in section 5.7.2.

### Mandatory Pre-Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

### Mandatory Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These files must be installed and distributed in the following order. Detailed instructions are in section 5.8.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p>Install CPRS_V32C_COMBINED_BUILD.KID</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol start="2" type="1">
<li><p>Lock General User Access to the CPRS GUI</p></li>
</ol></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li><p>Distribute the CPRS GUI executable (OR_30_588.zip)</p></li>
</ol></td>
</tr>
</tbody>
</table>

## Installation Procedure(s) for 32c software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CPRS_V32C_COMBINED_BUILD.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS_V32C_COMBINED_BUILD.KID should not be installed with users on the system. It is recommended that you install it during non-peak hours to minimize potential disruptions to users. This patch should take less than five minutes to install.

> **WARNING:** Do not queue the installation. Installation of a CPRS upgrade should not be queued.

> **NOTE:** If CPRS v32c gets installed before your site installs GMRV\*5.0\*40, you will see these messages during the initial Options installation:  
--RPC GMV WEIGHT ALERT in Option OR CPRS GUI CHART \*\*NOT FOUND\*\*  
--RPC GMV WEIGHT CHECK in Option OR CPRS GUI CHART \*\*NOT FOUND\*\*  
No action is required on your part. This message will not appear if your site installs GMRV\*5.0\*40 before CPRS v32c.  
  
If CPRS v32c gets installed before your site installs OR\*3.0\*504, you will see two messages during the initial Options installation:  

--RPC OR GN GET CONFIG in Option OR CPRS GUI CHART \*\*NOT FOUND\*\*  
--RPC OR GN SAVE CONFIG in Option OR CPRS GUI CHART \*\*NOT FOUND\*\*  
No action is required on your part. This message will not appear if your site installs OR\*3.0\*504 before CPRS v32c.

Installation Instructions:

1.  From the Kernel Installation and Distribution menu, select the Installation menu.
2.  From the Installation menu, select the Load a Distribution option and enter the location of the Host File, CPRS_V32C_COMBINED_BUILD.KID.
3.  From the Installation menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter ‘CPRS V32C COMBINED BUILD 1.0’.
    1.  Backup a Transport Global -This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted with 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', select ‘NO’.
6.  When prompted with ‘Want KIDS to INHIBIT LOGONs during the install? NO//', select ‘NO’.
7.  When prompted with 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', select ‘NO’.
8.  If prompted with ‘Delay Install (Minutes): (0-60):0//’, select ‘0’.

### Lock General User Access to the CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user launches the CPRS GUI, the underlying VistA system checks to see if the user has access to the OR CPRS GUI CHART entry in the OPTION (#19) file. If the user has access to the option, they can continue opening the CPRS GUI. Locking an option with a security key is a long-standing VistA feature that is applied to the usage of OR CPRS GUI CHART.

The ability to run the CPRS GUI can be restricted by adding the OR CPRS TESTER security key to the OR CPRS GUI CHART entry’s LOCK (#3) field in the OPTION (#19) file. The primary benefit of restricting access to CPRS GUI is reducing the potential for errors from users accessing the software before post-installation configuration has completed. 

When the lock is activated in a VistA system, only users who hold either the OR CPRS TESTER or XUPROGMODE security keys will be able to launch the CPRS GUI against that VistA system. Until the lock is deactivated, all other users who attempt to launch the CPRS GUI in that VistA system will receive an “option is locked” error message. Since option locking is a VistA feature, locking access to OR CPRS GUI CHART in a test VistA system has no effect on a user’s ability to access OR CPRS GUI CHART in a production VistA system.

> **IMPORTANT:** Prior to installing CPRS v32c, facility staff must create a list of users to whom the OR CPRS TESTER key shall be assigned. Typically, these users would be informatics staff involved with testing and configuring a new version of CPRS GUI. These names will be used in the next section.

#### Lock the OR CPRS GUI CHART Option

> **IMPORTANT:** When the OR CPRS GUI CHART option is locked, it will prevent users from logging into VistA Read-Only (VistARO). To overcome this login restriction, you can contact the Health Systems team and ask them to turn off shadowing before you lock the option.  
  
After the installation, when you remove the lock from the option, you will need to notify the Health Systems team to turn the shadowing on. 

VistA Applications Support—To enact locking and allow only authorized users to open the CPRS GUI:

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

> **NOTE:** When the OR CPRS GUI CHART option is locked, some users’ names will not display in the provider selection box(es) in CPRS.

### OR\*3.0\*588.zip

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR_30_588.zip contains the CPRS GUI executable file and the following DLL files for v32c:

- RoboEx32.dll
- borlndmm.dll
- WebView2Loader.dll (version 1.0.1462.37)

Download the ZIP file and extract all the files in it.

#### CPRS GUI Executable Methods of Installation

Sites are using these four methods to distribute the application:

- Network (shared) Installation:  
  The executable is placed on a network drive, with a shortcut on users’ desktops. The executable is replaced when no users are accessing the GUI program. There are no changes necessary for this method of installation—local policies and procedures should be followed.
- Citrix Installation:  
  The executable is run on a remote workstation and the user views the screen remotely. There are no changes necessary for this method of installation—local policies and procedures should be followed.
- Manual Install:  
  This method is used primarily for debugging purposes, or for emergency or specific testing situations.

#### Manual Installation

Installation Instructions:

1.  Locate OR_30_588.ZIP and unzip all the files into a test directory, for example, C:\cprstest. You may need to create a new directory.  
    NOTE: A user may need to have Administrator rights to execute these steps.
2.  Create a Shortcut and name it “CPRSv32c”. The name will give the user another visual cue that this is not the normal CPRS icon.  
      
    ![](or-3-0-588-cprs-v32c-deployment-installation-back-out-and-rollback-guide/002.png)
3.  Determine the DNS server name or IP address for the appropriate VistA server.
4.  Determine the Broker RPC port for the VistA account.
5.  On the CPRSv32c icon, right-click “Properties”.
6.  In the CPRS V32 Properties window, do the following:
    1.  Make sure the Shortcut folder is highlighted.
    2.  In the Target field, enter the IP and RPC port (or use ServerList.exe).

> Figure 1: Example of the Target Field

![](or-3-0-588-cprs-v32c-deployment-installation-back-out-and-rollback-guide/003.png)

In Figure 1, the server and port number are fictitious and are for example only.

#### DLL Installation

CPRS v32c (OR\*3.0\*588) does not distribute the Mental Health and Vitals DLL.

> **IMPORTANT:** Copy your site’s current version of the Mental Health and Vitals DLL into the directory/folder where you placed the CPRS executable,

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, you can check that you have the updated version of CPRS by checking the splash screen. The correct GUI version should be 1.32.515.2. The CRC should be 4C985928.

To verify the VistA installation, use FileMan inquiry to the OPTION (#19) file. When prompted for the option, enter OR CPRS GUI CHART. Ensure that the MENU TEXT reflects that the CPRS Chart version is: 1.32.515.2.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Executing the Routine to Remove Erroneous Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During testing of CPRS v32c, the Software Quality Assurance (SQA) team discovered erroneous entries in the ‘AC’ and ‘AEVT’ cross-reference on the ORDER file (#100). Because of this discovery, the CPRS team developed a post-install routine that will remove erroneous entries. This post-install routine will support the Order Search option being added to 32c to support conversions to the new Electronic Health Record.

## Remove Locking of the OR CPRS GUI CHART Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message to the CACs: Once any/all post-install configuration and testing has completed and you are ready for at-large users for use CPRS, let VistA Applications Support know that the locking can be removed.

Instructions to VistA Applications Support - To remove the locking and have CPRS GUI opened by all users:  

1.  At the Systems Manager Menu Option prompt, type Menu Management and press \<Enter\>. 
2.  At the Select Menu Management Option prompt, type Edit Options and press \<Enter\>.
3.  At the Select OPTION to edit prompt, type OR CPRS GUI CHART and press \<Enter\>.
4.  At the NAME prompt, it should read OR CPRS GUI CHART. Accept the name by pressing \<Enter\>.
5.  At the MENU TEXT prompt, it should read CPRSChart version 1.32.515.2. Accept the menu text by pressing \<Enter\>.
6.  At the PACKAGE prompt, press \<Enter\>.
7.  At the OUT OF ORDER MESSAGE prompt, press \<Enter\>.
8.  At the LOCK prompt, type @ to remove the OR CPRS TESTER and press \<Enter\>.
9.  At the SURE YOU WANT TO DELETE? prompt, type YES and press \<Enter\>.

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

LOCK: OR CPRS TESTER// @

SURE YOU WANT TO DELETE? YES

REVERSE/NEGATIVE LOCK: ^

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a catastrophic failure, the Area Manager will discuss the possibility of backing out the patch and rolling back any necessary database changes with site personnel, product support, patient safety representatives, and the development team. And then, the Area Manager will make the final decision about backout and rollback.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If backing out CPRS v32c becomes necessary, sites can use the build created by the CPRS Development Team to back out the patches and return the system to the pre-installation state. The backout patch host file is CPRS_V32C_COMBINED_BUILD_515_2_BACKOUT.KID

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Site administrators should consider how backing out CPRS v32c could affect the system and should consult with the development team and support staff.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS SQA team tests the CPRS v32c software prior to distribution. Test sites will verify that the changes in CPRS also function correctly in their environment.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because CPRS is used by clinical staff on a regular basis, backing out CPRS v32c should only be considered because of a catastrophic error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks are based on the amount of time CPRS v32c has been operational.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ultimate authority for backing out CPRS v32c lies with the Area Manager.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To backout the CPRS v32c changes, the CPRS development team will make these backout builds available to sites for installation:

- CPRS_V32C_COMBINED_BUILD_BACKOUT.KID

To backout the GUI, HISM personnel responsible for deploying the GUI will need to push out the CPRS v32b executable to the locations where the software is located (i.e., VACS servers, Citrix servers, desktops).

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the back-out was successful:

1.  Check the OPTION (#19) file for option OR CPRS GUI CHART and ensure the MENU TEXT reflects version 1.32.221.1.
2.  Launch the CPRS GUI, ensure that it properly connects to VistA, and verify that it is version to 1.32.221.1

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