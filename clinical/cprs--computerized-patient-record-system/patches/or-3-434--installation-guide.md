---
title: OR*3*434 Deployment, Installation, Back-Out, and Rollback Guide CPRS GUI 31A
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: CPRS GUI 31A
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*434
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - cprs
  - parameter
  - installation
  - order
  - back
  - edit
  - install
  - values
page_count: 0
word_count: 7162
section_count: 32
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 2017-10-12
revision_count: 6
revision_newest: 2017-10-12
revision_oldest: 2017-03-14
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_434_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_434_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

CPRS v31a (OR\*3\*434)

Deployment, Installation, Back-Out, and Rollback Guide

![](or-3-434-deployment-installation-back-out-and-rollback-guide-cprs-gui-31a/001.png)

November 2017

Office of Information and Technology (OI&T)

Revision History

| Date   | Version | Description                                                                                                                                                                                                                                     | Author                         |
|------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 2017-10-12 | 0.6         | Added information on the way to ensure that sites using COM objects and distributing the CPRS GUI correctly handle registry entries. The information is under the Direct Access to a Local Copy of CPRSChart.exe (bypassing the loader) bullet. | <span class="mark">REDACTED</span> |
| 2017-10-12 | 0.5         | Updated information on required patches, about the JLV button label, download information, and a version number from reviewer’s comments.                                                                                                           | <span class="mark">REDACTED</span> |
| 2017-07-20 | 0.4         | Added information about a Return to Clinic notification                                                                                                                                                                                             | <span class="mark">REDACTED</span> |
| 2017-06-09 | 0.3         | Added information about the Return to Clinic order dialog configuration.                                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 2017-03-14 | 0.2         | Updates version numbers.                                                                                                                                                                                                                            | <span class="mark">REDACTED</span> |
| 2017-03-14 | 0.1         | Initial Draft                                                                                                                                                                                                                                       | <span class="mark">REDACTED</span> |

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
    - [Site Information (Locations, Deployment Recipients)](#site-information-locations-deployment-recipients)
    - [Site Preparation](#site-preparation)
  - [Resources](#resources)
    - [Facility Specifics](#facility-specifics)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Backing Up Important Files](#backing-up-important-files)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [CPRS v31a Multi-Package Build KIDS Installation](#cprs-v31a-multi-package-build-kids-installation)
    - [Move All DLLs to the Appropriate Directories](#move-all-dlls-to-the-appropriate-directories)
    - [CPRS v31a GUI Installation](#cprs-v31a-gui-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
    - [Place New Order Dialogs on Order Menus](#place-new-order-dialogs-on-order-menus)
    - [ORWOR CATEGORY SEQUENCE Parameters](#orwor-category-sequence-parameters)
    - [Edit the name of the Mental Health DLL](#edit-the-name-of-the-mental-health-dll)
    - [(Optional) Add Return to Clinic Additional Information](#optional-add-return-to-clinic-additional-information)
    - [(Optional) Add Return to Clinic Prerequisites](#optional-add-return-to-clinic-prerequisites)
    - [(Optional) Enable the Return to Clinic Alert](#optional-enable-the-return-to-clinic-alert)
    - [(Optional) Change the Name on the Button from VistaWeb to JLV](#optional-change-the-name-on-the-button-from-vistaweb-to-jlv)
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
    - [Installing the Back-Out Patch](#installing-the-back-out-patch)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Example Installation](#example-installation)
This document describes how to deploy and install CPRS v31a*,* as well as how to back-out the product and rollback to a previous version.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom CPRS v31a will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, a communications plan, and a rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v31a project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system. The installation of CPRS v31a is required for the future installations of CPRS GUI releases (such as v31b and v32).

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a and associated M patches are expected to be installed on existing VistA platforms.

One feature of CPRS v31a is the support for two-factor authentication (2FA). However, for 2FA to work, user accounts at the sites must be bound to their Active Directory accounts. All users need to use the Link My Account portal to link their account so that two-factor authentication will work. Information on how to use Link My Account has already been distributed to all sites.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No single entity is in charge of decision making for deployment, installation, back out and rollback of CPRS v31a. Rather, the Critical Decision Point representatives (commonly referred to as the three in the box) under the Veterans In Process (VIP) will meet and approve release from a business perspective.

If an issue with the software arises that would require a national rollback, then the same three in the box members under VIP will coordinate with several groups (including Patient Safety Health Product Support, Information Technology Operations Service (ITOPS), and Site leadership) to decide whether a back out and rollback of the software is necessary. The Facility Chief Information Officer (FCIO) has the final authority to require the patch back out and data rollback and accept the associated risks.

The following table provides CPRS v31a project information.

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table>
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
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS.</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
<td>After national release.</td>
</tr>
<tr class="even">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS.</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
<td>After national release.</td>
</tr>
<tr class="odd">
<td></td>
<td>Site personnel.</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
<td>After national release.</td>
</tr>
<tr class="even">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
<td>Deployment</td>
<td>Execute deployment</td>
<td>After national release.</td>
</tr>
<tr class="odd">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
<td>Installation</td>
<td>Plan and schedule installation</td>
<td>After national release.</td>
</tr>
<tr class="even">
<td></td>
<td>N/A – will work under the VistA ATO and security protocols.</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>N/A – no equipment is being added.</td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>N/A – no new functionality is being introduced.</td>
<td>Installations</td>
<td>Coordinate training</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Facility CIO and IT support – which may be local or regional.</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
<td>After national release.</td>
</tr>
<tr class="even">
<td></td>
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the CPRS Development Team during the compliance period. At the end of the compliance period, support will be transitioned to VistA Maintenance.</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
<td>After national release.</td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because of the importance of the features released with CPRS v31a, the deployment will be a standard release with a 42-day compliance window (installed in production by December 19, 2017).

There are currently no site-facing on-line meetings or training planned for this deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The timeline is for the patch to be released in November 2017, with a 42-day compliance period after national release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CPRS v31a deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway. There are also instances, such as the Meds by Mail personnel who may not have a VistA instance, but will have the executable deployed.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capabilities (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, CPRS v31a (OR\*3\*434) will be deployed to all VistA systems.

The Production (IOC) Test sites are:

- Heartland East
- Heartland West
- Tuscaloosa

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a introduces 2-factor authentication to CPRS. As a result, each CPRS user must use the Link My Account portal to bind their Active Directory account to their user account. All sites have received information on how to use the Link My Account portal.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an SDE Bulletin prior to the release of CPRS v31a advising sites of the upcoming release.

CPRS v31a will be deployed using the normal patch deployment process. After the patch is nationally released, sites will have 42 days to install CPRS v31a (by December 19, 2017). There will be an M patch, a GUI executable, and two new DLLS.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a assumes a fully-patched VistA system.

## Backing Up Important Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Backup files ^ORD(101.41), ^ORD(100.98), and ^PXRMD(801.41) using your site’s policy for backing up data.

> If the steps are unknown, here is a way it can be done, using ^PXRMD(801.41) as an example:

1.  Go to a command prompt.
2.  At the prompt, enter D GOGEN^%ZSPECIAL.
3.  At the device prompt, enter the directory and file name where the global backup is to be stored.
4.  At the Parameters? Prompt, press \<enter\>.
5.  At the Global prompt, enter ^PXRMD(801.41.
6.  Verify that the file was created and exists in the directory specified.

> Example

DEV5A4:DVFDEV\>D GOGEN^%ZSPECIAL

Device: VA5\$:\[Local Directory\]31_FILES_BACKUP.GBL

Parameters? ("WNS") =\>

> **WARNING:** Use a "V" format to avoid problems with control characters.

Global ^PXRMD(801.41,

Global ^

> **IMPORTANT:** These files will be important if, for some reason, there was a need for a rollback. Please retain these files for at least two weeks after installing the patch.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please check your system to verify that the following, previously released national patches are installed:

- OR\*3.0\*421
- OR\*3.0\*423
- OR\*3.0\*424
- OR\*3.0\*425
- OR\*3.0\*436
- XU\*8\*659
- XWB\*1.1\*64
- FileMan 22.2 must be installed in the environment.

This multi-package build (VistA KIDS Build) should take less than 5 minutes to install.

The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation install, etc.).

It is recommended that the installation be done during non-peak hours. If at all possible, the users should not be in CPRS when the KIDS installation is being performed.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a is being released as two files. The OR\*3.0\*434 patch is being released in a host file called CPRSV31A_COMBINED_BUILD.KID. Other necessary files are included in the OR_30_434.ZIP file.

The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI&T Field Offices:

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library at:

<http://www.va.gov/vdl/>

CPRS v31a files

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 34%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>CPRS v31a files to be downloaded</th>
<th>File Contents</th>
<th>Download Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CPRSV31A_COMBINED_BUILD.KID</td>
<td><ul>
<li><p><strong>OR*3*434</strong>: M changes for CPRS v31a</p></li>
</ul></td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>OR_30_434.ZIP</td>
<td><ul>
<li><blockquote>
<p>Borlndmm.dll</p>
</blockquote></li>
<li><blockquote>
<p>CPRSChart.exe</p>
</blockquote></li>
<li><blockquote>
<p>CPRSChart.map</p>
</blockquote></li>
<li><blockquote>
<p>GMV_VitalsViewEnter.cnt</p>
</blockquote></li>
<li><blockquote>
<p>GMV_VitalsViewEnter.dll</p>
</blockquote></li>
<li><blockquote>
<p>GMV_VitalsViewEnter.hlp</p>
</blockquote></li>
<li><blockquote>
<p>RoboEx32.dll</p>
</blockquote></li>
<li><blockquote>
<p>YS_MHA_A_XE8.dll</p>
</blockquote></li>
<li><blockquote>
<p>Help directory</p>
</blockquote></li>
<li><blockquote>
<p>cprsguitm.doc</p>
</blockquote></li>
<li><blockquote>
<p>cprsguitm.pdf</p>
</blockquote></li>
<li><blockquote>
<p>cprsguium.doc</p>
</blockquote></li>
<li><blockquote>
<p>cprsguium.pdf</p>
</blockquote></li>
<li><blockquote>
<p>or_30_434_ig.docx</p>
</blockquote></li>
<li><blockquote>
<p>or_30_434_ig.pdf</p>
</blockquote></li>
<li><blockquote>
<p>or_30_434_rn.docx</p>
</blockquote></li>
<li><blockquote>
<p>or_30_434_rn.pdf</p>
</blockquote></li>
</ul></td>
<td>Binary</td>
</tr>
</tbody>
</table>

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

Installation of CPRS v31a requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.
- Loader installs – access/ability to upload new executable to the GOLD directory.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CPRS v31a Multi-Package Build KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. For the installation, it is recommended that users are off the system.

1.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
2.  Next, select ‘Load a Distribution’. When prompted “Enter a Host File: “, enter \<directory\>CPRSV31A_COMBINED_BUILD.KID (where directory represents the location where you stored the KIDS file).
3.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
4.  From this menu, you may elect to use the following options
1.  Backup a Transport Global
2.  Compare Transport Global to Current System
3.  Verify Checksums in Transport Global
5.  Use the Install Package(s) options and select the package CPRSV31A.
6.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install?”, respond NO.
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
8.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.

### Move All DLLs to the Appropriate Directories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Place the DLLs and other files in the zip file in the appropriate locations.

> **NOTE:** The Borlandmm.dll must be in the same directory as the CPRSChart.exe.

The other DLLs are no longer required to reside on individual workstations. For example, if you are doing a network install of the CPRSChart executable, you can place the DLLs in that same directory.

> **NOTE:** Some sites have experienced unacceptable delays in launching the DLLs if they are located on the server. If this occurs, the DLLs should be placed on the local workstations.

Here is the hierarchy the CPRS GUI uses to search for the DLLs:

1.  The same folder as the application
2.  A “Common Files\\ folder in the same folder as the application
3.  Windows 7:

For 64 bit machines: “C:\Program Files (x86)\Vista\Common Files”

For 32 bit machines: “C:\Program Files\Vista\Common Files”

### CPRS v31a GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several different ways to install the CPRS GUI executable (CPRSChart.exe). Which method you choose depends on your system configuration and how CPRS is support at your site.

#### CPRS GUI Methods of Installation

The following methods of installation of CPRS are available. Sites' choice of which method(s) to use will depend upon ITOPS/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

- Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPRSChart.exe) across the LAN.

> The GUI executable (CPRSChart.exe), and ancillary files (DLLs, Help files etc.), are copied to a network shared location. Users are provided with a desktop shortcut to run CPRSChart.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the “Target” field of the shortcut properties

> At the time of a CPRS version update the copy of CPRSChart.exe (and any updated ancillary files) is simply replaced, on the network share, with the new version.

> Any users requiring access to another site's CPRS system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of CPRS (e.g. during a phased deployment, when sites are temporarily not all on the same version, or for testing purposes) a different version of CPRSChart.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

> Note: The version of CPRSChart a user executes must always match the patch-level version of the VistA system targeted.

- Citrix installation:

> The GUI executable (CPRSChart.exe) and ancillary files (DLLs, Help files etc.) are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

> During a phased deployment of a new version of CPRS, if a Citrix Farm is serving users who are scheduled to deploy at different times, the Farm administrator may be required to temporarily maintain hosts with both the old and the new versions of CPRSChart.exe available.

- Gold Path installation:

> This method of installation places the GUI executable (CPRSChart.exe), and ancillary files (DLLs, Help files etc.) on and run from the user's local workstation. In normal day-to-day operation, the user's shortcut executes a locally installed copy of CPRSLoader.exe which looks in a pre-configured network “Gold Path” (specified in a command line parameter) to see if there is a later version of CPRSChart.exe ready to be installed. If not, then execution passes to the locally installed version of CPRSChart.exe. If an updated version is found on the Gold Path, then a silent installation of the new version takes place, following which the newly installed version of CPRSChart.exe is executed on the local workstation.

> This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file (CPRSLoader.msi) to each user's workstation, typically accomplished via SCCM. This is outside the scope of CPRS development. A National package (CPRS Loader 1.30.40) has been prepared and made available to Regional COR Client Technologies leadership.

> The CPRS Loader installation package can be found on the System Center Configuration Manager (SCCM) central site at the following locations.

> Note: The Loader has not been updated for CPRS v31a. There is no need to update the Loader. This is being left here for reference only.

> Package Name: 1VA - VA CPRS Loader

> Package ID: 1VA004E7, R03002C4

> Test Location:

> VA Central Site Packages \> Test \> 1VA - VA CPRS Loader

> Production Location:

> VA Central Site Packages \> Production \> 1VA – Applications \> 1VA - VA CPRS Loader

> All details of the SCCM package can be found in the build document and should be reviewed before deployment:

> TBD

> The CPRSChart.exe component of the update is held in a Microsoft Software Patch (MSP) file (CPRSChart.msp) which is copied to the network Gold Path location—that should be all that is required for a normal CPRS version update for sites using this method. The exception is if a new version of CPRS Loader is also being released, in which case the cycle begins again with the distribution to users' workstations of the new CPRSLoader.msi (before the new CPRSChart.msp is copied to the network Gold Path). CPRS v31a does not have a new loader.

> The CPRS deployment software distribution will include an appropriate version of the CPRS Microsoft patch file (named CPRS_XX_YY.msp, where XX is the current version number for CPRS, and YY is the current build number. At this point the current file name is OR_30_434.msp). This file has the named version of CPRSChart embedded within it, along with any updated ancillary files. Also included in the deployment software distribution will be a .VER file. This file will have the same name as the MSP file, with only the file extension changed. As an example, the .VER file for OR_30_434.msp will be named OR_30_434.ver. To be effective, the .VER file must be placed in the same Gold Path in which the .MSP file was placed. The .VER is optional but beneficial. It will allow the CPRS loader to much more quickly find an appropriate version of CPRSChart.exe for use with the current VistA system. Including the VER file in the Gold Path can shorten CPRS start times substantially.

> For the convenience of local System Administrators, the file CPRSLoader.msi is also included in the release package, in case they need to manually install it on a workstation.

- Direct Access to a Local Copy of CPRSChart.exe (bypassing the loader)

> Sites that want to deploy the CPRS executable to their user’s local workstation often use this distribution. This method is recommended for local workstation distribution for CPRS v31a because installation of the Loader’s MSP file now requires Administrative access to the user’s PC.

> There is a national SCCM package to distribute the Cprschart.exe file to help sites or ITOPS install the CPRS GUI.

> WARNING:If your site

- uses COM objects (such as Dental Record Manager, LES, patient identification object that displays a patient picture, MED, etc.)
- and you distribute the CPRS GUI using SCCM

> you MUST make registry entries similar to the following after making sure the path is correct for your site:

> The path example C:\\CPRS\\Workspaces\\build_CPRS_v31_Development\\CPRS_src\\CPRS-chart\\ in the instructions should be replaced with the correct path for the machine.

> \[HKEY_CLASSES_ROOT\TypeLib\\0A4A6086-6504-11D5-82DE-00C04F72C274}\]

> \[HKEY_CLASSES_ROOT\TypeLib\\0A4A6086-6504-11D5-82DE-00C04F72C274}\1.0\]

> @="CPRSChart Library"

> \[HKEY_CLASSES_ROOT\TypeLib\\0A4A6086-6504-11D5-82DE-00C04F72C274}\1.0\0\]

> \[HKEY_CLASSES_ROOT\TypeLib\\0A4A6086-6504-11D5-82DE-00C04F72C274}\1.0\0\win32\]

> @="C:\\CPRS\\Workspaces\\build_CPRS_v31_Development\\CPRS_src\\CPRS-chart\\CPRSChart.exe"

> \[HKEY_CLASSES_ROOT\TypeLib\\0A4A6086-6504-11D5-82DE-00C04F72C274}\1.0\FLAGS\]

> @=0

> \[HKEY_CLASSES_ROOT\TypeLib\\0A4A6086-6504-11D5-82DE-00C04F72C274}\1.0\HELPDIR\]

> @="C:\\CPRS\\Workspaces\\build_CPRS_v31_Development\\CPRS_src\\CPRS-chart\\"

> Note: An SCCM package has been written, and used, in Region 4 which would require minimal editing to be useable at other locations—contact the CPRS Implementation Team (<OITPDCPRSImplementationTeam@va.gov>) for additional information.

> If you do not make these corrections, your COM object-related will not work correctly or will create errors. The reason for this is that many 3rd party/Class 3 COM objects use the CPRS RPC Broker COM server as their pipe to the VistA database. The MSI installation uninstalled any previous version of CPRS before installing CPRS v31a. This uninstallation appears to have removed the registry information that Windows needs in order to allow the CPRS RPC Broker COM server to be used. The information in the text file replaces the information that was deleted.

> An alternative, hybrid, version of this method would be to have two shortcuts for the users: One, for day-to-day use, which points directly to the local CPRSChart.exe and a second, to be used only for updating, which points to CPRSLoader.exe.

- Manual install

  This method is used primarily for advanced users and at testing locations.  
  This method is somewhat changed from that used previously for Windows XP workstations.
1.  Locate the OR_30_434.ZIP and unzip the file.
7.  Copy the CPRSChart.exe to a test directory, for example, C:\cprstest. You may need to create this new directory.

    Note: You may need to have a user with Administrator rights complete this step.
8.  Create a Shortcut and name it “Test CPRSv31a”. This is to give the user another visual cue that this is not the normal CPRS icon.

    ![](or-3-434-deployment-installation-back-out-and-rollback-guide-cprs-gui-31a/002.png)
9.  Copy the borlandmm.dll file into the same directory as cprschart.exe (for example, c:\cprstest). This file should be in the same directory as the CPRSChart.exe for CPRS v31a.
10. Determine the DNS server name or IP address for the appropriate VistA server.
11. Determine the Broker RPC port for the VistA account.
12. Enter IP and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

> ![](or-3-434-deployment-installation-back-out-and-rollback-guide-cprs-gui-31a/003.png)

> Example of what the shortcut properties dialog might look like.

> The server and port number shown above are not real and are for example only.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Launch the CPRS GUI and verify the splash screen now announces that you are running version 31.116.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the installation of CPRS v31a and the associated patches, there is some configuration that will need to be done, including

- Place new Order dialogs on Order Menus
- Change the name of the Mental Health DLL
- (optional) If your site will use prerequisites for the Return to Clinic features, they will need to be entered into the parameter.
- (Optional) If your site will use the Additional Information field in the Return to Clinic order dialog, the text will need to be entered into the parameter.
- (Optional) If you will use the Return to Clinic alert
- (Optional) If your site has transitioned to using Joint Legacy Viewer (JLV), set the parameter ORWRP LEGACY VIEWER LABEL at the SYSTEM level to be the text: JLV

### Place New Order Dialogs on Order Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Order dialog will not function correctly until the necessary Scheduling patch SD\*5.3\*671 is installed.

The following ORDER DIALOG has been exported in patch OR\*3\*434:

| Order Dialog - Name | Order Dialog – Display Text |
|-------------------------|---------------------------------|
| SD RTC                  | Return to Clinic                |

These new ORDER DIALOGS will need to be added to any appropriate order menus at your site so that your users can place these types of orders.

### ORWOR CATEGORY SEQUENCE Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ORWOR CATEGORY SEQUENCE parameter at a site defines the order of display groups on the CPRS Orders tab. For the orders in the CLINIC SCHEDULING display group to be labeled properly, a new sequence value must be entered as a new Instance for this parameter. The Package level parameter has been exported with the new instance/values for this new display group as shown in the table below.

Parameter Instance Value

----------------------------------------------------------------------------

PKG: ORDER ENTRY/RESULTS REPOR 10 M.A.S.

PKG: ORDER ENTRY/RESULTS REPOR 20 ALLERGIES

PKG: ORDER ENTRY/RESULTS REPOR 30 VITALS/MEASUREMENTS

PKG: ORDER ENTRY/RESULTS REPOR 35 ACTIVITY

PKG: ORDER ENTRY/RESULTS REPOR 40 NURSING

PKG: ORDER ENTRY/RESULTS REPOR 50 DIETETICS

PKG: ORDER ENTRY/RESULTS REPOR 59 CLINIC INFUSIONS

PKG: ORDER ENTRY/RESULTS REPOR 60 IV MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 65 OUTPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 68 NON-VA MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 69 CLINIC MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 70 INPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 75 LABORATORY

PKG: ORDER ENTRY/RESULTS REPOR 80 IMAGING

PKG: ORDER ENTRY/RESULTS REPOR 90 CONSULTS

PKG: ORDER ENTRY/RESULTS REPOR 100 PROCEDURES

PKG: ORDER ENTRY/RESULTS REPOR 110 SURGERY

PKG: ORDER ENTRY/RESULTS REPOR 120 OTHER HOSPITAL SERVICES

PKG: ORDER ENTRY/RESULTS REPOR 130 SUPPLIES/DEVICES

PKG: ORDER ENTRY/RESULTS REPOR 131 CLINIC ORDERS

PKG: ORDER ENTRY/RESULTS REPOR 135 CLINIC SCHEDULING

However, if your site has the parameter defined at the System or User levels, this display group will need to be manually placed in your custom sequences based upon your site’s discretion. Below is an example of adding this display group to the sequence:

\<TEST ACCOUNT\> LV List Values for a Selected Parameter

\<TEST ACCOUNT\> LE List Values for a Selected Entity

\<TEST ACCOUNT\> LP List Values for a Selected Package

\<TEST ACCOUNT\> LT List Values for a Selected Template

\<TEST ACCOUNT\> EP Edit Parameter Values

\<TEST ACCOUNT\> ET Edit Parameter Values with Template

\<TEST ACCOUNT\> EK Edit Parameter Definition Keyword

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select General Parameter Tools \<TEST ACCOUNT\> Option: EP Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE Orders Category Sequence

ORWOR CATEGORY SEQUENCE may be set for the following:

4 User USR \[choose from NEW PERSON\]

8 System SYS \[TEST.CLEVELAND.MED.VA.GOV\]

10 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 8 System TEST.CLEVELAND.MED.VA.GOV

--- Setting ORWOR CATEGORY SEQUENCE for System: TEST.CLEVELAND.MED.VA.GOV ---

Select Sequence: 91

Are you adding 91 as a new Sequence? Yes// YES

Sequence: 91// 91

Display Group: CLINIC

1 CLINIC INFUSIONS

2 CLINIC INJECTIONS

3 CLINIC MEDICATIONS

4 CLINIC ORDERS

5 CLINIC SCHEDULING

CHOOSE 1-4: 5 CLINIC SCHEDULING

Select Sequence: 92

Are you adding 92 as a new Sequence? Yes// YES

### Edit the name of the Mental Health DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit the name of the Mental Health DLL to YS_MHA_A_XE8.DLL using the XPAR option as shown below.

Select OPTION NAME: XPAR EDIT

1 XPAR EDIT BY TEMPLATE Edit Parameter Values with Template

2 XPAR EDIT KEYWORD Edit Parameter Definition Keyword

3 XPAR EDIT PARAMETER Edit Parameter Values

CHOOSE 1-3: 3 XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: YS MHA_A DLL NAME Name of the YS_MHA_A dll

to use

------ Setting YS MHA_A DLL NAME for System: CPRS31.FO-SLC.MED.VA.GOV ------

DLL NAME: YS_MHA_A_XE3.dll// YS_MHA_A_XE8.DLL

### (Optional) Add Return to Clinic Additional Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a includes two new parameters that can be used by sites to include information that will display to the user entering the order.

The OR SD ADDITIONAL INFORMATION parameter enables the site or ITOPS personnel to enter text that they would like the user entering the Return to Clinic order. It is free text and can be entered or edited using XPAR EDIT.

To edit this parameter, use these steps:

1.  Login to VistA.
2.  On the CPRS Manager Menu (ORMGR), type IR (CPRS Configuration (IRM)) and press \<Enter\>.
3.  On the (CPRS Configuration (IRM) menu, type XX (General Parameter Tools) and press \<Enter\>..
4.  On the General Parameter Tools menu, type EP (Edit Parameter Values) and press \<Enter\>.
5.  At the Select PARAMETER DEFINITION NAME: prompt, type OR SD ADDITIONAL INFORMATION and press \<Enter\>.
6.  Select the level at which you want to edit, either System or Division, type 5 for Division or type 6 for System and press \<Enter\>.
7.  At the Additional Information Message Text: prompt where the cursor is by the Replace prompt, press \<Enter\>.
8.  In the Word Processing field that appears, type any text or edit what is there.
13. When finished entering or editing the text, to exit the field, select CTRL + E. If you wish to save your changes, answer Yes to the question that appears.

Here is an example of what it might look like.

Select OPTION NAME: ORMGR CPRS Manager Menu

CL Clinician Menu ...

NM Nurse Menu ...

WC Ward Clerk Menu ...

PE CPRS Configuration (Clin Coord) ...

IR CPRS Configuration (IRM) ...

Select CPRS Manager Menu \<TEST ACCOUNT\> Option: XX CPRS Configuration (IRM)

OC Order Check Expert System Main Menu ...

TI ORMTIME Main Menu ...

UT CPRS Clean-up Utilities ...

XX General Parameter Tools ...

DBG RPC DEBUG REPORT

HD HealtheVet Desktop Configuration ...

RD Remote Data Order Checking Parameters

Select CPRS Configuration (IRM) \<TEST ACCOUNT\> Option: XX General Parameter Tools

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools \<TEST ACCOUNT\> Option: ep Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: OR SD ADDITIONAL INFORMATION RTC Order Dialog Additional Information

OR SD ADDITIONAL INFORMATION may be set for the following:

5 Division DIV \[choose from INSTITUTION\]

6 System SYS \[TEST.DAYTON.MED.VA.GOV\]

Enter selection: 6 System TEST.DAYTON.MED.VA.GOV

-- Setting OR SD ADDITIONAL INFORMATION for System: TEST.DAYTON.MED.VA.GOV --

Additional Information Message Text: Testing additional messaging

Replace ....

==\[ WRAP \]==\[INSERT \]====\< Testing additional messagi\[Press \<PF1\>H for help\]====

MORE INFO TEST BUILD 112. Providers must request return appointments at

least one week in the future.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>=====

### (Optional) Add Return to Clinic Prerequisites 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a includes two new parameters that can be used by sites to include information, such as information the site can include that will display to the user entering the order.

The OR SD DIALOG PREREQ parameter enables the site or ITOPS personnel to enter text that they would like the user entering the Return to Clinic order. It is free text and can be entered or edited using XPAR EDIT.

To edit this parameter, use these steps:

1.  Login to VistA.
14. On the CPRS Manager Menu (ORMGR), type IR (CPRS Configuration (IRM)) and press \<Enter\>.
15. On the (CPRS Configuration (IRM) menu, type XX (General Parameter Tools) and press \<Enter\>..
16. On the General Parameter Tools menu, type EP (Edit Parameter Values) and press \<Enter\>.
17. At the Select PARAMETER DEFINITION NAME: prompt, type OR SD DIALOG PREREQ and press \<Enter\>.
18. To add a new item, enter an appropriate number at the Select Instance: prompt. Type the number and press \<Enter\>.
19. At the Are you adding 8 as a new Instance? Prompt, type Y and press \<Enter\>.
20. At the Instance prompt, press \<Enter\>.
21. At the RTC Order Prerequisites: prompt, type the text that you want to appear with a checkbox.

> Note: The Prerequisite entry is text only.

Here is an example of what it might look like.

Select OPTION NAME: ORMGR CPRS Manager Menu

CL Clinician Menu ...

NM Nurse Menu ...

WC Ward Clerk Menu ...

PE CPRS Configuration (Clin Coord) ...

IR CPRS Configuration (IRM) ...

Select CPRS Manager Menu \<TEST ACCOUNT\> Option: IR CPRS Configuration (IRM)

OC Order Check Expert System Main Menu ...

TI ORMTIME Main Menu ...

UT CPRS Clean-up Utilities ...

XX General Parameter Tools ...

DBG RPC DEBUG REPORT

HD HealtheVet Desktop Configuration ...

RD Remote Data Order Checking Parameters

Select CPRS Configuration (IRM) \<TEST ACCOUNT\> Option: XX General Parameter Tools

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools \<TEST ACCOUNT\> Option: EP Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: OR SD

1 OR SD ADDITIONAL INFORMATION RTC Order Dialog Additional Information

2 OR SD DIALOG PREREQ RTC Order Dialog Prerequisites

CHOOSE 1-2: 2 OR SD DIALOG PREREQ RTC Order Dialog Prerequisites

------ Setting OR SD DIALOG PREREQ for System: TEST.DAYTON.MED.VA.GOV ------

Select Instance: ?

Instance Value

-------- -----

1 LABS

2 VITALS

3 CONSULTS

4 NOTES

7 Radiology

Select Instance: 8

Are you adding 8 as a new Instance? Yes// YES

Instance: 8// 8

RTC Order Prerequisites: A1C lab

### (Optional) Enable the Return to Clinic Alert

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a has a new alert to communicate back to providers when a Return to Clinic (RTC) request has been cancelled. This alert is optional. If sites would like their providers to see these alerts, they must activate the alert. This alert will not be activated when CPRS v31a is installed. The alert is described below:

NUMBER: 91                              NAME: APPOINTMENT REQUEST CANCELLED

  PACKAGE ID: OR

  MESSAGE TEXT: Appointment Request Cancelled in Scheduling

  MESSAGE TYPE: PACKAGE PROVIDES A VARIABLE MESSAGE

  ACTION FLAG: RUN ROUTINE              ENTRY POINT: RTC

  ROUTINE NAME: ORB3FUP2                RELATED PACKAGE: OR

  FOLLOW-UP TYPE: ORDER

  DESCRIPTION: The purpose of this notification to advise the provider recipient

s when an appointment request is cancelled by the scheduling package.

PROCESSING FLAG: COMBINE DATA FROM DUPLICATES

PROCESSING FLAG: GENERATE ONE NOTIFICATION PER PATIENT

Please note that enabling this notification is optional. Your site will need to decide if you would like to enable this notification.

Use the following steps to enable this notification in CPRS:

1.  In the List Manager interface, choose the ORMGR CPRS Manager menu.
2.  Select the PE CPRS Configuration (Clin Coord) option.
3.  Select the NO Notification Mgmt Menu option.
4.  Select Enable/Disable Notifications option.
5.  Select the level for which you are setting this parameter:
    - User          USR    \[choose from NEW PERSON\]
    - Team (OE/RR)  OTL    \[choose from OE/RR LIST\]
    - Service       SRV    \[choose from SERVICE/SECTION\]
    - Location      LOC    \[choose from HOSPITAL LOCATION\]
    - Division      DIV    \[choose from INSTITUTION\]
    - System        SYS    \[xxxxx.FO-SLC.MED.VA.GOV\]
6.  Type the name of the notification you want to enable: APPOINTMENT REQUEST CANCELLED and press \<Enter\>. (You can also type two question marks and press \<Enter\> to get a list of ALL notifications.)
7.  When prompted if you are adding the notification as a new notification, type Y and press \<Enter\>.
8.  At the Notification prompt, if the correct notification is listed, press \<Enter\>.
9.  At the Value prompt, enable the notification or set it as mandatory. To enable, type E and press \<Enter\>. To make the notification Mandatory, type M and press \<Enter\>.

The notification should now be enabled.

### (Optional) Change the Name on the Button from VistaWeb to JLV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Joint Legacy Viewer (JLV) is a new way to view remote data and will eventually replace VistaWeb. Some sites may not switch to JLV until VistAWeb is decommissioned, while others may choose to transition sooner. This transition should be made in collaboration with local Informatics staff and the JLV team.

When your site transitions to the JLV for reviewing external remote data, you will use the General Parameter Tool option (XPAR Edit) to set the ORWRP LEGACY VIEWER LABEL parameter to set the text to display JLV for those users that are now using JLV.

The ORWRP LEGACY VIEWER LABEL parameter changes only the text on the button. A different parameter controls the implementation of the JLV for a site.

Eventually, all sites will change over to the Joint Legacy Viewer. For now, while VistaWeb is still active, sites can elect to use VistaWeb, JLV, or a mix of both. As with all CPRS parameters, the more specific level takes precedence over the more general. For example, if you set the System level at JLV, the button will read JLV for the whole site unless the parameter was set differently for a Division or User. If set at the Division level, the specified division will have different text.

To make the change, use the General Parameter Tools \| Edit Parameter Values on the Vista CPRS Configuration (IRM) menu.

Remember, this parameter only affects the text on the button.

See the example below.

Select OPTION NAME: XPAR

1 XPAR EDIT BY TEMPLATE Edit Parameter Values with Template

2 XPAR EDIT KEYWORD Edit Parameter Definition Keyword

3 XPAR EDIT PARAMETER Edit Parameter Values

4 XPAR LIST BY ENTITY List Values for a Selected Entity

5 XPAR LIST BY PACKAGE List Values for a Selected Package

Press \<Enter\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 3 XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: ORWRP LEGACY VIEWER LABEL JLV Remote Button Label Name

ORWRP LEGACY VIEWER LABEL may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Division DIV \[choose from INSTITUTION\]

3 System SYS \[TEST.DAYTON.MED.VA.GOV\]

Enter selection: 3 System TEST.DAYTON.MED.VA.GOV

--- Setting ORWRP LEGACY VIEWER LABEL for System: TEST.DAYTON.MED.VA.GOV ---

JLV REMOTE BUTTON LABEL NAME: JLV//

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To revert back to the previous version of CPRS, v.30.c, site or region personnel would back up some important files, install the back out patch, and redistribute the 30.c GUI.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on v31a. There are only minor changes to this version—including the major change to enable two-factor authentication.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the three test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of OR\*3\*434. The sites either passed or failed any item based on testing. The tests were performed by Clinical Application Coordinators at each site who are familiar using the CPRS application. The test cases were then delivered with concurrence by the sites to the CPRS development team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the CPRS application or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out CPRS v31a would remove two-factor authentication. Currently, two-factor authentication will soon be required to login to CPRS, but technical issues may cause delays in implementing 2FA.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out the patch should only be considered if there is a catastrophic failure of CPRS v31a. The back out would be accomplished in two phases: first, backing up several files and two, a patch will be installed and will accomplish the back out.

### Installing the Back-Out Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for CPRS v31a is in the event of a catastrophic failure.

1.  Contact the CPRS v31a implementation team to notify them there has been a catastrophic failure with v31a. Use the mail group: OIT PD CPRS Implementation Team <OITPDCPRSImplementationTeam@va.gov>. In addition, phone/use Lync to contact:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

2.  If the decision is made to proceed with back-out and rollback, coordinate with the appropriate IT support, local and ITOPS, to schedule the time to update the necessary options, make parameter changes, and to push out / install the previous GUI executable, Mental Health DLL and Vitals DLL.
3.  Install patch OR\*3.0\*460.
4.  Using the method of distribution appropriate to your site (share, individual PC, etc), redistribute the CPRS v30c executable.
5.  Using the method of distribution appropriate to your site (share, individual PC, etc), redistribute the Mental Health and Vitals DLLs distributed with CPRS v30b.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the OPTION file (#19) for OR CPRS GUI CHART is set to CPRSChart version 1.0.30.75.
2.  Ensure the v30C executable launches properly.
3.  Perform regression testing to verify that login with the username and password works and that the VistaWeb link is working.
4.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no database changes specifically related to CPRS v31a except for the addition of new parameters and a new order dialog. The parameters are dormant unless CPRS v31a is active, so no rollback is required.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the system starts to experience severe performance problems or if the new software introduces patient safety issues that can only be resolve by uninstalling the patch.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risk for a rollback should be minimal, however whenever changing the software there is always the possibility of unknown adverse impact happening.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Take the users off of CPRS.
2.  Install the back out patch OR\*3.0\*460.
3.  If the rollback is happening within the week of the initial install, then sites should re-install the data that was backed up in the pre-installation of the CPRS v31a.
4.  If the rollback is happening after the first week of the initial install, then sites will need to verify that the SD RTC order dialog has been removed from all menus, order sets, and Reminder Dialogs.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the system works as expected. Verify the SD RTC order dialog has been remove from all menus, order sets, and reminder dialogs.

# Example Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: CPRS V31A COMBINED BUILD 1.0 6/7/17@13:45:21

=\> CPRS V31A ;Created on Jun 06, 2017@19:42:11

This Distribution was loaded on Jun 07, 2017@13:45:21 with header of

CPRS V31A ;Created on Jun 06, 2017@19:42:11

It consisted of the following Install(s):

CPRS V31A COMBINED BUILD 1.0 OR\*3.0\*434 GMRV\*5.0\*34 YS\*5.01\*128

Checking Install for Package CPRS V31A COMBINED BUILD 1.0

Install Questions for CPRS V31A COMBINED BUILD 1.0

Checking Install for Package OR\*3.0\*434

Will first run the Environment Check Routine, ORY434

Install Questions for OR\*3.0\*434

Incoming Files:

100 ORDER (Partial Definition)

> **NOTE:** You already have the 'ORDER' File.

100.9 OE/RR NOTIFICATIONS (including data)

> **NOTE:** You already have the 'OE/RR NOTIFICATIONS' File.

I will OVERWRITE your data with mine.

100.98 DISPLAY GROUP (including data)

> **NOTE:** You already have the 'DISPLAY GROUP' File.

I will REPLACE your data with mine.

101.41 ORDER DIALOG (including data)

> **NOTE:** You already have the 'ORDER DIALOG' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// YES

Checking Install for Package GMRV\*5.0\*34

Install Questions for GMRV\*5.0\*34

Checking Install for Package YS\*5.01\*128

Install Questions for YS\*5.01\*128

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TEMINAL

--------------------------------------------------------------------------------

Install Started for CPRS V31A COMBINED BUILD 1.0 :

Jun 07, 2017@13:51:33

Build Distribution Date: Jun 06, 2017

Installing Routines:

Jun 07, 2017@13:51:33

Install Started for OR\*3.0\*434 :

Jun 07, 2017@13:51:33

Build Distribution Date: Jun 06, 2017

Installing Routines:

Jun 07, 2017@13:51:33

Installing Data Dictionaries:

Jun 07, 2017@13:51:33

Installing Data: ..............................................................

Jun 07, 2017@13:51:45

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Installing REMOTE PROCEDURE

Installing OPTION

Installing PARAMETER DEFINITION

Jun 07, 2017@13:51:47

Running Post-Install Routine: POST^ORY434

Adding 'Clinic Scheduling' Display Group to

the 'All Services' Display Group...

Display group already attached

DONE

Adding 'Clinic Scheduling' Display Group to

parameter 'ORWOR CATEGORY SEQUENCE'...

DONE

Loading parameter values for new notification...

Finished loading new notification values

Updating Routine file...

The following Routines were created during this install:

ORD2

ORD21

ORD210

ORD211

ORD212

ORD213

ORD214

ORD22

ORD23

ORD24

ORD25

ORD26

ORD27

ORD28

ORD29

Updating KIDS files...

OR\*3.0\*434 Installed.

Jun 07, 2017@13:51:47

Not a production UCI

NO Install Message sent

Install Started for GMRV\*5.0\*34 :

Jun 07, 2017@13:51:47

Build Distribution Date: Jun 06, 2017

Installing Routines:

Jun 07, 2017@13:51:47

Running Post-Install Routine: EN^GMV34PST

Updating DLL parameter.

Updating Routine file...

Updating KIDS files...

GMRV\*5.0\*34 Installed.

Jun 07, 2017@13:51:47

Not a production UCI

NO Install Message sent

Install Started for YS\*5.01\*128 :

Jun 07, 2017@13:51:47

Build Distribution Date: Jun 06, 2017

Installing Routines:

Jun 07, 2017@13:51:47

Running Post-Install Routine: POST^YS128PS0

Updating Routine file...

Updating KIDS files...

YS\*5.01\*128 Installed.

Jun 07, 2017@13:51:47

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

CPRS V31A COMBINED BUILD 1.0 Installed.

Jun 07, 2017@13:51:47

Install Completed