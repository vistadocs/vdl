---
title: InterSystems Health Connect - HL7 Messaging Production Operations Manual (POM) - Master
doc_type: POM
doc_label: Production Operations Manual
doc_layer: plain
doc_subject: InterSystems Health Connect - HL7 Messaging  (POM) - Master
app_code: PRC
app_name: IFCAP
section: FIN
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 3
description: > This Production Operations Manual (POM) describes how to maintain the components of the InterSystems Health Level Seven (HL7) Health Connect (HC) messaging system. It also describes how to troubleshoot problems that might occur with this system in production. The intended audience for this documen
audience: 
keywords: 
  - blockquote
  - class
  - strong
  - table
  - contents
  - style
  - width
  - span
  - bookmark
  - colspan
page_count: 0
word_count: 15329
section_count: 20
table_count: 0
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: August 1999
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/hc_hl7_messaging_pom-signed.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/hc_hl7_messaging_pom-signed.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

# InterSystems Health Connect – HL7 Messaging Production Operations Manual (POM)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [InterSystems Health Connect – HL7 Messaging Production Operations Manual (POM)](#intersystems-health-connect-hl7-messaging-production-operations-manual-pom)
    - [August 1999](#august-1999)
    - [Department of Veterans Affairs (VA) Office of Information and Technology (OIT)](#department-of-veterans-affairs-va-office-of-information-and-technology-oit)
    - [Artifact Rationale](#artifact-rationale)
    - [List of Tables](#list-of-tables)
- [Introduction](#introduction)
- [Routine Operations](#routine-operations)
  - [System Management Portal (SMP)](#system-management-portal-smp)
  - [Access Requirements](#access-requirements)
  - [Administrative Procedures](#administrative-procedures)
    - [System Start-Up](#system-start-up)
    - [System Shut-Down](#system-shut-down)
    - [Back-Up & Restore](#back-up-restore)
  - [Security / Identity Management](#security-identity-management)
    - [Identity Management](#identity-management)
    - [Access Control](#access-control)
    - [Audit Control](#audit-control)
  - [User Notifications](#user-notifications)
    - [User Notification Points of Contact](#user-notification-points-of-contact)
  - [System Monitoring, Reporting, & Tools](#system-monitoring-reporting-tools)
    - [Support](#support)
    - [Monitor Commands](#monitor-commands)
    - [Other Options](#other-options)
    - [Dataflow Diagram](#dataflow-diagram)
    - [Availability Monitoring](#availability-monitoring)
    - [High Availability Mirror Monitoring](#high-availability-mirror-monitoring)
    - [System/Performance/Capacity Monitoring](#systemperformancecapacity-monitoring)
    - [Critical Metrics](#critical-metrics)
  - [Routine Updates, Extracts, and Purges](#routine-updates-extracts-and-purges)
    - [Purge Management Data](#purge-management-data)
  - [Scheduled Maintenance](#scheduled-maintenance)
    - [Switch Journaling Back from AltJournal to Journal](#switch-journaling-back-from-altjournal-to-journal)
  - [Capacity Planning](#capacity-planning)
    - [Initial Capacity Plan](#initial-capacity-plan)
- [Exception Handling](#exception-handling)
  - [Routine Errors](#routine-errors)
    - [Security Errors](#security-errors)
    - [Time-Outs](#time-outs)
    - [Concurrency](#concurrency)
  - [Significant Errors](#significant-errors)
    - [Application Error Logs](#application-error-logs)
    - [Application Error Codes and Descriptions](#application-error-codes-and-descriptions)
    - [Infrastructure Errors](#infrastructure-errors)
  - [Dependent System(s)](#dependent-systems)
  - [Troubleshooting](#troubleshooting)
  - [System Recovery](#system-recovery)
    - [Manually Initiate a HealthShare Mirror Failover](#manually-initiate-a-healthshare-mirror-failover)
    - [Recover from a HealthShare Mirror Failover](#recover-from-a-healthshare-mirror-failover)
    - [Restart after Non-Scheduled System Interruption](#restart-after-non-scheduled-system-interruption)
    - [Restart after Database Restore](#restart-after-database-restore)
    - [Back-Out Procedures](#back-out-procedures)
    - [Rollback Procedures](#rollback-procedures)
- [Operations and Maintenance Responsibilities](#operations-and-maintenance-responsibilities)
  - [RACI Matrix](#raci-matrix)
- [Approval Signatures](#approval-signatures)
- [Appendix A—Products Migrating from VIE to HL7 Health Connect](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect)
  - [Pharmacy Automated Dispensing Equipment (PADE)](#pharmacy-automated-dispensing-equipment-pade)
    - [Review PADE System Default Settings](#review-pade-system-default-settings)
    - [Review PADE Router Lookup Settings](#review-pade-router-lookup-settings)
    - [PADE Troubleshooting](#pade-troubleshooting)
    - [PADE Rollback Procedures](#pade-rollback-procedures)
    - [PADE Business Process Logic (BPL)](#pade-business-process-logic-bpl)
    - [PADE Approval Signatures](#pade-approval-signatures)
  - [Outpatient Pharmacy Automation Interface (OPAI)](#outpatient-pharmacy-automation-interface-opai)
    - [Review OPAI System Default Settings](#review-opai-system-default-settings)
    - [Review OPAI Router Lookup Settings](#review-opai-router-lookup-settings)
    - [OPAI Troubleshooting](#opai-troubleshooting)
    - [OPAI Rollback Procedures](#opai-rollback-procedures)
    - [OPAI Business Process Logic (BPL)](#opai-business-process-logic-bpl)
    - [OPAI Approval Signatures](#opai-approval-signatures)
- [Appendix B—Configuring Alert Email Notifications](#appendix-bconfiguring-alert-email-notifications)
  - [Configure Level 2 Alerting](#configure-level-2-alerting)
  - [Configure Email Alert Notifications](#configure-email-alert-notifications)
![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/001.png)

### August 1999

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Department of Veterans Affairs (VA) Office of Information and Technology (OIT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Revision History
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>08/06/1999</p>
</blockquote></td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>Tech Edit Review:</p>
</blockquote>
<ul>
<li><p>Corrected OPAI acronym to “Outpatient Pharmacy Automation Interface” throughout.</p></li>
<li><p>Corrected/Updated formatting throughout.</p></li>
<li><p>Corrected Table and Figure captions and cross-references throughout.</p></li>
<li><p>Verified document is Section 508 conformant.</p></li>
</ul></td>
<td><blockquote>
<p>VA Tech Writer: REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>08/02/1999</p>
</blockquote></td>
<td><blockquote>
<p>1.4</p>
</blockquote></td>
<td><blockquote>
<p>Updates:</p>
<p>Added OPAI Section <a href="#outpatient-pharmacy-automation-interface-opai"><u>6.2,</u> “<u>Outpatient</u></a> <a href="#outpatient-pharmacy-automation-interface-opai"><u>Pharmacy Automation Interface (OPAI)</u></a>”</p>
</blockquote></td>
<td><blockquote>
<p>Halfaker and Associates</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>07/12/1999</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>Updates:</p>
</blockquote>
<ul>
<li><p>Added Section <a href="#manually-initiate-a-healthshare-mirror-failover"><u>3.5.1</u></a>, “<a href="#manually-initiate-a-healthshare-mirror-failover"><u>Manually</u> <u>Initiate a HealthShare Mirror Failover</u></a>.”</p></li>
<li><p>Added Section <a href="#recover-from-a-healthshare-mirror-failover"><u>3.5.2</u></a>, “<a href="#recover-from-a-healthshare-mirror-failover"><u>Recover from a</u> <u>HealthShare Mirror Failover</u></a>.”</p></li>
</ul></td>
<td><blockquote>
<p>FM24 Project Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04/24/1999</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>Updates:</p>
</blockquote>
<ul>
<li><p>Added PADE Section <a href="#review-pade-system-default-settings"><u>6.1.1</u></a>, “<a href="#review-pade-system-default-settings"><u>Review</u> <u>PADE System Default Settings</u></a>.”</p></li>
<li><p>Added PADE Section <a href="#review-pade-router-lookup-settings"><u>6.1.2</u></a>, “<a href="#review-pade-router-lookup-settings"><u>Review</u> <u>PADE Router Lookup Settings</u></a>.”</p></li>
</ul></td>
<td><blockquote>
<p>FM24 Project Team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04/23/1999</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>Updates:</p>
</blockquote>
<ul>
<li><p>Added Section <a href="#high-availability-mirror-monitoring"><u>2.6.6</u></a>, “<a href="#high-availability-mirror-monitoring"><u>High Availability</u> <u>Mirror Monitoring</u></a>” and subsections based on feedback from P.B. and J.W.</p></li>
<li><p>Added the following sections:</p>
<ul>
<li><p>“<a href="#monitoring-system-alerts"><u>Monitoring System Alerts</u></a>.”</p></li>
<li><p>“<a href="#console-log-page"><u>Console Log Page</u></a>.”</p></li>
<li><p>“<a href="#level-2-use-case-scenarios-2.6.6.4.2.1-use-case-1"><u>Level 2 Use Case Scenarios</u></a>.”</p></li>
</ul></li>
<li><p>Updated the “<a href="#purge-journal-files"><u>Purge Journal Files</u></a>” section.</p></li>
<li><p>Moved email notification setup instructions to “<a href="#7_Appendix_B—Configuring_Alert_Email_Not"><u>Appendix B—</u> <u>Configuring Alert Email Notification</u></a>.” This section may later be moved to a separate install guide.</p></li>
</ul></td>
<td><blockquote>
<p>FM24 Project Team</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><ul>
<li><p>Replaced and scrubbed some images to remove user names.</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04/03/1999</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Initial signed, baseline version of this document was based on VIP Production Operations Manual Template: Version 1.6; Mach 2016.</p>
<p>04/06/1999: The PDF version of this document was signed off in the “<a href="#pade-approval-signatures"><u>PADE</u></a> <a href="#pade-approval-signatures"><u>Approval Signatures</u></a>” section.</p>
<p>For earlier document revision history, see the earlier document versions stored in the EHRM FM24 Documentation stream in Rational Jazz RTC.</p>
</blockquote></td>
<td><blockquote>
<p>FM24 Project Team</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Production Operations Manual provides the information needed by the production operations team to maintain and troubleshoot the product. The Production Operations Manual *must* be provided prior to release of the product.

### List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table 10: OPAI System IP Addresses/DNS—Production (will be updated once in](#_bookmark225) [production) 89](#_bookmark225)
> [Table 11: OPAI—Common Issues and Resolutions 91](#_bookmark236)
> [Table 12: OPAI—Alerts 97](#_bookmark249)
> [Table 13: Manage Email Options Menu Options 102](#_bookmark257)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This Production Operations Manual (POM) describes how to maintain the components of the InterSystems Health Level Seven (HL7) Health Connect (HC) messaging system. It also describes how to troubleshoot problems that might occur with this system in production. The intended audience for this document is the Office of Information and Technology (OIT) teams responsible for hosting and maintaining the system after production release. This document is normally finalized just prior to production release, and includes many updated elements specific to the hosting environment.

> InterSystems has an Enterprise Service Bus (ESB) product called Health Connect (HC):

- Health Level Seven (HL7) Health Connect—Includes projects above the line (e.g., [<u>PADE</u>](#pharmacy-automated-dispensing-equipment-pade) and [<u>OPAI</u>](#outpatient-pharmacy-automation-interface-opai)).
- HealthShare Enterprise (HSE) Health Connect—Pushes data from Veterans Health Information Systems and Technology Architecture (VistA) into Health Connect.

> Health Connect provides the following capabilities:

- HL7 Messaging between VistA and VAMC Local Devices in all Regions.
- HL7 Messaging between VistA instances (intra Region and between Regions).
- HSE VistA data feeds between the national HSE instances (HSE-AITC, HSE-PITC, and HSE-Cloud) and the regional Health Connect instances.

> Electronic Health Record Modernization (EHRM) is currently deploying the initial HC capability into each of the VA regional data centers with a HealthShare Enterprise (HSE) capability in the VA enterprise data centers.

> HealthShare Enterprise Platform (HSEP) Health Connect instance pairs are expanded to all VA Regional Data Centers (RDCs) enabling HL7 messaging for other applications (e.g., [<u>PADE</u>](#pharmacy-automated-dispensing-equipment-pade) and [<u>OPAI</u>](#outpatient-pharmacy-automation-interface-opai)) in all regions.

> Primary Health Connect pairs (for HL7 messaging and HSE VistA data feeds) are deployed to all regions to align with production VistA instances in both RDC pairs.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/002.png) NOTE: This POM describes the functionality, utilities, and options available with the HL7 Health Connect system.

# Routine Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes, at a high-level, what is required of an operator/administrator or other *non*- business user to maintain the system at an operational and accessible state.

## System Management Portal (SMP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The System Management Portal (SMP) provides access to the HL7 Health Connect utilities and options (see [<u>Figure 1</u>](#_bookmark3)). These utilities and options are used to maintain and monitor the HL7 Health Connect system.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/003.png)<span id="_bookmark3" class="anchor"></span>Figure 1: System Management Portal (SMP)

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/004.png) REF: For more information on these utilities and options, see the InterSystems documentation at: [<u>http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=EGMG_int</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=EGMG_intro&EGMG_intro_portal) [<u>ro#EGMG_intro_portal</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=EGMG_intro&EGMG_intro_portal)

> Specifically, for more information on the Ensemble System Monitor: [<u>http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=EMONITO</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=EMONITOR_all) [<u>R_all</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=EMONITOR_all)

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/005.png) NOTE: Use of the SMP is referred to throughout this document.

## Access Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is important to note that all users who maintain and monitor the HL7 Health Connect system

> *must* have System Administrator level access with elevated privileges.

## Administrative Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### System Start-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to start the Health Connect system on Linux and bring it to an operational state.

> To start Health Connect, do the following:

1.  <span id="_bookmark7" class="anchor"></span>Run the following command before system startup:

> ccontrol list

> This Caché command displays the currently installed instances on the server. It also indicates the current status and state of the installed instances. For example, you may see the following State indicated:

- ok—No issues.
- <span id="_bookmark8" class="anchor"></span>alert—Possible issue, you need to investigate.

> Figure 2: Using the “control list” Command—Sample List of Installed Instances and their Status and State on a Server

2.  Boot up servers.
3.  Start Caché on database (backend) servers. Run the following command:

> cstart *\<instance name\>*

4.  Start Caché on Application servers. Run the following command:

> cstart *\<instance name\>*

5.  Start Health Level Seven (HL7).
6.  Verify the startup was successful. Run the ccontrol list command (see [<u>Step 1</u>](#_bookmark7)) to verify all instances show the following:
    - Status: Running
    - State: ok

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/006.png) REF: For a list of Veterans Health Information Systems and Technology Architecture (VistA) instances by region, see the HC_HL_App_Server_Standards_All_Regions_MASTER.xlsx Microsoft<sup>®</sup> Excel document located at: [<u>http://go.va.gov/sxcu</u>](http://go.va.gov/sxcu).

#### VMS Commands

> The following procedure checks CACHE\$LOGS:SCD_BKUP_DDMMMYYY.LOG file:

> CACHE\$BKUP:CHECK-BACKUP-COMPLETE.COM

> This procedure checks any backups that started the previous day after 07:00. It does the following:

1.  Checks for messages that say "Warning!" Errors could be VMS errors (e.g., space issues, -E-, -F-, devalloc, etc.), quiescence errors, and cache incremental backup errors.
2.  If VMS errors are found, it checks the SCD.LOG for "D2D-E-FAILED" messages, all other messages are non-fatal.
3.  Checks for integrity errors, "ERRORS \*\*\*" and "ERROR \*\*\*".
4.  Checks for "Backup failed" message, which is the failure of the cache incremental restore.
5.  If backup completely fails, there will be no log file to check, message will be printed.
6.  If backup all successful, journal files older than 5 days will be deleted unless logical is set.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/007.png) REF: See DONT-DEL-OLD_JOURN.

> Backup check will be submitted for the next day.

> Report is mailed out at 7:00 a.m. to VMS mail list MAIL\$DIST:BKUP_CHK.DIS.

> <span id="_bookmark9" class="anchor"></span>Figure 3: Sample Backup Check Report

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 26%" />
<col style="width: 19%" />
<col style="width: 25%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>BAL</p>
</blockquote></th>
<th>15-AUG-2010</th>
<th><blockquote>
<p>17:00:00</p>
</blockquote></th>
<th>15-AUG-2010</th>
<th><blockquote>
<p>22:53:00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>WBP</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>16:45:00</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>20:48:53</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PHI</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>16:45:00</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>21:55:16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ALT</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>17:00:00</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>19:59:07</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BUT</p>
</blockquote></td>
<td>16-AUG-2010</td>
<td><blockquote>
<p>00:25:00</p>
</blockquote></td>
<td>16-AUG-2010</td>
<td><blockquote>
<p>01:47:40</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ERI</p>
</blockquote></td>
<td>16-AUG-2010</td>
<td><blockquote>
<p>00:20:00</p>
</blockquote></td>
<td>16-AUG-2010</td>
<td><blockquote>
<p>01:48:09</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LEB</p>
</blockquote></td>
<td>16-AUG-2010</td>
<td><blockquote>
<p>00:15:00</p>
</blockquote></td>
<td>16-AUG-2010</td>
<td><blockquote>
<p>02:33:19</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CLA</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>16:00:00</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>19:24:07</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BHS</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>16:45:00</p>
</blockquote></td>
<td>15-AUG-2010</td>
<td><blockquote>
<p>23:21:01</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NOP</p>
</blockquote></td>
<td>16-AUG-2010</td>
<td><blockquote>
<p>00:30:00</p>
</blockquote></td>
<td>16-AUG-2010</td>
<td><blockquote>
<p>03:31:17</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### System Start-Up from Emergency Shut-Down

> If a start-up from a power outage or emergency shut-down occurs, do the following procedures to restart the HL7 Health Connect system:

> ccontrol start \$*instance*

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/008.png) REF: For a list of VistA instances by region, see the HC_HL_App_Server_Standards_All_Regions_MASTER.xlsx Microsoft<sup>®</sup> Excel document located at: [<u>http://go.va.gov/sxcu</u>](http://go.va.gov/sxcu).

### System Shut-Down

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to shut down the system and bring it to a *non*-operational state. This procedure stops all processes and components. The end state of this procedure is a state in which you can apply the start-up procedure.

> To shut down the system, do the following:

1.  Disable TCPIP services.
2.  Shut down HL7.
3.  Shut down TaskMan.
4.  Shut down Caché Application servers.
5.  Shut down Caché Database servers.
6.  Shut down operating system on all servers.

> To restart the HL7 Health Connect system, run the following command:

> ccontrol start \$*instance*

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/009.png) REF: For a list of VistA instances by region, see the HC_HL_App_Server_Standards_All_Regions_MASTER.xlsx Microsoft<sup>®</sup> Excel document located at: [<u>http://go.va.gov/sxcu</u>](http://go.va.gov/sxcu).

#### Emergency System Shut-Down

> This section guides personnel through the proper emergency system shutdown, which is different from a normal system shutdown, to avoid potential file corruption or component damage.

### Back-Up & Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section is a high-level description of the system backup and restore strategy.

#### Back-Up Procedures

> This section describes the installation of the Restore configuration and creation of the Linux files associated with the Backup process, as well as a more in depth look at the creation and maintenance of the site backup.dat file.

#### Access Required

> To perform the tasks in this section, users *must* have root level access.

#### Discussion Topics

> The following topics are described in this section:

- [<u>Installing Backup (rdp_bkup_setup Script)</u>](#installing-backup-rdp_bkup_setup-script)
- [<u>Maintaining Backup Parameter File (backup.dat)</u>](#maintaining-backup-parameter-file-backup.dat)
- [<u>Scheduling and Managing Backups</u>](#scheduling-and-managing-backups)
- [<u>Monitoring Backup Process</u>](#monitoring-backup-process)
- [<u>Monitoring Backup Log Files</u>](#monitoring-backup-log-files)

#### Installing Backup (rdp_bkup_setup Script)

> The installation of the Restore configuration and the backup scripts is typically done when the site’s Caché instance is originally installed. Although this should *not* need to be done more than once, the steps for the Backup installation are included below.

> All backup scripts are located in the following Linux directory:

#### /usr/local/sbin

> The rdp_bkup_setup script installs the Caché RESTORE configuration, creates backup users and groups, and creates the backup.dat.

1.  Verify that all BKUP files are present on all cluster members.

> <span id="_bookmark16" class="anchor"></span>Figure 4: Verify All BKUP Files are Present on All Cluster Members (Sample Code)

2.  Run the BKUP setup script.

> <span id="_bookmark17" class="anchor"></span>Figure 5: Run the BKUP Script (Sample Code)

> \#\] rdp_bkup_setup *\<scd\>*

> No remote system IP or hostname specified. Installation for local backup.

> Created OS EXAMPLEusr account... Generating public/private rsa key pair.

> Your identification has been saved in /home/EXAMPLEusr/.ssh/id_rsa. Your public key has been saved in /home/EXAMPLEusr/.ssh/id_rsa.pub. The key fingerprint is: bf:6d:44:dc:30:32:7c:5e:8f:53:4d:c3:f4:0b:d4:51

> [REDACTED](mailto:farbckusr@r02smodhcd082.r02.med.va.gov)

> The key's randomart image is:

> +--\[ RSA 2048\] +

> \+ +

> Please review the installation options:

> Instance name: restore

> Destination directory: /usr/local/cachesys/restore Cache version to install: 2011.1.2.701.0.11077 Installation type: Custom

> Unicode support: N

> Initial Security settings: Normal User who owns instance: cachemgr

> Group allowed to start and stop instance: cachemgr Effective group for Cache processes: cacheusr Effective user for Cache SuperServer: cacheusr SuperServer port: REDACTED

> WebServer port: REDACTED

> JDBC Gateway port: REDACTED

> CSP Gateway: using built-in web server Client components:

> ODBC client C++ binding C++ SDK

> Do you want to proceed with the installation \<Yes\>? Y

> Starting installation...

3.  Place the CV token file.
4.  Edit/Verify the /etc/aliases file to ensure that the Region specific Backup Mail Group is defined (this file can be deployed from the Red Hat Satellite Server for consistency).

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/010.png) REF: For more information on the Red Hat Satellite Server, see [<u>https://www.redhat.com/en/technologies/management/satellite</u>](https://www.redhat.com/en/technologies/management/satellite) or contact VA Satellite Admins: REDACTED

> <span id="_bookmark18" class="anchor"></span>Figure 6: Edit/Verify the /etc/aliases File (Sample Code)

5.  Run the vgs command to calculate how much free space remains within your

> <span id="_bookmark19" class="anchor"></span>vg\_*\<scd\>*\_vista volume group.

> Figure 7: Run the vgs Command (Sample Code)

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/011.png) NOTE: The space highlighted in [<u>Figure 7</u>](#_bookmark19) is provided by the snap PVs and is used to create the temporary LVM snapshot copies used during the BKUP process.

6.  Open the backup definition file for editing. You need to adjust the snap disk sizes, integrity thread ordering and days to keep bkups.

> <span id="_bookmark20" class="anchor"></span>Figure 8: Open Backup Definition File for Editing (Sample Code)

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/012.png) NOTE: Since database access during backup hours is usually more READs than

> WRITEs, you can do the following:

- Size the LVM snaps to be between 40% - 50% of the origin volume without issue.
- Change the days to keep value from 3 to 2.
- Arrange the integrity threads, so that you evenly spread the load; keeping in mind that by default you run 3 threads.

#### Maintaining Backup Parameter File (backup.dat)

> Access Level Required

> To maintain the backup parameter file (i.e., backup.dat), users *must* have root level access.

#### File Location and Description

> The backup.dat file is located in the following directory:

#### /example/*\<scd\>*/user/backup/

> The original *\<scd\>*backup.dat file is created when the rdp_bkup_setup script is run. The *\<scd\>*backup.dat file contains parameters for configuring and running the backup.

#### Discussion Topics

> The following topics are described in this section:

- [<u>Snapshot Volume Definitions</u>](#snapshot-volume-definitions)
- [<u>Defining General Backup Behavior</u>](#defining-general-backup-behavior)
- [<u>Defining the Datasets for Backup and the Backup Location</u>](#defining-the-datasets-for-backup-and-the-backup-location)

#### Snapshot Volume Definitions

> Snapshot volume sizes are defined according to the size of the corresponding dat disk. As dat disks are increased, it may be necessary to increase the size of the snapshots. This section of the backup.dat file contains the snapshot volume definitions.

> <span id="_bookmark23" class="anchor"></span>Figure 9: Sample Snapshot Volume Definitions Report

#### Defining General Backup Behavior

> This section of the backup.dat file includes the parameters for the number of concurrent integrity jobs, the D2D target path, the number of days of journal files to keep, etc.

> <span id="_bookmark25" class="anchor"></span>Figure 10: Sample General Backup Behavior Report

> \# \# GENERAL BACKUP BEHAVIOR

> \#

> \# The following line provides custom settings for backup behavior:

> \# \<# concurrent INTEGRIT jobs\>,\<D2D target path\>,\<# days jrn files to keep\>,

> \# \<gzip flag\>,\<Tier1 backup days to retain\>,\<Tier3 backup days to retain\>

> \#

> \# NOTE: each field must be represented by commas even if blank, e.g.: \# ,/example/elp/d2d,,N,,

> \# NOTE: \# concurrent INTEGRIT jobs = 0-9. If 0, NO INTEGRITs WILL BE RUN

> \# The default value is to allow three concurrent INTEGRIT jobs \# NOTE: The default value for days of journal files to retain is 5

> \# NOTE: specify 'y' or 'Y' if backed up DAT files should be gzipped.

> Zipping

> \# the backup will roughly double backup time. The default behavior is

> \# no zipping of files

> \# NOTE: Tier1 backup days to retain specifies that disk backups older than N

> \# days will be deleted at the start of the backup IF the backup was \# successfully copied to tape or Tier3. The default is 2 days of backups to retain.

> \#

> \# example:

> \# 6,/example/elp/d2d,5,n,2 \#

> 6,/example/scd/d2d,5,n,2

#### Defining the Datasets for Backup and the Backup Location

> The last section of the backup.dat file includes the definitions for each dataset to be backed up and its corresponding snapshot directory.

> <span id="_bookmark27" class="anchor"></span>Figure 11: Sample Data to be Backed Up Report

> \# \# DATA TO BE BACKED UP

> \#

> \# Each subsequent line provides DAT file, jrn and miscellaneous directory to

> \# be backed up: \<backup set name\>,\<SNAPSHOT directory to back up\> \#

> \# NOTE: The backup set name is user specified and can be any value, however,

> \# 'jrn' is reserved for the journal file reference. Best practice is

> \# use the Cache' database or directory name as the backup set name. \# NOTE: If specified, INTEGRITs will be run on directories that contain a \# CACHE.DAT file. Best practice is to order the database list to

> \# alternate snapshot disks to reduce contention. Consider running \# INTEGRITs on the largest DAT files first and limit the number of

> \# concurrent INTEGRIT jobs to avoid simultaneous jobs running on the \# same disk at the same time.

> \# NOTE: user disk directories must be specified one line per directory and \# will not allow recursion since the user disk serves as the mount point

> \# for all other disks:

> \# user,/example/elp/path7/user/\<directory1\> \# user,/example/elp/path7/user/\<directory2\>

> \# NOTE: For local d2d backups any directory path may be specified for backup

> \# and need reside on a snapshot (e.g. /home). Network backups, however,

> \# may only use snapshot logical volumes. \#

> \# example:

> \# taa,/example/elp/path1/taa \# tff,/example/elp/path2/tff \# tbb,/example/elp/path3/tbb

> \# mgr,/example/elp/path5/elpr2tsvr/mgr \# jrn,/example/elp/path6/jrn/elpr2tsvr \# backup,/example/elp/path7/user/backup \# home,/home

> \#

> vbb,/example/scd/path2/vbb vhh,/example/scd/path1/vhh vdd,/example/scd/path3/vdd vff,/example/scd/path4/vff vee,/example/scd/path3/vee vgg,/example/scd/path2/vgg rou,/example/scd/path1/rou vcc,/example/scd/path4/vcc xshare,/example/scd/path1/xshare ztshare,/example/scd/path4/ztshare

#### Scheduling and Managing Backups

> Discussion Topics

> The following topics are described in this section:

- [<u>Schedule Backup Job Using crontab</u>](#schedule-backup-job-using-crontab)
- [<u>Running a Backup Job on Demand</u>](#running-a-backup-job-on-demand)
- [<u>View Running Backup Job</u>](#view-running-backup-job)
- [<u>Stop Running Backup Job</u>](#stop-running-backup-job)

#### Schedule Backup Job Using crontab

> The main backup control script is rdp_bkup_local. Schedule this script to run daily on the system. Scheduling the daily backup requires root level access in order to access the root user’s crontab.

> This function requires root level access - crontab

> To list the currently scheduled jobs in the root user’s crontab, do the following:

> <span id="_bookmark30" class="anchor"></span>Figure 12: Schedule Backup Job Using crontab (Sample Code)

> To add, modify, or remove the backup job, run the following command to open a vi editor for editing the crontab:

#### Running a Backup Job on Demand

> Running the backup job on demand can be accomplished by scheduling the backup script to run using the “at” scheduler.

#### View Running Backup Job

> To view a running backup job, do the following:

> <span id="_bookmark33" class="anchor"></span>Figure 13: View a Running Backup Job (Sample Code)

<table style="width:100%;">
<colgroup>
<col style="width: 1%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 45%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="10"><blockquote>
<p># <strong>ps aux | grep bkup</strong></p>
<p>USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td><blockquote>
<p>2967</p>
</blockquote></td>
<td><blockquote>
<p>0.0</p>
</blockquote></td>
<td>0.0</td>
<td>9324</td>
<td><blockquote>
<p>648 ?</p>
</blockquote></td>
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>07:54</p>
</blockquote></td>
<td><blockquote>
<p>0:00 /bin/bash /usr/local/sbin/rdp_bkup_integ</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>scd 154738</p>
</blockquote></td>
<td><blockquote>
<p>4225</p>
</blockquote></td>
<td><blockquote>
<p>0.0</p>
</blockquote></td>
<td>0.0</td>
<td>103240</td>
<td><blockquote>
<p>888 pts/1</p>
</blockquote></td>
<td><blockquote>
<p>S+</p>
</blockquote></td>
<td><blockquote>
<p>07:54</p>
</blockquote></td>
<td><blockquote>
<p>0:00 grep bkup</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td><blockquote>
<p>6643</p>
</blockquote></td>
<td><blockquote>
<p>0.0</p>
</blockquote></td>
<td>0.0</td>
<td>9328</td>
<td><blockquote>
<p>668 ?</p>
</blockquote></td>
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>06:48</p>
</blockquote></td>
<td><blockquote>
<p>0:00 /bin/bash /usr/local/sbin/rdp_bkup_integ</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>scd</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td><blockquote>
<p>10469</p>
</blockquote></td>
<td><blockquote>
<p>0.0</p>
</blockquote></td>
<td>0.0</td>
<td>9328</td>
<td><blockquote>
<p>1512 ?</p>
</blockquote></td>
<td><blockquote>
<p>Ss</p>
</blockquote></td>
<td><blockquote>
<p>01:00</p>
</blockquote></td>
<td><blockquote>
<p>0:00 /bin/bash /usr/local/sbin/rdp_bkup_local</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>scd CVB</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td><blockquote>
<p>14065</p>
</blockquote></td>
<td><blockquote>
<p>0.0</p>
</blockquote></td>
<td>0.0</td>
<td>9324</td>
<td><blockquote>
<p>1476 ?</p>
</blockquote></td>
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>01:00</p>
</blockquote></td>
<td><blockquote>
<p>0:00 /bin/bash /usr/local/sbin/rdp_bkup_integ</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>scd</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td><blockquote>
<p>18819</p>
</blockquote></td>
<td><blockquote>
<p>0.0</p>
</blockquote></td>
<td>0.0</td>
<td>9328</td>
<td><blockquote>
<p>676 ?</p>
</blockquote></td>
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>06:56</p>
</blockquote></td>
<td><blockquote>
<p>0:00 /bin/bash /usr/local/sbin/rdp_bkup_integ</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>scd</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Stop Running Backup Job

> To stop a running backup job, do the following:

1.  Get the Process Identifiers (PIDs) of all running backup jobs (bkup_local script, and any integs, d2d, etc.):

> <span id="_bookmark35" class="anchor"></span>Figure 14: Stop a Running Backup Job (Sample Code)

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>USER</p>
<p>COMMAND</p>
</blockquote></th>
<th>PID %CPU %MEM</th>
<th>VSZ</th>
<th colspan="2"><blockquote>
<p>RSS TTY</p>
</blockquote></th>
<th><blockquote>
<p>STAT</p>
</blockquote></th>
<th><blockquote>
<p>START</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TIME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>2967 0.0 0.0</td>
<td>9324</td>
<td colspan="2"><blockquote>
<p>648 ?</p>
</blockquote></td>
<td>S</td>
<td><blockquote>
<p>07:54</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0:00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>/bin/bash 154738</p>
<p>bkup root</p>
<p>/bin/bash</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>/usr/local/sbin/rdp_bkup_integ scd 4225 0.0 0.0 103240 888 pts/1</p>
<p>6643 0.0 0.0 9328 668 ?</p>
<p>/usr/local/sbin/rdp_bkup_integ scd</p>
</blockquote></td>
<td><blockquote>
<p>S+ S</p>
</blockquote></td>
<td><blockquote>
<p>07:54</p>
<p>06:48</p>
</blockquote></td>
<td><blockquote>
<p>0:00</p>
<p>0:00</p>
</blockquote></td>
<td><blockquote>
<p>grep</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>10469 0.0 0.0</td>
<td colspan="3"><blockquote>
<p>9328 1512 ?</p>
</blockquote></td>
<td><blockquote>
<p>Ss</p>
</blockquote></td>
<td><blockquote>
<p>01:00</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0:00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>/bin/bash /usr/local/sbin/rdp_bkup_local</p>
</blockquote></td>
<td><blockquote>
<p>scd</p>
</blockquote></td>
<td><blockquote>
<p>CVB</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>root 14065 0.0 0.0 9324 1476 ?</p>
<p>/bin/bash /usr/local/sbin/rdp_bkup_integ root 18819 0.0 0.0 9328 676 ?</p>
<p>/bin/bash /usr/local/sbin/rdp_bkup_integ</p>
</blockquote></td>
<td><blockquote>
<p>scd scd</p>
</blockquote></td>
<td><blockquote>
<p>S S</p>
</blockquote></td>
<td><blockquote>
<p>01:00</p>
<p>06:56</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0:00</p>
<p>0:00</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Kill the backup jobs using the PIDs:
3.  Stop the RESTORE instance if it is running:
4.  Check for the backup.active file, if it exists rename it to backup.error:
5.  Check if snapshot volumes are mounted:

> <span id="_bookmark36" class="anchor"></span>Figure 15: Check if Snapshot Volumes are Mounted (Sample Code)

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p># <strong>df –h</strong></p>
<p>Filesystem</p>
</blockquote></th>
<th>Size</th>
<th>Used</th>
<th>Avail</th>
<th>Use%</th>
<th><blockquote>
<p>Mounted on</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-root</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>12G</td>
<td>3.1G</td>
<td>7.9G</td>
<td>29%</td>
<td><blockquote>
<p>/</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>tmpfs</p>
</blockquote></td>
<td>24G</td>
<td>29M</td>
<td>24G</td>
<td>1%</td>
<td><blockquote>
<p>/dev/shm</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>/dev/sda1</p>
</blockquote></td>
<td>485M</td>
<td>91M</td>
<td>369M</td>
<td>20%</td>
<td><blockquote>
<p>/boot</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-home</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>2.0G</td>
<td>293M</td>
<td>1.6G</td>
<td>16%</td>
<td><blockquote>
<p>/home</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-opt</p>
</blockquote></td>
<td>3.9G</td>
<td>796M</td>
<td>2.9G</td>
<td>22%</td>
<td><blockquote>
<p>/opt</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>/dev/mapper/path3-srv</p>
</blockquote></td>
<td>12G</td>
<td>158M</td>
<td>11G</td>
<td>2%</td>
<td><blockquote>
<p>/srv</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-tmp</p>
</blockquote></td>
<td>3.9G</td>
<td>72M</td>
<td>3.6G</td>
<td>2%</td>
<td><blockquote>
<p>/tmp</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>/dev/mapper/path3-var</p>
</blockquote></td>
<td>4.0G</td>
<td>564M</td>
<td>3.2G</td>
<td>15%</td>
<td><blockquote>
<p>/var</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-log</p>
</blockquote></td>
<td>2.0G</td>
<td>284M</td>
<td>1.6G</td>
<td>15%</td>
<td><blockquote>
<p>/var/log</p>
</blockquote></td>
</tr>
</tbody>
</table>

/dev/mapper/path3-audit

> 1008M 60M 898M 7% /var/log/audit

/dev/mapper/vg_example-lv_scd_user

> 20G 5.9G 14G 31% /example/scd

/dev/mapper/vg_example-lv_scd_cache

> 30G 3.3G 26G 12% /example/scd/cache

/dev/mapper/vg_example-lv_scd_jrn

> 84G 50G 33G 61% /example/scd/jrn

/dev/mapper/vg_example-lv_scd_dat1

> 212G 175G 35G 84% /example/scd/dat1

/dev/mapper/vg_example-lv_scd_dat2

> 217G 182G 33G 85% /example/scd/dat2

/dev/mapper/vg_example-lv_scd_dat3

> 217G 181G 34G 85% /example/scd/dat3

/dev/mapper/vg_example-lv_scd_dat4

> 227G 181G 44G 81% /example/scd/dat4

/dev/mapper/vg_scd_d2d-lv_scd_d2d_a

> 1004G 971G 23G 98% /example/scd/d2d/a

/dev/mapper/vg_scd_d2d-lv_scd_d2d_b

> 1004G 756G 238G 77% /example/scd/d2d/b

/dev/mapper/vg_example-lv_scd_user--snap

20G 6.0G 14G 31%

/dev/mapper/vg_example-lv_scd_dat1--snap

212G 175G 35G 84%

/dev/mapper/vg_example-lv_scd_dat2--snap

217G 182G 33G 85%

/dev/mapper/vg_example-lv_scd_dat3--snap

217G 181G 34G 85%

/dev/mapper/vg_example-lv_scd_dat4--snap

227G 181G 44G 81%

/dev/mapper/vg_example-lv_scd_cache--snap

30G 3.3G 26G 12%

/dev/mapper/vg_example-lv_scd_jrn--snap

84G 49G 35G 59%

/example/scd/path6/jrn

6.  Remove the unmount and destroy the snapshots if they are mounted:

#### Monitoring Backup Process

> Discussion Topics

> The following topics are described in this section:

- [<u>Look for Running Backup Process</u>](#look-for-running-backup-process)
- [<u>Look for Mounted Backup Disks</u>](#look-for-mounted-backup-disks)

#### Look for Running Backup Process

> Use the ps aux command to search through running processes to find jobs related to the backup process.

#### Look for Mounted Backup Disks

> The df command reports the system's disk space usage. Use this command to determine whether the backup process still has the snapshot disks mounted (e.g., /example/scd/path\*).

> <span id="_bookmark40" class="anchor"></span>Figure 16: Look for Mounted Backup Disks (Sample Code)

<table style="width:100%;">
<colgroup>
<col style="width: 40%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p># <strong>df –h</strong></p>
<p>Filesystem</p>
</blockquote></th>
<th>Size</th>
<th>Used</th>
<th>Avail</th>
<th>Use%</th>
<th><blockquote>
<p>Mounted on</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-root</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>12G</td>
<td>3.1G</td>
<td>7.9G</td>
<td>29%</td>
<td><blockquote>
<p>/</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>tmpfs</p>
</blockquote></td>
<td>24G</td>
<td>29M</td>
<td>24G</td>
<td>1%</td>
<td><blockquote>
<p>/dev/shm</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>/dev/sda1</p>
</blockquote></td>
<td>485M</td>
<td>91M</td>
<td>369M</td>
<td>20%</td>
<td><blockquote>
<p>/boot</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-home</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>2.0G</td>
<td>293M</td>
<td>1.6G</td>
<td>16%</td>
<td><blockquote>
<p>/home</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-opt</p>
</blockquote></td>
<td>3.9G</td>
<td>796M</td>
<td>2.9G</td>
<td>22%</td>
<td><blockquote>
<p>/opt</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>/dev/mapper/path3-srv</p>
</blockquote></td>
<td>12G</td>
<td>158M</td>
<td>11G</td>
<td>2%</td>
<td><blockquote>
<p>/srv</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-tmp</p>
</blockquote></td>
<td>3.9G</td>
<td>72M</td>
<td>3.6G</td>
<td>2%</td>
<td><blockquote>
<p>/tmp</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>/dev/mapper/path3-var</p>
</blockquote></td>
<td>4.0G</td>
<td>564M</td>
<td>3.2G</td>
<td>15%</td>
<td><blockquote>
<p>/var</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>/dev/mapper/path3-log</p>
</blockquote></td>
<td>2.0G</td>
<td>284M</td>
<td>1.6G</td>
<td>15%</td>
<td><blockquote>
<p>/var/log</p>
</blockquote></td>
</tr>
</tbody>
</table>

/dev/mapper/path3-audit

1008M 60M 898M 7% /var/log/audit

/dev/mapper/vg_example-lv_scd_user

> 20G 5.9G 14G 31% /example/scd

/dev/mapper/vg_example-lv_scd_cache

> 30G 3.3G 26G 12% /example/scd/cache

/dev/mapper/vg_example-lv_scd_jrn

> 84G 50G 33G 61% /example/scd/jrn

/dev/mapper/vg_example-lv_scd_dat1

> 212G 175G 35G 84% /example/scd/dat1

/dev/mapper/vg_example-lv_scd_dat2

> 217G 182G 33G 85% /example/scd/dat2

/dev/mapper/vg_example-lv_scd_dat3

> 217G 181G 34G 85% /example/scd/dat3

/dev/mapper/vg_example-lv_scd_dat4

> 227G 181G 44G 81% /example/scd/dat4

/dev/mapper/vg_scd_d2d-lv_scd_d2d_a

> 1004G 971G 23G 98% /example/scd/d2d/a

/dev/mapper/vg_scd_d2d-lv_scd_d2d_b

> 1004G 756G 238G 77% /example/scd/d2d/b

/dev/mapper/vg_example-lv_scd_user--snap

20G 6.0G 14G 31%

/dev/mapper/vg_example-lv_scd_dat1--snap

212G 175G 35G 84%

/dev/mapper/vg_example-lv_scd_dat2--snap

217G 182G 33G 85%

/dev/mapper/vg_example-lv_scd_dat3--snap

217G 181G 34G 85%

/dev/mapper/vg_example-lv_scd_dat4--snap

227G 181G 44G 81%

/dev/mapper/vg_example-lv_scd_cache--snap

30G 3.3G 26G 12%

#### Monitoring Backup Log Files

> Discussion Topics

> The following topics are described in this section:

- [<u>/var/log/vista/\<instance\> File</u>](#2.3.3.1.5.1_/var/log/vista/<instance>_Fi)
- [<u>/var/log/messages File</u>](#varlogmessages-file)
  1.  <span id="2.3.3.1.5.1_/var/log/vista/<instance>_Fi" class="anchor"></span>/var/log/vista/*\<instance\>* File

Most of the backup log files can be found in the following directory:

/var/log/vista/*\<instance\>*

Some of the included log files are:

- Summary Backup Log file:

> *\<date\>*-*\<instance\>*-backup.log

- Summary Integrity Log file:

> *\<date\>*-*\<job\>*-integrits.log

- Individual Integrity Log file:

> *\<database\>*-*\<date\>*-*\<job\>*-integ.log

> Also, the backup.active file can be found in the following directory:

> /var/log/vista/*\<instance\>*

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/013.png) REF: For a list of VistA instances by region, see the HC_HL_App_Server_Standards_All_Regions_MASTER.xlsx Microsoft<sup>®</sup> Excel document located at: [<u>http://go.va.gov/sxcu</u>](http://go.va.gov/sxcu).

#### /var/log/messages File

> The /var/log/messages file can also be monitored for backup activity, including the mounting and unmounting of snapshots volumes.

#### Restore Procedures

> This section describes how to restore the system from a backup. The HL7 Health Connect restore procedures are TBD.

#### Back-Up Testing

> Periodic tests verify that backups are accurate and can be used to restore the system. This section describes the procedure to test each of the back-up types described in the back-up section. It describes the regular testing schedule. It also describes the basic operational tests to be performed as well as specific data quality tests.

> The VA and HL7 Health Connect will perform backup services and will also ensure those backups are tested to verify the backup was successfully completed.

> The HL7 Health Connect backup testing process is TBD.

#### Storage and Rotation

> This section describes how, when (schedule), and where HL7 Health Connect backup media is stored and transported to and from an off-site location. It includes names and contact information for all principals at the remote facility.

> The HL7 Health Connect storage and rotation process is TBD.

## Security / Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the security architecture of the system, including the authentication and authorization mechanisms.

> HL7 Health Connect uses Caché encryption at the database level.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/014.png) REF: For more information and to get an architectural overview (e.g., Datacenter regional diagram), see the *Regional HealthConnect Installation - All RDCs* document (i.e., Regional_HealthConnect_Installation_All_RDCs.docx) located at: [<u>http://go.va.gov/sxcu</u>](http://go.va.gov/sxcu)

### Identity Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section defines the procedures for adding new users, giving and modifying rights, and deactivating users. It includes the administrative process for granting access rights and any authorization levels, if more than one exists. Describe what level of administrator has the authority for user management:

- Authentication—Process of proving your identity (i.e., who are you?). Authentication can take many forms, such as user identification (ID) and password, token, digital certificate, and biometrics.
- Authorization—Takes the authenticated identity and verifies if you have the necessary privileges or assigned role to perform the action you are requesting on the resource you are seeking to act upon.

> This is perhaps the cornerstone of any security architecture, since security is largely focused on providing the proper level of access to resources.

> The HL7 Health Connect identity management process is TBD.

### Access Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the systems access control functionality. It includes security procedures and configurations *not* covered in the previous section. It includes any password aging and/or strictness controls, user/security group management, key management, and temporary rights.

> Safeguarding data and access to that data is an important function of the VA. An enterprise-wide security approach includes the interrelationships between security policy, process, and technology (and implications by their organizational analogs). VA security addresses the following services.

- Authentication
- Authorization
- Confidentiality
- Data Integrity

> The HL7 Health Connect access control process is TBD.

### Audit Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To access the HL7 Health Connect “Auditing” screen, do the following:

#### SMP  System Administration  Security  Auditing

<span id="_bookmark51" class="anchor"></span>Redacted Figure 17: Audit Control

## User Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section defines the process and procedures used to notify the user community of any scheduled or unscheduled changes in the system state. It includes planned outages, system upgrades, and any other maintenance work, plus any unexpected system outages.

> The HL7 Health Connect user notifications process is TBD.

### User Notification Points of Contact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section identifies the key individuals or organizations that *must* be informed of a system outage, system or software upgrades to include schedule or unscheduled maintenance, or system

> changes. The table lists the Name/Organization/Phone \#/E-Mail Address/Method of notification (phone or E-Mail)/Notification Priority/Time of Notification).

> The HL7 Health Connect user notification points of contact are TBD.

## System Monitoring, Reporting, & Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the high-level approach to monitoring the HL7 Health Connect system. It covers items needed to insure high availability. The HL7 Health Connect monitoring tools include:

- [<u>Ensemble System Monitor</u>](#ensemble-system-monitor)
- InterSystems Diagnostic Tools:
  - [<u>^Buttons</u>](#buttons)
  - [<u>^pButtons</u>](#pbuttons)
  - [<u>cstat</u>](#cstat)
  - ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/015.png)[<u>mgstat</u>](#mgstat)

> CAUTION: The InterSystems Diagnostic Tools should only be used with the recommendation and assistance of the [InterSystems Support](#intersystems-support) team.

### Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Tier 2

> Use the following Tier 2 email distribution group to add appropriate members/roles to be notified when needed:

#### OIT EPMO TRS EPS HSH HealthConnect Administration

> REDACTED

#### VA Enterprise Service Desk (ESD)

> For Information Technology (IT) support 24 hours a day, 365 days a year call the VA Enterprise Service Desk:

- Phone: REDACTED
- Information Technology Service Management (ITSM) Tool—ServiceNow site:

REDACTED

- Enter an Incident or Request ticket (YourIT) in ITSM ServiceNow system via the shortcut on your workstation.

#### InterSystems Support

> If you are unable to diagnose any of the HL7 Health Connect system issues, contact the InterSystems Support team at:

- Email: [<u>support@intersystems.com</u>](mailto:support@intersystems.com)
- Worldwide Response Center (WRC) Direct Phone: 617-621-0700.

### Monitor Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All of the commands in this section are run from the Linux prompt.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/016.png) REF: For information on Linux system monitoring, see the OIT Service Line documentation.

#### ps Command

> The ps ax command displays a list of current system processes, including processes owned by other users. To display the owner alongside each process, use the ps aux command. This list is a static list; in other words, it is a snapshot of what was running when you invoked the command. If you want a constantly updated list of running processes, use top as described in the “[<u>top</u>](#top-command) [<u>Command</u>](#top-command)” section.

> The ps output can be long. To prevent it from scrolling off the screen, you can pipe it through less:

> You can use the ps command in combination with the grep command to see if a process is running. For example, to determine if Emacs is running, use the following command:

#### top Command

> The top command displays currently running processes and important information about them, including their memory and CPU usage. The list is both real-time and interactive. An example of output from the top command is provided in [<u>Figure 18</u>](#_bookmark62):

> <span id="_bookmark62" class="anchor"></span>Figure 18: The top Command—Sample Output

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 2%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>si</p>
</blockquote></th>
<th colspan="12"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Mem:</p>
</blockquote></td>
<td>775024k</td>
<td colspan="2"><blockquote>
<p>total,</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>772028k used,</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>2996k free,</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>68468k buffers</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Swap:</p>
</blockquote></td>
<td>1048568k</td>
<td colspan="2"><blockquote>
<p>total,</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>176k used,</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>1048392k free,</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>441172k cached</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PID</td>
<td><blockquote>
<p>USER</p>
</blockquote></td>
<td>PR</td>
<td>NI</td>
<td>VIRT</td>
<td>RES</td>
<td>SHR</td>
<td>S</td>
<td>%CPU</td>
<td>%MEM</td>
<td colspan="2"><blockquote>
<p>TIME+</p>
</blockquote></td>
<td><blockquote>
<p>COMMAND</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4624</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>15</td>
<td>0</td>
<td>40192</td>
<td>18m</td>
<td>7228</td>
<td>S</td>
<td>28.4</td>
<td>2.4</td>
<td colspan="2"><blockquote>
<p>1:23.21</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4926</td>
<td><blockquote>
<p>mhideo</p>
</blockquote></td>
<td>15</td>
<td>0</td>
<td>55564</td>
<td>33m</td>
<td>9784</td>
<td>S</td>
<td>13.5</td>
<td>4.4</td>
<td colspan="2"><blockquote>
<p>0:25.96</p>
</blockquote></td>
<td><blockquote>
<p>gnome-</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="13"><blockquote>
<p>terminal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6475</td>
<td><blockquote>
<p>mhideo</p>
</blockquote></td>
<td>16</td>
<td>0</td>
<td>3612</td>
<td>968</td>
<td>760</td>
<td>R</td>
<td>0.7</td>
<td>0.1</td>
<td colspan="2"><blockquote>
<p>0:00.11</p>
</blockquote></td>
<td><blockquote>
<p>top</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4920</td>
<td><blockquote>
<p>mhideo</p>
</blockquote></td>
<td>15</td>
<td>0</td>
<td>20872</td>
<td>10m</td>
<td>7808</td>
<td>S</td>
<td>0.3</td>
<td>1.4</td>
<td colspan="2"><blockquote>
<p>0:01.61</p>
</blockquote></td>
<td><blockquote>
<p>wnck-applet</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>16</td>
<td>0</td>
<td>1732</td>
<td>548</td>
<td>472</td>
<td>S</td>
<td>0.0</td>
<td>0.1</td>
<td colspan="2"><blockquote>
<p>0:00.23</p>
</blockquote></td>
<td><blockquote>
<p>init</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>34</td>
<td>19</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>S</td>
<td>0.0</td>
<td>0.0</td>
<td colspan="2"><blockquote>
<p>0:00.00</p>
</blockquote></td>
<td><blockquote>
<p>ksoftirqd/0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>5</td>
<td>-10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>S</td>
<td>0.0</td>
<td>0.0</td>
<td colspan="2"><blockquote>
<p>0:00.03</p>
</blockquote></td>
<td><blockquote>
<p>events/0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>6</td>
<td>-10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>S</td>
<td>0.0</td>
<td>0.0</td>
<td colspan="2"><blockquote>
<p>0:00.02</p>
</blockquote></td>
<td><blockquote>
<p>khelper</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>5</td>
<td>-10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>S</td>
<td>0.0</td>
<td>0.0</td>
<td colspan="2"><blockquote>
<p>0:00.00</p>
</blockquote></td>
<td><blockquote>
<p>kacpid</p>
</blockquote></td>
</tr>
<tr class="even">
<td>29</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>5</td>
<td>-10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>S</td>
<td>0.0</td>
<td>0.0</td>
<td colspan="2"><blockquote>
<p>0:00.00</p>
</blockquote></td>
<td><blockquote>
<p>kblockd/0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>47</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>16</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>S</td>
<td>0.0</td>
<td>0.0</td>
<td colspan="2"><blockquote>
<p>0:01.74</p>
</blockquote></td>
<td><blockquote>
<p>pdflush</p>
</blockquote></td>
</tr>
<tr class="even">
<td>50</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>11</td>
<td>-10</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>S</td>
<td>0.0</td>
<td>0.0</td>
<td colspan="2"><blockquote>
<p>0:00.00</p>
</blockquote></td>
<td><blockquote>
<p>aio/0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>30</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>15</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>S</td>
<td>0.0</td>
<td>0.0</td>
<td colspan="2"><blockquote>
<p>0:00.05</p>
</blockquote></td>
<td><blockquote>
<p>khubd</p>
</blockquote></td>
</tr>
<tr class="even">
<td>49</td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td>16</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>S</td>
<td>0.0</td>
<td>0.0</td>
<td colspan="2"><blockquote>
<p>0:01.44</p>
</blockquote></td>
<td><blockquote>
<p>kswapd0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> To exit top, press the q key.

#### procinfo Command

> <span id="_bookmark64" class="anchor"></span>Figure 19: Sample System Data Output

> You can find out detailed information with -a flag:

> <span id="_bookmark65" class="anchor"></span>Figure 20: Sample System Data Output

> Linux 2.6.5-7.252-default (redacted) (gcc 3.3.3 ) \#1 2CPU \[redacted\]

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 21%" />
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Memory:</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>Total Used</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>Free Shared Buffers</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Mem:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>4125168 4112656</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>12512 0 276512</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Swap:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>4200688 32</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>4200656</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Bootup: 6641</p>
<p>user :</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Mon Apr 10 13:46:48 2006</p>
<p>0:59:24.49 2.2%</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Load average: 0.76 0.70 0.32 1/105</p>
<p>page in : 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>nice :</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0:11:08.41 0.4%</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>page out: 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>system:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0:06:51.10 0.2%</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>swap in : 0</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>idle :</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>18d 15:46:46.95 1020.6%</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>swap out: 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>uptime:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>9d 8:37:33.35</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>context : 84375734</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>irq 0:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0 0</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>irq 54: 396314 ioc0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>irq</p>
</blockquote></td>
<td><blockquote>
<p>28:</p>
</blockquote></td>
<td>1800</td>
<td><blockquote>
<p>cpe_poll</p>
</blockquote></td>
<td>irq 55:</td>
<td>30</td>
<td><blockquote>
<p>ioc1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>irq</p>
</blockquote></td>
<td><blockquote>
<p>29:</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>cmc_poll</p>
</blockquote></td>
<td>irq 56:</td>
<td>1842085</td>
<td><blockquote>
<p>eth1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>irq</p>
</blockquote></td>
<td><blockquote>
<p>31:</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>cmc_hndlr</p>
</blockquote></td>
<td>irq 57:</td>
<td>18</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>irq</p>
</blockquote></td>
<td><blockquote>
<p>48:</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>acpi</p>
</blockquote></td>
<td>irq232:</td>
<td>0</td>
<td><blockquote>
<p>mca_rdzv</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>irq</p>
</blockquote></td>
<td><blockquote>
<p>49:</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>ohci_hcd</p>
</blockquote></td>
<td>irq238:</td>
<td>0</td>
<td><blockquote>
<p>perfmon</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>irq</p>
</blockquote></td>
<td><blockquote>
<p>50:</p>
</blockquote></td>
<td>1892</td>
<td><blockquote>
<p>ohci_hcd</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>irq239:1656130975</p>
</blockquote></td>
<td><blockquote>
<p>timer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>irq</p>
</blockquote></td>
<td><blockquote>
<p>51:</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>ehci_hcd</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>irq240: 0</p>
</blockquote></td>
<td><blockquote>
<p>mca_wkup</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>irq</p>
</blockquote></td>
<td><blockquote>
<p>52:</p>
</blockquote></td>
<td>5939450</td>
<td><blockquote>
<p>ide0</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>irq254: 792697</p>
</blockquote></td>
<td><blockquote>
<p>IPI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>irq</p>
</blockquote></td>
<td><blockquote>
<p>53:</p>
</blockquote></td>
<td>404118</td>
<td><blockquote>
<p>eth0</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

> Kernel Command Line:

> BOOT_IMAGE=scsi0:\efi\SuSE\vmlinuz root=/dev/sda3 selinux=0 splash=silent elevator=cfq ro

> Modules:

> 147 snd_pcm_oss 240 \*snd_pcm 38 \*snd_page_alloc 74 \*snd_timer

> 57 \*snd_mixer_oss 149 \*snd 33 \*soundcore 44 thermal

> 48 \*processor 23 fan 28 button 78 usbserial

> 73 parport_pc 38 lp 104 \*parport 700 \*ipv6

> 113 hid 36 joydev 97 sg 98 st

<table style="width:100%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 5%" />
<col style="width: 18%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>51 sr_mod</p>
</blockquote></th>
<th>93</th>
<th><blockquote>
<p>ide_cd</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>90 *cdrom</p>
</blockquote></th>
<th colspan="2">84</th>
<th><blockquote>
<p>ehci_hcd</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63 ohci_hcd</p>
</blockquote></td>
<td>35</td>
<td><blockquote>
<p>evdev</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>244 tg3</p>
</blockquote></td>
<td colspan="2">63</td>
<td><blockquote>
<p>*af_packet</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>40 *binfmt_misc</p>
</blockquote></td>
<td>246</td>
<td><blockquote>
<p>*usbcore</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>122 e100</p>
</blockquote></td>
<td colspan="2">32</td>
<td><blockquote>
<p>*subfs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>19 *nls_utf8</p>
</blockquote></td>
<td>24</td>
<td><blockquote>
<p>*nls_cp437</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>139 dm_mod</p>
</blockquote></td>
<td colspan="2">266</td>
<td><blockquote>
<p>*ext3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>165 *jbd</p>
<p>*scsi_transport</p>
<p>29 *mptspi</p>
<p>237 *scsi_mod</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>30 mptsas</p>
<p>98 *mptscsih</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>30 mptfc 29</p>
<p>131 *mptbase 52 *sd_mod</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Character Devices:</p>
<p>1 mem</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>misc</td>
<td colspan="3"><blockquote>
<p>Block Devices:</p>
<p>1 ramdisk</p>
</blockquote></td>
<td><blockquote>
<p>71</p>
</blockquote></td>
<td>sd</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2 pty</p>
</blockquote></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>input</td>
<td>3</td>
<td><blockquote>
<p>ide0</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>128</p>
</blockquote></td>
<td>sd</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 ttyp</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>sound</td>
<td>7</td>
<td><blockquote>
<p>loop</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>129</p>
</blockquote></td>
<td><blockquote>
<p>sd</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4 /dev/vc/0</p>
</blockquote></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
<td>sg</td>
<td>8</td>
<td><blockquote>
<p>sd</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>130</p>
</blockquote></td>
<td>sd</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4 tty</p>
</blockquote></td>
<td><blockquote>
<p>29</p>
</blockquote></td>
<td>fb</td>
<td>9</td>
<td><blockquote>
<p>md</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>131</p>
</blockquote></td>
<td>sd</td>
</tr>
<tr class="even">
<td><blockquote>
<p>4 ttyS</p>
</blockquote></td>
<td>116</td>
<td>alsa</td>
<td>11</td>
<td><blockquote>
<p>sr</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>132</p>
</blockquote></td>
<td>sd</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5 /dev/tty</p>
</blockquote></td>
<td>128</td>
<td>ptm</td>
<td>65</td>
<td><blockquote>
<p>sd</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>133</p>
</blockquote></td>
<td>sd</td>
</tr>
<tr class="even">
<td><blockquote>
<p>5 /dev/console</p>
</blockquote></td>
<td>136</td>
<td>pts</td>
<td>66</td>
<td><blockquote>
<p>sd</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>134</p>
</blockquote></td>
<td>sd</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 26%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><ol start="5" type="1">
<li><p>/dev/ptmx</p></li>
<li><p>lp</p></li>
</ol>
<blockquote>
<p>mapper</p>
</blockquote></th>
<th><blockquote>
<p>180 usb</p>
<p>188 ttyUSB</p>
</blockquote></th>
<th><ol start="67" type="1">
<li><p>sd</p></li>
<li><p>sd</p></li>
</ol></th>
<th><blockquote>
<p>135 sd</p>
<p>253 device-</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>7 vcs</p>
</blockquote></td>
<td><blockquote>
<p>254 snsc</p>
</blockquote></td>
<td><blockquote>
<p>69 sd</p>
</blockquote></td>
<td><blockquote>
<p>254 mdp</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9 st</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>70 sd</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>File Systems:</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ext3</p>
</blockquote></td>
<td><blockquote>
<p>[sysfs]</p>
</blockquote></td>
<td><blockquote>
<p>[rootfs]</p>
</blockquote></td>
<td><blockquote>
<p>[bdev]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[proc]</p>
</blockquote></td>
<td><blockquote>
<p>[cpuset]</p>
</blockquote></td>
<td><blockquote>
<p>[sockfs]</p>
</blockquote></td>
<td><blockquote>
<p>[pfmfs]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[futexfs]</p>
</blockquote></td>
<td><blockquote>
<p>[tmpfs]</p>
</blockquote></td>
<td><blockquote>
<p>[pipefs]</p>
</blockquote></td>
<td>[eventpollfs]</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[devpts]</p>
</blockquote></td>
<td><blockquote>
<p>ext2</p>
</blockquote></td>
<td><blockquote>
<p>[ramfs]</p>
</blockquote></td>
<td><blockquote>
<p>[hugetlbfs]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>minix</p>
</blockquote></td>
<td><blockquote>
<p>msdos</p>
</blockquote></td>
<td><blockquote>
<p>vfat</p>
</blockquote></td>
<td><blockquote>
<p>iso9660</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[nfs]</p>
</blockquote></td>
<td><blockquote>
<p>[nfs4]</p>
</blockquote></td>
<td><blockquote>
<p>[mqueue]</p>
</blockquote></td>
<td><blockquote>
<p>[rpc_pipefs]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[subfs]</p>
</blockquote></td>
<td><blockquote>
<p>[usbfs]</p>
</blockquote></td>
<td><blockquote>
<p>[usbdevfs]</p>
</blockquote></td>
<td>[binfmt_misc]</td>
</tr>
</tbody>
</table>

### Other Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- -f—Run procinfo continuously full-screen (update status on screen, the default is 5

> seconds, use -n SEC to setup pause).

- -Ffile—Redirect output to file (usually a tty). For example:

#### procinfo -biDn1 -F/dev/tty5

- Pstree—Process monitoring can also be achieved using the pstree command. It displays a snapshot of running process. It always uses a tree-like display like ps f:
  - By default, it shows only the name of each command.
  - Specify a pid as an argument to show a specific process and its descendants.
  - Specify a user name as an argument to show process trees owned by that user.
- Pstree options:
  - -a—Display commands’ arguments.
  - -c—Do *not* compact identical subtrees.
  - -G—Attempt to use terminal-specific line-drawing characters.
  - -hHighlight—Ancestors of the current process.
  - -n—Sort processes numerically by pid, rather than alphabetically by name.
  - <span id="2.6.4_Dataflow_Diagram" class="anchor"></span>-p—Include pids in the output.

### Dataflow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For a Dataflow diagram, see the InterSystems Health Connect documentation.

### Availability Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the procedure to determine the overall operational state and the state of the individual components for the HL7 Health Connect system.

> The following Caché command from a Linux prompt displays the currently installed instances on the server. It also indicates the current status and state of the installed instances:

> \$ ccontrol list

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/017.png)REF: For more information on the ccontrol command, see [<u>Step 1</u>](#_bookmark7) in Section [<u>2.3.1</u>,](#system-start-up) “[<u>System Start-Up</u>](#system-start-up).”

### High Availability Mirror Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Mirror monitoring is a system in which there are backup systems containing all tracked databases. This tracked database is used for failover situations in case the primary system fails.

> One situation that allows for a failover is disaster recovery in which the failover node takes over when the primary system is down; this occurs with no downtime.

#### Logical Diagrams

> [<u>Figure 21</u>](#_bookmark71) illustrates the HealthShare Enterprise (HSE) Health Connect (HC) deployment with Enterprise Caché Protocol (ECP) connectivity to production VistA instances.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/018.png)<span id="_bookmark71" class="anchor"></span>Figure 21: Logical Diagrams—HSE Health Connect with ECP to VistA

> [<u>Figure 22</u>](#_bookmark72) illustrates the Health Level Seven (HL7) Health Connect deployment for VistA Interface Engine (VIE) replacement for HL7 message traffic.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/019.png)<span id="_bookmark72" class="anchor"></span>Figure 22: Logical Diagrams—HL7 Health Connect

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/020.png) REF: For more information on the system architecture, see the *Systems Architecture and Build Summary: HealthShare Health Connects-(HSE & HL7)* document (i.e., System- Build-HealthConnect.rtf document; written by: Thomas H Sasse, ISC M.B. and Travis Hilton, Architect.

#### Accessing Mirror Monitor

> To access the Mirror Monitor, do the following:

1.  From the InterSystems’ System Management Portal (SMP) “Home” page, enter<span id="_bookmark74" class="anchor"></span> “MIRROR MONITOR” in the Search box. The search result is displayed in [<u>Figure 23</u>](#_bookmark74):

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/021.png)Figure 23: SMP Home Page “Mirror Monitor” Search Results

2.  From the search results displayed ([<u>Figure 23</u>](#_bookmark74)), select the “Mirror Monitor” link to go to<span id="_bookmark75" class="anchor"></span> the “Mirror Monitor” page, as shown in [<u>Figure 24</u>](#_bookmark75):

> Redacted Figure 24: SMP Mirror Monitor Page

#### Mirror Monitor Status Codes

> [<u>Table 1</u>](#_bookmark77) lists the possible Mirror Monitor status codes.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/022.png) NOTE: Some of these status codes (e.g., [Stopped](#_bookmark82), [Crashed](#_bookmark83), [Error,](#_bookmark84) or [Down](#_bookmark85)) may need your intervention in consultation with [<u>InterSystems support</u>](#intersystems-support):

> <span id="_bookmark77" class="anchor"></span>Table 1: Mirror Monitor Status Codes

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Status</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Not Initialized</strong></p>
</blockquote></td>
<td><blockquote>
<p>This instance is <em>not</em> yet initialized, or <em>not</em> a member of the specified mirror.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><span id="_bookmark78" class="anchor"></span><strong>Primary</strong></p>
</blockquote></td>
<td><blockquote>
<p>This instance is the primary mirror member. Like the classmethod</p>
<p><a href="http://docs.intersystems.com/latest/csp/docbook/%25CSP.Documatic.cls?PAGE=CLASS&amp;LIBRARY=%25sys&amp;CLASSNAME=%25SYSTEM.Mirror&amp;IsPrimary"><strong>IsPrimary</strong></a> this indicates that the node is active as the <strong>Primary</strong>.</p>
<p><strong>$LG(status,2)</strong> contains “<strong>Trouble</strong>” when the <strong>Primary</strong> is in <strong>trouble</strong> state.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><span id="_bookmark79" class="anchor"></span><strong>Backup</strong></p>
</blockquote></td>
<td><blockquote>
<p>This instance is connected to the <a href="#_bookmark78"><strong>Primary</strong></a> as a backup member.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><span id="_bookmark80" class="anchor"></span><strong>Connected</strong></p>
</blockquote></td>
<td><blockquote>
<p>This instance is an <strong>async</strong> member currently connected to the mirror.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>m/n Connected</strong></p>
</blockquote></td>
<td><blockquote>
<p>Returned for <strong>async</strong> members, which connect to more than one mirror when the <strong>MirrorName</strong> argument is omitted:</p>
</blockquote>
<ul>
<li><p><em><strong>&lt;m&gt;</strong></em> is the number of mirrors to which instance is currently connected.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Status</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><ul>
<li><blockquote>
<p><em><strong>&lt;n&gt;</strong></em> is the number of mirrors tom which the instance is configured to connect.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Transition</strong></p>
</blockquote></td>
<td><blockquote>
<p>In a transitional state that will soon change when initialization or another operation completes. This status prompts processes querying a member's status to query again shortly. Failover members remain in this state while retrieving and applying journals when no other failover member is <a href="#_bookmark78"><strong>Primary</strong></a>. This is an indication that it may become <strong><a href="#_bookmark78">Primary</a></strong> upon finishing, so a caller that is waiting for this member to become <a href="#_bookmark78"><strong>Primary</strong></a> may wish to continue waiting; if there is another failover member that is <a href="#_bookmark78"><strong>Primary</strong>,</a> the state will be <a href="#_bookmark81"><strong>Synchronizing</strong></a> instead.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><span id="_bookmark81" class="anchor"></span><strong>Synchronizing</strong></p>
</blockquote></td>
<td><blockquote>
<p>Starting up or reconnecting after being <a href="#_bookmark82"><strong>Stopped</strong></a> or <strong>disconnected</strong>, retrieving and applying journal files in order to synchronize the database and journal state before becoming <a href="#_bookmark79"><strong>Backup</strong></a> or <a href="#_bookmark80"><strong>Connected</strong></a>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Waiting</strong></p>
</blockquote></td>
<td><blockquote>
<p>For a failover member this means the member is unable to become the <a href="#_bookmark78"><strong>Primary</strong></a> or <a href="#_bookmark79"><strong>Backup</strong></a> for some reason. For an <strong>async</strong> member this has similar meaning, either there is some trouble preparing to contact the mirror or it failed to establish a connection to the mirror. In all cases, there should be a note in the console log as to the problem and the member should be retrying to detect when the trouble condition is resolved.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><span id="_bookmark82" class="anchor"></span><strong>Stopped</strong></p>
</blockquote></td>
<td><blockquote>
<p>Mirroring is configured but <em>not</em> running and will <em>not</em> start automatically. Either the mirror management interface has been used to stop mirroring or the current state of the system has prevented mirroring from starting, which includes:</p>
</blockquote>
<ul>
<li><p>Emergency startup mode</p></li>
<li><p>Insufficient license</p></li>
<li><p>Mirror service disabled</p></li>
<li><p>Certain errors during mirroring initialization</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p><span id="_bookmark83" class="anchor"></span><strong>Crashed</strong></p>
</blockquote></td>
<td><blockquote>
<p>The mirror master job for this mirror is no longer running. Restarting Caché is required for mirroring to work again.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><span id="_bookmark84" class="anchor"></span><strong>Error</strong></p>
</blockquote></td>
<td><blockquote>
<p>An unexpected error occurred. Either a Caché error was caught or the system is in some unexpected state. <strong>$LG(status,2)</strong> contains the value of the <strong>$ZERROR</strong> variable.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><span id="_bookmark85" class="anchor"></span><strong>Down</strong></p>
</blockquote></td>
<td><blockquote>
<p>This member is down. This is displayed by other members when this member is down.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Monitoring System Alerts

> This section describes the possible console log and email alerts indicating system trouble at

> Level 2 or higher. The three severity levels of console log entries generating notifications are:

- 1—Warning, Severe, and Fatal
- 2—Severe and Fatal
- 3—Fatal only

> Anyone belonging to the [<u>Tier 2</u>](#tier-2) email group may receive email notifications. [<u>Figure 25</u>](#_bookmark87) is a sample email message indicating system alerts:

> <span id="_bookmark87" class="anchor"></span>Redacted Figure 25: Sample Production Message

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/023.png) NOTE: For email notification setup and configuration, see “[<u>Appendix B—Configuring</u>](#7_Appendix_B—Configuring_Alert_Email_Not) [<u>Alert Email Notification</u>](#7_Appendix_B—Configuring_Alert_Email_Not).”

> In addition to email notifications, these errors are reported to the cconsole.log. The cconsole.log

> file location is:

> *\<instance path\>*/mgr/cconsole.log

> To find this log file, enter the following command at a Linux prompt:

#### control list

> When this log reaches capacity (currently set at 5 megabytes), it appends a date and time to the file name and then starts a new cconsole.log file:

> *\<instance path\>*/mgr/cconsole.log*.\<date/Time\>*

> In some cases, you may need to review several log files over a period of time to get a complete picture of any recent occurrences.

#### Console Log Page

> To access the SMP “Console Log” page, do the following:

#### SMP System Operation  System Logs  Console Log

> <span id="_bookmark89" class="anchor"></span>Redacted Figure 26: Sample SMP Console Log Page with Alerts (1 of 2)

> <span id="_bookmark90" class="anchor"></span>Redacted Figure 27: Sample SMP Console Log Page with Alerts (2 of 2)

> System issues are displayed in a list from oldest at the top to most recent occurrence at the bottom.

> The second column (see green boxes in [<u>Figure 26</u>](#_bookmark89) and [<u>Figure 27</u>](#_bookmark90)) indicates the alert level number (e.g., 0 or 2). Level 2 alerts need to be reviewed and possible action required.

#### Level 2 Use Case Scenarios 2.6.6.4.2.1 Use Case 1

> Issue: Lost Communication with Arbiter

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/024.png) NOTE: The Arbiter \[ISCagent\] determines the Failover system. For example, you receive the following system messages:

> <span id="_bookmark92" class="anchor"></span>Figure 28: Sample Alert Messages Related to Arbiter Communications

#### Resolution:

> After timeout period expires (e.g., 60 seconds), the system automatically fails over to the backup (Failover) system; see [<u>Use Case 3</u>.](#use-case-3)

#### Use Case 2

> Issue: Primary Mirror is Down Resolution:

> Troubleshoot by looking at Mirror Monitor ([<u>Figure 24</u>](#_bookmark75)). Make sure the Primary Mirror is running successfully on one node.

#### Use Case 3

> Issue: Failover Mirror is Down Resolution:

> System automatically fails over to the backup Failover Mirror. The system administrator should do the following:

1.  Start up the original Primary system. Enter the following command:

> ccontrol start *\<instancename\>*

2.  Stop the current Primary (Failover) system. Enter the following command:

> ccontrol stop *\<instancename\>*

3.  Start a new Failover system. Enter the following command:

> ccontrol start *\<instancename\>*

#### Use Case 4

> Issue: ISCagent is Down Resolution:

> Call [<u>InterSystems support</u>](#intersystems-support).

### System/Performance/Capacity Monitoring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section details the following InterSystems monitoring and diagnostic tools available in HL7 Health Connect:

- [<u>Ensemble System Monitor</u>](#ensemble-system-monitor)
- InterSystems Diagnostic Tools:
  - [<u>^Buttons</u>](#buttons)
  - [<u>^pButtons</u>](#pbuttons)
  - [<u>cstat</u>](#cstat)
  - ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/025.png)[<u>mgstat</u>](#mgstat)

> CAUTION: The InterSystems Diagnostic Tools should only be used with the recommendation and assistance of the [InterSystems Support](#intersystems-support) team.

#### Ensemble System Monitor

> The HL7 Health Connect “Ensemble System Monitor” page ([<u>Figure 29</u>,](#_bookmark96) [<u>Figure 30</u>,](#_bookmark97) and [<u>Figure</u>](#_bookmark98) [<u>31</u>](#_bookmark98)) provides a high-level view of the state of the system, across all namespaces. It displays Ensemble information combined with a subset of the information shown on the “System Dashboard” page ([<u>Figure 32</u>](#_bookmark99)), which is provided for the users of HL7 Health Connect.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/026.png) REF: For more information on the Ensemble System Monitor, see InterSystems’ documentation at: [<u>http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=EMONITO</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=EMONITOR_all) [<u>R_all</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=EMONITOR_all)

> To access the HL7 Health Connect Ensemble System Monitor, do the following:

#### System Management Portal (SMP)  Ensemble  Monitor  System Monitor

> <span id="_bookmark96" class="anchor"></span>Redacted Figure 29: Accessing the Ensemble System Monitor from SMP

> <span id="_bookmark97" class="anchor"></span>Redacted Figure 30: Ensemble Production Monitor (1 of 2)

> <span id="_bookmark98" class="anchor"></span>Redacted Figure 31: Ensemble Production Monitor (2 of 2)

> <span id="_bookmark99" class="anchor"></span>Redacted Figure 32: System Dashboard

#### ^Buttons

> ^Buttons is an InterSystems diagnostic tool.

1.  <span id="_bookmark101" class="anchor"></span>To run the ^Buttons utility, go to %SYS namespace, and do the following:

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/027.png)Figure 33: Running the ^Buttons Utility (Microsoft Windows Example)

#### ^pButtons

> ^pButtons is an InterSystems diagnostic tool. The ^pButtons utility, a tool for collecting detailed performance data about a Caché instance and the platform on which it is running.

2.  <span id="_bookmark103" class="anchor"></span>To run the ^pButtons utility, go to %SYS namespace, and do the following:

![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/028.png)Figure 34: ^pButtons—Running Utility (Microsoft Windows Example)

> For example: At the “select profile number to run:” prompt, enter 3 to run the 30mins profile. If you expect the query will take longer than 30 minutes, you can use a 4 hours report. You can just terminate the ^pButtons process later when the MDX report is ready. For example:

- Collection of this sample data will be available in 1920 seconds.
- The runid for this data is 20111007_1041_30mins.
- <span id="_bookmark105" class="anchor"></span>Please make a note of the log directory and the runid.
3.  After the runid is available for your reference, go to the "analytics" namespace, copy the

> MDX query from the DeepSee Analyzer, in terminal run the following:

<span id="_bookmark106" class="anchor"></span>Figure 35: ^pButtons—Copying MDX query from the DeepSee Analyzer

> The query is called and the related stats are logged in the MDXUtils report. After the files are created, go to the output folder path, and find the folder there.

4.  <span id="_bookmark107" class="anchor"></span>When you have finished running the queries, use the runid you got from [<u>Step 1</u>,](#_bookmark103) in terminal type, do the following:

> <span id="_bookmark108" class="anchor"></span>Figure 36: ^pButtons—Stop and Collect Procedures

> Wait 1 to 2 minutes, and then go to the log directory (see [<u>Step 1</u>](#_bookmark103)) and find the log/html

> file.

5.  <span id="_bookmark109" class="anchor"></span>Zip the report folders you got from both [<u>Step 2</u>](#_bookmark105) and [<u>3</u>](#_bookmark107); name it as “query \#”, and send it to [<u>InterSystems Support</u>.](#intersystems-support) Please make sure the two reports for one single query to be in one folder.
6.  Repeat [<u>Step 1</u>](#_bookmark103) through [<u>Step 4</u>](#_bookmark109) for the next query.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/029.png) REF: For more information on ^pButtons, see the InterSystems documentation at: [<u>http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_pbut</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_pbuttons) [<u>tons</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_pbuttons)

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/030.png)<span id="_bookmark110" class="anchor"></span>Figure 37: ^pButtons—Sample User Interface

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/031.png)<span id="_bookmark111" class="anchor"></span>Figure 38: ^pButtons—Task Scheduler Wizard

#### cstat

> cstat is an InterSystems diagnostic tool for system level problems, including:

- Caché hangs
- Network problems
- Performance issues

> When run, cstat attaches to the shared memory segment allocated by Caché at start time, and displays InterSystems’ internal structures and tables in a readable format. The shared memory segment contains:

- Global buffers
- Lock table
- Journal buffers
- A wide variety of other memory structures that need to be accessible to all Caché processes.

> Processes also maintain their own process private memory for their own variables and stack information. The basic display-only options of cstat are fast and *non*-invasive to Caché.

> In the event of a system problem, the cstat report is often the most important tool that InterSystems uses to determine the cause of the problem. Use the following guidelines to ensure that the cstat report contains all of the necessary information.

> Run cstat at the time of the event. From the Caché installation directory, the command would be as follows:

#### bash-3.00\$ ./bin/cstat -smgr

> Or:

> bash-3.00\$ ccontrol stat *Cache_Instance_Name*

> Where *Cache_Instance_Name* is the name of the Caché instance on which you are running

#### cstat.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/032.png)NOTE: The command sample above runs the basic default output of cstat.

> If the system gets hung, verify the following steps:

1.  Verify the user has admin rights.
2.  Locate the CacheHung script. This script is an operating system (OS) tool used to collect data on the system when a Caché instance is hung. This script is located in the following directory:

> *\<instance-install-dir\>*/bin

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/033.png) REF: For a list of VistA instances by region, see the HC_HL_App_Server_Standards_All_Regions_MASTER.xlsx Microsoft<sup>®</sup> Excel document located at: [<u>http://go.va.gov/sxcu</u>.](http://go.va.gov/sxcu)

3.  Execute the following command:

> cstat -e2 -f-1 -m-1 -n3 -j5 -g1 -L1 -u-1 -v1 -p-1 -c-1 -q1 -w2 -E-1 -N65535

4.  Check for cstat output files (.txt files). CacheHung generates cstat output files that are often very large, in which case they are saved to separate .txt files. Remember to check for these files when collecting the output.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/034.png) REF: For more information on cstat, see InterSystems’ Monitoring Caché Using the cstat Utility (DocBook): [<u>http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_cstat</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_cstat)

#### mgstat

> mgstat is an InterSystems diagnostic tool.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/035.png) REF: For more information on mgstat, see InterSystems’ documentation at: [<u>http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_mgst</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_mgstat) [<u>at</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_mgstat)

### Critical Metrics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides details about the exact metrics that are critical to validating the normal operation of the HL7 Health Connect system. It includes any indirect metrics that indicate a problem in the HL7 Health Connect system and related systems as well as the upstream and downstream indications of application issues. The frequency for metrics is determined by the Service Level Agreement (SLA) or the receiving organization’s standard operating procedures.

#### Ensemble System Monitor

> To access the HL7 Health Connect Ensemble System Monitor, do the following:

#### System Management Portal (SMP)  Ensemble  Monitor  System Monitor

> The Ensemble System Monitor provides the following four critical metrics:

- Ensemble Throughput ([<u>Table 2</u>](#_bookmark116))
- System Time ([<u>Table 3</u>](#_bookmark117))
- Errors and Alerts ([<u>Table 4</u>](#_bookmark118))
- <span id="_bookmark116" class="anchor"></span>Task Manager ([<u>Table 5</u>](#_bookmark119))

> Table 2: Ensemble Throughput Critical Metrics

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Critical Metrics</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Normal Value*</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Productions Running</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Production Suspended or Troubled</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Normal Value\*—If any *non*-normal value appears, contact the <u>VA Enterprise Service Desk</u> [<u>(ESD) Tier 1 Support</u>](#tier-2) team.

> <span id="_bookmark117" class="anchor"></span>Table 3: System Time Critical Metrics

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Critical Metrics</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Normal Value*</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Last Backup</p>
</blockquote></td>
<td><blockquote>
<p>Daily</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Database Space</p>
</blockquote></td>
<td><blockquote>
<p>Normal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Database Journal</p>
</blockquote></td>
<td><blockquote>
<p>Normal</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Journal Space</p>
</blockquote></td>
<td><blockquote>
<p>Normal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Lock Table</p>
</blockquote></td>
<td><blockquote>
<p>Normal</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Write Daemon</p>
</blockquote></td>
<td><blockquote>
<p>Normal</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Normal Value\*—If any *non*-normal value appears, contact the <u>VA Enterprise Service Desk</u> [<u>(ESD) Tier 1 Support</u>](#tier-2) team.

> <span id="_bookmark118" class="anchor"></span>Table 4: Errors and Alerts Critical Metrics

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Critical Metrics</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Normal Value*</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Serious System Alerts</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Ensemble Alerts</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Ensemble Errors</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Normal Value\*—If any *non*-normal value appears, contact the <u>VA Enterprise Service Desk</u> [<u>(ESD) Tier 1 Support</u>](#tier-2) team.

<span id="_bookmark119" class="anchor"></span>Table 5: Task Manager Critical Metrics

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Critical Metrics</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Normal Value*</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Any task</p>
</blockquote></td>
<td><blockquote>
<p>Not Errored State</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Normal Value\*—If any *non*-normal value appears, contact the <u>VA Enterprise Service Desk</u> [<u>(ESD) Tier 1 Support</u>](#tier-2) team.

<span id="_bookmark120" class="anchor"></span>Redacted Figure 39: Ensemble System Monitor Dashboard Displaying Critical Metrics

#### Ensemble Production Monitor

> To access the HL7 Health Connect Ensemble “Production Monitor” screen, do the following:

#### System Management Portal (SMP)  Ensemble  Monitor  System Monitor

> The Ensemble Production Monitor displays the current state of the production system:

- Healthy—Green
- Suspend—Yellow
- Not Connected—Purple
- Error—Red

> If any of the sections are *not* Green, contact the <u>VA Enterprise Service Desk (ESD) Tier 1</u> [<u>Support</u>](#tier-2) team.

> <span id="_bookmark122" class="anchor"></span>Redacted Figure 40: Ensemble Production Monitor—Displaying Critical Metrics

#### Normal Daily Task Management

> To access the HL7 Health Connect “Task Schedule” screen, do the following:

#### SMP  System Operation  Task Manager  Task Schedule

> Normal Task Management Processing will have a "Last Finished" date and time. If there is none or if the “Suspended” column is filled in, then contact the <u>VA Enterprise Service Desk (ESD)</u> [<u>Tier 1 Support</u>](#tier-2) team.

> <span id="_bookmark124" class="anchor"></span>Redacted Figure 41: Normal Daily Task Management Critical Metrics

#### System Console Log

> To access the HL7 Health Connect “View Console Log” screen, do the following:

#### SMP  System Logs  Console Log

> The Console Log should be reviewed for abnormal or crashed situations. For example:

> <span id="_bookmark126" class="anchor"></span>Redacted Figure 42: System Console Log Critical Metrics—Sample Alerts

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/036.png) REF: For more information on the Console Log, see the “[<u>Monitoring System Alerts</u>](#monitoring-system-alerts)” and “[<u>Console Log Page</u>](#console-log-page)” sections.

#### Application Error Logs

To access the HL7 Health Connect “Application Error Logs” screen, do the following:

#### SMP  System Operation  System Logs  Application Error Logs

For any application, all application errors are logged in the Application Error Log.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/037.png) REF: For sample screen images and more information on the Application Error Logs, see the “[Application Error Logs](#application-error-logs-1)” section.

## Routine Updates, Extracts, and Purges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section defines the procedures for typical maintenance activities of the HL7 Health Connect system, such as updates, on-request or periodic data extracts, database reorganizations, purges of data, and triggering events.

### Purge Management Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Ensemble Message Purging

> Ensemble Message Purging is an automatic system setup step, and if necessary, the message purging can be done manually by following the subsequent steps:

#### SMP  Ensemble  Manage  Purge Management Data

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/038.png)<span id="_bookmark131" class="anchor"></span>Figure 43: Manually Purge Management Data

#### Purge Journal Files

> The /Journal file system can begin to fill up rapidly with cache journal files for any number of reasons. When this occurs, it is often desirable to purge unneeded journal files in advance of having the /Journal file system fill up and switch to the /AltJournal file system.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/039.png) NOTE: Purging journal files is *not* required for transaction rollbacks or crash recovery. To purge Journal files, do any of the following procedures:

#### Procedure: Manually, from cache terminal, do the following:

1.  Run zn "%SYS".

#### do PURGE^JOURNAL.

2.  Select Option 1 - Purge any journal.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/040.png) NOTE: This is *not* required for transaction rollback or crash recovery.

3.  When returned to the “Option?” prompt simply press Enter to exit.

#### Halt.

- Procedure: Create an on demand task:
1.  In the System Management Portal (SMP) navigate to the following:

#### System  Operation  Task Manager  New Task

2.  For each label in the Task Scheduler Wizard enter the content described below:
    - Task Name: Purge Journal On Demand
    - Description: Purge Journal On Demand
    - Namespace to run task in: %SYS
    - Task Type: RunLegacyTask
    - ExecuteCode: do \##class(%SYS.Journal.File).PurgeAll()
    - Task priority: Priority Normal
    - Run task as this user: *\<chose system user\>* (e.g., ensusr or healthshare).
    - Open output file when task is running: No
    - Output file: *\<leave blank\>*
    - Suspend task on error: No
    - Reschedule task after system restart: No
    - Send completion email notification to: *\<leave blank\>*
    - Send email error notification to: *\<choose distribution list\>* (e.g., <ApplicationsIntegrationTeam@seattlechildrens.org> or hieteam@seattlechildrens.org)
    - Click Next at the bottom of the screen:

> How often do you want the Task Manager to execute this task: On Demand

- Click Finish at the bottom of the screen.
- To run the on demand task in the Management Portal navigate to the following:

#### System  Operation  Task Manager  On-demand Task

- Find the task named Purge Journal On Demand
- Click the Run link beside the task name.

#### Procedure: Create a scheduled task:

- It is possible but *not recommended* to create a purge journal task to run on a schedule.
- Simply follow the steps above but rather than choose the following:

> How often do you want the Task Manager to execute this task: On Demand

> Instead choose a schedule from the variety of choices available.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/041.png)![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/042.png) NOTE: When purging journals using methods described here can produce Journal Purge errors in the cconsole.log when the nightly purge journal task runs. This happens because the nightly purge tracks journal file names and the number of days retention expected for those journals. When purged before expected the cconsole.log reflects the errors.

> CAUTION: Real journal errors can be mistaken for these errors caused by the early purging of journals. Use caution *not* to become desensitized to these messages and overlook real unexpected errors.

#### Purge Audit Database

> The HL7 Health Connect purge audit database process is TBD.

#### Purge Task

> The HL7 Health Connect purge task process is TBD.

#### Purge Error and Log Files

> The HL7 Health Connect purge error and log files process is TBD.

## Scheduled Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section defines the maintenance schedule for HL7 Health Connect. It includes time intervals (e.g., yearly, quarterly, and monthly) and what *must* be done at each interval. It provides full procedures for each interval and a time estimate for the duration of the system outage. It also defines any processes for scheduling ad-hoc maintenance windows.

### Switch Journaling Back from AltJournal to Journal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HealthShare has a built-in safe guard so that when journaling fills up the /Journal file system it will automatically switch over the /AltJournal file system. This prevents system failures and allows processing to continue until the situation can be resolved. Once journaling switches from

> /Journal to /AltJournal it will *not* switch back automatically. However, the procedure for switching back to the normal state is quite simple once the space issue is resolved.

> To switch journaling back from AltJournal to Journal, do the following:

1.  Prepare for switching journaling back from AltJournal to Journal by freeing the disk space on the /Journal file system:
    1.  Follow the procedure in Section [<u>2.7.1.2</u>,](#purge-journal-files) “[<u>Purge Journal Files</u>](#purge-journal-files),” for purging all journals.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/043.png) NOTE: This is *not* required for transaction rollbacks or crash recovery.

2.  Verify that this procedure worked and has freed a significant amount of space on the original /Journal file system using the Linux terminal, enter either of the following commands:

> df –h

> Or

> df -Ph \| column –t

3.  If for any reason the procedure for purging journals does *not* work, then consult with an [<u>InterSystems Support</u>](#intersystems-support) representative before proceeding.
4.  In a state of emergency, it is possible to manually remove the files from the /Journal file system, but use caution, because it is possible to create problems with the normal scheduled journal purge in which case you will need to consult with an [<u>InterSystems</u> <u>Support</u>](#intersystems-support) representative to correct that problem. However, it is a correctible problem. Using a Linux terminal, change directories by entering the following command:

> cd /*\<journal\>*

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/044.png)Where *\<journal\>* is the name of the primary journal file system (e.g., /Journal). Run the following command:

> **CAUTION:** Use the following command *with extreme care*:

> rm -i \*

> Once this step is complete, the actual switch is relatively simple.

2.  To switching journaling back from AltJournal to Journal, do the following:
    1.  In the Management Portal navigate to the following:

#### System Administration  Configuration  System Configuration 

> Journal Settings

2.  Make note of the contents of both the Primary journal directory and the Secondary

> journal directory entry (these should never be the same path).

3.  Click on the path in the Primary journal directory field and modify the path to match the Secondary journal directory path.
4.  Click Save. This automatically forces a journal switch and the Primary journal directory resumes control of where the journal files are placed.
5.  Navigate into the Journal Settings a second time and modify the Primary journal directory path back to the original path you noted above.
6.  Click Save. This automatically forces a journal switch and the Primary journal directory is now the original path and journal files will assume writing in the

> /Journal file system.

7.  ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/045.png)Verify that the current journal file is being written to the original /Journal file system.

> CAUTION: Be aware that if the /Journal file system fills up and the /AltJournal file system fills up then all journaling will cease placing the system in jeopardy of catastrophic failure. This safe guard is in place for protection but the situation should be resolved as soon as possible.

## Capacity Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the process and procedures for performing capacity planning reviews. It includes the:

- Schedule for the reviews.
- Method for collecting the data.
- Who performs the reviews.
- How the results of the review will be presented.
- Who will be responsible for adjusting the system’s capacity. The HL7 Health Connect capacity planning process is TBD.

### Initial Capacity Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides an initial capacity plan that forecasts for the first 3-month period and a 12- month period of production.

> The HL7 Health Connect initial capacity plan is TBD.

# Exception Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides a high-level overview of how the HL7 Health Connect system problems are handled. It describes the expectations for how administrators and other operations personnel will respond to and handle system problems. It defines the types of issues that operators and administrators should resolve and the types of issues that *must* be escalated.

> The subsections below provide information necessary to detect and resolve system and application problems. These subsections should be considered the minimum set.

## Routine Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Like most systems, HL7 Health Connect messaging may generate a small set of errors that may be considered routine, in the sense that they have minimal impact on the user and do *not* compromise the operational state of the system. Most of the errors are transient in nature and only require the user to retry an operation. The following subsections describe these errors, their causes, and what, if any, response an operator needs to take.

> While the occasional occurrence of these errors may be routine, getting a large number of an individual error over a short period of time is an indication of a more serious problem. In that case the error needs to be treated as an exceptional condition.

> The following subsections are three general categories of errors that typically generate these kinds of errors.

### Security Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists all security type errors that a user or operator may encounter. It lists each individual error, with a description of what it is, when it may occur, and what the appropriate response to the error should be.

> Security errors can vary for a project/product.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/046.png) REF: For Security type errors specific to a product, see the list of products in the “[<u>Appendix A—Products Migrating from VIE to HL7 Health Connect</u>](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect)” section.

### Time-Outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists all time-out type errors that a user or operator may encounter. It lists each individual error, with a description of what it is, when it may occur, and what the appropriate response to the error should be.

> Time-outs involve csp gateway time outs and connection timeout defined in an ensemble production. Time-Out type errors can vary for a project/product.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/047.png) REF: For Time-Outs type errors specific to a product, see the list of products in the “[<u>Appendix A—Products Migrating from VIE to HL7 Health Connect</u>](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect)” section.

### Concurrency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists all concurrency type errors that a user or operator may encounter. It lists each individual error, with a description of what it is, when it may occur, and what the appropriate response to the error should be.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/048.png) NOTE: This section does *not* apply to HL7 Health Connect.

## Significant Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Significant errors can be defined as errors or conditions that affect the system stability, availability, performance, or otherwise make the system unavailable to its user base. The following subsections contain information to aid administrators, operators, and other support personnel in the resolution of significant errors, conditions, or other issues.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/049.png) REF: For significant errors or conditions that affect the system stability, see Section [<u>2.6.8</u>](#critical-metrics), “[<u>Critical Metrics</u>](#critical-metrics).”

### Application Error Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the error logging functionality, the locations where logs are stored, and what, if any, special tools are needed to view the log entries. For each log, it describes the maximum size, growth rate, rotation, and retention policy. It also identifies any error or alarm messages the system sends to external systems.

> To access application error logs, do the following:

#### SMP  System Operation  System Logs  Application Error Logs

> For any application all Application errors are logged in the Application Error Log. The Operator would select one of the items in the table, as shown in [<u>Figure 44</u>](#_bookmark147):

> <span id="_bookmark147" class="anchor"></span>Redacted Figure 44: Application Error Logs Screen

> The application error details are shown in a separate screen after selection, as shown in [<u>Figure</u>](#_bookmark148) [<u>45</u>](#_bookmark148):

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/050.png)<span id="_bookmark148" class="anchor"></span>Figure 45: Application Error Logs Screen—Error Details

### Application Error Codes and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists all the unique errors that the system can generate. It describes the standard format of these messages. It provides the following information for each error:

- Code associated with each error
- Short and long description
- Severity of the error.
- Possible response to the error:
- HL7 Health Connect can contain many application errors. Use the following path to access the Application Error Logs:

#### SMP  System Operation  System Logs  Application Error Logs

> If applicable, you should perform an analysis for each error.

- For any application all Application errors are logged in the Application Error Log.
- The Operator would select one of the items from the table shown in [<u>Figure 44</u>](#_bookmark147). The details will be shown on this screen shot after selection (see [<u>Figure 45</u>](#_bookmark148)).

### Infrastructure Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA IT systems rely on various infrastructure components, as defined for HL7 Health Connect system in the Logical and Physical Descriptions section of this document. Most, if not all, of these infrastructure components generate their own sets of errors. Each component has its own subsection below that describes how errors are reported.

#### Database

> This section describes the system- or application-specific implementation of the database configuration as it relates to errors, error reporting, and other pertinent information about causes and remedies for database errors.

> To manage databases in the intersystem document, see the InterSystems’ *Maintaining Local Databases* documentation at: [<u>http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GSA_manage#GS</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GSA_manage&GSA_manage_databases) [<u>A_manage_databases</u>](http://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GSA_manage&GSA_manage_databases)

> If a tech needs to expand the database, contact the [<u>InterSystems Support</u>](#intersystems-support) team.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/051.png) REF: For Database usage for specific products, see the list of products in the “[<u>Appendix</u>](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect) [<u>A—Products Migrating from VIE to HL7 Health Connect</u>](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect)” section.

#### Web Server

> This section describes the system- or application-specific implementation of the Web server configuration as it relates to errors, error reporting, and other pertinent information about causes of and remedies for Web server errors.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/052.png) REF: For Web Server usage for specific products, see the list of products in the “[<u>Appendix A—Products Migrating from VIE to HL7 Health Connect</u>](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect)” section.

#### Application Server

> This section describes the system- or application-specific implementation of the application server configuration as it relates to errors, error reporting, and other pertinent information about causes of and remedies for application server errors.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/053.png)REF: For Application Server usage for specific products, see the list of products in the “[<u>Appendix A—Products Migrating from VIE to HL7 Health Connect</u>](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect)” section.

#### Network

> This section describes the system- or application-specific implementation of the network configuration as it relates to errors, error reporting, and other pertinent information on causes and remedy of network errors.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/054.png) NOTE: This section is *not* applicable for HL7 Health Connect at the current time.

#### Authentication & Authorization

> This section describes the system- or application-specific implementation of the authentication and authorization component(s) as it relates to errors, error reporting, and other pertinent information about causes of and remedies for errors.

> The HL7 Health Connect authentication and authorization follows the same model as in Section [<u>2.4</u>](#security-identity-management), “[<u>Security / Identity Management</u>](#security-identity-management).”

#### Logical and Physical Descriptions

> This section includes the logical and physical descriptions of the HL7 Health Connect system.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/055.png) REF: For logical and physical descriptions for specific products, see the list of products in the “[<u>Appendix A—Products Migrating from VIE to HL7 Health Connect</u>](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect)” section.

## Dependent System(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists any systems dependent on HL7 Health Connect. It describes the errors and error reporting as it relates to these systems, and what remedies are available to administrators for the resolution of these errors.

> The HL7 Health Connect dependent systems are TBD.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides any helpful information on troubleshooting that has been learned as part of the development and testing processes, or from the operation of similar systems.

> For troubleshooting HL7 Health Connect, contact the [<u>InterSystems Support</u>](#intersystems-support) team.

## System Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following subsections define the process and procedures necessary to restore the system to a fully operational state after a service interruption. Each of the subsections starts at a specific system state and ends up with a fully operational system.

> The subsections defined below are typical, but *not* comprehensive. These sections define how to recover from the crash of HL7 Health Connect by bringing the system to a known state and then restarting components of the system until it is fully operational.

### Manually Initiate a HealthShare Mirror Failover

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> One situation that allows for a failover is disaster recovery in which the failover node

> (e.g., Backup node) takes over when the primary system is down; this occurs with no downtime. To manually initiate a HealthShare mirror failover, do the following:

1.  Access the Mirror Monitor.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/056.png) REF: To access the Mirror Monitor, follow the procedure in Section [<u>2.6.6.2</u>,](#accessing-mirror-monitor) [<u>Accessing Mirror Monitor</u>.](#accessing-mirror-monitor)

2.  From the “Mirror Monitor” screen, verify the system “normal state” and identify the

> Primary and Backup nodes, as shown in [<u>Figure 46</u>](#_bookmark161):

> <span id="_bookmark161" class="anchor"></span>Redacted Figure 46: Mirror Monitor—Verifying the Normal State (Primary and Backup Nodes)

> In this example ([<u>Figure 46</u>](#_bookmark161)), the following are the Failover Member Names for the

> Primary and Backup nodes:

- Primary: REDACTED
- Backup: REDACTED
3.  From a command line prompt, enter the following command:

> ccontrol list

> This command displays the status, state, and the mirroring Member Type of the instance. As you can see in [<u>Figure 47</u>](#_bookmark162), the following data is displayed for a “normal state”:

- status: running
- mirroring: Member Type = Failover; Status = Primary
- state: ok

> <span id="_bookmark162" class="anchor"></span>redacted Figure 47: Using the “control list” Command—Sample List of Installed Instance and its Status and State on a Primary Server

4.  To initiate a manual failover, issue the following command on the Primary node of the member:

> dzdo control stop *\<INSTANCE NAME\>*

> The dzdo[<sup>1</sup>](#_bookmark163) command is the same as the standard sudo command, except it uses centrify agent to check for rights in active directory, while the native sudo is checking the local

> /etc/sudoers file.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/057.png) REF: For a list of Veterans Health Information Systems and Technology Architecture (VistA) instances by region, see the HC_HL_App_Server_Standards_All_Regions_MASTER.xlsx Microsoft<sup>®</sup> Excel document located at: [<u>http://go.va.gov/sxcu</u>](http://go.va.gov/sxcu)

> <span id="_bookmark163" class="anchor"></span><sup>1</sup> Definition from the Centrify Infrastructure Services website: [<u>https://community.centrify.com/t5/Centrify-</u>](https://community.centrify.com/t5/Centrify-Infrastructure-Services/howto-DZDO-Command/td-p/29835) [<u>Infrastructure-Services/howto-DZDO-Command/td-p/29835</u>.](https://community.centrify.com/t5/Centrify-Infrastructure-Services/howto-DZDO-Command/td-p/29835)

> <span id="_bookmark164" class="anchor"></span>Redacted Figure 48: Using the “dzdo control stop” Command—Manually Stopping the Primary Node to initiate a Failover to the Backup Node

5.  After stopping the Primary node instance, run the following command:

> ccontrol list

> It now shows the status as “down”, as shown in [<u>Figure 49</u>](#_bookmark165):

> <span id="_bookmark165" class="anchor"></span>Redacted Figure 49: Using the “ccontrol list” Command—Sample List of Installed Instance and its Status and State on a Down Server

6.  On the new Primary (Previous Backup) node:
1.  Log into the HealthShare web console.
2.  Navigate to System Operation  Mirror Monitor. You can now see the status of the mirror has changed:
    - The previous Backup node is now the Primary node.
    - The previous Primary node is now Down.
      1.  If you issue the following command on the original Primary node (the same one we just stopped), as shown in [<u>Figure 50</u>](#_bookmark166):

> dzdo control start *\<INSTANCE NAME\>*

> You see the status of that node changes from Down to Backup, as shown in [Figure 51.](#_bookmark167)

> <span id="_bookmark166" class="anchor"></span>Redacted Figure 50: Using the “dzdo control start” Command—Manually Starting the Down Node as the Backup Node

> <span id="_bookmark167" class="anchor"></span>Redacted Figure 51: Using the “control list” Command—Sample List of Installed Instance and its Status and State on a Backup Server

2.  Access the Mirror Monitor.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/058.png) REF: To access the Mirror Monitor, follow the procedure in Section [<u>2.6.6.2</u>,](#accessing-mirror-monitor) [<u>Accessing Mirror Monitor</u>.](#accessing-mirror-monitor)

3.  From the “Mirror Monitor” screen, verify the system is restored to its “normal state” (Primary & Backup nodes), as shown in [<u>Figure 52</u>](#_bookmark168):

> <span id="_bookmark168" class="anchor"></span>Redacted Figure 52: Mirror Monitor—Verifying the Current Primary and Backup Nodes: Switched after a Manual Failover

> In this example ([<u>Figure 52</u>](#_bookmark168)), the following are the Failover Member Names for the

> Primary and Backup nodes:

- Primary: REDACTED
- Backup: REDACTED

> When you compare the Failover Member data in in [<u>Figure 52</u>](#_bookmark168) with the original data in [<u>Figure 46</u>,](#_bookmark161) you can see the Primary and Backup nodes have been switched.

### Recover from a HealthShare Mirror Failover

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To recover from a HealthShare mirror failover and return to the original state, do the following:

4.  On the current Primary node (REDACTED; original

> Backup node, see [<u>Figure 46</u>](#_bookmark161)), enter the following command:

> dzdo control stop *\<INSTANCE NAME\>*

> <span id="_bookmark170" class="anchor"></span>Figure 53: Using the “dzdo control stop” Command

REDACTED

> This brings the current Primary node Down and causes a failover to the current Backup node (REDACTED original Primary node, see [<u>Figure 46</u>](#_bookmark161)), which will become the new Primary node ([<u>Figure 54</u>](#_bookmark171)).

5.  Access the Mirror Monitor.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/059.png) REF: To access the Mirror Monitor, follow the procedure in Section [<u>2.6.6.2</u>,](#accessing-mirror-monitor) [<u>Accessing Mirror Monitor</u>.](#accessing-mirror-monitor)

6.  From the “Mirror Monitor” screen, verify the current system state and identify the

> <span id="_bookmark171" class="anchor"></span>Primary and Down nodes, as shown in [<u>Figure 54</u>](#_bookmark171):

> Redacted Figure 54: Mirror Monitor—Verifying the Current Primary and Down Nodes

> In this example ([<u>Figure 54</u>](#_bookmark171)), the following are the Failover Member Names for the

> Primary and Down (formerly Backup) nodes:

- Primary: REDACTED
- Down: REDACTED
7.  On the Down node (REDACTED enter the following command:

> dzdo control start *\<INSTANCE NAME\>*

> <span id="_bookmark172" class="anchor"></span>Figure 55: Using the “dzdo control start” Command

> REDACTED

8.  This process reinstates the node as the Backup node; it is returned to the original configuration.

> <span id="_bookmark173" class="anchor"></span>Figure 56: Mirror Monitor—Verifying the Current Primary and Backup Nodes: Returned to the Original Node States after the Recovery Process

REDACTED

> In this example ([<u>Figure 56</u>](#_bookmark173)), the following are the restored Failover Member Names for the Primary and Backup nodes after the recovery process:

- Primary: REDACTED
- Backup: REDACTED

### Restart after Non-Scheduled System Interruption

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the restart of the system after the crash of the main application. It covers the failure of other components as alternate flows to the main processes.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/060.png) REF: For more information on startup, see the “[<u>System Start-Up</u>](#system-start-up)” section.

### Restart after Database Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to restart the system after restoring from a database backup.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/061.png) REF: For more information on startup, see the “[<u>System Start-Up</u>](#system-start-up)” section.

### Back-Out Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HL7 Health Connect Deployment and Installation Plan includes sections about Back-Out and Rollback Procedures.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/062.png) REF: For more information on back-up and restore procedures, see the “[<u>Back-Up &</u>](#back-up-restore) [<u>Restore</u>](#back-up-restore)” section.

### Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HL7 Health Connect Deployment and Installation Plan includes sections about Back-Out and Rollback procedures.

> The HL7 Health Connect rollback procedures are TBD.

# Operations and Maintenance Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains [<u>Table 6: HL7 Health Connect—Operations and Maintenance</u>](#_bookmark179) [<u>Responsibilities</u>](#_bookmark179) and an attached completed Responsible, Accountable, Consulted, and Informed (RACI) Matrix that defines the key roles required for the Operations and Maintenance (O&M) of the HL7 Health Connect system.

> The HL7 Health Connect operations and maintenance responsibilities table entries are TBD.

> The RACI identifies who is responsible for key activities, such as hardware and software support during the O&M phase of the product’s lifecycle. It includes identifying the Sustainment Support resources.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/063.png) NOTE: The RACI and POM documents are kept as separate documents located under source control in the EHRM FM24 Documentation Rational Jazz RTC and in SharePoint [<u>here</u>.](https://vaww.oed.portal.va.gov/pm/hppmd/fm222iwg/FileMan%2024/FM24%20RACI/FM24_RACI_20180615.xlsx)

- Responsible, Accountable, Consulted, and Informed (RACI) (i.e., FM24_RACI.xlsx)
- Production Operations Manual (POM)

> (i.e., HC-HL7_Messaging_1_0_POM.docx)

> The POM and the RACI are “living” documents and will be updated throughout the system lifecycle.

> <span id="_bookmark179" class="anchor"></span>Table 6: HL7 Health Connect—Operations and Maintenance Responsibilities

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 30%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Role &amp; Brief Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Assigned Organization (Pillar and Sub-office)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Contact Information</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Tier 0:</strong> Local End User Support</p>
<p>(e.g., Automated Data Processing Application Coordinator [ADPAC])</p>
</blockquote></td>
<td><blockquote>
<p>Local ADPAC, Veterans Health Information Systems and Technology Architecture (VistA) or Enterprise Service designated for each Local VAMC and or each Region</p>
</blockquote></td>
<td><blockquote>
<p>Will be for separate for each VA Medical Center (VAMC) location.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Enterprise Service Desk (ESD) Tier 1:</strong> Provide first contact resolution via Knowledge Documents retained in <u>Enterprise Service</u> <a href="#tier-2"><u>Desk (ESD)</u></a> Manager (ServiceNow)</p>
</blockquote></td>
<td><blockquote>
<p>ITOPs (Enterprise Service Desk [ESD])</p>
</blockquote></td>
<td><blockquote>
<p><strong>855-673-4357</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 30%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Role &amp; Brief Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Assigned Organization (Pillar and Sub-office)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Contact Information</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Tier 2:</strong> The second level of service provider functions, which include problem screening, definition, and resolution. Service requests that <em>cannot</em> be resolved at this level in a set period of time are elevated to appropriate service providers at the Tier 3 level.</p>
</blockquote></td>
<td><blockquote>
<p>HSH EO Incident Management</p>
</blockquote></td>
<td><blockquote>
<p>ESD Tickets escalated to Tier 2 POC: OIT EPMO TRS EPS HSH</p>
<p>Incident Response</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Tier 3</strong>: The third level of service provider functions, which consist primarily of problem identification, diagnosis, and resolution. Service requests that <em>cannot</em> be resolved at the Tier 2 level are typically referred to the Tier 3 for resolution.</p>
</blockquote></td>
<td><blockquote>
<p>VA OIT FM24 VA and</p>
<p>Contractors</p>
</blockquote></td>
<td><blockquote>
<p>ESD Tickets escalated to Tier 3 POC: VA OIT FM24 VA and</p>
<p>Contractors</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Tier 4:</strong> COTS Support from InterSystems. To be engaged if Tier 3 <em>cannot</em> determine root cause or resolve issue.</p>
</blockquote></td>
<td><blockquote>
<p>To contact InterSystems for Technical Assist 24/7, you can call the toll-free number: <strong>1-800-227-2114</strong></p>
<p>Email: <a href="mailto:support@intersystems.com"><u>support@intersystems.com</u></a></p>
</blockquote></td>
<td><blockquote>
<p>InterSystems Support: <a href="https://www.intersystems.com/support-learning/support/immediate-help/"><u>https://www.intersystems.com/support-</u></a> <a href="https://www.intersystems.com/support-learning/support/immediate-help/"><u>learning/support/immediate-help/</u></a></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 30%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Role &amp; Brief Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Assigned Organization (Pillar and Sub-office)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Contact Information</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Receiving Org/Sustainment Manager: Coordinates ongoing support activities including budget reporting, contract management, and technical risk management during O&amp;M.</p>
<p> If applicable, include key details such as whether this individual will be reviewing deliverables from an O&amp;M contract.</p>
</blockquote></td>
<td><blockquote>
<p>EPMO: Transition, Release, and Support (TRS)</p>
</blockquote></td>
<td><blockquote>
<p>POC: REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>COR  Check with the Contracting Officer to determine if a certified COR is required and at what level during O&amp;M.</p>
</blockquote></td>
<td><blockquote>
<p>EPMO</p>
</blockquote></td>
<td><blockquote>
<p>POC: <em>&lt; TBD: Insert Contact &gt;</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Contracting Office</p>
</blockquote></td>
<td><blockquote>
<p>Technical Acquisition Center (TAC)</p>
</blockquote></td>
<td><blockquote>
<p>POC: <em>&lt; TBD: Insert Contact &gt;</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

## RACI Matrix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Responsible, Accountable, Consulted, and Informed (RACI) document

> (i.e., FM24_RACI.xlsx) is kept as a separate document located under source control in the EHRM FM24 Documentation Rational Jazz RTC and in SharePoint at: REDACTED

> The RACI is a “living” document that will be updated throughout the system lifecycle.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/064.png) NOTE: Due to Section 508 conformance requirements, the RACI document *cannot* be embedded into this document.

# Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Signatures indicate the approval of the InterSystems HL7 Health Connect Messaging Production Operations Manual (POM) and accompanying RACI.

> Currently, there are 14 applications that will be migrated from VistA Interface Engine (VIE) to HL7 Health Connect; so, each individual application added will require a separate “Approval Signatures” section.

> To approve and sign this POM for [<u>Outpatient Pharmacy Automation Interface (OPAI)</u>](#outpatient-pharmacy-automation-interface-opai), see the “[<u>OPAI Approval Signatures</u>](#opai-approval-signatures)” section.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/065.png) REF: For a list of all products scheduled to be migrated from VIE to HL7 Health Connect, see the “[<u>Appendix A—Products Migrating from VIE to HL7 Health Connect</u>](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect)” section.

> Eventually, all 14 of these applications will be added to this POM with separate subsections (including separate approval signature blocks) in [<u>Appendix A</u>](#appendix-aproducts-migrating-from-vie-to-hl7-health-connect).

# Appendix A—Products Migrating from VIE to HL7 Health Connect

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HL7 Health Connect (HC) production system replaces the current functionality provided by the Vitria Interface Engine (VIE), with messaging routed through the HL7 Health Connect production system.

> As the VA consolidates onto one enterprise health information interface engine, the FM 24 project team is migrating messaging from VIE to InterSystems HL7 Health Connect (HealthShare). This effort ensures that all Veteran health information is consistent as it is shared across the VA enterprise. Leveraging existing VA IT investments and reducing the number of messaging platforms; therefore, driving efficiency.

> Over time, the following 14 applications will be migrated from VIE to HL7 Health Connect:

- [<u>Pharmacy Automated Dispensing Equipment (PADE)</u>](#pharmacy-automated-dispensing-equipment-pade)
- [<u>Outpatient Pharmacy Automation Interface (OPAI)</u>](#outpatient-pharmacy-automation-interface-opai)
- Laboratory Electronic Data Interchange (LEDI) / Lab Data Sharing and Interoperability (LDSI) Lab Data
- Claims Processing & Eligibility (CPE)
- Enrollment System ESR/MVR (eGate)
- Federal Health Information Exchange (FHIE) / Bidirectional Health Information Exchange (BHIE) / Data Sharing Interface (DSI)
- Electronic Contract Management System (eCMS)
- National Provider Identifier (NPI)
- Federal Procurement Data System (FPDS)
- Remote Order Entry System (ROES)
- Standards Terminology Service (STS)
- Transcription Services (Shadowlink, Goodwill)
- Clinical/Health Data Repository (CHDR)
- Health Data Repository (HDR)

> As each application is migrated from VIE to HL7 Health Connect, a new sub-section will be added to this Production Operations Manual (POM) appendix.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/066.png) NOTE: [<u>Pharmacy Automated Dispensing Equipment (PADE)</u>](#pharmacy-automated-dispensing-equipment-pade) was the first application to migrate and will be used as a template for the other applications that follow.

## Pharmacy Automated Dispensing Equipment (PADE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains content specific to the Pharmacy Automated Dispensing Equipment (PADE) system. PADE is the first system to migrate from VIE to HL7 Health Connect.

> This section describes how to maintain the components of the HL7 Health Connect Production as well as how to troubleshoot problems that might occur with PADE in production. The intended audience for this document is the Office of Information and Technology (OIT) teams responsible for hosting and maintaining the PADE system after production release.

### Review PADE System Default Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to access the PADE system default settings and review the current settings for the following environments:

- [<u>PADE Pre-Production Environment—System Default Settings</u>](#pade-pre-production-environmentsystem-default-settings)
- ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/067.png)[<u>PADE Production Environment—System Default Settings</u>](#pade-production-environmentsystem-default-settings)

> CAUTION: Once the environment is setup and in operation you should *not*

> change these system default settings!

> To access the “System Default Settings” page, do the following:

#### SMP  Ensemble  Configure  System Default Settings

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/068.png) NOTE: In the future, what is currently a manual process will be automated and the “System Default Settings” page will only be used to verify system information.

#### PADE Pre-Production Environment—System Default Settings

> [<u>Figure 57</u>](#_bookmark186) displays the current PADE *Pre-Production* system default settings:

> <span id="_bookmark186" class="anchor"></span>REDACTED Figure 57: PADE “System Default Settings” Page—Pre-Production

> The list of PADE *Pre-Production* IP addresses/DNS depicted in <u>[Figure 59](#_bookmark189)7</u> is stored in a secure folder on SharePoint.

> [<u>Figure 58</u>](#_bookmark187) displays the PADE *Pre-Production* key value system defaults:

> <span id="_bookmark187" class="anchor"></span>REDACTED Figure 58: PADE Ensemble “Production Configuration” Page System Defaults—Pre-Production

> On the Settings tab for the highlighted operation in [<u>Figure 58</u>,](#_bookmark187) make sure the “IP Address” is blue, which indicates it is a system default.

#### PADE Production Environment—System Default Settings

> [<u>Figure 59</u>](#_bookmark189) displays the current PADE *Production* system default settings:

> <span id="_bookmark189" class="anchor"></span>REDACTED Figure 59: PADE “System Default Settings” Page—Production

> The list of PADE *Production* IP addresses/DNS depicted in [<u>Figure 59</u>](#_bookmark189) is stored in a secure folder on SharePoint.

> [<u>Figure 60</u>](#_bookmark190) displays the PADE *Production* key value system defaults:

> <span id="_bookmark190" class="anchor"></span>REDACTED Figure 60: PADE Ensemble “Production Configuration” Page System Defaults—Production

> On the Settings tab for the highlighted operation in [<u>Figure 60</u>,](#_bookmark190) make sure the “IP Address” is blue, which indicates it is a system default.

### Review PADE Router Lookup Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to access the PADE router lookup settings and review the current settings for the following environments:

- [<u>PADE Pre-Production Environment—Router Settings</u>](#pade-pre-production-environmentrouter-settings)
- [<u>PADE Production Environment—Router Settings</u>](#pade-production-environmentrouter-settings)

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/069.png)CAUTION: Once the environment is setup and in operation you should *not*

> change these router lookup settings!

> To access the “Lookup Table Viewer” page, do the following:

#### SMP  Ensemble  Configure  Data Lookup Tables

#### PADE Pre-Production Environment—Router Settings

> [<u>Figure 61</u>](#_bookmark193) displays the PADE *Pre-Production* lookup settings for the InboundRouter:

> <span id="_bookmark193" class="anchor"></span>REDACTED Figure 61: PADE Lookup Table Viewer Page—Pre-Production InboundRouter

> [<u>Figure 62</u>](#_bookmark194) displays the PADE *Pre-Production* lookup settings for the OutboundRouter:

> <span id="_bookmark194" class="anchor"></span>REDACTED Figure 62: PADE Lookup Table Viewer Page—Pre-Production OutboundRouter

#### PADE Production Environment—Router Settings

> [<u>Figure 63</u>](#_bookmark196) displays the PADE *Production* lookup settings for the InboundRouter:

> <span id="_bookmark196" class="anchor"></span>REDACTED Figure 63: PADE Lookup Table Viewer Page—Production InboundRouter

> [<u>Figure 64</u>](#_bookmark197) displays the PADE *Production* lookup settings for the OutboundRouter:

> <span id="_bookmark197" class="anchor"></span>REDACTED Figure 64: PADE Lookup Table Viewer Page—Production OutboundRouter

### PADE Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For troubleshooting PADE:

- Enter an Incident or Request ticket in ITSM ServiceNow system.
- Contact [<u>Tier 2</u>](#tier-2) or <u>VA Enterprise Service Desk (ESD)</u>.
- Contact [<u>InterSystems Support</u>](#intersystems-support).

#### PADE Common Issues and Resolutions

> <span id="_bookmark200" class="anchor"></span>Table 7: PADE—Common Issues and Resolutions

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 37%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Issue</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Common Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Support Contact</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>The registration team transfers/cancels admission/cancels discharges/re- admits trying to fix some copay issues. This ends up discharging the patient from PADE. They had to find out the hard way by reviewing the sequences of the HL7 messages from the PADE Outbound Message file.</p>
</blockquote></td>
<td><blockquote>
<p>Sites need to be aware that for any such Admission/Discharge/Transfer (ADT) changes, Pharmacy needs to be informed and to make sure the patient is on PADE along with the orders. In this case, the orders were <em>not</em> there, so he/she was able to re- send the orders by using the <strong>PSJ PADE Send Order</strong> option.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PADE is <em>not</em> receiving messages.</p>
</blockquote></td>
<td><blockquote>
<p>Check to see if logical link is working.</p>
<p>Submit a <a href="#tier-2"><u>YourIT (ServiceNow)</u></a> ticket.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>What is the contingency plan if Health Connect goes down?</p>
</blockquote></td>
<td><blockquote>
<p>For all of the applications that are supported by Health Connect (HC), if a site has an issue they think is related to HC, they can open a <a href="#tier-2"><u>YourIT</u></a> <a href="#tier-2"><u>(ServiceNow)</u></a> ticket In the case of PADE, they should open a High Priority <a href="#tier-2"><u>YourIT</u></a> <a href="#tier-2"><u>(ServiceNow)</u></a> ticket by calling the VA <a href="#tier-2"><u>Enterprise Service Desk</u></a> <a href="#tier-2"><u>(ESD)</u></a>. Request that the help desk get a member of the HC National Admin team on the phone 24/7. PADE is supported in the same way as OPAI.</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect Support (mail group TBD) —Submit <a href="#tier-2"><u>YourIT</u></a> <a href="#tier-2"><u>(ServiceNow)</u></a> Ticket</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PADE Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For back-out and rollback procedures, see the *PADE Deployment, Installation, Back-Out, and Roll Back Guide* (HC_PADE_1_0_IG.docx) document located at: [<u>http://go.va.gov/sxcu</u>](http://go.va.gov/sxcu).

### PADE Business Process Logic (BPL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Workflow logic to route HL7 messages based on Receiving Facility ID:

1.  <span id="_bookmark203" class="anchor"></span>Get Receiving Facility. Assign the MSH:ReceivingFacility.universalID, which is piece

> 6.2 from the MSH header, to receivingSystem.

2.  Look up Business Operation. Create a sql statement Lookup Business Operation to get the receivingBusinessoperation value from the Outboundrouter table based on the receivingSystem value from [<u>Step 1</u>](#_bookmark203).

> <span id="_bookmark204" class="anchor"></span>Figure 65: Sample sql Statement

3.  If condition to check receivingBusinessOperation value is empty:
    1.  If receivingBusinessOperation is null, send an alert to the Support Grp and move the message to the BadMessageHandler. Support Grp will need to check the MSH segment of the message and verify that an entry for the Universal Id in the MSH segment exists in the Outbound Router Table and maps to a corresponding Operation value (see [<u>Figure 68</u>](#_bookmark210)).
    2.  If receivingBusinessOperation is *not* empty continue to [<u>Step 4</u>](#_bookmark205).
4.  <span id="_bookmark205" class="anchor"></span>If condition to check the Operation value in Outbound Router is Enabled:
    1.  If Operation is *not*Enabled send out an alert to the [<u>Tier 2</u>](#tier-2) support group, to enable the Operation and continue to [Step 5.](#_bookmark206)
    2.  If Operation is Enabled continue to [Step 5](#_bookmark206).
5.  <span id="_bookmark206" class="anchor"></span>Send to Outbound Operator. Send the HL7 message to the Configured Business Operation.

<span id="_bookmark207" class="anchor"></span>REDACTED Figure 66: Business Process Logic (BPL) for OutRouter

#### PADE Message Sample

<span id="_bookmark209" class="anchor"></span>REDACTED Figure 67: PADE—Message Sample

<span id="_bookmark210" class="anchor"></span>REDACTED Figure 68: BPL—Outbound Router Table with MSH Segment Entry to Operation: PADE

<span id="_bookmark211" class="anchor"></span>REDACTED Figure 69: BPL—Enabled Operation 999.PADE.Server

#### PADE Alerts

> <span id="_bookmark213" class="anchor"></span>Table 8: PADE—Alerts

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Alert</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Automatically Resend HL7 Message</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect shall place the HL7 message in a queue and automatically resend the message for the system configured time period until an Accept Acknowledgment commit response is received:</p>
</blockquote>
<ul>
<li><p><strong>CA</strong>—Commit Accept</p></li>
<li><p><strong>CE</strong>—Commit Error</p></li>
<li><p><strong>CR</strong>—Commit Reject</p></li>
</ul>
<blockquote>
<p>This setting can be found on the business operation by going to</p>
<p><strong>Settings</strong> tab and updating <strong>Failure Timeout</strong>.</p>
<p>In this situation, the business operation should turn purple (see <a href="#_bookmark214"><u>Figure 70</u></a> and <a href="#_bookmark215"><u>Figure 71</u></a>).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Send Email Alert(s) that System or Device Offline</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect sends designated operations support personnel email alert(s) identifying the system or device that is offline based on the configured system parameter for frequency to send email alerts.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Send Email Alert Message Queue Size Exceeded</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect sends an email alert to designated Health Connect operations support personnel when the message send queue exceeds the configurable message queue limit. This setting can be found on the business operation by going to settings tab and updating Queue Count Alert.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Send Email Alert When Commit Reject Message Received</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect sends an email alert to designated Health Connect operations support personnel when it receives a commit reject message in response to sending an HL7 message. This setting can be found on the business operation by going to settings tab and updating Reply Code Actions.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Send Email Alert When Commit Error Message Received</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect sends an email alert to designated Health Connect operations support personnel when it receives a commit error message in response to sending an HL7 message. This setting can be found on the business operation by going to settings tab and updating Reply Code Actions.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark214" class="anchor"></span>REDACTED Figure 70: PADE—Alerts: Automatically Resent HL7 Message: Operations List showing PADE Server with Purple Indicator (Retrying)

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/070.png)<span id="_bookmark215" class="anchor"></span>Figure 71: HL7 Health Connect—Production Configuration Legend: Status Indicators

### PADE Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The signatures in this section indicate the approval of the HL7 InterSystems Health Connect Production Operations Manual (POM) and accompanying RACI for the Pharmacy Automated Dispensing Equipment (PADE) application.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/071.png) NOTE: Digital signatures will only be added to the PDF version of the Microsoft<sup>®</sup> Word document (i.e., HC-HL7_Messaging_1_0_POM-Signed.pdf).

> REVIEW DATE: *\<date\>*

> SCRIBE: *\<name\>*

> Signed: REDACTED Date

> Program Manager Common Services

> Signed:

> REDACTED Date

> Pharmacy Informatics Specialist (PBM)

> Signed: REDACTED Date

> Division Chief, Application Hosting, Transition & Migration Division

## Outpatient Pharmacy Automation Interface (OPAI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains content specific to the Outpatient Pharmacy Automation Interface (OPAI) system. OPAI is the second system to migrate from VIE to HL7 Health Connect.

> This section describes how to maintain the components of the HL7 Health Connect Production as well as how to troubleshoot problems that might occur with OPAI in production. The intended audience for this document is the Office of Information and Technology (OIT) teams responsible for hosting and maintaining the OPAI system after production release.

### Review OPAI System Default Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to access the OPAI system default settings and review the current settings for the following environments:

- [<u>OPAI Pre-Production Environment—System Default Settings</u>](#opai-pre-production-environmentsystem-default-settings)
- ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/072.png)[<u>OPAI Production Environment—System Default Settings</u>](#opai-production-environmentsystem-default-settings)

> CAUTION: Once the environment is setup and in operation you should *not*

> change these system default settings!

> To access the “System Default Settings” page, do the following:

#### SMP  Ensemble  Configure  System Default Settings

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/073.png) NOTE: In the future, what is currently a manual process will be automated and the “System Default Settings” page will only be used to verify system information.

#### OPAI Pre-Production Environment—System Default Settings

> [<u>Figure 72</u>](#_bookmark220) displays the current OPAI *Pre-Production* system default settings:

<span id="_bookmark220" class="anchor"></span>REDACTED Figure 72: OPAI “System Default Settings” Page—Pre-Production

> [<u>Table 9</u>](#_bookmark221) lists only the OPAI *Pre-Production* IP addresses/DNS depicted in [<u>Figure 72</u>](#_bookmark220):

<span id="_bookmark221" class="anchor"></span>Table 9: OPAI System IP Addresses/DNS—Pre-Production

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 40%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Item Name (_Port Number)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Internet Protocol (IP) Address or Domain Name Server (DNS)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Port</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>To_OPAI640_Parata_9025</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>To_OPAI640_Pickpoint_9300</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>To_OPAI678_Scriptpro_9600</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>To_VISTA640_5025</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>To_VISTA678_5025</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

> [<u>Figure 73</u>](#_bookmark222) displays the OPAI *Pre-Production* key value system defaults:

<span id="_bookmark222" class="anchor"></span>REDACTED Figure 73: OPAI Ensemble “Production Configuration” Page System Defaults—Pre-Production

> On the Settings tab for the highlighted operation in [<u>Figure 73</u>,](#_bookmark222) make sure the “IP Address” is blue, which indicates it is a system default.

#### OPAI Production Environment—System Default Settings

> [<u>Figure 74</u>](#_bookmark224) displays the current OPAI *Production* system default settings:

<span id="_bookmark224" class="anchor"></span>Figure 74: OPAI “System Default Settings” Page—Production

*\< TBD: Insert Production Image Here \>*

> [<u>Table 10</u>](#_bookmark225) lists only the OPAI *Production* IP addresses/DNS depicted in [<u>Figure 74</u>](#_bookmark224):

<span id="_bookmark225" class="anchor"></span>Table 10: OPAI System IP Addresses/DNS—Production (will be updated once in production)

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 40%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Item Name (_Port Number)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Internet Protocol (IP) Address or Domain Name Server (DNS)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Port</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> [<u>Figure 75</u>](#_bookmark226) displays the OPAI *Production* key value system defaults:

<span id="_bookmark226" class="anchor"></span>Figure 75: OPAI Ensemble “Production Configuration” Page System Defaults—Production

*\< TBD: Insert Production Image Here \>*

> On the Settings tab for the highlighted operation in [<u>Figure 75</u>,](#_bookmark226) make sure the “IP Address” is blue, which indicates it is a system default.

### Review OPAI Router Lookup Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to access the OPAI router lookup settings and review the current settings for the following environments:

- [<u>OPAI Pre-Production Environment—Router Settings</u>](#opai-pre-production-environmentrouter-settings)
- ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/074.png)[<u>OPAI Production Environment—Router Settings</u>](#opai-production-environmentrouter-settings)

> CAUTION: Once the environment is setup and in operation you should *not*

> change these router lookup settings!

> To access the “Lookup Table Viewer” page, do the following:

#### SMP  Ensemble  Configure  Data Lookup Tables

#### OPAI Pre-Production Environment—Router Settings

> [<u>Figure 76</u>](#_bookmark229) displays the OPAI *Pre-Production* lookup settings for the InboundRouter:

<span id="_bookmark229" class="anchor"></span>REDACTED Figure 76: OPAI Lookup Table Viewer Page—Pre-Production InboundRouter

> [<u>Figure 77</u>](#_bookmark230) displays the OPAI *Pre-Production* lookup settings for the OutboundRouter:

<span id="_bookmark230" class="anchor"></span>REDACTED Figure 77: OPAI Lookup Table Viewer Page—Pre-Production OutboundRouter

#### OPAI Production Environment—Router Settings

> [<u>Figure 78</u>](#_bookmark232) displays the OPAI *Production* lookup settings for the InboundRouter:

<span id="_bookmark232" class="anchor"></span>Figure 78: OPAI Lookup Table Viewer Page—Production InboundRouter

*\< TBD: Insert Production Image Here \>*

> [<u>Figure 79</u>](#_bookmark233) displays the OPAI *Production* lookup settings for the OutboundRouter:

<span id="_bookmark233" class="anchor"></span>Figure 79: OPAI Lookup Table Viewer Page—Production OutboundRouter

*\< TBD: Insert Production Image Here \>*

### OPAI Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For troubleshooting OPAI:

- Enter an Incident or Request ticket in ITSM ServiceNow system.
- Contact [<u>Tier 2</u>](#tier-2) or <u>VA Enterprise Service Desk (ESD)</u>.
- Contact [<u>InterSystems Support</u>](#intersystems-support).

#### OPAI Common Issues and Resolutions

> <span id="_bookmark236" class="anchor"></span>Table 11: OPAI—Common Issues and Resolutions

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 37%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Issue</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Common Resolution</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Support Contact</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>When putting a medication order through OPAI application in VistA, the sites fail to receive an acknowledgement message in VistA.</p>
</blockquote></td>
<td><blockquote>
<p>Sites need to be aware to check the WP fields and make sure there are no blank lines or ending characters, which cause end of messages in Health Connect.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OPAI is <em>not</em> receiving messages.</p>
</blockquote></td>
<td><blockquote>
<p>Check to see if logical link is working.</p>
<p>Submit a <a href="#tier-2"><u>YourIT (ServiceNow)</u></a> ticket.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>What is the contingency plan if Health Connect goes down?</p>
</blockquote></td>
<td><blockquote>
<p>For all of the applications that are supported by Health Connect (HC), if a site has an issue they think is related to HC, they can open a <a href="#tier-2"><u>YourIT</u></a> <a href="#tier-2"><u>(ServiceNow)</u></a> ticket. In the case of OPAI or Outpatient Automation Interface (OPAI), they should open a High Priority <a href="#tier-2"><u>YourIT (ServiceNow)</u></a> ticket by calling the VA <a href="#tier-2"><u>Enterprise</u></a> <a href="#tier-2"><u>Service Desk (ESD)</u></a>. Request that the ESD get a member of the HC National Admin team on the phone 24/7. OPAI is supported in the same way as PADE.</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect Support (mail group TBD)—Submit <a href="#tier-2"><u>YourIT</u></a> <a href="#tier-2"><u>(ServiceNow)</u></a> Ticket</p>
</blockquote></td>
</tr>
</tbody>
</table>

### OPAI Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For back-out and rollback procedures, see the *OPAI Deployment, Installation, Back-Out, and Roll Back Guide* (HC_OPAI_1_0_IG.docx) document located at: [<u>http://go.va.gov/sxcu</u>.](http://go.va.gov/sxcu)

### OPAI Business Process Logic (BPL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Workflow logic to route HL7 messages based on Receiving Facility ID:

1.  <span id="_bookmark239" class="anchor"></span>Get Receiving Facility. Assign the MSH:ReceivingFacility.universalID, which is piece

> 6.2 from the MSH header, to receivingSystem.

2.  Look up Business Operation. Create a sql statement Lookup Business Operation to get the receivingBusinessoperation value from the Outboundrouter table based on the receivingSystem value from [<u>Step 1</u>](#_bookmark239).

> <span id="_bookmark240" class="anchor"></span>Figure 80: Sample sql Statement

3.  If condition to check receivingBusinessOperation value is empty:
    1.  If receivingBusinessOperation is null, send an alert to the Support Grp and move the message to the BadMessageHandler. Support Grp will need to check the MSH segment of the message and verify that an entry for the Universal Id in the MSH segment exists in the Outbound Router Table and maps to a corresponding Operation value (see [<u>Figure 83</u>](#_bookmark246)).
    2.  If receivingBusinessOperation is *not* empty continue to [<u>Step 4</u>](#_bookmark241).
4.  <span id="_bookmark241" class="anchor"></span>If condition to check the Operation value in Outbound Router is Enabled:
    1.  If Operation is *not*Enabled send out an alert to the [<u>Tier 2</u>](#tier-2) support group, to enable the Operation and continue to [Step 5.](#_bookmark242)
    2.  If Operation is Enabled continue to [Step 5](#_bookmark242).
5.  <span id="_bookmark242" class="anchor"></span>Send to Outbound Operator. Send the HL7 message to the Configured Business Operation.

> <span id="_bookmark243" class="anchor"></span>REDACTED Figure 81: Business Process Logic (BPL) for OutRouter

#### OPAI Message Sample

> <span id="_bookmark245" class="anchor"></span>Figure 82: OPAI—Message Sample

> MSH\|~^\\\|PSO VISTA\|REDACTED ~DNS\|PSO DISPENSE\|~REDACTED~DNS\|19990530113424- 0400\|\|RDS~O13\|999157291007\|T\|2.4\|\|\|AL\|AL\|USA PID\|\|\|101085731\~\~~USSSA&&0363~SS~VA FACILITY ID&456&L^""\~\~~USDOD&&0363~TIN~VA FACILITY ID&456&L^""\~\~~USDOD&&0363~FIN~VA FACILITY ID&456&L^16392\~\~~USVHA&&0363~PI~VA FACILITY ID&456&L^508056640\~\~~USVBA&&0363~PN~VA FACILITY

> ID&456&L\|\|NAME~EMPLOYEE\~\~\~\~~L^""\~\~\~\~\~~N\|\|19671008\|M\|\|\|4596 IRON HORSE RD~""~ANYCITY~WY~00001~USA~P~""~021^\~~ANYPLACE~NE\~~""~N\|\|(555)555-

> 5555~PRN~PH^(555)555-5555~WPN~PH^(555)555-5555~ORN~CP\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\| PV1\|\|O\|

> PV2\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|OPT SC~NO COPAY\| IAM\|\|D~DRUG~LGMR120.8\|20009~CODEINE~LGMR120.8\|U\|PHARMACOLOGIC\|\|\|\|\|\|\|\|\|\|\|\|C ORC\|NW\|2210376~OP7.0\|\|\|\|\|\|\|19990430\|520824646~EMPLOYEE~EMPLOYEENAME~E\|\|520675728~REDACTED\|RX1\|\|19990430\|REFILL\|325~CHY EMERGENCY ROOM~99PSC\|\|\|\|ANYSITE VAM&ROC\~~999\|P.O. BOX 20350\~~ANYSITE~WY~99999- 7008\|(307)778-7524

> NTE\|1\|\|TAKE ONE TABLET BY MOUTH ONCE DAILY FOR 15 DAYS TESTING\|Medication

> Instructions

> NTE\|2\|\|Do not allow your medication to run short. Order the next shipment of medication assoon as you receive the medication in themail. Pharmacy Telephone Numbers: EMERGENCYMedication: (307) 778-7555 (Call Center):888- 483-9127 \*\*Ask for Extension 4205\*\*\* (Auto-Attendant): 866-420- 6337(Nights,Weekends, Holidays) \|Patient Narrative

> NTE\|3\|\|SEE MEDICATION INFORMATION SHEET FOR DRUG INFO\\sp\Some non-

> prescription drugs may aggravate your condition. Read all labels carefully. If a warning appears, check with your doctor.\|Drug Warning Narrative

> RXE\|""\|A1345~ALISKIREN 150MG TAB~99PSNDF~4230.18208.4452~ALISKIREN 150MG TAB~99PSD\|\|\|20~MG~99PSU\|63~TAB~99PSF\|\|WALK- IN\|\|15\|~TAB\|11\|BM3747271\|\~~\|2297748\|9\|2\|19990521\|\|\|~ALISKIREN 150MG

> TAB^~ALISKIREN 150MG TAB\|\|\|\|\|\|\|\|\|\|N^0^N

> RXD\|2\|A1345~ALISKIREN 150MG TAB~99PSNDF~4230.18208.4452~ALISKIREN 150MG TAB~99PSD\|19990530\|\|\|\|2297748\|11\|6P^00078-0485- 15\|520824646~EMPLOYEE~EMPLOYEENAME~E\|\|30\|WINDOW\|\|~SAFETY\|\|\|\|20190501\|\|\|\|\|\|33~PATIEN

> T INFO^9N~^\|\|

> NTE\|7\|\|ALISKIREN - ORAL\H\WARNING\N\\ This drug can cause serious (possibly fatal) harm to an unborn baby if used during pregnancy. Therefore, it is important to prevent pregnancy while taking this medication. Consult your doctor for more details and to discuss the use of reliable forms of birth control while taking this medication. If you are planning pregnancy, become pregnant, or think you may be pregnant, tell your doctor right away.\H\\ USES\N\\ This medication is used to treat high blood pressure (hypertension). Lowering high blood pressure helps prevent strokes, heart attacks, and kidney problems. Aliskiren works by relaxing blood vessels so blood can flow more easily. It belongs to a class of drugs known as direct renin inhibitors. This drug is not recommended for use in children younger than 6 years or who weigh less than 44 pounds (20 kilograms) due to an increased risk of side effects.\H\\ HOW TO USE\N\\ Read the Patient Information Leaflet if available from your pharmacist before you start taking this medication and each time you get a refill. If you have any questions, ask your doctor or pharmacist. Take this medication by mouth as directed by your doctor, usually once daily. You may take this medication with or without food, but it is important to choose one way and take this medication the same way with every dose.

> High-fat foods may decrease how well this drug is absorbed by the body, so it is best to avoid taking this medication with a high-fat meal. Do not take with fruit juices (such as apple, grapefruit, or orange) since they may decrease the absorption of this drug. The dosage is based on your medical condition and response to treatment. Take this medication regularly to get the most benefit from it. To help you remember, take it at the same time each day. It is important to continue taking this medication even if you feel well. Most people with high blood pressure do not feel sick. It may take 2 weeks before you get the full benefit of this medication. Tell your doctor if your condition does not improve or if it worsens (your blood pressure readings remain high or increase).\H\\ SIDE EFFECTS\N\\ Dizziness, lightheadedness, cough, diarrhea, or tiredness may occur. If any of these effects persists or worsens, tell your doctor or pharmacist promptly. To reduce the risk of dizziness and lightheadedness, get up slowly when rising from a sitting or lying position. Remember that your doctor has prescribed this medication because he or she has judged that the benefit to you is greater than the risk of side effects. Many people using this medication do not have serious side effects. Tell your doctor right away if you have any serious side effects, including: fainting, symptoms of a high potassium blood level (such as muscle weakness, slow/irregular heartbeat), signs of kidney problems (such as change in the amount of urine). A very serious allergic reaction to this drug is rare. However, get medical help right away if you notice any symptoms of a serious allergic reaction, including: rash, itching/swelling (especially of the face/tongue/throat), severe dizziness, trouble breathing. This is not a complete list of possible side effects. If you notice other effects not listed above, contact your doctor or pharmacist. In the US - Call your doctor for medical advice about side effects. You may report side effects to FDA at 1-800-FDA-1088 or at [www.fda.gov/medwatch.](http://www.fda.gov/medwatch) In Canada - Call your doctor for medical advice about side effects. You may report side effects to Health Canada at 1-866- 234-2345.\H\\ PRECAUTIONS\N\\ Before taking aliskiren, tell your doctor or pharmacist if you are allergic to it; or if you have any other allergies. This product may contain inactive ingredients, which can cause allergic reactions or other problems. Talk to your pharmacist for more details.

> Before using this medication, tell your doctor or pharmacist your medical history, especially of: diabetes, kidney disease, severe loss of body water and minerals (dehydration). This drug may make you dizzy. Alcohol or

> marijuana can make you more dizzy. Do not drive, use machinery, or do anything that needs alertness until you can do it safely. Limit alcoholic beverages. Talk to your doctor if you are using marijuana. Too much sweating, diarrhea, or vomiting may cause you to feel lightheaded. Report prolonged diarrhea or vomiting to your doctor. This medication may increase your potassium levels. Before using potassium supplements or salt substitutes that contain potassium, consult your doctor or pharmacist.

> Before having surgery, tell your doctor or dentist about all the products you use (including prescription drugs, nonprescription drugs, and herbal products). This medication is not recommended for use during pregnancy. It may harm an unborn baby. Consult your doctor for more details. (See also Warning section.) It is unknown if this drug passes into breast milk.

> Consult your doctor before breast-feeding.\H\\ DRUG INTERACTIONS\N\\ See also How to Use and Precautions sections. Drug interactions may change how your medications work or increase your risk for serious side effects. This document does not contain all possible drug interactions. Keep a list of all the products you use (including prescription/nonprescription drugs and herbal products) and share it with your doctor and pharmacist. Do not start, stop, or change the dosage of any medicines without your doctor's approval. Some products that may interact with this drug include: drugs that may increase the level of potassium in the blood (including ACE inhibitors such as benazepril/lisinopril, ARBs such as candesartan/losartan, birth control pills containing drospirenone). Other medications can affect the removal of aliskiren from your body, which may affect how aliskiren works. Examples include itraconazole, cyclosporine, quinidine, among others. Some products have ingredients that could raise your blood pressure. Tell your pharmacist what products you are using, and ask how to use them safely (especially cough-and-cold products, diet aids, or NSAIDs such as ibuprofen/naproxen).\H\\ OVERDOSE\N\\ If someone has overdosed and has serious symptoms such as passing out or trouble breathing, call 911. Otherwise, call a poison control center right away.

> US residents can call their local poison control center at 1-800-222-1222. Canada residents can call a provincial poison control center. Symptoms of overdose may include: severe dizziness, fainting.\H\\ NOTES\N\\ Do not share this medication with others. Lifestyle changes that may help this medication work better include exercising, stopping smoking, and eating a low-cholesterol/low-fat diet. Consult your doctor for more details.

> Laboratory and/or medical tests (such as kidney function, potassium levels) should be performed regularly to monitor your progress or check for side effects. Have your blood pressure checked regularly while taking this medication. Learn how to monitor your own blood pressure at home, and share the results with your doctor.\H\\ MISSED DOSE\N\\ If you miss a dose, take it as soon as you remember. If it is near the time of the next dose, skip the missed dose and resume your usual dosing schedule. Do not double the dose to catch up.\|Patient Medication Instructions

> NTE\|9\|\|The VA Notice of Privacy Practices, IB 10-163, which outlines your privacy rights, is available online at <http://www1.va.gov/Health/> or you may obtain a copy by writing the VHA Privacy Office (19F2),810 Vermont Avenue NW, Washington, DC 20420.\|Privacy Notification

> RXR\|1~ORAL (BY MOUTH)~99PSR\|\|\|\|

<span id="_bookmark246" class="anchor"></span>REDACTED Figure 83: BPL—Outbound Router Table with MSH Segment Entry to Operation: OPAI

<span id="_bookmark247" class="anchor"></span>Figure 84: BPL—Enabled Operation To_OPAI640_Parata_9025

REDACTED

#### OPAI Alerts

> <span id="_bookmark249" class="anchor"></span>Table 12: OPAI—Alerts

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Alert</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Automatically Resend HL7 Message</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect shall place the HL7 message in a queue and automatically resend the message for the system configured time period until an Accept Acknowledgment commit response is received:</p>
</blockquote>
<ul>
<li><p><strong>CA</strong>—Commit Accept</p></li>
<li><p><strong>CE</strong>—Commit Error</p></li>
<li><p><strong>CR</strong>—Commit Reject</p></li>
</ul>
<blockquote>
<p>This setting can be found on the business operation by going to</p>
<p><strong>Settings</strong> tab and updating <strong>Failure Timeout</strong>.</p>
<p>In this situation, the business operation should turn purple (see <a href="#_bookmark250"><u>Figure 85</u></a> and <a href="#_bookmark251"><u>Figure 86</u></a>).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Alert</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Send Email Alert(s) that System or Device Offline</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect sends designated operations support personnel email alert(s) identifying the system or device that is offline based on the configured system parameter for frequency to send email alerts.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Send Email Alert Message Queue Size Exceeded</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect sends an email alert to designated Health Connect operations support personnel when the message send queue exceeds the configurable message queue limit. This setting can be found on the business operation by going to settings tab and updating Queue Count Alert.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Send Email Alert When Commit Reject Message Received</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect sends an email alert to designated Health Connect operations support personnel when it receives a commit reject message in response to sending an HL7 message. This setting can be found on the business operation by going to settings tab and updating Reply Code Actions.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Send Email Alert When Commit Error Message Received</p>
</blockquote></td>
<td><blockquote>
<p>Health Connect sends an email alert to designated Health Connect operations support personnel when it receives a commit error message in response to sending an HL7 message. This setting can be found on the business operation by going to settings tab and updating Reply Code Actions.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark250" class="anchor"></span>Figure 85: OPAI—Alerts: Automatically Resent HL7 Message: Operations List showing OPAI Server with Purple Indicator (Retrying)

REDACTED

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/075.png)<span id="_bookmark251" class="anchor"></span>Figure 86: HL7 Health Connect—Production Configuration Legend: Status Indicators

### OPAI Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The signatures in this section indicate the approval of the HL7 InterSystems Health Connect Production Operations Manual (POM) and accompanying RACI for the Outpatient Pharmacy Automation Interface (OPAI) application.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/076.png) NOTE: Digital signatures will only be added to the PDF version of the Microsoft<sup>®</sup> Word document (i.e., HC-HL7_Messaging_1_0_POM-Signed.pdf).

<span id="7_Appendix_B—Configuring_Alert_Email_Not" class="anchor"></span>REDACTED

REDACTED

REDACTED

# Appendix B—Configuring Alert Email Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section is used to configure alert email notifications to receive, review, and process Level 2

> alerts. The procedures described in this section are a one-time setup.

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/077.png) NOTE: This appendix may be moved to an Install Guide.

## Configure Level 2 Alerting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure Level 2 alerting, which includes Mirror Monitoring, because mirror error events are Level 2 errors, do the following ([<u>Figure 87</u>](#_bookmark255)):

1.  Start the Caché Monitor Manager by entering the following command at a Caché prompt:

> DO ^MONMGR

2.  At the first “Option?” prompt select the Manage MONITOR Options option.
3.  At the next “Option?” prompt, select the Set Alert Level option.
4.  At the “Alert on Severity (1=warning,2=severe,3=fatal)?” prompt, enter 2 to select Level 2 alerts.

> <span id="_bookmark255" class="anchor"></span>Figure 87: Choose Alert Level for Alert Notifications

> “Becoming primary mirror server” is a Level 2 alert, so it is reported as long as this is set below Level 3.

## Configure Email Alert Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure email alert notifications, do the following ([<u>Figure 88</u>](#_bookmark258)):

5.  Start the Caché Monitor Manager by entering the following command at a Caché prompt:

> DO ^MONMGR

6.  At the first “Option?” prompt select the Manage MONITOR Options option.
7.  At the next “Option?” prompt, select the Manage Email Options option.
8.  At the next “Option?” prompt, choose any of the options listed in [<u>Table 13</u>](#_bookmark257) to completed setting up your email notifications:

> <span id="_bookmark257" class="anchor"></span>Table 13: Manage Email Options Menu Options

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Option</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1) Enable / Disable Email</p>
</blockquote></td>
<td><blockquote>
<p>Enabling email causes Caché Monitor to:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Send an email notification for each item currently in the alerts log, if any.</p>
</blockquote></li>
<li><p>Delete the <strong>alerts.log</strong> file (if it exists).</p></li>
<li><p>Send email notifications for console log entry of the configured severity from that point forward.</p></li>
</ul>
<blockquote>
<p>Disabling email causes Caché Monitor to write entries to the <strong>alerts</strong> log.</p>
<p>Enabling/disabling email does <em>not</em> affect other email settings; that is, it is <em>not</em> necessary to reconfigure email options when you enable/disable email.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2) Set Sender</p>
</blockquote></td>
<td><blockquote>
<p>Select this option to enter text that indicates the sender of the email (e.g., Cache Monitor). The text you enter does <em>not</em> have to represent a valid email account. You can set this field to <strong>NULL</strong> by entering <strong>-</strong> (dash).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3) Set Server</p>
</blockquote></td>
<td><blockquote>
<p>Select this menu item to enter the name and port number (default <strong>25</strong>) of the email server that handles email for your site. Consult your IT staff to obtain this information. You can set this field to <strong>NULL</strong> by entering <strong>-</strong> (dash).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4) Manage Recipients</p>
</blockquote></td>
<td><blockquote>
<p>This option displays a submenu that lets you list, add, or remove the email addresses to which each notification is sent:</p>
<p>Each valid email address <em>must</em> be added individually; when you select 2) Add Recipient, do <em>not</em> enter more than one address when responding to the “Email Address?” prompt.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5) Set Authentication</p>
</blockquote></td>
<td><blockquote>
<p>This option lets you specify the authentication username and password if required by your email server. Consult your IT staff to obtain this information. If you do <em>not</em> provide entries, the authentication username and password are set to <strong>NULL</strong>. You can set the User field to <strong>NULL</strong> by entering <strong>-</strong> (dash).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6) Test Email</p>
</blockquote></td>
<td><blockquote>
<p>This option sends a test message to the specified recipients using the specified email server.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7) Exit</p>
</blockquote></td>
<td><blockquote>
<p>This option returns to the <strong>Manage Monitor Options</strong></p>
<p>submenu.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark258" class="anchor"></span>Figure 88: Configure Email Alert Notifications

> ![](intersystems-health-connect-hl7-messaging-production-operations-manual-pom-maste/078.png) REF: For more information on InterSystems’ ^MONMGR utility and how to configure email notifications, see the InterSystems online documentation: [<u>https://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_mo</u>](https://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_monitor_system_manager) [<u>nitor_system_manager</u>](https://docs.intersystems.com/latest/csp/docbook/DocBook.UI.Page.cls?KEY=GCM_monitor_system_manager)