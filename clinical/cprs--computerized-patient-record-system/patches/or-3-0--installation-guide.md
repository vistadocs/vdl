---
title: OR*3*0*626 MOCHA Version 3.0 Combined Build Deployment, Installation, Back-Out, Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*0
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - install
  - installation
  - build
  - patch
  - back
  - order
  - distribution
  - mocha
page_count: 0
word_count: 7480
section_count: 32
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_626_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_626_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>MOCHA 3.0 Pharmacogenomics (PGx) Order Checks Combined Build

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](or-3-0-626-mocha-version-3-0-combined-build-deployment-installation-back-out-rol/001.png)

National Drug File PSN\*4.0\*576Pharmacy Data Management PSS\*1.0\*262

Inpatient Pharmacy PSJ\*5.0\*447

Outpatient Pharmacy PSO\*7.0\*737

Order Entry/Results Reporting OR\*3.0\*626

August 2025Department of Veterans Affairs

Office of Information and Technology (OIT)

Revision History

| Date    | Version | Description | Author |
|-------------|-------------|-----------------|------------|
| August 2025 | 1.0         | Initial Version | Redacted   |

<span id="_Toc199243642" class="anchor"></span>Table 5: Software Specification

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Table of Contents

List of Tables

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
  - [POST-INSTALL MOCHA PGx Clinical Reminder Order Check (CROC) Update](#post-install-mocha-pgx-clinical-reminder-order-check-croc-update)
  - [Installation Verification Procedure](#installation-verification-procedure)
    - [Routine (Code) Installation Verification](#routine-code-installation-verification)
    - [Data Definition Installation Verification](#data-definition-installation-verification)
    - [Data Definition Installation Verification](#data-definition-installation-verification-1)
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
    - [Back-Out Instructions](#back-out-instructions)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the MOCHA 3.0 Pharmacogenomics (PGx) Order Checks combined build (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial Off the Shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the combined build MOCHA 3.0 PGx Order Checks (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSN\*4.0\*396 must be installed BEFORE PSN\*4.0\*576

PSS\*1.0\*253 must be installed BEFORE PSS\*1.0\*262

PSS\*1.0\*254 must be installed BEFORE PSS\*1.0\*262

PSJ\*5.0\*426 must be installed BEFORE PSJ\*5.0\*447

PSO\*7.0\*417 must be installed BEFORE PSO\*7.0\*737

PSO\*7.0\*747 must be installed BEFORE PSO\*7.0\*737

OR\*3.0\*405 must be installed BEFORE OR\*3.0\*626

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199243638" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                                                                                                                                                                         | Phase / Role   | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | Department of Veterans Affairs (VA) Office of Information and Technology (OIT), Health Services Portfolio (HSP) Patient Care Services (PCS), and Program Management Office (PMO) | Deployment         | Plan and schedule deployment                                                                                        | Planning                         |
| 2      | Health Product Support and Field Operations (FO)                                                                                                                                 | Deployment         | Determine and document the roles and responsibilities of those involved in the deployment                           | Planning                         |
| 3      | Field Testing (Initial Operating Capability-IOC), Health Product Support Testing & VIP Release Agent Approval                                                                    | Deployment         | Test for operational readiness                                                                                      | Testing                          |
| 4      | Application Coordinators                                                                                                                                                         | Release Deployment | Application Coordinators release patches                                                                            | Deployment                       |
| 5      | HSP PCS and FO                                                                                                                                                                   | Deployment         | Execute deployment                                                                                                  | Deployment                       |
| 6      | OIT, Development, Security, and Operations (DevSecOps) Infrastructure Operations (IO) and Individual Veterans Administration Medical Centers (VAMCs)                             | Installation       | Plan and schedule installation                                                                                      | Deployment                       |
| 7      | Facility Area Manager and OIT support, which may be local or regional                                                                                                            | Back-out           | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                       |
| 8      | VA OIT, HSP PCS, and the Development Team                                                                                                                                        | Post Deployment    | Hardware, Software and System Support                                                                               | Warranty                         |

<span id="_Toc199243643" class="anchor"></span>Table 6: Deployment/Installation/Back-Out Checklist

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national general availability release. The scheduling of test/mirror installs, testing, and the deployment to production will be at the sites’ discretion.

A national release is planned after testing has been successfully completed at initial operating capability (IOC) test sites.

Deployment will be performed by the local or regional OIT staff and supported by team members from these organizations: FO and Enterprise Operations. Other teams may provide additional support.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for 14 days, as depicted in the master deployment schedule for Pharmacy Operational Updates.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the deployment of the combined build MOCHA 3.0 PGx Order Checks (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626)

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release will be deployed to all VistA instances.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IOC test sites are:

- Durham, NC
- Madison, WI
- Phoenix, AZ
- Shreveport, LA

Upon national release all VAMCs are expected to install this patch prior to or on the compliance date. The software will be distributed through Forum.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

<span id="_Toc199243639" class="anchor"></span>Table 2: Site Preparation

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            | N/A                       | N/A                                         | N/A               | N/A       |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

<span id="_Toc199243640" class="anchor"></span>Table 3: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

<span id="_Toc199243641" class="anchor"></span>Table 4: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   | N/A       | N/A         | N/A               | N/A              | N/A       |

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the following table (Table 5: Software Specifications) which describes the software specifications required at each site prior to deployment.

| Required Software                                                                                       | Make  | Version | Configuration | Manufacturer            | Other |
|---------------------------------------------------------------------------------------------------------|-------|---------|---------------|-------------------------|-------|
| Fully patched National Drug File package within VistA (including PSN\*4.0\*396)                         | VistA | 4.0     | N/A           | Veterans Administration | N/A   |
| Fully patched Pharmacy Data Management package within VistA (including PSS\*1.0\*253 and PSS\*1.0\*254) | VistA | 1.0     | N/A           | Veterans Administration | N/A   |
| Fully patched Inpatient Medications package within VistA (including PSJ\*5.0\*426)                      | VistA | 5.0     | N/A           | Veterans Administration | N/A   |
| Fully patched Outpatient Pharmacy package within VistA (including PSO\*7.0\*417 and PSO\*7.0\*747)      | VistA | 7.0     | N/A           | Veterans Administration | N/A   |
| Fully patched Order Entry/Results Reporting package within VistA (including OR\*3.0\*405)               | VistA | 3.0     | N/A           | Veterans Administration | N/A   |
| VA FileMan                                                                                              | VistA | 22.2    | N/A           | Veterans Administration | N/A   |
| Kernel                                                                                                  | VistA | 8.0     | N/A           | Veterans Administration | N/A   |
| Kernel Toolkit                                                                                          | VistA | 7.3     | N/A           | Veterans Administration | N/A   |
| VA MailMan                                                                                              | VistA | 8       | N/A           | Veterans Administration | N/A   |
|                                                                                                         |       |         |               |                         |       |

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For national release, sites will receive communication that the release has occurred, which will normally be an Action Item or Bulletin.

Sites will use their internal communications to let their users know about upcoming installations and any associated downtime. This is critical as users can often slow the installation process if they are on the system while installers are trying to get the software installed.

Clinical Application Coordinators (CACs), installers, and other site personnel (as determined by the site) will need to coordinate installation dates and times. In addition, other support personnel may need to be consulted – such as the Citrix support, Client Technologies (if required).

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the combined build for MOCHA 3.0 PGx Order Checks (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) which is tracked in the National Patch Module (NPM) in FORUM, nationally to all VAMCs. FORUM automatically tracks the patches as they are installed in the different VAMC production systems as described in the previous section. One can run a report in FORUM to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not installed the patch in their VistA production system as of that moment in time.

Therefore, this information does not need to be manually tracked. The table is included below if manual tracking is desired.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | TBD | TBD  | TBD                           |
| Install  | TBD | TBD  | TBD                           |
| Back-Out | TBD | TBD  | TBD                           |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The combined build for MOCHA 3.0 PGx Order Checks (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) is installable on a fully patched M VistA system and operates on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities which communicate with the underlying operating system and hardware, thereby providing each VistA package independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of the applications involved in this project along with their patch numbers.

APPLICATION/VERSION PATCH

NATIONAL DRUG FILE v4.0 PSN\*4.0\*576

PHARMACY DATA MANAGEMENT v1.0 PSS\*1.0\*262

INPATIENT MEDICATIONS v5.0 PSJ\*5.0\*447

OUTPATIENT PHARMACY v7.0 PSO\*7.0\*737

ORDER ENTRY/RESULTS REPORTING v3.0 OR\*3.0\*626

The VistA patches in this release should be installed into the test/mirror/pre-prod accounts before the production account as is the normal VistA patch installation standard convention. When installing any VistA patch, sites should utilize the option “Backup a Transport Global” to create a backup message of the “Build (including routines)” exported with this patch. Pre- and post-installation checksums are found in the Patch Description in the FORUM NPM.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download and extract files are not applicable for the PSN\*4.0\*576 or PSS\*1.0\*262 patches that are a part of the overall combined build as they are standard PackMan installations.

The patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626 are bundled together into a multi-build for MOCHA 3.0 PGx Order Checks. The file name is MOCHA_3_0_PGX_COMBINED_BUILD_1_0.KID, and after the patches are nationally released the file can be found on the VA’s SFTP download servers in the /srv/vista/patches/SOFTWARE folder.

Documentation can also be found on the VA Software Documentation Library at: [<u>https://www.va.gov/vdl/</u>](https://www.va.gov/vdl/)

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database creation is not applicable for this VistA Patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation scripts are not applicable for this VistA patch.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cron scripts are not applicable for this VistA patch.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install this VistA patch, the patch installer must be an active user on the VistA system and have access to the VistA menu option “Kernel Installation & Distribution System” \[XPD MAIN\] and have VistA security keys XUPROG and XUPROGMODE. Knowledge on how to install VistA patches using the items on this menu option is also a required skill.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The following is the required installation order:

- PSN\*4.0\*576
- PSS\*1.0\*262
- MOCHA 3.0 PGX COMBINED BUILD 1.0

Installation Instructions for PSN\*4.0\*576:

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch name, PSN\*4.0\*576.
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup: the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
        1.  At the Installation option menu, select Backup a Transport Global.
        2.  At the Select INSTALL NAME prompt, enter your build PSN\*4.0\*576.
        3.  When prompted for the following, enter "R" for Routines or "B" for Build.

Select one of the following:

B Build

R Routines

Enter response: Build

4.  When prompted "Do you wish to secure this message? NO//", press \<enter\> and take the default response of "NO".
5.  When prompted with, "Send mail to: Last name, First Name", press \<enter\> to take default recipient. Add any additional recipients.
6.  When prompted with "Select basket to send to: IN//", press \<Enter\> and take the default IN mailbox or select a different mailbox.
3.  You may also elect to use the following options:
    1.  Print Transport Global - This option will allow you to view the components of the Kernel Installation and Distribution System (KIDS) build.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all the components of this patch, such as routines, data dictionaries (DDs), templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
    1.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer 'NO'
    2.  When prompted Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//, answer ‘NO’

> PSN\*4\*576 Post-Installation Summary:

- Populate the PGX ELIGIBLE (#46) field and the PGX SUPPRESSED (#47) field in the VA PRODUCT (#50.68) file with data.
- Populate the PGX ELIGIBLE (#5) field and the PGX SUPPRESSED (#6) field in the DRUG INGREDIENTS (#50.416) file with data.
- Generate a VistA mail message to the patch installer with information about these post-installation tasks.

> **NOTE:** The patch installer should check his/her VistA email after patch installation for the email with the subject "PSN\*4\*576 Post-Install Complete".

This email will indicate if there were any problems encountered during the Post-Install process, and will provide instructions on what to do if there were any problems.

Installation Instructions for PSS\*1.0\*262:

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch name, PSS\*1.0\*262.
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup: the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
        1.  At the Installation option menu, select Backup a Transport Global.
        2.  At the Select INSTALL NAME prompt, enter your build PSS\*1.0\*262.
        3.  When prompted for the following, enter "R" for Routines or "B" for Build.

Select one of the following:

B Build

R Routines

Enter response: Build

4.  When prompted "Do you wish to secure this message? NO//", press \<enter\> and take the default response of "NO".
5.  When prompted with, "Send mail to: Last name, First Name", press \<enter\> to take default recipient. Add any additional recipients.
6.  When prompted with "Select basket to send to: IN//", press \<Enter\> and take the default IN mailbox or select a different mailbox.
3.  You may also elect to use the following options:
    1.  Print Transport Global - This option will allow you to view the components of the Kernel Installation and Distribution System (KIDS) build.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all the components of this patch, such as routines, data dictionaries (DDs), templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
    1.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', press \<enter\> and take the default response of "NO"
    2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer 'NO'
    3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer 'NO'.

> PSS\*1\*262 Post-Installation Summary:

- Add the new PSS PGX-HDR SERVICE entry to the WEB SERVICE (#18.02) file.
- Add the new PSS PGX-HDR SERVER entry to the WEB SERVER(#18.12) file.
- Enable and test the new PSS PGX-HDR SERVICE.
- Create two new entries in the APSP INTERVENTION TYPE (9009032.2) File: PHARMACOGENOMIC HIGH ORDER CHECK and PHARMACOGENOMIC MEDIUM ORDER CHECK.
- Remove the Check Drug Interaction \[PSS CHECK DRUG INTERACTION\] option from the Pharmacy Data Management \[PSS MGR\] Menu option.
- Add the Check Drug Interaction \[PSS CHECK DRUG INTERACTION\] option to the Order Check Management \[PSS ORDER CHECK MANAGEMENT\] Menu Option
- Add the Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option to the Order Check Management \[PSS ORDER CHECK MANAGEMENT\] Menu Option.
- Add the Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option to the Outpatient Pharmacy Manager \[PSO MANAGER\] Menu Option.
- Add the Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option to the Pharmacist Menu \[PSO USER1\] Menu Option.
- Add the Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option to the Unit Dose Medications \[PSJU MGR\] Menu Option.
- Add the Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option to the IV Menu \[PSJI MGR\] Menu Option.
- Add the current Uniform Resource Locator (URL) to the VA PHARMACOGENOMICS URL (#103) field of the PHARMACY SYSTEM (#59.7) file.
- Generate a VistA mail message to the patch installer with information about these post-installation tasks.

> **NOTE:** The patch installer should check his/her VistA email after patch installation for the Post-Install email. This email will indicate if there were any problems

during the post-install process and will provide instructions in the email on what to do if there were any problems. The subject of the email will be one of these two:

PSS\*1\*262 Installation has completed. (This indicates the PSS\*1\*262 Post-Install had no problems, and no further action required)

PSS\*1\*262 Installation has Issues (This indicates the PSS\*1\*262 had issues, and further action is required)

Installation Instructions for the MOCHA 3.0 PGX COMBINED BUILD 1.0:

The patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626 are bundled together into a multi-build for MOCHA 3.0 PGx Order Checks.

The file name is MOCHA_3_0_PGX_COMBINED_BUILD_1_0.KID, and the file can be found on the VA’s SFTP download servers in the /srv/vista/patches/SOFTWARE folder.

1.  Place the KIDS multi-build file MOCHA_3_0_PGX_COMBINED_BUILD_1_0.KID into a local directory and use the KIDS Load a Distribution option to load it into the transport global.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch name or build name (ex. MOCHA 3.0 PGX COMBINED BUILD 1.0).

> NOTE: Using \<spacebar\>\<enter\> will not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build

2.  Select the Backup a Transport Global option to create a backup message. When prompted for Install Name, enter MOCHA 3.0 PGX COMBINED BUILD 1.0. When prompted to backup by either ‘Build (including Routines)’ or ‘Routines Only’, select ‘B’ for ‘Build (including Routines)’ .

> NOTE: Recommend adding “b” to backup multi-build filename for identification as a backup multi-build: MOCHA_3_0_PGX_COMBINED_BUILD_1_0b.KID

3.  Compare Transport Global to Current System - This option will (allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
4.  Verify Checksums in Transport Global - This option allows you to ensure the integrity of the routines that are in the transport global.
5.  From the Installation Menu, select the Install Package(s) option and choose the patch to install (MOCHA 3.0 PGX COMBINED BUILD 1.0).
    1.  Accept the default when prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'
    2.  Accept the default when prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//'

MOCHA 3.0 PGX COMBINED BUILD 1.0 Post-Installation Summary:

> OR\*3\*626 Post-Installation Summary:

- Create two new entries in the CPRS ORDER CHECKS (#100.8) File: PHARMACOGENOMICS HIGH and PHARMACOGENOMICS MODERATE.
- Set both new CPRS ORDER CHECKS to enabled and un-editable, along with setting the appropriate severity to each check.

> **NOTE:** There is no mail message generated after the install of OR\*3\*626. To verify a successful Post-Install, review the install message of the OR\*3\*626 patch using the Install File Print \[XPD PRINT INSTALL FILE\] option located under the Utilities \[XPD UTILITY\] Menu option located under the Kernel Installation and Distribution \[XPD MAIN\] Menu option.

> **NOTE:** There are no Post-install process for patches PSJ\*5\*447 and PSO\*7\*737.

## POST-INSTALL MOCHA PGx Clinical Reminder Order Check (CROC) Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This step should be executed by the Clinical Application Coordinator (CAC). Install the MOCHA PGx clinical reminder order check update following the instructions in the attached MOCHA PGx CROC Update document.

- ![](or-3-0-626-mocha-version-3-0-combined-build-deployment-installation-back-out-rol/002.png)

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful installation can be verified by reviewing the first 2 lines of the routines contained in the patch. The second line will contain the patch number in the \[PATCH LIST\] section.

The option Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] can be run to compare the routine checksums to what is documented in the patch.

### Routine (Code) Installation Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the routine checksums (for the individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and for the multi-build which consists of patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) match the checksum in the patch descriptions. The checksums should have been captured as part of the patch installation step “Verify Checksums in Transport Global”. If checksums were not captured, they may be verified by running the option Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] for each patch, (PSN\*5.0\*576, PSS\*1.0\*262, PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626).

> <u>Example:</u>

> Use the following VistA option:

> CALculate and Show Checksum Values

> This option determines the current Old (CHECK^XTSUMBLD) or New (CHECK1^XTSUMBLD)

> logic checksum of selected routine(s).

> Select one of the following:

> 1 Old

> 2 New

> New or Old Checksums: New//

> New CheckSum

> This option determines the current checksum of selected routine(s).

> The Checksum of the routine is determined as follows:

> 1\. Any comment line with a single semi-colon is presumed to be

> followed by comments and only the line tag will be included.

> 2\. Line 2 will be excluded from the count.

> 3\. The total value of the routine is determined (excluding

> exceptions noted above) by multiplying the ASCII value of each

> character by its position on the line and position of the line in

> the routine being checked.

> Select one of the following:

> P Package

> B Build

> Build from: Build

> This will check the routines from a BUILD file.

> Select BUILD NAME: PSN\*4.0\*576<sup>1</sup>

<sup>1</sup>NOTE: To verify all routine checksums, this must be run FIVE times, once for each BUILD NAME that is a part of the combined build, and the two stand-alone patches:

- PSN\*4.0\*576
- PSS\*1.0\*262
- PSJ\*5.0\*447
- PSO\*7.0\*737
- OR\*3.0\*626

### Data Definition Installation Verification 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Fileman to confirm the following partial data dictionary updates were installed by PSN\*4.0\*576:

- PGX ELIGIBLE (#46) field in the VA PRODUCT (#50.68) file
- PGX SUPPRESSED (#47) field in the VA PRODUCT (#50.68) file
1.  From Fileman, select the DATA DICTIONARY UTILITY menu.
2.  Select the LIST FILE ATTRIBUTES option.
3.  Select the VA PRODUCT (#50.68) file at the prompt ‘START WITH What File’.
4.  Accept the default (VA PRODUCT) at the prompt ‘GO TO What File’.
5.  Accept the default (STANDARD).
6.  Enter “46” at the prompt ‘Start with field:’.
7.  Enter “47” at the prompt ‘Go to field:’.
8.  Accept the blank default at the ‘DEVICE:’ prompt to print to the screen.
9.  Accept the default at the ‘Right Margin:’ prompt.
10. The output should display the new fields installed by PSN\*4.0\*576:

START WITH What File: 50.68 VA PRODUCT

(34014 entries)

GO TO What File: VA PRODUCT// (34014 entries)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD//

Start with field: FIRST// PGX ELIGIBLE

Go to field: PGX SUPPRESSED

DEVICE: Linux Telnet /SSh

STANDARD DATA DICTIONARY \#50.68 -- VA PRODUCT FILE XX/XX/25 PAGE 1

STORED IN ^PSNDF(50.68, (34014 ENTRIES) SITE: XXXX ISC ACCOUNT UCI:XXXX,XXX (VERSION 4.0)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

50.68,46 PGX ELIGIBLE PGX;1 SET (Required) (audited)

'1' FOR YES;

'0' FOR NO;

LAST EDITED: APR 18, 2025

HELP-PROMPT: Enter 'Yes' if you want medication orders for

drugs matched to this VA Product to participate

in Pharmacogenomic (PGx) order checks.

DESCRIPTION: If this field is set to Yes, then any

medication order for a drug matched to this VA

Product will participate in Pharmacogenomic

(PGx) order checks.

TECHNICAL DESCR: This field is set at the national level and is

not locally editable.

AUDIT: YES, ALWAYS

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

CROSS-REFERENCE: 50.68^APGX^MUMPS

1)= I \$G(X) S ^PSNDF(50.68,"APGX",DA)=""

2)= K ^PSNDF(50.68,"APGX",DA)

This cross reference identifies VA Products

eligible for pharmacogenomic order checking.

50.68,47 PGX SUPPRESSED PGX;2 SET (Required) (audited)

'1' FOR YES;

'0' FOR NO;

LAST EDITED: MAR 09, 2024

HELP-PROMPT: Enter 'Yes' if you want medication orders for

profile drugs matched to this VA Product to

participate in suppression rules for PGx order

checks.

DESCRIPTION: If this field is set to Yes, then any profile

medication order for a drug matched to this VA

Product will participate in the suppression

rules for Pharmacogenomic (PGx) order checks.

TECHNICAL DESCR: This field is set at the national level and is

not locally editable.

AUDIT: YES, ALWAYS

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

Use Fileman to confirm the following partial data dictionary updates were installed by PSN\*4.0\*576:

- PGX ELIGIBLE (#5) field in the DRUG INGREDIENTS (#50.416) file
- PGX SUPPRESSED (#6) field in the DRUG INGREDIENTS (#50.416) file
11. From Fileman, select the DATA DICTIONARY UTILITY menu.
12. Select the LIST FILE ATTRIBUTES option.
13. Select the DRUG INGREDIENTS (#50.416) file at the prompt ‘START WITH What File’.
14. Accept the default (DRUG INGREDENTS) at the prompt ‘GO TO What File’.
15. Accept the default (STANDARD).
16. Enter “5” at the prompt ‘Start with field:’.
17. Enter “6” at the prompt ‘Go to field:’.
18. Accept the blank default at the ‘DEVICE:’ prompt to print to the screen.
19. Accept the default at the ‘Right Margin:’ prompt.
20. The output should display the new fields installed by PSN\*4.0\*476:

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH What File: VA PRODUCT// 50.416 DRUG INGREDIENTS

(5713 entries)

GO TO What File: DRUG INGREDIENTS// (5713 entries)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD//

Start with field: FIRST// PGX ELIGIBLE

Go to field: PGX SUPPRESSED

DEVICE: Linux Telnet /SSh

STANDARD DATA DICTIONARY \#50.416 -- DRUG INGREDIENTS FILE XX/XX/25 PAGE 1

STORED IN ^PS(50.416, (5713 ENTRIES) SITE: XXXX ISC ACCOUNT UCI: XXXX,XXX (VERSION 4.0)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

50.416,5 PGX ELIGIBLE PGX;1 SET (Required) (audited)

'1' FOR YES;

'0' FOR NO;

LAST EDITED: MAR 10, 2024

HELP-PROMPT: Enter 'Yes' if you want medication orders for

drugs containing this ingredient to participate

in PGx order checks.

DESCRIPTION: If this field is set to Yes, then any

medication order for a drug containing this

ingredient will participate in Pharmacogenomic

(PGx) order checks.

TECHNICAL DESCR: This field is set at the national level and not

locally editable.

AUDIT: YES, ALWAYS

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

50.416,6 PGX SUPPRESSED PGX;2 SET (Required) (audited)

'1' FOR YES;

'0' FOR NO;

LAST EDITED: MAR 10, 2024

HELP-PROMPT: Enter 'Yes' if you want medication orders for

profile drugs containing this ingredient to

participate in suppression rules for PGx order

checks.

DESCRIPTION: If this field is set to Yes, then any profile

medication order containing this ingredient

will participate in the suppression rules for

Pharmacogenomic (PGx) order checks.

TECHNICAL DESCR: This field is set at the national level and not

locally editable.

AUDIT: YES, ALWAYS

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

### Data Definition Installation Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Fileman to confirm the following new files were installed by PSS\*1.0\*262:

- PHARMACOGENOMIC GENES (#51.26)
- PHARMACOGENOMIC PHENOTYPES (#51.28)
- PHARMACOGENOMIC EMAIL LOG (#51.29)

1\. From Fileman, select the DATA DICTIONARY UTILITY menu.

2\. Select the LIST FILE ATTRIBUTES option.

3\. Select a file number from the list above

4\. Verify that the file displays as selectable<sup>2</sup>

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH What File: DRUG INGREDIENTS// 51.26 PHARMACOGENOMIC GENES

(19 entries)

GO TO What File: PHARMACOGENOMIC GENES//

<sup>2</sup>NOTE: In order to verify all new files were installed, this must be run THREE TIMES, once for each file number (51.26, 51.28, and 51.29)

Use Fileman to confirm the partial data dictionary update in the PHARMACY SYSTEM (#59.7) file of the new VA PHARMACOGENOMICS URL (#103) field was applied properly by PSS\*1.0\*262:

1.  From Fileman, select the DATA DICTIONARY UTILITY menu.
2.  Select the LIST FILE ATTRIBUTES option.
3.  Select the PHARMACY SYSTEM (#59.7) file at the prompt ‘START WITH What File’.
4.  Accept the default (PHARMACY SYSTEM) at the prompt ‘GO TO What File’.
5.  Accept the default (STANDARD).
6.  Enter “103” at the prompt ‘Start with field:’.
7.  Enter “103” at the prompt ‘Go to field:’.
8.  Accept the blank default at the ‘DEVICE:’ prompt to print to the screen.
9.  Accept the default at the ‘Right Margin:’ prompt.
10. The output should display the new field installed by PSS\*1.0\*262:

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH What File: 59.7 PHARMACY SYSTEM

(1 entry)

GO TO What File: PHARMACY SYSTEM// (1 entry)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD//

Start with field: FIRST// 103 VA PHARMACOGENOMICS URL

Go to field: 103 VA PHARMACOGENOMICS URL

DEVICE: Linux Telnet /SSh

STANDARD DATA DICTIONARY \#59.7 -- PHARMACY SYSTEM FILE XX/XX/25 PAGE 1

STORED IN ^PS(59.7, (1 ENTRY) SITE: XXXX ISC SUPPORT ACCOUNT UCI: XXXX,XXX

(VERSION 1.0)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

59.7,103 VA PHARMACOGENOMICS URL PGX;1 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>100!(\$L(X)\<1) X

MAXIMUM LENGTH: 100

LAST EDITED: OCT 27, 2024

HELP-PROMPT: Enter the URL for the VA National

Pharmacogenomics Program (1 to 100 characters).

DESCRIPTION: This is the Uniform Resource Locator (URL) for

the VA National Pharmacogenomics program. This

URL will be used for display when the URL

normally received from the Health Data

Repository (HDR) is not available.

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System configuration is not applicable for this VistA patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database tuning is not applicable for this VistA patch.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings. In the event of a catastrophic failure, the Area Manager may make the decision to backout the patch and rollback any necessary database changes. The Area Manager, working with site personnel, tier 2 product support, and the development team will be involved in the decision. However, the Area Manager will make the final decision.

The back-out procedure for these patches are to install the backup builds created in step 2.b. of the Installation Procedures for the MOCHA 3.0 PGx Combined Build (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626).

> **IMPORTANT:** When install the backups, the backups must be the backups made from the original install of the Mocha 3.0 patches, and the backups must be installed in this order:

MOCHA 3.0 PGX COMBINED BUILD 1.0

PSS\*1\*262

PSN\*4\*576

A follow up Back-Out patch will be nationally released sometime after all the successful backouts have occurred. That patch is PSS\*1\*267. It will export the 2 new entries in the APSP INTERVENTION TYPE (9009032.2) File (PHARMACOGENOMIC HIGH ORDER CHECK and PHARMACOGENOMIC MEDIUM ORDER CHECK) to all sites since it is considered national standard data. That data is not backed out as part of the PSS\*1\*262 backout. All sites will be required to install PSS\*1\*267 once it is released.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out Procedures are only needed if there are major problems (examples include the KIDS notice of incompletion or hard errors) resulting from the installation of this patch. You must have concurrence from Health Product Support (HPS) before a back-out can occur. Enter a ServiceNow ticket to obtain this concurrence.

Although it is unlikely due to care in collecting approved requirements, Software Quality Assurance (SQA) review and multiple testing stages (Unit testing, Component Integration Testing, User Acceptance Testing) a back-out decision due to major issues with this patch could occur during site Mirror Testing, Site Production Testing or after National Release to the Field. The strategy would depend upon the stage of testing when the decision is made. If during Site Production Testing, unless the patch produces catastrophic problems, the normal VistA response would be for a new version of the test patch correcting defects to be produced, retested and upon successfully passing development team testing would be resubmitted to the site for testing. If the defects were not discovered until after national release but during the warranty support period, a new patch will be entered into the National Patch Module on Forum and go through all the necessary testing milestones and reviews.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes implemented in the combined build for MOCHA 3.0 PGx Order Checks (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) should be backed out in their entirety, they are generally interdependent and should not be backed out on an item-by-item basis.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load Testing is not applicable for this VistA patch.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance is detailed in the Pharmacy Operational Updates Jira project site.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It may be decided to back out this patch if the project is canceled, the requested changes implemented by the patch are no longer desired by VA OIT and the Pharmacy Business team, or the patch produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out risks include the current state VistA handling of Inpatient, Outpatient, and CPRS functionality.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any back-out decision should be a joint decision of the Area Manager, the Business Owner (or their representative) and the Program Manager with input from the HSP PCS Application Coordinator, HPS Support, the project development team.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out plan for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch.

Back-Out Procedure prior to National Release

If it is prior to national release, the site will be already working directly with the development team daily and should contact that team. The development team members will have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that development team can quickly address via a new software version. If the site is unsure whom to contact, they may log a ticket or contact Health Product Support - Management Systems Team.

Back-Out Procedure after National Release but during the Warranty Support Period

If a decision to back out is made after national release and within the designated support period, a new patch will be entered into the NPM in Forum and will go through all the necessary milestone reviews, etc. as a patch for a patch. This patch could be defined as an emergency patch, and it could be used to address specific issues pertaining to the original patch or it could be used to restore the build components to their original pre-patch condition.

Back-Out Procedure after National Release but during the Warranty Support Period

After the support period, the VistA Maintenance Program will produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

### Back-Out Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The combined build for MOCHA 3.0 PGx Order Checks (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) contains the following build components:

- Routines
- Data Dictionary (new files)
- Partial Data Dictionary (new fields)

Please log a ServiceNow ticket for assistance in backing out this patch since these installed patches contain components in addition to routines.

If a decision to back out is made during Mirror Testing or Site Production Testing, the routine backup created prior to installation may be used to restore components to their pre-patch condition.

Example: Combined build restoration from backupsMULTI-BUILD restoration from backup:Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: installation

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: /srv/vista/xxx/user/hfs/xxxxx/MOCHA_3_0_PGX_COMBINED_BUILD_1_0b.KID

KIDS Distribution saved on Mar 25, 2025@11:14:03

Comment: Backup of MOCHA 3.0 PGX COMBINED BUILD 1.0, PSJ\*5.0\*447, PSO\*7.

This Distribution contains Transport Globals for the following Package(s):

MOCHA 3.0 PGX COMBINED BUILD 1.0b

PSJ\*5.0\*447b

PSO\*7.0\*737b

OR\*3.0\*626b

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

MOCHA 3.0 PGX COMBINED BUILD 1.0b

PSJ\*5.0\*447b

PSO\*7.0\*737b

OR\*3.0\*626b

Use INSTALL NAME: MOCHA 3.0 PGX COMBINED BUILD 1.0b to install this Distribution

.

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INStallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: INStall Package(s)

Select INSTALL NAME: MOCHA 3.0 PGX COMBINED BUILD 1.0b.0b 3/25/25@11:14:28

=\> Backup of MOCHA 3.0 PGX COMBINED BUILD 1.0, PSJ\*5.0\*447, PSO\*7. ;Crea

This Distribution was loaded on Mar 25, 2025@11:14:28 with header of

Backup of MOCHA 3.0 PGX COMBINED BUILD 1.0, PSJ\*5.0\*447, PSO\*7. ;Created on

Mar 25, 2025@11:14:03

It consisted of the following Install(s):

MOCHA 3.0 PGX COMBINED BUILD 1.0b PSJ\*5.0\*447b PSO\*7.0\*737b OR\*3.0\*626b

Checking Install for Package MOCHA 3.0 PGX COMBINED BUILD 1.0b

Install Questions for MOCHA 3.0 PGX COMBINED BUILD 1.0b

Checking Install for Package PSJ\*5.0\*447b

Install Questions for PSJ\*5.0\*447b

Checking Install for Package PSO\*7.0\*737b

Install Questions for PSO\*7.0\*737b

Checking Install for Package OR\*3.0\*626b

Install Questions for OR\*3.0\*626b

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// Linux Telnet /SSh

--------------------------------------------------------------------------------

Install Started for MOCHA 3.0 PGX COMBINED BUILD 1.0b :

Mar 25, 2025@11:14:46

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:14:46

Install Started for PSJ\*5.0\*447b :

Mar 25, 2025@11:14:46

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:14:46

Updating Routine file...

Updating KIDS files...

PSJ\*5.0\*447b Installed.

Mar 25, 2025@11:14:46

NO Install Message sent

Install Started for PSO\*7.0\*737b :

Mar 25, 2025@11:14:46

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:14:46

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*737b Installed.

Mar 25, 2025@11:14:46

NO Install Message sent

Install Started for OR\*3.0\*626b :

Mar 25, 2025@11:14:46

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:14:46

Running Post-Install Routine: EN^ORY626RR

Disabling the Pharmacogenomics order checks...

Patch OR\*3\*262 rollback successful!

Updating Routine file...

Updating KIDS files...

OR\*3.0\*626b Installed.

Mar 25, 2025@11:14:46

NO Install Message sent

Updating Routine file...

Updating KIDS files...

MOCHA 3.0 PGX COMBINED BUILD 1.0b Installed.

Mar 25, 2025@11:14:46

No link to PACKAGE file

Install Completed

PSS\*1.0\*262 restoration from backup:

Select backup message from local mail system:

Subj: Backup of PSS\*1.0\*262 on Aug 06, 2025 \[#XXXXXX\] 08/06/25@10:37

8883 lines

From: USER,TEST In 'IN' basket. Page 1

-------------------------------------------------------------------------------

\$TXT Created by USER,TEST at XXXX-XXXX.XXX.XX.XXX (KIDS) on Wednesday, 0

8/06/25 at 10:37

> **WARNING:** Installing this backup patch message will install older versions

of routines and Build Components (options, protocols, templates, etc.).

Please verify with the Development Team that it is safe to install.

\$END TXT

\$KID PSS\*1.0\*262b

\*\*INSTALL NAME\*\*

PSS\*1.0\*262b

"BLD",13206,0)

PSS\*1.0\*262b^PHARMACY DATA MANAGEMENT^0^3250806^n

"BLD",13206,1,0)

^^5^5^3250806

"BLD",13206,1,1,0)

Backup of PSS\*1.0\*262 on Aug 06, 2025

"BLD",13206,1,2,0)

Type \<Enter\> to continue or '^' to exit: ^

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: I

1 INSTALL SELECTED ROUTINE(S)

2 INSTALL/CHECK MESSAGE

CHOOSE 1-2: 2 INSTALL/CHECK MESSAGE

Line 8 Message \#304912 Unloading KIDS Distribution PSS\*1.0\*262b

Build PSS\*1.0\*262b has been loaded before, here is when:

PSS\*1.0\*262b Install Completed

was loaded on Jul 17, 2024@11:38:11

PSS\*1.0\*262b Install Completed

was loaded on Mar 04, 2025@14:20:59

PSS\*1.0\*262b Install Completed

was loaded on Mar 25, 2025@11:15:51

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

PSS\*1.0\*262b

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: Installa

tion

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

Select INSTALL NAME: PSS\*1.0\*262b 8/6/25@10:38:05

=\> Backup of PSS\*1.0\*262 on Aug 06, 2025

This Distribution was loaded on Aug 06, 2025@10:38:05 with header of

Backup of PSS\*1.0\*262 on Aug 06, 2025

It consisted of the following Install(s):

PSS\*1.0\*262b

Checking Install for Package PSS\*1.0\*262b

Install Questions for PSS\*1.0\*262b

Incoming Files:

51.26 PHARMACOGENOMIC GENES

> **NOTE:** You already have the 'PHARMACOGENOMIC GENES' File.

51.28 PHARMACOGENOMIC PHENOTYPES

> **NOTE:** You already have the 'PHARMACOGENOMIC PHENOTYPES' File.

51.29 PHARMACOGENOMIC EMAIL LOG

> **NOTE:** You already have the 'PHARMACOGENOMIC EMAIL LOG' File.

59.7 PHARMACY SYSTEM (Partial Definition)

> **NOTE:** You already have the 'PHARMACY SYSTEM' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;9999 Linux Telnet /SSh

--------------------------------------------------------------------------------

Install Started for PSS\*1.0\*262b :

Aug 06, 2025@10:39:20

Build Distribution Date: Aug 06, 2025

Installing Routines:

Aug 06, 2025@10:39:20

Installing Data Dictionaries: .

Aug 06, 2025@10:39:20

Installing PACKAGE COMPONENTS:

Installing OPTION

Aug 06, 2025@10:39:20

Running Post-Install Routine: EN^PSS262RR

Removing the HDR server and HDR web service for MOCHA PGx

PSS PGX-HDR SERVER web server successfully removed.

PSS PGX-HDR SERVICE web service successfully removed.

Adding the new intervention type entries to the APSP INTERVENTION TYPE

(#9009032.3) file:

\- PHARMACOGENOMIC HIGH ORDER CHECK intervention type already exists.

\- PHARMACOGENOMIC MEDIUM ORDER CHECK intervention type already exists.

Deleting VA PHARMACOGENOMICS URL (#103) field from PHARMACY SYSTEM (#59.7) File

Field \#103 deleted from the PHARMACY SYSTEM (#59.7) File

Deleting files 51.26, 51.28, and 51.29

PHARMACOGENOMIC GENES (#51.26) File successfully deleted.

PHARMACOGENOMIC PHENOTYPES (#51.28) File successfully deleted.

PHARMACOGENOMIC EMAIL LOG (#51.29) File successfully deleted.

Restructuring the PSS menus:

PSS CHECK DRUG INTERACTION removed from PSS ORDER CHECK MANAGEMENT....

PSS CHECK DRUG INTERACTION added to the PSS MGR option.

Web Service removal is complete for PSS PGX-HDR SERVICE

APSP intervention type update is complete

Updating Routine file...

Updating KIDS files...

PSS\*1.0\*262b Installed.

Aug 06, 2025@10:39:21

Install Completed

PSN\*4.0\*576 restoration from backup:

Select backup message from local mail system:

Subj: Backup of PSN\*4.0\*576 on Mar 25, 2025 \[#XXXXXX\] 03/25/25@11:11 1739 lines

From: LAST,FIRST In 'IN' basket. Page 1

-------------------------------------------------------------------------------

\$TXT Created by LAST,FIRST at XXXX.FO-BIRM.MED.VA.GOV (KIDS) on Tuesday,

03/25/25 at 11:11

> **WARNING:** Installing this backup patch message will install older versions

of routines and Build Components (options, protocols, templates, etc.).

Please verify with the Development Team that it is safe to install.

\$END TXT

\$KID PSN\*4.0\*576b

\*\*INSTALL NAME\*\*

PSN\*4.0\*576b

"BLD",13189,0)

PSN\*4.0\*576b^NATIONAL DRUG FILE^0^3250325^n

"BLD",13189,1,0)

^^5^5^3250325

"BLD",13189,1,1,0)

Backup of PSN\*4.0\*576 on Mar 25, 2025

"BLD",13189,1,2,0)

"BLD",13189,1,3,0)

Type \<Enter\> to continue or '^' to exit: ^

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

Line 8 Message \#XXXXX Unloading KIDS Distribution PSN\*4.0\*576b

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

PSN\*4.0\*576b

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INStallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: INStall Package(s)

Select INSTALL NAME: PSN\*4.0\*576b 3/25/25@11:15:24

=\> Backup of PSN\*4.0\*576 on Mar 25, 2025

This Distribution was loaded on Mar 25, 2025@11:15:24 with header of

Backup of PSN\*4.0\*576 on Mar 25, 2025

It consisted of the following Install(s):

PSN\*4.0\*576b

Checking Install for Package PSN\*4.0\*576b

Install Questions for PSN\*4.0\*576b

Incoming Files:

50.416 DRUG INGREDIENTS (Partial Definition)

> **NOTE:** You already have the 'DRUG INGREDIENTS' File.

50.68 VA PRODUCT (Partial Definition)

> **NOTE:** You already have the 'VA PRODUCT' File.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// Linux Telnet /SSh

--------------------------------------------------------------------------------

Install Started for PSN\*4.0\*576b :

Mar 25, 2025@11:16:11

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:16:11

Running Post-Install Routine: EN^PSN576RR

Deleting PGx data from the DRUG INGREDIENT (#50.416) File...

Deleting PGx fields from the DRUG INGREDIENT (#50.416) File

PGX ELIGIBLE (#5) Field successfully deleted.

PGX SUPPRESSED (#6) Field successfully deleted.

Deleting PGx data from the VA PRODUCT (#50.68) File

Deleting PGx fields from the VA PRODUCT (#50.68) File

PGX ELIGIBLE (#46) Field successfully deleted.

PGX SUPPRESSED (#47) Field successfully deleted.

Updating Routine file...

Updating KIDS files...

PSN\*4.0\*576b Installed.

Mar 25, 2025@11:16:11

Install Completed

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out may only be performed by installing the patch back-ups. After back-out, testing must be conducted to verify the back-out acted as expected, as defined together with the team the site contacted in section 5.5.

Successful back-out can be confirmed by verification that the routine checksums have been restored to their pre-patch state, and the new components have been removed.

Backout Verification Steps

Routines:

Verify that the routine checksums for the combined build for MOCHA 3.0 PGx Order Checks (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) match the checksums captured prior to installing the patches. The ‘pre’ checksums should have been captured as part of the patch pre-installation steps. The current (post back-out) routine checksums may be verified by running the option Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] from for all patches [(see Routine Installation Verification section 4.8.1.)](#routine-code-installation-verification).

Data Dictionary:

Use Fileman to confirm that the partial data dictionary updates that were installed by PSN\*4.0\*576:

- PGX ELIGIBLE (#46) field in the VA PRODUCT (#50.68) file
- PGX SUPPRESSED (#47) field in the VA PRODUCT (#50.68) file
- PGX ELIGIBLE (#5) field in the DRUG INGREDIENTS (#50.416) file
- PGX SUPPRESSED (#6) field in the DRUG INGREDIENTS (#50.416) file

AND that the following data dictionary updates that were installed by PSS\*1.0\*262:

- PHARMACOGENOMIC GENES (#51.26) - NEW
- PHARMACOGENOMIC PHENOTYPES (#51.28) - NEW
- PHARMACOGENOMIC EMAIL LOG (#51.29) – NEW
- VA PHARMACOGENOMICS URL (#103) field in the PHARMACY SYSTEM (#59.7) file - PARTIAL

no longer exist. These data dictionary restorations may be verified using the Fileman option LIST FILE ATTRIBUTES in the DATA DICTIONARY UTILITY menu [(see Data Dictionary Verification starting in section 4.8.2).](#data-definition-installation-verification)

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.