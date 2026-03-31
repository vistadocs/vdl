---
title: OR*3*509 Windows 10 Deployment, Installation, Back-Out, and Rollback Guide CPRS GUI 31A
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Windows 10  CPRS GUI 31A
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*509
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
  - installation
  - back
  - windows
  - rollback
  - deployment
  - install
  - procedure
page_count: 0
word_count: 4232
section_count: 32
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_509_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_509_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

CPRS v31a Windows 10 (OR\*3\*509)

Deployment, Installation, Back-Out, and Rollback Guide

![](or-3-509-windows-10-deployment-installation-back-out-and-rollback-guide-cprs-gui/001.png)

April 2019

Office of Information and Technology (OI&T)

Revision History

| Date       | Version | Description    | Author                         |
|----------------|-------------|--------------------|------------------------------------|
| April 30, 2019 |             | Updated to v31.118 | <span class="mark">REDACTED</span> |
| April 16, 2019 | 1.0         | Initial Draft      | <span class="mark">REDACTED</span> |

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
  - [Access Requirements and Skills Needed for Installation](#access-requirements-and-skills-needed-for-installation)
  - [Installation Procedure](#installation-procedure)
    - [CPRS v31a Windows 10 Multi-Package Build KIDS Installation](#cprs-v31a-windows-10-multi-package-build-kids-installation)
    - [CPRS v31a Windows 10 GUI Installation](#cprs-v31a-windows-10-gui-installation)
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
    - [Back-Out Steps](#back-out-steps)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Sample Installation](#sample-installation)
This document describes how to deploy and install CPRS v31a Windows 10*,* as well as how to back-out the product and rollback to a previous version.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom CPRS v31a Windows 10 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, a communications plan, and a rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v31a Windows 10 project is meant to be installed on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system. The installation of CPRS v31a Windows 10 is required for the future installations of CPRS GUI releases (such as v31b and v32).

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a Windows 10 is expected to be installed on existing VistA platforms.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No single entity oversees decision making for deployment, installation, back-out and rollback of CPRS v31a Windows 10. Rather, the Critical Decision Point representatives (commonly referred to as the three in the box) under the Veterans In Process (VIP) will meet and approve release from a business perspective.

If an issue with the software arises that would require a national rollback, then the same three in the box members under VIP will coordinate with several groups (including Patient Safety Health Product Support, Information Technology Operations Service (ITOPS), and Site leadership) to decide whether a back-out and rollback of the software is necessary. The Facility Chief Information Officer (FCIO) has the final authority to require the patch back-out and data rollback and accept the associated risks.

The following table provides CPRS v31a Windows 10 project information.

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 33%" />
<col style="width: 15%" />
<col style="width: 26%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Team</strong></th>
<th><strong>Phase/Role</strong></th>
<th><strong>Tasks</strong></th>
<th><strong>Project Phase (See Schedule)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
<td>After national release</td>
</tr>
<tr class="even">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment</td>
<td>After national release</td>
</tr>
<tr class="odd">
<td></td>
<td>Site personnel</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
<td>After national release</td>
</tr>
<tr class="even">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
<td>Deployment</td>
<td>Execute deployment</td>
<td>After national release</td>
</tr>
<tr class="odd">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
<td>Installation</td>
<td>Plan and schedule installation</td>
<td>After national release</td>
</tr>
<tr class="even">
<td></td>
<td>N/A – will work under the VistA ATO and security protocols</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>N/A – no equipment is being added</td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>N/A – no new functionality is being introduced</td>
<td>Installation</td>
<td>Coordinate training</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Facility CIO and IT support – which may be local or regional</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
<td>After national release</td>
</tr>
<tr class="even">
<td></td>
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the CPRS Development Team during the compliance period. At the end of the compliance period, support will be transitioned to VistA Maintenance</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
<td>After national release</td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because of the importance of the features released with CPRS v31a Windows 10, the deployment will be an expedited release with an 18-day compliance window.

There are currently no site-facing on-line meetings or training planned for this deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The provisional timeline calls for the patch to be released sometime in May of 2019 with an 18-day compliance period after national release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CPRS v31a Windows 10 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a Windows 10 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway. There are also instances, such as the Meds by Mail personnel who may not have a VistA instance but will have the executable deployed.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capabilities (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, CPRS v31a Windows 10 will be deployed to all VistA systems.

The Production (IOC) Test sites are:

- Central Texas
- Little Rock
- Minneapolis
- Pittsburgh

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

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

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an SDE Bulletin prior to the release of CPRS v31a Windows 10 advising sites of the upcoming release.

CPRS v31a Windows 10 will be deployed using the normal patch deployment process. After the patch is nationally released, sites will have 18 days to install CPRS v31a Windows 10. There will be a GUI executable.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a Windows 10 assumes a fully-patched VistA system.

## Backing Up Important Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do NOT permanently delete the existing CPRS GUI executable, 31.116 (file version 1.0.31.116). In the unlikely event a backout is needed, redistributing the 31.116 executable will be necessary.

> Important: These files will be important if, for some reason, there was a need for a rollback. Please retain these files for at least two weeks after installing the patch

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please check your system to verify that the following, previously released national patches are installed:

- OR\*3.0\*434
- GMRV\*5.0\*38 (although not required, this is recommended because it corrects some Windows 10 issues with Vitals)

The VistA PackMan should take less than 5 minutes to install. The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.).

It is recommended that the installation be done during non-peak hours. If possible, users should not be in CPRS when the VistA installation is being performed.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a Windows 10 is being released as one zip file plus a PackMan patch message from the National Patch Module. Documentation can also be found on the VA Software Documentation Library at: <http://www.va.gov/vdl/>

> CPRS v31a Windows 10 files

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 43%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>CPRS v31a Windows 10 files to be downloaded</th>
<th>File Contents</th>
<th>Download Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR_30_509.ZIP</td>
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
<p>Help directory</p>
</blockquote></li>
<li><blockquote>
<p>RoboEx32.dll</p>
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

## Access Requirements and Skills Needed for Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of CPRS v31a Windows 10 requires the following:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.
- Loader installs – access/ability to upload new executable to the GOLD directory.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CPRS v31a Windows 10 Multi-Package Build KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. For the installation, it is recommended that users are off the system.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
4.  From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the patch number, OR\*3.0\*509.
    1.  Backup a Transport Global.
    2.  Compare Transport Global to Current System.
    3.  Verify Checksums in Transport Global.
5.  Use the Install Package(s) options and select the patch to install, OR\*3.0\*509.
6.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install?”, respond NO.
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
8.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.
9.  If prompted, ‘Delay Install (Minutes): (0-60): 0//’, respond 0.

### CPRS v31a Windows 10 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several different ways to install the CPRS GUI executable (CPRSChart.exe). Which method you choose depends on your system configuration and how CPRS is support at your site.

#### CPRS GUI Methods of Installation

The following methods of installation of CPRS are available. Sites' choice of which method(s) to use will depend upon ITOPS/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant the use of more than one of the options below.

NETWORK (SHARED) INSTALLATION

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPRSChart.exe) across the LAN.

The GUI executable (CPRSChart.exe), and ancillary files (DLLs, Help files etc.), are copied to a network shared location. Users are provided with a desktop shortcut to run CPRSChart.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the “Target” field of the shortcut properties

At the time of a CPRS version update the copy of CPRSChart.exe (and any updated ancillary files) is simply replaced, on the network share, with the new version.

Any users requiring access to another site's CPRS system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of CPRS (e.g. during a phased deployment, when sites are temporarily not all on the same version, or for testing purposes) a different version of CPRSChart.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

> Note: The version of CPRSChart a user executes must always match the patch-level version of the VistA system targeted

CITRIX INSTALLATION

The GUI executable (CPRSChart.exe) and ancillary files (DLLs, Help files etc.) are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> Note: For issues with CAG, please contact your local or national help desk

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

During a phased deployment of a new version of CPRS, if a Citrix Farm is serving users who are scheduled to deploy at different times, the Farm administrator may be required to temporarily maintain hosts with both the old and the new versions of CPRSChart.exe available.

DIRECT ACCESS TO A LOCAL COPY OF CPRSCHART.EXE (BYPASSING THE LOADER)

Some sites have elected to install CPRS on local workstations (bypassing CPRSLoader.exe) and have the users’ shortcuts point directly to a local installation of CPRSChart.exe. The advantage to this method is usually increased performance because CPRS is launched locally, rather than from a server. The downside to this approach is maintenance. Each future release of CPRSChart.exe will not be automatically picked up from the Gold Path by that workstation, and the new CPRSChart.exe (plus any additional changed DLLs and Help files) will need to be pushed out to workstations by other means, such as an SCCM package.

> NOTE: There is a national SCCM package to distribute the Cprschart.exe file to help sites or ITOPS install the CPRS GUI

An alternative, hybrid, version of this method would be to have two shortcuts for the users: One, for day-to-day use, which points directly to the local CPRSChart.exe and a second, to be used only for updating, which points to CPRSLoader.exe.

MANUAL INSTALL

This method is used primarily for advanced users and at testing locations. Note: You may need to have Administrator rights to complete these steps.

1.  Locate the OR_30_509.ZIP and unzip the file.
2.  If this is an installation for a conventional, day-to-day CPRS user, then all files are typically copied into C:\Program Files (x86)\CPRS\\ or C:\Program Files\CPRS\\.

If this is an installation for a secondary use (e.g. testing or accessing a different version of CPRS), then copy all files into a different location than the conventional path above (e.g. "C:\Program Files (x86)\CPRSTest" or other appropriate naming).

> **NOTE:** The borlandmm.dll should reside in the same directory as CPRSChart.exe.

3.  Create a Shortcut and name it “Test CPRSv31a Windows 10”. This is to give the user another visual cue that this is not the normal CPRS icon.

    ![](or-3-509-windows-10-deployment-installation-back-out-and-rollback-guide-cprs-gui/002.png)
4.  Determine the DNS server name or IP address for the appropriate VistA server.
5.  Determine the Broker RPC port for the VistA account.
6.  Enter IP and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

> ![](or-3-509-windows-10-deployment-installation-back-out-and-rollback-guide-cprs-gui/003.png)

> Example of what the shortcut properties dialog might look like.

The server and port number shown above are not real and are for example only.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Launch the CPRS GUI and verify the splash screen now announces that you are running version 31.118.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new system configuration is required with the installation of CPRS v31a Windows 10.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To revert to the previous version of CPRS v31a, site or region ITOPS personnel would edit a VistA option and redistribute the v31a 1.0.31.116 GUI. Details and examples of the edits are included later in section 5.6.1.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on v31a Windows 10. There are only minor changes to this version.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the four test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of OR\*3\*509. The sites either passed or failed any item based on testing. The tests were performed by Clinical Application Coordinators at each site who are familiar using the CPRS application. The test cases were then delivered with concurrence by the sites to the CPRS development team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the CPRS application or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out CPRS v31a Windows 10 would restore known incompatibilities when using CPRS on a Windows 10 computer. This decision would also delay the enterprise deployment of Windows 10 into clinical areas and adversely affect VA compliance with Maintaining Internal Systems and Strengthening Integrated Outside Networks (MISSION) Act of 2018.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out the patch should only be considered if there is a catastrophic failure of CPRS v31a Windows 10. The back-out would be accomplished in two phases: first, editing an OPTION file entry in VistA and two, re-deploying the CPRS v31a 1.0.31.116 GUI executable.

### Back-Out Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for CPRS v31a Windows 10 is in the event of a catastrophic failure.

1.  Contact the CPRS v31a Windows 10 implementation team to notify them there has been a catastrophic failure with v31a Windows 10. Use the mail group: OIT PD CPRS Implementation Team <OITPDCPRSImplementationTeam@va.gov>. In addition, phone/use Skype to contact:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

2.  If the decision is made to proceed with back-out and rollback, coordinate with the appropriate IT support, local and ITOPS, to schedule the time to update the necessary option and to push out / install the previous GUI executable.
3.  Edit OR CPRS GUI CHART in the OPTION (#19) file.
    1.  In VistA Menu Management \[XUMAINT\], use the 'Edit options' \[XUEDITOPT\] option and update the MENU TEXT field to replace "118" with "116".

> Select OPTION to edit: OR CPAS GUI CHART CPRSChart version 1 0.31.118

> NAME: OR CPRS GUI CHART//

> MENU TEXT: CPRSChart version 1.0.31.118 Replace 118 With 116

> Replace

> CPRSChart version 1.0.31.116

> PACKAGE :

> OUT OF ORDER MESSAGE: ^

4.  Using the method of distribution appropriate to your site (share, individual PC, etc.), redistribute the CPRS v31a 1.0.31.116 executable. For detailed descriptions for re-installing 31a 1.0.31.116, refer to the CPRS v31a (OR\*3\*434) Deployment, Installation, Back-Out, and Rollback Guide, found on the Virtual Document Library.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the OPTION file (#19) for OR CPRS GUI CHART is set to CPRSChart version 1.0.31.116.
2.  Ensure the v31a 1.0.31.116 executable launches properly.
3.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no database changes specifically related to CPRS v31a Windows 10 except for updating the OPTION (#19) file entry OR CPRS GUI CHART. This option would be reset during the back-out procedure described above.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A since no database updates were done, except for the menu option.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the instructions in section 5.7 Back-Out Verification Procedure.

# Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: OR\*3.0\*509 4/16/19@09:58:05

=\> OR\*3\*509 TEST v118

This Distribution was loaded on Apr 16, 2019@09:58:05 with header of

OR\*3\*509 TEST v118

It consisted of the following Install(s):

OR\*3.0\*509

Checking Install for Package OR\*3.0\*509

Install Questions for OR\*3.0\*509

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME

------------------------------------------------------------------------

Install Started for OR\*3.0\*509 :

Apr 16, 2019@10:01:04

Build Distribution Date: Apr 15, 2019

Installing Routines:

Apr 16, 2019@10:01:04

Installing PACKAGE COMPONENTS:

Installing OPTION

Apr 16, 2019@10:01:05

Updating Routine file...

Updating KIDS files...

OR\*3.0\*509 Installed.

Apr 16, 2019@10:01:05

Not a production UCI

NO Install Message sent

Install Completed