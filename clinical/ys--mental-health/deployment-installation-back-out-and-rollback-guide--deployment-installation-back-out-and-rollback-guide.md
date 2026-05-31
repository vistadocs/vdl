---
title: YS*5.01*202 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*202
group_key: YS:YS:5.01
file_numbers: []
security_keys: []
menu_options: 0
description: '| Date | Version | Description | Author | |------------|-------------|-----------------|----------------------| | 10/05/2022 | 1.0 | Initial Version | Liberty IT Solutions'
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 1735
section_count: 28
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: false
is_stub: false
pub_date: October 2022
revision_count: 1
revision_newest: 10/05/2022
revision_oldest: 10/05/2022
docx_url: https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_202_dibrg.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_202_dibrg.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=78
audit_applied: '2026-05-31'
master_source: YS*5.01*202 Deployment, Installation, Back-Out, and Rollback Guide
master_pub_date: October 2022
consolidated_from: 2 versions
prior_versions:
- YS*5.01*207 Deployment, Installation, Back-Out, and Rollback Guide
consolidated_title: deployment, installation, back-out, and rollback guide
---

![](ys-5-01-202-deployment-installation-back-out-and-rollback-guide/001.png)

October 2022

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description | Author           |
|------------|-------------|-----------------|----------------------|
| 10/05/2022 | 1.0         | Initial Version | Liberty IT Solutions |

<span id="_Toc72323085" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

List of Tables

[Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities [1](#_Toc72323085)](#_Toc72323085)

[Table 2: Acronyms [12](#_Toc72323087)](#_Toc72323087)

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
    - [Facility Specifics (optional)](#facility-specifics-optional)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Post-installation](#post-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
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
- [Appendix A – Acronyms](#appendix-a-acronyms)
> This document describes how to deploy and install the patch YS\*5.01\*202 of the Mental Health package, as well as how to back-out the product and rollback to a previous version or data set.
> This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom Mental Health patch YS\*5.01\*202 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is assumed that this patch is being installed into a fully patched Veterans Health Information System and Technology Architecture (VistA) system. Patches YS\*5.01\*121, YS\*5.01\*130, YS\*5.01\*141, YS\*5.01\*172, and YS\*5.01\*207 must be installed prior to this patch.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For all other VistA sites, there are no constraints beyond the installation into an up-to-date VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following describes the roles and responsibilities associated with the testing and release of YS\*5.01\*202. This application requires both a VistA installation and an update to the web application. The Azure application manager will install the web application part of the patch. The VistA patch will be deployed via the normal PackMan route.

| Team                                     | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|----------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Project Manager                              | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment                           | Design                           |
| Software Quality Assurance (SQA), Test Sites | Deployment       | Test for operational readiness                                                                                      | Test                             |
| Project Manager, Release Manager             | Deployment       | Execute deployment                                                                                                  | Release                          |
| Individual VistA Sites                       | Installation     | Plan and schedule installation                                                                                      | Release                          |
| Azure Manager                                | Installation     | Plan and schedule installation                                                                                      | Release                          |
| Release Manager                              | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Release                          |
| Sustainment Team                             | Post Deployment  | Hardware, Software and System Support                                                                               | Sustain                          |

<span id="_Toc72323087" class="anchor"></span>Table 2: Acronyms

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment is planned as a simultaneous (National Release) rollout. Once approval has been given to nationally release, YS\*5.01\*202 will be available for installation and deployment at all sites.

> Scheduling of test installs, testing, and production deployment will be at the site's discretion. It is anticipated there will be a 30-day compliance period.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment and installation are scheduled to run during August 2022.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the YS\*5.01\*202 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The web part of the application for YS\*5.01\*202 will be deployed to the Azure application server and will be available at each site once the VistA patch is installed. Local sites, as well as regional data centers, will need to execute the VistA installation steps during the required installation period to stay synchronized with the updates to the web application.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The initial deployment will be to Initial Operating Capability (IOC) sites for verification of functionality. Once testing is completed and approval is given for National Release, YS\*5.01\*202 will be deployed to all VistA systems.

> The Production IOC testing sites are:

- Clement J. Zablocki VAMC (Milwaukee, WI)
- Orlando VAMC (Orlando, FL)

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> YS\*5.01\*202 requires a fully patched VistA system. In particular, YS\*5.01\*121, YS\*5.01\*130, YS\*5.01\*141, YS\*5.01\*172, and YS\*5.01\*207 must be installed prior to the installation of YS\*5.01\*202.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No specific facility instructions needed.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No hardware instructions needed.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No software instructions needed.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When YS\*5.01\*202 is released, the released-patch notification will be sent from the National Patch Module to all personnel who have subscribed to notifications for the Mental Health package patch.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no pre-installation requirements.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch can be loaded with users in the system. Installation time will be less than 5 minutes.

> To ensure the integrity of the transport global, use the "Verify Checksums in Transport Global" to compare the checksums with the list that follows:

> The checksums below are new checksums, and

> can be checked with CHECK1^XTSUMBLD.

Select BUILD NAME: YS\*5.01\*202 MENTAL HEALTH

YS202PST value = 31326919

YS202TXT value = 110611824

YSBDD1 value = 143139238

YSBJSON value = 42050108

YSBPREFS value = 52870651

YSBRPC value = 68268540

YSBWHIG2 value = 90905063

YSBWHIGH value = 207104998

YTQRCAT value = 44680325

YTQREST value = 32941761

YTQRQAD2 value = 50997052

YTQRQAD3 value = 82183785

YTQRQAD4 value = 208885212

YTQRQAD5 value = 54727270

YTQRQAD7 value = 205041922

YTQRQAD8 value = 9054687

YTSCAT value = 44396601

YTSEHS14 value = 9892060

YTSFAST value = 3839483

YTSMCMI4 value = 251360451

YTSPEB20 value = 10412071

YTSPEB27 value = 10411704

YTSWBS value = 5723495

YTWJSON value = 78132023

YTWJSONO value = 23348872

YTXCHGI value = 55947879

YTXCHGM value = 75625677

YTXCHGT value = 24969505

done

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The software for this patch is being released using a host file.

> The host file is available at the following location:

> /srv/vista/patches/SOFTWARE/YS_5_01_202.KID

> build.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation of YS\*5.01\*202 requires access to the Kernel Installation and Distribution System (KIDS).

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

1.  Use the Load a Distribution option contained on the Kernel Installation and Distribution System Menu to load the host file.

When prompted to "Enter a Host File:" enter

/srv/vista/patches/SOFTWARE/YS_5_01_202.KID

2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu:
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name (YS\*5.01\*202).
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option for each patch contained in the Host File. For each patch you can specify what to backup, the entire Build or just Routines. The backup message can be used to restore just the routines or everything that will restore your system to pre-patch condition.
    3.  You may also elect to use the following options:
        1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
    4.  Select the Install Package(s) option and choose the patch to install (YS\*5.01\*202).
        1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
        2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
        3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

## Post-installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A post-install routine will run to update the PCL-5, PCL-5 WEEKLY, CSI PARTNER VERSION, CAD-PTSD-DX, and MCMI4 instruments. The post-install will also add instrument categories to CAT-PSYCHOSIS, EHS-14, PEBS-20, PEBS-27, WBS, ASRS, and DAR-5 instruments. The CAT-PTSD, CAT-ADHD, and CAT-SDOH instruments will be dropped. Blank fields in the BASIS-24 instrument will be removed. The CPRS TOOLS link URL for MHA Web will be updated in the ORWT TOOLS MENU Parameter. Finally, a new field in the MH TESTS AND SURVEYS file, INTERPRETIVE TEXT, will be populated for instruments that have text.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open CPRS and launch the MHA Web application. Create a new assignment on a test patient and verify instruments such as the EHS-14, PEBS-20, and PEBS-27 are selectable. Press the CANCEL button to cancel the assignment.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning required.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch updates the Mental Health Assistant – Web (MHA Web) application. If MHA Web does not perform as desired, it is possible to back out to the previous implementation.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the YS\*5.01\*202 patch is backed out, there will be minimal impact to users.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out should only be considered if there is a patient safety issue, if MHA Web no longer functions, or if there is some other catastrophic failure.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risks vary depending on what is causing the failure of the system. The main risk is that the MHA Web will be unavailable.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA system manager determines if a back-out of YS\*5.01\*202 should be considered.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines need to be restored to their previous versions:

- YTQREST
- YTQRCAT
- YTQRQAD2
- YTQRQAD3
- YTQRQAD4
- YTQRQAD5
- YTQRQAD7
- YTQRQAD8
- YTSCAT
- YTSFAST
- YTSMCMI4
- YTWJSON
- YTWJSONO
- YTSCHGI
- YTSCHGM
- YTSCHGT

Use the KIDS utility restore the routines backed up in section 4.5, 2B.

Verify with the Azure application administrator that the web application has been backed out to the previous version.

The link in CPRS will need to be reverted back to its original format. Log into VistA and go to the GUI TOOL MENU. Select SYS for system level. Identify the Sequence number for the MHA Web option. Replace /b/ in the URL with /a/. In the example screenshot below, the Sequence is 14 and the station is 965. At the Replace prompt, enter /b/. At the With prompt, enter /a/ and press \[Enter\].

\*NOTE: In the example above the station is 965. Your actual station number should be substituted.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open CPRS and launch MHA Web. After logging in with your PIV card, look at the URL. Verify that it now has /a/ in it.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To rollback this patch, three entries in the MH TESTS AND SURVEYS file need to be updated. The seven instruments that were added in this patch need to be set to DROPPED. Three instruments that were dropped by this patch and need to be reactivated.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the patch is backed out, the MH TESTS AND SURVEYS file must be rolled back.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By only changing the OPERATIONAL flag, LAST EDIT DATE, and LAST EDITED BY fields in the MH TESTS AND SURVEYS file, the risks are minimal as any existing MH ADMINISTRATION that used these instruments will still be available.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the backout of the patch is authorized, then that same authorization is required for rollback.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Deactivate:  
> </u>

- CAT PSYCHOSIS
- EHS-14
- PEBS-20
- PEBS-27
- WBS
- ASRS
- DAR-5

> The example below is for the CAT-PSYCHOSIS but will be the same for each instrument.

> Log in to VistA.

> Go to the VA FileMan menu

> Go to Enter or Edit File Entries

![](ys-5-01-202-deployment-installation-back-out-and-rollback-guide/002.png)

> At the Input to what File: prompt enter MH TESTS AND SURVEYS

> At the EDIT WHICH FIELD prompt enter:

> OPERATIONAL

> LAST EDIT DATE

> LAST EDITED BY

![](ys-5-01-202-deployment-installation-back-out-and-rollback-guide/003.png)

> At the Select MH TESTS AND SURVEYS NAME: prompt enter CAT-PSYCHOSIS

> At the OPERATIONAL prompt enter DROPPED

> At the LAST EDIT DATE prompt enter N for NOW

> At the LAST EDITED BY prompt enter your name.

![](ys-5-01-202-deployment-installation-back-out-and-rollback-guide/004.png)

> Repeat this process for the EHS-14, PEBS-20, PEBS-27, WBS, ASRS, and DAR-5 instruments.

> <u>Reactivate</u>

- CAT-ADHD
- CAT-SDOH
- CAT-PTSD

> The example below is for the CAT-ADHD but will be the same for each instrument.

> At the Select MH TESTS AND SURVEYS NAME: prompt enter CAT-ADHD

> At the OPERATIONAL prompt enter YES

> At the LAST EDIT DATE prompt enter N for NOW

> At the LAST EDITED BY prompt enter your name.

![](ys-5-01-202-deployment-installation-back-out-and-rollback-guide/005.png)

> Repeat this process for the CAT-SDOH and CAT-PTSD instruments.

> Press ENTER to exit the FileMan edit option.

> Log out as usual.

> All other file updates may remain without rolling back.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go to CPRS and log in. Go to the Tools Menu and launch MHA Web. Click on the plus sign to create a new Assignment. Click on View All Instruments to see the full instrument list. Verify that the CAT-PSYCHOSIS, EHS-14, PEBS-20, PEBS-27, WBS, ASRS, and DAR-5 do not appear and that the CAT-ADHD, CAT-SDOH, and CAT-PTSD instruments appear.

# Appendix A – Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                 |
|-------------|----------------------------------------------------------------|
| CAG         | Citrix Access Gateway                                          |
| CAT         | Computer Adaptive Testing                                      |
| CPRS        | Computerized Patient Record System                             |
| DIBRG       | Deployment, Installation, Back-out, and Rollback Guide         |
| IOC         | Initial Operating Capability                                   |
| KIDS        | Kernel Installation and Distribution System                    |
| MHA         | Mental Health Assistant                                        |
| OIT         | Office of Information and Technology                           |
| PIN         | Personal Identification Number                                 |
| PIV         | Personal Identity Verification                                 |
| SPP         | Suicide Prevention Package                                     |
| SQA         | Software Quality Assurance                                     |
| SSOi        | Single Sign-On Integration                                     |
| VA          | Department of Veterans Affairs                                 |
| VAMC        | Veterans Affairs Medical Center                                |
| VIP         | Veteran-focused Integration Process                            |
| VistA       | Veterans Health Information System and Technology Architecture |