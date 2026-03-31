---
title: OR*3*423 Deployment, Installation, Back-Out, and Rollback Guide CPRS GUI 30C
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: CPRS GUI 30C
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*423
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - cprs
  - back
  - rollback
  - deployment
  - site
  - procedure
  - class
page_count: 0
word_count: 4087
section_count: 31
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_423_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_423_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

CPRS v30c (OR\*3\*423)

Deployment, Installation, Back-Out, and Rollback Guide

![](or-3-423-deployment-installation-back-out-and-rollback-guide-cprs-gui-30c/001.png)

August 2016

Office of Information and Technology (OI&T)

Revision History

| Date      | Version | Description | Author                         |
|---------------|-------------|-----------------|------------------------------------|
| June 22, 2016 | 1.0         | Initial Draft   | <span class="mark">REDACTED</span> |

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
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [OR\3\423 KIDS Installation](#or3423-kids-installation)
    - [CPRS v30C GUI Installation](#cprs-v30c-gui-installation)
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
This document describes how to deploy and install CPRS v30C*,* as well as how to back-out the product and rollback to a previous version.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom CPRS v30C will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, a communications plan, and a rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v30C project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system. The installation of CPRS v30C is required for the future installations of CPRS GUI releases (such as V31 and V32).

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v30C and associated M patches are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. CPRS v30C utilizes existing, nationally released security controls to control access.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No one single entity is in charge of decision making for deployment, installation, back out and rollback of CPRS v30c. Rather, the Critical Decision Point representatives (commonly referred to as the three in the box) under the Veterans In Process will meet and approve deployment and install from an OI&T perspective. If an issue with the software arises, then the same three in the box members under VIP will meet along with input from Patient Safety and Health Product Support to initiate a back out and rollback decision of the software along with Region and Site leadership. The following table provides CPRSv30c project information.

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
<td>Site personnel in conjunction with IT support – which may be local or regional.</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
<td>After national release.</td>
</tr>
<tr class="even">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or regional.</td>
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
<td>Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
<td>Deployment</td>
<td>Execute deployment</td>
<td>After national release.</td>
</tr>
<tr class="odd">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
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

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release, the patch OR\*3\*423 will be released from the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing and deployment to production will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no timeline specifically for deployment. This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period for the release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CPRS v30C deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v30C will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway. There are also instances, such as the Meds by Mail personnel who may not have a VistA instance, but will have the executable deployed.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to IOC sites for verification of functionality. Once that testing is completed and approval is given for national release, CPRS v30C (OR\*3\*423) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

- Salem VAMC
- Central Plains HCS
- Visn2 Upstate New York HCS
- Hines VAMC

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for CPRS v30C. A fully patched VistA system is the only requirement.

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

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an SDE Bulletin prior to the release of CPRS v30C advising them of the upcoming release.

CPRS v30C will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch OR\*3\*423 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v30C assumes a fully-patched VistA system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please check your system to verify that the following, previously released national patches are installed:

- OR\*3\*269
- OR\*3\*348
- OR\*3\*350
- OR\*3\*389

  This patch (VistA KIDS Build) should take less than 5 minutes to install. The time for the post-install rebuild of the cross-references as well as the move of the supply quick orders will depend upon the size of the ORDER file (#100) and the number of supply quick orders, respectively.

  The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation install, etc.).

  It is recommended that the installation be done during non-peak hours. If at all possible, the users should not be in CPRS when the KIDS installation is being performed.

  Warning: The GMRCOR CONSULT entry in the ORDER DIALOG (#101.41) file will be overwritten. Please review and save your entry in the event you have custom/site modifications that will need to be reapplied after installation. The changes will have to be applied manually so that the new GMRCOR CONSULT dialog retains the defect repair being done in OR\*3\*423.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v30C is being released as two host files.

The preferred method is to retrieve files from download.vista.med.va.gov.

This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following

OI Field Offices:

 

<span class="mark">REDACTED</span>

 

Documentation can also be found on the VA Software Documentation Library at:

<http://www.va.gov/vdl/>

CPRS v30C files

| CPRS v30 files to be downloaded | File Contents           | Download Format |
|---------------------------------|-------------------------|-----------------|
| OR_30_423.KID                   | M changes for CPRS v30C | ASCII           |
| OR_30_423.ZIP                   | CPRS executable         | Binary          |

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

Installation of CPRS v30C requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.
- Loader installs – access/ability to upload new executable to the GOLD directory.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### OR\*3\*423 KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

1.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
2.  Next, select ‘Load a Distribution’. When prompted “Enter a Host File: “, enter \<directory\>OR_30_423.KID (where directory represents the location where you stored the KIDS file).
3.  When prompted: Build OR\*3.0\*423 has an Environmental Check Routine, Want to RUN the Environment Check Routine? YES//”, respond YES.
4.  When prompted: GMRCOR CONSULT in ORDER DIALOG (#101.41) will be overwritten. Continue? NO//” respond YES, ensure you have followed the pre-installation instructions regarding saving off the dialog in the event you have site modifications.
5.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
6.  From this menu, you may elect to use the following options
1.  Backup a Transport Global
2.  Compare Transport Global to Current System
3.  Verify Checksums in Transport Global
7.  Use the Install Package(s) options and select the package OR\*30\*423.
8.  When prompted for “GMRCOR CONSULT in ORDER DIALOG (#101.41) will be overwritten. Continue? NO//”, Respond YES.
9.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install?”, respond NO.
10. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
11. When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.

After the installation is complete, the installer will receive two different messages.

The first one is related to some updates that required changes to the order check expert system and should be received immediately:

<span class="mark">Subj: Order Check Compiler Status</span>  \[#79192\] 07/22/16@11:27  14 lines

From: POSTMASTER  In 'OR' basket.   Page 1

-------------------------------------------------------------------------------

  The Order Check routine compiler has completed normally

      on JUL 22,2016 at 11:27 by \[12098\]  PATCH,INSTALLER

       ORDER CHECK EXPERT version 1.01 released OCT 29,1998

                   Elapsed time: 0 minutes 4 seconds

                                 Automatic Mode

           Execution Trace Mode: OFF

      Elapsed time Logging Mode: 

          Raw Data Logging Mode: OFF

        Lines of code generated: No longer tracked

Enter message action (in OR basket): Ignore//

The second message is related to the C and D cross-references being rebuilt. That message will only be sent when that rebuild is completed. Depending upon the size of your ORDER file (#100), that rebuild may take quite a bit of time:

<span class="mark">Subj:</span> <span class="mark">PATCH OR\*3.0\*423 ORDER INDEX CORRECTION STATUS</span>  \[#79193\] 07/22/16@11:27 1 line

From: POSTMASTER  In 'OR' basket.   Page 1

-------------------------------------------------------------------------------

The file \#100 index correction from OR\*3.0\*423 was successfully completed.

Enter message action (in OR basket): Ignore//

### CPRS v30C GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the CPRS GUI executable. Download the ZIP file and extract all the files.

#### CPRS GUI Methods of Installation

The following methods of installation of CPRS are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

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

> This is the “standard” method of installation where the GUI executable (CPRSChart.exe), and ancillary files (DLLs, Help files etc.), are installed on and run from the user's local workstation. In normal day-to-day operation, the user's shortcut executes a locally installed copy of CPRSLoader.exe which looks in a pre-configured network “Gold Path” (specified in a command line parameter) to see if there is a later version of CPRSChart.exe ready to be installed. If not, then execution passes to the locally installed version of CPRSChart.exe. If an updated version is found on the Gold Path, then a silent installation of the new version takes place, following which the newly installed version of CPRSChart.exe is executed on the local workstation.

> This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file (CPRSLoader.msi) to each user's workstation, typically accomplished via SCCM. This is outside the scope of CPRS development. A National package (CPRS Loader 1.30.40) has been prepared and made available to Regional COR Client Technologies leadership.

> The CPRS Loader installation package can be found on the System Center Configuration Manager (SCCM) central site at the following locations.

> Note: The Loader has not been updated for CPRS v.30.c. There is no need to update the Loader. This is being left here for reference only.

> Package Name: 1VA - VA CPRS Loader

> Package ID: 1VA004E7, R03002C4

> Test Location:

> VA Central Site Packages \> Test \> 1VA - VA CPRS Loader

> Production Location:

> VA Central Site Packages \> Production \> 1VA – Applications \> 1VA - VA CPRS Loader

> All details of the SCCM package can be found in the build document and should be reviewed before deployment:

<span class="mark">REDACTED</span>

> The CPRSChart.exe component of the update is held in a Microsoft Software Patch (MSP) file (CPRSChart.msp) which is copied to the network Gold Path location—that should be all that is required for a normal CPRS version update for sites using this method. The exception is if a new version of CPRS Loader is also being released, in which case the cycle begins again with the distribution to users' workstations of the new CPRSLoader.msi (before the new CPRSChart.msp is copied to the network Gold Path)—this is the circumstance in which CPRS v30b is being released.

> The CPRS deployment software distribution will include an appropriate version of the CPRS Microsoft patch file (named CPRS_XX_YY.msp, where XX is the current version number for CPRS, and YY is the current build number. At this point the current file name is CPRS_30_72.msp). This file has the named version of CPRSChart embedded within it, along with any updated ancillary files. Also included in the deployment software distribution will be a .VER file. This file will have the same name as the MSP file, with only the file extension changed. As an example, the .VER file for CPRS_30_72.MSP will be named CPRS_30_72.VER. To be effective, the .VER file must be placed in the same Gold Path in which the .MSP file was placed. The .VER is optional but beneficial. It will allow the CPRS loader to much more quickly find an appropriate version of CPRSChart.exe for use with the current VistA system. Including the VER file in the Gold Path can shorten CPRS start times substantially.

> For the convenience of local System Administrators, the file CPRSLoader.msi is also included in the release package, in case they need to manually install it on a workstation.

- Direct Access to a Local Copy of CPRSChart.exe (bypassing the loader)

> In cases where a site's network performance is weak enough that CPRSLoader.exe, in checking the Gold Path every time a user starts CPRS, introduces unacceptable delays, some sites have elected to bypass CPRSLoader.exe altogether and have the users’ shortcuts point directly to a local installation of CPRSChart.exe. The downside to this approach is that a future release of CPRSChart.exe will not be automatically picked up from the Gold Path by that workstation and the new CPRSChart.exe (plus any additional changed DLLs and Help files) will need to be pushed out to workstations by other means, such as an SCCM package.

> NOTE: There is a national SCCM package to distribute the Cprschart.exe file to help sites or regions install the CPRS GUI.

> An alternative, hybrid, version of this method would be to have two shortcuts for the users: One, for day-to-day use, which points directly to the local CPRSChart.exe and a second, to be used only for updating, which points to CPRSLoader.exe.

- Manual install:

  This method is used primarily for advanced users and at testing locations.  
  This method is somewhat changed from that used previously for Windows XP workstations.
1.  Locate the OR_30_423.ZIP and unzip the file.
2.  Copy the CPRSChart.exe to a test directory, for example, C:\cprstest. You may need to create this new directory.

    Note: You may need to have a user with Administrator rights complete this step.
3.  Create a Shortcut and name it “Test CPRSv30”. This is to give the user another visual cue that this is not the normal CPRS icon.

    ![](or-3-423-deployment-installation-back-out-and-rollback-guide-cprs-gui-30c/002.png)
4.  Copy the borlandmm.dll file into the same directory as cprschart.exe (for example, c:\cprstest). This file should be in the same directory as the CPRSChart.exe for CPRS v30C.
5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  Enter IP and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

> ![](or-3-423-deployment-installation-back-out-and-rollback-guide-cprs-gui-30c/003.png)

> Example of what the shortcut properties dialog might look like.

> The server and port number shown above are not real and are for example only.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Launch the CPRS GUI and verify the splash screen now announces that you are running version 30.75.
2.  Execute the provided test scripts and verify that all tests pass.

    ![](or-3-423-deployment-installation-back-out-and-rollback-guide-cprs-gui-30c/004.png)

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One site has reported a sporadic issue with the date range selection prompts not displaying for some reports, such as the Lab Worksheet. The issue only occurred when the OR REPORT DATE SELECT TYPE parameter is set to NO or blank.

If this occurs at your site, you can change the OR REPORT DATE SELECT TYPE to YES, which will toggle your display to the radio button view.

To set this parameter, use these steps:

1.  In Vista, go to the ORMGR menu.
2.  Go to the CPRS Configuration (IRM) … menu by typing IR and pressing \<Enter\>.
3.  Select General Parameter Tools by typing XX and pressing \<Enter\>.
4.  Select Edit Parameter Values by typing EP and pressing \<Enter\>.
5.  In the Select PARAMETER DEFINITION NAME: prompt, type OR REPORT DATE SELECT TYPE and press \<Enter\>.
6.  Select the Package level by typing 3 and pressing \<Enter\>.
7.  At the Setting OR REPORT DATE SELECT TYPE for System: prompt, type Yes and press \<Enter\>.

Select CPRS Configuration (Clin Coord) Option:

CL Clinician Menu ...

NM Nurse Menu ...

WC Ward Clerk Menu ...

PE CPRS Configuration (Clin Coord) ...

IR CPRS Configuration (IRM) ...

Select CPRS Manager Menu Option: IR CPRS Configuration (IRM)

Select CPRS Configuration (IRM) Option: XX General Parameter Tools

Select General Parameter Tools Option: EP Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: OR REPORT DATE SELECT TYPE Reports/Lab Tab Date Select Type

OR REPORT DATE SELECT TYPE may be set for the following:

1 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

2 Division DIV \[choose from INSTITUTION\]

3 System SYS \[CPRS30.FO-SLC.MED.VA.GOV\]

Enter selection: 3 System CPRS30.FO-SLC.MED.VA.GOV

-- Setting OR REPORT DATE SELECT TYPE for System: -- Yes/No: YES//

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A patch has been created (OR\*3\*432) that will revert the OE/RR components to their pre-v30C state. This includes everything transported in the OR\*3\*423 (CPRS v30C) build.

To revert the CPRS GUI, the 30.72 (CPRS v30B) GUI would have to be redistributed.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on v30C. This was a maintenance release to correct defects discovered in v30B. There was no additional functionality included.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the four test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of OR\*3\*423. The sites either passed or failed any item based on testing. The tests were performed by Clinical Application Coordinators at each site who are familiar using the CPRS application. The test cases were then delivered with concurrence by the sites to the CPRS development team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the CPRS application and a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out CPRS v30C would result in the re-instatement of the two patient safety issues being corrected as well as the issues addressed in CPRS v30C.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for CPRS v30C is in the event of a catastrophic failure.

Contact the CPRS v30C implementation team to notify them there has been a catastrophic failure with v30C. Use the mail group: OIT PD CPRS Implementation Team <span class="mark">REDACTED</span>

1.  . In addition, phone/use Lync to contact:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

2.  If the decision is made to proceed with back-out and rollback, the CPRS development team will send you a copy of the patch OR\*3\*432 as well as give you the instructions on downloading the CPRS v30B executable.
3.  Coordinate with the appropriate IT support, local and regional, to schedule the time to install OR\*3\*432 and to push out / install the previous GUI executable.
4.  Once OR\*3\*432 and CPRS v30B have been installed, verify operations before making available to all staff.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the OPTION file (#19) for OR CPRS GUI CHART is set to CPRSChart version 1.0.30.72.
2.  Ensure the v30B executable launches properly.
3.  Perform regression testing on Orders, Notes, Consults and Reports.
4.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any rollback that is required will be performed by the back-out patch OR\*3\*432. There are only two database updates in OR\*3\*423 (v30C). The first is to correct the ‘C’ and ‘D’ cross-references. There is no need to rollback these changes.

The second relates to quick orders using the PSO SUPPLY dialog. The movement from this dialog back to PSO OERR is necessary for supply quick orders to function appropriately so this change will not be rolled back.

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

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A