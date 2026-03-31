---
title: PSO*7*472 CTT and DM NDS Meds DIBR
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: CTT and DM NDS Meds DIBR
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*472
group_key: "PSO:PSO:7"
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
  - deployment
  - rollback
  - procedure
  - medications
  - global
page_count: 0
word_count: 2394
section_count: 31
table_count: 4
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2017
revision_count: 2
revision_newest: 12/20/2016
revision_oldest: 12/18/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso70_472ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso70_472ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Collaborative Terminology Tooling & Data Management (CTT & DM)

  Native Domain Standardization (NDS) Medications

  PSO_7_0_472 Deployment, Installation,

  Back-Out, and Rollback Guide
---

![](pso-7-472-ctt-and-dm-nds-meds-dibr/001.png)

April 2017

Office of Information and Technology (OI&T)

Revision History

| Date       | Version | Description                                                    | Author                             |
|------------|---------|----------------------------------------------------------------|------------------------------------|
| 04/2017    | 1.1     | Updates per Release Coordinator Request Date changed to April. | <span class="mark">REDACTED</span> |
| 02/2017    | 1.0     | Delivery to Customer.                                          | <span class="mark">REDACTED</span> |
| 02/2017    | .04     | Updates as per Release Coordinator requests.                   | <span class="mark">REDACTED</span> |
| 01/2017    | .03     | Updated Backout section to remove reference to backout patch.  | <span class="mark">REDACTED</span> |
| 12/20/2016 | .02     | Tech Writer Review.                                            | <span class="mark">REDACTED</span> |
| 12/18/2016 | .01     | Initial Draft.                                                 | <span class="mark">REDACTED</span> |

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

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
    - [Pre/Post Installation Overview](#prepost-installation-overview)
    - [Pre-Installation Instructions](#pre-installation-instructions)
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
This document describes how to deploy and install Medications Native Domain Standardization Patch PSO\*7\*472, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Medications Native Domain Standardization Patch PSO\*7\*472 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medications Native Domain Standardization Patch PSO\*7\*472 possesses a direct application dependency on the VistA Outpatient Pharmacy v.7.0 application.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Medications Native Domain Standardization Patch PSO\*7\*472 possesses the following constraints:

- The update to files \#50.416, \#50.6, \#50.605, and \#50.68 shall not affect the current functionality or conflict with applications that utilize these files.
- The fields being added to these files should only be visible within VistA and to those requesting the information. No GUI applications will be modified or affected in this effort.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                               | Phase / Role | Tasks                                                                                                       | Project Phase (See Schedule) |
|-----|----------------------------------------------------|--------------|-------------------------------------------------------------------------------------------------------------|------------------------------|
| 1   | STS Team                                           | Deployment   | Plan and schedule deployment (including orchestration with vendors)                                         |                              |
| 2   | STS Team                                           | Deployment   | Develop O&M Plan                                                                                            |                              |
| 3   | FO                                                 | Deployment   | Test for operational readiness                                                                              |                              |
| 4   | STS Team / FO                                      | Deployment   | Execute deployment                                                                                          |                              |
| 5   | STS Team / FO                                      | Installation | Plan and schedule installation                                                                              |                              |
| N/A | Regional PM/FIS/OPP PM                             | Installation | Ensure authority to operate and that certificate authority (CA)/security documentation is in place          |                              |
| N/A | Regional PM/FIS/OPP PM/                            | Installation | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes |                              |
| N/A | Regional PM/FIS/OPP PM/ Nat’l Education & Training | Installation | Coordinate training                                                                                         |                              |

Table 2: Software Specifications

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a concurrent online rollout. During IOC testing and after national release, patch PSO\*7\*472 will be distributed via the FORUM Patch Module, and may be deployed at any site without regard to deployment status at other sites.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for a period of thirty days, as depicted in the Master Deployment Schedule.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CTT & DM NDS Medications Patch PSO\*7\*472 deployment.

The PSO\*7\*472 Medications Patch must be manually installed, or manually queued for installation at each VistA instance at which it is deployed, using the standard Kernel Installation Distribution System (KIDS) software. The PSO\*7\*472 Patch should be installed at all VA VistA instances running Outpatient Pharmacy or any of the VistA Pharmacy applications, and will update the M (Mumps) server software on each VistA server.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment topology for the CTT & DM NDS Medications Patch PSO\*7\*472, during IOC testing and after national release is described below.

Figure 1. Deployment Topology (Targeted Architecture)

![](pso-7-472-ctt-and-dm-nds-meds-dibr/002.png)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During IOC testing, CTT & DM NDS Medications Patch PSO\*7\*472 will be deployed at the following sites:

- Great Plains
- Oklahoma City

After National Release, CTT & DM NDS Medications Patch PSO\*7\*472 will be deployed at all sites running the Outpatient Pharmacy v.7.0 application.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special preparation is required by the site prior to deployment.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment of CTT & DM NDS Medications Patch PSO\*7\*472 requires an up to date VistA environment running the Outpatient Pharmacy v.7.0 application.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific deployment or installation features of CTT & DM NDS Medications patch PSO\*7\*472.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT & DM NDS Medications Patch PSO\*7\*472 requires no site hardware specifications during, or prior to deployment.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software   | Make | Version | Configuration | Manufacturer | Other |
|---------------------|------|---------|---------------|--------------|-------|
| Outpatient Pharmacy |      | 7.0     | Standard      | VHA          |       |

Table 3: Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities Table in Section 2 for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No notifications are required for deployment of CTT & DM NDS Medications patch PSO\*7\*472.

#### Deployment/Installation/Back-Out Checklist

| Activity                                                                                                                           | Day | Time | Individual who completed task |
|------------------------------------------------------------------------------------------------------------------------------------|-----|------|-------------------------------|
| Deploy -The Deploy activity is performed when the patch is sent to test site(s) by the development team.                           | TBD | TBD  | TBD                           |
| Install - The Install activity is performed when the patch is installed at the test site(s).                                       | TBD | TBD  | TBD                           |
| Back-Out - The optional Back-Out activity is performed in the event the patch must be uninstalled, or removed, from the test site. | TBD | TBD  | TBD                           |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ordinarily it is recommended that a “Back-up” Local Patch File is created that can be re-installed in the event that a new patch must be backed out. However, this method does not back out Database Definitions (DDs), and as Patch PSO\*7\*472 contains only DDs; there is no need to create a Back-up Local Patch.

### Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*472 does not require any platform installation or preparation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT & DM NDS Medications Patch PSO\*7\*472 is being released as a FORUM Patch via the Patch Module, therefore, the patch must be downloaded from FORUM, and forwarded to the destination site, in the form of a Packman message. There is no new documentation available as this patch does not create any new functionality.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new database is required for the CTT & DM NDS Medications patch PSO\*7\*472.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are required for installation of CTT & DM NDS Medications patch PSO\*7\*472.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are required for installation of CTT & DM NDS Medications Patch PSO\*7\*472.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to National VA Network, as well as the local network of each site to receive CTT & DM NDS Medications patch PSO\*7\*472 is required to perform the installation, as well as authority to create and install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

The installation of Patch PSO\*7\*472 will modify the DRUG INGREDIENTS file (#50.416), the VA GENERIC (#50.6) file, the VA DRUG CLASS file (#50.605), and the VA PRODUCT (#50.68) File.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the Patch \#, PSO\*7\*472.
4.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
5.  Compare Transport Global to Current System - This option will (allow you to view all changes that will be made when this patch is installed. It compares all components of these patch routines, DDs, templates, etc.).
6.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
7.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
8.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' respond NO.
9.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
10. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' respond NO.
11. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of CTT & DM NDS Medications Patch PSO\*7\*472 may be verified by running global listings from the VistA server command line after installation:

D ^%G

Global listings should be performed for the following global nodes:

Global ^DD(50.416,4,0

Global ^DD(50.6,5,0

Global ^DD(50.605,5,0

Global ^DD(50.68,43,0

Example:

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global ^DD(50.416,4,0 -- NOTE: translation in effect

^DD(50.416,4,0)="CODING SYSTEM^50.4164^^4;0"

Global ^DD(50.6,5,0 -- NOTE: translation in effect

^DD(50.6,5,0)="CODING SYSTEM^50.65^^5;0"

Global ^DD(50.605,5,0 -- NOTE: translation in effect

^DD(50.605,5,0)="CODING SYSTEM^50.6055^^5;0"

Global ^DD(50.68,43,0 -- NOTE: translation in effect

^DD(50.68,43,0)="CODING SYSTEM^50.6843^^11;0"

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration is required before or after deployment of CTT & DM NDS Medications Patch PSO\*7\*472.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning is required before or after deployment of CTT & DM NDS Medications Patch PSO\*7\*472.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

The Backout Procedure consists of individually removing each new Data Definition (DD) introduced by the Patch PSO\*7\*472. Since there are no other software components (routines, templates, etc.) contained in the patch, there is no ‘restore’ or backout process involving Kernel Installation and Distribution System (KIDS).

The backout is to be performed by persons with programmer-level access, and in conjunction with the STS Team.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Backout Strategy is to manually delete the new Data Definitions (DDs) introduced with this patch.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The backout should only be done in the event that the facility systems management determines that the Patch PSO\*7\*472 is not appropriate for that facility, and should only be done as a last resort. HPS Clinical 1 team may be consulted if needed.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch PSO\*7\*472.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Facility Systems Management would need to determine patch PSO\*7\*472 is not appropriate for their facility. HPS Clinical 1 team may be consulted if needed.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out PSO\*7\*472, the local facility will not be able to use the Adverse Reaction Tracking package to update VistA allergies and allergy symptoms with standard terminology codes from the respective Standards Development Organizations. HPS Clinical 1 team may be consulted if needed.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility Systems Management has the authority to back-out patch PSO\*7\*472. HPS Clinical 1 team may be consulted if needed.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The backout is to be performed by persons with programmer-level access, and in conjunction with the STS Team. File Manager should be used to delete the new CODING SYSTEM multiple added with PSO\*7\*472, which will automatically also remove sub-fields and data.

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

The following will need to be executed from the programmers prompt (User input depicted below in *bold italicized* font):

Delete CODING SYSTEM multiple and data from DRUG INGREDIENTS (#50.416) file:

> *D P^DI*

> Select OPTION: *MODIFY FILE ATTRIBUTES*

> Do you want to use the screen-mode version? YES// *NO*

> MODIFY WHAT FILE: HDIS FILE/FIELD// *50.416* DRUG INGREDIENTS

> (4951 entries)

> Select FIELD: *CODING SYSTEM* (multiple)

> LABEL: CODING SYSTEM// *@*

> SURE YOU WANT TO DELETE THE ENTIRE 'CODING SYSTEM' FIELD? *Y* (Yes)

> OK TO DELETE 'CODING SYSTEM' FIELDS IN THE EXISTING ENTRIES? Yes// *Y* (Yes).....

Delete Coding System multiple and data from VA GENERIC (#50.6) file:

> *D P^DI*

> Select OPTION: *MODIFY FILE ATTRIBUTES*

> Do you want to use the screen-mode version? YES// *NO*

> MODIFY WHAT FILE: HDIS FILE/FIELD// *50.6* VA GENERIC

> (4948 entries)

> Select FIELD: *CODING SYSTEM* (multiple)

> LABEL: CODING SYSTEM// *@*

> SURE YOU WANT TO DELETE THE ENTIRE 'CODING SYSTEM' FIELD? *Y* (Yes)

> OK TO DELETE 'CODING SYSTEM' FIELDS IN THE EXISTING ENTRIES? Yes// *Y* (Yes).....

Delete Coding System multiple and data from VA DRUG CLASS (#50.605) file:

> *D P^DI*

> Select OPTION: *MODIFY FILE ATTRIBUTES*

> Do you want to use the screen-mode version? YES// *NO*

> MODIFY WHAT FILE: HDIS FILE/FIELD// *50.605* VA DRUG CLASS

> (579 entries)

> Select FIELD: *CODING SYSTEM* (multiple)

> LABEL: CODING SYSTEM// *@*

> SURE YOU WANT TO DELETE THE ENTIRE 'CODING SYSTEM' FIELD? *Y* (Yes)

> OK TO DELETE 'CODING SYSTEM' FIELDS IN THE EXISTING ENTRIES? Yes// *Y* (Yes).....

Delete Coding System multiple and data from VA PRODUCT (#50.68) file:

> *D P^DI*

> Select OPTION: *MODIFY FILE ATTRIBUTES*

> Do you want to use the screen-mode version? YES// *NO*

> MODIFY WHAT FILE: HDIS FILE/FIELD// *50.68* VA PRODUCT

> (27332 entries)

> Select FIELD: *CODING SYSTEM* (multiple)

> LABEL: CODING SYSTEM// *@*

> SURE YOU WANT TO DELETE THE ENTIRE 'CODING SYSTEM' FIELD? *Y* (Yes)

> OK TO DELETE 'CODING SYSTEM' FIELDS IN THE EXISTING ENTRIES? Yes// *Y* (Yes).....

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out Patch PSO\*7\*472, back-out of CTT & DM NDS Medications Patch PSO\*7\*472 may be verified by running a global listings from the VistA server command line after installation. Global listings should be performed for the following global nodes, after which nothing should be listed if back-out was successful:

> Global ^DD(50.416,4,0

> Global ^DD(50.6,5,0

> Global ^DD(50.605,5,0

> Global ^DD(50.68,43,0

Example:

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global ^DD(50.416,4,0 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(50.6,5,0 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(50.605,5,0 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(50.68,43,0 -- NOTE: translation in effect

\<nothing should print\>

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

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

N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A