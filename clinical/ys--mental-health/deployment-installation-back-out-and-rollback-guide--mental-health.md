---
consolidated_title: "mental health deployment, installation, back-out, and rollback guide"
app_code: YS
doc_type: DIBR
master_source: "YS*5.01*149 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
master_pub_date: December 2020
consolidated_from: 24 versions
prior_versions:
  - "YS*5.01*121 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*123 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*129 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*142 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*148 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*174 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*175 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*177  Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*181 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*183 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*199 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*208 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*221 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*223 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*224 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*233 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*234 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*235 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*236 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*239 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*249 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*250 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*255 Mental Health Deployment, Installation, Back-Out, and Rollback Guide"
---

---
title: |
  Clozapine Modernization (ClozMod) YS\*5.01\*149

  Deployment, Installation, Back-out, and Rollback Guide (DIBR)
---

![](ys-5-01-149-mental-health-deployment-installation-back-out-and-rollback-guide/001.png)

December 2020

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date      | Revision | Description                 | Author               |
|-----------|----------|-----------------------------|----------------------|
| 12/1/20   | 1.2      | Changed for updates         | Liberty IT Solutions |
| 11/10/20  | 1.1      | Patch 149 update and review | Liberty IT Solutions |
| 6/25/2020 | 1.0      | Initial Version             | B3 Group             |

This table displays a summary of the document's revision history.

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
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [Installation Instructions](#installation-instructions)
  - [Sample Install Log](#sample-install-log)
  - [Post-Installation Steps and Installation Verification Procedures](#post-installation-steps-and-installation-verification-procedures)
  - [System Configuration](#system-configuration)
- [Back-out Procedure](#back-out-procedure)
  - [Back-out Strategy](#back-out-strategy)
  - [Back-out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-out Criteria](#back-out-criteria)
  - [Back-out Risks](#back-out-risks)
  - [Authority for Back-out](#authority-for-back-out)
  - [Back-out Procedure](#back-out-procedure-1)
    - [Back-out Instructions](#back-out-instructions)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install ClozMod’s project’s VistA Patch YS\*5.01\*149, as well as how to back-out the product and rollback to a previous version or data set. This patch will enhance the Clozapine nightly transmission by replacing the MailMan messages with HL7 messages.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a document that describes how, where, and when VistA Patch YS\*5.01\*149 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources and includes a communications plan with the rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VistA patches must be installed at the site:

- YS\*5.01\*154
- PSO\*7.0\*574

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table: Deployment, Installation, Back-out and Rollback Roles and Responsibilities

| ID  | Team                      | Phase/Role      | Tasks                                                                                                               |
|-----|---------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|
| 1   | Filed Operations (FO)     | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                 |
| 2   | FO                        | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment                           |
| 3   | FO                        | Deployment      | Test for operational readiness                                                                                      |
| 4   | FO                        | Deployment      | Execute deployment                                                                                                  |
| 5   | FO                        | Installation    | Plan and schedule installation                                                                                      |
| 6   | Contractor Team (Liberty) | Installation    | Ensure authority to operate and that certificate authority security documentation is in place                       |
| 7   | Contractor Team (Liberty) | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |
| 8   | Contractor Team (Liberty) | Post-deployment | Hardware, software, and system support                                                                              |

Deployment, Installation, Backout and Rollback Roles and ResponsibilitiesThis table lists the stakeholders for deployment, installation, backout, and rollback procedures by providing ID, Team, Phase or Role, and Tasks information.

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national general availability release. The scheduling of test/mirror installs, testing, and the deployment to production will be at the sites’ discretion. It is anticipated that there will be a 14-day compliance period.

A national release is planned for December 2020 after testing has been successfully completed at two initial operating capability (IOC) test sites: Greater Los Angeles and West Haven.

Deployment will be performed by the local or regional staff and supported by team members from these organizations: Field Operations and Enterprise Operations. Other teams may provide additional support.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The general availability national release is scheduled to occur in December 2020.

Table: Release Timeline Overview

| Task Name                                   | Start        | Finish       |
|---------------------------------------------|--------------|--------------|
| Finalize and Submit Technical Documentation | Mon 9/14/20  | Tue 10/20/20 |
| Finalize and Submit Technical Manual        | Tue 10/6/20  | Mon 10/12/20 |
| Create DIBR                                 | Tue 10/6/20  | Fri 10/9/20  |
| Review DIBR                                 | Mon 10/12/20 | Wed 10/14/20 |
| Finalize DIBR                               | Mon 9/14/20  | Mon 10/19/20 |
| Create YS\*5.01\*149 POLARIS Entry          | Mon 10/5/20  | Mon 10/5/20  |
| Create Version Description Document (VDD)   | Tue 10/6/20  | Mon 10/12/20 |
| Review VDD                                  | Mon 9/14/20  | Thu 10/15/20 |
| Finalize VDD                                | Thu 10/15/20 | Tue 10/20/20 |
| Create and Submit IOC Defect Log            | Tue 10/6/20  | Mon 10/19/20 |
| Prepare for Release Readiness Review        | Tue 10/6/20  | Mon 10/19/20 |
| Begin Release Readiness Report              | Tue 10/6/20  | Tue 10/6/20  |
| Upload YSCL Technical Manual                | Tue 10/6/20  | Tue 10/6/20  |
| Upload DIBR                                 | Tue 10/6/20  | Tue 10/6/20  |
| Upload Final Source Code to GitHub          | Tue 10/6/20  | Tue 10/6/20  |
| Upload VDD to GitHub                        | Tue 10/6/20  | Tue 10/6/20  |
| Release Readiness Report Completed          | Tue 10/6/20  | Tue 10/6/20  |
| Application Coordinator Review              | Wed 10/7/20  | Thu 10/15/20 |
| Release Readiness Review                    | Fri 10/16/20 | Mon 10/19/20 |
| Receive NCCC approval                       | Mon 10/19/20 | Mon 10/19/20 |

This table displays an overview of the release timeline including task name, and start and finish dates.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch YS\*5.01\*149 will be deployed in VistA.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch YS\*5.01\*149 will be installed using the standard VistA installation process.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No activities are needed to prepare the VistA sites for this release.

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

The VistA Patch YS\*5.01\*149 is written in MUMPS operating system using the vendor Caché and is compliant with VistA's standards and conventions. Software elements, such as protocols, are stored in the appropriate files.

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these software specifications.

## Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The development team will use email and conference calls for communication during the deployment; email and/or conference calls will also be utilized to notify stakeholders of the successful product release.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch YS\*5.01\*149 will be distributed as a standard Kernel Installation and Distribution System (KIDS) build. The patch description also contains the installation procedure.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch YS\*5.01\*149 can be installed with users on the system. It may be best to install it during non-peak hours. The release should take five minutes or less to install.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA patch will be distributed via the standard VistA release process; no files need to be downloaded for the installation of this patch.

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

The KIDS build will be installed by local or regional OIT staff. Routines will be backed up to a PackMan message before installing the build. YS\*5.01\*149 contains one pre-existing routine: YSCLTST5. The rest of the routines are new and will not be backed up.

Prior to installing YS\*5.01\*149, CHECK1^XTSUMBLD will be run to capture the ‘pre’ patch checksums.

### Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch YS\*5.01\*149 is installed using KIDS.

For install, perform the following steps in order:

- Choose the PackMan message containing this patch.
- Choose the INSTALL/CHECK MESSAGE PackMan option.
- From the KIDS Menu, select the Installation Menu. From this menu:
  - Select the Verify Checksums in Transport Global option to confirm the integrity of the routines in the transport global. When prompted for the INSTALL NAME enter the patch or build name.
  - Select the Backup a Transport Global option to create a backup message of any routines exported with this patch. It will not backup any other changes such as Data Dictionaries (DDs) or options.
  - One of the following options can also be elected for use:
    - Print Transport Global - This option allows viewing of the components of the KIDS build.
    - Compare Transport Global to Current System - This option allows viewing of all changes that will be made when this patch is installed. It compares all the components of this patch, such as routines, DDs, templates, etc.
- From the Installation Menu, select the Install Package(s) option and choose YS\*5.01\*149 to install.
- Accept the default when prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//'
- Accept the default when prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'
- Accept the default when prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//'
- If prompted ‘Delay Install (Minutes): (0 - 60): 0// enter 0 (zero).’

## Sample Install Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: YS\*5.01\*149 11/29/19@17:04:58

=\> YS\*5.01\*149 BACKUP THREE

This Distribution was loaded on Nov 29, 2019@17:04:58 with header of

YS\*5.01\*149

It consisted of the following Install(s):

YS\*5.01\*149

Checking Install for Package YS\*5.01\*149

Install Questions for YS\*5.01\*149

Incoming Files:

603.03 CLOZAPINE PARAMETERS

> **NOTE:** You already have the 'CLOZAPINE PARAMETERS' File.

603.05 CLOZAPINE HL7 TRANSMISSION

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'YSCLHL7 LOGS': DEVELOPER,JC JCH

192 OI&T STAFF

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// YES

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

## Post-Installation Steps and Installation Verification Procedures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation of the patch, the installer should notify the coordinator of the YSCLHL7 LOGS mail group (see section 4.9) and schedule the new transmission option: Transmit Clozapine Rx HLS Messages \[YSCL HL7 CLOZ TRANSMISSION\].

The new option will be scheduled to run in the off-hours daily, typically between 10:00 PM and 2:00 AM. This option is scheduled in TaskMan using the TaskMan Schedule/Unschedule Options \[XUTM SCHEDULE\]. The device field for the option will be null as the option will not have a DEVICE FOR QUEUED JOB OUTPUT.

Example:

Edit Option Schedule

Option Name: YSCL HL7 CLOZ TRANSMISSION

Menu Text: Transmit Clozapine Rx HL7 Messages

TASK ID: 8798880

QUEUED TO RUN AT WHAT TIME: DEC 5,2019@23:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

After the new transmission option is scheduled, verify that the VistA menu and options below are installed and the options are attached to the menu:

- Clozapine HL7 Transmission Options \[YSCL HL7 MAIN\] menu
  - Clozapine HL7 Messages Summary \[YSCL HL7 STATUS REPORT\] option
  - List of Clozapine Prescription \[YSCLHL7 LIST CLOZXAPINE RXS\] option
  - Print HL7 Report by Date \[YSCL HL7 REPORT BY DATE\] option
  - Retransmit Clozapine Rx HL7 Messages \[YSCL HL7 CLOZ RETRANSMIT\] option
  - Queue Clozapine Rx HL7 Messages \[YSCL HL7 QUEUE TRANSMISSION\] option

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No configuration changes are needed in VistA. The configuration values for the new YSCL-NCCC entry in the HL LOGICAL LINK file (#870) are supplied by the patch installation process.

# Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out procedure returns the software to the last known good operational state of the software and appropriate platform settings.

## Back-out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA software can be removed manually using standard VistA software. The one pre-existing routine in the patch, YSCLTST5, may be restored to its pre-patch state by installing the backup created prior to installation. All other routines in this patch are new and must be manually deleted. Any existing software will remain functional. The other non-routine individual software components for this patch can be removed using FileMan.

## Back-out Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes implemented with Patch YS\*5.01\*149 should be backed out in their entirety. Changes are generally interdependent and should not be backed out on an item by item basis.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) will be covered by Initial Operating Capability (IOC) testing performed at the following VistA test sites: West Haven (689) and West Los Angeles (691).

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch YS\*5.01\*149 may be backed out if it is decided that the project is canceled, the software is not functioning as expected, or the requested changes implemented by the patch are no longer desired by VA OIT and the Clozapine eBusiness team.

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As most of the changes in Patch YS\*5.01\*149 are new software components and functionalities that are not dependent upon by existing VistA software, backing out the changes will revert the software to its pre-patch state and does not pose any additional risk.

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authorization to back out requires concurrence from the Chief of Mental Health, Chief of Staff, and the Facility Director.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA back-out procedure can be executed by deleting the routines and other elements from the VistA environment. Since this is new software, the routines and elements can be removed without affecting any other VistA modules.

### Back-out Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA back-out procedure can be executed by restoring existing routines to their pre-patch state and deleting new routines and other elements from the VistA environment. Deleting all VistA options exported within the patch will remove all pointers to the option including scheduled tasks. New routines and elements can be removed without affecting any existing VistA functionality since the new routines and other components are not referenced by existing software.

The VistA KIDS installation procedure allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action. The back-out procedure for new routines, globals, data dictionaries, and other VistA components requires manual removal or the issuance of a follow-up patch to ensure all components are properly removed and/or restored. All software components, routines and other items, must be restored to their previous state at the same time and in conjunction with the restoration of the data.

Patch YS\*5.01\*149 contains the following build components:

- Routines (New and Existing)
- Data Dictionary
- Options
- HLO Application Registry
- HL7 Logical Link
- Mail Group

Please contact the Enterprise Program Management Office team for assistance since this installed patch contains components in addition to routines.

#### Restore Modified Routines

To restore modified routines from backup, perform the following steps in order:

- From VistA mailman, select Read/Manage Messages
- Accept default message reader.
- Select mail basket containing backup of patch routines.
- Select message containing backup of patch routines.
- Enter “^” to exit at the ‘Type \<Enter\> to continue or ‘^’ to exit’.
- Enter ‘6’ for the Install/Check Message action at the ‘Enter message action’ prompt.
- Enter “YES” at the ‘Do you really want to do this?’ prompt.
- Optionally save the routines to be overwritten by entering “YES” at the ‘Shall I preserve the routines on disk in a separate back-up message?’ prompt.

#### Remove New Routines

To remove new routines, perform the following steps:

VISTAS1:VISTA\>D ^%RDELETE

Delete routines/INCLUDE files.

> **WARNING:** When \<rtn\>.MAC.0 is deleted, the latest backup is moved

to \<rtn\>.MAC.0, UNCOMPILED.

Routine(s): YSCL149P

Routine(s): YSCLHLAD

Routine(s): YSCLHLFN

Routine(s): YSCLHLGT

Routine(s): YSCLHLMA

Routine(s): YSCLHLOP

Routine(s): YSCLHLPD

Routine(s): YSCLHLPR

Routine(s): YSCLHLRD

Output on Device:

Right margin: 80 =\>

YSCL149P.INT YSCLHLAD.INT YSCLHLFN.INT YSCLHLGT.INT YSCLHLMA.INT YSCLHLOP.INT YSCLHLPD.INT YSCLHLPR.INT YSCLHLRD.INT YSCLTST5.INT

Okay to continue? Yes =\> Yes

#### Delete New VistA Options

To delete new VistA options, perform the following steps in order:

Use the Fileman ENTER OR EDIT FILE ENTRIES option to delete the options exported with the patch.

- Enter the option name at the ‘NAME:’ prompt.
- Enter ‘@’ at the prompt for ‘Replace’.
- Enter ‘Y’ at the prompt ‘SURE YOU WANT TO DELETE THE ENTIRE ‘\<OPTION NAME\>’ OPTION?
- Enter ‘N’ at the prompt ‘DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)?’.

Perform all four of the steps above for each of the following options:

- Retransmit Clozapine Rx HL7 Messages \[YSCL HL7 CLOZ RETRANSMIT\]
- Transmit Clozapine Rx HL7 Messages \[YSCL HL7 CLOZ TRANSMISSION\]
- List of Clozapine Prescriptions \[YSCL HL7 LIST CLOZAPINE RXS\]
- Clozapine HL7 Transmission Options \[YSCL HL7 MAIN\]
- Queue Clozapine Rx HL7 Messages \[YSCL HL7 QUEUE TRANSMISSION\]
- Print HL7 Report by Date \[YSCL HL7 REPORT BY DATE\]
- Clozapine HL7 Messages Summary \[YSCL HL7 STATUS REPORT\]

Example:

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: OPTION// (13653 entries)

EDIT WHICH FIELD: ALL//

Select OPTION NAME: YSCL HL RETRANSMIT Retransmit Clozapine Rx HL7 Messages

NAME: YSCL HL7 CLOZ RETRANSMIT Replace @

SURE YOU WANT TO DELETE THE ENTIRE 'YSCL HL7 CLOZ RETRANSMIT' OPTION? Y

(Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// N

(No)

#### Delete New Clozapine HL7 Transmission File

Delete the new CLOZAPINE HL7 TRANSMISSION file (#603.05) using the Fileman option EDIT FILE located in the UTILITY FUNCTIONS menu.

Example:

Select OPTION: UTILITY FUNCTIONS

Select UTILITY OPTION: EDIT FILE

Modify what File: CLOZAPINE HL7 TRANSMISSION// (21 entries)

Do you want to use the screen-mode version? YES// NO

NAME: CLOZAPINE HL7 TRANSMISSION Replace @

DO YOU WANT JUST TO DELETE THE 21 FILE ENTRIES,

& KEEP THE FILE DEFINITION? No// N (No)

IS IT OK TO DELETE THE '^YSCL(603.05)' GLOBAL? Yes// Y (Yes)

SURE YOU WANT TO DELETE THE ENTIRE 'CLOZAPINE HL7 TRANSMISSION' FILE? Y

(Yes)

Deleting the DATA DICTIONARY...

Deleting the INPUT TEMPLATES..........

Deleting the PRINT TEMPLATES................................

Deleting the SORT TEMPLATES.........

Deleting the FORMS...

Deleting the BLOCKS...

#### Delete HLO Applications

Use the Fileman ENTER OR EDIT FILE ENTRIES option to delete the following new HLO APPLICATION REGISTRY entries exported with the patch:

- YSCL-REG-REC
- YSCL-REG-SEND

Example:

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: HLO APPLICATION REGISTRY// (11 entries)

EDIT WHICH FIELD: ALL//

Select HLO APPLICATION REGISTRY APPLICATION NAME: YSCL-REG-REC

APPLICATION NAME: YSCL-REG-REC// @

SURE YOU WANT TO DELETE THE ENTIRE 'YSCL-REG-REC' HLO APPLICATION REGISTRY? Y (Yes)

Select HLO APPLICATION REGISTRY APPLICATION NAME: YSCL-REG-SEND

APPLICATION NAME: YSCL-REG-SEND// @

SURE YOU WANT TO DELETE THE ENTIRE 'YSCL-REG-SEND' HLO APPLICATION REGISTRY? Y (Yes)

#### Delete HL Logical Link

Use the Fileman ENTER OR EDIT FILE ENTRIES option to delete the following new HL LOGICAL LINK entry exported with the patch.

- YSCL-NCCC

Example:

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: HL LOGICAL LINK// (293 entries)

EDIT WHICH FIELD: ALL//

Select HL LOGICAL LINK NODE: YSCL-NCCC

NODE: YSCL-NCCC// @

SURE YOU WANT TO DELETE THE ENTIRE 'YSCL-NCCC' HL LOGICAL LINK? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'OUTPATIENT SITE' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// N

(No)

#### Delete Mail Group

Use the Fileman ENTER OR EDIT FILE ENTRIES option to delete the following new MAIL GROUP entry exported with the patch.

- YSCL HL7 LOGS

Example:

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: MAIL GROUP// (770 entries)

EDIT WHICH FIELD: ALL//

Select MAIL GROUP NAME: YSCLHL7 LOGS

NAME: YSCLHL7 LOGS// @

SURE YOU WANT TO DELETE THE ENTIRE 'YSCLHL7 LOGS' MAIL GROUP? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'BULLETIN' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// N

(No)

#### Delete Data Dictionaries

#### Delete Data Dictionaries via Fileman

Use the Fileman MODIFY FILE ATTRIBUTES option to delete the following new fields exported with the patch:

Table: New Fields

| File Name            | File Number | Field Name             | Field Number |
|----------------------|-------------|------------------------|--------------|
| CLOZAPINE PARAMETERS | 603.03      | HL7 TRANSMISSION START | 20.01        |
| CLOZAPINE PARAMETERS | 603.03      | HL7 TRANSMISSION END   | 20.02        |

This table displays the new fields exported with the patch by the file name, file number, field name, and field number.

Example:

Select OPTION: MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES// NO

Modify what File: CLOZAPINE PARAMETERS// (1 entry)

Select FIELD: 20.01 HL7 TRANSMISSION START

LABEL: HL7 TRANSMISSION START Replace @

SURE YOU WANT TO DELETE THE ENTIRE 'TRANSMISSION START’ FIELD? Y (Yes)

OK TO DELETE ‘HL7 TRANSMISSION START’ FIELDS IN THE EXISTING ENTRIES? Yes// Y (Yes)

Select FIELD: 20.02 HL7 TRANSMISSION END

LABEL: HL7 TRANSMISSION END Replace @

SURE YOU WANT TO DELETE THE ENTIRE 'TRANSMISSION END’ FIELD? Y (Yes)

OK TO DELETE ‘HL7 TRANSMISSION END’ FIELDS IN THE EXISTING ENTRIES? Yes// Y (Yes)

#### Delete Data Dictionaries via Command Line FM API

Use the MUMPs programmer command line to invoke Fileman API DIU2 – Delete Data Dictionary.

Example:

Select OPTION: MODIFY FILE ATTRIBUTES

VISTA\>S DIU=”603.05”

VISTA\>S DIU(0)=”DE”

VISTA\>D EN^DIU2

Deleting the DATA DICTIONARY...

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For non-routine components, back-out verification can be performed using FileMan INQUIRE TO FILE ENTRIES to verify that the elements have been removed.

For VistA routines, CHECK1^XTSUMBLD may be run for the patch at the programmer prompt.

Example routine CHECK1^XTSUMBLD:

VISTAS1:VISTA\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: YS\*5.01\*149 MENTAL HEALTH

YSCL149P Routine not in this UCI.

YSCLHLAD Routine not in this UCI.

YSCLHLFN Routine not in this UCI.

YSCLHLGT Routine not in this UCI.

YSCLHLMA Routine not in this UCI.

YSCLHLOP Routine not in this UCI.

YSCLHLPD Routine not in this UCI.

YSCLHLPR Routine not in this UCI.

YSCLHLRD Routine not in this UCI.

YSCLTST5 value = B143634815.

Done

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. Patch YS\*5.01\*149 does not alter any existing data or add new global variables so rollback procedures are not required. Any data contained in new files and fields are deleted when the files and fields are deleted during the Back-out Procedure (see section 5.6.1.8, Delete Data Dictionaries). No special software is needed to remove the patch.

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

The authorization for a rollback witll be determined by the VA Project Manager.

## Rollback Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

## Rollback Verification Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: YS*5.01*121 Mental Health Deployment, Installation, Back-Out, and Rollback Guide

### May 2018

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs

### Office of Information and Technology (OI&T)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *.*
> Revision History
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>March 2018</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>Corrected test sites and updated pagination</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>March 2017</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Updated with team input</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>March 2017</p>
</blockquote></td>
<td><blockquote>
<p>0.01</p>
</blockquote></td>
<td><blockquote>
<p>Initial Version</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After installation, notify mental health package users that the following new instruments are available:

> Alcohol Smoking and Substance Involvement Screening

> \- NIDA modified version ASSIST-NIDA

> Brief Resiliency Scale BRS

> Cross-Cutting Symptom Assessment for DSM-5 CCSA-DSM5 Client Evaluation of Motivational Interviewing CEMI Couple Satisfaction Index CSI

> Couple Satisfaction Index - 4 Item CSI-4

> Couple Satisfaction Index Partner Version CSI PARTNER VERSION Couple Satisfaction Index - 4 Item Partner Version CSI-4 PARTNER

> VERSION

> Geriatric Anxiety Inventory GAI

> Insomnia Severity Index ISI

> Modified Katz Index of ADLs KATZ-ADL-6pt

> Pain Stages of Change Questionnaire PSOCQ

> Perceived Stress Scale PSS

> Restless Legs Syndrome Rating Scale RLS

> Smith Morning-Evening Scale SMEQ

> Sleep Need Questionnaire SNQ

> Snoring, Tired, Observed, Blood Pressure STOP

> These instruments are no longer available:

> Alcohol Use Inventory (Revised) AUIR Center for Epidemiologic Studies Depression Scale

> (5-item version) CESD5

> Depression Outcome Module 8.0 DOM80 Depression Outcomes Module: Geriatric Screen DOMG Employment Readiness Scale ERS

> Health Locus of Control Scale HLOC

> Rotter Internal-External Scale IEQ

> Rotter Locus of Control RLOC

> Spiritual Assessment Inventory SAI

> Crowne-Marlowe Social Desirability Scale SDES

> Short Michigan Alcoholism Screening Test SMAST

> Validity Scale VALD

> Ward Atmosphere Scale WAS

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

### From: YS*5.01*175 Mental Health Deployment, Installation, Back-Out, and Rollback Guide

## Backout Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA software can be restored to its pre-patch state by installing the backup created prior to installation. No other software components need removal.

## Backout Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes implemented with Patch YS\*5.01\*149 should be backed out in their entirety. Changes are generally interdependent and should not be backed out on an item by item basis.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for this release.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) will be covered by Initial Operating Capability (IOC) testing.

## Backout Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch YS\*5.01\*175 may be backed out if it is decided that the project is canceled, the software is not functioning as expected, or the requested changes implemented by the patch are no longer desired by VA OIT and the Clozapine eBusiness team.

## Backout Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As the changes in Patch YS\*5.01\*175 are routine only defect fixes, backing out the changes will revert the software to its pre-patch state and does not pose any additional risk.

## Authority for Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authorization to back out requires concurrence from the Chief of Mental Health, Chief of Staff, and the Facility Director.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA backout procedure can be executed by restoring the routine to its pre-patch state.

### Backout Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA backout procedure can be executed by restoring existing routines to their pre-patch state by installing the backup created prior to installation.

The VistA KIDS installation procedure allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action. The back-out procedure for modified routines is to install the routine backup created prior to installation.

Patch YS\*5.01\*175 contains the following build components:

- Routines (One modified routine – YSCLHLGT)

This patch does not contain any other software components.

#### Restore Modified Routines

To restore modified routines from backup, perform the following steps in order:

- From VistA mailman, select Read/Manage Messages
- Accept default message reader.
- Select mail basket containing backup of patch YS\*5.01\*175.
- Select message containing backup of patch YS\*5.01\*175 routines.
- Enter “^” to exit at the ‘Type \<Enter\> to continue or ‘^’ to exit’.
- Enter ‘6’ for the Install/Check Message action at the ‘Enter message action’ prompt.
- Enter “YES” at the ‘Do you really want to do this?’ prompt.
- Optionally save the routines to be overwritten by entering “YES” at the ‘Shall I preserve the routines on disk in a separate back-up message?’ prompt.

## Backout Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For VistA routines, backout verification can be performed by running CHECK1^XTSUMBLD at the programmer prompt.

EXAMPLE screen of routine CHECK1^XTSUMBLD:

VISTAS1:VISTA\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: YS\*5.01\*175b MENTAL HEALTH

YSCLHLGT value = 184903686 Missing patch number

Done

### From: YS*5.01*250 Mental Health Deployment, Installation, Back-Out, and Rollback Guide

## Post-installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A post-install routine will run to update instrument categories. It will reactivate the BBHI-2 instrument. It will also update the URL for launching Mental Health Assistant (MHA) in the Computerized Patient Record System (CPRS) Tools menu.  
  
A new parameter, YS MHA LOG APPLICATION ERRORS, has been implemented to toggle on and off the VistA error trap for debugging. It is installed in the "off" state by default and can be turned on through the General Parameter Tools menu when VistA error trap debugging is needed. This will be done on a case by case basis at an individual site.

\*NOTE:DO NOT exercise these steps during installation of the patch. These are the steps that will be requested when a site reports a problem that requires special investigation.

If a site experiences a problem with Mental Health instrument administrations, a Service Now ticket should be created and directed to SPM.Health.ClinSvs.MHSP.MHA.

If the problem requires special error logging, the MHA team will work with the site CAC/ADPAC who has access to the General Parameter Tools.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Steps to Activate/Deactivate the YS MHA LOG APPLICATION ERRORS Parameter

-From the menu, select EP Edit Parameter Values.

-For the PARAMETER DEFINITION NAME, enter YS MHA LOG APPLICATION ERRORS

-Select 10 System.

-At the Enabled? prompt, enter Y for Yes.

Once the error is replicated and sufficient data is collected, the

CAC/ADPAC will execute the following steps from the General Parameter

Tools menu:

-From the menu, select EP Edit Parameter Values.

-For the PARAMETER DEFINITION NAME, enter YS MHA LOG APPLICATION ERRORS

-Select 10 System.

-At the Enabled? prompt, enter N for No.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

### From: YS*5.01*129 Mental Health Deployment, Installation, Back-Out, and Rollback Guide

### YS\*5.01\*129 KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

1.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
2.  Next, select ‘Load a Distribution’. When prompted “Enter a Host File: “, enter

> \<directory\>YS_501_129.KID (where \<directory\> represents the location where you stored the KIDS file).

3.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
4.  From this menu, you may elect to use the following options
    1.  Backup a Transport Global
    2.  Compare Transport Global to Current System
    3.  Verify Checksums in Transport Global
5.  Use the Install Package(s) options and select the package: YS_501_129.KID
6.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install?” respond NO.
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
8.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.
9.  If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

### YS\*5.01\*129 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ZIP file contains the MHA GUI executable and supporting files. Download the ZIP file and extract all the files.

> The following methods of installation are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

#### Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the MHA GUI executable (YS_MHA.exe) across the LAN.

> The MHA executable (YS_MHA.exe), along with the other files that are included in YS_501_129.ZIP, are copied to a network shared location. Since MHA is launched from CPRS, the item that starts up MHA on the ORWT TOOLS MENU should reflect the network location of YS_MHA.exe. Similarly, the parameter that specifies the location of the supporting DLL, YS MHA_AUX DLL LOCATION, needs to be edited to reflect the network location. See the section, File Location Parameters, to see examples of editing these parameters.

#### Citrix installation:

> The MHA executable (YS_MHA.exe) and supporting files are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to the manual installation method outlined below.

#### Manual install:

> This method is used primarily for advanced users and at testing locations.

> Note: You may need to have a user with Administrator rights complete this step.

> The following steps will update an existing installation of MHA, if one exists on the workstation. These steps use the default file locations.

1.  Locate the YS_501_129.ZIP file and unzip it.
2.  Copy the following files to the C:\Program Files (x86)\Vista\YS\MHA

> folder:

1.  YS_MHA.exe
2.  borlndmm.dll
3.  YS_MHA.GID
4.  YS_MHA.HLP
3.  Copy the following file to the C:\Program Files (x86)\Vista\Common Files folder:
    1.  YS_MHA_AUX.dll

> If desired, you may use different directories than those specific above, but you must also update the ORWT TOOLS MENU and YS MHA_AUX DLL LOCATION parameters to reflect the file locations.

#### SCCM Install

> An SCCM package is available for deployment to workstations at a site. To deploy via SCCM, request that the “Mental Health Assistant – R03” program be deployed.

### Setting MHA on the CPRS Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This procedure configures VistA so that “Mental Health Assistant” appears as a choice on a user’s Tools menu on the CPRS desktop software. Unlike previous versions of MHA, where this was optional, Version 3 of VistA MHA MUST be started from the CPRS Tools Menu. Selecting this choice from the CPRS Tools menu will offer the user full MHA3 functionality, based on a user’s particular access permissions in VistA.

> The basic steps for setting up VistA MHA3 on the Tools menu are no different from doing it for other applications. The main difference lies in how the Name=Command entry is formatted. The following text capture is taken from the CPRS Setup documentation, to serve as an example of how to perform this step for MHA3:

> Example: Setting up VistA MHA3 on the CPRS Tools menu, GUI Parameters \[ORW PARAM GUI\]

> From the previous example, adjust according to your own system’s settings, such as directory path, New Person Name and other parameters—consult the CPRS Setup Guide for the meaning of these parameters. The pertinent portion of the example is the “Name=Command:” field. This field should be entered in a single line—<u>no line-breaks allowed</u>, including all the % parameters that follow the filename and path to the MHA3 executable file.

> The path shown represents a typical path used during a default installation. If your path is different, adjust accordingly. ALL five parameters must be included as shown above, in the precise order in which they are found in the example. Here is what the Name=Command line should look like:

> Mental Health Assistant=”C:\Program Files (x86)\Vista\YS\MHA3\YS_MHA.exe” s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

> Sequence number 2 is shown in the example, but, if you have other entries in the Tools Menu, then the next free sequence number will do just fine. (Sometimes when cutting and pasting, unseen control characters can be included in the text and will cause the command line to malfunction.)

> After this step is completed, a new choice will appear in the user’s CPRS Tools Menu labeled “Mental Health Assistant”. Clicking on this menu entry will start MHA3 with a selected patient synchronized to the one currently selected in CPRS.

> Refer to the Computerized Patient Record System (CPRS) Setup Guide for more information about this procedure.

### Setting an Alternate DLL Location (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The default locations for the MHA auxiliary DLL is:

> YS_MHA_AUX.dll C:\Program Files (x86)\Vista\Common Files

> If you put the file in this location, no further action is necessary. If you wish to locate YS_MHA_AUX.dll in another location, you may edit the YS MHA_AUX DLL LOCATION parameter to set your preferred location. This may be done once for a site or division if all users have the same path in common. It may also be done at the individual user level. You can use General Parameter Tools to edit the parameter.

> Select PARAMETER DEFINITION NAME: YS MHA_AUX DLL LOCATION YS_MHA_AUX path

> and name

> YS MHA_AUX DLL LOCATION may be set for the following:

> 2 User USR \[choose from NEW PERSON\]

> 5 Division DIV \[choose from INSTITUTION\]

> 8 System SYS \[MHA-DEVA.FO-SLC.MED.VA.GOV\]

> Enter selection: 2 User NEW PERSON Select NEW PERSON NAME: MHPROVIDER,ONE

> --------- Setting YS MHA_AUX DLL LOCATION for User: MHPROVIDER,ONE --------

> AUX DLL: G:\Vista\Common\YS_MHA_AUX.dll Replace

> In the case shown above, the pertinent portion is what is entered at AUX DLL. In the example, YS_MHA_AUX.dll is located on a network drive at G:\VistA\Common\YS_MHA_AUX.dll. When MHA runs, it will look in that location for the DLL.

### Installation for Off-line Usage (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Some limited use of MHA is available when a connection to VistA is not possible. This may be useful in settings such as home health care. To use MHA in off-line mode, auxiliary DLL must be in the default directory, as follows:

> C:\Program Files (x86)\Vista\Common Files\YS_MHA_AUX.dll

> It is also necessary to start MHA directly, since CPRS does not run in off-line mode. To set up a shortcut so you can start MHA, do the following:

1.  Find the file, YS_MHA.exe, which is usually in the directory:

> C:\Program Files (x86)\Vista\YS\MHA .

2.  Select the file with the mouse.
3.  While holding the ALT key, drag the file to the desired location (usually the Desktop) and release the mouse.
4.  This will create a link that will allow you to start MHA directly.

> When MHA is started directly, it will warn you that you are running in off-line mode and verify that you want to do that.

### From: YS*5.01*181 Mental Health Deployment, Installation, Back-Out, and Rollback Guide

## Configure/Update MHA Web on the CPRS Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This procedure configures or updates VistA so that “MHA Web” appears as a choice on a user’s Tools menu on the CPRS desktop software. MHA Web must be started from the CPRS Tools Menu and should launch in a new browser window rather than appear as an additional tab on an existing browser session if one exists. Note that it must be decided ahead of time if Microsoft Edge or Google Chrome will be used for MHA Web at the site.

Go to the GUI TOOL Menu,  Select 4 for System. At the Select Sequence prompt, enter a question mark to see if MHA Web has already been set up in the Tools Menu. If it has, then select that sequence number. If it has not, then select a new sequence number to assign for MHA Web.

- Microsoft Edge

The Name=Command is  

MHA Web=cmd c/ start msedge.exe -new-window “https://\<server\>/app/home?station=\<station number\>&poi=%DFN” 

You need to substitute the \<server\> with the MHA Web server name “mha.med.va.gov” and the \<station number\> with your VistA instance station number. NOTE: there is only a single space between -new-window and the quoted URL.

- Google Chrome

The Name=Command is  

MHA Web=cmd c/ start chrome.exe -new-window “https://\<server\>/app/home?station=\<station number\>&poi=%DFN” 

You need to substitute the \<server\> with the MHA Web server name “mha.med.va.gov” and the \<station number\> with your VistA instance station number. NOTE: there is only a single space between -new-window and the quoted URL.

Example: The example below shows the set up of MHA Web on the CPRS Tools menu from the GUI TOOLS MENU \[ORW TOOL MENU ITEMS\] option:  

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

> **NOTE:** 999 is the example VistA Station number.

### From: YS*5.01*142 Mental Health Deployment, Installation, Back-Out, and Rollback Guide

### November 2019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 1.0

### Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)
> *.*
> Revision History
| Date    | Version | Description | Author                         |
|-------------|-------------|-----------------|------------------------------------|
| April 20190 | 1.0         | Initial Version | <span class="mark">REDACTED</span> |

## Appendix A - Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                 |
|-------------|----------------------------------------------------------------|
| CAG         | Citrix Access Gateway                                          |
| CD          | Critical Decision                                              |
| DIBO&RG     | Deployment, Installation, Back-out, and Rollback Guide         |
| IOC         | Initial Operating Capability                                   |
| MHA         | Mental Health Assistant                                        |
| PIN         | Personal Identification Number                                 |
| PIV         | Personal Identity Verification                                 |
| SPP         | Suicide Prevention Package                                     |
| SQA         | Software Quality Assurance                                     |
| SSOi        | Single Sign-On Integration                                     |
| VA          | Department of Veterans Affairs                                 |
| VAMC        | Veterans Affairs Medical Center                                |
| VIP         | Veteran-focused Integration Process                            |
| VistA       | Veterans Health Information System and Technology Architecture |

### From: YS*5.01*123 Mental Health Deployment, Installation, Back-Out, and Rollback Guide

### February 2019 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)
> *.*
> Revision History
| Date       | Version | Description                               | Author                         |
|----------------|-------------|-----------------------------------------------|------------------------------------|
| February 2019  | 1.3         | Updated version numbers, PC PTSD instructions | <span class="mark">REDACTED</span> |
| September 2018 | 1.2         | Updated for Patch 123                         | <span class="mark">REDACTED</span> |
| March 2018     | 1.1         | Updated version numbers, test sites           | <span class="mark">REDACTED</span> |
| May 2017       | 1.0         | Technical edits                               | <span class="mark">REDACTED</span> |
| May 2017       | 0.02        | Peer review input                             | <span class="mark">REDACTED</span> |
| April 2017     | 0.01        | Initial Version                               | <span class="mark">REDACTED</span> |

### YS\*5.01\*123 KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

1.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
2.  Next, select ‘Load a Distribution’. When prompted “Enter a Host File: “, enter

> \<directory\>YS_501_123.KID (where \<directory\> represents the location where you stored the KIDS file).

3.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
4.  From this menu, you may elect to use the following options
    1.  Backup a Transport Global
    2.  Compare Transport Global to Current System
    3.  Verify Checksums in Transport Global
5.  Use the Install Package(s) options and select the package: YS_501_123.KID
6.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install?” respond NO.
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' respond NO.
8.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.
9.  If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

### YS\*5.01\*123 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ZIP file contains the MHA GUI executable and supporting files. Download the ZIP file and extract all the files.

> The following methods of installation are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

#### Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the MHA GUI executable (YS_MHA.exe) across the LAN.

> The MHA executable (YS_MHA.exe), along with the other files that are included in

> YS_501_123.ZIP, are copied to a network shared location.

> When MHA files are not located in C:\Program Files (x86)\Vista\YS\MHA and C:\Program Files (x86)\Vista\YS\Common folders, parameters must be set up to ensure MHA works correctly since it is launched from the CPRS toolbar (see Section 4.5.3 below).

- Use the parameter, ”ORWT TOOLS MENU”, to enter the network location of

> YS_MHA.exe.

- Use the parameter, ”YS MHA_AUX DLL LOCATION”, to set the location of

> YS_MHA_AUX.dll.

> See the section 4.6.3, “Setting MHA on the CPRS Tools Menu”, and section 4.6.4, “Setting an Alternate DLL Location”, to see examples of editing these parameters.

> *If you are also running CPRS from a network drive* the file, YS_MHA_A_XE8.dll, must be copied to the CPRS directory when YS\*5.01\*123 is installed. This will replace the previous version of YS_MHA_A_XE8.dll that was used by CPRS.

#### Citrix installation:

> The MHA executable (YS_MHA.exe) and supporting files are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to the manual installation method outlined below.

#### Manual install:

> This method is used primarily for advanced users and at testing locations.

> Note: You may need to have a user with Administrator rights complete this step.

> The following steps will update an existing installation of MHA, if one exists on the workstation. These steps use the default file locations.

1.  Locate the YS_501_123.ZIP file and unzip it.
2.  Copy the following files to the C:\Program Files (x86)\Vista\YS\MHA

> folder:

1.  YS_MHA.exe
2.  borlndmm.dll
3.  YS MHA Help.chm
3.  Copy the following files to the C:\Program Files (x86)\Vista\Common Files folder:
    1.  YS_MHA_AUX.dll
    2.  YS_MHA_A_XE8.dll

> If desired, you may use different directories than those specified above, but you must also update the ORWT TOOLS MENU and YS MHA_AUX DLL LOCATION parameters to reflect the file locations.

#### SCCM install:

> An SCCM package is available for deployment to workstations at a site. To deploy via SCCM, request that the “Mental Health Assistant ” program be deployed.

### Monitor Background Re-Scoring (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](ys-5-01-123-mental-health-deployment-installation-back-out-and-rollback-guide/002.png)After the installation of YS\*5.01\*123, a job will be tasked that will re-score previously administered instruments to ensure that all results have been properly calculated. This job will run nightly for about 4 hours until all previous administrations have been re-scored. At test sites, this took about 1-4 nights. If you want to monitor the progress of the re-scoring, use the option, “YS123 RESCORING MONITOR”. Immediately after installation, you will see that the re- scoring task has been scheduled:

> The options available are:

- *Refresh (R)*: This updates the display; only useful while the rescoring task is actually running.
- *Browse (B)*: This allows you to browse errors that may have been encountered.
- *Quit (Q)*: This exits the monitoring view.

> ![](ys-5-01-123-mental-health-deployment-installation-back-out-and-rollback-guide/003.png)After rescoring is complete, the monitor will show something like this:

> It is likely that the number of Errors Encountered will be greater than 0. *This should not be cause for concern.* Over the years, it is likely that some of the instrument administrations could have some anomalies. The errors are just there for information. You don’t necessarily need to do anything to resolve them.

### From: YS*5.01*183 Mental Health Deployment, Installation, Back-Out, and Rollback Guide

### User Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The version of the application supported by this document is MHA v1.2.22.

### Add the Necessary Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new Security Keys are required.

### From: YS*5.01*148 Mental Health Deployment, Installation, Back-Out, and Rollback Guide

### April 2019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Version 1.0
