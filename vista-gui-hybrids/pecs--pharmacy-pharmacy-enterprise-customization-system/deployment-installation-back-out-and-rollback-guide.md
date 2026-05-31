---
title: PREC*6.2*4 PECS Deployment, Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: PECS
app_name: 'Pharmacy: Pharmacy Enterprise Customization System'
section: GUI
app_status: active
pkg_ns: PREC
patch_ver: 6.2
patch_id: PREC*6.2*4
group_key: PECS:PREC:6.2
file_numbers: []
security_keys: []
menu_options: 0
description: '''Table 1: Deployment, Installation, Back-out, and Rollback Roles and'''
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 2024
section_count: 31
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: January 2024
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/prec_6_2_4_dibr.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/prec_6_2_4_dibr.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=204
audit_applied: '2026-05-31'
master_source: PREC*6.2*4 PECS Deployment, Installation, Back-out, and Rollback Guide
master_pub_date: January 2024
consolidated_from: 5 versions
prior_versions:
- PREC*6.2*1 PECS Deployment, Installation, Back-out, and Rollback Guide
- PREC*6.2*2 PECS Deployment, Installation, Back-out, and Rollback Guide
- PREC*6.2*3 PECS Deployment, Installation, Back-out, and Rollback Guide
- PREC*7*1 PECS Deployment, Installation, Back-out, and Rollback Guide
consolidated_title: pecs deployment, installation, back-out, and rollback guide
---

![](prec-6-2-4-pecs-deployment-installation-back-out-and-rollback-guide/001.png)

January 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 10%" />
<col style="width: 47%" />
<col style="width: 22%" />
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
<td>01/04/2024</td>
<td>1.2</td>
<td>Updated patch version numbers</td>
<td>BAH</td>
</tr>
<tr class="even">
<td>12/08/2023</td>
<td>1.1</td>
<td>Updated Log4j to be compliant via the Technical Reference Model per the VA Security Standards</td>
<td>BAH</td>
</tr>
<tr class="odd">
<td>08/14/2023</td>
<td>1.0</td>
<td><p>PREC*6*2*4:</p>
<ul>
<li><p>Addresses an issue that occurs when customizing an interaction in PECS.</p></li>
<li><p>Log4j2 libraries have been upgraded to version 2.20.0 to remediate security vulnerabilities and to comply with the Technical Reference Model (TRM).</p></li>
</ul></td>
<td>BAH</td>
</tr>
</tbody>
</table>

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Guide for the PECS Java portion of the PECS v6.2.4 release. This is a subdocument of the main PECS Deployment, Installation, Back-Out, and Rollback Guide. It is separate since many of the details of PECS Java application deployment involve a different set of personnel coordinating at just a few critical collaboration points with the VistA/MUMPS portion. Those collaboration points will be highlighted and cross-referenced in the main document as well as in this document.

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
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
    - [Properties Files](#properties-files)
    - [Import VA Certificates](#import-va-certificates)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
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
This document describes how to deploy and install the Pharmacy Enterprise Customization System (PECS) Java Application, including the WebLogic, Oracle, and Single Sign-On Internal (SSOi) configurations for PREC\*6.2\*4.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to describe how to deploy and install the PECS Java Application, including the WebLogic, Oracle, and SSOi configurations.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following pre-existing PECS v6.2.3 interfacing systems must be available during the deployment.

- SSOi
- Standard Terminology Services/Veterans Enterprise Terminology Services (STS/VETS)

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints for the PREC\*6.2\*4 release.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                        | Phase / Role    | Tasks                                                                                                               | Project Phase (See Schedule) |
|-----|---------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|------------------------------|
|     | Austin Information Technology Center (AITC) | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                 |                              |
|     | AITC                                        | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                          |                              |
|     | AITC                                        | Deployment      | Test for operational readiness                                                                                      |                              |
|     | AITC                                        | Deployment      | Execute deployment                                                                                                  |                              |
|     | PECS Sustainment Team                       | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |                              |
|     | Product Support                             | Post Deployment | Hardware, Software, and System Support                                                                              |                              |

Table 2: Site Preparation

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the schedule and milestones for the deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PREC\*6.2\*4 will be nationally deployed at AITC after User Acceptance Testing (UAT) and National Release approval.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS Java Application is a single, nationally deployed, web application deployed in the AITC.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS Java Application and Database will be installed on the existing PECS v6.2.3 production platform.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Section 3.3](#resources) describes the PECS Java Application and it is deployed in AITC as a national web application.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

| Site/Other | Problem/Change Needed                            | Features to Adapt/Modify to New Product | Actions/Steps                                                                                                                                        | Owner |
|------------|--------------------------------------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| AITC       | Ensure Firewall access between PECS and STS/VETS |                                         | If connectivity is not open between the PECS web application server and the STS/VETS server, request that the firewall be opened for this connection |       |

Table 3: Facility-Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pre-existing PECS v6.2.3 environment resources will be used.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      |                |                     |           |

Table 4: Hardware Specifications

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   |           |             |                   |                  |           |

Table 5: Software Specifications

Please see the Roles and Responsibilities table in [Section 2](#roles-and-responsibilities) for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software                     | Version             | Configuration |
|---------------------------------------|---------------------|---------------|
| Oracle WebLogic                       | 12.2.1.4            | New           |
| Oracle 11g Enterprise Edition Release | 19.10.0.0.0         | New           |
| Apache httpd                          | Apache/2.4.6 (Unix) | New           |
| Red Hat Enterprise Linux Server       | 7.9 (Santiago)      | New           |
| Java SDK                              | 1.8.0_371 or higher | New           |

Please see the Roles and Responsibilities table in [Section 2](#roles-and-responsibilities) above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Notify business owner of production deployment.
- The Release Manager will schedule activities and identify the required personnel for each activity.
- Meetings will be scheduled for deployment personnel to work through the deployment steps.

#### Deployment/Installation/Back-Out Checklist

Table 6: Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS Java Application and Database will be installed on the existing PECS v6.2.3 production platform.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pre-existing PECS v6.2.3 platform will be used.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See [Section 4.5](#installation-scripts), specific filenames will be detailed in the Request for Change Order (RFC).

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pre-existing PECS v6.2.3 database will be used.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All scripts and files are provided to AITC Infrastructure Operations team via Outlook/Teams. The installer should follow the instructions in the appropriate RFC.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron job changes are required for this deployment.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Linux System Administrators will need:

- Access to the Linux console of the server where PECS's WebLogic is running.
- Access to the WebLogic web-based Console.

Database Administrators will need access to the Linux console of the server where PECS's Oracle database is running.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is a high-level overview of the installation procedure steps. Detailed steps are in the RFC for database and application deployment, and they will be sent via Outlook.

Ear File Deployment

1.  Stop the Managed Server.
1.  Un-deploy the two existing EAR files for the PECS v6.2.3 application.
2.  Deploy the two new EAR files for the PECS v6.2.4 application.
3.  Start the PECS Application.
4.  Perform Smoke Testing on PECS.

Increase The JTA Transaction Timeout Seconds Field in Weblogic Admin Console

- Open WebLogic Server Administration Console.
- Click Lock & Edit button.
- Click on the Domain name on the left-hand side navigation menu.
- Click on the JTA tab to open the JTA page under Domain \| Configuration.
- Replace current timeout setting with 14400 in the Timeout Seconds field.
- Click on the Save button.
- Click Activate Changes button.

Increase The Stuck Thread Max Time Field in the Weblogic Admin Console

- Open WebLogic Server Administration Console.
- Click Lock & Edit button.
- Expand the Servers node in the left pane to display the servers configured in your domain.
- Click the name of the server instance that you want to modify.
- Select the Configuration —\> Tuning tab in the right pane.
- Modify the Stuck Thread Max Time = 2147483647
- Click on the Save button.
- Click Activate Changes button.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the deployment is updated, PECS will be smoke tested.

The system administrator will check application logs for the absence of errors.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Properties Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No property file changes are required for this deployment. The pre-existing PECS v6.2.3 property files will be used.

### Import VA Certificates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No certificate changes are required for this deployment. The pre-existing PECS v6.2.3 VA certificates will be used.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, the AITC database administrator should monitor the Oracle Enterprise Manager/Cloud Control to note any performance problems.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out strategy for the PECS Java application is to restore the previous PECS v6.2.3 EAR file.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PREC\*6.2\*4.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing is performed by the Business Office.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out should only be considered if it is determined that PREC\*6.2\*4 is the cause of a patient safety issue or catastrophic system failure.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks of backing out include not reconfiguring the application in the same manner it was before the start of the implementation. This can be remediated by taking backups of the appropriate file systems and database before starting the deployment.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS Sustainment PM has the authority to determine if a back-out of PREC\*6.2\*4 is required.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deploy the previous PECS v6.2.3 application EAR file in WebLogic.

1.  Stop the Managed Server.
2.  Un-deploy the two existing EAR files for the PECS v6.2.4 application.
3.  Deploy the two previous EAR files for the PECS v6.2.3 application.
4.  Start the PECS Application.
5.  Perform Smoke Testing on PECS

    Reset the JTA Transaction timeout and Stuck Thread Max timeout to their previous value.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A smoke test will be performed to determine that the application is working properly.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PREC\*6.2\*4.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PREC\*6.2\*4.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PREC\*6.2\*4.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PREC\*6.2\*4.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PREC\*6.2\*4.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PREC\*6.2\*4.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PREC\*6.2\*4.