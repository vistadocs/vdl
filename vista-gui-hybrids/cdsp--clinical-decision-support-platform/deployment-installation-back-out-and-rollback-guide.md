---
consolidated_title: "deployment, installation, back-out, and rollback guide word doc"
app_code: CDSP
doc_type: DIBR
master_source: "OR*3*614 Deployment, Installation, Back-out, and Rollback Guide Word Doc"
master_pub_date: revision_count: 0
consolidated_from: 2 versions
prior_versions:
  - "CDSP*1*0 Deployment, Installation, Back-out, and Rollback Guide Word Doc"
---

---
title: |
  <span id="_heading=h.gjdgxs" class="anchor"></span>OR\*3.0\*614 Vista Patch

  Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)
---

![](or-3-614-deployment-installation-back-out-and-rollback-guide-word-doc/001.png)

February 2024OR\*3\*614Department of Veterans AffairsOffice of Information and Technology (OIT)Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2/1/2024</td>
<td>3.0</td>
<td><p>OR*3.0*614</p>
<ul>
<li><p>Approved on 2/1/2024</p></li>
</ul></td>
<td>TWKS CDSP</td>
</tr>
</tbody>
</table>

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integration Process (VIP) Guide, the “Deployment, Installation, Back-out, and Rollback Plan” is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

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
  - [Pre-installation and System Requirement](#pre-installation-and-system-requirement)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [KIDS Installation](#kids-installation)
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
    - [Delete CDSP COM Objects:](#delete-cdsp-com-objects)
  - [## KIDS Back-out](#kids-back-out)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
  - [N/A](#na)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the patch OR\*3\*614, as well as how to back-out the product and rollback to a previous version or data set.
This patch is being deployed initially to the test sites (mentioned in [<u>Site Information</u>](#_heading=h.35nkun2)) and will be evaluated for national deployment.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the OR\*3\*0\*614 patch will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                          | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|-----------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | Project Team and Development Team | Deployment       | Plan and schedule deployment                                                                                        | Planning                         |
| 2      | Development Team                  | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment                           | Planning                         |
| 3      | Enterprise Operations (EO)        | Deployment       | Test for operational readiness                                                                                      | Testing                          |
| 4      | Development Team                  | Deployment       | Execute deployment                                                                                                  | Deployment                       |
| 5      | Development Team                  | Installation     | Plan and schedule installation                                                                                      | Deployment                       |
| 6      | Project Team                      | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                       | Deployment                       |
| 7      | Development Team                  | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                       |
| 8      | Project Team                      | Post Deployment  | Hardware, Software and System Support                                                                               | Warranty                         |

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment for OR\*3\*614 is planned as a single VistA Package rollout.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for approximately one day.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the OR\*3\*614 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch OR\*3\*614 is to be deployed to the test sites and upon acceptance will be nationally released.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The test sites for the OR\*3\*614 patch testing are:

- Miami VA Healthcare System (Miami, FL),
- Phoenix VA Health Care System (Phoenix, AZ)

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

Table 2:SitePreparation

| Site/Other                | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner                                                                             |
|-------------------------------|---------------------------|---------------------------------------------|-------------------|---------------------------------------------------------------------------------------|
| Miami VA Healthcare System    | N/A                       | N/A                                         | Install patch     | Information Resource Management (IRM) or Enterprise Service Line (ESL) representative |
| Phoenix VA Health Care System | N/A                       | N/A                                         | Install patch     | IRM or ESL                                                                            |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

Table 3: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      |                |                     |           |

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

Table 4: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   |           |             |                   |                  |           |

Please see the Roles and Responsibilities table in section <u>2</u> for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

Table 5:Software Specifications

| Required Software | Make | Version | Configuration | Manufacturer | Other |
|-----------------------|----------|-------------|-------------------|------------------|-----------|
| N/A                   |          |             |                   |                  |           |

Please see the Roles and Responsibilities table in section <u>2</u> above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites that are participating in the field testing of this patch will use the Patch Tracking message in Outlook to communicate with the CDSP and OR teams.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch OR\*3\*614, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in FORUM. FORUM automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in FORUM to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not currently installed the patch in their VistA production system.

Therefore, this information does not need to be manually tracked in the chart below. Below there is a table below if manually tracking is desired.

Table 6: Deployment/Installation/Back-Out Checklist

|              |         |          |                                   |
|--------------|---------|----------|-----------------------------------|
| Activity | Day | Time | Individual who completed task |
| Deploy       |         |          |                                   |
| Install      |         |          |                                   |
| Back-Out     |         |          |                                   |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3\*614 will be transmitted via PackMan message, and therefore does need to be downloaded separately.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3\*614 modifies the VistA database. All changes can be found on the NPM documentation for this patch in FORUM.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are needed for the OR\*3\*614 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for the OR\*3\*614 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install the VistA patches in the host file, the patch installer must be an active user on the

VistA system and have access to the VistA menu option “Kernel Installation & Distribution

System” \[XPD MAIN\] and have VistA security keys XUPROG and XUPROGMODE.

Knowledge on how to install VistA patches using the items on this menu option is also a

required skill. The patch installer will need access to the PackMan message containing the OR\*3\*614 patch or to FORUM’s NPM for downloading the patch.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation Menu. From this menu,
    1.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup, the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
        1.  At the Installation option menu, select Backup a Transport Global
        2.  At the Select INSTALL NAME prompt, enter OR\*3.0\*614
        3.  When prompted for the following, enter B for Build.

> Select one of the following:

> B Build

> R Routines

> Enter response: Build

4.  When prompted “Do you wish to secure your build? NO//”, press \<enter\> and take the default response of NO.
5.  When prompted with, “Send mail to: Last name, First Name”, press \<enter\> to take default recipient. Add any additional recipients.
6.  When prompted with “Select basket to send to: IN//”, press \<enter\> and take the default IN mailbox or select a different mailbox.
2.  You may also elect to use the following options:
    1.  Print Transport Global – This option will allow you to view the components of the KIDS build.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all the components of this patch, such as routines, DDs, templates, etc.
3.  Select the Install Package(s) option and choose the patch to install.
    1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
    2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
    3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OR\*3\*614 patch does not contain any routines and therefore does not require checksum verification

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required for this patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocations or other resources is necessary.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings. The back-out procedure should not be performed as part of the installation process, but instead be performed only if the system needs to be restored to its previous state due to catastrophic issues. Please read further for more information.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although it is highly unlikely that problems with this patch will occur as there are no Data

Dictionaries modifications associated with the OR\*3\*614 patch, a back-out decision due

to other considerations could occur.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the back-out is post-release of patch OR\*3\*614, this patch should be assigned the status of

“Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out process would be executed at normal, rather than raised job priority, and is

expected to have no significant effect on total system performance. Subsequent to the reversion,

the performance demands on the system would be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Criteria for back-out includes, but is not limited to, the project’s cancelation or OR\*3\*614 produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The release coordinator, portfolio director, and Health Product Support have the authority to

initiate a back-out decision. This should be done in consultation with the development team.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The general strategy for a VistA back-out is to repair the code with a follow-up patch. However,

this patch only includes changes to the 101.15 OE/RR COM OBJECTS file contents and does not install any new functionality through Data Dictionaries.

The development team recommends that sites log a ticket if it is a nationally released patch. If

not, the site should contact the team directly via VA email.

The OR\*3\*614 patch includes the following build components:

Files:

- 101.15 OE/RR COM OBJECTS

The OE/RR COM OBJECTS file includes two CDSP related COM objects. Upon installation of the patch, the file included in the patch will be merged with the 101.15 file at the VistA site. In order to remove the two CDSP COM objects installed by the OR\*3\*614 patch, complete the following steps:

### Delete CDSP COM Objects:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

D P^DI

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: PACKAGE// OE/RR COM OBJECTS (4 entries)

EDIT WHICH FIELD: ALL//

Select OE/RR COM OBJECTS NAME: CDSP

1 CDSP COM OBJ 1.0

2 CDSP COM OBJ WRAPPER 1.0

CHOOSE 1-2: 1 CDSP COM OBJ 1.0

NAME: CDSP COM OBJ 1.0// @

SURE YOU WANT TO DELETE THE ENTIRE 'CDSP COM OBJ 1.0' OE/RR COM OBJECTS? Y

(Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'TIU TEMPLATE' FILE,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// N

(No)

Input to what File: OE/RR COM OBJECTS// (3 entries)

EDIT WHICH FIELD: ALL//

Select OE/RR COM OBJECTS NAME: CDSP COM OBJ WRAPPER 1.0

NAME: CDSP COM OBJ WRAPPER 1.0 Replace @

SURE YOU WANT TO DELETE THE ENTIRE 'CDSP COM OBJ WRAPPER 1.0' OE/RR COM OBJEC

TS? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'TIU TEMPLATE' FILE,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No//

(No)

## ## KIDS Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-out Verification Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## N/A 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. The only data changes in this patch are specific to the operational

software and platform settings. These data changes are covered in section 5.6 Back-OutProcedure.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for OR\*3\*614.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for OR\*3\*614.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for OR\*3\*614.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for OR\*3\*614.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for OR\*3\*614.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for OR\*3\*614.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: CDSP*1*0 Deployment, Installation, Back-out, and Rollback Guide Word Doc

### Delete CDSP RPC CONTEXT Option:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

D P^DI

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: OE/RR COM OBJECTS// OPTION

1 OPTION (11204 entries)

2 OPTION SCHEDULING (12 entries)

CHOOSE 1-2: 1 OPTION (11204 entries)

EDIT WHICH FIELD: ALL//

Select OPTION NAME: CDSP RPC CONTEXT CDSP RPC CONTEXT

NAME: CDSP RPC CONTEXT// @

SURE YOU WANT TO DELETE THE ENTIRE 'CDSP RPC CONTEXT' OPTION? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// N

(No)
