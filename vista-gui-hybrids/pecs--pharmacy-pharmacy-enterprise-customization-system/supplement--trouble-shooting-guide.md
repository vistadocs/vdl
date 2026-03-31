---
consolidated_title: "trouble shooting guide"
app_code: PECS
doc_type: SUP
master_source: "PREC*6*516 TROUBLE SHOOTING GUIDE"
master_pub_date: May 2016
consolidated_from: 2 versions
prior_versions:
  - "PREC*6.1*717 TROUBLE SHOOTING GUIDE"
---

---
title: |
  Pharmacy Enterprise Customization System (PECS)

  Troubleshooting Guide

  ![](prec-6-516-trouble-shooting-guide/001.png)
---

Version 6.0.01

May 2016

Office of Information and Technology (OIT)

Product Development (PD)

Revision History

<table>
<caption><p><span id="_Toc347930609" class="anchor"></span>Table : WebLogic Application Server</p></caption>
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
<td>03/22/2016</td>
<td><p>22</p>
<p>All</p></td>
<td>PREC*6.0*1</td>
<td><p>Update emails in section 3.3</p>
<p>508 conformance edit - <mark>REDACTED</mark></p>
<p>Updated for PECS v6.0.01 - <mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/06/2014</td>
<td>All</td>
<td>PREC*5.0*1</td>
<td><p>Updated for PECS v5.0</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
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
<tr class="even">
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
<tr class="odd">
<td>02/06/2013</td>
<td>33-37</td>
<td>PREC*3.0*1</td>
<td><p>Edited items in sections 5.1.2.1 and 5.1.4.1.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/01/2013</td>
<td>31-46</td>
<td>PREC*3.0*1</td>
<td><p>Updated document for PECS v3.0. Updated the messages in the Dose Range, Drug Pairs, Duplicate Therapy and Professional Monograph sections.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>07/13/2012</td>
<td>All; 3, 8, 9, TOC</td>
<td>PREC*2.2*1</td>
<td><p>Performed general edits; replaced figures 1 (page 3), 3 (page 8), and 4 (page 9) to match System Design Document; updated TOC.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/23/2012</td>
<td>37-48</td>
<td>PREC*2.2*1</td>
<td><p>Updated document for PECS v2.2. Updated the messages in the Single Drug Pairs, DDI, Drug Pairs Customization and Dose Range sections. Added the Record Locking section. Deleted the "user clicked the Customize button" statements from the Single Drug Pairs section.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/16/2011</td>
<td>All</td>
<td>N/A, First Release</td>
<td><p>Finalized Document</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/16/2011</td>
<td>All</td>
<td>N/A, First Release</td>
<td><p>Updated Various Sections</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/04/2011</td>
<td>All</td>
<td>N/A, First Release</td>
<td><p>Initial Draft</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

<span id="_Toc347930609" class="anchor"></span>Table : WebLogic Application Server

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
    - [Back-up & Restore](#back-up-restore)
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
    - [All Concepts](#all-concepts)
    - [Dose Range](#dose-range)
    - [Drug-Drug Interaction](#drug-drug-interaction)
    - [Drug Pair](#drug-pair)
    - [Duplicate Therapy](#duplicate-therapy)
    - [Professional Monograph](#professional-monograph)
  - [Custom Update Messages](#custom-update-messages)
    - [Error Messages](#error-messages)
  - [Query Pages Messages](#query-pages-messages)
    - [Error Messages](#error-messages-1)
    - [Informational Messages](#informational-messages)
  - [Record Locking Messages](#record-locking-messages)
    - [Popup Messages](#popup-messages)
  - [Reports Pages Messages](#reports-pages-messages)
- [Infrastructure Errors](#infrastructure-errors)
  - [Database](#database)
  - [Web Server](#web-server)
  - [Application Server](#application-server)
  - [Network](#network)
  - [Authentication and Authorization](#authentication-and-authorization)
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

This scope of this document is limited to the PECS application. Any references to external systems are only for describing an interface and how the interface and that system affects the operation of PECS, or as a tool that may be used as part of system monitoring or the support and issue resolution system.

# System Business and Operational Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS is a Graphical User Interface application used to research, review, report, and manage customization changes currently within five FDB MedKnowledge[^1] custom tables. The tables are Drug interaction, Drug Pairs, Drug Dosing, Duplicate Therapy, and Professional Monograph. The data changes performed for customizations are specific to VA patient care. The changes are different then what the vendor has provided such as the drug severity of two drugs. The change affects the information presented to the pharmacist when a drug order check is ordered on a patient.

The Pharmacy Benefits Management group (PBM) is the primary business owners of the application. They are responsible in overseeing customized changes that are necessary of overriding data table updates supplied weekly by First Data Bank.

## Operational Priority and Service Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Service Level of the system and the availability of the system are described in the Rough Order of Magnitude (ROM) it provides information to the set up and support the PRE PECS application and PRE VistA environments at ITC-Austin TX. No formal SLA is available for the PECS application.

## Logical System Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The logical view describes the architecturally significant parts of the design model. The object-oriented decomposition of the PECS application can be logically divided into three primary tiers: Presentation Tier, Business Logic Tier, and Data Persistence Tier. Each tier has its own design and implementation framework, and defined points of interaction with the other respective tiers.

The PECS application is a web-based application accessible only from within the VA network via a client workstation with a VA approved Internet browser. The PECS application’s architecture is designed and implemented according to VA architecture requirements using JEE framework. PECS is architected as an n-tier JEE application consisting of Presentation Tier, Business Logic Tier, and Data Persistence Tier. Each tier has its own design and implementation framework, and defined points of interaction with the other respective tiers.

### Presentation Tier Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The presentation tier represents the GUI screens that allow the user to interact with the application, and the logic initiated by user interaction to execute screen functionality. The presentation tier uses a well-known Model-View-Controller (MVC) design pattern implemented by the Spring MVC framework using JEE JSP pages as the “View” portion of MVC. The MVC framework is used to manage the display screens and to dispatch and delegate requests initiated by the user to a business rule processing business logic tier. The design of the MVC framework as it is used in the PECS application leverages an object hierarchy with commonly shared base classes.

### Business Logic Tier Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The business logic tier is responsible for receiving business rule processing requests from the presentation tier, or other parts of the business logic tier. It is composed of services implemented as Spring beans. Transactional integrity is ensured by using Spring managed transactions.

The main services implemented deal with creation/modification/deletion of customization requests, workflow, queries and custom update generation.

The services encapsulate the business rules governing the creation/modification/deletion of customization requests and their workflow. The services are also responsible for interfacing and abstracting the data persistence tier from the rest of the application logic.

### Data Persistence Tier Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data persistence tier is designed and implemented with the open source Hibernate framework. The Hibernate framework is an object-oriented abstraction for database CRUD operations (please see the Hibernate website for further information).

The data persistence tier interfaces with two logical Oracle databases. The first is the PECS database containing the tables and database objects necessary for the PECS application to perform Order Check customizations and track workflow status. The second is the FDB MedKnowledge database, which is the source of production Order Check data. The relevant tables in each of these databases have representative domain model objects and data access objects (DAOs) in the data persistence design.

<span id="_Toc447005113" class="anchor"></span>Figure - PECS Logical System Overview

![](prec-6-516-trouble-shooting-guide/002.png)

### DATUP DIF Update Logical System Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The logical system description defines the FDB-DIF Update DATUP and PECS system components. The components are shown together because they combine to form a common goal – FDB-DIF and FDB-Custom update distribution.

The combined logical system components are:

- FDB-DIF Update DATUP – Implements the FDB-DIF update business logic.
- Scheduler – Background process for scheduling Droid.
- WebLogic – Application server environment.
- Configuration File – Defines the DATUP configuration settings.
- Email Templates – Template emails for notifications sent to National/Local Managers.
- Secure File Transfer Protocol (SFTP) Server – SFTP Server that hosts the FDB-DIF update archives.
- Email Server – Email relay server.
- PECS – Implements the FDB-Custom drug business logic.
- CT Staging Database – Stores PECS FDB-Custom modifications.
- DATUP Database – Stores DATUP site update history.
- FDB-DIF Database – Stores the FDB-DIF drug database.
- Legacy VistA – Existing VistA server.

The logical system components for the National and Local environments are illustrated below. The National components are responsible for verifying and publishing FDB-DIF and FDB-Custom updates to the SFTP Server. The Local components then consume and apply the verified updates in an automated manner.

<span id="_Toc447005114" class="anchor"></span>Figure 2 - Logical System Components for the National and Local Environments

![](prec-6-516-trouble-shooting-guide/003.png)

## Physical System Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS is a national deployment at the Austin Information Technology Center (AITC). There is no disaster recovery site at AITC. The PECS application’s components are deployed on two servers: an application server (WebLogic) and a database server (Oracle). These servers’ characteristics are described in more detail below.

| Parameter                 | Value                                                              |
|---------------------------|--------------------------------------------------------------------|
| Central Processing Unit   | 2 CPU, x86 architecture (Intel x86 or equivalent), 2 GHz or faster |
| RAM                       | 8 GB                                                               |
| Available Hard Disk Space | 70 GB                                                              |
| RAID Configuration        | RAID 1                                                             |
| Operating System          | Red Hat Linux – Enterprise Edition Version 5.0                     |
| Mouse                     | Generic                                                            |
| Video Resolution          | 640 x 480 pixels                                                   |
| Network Interface         | dual 10 Base T or higher                                           |
| Software                  | WebLogic 12.1.1                                                    |

<span id="_Toc347930610" class="anchor"></span>Table : Oracle Database Server

| Parameter                 | Value                                                               |
|---------------------------|---------------------------------------------------------------------|
| Central Processing Unit   | 4 CPU, i386 architecture (Intel 386 or equivalent), 2 GHz or faster |
| RAM                       | 16 GB                                                               |
| Available Hard Disk Space | 150 GB                                                              |
| RAID Configuration        | RAID 1                                                              |
| Operating System          | Red Hat Linux v 5.0                                                 |
| Mouse                     | Generic                                                             |
| Video Resolution          | 640 x 480 pixels                                                    |
| Network Interface         | dual 10 Base T or higher                                            |
| Fiber Channel Interface   | dual Host Bus Adapters                                              |
| Database                  | Oracle 10 g                                                         |

<span id="_Toc347930611" class="anchor"></span>Table : Software Components for the FDB-DIF Update DATUP

PECS is deployed at the national level as a single application server node connected to a database server.

<span id="_Toc447005115" class="anchor"></span>Figure 3 – PECS Deployment

![](prec-6-516-trouble-shooting-guide/004.png)

<span id="_Toc447005116" class="anchor"></span>Figure : - PECS Deployment, Continued

![](prec-6-516-trouble-shooting-guide/005.png)

## Software Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS application conforms to the VA’s requirements determining the use of third party tools. Please refer to the PECS Product Architecture Document for reference. See the PECS TSPR site: <span class="mark">REDACTED</span>

The three-tiered architecture, which consists of an Internet browser-based graphical user interface accessing a Spring MVC-based web application/presentation tier, a Java Enterprise Edition (JEE)-based business logic service processing layer, and a Hibernate-based data access tier, conforms to the design recommended by the Health Systems Design & Development (HSD&D) Core Specifications for Re-hosting Initiatives and generally acceptable JEE implementation recommendations.

PECS is a JEE application, conforming to version 1.4 of the specification. It is deployed on WebLogic 12.1.1. It makes use of the following third party frameworks: Spring 4.1.5, Hibernate 4.3.8, and Log4j 1.2.17. As mandated by the VA, PECS employs Kernel Authentication & Authorization for J2EE (KAAJEE) 1.1.0.007 for user authentication and authorization. KAAJEE, in turn, uses SDS 17.0 and VistALink 1.6.

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

<span id="_Toc347930612" class="anchor"></span>Table : System Automation Dependencies

### Background Processes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several background processes that run on the PECS production and pre-production servers.

At 7:00 a.m. each morning, a job runs to alert DBAs to service accounts with passwords that will expire in the next 15 days.

Also at 7:00 a.m., a job runs to purge trace files, log files older than a set parameter.

At 5:00 a.m., a daily job runs to move audit logs that need to be kept longer to a more permanent location.

At 6:00 a.m., a job runs to move old alert logs to a backup directory and start a new log for each day to make troubleshooting and maintenance easier and to free up space for customer data.

Every night at 11:00 p.m., a job runs to gather statistics on each table which are used by the Oracle optimizer to choose data access paths for peak performance.

A weekly job runs on Sunday to monitor space usage and allow database and system administrators to do capacity planning. A weekly job runs on Thursdays to verify/monitor privileges held by users for security and DBA review.

Backup jobs that run in background are described in section 3.4.

- Oracle for managing the table
- KAAJEE for security and time out
- DATUP Background Process
- PECS Background Process

The CommonJ Scheduler runs in the background. It maintains the update schedule and fires after the configured timer has expired.

### Job Schedules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the job scheduling for DATUP and PECS.

DATUP

The DATUP automated application schedules the FDB-DIF update process to execute at a configured time once per day. Whether successful or unsuccessful, the process will execute again on the following day.

An automated process checks for daily updates to be applied to the PECS application

The process update is processed by an automatic scheduler that checks for available files in the *Anonymous* directory. The files may be an FDB-DIF zip file supplied weekly by FDB or PECS customization changes in zip file format provided when necessary by the Release Manager within PECS.

The automated process automatically checks for updates, applies the updates, verifies completion of failed or normal executions, sends email messages, and moves files when completed.

PECS

PECS v2.2 introduced a background process that generates FDB Comparison Reports based upon the FDB-DIF Incremental Update file that have been received. This process needs to execute before the DATUP automated process described above.

The FDB Comparison Reports will read the incoming FDB Incremental Update file as well as the data from the FDB Database. If the concept has been customized, a comparison of the new FDB data, existing FDB data, and customized data is produced.

## Dependent Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS depends on VistA for user authentication and authorization. That a consequence of the use of KAAJEE which employs VistALink to authenticate users with VistA. In addition, it also needs an SDS instance to provide institution information. KAAJEE uses an Oracle database to temporarily store user information.

<span id="_Toc447005117" class="anchor"></span>Figure - Dependent System

![](prec-6-516-trouble-shooting-guide/006.png)

| Dependency Name            | Location                    | Function                                                  | Interface Method             |
|----------------------------|-----------------------------|-----------------------------------------------------------|------------------------------|
| FTP Server over SSH (SFTP) | VA Internal                 | Stores FDB-DIF and FDB-Custom archives (ZIP files).       | FTP Protocol over SSH (SFTP) |
| Email Server               | VA Internal                 | Transmits notification email to configured mailing lists. | SMTP Protocol                |
| Java Messages Service      | WebLogic Application Server | Transmits messages from Local Sites to National.          | JMS Protocol                 |
| VistA                      | VA Internal                 | Vista access to PECS                                      | WEB                          |
| KAAJEE                     |                             | Security                                                  |                              |
| CMOP                       | CMOP                        | Transmit FDB DIF full and incremental zip files           | FTP Protocol over SSH (SFTP) |

<span id="_Toc347930613" class="anchor"></span>Table : WebLogic Pre-Prod Steps

# Routine Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS requires Oracle support for the FDB-DIF and CT staging tables by a database administrator. It also requires the understanding of Linux and WebLogic.

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

<span id="_Toc347930614" class="anchor"></span>Table : WebLogic Production Steps

| Name                        | Directory/Path                                                |     |
|-----------------------------|---------------------------------------------------------------|-----|
| WebLogic Install Directory  | /u01/app /bea                                                 |     |
| Domain Directory            | /u01/app /bea/user_projects/domains/pecs-prod                 |     |
| Admin Server Startup Script | /u01/app/bea/user_projects/domains/pecs-prod/startWebLogic.sh |     |
| Node Manager Startup Script | /u01/app /bea/wlserver_10.3/server/bin/startNodeManager.sh    |     |
| Managed Server Startup      | From Admin Console: pecs_ms1, peps_ms1                        |     |

<span id="_Toc347930615" class="anchor"></span>Table : Role-based Security Keys

1.  Login to server as your user and become the WebLogic user:

> i.e.*: sudo su - weblogic*

2.  See the previous table to identify the script you wish to run for starting the Admin Server or a Node Manager. When running a script, preface all startup scripts with the *nohup* command and place in the background.

i.e.: Starting the Admin Server

> *cd /u01/appbea/user_projects/domains/pecs-\

> *nohup ./startWebLogic.sh &*

i.e.: Starting a Node Manager

> *cd /u01/app/bea/wlserver_10.3/server/bin*

> *nohup ./startNodeManager.sh &*

Login to the WebLogic GUI Admin console with your LAN ID, if this does not work, check the Password Vault for the environment and use the specified account.

Start the requested Managed Servers.

### System Shut-down

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application is first taken offline by the application admin and advises the team. The DBA takes the DB offline and advises the team. The SA will run “ps –ef” to identify any hung WebLogic or Oracle processes prior to shutdown/reboot of the servers.

If the server is up and the database is up but needs to come down for maintenance on the database or server, the script on the database server, vapredbs1, in the directory, /u01/oracle/admin/PREP/scripts, is a shutdown\_ script which can be run by the Oracle Unix user to shut down any database on the server. It is called from that directory as ./shutdown_db.ksh \<database_name\>, i.e., ./shutdown_db.ksh PREP.

1.  Login to the WebLogic GUI Admin console with your LAN ID, if this does not work, check the Password Vault for the environment and use the specified account.

> Select all the servers including Admin server and shut them down.

2.  Login to server as your user and become the WebLogic user:

> i.e.: sudo su – weblogic

> Kill \<nodemanager PID\>

3.  Verify if all the servers are stopped.

> i.e. ps –ef \| grep java, should not see any WebLogic instances.

### Back-up & Restore 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this section, a high-level description of the systems back-up and restore strategy is elaborated.

Back-up Procedures

All servers are backed up under the AITC Enterprise Backup solution.

The PRE servers are back up policy are as follow;

- Differentials run Mon-Thurs – three-week retention.
- Full backup run on Fridays – three-month retention

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

The database server, vapredbs1, is backed up for a system backup each weekend to tape and the tapes are retained for a month.

Oracle RMAN software is used to perform full backups of the PREP database each Tuesday and Saturday mornings. The tapes are retained offsite for 1 month. RMAN is also used to backup archive logs and the database control file to tape daily and are also retained offsite for a month. The full database backups run for about 40-45 minutes. The archive log backups are shorter, about 25-30 minutes.

Restore Procedures

Recover Disk Layout and OS Version

1.  Refer to one of the following for a filesystem layout:
1.  [cfg2html reports](http://vaaacmul11.aac.va.gov/cfg2html/)
2.  Filesystem report stored in /opt/ops/hosts.reports/\<hostname\>.fs.txt on <span class="mark">REDACTED</span>
3.  Restore /opt/ops/\<hostname\>.fs.txt to /tmp/ on <span class="mark">REDACTED</span>.
2.  Refer to one of the following to determine which RedHat version to install:
1.  [cfg2html reports](http://vaaacmul11.aac.va.gov/cfg2html/)
2.  Cfg2html output stored in /opt/cfg2html on <span class="mark">REDACTED</span>
3.  RedHat release report stored in /opt/ops/hosts.reports/\<hostname\>.release.txt on <span class="mark">REDACTED</span>
4.  Restore /etc/redhat-release to /tmp/ on <span class="mark">REDACTED</span> .

> Build server using STK image server

1.  [STK image server](http://vaaacmul13.aac.va.gov/KickStart/)

> Install Netbackup client

1.  [NetBackup Client setup document](http://vaaacmul11.aac.va.gov/docs/netbackup.client.setup.txt)

Rebuild User Accounts

1.  Request NetBackup administrator to restore following files:
1.  /home
2.  /etc/passwd
3.  /etc/shadow
4.  /etc/group
5.  /etc/gshadow
2.  Run pwck to verify password files
3.  Run grpck to verify group file

Restore Customized Configuration Files and User Directories

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
2.  Restart following services:
- snmpd
- sendmail
- httpd
- syslog
- nptd
- multipathd

Install 3rd Party Software

Once the server, vapredbs1 is restored from tape, including /etc, /var and /u01 with the Oracle software have been restored from tape, the database can be restored using RMAN. The script to do this should have been restored to the /u01/oracle/admin/PREP/rman directory and is called rman_restore_db_from_tape.ksh. It must be run as the Oracle Unix user with the latest full backup of the database in the tape device and the database name as a parameter.

Back-up Testing

At the Program Manager’s discretion, random files can be selected to be restored to an alternate location.

Currently, there is no restore testing. The DBA team has requested an extra server to user for this purpose and will implement testing procedures when this server is purchased by AITC.

Storage and Rotation

Full Backups are performed on Sundays and kept for a month. This means that at any time, we should have 4 full backup tapes available for each server. Tapes are normally dispatched offsite on Mondays.

Differentials are run for the remainder of the week to capture daily changes and are sent offsite on Mondays.

These are the files that we backup on vapredbs1:

- /
- /boot
- /home
- /opt
- /usr
- /var
- /u01

Schedule:

- Diff Mon-Thurs 3 week retention
- Full Fri 3 months retention

## Security / Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security used is - KAAJEE.

KAAJEE document webpage: <span class="mark">REDACTED</span>

Document used from this page is the Installation Guide & Release Notes 1.0.1 (WebLogic 8.1)

The PECS application is only accessible by users signed directly into the VA network, or by users signed into the VA network via the RESCUE client. User authentication into the VA network is a precondition of PECS application access. Application authentication and authorization will be controlled by the VA KAAJEE security API.

In order to log into the application, each user must have a valid VistA account, at a local or national facility, since KAAJEE delegates user authentication to VistA. At the application’s login screen, users will be prompted for their access and verify codes and will be allowed to select the VistA instance which issued their credentials.

<span id="_Toc447005118" class="anchor"></span>Figure - KAAJEE Application Overview

![](prec-6-516-trouble-shooting-guide/007.png)

### Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AITC utilizes VA Form 9957 for the creation, modification, and deletion of accounts. The request is approved by the Program Manager or his or designated representative. The 9957 request also identifies the servers and the level of access to be granted.

Users are verified for access to PECS by the current VA VistA system. New users must be created in VistA to have access to PECS and the PREP database using form 9957 which must be completed by a functional group manager and sent to security to review. Once it is reviewed and approved by security, it is sent to the AITC group who administers VistA to add the user. VistA administrators are in a separate group within AITC from the database and system administrators.

Security reviews of the application and database are performed after each upgrade and after quarterly security database patches are applied to verify access is limited to approve users. Any issues found at the application level, VistA level, or Database level must be remediated within a week to 30 days depending on the level of the issue.

Identity Management is done through VistA Link. We will have one connection configured for each VistA site and the user management is done at each local VistA site.

Authorization is handled through the use of specific VistA security keys. PECS does not assign individual permissions to users. Instead, it defines a number of roles for its users (requestor, approver, release manager, and administrator) and associates a set of permissions with each of them. These roles are mapped to security keys as follows.

| PECS Role       | VistA Security Key          |
|-----------------|-----------------------------|
| Requestor       | PSS_CUSTOM_TABLES_REQUESTOR |
| Approver        | PSS_CUSTOM_TABLES_APPROVER  |
| Release Manager | PSS_CUSTOM_TABLES_REL_MAN   |
| Administrator   | PSS_CUSTOM_TABLES_ADMIN     |

<span id="_Toc347930616" class="anchor"></span>Table : Role-based Application Screens and Permitted Operations (Several Tables)

Depending on the permissions needed by a user, the appropriate role is determined, and the corresponding key assigned to their account. The user provisioning process is part of the VistA system and is thus not documented here. Password changes, account activation/inactivation etc. must be performed through VistA. Refer to the appropriate documentation for details on user account management.

### Access Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A password aging script is used to identify accounts for which passwords have not been changed with 90 days. Accounts are automatically locked if they are not changed at the end of the 90 day period. Accounts are removed after 180 day and a new 9957 will need to be submitted if the user still requires access. Passwords cannot be changed within the first 7 days. Passwords have a minimum length of 8 characters and locked.

Passwords must meet the VA security policy including being at least 8 characters long with alpha, numeric, special characters, and mixed case, and must be changed every 90 days. Userids are only granted to VA employees who have already been granted VA network ids.

WebLogic console admin username and passwords are saved in Password Vault and its accessible only by WebLogic admin group.

Temporary or read only access can be provided to development or operational teams through the WebLogic security realms if required.

The purpose of this screen is to provide an authorized user access to the system. The user must enter their valid, assigned/designated Access Code and Verify Code using this screen. The Access Codes and Verify Codes are stored in and validated against the VistA Link system via the KAAJEE interface. The system will validate or authenticate the data entered by the user and, if it is valid, allow the user access to the PECS application. The maintenance of the user account and password information is part of the VistA system and is thus not documented here. Refer to VistA documentation for details on the user account maintenance.

If the response from the authentication request is successful via the KAAJEE API, KAAJEE will return a user profile object which will be used by the application to determine the user's role(s) and permissions. On successful login, the system transfers (navigate) the user to the Home page of the application.

It should be noted that the authentication mechanism used by the KAAJEE API is “Form” based authentication. This type of authentication is configured in and enforced by the application server. A login form page is specified within the application configuration deployment descriptor which tells the application server what page within the application is to be used for authentication. When a request for login is received by the application server, the server knows to display this form. If a user session times out and the user subsequently requests an application link or resource, the application server will forward requests to the page specified as the login form first.

Within the PECS application, if the user session times out the application server will forward the user to the login page, then it will redirect the user to accept the confidentiality statement. Once the confidentiality statement is accepted, the user will be redirected to the application home page. The confidentiality statement must be accepted at least once per user session.

A user’s role will determine the screens and operations that will be accessible. The table below details presents a security the matrix.

Menu Tab

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

Home Page

|                                   | Type  | Requester | Approver | Release Manager | Administrator |
|-----------------------------------|-------|-----------|----------|-----------------|---------------|
| My Request History                | Panel | X         | X        |                 |               |
| My Assigned Requests for Review   | Panel |           | X        |                 |               |
| My Assigned Requests for Approval | Panel |           | X        |                 |               |
| My Assigned Requests for Deletion | Panel |           | X        |                 |               |
| Unassigned Requests               | Panel |           | X        |                 |               |
| All Requests                      | Panel |           | X        |                 |               |

Advanced Query/Customization/My Queries

|                   | Type   | Requester | Approver | Release Manager | Administrator |
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

Advanced Query/Customization/Other User’s Queries

|                   | Type   | Requester | Approver | Release Manager | Administrator |
|-------------------|--------|-----------|----------|-----------------|---------------|
| Run A Saved Query | Panel  | X         | X        | X               | X             |
| Query Result      | Panel  | X         | X        | X               | X             |
| Load              | Button | X         | X        |                 |               |

Custom Updates

|                          | Type   | Requester | Approver | Release Manager | Administrator |
|--------------------------|--------|-----------|----------|-----------------|---------------|
| Download Existing Update | Link   |           |          | X               |               |
| Create New Update        | Button |           |          | X               |               |

Administration

|                        | Type   | Requester | Approver | Release Manager | Administrator |
|------------------------|--------|-----------|----------|-----------------|---------------|
| Save                   | Button |           |          |                 | X             |
| Cancel                 | Button |           |          |                 | X             |
| Null Drug Pair Removal | Button |           |          |                 | X             |

## User Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User standard CDCO procedures for ANR, etc.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step 1</strong></th>
<th><p>Send out email to:</p>
<p>VA IT SDE EO EAS PEC SUSTAINMENT &lt;<mark>REDACTED</mark>&gt;</p>
<p>PD PEC Team &lt;<mark>REDACTED</mark>&gt;</p>
<p>VHAPBH NDF Support Group &lt;<mark>REDACTED</mark>&gt;</p>
<ol type="a">
<li><blockquote>
<p>Subject: Per CO or ANR xxxxx AITC will bring down &lt;ENV&gt; to perform maintenance at hh:mm AM/PM CST</p>
</blockquote></li>
</ol>
<ol start="4" type="a">
<li><blockquote>
<p>Email line1: Per CO or ANR xxxxx AITC will bring down &lt;ENV&gt; to perform scheduled maintenance at hh:mm AM/PM CST</p>
</blockquote></li>
<li><blockquote>
<p>Email line2: AITC will send out notice once the &lt;ENV&gt; is back online and ready for smoke test.</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Step 2</strong></td>
<td><p>Login to the WebLogic GUI Admin console with your LAN ID; if this does not work, check the Password Vault for the environment and use the specified account.</p>
<p>Shutdown the requested Managed Servers or Clusters as listed in the Change Order or Service Request.</p></td>
</tr>
<tr class="even">
<td><strong>Step 3</strong></td>
<td><p>Verify maintenance/deployment completed</p>
<p>Start the requested Managed Servers or Clusters as listed in the Change Order or Service Request.</p></td>
</tr>
<tr class="odd">
<td><strong>Step 4</strong></td>
<td><p>Send out email to:</p>
<p>VA IT SDE EO EAS PEC SUSTAINMENT &lt;<mark>REDACTED</mark>&gt;</p>
<p>PD PEC Team &lt;<mark>REDACTED</mark>&gt;</p>
<p>VHAPBH NDF Support Group &lt;<a href="mailto:NDFsupportGroup@med.va.gov"><mark>REDACTED</mark></a>&gt;</p>
<ol type="a">
<li><blockquote>
<p>Subject: Per CO or ANR xxxxx AITC has successfully completed &lt;ENV&gt; maintenance at {time} CST.</p>
</blockquote></li>
</ol>
<ol start="6" type="a">
<li><blockquote>
<p>Email line1: Per CO or ANR xxxxx AITC has successfully completed &lt;ENV&gt; maintenance at {time} CST.</p>
</blockquote></li>
<li><blockquote>
<p>Email line2: &lt;ENV&gt; is back online and ready for smoke test.</p>
</blockquote></li>
<li><blockquote>
<p>Email line3: Please update this thread with test results and any outstanding issues.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

System downtime due to application or system software upgrades will be planned with AITC. Users will be notified by PRE using the appropriate mailing lists. The notice will be provided at least two hours in advance. Notification will also be provided when the application becomes available again.

## System Monitoring, Reporting, & Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oracle Enterprise Manager and Grid Control are used to monitor availability and performance of the PECS database on the vapredbs1 server. Standard AITC thresholds are set for space monitoring, availability of the database, and network connectivity. Database administrators are alerted immediately if the monitoring tool detects a problem. In addition, if connectivity to the database fails, an incident ticket is created in the User Service Desk software and relayed to AITC management and the primary and secondary database administrator for the project.

System monitoring is done through the following:

1.  WebLogic console
3.  VistA link console
4.  Introscope
5.  CEM
6.  Xpolog

### Availability Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  WebLogic console has the entire WebLogic environment configuration.
1.  We can monitor the admin server, node manager and managed servers running states, and control managed servers start and stop activity.
2.  Manager servers health and performance, application deployment state, database connection pools, and JMS can also be monitored from here.
2.  VistA link console has the VistA sites connection information.  
    It gives the ability to add, edit, update, and check the status of each connection configured.
3.  Introscope: Monitoring tool. One agent per machine is deployed and it can provide in detail monitoring of all the WebLogic components from that environment. And monitoring alerts and notifications can be generated using this tool.

### Performance/Capacity Monitoring 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patrol is utilized by AITC to capture Performance and Capacity activities.

It can monitor the http traffic coming from internet cloud to AITC.

## Routine Updates, Extracts and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The third Monday of each month, data is exported from the PREP production database, and imported into the pre-production database, PREY, and to the SQA database so testers can work with updated data.

The PECS application receives weekly data updates from the COTS vendor that affects the Oracle tables. The updates are applied automatically using DATUP. This same DATUP process is used whenever a released customized file is created from the PECS application. Refer to PECS_FDB-DIF_Custom_Data_Update_Process document that explains the details steps and process contained within the automation.

## Scheduled Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, there is no scheduled maintenance window for PRE. This will be needed in the future so AITC has a window to do server patching, etc.

Any normal changes that are initiated by the PRE team will come in a Request for Change form to the AITC Build Manager. These requests will be submitted by 12:00pm CST on Friday for a Monday implementation in the Pre-Production environment. Production requests must be received by 12:00pm on Tuesday for implementation on Wednesday. Emergency change requests will be implemented as soon as possible.

## Capacity Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Initial Capacity Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial Capacity Planning for Storage was done by PRE and Enterprise Infrastructure Engineering (EIE) team as per the Application requirement. Subsequently, it was decided in concurrence with AITC Architect to add HBA cards to the Servers, so as PRE Servers have access to Storage Area Network (SAN) storage. The SAN storage will be used to expand the storage capacity for future use as needed.

# Exception Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section presents a list of possible exceptions/errors that may occur during normal operation.

## Routine Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system validates form field values per business rule and data integrity constraints before the form is submitted for processing. If values do not pass user interface validation, the user is redirected back to the wizard form and a message is displayed informing the user of the corrections needed. Please see Alternative Flows for data validation errors.

The system receives the value after form validation and applies the appropriate business rules (if any) to the value. Examples of a business rule validation may include bounds checking, or any interdependencies that may exist between two data values. Please see Alternative Flows for data validation errors.

Like most systems, PECS may generate a small set of error that may be considered “routine”. These errors are routine in the sense that they have minimal impact on the user and do not compromise the operational state of the system. Most of the errors are transient in nature and only require the user to retry an operation. The following sub-section describes these errors, their causes, and what response, if any, an operator needs to take.

While the occasional occurrence of these errors may be routine, getting a large number of an individual errors over a short period of time is an indication of a more serious problem. In that case the error needs to be treated as an exceptional condition.

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security is addressed at design tiers respective of the security requirement. Security authentication and authorization is provided by the KAAJEE security API and is abstracted by the services layer of the application.

The DATUP subsystem does not provide or enforce a security model. However, the system does access other system interfaces which may encounter security violations when accessed. The following known security errors may occur:

1.  Access to FTP denied – The configured FTP Protocol over SSH (SFTP) account username and/or password is incorrect. To resolve this, the FDB-DIF Update DATUP configuration file should be modified to include the correct access information.
2.  Access to Email denied – The configured email account username and/or password is incorrect. To resolve this, the FDB-DIF Update DATUP configuration file should be modified to include the correct access information.
3.  Access to FDB-DIF denied – The configured JDBC driver URL, driver name, username, and/or password is incorrect. To resolve this, the FDB-DIF Update configuration file should be modified to include the correct access information.
4.  Access to “temporary” directory denied – The WebLogic process does not have sufficient permission to write to the operating system defined temporary directory (e.g., “/tmp”). To resolve this, the WebLogic process should be granted write access to the temporary directory.

### Time-outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Time out may occur when accessing third party Database. Sometimes queries are dependent upon the availability of the database or run out of time if a large results query is requested.

The following process has a known potential timeout in the DATUP subsystem:

> Java Messaging Service – A Local JMS send will timeout if it is unable to connect to the National JMS server. To resolve this, the National WebLogic server port should be made accessible from the Local site.

### Concurrency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No information at this time.

## Significant Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant errors can be defined as errors or conditions that affect the system stability, availability, performance, or otherwise make the system unavailable to its user base. The following sub-sections contain information to aid administrators, operators, and other support personnel in the resolution of errors, conditions, or other issues.

### Application Error Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS uses the Apache Log4j framework for logging. Log files are accessible to authorized users through the web-based Xpolog tool.

Logs location - /u01/app/bea/user_projetcs/domains/pecs-\<Env\>/ vistALink_Folder/logs/

> Maxfilesize=10000KB

> Max. backed up files are 10.

> Growth rate =

# Application Error Messages and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter lists all PECS error, informational, and warning messages and describes what caused them to display. In cases where the support team needs to be contacted, there will usually be a "please contact the support team" statement within the message.

## Customization Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the messages that could appear when a user customizes a Drug-Drug Interaction, Drug Pair, Dose Range, Duplicate Therapy, or Professional Monograph FDB record.

### All Concepts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the error, informational, and warning messages that can appear for all concepts. If the support team needs to be notified, the statement to notify them is highlighted in yellow.

Error Messages

This section lists the error messages that can appear for all concepts.

| All Concepts Error Message                                                                                                                                                               | Cause                                                                                                                                 |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Current Action Reason field is required                                                                                                                                                  | User didn’t fill out the ‘Current Action Reason’ field.                                                                               |
| Action 'Submit as Reviewed' cannot be performed on modified records. Please click the 'Modify' button after changing fields. Field '\<name of field\>' cannot be changed for this action | Approver modifies an FDB field on a custom record in the Modified or Deleted action status and clicks the 'Submit as Reviewed' button |
| Action 'Submit for Delete' cannot be performed on modified records. Please click the 'Modify' button after changing fields. Field '\<name of field\>' cannot be changed for this action  | Approver modifies an FDB field on a custom record in the Approved or Deleted action status and clicks the 'Submit for Delete' button  |

Informational Messages

This section lists the informational messages that can appear for all concepts.

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
| This reviewed record has been rejected. The record has returned to previous action status (‘Deleted’).           | Approver clicked the 'Submit as Reviewed' button on a custom record in the Deleted action status and then, the user clicked the 'Reject' button.‘                                                                         |
| This request for modification has been rejected. The record has returned to previous action status (‘Approved’). | Approver modified an FDB field on a custom record in the Approved action status and clicked the 'Modify' button and then, the user clicked the 'Reject' button.                                                           |
| This request for modification has been rejected. The record has returned to previous action status (‘Deleted’).  | Approver modified an FDB field on a custom record in the Deleted action status and clicked the 'Modify' button and then, the user clicked the 'Reject' button.                                                            |
| To update the record, click the edit button below.                                                               | User has entered the detail page for one of the concepts. (When a user first enters a detail page, it will be in read-only mode. The only way a user will be able to update the detail page is to click the Edit button.) |

### Dose Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the Dose Range error, informational and warning messages.

Error Messages

This section lists the Dose Range error messages.

<table>
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
<td><p>Unable to perform field validation due to: "+ex.getMessage());</p>
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
<td>Either the user enters a value for Age High in Days field that is greater than 10 numeric characters or the user enters a non-numeric value.</td>
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
<td>User modifies a record that has a blank units field for a corresponding field containing a numeric value. For example, the 'Dose Low' field contains a number with no corresponding dose low units.</td>
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
<td>User enters a non-numeric value in the Max Single Not to Exceed (NTE) Dose field</td>
</tr>
<tr class="odd">
<td>MAXSINGLENTEDOSEFORM field must be numeric</td>
<td>User enters a non-numeric value in the Max Single NTD Dose Form field</td>
</tr>
<tr class="even">
<td>MAXSINGLENTEDOSE field must be a number up to 10 digits including a maximum of six digits to the right of the decimal point</td>
<td>User enters a value that is more than 10 digits or has more than 6 digits after the decimal point in the Max Single NTE Dose field</td>
</tr>
<tr class="odd">
<td>MAXSINGLENTEDOSEFORM field must be a number up to 10 digits including a maximum of six digits to the right of the decimal point</td>
<td>User enters a value that is more than 10 digits or has more than 6 digits after the decimal point in the Max Single NTE Dose Form field</td>
</tr>
<tr class="even">
<td><p>'x' field cannot be blank when 'y' field has numeric value</p>
<p>Where x = the NTE unit field (MAXSINGLENTEDOSEUNIT or MAXSINGLENTEDOSE FORMUNIT)</p>
<p>y = the NTE dose field (MAXSINGLENTEDOSE or MAXSINGLENTEDOSEFORM)</p></td>
<td>User enters a value for the Max Single NTE Dose or Max Single NTE Dose Form field but leaves the corresponding units field blank (Max Single NTE Dose Unit or Max Single NTE Dose Form)</td>
</tr>
</tbody>
</table>

Informational Messages

Dose Range informational messages are in the All Concepts Informational Messages section.

Warning Messages

This section lists the Dose Range warning messages.

| Dose Range Detail Page Warning Message                                                                                                                | Cause                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| A request for customization exists for this dosing concept id: x submitted by: y, updated on z. See below for the duplicate VA custom record details. | User selects an FDB record to customize for which a VA custom record already exists |

### Drug-Drug Interaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the Drug-Drug Interaction error, informational and warning messages.

Error Messages

This section lists the Drug-Drug Interaction error messages.

<table>
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
<td>User doesn't input a value into the ‘Interaction Description' field.</td>
</tr>
<tr class="even">
<td>Interaction Description field is invalid; it must contain two drug names separated by a forward slash/</td>
<td>User inputs more than one forward slash (/) when entering a value into the Interaction Description field.</td>
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
<td>An FDB record cannot be retrieved from the FDB database for the given interaction id when selected for customization or a VA record cannot be retrieved from the staging database for the given id when selected for modification because the interaction id is invalid or inactive or deleted.</td>
</tr>
<tr class="odd">
<td><p>The specified VA Custom interaction ID has errors.</p>
<p>Please report this error to the support team.</p></td>
<td>User selects a DDI VA record to modify; however, the customized VA record cannot be found in the database for the given interaction id. This error displays in the VA table results area and the detailed page doesn’t get loaded.</td>
</tr>
</tbody>
</table>

Informational Messages

This section lists the DDI informational messages.

<table>
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
<p>Click on the DrugPairs button to add drug pairs to the interaction.</p></td>
<td>The custom DDI record in the New, Reviewed, or Modified (after Delete) action status does not have any drug pairs associated with it.</td>
</tr>
<tr class="odd">
<td>The associated drug pairs are not all reviewed yet. To submit this interaction as reviewed, you must review all associated drug pairs. First click on the Drug Pairs button then take appropriate action.</td>
<td>The drug pairs associated with the DDI custom record are not all in the Reviewed action status. They may all be in the 'New' action status or some of them may be 'New' while others are in the 'Reviewed' action status.</td>
</tr>
<tr class="even">
<td>The associated drug pairs are not all approved as yet. To approve the interaction, you must approve all the associated drug pairs first. Click on the Drug Pairs button to view and approve the associated drug pairs.</td>
<td>The drug pairs associated with the DDI custom record are not all in the Approved action status. They may all be in the 'Reviewed' action status or some of them may be 'Reviewed' while others are in the 'Approved' action status.</td>
</tr>
<tr class="odd">
<td>Click on the Drug Pairs button to add or remove drug pairs to the interaction.</td>
<td>Approver modified an FDB field on a custom record in the Approved action status and clicked the 'Modify' button.</td>
</tr>
<tr class="even">
<td>The associated drug pairs are all in the rejected state.</td>
<td>The drug pairs associated with a DDI custom record are all in the Rejected action status.</td>
</tr>
<tr class="odd">
<td>The associated drug pairs are not all rejected or deleted yet. You must click on the Drug Pairs button then take appropriate action.</td>
<td>Approver rejected a DDI custom record in the Reviewed action status while its drug pairs were still in the Approved action status.</td>
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

Warning Messages

This section lists the DDI warning messages.

| Drug-Drug Interaction Warning Messages                                                                                              | Cause                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The interaction ‘\<Drug A/Drug B\>’' is already customized with severity 'x'. See below for the duplicate VA custom record details. | User requests an FDB customization and changes the Severity Level Code. However, there is already an existing custom VA record at the requested severity level. For example, a requestor selects an FDB record to customize from severity level code 3 to 2. But there is already an existing custom VA record created from this FDB record at severity level 2. |

### Drug Pair

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Messages on the Drug Pair Customization Page

Error Messages

This section lists the Drug Pair Customization Page error messages.

<table>
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
<td>On the Drug Pair Customization page accessed by the ‘Drug Pair’ button on the drug-drug interaction customization detail page, user adds a drug pair to a Drug-Drug interaction by selecting a pair of routed generic drugs in which both drugs in the pair are the same drug.</td>
</tr>
<tr class="even">
<td>Unable to perform the save operation on the customization. (Drug pairs cannot be added to a deleted interaction)</td>
<td>On the Drug Pair Customization page accessed by the ‘Drug Pair’ button on the drug-drug interaction customization detail page for a Drug-Drug interaction with a Deleted or Delete Reviewed action status, user tries to add a drug pair.</td>
</tr>
<tr class="odd">
<td>Unable to perform the save operation on the customization. (Field 'Current Action Reason' is required)</td>
<td>User adds a drug pair to a Drug-Drug interaction without entering a current action reason by either adding an FDB drug pair or selecting a pair of routed generic drugs.</td>
</tr>
<tr class="even">
<td>Enter values in text boxes below and click 'Customize' to add drug pairs to interaction.</td>
<td>When using the ‘Drug Pair’ button on the drug-drug interaction customization detail, user chooses to expand the option to ‘Select Drug Pairs to add to the above VA Custom Interaction page</td>
</tr>
<tr class="odd">
<td>Select from list of FDB drug pairs - note that at least one drug pair must be chosen before clicking the Customize button.</td>
<td>When ‘Drug Pair’ button on the drug-drug interaction customization detail page, user chooses to select a drug pair to add to the custom drug-drug interaction by selecting an FDB drug pair</td>
</tr>
<tr class="even">
<td>Select from list of Generic drug pairs - note that a drug pair must be chosen before clicking the Customize button. Routed Generic #1 and Routed Generic #2 fields cannot be the same value. Routed Generic #1 and Routed Generic #2 must follow the same order as the Interaction Description.</td>
<td>When using the ‘Drug Pair’ button on the drug-drug interaction customization detail page, user chooses to select a drug pair by selecting from routed generic drug lists</td>
</tr>
<tr class="odd">
<td>Either no drug pairs exist for this custom interaction or there are no drug pairs for the current Action Status filter. Please update the Action Status filter or create new custom drug pair(s) for this interaction by clicking on ‘Select Drug Pairs to add to the above VA Custom Interaction’.</td>
<td>On the Drug Pair Customization page accessed by the 'Drug Pair' button on the DDI Detail page, the user chooses to view and/or edit associated drug pairs when either the DDI has no associated drug pairs or there are no drug pairs for the Action Status filter that was selected.</td>
</tr>
<tr class="even">
<td>Select/Deselect All Drug Pairs Displayed from VA Custom Interaction</td>
<td>On the Drug Pair Customization page accessed by the ‘Drug Pair’ button on the drug-drug interaction customization detail page for a Drug-Drug interaction, user chooses to view and/or edit associated Drug-Drug pairs.</td>
</tr>
<tr class="odd">
<td><p>Now showing x of y total records.</p>
<p>Where x is the number of associated drug pairs filtered to display and y is the total number of associated drug pairs.</p></td>
<td>On the Drug Pair Customization page accessed by the ‘Drug Pair’ button on the drug-drug interaction customization detail page for a Drug-Drug interaction, user chooses to get a count of the displayed and total associated drug pairs.</td>
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

Messages on the Drug Pair Lookup Query Page

Error Messages

<table>
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
<td><p>The Drug-Drug interaction ‘x’ has not been customized. You must customize the Drug-Drug interaction prior to customizing the Drug-Drug pair.</p>
<p>Where x is the selected interaction id and interaction id description</p></td>
<td>User chooses to view a FDB defined drug pair that is not associated with a customized VA drug-drug interaction</td>
</tr>
<tr class="odd">
<td>The selected drug pair is associated with the VA custom interaction ‘x' with severity 'y'. See below for the duplicate VA custom record details. Where x is the interaction description and y is the severity level code.</td>
<td>User chooses to view an FDB defined drug pair that is associated with a customized VA drug-drug interaction</td>
</tr>
</tbody>
</table>

Messages on the Single Drug Pairs Detail Page

Error Messages

<table>
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
<td>User clicked the Drug Pair Lookup button, selected a drug pair from the FDB table, and got a message that the drug pair ID has errors.</td>
</tr>
<tr class="even">
<td>The Drug-Drug interaction &lt;Drug A/Drug B&gt;’ has not been customized. You must customize the Drug-Drug interaction prior to customizing the Drug-Drug pair. Do you want to customize the Drug-Drug interaction?</td>
<td>User does a drug pair query, selects a FDB drug pair associated with an FDB Drug interaction that has never been customized and sees a Drug-Drug Interaction Message instead of the Drug Pairs detail page</td>
</tr>
<tr class="odd">
<td><p>The selected drug pair is not customized. The drug interaction &lt;Drug A/Drug B&gt; has been customized with severity level ‘x’.</p>
<p>Customization of this drug pair can be done only through the VA custom Drug-Drug Interaction detail page.</p></td>
<td>User does a drug pair query and selects a drug pair in the FDB table. The drug pair is not customized but its parent DDI has already been customized.</td>
</tr>
<tr class="even">
<td>The selected drug pair is associated with the VA custom interaction ‘x' with severity 'y'. See below for the duplicate VA custom record details.<br />
Further customization or deletion of this drug pair can be done only through the VA custom Drug-Drug Interaction detail page.</td>
<td>User does a drug pair query and selects a drug pair in the FDB table. The drug pair and its parent DDI are customized.</td>
</tr>
<tr class="odd">
<td>Further customization or deletion of this drug pair can be done through the VA custom Drug-Drug Interaction detail page.</td>
<td>User does a drug pair query and selects a drug pair in the VA table</td>
</tr>
</tbody>
</table>

Informational Messages

<table>
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
<li><p>On all of the older VA customizations, the drug pair has been rejected and/or deleted;</p></li>
<li><p>On the latest VA customization, the drug pair is in the New, Modified, Reviewed, Approved, Delete_Reviewed, or Deleted action status.</p></li>
</ol>
<p>After the user does a query on an FDB drug pair that has all three traits mentioned above, the drug pair displayed on the Drug Pairs Detail Page is the one associated with the latest VA customization and the drug pair for all of the other VA customizations is described in the message listed on the left.</p></td>
</tr>
</tbody>
</table>

### Duplicate Therapy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the Duplicate Therapy error messages.

Error Messages

Duplicate Therapy error messages are listed below.

| Duplicate Therapy Message                                                                                                  | Cause                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Custom String field is required                                                                                            | User does not input any data into the ‘Custom String’ field                                                                                                                                                                        |
| The specified Duplicate Therapy Customization ID (DTCID) could not be found. Please report this error to the support team. | User selects a DT FDB record to customize; however, an FDB record cannot be found in the database for the given Duplicate Therapy Customization ID (DTCID). An error message will appear before the detail page is loaded.         |
| The specified Duplicate Therapy Customization ID (DTCID) could not be found. Please report this error to the support team. | User selects a DT VA record from the query results to modify. However, the VA record ID is null or empty (“”) for some reason.                                                                                                     |
| The specified Duplicate Therapy Customization ID (DTCID) could not be found. Please report this error to the support team. | User selects a DT FDB record from the query to customize. However, the DTCID is null or empty (“”) for some reason.                                                                                                                |
| The specified Duplicate Therapy Customization ID (DTCID) could not be found. Please report this error to the support team. | The user selects a VA customized record from the list and for some reason; the DTCID is invalid, inactive, or deleted.                                                                                                             |
| Field must be numeric and cannot contain more than 10 characters.                                                          | DTCID is null or has a length greater than ten.                                                                                                                                                                                    |
| The specified VA custom record could not be found. Please report this error to the support team.                           | The user selects a record from the VA customization list; however, the detailed information for the customized record is missing from the database. This error appears after the user selects the customized record from the list. |

Informational Messages

Duplicate Therapy informational messages are listed below.

| Duplicate Therapy Message                                                           | Cause                                                                               |
|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Following VA custom record already exists for this FDB Duplicate Therapy: \[DTCID\] | User opens an FDB duplicate therapy record that has an associated VA custom record. |

### Professional Monograph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error Messages

| Professional Monograph Detail Page Message                                                                                                                | Cause                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Monograph Title is required                                                                                                                               | User didn't fill in the ‘Monograph Title’ field                                                                                      |
| The Professional Monograph FDB reference record was not found in the database. Please report this error to the support team                               | User selected a Professional Monograph record in the FDB table. However, it wasn't found in the database.                            |
| Multiple Professional Monograph FDB reference records were found in the FDB database for the specified ID. Please report this error to the support team   | User selected a Professional Monograph record in the FDB table but multiple records were found in the database for the specified ID. |
| The specified Professional Monograph ID has errors. Please report this error to the support team                                                          | User customized a Professional Monograph. However, the record couldn't load from the FDB table.                                      |
| The customization was not found. The monograph may be invalid, or it may have an INACTIVE or DELETED status. Please report this error to the support team | User selected a Professional Monograph record in the VA table. However, the custom record was not found in the database.             |
| Unable to perform the update operation on the customization. Custom monograph title \<monograph title\>' is not unique.                                   | User inputs a monograph title that already exists.                                                                                   |

Informational Messages

| Professional Monograph Detail Page Message                                              | Cause                                                                                    |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Following VA custom record exists for this FDB Professional Monograph: \[Monograph ID\] | User opens an FDB professional monograph record that has an associated VA custom record. |

Warning Messages

| Professional Monograph Detail Page Warning Message                                                          | Cause                                                                                              |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| The monograph with title '\<title\> is already customized. See the duplicate VA custom record details below | Requestor did a query of FDB monographs and selected a monograph that had already been customized. |

## Custom Update Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Custom Update Page Message                                                                            | Cause                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unable to generate the update file. The update file specified does not exist or could not be located. | Release manager selects a custom update and clicks the ‘Download Existing Update’ button. However, the system is unable to generate the update file. |
| Unable to generate the update file. Failed to create customization update file                        | Release manager clicks the ‘Create New Update’ button. However, the system is unable to generate the update file.                                    |

## Query Pages Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
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
<td><p>Either a system error occurred or the query operation timed out, and the operation to save the query could not be executed.</p>
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
<td><p>Either a system error occurred or the query operation timed out, and the operation to execute the Others query could not be executed.</p>
<p>Resubmit query. If problem persists, report this error to the support team.</p></td>
<td>User tries to access queries saved by other users and they cannot be retrieved from the database</td>
</tr>
</tbody>
</table>

### Informational Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
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
<td><p>Your query saved successfully with name: ‘x’</p>
<p>where x is the name I assigned the query or “Unnamed Query” if I did not assign the query a name. No change</p></td>
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

## Record Locking Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Popup Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
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
<td>This record is being edited by user &lt;user id&gt; and is unavailable for editing.</td>
<td>User clicked the <em><strong>Edit</strong></em> button on the detail page. However, another user is currently editing the record.</td>
</tr>
<tr class="even">
<td>This record was recently modified by another user and is no longer current. Click OK to open the current record.</td>
<td>A state change was performed on the record after the user opened it. This happens when User A opens a record in 'read only' mode while User B opens the same record, clicks the Edit button, and performs a state change.</td>
</tr>
<tr class="odd">
<td>This action will cause you to lose any edits you may have made. Click OK to proceed or click cancel to continue editing this record.</td>
<td>The detail page was in Edit mode and the user clicked the <em><strong>Cancel Edit</strong></em> button.</td>
</tr>
<tr class="even">
<td><p><em><strong>Note:</strong></em> This message is browser-dependent.<br />
<br />
From Internet Explorer 7 (IE7): Are you sure you want to navigate away from this page? Click OK to continue, or cancel to stay on the current page.<br />
<br />
IE9: Are you sure you want to leave this page? (System gives option to leave this page or stay on this page)</p>
<p>Firefox: This page is asking you to confirm that you want to leave – data you have entered may not be saved. (System gives option to leave this page or stay on this page.)</p></td>
<td>User tried to navigate away from the page or closed their browser prior to clicking a state change button.</td>
</tr>
<tr class="odd">
<td>Your editing session on this page will end in one minute. To avoid losing your changes, click OK to extend your editing session.</td>
<td>The detail page was in Edit mode and the user was inactive for nineteen minutes.</td>
</tr>
</tbody>
</table>

## Reports Pages Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no reports page messages.

# Infrastructure Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VHA IT systems rely on various infrastructure components. These components will have been defined in the Logical and Physical Descriptions section of this document. Most, if not all of these infrastructure components generate their own set of errors. Each Component has its own sub-section and describes how errors are reported. The sub-sections are typical list of components and are meant to be modified for each individual system.

The sub sections are not meant to replicate existing documentation on the infrastructure component. If documentation is available online, then a link to the documentation is appropriate. Each sub-section should contain implementation specific details such and Database names, server names, paths to log files, etc.

PRE Team will work with AITC resources to resolve the Infrastructure errors. AITC will be responsible for System, Network, Database and PRE will provide the support as SME and on PECS application.

## Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oracle monitoring tools monitor several aspects of the PECS databases and alert database administrators via email and create service desk tickets for conditions such as “disk full errors or tablespace full”, archive log directory full, database down, connectivity to database down, etc.

In addition, as with all Oracle databases, errors within the database are recorded in the Oracle alert log for the database and trace files are created that will allow DBAs to review any errors. Any such errors are emailed to the database administrators daily.

## Web Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At this Time the PECS application does not implement a Web server front end, or the WebLogic/Apache Plug-in is not being utilized officially. Apache writes output to Logs Located on the Linux web server, to the directory /var/log/httpd/, unless changed in the httpd.conf configuration file. Access to these usually requires SUDO or ROOT access.

## Application Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS application and WebLogic log in conjunction assist in the Troubleshooting of the App or the WebLogic portal. PECS Logs are located in the

> \${DOMAIN_HOME}/PECSLogs directory, consisting of the Following Files: ct_prod.log, hibernate.log, server.log, spring.log, and struts.log.

Assistance from PECS Java Developers may be required to parse the Logs files to determine any issues.

The WebLogic application server logs reside in the

> \${DOMAIN_HOME}/servers/\${Each_Managed_Server_name}/logs/.

There are 2 primary log files to review:

- \${Each_Managed_Server_name}.log
- \${Each_Managed_Server_name}.out.

The WebLogic administrator should be able to parse these files. Assistance from PECS Java Developers may be required if out to the scope of the WebLogic Administration skill set.

## Network

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using Orion, a Solar Winds monitoring tool, AITC Service Desk and/or network engineers monitor the layer 2 and layer 3 network switches. If an alarm is generated by Orion, AITC Service Desk will create a service ticket, and then attempt to triage the problem. AITC Service Desk, which operates 24x7, will notify the appropriate personnel. Appropriate personnel will triage the issue and work on the resolution of the issue.

## Authentication and Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authentication and authorization errors can be reported if KAAJEE encounters errors. The most common causes would be problems with the KAAJEE user store connection or the dependent systems: SDS or one of the VistA instances. In either case, appropriate errors will be logged, indicating the cause.

## Dependent System(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The dependent systems are those used for authentication and authorization. See [Section 2.5, Dependent Systems](#dependent-systems), for a discussion of errors.

# System Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sub-sections define the process and procedures necessary to restore the system to a fully operational state after a service interruption. Each of the sub-sections starts at a specific system state and ends up with a fully operational system.

PECS is designated as Routine Support for disaster recovery. This level of support will acquire replacement processing capacity after an AITC disaster declaration. The recovery time objective (RTO) is that it will be operational when the AITC resumes regular processing services or no later than 30 days after a disaster declaration. Data will be restored from the last backup (recovery point objective (RPO)).

System backups of the vapredbs1 server are performed on the following basis;

- Full backups are performed on Sundays and kept for one month. This means that at any time, there should be four full backup tapes available for each server.
- Tapes are normally dispatched offsite on Mondays.
- Differentials are run for the remainder of the week to capture daily changes.
- Differential results are sent offsite on Mondays.
- Oracle RMAN is the application used to perform full backups of the PREP database every Tuesday and Saturday morning. The tapes are retained offsite for one month. RMAN is also used to back up archive logs and the control file database to tape daily and are also retained offsite for a month. The full database backups run for about 40-45 minutes. The archive log backups are shorter, which run about 25-30 minutes.

This section provides procedures for recovering the application at the alternate site, while Section 5.0 describes other efforts that are directed to repair damage to the original system and capabilities. Backup procedures are also defined in this section.

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

### From: PREC*6.1*717 TROUBLE SHOOTING GUIDE

### User SSOi Logout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user has issues with the SSOi session, one of the following options can be used to reset the user’s SSOi session.

- The user can go to the IAM SSOi Landing page using the link below and click on the Logout button.
- <span class="mark">REDACTED</span>
- The user can go to the IAM SSOi Logout page using the link below. The user will be logged out of SSOi.
- <span class="mark">REDACTED</span>
- The user can go to the browser Internet Options and under the Content tab, the user can click on the Clear SSL state button.
