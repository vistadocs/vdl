---
consolidated_title: "pecs troubleshooting guide"
app_code: PECS
doc_type: SUP
master_source: "PECS Version 6.2 Troubleshooting Guide (PREC*6.2*3)"
master_pub_date: April 2022
consolidated_from: 2 versions
prior_versions:
  - "PREC*7*1 PECS Troubleshooting Guide"
---

---
title: |
  Pharmacy Enterprise Customization System (PECS)

  Troubleshooting Guide

  ![](pecs-version-6-2-troubleshooting-guide-prec-6-2-3/001.png)
---

April 2022

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Development (PD)

Revision History

When updates occur, the Title Page lists the new revised date and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

Refer to the SOFTWARE library version of this document to view <span class="mark">REDACTED</span> information.

<table>
<caption><p><span id="_Ref75527746" class="anchor"></span>Table 1: WebLogic Application Server</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revised Pages</th>
<th>Patch Number</th>
<th>Change Reference</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>04/11/2022</td>
<td>Title, i, iv, vi, vii, 5, 8, and 25</td>
<td>PREC*6.2*3</td>
<td><ul>
<li><p>Updated WebLogic version number to 12.2.1.4 in <strong><u>Table 1</u></strong></p></li>
<li><p>Updated the Log4j version number to 2.17.1 and WebLogic version number to 12.2.1.4 in section <strong><u>2.4 Software Description</u></strong></p></li>
<li><p>Updated Log location in section <strong><u>4.2.1 Application Error Logs</u></strong></p></li>
<li><p>Updated Title page, Revision History, Table of Contents, List of Tables, List of Figures, and Footers</p></li>
</ul></td>
</tr>
<tr class="even">
<td>6/30/2021</td>
<td>Title, i, v, 5, 6, 8, and all</td>
<td>PREC*6.2*1</td>
<td><ul>
<li><p>i: Added description above the <strong>Revision History</strong> table</p></li>
<li><p>v: Formatted tables to appear in the <strong><u>List of Tables</u></strong></p></li>
<li><p>5: Updated <strong><u>Figure 2</u></strong></p></li>
<li><p>6: Updated WebLogic in <strong><u>Table 1</u></strong></p></li>
<li><p>8: Updated WebLogic, Spring, and Log4j in <strong><u>Table 3</u></strong></p></li>
<li><p>See the non-redacted prec_6_2_p1_tg on the SOFTWARE library for viewing <mark>REDACTED</mark> information</p></li>
</ul>
<p>Liberty ITS</p></td>
</tr>
<tr class="odd">
<td>07/12/2017</td>
<td>All</td>
<td>PREC*6.1*1</td>
<td><p>Made updates for PECS v6.1 which addresses 2FA Compliance and IAM SSOi intergration for PIV authentication.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>03/22/2016</td>
<td><p>22</p>
<p>All</p></td>
<td>PREC*6.0*1</td>
<td><p>Update emails in section 3.3</p>
<p>508 conformance edit - <mark>REDACTED</mark></p>
<p>Updated for PECS v6.0.01 - <mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/06/2014</td>
<td>All</td>
<td>PREC*5.0*1</td>
<td><p>Updated for PECS v5.0</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/18/2014</td>
<td>All</td>
<td>PREC*3.0*1</td>
<td><p>Updated Title Page</p>
<p>Changed date to be date (month) of release.</p>
<p>Added footnote describing relationship between FDB MedKnowledge Framework and FDB-DIF, updated text appropriately. Updated TOC.</p>
<p>Fixed Revision History Format; fixed for Section 508 compliance</p>
<p>Changed title page and footers to reflect the actual release month/year. Changed footers in Revision History section</p>
<p>General edits (section 3.0), other Tech Writing edits</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/06/2013</td>
<td>9, 13, 29, 43, all</td>
<td>PREC*3.0*1</td>
<td><p>Updated Footer, All Pages</p>
<p>Updated Revision History formatting, content</p>
<p>Corrected grammar on Page 9</p>
<p>Revised introductory text on Page 13</p>
<p>Removed extra space on Page 29</p>
<p>Removed extra space on Page 43</p>
<p>Corrected inconsistency in use of the phrase ‘Where X…’ throughout document</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/06/2013</td>
<td>33-37</td>
<td>PREC*3.0*1</td>
<td><p>Edited items in sections 5.1.2.1 and 5.1.4.1.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/01/2013</td>
<td>31-46</td>
<td>PREC*3.0*1</td>
<td><p>Updated document for PECS v3.0. Updated the messages in the Dose Range, Drug Pairs, Duplicate Therapy and Professional Monograph sections.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/13/2012</td>
<td>All; 3, 8, 9, TOC</td>
<td>PREC*2.2*1</td>
<td><p>Performed general edits; replaced figures 1 (page 3), 3 (page 8), and 4 (page 9) to match System Design Document; updated TOC.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/23/2012</td>
<td>37-48</td>
<td>PREC*2.2*1</td>
<td><p>Updated document for PECS v2.2. Updated the messages in the Single Drug Pairs, DDI, Drug Pairs Customization and Dose Range sections. Added the Record Locking section. Deleted the "user clicked the Customize button" statements from the Single Drug Pairs section.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/16/2011</td>
<td>All</td>
<td>N/A, First Release</td>
<td><p>Finalized Document</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/16/2011</td>
<td>All</td>
<td>N/A, First Release</td>
<td><p>Updated Various Sections</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/04/2011</td>
<td>All</td>
<td>N/A, First Release</td>
<td><p>Initial Draft</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

<span id="_Ref75527746" class="anchor"></span>Table 1: WebLogic Application Server

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Summary](#summary)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [System Business and Operational Description](#system-business-and-operational-description)
  - [Operational Priority and Service Level](#operational-priority-and-service-level)
  - [Logical System Description](#logical-system-description)
    - [Presentation Tier Overview](#presentation-tier-overview)
    - [Business Logic Tier Overview](#business-logic-tier-overview)
    - [Data Persistence Tier Overview](#data-persistence-tier-overview)
    - [DATUP DIF Update Logical System Components](#datup-dif-update-logical-system-components)
  - [Physical System Description](#physical-system-description)
  - [Software Description](#software-description)
    - [Background Processes](#background-processes)
    - [Job Schedules](#job-schedules)
  - [Dependent Systems](#dependent-systems)
- [Routine Operations](#routine-operations)
  - [Administrative Procedures](#administrative-procedures)
    - [System Start-up](#system-start-up)
    - [System Shut-down](#system-shut-down)
    - [Backup & Restore](#backup-restore)
  - [Security / Identity Management](#security-identity-management)
    - [Identity Management](#identity-management)
    - [Access Control](#access-control)
  - [User Notifications](#user-notifications)
  - [System Monitoring, Reporting, & Tools](#system-monitoring-reporting-tools)
    - [Availability Monitoring](#availability-monitoring)
    - [Performance/Capacity Monitoring](#performancecapacity-monitoring)
  - [Routine Updates, Extracts and Purges](#routine-updates-extracts-and-purges)
  - [Scheduled Maintenance](#scheduled-maintenance)
  - [Capacity Planning](#capacity-planning)
    - [Initial Capacity Plan](#initial-capacity-plan)
- [Exception Handling](#exception-handling)
  - [Routine Errors](#routine-errors)
    - [Security](#security)
    - [Time-outs](#time-outs)
    - [Concurrency](#concurrency)
  - [Significant Errors](#significant-errors)
    - [Application Error Logs](#application-error-logs)
- [Application Error Messages and Descriptions](#application-error-messages-and-descriptions)
  - [Customization Messages](#customization-messages)
    - [All Concepts Messages](#all-concepts-messages)
    - [Dose Range Messages](#dose-range-messages)
    - [Drug-Drug Interaction Messages](#drug-drug-interaction-messages)
    - [Drug Pair Messages](#drug-pair-messages)
    - [Duplicate Therapy Messages](#duplicate-therapy-messages)
    - [Professional Monograph Messages](#professional-monograph-messages)
  - [Custom Update Messages](#custom-update-messages)
  - [Query Pages Messages](#query-pages-messages)
  - [Record Locking Messages](#record-locking-messages)
  - [Reports Pages Messages](#reports-pages-messages)
- [Infrastructure Errors](#infrastructure-errors)
  - [Database](#database)
  - [Web Server](#web-server)
  - [Application Server](#application-server)
  - [Network](#network)
  - [Authentication and Authorization](#authentication-and-authorization)
    - [User SSOi Logout](#user-ssoi-logout)
  - [Dependent System(s)](#dependent-systems-1)
- [System Recovery](#system-recovery)
  - [Restart After Non-Scheduled System Interruption](#restart-after-non-scheduled-system-interruption)

## Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS Troubleshooting Guide is written to be a supplement to any Operations Manual that is provided for the support staff, whether it be Field Operations, Enterprise Applications Management (or whatever team is in place after the product is in production), or the development team that needs to initially support the product.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to list the error messages that any user may come across in the application. Some of the messages require that support staff be notified, and these are noted.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This scope of this document is limited to the PECS application. Any references to external systems are only for describing an interface and how the interface and that system affect the operation of PECS. The external system may also act as a tool to be used as part of system monitoring or the support and issue resolution system.

# System Business and Operational Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS is a Graphical User Interface (GUI) application used to research, review, report, and manage customization changes currently within five First Data Bank (FDB) MedKnowledge[^1] custom tables. The tables are Drug interaction, Drug Pairs, Drug Dosing, Duplicate Therapy, and Professional Monograph. The data changes performed for customizations are specific to VA patient care. The changes are different then what the vendor has provided, such as, the drug severity of two drugs. The change affects the information presented to the pharmacist when a drug order check is ordered on a patient.

The Pharmacy Benefits Management group (PBM) is the primary business owners of the application. They are responsible in overseeing customized changes that are necessary for overriding data table updates supplied weekly by FDB.

## Operational Priority and Service Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Service Level of the system and the availability of the system are described in the Rough Order of Magnitude (ROM). The ROM provides information for the set up and support of the Pharmacy Re-Engineering (PRE) PECS application at ITC-Austin TX and the Identity and Access Management (IAM) Single Sign On internal (SSOi) system. No formal SLA is available for the PECS application.

## Logical System Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The logical view describes the architecturally significant parts of the design model. The object-oriented decomposition of the PECS application can be logically divided into three primary tiers: Presentation Tier, Business Logic Tier, and Data Persistence Tier. Each tier has its own design and implementation framework and defined points of interaction with the other respective tiers.

The PECS application is a web-based application accessible only from within the VA network via a client workstation with a VA approved Internet browser. The PECS application’s architecture is designed and implemented according to VA architecture requirements using Java Platform Enterprise Edition (JEE) framework.

### Presentation Tier Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The presentation tier represents the GUI screens that allow the user to interact with the application and the logic initiated by user interaction to execute screen functionality. The presentation tier uses a well-known Model-View-Controller (MVC) design pattern implemented by the Spring MVC framework using JEE Java Server Pages (JSP) as the “View” portion of MVC. The MVC framework is used to manage the display screens and to dispatch and delegate requests initiated by the user to a business rule processing the business logic tier. The design of the MVC framework as it is used in the PECS application leverages an object hierarchy with commonly shared base classes.

### Business Logic Tier Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The business logic tier is responsible for receiving business rule processing requests from the presentation tier, or other parts of the business logic tier. It is composed of services implemented as Spring beans. Transactional integrity is ensured by using Spring managed transactions.

The main services implemented deal with creation/modification/deletion of customization requests, workflows, queries and custom update generations.

The services encapsulate the business rules governing the creation/modification/deletion of customization requests and their workflow. The services are also responsible for interfacing and abstracting the data persistence tier from the rest of the application logic.

### Data Persistence Tier Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data persistence tier is designed and implemented with the open source Hibernate framework. The Hibernate framework is an object-oriented abstraction for the database operations create, read, update, and delete (CRUD). For more information please refer to the Hibernate website.

The data persistence tier interfaces with two logical Oracle databases. The first is the PECS database containing the tables and database objects necessary for the PECS application to perform Order Check customizations and track workflow status. The second is the FDB MedKnowledge database, which is the source of production Order Check data. The relevant tables in each of these databases have representative domain model objects and data access objects (DAOs) in the data persistence design.

<span id="PREC_2_2_1_F1_PECS_Logical_System" class="anchor"></span>Figure 1: PECS Logical System Overview

![](pecs-version-6-2-troubleshooting-guide-prec-6-2-3/002.png)

### DATUP DIF Update Logical System Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The logical system description defines the FDB-Data Information Framework (DIF) Update Data Update (DATUP) and PECS system components. The components are shown together because they combine to form a common goal – FDB-DIF and FDB-Custom update distribution.

The combined logical system components are:

- FDB-DIF Update DATUP – Implements the FDB-DIF update business logic.
- Scheduler – Background process for scheduling Droid.
- WebLogic – Application server environment.
- Configuration File – Defines the DATUP configuration settings.
- Email Templates – Template emails for notifications sent to National/Local Managers.
- Secure File Transfer Protocol (SFTP) Server – SFTP Server that hosts the FDB-DIF update archives.
- Email Server – Email relay server.
- PECS – Implements the FDB-Custom drug business logic.
- Custom Table (CT) Staging Database – Stores PECS FDB-Custom modifications.
- DATUP Database – Stores DATUP site update history.
- FDB-DIF Database – Stores the FDB-DIF drug database.

The logical system components for the National and Local environments are illustrated below. The National components are responsible for verifying and publishing FDB-DIF and FDB-Custom updates to the SFTP Server. The Local components then consume and apply the verified updates in an automated manner.

<span id="_Ref75527734" class="anchor"></span>Figure 2: Logical System Components for the National and Local Environments

![](pecs-version-6-2-troubleshooting-guide-prec-6-2-3/003.png)

## Physical System Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS is a national deployment at the Austin Information Technology Center (AITC). There is no disaster recovery site at AITC. The PECS application’s components are deployed on two servers: an application server (WebLogic) and a database server (Oracle). These server’s characteristics are described in more detail below.

| Parameter                 | Value                                                              |
|---------------------------|--------------------------------------------------------------------|
| Central Processing Unit   | 2 CPU, x86 architecture (Intel x86 or equivalent), 2 GHz or faster |
| RAM                       | 8 GB                                                               |
| Available Hard Disk Space | 70 GB                                                              |
| RAID Configuration        | RAID 1                                                             |
| Operating System          | Red Hat Linux – Enterprise Edition Version 6.8                     |
| Mouse                     | Generic                                                            |
| Video Resolution          | 640 x 480 pixels                                                   |
| Network Interface         | dual 10 Base T or higher                                           |
| Software                  | WebLogic 12.2.1.4                                                  |

<span id="_Toc347930610" class="anchor"></span>Table 2: Oracle Database Server

| Parameter                 | Value                                                               |
|---------------------------|---------------------------------------------------------------------|
| Central Processing Unit   | 4 CPU, i386 architecture (Intel 386 or equivalent), 2 GHz or faster |
| RAM                       | 16 GB                                                               |
| Available Hard Disk Space | 150 GB                                                              |
| RAID Configuration        | RAID 1                                                              |
| Operating System          | Red Hat Linux v 6.8                                                 |
| Mouse                     | Generic                                                             |
| Video Resolution          | 640 x 480 pixels                                                    |
| Network Interface         | dual 10 Base T or higher                                            |
| Fiber Channel Interface   | dual Host Bus Adapters                                              |
| Database                  | Oracle 11g                                                          |

<span id="_Ref75527753" class="anchor"></span>Table 3: Software Components for the FDB-DIF Update DATUP

PECS is deployed at the national level as a single application server node connected to a database server.

<span id="PREC_2_2_1_F3_PECS_Deployment" class="anchor"></span>Figure 3: PECS Deployment

![](pecs-version-6-2-troubleshooting-guide-prec-6-2-3/004.png)

<span id="PREC_2_2_1_F3_PECS_DeploymentCont" class="anchor"></span>Figure 4: PECS Deployment, Continued

![](pecs-version-6-2-troubleshooting-guide-prec-6-2-3/005.png)

## Software Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS application conforms to the VA’s requirements determining the use of third-party tools. Please refer to the PECS Product Architecture Document for reference. See the non-redacted version of this document on the SOFTWARE library for the PECS TSPR site: <span class="mark">REDACTED</span>

The three-tiered architecture consists of an Internet browser-based graphical user interface accessing a Spring MVC-based web application/presentation tier, a Java Enterprise Edition (JEE)-based business logic service processing layer, and a Hibernate-based data access tier. These conform to the design recommended by the Health Systems Design & Development (HSD&D) Core Specifications for Re-hosting Initiatives and generally acceptable JEE implementation recommendations.

PECS is a JEE application, conforming to version 1.4 of the specification. It is deployed on WebLogic 12.2.1.4. It makes use of the following third-party frameworks: Spring 4.2.9, Hibernate 5.1.1, and log4j-api-2.17.1. As mandated by the VA, PECS is integrated with Identity and Access Management (IAM) Single Sign On internal (SSOi) to support two factor authentication (2FA) using Personal Identity Verification (PIV).

| Component Name         | Vendor       | Version | License                    | Configuration                         |
|------------------------|--------------|---------|----------------------------|---------------------------------------|
| Operating System       | Redhat       |         |                            | Standard                              |
| National Database      | Oracle       |         |                            | See PECS Installation Guide.          |
| Local Database         | Intersystems |         |                            | See MOCHA Server Installation Guide.  |
| Programming Language   | Oracle       | 6       | Oracle Binary Code License | Standard                              |
| WebLogic               | Oracle       |         |                            | See PECS Installation Guide.          |
| Java Messaging Service | Oracle       |         |                            | See DATUP Installation Guide.         |
| CommonJ Scheduler      | Oracle       |         |                            | See PECS & DATUP Installation Guides. |
| SFTP Server            | Apache       |         |                            | Standard                              |
| Email Server           | Microsoft    |         |                            | Open relay                            |

<span id="_Toc347930612" class="anchor"></span>Table 4: System Automation Dependencies

### Background Processes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several background processes that run on the PECS production and pre-production servers daily.

At 7:00 a.m., a job runs to alert Database Administrators (DBA)s to service accounts with passwords that will expire in the next 15 days.

Also, at 7:00 a.m., a job runs to purge trace files and log files older than a set parameter.

At 5:00 a.m., a job runs to move audit logs that need to be kept longer to a more permanent location.

At 6:00 a.m., a job runs to move old alert logs to a backup directory and start a new log for each day making troubleshooting and maintenance easier while freeing up space for customer data.

At 11:00 p.m., a job runs to gather statistics on each table, which are used by the Oracle optimizer, to choose data access paths for peak performance.

Weekly, a job runs on Sunday to monitor space usage and allow DBAs and system administrators to do capacity planning.

Weekly, job runs on Thursdays to verify/monitor privileges held by users for security and DBA review.

Backup jobs that run in the background are described in section 3.4.

- Oracle for managing the table
- DATUP Background Process
- PECS Background Process

The CommonJ Scheduler also runs in the background. It maintains the update schedule and fires after the configured timer has expired.

### Job Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the job scheduling for DATUP and PECS.

#### DATUP

Once per day at a configured time the DATUP automated application schedules the execution of the FDB-DIF update process. Whether successful or unsuccessful, the process will execute again on the following day.

An automated process checks for daily updates to be applied to the PECS application. The updates are processed by an automatic scheduler that checks for available files in the *Anonymous* directory. The files may be an FDB-DIF zip file supplied weekly by FDB or PECS customization changes in zip file format provided when necessary by the Release Manager within PECS. The automated process checks for updates, applies the updates, verifies completion or failure of normal executions, sends email messages, and moves files when completed.

#### PECS

PECS v6.2 introduced a background process that generates FDB Comparison Reports based upon the FDB-DIF Incremental Update file that has been received. This process needs to execute before the automated DATUP process described above.

The FDB Comparison Reports will read the incoming FDB Incremental Update file as well as the data from the FDB Database. If the concept has been customized, then a comparison of the new FDB data, existing FDB data, and customized data is produced.

## Dependent Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS depends on IAM SSOi for user authentication where user authorization and roles are managed within the PECS application.

<span id="_Toc100128390" class="anchor"></span>Figure 5: Dependent System

![](pecs-version-6-2-troubleshooting-guide-prec-6-2-3/006.png)

| Dependency Name            | Location                    | Function                                                  | Interface Method             |
|----------------------------|-----------------------------|-----------------------------------------------------------|------------------------------|
| FTP Server over SSH (SFTP) | VA Internal                 | Stores FDB-DIF and FDB-Custom archives (ZIP files).       | FTP Protocol over SSH (SFTP) |
| Email Server               | VA Internal                 | Transmits notification email to configured mailing lists. | SMTP Protocol                |
| Java Messages Service      | WebLogic Application Server | Transmits messages from Local Sites to National.          | JMS Protocol                 |
| IAM SSOi                   | VA Internal                 | Security                                                  | WEB                          |
| CMOP                       | CMOP                        | Transmit FDB DIF full and incremental zip files           | FTP Protocol over SSH (SFTP) |

<span id="_Toc347930613" class="anchor"></span>Table 5: WebLogic Pre-Prod Steps

# Routine Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS requires Oracle support for the FDB-DIF and CT staging tables by a DBA. It also requires the understanding of Linux and WebLogic.

## Administrative Procedures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### System Start-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The servers are brought online by applying appropriate power and pressing the power button. Once the operating system is loaded and the server is accessible, the DBA is advised and will bring the database online. Once the database is online, the application admin is advised and will bring the application online.

If the server is up and the database is down, the script on the database server, vapredbs1, in the directory, /u01/oracle/admin/PREP/scripts, is a startup script which can be run by the Oracle Unix user to start up any database on the server. It is called from that directory as ./startup_db.ksh \<database_name\>, i.e., ./startup_db.ksh PREP.

| Name                        | Directory/Path                                                    |
|-----------------------------|-------------------------------------------------------------------|
| WebLogic Install Directory  | /u01/app/bea                                                      |
| Domain Directory            | /u01/app /bea/user_projects/domains/ pecs-preprod                 |
| Admin Server Startup Script | /u01/app /bea/user_projects/domains/pecs-preprod/startWebLogic.sh |
| Node Manager Startup Script | /u01/app /bea/wlserver_10.3/server/bin/startNodeManager.sh        |
| Managed Server Startup      | From Admin Console: pecs_ms1, peps_ms1                            |

<span id="_Toc347930614" class="anchor"></span>Table 6: WebLogic Production Steps

| Name                        | Directory/Path                                                |     |
|-----------------------------|---------------------------------------------------------------|-----|
| WebLogic Install Directory  | /u01/app /bea                                                 |     |
| Domain Directory            | /u01/app /bea/user_projects/domains/pecs-prod                 |     |
| Admin Server Startup Script | /u01/app/bea/user_projects/domains/pecs-prod/startWebLogic.sh |     |
| Node Manager Startup Script | /u01/app /bea/wlserver_10.3/server/bin/startNodeManager.sh    |     |
| Managed Server Startup      | From Admin Console: pecs_ms1, peps_ms1                        |     |

<span id="_Toc347930616" class="anchor"></span>Table 7: Menu Tab

1.  Login to the server as your user and become the WebLogic user:

    *sudo su - weblogic*
2.  See the previous table to identify the script you wish to run for starting the Admin Server or a Node Manager. When running a script, preface all startup scripts with the *nohup* command and place in the background.
    - Starting the Admin Server

      *cd /u01/appbea/user_projects/domains/pecs-\

      *nohup ./startWebLogic.sh &*
    - Starting a Node Manager

      *cd /u01/app/bea/wlserver_10.3/server/binnohup ./startNodeManager.sh &*
3.  Login to the WebLogic GUI Admin console with your LAN ID, if this does not work, check the Password Vault for the environment and use the specified account.
4.  Start the requested Managed Servers.

### System Shut-down

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application admin takes the application offline and advises the team. The DBA takes the database offline and advises the team. The server admin will run “ps –ef” to identify any hung WebLogic or Oracle processes prior to shutdown/reboot of the servers.

If the server and database are up but need to come down for maintenance for either one, then the script on the database server, vapredbs1, in the directory, /u01/oracle/admin/PREP/scripts, is a shutdown\_ script which can be run by the Oracle Unix user to shut down any database on the server. It is called from that directory as ./shutdown_db.ksh \<database_name\>, i.e., ./shutdown_db.ksh PREP.

1.  Login to the WebLogic GUI Admin console with your LAN ID, if this does not work, check the Password Vault for the environment and use the specified account.
    - Select all the servers including Admin server and shut them down.
5.  Login to the server as your user and become the WebLogic user:
    - sudo su – weblogic

      Kill \<nodemanager PID\>
6.  Verify if all the servers are stopped.
    -  ps –ef \| grep java, you should not see any WebLogic instances.

### Backup & Restore 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this section, a high-level description of the systems back-up and restore strategy is elaborated.

#### Backup Procedures

All servers are backed up under the AITC Enterprise Backup solution.

The PRE servers backup policy are as follow;

- Differentials run Mon-Thurs – three-week retention.
- Full back up run on Fridays – three-month retention

host vapredbs1-b: vapredbs1-

===============================================================================

Running Command: bpcoverage -c vapredbs1-b -coverage -no_cov_header

CLIENT: vapredbs1-b

Mount Point Device Backed Up By Policy Notes

----------- ------ ------------------- -----

/ /dev/mapper/rootvg-root PRE_prd_sys

/ /dev/mapper/rootvg-root \*PRE_prd_ays

/boot /dev/sda1 PRE_prd_sys

/boot /dev/sda1 \*PRE_prd_ays

/dev/pts devpts UNCOVERED

/home /dev/mapper/rootvg-home PRE_prd_sys

/home /dev/mapper/rootvg-home \*PRE_prd_ays

/opt /dev/mapper/rootvg-opt PRE_prd_sys

/opt /dev/mapper/rootvg-opt \*PRE_prd_ays

/proc/sys/fs/binfmt_misc none UNCOVERED

/sys sysfs UNCOVERED

/u01 /dev/mapper/rootvg-u01 PRE_prd_sys

/u01 /dev/mapper/rootvg-u01 \*PRE_prd_ays

/u02 /dev/mapper/VG01-u02 UNCOVERED

/u03 /dev/mapper/VG01-u03 UNCOVERED

/u04 /dev/mapper/VG01-u04 UNCOVERED

/u05 /dev/mapper/VG01-u05 UNCOVERED

/u06 /dev/mapper/VG01-u06 UNCOVERED

/u07 /dev/mapper/VG01-u07 UNCOVERED

/usr /dev/mapper/rootvg-usr PRE_prd_sys

/usr /dev/mapper/rootvg-usr \*PRE_prd_ays

/var /dev/mapper/rootvg-var PRE_prd_sys

/var /dev/mapper/rootvg-var \*PRE_prd_ays

Working on vapredbs1 now!

===============================================================================

Checking status of latest backup run:

-------------------------------------------------------------------------------

Backups from last 24 hours:

/net/work/bpjobs/bpjobs.linux.bsh: kill: (8134) - No such pid

STATUS CLIENT POLICY SCHED SERVER TIME COMPLETED

0 vapredbs1-b RMAN PRE_1mo vaaacbck7-b 07/11/2010 05:05:44

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Running Command: ping -s vapreapp1-b 56 3

----vapreapp1-b PING Statistics----

3 packets transmitted, 3 packets received, 0% packet loss

round-trip (ms) min/avg/max = 0/0/2

===============================================================================

Running Command: bpclntcmd -hn vapreapp1-b

host vapreapp1-b: vapreapp1-b

===============================================================================

Running Command: bpcoverage -c vapreapp1-b -coverage -no_cov_header

CLIENT: vapreapp1-b

Mount Point Device Backed Up By Policy Notes

----------- ------ ------------------- -----

/ /dev/mapper/rootvg-root PRE_prd_sys

/ /dev/mapper/rootvg-root \*PRE_prd_ays

/boot /dev/sda1 PRE_prd_sys

/boot /dev/sda1 \*PRE_prd_ays

/dev/pts devpts UNCOVERED

/home /dev/mapper/rootvg-home PRE_prd_sys

/home /dev/mapper/rootvg-home \*PRE_prd_ays

/opt /dev/mapper/rootvg-opt PRE_prd_sys

/opt /dev/mapper/rootvg-opt \*PRE_prd_ays

/proc/sys/fs/binfmt_misc none UNCOVERED

/sys sysfs UNCOVERED

/u01 /dev/mapper/rootvg-u01 PRE_prd_sys

/u01 /dev/mapper/rootvg-u01 \*PRE_prd_ays

/usr /dev/mapper/rootvg-usr PRE_prd_sys

/usr /dev/mapper/rootvg-usr \*PRE_prd_ays

/var /dev/mapper/rootvg-var PRE_prd_sys

/var /dev/mapper/rootvg-var \*PRE_prd_ays

The database server, vapredbs1, has a system backup performed each weekend to tape and the tapes are retained for a month.

Oracle Recovery Manager (RMAN) software is used to perform full backups of the PREP database each morning on Tuesday and Saturday. The tapes are retained offsite for one month. RMAN is also used to back up the database control file and archive logs to tape daily, which are retained offsite for one month. The full database backups run for about 40-45 minutes. The archive log backups are shorter at about 25-30 minutes.

#### Restore Procedures

#### Recover Disk Layout and OS Version 

1.  Refer to one of the following for a filesystem layout:
    - [cfg2html reports](http://vaaacmul11.aac.va.gov/cfg2html/)
    - Filesystem report stored in /opt/ops/hosts.reports/\<hostname\>.fs.txt on <span class="mark">REDACTED</span>
    - Restore /opt/ops/\<hostname\>.fs.txt to /tmp/ on <span class="mark">REDACTED</span>
7.  Refer to one of the following to determine which RedHat version to install:
    - [cfg2html reports](http://vaaacmul11.aac.va.gov/cfg2html/)
    - Cfg2html output stored in /opt/cfg2html on <span class="mark">REDACTED</span>
    - RedHat release report stored in /opt/ops/hosts.reports/\<hostname\>.release.txt on <span class="mark">REDACTED</span>
    - Restore /etc/redhat-release to /tmp/ on <span class="mark">REDACTED</span>
8.  Build server using STK image server
    - [STK image server](http://vaaacmul13.aac.va.gov/KickStart/)
9.  Install Netbackup client
    - [NetBackup Client setup document](http://vaaacmul11.aac.va.gov/docs/netbackup.client.setup.txt)

#### Rebuild User Accounts

1.  Request NetBackup administrator to restore following files:
    - /home
    - /etc/passwd
    - /etc/shadow
    - /etc/group
    - /etc/gshadow
10. Run pwck to verify password files
11. Run grpck to verify group file

#### Restore Customized Configuration Files and User Directories

1.  Request NetBackup administrator to restore following files/directories:
    - /etc/snmp/snmpd/conf
    - /etc/at.allow
    - /etc/at.deny
    - /etc/cron.allow
    - /etc/cron.deny
    - /etc/hosts
    - /etc/sudoers
    - /etc/security/limits.conf
    - /etc/yum.conf
    - /etc/aliases
    - /etc/hosts.allow
    - /etc/hosts.deny
    - /etc/httpd
    - /etc/sysctl.conf
    - /etc/syslog.conf
    - /opt/ops/acct
    - /opt/ops/bin
    - /etc/cron.daily/passwd_age
    - /etc/cron.monthly/SecurityCheck
    - /usr/local/bin
    - /usr/local/nagios
    - /etc/logrotate.d
    - /etc/logrotate.conf
    - /etc/ntp
    - /etc/ntp.conf
    - /etc/multipath.conf
    - /u0x
    - /var/spool/cron
12. Restart following services:
    - snmpd
    - sendmail
    - httpd
    - syslog
    - nptd
    - multipathd

#### Install 3rd Party Software

Once the server, vapredbs1, /etc, /var, /u01, and Oracle software are restored from tape, the database can be restored using RMAN. The script to do this should have been restored to the /u01/oracle/admin/PREP/rman directory and is called rman_restore_db_from_tape.ksh. It must be run as the Oracle Unix user with the latest full backup of the database in the tape device and the database name as a parameter.

#### Backup Testing

At the Program Manager’s discretion random files can be selected and restored to an alternate location. Currently, there is no restore testing. The DBA team has requested an extra server to be used for this purpose and will implement testing procedures when this server is purchased by AITC.

#### Storage and Rotation

Full Backups are performed on Sundays and are kept for one month. This means that at any time, there exists four full backup tapes available for each server. Tapes are normally dispatched offsite on Mondays.

Differentials are run for the remainder of the week to capture daily changes and are sent offsite on Mondays.

These are the files that are stored as backup on vapredbs1:

- /
- /boot
- /home
- /opt
- /usr
- /var
- /u01

Schedule:

- Diff Mon-Thurs three-week retention
- Full Fri three-month retention

## Security / Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security used is – IAM SSOi.

The PECS application is only accessible by users signed directly into the VA network, or by users signed into the VA network via the RESCUE client. User authentication into the VA network is a precondition of PECS application access. Application authentication will be controlled by IAM SSOi using the user PIV card. In order to log into the application, each user must have a PIV or Windows credentials.

<span id="_Toc100128391" class="anchor"></span>Figure 6: SSOi Central Login Page

![](pecs-version-6-2-troubleshooting-guide-prec-6-2-3/007.png)

### Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VA users can login into the PECS application using their PIV. Identity Management is done through IAM SSOi.

Authorization is handled by the PECS application using the Database tables. All users will have the default Requestor role. For higher roles like Approver, Release Manager, and Administrator, users must contact the PBM National Drug File (NDF) managers.

### Access Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user must login with the PIV or Windows credentials at the SSOi login page. The user is authenticated by the IAM SSOi system against the VA Active Directory. The IAM SSOi system will authenticate the user and, if valid, allow the user access to the PECS application.

Within the PECS application, if the user session times out, then the user will be redirected to the SSOi central login page. After successful login, the confidentiality statement will be shown to the user. The user will be redirected to the application home page once the confidentiality statement is accepted. The confidentiality statement must be accepted at least once per user session.

A user’s role will determine the screens and operations that will be accessible. The tables below details presents a security the matrix.

| Screen Page                  | Requester | Approver | Release Manager | Administrator |
|------------------------------|-----------|----------|-----------------|---------------|
| Home                         | X         | X        | X               | X             |
| Advanced Query/Customization | X         | X        | X               | X             |
| Drug Pair Lookup             | X         | X        |                 |               |
| Administration               |           |          |                 | X             |
| Reports                      |           | X        |                 | X             |
| Custom Updates               |           |          | X               |               |
| Help                         | X         | X        | X               | X             |
| Contact Us                   | X         | X        | X               | X             |

<span id="_Toc100128360" class="anchor"></span>Table 8: Home Page

| Name                              | Type  | Requester | Approver | Release Manager | Administrator |
|-----------------------------------|-------|-----------|----------|-----------------|---------------|
| My Request History                | Panel | X         | X        |                 |               |
| My Assigned Requests for Review   | Panel |           | X        |                 |               |
| My Assigned Requests for Approval | Panel |           | X        |                 |               |
| My Assigned Requests for Deletion | Panel |           | X        |                 |               |
| Unassigned Requests               | Panel |           | X        |                 |               |
| All Requests                      | Panel |           | X        |                 |               |

<span id="_Toc100128361" class="anchor"></span>Table 9: Advanced Query/Customization/My Queries

| Name              | Type   | Requester | Approver | Release Manager | Administrator |
|-------------------|--------|-----------|----------|-----------------|---------------|
| Run A Saved Query | Panel  | X         | X        | X               | X             |
| Save              | Button | X         | X        | X               | X             |
| Delete            | Button | X         | X        | X               | X             |
| Query Builder     | Panel  | X         | X        | X               | X             |
| AND               | Button | X         | X        | X               | X             |
| OR                | Button | X         | X        | X               | X             |
| Clear             | Button | X         | X        | X               | X             |
| Query             | Button | X         | X        | X               | X             |
| Query Result      | Panel  | X         | X        | X               | X             |
| Load              | Button | X         | X        |                 |               |

<span id="_Toc100128362" class="anchor"></span>Table 10: Advanced Query/Customization/Other User’s Queries

| Name              | Type   | Requester | Approver | Release Manager | Administrator |
|-------------------|--------|-----------|----------|-----------------|---------------|
| Run A Saved Query | Panel  | X         | X        | X               | X             |
| Query Result      | Panel  | X         | X        | X               | X             |
| Load              | Button | X         | X        |                 |               |

<span id="_Toc100128363" class="anchor"></span>Table 11: Custom Updates

| Name                     | Type   | Requester | Approver | Release Manager | Administrator |
|--------------------------|--------|-----------|----------|-----------------|---------------|
| Download Existing Update | Link   |           |          | X               |               |
| Create New Update        | Button |           |          | X               |               |

<span id="_Toc100128364" class="anchor"></span>Table 12: Administration

| Name                   | Type   | Requester | Approver | Release Manager | Administrator |
|------------------------|--------|-----------|----------|-----------------|---------------|
| Save                   | Button |           |          |                 | X             |
| Cancel                 | Button |           |          |                 | X             |
| Null Drug Pair Removal | Button |           |          |                 | X             |

<span id="_Toc100128365" class="anchor"></span>Table 13: CDCO Procedures

## User Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User standard CDCO procedures for ANR, etc.

<table>
<caption><p><span id="_Toc100128366" class="anchor"></span>Table 14: Concepts Error Messages</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>Step</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Step 1</td>
<td><p>Send out email to:</p>
<p>VA IT SDE EO EAS PEC SUSTAINMENT <mark>REDACTED</mark></p>
<p>PD PEC Team <mark>REDATED</mark></p>
<p>VHAPBH NDF Support Group <mark>REDACTED</mark></p>
<p>Subject: Per CO or ANR xxxxx AITC will bring down &lt;ENV&gt; to perform maintenance at hh:mm AM/PM CST</p>
<p>Email line1: Per CO or ANR xxxxx AITC will bring down &lt;ENV&gt; to perform scheduled maintenance at hh:mm AM/PM CST</p>
<p>Email line2: AITC will send out notice once the &lt;ENV&gt; is back online and ready for smoke test.</p></td>
</tr>
<tr class="even">
<td>Step 2</td>
<td><p>Login to the WebLogic GUI Admin console with your LAN ID; if this does not work, check the Password Vault for the environment and use the specified account.</p>
<p>Shutdown the requested Managed Servers or Clusters as listed in the Change Order or Service Request.</p></td>
</tr>
<tr class="odd">
<td>Step 3</td>
<td><p>Verify maintenance/deployment completed</p>
<p>Start the requested Managed Servers or Clusters as listed in the Change Order or Service Request.</p></td>
</tr>
<tr class="even">
<td>Step 4</td>
<td><p>Send out email to:</p>
<p>VA IT SDE EO EAS PEC SUSTAINMENT <mark>REDACTED</mark></p>
<p>PD PEC Team <mark>REDACTED</mark></p>
<p>VHAPBH NDF Support Group <mark>REDACTED</mark></p>
<p>Subject: Per CO or ANR xxxxx AITC has successfully completed &lt;ENV&gt; maintenance at {time} CST.</p>
<p>Email line1: Per CO or ANR xxxxx AITC has successfully completed &lt;ENV&gt; maintenance at {time} CST.</p>
<p>Email line2: &lt;ENV&gt; is back online and ready for smoke test.</p>
<p>Email line3: Please update this thread with test results and any outstanding issues.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc100128366" class="anchor"></span>Table 14: Concepts Error Messages

System downtime due to application or system software upgrades will be coordinated with AITC. Users will be notified by PRE using the appropriate mailing lists. The notice will be provided at least two hours in advance. Notification will also be provided when the application becomes available again.

## System Monitoring, Reporting, & Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oracle Enterprise Manager and Grid Control are used to monitor availability and performance of the PECS database on the vapredbs1 server. Standard AITC thresholds are set for space monitoring, availability of the database, and network connectivity. DBAs are alerted immediately if the monitoring tool detects a problem. In addition, if connectivity to the database fails, then an incident ticket is created in the User Service Desk software. This incident ticket is relayed to AITC management and the primary and secondary DBA for the project.

System monitoring is done through the following:

1.  WebLogic console
13. Introscope
14. CEM
15. Xpolog

### Availability Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  WebLogic console has the entire WebLogic environment configuration.
    - The team can monitor the admin server, node manager, managed servers running states, and control managed servers start and stop activity.
    - Manager server’s health and performance, application deployment state, database connection pools, and Java Message Service (JMS) can also be monitored from here.
2.  Introscope: Monitoring tool. One agent per machine is deployed. It can provide in-detail monitoring of all the WebLogic components from that environment and monitoring alerts and notifications can be generated using this tool.

### Performance/Capacity Monitoring 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patrol is utilized by AITC to capture Performance and Capacity activities. It can monitor the http traffic coming from internet cloud to AITC.

## Routine Updates, Extracts and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The third Monday of each month, data is exported from the PREP production database, and imported into the pre-production database, PREY, and to the Safety Quality Assurance (SQA) database, so testers can work with updated data.

The PECS application receives weekly data updates from the COTS vendor that affects the Oracle tables. The updates are applied automatically using DATUP. This same DATUP process is used whenever a released customized file is created from the PECS application. Refer to PECS_FDB-DIF_Custom_Data_Update_Process document that explains the details steps and process contained within the automation.

## Scheduled Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, there is no scheduled maintenance window for PRE. This will be needed in the future, so AITC has a window to do server patching, etc.

Any normal changes that are initiated by the PRE team will come in a Request for Change form to the AITC Build Manager. These requests will be submitted by 12:00pm CST on Friday for a Monday implementation in the Pre-Production environment. Production requests must be received by 12:00pm on Tuesday for implementation on Wednesday. Emergency change requests will be implemented as soon as possible.

## Capacity Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Initial Capacity Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial Capacity Planning for Storage was done by PRE and Enterprise Infrastructure Engineering (EIE) team as per the Application requirement. Subsequently, it was decided in concurrence with AITC Architect to add Host Bus Adapter (HBA) cards to the servers, so that PRE servers have access to Storage Area Network (SAN) storage. The SAN storage will be used to expand the storage capacity for future use as needed.

# Exception Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section presents a list of possible exceptions/errors that may occur during normal operation.

## Routine Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system validates form field values per business rule and data integrity constraints before the form is submitted for processing. If values do not pass user interface validation, then the user is redirected back to the wizard form and a message is displayed informing the user of the corrections needed. Please see Alternative Flows for data validation errors.

The system receives the value after form validation and applies the appropriate business rules (if any) to the value. Examples of a business rule validation may include bounds checking, or any interdependencies that may exist between two data values. Please see Alternative Flows for data validation errors.

Like most systems, PECS may generate a small set of errors that may be considered “routine”. These errors are routine in the sense that they have minimal impact on the user and do not compromise the operational state of the system. Most of the errors are transient in nature and only require the user to retry an operation. The following sub-section describes these errors, their causes, and what response, if any, an operator needs to take.

While the occasional occurrence of these errors may be routine, getting reoccurring errors over a short period of time is an indication of a more serious problem. In that case the error needs to be treated as an exceptional condition.

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security is addressed at design tiers respective of the security requirement. Security authentication is provided by IAM and SSOi and is abstracted by the services layer of the application.

The DATUP subsystem does not provide or enforce a security model. However, the system does access other system interfaces which may encounter security violations. The following known security errors may occur:

1.  Access to FTP denied – The configured FTP Protocol over SSH (SFTP) account username and/or password is incorrect. To resolve this, the FDB-DIF Update DATUP configuration file should be modified to include the correct access information.
16. Access to Email denied – The configured email account username and/or password is incorrect. To resolve this, the FDB-DIF Update DATUP configuration file should be modified to include the correct access information.
17. Access to FDB-DIF denied – The configured JDBC driver URL, driver name, username, and/or password is incorrect. To resolve this, the FDB-DIF Update configuration file should be modified to include the correct access information.
18. Access to “temporary” directory denied – The WebLogic process does not have sufficient permission to write to the operating system defined temporary directory (e.g., “/tmp”). To resolve this, the WebLogic process should be granted write access to the temporary directory.

### Time-outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A time out may occur when accessing a third-party Database. Sometimes queries are dependent upon the availability of the database or run out of time if a large query is requested.

The following process has a known potential timeout in the DATUP subsystem:

Java Messaging Service – A Local JMS send will timeout if it is unable to connect to the National JMS server. To resolve this, the National WebLogic server port should be made accessible from the Local site.

### Concurrency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No information currently.

## Significant Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant errors can be defined as errors or conditions that affect the system stability, availability, performance, or otherwise make the system unavailable to its user base. The following sub-sections contain information to aid administrators, operators, and other support personnel in the resolution of errors, conditions, or other issues.

### Application Error Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS uses the Apache Log4j2 framework for logging. Log files are accessible to authorized users through the web-based Xpolog tool.

Logs location - /u01/app/oracle/user_projects/domains/pecs-\<ENV\>/PECSLogs/

> Maxfilesize=10000KB

> Max. backed up files are 10.

> Growth rate =

# Application Error Messages and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter lists all PECS error, informational, and warning messages and describes what caused them to display. In cases where the support team needs to be contacted, there will usually be a "please contact the support team" statement within the message.

## Customization Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the messages that could appear when a user customizes a Drug-Drug Interaction, Drug Pair, Dose Range, Duplicate Therapy, or Professional Monograph FDB record.

### All Concepts Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the error, informational, and warning messages that can appear for all concepts. If the support team needs to be notified, the statement to notify them is highlighted in yellow.

#### Error Messages

| All Concepts Error Message                                                                                                                                                               | Cause                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Current Action Reason field is required                                                                                                                                                  | User didn’t fill out the ‘Current Action Reason’ field.                                                                               |
| Action 'Submit as Reviewed' cannot be performed on modified records. Please click the 'Modify' button after changing fields. Field '\<name of field\>' cannot be changed for this action | Approver modifies an FDB field on a custom record in the Modified or Deleted action status and clicks the 'Submit as Reviewed' button |
| Action 'Submit for Delete' cannot be performed on modified records. Please click the 'Modify' button after changing fields. Field '\<name of field\>' cannot be changed for this action  | Approver modifies an FDB field on a custom record in the Approved or Deleted action status and clicks the 'Submit for Delete' button  |

<span id="_Toc100128367" class="anchor"></span>Table 15: Concepts Informational Messages

#### Informational Messages

| All Concepts Information Message                                                                                 | Cause                                                                                                                                                                                                                     |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| This custom record has been successfully submitted and will be reviewed at the national level.                   | Either the user clicked the 'Customize' button on an FDB record or the approver modified an FDB field on a custom record in the Approved or Deleted action status and clicked the 'Modify' button                         |
| This custom record has been successfully rejected.                                                               | User clicked the 'Reject' button on a VA custom record and did not previously click the 'Submit for Delete' or 'Submit as Reviewed' button.                                                                               |
| This custom record has been successfully submitted for review.                                                   | Approver clicked the 'Submit for Review' button on a VA custom record and didn't fill out any FDB fields on the customization.                                                                                            |
| This custom record has been approved.                                                                            | Approver clicked the 'Approve' button on a custom record.                                                                                                                                                                 |
| This custom record has been successfully modified and will be reviewed at the national level.                    | Approver modified several non-FDB fields on a custom record in the Approved action status and clicked the 'Modify' button.                                                                                                |
| This custom record has been successfully submitted for delete.                                                   | Approver clicked the 'Submit for Delete' button on a custom record in the Approved action status whose associated drug pairs had been deleted.                                                                            |
| This custom record has been successfully deleted.                                                                | Approver clicked the 'Delete' button on a customization in the Delete_Reviewed action status.                                                                                                                             |
| This request for deletion has been rejected. The record has returned to previous action status (‘Approved’).     | Approver clicked the 'Submit for Delete' button on a custom record in the Approved action status and then, the user clicked the 'Reject' button.                                                                          |
| This reviewed record has been rejected. The record has returned to previous action status (‘Deleted’).           | Approver clicked the 'Submit as Reviewed' button on a custom record in the Deleted action status and then, the user clicked the 'Reject' button.                                                                          |
| This request for modification has been rejected. The record has returned to previous action status (‘Approved’). | Approver modified an FDB field on a custom record in the Approved action status and clicked the 'Modify' button and then, the user clicked the 'Reject' button.                                                           |
| This request for modification has been rejected. The record has returned to previous action status (‘Deleted’).  | Approver modified an FDB field on a custom record in the Deleted action status and clicked the 'Modify' button and then, the user clicked the 'Reject' button.                                                            |
| To update the record, click the edit button below.                                                               | User has entered the detail page for one of the concepts. (When a user first enters a detail page, it will be in read-only mode. The only way a user will be able to update the detail page is to click the Edit button.) |

<span id="_Toc100128368" class="anchor"></span>Table 16: Dose Range Error Messages

### Dose Range Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Error Messages

<table>
<caption><p><span id="_Toc100128369" class="anchor"></span>Table 17: Dose Range Warning Messages</p></caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Dose Range Detail Page Error Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Unable to perform field validation due to: “+ex.getMessage());”</p>
<p>Please report this error to the support team.</p></td>
<td><p>User chooses a VA customized table, and the system is unable to retrieve the field names to display.</p>
<p>Note –Based on how the code is currently written, this error should never occur.</p></td>
</tr>
<tr class="even">
<td><p>The customized Dose Range Check record could not be found.</p>
<p>Please report this error to the support team.</p></td>
<td>User queries for a dose range record and the system can’t correctly parse the record to display.</td>
</tr>
<tr class="odd">
<td><p>FDB customized object was not found in the database.</p>
<p>Please report this error to the support team.</p></td>
<td>User chooses an FDB record to customize, and the system is unable to retrieve the FDB record.</td>
</tr>
<tr class="even">
<td><p>Unable to perform the load operation on the customization.</p>
<p>Record cannot be retrieved.</p>
<p>Please report this error to the support team.</p></td>
<td>User attempts to retrieve a record, and the system is unable to execute the process.</td>
</tr>
<tr class="odd">
<td><p>Unable to perform the update operation on the customization.</p>
<p>Please report this error to the support team.</p></td>
<td>User attempts to perform a customization, and the system is unable to execute the process.</td>
</tr>
<tr class="even">
<td>The age range entered overlaps with an existing customization.</td>
<td>User enters values in the 'Age Low In Days' and 'Age High in Days' fields that overlap with an age range on an existing customization.</td>
</tr>
<tr class="odd">
<td>The age low and age high in days fields cannot both be zero (or blank) at the same time.</td>
<td>User either enters value of zero in both the 'Age Low in Days' and 'Age High in Days' fields or leaves both fields blank.</td>
</tr>
<tr class="even">
<td>Age Low In Days field must be numeric and cannot contain more than 10 characters.</td>
<td>Either the user enters a value in the 'Age Low in Days' field that is greater than 10 numeric characters or enters a non-numeric value.</td>
</tr>
<tr class="odd">
<td>Age High In Days field must be numeric and cannot contain more than 10 characters.</td>
<td>Either the user enters a value for 'Age High in Days' field that is greater than 10 numeric characters or the user enters a non-numeric value.</td>
</tr>
<tr class="even">
<td>The value in the Age High in Days field that is less than the value of the Age Low in Days field.</td>
<td>The value in the 'Age High in Days' field that is less than the value of the 'Age Low in Days' field.</td>
</tr>
<tr class="odd">
<td>Dose Route field is required.</td>
<td>User enters a blank value in the 'Dose Route' field.</td>
</tr>
<tr class="even">
<td>Dose Type field is required.</td>
<td>User enters a blank value in the 'Dose Type' field.</td>
</tr>
<tr class="odd">
<td>Dose Low field must be a number up to 10 digits including a maximum of six digits to the right of the decimal point.</td>
<td>Either the user enters a value in the 'Dose Low' field that is either greater than ten digits or has more than six digits to the right of the decimal point or the user enters a non-numeric value.</td>
</tr>
<tr class="even">
<td>Dose High field must be a number up to 10 digits including a maximum of six digits to the right of the decimal point.</td>
<td>Either the user enters a value in the 'Dose High' field that is either greater than ten digits or has more than six digits to the right of the decimal point or the user enters a non-numeric value.</td>
</tr>
<tr class="odd">
<td>DOSEFORMLOW field must be numeric.</td>
<td>User enters a non-numeric value in the 'Dose Form Low' field.</td>
</tr>
<tr class="even">
<td>DOSEFORMHIGH field must be numeric.</td>
<td>User enters a non-numeric value in the 'Dose Form High' field.</td>
</tr>
<tr class="odd">
<td>FREQUENCYLOW field must be numeric.</td>
<td>User enters a non-numeric value in the ' Frequency Low' field.</td>
</tr>
<tr class="even">
<td>FREQUENCYHIGH field must be numeric.</td>
<td>User enters a non-numeric value in the 'Frequency High' field.</td>
</tr>
<tr class="odd">
<td>DURATIONLOW field must be numeric.</td>
<td>User enters a non-numeric value in the 'Duration Low' field.</td>
</tr>
<tr class="even">
<td>DURATIONHIGH field must be numeric.</td>
<td>User enters a non-numeric value in the 'Duration High' field.</td>
</tr>
<tr class="odd">
<td>MAXDURATION field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Duration' field.</td>
</tr>
<tr class="even">
<td>MAXSINGLEDOSE field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Single Dose' field.</td>
</tr>
<tr class="odd">
<td>MAXSINGLEDOSEFORM field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Single Dose Form' field.</td>
</tr>
<tr class="even">
<td>MAXDAILYDOSE field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Daily Dose' field.</td>
</tr>
<tr class="odd">
<td>MAXDAILYDOSEFORM field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Daily Dose Form' field.</td>
</tr>
<tr class="even">
<td>MAXLIFETIMEDOSE field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Lifetime Dose' field.</td>
</tr>
<tr class="odd">
<td>MAXLIFETIMEDOSEFORM field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Lifetime Dose Form' field.</td>
</tr>
<tr class="even">
<td>DOSERATELOW field must be numeric.</td>
<td>User enters a non-numeric value in the 'Dose Rate Low' field.</td>
</tr>
<tr class="odd">
<td>DOSERATEHIGH field must be numeric.</td>
<td>User enters a non-numeric value in the 'Dose Rate High' field.</td>
</tr>
<tr class="even">
<td>DOSEFORMRATELOW field must be numeric.</td>
<td>User enters a non-numeric value in the 'Dose Form Rate Low' field.</td>
</tr>
<tr class="odd">
<td>DOSEFORMRATEHIGH field must be numeric.</td>
<td>User enters a non-numeric value in the 'Dose Form Rate High' field.</td>
</tr>
<tr class="even">
<td>MAXSINGLEDOSERATE field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Single Dose Rate' field.</td>
</tr>
<tr class="odd">
<td>MAXSINGLEDOSEFORMRATE field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Single Dose Form Rate' field.</td>
</tr>
<tr class="even">
<td>MAXDAILYDOSERATE field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Daily Dose Rate' field.</td>
</tr>
<tr class="odd">
<td>MAXDAILYDOSEFORMRATE field must be numeric.</td>
<td>User enters a non-numeric value in the 'Max Daily Dose Form Rate' field.</td>
</tr>
<tr class="even">
<td>HEPATICIMPAIRMENTIND field must be numeric and cannot contain more than 6 characters.</td>
<td>Either the user enters a non-numeric value in the 'Hepatic Impairment Indicator' field or the user enters a value that is greater than six digits.</td>
</tr>
<tr class="odd">
<td>RENALIMPAIRMENTIND field must be numeric and cannot contain more than 6 characters.</td>
<td>Either the user enters a non-numeric value in the 'Renal Impairment Indicator' field or a user enters a value that is greater than six digits.</td>
</tr>
<tr class="even">
<td>CRCLTHRESHHOLD field must be numeric and cannot contain more than 6 characters.</td>
<td>Either the user enters a non-numeric value in the 'Creatinine Clearance Threshold' field or the user enters a value that is greater than six digits.</td>
</tr>
<tr class="odd">
<td>LOWELIMINATIONHALFLIFE field must be numeric</td>
<td>User enters a non-numeric value in the 'Low Elimination Half Life' field.</td>
</tr>
<tr class="even">
<td>HIGHELIMINATIONHALFLIFE field must be numeric</td>
<td>User enters a non-numeric value in the 'High Elimination Half Life' field.</td>
</tr>
<tr class="odd">
<td>WEIGHTREQUIREDIND field must be numeric and cannot contain more than 6 characters.</td>
<td>Either the user enters a non-numeric value for 'Weight Required Indicator' field or the user enters a value greater than six digits.</td>
</tr>
<tr class="even">
<td>BSAREQUIREDIND field must be numeric and cannot contain more than 6 characters.</td>
<td>Either the user enters a non-numeric value for' BSA Required Indicator' field or the user enters a value greater than six digits.</td>
</tr>
<tr class="odd">
<td>Reference Text field cannot contain more than 1024 characters.</td>
<td>User enters more than 1024 characters in the 'Reference Text' field.</td>
</tr>
<tr class="even">
<td><p>System error, the navigation action is not valid.</p>
<p>Please report this error to the support team.</p></td>
<td><p>User attempts navigation that is not coded.</p>
<p>Note – according to the developer this scenario is impossible, though it is in the code</p></td>
</tr>
<tr class="odd">
<td><p>System error, wizard flow is not consistent with this action.</p>
<p>Please report this error to the support team.</p></td>
<td><p>User attempts an action that is not coded.</p>
<p>Note – according to the developer this scenario is impossible, though it is in the code</p></td>
</tr>
<tr class="even">
<td><p>System error, unable to perform the customization on this record.</p>
<p>Please report this error to the support team.</p></td>
<td>User attempts to save a record, and the system is unable to execute the process.</td>
</tr>
<tr class="odd">
<td>‘X’ UNITS field cannot be blank when ‘X’ field has numeric value.</td>
<td>User modifies a record that has a blank ‘units’ field for a corresponding field containing a numeric value. For example, the 'Dose Low' field contains a number with no corresponding dose low units.</td>
</tr>
<tr class="even">
<td>Concept Type/Concept ID Number combination does not exist in FDB (Note: This is a popup error message.)</td>
<td>User enters an invalid Concept ID Number on the Open Blank Form page</td>
</tr>
<tr class="odd">
<td>Cannot customize. Invalid Concept Type/Concept ID Number combination</td>
<td>User tries to customize a record with a new Concept ID Number on the Open Blank Form page</td>
</tr>
<tr class="even">
<td>MAXSINGLENTEDOSE field must be numeric</td>
<td>User enters a non-numeric value in the 'Max Single Not to Exceed (NTE) Dose' field</td>
</tr>
<tr class="odd">
<td>MAXSINGLENTEDOSEFORM field must be numeric</td>
<td>User enters a non-numeric value in the 'Max Single NTD Dose Form' field</td>
</tr>
<tr class="even">
<td>MAXSINGLENTEDOSE field must be a number up to 10 digits including a maximum of six digits to the right of the decimal point</td>
<td>User enters a value that is more than 10 digits or has more than 6 digits after the decimal point in the 'Max Single NTE Dose' field</td>
</tr>
<tr class="odd">
<td>MAXSINGLENTEDOSEFORM field must be a number up to 10 digits including a maximum of six digits to the right of the decimal point</td>
<td>User enters a value that is more than 10 digits or has more than 6 digits after the decimal point in the 'Max Single NTE Dose Form' field</td>
</tr>
<tr class="even">
<td><p>'x' field cannot be blank when 'y' field has numeric value</p>
<p>Where x = the NTE unit field (MAXSINGLENTEDOSEUNIT or MAXSINGLENTEDOSE FORMUNIT)</p>
<p>y = the NTE dose field (MAXSINGLENTEDOSE or MAXSINGLENTEDOSEFORM)</p></td>
<td>User enters a value for the 'Max Single NTE Dose' or 'Max Single NTE Dose Form' field but leaves the corresponding ‘units’ field blank (Max Single NTE Dose Unit or Max Single NTE Dose Form)</td>
</tr>
</tbody>
</table>

<span id="_Toc100128369" class="anchor"></span>Table 17: Dose Range Warning Messages

#### Warning Messages

| Dose Range Detail Page Warning Message                                                                                                                | Cause                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| A request for customization exists for this dosing concept id: x submitted by: y, updated on z. See below for the duplicate VA custom record details. | User selects an FDB record to customize for which a VA custom record already exists |

<span id="_Toc100128370" class="anchor"></span>Table 18: Drug-Drug Interaction Error Messages

### Drug-Drug Interaction Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Error Messages

<table>
<caption><p><span id="_Toc100128371" class="anchor"></span>Table 19: DDI Informational Messages</p></caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Drug-Drug Interaction Error Messages</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Interaction Description is required</td>
<td>User doesn't input a value into the 'Interaction Description' field.</td>
</tr>
<tr class="even">
<td>Interaction Description field is invalid; it must contain two drug names separated by a forward slash/</td>
<td>User inputs more than one forward slash (/) when entering a value into the 'Interaction Description' field.</td>
</tr>
<tr class="odd">
<td>Record could not be retrieved due to missing ID number. Please report this error to the support team.</td>
<td>User selects a DDI VA record from the query results to modify, but the record id is null or empty (“”).</td>
</tr>
<tr class="even">
<td><p>The specified FDB record was not found.</p>
<p>Please report this error to the support team.</p></td>
<td>User selects an FDB record to customize but it cannot be found in the database for the given FDB interaction id. This error displays in the FDB table results area and the detailed page doesn’t get loaded.</td>
</tr>
<tr class="odd">
<td><p>The specified FDB interaction ID has errors.</p>
<p>Please report this error to the support team.</p></td>
<td>User selects an FDB record to customize; however, multiple FDB records are in the database for the given interaction id. This error displays in the FDB table results area and the detailed page doesn’t get loaded.</td>
</tr>
<tr class="even">
<td><p>The specified Interaction ID has errors.</p>
<p>Please report this error to the support team.</p></td>
<td>An FDB record cannot be retrieved from the FDB database for the given interaction id when selected for customization or a VA record cannot be retrieved from the staging database for the given id when selected for modification, because the interaction id is invalid, inactive, or deleted.</td>
</tr>
<tr class="odd">
<td><p>The specified VA Custom interaction ID has errors.</p>
<p>Please report this error to the support team.</p></td>
<td>User selects a DDI VA record to modify; however, the customized VA record cannot be found in the database for the given interaction id. This error displays in the VA table results area and the detailed page doesn’t get loaded.</td>
</tr>
</tbody>
</table>

<span id="_Toc100128371" class="anchor"></span>Table 19: DDI Informational Messages

#### Informational Messages

<table>
<caption><p><span id="_Toc100128372" class="anchor"></span>Table 20: DDI Warning Messages</p></caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Drug-Drug Interaction Informational Messages</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The custom severity level entered is less than the FDB reference record severity level.</td>
<td>User selects an FDB record to customize and selects a severity level that is lower than the FDB reference record severity level. For example, the FDB record severity level is 2 but the user selects a severity level of 3.</td>
</tr>
<tr class="even">
<td><p>The interaction does not have any associated drug pairs.</p>
<p>Click on the Drug Pairs button to add drug pairs to the interaction.</p></td>
<td>The custom DDI record in the New, Reviewed, or Modified (after Delete) action status does not have any drug pairs associated with it.</td>
</tr>
<tr class="odd">
<td>The associated drug pairs are not all reviewed yet. To submit this interaction as reviewed, you must review all associated drug pairs. First click on the Drug Pairs button then take appropriate action.</td>
<td>The drug pairs associated with the DDI custom record are not all in the Reviewed action status. They may all be in the 'New' action status or some of them may be 'New' while others are in the 'Reviewed' action status.</td>
</tr>
<tr class="even">
<td>The associated drug pairs are not all approved yet. To approve the interaction, you must approve all the associated drug pairs first. Click on the Drug Pairs button to view and approve the associated drug pairs.</td>
<td>The drug pairs associated with the DDI custom record are not all in the Approved action status. They may all be in the 'Reviewed' action status or some of them may be 'Reviewed' while others are in the 'Approved' action status.</td>
</tr>
<tr class="odd">
<td>Click on the Drug Pairs button to add or remove drug pairs to the interaction.</td>
<td>Approver modified an FDB field on a custom record in the 'Approved' action status and clicked the 'Modify' button.</td>
</tr>
<tr class="even">
<td>The associated drug pairs are all in the rejected state.</td>
<td>The drug pairs associated with a DDI custom record are all in the Rejected action status.</td>
</tr>
<tr class="odd">
<td>The associated drug pairs are not all rejected or deleted yet. You must click on the Drug Pairs button then take appropriate action.</td>
<td>Approver rejected a DDI custom record in the 'Reviewed' action status while its drug pairs were still in the 'Approved' action status.</td>
</tr>
<tr class="even">
<td>Following VA custom record(s) already exist for this FDB Drug-Drug Interaction.</td>
<td>User opened an FDB DDI detail page from the Advanced Query/Customization tab and the FDB DDI has some VA custom records already created from it.<br />
This message is displayed on the FDB DDI Detail page if the FDB DDI has a VA custom record associated with it.</td>
</tr>
<tr class="odd">
<td>Following additional VA custom record(s) exist for the corresponding FDB Drug-Drug Interaction.</td>
<td>The user opened a VA custom record from the Advanced Query/Customization tab and the corresponding FDB DDI was used to create more than one VA record.<br />
This message is displayed on the VA DDI Detail page if the corresponding FDB DDI has more than one VA custom record.</td>
</tr>
</tbody>
</table>

<span id="_Toc100128372" class="anchor"></span>Table 20: DDI Warning Messages

#### Warning Messages

| Drug-Drug Interaction Warning Messages                                                                                             | Cause                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The interaction '\<Drug A/Drug B\>' is already customized with severity 'x'. See below for the duplicate VA custom record details. | User requests an FDB customization and changes the Severity Level Code. However, there is already an existing custom VA record at the requested severity level. For example, a requestor selects an FDB record to customize from severity level code 3 to 2. But there is already an existing custom VA record created from this FDB record at severity level 2. |

<span id="_Toc100128373" class="anchor"></span>Table 21: Drug Pair Customization Page Error Messages

### Drug Pair Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Customization Page Messages

#### Error Messages

<table>
<caption><p><span id="_Toc100128374" class="anchor"></span>Table 22: Drug Pair Lookup Query Page Error Messages</p></caption>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Drug Pair Customization Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The specified Drug-Drug Pair ID has errors.</p>
<p>Please report this error to the support team.</p></td>
<td><p>User tries to display drug pair whose record id is the incorrect length.</p>
<p>Note – the record id is an internal database element</p></td>
</tr>
<tr class="even">
<td><p>Custom interaction is null on drug pairs wizard table.</p>
<p>Please report this error to the support team.</p></td>
<td>User tries to reference a drug pair by the drug interaction ID and the data record cannot be retrieved from the database.</td>
</tr>
<tr class="odd">
<td>Routed Generic #1 and Routed Generic #2 cannot be the same value. X<br />
Where X is the drug name</td>
<td>On the Drug Pair Customization page accessed by the 'Drug Pair' button on the drug-drug interaction customization detail page, user adds a drug pair to a Drug-Drug interaction by selecting a pair of routed generic drugs in which both drugs in the pair are the same drug.</td>
</tr>
<tr class="even">
<td>Unable to perform the save operation on the customization. (Drug pairs cannot be added to a deleted interaction)</td>
<td>On the Drug Pair Customization page accessed by the 'Drug Pair' button on the drug-drug interaction customization detail page for a Drug-Drug interaction with a 'Deleted' or 'Delete Reviewed' action status, user tries to add a drug pair.</td>
</tr>
<tr class="odd">
<td>Unable to perform the save operation on the customization. (Field 'Current Action Reason' is required)</td>
<td>User adds a drug pair to a Drug-Drug interaction without entering a current action reason by either adding an FDB drug pair or selecting a pair of routed generic drugs.</td>
</tr>
<tr class="even">
<td>Enter values in text boxes below and click 'Customize' to add drug pairs to interaction.</td>
<td>When using the 'Drug Pair' button on the drug-drug interaction customization detail, user chooses to expand the option to 'Select Drug Pairs' to add to the above VA Custom Interaction page</td>
</tr>
<tr class="odd">
<td>Select from list of FDB drug pairs - note that at least one drug pair must be chosen before clicking the Customize button.</td>
<td>When 'Drug Pair' button on the drug-drug interaction customization detail page, user chooses to select a drug pair to add to the custom drug-drug interaction by selecting an FDB drug pair</td>
</tr>
<tr class="even">
<td>Select from list of Generic drug pairs - note that a drug pair must be chosen before clicking the Customize button. Routed Generic #1 and Routed Generic #2 fields cannot be the same value. Routed Generic #1 and Routed Generic #2 must follow the same order as the Interaction Description.</td>
<td>When using the 'Drug Pair' button on the drug-drug interaction customization detail page, user chooses to select a drug pair by selecting from routed generic drug lists</td>
</tr>
<tr class="odd">
<td>Either no drug pairs exist for this custom interaction or there are no drug pairs for the current Action Status filter. Please update the Action Status filter or create new custom drug pair(s) for this interaction by clicking on 'Select Drug Pairs' to add to the above VA Custom Interaction’.</td>
<td>On the Drug Pair Customization page accessed by the 'Drug Pair' button on the DDI Detail page, the user chooses to view and/or edit associated drug pairs when either the DDI has no associated drug pairs or there are no drug pairs for the 'Action Status' filter that was selected.</td>
</tr>
<tr class="even">
<td>Select/Deselect All Drug Pairs Displayed from VA Custom Interaction</td>
<td>On the Drug Pair Customization page accessed by the 'Drug Pair' button on the drug-drug interaction customization detail page for a Drug-Drug interaction, user chooses to view and/or edit associated Drug-Drug pairs.</td>
</tr>
<tr class="odd">
<td><p>Now showing x of y total records.</p>
<p>Where x is the number of associated drug pairs filtered to display and y is the total number of associated drug pairs.</p></td>
<td>On the Drug Pair Customization page accessed by the 'Drug Pair' button on the drug-drug interaction customization detail page for a Drug-Drug interaction, user chooses to get a count of the displayed and total associated drug pairs.</td>
</tr>
<tr class="even">
<td>Attempt to create duplicate drug pair(s): x<br />
<br />
Where x is each pair of duplicate routed generic drugs that cannot be created.</td>
<td>On the Drug Pair Customization page, the user tries to customize one or more duplicate DPs from the Routed Generic Drug List.</td>
</tr>
<tr class="odd">
<td><p>Attempt to create duplicate drug pair(s): x. This Drug Pair combination already exist for the Interaction ID y. Drug Pair must first be deleted from Interaction ID y to be added to this new VA custom DDI with Interaction ID z<br />
<br />
Where x is each pair of duplicate routed generic drugs that cannot be created;</p>
<p>y is the other interaction that is associated with the duplicate drug pair;</p>
<p>z is the current interaction.</p></td>
<td>On the Drug Pair Customization page, the user tries to customize one or more drug pairs that already exist on an associated interaction,</td>
</tr>
<tr class="even">
<td>Another pair exists with the drugs in reverse order: x<br />
Where x is each pair of routed generic drugs whose reverse already exists.</td>
<td>On the Drug Pair Customization page, the user tries to customize one or more DPs that are the reverse of a drug pair that already exists on the current interaction.</td>
</tr>
<tr class="odd">
<td><p>Another pair exists with the drugs in reverse order: x. This Drug Pair combination already exists (in reverse order) for the Interaction ID: y. The Drug Pair must first be deleted from Interaction ID: y to be added to this new VA custom DDI with Interaction ID: z</p>
<p>Where x is each pair of routed generic drugs whose reverse already exists;</p>
<p>y is the interaction that is associated with the reverse drug pair;</p>
<p>z is the current interaction.</p></td>
<td>On the Drug Pair Customization page, the user tries to customize one of more drug pairs that are the reverse of a drug pair that already exists on an associated interaction,</td>
</tr>
<tr class="even">
<td>Existing VA Custom Record(s)</td>
<td>When a User opens the Drug Pair Customization Page, a list of custom records for the associated FDB DDI appears.</td>
</tr>
</tbody>
</table>

<span id="_Toc100128374" class="anchor"></span>Table 22: Drug Pair Lookup Query Page Error Messages

#### Lookup Query Page Messages

#### Error Messages

<table>
<caption><p><span id="_Toc100128375" class="anchor"></span>Table 23: Single Drug Pairs Detail Page Error Messages</p></caption>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Drug Pair Lookup Page Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No VA custom records.</td>
<td>User submits a drug pair query that finds FDB records but no customized VA records</td>
</tr>
<tr class="even">
<td><p>x is not a number, only numbers are Allowed.</p>
<p>where x is the value entered for the interaction.</p></td>
<td>User submits a non-numeric value in the interaction field in a drug pair query</td>
</tr>
<tr class="odd">
<td><p>No VA custom records.</p>
<p>and</p>
<p>No FDB records.</p></td>
<td>User submits a drug pair query that finds no customized VA records or FDB records</td>
</tr>
<tr class="even">
<td><p>The Drug-Drug interaction 'x' has not been customized. You must customize the Drug-Drug interaction prior to customizing the Drug-Drug pair.</p>
<p>Where x is the selected interaction id and interaction id description</p></td>
<td>User chooses to view a FDB defined drug pair that is not associated with a customized VA drug-drug interaction</td>
</tr>
<tr class="odd">
<td>The selected drug pair is associated with the VA custom interaction 'x' with severity 'y'. See below for the duplicate VA custom record details. Where x, is the interaction description and y, is the severity level code.</td>
<td>User chooses to view an FDB defined drug pair that is associated with a customized VA drug-drug interaction</td>
</tr>
</tbody>
</table>

<span id="_Toc100128375" class="anchor"></span>Table 23: Single Drug Pairs Detail Page Error Messages

#### Single Drug Pairs Detail Page Messages

#### Error Messages

<table>
<caption><p><span id="_Toc100128376" class="anchor"></span>Table 24: Single Drug Pairs Detail Page Informational Messages</p></caption>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Single Drug Pairs Detail Page Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The specified Drug Pair ID has errors. Please report this error to the support team.</td>
<td>User clicked the 'Drug Pair Lookup' button, selected a drug pair from the FDB table, and got a message that the drug pair ID has errors.</td>
</tr>
<tr class="even">
<td>The Drug-Drug interaction &lt;Drug A/Drug B&gt;’ has not been customized. You must customize the Drug-Drug interaction prior to customizing the Drug-Drug pair. Do you want to customize the Drug-Drug interaction?</td>
<td>User does a drug pair query, selects a FDB drug pair associated with an FDB Drug interaction that has never been customized and sees a Drug-Drug Interaction Message instead of the Drug Pairs detail page</td>
</tr>
<tr class="odd">
<td><p>The selected drug pair is not customized. The drug interaction &lt;Drug A/Drug B&gt; has been customized with severity level 'x'.</p>
<p>Customization of this drug pair can be done only through the VA custom Drug-Drug Interaction detail page.</p></td>
<td>User does a drug pair query and selects a drug pair in the FDB table. The drug pair is not customized but its parent DDI has already been customized.</td>
</tr>
<tr class="even">
<td>The selected drug pair is associated with the VA custom interaction 'x' with severity 'y'. See below for the duplicate VA custom record details.<br />
Further customization or deletion of this drug pair can be done only through the VA custom Drug-Drug Interaction detail page.</td>
<td>User does a drug pair query and selects a drug pair in the FDB table. The drug pair and its parent DDI are customized.</td>
</tr>
<tr class="odd">
<td>Further customization or deletion of this drug pair can be done through the VA custom Drug-Drug Interaction detail page.</td>
<td>User does a drug pair query and selects a drug pair in the VA table</td>
</tr>
</tbody>
</table>

<span id="_Toc100128376" class="anchor"></span>Table 24: Single Drug Pairs Detail Page Informational Messages

#### Informational Messages

<table>
<caption><p><span id="_Toc100128377" class="anchor"></span>Table 25: Duplicate Therapy Error Messages</p></caption>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Single Drug Pairs Detail Page Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The selected drug pair is also associated with VA Custom Interaction 'x' with severity level 'y' and is in the &lt;Rejected or<br />
Deleted&gt; action status.<br />
<br />
Where 'x' is the Interaction ID and Description and 'y' is the severity level.</td>
<td><p>User does a query on an FDB drug pair that has these characteristics:</p>
<ol type="a">
<li><p>The drug pair is associated with an FDB DDI that has been customized more than once;</p></li>
<li><p>On all the older VA customizations, the drug pair has been rejected and/or deleted;</p></li>
<li><p>On the latest VA customization, the drug pair is in the New, Modified, Reviewed, Approved, Delete_Reviewed, or Deleted action status.</p></li>
</ol>
<p>After the user does a query on an FDB drug pair that has all three traits mentioned above, the drug pair displayed on the Drug Pairs Detail Page is the one associated with the latest VA customization and the drug pair for all the other VA customizations is described in the message listed on the left.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc100128377" class="anchor"></span>Table 25: Duplicate Therapy Error Messages

### Duplicate Therapy Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Error Messages

| Duplicate Therapy Message                                                                                                  | Cause                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Custom String field is required                                                                                            | User does not input any data into the 'Custom String' field                                                                                                                                                                        |
| The specified Duplicate Therapy Customization ID (DTCID) could not be found. Please report this error to the support team. | User selects a DT FDB record to customize; however, an FDB record cannot be found in the database for the given Duplicate Therapy Customization ID (DTCID). An error message will appear before the detail page is loaded.         |
| The specified Duplicate Therapy Customization ID (DTCID) could not be found. Please report this error to the support team. | User selects a DT VA record from the query results to modify. However, the VA record ID is null or empty (“”) for some reason.                                                                                                     |
| The specified Duplicate Therapy Customization ID (DTCID) could not be found. Please report this error to the support team. | User selects a DT FDB record from the query to customize. However, the DTCID is null or empty (“”) for some reason.                                                                                                                |
| The specified Duplicate Therapy Customization ID (DTCID) could not be found. Please report this error to the support team. | The user selects a VA customized record from the list and for some reason; the DTCID is invalid, inactive, or deleted.                                                                                                             |
| Field must be numeric and cannot contain more than 10 characters.                                                          | DTCID is null or has a length greater than ten.                                                                                                                                                                                    |
| The specified VA custom record could not be found. Please report this error to the support team.                           | The user selects a record from the VA customization list; however, the detailed information for the customized record is missing from the database. This error appears after the user selects the customized record from the list. |

<span id="_Toc100128378" class="anchor"></span>Table 26: Duplicate Therapy Informational Messages

#### Informational Messages

| Duplicate Therapy Message                                                           | Cause                                                                               |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Following VA custom record already exists for this FDB Duplicate Therapy: \[DTCID\] | User opens an FDB duplicate therapy record that has an associated VA custom record. |

<span id="_Toc100128379" class="anchor"></span>Table 27: Professional Monograph Error Messages

### Professional Monograph Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Error Messages

| Professional Monograph Detail Page Message                                                                                                                | Cause                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Monograph Title is required                                                                                                                               | User didn't fill in the 'Monograph Title' field                                                                                       |
| The Professional Monograph FDB reference record was not found in the database. Please report this error to the support team                               | User selected a Professional Monograph record in the FDB table. However, it wasn't found in the database.                             |
| Multiple Professional Monograph FDB reference records were found in the FDB database for the specified ID. Please report this error to the support team   | User selected a Professional Monograph record in the FDB table, but multiple records were found in the database for the specified ID. |
| The specified Professional Monograph ID has errors. Please report this error to the support team                                                          | User customized a Professional Monograph. However, the record couldn't load from the FDB table.                                       |
| The customization was not found. The monograph may be invalid, or it may have an INACTIVE or DELETED status. Please report this error to the support team | User selected a Professional Monograph record in the VA table. However, the custom record was not found in the database.              |
| Unable to perform the update operation on the customization. Custom monograph title '\<monograph title\>' is not unique.                                  | User inputs a monograph title that already exists.                                                                                    |

<span id="_Toc100128380" class="anchor"></span>Table 28: Professional Monograph Informational Messages

#### Informational Messages

| Professional Monograph Detail Page Message                                              | Cause                                                                                    |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Following VA custom record exists for this FDB Professional Monograph: \[Monograph ID\] | User opens an FDB professional monograph record that has an associated VA custom record. |

<span id="_Toc100128381" class="anchor"></span>Table 29: Professional Monograph Warning Messages

#### Warning Messages

| Professional Monograph Detail Page Warning Message                                                           | Cause                                                                                              |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| The monograph with title '\<title\>' is already customized. See the duplicate VA custom record details below | Requestor did a query of FDB monographs and selected a monograph that had already been customized. |

<span id="_Toc100128382" class="anchor"></span>Table 30: Custom Update Error Messages

## Custom Update Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Error Messages

| Custom Update Page Message                                                                            | Cause                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unable to generate the update file. The update file specified does not exist or could not be located. | Release manager selects a custom update and clicks the 'Download Existing Update' button. However, the system is unable to generate the update file. |
| Unable to generate the update file. Failed to create customization update file                        | Release manager clicks the 'Create New Update' button. However, the system is unable to generate the update file.                                    |

<span id="_Toc100128383" class="anchor"></span>Table 31: Query Pages Error Messages

## Query Pages Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Error Messages

<table>
<caption><p><span id="_Toc100128384" class="anchor"></span>Table 32: Query Pages Informational Messages</p></caption>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Query Page Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Either a system error occurred, or the query timed out, and the query could not be executed at this time.</p>
<p>Resubmit query. If problem persists, report this error to the support team.</p></td>
<td>User submits a query that errors during execution or cannot be executed</td>
</tr>
<tr class="even">
<td><p>The list of columns set for display could not be loaded from the database.</p>
<p>Resubmit query. If problem persists, report this error to the support team.</p></td>
<td>User queries the database and the list of columns to display is empty because of a failure in the process that retrieves the data from the database</td>
</tr>
<tr class="odd">
<td><p>Either a system error occurred, or the query operation timed out, and the operation to save the query could not be executed.</p>
<p>Resubmit query. If problem persists, report this error to the support team.</p></td>
<td>Approver tries to save a query, but it cannot be saved due to a database issue</td>
</tr>
<tr class="even">
<td>This query was not correctly saved and must be rebuilt after it is deleted. Please report this query to the support team to ensure it is deleted properly.</td>
<td><p>Approver saves a query on a page which displays both custom VA and FDB records, but the query does not correctly save with custom VA table names due to a system problem</p>
<p>Note – according to the developer this scenario is impossible, though it is in the code</p></td>
</tr>
<tr class="odd">
<td><p>One or more saved queries were unable to be retrieved at this time.</p>
<p>Resubmit query. If problem persists, report this error to the support team.</p></td>
<td>Approver tries to access his or her saved queries and they cannot be retrieved from the database</td>
</tr>
<tr class="even">
<td><p>Saved query was not found and is unable to be deleted at this time.</p>
<p>Resubmit query. If problem persists, report this error to the support team.</p></td>
<td>Approver tries to delete a query and it cannot be retrieved from the database</td>
</tr>
<tr class="odd">
<td><p>Either a system error occurred, or the query operation timed out, and the operation to execute the Others query could not be executed.</p>
<p>Resubmit query. If problem persists, report this error to the support team.</p></td>
<td>User tries to access queries saved by other users and they cannot be retrieved from the database</td>
</tr>
</tbody>
</table>

<span id="_Toc100128384" class="anchor"></span>Table 32: Query Pages Informational Messages

#### Informational Messages

<table>
<caption><p><span id="_Toc100128385" class="anchor"></span>Table 33: Record Locking Pop-Up Messages</p></caption>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Query Page Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No query results found. Please (re)submit a query.</td>
<td>User submits a query for either FDB or customized VA records that finds no records</td>
</tr>
<tr class="even">
<td><p>There were no Custom records found that matched your query parameters.</p>
<p>and</p>
<p>There were no FDB records found that matched your query parameters.</p></td>
<td>User submits a query for both customized VA records and FDB records that finds no records</td>
</tr>
<tr class="odd">
<td>There were no FDB records found that matched your query parameters.</td>
<td>User submits a query for both customized VA records and FDB records that finds only customized VA records</td>
</tr>
<tr class="even">
<td><p>The selected query could not be loaded.</p>
<p>Please reselect the query parameters to refresh the saved searches.</p></td>
<td>User tries to load a query saved by another user and the query was deleted since the time the name was displayed.</td>
</tr>
<tr class="odd">
<td>There were no Custom records found that matched your query parameters.</td>
<td>User submits a query for both customized VA records and FDB records that finds only FDB records</td>
</tr>
<tr class="even">
<td><p>Your query saved successfully with name: 'x'</p>
<p>where x is the name, I assigned the query or “Unnamed Query” if I did not assign the query a name. No change</p></td>
<td>Approver saves a query</td>
</tr>
<tr class="odd">
<td>The maximum of 10 saved queries already exists. Delete a query before attempting to save.</td>
<td>User tries to save a query, but 10 queries have already been saved.</td>
</tr>
<tr class="even">
<td>Your query was successfully deleted.</td>
<td>Approver deletes a query saved by him</td>
</tr>
<tr class="odd">
<td>You cannot delete a saved query created by another user.</td>
<td>Approver tries to delete a query saved by a different user</td>
</tr>
</tbody>
</table>

<span id="_Toc100128385" class="anchor"></span>Table 33: Record Locking Pop-Up Messages

## Record Locking Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Pop-Up Messages

<table>
<caption>Shows Record Locking pop-up messages and their cause.</caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Popup Message</th>
<th>Cause</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This record is being edited by user '&lt;user id&gt;' and is unavailable for editing.</td>
<td>User clicked the 'Edit' button on the detail page. However, another user is currently editing the record.</td>
</tr>
<tr class="even">
<td>This record was recently modified by another user and is no longer current. Click 'OK' to open the current record.</td>
<td>A state change was performed on the record after the user opened it. This happens when User A opens a record in 'read only' mode while User B opens the same record, clicks the 'Edit' button, and performs a state change.</td>
</tr>
<tr class="odd">
<td>This action will cause you to lose any edits you may have made. Click 'OK' to proceed or click cancel to continue editing this record.</td>
<td>The detail page was in Edit mode and the user clicked the 'Cancel' Edit button.</td>
</tr>
<tr class="even">
<td><p><em><strong>Note:</strong></em> This message is browser-dependent.<br />
<br />
From Internet Explorer 7 (IE7): Are you sure you want to navigate away from this page? Click 'OK' to continue or cancel to stay on the current page.<br />
<br />
IE9: Are you sure you want to leave this page? (System gives option to leave this page or stay on this page)</p>
<p>Firefox: This page is asking you to confirm that you want to leave – data you have entered may not be saved. (System gives option to leave this page or stay on this page.)</p></td>
<td>User tried to navigate away from the page or closed their browser prior to clicking a state change button.</td>
</tr>
<tr class="odd">
<td>Your editing session on this page will end in one minute. To avoid losing your changes, click 'OK' to extend your editing session.</td>
<td>The detail page was in Edit mode and the user was inactive for nineteen minutes.</td>
</tr>
</tbody>
</table>

Shows Record Locking pop-up messages and their cause.

## Reports Pages Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no reports pages messages.

# Infrastructure Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA IT systems rely on various infrastructure components. These components have been defined in the Logical and Physical Descriptions section of this document. Most, if not all, of these infrastructure components generate their own set of errors. Each Component has its own sub-section and describes how errors are reported. The sub-sections are generic lists of components and are meant to be modified for each individual system.

The sub-sections are not meant to replicate existing documentation on the infrastructure component. If documentation is available online, then a link to the documentation is appropriate. Each sub-section should contain implementation specific details such as Database names, server names, paths to log files, etc.

PRE Team will work with AITC resources to resolve the Infrastructure errors. AITC will be responsible for the System, Network, and Database. PRE will provide the support as Subject Matter Expert (SME) and on PECS application.

## Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oracle monitoring tools monitor several aspects of the PECS databases. The monitory tools alert DBAs via email and create service desk tickets for conditions such as “disk full errors or tablespace full”, archive log directory full, database down, connectivity to database down, etc.

In addition, as with all Oracle databases, errors within the database are recorded in the Oracle alert log for the database and trace files that are created, which will allow DBAs to review any errors. Any such errors are emailed to the DBAs daily.

## Web Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At this Time the PECS application does not implement a Web server front end, or the WebLogic/Apache Plug-in is not being utilized officially. Apache writes output to Logs Located on the Linux web server, to the directory /var/log/httpd/, unless changed in the httpd.conf configuration file. Access to these usually requires SUDO or ROOT access.

## Application Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS application in conjunction with the WebLogic log assist in the Troubleshooting of the App or the WebLogic portal. PECS Logs are in the:

- \${DOMAIN_HOME}/PECSLogs directory, consisting of the Following Files: ct_prod.log, hibernate.log, server.log, spring.log, and struts.log.

Assistance from PECS Java Developers may be required to parse the Logs files to determine any issues.

The WebLogic application server logs reside in the:

- \${DOMAIN_HOME}/servers/\${Each_Managed_Server_name}/logs/.

There are 2 primary log files to review:

1.  \${Each_Managed_Server_name}.log
19. \${Each_Managed_Server_name}.out.

The WebLogic administrator should be able to parse these files. Assistance from PECS Java Developers may be required if out to the scope of the WebLogic Administration skill set.

## Network

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using Orion, a Solar Winds monitoring tool, AITC Service Desk and/or network engineers monitor the layer 2 and layer 3 network switches. If an alarm is generated by Orion, AITC Service Desk will create a service ticket, and then attempt to triage the problem. AITC Service Desk, which operates year-round, will notify the appropriate personnel who will triage the issue and work on the resolution.

## Authentication and Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authentication errors can be reported if user encounters errors on the SSOi login page using their PIV card or the Windows network ID.

User roles-based authorization is managed within the application using Database tables. All users have the default Requestor role.

### User SSOi Logout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user has issues with the SSOi session, then one of the following options can be used to reset the user’s SSOi session.

- The user can go to the IAM SSOi Landing page using the link and select the Logout button.

  <span class="mark">REDACTED</span> 
- The user can go to the IAM SSOi Logout page using the link. The user will be logged out of SSOi.

  <span class="mark">REDACTED</span>
- The user can go to the browser Internet Options and under the Content tab, the user can select the Clear SSL state button.

## Dependent System(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The dependent systems are those used for authentication and authorization. See [Section 2.5, Dependent Systems](#dependent-systems), for a discussion of errors.

# System Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sub-sections define the process and procedures necessary to restore the system to a fully operational state after a service interruption. Each of the sub-sections starts at a specific system state and ends up with a fully operational system.

PECS is designated as Routine Support for disaster recovery. This level of support will acquire replacement processing capacity after an AITC disaster declaration. The recovery time objective (RTO) is that it will be operational when the AITC resumes regular processing services or no later than 30 days after a disaster declaration. Data will be restored from the last backup \[recovery point objective (RPO)\].

System backups of the vapredbs1 server are performed based on the follow:

- Full backups are performed on Sundays and kept for one month. This means that at any time, there should be four full backup tapes available for each server.
- Tapes are normally dispatched offsite on Mondays.
- Differentials are run for the remainder of the week to capture daily changes.
- Differential results are sent offsite on Mondays.
- Oracle RMAN is the application used to perform full backups of the PREP database every Tuesday and Saturday morning. The tapes are retained offsite for one month. RMAN is also used to back up the control file database and archive logs to tape daily and are retained offsite for one month. The full database backups run for about 40-45 minutes. The archive log backups are shorter, at 25-30 minutes.

This section provides procedures for recovering the application at the alternate site. While Section 5.0 describes other efforts that are directed to repair damage to the original system and capabilities. Backup procedures are also defined in this section.

Procedures are outlined for each team required to complete the recovery. Each procedure should be executed in the sequence it is presented to maintain efficient operations.

The Team Leader or designee will provide hourly recovery status updates to the Austin Service Desk (ASD).

## Restart After Non-Scheduled System Interruption 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section’s instructions are identical to those found in Section 3.1, Administrative Procedures.

Software is recovered from images stored on the SAN. The same recovery procedures listed in ACP 4.1 should be followed for a return to original site restoration. An alternate site would need comparable equipment installed and would need to be able to boot from SAN for successful execution of this plan.

[^1]: At the time of development, this product was known as FDB Drug Information Framework (commonly abbreviated as FDB-DIF). The references to FDB-DIF in this manual are necessary due to previously completed code and instructions that could not be changed to match the new product name.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PREC*7*1 PECS Troubleshooting Guide

### PECS / DATUP DIF Update Logical System Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The logical system description defines the FDB-Data Information Framework (DIF) Data Update (DATUP) and PECS system components. The components are shown together because they combine to form a common goal – FDB45_DIF and FDB-Custom update distribution.

The combined logical system components are:

- DATUP – Implements the FDB45_DIF update business logic.
- Scheduler – Background process for scheduler
- WebLogic – Application server environment.
- Configuration File – Defines the DATUP configuration settings.
- Email Templates – Template emails for notifications sent to National
- Secure File Transfer Protocol (SFTP) Server – SFTP Server that hosts the FDB45_DIF update archives.
- Email Server – Email relay server.
- PECS – Implements the FDB-Custom drug business logic.
- Custom Table Staging (CTSTAGING) Database – Stores PECS FDB-Custom modifications.
- DATUP Database – Stores DATUP site update history.
- FDB45_DIF Database – Stores the FDB45_DIF drug database.

The logical system components for the National environments are illustrated below. The National components are responsible for verifying and publishing FDB45_DIF and FDB-Custom updates to the SFTP Server. The components then consume and apply the verified updates in an automated manner. Note: The PITC is not shown in the diagram, PITC will be used if there is a need for a Disaster Recovery as mentioned in section

<span id="_Ref75527734" class="anchor"></span>Figure 2: Logical System Components for the National Environments

![](prec-7-1-pecs-troubleshooting-guide/003.png)

### DATUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once per day at a configured time the DATUP automated application schedules the execution of the FDB45_DIF update process. Whether successful or unsuccessful, the process will execute again on the following day.

An automated process checks for daily updates to be applied to the PECS application. The updates are processed by an automatic scheduler that checks for available files in the *Anonymous* directory. The files may be a FDB45_DIF zip file supplied weekly by FDB or PECS customization changes in zip file format provided, when necessary, by the Release Manager within PECS. The automated process checks for updates, applies the updates, verifies completion or failure of normal executions, sends email messages, and moves files when completed.

### PECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A background process that generates FDB Comparison Reports based upon the FDB45_DIF Incremental Update file that has been received. This process needs to execute before the automated DATUP process described above.

The FDB Comparison Reports will read the incoming FDB Incremental Update file as well as the data from the FDB Database. If the concept has been customized, then a comparison of the new FDB data, existing FDB data, and customized data is produced.
