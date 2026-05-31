---
title: MD*1*85 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: MD
app_name: Clinical Procedures
section: CLI
app_status: active
pkg_ns: MD
patch_ver: 1
patch_id: MD*1*85
group_key: MD:MD:1
file_numbers: []
security_keys: []
menu_options: 0
description: This document describes how to deploy and install the CP User v1.0.85.2, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed commercial-off-the-s
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 3791
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: February 2024
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/ClinProc/MD-1-85-DIBR.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/ClinProc/MD-1-85-DIBR.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=139
audit_applied: '2026-05-31'
master_source: MD*1*85 Deployment, Installation, Back-Out, and Rollback Guide
master_pub_date: February 2024
consolidated_from: 5 versions
prior_versions:
- MD*1*86 Deployment, Installation, Back-Out, and Rollback Guide
- MD*1*87 Deployment, Installation, Back-Out, and Rollback Guide
- MD*1*93 Deployment, Installation, Back-Out, and Rollback Guide
- MD*1*95 Deployment, Installation, Back-Out, and Rollback Guide
consolidated_title: deployment, installation, back-out, and rollback guide
---

## Table of Contents

  - [Introduction](#introduction)
    - [Purpose](#purpose)
    - [Dependencies](#dependencies)
    - [Constraints](#constraints)
  - [Roles and Responsibilities](#roles-and-responsibilities)
  - [Deployment](#deployment)
    - [Timeline](#timeline)
    - [Site Readiness Assessment](#site-readiness-assessment)
    - [Resources](#resources)
  - [Installation](#installation)
    - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
    - [Platform Installation and Preparation](#platform-installation-and-preparation)
    - [Download and Extract Files](#download-and-extract-files)
    - [Database Creation](#database-creation)
    - [Installation Scripts](#installation-scripts)
    - [Cron Scripts](#cron-scripts)
    - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
    - [Installation Procedure](#installation-procedure)
    - [Installation Verification Procedure](#installation-verification-procedure)
    - [System Configuration](#system-configuration)
    - [Database Tuning](#database-tuning)
  - [Back-Out Procedure](#back-out-procedure)
    - [Back-Out Strategy](#back-out-strategy)
    - [Back-Out Considerations](#back-out-considerations)
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
---
title: |
  <span id="_Toc205632711" class="anchor"></span>Clinical Procedures (CP)
  <span id="_Hlk174352757" class="anchor"></span>CP User (MD\*1.0\*85)
  <span id="_Hlk174352758" class="anchor"></span>Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)
---
![](md-1-85-deployment-installation-back-out-and-rollback-guide/001.png)
February 2024
Department of Veterans Affairs (VA)
Office of Information and Technology (OIT)
Revision History
| Date    | Version | Description                | Author                        |
|---------|---------|----------------------------|-------------------------------|
| 2/2024  | 1.2     | Updated for MD\*1.0\*85 V2 | HPS Clinical Sustainment Team |
| 11/2023 | 1.1     | Updated for MD\*1.0\*85    | HPS Clinical Sustainment Team |
| 9/2018  | 1.0     | Initial Release            | HPS Clinical Sustainment Team |
<span id="_Toc20903972" class="anchor"></span>Table 1: Roles and Responsibilities
Artifact Rationale
This document describes the Deployment, Installation, Back-out, and Rollback Guide for new products going into the VA Enterprise. The guide includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect these procedures at a single or at multiple locations.
Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Guide is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.
Table of Contents
List of Tables
List of Figures
[Figure 1: Shortcut Icon for Test CPUser v85 [9](#_Toc174352414)](#_Toc174352414)
[Figure 2: Test CPUser v85 Properties [10](#_Toc174352415)](#_Toc174352415)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install the CP User v1.0.85.2, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed commercial-off-the-shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CP User v1.0.85.2 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

### Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP User v1.0.85.2 project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system.

### Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP User v1.0.85.2 and the associated MUMPS patch (if applicable) are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. CP User v1.0.85.2 utilizes existing, nationally released security controls to control access.

## Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No one single entity oversees decision making for deployment, installation, back out and rollback of CP User v1.0.85.2. The Release Agent and Application Coordinators under the VIP will approve deployment and install from an OIT perspective. If an issue with the software arises, then the facility's Chief Information Officer (CIO) and other site leadership will meet along with input from Patient Safety, Health Product Support (HPS), Information Technology (IT) Operations, and Services personnel, to initiate a back out and rollback decision of the software. The following table provides CP User v1.0.85.2 project information.

<table>
<caption><p><span id="_Toc20903974" class="anchor"></span>Table 2: Files to be Downloaded</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 15%" />
<col style="width: 34%" />
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
<p>The IT support will need to include person(s) to install the Kernel Installation &amp; Distribution System (KIDS) build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix Access Gateway (CAG)</p></td>
<td>Deployment</td>
<td>Execute deployment</td>
</tr>
<tr class="odd">
<td><p>IT Operations and Services personnel.</p>
<p>The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the CAG</p></td>
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

<span id="_Toc20903974" class="anchor"></span>Table 2: Files to be Downloaded

## Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release, the patch MD\*1.0\*85 will be released from the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing and deployment to production will be at the site's discretion. It is anticipated there will be a 30-day compliance period.

### Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific timeline for deployment. This is considered a maintenance release and installation will be at the site's discretion, within the constraints of the compliance period.

### Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CP User v1.0.85.2 deployment.

#### Deployment Topology (Targeted Architecture)

CP User Documentation v1.0.85.2 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the CAG.

#### Site Information (Locations, Deployment Recipients) 

The initial deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, CP User v1.0.85.2 (MD\*1.0\*85) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

- Manchester VA Medical Center (Manchester, NH)
- Minneapolis VA Health Care System (Minneapolis, MN)

#### Site Preparation 

There is no special preparation required for CP User v1.0.85.2. A fully patched VistA system is the only requirement.

### Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

#### Facility Specifics

N/A

#### Hardware 

N/A

#### Software 

N/A

#### Communications 

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action item and National Change Order prior to the release of CP User v1.0.85.2 advising them of the upcoming release.

CP User v1.0.85.2 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch MD\*1.0\*85 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP User v1.0.85.2 assumes a fully-patched VistA system.

### Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users should be off the system.

\[GUI\] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.)

### Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP User v1.0.85.2 is being released as a PackMan Message distributed through the National Patch Module combined with a .ZIP file containing the GUI file(s).

Files can be obtained from the SOFTWARE directory:

<https://download.vista.med.va.gov/index.html/SOFTWARE/>

Documentation can also be found on the VA Software Documentation Library at:

<https://www.va.gov/vdl/application.asp?appid=139>

| File Name       | File Contents                              | Download Format |
|-----------------|--------------------------------------------|-----------------|
| MD_1_85.ZIP     | CP User v1.0.85.2 executable and help file | Binary          |
| MD_1_85_SRC.ZIP | CP User Source control files               | Binary          |

<span id="_Toc174352409" class="anchor"></span>Table 3: HPS Clinical Sustainment Contacts

### Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of CP User v1.0.85.2 requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MD\*1.0\*85 VistA Installation

1.  Choose the PackMan message containing this patch and select the INSTALL/CHECK MESSAGE PackMan option to load the KIDS patch into a Transport Global on your system.
2.  From the Kernel Installation & Distribution System Menu (KIDS), select the Installation menu:

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, you must use the Backup a Transport Global option to create a back out message. When prompted for the INSTALL NAME enter the package name: MD\*1.0\*85
4.  Also from this menu, you may elect to use the following options:
    - Verify Checksums in Transport Global
    - Print Transport Global
    - Compare Transport Global to Current System
5.  Select the Install Package(s) option and enter the package name: MD\*1.0\*85
6.  When prompted, Want KIDS to INHIBIT LOGONs during the install? NO//, respond NO.
7.  When prompted, Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//, respond NO.

#### CP User v1.0.85.2 GUI Installation

The ZIP file contains the CP User GUI executable and help file. Download the ZIP file and extract all the files.

#### CP User documentation GUI Methods of Installation

The following methods of installation of CP User are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/Veterans Integrated Services Network (VISN) policies, Local Area Network (LAN) performance, or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

<u>Network (shared) installation:</u>

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPUser.exe) across the LAN.

The GUI executable (CPUser.exe), help file (CPUSER.chm) files are copied to a network shared location. Users are provided with a desktop shortcut to run CPUser.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the Target field of the shortcut properties.

At the time of a CP User version update the copy of CPUser.exe and the help file are replaced, on the network share, with the new version.

Any users requiring access to another site's CP User system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of CP User (e.g. for testing purposes) a different version of CPUser.exe can be placed in a separate network location and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

<u>Citrix installation:</u>

The GUI executable (CPUser.exe) and associated files are installed and run from a remote workstation, and the user views the remote workstation's screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary CAG infrastructure).

> **NOTE:** For issues with CAG, please contact your local or national help desk.

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

<u>Local workstation installation:</u>

This is the "standard" method of installation where the GUI executable (CPUser.exe) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via System Center Configuration Manager (SCCM). This is outside the scope of the Sustainment team. A National package (CP User v1.0.85.2) has been prepared and made available to Regional Contracting Officer's Representative (COR) Client Technologies leadership.

<u>Manual install:</u>

This method is available for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.

1.  Locate the MD_1_85.ZIP and unzip the file.
2.  Copy the contents of the zip archive to a test directory, for example, C:\CPUser. You may need to create this new directory.

    Note: You need to have a user with Administrator rights to the personal computer (PC) to complete these steps.
3.  Create a Shortcut and name it, Test CP User v1_85. This is to give the user another visual cue that this is not the normal CP User icon.

> <span id="_Toc174352414" class="anchor"></span>Figure 1: Shortcut Icon for Test CPUser v85

![](md-1-85-deployment-installation-back-out-and-rollback-guide/002.png)

4.  Determine the Domain Name System (DNS) server name or Internet Protocol (IP) address for the appropriate VistA server.
5.  Determine the Broker RPC port for the VistA account.
6.  Enter IP (or DNS name) and RPC port in the Target field of the Shortcut properties or use ServerList.exe (which launches a selection screen for various servers and ports defined).
7.  CP User has been updated to accept a parameter "showcerts" in the desktop shortcut for the application. When this parameter is present, the application with display a prompt allowing users to select the correct certificate and then they will be prompted for their PIV card PIN.

> <span id="_Toc174352415" class="anchor"></span>Figure 2: Test CPUser v85 Properties

![](md-1-85-deployment-installation-back-out-and-rollback-guide/003.png)

> **NOTE:** The server and port number shown above are for example only.

### Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VISTA\] Verify the checksum of routine MDPOST85 is equal to the checksum listed in the patch description.

\[GUI\] Launch the CP User GUI and verify the splash screen now announces that you are running Version: 1.0 and Patch: MD\*1.0\*85.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] In Section 0 (step 3) the individual installing the patch used option \[Backup a Transport Global\] to create a PackMan message that will revert the CP User components to their pre-v1.0.85.2 state. This includes everything transported in the MD\*1.0\*84 (CP User v1.0.84.1) build. If for any reason that PackMan Message cannot be located, contact HPS Sustainment: Clinical (see Section 5.6).

\[GUI\] To revert the CP User GUI, the v1.0.84.1 GUI will have to be redistributed.

### Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### User Acceptance Testing

User acceptance testing was conducted by the test sites listed in Section 0.

The sites followed the provided test plan and executed the test cases according to the plan for the MD\*1.0\*85 build. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to the HPS Clinical Sustainment team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

### Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will only be considered if there is a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.

### Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out CP User v1.0.85.2 would result in the re-instatement of the issues addressed in CP User v1.0.84.1.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

### Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

### Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for CP User v1.0.85.2 is in the event of a catastrophic failure.

Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with CP User v1.0.85.2. Use the following contacts:

<table>
<caption>The HPS Clinical Sustainment Contacts table organizes contact information using the Name &amp; Title, Email, and Telephone Number columns.</caption>
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
<td><p><mark>REDACTED</mark></p>
<p>Project Manager</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p><mark>REDACTED</mark></p>
<p>Technical Leader</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

The HPS Clinical Sustainment Contacts table organizes contact information using the Name & Title, Email, and Telephone Number columns.

1.  If the decision is made to proceed with back-out and rollback, the HPS Sustainment Clinical team will be available to assist sites that have misplaced their backup PackMan message, as well as give you the instructions for downloading the executable.
8.  \[VistA\]
1.  Open the Backup MailMan Message.
2.  At the Enter message action (in IN basket): Ignore// prompt, enter X for \[Xtract PackMan\].
3.  At the Select PackMan function: prompt, select \[INSTALL/CHECK MESSAGE\]. The old routine is now restored.
9.  \[GUI\] Coordinate with the appropriate IT support, local and regional, to schedule the time to install MD\*1.0\*84 and to push out/install the previous GUI executable.
10. Once MD\*1.0\*84 and CP User v1.0.84.1 have been installed, verify operations before making available to all staff.

### Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure the CP User v1.0.84.1 executable launches properly.
2.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on CP User v1.0.85.2. This was a maintenance release to correct defects discovered in CP User v1.0.84.1. There was no additional functionality included.

### Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to Section 5.3 for criteria that would require a rollback of this patch.

### Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out CP User v1.0.85.2 would result in the re-instatement of the issues addressed in CP User v1.0.84.1.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

### Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks.

### Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Included in the VistA patch, there is a post-install routine, MDPOST85. This routine contains a rollback section called ROLLBACK. If for some reason it is deemed necessary to back out this patch, simply executing that section of the routine, D ROLLBACK^MDPOST85 will reset the version information needed for the previous release of CP User, which is MD\*1.0\*84.

### Rollback Verification Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ensure the CP User v1.0.84.1 executable launches properly.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MD*1*93 Deployment, Installation, Back-Out, and Rollback Guide

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Hemodialysis Documentation v1.0.93.2 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the CAG.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, CP Hemodialysis v1.0.93.2 (MD\*1.0\*93) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

- Palo Alto HCS (Palo Alto, CA)
- Southern Nevada HCS (Las Vegas, NV)

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for CP Hemodialysis v1.0.93.2. A fully patched VistA system is the only requirement.

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

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action item and National Change Order prior to the release of CP Hemodialysis v1.0.93.2 advising them of the upcoming release.

CP Hemodialysis v1.0.93.2 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch MD\*1.0\*93 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

### MD\*1.0\*93 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and select the INSTALL/CHECK MESSAGE PackMan option to load the KIDS patch into a Transport Global on your system.
2.  From the Kernel Installation & Distribution System Menu (KIDS), select the Installation menu:

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, you must use the Backup a Transport Global option to create a back out message. When prompted for the INSTALL NAME enter the package name: MD\*1.0\*93
4.  Also from this menu, you may elect to use the following options:
    - Verify Checksums in Transport Global
    - Print Transport Global
    - Compare Transport Global to Current System
5.  Select the Install Package(s) option and enter the package name: MD\*1.0\*93
6.  When prompted, Want KIDS to INHIBIT LOGONs during the install? NO//, respond NO.
7.  When prompted, Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//, respond NO.

### CP Hemodialysis v1.0.93.2 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the CP Hemodialysis GUI executable. Download the ZIP file and extract the file.

#### CP Hemodialysis documentation GUI Methods of Installation

The following methods of installation of CP Hemodialysis are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/Veterans Integrated Services Network (VISN) policies, Local Area Network (LAN) performance, or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

- Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (Hemodialysis.exe) across the LAN.

> The GUI executable (Hemodialysis.exe) file is copied to a network shared location. Users are provided with a desktop shortcut to run Hemodialysis.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the Target field of the shortcut properties.

> At the time of a CP Hemodialysis version update the copy of Hemodialysis.exe is replaced, on the network share, with the new version.

> Any users requiring access to another site's CP Hemodialysis system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of CP Hemodialysis (e.g. for testing purposes) a different version of Hemodialysis.exe can be placed in a separate network location and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

- Citrix installation:

> The GUI executable (Hemodialysis.exe) and associated files are installed and run from a remote workstation, and the user views the remote workstation's screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary CAG infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

- Local workstation installation:

  This is the "standard" method of installation where the GUI executable (Hemodialysis.exe) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via System Center Configuration Manager (SCCM). This is outside the scope of the Sustainment team. A National package (CP Hemodialysis v1.0.93.2) has been prepared and made available to Regional Contracting Officer's Representative (COR) Client Technologies leadership.
- Manual install:

  This method is available for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.
1.  Locate the MD_1_93.ZIP and unzip the file.
2.  Copy the contents of the zip archive to a test directory, for example, C:\CPHemodialysis. You may need to create this new directory.

    Note: You need to have a user with Administrator rights to the personal computer (PC) to complete these steps.
3.  Create a Shortcut and name it, Test CP Hemodialysis v1_93. This is to give the user another visual cue that this is not the normal CP Hemodialysis icon.

> <span id="_Toc181092935" class="anchor"></span>Figure 1: Shortcut Icon for Test Hemodialysis v93

![](md-1-93-deployment-installation-back-out-and-rollback-guide/002.png)

4.  Determine the Domain Name System (DNS) server name or Internet Protocol (IP) address for the appropriate VistA server.
5.  Determine the Broker RPC port for the VistA account.
6.  Enter IP (or DNS name) and RPC port in the Target field of the Shortcut properties or use ServerList.exe (which launches a selection screen for various servers and ports defined).

> <span id="_Toc181092936" class="anchor"></span>Figure 2: Test CP Hemodialysis v93 Properties

> ![](md-1-93-deployment-installation-back-out-and-rollback-guide/003.png)

> **NOTE:** The server and port number shown above are for example only.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the test sites listed in Section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the MD\*1.0\*93 build. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to the HPS Clinical Sustainment team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

### From: MD*1*95 Deployment, Installation, Back-Out, and Rollback Guide

### MD\*1.0\*95 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and select the INSTALL/CHECK MESSAGE PackMan option to load the KIDS patch into a Transport Global on your system.
2.  From the Kernel Installation & Distribution System Menu (KIDS), select the Installation menu:

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, you must use the Backup a Transport Global option to create a back out message. When prompted for the INSTALL NAME enter the package name: MD\*1.0\*95
4.  Also from this menu, you may elect to use the following options:
    - Verify Checksums in Transport Global
    - Print Transport Global
    - Compare Transport Global to Current System
5.  Select the Install Package(s) option and enter the package name: MD\*1.0\*95
6.  When prompted, Want KIDS to INHIBIT LOGONs during the install? NO//, respond NO.
7.  When prompted, Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//, respond NO.

### CP Gateway v1.0.95.1 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the CP Gateway GUI executable. Download the ZIP file and extract the file.

#### CP Gateway documentation GUI Methods of Installation

The following methods of installation of CP Gateway are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/Veterans Integrated Services Network (VISN) policies, Local Area Network (LAN) performance, or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

- Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPGateway.exe) across the LAN.

> The GUI executable (CPGateway.exe) file is copied to a network shared location. Users are provided with a desktop shortcut to run CPGateway.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the Target field of the shortcut properties.

> To enable the use of Windows Certificates as part of the authentication procedure on launch of the application, add /showcerts as a parameter to the executable in the Target field. (cpgateway.exe /showcerts)

> To disable the purge process for the duration of the application's running session, add /nopurge as a parameter to the executable in the Target field. (cpgateway.exe /nopurge).

> The two new parameters, /showcerts and /nopurge can be used in any combination. Their behaviors are independent of each other.

> At the time of a CP Gateway version update the copy of CPGateway.exe is replaced, on the network share, with the new version.

> Any users requiring access to another site's CP Gateway system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of CP Gateway (e.g. for testing purposes) a different version of CPGateway.exe can be placed in a separate network location and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

- Citrix installation:

> The GUI executable (CPGateway.exe) and associated files are installed and run from a remote workstation, and the user views the remote workstation's screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary CAG infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

- Local workstation installation:

  This is the "standard" method of installation where the GUI executable (CPGateway.exe) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via System Center Configuration Manager (SCCM). This is outside the scope of the Sustainment team. A National package (CP Gateway v1.0.95.1) has been prepared and made available to Regional Contracting Officer's Representative (COR) Client Technologies leadership.
- Manual install:

  This method is available for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.
1.  Locate the MD_1_95.ZIP and unzip the file.
2.  Copy the contents of the zip archive to a test directory, for example, C:\CPGateway. You may need to create this new directory.

    Note: You need to have a user with Administrator rights to the personal computer (PC) to complete these steps.
3.  Create a Shortcut and name it, Test CP Gateway v1_95. This is to give the user another visual cue that this is not the normal CP Gateway icon.

<span id="_Toc195755647" class="anchor"></span>![](md-1-95-deployment-installation-back-out-and-rollback-guide/002.png)Figure 1: Shortcut Icon for Test CPGateway v95

4.  Determine the Domain Name System (DNS) server name or Internet Protocol (IP) address for the appropriate VistA server.
5.  Determine the Broker RPC port for the VistA account.
6.  Enter IP (or DNS name) and RPC port in the Target field of the Shortcut properties or use ServerList.exe (which launches a selection screen for various servers and ports defined).

<span id="_Toc195755648" class="anchor"></span>![](md-1-95-deployment-installation-back-out-and-rollback-guide/003.png)Figure 2: Test CPGateway v95 Properties

> **NOTE:** The server and port number shown above are for example only.
