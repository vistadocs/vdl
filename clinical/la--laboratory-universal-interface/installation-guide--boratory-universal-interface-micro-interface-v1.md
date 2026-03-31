---
title: "Laboratory: Universal Interface Micro Interface Version 1 Installation Guide"
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 1
patch_id: 
group_key: "LA::1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - test
  - strong
  - table
  - contents
  - culture
  - installation
  - build
  - accession
  - code
  - instrument
page_count: 0
word_count: 6907
section_count: 25
table_count: 2
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: February 2017
revision_count: 23
revision_newest: 02/02/2017
revision_oldest: 03/02/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_micro_interface_release_1_0_install_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_micro_interface_release_1_0_install_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

VistA Lab Enhancements – Microbiology

Release: Lab Micro Interface Release 1.0

(combined build for LA\*5.2\*90 and LR\*5.2\*474)

Deployment, Installation, Back-out, and Rollback Guide

![](laboratory-universal-interface-micro-interface-version-1-installation-guide/001.png)

February 2017

Document Version 3.2

Office of Information and Technology (OI&T)

Revision History

| Date       | Document Version | Description                                                                                                                                                                              | Author / Team Role                 |
|------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 02/02/2017 | 3.2              | Updates to Table 3.                                                                                                                                                                      | <span class="mark">REDACTED</span> |
| 01/10/2017 | 3.1              | Addition of version number for Data Innovation’s Instrument Manager.                                                                                                                     | <span class="mark">REDACTED</span> |
| 01/06/2017 | 3.0              | Minor technical edits based on feedback from Michael Belschwinder and Claudette Murch of Enterprise Project Management Office.                                                           | <span class="mark">REDACTED</span> |
| 01/05/2017 | 2.9              | Updated routine checksums in Table 5; addition of new examples for Figure 1. Figure 1 moved to Appendix. Removed section 5.2.1 Load Testing as not applicable. Captured install updated. | <span class="mark">REDACTED</span> |
| 12/20/2016 | 2.8              | Removed LR\*5.2\*463 information.                                                                                                                                                        | <span class="mark">REDACTED</span> |
| 12/16/2016 | 2.7              | Updated figure 1 and document names in section 4.3.                                                                                                                                      | <span class="mark">REDACTED</span> |
| 12/15/2016 | 2.6              | Reordered section 4.                                                                                                                                                                     | <span class="mark">REDACTED</span> |
| 12/14/2016 | 2.5              | Removed IOC Test Site information per feedback from Enterprise Project Management Office.                                                                                                | <span class="mark">REDACTED</span> |
| 12/07/2016 | 2.4              | Addition of Appendix.                                                                                                                                                                    | <span class="mark">REDACTED</span> |
| 12/05/2016 | 2.3              | Removed MMRS\*1.0\*4 related information.                                                                                                                                                | <span class="mark">REDACTED</span> |
| 11/30/2016 | 2.2              | Updated figure 1; examples provided by Randal Frommater.                                                                                                                                 | <span class="mark">REDACTED</span> |
| 11/28/2016 | 2.1              | Addition of Lab Micro Interface Release 1.0 captured install.                                                                                                                            | <span class="mark">REDACTED</span> |
| 11/07/2016 | 2.0              | Incorporation of MMRS\*1.0\*4 captured install.                                                                                                                                          | <span class="mark">REDACTED</span> |
| 11/02/2016 | 1.9              | Technical Edit provided by Enterprise Project Management Office; some verbiage updated.                                                                                                  | <span class="mark">REDACTED</span> |
| 09/21/2016 | 1.8              | Updated captured install in Appendix for MMRS.                                                                                                                                           | <span class="mark">REDACTED</span> |
| 09/20/2016 | 1.7              | Addition of post installation instructions and captured install example for MMRS.                                                                                                        | <span class="mark">REDACTED</span> |
| 09/18/2016 | 1.6              | Updated to include details for MMRS\*1.0\*4 and new patch LR\*5.2\*474. Information pertaining to LA\*5.2\*90 updated.                                                                   | <span class="mark">REDACTED</span> |
| 09/10/2016 | 1.5              | Added preliminary information for patch LR\*5.2\*474.                                                                                                                                    | <span class="mark">REDACTED</span> |
| 08/25/2016 | 1.4              | Updated document to include MMRS and LA\*5.2\*90 patches.                                                                                                                                | <span class="mark">REDACTED</span> |
| 05/05/2016 | 1.3              | Updated Build Name; completed formatting change to center table headings.                                                                                                                | <span class="mark">REDACTED</span> |
| 05/01/2016 | 1.2              | Removed Workload code instructions; added notation regarding Workload codes. Replaced Captured Install with updated example Appendix A and TOC.                                          | <span class="mark">REDACTED</span> |
| 03/17/2016 | 1.1              | Updated Section 5. Back-out Procedure.                                                                                                                                                   | <span class="mark">REDACTED</span> |
| 03/02/2016 | 1.0              | Baselined document for the release.                                                                                                                                                      | <span class="mark">REDACTED</span> |

<span id="_Toc457391409" class="anchor"></span>Table : Site Preparation

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

1 Introduction [1](#introduction)

1.1 Purpose [1](#purpose)

1.2 Dependencies [2](#dependencies)

1.3 Constraints [2](#constraints)

1.4 Orientation [2](#orientation)

1.4.1 Computer Dialogue [2](#computer-dialogue)

1.4.2 Instructions [2](#instructions)

1.4.3 User Response [2](#user-response)

2 Roles and Responsibilities [3](#roles-and-responsibilities)

3 Deployment [3](#deployment)

3.1 Site Preparation [4](#site-preparation)

3.2 Software [4](#software)

3.3 Communications [5](#communications)

4 Pre-Installation and Installation Preparation Instructions [5](#pre-installation-and-installation-preparation-instructions)

4.1 Platform Installation and Preparation [5](#platform-installation-and-preparation)

4.2 Installation Timing Recommendation [5](#installation-timing-recommendation)

4.2.1 Estimated Timing [6](#estimated-timing)

4.2.2 Kernel Patches [6](#kernel-patches)

4.2.3 Global Growth [6](#global-growth)

4.3 Download and Extract Files [6](#download-and-extract-files)

4.4 Access Requirements and Skills Needed for the Installation [6](#access-requirements-and-skills-needed-for-the-installation)

4.5 Pre-Installation and System Requirements [7](#pre-installation-and-system-requirements)

4.6 Installation Procedure [7](#installation-procedure)

5 Back-Out Procedure [9](#back-out-procedure)

5.1 Back-Out Strategy [9](#back-out-strategy)

5.2 Back-Out Considerations [9](#back-out-considerations)

5.3 Back-Out Criteria [9](#back-out-criteria)

5.4 Back-Out Risks [9](#back-out-risks)

5.5 Authority for Back-Out [9](#authority-for-back-out)

5.6 Back-Out Procedure [10](#back-out-procedure-1)

6 Rollback Procedure [10](#rollback-procedure)

6.1 Rollback Considerations [10](#rollback-considerations)

6.2 Rollback Criteria [10](#rollback-criteria)

6.3 Rollback Risks [10](#rollback-risks)

6.4 Authority for Rollback [10](#authority-for-rollback)

6.5 Rollback Procedure [10](#rollback-procedure-1)

Appendix A: Examples of Auto Instrument File and Load / WorklistS [11](#appendix-a-examples-of-auto-instrument-file-and-load-worklists)

Appendix B: Captured Install [18](#appendix-b-captured-install)

List of Figures

[FIGURE 1: EXAMPLES OF AUTO INSTRUMENT FILE AND LOAD / WORKLISTS [11](#_Toc471470484)](#_Toc471470484)

[FIGURE 2: CAPTURED INSTALLATION [18](#_Toc471470485)](#_Toc471470485)

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
  - [Orientation](#orientation)
    - [Computer Dialogue](#computer-dialogue)
    - [Instructions](#instructions)
    - [User Response](#user-response)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Site Preparation](#site-preparation)
  - [Software](#software)
  - [Communications](#communications)
- [Pre-Installation and Installation Preparation Instructions](#pre-installation-and-installation-preparation-instructions)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Installation Timing Recommendation](#installation-timing-recommendation)
    - [Estimated Timing](#estimated-timing)
    - [Kernel Patches](#kernel-patches)
    - [Global Growth](#global-growth)
  - [Download and Extract Files](#download-and-extract-files)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Pre-Installation and System Requirements](#pre-installation-and-system-requirements)
  - [Installation Procedure](#installation-procedure)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
- [Appendix A: Examples of Auto Instrument File and Load / Worklists](#appendix-a-examples-of-auto-instrument-file-and-load-worklists)
- [Appendix B: Captured Install](#appendix-b-captured-install)
The Installation, Back-out, Rollback Guide defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product. It provides installation instructions for the VistA Lab Enhancements (VLE) Microbiology project, release Lab Micro Interface Release 1.0.
The releases shall be distributed as follows:
- Lab Micro Interface Release 1.0, Kernel Information and Distribution System (KIDS) build available via Secure File Transfer Protocol (SFTP) from download.vista.med.va.gov
The Lab Micro Interface Release 1.0 is a combined build that contains the LR\*5.2\*474 and the LA\*5.2\*90 patches. The combined build will support the electronic bidirectional communication of automated identification and susceptibility testing instruments with the VistA Laboratory Universal Interface (UI) through middleware or a generic instrument manager.
Patch LR\*5.2\*474 will provide new functionality to the Enter/Verify Data option of the Lab UI package. Three new release actions will now be available to the Technologist with the authority to release results. Results will be available to the applicable authorized clinicians and providers. In addition, the patch will allow a VA Medical Center the option of setting release defaults at the Package or User level.
Patch LA\*5.2\*90 will provide the constructs necessary to allow Microbiology or MI subscripted tests to be added to an Auto Instrument entry. An enhancement is also included for antibiotic susceptibility result processing which will now allow laboratories the ability to report susceptibilities to antimicrobial agents by utilizing SNOMED CT codes such as Positive and Negative. The handling of variations is also included in the build, such as the reporting of extended-spectrum beta-lactamases or ESBL enzymes that are resistant to most beta-lactam antibiotics. Locally mapped codes using an “L” for code set ID will now be processed for antibiotic susceptibilities.
All of the following SNOMED CT codes shall be supported with the release of patch LA\*5.2\*90:
- 131196009 Susceptible
- 260357007 Moderately susceptible
- 264841006 Intermediately susceptible
- 30714006 Resistant
- 10828004 Positive
- 260385009 Negative

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the Lab Micro Interface Release 1.0 build will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LA\*5.2\*90 includes the following dependencies:

- LA\*5.2\*74
- LA\*5.2\*88

Patch LR\*5.2\*474 includes the following dependencies:

- LR\*5.2\*221
- LR\*5.2\*291
- LR\*5.2\*416
- LR\*5.2\*422
- LR\*5.2\*433
- LR\*5.2\*453

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security controls will be inherited from VistA and therefore will be fully compliant with National Institute of Standards and Technology (NIST) controls and in compliance with Directive 6500. In addition, Lab Micro Interface Release 1.0 will be 508 compliant and designed to ensure no performance impacts will be experienced in the production environments.

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses package or audience specific notations or directions (e.g., symbols used

to indicate terminal dialogues or user responses) for the installation instructions included in this document.

All headings and text in this guide are intentionally formatted flush left, regardless of the heading level, to save space and to make for better readability.

In tables which list mandatory steps (as for installation and post-installation), a column is provided at the right-hand side so that users may check () off the step as it is performed.

### Computer Dialogue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The computer dialogue will appear in Courier New 11-point font.

Example: Courier New font 11 points

### Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions will appear in Arial 11-point font.

Example: Arial font 11 points

### User Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User entry responses will appear in Courier New 11-point font.

Example: Courier New font 11 points

In VistA, every response you type must be followed by pressing the \< Return \> key or the \< Enter \> key.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment, installation, back-out, and roll-back roles and responsibilities are outlined in Table 1 which also lists the teams that will perform the tasks described in this guide.

<span id="_Toc457391406" class="anchor"></span>Table 1: Roles and Responsibilities

| ID | Team              | Phase / Role | Tasks                                                                                                                 |
|--------|-----------------------|------------------|---------------------------------------------------------------------------------------------------------------------------|
| 1      | Field Operations (FO) | Deployment       | Plan and schedule deployment (including orchestration with vendors).                                                      |
| 2      | FO                    | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                                |
| 3      | FO                    | Deployment       | Test for operational readiness.                                                                                           |
| 4      | FO                    | Deployment       | Execute deployment.                                                                                                       |
| 5      | FO                    | Installation     | Plan and schedule installation.                                                                                           |
| 6      | FO                    | Installation     | Ensure authority to operate and that certificate authority security documentation is in place.                            |
| 7      | FO                    | Installation     | Validate through facility point of contact to ensure that IT equipment has been accepted using asset inventory processes. |
| 8      | FO                    | Installations    | Coordinate training.                                                                                                      |
| 9      | FO                    | Back-out         | Confirm availability of back-out instructions and back-out strategy.                                                      |
| 10     | FO                    | Post Deployment  | Hardware, Software and System Support.                                                                                    |

<span id="_Toc457391411" class="anchor"></span>Table : Software Specifications

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Microbiology (Micro) Initiative is a collaborative solution between the VistA Laboratory Enhancement (VLE) Team and Clinical Laboratory personnel. This solution provides Micro Laboratory Technologists a system that integrates with the existing VistA Microbiology system.

A National Release is planned for January 2017 after testing has been successfully completed at two Test Sites.

Deployment will be performed by Local Facility staff and supported by team members from one or more of the operations organizations: Enterprise Systems Engineering (ESE), Field Operations (FO), Enterprise Operations (EO), and/or others.

## Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each site must prepare for the deployment, installation, and implementation of the Micro capabilities. The extent for which they must prepare will vary based upon the sites current processes.

The following table describes preparation required by the site prior to deployment.

<table>
<caption><p><span id="_Toc471329622" class="anchor"></span>Table : Files for Retrieval</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site/Other</strong></th>
<th><strong>Problem/Change Needed</strong></th>
<th><strong>Features to Adapt/Modify to New Product</strong></th>
<th><strong>Actions/Steps</strong></th>
<th><strong>Owner</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All</td>
<td>Determine changes to current processes.</td>
<td>Existing Micro MDRO and Instrument interface procedures.</td>
<td>Evaluate how new processes differ from current processes and adapt training accordingly.</td>
<td><p>Micro Technologists, Laboratory Information Managers (LIMs),</p>
<p>Facility Business Owners</p></td>
</tr>
<tr class="even">
<td>Sites using a VistA Micro currently.</td>
<td>Evaluate configuration changes that will need to be made to adapt to new Micro enhancements.</td>
<td>Existing Order Menus, Order Sets, and Quick Orders.</td>
<td>If using Generic Lab or Consult Order Types, determine if there are ordering menus, sets, and/or quick orders that need to be modified.</td>
<td><p>Micro Technologists, LIMs,</p>
<p>Facility Business Owners</p></td>
</tr>
</tbody>
</table>

<span id="_Toc471329622" class="anchor"></span>Table : Files for Retrieval

## Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment for the Lab Micro Interface Release 1.0.

<table>
<caption><p><span id="_Toc471329623" class="anchor"></span>Table : M Code Installation Instructions</p></caption>
<colgroup>
<col style="width: 38%" />
<col style="width: 17%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Software</strong></th>
<th><strong>Manufacturer</strong></th>
<th><strong>Other</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The following prerequisite release is required for the Lab Micro Interface Release 1.0:</p>
<ul>
<li><p>Lab Auto Release 1.0 (LR*5.2*458 and LA*5.2*88)</p></li>
</ul></td>
<td>Not applicable.</td>
<td>Local OI&amp;T staff will provide the assistance needed to ensure that the users have the latest patches and upgrades required for the build.</td>
</tr>
<tr class="even">
<td><strong>Data Innovations Instrument Manager (IM) version 8.13.03 or greater.</strong></td>
<td>Data Innovations</td>
<td>Local OI&amp;T staff and Data Innovations support will provide the assistance needed to ensure that the users have version 8.13.03 or greater of the IM for the utilization of the full functionality in the Lab Micro Interface Release 1.0 build.</td>
</tr>
<tr class="odd">
<td><strong>VA Hybrid Health Level Seven (HL7) driver v8.00.0018 or greater.</strong></td>
<td>Not applicable.</td>
<td>Local OI&amp;T staff will provide the assistance needed to ensure that the users have the latest HL7 driver.</td>
</tr>
</tbody>
</table>

<span id="_Toc471329623" class="anchor"></span>Table : M Code Installation Instructions

## Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Technicians will use email and conference calls for communication during the deployment; email and/or conference calls will be utilized to notify the stakeholders of the successful release of the product.

# Pre-Installation and Installation Preparation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides pre-installation and installation preparation instructions for the Lab Micro Interface Release 1.0 build.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Micro Interface Release 1.0 installation must be coordinated with the Laboratory Automated Data Processing Application Coordinator (ADPAC) at each site.

## Installation Timing Recommendation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Micro Interface Release 1.0 may be loaded with users on the system if the Lab Interface related activities have been halted, which includes, but is not limited to, the following:

- Editing of an Auto Instrument file entry.
- Turning off the Auto Downloading process to prevent the building and downloading

of a Load/Worklist to the Instrument Manager.

- Shutting down all LA7UI logical links and any other HL7 process (HLZTCP or HLLP processes) to prevent the processing of result messages from the IM.

### Estimated Timing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation will take less than 5 minutes.

### Kernel Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel patches must be current on the target system to avoid problems loading and/or installing this patch.

### Global Growth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no significant change to global growth.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The product and associated documentation will be available via the National Patch Tracking Module in FORUM and the SOFTWARE.DIR directory at the OI&T Field Offices listed below.

<span class="mark">REDACTED</span>

The preferred method is to retrieve the file(s) using Secure File Transfer Protocol (SFTP) from download.vista.med.va.gov, which transmits files from the first available SFTP server.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 53%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Contents</strong></th>
<th><strong>Retrieval Format</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LAB_MICRO_INTERFACE_ RELEASE_1_0.KID</td>
<td>Host File containing ASCII</td>
<td>ASCII</td>
</tr>
<tr class="even">
<td><p>LAB_MICRO_INTERFACE_</p>
<p>RELEASE_1_0_DOCS.ZIP</p></td>
<td><p>VLE Micro_Lab_Micro_Interface_Release_1.0_</p>
<p>Technical_Manual</p>
<p>VLE Micro_Lab_Micro_Interface_Release_1.0_</p>
<p>User_Guide</p>
<p>VLE Micro_Deployment_Installation_Roll Back_Back Out_Guide</p></td>
<td>Binary</td>
</tr>
</tbody>
</table>

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is written with the assumption that the reader is experienced or familiar with the following:

- VistA computing environment
- VA FileMan data structures and terminology
- Microsoft Windows

Local or Regional OI&T staff will coordinate the patch installation with the Laboratory Information Manager (LIM) at each site. The Local or Regional OI&T staff have the necessary access and skill set to conduct the installation.

## Pre-Installation and System Requirements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Micro Interface Release 1.0 installation must be coordinated with the Laboratory Automated Data Processing Application Coordinator (ADPAC) to ensure that all Lab Interface related activities are halted.

## Installation Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the instructions outlined in the Table below to install the software.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 66%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step #</strong></th>
<th colspan="2"><strong>Description</strong></th>
<th><strong></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td colspan="2">Access the KIDS menu (XPD MAIN).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td colspan="2">From the KIDS menu, select the Installation menu.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td colspan="2">From the Installation menu, select option #1: Load a Distribution.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td colspan="2">When prompted, ‘Enter a Host File:’, select LAB_MICRO_INTERFACE_RELEASE_1_0.KID</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td colspan="2">When prompted, ‘Want to Continue with Load? YES//’, respond "Yes".</td>
<td></td>
</tr>
<tr class="even">
<td><strong>6</strong></td>
<td colspan="2">When prompted, ‘Want to RUN the Environment Check Routine? YES//’ respond "Yes".</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>7</strong></td>
<td colspan="2">From the Installation menu, select option #2, Verify Checksums in Transport Global.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>8</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘LA*5.2*90’</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>9</strong></td>
<td colspan="2">When prompted ‘Want each Routine Listed with Checksums: Yes//’ respond “Yes”</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>a</strong></td>
<td><p>Verify the following routine information for LA*5.2*90:</p>
<p>LA7VHLU6 Calculated 58736241</p>
<p>LA7VIN2A Calculated 34485992</p>
<p>LA7VIN7 Calculated 83943151</p>
<p>LA7VIN7A Calculated 61187996</p>
<p>LA7VIN7B Calculated 65792075</p>
<p>LA90A Calculated 5670536</p></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>b</strong></td>
<td><p>Verify the following routine information for LR*5.2*474:</p>
<p>LRMIEDZ2 Calculated 72283385</p>
<p>LRVR0 Calculated 154172378</p>
<p>LRVRMI2 Calculated 36282264</p>
<p>LRVRMI2A Calculated 78602425</p>
<p>LRVRMI3 Calculated 26756120</p>
<p>LRVRMI4 Calculated 39771458</p>
<p>LRVRMI4A Calculated 96471289</p></td>
<td></td>
</tr>
<tr class="even">
<td><strong>10</strong></td>
<td colspan="2">From the Installation menu, select option #3, Print Transport Global</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>11</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘LA*5.2*90’</td>
<td></td>
</tr>
<tr class="even">
<td><strong>12</strong></td>
<td colspan="2">When prompted ‘Select one of the following:” respond “1” for Print Summary.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>13</strong></td>
<td colspan="2">When prompted ‘Want each Routine Listed with Checksums: Yes//’ respond “Yes”</td>
<td></td>
</tr>
<tr class="even">
<td><strong>14</strong></td>
<td colspan="2">From the Installation menu, select option #4, Compare Transport Global to Current System.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>15</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘LA*5.2*90’</td>
<td></td>
</tr>
<tr class="even">
<td><strong>16</strong></td>
<td colspan="2">When prompted ‘Select one of the following:” respond “2” for Second line of Routines only.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>17</strong></td>
<td colspan="2">From the Installation menu, select option #5: Backup a Global Transport.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>18</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘LA*5.2*90’</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>19</strong></td>
<td colspan="2">From the Installation menu, select option #6: Install Package(s).</td>
<td></td>
</tr>
<tr class="even">
<td><strong>20</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘LA*5.2*90’</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>21</strong></td>
<td colspan="2">When prompted 'Want KIDS to INHIBIT LOGONs during the install?  NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="even">
<td><strong>22</strong></td>
<td colspan="2">When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>23</strong></td>
<td colspan="2">When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="even">
<td><strong>24</strong></td>
<td colspan="2">When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>25</strong></td>
<td colspan="2">If prompted 'Delay Install (Minutes): (0 - 60): 0//', respond "NO".</td>
<td></td>
</tr>
<tr class="even">
<td><strong>26</strong></td>
<td colspan="2"><p>After receiving the message ‘Install Completed’, print out the Install for both the LA*5.2*90 and the LR*5.2*474 patches.</p>
<p>From the KIDS menu, select the Utilities menu.</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>27</strong></td>
<td colspan="2">From the Utilities menu, select Install File Print<strong>.</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>28</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘LA*5.2*90’</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>29</strong></td>
<td colspan="2">From the Utilities menu, select Install File Print<strong>.</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>30</strong></td>
<td colspan="2">When prompted ‘Select INSTALL NAME:’ respond ‘LR*5.2*474’</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>31</strong></td>
<td colspan="2">Save all printouts.</td>
<td></td>
</tr>
</tbody>
</table>

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The build does not make any changes that would affect the operational state of the software and platform settings. The functionality in the Lab Micro Interface Release 1.0 build will not be available until the installation process has been successfully completed.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation, if the option to back up routines was run as directed, ‘Backup a Transport Global’, then routines have the ability to be restored from the “backup” MailMan message that was generated. However, the KIDS installation process does not perform a restore of other VistA components, such as data dictionary, cross-reference, and template changes, etc.

Prior to attempting a back-out of the software, please contact the VA Help Desk at 1-855-673-4357 for support or assistance.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM and the Chief of Pathology have the authority to order the back-out.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Criteria for a back-out includes, but are not limited, to the following:

1.  Failed baseline testing.
2.  Non-recoverable software error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No back-out risks have been determined at this time.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM and the Chief of Pathology have the authority to order the Back-out Procedure.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The need for a back-out is highly unlikely, however if it is required, please contact the Product Support team for assistance.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LR\*5.2\*474 and LA\*5.2\*90 patches (part of the combined build, Lab Micro Interface Release 1.0) as well as any installed dependent patch changes that follow these releases need to be taken out in reverse of the order in which they were installed; routines and data dictionary modifications and populated data must also be rolled back in reverse order.

Please contact the VA Help Desk at 1-855-763-4357 for support or assistance regarding roll-back procedures.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback considerations have been determined at this time.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only criteria for a rollback that has been determined at this time is that the installation failed baseline testing.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only risk determined at this time is the possibility of downtime which would only effect the users of the Laboratory package.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM, the Lab Manager, and the Chief of Pathology have the authority to require the rollback and accept the risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The need for a rollback is highly unlikely, however if it is required, please contact the Product Support team for assistance. The rollback procedure will require Lab downtime and a reinstall of any previous KIDS versions.

# Appendix A: Examples of Auto Instrument File and Load / Worklists 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 1 below displays examples of the AUTO INSTRUMENT file (#62.4) and LOAD / WORKLIST pairs for the BD EpiCenter<sup>TM</sup> and bioMérieux Myla <sup>TM</sup> software and the BD Bactec<sup>TM</sup>, Dade MicroScan <sup>TM</sup>, and bioMérieux Vitek<sup>TM</sup> systems.

> **NOTE:** For more information on configurations with applicable middleware and analyzers, consult the manufacturer of the product(s).

<span id="_Toc471470484" class="anchor"></span>Figure : Examples of Auto Instrument File and Load / Worklists

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Auto Instrument: EPICENTER</strong></p>
<p>NUMBER: 285 NAME: EPICENTER</p>
<p>LOAD/WORK LIST: BACTEC FX</p>
<p>ENTRY for LAGEN ROUTINE: Accession cross-reference</p>
<p>CROSS LINKED BY: IDE MESSAGE CONFIGURATION: LA7UI3</p>
<p>METHOD: BACTEC DEFAULT ACCESSION AREA: MICROBIOLOGY</p>
<p>OVERLAY DATA: YES STORE REMARKS: YES</p>
<p>NUMBER: 1 TEST: BLOOD CULTURE</p>
<p>UI TEST CODE: STDANF ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES</p>
<p>NUMBER: 2 TEST: MYCOLOGY CULTURE</p>
<p>UI TEST CODE: MYCFLYTIC ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES</p>
<p>FILE BUILD ENTRY: EN FILE BUILD ROUTINE: LA7UID</p>
<p>AUTO DOWNLOAD: YES SHORT ACCESSION # LENGTH: 5</p>
<p>AUTO RELEASE: NO WKLD METHOD: BACTEC 9240</p>
<p>WKLD CODE METHOD NAME: BACTEC 9240 WKLD CODE SUFFIX: .7103</p>
<p><strong>Load/Worklist: BACTEC FX</strong></p>
<p>NAME: BACTEC FX LOAD TRANSFORM: UNIVERSAL</p>
<p>TYPE: TRAY,CUP CUPS PER TRAY: 10</p>
<p>FULL TRAY'S ONLY: NO INCLUDE UNCOLLECTED ACCESSIONS: NO</p>
<p>USER ACCESS AUTHORIZATION: LRVERIFY DATE OF SETUP: JUN 13, 2016</p>
<p>PROFILE: BLOOD CULTURE ACCESSION AREA: BLOOD CULTURE</p>
<p>UID VERIFICATION: ANY ACCESSION AREA STORE DUPLICATE COMMENTS: NO</p>
<p>DEFAULT REFERENCE LABORATORY: TAMPA VAMC</p>
<p>AUTO RELEASE: NO</p>
<p>TEST: BLOOD CULTURE BUILD NAME ONLY: NO</p>
<p>TEST: MYCOLOGY CULTURE BUILD NAME ONLY: NO</p>
<p>PROFILE: MYCOLOGY CULTURE ACCESSION AREA: FUNGAL</p>
<p>UID VERIFICATION: ANY ACCESSION AREA DEFAULT REFERENCE LABORATORY: TAMPA VAMC</p>
<p>AUTO RELEASE: NO</p>
<p>TEST: MYCOLOGY CULTURE BUILD NAME ONLY: NO</p>
<p>WKLD METHOD: BACTEC 9240 WKLD CODE METHOD NAME: BACTEC 9240</p>
<p>WKLD CODE SUFFIX: .7103 MAJOR ACCESSION AREA: MICROBIOLOGY</p>
<p>LAB SUBSECTION: BLOOD CULTURE</p>
<p><strong>Auto Instrument: VITEK MS</strong></p>
<p>NUMBER: 286 NAME: VITEK MS</p>
<p>LOAD/WORK LIST: VITEK MS</p>
<p>ENTRY for LAGEN ROUTINE: Accession cross-reference</p>
<p>CROSS LINKED BY: IDE MESSAGE CONFIGURATION: LA7UI3</p>
<p>METHOD: VITEK DEFAULT ACCESSION AREA: MICROBIOLOGY</p>
<p>OVERLAY DATA: YES STORE REMARKS: YES</p>
<p>NUMBER: 1 TEST: BLOOD CULTURE</p>
<p>UI TEST CODE: C ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES</p>
<p>NUMBER: 2 TEST: CULTURE &amp; SUSCEPTIBILITY</p>
<p>UI TEST CODE: C ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES</p>
<p>NUMBER: 3 TEST: MYCOLOGY CULTURE</p>
<p>UI TEST CODE: C ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES</p>
<p>NUMBER: 4 TEST: CULTURE &amp; SUSCEPTIBILITY</p>
<p>UI TEST CODE: o2-Final Organism Name ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: NO</p>
<p>FILE BUILD ENTRY: EN FILE BUILD ROUTINE: LA7UID</p>
<p>MICRO INTERPRETATION CHECK: CHECK BOTH FILE AND INSTRUMENT INTERPRETATION OVER</p>
<p>WRITE WITH FILE AUTO DOWNLOAD: YES</p>
<p>SHORT ACCESSION # LENGTH: 5 AUTO RELEASE: NO</p>
<p>WKLD METHOD: VITEK AMS WKLD CODE METHOD NAME: VITEK AMS</p>
<p>WKLD CODE SUFFIX: .7087</p>
<p><strong>Load/Worklist: VITEK MS</strong></p>
<p>NAME: VITEK MS LOAD TRANSFORM: UNIVERSAL</p>
<p>TYPE: SEQUENCE/BATCH CUPS PER TRAY: 0</p>
<p>FULL TRAY'S ONLY: NO EXPAND PANELS ON PRINT: NO</p>
<p>INCLUDE UNCOLLECTED ACCESSIONS: NO USER ACCESS AUTHORIZATION: LRVERIFY</p>
<p>DATE OF SETUP: JUL 15, 2016</p>
<p>PROFILE: CULTURE ACCESSION AREA: MICROBIOLOGY</p>
<p>UID VERIFICATION: ANY ACCESSION AREA STORE DUPLICATE COMMENTS: NO</p>
<p>DEFAULT REFERENCE LABORATORY: TAMPA VAMC</p>
<p>AUTO RELEASE: NO</p>
<p>TEST: BLOOD CULTURE BUILD NAME ONLY: NO</p>
<p>TEST: MYCOLOGY CULTURE BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE &amp; SUSCEPTIBILITY BUILD NAME ONLY: NO</p>
<p>WKLD METHOD: VITEK AMS WKLD CODE METHOD NAME: VITEK AMS</p>
<p>WKLD CODE SUFFIX: .7087 MAJOR ACCESSION AREA: MICROBIOLOGY</p>
<p>LAB SUBSECTION: MICROBIOLOGY</p>
<p><strong>Auto Instrument: VITEK II</strong></p>
<p>NUMBER: 287 NAME: VITEK II</p>
<p>LOAD/WORK LIST: VITEK II</p>
<p>ENTRY for LAGEN ROUTINE: Accession cross-reference</p>
<p>CROSS LINKED BY: IDE MESSAGE CONFIGURATION: LA7UI3</p>
<p>METHOD: VITEK DEFAULT ACCESSION AREA: MICROBIOLOGY</p>
<p>OVERLAY DATA: YES STORE REMARKS: YES</p>
<p>NUMBER: 1 TEST: CULTURE &amp; SUSCEPTIBILITY</p>
<p>UI TEST CODE: C ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES</p>
<p>NUMBER: 2 TEST: BLOOD CULTURE</p>
<p>UI TEST CODE: C ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES</p>
<p>NUMBER: 3 TEST: MYCOLOGY CULTURE</p>
<p>UI TEST CODE: C ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES</p>
<p>FILE BUILD ENTRY: EN FILE BUILD ROUTINE: LA7UID</p>
<p>AUTO DOWNLOAD: YES AUTO RELEASE: NO</p>
<p>WKLD METHOD: VITEK WKLD CODE METHOD NAME: VITEK</p>
<p>WKLD CODE SUFFIX: .7015</p>
<p><strong>Load/Worklist: VITEK II</strong></p>
<p>NAME: VITEK II LOAD TRANSFORM: UNIVERSAL</p>
<p>TYPE: SEQUENCE/BATCH CUPS PER TRAY: 0</p>
<p>FULL TRAY'S ONLY: NO EXPAND PANELS ON PRINT: NO</p>
<p>INCLUDE UNCOLLECTED ACCESSIONS: NO USER ACCESS AUTHORIZATION: LRVERIFY</p>
<p>DATE OF SETUP: SEP 16, 2016</p>
<p>PROFILE: CULTURE ACCESSION AREA: MICROBIOLOGY</p>
<p>UID VERIFICATION: ANY ACCESSION AREA STORE DUPLICATE COMMENTS: NO</p>
<p>DEFAULT REFERENCE LABORATORY: TAMPA VAMC</p>
<p>AUTO RELEASE: NO</p>
<p>TEST: CULTURE &amp; SUSCEPTIBILITY BUILD NAME ONLY: NO</p>
<p>TEST: BLOOD CULTURE BUILD NAME ONLY: NO</p>
<p>TEST: MYCOLOGY CULTURE BUILD NAME ONLY: NO</p>
<p>WKLD METHOD: VITEK AMS WKLD CODE METHOD NAME: VITEK AMS</p>
<p>WKLD CODE SUFFIX: .7087 MAJOR ACCESSION AREA: MICROBIOLOGY</p>
<p>LAB SUBSECTION: MICROBIOLOGY</p>
<p><strong>Auto Instrument: MICROSCAN</strong></p>
<p>NUMBER: 95                              NAME: MICROSCAN</p>
<p>  LOAD/WORK LIST: MICROSCAN</p>
<p>  ENTRY for LAGEN ROUTINE: Accession cross-reference</p>
<p>  CROSS LINKED BY: IDE                  MESSAGE CONFIGURATION: LA7UI1</p>
<p>  METHOD: MICROSCAN                     OVERLAY DATA: YES</p>
<p>  STORE REMARKS: YES</p>
<p>NUMBER: 1                               TEST: CULTURE, ABSCESS</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 2                               TEST: CULTURE, ASPIRATE</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 3                               TEST: CULTURE, BLOOD</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: BLOOD CULTURES</p>
<p>NUMBER: 4                               TEST: CULTURE, BODY FLUID</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 5                               TEST: CULTURE, TISSUE</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 6                               TEST: CULTURE, BONE</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 7                               TEST: CULTURE, BONE MARROW</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 8                               TEST: CULTURE, BRONCHIAL</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 9                               TEST: CULTURE, CATHETER TIP</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 10                              TEST: CULTURE, CSF</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 11                              TEST: CULTURE, EAR</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 12                              TEST: CULTURE, EYE</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 13                              TEST: CULTURE, GC</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 14                              TEST: CULTURE, SPUTUM</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 15                              TEST: CULTURE, STOOL</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 16                              TEST: CULTURE, URINE</p>
<p>  UI TEST CODE: ID                      ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>  DOWNLOAD TO INSTRUMENT: YES           STORE REMARKS: YES</p>
<p>  ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 17                              TEST: CULTURE, WOUND-DEEP</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES                    ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 18                              TEST: CULTURE, WOUND-SUPERFICIAL</p>
<p>  UI TEST CODE: ID                      ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>  DOWNLOAD TO INSTRUMENT: YES           STORE REMARKS: YES</p>
<p>  ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 19                              TEST: PRE-PROSTATE BIOPSY RECTAL SCREEN</p>
<p>  UI TEST CODE: ID                      ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>  DOWNLOAD TO INSTRUMENT: YES           STORE REMARKS: YES</p>
<p>  ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 20                              TEST: MDRO SCREEN</p>
<p>  UI TEST CODE: ID                      ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>  DOWNLOAD TO INSTRUMENT: YES           STORE REMARKS: YES</p>
<p>  ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>NUMBER: 21                              TEST: .CULTURE, THROAT</p>
<p>  UI TEST CODE: ID                      DOWNLOAD TO INSTRUMENT: YES</p>
<p>  STORE REMARKS: YES</p>
<p>  FILE BUILD ENTRY: EN                  FILE BUILD ROUTINE: LA7UID</p>
<p>  AUTO DOWNLOAD: YES                    WKLD METHOD: MICROSCAN</p>
<p>  WKLD CODE METHOD NAME: MICROSCAN      WKLD CODE SUFFIX: .7038</p>
<p><strong>Load/Worklist: MICROSCAN</strong></p>
<p>NUMBER: 109                             NAME: MICROSCAN</p>
<p>  LOAD TRANSFORM: UNIVERSAL             TYPE: SEQUENCE/BATCH</p>
<p>  CUPS PER TRAY: 0                      FULL TRAY'S ONLY: NO</p>
<p>  VERIFY BY: ACCESSION                  SUPPRESS SEQUENCE #: NO</p>
<p>  INCLUDE UNCOLLECTED ACCESSIONS: NO    DATE OF SETUP: NOV 12, 2016</p>
<p>  FIRST TRAY: 1                         STARTING CUP: 1</p>
<p>  LAST TRAY: 1                          BUILDING IN PROGRESS: NO</p>
<p>PROFILE: BLOOD CULTURE                  ACCESSION AREA: BLOOD CULTURES</p>
<p>  UID VERIFICATION: ANY ACCESSION AREA</p>
<p>TEST: CULTURE, BLOOD                    BUILD NAME ONLY: NO</p>
<p>PROFILE: MICROBIOLOGY                   ACCESSION AREA: MICROBIOLOGY CDD</p>
<p>  UID VERIFICATION: ANY ACCESSION AREA</p>
<p>TEST: CULTURE, ABSCESS                  BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, ASPIRATE                 BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, BODY FLUID               BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, BONE                     BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, BONE MARROW              BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, BRONCHIAL                BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, CATHETER TIP             BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, CSF                      BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, EAR                      BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, EYE                      BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, GC                       BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, SPUTUM                   BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, STOOL                    BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, TISSUE                   BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, URINE                    BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, WOUND-DEEP               BUILD NAME ONLY: NO</p>
<p>TEST: CULTURE, WOUND-SUPERFICIAL        BUILD NAME ONLY: NO</p>
<p>TEST: MDRO SCREEN                       BUILD NAME ONLY: NO</p>
<p>TEST: PRE-PROSTATE BIOPSY RECTAL SCREEN</p>
<p>  BUILD NAME ONLY: NO</p>
<p>TEST: .CULTURE, THROAT                  BUILD NAME ONLY: NO</p>
<p>  WKLD METHOD: MICROSCAN                WKLD CODE METHOD NAME: MICROSCAN</p>
<p>  WKLD CODE SUFFIX: .7038               MAJOR ACCESSION AREA: MICROBIOLOGY CDD</p>
<p><strong>Auto Instrument: MYLA</strong></p>
<p>NUMBER: 602 NAME: MYLA</p>
<p>LOAD/WORK LIST: IMB</p>
<p>ENTRY for LAGEN ROUTINE: Accession cross-reference</p>
<p>CROSS LINKED BY: IDE MESSAGE CONFIGURATION: LA7UI4</p>
<p>METHOD: MYLA DEFAULT ACCESSION AREA: IBACTERIOLOGY</p>
<p>OVERLAY DATA: YES STORE REMARKS: YES</p>
<p>NUMBER: 1 TEST: BLOOD CULTURE (AEROBE,ANAEROBE)</p>
<p>UI TEST CODE: C ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES STORE REMARKS: YES</p>
<p>ACCESSION AREA: IBLOOD CULTURE</p>
<p>NUMBER: 2 TEST: C&amp;S (AEROBIC) + GRAM STAIN</p>
<p>UI TEST CODE: CGS ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES STORE REMARKS: YES</p>
<p>ACCESSION AREA: IBACTERIOLOGY</p>
<p>NUMBER: 3 TEST: GRAM STAIN</p>
<p>UI TEST CODE: GS ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES STORE REMARKS: YES</p>
<p>ACCESSION AREA: IBACTERIOLOGY</p>
<p>NUMBER: 4 TEST: C&amp;S (AEROBIC CULTURE/SUSCEPT)</p>
<p>UI TEST CODE: CNS ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES STORE REMARKS: YES</p>
<p>ACCESSION AREA: IBACTERIOLOGY</p>
<p>NUMBER: 5 TEST: AFB CULTURE &amp; SMEAR</p>
<p>UI TEST CODE: AFB ACCEPT RESULTS FOR THIS TEST: YES</p>
<p>DOWNLOAD TO INSTRUMENT: YES ACCESSION AREA: IMYCOBACTERIUM</p>
<p>NUMBER: 6 TEST: C&amp;S (URINE CULTURE)*NE,IC</p>
<p>UI TEST CODE: UCS DOWNLOAD TO INSTRUMENT: YES</p>
<p>ACCESSION AREA: IBACTERIOLOGY</p>
<p>FILE BUILD ENTRY: EN FILE BUILD ROUTINE: LA7UID</p>
<p>AUTO DOWNLOAD: YES AUTO RELEASE: NO</p>
<p><strong>Load/Worklist: IMB</strong></p>
<p>NUMBER: 247 NAME: IMB</p>
<p>LOAD TRANSFORM: UNIVERSAL TYPE: SEQUENCE/BATCH</p>
<p>CUPS PER TRAY: 0 FULL TRAY'S ONLY: NO</p>
<p>EXPAND PANELS ON PRINT: NO INCLUDE UNCOLLECTED ACCESSIONS: NO</p>
<p>USER ACCESS AUTHORIZATION: LRVERIFY</p>
<p>PROFILE: IMB ACCESSION AREA: IBACTERIOLOGY</p>
<p>UID VERIFICATION: ANY ACCESSION AREA STORE DUPLICATE COMMENTS: YES</p>
<p>DEFAULT REFERENCE LABORATORY: IOWA CITY HCS</p>
<p>AUTO RELEASE: NO</p>
<p>TEST: BLOOD CULTURE (AEROBE,ANAEROBE) BUILD NAME ONLY: NO</p>
<p>TEST: C&amp;S (AEROBIC) + GRAM STAIN BUILD NAME ONLY: NO</p>
<p>TEST: GRAM STAIN BUILD NAME ONLY: NO</p>
<p>TEST: C&amp;S (AEROBIC CULTURE/SUSCEPT) BUILD NAME ONLY: NO</p>
<p>TEST: ANAEROBIC CULTURE BUILD NAME ONLY: NO</p>
<p>TEST: C&amp;S (URINE CULTURE)*NE,IC BUILD NAME ONLY: NO</p>
<p>WKLD METHOD: MANUAL MICRO WKLD CODE METHOD NAME: MANUAL MICRO</p>
<p>WKLD CODE SUFFIX: .7000 MAJOR ACCESSION AREA: IBACTERIOLOGY</p>
<p>LAB SUBSECTION: IBACTERIOLOGY</p>
<p><strong>Load/Worklist: IBC (a second one used for MYLA)</strong></p>
<p>NUMBER: 390 NAME: IBC</p>
<p>LOAD TRANSFORM: UNIVERSAL TYPE: SEQUENCE/BATCH</p>
<p>CUPS PER TRAY: 0 FULL TRAY'S ONLY: NO</p>
<p>EXPAND PANELS ON PRINT: NO INCLUDE UNCOLLECTED ACCESSIONS: NO</p>
<p>USER ACCESS AUTHORIZATION: LRVERIFY</p>
<p>PROFILE: IBC ACCESSION AREA: IBLOOD CULTURE</p>
<p>UID VERIFICATION: ANY ACCESSION AREA STORE DUPLICATE COMMENTS: YES</p>
<p>DEFAULT REFERENCE LABORATORY: IOWA CITY HCS</p>
<p>AUTO RELEASE: NO</p>
<p>TEST: BLOOD CULTURE (AEROBE,ANAEROBE) BUILD NAME ONLY: NO</p>
<p>TEST: FUNGAL BLOOD CULTURE*NE,IC BUILD NAME ONLY: NO</p>
<p>TEST: AFB CULTURE &amp; SMEAR BUILD NAME ONLY: NO</p>
<p>WKLD METHOD: MANUAL MICRO WKLD CODE METHOD NAME: MANUAL MICRO</p>
<p>WKLD CODE SUFFIX: .7000 MAJOR ACCESSION AREA: IBLOOD CULTU</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Appendix B: Captured Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of a captured install with LA\*5.2\*90 installed first followed by LR\*5.2\*474 as part of the installation process for the Lab Micro Interface Release 1.0 build.

<span id="_Toc471470485" class="anchor"></span>Figure : Captured Installation

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Installation &lt;TEST ACCOUNT&gt; Option: install Package(s)</p>
<p>Select INSTALL NAME: <mark>la*5.2*90</mark>      12/20/16@15:20:44</p>
<p>     =&gt; LAB MICRO INTERFACE RELEASE 1.0  ;Created on Dec 20, 2016@11:55:47</p>
<p>This Distribution was loaded on Dec 20, 2016@15:20:44 with header of</p>
<p>   LAB MICRO INTERFACE RELEASE 1.0  ;Created on Dec 20, 2016@11:55:47</p>
<p>   It consisted of the following Install(s):</p>
<p>      LA*5.2*90     LR*5.2*474</p>
<p>Checking Install for Package LA*5.2*90</p>
<p>Will first run the Environment Check Routine, LA90A</p>
<p>                        --- Environment Check is Ok ---                        </p>
<p>Install Questions for LA*5.2*90</p>
<p>Incoming Files:</p>
<p>   62.4      AUTO INSTRUMENT</p>
<p>Note:  You already have the 'AUTO INSTRUMENT' File.</p>
<p>Checking Install for Package <mark>LR*5.2*474</mark></p>
<p>Install Questions for LR*5.2*474</p>
<p>Want KIDS to INHIBIT LOGONs during the install? NO//</p>
<p>Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//</p>
<p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt.</p>
<p>Enter a '^' to abort the install.</p>
<p>DEVICE: HOME//   HOME(CRT)</p>
<p>                                  LR*5.2*474                                  </p>
<p></p>
<p> Installing PACKAGE COMPONENTS:</p>
<p> </p>
<p> Installing PARAMETER DEFINITION</p>
<p> Installing PARAMETER TEMPLATE</p>
<p>               Dec 20, 2016@15:21:18</p>
<p> Updating Routine file...</p>
<p> Updating KIDS files...</p>
<p> LR*5.2*474 Installed.</p>
<p>               Dec 20, 2016@15:21:18</p>
<p> Not a production UCI</p>
<p> NO Install Message sent</p>
<p></p>
<p>          </p>
<p>  100%                 25             50             75               </p>
<p>Complete  </p>
<p>Install Completed</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>