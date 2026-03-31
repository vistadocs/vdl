---
title: YS*5.01*182 Mental Health Deployment, Installation, Back-out & Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Mental Health Deployment, Installation, Back-out & Rollback Guide
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*182
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - rollback
  - backout
  - procedure
  - routine
  - deployment
  - patch
  - health
page_count: 0
word_count: 2008
section_count: 27
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: October 2021
revision_count: 1
revision_newest: 10/18/2021
revision_oldest: 10/18/2021
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_182_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys_5_01_182_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Mental Health YS\*5.01\*182

  Deployment, Installation, Backout, and Rollback Guide
---

![](ys-5-01-182-mental-health-deployment-installation-back-out-rollback-guide/001.png)

October 2021

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description | Author           |
|------------|-------------|-----------------|----------------------|
| 10/18/2021 | 1.0         | Initial Version | Liberty IT Solutions |

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
    - [Facility Specifics (optional)](#facility-specifics-optional)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Backout Procedure](#backout-procedure)
  - [Backout Strategy](#backout-strategy)
  - [Backout Considerations](#backout-considerations)
  - [Backout Criteria](#backout-criteria)
  - [Backout Risks](#backout-risks)
  - [Authority for Backout](#authority-for-backout)
  - [Backout Procedure](#backout-procedure-1)
  - [Backout Verification Procedure](#backout-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Appendix A - Acronyms](#appendix-a-acronyms)
This document describes how to deploy and install the patch YS\*5.01\*182 of the Mental Health package, as well as how to back out the product and roll back to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom Mental Health patch YS\*5.01\*182 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is assumed that this patch is being installed into a fully patched Veterans Health Information System and Technology Architecture (VistA) system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints beyond the installation into an up-to-date VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes the roles and responsibilities associated with the testing and release of YS\*5.01\*182. This is a VistA patch that will be deployed via the normal Mailman route.

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| Team                                     | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|----------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Project Manager                              | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          | Design                           |
| Software Quality Assurance (SQA), Test Sites | Deployment       | Test for operational readiness                                                                                      | Test                             |
| Project Manager, Release Manager             | Deployment       | Execute deployment                                                                                                  | Release                          |
| Regional IT                                  | Installation     | Plan and schedule installation                                                                                      | Release                          |
| Release Manager                              | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Release                          |
| Sustainment Team                             | Post Deployment  | Hardware, Software and System Support                                                                               | Sustain                          |

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a simultaneous (National Release) rollout. Once approval has been given to nationally release, YS\*5.01\*182 will be available for installation and deployment at all sites.

Scheduling of test installs, testing, and production deployment will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run during September 2021.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the YS\*5.01\*182 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS\*5.01\*182 will be deployed to each VistA instance. This includes local sites as well as regional data centers. A corresponding update to the MHA Web application will be made in the Azure VA Enterprise Cloud.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capability (IOC) sites for verification of functionality. Once testing is completed and approval is given for national release, YS\*5.01\*182 will be deployed to all VistA systems.

The Production IOC testing sites are:

- Clement J. Zablocki VAMC (Milwaukee, WI)
- Orlando VAMC (Orlando, FL)

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS\*5.01\*182 requires a fully patched VistA system.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No specific facility instructions needed.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No hardware instructions needed.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No software instructions needed.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When YS\*5.01\*182 is released, the released-patch notification will be sent from the National Patch Module to all personnel who have subscribed to notifications for the Mental Health package.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no pre-installation requirements.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can be loaded with users in the system. Installation time will be less than 5 minutes.

To ensure the integrity of the transport global, use the “Verify Checksums in Transport Global” to compare the checksums with the list that follows:

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

Routine Name: YS182PST Before: n/a After: B6355081 \*\*182\*\*

Routine Name: YTQAPI Before: B18133059 After: B18593897 \*\*85,130,141,182\*\*

Routine Name: YTQRCAT Before: n/a After: B42497178 \*\*182\*\*

Routine Name: YTQREST Before: B16134782 After: B18216959 \*\*158,178,182\*\*

Routine Name: YTQREST0 Before: B7781538 After: B8623741 \*\*130,178,182\*\*

Routine Name: YTQRIS Before: B90480805 After: B99568712 \*\*130,141,182\*\*

Routine Name: YTQRQAD1 Before: B87154790 After: B94482754 \*\*130,141,178,182\*\*

Routine Name: YTQRQAD2 Before: B45041984 After: B46192834 \*\*130,141,173,178,182\*\*

Routine Name: YTQRQAD3 Before: B40827460 After: B42257210 \*\*130,141,158,178,182\*\*

Routine Name: YTQRQAD4 Before: B97950328 After: B99761746 \*\*158,178,182\*\*

Routine Name: YTQRQAD5 Before: B53729604 After: B48936796 \*\*158,178,182\*\*

Routine Name: YTSCAT Before: n/a After: B37650998 \*\*182\*\*

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of YS\*5.01\*182 requires access to Kernel Installation and Distribution System (KIDS) options to be able to load and install the KIDS build.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pre/Post Installation Overview:

> The post-install will apply updates to mental health instrument files.

> The post installation routine, YS182PST, may be deleted after the

> installation completes

> Pre-Installation Instructions:

> This patch may be installed with users on the system although it is

> recommended that it be installed during non-peak hours to minimize

> potential disruption to users. This patch should take less than 5

> minutes to install.

> Installation Instructions:

> 1\. Choose the PackMan message containing this build. Then select

> the INSTALL/CHECK MESSAGE PackMan option to load the build.

> 2\. From the Kernel Installation and Distribution System Menu,

> select the Installation Menu. From this menu,

> A. Select the Verify Checksums in Transport Global

> option to confirm the integrity of the routines that

> are in the transport global. When prompted for the

> INSTALL NAME enter the patch or build name.

> (YS\*5.01\*182)

> NOTE: Using \<spacebar\>\<enter\> will not bring up a

> Multi-Package build even if it was loaded

> immediately before this step. It will only

> bring up the last patch in the build.

> B. Select the Backup a Transport Global option to create

> a backup message. You must use this option and specify

> what to backup; the entire Build or just Routines.

> The backup message can be used to restore the routines

> and components of the build to the pre-patch condition.

> i\. At the Installation option menu, select Backup

> a Transport Global

> ii\. At the Select INSTALL NAME prompt, enter your

> build YS\*5.01\*182

> iii\. When prompted for the following, enter "R" for

> Routines or "B" for Build.

> Select one of the following:

> B Build

> R Routines

> Enter response: Build

> iv\. When prompted "Do you wish to secure this message? NO//",

> press \<enter\> and take the default response of "NO".

> v\. When prompted with, "Send mail to: Last name, First

> Name", press \<enter\> to take default recipient. Add

> any additional recipients.

> vi\. When prompted with "Select basket to send to: IN//",

> press \<enter\> and take the default IN mailbox or select

> a different mailbox.

> C. You may also elect to use the following options:

> i\. Print Transport Global - This option will allow

> you to view the components of the KIDS build.

> ii\. Compare Transport Global to Current System - This

> option will allow you to view all changes that will

> be made when this patch is installed. It compares

> all of the components of this patch, such as

> routines, DDs, templates, etc.

> D. Select the Install Package(s) option and choose the

> patch to install.

> i\. If prompted 'Want KIDS to Rebuild Menu Trees Upon

> Completion of Install? NO//', answer NO.

> ii\. When prompted 'Want KIDS to INHIBIT LOGONs during the

> install? NO//', answer NO.

> iii\. When prompted 'Want to DISABLE Scheduled Options, Menu

> Options, and Protocols? NO//', answer NO.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds support for Computerized Adaptive Testing (CAT). You may verify installation by looking in the MH TESTS AND SURVEYS file (#601.71) for new entries that begin with “CAT-“.

VA FileMan 22.2

Select OPTION: INQUIRE TO FILE ENTRIES

Output from what File: MH TESTS AND SURVEYS// (265 entries)

Select MH TESTS AND SURVEYS NAME: CAT-

1 CAT-ADHD

2 CAT-ANX

3 CAT-CAD Interview

4 CAT-DEP

5 CAT-MANIA-HYPOMANIA

etc. . . .

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application versions supported by this document are:

- MHA-Web v1.2.23a
- Mental Health Patient Entry v1.1.7a

Note that the Windows version of MHA, MHA 1.0.3.86, does not support the new instruments in this patch. The CAT instruments are only supported in a web browser.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning required.

# Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Backout Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch updates the Mental Health database with all new records that support CAT. The backout procedure will leave these records in place, but inoperative since they pertain only to those instruments. If there is a compelling reason to back out the new instrument records themselves, you will need to contact the development team for a patch. The backout procedure below will restore MHA to its state prior to the patch installation.

## Backout Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the routines related to this patch are removed, CAT will be unavailable in MHA Web and the installation of future patches may cause unpredictable results. Users will not have access to new CAT interviews.

## Backout Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out should only be considered if there is a patient safety issue, if MHA or MHA Web no longer functions, or if there is some other catastrophic failure.

## Backout Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risks vary depending on what is causing the failure of the system. The main risk is that the new instruments will be unavailable.

## Authority for Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA system manager determines if a back-out of YS\*5.01\*182 should be considered.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back out routines, you must have already selected the "Backup a Transport Global" option during the installation process. To restore the previous routines:

1.  Choose the PackMan message containing the backup you created during installation.
2.  Invoke the INSTALL/CHECK MESSAGE PackMan option.
3.  Answer YES when prompted: Warning: Installing this message will cause a permanent update of globals and routines. Do you really want to do this? NO// YES
4.  The routines that were saved in the message will now be restored.

Disable all entries that begin with “CAT-“ or “CAD-“ by editing the OPERATIONAL field (#10) and the LAST EDIT DATE field (#18) in the MH TESTS AND SURVEYS file (#601.71). Set OPERATIONAL to "Dropped" and set LAST EDIT DATE to "Now".

## Backout Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the backout procedure, use the option “First Line Routine Print” (XU FIRST LINE PRINT) to make sure the routines no longer show patch 182 in the patch list:

PRINTS FIRST LINES

All Routines? No =\> No

Routine: YTQAPI

Routine: YTQREST

Routine: YTQREST0

Routine: YTQRIS

Routine: YTQRQAD1

Routine: YTQRQAD2

Routine: YTQRQAD3

Routine: YTQRQAD4

Routine:

8 routines

(A)lpha, (D)ate ,(P)atched, OR (S)ize ORDER: A//

Include line (2), Include lines 2&(3), (N)one: None//2

DEVICE: HOME// PSEUDO-TERMINAL SLAVE Right Margin: 80//

FIRST LINE LIST UCI: SPPUAT,SPPUAT 07/28/2021

YTQAPI ;ASF/ALB - MHQ REMOTE PROCEEDURES ; 4/3/07 10:36am

;;5.01;MENTAL HEALTH;\*\*85,130,141\*\*;Dec 30, 1994;Build 85

YTQREST ;SLC/KCM - RESTful API front controller ; 1/25/2017

;;5.01;MENTAL HEALTH;\*\*158,178\*\*;Dec 30, 1994;Build 7

YTQREST0 ;SLC/KCM - RESTful API front controller v0 ; 1/25/2017

;;5.01;MENTAL HEALTH;\*\*130,178\*\*;Dec 30, 1994;Build 7

YTQRIS ;SLC/KCM - Instrument Selection RPC's ; 1/25/2017

;;5.01;MENTAL HEALTH;\*\*130,141\*\*;Dec 30, 1994;Build 85

YTQRQAD1 ;SLC/KCM - RESTful Calls to handle MHA assignments ; 1/25/2017

;;5.01;MENTAL HEALTH;\*\*130,141,178\*\*;Dec 30, 1994;Build 7

YTQRQAD2 ;SLC/KCM - RESTful Calls to set/get MHA administrations ; 1/25/2017

;;5.01;MENTAL HEALTH;\*\*130,141,173,178\*\*;Dec 30, 1994;Build 7

YTQRQAD3 ;SLC/KCM - RESTful Calls to set/get MHA administrations ; 1/25/2017

;;5.01;MENTAL HEALTH;\*\*130,141,158,178\*\*;Dec 30, 1994;Build 7

YTQRQAD4 ;ISP/MJB - RESTful Calls to handle MHA lists ; 1/25/2017

;;5.01;MENTAL HEALTH;\*\*158,178\*\*;Dec 30, 1994;Build 7

8 ROUTINES

Also, run MHA Web, select the + button to assign assessments, and verify that the instruments beginning with “CAT-“ or “CAD-“ do not appear in the list of checkboxes on the left:

![](ys-5-01-182-mental-health-deployment-installation-back-out-rollback-guide/002.png)

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only additional data that one might roll back after installation of this patch would be the results of CAT interviews administered after the patch is installed, this is not recommended. If it is necessary, please contact the development team for assistance and a possible patch.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A rollback would be considered if there is erroneous patient data related to CAT interviews.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A rollback could cause the loss of patient information.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA system manager determines if a rollback of patient data created by CAT interviews because of YS\*5.01\*182 should be considered.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please contact the development team for assistance and a possible patch.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the rollback by ensuring that the patient information is now correct.

# Appendix A - Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                     |
|---------|----------------------------------------------------------------|
| CAG     | Citrix Access Gateway                                          |
| CAD     | Computerized Adaptive Diagnosis                                |
| CAT     | Computerized Adaptive Testing                                  |
| DIBRG   | Deployment, Installation, Back-out, and Rollback Guide         |
| IOC     | Initial Operating Capability                                   |
| KIDS    | Kernel Installation and Distribution System                    |
| MHA     | Mental Health Assistant                                        |
| OIT     | Office of Information and Technology                           |
| PIN     | Personal Identification Number                                 |
| PIV     | Personal Identity Verification                                 |
| SPP     | Suicide Prevention Package                                     |
| SQA     | Software Quality Assurance                                     |
| SSOi    | Single Sign-On Integration                                     |
| VA      | Department of Veterans Affairs                                 |
| VAMC    | Veterans Affairs Medical Center                                |
| VIP     | Veteran-focused Integration Process                            |
| VistA   | Veterans Health Information System and Technology Architecture |

AcronymsAcronyms used throughout this document.