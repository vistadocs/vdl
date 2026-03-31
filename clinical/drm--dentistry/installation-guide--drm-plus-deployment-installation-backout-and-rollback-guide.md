---
consolidated_title: "drm plus deployment, installation, backout and rollback guide"
app_code: DRM+
doc_type: installation-guide
master_source: "DENT*1.2*91 DRM Plus Deployment, Installation, Backout and Rollback Guide"
master_pub_date: April 1989
consolidated_from: 4 versions
prior_versions:
  - "DENT*1.2*90 DRM Plus Deployment, Installation, Backout and Rollback Guide"
  - "DENT*1.2*92 DRM Plus Deployment, Installation, Backout and Rollback Guide"
  - "DENT*1.2*93 DRM Plus Deployment, Installation, Backout and Rollback Guide"
---

## Dental Record Manager Plus (DRM Plus) Application

## Deployment, Installation, Backout, and Rollback Guide

## DENT*1.2*91

<!-- image -->

## Version 1.2 April 1989 (VA Release) (Revised March 2025)

Department of Veterans Affairs Office of Information and Technology (OI&amp;T) Enterprise Program Management Office

## Revision History

When updates occur, the Title Page lists the new revised date, and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

| Date         |   Version | Description                                                                                                                                                                                                                                                                                                                                                                                  | Author   |
|--------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| March 2025   |       2.6 | Patch 91 Updates: • Updated Cover Page for Patch 91. • Updated 1.2 Dependencies • Updated 2 Roles and Responsibilities. • Updated 3.1 Timeline • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated 4.4 Database Creation • Updated 5.2.2 User Acceptance Testing • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure • Updated 6 Rollback Procedure | REDACTED |
| January 2025 |       2.5 | Patch 92 Updates: • Updated Cover Page for Patch 92. • Updated 1.2 Dependencies • Updated 2 Roles and Responsibilities. • Updated 3.1 Timeline • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated 4.4 Database Creation • Updated 5.2.2 User Acceptance Testing                                                                                                             | REDACTED |

|               |     | • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure • Updated 6 Rollback Procedure                                                                                                                                                                                                                                          |          |
|---------------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| June 2024     | 2.4 | Patch 90 Updates: • Updated Cover Page for Patch 90. • Updated 1.2 Dependencies • Updated 3.1 Timeline • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated 4.4 Database Creation • Updated 5.2.2 User Acceptance Testing • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure • Updated 6 Rollback Procedure | REDACTED |
| November 2023 | 2.3 | Patch 89 Updates: • Updated Cover Page for Patch 89. • Updated 1.2 Dependencies • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated 4.4 Database Creation • Updated 5.2.2 User Acceptance Testing • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure • Updated 6 Rollback Procedure                        | REDACTED |

| July 2023     |   2.2 | Patch 88 Updates: • Updated Cover Page for Patch 88. • Updated 1.2 Dependencies • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated 4.4 Database Creation • Updated 5.2.2 User Acceptance Testing • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure • Updated 6 Rollback Procedure   | REDACTED   |
|---------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| April 2023    |   2.1 | Patch 86 Updates: • Updated Cover Page for Patch 86 • Updated 1.2 Dependencies • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated 4.4 Database Creation • Updated 5.2.2 User Acceptance Testing • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure • Updated 6 Rollback Procedure    | REDACTED   |
| December 2022 |   2   | Patch 87 Updates: • Updated Cover Page for Patch 87 • Updated 1.2 Dependencies • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated 4.4 Database Creation • Updated 5.2.2 User Acceptance Testing                                                                                                                | REDACTED   |

<!-- image -->

|             |     | • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure • Updated 6 Rollback Procedure                                                                                                                                                                                                                             |          |
|-------------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| August 2022 | 1.9 | Patch 85 Updates: • Updated Cover Page for Patch 85 • Updated 1.2 Dependencies • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated Section 4 Installation references. • Updated 5.2.2 User Acceptance Testing • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure Updated 6 Rollback Procedure | REDACTED |
| March 2022  | 1.8 | Patch 84 Updates: • Updated Cover Page for Patch 84 • Updated 1.2 Dependencies • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated 4.4 Database Creation • Updated 5.2.2 User Acceptance Testing • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure • Updated 6 Rollback Procedure            | REDACTED |

| December 2021   |   1.7 | Patch 80 Updates: • Updated Patch information on Title Page. • Updated Dependencies. • Updated Test Site Information. • Updated Software Reqs. • Updated Database Creation. • Updated User Acceptance Testing. • Updated Backout Procedure. • Updated Backout Verification. • Updated Rollback Procedure.                    | REDACTED   |
|-----------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| December 2020   |   1.6 | Patch 79 Updates: • Updated Cover Page for Patch 79 • Updated 1.2 Dependencies • Updated 3.2.2 Site Information • Updated 3.3.3 Software • Updated 4.4 Database Creation • Updated 5.2.2 User Acceptance Testing • Updated 5.6 Backout Procedure • Updated 5.7 Backout Verification Procedure • Updated 6 Rollback Procedure | REDACTED   |
| December 2020   |   1.5 | Updated month to December. • Updated Roles and Responsibilities. • Updated Access Requirements.                                                                                                                                                                                                                              | REDACTED   |
| November 2020   |   1.4 | Updated month to November                                                                                                                                                                                                                                                                                                    | REDACTED   |
| October 2020    |   1.3 | • Updated dates. • Added Test Case #4 and Test Case #6.                                                                                                                                                                                                                                                                      | REDACTED   |

| August 2020   |   1.2 | • Added User Acceptance Tests. • Updated the Table of Contents.                                                                                                                                                                                                      | REDACTED   |
|---------------|-------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| July 2020     |   1.1 | Patch 78 Updates: • Updated Patch information on Title Page. • Updated Dependencies. • Updated Test Site Information. • Updated Software Requirements. • Updated Database Creation. • Updated Backout Procedure. • Updated Backout Verification. • Updated Rollback. | REDACTED   |

## Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point #2 (CD #2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

## Table of Contents

| 1 Introduction ............................................................................................................................................1   | 1 Introduction ............................................................................................................................................1   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.1                                                                                                                                                            | Purpose .........................................................................................................................................1             |
| 1.2                                                                                                                                                            | Dependencies................................................................................................................................1                  |
| 1.3 Constraints..........................................................................................................................................1     | 1.3 Constraints..........................................................................................................................................1     |
| 2 Roles and Responsibilities ................................................................................................................1                 | 2 Roles and Responsibilities ................................................................................................................1                 |
| 3 Deployment ............................................................................................................................................2     | 3 Deployment ............................................................................................................................................2     |
| 3.2.1 Deployment Topology (Targeted Architecture)...........................................................................2                                  | 3.2.1 Deployment Topology (Targeted Architecture)...........................................................................2                                  |
| 3.2.2 Site Information (Locations, Deployment Recipients).................................................................2                                    | 3.2.2 Site Information (Locations, Deployment Recipients).................................................................2                                    |
| 3.2.3 Site Preparation ...........................................................................................................................3            | 3.2.3 Site Preparation ...........................................................................................................................3            |
| 3.3 Resources............................................................................................................................................3     | 3.3 Resources............................................................................................................................................3     |
| 3.3.1 Facility Specifics ...........................................................................................................................3          | 3.3.1 Facility Specifics ...........................................................................................................................3          |
| 3.3.2 Hardware .....................................................................................................................................3          | 3.3.2 Hardware .....................................................................................................................................3          |
| 3.3.3 Software.......................................................................................................................................4         | 3.3.3 Software.......................................................................................................................................4         |
| 3.3.4 Communications ..........................................................................................................................4               | 3.3.4 Communications ..........................................................................................................................4               |
| 3.3.5 Deployment/Installation/Backout Checklist................................................................................4                               | 3.3.5 Deployment/Installation/Backout Checklist................................................................................4                               |
| Installation ..............................................................................................................................................5   | Installation ..............................................................................................................................................5   |
| 4.1 Preinstallation and System Requirements..........................................................................................5                         | 4.1 Preinstallation and System Requirements..........................................................................................5                         |
| 4.2 Platform Installation and Preparation ................................................................................................5                    | 4.2 Platform Installation and Preparation ................................................................................................5                    |
| 4.3 Download and Extract Files.................................................................................................................5               | 4.3 Download and Extract Files.................................................................................................................5               |
| 4.4 Database Creation...............................................................................................................................5          | 4.4 Database Creation...............................................................................................................................5          |
| 4.5 Installation Scripts...............................................................................................................................5       | 4.5 Installation Scripts...............................................................................................................................5       |
| 4.6 Cron Scripts .........................................................................................................................................5    | 4.6 Cron Scripts .........................................................................................................................................5    |
| 4.7 Access Requirements and Skills Needed for the Installation..............................................................5                                  | 4.7 Access Requirements and Skills Needed for the Installation..............................................................5                                  |
| 4.8 Installation Procedure.........................................................................................................................5           | 4.8 Installation Procedure.........................................................................................................................5           |
| 4.9 Installation Verification Procedure.....................................................................................................6                  | 4.9 Installation Verification Procedure.....................................................................................................6                  |
| 4.10 System Configuration........................................................................................................................6             | 4.10 System Configuration........................................................................................................................6             |
| 4.11 Database Tuning ...............................................................................................................................7          | 4.11 Database Tuning ...............................................................................................................................7          |
| 5 Backout Procedure ...............................................................................................................................7           | 5 Backout Procedure ...............................................................................................................................7           |

| 5.1 Backout Strategy.................................................................................................................................8   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 5.1.1 Mirror Testing or Site Production Testing....................................................................................8                     |
| 5.1.2 After National Release .................................................................................................................8          |
| 5.2 Backout Considerations ......................................................................................................................8       |
| 5.2.1 Load Testing .................................................................................................................................8    |
| 5.2.2 User Acceptance Testing..............................................................................................................9             |
| 5.3 Backout Criteria.................................................................................................................................13  |
| 5.4 Backout Risks ....................................................................................................................................13 |
| 5.5 Authority for Backout .......................................................................................................................13      |
| 5.6 Backout Procedure............................................................................................................................13      |
| 5.7 Backout Verification Procedure........................................................................................................14             |
| Rollback Procedure ............................................................................................................................14        |
| 6.1 Rollback Considerations....................................................................................................................15        |
| 6.2 Rollback Criteria................................................................................................................................16  |
| 6.3 Rollback Risks....................................................................................................................................16 |
| 6.4 Authority for Rollback.......................................................................................................................16      |
| 6.5 Rollback Procedure ...........................................................................................................................16     |
| 6.6 Rollback Verification Procedure........................................................................................................16            |

© 2025 Document Storage Systems, Inc.

## Introduction

This document describes how to deploy and install DENT*1.2*91 and how to backout the product and rollback to a previous version or data set. DENT*1.2*91 consists of both a KIDS build and dentalmrmtx executable.

## Purpose

The purpose of this plan is to provide a single, common document that describes how, when, where, and DENT*1.2*91 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

GUI:

DENT*1.2*90

KIDS:

DENT*1.2*59

DENT*1.2*69

DEMT*1.2*77

DENT*1.2*86

## Constraints

This patch is intended for a fully patched VistA system.

## Roles and Responsibilities

|   ID | Team                                               | Phase/Role                 | Tasks                           | Project Phase (See Schedule)   |
|------|----------------------------------------------------|----------------------------|---------------------------------|--------------------------------|
|    1 | Field Testing (Initial Operating Capability - IOC) | Deployment DSS manages IOC | Test for operational readiness. | Testing                        |

| 2   | Field Testing (Initial Operating Capability - IOC)   | Installation Region COTS Teams   | Plan and schedule installation.                                                                       | Deployment                   |
|-----|------------------------------------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------|------------------------------|
| ID  | Team                                                 | Phase/Role                       | Tasks                                                                                                 | Project Phase (See Schedule) |
| 3   | Field Testing (Initial Operating Capability - IOC)   | Backout Region OI&T, DSS, OOD    | Confirm availability of backout instructions and backout strategy (what criteria triggers a backout). | Deployment                   |

## Deployment

The deployment is planned as a national release.

## Timeline

The duration of deployment and installation is 30 days (requested).

## Site Readiness Assessment

This section discusses the locations that will receive the deployment of DENT*1.2*91.

## Deployment Topology (Targeted Architecture)

## ****NOTE****

DENT*1.2*91 is to be nationally released to all VAMCs using DRM Plus.

VAMCs using eDRM (Oracle Cerner) should NOT install the updated executable or the KIDS build released with this patch.

## Site Information (Locations, Deployment Recipients)

The IOC sites are:

## · REDACTED

Upon national release all VAMCs are expected to install this patch prior to or on the compliance date.

## Site Preparation

The following table describes preparation required by the site prior to deployment.

| Site/Other   | Problem/Change Needed   | Features to Adapt/Modify to New Product   | Actions/Steps   | Owner   |
|--------------|-------------------------|-------------------------------------------|-----------------|---------|
| N/A          | N/A                     | N/A                                       | N/A             | N/A     |

## Resources

## Facility Specifics

The following table lists facility-specific features required for deployment.

| Site   | Space/Room   | Features Needed   | Other   |
|--------|--------------|-------------------|---------|
| N/A    | N/A          | N/A               | N/A     |

## Hardware

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware   | Model   | Version   | Configuration   | Manufacturer   | Other   |
|---------------------|---------|-----------|-----------------|----------------|---------|

| Existing VistA system   | N/A   | N/A   | N/A   | N/A   | N/A   |
|-------------------------|-------|-------|-------|-------|-------|

## Software

The following table describes software specifications required at each site prior to deployment.

| Required Software                                      | Make   | Version                                         | Configuration   | Manufacturer   | Other   |
|--------------------------------------------------------|--------|-------------------------------------------------|-----------------|----------------|---------|
| Prerequisite patch for Dental Record Manager Plus KIDS | N/A    | DENT*1.2*77 DENT*1.2*69 DENT*1.2*59 DENT*1.2*86 | N/A             | N/A            | N/A     |
| Prerequisite patch for Dental Record Manager Plus GUI  | N/A    | DENT*1.2*90                                     | N/A             | N/A            | N/A     |

## Communications

The sites that are participating in field testing (IOC) will use the 'Patch Tracking' message in Outlook to communicate with DSS and product support personnel.

## Deployment/Installation/Backout Checklist

The Release Management team will deploy DENT*1.2*91, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in FORUM. FORUM automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in FORUM to identify when and by whom the patch was installed into the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch into their VistA production system.  Therefore, this information does not need to be manually tracked in the chart below.

| Activity   | Day   | Time   | Individual who completed task   |
|------------|-------|--------|---------------------------------|
| Deploy     | N/A   | N/A    | N/A                             |
| Install    | N/A   | N/A    | N/A                             |

## Installation

## Preinstallation and System Requirements

The DENT*1.2*91 Patch is installable on a VistA system with the prerequisite patches installed.

## Platform Installation and Preparation

Refer to the DENT*1.2*91 documentation and software retrieval in FORUM for the location of detailed installation instructions. These instructions include any preinstallation steps if applicable.

## Download and Extract Files

Refer to the DENT*1.2*91 patch description in FORUM to find related documentation that can be downloaded.

## Database Creation

DENT*1.2*91 Patch contains 1 new routine, DENTVU1.

## Installation Scripts

No installation scripts are needed for DENT*1.2*91 installation.

## Cron Scripts

No Cron scripts are needed for DENT*1.2*91 installation.

## Access Requirements and Skills Needed for the Installation

The software for this patch is being released in a PackMan message on

FORUM and is distributed to sites upon release.

Documentation describing the new functionality is included in this release.

Documentation can be found on the VA Software Documentation Library at: https://www.va.gov/vdl/.

Documentation can also be obtained at https://download.vista.med.va.gov/index.html/SOFTWARE.

The documentation includes:

| File Description   | File Name       | FTP Mode   |
|--------------------|-----------------|------------|
| Dental ZIP file    | DENT_1_2_91.ZIP | BINARY     |

The DENT\_1\_2\_91.zip file contains the following files:

| Title                                                                                                                                        | File Name                                                                     | FTP Mode                    |
|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|-----------------------------|
| DRM Plus Release Notes DRM Plus Installation Guide DRM Plus Technical Manual DRM Deployment, Installation, Backout & Rollback Guide (DIBORG) | DENT_1_2P91_RN.pdf DENT_1_2P91_IG.pdf DENT_1_2P91_TM.pdf DENT_1_2P91_DIBR.pdf | Binary Binary Binary Binary |

## Installation Procedure

Installation instructions are included in the patch description for DENT*1.2*91 which is distributed to sites through the National Patch Module in Forum upon national release. The installation guide for DENT*1.2*91 can be found on the VA Software Documentation Library at: https://www.va.gov/vdl/ or obtained at https://download.vista.med.va.gov/index.html/SOFTWARE.

## Installation Verification Procedure

Refer to the DENT*1.2*91 documentation and software retrieval in FORUM for the location of detailed installation instructions. These instructions include any postinstallation steps if applicable.

## System Configuration

No system configuration changes are required for this patch.

## Database Tuning

No reconfiguration of the VistA database, memory allocations or other resources is necessary.

## Backout Procedure

A DRM Plus backout would include backing out all of the components of a DRM Plus installation from a current patch.  If only a KIDS build is included in the patch to be backed out, then all that would be required for a back out would be the KIDS back out. If only a dentalmrmtx executable was included in a patch, then all that would be required for a back out would be the dentalmrmtx executable back out.  If only a setupPxx executable was included in a patch then all that would be required for a back out would be the setupPxx back out.  With DRM Plus patches, it is possible that different combinations of these components would be included so it is important to note what is included in the patch to be backed out from and what was included in the patch to be backed up to.

## KIDS Roll Back:

Directions for backing up a global are included in each DRM Plus Patch Description and Installation guide.  It is this back up global that would be used to back out of the installed patch to the previous version of DRM Plus M routines.

All users should not access the DRM Plus application(dentalmrmtx.exe) during a backout.  If this cannot be coordinated with the Dental Service Chief, then removing the CPRS command line of DRM Plus (DRM Plus can only be accessed through CPRS) will not allow access of the DRM Plus application to any user.  If the command line is removed prior to a back out, it must be replaced as soon as a successful back out is confirmed.

These procedures include the process of backing out of all the possible DRM Plus components that could be included in a patch release.

## GUI Roll Back:

To back out the dentalmrmtx executable included with the patch, the dentalmrmtx executable would need to be replaced by the dentalmrmtx executable to the previous version of DRM Plus.

These procedures include the process of backing out of all the possible DRM Plus components that could be included in a patch release.

## Backout Strategy

The vendor of Dental Record Manager Plus, Document Storage Systems, Inc., recommends that any site backing out of any component of any DRM Plus patch contact DRM Plus Technical Support at REDACTED or email REDACTED for assistance.

## Mirror Testing or Site Production Testing

Please note: backout can vary in complexity depending on whether you are backing out DRM Plus in its entirety or only one or two specific components.  Dental Record Manager Plus is a Class 1 COTS vendor supported product.  Sites should call DRM Plus Technical Support at REDACTED or email REDACTED for assistance.

## After National Release

Please note: backout can vary in complexity depending on whether you are backing out DRM Plus in its entirety or only one or two specific components.  Dental Record Manager Plus is a Class 1 COTS vendor supported product.  Sites should call DRM Plus Technical Support at REDACTED or email REDACTED for assistance.

## Backout Considerations

Please note: backout can vary in complexity depending on whether you are backing out DRM Plus in its entirety or only one or two specific components.  Dental Record Manager Plus is a Class 1 COTS vendor supported product.  Sites should call DRM Plus Technical Support at REDACTED or email REDACTED for assistance.

## Load Testing

Not Applicable.  The performance demands on the system will be unchanged.

## User Acceptance Testing

Below are the acceptance criteria for each test case included in DENT*1.2*91.

Test Case #1 - Changed "Reference" field label to "Model" in Device Tracking to match the text populated in Progress Notes.

Acceptance Criteria: 'Model' shows in both Device Tracking and Progress Note text.

<!-- image -->

Test Case #2 - Added legal boilerplate and additional text to the "About…" screen as per VA requirements.

Acceptance Criteria: The required text and legal disclaimer displays in the 'About…' screen.

<!-- image -->

Test Case #3 - Added check and filter for control characters in Speed Codes.

Acceptance Criteria: Control characters are filtered when inputting into Speed Code names and descriptions.

<!-- image -->

Test Case #4:Corrected an error when completing CPRS templates.

Acceptance Criteria: CPRS template opens in DRM Plus without an error popping up first.

<!-- image -->

Test Case #5 - Adjusted verbiage for PCE data filing in confirmation message.

Acceptance Criteria: PCE confirmation message notifies user if data may not have filed and recommends checking PCE.

<!-- image -->

Test Case #6 - Added catch to prevent errors for potential duplicate incomplete D2940 transactions.

Acceptance Criteria: DRM Plus loads without errors.

<!-- image -->

Test Case #7 - Updated "Panel Add/Edit" screen to allow for partial panel moves, removal of deceased patients from panels, and changed Fee Basis to Integrated Veteran Care in provider table.

Acceptance Criteria: The new layout for the 'Panel Add/Edit' displays in DRM Plus when launched.

<!-- image -->

## Backout Criteria

It may be decided to back out this patch if the project is canceled, the requested changes implemented by DENT*1.2*91 are no longer desired by VistA Applications and Office Information &amp; Technology (OIT), Development, Security and Operations (DevSecOps), and the Office of Dentistry, or the patch produces catastrophic problems.

## Backout Risks

Please note: backout can vary in complexity depending on whether you are backing out DRM Plus in its entirety or only one or two specific components.  Dental Record Manager Plus is a Class 1 COTS vendor supported product.  Sites should call DRM Plus Technical Support at REDACTED or email REDACTED com for assistance.

## Authority for Backout

Please note: backout can vary in complexity depending on whether you are backing out DRM Plus in its entirety or only one or two specific components.  Dental Record Manager Plus is a Class 1 COTS vendor supported product.  Sites should call DRM Plus Technical Support at REDACTED or email REDACTED for assistance.

## Backout Procedure

A DRM Plus backout would include backing out all of the components of a DRM Plus installation from a current patch. For DENT*1.2*91 there is both a KIDS build and dentalmrmtx executable in the patch.  Both the KIDS build and dentalmrmtx executable are required for a backout.

The KIDS  backup created prior to install can be used to back out the installed patch to the previous version of DRM Plus M routines.

The backup steps are as follows:

1. Using Mailman, READ the backup message which begins with Backup of...
2. At the Mailman message action prompt enter X to extract the PackMan message.

3. At the Select PackMan function option select INSTALL/CHECK MESSAGE. Answer YES  to 'Want to Continue with the Load? No/' YES.
4. Select the 'Installation' menu on the Kernel Installation &amp; Distribution menu.
5.  Use  the  option  'Install  Package(s)  and  when  prompted  for  INSTALL  NAME  enter 'DENT*1.2*91b'.
6. When prompted 'Want KIDS TO INHIBIT LOGONs during the install? NO//' accept the default.
7. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' accept the default.
8. When prompted 'Enter the Device you want to print the Install messages. You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

DEVICE: HOME//' accept the default home and the Install Completed message will write to the screen.

## ***DO NOT QUEUE INSTALL OF THE BACKOUT***

Contact Help desk to log a ticket with DSS to assist with rolling back data and removing routines modified by this patch.

To back out the dentalmrmtx executable (version 9.1.0.14) included with the patch, the dentalmrmtx executable would need to be replaced by the dentalmrmtx executable (version 9.0.0.4) released with DENT*1.2*90.

## Backout Verification Procedure

The backup steps are as follows:

1. After Loading a Distribution, Select the Backup a Transport Global option.  This global is a MailMan message.

> **NOTE:** without this step, you cannot roll back.

2. Using Mailman, READ the backup message which begins with Backup of...
3. At the Mailman message action prompt enter X to extract the PackMan message.

4. At the Select PackMan function option select INSTALL/CHECK MESSAGE.
5. Answer YES that you want to perform the function.
6. Answer NO to preserve a copy of the backup in another message. Contact Help desk to log a ticket and DSS to assist with entering the routines from the temp global

Successful backout is confirmed by verification that the checksums match as following:

DENTVA2 B44383866

DENTVA3 B26287253

DENTVA7 B69580370

DENTVPA

B78126672

DENTVPD B49616067

The executable version can also be confirmed as 9.0.0.4 in the event of a backout.

## Rollback Procedure

Rollback pertains to data. DENT*1.2*91 contains one new routine, DENTVUT1. All other changes are covered in the backout procedures detailed elsewhere in the document.

The backup steps are as follows:

1. After Loading a Distribution, Select the Backup a Transport Global option.  This global is a MailMan message.

> **NOTE:** without this step, you cannot roll back.

2. Using Mailman, READ the backup message which begins with Backup of...
3. At the Mailman message action prompt enter X to extract the PackMan message.
4. At the Select PackMan function option select INSTALL/CHECK MESSAGE.
5. Answer YES that you want to perform the function.
6. Answer NO to preserve a copy of the backup in another message.

Contact Help desk to log a ticket and DSS to assist with entering the routines from the temp global

## Rollback Considerations

Not applicable.

## Rollback Criteria

Not applicable.

## Rollback Risks

Not applicable.

## Authority for Rollback

Not applicable.

## Rollback Procedure

Not applicable.

## Rollback Verification Procedure

Not applicable.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DENT*1.2*93 DRM Plus Deployment, Installation, Backout and Rollback Guide

## Version 1.2 April 1989 (VA Release)

## Edited ADA Codes for January 1 st , 2026:

- D0171; RVU 0
- D0372; RVU 40
- D0709; RVU 0
- D1320; RVU 5
- D2642; RVU 120
- D4266; RVU 15
- D4921; RVU 0
- D5932; RVU 250
- 15780; RVU 180
- 15781; RVU 30
- 15782; RVU 0
- 69714; RVU 0

## Inactivated ADA Codes for January 1 st , 2026:

- D1352
- D1705
- D1706
- D1707
- D1712
- D9248
- 10040
- 99441
- 99442
- 99443

## INACTIVE DATE field (.02) removed:

- D1352
- D1705
- D1706
- D1707
- D1712
- D9248
- 10040
- 99441
- 99442
- 99443

Successfully back out of the build/routines can be verified by confirming routine DENTV093 has been deleted.

2.  Using 'List Routines' [XUPRROU] option, verify routineDENTV093 added by DENT*1.2*93 was deleted.

### From: DENT*1.2*90 DRM Plus Deployment, Installation, Backout and Rollback Guide

## Deployment/lnstallation/Backout Checklist

The Release Management team will deploy DENT*1.2*90, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in FORUM. FORUM automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in FORUM to identify when and by whom the patch was installed into the VistA production at each site. A report can also be run to identify which sites have

4

| Activity   | Day   | Time   | Individual who completed task   |
|------------|-------|--------|---------------------------------|
| Deploy     | N/A   | N/A    | N/A                             |
| Install    | N/A   | N/A    | N/A                             |

<!-- image -->
