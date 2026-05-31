---
title: VES Version 5.3 Production Operations Manual
doc_type: POM
doc_label: Production Operations Manual
doc_layer: anchor
doc_subject: null
app_code: VES
app_name: VA Enrollment System
section: GUI
app_status: archive
pkg_ns: VES
patch_ver: 5.3
patch_id: VES*5.3
group_key: VES:VES:5.3
file_numbers: []
security_keys: []
menu_options: 0
description: '| Date | Version | Description | Author | |------------|---------|---------------------|----------------| | 07/09/2018 | 5.3 | 5.3 updates | Liberty ITS TW | | 03/13/2018 | 5.2 | 5.2 updates | SMS/Leidos TW | | 02/15/2018 | 5.1 | 5.1 updates | SMS/Leidos TW | | 10/23/2017 | 5.0 | 5.0 updates |...'
audience: Production operations, release engineers
keywords: []
page_count: 0
word_count: 7197
section_count: 13
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: July 2018
revision_count: 11
revision_newest: 07/09/2018
revision_oldest: 12/15/2016
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/es_5_3_pom_raci.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/es_5_3_pom_raci.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=293
audit_applied: '2026-05-31'
master_source: VES Version 5.3 Production Operations Manual
master_pub_date: July 2018
consolidated_from: 7 versions
prior_versions:
- VES Version 5.10 Production Operations Manual
- VES Version 5.5 Production Operations Manual
- VES Version 5.6 Production Operations Manual
- VES Version 5.7 Production Operations Manual
- VES Version 5.8 Production Operations Manual
- VES Version 5.9 Production Operations Manual
consolidated_title: ves production operations manual
---

![](ves-version-5-3-production-operations-manual/001.png)

July 2018

Revision History

| Date       | Version | Description         | Author         |
|------------|---------|---------------------|----------------|
| 07/09/2018 | 5.3     | 5.3 updates         | Liberty ITS TW |
| 03/13/2018 | 5.2     | 5.2 updates         | SMS/Leidos TW  |
| 02/15/2018 | 5.1     | 5.1 updates         | SMS/Leidos TW  |
| 10/23/2017 | 5.0     | 5.0 updates         | SMS/Leidos TW  |
| 09/19/2017 | 4.0     | 4.8 updates         | SMS/Leidos TW  |
| 09/01/2017 | 3.0     | 4.7 updates         | SMS/Leidos TW  |
| 05/30/2017 | 2.2     | 4.6.2 updates       | SMS/Leidos TW  |
| 04/25/2017 | 2.1     | 4.6.1 updates       | SMS/Leidos TW  |
| 03/16/2017 | 2.0     | 4.6 updates         | SMS/Leidos TW  |
| 01/09/2017 | 1.1     | 4.5.1 updates       | SMS/Leidos TW  |
| 12/15/2016 | 1.0     | Initial publication | SMS/Leidos TW  |

Table : User Notification Points of Contact

> **NOTE:** The revision history cycle begins once changes or enhancements are requested, after the Production Operations Manual is baselined.

Artifact Rationale

The Production Operations Manual provides the information needed by the production operations team to maintain and troubleshoot the product. The Production Operations Manual must be provided prior to release of the product.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Routine Operations](#routine-operations)
  - [Administrative Procedures](#administrative-procedures)
    - [System Startup](#system-startup)
    - [System Shutdown](#system-shutdown)
    - [Backup and Restore](#backup-and-restore)
  - [Security/Identity Management](#securityidentity-management)
    - [Identity Management](#identity-management)
    - [Access control](#access-control)
  - [User Notifications](#user-notifications)
    - [User Notification Points of Contact](#user-notification-points-of-contact)
  - [System Monitoring, Reporting and Tools](#system-monitoring-reporting-and-tools)
    - [Dataflow Diagram](#dataflow-diagram)
    - [Availability Monitoring](#availability-monitoring)
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
- [Operations and Maintenance Responsibilities](#operations-and-maintenance-responsibilities)
- [Approval Signatures](#approval-signatures)
The mission of the Department of Veterans Affairs (VA) Office of Information and Technology (OIT), Enterprise Program Management Office (EPMO) is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective, and efficient IT services, and Operations and Maintenance (O&M) to persons and organizations that provide point-of-care services to our Veterans.
The VA's goals for its Veterans and families include:
- Make it easier for Veterans and their families to receive the right benefits, and meeting their expectations for quality, timeliness, and responsiveness.
- Improve the quality and accessibility of health care, benefits, and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive, and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice, and ongoing support needed to make informed health decisions and successfully implement the Veteran's personal health plans.
- Receive timely, high quality, personalized, safe, effective, and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates, and other service organizations.
To assist in meeting these goals, the Enterprise Health Benefits Determination (EHBD) program will provide enterprise wide enhancements and sustainment for the following systems/applications:
- The Enrollment System (ES) assists Veterans to enroll for VA healthcare benefits and is the core application that feeds other VA systems with Enrollment and Eligibility (E&E) data.
- Income Verification Match (IVM) assists in determining priority grouping for healthcare eligibility.
- VistA Registration, Eligibility & Enrollment (REE) shares information with other VistA applications and enables registration and eligibility determinations and enrollment at VA Medical Centers (VAMC).
- Veteran's On-Line Application (VOA) is re-purposed for the online Veterans Health Benefits Handbook (VHB). VHB provides each enrolled Veteran on-demand online access to a personalized and dynamic health benefits-related Handbook.
- 
Enrollment System Modernization (ESM) <span class="mark">Phase 2</span> defines health benefit plans for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care. Key enhancements to be completed include Pending Eligibility Determination, fixes to the Enrollment System, Date of Death, Internal Controls, Workflow, Veterans Financial Assessment, converting of Military Service Data Sharing (MSDS) to Enterprise Military Information Service (eMIS), Manage Relationships, Veteran Contact Service, and support for Enrollment System Community Care (ESCC).
Veteran's Health Administration (VHA) Chief Business Office (CBO) is the business owner for ES and Health Eligibility Center (HEC) is the main system user. HEC is VHA's authoritative source for enrollment and eligibility activities, which support the delivery of VA healthcare benefits.
ES is a Java application that utilizes the Java 2 Enterprise Edition (J2EE) platform architecture. It consists of two major sub-systems or modules: messaging and case management. The messaging sub-system provides a seamless bi-directional interface with external VHA and non-VHA systems for data exchange of Veterans information. The case management sub-system is an intranet Web-based application that provides authorized VHA case representatives at the HEC with a Web interface to easily track, maintain, and manage cases associated with Veteran benefits.

# Routine Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes procedures and tasks required for normal operations of the system.

## Administrative Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### System Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the Administration Console for administrative procedures regarding WebLogic administration tasks. Tasks such as system startup, system shutdown, and backup and restore are managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators. Using the Administration Console, more detailed information on WebLogic administration tasks can be obtained from the official documentation at:  
[Oracle WebLogic Server on Oracle Fusion Middleware 12c (12.2.1.2.0)](https://docs.oracle.com/middleware/12212/wls/index.html)

#### System Startup from Emergency Shutdown

System startup is managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

### System Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System shutdown is managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

#### Emergency System Shutdown

Emergency system shutdown is managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

### Backup and Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backup and restore operations are managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

#### Backup Procedures

Backup operations are managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

#### Restore Procedures

Restore operations are managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

#### Backup Testing

Backup testing is managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

#### Storage and Rotation

Storage and rotation operations are managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

## Security/Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enrollment System (ES) application is integrated with the Web-based enterprise-level authentication services using CA SiteMinder provided by Identity and Access Management (IAM).

The ADR database team is responsible for maintaining an audit trail. The team maintains an audit log at the application level. Changes to user information are tracked through ES, which automatically records additions and deletions. Currently, ES administrators generate and review the audit log for security purposes on a daily basis, and the Information Security Officer (ISO) generates and reviews the audit log on a weekly basis. ES maintains audit trails that are sufficient in assisting in reconstruction of events due to a security compromise or malfunction.

The audit trail of ES contains the following requirements:

- Identity of each person and device having access or attempting access to the system
- Date and time of the access and logoff
- Activities that modify, bypass, or negate IT security safeguards controlled by the computer system
- Security-relevant actions associated with processing
- User ID for unsuccessful logon attempts

> Note: Access to online security audit logs is strictly enforced. Only the Data Base Administrator (DBA) and ISO are authorized to access the security audit logs. In addition, audit trails are reviewed following a known system violation or application software problem that has occurred. If discrepancies are identified, the information in the audit trail provides the means for a thorough investigation.

### Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ES ensures that each user is authenticated before access is permitted. HEC users must submit a request for an ES role in order to gain access to the system. All users receive a user ID, and access rights because of their roles and responsibility to the system. Accounts that are inactive for 90 days are disabled.

### Access control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The controls to access ES for the user and user classes are controlled through the ISO located at the HEC. In addition, the access of business roles is controlled and monitored through the HEC ISO, however, specific roles are defined within the ES application. The HEC ISO controls the population of the user groups across the domain but the AITC controls the access groups.

> Note: Details are described in the AITC Directive 0712 (Parts: 16 General User Security Procedures and 20 System Administrator Security Procedures) and HEC-18.

Application users are restricted from accessing the operating system, applications, or other system resources not required in the performance of their duties. Authorized Web services staff monitors the security log regularly to detect any instances of unauthorized transaction attempts. The system will automatically end the user's session after 20 minutes of inactivity.

Listed below are the following recommended users/security keys/roles:

- Local Administrator/ISO/Report Viewer – DQM
- System Administrator/IRM/Report Viewer – LAS
- EE LAS/Report Manager – Everything/Report Viewer – PSC
- EE Supervisor/Report Manager – DQM/Report Viewer – SSN
- DQ Supervisor/Report Manager – LAS/Report Viewer – NON-HEC Limited
- Director/Report Manager – PSC/Undeliverable Mail Manager
- EE Program Clerk/Report Viewer–Everything/EGT Manager
- VistA Clerk/Report Viewer – Non-HEC/IV LAS
- Call Center Clerk/Report Viewer – HEC

> Note: Federal policies require that all IT positions are evaluated and that a sensitivity level is assigned to the position description. A background investigation is required for all VHA employees filling sensitive positions. VHA personnel and non-VHA personnel, including contractors, must have personnel security clearances commensurate with the highest level of information processed by the system.

User access is restricted to the minimum necessary to perform the job. Each ES user is assigned privileges that allows or restricts updating, deleting, and/or inserting records in the database. In addition, ES uses application-level security controls to limit access to various system functions to only authorized users.

## User Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enterprise Service Desk (ESD) will be notified of any system outages. ESD will release an Automated Notification Reporting (ANR) message informing all users of the affected system(s), status, and expected time the system will be operational (for scheduled outages).

### User Notification Points of Contact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the case of a system outage, system or software upgrades to include scheduled or unscheduled maintenance, or system changes, the following organizations listed in Table 1 are notified by ANR and email—at or before the time of ANR creation—approximately 5-7 days prior to deployment. There is no specific priority assigned to notifications.

<table>
<caption><p>Table : Log Message Attributes</p></caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Organization</th>
<th>Email Address</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Health Eligibility Center (HEC)</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Change Healthcare</td>
<td>commandcenter@changehealthcare.com</td>
</tr>
<tr class="odd">
<td>Veteran's On-Line Application (VOA)</td>
<td><p>OIT EPMO TRS EPS SoS Weblogic Support</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>Veteran Information Eligibility Record Services (VRS)</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>National Health Information (NHI)</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Income Verification Match/Enrollment Database (IVM/EDB)</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Healthcare Claims Processing System (HCPS)</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Veterans Health ID Card (VHIC)</td>
<td>REDCTED</td>
</tr>
</tbody>
</table>

Table : Log Message Attributes

## System Monitoring, Reporting and Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes a high-level overview of the monitoring for the ES production environment.

### Dataflow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 1 is an overview diagram of the internal and external systems and sub-systems that interface with the ES and shows the data stores that ES shares with other systems.

![](ves-version-5-3-production-operations-manual/002.png)

Figure : Dataflow Diagram

### Availability Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system is monitored by AITC using the tools CA Introscope and BlueStripe. The tools can be accessed via the URL: REDACTED.

You need to be in the CA APM Application Environment Tool in order to access Introscope and BlueStripe.

Monitoring tool alerts describes the various system components that are being monitored for various parameters, as seen in Figure 2.

![](ves-version-5-3-production-operations-manual/003.png)

Figure : Introscope Alert Dashboard

### Performance/Capacity Monitoring 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a number of metrics captured via the Introscope Server:

- CPU utilization
- Memory utilization
- WebLogic Java Messaging Service (JMS) queues current and pending count
- WebLogic JMS queues response time
- CPU per Java process
- Garbage collection pattern
- Managed server status
- Web module average response time
- Backend database average response time
- Web service response time
- Connectivity with other systems such as VistA Interface Engine (VIE) and Person Service Identity Management (PSIM)

These metrics can be browsed for either real time data, or for a selected period of time. A sample graph is shown in Figure 3.

![](ves-version-5-3-production-operations-manual/004.png)

Figure : Sample ES Performance Monitoring Graph

### Critical Metrics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The critical metrics captured for ES are covered in Section 2.4.3, Performance/Capacity Monitoring.

## Routine Updates, Extracts and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no additional maintenance activities required for ES.

## Scheduled Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ES has scheduled maintenance on the third Saturday of each month. Prior to each scheduled maintenance window, the ESD is notified and an ANR released to notify all users.

## Capacity Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity planning for each release starts in the requirements phase. The steps are as follows.

- Analyze the requirements and identify changes in the following areas:
1.  Increase in messaging volume and pattern
2.  Increase in Web service request volume and pattern
3.  Volume of records processed by batch processes
4.  Data storage increase
5.  File storage increase
6.  Performance requirements
- Assess current capacity usage against the new needs
- Plan and Initiate Service requests for additional infrastructure if needed

### Initial Capacity Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 4 shows the current total top 10 activities (Event) based on over 4 million activities by frequency. These activities impact the ADR and VistA databases, however with non CPU/WAN/LAN intensity.

![](ves-version-5-3-production-operations-manual/005.png)

Figure : Top 10 Business Events

# Exception Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a high-level view of system errors that may be encountered during operation.

## Routine Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Like most systems, ES may generate a small set of errors that may be considered routine, in the sense that they have minimal impact on the user and do not compromise the operational state of the system. Most of the errors are transient in nature and only require the user to retry an operation. The following subsections describe these errors, their causes, and what, if any, response an operator needs to take.

While the occasional occurrence of these errors may be routine, getting large numbers of individual errors over a short period of time is an indication of a more serious problem. In that case the error needs to be treated as an exceptional condition.

### Security Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security errors encountered by users and/or operators will involve login and privilege issues. These will typically involve a user not having the appropriate access levels granted. These can be corrected by contacting the appropriate security administrator or the VA help desk.

### Time-outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Session time-outs may occur to end a user's session if it is left unattended for an extended period of time. The user will need to establish a new session by logging in and resuming the work in progress.

### Concurrency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Concurrency errors may be encountered by users attempting to update a case or other business records at the same time as another user. This is an extremely rare occurrence due to the way cases are assigned to users and to the fact that the user base is relatively small. If this does occur, the first user will take precedence and the second user will be notified that any changes made during the session will not be written to the database. This type of optimistic locking assumes low likelihood of occurrence and will prevent inadvertent corruption of data.

## Significant Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant errors are errors or conditions that affect the system stability, availability, performance, or make the system unavailable. The following subsections can help administrators, operators, and other support personnel resolve significant errors, conditions, or other issues.

### Application Error Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information regarding the logging capabilities of the system.

The ES application is hosted by a WebLogic Domain of clustered servers. The domain consists of one Admin server instance, ESRAdminServer, and three managed servers (MS1, MS2 and MS3).

Each subsystem within WebLogic Server generates server log messages to communicate its status. To keep a record of the messages that the subsystems generate, WebLogic Server writes the messages to log files. The server log records information about events, such as the startup and shutdown of servers, the deployment of new applications, and the failure of one or more subsystems. The messages include information about the time and date of the event, as well as the ID of the user who initiated the event.

In addition to writing messages to a log file, each server instance prints a subset of its messages to the standard output log. By default, a server instance prints only messages of a WARNING severity level or higher to the standard output log.

The messages for all WebLogic Server subsystems contain a consistent set of fields (attributes) as described in Table 2.

<table>
<caption><p>Table : Message Severity</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Timestamp</td>
<td>Time and date when the message originated, in a format that is specific to the locale. The Java Virtual Machine (JVM) that runs each WebLogic Server instance refers to the host computer's operating system for information about the local time zone and format.</td>
</tr>
<tr class="even">
<td>Severity</td>
<td>Indicates the degree of impact or seriousness of the event reported by the message</td>
</tr>
<tr class="odd">
<td>Subsystem</td>
<td>Indicates the subsystem of WebLogic Server that was the source of the message For example, Enterprise Java Bean (EJB) container or Java Messaging Service (JMS)</td>
</tr>
<tr class="even">
<td>Server Name<br />
Machine Name<br />
Thread ID</td>
<td><p>Identify the origins of the message:</p>
<p>Server Name is the name of the WebLogic Server instance on which the message was generated.</p>
<p>Machine Name is the DNS name of the computer that hosts the server instance.</p>
<p>Thread ID is the ID that the JVM assigns to the thread in which the message originated.</p>
<p>Log messages that are generated within a client JVM client do not include these fields. For example, if an application runs in a client JVM and it uses the WebLogic logging services, the messages that it generates and sends to the WebLogic Server log files will not include these fields.</p></td>
</tr>
<tr class="odd">
<td>User</td>
<td><p>The user ID under which the associated event was executed.</p>
<p>To execute some pieces of internal code, WebLogic Server authenticates the ID of the user who initiates the execution and then runs the code under a special Kernel Identity user ID.</p>
<p>J2EE modules such as EJBs that are deployed onto a server instance report the user ID that the module passes to the server.</p>
<p>Log messages generated within a client JVM client do not include this field.</p></td>
</tr>
<tr class="even">
<td>Transaction ID</td>
<td>Present only for messages logged within the context of a transaction.</td>
</tr>
<tr class="odd">
<td>Message ID</td>
<td><p>A unique six-digit identifier</p>
<p>All message IDs that WebLogic Server system messages generate start with BEA- and fall within a numerical range of 0-499999.</p></td>
</tr>
<tr class="even">
<td>Message Text</td>
<td>A description of the event or condition</td>
</tr>
</tbody>
</table>

Table : Message Severity

The severity attribute of a WebLogic Server log message indicates the potential impact of the event or condition that the message reports.

Table 3 lists the severity levels of log messages from WebLogic Server subsystems, the lowest to highest impact level. WebLogic Server subsystems can generate many lower severity messages and a few high severity messages (e.g., under normal circumstances, they can generate many INFO messages and no EMERGENCY messages).

<table>
<caption><p>Table : ES Dependent Systems</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Severity</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>INFO</td>
<td>Used for reporting normal operations.</td>
</tr>
<tr class="even">
<td>WARNING</td>
<td>A suspicious operation or configuration has occurred but it might not affect normal operation.</td>
</tr>
<tr class="odd">
<td>ERROR</td>
<td>A user error has occurred. The system or application can handle the error with no interruption and limited degradation of service.</td>
</tr>
<tr class="even">
<td>NOTICE</td>
<td><p>An INFO or WARNING-level message that is particularly important for monitoring the server.</p>
<blockquote>
<p><strong>Note:</strong> Only WebLogic Server and its subsystems generate messages of this severity.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CRITICAL</td>
<td><p>A system or service error has occurred. The system can recover but there might be a momentary loss or permanent degradation of service.</p>
<blockquote>
<p><strong>Note:</strong> Only WebLogic Server and its subsystems generate messages of this severity.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ALERT</td>
<td><p>A particular service is in an unusable state while other parts of the system continue to function. Automatic recovery is not possible; the immediate attention of the administrator is needed to resolve the problem.</p>
<blockquote>
<p><strong>Note:</strong> Only WebLogic Server and its subsystems generate messages of this severity.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>EMERGENCY</td>
<td><p>The server is in an unusable state. This severity indicates a severe system failure or panic.</p>
<blockquote>
<p><strong>Note:</strong> Only WebLogic Server and its subsystems generate messages of this severity.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Table : ES Dependent Systems

When a WebLogic Server instance writes a message to the log file, the first line of each message begins with \#### followed by the message attributes. Each attribute is contained between angle brackets.

The following is an example of a message in a log file:

> \####\<Sep 12, 2017 12:00:34 PM CDT\> \<Info\> \<Diagnostics\> \<REDACTED\> \<MS1\> \<\[ACTIVE\] ExecuteThread: '0' for queue: 'weblogic.kernel.Default (self-tuning)'\> \<\<WLS Kernel\>\> \<\> \<\> \<1505235634542\> \<BEA-320145\> \<Size based data retirement operation completed on archive EventsDataArchive. Retired 0 records in 1 ms.\>

In this example, the message attributes are: Timestamp, Severity, Subsystem, Machine Name, Server Name, Thread ID, User ID, Transaction ID, Message ID, and Message Text.

- If a message is not logged within the context of a transaction, the angle brackets for Transaction ID are present even though no Transaction ID is present.
- If the message includes a stack trace, the stack trace follows the list of message attributes.

When a WebLogic server instance writes a message to the standard output log, the output does not include the \#### prefix and does not include the Server Name, Machine Name, Thread ID, and User ID fields.

The following is an example of how the message from the previous section would be printed to the standard output log:

> \<Sep 12, 2017 11:05:59 AM CDT\> \<Info\> \<Security\> \<BEA-090905\> \<Disabling CryptoJ JCE Provider self-integrity check for better startup performance. To enable this check, specify -Dweblogic.security.allowCryptoJDefaultJCEVerification=true\>

In this example, the message attributes are: Timestamp, Severity, Subsystem, Message ID, and Message Text.

Each WebLogic Server instance writes all messages from its subsystems and applications to a log file that is located on the local host computer.

In addition to writing messages to its local log file, each server instance forwards a subset of its messages to a domain-wide log file. By default, servers forward only messages of severity level ERROR or higher.

The ES application uses Log4j logging framework, which makes it possible to enable logging at runtime without modifying the application.

Log files can be accessed using a Web log portal called REDACTED

The log files (server and domain) and standard output log files are located on the application servers and can also be accessed using SSH to servers. The servers have the .log and .out files located below the server root directory in logs directory.

> ./servers/\<serverName\>/logs/\<serverName\>.log

> ./servers/\<serverName\>/logs/\<serverName\>.out

The Log4j log files are created in the \$DOMAIN_HOME directory

> ./esr\_\<serverName\>.log

### Application Error Codes and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All application errors are logged. The ES does not generate error codes, but produces and logs Java style exceptions.

### Infrastructure Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Common errors displayed by the ES due to interactions with external systems are described in the Dependent Systems section.

#### Database

All database errors are logged in the application error log.

#### Web Server

All Web server errors are logged in the application error log. In addition to server logs, HTTP logging is enabled on each server and the server saves HTTP requests in a separate log file, named *access.log* in

> ./servers/\<serverName\>/logs/access.log

#### Application Server

All application server errors are logged in the application error log.

#### Network

N/A  
Network errors can arise due to many factors, and are often beyond the extent of the ES system. For this reason, network errors are not applicable.

#### Authentication & Authorization

The application error log includes authentication and authorization errors caused by interactions with external systems.

#### Logical and Physical Descriptions

From an application perspective, the ES is designed following layering and Service Oriented architectural framework. Logically, the system is segmented under two major components, the enterprise framework and the application component. The enterprise framework consists of low-level system plumbing and management critical to any large mission critical system, including transaction management, security, data access layer and many more. The application component resides on top of the enterprise framework and is responsible for the business processes.

The Enrollment System (ES) application (formerly ESR) is comprised of four major modules: Framework, Common, User Interface (UI), and Messaging. Each of these modules is an independent set of services that are consumed by other external or internal clients.

- The framework module represents the system plumbing and integration points with other third-party libraries.
- The common module represents the application layer component consumed by the messaging, workflow, communication, and the User Interface (UI) modules.
- The messaging module is the integration point between ES and other external applications. This module allows for asynchronous and synchronous communication protocols.
- The UI module is the presentation layer of ES. The end users access this module through a Web interface, hosted on the VHA network.

Figure 5 is a diagram of the ES Application Architecture Overview of the ES application.

![](ves-version-5-3-production-operations-manual/006.png)

Figure : ES Application Architecture Overview

The ES Physical Architecture outlines the hardware components that represent the environments mentioned in Figure 6. The Web-tier is represented by a series of Web servers, the business-tier is represented by a series of application servers in clustered environment, and the enterprise information data tier is represented by pure database servers. The following sections define the ES platform with hardware and software specifications.

![](ves-version-5-3-production-operations-manual/007.png)

Figure : ES Physical Model

The ES Physical view in Figure 7 represents the deployed environment and the relationship between the different software packages and hardware components residing on the ES platform.

REDACTED

Figure : ES Production Configuration

AITC maintains the hardware specifications in a configuration management database.

## Dependent System(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 4 lists the systems used by ES.

<table>
<caption><p>Table : Role Identification</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 26%" />
<col style="width: 30%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>Internal or External</th>
<th>Name</th>
<th>Description</th>
<th>Interface Name</th>
<th>Interface System</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>External</td>
<td>Social Security Agency (SSA)</td>
<td>To verify Social Security numbers (SSN)</td>
<td>SSN Verification</td>
<td>SSA</td>
</tr>
<tr class="even">
<td>Internal</td>
<td>Austin Information Technology Center (AITC) Mail Center</td>
<td>To print and mail letters to Veterans</td>
<td>Letters Interface</td>
<td>AITC mainframe</td>
</tr>
<tr class="odd">
<td>Internal</td>
<td>Veterans Health Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE)</td>
<td>To receive and send Veteran data</td>
<td>Messaging Interface</td>
<td>VistA Health Level 7 (HL7)</td>
</tr>
<tr class="even">
<td>Internal</td>
<td>VistA Integrated Billing (IB)</td>
<td>To share Income Verification Match (IVM) conversion decisions</td>
<td>Messaging interface</td>
<td>VistA IB</td>
</tr>
<tr class="odd">
<td>Internal</td>
<td>Master Veteran Index (MVI)</td>
<td>To retrieve primary view traits, update person traits, receive Date of Death Notification, receive merge/unmerge notifications on person ICN</td>
<td>MVI interface</td>
<td>MVI Person Service Identity Management (PSIM)</td>
</tr>
<tr class="even">
<td>Internal</td>
<td>Veteran Information/Eligibility Record Services (VIERS)</td>
<td>Enrollment Data to support Affordable Care Act (ACA), nd eMIS queries from the Content Management System (CMS)</td>
<td>ACA interface</td>
<td>VIERS</td>
</tr>
<tr class="odd">
<td>Internal</td>
<td>VA/DoD Identity Repository (VADIR)</td>
<td>To retrieve Military Service Data</td>
<td>Enterprise Military Information Service (eMIS)</td>
<td><p>VADIR/</p>
<p>Beneficiary Identification Records Locator System (BIRLS)</p></td>
</tr>
<tr class="even">
<td>Internal</td>
<td>Corporate Data Warehouse (CDW)</td>
<td>To retrieve Primary Care Provider Data</td>
<td>Preferred Facility</td>
<td>CDW</td>
</tr>
<tr class="odd">
<td>External</td>
<td>CMS</td>
<td>To print and mail handbooks and inserts</td>
<td>Handbook</td>
<td>NPC</td>
</tr>
<tr class="even">
<td>Internal</td>
<td>IVM</td>
<td>To share person data and receive case decisions (conversions/reversals) and predetermine the enrollment</td>
<td>IVM bi-directional</td>
<td>IVM</td>
</tr>
<tr class="odd">
<td>Internal</td>
<td>Veterans Benefits Handbook</td>
<td>To allow Veterans to access on-demand personalized and dynamic health benefits-related handbook</td>
<td>Handbook Portal</td>
<td>VOA</td>
</tr>
<tr class="even">
<td>External</td>
<td>National Change of Address (NCOA)</td>
<td>To receive address corrections</td>
<td>Address Verification</td>
<td>NCOA</td>
</tr>
<tr class="odd">
<td>Internal</td>
<td>Master Veteran Record (MVR)</td>
<td>Sending of solicited eligibility/enrollment information and the receiving of unsolicited eligibility/enrollment information</td>
<td>MVR</td>
<td>Veterans Benefit Administration (VBA)</td>
</tr>
<tr class="even">
<td>Internal</td>
<td>VistA</td>
<td>Sending of solicited eligibility/enrollment information and the receiving of unsolicited eligibility/enrollment information</td>
<td>VistA</td>
<td>VistA REE</td>
</tr>
<tr class="odd">
<td>Internal</td>
<td>Veteran Health Identification Card (VHIC)</td>
<td>Query Veteran's identity card details and status</td>
<td>VHIC interface</td>
<td>VHIC</td>
</tr>
<tr class="even">
<td>External</td>
<td>IRS</td>
<td>Service provider for the 1095B coverage period transactions</td>
<td>IRS</td>
<td>IRS</td>
</tr>
<tr class="odd">
<td>External</td>
<td>Third Party Administrators (TPA)</td>
<td>Sending Community Care (CC) eligibility and demographics data</td>
<td>TPA</td>
<td>Secure File Transfer Protocol (SFTP)</td>
</tr>
<tr class="even">
<td>External</td>
<td>Community Care Network (CCN) contractors</td>
<td>Sending Community Care (CC) eligibility and demographics data</td>
<td>CCN</td>
<td>Data Access Services (DAS)</td>
</tr>
<tr class="odd">
<td>Internal</td>
<td>VET360</td>
<td>Authoritative contact information service for validating delivery point on addresses</td>
<td>VET360</td>
<td>VET360</td>
</tr>
</tbody>
</table>

Table : Role Identification

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information to assist with resolving error conditions that may be encountered with the ES.

Scenario 1: Missing Inbound Message

Troubleshooting Steps

1.  Which site sent the message?

> This can be found in the BHS segment. In the below example, the Z07 came from VA Medical Center (VAMC) 552.

> BHS^~\|\\^VAMC 552^552^ESR^200ESR^20040810^^~T~ORU\|Z07~2.3.1~AL~AL^^54364365^

2.  What are the Batch Control Number and Message Control Number?

> In the below example, 54364365 is the batch control number and 88865050-1 is the message control number.

> BHS^~\|\\^VAMC 552^552^ESR^200ESR^20040810^^~T~ORU\|Z07~2.3.1~AL~AL^^54364365^

> MSH^~\|\\^VAMC 552^552^ESR^200ESR^20030904121212-0500^^ORU~Z07^88865050-1^T^2.1^^^AL^AL^USA

3.  What Person is contained in the HL7 message?

> The Data File Number (DFN) is in the PI section of the PID segment. In this example, 55202 is the DFN.

> PID^1^1000913833V082573^1000913833V082573\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|55202\~\~~

> USVHA&&0363~PI~VA FACILITY ID&500&L\|000004834\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\|666123456\~\~~USSSA&&0363~SS~VA FA

> CILITY ID&500&L\~~20060127\|000123456\~\~~USSSA&&0363~SS~VA FACILITY ID&500&L\~~20060127^^ESRPATIENT~FNAME~X\~\~~^^19270101^M^^^557 OREGONS~""~LITTLE FALLS~NY~13333-1633~USA~VACAE~STE 322\~\~\~~20020125&20060125\|3400 EDS DRIVE~""~HERNDON~VA~20171-1633~USA~P~STE 322\~\~\~~20020125&20060125^^

> (999)123-0001~PRN~PH\|(999)123-0002~WPN~PH\|(999)123-0003~ORN~CP\|(999)123-0004~BPN~BP\|~NET~INTERNET~EMAIL@FOO.COM^(999)123-0005X3464

> ^^^^^1346

4.  When was the message sent?

> The message below was sent on 8/10/2004

> BHS^~\|\\^VAMC 552^552^ESR^200ESR^20040810^^~T~ORU\|Z07~2.3.1~AL~AL^^54364365^

5.  Query the database for the message.

> If the message is not found in the database then either ES has not received it, or it is still in the inbound JMS queue waiting to be processed.

> Find a Message by Message Control Id (replace number)

> Select message_control_number, record_created_by, to_char(record_created_date, 'mm/dd/yyyy hh:mi:ss') from hl7_transaction_log where message_control_number='88865050-1'

6.  Look at the backlog of messages on JMS queue (using Introscope).

> Note: A high volume of messages in MessagesCurrentCount for a particular JMS queue would indicate that there are messages that ES has not yet processed.

7.  Check with VIE, as to the status of the message

> VIE will typically need the Batch Control ID to track it down in their JMS queues.

Scenario 2: Missing Outbound Message

Troubleshooting Steps

1.  First look in the HL7_TRANSACTION_LOG table for the Message Control ID.

> Select message_control_number, record_created_by, to_char(record_created_date, 'mm/dd/yyyy hh:mi:ss') from HL7_transaction_log where message_control_number='88865050-1'

8.  If it is not found in HL7_TRANSACTION_LOG, then check whether ES triggered this outbound message at all?

> Look in triggerEvent.log in XpoLog

> Note: Search for personId=xxx

9.  Is there a Consistency Check failure that occurred in Cluster1?

> The following would be found in the esr.log for the outbound managed server:

> \[ERROR\] 21 Aug 03:45:25.467 PM ExecuteThread: '8' for queue: 'OutboundMessageThreadPool' \[REDACTED.messaging.util.MessagingWorkloadCaseHelper\]

> Create ConsistencyCheck WorkloadCase for group \[Enrollment Eligibility\] and target Person \[133156322\] for target Message \[ORUZ05-S\]

10. Is there a Workload Case created?

> Replace with personId and *n* in the following.

> Select \* from wkf_Case where person_ID=2 and rownum\<20 order by record_created_date desc

11. Look in esr.log in Cluster1.
12. If everything looks okay in ES, contact the VIE team, giving them the Batch Control ID or Message Control ID.

Scenario 3: Batch Process Taking Too Long

Troubleshooting Steps

1.  Confirm if the batch process is still running. This may not always be straightforward.
- Look for the batch process' execution in the esr.log file.

> \[INFO\] 22 Aug 03:10:00.043 AM ExecuteThread: '13' for queue: 'InternalEventThreadPool'

> \[REDACTED.BatchProcessServiceImpl\]

> Executing job/process \[scheduledJob.dataSynchronizationHECLegacyProducer\] for executionContext/user \[AUTO_PER_SCHEDULE\]

- Find the thread ID running the batch process.
- Look for subsequent log statements with the thread ID.

> \[INFO\] 22 Aug 03:10:01.106 AM ExecuteThread: '13' for queue: 'InternalEventThreadPool' \[REDACTED.common.batchprocess.datasync.HECLegacyDataSynchronizationProducerProcess\]

> AbstractDataQueryIncrementalProcess acquired 65 data records

- Do a few refreshes for the view on the Batch Processes -\> Active tab. If the number of records does not change after several refreshes, then check the history of the job on the management tab. An entry with a status of NOT_EXECUTED_SINCE_INFLIGHT_PROCESS can indicate that the server restarted, and the batch job is therefore stalled.
13. If the batch process is running, look at database statistics from Prod Database Service (DBS) and/or Introscope.
14. If the batch process is not running, mark as ERROR from the user interface to clean up the view.
15. If the batch job is scheduled to execute again within 12 hours, then wait for the job to start automatically at the next scheduled start time. Otherwise, restart the job by clicking the execute hyperlink for the batch job listed on the Batch Processes tab.

Scenario 4: NumberOfErrorRecords

For a batch process, what is the reason for the numberOfErrorRecords=n, where n is not 0?

Troubleshooting Steps

1.  Find the batch process' execution in esr.log.
2.  Determine the thread ID.
3.  Look for any exceptions that follow for that thread ID. Threads get reused once they are complete, so the thread may be used by another process later on.
4.  Analyze the exceptions found, and work with Level 3 support to resolve them.

> Note: Some batch jobs write exceptions to an .exception file. The ones that do this are: IVM Producer and Austin Automation Center (AAC) Letter Export.

Scenario 5: eMIS Query Status in "Queried – Pending Response"

This scenario assumes that a Veteran record was already identified.

Troubleshooting Steps

1.  Contact the "OIT EPMO TRS EPS SoS Weblogic Support" mail group in Outlook REDACTED asking them to check the status of the ES Enterprise Military Information Service (eMIS) Web service.
5.  Contact Tier 3 support.

Scenario 6: Users Getting No Response

Users of the ES Eligibility & Enrollment Web Service say they are not getting a response.

Troubleshooting Steps

1.  Contact the "OIT EPMO TRS EPS SoS Weblogic Support" mail group in Outlook REDACTED asking them to check the status of the ES Eligibility and Enrollment Service (EES) Web service.
6.  Contact Tier 3 support.

Scenario 7: Outbound Messages Missing Troubleshooting Steps

Troubleshooting Steps

1.  Contact the "OIT EPMO TRS EPS SoS Weblogic" mail group in Outlook (REDACTED), asking them to check the person id for the missing message in cluster 1 logs. If the person id is not found, request them to check status of the messaging event queue to see if there are any pending messages in the queue.
7.  Contact Tier 3 support.

Scenario 8: PSIM Web Service Interface Failing Axis Fault Error

Troubleshooting Steps

1.  If you see error message like "Caused by: javax.net.ssl.SSLHandshakeException: Received fatal alert: certificate_expired".
8.  Contact the "OIT EPMO TRS EPS SoS Weblogic" mail group in Outlook (REDACTED asking them to check the logs for any certificate errors or VAAFI connection errors. If there are certificate or VAAFI connectivity errors, contact the VAAFI support team.

Scenario 9: HBP Data in ES Not Being Transmitted to Sites

Troubleshooting Steps

1.  Verify a Z11 was transmitted from ES to the sites; Verify the Z11 contains the ZHP segment
16. Login to ES, then navigate to Admin -\> System Parameters. Verify the system parameter named Health Benefit Plans (HBP) Data sharing indicator is set to "Y" to enable the ZHP segment to be included in the Z11 messages to the sites.
17. Contact Tier 3 support.

Scenario 10: Enrollment Records in VistA CL = Yes Patient Not Eligible

Troubleshooting Steps

1.  Verify a Z11 was transmitted from ES to the sites; Verify the Z11 contains the ZHP segment. Verify a Z11 was transmitted from ES to the sites; Verify the Z11 does not contain Camp Lejeune data on the ZEL segment.
18. Login to ES, and then navigate to Admin -\> System Parameters. Verify the system parameter named CL_VISTA_FULL_ROLLOUT is set to "ALL" or has the site in the delimited field to enable the Camp Lejeune information to be included in the Z11 messages to the sites.
19. Contact Tier 3 support.

> Note: The system parameter CL_VISTA_FULL_ROLLOUT needs to be set to "all". This is done by the HEC System Administrator when the CL-V VistA host file DG\*5.3\*909 is deployed to production. This system parameter should never be inactivated.

## System Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process and procedures necessary for system recovery are managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

### Restart after Non-Scheduled System Interruption 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process and procedures necessary to restart after a non-scheduled system interruption are managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

### Restart after Database Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The process and procedures necessary to restart after a database restore are managed by the Austin Information Technology Center (AITC) and handled by the AITC system administrators.

### Back-out Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For back-out procedures, refer to the *ES 5.3 Deployment, Installation, Back-out, and Rollback Guide*.

### Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For rollback procedures, refer to the *ES 5.3 Deployment, Installation, Back-out, and Rollback Guide*

# Operations and Maintenance Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The role identification list and subsequent RACI matrix are customized according to the requirements of each system.

<table>
<caption>Primary Operational Support Entities &amp; FTEs table in support of EHBD, including name, role, Gov/non-Gov, FTE (man hours/yr), org, and contact information for each employee</caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Role</th>
<th>Org</th>
<th>Contact Info</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>REDACTED</td>
<td>Program Manager</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>National Service Desk Dev/Ops (PD/ESE)</td>
<td>National Service Desk Tier 1</td>
<td>ITOPS</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>VA IT SDE EO EIS VHA Linux System Admins<br />
Tier 2</td>
<td>System Admin (Unix)</td>
<td>AITC</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>REDACTED<br />
Tier 2</td>
<td>System Admin (Windows)</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>REDACTED<br />
Tier 2</td>
<td>System Admin (Windows)</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>REDACTED</td>
<td>Linux Admin</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td><p>REDACTED</p>
<p>Tier 2</p></td>
<td>Application Manager</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>REDACTED<br />
Tier 2</td>
<td>Application Manager</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>REDACTED<br />
Tier 2</td>
<td>Application Manager</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>REDACTED<br />
Tier 2</td>
<td>Database Administrator</td>
<td>AITC</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>REDACTED<br />
Tier 2</td>
<td>Database Administrator</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>REDACTED<br />
Tier 2</td>
<td>WebLogic Administrator</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>REDACTED<br />
Tier 2</td>
<td>Monitoring</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>REDACTED<br />
Tier 2</td>
<td>Build Manager</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td><p>REDACTED</p>
<p>Tier 2</p></td>
<td>Build Manager</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>REDACTED<br />
Tier 2</td>
<td>Build Manager</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>REDACTED<br />
Tier 2</td>
<td>Solaris (IVM)</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>REDACTED<br />
Tier 2</td>
<td>Linux (IVM)</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>REDACTED<br />
Tier 2</td>
<td>Database Administrator (IVM)</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>REDACTED</td>
<td>Messaging (IVM)</td>
<td>AITC</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>Health Product Support<br />
Tier 2</td>
<td>Application Support</td>
<td>EPMO</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>REDACTED<br />
Tier 3</td>
<td>Program Manager<br />
EHBD</td>
<td>EPMO</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>REDACTED<br />
Tier 3</td>
<td>Project Manager<br />
ES</td>
<td>EPMO</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td><p>REDACTED</p>
<p>Tier 3</p></td>
<td>Project Manager<br />
ES</td>
<td>EPMO</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>REDACTED<br />
Tier 3</td>
<td>Technical Lead<br />
EHBD</td>
<td>EPMO</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
</tbody>
</table>

Primary Operational Support Entities & FTEs table in support of EHBD, including name, role, Gov/non-Gov, FTE (man hours/yr), org, and contact information for each employee

Attached is the IO Hosting Services Responsibility Matrix, ESR-17-103.

REDACTED

# Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REDACTED

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REDACTED

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REDACTED

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

REDACTED