---
title: MAG*3*197 Production Operations Manual
doc_type: POM
doc_label: Production Operations Manual
doc_layer: patch
doc_subject: 
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: archive
pkg_ns: MAG
patch_ver: 3
patch_id: MAG*3*197
group_key: "MAG:MAG:3"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document explains how to maintain and administer the Veterans Health Information Systems and Technology Architecture (VistA) Imaging Exchange (VIX) service. The VIX is used to facilitate data sharing and exchange across organizational and functional boundaries. Currently the VIX’s primary pur
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - procedures
  - errors
  - back
  - application
  - routine
  - security
  - restore
  - capacity
page_count: 0
word_count: 1269
section_count: 14
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 8
revision_newest: 4/5/2018
revision_oldest: 9/23/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/mag3_0p197_production_operations_manual_05022018.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/mag3_0p197_production_operations_manual_05022018.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=413"
---

# Image Viewer Version 2.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Image Viewer Version 2.0](#image-viewer-version-20)
    - [MAG\3.0\197](#mag30197)
    - [Revision History](#revision-history)
- [Artifact Rationale](#artifact-rationale)
- [Introduction](#introduction)
  - [Intended Audience](#intended-audience)
- [Routine Operations](#routine-operations)
  - [Administrative Procedures](#administrative-procedures)
    - [System Start-up and Shut Down](#system-start-up-and-shut-down)
    - [Back-up & Restore](#back-up-restore)
  - [Security / Identity Management](#security-identity-management)
    - [Identity Management](#identity-management)
    - [Access control](#access-control)
    - [VIX Interfaces](#vix-interfaces)
    - [Other VIX Components](#other-vix-components)
    - [VIX Security Certificate](#vix-security-certificate)
  - [User Notifications](#user-notifications)
    - [User Notification Points of Contact](#user-notification-points-of-contact)
  - [System Monitoring, Reporting & Tools](#system-monitoring-reporting-tools)
    - [Dataflow Diagram](#dataflow-diagram)
    - [Performance/Capacity Monitoring](#performancecapacity-monitoring)
    - [Critical Metrics](#critical-metrics)
  - [Routine Updates, Extracts and Purges](#routine-updates-extracts-and-purges)
  - [Scheduled Maintenance](#scheduled-maintenance)
  - [Capacity Planning](#capacity-planning)
    - [Initial Capacity Plan](#initial-capacity-plan)
- [Exception Handling](#exception-handling)
  - [Routine Errors](#routine-errors)
    - [Security Errors](#security-errors)
    - [Time-outs](#time-outs)
    - [Concurrency](#concurrency)
  - [Significant Errors](#significant-errors)
    - [Application Error Logs](#application-error-logs)
    - [Application Error Codes and Descriptions](#application-error-codes-and-descriptions)
    - [Infrastructure Errors](#infrastructure-errors)
  - [Dependent System(s)](#dependent-systems)
  - [Troubleshooting](#troubleshooting)
  - [System Recovery](#system-recovery)
    - [Restart after Non-Scheduled System Interruption](#restart-after-non-scheduled-system-interruption)
    - [Restart after Database Restore](#restart-after-database-restore)
    - [Back-out Procedures](#back-out-procedures)
    - [Rollback Procedures](#rollback-procedures)
- [Operations and Maintenance Responsibilities/RACI](#operations-and-maintenance-responsibilitiesraci)
- [Approval Signatures](#approval-signatures)
- [References](#references)
- [Acronyms](#acronyms)
> Production Operations Manual (POM)
![](mag-3-197-production-operations-manual/001.png)

### MAG\*3.0\*197

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date   | Version | Description                  | Author                         |
|------------|-------------|----------------------------------|------------------------------------|
| 4/5/2018   | 0.8         | Additional MAG\*3.0\*197 Updates | <span class="mark">REDACTED</span> |
| 1/19/2018  | 0.7         | Updated for MAG\*3.0\*197        | <span class="mark">REDACTED</span> |
| 11/14/2017 | 0.6         | Additional MAG\*3.0\*185 Updates | <span class="mark">REDACTED</span> |
| 10/17/2017 | 0.5         | Updated for MAG\*3.0\*185        | <span class="mark">REDACTED</span> |
| 5/8/2017   | 0.4         | Date and other minor updates     | <span class="mark">REDACTED</span> |
| 3/27/2017  | 0.3         | Updated for MAG\*3.0\*177        | <span class="mark">REDACTED</span> |
| 2/10/2017  | 0.2         | Initial draft                    | Development Team                   |
| 9/23/2016  | 0.1         | Initial draft                    | Development Team                   |
> Note: The revision history cycle begins once changes or enhancements are requested after the Production Operations Manual has been baselined.

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Production Operations Manual provides the information needed by the production operations team to maintain and troubleshoot the product. The Production Operations Manual must be provided prior to release of the product.

1.  [Introduction 4](#introduction)
    1.  [Intended Audience 4](#intended-audience)
2.  [Routine Operations 4](#routine-operations)
    1.  [Administrative Procedures 4](#administrative-procedures)
        1.  [System Start-up and Shut Down 4](#system-start-up-and-shut-down)
        2.  [Back-up & Restore 4](#back-up-restore)
            1.  [Back-Up Procedures 4](#back-up-procedures)
            2.  [Restore Procedures 4](#restore-procedures)
            3.  [Back-Up Testing 4](#back-up-testing)
            4.  [Storage and Rotation 4](#storage-and-rotation)
    2.  [Security / Identity Management 4](#security-identity-management)
        1.  [Identity Management 5](#identity-management)
        2.  [Access control 5](#access-control)
        3.  [VIX Interfaces 5](#vix-interfaces)
        4.  [Other VIX Components 5](#other-vix-components)
        5.  [VIX Security Certificate 5](#vix-security-certificate)
    3.  [User Notifications 5](#user-notifications)
        1.  [User Notification Points of Contact 5](#user-notification-points-of-contact)
    4.  [System Monitoring, Reporting & Tools 5](#system-monitoring-reporting-tools)
        1.  [Dataflow Diagram 5](#dataflow-diagram)
        2.  [Performance/Capacity Monitoring 5](#performancecapacity-monitoring)
        3.  [Critical Metrics 5](#critical-metrics)
    5.  [Routine Updates, Extracts and Purges 5](#routine-updates-extracts-and-purges)
    6.  [Scheduled Maintenance 6](#scheduled-maintenance)
    7.  [Capacity Planning 6](#capacity-planning)
        1.  [Initial Capacity Plan 6](#initial-capacity-plan)
3.  [Exception Handling 6](#exception-handling)
    1.  [Routine Errors 6](#routine-errors)
        1.  [Security Errors 6](#security-errors)
        2.  [Time-outs 6](#time-outs)
        3.  [Concurrency 6](#concurrency)
    2.  [Significant Errors 6](#significant-errors)
        1.  [Application Error Logs 7](#application-error-logs)
        2.  [Application Error Codes and Descriptions 7](#application-error-codes-and-descriptions)
        3.  [Infrastructure Errors 7](#infrastructure-errors)
            1.  [Database 7](#database)
            2.  [Web Server 7](#web-server)
            3.  [Application Server 7](#application-server)
            4.  [Network 7](#network)
            5.  [Authentication & Authorization 7](#authentication-authorization)
            6.  [Logical and Physical Descriptions 7](#logical-and-physical-descriptions)
    3.  [Dependent System(s) 7](#dependent-systems)
    4.  [Troubleshooting 8](#troubleshooting)
    5.  [System Recovery 8](#system-recovery)
        1.  [Restart after Non-Scheduled System Interruption 8](#restart-after-non-scheduled-system-interruption)
        2.  [Restart after Database Restore 8](#restart-after-database-restore)
        3.  [Back-out Procedures 8](#back-out-procedures)
        4.  [Rollback Procedures 8](#rollback-procedures)
4.  [Operations and Maintenance Responsibilities/RACI 9](#operations-and-maintenance-responsibilitiesraci)
5.  [Approval Signatures 10](#approval-signatures)
1.  [References 11](#references)
2.  [Acronyms 12](#acronyms)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document explains how to maintain and administer the Veterans Health Information Systems and Technology Architecture (VistA) Imaging Exchange (VIX) service. The VIX is used to facilitate data sharing and exchange across organizational and functional boundaries. Currently the VIX’s primary purpose is to support image sharing between the Department of Veterans Affairs (VA) medical facilities as well as between VA and the Department of Defense (DoD) medical facilities. It is anticipated that the VIX’s role will be expanded to support data sharing and exchange within a facility as well as between facilities. This document assumes that the VIX is installed and configured. For information about VIX system requirements, installation, and configuration see the [*<u>MAG\*3.0\*197 VIX Installation Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document is intended for VA staff responsible for managing a local VIX. Some parts of this document may also be of interest to VA Imaging Coordinators at non-VIX sites. It describes how remote VIXes log access to locally stored images. This document presumes a working knowledge of the VistA environment; VistA Imaging components and workflow; and Windows server administration.

# Routine Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Administrative Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### System Start-up and Shut Down

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide and the MAG\*3.0\*197 VIX Installation Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### Back-up & Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Back-Up Procedures

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

#### Restore Procedures

> No tape restore.

#### Back-Up Testing

> N/A.

#### Storage and Rotation

> N/A.

## Security / Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### Access control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### VIX Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### Other VIX Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### VIX Security Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

## User Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Notification Points of Contact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                           | Organization                   | Phone                          | Email                          | Method (email/phone)           | Priority                       | Time                           |
|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

## System Monitoring, Reporting & Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### Dataflow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### Performance/Capacity Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> System performance can be assessed by the response times experienced by the end user. The system resources are self-managed. Cache is sized not to exceed available storage sizes.

### Critical Metrics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A.

## Routine Updates, Extracts and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A.

## Scheduled Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A.

## Capacity Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A.

### Initial Capacity Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The hardware was sized to service the estimated user demand based on an estimated number of requests during peak usage.

# Exception Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Site personnel are expected to contact CLIN3 via an NSD ticket to resolve operation errors. Programmatic problems are triaged to developers.

## Routine Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system may generate a small set of errors that may be considered routine in the sense that they have minimal impact on the user and do not compromise the operational state of the system. Most of the errors are transient in nature and only require the user to retry an operation. The following subsections describe these errors, their causes, and what, if any, response an operator needs to take.

> While the occasional occurrence of these errors may be routine, a large number of errors over a short period of time is an indication of a more serious problem. In that case, the error needs to be treated as an exceptional condition.

### Security Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since the system is a component of a larger system that is responsible for user-level security, it is expected that all errors related to security are handled by the controlling application. All security failures (e.g., inability to access resources or stored objects) are generally caused by the controlling application either incorrectly passing security tokens or failing user authentication.

> Other security issues are under the jurisdiction of the site VistA Imaging security that has already established protocols and procedures.

### Time-outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### Concurrency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A.

## Significant Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Significant errors can be defined as errors or conditions that affect the system stability, availability, performance, or otherwise make the system unavailable to its user base. The

> following subsections contain information to aid administrators, operators, and other support personnel in the resolution of significant errors, conditions, or other issues.

### Application Error Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### Application Error Codes and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See [*<u>Section 3.2.1: Application Error Logs</u>*](#application-error-logs)

### Infrastructure Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A.

#### Database

> The application installs a Structured Query Language (SQL) Server database that is completely self-managed. There are no site interactions required to maintain this database. The purpose of the database is to manage cached objects. The complete loss of this database is not a failure as it gets repopulated with each caching operation. The amount of data stored in the database and the cache is managed by the application based on available storage. No specific database errors are identified.

#### Web Server

> Web Services are provided by the VIX using already deployed components. No other Commercial Off-The-Shelf (COTS) components are required. Refer to the *[<u>VIX Administrator’s</u>](https://www.va.gov/vdl/application.asp?appid=105)* [*<u>Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105) for specific errors.

#### Application Server

> N/A.

#### Network

> N/A.

#### Authentication & Authorization

> Refer to the [<u>*VIX Administrator’s Guide*.</u>](https://www.va.gov/vdl/application.asp?appid=105) The VIX services use pass through authentication via security tokens. Errors manifest themselves as the inability to load images. Correction of these errors involve the controlling application or altering the site specific settings in VistA Imaging.

#### Logical and Physical Descriptions

> N/A.

## Dependent System(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX Viewer is part of VistA Imaging. The main system dependency is on VistA. Inability to access Vista is logged in the VIX logs, and alerts are sent via email.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Errors manifest themselves as the inability to load images. Review of the VIX error logs and transaction logs is the only tool available on the VIX to troubleshoot these conditions. Refer to the [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105) for further details.

## System Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following subsections define the process and procedures necessary to restore the system to a fully operational state after a service interruption. Each of the subsections starts at a specific system state and ends up with a fully operational system.

### Restart after Non-Scheduled System Interruption

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [<u>Section 2.1.1: System Start-up and Shut Down</u>](#system-start-up-and-shut-down)

### Restart after Database Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A.

### Back-out Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>MAG\*3.0\*197 VIX Installation Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

### Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the [*<u>MAG\*3.0\*197 VIX Installation Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

# Operations and Maintenance Responsibilities/RACI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This responsibility matrix defines the roles and responsibilities for supporting VistA patches as part of a deployed solution. This is a template of the standard support structure required for VistA patches therefore the Project Manager (PM) should note any deviations in responsibility from this standardized Field Operations responsibility matrix in the Operational Acceptance Plan (OAP).

> VistA Patching is generally relegated to sustainment of existing solutions but may also include emergency “hot fix” patches designed to remediate a noted deficiency within the solution. This Responsibility Matrix (Responsible, Accountable, Consulted, Informed, or RACI) is related to VistA patches released and supported at the national level (known as “Class I” patches) which are distributed to the entire Enterprise after testing and release management has been completed. VistA Patches are released via the FORUM, KERNEL or via Secure File Transfer Protocol (SFTP) directly to the Field.

#### Entities involved with VistA Patching:

> NSD = OI&T National Service Desk FCIO = Facility Chief Information Officer SL = OI&T Service Lines

> Application Service Line (SL-ASL) Core Systems Service Line (SL-Core)

> PS = OI&T Product Support VHA = Local Facility medical staff (customer)

> FO = Field Operations

> PD = OI&T Product Developer

> DSO = VHA Decision Support Office

> HPS = Health Product Support

#### Support:

> Tier 1: NSD

> Tier 2: (local OI&T – FCIO/SL-ASL) Tier 3: HPS

> Tier 4: PD/Maintenance

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>FO VistA Patching Responsibility Matrix</th>
<th>Production Environments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Application development</td>
<td>PD</td>
</tr>
<tr class="even">
<td>Release Management</td>
<td>HPS</td>
</tr>
<tr class="odd">
<td>Rollback Plan</td>
<td>PD</td>
</tr>
<tr class="even">
<td>Application installation</td>
<td>FCIO/SL-ASL</td>
</tr>
<tr class="odd">
<td>Application support</td>
<td>NSD, FCIO, SL, HPS, Vendor</td>
</tr>
<tr class="even">
<td>Client/Server Update (where applicable)</td>
<td>SL-Core</td>
</tr>
<tr class="odd">
<td>OS Patching (where applicable)</td>
<td>SL-Core</td>
</tr>
<tr class="even">
<td>Change Management</td>
<td>SL-ASL</td>
</tr>
<tr class="odd">
<td><p>Application Administration (Operations and</p>
<p>Maintenance)</p></td>
<td>SL-ASL</td>
</tr>
<tr class="even">
<td>Local Training for Front Line Staff</td>
<td>VHA</td>
</tr>
<tr class="odd">
<td>National Training (where applicable)</td>
<td>DSO</td>
</tr>
</tbody>
</table>

# Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Indicate the approval of the Production Operations Manual below or by recording approval in the appropriate Work Item or CD#2 decision in the Rational tool set.*

> REVIEW DATE: *\<date\>*

> SCRIBE: *\<name\>*

> Signed:

> Portfolio Manager Date

> Signed:

> Product Owner Date

> Signed:

> Receiving Organization (Operations Support) Date

> Signed:

> Product Support Date

> Signed:

> Project Manager Date

# References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- [*<u>MAG\*3.0\*197 Deployment, Installation, Back-Out, and Rollback Plan</u>*](https://www.va.gov/vdl/application.asp?appid=105)
- [*<u>VIX Administrator’s Guide</u>*](https://www.va.gov/vdl/application.asp?appid=105)
> •

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ACL Access Control List
> BSE Broker Security Enhancement
> COTS Commercial Off-The-Shelf CRUD Create, Read, Update and Delete CVIX Central VistA Imaging Exchange
> DCF DICOM® Connectivity Framework
> DICOM Digital Imaging and Communications in Medicine DoD Department of Defense
> JLV Joint Legacy Viewer
> JPEG Joint Photographic Experts Group JRE Java Runtime Environment
> PACS Picture Archiving and Communication System POM Production Operations Manual
> SQL Structured Query Language
> VA Department of Veterans Affairs
> VistA Veterans Health Information Systems and Technology Architecture VIX VistA Imaging Exchange
