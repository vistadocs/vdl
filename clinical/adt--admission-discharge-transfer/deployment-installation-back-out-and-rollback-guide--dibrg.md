---
consolidated_title: "dibrg"
app_code: ADT
doc_type: DIBR
master_source: "DG*5.3*952 DIBRG"
master_pub_date: February 2020
consolidated_from: 9 versions
prior_versions:
  - "DG*5.3*1016 DIBRG"
  - "DG*5.3*1025 DIBRG"
  - "DG*5.3*1029 DIBRG"
  - "DG*5.3*1034 DIBRG"
  - "DG*5.3*1035 DIBRG"
  - "DG*5.3*1047 DIBRG"
  - "DG*5.3*916 DIBRG"
  - "DG*5.3*977 DIBRG"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Suicide High Risk Patient Enhancements (SHRPE)

  DG\*5.3\*952 and IVM\*2.0\*184

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](dg-5-3-952-dibrg/001.png)

February 2020

Revision History

<table>
<caption><p>Table 1: Deployment, Installation, Back-out, and Rollback Roles, and Responsibilities</p></caption>
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
<td>02/07/2020</td>
<td>10.0</td>
<td>Added missing pre-requisite patch to the 1.2. Dependencies section.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/15/2020</td>
<td>9.0</td>
<td>Addressed issues reported by HPS.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/03/2019</td>
<td>8.0</td>
<td>Removed references to DG*5.3*914.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/03/2019</td>
<td>7.0</td>
<td>Changes for section 5.7 Back-out Verification Procedure.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/05/2019</td>
<td>6.0</td>
<td><p>Changed the name of the OTH eligibility from EXPANDED MH CARE NON-VETERANS to EXPANDED MH CARE NON-ENROLLEE:</p>
<p>Added new dependencies for DG*5.3*952</p>
<p>Updated KID build filename.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/18/2019</td>
<td>5.0</td>
<td>IVM*2.0*184 information was added to the document because DG*5.3*952 and the new IVM*2.0*184 patch are bundled and will be installed together.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/29/2019</td>
<td>4.0</td>
<td>Updated information and instructions regarding new components have been added to the patch.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/02/2018</td>
<td>3.0</td>
<td>Updated information and instructions regarding new components have been added to the patch.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/6/2018</td>
<td>2.0</td>
<td>Information and instructions regarding new components have been added to the sections 5.6 and 5.7</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>4/16/2018</td>
<td>1.0</td>
<td>Initial Draft</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table 1: Deployment, Installation, Back-out, and Rollback Roles, and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

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
  - [Pre-Installation and System Requirements](#pre-installation-and-system-requirements)
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
    - [Mirror Testing or Site Production Testing](#mirror-testing-or-site-production-testing)
    - [After National Release but During the Designated Support Period](#after-national-release-but-during-the-designated-support-period)
    - [After National Release and Warranty Period](#after-national-release-and-warranty-period)
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
This document describes how to deploy and install the Veterans Information Systems and Technology Architecture (VistA) Registration patch DG\*5.3\*952 and Income Verification Match (IVM) patch IVM\*2.0\*184*,* as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.
Modifications are needed to VistA to ensure former service members with an Other Than Honorable (OTH) administrative discharge, and their eligibility for emergency mental health care services, are identifiable in the electronic health record, and VA staff can track the former service member’s status within a 90‑day episode of care.
The current process does not allow the health care team to readily identify a former service member’s OTH discharge type and eligibility status in the electronic health record when they are treated under Emergent mental health (MH) care authority.
The current process does not capture and track where the former service member falls within the 90-day episode of care during provision of mental health care.
The current process does not allow the health care team to view former service members with OTH administrative discharges and their eligibility and 90-day status in CPRS for emergency mental health care services.
The challenges to the current process will be addressed with the following enhancements:
- A new EXPANDED MH CARE TYPE value “OTH-90” will be implemented in VistA. This new code identities former service members with an OTH discharge type that are treated under Emergent MH care authority to Veterans Health Administration (VHA) healthcare team members and allows them to be tracked. The new code will display in Registration and CPRS.
- Per VA policy, VHA DIRECTIVE 1601A.02, the former service member is allowed two 90-day episodes of care within a 365-day period. The Veterans Integrated Service Network (VISN) Chief Medical Officer must approve a second 90-day episode of care. The 90-Day Status will consist of a countdown clock to be displayed in CPRS. This clock will inform VHA healthcare team members the number of days remaining within a 90‑day episode of care. The countdown clock is initiated at the number 90, decrements by 1 daily, and counts down to zero. A value of 90 indicates that the 90-Day Episode of Care has started, and a value of zero indicates that the 90-Day Episode of Care has expired. New Registration menu options will provide functionality to allow DG staff to manage the OTH clock start dates and enter/edit required authorization for the 2<sup>nd</sup> 90-days period.
- OTH status displayed on the CPRS screen.
To meet the objectives of these OTH Enhancements (SHRPE), the solution will be deployed in two parts.
The first part is a bundle of the Registration patch DG\*5.3\*952 and Income Verification Match (IVM) patch IVM\*2.0\*184, which will:
- Introduce the new EXPANDED MH CARE NON-ENROLLEE eligibility in the ELIGIBILITY CODE (#8) and MAS ELIGIBILITY CODE (#8.1) files.
- Add new EXPANDED MH CARE TYPE (#.5501) field to the PATIENT (#2) file to indicate EXPANDED MH CARE TYPE value “OTH-90” for the Emergent OTH authority.
- Create the new file OTH ELIGIBILITY PATIENT (#33) to track patients eligible for VA care under Emergent OTH authority.
- Add new functionality to the Registration Menu \[DG REGISTRATION MENU\] option to manage Emergent OTH authority patients. The following menu options and submenus have been added:
> Other Than Honorable Patients Menu \[DG OTH MENU\]
> OTH Management \[DG OTH MANAGEMENT\]
> Patient Inquiry (OTH) \[DG OTH PATIENT INQUIRY\]
> Other Than Honorable Reports \[DG OTH REPORTS MENU\]
> Tracking Report (OTH-90) \[DG OTH 90-DAY PERIOD\]
> Authorization Reports (OTH-90) \[DG OTH OTH90 AUTH REPORTS\]
> Other Than Honorable MH Status Report \[DG OTH MH STATUS REPORT\]
> Potential 'OTH' Patient Report \[DG OTH POTENTIAL OTH\]
- Modify the HL7 VistA software to include OTH data in transmissions between VistA and Enrollment System (ES).
- Modify the HL7 messaging to include OTH clock related fields in Z07 HL7 messages that are sent Enrollment System (ES).
- Modify the HL7 messaging code to process OTH clock related fields in Z11 HL7 messages that are sent by ES to VistA.
- Provide the new API to be used by CPRS to provide OTH information to display it on the CPRS screen. The API is covered by the Controlled Subscription ICR (#6873) DG OTH ELIGIBILITY PATIENT STATUSICR.
- Add the new OTH menu to Registration with options to manage the OTH clock.
- Introduce OTH reports.
The second part is delivered with the CPRS v31b patch OR\*3.0\*377, which will:
- Contain the new OR routine OROTHCL that will use the new DG OTHBTN^DGOTHBTN API introduced by DG\*5.3\*952.
- Contain a new OR OTHD CLOCK GET RPC that uses the code in OROTHCL to provide OTH clock information to CPRS GUI application.
Please refer to CPRS v31b documentation in regard to deployment, installation, back-out, and rollback instructions.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the VistA Registration patch DG\*5.3\*952 and Income Verification Match (IVM) patch IVM\*2.0\*184 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies existing VistA Registration routines to provide new functionality that addresses changes for Emergent OTH patients.

- DG\*5.3\*504, DG\*5.3\*887, DG\*5.3\*903, DG\*5.3\*972 and DG\*5.3\*978 must be installed before DG\*5.3\*952.
- IVM\*2.0\*164 must be installed before IVM\*2.0\*184.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be installed in all VA VistA production sites. This patch is intended for a fully patched VistA system. Its installation will not noticeably impact the production environment.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID | Team                                                                                                        | Phase / Role | Tasks                                                                                                                       | Project Phase (See Schedule) |
|--------|-----------------------------------------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | VA OI&T, VA OI&T Health Product Support & PMO                                                                   | Deployment       | Plan and schedule deployment (including orchestration with vendors).                                                            | Planning                         |
| 2      | Local Individual Veterans Administration Medical Centers (VAMCs)                                                | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                                      | Planning                         |
| 3      | Field Testing (Initial Operating Capability - IOC), Health Product Support Testing & VIP Release Agent Approval | Deployment       | Test for operational readiness.                                                                                                 | Testing                          |
| 4      | Health Product Support and Field Operations                                                                     | Deployment       | Execute deployment.                                                                                                             | Deployment                       |
| 5      | VAMCs                                                                                                           | Installation     | Plan and schedule installation.                                                                                                 | Deployment                       |
| 6      | VIP Release Agent                                                                                               | Installation     | Obtain authority to operate and that certificate authority security documentation is in place.                                  | Deployment                       |
| 7      | N/A for this patch as we are using only the existing VistA system                                               | Installation     | Validate through facility Point of Contact (POC) to ensure that IT equipment has been accepted using asset inventory processes. | Deployment                       |
| 8      | The VA’s SHRPE team                                                                                             | Installations    | Coordinate knowledge transfer with the team responsible for user training.                                                      | Deployment                       |
| 9      | VIP release Agent, Health Product Support & the development team                                                | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).            | Deployment                       |
| 10     | SHRPE Team                                                                                                      | Post-Deployment  | Hardware, Software, and System Support.                                                                                         | Warranty                         |

Table 2: Site Preparation

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national rollout.

This section provides the schedule and milestones for the deployment.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The duration of deployment and installation is 30 days. A detailed schedule will be provided during the build.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the DG\*5.3\*952 and IVM\*2.0\*184 patch deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Registration patch DG\*5.3\*952 and IVM\*2.0\*184 should be installed in all VA VistA production sites.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The test sites for IOC testing are:

- Atlanta VA Health Care System (508)
- N FL/S GA Health System (573)
- Palo Alto VA Health Care System (640)

Upon national release all VAMCs are expected to install this patch prior to or on the compliance date. The software will be distributed as a host file, which will be posted in ftp sites:

- Hines: fo-hines.med.va.gov
- Salt Lake City: fo-slc.med.va.gov

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No site-specific preparations are needed for this patch. The VA site should follow the standard procedure they are using now for installation of VistA patches (Table 2).

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            | N/A                       | N/A                                         | N/A               | N/A       |

Table 3: Facility Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no additional resources required for installation of these patches.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific features (Table 3) required for deployment of this patch.

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |

Table 4: Hardware Specifications

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special requirements regarding new or existing hardware capability. Existing hardware resources will not be impacted by the changes in this project.

Table 4 describes hardware specifications required at each site prior to deployment.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| Existing VistA system | N/A       | N/A         | N/A               | N/A              | N/A       |

Table 5: Software Specifications

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 5 describes the software specifications required at each site prior to deployment.

<table style="width:100%;">
<caption><p>Table 6: Deployment/Installation/Back-Out Checklist</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Software</strong></th>
<th><strong>Make</strong></th>
<th><strong>Version</strong></th>
<th><strong>Configuration</strong></th>
<th><strong>Manufacturer</strong></th>
<th><strong>Other</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Fully patched Registration package within VistA</td>
<td>N/A</td>
<td>5.3</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>DG*5.3*504</td>
<td>N/A</td>
<td><p>Nationally</p>
<p>released</p>
<p>version</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>DG*5.3*972</td>
<td>N/A</td>
<td><p>Nationally</p>
<p>released</p>
<p>version</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>DG*5.3*903</td>
<td>N/A</td>
<td><p>Nationally</p>
<p>released</p>
<p>version</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>DG*5.3*978</td>
<td>N/A</td>
<td><p>Nationally</p>
<p>released</p>
<p>version</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>IVM*2.0*164</td>
<td>N/A</td>
<td><p>Nationally</p>
<p>released</p>
<p>version</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

Table 6: Deployment/Installation/Back-Out Checklist

Please see the *Deployment*, *Installation, Back-out, and Rollback Roles, and* Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites that are participating in field testing IOC will use the “Patch Tracking” message in Outlook to communicate with the SHRPE team, the developers, and product support personnel.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy patches DG\*5.3\*952 and IVM\*2.0\*184, which are tracked nationally for all VAMCs in the National Patch Module (NPM) in FORUM. FORUM automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in FORUM to identify when the patch was installed in the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch in their VistA production system. Therefore, this information does not need to be manually tracked in Table 6.

| Activity | Day | Time | Individual who completed task |
|--------------|---------|----------|-----------------------------------|
| Deploy       | N/A     | N/A      | N/A                               |
| Install      | N/A     | N/A      | N/A                               |
| Back-Out     | N/A     | N/A      | N/A                               |

Deployment/Installation/Back-Out ChecklistA report can also be run, to identify which sites have not currently installed the patch in their VistA production system. Therefore, this information does not need to be manually tracked in this table.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*952, a patch to the existing VistA Registration 5.3 package, and IVM\*2.0\*184, a patch to the existing VistA Income Verification Match 2.0 package, are installable as a bundle (a host file with the combined build) on a fully patched Massachusetts General Hospital Utility Multi-Programming System (MUMPS) VistA system and operates on top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities that communicate with the underlying operating system and hardware, thereby providing Registration and Income Verification Match independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the DG\*5.3\*952 and IVM\*2.0\*184 Patch Descriptions on the NPM in FORUM for the detailed installation instructions. These instructions would include any pre-installation steps, if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the DG\*5.3\*952 and IVM\*2.0\*184 documentation on the NPM to find related documentation that can be downloaded. DG\*5.3\*952 and IVM\*2.0\*184 combined build host file DG_53_P952.KID will be made available for downloading from VA sftp sites.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch is applied to an existing MUMPS VistA database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the DG\*5.3\*952 and IVM\*2.0\*184 Patch Descriptions in the NPM for installation instructions.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for the DG\*5.3\*952 and IVM\*2.0\*184 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to National VA Network, as well as the local network of each site to receive DG patches, is required to perform the installation, as well as authority to create and install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the DG\*5.3\*952 and IVM\*2.0\*184 Patch Descriptions documentation on the NPM in FORUM for detailed installation instructions.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, the user verifies installation results by using the “Install File Print” menu option in the “Utilities” submenu of the Kernel Installation & Distribution System.

Also refer to the DG\*5.3\*952 and IVM\*2.0\*184 documentation on the NPM for detailed installation instructions. These instructions include any post-installation steps, if applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required for this patch.

Refer to the DG\*5.3\*952 and IVM\*2.0\*184 patch documentation in the NPM for information concerning new or modified security keys and assignment of user privilege.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocations, or other resources is necessary.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the Enterprise Service Desk (ESD) to submit a ticket; the development team will assist with the process.

The Back-Out Procedure consists of restoring routines and manually removing each new Data Dictionary (DD) definition component introduced by the patch.

The back-out is to be performed by persons with programmer-level access, and in conjunction with the SHRPE Team.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although it is unlikely due to care in collecting, elaborating, and designing approved user stories, followed by multiple testing stages such as the Developer Unit Testing, Component Integration Testing, SQA Testing, and User Acceptance Testing, a back-out decision due to major issues with this patch could occur. A decision to back out could be made during site Mirror Testing, Site Production Testing or after National Release to the field VAMCs. The best strategy decision is dependent on the severity of the defects and the stage of testing during which the decision is made.

### Mirror Testing or Site Production Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If during Mirror testing or Site Production Testing, a new version of a defect correcting test patch is produced, retested, and successfully passes development team testing, it will be resubmitted to the site for testing. If the patch produces catastrophic problems, a new version of the patch can be used to restore the build components to their pre-patch condition.

### After National Release but During the Designated Support Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA KIDs builds cannot be backed out/restored in totality—only routines are part of a backup transport global. Special care is taken during development of VistA code (routines, files, remote procedures, etc.) to make them backward compatible with newer GUI versions to alleviate the issue and avoid typical critical scenario solutions such as emergency patches.

The decision to back out a specific release needs to be made in a timely manner. Catastrophic failures are usually known early in the testing process—within the first two or three days. Sites are encouraged to perform all test scripts to ensure new code is functioning in their environment, with their data. A back-out should only be considered for critical issues or errors. The normal or an expedited, issue-focused patch process can correct other bugs.

The general strategy for SHRPE VistA functionality rollback will likely be to repair the code with another follow-on patch.

If any issues with SHRPE Vista software are discovered after it is nationally released and within the 90-day warranty period, the SHRPE development team will research the issue and provide guidance for any immediate, possible workaround. After discussing the defect with VA and receiving their approval for the proposed resolution, the SHRPE development team will communicate guidance for the long-term solution to the field.

The long-term solution will likely be the installation of a follow-up patch to correct the defect, a follow-up patch to remove the SHRPE updates, or a detailed set of instructions on how the software can be safely backed out of the production system.

In addition, at the time of deployment, local sites can perform the following steps:

1.  At the time of system deployment, create a complete backup of the current system and store it on a separate machine.
2.  Continue with application-specific system deployment steps.
1.  If the system fails during deployment, perform a system rollback using the system backup created in Step 1.
3.  Perform thorough and comprehensive testing to ensure the integrity and functionality of the system is intact.
4.  Perform a system backup once the system is deemed stable and ready for users, and store it on a separate machine.
1.  Once users begin working on the system, regularly create system backups and store them on another machine.

If system failure occurs after users are on the system, perform a system rollback using the system backup created in Step 4a.

### After National Release and Warranty Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the support period, the VistA Maintenance Program would produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if a wholesale back-out of the DG\*5.3\*952 and IVM\*2.0\*184 patches is needed or if a better course of action is needed to correct through a new version of the patch (if prior to national release) or a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale back-out of the patches will still require a new version (if prior to national release) or a subsequent patch(es) (after national release). If the back-out is post-release of patch DG\*5.3\*952 and IVM\*2.0\*184, these patches should be assigned the status of “Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation process of the back-out patches, which would be executed at normal, rather than raised job priority, is expected to have minimal effect on total system performance. To minimize the potential impact on users, installation of the back-out patches can be queued to run during hours of reduced user activity. Subsequent to the reversion, the performance demands on the system would be slightly decreased as less data would be filed per transaction.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The results will be provided upon the completion of the User Acceptance Testing.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The project is canceled, the requested changes implemented by DG\*5.3\*952 and IVM\*2.0\*184 are no longer desired by VA OI&T, or the patches produce catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out DG\*5.3\*952 and IVM\*2.0\*184 patches, the local facility will not be able to provide SHRPE functionality implemented by the patch:

- Process HL7 messages with OTH data that allows to keep VistA systems and ES in sync in regard to the OTH eligibility and OTH 90-day periods (OTH clocks) across all the VA sites.
- The new EXPANDED MH CARE TYPE value “OTH-90” identities former service members with an OTH discharge type to VHA healthcare team members, that are eligible to receive emergent MH care and allows them to be tracked. The new value will display in Registration and CPRS.
- Per VA policy, the former service member is allowed two 90-day episodes of care within a 365-day period. The VISN Chief Medical Officer must approve a second 90-day episode of care. The 90-Day Status will consist of a countdown clock to be displayed in CPRS. This clock will inform VHA healthcare team members the number of days remaining within a 90‑day episode of care. The countdown clock is initiated at the number 90, decrements by 1 daily, and counts down to zero. A value of 90 indicates that the 90-Day Episode of Care has started, and a value of zero indicates that the 90-Day Episode of Care has expired. New Registration menu options will provide functionality to allow DG staff to manage the OTH clock start dates and enter/edit required authorization for the 2<sup>nd</sup> 90-day period.
- OTH status displayed on the CPRS screen.

The current changes made in the patch don’t affect other applications and thus the backing out the software should not pose any issues.

The project is still under development so there are chances that dependencies with other applications are introduced and if this happens then this section will need to be re-evaluated to determine potential risks.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The order would come from: Portfolio Director, VA Project Manager and Business Owner. Health Product Support will work to identify the problem and assisting with implementation. This should be done in consultation with the development team and project stakeholders. 

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA rollback is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch. The DG\*5.3\*952 and IVM\*2.0\*184 patches contain the following build components:

- Routines

The pre-patch versions of routines can be restored by using backup MailMan message that should be created during installation.

> **NOTE:** The routines can be modified by another patch that follows the DG\*5.3\*952 and IVM\*2.0\*184 and released after the installation of the DG\*5.3\*952 and IVM\*2.0\*184. In this case, restoring routines from the backup MailMan message might cause issues. It is recommended that the sites contact the development team and the Health Product Support team after for specific solutions to their unique problems.

- Data dictionaries

The following data dictionaries in the environment need to be restored to their previous state by the back-out patch that needs to be designed for this:

> PATIENT file (#2)

> PATIENT ENROLLMENT file (#27.11)

> ELIGIBILITY CODE file (#8)

> MAS ELIGIBILITY CODE file (#8.1)

The new OTH ELIGIBILITY PATIENT file (#33) can be deleted by the back-out patch that needs to be designed for this.

- Options

The following new entries in the OPTION file (#19) can be deleted by the back-out patch that needs to be designed for this:

Option Name

-----------

DG OTH 90-DAY PERIOD

DG OTH MANAGEMENT

DG OTH MENU

DG OTH MH STATUS REPORT

DG OTH OTH90 AUTH REPORTS

DG OTH PATIENT INQUIRY

DG OTH POTENTIAL OTH

DG OTH REPORTS MENU

The following entry in the OPTION file (#19) needs to be restored to the previous version by the back-out patch that needs to be designed for this:

Option Name

-----------

DG REGISTRATION MENU

- Protocols

The following new entries in the PROTOCOL file (#101) can be deleted the back-out patch that needs to be designed for this:

Option Name

-----------

DG OTH ADD 90 DAYS

DG OTH MGMT MENU

DG OTH PATIENT INQUIRY

DG OTH SELECT PATIENT

DG OTH SHOW DETAILS

DG OTH SHOW PENDING

DG OTH VIEW APPROVED

DG OTH VIEW DENIED

- Security keys

The following new entries in the SECURITY KEY file (#19.1) can be deleted the back-out patch that needs to be designed for this:

Security Key Name

-----------------

DG OTH ADD PERIOD  
DG OTH MGR

- List Template

The following list template can be deleted by the back-out patch that needs to be designed for this.

NAME:

--------------------

DG OTH MANAGEMENT

- Input Template

The following template needs to be restored to the previous version by the back-out patch that needs to be designed for this.

NAME:

--------------------

DG LOAD EDIT SCREEN 7 FILE \#2

- Data

The following entry in the ELIGIBILITY CODE file (#8) can be deleted by the back-out patch that needs to be designed for this:

NAME:

--------------------

EXPANDED MH CARE NON-ENROLLEE

The following entry in the MAS ELIGIBILITY CODE file (#8.1) can be deleted by the back-out patch that needs to be designed for this:

NAME:

--------------------

EXPANDED MH CARE NON-ENROLLEE

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If restoring routines from back up emails is used, then successful back-out is confirmed by verification of BEFORE checksums listed in the patch description for these routines in NPM in FORUM.

If the special back-out patch is used, then successful back-out is confirmed by verification that the back-out patch was successfully installed.

If deletion of the new OTH ELIGIBILITY PATIENT file (#33) was performed manually, then the standard FileMan DATA DICTIONARY UTILITIES utility can be used to verify if the file was deleted successfully.

If deletion of the new field EXPANDED MH CARE TYPE (#.5501) in the PATIENT file (#2) was performed manually, then the standard FileMan DATA DICTIONARY UTILITIES utility can be used to verify if the file was updated correctly.

If deletion of the new field EXPANDED MH CARE TYPE (#50.31) in the PATIENT ENROLLMENT file (#27.11) was performed manually, then the standard FileMan DATA DICTIONARY UTILITIES utility can be used to verify if the file was updated correctly.

If deletion of the new entries in the OPTION file (#19) was performed manually, then the standard FileMan INQUIRE TO FILE ENTRIES utility can be used to verify if the entries were deleted successfully.

If deletion of the new entries in the SECURITY KEY file (#19.1) was performed manually, then the standard FileMan INQUIRE TO FILE ENTRIES utility can be used to verify if the entries were deleted successfully.

If deletion of the new entry in the ELIGIBILITY CODE file (#8) was performed manually, then the standard FileMan INQUIRE TO FILE ENTRIES utility can be used to verify if the entry was deleted successfully.

If deletion of the new entry in the MAS ELIGIBILITY CODE file (#8.1) was performed manually, then the standard FileMan INQUIRE TO FILE ENTRIES utility can be used to verify if the entry was deleted successfully.

If deletion of the new entry in the LIST TEMPLATE file (#409.61) was performed manually, then the standard FileMan INQUIRE TO FILE ENTRIES utility can be used to verify if the entry was deleted successfully.

If deletion of the new entries in the PROTOCOL file (#101) was performed manually, then the standard FileMan INQUIRE TO FILE ENTRIES utility can be used to verify if the entries were deleted successfully.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. This patch doesn’t change any standard data on the site. If any billing errors occurred due to the patch, then research performed by qualified DG staff will be required and corrections will need to be performed manually.

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

Not applicable

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DG*5.3*1047 DIBRG

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install the Veterans Information Systems and Technology Architecture (VistA) Registration patch DG\*5.3\*1047, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

This patch DG\*5.3\*1047:

- Introduces the new report Potential Presumptive Psychosis Patient Report \[DG POTEN PRESUMPT PSYCHOSIS\] to identify patients who have been registered in VistA using the Presumptive Psychosis (PP) 'workaround' process since 38 United States Code (USC) 1702 was passed on 3/14/2013. The report is to be used by Registration/Enrollment users to identify PP patients without PP category and select the PP category for them.
- Implements two modifications to support benefits provided by the Deborah Sampson Act for all Former Service Members (FSM) including those eligible for Other Than Honorable (OTH) benefits. Per the Deborah Sampson Act, FSMs who experienced Military Sexual Trauma (MST) are eligible for the full range of MST-related care, both mental health and other medical care.
1.  The patch adds MST information to the Former OTH Patient Reports. This will assist billing staff in proper billing of these patients after Veterans Benefits Administration (VBA) adjudication.
2.  The patch also adds a notification and a reminder about necessity to perform MST screening in the pop-up window that is displayed when the Computerized Patient Record System (CPRS) user clicks on the OTH button for OTH patients with the OTH Emergent (OTH-90) care type.

To meet the objectives of these enhancements, the solution:

- Creates new option Potential Presumptive Psychosis Patient Report \[DG POTEN PRESUMPT PSYCHOSIS\] and introduces the new routine DGPOTEN that implements this report.
- Modifies DG routines DGOTHFSM and DGOTHFS4 to add MST information to the code that supports the Former OTH Patient Eligibility Change Report \[IB OTH FSM ELIG. CHANGE REPORT\].
- Modifies DG routine DGPPDRX to display either Return to Medication or Partial in the header of the Patient's Released Prescription section of the Presumptive Psychosis Patient Detail Report \[DG PRESUMP. PSYCH. PAT. DETAIL\].
- Modifies DG routine DGOTHBTN to add notification and a reminder about necessity to perform MST screening in the pop-up window that is displayed in the CPRS.

### From: DG*5.3*1016 DIBRG

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the Department of Veterans Affairs (VA) Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point 2 (CD2).

## Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID | Team                                                                                                          | Phase / Role | Tasks                                                                                                                                                | Project Phase (See Schedule) |
|--------|-------------------------------------------------------------------------------------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | VA Office of Information & Technology (OI&T), VA OI&T Health Product Support & Project Management Office (PMO)    | Deployment       | Plan and schedule deployment (including orchestration with vendors).                                                                                     | Planning                         |
| 2      | Local Individual Veterans Administration Medical Centers (VAMC)                                                   | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                                                               | Planning                         |
| 3      | Field Testing (Initial Operating Capability – (IOC)), Health Product Support Testing & VIP Release Agent Approval | Deployment       | Test for operational readiness.                                                                                                                          | Testing                          |
| 4      | Health Product Support and Field Operations                                                                       | Deployment       | Execute deployment.                                                                                                                                      | Deployment                       |
| 5      | VAMCs                                                                                                             | Installation     | Plan and schedule installation.                                                                                                                          | Deployment                       |
| 6      | VIP Release Agent                                                                                                 | Installation     | Obtain authority to operate and that certificate authority security documentation is in place.                                                           | Deployment                       |
| 7      | N/A for this patch as we are using only the existing VistA system                                                 | Installation     | Validate through facility Point of Contact (POC) to ensure that Information Technology (IT) equipment has been accepted using asset inventory processes. | Deployment                       |
| 8      | The VA’s SHRPE team                                                                                               | Installations    | Coordinate knowledge transfer with the team responsible for user training.                                                                               | Deployment                       |
| 9      | VIP release Agent, Health Product Support & the development team                                                  | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).                                     | Deployment                       |
| 10     | SHRPE Team                                                                                                        | Post-Deployment  | Hardware, Software, and System Support.                                                                                                                  | Warranty                         |

<span id="_Ref503892992" class="anchor"></span>Table 2: Site Preparation

## Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national rollout. This section provides the schedule and milestones for the deployment.

### Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The duration of deployment and installation is 30 days. A detailed schedule will be provided during the build.

### Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the DG\*5.3\*1016 patch deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Registration patch DG\*5.3\*1016 should be installed in all VA VistA production sites.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The test sites for IOC testing are:

- Palo Alto VA Health Care System (HCS) (640)
- North Florida/South Georgia VA HCS (573)
- Omaha VAMC (636)

Upon national release, all VAMCs are expected to install this patch prior to or on the compliance date. The software will be distributed in FORUM.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No site-specific preparations are needed for this patch. The VA sites should follow the standard procedure they are using now for installation of VistA patches (Table 2).

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            | N/A                       | N/A                                         | N/A               | N/A       |

<span id="_Ref503893066" class="anchor"></span>Table 3: Facility Specific Features

## ## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre-Installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*1016, a patch to the existing VistA Registration 5.3 package, is installable on a fully patched MUMPS VistA system and operates on top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities that communicate with the underlying operating system and hardware, thereby providing Registration independence from variations in hardware and operating system.

### Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the DG\*5.3\*1016 Patch Description on the NPM in FORUM for the detailed installation instructions. These instructions would include any pre-installation steps, if applicable.

### Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the DG\*5.3\*1016 documentation on the NPM to find related documentation that can be downloaded. DG\*5.3\*1016 will be transmitted via a PackMan message and can be pulled from the NPM. It is not a host file, and therefore does not need to be downloaded separately.

### Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch is applied to an existing MUMPS VistA database.

### Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the DG\*5.3\*1016 Patch Description in the NPM for installation instructions.

### Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for the DG\*5.3\*1016 installation.

### Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the National VA Network, as well as the local network of each site to receive DG patches, is required to perform the installation, as well as authority to install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx).

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the DG\*5.3\*1016 Patch Description in the NPM in FORUM for detailed installation instructions.

### Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, the user verifies installation results by using the “Install File Print” menu option in the “Utilities” submenu of the KIDS.

Also refer to the DG\*5.3\*1016 documentation on the NPM for detailed installation instructions. These instructions include any post-installation steps, if applicable.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required for this patch.

### Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocations, or other resources is necessary.

## ## Appendix A: Acronyms List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Meaning                                                     |
|-------------|-----------------------------------------------------------------|
| ADT         | Admission, Discharge, and Transfer                              |
| CD \#2      | Critical Decision Point \#2                                     |
| ESD         | Enterprise Service Desk                                         |
| DD          | Data Dictionary                                                 |
| DGEN        | dBASE IV Command (to generate messages)                         |
| DIBRG       | Deployment, Installation, Back-Out, and Rollback Guide          |
| HCS         | Health Care System                                              |
| IOC         | Initial Operating Capability                                    |
| IT          | Information Technology                                          |
| KIDS        | Kernel Installation and Distribution System                     |
| MH          | Mental Health                                                   |
| MST         | Military Sexual Trauma                                          |
| MUMPS       | Massachusetts General Hospital Utility Multi-Programming System |
| N/A         | Not Applicable                                                  |
| NPM         | National Patch Module                                           |
| OI&T        | Office of Information & Technology                              |
| OTH         | Other Than Honorable                                            |
| OTH-EXT     | OTH-Extended                                                    |
| PMO         | Project Management Office                                       |
| POC         | Point of Contact                                                |
| SHRPE       | Suicide High Risk Patient Enhancements                          |
| SQA         | Software Quality Assurance                                      |
| UAT         | User Acceptance Testing                                         |
| VA          | Department of Veterans Affairs                                  |
| VAMC        | Veterans Administration Medical Centers                         |
| VIP         | Veteran-focused Integrated Process                              |
| VistA       | Veterans Health Information Systems and Technology Architecture |

### From: DG*5.3*1029 DIBRG

### After National Release but During Designated Support Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to back out a specific release needs to be made in a timely manner. Catastrophic failures are usually known early in the testing process—within the first two or three days. Sites are encouraged to perform all test scripts to ensure new code is functioning in their environment, with their data. A back-out should only be considered for critical issues or errors. The normal or an expedited, issue-focused patch process can correct other bugs.

The general strategy for SHRPE VistA functionality rollback will likely be to repair the code with another follow-on patch.

If any issues with SHRPE VistA software are discovered after it is nationally released and within the 90-day warranty period window, the SHRPE development team will research the issue and provide guidance for any immediate, possible workaround. After discussing the defect with VA and receiving their approval for the proposed resolution, the SHRPE development team will communicate guidance for the long-term solution.

The long-term solution will likely be the installation of a follow-up patch to correct the defect, a follow-up patch to remove the SHRPE updates, or a detailed set of instructions on how the software can be safely backed out of the production system.

### From: DG*5.3*916 DIBRG

## Documentation and Distribution 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this patch is available.

<span class="mark">Redacted</span>

Documentation can also be found on the VA Software Documentation Library at: http://www.va.gov/vdl/

Title File Name FTP Mode

--------------------------------------------------------------------------------------------------

Release Notes/Installation Guide dg_5_3_p916_rn.pdf Binary

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

===========================================================================

Run Date: AUG 18, 2016 Designation: DG\*5.3\*916

Package : REGISTRATION Priority : MANDATORY

Version : 5.3 Status : COMPLETE/NOT RELEASED

===========================================================================

Associated patches: (u)IB\*2\*549 \<\<= must be installed BEFORE \`DG\*5.3\*916'

Subject: EINSURANCE-COMPLIANCE PHASE 3 FY15

Category: DATA DICTIONARY

ENHANCEMENT

Description:

==========

Below is a list of all the applications involved in this project along with their patch number:

APPLICATION/VERSION PATCH

--------------------------------------------------------------------------------

INTEGRATED BILLING (IB) V. 2.0 IB\*2.0\*549

REGISTRATION (DG) V. 5.3 DG\*5.3\*916

The patches (IB\*2.0\*549 and DG\*5.3\*916) are being released in the Kernel Installation and Distribution System (KIDS) multi-build distribution as IB_DG_BUNDLE_1_0.KID.

A new style MUMPS cross reference was added to the DATE OF DEATH field (#2,.351) which is invoked when the DATE OF DEATH is populated and has not previously been manually entered. This code terms all of the patient's active insurance policies (without an expiration date, regardless of whether or not an effective date exists). The term date is to be set to the date of death+1. This is associated with ICR \#6231.

Patch Components:

-----------------------

Files & Fields Associated:

File Name (Number) Field Name (Number) New/Modified/Deleted

------------------------- --------------------------- ----------------------------

PATIENT (#2) Date of Death (#.351) Modified

Forms Associated:

Form Name File \# New/Modified/Deleted

-------------- -------- ----------------------------

N/A

Mail Groups Associated:

Mail Group Name New/Modified/Deleted

---------------------- ----------------------------

N/A

Options Associated:

Option Name Type New/Modified/Deleted

------------------ ------ ----------------------------

N/A

Protocols Associated:

Protocol Name New/Modified/Deleted

------------------ ----------------------------

N/A

Security Keys Associated:

Security Key Name

------------------------

N/A

Templates Associated:

Template Name Type File Name (Number) New/Modified/Deleted

------------------- ------- ------------------------- ----------------------------

N/A

Additional Information:

-----------------------------

N/A

New Service Requests (NSRs):

--------------------------------------

NSR 20140413 - Medical Care Collection Fund (MCCF) eInsurance Compliance Phase 3

Patient Safety Issues (PSIs):

----------------------------------

N/A

Defect Tracking System Ticket(s) & Overview:

--------------------------------------

N/A

Problem:

-----------

N/A

Resolution:

--------------

N/A

Test Sites:

-------------

Bay Pines, FL

Central Plains HCS

Chillicothe, OH

Louisville, KY

DOCUMENTATION RETRIEVAL INSTRUCTIONS

------------------------------------------------------------------

Updated documentation describing the new functionality introduced by this patch is available.

<span class="mark">Redacted</span>

Documentation can also be found on the VA Software Documentation Library at: http://www.va.gov/vdl/

Title File Name FTP Mode

--------------------------------------------------------------------------------------------------

Release Notes/Installation Guide dg_5_3_p916_rn.pdf Binary

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The components sent with this patch DG\*5.3\*916 have been included in the host file IB_DG_BUNDLE_1_0.KID. Please follow the installation instructions listed in the patch description for patch IB\*2.0\*549.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The components sent with this patch DG\*5.3\*916 have been included in the HOST File IB_DG_BUNDLE_1_0.KID. Please follow the installation instructions listed in the patch description for patch IB\*2.0\*549.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Note that there are very important pre and post install \*

\* instructions that need to be followed when installing the host file. \*

\* Follow the installation instructions for patch IB\*2.0\*549. \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The host file IB_DG_BUNDLE_1_0.KID, contains the following patches:

IB\*2.0\*549

DG\*5.3\*916

Routine Information:

===============

No routines included.

## Overview of Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a “one size fits all” solution. The general strategy for a VistA rollback is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch. If not, the site should contact the product support team directly for specific solutions to their unique problems.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA installation procedure of the KIDS build, the installer can back up the modified routines using the ‘Backup a Transport Global’ action. The installer can restore the routines using the MailMan message that was saved prior to the installation of the patch. The backout procedure for global, data dictionary and other VistA components is more complex and will require issuance of a follow-up patch to ensure all components are properly removed. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with the restoration of the data. This backout process may need to include a database cleanup process.

Please contact the product support team for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to backout the patch. If the installed patch that needs to be backed out includes a pre or post install routine, please contact the product support team before attempting the backout.

From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following option:

- Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.

> **NOTE:** When prompted for the INSTALL enter the patch \#.

## Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Date of Death Modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new style MUMPS cross reference was added to the DATE OF DEATH field (#2,.351) which is invoked when the DATE OF DEATH is populated and has not previously been entered. This code terms all of the patient's active insurance policies (without an expiration date). The term date is to be set to the date of death +1. This is associated with ICR \#6231.

## Issue Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch addresses the following New Service Request (NSR):

NSR 20140413 - Medical Care Collection Fund (MCCF) eInsurance Compliance Phase 3

### Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Remedy tickets associated with this patch.
