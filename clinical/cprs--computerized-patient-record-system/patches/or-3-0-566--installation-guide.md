---
title: OR*3.0*566 Provider Role Tool Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Provider Role Tool
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*566
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - provider
  - install
  - tool
  - role
  - back
  - task
  - test
page_count: 0
word_count: 6847
section_count: 34
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_566_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_566_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

---
title: |
  <span id="_Hlk527034419" class="anchor"></span>Provider Role Tool (PRT)

  Deployment, Installation, Back-Out, and Rollback Guide (OR\*3\*566)  
---

![](or-3-0-566-provider-role-tool-installation-guide/001.png)

August 2021

Office of Information and Technology (OI&T)

Enterprise Program Management Office

Revision History

<table>
<caption><p><span id="_Toc79770229" class="anchor"></span>Table 4: CPRS Development Team Contacts</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 21%" />
<col style="width: 32%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Pages</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8/13/2021</td>
<td>0.14</td>
<td>19</td>
<td>OR*3*566 (Informational Patch): In the Configure Exception Parameters section, removed the CPRS parameters (OR CPRS EXCEPTION EMAIL, OR CPRS EXCEPTION LOGGER, OR CPRS EXCEPTION PURGE) and replaced them with PRT parameters.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>7/28/2021</td>
<td>0.13</td>
<td>ii-iii, 5, 8, 21</td>
<td>OR*3*453: Redacted the manual for the VA Document Library (VDL). Removed names in revision history, port numbers and links to software builds.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>07/15/2021</td>
<td>0.12</td>
<td>2,4,5,6,8,20,21</td>
<td>OR*3*453: Replaced v18 with v21, as in v1.0.453.21.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>06/23/2021</td>
<td>0.11</td>
<td>5,6,7</td>
<td>OR*3*453: Updated sections 4.3 (‘Download and Extract Files’) and 4.8.1 (‘Install OR*3.0*453’) because the installation method changed from a host file install to a PackMan install.<br />
Updated the build version to OR_30_453V21.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>04/05/2021</td>
<td>0.10</td>
<td>2,4,6,8,18,19, 20, 21</td>
<td>OR*3*453: Updated the “Assign a CPRS Tools Menu Item to Those Identified as Provider Role Tool GUI Users” section. Updated the build number to 18.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>07/30/2020</td>
<td>0.09</td>
<td><p>Title page, 1,2,3,4,5,6,7,8,13,</p>
<p>19,20,21,22,23</p></td>
<td>OR_3_453: Incorporated the reviewer’s comments.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>07/17/2020</td>
<td>0.08</td>
<td>2,4,5,6,8,20,21</td>
<td>OR*3*453: Updated the build number to 17.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>6/26/2020</td>
<td>0.07</td>
<td>2,4,5,6,8,20,21</td>
<td>OR*3*453: Updated the build number to 16, updated the back-out/rollback instructions</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/15/2020</td>
<td>0.06</td>
<td>ii,1,2,3,6,22</td>
<td>OR*3*453: Fixed accessibility issues and added information about the EPRTAU cross-rererence.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>7/9/2019</td>
<td>0.05</td>
<td>15</td>
<td>OR*3*453: Under ‘Section 5.1 Ensure that the Post Installation Routine Runs to Completion’: per developer, updated ‘Sample Kernel Installation &amp; Distribution System Menu’</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/20/2019</td>
<td>0.04</td>
<td>24</td>
<td>OR*3*453: Added ‘Configure Exception Parameter’ section</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>3/15/2019</td>
<td>0.04</td>
<td>11</td>
<td>OR*3*453: Removed Note reference to Vitals Manager</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>3/5/2019</td>
<td>0.03</td>
<td></td>
<td>OR*3*453: Updates per Developer review</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>2/28/2019</td>
<td>0.02</td>
<td></td>
<td>OR*3*453: Developer Review</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>1/25/2019</td>
<td>0.01</td>
<td></td>
<td>OR*3*453: Tech Writer review</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Toc79770229" class="anchor"></span>Table 4: CPRS Development Team Contacts

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

List of Tables

List of Figures

[Figure 1: Shortcut Icon Provider Role Tool [8](#_Toc79770249)](#_Toc79770249)

[Figure 2: Test ProviderRoleTool453 Properties [9](#_Toc79770250)](#_Toc79770250)

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
  - [Pre-installation Considerations](#pre-installation-considerations)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [Install OR\3.0\453](#install-or30453)
    - [Provider Role Tool GUI Installation](#provider-role-tool-gui-installation)
- [Post-Installation Considerations](#post-installation-considerations)
  - [Ensure that the Post Installation Routine Runs to Completion](#ensure-that-the-post-installation-routine-runs-to-completion)
  - [Assign the OR PRT Access Security Key to Those Identified as Provider Role Tool GUI Users](#assign-the-or-prt-access-security-key-to-those-identified-as-provider-role-tool-gui-users)
  - [Assign a CPRS Tools Menu Item to Those Identified as Provider Role Tool GUI Users](#assign-a-cprs-tools-menu-item-to-those-identified-as-provider-role-tool-gui-users)
  - [Configure Exception Parameters](#configure-exception-parameters)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
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
The purpose of this patch is to allow an Ordering Provider who is moving to a new role (e.g., transferring to DoD from VA, rotating from Cardiology to Oncology within the facility), to have his or her Patient Orders reassigned permanently to one or more Providers who will then receive alerts/notifications for those orders as of the transfer date/time. This reassignment is only for alerts, the ordering provider on the orders will remain the same.
A new Provider Role Tool Graphical User Interface (GUI) tool will be available to pull up an ordering provider’s patient orders for a date range selected by the end user. Using the GUI tool, the end user will be able to reassign those patient orders to one or more providers who must be able, at least generally, to receive alerts/notifications. Only patient orders in a signed state will be available for selection. See Post Installation instructions below to see how to set up security for users who need access to this new tool.
A new "EPRACDT" cross reference (index) on the ORDER file (#100) has been created to be able to quickly pull up order providers from the ORDER ACTIONS multiple field (.8) who are currently responsible for patient orders, so these can be reassigned.
Once new providers have been assigned patient orders, the end user can press the Apply Changes button to complete the reassignments. Each patient order will report back to the end user success or failure of reassignment. For example, one failure could occur if a patient order is being edited by another user.
Another new "EPRTRDT" cross reference (index) on the ORDER file (#100) has been created to allow a newly assigned provider's patient orders to be reassigned permanently to yet another provider. This may rarely occur but it is possible.
A new “EPRTAU” New Style cross reference (index) has also been created to facilitate the auditing of transfers.
This document describes how to deploy and install, how to back-out the product, and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how to install the Provider Role Tool (OR\*3.0\*453) patch as well as when, where, and to whom the Provider Role Tool GUI will be deployed and installed. The guide also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the Provider Role Tool patch (OR\*3.0\*453) and the associated Provider Role Tool GUI assumes a fully patched VistA system and a Windows system. In addition, the following specific patches must be installed:

- OR\*3.0\*42
- OR\*3.0\*377
- OR\*3.0\*471

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool patch (OR\*3.0\*453) will be installed on VistA servers. The associated GUI is 508 compliant.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No one single entity oversees decision making for deployment, installation, back out and rollback of Provider Role Tool v1.0.453.21. The OI&T management, business owners, and Application Coordinators under the Veterans in Process will approve deployment and install from a product development perspective. If an issue with the software arises, the Area Managers and other site leadership will meet along with input from Patient Safety and Health Product Support to initiate a back out and rollback decision of the software along with the IT Operations and Services personnel. The following table provides Provider Role Tool v1.0.453.21 project information.

<span id="_Toc79770227" class="anchor"></span>Table 1: Roles and Responsibilities

<table>
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
<p>The IT support will need to include person(s) to install the Kernel Installation and Distribution System (KIDS) build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network, and/or the Citrix access gateway</p></td>
<td>Deployment</td>
<td>Execute deployment</td>
</tr>
<tr class="odd">
<td><p>IT Operations and Services personnel.</p>
<p>The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network, and/or the Citrix access gateway</p></td>
<td>Installation</td>
<td>Plan and schedule installation</td>
</tr>
<tr class="even">
<td>N/A – will work under the VistA ATO and security protocols.</td>
<td>Installation</td>
<td>Ensure authority to operate and that the certificate authority security documentation is in place</td>
</tr>
<tr class="odd">
<td>N/A – no equipment is being added.</td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
</tr>
<tr class="even">
<td>N/A – no new functionality is being introduced.</td>
<td>Installations</td>
<td>Coordinate training</td>
</tr>
<tr class="odd">
<td>Facility CIO, IT Operations, and Services personnel</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
</tr>
<tr class="even">
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the HPS Clinical Sustainment team.</p></td>
<td>Post Deployment</td>
<td>Hardware, Software, and System Support</td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provider Role Tool features are included in the M side patch (OR\*3.0\*453) and a Provider Role Tool GUI component, both of which must be installed for the features to be available. The patch will be installed on the VistA server. However, because Provider Role Tool GUI is not needed for all users, only a small group of users will have access to the Provider Role Tool GUI. The GUI may be provided as a stand-alone shortcut, but can also be made available through a link on the user’s CPRS Tools menu.

The deployment will be a standard release with a 30-day compliance window.

There are currently no site-facing online meetings or training planned for this deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no timeline specifically for deployment. Installation will be at the site’s discretion, within the constraints of the compliance period for the release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Provider Role Tool v1.0.453.21 deployment.

- Provider Role Tool patch OR\*3\*453 will be installed on all VistA instances for all VistA databases.
- Sites must decide which individuals will be responsible for reassigning orders. These individuals must be given a security key and access to the Provider Role Tool GUI.
- The system must have the required patches installed.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provider Role Tool v1.0.453.21 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to IOC sites for verification of functionality. Once that testing is completed and approval is given for national release, Provider Role Tool v1.0.453.21 (OR\*3.0\*453) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

- Central Arkansas Veterans Health Care System
- Milwaukee, WI
- VA Black Hills Health Care System, SD

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system must have the required patches installed and a fully patched VistA system.

There are no specific hardware preparations required for patch OR\*3.0\*453 or the associated GUI.

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

As stated above, patch OR\*3.0\*453 requires a fully patched VistA system and the GUI requires a Windows operating system.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Communication with the Client Technologies group and Citrix Access Gateway administrators, may be required depending on the installation method chosen.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3.0\*453 installs on a standard VistA server and the GUI runs on a Windows operating system. There are no special hardware or operating system requirements.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch OR\*3\*453 may be installed with users on the system, although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. The length of time post-install before the functionality is usable will depend on the number of ORDER file (#100) ORDER ACTIONS multiple records that the New Style cross reference (index) "EPRACDT" will have to create entries for.

The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.).

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provider Role Tool is being released as a ZIP file containing the GUI file(s) plus a PackMan message.

The ZIP file is available at the following location: REDACTED

Documentation is available on the VA Software Documentation Library at:

[Computerized Patient Record System (CPRS)](https://www.va.gov/vdl/application.asp?appid=61)

<span id="_Toc79770228" class="anchor"></span>Table 3: Files to be Downloaded

| File Name        | File Contents                        | Download Format |
|------------------|--------------------------------------|-----------------|
| OR_30_453V21.ZIP | Provider Role Tool GUI and help file | Binary          |

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

Installation of Provider Role Tool v1.0.453.21 requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Local facility or Information Technology Operations and Services (ITOPS) to give the user the OR PRT ACCESS security key and add the Provider Role Tool item to designated users, such as Clinical Application Coordinators (CACs) or others, Tools menu in CPRS.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before proceeding, ensure that the following patches are installed on your system:

- OR\*3\*42
- OR\*3\*377
- OR\*3\*471

### Install OR\*3.0\*453

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please coordinate with the appropriate personnel to ensure the patch and the executable are installed at the appropriate times and in the correct order.

Installation Instructions:

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter: OR\*3.0\*453.
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes, such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
3.  From the Installation Menu, select the Install Package(s) option and choose the patch to install: OR\*3.0\*453
4.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond NO.
5.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
6.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond NO.
7.  If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

### Provider Role Tool GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the Provider Role Tool GUI executable. Download the ZIP file and extract all the files.

The following methods of installation of Provider Role Tool are available. A site’s choice of which method(s) to use will depend upon IT Operations and Services personnel/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

Network (shared) installation:

This method is typically the simplest to maintain, providing the local and wide area network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (ProviderRoleTool.exe) across the network.

The GUI executable (ProviderRoleTool.exe) and help file (ProviderRoleTool.chm) are copied to a network shared location. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the “Target” field of the shortcut properties.

At the time of a Provider Role Tool version update, the copy of ProviderRoleTool.exe and the help file are replaced, on the network share, with the new version.

Any users requiring access to another site's ProviderRoleTool.exe system can get an alternate shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of ProviderRoleTool.exe (e.g. for testing purposes), a different version of ProviderRoleTool.exe can be placed in a separate network location and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

Citrix installation:

The GUI executables (ProviderRoleTool.exe) and help folder and file (ProviderRoleTool.chm) are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> **NOTE:** For issues with CAG, please contact the local or national help desk.

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

Local workstation installation:

This is the method of installation where the GUI executable (ProviderRoleTool.exe) and file (ProviderRoleTool.chm) are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via SCCM. A National package (Provider Role Tool v1.0.453.21) has been prepared and made available to Regional COR Client Technologies leadership.

Manual install:

This method is used for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.

1.  Locate the OR_30_453.ZIP and unzip the file.

    Copy the contents of the zip archive (the GUI and the help file) to a test directory, for example, C:\ProviderRoleToolTest. A new directory may need to be created.

    Note: Administrator rights are required for the PC used to complete this step.
8.  Create a Shortcut and name it “Test ProviderRoleTool453”

    This shortcut will give the user another visual cue that this is not the normal Provider Role Tool icon.

> <span id="_Toc79770249" class="anchor"></span>Figure 1: Shortcut Icon Provider Role Tool

![](or-3-0-566-provider-role-tool-installation-guide/002.png)

9.  Determine the DNS server name or IP address for the appropriate VistA server.
10. Determine the Broker RPC port for the VistA account.
11. Enter IP (or DNS name) and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

> <span id="_Toc79770250" class="anchor"></span>Figure 2: Test ProviderRoleTool453 Properties

> ![](or-3-0-566-provider-role-tool-installation-guide/003.png)

> **NOTE:** The server and port number shown above are for example only.

# Post-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several things that need to happen after the patch is installed.

## Ensure that the Post Installation Routine Runs to Completion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch starts a Post Installation routine OR3P453 that will run a Background Job to create the EPRACDT New Style cross reference along with the data for this index from the ORDER file (#100). Once it has finished, it will send a MailMan message indicating so to the installing user.

> **NOTE:** Do NOT activate the Provider Role Tool GUI for users until this Background Job has run to a successful completion. Whoever kicked off the OR\*3\*453 installation can get the TaskMan job for this Background Job by looking at the Install File Print for the Install. If the system is experiencing slowness, the post-installation routine can be paused and restarted, but it MUST run to completion before the rest of the installation continues.

> **NOTE:** This Background Job pauses every 100,000 records for 5 minutes so that it will not hit the journal files for the Production system too hard during creation of the new cross-reference. Users who have access to the TaskMan User option can stop the job. This may require someone from the Information Technology (IT) Operations and Services team (ITOPS). ITOPS team members who have programmer access will be able to resume it if it has to be stopped, and check the percentage completed by running the CHECK^OR3P453 Tag.

Below is an example of the post installation routine running. It also shows the user stopping and restarting the routine.

> **NOTE:** The capture below is a basic example from a test account, not a true production installation. As a result, some items may have been altered to remove identifying features or for clarity.

Select OPTION NAME: XPD MAIN       Kernel Installation & Distribution System menu

          Edits and Distribution ...

          Utilities ...

          Installation ...

          Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INstallation

   1      Load a Distribution

   2      Verify Checksums in Transport Global

   3      Print Transport Global

   4      Compare Transport Global to Current System

   5      Backup a Transport Global

   6      Install Package(s)

          Restart Install of Package(s)

          Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME:    OR\*3.0\*453    8/10/18@09:55:46

     =\> OR\*3\*453 TEST v7

This Distribution was loaded on Aug 10, 2018@09:55:46 with header of

   OR\*3\*453 TEST v7

   It consisted of the following Install(s):

     OR\*3.0\*453

Checking Install for Package OR\*3.0\*453

Install Questions for OR\*3.0\*453

Incoming Files:

   100       ORDER  (Partial Definition)

> **NOTE:** You already have the 'ORDER' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   SECURE SHELL

                                   OR\*3.0\*453                                  



     ORD218

     ORD22

     ORD23

     ORD24

     ORD25

     ORD26

     ORD27

     ORD28

     ORD29

 Updating KIDS files...

 OR\*3.0\*453 Installed.

               Aug 10, 2018@09:57:20

 Not a production UCI

 NO Install Message sent



          

  100%                 25             50             75               

Complete  

Install Completed

Start:    08/10/2018 09:57:01

Finish:   08/10/2018 09:57:20

Elapsed:  00:00:19

   1      Load a Distribution

   2      Verify Checksums in Transport Global

   3      Print Transport Global

   4      Compare Transport Global to Current System

   5      Backup a Transport Global

   6      Install Package(s)

          Restart Install of Package(s)

          Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option:

          Edits and Distribution ...

          Utilities ...

          Installation ...

          Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: UTilities

          Build File Print

          Install File Print

          Edit Install Status

          Convert Loaded Package for Redistribution

          Display Patches for a Package

          Purge Build or Install Files

          Rollup Patches into a Build

          Update Routine File

          Verify a Build

          Verify Package Integrity

Select Utilities \<TEST ACCOUNT\> Option: INstall File Print

Select INSTALL NAME:    OR\*3.0\*453    8/10/18@09:57:20

     =\> OR\*3\*453 TEST v7

DEVICE: HOME//   SECURE SHELL

                                             COMPLETED           ELAPSED

-----------------------------------------------------------------------

STATUS: Install Completed                 DATE LOADED: AUG 10, 2018@09:55:46

INSTALLED BY: CPRSINSTALLER,ONE

NATIONAL PACKAGE: ORDER ENTRY/RESULTS REPORTING

INSTALL STARTED: AUG 10, 2018@09:57:19       09:57:20             0:00:01

ROUTINES:                                    09:57:19           

FILES:

ORDER                                        09:57:20             0:00:01

SECURITY KEY                                 09:57:20           

REMOTE PROCEDURE                             09:57:20           

OPTION                                       09:57:20           

POST-INIT CHECK POINTS:

XPD POSTINSTALL STARTED                      09:57:20           

PACKAGE: OR\*3.0\*453     Aug 10, 2018 9:57 am                          PAGE 2

                                             COMPLETED           ELAPSED

-----------------------------------------------------------------------

XPD POSTINSTALL COMPLETED                    09:57:20           

INSTALL QUESTION PROMPT                                               ANSWER

XPO1   Want KIDS to Rebuild Menu Trees Upon Completion of Install     NO

XPI1   Want KIDS to INHIBIT LOGONs during the install                 NO

XPZ1   Want to DISABLE Scheduled Options, Menu Options, and Protocols NO

MESSAGES:

 Install Started for OR\*3.0\*453 :

               Aug 10, 2018@09:57:19

Build Distribution Date: Aug 10, 2018

 Installing Routines:

               Aug 10, 2018@09:57:19

PACKAGE: OR\*3.0\*453     Aug 10, 2018 9:57 am        PAGE 3

                                             COMPLETED           ELAPSED

-----------------------------------------------------------------------

 Installing Data Dictionaries:

               Aug 10, 2018@09:57:20

 Installing PACKAGE COMPONENTS:

 

 Installing SECURITY KEY

 Installing REMOTE PROCEDURE

 Installing OPTION

               Aug 10, 2018@09:57:20

 Running Post-Install Routine: POST^OR3P453

This patch will create a new New Style cross reference

called 'EPRACDT' which will be at the ORDER file level

Type \<Enter\> to continue or '^' to exit:

PACKAGE: OR\*3.0\*453     Aug 10, 2018 9:57 am                          PAGE 4

                                             COMPLETED           ELAPSED

-----------------------------------------------------------------------

but on PROVIDER & DATE/TIME ORDERED sub-fields of the

ORDER ACTIONS Multiple.

Creation of 'EPRACDT' will now go forward in the

Background.

You will be given a TaskMan task \# to check on or,

alternately, you can check your mail on MailMan for a

message expressing Completion of this Task with

appropriate details.

Note Install of this Patch cannot be considered

Complete unless and until this Task is Completed.

Note also that the Status of the 'EPRACDT' Creation

can be checked by requesting IT to run 'D CHECK^OR3P453'

Type \<Enter\> to continue or '^' to exit:

PACKAGE: OR\*3.0\*453     Aug 10, 2018 9:57 am                          PAGE 5

                                             COMPLETED           ELAPSED

-------------------------------------------------------------------------------

at the Command Prompt.

Task \#2086121 queued to start Aug 10, 2018@09:57:20

 Updating Routine file...

 The following Routines were created during this install:

     ORD2

     ORD21

     ORD210

     ORD211

     ORD212

     ORD213

     ORD214

     ORD215

     ORD216

Type \<Enter\> to continue or '^' to exit:

PACKAGE: OR\*3.0\*453     Aug 10, 2018 9:57 am                          PAGE 6

                                             COMPLETED           ELAPSED

-------------------------------------------------------------------------------

     ORD217

     ORD218

     ORD22

     ORD23

     ORD24

     ORD25

     ORD26

     ORD27

     ORD28

     ORD29

 Updating KIDS files...

 OR\*3.0\*453 Installed.

               Aug 10, 2018@09:57:20

Type \<Enter\> to continue or '^' to exit:

PACKAGE: OR\*3.0\*453     Aug 10, 2018 9:57 am                          PAGE 7

                                             COMPLETED           ELAPSED

-------------------------------------------------------------------------------

Not a production UCI

 NO Install Message sent

          Build File Print

          Install File Print

          Edit Install Status

          Convert Loaded Package for Redistribution

          Display Patches for a Package

          Purge Build or Install Files

          Rollup Patches into a Build

          Update Routine File

          Verify a Build

          Verify Package Integrity

Select Utilities \<TEST ACCOUNT\> Option:

          Edits and Distribution ...

          Utilities ...

          Installation ...

          Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option:

Do you really want to halt? YES//

Logged out at Aug 10, 2018 9:57 am

TEST593\>D ^XTER

In response to the DATE prompt you can enter:

     'S' to specify text to be matched in error or routine name

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...Currently, 15% of Records have been Processed.

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...Currently, 16% of Records have been Processed.

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...Currently, 20% of Records have been Processed.

Select OPTION NAME: EVE

     1   EVE       Systems Manager Menu     menu

     2   EVE + VPE       EVE Menu Plus VPE Options     menu

     3   EVENT CAPTURE  ECX ECS MAINTENANCE     Event Capture     menu

     4   EVENT CAPTURE (ECS) EXTRACT AU  ECX ECS SOURCE AUDIT     Event Capture

(ECS) Extract Audit     run routine

     5   EVENT CAPTURE DATA ENTRY  ECENTER     Event Capture Data Entry     menu

Press \<Enter\> to see more, '^' to exit this list,  OR

CHOOSE 1-5: 1  EVE     Systems Manager Menu     menu

          Core Applications ...

          Device Management ...

   FM     VA FileMan ...

          Manage Mailman ...

          Menu Management ...

          Programmer Options ...

          Operations Management ...

          Spool Management ...

          Information Security Officer Menu ...

          Taskman Management ...

          User Management ...

   HL7    HL7 Main Menu ...

          Application Utilities ...

          Capacity Planning ...

Select Systems Manager Menu \<TEST ACCOUNT\> Option: TBOX  User's Toolbox

          Change my Division

          Display User Characteristics

          Edit User Characteristics

          Electronic Signature code Edit

          Menu Templates ...

          Spooler Menu ...

          Switch UCI

          TaskMan User

          User Help

Select User's Toolbox \<TEST ACCOUNT\> Option: TASKMan User

Select TASK: 2086121  Creation of New Style X-Ref 'EPRACDT' in ORDER file

               Taskman User Option

                    Display status.

                    Stop task.

                    Edit task.

                    Print task.

                    List own tasks.

                    Select another task.

               Select Action (Task \# 2086121): STOP  Stop task.

This task has already started running, but it has been asked to stop.

               Taskman User Option

                    Display status.

                    Stop task.

                    Edit task.

                    Print task.

                    List own tasks.

                    Select another task.

               Select Action (Task \# 2086121): DIS  Display status.

2086121: SETXREF^OR3P453, Creation of New Style X-Ref 'EPRACDT' in ORDER file.

         No device.  DEVCUR,DEVCUR.  From Today at 9:57,  By you.

         Completed Today at 9:59.  Job Msg: Received shutdown request

               Taskman User Option

                    Display status.

                    Stop task.

                    Edit task.

                    Print task.

                    List own tasks.

                    Select another task.

               Select Action (Task \# 2086121): ^

          Change my Division

          Display User Characteristics

          Edit User Characteristics

          Electronic Signature code Edit

          Menu Templates ...

          Spooler Menu ...

          Switch UCI

          TaskMan User

          User Help

Select User's Toolbox \<TEST ACCOUNT\> Option:

          Core Applications ...

          Device Management ...

   FM     VA FileMan ...

          Manage Mailman ...

          Menu Management ...

          Programmer Options ...

          Operations Management ...

          Spool Management ...

          Information Security Officer Menu ...

          Taskman Management ...

          User Management ...

   HL7    HL7 Main Menu ...

          Application Utilities ...

          Capacity Planning ...

Select Systems Manager Menu \<TEST ACCOUNT\> Option:

Do you really want to halt? YES//

Logged out at Aug 10, 2018 9:59 am

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...and Stopped Aug 10, 2018@09:59:01.

...Currently, 30% of Records have been Processed.

TEST593\>D POST^OR3P453

This patch will create a new New Style cross reference

called 'EPRACDT' which will be at the ORDER file level

but on PROVIDER & DATE/TIME ORDERED sub-fields of the

ORDER ACTIONS Multiple.

Creation of 'EPRACDT' will now go forward in the

Background.

You will be given a TaskMan task \# to check on or,

alternately, you can check your mail on MailMan for a

message expressing Completion of this Task with

appropriate details.

Note Install of this Patch cannot be considered

Complete unless and until this Task is Completed.

Note also that the Status of the 'EPRACDT' Creation

can be checked by requesting IT to run 'D CHECK^OR3P453'

at the Command Prompt.

Task to Create 'EPRACDT' Already Begun Aug 10, 2018@09:57:20.

...and Stopped Aug 10, 2018@09:59:01.

...Resuming 'EPRACDT' Creation.

Task \#2086125 queued to start Aug 10, 2018@09:59:32   new task \# to resume

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...Currently, 43% of Records have been Processed.

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...Currently, 45% of Records have been Processed.

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...Currently, 48% of Records have been Processed.

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...Currently, 70% of Records have been Processed.

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...Currently, 75% of Records have been Processed.

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...Currently, 90% of Records have been Processed.

TEST593\>D CHECK^OR3P453

Task to Create 'EPRACDT' Begun Aug 10, 2018@09:57:20.

...and Completed Aug 10, 2018@10:04:47.

TEST593\>D ^XM

VA MailMan 8.0 service for REDACTED

You last used MailMan: 08/10/18@09:56

You have 1 new message.

Select MailMan Option: READ/MANAGE MESSAGES 

Select message reader: Classic// Summary Full Screen

Read mail in basket: IN//        (4 messages, 1 new)

IN Basket, 4 messages (1-4), 1 new

\*=New/!=Priority.......Subject........................From.....................

\*4. OR\*3.0\*453 post install has run to completion.   PATCH OR\*3.0\*453

Enter message number or command: 4

Subj: OR\*3.0\*453 post install has run to completion.  \[#474100\] 08/10/18@10:04

5 lines

From: PATCH OR\*3.0\*453  In 'IN' basket.   Page 1  \*New\*

-------------------------------------------------------------------------------

Creation of 'EPRACDT' X-Ref for ORDER file Started Aug 10, 2018@09:57:20.

Creation of 'EPRACDT' X-Ref Completed.

Background Task Finished Aug 10, 2018@10:04:47.

Enter message action (in IN basket): Ignore//

## Assign the OR PRT Access Security Key to Those Identified as Provider Role Tool GUI Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Appropriate personnel must give the OR PRT ACCESS key to those who will use the Provider Role Tool GUI. Your site should have determined which users will be reassigning orders.

## Assign a CPRS Tools Menu Item to Those Identified as Provider Role Tool GUI Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Section 3 - Deployment, sites were directed to identify which users would get the necessary access to perform the order reassignment. If this step has not been completed, it must be done immediately before proceeding with this step.

For the appropriate users to reassign orders, they must be given the security key and the necessary menu item. The users should have already been assigned the security key. If that assignment has not occurred, please assign the key.

PRT needs to be added to the Tools menu. Assuming that the executable exists in the user’s C:\Program Files (x86)\VISTA\Provider Role Tool directory, this is an example of the entry format:

Provider Role Tool=C:\progra~2\VISTA\Provider Role Tool\ProviderRoleTool.exe S=%SRV P=%PORT

After the key has been assigned and the item has been placed on the user’s Tools menu, ensure that CPRS launches correctly and shows the new Provider Role Tool option available in the CPRS Tools menu. The new Provider Role Tool GUI should launch and enable the user to reassign the patient orders of an Ordering Provider who is changing roles (e.g., being transferred from VA to DoD) to one or more VA Providers. Through the Provider Role Tool GUI, the user can either accept the default of one year in the past or can set the date/time so that from that point forward, that Provider will receive alerts/notifications for the orders.

This new Provider Role Tool option should not launch within CPRS if this patch has not yet been installed.  
  
> **NOTE:** If the user does not have the Provider Role Tool key, the user will not be able to execute the Provider Role Tool option on the CPRS Tools menu.

## Configure Exception Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This step should be performed by Clinical Application Coordinator (CAC) or similar personnel at the site.

Three PRT parameters help to give support personnel information if an exception (such as an access violation) occurs. This information can help individuals supporting PRT to troubleshoot any possible exception issues.

- PRT EXCEPTION LOGGER: When this parameter is set to "yes", the application will display a custom access violation screen to the user as well as logging the error stack and allowing it to be sent via an email (if PRT EXCEPTION EMAIL is not blank).
- PRT EXCEPTION EMAIL: When the Exception Logger is enabled (PRT EXCEPTION LOGGER), the user has the ability to pre populate an email through Microsoft Outlook. If this parameter is not empty, the user can email the error log and this email address will be used for the pre population of that email.
- PRT EXCEPTION PURGE: When an error occurs and the Exception Logger is enabled (PRT EXCEPTION LOGGER), any file(s) that are older than the number of days set in this parameter will be removed from the user's machine.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA patch installer can verify installation by looking at Install File Print for OR\*3\*453 to check on the status of the post-install routine (ensuring it has run to completion), as well as ensuring that the installer received a MailMan message that the EPRACDT cross reference creation completed.

Launch the Provider Role Tool GUI and verify the splash screen now announces that version 1.0.453.21 is running. Log into the desired server and verify that a version mismatch message is not received.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a major issue with the patch, the Facility Area Manager may make the decision to back-out the patch. However, this decision should also include Patient Safety, Health Product Support and the CPRS development team.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove the Provider Role Tool features, the site must remove the patch and the way to access it. Step-by-step instructions are given in [Section 6.6 Back-Out Procedure](#back-out-procedure-1).

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on Provider Role Tool v1.0.453.21.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the build of OR\*3.0\*453. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to the CPRS Development team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out the patches would prevent the site’s ability to reassign the orders to different providers, which was a patient safety issue.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility Area Manager has the ultimate responsibility for the decision to back out the Provider Role Tool patch and the associated GUI. The CPRS Development team, patient safety, and Health Product Support Clinical personnel should be consulted before backing out the patches.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for Provider Role Tool v1.0.453.21 is in the event of a catastrophic failure.

1.  Contact the CPRS Development team to notify them there has been a catastrophic failure with Provider Role Tool 1.0.453.21. Use the following contacts:

| Name & Title | Email    | Telephone Number |
|--------------|----------|------------------|
| REDACTED     | REDACTED | REDACTED         |
| REDACTED     | REDACTED | REDACTED         |
| REDACTED     | REDACTED | REDACTED         |
| REDACTED     | REDACTED | REDACTED         |

12. If a decision is made to proceed with back-out and rollback, the CPRS development team will provide the back-out/rollback patch.
13. Remove any records within ORWT TOOLS MENU which contain ProviderRoleTool.exe.
14. Before the back-out/rollback patch gets installed, use FileMan to search for any orders that have a new multiple for ORDER TRANSFERS populated.
15. Install the back-out/rollback patch provided by the CPRS development team.
16. Using the list of Order Numbers from Step 4 above, determine the appropriate dispensation of any alerts that might have been generated.  
    NOTE: You can use the Alert menu to retrieve a list of any alerts created.
17. Remove the Provider Role Tool GUI from any servers or workstations.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once steps have been completed in Section 6.6 above, verify that the Provider Role Tool GUI can no longer be launched from the CPRS Tools menu for the affected users.

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

The Facility Area Manager has the final authority to require the rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will automatically rollback version.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A