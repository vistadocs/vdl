---
consolidated_title: "inbound eprescribing implementation guide"
app_code: PSO
doc_type: IG-IMP
master_source: "Inbound ePrescribing Implementation Guide (PSO*7*581)"
master_pub_date: January 2021
consolidated_from: 2 versions
prior_versions:
  - "Inbound ePrescribing Implementation Guide (PSO*7*635)"
---

Pharmacy Reengineering (PRE)

Inbound ePrescribing Version 4.0

VistA Patch \# PSO\*7.0\*581

Installation Guide

![](inbound-eprescribing-implementation-guide-pso-7-581/001.png)

January 2021

Office of Information and Technology (OI&T)

Revision History

<table>
<caption>Revision History showing date artifact was created or revised, version number, description, and author.</caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 47%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01/2021</td>
<td>1.5</td>
<td>Updated PSOERX01 Checksum to match value in Patch Description (<a href="#RoutineInfo">pg12</a>)</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>12/2020</td>
<td>1.4</td>
<td>Updated section 4.1.1 with Change Healthcare coordination (<a href="#prepost-installation-overview">pg6</a>), Added section 4.11.2 for contact support for Change Healthcare coordination <a href="#coordination-of-installation-with-change-healthcare">(pg15</a>),Updated section 4.8 Installation Procedure (<a href="#installation-procedure">pg8</a>) , Updated section 4.10 with PSO*7.O*581-T12 Routine information (<a href="#RoutineInfo">pg10</a>), Updated section 4.9 reference to section 4.11 (<a href="\l">pg11</a>); Updated section 4.11 text (<a href="#post-installation-procedure">pg14)</a>; Updated section 5.6 SNow reference (<a href="#back-out-procedure-1">pg17</a>).</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>12/2020</td>
<td>1.3</td>
<td>Updated section 4.10 Routine Information (<a href="#post-installation-procedure">pg10</a>); Updated section 4.9 Post Installation Instructions (<a href="#RoutineInfo">pg10</a>); Updated section 4.8 Installation instructions to match PD, Updated section 4.8 remove redundant text (<a href="#installation-procedure">pg8</a>); Updated Section 4.11.1 section heading, Added additional steps to section 4.11.1 (<a href="#ConfigWeb">pg14</a>); Updated section 4.1 and deleted section 4.1.2 (<a href="\l">pg6</a>)</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>12/2020</td>
<td>1.2</td>
<td>Updated section 4.1.1 with reference to Installation steps (<a href="#prepost-installation-overview">pg6</a>); Added section 4.10.1 Configure Web Server Entry (<a href="\l">pg14)</a></td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>12/2020</td>
<td>1.1</td>
<td>Deleted DIRB reference (<a href="#_Hlk57204759">pg7</a>); Updated Section 4.8 KIDS Installation (<a href="\l">pg9</a>)</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>12/2020</td>
<td>1.0</td>
<td><p>Updated <a href="#_Hlk51761109">Section 1.1</a> on patch dependencies</p>
<p>Updated <a href="#p2">Section 3.1</a>, <a href="#site-information-locations-deployment-recipients">Section 3.1.2,</a> <a href="#site-preparation">Section 3.1.3</a>, <a href="#p43">Section 4.3</a>, <a href="#installation-procedure">Section 4.9</a>, and Section <a href="#_Hlk57204759">4.10</a></p></td>
<td>Technatomy</td>
</tr>
</tbody>
</table>

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
    - [Configure Web Server Entry Needed for PSO\7\581](#configure-web-server-entry-needed-for-pso7581)
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
This document describes how to deploy and install the Pharmacy Reengineering (PRE) Inbound ePrescribing (IEP) VistA Patch (PSO\*7.0\*581).
The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the IEP patch PSO\*7.0\*581 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*581 possesses a direct application dependency on the VistA Outpatient Pharmacy (OP) v.7.0 application. <span id="_Hlk51761109" class="anchor"></span>Patch PSO\*7\*457, PSO\*7\*508, PSO\*7\*527, PSO\*7\*551, PSO\*7\*565, PSO\*7\*567, PSO\*7\*582, PSO\*7\*591, PSO\*7\*598, and PSO\*7\*606 are required to be installed before PSO\*7.0\*581.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Pre-installation routine exists that will load new file entries for the

ERX SERVICE REASON CODES file (#52.45). The number of codes are large

enough that it will require the installer to use GIGEN^%ZSPECIAL to load a

.GBL file which contains a temp global.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the roles and responsibilities for managing the deployment of the patch PSO\*7.0\*581.

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

Patch PSO\*7.0\*581 addresses workflow concerns during the creation of an eR<sub>X</sub>, resolves formatting issues, and corrects the locking functionality of the Inbound eR<sub>X</sub> software. Patch PSO\*7.0\*581 will be distributed via the FORUM Patch Module and may be deployed at any site without regard to deployment status at other sites.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for a period of thirty days, as depicted in the Master Deployment Schedule.

Table 2: Master Deployment Schedule

| <span id="p2" class="anchor"></span>VIP Build                   | Delivery Dates    |
|-----------------------------------------------------------------|-------------------|
| VIP Build 1 - NewRx and Cancel Rx Request/Response              | 09/23/19-12/20/19 |
| VIP Build 2 - RxRenewal Request/Response                        | 12/23/19-04/10/20 |
| VIP Build 3 - RxChange / Rational Migration                     | 03/23/20-06/12/20 |
| VIP Build 4 - RxChange / Rational Migration                     | 06/15/20-09/04/20 |
| VIP Build 5 - Regression Testing, Bug fixes, Certification Test | 09/08/20-10/16/20 |
| IOC Preparation and Testing                                     | 10/19/20-12/10/20 |

Deployment Timeline table displays the VIP Build and delivery dates

### Deployment Topology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*581 will be released to all VistA sites.

![](inbound-eprescribing-implementation-guide-pso-7-581/002.png)

Figure 1: Deployment Topology (Targeted Architecture)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During IOC testing, patch PSO\*7.0\*581 will be deployed at the following sites:

- VA Honolulu Regional Office
- Fayetteville VAMC Veterans Health Care System of the Ozarks
- Health Administration Center (Meds by Mail)
- Indianapolis, IN VA Medical Center

PSO\*7.0\*581 will be delivered to the Information Technology (IT) support staff responsible for the VistA installation at those sites. The software will be installed in the IOC test and production environments.

After National Release, Patch PSO\*7.0\*581 will be deployed at all sites running the Outpatient Pharmacy v.7.0 application.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To prepare for the site, patch: Patch PSO\*7\*457, Patch PSO\*7\*508, PSO\*7\*527, PSO\*7\*551, PSO\*7\*565, PSO\*7\*567, PSO\*7\*582, PSO\*7\*591, PSO\*7\*598, and PSO\*7\*606 required to be installed before PSO\*7.0\*581.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment of Patch PSO\*7.0\*581 requires an up to date VistA environment running the Outpatient Pharmacy v.7.0 application, as well as designated IT support available to perform the patch installation.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific deployment or installation features of patch PSO\*7\*581.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*581 is being released to enhance VistA’s Pharmacy Outpatient Pharmacy package. The patch allows the VA to receive prescriptions from external providers and allows the pharmacist to validate the prescription for final processing and dispensing in existing VistA functionality. It will be deployed to all VA pharmacy VistA sites nationwide.

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

No notifications are required for deployment of patch PSO\*7.0\*581 other than the patch description released through Forum.

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

Access to the National VA Network and to the local network of each site to receive patch PSO\*7.0\*581 is required to perform the installation, as well as the authority to install patches.

### Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A pre-installation routine exists that will load new file entries for the ERX SERVICE REASON CODES file (#52.45). The number of codes are large enough that it will require the installer to use D GIGEN^%ZSPECIAL to load a .GBL file which contains a temp global.

There is additional action needed to configure the web service changes for complete installation of this patch. These changes are critical to ensure new functionality additions and seamless communication of Inbound eRx prescriptions to your medical center.

Prior to installation, please contact Inbound eRx implementation group, InboundeRx@va.gov, to finalize coordination of installation with Change Healthcare.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7.0\*581 does not require any platform installation or preparation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="p43" class="anchor"></span>Patch PSO\*7\*581 is being released as a FORUM Patch message, which will be sent to the G.PATCHES mail group. This patch also has a supporting .GBL data file.

The supporting data file is available at the following location:

/srv/vista/patches/SOFTWARE/PSO_7_581.GBL

File Name Contents FTP Mode

----------------- ---------- ---------

PSO_7_581.GBL PSO\*7\*581 GLOBAL ASCII

The documentation, described in the table below, will be in the form of Adobe Acrobat files. Documentation can be found on the VA Software Documentation Library at: <http://www.va.gov/vdl/>. <span id="_Hlk57204759" class="anchor"></span>Documentation can also be found at [<u>https://download.vista.med.va.gov/index.html/SOFTWARE</u>](https://download.vista.med.va.gov/index.html/SOFTWARE).

Table 5: Installation Documentation

| Title                                                       | File Name            | FTP Mode |
|-------------------------------------------------------------|----------------------|----------|
| Installation Guide - Inbound ePrescribing (PSO\*7.0\*581)   | PSO_7_0_P581_ig.pdf  | Binary   |
| User Manual – Inbound ePrescribing (PSO\*7.0\*581)          | PSO_7_0_P581_um.pdf  | Binary   |
| Release Notes - Inbound ePrescribing (PSO\*7.0\*581)        | PSO_7_0_P581_rn.pdf  | Binary   |
| Technical Manual/Security Guide - Outpatient Pharmacy V.7.0 | PSO_7_0_P581_tm.pdf  | Binary   |
| Implementation Guide - Inbound ePrescribing (PSO\*7.0\*581) | PSO_7_0_P581_img.pdf | Binary   |

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new database is required for the patch PSO\*7.0\*581.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are required for installation of patch PSO\*7.0\*581.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are required for installation of patch PSO\*7.0\*581.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the National VA Network and to the local network of each site to receive patch PSO\*7.0\*581 is required to perform the installation, as well as the authority to install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

Option \[PSO ERX FINISH\] should be marked out of order during installation of PSO\*7.0\*581.

1)  Users may be on the system during the install of PSO\*7\*581. It is recommended that this patch be installed during non-peak hours. This patch should take from 1 to 3 minutes to install depending on the system.

    Create a backup 1-2 minutes

    Load the Global 1-2 minute

    Kids Install 1-3 minutes
2)  Size/Disk Space Requirements:
- The changes to the ERX service reason codes file will be less than 200 kilobytes.
3)  Create a backup of the following global files before continuing:
- ERX SERVICE REASON CODES \#52.45 ^PS(52.45

> **NOTE:** These backup files may get as large as 150 kilobytes. Make sure space is available before proceeding. Creating the backup files should take from 0 to 2 minutes to create backup files.

When you are creating a backup of a subscripted global, you are saving a partial global (a file

within a global). You should use the utility GOGEN^%ZSPECIAL, and when prompted for

a global, enter the open global reference as shown below.

Example:

Enter To create a Backup copy of:

------- ----------------------------------

^PS(52.45, ERX SERVICE REASON CODES

4)  Install the data from the global host file PSO_7_581.GBL. This file contains the eRx

    service codes import global ^TMP("PSO581PO").

> **NOTE:** This global is approximately 150 kilobytes in size. Make sure there is sufficient space available to load this global on your system. The loading of the global should take less than one minute.

From the Programmer prompt, execute the following routine:

\>D GIGEN^%ZSPECIAL

Global input

Device: /filepath/PSO_7_581.GBL

Parameter: RS=\>

If you receive the following prompt, respond with 'Y'.

Transfer entire set of files? No=\> Y

Input option: A ^TMP("PSO581PO")

5)  Set up user and IO variables (D ^XUP) for programmer access.
6)  Distribution Load:

    Load the KIDS Distribution from the Packman Message using the Packman function "Install/Check Message."
7)  From the Kernel Installation and Distribution System Menu, select

> the Installation Menu. From this menu, you may elect to use the

> following options. When prompted for the INSTALL NAME enter:

> PSO\*7.0\*581

1.  Backup a Transport Global - This option will create a backup build of patch

    components. Respond “BUILD” at the “Select one of the following: B

> Build or R Routines” prompt. \*\*THIS IS CRITICAL TO ACCURATE PATCH

> BACKUP ON YOUR SYSTEM. \*\*

2.  Compare Transport Global to Current System - This option will allow you to view all

    changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the

    integrity of the routines that are in the transport global.
8)  KIDS Installation:
    1.  Install the patch using the KIDS Installation Menu action

        "Install Package(s)" and the install name PSO\*7.0\*581.
2.  Respond "NO" at the "Want KIDS to INHIBIT LOGONs during the install?" prompt.
3.  Respond "YES" at the "Want to DISABLE Scheduled Options,

    Menu Options, and Protocols?" prompt. Choose option \[PSO ERX FINISH
4.  The KIDs install should take less than 1 minute.
9)  Cleanup
1)  The Post-Install routine PSO581PO should be deleted using the KERNEL option 'Delete Routines' \[XTRDEL\] upon completion of the installation.

> **NOTE:** The installation of this patch should trigger an update protocol and may spawn background tasks for the Clinical Reminders or Consult packages. You do not need to wait for these background jobs to complete to delete the Environment Check and Post-Install routines.

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

Routine Name: PSO581EN

Before: n/a After: B538156 \*\*581\*\*

Routine Name: PSO581PO

Before: n/a After: B28129273 \*\*581\*\*

Routine Name: PSOERX

Before:B134630031 After:B135510353 \*\*467,527,508,551,567,591,581\*\*

Routine Name: PSOERX1

Before: B99497004 After:B169020138 \*\*467,520,527,508,551,581\*\*

Routine Name: PSOERX1A

Before:B150463790 After:B175273948 \*\*467,527,508,551,581\*\*

Routine Name: PSOERX1B

Before:B185624398 After:B148682031 \*\*467,506,520,527,508,551,591,

606,581\*\*

Routine Name: PSOERX1C

Before: B64623473 After:B113785814 \*\*467,520,527,508,551,581\*\*

Routine Name: PSOERX1D

Before: n/a After:B217653722 \*\*581\*\*

Routine Name: PSOERX1E

Before: n/a After: B1908867 \*\*581\*\*

Routine Name: PSOERXA1

Before:B188036698 After:B191218900 \*\*467,520,508,551,581\*\*

Routine Name: PSOERXA5

Before: B65388361 After: B67783943 \*\*508,581\*\*

Routine Name: PSOERXA6

Before: n/a After: B60070780 \*\*581\*\*

Routine Name: PSOERXC1

Before:B106890934 After:B106435535 \*\*508,551,567,581\*\*

Routine Name: PSOERXD1

Before:B131735326 After:B142880201 \*\*467,520,551,582,581\*\*

Routine Name: PSOERXD2

Before:B183875290 After:B164315173 \*\*467,506,520,508,551,581\*\*

Routine Name: PSOERXEN

Before: B15625365 After: B16386315 \*\*508,581\*\*

Routine Name: PSOERXH1

Before: B17222601 After: B36800437 \*\*467,527,508,581\*\*

Routine Name: PSOERXI1

Before: n/a After:B156967276 \*\*581\*\*

Routine Name: PSOERXIA

Before: n/a After: B81005829 \*\*581\*\*

Routine Name: PSOERXIB

Before: n/a After: B57255225 \*\*581\*\*

Routine Name: PSOERXIC

Before: n/a After: B14137332 \*\*581\*\*

Routine Name: PSOERXID

Before: n/a After: B88864726 \*\*581\*\*

Routine Name: PSOERXIE

Before: n/a After:B158461983 \*\*581\*\*

Routine Name: PSOERXIF

Before: n/a After:B151624775 \*\*581\*\*

Routine Name: PSOERXIG

Before: n/a After:B148255571 \*\*581\*\*

Routine Name: PSOERXIH

Before: n/a After: B56027681 \*\*581\*\*

Routine Name: PSOERXII

Before: n/a After: B46614130 \*\*581\*\*

Routine Name: PSOERXIU

Before: n/a After: B15943170 \*\*581\*\*

<span id="RoutineInfo" class="anchor"></span>Routine Name: PSOERXO1

Before:B115835250 After:B177621724 \*\*467,520,508,581\*\*

Routine Name: PSOERXOA

Before: n/a After: B77421182 \*\*581\*\*

Routine Name: PSOERXOB

Before: n/a After: B66413086 \*\*581\*\*

Routine Name: PSOERXOC

Before: n/a After: B42735501 \*\*581\*\*

Routine Name: PSOERXOD

Before: n/a After: B54001451 \*\*581\*\*

Routine Name: PSOERXOE

Before: n/a After: B31609262 \*\*581\*\*

Routine Name: PSOERXOF

Before: n/a After: B18714201 \*\*581\*\*

Routine Name: PSOERXOG

Before: n/a After: B63703408 \*\*581\*\*

Routine Name: PSOERXOH

Before: n/a After: B16534499 \*\*581\*\*

Routine Name: PSOERXOI

Before: n/a After: B19896023 \*\*581\*\*

Routine Name: PSOERXOJ

Before: n/a After: B37952226 \*\*581\*\*

Routine Name: PSOERXOK

Before: n/a After: B55804980 \*\*581\*\*

Routine Name: PSOERXOL

Before: n/a After: B66259682 \*\*581\*\*

Routine Name: PSOERXOM

Before: n/a After:B121574740 \*\*581\*\*

Routine Name: PSOERXON

Before: n/a After:B116135344 \*\*581\*\*

Routine Name: PSOERXOU

Before: n/a After: B11448528 \*\*581\*\*

Routine Name: PSOERXP1

Before: B28678984 After: B28700221 \*\*467,520,527,551,581\*\*

Routine Name: PSOERXR1

Before: B33604868 After: B32193647 \*\*467,520,527,581\*\*

Routine Name: PSOERXU1

Before:B153595246 After:B157028111 \*\*467,520,508,551,565,581\*\*

Routine Name: PSOERXU2

Before: B56457252 After: B61412991 \*\*508,598,581\*\*

Routine Name: PSOERXU3

Before:B169980946 After:B187651757 \*\*508,591,606,581\*\*

Routine Name: PSOERXU4

Before: B68679574 After: B69312142 \*\*520,508,551,581\*\*

Routine Name: PSOERXU5

Before: B64488961 After:B149296453 \*\*508,581\*\*

Routine Name: PSOERXU6

Before:B117656460 After:B120358979 \*\*508,551,581\*\*

Routine Name: PSOERXU7

Before: n/a After: B44585380 \*\*581\*\*

Routine Name: PSOERXU8

Before: n/a After: B10018931 \*\*581\*\*

Routine Name: PSOERXX1

Before:B155540262 After:B174429887 \*\*467,520,527,508,581\*\*

Routine Name: PSOERXX2

Before:B185958519 After:B182775958 \*\*467,508,581\*\*

Routine Name: PSOORNEW

Before:B119452733 After:B124801369 \*\*11,23,27,32,55,46,71,90,94,

106,131,133,143,237,222,258,

206,225,251,386,390,391,372,

416,431,313,408,436,411,444,

486,446,505,517,508,457,581\*\*

Routine list of preceding patches: 457, 565, 582, 598, 606

## Post-Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are additional steps to be completed to finish patch 581 install and implementation at your site.

### Configure Web Server Entry Needed for PSO\*7\*581

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="ConfigWeb" class="anchor"></span>Identify the FQDN, PORT, USERNAME/PASSWORD for the Web Server and Edit the Web Server Entry

> **NOTE:** To obtain the information needed for configuring the Web Server Entry, submit a help desk ticket to the VA National Service Desk (NSD) at 855-NSD-HELP (673-4357) and reference “Inbound eRx to submit a YourIT ServiceNow ticket” . The ticket will be routed to an IEP Administrator for assistance.

1.  Select option XOBW WEB SERVER MANAGER.
1.  Choose ‘ES’ for Edit Server.
2.  When prompted ‘NAME’ enter ‘PSO WEB SERVER’.
3.  When prompted ‘SERVER:’, enter the FQDN of the target server.
4.  When prompted ‘PORT:’, enter the port number for the target server.
5.  When prompted for ‘STATUS:’, ensure this is set to ENABLED.
6.  When prompted for ‘LOGIN REQUIRED:’, answer ‘YES’.
7.  When prompted for ‘USERNAME:’, enter the assigned username.
8.  When prompted ‘Want to edit PASSWORD (Y/N), respond ‘YES’.
9.  Enter the password associated with the username.
10. Re-enter the password to verify the password.
11. At the “SSL ENABLED” prompt, accept the default of “FALSE”.
12. At the “Select Web Service” prompt, enter “PSO ERX WEB SERVICE”.

> **NOTE:** Do not include restricted information in the help desk ticket. It is VA Policy to send this information securely via public key infrastructure (PKI) message. Securely send this information for both the VistALink connector on your test VistA system and the VistALink connector on your production VistA system.

### Coordination of Installation with Change Healthcare

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please contact Inbound eRx implementation group, InboundeRx@va.gov, to finalize coordination of installation with Change Healthcare.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning is required before or after deployment of PSO\*7.0\*581.

![](inbound-eprescribing-implementation-guide-pso-7-581/003.png)

> **NOTE:** Installation of PSO\*7.0\*581 is completed. The following procedure is to be followed only if PSO\*7.0\*581 needs to be backed out.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the NSD at 855-NSD-HELP (673-4357) and reference “Inbound eRx” to submit a YourIT ServiceNow ticket; the development team will assist with the process.

The Back-out Procedure consists of restoring the routines and removing the Data Dictionaries (DD) introduced by the Patch PSO\*7.0\*581.

The rollback/backout procedure for these patches should only occur when there is concurrence from the Enterprise Product Support and Inbound ePrescribing development teams, because of the complexity and risk involved in a rollback/backout. Normal installation back-ups using KIDS will back up only Mumps routines. For all non-routine components of these builds, Enterprise Product Support will have a build available if needed. Make sure the ‘Backup a Transport Global’ step in section 4.8 of this document is followed, so you do have a backup of all the routines if needed.

The back-out is to be performed by persons with programmer-level access.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-out Strategy is to manually delete the new Data Definitions (DDs) introduced with this patch.

The Back-out and Rollback plan for VistA applications is complex and not able to be a “one size fits all.” The general strategy for VistA back-out and rollback is to repair the code with a follow-on patch. However, the backup of the transport global when created as part of the install will allow the routines to be converted to the prior patch state. For IEP, this is sufficient to restore the code to prior functionality.

The development team recommends that sites log a help desk ticket if it is a nationally released patch; otherwise, the site should contact the product development team directly for specific solutions to their unique problems.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out should only be done in the event that the local facility management determines that the Patch PSO\*7.0\*581 is not appropriate for that facility and should only be done as a last resort.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch PSO\*7.0\*581.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Initial Operating Capabilities (IOC) Testing for patch PSO\*7.0\*581 occurred from November 19, 2020 to December 03, 2020.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Facility Management would need to determine patch PSO\*7.0\*581 is not appropriate for their facility.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out PSO\*7.0\*581, the local facility will not be able to use the IEP functionality to validate and process Inbound ePrescriptions (eR<sub>x</sub>es) from external providers.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Facility Management has the authority to back-out patch PSO\*7.0\*581.

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

The chief of Pharmacy Benefits Management (PBM) must provide the authority to roll back patch PSO\*7.0\*581.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the [Back-Out Procedure](#back-out-procedure) section of this document.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Inbound ePrescribing Implementation Guide (PSO*7*635)

### April 2021

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 3.9 Department of Veterans Affairs
> Office of Information and Technology (OIT)

## VistA PSO\*7.0\*635 Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IEP VistA Patch PSO\*7.0\*635 Warranty defect remediation provides software fixes for:

- SIG text is supposed to be up to 1000 characters, Inbound eRx software assigns wrong unit of measure in RxRenewal Request, RxRenewal Request failing at hub because "IndicationForUse" segment is not sending in "Sig" segment
- Inbound eRx software assigns wrong unit of measure in RxRenewal Request
- NewRx coming in with ObservationDateTime, causing a failure at the eRx processing hub when generating an RxRenewal Request
- Updated Data Dictionary – ERX SERVICE REASON CODES file (#52.45), ACR

> codes in ERX SERVICE REASON CODES file (#52.45) have an extra space at the end

- ACR codes in ERX SERVICE REASON CODES file (#52.45) have an extra space at the end
- VA 'Refills' displaying incorrectly for RxRenewal response replace response messages
- VA 'Refills' displaying incorrectly for RxRenewal response replace response messages extend the logic from 365 days to 1 and half year for messages related to display at hub (Track/Audit page), a backlog of messages is queueing up and waiting for outbound

> delivery to CH during peak hours, reports page columns are missing in the last three reports

- NewRx counts not showing for summary new Rx Only and report totals at the bottom of the tables do not align with the correct column
- Reports - number of records not being displayed at the bottom of all reports and column width for Message Type in Track/Audit not wide enough.
- When editing the Validate Drug/SIG for Replace RxRenewal Response, eRx refills are not decrementing correctly and incorrectly displays the \# of Refills.

> The steps required for full implementation are listed. However, this document is limited to the technical changes required for implementation. Please refer to the Inbound ePrescribing User Guide in the VA Software Document Library (VDL) for more information on the VistA eR<sub>X</sub> Holding Queue functionality and other eR<sub>X</sub> user functions.

### Install VistA Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the patch is received from Forum for National Deployment the local Site IT Administrator for each Pharmacy site needs to install the PSO\*7.0\*635 patch. The software for this patch is

> being released in a PackMan message.

1.  Install VistA Patch PSO\*7.0\*635 – For detailed instructions, refer to Installation Guide - Inbound ePrescribing (pso_7_0_p635_ig.pdf).
2.  See Pre-Installation Instructions in the Patch Description for sites configured and running PSO\*7.0\*635.
3.  Validate that the Inbound eR<sub>X</sub> patch was installed successfully.

### Training

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the Pharmacy Manager has decided that their site will be processing live eR<sub>X</sub>’s they need to first ensure that their pharmacists/users have been trained on using the ePrescribing application.

> To train the end users on using the application, refer to Training Material at [<u>Inbound</u>](https://dvagov.sharepoint.com/sites/OITEPMOPRE/PRE_Inb_eRx/v4%20Shared%20Documents/Forms/AllItems.aspx?viewid=4cd4d485%2D482a%2D4c96%2Da908%2D7481510bddc5&id=%2Fsites%2FOITEPMOPRE%2FPRE%5FInb%5FeRx%2Fv4%20Shared%20Documents%2FTraining%20Materials) [<u>ePrescribing (IEP) Training Materials</u>.](https://dvagov.sharepoint.com/sites/OITEPMOPRE/PRE_Inb_eRx/v4%20Shared%20Documents/Forms/AllItems.aspx?viewid=4cd4d485%2D482a%2D4c96%2Da908%2D7481510bddc5&id=%2Fsites%2FOITEPMOPRE%2FPRE%5FInb%5FeRx%2Fv4%20Shared%20Documents%2FTraining%20Materials)

### Assign Security Keys in VistA to eRX Holding Queue Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign keys for users who need access to the VistA eR<sub>X</sub> Holding Queue.

#### VistA Security Keys for accessing eR<sub>X</sub> Holding Queue

> The following keys are available:

- PSDRPH: PSDRPH key is assigned to Pharmacists only. Most Pharmacists may already have been allocated this key, and therefore no additional action is required for these users.

#### PSO ERX ADV TECH

- PSO ERX TECH

#### PSO ERX VIEW

> <span id="_bookmark6" class="anchor"></span>Table 1: NewRx, Refill/RxRenewal Request and Response, CancelRx Request and Response (v2.0 and v3.0)

| VistA Security Key | PSD RPH | PSO ERX ADV TECH | PSO ERX TECH | PSO ERX VIEW |
|------------------------|-------------|----------------------|------------------|------------------|
| Validate Patient       | X           | X                    | X                |                  |
| Validate Provider      | X           | X                    | X                |                  |
| Validate Drug/SIG      | X           | X                    | X                |                  |
| Accept Validation      | X           | X                    |                  |                  |

| VistA Security Key        | PSD RPH | PSO ERX ADV TECH | PSO ERX TECH | PSO ERX VIEW |
|-------------------------------|-------------|----------------------|------------------|------------------|
| Accept eRX                    | X           | X                    |                  |                  |
| Reject                        | X           | X                    | X                |                  |
| Remove                        | X           | X                    | X                |                  |
| Hold                          | X           | X                    | X                |                  |
| Un Hold                       | X           | X                    | X                |                  |
| Search/Sort                   | X           | X                    | X                | X                |
| Print                         | X           | X                    | X                | X                |
| Message View                  | X           | X                    | X                | X                |
| Ack – RxRenewal Response      | X           | X                    | X                |                  |
| RxChange Request              | X           | X                    | X                |                  |
| RxRenewal Request (OP)        | X           | X                    | X                |                  |
| Ack – CancelRx                | X           | X                    |                  |                  |
| Ack – Inbound RxRenewal Error | X           | X                    | X                |                  |

> <span id="_bookmark7" class="anchor"></span>Table 2: RxRenewal Response – Replace Type (v4.0)

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Security Key</strong></th>
<th><strong>PSD RPH</strong></th>
<th><strong>PSO ERX ADV TECH</strong></th>
<th><blockquote>
<p><strong>PSO ERX TECH</strong></p>
</blockquote></th>
<th><strong>PSO ERX VIEW</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Validate Patient</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Validate Provider</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Validate Drug/SIG</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Accept Validation</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Accept eRX</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Reject</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Remove</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Hold</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Un Hold</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Search/Sort</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td>Print</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td>Message View</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
</tbody>
</table>

> <span id="_bookmark8" class="anchor"></span>Table 3: RxChange Response – Replace Type (v4.0)

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Security Key</strong></th>
<th><strong>PSD RPH</strong></th>
<th><strong>PSO ERX ADV TECH</strong></th>
<th><blockquote>
<p><strong>PSO ERX TECH</strong></p>
</blockquote></th>
<th><strong>PSO ERX VIEW</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Validate Patient</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Validate Provider</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Validate Drug/SIG</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Accept Validation</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Accept eRX</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Reject</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Remove</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Hold</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>Un Hold</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Search/Sort</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td>Print</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td>Message View</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td>Ack – RxChange Response</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> X – This means have ability to use option.

#### Steps to assign Security Keys in VistA

> The following outlines the steps for assigning keys (may need to be done by local Site IT Administrator):

1.  Log in to VistA.
2.  At the “Select OPTION NAME” prompt, type “eve” and then press the \<Enter\> key.
3.  At the “Choose 1-5” prompt, type “1” (for EVE Systems Manager Menu) and then press the \<Enter\> key.
4.  At the “Select Systems Manager Menu Option” prompt, type “menu” (for Menu Management) and then press the \<Enter\> key.
5.  At the “Select Menu Management Option” prompt, type “key” (for Key Management) and then press the \<Enter\> key.
6.  At the “Select Key Management Option” prompt, type “allocation” (for Allocation of Security Keys) and then press the \<Enter\> key.
7.  At the “Allocate key” prompt, type the name of the security key you want to assign and then press the \<Enter\> key.
8.  At the “Holder of key” prompt, type the name of the first user to whom you are assigning the key and then press the \<Enter\> key.
9.  At the “Another holder” prompt, type the name of a second user to whom you are

> assigning the key and then press the \<Enter\> key. Repeat this step for all users to whom you are assigning the key.

10. At the “You are allocating keys. Do you wish to proceed? YES//” prompt, press the

> \<Enter\> key to accept the default response.

### Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The sites need to determine which outpatient pharmacy site is going live. A pharmacy site is

> considered a Division in outpatient pharmacy. All inbound eR<sub>X</sub> sites must be physical locations, already have an NCPDP NUMBER, and have an NPI NUMBER.

### Verify NCPDP NUMBER used by ePharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Review the local pharmacy information by contacting the ePharmacy Team via email at [<u>VHA</u>](mailto:VHAePharmacyImplementationTeam@va.gov) <u>[ePharmacy Implementation Team](mailto:VHAePharmacyImplementationTeam@va.gov).</u>

> For each dispensing pharmacy, verify the following data in the columns of the spreadsheet maintained by the ePharmacy Team:

- Physical Address (columns J-M)
- Pharmacy Phone Number (column N)
- Pharmacy Fax Number (column O)
- Pharmacy email address (column P)
- Date Pharmacy Logistics Updated (column U)
- Updates Completed by (column V)

> Make, or request ePharmacy Team to make, the changes on the spreadsheet. Once a pharmacy goes live with Inbound eR<sub>X</sub>, the NCPDP information is published to providers and others,

> therefore accuracy is essential. In addition, if the eR<sub>X</sub> fails, the clearing house sends an

> automated fax of the eR<sub>X</sub> to the pharmacy. So, ensure that your pharmacy’s fax number is correct. If changes are made, they update at the NCPDP and the clearinghouse. Updating NCPDP and the clearinghouse is a manual process and takes time.

### OUTPATIENT SITE file (#59)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Using FileMan, inquire into the OUTPATIENT SITE file (#59), check the NCPDP NUMBER file (#1008), NPI Institution field (#101), and CPRS Order Institution field (#8).

1.  Ensure that the NCPDP NUMBER is the same as the one that is listed in the ECME Setup-Pharmacies Report (see Section <u>1.1.5</u> above).
2.  Make note of the NPI Institution entry.
3.  Add the pharmacy (in the NPI Institution field) as a CPRS Ordering Institution, so the

> ![](inbound-eprescribing-implementation-guide-pso-7-635/002.png)eRX orders can be pulled using Complete orders from OERR \[PSO LMOE FINISH\].

> <span id="_bookmark13" class="anchor"></span>Figure 1-1: OUTPATIENT SITE file (#59) in Inquire Mode

### When to contact ePharmacy Implementation Team:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites should contact the ePharmacy Team prior to making any changes to the VistA Electronic Claims Management Engine Number (ECME) Setup.

> The ePharmacy Team should be notified of changes to the Physical Address, Telephone Number,

> Fax Number, when new pharmacies open and/or if a pharmacy closes. The ePharmacy Team coordinates any needed changes with NCPDP, NPI Team and the clearinghouse. Contact

> ePharmacy Team by e-mail at [<u>VHA ePharmacy Implementation Team</u>](mailto:VHAePharmacyImplementationTeam@va.gov).

### Configure Default eRX Clinic (OPTIONAL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Default eR<sub>X</sub> Clinic allows the local user to locate non-processed eR<sub>X</sub> prescriptions by clinic name, in the existing pending queue.

> Sites can add a Default eR<sub>X</sub> Clinic in OUTPATIENT SITE file (#59), DEFAULT ERX CLINIC field (#10). A new Hospital Location entry with type as ‘Clinic’ needs to be created for the

> purpose of Inbound ePrescribing.

> The diagram below depicts the relationship between OUTPATIENT SITE file (#59), HOSPITAL LOCATION file (#44), and INSTITUTION file (#4).

![](inbound-eprescribing-implementation-guide-pso-7-635/003.png)

> <span id="_bookmark16" class="anchor"></span>Figure 1-2: INSTITUTION file (#4), OUTPATIENT SITE file (#59) and HOSPITAL LOCATION file (#44)

> Configuration

> To confirm setup of Default eR<sub>X</sub> Clinic, using FileMan “Enter or Edit File Entries” option, in the HOSPITAL LOCATION file (#44). This setup may require assistance from Medical Administration Team:

1.  Check the field: INSTITUTION field (#3).
2.  If it is blank, use the NPI INSTITUTION identified in OUTPATIENT SITE file (#59).
3.  If it is not blank, ensure that the NPI INSTITUTION is same as the one identified in OUTPATIENT SITE file (#59).

> ![](inbound-eprescribing-implementation-guide-pso-7-635/004.png)

> <span id="_bookmark17" class="anchor"></span>Figure 1-3: HOSPITAL LOCATION file (#44) in Enter or Edit File Entries Mode

> Using FileMan “Enter or Edit File Entries”, in the OUTPATIENT SITE file (#59), enter the DEFAULT ERX CLINIC field (#10).

1.  If it is blank, populate it with the Clinic created for the purpose of Inbound ePrescribing.
2.  If it is not blank, ensure that the Clinic used is same as the one created for the purpose of Inbound ePrescribing.

![](inbound-eprescribing-implementation-guide-pso-7-635/005.png)

> <span id="_bookmark18" class="anchor"></span>Figure 1-4: OUTPATIENT SITE file (#59) in Enter or Edit File Entries Mode

### NPI Institution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Using FileMan Inquiry into the INSTITUTION file (#4), select the NPI Institution identified in the OUTPATIENT SITE file (#59) from section [<u>1.1.6</u>](#outpatient-site-file-59), step b. Make note of the Pharmacy NPI Number.

- If there is no Pharmacy NPI, contact the ePharmacy Team and the NPI Team by e-mail at [<u>VHA ePharmacy Implementation Team</u>](mailto:VHAePharmacyImplementationTeam@va.gov) and [<u>VHA NPI Team</u>](mailto:VHACONPI@va.gov).
- The ePharmacy Team collaborates with the site and the NPI Team to determine if a new NPI is needed. If a new NPI is needed, the NPI Team submits the request to National Plan and Provider Enumeration System (NPPES) and notifies the site when the NPI

> number is assigned by NPPES.

![](inbound-eprescribing-implementation-guide-pso-7-635/006.png)

> <span id="_bookmark20" class="anchor"></span>Figure 1-5: INSTITUTION file (#4) in Inquire Mode

### Configure ERX DEFAULT LOOKBACK DAYS (OPTIONAL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](inbound-eprescribing-implementation-guide-pso-7-635/007.png)Using Site Parameter Enter/Edit \[PSO SITE PARAMETERS\] option, update the value for ERX DEFAULT LOOK BACK DAYS (field \#10.2), in OUTPATIENT SITE file (#59), as required by the site. Navigate and jump (^) to the ERX DEFAULT LOOKBACK DAYS.

> <span id="_bookmark22" class="anchor"></span>Figure 1-6: OUTPATIENT SITE file (#59) in Inquire Mode

> ![](inbound-eprescribing-implementation-guide-pso-7-635/008.png)

> <span id="_bookmark23" class="anchor"></span>Figure 1-7: OUTPATIENT SITE file (#59) ERX DEFAULT LOOKBACK DAYS Updated

### Ready to Go Live

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the site confirms the users have been trained and the NCPDP and NPI information is correct the site is then ready to proceed with enabling their pharmacy to start receiving live eR<sub>X</sub>es. The Inbound eR<sub>X</sub> Support Team assists the site with the final steps to enable their pharmacy.

1.  To Go Live, submit a help desk ticket to the VA National Service Desk (NSD) at 855- NSD-HELP (673-4357) and reference “Inbound eR<sub>X</sub>”.
2.  Provide the following site information for the ticket: NCPDP NUMBER, NPI \#, VISN, VA Station ID, Pharmacy Name (External/Published), Address, Phone Number and Fax Number.
    1.  NSD Team routes the ‘go live’ request to Inbound eRX Support Team.
    2.  Once the Inbound eRX Support Team receives the NSD help ticket they contact the site point of contact (POC) to complete the steps to enable the pharmacy.
3.  The Support Team helps the local Site IT Administrator to setup the Connector Proxy.
4.  The local Site IT Administrator sets up the Connector Proxy and provides the access and verify codes to the Support Team.
    1.  Select XOBU SITE SETUP MENU.
    2.  Select CP - Enter/Edit Connector Proxy User.
    3.  Answer the prompts, naming the connector: CONNECTORPROXY, PSO.
    4.  At the “Want to edit ACCESS CODE (Y/N)” prompt, type “Y” (for Yes).
    5.  Enter the access code for the connector proxy.
    6.  Re-enter the access code for the connector proxy.
    7.  At the “Want to edit VERIFY CODE (Y/N)” prompt, type “Y” (for Yes).
    8.  Enter a verify code for the proxy connector.
    9.  Re-enter the verify code for the proxy connector.
5.  The local Site IT Administrator also provides the VistA link FQDN, TCP Port, and primary Station ID to the Support Team.
6.  The Support Team will uses this configuration information to create and test a new VistA link connection from the Inbound eR<sub>X</sub> Processing Hub to the site.
7.  The Support Team provides the FQDN, PORT, and USERNAME/PASSWORD for WEB SERVER entry to the local Site IT Administrator.
8.  The Site IT Administrator configures the WEB SERVER entry.
    1.  Select option XOBW WEB SERVER MANAGER.
    2.  Select ES for Edit Server.
    3.  At the “NAME” prompt, enter “PSO WEB SERVER”.
    4.  At the “SERVER:” prompt, enter the target server FQDN. The target server name and port are given to the site during implementation.
    5.  At the “PORT:” prompt, enter the target server port number.
    6.  At the “STATUS:” prompt, ensure status is set to “ENABLED”.
    7.  At the “LOGIN REQUIRED:” prompt, answer “YES”.
    8.  At the “USERNAME:” prompt, enter the assigned username.
    9.  At the “Want to edit PASSWORD (Y/N)” prompt, type “Y” (for YES).
    10. Enter the password associated with the username.
    11. Re-enter the password to verify the password.
    12. At the “SSL ENABLED” prompt, accept the default of “FALSE”.
    13. At the “Select Web Service” prompt, enter “PSO ERX WEB SERVICE”.
9.  The Support Team assigns user privileges for the IEP Web-based Graphical User Interface (GUI) Hub to the respective users from the site. Please see section [<u>1.2.3</u>](#_bookmark37) for additional details.
10. The Support Team notifies the clearinghouse that the site is ready to Go Live.
11. The Support Team coordinates with the site to determine the expected go live date.
12. On the go live date, the clearinghouse sends a test eR<sub>X</sub> message to the site to confirm inbound connectivity and receipt of the message in the VistA Holding Queue.
13. Upon confirming the receipt of the Test message successfully in VistA, the support team checks if a Verify message was sent successfully to test the outbound connection to the

> clearing house.

14. The site responds with a reject message to test the outgoing connection to the Transaction Hub.
15. Once successfully confirmed, the clearinghouse enables the Pharmacy in their directory and has SureScripts enable it in their directory.
16. The Pharmacy is now Live and enabled to receive eR<sub>X</sub>es.

### Help Desk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For issues with the IEP web-based application that cannot be resolved by this manual or the site administrator, please contact the National Service Desk at 855-NSD-HELP (673-4357) and

> reference “Inbound eRX”.

#### Help Desk Ticket Instructions

> To submit a Help Desk ticket:

1.  Select the “Your IT” icon on your desktop.

![](inbound-eprescribing-implementation-guide-pso-7-635/009.png)

> <span id="_bookmark27" class="anchor"></span>Figure 1-8: Your IT Desktop Icon

> The homepage displays.

2.  ![](inbound-eprescribing-implementation-guide-pso-7-635/010.png)Select Incident.

> <span id="_bookmark28" class="anchor"></span>Figure 1-9: Incident Selection

3.  Select Create New.

![](inbound-eprescribing-implementation-guide-pso-7-635/011.png)

> <span id="_bookmark29" class="anchor"></span>Figure 1-10: Create New Selection

4.  ![](inbound-eprescribing-implementation-guide-pso-7-635/012.png)Populate the required fields.
5.  <span id="_bookmark30" class="anchor"></span>Select Submit.

> Figure 1-11: New Incident

## Inbound ePrescribing Web-based Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IEP Web-based application provides eR<sub>X</sub> management, administration, and monitoring

> capabilities. There are four modules of the IEP Web-based application: Pharmacy Management, Track/Audit, User Management, and Help. Please refer to the Inbound ePrescribing User Guide for more information on the functionality found within the application.

> The IEP Web-based application is accessed at the following link: [<u>Inbound ePrescribing Web</u>](https://vaausappiep201.aac.va.gov/inbound/) [<u>Application</u>](https://vaausappiep201.aac.va.gov/inbound/).

### Create Shortcut on Workstation (Desktop)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> While at a user’s workstation, create shortcuts to the IEP Web-based application. To create a shortcut on a user’s desktop:

1.  Right-click the desktop and select New and then select Shortcut.
2.  ![](inbound-eprescribing-implementation-guide-pso-7-635/013.png)Type the URL provided by IT support or the local Site IT Administrator in the “Type the location of the item” field and then select Next. A “Create Shortcut” dialog, similar to the one in the figure below, displays.

> <span id="_bookmark33" class="anchor"></span>Figure 1-12: Create Shortcut Dialog Box

3.  <span id="_bookmark37" class="anchor"></span>Type a name for the shortcut in the “Type a name for this shortcut” field (e.g., Inbound ePrescribing).

![](inbound-eprescribing-implementation-guide-pso-7-635/014.png)

> <span id="_bookmark34" class="anchor"></span>Figure 1-13: Name Shortcut

4.  Select Finish to place the shortcut on the desktop.

### Turn off Compatibility Setting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IEP Web-based application runs in Internet Explorer 11 or greater. Note that Compatibility View must be turned off for the application to run effectively.

> To turn off Compatibility View:

5.  In Internet Explorer, select Tools \> Compatibility View Settings.
6.  ![](inbound-eprescribing-implementation-guide-pso-7-635/015.png)Verify that the “Display intranet sites in Compatibility View” checkbox is not selected.

> <span id="_bookmark36" class="anchor"></span>Figure 1-14: Compatibility View Settings

### Assign Roles in IEP Web-based Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A local Site IT Administrator needs to be identified and assigned for administering the IEP Web- based application. The local Site IT Administrator manages user access and permissions of the Web-based application at the site. The following roles are available in the application:

> <span id="_bookmark39" class="anchor"></span>Table 4: Inbound ePrescribing Web-Based Application User Roles & Capabilities

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>User Role</strong></th>
<th><strong>Functionality</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Administrator</td>
<td>Full Control, access to all tabs</td>
</tr>
<tr class="even">
<td>Pharmacy Management</td>
<td><p>Home</p>
<p>Pharmacy Management Track/Audit</p>
<p>Reports Help</p></td>
</tr>
<tr class="odd">
<td>PBM Administrator</td>
<td><p>Home</p>
<p>Pharmacy Management Track/Audit</p>
<p>Reports</p>
<p>Help</p></td>
</tr>
<tr class="even">
<td>Pharmacy Users</td>
<td>Home Track/Audit Reports Help</td>
</tr>
<tr class="odd">
<td>Def ault VA User (Read Only)</td>
<td>Home Reports Help</td>
</tr>
</tbody>
</table>

> The Support Team assigns user privileges for the IEP Web-based Graphical User Interface (GUI) Hub to the respective users from the site, including the Site IT Administrator role. For continued support in assigning user privileges, the local Site IT Administrators can use the User

> Management screen to add new users, modify user roles, and disable users. This module only displays for users with the Administrator role assigned.

#### Add New User

> System Administrators can add new users from the User Management screen. To add a new user:

1.  Enter the new user’s User ID, First Name, and Last Name.

![](inbound-eprescribing-implementation-guide-pso-7-635/016.png)

> <span id="_bookmark41" class="anchor"></span>Figure 1-15: Add User - User ID, First Name, Last Name

2.  Select the new user’s role(s). Multiple roles may be selected by holding \<Ctrl\> while selecting more than one role.

![](inbound-eprescribing-implementation-guide-pso-7-635/017.png)

> <span id="_bookmark42" class="anchor"></span>Figure 1-16: Add User - Select User Roles

3.  Select the Station ID(s) for the user to have access to. Use the drop down menu to display the Station ID selection Multiple Station IDs may be selected by holding \<Ctrl\> while selecting more than one Station ID.

![](inbound-eprescribing-implementation-guide-pso-7-635/018.png)

> <span id="_bookmark43" class="anchor"></span>Figure 1-17: Add User – Select Station ID

4.  Select the Add button to add the selected Station ID to the “Selected Station IDs” field. To remove Station IDs from the “Selected Station IDs” field, select Remove (not shown).

![](inbound-eprescribing-implementation-guide-pso-7-635/019.png)

> <span id="_bookmark44" class="anchor"></span>Figure 1-18: Add User – Add and Remove Station ID

> When a user is assigned to a Station ID, they are only able to see other users and information within that Station ID. For example, in the User Management table they only see users also

> assigned to that Station ID and under Pharmacy Management, they only see information for pharmacies within that Station ID.

> If All is selected from the “Station ID” field and added to the “Selected Station IDs” field, the user has access to all Station IDs. Additional Station ID values cannot be added if All has been

> selected and added to the “Selected Station IDs” field. If a user attempts to add additional values an error message displays.

![](inbound-eprescribing-implementation-guide-pso-7-635/020.png)

> <span id="_bookmark45" class="anchor"></span>Figure 1-19: All Selection Error Message

5.  Select Save to add the new user to the users list. To cancel adding a new user, select

#### Cancel.

![](inbound-eprescribing-implementation-guide-pso-7-635/021.png)

> <span id="_bookmark46" class="anchor"></span>Figure 1-20: Add User - Save and Cancel

#### Modify User Role

> System Administrators can modify user roles from the User Management screen. User roles include:

- Pharmacy Manager
- PBM Admin
- Pharmacy User
- Administrator

> For further information on user roles and capabilities, please refer to the Inbound ePrescribing User Guide.

> To modify user roles:

1.  From the users list, locate the user and select the checkbox(es) for the desired user role(s).

![](inbound-eprescribing-implementation-guide-pso-7-635/022.png)

> <span id="_bookmark48" class="anchor"></span>Figure 1-21: Select User Roles

2.  Select Save at the bottom of the screen. A message displays indicating that the user was updated successfully.
3.  Select Cancel to cancel modifying user roles.

#### Enable/Disable Users

> Users can be disabled and/or re-enabled to use the web application. To update a user’s access to the application, locate the user in the User Management table and select the checkmark in the “Enable/Disable” column. Select Save from the bottom of the screen to update the user’s access.

![](inbound-eprescribing-implementation-guide-pso-7-635/023.png)

> <span id="_bookmark50" class="anchor"></span>Figure 1-22: User Management Table – Enable/Disable User

> When a user is disabled, their information is greyed in the User Management table. To modify the user’s access again, select the checkbox in the “Enable/Disable” column again.

![](inbound-eprescribing-implementation-guide-pso-7-635/024.png)

> <span id="_bookmark51" class="anchor"></span>Figure 1-23: User Disabled

> If a user that has been disabled attempts to log in to the application, an error message displays.

![](inbound-eprescribing-implementation-guide-pso-7-635/025.png)

> <span id="_bookmark52" class="anchor"></span>Figure 1-24: User Disabled Error Message

### Pharmacy Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Pharmacy Management screen displays the Pharmacy Management table. The default view displays all VA pharmacies. Actions available to users include:

- [<u>Search Pharmacy</u>](#search-pharmacy)
- [<u>Add Pharmacy</u>](#add-pharmacy)
- [<u>Update Pharmacy</u>](#enable-pharmacy)

#### Search Pharmacy

> Users can search for a pharmacy from the Pharmacy Management screen. The default view lists all VA pharmacies.

> To search for a pharmacy:

1.  Enter the NCPDP ID (if known).
2.  Enter the Pharmacy Name.
3.  Select the desired VISN number from the “VISN” drop down.
4.  Select the desired Station ID from the “Station ID” drop down. If viewing All VISNs, the user is unable to select a Station ID. To select a specific Station ID, the VISN must be

> selected.

5.  Select Search.

> The Pharmacy Management table displays results for the selected search criteria.

> ![](inbound-eprescribing-implementation-guide-pso-7-635/026.png)

#### Add Pharmacy

> Figure 1-25: Search for a Pharmacy

> To add a new pharmacy, please submit a help desk ticket to the VA National Service Desk (NSD) at 1-855-NSD-HELP (673-4357) and reference “Inbound eRX”.

#### Enable Pharmacy

> ![](inbound-eprescribing-implementation-guide-pso-7-635/027.png)The pharmacy can be enabled to receive eR<sub>X</sub>es during initial go live or if it has been previously disabled. To enable a pharmacy select Yes from the “Inbound eR<sub>X</sub> Enabled” drop down on the Edit Pharmacy screen.

> <span id="_bookmark58" class="anchor"></span>Figure 1-26: Enable Pharmacy

1.  <span id="1.2.4.2.1.1_Enrollment_and_Eligibility_C" class="anchor"></span>Enrollment and Eligibility Check

> The Enrollment and Eligibility (E&E) check may be enabled or disabled for individual

> pharmacies. This option is provided so each pharmacy may decide whether to turn the E&E check on or off depending on whether the patients whose eRXes are filled at the pharmacy are enrolled in the E&E system. For example, MbM does not currently have any patient enrolled with the E&E system.

> To ensure the Enrollment and Eligibility Check is enabled for a pharmacy, select the desired

> pharmacy from the Pharmacy Management table and ensure “Yes” displays in the “Enrollment and Eligibility Check Enabled” field. If required, select Yes in the “Enrollment and Eligibility Check Enabled” drop down and then select Update.

![](inbound-eprescribing-implementation-guide-pso-7-635/028.png)

> <span id="_bookmark60" class="anchor"></span>Figure 1-27: Enrollment and Eligibility Check Enabled

#### Temporarily Disable Pharmacy

> In a case where a site needs to halt receiving ePrescriptions temporarily, use Disable eR<sub>X</sub>/Enable eR<sub>X</sub> fields.

> Disabling a pharmacy allows users the ability to temporarily disable the pharmacy from

> receiving eR<sub>X</sub>es in the event of a natural or facility disaster, maintenance, or move. This disables the pharmacy from receiving New eR<sub>X</sub>es, but outbound messages still go back to the external

> provider via Change Healthcare (CH). The pharmacy is disabled on the Processing Hub, but no changes are made in CH.

> To temporarily disable a pharmacy:

1.  On the Pharmacy Management screen, select Search and then, select the hyperlink for the desired pharmacy under the “NCPDP ID” column. The Edit Pharmacy screen

> ![](inbound-eprescribing-implementation-guide-pso-7-635/029.png)displays.

> <span id="_bookmark62" class="anchor"></span>Figure 1-28: Edit Pharmacy Screen

2.  ![](inbound-eprescribing-implementation-guide-pso-7-635/030.png)Select No from the “Inbound eR<sub>X</sub> Enabled” drop down.

> <span id="_bookmark63" class="anchor"></span>Figure 1-29: Inbound eRX Enabled Drop Down

4.  At the bottom of the Edit Pharmacy screen, select Update to save all changes. The date that the fields were modified displays in the “Updated Date” field.

![](inbound-eprescribing-implementation-guide-pso-7-635/031.png)

> <span id="_bookmark64" class="anchor"></span>Figure 1-30: Update Pharmacy Information

5.  Selecting the Return to Pharmacy Information button returns the user to the Pharmacy Management screen.

#### Disable Pharmacy

> To completely halt a specific Pharmacy from receiving ePrescriptions, please submit a help desk ticket to the VA National Service Desk (NSD) at 1-855-NSD-HELP (673-4357) and reference “Inbound eR<sub>X</sub>”.
