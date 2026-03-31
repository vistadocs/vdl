---
consolidated_title: "ampl production operations manual"
app_code: PREA
doc_type: POM
master_source: "AMPL Production Operations Manual"
master_pub_date: January 2026
consolidated_from: 2 versions
prior_versions:
  - "AMPL Production Operations Manual (POM)"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Advanced Medication Platform (AMPL)  
  Graphical User Interface (GUI)

  Production Operations Manual (POM)
---

![](ampl-production-operations-manual/001.png)

January 2026

Revision History

<table>
<caption><p><span id="_Toc191975496" class="anchor"></span>Table 1: AMPL Security Configuration by Environment</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 39%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01/2026</td>
<td>1.14</td>
<td><p><a href="#system-start-up">Section 2.1.1</a></p>
<p>Updated the names of the services that are active.</p>
<p><a href="#security-identity-management">Section 2.2</a></p>
<p>Updated the external sources</p>
<p><a href="#identity-management">Section 2.2.1</a></p>
<p>Updated security groups</p>
<p><a href="#user-notification-points-of-contact">Section 2.2.3</a></p>
<p>Updated user notifications points of contact table.</p>
<p><a href="\l">Section 2.4</a></p>
<p>Updated routine updates, extracts, and purges</p>
<p><a href="#capacity-planning">Section 2.6</a></p>
<p>Updated Capacity Planning number of users.</p>
<p><a href="#initial-capacity-plan">Section 2.6.1</a></p>
<p>Updated the initial capacity plan.</p>
<p><a href="#system-recovery">Section 3.5</a></p>
<p>Removed JumpBox Service from the System Recovery table.</p>
<p><a href="#acronyms-and-abbreviations">Section 5</a></p>
<p>Added HDR (Health Data Repository) to the Acronyms and Abbreviations table.</p></td>
<td>AMPL GUI Team</td>
</tr>
<tr class="even">
<td>08/2025</td>
<td>1.13</td>
<td>No Update</td>
<td>AMPL GUI Team</td>
</tr>
<tr class="odd">
<td>07/2025</td>
<td>1.12</td>
<td><p><a href="#security-identity-management">Section 2.2</a></p>
<p>Replaced IAM Endpoint URLs in the AMPL Security Configuration by Environment table</p></td>
<td>AMPL GUI Team</td>
</tr>
<tr class="even">
<td>04/2025</td>
<td>1.11</td>
<td>Changed numbering to match Build version number</td>
<td>AMPL GUI Team</td>
</tr>
<tr class="odd">
<td>01/2025</td>
<td>1.5</td>
<td>No Update</td>
<td>AMPL GUI Team</td>
</tr>
<tr class="even">
<td>11/2024</td>
<td>1.4</td>
<td>Content Update</td>
<td>AMPL GUI Team</td>
</tr>
<tr class="odd">
<td>06/2024</td>
<td>1.3</td>
<td>No Update</td>
<td>AMPL GUI Team</td>
</tr>
<tr class="even">
<td>02/2024</td>
<td>1.2</td>
<td>Content Update</td>
<td>AMPL GUI Team</td>
</tr>
<tr class="odd">
<td>08/2023</td>
<td>1.0</td>
<td>Document Baseline</td>
<td>AMPL GUI Team</td>
</tr>
</tbody>
</table>

<span id="_Toc191975496" class="anchor"></span>Table 1: AMPL Security Configuration by Environment

Artifact Rationale

The Production Operations Manual (POM) provides the information needed by the production operations team to maintain and troubleshoot the product. The POM must be provided prior to release of the product.

Table of Contents

1\. Introduction [1](#introduction)

2\. Routine Operations [1](#routine-operations)

2.1. Administrative Procedures [1](#administrative-procedures)

2.1.1. System Start-up [1](#system-start-up)

2.1.1.1. System Start-Up from Emergency Shutdown [2](#system-start-up-from-emergency-shutdown)

2.1.2. System Shutdown [2](#system-shutdown)

2.1.2.1. Emergency System Shutdown [2](#emergency-system-shutdown)

2.1.3. Backup and Restore [2](#backup-and-restore)

2.1.3.1. Backup Procedures [2](#backup-procedures)

2.1.3.2. Restore Procedures [3](#restore-procedures)

2.1.3.3. Backup Testing [3](#backup-testing)

2.1.3.4. Storage and Rotation [5](#storage-and-rotation)

2.2. Security / Identity Management [5](#security-identity-management)

2.2.1. Identity Management [6](#identity-management)

2.2.2. Access Control [6](#access-control)

2.2.3. User Notification Points of Contact [7](#user-notification-points-of-contact)

2.3. System Monitoring, Reporting, and Tools [7](#system-monitoring-reporting-and-tools)

2.3.1. Dataflow Diagram [7](#dataflow-diagram)

2.3.2. Availability Monitoring [8](#availability-monitoring)

2.3.3. Performance/Capacity Monitoring [9](#performancecapacity-monitoring)

2.3.4. Critical Metrics [10](#critical-metrics)

2.4. Routine Updates, Extracts and Purges [10](#routine-updates-extracts-and-purges)

2.5. Scheduled Maintenance [10](#scheduled-maintenance)

2.6. Capacity Planning [10](#capacity-planning)

2.6.1. Initial Capacity Plan [11](#initial-capacity-plan)

3\. Exception Handling [11](#exception-handling)

3.1. Routine Errors [11](#routine-errors)

3.1.1. Security Errors [11](#security-errors)

3.1.2. Time Outs [11](#time-outs)

3.1.3. Concurrency [11](#concurrency)

3.2. Significant Errors [12](#significant-errors)

3.2.1. Application Error Logs [12](#application-error-logs)

3.2.2. Application Error Codes and Descriptions [12](#application-error-codes-and-descriptions)

3.2.3. Infrastructure Errors [12](#infrastructure-errors)

3.2.3.1. Database [12](#database)

3.2.3.2. Web Server [13](#web-server)

3.2.3.3. Application Server [13](#application-server)

3.2.3.4. Authentication & Authorization (A&A) [13](#authentication-authorization-aa)

3.2.3.5. Logical and Physical Descriptions [13](#logical-and-physical-descriptions)

3.3. Dependent System(s) [14](#dependent-systems)

3.4. Troubleshooting [14](#troubleshooting)

3.5. System Recovery [15](#system-recovery)

3.5.1. Restart after Non-Scheduled System Interruption [15](#restart-after-non-scheduled-system-interruption)

3.5.2. Restart after Database Restore [15](#restart-after-database-restore)

3.5.3. Back-out Procedures [15](#back-out-procedures)

3.5.4. Rollback Procedures [15](#rollback-procedures)

4\. Operations and Maintenance Responsibilities [15](#operations-and-maintenance-responsibilities)

5\. Acronyms and Abbreviations [17](#acronyms-and-abbreviations)

Table of Tables

Table of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Routine Operations](#routine-operations)
  - [Administrative Procedures](#administrative-procedures)
    - [System Start-up](#system-start-up)
    - [System Shutdown](#system-shutdown)
    - [Backup and Restore](#backup-and-restore)
  - [Security / Identity Management](#security-identity-management)
    - [Identity Management](#identity-management)
    - [Access Control](#access-control)
    - [User Notification Points of Contact](#user-notification-points-of-contact)
  - [System Monitoring, Reporting, and Tools](#system-monitoring-reporting-and-tools)
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
    - [Time Outs](#time-outs)
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
- [Operations and Maintenance Responsibilities](#operations-and-maintenance-responsibilities)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
This document describes how to maintain the components of the Advanced Medication Platform (AMPL) Graphical User Interface (GUI) as well as how to troubleshoot problems that might occur with this product in production. The intended audience for this document is the Information Technology (IT) teams responsible for hosting and maintaining the system after production release.
This document will be finalized prior to production release and includes many updated elements specific to the hosting environment.

# Routine Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the procedures and tasks required for normal operations of the system.

## Administrative Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System administrators will complete routine operations to maintain the configuration, upkeep, and reliable operation of computer systems. Additionally, system administrators ensure that the performance, uptime, resources, and security of the systems meet the needs of the end users.

### System Start-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_System_Start-Up_from" class="anchor"></span>To verify if the AMPL GUI application is functioning, login to the AWS Management Console and run the following commands:

1.  Verify that the product AMPL GUI services are active.
2.  Navigate to the AWS ECS Cluster page (for AMPL-GUI).
3.  Navigate to the production cluster.
4.  Verify that the following services are active and the desired task is not set to zero:
    1.  Production-API-Service
    2.  Production-Web-Service
    3.  Iam-service-prod
    4.  Pgx-service-prod-service
    5.  Preference-prod-service
5.  If a service is down:
    1.  Change the desired task for the API task to a number greater than zero and update the service.
    2.  Ensure that the API service is active, then change the desired task for the Web task to a number greater than zero and update the service.
    3.  Verify that the API and Web tasks are running.
6.  Verify that the application is available by connecting to the application with a browser.

#### System Start-Up from Emergency Shutdown

In the event of a power outage or other abrupt termination of the server operating systems, please start up the servers as detailed in the [System Start-up](#system-start-up) and allow the operating system to check the disks for corruption.

### System Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To stop the ECS cluster running on EC2 instances, there are two steps:

1.  Stop the ECS Cluster services and tasks.
2.  Stop the EC2 instances supporting the ECS Cluster.

#### Emergency System Shutdown

The emergency system shutdown procedure is to shut down all AMPL GUI servers in AWS. These servers may be shut down in any order so the instructions as seen in [System Shutdown](#system-shutdown) can be used.

### Backup and Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI is created using an infrastructure as code methodology, therefore it is not necessary to create application server-level backups. The underlying infrastructure supporting the Container platform is created using archived scripts that are configuration managed within Veteran Administration (VA) controlled source control.

#### Backup Procedures

Auto scheduled snapshots using Lifecycle Manager are utilized to create a backup of instances once a week and are retained for three weeks.

<span id="_Toc194652447" class="anchor"></span>Figure 1: Lifecycle Manager

![](ampl-production-operations-manual/002.png)

#### Restore Procedures

Please refer to [Section 2.1.3.3 Backup Testing](#backup-testing).

#### Backup Testing 

1.  From the Snapshots list, choose the snapshot to create the volume.
2.  Click the Actions button and select Create Volume.

<span id="_Toc194652448" class="anchor"></span>Figure 2: Actions Button

> ![](ampl-production-operations-manual/003.png)

3.  Remember, for Availability Zone, choose the Availability Zone in which to create the volume.

> **NOTE:** EBS volumes can only be attached to EC2 instances in the same Availability Zone.

4.  Choose Create additional tags to add the approved VAEC tags to the volume. For each tag, provide a tag Key and a tag Value.

<span id="_Toc194652449" class="anchor"></span>Figure 3: Create Volume

![](ampl-production-operations-manual/004.png)

5.  Choose Create Volume.
6.  After you have restored a volume from a snapshot, you can attach it to an instance to begin using it. To do so:
    - Stop the instance.
    - Detach the volume and attach the new volume.
    - Start the instance.

<span id="_Toc194652450" class="anchor"></span>Figure 4: Create Volume Succeeded

![](ampl-production-operations-manual/005.png)

7.  Connect to instance.

<span id="_Toc194652451" class="anchor"></span>Figure 5: Remote Desktop Connection

![](ampl-production-operations-manual/006.png)

#### Storage and Rotation

Storage and rotation information is not applicable.

## Security / Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI is a read-only viewer of existing enterprise patient data. All data presented in AMPL GUI is obtained from the following external sources:

- Most all of the AMPL data is obtained from Veterans Data Integration & Federation (VDIF).
- Enterprise-wide patient search and patient images are obtained from Identity and Access Management (IAM) using the Master Patient Index (MPI) and the Veterans Health Identification Card (VHIC) data.
- Pharmacogenomics data is obtained from the Health Data Repository (HDR).

VDIF, IAM, and HDR are outside the ATO boundary of AMPL and implement their own security mechanisms. AMPL uses designated interfaces and security mechanisms to access data via these external sources. Additional information can be found in the *AMPL GUI System Design Document*.

<table>
<caption><p><span id="_Toc191975497" class="anchor"></span>Table 2: AMPL GUI AD Security Groups</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>AMPL Environment</th>
<th>AD Group</th>
<th>IAM Endpoint</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Development</td>
<td>AAC VDIF AMPL Read-Only NPD</td>
<td>https://int.fed.eauth.va.gov/oauthi/sps/oauth/oauth20/metadata/ISAMOP</td>
</tr>
<tr class="even">
<td>SQA</td>
<td>AAC VDIF AMPL Read-Only NPD</td>
<td>https://sqa.fed.eauth.va.gov/oauthi/sps/oauth/oauth20/ metadata/ISAMOP</td>
</tr>
<tr class="odd">
<td>Pre-Prod</td>
<td>AAC VDIF AMPL Read-Only PPD</td>
<td>https://preprod.fed.eauth.va.gov/oauthi/sps/oauth/oauth20/ metadata/ISAMOP</td>
</tr>
<tr class="even">
<td>Production</td>
<td><p>AAC VDIF AMPL Read-Only PRD</p>
<p>AAC VDIF AMPL ReadOnly A-M</p>
<p>AAC VDIF AMPL ReadOnly N-Z</p></td>
<td>https://fed.eauth.va.gov/oauthi/sps/oauth/oauth20/ metadata/ISAMOP</td>
</tr>
</tbody>
</table>

<span id="_Toc191975497" class="anchor"></span>Table 2: AMPL GUI AD Security Groups

### Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI only has one user role defined that allows read-only access to pharmacy-specific patient and medication data. There are no administrative roles defined in AMPL GUI.

User authentication is accomplished through Identity and Access Management (IAM) OAuth2 services and users are required to validate their identity with VA issued Personal Identity Verification (PIV) cards.

User authorization is controlled through membership in VA Active Directory (AD) groups. If the user is a member of the appropriate AD group, they are permitted to retrieve patient data from the VDIF services. Currently there are five AD groups defined for AMPL GUI.

Each AD group permits access to individual AMPL GUI environments and are defined in the table below.

| AD Group                   | AMPL Environment    | User Group                                    |
|----------------------------|---------------------|-----------------------------------------------|
| AAC VDIF AMPL ReadOnly PRD | Production          | Production Clinical and Support users         |
| AAC VDIF AMPL ReadOnly A-M | Production          | Clinical Providers                            |
| AAC VDIF AMPL ReadOn;y N-Z | Production          | Clinical Providers                            |
| AAC VDIF AMPL ReadOnly PPD | Pre-Production      | Test-Site, PBM and SQA test and support users |
| AAC VDIF AMPL ReadOnly NPD | Development and SQA | Test-Site, PBM and SQA test and support users |

<span id="_bookmark28" class="anchor"></span>Table 3: User Notification Points of Contact

### Access Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to AMPL GUI is granted by membership in an AD group. After initial implementation, a site may request access or removal of an individual by submitting a SNOW ticket by contacting the Enterprise Service Desk or by using the YourIT portal. The SNOW ticket must be assigned to the “SPM.Health.PCS.Sub_1. AMPL Engineering” group.

User Notifications

The system administrators will plan maintenance outages on the infrastructure level in AWS Cloud. The planned maintenance calendar will be shared to members of the AMPL team (architects, testers, developers, etc.). Planned outages will be completed on off days (i.e., Friday night or Saturday night). Unplanned outages are addressed when the architect and systems engineer get notified via email.

### User Notification Points of Contact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the personnel who will be notified in the event of scheduled or unscheduled changes in system state.

| Title                           | Name           | Phone    | Email                 |
|-------------------------------------|--------------------|--------------|---------------------------|
| Business Stakeholder                | Amy K. Norris      | 561-543-8876 | Amy.Colon@va.gov          |
| Business Stakeholder                | Dionne L. Roney    | 843-789-6566 | Dionne.Roney@va.gov       |
| Technical POC                       | Asli Goncer        | 407-359-0506 | Asli.Goncer@va.gov        |
| System Owner                        | James Goldsmith    | 903-267-0663 | James.Goldsmith@va.gov    |
| Program Manager                     | James Goldsmith    | 903-267-0663 | James.Goldsmith@va.gov    |
| Information System Security Officer | Bradley Rosborough |              | Bradley.Rosborough@va.gov |

<span id="_Toc191975499" class="anchor"></span>Table 4: DynaTrace and Elastic Search Reports POC

## System Monitoring, Reporting, and Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes a high-level overview of the monitoring for the AMPL production environment.

### Dataflow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following figure depicts the AMPL GUI HealthShare Data Flow. Additional information can be found in the *AMPL GUI System Design Document.*

<span id="_Toc194652452" class="anchor"></span>Figure 6: Logical High Level AMPL GUI HealthShare Data Flow

![](ampl-production-operations-manual/007.png)

### Availability Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Enterprise Cloud (VAEC) AWS GovCloud High is a General Support System that provides a secure application and hosting environment for VA applications, content, and utilities. These applications and services are used to deliver content to an audience comprising employees, Veterans, contractors, partners across all VA medical centers and component facilities, Federal government, and the general public. Content and applications are provided by Veterans Benefits Administration (VBA), Veterans Health Administration (VHA), National Cemetery Administration (NCA), and Support Offices. VAEC provides the following services: Content Delivery, Application Hosting, and Management Services.

The VAEC infrastructure is hosted by AWS GovCloud, a cloud service provider. The AWS GovCloud platform is used to provide a variety of hosting environments to suit a variety of needs. AWS GovCloud can support applications categorized up to High as rated in accordance with Federal Information Processing Standard (FIPS) 199. VA applications available to the public are hosted in AWS GovCloud.

A dedicated private data link (AWS Direct Connect) provides all connectivity for VA resources communicating to the environment. Virtual Private Clouds (VPC) wrap the applications within VAEC AWS GovCloud to encapsulate network access. Access from the applications to VA internal resources such as Identity, Credential, and Access Management (ICAM) and AD Services are conducted over the encrypted private data link to the VA network.

Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events, providing a unified view of AWS resources, applications, and services that run on AWS and on-premises servers. CloudWatch can be used to detect anomalous behavior in environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep applications running smoothly.

Amazon Simple Notification services are in place to send alerts generated from CloudWatch. The figure below displays the notifications sent. The email notifications are sent to the topics subscribed.

<span id="_Toc194652453" class="anchor"></span>Figure 7: Amazon Simple Notification

![](ampl-production-operations-manual/008.png)

### Performance/Capacity Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Performance monitoring is completed by reaching out to the Monitoring Service Registry (MSR) team and onboarded Dynatrace tool. Elastic Search is the mandatory tool for applications on the cloud.

[DynaTrace](https://cex678.dynatrace-managed.com/e/72874c19-c296-4b5f-86cd-a3ba91f5e8e2/#newhosts;gtf=-2h;gf=all), ScienceLogic, and [OpenSearch](https://prod.adfs.federation.va.gov/adfs/ls/idpinitiatedsignon.aspx) are in place to address various monitoring requirements. These dashboards provide information about AWS service including the service and application health, uptime, and capacity planning. AWS Cloud Watch and Amazon Simple Notification Service (SNS) notification services are also in place for monitoring and alerting. Reports can be obtained by contacting the POC in Table 4.

| Tool         | POC                   | Email Address                                                                                        |
|--------------|-----------------------|------------------------------------------------------------------------------------------------------|
| DynaTrace    | Jennifer Jeffress     | <Jennifer.Jeffress@va.gov>                                                                           |
| ScienceLogic | Iran Reynolds         | <Iran.Reynolds@va.gov>                                                                               |
| OpenSearch   | Nicholas Owusu-Sampah | [Nicholas.Owusu-Sampah@va.gov](file:///C:/Users/vhaorlslaugp/Downloads/Nicholas.Owusu-Sampah@va.gov) |

<span id="_Toc191975500" class="anchor"></span>Table 5: Initial Capacity Plan

### Critical Metrics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The critical metrics captured for AMPL GUI are covered in [Section 2.3.3: Performance/Capacity Monitoring](#performancecapacity-monitoring).

## Routine Updates, Extracts, and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI does not maintain or store any data. The AMPL GUI application solely uses VDIF, IAM, and HDR services for patient and pharmacy data retrieval. Therefore, the system does not implement or require any data updates, extracts, or purges.

## Scheduled Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes information on maintenance scheduled for AMPL GUI. The system administrators will plan maintenance outages on the infrastructure level in AWS Cloud. The planned maintenance calendar will be shared to members of the AMPL team (architects, testers, developers, etc.). Planned outages will be completed on off days (i.e., Friday night or Saturday night).

## Capacity Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMPL GUI system has a planned capacity of approximately 20,000 individual users with a maximum of about 4,000 individuals accessing the system simultaneously.

The number of individual users has no impact on AMPL GUI as they are maintained external to AMPL GUI in both the IAM System and the AD system.

The maximum number of simultaneous users is attributable to two factors: the capacity of the AMPL GUI and the capacity of the VDIF systems. To a reasonable extent, the capacity of the AMPL system can be measured in isolation. All testing done to date indicates that production infrastructure exceeds the maximum anticipated load. There is no lower VDIF environment that accurately reflects the production environment and there is no ability to extrapolate performance in production. To date, all tests of the VDIF platform show a deficit in performance.

Both the AMPL and VDIF systems include performance monitoring systems. System capacity is a function of performance, so capacity can be determined in the production environment. This data is periodically reviewed. If a deficit is detected or predicted, an action plan will be created to resolve the deficit.

### Initial Capacity Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial capacity plan includes two phases, which are outlined in the table below. The AMPL GUI system is currently in national release and is monitored by Dynatrace and other tools. These tools are used to measure the key metrics.

| Phase                                | Users | Simultaneous Users | CPU Utilization | Memory Utilization | Response Time  |
|--------------------------------------|-------|--------------------|-----------------|--------------------|----------------|
| Initial Operational Capability (IOC) | ~400  | \<100              | \<5%            | \<50%              | Stable         |
| Initial National Deployment          | ~8000 | \<1000             | \<50%           | \<60%              | \<20% increase |

<span id="_Toc191975501" class="anchor"></span>Table 6: Dependent System(s)

# Exception Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Similar to other systems, AMPL GUI may generate a small set of errors that may be considered routine, in the sense that they have minimal impact on the user and do not compromise the operational state of the system. Most of the errors are temporary in nature and only require the user to retry an operation. The following subsections describe these errors, their causes, and what response an operator needs to take.

## Routine Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While the occasional occurrence of these errors may be routine, getting many individual errors over a short period of time is an indication of a more serious problem. In that case, the error needs to be treated as an exceptional condition. Refer to [Significant Errors](#significant-errors) for more information.

### Security Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security is addressed by IAM Single Sign-On Internal (SSOi). User authentication is handled by the IAM SSOi system. The AMPL subsystem does not provide or enforce a security model. However, the system does access other system interfaces, which may encounter security violations when accessed.

### Time Outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Time outs may occur when accessing the VDIF system. Occasionally queries are dependent upon the availability of VDIF or run out of time if a large-results query is requested.

### Concurrency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI is a read-only application. As a read-only application maintaining data concurrency on writes is not applicable.

The VDIF services provide a federated view of all the VistA systems maintained by the VHA. There are inherent latencies in this system, so updates from source VistA systems may be delayed. Additionally, data caching is employed at various system layers for performance and may incur additional update latency.

## Significant Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant errors can be defined as errors or conditions that affect the system stability, availability, performance, or otherwise make the system unavailable to its user base.

The following subsections contain information to aid administrators, operators, and other support personnel in the resolution of significant errors, conditions, or other issues.

### Application Error Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI uses the AWS CloudWatch for logging of the applications. AMPL uses the Apache Log4j framework for logging.

Logs location – AWS CloudWatch - /ecs/Production-Web and /ecs/Production-Api

Maxfilesize = To be determined

Max. backed up files are not applicable to the AWS CloudWatch environment.

Growth rate is not applicable to the AWS CloudWatch environment.

### Application Error Codes and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An AMPL user may encounter Application System Errors. System Errors are unplanned errors encountered during normal system operation.

These unplanned errors include Java errors (e.g., null pointer exceptions), connection exceptions, and any other unexpected error the system might encounter. The Java errors will be logged in the Application Error Logs.

### Infrastructure Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA IT systems rely on various infrastructure components. These components are defined in the Logical and Physical Descriptions section of this document. Majority of these infrastructure components generate their own set of errors. Each component has its own sub-section and describes how errors are reported. The sub-sections are typical list of components and are meant to be modified for each individual system.

#### Database

AMPL does not employ a Database Management System (DBMS). The only persistence employed by AMPL is AWS S3 Buckets to store user preference data. This solely is configuration data and there is no clinical, PII, or PHI data retained.

#### Web Server

There are no expected errors that may come through the web server. Any unexpected errors need analysis of appropriate tools. Additional information can be found on [The Apache HTTP](https://httpd.apache.org/docs/2.4/logs.html).

#### Application Server

AMPL uses Spring Framework and the Spring Framework Exception Handling to capture and log errors. AMPL logs are in AWS CloudWatch. Assistance from AMPL Java Developers may be required to analyze log file entries to diagnose issues.

Network

The physical and virtual network in which AMPL GUI resides is controlled and managed by VAEC COMMS Team and AWS.

#### Authentication & Authorization (A&A)

Users will use VA SSOi and PIV authentication.

A&A error messages include:

- Smart Card Required: The user has not inserted their PIV card into the card reader.
- ActivClient: The user’s PIV PIN was entered incorrectly.

A detailed overview of the login process from the user’s perspective is provided in the *AMPL GUI User Guide*. All project documentation is available on the AMPL GUI Product Repository on GitHub.

#### Logical and Physical Descriptions

The VAEC AWS is in one AWS GovCloud region with two Availability Zones. AMPL GUI does not disclose the physical address of its data centers.

<span id="_Toc194652454" class="anchor"></span>Figure 8: AWS GOV Cloud

![](ampl-production-operations-manual/009.png)

## Dependent System(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists the other VA systems upon which AMPL GUI depends.

| Dependency                                    | Type | Dependency Type | Purpose                                                                                                                                                                                |
|---------------------------------------------------|----------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Fast Healthcare Interoperability Resources (FHIR) | Service  | HL7/FHIR            | Mapped data will be provided via VDIF Enterprise Platform (EP) with the use of FHIR messages. Screens display the appropriate fields and map to the appropriate underlining source element |
| VDIF VCRS                                         | Service  | REST                | Provides data directly from VistA Instance                                                                                                                                                 |
| Clinical Context Objective Workgroup (CCOW)       | Service  |                     | Synchronizes AMPL GUI patient context with other clinical applications                                                                                                                     |
| IAM SSOi                                          | Service  |                     | Authentication and Authorization Security provider                                                                                                                                         |

<span id="_Toc191975502" class="anchor"></span>Table 7: System Recovery

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tier 1 troubleshooting for internal VA users is handled through the Enterprise Service Desk (ESD). Tier 2 issues are handled by the Clinical Ancillary Products (CAP) Team 1. Troubleshooting is handled directly by application developers.

## System Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections define the process and procedures necessary to restore the system to a fully operational state after a service interruption. Each of the subsections starts at a specific system state and ends up with a fully operational system.

All hardware, network, and physical infrastructure are the responsibility of AWS and are outside the scope of this document. Recovery priorities are determined based on the criticality to the solution, as well as the number of users impacted and risk for interruption to normal business processes. Detailed processes are provided in the *VAEC System High Availability and Recovery Plan.*

| IS Services (Application/IS Support Services)  | Recovery Priority |
|----------------------------------------------------|-----------------------|
| Authentication Services                            | 2                     |
| Server Configuration Management Service            | 3                     |
| Vulnerability Scanning Service                     | 4                     |
| Monitoring Service                                 | 5                     |
| Auditing Service                                   | 6                     |
| Code Configuration and Release Management Services | 7                     |

<span id="_Toc191975503" class="anchor"></span>Table 8: Operations and Maintenance Responsibilities

### Restart after Non-Scheduled System Interruption 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a power outage or other abrupt termination of the server operating systems, please refer to [System Startup from Emergency Shutdown](#_System_Start-Up_from) and [System Start-up](#system-start-up) for guidance.

### Restart after Database Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to [System Start-up](#system-start-up) for the system startup procedures.

### Back-out Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For back-out procedures, refer to the Deployment, Installation, Backout, and Rollback Guide (DIBRG).

### Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Rollback procedures, refer to the DIBRG.

# Operations and Maintenance Responsibilities 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Operations and Maintenance (O&M) Plan defines the operational support tasks and activities that each of the Office of Information & Technology (OI&T) functional areas are required to provide in the delivery and support of a production enterprise system. The O&M Plan defines specific roles and responsibilities of OI&T functional support teams to avoid confusion over which party is responsible for specific areas of process, tasks, or actions. The O&M plan supports the specific service levels for each activity as defined in the Service Level Agreement (SLA), describes how performance is measured, and identifies the entities responsible for each activity. 

All key functions are assigned to one or more responsible parties and activities are clearly defined to maintain and support the applications and system components throughout its life cycle. These roles and responsibilities are displayed in a tabular RACI format at the end of each section of the plan to further define Responsibility, Accountability, Consultation, and Information roles.

<table>
<caption><p><span id="_Toc61428630" class="anchor"></span>Table 9: Acronyms and Abbreviations</p></caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 28%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>Role and Brief Description</th>
<th>Assigned Organization (Pillar and Sub-office)</th>
<th>Contact Information</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Enterprise Service Desk (ESD) Tier 1: Provide first contact resolution via the Knowledge section retained in ServiceNow (IT Service Management) ITSM.</td>
<td>ITOPs (ESD)</td>
<td><p>855-NSD-HELP (855-673-</p>
<p>4357)</p></td>
</tr>
<tr class="even">
<td>Tier 2: Provides second level service provider functions, which include problem screening, definition, and resolution. Service requests that cannot be resolved at this level within a set period are elevated to appropriate service providers at the Tier 3 level.</td>
<td>CAP Team 1</td>
<td>Will be routed via ESD Tickets from NSD Tier 1 team.</td>
</tr>
<tr class="odd">
<td>Tier 3: Provides third level service provider functions, which primarily consist of problem identification, diagnosis, and resolution. Service requests that cannot be resolved at the Tier 2 level are typically referred to the Tier 3 for resolution.</td>
<td>AMPL GUI Development Team</td>
<td>Will be routed via ESD Tickets from AMPL GUI Development Team.</td>
</tr>
</tbody>
</table>

<span id="_Toc61428630" class="anchor"></span>Table 9: Acronyms and Abbreviations

[![](ampl-production-operations-manual/010.png) AMPL_GUI_RACI.xlsx](https://dvagov.sharepoint.com/:x:/r/sites/OITDSOSPMAMPLGUITEAM2/Shared%20Documents/AMPL%20CD2%20Release%20Documentation/AMPL_GUI_RACI.xlsx?d=w4c91ac7288d84bc8a59788bc2ca52c2a&csf=1&web=1&e=ec47nf&xsdata=MDV8MDJ8fGQ0N2RhZWIwYjVkYjRkYTE0NmE5MDhkZDllMjIwNjYxfGU5NWYxYjIzYWJhZjQ1ZWU4MjFkYjdhYjI1MWFiM2JmfDB8MHw2Mzg4NDA1OTExNjAzNzM3ODh8VW5rbm93bnxUV0ZwYkdac2IzZDhleUpGYlhCMGVVMWhjR2tpT25SeWRXVXNJbFlpT2lJd0xqQXVNREF3TUNJc0lsQWlPaUpYYVc0ek1pSXNJa0ZPSWpvaVRXRnBiQ0lzSWxkVUlqb3lmUT09fDB8fHw%3d&sdata=bVllWnhJWmVvaXc5N3g1S1BGWmZFclc3OGRIb0hxYVh6ZGFjMml0N2xzQT0%3d)

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists acronyms found in this document and provides definitions.

| Acronym  | Definition                                                      |
|----------|-----------------------------------------------------------------|
| AD       | Active Directory                                                |
| AMPL GUI | Advanced Medication Platform Graphical User Interface           |
| AWS      | Amazon Web Services                                             |
| CAP      | Clinical Ancillary Products                                     |
| CCOW     | Clinical Context Objective Workgroup                            |
| DIBRG    | Deployment, Installation, Back-out, and Rollback Guide          |
| EC2      | Elastic Compute Cloud                                           |
| EUO      | End-User Operations                                             |
| FHIR     | Fast Healthcare Interoperability Resource                       |
| HDR      | Health Data Repository                                          |
| IAM      | Identity and Access Management                                  |
| ICAM     | Identity, Credential, and Access Management                     |
| IOC      | Initial Operating Capability                                    |
| ITOPS    | IT Operations and Services                                      |
| MSR      | Monitoring Service Registry                                     |
| MPI      | Master Patient Index                                            |
| NARS     | Network Access Requests                                         |
| NCA      | National Cemetery Administration                                |
| O&M      | Operation and Maintenance                                       |
| OI&T     | Office of Information and Technology                            |
| RACI     | Responsibility, Accountability, Consultation, and Information   |
| SLA      | Service Level Agreement                                         |
| SNOW     | Service Now                                                     |
| SNS      | Amazon Simple Notification Service                              |
| SRE      | Site Reliability Engineers                                      |
| SSOi     | Single Sign-On Integration                                      |
| VA       | Department of Veterans Affairs                                  |
| VAEC     | VA Enterprise Cloud                                             |
| VBA      | Veterans Benefits Administration                                |
| VDIF     | Veterans Data Integration & Federation                          |
| VHA      | Veterans Health Administration                                  |
| VistA    | Veterans Health Information Systems and Technology Architecture |
| VPC      | Virtual Private Clouds                                          |

Acronyms and AbbreviationsThe table lists acronyms found in this document and provides definitions.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: AMPL Production Operations Manual (POM)

### System Shut-down

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To stop the ECS cluster running on EC2 instances there are 2 steps:

1.  Stop the ECS Cluster services and tasks.
2.  Stop the EC2 instances supporting the ECS Cluster.

#### Emergency System Shut-down

The emergency system shutdown procedure is to shut down all AMPL GUI servers in AWS. These servers may be shut down in any order so the instructions as seen in [System Shut-down](#system-shut-down) can be used.

### Back-up & Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI is created using an infrastructure as code methodology, therefore it is not necessary to create application server-level backups. The underlying infrastructure supporting the Container platform is created using archived scripts that are configuration managed within Veteran (VA) controlled source control.

#### Back-Up Procedures

Auto scheduled snapshots using Lifecycle Manager are utilized to create backup of instances once a week and are retained for three weeks.

<span id="_Toc162509878" class="anchor"></span>Figure 1: Lifecycle Manager

![](ampl-production-operations-manual-pom/002.png)

#### Restore Procedures

Please refer to [Section 2.1.3.3 Back-up Testing](#back-up-testing).

#### Back-Up Testing 

1\. From the Snapshots list, choose the snapshot to create the volume.

2\. Click the Actions button and select Create Volume.

<span id="_Toc162509879" class="anchor"></span>Figure 2: Actions Button

![](ampl-production-operations-manual-pom/003.png)

3\. Remember, for Availability Zone, choose the Availability Zone in which to create the volume.

> **NOTE:** EBS volumes can only be attached to EC2 instances in the same Availability Zone.

4\. Choose Create additional tags to add the approved VAEC tags to the volume. For each tag, provide a tag Key and a tag Value.

<span id="_Toc162509880" class="anchor"></span>Figure 3: Create Volume

![](ampl-production-operations-manual-pom/004.png)

5\. Choose Create Volume.

6\. After you've restored a volume from a snapshot, you can attach it to an instance to begin using it. To do so,

- Stop the instance.
- Detach the volume and attach the new volume.
- Start the instance.

<span id="_Toc162509881" class="anchor"></span>Figure 4: Create Volume Request Succeeded

![](ampl-production-operations-manual-pom/005.png)

7\. Connect to instance.

<span id="_Toc162509882" class="anchor"></span>Figure 5: Remote Desktop Connection

![](ampl-production-operations-manual-pom/006.png)

#### Storage and Rotation

Storage and rotation information is not applicable.

## System Monitoring, Reporting & Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes a high-level overview of the monitoring for the AMPL production environment.

### Dataflow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following figure depicts the AMPL GUI HealthShare Data Flow. Additional information can be found in the *AMPL GUI System Design Document.*

<span id="_Toc162509883" class="anchor"></span>Figure 6: Logical High Level AMPL GUI HealthShare Data Flow

![](ampl-production-operations-manual-pom/007.png)

### Availability Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Enterprise Cloud (VAEC) AWS GovCloud High is a General Support System that provides a secure application and hosting environment for VA applications, content, and utilities. These applications and services are used to deliver content to an audience made up of employees, Veterans, contractors, partners across all VA medical centers and component facilities, Federal government, and the general public. Content and applications are provided by Veterans Benefits Administration (VBA), Veterans Health Administration (VHA), National Cemetery Administration (NCA), and Support Offices. VAEC provides the following services: Content delivery, Application Hosting and Management Services.

The VAEC infrastructure is hosted by AWS GovCloud, a cloud service provider. The AWS GovCloud platform is used to provide a variety of hosting environments to suit a variety of needs. AWS GovCloud can support applications categorized up to High as rated in accordance with Federal Information Processing Standard (FIPS) 199. VA applications available to the public are hosted in AWS GovCloud.

A dedicated private data link (AWS Direct Connect) provides all connectivity for VA resources communicating to the environment. Virtual Private Clouds (VPC) wrap the applications within VAEC AWS GovCloud to encapsulate network access. Access from the applications to VA internal resources such as Identity, Credential, and Access Management (ICAM) and AD Services are conducted over the encrypted private data link to the VA network.

Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health. CloudWatch collects monitoring and operational data in the form of logs, metrics, and events, providing a unified view of AWS resources, applications, and services that run on AWS and on-premises servers. CloudWatch can be used to detect anomalous behavior in environments, set alarms, visualize logs and metrics side by side, take automated actions, troubleshoot issues, and discover insights to keep applications running smoothly.

Amazon Simple Notification services are in place to send alerts generated from CloudWatch. The figure below displays the notifications sent. The email notifications are sent to the topics subscribed.

<span id="_Toc162509884" class="anchor"></span>Figure 7: Amazon Simple Notification

![](ampl-production-operations-manual-pom/008.png)

### Performance/Capacity Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Performance monitoring is completed by reaching out to the Monitoring Service Registry (MSR) team and onboarded Dynatrace tool. Elastic Search is the mandatory tool for applications on the cloud.

[DynaTrace](https://cex678.dynatrace-managed.com/e/72874c19-c296-4b5f-86cd-a3ba91f5e8e2/#newhosts;gtf=-2h;gf=all), ScienceLogic and [OpenSearch](https://prod.adfs.federation.va.gov/adfs/ls/idpinitiatedsignon.aspx) are in place to address various monitoring requirements. These dashboards provide information about AWS service including the service and application health, uptime, and capacity planning. AWS Cloud Watch and Amazon Simple Notification Service (SNS) notification services are also in place for monitoring and alerting. Reports can be obtained by contacting the POC in Table 4.

| Tool         | POC                   | Email Address                                                                                        |
|--------------|-----------------------|------------------------------------------------------------------------------------------------------|
| DynaTrace    | Jennifer Jeffress     | Jennifer.Jeffress@va.gov                                                                             |
| ScienceLogic | Iran Reynolds         | <Iran.Reynolds@va.gov>                                                                               |
| OpenSearch   | Nicholas Owusu-Sampah | [Nicholas.Owusu-Sampah@va.gov](file:///C:/Users/vhaorlslaugp/Downloads/Nicholas.Owusu-Sampah@va.gov) |

<span id="_Toc162509874" class="anchor"></span>Table 5: Initial Capacity Plan

### Critical Metrics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The critical metrics captured for AMPL GUI are covered in [Section 2.4.3: Performance/Capacity Monitoring.](#_Performance/Capacity_Monitoring)

## Routine Updates, Extracts and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI does not maintain or store any data. The AMPL GUI application solely uses VDIF services for patient and pharmacy data retrieval. Therefore, the system does not implement or require any data updates, extracts or purges.

### Time-outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Time out may occur when accessing the VDIF system. Occasionally queries are dependent upon the availability of VDIF or run out of time if a large results query is requested.
