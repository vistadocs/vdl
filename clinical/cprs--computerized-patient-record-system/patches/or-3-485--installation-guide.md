---
title: OR*3*485 COVID-19 Identifier Deployment, Installation, Back-Out, and Rollback Guide CPRS GUI 31A
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: COVID-19 Identifier  CPRS GUI 31A
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*485
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
  - covid
  - install
  - back
  - rollback
  - deployment
  - site
page_count: 0
word_count: 5421
section_count: 34
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_485_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_485_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

CPRS v31a COVID-19 Identifier

Deployment, Installation, Back-Out, and Rollback Guide

![](or-3-485-covid-19-identifier-deployment-installation-back-out-and-rollback-guide/001.png)

April 2020

Office of Information and Technology (OI&T)

Revision History

| Date      | Version | Description | Author                         |
|---------------|-------------|-----------------|------------------------------------|
| April 6, 2020 | 1.0         | Initial Draft   | <span class="mark">REDACTED</span> |

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
    - [Update CPRS with All Lab Test Parameters](#update-cprs-with-all-lab-test-parameters)
    - [OR\3\485/PXRM\2\72 Multi-Package Build KIDS Installation](#or3485pxrm272-multi-package-build-kids-installation)
    - [GUI Installation](#gui-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Taxonomy Update](#taxonomy-update)
  - [Install Details](#install-details)
  - [Install Example](#install-example)
- [Configuration](#configuration)
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
This document describes how to deploy and install CPRS v31a COVID-19 Identifier*,* as well as how to back-out the product and rollback to a previous version. This build will consist of a host file that is a combination of the patches OR\*3\*485 and PXRM\*2\*72.
In addition, there are installation and configuration steps for the clinical application coordinators and laboratory information managers.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom CPRS v31a COVID-19 Identifier will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, a communications plan, and a rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patches are meant to be installed on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system. The installation of CPRS v31a COVID-19 Identifier is required for the future installations of CPRS GUI releases (such as v31b and v32).

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a COVID-19 Identifier is expected to be installed on existing VistA platforms.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because of the compressed timelines for this release, the CPRS business owner will approve this release solely.

If an issue with the software arises that would require a national rollback, the CPRS business owner will coordinate with several groups (including Patient Safety Health Product Support, Information Technology Operations Service (ITOPS), and Site leadership) to decide whether a back-out and rollback of the software is necessary. The Facility Area Manager has the final authority to require the patch back-out and data rollback and accept the associated risks.

The following table provides project information.

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
<td>Area Manager and IT support – which may be local or regional</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
<td>After national release</td>
</tr>
<tr class="odd">
<td></td>
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the CPRS Development Team during the compliance period. At the end of the compliance period, support will be transitioned to Clinical Sustainment</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
<td>After national release</td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because of the importance of the features released with this project, this must be released and installed by April 21, 2020.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The provisional timeline calls for the patch to be released and installed by April 21, 2020.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway. There are also instances, such as the Meds by Mail personnel who may not have a VistA instance but will have the executable deployed.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capabilities (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release the patches will be deployed to all VistA systems.

The Production (IOC) Test sites are:

- <span class="mark">REDACTED</span>

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

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an SDE Bulletin prior to the release of these patches advising sites of the upcoming release.

CPRS v31a COVID-19 Identifier will be deployed as an emergency release. After the patches are nationally released, sites must complete the installation by April 21, 2020. The project contains two patches: OR\*3\*485 and PXRM\*2\*72, as well as a CPRS GUI executable.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a COVID-19 Identifier assumes a fully patched VistA system.

## Backing Up Important Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do NOT permanently delete the existing CPRS GUI executable, 31.118 (file version 1.0.31.118). In the unlikely event a backout is needed, redistributing the 31.118 executable will be necessary.

> Important: These files will be important if, for some reason, there was a need for a rollback. Please retain these files for at least two weeks after installing the patch

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please check your system to verify that the following, previously released national patches are installed:

- OR\*3.0\*509
- PXRM\*2\*47

The VistA host file should take less than 5 minutes to install. The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.).

It is recommended that the installation be done during non-peak hours. If possible, users should not be in CPRS when the VistA installation is being performed.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31a COVID-19 Identifier is being released as one zip file plus a KIDS host file. Documentation can also be found on the VA Software Documentation Library at: <http://www.va.gov/vdl/>

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 43%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>Files to be downloaded</th>
<th>File Contents</th>
<th>Download Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR_30_485.ZIP</td>
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
<tr class="even">
<td><p>OR_30_485.DOCX</p>
<p>OR_30_485.PDF</p></td>
<td><ul>
<li><p>CPRS v31a COVID-19 Identifier: Deployment, Installation, Back-Out, and Rollback Guide</p></li>
</ul></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td><p>CPRSGUIUM.DOCX</p>
<p>CPRSGUIUM.PDF</p></td>
<td><ul>
<li><blockquote>
<p>CPRS User Guide: GUI Version</p>
</blockquote></li>
</ul></td>
<td>Binary</td>
</tr>
<tr class="even">
<td><p>CPRSGUITM.DOCX</p>
<p>CPRSGUITM.PDF</p></td>
<td><ul>
<li><blockquote>
<p>CPRS Technical Manual: GUI Version</p>
</blockquote></li>
</ul></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>OR_30_485.KID</td>
<td><ul>
<li><blockquote>
<p>OR*3.0*485</p>
</blockquote></li>
<li><blockquote>
<p>PXRM*2.0*72</p>
</blockquote></li>
</ul></td>
<td>ASCII</td>
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

Installation of CPRS v31a COVID-19 Identifier requires the following:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual workstation installs – access/ability to push executable to required workstations.
- Loader installs – access/ability to upload new executable to the GOLD directory.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Update CPRS with All Lab Test Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run Update CPRS Parameters option:  Update CPRS with all Lab test parameters

Select OE/RR interface parameters \<TEST ACCOUNT\> Option: CC  Update CPRS Parameters

   PA     Update CPRS with Lab order parameters

   SI     Update CPRS with Single Lab test

   UP     Update CPRS with all Lab test parameters

   DO     Domain Level Parameter Edit

   LO     Location Level Parameter Edit

   PP     Package Level Parameter Edit

   UL     Display Lab User Parameters

### OR\*3\*485/PXRM\*2\*72 Multi-Package Build KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This build should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. For the installation, it is recommended that users are off the system.

1.  Load the host file using the “Load a Distribution” option on the VistA XPD INSTALLATION MENU.
    1.  Note that after loading the distribution you are directed to use the name “CPRS COVID 1.0” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu.
3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the bundle of patches by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt, you will need to use the name “CPRS COVID 1.0” as noted in 1.a above.
5.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.

> Notes:

- During the install of the PXRM\*2.0\*72 patch in the bundle, you will be notified that a Reminder Exchange is being installed.
- Also, during the installation of PXRM\*2.0\*72, a list of reminder terms is listed that needs to be shared with the Clinical Application Coordinators.

### GUI Installation

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

1.  Locate the OR_30_485.ZIP and unzip the file.
2.  If this is an installation for a conventional, day-to-day CPRS user, then all files are typically copied into C:\Program Files (x86)\CPRS\\ or C:\Program Files\CPRS\\.

If this is an installation for a secondary use (e.g. testing or accessing a different version of CPRS), then copy all files into a different location than the conventional path above (e.g. "C:\Program Files (x86)\CPRSTest" or other appropriate naming).

> **NOTE:** The borlandmm.dll should reside in the same directory as CPRSChart.exe.

3.  Create a Shortcut and name it “Test CPRS”. This is to give the user another visual cue that this is not the normal CPRS icon.

    ![](or-3-485-covid-19-identifier-deployment-installation-back-out-and-rollback-guide/002.png)
4.  Determine the DNS server name or IP address for the appropriate VistA server.
5.  Determine the Broker RPC port for the VistA account.
6.  Enter IP and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

> Example of what the shortcut properties dialog might look like.

> ![](or-3-485-covid-19-identifier-deployment-installation-back-out-and-rollback-guide/003.png)

The server and port number shown above are not real and are for example only.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Launch the CPRS GUI and verify the splash screen now announces that you are running version 31.121.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new system configuration is required with this installation.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Taxonomy Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CAC: This step would be accomplished by a Clinical Application Coordinator (CAC).

After installation of the main patches, this Reminders Exchange file must be installed.

The exchange file contains one update:

REMINDER TAXONOMY

VA-COVID-19 DIAGNOSIS

## Install Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This update is being distributed as a mailman message.

The file will be installed using Reminder Exchange, programmer access is not required.

Installation:

=============

This update can be loaded with users on the system. Installation will take less than 1 minutes.

## Install Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To Load the mailman message, navigate to Reminder exchange in Vista.

![](or-3-485-covid-19-identifier-deployment-installation-back-out-and-rollback-guide/004.png)

2.  At the <u>Select Action:</u> prompt, enter <u>LMM</u> for Load MailMan Message
3.  At the <u>Choose:</u> prompt, Select the number for this entry and press \<enter\>:

CREX: VA-COVID-19 DIAGNOSIS

![](or-3-485-covid-19-identifier-deployment-installation-back-out-and-rollback-guide/005.png)

You should see the following message at the top of your screen that the file successfully loaded.

Loading MailMan message number 220723

Added Exchange entry VA-COVID-19 DIAGNOSIS

MailMan message 220723 successfully loaded.

4.  Search and locate an entry titled VA-COVID-19 DIAGNOSIS in reminder exchange.

![](or-3-485-covid-19-identifier-deployment-installation-back-out-and-rollback-guide/006.png)

5.  At the <u>Select Action</u> prompt, enter <span class="mark"><u>IFE</u></span> for Install Exchange File Entry
6.  Enter the number that corresponds with your entry VA-COVID-19 DIAGNOSIS *(in this example it is entry 236 it will vary by site).* The date of the exchange file should be 04/15/2020.

![](or-3-485-covid-19-identifier-deployment-installation-back-out-and-rollback-guide/007.png)

7.  At the <u>Select Action</u> prompt, type <span class="mark"><u>IA</u></span> for Install all Components and hit enter.

Select Action: Next Screen// <span class="mark">IA Install all Components</span>

8.  You will see several prompts, for all new entries you will choose <span class="mark">I to Install</span>

Select one of the following:

C Create a new entry by copying to a new name

O Overwrite the current entry

U Update

Q Quit the install

S Skip, do not install this entry

9.  At this prompt REMINDER TAXONOMY entry named VA-COVID-19 DIAGNOSIS already exists but the packed component is different, what do you want to do? Enter response: O// verwrite the current entry
10. Are you sure you want to overwrite? N// y
11. Type <u><span class="mark">Q.</span></u>

Install complete.

# Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is expected that this section will be completed by the Clinical Application Coordinators, along with Laboratory personnel, as needed.

A post-install process for CPRS v31a COVID-19 Identifier will automatically map tests beginning with COVID-19 to the related Reminder terms. After the installation completes, these terms must be reviewed to ensure accuracy and completeness.

> **NOTE:** Each term listed below must be reviewed to determine if any local data needs to be mapped to the national terms.

Reminder terms included in the reminder definition VA-COVID-19 CPRS STATUS:<u>VA-COVID-19 PCR LAB RESULTS POSITIVE</u>

This term will be mapped one time automatically with the lab tests in your lab file that start with the naming convention COVID-19.

1.  After patch install, confirm with your Lab Ad Pac that all local COVID-19 PCR tests are included; add any that are needed or remove any that are not appropriate. Do not include any COVID-19 antibody lab tests.
2.  This term has a condition to look for a result that equals "DETECTED" or a result that contains “POS". If your site uses something else other than “DETECTED” or ‘POSITIVE” to result a positive test, you will need to add a condition on each mapped finding item in the term to correctly identify what represents a positive result at your site.

<u>VA-COVID-19 PCR LAB RESULTS NEGATIVE</u>

This term will be mapped one time automatically with the lab tests in your lab file that start with the naming convention COVID-19.

1.  After patch install, confirm with your Lab Ad Pac that all local COVID-19 PCR tests are included; add any that are needed or remove any that are not appropriate. Do not include any COVID-19 antibody lab tests.
2.  This term has a condition to look for results that contain the word “NOT” or a result that contains “NEG”. If your site uses something other than “NOT DETECTED” or “NEGATIVE” to result a negative test, you will need to add a condition on each mapped finding item in the term to correctly identify what represents a negative result at your site.

<u>VA-COVID-19 PCR LAB ORDERS</u>

This term will be mapped one time automatically with the orderable items that start with the naming convention COVID-19.

> After patch install, confirm with your Lab Ad Pac that all local COVID-19 PCR orderable items are included; add any that are needed or remove any that are not appropriate.

<u>VA-COVID-19 OUTSIDE PCR LAB NEGATIVE</u>

This term represents that a COVID-19 PCR Lab test was documented (via health factor) as being performed outside the VA with a negative result. Use the HF finding distributed with this reminder term AND map any additional local HF findings that indicate negative outside lab test results for COVID-19 PCR.

This term will include the national health factor: VA-COVID-19 PCR LAB OUTSIDE NEGATIVE

<u>VA-COVID-19 OUTSIDE PCR LAB POSITIVE</u>

This term represents that a COVID-19 PCR Lab test was documented (via health factor) as being performed outside the VA with a positive result. Use the HF finding distributed with this reminder term AND map any additional local HF findings that indicate positive outside lab test results for COVID-19 PCR.

This term will include the national health factor: VA-COVID-19 PCR LAB OUTSIDE POSITIVE

<u>VA-COVID-19 PRESUMED</u>

This term represents the provider determination that the patient has COVID-19 or that COVID-19 is suspected.

Items included in term:

- National health factor: VA-COVID-19 SUSPECTED
- National taxonomy: VA-COVID-19 DIAGNOSIS

<u>VA-COVID-19 RECOVERED</u>

This term represents the provider determination that the patient has recovered from COVID-19. Use the HF findings distributed with this reminder term AND map any additional local HF findings that indicates a provider has determined that a patient has recovered from COVID-19.

This term will include the national health factor: VA-COVID-19 RESOLVED

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To revert to the previous version of CPRS v31a, site or region ITOPS personnel would reset the OR CPRS GUI CHART menu option to 118, rather than 121 and then redistribute the v31a 1.0.31.118 GUI. Details and examples of this procedure are included later in section 5.6.1.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on this release. There are only minor changes to this version.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the four test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of CPRS v31a COVID-19 Identifier. The sites either passed or failed any item based on testing. The tests were performed by Clinical Application Coordinators and others at each site who are familiar using the CPRS and Lab applications. The test cases were then delivered with concurrence by the sites to the CPRS development team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the CPRS application or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out these patches would remove the COVID-19 support functionality.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out the patch should only be considered if there is a catastrophic failure of OR\*3\*485 and PXRM\*2\*72 or the associated CPRS GUI. The back-out would be accomplished in two phases: reverting the OR CPRS GUI CHART menu option to version 118 and then pushing the CPRS v31a Windows 10 GUI.

### Back-Out Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out is in the event of a catastrophic failure.

1.  Contact the CPRS implementation team to notify them there has been a catastrophic failure with OR\*3\*485 and PXRM\*2\*72. Use the mail group: OIT PD CPRS Implementation Team <span class="mark">REDACTED</span> In addition, phone/use Skype/Teams to contact:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

2.  If the decision is made to proceed with back-out and rollback, coordinate with the appropriate IT support, local and ITOPS, to schedule the time to update the necessary option and to push out / install the previous GUI executable.
3.  Edit the OR CPRS GUI CHART menu option and change the 121 to 118.
4.  Using the method of distribution appropriate to your site (share, individual PC, etc.), redistribute the CPRS v31a 1.0.31.118 executable. If you require detailed assistance, please contact the CPRS Implementation team.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the OPTION file (#19) for OR CPRS GUI CHART is set to CPRSChart version 1.0.31.118.
2.  Ensure the v31a 1.0.31.118 executable launches properly.
3.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The backout patch will also perform any necessary rollback.

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

Select INSTALL NAME: cprs COVID 1.0 4/8/20@12:05:29

=\> OR\*3.0\*485_COVID COMBINED KIDS BUILD ;Created on Apr 08, 2020@09:

This Distribution was loaded on Apr 08, 2020@12:05:29 with header of

OR\*3.0\*485_COVID COMBINED KIDS BUILD ;Created on Apr 08, 2020@09:42:39

It consisted of the following Install(s):

CPRS COVID 1.0 PXRM\*2.0\*72 OR\*3.0\*485

Checking Install for Package CPRS COVID 1.0

Install Questions for CPRS COVID 1.0

Checking Install for Package PXRM\*2.0\*72

Install Questions for PXRM\*2.0\*72

Incoming Files:

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Checking Install for Package OR\*3.0\*485

Install Questions for OR\*3.0\*485

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME

--------------------------------------------------------------------------------

Install Started for CPRS COVID 1.0 :

Apr 08, 2020@12:05:44

Build Distribution Date: Apr 08, 2020

Installing Routines:

Apr 08, 2020@12:05:44

Install Started for PXRM\*2.0\*72 :

Apr 08, 2020@12:05:44

Build Distribution Date: Apr 08, 2020

Installing Routines:

Apr 08, 2020@12:05:44

Running Pre-Install Routine: PRE^PXRMP72I

Installing Data Dictionaries:

Apr 08, 2020@12:05:44

Installing Data:

Apr 08, 2020@12:05:44

Running Post-Install Routine: POST^PXRMP72I

1\. Installing Reminder Exchange entry VA-COVID-19 CPRS STATUS

Forward the list of reminder terms to the CACs

to review the following reminder terms setup for any

missing lab tests or orders

VA-COVID-19 PCR LAB RESULTS NEGATIVE

VA-COVID-19 PCR LAB RESULTS POSITIVE

VA-COVID-19 PCR LAB ORDERS

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*72 Installed.

Apr 08, 2020@12:05:44

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*485 :

Apr 08, 2020@12:05:44

Build Distribution Date: Apr 08, 2020

Installing Routines:

Apr 08, 2020@12:05:44

Installing PACKAGE COMPONENTS:

Installing REMOTE PROCEDURE

Installing OPTION

Installing PARAMETER DEFINITION

Apr 08, 2020@12:05:44

Updating Routine file...

Updating KIDS files...

OR\*3.0\*485 Installed.

Apr 08, 2020@12:05:44

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

CPRS COVID 1.0 Installed.

Apr 08, 2020@12:05:44

No link to PACKAGE file

NO Install Message sent

Install Completed