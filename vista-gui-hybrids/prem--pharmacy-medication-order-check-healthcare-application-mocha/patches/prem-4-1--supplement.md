---
title: PREM*4*1 MOCHA Server 4 Productions Operations Manual
doc_type: POM
doc_label: Production Operations Manual
doc_layer: patch
doc_subject: MOCHA Server 4 Productions Operations Manual
app_code: PREM
app_name: "Pharmacy: Medication Order Check Healthcare Application (MOCHA)"
section: GUI
app_status: active
pkg_ns: PREM
patch_ver: 4
patch_id: PREM*4*1
group_key: "PREM:PREM:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - server
  - mocha
  - contents
  - database
  - class
  - application
  - operations
  - maintenance
  - errors
page_count: 0
word_count: 5356
section_count: 13
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Medication_Order_Check_HC_Applic/PREM_4_1_POM.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Medication_Order_Check_HC_Applic/PREM_4_1_POM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=201"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Pharmacy Re-Engineering (PRE)

  Medication Order Check Healthcare Application (MOCHA) Server 4.0

  Production Operations Manual
---

![](prem-4-1-mocha-server-4-productions-operations-manual/001.png)

June 2024

Department of Veterans Affairs (VA)

Revision History

<table>
<caption><p><span id="_Toc170472337" class="anchor"></span>Table 1: WebLogic Pre-Prod Steps</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
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
<td>06/28/2024</td>
<td>2.0</td>
<td><p>Updated version numbers, Point of Contacts</p>
<p>Added List of Tables and List of Figures</p>
<p>Updated Figures: Figure 2 and Figure 3</p>
<p>Table 3: POC</p>
<p>Updated Sections:</p>
<p>2.1.1 System Start-up</p>
<p>2.4 System Monitoring, Reporting, &amp; Tools</p>
<p>2.4.2 Availability Monitoring</p>
<p>2.4.3 Performance/Capacity Monitoring</p>
<p>2.5 Routine Updates, Extracts, and Purges</p>
<p>3.2.3.1 Database</p>
<p>3.2.3.4 Network</p>
<p>3.2.3.6 Logical and Physical Descriptions</p>
<p>3.3 Dependent System(s)</p>
<p>3.5 System Recovery</p>
<p>5 Approval Signatures</p></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>01/26/2017</td>
<td>1.0</td>
<td>Document submitted for approval</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/20/2016</td>
<td>0.2</td>
<td>Tech edits</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/19/2016</td>
<td>0.1</td>
<td>Initial version</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Toc170472337" class="anchor"></span>Table 1: WebLogic Pre-Prod Steps

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the Production Operations Manual has been baselined.

Artifact Rationale

The Production Operations Manual provides the information needed by the production operations team to maintain and troubleshoot the product. The Production Operations Manual must be provided prior to release of the product.

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Routine Operations](#routine-operations)
  - [Administrative Procedures](#administrative-procedures)
    - [System Start-up](#system-start-up)
    - [System Shutdown](#system-shutdown)
    - [Emergency System Shutdown](#emergency-system-shutdown)
    - [Back-up & Restore](#back-up-restore)
  - [Security / Identity Management](#security-identity-management)
    - [Identity Management](#identity-management)
    - [Access control](#access-control)
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
    - [Network](#network)
  - [Dependent System(s)](#dependent-systems)
  - [Troubleshooting](#troubleshooting)
  - [System Recovery](#system-recovery)
    - [Restart after Non-Scheduled System Interruption or Database Restore](#restart-after-non-scheduled-system-interruption-or-database-restore)
    - [Back-out and Rollback Procedures](#back-out-and-rollback-procedures)
- [Operations and Maintenance Responsibilities](#operations-and-maintenance-responsibilities)
- [# Approval Signatures](#approval-signatures)
This document describes how components of the Pharmacy Re-Engineering (PRE) Medication Order Check Healthcare Application (MOCHA) Server are maintained, as well as how to troubleshoot problems that might occur with this product in production. The intended audience for this document is the Information Technology (IT) teams responsible for hosting and maintaining the system. This document is normally finalized just prior to production release and includes many updated elements specific to the hosting environment.

# Routine Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Server is a Java Restful web service that requires the First Databank (FDB) MedKnowledge Framework (Fwk) (FDB-MedKnowledge) database tables and is developed to deploy on Oracle WebLogic.

The FDB-MedKnowledge database tables can be deployed to any relational database but is developed and tested against an Oracle database.

MOCHA Server requires the administration of the Oracle FDB-MedKnowledge database and Oracle WebLogic application server.

## Administrative Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### System Start-up 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The servers are brought online by starting the appropriate VMWare virtual machine. Once the operating system is loaded and the server is accessible, the Database Administrator (DBA) is advised and will bring the database online. Once the database is online, the WebLogic admin is advised and will bring the application online.

| Property                | Path                                          |
|-----------------------------|---------------------------------------------------|
| \$WL_HOME                   | /u01/app/oracle/weblogic                          |
| \$DOMAIN_HOME               | /u01/app/oracle/user_projects/domains/moc-preprod |
| WebLogic Install Directory  | \$WL_HOME                                         |
| Domain Directory            | \$DOMAIN_HOME                                     |
| Node Manager Startup Script | \$DOMAIN_HOME/bin/startNodeManager.sh             |
| Admin Server Startup Script | \$DOMAIN_HOME/startWebLogic.sh                    |
| Managed Server Startup      | From Admin Console: \<ManagedServerName\>         |

<span id="_Toc347912834" class="anchor"></span>Table 2: WebLogic Prod Steps

| Property                | Path                                       |
|-----------------------------|------------------------------------------------|
| \$WL_HOME                   | /u01/app/oracle/weblogic                       |
| \$DOMAIN_HOME               | /u01/app/oracle/user_projects/domains/moc-prod |
| WebLogic Install Directory  | \$WL_HOME                                      |
| Domain Directory            | \$DOMAIN_HOME                                  |
| Node Manager Startup Script | \$DOMAIN_HOME/bin/startNodeManager.sh          |
| Admin Server Startup Script | \$DOMAIN_HOME/startWebLogic.sh                 |
| Managed Server Startup      | From Admin Console: \<ManagedServerName\>      |

<span id="_Toc170472339" class="anchor"></span>Table 3: User Notification Points of Contact

Steps to perform the database start-up:

1.  Login to server as your user and become the Oracle user:

> i.e.*: sudo su - oracle*

2.  Start the Oracle command interface:

> *sqlplus “/as sysdba”*

3.  Start the database from the SQL\> prompt:

> *startup*

4.  Exit sql plus:

> *exit*

5.  Start the listener:

> *lsnrctl start*

Steps to perform application start-up:

1.  Login to server as your user and become the WebLogic user:

> i.e.*: sudo su - weblogic*

2.  See the previous table to identify the script you wish to run for starting the Admin Server or a Node Manager. When running a script, preface all startup scripts with the *nohup* command and place in the background.

> i.e.: Starting the Node Manager

> *nohup \$DOMAIN_HOME /bin/startNodeManager.sh &*

> i.e.: Starting the Admin Server

> *nohup ./ \$DOMAIN_HOME/startWebLogic.sh &*

3.  Login to the WebLogic Graphic User Interface (GUI) Admin console.
4.  Start the requested Managed Servers.

#### System Start-Up from Emergency Shut-Down

Steps to perform application start-up: Follow the regular startup steps in 2.1.1.

### System Shutdown 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application is first taken offline by the WebLogic admin and advises the team. The DBA takes the database (DB) offline and advises the team. The System Administrator (SA) will run “ps –ef” to identify any hung WebLogic or Oracle processes prior to shutdown/reboot of the servers.

If the server is up and the database is up but needs to come down for maintenance on the database or server, the script on the database server, vapredbs1, in the directory, /u01/oracle/admin/PREP/scripts, is a shutdown\_ script which can be run by the Oracle Linux user to shut down any database on the server. It is called from that directory as ./shutdown_db.ksh \<database_name\>, i.e., ./shutdown_db.ksh PREP.

1.  Login to the WebLogic GUI Admin console with your LAN ID, if this does not work, check the Password Vault for the environment and use the specified account.

> Select all the servers including Admin server and shut them down.

2.  Login to server as your user and become the WebLogic user:

> i.e.: *sudo su – weblogic*

> Kill \<nodemanager PID\>

3.  Verify if all the servers are stopped.

> i.e.: *ps –ef \| grep java*, should not see any WebLogic instances.

### Emergency System Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event there is an emergency that requires the system be shut down, follow the steps detailed in 2.1.2.

### Back-up & Restore 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enterprise operations will follow their established operating procedures to back up and restore.

#### Back-Up Procedures

Enterprise Operations will follow their standard operating procedures to back up the MOCHA Server system to include the application server and database. Outside of the environment configuration, MOCHA Server does not have any specific requirement regarding the backup and restoration of data.

System configuration should follow the steps defined in the administrative procedures of this document.

#### Restore Procedures

MOCHA Server is designated as Routine Support for disaster recovery. This level of support will require replacement processing capacity after an Austin Information Technology Center (AITC) disaster declaration. The MOCHA Server system is designed for high-availability, using an active-active deployment at both the AITC and Philadelphia Information Technology Center (PITC) data centers. As a result, the system can tolerate a failure at one data center with no downtime. In the event of a catastrophic site failure at either AITC or PITC, all traffic would be routed to the alternate site. Therefore, recovery time objective (RTO) and recovery point objective (RPO) are not applicable. MOCHA Server relies on redundancies in the infrastructure, including both application and database servers, and the configuration of the load balancers to maintain 24/7 service.

System configuration should follow the steps defined in the administrative procedures of this document.

#### Back-Up Testing

At the Program Manager’s discretion, random files can be selected to be restored to an alternate location. AITC currently has a backup and recovery process that will be used for MOCHA Server. Details of this procedure can be found in the Information Systems Contingency Plan Assessment (ISCPA). The ISCPA can be found in eMASS under the project code MOC. Operations will run their production test scenarios to ensure functionality. These would be the tests used to verify any deployment of MOCHA Server.

#### Storage and Rotation 

The details of these operations can be found in the AITC Disaster Recovery Plan inside of the ISCPA for MOCHA Server. The ISCPA can be found in eMASS under the project code MOC. If a copy of the ISCPA is needed, the request will need to go to the MOCHA Server Information Security Officer (ISO) to facilitate the viewing of any information hosted in eMASS.

## Security / Identity Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Server is a web service with no user interface. It is accessed by the My Health*<u>e</u>*Vet Web Service Client (HWSC). All communications are system to system with no user authentication or management within MOCHA Server. User authentication occurs within the requesting system.

### Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Server does not contain any Personally Identifiable Information (PII) or Protected Health Information (PHI) information. The data handled by MOCHA Server involves standard pharmacy drug information available from a commercial nationally distributed database, First Data Bank (FDB). The request and response calls to MOCHA Server are made over standard Hypertext Transfer Protocol (HTTP).

### Access control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Server does not manage users or handle authentication. As a web service with no user interface, the requesting application manages user authentication.

## User Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 2.3.1 details the MOCHA Server contact list.

### User Notification Points of Contact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a MOCHA Server outage or any scheduled event that may impact availability, the table below details the notification Points of Contact (POCs).

| Name                                               | Organization | Phone/Email                                       | Notification priority | Time of notification |
|----------------------------------------------------|--------------|---------------------------------------------------|-----------------------|----------------------|
| MOCHA Sustainment Team                             | OIT          | vaitsdeeoeasmocsustainment@va.gov                 | 1                     | Immediate            |
| OIT EPMO Product Support Health T3 Clinical Delta  | OIT          | OITEPMOProductSupportHealthT3ClinicalDelta@va.gov | 1                     | Immediate            |
| OIT EPMO HEALTH SERVICES PORTFOLIO Clinical Team 1 | OIT          | Clin1@va.gov                                      | 1                     | Immediate            |
| VHAPBH PMO-DATA mail group                         | PMO          | PMO-DATA@va.gov                                   | 1                     | Immediate            |
| Dan Carroll                                        | OIT          | Dan.Carroll@va.gov                                | 1                     | Immediate            |
| Scott Soldan                                       | OIT          | Scott.Soldan@va.gov                               | 1                     | Immediate            |
| Sherry Griles                                      | OIT          | Sherry.Griles@va.gov                              | 1                     | Immediate            |
| EJ Marine                                          | OIT          | Ej.Marine@VA.gov                                  | 1                     | Immediate            |

<span id="_Toc170472340" class="anchor"></span>Table 4: Application Error Codes and Descriptions

## System Monitoring, Reporting & Tools 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oracle Enterprise Manager and Grid Control are used to monitor availability and performance of the MOCHA database and application servers. Standard AITC thresholds are set for space monitoring, availability of the database, and network connectivity. Administrators are alerted immediately if the monitoring tool detects a problem. In addition, if connectivity to the database fails, an incident ticket is created in the User Service Desk software and relayed to AITC management and the primary and secondary database administrator for the project. Any connectivity issues that cause the application to stop responding as designed should be considered an outage. The POCs listed in section 2.3.1 should be notified in the event of a system outage.

System monitoring is achieved using the following tools:

- WebLogic console
- AppDynamics

### Dataflow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prem-4-1-mocha-server-4-productions-operations-manual/002.png)

<span id="_Toc170472342" class="anchor"></span>Figure 1: MOCHA Server Process Flow

### Availability Monitoring 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note: The Monitoring of the MOCHA Application Servers in Production will be done by AITC WebLogic administration.*

The steps and explanations of how to monitor machine availability is as follows:

1.  WebLogic console has the entire WebLogic environment configuration.
1.  We can monitor the admin server, node manager and managed servers running states, and control managed servers start and stop activity.
2.  Health*<u>e</u>*Vet Web Services Client (HWSC) has the Veterans Health Information Systems and Technology Architecture (VistA) sites’ connection information. It gives the ability to add, edit, update, and check the status of each connection configured.
3.  AppDynamics: is a monitoring tool. One agent per machine is deployed and it can provide in detail monitoring of all the WebLogic components from that environment. Monitoring alerts and notifications can be generated using this tool.

### Performance/Capacity Monitoring 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AppDynamics is utilized by AITC to capture Performance and Capacity activities.

It can monitor the HTTP traffic coming to AITC.

### Critical Metrics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PRE MOCHA planning and design requirements are identified in the PRE MOCHA service levels for all the solutions provided to and by the PRE MOCHA-Program Manager. Clear explanation of PRE MOCHA service level ensures that agreements about the services to be provided to the customers are defined and achieved. Identification and approval of service levels allow the PRE MOCHA management to determine and provision for what services they can agree to deliver. Service levels establish the parameters in which the PRE MOCHA management can consistently deliver services to VA customers by ongoing monitoring of the service achievements and reporting these to the customer.

PRE MOCHA-Service Level Agreement (SLA) is a high-level description of IT services to be provided by the PRE MOCHA solution and by the PRE MOCHA operations support personnel. The service level management process is responsible for defining the SLA. The SLA is the most important driver for all on-going PRE MOCHA operations and maintenance processes.

PRE MOCHA-Program Manager indicates to what extent the requirements of the SLA are achieved and through what operational and maintenance activities.

PRE MOCHA-VA customers identified the significance of all business processes during the initial design of PRE MOCHA. These business processes depend upon PRE MOCHA operational and maintenance services, and therefore upon the PRE MOCHA operational and maintenance organization.

The PRE MOCHA /AITC Project Service Level Agreement (PSLA) provides a general description of the services the AITC will conduct in support of the PRE MOCHA-Operations and Maintenance (O&M) Plan. The O&M Plan translates the PSLA general descriptions into detailed services and their components. The PSLA establishes clear levels of services required by PRE MOCHA and the metrics that will be used by both parties to measure the acceptability of provided services.

PRE MOCHA-PSLA provides measurable Key Performance Indicators (KPIs) and criteria. KPIs are measurable parameters (metrics), and performance criteria set at achievable levels. In some cases, it will be difficult to agree upon measurable parameters. PRE MOCHA availability KPIs are expressed numerically.

The PRE MOCHA-PSLA will affect the cost involved in the AITC’s delivery of services. Both parties will evaluate opportunities to improve the value derived from PRE MOCHA expenditures for AITC-provided services and will jointly perform periodic reviews of the PSLA and its associated metrics. The information for these joint reviews comes from the customer contract SLA, PSLA, and O&M plan that are based on budget (planned costs) and actual expenditures.

## Routine Updates, Extracts, and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Server FDB-MedKnowledge database is replicated by materialized view, over a DB-Link, with the Pharmacy Enterprise Customization System (PECS) database instance which contains FDB Standard and Customized data. Replication is automatic and does not require interaction from the administrator team. Details of this configuration can be found in section 2 Routine Operations of this document.

## Scheduled Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, there is no scheduled maintenance window for PRE. This will be needed in the future, so AITC has a window to do server patching, etc.

Any normal changes that are initiated by the PRE team will come in a Request for Change form to the AITC Build Manager. These requests will be submitted by 12 p.m. CST on Friday for a Monday implementation in the Pre-Production environment. Production requests must be received by 12:00 p.m. CST on for implementation on. Emergency change requests will be implemented as soon as possible.

## Capacity Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The section below details Capacity Planning in detail.

### Initial Capacity Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial Capacity Planning for Storage was done by PRE and Enterprise Infrastructure Engineering (EIE) team as per the Application requirement. Subsequently, it was decided in concurrence with AITC Architect to add Host Base Adapter (HBA) cards to the Servers, so as PRE Servers have access to Storage Area Network (SAN) storage. The SAN storage will be used to expand the storage capacity for future use as needed.

# Exception Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section presents a list of possible exceptions/errors that may occur during normal operation.

## Routine Errors 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Like most systems, MOCHA Server may generate a small set of errors that may be considered routine, in the sense that they have minimal impact on the user and do not compromise the operational state of the system. Most of the errors are transient in nature and only require the user to retry an operation. The following subsections describe these errors, their causes, and what, if any, response an operator needs to take.

While the occasional occurrence of these errors may be routine, getting a large number of an individual error over a short period of time is an indication of a more serious problem. In that case the error needs to be treated as an exceptional condition.

### Security Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Server does not have any specific requirements regarding error logging of the application server.

### Time-outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Time out may occur when accessing a third-party Database. Sometimes queries are dependent upon the availability of the database or run out of time if a large results query is requested. In the event of a timeout error, the MOCHA Server maintenance team will work with administrators to determine if the database connection pool is properly configured. If the system is configured properly, the maintenance team will work with administrators to determine the root cause of the timeouts.

### Concurrency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable (N/A)

## Significant Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant errors can be defined as errors or conditions that affect the system stability, availability, performance, or otherwise make the system unavailable to its user base. The following subsections contain information to aid administrators, operators, and other support personnel in the resolution of significant errors, conditions, or other issues.

### Application Error Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Server does not currently send automated notifications as a result of an application error. Application logs should be a maximum size of 10MB. The growth rate of each log will depend on the number of requests to the MOCHA Server service.

MOCHA Server logging requirements are as follows:

1.  Log files shall be configured to not overwrite data as more log information is appended to the file. If the file reaches maximum file size, the file should be archived to a separate location or another file created.
2.  A mechanism for archiving log files on a periodic interval (daily or weekly) shall be put in place to move log files to an appropriate share drive. The appropriate archive interval shall be determined with input from server administration personnel.
3.  The share drive used for archiving log files shall have security permissions in place to only allow access to appropriate personnel.
4.  Archived log files shall be named or placed into folders in a manner that will indicate the dates, time period, and the server to which the file applies.
5.  Logging levels for the Production environments shall be configured to a warn or error level. Debug level should not be used for Production environments on a regular basis.
6.  Archived log files for the Production environments shall be kept in place for at least 3 years prior to deletion.
7.  Archived log files for the Pre-Production, Test, and Development environments shall be kept in place for at least 30 days prior to deletion.

### Application Error Codes and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of an application error, MOCHA Server returns an exception payload and logs the error in the application logs. MOCHA Server application errors have four classifications listed below:

| Error Type | Error Description                                                       | Administrator action                                                                                                                                                                       |
|------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRE        | Checked exception while processing a MOCHA Server request               | Notify the MOCHA Server maintenance team including all available detail on the error and user scenario                                                                                     |
| FDB        | Error or issue connecting to, or retrieving data from, the FDB Database | Review the detailed message for additional information regarding the error. Check the WebLogic FDB- MedKnowledge JNDI configuration and verify the system has connectivity to the database |
| JAVA       | Thrown when the application generates a runtime exception               | Notify the MOCHA Server maintenance team including all available detail on the error and user scenario                                                                                     |
| SYSTEM     | Unhandled exception                                                     | Notify the MOCHA Server maintenance team including all available detail on the error and user scenario                                                                                     |

<span id="_Toc170472341" class="anchor"></span>Table 5: Operations and Maintenance Responsibilities

### Infrastructure Errors 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA Veterans Health Administration (VHA) IT systems rely on various infrastructure components. These components have been defined in the Logical and Physical Descriptions section of this document. Most, if not all, of these infrastructure components generate their own set of errors. Each Component has its own sub-section and describes how errors are reported. The sub-sections are a topical list of components and are meant to be modified for each individual system.

The sub sections are not meant to replicate existing documentation on the infrastructure component. If documentation is available online, then a link to the documentation is appropriate. Each sub-section should contain implementation specific details such and Database names, server names, paths to log files, etc.

PRE Team will work with AITC resources to resolve the Infrastructure errors. AITC will be responsible for System, Network, Database, and PRE will provide support in the event of an application error.

#### Database

Oracle monitoring tools monitor several aspects of the PECS, MOCHA, and PPS-N databases and alert database administrators via email who then create service desk tickets for conditions such as “disk full errors or tablespace full”, archive log directory full, database down, connectivity to database down, etc.

In addition, as with all Oracle databases, errors within the database are recorded in the Oracle alert log for the database and trace files are created that will allow DBAs to review any errors. Any such errors are emailed to the database administrators daily.

#### Web Server

At this time the MOCHA Server application does not implement a web server front end, or the WebLogic/Apache plug-in is not being utilized officially. Apache writes output to logs located on the Linux web server, to the directory /var/log/httpd/, unless changed in the httpd.conf configuration file. Access to these files requires SUDO or ROOT access.

#### Application Server

MOCHA Server does not have any specific requirements regarding error logging of the application server. Administrators should refer to the standard system logs for any application specific issues.

### Network

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using AppDynamics, , AITC service desk and/or network engineers monitor the layer 2 and layer 3 network switches. If an alarm is generated by AppDynamics, AITC service desk will create a service ticket, and then attempt to triage the problem. AITC service desk, which operates 24x7, will notify the appropriate personnel. Appropriate personnel will triage the issue and work on the resolution of the issue.

#### Authentication & Authorization

MOCHA Server does not authenticate or authorize users at the application level.

#### Logical and Physical Descriptions

The diagram below depicts the physical architecture of the MOCHA Server platform:

![](prem-4-1-mocha-server-4-productions-operations-manual/003.png)

<span id="_Ref83383902" class="anchor"></span>Figure 2: Physical Architecture of the MOCHA Server Platform

The “Authoritative FDB-MedKnowledge” database is not part of the MOCHA Server infrastructure but is the PRE-Pharmacy Enterprise Customization System (PECS) FDB-MedKnowledge instance. PECS is the authoritative source for FDB information to include COTS updates and VA customizations.

## Dependent System(s) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Server web services are currently used by both VistA and Computerized Patient Record System (CPRS) by means of the VistA Health*<u>e</u>*Vet Web Service Client (HWSC).

Below is the logical deployment of MOCHA Server:

![](prem-4-1-mocha-server-4-productions-operations-manual/004.png)

<span id="_Toc170472344" class="anchor"></span>Figure 3: Logical Deployment of the MOCHA Server

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## System Recovery 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event that system recovery is needed, Service Delivery and Engineering (SDE) Enterprise Operations (EO) will follow their standard operating procedures to restore the environment based on the latest backup or image available.

MOCHA Server does not have any specific requirements regarding system or data recovery. Once the MOCHA Server system, including the application server and database, are restored and operational then the database will automatically replicate from the PPS-N FDB-MedKnowledge datastore.

MOCHA is designated as Routine Support for disaster recovery. This level of support will acquire replacement processing capacity after an AITC disaster declaration. The recovery time objective (RTO) is that it will be operational when the AITC resumes regular processing services or no later than 45 days after a disaster declaration. Data will be restored from the last backup (Recovery Point Objective (RPO)).

System backups of the server are performed on the following basis:

- Full backups are performed on daily and kept for 45 days. This means that at any time, there should be 45 full backup tapes available for each server.
- Oracle Recovery Manager software is used to perform full backups of the MOCHA (vaausdbsmoc210 and vaausdbsmoc211) database every night at 11 PM central time and kept for 45 days. Recovery Manager is also used to backup archive logs and the database control file to tape daily. The full database backups run for about 10 minutes. The archive log backups run every 15 to 30 minutes, based on size.

### Restart after Non-Scheduled System Interruption or Database Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any restart of MOCHA Server should follow the steps detailed in section 2.1 of this document.

MOCHA Server does not have any specific requirements for a restart after a system interruption. During any system interruption, scheduled or unscheduled, the MOCHA Server instance experiencing the outage should be removed from the Global Load Balancer so that end users of consuming application are not affected.

### Back-out and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MOCHA Server deployment and installation guide can be found under MOCHA Server documentation in the VDL or product repository. Each release of MOCHA Server will include back out procedures in the Change Request that should be used in the event of a failed deployment.

# Operations and Maintenance Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Operations and Maintenance ResponsibilitiesThis table lists the Operations and Maintenance responsibilities for MOCHA Server.</caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 27%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>EO IT Core Services Matrix</th>
<th><p>Development and Test Environments</p>
<p>Customer = Customer Owned and Managed</p>
<p>EO = EO Owned and Managed</p>
<p> Optional = EO <u>or</u> Customer Owned and Managed. <u>Annotate Ownership (EO or Customer) in the Blocks Below During the EO Intake Process.</u></p></th>
<th><p>Pre-Production and Production Environments</p>
<p>Customer = Customer Owned and Managed</p>
<p>EO = EO Owned and Managed</p>
<p> Optional = EO <u>or</u> Customer Owned and Managed. <u>Annotate Ownership (EO or Customer) in the Blocks Below During the EO Intake Process.</u></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Requirements Definition</td>
<td>Customer</td>
<td>Customer</td>
</tr>
<tr class="even">
<td>Environmental (Power, Space, Cooling)</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Physical Security Services</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Cabling (Cat and Fiber)</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Asset Management</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Program and Project Management of EO activities.</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Program and Project Management of Customer activities.</td>
<td>Customer</td>
<td>Customer</td>
</tr>
<tr class="even">
<td>Release, Configuration and Build Management support of EO activities.</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Release, Configuration, and Build Management support of Customer activities.</td>
<td>Customer</td>
<td>Customer</td>
</tr>
<tr class="even">
<td>Rough Order of Magnitude (ROM) Pricing Estimates</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Detailed Bill of Materials (BOM) Pricing Estimates</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Hosting Design and Placement</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Architecture Services</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="even">
<td>System Ownership</td>
<td>Customer</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Networking Infrastructure, Operations and Maintenance – Switches, Routers, Load Balancers, IP Address Space and Allocations</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Enterprise Storage Infrastructure, Operations and Maintenance – SAN, NAS, and Enterprise Tape Backup Systems</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Server Platforms Infrastructure, Operations and Maintenance (Hardware Layer)</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Virtual Systems and Cloud Infrastructure, Operations and Maintenance (VMware, Sun Virtualization)</td>
<td>EO</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Provision Virtual Machines, EO baseline OS installation, IIS, SSL, and .NET installation, OS upgrades, V2S Client installation and updates, group policy management, initial user provisioning, OS level security compliance</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Application installation, configuration &amp; maintenance, subsequent user provisioning, Application troubleshooting, Security compliance and remediation of application related vulnerabilities</td>
<td>Customer</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Responsible for <u>physical</u> Database installation, database creation, and initial configuration of table space (for example in Oracle (SYSTEM, SYSAUX, TEMP, UNDO, USER) and other standard database objects (such as SYSTEM, SYS, SYSMAN)); for SQL Server the creations of System Databases to include master, model, and msdb; DB upgrades and Continuous Readiness in Information Security Program (CRISP) patches and configuration settings, initial database user provisioning, database level security compliance, backup and restore operations</td>
<td>EO</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Responsible for <u>logical</u> Database functions, such as manipulating database schema objects, managing table spaces, and adding data files, managing database users and privileges, creating PL/SQL procedures, triggers, and packages, setting up replication objects, database performance tuning, data extraction, transformation and loading, Security compliance and remediation of application related vulnerabilities, and Database related troubleshooting</td>
<td>Customer</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Security Scanning and Auditing Systems Infrastructure, Operations and Maintenance</td>
<td>EO</td>
<td>EO scans and provides report of findings to the customer and work with the maintenance team to address issues</td>
</tr>
<tr class="even">
<td>Systems Monitoring and Performance Infrastructure, Operations and Maintenance</td>
<td>EO</td>
<td>EO manages monitoring services and grants rights as well as addresses alerts</td>
</tr>
<tr class="odd">
<td>Operating System Operations and Maintenance <em>(Windows, Linux)</em></td>
<td>Customer</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Database Operations and Maintenance <em>(Oracle RDBMS)</em></td>
<td>Customer</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Middleware Operations and Maintenance <em>(Weblogic, FileNet, BusinessWare</em>)</td>
<td>Customer</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Web Server Operations and Maintenance (IIS, Tomcat)</td>
<td>Customer</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Application Operations and Maintenance</td>
<td>Customer</td>
<td>EO</td>
</tr>
<tr class="even">
<td>Assessment and Authorization Services (A&amp;A)</td>
<td>N/A</td>
<td>EO</td>
</tr>
<tr class="odd">
<td>Business Continuity Management Services</td>
<td>N/A</td>
<td>EO</td>
</tr>
</tbody>
</table>

Operations and Maintenance ResponsibilitiesThis table lists the Operations and Maintenance responsibilities for MOCHA Server.

# # Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REVIEW DATE:

SCRIBE:

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Dan Carroll, OIT Health Portfolio Director Date

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Lynn Sanders, Associate Chief Consultant Date

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Scott Soldan, Receiving Organization Date

(Project Manager, EPMD Health Portfolio)

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Sherry Griles, VA IT Project Manager Date