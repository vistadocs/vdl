---
consolidated_title: "vista imaging exchange (vix) production operations manual"
app_code: MAG
doc_type: POM
master_source: "VistA Imaging Exchange (VIX) Production Operations Manual (POM)"
master_pub_date: November 2024
consolidated_from: 5 versions
prior_versions:
  - "MAG*3*269 VistA Imaging Exchange (VIX) Production Operations Manual (POM)"
  - "MAG*3*303 VistA Imaging Exchange (VIX) Production Operations Manual (POM)"
  - "MAG*3*329 VistA Imaging Exchange (VIX) Production Operations Manual (POM)"
  - "MAG*3*348 VistA Imaging Exchange (VIX) Production Operations Manual (POM)"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>VistA Imaging eXchange (VIX) <span id="PatchTitle" class="anchor"></span>Enhancements and Maintenance

  MAG\*3.0\*<span id="PatchNumber" class="anchor"></span>358

  Production Operations Manual (POM)
---

![](vista-imaging-exchange-vix-production-operations-manual-pom/001.png)

November 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date       | Revision | Description                             | Author                             |
|------------|----------|-----------------------------------------|------------------------------------|
| 11/04/2024 | 8.0      | Initial draft for MAG\*3.0\*358         | VA IT VistA Imaging Technical team |
| 01/02/2024 | 7.3      | Updates for MAG\*3.0\*348 release date. | VA IT VistA Imaging Technical team |
| 12/01/2023 | 7.2      | Updates for MAG\*3.0\*348 release date. | VA IT VistA Imaging Technical team |
| 11/01/2023 | 7.1      | Updates for MAG\*3.0\*348 release date. | VA IT VistA Imaging Technical team |
| 09/01/2023 | 7.0      | Initial draft for MAG\*3.0\*348         | VA IT VistA Imaging Technical team |
| 05/03/2023 | 6.0      | Initial draft for MAG\*3.0\*329         | VA IT VistA Imaging Technical team |
| 11/01/2022 | 5.0      | Update for MAG\*3.0\*303                | VA IT VistA Imaging Technical team |
| 06/01/2022 | 4.2      | Updates for MAG\*3.0\*269 release date. | VA IT VistA Imaging Technical team |
| 02/18/2022 | 4.1      | Update for MAG\*3.0\*269 name           | VA IT VistA Imaging Technical team |
| 11/04/2021 | 4.0      | Update for MAG\*3.0\*269                | VA IT VistA Imaging Technical team |
| 08/31/2021 | 3.0      | Update for MAG\*3.0\*284                | Maryann Shovestul                  |
| 01/07/2021 | 2.0      | Update for MAG\*3.0\*254                | VA IT VistA Imaging Technical team |
| 05/21/2020 | 1.0      | Update for MAG\*3.0\*249                | <span class="mark">REDACTED</span> |
| 03/13/2019 | 0.15     | Update for MAG\*3.0\*230                | <span class="mark">REDACTED</span> |
| 12/21/2018 | 0.10     | Updated for MAG\*3.0\*221               | <span class="mark">REDACTED</span> |
| 4/11/2018  | 0.9      | Updated for MAG\*3.0\*201               | <span class="mark">REDACTED</span> |
| 4/5/2018   | 0.8      | Additional MAG\*3.0\*197 Updates        | <span class="mark">REDACTED</span> |
| 1/19/2018  | 0.7      | Updated for MAG\*3.0\*197               | <span class="mark">REDACTED</span> |
| 11/14/2017 | 0.6      | Additional MAG\*3.0\*185 Updates        | <span class="mark">REDACTED</span> |
| 10/17/2017 | 0.5      | Updated for MAG\*3.0\*185               | <span class="mark">REDACTED</span> |
| 5/8/2017   | 0.4      | Date and other minor updates            | <span class="mark">REDACTED</span> |
| 3/27/2017  | 0.3      | Updated for MAG\*3.0\*177               | <span class="mark">REDACTED</span> |
| 2/10/2017  | 0.2      | Initial draft                           | <span class="mark">REDACTED</span> |
| 9/23/2016  | 0.1      | Initial draft                           | <span class="mark">REDACTED</span> |

Table 1: User Notification Points of Contact

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the Production Operations Manual has been baselined.

Artifact Rationale

The Production Operations Manual provides the information needed by the production operations team to maintain and troubleshoot the product. The Production Operations Manual must be provided prior to release of the product.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Intended Audience](#intended-audience)
- [Routine Operations](#routine-operations)
  - [Administrative Procedures](#administrative-procedures)
    - [System Start-up](#system-start-up)
    - [System Shut-down](#system-shut-down)
    - [Back-up & Release](#back-up-release)
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
    - [Availability Monitoring](#availability-monitoring)
    - [Performance/Capacity Monitoring](#performancecapacity-monitoring)
    - [Critical Metrics](#critical-metrics)
  - [Routine Updates, Extracts, and Purges](#routine-updates-extracts-and-purges)
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
This document explains how to maintain and administer the Veterans Health Information Systems and Technology Architecture Imaging Exchange service (most often referred to as the VistA Imaging eXchange (VIX) service). The VIX is used to facilitate data sharing and exchange across organizational and functional boundaries. Currently, the VIX’s primary purpose is to support image sharing between the Department of Veterans Affairs (VA) medical facilities and between the VA and the Department of Defense (DoD) medical facilities. It is anticipated that the VIX’s role will be expanded to support data sharing and exchange within a facility and between facilities. This document assumes that the VIX is installed and configured. For information about VIX system requirements, installation, and configuration, see the [*MAG\*3.0\*<u>358</u> VIX Installation Guide.*](https://www.va.gov/vdl/application.asp?appid=105)

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is intended for VA staff responsible for managing a local VIX. It describes how remote VIXes log access to locally stored images. This document presumes a working knowledge of the VistA environment, VistA Imaging components and workflow, and Windows server administration.

# Routine Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Administrative Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### System Start-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide and the MAG\*3.0\*<u>358</u> VIX Installation Guide.*](https://www.va.gov/vdl/application.asp?appid=105)

#### System Start-Up from Emergency Shut-Down

See the *[VIX Administrator’s Guide and the MAG\*3.0\*<u>358</u> VIX Installation Guide.](https://www.va.gov/vdl/application.asp?appid=105)*

### System Shut-down

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the *[VIX Administrator’s Guide and the MAG\*3.0\*<u>358</u> VIX Installation Guide.](https://www.va.gov/vdl/application.asp?appid=105)*

#### Emergency System Shut-down

See the *[VIX Administrator’s Guide and the MAG\*3.0\*<u>358</u> VIX Installation Guide.](https://www.va.gov/vdl/application.asp?appid=105)*

### Back-up & Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Back-up Procedures

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

#### Restore Procedures

N/A

#### Back-up Testing

N/A

#### Storage and Rotation

N/A

## Security / Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### Access control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### VIX Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### Other VIX Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### VIX Security Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

## User Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### User Notification Points of Contact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                               | Organization                       | Phone                              | URL                                | Method (email/phone) | Priority | Time |
|------------------------------------|------------------------------------|------------------------------------|------------------------------------|----------------------|----------|------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | Phone                | Tier 3   | N/A  |

Table 2: Critical Metrics

## System Monitoring, Reporting & Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### Dataflow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### Availability Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### Performance/Capacity Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System performance can be assessed by the response times experienced by the end-user. The system resources are self-managed. The cache is sized not to exceed available storage sizes.

### Critical Metrics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| System Accessibility           | 24/7                                |
|--------------------------------|-------------------------------------|
| System Uptime                  | Based on VistA uptime               |
| Online Operational Performance | Aggregate image throughput \>5 Mb/s |
| Production Incidents           | Fewer than 1/month                  |

Table 3: Responsibility Matrix for Entities involved with VistA Patching:

## Routine Updates, Extracts, and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Scheduled Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Capacity Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Initial Capacity Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The hardware was sized to service the estimated user demand based on an estimated number of requests during peak usage.

# Exception Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Site personnel are expected to contact the Health, Clinical Services Diagnostics Team (previously known as Clin 3, the group name is SPM.Health.ClinSvs.Diag) team via a Service Now ticket to resolve operation errors. Programmatic problems are triaged to developers.

## Routine Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system may generate a small set of errors that may be considered routine in the sense that they have minimal impact on the user and do not compromise the operational state of the system. Most of the errors are transient in nature and only require the user to retry an operation. The following subsections describe these errors, their causes, and what, if any, response an operator needs to take.

While the occasional occurrence of these errors may be routine, a large number of errors over a short period of time is an indication of a more serious problem. In that case, many errors need to be treated as an exceptional condition.

### Security Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the system is a component of a larger system that is responsible for user-level security, it is expected that all errors related to security are handled by the controlling application. All security failures (e.g., inability to access resources or stored objects) are generally caused by the controlling application either incorrectly passing security tokens or failing user authentication. Other security issues are under the jurisdiction of the site VistA Imaging security that has already established protocols and procedures.

### Time-outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### Concurrency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Significant Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant errors can be defined as errors or conditions that affect the system stability, availability, performance, or otherwise make the system unavailable to its user base. The following subsections contain information to aid administrators, operators, and other support personnel in resolving significant errors, conditions, or other issues.

### Application Error Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105)

### Application Error Codes and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See [*Section 3.2.1: Application Error Logs*](#application-error-logs)

### Infrastructure Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

#### Database

The application installs SQLite a Structured Query Language (SQL) database that is completely self-managed. There are no site interactions required to maintain this database. The purpose of the database is to manage cached objects. The complete loss of this database is not a failure as it gets repopulated with each caching operation. The amount of data stored in the database and the cache is managed by the application based on available storage. No specific database errors are identified.

#### Web Server

Web Services are provided by the VIX using already deployed components. No other Commercial-Off-The-Shelf (COTS) components are required. Refer to the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105) for specific errors.

#### Application Server

N/A

#### Network

N/A

#### Authentication & Authorization

Refer to the [*VIX Administrator’s Guide*.](https://www.va.gov/vdl/application.asp?appid=105) The VIX services use pass-through authentication via security tokens. Errors manifest themselves as the inability to load images. Correction of these errors involves the controlling application or altering the site-specific settings in VistA Imaging.

#### Logical and Physical Descriptions

N/A

## Dependent System(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIX Viewer is part of VistA Imaging components. The main system dependency is on VistA. Inability to access Vista is logged in the VIX logs, and alerts are sent via email.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Errors manifest themselves as the inability to load images. A review of the VIX error logs and transaction logs is the only tool available on the VIX to troubleshoot these conditions. Refer to the [*VIX Administrator’s Guide*](https://www.va.gov/vdl/application.asp?appid=105) for further details.

## System Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections define the process and procedures necessary to restore the system to a fully operational state after a service interruption. Each of the subsections starts at a specific system state and ends up with a fully operational system.

### Restart after Non-Scheduled System Interruption

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See [*Section 2.1.1: System Start-up and Shut Down*](#system-start-up)

### Restart after Database Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Back-out Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it is necessary to uninstall the MAG\*3.0\*358 VIX, go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*358 VIX Service Installation Wizard. To backout the VIX and replace it with the prior version which was included in MAG\*3.0\*357, please see the [*MAG\*3.0\*<u>358</u> VIX Installation Guide*](https://www.va.gov/vdl/application.asp?appid=105) for more detail

### Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it is necessary to uninstall the MAG\*3.0\*358 VIX, go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*358 VIX Service Installation Wizard. To rollback the VIX and replace it with the prior version which was included in MAG\*3.0\*357, please see the [*MAG\*3.0\*<u>358</u> VIX Installation Guide*](https://www.va.gov/vdl/application.asp?appid=105) for more detail

# Operations and Maintenance Responsibilities/RACI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This responsibility matrix defines the roles and responsibilities for supporting VistA patches as part of a deployed solution. This is a template of the standard support structure required for VistA patches; therefore, the Project Manager (PM) should note any deviations in responsibility from this standardized Field Operations responsibility matrix in the Operational Acceptance Plan (OAP).

VistA Patching is generally relegated to the sustainment of existing solutions but may also include emergency “hotfix” patches designed to remediate a noted deficiency within the solution. This Responsibility Matrix (Responsible, Accountable, Consulted, Informed, or RACI) (Table 3, Table 4, Table 5, and Table 6) is related to VistA patches released and supported at the national level (known as “Class I” patches), which are distributed to the entire Enterprise after testing and release management has been completed. VistA Patches are released via the FORUM, KERNEL, or via Secure File Transfer Protocol (SFTP) directly to the Field.

|                                               | R     | A   | C   | I     |
|-----------------------------------------------|-------|-----|-----|-------|
| SL = OI&T Service Lines                   | x |     |     | x |
| NSD = OI&T National Service Desk          |       |     |     |       |
| FCIO = Facility Chief Information Officer |       |     |     | x |
| SL = OI&T Service Lines                   |       |     |     | x |
| Application Service Line (SL-ASL)         |       |     |     | x |
| SL = OI&T Service Lines                   |       |     |     | x |

Table : Responsibility Matrix for Core Systems Service Line

|                                                   | R     | A     | C   | I     |
|---------------------------------------------------|-------|-------|-----|-------|
| PS = OI&T Product Support                     |       |       |     | x |
| VHA = Local Facility medical staff (customer) |       |       |     | x |
| FO = Field Operations                         |       |       |     | x |
| PD = OI&T Product Developer                   | x |       |     |       |
| DSO = VHA Decision Support Office             |       |       |     | x |
| HPS = Health Product Support                  |       | x |     |       |

Table : Responsibility Matrix for Support

|                                    | R     | A   | C   | I   |
|------------------------------------|-------|-----|-----|-----|
| Tier 1: NSD                        | x |     |     |     |
| Tier 2: (local OI&T – FCIO/SL-ASL) | x |     |     |     |
| Tier 3: HPS                        | x |     |     |     |
| Tier 4: PD/Maintenance             | x |     |     |     |

Table : Responsibility Matrix for Field Operations VistA Patching

| FO VistA Patching Responsibility Matrix                 | Production Environments    |
|---------------------------------------------------------|----------------------------|
| Application development                                 | PD                         |
| Release Management                                      | HPS                        |
| Rollback Plan                                           | PD                         |
| Application installation                                | FCIO/SL-ASL                |
| Application support                                     | NSD, FCIO, SL, HPS, Vendor |
| Client/Server Update (where applicable)                 | SL-Core                    |
| OS Patching (where applicable)                          | SL-Core                    |
| Change Management                                       | SL-ASL                     |
| Application Administration (Operations and Maintenance) | SL-ASL                     |
| Local Training for Front Line Staff                     | VHA                        |
| National Training (where applicable)                    | DSO                        |

Table : Definitions, Acronyms, and Abbreviations

# Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REVIEW DATE:

SCRIBE:

<span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Portfolio Director Date

<span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Product Owner Date

<span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Receiving Organization POC (Operations Support) Date

<span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Operations Support POC Date

<span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Project Manager Date

1.  <span id="_Toc181633332" class="anchor"></span>References
- [*MAG\*3.0\*<u>358</u> Deployment, Installation, Back-Out, and Rollback Plan*](https://www.va.gov/vdl/application.asp?appid=105)
- [*VIX Administrator’s Guide  
  > *](https://www.va.gov/vdl/application.asp?appid=105)
  1.  [<span id="_Toc181633333" class="anchor"></span>Definitions*,*](https://www.va.gov/vdl/application.asp?appid=105) Acronyms, and Abbreviations

| Acronym | Definition                                                      |
|---------|-----------------------------------------------------------------|
| COTS    | Commercial Off The Shelf                                        |
| DoD     | Department of Defense                                           |
| FCIO    | Facility Chief Information Officer                              |
| FO      | Field Operations                                                |
| HPS     | Healthy Product Support                                         |
| NSD     | National Service Desk                                           |
| OAP     | Operational Acceptance Plan                                     |
| OIT     | Office of Information Technology                                |
| PD      | Product Developer                                               |
| PM      | Program Manager                                                 |
| POM     | Production Operations Manual                                    |
| RACI    | Responsible, Accountable, Consulted Informed                    |
| SFTP    | Secure File Transfer Protocol                                   |
| SL      | Service Lines                                                   |
| SQL     | Structured Query Language                                       |
| VA      | Department of Veterans Affairs                                  |
| VistA   | Veterans Health Information Systems and Technology Architecture |
| VIX     | VistA Imaging eXchange                                          |