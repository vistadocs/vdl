---
title: Event Capture Version 2.0 GUI Deployment Installation Back-out and Rollback Guide (Updated EC*2*170)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: GUI  (Updated EC*2*170)
app_code: EC
app_name: Event Capture System (ECS)
section: FIN
app_status: active
pkg_ns: EC
patch_ver: 2.0
patch_id: EC*2.0
group_key: "EC:EC:2.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - patch
  - back
  - install
  - deployment
  - class
  - rollback
  - kids
page_count: 0
word_count: 5793
section_count: 34
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Event_Capture/ec_2_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Event_Capture/ec_2_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=39"
---

Event Capture System 2.0

Graphical User Interface

> Deployment, Installation, Back-out, and Rollback Guide

![](event-capture-version-2-0-gui-deployment-installation-back-out-and-rollback-guid/001.png)

April 2024

Office of Information and Technology

Revision History

<table>
<caption><p><span id="_Ref128572205" class="anchor"></span>Table DIBR Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 45%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
<tr class="odd">
<th>04/2024</th>
<th>1.7</th>
<th><p>ECS FY24 EC*2.0*165</p>
<p>Updated patch numbers, release date, and GUI Context version throughout document</p>
<p>Updated <a href="#kids-installation-example">4.8.3</a> KIDS Installation example</p></th>
<th>Booz Allen Hamilton</th>
</tr>
<tr class="header">
<th>10/2023</th>
<th>1.6</th>
<th><p>ECS FY23 EC*2.0*164</p>
<p>Updated patch numbers, release date, and GUI Context version throughout document</p>
<p>Updated <a href="#kids-installation-example">4.8.3</a> KIDS Installation example</p></th>
<th>Booz Allen Hamilton</th>
</tr>
<tr class="odd">
<th>06/2023</th>
<th>1.5</th>
<th><p>ECS FY23 EC*2.0*159</p>
<p>Updated patch number, release date, and GUI Context version throughout document</p>
<p>Updated <a href="#kids-installation-example">4.8.3</a> KIDS Installation example</p>
<p>Updated name of VistA support team in Table 1, Table 3, section 4.9, and section 6.5</p>
<p>Added “AC” to Table 5 Acronyms</p>
<p>Removed “HPS” and “HSP” from Table 5 Acronyms</p></th>
<th>Booz Allen Hamilton</th>
</tr>
<tr class="header">
<th>11/2022</th>
<th>1.4</th>
<th><p>ECS FY22 EC*2.0*161</p>
<p>Updated patch number, release date, and GUI Context version throughout document</p>
<p>Updated <a href="#kids-installation-example">4.8.3</a> KIDS Installation example</p></th>
<th>Booz Allen Hamilton</th>
</tr>
<tr class="odd">
<th>08/2022</th>
<th>1.3</th>
<th><p>ECS FY22 EC*2.0*158 v2</p>
<p>Updated 4.8.3 KIDS Installation example to reflect patch v2</p></th>
<th>Booz Allen Hamilton</th>
</tr>
<tr class="header">
<th>07/2022</th>
<th>1.2</th>
<th><p>ECS FY22 EC*2.0*158</p>
<p>Updated patch number, release date, and GUI Context version throughout document</p>
<p>Updated <a href="#kids-installation-example">4.8.3</a> KIDS Installation example</p></th>
<th>Booz Allen Hamilton</th>
</tr>
<tr class="odd">
<th>01/2022</th>
<th>1.1</th>
<th><p>ECS FY22 EC*2.0*156</p>
<p>Updated KIDS Installation example</p>
<p>Updated Patch Number and GUI Context version throughout document</p>
<p>Updated footer for template compliance and consistency</p>
<p>Added hyperlink for VDL</p>
<p>Updated Release date</p>
<p>Removed (optional) section “Facility Specifics”</p>
<p>Removed the Deployment/Installation/Back-Out Checklist table from section 3.3.3.1 because all cells were N/A</p></th>
<th>Booz Allen Hamilton</th>
</tr>
<tr class="header">
<th>02/2021</th>
<th>1.0</th>
<th><p>ECS FY21 EC*2*152</p>
<p>Modified in accordance with the <em>OIT End-User Documentation</em> Standards</p></th>
<th>Liberty IT Solutions</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref128572205" class="anchor"></span>Table DIBR Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the *Veteran-focused Integrated Process* (VIP) *Guide*, the *Deployment, Installation, Back-out, and Rollback Guide* (DIBR) is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

List of Tables

List of Figures

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
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-Installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [Load Transport Global](#load-transport-global)
    - [Server Installation](#server-installation)
    - [KIDS Installation Example](#kids-installation-example)
    - [Select Installation Option](#select-installation-option)
    - [Install Package(s)](#install-packages)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Client Installation](#client-installation)
  - [Command Line Parameters](#command-line-parameters)
  - [ECS GUI Client Installation](#ecs-gui-client-installation)
  - [Accessing ECS GUI via CPRS Single Sign-On](#accessing-ecs-gui-via-cprs-single-sign-on)
    - [Instructions for Setting Up the CPRS Menu](#instructions-for-setting-up-the-cprs-menu)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the Event Capture (EC) EC\*2.0\*165 patch, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.
The entry for Patch EC\*2.0\*165 in the National Patch Module (NPM) on FORUM provides detailed instructions for the installation of this patch. A copy of these instructions is distributed to sites in the PackMan e-mail message along with the software. This current document details the criteria for determining if a back-out is necessary, the authority for making that decision, the order in which installed components will be backed out, the risks and criteria for a rollback, and authority for acceptance or rejection of the risks.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Event Capture System (ECS) Fiscal Year 24 (FY24) Patch EC\*2.0\*165 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

The intended audience includes Technical Services, National Veterans Health Information Systems and Technology Architecture (VistA) Support and Software Quality Assurance (SQA).

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new dependencies beyond those covered under separate topics within this document that are being introduced in this version of the ECS application.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECS FY24 has the following constraint:

- Data is available from other packages

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 identifies, at a high level, the parties responsible for supporting VistA patches.

<table>
<caption><p><span id="_Toc131499860" class="anchor"></span>Table Software Specifications</p></caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
<th><strong>Project Phase</strong></th>
</tr>
<tr class="odd">
<th>VA Office of Information and Technology (OIT), VHA Finance Product Line (Tier 2 VistA Support) &amp; Project Management Office (PMO)</th>
<th>Deployment</th>
<th>Plan and schedule deployment (including orchestration with vendors)</th>
<th>Planning</th>
</tr>
<tr class="header">
<th>Local Individual Veterans Administration Medical Center (VAMC)</th>
<th>Deployment</th>
<th>Determine and document the roles and responsibilities of those involved in the deployment.</th>
<th>Planning</th>
</tr>
<tr class="odd">
<th>Field Testing (Initial Operating Capability – (IOC)), Tier 2 VistA Support &amp; VIP Release Agent Approval</th>
<th>Deployment</th>
<th>Test for operational readiness</th>
<th>Testing</th>
</tr>
<tr class="header">
<th>Tier 2 VistA Support Application Coordinators</th>
<th>Deployment</th>
<th>Execute deployment</th>
<th>Deployment</th>
</tr>
<tr class="odd">
<th>VIP Release Agent</th>
<th>Installation</th>
<th><p>Plan and schedule installation.</p>
<p>Obtain authority to operate and confirm that certificate authority security documentation is in place.</p></th>
<th>Deployment</th>
</tr>
<tr class="header">
<th><p>Managerial Cost Accounting Office (MCAO)</p>
<p>ECS Team</p></th>
<th>Installations</th>
<th>Coordinate knowledge transfer with the team responsible for user training.</th>
<th>Deployment</th>
</tr>
<tr class="odd">
<th>VIP Release Agent, Tier 2 VistA support ACs, and the ECS development team</th>
<th>Back-out</th>
<th>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</th>
<th>Deployment</th>
</tr>
<tr class="header">
<th>ECS Team</th>
<th>Post Deployment</th>
<th>Hardware, Software and System Support</th>
<th>Warranty</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc131499860" class="anchor"></span>Table Software Specifications

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Site deployment is divided into three distinct phases:

1.  Pre-Installation/Initial Site Setup
2.  Pre-Production/Test Environment Installation
3.  Production Environment Installation

Section 4 details the required steps each Initial Operating Capability (IOC) site must perform in order to successfully install Patch EC\*2.0\*165.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EC\*2.0\*165 is scheduled to be installed and deployed in the IOC site production environments. During this time, the testers will perform production testing and the Enterprise Service Line (ESL) Patch Installer will verify the installation to ensure there are no errors.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Per the Veteran-Focused Integration Process (VIP) guidelines, a Critical Decision (CD) 2 event will be conducted to review the patch and its readiness for release into the IOC production environment. Upon approval from ECS leadership, the patch will proceed to IOC production testing. Upon successful production testing, the patch is ready for National Release.

The Patch will be released by the Tier 2 VistA Support Application Coordinators (ACs), and the Patch Development Team will upload all relevant patch documentation to the [VA Software Documentation Library](https://www.va.gov/vdl/search.asp?group=application&terms=ECS) (VDL).

The Patch Development Team will provide support to Tier 2 VistA Support ACs.

The software product shall conform to the existing VistA conventions. The reports, options, and screen formats shall conform to the conventions using a Graphical User Interface (GUI). Pilot (Pre-Alpha, Alpha, and Beta) sites will test options processing for usability. This will ensure that all new functionality meets the needs of the Veterans Health Administration (VHA) user.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EC\*2.0\*165, a patch to the EC package, is installable on a fully patched Massachusetts General Hospital Utility Multi-Programming System (MUMPS) VistA system and operates on top of the VistA environment provided by the VistA infrastructure packages. The latter provide utilities which communicate with the underlying operating system and hardware, thereby providing ECS independence from variations in hardware and operating system.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECS FY24 Patch EC\*2.0\*165 will be deployed Enterprise-wide.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional site preparation activities are required. ECS FY24 will run under current site configuration.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the relevant hardware, software, facilities, and documentation for ECS FY24 Patch EC\*2.0\*165 deployment.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new hardware or other resources are required.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 2 describes the minimum version for VistA infrastructure software applications for installation and normal operation. The following package versions (or higher) must be installed prior to loading this patch of EC:

| Required Software                                                                              | Make | Version | Configuration | Manufacturer | Other |
|------------------------------------------------------------------------------------------------|------|---------|---------------|--------------|-------|
| Current Procedural Terminology (CPT) / Healthcare Common Procedure Coding System (HCPCS) Codes | \*   | 6.0     | \*            | \*           | \*    |
| Diagnosis Related Group (DRG) Grouper                                                          | \*   | 18      | \*            | \*           | \*    |
| Kernel                                                                                         | \*   | 8.0     | \*            | \*           | \*    |
| MailMan                                                                                        | \*   | 8.0     | \*            | \*           | \*    |
| Patient Care Encounter (PCE)                                                                   | \*   | 1.0     | \*            | \*           | \*    |
| Patient Information Management Service (PIMS)                                                  | \*   | 5.3     | \*            | \*           | \*    |
| Registration                                                                                   | \*   | 5.2     | \*            | \*           | \*    |
| Remote Procedure Call (RPC) Broker                                                             | \*   | 1.1     | \*            | \*           | \*    |
| ToolKit                                                                                        | \*   | 7.3     | \*            | \*           | \*    |
| FileMan                                                                                        | \*   | 22.2    | \*            | \*           | \*    |

<span id="_Ref128574016" class="anchor"></span>Table Release Deployment POC Information

\*Information maintained by the VA.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Communications with test sites continues to be through e-mail, Patch Tracking Message in FORUM and Outlook, and one-on-one telephone calls to individuals involved in testing.

#### Deployment/Installation/Back-out Checklist

The Release Management team will deploy the patch EC\*2.0\*165, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in FORUM.

FORUM automatically tracks the patches as they are installed in the different VAMC production systems. A report can be run in FORUM to identify when the patch was installed in the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch in their VistA production system. Therefore, this information will no longer be manually tracked in this document.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The electronic release package contains a single EXE file and supporting documentation. The executable is generated from a baseline. The electronic production release package media will be labeled with an identification number, descriptive name, and release date.

## Pre-Installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECS GUI may run in a test environment before installation, but this is not necessary. EC runs on the standard hardware platforms used by VA Healthcare facilities. These systems consist of Virtual Memory System (VMS)/Cache or Linux/Cache platforms.

To run this Delphi-based application, the following is recommended:

- Intel Core I3 or higher (I5 recommended)
- Microsoft Windows 7 or higher
- Memory: 4GB of RAM or higher
- Hard disk space: 50GB
- Extended Graphics Array (XGA) or higher resolution monitor

Software that is wholly a local development effort (e.g., BA Loader) may not be compatible with EC. Verify compatibility prior to installation.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new hardware or other resources are required.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EC\*2.0\*165 is provided to IOC sites as a Kernel Installation and Distribution System (KIDS) build via FORUM. Refer to the EC\*2.0\*165 patch documentation in the NPM.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch is applied to an existing MUMPS VistA database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation scripts are not needed for software installation. Refer to the EC\*2.0\*165 patch documentation in the National Patch Module.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Cron scripts associated with ECS or its installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the National VA Network, as well as the local network of each site to receive patches, is required to perform the installation, as well as authority to install patches.

Account Access Requirements for Installation:

- Access: Programmer @ sign to ensure all programmer access at the sites
- MailMan access

Skill level requirements for installation:

- Knowledge of GUI navigation and commands to support install
- Knowledge and ability to verify checksums
- Knowledge and ability to back up globally
- Knowledge and ability to check error traps
- Knowledge and ability to troubleshoot installation issues

Instructions on how to perform these installation functions are included in this installation guide, as well as in the formal NPM Patch Description that is sent to site/regional personnel prior to the installation.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The subsections below describe the steps for installing Patch EC\*2.0\*165.

### Load Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Choose the PackMan message containing the EC\*2.0\*165 patch and invoke the INSTALL/CHECK MESSAGE PackMan option.

### Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu to unload the KIDS distribution included with this message.
4.  From the KIDS Menu, select the Installation menu.
5.  The following steps are optional but are recommended. (When prompted for INSTALL NAME, enter EC\*2.0\*165):
1)  Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as Data Dictionaries (DD) or templates.
2)  Compare Transport Global to Current System - This option allows you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3)  Verify Checksums in Transport Global - This option allows you to ensure the integrity of the routines that are in the transport global.
4)  Print Transport Global - This option allows you to view the components of the KIDS build.
6.  Use the Install Package(s) option and select the package EC\*2.0\*165.
7.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' Answer NO
8.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
9.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer YES.
10. When prompted 'Enter options you wish to mark as 'Out of Order':' Enter the following options: EC GUI Context version 2.12.0.0
11. When prompted 'Enter protocols you wish to mark as 'Out of Order':' press \<Enter\>.

### KIDS Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: EC\*2.0\*165 11/27/23@09:52:49

=\> EC\*2.0\*165 v1

This Distribution was loaded on Nov 27, 2023@09:52:49 with header of

EC\*2.0\*165 v1

It consisted of the following Install(s):

EC\*2.0\*165

Checking Install for Package EC\*2.0\*165

Install Questions for EC\*2.0\*165

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

Enter options you wish to mark as 'Out Of Order': EC GUI CONTEXT

EC GUI Context version 2.11.1.0

Enter options you wish to mark as 'Out Of Order':

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// UCX/TELNET

--------------------------------------------------------------------------------

Install Started for EC\*2.0\*165 :

Nov 27, 2023@09:56:03

Build Distribution Date: Nov 27, 2023

Installing Routines:

Nov 27, 2023@09:56:03

Installing PACKAGE COMPONENTS:

Installing OPTION

Nov 27, 2023@09:56:03

Updating Routine file...

Updating KIDS files...

EC\*2.0\*165 Installed.

Nov 27, 2023@09:56:03

Not a production UCI

Install Completed

### Select Installation Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When prompted for the INSTALL NAME, enter EC\*2.0\*165

The following steps are optional, but are recommended:

1.  Backup a Transport Global  
    This option creates a backup message of any routines exported with this patch. It will not backup any other changes such as Data Dictionaries or templates.
12. Compare Transport Global to Current System  
    This option allows the installer to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, Data Dictionaries, templates, etc.).
13. Verify Checksums in Transport Global  
    This option allows the installer to ensure the integrity of the routines that are in the transport global.

### Install Package(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps start the installation of the KIDS patch:

1.  Choose the Install Package(s) option to start the patch install. Enter EC\*2.0\*165 when prompted for a build name.
14. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' respond NO.
15. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
16. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' respond YES.
17. When prompted 'Enter options you wish to mark as 'Out of Order', enter the following option:

    EC GUI Context version 2.11.2.0
18. When prompted 'Enter protocols you wish to mark as 'Out of Order' press \<Enter\>.
19. If prompted 'Delay Install (Minutes): (0-60): 0//' answer "0" (unless otherwise indicated).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Application Coordinator (AC) is responsible for coordinating the activities for the national release of the product or patch, representing Tier 2 VistA Support as a member of the project team for the product or patch release. This includes working with the appropriate Sustainment Manager (SM) to ensure a smooth and successful transition of the product from development to sustainment.

Table 3 lists the release deployment Point of Contact (POC) information for ECS FY24.

| Release Identification | Release Package POC Name                        | Release Package POC Email |
|------------------------|-------------------------------------------------|---------------------------|
| EC\*2.0\*165           | Tier 2 VistA Support Application Coordinator(s) | REDACTED                  |

<span id="_Toc131499862" class="anchor"></span>Table Command Line Parameters

The POC for each process will verify that all required inputs are available. Upon completion of each sub-task in the execution, the POC will verify that all required outputs have been generated and all the necessary exit criteria have been met.

The master process is not considered complete until all related sub-tasks for the perceived entry criteria have been completed. Verification and validation are performed to ensure that the processes executed meet the needs of the development effort and the execution of this process satisfies the certification requirements of the organization requesting the activity.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocation, or other resources is necessary for ECS Patch EC\*2.0\*165.

# Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides instructions for the ECS GUI command line parameters, client installation, and accessing ECS GUI via the Computerized Patient Record System (CPRS). Screen images have also been included.

## Command Line Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The necessary command line parameters are entered in the “Target” field of the shortcut properties. Table <span class="mark"></span>4 lists the Command Line Parameters. The parameters may be in any order. Parameters S and P are a set (i.e., they must both be present, or they will be ignored). To take advantage of the Clinical Context Object Workgroup (CCOW) Single Sign-on in Event Capture, add the CCOW parameter to the shortcut. The CCOW parameter should only be added if the Vergence desktop program is installed.

<table>
<caption><p><span id="_Ref128574182" class="anchor"></span>Table Acronyms</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Example (Default)</strong></th>
<th><strong>Description</strong></th>
</tr>
<tr class="odd">
<th>S=</th>
<th>S=BrokerServer</th>
<th>The name of the ECS GUI BrokerServer as defined in the Host file. The default is ‘BrokerServer’</th>
</tr>
<tr class="header">
<th>P=</th>
<th>P=nnnn</th>
<th><p>The ServerPort used by the ECS GUI BrokerServer.</p>
<p>Example P=9200</p></th>
</tr>
<tr class="odd">
<th>CCOW</th>
<th>CCOW</th>
<th>Enable EC to utilize CCOW Single Sign-on functionality.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref128574182" class="anchor"></span>Table Acronyms

## ECS GUI Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application file (ECS GUI.exe) is zipped into the file EC_2_P165.zip. Sites may retrieve the file EC_2_P165.zip directly from the VA Index of Software Documentation webpage.

> **NOTE:** It is strongly suggested to use Chrome for the download.Internet Explorer and Edge do not save the file with the correct file extension (.zip).

This application file will need to be unzipped and copied to a directory; a shortcut to that file can be created to run the application. These steps are listed below.

Follow these instructions to install the ECS GUI.

1.  Save the zip file to one of your network or local drives. Do not save it directly to the desktop.
20. Double-click on the zip file. The following window will appear (Figure 1).

<span id="_Toc109716722" class="anchor"></span>Figure Example of Opening the zip File

![](event-capture-version-2-0-gui-deployment-installation-back-out-and-rollback-guid/002.png)

21. Right-click the ECS GUI application file and select Copy.
22. Choose an existing folder to install the program or create a new one. (a common location is C:\Program Files\VistA\EC). Paste ECS GUI.exe into the target directory.
23. The application file will open in the explorer window for that directory (Figure 2).

<span id="_Toc109716723" class="anchor"></span>Figure Example of Application File in Folder

![](event-capture-version-2-0-gui-deployment-installation-back-out-and-rollback-guid/003.png)

24. Now that the application file is in the directory, right-click on it and select Send to Desktop (create shortcut).
25. A Shortcut should be created on the desktop (Figure 3).

<span id="_Toc109716724" class="anchor"></span>Figure Example of Desktop Shortcut

![](event-capture-version-2-0-gui-deployment-installation-back-out-and-rollback-guid/004.png)

26. Right-click on the newly created shortcut and select Properties and navigate to the shortcut tab.
27. After the file name (listed in Target), add the server (example: s=XXXX) and port (example: p=XXXX), as shown in Figure 4. Ensure there is a single space before the server and port information.
28. The server and port can be provided for a particular site. Without this information, EC will not be able to run. To enable EC to use CCOW Single Sign-on, add the text “CCOW” after the port information.
29. Click Apply.
30. The setup is complete.

    <span id="_Toc109716725" class="anchor"></span>Figure Example of Adding Server and Port to the Target Field

![](event-capture-version-2-0-gui-deployment-installation-back-out-and-rollback-guid/005.png)

## Accessing ECS GUI via CPRS Single Sign-On 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ECS user authentication can be achieved via Single Sign On (SSO) through CPRS. This is achieved by selecting the Event Capture Interface in the CPRS Tools Menu which allows the user to enter Event Capture patient procedures. When accessing Event Capture in this way, both user and patient context are maintained. This CPRS feature requires set up by local Technical Support and/or the Clinical Application Coordinator.

### Instructions for Setting Up the CPRS Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Parentheses denote abbreviations that can be entered instead of entering the full name of the option.

1.  From the CPRS Configuration Menu for Clinical Coordinators, enter GUI Parameters (GP) at the prompt.
31. From the list of options given, enter GUI Tool Menu Items (TM) at the prompt.
32. From the list of options given, enter Package (9). Choosing this option gives functionality to all users. Choose User (1) to assign this functionality to a single user.
33. The user will receive two messages; one regarding the parameters set for ‘Package’ and the other for the Setting of the CPRS GUI Tools Menu for Package.
34. The user will be asked to select a sequence. Type a question mark (?) to get a list of options.
35. Enter a number higher than the last option to add a new option.
36. When asked if you are adding a new option, enter YES.
37. When prompted for a “Name=Command”, enter: Event Capture Interface= plus the full path to the ECS executable. The specific words “Event Capture Interface” are required to maintain this context preserving functionality between CPRS and ECS. See Example:

    Event Capture Interface = "c:\program files\vista\ec\ecs gui.exe"
38. When asked to select a sequence again, press \<Enter\> to get out of the prompt.

> Example: Setting Up EC Option in the Tools Menu of CPRS GUI:

AL Allocate OE/RR Security Keys

KK Check for Multiple Keys

DC Edit DC Reasons

GP GUI Parameters ...

GA GUI Access – Tabs,RPL

MI Miscellaneous Parameters

NO Notification Mgmt Menu ...

OC Order Checking Mgmt Menu ...

MM Order Menu Management ...

LI Patient List Mgmt Menu ...

FP Print Formats

PR Print/Report Parameters ...

RE Release/Cancel Delayed Orders

US Unsigned orders search

EX Set Unsigned Orders View on Exit

NA Search orders by Nature or Status

CA Care Management Menu ...

DO Event Delayed Orders Menu ...

LO Lapsed Order search

PM Performance Monitor Report

Select CPRS Configuration (Clin Coord) Option: GP GUI Parameters

CS GUI Cover Sheet Display Parameters ...

HS GUI Health Summary Types

TM GUI Tool Menu Items

MP GUI Parameters - Miscellaneous

UC GUI Clear Size & Position Settings for User

RE GUI Report Parameters ...

NV GUI Non-VA Med Statements/Reasons

EX GUI Expired Orders Search Hours

RM GUI Remove Button Enabled

NON GUI Remove Button Enabled for Non-OR Alerts

CLOZ GUI Edit Inpatient Clozapine Message

COAG GUI Anticoagulation Parameters ...

\*\*\> Out of order: On hold

EIE GUI Mark Allergy Entered in Error

Select GUI Parameters Option: TM GUI Tool Menu Items

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[PERF.ISC-BAYPINES.VA.GOV\]

9 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 9 Package ORDER ENTRY/RESULTS REPORTING

Parameters set for 'Package' may be replaced if ORDER ENTRY/RESULTS REPORTING is installed in this account.

-- Setting CPRS GUI Tools Menu for Package: ORDER ENTRY/RESULTS REPORTING --

Select Sequence: ?

Sequence Value

-------- -----

1 &Time=Clock.exe

2 &Calculator=Calc.exe

3 &Windows Introduction=WinHlp32 Wind

4 &Notepad=Notepad.exe

Select Sequence: 5

Are you adding 5 as a new Sequence? Yes// YES

Sequence: 5// 5

Name=Command: &Event Capture Interface="c:\program files\vista\ec\ecs gui.exe"Note: If you desire to launch the full ECS application without maintaining User and Patient context, use a command name other than “Event Capture Interface.”

An example of this would be: ECS="c:\program files\vista\ec\ecs gui.exe"

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To revert to the previous version of Event Capture, EC\*2.0\*164 RB1, the ESL Patch Installer performs backups on routines prior to patch installation. If for any reason a need arises, the ESL Patch Installer will back out the patch and revert to the previous backup point to restore their respective environments. Any changes that need to be reapplied to the database will be manually applied.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event that the Patch EC\*2.0\*165 package needs to be backed out, the ESL Patch Installers will assist the site with removing the VistA routines as needed.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations would include the following:

- Health of site systems
- Ability to recover to a stable environment
- Minimal disruption to a site
- Minimize issues within the VistA host

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load Testing is not applicable. The back-out process for Patch EC\*2.0\*165 would be executed at a normal, rather than raised job priority, and expected to have minimal effect on total system performance. To minimize potential impact on users, implementation of a back-out can be queued to run during hours of reduced user activity. After the reversion, the performance demands on the system would be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is expected that the restoration of the pre-EC\*2.0\*165 version of routines could be confirmed by IT Support quickly using utility CHECK1^XTSUMBLD, which returns the checksum or routine comparison utilities from VA Kernel without any need of User Acceptance Testing (UAT).

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out of the software should only be performed in response to severe system impairment and there is no other option available.

Booz Allen Hamilton (BAH) will analyze the issue and related system functionality impairment and provide feedback. Based on the severity of the condition, a determination will be made by the Back-out authorities if a back-out of the software is required.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks for a back-out include:

- Further corruption of system
- Inability to completely remove all software code from system
- Loss of system functionality while back-out is in progress
- Loss of data; some records may never be recovered

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The order would come from the Portfolio Director, the VA Project Manager, and the Business Owner. The Tier 2 VistA Support Application Coordinator(s) will work to identify the problem and assist with implementation. This should be done in consultation with the development team and project stakeholders.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If for any reason a need arises, the ESL Patch Installer will back out the patch and revert to the previous backup point to restore their respective environments. Any changes that need to be reapplied to the database will be manually applied. It may be necessary for the developer to be given access to the site to assist with these procedures.

Prior to installing an updated KIDS package, the ESL Patch Installer should have saved a backup of the routines in a mail message, using the Backup a Transport Global \[XPD BACKUP\] menu option (this is done at the time of install). The message containing the backed-up routines can be loaded with the "Xtract PackMan" function at the Message Action prompt. The PackMan function INSTALL/CHECK MESSAGE is then used to install the backed-up routines onto the VistA system.

Coordinate with the ECS development team to receive a copy of the previous EC\*2.0\*164 RB1 GUI executable and installation instructions.

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is expected that the restoration of the pre-EC\*2.0\*165 version of routines could be confirmed by IT Support quickly using utility CHECK1^XTSUMBLD, which returns the checksum or routine comparison utilities from VA Kernel. Manually check database changes to verify that files are in their previous state.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Rollback Procedure pertains to data. ECS does not roll back to the previous state of the data and/or platform settings.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

#### Acronyms

Table 5 lists the acronyms utilized throughout the ECS FY24 Deployment, Installation, Back-Out and Rollback Guide.
| Acronym | Description                                                     |
|---------|-----------------------------------------------------------------|
| AC      | Application Coordinator                                         |
| CCOW    | Clinical Context Object Workgroup                               |
| CD      | Critical Decision                                               |
| CM      | Configuration Management                                        |
| CPRS    | Computerized Patient Record System                              |
| CPT     | Current Procedural Terminology                                  |
| DD      | Data Dictionary                                                 |
| DIBR    | Deployment, Installation, Back-Out, and Rollback Guide          |
| DRG     | Diagnosis Related Group                                         |
| EC      | Event Capture                                                   |
| ECS     | Event Capture System                                            |
| ESL     | Enterprise Service Line                                         |
| FY      | Fiscal Year                                                     |
| GP      | GUI Parameter                                                   |
| GUI     | Graphical User Interface                                        |
| HCPCS   | Healthcare Common Procedure Coding System                       |
| IOC     | Initial Operating Capability                                    |
| IT      | Information Technology                                          |
| KIDS    | Kernel Installation and Distribution System                     |
| MCA     | Managerial Cost Accounting                                      |
| MCAO    | Managerial Cost Accounting Office                               |
| MUMPS   | Massachusetts General Hospital Utility Multi-Programming System |
| N/A     | Not Applicable                                                  |
| NPM     | National Patch Module                                           |
| OIT     | Office of Information and Technology                            |
| PCE     | Patient Care Encounter                                          |
| POC     | Point of Contact                                                |
| RB1     | Release Build 1                                                 |
| RPC     | Remote Procedure Call                                           |
| SM      | Sustainment Manager                                             |
| SQA     | Software Quality Assurance                                      |
| TM      | Tool Menu                                                       |
| UAT     | User Acceptance Testing                                         |
| VA      | Department of Veterans Affairs                                  |
| VDL     | VA Software Documentation Library                               |
| VHA     | Veterans Health Administration                                  |
| VIP     | Veteran-Focused Integration Process                             |
| VISN    | Veterans Integrated Service Network                             |
| VistA   | Veterans Health Information Systems and Technology Architecture |
| VMS     | Virtual Memory System                                           |
| XGA     | Extended Graphics Array                                         |
Acronym Table
