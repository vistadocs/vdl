---
consolidated_title: "inbound eprescribing installation guide"
app_code: PSO
doc_type: IG
master_source: "Inbound ePrescribing Installation Guide (PSO*7*617)"
master_pub_date: November 2021
consolidated_from: 2 versions
prior_versions:
  - "PSO*7*589 Inbound ePrescribing Installation Guide"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Outpatient Pharmacy

  Inbound ePrescribing Version 5.0

  Controlled Substance eRx

  VistA Patch \# PSO\*7.0\*617

  Installation Guide
---

![](inbound-eprescribing-installation-guide-pso-7-617/001.png)

November 2021

Office of Information and Technology (OI&T)

Revision History

| Date    | Version | Description      | Author   |
|---------|---------|------------------|----------|
| 10/2021 | 2.0     | Document Updates | REDACTED |
| 09/2021 | 1.0     | Initial Document | REDACTED |

Revision History showing date artifact was created or revised, version number, description, and author.
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
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
    - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [Back-out Plan](#back-out-plan)
    - [Patch Verification](#patch-verification)
  - [Post-Installation Instructions](#post-installation-instructions)
  - [Routine Information](#routine-information)
  - [Post-Installation Procedure](#post-installation-procedure)
    - [Coordination of Installation with Change Healthcare](#coordination-of-installation-with-change-healthcare)
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
This document describes how to deploy and install the Pharmacy Inbound ePrescribing (IEP) VistA Patch (PSO\*7.0\*617).
The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the IEP patch PSO\*7.0\*617 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*617 possesses a direct application dependency on the VistA Outpatient Pharmacy (OP) v.7.0 application. Patch PSO\*7\*52, PSO\*7\*557, PSO\*7\*568, PSO\*7\*631, and PSO\*7\*635 are required to be installed before PSO\*7.0\*617.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the roles and responsibilities for managing the deployment of the patch PSO\*7.0\*617.

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| <span class="mark">ID</span> | <span class="mark">Team</span>                                                                                                       | <span class="mark">Phase / Role</span> | <span class="mark">Tasks</span>                                                                                     | <span class="mark">Project Phase (See Schedule)</span> |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| 1                            | Field Operations (FO), Enterprise Operations (EO), or Enterprise Program Management Office (EPMO) (depending upon project ownership) | Deployment                             | Plan and schedule deployment (including orchestration with vendors)                                                 | Deployment                                             |
| 2                            | FO, EO, or EPMO (depending upon project ownership)                                                                                   | Deployment                             | Determine and document the roles and responsibilities of those involved in the deployment.                          | Design/Build                                           |
| 3                            | FO, or EO                                                                                                                            | Deployment                             | Test for operational readiness                                                                                      | Design/Build                                           |
| 4                            | FO or EO                                                                                                                             | Deployment                             | Execute deployment                                                                                                  | Design/Build                                           |
| 5                            | FO or EO                                                                                                                             | Installation                           | Plan and schedule installation                                                                                      | Deployment                                             |
| 6                            | Regional Project Manager (PM)/ Field Implementation Services (FIS)/ Office of Policy and Planning (OPP) PM                           | Installation                           | Ensure authority to operate and that certificate authority security documentation is in place                       | Design/Build                                           |
| 7                            | Regional PM/FIS/OPP PM/ Nat’l Education & Training                                                                                   | Installations                          | Coordinate training                                                                                                 | Deployment                                             |
| 8                            | FO, EO, or Product Development (depending upon project ownership)                                                                    | Back-out                               | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                                             |
| 9                            | FO, EO, or Product Development (depending upon project ownership)                                                                    | Post Deployment                        | Hardware, Software and System Support                                                                               | Maintenance                                            |

Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*617 enables sites to electronically receive and process Controlled Substance eRx prescriptions. Patch PSO\*7.0\*617 will be distributed via the FORUM Patch Module and may be deployed at any site without regard to deployment status at other sites.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for a period of thirty days, as depicted in the Master Deployment Schedule.

Table 2: Master Deployment Schedule

| VIP Build | Delivery Dates |
|-----------|----------------|
| N/A       |                |

Deployment Timeline table displays the VIP Build and delivery dates

### Deployment Topology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*617 will be released to all VistA sites.

![](inbound-eprescribing-installation-guide-pso-7-617/002.png)

Figure 1: Deployment Topology (Targeted Architecture)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During IOC testing, patch PSO\*7.0\*617 will be deployed at the following sites:

- VA Honolulu Regional Office
- Health Administration Center (Meds by Mail)
- Indianapolis, IN VA Medical Center
- Central Texas, Temple VA Medical Center Pharmacy
- Erie, PA VA Medical Center

PSO\*7.0\*617 will be delivered to the Information Technology (IT) support staff responsible for the VistA installation at those sites. The software will be installed in the IOC test and production environments.

After National Release, Patch PSO\*7.0\*617 will be deployed at all sites running the Outpatient Pharmacy v.7.0 application.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To prepare for the site, patch: Patch PSO\*7\*52, PSO\*7\*557, PSO\*7\*568, PSO\*7\*631, and PSO\*7\*635 are required to be installed before PSO\*7.0\*617.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment of Patch PSO\*7.0\*617 requires an up to date VistA environment running the Outpatient Pharmacy v.7.0 application, as well as designated IT support available to perform the patch installation.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific deployment or installation features of patch PSO\*7\*617.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*617 is being released to enhance VistA’s Pharmacy Outpatient Pharmacy package. The patch allows the VA to receive prescriptions from external providers and allows the pharmacist to validate the prescription for final processing and dispensing in existing VistA functionality. It will be deployed to all VA pharmacy VistA sites nationwide.

It does not require additional hardware capabilities other than what is currently used by a VistA installation at the sites.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

Table 3: Software Specifications

| Required Software   | Make | Version | Configuration | Manufacturer | Other |
|---------------------|------|---------|---------------|--------------|-------|
| Outpatient Pharmacy |      | 7.0     | Standard      | VHA          |       |

Software Specifications

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No notifications are required for deployment of patch PSO\*7.0\*617 other than the patch description released through Forum.

#### Deployment/Installation/Back-Out Checklist

Sites should fill out the table below indicating who performed an activity and when it was performed prior to installation.

Table 4: Deployment/Installation/Back-Out Checklist

| Activity                                                                                                                         | Day | Time | Individual who completed task |
|----------------------------------------------------------------------------------------------------------------------------------|-----|------|-------------------------------|
| Deploy -The Deploy activity is performed when the patch is sent to site(s) by the National Patch Module or Release Agent.        |     |      |                               |
| Install - The Install activity is performed when the patch is installed at the site(s).                                          |     |      |                               |
| Back-Out - The optional Back-Out activity is performed in the event the patch must be uninstalled, or removed, from the site(s). |     |      |                               |

Deployment/Installation/Back-Out ChecklistDeployment/Installation/Back-Out Checklist

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the National VA Network and to the local network of each site to receive patch PSO\*7.0\*617 is required to perform the installation, as well as the authority to install patches.

### Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A post-installation routine will be executed right after the patch installation to add new HOLD, REMOVE and REJECT codes to the ERX SERVICE REASON CODES file (#52.45).

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*617 does not require any platform installation or preparation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*617 is being released as a FORUM Patch message, which will be sent to the G.PATCHES mail group.

The documentation, described in the table below, will be in the form of Adobe Acrobat files. Documentation can be found on the VA Software Documentation Library at: <http://www.va.gov/vdl/>. Documentation can also be found at [<u>REDACTED</u>](https://download.vista.med.va.gov/index.html/SOFTWARE).

Table 5: Installation Documentation

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 34%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Title</th>
<th>File Name</th>
<th>FTP Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Installation Guide - Inbound ePrescribing (PSO*7.0*617)</td>
<td><p>PSO_7_0_P617_IG.docx</p>
<p>PSO_7_0_P617_IG.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>User Manual – Inbound ePrescribing (PSO*7.0*617)</td>
<td><p>PSO_7_0_P617_UM_1_2.docx</p>
<p>PSO_7_0_P617_UM_1_2.pdf</p>
<p>PSO_7_0_P617_UM_31.docx</p>
<p>PSO_7_0_P617_UM_31.pdf</p>
<p>PSO_7_0_P617_UM_32.docx</p>
<p>PSO_7_0_P617_UM_32.pdf</p>
<p>PSO_7_0_P617_UM_41.docx</p>
<p>PSO_7_0_P617_UM_41.pdf</p>
<p>PSO_7_0_P617_UM_42.docx</p>
<p>PSO_7_0_P617_UM_42.pdf</p>
<p>PSO_7_0_P617_UM_51.docx</p>
<p>PSO_7_0_P617_UM_51.pdf</p>
<p>PSO_7_0_P617_UM_52.docx</p>
<p>PSO_7_0_P617_UM_52.pdf</p>
<p>PSO_7_0_P617_UM_6.docx</p>
<p>PSO_7_0_P617_UM_6.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>Technical Manual/Security Guide - Outpatient Pharmacy V.7.0</td>
<td><p>PSO_7_0_P617_TM.docx</p>
<p>PSO_7_0_P617_TM.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td><span id="_Toc84505186" class="anchor"></span>Release Notes – CS Inbound ePrescribing (PSO*7.0*617)</td>
<td><p>PSO_7_0_P617_RN.docx</p>
<p>PSO_7_0_P617_RN.pdf</p></td>
<td>Binary</td>
</tr>
</tbody>
</table>

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new database is required for the patch PSO\*7.0\*617.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are required for installation of patch PSO\*7.0\*617.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are required for installation of patch PSO\*7.0\*617.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the National VA Network and to the local network of each site to receive patch PSO\*7.0\*617 is required to perform the installation, as well as the authority to install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install. Users may NOT be on the system during the install of PSO\*7\*617. It is recommended that this patch be installed during non-peak hours.

> **NOTE:** These backup files may get as large as 150 kilobytes. Make sure space is available before proceeding. Creating the backup files should take from 0 to 2 minutes to create backup files.

1)  Distribution Load:

    Load the KIDS Distribution from the Packman Message using the Packman function "Install/Check Message."
2)  From the Kernel Installation and Distribution System Menu, select

> the Installation Menu. From this menu, you may elect to use the

> following options. When prompted for the INSTALL NAME enter:

> PSO\*7.0\*617

1.  Backup a Transport Global - This option will create a backup build of patch

    components. Respond “BUILD” at the “Select one of the following: B

> Build or R Routines” prompt. \*\*THIS IS CRITICAL TO ACCURATE PATCH

> BACKUP ON YOUR SYSTEM. \*\*

2.  Compare Transport Global to Current System - This option will allow you to view all

    changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the

    integrity of the routines that are in the transport global.
3)  KIDS Installation:
    1.  Install the patch using the KIDS Installation Menu action

        "Install Package(s)" and the install name PSO\*7.0\*617.
2.  Respond "NO" at the "Want KIDS to INHIBIT LOGONs during the install?" prompt.
3.  Respond "YES" at the "Want to DISABLE Scheduled Options,

    Menu Options, and Protocols?" prompt. Choose option \[PSO ERX FINISH
4.  The KIDs install should take less than 1 minute.

### Back-out Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back-out data from a production account could cause broken pointers, \<UNDEFINED\> errors and hard MUMPS crashes. The back-out plan for data only patches is to report your findings and wait for a repair patch. Contact Help desk to log a ticket.

### Patch Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Installation & Distribution System-\> Utilities-\> Install. File Print option can be used to check for any errors plus the status of the install being Completed.

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are additional steps to be completed in order to finalize installation of this patch. Please see Post Installation Procedure below in section 4.11.

## Routine Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second line of each of these routines now looks like:

;;7.0;OUTPATIENT PHARMACY;\*\*\[Patch List\]\*\*;DEC 1997;Build 121

The checksums below are new checksums, an can be checked with CHECK1^XTSUMBLD.

Routine Name: PSO617PI

Before: n/a After: B4936072 \*\*617\*\*

Routine Name: PSOCMOPR

Before: B51028555 After: B54050720 \*\*33,52,617\*\*

Routine Name: PSODISP1

Before: B49194938 After: B52176319 \*\*15,9,33,391,617\*\*

Routine Name: PSOERX

Before:B135510353 After:B144901593 \*\*467,527,508,551,567,591,581,617\*\*

Routine Name: PSOERX1

Before:B170801530 After: B1264803 \*\*467,520,527,508,551,581,635,617\*\*

Routine Name: PSOERX1A

Before:B175273948 After:B210939178 \*\*467,527,508,551,581,617\*\*

Routine Name: PSOERX1B

Before:B148682031 After:B156836740 \*\*467,506,520,527,508,551,591,

606,581,617\*\*

Routine Name: PSOERX1C

Before:B113785814 After:B114573841 \*\*467,520,527,508,551,581,617\*\*

Routine Name: PSOERX1D

Before:B217653722 After:B218498146 \*\*581,617\*\*

Routine Name: PSOERX1F

Before: n/a After:B156911552 \*\*617\*\*

Routine Name: PSOERX1G

Before: n/a After:B180972623 \*\*617\*\*

Routine Name: PSOERXA0

Before: B33354450 After: B33174587 \*\*467,586,617\*\*

Routine Name: PSOERXA1

Before:B191218900 After:B135172284 \*\*467,520,508,551,581,617\*\*

Routine Name: PSOERXA3

Before: B38164072 After: B96572503 \*\*467,508,617\*\*

Routine Name: PSOERXA5

Before: B71429258 After: B71430254 \*\*508,581,631,617\*\*

Routine Name: PSOERXAU

Before: n/a After: B49335870 \*\*617\*\*

Routine Name: PSOERXC1

Before:B109912416 After:B116832004 \*\*508,551,567,581,631,617\*\*

Routine Name: PSOERXD1

Before:B164705003 After:B165709901 \*\*467,520,551,582,581,635,617\*\*

Routine Name: PSOERXD2

Before:B164315173 After:B183851354 \*\*467,506,520,508,551,581,617\*\*

Routine Name: PSOERXEN

Before: B16386315 After: B22111033 \*\*508,581,617\*\*

Routine Name: PSOERXH1

Before: B36800437 After: B37438342 \*\*467,527,508,581,617\*\*

Routine Name: PSOERXI1

Before:B156967276 After:B182379733 \*\*581,617\*\*

Routine Name: PSOERXIE

Before:B158461983 After:B160758654 \*\*581,617\*\*

Routine Name: PSOERXO1

Before:B177621724 After:B177622161 \*\*467,520,508,581,617\*\*

Routine Name: PSOERXOA

Before: B77421182 After: B77421421 \*\*581,617\*\*

Routine Name: PSOERXU1

Before:B157028111 After:B167891410 \*\*467,520,508,551,565,581,617\*\*

Routine Name: PSOERXU2

Before: B61501050 After: B53578392 \*\*508,598,581,631,617\*\*

Routine Name: PSOERXU3

Before:B187651757 After:B187964099 \*\*508,591,606,581,617\*\*

Routine Name: PSOERXU4

Before: B72569032 After: B78849793 \*\*520,508,551,581,635,617\*\*

Routine Name: PSOERXU6

Before:B120600986 After:B123957779 \*\*508,551,581,631,617\*\*

Routine Name: PSOERXU7

Before: B44585380 After: B44861191 \*\*581,617\*\*

Routine Name: PSOERXU8

Before: B10018931 After: B16430599 \*\*581,617\*\*

Routine Name: PSOERXU9

Before: n/a After: B30267841 \*\*617\*\*

Routine Name: PSOERXUT

Before: n/a After: B58611194 \*\*617\*\*

Routine Name: PSOERXX1

Before:B174429887 After:B173990318 \*\*467,520,527,508,581,617\*\*

Routine Name: PSOORFI1

Before: B86566158 After: B92874767 \*\*7,15,23,27,32,44,51,46,71,

90,108,131,152,186,210,222,258,

260,225,391,408,444,467,505,

617\*\*

Routine Name: PSOORFI5

Before: B77628062 After: B79004074 \*\*225,315,266,391,372,416,504,

505,557,617\*\*

Routine Name: PSOORNEW

Before:B124801369 After:B129961468 \*\*11,23,27,32,55,46,71,90,94,

106,131,133,143,237,222,258,

206,225,251,386,390,391,372,

416,431,313,408,436,411,444,

486,446,505,517,508,457,581,

617\*\*

Routine list of preceding patches: 52, 557, 586, 631, 635

## Post-Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are additional steps to be completed to finish patch PSO\*7\*617 install and implementation at your site.

### Coordination of Installation with Change Healthcare

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please contact Inbound eRx implementation group, InboundeRx@va.gov, to finalize coordination of installation with Change Healthcare.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning is required before or after deployment of PSO\*7.0\*617.

![](inbound-eprescribing-installation-guide-pso-7-617/003.png)

> **NOTE:** Installation of PSO\*7.0\*617 is completed. The following procedure is to be followed only if PSO\*7.0\*617 needs to be backed out.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the NSD at 855-NSD-HELP (673-4357) and reference “Inbound eRx” to submit a YourIT ServiceNow ticket; the development team will assist with the process.

The Back-out Procedure consists of restoring the routines and removing the Data Dictionaries (DD) introduced by the Patch PSO\*7.0\*617.

The rollback/backout procedure for these patches should only occur when there is concurrence from the Enterprise Product Support and Inbound ePrescribing development teams, because of the complexity and risk involved in a rollback/backout. Normal installation back-ups using KIDS will back up only Mumps routines. For all non-routine components of these builds, Enterprise Product Support will have a build available if needed. Make sure the ‘Backup a Transport Global’ step in section 4.8 of this document is followed, so you do have a backup of all the routines if needed.

The back-out is to be performed by persons with programmer-level access.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-out Strategy is to manually delete the new Data Definitions (DDs) introduced with this patch.

The Back-out and Rollback plan for VistA applications is complex and not able to be a “one size fits all.” The general strategy for VistA back-out and rollback is to repair the code with a follow-on patch. However, the backup of the transport global when created as part of the install will allow the routines to be converted to the prior patch state. For IEP, this is sufficient to restore the code to prior functionality.

The development team recommends that sites log a help desk ticket if it is a nationally released patch; otherwise, the site should contact the product development team directly for specific solutions to their unique problems.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out should only be done in the event that the local facility management determines that the Patch PSO\*7.0\*617 is not appropriate for that facility and should only be done as a last resort.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch PSO\*7.0\*617.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Initial Operating Capabilities (IOC) Testing for patch PSO\*7.0\*617 occurred from August 01, 2021 to September 15, 2021.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Facility Management would need to determine patch PSO\*7.0\*617 is not appropriate for their facility.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out PSO\*7.0\*617, the local facility will not be able to use the IEP functionality to validate and process Inbound ePrescriptions (eR<sub>x</sub>es) from external providers.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Facility Management has the authority to back-out patch PSO\*7.0\*617.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the complexity of this patch, it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) at 855-NSD-HELP (673-4357) and reference “Inbound eR<sub>X</sub>” to submit a YourIT ServiceNow ticket; the development team will assist with the process.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedures for this patch are the same as the back-out procedures.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the [Back-Out Procedure](#back-out-procedure) section of this document.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the [Back-Out Procedure](#back-out-procedure) section of this document.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risks of performing a rollback include the downtime of not validating and processing eR<sub>X</sub>es received from external providers.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The chief of Pharmacy Benefits Management (PBM) must provide the authority to roll back patch PSO\*7.0\*617.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the [Back-Out Procedure](#back-out-procedure) section of this document.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSO*7*589 Inbound ePrescribing Installation Guide

## Pre-installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to section 4.1 Pre-installation and System Requirements for pre-installation instructions.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
