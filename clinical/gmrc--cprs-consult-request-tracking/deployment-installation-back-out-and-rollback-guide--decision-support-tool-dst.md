---
title: Decision Support Tool (DST) Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: plain
doc_subject: Decision Support Tool (DST)
app_code: GMRC
app_name: 'CPRS: Consult/Request Tracking'
section: CLI
app_status: archive
pkg_ns: GMRC
patch_ver: null
patch_id: null
group_key: null
file_numbers: []
security_keys: []
menu_options: 0
description: '> Deployment, Installation, Back-Out, and Rollback Guide'
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 4467
section_count: 25
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: April 2020
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking_Archive/dst_dibr.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking_Archive/dst_dibr.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=343
audit_applied: '2026-05-31'
master_source: Decision Support Tool (DST) Deployment, Installation, Back-Out, and Rollback Guide
master_pub_date: April 2020
consolidated_from: 2 versions
prior_versions:
- Decision Support Tool (DST) Deployment, Installation, Back-Out, and Rollback Guide v1.1.1314
consolidated_title: decision support tool (dst) deployment, installation, back-out, and rollback guide
---

> Care Coordination Decision Support Tool (DST)

> Build 20

> Deployment, Installation, Back-Out, and Rollback Guide (DIBR)

![](decision-support-tool-dst-deployment-installation-back-out-and-rollback-guide/001.png)

> April 2020 Department of Veterans Affairs

> Office of Information and Technology (OIT)

> Revision History

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 16%" />
<col style="width: 43%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>04/13/2020</td>
<td>1.8</td>
<td>Updated for Build 20 v1.1.972</td>
<td>Ablevets</td>
</tr>
<tr class="even">
<td>03/03/2020</td>
<td>1.7</td>
<td>Updated for Build 20</td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>02/05/2020</td>
<td>1.6</td>
<td>Updated for Build 19</td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>11/21/2019</td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>Updated for Build 18</p>
</blockquote></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>10/03/2019</td>
<td><blockquote>
<p>1.4</p>
</blockquote></td>
<td><blockquote>
<p>Updated for Build 18</p>
</blockquote></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>09/09/2019</td>
<td>1.3</td>
<td>Updated for Build 18</td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>08/13/2019</td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>Updated for v1.1</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/06/2019</td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>Updated for v1.0.12</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>07/30/2019</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Updated for v1.0.11</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>07/22/2019</td>
<td><blockquote>
<p>0.9</p>
</blockquote></td>
<td><blockquote>
<p>Updated for v1.0.10</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>07/16/2019</td>
<td><blockquote>
<p>0.8</p>
</blockquote></td>
<td><blockquote>
<p>Updated for v1.0.09</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>07/08/2019</td>
<td><blockquote>
<p>0.7</p>
</blockquote></td>
<td><blockquote>
<p>Updated for v1.0.08</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>06/12/2019</td>
<td><blockquote>
<p>0.6</p>
</blockquote></td>
<td><blockquote>
<p>Updated for v1.0.05</p>
</blockquote></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>05/30/2019</td>
<td><blockquote>
<p>0.5</p>
</blockquote></td>
<td><blockquote>
<p>Updated for v1.0.04</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>05/15/2019</td>
<td><blockquote>
<p>0.4</p>
</blockquote></td>
<td><blockquote>
<p>Defect remediation</p>
</blockquote></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>04/26/2019</td>
<td><blockquote>
<p>0.3</p>
</blockquote></td>
<td><blockquote>
<p>Defect remediation</p>
</blockquote></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>04/24/2019</td>
<td><blockquote>
<p>0.2</p>
</blockquote></td>
<td><blockquote>
<p>Added TLS installation specific to GMRC*3.0*125 Patch Information</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/11/2019</td>
<td><blockquote>
<p>0.1</p>
</blockquote></td>
<td><blockquote>
<p>Initial Draft</p>
</blockquote></td>
<td><blockquote>
<p>AbleVets</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

1.  1.  
    2.  
    3.  
2.  
3.  1.  
    2.  1.  
        2.  
    3.  1.  
        2.  
        3.  
    4.  
4.  1.  1.  
        2.  
        3.  
        4.  
    2.  
    3.  
    4.  
    5.  
    6.  
    7.  
    8.  
    9.  
    10. 
5.  1.  
    2.  
6.  1.  
    2.  
    3.  
    4.  
    5.  
7.  

[Introduction 1](#introduction)[Purpose 1](#purpose)[Dependencies 1](#dependencies)[Constraints 2](#constraints)[Roles and Responsibilities 3](#roles-and-responsibilities)[Deployment 3](#deployment)[Timeline 4](#timeline)[Site Readiness Assessment 4](#site-readiness-assessment)[Deployment Topology (Targeted Architecture) 4](#deployment-topology-targeted-architecture)[Site Information (Locations, Deployment Recipients) 5](#site-information-locations-deployment-recipients)[Resources 5](#resources)[Hardware 5](#hardware)[Software 7](#software)[Communications 7](#communications)[Deployment/Installation/Back-Out Checklist 7](#deploymentinstallationback-out-checklist)[Installation 8](#installation)[Platform Installation and Preparation in Facility level 8](#platform-installation-and-preparation-in-facility-level)[Consult Toolbox 8](#consult-toolbox)[VistA DST Patch to the GMRC Package at Each VistA Site 8](#vista-dst-patch-to-the-gmrc-package-at-each-vista-site)[DST Application 9](#dst-application)[Cerner PowerChart 9](#cerner-powerchart)[Download and Extract Files 9](#download-and-extract-files)[Database ETL Jobs 9](#database-etl-jobs)[Installation Scripts 10](#installation-scripts)[Cron Scripts 11](#cron-scripts)[Access Requirements and Skills Needed for the Installation 11](#access-requirements-and-skills-needed-for-the-installation)[Installation Procedure 11](#installation-procedure)[Installation Verification Procedure 11](#installation-verification-procedure)[System Configuration 12](#system-configuration)[Database Tuning 12](#database-tuning)[Back-Out Procedure 12](#back-out-procedure)[Back-Out Procedure 12](#back-out-procedure-1)[Authority for Back-Out 12](#authority-for-back-out)[Rollback Procedure 12](#rollback-procedure)[Rollback Considerations. 12](#rollback-considerations.)[Rollback Criteria 12](#rollback-criteria)[Rollback Risks 13](#rollback-risks)[Authority for Rollback 13](#authority-for-rollback)[Rollback Procedure 13](#rollback-procedure-1)[Risk and Mitigation Plan 13](#risk-and-mitigation-plan)

> List of Tables

> [Table 1: DST Application Dependencies 1](#_bookmark3)

> [Table 2: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities 3](#_bookmark6)

> [Table 3: DST Task Names and Start Dates 4](#_bookmark9)

> [Table 4: Hardware Specifications 6](#_bookmark15)

> [Table 5: Software Specifications 7](#_bookmark17)

> [Table 6: Deployment/Installation/Back-Out Checklist 7](#_bookmark20)

> [Table 7: CDW ETL Jobs 10](#_bookmark29)

> [Table 8: Cron Scripts 11](#_bookmark32)

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
  - [Resources](#resources)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
  - [Deployment/Installation/Back-Out Checklist](#deploymentinstallationback-out-checklist)
- [Installation](#installation)
  - [Platform Installation and Preparation in Facility level](#platform-installation-and-preparation-in-facility-level)
    - [Consult Toolbox](#consult-toolbox)
    - [VistA DST Patch to the GMRC Package at Each VistA Site](#vista-dst-patch-to-the-gmrc-package-at-each-vista-site)
    - [DST Application](#dst-application)
    - [Cerner PowerChart](#cerner-powerchart)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database ETL Jobs](#database-etl-jobs)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Authority for Back-Out](#authority-for-back-out)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations.](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
- [Risk and Mitigation Plan](#risk-and-mitigation-plan)
This document describes how to deploy and install the Community Care Decision Support Tool (DST) as well as how to back-out the product and rollback to a previous version or data set if applicable. This document is a companion to the project charter and management plan for this effort. This document details the criteria for determining if a back-out is necessary, the authority for making that decision, the order in which installed components will be backed out, the risks and criteria for a rollback, and authority for acceptance or rejection of the risks.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the DST be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DST Application is dependent on the following Systems/Applications/Services.

> <span id="_bookmark3" class="anchor"></span>Table 1: DST Application Dependencies

| Dependency                            | Type | Dependency Type | DST Use                                                                                                                                                                                                                                                                                            |
|-------------------------------------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Computerized Patient Record System (CPRS) | System   | System              | Consult data is supplied to DST. This data is used to initiate a DST decision for a given consult.                                                                                                                                                                                                     |
| Master Veteran Index (MVI)                | Service  | Data/Information    | Internal data service to access Master Patient Index (MPI)/MVI external data. Will contain all unique query logic to interact with the external service, along with external interface configuration setup (such as authentication).                                                                   |
| Corporate Data Warehouse (CDW)            | Service  | Data/Information    | Internal data service to interact and query CDW cached data. Data will be a scheduled task to load CDW into the DST environment. CDW data will reside within DST for lookup and reference within the DST decision logic. The data will have its own designated datastore due it being relational data. |

| Dependency                                 | Type | Dependency Type | DST Use                                                                                                                                                                                                              |
|------------------------------------------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enrollment System Redesign (E&E/ESR)           | Service  | Data/Information    | Internal data service to access Enrollment Service external data. Will contain all unique query logic to interact with the external service, along with external interface configuration setup (such as authentication). |
| Provider Profile Management System (PPMS)      | Service  | Data/Information    | Internal data service to access PPMS external data. Will contain all unique query logic to interact with the external service, along with external interface configuration setup (such as authentication).               |
| Lighthouse Application Program Interface (API) | Service  | Data/Information    | Internal data service to access facility data. Will contain all unique query logic to interact with the external service, along with external interface configuration setup (such as authentication).                    |
| Standardized Episodes of Care (SEOC)           | Service  | Data/Information    | Internal data service to access SEOC stored internal data. Will contain all unique query logic to interact with the datastore to query data, including configuration setup (such as authentication).                     |

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DST project team, software, and test servers will adhere to the following directives, policies, procedures, standards, and guidelines:

- Veteran-focused Integration Process (VIP).
- Section 508 Information Technology (IT) accessibility standards governed under 29

> U.S.C 794d.

- Health Insurance Portability and Accountability Act (HIPAA).
- VA DIRECTIVE 6508 - Privacy Impact Assessments.
- VA Directive 6500 – Information Security Program.
- One-VA Technical Reference Model (TRM).
- VA Standards & Conventions Committee (SACC) Codes Standards and Conventions.
- The DST will pass any Web Application Security Assessment (WASA) scans.
- The DST will not have any Critical or High issues identified by a Fortify scan.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the following table for the deployment, installation, back-out, and rollback roles and responsibilities.

> <span id="_bookmark6" class="anchor"></span>Table 2: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team             | Phase / Role                                                                                                    | Tasks                                                                                                                      |
|--------|----------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| 1      | AbleVets Development | Deployment in Local Dev                                                                                             | Plan and schedule deployment in local environment                                                                              |
| 2      | AbleVets Development | Deployment in Software Quality Assurance (SQA)/User Acceptance Testing (UAT) in Department of Veterans Affairs (VA) | Determine and document the roles and responsibilities of those involved in the deployment.                                     |
| 3      | AbleVets Development | Deployment in Production                                                                                            | Test for operational readiness                                                                                                 |
| 4      | AbleVets Development | Installation                                                                                                        | Plan and schedule installation                                                                                                 |
| 6      | VA                   | Installation                                                                                                        | Validate through facility point of contact (POC) to ensure that IT equipment has been accepted using asset inventory processes |
| 8      | AbleVets Development | Back-out                                                                                                            | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)            |
| 9      | AbleVets Development | Post Deployment                                                                                                     | Hardware, Software and System Support                                                                                          |

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as an iterative rollout. The following swim lane provides the high- level overview of DST Release Process.

> ![](decision-support-tool-dst-deployment-installation-back-out-and-rollback-guide/002.png)Figure 1: Overview of the DST Release Process

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section providers the project schedule and milestones for this version.

> <span id="_bookmark9" class="anchor"></span>Table 3: DST Task Names and Start Dates

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 34%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Task Name</strong></th>
<th><blockquote>
<p><strong>Start Date</strong></p>
</blockquote></th>
<th><strong>End Date</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Hand-off to SQA</td>
<td><blockquote>
<p>04/06/2020</p>
</blockquote></td>
<td><blockquote>
<p>04/06/2020</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SQA Testing</td>
<td><blockquote>
<p>04/07/2020</p>
</blockquote></td>
<td>04/10/2020</td>
</tr>
<tr class="odd">
<td>Promote Code to Pre-Prod</td>
<td><blockquote>
<p>No PreProd events for Build 20</p>
</blockquote></td>
<td>No PreProd events for Build 20</td>
</tr>
<tr class="even">
<td>Release to Prod</td>
<td><blockquote>
<p>04/14/2020</p>
</blockquote></td>
<td>04/14/2020</td>
</tr>
</tbody>
</table>

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DST application will exist within the VA Enterprise Cloud (VAEC) for DEV, PREPROD, DEMO (Sandbox), and Production environments. The DST development team will maintain a local DEV to be used for sprint development and testing processes.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The figure below shows the Deployment Topology (Targeted Architecture) of the DST application.

> ![](decision-support-tool-dst-deployment-installation-back-out-and-rollback-guide/003.png)Figure 2: Deployment Topology (Targeted Architecture)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment of the DST web interface will be to Initial Operating Capability (IOC) sites so that users can verify the functionalities of DST. Once testing is completed and DST is approved for national release, DST will be deployed nationally.

DST will be deployed to the following IOC sites.

- <span class="mark">redacted</span>

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes hardware, software, facilities, documentation, and any other resources, other than personnel, required for deployment and installation.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST is in the VAEC cloud enclave. There are three VAEC cloud environments maintained. All environments have a common hardware parity with the hardware specifications listed below. All application software and microservice configuration (Kubernetes) are executed on the hardware.

Please refer to [Table 2](#_bookmark6) in the Roles and Responsibilities section of this document for details about who is responsible for preparing the site to meet these hardware specifications.

> ![](decision-support-tool-dst-deployment-installation-back-out-and-rollback-guide/004.png)Figure 3: Hardware Resources

> <span id="_bookmark15" class="anchor"></span>Table 4: Hardware Specifications

| Required Hardware | Model | Version | Configuration | Manufacturer | Other   |
|-----------------------|-----------|-------------|-------------------|------------------|-------------|
| AWS                   | M5        | XLarge      | Virtual           | Virtual          | All Servers |

| Technology Component Production 1 | Location         | Usage                                                          |
|---------------------------------------|----------------------|--------------------------------------------------------------------|
| DST Production – VA Cloud             | VA Cloud environment | To serve the DST application within the VA Production environment. |

| Technology Component Verification/Test | Location         | Usage                                                                     |
|--------------------------------------------|----------------------|-------------------------------------------------------------------------------|
| DST PreProd – VA Cloud                     | VA Cloud environment | To test the DST application within a VA test and/or verification environment. |

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Technology Component Verification/Test</strong></th>
<th><strong>Location</strong></th>
<th><strong>Usage</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>DST DEV/SQA/DEMO – VA</p>
<p>Cloud</p></td>
<td>VA Cloud environment</td>
<td>To test the DST application within a VA test and/or verification environment.</td>
</tr>
</tbody>
</table>

| Technology Component Development | Location               | Usage                                                                                     |
|--------------------------------------|----------------------------|-----------------------------------------------------------------------------------------------|
| DST Development – AbleVets Cloud     | AbleVets Cloud environment | To develop, test, and demo the DST application before transition to the VA cloud environment. |

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required prior to deployment. If there are difference depending upon site, those difference will need to be provided.

> <span id="_bookmark17" class="anchor"></span>Table 5: Software Specifications

| Required Software | Make                | Version |
|-----------------------|-------------------------|-------------|
| Apache                | Apache Software         | 2.4.X       |
| Kubernetes            | Red Hat                 | 1.13.X      |
| Docker                | Docker, Inc             | 18.06.0-ce  |
| Red Hat               | Enterprise Linux Server | 7.X         |

Please refer to [Table 2](#_bookmark6) in the Roles and Responsibilities section of this document for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notification of scheduled maintenance periods that require the service to be offline or that may degrade system performance will be disseminated to the business user community a minimum of 48 hours prior to the scheduled event.

Notification to VA users for unscheduled system outages or other events that impact the response time will be distributed within 30 minutes of the occurrence.

Notification to VA users for unexpected system outages or other events that impact the response time will be distributed to Users as soon as possible.

Notification will be distributed to VA users regarding technical help desk support for obtaining assistance with receiving and processing.

## Deployment/Installation/Back-Out Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below outlines the coordination effort and documents for the day/time/individual when each activity (deploy, install, back-out) is completed for DST.

> <span id="_bookmark20" class="anchor"></span>Table 6: Deployment/Installation/Back-Out Checklist

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Activity</strong></th>
<th><blockquote>
<p><strong>Day</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Time</strong></p>
</blockquote></th>
<th><strong>Individual who completed task</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Deploy</td>
<td><blockquote>
<p>Dependent on current build timeline</p>
</blockquote></td>
<td><blockquote>
<p>When approved by VA stakeholders</p>
</blockquote></td>
<td>AbleVets</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Activity</strong></th>
<th><blockquote>
<p><strong>Day</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Time</strong></p>
</blockquote></th>
<th><strong>Individual who completed task</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Install</td>
<td><blockquote>
<p>Dependent on current build timeline</p>
</blockquote></td>
<td><blockquote>
<p>When approved by VA stakeholders</p>
</blockquote></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>Back-Out</td>
<td><blockquote>
<p>Dependent on current build timeline</p>
</blockquote></td>
<td><blockquote>
<p>When approved by VA stakeholders</p>
</blockquote></td>
<td>AbleVets</td>
</tr>
</tbody>
</table>

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Platform Installation and Preparation in Facility level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST requires the following four separate components to be deployed for each facility.

### Consult Toolbox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Consult Toolbox (CTB) is the Auto Hotkey component of the DST solution that is installed as a thick-client on the CPRS user's workstations by the VA-ITOPS team. It is responsible for monitoring the state of which CPRS screen is displayed to the User, presenting the user with the option to launch DST, and facilitating the transfer of information between CPRS and the DST API/Database. Starting with version v1.9.0044 for MISSION Act, CTB included a dedicated DST .ini file that includes a string parameter containing the root URL for the DST endpoints.

When this parameter is NULL or the DST .ini file is not found, Consult Toolbox does not attempt any communication with DST and operates based on its pre-DST user experience. The initial national deployment of CTB v1.9.0044 was deployed with the DST URL set to an empty string.

During Quality Assurance and User Acceptance testing, the latest, approved version of CTB is used to verify full end-to-end solution.

### VistA DST Patch to the GMRC Package at Each VistA Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST Veterans Health Information Systems and Technology Architecture (VistA) Patches GMRC are the VistA component of DST which must be installed on every VistA system where CPRS users need to use DST. The patch includes a protocol that invokes a process to retrieve the consult factor text from DST and insert it into a consult comment whenever a consult is signed that contains the string "DST ID:" in the Reason for Request field. The patch also adds the ability for the DST to Auto Forward requested Consults in accordance with Community Care Directives.

If the DST URL is not active during SQA testing, a test endpoint will be created to allow for end-to-end testing of the DST patch operation. The DST endpoint will respond when the CPRS RPC, detects the presence of literal "DST ID:", in an order. The Protocol will then trigger and retrieve consult factor text from the DST API and insert the consult factor text into a newly- created consult. If the Auto-Forwarding comment is also included, then the Consult will be Forwarded to the included consult name.

The installation procedure for this VistA patch are uploaded to VA Forum per VA installation requirements.

### DST Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DST is a web application that is invoked during the consult ordering workflow in CPRS using Consult Toolbox to intercept user interactions to inform the Veteran and their referring clinician about the availability of services in the VA and the Veteran's eligibility for receiving care in the community.

DST provides three main capabilities in support of the MISSION Act requirements:

- Inform the Veteran and their referring clinician about service availability at nearby VA facilities and the Veteran's eligibility for Community Care.
- Document the outcome of the care pathway decision process and provide structured data in the CPRS order.
- Report on system-wide compliance and utilization.

When the user opts to open DST, Consult Toolbox sends the following patient and consult information from CPRS. After DST is opened, DST orchestration calls all data partners to display all required decision data from the internal VA data interfaces namely - CDW, Eligibility and Enrollment system (E&E/ESR) Service, PPMS, Lighthouse API, SEOC, and MVI. Further, the user enters a DST eligibility decision to be collected by a supportive VistA data interface to save in the consult.

### Cerner PowerChart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cerner's PowerChart is a hybrid Electronic Medical Record (EMR) solution that caters to clinicians in hospitals and ambulatory facilities and helps them to create multi-entity electronic medical records. The solution also provides capabilities for on-premise deployment. It provides various built-in templates that cover various specialties, thus serving a wide range of medical providers. PowerChart coordinates care between multiple locations and practitioners, helping users manage duplicated records while still giving staff flexible documentation options. These documentation options are reflected in the solution's database of templates and customizable procedure workflows.

The DST application supports the Electronic Health Record Modernization (EHRM) by providing a Decision Support Viewer (DSV) application within the same DST application installation. The DSV application is used from Cerner's PowerChart to review community care eligibility information for the patient.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST does not download and extract files as a manual process. DST builds all environments using CI/CD pipeline approach utilizing a Jenkins build machine. With use of the Kubernetes infrastructure, as described in later sections, all services that comprise the DST application are compiled, packaged, published in the DST Jenkins environment. When a new deployment is available for an environment, the published Docker image artifacts are pulled from the registry to be installed within Kubernetes environment.

## Database ETL Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DST application relies on CDW data to provide clinical information and average wait time for services on the application. This information is loaded daily as part of CDW Extract,

Transform, Load (ETL) jobs maintained by the DST project team. This ETL code is maintained in the VA GitHub dst-cdw-etl repository and executed on a shared CDW ETL server maintained by the VA CDW group. This information is listed for informational purposes only. There are no additional install instructions needed for this release.

> <span id="_bookmark29" class="anchor"></span>Table 7: CDW ETL Jobs

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Job Name</strong></th>
<th><blockquote>
<p><strong>Schedule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Purpose</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Consult-Clinical Services Mappings</td>
<td><blockquote>
<p>Every day at 2 AM</p>
</blockquote></td>
<td><blockquote>
<p>Refreshes consult name to clinical service based on clinical stop codes</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Facility-Clinical Services AWT</td>
<td><blockquote>
<p>Every week at 2 AM</p>
</blockquote></td>
<td><blockquote>
<p>Refreshes facility average wait time based on clinical stop codes</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](decision-support-tool-dst-deployment-installation-back-out-and-rollback-guide/005.png)Figure 4: CDW ETL Jobs

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following database scripts found in the dst-postgres-db code repo must be run for Build 20 functionality.

1.  21_alter_decision_support_hsrm_25005.sql
2.  22_Update_cc_average_wait_time default-1_Consult_AWT.sql
3.  22_mockData_for_acceptanceTests.sql

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST executed scheduled jobs within the Kubernetes ecosystem to load SEOC, load static facility information, and purged DST records. These jobs are part of the dst-scheduler VA Git repository. This code repository is built as a Kubernetes container pod. This information is listed for informational purposes only. There are no additional install instructions needed for this release.

> <span id="_bookmark32" class="anchor"></span>Table 8: Cron Scripts

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Job Name</strong></th>
<th><blockquote>
<p><strong>Schedule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Purpose</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Delete_Decision_Support</td>
<td><blockquote>
<p>Every day at 2 AM</p>
</blockquote></td>
<td><blockquote>
<p>Purges stale DST records that are greater than 30 days old, since DST is the source of record for this data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Load_SEOC</td>
<td><blockquote>
<p>Every day at 2 AM</p>
</blockquote></td>
<td><blockquote>
<p>Refreshes active SEOC data within DST system.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Load_Facilities</td>
<td><blockquote>
<p>Every day at 5 AM</p>
</blockquote></td>
<td><blockquote>
<p>Refreshes static facility information from Lighthouse API.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers will need to have a proper ePAS in order to gain access to the server with elevated privileges. The installers will need to have knowledge of Apache, Kubernetes, Docker, and Git.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DST application uses Helm commands to install the DST Helm chart. This chart describes the DST Kubernetes microservices and configuration for the system. Helm and Kubernetes are maintained in each DST VA Git repository. Specifically, the DST main chart that maintains the complete DST ecosystem is within the env-dst-pod-migration VA Git repository. The following steps are part of automated VA Jenkins job that run based on latest tested changes from the DST GitHub code repos.

To upgrade DST microservices with a new version of the software on any DST node that has Helm installed, execute the following commands:

1.  helm repo update \#get all latest charts.
2.  helm upgrade \<chart name\> --namespace \<DST namespace\> --version=\<version to be upgrade to\>.
3.  helm list \#to verify latest charts that are installed.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the installation is running on any DST node that has Helm installed, execute the following command: helm list \#to verify latest charts that are installed. This process is executed during the normal installation procedures of the application.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps described below outline the procedure to remove the DST application from the CPRS Platform in Production.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On any DST node that has Helm installed, execute the following commands:

1.  helm list \#to verify latest charts that are installed.
2.  helm rollback \<chart name\> --version \<version to be rolled back\>.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on authority provided by our Business Sponsor and VA Office of Information and Technology (OIT) IT program manager, DST can be backed out in accordance to their approval.

DST can back-out any service within the Kubernetes cluster, which are all application components.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database (DB) snapshots are taken every evening. To restore the DST Database instance from a DB snapshot

1.  Sign into the Amazon Web Services (AWS) Management Console and open the Amazon Relational Database Service (RDS) console.
2.  In the navigation pane, choose Snapshots.
3.  Choose the DB snapshot that you want to restore from.
4.  For Actions, choose Restore Snapshot. The Restore DB Instance page displays.
5.  For DB Instance Identifier under Settings, enter the name that you want to use for the restored Database instance. If you are restoring from a DB instance that you deleted after you made the Database snapshot, you can use the name of that DB instance.
6.  Choose Restore DB Instance.

## Rollback Considerations.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST can roll back the DST AWS RDS Postgres instance.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback criteria are not applicable.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is minimal risk associated to these rollback procedures. It is common practice to rollback Kubernetes microservices and is part of the design of the technology. All DST application code and infrastructure are maintained as code saved in source control in VA GitHub, so there is minimal potential loss of functionality when an issue arises. Finally, AWS provides highly resilient backup processes for all the DST AWS RDS database.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on authority provided by our Business Sponsor and VA OIT IT program manager, DST can be backed out in accordance to their approval.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure steps are documented in Section 5.1 [Back-Out Procedure](#back-out-procedure-1) for the application and infrastructure. The backout instructions are the same as rollback for the application. The rollback procedure steps are documented in Section [6](#rollback-procedure) for the database.

# Risk and Mitigation Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DST project team maintains a Program Risk Registry. Refer to the Program Risk Registry for all risks and mitigation plans for the entire DST project, including Consult Toolbox and VistA integration along with the VA partner interfaces (MPI/MVI, E&E/ESR, PPMS, Lighthouse API, CDW, SEOC).