---
consolidated_title: "blind rehab deployment, installation, back-out, rollback guide"
app_code: ANRV
doc_type: DIBR
master_source: "Blind Rehab Version 5.1.3 Deployment, Installation, Back-out, Rollback Guide"
master_pub_date: February 2023
consolidated_from: 3 versions
prior_versions:
  - "Blind Rehab Version 5.1.11 Deployment, Installation, Back-Out, Rollback Guide"
  - "Blind Rehab Version 5.1.12 Deployment, Installation, Back-Out, Rollback Guide"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Blind Rehabilitation (ANRV)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](blind-rehab-version-5-1-3-deployment-installation-back-out-rollback-guide/001.png)

February 2023

ANRV\*5.1\*6

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

When updates occur, the Title Page lists the new revised date, and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

| Date | Version | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Author          |
|----------|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| 02/2023  | 5.1.6       | Correct dates and typos, modified team from Liberty to Booz Allen, changed deployment instructions in section 3, updated timeline in section 3.1, updated site information in section 3.2.2, updated sections 4.4 and 4.5. Modified 4.8 with and extra prompt, 4.9 with correct names, 4.10 with an additional note, updated section 5 back-out procedure by deleting confusing verbiage and adding in clearer instructions, updated section 5.1 back-out strategy with clearer instructions. Updated Section 6.5 and 6.6 with clearer instructions and URL | Booz Allen Hamilton |
| 12/2022  | 5.1.3       | Patch 2 “Entered in Error”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Booz Allen Hamilton |
| 10/2022  | 5.1.2       | Patch 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Booz Allen Hamilton |
| 8/2022   | 5.1         | Initial Release                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Booz Allen Hamilton |

<span id="_Toc126327615" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

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
    - [Adaptive Technology Software for Individual Work Station](#adaptive-technology-software-for-individual-work-station)
    - [Communications](#communications)
- [Patch Installation](#patch-installation)
  - [Pre-Installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation on the AWS Platform](#access-requirements-and-skills-needed-for-the-installation-on-the-aws-platform)
  - [Installation Procedure](#installation-procedure)
    - [Ear File Deployment](#ear-file-deployment)
    - [KIDS Installation](#kids-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
    - [KIDS Verification](#kids-verification)
  - [System Configuration](#system-configuration)
  - [System Configuration](#system-configuration-1)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
    - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
    - [Ear File Backout](#ear-file-backout)
    - [KIDS Back-Out](#kids-back-out)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
    - [Ear File Back-out Verification](#ear-file-back-out-verification)
    - [KIDS Back-out Verification](#kids-back-out-verification)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the Blind Rehabilitation patch ANRV\*5.1\*6 web application*,* as well as how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Blind Rehabilitation web application will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Blind Rehabilitation web application requires that Identify and Access Management (IAM), Blind Single Sign-On Internal (SSOi) be provisioned for the application and that users of the application Link any of their existing VistA accounts with IAM’s Link My Account.

ANRV\*5.1\*6 project is for installation on a fully patched Veterans Health Information Systems and Technology Architecture (VistA) system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment, installation, back-out, and rollback roles and responsibilities are shown in Table 1.

| Team                                                                                                                                                                                            | Phase / Role | Tasks                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|
| Booz Allen Hamilton, National Blind Rehabilitation Server, VistA Applications and Office Information & Technology (OIT), Development, Security, and Operations (DevSecOps) and Product Support Team | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                 |
| Booz Allen Hamilton, National Blind Rehabilitation Server, VistA Applications and Office Information & Technology (OIT), Development, Security, and Operations (DevSecOps) and Product Support Team | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          |
| Booz Allen Hamilton, National Blind Rehabilitation Server, VistA Applications and Office Information & Technology (OIT), Development, Security, and Operations (DevSecOps) and Product Support Team | Deployment       | Test for operational readiness                                                                                      |
| VistA Applications and Office Information &Technology (OIT), Development, Security, and Operations (DevSecOps)                                                                                      | Deployment       | Execute deployment                                                                                                  |
| VistA Applications and Office Information &Technology (OIT), Development, Security, and Operations (DevSecOps) and Product Support Team                                                             | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |
| VistA Applications and Office Information &Technology (OIT), Development, Security, and Operations (DevSecOps) and Product Support Team                                                             | Post Deployment  | Hardware, Software and System Support                                                                               |

<span id="_Toc126327616" class="anchor"></span>Table 2: Software Specifications

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Server promotion deployment of BRS 5.1.6 by Infrastructure Operations (IO) after ANRV\*5.1\*6 national release approval.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ANRV\*5.1\*6 will occur, at the same time for all sites, as a result of the deployment upon approval for national release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the ANRV\*5.1\*6 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The nationally deployed BRS will be updated to BRS 5.1.6.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IOC sites are:

- West Palm Beach, FL VAMC
- Augusta, GA VAMC

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ANRV\*5.1\*6 patch will require a fully patched VistA system.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software        |
|------------------------------|
| A fully patched VistA system |

<span id="_Toc109300287" class="anchor"></span>Table : Associated Patch Files

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Adaptive Technology Software for Individual Work Station

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehabilitation users are responsible for ensuring their adaptive technology software is fully updated (JAWS/ZoomText/etc.). Please contact local desktop support for assistance if needed.

Your adherence to the VA Technical Reference Model (TRM) is essential to improving the technical environment within VA. Architecture & Engineering Services (AES), specifically EA, has overall responsibility for the VA TRM and needs your support and cooperation to make it a success.

You may access: REDACTED to view approved versions.

JAWS 2020 Software enhancements version releases:

- Enhancements in JAWS 2020.2001.70 (February 2020)
- Enhancements in JAWS 2020.2003.13 (March 2020)
- Enhancements in JAWS 2020.2004.66 (April 2020)
- Enhancements in JAWS 2020.2006.12 (June 2020)
- Enhancements in JAWS 2020.2008.24 (August 2020)
- Enhancements in JAWS 2020.2012.9 (December 2020)
- Enhancements in JAWS 2020.2110.3 (November 2021)

The latest patch for JAWS 2020 is: JAWS 2020.2110.3 Offline 64-bit November 2021.

It is recommended that BR staff be updated to JAWS 2023.

ZoomText: Recommended version – 2023.x (October 2022).

For more info on these releases, please go here: REDACTED and select in the drop-down JAWS 2020.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ANRV\*5.1\*6 will be deployed using the standard method of patch release from the National Patch Module. When ANRV\*5.1\*6 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

# Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OIT BR Sustainment team to deliver the new ear files to the IO team.

- REDACTED

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the ANRV\*5.1\*6 patch description in FORUM to find related documentation that can be downloaded.

The following documents and files can be obtained from the SOFTWARE library:

REDACTED

<table>
<caption><p><span id="_Toc109300288" class="anchor"></span>Table : Routines</p></caption>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>File</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>ANRV_5_1_6_RN.docx</p>
<p>ANRV_5_1_6_RN.pdf</p></td>
<td>Blind Rehabilitation (BR) Release 5.1.6 Release Notes</td>
</tr>
<tr class="even">
<td><p>ANRV_5_1_6_UM.docx</p>
<p>ANRV_5_1_6_UM.pdf</p></td>
<td>BR User Manual</td>
</tr>
<tr class="odd">
<td><p>ANRV_5_1_6_DIBRG.docx</p>
<p>ANRV_5_1_6_DIBRG.pdf</p></td>
<td>BR Deployment, Installation, Back-out, and Rollback Guide</td>
</tr>
<tr class="even">
<td><p>ANRV_5_1_6_CIG.docx</p>
<p>ANRV_5_1_6_CIG.pdf</p></td>
<td>BR Centralized Server Installation/Implementation Guide</td>
</tr>
</tbody>
</table>

<span id="_Toc109300288" class="anchor"></span>Table : Routines

Redacted versions are also available on the VA Software Document Library (VDL):

REDACTED

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are needed for ANRV\*5.1\*6 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6

## Access Requirements and Skills Needed for the Installation on the AWS Platform

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BRS 5.1.6 deployment requires an IO web administrator.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Ear File Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  IO team backups the previous ear files.
    1.  REDACTED
2.  IO team removes the previous ear files.
3.  IO team deploys the new ear files.
    1.  REDACTED

### KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The bottom right corner of the application login page from the BRS URL should begin with REDACTED.

### KIDS Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

| Routine | Before Checksum | After Checksum | Patch List |
|---------|-----------------|----------------|------------|
| N/A     |                 |                |            |

RoutinesThis table shows the list of routines and their before checksums, after checksums, and patch list associations.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to back-out or rollback software will be a joint decision between development team, VA site/region personnel and other appropriate VA personnel.

To request assistance with a back-out, please log a ServiceNow ticket, and state that you're requesting assistance with backing out a patch.

<u>AWS Deployment Backout:</u>

Since the application is deployed as a Java enterprise archive (EAR), the application will be placed in the REDACTED directory. The version of the application is included in the EAR file. The WebLogic administrator may have unlimited previous versions of the EAR file in the REDACTED directory. However, to conserve space, the Booz Allen team suggests that one previous version be stored. Older versions can be created using GitHub and a build process. Follow the same installation procedure of the WebLogic admin, use the last known good operational state of the EAR software and appropriate platform settings, and undeploy the version of the application that are causing issues.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backout of this patch will be performed only with the concurrence and participation of the appropriate VA site/region personnel. The decision to back out the patch will be a joint decision between VA site/region personnel and other appropriate VA personnel.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The load testing is being done during the live testing phase at the test sites.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) can be provided upon request and outcome of UAT is managed and completed by Booz Allen Hamilton . For User Acceptance Testing details, please contact:

• REDACTED

• REDACTED

### Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AWS-The product can be backed out if significant issues are experienced during deployment of the EAR or if issues arise during use of the application (regression testing) once made available in the appropriate environment.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out the ANRV\*5.1\*6 patch, corrective actions included with the patch will be removed and an earlier version will be restored.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Business owner, OIT DevSecOps and Liberty have the authority to request a backout be performed.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Ear File Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  IO team removes the new ear files.
    1.  REDACTED
2.  IO team deploys the previous ear files.
    1.  REDACTED

### KIDS Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

Backout of this patch will be performed only with the concurrence and participation of the appropriate VA site/region personnel. The decision to back out the patch will be a joint decision between VA site/region personnel and other appropriate VA personnel.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Ear File Back-out Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The bottom right corner of the application login page from the BR URL should begin with Build: REDACTED.

### KIDS Back-out Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for ANRV\*5.1\*6.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Blind Rehab Version 5.1.11 Deployment, Installation, Back-Out, Rollback Guide

## VistA Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff performing the installation of ANRV\*5.1\*11 patch will need access to FORUM.

This patch is “Informational.”

### From: Blind Rehab Version 5.1.12 Deployment, Installation, Back-Out, Rollback Guide

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document has been prepared for system administrators and database administrators who need to update pre-production and/or production environments in the VA Enterprises Cloud (VAEC). It is presumed that readers of this document understand basic concepts of the VAEC BR v5.1 environments as well as any system specialties that might pertain to the installation of the BR v5.1 software.

## Scope/Deliverables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The scope of this plan encompasses the Blind Rehabilitation Services, and their related responsibilities. The plan specifies the steps and software necessary to install and configure BR v5.1 on a Linux server environment.
