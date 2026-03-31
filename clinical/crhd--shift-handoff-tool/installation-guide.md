---
consolidated_title: "install guide"
app_code: CRHD
doc_type: IG
master_source: "CRHD*1*8 Install Guide"
master_pub_date: June 2019
consolidated_from: 2 versions
prior_versions:
  - "CRHD*1*7 Install Guide"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Shift Change Handoff Tool (CRHD\*1.0\*8)

  Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)
---

![](crhd-1-8-install-guide/001.png)

June 2019

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date      | Description     | Author                             |
|-----------|-----------------|------------------------------------|
| June 2019 | Initial Release | <span class="mark">REDACTED</span> |

<span id="_Toc10645962" class="anchor"></span>Table 1: Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

List of Tables

List of Figures

[Figure 1: Shortcut Icon for CRHDv8 [9](#_Toc10645966)](#_Toc10645966)

[Figure 2: CRHDv8 Properties [10](#_Toc10645967)](#_Toc10645967)

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
    - [CRHD\1.0\8 VistA Installation](#crhd108-vista-installation)
    - [Shift Handoff Tool v1.0.8.3 GUI Installation](#shift-handoff-tool-v1083-gui-installation)
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
This document describes how to deploy and install the Shift Handoff Tool v1.0.8.3, and how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed commercial off the shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Shift Handoff Tool v1.0.8.3 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Shift Handoff Tool v1.0.8.3 project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Shift Handoff Tool v1.0.8.3 and the associated MUMPS (M) patch (if applicable) are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. Shift Handoff Tool v1.0.8.3 utilizes existing, nationally released security controls.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No one single entity oversees decision making for deployment, installation, back out and rollback of Shift Handoff Tool v1.0.8.3. The Release Agent and Application Coordinators under the Veterans in Process will approve deployment and install from an OIT perspective. If an issue with the software arises, then the facility Chief Information Officer (CIO) and other site leadership will meet along with input from Patient Safety and Health Product Support to initiate a back out and rollback decision of the software along with the Information Technology (IT) Operations and Services personnel. The following table provides Shift Handoff Tool v1.0.8.3 project information.

<table>
<caption><p><span id="_Toc10645963" class="anchor"></span>Table 2: OI Field Offices</p></caption>
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
<p>The IT support will need to include person(s) to install the Kernel Installation &amp; Distribution System (KIDS) build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</p></td>
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
<td>Facility CIO, IT Operations, and Services personnel</td>
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

<span id="_Toc10645963" class="anchor"></span>Table 2: OI Field Offices

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release, the patch CRHD\*1.0\*8 will be released from the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing and deployment to production will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no timeline specifically for deployment. This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period for the release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Shift Handoff Tool v1.0.8.3 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Shift Handoff Tool v1.0.8.3 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, Shift Handoff Tool v1.0.8.3 (CRHD\*1.0\*8) will be deployed to all VistA systems.

The Production IOC testing sites are:

- <span class="mark">REDACTED</span>

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for Shift Handoff Tool v1.0.8.3. A fully patched VistA system is the only requirement.

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

Service Delivery and Engineering (SDE) Field Implementation Services will send out an Action Item and National Change Order prior to the release of Shift Handoff Tool v1.0.8.3 advising them of the upcoming release.

Shift Handoff Tool v1.0.8.3 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch CRHD\*1.0\*8 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Shift Handoff Tool v1.0.8.3 assumes a fully-patched VistA system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

\[GUI\] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.)

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Shift Handoff Tool v1.0.8.3 is being released as a PackMan Message distributed through the National Patch Module combined with a .ZIP file containing the GUI file(s).

The preferred method is to retrieve files from download.vista.med.va.gov.

This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the <span class="mark">REDACTED</span>directory at the following

| Location                           | Site                               |
|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

<span id="_Toc10645964" class="anchor"></span>Table 3: Files to be Downloaded

Documentation can also be found on the VA Software Documentation Library at:

https://www4.va.gov/vdl/

| File Name        | File Contents                             | Download Format |
|------------------|-------------------------------------------|-----------------|
| CRHD_1_8.ZIP     | Shift Handoff Tool executable & help file | Binary          |
| CRHD_1_8_SRC.ZIP | GUI Source files                          | Binary          |

<span id="_Toc10645965" class="anchor"></span>Table 4: HPS Clinical Sustainment Contacts

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

Installation of Shift Handoff Tool v1.0.8.3 requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CRHD\*1.0\*8 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Select Kernel Installation & Distribution System Option: Installation
1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

    Restart Install of Package(s)

    Unload a Distribution
3.  From this menu, use the \[Backup a Transport Global\] option to create a back out message.
4.  From this menu, the following options may be elected:
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
5.  Use the Install Package(s) options and select the package CRHD\*1.0\*8
6.  If prompted, “Want KIDS to Rebuild Menu Trees Upon Completion of install? NO//” respond NO
7.  When prompted, “Want KIDS to INHIBIT LOGONs during the install? NO//” respond NO.
8.  When prompted, “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//” respond NO.

### Shift Handoff Tool v1.0.8.3 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP files contain the Shift Handoff Tool GUI executable and associated files. Download the ZIP file and extract all the files.

#### Shift Handoff Tool GUI Methods of Installation

The following methods of installation of Shift Handoff Tool are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/Veterans Integrated Services Network (VISN) policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

Network (shared) installation:

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (ShiftHandoffTool.exe) across the LAN.

The GUI executable (ShiftHandoffTool.exe), help file (CRHD.chm) and additional associated files are copied to a network shared location. Users are provided with a desktop shortcut to run ShiftHandoffTool.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the Target field of the shortcut properties

At the time of a Shift Handoff Tool version update the copy of ShiftHandoffTool.exe, the help file and additional associated files are replaced, on the network share, with the new version.

Any users requiring access to another site's Shift Handoff Tool system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of Shift Handoff Tool (e.g. for testing purposes) a different version of ShiftHandoffTool.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

Citrix installation:

The GUI executable (ShiftHandoffTool.exe) and associated files are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut and the necessary CAG infrastructure.

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

> **NOTE:** For issues with CAG, please contact the local or national help desk.

Local workstation installation:

This is the method of installation where the GUI executable (ShiftHandoffTool.exe) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via SCCM. This is outside the scope of the Sustainment team. A National package (Shift Handoff Tool v1.0.8.3) has been prepared and made available to Regional COR Client Technologies leadership.

Manual install:

This method is used for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or needs to have access to a pre-production (mirror) VistA instance.

1.  Locate the CRHD_1_8.ZIP and unzip the file.
2.  Copy the contents of the zip archive to a directory, for example, C:\CRHDGUI. A new directory may need to be created.

    Note: To complete these steps, administrator rights are required on the PC that is used when preforming this task.
3.  Create a Shortcut and name it, CRHDv8.

<span id="_Toc10645966" class="anchor"></span>Figure 1: Shortcut Icon for CRHDv8

> ![](crhd-1-8-install-guide/002.png)

4.  Determine the Domain Name System (DNS) server name or Internet Protocol (IP) address for the appropriate VistA server.
5.  Determine the Broker RPC port for the VistA account.
6.  Enter the IP address or DNS name and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

<span id="_Toc10645967" class="anchor"></span>Figure 2: CRHDv8 Properties

> ![](crhd-1-8-install-guide/003.png)

> Note: The server and port number shown above are for example only.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VISTA\] Verify the checksums for routines CRHD8PST and CRHD6 are equal to the checksums listed on the patch description.

\[GUI\] Launch the Shift Handoff Tool GUI and verify the splash screen announces version v1.0.8.3 is running.

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

\[VistA\] In section 4.8.1 (step 3) the individual installing the patch used option \[Backup a Transport Global\] to create a PackMan message that will revert the Shift Handoff Tool components to their pre-v1.0.8.3 state. This includes everything transported in the CRHD\*1.0\*8 (Shift Handoff Tool v1.0.8.3) build. If for any reason that PackMan Message cannot be located, Contact HPS Sustainment: Clinical (see section 5.6)

\[GUI\] To revert to the Shift Handoff Tool GUI, the 1.0.7.1 GUI would have to be redistributed

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on Shift Handoff Tool v1.0.8.3. This was a maintenance release to correct defects discovered in Shift Handoff Tool v1.0.7.1. There was no additional functionality included.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the two test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of CRHD\*1.0\*8. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to the HPS Clinical Sustainment team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out Shift Handoff Tool v1.0.8.3 would result in the re-instatement of the issues addressed from Shift Handoff Tool v1.0.7.1.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for Shift Handoff Tool v1.0.8.3 is in the event of a catastrophic failure.

Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with Shift Handoff Tool v1.0.8.3. Use the following contacts:

| Name & Title                       | Title                              | Email                              | Telephone Number                   |
|------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

Shows the contact information for key personell from HPS

1.  If the decision is made to proceed with a back-out and rollback, the HPS Sustainment Clinical team is available to assist sites that have misplaced their backup PackMan message and provide the instructions on downloading the executable.
9.  \[VistA\]
1.  Open the Backup MailMan Message
2.  At the, “Enter message action (in IN basket): Ignore//” prompt enter X for \[Xtract PackMan\]
3.  At the, “Select PackMan function:” prompt select \[INSTALL/CHECK MESSAGE\]. The old routine is now restored
4.  \[GUI\] Coordinate with the appropriate IT support, local and regional, to schedule the time to install CRHD\*1.0\*7 and to push out / install the previous GUI executable.
10. Once CRHD\*1.0\*7 and Shift Handoff Tool v1.0.7.1 have been installed, verify operations before making available to all staff.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure that the v1.0.7.1 executable launches properly.
11. Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

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

The Facility CIO has the final authority to require the rollback and accept the associated risks

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will automatically rollback version.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: CRHD*1*7 Install Guide

### CRHD\*1.0\*7 VistA Installation

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
5.  Use the Install Package(s) options and select the package CRHD\*1.0\*7
6.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install?” respond NO. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
7.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.
