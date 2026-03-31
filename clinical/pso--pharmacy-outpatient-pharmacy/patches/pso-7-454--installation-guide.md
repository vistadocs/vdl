---
title: PSO*7*454 OneVA Pharmacy Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: OneVA Pharmacy
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*454
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: This document describes how to deploy and install OneVA Pharmacy Patch (PSO\7.0\454).
audience: 
keywords: 
  - pharmacy
  - table
  - oneva
  - contents
  - installation
  - flag
  - span
  - class
  - vista
  - patch
page_count: 0
word_count: 4741
section_count: 28
table_count: 3
figure_count: 12
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2016
revision_count: 12
revision_newest: 11/21/16
revision_oldest: 07/17/16
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_p454_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_p454_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

OneVA Pharmacy (PSO\*7.0\*454)

Deployment, Installation, Back-Out, and Rollback Guide

![](pso-7-454-oneva-pharmacy-installation-guide/001.png)

November 2016

Revision History

| Date     | Version | Description                                                                                                               | Author                             |
|----------|---------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 11/21/16 | 1.8     | Update deployment schedule                                                                                                | <span class="mark">REDACTED</span> |
| 10/31/16 | 1.7     | Update deployment schedule                                                                                                | <span class="mark">REDACTED</span> |
| 10/13/16 | 1.6     | Applied feedback from reviewers                                                                                           | <span class="mark">REDACTED</span> |
| 09/30/16 | 1.5     | Applied feedback from reviewers                                                                                           | <span class="mark">REDACTED</span> |
| 09/29/16 | 1.4     | Updated for VIP Style Guide requirements and label device modifications; updated IOC site evaluation; deployment schedule | <span class="mark">REDACTED</span> |
| 07/25/16 | 1.3     | Technical Edit/Section 508 Compliance/Corrected Table of Contents                                                         | <span class="mark">REDACTED</span> |
| 07/20/16 | 1.2     | Review                                                                                                                    | <span class="mark">REDACTED</span> |
| 07/20/16 | 1.1     | Update VA Links                                                                                                           | <span class="mark">REDACTED</span> |
| 07/18/16 | 1.0     | Baseline                                                                                                                  | <span class="mark">REDACTED</span> |
| 07/18/16 | 0.3     | Review                                                                                                                    | <span class="mark">REDACTED</span> |
| 07/18/16 | 0.2     | Review                                                                                                                    | <span class="mark">REDACTED</span> |
| 07/17/16 | 0.1     | Initial Draft                                                                                                             | <span class="mark">REDACTED</span> |

<span id="_Toc467501138" class="anchor"></span>Table 1: Document Conventions Symbols
# Table of Tables


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Table of Tables](#table-of-tables)
- [Table of Figures](#table-of-figures)
- [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
  - [Documentation Conventions](#documentation-conventions)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Timeline](#timeline)
    - [Deployment Topology](#deployment-topology)
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
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
    - [Host Site OneVA Pharmacy Flag Not Set On Message](#host-site-oneva-pharmacy-flag-not-set-on-message)
    - [Steps to Turn On ONEVA PHARMACY FLAG (#3001)](#steps-to-turn-on-oneva-pharmacy-flag-3001)
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
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
Table 1: Document Conventions Symbols [6](#_Toc467501138)
Table 2: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities [7](#_Toc467501139)
Table 3: Site Preparation [10](#_Toc467501140)
Table 4: Facility-Specific Features [10](#_Toc467501141)
Table 5: Deployment/Installation [11](#_Toc467501142)

# Table of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

igure 1: OneVA Pharmacy TimeLine [9](#_Toc467501143)

Figure 2: OneVA Pharmacy Flag: VA FileMan [15](#_Toc467501144)

Figure 3: OneVA Pharmacy Flag: Enter FM Prompt [15](#_Toc458500067)

Figure 4: OneVA Pharmacy Flag: VA FileMan Menu Prompt [16](#_Toc458500068)

Figure 5: OneVA Pharmacy Flag: Enter \<EN\> to Enter or Edit File Entries Prompt [16](#_Toc458500069)

Figure 6: OneVA Pharmacy Flag: Input to What File Prompt [16](#_Toc458500070)

Figure 7: OneVA Pharmacy Flag: Edit Which Filed Prompt [16](#_Toc458500071)

Figure 8: OneVA Pharmacy Flag: Then Edit Field Prompt [16](#_Toc458500072)

Figure 9: OneVA Pharmacy Flag: Select OUTPATIENT SITE NAME Prompt [17](#_Toc458500073)

Figure 10: OneVA Pharmacy Flag: ^LOOP Command [17](#_Toc458500074)

Figure 11: OneVA Pharmacy Flag: Edit Entries by: NAME// Prompt [17](#_Toc458500075)

Figure 12: OneVA Pharmacy Flag: Start with Name Prompt [17](#_Toc458500076)

Figure 13: OneVA Pharmacy Flag: Loop Command Example [18](#_Toc458500077)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install OneVA Pharmacy Patch (PSO\*7.0\*454).

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the OneVA Pharmacy Patch will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The overall OneVA Pharmacy design has several components. They are:

1.  Veterans Health Information Systems and Technology Architecture (VistA) (Patch PSO\*7.0\*454)
2.  Health Level 7 (HL7) Messaging
3.  Enterprise Messaging Infrastructure (eMI) Enterprise Service Bus (ESB)
4.  Health Data Repository/Clinical Data Service (HDR/CDS)
- Patch PSO\*7\*427 must be installed before PSO\*7\*454.
- Patch PSO\*7\*444 must be installed before PSO\*7\*454.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OneVA Pharmacy is dependent on the integration of the eMI ESB and the HDR/CDS Repository using Logical Link communication. A new HL7 logical link, PSORRXSEND, facilitates the sending/receiving of the HL7 messages via eMI. The PSO VISTA PHARM and PSO EMI PHARM application parameters control the message processing within VistA. The existing VA multi-threaded listener is leveraged at each facility for receiving the HL7 messages into VistAs production environment. The constraint is that there is no communication established from a sites VistA test mirror account to eMI therefore the software is unable to be tested in the VistA test mirror account.

Another constraint would be for sites that have made local modifications to the same routines released in the OneVA Pharmacy Patch. Those sites would need to retrofit the software which may delay the ability to install the OneVA Pharmacy Patch in the mandated time frame.

## Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Various symbols used throughout the documentation to alert the reader to special information.

The following table gives a description of each of these symbols.

| Symbol                                                                                                                                                                                                                                     | Description                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](pso-7-454-oneva-pharmacy-installation-guide/002.png)                  | NOTE: Used to inform the reader of general information including references to additional reading material |
| ![](pso-7-454-oneva-pharmacy-installation-guide/003.png) | CAUTION: Used to caution the reader to take special notice of critical information                         |
| ![](pso-7-454-oneva-pharmacy-installation-guide/004.png)                                                                                                            | ACTION: Required action by VistA support personnel.                                                        |

<span id="_Toc467501139" class="anchor"></span>Table 2: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Leadership at the VAs Grassroots Innovations Program, a cooperative effort between the Chief Technology Officer, the Health and Medical Informatics Office, and the VAs Office of Information and Technology (OI&T) provided innovators (VA employees) with a forum to propose new opportunities and to develop new ideas into functional prototypes.

The OneVA Pharmacy is an Innovations Program initiative. OneVA Pharmacy software provides the Department of Veterans Health Administration (VHA) the capability to allow Veterans traveling across the United States to refill or partial their active VA non-controlled substance prescriptions at any VA Pharmacy location regardless of where the prescription originated. The Patch expands available pharmacy information in Veterans Health Information Systems and Technology Architecture (VistA) to Pharmacists, providing direct access to any active and refillable prescription from any VA Pharmacy location.

OneVA Pharmacy software provides a foundation to build and extend new capabilities to the Veteran.

- PMAS Project Number: N/A
- Current PMAS state: N/A
- EPS Code(s): <span class="mark">REDACTED</span>
- Proposed Production Install Date: Q4FY16
- Business Owner: <span class="mark">REDACTED</span>
- FISMA System Owner: N/A; This system falls under VistA Outpatient Pharmacy

<table>
<caption><p><span id="_Toc467501140" class="anchor"></span>Table 3: Site Preparation</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 46%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
<th><p><strong>Project Phase</strong></p>
<p><strong>Schedule</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ePIP</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
<td>To be completed by 10/24/2016</td>
</tr>
<tr class="even">
<td>ePIP</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
<td>To be completed by 10/24/2016</td>
</tr>
<tr class="odd">
<td>OneVA Pharmacy</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
<td>To be complete by 10/24/2016</td>
</tr>
<tr class="even">
<td>ePIP</td>
<td>Deployment</td>
<td>Execute deployment</td>
<td>To be complete by 01/13/2017</td>
</tr>
<tr class="odd">
<td><p>OneVA Pharmacy – IOC only</p>
<p>ePIP - deployment</p></td>
<td>Installation</td>
<td>Plan and schedule installation</td>
<td><p>To be complete by 10/24/2016</p>
<p>To be completed by 01/13/2017</p></td>
</tr>
<tr class="even">
<td>N/A</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
<td>Falls within existing ATOs</td>
</tr>
<tr class="odd">
<td>N/A</td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
<td>VistA Patch</td>
</tr>
<tr class="even">
<td>OneVA Pharmacy - IOC</td>
<td>Installations</td>
<td>Coordinate training</td>
<td>Completed on 8/8//2016</td>
</tr>
<tr class="odd">
<td>OneVA Pharmacy</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
<td>Completed in Software Quality Assurance (SQA) 7/13/2016</td>
</tr>
<tr class="even">
<td>ePIP/Health Product Support (HPS)</td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
<td>To be completed by 01/3/2017</td>
</tr>
</tbody>
</table>

<span id="_Toc467501140" class="anchor"></span>Table 3: Site Preparation

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two separate deployments for the OneVA Pharmacy Patch supported by two teams. They are:

1.  IOC Site Production Deployment completed by the OneVA Pharmacy Team
2.  National Deployment completed by the ePIP Team

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy Deployment Timeline is depicted in the following image. Also refer to the [Deployment/Installation/Back-Out Checklist](#deploymentinstallationback-out-checklist) within this section for further details.

<span id="_Toc467501143" class="anchor"></span>Figure 1: OneVA Pharmacy TimeLine

![](pso-7-454-oneva-pharmacy-installation-guide/005.png)

![](pso-7-454-oneva-pharmacy-installation-guide/006.png) Site Readiness Assessment will be a part of the ePIP Deployment Plan

### Deployment Topology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the [Timeline](#timeline) introduction paragraph for OneVA Pharmacy deployment topology.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IOC production deployment sites are Denver, Salt Lake City, and Grand Junction. The OneVA Pharmacy Patch was delivered to the Information Technology (IT) support staff responsible for the VistA installation at those sites. The software is installed in the IOC test and production environments.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy is a VistA Patch therefore; no additional site preparation is necessary. Each site will be required to install Patches PSO\*7\*427 and PSO\*7.0\*444 as they are dependent patches. Each site will need to ensure eMI connections are established. The OneVA Pharmacy VistA Patch sends/receives HL7 messages via eMI to/from an existing port on the VistA system.

<table>
<caption><p><span id="_Toc467501141" class="anchor"></span>Table 4: Facility-Specific Features</p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
<th><strong>Change Needed</strong></th>
<th><strong>Features</strong></th>
<th><strong>Actions/Steps</strong></th>
<th><strong>Owner</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Denver</td>
<td>Install Patch</td>
<td>Modification to existing VistA Outpatient Pharmacy software</td>
<td><ol type="1">
<li><p>Install patch</p></li>
<li><p>Test functionality</p></li>
</ol></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Salt Lake City</td>
<td>Install Patch</td>
<td>Modification to existing VistA Outpatient Pharmacy software</td>
<td><ol type="1">
<li><p>Install patch</p></li>
<li><p>Test functionality</p></li>
</ol></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Grand Junction</td>
<td>Install Patch</td>
<td>Modification to existing VistA Outpatient Pharmacy software</td>
<td><ol type="1">
<li><p>Install patch</p></li>
<li><p>Test functionality</p></li>
</ol></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<span id="_Toc467501141" class="anchor"></span>Table 4: Facility-Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section summarizes resources related to the OneVA Pharmacy project.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for the OneVA Pharmacy deployment.

| Site       | Space/Room | Features Needed | Other |
|----------------|----------------|---------------------|-----------|
| Denver         | N/A            | Patch PSO\*7.0\*454 | None      |
| Salt Lake City | N/A            | Patch PSO\*7.0\*454 | None      |
| Grand Junction | N/A            | Patch PSO\*7.0\*454 | None      |

IOC Facility SpecificsThe table lists the specific information needed for the facilities that are participating in the IOC evaluation.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*454 is being released to enhance VistA’s “Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]” menu (found within the VistA Pharmacy Outpatient Pharmacy package). The OneVA Pharmacy patch will allow the Pharmacist to query for and refill patient’s active and refillable (non-controlled substance) prescriptions from other VA Pharmacy VistA instances. It will be deployed to all VA Pharmacy VistA instances nationwide. It results in an insignificant increase to the VistA/Pharmacy file storage requirements. It does not require additional hardware capabilities other than what is currently used by a VistA installation at other sites.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy VistA Patch PSO\*7.0\*454 has a dependency on patches PSO\*7.0\*444 and PSO\*7\*427.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Various communications about the OneVA Pharmacy initiative have taken place. They include:

- IOC site weekly conference call
- Integrated Project Team (IPT) & VA Stakeholder weekly conference call
- Clin 1 call- (Pharmacy Informaticists/ADPACs, Clinical Application Coordinators) Thursday 9/15/2016
- Pharmacy Chief’s call (VHA Pharmacy leadership) Call 10/5/2016
- Clin 1 call- (Pharmacy Informaticists/ADPACs, Clinical Application Coordinators) Thursday 10/20/2016
- Pharmacy Showcase (Pharmacists, Pharmacy Technicians, Clinical Application coordinators, Informaticists) Wednesday 10/26/2016
- VA Secretary Robert McDonald (who spoke about the capability at the Brookings Institution on June 20, 2016):

> *“VA is making it easier for Veterans on the road, away from their regular VA hospital, to receive care or refill their prescription at another VA facility.”*

#### Deployment/Installation/Back-Out Checklist

The OneVA Pharmacy Back-out instructions tested successfully during the OneVA Pharmacy Software Quality Assurance (SQA) testing. The following table lists the deployment and installation activities for National Rollout.

<span id="_Toc467501142" class="anchor"></span>Table 5: <span id="DeployInstallTable" class="anchor"></span>Deployment/Installation

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Activity</strong></th>
<th><strong>Day</strong></th>
<th><strong>Time</strong></th>
<th><strong>Individual who completed task</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>National Release Compliance: Installation to Test and Production in Off Position</td>
<td>11/30/16*- 12/15/16</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Region 1 Activations:</p>
<p>Primary Sites (2) *</p>
<p>Remaining Sites</p></td>
<td><p>12/05/16 – 12/06/16</p>
<p>12/07/16* – 12/21/16</p></td>
<td>Business Day</td>
<td>Region 1 VistA Support &amp; Pharm ADPAC</td>
</tr>
<tr class="odd">
<td><p>Region 2 Activations:</p>
<p>Primary Sites (5) *</p>
<p>Remaining Sites </p></td>
<td><p>12/07/16 – 12/13/16</p>
<p>01/03/17 – 01/13/17</p></td>
<td>Business Day</td>
<td>Region 2 VistA Support &amp; Pharm ADPAC</td>
</tr>
<tr class="even">
<td><p>Region 3 Activations:</p>
<p>Primary Sites (5) </p>
<p>Remaining Sites </p></td>
<td><p>12/16/16 – 12/22/16</p>
<p>01/17/17 – 01/27/17</p></td>
<td>Business Day</td>
<td>Region 3 VistA Support &amp; Pharm ADPAC</td>
</tr>
<tr class="odd">
<td><p>Region 4 Activations:</p>
<p>Primary Sites (5) </p>
<p>Remaining Sites </p></td>
<td><p>12/16/16 – 12/22/16</p>
<p>01/23/17 – 02/03/17</p></td>
<td>Business Day</td>
<td>Region 4 VistA Support &amp; Pharm ADPAC</td>
</tr>
</tbody>
</table>

\*Note: Start of site installations is dependent upon the receipt of the national change order approval.

\*Note: Region 1 and Region 2 Primary sites are being requested to accelerate national release compliance in order to accommodate automated testing.

\*Note: Region 1 remaining sites are being requested to accelerate national release compliance in order to begin activation immediately after automated testing of the primary sites.

\*\*Note: If automated testing is progressing ahead of schedule, region 3 and 4 primary sites may be requested to accelerate the 11/15/16 national release compliance.

 \*\*Note: If regions are progressing ahead of schedule, subsequent regions may be requested to accelerate activation and smoke testing.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy Patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This Patch should take less than 5 minutes to install. This is a VistA Patch therefore no additional system requirements are necessary.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The preferred method to obtain the OneVA Pharmacy Patch is to download the software by using File Transfer Protocol (FTP. The files are found on the following FTP site:. Sites may also elect to retrieve software directly from a specific server as follows:

<span class="mark">REDACTED</span>

OneVA Pharmacy documentation can be found on the VA Software Documentation Library at: <http://www4.va.gov/vdl/>.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy Patch is an enhancement to the enhance VistA’s “Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]” menu (found within the VistA Pharmacy Outpatient Pharmacy package). It will be deployed to all VA Pharmacy VistA instances nationwide by those Regional and Local Field Offices currently responsible for all VistA installations and support.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pso-7-454-oneva-pharmacy-installation-guide/007.png)The following are the OneVA Pharmacy Patch installation instructions to be followed by the IT support staff responsible for installing VistA Patches:

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the patch \# PSO\*7.0\*454:
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates. The backup transport global will allow a rollback to the prior version of the routines released in this patch in the event a rollback is required.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed.  It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//'
8.  When prompted for which Menu Options to disable, enter: 'PSO LM BACKDOOR ORDERS'.
9.  If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy Installation Verification Procedure will be made available by 10/24/2016 when the ePIP Deployment Plan is released. This section will be updated at this time.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy Flag activation switch is supplied in the configuration to allow sites to active or deactivate the OneVA Pharmacy Patch.

![](pso-7-454-oneva-pharmacy-installation-guide/008.png)DO NOT turn on the OneVA Pharmacy Flag until directed to do so. Please know, OneVA Pharmacy will be rolled out Nationally in in accordance to the schedule as outlined in ‘[Deployment/Installation’](#deploymentinstallationback-out-checklist) table of this document. The software will be released, deployed, and installed with the activation flag set to the “off” position. The Existing Product Intake Program (EPIP) Implementation Team will coordinate with the sites Pharmacy Automatic Data Processing Application Coordinator (ADPAC) on the specific date in which to activate the software.

![](pso-7-454-oneva-pharmacy-installation-guide/009.png)To use OneVA Pharmacy, the ‘OneVA Pharmacy Flag’ needs to be turned on. The 'OneVA Pharmacy Flag' field (#3001) has been added to the Outpatient Site file (#59). This field will allow each division to toggle the OneVA Pharmacy logic 'on' or 'off' depending on current needs. The field can be changed by using File Manager and editing the 'OneVA Pharmacy Flag' field. The ‘OneVA Pharmacy Flag’ will be delivered to each division in the 'off' state. When this flag is in the 'off' state, the HDR/CDS Repository will not be queried for external prescriptions and other VistA instances will not be able to refill prescriptions that belong to the VistA instance with the flag set to the 'off' state. When in the 'on' state, all prescription queries and actions may be taken for remote queries, refills, and partial fills. In order to process prescriptions from another VistA instance, that instance will also need to have its ‘OneVA Pharmacy Flag’ set to the 'on' state.

OneVA Pharmacy will not execute if the patient has only one entry in the VistA Treating Facility List file (#391.91).

### Host Site OneVA Pharmacy Flag Not Set On Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the ‘ONEVA PHARMACY FLAG (#3001)’ is not set to the ‘on’ state at the host site, the dispensing site will receive the following message:

> *The OneVA Pharmacy flag is turned ‘OFF’ at this facility. Unable to process refill/partial fill requests. Queries will NOT be made to other VA Pharmacy locations*.

### Steps to Turn On ONEVA PHARMACY FLAG (#3001)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pso-7-454-oneva-pharmacy-installation-guide/010.png)DO NOT turn on the OneVA Pharmacy Flag until directed to do so. Please know OneVA Pharmacy will be rolled out nationally in in accordance to the schedule as outlined in ‘[Deployment/Installation’](#DeployInstallTable) table. The software will be released, deployed, and installed with the activation flag set to the “off” position. The Existing Product Intake Program (EPIP) Implementation Team will coordinate with the sites Pharmacy Automatic Data Processing Application Coordinator (ADPAC) on the specific date in which to activate the software.

To turn on the ‘ONEVA PHARMACY FLAG (#3001)’ for all the divisions, use the ‘VA FILEMAN \[DIUSER\]’ utility and perform the following steps.

Sign-in to the VistA system and select the menu option: VA FILEMAN \[DIUSER\].

<span id="_Toc467501144" class="anchor"></span>Figure 2: OneVA Pharmacy Flag: VA FileMan

![](pso-7-454-oneva-pharmacy-installation-guide/011.png)

1.  Enter \<FM\> and press \<ENTER\>.

<span id="_Toc458500067" class="anchor"></span>Figure 3: OneVA Pharmacy Flag: Enter FM Prompt

![](pso-7-454-oneva-pharmacy-installation-guide/012.png)

The system displays the option name and the prompt for the specific FileMan feature, as displayed in the following image.

<span id="_Toc458500068" class="anchor"></span>Figure 4: OneVA Pharmacy Flag: VA FileMan Menu Prompt

![](pso-7-454-oneva-pharmacy-installation-guide/013.png)

2.  Enter \<EN\> and press \<ENTER\>.

<span id="_Toc458500069" class="anchor"></span>Figure 5: OneVA Pharmacy Flag: Enter \<EN\> to Enter or Edit File Entries Prompt

![](pso-7-454-oneva-pharmacy-installation-guide/014.png)

The system displays the option name and the prompt for the ‘INPUT TO WHAT FILE’, as displayed in the following image.

<span id="_Toc458500070" class="anchor"></span>Figure 6: OneVA Pharmacy Flag: Input to What File Prompt

![](pso-7-454-oneva-pharmacy-installation-guide/015.png)

3.  Enter \<59\> for the ‘OUTPATIENT SITE (#59)’ file and press \<ENTER\>.

The system displays the option name and the prompt for the ‘EDIT WHICH FILE’, as displayed in the following image.

<span id="_Toc458500071" class="anchor"></span>Figure 7: OneVA Pharmacy Flag: Edit Which Filed Prompt

![](pso-7-454-oneva-pharmacy-installation-guide/016.png)

4.  Enter \<3001\> for the ‘ONEVA PHARMACY FLAG (#3001)’ field and press \<ENTER\>.

The system displays the option name and the prompt for the ‘THEN EDIT FIELD’, as displayed in the following image.

<span id="_Toc458500072" class="anchor"></span>Figure 8: OneVA Pharmacy Flag: Then Edit Field Prompt

![](pso-7-454-oneva-pharmacy-installation-guide/017.png)

5.  Press \<ENTER\>.

The system displays the option name and the prompt for the specific ‘OUTPATIENT SITE NAME’, as displayed in the following image.

<span id="_Toc458500073" class="anchor"></span>Figure 9: OneVA Pharmacy Flag: Select OUTPATIENT SITE NAME Prompt

![](pso-7-454-oneva-pharmacy-installation-guide/018.png)

6.  Enter the following command \<^LOOP\> and press \<ENTER\>.

<span id="_Toc458500074" class="anchor"></span>Figure 10: OneVA Pharmacy Flag: ^LOOP Command

![](pso-7-454-oneva-pharmacy-installation-guide/019.png)

The system displays the option name and the prompt for the specific ‘EDIT ENTRIES BY: NAME//’, as displayed in the following image.

<span id="_Toc458500075" class="anchor"></span>Figure 11: OneVA Pharmacy Flag: Edit Entries by: NAME// Prompt

![](pso-7-454-oneva-pharmacy-installation-guide/020.png)

7.  Press \<ENTER\>.

The system displays the option name and the prompt for the specific ‘START WITH NAME: FIRST//’, as displayed in the following image.

<span id="_Toc458500076" class="anchor"></span>Figure 12: OneVA Pharmacy Flag: Start with Name Prompt

![](pso-7-454-oneva-pharmacy-installation-guide/021.png)

The ‘^LOOP’ command causes the system to display each division, one by one, allowing the user to set the ‘ON’ option for the ‘ONEVA PHARMACY FLAG’ for each division. After pressing the return key, the next division will display until the ‘LOOP ENDED!’ message displays.

8.  Enter \<ON\> for each division press \<ENTER\> as displayed in the example for a test VistA instance in the following image.

<span id="_Toc458500077" class="anchor"></span>Figure 13: OneVA Pharmacy Flag: Loop Command Example

![](pso-7-454-oneva-pharmacy-installation-guide/022.png)

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-out and Rollback plan for VistA applications is complex and not able to be a “one size fits all.” The general strategy for VistA back-out and rollback is to repair the code with a follow-on patch. However, the backup of the transport global when created as part of the install will allow the routines to be converted to the prior patch state. For OneVA Pharmacy this is sufficient to restore the code to prior functionality.

The development team recommends that sites log a Remedy ticket if it is a nationally released patch; otherwise, the site should contact the product development team directly for specific solutions to their unique problems.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy software can be “turned-off” in lieu of restoring the software to its prior state. Refer to the ‘[System Configuration](#system-configuration)’ section in this document for instructions.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OneVA Pharmacy User Acceptance Testing (UFT) was completed with no Severity Level 1 or Level 2 defects.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Failed smoke testing
- Non recoverable software error

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- None determined at this time.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Chief of Pharmacy Benefits Management

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the KIDS options, restore the software from the Backup Transport Global. However, in lieu of restoring the software, it is recommended to turn off the OneVA Pharmacy patch. A 'OneVA Pharmacy Flag' (field \#3001) has been added to the Outpatient Site file (#59). This field will allow each division to toggle the OneVA Pharmacy logic 'on' or 'off' depending on current needs. The field can be changed by using File Manager and editing the 'OneVA Pharmacy Flag' field. The ‘OneVA Pharmacy Flag’ will be delivered to each division in the 'off' state. When this flag is in the 'off' state, the HDR/CDS Repository will not be queried for external prescriptions and other VistA instances will not be able to refill prescriptions that belong to the VistA instance with the flag set to the ‘off’ state. When in the 'on' state, all prescription queries and actions may be taken for remote queries, refills, and partials. In order to process prescriptions from another VistA instance, that instance will also need to have its ‘OneVA Pharmacy Flag’ set to the 'on' state.

Refer to the ‘[System Configuration](#system-configuration)’ section in this document for instructions.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedures for this patch are the same as the back-out procedures.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the [Back-Out Procedure](#rollback-procedure) section of this document.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the [Back-Out Procedure](#rollback-procedure) section of this document.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risks of performing a Rollback of the OneVA Pharmacy may require a downtime of Pharmacy \> Outpatient Pharmacy Manager package/users.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Chief of Pharmacy Benefits Management must give the authority to Rollback the OneVA Pharmacy software.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the [Back-Out Procedure](#rollback-procedure) section of this document.