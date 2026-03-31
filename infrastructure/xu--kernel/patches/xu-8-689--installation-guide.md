---
title: XU*8*689 Deployment, Installation, Backout, and Rollback Guide (DIBRG)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: (DIBRG)
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8
patch_id: XU*8*689
group_key: "XU:XU:8"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - install
  - patch
  - backout
  - build
  - rollback
  - procedure
  - routine
page_count: 0
word_count: 3864
section_count: 30
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu_8_p689_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu_8_p689_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Pharmacy Operational Updates Project (POU) XU\*8.0\*689

  Deployment, Installation, Backout, and Rollback Guide (DIBRG)
---

![](xu-8-689-deployment-installation-backout-and-rollback-guide-dibrg/001.png)

June 2023

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date      | Revision | Description     | Author   |
|-----------|----------|-----------------|----------|
| June 2023 | 1.0      | Initial version | Redacted |

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
  - [Resources](#resources-1)
    - [Hardware](#hardware-1)
    - [Software](#software-1)
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
    - [Installation Instructions](#installation-instructions)
  - [Post-Installation Steps and Installation Verification Procedures](#post-installation-steps-and-installation-verification-procedures)
  - [System Configuration](#system-configuration)
- [Backout Procedure](#backout-procedure)
  - [Backout Strategy](#backout-strategy)
  - [Backout Considerations](#backout-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Backout Criteria](#backout-criteria)
  - [Backout Risks](#backout-risks)
  - [Authority for Backout](#authority-for-backout)
  - [Backout Procedure](#backout-procedure-1)
    - [Backout Instructions](#backout-instructions)
  - [Backout Verification Procedure](#backout-verification-procedure)
    - [Routines](#routines)
    - [Options](#options)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to download install the Pharmacy Operations project’s VistA Patch XU\*8\*689, as well as how to backout the patch and rollback to a previous version or data set. This patch implements enhancements that enable multiple Drug Enforcement Administration (DEA) Numbers to be assigned to a prescriber.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a document that describes how, where, and when VistA Patch XU\*8.0\*689 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources and includes a communications plan with the rollout schedule. Specific instructions for installation, backout, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VistA patches must be installed at the site:

XU\*8\*548

XU\*8\*551

XU\*8\*688

XU\*8\*751

XU\*8\*765

XU\*8\*774

> **WARNING:** The DEA multi-package host file PSO_545_PSJ_372_OR_499.KID containing PSO\*7.0\*545, OR\*3.0\*499, and PSJ\*5.0\*372 must be installed IMMEDIATELY after installing this patch (XU\*8.0\*689). Controlled Substance medication ordering will be adversely affected if XU\*8.0\*689 is installed without also installing the DEA multi-package host file. See the PSO\*7.0\*545 Patch Description and DIBRG for more details.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                       | Phase/Role      | Tasks                                                                                                                |
|-----|----------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------|
| 1   | Field Operations (FO)      | Deployment      | Plan and schedule deployment.                                                                                        |
| 2   | FO                         | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                           |
| 3   | FO                         | Deployment      | Execute deployment.                                                                                                  |
| 4   | FO                         | Installation    | Plan and schedule installation.                                                                                      |
| 5   | Contractor Team (REDACTED) | Installation    | Ensure authority to operate and that certificate authority security documentation is in place.                       |
| 6   | Contractor Team (REDACTED) | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out). |
| 7   | Contractor Team (REDACTED) | Post Deployment | Hardware, Software, and System Support.                                                                              |

Deployment, Installation, Backout and Rollback Roles and ResponsibilitiesThis table lists the stakeholders for deployment, installation, backout, and rollback procedures by providing ID, Team, Phase or Role, and Tasks information.

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national general availability release. The scheduling of test/mirror installs, testing, and the deployment to production will be at the sites’ discretion.

A national release is planned after testing has been successfully completed at initial operating capability (IOC) test sites.

Deployment will be performed by the local or regional OIT staff and supported by team members from these organizations: FO and Enterprise Operations. Other teams may provide additional support.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The general availability national release is scheduled to occur in June of 2023.

Table 2: Timeline Overview

| Task                        | Start     | Finish    |
|-----------------------------|-----------|-----------|
| IOC Preparation and Testing | 2/23/2023 | 6/20/2023 |
| National Release            | 6/26/2023 | 6/26/2023 |
| Compliance Period           | 6/27/2023 | 7/27/2023 |

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XU\*8.0\*689 will be deployed to all VistA instances running on Intersystems Cache and/or Iris server platforms.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch XU\*8.0\*689 will be installed at all required locations using the standard VistA Kernel Installation and Distribution System (KIDS) host file processes.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch contains an environment check routine that ensures the BUSINESS ACTIVITY CODE file (#8991.8) contains the latest codes. If the file is not current, the missing

codes are added and the installation aborts. A message is displayed informing the installer

the DEA migration must be re-run using the DEA Migration Report \[PSO DEA MIGRATION REPORT\] option. The loading and installation of the patch may not proceed until the DEA migration is re-run.

The DEA multi-build host file PSO_545_PSJ_372_OR_499.KID containing patches PSO\*7\*545, PSJ\*5\*372, and OR\*3\*499 must be installed immediately after installing XU\*8\*689. Ensure the PSO_545_PSJ_372_OR_499.KID host file is available to load and install prior to installing XU\*8\*689.

### Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Patch XU\*8.0\*689 is written in the M programming language and is compliant with VistA's standards and conventions. Software elements, such as protocols, are stored in the appropriate files.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DEA Pharmacy Enhancement release does not require any special or specific resources other than a functional VistA system.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific hardware required other than that which already hosts the VistA system. This is a software enhancement that will not require additional hardware.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific software required other than that which already hosts the VistA system.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For national release, sites will receive communication that the release has occurred, typically this is an Action Item or Bulletin.

Sites will use their internal communications to let their users know about upcoming installations and any associated downtime. This is critical as users can often slow the installation process if they are on the system while installers are trying to get the software installed.

Clinical Application Coordinators (CACs), installers, and other site personnel (as determined by the site) will need to coordinate installation dates and times. In addition, other support personnel may need to be consulted – such as the Citrix support, Client Technologies (if required).

#### Deployment/Installation/Back-out Checklist

The Release Management team will deploy the patch XU\*8.0\*689, which are tracked in the NPM in Forum, nationally to all VAMCs. FORUM automatically tracks the patches as they are installed in the different VAMC production systems as described in the previous section. One can run a report in FORUM to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not installed the patch in their VistA production system as of that moment in time.

Therefore, this information does not need to be manually tracked. The table is included below if manual tracking is desired.

Table 3: Deployment / Installation / Back-out Checklist

| Activity | Day | Time | Individual who completed task |
|--------------|---------|----------|-----------------------------------|
| Deploy       | TBD     | TBD      | TBD                               |
| Install      | TBD     | TBD      | TBD                               |
| Back-out     | TBD     | TBD      | TBD                               |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch XU\*8.0\*689 will be a KIDS build distributed as a host file. Prior to installing, routine CHECK1^XTSUMBLD should be run to capture pre-patch checksums.

| Routine | Before Checksum | After Checksum |
|-------------|---------------------|--------------------|
| XU8P689     | (New)               | 1174266            |
| XU8PE689    | (New)               | 13409033           |
| XUEPCSU1    | (New)               | 61886394           |
| XUEPCSUT    | (New)               | 174456386          |
| XUEPCSVR    | (New)               | 785438             |
| XUPSPRA     | 921249              | 7292530            |
| XUSER       | 57408093            | 135855094          |
| XUSER3      | 9641979             | 57231548           |
| XUSNPIX1    | 169471076           | 16937094           |

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch XU\*8.0\*689 can be installed with users on the system. It may be best to install it during non-peak hours. The release should take five minutes or less to install.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA patch is being released as a host file. The host file build may be downloaded from the following URL: https://download.vista.med.va.gov/index.html/SOFTWARE

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is written with the assumption that the reader is experienced and/or familiar with VistA software installation via KIDS.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XU\*8.0\*689 patch will be installed by local or regional OIT staff.

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

> **NOTE:** This patch contains an environment check routine that ensures the BUSINESS ACTIVITY CODE file (#8991.8) contains the latest codes. If the file is not current, the missing codes are added and the installation aborts. A message is displayed informing the installer the DEA migration must be re-run using the DEA Migration Report \[PSO DEA MIGRATION REPORT\] option. The loading and installation of the patch may not proceed until the DEA migration is re-run.

### Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XU\*8.0\*689 is installed using a KIDS host file. As part of the installation, routines will be backed up to a PackMan message (Second Bullet Item, Second Sub-Bullet below).

To install, perform the following steps in order:

Installation Instructions:

- Use the Load a Distribution option contained on the Kernel Installation and Distribution System Menu to load the Host file. When prompted to "Enter a Host File:" enter /srv/vista/patches/SOFTWARE/XU_8_689.KID
- When prompted "OK to continue with Load?", enter "YES". The message "Distribution OK!" should display.
- When prompted "Want to Continue with Load?", enter "YES".
- If the DEA Migration is not complete or current, the environment check routine displays a message indicating the DEA Migration is outdated and must be re-run, and the installation is aborted. To re-run the migration:
  - Navigate to the DEA Migration Report \[PSO DEA MIGRATION REPORT\] option.
  - When prompted "Do you want to re-run the DEA Migration?" enter "YES".
  - When prompted "Are you sure you want to re-run the DEA Migration?", enter "YES".
  - At the prompt "Date/Time to Queue the DEA Migration", enter a date/time to queue the migration. The default is ten minutes from the date/time the prompt is displayed.
    - The DEA migration may take from two hours up to twelve hours to complete.
    - The patch XU\*8\*689 may not be loaded until the migration is complete.
    - When the migration is complete, a MailMan message is sent to the user who queued the migration, as well as holders of the PSDMGR key.
  - When the DEA migration is complete, repeat Step 1 to reload the patch and continue the installation.
- From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
  - Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter XU\*8.0\*689.
  - Select the Backup a Transport Global option to create a backup message of new and modified software components. You must use this option and specify what to backup; the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition,
    - At the Installation option menu, select Backup a Transport Global.
    - At the Select INSTALL NAME prompt, enter XU\*8.0\*689.
    - When prompted for the following, enter "B" for Build.

Select one of the following:

B Build

R Routines

Enter response: Build

- When prompted “Do you wish to secure this message? NO//”, press \<enter\> and take the default response of “NO”.
- When prompted with, "Send mail to: Last name, First Name", press \<enter\> to take default recipient. Add any additional recipients.
- When prompted with "Select basket to send to: IN//", press \<enter\> and take the default IN mailbox or select a different mailbox.
- Other options available:
  - Print Transport Global - This option allows viewing of the components of the KIDS build.
  - Compare Transport Global to Current System - This option allows viewing of all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
- From the Installation Menu, select the Install Package(s) option and choose XU\*8.0\*689 to install.
  - When prompted, ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’ answer NO.
  - When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO.
  - When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer \<NO\>.
  - When prompted ‘DEVICE: HOME// ‘ enter the device to which install messages should print.

<u>EXAMPLE of install log:</u>

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INSTALLation

Select Installation Option: INSTALL Package(s)

Select INSTALL NAME: XU\*8.0\*689 6/18/22@06:20:42

=\> XU\*8\*689 TEST v8

This Distribution was loaded on Jun 18, 2021@06:20:42 with header of

XU\*8\*689 TEST v8

It consisted of the following Install(s):

XU\*8.0\*689

Checking Install for Package XU\*8.0\*689

Install Questions for XU\*8.0\*689

Incoming Files:

8991.6 XUEPCS DATA (Partial Definition)

> **NOTE:** You already have the 'XUEPCS DATA' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// Linux Telnet /SSh

XU\*8.0\*689

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Installing OPTION

Jun 18, 2022@06:21:21

Running Post-Install Routine: POST^XU8P689

...Placing XU EPCS UTILITY FUNCTIONS menu options out of order...

Updating Routine file...

Updating KIDS files...

XU\*8.0\*689 Installed.

Jun 18, 2022@06:21:21

NO Install Message sent

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

100% . 25 50 75 .

Complete F,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

Install Completed

## Post-Installation Steps and Installation Verification Procedures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **WARNING:** The DEA multi-package host file PSO_545_PSJ_372_OR_499.KID containing PSO\*7.0\*545, OR\*3.0\*499, and PSJ\*5.0\*372 must be installed IMMEDIATELY after installing this patch (XU\*8.0\*689). Controlled Substance medication ordering will be adversely affected if XU\*8.0\*689 is installed without also installing the DEA multi-package host file. See the PSO\*7.0\*545 Patch Description and DIBRG for more details.

Verify the installation by print the build using option Build File Print \[XPD PRINT BUILD\], checking the installed build components match the patch description.

Example, Build File Print:

Select OPTION NAME: BUILD FILE PRINT XPD PRINT BUILD Build File Print

PACKAGE: XU\*8.0\*689 May 07, 2023 10:59 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: KERNEL ALPHA/BETA TESTING: NO

DATE DISTRIBUTED: May 01, 2023

DESCRIPTION:

See FORUM for patch description.

ENVIRONMENT CHECK: XU8PE689 DELETE ENV ROUTINE: No

PRE-INIT ROUTINE: PRE^XU8P689 DELETE PRE-INIT ROUTINE: Yes

POST-INIT ROUTINE: POST^XU8P689 DELETE POST-INIT ROUTINE: Yes

PRE-TRANSPORT RTN:

RESTORE ROUTINE:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

8991.6 XUEPCS DATA YES YES NO NO

Partial DD: subDD: 8991.6 fld: .03

fld: .07

fld: .08

ROUTINE: ACTION:

XUEPCSU1 SEND TO SITE

XUEPCSUT SEND TO SITE

XUEPCSVR SEND TO SITE

XUPSPRA SEND TO SITE

XUSER SEND TO SITE

XUSER3 SEND TO SITE

XUSNPIX1 SEND TO SITE

INSTALL QUESTIONS:

Default Rebuild Menu Trees Upon Completion of Install: NO

Default INHIBIT LOGONs during the install: NO

Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

REQUIRED BUILDS: ACTION:

XU\*8.0\*551 Don't install, leave global

XU\*8.0\*548 Don't install, leave global

XU\*8.0\*751 Don't install, leave global

XU\*8.0\*765 Don't install, leave global

XU\*8.0\*774 Don't install, leave global

XU\*8.0\*688 Don't install, leave global

Verify the options listed below are marked out of order with the message ‘PLACED OUT OF ORDER BY XU\*8\*689’

| Option Text                           | Option Name                 |
|-------------------------------------------|---------------------------------|
| ePCS Edit Prescriber Data                 | \[XU EPCS EDIT DATA\]           |
| Print Prescribers with Privileges         | \[XU EPCS PRIVS\]               |
| Print DISUSER Prescribers with Privileges | \[XU EPCS DISUSER PRIVS\]       |
| Print Setting Parameters Privileges       | \[XU EPCS SET PARMS\]           |
| Print Audits for Prescriber Editing       | \[XU EPCS PRINT EDIT AUDIT\]    |
| Edit Facility DEA# and Expiration Date    | \[XU EPCS EDIT DEA# AND XDATE\] |
| Print PSDRPH Key Holders                  | \[XU EPCS PSDRPH\]              |
| Allocate/De-Allocate of PSDRPH Key        | \[XU EPCS PSDRPH KEY\]          |

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No configuration changes are needed in VistA.

# Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The backout procedure returns the software to the last known good operational state of the software and appropriate platform settings.

## Backout Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New and modified VistA components may be restored to their pre-patch state by installing the backup created prior to installation.

## Backout Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes implemented with Patch XU\*8.0\*689 should be backed out in their entirety. Changes are generally interdependent and should not be backed out on an item by item basis.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) will be covered by Initial Operating Capability (IOC) testing.

## Backout Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XU\*8.0\*689 may be backed out if it is decided that the project is canceled, the software is not functioning as expected, or the requested changes implemented by the patch are no longer desired by VA OIT and the Pharmacy Benefits Management (PBM) office.

## Backout Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XU\*8.0\*689 contains software referenced by an updated version of the ePCS GUI. Backing out XU\*8.0\*689 will require users to revert to the previously released version of the ePCS GUI.

Patch XU\*8.0\*689 is included in a series of patches that are intended to be installed at the same time. If XU\*8.0\*689 is backed out, any related patches that require XU\*8.0\*689 must also be backed out to prevent errors.

## Authority for Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authorization to back out requires concurrence from the VA Project Manager and the Facility Director.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA backout procedure can be executed by restoring the system to its pre-patch state. This includes restoring modified components and removing new components.

### Backout Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA backout procedure can be executed by installing the backup created prior to installation. Modified software components are restored to their pre-patch state, and new software components are removed.

The VistA KIDS installation procedure allows the installer to back up the modified components using the ‘Backup a Transport Global’ action. The back-out procedure is to install the build backup created prior to installation.

Patch XU\*8.0\*689 contains the following build components:

<u>Routines</u>

| Routine Name | New/Modified |
|------------------|------------------|
| XU8P689          | New              |
| XU8PE689         | New              |
| XUEPCSUT         | New              |
| XUEPCSU1         | New              |
| XUEPCSVR         | New              |
| XUPSPRA          | Modified         |
| XUSER            | Modified         |
| XUSER3           | Modified         |
| XUSNPIX1         | Modified         |

<u>Options</u>

| Option Text                           | Option Name                 |
|-------------------------------------------|---------------------------------|
| ePCS Edit Prescriber Data                 | \[XU EPCS EDIT DATA\]           |
| Print Prescribers with Privileges         | \[XU EPCS PRIVS\]               |
| Print DISUSER Prescribers with Privileges | \[XU EPCS DISUSER PRIVS\]       |
| Print Setting Parameters Privileges       | \[XU EPCS SET PARMS\]           |
| Print Audits for Prescriber Editing       | \[XU EPCS PRINT EDIT AUDIT\]    |
| Edit Facility DEA# and Expiration Date    | \[XU EPCS EDIT DEA# AND XDATE\] |
| Print PSDRPH Key Holders                  | \[XU EPCS PSDRPH\]              |
| Allocate/De-Allocate of PSDRPH Key        | \[XU EPCS PSDRPH KEY\]          |

<u>Load patch build backup:</u>

1.  Find the XU\*8.0\*689 build backup message in in the MailMan Menu \[XMUSER\] option.
2.  At the ‘Enter message action:’ prompt, enter Xtract KIDS.
3.  At the ‘Select PackMan function:’ prompt, enter INSTALL/CHECK MESSAGE.
4.  At the ‘OK to continue with Load?’ prompt, enter YES.
5.  At the ‘Want to continue with Load?’ prompt, enter YES.

<u>Example, load backup PackMan message:</u>

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

Line 8 Message \#302200 Unloading KIDS Distribution XU\*8.0\*689b

Build XU\*8.0\*689b has been loaded before, here is when:

XU\*8.0\*689b Install Completed

was loaded on Jun 17, 2022@18:05:35

OK to continue with Load? NO// YES

Want to Continue with Load? YES//

Loading Distribution...

XU\*8.0\*689b

<u>Install build backup:</u>

1.  Select the Install Package(s) option in the Installation menu in the Kernel Installation & Distribution System \[XPD MAIN\] menu.
2.  At the ‘Select INSTALL NAME:’ prompt, select the previously loaded XU\*8.0\*689 build backup.
3.  At the ‘Want to Rebuild Menu Trees Upon Completion of Install?’ prompt, enter NO.
4.  At the ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols?’ prompt, enter NO.
5.  At the ‘DEVICE:’ prompt, enter an output device or accept the default.

Example, install previously loaded backup:

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INstallation

Select Installation \<TEST ACCOUNT\> Option: INstall Package(s)

Select INSTALL NAME: XU\*8.0\*689b 6/17/22@18:27:21

=\> Backup of XU\*8.0\*689 on Jun 17, 2021. Build

This Distribution was loaded on Jun 17, 2021@18:27:21 with header of

Backup of XU\*8.0\*689 on Jun 17, 2021. Build

It consisted of the following Install(s):

XU\*8.0\*689b

Checking Install for Package XU\*8.0\*689b

Install Questions for XU\*8.0\*689b

Incoming Files:

8991.6 XUEPCS DATA (Partial Definition)

> **NOTE:** You already have the 'XUEPCS DATA' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// Linux Telnet /SSh

XU\*8.0\*689b

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Installing Data Dictionaries:

Jun 17, 2021@18:34:39

Installing PACKAGE COMPONENTS:

Installing REMOTE PROCEDURE

Installing OPTION

Jun 17, 2021@18:34:39

Updating Routine file...

Updating KIDS files...

XU\*8.0\*689b Installed.

Jun 17, 2021@18:34:39

NO Install Message sent

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

100% . 25 50 75 .

Complete F,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

Install Completed

## Backout Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backout verification of VistA routines can be performed by running CHECK1^XTSUMBLD for Build Name XU\*8.0\*689 at the programmer prompt.

1.  Run CHECK1^XTSUMBLD from the programmer prompt.
2.  At the ‘Build from:’ prompt, enter BUILD.
3.  At the ‘Select BUILD NAME:’ prompt, enter XU\*8.0\*689.

The message ‘Routine not in this UCI’ should display next to each of the following new routines:

XU8P689 Routine not in this UCI

XU8PE689 Routine not in this UCI.

XUEPCSUT Routine not in this UCI.

XUEPCSU1 Routine not in this UCI.

XUEPCSVR Routine not in this UCI.

The checksums below should display next to the modified routines:

XUPSPRA value = 921249

XUSER value = 57408093

XUSER3 value = 9641979

XUSNPIX1 value = 169471076

EXAMPLE screen of routine CHECK1^XTSUMBLD:

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: XU\*8.0\*689 OUTPATIENT PHARMACY

XU8P689 Routine not in this UCI.

XU8PE689 Routine not in this UCI.

XUEPCSUT Routine not in this UCI.

XUEPCSU1 Routine not in this UCI.

XUEPCSVR Routine not in this UCI.

XUPSPRA value = 921249 Missing patch number

XUSER value = 57408093 Missing patch number

XUSER3 value = 9641979 Missing patch number

XUSNPIX1 value = 169471076 Missing patch number

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select the XU EPCS UTILITY Functions menu, verify there are no ‘\*\*\> Out of order:’ messages display with any options in this menu. Verify the options in the menu are selectable.

Example, options not marked out of order after backing out XU\*8.0\*689:

Print DISUSER Prescribers with Privileges \[XU EPCS DISUSER PRIVS\]

ePCS Edit Prescriber Data \[XU EPCS EDIT DATA\]

Edit Facility DEA# and Expiration Date \[XU EPCS EDIT DEA# AND XDATE\]

Print Audits for Prescriber Editing \[XU EPCS PRINT EDIT AUDIT\]

Print Prescribers with Privileges \[XU EPCS PRIVS\]

Print PSDRPH Key Holders \[XU EPCS PSDRPH\]

Allocate/De-Allocate of PSDRPH Key \[XU EPCS PSDRPH KEY\]

Print Setting Parameters Privileges \[XU EPCS SET PARMS\]

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No data is installed with the patch, rollback is not applicable for this release.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authorization for a rollback will be determined by the VA Project Manager.

## Rollback Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Verification Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.