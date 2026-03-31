---
consolidated_title: "mental health assistant deployment, installation, back-out, and rollback guide"
app_code: YS
doc_type: DIBR
master_source: "YS*5.01*217 Mental Health Assistant Deployment, Installation, Back-Out, and Rollback Guide"
master_pub_date: January 2023
consolidated_from: 6 versions
prior_versions:
  - "YS*5.01*187 Mental Health Assistant Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*204 Mental Health Assistant Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*218 Mental Health Assistant Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*228 Mental Health Assistant Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*238 Mental Health Assistant Deployment, Installation, Back-Out, and Rollback Guide"
---

---
title: |
  Mental Health YS\*5.01\*217

  <span id="_Toc120710156" class="anchor"></span>Deployment, Installation, Back-out, and Rollback Guide
---

![](ys-5-01-217-mental-health-assistant-deployment-installation-back-out-and-rollbac/001.png)

January 2023

Office of Information and Technology (OIT)

Revision History

| Date  | Version | Description | Author           |
|-----------|-------------|-----------------|----------------------|
| 12/1/2022 | 1.0         | Initial Version | Liberty IT Solutions |

<span id="_Toc72323085" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

List of Tables

[Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities [1](#_Toc72323085)](#_Toc72323085)

[Table 2: Acronyms [9](#_Toc72323087)](#_Toc72323087)

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
- [Back-out Procedure](#back-out-procedure)
  - [Back-out Strategy](#back-out-strategy)
  - [Back-out Considerations](#back-out-considerations)
  - [Back-out Criteria](#back-out-criteria)
  - [Back-out Risks](#back-out-risks)
  - [Authority for Back-out](#authority-for-back-out)
  - [Back-out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Appendix A – Acronyms](#appendix-a-acronyms)
This document describes how to deploy and install the patch YS\*5.01\*217 of the Mental Health package, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom Mental Health patch YS\*5.01\*217 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is assumed that this patch is being installed into a fully patched Veterans Health Information System and Technology Architecture (VistA) system. Patches YS\*5.01\*141 and YS\*5.01\*202 must be installed prior to this patch.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all other VistA sites, there are no constraints beyond the installation into an up-to-date VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes the roles and responsibilities associated with the testing and release of YS\*5.01\*217. This application requires both a VistA installation and an update to the web application. The Azure application manager will install the web application part of the patch. The VistA patch will be deployed via the normal PackMan route.

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

The deployment is planned as a simultaneous (National Release) rollout. Once approval has been given to nationally release, YS\*5.01\*217 will be available for installation and deployment at all sites.

Scheduling of test installs, testing, and production deployment will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run during January and February 2023.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the YS\*5.01\*217 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local sites, as well as regional data centers, will need to execute the VistA installation steps during the required installation period to stay synchronized with the updates to the web application.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capability (IOC) sites for verification of functionality. Once testing is completed and approval is given for national release, YS\*5.01\*217 will be deployed to all VistA systems.

The Production IOC testing sites are:

Clement J. Zablocki VAMC (Milwaukee, WI)

Orlando VAMC (Orlando, FL)

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS\*5.01\*217 requires a fully patched VistA system. Patches YS\*5.01\*141 and YS\*5.01\*202 must be installed prior to the installation of YS\*5.01\*217.

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

When YS\*5.01\*217 is released, the released-patch notification will be sent from the National Patch Module to all personnel who have subscribed to notifications for the Mental Health package patch.

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

Select BUILD NAME: YS\*5.01\*217 MENTAL HEALTH

YS217PST value = 9701774

YTQAPI1 value = 33692139

YTQAPI17 value = 5761273

YTQAPI2 value = 33799161

YTQROPT value = 9607623

YTSCAT value = 57710486

YTSCIA value = 5411954

YTSCORE value = 58177918

YTSEDEQ value = 11852660

YTSMCMI4 value = 251755612

YTSMCMIA value = 86005550

done

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of YS\*5.01\*217 requires access to Kernel Installation and Distribution System (KIDS) options to be able to load and install the KIDS build.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu:
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name (YS\*5.01\*217).
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option for each patch contained in the Host File. For each patch you can specify what to backup, the entire Build or just Routines. The backup message can be used to restore just the routines or everything that will restore your system to pre-patch condition.
    3.  You may also elect to use the following options:
        1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
    4.  Select the Install Package(s) option and choose the patch to install (YS\*5.01\*217).
        1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
        2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
        3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

## Post-installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A post-install routine will run to change the name of the ASRS instrument to ASRS-6 and update the CESD instrument with a Total scale. A new instrument category, Eating/Nutrition, will be added. The routine will also set the instrument categories for the EDE-Q, CIA, AD8, NUDESC, SIP-AD-30, SIP-AD-START, and SWEMWBS instruments.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open CPRS and launch the MHA Web application. Create a new assignment on a test patient and verify instruments such as the CIA and EDD-Q are selectable. Also verify that the ASRS instrument is now named ASRS-6. Press the CANCEL button to cancel the assignment.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning required.

# Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch updates the Mental Health Assistant – Web (MHA Web) application. If MHA Web does not perform as desired, it is possible to back out to the previous implementation.

## Back-out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the YS\*5.01\*217 patch is backed out, there will be minimal impact to users. Special consideration will have to be given to deactivating the instruments that were added (CIA and EDE-Q).

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out should only be considered if there is a patient safety issue, if MHA Web no longer functions, or if there is some other catastrophic failure.

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risks vary depending on what is causing the failure of the system. The main risk is that the MHA Web will be unavailable.

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA system manager determines if a back-out of YS\*5.01\*217 should be considered.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines need to be restored to their previous versions:

- YTQAPI1
- YTQAPI17
- YTQAPI2
- YTQROPT
- YTSCAT
- YTSCIA
- YTSEDEQ
- YTSCORE
- YTSMCMI4
- YTSMCMIA

Use the KIDS utility restore the routines backed up in section 4.4, 2B.

\*\*\* NOTE \*\*\*Follow the instrument Deactivation procedure in section 6.5 Rollback Procedure to Drop the CIA and EDE-Q instruments.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open CPRS and launch MHA Web. Click on the + sign to create a new Assignment. Verify that the CIA and EDE-Q instruments are no longer visible.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To rollback this patch, three entries in the MH TESTS AND SURVEYS file need to be updated. The two instruments that were added in this patch need to be set to DROPPED.

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

- CIA
- EDE-Q

> The following example is for the CIA but will be the same for each instrument.

> Log in to VistA.

> Go to the VA FileMan menu

> Go to Enter or Edit File Entries

![](ys-5-01-217-mental-health-assistant-deployment-installation-back-out-and-rollbac/002.png)

At the Input to what File: prompt enter MH TESTS AND SURVEYS

At the EDIT WHICH FIELD prompt enter:

> OPERATIONAL

> LAST EDIT DATE

> LAST EDITED BY

![](ys-5-01-217-mental-health-assistant-deployment-installation-back-out-and-rollbac/003.png)

At the Select MH TESTS AND SURVEYS NAME: prompt enter CIA

At the OPERATIONAL prompt enter DROPPED

At the LAST EDIT DATE prompt enter N for NOW

At the LAST EDITED BY prompt enter your name.

![](ys-5-01-217-mental-health-assistant-deployment-installation-back-out-and-rollbac/004.png)

Repeat this process for the EDE-Q.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go to CPRS and log in. Go to the Tools Menu and launch MHA Web. Click on the plus sign to create a new Assignment. Click on View All Instruments to see the full instrument list. Verify that the CIA and EDE-Q do not appear.

# Appendix A – Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                 |
|-------------|----------------------------------------------------------------|
| ASRS        | Adult ADHD Self-Report Scale                                   |
| CAG         | Citrix Access Gateway                                          |
| CES-D       | Center for Epidemiologic Studies Depression Scale              |
| CIA         | Clinical Impairment Assessment                                 |
| CPRS        | Computerized Patient Record System                             |
| DIBRG       | Deployment, Installation, Back-out, and Rollback Guide         |
| EDE-Q       | Eating Disorder Examination Questionnaire                      |
| IOC         | Initial Operating Capability                                   |
| KIDS        | Kernel Installation and Distribution System                    |
| MHA         | Mental Health Assistant                                        |
| OIT         | Office of Information and Technology                           |
| PIN         | Personal Identification Number                                 |
| PIV         | Personal Identity Verification                                 |
| SQA         | Software Quality Assurance                                     |
| SSOi        | Single Sign-On Integration                                     |
| VA          | Department of Veterans Affairs                                 |
| VAMC        | Veterans Affairs Medical Center                                |
| VIP         | Veteran-focused Integration Process                            |
| VistA       | Veterans Health Information System and Technology Architecture |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: YS*5.01*187 Mental Health Assistant Deployment, Installation, Back-Out, and Rollback Guide

### Configure/Update MHA Web on the CPRS Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This procedure configures or updates VistA so that “MHA Web” appears as a choice on a user’s Tools menu on the CPRS desktop software.

> NOTE: If you already have MHA Web on the CPRS Tools Menu, still look carefully at the command as it has changed to launch MHA Web in its own browser instance.

> MHA Web must be started from the CPRS Tools Menu and should launch in a new browser window rather than appear as an additional tab on an existing browser session if one exists. Each site must decide if Microsoft Edge or Google Chrome will be used for MHA Web.

> Go to the GUI TOOL Menu, Select 4 for System. At the Select Sequence prompt, enter a question mark to see if MHA Web has already been set up in the Tools Menu. If it has, then select that sequence number. If it has not, then select a new sequence number to assign for MHA Web.

- If using Microsoft Edge

> The Name=Command is

> MHA Web=cmd /c start msedge.exe -new-window “https://mha.med.va.gov/app/home?station=\<station number\>&poi=%DFN” 

> You need to substitute \<station number\> with your three-digit VistA instance station number. NOTE: there is only a single space between -new-window and the quoted URL.

- If using Google Chrome

> The Name=Command is

> MHA Web=cmd /c start chrome.exe -new-window “https://mha.med.va.gov/app/home?station=\<station number\>&poi=%DFN” 

> You need to substitute \<station number\> with your three-digit VistA instance station number. NOTE: there is only a single space between -new-window and the quoted URL.

> Example: The example below shows the setup of MHA Web on the CPRS Tools menu from the GUI TOOLS MENU \[ORW TOOL MENU ITEMS\] option:

\<CPM\> Select OE/RR MASTER MENU \<NGOLD\> Option: ^GUI TOOL Menu Items 

 

CPRS GUI Tools Menu may be set for the following: 

 

     1   User          USR    \[choose from NEW PERSON\] 

     2   Location      LOC    \[choose from HOSPITAL LOCATION\] 

     2.5 Service       SRV    \[choose from SERVICE/SECTION\] 

     3   Division      DIV    \[LYNCHBURG (CLL)\] 

     4   System        SYS    \[NGOLD.DEVSLC.FO-SLC.MED.VA.GOV\] 

     9   Package       PKG    \[ORDER ENTRY/RESULTS REPORTING\] 

 

Enter selection: 4  System   NGOLD.DEVSLC.FO-SLC.MED.VA.GOV 

 

 

-- Setting CPRS GUI Tools Menu  for System: NGOLD.DEVSLC.FO-SLC.MED.VA.GOV -- 

Select Sequence: 5 

Are you adding 5 as a new Sequence? Yes// \<enter\>  YES 

 

Sequence: 5// \<enter\>   5 

Name=Command:MHA Web=cmd /c start msedge.exe -new-window “https://mha.med.va.gov/app/home?station=999&poi=%DFN”

Select Sequence: \<enter\> 

> NOTE: 999 is the example VistA Station number.

> In addition to this post-install step, a post-install routine will run to clear out extraneous MCMI4 log data, update the TAG FOR SUICIDE RISK and ROUTINE FOR SUICIDE RISK for the BDI2 and CCSA-DSM5 instruments, and install instrument updates through the Instrument Exchange utility.
