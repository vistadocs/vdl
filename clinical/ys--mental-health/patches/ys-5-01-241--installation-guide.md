---
title: YS*5.01*241 (Emergency Patch) Mental Health Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: (Emergency Patch) Mental Health
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*241
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - back
  - installation
  - rollback
  - procedure
  - patch
  - deployment
  - site
  - verification
page_count: 0
word_count: 1449
section_count: 27
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: October 2023
revision_count: 1
revision_newest: 09/21/2023
revision_oldest: 09/21/2023
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_241_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_241_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

---
title: |
  Mental Health YS\*5.01\*241

  *(Emergency Patch)*

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](ys-5-01-241-emergency-patch-mental-health-deployment-installation-back-out-and-r/001.png)

October 2023

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description | Author          |
|------------|-------------|-----------------|---------------------|
| 09/21/2023 | 1.0         | Initial Version | Booz Allen Hamilton |

<span id="_Toc72323085" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

List of Tables

[Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities [1](#_Toc72323085)](#_Toc72323085)

[Table 2: Acronyms [8](#_Toc72323087)](#_Toc72323087)

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
> This document describes how to deploy and install the patch YS\*5.01\*241 of the Mental Health package, as well as how to back-out the product and rollback to a previous version or data set.
> This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom Mental Health patch YS\*5.01\*241 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is assumed that this patch is being installed into a fully patched Veterans Health Information System and Technology Architecture (VistA) system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For all other VistA sites, there are no constraints beyond the installation into an up-to-date VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following describes the roles and responsibilities associated with the testing and release of YS\*5.01\*241. This application requires both a VistA installation and an update to the web application. The Azure application manager will install the web application part of the patch. The VistA patch will be deployed via the normal PackMan route.

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

> The deployment is planned as a simultaneous (National Release) rollout. Once approval has been given to nationally release, YS\*5.01\*241 will be available for installation and deployment at all sites.

> Scheduling of test installs, testing, and production deployment will be at the site’s discretion. It is anticipated there will be a 7-day compliance period.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment and installation are scheduled to run during September and October 2023.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the YS\*5.01\*241 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The web part of the application for YS\*5.01\*241 will be deployed to the Azure application server and will be available at each site once the VistA patch is installed. Local sites, as well as regional data centers, will need to execute the VistA installation steps during the required installation period to stay synchronized with the updates to the web application.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The initial deployment will be to Initial Operating Capability (IOC) sites for verification of functionality. Once testing is completed and approval is given for national release, YS\*5.01\*241 will be deployed to all VistA systems.

> The Production IOC testing sites are:

- Clement J. Zablocki VAMC (Milwaukee, WI)
- Orlando VAMC (Orlando, FL)
- St. Louis VAMC (St. Louis, MO)

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> YS\*5.01\*241 requires a fully patched VistA system.

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

> When YS\*5.01\*241 is released, the released-patch notification will be sent from the National Patch Module to all personnel who have subscribed to notifications for the Mental Health package patch.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no pre-installation requirements.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch can be loaded with users in the system. Installation time will be less than 5 minutes.

> To ensure the integrity of the transport global, use the “Verify Checksums in Transport Global” to compare the checksums with the list that follows:

> The checksums below are new checksums, and

> can be checked with CHECK1^XTSUMBLD.

Select BUILD NAME: YS\*5.01\*241 MENTAL HEALTH

YS241PST value = 2617793

YTSWBS2 value = 4474781

done

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation of YS\*5.01\*241 requires access to Kernel Installation and Distribution System (KIDS) options to be able to load and install the KIDS build.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu:
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME, enter the patch or build name (YS\*5.01\*241).
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option for each patch contained in the Host File. For each patch you can specify what to backup, the entire Build or just Routines. The backup message can be used to restore just the routines or everything that will restore your system to pre-patch condition.
    3.  You may also elect to use the following options:
        1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
    4.  Select the Install Package(s) option and choose the patch to install (YS\*5.01\*241).
        1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
        2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
        3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

## Post-installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A post-install routine will run to add the appropriate categories to the WBS_V2 instrument. It also deactivates the previous version of the instrument, Well-Being Signs (WBS).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open Computerized Patient Record System (CPRS) and launch the Mental Health Assistant (MHA) application. Click on the + icon to create a new assignment. Verify that the WBS_V2 now shows up under Screening and Quality of Life. Verify that the previous version, WBS, no longer shows.

Logout of the application.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning required.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch updates the MHA application. If MHA does not perform as desired, it is possible to back out to the previous implementation.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the YS\*5.01\*241 patch is backed out, there will be minimal impact to users.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out should only be considered if there is a patient safety issue, if MHA no longer functions or if there is some other catastrophic failure.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risks vary depending on what is causing the failure of the system. The main risk is that the MHA will be unavailable.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA system manager determines if a back-out of YS\*5.01\*241 should be considered.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds one new routine that does not need to be backed out.

\*\*\* NOTE \*\*\*

> Follow the instrument Deactivation procedure in Section 6.5 Rollback Procedure to drop the WBS_V2 instrument and reactivate the WBS instrument before executing the Back-out Verification Procedure.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open CPRS and launch MHA Web. Click on the + sign to create a new Assignment. Verify that the WBS_V2 instrument is no longer visible and that the WBS is now showing.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To rollback this patch, two entries in the MH TESTS AND SURVEYS file need to be updated. The OPERATIONAL field for the WBS_V2 needs to be set to DROPPED and set to Yes for the WBS.

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

> <u>Deactivate:</u>

- WBS_V2

> The following example is for the WBS_V2 instrument.

> Log in to VistA.

> Go to the VA FileMan menu

> Go to Enter or Edit File Entries

![](ys-5-01-241-emergency-patch-mental-health-deployment-installation-back-out-and-r/002.png)

> At the Input to what File: prompt enter MH TESTS AND SURVEYS

> At the EDIT WHICH FIELD prompt enter:

> OPERATIONAL

> LAST EDIT DATE

> LAST EDITED BY

![](ys-5-01-241-emergency-patch-mental-health-deployment-installation-back-out-and-r/003.png)

> At the Select MH TESTS AND SURVEYS NAME: prompt enter WBS_V2

> At the OPERATIONAL prompt enter DROPPED

> At the LAST EDIT DATE prompt enter N for NOW

> At the LAST EDITED BY prompt enter your name.

![](ys-5-01-241-emergency-patch-mental-health-deployment-installation-back-out-and-r/004.png)

> Do the same procedure for the WBS instrument but change the OPERATIONAL status from DROPPED to YES.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open CPRS and launch the MHA Web application. Create a new assignment on a test patient and verify that the WBS_V2 instrument does not appear in the instrument list and that WBS does appear. Press the CANCEL button to cancel the assignment.

# Appendix A – Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                 |
|-------------|----------------------------------------------------------------|
| IOC         | Initial Operating Capability                                   |
| KIDS        | Kernel Installation and Distribution System                    |
| MH          | Mental Health                                                  |
| MHA         | Mental Health Assistant                                        |
| OIT         | Office of Information and Technology                           |
| SQA         | Software Quality Assurance                                     |
| VA          | Department of Veterans Affairs                                 |
| VAMC        | Veterans Affairs Medical Center                                |
| VistA       | Veterans Health Information System and Technology Architecture |
| WBS         | Well-Being Signs                                               |
| WBS_V2      | Well-Being Signs Version 2                                     |

AcronymsList of Acronyms used thorughout this document