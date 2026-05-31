---
title: DATUP Version 4.0.1 Deployment, Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: null
app_code: PRED
app_name: 'Pharmacy: Pharmacy Data Update (DATUP)'
section: GUI
app_status: active
pkg_ns: PRED
patch_ver: 4.0.1
patch_id: PRED*4.0.1
group_key: PRED:PRED:4.0.1
file_numbers: []
security_keys: []
menu_options: 0
description: '| Date | Version | Description | Author | |------------|-------------|--------------------------|----------------------| | 07/12/2024 | 1.0 | DATUP 4.0.1 / PRED\*4\*2 | Liberty IT Solutions'
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 2046
section_count: 31
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: July 2024
revision_count: 1
revision_newest: 07/12/2024
revision_oldest: 07/12/2024
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/PRED_4_0_P2_DIBR.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/PRED_4_0_P2_DIBR.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=203
audit_applied: '2026-05-31'
master_source: DATUP Version 4.0.1 Deployment, Installation, Back-out, and Rollback Guide
master_pub_date: July 2024
consolidated_from: 2 versions
prior_versions:
- PRED*4*3 DATUP Version 4.0.3 Deployment, Installation, Back-out, and Rollback Guide
consolidated_title: datup deployment, installation, back-out, and rollback guide
---

![](datup-version-4-0-1-deployment-installation-back-out-and-rollback-guide/001.png)

July 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description          | Author           |
|------------|-------------|--------------------------|----------------------|
| 07/12/2024 | 1.0         | DATUP 4.0.1 / PRED\*4\*2 | Liberty IT Solutions |

<span id="_Toc154486942" class="anchor"></span>Table 6: Deployment/Installation/Back-Out Checklist

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

The Veteran-focused Integrated Process (VIP) 4.0 Guide indicates the VA Product (Line) Accountability and Reporting System (VA PARS) reporting tool requires a Gateway Review that will move the project from the Planning Stage and to the Build Stage and will require Release Approval before deploying into production. The Product Line Manager will ensure necessary documents are made available for the release approval process.

Table of Contents

List of Tables

List of Figures

[Figure 1: DATUP Repository [5](#_Toc154486794)](#_Toc154486794)

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
This document describes how to deploy and install the PRED\*4\*2 release of the DATUP version (v) 4.0.1, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial Off-The-Shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan to provide a single, common document that describes how, when, where, and to whom the PRED\*4\*2 release will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following must be available during the deployment.

- First Databank (FDB) Framework (Fwk) COTS set up for incremental updates.
- Configuration changes for Consolidated Mail Outpatient Pharmacy (CMOP) on Secure File Transfer Protocol (sFTP) Server.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints for the PRED\*4\*2 release.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc154486937" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                                    | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|---------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | Austin Information Technology Center (AITC) | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                 |                                  |
| 2      | AITC                                        | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment                           |                                  |
| 3      | AITC                                        | Deployment       | Test for operational readiness                                                                                      |                                  |
| 4      | AITC                                        | Deployment       | Execute deployment                                                                                                  |                                  |
| 5      | DATUP Sustainment Team                      | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |                                  |
| 6      | Product Support                             | Post Deployment  | Hardware, Software and System Support                                                                               |                                  |

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the schedule and milestones for the deployment.

Contract Dates :

- Base Period: 5/4/2020 – 5/3/2021
- Extension Period 1: 5/6/2021 – 10/7/2022
- Extension Period 2: 9/16/2022 – 2/15/2023
- Extension Period 3: 2/16/2023 – 9/26/2023
- Extension Period 4: 9/27/2023 – 9/15/2024

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DATUP v4.0.1 Java Enterprise Edition (J2EE) application will be nationally deployed at AITC after initial operating capacity (IOC) testing and national release approval.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DATUP v4.0.1 Java Application is a single, nationally deployed application deployed in AITC.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DATUP Java Application and Database will be installed on the existing DATUP v4.0.1 production platform.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 3.2 describes the DATUP Java Application.

User acceptance testing (UAT) successfully completed by the Business Office, Pharmacy Benefits Management (PBM).

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

<span id="_Toc154486938" class="anchor"></span>Table 2: Site Preparation

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            |                           |                                             |                   |           |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pre-existing DATUP v4.0 environment resources will be used.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

<span id="_Toc154486939" class="anchor"></span>Table 3: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      |                |                     |           |

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

<span id="_Toc154486940" class="anchor"></span>Table 4: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   |           |             |                   |                  |           |

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

<span id="_Toc154486941" class="anchor"></span>Table 5: Software Specifications

| Required Software                   | Version    | Configuration |
|-----------------------------------------|----------------|-------------------|
| Oracle WebLogic                         | 12.2.1.4.1     | Pre-existing      |
| Oracle 19c Enterprise Edition Release   | 19.14.0.0.0    | Pre-existing      |
| Red Hat Enterprise Linux Server (RHELS) | 7.0 (Santiago) | Pre-existing      |
| Java Software Development Kit (SDK)     | 1.8.0_391      | Pre-existing      |

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Notify business owner of production deployment
- The Release Manager will schedule activities and identify the required personnel for each activity.
- Meetings will be scheduled for deployment personnel to work through the deployment steps.<span id="_Toc87859373" class="anchor"></span>Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task  |
|----------|-----|------|--------------------------------|
| Deploy   | TBD | TBD  | Infrastructure Operations (IO) |
| Install  | TBD | TBD  | IO                             |
| Back-Out | N/A | N/A  | IO                             |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DATUP J2EE will be installed on the existing DATUP v4.0 production platform.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pre-existing DATUP v4.0 platform will be used. Specifics will be detailed in the Request For Change (RFC) order.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Section 4.5, specific filenames will be detailed in the RFC order.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new FDB Fwk v4.5 database will need to be set up.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All scripts and files are provided to AITC Infrastructure Operations team via Outlook/Teams. The installer should follow the instructions in the appropriate RFC documents.

Installation scripts needed for the software and database installation, as well as the procedure on how to set up FDB Fwk v4.5, are provided in VA GitHub EC, located in the [datup-code](https://github.ec.va.gov/EPMO/datup-code/tree/master) repository docs folder. DBA should make sure to disable the archive mode before setting up 4.5 schema and then enable it after schema import.

<span id="_Toc154486794" class="anchor"></span>Figure 1: DATUP Repository

![](datup-version-4-0-1-deployment-installation-back-out-and-rollback-guide/002.png)

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron job changes are required for this deployment.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide reference instructions on how to perform these functions (e.g., vendor-supplied operating system manuals, VistA publications, or other reference materials).  
Linux System Administrator will need:

- Access to the Linux console of the server where DATUP's WebLogic is running
- Access to the WebLogic web-based Console
- Access to the location indicated in section 4.5 Installation Scripts

Database Administrator will need:

- Access to the Linux console of the server where DATUP's Oracle Database is running
- Access to the location indicated in section 4.5 Installation Scripts

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is a high-level overview of the installation procedure steps. Detailed steps are in the RFCs for the Database and Application deployment, and they will be published at the locations in Section 4.5.

1.  Stop the Managed Server
1.  Install EAR file for DATUP 4.0.1.
2.  Validate the fdb_datup4_configuration.properties for SFTP server path location, if updated.
3.  Validate any changes to datasource name FDB45_DIF for database connection the one new EAR file for DATUP v4.0.1 Application
4.  Start the DATUP Application
5.  Perform Smoke Test on DATUP

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After deployment is updated, DATUP will be smoke tested.

The system administrator will check application logs for the absence of errors.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Properties Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No property file changes are required for this deployment. The pre-existing DATUP v4.0 property file will be used.

### Import VA Certificates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No certificate changes are required for this deployment. The pre-existing DATUP v4.0 VA certificates will be used.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, the AITC Database Administrator (DBA) should monitor Oracle Enterprise Manager/Cloud Control to note any performance problems.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out strategy for the DATUP Java application is to restore the previous DATUP EAR file in PRED\*4\*1.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for PRED\*4\*2.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) is performed at test sites during IOC Testing.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out of PRED\*4\*2 should only be considered if it is determined there is the cause for a patient safety issue or catastrophic system failure.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks of backing out include not reconfiguring the application in the same manner it was before the start of the implementation. This can be remediated by taking backups of the appropriate file systems and database before the start of the deployment.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DATUP Sustainment PM has the authority to determine if a back-out of PRED\*4\*2 is required.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deploy the previous latest DATUP application EAR file in WebLogic, currently PRED\*4\*1 as of January 2024.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A smoke test will be performed to determine that the application is working properly.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Section 5 for rollback procedures.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A