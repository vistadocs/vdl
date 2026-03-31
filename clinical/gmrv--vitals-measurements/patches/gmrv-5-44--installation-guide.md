---
title: GMRV*5*44 Deployment, Installation, Back Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: GMRV
app_name: Vitals/Measurements
section: CLI
app_status: active
pkg_ns: GMRV
patch_ver: 5
patch_id: GMRV*5*44
group_key: "GMRV:GMRV:5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - vitals
  - installation
  - back
  - rollback
  - deployment
  - class
  - lite
  - vista
page_count: 0
word_count: 4495
section_count: 30
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/gmrv_5_0_44_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/gmrv_5_0_44_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=107"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Vitals Suite (GMRV\*5.0\*44)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](gmrv-5-44-deployment-installation-back-out-and-rollback-guide/001.png)

January 2021

Office of Information and Technology (OI&T)

Revision History

<table>
<caption><p><span id="_Toc62116446" class="anchor"></span>Table : Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 44%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01/2021</td>
<td><p>Section 1 Introduction, add note regarding <a href="#Vitals_Manager">Vitals Manager</a></p>
<p>Section 5.1, remove EXCEPTION parameters</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>12/2020</td>
<td>Initial Release</td>
<td>CPRS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Toc62116446" class="anchor"></span>Table : Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

List of Tables

List of Figures

[Figure 1: Shortcut Icons for Vitals [7](#_Toc62116594)](#_Toc62116594)

[Figure 2: Test Vitals44 Properties [8](#_Toc62116595)](#_Toc62116595)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
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
    - [GMRV\5.0\44 VistA Installation](#gmrv5044-vista-installation)
    - [Vitals Lite v5.0.44 and Vitals v5.0.44 Installation](#vitals-lite-v5044-and-vitals-v5044-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Post Installation](#post-installation)
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
The Vitals Suite (GMRV\*5.0\*44) consists of Vitals Lite v5.0.44.1 and Vitals v5.0.44.1. This document describes how to deploy and install, how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.
PLEASE NOTE: <span id="Vitals_Manager" class="anchor"></span>Vitals Manager is NOT being updated with this patch. Vitals Manager will remain at version 38.3.
The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 project is for installation on a fully patched VistA system. There are two Graphical User Interface (GUI) components and a Dynamic-Link Library (DLL) that should be running on a Windows system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 and the associated M patch are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. It utilizes existing, nationally released security controls to control access.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No one single entity oversees decision making for deployment, installation, back-out and rollback of Vitals Lite v5.0.44.1 and Vitals v5.0.44.1. The Release Agent and Application Coordinators under the Veterans in Process will approve release from a product development perspective. Local representatives will approve the installation at each site. If an issue with the software arises, the Area Managers and other site leadership will meet along with input from Patient Safety, Development, and Health Product Support to initiate a back-out and rollback decision of the software along with the IT Operations and Services personnel. The following table provides Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 project information.

<table>
<caption><p><span id="_Toc62116447" class="anchor"></span>Table : Files to be Downloaded</p></caption>
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
<td>Plan and schedule deployment</td>
</tr>
<tr class="even">
<td>IT Operations and Services personnel</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment</td>
</tr>
<tr class="odd">
<td>Site personnel</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="even">
<td><p>IT Operations and Services personnel.</p>
<p>The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</p></td>
<td>Installation</td>
<td>Plan and schedule installation</td>
</tr>
<tr class="odd">
<td>N/A – will work under the VistA ATO and security protocols.</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
</tr>
<tr class="even">
<td>N/A – no equipment is being added.</td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
</tr>
<tr class="odd">
<td>N/A – no new functionality is being introduced.</td>
<td>Installations</td>
<td>Coordinate training</td>
</tr>
<tr class="even">
<td>Area Manager, IT Operations, and Services personnel</td>
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

<span id="_Toc62116447" class="anchor"></span>Table : Files to be Downloaded

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module release. Once approval is given the patch GMRV\*5.0\*44 will be released from the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing and deployment to production will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no timeline specifically for deployment. Installation will be at the site’s discretion, within the constraints of the compliance period for the release.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to IOC sites for verification of functionality. Once that testing is completed and approval is given for national release, Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 (GMRV\*5.0\*44) will be deployed to all VistA systems.

The Production (IOC) testing sites are: Birmingham VAMC, AL and North Texas Healthcare System.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for Vitals Lite v5.0.44.1 and Vitals v5.0.44.1. A fully patched VistA system is the only requirement.

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

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action item and National Change Order prior to the release of Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 advising them of the upcoming release.

It will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch GMRV\*5.0\*44 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 assumes a fully-patched VistA system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only preparation necessary is to ensure you back up the KIDS build before proceeding with the installation.

\[VistA\] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

\[GUI\] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.).

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 are being released as a PackMan Message distributed through the National Patch Module combined with a .ZIP file containing the GUI file(s).

The .ZIP file and the documentation can be obtained at location: /srv/vista/patches/SOFTWARE

Other software files can also be obtained by accessing the URL: REDACTED

Documentation can also be found on the VA Software Document Library at:

[Computerized Patient Record System (CPRS)](https://www.va.gov/vdl/application.asp?appid=61)

<table>
<caption><p><span id="_Toc62116448" class="anchor"></span>Table : CPRS Development Team Contacts</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 49%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Zip File Contents</th>
<th>Download Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GMRV_50_44.ZIP</td>
<td><p>GMV_VitalsViewEnter.dll</p>
<p>GMV_VitalsViewEnter.map</p>
<p>Vitals.exe</p>
<p>Vitals.map</p>
<p>Help Folder</p></td>
<td>Binary</td>
</tr>
</tbody>
</table>

<span id="_Toc62116448" class="anchor"></span>Table : CPRS Development Team Contacts

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

Installation of Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### GMRV\*5.0\*44 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation Menu. From this menu:
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name GMRV\*5.0\*44.
    2.  Select the Backup a Transport Global option to create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.

        It is imperative this backup be performed.
    3.  You may also elect to use the following options:
        1.  Print Transport Global – This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
    4.  Select the Install Package(s) option and choose the patch to install.
        1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' answer NO.
        2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
        3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

### Vitals Lite v5.0.44 and Vitals v5.0.44 Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the Vitals executables and Vitals Lite DLL. Download the ZIP file and extract all the files System Configuration.

#### Vitals GUI Methods of Installation

The following methods of installation of Vitals are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

Network (shared) installation:

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (Vitals.exe) across the LAN.

The GUI executable (Vitals.exe), help files (VITALS.chm) are copied to a network shared location. Users are provided with a desktop shortcut to run Vitals.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the “Target” field of the shortcut properties

At the time of a Vitals version update, the copy of Vitals.exe and the help files are replaced on the network share with the new version.

Any users requiring access to another site's Vitals.exe system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of Vitals.exe (e.g. for testing purposes), a different version of Vitals.exe can be placed in a separate network location and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

Citrix installation:

The GUI executables (Vitals.exe) and help folder and files (VITALS.chm) are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> **NOTE:** For issues with CAG, please contact the local or national help desk.

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

Local workstation installation:

This is the method of installation where the GUI executables (Vitals.exe) and help folder and files (VITALS.chm) are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via SCCM. A National package (Vitals Lite v5.0.44.1 and Vitals v5.0.44.1) has been prepared and made available to Regional COR Client Technologies leadership.

Manual install:

This method is used for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.

1.  Locate the GMRV_50_44.ZIP and unzip the file.

    Copy the contents of the zip archive (the 2 GUIs and the 2 help files) to a test directory, for example, C:\VitalsTest. A new directory may need to be created.

    <u>Note</u>: Administrator rights are required for the PC used to complete this step.
3.  Create shortcut(s) and name it/them “Test Vitals44.”

    This is to give the user another visual cue that this is not the normal Vitals icon.

<span id="_Toc62116594" class="anchor"></span>Figure : Shortcut Icons for Vitals

![](gmrv-5-44-deployment-installation-back-out-and-rollback-guide/002.png)

4.  Determine the DNS server name or IP address for the appropriate VistA server.
5.  Determine the Broker RPC port for the VistA account.
6.  Enter IP (or DNS name) and RPC port in the Target field of the shortcut properties (or use ServerList.exe).

<span id="_Toc62116595" class="anchor"></span>Figure : Test Vitals44 Properties

> ![](gmrv-5-44-deployment-installation-back-out-and-rollback-guide/003.png)

> **NOTE:** The server and port number shown above are for example only.

#### Vitals Lite DLL Methods of Installation

The following methods of installation of Vitals Lite are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

Network (shared) installation:

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the DLL (GMV_VitalsViewEnter.dll) across the network.

The DLL (GMV_VitalsViewEnter.dll), and help file (GMV_VitalsViewEnter.chm), are copied to the network shared location that contains the CPRS executable. Users will access the DLL via CPRS's coversheet.

At the time of a Vitals Lite version update the copy of GMV_VitalsViewEnter.dll and the help file are simply replaced, on the network share, with the new version. Specifically, the CHM file should replace the existing HLP file.

If a user requires access to an older or newer version of GMV_VitalsViewEnter.dll (e.g. for testing purposes), a different version of GMV_VitalsViewEnter.dll can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

Citrix installation:

The DLL (GMV_VitalsViewEnter.dll) and help file (GMV_VitalsViewEnter.chm) are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> **NOTE:** For issues with CAG, please contact the local or national help desk.

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

Local workstation installation:

This is the “standard” method of installation where the Vitals Lite (GMV_ViewEnter.dll) and help file (GMV_VitalsViewEnter.chm) are installed on and run from the user's local workstation.

> **NOTE:** There is a national SCCM package to help sites or ITOPS distribute the Vitals Lite GUI.

Manual install:

Unzip the GMRV_50_44.ZIP file and move the files to an appropriate directory and/or workstation.

Windows 7 & 10:

- For 64-bit machines: “C:\Program Files (x86)\Vista\Common Files”
- For 32-bit machines: “C:\Program Files\Vista\Common Files”
1.  Rename the current version of the DLL (5.0.38.2) to GMV_VitalsViewEnter.dll.bkup.38.
2.  Copy the new version of the DLL (5.0.44.1) into the same folder.
3.  Replace the help file GMV_VitalsViewEnter.hlp with the new help file GMV_VitalsViewEnter.chm.

To switch between versions, reverse the steps above - rename the current release DLL (5.0.38.2) to GMV_VitalsViewEnter.dll, rename the new version of the DLL (5.0.44.1) to GMV_VitalsViewEnter.dll.bkup.38, and replace the CHM help file with the HLP file.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VISTA\] Verify the checksum of routine GMV44PST is equal to the checksum listed on the patch description.

\[GUI\] Launch the Vitals GUIs and verify the splash screen now announces that version 5.0.44.1 is running. Log into the desired server and verify that a version mismatch is not received. Launch the Vitals Lite DLL from within CPRS and verify the About screen now announces that version 5.0.44.1 is running.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No post installation steps.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] The previous Vitals GUI versions do not store the version number on the VistA System, no action is needed. The DLL version will be backed out by installing a previous version of the DLL.

\[GUI\] To revert the Vitals GUI(s), the prior GUI(s) would have to be redistributed. For Vitals, this is v5.0.38.2. To revert the Vitals Lite DLL, the prior DLL (v5.0.38.2) would have to be redistributed.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on Vitals Lite v5.0.44.1 and Vitals v5.0.44.1.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the two test sites listed in Section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the second build of GMRV\*5.0\*44. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to the CPRS Development team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 would result in the re-instatement of the issues that were addressed as well as the removal of the new features that were added.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for Vitals Lite v5.0.44.1 and Vitals v5.0.44.1 is in the event of a catastrophic failure.

1.  Contact the CPRS Development team to notify them there has been a catastrophic failure with Vitals Lite v5.0.44.1 and Vitals v5.0.44.1. Use the following contacts:

<table>
<caption>Lists the individuals who should be contacted if this patch needs to be backed-out. It provides their email and phone contact information.</caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 37%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>Name &amp; Title</th>
<th>Email</th>
<th>Telephone Number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>REDACTED</p>
<p>Project Manager</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td><p>REDACTED</p>
<p>Delphi Developer</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td><p>REDACTED</p>
<p>M Developer</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

Lists the individuals who should be contacted if this patch needs to be backed-out. It provides their email and phone contact information.

1.  If the decision is made to proceed with back-out and rollback, the CPRS Development team will be available to assist sites that have misplaced their backup PackMan message or build, and provide the instructions on downloading the executables, if necessary.
2.  Coordinate with the appropriate IT support, local and regional, to schedule the time to install GMRV\*5.0\*38 and to push out / install the previous GUI executable.
3.  \[VistA\]
1.  Install the back-up message created during the KIDS installation of GMRV\*5.0\*44.
2.  Install GMRV\*5.0\*38.
4.  Once GMRV\*5.0\*38 and Vitals Suite 5.0.38.2 have been installed, verify operations before making available to all staff.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure the v5.0.38.2 executables and the v5.0.38.2 DLL launch properly.
2.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

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

Back-out will automatically rollback version.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A