---
title: CRHD*1*11 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: CRHD
app_name: Shift Handoff Tool
section: CLI
app_status: active
pkg_ns: CRHD
patch_ver: 1
patch_id: CRHD*1*11
group_key: "CRHD:CRHD:1"
file_numbers: []
security_keys: []
menu_options: 0
description: This document describes how to deploy and install CRHD\1.0\11 Shift Handoff Tool v1.0.11.2, and how to back-out the product and rollback to a previous version or data set.
audience: 
keywords: 
  - table
  - contents
  - installation
  - back
  - tool
  - shift
  - handoff
  - rollback
  - vista
  - crhd
page_count: 0
word_count: 3813
section_count: 7
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/CRHD-1-11-DIBRG.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/CRHD-1-11-DIBRG.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=175"
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
title: <span id="_Toc205632711" class="anchor"></span>Shift Change Handoff Tool
---
CRHD\*1.0\*11
Deployment, Installation, Back-Out, and Rollback Guide
![](crhd-1-11-deployment-installation-back-out-and-rollback-guide/001.png)
August 2024Version 1.0
Department of Veterans Affairs (VA)
Office of Information and Technology (OIT)
Revision History
<table>
<caption><p><span id="_Toc174532170" class="anchor"></span>Table 1: Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 47%" />
<col style="width: 33%" />
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
<td>August 2024</td>
<td><p>Updated for Patch CRHD*1.0*11</p>
<p>Shift Handoff Tool v1.0.11.2</p></td>
<td>Liberty</td>
</tr>
</tbody>
</table>
<span id="_Toc174532170" class="anchor"></span>Table 1: Roles and Responsibilities
Table of Contents
> [3.2.1 Deployment Topology (Targeted Architecture) [4](#deployment-topology-targeted-architecture)](#deployment-topology-targeted-architecture)
> [3.2.2 Site Information (Locations, Deployment Recipients) [4](#site-information-locations-deployment-recipients)](#site-information-locations-deployment-recipients)
> [3.2.3 Site Preparation [4](#site-preparation)](#site-preparation)
[3.3 Resources [4](#resources)](#resources)
> [3.3.1 Facility Specifics [5](#facility-specifics)](#facility-specifics)
> [3.3.2 Hardware [5](#hardware)](#hardware)
> [3.3.3 Software [5](#software)](#software)
> [3.3.4 Communications [5](#communications)](#communications)
> [3.3.5 Deployment/Installation/Back-Out Checklist [5](#deploymentinstallationback-out-checklist)](#deploymentinstallationback-out-checklist)
> [4.8.1 CRHD\*1.0\*11 VistA Installation [7](#crhd1.011-vista-installation)](#crhd1.011-vista-installation)
> [4.8.2 Shift Handoff Tool v1.0.11.2 GUI Installation [8](#shift-handoff-tool-v1.0.11.2-gui-installation)](#shift-handoff-tool-v1.0.11.2-gui-installation)
5.5 Authority for Back-Out [13](#authority-for-back-out)
5.6 Back-Out Procedure [13](#back-out-procedure-1)
List of Tables
[Table 1: Roles and Responsibilities [2](#_Toc174532170)](#_Toc174532170)
[Table 3: Files to be Downloaded [6](#_Toc174532171)](#_Toc174532171)
List of Figures
[Figure 1: Shortcut Icon for V11-ShifthandoffTool [10](#_Toc174532172)](#_Toc174532172)
[Figure 2: CRHDv11 Properties [11](#_Toc174532173)](#_Toc174532173)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install CRHD\*1.0\*11 Shift Handoff Tool v1.0.11.2, and how to back-out the product and rollback to a previous version or data set.

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CRHD\*1.0\*11 Shift Handoff Tool v1.0.11.2 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

### Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CRHD\*1.0\*11 Shift Handoff Tool v1.0.11.2 project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system. CRHD\*1.0\*10 Shift Handoff Tool v1.0.10.2 is the previous edition that should be used in case a rollback is needed.

### Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CRHD\*1.0\*11 Shift Handoff Tool v1.0.11.2 and the associated MUMPS (M) patch are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. CRHD\*1.0\*11 Shift Handoff Tool v1.0.11.2 utilizes existing, nationally released security controls.

## Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc174532171" class="anchor"></span>Table 2: Files to be Downloaded</p></caption>
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
<td>Department of Veterans Affairs (VA) Office of Information and Technology (OIT), Health Services Portfolio (HSP) Patient Care Services (PCS), and Program Management Office (PMO)</td>
<td>Deployment</td>
<td>Plan and schedule deployment</td>
</tr>
<tr class="even">
<td>Health Product Support and Field Operations (FO)</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
</tr>
<tr class="odd">
<td>Field Testing (Initial Operating Capability-IOC) and Health Services/ Patient Care Services</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="even">
<td><p>OIT, Development, Security, and Operations (DevSecOps) Infrastructure Operations (IO).</p>
<p>The IT support will need to include person(s) to install the Kernel Installation &amp; Distribution System (KIDS) build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</p></td>
<td>Deployment</td>
<td>Execute deployment</td>
</tr>
<tr class="odd">
<td><p>OIT, DevSecOps</p>
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
<td>Facility Area Manager, and DevSecOps</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
</tr>
<tr class="even">
<td><p>Hardware and System support – no changes.</p>
<p>Software issues support will be provided by local IT first and if needed a ServiceNow ticket will be entered to escalate support.</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
</tr>
</tbody>
</table>

<span id="_Toc174532171" class="anchor"></span>Table 2: Files to be Downloaded

## Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module (NPM) patch rollout. Once approval has been given to nationally release, the patch CRHD\*1.0\*11 will be released from the NPM. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing and deployment to production will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

### Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The duration of deployment and installation is 30 days (requested). This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period for the release.

### Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Shift Handoff Tool patch CRHD\*1.0\*11 and ShiftHandoffTool.exe v1.0.11.2 deployment.

#### Deployment Topology (Targeted Architecture)

The release will be deployed to all VistA instances.

#### Site Information (Locations, Deployment Recipients) 

The initial deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, Shift Handoff Tool v1.0.11.2 (CRHD\*1.0\*11) will be deployed to all VistA systems.

The Production IOC testing sites are:

- Durham VA Medical Center (Durham, NC)
- Central California VA Health Care System (Fresno, CA)

#### Site Preparation 

There is no special preparation required for Shift Handoff Tool v1.0.11.2. A fully patched VistA system is the only requirement.

### Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Resources involved in the release of the VistA MUMPS patch CRHD\*1.0\*11 are the assigned Application Coordinators and the project VistA development Liberty Team. The team will work with the test sites VistA Applications and OI&T, DevSecOps to install and verify patches.

#### Facility Specifics

N/A

#### Hardware 

N/A

#### Software 

The following table describes software specifications required at each site prior to deployment.

| Required Software                                          | Version   |
|----------------------------------------------------------------|---------------|
| Prerequisite patch for CRHD\*1.0\*11 and ShiftHandoff Tool GUI | CRHD\*1.0\*10 |

#### Communications 

Service Delivery and Engineering (SDE) Field Implementation Services will send out an Action Item and National Change Order prior to the release of Shift Handoff Tool v1.0.11.2 GUI and CRHD\*1.0\*11 advising them of the upcoming release.

Shift Handoff Tool v1.0.11.2 will be deployed using the standard method of patch release from the NPM rather than a phased deployment. When patch CRHD\*1.0\*11 is released, the NPM will send a notification to all personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released. Patches are tracked nationally for all VAMCs in the NPM in FORUM. FORUM automatically tracks the patches as they are installed at VAMC production systems. One can run a report in FORUM to identify when and by whom the patch was installed into the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch into their VistA production system. Therefore, this information does not need to be manually tracked.

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Shift Handoff Tool v1.0.11.2 GUI and CRHD\*1.0\*11 is installable on a VistA system with the prerequisite patches installed.

### Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

\[GUI\] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.)

### Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Shift Handoff Tool v1.0.11.2 GUI and CRHD\*1.0\*11 is being released as a PackMan Message distributed through the NPM combined with an associated .ZIP file containing the GUI file(s).

Files can be obtained from the SOFTWARE directory:

<https://download.vista.med.va.gov/index.html/SOFTWARE/>

Documentation (not the .ZIP) can also be found on the VA Software Documentation Library at: <https://www.va.gov/vdl/>

| File Description                                               | File Name                   | Download Format  |
|----------------------------------------------------------------|-----------------------------|------------------|
| Deployment, Installation, Back-Out, and Rollback Guide (DIBRG) | CRHD_1_11_DIBRG.pdf         | Binary           |
| ShiftHandoffTool executable & help file                        | CRHD_1_11.ZIP               | Binary           |
| CRHD_1_11_SRC.ZIP                                              | GUI Source files (Optional) | Binary           |
|                                                                |                             |                  |
| Zip File Name                                              | Zip Contents            | Bytes (size) |
| ShiftHandoffTool.exe                                           | ShiftHandoffTool.Executable | 8,273 kb         |
| CRHD.chm                                                       | ShiftHandoffTool Help File  | 146 kb           |

Provides a list of the files, it’s content, and the download format that will be needed for this patch.

### Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database creation is not applicable for this VistA patch.

### Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of Shift Handoff Tool v1.0.11.2 requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual workstation installs – access/ability to push executable to required workstations.

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### CRHD\*1.0\*11 VistA Installation

> 1\. Choose the PackMan message containing this patch.

> 2\. Choose the INSTALL/CHECK MESSAGE PackMan option to load the KIDS patch into a Transport Global on your system.

> 3\. From the Kernel Installation & Distribution System Menu (KIDS), select the Installation Menu.

> 4\. From the Installation Menu:

1.  At the Installation option menu, select Backup a Transport Global.
2.  At the Select INSTALL NAME prompt, enter your build CRHD\*1.0\*11.
3.  When prompted for the following, enter "R" for Routines or "B" for Build.

Select one of the following:

B Build

R Routines

Enter response: Build

4.  When prompted "Do you wish to secure your build? NO//", press \<enter\> and take the default response of "NO".
5.  When prompted with, "Send mail to: Last name, First Name", press \<enter\> to take default recipient. Add any additional recipients.
6.  When prompted with "Select basket to send to: IN//", press \<enter\> and take the default IN mailbox or select a different mailbox., select the Backup a Transport Global.

> 5\. From the Installation Menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the patch CRHD\*1.0\*11.

1.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
2.  Print Transport Global - This option will allow you to print only a summary of the patch, to print a summary of the patch and the routines in the transport global, or to print only the routines in the transport global.
3.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. (It compares all components of this patch's routines, DDs, templates, etc.).

> 6\. From the Installation Menu, select the Install Package(s) option and enter the patch CRHD\*1.0\*11.

> 7\. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond 'NO'.

> 8\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond 'NO'.

#### Shift Handoff Tool v1.0.11.2 GUI Installation

CRHD\*1.0\*11 ZIP files contain the GUI executable (Shift Handoff Tool.exe) and help file (CRHD.chm). Download the ZIP file and extract all the files.

#### Shift Handoff Tool GUI Methods of Installation

The following methods of installation of Shift Handoff Tool are available. Sites choose which method(s) to use and it will depend upon DevSecOps/Veterans Integrated Services Network (VISN) policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

Network (shared) installation:

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (ShiftHandoffTool.exe) across the LAN.

The GUI executable (ShiftHandoffTool.exe), help file (CRHD.chm) and additional associated files are copied to a network shared location. Users are provided with a desktop shortcut to run ShiftHandoffTool.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the Target field of the shortcut properties.

At the time of a Shift Handoff Tool version, replace the copy of ShiftHandoffTool.exe, the help file and additional associated files on the network share, with the new version.

Any users requiring access to another site's Shift Handoff Tool system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of Shift Handoff Tool (e.g., for testing purposes) a different version of ShiftHandoffTool.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

Citrix installation:

The GUI executable (ShiftHandoffTool.exe) and associated files are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut and the necessary CAG infrastructure.

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

> **NOTE:** For issues with CAG, please contact the local or national help desk.

Local workstation installation:

This is the method of installation where the GUI executable (ShiftHandoffTool.exe) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via SCCM. This is outside the scope of the Sustainment team. A National package (Shift Handoff Tool v1.0.11) has been prepared and made available to Regional COR Client Technologies leadership.

Manual install:

This method is used for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or needs to have access to a pre-production (mirror) VistA instance.

1.  Locate the CRHD_1_11.ZIP and unzip the file.
2.  Copy the contents of the zip archive to a directory, for example, “C:\Program Files (x86)\Vista\ShiftHandOff”. A new directory may need to be created.

    Note: To complete these steps, administrator rights are required on the PC that is used when preforming this task.
3.  Create a Shortcut and name it, for example, V11-ShifthandoffTool.

<span id="_Toc174532172" class="anchor"></span>Figure 1: Shortcut Icon for V11-ShifthandoffTool

> ![](crhd-1-11-deployment-installation-back-out-and-rollback-guide/002.png)

4.  Determine the Domain Name System (DNS) server name or Internet Protocol (IP) address for the appropriate VistA server.
5.  Determine the Broker RPC port for the VistA account.
6.  Enter the IP address or DNS name and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

<span id="_Toc174532173" class="anchor"></span>Figure 2: CRHDv11 Properties

> ![](crhd-1-11-deployment-installation-back-out-and-rollback-guide/003.png)

> **NOTE:** The server and port number shown above are for example only.

### Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VISTA\] Verify the checksums for routines CRHD11PI and CRHDAM are equal to the checksums listed on the patch description.

\[GUI\] Launch the Shift Handoff Tool GUI and verify the splash screen announces version v1.0.11.2 is running.

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

\[VistA\] In section 4.8.1 (step 2 item B) the individual installing the patch used option \[Backup a Transport Global\] to create a PackMan message that will revert the Shift Handoff Tool components to their pre-v1.0.11.2 state. This includes everything transported in the CRHD\*1.0\*11 (Shift Handoff Tool v1.0.11) build. If for any reason that PackMan Message cannot be located, Contact HPS Sustainment: Clinical (see section 5.6).

\[GUI\] To revert to the Shift Handoff Tool GUI, the 1.0.10.2 GUI would have to be redistributed.

### Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Load Testing

No load testing was performed on Shift Handoff Tool v1.0.11.2. This was a maintenance release to correct defects discovered in Shift Handoff Tool v1.0.10.2. There was no additional functionality included.

#### User Acceptance Testing (UAT)

User acceptance testing was conducted by the two test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for CRHD\*1.0\*11. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to Health Services/Patient Care Services AC. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

### Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.

### Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out Shift Handoff Tool v1.0.11.2 would result in the re-instatement of the issues addressed from Shift Handoff Tool v1.0.10.2.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

### Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

### Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for Shift Handoff Tool v1.0.11.2 is in the event of a catastrophic failure.

Sites should log a Service Now Incident Contact the HPS Clinical Sustainment implementation team to notify that them there has been a catastrophic failure with Shift Handoff Tool v1.0.11.2.

If the decision is made to proceed with a back-out and rollback, the Health Services/Patient Care Services team is available to assist sites that have misplaced the previous V1.0.10.2 NPM message and provide the instructions on downloading the executable.

1.  \[VistA\]
1.  Open the NPM V1.0.10.2 Patch Message
2.  At the, “Enter message action (in IN basket): Ignore//” prompt enter X for \[Xtract PackMan\]
3.  At the, “Select PackMan function:” prompt select \[INSTALL/CHECK MESSAGE\]. The old routine is now restored.
4.  \[GUI\] Coordinate with the appropriate IT support, local and regional, to schedule the time to install CRHD\*1.0\*10.2 and to push out/install the previous GUI executable.
1.  Once CRHD\*1.0\*10.2 Vista patch and Shift Handoff Tool GUI v1.0.10.2 have been installed, verify operations before making available to all staff.

### Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure that the v1.0.10.2 executable launches properly.
2.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Appointed site staff can run the standard patch removal tool to back out the patch(es). If a site determines that a roll back is required, a ServiceNow ticket should be registered with the VA ESD for assistance with a rollback.

### Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following are checkpoints to consider when determining if the software needs to be rolled back:

- Conduct a check of the Transport Global backup.
- Validate the checksum(s).
- Check ServiceNow for the submission of previous VA ESD ticket resolutions.

### Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The criterion for rolling back to the previous version is that the application is not performing as expected.

### Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to roll back the CRHD\*1.0\*11 VistA patch and ShiftHandoff Tool v1.0.11.2 GUI is reached mutually among various stakeholders.

### Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once approval for a rollback has been obtained, follow the procedures detailed below to roll back to the previous version of the product.

Locate the results from your site’s Transport Global backup, done prior to installing the patches. The Transport Global backup creates a record of any routines exported with the installed patches. It will not back up any other changes, such as Data Dictionaries (DD) or templates.

### Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the rollback is complete, the OIT programmer should manually verify that the GUI and VistA patch rollback was successful. Verification is performed by opening the application and having the user ensure that the application is performing as expected. When rollback is complete, validate the previous version of the GUI displays.