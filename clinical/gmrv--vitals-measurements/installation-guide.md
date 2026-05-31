---
title: GMRV*5*38 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: null
app_code: GMRV
app_name: Vitals/Measurements
section: CLI
app_status: active
pkg_ns: GMRV
patch_ver: 5
patch_id: GMRV*5*38
group_key: GMRV:GMRV:5
file_numbers: []
security_keys: []
menu_options: 0
description: '| Date | Description | Author | |------------|-----------------|------------------------------------| | April 2019 | Initial Release | REDACTED'
audience: System administrators performing installation
keywords: []
page_count: 0
word_count: 4460
section_count: 31
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: April 2019
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/GMRV_5_0_P38_IG.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/GMRV_5_0_P38_IG.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=107
audit_applied: '2026-05-31'
master_source: GMRV*5*38 Installation Guide
master_pub_date: April 2019
consolidated_from: 6 versions
prior_versions:
- GMRV*5*22 Installation Guide
- GMRV*5*23 Installation Guide
- GMRV*5*3 Installation Guide
- GMRV*5*36 Installation Guide
- GMRV*5*37 Installation Guide
consolidated_title: installation guide
---

![](gmrv-5-38-installation-guide/001.png)

April 2019

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date       | Description     | Author                             |
|------------|-----------------|------------------------------------|
| April 2019 | Initial Release | <span class="mark">REDACTED</span> |

<span id="_Toc6404072" class="anchor"></span>Table 1: Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software and should be structured appropriately to reflect these procedures.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Guide is to be completed prior to Critical Decision Point \#2 (CD \#2). The expectation is that this document will be updated, as needed, throughout the lifecycle of the project.

Table of Contents

List of Tables

List of Figures

[Figure 1: Shortcut Icons for Vitals and Vitals Manager [9](#_Toc6404076)](#_Toc6404076)

[Figure 2: Test Vitals38 Properties [10](#_Toc6404077)](#_Toc6404077)

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
    - [GMRV\5.0\38 VistA Installation](#gmrv5038-vista-installation)
    - [Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 Installation](#vitals-lite-v50383-vitals-v50383-and-vitals-manager-v50383-installation)
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
The Vitals Suite (GMRV\*5.0\*38) consists of Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3. This document describes how to deploy and install Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed commercial off the shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single common document that describes how, when, where, and to whom the Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 will be deployed and installed as well as how they are to be backed out and rolled back. The plan also identifies the resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 projects are for installation on a fully patched VistA system. There are two Graphical User Interface (GUI) components and a Dynamic-Link Library (DLL) that should be running on a Windows system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 and the associated Mumps patches are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 utilize existing nationally released security controls to control access.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No one single entity oversees decision making for deployment, installation, back out and rollback of Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3. The Release Agent and Application Coordinators under the Veterans in Process will approve deployment and install from a product development perspective. If an issue with the software arises, then the Area Managers and other site leadership will meet, along with input from Patient Safety and Health Product Support, to initiate a back out and rollback decision of the software in accordance with the Information Technology (IT) Operations and Services personnel. The following table provides Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 project information.

<table>
<caption><p><span id="_Toc6404073" class="anchor"></span>Table 2: OI Field Offices</p></caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 15%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>Team</th>
<th>Phase / Role</th>
<th>Tasks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IT Operations and Services personnel</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
</tr>
<tr class="even">
<td>IT Operations and Services personnel</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
</tr>
<tr class="odd">
<td>Site personnel.</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="even">
<td><p>IT Operations and Services personnel</p>
<p>The IT support will need to include person(s) to install the Kernel Installation and Distribution System (KIDS) build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</p></td>
<td>Deployment</td>
<td>Execute deployment</td>
</tr>
<tr class="odd">
<td><p>IT Operations and Services personnel.</p>
<p>The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</p></td>
<td>Installation</td>
<td>Plan and schedule installation</td>
</tr>
<tr class="even">
<td>N/A – will work under the VistA authority to operate (ATO) and security protocols.</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
</tr>
<tr class="odd">
<td>N/A – no equipment is being added.</td>
<td>Installation</td>
<td>Validate through facility point of contact (POC) to ensure that IT equipment has been accepted using asset inventory processes</td>
</tr>
<tr class="even">
<td>N/A – no new functionality is being introduced.</td>
<td>Installations</td>
<td>Coordinate training</td>
</tr>
<tr class="odd">
<td>Facility chief information officer (CIO), IT Operations, and Services personnel</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
</tr>
<tr class="even">
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the Health Product Support (HPS) Clinical Sustainment team.</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
</tr>
</tbody>
</table>

<span id="_Toc6404073" class="anchor"></span>Table 2: OI Field Offices

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release, the GMRV\*5.0\*38 patch will be released from the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing and deployment to production will be at the site's discretion. It is anticipated there will be a 30-day compliance period.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific timeline for deployment. This is considered a maintenance release and installation will be at the site's discretion, within the constraints of the compliance period for the release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executables will also be deployed to the Citrix Access Gateway.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to IOC sites for verification of functionality. Once that testing is completed and approval is given for national release, Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 (GMRV\*5.0\*38) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

- Tuscaloosa VA Medical Center
- VA Salt Lake City Health Care System

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3. A fully patched VistA system is the only requirement.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an action item and National Change Order prior to the release of Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 advising them of the upcoming release.

Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch GMRV\*5.0\*38 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 assume a fully-patched VistA system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

\[GUI\] The time to deploy the GUI will depend on which method the site utilizes for running the executables (network share, Citrix, individual workstation installs, etc.).

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 is being released as a PackMan message distributed through the National Patch Module combined with a .ZIP file containing the GUI file(s).

<span class="mark">REDACTED</span>

This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the <span class="mark">REDACTED</span> directory at the following OI Field Offices:

| Location                           | Site                               |
|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

<span id="_Toc6404074" class="anchor"></span>Table 3: Files to be Downloaded

Documentation can also be found on the VA Software Documentation Library at:

<https://www.va.gov/vdl/>

| File Name            | File Contents                                                      | Download Format |
|----------------------|--------------------------------------------------------------------|-----------------|
| GMRV_5_0_P38.ZIP     | GUI Files (Vitals and Vitals Manager executables; Vitals Lite DLL) | Binary          |
| GMRV_5_0_P38_SRC.ZIP | GUI Source Files                                                   | Binary          |

<span id="_Toc6404075" class="anchor"></span>Table 4: HPS Clinical Sustainment Contacts

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 requires the following to install:

- Programmer access to the VistA instance and the ability to install the KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executables to the network share location.
- Individual workstation installs – access/ability to push executables to required workstations.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### GMRV\*5.0\*38 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, must use the \[Backup a Transport Global\] option to create a back out message.
4.  From this menu, the following options may be used:
    - Compare Transport Global to Current System
    - Verify Checksums in Transport Global
5.  Use the Install Package(s) options and select the package GMRV\*5.0\*38
6.  When prompted Want KIDS to INHIBIT LOGONs during the install? NO//, respond NO.
7.  When prompted Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//, respond NO.

### Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the Vitals and Vitals Manager GUI executables and Vitals Lite DLL. Download the ZIP file and extract all the files.

#### Vitals and Vitals Manager GUI Methods of Installation

The following methods of installation of Vitals and Vitals Manager are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/Veterans Integrated Service Network (VISN) policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

> **NOTE:** Vitals Manager is not needed for every user. This is designed for users who are responsible for the management of the Vitals package for this server.

Network (shared) installation:

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executables (Vitals.exe and VitalsManager.exe) across the LAN.

The GUI executables (Vitals.exe & VitalsManager.exe) and help files (VITALS.chm & VITALSMANAGER.chm) are copied to a network shared location. Users are provided with a desktop shortcut to run Vitals.exe & VitalsManager.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the Target field of the shortcut properties.

At the time of a Vitals and/or Vitals Manager version update, the copy of Vitals.exe & VitalsManager.exe and the help files are replaced, on the network share, with the new version.

Any users requiring access to another site's Vitals.exe and/or VitalsManager.exe system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of Vitals.exe or VitalsManager.exe (e.g. for testing purposes), then a different version of Vitals.exe and/or VitalsManager.exe can be placed in a separate network location, and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

Citrix installation:

The GUI executables (Vitals.exe & VitalsManager.exe) and help folder and files (VITALS.chm & VITALSMANAGER.chm) are installed and run from a remote workstation, and the user views the remote workstation's screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary CAG infrastructure).

> **NOTE:** For issues with CAG, please contact the local or national help desk.

Local workstation installation:

This is the "standard" method of installation where the GUI executables (Vitals.exe & VitalsManager.exe) and help folder and files (VITALS.chm & VITALSMANAGER.chm) are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via SCCM. This is outside the scope of the Sustainment team. A National package (Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3) has been prepared and made available to Regional COR Client Technologies leadership.

Manual install:

This method is used for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.

1.  Locate the GMRV_5_0_P38.ZIP and unzip the file.

    Copy the contents of the zip archive (the 2 GUIs and the 2 help files) to a test directory, for example, C:\VitalsTest. A new directory may need to be created.

    Note: Administrator rights are required for the PC used to complete this step.
8.  Create Shortcut(s) and name it/them Test Vitals38 and/or Test VitalsManager38. This is to give the user another visual cue that these are not the normal Vitals icon.

<span id="_Toc6404076" class="anchor"></span>Figure 1: Shortcut Icons for Vitals and Vitals Manager

![](gmrv-5-38-installation-guide/002.png)

9.  Determine the domain name server (DNS) server name or internet protocol (IP) address for the appropriate VistA server.
10. Determine the Broker Remote Procedure Call (RPC) port for the VistA account.
11. Enter the IP (or DNS name) and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

<span id="_Toc6404077" class="anchor"></span>Figure 2: Test Vitals38 Properties

![](gmrv-5-38-installation-guide/003.png)

> Note: The server and port number shown above are for example only.

#### Vitals Lite DLL Methods of Installation

The following methods of installation of Vitals Lite are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

Network (shared) installation:

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the DLL (GMV_VitalsViewEnter.dll) across the network.

The DLL (GMV_VitalsViewEnter.dll) and help file (GMV_VitalsViewEnter.chm) are copied to the network shared location that contains the Computerized Patient Record System (CPRS) executable. Users will access the DLL via CPRS's coversheet.

At the time of a Vitals Lite version update the copy of GMV_VitalsViewEnter.dll and the help file are replaced, on the network share, with the new version. Specifically, the CHM file should replace the existing HLP file.

If a user requires access to an older or newer version of GMV_VitalsViewEnter.dll (e.g. for testing purposes), then a different version of GMV_VitalsViewEnter.dll can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

Citrix installation:

The DLL (GMV_VitalsViewEnter.dll) and help file (GMV_VitalsViewEnter.chm) are installed and run from a remote workstation, and the user views the remote workstation's screen on their local workstation.

For the local site users, this method is similar to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary CAG infrastructure).

> **NOTE:** For issues with CAG, please contact the local or national help desk.

> **NOTE:** In GMRV\*5\*38, the DLL cannot find its help file when both files are in any folder other than the folder with CPRS (CPRSChart.exe). If users require the help file while using Vitals Lite, it will need to be installed in the same folder as CPRS. This is a known bug and pre-dates GMRV\*5\*38. It will be fixed in a future patch.

Local workstation installation:

This is the "standard" method of installation where the Vitals Lite (GMV_ViewEnter.dll) and help file (GMV_VitalsViewEnter.chm) are installed on and run from the user's local workstation.

> **NOTE:** There is a national SCCM package to help sites or ITOPS distribute the Vitals Lite DLL. However, in GMRV\*5\*38, the DLL cannot find its help file when both files are in any folder other than the folder with CPRS (CPRSChart.exe). If users require the help file while using Vitals Lite, it will need to be installed in the same folder as CPRS. This is a known bug and pre-dates GMRV\*5\*38. It will be fixed in a future patch.

Manual install:

Unzip the GMRV_5_0_P38.ZIP file and move the files to an appropriate directory and/or workstation.

Windows 7 & 10:

- For 64-bit machines: C:\Program Files (x86)\Vista\Common Files
- For 32-bit machines: C:\Program Files\Vista\Common FilesNote: The above directories are the standard approach. However, in GMRV\*5\*38, the DLL cannot find its help file when the DLL and help file are in any folder than the folder with CPRS (CPRSChart.exe). If users require the help file while using Vitals Lite, it will need to be installed in the same folder as CPRS. This is a known bug and pre-dates GMRV\*5\*38. It will be fixed in a future patch.
1.  Rename the current version of the DLL (5.0.37.2) to GMV_VitalsViewEnter.dll.bkup.37.
2.  Copy the new version of the DLL (5.0.38.3) into the same folder.
3.  Rename the GMV_VitalsViewEnter.hlp to GMV_VitalsViewEnter.hlp.bkup.37.
4.  Copy the GMV_VitalsViewEnter.chm into the same folder.

To switch between versions, reverse the steps above - rename the current release DLL (5.0.37.2) to GMV_VitalsViewEnter.dll, rename the new version of the DLL (5.0.38.3) to GMV_VitalsViewEnter.dll.bkup.38, rename the current release HLP file to GMV_VitalsViewEnter.hlp, and rename the CHM file to GMV_VitalsViewEnter.chm.bkup.38.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VISTA\] Verify the checksum of routine GMV38PST is equal to the checksum listed on the patch description.

\[GUI\] Launch both the Vitals and Vitals Manager GUIs and verify the splash screen now announces that version 5.0.38.3 is running. Log into the desired server and verify that a version mismatch is not received. Launch the Vitals Lite DLL from within CPRS and verify the About screen now announces that version 5.0.38.3 is running.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] To revert the Vitals and/or Vitals Manager version, re-install patch GMRV\*5.0\*36. To revert the Vitals Lite version, re-install patch GMRV\*5.0\*37.

\[GUI\] To revert the Vitals and/or Vitals Manager GUI(s), the prior GUI(s) would have to be redistributed. For Vitals this is v5.0.36.2 and for Vitals Manager this is v5.0.36.1. To revert the Vitals Lite DLL, the prior DLL (v5.0.37.2) would have to be redistributed.

The HPS Sustainment Clinical team is available to assist with sites that have misplaced their backup PackMan message. They will also give you the instructions on downloading the executables.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3. This was a maintenance release to correct defects discovered in Vitals Lite v5.0.37.2, Vitals v5.0.36.2, and Vitals Manager v5.0.36.1. There was no additional functionality included.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the two test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the third build of GMRV\*5.0\*38. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to the HPS Clinical Sustainment team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the applications and/or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 would result in the re-instatement of the issues that were addressed.

In addition, there is a risk that the process, which would be performed only in an emergency situation, would significantly impact patient care due to the interruption.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3 is in the event of a catastrophic failure.

1.  Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with Vitals Lite v5.0.38.3, Vitals v5.0.38.3, and Vitals Manager v5.0.38.3. Use the following contacts:

| Name & Title                       | Email                              | Telephone Number                   |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

Lists the individuals who should be contacted if this patch needs to be backed-out. It provides their email and phone contact information.

12. If the decision is made to proceed with back-out and rollback, the HPS Sustainment Clinical team will be available to assist sites that have misplaced their backup PackMan message and provide the instructions on downloading the executables.
13. \[VistA\]
1.  Open the Backup MailMan Message
2.  At the Enter message action (in IN basket): Ignore// prompt Enter X for \[Xtract PackMan\]
3.  At the Select PackMan function: prompt select \[INSTALL/CHECK MESSAGE\]. The old routine is now restored.
14. \[GUI\] Coordinate with the appropriate IT support, local and regional, to schedule the time to install GMRV\*5.0\*36 for Vitals and Vitals Manager and GMRV\*5.0\*37 for Vitals Lite, and to push out / install the previous GUI executables and DLL.
15. Once GMRV\*5.0\*36 for Vitals and Vitals Manager and GMRV\*5.0\*37 for Vitals Lite have been installed, verify operations before making available to all staff.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure the v5.0.36.1 and v5.0.36.2 executables and the v5.0.37.2 DLL launch properly.
16. Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

The Facility CIO has the final authority to require the rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will automatically rollback version.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: GMRV*5*36 Installation Guide

### GMRV\*5.0\*36 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, must use the \[Backup a Transport Global\] option to create a back out Patch
4.  Also from this menu, you may elect to use the following options:
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
- Use the Install Package(s) options and select the package GMRV\*5.0\*36
5.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install?" respond NO.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond NO.

### Vitals v5.0.36.2 & Vitals Manager v5.0.36.1 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the Vitals and Vitals Manager GUI executables. Download the ZIP file and extract all the files.

#### Vitals and Vitals Manager GUI Methods of Installation

The following methods of installation for Vitals are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

> <u>Note</u>: Vitals Manager is not needed for every user. This is designed for users who are responsible for the Management of the Vitals package for this server.

- Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executables (Vitals.exe & VitalsManager.exe) across the LAN.

> The GUI executables (Vitals.exe & VitalsManager.exe), and help folder and files (VITALS.HLP & VITALSMANAGER.HLP), are copied to a network shared location. Users are provided with a desktop shortcut to run Vitals.exe and VitalsManager.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the "Target" field of the shortcut properties

> At the time of a Vitals and/or Vitals Manager version update the copy of Vitals.exe and VitalsManager.exe and the help files are simply replaced, on the network share, with the new version.

> Any users requiring access to another site's Vitals.exe and/or VitalsManager.exe system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of Vitals.exe or VitalsManager.exe (e.g. for testing purposes) a different version of Vitals.exe and/or VitalsManager.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

- Citrix installation:

> The GUI executables (Vitals.exe & VitalsManager.exe) and help folder and files (VITALS.HLP & VITALSMANAGER.HLP) are installed and run from a remote workstation, and the user views the remote workstation's screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> <u>Note</u>: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

- Local workstation installation:

  Download the ZIP file and extract all the files.

  GMRV\*5.0\*36 - Vitals & Vitals Manager

  Vitals.exe, VitalsManager.exe and the associated help files will need to be installed in the same directory on workstations.

  <u>Note</u>: There is a national SCCM package to help sites or ITOPS distribute the Vitals and Vitals Manager GUIs.
- Manual install:

  This method is used primarily for advanced users and at testing locations.  
  This method is somewhat changed from that used previously for Windows XP workstations.
1.  Locate the GMRV_5_36.ZIP and unzip the file.
2.  Copy the Vitals.exe and/or VitalsManager.exe to a test directory, for example, C:\VitalsTest. You may need to create this new directory.

    <u>Note</u>: You may need to have a user with Administrator rights complete this step.
3.  Create a Shortcut(s) and name it "Test Vitals36" and/or "Test VitalsManager36". This is to give the user another visual cue that this is not the normal Vitals icon.

    ![](gmrv-5-36-installation-guide/002.png)

> <span id="_Toc505761168" class="anchor"></span>Figure 1: Vitals Icon

4.  Copy the Help folder and its contents (VITALS.HLP & VITALSMANAGER.HLP) into the same directory as CRHDShiftChgHandoff.exe (for example, c:\VitalsTest). This file should be in the same directory Vitals.exe and/or VitalsManager.exe.
5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  Enter IP (or DNS name) and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

> ![](gmrv-5-36-installation-guide/003.png)

> <span id="_Toc505761169" class="anchor"></span>Figure 2: Test Vitals36 Properties Tab

> Example of what the shortcut properties dialog might look like.

> ![](gmrv-5-36-installation-guide/004.png)

> <span id="_Toc505761170" class="anchor"></span>Figure 3: Test VitalsManager36 Properties Tab

> The server and port number shown above are not real and are for example only.

### From: GMRV*5*37 Installation Guide

### GMRV\*5.0\*37 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, must use the \[Backup a Transport Global\] option to create a back out Patch
4.  Also from this menu, you may elect to use the following options:
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
- Use the Install Package(s) options and select the package GMRV\*5.0\*37
5.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
6.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond NO.

### Vitals Lite Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the Lite DLL. Download the ZIP file and extract all the files.

#### Vitals Lite DLL Methods of Installation

The following methods of installation of Vitals Lite are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

> **NOTE:** Vitals Manager is not needed for every user. This is designed for users who are responsible for the Management of the Vitals package for this server.

Network (shared) installation:

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the DLL (GMV_VitalsViewEnter.dll) across the network.

The DLL (GMV_VitalsViewEnter.dll), and help folder and files (GMV_VitalsViewEnter.hlp), are copied to the network shared location that contains the CPRS executable. Users will access the DLL via CPRS's coversheet.

At the time of a Vitals Lite version update the copy of GMV_VitalsViewEnter.dll and the help file are simply replaced, on the network share, with the new version.

If a user requires access to an older or newer version of GMV_VitalsViewEnter.dll (e.g. for testing purposes) a different version of GMV_VitalsViewEnter.dll can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

Citrix installation:

The DLL (GMV_VitalsViewEnter.dlll) and help file (GMV_VitalsViewEnter.) are installed and run from a remote workstation, and the user views the remote workstation's screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

Local workstation installation:

This is the "standard" method of installation where the Vitals Lite (GMV_ViewEnter.dll) and help folder and files (GMV_ViewEnter.HLP) are installed on and run from the user's local workstation.

<u>Note</u>: There is a national SCCM package to help sites or ITOPS distribute the Vitals Lite GUI.

Manual install:

Unzip the GMRV_5_37.ZIP file and move the files to an appropriate directory and/or workstations.

Windows 7:

- For 64 bit machines: "C:\Program Files (x86)\Vista\\Common Files"
- For 32 bit machines: "C:\Program Files\Vista\Common Files"
1.  Rename the current version of the DLL (5.0.34.5) to GMV_VitalsViewEnter.dll.bkup.34.
2.  If not already, rename the new version of the DLL (5.0.37.2) to GMV_VitalsViewEnter.dll.
3.  Both of these files should be in the same folder (see *fig 1*).

> Figure : GMV Manual Install File Names

![](gmrv-5-37-installation-guide/002.png)

To switch between versions, revers the steps above and rename the current release DLL (5.0.34.5) to GMV_VitalsViewEnter.dll and make the new version of the DLL (5.0.37.2) GMV_VitalsViewEnter.dll.BCKUP.37

### From: GMRV*5*23 Installation Guide

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch GMRV\*5.0\*23 contains changes to the Gen. Med. Rec. – Vitals package (aka Vitals/Measurements). The package namespaces are GMRV and GMV.

- This patch includes a Dynamic Link Library (DLL) file. This file is used by CPRS.
- This patch modifies the current Vitals.exe file which is the Graphical User Interface (GUI) for entering patient vitals/measurements data via the Vitals/Measurements package.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents can be downloaded from the VistA Documentation Library (VDL) at <http://www.va.gov/vdl/> under Vitals/Measurements:

- *Vitals/Measurements User Manual 5.0*
- *Vitals/Measurements Release Notes GMRV\*5.0\*23*
- *Vitals/Measurements Technical Manual and Package Security Guide 5.0*
- *Portable Vital Signs Monitors Interface Specifications (October 2005)  
This page intentionally left blank for double-sided printing.*

## M Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following packages and patches must be installed and fully patched for the installation environment:

1.  VA FileMan V. 22 or greater
2.  Kernel V. 8.0 or greater
3.  Kernel Toolkit V. 7.3 or greater
4.  Kernel RPC Broker V. 1.1 or greater
5.  PIMS V. 5.3 or greater
6.  Intake and Output V. 4.0
7.  Health Summary V. 2.7 or greater
8.  Nursing V. 4.0 or greater

## Client Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The client (disk) storage requirements are approximately:

| Type of Data            | Size   |
|-------------------------|--------|
| Vitals.exe              | 1900 k |
| VitalsManager.exe       | 1200 k |
| GMV_VitalsViewEnter.dll | 1500 k |
| VITALS.HLP              | 41 k   |
| VITALSMANAGER.HLP       | 22 k   |
| GMV_VitalsViewEnter.hlp | 36 k   |

The installation environment on the VistA client workstation requires the following:

1.  Workstations must be running Windows NT (V4 or later), Windows 2000, or Windows XP.
9.  Workstations must be connected to the local area network (LAN).
10. 12 megabytes of disk space must be available.
11. RPC Broker Workstation may be installed (optional).

*This page intentionally left blank for double-sided printing.*

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before attempting to install this patch, complete the following steps:

1.  Coordinate the installation with the Clinical Application Coordinator (CAC), package Automated Data Processing Application Coordinator (ADPAC) and Information Resource Management Systems (IRMS).
12. Forward the GMRV\*5.0\*23 patch message from FORUM to your system. The FORUM message contains the KIDS build.
13. Download the VITL5_P23.ZIP file. The following files are included in this ZIP file:

| <u>File Name</u>           | <u>Contents</u>                    | <u>Retrieval Format</u> |
|--------------------------------|----------------------------------------|-----------------------------|
| GMV_VitalsViewEnter.dll        | Dynamic Link Library file              | Binary                      |
| GMV_VitalsViewEnter.hlp        | Help file for DLL                      | Binary                      |
| GMV_VitalsViewEnter.cnt        | Help file TOC for DLL                  | Binary                      |
| VITL5_P23_IG.PDF               | Patch GMRV\*5.0\*23 Installation Guide | Binary                      |
| VITL5_P23_RN.PDF               | Patch GMRV\*5.0\*23 Release Notes      | Binary                      |
| VITL5_P23.EXE                  | Installation Wizard                    | Binary                      |
| VITL5_P23.SRC.ZIP              | Source Code                            | Binary                      |
| VITL5_TM.PDF                   | Technical Manual (all pages)           | Binary                      |
| VITL5_UM.PDF                   | User Manual (all pages)                | Binary                      |
| VITL_5_P23_TM_CHANGE_PAGES.PDF | Technical Manual (change pages)        | Binary                      |
| VITL_5_P23_UM_CHANGE_PAGES.PDF | User Manual (change pages)             | Binary                      |

The preferred method is to FTP the ZIP file from:

<span class="mark">REDACTED</span>

This transmits the ZIP file from the first available FTP server. Sites may also elect to retrieve the ZIP directly from a specific server:

| CIO Field Office                   | FTP Address                        | Directory                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

14. After you have saved the ZIP file, double click on it to "Unzip" it. Highlight all of the files and click the Extract button. Save the files to a directory of your choice.

## M Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The M Server installation must be done before the Client installation.

1.  On the VistA system, set the variables DUZ and DUZ(0) by executing the command  
    D ^XUP. Verify DUZ(0) = @.
15. Load the GMRV\*5.0\*23 KIDS build from the MailMan message.
16. Use the KIDS installation menu option \[XPD MAIN\] and select Installation and then Install Package(s) and select GMRV\*5.0\*23. See the M Server sample installation below for additional information.

Users may remain on the system at the time of installation, though it should be installed when entry of patient vitals data is low. The software should be installed when use of the Vitals/Measurements package is minimal. Follow your facility's policy regarding the rebuilding of the menu trees upon patch completion.

### M Server – sample installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\> D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

KIDS Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option: INSTALLATION

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: GMRV\*5.0\*23 Loaded from Distribution 2/20/08@14:20:03

=\> GMRV\*5\*23

This Distribution was loaded on Feb 20, 2008@14:20:03 with header of

GMRV\*5\*23

It consisted of the following Install(s):

GMRV\*5.0\*23

Checking Install for Package GMRV\*5.0\*23

Install Questions for GMRV\*5.0\*23

Want KIDS to INHIBIT LOGONs during the install? NO// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET

Install Started for GMRV\*5.0\*23 :

Feb 20, 2008@14:20:33

Build Distribution Date: Feb 20, 2008

Installing Routines:

Feb 20, 2008@14:20:33

Installing PACKAGE COMPONENTS:

GMRV\*5.0\*23

────────────────────────────────────────────────────────────────────────────────

Installing REMOTE PROCEDURE

Feb 20, 2008@14:20:33

Running Post-Install Routine: ^GMV23PST

Updating system parameters.

Updating DLL parameter.

Updating Routine file...

Updating KIDS files...

GMRV\*5.0\*23 Installed.

Feb 20, 2008@14:20:33

Install Message sent \#68780

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

## Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The M Server installation must be done before the VistA Client installation.

1.  Double click on the VITL5_P23.exe file in the directory where you placed it. This file is an installation wizard that contains the updated versions for:
- Vitals.exe
- VitalsManager.exe
- Vitals.hlp
- Vitals.cnt
- VitalsManager.hlp
- VitalsManager.cnt
- Roboex32.dll
17. An InstallShield welcome screen opens. Click Next to start the installation.

![Figure 1

18. Several dialog boxes will then quickly flash across the screen before the "Modify, repair or remove the program" dialog box appears.](gmrv-5-23-installation-guide/001.png)

*Figure 1

18. Several dialog boxes will then quickly flash across the screen before the "Modify, repair or remove the program" dialog box appears.*

![Figure 2

19. Select Repair, then click Next. The Install wizard will verify settings and replace all existing files on your workstation with the newer versions. If the installation files are located on the client PC, the installation should complete in less than one minute. Installations over the network may be slower because of server traffic or connectivity issues.](gmrv-5-23-installation-guide/002.png)

*Figure 2

19. Select Repair, then click Next. The Install wizard will verify settings and replace all existing files on your workstation with the newer versions. If the installation files are located on the client PC, the installation should complete in less than one minute. Installations over the network may be slower because of server traffic or connectivity issues.*
20. When all files have been copied, the InstallShield Wizard Complete screen will open. Click Finish to finalize the client installation.

![Figure 3

21. The installation wizard creates the following files:](gmrv-5-23-installation-guide/003.png)

*Figure 3

21. The installation wizard creates the following files:*
- \Program Files\VistA\Vitals\Vitals.exe
- \Program Files\VistA\Vitals\VitalsManager.exe
- \Program Files\VistA\Vitals\Help\Vitals.hlp
- \Program Files\VistA\Vitals\Help\Vitals.cnt
- \Program Files\VistA\Vitals\Help\VitalsManager.hlp
- \Program Files\VistA\Vitals\Help\VitalsManager.cnt
- \Program Files\VistA\Vitals\Help\Roboex32.dll

  The exe files are placed in the "Program Files\vista\Vitals" directory on the workstation. The other files are placed in the "Program Files\vista\Vitals\Help" directory.

  If you are running the software from a server, you should move these files to the server.

  If you are running the software from individual workstations and want to push these files, you should include them in your script.
22. Push the GMV_VitalsViewEnter.dll, GMV_VitalsViewEnter.hlp, and GMV_VitalsViewEnter.cnt files to the "Program Files\vista\Common Files" directory of the workstation where CPRS is located. For example, if CPRS is installed on the C:\\ drive, the three DLL related files must be copied into the C:\\ Program Files\vista\Common Files directory. If this directory path does not exist, you must create it.

    IMPORTANT: These files must not be installed in the same folder as CPRS. CPRS looks for these three files in the specified directory path. If CPRS cannot find the DLL and its supporting files, the users will not be able to enter patient vitals/measurements data.

> Note: The GMV_VitalsViewEnter.dll does not have to be registered in the Windows registry.

> The Client installation is complete.

## Customizing the Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, the client installation creates the icons and "Program Files\vista\Vitals" folders without any command line switches. Vitals/Measurements utilizes the ServerList utility of the RPC Broker for selecting a server to connect to if it is configured on the client workstation. Instructions for configuration and utilization of the ServerList utility can be found in the RPC Broker documentation located on the VDL.

If the ServerList utility has not been configured on the client, both Vitals and Vitals Manager applications will, by default, attempt to connect to the server identified in the users HOSTS file as BROKERSERVER on Listener Port 9200.

To override these default parameters, use the following procedure to add command line parameters to the application shortcuts.

1.  On the client desktop, right-click the Vitals icon and select Properties. The Vitals Properties window opens. Click the Shortcut tab to display the current target settings.

![Figure 4

23. In Figure 4, the application will attempt to connect to the server identified in your HOSTS file as *yourserver* and will use listener port 9200. In this example, the complete Target line would read:](gmrv-5-23-installation-guide/004.png)

*Figure 4

23. In Figure 4, the application will attempt to connect to the server identified in your HOSTS file as *yourserver* and will use listener port 9200. In this example, the complete Target line would read:*

"C:\Program Files\VistA\Vitals\Vitals.exe" /s=yourserver /p=9200

24. Enter a different parameter or switch in the Target field. The command line parameters available from the command prompt or within Windows shortcut definitions are:

> Vitals.exe \[/server=*servername*\] \[/port=*listenerport*\] \[/tempdir=*temporarydirectory*\] \[/helpdir=*helpdirectory*\] \[/debug={on\|off}\] \[/noccow\] \[/ccow=patientonly\]

> VitalsManager.exe \[/server=*servername*\] \[/port=*listenerport*\] \[/helpdir=*helpdirectory*\] \[/debug={on\|off}\]

> The following table describes each of the available parameters and switches.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 55%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Switches</strong></td>
<td><strong>Description</strong></td>
<td><strong>Example</strong></td>
</tr>
<tr class="even">
<td>/server</td>
<td><p>Specifies an alternate server to connect to. The server must be defined in the clients hosts file.</p>
<p>Default Hosts. file locations:</p>
<p>NT 4.0/W2K = c:\winnt\system32\drivers\etc\hosts.</p>
<p>Windows 9x = c:\windows\hosts.</p>
<p>Default = BROKERSERVER</p></td>
<td>/server=vista</td>
</tr>
<tr class="odd">
<td>/port</td>
<td><p>Specifies an alternate listener port on the selected server. This is the TCP/IP port that the broker is running on VistA server.</p>
<p>Default = 9200</p></td>
<td>/port=9200</td>
</tr>
<tr class="even">
<td>/tempdir</td>
<td><p>Location accessible to the client workstation and current user for storage of temporary scratch files.</p>
<p>Default = <em>application_directory</em>\temp</p></td>
<td>/tempdir=C:\temp</td>
</tr>
<tr class="odd">
<td>/helpdir</td>
<td><p>Location of the Vitals/Measurements windows help files.</p>
<p>Default = <em>application_directory</em>\help</p></td>
<td>/helpdir=C: \help</td>
</tr>
<tr class="even">
<td>/debug</td>
<td><p>Set the debug mode for both the RPC Broker and the Vitals/Measurements application.</p>
<p>Default = Off.</p></td>
<td>/debug=On</td>
</tr>
<tr class="odd">
<td>/noccow</td>
<td>The application will not check the CCOW context at all. This switch will force the user to sign on and select a patient when invoking the Vitals GUI.</td>
<td>/noccow</td>
</tr>
<tr class="even">
<td>/ccow=patientonly</td>
<td>The application will use CCOW, but will be set to check for patient context only. Automatic sign on will be disabled, but the automatic selection of a patient will be enabled. If a patient is already selected in an open application, Vitals will automatically open the patient being used by that application.</td>
<td>/ccow=patientonly</td>
</tr>
</tbody>
</table>

### From: GMRV*5*22 Installation Guide

### M Server – sample installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\> D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

KIDS Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option: INSTALLATION

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: GMRV\*5.0\*22 Loaded from Distribution 9/6/07@14:41:26

=\> GMRV\*5\*22

This Distribution was loaded on Sep 06, 2007@14:41:26 with header of

GMRV\*5\*22

It consisted of the following Install(s):

GMRV\*5.0\*22

Checking Install for Package GMRV\*5.0\*22

Install Questions for GMRV\*5.0\*22

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

Enter options you wish to mark as 'Out Of Order': GMV V/M GUI Vitals/Measu

rements GUI Application

Enter options you wish to mark as 'Out Of Order':

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET

Install Started for GMRV\*5.0\*22 :

Sep 06, 2007@14:46:16

Build Distribution Date: Jun 26, 2007

Installing Routines:

Sep 06, 2007@14:46:16

Installing PACKAGE COMPONENTS:

Installing REMOTE PROCEDURE

Sep 06, 2007@14:46:16

Running Post-Install Routine: EN^GMV7PST

Updating system parameters.

Checking STANDING qualifier...

Checking input template definitions...

No Description\|1:0:1,2~2,64~3,50~6,66;22:0;5:0:1,22~2,61~3,50~5,63;21:0:2,84;3:0

:2,47~3,50;2:0:1,6;9:0:4,42

No Description\|1:0:1,2~2,64~3,50~6,66;22:0;5:0:1,22~2,61~3,50~5,63;21:0:2,84;3:0

:2,47~3,50;2:0:1,6;9:0:2,51~4,42

GMRV\*5.0\*22

────────────────────────────────────────────────────────────────────────────────

Test - optional\|1:0:1,2~2,64~3,50~6,66;8:0:4,42;5:0;3:0;2:0;9:0:4,42

Test - optional\|1:0:1,2~2,64~3,50~6,66;8:0:4,42;5:0;3:0;2:0;9:0:2,51~4,42

ALL VITALS\|1:0:1,2~2,64~3,50~6,66;20:0:1,74~5,63;8:0:4,42;22:0;5:0:1,22~2,59~3,5

0~5,63;21:0:2,93;3:0:2,47~3,50;2:0:1,6;9:0:4,42;4:0

ALL VITALS\|1:0:1,2~2,64~3,50~6,66;20:0:1,74~5,63;8:0:4,42;22:0;5:0:1,22~2,59~3,5

0~5,63;21:0:2,93;3:0:2,47~3,50;2:0:1,6;9:0:2,51~4,42;4:0

Updating Routine file...

Updating KIDS files...

GMRV\*5.0\*22 Installed.

Sep 06, 2007@14:46:17

Install Message sent \#50274

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed
