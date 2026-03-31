---
consolidated_title: "mental health suicide prevention deployment, installation, back-out, and rollback guide"
app_code: YS
doc_type: DIBR
master_source: "YS*5.01*136 Mental Health Suicide Prevention Deployment, Installation, Back-Out, and Rollback Guide"
master_pub_date: November 2018
consolidated_from: 4 versions
prior_versions:
  - "YS*5.01*137 Mental Health Suicide Prevention Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*139 Mental Health Suicide Prevention Deployment, Installation, Back-Out, and Rollback Guide"
  - "YS*5.01*147 Mental Health Suicide Prevention Deployment, Installation, Back-Out, and Rollback Guide"
---

# Department of Veterans Affairs Mental Health – Suicide Prevention


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Department of Veterans Affairs Mental Health – Suicide Prevention](#department-of-veterans-affairs-mental-health-suicide-prevention)
    - [Suicide Prevention Package](#suicide-prevention-package)
    - [Version 1.3](#version-13)
    - [Submitted as CLIN 0001AX](#submitted-as-clin-0001ax)
- [Artifact Rationale](#artifact-rationale)
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
  - [Appendix A - Acronyms](#appendix-a-acronyms)

### Suicide Prevention Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ys-5-01-136-mental-health-suicide-prevention-deployment-installation-back-out-an/001.png)
> November 2018

### Version 1.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Deployment, Installation, Back-Out, and Rollback Guide for YS\*5.01\*136

### Submitted as CLIN 0001AX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Contract VA118-16-D-1007, Task Order VA11817F10070006
> *.*
> Revision History
| Date      | Version | Description       | Author          |
|---------------|-------------|-----------------------|---------------------|
| November 2018 | 1.3         | YS\*5.01\*136 updates | Booz Allen Hamilton |
| August 2018   | 1.2         | YS\*5.01\*134 updates | Booz Allen Hamilton |
| July 2018     | 1.1         | YS\*5.01\*134 updates | Booz Allen Hamilton |
| March 2018    | 1.0         | Initial Version       | Booz Allen Hamilton |

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the Deployment, Installation, Back-out, and Rollback Guide (DIBO&RG) for new products going into the Veterans Affairs (VA) Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the DIBO&RG is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

1.  [Introduction 5](#introduction)
    1.  [Purpose 5](#purpose)
    2.  [Dependencies 5](#dependencies)
    3.  [Constraints 5](#constraints)
2.  [Roles and Responsibilities 5](#roles-and-responsibilities)
3.  [Deployment 6](#deployment)
    1.  [Timeline 6](#timeline)
    2.  [Site Readiness Assessment 6](#site-readiness-assessment)
        1.  [Deployment Topology (Targeted Architecture) 6](#deployment-topology-targeted-architecture)
        2.  [Site Information (Locations, Deployment Recipients) 6](#site-information-locations-deployment-recipients)
        3.  [Site Preparation 6](#site-preparation)
    3.  [Resources 7](#resources)
        1.  [Facility Specifics (optional) 7](#facility-specifics-optional)
        2.  [Hardware 7](#hardware)
        3.  [Software 7](#software)
        4.  [Communications 7](#communications)
4.  [Installation 7](#installation)
    1.  [Pre-installation and System Requirements 7](#pre-installation-and-system-requirements)
    2.  [Platform Installation and Preparation 7](#platform-installation-and-preparation)
    3.  [Access Requirements and Skills Needed for the Installation 8](#access-requirements-and-skills-needed-for-the-installation)
    4.  [Installation Procedure 8](#installation-procedure)
    5.  [Installation Verification Procedure 9](#installation-verification-procedure)
    6.  [System Configuration 10](#system-configuration)
    7.  [Database Tuning 10](#database-tuning)
5.  [Back-Out Procedure 10](#back-out-procedure)
    1.  [Back-Out Strategy 10](#back-out-strategy)
    2.  [Back-Out Considerations 10](#back-out-considerations)
    3.  [Back-Out Criteria 10](#back-out-criteria)
    4.  [Back-Out Risks 10](#back-out-risks)
    5.  [Authority for Back-Out 10](#authority-for-back-out)
    6.  [Back-Out Procedure 11](#back-out-procedure-1)
    7.  [Back-out Verification Procedure 11](#back-out-verification-procedure)
6.  [Rollback Procedure 12](#rollback-procedure)
    1.  [Rollback Considerations 12](#rollback-considerations)
    2.  [Rollback Criteria 12](#rollback-criteria)
    3.  [Rollback Risks 12](#rollback-risks)
    4.  [Authority for Rollback 12](#authority-for-rollback)
    5.  [Rollback Procedure 12](#rollback-procedure-1)
    6.  [Rollback Verification Procedure 12](#rollback-verification-procedure)

[Appendix A - Acronyms 13](#appendix-a---acronyms)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install the patch YS\*5.01\*136 of the Mental Health package, as well as how to back-out the product and rollback to a previous version or data set.

This document is a companion to the project charter and management plan for this effort in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom Mental Health patch YS\*5.01\*136 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is assumed that this patch is being installed into a fully patched Veterans Health Information System and Technology Architecture (VistA) system. In particular, patch YS\*5.01\*121 must be installed prior to the installation of this patch.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints beyond the installation into an up-to-date VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes the roles and responsibilities associated with the testing and release of YS\*5.01\*136. This is a VistA patch that will be deployed via the normal Mailman route.

> Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| Team                                     | Phase / Role | Tasks                                                                                  | Project Phase (See Schedule) |
|----------------------------------------------|------------------|--------------------------------------------------------------------------------------------|----------------------------------|
| Project Manager                              | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment. | Design                           |
| Software Quality Assurance (SQA), Test Sites | Deployment       | Test for operational readiness                                                             | Test                             |
| Project Manager, Release Manager             | Deployment       | Execute deployment                                                                         | Release                          |
| Individual VistA Sites                       | Installation     | Plan and schedule installation                                                             | Release                          |

| Team         | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Release Manager  | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Release                          |
| Sustainment Team | Post Deployment  | Hardware, Software and System Support                                                                               | Sustain                          |

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a simultaneous (National Release) rollout. Once approval has been given to nationally release, YS\*5.01\*136 will be available for installation and deployment at all sites.

Scheduling of test installs, testing and production deployment will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run from June through December 2018 as depicted in the Master Deployment Schedule in the Suicide Prevention Program (SPP) Project Management Plan.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the YS\*5.01\*136 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Update (YS\*5.01\*136) will be deployed to each VistA instance. This includes local sites as well as regional data centers. The executable and associated files will also be deployed to client workstations.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capability (IOC) sites for verification of functionality. Once testing is completed and approval is given for national release, MHA Update (YS\*5.01\*136) will be deployed to all VistA systems.

The Production IOC testing sites are:

- Milwaukee Veterans Affairs Medical Center (VAMC)
- Orlando VAMC

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Other than a fully patched VistA system, there is no other preparation required.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When MHA Update (YS\*5.01\*136) is released, the released-patch notification will be sent from the National Patch Module to all personnel who have subscribed to notifications for the Mental Health package.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health patch YS\*5.01\*121 must be installed prior to the installation of YS\*5.01\*136. The environment check for YS\*5.01\*136 will verify this.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See previous section for required Mental Health patches.

This patch installs new instruments that will consume about 2MB of disk space in the ^XTMP global during installation. The growth of the ^YTT global will be about 1MB.

This patch can be loaded with users in the system but it is recommended that it be installed when user activity is low. Installation time will be less than 5 minutes.

It is recommended that you use the “Backup a Transport Global” option that is referenced in the installation instructions. This will be useful should it be decided to back out the installation.

To ensure the integrity of the transport global, use the “Verify Checksums in Transport Global” to compare the checksums with the list that follows:

> The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

> Routine Name: YS136PST Before: n/a After: B1118766 \*\*136\*\* Routine Name: YTQAPI2B Before: B119361091 After: B119361091 \*\*136\*\* Routine Name: YTQAPI2C Before: n/a After: B68236793 \*\*136\*\*

> Routine list of preceding patches: 134

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of MHA Update (YS\*5.01\*136) requires the following:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual workstation installs – access/ability to push executable and supporting files to required work stations.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Start up the Kernel Installation and Distribution System Menu \[XPD MAIN\]:

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

3.  From this menu, you may elect to use the following options (When prompted for the INSTALL NAME, enter YS\*5.01\*136):
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  Use the Install Package(s) option and select the package YS\*5.01\*136
1.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", answer NO.
2.  When prompted "Want to DISABLE Scheduled Options and Menu Options and Protocols? NO//", answer NO.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that everything is installed properly, do the following:

- Launch CPRS.
- From the CPRS menu, select Tools, then Mental Health Assistant (MHA).
- ![](ys-5-01-136-mental-health-suicide-prevention-deployment-installation-back-out-an/002.png)As MHA starts you should see the splash screen with version 1.0.3.72 displayed in the lower right corner.

> When MHA prompts for user credentials, it should use the Personal Identity Verification (PIV) Personal Identification Number (PIN) prompt, rather than access/verify codes.

![](ys-5-01-136-mental-health-suicide-prevention-deployment-installation-back-out-an/003.png)

If MHA prompts for a PIV PIN as it is starting, the software has been installed properly. (If the Single Sign-On Integration (SSOi) servers are not available, you will see the usual access/verify prompt.)

After installation, notify mental health package users that the following new Suicide and Depression Screening instruments are available:

<table>
<colgroup>
<col style="width: 76%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Instrument</p>
</blockquote></th>
<th><blockquote>
<p><strong>Identifier</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Brief Psychiatric Rating Scale – Anchored</td>
<td>BPRS-A</td>
</tr>
<tr class="even">
<td>Patient Safety Secondary Screener</td>
<td>PSS3-2<sup>nd</sup></td>
</tr>
<tr class="odd">
<td>PCL-5 Weekly</td>
<td>PCL-5 Weekly</td>
</tr>
<tr class="even">
<td>Heaviness of Smoking Index</td>
<td>HSI</td>
</tr>
<tr class="odd">
<td>Warwick Edinberg Mental Well Being Scale</td>
<td>WEMWBS</td>
</tr>
<tr class="even">
<td>Mental Health Recovery Measure</td>
<td>MHRM</td>
</tr>
</tbody>
</table>

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is possible to partially back-out the installation of YS\*5.01\*136. This would involve restoring instrument specifications to their previous state and then restoring the saved routines. The back- out of changes to the data dictionary would require a patch to a patch.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please contact VistA support and the development team before attempting a back-out. The back- out procedure will still leave some changes in place. In addition, the installation of subsequent patches may be problematic if YS\*5.01\*136 is not installed.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out should only be considered if there is a patient safety issue, if MHA no longer functions, or if there is some other catastrophic failure.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risks vary depending on what is causing the failure of the system. The main risk is that the Mental Health package would be left in an unknown configured state.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA system manager determines if a back-out of YS\*5.01\*136 should be considered.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you wish to restore newly installed instruments to their previous state, you must do that <u>before</u> any other back-out steps. See the instructions for restoring the previous instrument state in the Rollback Procedure section to do this.

To back-out routines, you must have already selected the “Backup a Transport Global” option during the installation process. To restore the previous routines:

1.  Choose the PackMan message containing the backup you created during installation.
2.  Invoke the INSTALL/CHECK MESSAGE PackMan option.
3.  Select Kernel Installation & Distribution System Option: Installation
4.  Use the Install Package(s) option to install the previously saved routines.

If you need to back-out data dictionary modifications, remove protocols, options, or templates, you will need to contact the development team for a patch.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A successful back-out may be verified by running MHA and seeing a splash screen with the highlighted version number:

![](ys-5-01-136-mental-health-suicide-prevention-deployment-installation-back-out-an/004.png)

MHA should prompt for access/verify instead of PIV PIN and run successfully.

Verification of the back-out procedure would be the resolution of the problem that caused the need for the back-out.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

YS\*5.01\*136 adds new and updates existing mental health instruments. It is possible to roll back these changes within one week of the installation.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A rollback might be considered if the behavior of mental health instruments appears to be adversely affected after installation of YS\*5.01\*136. The VistA support and product development team should be contacted to determine if there is an alternative fix short of a rollback.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A rollback could adversely impact future installations of mental health instruments and cause problems with scoring existing mental health instruments.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA system manager determines if a rollback of mental health instruments distributed by YS\*5.01\*136 should be considered.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that there is a compelling reason to rollback specific instruments to their previous state.

For instruments that have been inactivated by YS\*5.01\*136 that need to be made active again:

- Using FileMan, edit the OPERATIONAL field (#10) and the LAST EDIT DATE field (#18) in the MH TESTS AND SURVEYS file (601.71). Select the instrument that requires re-activation.
- Change the value of the OPERATIONAL field from “Dropped” back to “Yes”
- Change the value of the LAST EDIT DATE field to ‘NOW’.

Should it be required to move instruments back to being scored in YS_MHA_AUX DLL, contact the Mental Health development team for a routine that can find the appropriate records and make the replacement.

Optionally, if you want to see how many records will be restored, choose “Trial Install” then select the number of the backup you wish to restore.

When you are ready to restore an instrument, choose “Install Exchange Entry” then select the number of the backup you want to restore.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the restore by checking to see that the instrument behaves as it did prior to the install.

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

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: YS*5.01*139 Mental Health Suicide Prevention Deployment, Installation, Back-Out, and Rollback Guide

### Suicide Prevention Package - YS\*5.01\*139

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ys-5-01-139-mental-health-suicide-prevention-deployment-installation-back-out-an/001.png)
> August 2019

### Contract VA118-16-D-1007, Task Order VA11817F10070006

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Document Revision History
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 18%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Document Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VDD Author / Team Role</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VA Group or Contract Company</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>August 2019</td>
<td>1.2</td>
<td>Updated 139 VDD</td>
<td>Booz Allen</td>
<td>SPP</td>
</tr>
<tr class="even">
<td>February 2019</td>
<td>1.1</td>
<td>Initial 139 VDD</td>
<td>Booz Allen Hamilton</td>
<td>SPP</td>
</tr>
</tbody>
</table>

### Deliverable (Product) Version History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 23%" />
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Release / Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Project Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VA Department</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>August 2019</td>
<td>YS*5.01*139v.33</td>
<td><blockquote>
<p>Deactivated RAID from Patch 139</p>
</blockquote></td>
<td>SPP</td>
<td><blockquote>
<p>Product Development (PD), Veterans Health Administration</p>
<p>(VHA), Product Support (PS)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>February 2019</td>
<td>YS*5.01*139v.16</td>
<td><blockquote>
<p>Includes 5 new instruments to be added to the MHA Framework plus addressing defects reported for 8 previously released instruments</p>
</blockquote></td>
<td>SPP</td>
<td><blockquote>
<p>Product Development (PD), Veterans Health Administration (VHA), Product Support (PS)</p>
</blockquote></td>
</tr>
</tbody>
</table>
> The Department of Veterans Affairs (VA) uses the Version Description Document (VDD) to identify, maintain, enhance, and recreate the product (Information Technology \[IT\] asset) throughout its lifecycle. The VDD reinforces strong risk management practices and helps protect VA from loss of the product, which is especially important with a regular rotation of personnel and contractors.
> The VDD is the authoritative inventory and roadmap of all Configuration Items (CIs) that make up the deployable product/system. CIs include source code files, builds/packaging, tools, baselines, locations, and associated product files. The VDD is itself a CI maintained under change control in the Technical Reference Model (TRM)-approved configuration management system, which is part of the VA Federated Configuration Management Data Base (CMDB).
> Project Managers (PMs) and Configuration Managers (CMs) use the VDD template as a tool for managing CIs associated with the deployable product. PMs distribute the VDD template to IT CMs (or IT Architect/Development Lead) at the beginning of the product build process (ProPath, Product Build: BLD-1 Develop Product Component). The CM creates/updates the VDD each time the deliverable (file set) leaves the development environment, such as for testing or deployment. For product procedures, refer to the Software Configuration Management Procedures Template (ProPath, Project Planning: PRP 3.7).
> The PM is responsible for ensuring the CM completes the VDD and places the VDD with the deliverables (files) in the TRM-approved configuration management system.
> 1
1.  [General Configuration Management Information 1](#general-configuration-management-information)
2.  [Configuration Management Tools 2](#configuration-management-tools)
3.  [Configuration Management of Documents 3](#configuration-management-of-documents)
    1.  [Rational Change and Configuration Management Documents 3](#rational-ccm-documents)
    2.  [Configuration Management Development Files (Ex. Source, Java Server Pages \[JSP\], Configuration, and Build Files) 3](#configuration-management-development-files-ex.-source-java-server-pages-jsp-configuration-and-build-files)
        1.  [Baseline 3](#baseline)
        2.  [Component(s) 4](#components)
    3.  [Rational CCM Repository (Formerly RTC) 4](#rational-ccm-repository)
4.  [Build Information 5](#build-information)
    1.  [CCM/RTC Build Definition 5](#ccmrtc-build-definition)
    2.  [Build Label or Number 5](#build-label-or-number)
5.  [Build and Packaging 6](#build-and-packaging)
    1.  [Build Logs 6](#build-logs)
    2.  [Build System/Process Information 6](#build-systemprocess-information)
6.  [Change Tracking 7](#change-tracking)
    1.  [Work Items 7](#work-items)
7.  [Release (Deployment) Information 8](#_bookmark16)
8.  [Known Problems 9](#known-problems)
9.  [Additional Supporting Documentation 10](#additional-supporting-documentation)
[Appendix A - Acronyms 11](#appendix-a---acronyms)

## Rational CCM Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CCM (formally Rational Team Concert (RTC)) location for the documents and CCM explanation for the information

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>CCM/RTC Information</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Explanation</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CCM Uniform Resource Locator (URL)</strong></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><strong>CCM Project Area</strong></td>
<td>MHLTH</td>
</tr>
<tr class="odd">
<td><strong>CCM Team Area</strong></td>
<td>SPP</td>
</tr>
<tr class="even">
<td><strong>CCM Stream</strong></td>
<td>MHLTH_SPP</td>
</tr>
<tr class="odd">
<td><strong>Baseline Identification (ID)</strong></td>
<td>MHLTH_YS_Source (*20: SPP P139_V33 IOC Entry)</td>
</tr>
<tr class="even">
<td><strong>Components</strong></td>
<td>MHLTH_SPP_Documentation</td>
</tr>
<tr class="odd">
<td><strong>Directory Path (Code)</strong></td>
<td>Source Control &gt; Streams &gt; MHLTH_SPP_YS*5.01*139</td>
</tr>
<tr class="even">
<td><strong>Directory Path (Code)</strong></td>
<td>Source Control &gt; Streams &gt; MHLTH_ SPP_Documentation</td>
</tr>
<tr class="odd">
<td><strong>Documents included in the RTC Baseline</strong></td>
<td><ul>
<li><p>SPP Deployment, Installation, Back-Out, and Rollback Guide</p></li>
<li><p>SPP Initial Operating Capability Release Plan</p></li>
<li><p>SPP Patch Description 139</p></li>
<li><p>SPP Software Design Document</p></li>
<li><p>SPP Sustainment Transition Acceptance Plan</p></li>
<li><p>SPP Test Environment Maintenance Guide</p></li>
<li><p>SPP Technical Manual</p></li>
<li><p>SPP User Manual</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Configuration Management Development Files (Ex. Source, Java Server Pages \[JSP\], Configuration, and Build Files)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Baseline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The baseline name, such as a label or tag

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>N/A</td>
<td><blockquote>
<p>Massachusetts General Hospital Utility Multi- Programming System (MUMPS) development and managed through Veterans Health Information System and Technology Architecture (VistA)</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Component(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Where a set of artifacts are grouped and managed.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

## Rational CCM Repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CCM location for the documents and CCM explanation for the information

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>CCM/RTC</strong></p>
<p><strong>Information</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Explanation</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CCM URL</strong></td>
<td>https://clm.rational.oit.va.gov/ccm/web</td>
</tr>
<tr class="even">
<td><strong>CCM Project Area</strong></td>
<td>MHLTH_SPP</td>
</tr>
<tr class="odd">
<td><strong>CCM Team Area</strong></td>
<td>SPP</td>
</tr>
<tr class="even">
<td><strong>CCM Stream</strong></td>
<td>MHLTH_SPP</td>
</tr>
<tr class="odd">
<td><strong>Baseline ID</strong></td>
<td>“SPP 139 IOC Entry”</td>
</tr>
</tbody>
</table>

### CCM/RTC Build Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The name of the build definition, which controls what is built and how it is built

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

### Build Label or Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The identifier for the derived object or package that was produced for deployment and/or install

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS*5.01*139_v33</td>
<td><blockquote>
<p>Build 5</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Build Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Build System/Process Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Work Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Work Item ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Summary</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>All 139 work</p>
<p>items in Rational</p></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  <span id="_bookmark16" class="anchor"></span>Release (Deployment) Information

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 22%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Release Identification</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Release Package POC Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Release Package POC Email</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VistA YS*5.01*139</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 21%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Release Package (Component) Identified</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Release Package Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Release Package Delivery Method</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Release Package Location Identified</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS*5.01*139</td>
<td>MUMPS Patch</td>
<td>FORUM</td>
<td>FORUM</td>
</tr>
</tbody>
</table>

### From: YS*5.01*147 Mental Health Suicide Prevention Deployment, Installation, Back-Out, and Rollback Guide

## Post Install for Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To get Progress Notes to show in CPRS Notes, use one of the following procedures - MHA3 Utilities or FileMan (see samples below).

> After you have changed the PNote field, TIU Title Field or the Consult Note Title Field, make sure the: LAST EDIT DATE in the MH TESTS AND SURVEYS ( \#601.71) file is updated with the current date and time.

> <u>Progress Note Field requirements for 147 instruments.</u> These instruments should have the PNote field populated with either a Yes/No, as indicated in the table below:

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 23%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Instrument</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Identifier</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Should the instrument display a</strong></p>
<p><strong>Progress Note?</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Ascertain Dementia 8-item Informant</p>
<p>Questionnaire</p></td>
<td>AD8</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Edinburgh Postnatal Depression Scale</td>
<td>EPDS</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>Fagerström Test for Nicotine</p>
<p>Dependence</p></td>
<td>FTND</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Combat Exposure Scale</td>
<td>CES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>WHYMPI Pain Interference Scale</td>
<td>MPI-PAIN-INTRF</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>Behavior and Symptom Identification</p>
<p>Scale 24 – Psychosis Symptoms</p></td>
<td>BASIS-24 PSYCHOSIS</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Indiana Job Satisfaction Scale</td>
<td>IJSS</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Instructions using the MHA3 Utilities Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “Stop/Re-Start Progress Notes for an Instrument” on the MHA3 Utilities menu (YTQ MHA3 MENU) can be used to edit the PNote Field (Progress Note), TIU Title Field, and Consult Note Title Field without having to go into FileMan.

> Based on what the PNote field should read, either Yes to show the Progress Note, or No to not show the Progress note, you would need to either “Start” or “Stop” the Progress Note field for the Instrument.

> If a progress note is Yes and should appear, but it is NOT appearing, then you should use the START PROGRESS NOTES instructions below.

> If a progress note is No and should NOT appear, but it IS appearing, then you should use the STOP PROGRESS NOTES instructions below.

> START PROGRESS NOTES:

1.  Stop/Re-Start Progress Notes for an Instrument
2.  Print Test Form
3.  Detailed Definition
4.  Delete Patient Data
6.  Test Usage
7.  Instrument Exchange

> 5 Exempt Test

> Select MHA3 Utilities \<SPPNXT\> Option: 1 Stop/Re-Start Progress Notes for an Instrument

> Select MH TESTS AND SURVEYS NAME: \[Insert instrument name here\] GENERATE PNOTE: No// Y Yes

> TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// CONSULT NOTE TITLE: MENTAL HEALTH CONSULT NOTE//

> STOP PROGRESS NOTES:

1.  Stop/Re-Start Progress Notes for an Instrument
2.  Print Test Form
3.  Detailed Definition
4.  Delete Patient Data
6.  Test Usage
7.  Instrument Exchange

> 5 Exempt Test

> Select MHA3 Utilities \<SPPNXT\> Option: 1 Stop/Re-Start Progress Notes for an Instrument

> Select MH TESTS AND SURVEYS NAME: \[Insert instrument name here\] GENERATE PNOTE: Yes// N No

> TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// CONSULT NOTE TITLE: MENTAL HEALTH CONSULT NOTE//

> UPDATING LAST EDIT DATE IN FILEMAN IF YOU USE MHA3 UTILITIES:

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> Input to what File: MH TESTS AND SURVEYS// (250 entries) EDIT WHICH FIELD: ALL// LAST

1.  LAST EDIT DATE
2.  LAST EDITED BY CHOOSE 1-2: 1 LAST EDIT DATE THEN EDIT FIELD:

> Select MH TESTS AND SURVEYS NAME: \[Insert instrument name here\] LAST EDIT DATE: FEB 5,2019@19:31// Now (MAR 04, 2019@06:10)

### FileMan Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user needs to access FileMan and choose option ‘ENTER OR EDIT FILE ENTRIES’.
2.  In ‘Input to what File’ enter MH TESTS AND SURVEYS
3.  For EDIT WHICH FIELD: – GENERATE PNOTE
4.  For THEN EDIT FIELD: TIU TITLE
5.  For THEN EDIT FIELD: CONSULT NOTE TITLE
6.  Last Edit Date: (Enter Current Date)

> Press return and at the prompt: Select MH TESTS AND SURVEYS NAME: enter name of instrument

> For field ‘GENERATE PNOTE:’ enter “YES” or “NO”, depending on the instructions provided for each instrument in this Install Guide. For FIELD ‘TIU TITLE:’ enter the TIU Title as defined by your site

> For FIELD ‘CONSULT NOTE TITLE:’ enter the title of the CONSULT NOTE as defined by your site

> For LAST EDIT DATE: enter current date

> Exit FileMan and your notes should now save to CPRS Notes.

> Example for Instrument: ‘CES’

> Select OPTION: ?

> Answer with OPTION NUMBER, or NAME Choose from:

1.  ENTER OR EDIT FILE ENTRIES
2.  PRINT FILE ENTRIES
3.  SEARCH FILE ENTRIES
4.  MODIFY FILE ATTRIBUTES
5.  INQUIRE TO FILE ENTRIES
6.  UTILITY FUNCTIONS
7.  OTHER OPTIONS
8.  DATA DICTIONARY UTILITIES
9.  TRANSFER ENTRIES

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

> Input to what File: MH TESTS AND SURVEYS// (250 entries) EDIT WHICH FIELD: ALL// GENERATE PNOTE

> THEN EDIT FIELD: TIU TITLE

> THEN EDIT FIELD: CONSULT NOTE TITLE THEN EDIT FIELD: LAST EDIT DATE

> Select MH TESTS AND SURVEYS NAME: CES GENERATE PNOTE: Yes// Yes

> TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE//

> CONSULT NOTE TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// LAST EDIT DATE: FEB 5,2019@19:31// Now (MAR 04, 2019@06:10)

### From: YS*5.01*137 Mental Health Suicide Prevention Deployment, Installation, Back-Out, and Rollback Guide

### Instructions using the MHA3 Utilities Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “Stop/Re-Start Progress Notes for an Instrument” on the MHA3 Utilities menu (YTQ MHA3 MENU) can be used to edit the PNote Field (Progress Note), TIU Title Field, and Consult Note Title Field without having to go into FileMan.

> Based on what the PNote field should read, either Yes to show the Progress Note, or No to not show the Progress note, you would need to either “Start” or “Stop” the Progress Note field for the Instrument.

> If a progress note is Yes and should appear, but it is NOT appearing, then you should use the START PROGRESS NOTES instructions below.

> If a progress note is No and should NOT appear, but it IS appearing, then you should use the STOP PROGRESS NOTES instructions below.

> START PROGRESS NOTES:

1.  Stop/Re-Start Progress Notes for an Instrument
2.  Print Test Form
3.  Detailed Definition
4.  Delete Patient Data
6.  Test Usage
7.  Instrument Exchange

> 5 Exempt Test

> Select MHA3 Utilities \<SPPNXT\> Option: 1 Stop/Re-Start Progress Notes for an Instrument

> Select MH TESTS AND SURVEYS NAME: \[Insert instrument name here\] GENERATE PNOTE: No// Y Yes

> TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// CONSULT NOTE TITLE: MENTAL HEALTH CONSULT NOTE//

> STOP PROGRESS NOTES:

1.  Stop/Re-Start Progress Notes for an Instrument
2.  Print Test Form
3.  Detailed Definition
4.  Delete Patient Data
6.  Test Usage
7.  Instrument Exchange

> 5 Exempt Test

> Select MHA3 Utilities \<SPPNXT\> Option: 1 Stop/Re-Start Progress Notes for an Instrument

> Select MH TESTS AND SURVEYS NAME: \[Insert instrument name here\] GENERATE PNOTE: Yes// N No

> TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// CONSULT NOTE TITLE: MENTAL HEALTH CONSULT NOTE//

> UPDATING LAST EDIT DATE IN FILEMAN IF YOU USE MHA3 UTILITIES:

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> Input to what File: MH TESTS AND SURVEYS// (250 entries) EDIT WHICH FIELD: ALL// LAST

1.  LAST EDIT DATE
2.  LAST EDITED BY CHOOSE 1-2: 1 LAST EDIT DATE THEN EDIT FIELD:

> Select MH TESTS AND SURVEYS NAME: \[Insert instrument name here\] LAST EDIT DATE: FEB 5,2019@19:31// Now (MAR 04, 2019@06:10)

### FileMan Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user needs to access FileMan and choose option ‘ENTER OR EDIT FILE ENTRIES’.
2.  In ‘Input to what File’ enter MH TESTS AND SURVEYS
3.  For EDIT WHICH FIELD: – GENERATE PNOTE
4.  For THEN EDIT FIELD: TIU TITLE
5.  For THEN EDIT FIELD: CONSULT NOTE TITLE
6.  Last Edit Date: (Enter Current Date)

> Press return and at the prompt: Select MH TESTS AND SURVEYS NAME: enter name of instrument

> For field ‘GENERATE PNOTE:’ enter “YES” or “NO”, depending on the instructions provided for each instrument in this Install Guide. For FIELD ‘TIU TITLE:’ enter the TIU Title as defined by your site

> For FIELD ‘CONSULT NOTE TITLE:’ enter the title of the CONSULT NOTE as defined by your site

> For LAST EDIT DATE: enter current date

> Exit FileMan and your notes should now save to CPRS Notes.

> Example for Instrument: ‘CES’

> Select OPTION: ?

> Answer with OPTION NUMBER, or NAME Choose from:

1.  ENTER OR EDIT FILE ENTRIES
2.  PRINT FILE ENTRIES
3.  SEARCH FILE ENTRIES
4.  MODIFY FILE ATTRIBUTES
5.  INQUIRE TO FILE ENTRIES
6.  UTILITY FUNCTIONS
7.  OTHER OPTIONS
8.  DATA DICTIONARY UTILITIES
9.  TRANSFER ENTRIES

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

> Input to what File: MH TESTS AND SURVEYS// (250 entries) EDIT WHICH FIELD: ALL// GENERATE PNOTE

> THEN EDIT FIELD: TIU TITLE

> THEN EDIT FIELD: CONSULT NOTE TITLE THEN EDIT FIELD: LAST EDIT DATE

> Select MH TESTS AND SURVEYS NAME: CES GENERATE PNOTE: Yes// Yes

> TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE//

> CONSULT NOTE TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// LAST EDIT DATE: FEB 5,2019@19:31// Now (MAR 04, 2019@06:10)
