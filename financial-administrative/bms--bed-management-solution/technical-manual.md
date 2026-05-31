---
title: Bed Management Solution Version 2.4 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: null
app_code: BMS
app_name: Bed Management Solution
section: FIN
app_status: archive
pkg_ns: BMS
patch_ver: 2.4
patch_id: BMS*2.4
group_key: BMS:BMS:2.4
file_numbers: []
security_keys: []
menu_options: 4
description: '- Bed Management Solution (BMS) - Technical Manual - Revision History - List of Tables - Introduction - Purpose - BMS Overview - References -...'
audience: Technical staff, IRM, system administrators
keywords: []
page_count: 0
word_count: 83195
section_count: 34
table_count: 0
figure_count: 0
appendix_count: 2
has_toc: false
is_stub: false
pub_date: null
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/Bed_Management_Solution_(BMS)_Archive/bms_2_0_tm_2_4.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/Bed_Management_Solution_(BMS)_Archive/bms_2_0_tm_2_4.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=247
audit_applied: '2026-05-31'
master_source: Bed Management Solution Version 2.4 Technical Manual
master_pub_date: 'null'
consolidated_from: 11 versions
prior_versions:
- Bed Management Solution Version 2.11 Technical Manual
- Bed Management Solution Version 2.5 Technical Manual
- Bed Management Solution Version 2.6 Technical Manual
- Bed Management Solution Version 2.8 Technical Manual
- Bed Management Solution Version 2.9 Technical Manual
- Bed Management Solution Version 3.10 Technical Manual
- Bed Management Solution Version 3.3 Technical Manual
- Bed Management Solution Version 3.7 Technical Manual
- Bed Management Solution Version 3.8 Technical Manual
- Bed Management Solution Version 5.0 Technical Manual
consolidated_title: bed management solution technical manual
---

# Bed Management Solution (BMS)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Bed Management Solution (BMS)](#bed-management-solution-bms)
    - [Technical Manual](#technical-manual)
    - [Revision History](#revision-history)
    - [List of Tables](#list-of-tables)
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [BMS Overview](#bms-overview)
  - [References](#references)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [BMS Infrastructure Diagram](#bms-infrastructure-diagram)
  - [System Requirements (Hardware and Software)](#system-requirements-hardware-and-software)
  - [Configuration Parameters](#configuration-parameters)
  - [Scheduled Windows and SQL Jobs Configuration](#scheduled-windows-and-sql-jobs-configuration)
    - [BMS Reports Full](#bms-reports-full)
    - [BMS Incremental](#bms-incremental)
    - [BMS Reports Windows Management Instrumentation (WMI)](#bms-reports-windows-management-instrumentation-wmi)
  - [Ward Whiteboard Kiosk Mode Display Configuration (BMS Whiteboard Kiosk Setup)](#ward-whiteboard-kiosk-mode-display-configuration-bms-whiteboard-kiosk-setup)
    - [Create the Ward Whiteboard Kiosk URL](#create-the-ward-whiteboard-kiosk-url)
    - [Set up a default user for the BMS Kiosk](#set-up-a-default-user-for-the-bms-kiosk)
    - [Set up the Workstation / Kiosk Machine](#set-up-the-workstation-kiosk-machine)
  - [Whiteboard Snapshot Configuration](#whiteboard-snapshot-configuration)
    - [Create Snapshot Folder](#create-snapshot-folder)
    - [Define Network Share](#define-network-share)
    - [Assign Rights to Master BMS Service Account User](#assign-rights-to-master-bms-service-account-user)
    - [Assign Snapshot Folder Path to Ward Group](#assign-snapshot-folder-path-to-ward-group)
    - [Associate Scheduler with Whiteboard Report](#associate-scheduler-with-whiteboard-report)
  - [EMS Mobile Device Configuration](#ems-mobile-device-configuration)
    - [Configure EMS Mobile Device Default Login User](#configure-ems-mobile-device-default-login-user)
    - [Configure EMS Mobile Device URL](#configure-ems-mobile-device-url)
  - [VistA Integration](#vista-integration)
    - [Choose VistA Site](#choose-vista-site)
    - [Define Schedulers](#define-schedulers)
    - [Run Scheduler](#run-scheduler)
    - [View Audit Results](#view-audit-results)
  - [NUMI Integration](#numi-integration)
    - [Integration Settings](#integration-settings)
    - [Choose VistA Site](#choose-vista-site-1)
    - [Define Schedulers](#define-schedulers-1)
    - [Select Scheduler](#select-scheduler)
- [Application structure](#application-structure)
  - [Application Components](#application-components)
  - [Application Directory Structure](#application-directory-structure)
  - [Database Architecture](#database-architecture)
  - [Component Files](#component-files)
- [Archiving](#archiving)
- [External Relationships](#external-relationships)
- [External Interfaces](#external-interfaces)
- [Software Security](#software-security)
  - [Policy Manager](#policy-manager)
  - [Operation Definitions](#operation-definitions)
  - [Task Definitions](#task-definitions)
  - [Role Definitions](#role-definitions)
  - [Assigning a Role to a User](#assigning-a-role-to-a-user)
  - [Adding a New Role](#adding-a-new-role)
  - [Adding a New Task](#adding-a-new-task)
  - [Adding a New Operation](#adding-a-new-operation)
  - [Business scenarios and use cases](#business-scenarios-and-use-cases)
- [Detailed Functional Model on Each Interface](#detailed-functional-model-on-each-interface)
  - [Service contracts](#service-contracts)
  - [Data contracts](#data-contracts)
  - [BMS Roles](#bms-roles)
- [Troubleshooting](#troubleshooting)
- [Appendix A – BMS Diagrams](#appendix-a-bms-diagrams)
  - [Business Process Diagrams](#business-process-diagrams)
  - [Activity Diagram](#activity-diagram)
  - [Functional Flow Diagram](#functional-flow-diagram)
  - [Data Flow Diagram](#data-flow-diagram)
  - [Application Flow Map from APPDYNAMICS](#application-flow-map-from-appdynamics)
- [Appendix B - Terms, Acronyms, and Abbreviations](#appendix-b-terms-acronyms-and-abbreviations)

### Technical Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bed-management-solution-version-2-4-technical-manual/001.png)
> January 2020

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 27%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Creation Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version No.</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description/Comments</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Reviewer(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Review Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Issue Date</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>01/13/2020</p>
</blockquote></td>
<td><blockquote>
<p>0.12</p>
</blockquote></td>
<td><blockquote>
<p>Updated for Version 2.4: Minor editing changes to format. Updated release dates on title page and</p>
<p>footer.</p>
</blockquote></td>
<td><blockquote>
<p><strong>REDACTED</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4/23/2019 –</p>
<p>07/24/2019</p>
</blockquote></td>
<td><blockquote>
<p>0.11</p>
</blockquote></td>
<td><blockquote>
<p>Updated document for BMS v2.3.1: Updates to Figure Diagrams to reflect current BMS is using VIA not MDWS, updated parameter tables to include VIA parameters, updated, new service account user to reflect new service account</p>
<p>for new server migration.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>07/24/2019</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12/19/2016</p>
</blockquote></td>
<td><blockquote>
<p>0.10</p>
</blockquote></td>
<td><blockquote>
<p>Updated for BMS 2.1 merge of VAE MDWS–VIA</p>
<p>migration</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11/29/2016</p>
</blockquote></td>
<td><blockquote>
<p>0.9</p>
</blockquote></td>
<td><blockquote>
<p>Updated for December 2016 Release, added section "CA SiteMinder Web Agent"</p>
<p>installation</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11/2/2016</p>
</blockquote></td>
<td><blockquote>
<p>0.8</p>
</blockquote></td>
<td><blockquote>
<p>Updated document for Public VDA Portal, 508 compliance and removed real servernames and url</p>
<p>addresses.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8/5/2016</p>
</blockquote></td>
<td><blockquote>
<p>0.7</p>
</blockquote></td>
<td><blockquote>
<p>Updated document for BMS v2.0: Updates to Figure 1 Diagram, SQL Server</p>
<p>version, ASP.NET, MVC.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>8/12/2016</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 27%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Creation Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version No.</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description/Comments</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Reviewer(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Review Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Issue Date</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3/4/2016</p>
</blockquote></td>
<td><blockquote>
<p>0.6</p>
</blockquote></td>
<td><blockquote>
<p>Removed real URL and server addresses and replaced them with generic address names throughout the document</p>
</blockquote></td>
<td><blockquote>
<p><strong>REDACTED</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>3/4/2016</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7/15/2015</p>
</blockquote></td>
<td><blockquote>
<p>0.5</p>
</blockquote></td>
<td><blockquote>
<p>Final team review</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>7/15/15</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/05/2015</p>
</blockquote></td>
<td><blockquote>
<p>0.5</p>
</blockquote></td>
<td><blockquote>
<p>Technical edit. Fix issues with table of tables and table of figures.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>06/30/2015</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6/05/2015</p>
</blockquote></td>
<td><blockquote>
<p>0.5</p>
</blockquote></td>
<td><blockquote>
<p>Updated the following sections:</p>
</blockquote>
<ol start="2" type="1">
<li><p>System Requirements</p></li>
<li><blockquote>
<p>Configuration Parameters</p>
</blockquote></li>
<li><blockquote>
<p>Scheduled Windows and SQL Jobs Configuration</p>
</blockquote>
<ol type="1">
<li><p>BMS Reports Full</p></li>
<li><blockquote>
<p>BMS Incremental</p>
</blockquote></li>
<li><blockquote>
<p>BMS Reports WMI</p>
</blockquote></li>
</ol></li>
<li><blockquote>
<p>Ward Whiteboard Kiosk Setup</p>
</blockquote></li>
<li><blockquote>
<p>Whiteboard Snapshot Configuration</p>
</blockquote></li>
<li><blockquote>
<p>EMS Mobile Defice Configuration</p>
</blockquote></li>
</ol>
<blockquote>
<p>2.9 NUMI Integration</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>6/30/2015</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 27%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 9%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Creation Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version No.</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description/Comments</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Reviewer(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Review Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Issue Date</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><ol start="3" type="1">
<li><p>Database Architecture</p></li>
<li><blockquote>
<p>Component Files 7 Software Security</p>
</blockquote></li>
</ol></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>07/17/2013</td>
<td><blockquote>
<p>0.4</p>
</blockquote></td>
<td><blockquote>
<p>Updated section 2.3 Configuration Parameters, updated section 2.5 Whiteboard Kiosk Mode, updated section 2.7 EMS Mobile Device Configuration, added Appendix 9.5,</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td>07/19/2013</td>
</tr>
<tr class="odd">
<td>07/29/2013</td>
<td><blockquote>
<p>0.3</p>
</blockquote></td>
<td><blockquote>
<p>Updated section 2.8.1.1 to include the MDWS Endpoint.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td>08/06/2013</td>
</tr>
<tr class="even">
<td>10/07/2013</td>
<td><blockquote>
<p>0.2</p>
</blockquote></td>
<td><blockquote>
<p>Updated section 2.2 with service account information, Renamed and Updated section 2.6.3, Added a note to section 2.6.4, added log files to section 8.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td>10/15/2013</td>
</tr>
<tr class="odd">
<td>06/12/2013</td>
<td><blockquote>
<p>0.1</p>
</blockquote></td>
<td><blockquote>
<p>Initial baseline.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td></td>
<td></td>
<td>07/09/2013</td>
</tr>
</tbody>
</table>
1.  [Introduction 11](#introduction)
    1.  [Purpose 11](#purpose)
    2.  [BMS Overview 11](#bms-overview)
    3.  [References 11](#references)
2.  [Implementation and Maintenance 12](#implementation-and-maintenance)
    1.  [BMS Infrastructure Diagram 12](#bms-infrastructure-diagram)
    2.  [System Requirements (Hardware and Software) 13](#system-requirements-hardware-and-software)
    3.  [Configuration Parameters 15](#configuration-parameters)
    4.  [Scheduled Windows and SQL Jobs Configuration 116](#scheduled-windows-and-sql-jobs-configuration)
        1.  [BMS Reports Full 116](#bms-reports-full)
        2.  [BMS Incremental 137](#bms-incremental)
        3.  [BMS Reports Windows Management Instrumentation (WMI) 144](#bms-reports-windows-management-instrumentation-wmi)
    5.  [Ward Whiteboard Kiosk Mode Display Configuration (BMS Whiteboard Kiosk Setup)](#ward-whiteboard-kiosk-mode-display-configuration-bms-whiteboard-kiosk-setup)
[............................................................................................................................ 145](#ward-whiteboard-kiosk-mode-display-configuration-bms-whiteboard-kiosk-setup) [2.5.1](#create-the-ward-whiteboard-kiosk-url) [Create the Ward Whiteboard Kiosk URL ............................................................ 147](#create-the-ward-whiteboard-kiosk-url)
2.  [Set up a default user for the BMS Kiosk 148](#set-up-a-default-user-for-the-bms-kiosk)
3.  [Set up the Workstation / Kiosk Machine 150](#set-up-the-workstation-kiosk-machine)
6.  [Whiteboard Snapshot Configuration 160](#whiteboard-snapshot-configuration)
    1.  [Create Snapshot Folder 160](#create-snapshot-folder)
    2.  [Define Network Share 161](#define-network-share)
    3.  [Assign Rights to Master BMS Service Account User 163](#assign-rights-to-master-bms-service-account-user)
    4.  [Assign Snapshot Folder Path to Ward Group 168](#assign-snapshot-folder-path-to-ward-group)
    5.  [Associate Scheduler with Whiteboard Report 168](#associate-scheduler-with-whiteboard-report)
7.  [EMS Mobile Device Configuration 169](#ems-mobile-device-configuration)
    1.  [Configure EMS Mobile Device Default Login User 169](#configure-ems-mobile-device-default-login-user)
    2.  [Configure EMS Mobile Device URL 171](#configure-ems-mobile-device-url)
8.  [VistA Integration 172](#vista-integration)
    1.  [Choose VistA Site 172](#choose-vista-site)
    2.  [Define Schedulers 173](#define-schedulers)
    3.  [Run Scheduler 174](#run-scheduler)
    4.  [View Audit Results 175](#view-audit-results)
9.  [NUMI Integration 177](#numi-integration)
[Integration Settings 177](#integration-settings)
1.  [Choose VistA Site 178](#choose-vista-site-1)
2.  [Define Schedulers 178](#define-schedulers-1)
3.  [Select Scheduler 178](#select-scheduler)
3.  [Application structure 179](#application-structure)
    1.  [Application Components 179](#application-components)
    2.  [Application Directory Structure 179](#application-directory-structure)
    3.  [Database Architecture 180](#database-architecture)
    4.  [Component Files 181](#component-files)
4.  [Archiving 206](#archiving)
5.  [External Relationships 206](#external-relationships)
6.  [External Interfaces 207](#external-interfaces)
7.  [Software Security 208](#software-security)
    1.  [Policy Manager 210](#policy-manager)
    2.  [Operation Definitions 210](#operation-definitions)
    3.  [Task Definitions 221](#task-definitions)
    4.  [Role Definitions 231](#role-definitions)
    5.  [Assigning a Role to a User 233](#assigning-a-role-to-a-user)
    6.  [Adding a New Role 234](#adding-a-new-role)
    7.  [Adding a New Task 236](#adding-a-new-task)
    8.  [Adding a New Operation 238](#adding-a-new-operation)
    9.  [Business scenarios and use cases 239](#business-scenarios-and-use-cases)
8.  [Detailed Functional Model on Each Interface 241](#detailed-functional-model-on-each-interface)
    1.  [Service contracts 241](#service-contracts)
[Data contracts 245](#data-contracts)
2.  [BMS Roles 245](#bms-roles)
9.  [Troubleshooting 246](#troubleshooting)
10. [Appendix A – BMS Diagrams 250](#appendix-a-bms-diagrams)
    1.  [Business Process Diagrams 250](#business-process-diagrams)
    2.  [Activity Diagram 254](#activity-diagram)
    3.  [Functional Flow Diagram 256](#functional-flow-diagram)
11. [Appendix B - Terms, Acronyms, and Abbreviations 258](#appendix-b---terms-acronyms-and-abbreviations)

### List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table 1-Server for Web Applications 13](#_bookmark8)
> [Table 2-Application Server 13](#_bookmark9)
> [Table 3-Database Server 14](#_bookmark10)
> [Table 4-BMS ServiceHost Configuration Parameters 15](#_bookmark12)
> [Table 5-EIS Service Configuration Parameters 94](#_bookmark13)
> [Table 6-EVS Service Configuration Parameters 97](#_bookmark14)
> [Table 7-PAP Service Configuration Parameters 101](#_bookmark15)
> [Table 8-PDP Service Configuration Parameters 104](#_bookmark16)
> [Table 9-RS Service Configuration Parameters 105](#_bookmark17)
> [Table 10-STS Service Configuration Parameters 106](#_bookmark18)
> [Table 11-Win ServiceHost Configuration Parameters 109](#_bookmark19)
> [Table 12-WMI User Group Configuration Parameters 110](#_bookmark21)
> [Table 13-Policy Manager Configuration Parameters 110](#_bookmark22)
> [Table 14-BMS Web Configuration Parameters 111](#_bookmark23)
> [Table 15-Ward Whiteboard URL Configuration Parameters 147](#_bookmark61)
> [Table 16-Facility Settings Page Parameters 170](#_bookmark104)
> [Table 17-BMS Admin Page Parameters 171](#_bookmark106)
> [Table 18-Description and Configuration for EMS Mobile Device URL Parameters 171](#_bookmark108)
> [Table 19-New VistA Site Parameters 173](#_bookmark113)
> [Table 20-New Scheduler Parameters 174](#_bookmark116)
> [Table 21-View Aduit Results Columns Report 177](#_bookmark122)
> [Table 22-BMS Database Files 181](#_bookmark136)
> [Table 23-BMS Service Files 183](#_bookmark137)
> [Table 24-WIN Service Host Files 187](#_bookmark138)
> [Table 25-BMS Website Files 196](#_bookmark139)
> [Table 26-Policy Manager Files 205](#_bookmark140)
> [Table 27-BMS Operations 211](#_bookmark153)
> [Table 28- BMS Tasks 223](#_bookmark157)
> [Table 29-Terms, Acronyms, and Abbreviations 258](#_bookmark205)
> List of Figures
> [Figure 1-BMS Infrastructure Diagram 12](#_bookmark6)
> [Figure 2-BMS-Report Full Job 116](#_bookmark26)
> [Figure 3-BMS-Start Full Job 117](#_bookmark27)
> [Figure 4-BMS-Check State Job Incremental 118](#_bookmark28)
> [Figure 5-BMS-Waits 1 Min for Incremental Job to stop 119](#_bookmark29)
> [Figure 6-BMS-Check State Job Incremental 120](#_bookmark30)
> [Figure 7-BMS-Job Step Properties 121](#_bookmark31)
> [Figure 8- BMS- Job Step Properties-Call Stored Procedure 122](#_bookmark32)
> [Figure 9- BMS-Job Step Properties-Call Stored Procedure_SP_Infoworld 123](#_bookmark33)
> [Figure 10-BMS-Job Step Properties_BMS EVS 124](#_bookmark34)
> [Figure 11-BMS- Job Step Procedures-VOCAB 125](#_bookmark35)
> [Figure 12-BMS-Job Step Procedurs-ETL_Processfull_Facts 126](#_bookmark36)
> [Figure 13- BMS- Copy User in history database 127](#_bookmark37)
> [Figure 14- Clear DS data 128](#_bookmark38)
> [Figure 15-BMS-Re-enable Incremental 129](#_bookmark39)
> [Figure 16-On Fail Re-enable Incremental 130](#_bookmark40)
> [Figure 17-BMS-Shrink 131](#_bookmark41)
> [Figure 18-BMS-Clear Data 132](#_bookmark42)
> [Figure 19- BMS-Call Procedure Full 133](#_bookmark43)
> [Figure 20- Copy Users in History Database 134](#_bookmark44)
> [Figure 21-BMS Reports Full Path File Log 135](#_bookmark45)
> [Figure 22- Clear Data from DS 136](#_bookmark46)
> [Figure 23-BMS Start Job and Send Email 137](#_bookmark47)
> [Figure 24- BMS- Report Incremental Job 138](#_bookmark49)
> [Figure 25-BMS-STart Job Incremental 139](#_bookmark50)
> [Figure 26-BMS-Check State Job Full 140](#_bookmark51)
> [Figure 27-BMS-Call Procedure Properties 141](#_bookmark52)
> [Figure 28-BMS-Call Procedure Incremental_DW 142](#_bookmark53)
> [Figure 29- BMS Incremental Path File Log 143](#_bookmark54)
> [Figure 30- BMS-Call Procedure Recalculate Statistics 144](#_bookmark55)
> [Figure 31- BMS Ward Whiteboard Screen 145](#_bookmark58)
> [Figure 33-Facility Settings 149](#_bookmark63)
> [Figure 33- Whiteboard Kiosk User Role Assignment 150](#_bookmark64)
> [Figure 34- Screen Saver Option 151](#_bookmark66)
> [Figure 35- Screen Saver Settings Window 152](#_bookmark67)
> [Figure 36- Power Options 153](#_bookmark68)
> [Figure 37- Change Plan Settings Option 153](#_bookmark69)
> [Figure 38- Power Options Settings 154](#_bookmark70)
> [Figure 39- Run Window 154](#_bookmark71)
> [Figure 40- Run Window with Comman Entered 155](#_bookmark72)
> [Figure 41- User Accounts Window 155](#_bookmark73)
> [Figure 42- User Accounts 156](#_bookmark74)
> [Figure 43- Tools Menu of Internet Explorer 157](#_bookmark75)
> [Figure 44- General Tab of Internet Options 157](#_bookmark76)
> [Figure 45- Open Option 158](#_bookmark77)
> [Figure 46- Internet Explorer Shortcut 159](#_bookmark78)
> [Figure 47-Windows Registry Editor 159](#_bookmark79)
> [Figure 48- Whiteboard Snapshot Folder 161](#_bookmark82)
> [Figure 49- Whiteboard Snapshot Folder Properties 161](#_bookmark84)
> [Figure 50- Advanced Sharing Option 162](#_bookmark85)
> [Figure 51- Share this Folder Option 162](#_bookmark86)
> [Figure 52- Permissions for Whiteboard Snapshot 163](#_bookmark88)
> [Figure 53-Select Users or Groups Window 163](#_bookmark89)
> [Figure 54- Advanced Section of Select Users or Group Window 164](#_bookmark90)
> [Figure 55- Search Result Section 165](#_bookmark91)
> [Figure 56- Object Names Section 165](#_bookmark92)
> [Figure 57- Permissions Window 166](#_bookmark93)
> [Figure 58- User Permissions 167](#_bookmark94)
> [Figure 59- Advanced Sharing Window 167](#_bookmark95)
> [Figure 60- WardGroup1-PC Path 168](#_bookmark96)
> [Figure 61-Contingency Settings Page 168](#_bookmark98)
> [Figure 62- Whiteboard Report Scheduler Association 169](#_bookmark100)
> [Figure 63- EMS Fields Filled on the Facility Settings Page 170](#_bookmark103)
> [Figure 64-EMS Fields Filled on the BMS Admin Page 171](#_bookmark105)
> [Figure 65-EMS Staff Page for Mobile Devices 172](#_bookmark109)
> [Figure 66-Adding a VistA Site 173](#_bookmark112)
> [Figure 67-Schedulers Tab 174](#_bookmark115)
> [Figure 68-VistA Integration Tab 175](#_bookmark118)
> [Figure 69- Aduit Tab 176](#_bookmark120)
> [Figure 70- View Aduit Results 176](#_bookmark121)
> [Figure 71-NUMI Tab 178](#_bookmark128)
> [Figure 72- Selecting the VistA Site for NUMI data 179](#_bookmark129)
> [Figure 73-Database Architecture 181](#_bookmark134)
> [Figure 74-Backup Maintenance Plan 206](#_bookmark142)
> [Figure 75-BMS Exnternal Interfaces 207](#_bookmark146)
> [Figure 76-Security Services Architecture 209](#_bookmark148)
> [Figure 77-Policy Manager Main Window 210](#_bookmark150)
> [Figure 78-Operation Definition 211](#_bookmark152)
> [Figure 79-Task Definition 222](#_bookmark155)
> [Figure 80-Operations Defining a Task 223](#_bookmark156)
> [Figure 81-Role Definition 232](#_bookmark159)
> [Figure 82-Assigning Roles to Users 233](#_bookmark161)
> [Figure 83-New Role Definition 234](#_bookmark163)
> [Figure 84-Adding Tasks and Operations to a Role 235](#_bookmark164)
> [Figure 85-Add Role to Role Assignments List 236](#_bookmark165)
> [Figure 86-New Task Definition 237](#_bookmark167)
> [Figure 87-Adding Operations to a Task 238](#_bookmark168)
> [Figure 88-New Operation Definition 238](#_bookmark170)
> [Figure 89-Authentication Use Cases 239](#_bookmark172)
> [Figure 90-Authorization Use Cases 239](#_bookmark173)
> [Figure 91- Authorization Administration Use Cases 240](#_bookmark174)
> [Figure 92-Class Diagram for Data Contracts in PAP and PDP 245](#_bookmark178)
> [Figure 93-500 Server Error 246](#_bookmark181)
> [Figure 94-No Facilities Error 247](#_bookmark182)
> [Figure 95-Unhandled Exception 247](#_bookmark183)
> [Figure 96-Login Unsuccessful 248](#_bookmark184)
> [Figure 97- EMS Bed Status Report is Missing 249](#_bookmark185)
> [Figure 98- Report Cannot be Found 249](#_bookmark186)
> [Figure 99-Admit Patient to PPBP Business Proces 250](#_bookmark189)
> [Figure 100-Transfer Patients to PPBP Business Process 251](#_bookmark190)
> [Figure 101-Display and Update PPBP Business Process 251](#_bookmark191)
> [Figure 102-Display and Update Bed Status Business Process 252](#_bookmark192)
> [Figure 103-Manage Bed Cleaning Business Process 252](#_bookmark193)
> [Figure 104-Create Notification Business Process 253](#_bookmark194)
> [Figure 105-Create Facility Diversion Business Process 253](#_bookmark195)
> [Figure 106-Manage Whiteboard Business Process 254](#_bookmark196)
> [Figure 107-Reports Business Process 254](#activity-diagram)
> [Figure 108-BMS Overview Activity Diagram 255](#_bookmark199)
> [Figure 109-BMS Overview Functional Flow Diagram 256](#_bookmark201)
> [Figure 110-BMS Overview Data Flow Diagram 257](#_bookmark202)
> [Figure 111-Application Flow map from APPDYNAMICS 258](#_bookmark203)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document is designed to provide sufficient technical information about the Bed Management Solution (BMS) application to the developers and Information Resources Management (IRM) technical personnel to operate and maintain the software.

## BMS Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS is a real-time, user-friendly Web-based Veterans Health Information Systems and Technology Architecture (VistA) interface for tracking patient movement, bed status and bed availability. It provides performance information that can be used to improve patient flow within, and between, VA Medical Centers (VAMCs).

> BMS allows administrative and clinical staff to record, manage and report on the planning, patient- movement, patient occupancy, and other activities related to management of beds. All patient admission, discharge, and transfer movements are sent directly from VistA to BMS.

> BMS offers the following features:

- Tracks patient movement through the system;
- Displays patient and bed occupancy status for all beds in the facility and/or Veterans Integrated Service Networks (VISN);
- Provides visibility of bed availability within VAMC's to support emergency management;
- Automates request and assignment of beds;
- Displays and facilitates timely discharge appointments;
- Supports and facilitates efficient flow operations and is a catalyst to process improvement and best practices;
- Provides reports on performance measures associated with bed management and patient flow. BMS provides answers to the following questions:
  - How many beds do we have?
  - How many empty beds do we have?
  - How many available female beds do we have?
  - How many beds are out of service and why?
  - How long does it take to clean a bed?
  - How many patients are waiting for beds in community hospitals?
  - How many admissions, transfers, and discharges did my unit have yesterday?
  - How many discharges will we have tomorrow?
  - How many scheduled admissions do we have for today?

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Requirements Specification Document (CLIN: 0002AA; title: Requirements Specification Document; file:
> Init8_BMS_RSD)
> System Design Document; file: BMS_SDD)

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## BMS Infrastructure Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The BMS application has a list of physical components that can be divided on more physical servers according with their roles.

> The following diagram represents a possible schema of physical deployment.

![](bed-management-solution-version-2-4-technical-manual/002.png)

> <span id="_bookmark6" class="anchor"></span>Figure 1-BMS Infrastructure Diagram

> BMS is divided into specific components:

1.  Persistence layer: SQL Server 2016 Enterprise database
2.  Application server layer: Windows Communication Foundation (WCF) Web Services installed as Windows Services
3.  Web server layer: Active Server Pages (ASP) .NET Model-View-Controller (MVC) Web application hosted in Internet Information Services (IIS)
4.  Data Exchange Servers:
    1.  National Utilization Management Integration (NUMI) SQL Server Database
    2.  VistA integration servers (servers that have access to VistA)
5.  Client Layer: Web Application client launched from browsers

## System Requirements (Hardware and Software)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS requires the creation of a Master Windows Service Account User and numerous facility/Site Service Account Users for execution and operations.

> All the BMS Application Services run under a service account.

- AITC has created the Windows User (acc\VAAACBMSPrd) as the master service account that the four BMS Services runs under. This can be referred to as the Master BMS Service Account.
- The \<SERVERADDRESS\>210 server hosts the three application services:
  - BMS.BedManagerService
  - BMS.SecurityHost
  - BMS.ServiceHost
- The \<ServerAddress\>211 server hosts the two application services:
  - BMS.VI.ServiceHost.
  - BMS.ServiceHost

> All BMS Facilities/Sites require at least one service account for certain site functionality.

- This service account will run the EMS Mobile Page and Whiteboard Kiosk Page functions.
- Under BMS version 1.xx a single service account can be used for both functions.
- The service account that runs the EMS Mobile Page and Whiteboard Kiosk Page functions must not have any Policies assigned that restrict its use to specific computers.

> BMS minimum hardware and software requirements are presented below:

> <span id="_bookmark8" class="anchor"></span>Table 1-Server for Web Applications

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Basic software:</p>
</blockquote></th>
<th><blockquote>
<p>Microsoft Windows Server 2012 64 bit R2 Standard Microsoft Clustering Services 2008</p>
<p>IIS 7.5 ASP.NET MVC5</p>
<p>.NET Framework 4.6.1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Application software:</p>
</blockquote></td>
<td><blockquote>
<p>Dashboards web application</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Processor(s):</p>
</blockquote></td>
<td><blockquote>
<p>16 x Intel Xeon E5520 or equivalent</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Memory:</p>
</blockquote></td>
<td><blockquote>
<p>32 GB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hard disks:</p>
</blockquote></td>
<td><blockquote>
<p>190 GB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Network controller:</p>
</blockquote></td>
<td><blockquote>
<p>Broadcom NetXtreme Gigabit Ethernet, or equivalent</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark9" class="anchor"></span>Table 2-Application Server

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Server 1</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Basic software:</strong></p>
</blockquote></td>
<td><blockquote>
<p>Microsoft Windows Server 2012 64 bit R2 Standard</p>
<p>.NET Framework 4.6.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Application software:</strong></p>
</blockquote></td>
<td><blockquote>
<p>EIS, EVS, DS, BMS InFlow</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Processor(s):</strong></p>
</blockquote></th>
<th><blockquote>
<p>14 x Intel Xeon E5520 or equivalent</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Memory:</strong></p>
</blockquote></td>
<td><blockquote>
<p>65 GB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Hard disks:</strong></p>
</blockquote></td>
<td><blockquote>
<p>190 GB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Network controller:</strong></p>
</blockquote></td>
<td><blockquote>
<p>Broadcom NetXtreme Gigabit Ethernet, or equivalent</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>Server 2</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Basic software:</strong></p>
</blockquote></td>
<td><blockquote>
<p>Microsoft Windows Server 2012 64 bit R2 Standard</p>
<p>.NET Framework 4.6.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Application software:</strong></p>
</blockquote></td>
<td><blockquote>
<p>EIS, EVS, DS, BMS InFlow</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Processor(s):</strong></p>
</blockquote></td>
<td><blockquote>
<p>12 x Intel Xeon E5520 or equivalent</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Memory:</strong></p>
</blockquote></td>
<td><blockquote>
<p>65 GB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Hard disks:</strong></p>
</blockquote></td>
<td><blockquote>
<p>210 GB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Network controller:</strong></p>
</blockquote></td>
<td><blockquote>
<p>Broadcom NetXtreme Gigabit Ethernet, or equivalent</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark10" class="anchor"></span>Table 3-Database Server

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Basic software:</strong></p>
</blockquote></th>
<th><blockquote>
<p>Microsoft Windows Server 2012 64 bit R2 Standard Microsoft SQL Server 2016 Enterprise</p>
<p>.NET Framework 4.6.1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Application software:</strong></p>
</blockquote></td>
<td><blockquote>
<p>Databases used by the services installed on APP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Processor(s):</strong></p>
</blockquote></td>
<td><blockquote>
<p>32 x Intel Xeon E5520 or equivalent</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Memory:</strong></p>
</blockquote></td>
<td><blockquote>
<p>136 GB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Hard disks:</strong></p>
</blockquote></td>
<td><blockquote>
<p>1500 GB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Network controller:</strong></p>
</blockquote></td>
<td><blockquote>
<p>Broadcom NetXtreme Gigabit Ethernet, or equivalent</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Configuration Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes configuration parameters of the BMS application.

> <span id="_bookmark12" class="anchor"></span>Table 4-BMS ServiceHost Configuration Parameters

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des</strong></p>
<p><strong>cript ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="4"><blockquote>
<p><strong>configSections</strong></p>
</blockquote></td>
<td><blockquote>
<p>mtmodules</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="ePractice.MiddleTier.MTModuleSectionHandler, MiddleTier"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>enterpriselibrary.configurat ionSettings</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="ePractice.Configuration.ConfigurationManagerSectionHandler, MS.Configuration"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pagingSortGroup</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="BMS.Utils.PagingSortSection, BMS.Utils" allowDefinition="Everywhere" allowExeDefinition="MachineToApplication" restartOnExternalChanges="true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>log4net</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Config.Log4NetConfigurationSectionHandler,log4net"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>connectionStrin gs</strong></p>
</blockquote></td>
<td><blockquote>
<p>Authorization</p>
</blockquote></td>
<td><blockquote>
<p>connectionString="Data Source=&lt;DatabaseAddress&gt;;Network Library=DBMSSOCN;Initial Catalog=BMS;Persist Security Info=False;Integrated Security=SSPI;Pooling=true;Min Pool Size=0;Max Pool Size=250;"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>connectionString="Data Source=&lt;DatabaseAddress&gt;</p>
<p>;Network Library=DBMSSOCN;Initial Catalog=BMS;Persist Security Info=False;Integrated Security=SSPI;Pooling=true; Min Pool Size=0;Max Pool Size=250;"</p>
</blockquote></td>
<td><blockquote>
<p>connectionString="Data Source=&lt;DatabaseAddres s&gt;;Initial Catalog=BMS;Persist Security Info=False;Integrated Security=SSPI;Pooling=tru e;Min Pool Size=0;Max Pool Size=100;"</p>
</blockquote></td>
<td><blockquote>
<p>Con necti on strin g for the conn ectio n to the BMS</p>
<p>data base</p>
<p>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5"><blockquote>
<p><strong>appSettings</strong></p>
</blockquote></td>
<td><blockquote>
<p>DatasetPath</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="DBRepository"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LocalServer</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="yes"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UseSecurityContext</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="1"</p>
</blockquote></td>
<td><blockquote>
<p>Secu rity - Auth oriza</p>
<p>tion</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ePractice.MiddleTier.Trans action</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="MiddleTier.dll"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ConnectionRef</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="1"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="5"></td>
<td><blockquote>
<p>TransactionProvider</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="ePractice.MiddleTier.CustomTransactionProvider"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaWorker.WorkerDelay TimeSpan</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="0:0:0:30"</p>
</blockquote></td>
<td><blockquote>
<p>Dela y time from servi ce start to first proc essin</p>
<p>g</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaWorker.WorkerPeriod TimeSpan</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="0:0:0:15"</p>
</blockquote></td>
<td><blockquote>
<p>Perio d betw een work er proc essin g</p>
<p>step s</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaWorker.BulkSize</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="100"</p>
</blockquote></td>
<td><blockquote>
<p>Maxi mum num ber of proc esse d entiti es in</p>
<p>one step</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaWorker.Enabled</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>N/A (No longer used)</p>
</blockquote></td>
<td><blockquote>
<p>Whet</p>
<p>her vista</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="4"></td>
<td></td>
<td colspan="4"></td>
<td><blockquote>
<p>work er is enab led or not (true or false</p>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration.Enabled</p>
</blockquote></td>
<td><blockquote>
<p>value="false"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="true"</p>
</blockquote></td>
<td><blockquote>
<p>value="true"</p>
</blockquote></td>
<td><blockquote>
<p>Whet her vista integ ratio n is enab led or not (true or false</p>
<p>)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration.Scheduler SecondsLate</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="30"</p>
</blockquote></td>
<td><blockquote>
<p>The time dela y of sche</p>
<p>duler s</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration.UpdateBm sPatients</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="true"</p>
</blockquote></td>
<td><blockquote>
<p>Whet her upda te bms patie</p>
<p>nts is enab</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="5"></td>
<td></td>
<td colspan="4"></td>
<td><blockquote>
<p>led or not (true or false</p>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SmtpHost</p>
</blockquote></td>
<td><blockquote>
<p>value="smtp.va.gov"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="smtp.va.gov"</p>
</blockquote></td>
<td><blockquote>
<p>value="localhost"</p>
</blockquote></td>
<td><blockquote>
<p>smtp host</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaWorker.VistASitesFile Path</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="VistASites.xml"</p>
</blockquote></td>
<td><blockquote>
<p>The vista sites confi gurat ion file nam</p>
<p>e</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistasBedHoldSupported</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>List of vista sites that supp ort bed</p>
<p>hold.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>visitorAppPwd</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="UM"</p>
</blockquote></td>
<td><blockquote>
<p>Pass word used by MD WS</p>
<p>to conn ect to VistA</p>
<p>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="39"></td>
<td><blockquote>
<p>visitorUserSiteCode</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="523"</p>
</blockquote></td>
<td><blockquote>
<p>User</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>Site</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>Cod</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>used</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>by</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>MD</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>WS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>conn</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>ect</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>to</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>VistA</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>visitorUserName</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt; visitorUserName &gt;</p>
</blockquote></td>
<td><blockquote>
<p>User</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>Nam</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>e</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>by</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>MD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>WS</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>to</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>conn</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>ect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>VistA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>visitorUserDuz</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="&lt;visitorUserDuz &gt;"</p>
</blockquote></td>
<td><blockquote>
<p>User</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>Duz</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>used</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>by</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>MD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>WS</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>to</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>conn</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>ect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>VistA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td><blockquote>
<p>visitorUserSsn</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="&lt;visitorUserSsn &gt;"</p>
</blockquote></td>
<td><blockquote>
<p>User SSN</p>
<p>used by MD WS</p>
<p>to conn ect to VistA</p>
<p>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>visitorContext</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="&lt;visitorContext &gt;"</p>
</blockquote></td>
<td><blockquote>
<p>Cont ext used by MD WS</p>
<p>to conn ect to VistA</p>
<p>.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UsingNewMdwsMethods</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="true"</p>
</blockquote></td>
<td><blockquote>
<p>Whet her use new mdw s meth ods for vista integ ratio n</p>
<p>(true or</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="4"></td>
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>false</p>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_EIS_GET_ENTITY_ FILTR_PAGE_SIZE</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="1000"</p>
</blockquote></td>
<td><blockquote>
<p>Num ber of recor ds queri ed that are brou ght from EIS</p>
<p>in one page</p>
<p>.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_EVS_GET_CONCE PT_PAGE_SIZE</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="1000"</p>
</blockquote></td>
<td><blockquote>
<p>Num ber of recor ds queri ed that are brou ght from EVS</p>
<p>in one page</p>
<p>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Changeset</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="72898"</p>
</blockquote></td>
<td><blockquote>
<p>Cha</p>
<p>nges et of</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="4"></td>
<td></td>
<td colspan="3"></td>
<td><blockquote>
<p>the instal led build</p>
<p>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NumiSvcAuthenticationKe y</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="&lt;NumiSvcAuthenticationKey &gt; "</p>
</blockquote></td>
<td><blockquote>
<p>NUM I</p>
<p>servi ce auth entic ation</p>
<p>key.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NumiMaxNumberOfSitesP erCall</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="5"</p>
</blockquote></td>
<td><blockquote>
<p>Maxi mum num ber of sites that NUM I</p>
<p>proc esse s in</p>
<p>one call.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Is_IIS_Single_Instance</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>value="true"</p>
</blockquote></td>
<td><blockquote>
<p>Whet her use SSL</p>
<p>endp oint from confi gurat ion</p>
<p>file. (true</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="4"></td>
<td></td>
<td colspan="4"></td>
<td><blockquote>
<p>or false</p>
<p>)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UseCacheEndpointFromC onfigWithSsl</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="true"</p>
</blockquote></td>
<td><blockquote>
<p>Whet her use SSL</p>
<p>endp oint from confi gurat ion</p>
<p>file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ProxyPoolMaxCount</p>
</blockquote></td>
<td><blockquote>
<p>value="1000"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="50"</p>
</blockquote></td>
<td><blockquote>
<p>value="1000"</p>
</blockquote></td>
<td><blockquote>
<p>The maxi mum num ber of proxi es in</p>
<p>the pool.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegrationJobFailed MaxCount</p>
</blockquote></td>
<td><blockquote>
<p>value="25"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>&lt;add key="MdwsEndpointUrl_DFL T"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>tt<a href="http://vaausbmsweb2/">p://vaausbms</a>w<a href="http://vaausbmsweb2/">eb2</a> 6:87/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_R1" valu<a href="http://vaausbmsweb2/">e="h</a>tt<a href="http://vaausbmsweb2/">p://vaausbms</a>w<a href="http://vaausbmsweb2/">eb2</a> 6:88/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_R2" valu<a href="http://vaausbmsweb2/">e="h</a>tt<a href="http://vaausbmsweb2/">p://vaausbms</a>w<a href="http://vaausbmsweb2/">eb2</a> 6:89/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_R3"</p>
</blockquote></td>
<td><blockquote>
<p>value="http://localhost:82/ QuerySvc.asmx" value="http://localhost:82/ QuerySvc.asmx"</p>
</blockquote></td>
<td><blockquote>
<p>MD WS</p>
<p>insta nce URL</p>
<p>addr ess.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>tt<a href="http://vaausbmsweb2/">p://vaausbms</a>w<a href="http://vaausbmsweb2/">eb2</a> 6:90/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_R4" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:91/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V1" valu<a href="http://vaausbmsweb2/">e="h</a>tt<a href="http://vaausbmsweb2/">p://vaausbms</a>w<a href="http://vaausbmsweb2/">eb2</a> 6:92/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V2" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:93/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V3" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:94/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V4" value="<a href="http://vaausbmsweb2/">http://vaausbmsweb2</a> 6:95/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V5" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:96/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V6" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:97/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V7" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:98/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V8" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:99/QuerySvc.asmx"/&gt;</p>
<p>&lt;add</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>key="MdwsEndpointUrl_V9" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:100/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V10" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:101/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V11" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:102/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V12" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:103/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V13" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:104/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V14" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:105/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V15" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:106/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V16" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:107/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V17" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:108/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V18" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a></p>
<p>6:109/QuerySvc.asmx"/&gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>&lt;add key="MdwsEndpointUrl_V19" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:110/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V20" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:111/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V21" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:112/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V22" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:113/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_V23" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:114/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_GLA "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:115/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_LAS "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:116/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_LOM "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:117/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_LON "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>6:118/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_SDC "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:119/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_KAN "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:120/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_STL "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:121/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_NFL "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:122/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_WP B"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:123/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_BAY "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:124/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_MIA" valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:125/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_ORL "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>6:126/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_SAJ "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:127/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_TAM "</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 6:128/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 1"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:87/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 2"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:88/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 3"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:89/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 4"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:90/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 5"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:91/QuerySvc.asmx"/&gt;</p>
<p>&lt;add</p>
<p>key="MdwsEndpointUrl_RSV 6"</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:92/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 7"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:93/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 8"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:94/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 9"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:95/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 10"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:96/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 11"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:97/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 12"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:98/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 13"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:99/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>14"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:100/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 14"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:101/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 15"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:102/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 16"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:103/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 17"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:104/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 18"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:105/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 19"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:106/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 20"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:107/QuerySvc.asmx"/&gt;</p>
<p>&lt;add</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>key="MdwsEndpointUrl_RSV 21"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:108/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 22"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:109/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 23"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:110/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 24"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:111/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 25"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:112/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 26"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:113/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_RSV 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:114/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_GLA 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:115/QuerySvc.asmx"/&gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>&lt;add key="MdwsEndpointUrl_LAS 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:116/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_LOM 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:117/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_LON 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:118/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_SDC 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:119/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_KAN 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:120/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_STL 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:121/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_NFL 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:122/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_WP B27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>7:123/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_BAY 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:124/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_MIA 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:125/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_ORL 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:126/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_SAJ 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:127/QuerySvc.asmx"/&gt;</p>
<p>&lt;add key="MdwsEndpointUrl_TAM 27"</p>
<p>valu<a href="http://vaausbmsweb2/">e="h</a>ttp<a href="http://vaausbmsweb2/">://vaausbmsweb2</a> 7:128/QuerySvc.asmx"/&gt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegrationJobFailedI ncrementDateMinutes</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="10"</p>
</blockquote></td>
<td><blockquote>
<p>The maxi mum num ber of job failur es until the syste</p>
<p>m</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td></td>
<td colspan="4"></td>
<td><blockquote>
<p>deci des to</p>
<p>retry.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegrationJobFailedN otificationEmailTo</p>
</blockquote></td>
<td colspan="4"></td>
<td><blockquote>
<p>The time span (min utes) that the syste m deci des to incre ment job's start date whe n the thres hold of job failur es is reac</p>
<p>hed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegrationJobFailedN otificationEmailFrom</p>
</blockquote></td>
<td><blockquote>
<p>value="BMSBackgroundProcessorAgent@ va.gov"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td><blockquote>
<p>Reci pient 's emai l used</p>
<p>whe n a</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="5"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td><blockquote>
<p>job fails. (va_ pers on@ va.g</p>
<p>ov)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_EIS_LongRunningM ethodsMaxConcurrentCall s</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="100"</p>
</blockquote></td>
<td><blockquote>
<p>Send er's emai l used whe n a job</p>
<p>fails.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_EVS_LongRunning</p>
<p>MethodsMaxConcurrentCa lls</p>
</blockquote></td>
<td><blockquote>
<p>value="100"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="75"</p>
</blockquote></td>
<td><blockquote>
<p>value="75"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMSServiceHostStartType</p>
</blockquote></td>
<td><blockquote>
<p>value="BMS"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="100"</p>
</blockquote></td>
<td><blockquote>
<p>value="50"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration.TaskSche dulerDelayMin</p>
</blockquote></td>
<td><blockquote>
<p>value="0"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="BMS.VI"</p>
</blockquote></td>
<td><blockquote>
<p>value="ALL"</p>
</blockquote></td>
<td><blockquote>
<p>Ident ifies how BMS</p>
<p>is ran and the assc oiate confi gurat ion file. (pos</p>
<p>sible valu</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="6"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td><blockquote>
<p>es: ALL, BMS</p>
<p>, BMS</p>
<p>.VI)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration.TaskSche dulerDelayMax</p>
</blockquote></td>
<td><blockquote>
<p>value="10"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="0"</p>
</blockquote></td>
<td><blockquote>
<p>value="0"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration.TaskSche</p>
<p>dulerDelayStep</p>
</blockquote></td>
<td><blockquote>
<p>value="5"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="10"</p>
</blockquote></td>
<td><blockquote>
<p>value="10"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ThreadPoolMaxWorkerThr eads</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>value="5"</p>
</blockquote></td>
<td><blockquote>
<p>value="5"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration.PatientMo vementIenDays</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>value="200"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ViaEndpointUrl</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>value="60"</p>
</blockquote></td>
<td><blockquote>
<p>value="60"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ViaRequestingApp</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>value="https://REDACTED.via. va.gov/via- webservices/services/Backgr</p>
<p>oundProcessService"</p>
</blockquote></td>
<td><blockquote>
<p>value="https://REDACTED.vi a.va.gov/via- webservices/services/Back</p>
<p>groundProcessService"</p>
</blockquote></td>
<td><blockquote>
<p><strong>URL</strong></p>
<p><strong>for VIA</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ViaAppToken</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>value="BMSBatch"</p>
</blockquote></td>
<td><blockquote>
<p>value="BMSBatch"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ViaAppPassword</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>value="BMSB_ID577"</p>
</blockquote></td>
<td><blockquote>
<p>value="BMSB_ID577"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MinimumFilemanDate</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>value="*"</p>
</blockquote></td>
<td><blockquote>
<p>Value="*"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Value="01/01/1992"</p>
</blockquote></td>
<td><blockquote>
<p>Value="01/01/1992"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>sortColumnCode="entered "</p>
</blockquote></td>
<td><blockquote>
<p>sortColumnName="[A].[CREATION_DATE] "</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="7"><blockquote>
<p><strong>pagingSortGrou p\pagingSort</strong></p>
</blockquote></td>
<td><blockquote>
<p>sortColumnCode="patient"</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>sortColumnName="[PAT].[LAST_NAME], [PAT].[FIRST_NAME]"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sortColumnCode="facility"</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>sortColumnName="[F].[NAME]"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>sortColumnCode="request dt"</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>sortColumnName="[A].[CREATION_DATE]"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sortColumnCode="specialt y"</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>sortColumnName="[REQSP].[DISPLAY_NAME]"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>sortColumnCode="visn"</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>sortColumnName="[TR].[FACILITY_VISN]</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sortColumnCode="region"</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>sortColumnName="[TR].[FACILITY_REGION]"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>sortColumnCode="eventdt</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>sortColumnName="[AEVN].[CREATION_DATE]"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="5"></td>
<td><blockquote>
<p>"</p>
</blockquote></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sortColumnCode="Vacate dDate"</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>sortColumnCode="VacatedDate"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>sortColumnCode="transfer eventdt"</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>sortColumnName="[A].[CREATION_DATE]"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sortColumnCode="transfer requestdt"</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>sortColumnName="[TR].[REQUESTED_DATE]"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>assembly="General.MT.dll "</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>servername=""</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p><strong>mtmodules [defaultserver=" "]</strong></p>
</blockquote></td>
<td><blockquote>
<p>assembly="BMS.MT.dll"</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>servername=""</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configurationSections\confi gurationSection xsi:type="ReadOnlyConfig urationSectionData" name="securityConfigurati</p>
<p>on" encrypt="false"</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>storageProvider xsi:type="XmlFileStorageProviderData" name="XML File Storage Provider" path="securityConfiguration.config"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>enterpriselibrar y.configuration Settings xmlns:xsd="htt p://<a href="http://www.w3.org/">www.w3.org/</a> 2001/XMLSche ma" xmlns:xsi="http</strong></p>
<p><strong>://<a href="http://www.w3.org/2">www.w3.org/2</a> 001/XMLSchem a-instance" applicationNam e="HMSI"</strong></p>
<p><strong>xmln<a href="http://w/">s="http://w</a> ww.microsoft.c om/practices/en</strong></p>
<p><strong>terpriselibrary/0</strong></p>
</blockquote></td>
<td><blockquote>
<p>configurationSections\confi gurationSection xsi:type="ReadOnlyConfig urationSectionData" name="securityConfigurati on" encrypt="false" configurationSections\confi gurationSection xsi:type="ReadOnlyConfig urationSectionData" name="cachingConfigurati on" encrypt="false"</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt;dataTransformer xsi:type="XmlSerializerTransformerData" name="Xml Serializer Transformer"&gt;</p>
<p>&lt;includeTypes&gt;</p>
<p>&lt;includeType name="HMUserAccessAuthenticationProviderData" type="ePractice.Security.HMUserAccess.Configuration.HMUserAccessAuthenticationProviderData, Security.HMUserAccess"/&gt;</p>
<p>&lt;includeType name="HMUserAccessAuthorizationProviderData" type="ePractice.Security.HMUserAccess.Configuration.HMUserAccessAuthorizationProviderData, Security.HMUserAccess"/&gt;</p>
<p>&lt;includeType name="HMUserAccessRolesProviderData" type="ePractice.Security.HMUserAccess.Configuration.HMUserAccessRolesProviderData, Security.HMUserAccess"/&gt;</p>
<p>&lt;includeType name="NullAuthenticationProviderData" type="ePractice.Security.Null.Configuration.NullAuthenticationProviderData, Security.Null"/&gt;</p>
<p>&lt;includeType name="NullAuthorizationProviderData" type="ePractice.Security.Null.Configuration.NullAuthorizationProviderData, Security.Null"/&gt;</p>
<p>&lt;/includeTypes&gt;</p>
<p>&lt;/dataTransformer&gt;</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p><strong>8-31-</strong></p>
<p><strong>2004/configurati on"</strong></p>
</blockquote></td>
<td></td>
<td colspan="3"><blockquote>
<p>storageProvider xsi:type="XmlFileStorageProviderData" name="XML File Storage Provider" path="cachingConfiguration.config"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>configurationSections\confi gurationSection xsi:type="ReadOnlyConfig urationSectionData" name="cachingConfigurati on" encrypt="false" configurationSections\confi gurationSection xsi:type="ReadOnlyConfig urationSectionData" name="connectionConfigu</p>
<p>ration" encrypt="false"</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>&lt;dataTransformer xsi:type="XmlSerializerTransformerData" name="Xml Serializer Transformer"&gt;</p>
<p>&lt;includeTypes/&gt;</p>
<p>&lt;/dataTransformer&gt;</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Cach ing confi gurat ion is for CLIE NT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>storageProvider xsi:type="XmlFileStorageProviderData" name="XML File Storage Provider" path="connectionConfiguration.config"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td rowspan="2"><blockquote>
<p>configurationSections\confi gurationSection xsi:type="ReadOnlyConfig urationSectionData" name="connectionConfigu ration" encrypt="false" keyAlgorithmStorageProvi der</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>&lt;dataTransformer xsi:type="XmlSerializerTransformerData" name="Xml Serializer Transformer"&gt;</p>
<p>&lt;includeTypes&gt;</p>
<p>&lt;includeType name="ServicesDatabaseConnectionProviderData" type="ePractice.Connection.SingleDatabase.Configuration.ServicesDatabaseConnectionProviderData, Connections.SingleDatabase, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"/&gt;</p>
<p>&lt;/includeTypes&gt;</p>
<p>&lt;/dataTransformer&gt;</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Con necti on confi gurat ion is for SER VER</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>xsi:nil="true"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>application\channels\chan nel</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="System.Runtime.Remoting.Channels.Tcp.TcpChannel, System.Runtime.Remoting, Version=1.0.5000.0, Culture=neutral, PublicKeyToken=b77a5c561934e089" name="RegularChannel"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>system.runtime. remoting</strong></p>
</blockquote></td>
<td><blockquote>
<p>connectionManagement\a dd</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>address="*" maxconnection="1000"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>system.net</strong></p>
</blockquote></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>name="BMS.ServiceImplementation.BedManagerOperationsCore" behaviorConfiguration="ServiceBehavior"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>system.service Model\services</strong></p>
</blockquote></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>baseAddress="http://&lt;ServerAddress&gt;25:16050/BMSOperations"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address="" bindingConfiguration="ServiceBinding" binding="wsFederationHttpBinding" contract="BMS.ServiceContracts.IBedMan</p>
<p>agerOperations"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>baseAddress="http://&lt;Server Address&gt;211:16050/BMSOp erations"</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress="http://localh ost:16050/BMSOperations"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>address="win" bindingConfiguration="WinBinding" binding="wsFederationHttpBinding" contract="BMS.ServiceContracts.IBedManagerOperations"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>contract="IMetadataExchange" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.ServiceContracts.IBedManagerOperations"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>name="BMS.ServiceImplementation.BedManagerQueryCore" behaviorConfiguration="ServiceBehavior"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>baseAddress="http://&lt;ServerAddress&gt;210:16050/BMSQuery"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address="" bindingConfiguration="ServiceBinding" binding="wsFederationHttpBinding"</p>
<p>contract="BMS.ServiceContracts.IBedMan agerQuery"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>baseAddress="http://&lt;Server Address&gt;211:16050/BMSQu ery"</p>
</blockquote></td>
<td><blockquote>
<p>baseAddr<a href="http://localh/">ess="h</a>tt<a href="http://localh/">p://</a>lo<a href="http://localh/">cal</a>h ost:16050/BMSQuery"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>address="win" bindingConfiguration="WinBinding" binding="wsFederationHttpBinding" contract="BMS.ServiceContracts.IBedManagerQuery"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>contract="IMetadataExchange" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.ServiceContracts.IBedManagerQuery"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>name="BMS.ServiceImplementation.BedManagerCacheCore" behaviorConfiguration="ServiceBehavior"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>baseAddress="http://&lt;Server Address&gt;211:16050/BMSCa</p>
<p>che"</p>
</blockquote></td>
<td><blockquote>
<p>baseAddr<a href="http://localh/">ess="h</a>tt<a href="http://localh/">p://</a>lo<a href="http://localh/">cal</a>h ost:16050/BMSCache"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="" bindingConfiguration="Servic eBinding" binding="wsFederationHttpBi nding" contract="BMS.ServiceContr acts.IBedManagerCache"</p>
</blockquote></td>
<td><blockquote>
<p>address="" bindingConfiguration="Serv iceBinding" binding="wsFederationHttp Binding" contract="BMS.ServiceCon tracts.IBedManagerCache"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="win" bindingConfiguration="WinBi nding" binding="wsFederationHttpBi nding" contract="BMS.ServiceContr acts.IBedManagerCache"</p>
</blockquote></td>
<td><blockquote>
<p>address="win" bindingConfiguration="Win Binding" binding="wsFederationHttp Binding" contract="BMS.ServiceCon tracts.IBedManagerCache"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>contract="IMetadataExchang e" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td><blockquote>
<p>contract="IMetadataExcha nge" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td><blockquote>
<p>name="BMS.ServiceImplementation.Config urationOperationsCore" behaviorConfiguration="ServiceBehavior"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.ServiceContr acts.IBedManagerCache"</p>
</blockquote></td>
<td><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.ServiceCon tracts.IBedManagerCache"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress="http://&lt;ServerAddress&gt;210: 16050/BMSConfigurationOperations"</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>name="BMS.ServiceImple mentation.ConfigurationOp erationsCore" behaviorConfiguration="Se rviceBehavior"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address="" bindingConfiguration="ServiceBinding" binding="wsFederationHttpBinding" contract="BMS.ServiceContracts.IConfigur</p>
<p>ationOperations"</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>baseAddr<a href="http://localh/">ess="h</a>tt<a href="http://localh/">p://</a>lo<a href="http://localh/">cal</a>h ost:16050/BMSConfigurati onOperations"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address="win" bindingConfiguration="WinBinding" binding="wsFederationHttpBinding" contract="BMS.ServiceContracts.IConfigur ationOperations"</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>address="" bindingConfiguration="Serv iceBinding" binding="wsFederationHttp Binding" contract="BMS.ServiceCon tracts.IConfigurationOperat ions"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td><blockquote>
<p>contract="IMetadataExchange" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>address="win" bindingConfiguration="Win Binding" binding="wsFederationHttp Binding" contract="BMS.ServiceCon tracts.IConfigurationOperat ions"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.ServiceContracts.IConfigur ationOperations"</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>contract="IMetadataExcha nge" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td><blockquote>
<p>name="InfoWorld.Security.Authorization.Au thorizationSubscriber.AuthorizationSubscri ber" behaviorConfiguration="ServiceBehavior"</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.ServiceCon tracts.IConfigurationOperat ions"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress="http://&lt;ServerAddress&gt;210: 16050/BMS/AuthorizationSubscriber"</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>name="InfoWorld.Security. Authorization.Authorization Subscriber.AuthorizationSu bscriber" behaviorConfiguration="Se rviceBehavior"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address="" binding="wsFederationHttpBinding" bindingConfiguration="WinBinding" contract="InfoWorld.Security.Authorization.</p>
<p>AuthorizationSubscriber.IAuthorizationSub scriber"</p>
</blockquote></td>
<td colspan="2"></td>
<td><blockquote>
<p>baseAddr<a href="http://localh/">ess="h</a>tt<a href="http://localh/">p://</a>lo<a href="http://localh/">cal</a>h ost:16050/BMS/Authorizati onSubscriber"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>address="" binding="wsFederationHttp Binding" bindingConfiguration="Win Binding" contract="InfoWorld.Securit y.Authorization.Authorizati onSubscriber.IAuthorizatio nSubscriber"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="TransferFlow" behaviorConfiguration="Work flowService"</p>
</blockquote></td>
<td><blockquote>
<p>name="TransferFlow" behaviorConfiguration="W orkflowService"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>baseAddress="http://&lt;Server Address&gt;211:16050/Transfer</p>
<p>WF"</p>
</blockquote></td>
<td><blockquote>
<p>baseAddr<a href="http://localh/">ess="h</a>tt<a href="http://localh/">p://</a>lo<a href="http://localh/">cal</a>h ost:16050/TransferWF"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="" bindingConfiguration="Servic eBinding" binding="wsFederationHttpBi nding" contract="BMS.Workflows.W F.ITransferFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="" bindingConfiguration="Serv iceBinding" binding="wsFederationHttp Binding" contract="BMS.Workflows. WF.ITransferFlow"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="win" bindingConfiguration="WinBi nding" binding="wsFederationHttpBi nding" contract="BMS.Workflows.W F.ITransferFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="win" bindingConfiguration="Win Binding" binding="wsFederationHttp Binding" contract="BMS.Workflows. WF.ITransferFlow"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>contract="IMetadataExchang e" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td><blockquote>
<p>contract="IMetadataExcha nge" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.Workflows.W F.ITransferFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.Workflows. WF.ITransferFlow"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="WaitingListFlow" behaviorConfiguration="Work flowService"</p>
</blockquote></td>
<td><blockquote>
<p>name="WaitingListFlow" behaviorConfiguration="W orkflowService"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>baseAddress="http://&lt;Server Address&gt;211:16050/Waiting</p>
<p>ListWF"</p>
</blockquote></td>
<td><blockquote>
<p>baseAddr<a href="http://localh/">ess="h</a>tt<a href="http://localh/">p://</a>lo<a href="http://localh/">cal</a>h ost:16050/WaitingListWF"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="" bindingConfiguration="Servic eBinding" binding="wsFederationHttpBi nding" contract="BMS.Workflows.W F.IWaitingListFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="" bindingConfiguration="Serv iceBinding" binding="wsFederationHttp Binding" contract="BMS.Workflows. WF.IWaitingListFlow"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="win" bindingConfiguration="WinBi nding" binding="wsFederationHttpBi nding" contract="BMS.Workflows.W F.IWaitingListFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="win" bindingConfiguration="Win Binding" binding="wsFederationHttp Binding" contract="BMS.Workflows. WF.IWaitingListFlow"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>contract="IMetadataExchang e" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td><blockquote>
<p>contract="IMetadataExcha nge" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.Workflows.W F.IWaitingListFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.Workflows. WF.IWaitingListFlow"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="BedUnavailableFlow" behaviorConfiguration="Work flowService"</p>
</blockquote></td>
<td><blockquote>
<p>name="BedUnavailableFlo w" behaviorConfiguration="W orkflowService"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>baseAddress="http://&lt;Server Address&gt;211:16050/BedUna vailableWF"</p>
</blockquote></td>
<td><blockquote>
<p>name="BedUnavailableFlo w" behaviorConfiguration="W orkflowService"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="" bindingConfiguration="Servic eBinding" binding="wsFederationHttpBi nding" contract="BMS.Workflows.W F.IBedUnavailableFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="" bindingConfiguration="Serv iceBinding" binding="wsFederationHttp Binding" contract="BMS.Workflows. WF.IBedUnavailableFlow"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="win" bindingConfiguration="WinBi nding" binding="wsFederationHttpBi nding" contract="BMS.Workflows.W F.IBedUnavailableFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="win" bindingConfiguration="Win Binding" binding="wsFederationHttp Binding" contract="BMS.Workflows. WF.IBedUnavailableFlow"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>contract="IMetadataExchang e" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td><blockquote>
<p>contract="IMetadataExcha nge" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.Workflows.W F.IBedUnavailableFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.Workflows. WF.IBedUnavailableFlow"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="BMS.ServiceImpleme ntation.VistaQueryCore" behaviorConfiguration="Servi ceBehavior"</p>
</blockquote></td>
<td><blockquote>
<p>name="BMS.ServiceImple mentation.VistaQueryCore" behaviorConfiguration="Se rviceBehavior"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>baseAddress="http://&lt;Server Address&gt;211:16050/VistaQu</p>
<p>ery"</p>
</blockquote></td>
<td><blockquote>
<p>baseAddr<a href="http://localh/">ess="h</a>tt<a href="http://localh/">p://</a>lo<a href="http://localh/">cal</a>h ost:16050/VistaQuery"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="" bindingConfiguration="Servic eBinding" binding="wsFederationHttpBi nding" contract="BMS.ServiceContr acts.IVistaWorkerQuery"</p>
</blockquote></td>
<td><blockquote>
<p>address="" bindingConfiguration="Serv iceBinding" binding="wsFederationHttp Binding" contract="BMS.ServiceCon tracts.IVistaWorkerQuery"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="win" bindingConfiguration="WinBi nding" binding="wsFederationHttpBi nding" contract="BMS.ServiceContr acts.IVistaWorkerQuery"</p>
</blockquote></td>
<td><blockquote>
<p>address="win" bindingConfiguration="Win Binding" binding="wsFederationHttp Binding" contract="BMS.ServiceCon tracts.IVistaWorkerQuery"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>contract="IMetadataExchang e" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td><blockquote>
<p>contract="IMetadataExcha nge" binding="mexHttpBinding" address="mex"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>service</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.ServiceContr acts.IVistaWorkerQuery"</p>
</blockquote></td>
<td><blockquote>
<p>address="unsec" binding="basicHttpBinding" contract="BMS.ServiceCon tracts.IVistaWorkerQuery"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>host\base\baseAddresses\ add</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="BMS.VistaIntegration</p>
<p>.HL7.ServiceImplementation. HL7OperationsCore" behaviorConfiguration="Basi cBindingBehavior"</p>
</blockquote></td>
<td><blockquote>
<p>name="BMS.VistaIntegrati on.HL7.ServiceImplementa tion.HL7OperationsCore" behaviorConfiguration="Ba sicBindingBehavior"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>baseAddress="http://&lt;Server Address&gt;211:16050/HL7Ope</p>
<p>rations"</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress="http://localh ost:16050/HL7Operations"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>bindings\basicHttpBinding</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="" bindingConfiguration="messa gingBinding" binding="basicHttpBinding" contract="BMS.VistaIntegrati on.HL7.ServiceContracts.IHL 7Operations"</p>
</blockquote></td>
<td><blockquote>
<p>address="" bindingConfiguration="mes sagingBinding" binding="basicHttpBinding" contract="BMS.VistaIntegr ation.HL7.ServiceContract s.IHL7Operations"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="EVSBinding" maxReceivedMessageSize=" 2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td><blockquote>
<p>name="EVSBinding" maxReceivedMessageSize</p>
<p>="2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="subscriptionBinding" maxBufferSize="2147483647 "</p>
<p>maxReceivedMessageSize=" 2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td><blockquote>
<p>name="subscriptionBinding "</p>
<p>maxBufferSize="21474836 47"</p>
<p>maxReceivedMessageSize</p>
<p>="2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>readerQuotas</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="messagingBinding" maxBufferSize="2147483647 "</p>
<p>maxReceivedMessageSize=" 2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td><blockquote>
<p>name="messagingBinding" maxBufferSize="21474836 47"</p>
<p>maxReceivedMessageSize</p>
<p>="2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>maxDepth="2147483647" maxStringContentLength="2 147483647"</p>
<p>maxArrayLength="21474836 47"</p>
<p>maxBytesPerRead="214748 3647"</p>
<p>maxNameTableCharCount=" 2147483647"</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="2147483647" maxStringContentLength=" 2147483647"</p>
<p>maxArrayLength="2147483 647"</p>
<p>maxBytesPerRead="21474 83647"</p>
<p>maxNameTableCharCount</p>
<p>="2147483647"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>readerQuotas</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="QuerySvcSoap" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00" allowCookies="false"</p>
<p>bypassProxyOnLocal="false" hostNameComparisonMode= "StrongWildcard"</p>
<p>maxBufferSize="2147483647 "</p>
<p>maxReceivedMessageSize=" 2147483647"</p>
<p>messageEncoding="Text" textEncoding="utf-8" transferMode="Buffered"</p>
<p>useDefaultWebProxy="true"</p>
</blockquote></td>
<td><blockquote>
<p>name="QuerySvcSoap" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00" allowCookies="false"</p>
<p>bypassProxyOnLocal="fals e" hostNameComparisonMod e="StrongWildcard"</p>
<p>maxBufferSize="21474836 47"</p>
<p>maxReceivedMessageSize</p>
<p>="2147483647"</p>
<p>messageEncoding="Text" textEncoding="utf-8" transferMode="Buffered"</p>
<p>useDefaultWebProxy="true "</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>security mode="None"</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>maxDepth="32" maxStringContentLength="2 147483647"</p>
<p>maxArrayLength="21474836 47"</p>
<p>maxBytesPerRead="214748 3647"</p>
<p>maxNameTableCharCount=" 2147483647"</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="32" maxStringContentLength=" 2147483647"</p>
<p>maxArrayLength="2147483 647"</p>
<p>maxBytesPerRead="21474 83647"</p>
<p>maxNameTableCharCount</p>
<p>="2147483647"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>transport</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>message</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>clientCredentialType="None" proxyCredentialType="None" realm=""</p>
</blockquote></td>
<td><blockquote>
<p>clientCredentialType="Non e" proxyCredentialType="Non e"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>realm=""</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>clientCredentialType="UserN</p>
<p>ame" algorithmSuite="Default"</p>
</blockquote></td>
<td><blockquote>
<p>clientCredentialType="User</p>
<p>Name" algorithmSuite="Default"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>readerQuotas</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="QuerySvcSoapHttps" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00" allowCookies="false"</p>
<p>bypassProxyOnLocal="false" hostNameComparisonMode= "StrongWildcard" maxBufferSize="2147483647 "</p>
<p>maxReceivedMessageSize=" 2147483647"</p>
<p>messageEncoding="Text" textEncoding="utf-8" transferMode="Buffered" useDefaultWebProxy="true"</p>
</blockquote></td>
<td><blockquote>
<p>name="QuerySvcSoapHttp s" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00" allowCookies="false"</p>
<p>bypassProxyOnLocal="fals e" hostNameComparisonMod e="StrongWildcard" maxBufferSize="21474836 47"</p>
<p>maxReceivedMessageSize</p>
<p>="2147483647"</p>
<p>messageEncoding="Text" textEncoding="utf-8" transferMode="Buffered" useDefaultWebProxy="true "</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>security mode="Transport"</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>maxDepth="32" maxStringContentLength="2 147483647"</p>
<p>maxArrayLength="21474836 47"</p>
<p>maxBytesPerRead="214748 3647"</p>
<p>maxNameTableCharCount=" 2147483647"</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="32" maxStringContentLength=" 2147483647"</p>
<p>maxArrayLength="2147483 647"</p>
<p>maxBytesPerRead="21474 83647"</p>
<p>maxNameTableCharCount</p>
<p>="2147483647"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>transport</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>wsFederationHttpBinding</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>clientCredentialType="None" proxyCredentialType="None" realm=""</p>
</blockquote></td>
<td><blockquote>
<p>clientCredentialType="Non e" proxyCredentialType="Non e" realm=""</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>readerQuotas</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>name="WSFederationHttpBi nding_AuthenticatedService" maxReceivedMessageSize=" 2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td><blockquote>
<p>name="WSFederationHttp Binding_AuthenticatedServ ice" maxReceivedMessageSize</p>
<p>="2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>security mode="Message"</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>maxDepth="32" maxStringContentLength="2 147483647"</p>
<p>maxArrayLength="21474836 47"</p>
<p>maxBytesPerRead="4096" maxNameTableCharCount="</p>
<p>16384"</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="32" maxStringContentLength=" 2147483647"</p>
<p>maxArrayLength="2147483 647"</p>
<p>maxBytesPerRead="4096" maxNameTableCharCount</p>
<p>="16384"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>message</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>issuer</p>
</blockquote></td>
<td><blockquote>
<p>address="http://&lt;ServerAddress&gt;210:1605 0/STS/mex"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>algorithmSuite="Default" issuedKeyType="Symmetric Key" issuedTokenType="http://doc s.oasis-open.org/wss/oasis- wss-saml-token-profile- 1.1#SAMLV2.0"</p>
<p>negotiateServiceCredential=" false" establishSecurityContext="tr ue"</p>
</blockquote></td>
<td><blockquote>
<p>algorithmSuite="Default" issuedKeyType="Symmetri cKey" issuedTokenType="http://d ocs.oasis- open.org/wss/oasis-wss- saml-token-profile- 1.1#SAMLV2.0"</p>
<p>negotiateServiceCredential</p>
<p>="false"</p>
<p>establishSecurityContext=" true"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>address="http://&lt;ServerAddr ess&gt;210:16050/STS/"</p>
<p>binding="wsHttpBinding" bindingConfiguration="wsUs erName"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/STS/"</p>
<p>binding="wsHttpBinding" bindingConfiguration="wsU serName"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td><blockquote>
<p>name="ServiceBinding" maxBufferPoolSize="2147483647" maxReceivedMessageSize="2147483647" closeTimeout="00:10:00" openTimeout="00:10:00"</p>
<p>receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="IWHM3STS"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3STS"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>readerQuotas</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="32" maxStringContentLength="2147483647" maxArrayLength="2147483647" maxBytesPerRead="4096" maxNameTableCharCount="16384"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>name="ServiceBinding" maxBufferPoolSize="214748 3647"</p>
<p>maxReceivedMessageSize=" 2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td><blockquote>
<p>name="ServiceBinding" maxBufferPoolSize="2147 483647"</p>
<p>maxReceivedMessageSize</p>
<p>="2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>security mode="Message"</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>maxDepth="32" maxStringContentLength="2 147483647"</p>
<p>maxArrayLength="21474836 47"</p>
<p>maxBytesPerRead="4096" maxNameTableCharCount="</p>
<p>16384"</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="32" maxStringContentLength=" 2147483647"</p>
<p>maxArrayLength="2147483 647"</p>
<p>maxBytesPerRead="4096" maxNameTableCharCount</p>
<p>="16384"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>message issuedTokenType="http://d ocs.oasis- open.org/wss/oasis-wss- saml-token-profile- 1.1#SAMLV2.0"</p>
<p>negotiateServiceCredential</p>
<p>="false"</p>
</blockquote></td>
<td><blockquote>
<p>issuerMetadata address="http://&lt;ServerAddress&gt;210:1605 0/STS/mex"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>establishSecurityContext=" true"</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td><blockquote>
<p>name="WinBinding" maxBufferPoolSize="2147483647" maxReceivedMessageSize="2147483647" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>issuerMetadata address="http://&lt;ServerAddr ess&gt;210:16050/STS/mex"</p>
</blockquote></td>
<td><blockquote>
<p>issuerMetadata address="http://localhost:1 6050/STS/mex"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>readerQuotas</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="32" maxStringContentLength="2147483647" maxArrayLength="2147483647" maxBytesPerRead="4096" maxNameTableCharCount="16384"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>name="WinBinding" maxBufferPoolSize="214748 3647"</p>
<p>maxReceivedMessageSize=" 2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td><blockquote>
<p>name="WinBinding" maxBufferPoolSize="2147 483647"</p>
<p>maxReceivedMessageSize</p>
<p>="2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>security mode="Message"</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>maxDepth="32" maxStringContentLength="2 147483647"</p>
<p>maxArrayLength="21474836 47"</p>
<p>maxBytesPerRead="4096"</p>
<p>maxNameTableCharCount=" 16384"</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="32" maxStringContentLength=" 2147483647"</p>
<p>maxArrayLength="2147483 647"</p>
<p>maxBytesPerRead="4096" maxNameTableCharCount</p>
<p>="16384"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>message</p>
</blockquote></td>
<td><blockquote>
<p>issuedTokenType="http://docs<a href="http://docs.oasis-/">.oasis-</a> open.org/wss/oasis-wss-saml-token-profile- 1.1#SAMLV2.0"</p>
<p>negotiateServiceCredential="false" establishSecurityContext="true"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>issuer</p>
</blockquote></td>
<td><blockquote>
<p>address="http://&lt;ServerAddress&gt;210:1605 0/STS/Windows" binding="wsHttpBinding" bindingConfiguration="StsWinBinding"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>issuedTokenType="http://doc s.oasis-open.org/wss/oasis- wss-saml-token-profile- 1.1#SAMLV2.0"</p>
<p>negotiateServiceCredential=" false" establishSecurityContext="tr ue"</p>
</blockquote></td>
<td><blockquote>
<p>issuedTokenType="http://d ocs.oasis- open.org/wss/oasis-wss- saml-token-profile- 1.1#SAMLV2.0"</p>
<p>negotiateServiceCredential</p>
<p>="false" establishSecurityContext="</p>
<p>true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>identity\servicePrincipalNa me</p>
</blockquote></td>
<td><blockquote>
<p>value="host/localhost"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>address="http://&lt;ServerAddr ess&gt;210:16050/STS/Window s" binding="wsHttpBinding" bindingConfiguration="StsWi nBinding"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/STS/Windows" binding="wsHttpBinding" bindingConfiguration="Sts WinBinding"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td><blockquote>
<p>name="WinBindingHttps" maxBufferPoolSize="2147483647" maxReceivedMessageSize="2147483647" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00"</p>
<p>sendTimeout="00:10:00"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="host/localhost"</p>
</blockquote></td>
<td><blockquote>
<p>value="host/localhost"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>readerQuotas</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="32" maxStringContentLength="2147483647" maxArrayLength="2147483647" maxBytesPerRead="4096" maxNameTableCharCount="16384"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>name="WinBindingHttps" maxBufferPoolSize="214748 3647"</p>
<p>maxReceivedMessageSize=" 2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td><blockquote>
<p>name="WinBindingHttps" maxBufferPoolSize="2147 483647"</p>
<p>maxReceivedMessageSize</p>
<p>="2147483647"</p>
<p>closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>security mode="TransportWithMes sageCredential"</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>maxDepth="32" maxStringContentLength="2 147483647"</p>
<p>maxArrayLength="21474836 47"</p>
<p>maxBytesPerRead="4096"</p>
<p>maxNameTableCharCount=" 16384"</p>
</blockquote></td>
<td><blockquote>
<p>maxDepth="32" maxStringContentLength=" 2147483647"</p>
<p>maxArrayLength="2147483 647"</p>
<p>maxBytesPerRead="4096" maxNameTableCharCount</p>
<p>="16384"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>message</p>
</blockquote></td>
<td><blockquote>
<p>issuedTokenType="http://docs<a href="http://docs.oasis-/">.oasis-</a> open.org/wss/oasis-wss-saml-token-profile- 1.1#SAMLV2.0"</p>
<p>negotiateServiceCredential="false" establishSecurityContext="true"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>issuer</p>
</blockquote></td>
<td><blockquote>
<p>address="http://&lt;ServerAddress&gt;210:1605 0/STS/Windows" binding="wsHttpBinding" bindingConfiguration="StsWinBinding"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>issuedTokenType="http://doc s.oasis-open.org/wss/oasis- wss-saml-token-profile- 1.1#SAMLV2.0"</p>
<p>negotiateServiceCredential=" false" establishSecurityContext="tr ue"</p>
</blockquote></td>
<td><blockquote>
<p>issuedTokenType="http://d ocs.oasis- open.org/wss/oasis-wss- saml-token-profile- 1.1#SAMLV2.0"</p>
<p>negotiateServiceCredential</p>
<p>="false" establishSecurityContext="</p>
<p>true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>identity\servicePrincipalNa me</p>
</blockquote></td>
<td><blockquote>
<p>value="host/localhost"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>address="http://&lt;ServerAddr ess&gt;210:16050/STS/Window s" binding="wsHttpBinding" bindingConfiguration="StsWi nBinding"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/STS/Windows" binding="wsHttpBinding" bindingConfiguration="Sts WinBinding"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>wsHttpBinding</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>value="host/localhost"</p>
</blockquote></td>
<td><blockquote>
<p>value="host/localhost"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td><blockquote>
<p>name="wsUserName" maxReceivedMessageSize="2147483647" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00"</p>
<p>sendTimeout="00:10:00"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>security mode="Message"</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>message</p>
</blockquote></td>
<td><blockquote>
<p>clientCredentialType="UserName" negotiateServiceCredential="false" algorithmSuite="Default"</p>
<p>establishSecurityContext="true"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>name="StsWinBinding" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>security mode="Message"</p>
</blockquote></td>
<td colspan="4"></td>
<td><blockquote>
<p>Kerb eros/ NTL</p>
<p>M</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>message</p>
</blockquote></td>
<td><blockquote>
<p>clientCredentialType="UserName" negotiateServiceCredential="false"</p>
<p>algorithmSuite="Default" establishSecurityContext="true"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td><blockquote>
<p>name="StsWinBinding" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>clientCredentialType="UserN ame" negotiateServiceCredential=" false" algorithmSuite="Default"</p>
<p>establishSecurityContext="tr ue"</p>
</blockquote></td>
<td><blockquote>
<p>clientCredentialType="User Name" negotiateServiceCredential</p>
<p>="false" algorithmSuite="Default" establishSecurityContext="</p>
<p>true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>security mode="Message"</p>
</blockquote></td>
<td><blockquote>
<p>name="StsWinBinding" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>name="StsWinBinding" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td><blockquote>
<p>name="StsWinBinding" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>message</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>clientCredentialType="Windows" negotiateServiceCredential="true" establishSecurityContext="true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>binding</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>name="wsBindConf" maxReceivedMessageSize="2147483647" closeTimeout="00:10:00" openTimeout="00:10:00" receiveTimeout="00:15:00" sendTimeout="00:10:00"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>client</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>addr<a href="http://vaausbms/">ess="h</a>tt<a href="http://vaausbms/">p://</a>vaa<a href="http://vaausbms/">usbms</a> web26:87/QuerySvc.asmx" binding="basicHttpBinding"</p>
<p>bindingConfiguration="Que rySvcSoap" contract="QuerySvcServic e.QuerySvcSoap"</p>
<p>name="QuerySvcSoap"</p>
</blockquote></td>
<td><blockquote>
<p>addr<a href="http://vaausbms/">ess="h</a>tt<a href="http://vaausbms/">p://</a>vaa<a href="http://vaausbms/">usbms</a> web76/mdws2/QuerySvc.a smx" binding="basicHttpBinding"</p>
<p>bindingConfiguration="Que rySvcSoap" contract="QuerySvcServic e.QuerySvcSoap"</p>
<p>name="QuerySvcSoap"</p>
</blockquote></td>
<td><blockquote>
<p>MD WS2</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="https://vaausnum web22.aac.dva.va.gov/Inp atient.asmx" binding="basicHttpBinding"</p>
<p>bindingConfiguration="Que rySvcSoapHttps" contract="BMS.ServicesWr apper.Proxy.InpatientSoap "</p>
<p>name="InpatientSoap"</p>
</blockquote></td>
<td><blockquote>
<p>address="https://hceveah0 3:100/Inpatient.asmx" binding="basicHttpBinding"</p>
<p>bindingConfiguration="Que rySvcSoapHttps" contract="BMS.ServicesWr apper.Proxy.InpatientSoap "</p>
<p>name="InpatientSoap"</p>
</blockquote></td>
<td><blockquote>
<p>NUM I</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;210:16050/PAP"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>contract="InfoWorld.Securit y.Authorization.PolicyAdmi nistrationPoint.IAdministrati veFunctions"</p>
<p>name="PAP.Administrative Functions"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/PAP"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>contract="InfoWorld.Securit y.Authorization.PolicyAdmi nistrationPoint.IAdministrati veFunctions"</p>
<p>name="PAP.Administrative Functions"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>PAP</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>endpoint address="http://&lt;ServerAd dress&gt;210:16050/PDP"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>contract="InfoWorld.Securit y.PolicyDecisionPoint.IAut horizationService"</p>
<p>name="PDP.Authorization Service"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/PDP"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>contract="InfoWorld.Securit y.PolicyDecisionPoint.IAut horizationService"</p>
<p>name="PDP.Authorization Service"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>PDP</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;210:16050/PAP"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="InfoWorld.Securit y.Authorization.PolicyAdmi nistrationPoint.IAdministrati veFunctions"</p>
<p>name="PAP.Administrative Functions.Windows"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/PAP"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="InfoWorld.Securit y.Authorization.PolicyAdmi nistrationPoint.IAdministrati veFunctions"</p>
<p>name="PAP.Administrative Functions.Windows"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>PAP:</p>
<p>Wind ows auth entic ation</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;210:16050/PDP"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="InfoWorld.Securit y.PolicyDecisionPoint.IAut horizationService"</p>
<p>name="PDP.Authorization Service.Windows"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/PDP"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="InfoWorld.Securit y.PolicyDecisionPoint.IAut horizationService"</p>
<p>name="PDP.Authorization Service.Windows"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>PDP:</p>
<p>Wind ows auth entic ation</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/QueryFu nctions"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="EIS.QueryFunction s"</p>
<p>contract="InfoWorld.EIS.IQ ueryFunctions"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/QueryFunctions"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="EIS.QueryFunction s"</p>
<p>contract="InfoWorld.EIS.IQ ueryFunctions"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>EIS:</p>
<p>Quer yFun ction s</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/QueryFu nctions"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="InfoWorld.EIS.IQ ueryFunctions"</p>
<p>name="EIS.QueryFunction s.Windows"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/QueryFunctions"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="InfoWorld.EIS.IQ ueryFunctions"</p>
<p>name="EIS.QueryFunction s.Windows"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>EIS:</p>
<p>Wind ows auth entic ation</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/EntityMa nagement"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>name="EIS.EntityManage ment"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>contract="InfoWorld.EIS.IE ntityManagement"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/EntityManagement"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>name="EIS.EntityManage ment"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>contract="InfoWorld.EIS.IE ntityManagement"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>EIS:</p>
<p>Entit yMa nage ment</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/EntityMa nagement"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>name="EIS.EntityManage ment.Windows"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="InfoWorld.EIS.IE ntityManagement"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/EntityManagement"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>name="EIS.EntityManage ment.Windows"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="InfoWorld.EIS.IE ntityManagement"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>EIS:</p>
<p>Wind ows auth entic ation</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/CTSVoc abularyRuntime" name="EVS.CTSVocabula ryRuntime" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSVAPI.RuntimeOperation s" behaviorConfiguration="Da</p>
<p>taContractSerializer"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/CTSVocabularyRunti me" name="EVS.CTSVocabula ryRuntime" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSVAPI.RuntimeOperation s" behaviorConfiguration="Da</p>
<p>taContractSerializer"</p>
</blockquote></td>
<td><blockquote>
<p>EVS</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/CTSVoc abularyBrowse" name="EVS.CTSVocabula ryBrowse" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSVAPI.BrowserOperation s" behaviorConfiguration="Da</p>
<p>taContractSerializer"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/CTSVocabularyBrow se" name="EVS.CTSVocabula ryBrowse" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSVAPI.BrowserOperation s" behaviorConfiguration="Da</p>
<p>taContractSerializer"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/CTSMes sageBrowse" name="EVS.CTSMessage Browse" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSMAPI.BrowserOperation s"</p>
<p>behaviorConfiguration="Da taContractSerializer"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/CTSMessageBrowse "</p>
<p>name="EVS.CTSMessage Browse" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSMAPI.BrowserOperation s" behaviorConfiguration="Da</p>
<p>taContractSerializer"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/CTSMes sageRuntime" name="EVS.CTSMessage Runtime" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSMAPI.RuntimeOperation s" behaviorConfiguration="Da</p>
<p>taContractSerializer"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/CTSMessageRuntim e" name="EVS.CTSMessage Runtime" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSMAPI.RuntimeOperation s" behaviorConfiguration="Da</p>
<p>taContractSerializer"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/CTSMes sageEdit" name="EVS.CTSMessage Edit" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSEdit.IMessageEdit" behaviorConfiguration="Da taContractSerializer"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/CTSMessageEdit" name="EVS.CTSMessage Edit" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="InfoWorld.EVS.C TSEdit.IMessageEdit" behaviorConfiguration="Da taContractSerializer"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/CTSVoc abularyEdit" name="EVS.CTSVocabula ryEdit" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="ICTSEditVocabul</p>
<p>ary"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/CTSVocabularyEdit" name="EVS.CTSVocabula ryEdit" binding="basicHttpBinding" bindingConfiguration="EVS Binding" contract="ICTSEditVocabul ary"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/BMSQue ry"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMS.BMSQuery"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerQuery"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BMSQuery"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMS.BMSQuery"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerQuery"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Quer y</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/BMSQue ry"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMS.BMSQuery.W indows"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerQuery"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BMSQuery"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMS.BMSQuery.W indows"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerQuery"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Quer y: Wind ows</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/BMSOpe rations"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMS.BMSOperatio ns"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerOperati ons"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BMSOperations"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMS.BMSOperatio ns"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerOperati ons"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Oper ation s</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/BMSOpe rations"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMS.BMSOperatio ns.Windows"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerOperati ons"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BMSOperations"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMS.BMSOperatio ns.Windows"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerOperati ons"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Oper ation s: Wind ows</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;210:16050/BMSCon figurationOperations"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name</p>
<p>="BMS.BMSConfiguration Operations"</p>
<p>contract="BMS.ServiceCon tracts.IConfigurationOperat ions"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BMSConfigurationOp erations"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name</p>
<p>="BMS.BMSConfiguration Operations"</p>
<p>contract="BMS.ServiceCon tracts.IConfigurationOperat ions"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Confi gurat ion</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;210:16050/BMSCon figurationOperations"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name</p>
<p>="BMS.BMSConfiguration Operations.Windows"</p>
<p>contract="BMS.ServiceCon tracts.IConfigurationOperat ions"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BMSConfigurationOp erations"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name</p>
<p>="BMS.BMSConfiguration Operations.Windows"</p>
<p>contract="BMS.ServiceCon tracts.IConfigurationOperat ions"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Confi gurat ion: Wind ows</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/BedUnav ailableWF"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMSWF.IBedUnav ailableFlow"</p>
<p>contract="BMS.Workflows. WF.IBedUnavailableFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BedUnavailableWF"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMSWF.IBedUnav ailableFlow"</p>
<p>contract="BMS.Workflows. WF.IBedUnavailableFlow"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Bed Unav ailabl e Work flow</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/BedUnav ailableWF"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMSWF.IBedUnav ailableFlow.Windows"</p>
<p>contract="BMS.Workflows. WF.IBedUnavailableFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BedUnavailableWF"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMSWF.IBedUnav ailableFlow.Windows"</p>
<p>contract="BMS.Workflows. WF.IBedUnavailableFlow"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Bed Unav ailabl e Work flow: Wind ows</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/WaitingLi stWF"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMSWF.IWaitingLi stFlow"</p>
<p>contract="BMS.Workflows. WF.IWaitingListFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/WaitingListWF"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMSWF.IWaitingLi stFlow"</p>
<p>contract="BMS.Workflows. WF.IWaitingListFlow"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Waiti ng List Work flow</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/WaitingLi stWF"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMSWF.IWaitingLi stFlow.Windows"</p>
<p>contract="BMS.Workflows. WF.IWaitingListFlow"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/WaitingListWF"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMSWF.IWaitingLi stFlow"</p>
<p>contract="BMS.Workflows. WF.IWaitingListFlow"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Waiti ng List Work flow</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/VistaQue ry"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>contract="BMS.ServiceCon tracts.IVistaWorkerQuery"</p>
<p>name</p>
<p>="BMS.VistaQuery"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/WaitingListWF"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMSWF.IWaitingLi stFlow.Windows"</p>
<p>contract="BMS.Workflows. WF.IWaitingListFlow"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Waiti ng List Work flow: Wind ows</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/VistaQue ry"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="BMS.ServiceCon tracts.IVistaWorkerQuery"</p>
<p>name</p>
<p>="BMS.VistaQuery.Window s"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/VistaQuery"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="BMS.ServiceCon tracts.IVistaWorkerQuery"</p>
<p>name</p>
<p>="BMS.VistaQuery.Window s"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Vista Quer y - Confi gurat ion Wind ows</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>addr<a href="http://vaww.bms/">ess="h</a>tt<a href="http://vaww.bms/">p://</a>va<a href="http://vaww.bms/">ww</a>.<a href="http://vaww.bms/">bms.</a> va.gov:80/CacheService.sv c"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMS.Cache.Windo ws"</p>
<p>contract="BMS.ServiceCon tracts.ICacheService"</p>
</blockquote></td>
<td><blockquote>
<p>addr<a href="http://vaausbms/">ess="h</a>tt<a href="http://vaausbms/">p://</a>vaa<a href="http://vaausbms/">usbms</a> web75.aac.dva.va.gov:80/ CacheService.svc"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>name="BMS.Cache.Windo ws"</p>
<p>contract="BMS.ServiceCon tracts.ICacheService"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Web Cach e - Clien t: Wind ows</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="https://REDACTED</p>
<p>.va.gov:443/CacheService. svc"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win BindingHttps"</p>
<p>name="BMS.Cache.Windo ws.Https"</p>
<p>contract="BMS.ServiceCon tracts.ICacheService"</p>
</blockquote></td>
<td><blockquote>
<p>address="https://vaausbms web75.aac.dva.va.gov:443</p>
<p>/CacheService.svc"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win BindingHttps"</p>
<p>name="BMS.Cache.Windo ws.Https"</p>
<p>contract="BMS.ServiceCon tracts.ICacheService"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Web Cach e - Clien t: Wind ows</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/BMSCac he"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMS.BMSCache"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerCache"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BMSCache"</p>
<p>behaviorConfiguration="Cli entCredentialsBehavior"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="WS FederationHttpBinding_Aut henticatedService"</p>
<p>name="BMS.BMSCache"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerCache"</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS</p>
<p>Cach e</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>endpoint</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>identity\dns</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>address="http://&lt;ServerAd dress&gt;211:16050/BMSCac he"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerCache"</p>
<p>name="BMS.BMSCache.W indows"</p>
</blockquote></td>
<td><blockquote>
<p>address="http://localhost:1 6050/BMSCache"</p>
<p>behaviorConfiguration="Wi ndowsClientCredentials"</p>
<p>binding="wsFederationHttp Binding"</p>
<p>bindingConfiguration="Win Binding"</p>
<p>contract="BMS.ServiceCon tracts.IBedManagerCache"</p>
<p>name="BMS.BMSCache.W indows"</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>behaviors</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
<td><blockquote>
<p>value="IWHM3Services"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>serviceBehaviors</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>behavior</p>
</blockquote></td>
<td><blockquote>
<p>name="ServiceBehavior"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>serviceMetadata</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>httpGetEnabled="true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>serviceDebug</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>includeExceptionDetailInFaults="true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>dataContractSerializer</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>type="InfoWorld.Security.Saml20.Saml20ServiceCredentials, Saml20"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>serviceCredentials</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>type="InfoWorld.Security.Saml20.Saml20ServiceCredentials, Saml20"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>serviceCertificate</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>findValue="IWHM3Services" storeLocation="LocalMachine" storeName="My" x509FindType="FindBySubjectName"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>issuedTokenAuthentication</p>
<p>\knownCertificates\add</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>findValue="IWHM3STS" storeLocation="LocalMachine" storeName="My" x509FindType="FindBySubjectName"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>behavior name="WorkflowService"</p>
</blockquote></td>
<td colspan="3"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>serviceMetadata httpGetEnabled="true"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>serviceThrottling</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>serviceDebug</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>maxConcurrentCalls="150 0"</p>
<p>maxConcurrentSessions=" 1500"</p>
</blockquote></td>
<td><blockquote>
<p>maxConcurrentCalls="100 0"</p>
<p>maxConcurrentSessions=" 1000"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>serviceCredentials</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>includeExceptionDetailInFa ults="true"</p>
</blockquote></td>
<td><blockquote>
<p>includeExceptionDetailInFa ults="true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>serviceCertificate</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>type="InfoWorld.Security.S aml20.Saml20ServiceCred entials, Saml20"</p>
</blockquote></td>
<td><blockquote>
<p>type="InfoWorld.Security.S aml20.Saml20ServiceCred entials, Saml20"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>issuedTokenAuthentication</p>
<p>\knownCertificates\add</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>findValue="IWHM3Service s" storeLocation="LocalMachi ne" storeName="My" x509FindType="FindBySub jectName"</p>
</blockquote></td>
<td><blockquote>
<p>findValue="IWHM3Service s" storeLocation="LocalMachi ne" storeName="My" x509FindType="FindBySub jectName"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>sqlWorkflowInstanceStore</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>findValue="IWHM3STS" storeLocation="LocalMachi ne" storeName="My" x509FindType="FindBySub jectName"</p>
</blockquote></td>
<td><blockquote>
<p>findValue="IWHM3STS" storeLocation="LocalMachi ne" storeName="My" x509FindType="FindBySub jectName"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>workflowIdle</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>connectionString="Data Source=&lt;DatabaseAddres s&gt;;Network Library=DBMSSOCN;Initial Catalog=BMS_InstanceSto re;Integrated Security=True;Asynchrono us Processing=True;Pooling=t rue;Min Pool Size=0;Max Pool Size=250;" instanceEncodingOption=" None" instanceCompletionAction= "DeleteAll" instanceLockedExceptionA ction="BasicRetry" hostLockRenewalPeriod=" 00:00:30"</p>
<p>runnableInstancesDetectio nPeriod="00:00:02"</p>
</blockquote></td>
<td><blockquote>
<p>connectionString="Data Source=&lt;DatabaseAddres s&gt;;Initial Catalog=BMS_InstanceSto re;Integrated Security=True;Asynchrono us Processing=True;Pooling=t rue;Min Pool Size=0;Max Pool Size=100;" instanceEncodingOption=" None" instanceCompletionAction= "DeleteAll" instanceLockedExceptionA ction="BasicRetry" hostLockRenewalPeriod=" 00:00:30"</p>
<p>runnableInstancesDetectio nPeriod="00:00:02"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>sqlWorkflowInstanceStore</p>
<p>Promotion</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>timeToUnload="00:00:00"</p>
<p>timeToPersist="00:00:00"</p>
</blockquote></td>
<td><blockquote>
<p>timeToUnload="0"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>promotionSets</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>connectionString="Data Source=&lt;DatabaseAddres s&gt;;Network Library=DBMSSOCN;Initial Catalog=BMS_InstanceSto re;Integrated Security=True;Pooling=tru e;Min Pool Size=0;Max</p>
<p>Pool Size=250;"</p>
</blockquote></td>
<td><blockquote>
<p>connectionString="Data Source=&lt;DatabaseAddres s&gt;;Initial Catalog=BMS_InstanceSto re;Integrated Security=True;Pooling=tru e;Min Pool Size=0;Max Pool Size=100;"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>promotionSet name="AdmissionData"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>promotionSet name="TransferData"</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>&lt;promotedValue propertyName="AdmissionI d"/&gt;</p>
<p>&lt;promotedValue propertyName="PatientNa me"/&gt;</p>
<p>&lt;promotedValue propertyName="LocationN ame"/&gt;</p>
</blockquote></td>
<td><blockquote>
<p>&lt;promotedValue propertyName="AdmissionI d"/&gt;</p>
<p>&lt;promotedValue propertyName="PatientNa me"/&gt;</p>
<p>&lt;promotedValue propertyName="LocationN ame"/&gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>behavior</p>
<p>name="BasicBindingBeha vior"</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>promotedValue</p>
<p>propertyName="PatientSS N"</p>
</blockquote></td>
<td><blockquote>
<p>promotedValue</p>
<p>propertyName="PatientSS N"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>endpointBehaviors</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>&lt;dataContractSerializer maxItemsInObjectGraph=" 2147483647"/&gt;</p>
<p>&lt;serviceDebug includeExceptionDetailInFa ults="true"/&gt;</p>
<p>&lt;serviceMetadata httpGetEnabled="true"/&gt;</p>
</blockquote></td>
<td><blockquote>
<p>&lt;dataContractSerializer maxItemsInObjectGraph=" 2147483647"/&gt;</p>
<p>&lt;serviceDebug includeExceptionDetailInFa ults="true"/&gt;</p>
<p>&lt;serviceMetadata httpGetEnabled="true"/&gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>behavior</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>dataContractSerializer</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>name="ClientCredentialsB ehavior"</p>
</blockquote></td>
<td><blockquote>
<p>name="ClientCredentialsB ehavior"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>durableIssuedTokenClient</p>
<p>Credentials\serviceCertific ate</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>maxItemsInObjectGraph=" 2147483647"</p>
</blockquote></td>
<td><blockquote>
<p>maxItemsInObjectGraph=" 2147483647"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>authentication</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>x509FindType="FindBySub jectName" findValue="IWHM3Service s" storeName="My" storeLocation="LocalMachi</p>
<p>ne"</p>
</blockquote></td>
<td><blockquote>
<p>x509FindType="FindBySub jectName" findValue="IWHM3Service s" storeName="My" storeLocation="LocalMachi</p>
<p>ne"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>scopedCertificates\add</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>revocationMode="NoCheck "</p>
</blockquote></td>
<td><blockquote>
<p>revocationMode="NoCheck "</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>durableIssuedToken</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>targetUri="http://&lt;ServerAd dress&gt;210:16050/STS/" x509FindType="FindBySub jectName" findValue="IWHM3STS" storeName="My" storeLocation="LocalMachi ne"</p>
</blockquote></td>
<td><blockquote>
<p>targetUri="http://localhost:1 6050/STS/"</p>
<p>x509FindType="FindBySub jectName" findValue="IWHM3STS" storeName="My" storeLocation="LocalMachi ne"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>behavior</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>connectionString="Data Source=&lt;DatabaseAddres s&gt;;Network Library=DBMSSOCN;Initial Catalog=BMS;Integrated Security=True;Pooling=tru e;Min Pool Size=0;Max Pool Size=250;"</p>
<p>identifier="SessionID"</p>
<p>isolationLevel="ReadCom mitted"</p>
</blockquote></td>
<td><blockquote>
<p>connectionString="Data Source=&lt;DatabaseAddres s&gt;;Initial Catalog=BMS;Integrated Security=True;Pooling=tru e;Min Pool Size=0;Max Pool Size=100;"</p>
<p>identifier="SessionID"</p>
<p>isolationLevel="ReadCom mitted"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>dataContractSerializer</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>name="WindowsClientCre dentials"</p>
</blockquote></td>
<td><blockquote>
<p>name="WindowsClientCre dentials"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>clientCredentials</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>maxItemsInObjectGraph=" 2147483647"</p>
</blockquote></td>
<td><blockquote>
<p>maxItemsInObjectGraph=" 2147483647"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>windows</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>type="InfoWorld.Security.A uthentication.CacheClientC redentials,</p>
<p>SecurityTokenCache"</p>
</blockquote></td>
<td><blockquote>
<p>type="InfoWorld.Security.A uthentication.CacheClientC redentials,</p>
<p>SecurityTokenCache"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>serviceCertificate</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>allowNtlm="true"</p>
</blockquote></td>
<td><blockquote>
<p>allowNtlm="true"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>defaultCertificate</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>authentication</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>x509FindType="FindBySub jectName" findValue="IWHM3Service s" storeName="My" storeLocation="LocalMachi ne"</p>
</blockquote></td>
<td><blockquote>
<p>x509FindType="FindBySub jectName" findValue="IWHM3Service s" storeName="My" storeLocation="LocalMachi ne"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>scopedCertificates\add</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>revocationMode="NoCheck "</p>
</blockquote></td>
<td><blockquote>
<p>revocationMode="NoCheck "</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>behavior</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>targetUri="http://&lt;ServerAd dress&gt;210:16050/STS/Win dows" x509FindType="FindBySub jectName" findValue="IWHM3STS" storeName="My" storeLocation="LocalMachi</p>
<p>ne"</p>
</blockquote></td>
<td><blockquote>
<p>targetUri="http://localhost:1 6050/STS/Windows" x509FindType="FindBySub jectName" findValue="IWHM3STS" storeName="My" storeLocation="LocalMachi ne"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>dataContractSerializer</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>name="DataContractSeriali zer"</p>
</blockquote></td>
<td><blockquote>
<p>name="DataContractSeriali zer"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>extensions\behaviorExtens ions</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>maxItemsInObjectGraph=" 2147483647"</p>
</blockquote></td>
<td><blockquote>
<p>maxItemsInObjectGraph=" 2147483647"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>add</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>add</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>name="sqlWorkflowInstanc eStorePromotion" type="BMS.Workflows.Pro pertyPromotionActivity.Con figuration.SqlWorkflowInsta nceStorePromotionElemen t, BMS.Workflows.PropertyPr omotionActivity"</p>
</blockquote></td>
<td><blockquote>
<p>name="sqlWorkflowInstanc eStorePromotion" type="BMS.Workflows.Pro pertyPromotionActivity.Con figuration.SqlWorkflowInsta nceStorePromotionElemen t, BMS.Workflows.PropertyPr omotionActivity"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>add</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>name="errorHandler" type="BMS.Workflows.Cus tomActivities.Utils.WFError HandlerElement, BMS.Workflows.CustomAc</p>
<p>tivities"</p>
</blockquote></td>
<td><blockquote>
<p>name="errorHandler" type="BMS.Workflows.Cus tomActivities.Utils.WFError HandlerElement, BMS.Workflows.CustomAc</p>
<p>tivities"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>log4net</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>name="durableIssuedToke nClientCredentials" type="BMS.Security.Config uration.DurableIssuedToke nClientCredentialsConfigH andler, BMS.Security"</p>
</blockquote></td>
<td><blockquote>
<p>name="durableIssuedToke nClientCredentials" type="BMS.Security.Config uration.DurableIssuedToke nClientCredentialsConfigH andler, BMS.Security"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>root</p>
</blockquote></td>
<td><blockquote>
<p>value="OFF"</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>set the level valu e to ALL</p>
<p>or DEB UG</p>
<p>in order to</p>
<p>trace meth</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>od entry and exit time</p>
<p>s</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>level value</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>"SQLAppender"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>appender-ref ref</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>name="FileAppender" type="log4net.Appender.FileAppender"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>appender</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>name="FileAppender" type="log4net.Appender.FileAppender"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="log-file.txt"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>appendToFile</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>layout</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Layout.PatternLayout"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>conversionPattern</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="%date [%6thread] -&amp;gt; %message% &amp;lt;-%newline"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>appender</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>name="SQLAppender" type="log4netAsync.AsyncAdoNetAppender,log4netAsync"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>bufferSize</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="1000"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>connectionType</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="System.Data.SqlClient.SqlConnection, System.Data, Version=1.0.3300.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>connectionString</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="data source=&lt;DatabaseAddress&gt;;Network Library=DBMSSOCN;initial</p>
<p>catalog=BMS_LOG;integrated security=SSPI;persist security info=False;Pooling=true;Min Pool Size=0;Max Pool Size=250;"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>commandText</p>
</blockquote></td>
<td><blockquote>
<p>value="INSERT INTO Log ([Date],[Thread],[Level],[Logger],[Message]</p>
<p>,[Exception]) VALUES (@log_date, @thread, @log_level, @logger, @message, @exception)"</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>value="data source=&lt;DatabaseAddress&gt;; Network Library=DBMSSOCN;initial catalog=BMS_LOG;integrate d security=SSPI;persist security info=False;Pooling=true;Min Pool Size=0;Max Pool</p>
<p>Size=250;"</p>
</blockquote></td>
<td><blockquote>
<p>value="data source=&lt;DatabaseAddress</p>
<p>&gt;;initial catalog=LOG;integrated security=SSPI;persist security info=False;Pooling=true;Mi n Pool Size=0;Max Pool Size=100;"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>parameter</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>parameterName</p>
</blockquote></td>
<td><blockquote>
<p>value="@log_date"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>dbType</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="DateTime"</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>layout</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Layout.RawTimeStampLayout"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>parameter</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>parameterName</p>
</blockquote></td>
<td><blockquote>
<p>value="@thread"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>dbType</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="String"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>size</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="255"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>layout</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Layout.PatternLayout"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>conversionPattern</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="%thread"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>parameter</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>parameterName</p>
</blockquote></td>
<td><blockquote>
<p>value="@log_level"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>dbType</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="String"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>size</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="50"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>layout</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Layout.PatternLayout"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>conversionPattern</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="%level"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>parameter</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>parameterName</p>
</blockquote></td>
<td><blockquote>
<p>value="@logger"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>dbType</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="String"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>size</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="255"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>layout</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Layout.PatternLayout"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>conversionPattern</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="%logger"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>parameter</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>parameterName</p>
</blockquote></td>
<td><blockquote>
<p>value="@message"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>dbType</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="String"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>size</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="4000"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>layout</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Layout.PatternLayout"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>conversionPattern</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="%message"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>parameter</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>parameterName</p>
</blockquote></td>
<td><blockquote>
<p>value="@exception"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>dbType</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="String"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>size</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="2000"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>layout</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Layout.ExceptionLayout"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>filter</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Filter.StringMatchFilter"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>stringToMatch</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="00:00:00.00"</p>
</blockquote></td>
<td><blockquote>
<p>do not log mes sage s with durat ions unde r 00:0</p>
<p>0:00.</p>
<p>00*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>acceptOnMatch</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="false"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>filter</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>type="log4net.Filter.StringMatchFilter"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>stringToMatch</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="Entry"</p>
</blockquote></td>
<td><blockquote>
<p>do not log entry mes sage s as they are not relev ant durat</p>
<p>ion- wise</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 27%" />
<col style="width: 1%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration Key/Name</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th></th>
<th><blockquote>
<p><strong>Des cript</strong></p>
<p><strong>ion</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="3"><blockquote>
<p>Split Service</p>
</blockquote></td>
<td><blockquote>
<p>Combine Service</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td><blockquote>
<p>BMS.VI.ServiceHost.exe.c onfig</p>
</blockquote></td>
<td><blockquote>
<p>BMS.ServiceHost.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>acceptOnMatch</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>value="false"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>startup</p>
</blockquote></td>
<td colspan="4"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>supportedRuntime</p>
</blockquote></td>
<td><blockquote>
<p>version="v4.6" sku=".NETFramework,Version=v4.6.1"</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>runtime\gcServer</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>enabled="true"</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="4"></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="_bookmark13" class="anchor"></span>Table 5-EIS Service Configuration Parameters

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>configuration/ connectionStrings/ add</p>
</blockquote></td>
<td><blockquote>
<p>ConnectionString</p>
</blockquote></td>
<td><blockquote>
<p>Workstation id= <em>vadbserver\sql2008r2</em>;packet size=4096;data source= <em>vadbserver \sql2008r2</em>;persist security info=False;Initial Catalog=BMS_EIS;Integrated Security=SSPI;</p>
</blockquote></td>
<td><blockquote>
<p>Connection string for the connection to the BMS_EIS database.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EISService</p>
</blockquote></td>
<td rowspan="8"></td>
<td></td>
<td><blockquote>
<p>DatasetPath</p>
<p>OverwriteCreateEntityId</p>
</blockquote></td>
<td><blockquote>
<p>DBRepository</p>
<p>true/false</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Data Adapters (XML mapping files) path.</p>
<p>If set to true, the service generates a new unique identifier on each resource create call, otherwise, it uses the identifier received as parameter.</p>
<p>If set to true, the service notifies linked</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Implementation. dll.config</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NotificationIndicator</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EIS services of changes produced on entities.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td><blockquote>
<p>UseSecurityContext</p>
</blockquote></td>
<td><blockquote>
<p>0/1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ePractice security context</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td rowspan="2"><blockquote>
<p>appSettings/ key</p>
</blockquote></td>
<td><blockquote>
<p>DnsIdentity</p>
</blockquote></td>
<td><blockquote>
<p>IWHM3Services</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Certificate which specifies the service's</p>
<p>dns identity.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ReceiveIndicator</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>If set to true, the service accepts</p>
<p>notification messages from linked EIS services.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>AutomaticLinkIndicator</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>If set to true, entities are automatically</p>
<p>linked (associated as equivalent) across linked EIS services.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>XEISIndicator</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Specifies whether the cross EIS worker</p>
<p>should be started.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>XEISDomain</p>
</blockquote></td>
<td><blockquote>
<p>domain name</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Domain of the cross EIS implementation.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="35"></td>
<td rowspan="10"></td>
<td></td>
<td></td>
<td><blockquote>
<p>Specifies the topic of the synchronization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SubscriptionTopic</p>
</blockquote></td>
<td><blockquote>
<p>entity</p>
</blockquote></td>
<td><blockquote>
<p>subscription, meaning what should be</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>synced.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>AuditProtocol</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>none/udp</p>
</blockquote></td>
<td><blockquote>
<p>Transfer protocol to communicate with the</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>audit service or none if not used.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AuditServer</p>
</blockquote></td>
<td><blockquote>
<p>auditserver</p>
</blockquote></td>
<td><blockquote>
<p>Server where the audit service resides.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>AuditPort</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>10000</p>
</blockquote></td>
<td><blockquote>
<p>Port of the audit service on the specified</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>server.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>AuditSynchronIndicator</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>true/false</p>
</blockquote></td>
<td><blockquote>
<p>Specifies if the Audit Service should be</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>called synchronous or asynchronous.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>system.serviceMod</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>el/behaviors/endpoi</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ntBehaviors/behavi</p>
<p>or/clientCredentials/</p>
</blockquote></td>
<td><blockquote>
<p>targetUri</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/</p>
<p>Windows</p>
</blockquote></td>
<td><blockquote>
<p>URI of STS certificate.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>serviceCertificate/sc</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>opedCertificates/ad</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>d</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>system.serviceMod</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>el/bindings/</p>
<p>wsFederationHttpBi</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/mex</p>
</blockquote></td>
<td><blockquote>
<p>STS metadata exchange URL used by</p>
<p>ServiceBinding.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>nding/binding/mess</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>age/issuerMetadata</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>system.serviceMod</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>el/bindings/</p>
<p>wsFederationHttpBi</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/</p>
<p>Windows</p>
</blockquote></td>
<td><blockquote>
<p>STS URL used by WinBinding.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>nding/binding/securi</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ty/message/issuer</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>system.serviceMod</p>
<p>el/services/service/h</p>
<p>ost/baseAddress/</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ QueryFunctions</p>
</blockquote></td>
<td><blockquote>
<p>EIS Query Functions service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>add</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>system.serviceMod</p>
<p>el/services/service/h ost/baseAddress/</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ Administration</p>
</blockquote></td>
<td><blockquote>
<p>EIS Administration service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>add</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/</p>
</blockquote></td>
<td><blockquote>
<p>EIS EntityManagement service endpoint</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>system.serviceMod</p>
</blockquote></td>
<td><blockquote>
<p>EntityManagement</p>
</blockquote></td>
<td><blockquote>
<p>address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="9"></td>
<td><blockquote>
<p>el/services/service/h</p>
<p>ost/baseAddress/ add</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
<p>system.serviceMod el/services/service/h</p>
<p>ost/baseAddress/ add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ ServiceMetadataManagement</p>
</blockquote></td>
<td><blockquote>
<p>EIS ServiceMetadataManagement service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/</p>
<p>system.serviceMod el/services/service/h ost/baseAddress/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ BulkEntityManagement</p>
</blockquote></td>
<td><blockquote>
<p>EIS Bulk BulkEntityManagement service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h</p>
<p>ost/baseAddress/ add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ Subscribe</p>
</blockquote></td>
<td><blockquote>
<p>EIS Subscribe service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/</p>
<p>system.serviceMod el/services/service/h ost/baseAddress/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ LinkAlgorithmAdministration</p>
</blockquote></td>
<td><blockquote>
<p>EIS LinkAlgorithmAdministration service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h ost/baseAddress/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/EIS/ SubscriptionAdministration</p>
</blockquote></td>
<td><blockquote>
<p>EIS SubscriptionAdministration service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h ost/baseAddress/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/Receive</p>
</blockquote></td>
<td><blockquote>
<p>EIS Receive service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h</p>
<p>ost/baseAddress/ add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/EIS/ MessageAdministration</p>
</blockquote></td>
<td><blockquote>
<p>EIS MessageAdministration service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/</p>
<p>system.serviceMod el/services/service/h</p>
<p>ost/baseAddress/</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/EIS/ AuthorizationSubscriber</p>
</blockquote></td>
<td><blockquote>
<p>EIS AuthorizationSubscriber service endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>add</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Connections.xml</p>
</blockquote></td>
<td><blockquote>
<p>MyConnections/ connectionString</p>
</blockquote></td>
<td><blockquote>
<p>connectionString</p>
</blockquote></td>
<td><blockquote>
<p>workstation id= <em>vadbserver\sql2008r2</em>;packet size=4096;data source= <em>vadbserver\sql2008r2</em>;persist security info=False;Initial Catalog=BMS_EIS;Integrated</p>
<p>Security=SSPI;</p>
</blockquote></td>
<td><blockquote>
<p>Connection string for the connection to the BMS_EIS database.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark14" class="anchor"></span>Table 6-EVS Service Configuration Parameters

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="12"><blockquote>
<p>MessageImpl.dll. config</p>
</blockquote></td>
<td rowspan="12"><blockquote>
<p>configuration/ appSettings/ key</p>
</blockquote></td>
<td><blockquote>
<p>DatasetPath ApplicationFolder SqlScriptsFolder TextFilesFolder PackageFilesFolder CodeMappingTempTable</p>
</blockquote></td>
<td><blockquote>
<p>DBRepository D:\CTS\CTSImport SqlScrips TextFiles PackageFiles dbo.TempMapping</p>
</blockquote></td>
<td><blockquote>
<p>Data Adapters (XML mapping files) path. String path to application folder.</p>
<p>SQL scripts folder name. Text files folder name.</p>
<p>Package files folder name.</p>
<p>The mapping temporary table name.</p>
</blockquote></td>
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
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TemporaryFolder</p>
</blockquote></td>
<td><blockquote>
<p>Temp</p>
</blockquote></td>
<td><blockquote>
<p>Temporary folder name.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SubscriptionTopic</p>
</blockquote></td>
<td><blockquote>
<p>cts</p>
</blockquote></td>
<td><blockquote>
<p>Specifies the topic of the synchronization subscription, meaning what should be synced.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NotificationIndicator</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td><blockquote>
<p>Notification indicator.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BulkInsertBatchSize</p>
</blockquote></td>
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>Maximum number of processed records in one step.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DnsIdentity</p>
</blockquote></td>
<td><blockquote>
<p>IWHM3Services</p>
</blockquote></td>
<td><blockquote>
<p>Certificate which specifies the service's</p>
<p>dns identity.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>StartSecurityEndpoints</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td><blockquote>
<p>Specifies if the secure endpoints are to be started.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>http://localhost:17050/CTSImport</p>
</blockquote></td>
<td><blockquote>
<p>EVS</p>
</blockquote></td>
<td><blockquote>
<p>EVS import from excel key.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3"></td>
<td></td>
<td><blockquote>
<p>http://localhost:17050/CTSExport</p>
</blockquote></td>
<td><blockquote>
<p>EVS</p>
</blockquote></td>
<td><blockquote>
<p>EVS export to excel key.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
<p>system.serviceMod el/services/service/h</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSVocabularyRuntime</p>
</blockquote></td>
<td><blockquote>
<p>CTS VocabularyRuntime service endpoint address (HTTP Protocol).</p>
<p>CTS VocabularyRuntime service endpoint</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ost/baseAddresses/</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>https://vaserver:17706/</p>
</blockquote></td>
<td><blockquote>
<p>address (HTTPS Protocol).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="12"></td>
<td><blockquote>
<p>add</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CTSVocabularyRuntime</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSMapping</p>
</blockquote></td>
<td><blockquote>
<p>CTS Mapping service endpoint address (HTTP Protocol).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>el/services/service/h</p>
<p>ost/baseAddresses/ add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>https://<em>vaserver:17706</em>/ CTSMapping</p>
</blockquote></td>
<td><blockquote>
<p>CTS Mapping service endpoint address (HTTPS Protocol).</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>configuration/ system.serviceMod el/services/service/h</p>
<p>ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/</p>
<p>CTSVocabularyBrowse</p>
</blockquote></td>
<td><blockquote>
<p>CTS VocabularyBrowse service endpoint address (HTTP Protocol).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>https://<em>vaserver:17706</em>/ CTSVocabularyBrowse</p>
</blockquote></td>
<td><blockquote>
<p>CTS VocabularyBrowse service endpoint address (HTTPS Protocol).</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>configuration/ system.serviceMod el/services/service/h</p>
<p>ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/</p>
<p>CTSMessageRuntime</p>
</blockquote></td>
<td><blockquote>
<p>CTS MessageRuntime service endpoint address (HTTP Protocol).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>https://<em>vaserver:17706</em>/ CTSMessageRuntime</p>
</blockquote></td>
<td><blockquote>
<p>CTS MessageRuntime service endpoint address (HTTPS Protocol).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSMessageBrowse</p>
</blockquote></td>
<td><blockquote>
<p>CTS MessageBrowse service endpoint address (HTTP Protocol).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>el/services/service/h</p>
<p>ost/baseAddresses/ add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>https://<em>vaserver:17706</em>/ CTSMessageBrowse</p>
</blockquote></td>
<td><blockquote>
<p>CTS MessageBrowse service endpoint address (HTTPS Protocol).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSMessageEdit</p>
</blockquote></td>
<td><blockquote>
<p>CTS MessageEdit service endpoint address (HTTP Protocol).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>el/services/service/h</p>
<p>ost/baseAddresses/ add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>https://<em>vaserver:17706</em>/ CTSMessageEdit</p>
</blockquote></td>
<td><blockquote>
<p>CTS MessageEdit service endpoint address (HTTPS Protocol).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/</p>
<p>CTSVocabularyEdit</p>
</blockquote></td>
<td><blockquote>
<p>CTS VocabularyEdit service endpoint address (HTTP Protocol).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td><blockquote>
<p>system.serviceMod</p>
<p>el/services/service/h ost/baseAddresses/</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>https://<em>vaserver:17706</em>/ CTSVocabularyEdit</p>
</blockquote></td>
<td><blockquote>
<p>CTS VocabularyEdit service endpoint address (HTTPS Protocol).</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>configuration/ system.serviceMod el/services/service/h</p>
<p>ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/</p>
<p>CTSMappingEdit</p>
</blockquote></td>
<td><blockquote>
<p>CTS MappingEdit service endpoint address (HTTP Protocol).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>https://<em>vaserver:17706</em>/ CTSMappingEdit</p>
</blockquote></td>
<td><blockquote>
<p>CTS MappingEdit service endpoint address (HTTPS Protocol).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
<p>system.serviceMod el/services/service/h</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/Xaml</p>
</blockquote></td>
<td><blockquote>
<p>XAML service endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="6"></td>
<td><blockquote>
<p>ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h</p>
<p>ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ EVSWrapper</p>
</blockquote></td>
<td><blockquote>
<p>EVS Wrapper service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSImport</p>
</blockquote></td>
<td><blockquote>
<p>CTS Import service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSExport</p>
</blockquote></td>
<td><blockquote>
<p>CTS Export service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h</p>
<p>ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSEditBulk</p>
</blockquote></td>
<td><blockquote>
<p>CTS EditBulk service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h</p>
<p>ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/CTS/ SubscriptionAdministration</p>
</blockquote></td>
<td><blockquote>
<p>CTS Subscription Administration service endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><strong>Configuration values (ex.)</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"></td>
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/h</p>
<p>ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/CTS/ MessageAdministration</p>
</blockquote></td>
<td><blockquote>
<p>CTS Message Administration service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>bindings/ wsFederationHttpBi nding/binding/</p>
<p>security/message/ issuerMetadata</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td>http://<em>vaserver</em>:<em>17050</em>/STS/mex</td>
<td><blockquote>
<p>STS metadata exchange URL used by ServiceBinding.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/bin dings/ wsFederationHttpBi</p>
<p>nding/binding/securi ty/message/issuer</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ STS/Windows</p>
</blockquote></td>
<td><blockquote>
<p>STS URL used by WinBinding.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVSWrapper.dll. config</p>
</blockquote></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/ser vices/service/host/ baseAddresses/add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ EVSWrapper</p>
</blockquote></td>
<td><blockquote>
<p>EVS Wrapper service endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark15" class="anchor"></span>Table 7-PAP Service Configuration Parameters

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DefaultResourceRoot</p>
</blockquote></td>
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Default root for identifiers.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/ appSettings/</p>
</blockquote></td>
<td rowspan="7"></td>
<td><blockquote>
<p>DatasetPath</p>
<p>su SubscriptionTopic</p>
</blockquote></td>
<td><blockquote>
<p>DBRepository</p>
<p>hmcomplus Authorization</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Data Adapters (XML mapping files) path.</p>
<p>Specifies the super user of the application.</p>
<p>Specifies the topic of the synchronization subscription, meaning what should be synced.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>key</p>
</blockquote></td>
<td><blockquote>
<p>DnsIdentity</p>
</blockquote></td>
<td><blockquote>
<p>IWHM3Services</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Certificate which specifies the service's dns identity.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>AuditProtocol</p>
</blockquote></td>
<td><blockquote>
<p>none/udp</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Transfer protocol to communicate with the</p>
<p>audit service or none if not used.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PolicyAdministration</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>AuditServer</p>
</blockquote></td>
<td><blockquote>
<p>auditserver</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Server where the audit service resides.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Point.dll.config</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>AuditPort</p>
</blockquote></td>
<td><blockquote>
<p>10000</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Port of the audit service on the specified server.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>configuration/ connectionStrings/ add</p>
</blockquote></td>
<td><blockquote>
<p>connectionString</p>
</blockquote></td>
<td><blockquote>
<p>workstation id= <em>vadbserver\sql2008r2</em>;packet size=4096;data source= <em>vadbserver\sql2008r2</em>;persist security info=False;Initial Catalog=BMS_AUTHZ;Integrated</p>
<p>Security=SSPI;</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Connection string for the connection to the BMS_AUTHZ database.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>configuration/syste m.serviceModel/ bindings/ wsFederationHttpBi</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/ Windows</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STS URL used by UpnBinding.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>nding/binding/securi ty/message/issuer</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="7"></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/ bindings/ wsFederationHttpBi nding/binding/securi</p>
<p>ty/message/issuer</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/ Windows</p>
</blockquote></td>
<td><blockquote>
<p>STS URL used by WinBinding.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/syste m.serviceModel/ser vices/service/host/ baseAddresses/add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PAP</p>
</blockquote></td>
<td><blockquote>
<p>PAP service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/syste m.serviceModel/ser vices/service/host/ baseAddresses/add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ AuthorizationPublisher</p>
</blockquote></td>
<td><blockquote>
<p>AuthorizationPublisher service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/syste m.serviceModel/ser vices/service/host/ baseAddresses/add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PAP/ MessageAdministration</p>
</blockquote></td>
<td><blockquote>
<p>MessageAdministration service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/syste m.serviceModel/ser vices/service/host/ baseAddresses/add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PAP/ SubscriptionAdministration</p>
</blockquote></td>
<td><blockquote>
<p>SubscriptionAdministration service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/syste m.serviceModel/ client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PDP/ Request</p>
</blockquote></td>
<td><blockquote>
<p>PDP request client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/syste m.serviceModel/beh aviors/endpointBeh aviors/behavior/ clientCredentials/ serviceCertificate/</p>
<p>scopedCertificates/ add</p>
</blockquote></td>
<td><blockquote>
<p>targetUri</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/ Windows</p>
</blockquote></td>
<td><blockquote>
<p>URI of STS certificate.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Connections.xml</p>
</blockquote></td>
<td><blockquote>
<p>MyConnections/</p>
<p>MyConnection/</p>
</blockquote></td>
<td><blockquote>
<p>connectionString</p>
</blockquote></td>
<td><blockquote>
<p>workstation id=</p>
<p><em>vadbserver\sql2008r2</em>;packet</p>
</blockquote></td>
<td><blockquote>
<p>Connection string for the connection to</p>
<p>the BMS_AUTHZ database.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ConnectionString</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>size=4096;data source= <em>vadbserver\sql2008r2</em>;persist security info=False;Initial Catalog=BMS_AUTHZ;Integrated</p>
<p>Security=SSPI;</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="_bookmark16" class="anchor"></span>Table 8-PDP Service Configuration Parameters

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"></td>
<td rowspan="2"><blockquote>
<p>configuration/ appSettings/ key</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DefaultResourceRoot</p>
</blockquote></td>
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Default root for identifiers.</p>
</blockquote></td>
<td rowspan="3"></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>ConnectionString</p>
</blockquote></td>
<td><blockquote>
<p>Data source=<em>vadbserver\sql2008</em>;</p>
<p>InitialCatalog=BMS_AUTHZ;Persi</p>
<p>st Security Info=False;Integrated Security=SSPI</p>
</blockquote></td>
<td><blockquote>
<p>Connection string for the connection to the BMS_AUTHZ database.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PolicyDecision Point.dll.config</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>system.serviceMod el/bindings/ wsFederationHttpBi nding/binding/securi ty/message/issuerM</p>
<p>etadata</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/mex</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STS metadata exchange URL used by ServiceBinding.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>system.serviceMod el/services/service/h ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PDP</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PDP service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>system.serviceMod el/services/service/h ost/baseAddresses/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PDP/ Request</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PDP Request service endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark17" class="anchor"></span>Table 9-RS Service Configuration Parameters

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>RS.Service Implementation.</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>configuration/ appSettings/</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DefaultResourceRoot</p>
</blockquote></td>
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Default root for identifiers.</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ReportingServicesURL</p>
</blockquote></td>
<td><blockquote>
<p>http://vaserver:90/Report</p>
</blockquote></td>
<td><blockquote>
<p>Reporting services URL address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dll.config</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>key</p>
</blockquote></td>
<td rowspan="2"></td>
<td><blockquote>
<p>Server/ReportService2005.</p>
</blockquote></td>
<td colspan="2" rowspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>asmx</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>RootFolderName</p>
</blockquote></td>
<td><blockquote>
<p>Reporting Service</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Reports root folder in the reporting services.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>AuditProtocol</p>
</blockquote></td>
<td><blockquote>
<p>none/udp</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Transfer protocol to communicate with the</p>
<p>audit service or none if not used.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>AuditServer</p>
</blockquote></td>
<td><blockquote>
<p>auditserver</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Server where the audit service resides.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>AuditPort</p>
</blockquote></td>
<td><blockquote>
<p>10000</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Port of the audit service on the specified</p>
<p>server.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PDP/ Request</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PDP request client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>system.serviceMod el/bindings/ wsFederationHttpBi nding/binding/securi</p>
<p>ty/message/issuerM etadata</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/mex</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STS metadata exchange URL used by ServiceBinding.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>system.serviceMod</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>el/bindings/ wsFederationHttpBi nding/binding/</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/ Windows</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>URL of CustomBinding_IAuthenticationService.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>security/message/</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>issuer</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>system.serviceMod el/services/service/</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/RS</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>RS service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>host/baseAddresse s/add</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/ system.serviceMod el/behaviors/ endpointBehaviors/ behavior/ clientCredentials/ serviceCertificate/</p>
<p>scopedCertificates/a dd</p>
</blockquote></td>
<td><blockquote>
<p>targetUri</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/ Windows</p>
</blockquote></td>
<td><blockquote>
<p>URI of STS certificate.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark18" class="anchor"></span>Table 10-STS Service Configuration Parameters

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 19%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td rowspan="4"></td>
<td><blockquote>
<p>Delay</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0:01:00</p>
</blockquote></td>
<td><blockquote>
<p>Sleep interval between the retries to insert the superusers in the database.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TokenTTL</p>
</blockquote></td>
<td><blockquote>
<p>InMinutes</p>
</blockquote></td>
<td><blockquote>
<p>1442</p>
</blockquote></td>
<td><blockquote>
<p>Time to live of the security token, in minutes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STSCertifi</p>
<p>STSCertifi</p>
</blockquote></td>
<td><blockquote>
<p>cateStoreName</p>
<p>cateStoreLocation</p>
</blockquote></td>
<td><blockquote>
<p>My</p>
<p>LocalMachine</p>
</blockquote></td>
<td><blockquote>
<p>Specifies the name of the X.509 certificate store to open.</p>
<p>Specifies the location of the X.509 STS certificate store.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>STSCertifi</p>
</blockquote></td>
<td><blockquote>
<p>cateFindType</p>
</blockquote></td>
<td><blockquote>
<p>FindBySubjectName</p>
</blockquote></td>
<td><blockquote>
<p>Specifies the type of value the X509Certificate2Collection.Find method</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td rowspan="2"><blockquote>
<p>configuration/ appSettings/</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
<td><blockquote>
<p>searches for.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>STSCertificateFindValue</p>
</blockquote></td>
<td><blockquote>
<p>IWHM3STS</p>
</blockquote></td>
<td><blockquote>
<p>STS Certificate name.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>key</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ServiceCertificateStoreName</p>
</blockquote></td>
<td><blockquote>
<p>My</p>
</blockquote></td>
<td><blockquote>
<p>Specifies the name of the X.509 certificate</p>
<p>store to open.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SecureToken</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>ServiceCertificateStoreLocation</p>
</blockquote></td>
<td><blockquote>
<p>LocalMachine/CurrentUser</p>
</blockquote></td>
<td><blockquote>
<p>Specifies the location of the X.509 services' certificate store.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Service.dll.config</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>ServiceCertificateFindType</p>
</blockquote></td>
<td><blockquote>
<p>FindBySubjectName</p>
</blockquote></td>
<td><blockquote>
<p>Specifies the type of value the</p>
<p>X509Certificate2Collection.Find method searches for.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>ServiceCertificateFindValue</p>
</blockquote></td>
<td><blockquote>
<p>IWHM3Services</p>
</blockquote></td>
<td><blockquote>
<p>Services' Certificate name.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td rowspan="2"></td>
<td><blockquote>
<p>su</p>
</blockquote></td>
<td><blockquote>
<p>Domain qualified user names, comma separated.</p>
</blockquote></td>
<td><blockquote>
<p>Usernames of all the super users in the application.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>domains</p>
</blockquote></td>
<td><blockquote>
<p>VA|VA</p>
</blockquote></td>
<td><blockquote>
<p>Comma separated list of root|extension</p>
<p>values for the application's domains.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/ connectionStrings/ add</p>
</blockquote></td>
<td><blockquote>
<p>connectionString</p>
</blockquote></td>
<td><blockquote>
<p>workstation id= <em>vadbserver\sql2008r2</em>;packet size=4096;data source= <em>vadbserver\sql2008</em>;persist security info=False;Initial Catalog=BMS_AUTHZ;Integrated</p>
<p>Security=SSPI;</p>
</blockquote></td>
<td><blockquote>
<p>Connection string for the connection to the BMS_AUTHZ database.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/ system.serviceMod el/services/service/</p>
<p>host/baseAddresse s/add</p>
</blockquote></td>
<td><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS</p>
</blockquote></td>
<td><blockquote>
<p>STS service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="10"></td>
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>baseAddress</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/authsvc</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>Authsvc service endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>system.serviceMod</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>el/services/service/</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>system.serviceMod el/bindings/ wsFederationHttpBi nding/binding/securi</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/mex</p>
</blockquote></td>
<td><blockquote>
<p>STS metadata exchange URL used by ServiceBinding.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>system.serviceMod el/bindings/ wsFederationHttpBi nding/binding/securi ty/message/issuer</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/ Windows</p>
</blockquote></td>
<td><blockquote>
<p>URL of STS used by WindowsBinding.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>system.serviceMod</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>el/bindings/ wsFederationHttpBi nding/binding/securi ty/message/issuer/i dentity/userPrincipal Name</p>
</blockquote></td>
<td><blockquote>
<p>value</p>
</blockquote></td>
<td><blockquote>
<p><a href="mailto:VAUser@domain.com">VAUser@domain.com</a></p>
</blockquote></td>
<td><blockquote>
<p>Name of the user under which the service is running.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><strong>Configuration values (ex.)</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/ system.serviceMod el/behaviors/service</p>
<p>Behaviors/behavior/</p>
<p>serviceMetadata</p>
</blockquote></td>
<td><blockquote>
<p>httpGetUrl</p>
</blockquote></td>
<td>http://<em>vaserver</em>:<em>17050</em>/STS/mex</td>
<td><blockquote>
<p>Metadata exchange address of ServiceSTSBehavior.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark19" class="anchor"></span>Table 11-Win ServiceHost Configuration Parameters

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Section</strong></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>LocalServer UseSecurityContext AuditProtocol</p>
</blockquote></td>
<td><blockquote>
<p>yes/no 0/1 none/udp</p>
</blockquote></td>
<td><blockquote>
<p>ePractice remoting flag. Only used with yes.</p>
<p>Flag which specifies if ePractice uses the security context.</p>
<p>Transfer protocol to communicate with the audit service or none if not used.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>ServiceStartupTimeoutSecondsAdd</p>
</blockquote></td>
<td><blockquote>
<p>90</p>
</blockquote></td>
<td><blockquote>
<p>Time in seconds to wait for the services to start</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>AuditServer</p>
</blockquote></td>
<td><blockquote>
<p>auditserver</p>
</blockquote></td>
<td><blockquote>
<p>Server where the audit service resides.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WinServiceHost.</p>
</blockquote></td>
<td>configuration/</td>
<td><blockquote>
<p>AuditPort</p>
</blockquote></td>
<td><blockquote>
<p>10000</p>
</blockquote></td>
<td><blockquote>
<p>Port of the audit service on the specified server.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>exe.config</p>
</blockquote></td>
<td><blockquote>
<p>appSettings/</p>
<p>key</p>
</blockquote></td>
<td><blockquote>
<p>ServiceCertificateStoreName</p>
</blockquote></td>
<td><blockquote>
<p>My</p>
</blockquote></td>
<td><blockquote>
<p>Specifies the name of the X.509 certificate</p>
<p>store to open.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>ServiceCertificateStoreLocation</p>
</blockquote></td>
<td><blockquote>
<p>LocalMachine</p>
</blockquote></td>
<td><blockquote>
<p>Specifies the location of the X.509 services' certificate store.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p><span id="_bookmark20" class="anchor"></span>ServiceCertificateFindType</p>
</blockquote></td>
<td><blockquote>
<p>FindBySubjectName</p>
</blockquote></td>
<td><blockquote>
<p>Specifies the type of value the X509Certificate2Collection.Find method</p>
<p>searches for.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>ServiceCertificateFindValue</p>
</blockquote></td>
<td><blockquote>
<p>IWHM3Services</p>
</blockquote></td>
<td><blockquote>
<p>Services' Certificate name.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark21" class="anchor"></span>Table 12-WMI User Group Configuration Parameters

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>WMI_UserGroup. exe</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>configuration/ appSettings/ key</p>
</blockquote></td>
<td><blockquote>
<p>DatasetPath</p>
</blockquote></td>
<td><blockquote>
<p>DBRepository</p>
</blockquote></td>
<td><blockquote>
<p>Data Adapters (XML mapping files) path.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LocalMachineName</p>
</blockquote></td>
<td><blockquote>
<p>Localhost</p>
</blockquote></td>
<td><blockquote>
<p>Name of the host where WMI_UserGroup will run.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IsRunningOnLocalMachine</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td><blockquote>
<p>Specify if WMI_UserGroup will run on</p>
<p>local machine or not.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Connections.xml</p>
</blockquote></td>
<td><blockquote>
<p>MyConnections/ MyConnection/ ConnectionString</p>
</blockquote></td>
<td><blockquote>
<p>ConnectionString</p>
</blockquote></td>
<td><blockquote>
<p>packet size=4096;data source= <em>vadbserver\sql2008r2</em>;persist security info=False;Initial Catalog=BMS_DW;Integrated Security=SSPI;connection timeout</p>
<p>= 600</p>
</blockquote></td>
<td><blockquote>
<p>Connection string for the connection to the BMS_DW database.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark22" class="anchor"></span>Table 13-Policy Manager Configuration Parameters

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td rowspan="3"><blockquote>
<p>configuration/ appSettings/ key</p>
<p>configuration/</p>
</blockquote></td>
<td><blockquote>
<p>DefaultResourceRoot AuditProtocol AuditServer AuditPort</p>
</blockquote></td>
<td><blockquote>
<p>VA</p>
<p>none/udp auditserver 10000</p>
</blockquote></td>
<td><blockquote>
<p>Default root for identifiers.</p>
<p>Transfer protocol to communicate with the audit service or none if not used.</p>
<p>Server where the audit service resides.</p>
<p>Port of the audit service on the specified server.</p>
</blockquote></td>
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
<td><blockquote>
<p>system.serviceMod el/bindings/wsFeder ationHttpBinding/bin ding/security/messa</p>
<p>ge/issuer</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/</p>
</blockquote></td>
<td><blockquote>
<p>STS address used by wsFederationBinding binding</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Section</strong></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PolicyManager.exe.</p>
<p>config</p>
</blockquote></td>
<td><blockquote>
<p>configuration/ system.serviceMod el/behaviors/</p>
<p>endpointBehaviors/</p>
<p>behavior/ clientCredentials/ scopedCertificates/</p>
<p>add</p>
</blockquote></td>
<td><blockquote>
<p>targetUri</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/</p>
</blockquote></td>
<td><blockquote>
<p>STS address of STS certificate.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PAP</p>
</blockquote></td>
<td><blockquote>
<p>PAP client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>client/endpoint</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ AuthorizationPublisher</p>
</blockquote></td>
<td><blockquote>
<p>AuthorizationPublisher client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PolicyEditor.dll. config</p>
</blockquote></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/ client</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PAP</p>
</blockquote></td>
<td><blockquote>
<p>PAP client endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark23" class="anchor"></span>Table 14-BMS Web Configuration Parameters

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Web.config</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>configuration/ appSettings/</p>
</blockquote></td>
<td><blockquote>
<p>webpages:Version</p>
</blockquote></td>
<td><blockquote>
<p>1.0.0.0</p>
</blockquote></td>
<td><blockquote>
<p>Version of the web site.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ClientValidationEnabled</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td><blockquote>
<p>Gets or sets a value that indicates</p>
<p>whether client-side validation is enabled.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="4"></td>
<td rowspan="4"><blockquote>
<p>key</p>
</blockquote></td>
<td><blockquote>
<p>UnobtrusiveJavaScriptEnabled</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td><blockquote>
<p>Gets or sets a value that indicates</p>
<p>whether unobtrusive JavaScript is enabled.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ReportsPath</p>
</blockquote></td>
<td><blockquote>
<p>/BMS</p>
</blockquote></td>
<td><blockquote>
<p>Path of the reports in the reporting</p>
<p>services.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.EVSDictionaryCacheSize</p>
</blockquote></td>
<td><blockquote>
<p>512</p>
</blockquote></td>
<td><blockquote>
<p>Cache size for the vocabulary service,</p>
<p>representing the number of concepts cached.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VAURL</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://vaww.esm.infoshare.va.gov/">http://vaww.esm.infoshare.va.gov/</a> PMIC/Projects/BMS/</p>
<p>Implement/default.aspx</p>
</blockquote></td>
<td><blockquote>
<p>BMS Sharepoint Site.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="11"></td>
<td rowspan="11"></td>
<td><blockquote>
<p>TICKETURL</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://vaww.esm.infoshare.va.gov/">http://vaww.esm.infoshare.va.gov/</a> PMIC/Projects/BMS/ Implement/HDProcess/</p>
<p>default.aspx</p>
</blockquote></td>
<td><blockquote>
<p>Enter a defect and enhancement ticket.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WhiteboardRefreshRate</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>Time in seconds of refresh rate of the whiteboard page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>THRESHOLD</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>Threshold value used to compare wait time value of the patient from the Patients Pending Placement List in order to display an alert on the Patients Pending</p>
<p>Placement List.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>aspnet:MaxHttpCollectionKeys</p>
</blockquote></td>
<td><blockquote>
<p>2000</p>
</blockquote></td>
<td><blockquote>
<p>Maximum number of aps.net collection</p>
<p>keys.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WhiteboardAjaxRefreshRate</p>
</blockquote></td>
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>Time in seconds of AJAX refresh rate of</p>
<p>the whiteboard page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WhiteboardRealRefreshRate</p>
</blockquote></td>
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>Time in minutes of standard refresh rate</p>
<p>of the whiteboard page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HomePageRefreshRate</p>
</blockquote></td>
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>Time in seconds of refresh rate of the</p>
<p>home page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_EIS_GET_ENTITY_</p>
<p>FILTR_PAGE_SIZE</p>
</blockquote></td>
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>Number of records queried that are brought from EIS in one page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_EVS_GET_CONCEPT_</p>
<p>PAGE_SIZE</p>
</blockquote></td>
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>Number of records queried that are brought from EVS in one page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SmtpHost</p>
</blockquote></td>
<td><blockquote>
<p>VA_MAIL_SERVER</p>
</blockquote></td>
<td><blockquote>
<p>Mail Server host.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DisplayDetailedErrorMessage</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td><blockquote>
<p>If set to true displays detailed error message, otherwise displays a generic</p>
<p>message ("Please contact BMS administrator.").</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td rowspan="2"></td>
<td><blockquote>
<p>Is_IIS_Single_Instance</p>
</blockquote></td>
<td><blockquote>
<p>true/false</p>
</blockquote></td>
<td><blockquote>
<p>If set to true a single IIS instance is used.</p>
<p>If set to false multiple IIS instances are used (web farm scenario).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ProxyPoolMaxCount</p>
</blockquote></td>
<td><blockquote>
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>The maximum number of proxies in the</p>
<p>pool.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>MdwsEndpointUrl_1</p>
</blockquote></td>
<td><blockquote>
<p>http://mdws_server:81/ QuerySvc.asmx</p>
</blockquote></td>
<td><blockquote>
<p>MDWS instance URL address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MdwsEndpointUrl_2</p>
</blockquote></td>
<td><blockquote>
<p>http://mdws_server:82/</p>
<p>QuerySvc.asmx</p>
</blockquote></td>
<td><blockquote>
<p>MDWS instance URL address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="8"></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>bindings/ wsFederationHttpBi nding/binding/securi</p>
<p>ty/message/issuer</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/ Windows</p>
</blockquote></td>
<td><blockquote>
<p>STS Windows address used by WindowsBinding.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>bindings/ wsFederationHttpBi nding/binding/securi</p>
<p>ty/message/issuer</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/STS/</p>
</blockquote></td>
<td><blockquote>
<p>STS address used by WSFederationHttpBinding_Authenticated Service binding.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/authsvc/ upnidentity</p>
</blockquote></td>
<td><blockquote>
<p>Security Authentication client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/RS</p>
</blockquote></td>
<td><blockquote>
<p>Reporting Services client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ QueryFunctions</p>
</blockquote></td>
<td><blockquote>
<p>EIS QueryFunctions client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ QueryFunctions</p>
</blockquote></td>
<td><blockquote>
<p>EIS QueryFunctions Windows authentication client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ EntityManagement</p>
</blockquote></td>
<td><blockquote>
<p>EIS EntityManagement client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/</p>
<p>EntityManagement</p>
</blockquote></td>
<td><blockquote>
<p>EIS EntityManagement Windows authentication client endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><blockquote>
<p>client/endpoint</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PAP</p>
</blockquote></td>
<td><blockquote>
<p>PAP client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PAP</p>
</blockquote></td>
<td><blockquote>
<p>PAP Windows authentication client endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PDP</p>
</blockquote></td>
<td><blockquote>
<p>PDP client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/PDP</p>
</blockquote></td>
<td><blockquote>
<p>PDP Windows authentication client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSVocabularyRuntime</p>
</blockquote></td>
<td><blockquote>
<p>CTS VocabularyRuntime client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSVocabularyBrowse</p>
</blockquote></td>
<td><blockquote>
<p>CTS VocabularyBrowse client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSMessageBrowse</p>
</blockquote></td>
<td><blockquote>
<p>CTS MessageBrowse client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSMessageRuntime</p>
</blockquote></td>
<td><blockquote>
<p>CTS MessageRuntime client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSMessageEdit</p>
</blockquote></td>
<td><blockquote>
<p>CTS MessageEdit client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ CTSVocabularyEdit</p>
</blockquote></td>
<td><blockquote>
<p>CTS VocabularyEdit client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste</p>
<p>m.serviceModel/ client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ BMSConfigurationOperations</p>
</blockquote></td>
<td><blockquote>
<p>BMS ConfigurationOperations client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ BMSConfigurationOperations</p>
</blockquote></td>
<td><blockquote>
<p>BMS ConfigurationOperations Windows authentication client endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 25%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration key</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Configuration values (ex.)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ BMSQuery</p>
</blockquote></td>
<td><blockquote>
<p>BMS Query client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ BMSOperations</p>
</blockquote></td>
<td><blockquote>
<p>BMS Operations client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ TransferWF</p>
</blockquote></td>
<td><blockquote>
<p>Transfer workflow client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ BMSWF</p>
</blockquote></td>
<td><blockquote>
<p>BMS workflow client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ WaitingListWF</p>
</blockquote></td>
<td><blockquote>
<p>Patients Pending Placement List workflow client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ BedCleanWF</p>
</blockquote></td>
<td><blockquote>
<p>Bed clean workflow client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ BedUnavailableWF</p>
</blockquote></td>
<td><blockquote>
<p>Bed Unavailable workflow client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ VistaQuery</p>
</blockquote></td>
<td><blockquote>
<p>VistA Query client endpoint address.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>configuration/syste m.serviceModel/</p>
<p>client/endpoint</p>
</blockquote></td>
<td><blockquote>
<p>address</p>
</blockquote></td>
<td><blockquote>
<p>http://<em>vaserver</em>:<em>17050</em>/ VistaQuery</p>
</blockquote></td>
<td><blockquote>
<p>VistA Query Windows authentication client endpoint address.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Scheduled Windows and SQL Jobs Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS runs one Windows Scheduled task: BMS – WMI_UserGroup and two SQL Jobs in order to bring data into the data warehouse (BMS_DW database): BMS - Reports Full and BMS – Reports Incremental. More information about BMS databases can be referenced from [<u>Section 3.3</u>.](#database-architecture)

### BMS Reports Full

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bed-management-solution-version-2-4-technical-manual/003.png)

> <span id="_bookmark26" class="anchor"></span>Figure 2-BMS-Report Full Job

> The job's steps can be seen in the figure above and most of them execute stored procedures. At the beginning of the process, the operations are done between the source databases and the destination database, which is BMS_DS in our case.

> Each step is described below:

> Step 1. Start job full: this is only an informative step for the log file.

> ![](bed-management-solution-version-2-4-technical-manual/004.png)

> <span id="_bookmark27" class="anchor"></span>Figure 3-BMS-Start Full Job

> Step 2. Check state job incremental: it checks the state of the BMS incremental and attempts to stop the incremental job.

> ![](bed-management-solution-version-2-4-technical-manual/005.png)

> <span id="_bookmark28" class="anchor"></span>Figure 4-BMS-Check State Job Incremental

> Step 3. Waits 1 min for incremental job to stop:

> ![](bed-management-solution-version-2-4-technical-manual/006.png)

> <span id="_bookmark29" class="anchor"></span>Figure 5-BMS-Waits 1 Min for Incremental Job to stop

> Step 4. Disable Incremental Job:

> ![](bed-management-solution-version-2-4-technical-manual/007.png)

> <span id="_bookmark30" class="anchor"></span>Figure 6-BMS-Check State Job Incremental

> Step 5. Call stored procedure sp_infoworld_pachet_full_BMS_AUTHZ:

> ![](bed-management-solution-version-2-4-technical-manual/008.png)

> <span id="_bookmark31" class="anchor"></span>Figure 7-BMS-Job Step Properties

> Step 6. Call stored procedure sp_infoworld_pachet_full_BMS

> ![](bed-management-solution-version-2-4-technical-manual/009.png)

> <span id="_bookmark32" class="anchor"></span>Figure 8- BMS- Job Step Properties-Call Stored Procedure

> Step 7. Call stored procedure sp_infoworld_pachet_full_BMS_EIS

> ![](bed-management-solution-version-2-4-technical-manual/010.png)

> <span id="_bookmark33" class="anchor"></span>Figure 9- BMS-Job Step Properties-Call Stored Procedure_SP_Infoworld

> Step 8. Call stored procedure sp_infoworld_pachet_full_BMS_EVS

> ![](bed-management-solution-version-2-4-technical-manual/011.png)

> <span id="_bookmark34" class="anchor"></span>Figure 10-BMS-Job Step Properties_BMS EVS

> Step 9. Clear/Load DW Data, call usp_ETL_ProcessFull_VOCAB

> ![](bed-management-solution-version-2-4-technical-manual/012.png)

> <span id="_bookmark35" class="anchor"></span>Figure 11-BMS- Job Step Procedures-VOCAB

> Step 10. Call stored procedure usp_ETL_ProcessFull_FACTS

> ![](bed-management-solution-version-2-4-technical-manual/013.png)

> <span id="_bookmark36" class="anchor"></span>Figure 12-BMS-Job Step Procedurs-ETL_Processfull_Facts

> Step 11. Copy users in history database

> ![](bed-management-solution-version-2-4-technical-manual/014.png)

> <span id="_bookmark37" class="anchor"></span>Figure 13- BMS- Copy User in history database

> Step 12. Clear DS data

> ![](bed-management-solution-version-2-4-technical-manual/015.png)

> <span id="_bookmark38" class="anchor"></span>Figure 14- Clear DS data

> Step 13. On Success Re-enable Incremental

> ![](bed-management-solution-version-2-4-technical-manual/016.png)

> <span id="_bookmark39" class="anchor"></span>Figure 15-BMS-Re-enable Incremental

> Step 14. On Fail Re-enable Incremental

> ![](bed-management-solution-version-2-4-technical-manual/017.png)

> <span id="_bookmark40" class="anchor"></span>Figure 16-On Fail Re-enable Incremental

> Step 15. Shrink BMS_DS: Shrinks the file with the id 2 (the log file, to the size of 1 MB.

> ![](bed-management-solution-version-2-4-technical-manual/018.png)

> <span id="_bookmark41" class="anchor"></span>Figure 17-BMS-Shrink

> Step 16. Clear data from BMS_DW: the data warehouse database is cleared, meaning that its tables will become empty, but of course exceptions can exist and they really do - tables that contain static data and should not be removed. Thus, the database becomes ready to receive all the source data.

> ![](bed-management-solution-version-2-4-technical-manual/019.png)

> <span id="_bookmark42" class="anchor"></span>Figure 18-BMS-Clear Data

> Step 17. Call procedure full on BMS_DW: it inserts first the vocabulary data, then EIS entities (ETL dimension tables) and BMS acts (ETL facts tables).

> ![](bed-management-solution-version-2-4-technical-manual/020.png)

> <span id="_bookmark43" class="anchor"></span>Figure 19- BMS-Call Procedure Full

> Step 18. Copy users in history database: adds users in user in the table from BMS History database. This step is needed because some reports need to display users that did certain insert/update/delete operations in the application.

> ![](bed-management-solution-version-2-4-technical-manual/021.png)

> <span id="_bookmark44" class="anchor"></span>Figure 20- Copy Users in History Database

> For each step a log file can be set, see screenshot below for step 7:

> ![](bed-management-solution-version-2-4-technical-manual/022.png)

> <span id="_bookmark45" class="anchor"></span>Figure 21-BMS Reports Full Path File Log

> The job can be run by right clicking on the job and then choosing "Start job at step…", selecting the first job in the appearing window and then hitting the Start button. Then a smaller window remains open, showing the progress of the execution and its result: success or failure. The detailed results can be found in the log file that you set at the installation phase. If an operation fails at any step, the job will quit. This setting can be changed in the step's *Advanced* tab.

> Step 19. Clear data from BMS DS database.

> ![](bed-management-solution-version-2-4-technical-manual/023.png)

> <span id="_bookmark46" class="anchor"></span>Figure 22- Clear Data from DS

> Step 20. This step is only invoked if any of the prior steps of the BMS Report Full job fail. Once invoked, email notification of the failure is sent to the BMS Technical team and BMS Report Full job is restarted.

> ![](bed-management-solution-version-2-4-technical-manual/024.png)

> <span id="_bookmark47" class="anchor"></span>Figure 23-BMS Start Job and Send Email

### BMS Incremental

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS Incremental logic is to keep the BMS_DW database up to date without having to delete all the existing data. The following picture shows the job's steps.

> ![](bed-management-solution-version-2-4-technical-manual/025.png)

> <span id="_bookmark49" class="anchor"></span>Figure 24- BMS- Report Incremental Job

> Step 1. Start job incremental: this is only an informative step for the log file.

> ![](bed-management-solution-version-2-4-technical-manual/026.png)

> <span id="_bookmark50" class="anchor"></span>Figure 25-BMS-STart Job Incremental

> Step 2. Check state job full: it checks the state of the BMS full job described above in order to be sure that it is not currently running, in which case the incremental job cannot continue.

> ![](bed-management-solution-version-2-4-technical-manual/027.png)

> <span id="_bookmark51" class="anchor"></span>Figure 26-BMS-Check State Job Full

> Step 3. Call procedure sp_infoworld_incremental_package: makes all the necessary updates from the source databases to the BMS_DS database. When rows are deleted in the source tables, an update is made in BMS_DS database (in the necessary tables) by changing a flag column's value to 1 (deleted) from 0 (existing).

> ![](bed-management-solution-version-2-4-technical-manual/028.png)

> <span id="_bookmark52" class="anchor"></span>Figure 27-BMS-Call Procedure Properties

> Step 4. Call procedure incremental DW: will search for any new, updated or deleted row in BMS_DS database's tables in order to do the correspondent operations in its tables.

> ![](bed-management-solution-version-2-4-technical-manual/029.png)

> <span id="_bookmark53" class="anchor"></span>Figure 28-BMS-Call Procedure Incremental

> For each step a log file can be set, see screenshot below for step 4:

> ![](bed-management-solution-version-2-4-technical-manual/030.png)

> <span id="_bookmark54" class="anchor"></span>Figure 29- BMS Incremental Path File Log

> Step 5. If the duration of the last completed incremental job exceeded 3 minutes, then recalculate statistics to improve query plan execution for the next job run.

> ![](bed-management-solution-version-2-4-technical-manual/031.png)

> <span id="_bookmark55" class="anchor"></span>Figure 30- BMS-Call Procedure Recalculate Statistics

### BMS Reports Windows Management Instrumentation (WMI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This job runs a process through Windows Task Scheduler "BMS - Execute WMI_UserGroup" that takes all the users and user groups from the Active Directory and inserts them in BMS_DW database.

> In order to run the process successfully, the user needs to configure WMI_UserGroup.config file (Reference [Table 12 - WMI User Group Configuration Parameters](#_bookmark20)) and set the connection of the database in the Connections.xml file. These files are stored in the folder where WMI_UserGroup application is installed.

> The steps performed by this process include the following:

> Below are the steps:

1.  Deletes from the following tables from the BMS_DW database: dbo.DOMAIN_USER_GROUP

> dbo.DIM_DOMAIN_USER dbo.DIM_DOMAIN_GROUP

2.  Inserts the domain groups (all) into dbo.DIM_DOMAIN_GROUP table
3.  Inserts the users (all) into the dbo.DIM_DOMAIN_USER table
4.  Inserts the users group information into the dbo.DOMAIN_USER_GROUP table.
    1.  Here it determines who belongs to what group and adds them, since a single user can belong to many groups
5.  Writes the log messages
6.  Closes the connections
7.  Exits

> Windows Task Scheduler calls a Batch script D:\BMS\Data\WMI_UserGroup\WMI_Wrapper.BAT The script sets up some variables for Log Files. The 'Start' time is recorded in a variable then calls the

> WMI_UserGroup binary file. After the execution of the binary file the 'End' time is recorded. Calculations for the duration are done between the 'Start' and 'End' times, the metrics is sent to Introscope via a batch script which calls a Powershell script to send the Data. If the 'Duration' was less than 8 minutes, the base wrapper script is called again with an additional parameter of "2" added ( Second run ).

> Introscope records the 'Duration' and 'Exit' Results of the binary executable. If the second run also fails to complete with a duration longer than 8 minutes, email alerts are sent via the Introscope rules engine.

## Ward Whiteboard Kiosk Mode Display Configuration (BMS Whiteboard Kiosk Setup)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An electronic kiosk (or computer kiosk) houses a computer terminal designed to function while preventing users from accessing system functions. BMS has adopted the use of electronic kiosks to provide sites with the capability to setup Large Screen Displays for the BMS Ward Whiteboard for greater visibility. The Whiteboard Kiosk is read only access page that presents an overview of the beds in the current facility (or in the selected ward) and allows the user to assess at a glance the bed availability in their facility (or ward).

> Kiosk mode locks down the user interface to protect applications from accidental or deliberate misuse. These displays should be placed carefully, considering that confidential patient data (Social Security Number) should not be in view of people who are not authorized to see it.

![](bed-management-solution-version-2-4-technical-manual/032.png)

> <span id="_bookmark58" class="anchor"></span>Figure 31- BMS Ward Whiteboard Screen

> Setting up for the BMS Whiteboard Kiosk involves a series of steps that most often are performed by IT staff with access to Local Site network configuration and/or staff with authority to request the required Local Site and Active Directory (AD) network configuration changes.

> Steps for configuring the BMS Whiteboard Kiosk can be divided into three major categories:

- <span id="_bookmark59" class="anchor"></span>The Ward Whiteboard Kiosk URL
- The Network User for BMS Kiosk Access
- The Kiosk Workstation for Local Site Use

> Each category involves a series of required steps to ensure successful operation of the Kiosk. Following is an outline of the process to setup and configure the BMS Whiteboard Kiosk for a local site.

1)  *<u>Create the Ward Whiteboard Kiosk URL. See details in</u> [2.5.1 Create the Ward Whiteboard Kiosk URL](#_bookmark59)*
    1.  Determine the BMS Whiteboard Parameters for Kiosk Operation and Setup
    2.  Test the URL in a browser
2)  *<u>Set up a default user for the kiosk. See details in</u> [2.5.2 Set up a default user for the BMS Kiosk](#set-up-a-default-user-for-the-bms-kiosk)*
    1.  Set up the Network User for BMS Access
    2.  Configure the Whiteboard Kiosk Default Login User in BMS
    3.  Assign a Role to the Whiteboard Kiosk Default User in BMS
3)  *<u>Set up the Workstation / Kiosk Machine. See details in</u> [2.5.3 Set up the Workstation / Kiosk Machine](#set-up-the-workstation-kiosk-machine)*
    1.  Disable the Screen Saver
    2.  Configure the Power Settings to Disable Sleep and Stand by Mode
    3.  Configure Auto Log in Option and stop MS Lync from opening upon start up
    4.  Set the URL as the Home Page in IE
    5.  Add [https://REDACTED.va.gov](https://vaww.bms.va.gov/) to "Trusted Sites" in IE
    6.  Add to the start-up commands (Windows) the launch of the browser
    7.  Close IE, and restart to test
    8.  Set Registry Keys to configure Kiosk for local Site use

### Create the Ward Whiteboard Kiosk URL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Ward Whiteboard display uses parameters to determine the behavior of the display. For example, the whiteboard can display a specific ward or ALL wards for a site by setting the parameter wardName. Below is a description for each whiteboard display parameter along with available options for each.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 48%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Parameter</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Short Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Options</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>facilityCode</p>
</blockquote></td>
<td><blockquote>
<p>Code of facility (e.g., BROCKTON = BRK).</p>
</blockquote></td>
<td><blockquote>
<p>Enter the 3 character facility ID.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>wardName</p>
</blockquote></td>
<td><blockquote>
<p>Name of BMS Ward Name. To see all the wards the value that needs to be configured is ALL.</p>
</blockquote></td>
<td><blockquote>
<p>These are the BMS WARDS as defined in the Facility, Site Options, VistA Ward Add/Edit. The Ward name value should match the "BMS WARD GROUP TEXT". A single ward can be entered or the value "ALL" to display all the wards at the facility.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>splitScreen</p>
</blockquote></td>
<td><blockquote>
<p>To split the page in two tables enters the value "Yes".</p>
</blockquote></td>
<td><blockquote>
<p>Yes No</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>displayPTCode</p>
</blockquote></td>
<td><blockquote>
<p>How the patient should be displayed under the column "Patient" (full name or 1st+Last 4) or LastName. <strong>LastName is required for Kiosk mode due to Privacy regulations.</strong></p>
</blockquote></td>
<td><blockquote>
<p>FirstAndLast4</p>
<p><strong>LastName</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>genderColorCode</p>
</blockquote></td>
<td><blockquote>
<p>To change the background color for the row according with patient's gender.</p>
</blockquote></td>
<td><blockquote>
<p>Blue/Pink None</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>displayFooterCensus</p>
</blockquote></td>
<td><blockquote>
<p>To view the footer census.</p>
</blockquote></td>
<td><blockquote>
<p>Yes No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>displayStaffAttending</p>
</blockquote></td>
<td><blockquote>
<p>What column is displayed in the table? (Staff column, Attending column or both).</p>
</blockquote></td>
<td><blockquote>
<p>Staff and Attending Staff</p>
<p>Attending</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>scrollRate</p>
</blockquote></td>
<td><blockquote>
<p>The timer interval will affect the scrolling speed. This parameter can be absent. (If specified then it represents seconds).</p>
</blockquote></td>
<td><blockquote>
<p>Null or an integer value.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark61" class="anchor"></span>Table 15-Ward Whiteboard URL Configuration Parameters

#### Determine the parameters for the Kiosk, and create the URL

> Sample URL to display All Wards for site BRK:

> <u>https://REDACTED.va.gov/WardWhiteboardUrl?facilityCode=BRK&wardName=ALL&s</u> <u>plitScreen=No&displayPTCode=LastName&genderColorCode=Blue/Pink&displayFoo</u> <u>terCensus=Yes&displayStaffAttending=Staff%20and%20Attending&scrollRate=20</u>

#### Test the URL

> Once you have the URL, type it into a browser to test. The BMS Ward Whiteboard should come up. Note: a site can have a different URL for each kiosk.

### Set up a default user for the BMS Kiosk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create a network service account for accessing the BMS page. Make sure that it is in an Organizational Unit (OU) that will not get the Enterprise System Engineering (ESE) Federal Desktop Core Configuration (FDCC) / US Government Configuration Baseline (USGCB) User Settings. Set the "Log on to" so the account can only log onto the kiosk PC you are setting up.

#### Set up the Network User for BMS Access

- Create AD User with non-expiring password under Service Accounts for the local site. If you are not an AD administrator then provide the following instruction to the AD along with your request for a new service account.

> In Active Directory Create a Generic User with a Non-Expiring password in Service Accounts for your location with Access to All Computers.

> NOTE: You will create a single ID, not one for every PC. Also, do not setup auto login with this generic account at this point as PCs will automatically lock at this level.

- Right click the "Service Accounts" folder (VXX.med.va.gov/VISNxx/Facility(XXX)/Service Accounts) and select New…User.

> NOTE: Do not use the "Service Accounts" folder directly under vXX.med.va.gov. Under First Name, enter vhaXXX (such as vhaSTLBMSUser)

- Enter the same under "User Login Name"
- Enter a password when prompted and select
- Uncheck "User must change password at next logon"
- Check "Password never expires"
- Click "OK" at the warning that the user will not be prompted to change the password.
- Click "Next"
- At the top of the screen the path should read, "vXX.med.va.gov/VISNxx/Facility(XXX)/Service Accounts"
- Uncheck "Create an Exchange Mailbox"
- Click "Next"
- Review confirmation screen for accuracy and click "Finish".
- Your new account should be available in your "Service Accounts" list. You may have to refresh your list to

> see it.

- Double-click your new account, in the description field, add
- SERVICE ACCOUNT: VHAxxxxxxxx(YourUserName): BMS DISPLAY
- In the Account tab, ensure "This user can log on to "All computers". Do not identify any specific

> computers.

- When you are finished, your new account in the Service Accounts list should only show a Name, Type, and Description. All other fields should be blank.

#### Configure the Whiteboard Kiosk Default Login User in BMS

> For the current facility that will display the associated Whiteboard page, a default user needs to be configured in BMS application for the Ward Whiteboard Kiosk.

> To configure the Whiteboard Kiosk Default User:

- *Go to the BMS Site Home Page*
- *Click on the Site Options link*
- *Click on the Facility Setting link*
- *Fill the fields "Whiteboard Kiosk Default User Name:", "Whiteboard Kiosk Password:" and "Whiteboard Kiosk Password Confirm:" with the BMS Service Account ID*

![](bed-management-solution-version-2-4-technical-manual/033.png)

> <span id="_bookmark63" class="anchor"></span>Figure 32-Facility Settings

- *Click Submit*

#### Assign a Role to the Whiteboard Kiosk Default User in BMS

> Each facility must assign the BMS "EMS USER" Role to the Service Account ID created to run the Whiteboard Kiosk URL. This assignment can be done from the BMS Admin Section → Add/Edit BMS User hyperlink or Facility Site Options → BMS User Add/Edit hyperlink.

- *Click the Select Existing NT User Name button*
- *Select the correct VISN Domain from the left Drop Down Box.*
- *In the User Name box Enter the BMS Service Account ID created for the BMS EMS/Whiteboard Kiosk. Then click the Find button*
- *Click the Selected Radio button for the user. Then click the Select button.*
- *In the EMS User box, select "Yes". All other roles should be "No".*
- *In the Default Region box, select the correct Region.*
- *In the Default VISN box, select the correct VISN.*
- *In the Default Site box, select your Site.*
- *In the READ Access box, select "Yes".*
- *In the WRITE Access box, select "Yes".*

> ![](bed-management-solution-version-2-4-technical-manual/034.png)

> <span id="_bookmark64" class="anchor"></span>Figure 33- Whiteboard Kiosk User Role Assignment

- *Click Submit*

### Set up the Workstation / Kiosk Machine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After setting up the workstation / Kiosk machine, it will automatically log in to Windows, and automatically login to BMS.

#### Disable Screen Saver

> In order to display the Whiteboard page continuously the screen saver needs to be disabled.

> NOTE: The Windows menu that allows the disable of the screen saver might be different from one version of Windows to another. For example, for Windows 7 the needed operations are:

- *Right click on the desktop*
- *Click Personalize*
- *Click on the screensaver button on the lower-right part of the page*

![](bed-management-solution-version-2-4-technical-manual/035.png)

> <span id="_bookmark66" class="anchor"></span>Figure 34- Screen Saver Option

- *Select None from the screensaver drop down on the displayed form*

> ![](bed-management-solution-version-2-4-technical-manual/036.png)

> <span id="_bookmark67" class="anchor"></span>Figure 35- Screen Saver Settings Window

- *Click OK.*

#### Configure Power Settings: Disable Sleep and Stand-by Mode

> In order to display the Whiteboard page continuously the power settings need to be adjusted so that the computer will never enter into hibernate or stand-by and also the screen will never turn off.

> NOTE: The Windows menu that allows the configuration of the power settings might be different from one version of Windows to another. For example, for Windows 7 the needed operations are:

- *Go To Control Panel*
- *Select Power Options*

> ![](bed-management-solution-version-2-4-technical-manual/037.png)

> <span id="_bookmark68" class="anchor"></span>Figure 36- Power Options

- *Click on "Change Plan settings" for the active plan*

![](bed-management-solution-version-2-4-technical-manual/038.png)

> <span id="_bookmark69" class="anchor"></span>Figure 37- Change Plan Settings Option

- *Select "Never" from the drop downs associated with "Turn off the display" and "Put the computer to sleep"*

> ![](bed-management-solution-version-2-4-technical-manual/039.png)

> <span id="_bookmark70" class="anchor"></span>Figure 38- Power Options Settings

- *Click "Save changes"*

#### Configure Auto-login Option and stop Microsoft Lync from opening upon start up

> Configure Auto-Login: The computer that will display the Whiteboard page needs to have the auto-login configuration set to" true".

> NOTE: The Windows menu that allows the configuration of the auto-login settings might be different from one version of Windows to another. For example, for Windows 7 the needed operations are:

- *Press the Windows key + R on your keyboard to launch the "Run" dialog box.*

![](bed-management-solution-version-2-4-technical-manual/040.png)

> <span id="_bookmark71" class="anchor"></span>Figure 39- Run Window

- *Type in "control userpasswords2"*

![](bed-management-solution-version-2-4-technical-manual/041.png)

> <span id="_bookmark72" class="anchor"></span>Figure 40- Run Window with Comman Entered

- *Press Enter. The User Accounts window will display.*

![](bed-management-solution-version-2-4-technical-manual/042.png)

> <span id="_bookmark73" class="anchor"></span>Figure 41- User Accounts Window

- *Uncheck the option "Users must enter a user name and password to use this computer" for the BMS Default Kiosk User Account*

> ![](bed-management-solution-version-2-4-technical-manual/043.png)

> <span id="_bookmark74" class="anchor"></span>Figure 42- User Accounts

- *Click "OK"*

> Stop Microsoft Lync from opening at startup: To stop Microsoft Lync from opening at startup follow the steps below

- *From the Start Menu,*
- *Go to All Programs \>Microsoft Lync*
- *Open Microsoft Lync*
- *Go to Tools\>Options\>Personal*
- *Uncheck "automatically start Lync when I log on to Windows" & "Show Lync in foreground when it starts".*

#### Set the URL (from step 2.5.1) as the Home Page in Internet Explorer

> The specific Ward Whiteboard Kiosk URL needs to be configured as the Home-Page for the intended browser. The menu to set the default home-page might differ from one browser to another.

> For example, for Internet Explorer (IE) 9.0 the user needs to:

- *Select Tools menu*

> ![](bed-management-solution-version-2-4-technical-manual/044.png)

> <span id="_bookmark75" class="anchor"></span>Figure 43- Tools Menu of Internet Explorer

- *Select Internet Options*
- *On the General tab, under the homepage text field enter the URL*
- *Click OK*

![](bed-management-solution-version-2-4-technical-manual/045.png)

> <span id="_bookmark76" class="anchor"></span>Figure 44- General Tab of Internet Options

#### Add BMS to the "Trusted Sites"

> To add BMS to "Trusted Sites" in Internet Explorer

- *Go to Tools\>Internet Options\>Security\>Trusted sites\>Sites*
- *In the "Add this website to the zone:" field, enter [https://REDACTED.va.gov](https://vaww.bms.va.gov/)*
- *Click Add, Click OK*

#### Add the launch of the browser to the Windows start up commands.

> The next step is to add to the startup commands the launch of the chosen browser.

> NOTE: This operation might differ from one version of Windows to another. For example, for Windows 7 the steps needed are:

- *Click Start*
- *Select All Programs*
- *Right click on the Startup folder*
- *Select Open*

![](bed-management-solution-version-2-4-technical-manual/046.png)

> <span id="_bookmark77" class="anchor"></span>Figure 45- Open Option

- *Create a shortcut of the Internet Explorer and copy it to Startup folder*

> ![](bed-management-solution-version-2-4-technical-manual/047.png)

> <span id="_bookmark78" class="anchor"></span>Figure 46- Internet Explorer Shortcut

#### Test the Kiosk

> Close Internet Explorer. Restart Internet Explorer. The BMS Ward Whiteboard for the Kiosk should come up.

#### Set the Registry Keys to configure the Kiosk for local site use.

> The purpose of the following steps is to configure Kiosk workstation to serve one function only: BMS Ward Whiteboard display. The following instruction leads you through a series of steps that effectively lock down the workstation for this purpose. Access to workstation software and/or desktop will be prevented after the configuration setup is complete. The Whiteboard Kiosk is read only.

> \*It is recommended that prior to performing the configuration steps outlined in this section a backup of the existing system be created for rollback / recovery purposes, and that a restoration point be created.

1)  Modify Registry Settings

#### Restriction.reg

> <span id="_bookmark79" class="anchor"></span>Figure 47-Windows Registry Editor

2)  Run Restrictions.reg by double-clicking filename from Windows Explorer. Verify settings have been applied.
3)  Modify Local Group Policy Settings

> For local group policy changes run gpedit.msc and make the following changes: User Configuration\Administrative Templates\System\Ctrl+Alt+Del Options

> Remove TaskManager Disable

> Remove Lock Computer Enable

> Remove Change Password Enable

> Remove Logoff Enable

> User Configuration\Administrative Templates\Control Panel\Display

> o Password protect the screen saver Disabled

> Verify all settings have been applied. The purpose of these settings is to lock down the workstation for one purpose only, BMS Whiteboard Kiosk.

4)  Reboot Kiosk Machine to test set up.

> \*Note; if Kiosk continually "freezes", please contact the Service Desk to have an IE Refresher script installed.

## Whiteboard Snapshot Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to configure the Whiteboard snapshot certain steps, need to be completed:

1.  Create snapshot folder
2.  Define network share
3.  Assign rights to user
4.  Assign snapshot folder path to ward group
5.  Associate scheduler with the whiteboard report

> Suppose the goal is to configure the settings for two BMS Ward Groups: WARD GROUP 1 and WARD GROUP 2.

> Assuming that these two Ward groups are in different physical locations, a designated workstation will be assigned for each one of them.

> For the purpose of example, these workstations are called: WARDGROUP1-PC and WARDGROUP2- PC.

### Create Snapshot Folder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On WARDGROUP1-PC and WARDGROUP2-PC, a folder should be created for this purpose. For example, assume that this folder is on the "C:" drive, like this "C:\WhiteboardSnapshot".

> *On Windows 7 the needed operations are:*

- Click Start button
- Select All Programs
- Select Accessories folder
- Click Windows Explorer
- Go to C drive
- Right click on C drive
- Select New folder
- ![](bed-management-solution-version-2-4-technical-manual/048.png)Enter the name of the folder, e.g. WhiteboardSnapshot

> <span id="_bookmark82" class="anchor"></span>Figure 48- Whiteboard Snapshot Folder

### Define Network Share

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For these two folders (one on each computer) the Network Admin needs to define network shares. For example, assume that the network share name on each computer is "WhiteboardSnapshot".

> *Note: The Windows menu that allows the configuration of folder sharing might be different from one version of Windows to another. For example, for Windows 7 the needed operations are:*

- *N avigate to the "WhiteboardSnapshot" folder, right-click it and choose Properties*

![](bed-management-solution-version-2-4-technical-manual/049.png)

> <span id="_bookmark84" class="anchor"></span>Figure 49- Whiteboard Snapshot Folder Properties

- ![](bed-management-solution-version-2-4-technical-manual/050.png)*Go to Sharing tab and select Advance Sharing option.*

> <span id="_bookmark85" class="anchor"></span>Figure 50- Advanced Sharing Option

- *In Advanced Sharing dialog, enable Share this folder option. It will automatically add folder's name as Share name.*

![](bed-management-solution-version-2-4-technical-manual/051.png)

> <span id="_bookmark86" class="anchor"></span>Figure 51- Share this Folder Option

### Assign Rights to Master BMS Service Account User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The BMS Application runs under a service account. AICT has created the Windows User (acc\VAAACBMSPrd) as the master service account that the BMS Services runs under. The Windows user (aac\VAAACBMSPrd) that is configured to be the Login that runs the four BMS Windows Services needs to have full rights to these shares.

> This user must have full control on each facilities file folder that is used to store the Whiteboard Contingency Reports.

> *On Windows 7 the needed operations are:*

- *Having Advanced Sharing window open click on Permissions button to set the folder's permissions.*

![](bed-management-solution-version-2-4-technical-manual/052.png)

> <span id="_bookmark88" class="anchor"></span>Figure 52- Permissions for Whiteboard Snapshot

- *In the Permissions window click Add button to set the network user rights on the shared folder.*

![](bed-management-solution-version-2-4-technical-manual/053.png)

> <span id="_bookmark89" class="anchor"></span>Figure 53-Select Users or Groups Window

- *Click "Advanced" button to select user.*

![](bed-management-solution-version-2-4-technical-manual/054.png)

> <span id="_bookmark90" class="anchor"></span>Figure 54- Advanced Section of Select Users or Group Window

- *Enter the name of the user (aac\VAAACBMSPrd) that runs the two BMS Windows Services. Click Find Now button.*

> ![](bed-management-solution-version-2-4-technical-manual/055.png)

> <span id="_bookmark91" class="anchor"></span>Figure 55- Search Result Section

- *Scroll down the Search results section to select the user. Once done, click OK. It will add the user within the object names section.*

![](bed-management-solution-version-2-4-technical-manual/056.png)

> <span id="_bookmark92" class="anchor"></span>Figure 56- Object Names Section

> *Clicking OK will add folder access permission for user and takes you back to Permissions dialog, allowing you to configure the permissions for newly added users.*

![](bed-management-solution-version-2-4-technical-manual/057.png)

> <span id="_bookmark93" class="anchor"></span>Figure 57- Permissions Window

- *Select user, and from Permission*s *section check Full Control*.

> ![](bed-management-solution-version-2-4-technical-manual/058.png)

> <span id="_bookmark94" class="anchor"></span>Figure 58- User Permissions

- ![](bed-management-solution-version-2-4-technical-manual/059.png)*Click Ok to close Permissions window. It will take you back to Advanced Sharing window.*

> <span id="_bookmark95" class="anchor"></span>Figure 59- Advanced Sharing Window

- *Now, click OK to share the folder.*
- *Close Whiteboard Snapshot properties window.*

> Having these two folders shared and having that user given the rights previously mentioned, if someone is logged in the network with that user, he/she could access those folders from Windows Explorer using an URI address. See screenshot below:

![](bed-management-solution-version-2-4-technical-manual/060.png)

> <span id="_bookmark96" class="anchor"></span>Figure 60- WardGroup1-PC Path

### Assign Snapshot Folder Path to Ward Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Within the BMS Application, under Site Settings and then Contingency Settings page, the Admin should enter the values as captured in the screenshot (\\WARDGROUP1-PC\WhiteboardSnapshot for WARD GROUP 1 and respectively \\WARDGROUP2-PC \WhiteboardSnapshot for WARD GROUP 2).

> NOTE: The Windows User (acc\VAAACBMSPrd) must have full read/write access to this folder.

![](bed-management-solution-version-2-4-technical-manual/061.png)

> <span id="_bookmark98" class="anchor"></span>Figure 61-Contingency Settings Page

### Associate Scheduler with Whiteboard Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Within the BMS Application, Facility Home page, under Site Options and then Background Processors page, a Scheduler should be associated in the Whiteboard Report section.

> Under the Whiteboard Report section:

- In the "Add/Update Scheduler:" field, select the schedule frequency that Whiteboard should be backed

> up.

- Click Save Scheduler button.

![](bed-management-solution-version-2-4-technical-manual/062.png)

> <span id="_bookmark100" class="anchor"></span>Figure 62- Whiteboard Report Scheduler Association

## EMS Mobile Device Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to configure the BMS EMS Mobile Devices, the following steps must be completed:

- The local IS must create a local Service Account with a password that never expires and does not change. This account must not have any kind of policy that restricts its use to specific computers. The EMS Mobile Device will use this account to access the EMS Mobile page. This local Service Account can be the same as the Whiteboard Kiosk Default User Account created in Section 2.5.2.
- Each facility must enter the local Service Account and Password in the EMS Default User and Password fields on the Facilities Settings page.
- Configure the Mobile Device so that when it boots up, it will automatically open IE and go to the specified URL.

### Configure EMS Mobile Device Default Login User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For the current facility, a default user must be configured in the BMS application for the EMS Mobile Device. To accomplish this, the Facility Admin User must do the following:

- Go to the Facility Home Page.
- Click on the Site Options link.
- Click on the Facility Setting link.
- Fill the fields "EMS Default User Name:", "EMS Password:", and "EMS Password Confirm:" with the BMS Local Service Account.

> ![](bed-management-solution-version-2-4-technical-manual/063.png)

> <span id="_bookmark103" class="anchor"></span>Figure 63- EMS Fields Filled on the Facility Settings Page

- Click the Submit button.

> <span id="_bookmark104" class="anchor"></span>Table 16-Facility Settings Page Parameters

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EMS Default User Name:</p>
</blockquote></td>
<td><blockquote>
<p>The BMS Service Account ID needed to load the EMS Mobile Page for Mobile Devices.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMS Password:</p>
</blockquote></td>
<td><blockquote>
<p>The BMS Service Account ID password needed to load the EMS Mobile Page for Mobile Devices.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EMS Password confirm:</p>
</blockquote></td>
<td><blockquote>
<p>The confirmation of the password.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This setup can also be completed by the system Support User:

- Go to the BMS Admin Page
- Click on the Edit BMS Facility Settings link
- Click on the Facility Name Drop Down and select the name of the Facility to be configured
- Fill the fields "EMS Default User Name", "EMS Password" and "EMS Password Confirm" with the BMS Local Service Account

> ![](bed-management-solution-version-2-4-technical-manual/064.png)

> <span id="_bookmark105" class="anchor"></span>Figure 64-EMS Fields Filled on the BMS Admin Page

- Click the Submit button

> <span id="_bookmark106" class="anchor"></span>Table 17-BMS Admin Page Parameters

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EMS Default User Name:</p>
</blockquote></td>
<td><blockquote>
<p>The BMS Service Account ID needed to load the EMS Mobile Page for Mobile Devices.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMS Password:</p>
</blockquote></td>
<td><blockquote>
<p>The BMS Service Account ID password needed to load the EMS Mobile Page for Mobile Devices.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EMS Password confirm:</p>
</blockquote></td>
<td><blockquote>
<p>The confirmation of the password.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Configure EMS Mobile Device URL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For the current facility, the EMS Device URL must be configured in the EMS Mobile Device. The URL to be entered has a special format:

> [<u>https://REDACTED.va.gov/EMSMobileLogon?code=BRK</u>.](https://vaww.bms.va.gov/EMSMobileLogon?code=BRK)

> <span id="_bookmark108" class="anchor"></span>Table 18-Description and Configuration for EMS Mobile Device URL Parameters

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 48%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Parameter</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Short Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Options</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Code</p>
</blockquote></td>
<td><blockquote>
<p>Code of facility (e.g. BROCKTON = BRK)</p>
</blockquote></td>
<td><blockquote>
<p>Enter the 3-character facility ID.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> EMS staff can access the BMS Web page for mobile devices at the URL set up by their local IS staff. Be sure to use the code of the facility for which access is needed.

> The following page is displayed:

> ![](bed-management-solution-version-2-4-technical-manual/065.png)

> <span id="_bookmark109" class="anchor"></span>Figure 65-EMS Staff Page for Mobile Devices

## VistA Integration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes the process of importing vocabularies, entities, patient admission, transfer, discharge (ADT) and patient pending bed placement information from VistA.

> In order to integrate with VistA certain steps should be completed:

1.  Choose VistA site
2.  Define Schedulers
3.  Run Scheduler
4.  View Audit Results

### Choose VistA Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Sites tab from Background Processors page of Admin section allows the user to view the list of VA facility sites sharing the same VistA instance and to add a new VA facility to a VistA instance.

#### Adding a New VistA Site

> To add a VA facility site to a VistA instance follow the steps presented below.

1.  From the Background Processors page of Admin section select VistA Sites to display the page in the following image. A list of VA facility sites is displayed in the column to the left of the page.

> ![](bed-management-solution-version-2-4-technical-manual/066.png)

> <span id="_bookmark112" class="anchor"></span>Figure 66-Adding a VistA Site

2.  Click the Add new VistA site link then from the VistA Site area use the Name field to select the code of the site you want to add to the current VistA instance, and then select the Time Zone.

> In the Connections area you can choose between two connection methods: ODBC, MDWS and VIA. Fill in the following data for the ODBC method:

> <span id="_bookmark113" class="anchor"></span>Table 19-New VistA Site Parameters

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Connection String</p>
</blockquote></td>
<td><blockquote>
<p>The connection string for the ODBC method.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>User</p>
</blockquote></td>
<td><blockquote>
<p>The username for the connection.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Password</p>
</blockquote></td>
<td><blockquote>
<p>The password associated to the user account.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MDWS Endpoint</p>
</blockquote></td>
<td><blockquote>
<p>*MDWS available to be selected but no longer supported.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VIA</p>
</blockquote></td>
<td><blockquote>
<p>Select VIA connector.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> You can use the Test Connection buttons to verify the connection and press the Save button to enter the data into the system.

> The newly added site will be added in the sites list to the left of the screen.

### Define Schedulers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Schedulers tab from Background Processors page of Admin section displays a list of schedulers defined by user. It allows the user to add new schedulers, edit or remove old schedulers.

> NOTE: To run the schedulers, the VistA Integration tab must be used (see next section VistA Integration

> for details).

> The Schedulers tab is displayed as in the following image:

![](bed-management-solution-version-2-4-technical-manual/067.png)

> <span id="_bookmark115" class="anchor"></span>Figure 67-Schedulers Tab

#### Adding a New Scheduler

> To add a new scheduler follow the steps presented below.

3.  From the Background Processors page select the Schedulers tab.
4.  In the Schedulers tab fill in the following data:

> <span id="_bookmark116" class="anchor"></span>Table 20-New Scheduler Parameters

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td><blockquote>
<p>The name of the scheduler.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Recurs every</p>
</blockquote></td>
<td><blockquote>
<p>The frequency.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Time Zone</p>
</blockquote></td>
<td><blockquote>
<p>Time zone associated with the scheduler.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Occurs once at/Occurs every</p>
</blockquote></td>
<td><blockquote>
<p>The frequency values.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> After setting the desired frequency for the new scheduler, do not forget to press the Save button to enter the data into the system.

### Run Scheduler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Integration tab is used to run (automatically or manually) the defined schedulers and to select which data categories will be affected by a scheduler's action.

> The VistA Integration tab is displayed as in the following image:

> ![](bed-management-solution-version-2-4-technical-manual/068.png)

> <span id="_bookmark118" class="anchor"></span>Figure 68-VistA Integration Tab

> From the field in the upper part of the page select the VistA site where the scheduler(s) will run. Next step:

- Either click one data category from the column to the left (its name will appear in the Data field) and then select a method and scheduler from the Method and Schedulers fields in the Details area: this will cause the selected scheduler to run at the time set for it in the Schedulers tab and to bring data from the selected category.
- Or select several data categories (using the check-boxes) then select a connection method from the Run Job area, set the Start time/End time and click the Run button: this will cause the scheduler set using the selected method to start running now and bring the data from the selected categories.

### View Audit Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Audit tab displays the results of the operations performed in the VistA Integration tab. The Audit tab is displayed as shown in the following image.

> ![](bed-management-solution-version-2-4-technical-manual/069.png)

> <span id="_bookmark120" class="anchor"></span>Figure 69- Audit Tab

> The options to the left of the page allow the user to determine the filter criteria for the generated audit reports. The options to the right of the screen allow the user to select the type of operation to be captured by the audit report as well as the time interval for the audit.

> After selecting the desired criteria, click the Filter by button to display the page as in the following image.

![](bed-management-solution-version-2-4-technical-manual/070.png)

> <span id="_bookmark121" class="anchor"></span>Figure 70- View Audit Results

> A list of operations is displayed. For each entry the following data is available:

> <span id="_bookmark122" class="anchor"></span>Table 21-View Audit Results Columns Report

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>The VistA site where the audit action has been performed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Method</p>
</blockquote></td>
<td><blockquote>
<p>The method used for connecting to the VistA site.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Data</p>
</blockquote></td>
<td><blockquote>
<p>The type of data retrieved by the VistA integration operation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Rows no</p>
</blockquote></td>
<td><blockquote>
<p>The number of operations of the selected type captured by the audit action.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Start Date</p>
</blockquote></td>
<td><blockquote>
<p>The start date of the retrieval operation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>End Date</p>
</blockquote></td>
<td><blockquote>
<p>The end date of the retrieval operation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Launch Type</p>
</blockquote></td>
<td><blockquote>
<p>The way the audit action has been launched.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Parameters</p>
</blockquote></td>
<td><blockquote>
<p>Audit operation start date and time, and end date and time.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Status</p>
</blockquote></td>
<td><blockquote>
<p>The status of the VistA integration action.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Details</p>
</blockquote></td>
<td><blockquote>
<p>Clicking this link will display the number of entries in the report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## NUMI Integration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes the process of importing patient level of care information from NUMI.

> NUMI connects to VistA for synchronization of patient data using the NUMI Web Service that is part of the Commercial Off the Shelf McKesson product. Authentication to the NUMI Web Service is done by a NUMI supplied secret key.

> ![](bed-management-solution-version-2-4-technical-manual/071.png)NUMI Patient Level of Care transaction involves the following steps: Change patient level of care in NUMI.

> BMS Reader component will detect the patient level of care in NUMI. Patient level of care will be retrieved through a web service method call. BMS Writer component will update patient level of care in BMS database.

### Integration Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are a limited number of configuration parameters for NUMI.

- Secret Key
- Number of sites per call
- Path to NUMI web service

> These configurations are stored in BMS.Service.Host.exe.config The current secret key is: \<authorization key\>

> The number of site per call parameter how many sites will be bundled together in a transaction to NUMI. If this number is increased one should consider the frequency in which the calls are scheduled. Adding more sites will increase the transaction size and length.

> Currently all NUMI servers operate on port 100 at the specified endpoint

> https://\<servername\>.aac.dva.va.gov/Inpatient.asmx*.*

> In order to integrate with NUMI certain steps should be completed:

1.  Choose VistA site
2.  Define Schedulers
3.  Select Scheduler

### Choose VistA Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This step is the same as the one performed on VistA Integration process and can be referenced from [<u>Section 2.7.1</u>.](#choose-vista-site)

### Define Schedulers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The process of defining schedulers can be referenced from Vista Integration process, [<u>Section 2.7.2</u>.](#define-schedulers)

### Select Scheduler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The NUMI tab is used to select the scheduler that will connect to the NUMI server and will retrieve data for a certain VistA site.

> The NUMI tab is displayed as in the following image.

![](bed-management-solution-version-2-4-technical-manual/072.png)

> <span id="_bookmark128" class="anchor"></span>Figure 71-NUMI Tab

> From the Schedulers field select the scheduler created to retrieve the NUMI data then click the Add button: following page is displayed.

![](bed-management-solution-version-2-4-technical-manual/073.png)

> <span id="_bookmark129" class="anchor"></span>Figure 72- Selecting the VistA Site for NUMI data

> Select the VistA site for which the selected scheduler will retrieve NUMI data then press the Save button. Use the Edit link to select a different site for which the scheduler should retrieve NUMI data.

# Application structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Application Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS application consists of the following components:

- BMS Databases (BMS Database, BMS Authz, BMS EIS, BMS EVS, BMS_DS, BMS_DW, BMS InstanceStore and BMS History)
- BMS Services (BMS Service and Win ServiceHost)
  - BMS Service
  - Win Service Host (EIS Service, EVS Service, PAP service, PDP service, RS service and STS service)
- BMS Web Site
- WMI UserGroup

## Application Directory Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS application directory is structured as is presented below:

> +---Consoles

> \| +---PolicyManager

> +---Databases

> \| \\--SQLData

> \| \| \\--Job Logs

> \| \| \\--WMI_UserGroup

> +---Services

> \| +---BMS

> \| \| \\--DBRepository

> \| \| \\--LinqToSql

> \| \| \\--LocalReportWhiteboard

> \| \| \\--Scripts

> \| +---EIS

> \| \| \\--DBRepository

> \| +---EVS

> \| \| \\--DBRepository

> \| +---PAP

> \| \| \\--DBRepository

> \| +---PDP

> \| +---RS

> \| +---Shared

> \| \\--STS

> +---WebSite

> \| +---bin

> \| \| \\-- LocalReportWhiteboard

> \| \| \\-- Scripts

> \| +---Content

> \| \| \\--images

> \| \| +---themes

> \| \| \| +---base

> \| \| \| \| \\--images

> \| +---Reporting

> \| +---ReportsLocal

> \| +---Scripts

> \| \\--Views

## Database Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The BMS Database implementation is comprised of three main parts:

- BMS Database
  - BMS_EVS (Enterprise Vocabulary database)
  - BMS_EIS (Entity Identification Services database)
  - BMS_AUTHZ (Authorization database)
  - BMS (Bed Management database).
  - BMS_History (BMS Transactional History)
  - BMS_InstanceStore (BMS Instances)
- BMS_DS – Data Loaded by an ETL job
- BMS_DW - Data Loaded by an ETL job

> ![](bed-management-solution-version-2-4-technical-manual/074.png)

> <span id="_bookmark134" class="anchor"></span>Figure 73-Database Architecture

## Component Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A list with files for each BMS component is presented below:

> <span id="_bookmark136" class="anchor"></span>Table 22-BMS Database Files

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="11"><blockquote>
<p>Databases\SQLData Databases\SQLData2 Databases\SQLLogs</p>
</blockquote></td>
<td><blockquote>
<p>BMS_Data.mdf</p>
</blockquote></td>
<td rowspan="11"><blockquote>
<p>Database files (BMS database, BMS Authz, BMS EIS, BMS EVS….)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_Data_F.ndf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_Log.ldf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_AUTHZ_Data.mdf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_AUTHZ_Log.ldf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_DS_Data.mdf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_DS_Data_F.ndf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_DS_Log.ldf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_DW_Data.mdf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_DW_Log.ldf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_EIS_Data.mdf</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="10"></td>
<td><blockquote>
<p>BMS_EIS_Data_F.ndf</p>
</blockquote></td>
<td rowspan="10"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_EIS_Log.ldf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_EVS_Data.mdf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_EVS_Data.ndf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_EVS_Log.ldf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_HISTORY_Data.mdf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_HISTORY_Data_F.ndf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_HISTORY_Log.ldf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS_InstanceStore_Data.mdf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_InstanceStore_Log.ldf</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Databases\SQLData\Job_Log s</p>
</blockquote></td>
<td><blockquote>
<p>BMS_Reports_Log.txt</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>BMS Report Full job file log and BMS Incremental job file log.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS_Reports_Log_Incremental.txt</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="9"><blockquote>
<p>Databases\SQLData\WMI_Us erGroup</p>
</blockquote></td>
<td><blockquote>
<p>AdapterRepository.dll</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>Binaries of WMI UserGroup application.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Common.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>connectionConfiguration.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Connections.SingleDatabase.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ContextWriter.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>General.MT.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Infoworld.Configuration.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MiddleTier.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MS.Common.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="7"></td>
<td><blockquote>
<p>MS.Configuration.dll</p>
</blockquote></td>
<td rowspan="7"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MS.Connections.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WMI_UserGroup.exe</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WMI_UserGroup.exe.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WMI_UserGroup.vshost.exe</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WMI_UserGroup.vshost.exe.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WMI_UserGroup.vshost.exe.manifest</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Connections.xml</p>
</blockquote></td>
<td><blockquote>
<p>File used to set the connection to the database.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Databases\SQLData\WMI_Us erGroup\ DBRepository</p>
</blockquote></td>
<td><blockquote>
<p>InfoWorld.WMI_UserGroup.DTO.DTOUse rGroupDomain.xml</p>
</blockquote></td>
<td><blockquote>
<p>XML mapping file which contain mapping definitions between ePractice datasets and SQL tables. The dataset is specified by setting the &lt;MyDataSetInfo&gt; tag. The table to interact with – specified through the</p>
<p>&lt;MyDataTable&gt; tag – is defined by four commands – usually stored procedures – which represent the Create, Read, Update and Delete (CRUD) operations which can be performed on the table: select (Read), insert (Create), update (Update) and delete (Delete). Stored procedure parameters are passed from these datasets and mapped in the same XML file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark137" class="anchor"></span>Table 23-BMS Service Files

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="12"><blockquote>
<p>Services\BMS</p>
</blockquote></td>
<td><blockquote>
<p>AdapterRepository.dll</p>
</blockquote></td>
<td rowspan="12"><blockquote>
<p>The binaries of the BMS Service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AuditTrailSender.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthenticationProxy.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AuthorizationSubscriber.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.Contracts.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.Facade.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.Facade.Contracts.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.Host.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.dll.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.Numi.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.Schedulers.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="9"></td>
<td><blockquote>
<p>BMS.Security.dll</p>
</blockquote></td>
<td rowspan="9"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.ServiceHost.exe</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.ServiceHost.exe.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.ServiceImplementation.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.ServicesWrapper.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.UnitTesting.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.UnitTesting.dll.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.Utils.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.VistaIntegration.dll</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="22"></td>
<td><blockquote>
<p>BMS.VistaIntegration.Cache.dll</p>
</blockquote></td>
<td rowspan="22"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.VistaIntegration.Data.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.VistaIntegration.HL7.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.VistaIntegration.Mdws.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.VistaIntegration.UnitTesting.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.VistaIntegration_Accessor.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.VistaWorker.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.VistaWorker.Reader.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.VistaWorker2.Writer.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.Web.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.WhiteboardReport.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.Workflows.CustomActivities.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.Workflows.PropertyPromotionActivity</p>
<p>.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.Workflows.WF.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Castle.Core.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Common.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>connectionConfiguration.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Connections.SingleDatabase.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ContextWriter.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DataUtil.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FakeItEasy.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>General.MT.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="10"></td>
<td><blockquote>
<p>HL7DataTypes.dll</p>
</blockquote></td>
<td rowspan="10"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IContracts.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICTSEdit.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Infoworld.Configuration.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InterSystems.Data.CacheClient.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>log4net.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mdws2ORM.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Microsoft.Web.Mvc.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MiddleTier.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS.Common.dll</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="11"></td>
<td><blockquote>
<p>MS.Configuration.dll</p>
</blockquote></td>
<td rowspan="11"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS.Connections.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PAPProxy.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RS.Contracts.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Saml20.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SecurityTokenCache.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>trace.log</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tracing.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistASites.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Xacml2.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XacmlCore.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="10"><blockquote>
<p>Services\BMS\DBRepository</p>
</blockquote></td>
<td><blockquote>
<p>BMS.MT.Admission.xml</p>
</blockquote></td>
<td rowspan="10"><blockquote>
<p>XML mapping files which contains mapping definitions between ePractice datasets and SQL tables. The dataset is specified by setting the &lt;MyDataSetInfo&gt; tag. The table to interact with – specified through the</p>
<p>&lt;MyDataTable&gt; tag – is defined by four commands – usually stored procedures – which represent the CRUD operations which can be performed on the table: select (Read), insert (Create), update (Update) and delete (Delete). Stored procedure parameters are passed from these datasets and mapped in the same XML file. Connections.xml file is used to set the connection string to BMS database.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.AdmissionInfo.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.AdmissionLevelOfCare.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.BedCleanInfo.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.BedCleaning.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.BedCleanMobileInfo.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.BedDNDAndOOSFromVista.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.BedOccupancyCount.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.BedOccupancyInfo.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.BedStaff.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="11"></td>
<td><blockquote>
<p>BMS.MT.BedStaffHistory.xml</p>
</blockquote></td>
<td rowspan="11"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.BedSwitch.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.BedUnavailable.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.BedUnavailableHistory.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.BedUnavailableInfo.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.CancelableOrderInfo.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.Configuration.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.Discharge.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.Diversion.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.EISOrganization.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.EmsStaff.xml</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Relative Path</strong></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="20"></td>
<td><blockquote>
<p>BMS.MT.EvacuationPatients.xml</p>
</blockquote></td>
<td rowspan="20"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.IconAssociation.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.IconAssociationInfo.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.IconDetail.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.IconInfo.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.IconOrder.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.JobAudit.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.JobAuditInfo.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.LastActInfo.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.LevelOfCare.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.LoggedUser.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.Movement.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.NewEvent.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.OccupiedBedInfo.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.PatientIconAssociation.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.PatientLocation.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.PatientsWaitingCount.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.PatientWaitingDateView.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.PatientWaitingStandardView.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.Transfer.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="7"></td>
<td><blockquote>
<p>BMS.MT.TransferInfo.xml</p>
</blockquote></td>
<td rowspan="7"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.VistaIntegrationLog.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.VistaOperation.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS.MT.WaitingListItem.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS.MT.WaitingListReport.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ConfigurationService.DataAccess.Configu</p>
<p>rationsBE.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Connections.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Services\BMS\LocalReportW</p>
<p>hiteboard</p>
</blockquote></td>
<td><blockquote>
<p>WardWhiteboard.rdlc</p>
</blockquote></td>
<td><blockquote>
<p>Ward whiteboard report file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Services\BMS\Scripts</td>
<td><blockquote>
<p>conditional-validation.js</p>
</blockquote></td>
<td><blockquote>
<p>JavaScript conditional validation file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark138" class="anchor"></span>Table 24-WIN Service Host Files

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="14"><blockquote>
<p>Services\EIS</p>
</blockquote></td>
<td><blockquote>
<p>BindingExtensions.dll</p>
</blockquote></td>
<td rowspan="14"><blockquote>
<p>Binaries of the EIS Service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DTOGenericService.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DTOHL7Service.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EISAuditUtil.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EISAutomaticLink.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EISCache.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EISContracts.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EISDataAccess.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EISNotifications.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EISServiceGenericImplementation.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EISServiceHL7Implementation.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EISServiceImplementation.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EISServiceImplementation.dll.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICSharpCode.SharpZipLib.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="4"><blockquote>
<p>Services\EIS\DBRepository</p>
</blockquote></td>
<td><blockquote>
<p>Connections.xml</p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p>XML mapping files which contains mapping definitions between ePractice datasets and SQL tables. The dataset is specified by setting the &lt;MyDataSetInfo&gt; tag. The table to interact with – specified through the</p>
<p>&lt;MyDataTable&gt; tag – is defined by four commands – usually stored procedures –</p>
<p>which represent the CRUD operations which can be performed on the table: select</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.DTOA utomaticLink.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.DTOD omain.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.DTOE ntity.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="9"></td>
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.DTOE ntityType.xml</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>(Read), insert (Create), update (Update) and delete (Delete). Stored procedure parameters are passed from these datasets and mapped in the same XML file.</p>
<p>Connections.xml file is used to set the connection string to BMS_EIS database.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.DTOE ntityTypeClassifier.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.DTOE ntityTypeTraitCoresp.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.DTOTr ait.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.DTOTr aitAssignment.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.Entity Management.DTOEntityManageLink.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.Entity Management.DTOEntityMerge.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.Entity Management.DTOEntitySetStatus.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.LinkAl gorithmManagement.LinkAlgorithmTrait.x ml</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="14"></td>
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.LinkAl gorithmManagement.LinkAlgorithmTraits.x ml</p>
</blockquote></td>
<td rowspan="14"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.LinkAl gorithmManagement.Match.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.Query Functions.DTOConflictingEntities.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.Query Functions.DTOFindEntity.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.Query Functions.DTOGetAllInfoPar.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.Query Functions.DTOGetAllInformationForAnEnt ity.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.Query Functions.DTOGetSupportedDomains.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOGenericService.Query Functions.DTOLinkedEntities.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Address.x ml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Container. xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Container Filtr.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.ContainerI nfo.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Device.xm l</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.DeviceFiltr</p>
<p>.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="10"></td>
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.DeviceInfo</p>
<p>.xml</p>
</blockquote></td>
<td rowspan="10"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Manufactu redMaterial.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Manufactu redMaterialFiltr.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Manufactu redMaterialInfo.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Material.x ml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.MaterialFil tr.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.MaterialInf o.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.NonPerso nLivingSubject.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.NonPerso nLivingSubjectFiltr.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.NonPerso nLivingSubjectInfo.xml</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="15"></td>
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Organizati on.xml</p>
</blockquote></td>
<td rowspan="15"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Organizati onFiltr.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Organizati onInfo.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Person.xm l</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.PersonFiltr</p>
<p>.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.PersonInfo</p>
<p>.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Place.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.PlaceFiltr. xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.PlaceInfo. xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EIS.DTOHL7Service.Telecom.x ml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.CustomSubs criptions.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.Endpoints.xm l</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.FilterDialects. xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.Message.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.MessageGet. xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.MessageGet DeliveryTo.xml</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.Subscriptions</p>
<p>.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="10"></td>
<td><blockquote>
<p>ActionManager.dll</p>
</blockquote></td>
<td rowspan="10"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BindingExtensions.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CodingSystems.DAL.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Configuration.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>connectionConfiguration.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Connections.Common.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CTSEdit.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CTSEdit.Utils.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CTSEditBulk.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CTSExport.dll</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="19"><blockquote>
<p>Services\EVS</p>
</blockquote></td>
<td><blockquote>
<p>CTSImport.dll</p>
</blockquote></td>
<td rowspan="19"><blockquote>
<p>Binaries of EVS service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CTSImportProxy.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CTSService.Utils.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DTOCodeMappingEdit.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DTOMapping.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DTOMessageBrowser.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DTOMessageEdit.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DTOMessageRuntime.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DTOVocabularyEdit.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DTOVocabularyEdit.dll.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EVSWrapper.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EVSWrapper.dll.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Factory.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HL7DataTypes.XmlSerializers.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IContracts.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICSharpCode.SharpZipLib.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICTSEdit.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICTSEditBulk.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICTSExport.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="13"></td>
<td><blockquote>
<p>ICTSImport.dll</p>
</blockquote></td>
<td rowspan="13"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IEventing.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MappingImpl.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Message.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MessageImpl.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MessageImpl.dll.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS.Caching.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Notify.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SecureChannel.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Security.Null.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>securityConfiguration.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VocabularyBrowser.DTO.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VocabularyImpl.dll</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td><blockquote>
<p>VocabularyRuntime.DTO.dll</p>
</blockquote></td>
<td rowspan="4"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XamlContracts.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XamlDataContracts.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XamlImpl.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="12"><blockquote>
<p>Services\EVS\DBRepository</p>
</blockquote></td>
<td><blockquote>
<p>Connections.xml</p>
</blockquote></td>
<td rowspan="12"><blockquote>
<p>XML mapping files which contains mapping definitions between ePractice datasets and SQL tables. The dataset is specified by setting the &lt;MyDataSetInfo&gt; tag. The table to interact with – specified through the</p>
<p>&lt;MyDataTable&gt; tag – is defined by four commands – usually stored procedures – which represent the CRUD operations which can be performed on the table: select (Read), insert (Create), update (Update) and delete (Delete). Stored procedure parameters are passed from these datasets and mapped in the same XML file.</p>
<p>Connections.xml file is used to set the connection string to BMS_EVS database.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.Association. xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.CodingSyst em.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.Concept.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.ConceptAss ociationsToCMultiAttrib.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.ConceptPro perty.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.DSMap.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.DSMapEntr y.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.DTOReExp andValueSet.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.DTOValueS et.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.DTOVocabu laryDomain.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.Relation.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="10"></td>
<td><blockquote>
<p>InfoWorld.EVS.CTSEdit.DTO.ValueSets.x ml</p>
</blockquote></td>
<td rowspan="10"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.CodeSyste mInfo.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DomainVal ueSetFiltr.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSConcep tsByCode.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSConcep tsByCodeProperties.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSConcep tsByDesignation.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSConcep tsByDesignationProperties.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSFullVal ueSetDescription.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSValueS etContextExpansion.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSValueS etExpansion.xml</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="14"></td>
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSValueS etExpansionProperties.xml</p>
</blockquote></td>
<td rowspan="14"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSValueS etExpansionReverse.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.DSVocabu laryDomainDescription.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.GetFillInD etailsCD.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.IsCodeInV alueSet.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.ValidateCo de.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.ValueSetC odeReference.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.ValueSetFi ltr.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSMAPI.DTO.Vocabular yDomainFiltr.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMapping.DTO.DSMap ConceptCode.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSMapping.DTO.DSMap Entry.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSMapping.DTO.DSSup portedMapsFiltr.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.CodeSyste m.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.CodeSyste mFiltr.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="11"></td>
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.CodingSch emeFiltr.xml</p>
</blockquote></td>
<td rowspan="11"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.ConceptCo deValid.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.ConceptDe scription.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.ConceptEx pansion.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.ConceptPr operties.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.ConceptsB yDesignation.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.ConceptsB yProperty.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.Designatio n.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.CTSVAPI.DTO.RelatedCo ncepts.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.EVS.DTOEditBulk.ConceptBulk. xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.EVS.DTOEditBulk.ConceptProp ertyBulk.xml</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="11"></td>
<td><blockquote>
<p>InfoWorld.EVS.DTOEditBulk.RelationBulk. xml</p>
</blockquote></td>
<td rowspan="11"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.CustomSubs criptions.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.Endpoints.xm l</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.FilterDialects. xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.Message.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.MessageGet. xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.MessageGet DeliveryTo.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.Subscriptions</p>
<p>.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XamlDataContracts.DSXamlReverse.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XamlDataContracts.RootXaml.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XamlDataContracts.XAMLFiltr.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4"><blockquote>
<p>Services\PAP</p>
</blockquote></td>
<td><blockquote>
<p>ActionManager.dll</p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p>Binaries of PAP service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuthorizationProxy.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Configuration.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>connectionConfiguration.config</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="11"></td>
<td><blockquote>
<p>Connections.Common.dll</p>
</blockquote></td>
<td rowspan="11"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Microsoft.ApplicationBlocks.Data.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Microsoft.ApplicationBlocks.ExceptionMan agement.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Microsoft.ApplicationBlocks.ExceptionMan agement.Interfaces.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Microsoft.Practices.EnterpriseLibrary.Com mon.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Microsoft.Practices.EnterpriseLibrary.Exce ptionHandling.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Microsoft.Practices.EnterpriseLibrary.Exce ptionHandling.Logging.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Microsoft.Practices.EnterpriseLibrary.Logg ing.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Microsoft.Practices.ObjectBuilder.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS.Caching.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ObjectPickerHelper2.dll</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="6"></td>
<td><blockquote>
<p>PAPProxy.dll</p>
</blockquote></td>
<td rowspan="6"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PDPServiceAuthorizationManager.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PolicyAdministrationPoint.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PolicyAdministrationPoint.dll.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SecureChannel.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Security.Null.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="11"><blockquote>
<p>Services\PAP\DBRepository</p>
</blockquote></td>
<td><blockquote>
<p>Connections.xml</p>
</blockquote></td>
<td rowspan="11"><blockquote>
<p>XML mapping files which contains mapping definitions between ePractice datasets and SQL tables. The dataset is specified by setting the &lt;MyDataSetInfo&gt; tag. The table to interact with – specified through the</p>
<p>&lt;MyDataTable&gt; tag – is defined by four commands – usually stored procedures – which represent the CRUD operations which can be performed on the table: select (Read), insert (Create), update (Update) and delete (Delete). Stored procedure parameters are passed from these datasets and mapped in the same XML file.</p>
<p>Connections.xml file is used to set the connection string to BMS_AURHZ database.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.DE.DataAccess.LabSet.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.DE.DataAccess.LabSetId.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.DE.DataAccess.SentStatus.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.CustomSubs criptions.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.Endpoints.xm l</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.FilterDialects. xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.Message.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.MessageGet. xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.MessageGet DeliveryTo.xml</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InfoWorld.WSEventing.DTO.Subscriptions</p>
<p>.xml</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>Services\PDP</p>
</blockquote></td>
<td><blockquote>
<p>PolicyDecisionPoint.dll</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Binaries of PDP service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PolicyDecisionPoint.dll.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5"><blockquote>
<p>Services\RS</p>
</blockquote></td>
<td><blockquote>
<p>AuthorizationProxy.dll</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p>Binaries of RS service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RS.Contracts.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RS.Proxy.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RS.ServiceImplementation.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RS.ServiceImplementation.dll.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="6"></td>
<td><blockquote>
<p>7zip.dll</p>
</blockquote></td>
<td rowspan="6"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdapterRepository.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuditTrailSender.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AuthorizationSubscriber.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BindingExtensions.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Common.dll</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="18"><blockquote>
<p>Services\Shared</p>
</blockquote></td>
<td><blockquote>
<p>CommonResources.dll</p>
</blockquote></td>
<td rowspan="18"><blockquote>
<p>Shared binaries by BMS Service and Win Service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Connections.SingleDatabase.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ContextWriter.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DataUtil.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>General.MT.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HL7CDA.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HL7CMET.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HL7DataTypes.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICSharpCode.SharpZipLib.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Infoworld.Configuration.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>log4net.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MiddleTier.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MS.Common.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS.Configuration.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MS.Connections.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS.Security.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Saml20.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SecurityTokenCache.dll</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="6"></td>
<td><blockquote>
<p>Tracing.dll</p>
</blockquote></td>
<td rowspan="6"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WSEventing.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WSEventing.DataAccess.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WSEventing.DTO.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Xacml2.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XacmlCore.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Services\STS</p>
</blockquote></td>
<td><blockquote>
<p>SecureTokenService.dll</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Binaries of STS service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SecureTokenService.dll.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>Services</p>
</blockquote></td>
<td><blockquote>
<p>WinServiceHost.exe</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>WinServiceHost files.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WinServiceHost.exe.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BMS-Services.log</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark139" class="anchor"></span>Table 25-BMS Website Files

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 42%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="7"><blockquote>
<p>WebSite</p>
</blockquote></td>
<td><blockquote>
<p>CacheService.svc</p>
</blockquote></td>
<td rowspan="7"><blockquote>
<p>The binaries of the BMS Web Site, web site configuration file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Global.asax</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>packages.config</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Web.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebTrace.log</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>additional_login_msg.txt</p>
</blockquote></td>
<td><blockquote>
<p>Dynamic text for main login page</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\bin</p>
</blockquote></td>
<td><blockquote>
<p>AntiXSSLibrary.dll</p>
</blockquote></td>
<td><blockquote>
<p>Web site's binaries.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>AuditTrailSender.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>AuthenticationProxy.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BMS.Contracts.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>BMS.Facade.Contracts.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BMS.Facade.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>BMS.PAPContracts.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BMS.Security.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>BMS.ServicesWrapper.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BMS.Utils.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>BMS.Web.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>EISContracts.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>HL7DataTypes.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>HtmlAgilityPack.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>HtmlSanitizationLibrary.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>IContracts.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ICTSEdit.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Infoworld.Configuration.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>log4net.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>log4netAsync.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Microsoft.ReportViewer.Common.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Microsoft.ReportViewer.DataVisualization.dl</p>
<p>l</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Microsoft.ReportViewer.ProcessingObjectM odel.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Microsoft.ReportViewer.WebForms.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Microsoft.Web.Infrastructure.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Microsoft.Web.Mvc.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>RS.Contracts.dll</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 42%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Saml20.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>SecurityTokenCache.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>System.Web.Helpers.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>System.Web.Mvc.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>System.Web.Razor.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>System.Web.WebPages.Deployment.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>System.Web.WebPages.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>System.Web.WebPages.Razor.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Tracing.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Xacml2.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>XacmlCore.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\bin\LocalReportWhite board</p>
</blockquote></td>
<td><blockquote>
<p>WardWhitebord.rdlc</p>
</blockquote></td>
<td><blockquote>
<p>Ward Whiteboard report file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\bin\Scripts</p>
</blockquote></td>
<td><blockquote>
<p>Conditional-validation.js</p>
</blockquote></td>
<td><blockquote>
<p>File used by the site for conditional validation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Content</p>
</blockquote></td>
<td><blockquote>
<p>bundleCss.chirp.config</p>
</blockquote></td>
<td><blockquote>
<p>Images, themes and styles.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Controls.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>LayoutCss.min.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>LayoutVistaIntegrationCss.min.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Reports.min.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Site.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Content\images</p>
</blockquote></td>
<td><blockquote>
<p>add_tab_24.png</p>
</blockquote></td>
<td><blockquote>
<p>Images used by site.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>arrow_down.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>arrow_up.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>BMSLogoV6.jpg</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>check_inv.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>edit_staff_cancel.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>edit_staff_save.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>FavIcon.ico</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Info.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Ladybug.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>login_logo.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>logo.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>order_down.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>order_up.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>sort_down.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>sort_up.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Content\themes\base</p>
</blockquote></td>
<td><blockquote>
<p>jquery.ui.accordion.css</p>
</blockquote></td>
<td><blockquote>
<p>jQuery controls style- sheets files.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.ui.all.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.ui.autocomplete.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.ui.base.css</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 42%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.ui.button.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.ui.core.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.ui.datepicker.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.ui.dialog.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.ui.progressbar.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.ui.resizable.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.ui.selectable.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.ui.slider.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.ui.tabs.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.ui.theme.css</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Content\themes\base</p>
<p>\images</p>
</blockquote></td>
<td><blockquote>
<p>ui-bg_flat_0_aaaaaa_40x100.png</p>
</blockquote></td>
<td><blockquote>
<p>Images</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ui-bg_flat_75_ffffff_40x100.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ui-bg_glass_55_fbf9ee_1x400.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ui-bg_glass_65_ffffff_1x400.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ui-bg_glass_75_dadada_1x400.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ui-bg_glass_75_e6e6e6_1x400.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ui-bg_glass_95_fef1ec_1x400.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ui-bg_highlight-soft_75_cccccc_1x100.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ui-icons_222222_256x240.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ui-icons_2e83ff_256x240.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ui-icons_454545_256x240.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ui-icons_888888_256x240.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ui-icons_cd0a0a_256x240.png</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Reporting</p>
</blockquote></td>
<td><blockquote>
<p>EvacuationPatientReportViewer.aspx</p>
</blockquote></td>
<td><blockquote>
<p>Report Viewer pages.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>LocalReportViewer.aspx</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ReportError.aspx</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ReportViewer.aspx</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\ ReportsLocal</p>
</blockquote></td>
<td><blockquote>
<p>BedStatusReport.rdlc</p>
</blockquote></td>
<td><blockquote>
<p>Bed Status Report file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Scripts</p>
</blockquote></td>
<td><blockquote>
<p>antiForgeryToken.js</p>
</blockquote></td>
<td><blockquote>
<p>JavaScript files.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>bundleScripts.chirp.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>conditional-validation.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>element-change.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>hoverIntent.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.autosize.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.base64.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.base64.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.jscrollpane.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.maskedinput-1.3.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.mousewheel.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.tablescroll.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.tablescroll.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.tablesorter.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.tablesorter.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.ui.autocomplete.js</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 42%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.ui.core.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.ui.position.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.ui.progressbar.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.ui.widget.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.unobtrusive-ajax.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.unobtrusive-ajax.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.validate.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.validate.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.validate.unobtrusive.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery.validate.unobtrusive.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery.validate-vsdoc.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery-1.5.1.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery-1.5.1.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery-1.5.1-vsdoc.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery-1.7.1.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery-1.7.1.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery-ui-1.8.11.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>jquery-ui-1.8.11.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>jquery-ui-1.8.18.custom.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>json2.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>LayoutAdminAutoCompleteAndDatePicker.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>LayoutAdminScripts.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>LayoutAutoCompleteAndDatePicker.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>LayoutScripts.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>LayoutVistaIntegrationDatePicker.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>LayoutVistaIntegrationScripts.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>MicrosoftAjax.debug.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MicrosoftAjax.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>MicrosoftMvcAjax.debug.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MicrosoftMvcAjax.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>MicrosoftMvcValidation.debug.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MicrosoftMvcValidation.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>modernizr-1.7.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>modernizr-1.7.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Reports.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>superfish.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>supersubs.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>whiteboard-script.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>whiteboard-script.min.js</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views</p>
</blockquote></td>
<td><blockquote>
<p>_ViewStart.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>User Interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Web.config</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\Account</p>
</blockquote></td>
<td><blockquote>
<p>LogOff.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Login/Logout user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>LogOn.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\Admin</p>
</blockquote></td>
<td><blockquote>
<p>AddEditUser.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Admin section user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>AddUserOperations.cshtml</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 42%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CacheConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>FacilityEdit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>FacilityEditSaved.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>RefreshUsersConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>RemoveUserOperations.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>SelectUser.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>SisterSiteAddEdit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>SisterSiteEditSaved.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>UserEditHasSaved.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>UserOperationsView.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\AdminSpecialt yAssociation</p>
</blockquote></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Admin specialty association user interface</p>
<p>views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\AdminUnavailableR eason</p>
</blockquote></td>
<td><blockquote>
<p>AddConfirmation.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Admin unavailable reason user interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>DeleteConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>EditConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MissingUnavailableReasonText.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>UnavailableReasonAlreadyExists.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>UnavailableReasonList.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\AdminComments</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>NotifyChange.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\AdminWaitingArea</p>
</blockquote></td>
<td><blockquote>
<p>AddAction.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Admin waiting area user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>DeleteAction.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>EditAction.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\AdminWhiteboardRe port</p>
</blockquote></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Admin whiteboard report user interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\AdtOrderableItems</p>
</blockquote></td>
<td><blockquote>
<p>Confirmation.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>ADT Orderable Items user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>OrderableItemsList.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\BackgroundProcess ors</p>
</blockquote></td>
<td><blockquote>
<p>AddEditConfirmation.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Background Processors user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>DeleteConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\BedBoard</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>VISN user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\BedBoardModule</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Bed Board Module user</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 42%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>interface view.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\BedInformation</p>
</blockquote></td>
<td><blockquote>
<p>ClearAll.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Bed Information user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>NotifyChange.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\BedStatusReport</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Patients Pending Placement Status report</p>
<p>user interface view.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\ContingencySettings</p>
</blockquote></td>
<td><blockquote>
<p>Confirmation.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Contingency settings user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\DischargeClinic</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Discharge clinic user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>MessageConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\EmsBedStatusAdmi n</p>
</blockquote></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>EMS bed status user interface views</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>EMSBatchAssign.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>SaveConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\EMSMobile</p>
</blockquote></td>
<td><blockquote>
<p>EMSList.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>EMS Mobile user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Users.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\EMSMobileLogon</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>EMS Mobile Logon user interface view.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\EmsNotification</p>
</blockquote></td>
<td><blockquote>
<p>AddEdit.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>EMS Notification user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>AddEditAction.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>DeleteAction.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\EmsStaff</p>
</blockquote></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>EMS Staff user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\EventNotification</p>
</blockquote></td>
<td><blockquote>
<p>AddConfirmation.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Event Notification user interface views</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>AddEdit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>DeleteConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>EditConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\Exception</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Exception user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>WFException.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\FacilityDiversion</p>
</blockquote></td>
<td><blockquote>
<p>Add.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Facility Diversion user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Confirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\FacilitySettings</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Facility Settings user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>SaveConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 42%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\Home</p>
</blockquote></td>
<td><blockquote>
<p>AdmissionList.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Home user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>AdmissionSuccessRemove.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>AdmissionSuccessUndoRemove.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ChangeIntegratedSiteError.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>FeeUtilizationAdmissionList.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PatientFlowAdmissionList.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>PatientInHouseAdmissionList.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PatientInquiry.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>RemoveAdmission.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>StandardAdmissionList.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>UndoRemoveAdmission.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\IconLegend</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Icon Legend user interface view.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\IconLibrary</p>
</blockquote></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Icon Library user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>ResetConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>SaveConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\Information</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Information user interface view.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\LogOff</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>LogOff user interface view.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\MaintainMarquee</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Maintain Marquee user interface view.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Saved.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\NationalAndRegiona l</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>National user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PatientListView.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\NewEvents</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>New events user interface view.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\Numi</p>
</blockquote></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>NUMI user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\Patient</p>
</blockquote></td>
<td><blockquote>
<p>Admission.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Patient user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Confirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>EvacuationData.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>GenericWfFault.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>PatientWaitingAdd.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Select.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\Reports</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Patient user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\Shared</p>
</blockquote></td>
<td><blockquote>
<p>_Layout.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Shared user interface</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 42%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>_LayoutAdminPages.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>_VistaIntegrationLayout.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CustomWebViewPage.cs</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Error.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Header.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>HtmlHelpers.cs</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>RequiredIfHelpers.cs</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\SiteList</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Site list user interface view.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\SiteOptions</p>
</blockquote></td>
<td><blockquote>
<p>EvacuationConfirmation.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Site options user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\Transfer</p>
</blockquote></td>
<td><blockquote>
<p>AddEditResult.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>AddTranfer.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>EditTransfer.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>FinalizeResult.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\Unauthorized</p>
</blockquote></td>
<td><blockquote>
<p>PermissionAuth.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Unauthorized user interface view.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\UserConfiguration</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>User configuration views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>SelectUser.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>UserEditHasSaved.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\UnavailableReason</p>
</blockquote></td>
<td><blockquote>
<p>AddConfirmation.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Unavailable reason user interface views.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>DeleteConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>EditConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>MissingUnavailableReasonText.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>UnavailableReasonAlreadyExists.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>UnavailableReasonList.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\VistaIntegration</p>
</blockquote></td>
<td><blockquote>
<p>Audit.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>VistA integration user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>AuditLogEntries.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Categories.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>DeleteScheduler.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>EditScheduler.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>EditVistASite.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>ErrorDetail.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Schedulers.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>VistASites.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\WaitingArea</p>
</blockquote></td>
<td><blockquote>
<p>AddAction.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>DeleteAction.cshtml</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 42%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>EditAction.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\WardConfiguration</p>
</blockquote></td>
<td><blockquote>
<p>AddEditWardConfirmation.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Ward configuration user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Delete.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>DeleteConfirmation.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Wards.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\WardOccupancy</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Ward occupancy user interface view.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\WardWhiteboard</p>
</blockquote></td>
<td><blockquote>
<p>ClearAll.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Ward whiteboard user interface views.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Edit.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>NotifyChange.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>WardWhiteBoard.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>WhiteboardDataOne.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>WhiteboardDataTwo.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\WardWhiteboardUrl</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Ward whiteboard url user interface view.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WebSite\Views\WhiteboardStaff</p>
</blockquote></td>
<td><blockquote>
<p>Index.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>Whiteboard staff user interface view.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebSite\Views\ _ViewStart.cshtml</p>
</blockquote></td>
<td><blockquote>
<p>_ViewStart.cshtml</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="_bookmark140" class="anchor"></span>Table 26-Policy Manager Files

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Relative Path</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="17"><blockquote>
<p>Consoles\PolicyManager</p>
</blockquote></td>
<td><blockquote>
<p>7zip.dll</p>
</blockquote></td>
<td rowspan="17"><blockquote>
<p>Binaries of PolicyManager application</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdapterRepository.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuditTrailSender.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Infoworld.Configuration.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MS.Common.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS.Configuration.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MS.Connections.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAPProxy.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PolicyEditor.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PolicyEditor.dll.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PolicyManager.exe</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PolicyManager.exe.config</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ResourceSecurityProperties.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SecurityTokenCache.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WSEventing.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WSEventing.DataAccess.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WSEventing.DTO.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>Consoles\PolicyManager\ ro</p>
</blockquote></td>
<td><blockquote>
<p>PolicyEditor.resources.dll</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Binaries used by Policy Manager.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ResourceSecurityProperties.resources.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>Consoles\PolicyManager\ ro- RO</p>
</blockquote></td>
<td><blockquote>
<p>PolicyEditor.resources.dll</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Binaries used by Policy Manager.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ResourceSecurityProperties.resources.dll</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All the sensitive data in the BMS solution is persisted in a collection of SQL Server Databases. Therefore the archiving process is implying the definition of maintenance plans that will regularly make backups of these databases, backups that can be restored if needed.

> The maintenance plan can be defined as detailed in the following pictures:

![](bed-management-solution-version-2-4-technical-manual/075.png)

> <span id="_bookmark142" class="anchor"></span>Figure 74-Backup Maintenance Plan

# External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> External relationships can be referenced from [<u>External Interfaces</u>](#archiving) in the next section.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA and NUMI are the external interfaces that are connected with the BMS system (see screenshot below):

![](bed-management-solution-version-2-4-technical-manual/076.png)

> <span id="_bookmark146" class="anchor"></span>Figure 75-BMS Exnternal Interfaces

- All the VISTA deployments will be connected through VIA which has replaced MDWS. In order to connect to VIA, BMS service configuration file (BMS.ServiceHost.exe.config) should be changed as follow, see Table 4 – BMS ServiceHost Configuration Parameter section:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 36%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ViaEndpointUrl</p>
</blockquote></th>
<th><blockquote>
<p>value="https://REDACTED.via.va.gov/vi a- webservices/services/BackgroundProc</p>
<p>essService"</p>
</blockquote></th>
<th><blockquote>
<p>value="https://REDACTED.via.va.gov/via- webservices/services/BackgroundProcessSer vice"</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ViaRequestingApp</p>
</blockquote></td>
<td><blockquote>
<p>value="BMSBatch"</p>
</blockquote></td>
<td><blockquote>
<p>value="BMSBatch"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ViaAppToken</p>
</blockquote></td>
<td><blockquote>
<p>value="BMSB_ID577"</p>
</blockquote></td>
<td><blockquote>
<p>value="BMSB_ID577"</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ViaAppPassword</p>
</blockquote></td>
<td><blockquote>
<p>value="*"</p>
</blockquote></td>
<td><blockquote>
<p>Value="*"</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MinimumFilemanDate</p>
</blockquote></td>
<td><blockquote>
<p>Value="01/01/1992"</p>
</blockquote></td>
<td><blockquote>
<p>Value="01/01/1992"</p>
</blockquote></td>
</tr>
</tbody>
</table>

- NUMI - A connection string to NUMI database needs to be set in service configuration file (BMS.ServiceHost.exe.config), see [*Table 4 - BMS ServiceHost Configuration Parameters*](#_bookmark12) section:

> *\<ConnectionString\>Data Source=numiserver;Initial Catalog=NUMI;Integrated Security=True;\</ConnectionString\>.*

> NOTE: All the configurations described above are using dummy servers and ports. Real deployment should use appropriate server, port and database connection strings.

# Software Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS Security is implemented at two levels:

- The first level of security consists in deciding which users have access to what pages (National/Regional, VISN, facility, EMS page).
- The second level of security refers to the read/write permissions (which are the pages a user can edit/update).

> Both levels of security are implemented by means of the Policy Manager application described in the next section.

> An additional level of security is provided by the domain restrictions: users can access only the BMS pages within the domain where they have been granted access rights.

> The security services are based on well-established standards and practices such as:

- LDAP protocol;
- WS-Security specification;
- X509 certificates.

> These services are in charge of providing for the following 'functionalities':

- CIA:
  - Confidentiality – encrypted message.
  - Integrity – message hasn't been tampered.
  - Authentication – prove identity.
- Authorization – role based access.
- Accountability – audit trail.
- Policies – mutually agreed by involved parties.

> From the client application perspective, the security services are in charge of:

- Authentication:
  - SAML assertions verified by the called service.
- Role based authorization:
  - Roles stored in LDAP.
  - Policies defined using XACML language.
- Record level authorization.
- Audit trail.

> The audit services provide the means to address the issues of liability management, asset protection and quality of service. To facilitate a timely response to policy violations, security incidents or infrastructure and application failures, InFlow will support monitoring, logging, analysing, and reporting on every level of its architecture.

> ![](bed-management-solution-version-2-4-technical-manual/077.png)

> <span id="_bookmark148" class="anchor"></span>Figure 76-Security Services Architecture

> The security services consist of the authentication part: STS – security token service and authorization part: PAP

> – policy administration point and PDP – policy decision point.

## Policy Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Console folder of your BMS solution, select Policy Manager and then double-click the PolicyManager.exe file to display the following dialog window:

![](bed-management-solution-version-2-4-technical-manual/078.png)

> <span id="_bookmark150" class="anchor"></span>Figure 77-Policy Manager Main Window

> The Definitions folder in the left hand panel contains the definitions of the roles, tasks and operations valid within the BMS application.

> The Role Definitions folder contains the list of user roles defined within BMS.

> The Task Definitions folder contains the list of tasks that can be performed within BMS and their corresponding definitions. A task usually requires the completion of several operations.

> The Operation Definitions folder contains the list of operations that can be performed within BMS and their corresponding definitions.

## Operation Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view the definition of an operation select Operation definitions from the left-hand panel of the main Policy Manager window and double-click the operation to display the following dialog window:

> ![](bed-management-solution-version-2-4-technical-manual/079.png)

> <span id="_bookmark152" class="anchor"></span>Figure 78-Operation Definition

> A list with all the operations of BMS application is presented below:

> <span id="_bookmark153" class="anchor"></span>Table 27-BMS Operations

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Operation Name</strong></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Admin, AddEditUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add/Edit BMS User' hyperlink from the Administration section's menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, FacilityEdit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit BMS Site' hyperlink from the Administration</p>
<p>section's menu.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'BMS Admin' hyperlink from the National And Regional Page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><strong>Operation Name</strong></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, SelectUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Select Existing NT User Name' button from the</p>
<p>ADMINISTRATION SECTION - USERADD/EDIT page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, SisterSiteAddEdit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit Sister Sites' hyperlink from the Administration section's menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, AddUserOperations Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add User' button from the ADMINISTRATION SECTION</p>
<p>- FACILITY EDIT page (Edit BMS Site submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, RemoveUsers Read</p>
</blockquote></td>
<td><blockquote>
<p>'Remove Selected' button from the ADMINISTRATION SECTION - FACILITY EDIT page (Edit BMS Site</p>
<p>submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, SearchUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Find' button from the 'Select user' page ('Select Existing</p>
<p>NT User Name' button from the Administration Section menu, 'Add/Edit BMS User' submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, SearchUsers Read</p>
</blockquote></td>
<td><blockquote>
<p>'Find' button from the ADMINISTRATION SECTION -</p>
<p>FACILITY EDIT page (Edit BMS Site submenu).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Admin, ClearCache Read</p>
</blockquote></th>
<th><blockquote>
<p>'Clear Cache' link from the Administration section's menu.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Admin, AddEditUser Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the ADMINISTRATION SECTION -</p>
<p>USERADD/EDIT page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, FacilityEdit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from Administration section's menu 'Edit BMS Site' hyperlink (page ADMINISTRATION SECTION</p>
<p>- FACILITY EDIT).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, SisterSiteAddEdit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Edit Sister Sites' hyperlink from the Administration section's menu, 'Submit' button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, AddUserOperations Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from Add users page (Add User button from</p>
<p>the Facility page).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, RemoveUserOperations Update</p>
</blockquote></td>
<td><blockquote>
<p>'Remove Selected' button from the ADMINISTRATION SECTION - FACILITY EDIT page (Edit BMS Site</p>
<p>submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminComments, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' hyperlink from the Common Medical Terms page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminComments, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' hyperlink from the Common Medical Terms page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminComments, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Common Medical Terms' hyperlink from the Administration section's menu.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminComments, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from the Common Medical Terms page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Icon' button on ADMINISTRATION SECTION - EDIT ICON page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' Link on ADMINISTRATION SECTION - ICON</p>
<p>ADD/EDIT page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add/Edit Icon' link on ADMINISTRATION SECTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, Search Read</p>
</blockquote></td>
<td><blockquote>
<p>'Search' Link on ADMINISTRATION SECTION - ICON</p>
<p>ADD/EDIT page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, ViewIconReport Read</p>
</blockquote></td>
<td><blockquote>
<p>''Report' Link on ADMINISTRATION SECTION - ICON</p>
<p>ADD/EDIT page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Remove' button on ADMINISTRATION SECTION - DELETE ICON page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on ADMINISTRATION SECTION - EDIT</p>
<p>ICON page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Up/Down arrow' buttons on ADMINISTRATION</p>
<p>SECTION - ICON ADD/EDIT page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminSpecialtyAssociation, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' Link on ADMINISTRATION SECTION - Treating</p>
<p>Specialty/NUMA/HAvBED Edit page (Treating Specialty/NUMA/HAvBED Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminSpecialtyAssociation, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Treating Specialty/NUMA/HAvBED' Link on</p>
<p>ADMINISTRATION SECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminSpecialtyAssociation, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' Button on ADMINISTRATION SECTION -</p>
<p>Treating Specialty/NUMA/HAvBED Delete page (Treating Specialty/NUMA/HAvBED Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminSpecialtyAssociation, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' Button on ADMINISTRATION SECTION - Treating</p>
<p>Specialty/NUMA/HAvBED Edit page (Treating Specialty/NUMA/HAvBED Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminUnavailableReason, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link on ADMINISTRATION SECTION - National</p>
<p>Unavailable Reason page (National Unavailable Reason Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminUnavailableReason, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link on ADMINISTRATION SECTION - National</p>
<p>Unavailable Reason page (National Unavailable Reason Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminUnavailableReason, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'National Unavailable Reason' Link on</p>
<p>ADMINISTRATION SECTION</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AdminUnavailableReason, Delete Update</p>
</blockquote></th>
<th><blockquote>
<p>'Delete Record' button on ADMINISTRATION SECTION</p>
<p>- National Unavailable Reason Delete page (National Unavailable Reason Submenu)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AdminUnavailableReason, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button on ADMINISTRATION SECTION - National Unavailable Reason Edit page (National</p>
<p>Unavailable Reason Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminUnavailableReason, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button on ADMINISTRATION SECTION - National Unavailable Reason page (National Unavailable Reason Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWaitingArea, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link on ADMINISTRATION SECTION - National Waiting Areas Parameter page (National Waiting Area</p>
<p>Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWaitingArea, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link on ADMINISTRATION SECTION - National Waiting Areas Parameter page (National Waiting Area Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWaitingArea, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'National Waiting Area' Link on ADMINISTRATION</p>
<p>SECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWaitingArea, DeleteAction Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button on ADMINISTRATION SECTION</p>
<p>- National Waiting Area Parameter Delete page (National Waiting Area Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWaitingArea, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button on ADMINISTRATION SECTION -</p>
<p>National Waiting Area Parameter Edit page (National Waiting Area Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWaitingArea, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button on ADMINISTRATION SECTION - National</p>
<p>Waiting Area Parameter page (National Waiting Area Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWhiteboardReport, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link on ADMINISTRATION SECTION -</p>
<p>Whiteboard Report page (Background Processor Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWhiteboardReport, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link on ADMINISTRATION SECTION - Whiteboard</p>
<p>Report page (Background Processor Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWhiteboardReport, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Whiteboard Report' tab on ADMINISTRATION SECTION - Background Processor page</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWhiteboardReport, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button on ADMINISTRATION SECTION</p>
<p>- Whiteboard Report Delete page (Background Processor Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWhiteboardReport, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on ADMINISTRATION SECTION -</p>
<p>Whiteboard Report Edit page (Background Processor Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdtOrderableItems, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, ADT Orderable Items Add/Delete hyperlink</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdtOrderableItems, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' hyperlink from the list of orderable items.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdtOrderableItems, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Bed Board ADT Orderable Items Configuration.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BackgroundProcessors, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Backgroung Processors' hyperlink from Site Options page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BackgroundProcessors, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save Scheduler' button from Background Processors</p>
<p>page within Site Options.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuditLogReport, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'View audit log' link on ADMINISTRATION SECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Audit Log Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Audit Log Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedBoard, ChangeFacility Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a facility link from the VISN Network Bed Boards list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedBoard, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Return to VISN Network' hyperlink from the home page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedBoard, ShowFacilityBedSummaryReport Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a Facility Summary Report on VISN Network</p>
<p>Bed Boards list</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>BedBoard, ShowVISNBedSummaryReport Read</p>
</blockquote></th>
<th><blockquote>
<p>Click on a VISN Summary Report on VISN Network Bed Boards list</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>BedBoardModule, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Bed Board Module Enable/Disable link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedBoardModule, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Bed Board Module Activation and Configuration page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedInformation, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Ward Occupancy, click on a hyperlink from the BED</p>
<p>column.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedInformation, ClearAll Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on button 'Clear ALL Comments For ALL Wards Associate To This Bed…'.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedInformation, NotifyChange Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Add/Edit Bed Unavailable</p>
<p>Reason page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedInformation, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on buttons 'Submit' and/or 'Update Reason and Comments'.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ContingencySettings, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Contingency Settings" link on Site Settings pages.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ContingencySettings, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on Contingency Settings page on Site Settings pages.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DischargeClinic, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'Discharge Appt Clinics Add/Delete'</p>
<p>hyperlink.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DischargeClinic, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'Discharge Appt Clinics Add/Delete' hyperlink, 'Delete' button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DischargeClinic, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'Discharge Appt Clinics Add/Delete'</p>
<p>hyperlink, 'Add' button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin, EMS Supervisor Read/Update</p>
</blockquote></td>
<td><blockquote>
<p>'Assigned To' drop down on EMS Bed Edit page</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsBedStatusAdmin, EMSBatchAssign Read</p>
</blockquote></td>
<td><blockquote>
<p>'Batch Assign' button on Ems Bed Status Admin page</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin, EMSBatchAssign Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button on EMS Bed Edit page on EMS Bed Status Admin page</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsBedStatusAdmin, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>RoomBed column link click.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Return to VISN Network' link from the home page,</p>
<p>'Return to Regional Page' link, 'Go To Facility Bed Cleaning Page (EMS Staff Only) button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsBedStatusAdmin, SaveConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button click in the Environmental Management</p>
<p>Service Bed Status page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button click in the Environmental Management Service Bed Status page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EMSMobile, EMSList Read</p>
</blockquote></td>
<td><blockquote>
<p>Load Bed Clean Requests on EMS Mobile Pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMSMobile, Users Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a User button on EMS Mobile Pages</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EMSMobile, EMSList Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on a Bed Clean Request button on EMS Mobile Pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMSMobile, Users Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on Submit button after entering a PIN on EMS</p>
<p>Mobile Pages</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsNotification, AddEdit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Current Locations table (EMS Bed Notification).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsNotification, AddEditAction Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the EMS Bed Notification Edit page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsNotification, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Current Locations table (EMS Bed</p>
<p>Notification).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsNotification, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'EMS Notification Add/Edit' link</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsNotification, DeleteAction Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button from the EMS Bed Status Notification Delete page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsNotification, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the EMS Bed Notification Edit page</p>
<p>or Notifications Add page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsStaff, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link on EMS Staff page on Site Options pages</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>EmsStaff, Edit Read</p>
</blockquote></th>
<th><blockquote>
<p>'Edit' link on EMS Staff page on Site Options pages</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EmsStaff, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>EMS Staff link on Site Options page</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsStaff, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button on Ems Staff Delete page on Site Options pages</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsStaff, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button on Ems Staff Edit page on Site Options</p>
<p>pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EventNotification, AddConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Event Notification Add page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EventNotification, AddEdit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button or 'Edit' link from the Event Notifications page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EventNotification, EditConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Event Notifications Edit page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EventNotification, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'Event Notification Add/Edit' hyperlink.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EventNotification, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Event Notification Add page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Exception, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Appears when an exception occurs.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, Add Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Facility Diversion page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilityDiversion, AddConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Add New Diversion Status page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Facility Diversion page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilityDiversion, EditConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from the Diversion Status edit page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, FilterDiversions Read</p>
</blockquote></td>
<td><blockquote>
<p>'Current Diversions' or 'All Diversions' button from the</p>
<p>main Facility Diversions page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilityDiversion, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Facility Diversion' hyperlink from the home page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button or 'Edit' link from the Facility Diversion page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilitySettings, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Facility Settings link</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilitySettings, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Facility Settings link, Submit button</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home, Index2 Read</p>
</blockquote></td>
<td><blockquote>
<p>Current, Past 30-Days, Past 60-Days, Past 90-Days home page's buttons.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, PatientInquiry Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on the patient link from the Patients Pending</p>
<p>Placement list (Home page).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home, RemoveAdmission Read</p>
</blockquote></td>
<td><blockquote>
<p>Remove link from the Patients Pending Placement list (Home page).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, UndoRemoveAdmission Read</p>
</blockquote></td>
<td><blockquote>
<p>Undo link from the Patients Pending Placement list</p>
<p>(Home page).</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home, RemoveAdmissionPost Update</p>
</blockquote></td>
<td><blockquote>
<p>Remove link from the Patients Pending Placement list</p>
<p>(Home page), Remove button from the confirmation page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, UndoRemoveAdmissionPost Update</p>
</blockquote></td>
<td><blockquote>
<p>'Undo' button on Undo Remove Admission Page on Facility HomePage</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IconLegend, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Icon Legend' link from the bottom of the Home page or</p>
<p>Site Options, BMS Icon Legend link.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IconLibrary, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' Link on Site Options - Site Configurable Icons page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IconLibrary, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Site Configurable Icons link.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IconLibrary, ResetConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Reset' button on Edit Site Configurable Icon page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IconLibrary, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on Site Options - Site Configurable Icons page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>IconLibrary, Index Update</p>
</blockquote></th>
<th><blockquote>
<p>'Up/Down arrow' buttons on Site Options - Site Configurable Icons page.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>IconLibrary, ResetConfirmation Update</p>
</blockquote></td>
<td><blockquote>
<p>'Reset' button on Reset Site Configurable Icon page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Information, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Information' link from the bottom of the Home page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MaintainMarquee, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Maintain Marquee Text' link from the Administration Section's menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MaintainMarquee, ChangeMarquee Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the ADMINISTRATION SECTION -</p>
<p>MAINTAIN MARQUEE TEXT page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NationalAndRegional, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, Return to VISN Network link, Return to Regional Page link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NewEvents, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, New Events link.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Numi, Add Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Numi, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' Link on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Numi, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' Link on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Numi, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Numi' tab on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Numi, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button on ADMINISTRATION SECTION</p>
<p>- Background Processors Delete page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Numi, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on ADMINISTRATION SECTION -</p>
<p>Background Processors Add/Edit page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetDomain">http://tempuri.org/IAdministrativeFunctions/GetDomain</a></p>
<p>s</p>
</blockquote></td>
<td rowspan="6"><blockquote>
<p>Functions used in the Administration Section, Add/Edit BMS User and Edit BMS Site submenus.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetCurrent">http://tempuri.org/IAdministrativeFunctions/GetCurrent</a></p>
<p>Domain</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoles">http://tempuri.org/IAdministrativeFunctions/GetRoles</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetBulkPoli">http://tempuri.org/IAdministrativeFunctions/GetBulkPoli</a></p>
<p>cies</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GrantPermi">http://tempuri.org/IAdministrativeFunctions/GrantPermi</a></p>
<p>ssion</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/RevokePer">http://tempuri.org/IAdministrativeFunctions/RevokePer</a></p>
<p>mission</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleBy">http://tempuri.org/IAdministrativeFunctions/GetRoleBy</a></p>
<p>Name</p>
</blockquote></td>
<td rowspan="8"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetPermiss">http://tempuri.org/IAdministrativeFunctions/GetPermiss</a> ionsByResourceType</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetAllUser">http://tempuri.org/IAdministrativeFunctions/GetAllUser</a></p>
<p>sAndDomain</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetAllUser">http://tempuri.org/IAdministrativeFunctions/GetAllUser</a></p>
<p>Roles</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AssignUser">http://tempuri.org/IAdministrativeFunctions/AssignUser</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeassignU">http://tempuri.org/IAdministrativeFunctions/DeassignU</a> ser</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetPolicy">http://tempuri.org/IAdministrativeFunctions/GetPolicy</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/ClearPermi">http://tempuri.org/IAdministrativeFunctions/ClearPermi</a> ssionsForResource</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddActionE">http://tempuri.org/IAdministrativeFunctions/AddActionE</a></p>
<p>ntityType</p>
</blockquote></th>
<th rowspan="22"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddOperati">http://tempuri.org/IAdministrativeFunctions/AddOperati</a></p>
<p>on</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddRole">http://tempuri.org/IAdministrativeFunctions/AddRole</a></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddTask">http://tempuri.org/IAdministrativeFunctions/AddTask</a></p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AssignOper">http://tempuri.org/IAdministrativeFunctions/AssignOper</a></p>
<p>ations</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AssignRole">http://tempuri.org/IAdministrativeFunctions/AssignRole</a></p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/ChangeUse">http://tempuri.org/IAdministrativeFunctions/ChangeUse</a></p>
<p>rPassword</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeassignO">http://tempuri.org/IAdministrativeFunctions/DeassignO</a></p>
<p>perations</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeassignR">http://tempuri.org/IAdministrativeFunctions/DeassignR</a></p>
<p>ole</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteActio">http://tempuri.org/IAdministrativeFunctions/DeleteActio</a></p>
<p>nEntityType</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteOper">http://tempuri.org/IAdministrativeFunctions/DeleteOper</a></p>
<p>ation</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeletePerm">http://tempuri.org/IAdministrativeFunctions/DeletePerm</a></p>
<p>issionForResourceAndOperation</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeletePerm">http://tempuri.org/IAdministrativeFunctions/DeletePerm</a></p>
<p>issionsForResourcesAndOperations</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteRole">http://tempuri.org/IAdministrativeFunctions/DeleteRole</a></p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteTask">http://tempuri.org/IAdministrativeFunctions/DeleteTask</a></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetActionE">http://tempuri.org/IAdministrativeFunctions/GetActionE</a></p>
<p>ntityTypes</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetAvailabl">http://tempuri.org/IAdministrativeFunctions/GetAvailabl</a></p>
<p>eDomains</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetCallerIs">http://tempuri.org/IAdministrativeFunctions/GetCallerIs</a></p>
<p>SuperUser</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetConnec">http://tempuri.org/IAdministrativeFunctions/GetConnec</a></p>
<p>tedRolesAndOperations</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetEntityTy">http://tempuri.org/IAdministrativeFunctions/GetEntityTy</a></p>
<p>pes</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetOperati">http://tempuri.org/IAdministrativeFunctions/GetOperati</a></p>
<p>onByName</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetOperati">http://tempuri.org/IAdministrativeFunctions/GetOperati</a></p>
<p>onByNameExcludingId</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetOperati">http://tempuri.org/IAdministrativeFunctions/GetOperati</a></p>
<p>ons</p>
</blockquote></td>
<td rowspan="8"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleBy">http://tempuri.org/IAdministrativeFunctions/GetRoleBy</a></p>
<p>NameExcludingId</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleDef">http://tempuri.org/IAdministrativeFunctions/GetRoleDef</a></p>
<p>inition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRolesD">http://tempuri.org/IAdministrativeFunctions/GetRolesD</a></p>
<p>efinitionIntersect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleUs">http://tempuri.org/IAdministrativeFunctions/GetRoleUs</a></p>
<p>ers</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetSubscri">http://tempuri.org/IAdministrativeFunctions/GetSubscri</a></p>
<p>ptions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTaskBy">http://tempuri.org/IAdministrativeFunctions/GetTaskBy</a></p>
<p>Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTaskBy">http://tempuri.org/IAdministrativeFunctions/GetTaskBy</a></p>
<p>NameExcludingId</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTaskDe">http://tempuri.org/IAdministrativeFunctions/GetTaskDe</a></p>
<p>finition</p>
</blockquote></th>
<th rowspan="18"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTasks">http://tempuri.org/IAdministrativeFunctions/GetTasks</a></p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserBy">http://tempuri.org/IAdministrativeFunctions/GetUserBy</a></p>
<p>Sid</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserBy">http://tempuri.org/IAdministrativeFunctions/GetUserBy</a></p>
<p>UserName</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserDef">http://tempuri.org/IAdministrativeFunctions/GetUserDef</a></p>
<p>inedRoles</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserGr">http://tempuri.org/IAdministrativeFunctions/GetUserGr</a></p>
<p>oupId</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserRol">http://tempuri.org/IAdministrativeFunctions/GetUserRol</a></p>
<p>es</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/InsertPermi">http://tempuri.org/IAdministrativeFunctions/InsertPermi</a></p>
<p>ssionForResourceAndOperation</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/InsertPermi">http://tempuri.org/IAdministrativeFunctions/InsertPermi</a></p>
<p>ssionsForResourcesAndOperations</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/InsertReso">http://tempuri.org/IAdministrativeFunctions/InsertReso</a></p>
<p>urce</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/IsChild">http://tempuri.org/IAdministrativeFunctions/IsChild</a></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/RefreshCac">http://tempuri.org/IAdministrativeFunctions/RefreshCac</a></p>
<p>he</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/SearchUser">http://tempuri.org/IAdministrativeFunctions/SearchUser</a></p>
<p>s</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/SetCurrent">http://tempuri.org/IAdministrativeFunctions/SetCurrent</a></p>
<p>Domain</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/Syncronize">http://tempuri.org/IAdministrativeFunctions/Syncronize</a></p>
<p>AllSubscribers</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/UpdateOpe">http://tempuri.org/IAdministrativeFunctions/UpdateOpe</a></p>
<p>ration</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/UpdateRole">http://tempuri.org/IAdministrativeFunctions/UpdateRole</a></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/UpdateTas">http://tempuri.org/IAdministrativeFunctions/UpdateTas</a></p>
<p>k</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Patient, Admission Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Home page, Patients Pending</p>
<p>Placement list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient, Select Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add New Patient' link from the Home page, Patients</p>
<p>Pending Placement section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient, Admission Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from ADD/EDIT Patients Pending</p>
<p>Placement page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Active Admission Orders Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Active Admission Orders Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Active Discharge Orders Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Active Discharge Orders Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Active Transfer Orders Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Active Transfer Orders Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Antic Discharge Orders Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Antic Discharge Orders Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, BED AVAILABILITY STATUS REPORT</p>
</blockquote></td>
<td><blockquote>
<p>Access the BED AVAILABILITY STATUS REPORT.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Bed Specialty Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Bed Specialty Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Bed Specialty Roster</p>
</blockquote></td>
<td><blockquote>
<p>Access the Bed Specialty Roster.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Bed Summary Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Bed Summary Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Bed Turnaround Time Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Bed Turnaround Time Report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>rep, Beds Out of Service Report (All)</p>
</blockquote></th>
<th><blockquote>
<p>Access the Beds Out of Service Report (All).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>rep, Beds Out of Service Report (By Date)</p>
</blockquote></td>
<td><blockquote>
<p>Access the Beds Out of Service Report (By Date).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Discharges In Progress</p>
</blockquote></td>
<td><blockquote>
<p>Access the Discharges In Progress.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Emergency Management Evacuation Report</p>
</blockquote></td>
<td><blockquote>
<p>Access Emergency Management Evacuation Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Icon Usage Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Icon Usage Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Patient Inquiry</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patient Inquiry report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Patient Movement Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patient Movement Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Patient Movements by Date</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patient Movements by Date.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Patients w Discharge Appointments</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patients w Discharge Appointments.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Scheduled Admissions by Date</p>
</blockquote></td>
<td><blockquote>
<p>Access the Scheduled Admissions by Date.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Scheduled Admissions Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Scheduled Admissions Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, VISN Bed Summary Report</p>
</blockquote></td>
<td><blockquote>
<p>Access VISN Bed Summary Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, VISN Network Active Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Network Active Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, VISN Network Audit Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Network Audit Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, VISN Network Contract Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Network Contract Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, VISN Network Disposition Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Network Disposition Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Wait List Status Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patients Pending Placement Status Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Reports, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' buttons from the Home page corresponding to the reports.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SiteOptions, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, Site Options link.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SiteOptions, EvacuationConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>Access to Evacuation Confirmation page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SiteOptions, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from Site Options page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SiteOptions, EvacuationConfirmation Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from Evacuation Confirmation page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transfer, AddTransfer Read</p>
</blockquote></td>
<td><blockquote>
<p>VISN page, Add New Patient button, Submit button from the Select Patient page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, EditTransfer Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the VISN page, Patients in Community</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Hospitals list.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, FinalizeTransfer Read</p>
</blockquote></td>
<td><blockquote>
<p>'Finalize' link from the VISN page, Patients in Community Hospitals list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transfer, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>VISN page, Add New Patient button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, AddTransfer Update</p>
</blockquote></td>
<td><blockquote>
<p>VISN page, Add New Patient button, Submit button from the Select Patient page, and Submit button from the Enter Patient Data page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transfer, EditTransfer Update</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the VISN page's Patients in Community</p>
<p>Hospitals list and then Submit button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, FinalizeTransfer Update</p>
</blockquote></td>
<td><blockquote>
<p>'Finalize' link from the VISN page's Patients in</p>
<p>Community Hospitals list and then Submit button from the Finalize Patient Data page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UnavailableReason, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Bed Board Site Unavailable Reason</p>
<p>page's list.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>UnavailableReason, Edit Read</p>
</blockquote></th>
<th><blockquote>
<p>'Edit' link from the Bed Board Site Unavailable Reason</p>
<p>page's list.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>UnavailableReason, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Unavailable Reason Add/Edit link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UnavailableReason, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Bed Board Site Unavailable Reason page's list and then 'Delete Record' button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UnavailableReason, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Bed Board Site Unavailable Reason</p>
<p>page's list and then Submit button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UnavailableReason, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Bed Board Site Unavailable Reason page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UserConfiguration, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Add/Edit BMS User link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UserConfiguration, SearchUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Find and Save' buttons from the 'Select user' page</p>
<p>('Select Existing NT User Name' button from the Site Options, 'Add/Edit BMS User' link ).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UserConfiguration, SelectUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Select Existing NT User Name' button from the Site</p>
<p>Options - Add/Edit BMS User page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UserConfiguration, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Site Options - Add/Edit BMS User page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, Audit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Audit' tab on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu) and 'Filter By' button from the 'Audit' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, Categories Read</p>
</blockquote></td>
<td><blockquote>
<p>'VistA Integration' tab on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, DeleteScheduler Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add new scheduler' link and select a scheduled name</p>
<p>from the 'Scheduled' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Background Processors' link on ADMINISTRATION SECTION.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, Schedulers Read</p>
</blockquote></td>
<td><blockquote>
<p>'Schedulers' tab on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, TestMDWSConnection Read</p>
</blockquote></td>
<td><blockquote>
<p>'TestMDWSConnection' button from the 'VistA Sites' tab.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, TestODBCConnection Read</p>
</blockquote></td>
<td><blockquote>
<p>'TestODBCConnection' button from the 'VistA Sites' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, VistASites Read</p>
</blockquote></td>
<td><blockquote>
<p>'VistA Sites' tab on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, Categories Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save and Run' buttons from the 'VistA Integration' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, DeleteScheduler Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the 'Scheduled' tab and then 'Delete Record' button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, Schedulers Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from the 'Scheduled' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, VistASites Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from the 'VistA Sites' tab.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WaitingArea, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Patient Waiting Areas page's list of</p>
<p>Current Waiting Areas.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WaitingArea, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Patient Waiting Areas page's list of Current Waiting Areas.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WaitingArea, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Waiting Area Add/Delete link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WaitingArea, DeleteAction Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Patient Waiting Areas page's list of Current Waiting Areas and then 'Delete Record button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WaitingArea, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Patient Waiting Areas page's list of</p>
<p>Current Waiting Areas and then Submit button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WaitingArea, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Patient Waiting Areas page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardConfiguration, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Bed Board Ward Configuration, Current Vista Wards list.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>WardConfiguration, Index Read</p>
</blockquote></th>
<th><blockquote>
<p>Site Options, Vista Ward Add/Edit link.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>WardConfiguration, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Vista Ward Add/Edit link, Save button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardConfiguration, DeleteWard Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Vista Ward Add/Edit link, Delete operation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardOccupancy, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Home page corresponding to the</p>
<p>Ward Occupancy.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the BED column from WARD Whiteboard Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, EditPT Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the PT column from the WARD</p>
<p>Whiteboard Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, 'Ward Whiteboard' link.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, NotifyChange Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the BED column from WARD Whiteboard Report and then on the Submit button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WhiteboardStaff, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on the checkbox from the STAFF column from the</p>
<p>WARD Whiteboard Home.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, ShowReport Read</p>
</blockquote></td>
<td><blockquote>
<p>'Export Report' link from the right of the WARD</p>
<p>Whiteboard Home page or WARD Whiteboard Report page, Export Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, Submit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the WARD Whiteboard Home page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteBoard, WardWhiteBoard Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, 'Ward Whiteboard' link, Submit button from the WARD Whiteboard Home.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, ClearAll Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the BED column from WARD Whiteboard Report and then click on the button 'Clear</p>
<p>ALL Comments For ALL Wards Associate To This Bed…'.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteBoard, WardWhiteBoard Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on a staff name from the STAFF column from the</p>
<p>WARD WhiteBoard Report and then click on the image 'Save Staff'.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WhiteboardStaff, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on the checkbox from the STAFF column from</p>
<p>WARD Whiteboard Report and then on the 'Save' button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the BED column from WARD Whiteboard Report and then on the Submit button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Task Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view the definition of a task, select Task definitions from the left-hand panel of the main Policy Manager window and in the list in the right-hand area, double-click the task to display the following dialog window.

> ![](bed-management-solution-version-2-4-technical-manual/080.png)

> <span id="_bookmark155" class="anchor"></span>Figure 79-Task Definition

> To determine what resource type the task refers to, select one or more of the elements in the "*Applies to resource types"* area.

> To view the operations that need to be performed in order to complete the task, select the Definition tab to display it as in the following image:

> ![](bed-management-solution-version-2-4-technical-manual/081.png)

> <span id="_bookmark156" class="anchor"></span>Figure 80-Operations Defining a Task

> Use the Add and Remove buttons to add or remove operations from the list.

> A list with all the tasks, along with corresponding operations of the BMS application, is presented below:

> <span id="_bookmark157" class="anchor"></span>Table 28- BMS Tasks

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 50%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="10"><blockquote>
<p>Admin, Read</p>
</blockquote></td>
<td rowspan="10"><blockquote>
<p>Admin Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>Admin, AddEditUser Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, FacilityEdit Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, SelectUser Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, SisterSiteAddEdit Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, AddUserOperations Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, RemoveUsers Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, SearchUser Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, SearchUsers Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, ClearCache Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td rowspan="2"></td>
<td><blockquote>
<p>Admin, AddEditUser Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, FacilityEdit Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 50%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"><blockquote>
<p>Admin, Update</p>
</blockquote></th>
<th rowspan="3"><blockquote>
<p>Admin Update permission, user has the right to modify</p>
<p>data.</p>
</blockquote></th>
<th><blockquote>
<p>Admin, SisterSiteAddEdit Update</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Admin, AddUserOperations</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Admin, RemoveUserOperations</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>AdminComments, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>AdminComments Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminComments, Delete Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminComments, Edit Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminComments, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminComments, Update</p>
</blockquote></td>
<td><blockquote>
<p>AdminComments Update permission, user has the right to</p>
<p>modify data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminComments, Index Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="5"><blockquote>
<p>AdminIcon, Read</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p>AdminIcon Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminIcon, Delete Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, Edit Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, Search Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, ViewIconReport Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>AdminIcon, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>AdminIcon Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminIcon, Delete Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, Edit Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 44%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>AdminIcon, Index Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>AdminSpecialtyAssociation, Read</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>AdminSpecialtyAssociation Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminSpecialtyAssociation,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminSpecialtyAssociation,</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>AdminSpecialtyAssociation, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>AdminSpecialtyAssociation Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminSpecialtyAssociation,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminSpecialtyAssociation,</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>AdminUnavailableReason, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>AdminUnavailableReason Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminUnavailableReason,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminUnavailableReason, Edit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminUnavailableReason, Index</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>AdminUnavailableReason, Update</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>AdminUnavailableReason Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminUnavailableReason,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminUnavailableReason, Edit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminUnavailableReason, Index</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>AdminWaitingArea, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>AdminWaitingArea Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminWaitingArea, Delete Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWaitingArea, Edit Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWaitingArea, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>AdminWaitingArea, Update</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>AdminWaitingArea Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminWaitingArea, DeleteAction</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWaitingArea, Edit Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWaitingArea, Index Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>AdminWhiteboardReport, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>AdminWhiteboardReport Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminWhiteboardReport, Delete</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWhiteboardReport, Edit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWhiteboardReport, Index</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>AdminWhiteboardReport, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>AdminWhiteboardReport Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>AdminWhiteboardReport, Delete</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWhiteboardReport, Edit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdtOrderableItems, Read</p>
</blockquote></td>
<td><blockquote>
<p>AdtOrderableItems Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>AdtOrderableItems, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>AdtOrderableItems, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>AdtOrderableItems Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>AdtOrderableItems, Delete</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdtOrderableItems, Index Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 44%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>BackgroundProcessors, Read</p>
</blockquote></th>
<th><blockquote>
<p>BackgroundProcessors Read permission, user has the right only to view data.</p>
</blockquote></th>
<th><blockquote>
<p>BackgroundProcessors, Index</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>BackgroundProcessors,</p>
</blockquote></td>
<td><blockquote>
<p>BackgroundProcessors Update permission, user</p>
<p>has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>BackgroundProcessors, Index</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AuditLogReport, Read</p>
</blockquote></td>
<td><blockquote>
<p>AuditLogReport Read permission, user has the</p>
</blockquote></td>
<td><blockquote>
<p>AuditLogReport, Index Read</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 46%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>rep, Audit Log Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4"><blockquote>
<p>BedBoard, Read</p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p>BedBoard Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>BedBoard, ChangeFacility Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedBoard, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedBoard,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedBoard,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedBoardModule, Read</p>
</blockquote></td>
<td><blockquote>
<p>BedBoardModule Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>BedBoardModule, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedBoardModule, Update</p>
</blockquote></td>
<td><blockquote>
<p>BedBoardModule Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>BedBoardModule, Index Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>BedInformation, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>BedInformation Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>BedInformation, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedInformation, ClearAll Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedInformation, NotifyChange Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedInformation, Update</p>
</blockquote></td>
<td><blockquote>
<p>BedInformation Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>BedInformation, Index Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ContingencySettings, Read</p>
</blockquote></td>
<td><blockquote>
<p>ContingencySettings Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>ContingencySettings, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ContingencySettings, Update</p>
</blockquote></td>
<td><blockquote>
<p>ContingencySettings Update permission, user has the</p>
<p>right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>ContingencySettings, Index Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DischargeClinic, Read</p>
</blockquote></td>
<td><blockquote>
<p>DischargeClinic Read permission, user has the right</p>
<p>only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>DischargeClinic, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>DischargeClinic, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>DischargeClinic Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>DischargeClinic, Delete Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DischargeClinic, Index Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>EmsBedStatusAdmin, EMS Supervisor</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>EmsBedStatusAdmin EMS Supervisor permission, user has the right to re-assign the bed cleaning to another person and to batch assign the cleaning to a person.</p>
</blockquote></td>
<td><blockquote>
<p>EmsBedStatusAdmin, EMS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsBedStatusAdmin,</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>EmsBedStatusAdmin, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>EmsBedStatusAdmin Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>EmsBedStatusAdmin, Edit Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsBedStatusAdmin, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsBedStatusAdmin, Update</p>
</blockquote></td>
<td><blockquote>
<p>EmsBedStatusAdmin Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>EmsBedStatusAdmin, Edit Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMSMobile, Read</p>
</blockquote></td>
<td><blockquote>
<p>EMSMobile Read permission, user has the right only</p>
</blockquote></td>
<td><blockquote>
<p>EMSMobile, EMSList Read</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 50%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>view data.</p>
</blockquote></td>
<td><blockquote>
<p>EMSMobile, Users Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>EMSMobile, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>EMSMobile Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>EMSMobile, EMSList Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EMSMobile, Users Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>EmsNotification, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>EmsNotification Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>EmsNotification, AddEdit Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsNotification, AddEditAction</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsNotification, Delete Read</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 50%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>EmsNotification, Index Read</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>EmsNotification, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>EmsNotification Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>EmsNotification, DeleteAction</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsNotification, Index Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>EmsStaff, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>EmsStaff Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>EmsStaff, Delete Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsStaff, Edit Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsStaff, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>EmsStaff, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>EmsStaff Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>EmsStaff, Delete Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsStaff, Edit Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4"><blockquote>
<p>EventNotification, Read</p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p>EventNotification Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>EventNotification,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EventNotification, AddEdit Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EventNotification,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EventNotification, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EventNotification, Update</p>
</blockquote></td>
<td><blockquote>
<p>EventNotification Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>EventNotification, Index Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Exception, Read</p>
</blockquote></td>
<td><blockquote>
<p>Exception Read permission, user has the right only to view</p>
<p>data.</p>
</blockquote></td>
<td><blockquote>
<p>Exception, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="6"><blockquote>
<p>FacilityDiversion, Read</p>
</blockquote></td>
<td rowspan="6"><blockquote>
<p>FacilityDiversion Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>FacilityDiversion, Add Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilityDiversion,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, Edit Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilityDiversion, EditConfirmation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, FilterDiversions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilityDiversion, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, Update</p>
</blockquote></td>
<td><blockquote>
<p>FacilityDiversion Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>FacilityDiversion, Index Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 46%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>FacilitySettings, Read</p>
</blockquote></td>
<td><blockquote>
<p>FacilitySettings Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>FacilitySettings, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilitySettings, Update</p>
</blockquote></td>
<td><blockquote>
<p>FacilitySettings Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>FacilitySettings, Index Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="5"><blockquote>
<p>Home, Read</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p>Home Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>Home, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home, Index2 Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, PatientInquiry Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home, RemoveAdmission Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, UndoRemoveAdmission</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>Home, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Home Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>Home, RemoveAdmissionPost</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, UndoRemoveAdmissionPost</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IconLegend, Read</p>
</blockquote></td>
<td><blockquote>
<p>IconLegend Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>IconLegend, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>IconLibrary, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>IconLibrary Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>IconLibrary, Edit Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IconLibrary, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IconLibrary, ResetConfirmation</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>IconLibrary, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>IconLibrary Update permission, user has the right</p>
</blockquote></td>
<td><blockquote>
<p>IconLibrary, Edit Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IconLibrary, Index Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 46%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>to modify data.</p>
</blockquote></th>
<th><blockquote>
<p>IconLibrary, ResetConfirmation</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Information, Read</p>
</blockquote></td>
<td><blockquote>
<p>Information Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>Information, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MaintainMarquee, Read</p>
</blockquote></td>
<td><blockquote>
<p>MaintainMarquee Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>MaintainMarquee, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MaintainMarquee, Update</p>
</blockquote></td>
<td><blockquote>
<p>MaintainMarquee Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>MaintainMarquee, ChangeMarquee Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NationalAndRegional, Read</p>
</blockquote></td>
<td><blockquote>
<p>NationalAndRegional Read permission, user has</p>
<p>the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>NationalAndRegional, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NewEvents, Read</p>
</blockquote></td>
<td><blockquote>
<p>NewEvents Read permission, user has the right only</p>
<p>to view data.</p>
</blockquote></td>
<td><blockquote>
<p>NewEvents, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>Numi, Read</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>NUMI Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>Numi, Add Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Numi, Delete Read</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"></td>
<td rowspan="2"></td>
<td><blockquote>
<p>Numi, Edit Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Numi, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Numi, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>NUMI Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>Numi, Delete Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Numi, Edit Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="19"><blockquote>
<p>PAP,</p>
<p>User</p>
</blockquote></td>
<td rowspan="19"><blockquote>
<p>PAP permission, the right to access methods exposed by PAP service.</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetDomains">http://tempuri.org/IAdministrativeFunctions/GetDomains</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetCurrentD">http://tempuri.org/IAdministrativeFunctions/GetCurrentD</a>omain</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoles">http://tempuri.org/IAdministrativeFunctions/GetRoles</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetBulkPolic">http://tempuri.org/IAdministrativeFunctions/GetBulkPolic</a>ies</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GrantPermis">http://tempuri.org/IAdministrativeFunctions/GrantPermis</a>sion</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/RevokePerm">http://tempuri.org/IAdministrativeFunctions/RevokePermi</a>ssion</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleByN">http://tempuri.org/IAdministrativeFunctions/GetRoleByN</a>ame</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetPermissi">http://tempuri.org/IAdministrativeFunctions/GetPermissi</a>onsByRes ourceType</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetAllUsers">http://tempuri.org/IAdministrativeFunctions/GetAllUsers</a></p>
<p>AndDomain</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetAllUserR">http://tempuri.org/IAdministrativeFunctions/GetAllUserR</a>oles</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AssignUser">http://tempuri.org/IAdministrativeFunctions/AssignUser</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeassignUs">http://tempuri.org/IAdministrativeFunctions/DeassignUs</a>er</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetPolicy">http://tempuri.org/IAdministrativeFunctions/GetPolicy</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/ClearPermis">http://tempuri.org/IAdministrativeFunctions/ClearPermis</a> sionsForResource</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddActionEn">http://tempuri.org/IAdministrativeFunctions/AddActionEn</a>tityType</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddOperatio">http://tempuri.org/IAdministrativeFunctions/AddOperatio</a>n</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddRole">http://tempuri.org/IAdministrativeFunctions/AddRole</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddTask">http://tempuri.org/IAdministrativeFunctions/AddTask</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AssignOpera">http://tempuri.org/IAdministrativeFunctions/AssignOpera</a>tions</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"></th>
<th rowspan="2"></th>
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AssignRole">http://tempuri.org/IAdministrativeFunctions/AssignRole</a></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/ChangeUser">http://tempuri.org/IAdministrativeFunctions/ChangeUser</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="22"></td>
<td rowspan="22"></td>
<td><blockquote>
<p>Password</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeassignOp">http://tempuri.org/IAdministrativeFunctions/DeassignOp</a>erations</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeassignRol">http://tempuri.org/IAdministrativeFunctions/DeassignRol</a>e</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteAction">http://tempuri.org/IAdministrativeFunctions/DeleteAction</a> EntityType</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteOpera">http://tempuri.org/IAdministrativeFunctions/DeleteOpera</a>tion</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeletePermi">http://tempuri.org/IAdministrativeFunctions/DeletePermi</a>ssionForResourceAndOperatio</p>
<p>n</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeletePermi">http://tempuri.org/IAdministrativeFunctions/DeletePermi</a>ssionsForResourcesAndOperati</p>
<p>ons</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteRole">http://tempuri.org/IAdministrativeFunctions/DeleteRole</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteTask">http://tempuri.org/IAdministrativeFunctions/DeleteTask</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetActionEn">http://tempuri.org/IAdministrativeFunctions/GetActionEn</a>tityTypes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetAvailable">http://tempuri.org/IAdministrativeFunctions/GetAvailable</a> Domains</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetCallerIsS">http://tempuri.org/IAdministrativeFunctions/GetCallerIsS</a>uperUser</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetConnect">http://tempuri.org/IAdministrativeFunctions/GetConnect</a>edRolesAndOperations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetEntityTyp">http://tempuri.org/IAdministrativeFunctions/GetEntityTyp</a>es</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetOperatio">http://tempuri.org/IAdministrativeFunctions/GetOperatio</a>nByName</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetOperatio">http://tempuri.org/IAdministrativeFunctions/GetOperatio</a> nByNameExcludingId</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetOperatio">http://tempuri.org/IAdministrativeFunctions/GetOperatio</a>ns</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleByN">http://tempuri.org/IAdministrativeFunctions/GetRoleByN</a>ameExcludingId</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleDefi">http://tempuri.org/IAdministrativeFunctions/GetRoleDefi</a>nition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRolesDef">http://tempuri.org/IAdministrativeFunctions/GetRolesDef</a>initionIntersect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleUser">http://tempuri.org/IAdministrativeFunctions/GetRoleUser</a>s</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetSubscript">http://tempuri.org/IAdministrativeFunctions/GetSubscripti</a>ons</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 28%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="5"></td>
<td rowspan="5"></td>
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTaskByN">http://tempuri.org/IAdministrativeFunctions/GetTaskByN</a>ame</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTaskByN">http://tempuri.org/IAdministrativeFunctions/GetTaskByN</a>ameExcludin gId</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTaskDefi">http://tempuri.org/IAdministrativeFunctions/GetTaskDefi</a>nition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTasks">http://tempuri.org/IAdministrativeFunctions/GetTasks</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserBySi">http://tempuri.org/IAdministrativeFunctions/GetUserBySi</a>d</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 28%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="15"></th>
<th rowspan="15"></th>
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserByU">http://tempuri.org/IAdministrativeFunctions/GetUserByU</a>serName</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserDefi">http://tempuri.org/IAdministrativeFunctions/GetUserDefi</a>nedRoles</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserGro">http://tempuri.org/IAdministrativeFunctions/GetUserGro</a>upId</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserRole">http://tempuri.org/IAdministrativeFunctions/GetUserRole</a>s</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/InsertPermis">http://tempuri.org/IAdministrativeFunctions/InsertPermis</a>sionForResou</p>
<p>rceAndOperation</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/InsertPermis">http://tempuri.org/IAdministrativeFunctions/InsertPermis</a>sionsForReso</p>
<p>urcesAndOperations</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/InsertResour">http://tempuri.org/IAdministrativeFunctions/InsertResour</a>ce</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/IsChild">http://tempuri.org/IAdministrativeFunctions/IsChild</a></p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/RefreshCac">http://tempuri.org/IAdministrativeFunctions/RefreshCac</a>he</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/SearchUsers">http://tempuri.org/IAdministrativeFunctions/SearchUsers</a></p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/SetCurrentD">http://tempuri.org/IAdministrativeFunctions/SetCurrentD</a>omain</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/SyncronizeA">http://tempuri.org/IAdministrativeFunctions/SyncronizeA</a>llSubscribers</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/UpdateOper">http://tempuri.org/IAdministrativeFunctions/UpdateOper</a>ation</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/UpdateRole">http://tempuri.org/IAdministrativeFunctions/UpdateRole</a></p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/UpdateTask">http://tempuri.org/IAdministrativeFunctions/UpdateTask</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Patient, Read</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Patient Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>Patient, Admission Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient, Select Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient, Update</p>
</blockquote></td>
<td><blockquote>
<p>Patient Update permission, user has the right to modify</p>
<p>data.</p>
</blockquote></td>
<td><blockquote>
<p>Patient, Admission Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reporting</p>
<p>Services, Fetch</p>
</blockquote></td>
<td><blockquote>
<p>Reporting Services Fetch permission, the right to bring</p>
</blockquote></td>
<td><blockquote>
<p>rep, Active Admission Orders Report</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 44%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="16"></td>
<td rowspan="16"><blockquote>
<p>the list of reports from Reporting Services.</p>
</blockquote></td>
<td><blockquote>
<p>rep, Active Discharge Orders Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Active Transfer Orders Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Antic Discharge Orders Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, BED AVAILABILITY STATUS REPORT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Bed Specialty Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Bed Specialty Roster</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Bed Summary Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Bed Turnaround Time Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Beds Out of Service Report (All)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Beds Out of Service Report (By Date)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Discharges In Progress</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Emergency Management Evacuation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Icon Usage Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Patient Inquiry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Patient Movement Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Patient Movements by Date</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 44%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="9"></th>
<th rowspan="9"></th>
<th><blockquote>
<p>rep, Patients w Discharge Appointments</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>rep, Scheduled Admissions by Date</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>rep, Scheduled Admissions Report</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>rep, VISN Bed Summary Report</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>rep, VISN Network Active Report</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>rep, VISN Network Audit Report</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>rep, VISN Network Contract Report</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>rep, VISN Network Disposition Report</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>rep, Wait List Status Report</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Reports, Read</p>
</blockquote></td>
<td><blockquote>
<p>Reports permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>Reports, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>SiteOptions, Read</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>SiteOptions permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>SiteOptions, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SiteOptions, EvacuationConfirmation Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SiteOptions,</p>
</blockquote></td>
<td><blockquote>
<p>SiteOptions Update permission, user has the right</p>
</blockquote></td>
<td><blockquote>
<p>SiteOptions, Index Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 46%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>modify data.</p>
</blockquote></td>
<td><blockquote>
<p>SiteOptions, EvacuationConfirmation</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4"><blockquote>
<p>Transfer, Read</p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p>Transfer permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>Transfer, AddTransfer Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, EditTransfer Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transfer, FinalizeTransfer Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>Transfer, Update</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>Transfer Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>Transfer, AddTransfer Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, EditTransfer Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transfer, FinalizeTransfer Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>UnavailableReason, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>UnavailableReason Read permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>UnavailableReason, Delete Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UnavailableReason, Edit Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UnavailableReason, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>UnavailableReason, Update</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>UnavailableReason Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>UnavailableReason, Delete Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UnavailableReason, Edit Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UnavailableReason, Index Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>UserConfiguration, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>UserConfiguration permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>UserConfiguration, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UserConfiguration, SearchUser</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UserConfiguration, SelectUser Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UserConfiguration, Update</p>
</blockquote></td>
<td><blockquote>
<p>UserConfiguration Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>UserConfiguration, Index Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="8"><blockquote>
<p>VistaIntegration, Read</p>
</blockquote></td>
<td rowspan="8"><blockquote>
<p>VistaIntegration permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>VistaIntegration, Audit Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, Categories Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, DeleteScheduler</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, Schedulers Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration,</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, VistASites Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>VistaIntegration, Categories Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 46%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"><blockquote>
<p>VistaIntegration, Update</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>VistaIntegration Update permission, user has the</p>
<p>right to modify data.</p>
</blockquote></th>
<th><blockquote>
<p>VistaIntegration, DeleteScheduler</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>VistaIntegration, Schedulers Update</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 47%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>VistaIntegration, VistASites Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>WaitingArea, Read</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>WaitingArea permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>WaitingArea, Delete Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WaitingArea, Edit Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WaitingArea, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="3"><blockquote>
<p>WaitingArea, Update</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>WaitingArea Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>WaitingArea, DeleteAction Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WaitingArea, Edit Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WaitingArea, Index Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>WardConfiguration, Read</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>WardConfiguration permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>WardConfiguration, Delete Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardConfiguration, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>WardConfiguration, Update</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>WardConfiguration Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>WardConfiguration, Index Update</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardConfiguration, DeleteWard</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardOccupancy, Read</p>
</blockquote></td>
<td><blockquote>
<p>WardOccupancy permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>WardOccupancy, Index Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="9"><blockquote>
<p>WardWhiteboard, Read</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>WardWhiteboard permission, user has the right only to view data.</p>
</blockquote></td>
<td><blockquote>
<p>WardWhiteboard, Edit Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, EditPT Read</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, NotifyChange</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WhiteboardStaff, Index Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, ShowReport</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, Submit Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteBoard, WardWhiteBoard</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, ClearAll Read</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>WardWhiteboard, Update</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>WardWhiteboard Update permission, user has the right to modify data.</p>
</blockquote></td>
<td><blockquote>
<p>WardWhiteBoard, WardWhiteBoard</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WhiteboardStaff, Index Update</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, Edit Update</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Role Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view the actual definition of a BMS user role, from the Definitions folder select Role Definitions and double click the role name in the main panel of Policy Manager: in the Role Definition Properties dialog window, select the Definition tab to display it as in the following image:

> ![](bed-management-solution-version-2-4-technical-manual/082.png)

> <span id="_bookmark159" class="anchor"></span>Figure 81-Role Definition

## Assigning a Role to a User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To assign one of the roles defined for BMS to a user follow the steps below.

> From the main page of Policy Manager, from Role assignments folder select a role then right-click and select "*Assign Windows Users and Groups"*: the following dialog is displayed.

![](bed-management-solution-version-2-4-technical-manual/083.png)

> <span id="_bookmark161" class="anchor"></span>Figure 82-Assigning Roles to Users

> A list of users and user groups existing in the current domain are displayed. Use the arrow button of the field in the upper left corner of the dialog to select the domain and the Filter field if necessary, and then click each applicable check box to select the user or group of users for which you want to assign the selected BMS role. Click OK to finalize the operation.

## Adding a New Role

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To add a new role, click the Add Role button from the main Policy Manager window or right-click Role Definitions folder and select New Role Definition…: the following dialog window is displayed:

![](bed-management-solution-version-2-4-technical-manual/084.png)

> <span id="_bookmark163" class="anchor"></span>Figure 83-New Role Definition

> Enter the name of the new role and a short description.

> To add the tasks and operations that can be performed for this role click the Add button to display the following dialog window:

> ![](bed-management-solution-version-2-4-technical-manual/085.png)

> <span id="_bookmark164" class="anchor"></span>Figure 84-Adding Tasks and Operations to a Role

> Tasks and operations that can be performed within the BMS system are available in separate tabs. Select the ones to be included in the definition of the current role (the number of selected tasks/operations will be displayed in the corresponding tab title) then press OK:

> The selected tasks and operations will be displayed in the New Role Definition dialog box. Press OK to add the role to the list of roles defined for BMS: The Roles Definitions list will be updated to contain the new role. To add the new role to the Role Assignment folder, select the folder, right-click and select Assign Roles to display the following dialog window:

> ![](bed-management-solution-version-2-4-technical-manual/086.png)

> <span id="_bookmark165" class="anchor"></span>Figure 85-Add Role to Role Assignments List

> Select the role then press OK: The newly added role will be displayed in the Role Assignments list and you will be able to assign the new role to BMS users.

## Adding a New Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To add a new task, click the Add Task button from the main Policy Manager window or right-click Task Definitions folder and select New Task Definition: The following dialog window is displayed:

> ![](bed-management-solution-version-2-4-technical-manual/087.png)

> <span id="_bookmark167" class="anchor"></span>Figure 86-New Task Definition

> Enter the name of the new task followed by read/write option and a short description.

> To add the operations that define the Task, click the Add button to display the following dialog window:

> ![](bed-management-solution-version-2-4-technical-manual/088.png)

> <span id="_bookmark168" class="anchor"></span>Figure 87-Adding Operations to a Task

> Select the operations that define the selected task then click OK to return to the New Task Definition dialog box. Click OK to add the new task to the Task Definitions list.

## Adding a New Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To add a new operation, click the Add Operation button from the main Policy Manager window or right- click Operation Definitions folder and select New Operation Definition: The following dialog window is displayed.

![](bed-management-solution-version-2-4-technical-manual/089.png)

> <span id="_bookmark170" class="anchor"></span>Figure 88-New Operation Definition

> Enter the name of the new operation followed by read/write option and a short description. Click OK to add the new operation to the Operation Definitions list.

## Business scenarios and use cases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Authentication

> ![](bed-management-solution-version-2-4-technical-manual/090.png)

> <span id="_bookmark172" class="anchor"></span>Figure 89-Authentication Use Cases

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>Section</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Description</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Use Case Name</strong></p>
</blockquote></td>
<td><blockquote>
<p>User authentication</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Summary</strong></p>
</blockquote></td>
<td><blockquote>
<p>In the above diagram it is represented the methods that a client application can use to authenticate their users.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Preconditions</strong></p>
</blockquote></td>
<td><blockquote>
<p>The users, that will use the client application, need to be defined in an Active Directory</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Triggers</strong></p>
</blockquote></td>
<td><blockquote>
<p>External</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Basic course of events</strong></p>
</blockquote></td>
<td><ol type="1">
<li><p>The client application will send the user and the password or windows credentials</p></li>
<li><p>The system verifies the login information.</p></li>
<li><p>The system returns the result of the verification to the client application.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Alternative paths</strong></p>
</blockquote></td>
<td><ol type="1">
<li><p>The client application will send the X509 certificate of his user</p></li>
<li><p>The system verifies the certificate</p></li>
<li><p>The system returns the result</p></li>
</ol></td>
</tr>
</tbody>
</table>

#### Authorization

> ![](bed-management-solution-version-2-4-technical-manual/091.png)

User

> <span id="_bookmark173" class="anchor"></span>Figure 90-Authorization Use Cases

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>Section</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Description</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Use Case Name</strong></p>
</blockquote></td>
<td><blockquote>
<p>User authorization</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Summary</strong></p>
</blockquote></td>
<td><blockquote>
<p>In the above diagram it is represented the methods that a client application can use to check if an authenticated user has access to a specified action on a resource.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Preconditions</strong></p>
</blockquote></td>
<td><blockquote>
<p>The users, actions and resources must be defined in an Active Directory structure that the Security Service is using.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Triggers</strong></p>
</blockquote></td>
<td><blockquote>
<p>External</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Basic course of events</strong></p>
</blockquote></td>
<td><ol type="1">
<li><p>The client application will invoke a check access method for a specified action on a specific resource</p></li>
<li><p>The system will find the actions that the requesting users has access</p></li>
<li><p>The system returns true/false if the action requested is among the users defined actions</p></li>
</ol></td>
</tr>
</tbody>
</table>

![](bed-management-solution-version-2-4-technical-manual/092.png)

> <span id="_bookmark174" class="anchor"></span>Figure 91- Authorization Administration Use Cases

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>Section</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Description</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Use Case Name</strong></p>
</blockquote></td>
<td><blockquote>
<p>Action and resource management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Summary</strong></p>
</blockquote></td>
<td><blockquote>
<p>Administrative console can define actions and resources and associate an action with a resource type.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Preconditions</strong></p>
</blockquote></td>
<td><blockquote>
<p>The association method mandates that the action and the resource type should already be defined</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Triggers</strong></p>
</blockquote></td>
<td><blockquote>
<p>External</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Basic course of events</strong></p>
</blockquote></td>
<td><ol type="1">
<li><p>The client application will invoke a create action</p></li>
<li><p>The system will try to create requested action.</p></li>
<li><p>The system will fail if the specified action name already exists, or specified id already exists.</p></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>Section</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Description</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Use Case Name</strong></p>
</blockquote></td>
<td><blockquote>
<p>Role management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Summary</strong></p>
</blockquote></td>
<td><blockquote>
<p>Administrative console can define user roles and associate users/user groups with roles.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Preconditions</strong></p>
</blockquote></td>
<td><blockquote>
<p>The association method mandates that the role should already be defined</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Triggers</strong></p>
</blockquote></td>
<td><blockquote>
<p>External</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Basic course of events</strong></p>
</blockquote></td>
<td><ol type="1">
<li><p>The client application will invoke a create role</p></li>
<li><p>The system will try to create requested role.</p></li>
<li><p>The system will fail if the specified role name already exists, or specified id already exists.</p></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>Section</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Description</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Use Case Name</strong></p>
</blockquote></td>
<td><blockquote>
<p>Security policy management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Summary</strong></p>
</blockquote></td>
<td><blockquote>
<p>Administrative console can associate users (groups of users) with roles.</p>
<p>These roles are then associated with and action (operation).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Preconditions</strong></p>
</blockquote></td>
<td><blockquote>
<p>The association method mandates that the action and the resource type should already be defined.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Triggers</strong></p>
</blockquote></td>
<td><blockquote>
<p>External</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Detailed Functional Model on Each Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Service contracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Authentication

> The security service for authentication is represented by STS – security token cache that will issue a token whether the authentication succeeded, otherwise it will deny access to the application server. This STS Service will authenticate the user through WS-Security and validate application servers through WS-Trust using SAML v2.0 Token (Security Assertion Markup Language).

#### Authorization

> The security services for authorization are represented by a PDP and PAP implementation. PDP stands for policy decision point where the authenticated user can check the permission for a specified action on a specified resource. PAP stands for policy administration point. Here an administrative console can define actions, resource-types, roles and make associations with them (define security policies) that will server for PDP. The PDP service exposes one method: CheckAccess, whilst PAP service has specific functions for policy administration.

#### Detailed functional model on each interface

> STS – Security Token Service

- Authenticate

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Business friendly name</strong></p>
</blockquote></th>
<th><blockquote>
<p>User authentication</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
<td><blockquote>
<p>The function decides if the user and the password supplied as parameters</p>
<p>are valid. Will return true on success and false on any failure.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Inputs</strong></p>
</blockquote></td>
<td><blockquote>
<p>Windows client credentials or</p>
<p>Username – representing the username of the requested user.</p>
<p>Password – the password of the requested user.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Outputs</strong></p>
</blockquote></td>
<td><blockquote>
<p>True - on success False – on failure</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PDP – Policy Decision Point

- CheckPermission

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Business friendly name</strong></p>
</blockquote></th>
<th><blockquote>
<p>User authorization – check Access</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Signature</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>Message</em> CheckAccess (<em>Message</em> request);</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
<td><blockquote>
<p>The function decides if the user has the privilege to access the specified action(s) on the specified resource.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Inputs</strong></p>
</blockquote></td>
<td><blockquote>
<p>Username, operation name and resource id are encapsulated in the SAML</p>
<p>Message class</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Outputs</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Message containing the permit or deny result.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### PAP – Policy Administration Point

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Input</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Output</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><em><strong>AddRole</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Adds a role</p>
</blockquote></td>
<td><blockquote>
<p><em>String name</em> – name of the new role</p>
<p><em>String</em> description – role description</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> – new role's id</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>Delete Role</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Delete a role</p>
</blockquote></td>
<td><blockquote>
<p><em>String id</em> – role's id</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> – deleted role's id</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Update Role</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Update a role</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> id – role's id</p>
<p><em>String</em> name – role's name</p>
<p><em>String</em> description –role's description</p>
</blockquote></td>
<td><blockquote>
<p><em>bool</em> – operation result: <em>true</em> on succeeded; <em>false</em> if any error</p>
<p>aroused</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>Update Task</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Update a task</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> id – task's id</p>
<p><em>String</em> name –task's name <em>String</em> description – task's description</p>
</blockquote></td>
<td><blockquote>
<p><em>bool</em> – operation result: <em>true</em> on succeeded; <em>false</em> if any error aroused</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Update Operation</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Update an operation</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> id – operation's id</p>
<p><em>String</em> name – operation's name <em>String</em> description – operation's description</p>
</blockquote></td>
<td><blockquote>
<p><em>bool</em> – operation result: <em>true</em> on succeeded; <em>false</em> if any error aroused</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>IsChild</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Verifies if the sent operation is part of a</p>
<p>task</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> id – operation id</p>
</blockquote></td>
<td><blockquote>
<p><em>bool</em> – operation result</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Assign User</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Assign an user to a role</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> userId – user's id (SID)</p>
<p><em>String</em> roleId – role's id</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>DeassignUser</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Delete an association between an user and a</p>
<p>role</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> userId – user's id (SID)</p>
<p><em>String</em> roleId – role's id</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Grant</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Grant access to a</p>
</blockquote></td>
<td><blockquote>
<p><em>string</em> resourceId, <em>string</em> actionId,</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>Permission</strong></em></p>
</blockquote></th>
<th><blockquote>
<p>resource for a role on an action</p>
</blockquote></th>
<th><blockquote>
<p><em>string</em> roleId</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><em><strong>Revoke</strong></em></p>
<p><em><strong>Permission</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Revokes a permission</p>
</blockquote></td>
<td><blockquote>
<p><em>string</em> resourceId, <em>string</em> actionId,</p>
<p><em>string</em> roleId</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>GetRoles</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a list with all stored roles</p>
</blockquote></td>
<td><blockquote>
<p><em>Bool</em> assignedOnly - returns assigned roles if parameter is true</p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;Role&gt;</em> - retrieved roles</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Get Operations</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a list with all stored operations</p>
</blockquote></td>
<td><blockquote>
<p>-</p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;Operation&gt;</em> - retrieved operations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>GetTasks</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a list with all</p>
<p>stored tasks</p>
</blockquote></td>
<td><blockquote>
<p>-</p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;Task&gt;</em> - retrieved tasks</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Add Operation</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Add a new operation</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> name – operation's name <em>String</em> description – operation's description</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> id <em>– operation's id</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>Delete</strong></em></p>
<p><em><strong>Operation</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Delete an operation</p>
</blockquote></td>
<td><blockquote>
<p><em>String – operation's id</em></p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>AddTask</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Add a new task</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> name – task's name <em>String</em> description – task's description</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> id<em>– tasks's id</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>Delete</strong></em></p>
<p><em><strong>Task</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Delete a task</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> id<em>– tasks's id</em></p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Assign Operations</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Associate operations to a task</p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;String&gt;</em> operationIds – list of operations to be assigned</p>
<p><em>String</em> taskId – task's id</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>DeassignOperations</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Deassign operations from a task</p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;String&gt;</em> operationIds – list of operations to be assigned</p>
<p><em>String</em> taskId – task's id</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>GetTaskDefinition</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Retrieve a list with all operations of the specified task</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> id<em>– tasks's id</em></p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;DefinitionBase&gt; -</em> operation list</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>GetRole Definition</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns all associated operations to a</p>
<p>specified role</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> roleId – role's id</p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;DefinitionBase&gt; -</em> operation list</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>GetRole ByName</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a role by name</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> name – role's name</p>
</blockquote></td>
<td><blockquote>
<p><em>Role</em> – returned role</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>GetRole</strong></em></p>
<p><em><strong>ByName Excluding</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a role by name</p>
<p>excluding the role id sent by parameter</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> name – role's name</p>
<p><em>Guid</em> id – role's id</p>
</blockquote></td>
<td><blockquote>
<p><em>Role</em> – returned role</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>GetTask</strong></em></p>
<p><em><strong>ByName</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a task by name</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> name – task's name</p>
</blockquote></td>
<td><blockquote>
<p><em>Task</em> – returned task</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>GetTask ByName ExcludingId</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a task by name excluding the task id sent by parameter</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> name – task's name</p>
<p><em>Guid</em> id – task's id</p>
</blockquote></td>
<td><blockquote>
<p><em>Task</em> – returned task</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Get</strong></em></p>
<p><em><strong>Operation ByName</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns an operation by name</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> name <em>–</em> operation's name</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation</em> – returned operation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>Get Operation ByName</strong></em></p>
<p><em><strong>ExcludingId</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns an operation by name excluding the operation id sent by</p>
<p>parameter</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> name – operation's name</p>
<p><em>Guid</em> id – operation's id</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation</em> – returned operation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Get Permissions By Resource</strong></em></p>
<p><em><strong>Type</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a list with operations/task associated with a resource ype</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> resourceType – Resource type</p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;DefinitionBase&gt;</em> –</p>
<p>operation/task list</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>GetPolicy</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a list with all roles and operations associated with the</p>
<p>resource</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> resourceId – resource's id</p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;Role&gt;</em> – role list. Each role has the associated operations.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>GetRole Users</strong></em></p>
</blockquote></th>
<th><blockquote>
<p>Returns a list with all users associated to a specific role</p>
</blockquote></th>
<th><blockquote>
<p><em>Guid</em> roleId <em>–</em> role's id</p>
</blockquote></th>
<th><blockquote>
<p><em>List&lt;User&gt;</em> – user list</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><em><strong>Assign</strong></em></p>
<p><em><strong>Role</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Marks a role as</p>
<p>assigned</p>
</blockquote></td>
<td><blockquote>
<p><em>Guid</em> roleId <em>–</em> role's id</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>Deassign</strong></em></p>
<p><em><strong>Role</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Marks a role as</p>
<p>unassigned</p>
</blockquote></td>
<td><blockquote>
<p><em>Guid</em> roleId <em>–</em> role's id</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Get Connected</strong></em></p>
<p><em><strong>RolesAndOperations</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Returns a list with all roles and operations associated with the resource</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> resourceId – resource's id</p>
</blockquote></td>
<td><blockquote>
<p><em>List&lt;Role_Operation&gt;</em> – list with role-operations associations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>Clear Permissions For Resource</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Removes all permissions for a certain resource (all associations to this</p>
<p>resource)</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> resourceId – resource's id</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>Delete PermissionFor Resource</strong></em></p>
<p><em><strong>And</strong></em></p>
<p><em><strong>Operation</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Deletes a permission form a role based on the resource and operation sent.</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> resourceId – resource's id</p>
<p><em>String</em> roleId <em>–</em> role's id</p>
<p><em>String</em> actionGUID – operation's id</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>Insert PermissionFor Resource</strong></em></p>
<p><em><strong>And Operation</strong></em></p>
</blockquote></td>
<td><blockquote>
<p>Creates a permission for a certain role and an operation on a resource. It automatically creates the association within the permission and the operation if it doesn't</p>
<p>exist.</p>
</blockquote></td>
<td><blockquote>
<p><em>String</em> resourceId – resource's id</p>
<p><em>String</em> roleId <em>–</em> role's id</p>
<p><em>String</em> actionGUID – operation's id</p>
</blockquote></td>
<td><blockquote>
<p><em>-</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> The security services do not expose a fault contract as usual web services do. Instead, these services deliver information about any issue in processing the request in the return message of the service call (such as authentication error, authorization error etc.).

## Data contracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bed-management-solution-version-2-4-technical-manual/093.png)

> <span id="_bookmark178" class="anchor"></span>Figure 92-Class Diagram for Data Contracts in PAP and PDP

## BMS Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS users fall under the following categories:

> Administrators: This type of user will customize the BMS settings according to the needs of a facility. They will have access to the Site Options pages. This role refers to a group of users whose members are the person(s) responsible for setting up BMS options for the current facility.

> AuditLogUsers: This type of user will have access to Audit Log Report. This role cannot be used alone, only together with another role.

> EmsStaff: The EMS group of users will be allowed to edit and update the bed cleaning process but not the other parts of the bed board. Any member of your EMS staff that will be interacting with BMS must be in this group.

> EMSSupervisorUsers: The EMS supervisor group of users will be allowed to view the requests for bed clean

> operations, to filter existing requests by different criteria and to select requests in order to assign them to EMS staff. This role cannot be used alone, only together with EmsStaff role.

> Guests: The guest user will be allowed to generate the National Bed Availability report from National/Regional page.

> National Users/Regional Users: This type of user will have access to the National/Regional page only.

> Site Users: This type of user only has access to the BMS facility page.

> Support Users: This type of user will have access to the Administrative page of the BMS solution. They configure the sites for the BMS facilities and grant access and read/write rights to the users.

> VISN Users: This type of user will have access to the pages of different facilities within the VISN where they have been granted access.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains information on common issues with using BMS solution and how those may be resolved.

#### Symptom 1

> ![](bed-management-solution-version-2-4-technical-manual/094.png)When you try to load the BMS application, one of the following error messages appear:

> <span id="_bookmark181" class="anchor"></span>Figure 93-500 Server Error

> Problem

> IIS is not started/running.

#### Diagnoses and Solutions

> Start the IIS Manager and check if the Application Pool Identity is set to the correct service account. (). Verify the BMS pool is started, If stopped right click on the BMS, Select 'Start'.

> Verify the Site 'BMS' is started. If not select 'BMS' under the Site folder in IIS Manager, select 'Start' from the 'Manage Web Site' panel on the right side of the IIS Manager.

#### Symptom 2

> When trying to load the BMS application, one of the following error messages appears:

![](bed-management-solution-version-2-4-technical-manual/095.png)

> <span id="_bookmark182" class="anchor"></span>Figure 94-No Facilities Error

#### Diagnoses and Solutions

> Go to the MULx5 machine and check if the BMS.ServiceHost service is stopped. Start the services.msc console and start the service.

> Verify the service started.

#### Symptom 3

> When trying to load the BMS application, one of the following error messages appears:

![](bed-management-solution-version-2-4-technical-manual/096.png)

> <span id="_bookmark183" class="anchor"></span>Figure 95-Unhandled Exception

#### Diagnoses and Solutions

- Check if BMS.BMService service is stopped or SQL Server might also have stopped.
- Go to the SQL Server machine and start the SQL Server from the SQL Server Configuration Manager. Verify if the connection string to the database server is set properly.
- Then go to the services' machine, start the services.msc console and start the BMS.BMService service.

#### Symptom 4

> When trying to log-in to the BMS application, the following error is displayed:

> ![](bed-management-solution-version-2-4-technical-manual/097.png)

> <span id="_bookmark184" class="anchor"></span>Figure 96-Login Unsuccessful

> Diagnoses and Solutions

> Check if BMS.BMService service is stopped. Go to the services' machine, start the services.msc console and start the service.

#### Symptom 5

> Data does not appear in the reports. Data does not get refreshed in the reports.

#### Diagnoses and Solutions

> In SQL Configuration Manager, check if the SQL Server Agent is started, and if it isn't start it; then, in the SQL Server Management Studio, check if the *BMS - Reports Full* and *BMS - Reports Incremental* are deployed and run without errors. If the jobs are not deployed, install them.

#### Symptom 6

> A report is missing from Other Reports section on the Facility Home Page (e.g. *EMS Bed Status Report (Admin)*).

> ![](bed-management-solution-version-2-4-technical-manual/098.png)

> <span id="_bookmark185" class="anchor"></span>Figure 97- EMS Bed Status Report is Missing

> Diagnoses and Solutions

> Check if the report is missing from the SQL Server Reporting Services. Go to the management web page and add the missing report (Upload File).

#### Symptom 7

> When trying to view one of the reports (other than the *Other Reports*) the following error appears:

![](bed-management-solution-version-2-4-technical-manual/099.png)

> <span id="_bookmark186" class="anchor"></span>Figure 98- Report Cannot be Found

> Diagnoses and Solutions

> Check if the mentioned report is missing from the Reporting Services. Go to the management web page and add the specified report.

#### BMS Log Files

> There are five log files available to anyone supporting the BMS system, the WinServiceHost, the

> SecurityHost, the BMS.ServiceHost, the

> BMS.VI.ServiceHost and the WebTrace log.

- The WinServiceHost log file is named BMS-Services.log and its location is on the application server (vaausbmsmulx5) D:\BMS\Bin.
- The SecurityHost log file is named BMS-Security.log and its location is on the application server

> (vaausbmsmulx5) D:\BMS\Bin.

- The BMS.ServiceHost logfile is named BMS.trace.log and its location is on the application server (vaausbmsmulx5) at D:\BMS\Bin\BMS.
- The BMS.VI.ServiceHost logfile is named BMS.VI.trace.log and its location is on the application server (vaausbmsmulx6) at D:\BMS\Bin\BMS.
- The Web trace log is named WebTrace.log and its location is on the web server (vaausbmswebx5) at D:\BMS\BMS.Web.

> These logs contain various types of information (informational, warnings, and errors) with the exception of the web trace log, which only contains error messages.

> There is no log file for MDWS, those errors are captured through our integration calls and posted in the BMS.ServiceHost log file (Trace.log). These are bit trickier to debug as in any attempt requires the exact parameters to be passed to MDWS.

# Appendix A – BMS Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Business Process Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bed-management-solution-version-2-4-technical-manual/100.png)

> <span id="_bookmark189" class="anchor"></span>Figure 99-Admit Patient to PPBP Business Process

> ![](bed-management-solution-version-2-4-technical-manual/101.png)

> ![](bed-management-solution-version-2-4-technical-manual/102.png)<span id="_bookmark190" class="anchor"></span>Figure 100-Transfer Patients to PPBP Business Process

> <span id="_bookmark191" class="anchor"></span>Figure 101-Display and Update PPBP Business Process

> ![](bed-management-solution-version-2-4-technical-manual/103.png)

> ![](bed-management-solution-version-2-4-technical-manual/104.png)<span id="_bookmark192" class="anchor"></span>Figure 102-Display and Update Bed Status Business Process

> <span id="_bookmark193" class="anchor"></span>Figure 103-Manage Bed Cleaning Business Process

> ![](bed-management-solution-version-2-4-technical-manual/105.png)

> <span id="_bookmark194" class="anchor"></span>Figure 104-Create Notification Business Process

![](bed-management-solution-version-2-4-technical-manual/106.png)

> <span id="_bookmark195" class="anchor"></span>Figure 105-Create Facility Diversion Business Process

> ![](bed-management-solution-version-2-4-technical-manual/107.png)

> <span id="_bookmark196" class="anchor"></span>Figure 106-Manage Whiteboard Business Process

![](bed-management-solution-version-2-4-technical-manual/108.png)

## Activity Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 107-Reports Business Process

> ![](bed-management-solution-version-2-4-technical-manual/109.png)

> <span id="_bookmark199" class="anchor"></span>Figure 108-BMS Overview Activity Diagram

## Functional Flow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bed-management-solution-version-2-4-technical-manual/110.png)

> <span id="_bookmark201" class="anchor"></span>Figure 109-BMS Overview Functional Flow Diagram

## Data Flow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bed-management-solution-version-2-4-technical-manual/111.png)

> <span id="_bookmark202" class="anchor"></span>Figure 110-BMS Overview Data Flow Diagram

## Application Flow Map from APPDYNAMICS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](bed-management-solution-version-2-4-technical-manual/112.png)

> <span id="_bookmark203" class="anchor"></span>Figure 111-Application Flow map from APPDYNAMICS

# Appendix B - Terms, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark205" class="anchor"></span>Table 29-Terms, Acronyms, and Abbreviations

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Terms, Acronyms, Abbreviations</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definitions</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ASP</p>
</blockquote></td>
<td><blockquote>
<p>Active Server Pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BMS</p>
</blockquote></td>
<td><blockquote>
<p>Bed Management Solution</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRUD</p>
</blockquote></td>
<td><blockquote>
<p>Create, Read, Update, Delete</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EIS</p>
</blockquote></td>
<td><blockquote>
<p>Entity Identification Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EMS</p>
</blockquote></td>
<td><blockquote>
<p>Environmental Management Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ETL</p>
</blockquote></td>
<td><blockquote>
<p>Extract Transform Load</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EVS</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Vocabulary Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IE</p>
</blockquote></td>
<td><blockquote>
<p>Internet Explorer</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IIS</p>
</blockquote></td>
<td><blockquote>
<p>Internet Information Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IRM</p>
</blockquote></td>
<td><blockquote>
<p>Information Resources Management</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MDO</p>
</blockquote></td>
<td><blockquote>
<p>Medical Domain Objects</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MDWS</p>
</blockquote></td>
<td><blockquote>
<p>Medical Domain Web Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MVC</p>
</blockquote></td>
<td><blockquote>
<p>Model-View-Controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUMI</p>
</blockquote></td>
<td><blockquote>
<p>National Utilization Management Integration</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ODBC</p>
</blockquote></th>
<th><blockquote>
<p>Open Database Connectivity</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PAP</p>
</blockquote></td>
<td><blockquote>
<p>Policy Administration Point</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PPBPL</p>
</blockquote></td>
<td><blockquote>
<p>Patients Pending Bed Placement List . A list of patients in need of beds at VA facilities</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PDP</p>
</blockquote></td>
<td><blockquote>
<p>Policy Decision Point</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RS</p>
</blockquote></td>
<td><blockquote>
<p>Reporting Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SOA</p>
</blockquote></td>
<td><blockquote>
<p>Service Oriented Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SQL</p>
</blockquote></td>
<td><blockquote>
<p>Structured Query Language</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>STS</p>
</blockquote></td>
<td><blockquote>
<p>Secure Token Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>URI</p>
</blockquote></td>
<td><blockquote>
<p>Uniform Resource Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>URL</p>
</blockquote></td>
<td><blockquote>
<p>Uniform Resource Locator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VAMC</p>
</blockquote></td>
<td><blockquote>
<p>VA Medical Center</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VIA</p>
</blockquote></td>
<td><blockquote>
<p>Vista Integration Adapter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VISN</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Integrated Service Network</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information Systems and Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WCF</p>
</blockquote></td>
<td><blockquote>
<p>Windows Communication Foundation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XAML</p>
</blockquote></td>
<td><blockquote>
<p>Extensible Application Markup Language</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XML</p>
</blockquote></td>
<td><blockquote>
<p>eXtensible Markup Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WMI</p>
</blockquote></td>
<td><blockquote>
<p>Windows Management Instrumentation</p>
</blockquote></td>
</tr>
</tbody>
</table>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Bed Management Solution Version 2.6 Technical Manual

### ### ### ### List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Create a network service account for accessing the BMS page. Make sure that it is in an Organizational Unit (OU) that will not get the Enterprise System Engineering (ESE) Federal Desktop Core Configuration (FDCC) / US Government Configuration Baseline (USGCB) User Settings. Set the "Log on to" so the account can only log onto the kiosk PC you are setting up.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Set up the Network User for BMS Access

- Create AD User with non-expiring password under Service Accounts for the local site. If you are not an AD administrator then provide the following instruction to the AD along with your request for a new service account.

#### Configure the Whiteboard Kiosk Default Login User in BMS

#### For the current facility that will display the associated Whiteboard page, a default user needs to be configured in BMS application for the Ward Whiteboard Kiosk.

To configure the Whiteboard Kiosk Default User:

- *Go to the BMS Site Home Page*
- *Click on the Site Options link*
- *Click on the Facility Setting link*
- *Fill the fields "Whiteboard Kiosk Default User Name:", "Whiteboard Kiosk Password:" and "Whiteboard Kiosk Password Confirm:" with the BMS Service Account ID*

> ![](bed-management-solution-version-2-6-technical-manual/033.png)

<span id="_Toc20913887" class="anchor"></span>Figure 32-Facility Settings

- *Click Submit*

#### Assign a Role to the Whiteboard Kiosk Default User in BMS

> Each facility must assign the BMS "EMS USER" Role to the Service Account ID created to run the Whiteboard Kiosk URL. This assignment can be done from the BMS Admin Section Add/Edit BMS User hyperlink or Facility Site Options BMS User Add/Edit hyperlink.

- *Click the Select Existing NT User Name button*
- *Select the correct VISN Domain from the left Drop Down Box.*
- *In the User Name box Enter the BMS Service Account ID created for the BMS EMS/Whiteboard Kiosk. Then click the Find button*
- *Click the Selected Radio button for the user. Then click the Select button.*
- *In the EMS User box, select "Yes". All other roles should be "No".*
- *In the Default Region box, select the correct Region.*
- *In the Default VISN box, select the correct VISN.*
- *In the Default Site box, select your Site.*
- *In the READ Access box, select "Yes".*
- *In the WRITE Access box, select "Yes".*

> ![](bed-management-solution-version-2-6-technical-manual/034.png)

<span id="_Toc20913888" class="anchor"></span>Figure 33- Whiteboard Kiosk User Role Assignment

- *Click Submit*

### After setting up the workstation / Kiosk machine, it will automatically log in to Windows, and automatically login to BMS.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### #### Disable Screen Saver

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to display the Whiteboard page continuously the screen saver needs to be disabled.

> NOTE: The Windows menu that allows the disable of the screen saver might be different from one version of Windows to another. For example, for Windows 7 the needed operations are:

- *Right click on the desktop*
- *Click Personalize*
- *Click on the screensaver button on the lower-right part of the page*

> ![](bed-management-solution-version-2-6-technical-manual/035.png)

<span id="_Toc20913889" class="anchor"></span>Figure 34- Screen Saver Option

- *Select None from the screensaver drop down on the displayed form*

> ![](bed-management-solution-version-2-6-technical-manual/036.png)

<span id="_Toc20913890" class="anchor"></span>Figure 35- Screen Saver Settings Window

- *Click OK.*

#### Configure Power Settings: Disable Sleep and Stand-by Mode

> In order to display the Whiteboard page continuously the power settings need to be adjusted so that the computer will never enter into hibernate or stand-by and also the screen will never turn off.

> NOTE: The Windows menu that allows the configuration of the power settings might be different from one version of Windows to another. For example, for Windows 7 the needed operations are:

- *Go To Control Panel*
- *Select Power Options  
  > *

> ![](bed-management-solution-version-2-6-technical-manual/037.png)

<span id="_Toc20913891" class="anchor"></span>Figure 36- Power Options

- *Click on "Change Plan settings" for the active plan*

> ![](bed-management-solution-version-2-6-technical-manual/038.png)

<span id="_Toc20913892" class="anchor"></span>Figure 37- Change Plan Settings Option

- *Select "Never" from the drop downs associated with "Turn off the display" and "Put the computer to sleep"*

> ![](bed-management-solution-version-2-6-technical-manual/039.png)

<span id="_Toc20913893" class="anchor"></span>Figure 38- Power Options Settings

- *Click "Save changes"*

#### Configure Auto-login Option and stop Microsoft Lync from opening upon start up

Configure Auto-Login: The computer that will display the Whiteboard page needs to have the auto-login configuration set to" true".

> **NOTE:** The Windows menu that allows the configuration of the auto-login settings might be different from one version of Windows to another. For example, for Windows 7 the needed operations are:

- *Press the Windows key + R on your keyboard to launch the "Run" dialog box.*

> ![](bed-management-solution-version-2-6-technical-manual/040.png)

<span id="_Toc20913894" class="anchor"></span>Figure 39- Run Window

- *Type in "control userpasswords2"*

> ![](bed-management-solution-version-2-6-technical-manual/041.png)

<span id="_Toc20913895" class="anchor"></span>Figure 40- Run Window with Comman Entered

- *Press Enter. The User Accounts window will display.*

![](bed-management-solution-version-2-6-technical-manual/042.png)

<span id="_Toc20913896" class="anchor"></span>Figure 41- User Accounts Window

- *Uncheck the option "Users must enter a user name and password to use this computer" for the BMS Default Kiosk User Account*

> ![](bed-management-solution-version-2-6-technical-manual/043.png)

<span id="_Toc20913897" class="anchor"></span>Figure 42- User Accounts

- *Click "OK"*

> Stop Microsoft Lync from opening at startup: To stop Microsoft Lync from opening at startup follow the steps below

- *From the Start Menu,*
- *Go to All Programs \>Microsoft Lync*
- *Open Microsoft Lync*
- *Go to Tools\>Options\>Personal*
- *Uncheck "automatically start Lync when I log on to Windows" & "Show Lync in foreground when it starts".*

#### Set the URL (from step 2.5.1) as the Home Page in Internet Explorer

> The specific Ward Whiteboard Kiosk URL needs to be configured as the Home-Page for the intended browser. The menu to set the default home-page might differ from one browser to another.

> For example, for Internet Explorer (IE) 9.0 the user needs to:

- *Select Tools menu  
  > *

![](bed-management-solution-version-2-6-technical-manual/044.png)

<span id="_Toc20913898" class="anchor"></span>Figure 43- Tools Menu of Internet Explorer

- *Select Internet Options*
- *On the General tab, under the homepage text field enter the URL*
- *Click OK*

> ![](bed-management-solution-version-2-6-technical-manual/045.png)

<span id="_Toc20913899" class="anchor"></span>Figure 44- General Tab of Internet Options

#### Add BMS to the "Trusted Sites"

#### To add BMS to "Trusted Sites" in Internet Explorer

- *Go to Tools\>Internet Options\>Security\>Trusted sites\>Sites*
- *In the "Add this website to the zone:" field, enter <https://redacted.va.gov>*
- *Click Add, Click OK*

#### Add the launch of the browser to the Windows start up commands.

#### > The next step is to add to the startup commands the launch of the chosen browser.

> NOTE: This operation might differ from one version of Windows to another. For example, for Windows 7 the steps needed are:

- *Click Start*
- *Select All Programs*
- *Right click on the Startup folder*
- *Select Open*

> ![](bed-management-solution-version-2-6-technical-manual/046.png)

<span id="_Toc20913900" class="anchor"></span>Figure 45- Open Option

- *Create a shortcut of the Internet Explorer and copy it to Startup folder*

![](bed-management-solution-version-2-6-technical-manual/047.png)

<span id="_Toc20913901" class="anchor"></span>Figure 46- Internet Explorer Shortcut

#### Test the Kiosk

#### > Close Internet Explorer. Restart Internet Explorer. The BMS Ward Whiteboard for the Kiosk should come up.

#### Set the Registry Keys to configure the Kiosk for local site use.

#### > The purpose of the following steps is to configure Kiosk workstation to serve one function only: BMS Ward Whiteboard display. The following instruction leads you through a series of steps that effectively lock down the workstation for this purpose. Access to workstation software and/or desktop will be prevented after the configuration setup is complete. The Whiteboard Kiosk is read only.

> \*It is recommended that prior to performing the configuration steps outlined in this section a backup of the existing system be created for rollback / recovery purposes, and that a restoration point be created.

1)  Modify Registry Settings

> Restriction.reg

<span id="_Toc20913902" class="anchor"></span>Figure 47-Windows Registry Editor

2)  Run Restrictions.reg by double-clicking filename from Windows Explorer. Verify settings have been applied.
3)  Modify Local Group Policy Settings

> For local group policy changes run gpedit.msc and make the following changes:

> User Configuration\Administrative Templates\System\Ctrl+Alt+Del Options

> Remove TaskManager Disable

> Remove Lock Computer Enable

> Remove Change Password Enable

> Remove Logoff Enable

> User Configuration\Administrative Templates\Control Panel\Display

- Password protect the screen saver Disabled

> Verify all settings have been applied. The purpose of these settings is to lock down the workstation for one purpose only, BMS Whiteboard Kiosk.

4)  Reboot Kiosk Machine to test set up.

\*Note; if Kiosk continually "freezes", please contact the Service Desk to have an IE Refresher script installed.

### There are a limited number of configuration parameters for NUMI.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Secret Key
- Number of sites per call
- Path to NUMI web service

These configurations are stored in BMS.Service.Host.exe.config

The current secret key is: \<authorization key\>

The number of site per call parameter how many sites will be bundled together in a transaction to NUMI. If this number is increased one should consider the frequency in which the calls are scheduled. Adding more sites will increase the transaction size and length.

Currently all NUMI servers operate on port 100 at the specified endpoint https://\<servername\>.aac.dva.va.gov/Inpatient.asmx*.*

> In order to integrate with NUMI certain steps should be completed:

1.  Choose VistA site
2.  Define Schedulers
3.  Select Scheduler

## 6.  

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

7.  
8.

## > Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The security service for authentication is represented by STS – security token cache that will issue a token whether the authentication succeeded, otherwise it will deny access to the application server. This STS Service will authenticate the user through WS-Security and validate application servers through WS-Trust using SAML v2.0 Token (Security Assertion Markup Language).

> Authorization

The security services for authorization are represented by a PDP and PAP implementation. PDP stands for policy decision point where the authenticated user can check the permission for a specified action on a specified resource. PAP stands for policy administration point. Here an administrative console can define actions, resource-types, roles and make associations with them (define security policies) that will server for PDP. The PDP service exposes one method: CheckAccess, whilst PAP service has specific functions for policy administration.

Detailed functional model on each interface

> STS – Security Token Service

- Authenticate

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Business friendly name</strong></p>
</blockquote></td>
<td><blockquote>
<p>User authentication</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
<td><blockquote>
<p>The function decides if the user and the password supplied as parameters are valid. Will return true on success and false on any failure.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Inputs</strong></p>
</blockquote></td>
<td><blockquote>
<p>Windows client credentials or</p>
<p>Username – representing the username of the requested user.</p>
<p>Password – the password of the requested user.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Outputs</strong></p>
</blockquote></td>
<td><blockquote>
<p>True - on success</p>
<p>False – on failure</p>
</blockquote></td>
</tr>
</tbody>
</table>

> PDP – Policy Decision Point

- CheckPermission

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Business friendly name</strong></p>
</blockquote></td>
<td><blockquote>
<p>User authorization – check Access</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Signature</strong></p>
</blockquote></td>
<td><blockquote>
<p><em>Message</em> CheckAccess (<em>Message</em> request);</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
<td><blockquote>
<p>The function decides if the user has the privilege to access the specified action(s) on the specified resource.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Inputs</strong></p>
</blockquote></td>
<td><blockquote>
<p>Username, operation name and resource id are encapsulated in the SAML Message class</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Outputs</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Message containing the permit or deny result.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> PAP – Policy Administration Point

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
<td><strong>Input</strong></td>
<td><strong>Output</strong></td>
</tr>
<tr class="even">
<td><em><strong>AddRole</strong></em></td>
<td>Adds a role</td>
<td><em>String name</em> – name of the new role<br />
<em>String</em> description – role description</td>
<td><em>String</em> – new role's id</td>
</tr>
<tr class="odd">
<td><p><em><strong>Delete</strong></em></p>
<p><em><strong>Role</strong></em></p></td>
<td>Delete a role</td>
<td><em>String id</em> – role's id</td>
<td><em>String</em> – deleted role's id</td>
</tr>
<tr class="even">
<td><p><em><strong>Update</strong></em></p>
<p><em><strong>Role</strong></em></p></td>
<td>Update a role</td>
<td><em>String</em> id – role's id<br />
<em>String</em> name – role's name<br />
<em>String</em> description –role's description</td>
<td><em>bool</em> – operation result: <em>true</em> on succeeded; <em>false</em> if any error aroused</td>
</tr>
<tr class="odd">
<td><p><em><strong>Update</strong></em></p>
<p><em><strong>Task</strong></em></p></td>
<td>Update a task</td>
<td><em>String</em> id – task's id<br />
<em>String</em> name –task's name<br />
<em>String</em> description – task's description</td>
<td><em>bool</em> – operation result: <em>true</em> on succeeded; <em>false</em> if any error aroused</td>
</tr>
<tr class="even">
<td><p><em><strong>Update</strong></em></p>
<p><em><strong>Operation</strong></em></p></td>
<td>Update an operation</td>
<td><em>String</em> id – operation's id<br />
<em>String</em> name – operation's name<br />
<em>String</em> description – operation's description</td>
<td><em>bool</em> – operation result: <em>true</em> on succeeded; <em>false</em> if any error aroused</td>
</tr>
<tr class="odd">
<td><em><strong>IsChild</strong></em></td>
<td>Verifies if the sent operation is part of a task</td>
<td><em>String</em> id – operation id</td>
<td><em>bool</em> – operation result</td>
</tr>
<tr class="even">
<td><p><em><strong>Assign</strong></em></p>
<p><em><strong>User</strong></em></p></td>
<td>Assign an user to a role</td>
<td><em>String</em> userId – user's id (SID)<br />
<em>String</em> roleId – role's id</td>
<td><em>-</em></td>
</tr>
<tr class="odd">
<td><em><strong>DeassignUser</strong></em></td>
<td>Delete an association between an user and a role</td>
<td><em>String</em> userId – user's id (SID)<br />
<em>String</em> roleId – role's id</td>
<td><em>-</em></td>
</tr>
<tr class="even">
<td><p><em><strong>Grant</strong></em></p>
<p><em><strong>Permission</strong></em></p></td>
<td>Grant access to a resource for a role on an action</td>
<td><em>string</em> resourceId, <em>string</em> actionId, <em>string</em> roleId</td>
<td><em>-</em></td>
</tr>
<tr class="odd">
<td><p><em><strong>Revoke</strong></em></p>
<p><em><strong>Permission</strong></em></p></td>
<td>Revokes a permission</td>
<td><em>string</em> resourceId, <em>string</em> actionId, <em>string</em> roleId</td>
<td><em>-</em></td>
</tr>
<tr class="even">
<td><em><strong>GetRoles</strong></em></td>
<td>Returns a list with all stored roles</td>
<td><em>Bool</em> assignedOnly - returns assigned roles if parameter is true</td>
<td><em>List&lt;Role&gt;</em> - retrieved roles</td>
</tr>
<tr class="odd">
<td><p><em><strong>Get</strong></em></p>
<p><em><strong>Operations</strong></em></p></td>
<td>Returns a list with all stored operations</td>
<td>-</td>
<td><em>List&lt;Operation&gt;</em> - retrieved operations</td>
</tr>
<tr class="even">
<td><em><strong>GetTasks</strong></em></td>
<td>Returns a list with all stored tasks</td>
<td>-</td>
<td><em>List&lt;Task&gt;</em> - retrieved tasks</td>
</tr>
<tr class="odd">
<td><p><em><strong>Add</strong></em></p>
<p><em><strong>Operation</strong></em></p></td>
<td>Add a new operation</td>
<td><em>String</em> name – operation's name<br />
<em>String</em> description – operation's description</td>
<td><em>String</em> id <em>– operation's id</em></td>
</tr>
<tr class="even">
<td><p><em><strong>Delete</strong></em></p>
<p><em><strong>Operation</strong></em></p></td>
<td>Delete an operation</td>
<td><em>String – operation's id</em></td>
<td><em>-</em></td>
</tr>
<tr class="odd">
<td><em><strong>AddTask</strong></em></td>
<td>Add a new task</td>
<td><em>String</em> name – task's name<br />
<em>String</em> description – task's description</td>
<td><em>String</em> id<em>– tasks's id</em></td>
</tr>
<tr class="even">
<td><p><em><strong>Delete</strong></em></p>
<p><em><strong>Task</strong></em></p></td>
<td>Delete a task</td>
<td><em>String</em> id<em>– tasks's id</em></td>
<td><em>-</em></td>
</tr>
<tr class="odd">
<td><p><em><strong>Assign</strong></em></p>
<p><em><strong>Operations</strong></em></p></td>
<td>Associate operations to a task</td>
<td><em>List&lt;String&gt;</em> operationIds – list of operations to be assigned<br />
<em>String</em> taskId – task's id</td>
<td><em>-</em></td>
</tr>
<tr class="even">
<td><em><strong>DeassignOperations</strong></em></td>
<td>Deassign operations from a task</td>
<td><em>List&lt;String&gt;</em> operationIds – list of operations to be assigned<br />
<em>String</em> taskId – task's id</td>
<td><em>-</em></td>
</tr>
<tr class="odd">
<td><em><strong>GetTaskDefinition</strong></em></td>
<td>Retrieve a list with all operations of the specified task</td>
<td><em>String</em> id<em>– tasks's id</em></td>
<td><em>List&lt;DefinitionBase&gt; -</em> operation list</td>
</tr>
<tr class="even">
<td><p><em><strong>GetRole</strong></em></p>
<p><em><strong>Definition</strong></em></p></td>
<td>Returns all associated operations to a specified role</td>
<td><em>String</em> roleId – role's id</td>
<td><em>List&lt;DefinitionBase&gt; -</em> operation list</td>
</tr>
<tr class="odd">
<td><p><em><strong>GetRole</strong></em></p>
<p><em><strong>ByName</strong></em></p></td>
<td>Returns a role by name</td>
<td><em>String</em> name – role's name</td>
<td><em>Role</em> – returned role</td>
</tr>
<tr class="even">
<td><p><em><strong>GetRole</strong></em></p>
<p><em><strong>ByName</strong></em></p>
<p><em><strong>Excluding</strong></em></p></td>
<td>Returns a role by name excluding the role id sent by parameter</td>
<td><em>String</em> name – role's name<br />
<em>Guid</em> id – role's id</td>
<td><em>Role</em> – returned role</td>
</tr>
<tr class="odd">
<td><p><em><strong>GetTask</strong></em></p>
<p><em><strong>ByName</strong></em></p></td>
<td>Returns a task by name</td>
<td><em>String</em> name – task's name</td>
<td><em>Task</em> – returned task</td>
</tr>
<tr class="even">
<td><p><em><strong>GetTask</strong></em></p>
<p><em><strong>ByName</strong></em></p>
<p><em><strong>ExcludingId</strong></em></p></td>
<td>Returns a task by name excluding the task id sent by parameter</td>
<td><em>String</em> name – task's name<br />
<em>Guid</em> id – task's id</td>
<td><em>Task</em> – returned task</td>
</tr>
<tr class="odd">
<td><p><em><strong>Get</strong></em></p>
<p><em><strong>Operation</strong></em></p>
<p><em><strong>ByName</strong></em></p></td>
<td>Returns an operation by name</td>
<td><em>String</em> name <em>–</em> operation's name</td>
<td><em>Operation</em> – returned operation</td>
</tr>
<tr class="even">
<td><p><em><strong>Get</strong></em></p>
<p><em><strong>Operation</strong></em></p>
<p><em><strong>ByName</strong></em></p>
<p><em><strong>ExcludingId</strong></em></p></td>
<td>Returns an operation by name excluding the operation id sent by parameter</td>
<td><em>String</em> name – operation's name<br />
<em>Guid</em> id – operation's id</td>
<td><em>Operation</em> – returned operation</td>
</tr>
<tr class="odd">
<td><p><em><strong>Get</strong></em></p>
<p><em><strong>Permissions</strong></em></p>
<p><em><strong>By</strong></em></p>
<p><em><strong>Resource</strong></em></p>
<p><em><strong>Type</strong></em></p></td>
<td>Returns a list with operations/task associated with a resource ype</td>
<td><em>String</em> resourceType – Resource type</td>
<td><em>List&lt;DefinitionBase&gt;</em> – operation/task list</td>
</tr>
<tr class="even">
<td><em><strong>GetPolicy</strong></em></td>
<td>Returns a list with all roles and operations associated with the resource</td>
<td><em>String</em> resourceId – resource's id</td>
<td><em>List&lt;Role&gt;</em> – role list. Each role has the associated operations.</td>
</tr>
<tr class="odd">
<td><p><em><strong>GetRole</strong></em></p>
<p><em><strong>Users</strong></em></p></td>
<td>Returns a list with all users associated to a specific role</td>
<td><em>Guid</em> roleId <em>–</em> role's id</td>
<td><em>List&lt;User&gt;</em> – user list</td>
</tr>
<tr class="even">
<td><p><em><strong>Assign</strong></em></p>
<p><em><strong>Role</strong></em></p></td>
<td>Marks a role as assigned</td>
<td><em>Guid</em> roleId <em>–</em> role's id</td>
<td><em>-</em></td>
</tr>
<tr class="odd">
<td><p><em><strong>Deassign</strong></em></p>
<p><em><strong>Role</strong></em></p></td>
<td>Marks a role as unassigned</td>
<td><em>Guid</em> roleId <em>–</em> role's id</td>
<td><em>-</em></td>
</tr>
<tr class="even">
<td><p><em><strong>Get</strong></em></p>
<p><em><strong>Connected</strong></em></p>
<p><em><strong>RolesAndOperations</strong></em></p></td>
<td>Returns a list with all roles and operations associated with the resource</td>
<td><em>String</em> resourceId – resource's id</td>
<td><em>List&lt;Role_Operation&gt;</em> – list with role-operations associations</td>
</tr>
<tr class="odd">
<td><p><em><strong>Clear</strong></em></p>
<p><em><strong>Permissions</strong></em></p>
<p><em><strong>For</strong></em></p>
<p><em><strong>Resource</strong></em></p></td>
<td>Removes all permissions for a certain resource (all associations to this resource)</td>
<td><em>String</em> resourceId – resource's id</td>
<td><em>-</em></td>
</tr>
<tr class="even">
<td><p><em><strong>Delete</strong></em></p>
<p><em><strong>PermissionFor</strong></em></p>
<p><em><strong>Resource</strong></em></p>
<p><em><strong>And</strong></em></p>
<p><em><strong>Operation</strong></em></p></td>
<td>Deletes a permission form a role based on the resource and operation sent.</td>
<td><em>String</em> resourceId – resource's id<br />
<em>String</em> roleId <em>–</em> role's id<br />
<em>String</em> actionGUID – operation's id</td>
<td><em>-</em></td>
</tr>
<tr class="odd">
<td><p><em><strong>Insert</strong></em></p>
<p><em><strong>PermissionFor</strong></em></p>
<p><em><strong>Resource</strong></em></p>
<p><em><strong>And</strong></em></p>
<p><em><strong>Operation</strong></em></p></td>
<td>Creates a permission for a certain role and an operation on a resource. It automatically creates the association within the permission and the operation if it doesn't exist.</td>
<td><em>String</em> resourceId – resource's id<br />
<em>String</em> roleId <em>–</em> role's id<br />
<em>String</em> actionGUID – operation's id</td>
<td><em>-</em></td>
</tr>
</tbody>
</table>

The security services do not expose a fault contract as usual web services do. Instead, these services deliver information about any issue in processing the request in the return message of the service call (such as authentication error, authorization error etc.).

### From: Bed Management Solution Version 2.8 Technical Manual

## Authorization and Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Policy Manager has been removed as part of the Inflow-AUTHZ replacement. To perform modifications to Actions, Permissions, Roles, or Users, the BMS database tables, below will be used.

<span id="_Toc71031306" class="anchor"></span>Figure - New Tables added to BMS database for Policy Manager Replacement

![](bed-management-solution-version-2-8-technical-manual/077.png)

## BMS AuthAction Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The previously known "Operation Definitions" from using the policy manager have now been mapped to the new AuthAction table. Figure 77 displays the table example. The previous AuthActionUid has now been augmented with an integer primary key, AuthActionID. The AuthActionUid has been retained for backward compatibility, but will likely be phased out by the end of the Inflow project. The original "operation definitions" names have been maintained in the AuthActionName and AuthActionDescription fields, as well as the IsGroup and \_ssis_timestamp.

<span id="_Toc71031307" class="anchor"></span>Figure -AuthAction Table

![](bed-management-solution-version-2-8-technical-manual/078.png)

## BMS AuthPermissions Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AuthPermission table handles the permission mappings between the facility, user, and Permission type. (read or write) utilizing the unique key AuthPermissionsId, AuthUserId, PermissionName, and FacilityId. LastModifiedDate and LastModifiedBy is kept for auditing purposes.

<span id="_Toc71031308" class="anchor"></span>Figure -AuthPermissions Table

![](bed-management-solution-version-2-8-technical-manual/079.png)

## BMS AuthRoles Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AuthRoles table handles the Role definitions to be associated to Actions and Users. As noted in AuthAction, we've maintained the AuthRoleUid for backward compatibility, but added an integer primary key to quickly associate/join tables. The AuthRoleName, AuthRoleDescription column, AuthRoleAssigned, and \_ssis_timestamp were maintained from the previous BMS_AUTHZ database.

<span id="_Toc72939422" class="anchor"></span>Figure -AuthRolesTable

![](bed-management-solution-version-2-8-technical-manual/080.png)

## BMS AuthRoleActions Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AuthRoleActions table associates the AuthActionId from the AuthActions table and the AuthRoleId from the AuthRoles table for purposes of tying the Roles and Actions together.

<span id="_Toc71031309" class="anchor"></span>Figure -AuthRoleActions Table

![](bed-management-solution-version-2-8-technical-manual/081.png)

## BMS AuthUser Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AuthUser table maintains BMS user information, with a new integer primary key, AuthUsername (hidden for security purposes), the previously tracked AuthUserSID and LegacyUserPK (kept for backwards compatibility), IsSuperUser, and \_ssis_timestamp.

<span id="_Toc71031310" class="anchor"></span>Figure -AuthUser Table

![](bed-management-solution-version-2-8-technical-manual/082.png)

## BMS AuthUserRoles Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AuthUserRoles table associates the User and the Role they are mapped to, using The AuthUserID and the AuthRoleID. The AuthUserRoles use the integer primary key column named AuthUserRolesId and also maintains the \_ssis_timestamp.

<span id="_Toc71031311" class="anchor"></span>Figure -AuthUserRoles table

![](bed-management-solution-version-2-8-technical-manual/083.png)

## BMS AuthActions Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The entire listing of AuthActions (previously known as Task Definitions) is presented below:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Admin, AddEditUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add/Edit BMS User' hyperlink from the Administration section's menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, FacilityEdit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit BMS Site' hyperlink from the Administration section's menu.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'BMS Admin' hyperlink from the National And Regional Page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Admin, SelectUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Select Existing NT User Name' button from the ADMINISTRATION SECTION - USERADD/EDIT page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, SisterSiteAddEdit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit Sister Sites' hyperlink from the Administration section's menu.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, AddUserOperations Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add User' button from the ADMINISTRATION SECTION</p>
<p>- FACILITY EDIT page (Edit BMS Site submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, RemoveUsers Read</p>
</blockquote></td>
<td><blockquote>
<p>'Remove Selected' button from the ADMINISTRATION SECTION - FACILITY EDIT page (Edit BMS Site</p>
<p>submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, SearchUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Find' button from the 'Select user' page ('Select Existing NT User Name' button from the Administration Section</p>
<p>menu, 'Add/Edit BMS User' submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, SearchUsers Read</p>
</blockquote></td>
<td><blockquote>
<p>'Find' button from the ADMINISTRATION SECTION - FACILITY EDIT page (Edit BMS Site submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, ClearCache Read</p>
</blockquote></td>
<td><blockquote>
<p>'Clear Cache' link from the Administration section's menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, AddEditUser Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the ADMINISTRATION SECTION - USERADD/EDIT page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, FacilityEdit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from Administration section's menu 'Edit BMS Site' hyperlink (page ADMINISTRATION SECTION</p>
<p>- FACILITY EDIT).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, SisterSiteAddEdit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Edit Sister Sites' hyperlink from the Administration section's menu, 'Submit' button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Admin, AddUserOperations Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from Add users page (Add User button from the Facility page).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Admin, RemoveUserOperations Update</p>
</blockquote></td>
<td><blockquote>
<p>'Remove Selected' button from the ADMINISTRATION SECTION - FACILITY EDIT page (Edit BMS Site</p>
<p>submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminComments, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' hyperlink from the Common Medical Terms page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminComments, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' hyperlink from the Common Medical Terms page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminComments, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Common Medical Terms' hyperlink from the Administration section's menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminComments, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from the Common Medical Terms page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Icon' button on ADMINISTRATION SECTION - EDIT ICON page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' Link on ADMINISTRATION SECTION - ICON</p>
<p>ADD/EDIT page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add/Edit Icon' link on ADMINISTRATION SECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, Search Read</p>
</blockquote></td>
<td><blockquote>
<p>'Search' Link on ADMINISTRATION SECTION - ICON</p>
<p>ADD/EDIT page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, ViewIconReport Read</p>
</blockquote></td>
<td><blockquote>
<p>''Report' Link on ADMINISTRATION SECTION - ICON</p>
<p>ADD/EDIT page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Remove' button on ADMINISTRATION SECTION - DELETE ICON page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminIcon, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on ADMINISTRATION SECTION - EDIT</p>
<p>ICON page (Add/Edit Icon Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminIcon, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Up/Down arrow' buttons on ADMINISTRATION SECTION - ICON ADD/EDIT page (Add/Edit Icon</p>
<p>Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminSpecialtyAssociation, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' Link on ADMINISTRATION SECTION - Treating Specialty/NUMA/HAvBED Edit page (Treating</p>
<p>Specialty/NUMA/HAvBED Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminSpecialtyAssociation, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Treating Specialty/NUMA/HAvBED' Link on ADMINISTRATION SECTION</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AdminSpecialtyAssociation, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' Button on ADMINISTRATION SECTION - Treating Specialty/NUMA/HAvBED Delete page</p>
<p>(Treating Specialty/NUMA/HAvBED Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminSpecialtyAssociation, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' Button on ADMINISTRATION SECTION - Treating Specialty/NUMA/HAvBED Edit page (Treating<br />
Specialty/NUMA/HAvBED Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminUnavailableReason, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link on ADMINISTRATION SECTION - National Unavailable Reason page (National Unavailable Reason<br />
Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminUnavailableReason, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link on ADMINISTRATION SECTION - National Unavailable Reason page (National Unavailable Reason<br />
Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminUnavailableReason, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'National Unavailable Reason' Link on ADMINISTRATION SECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminUnavailableReason, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button on ADMINISTRATION SECTION</p>
<p>- National Unavailable Reason Delete page (National Unavailable Reason Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminUnavailableReason, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button on ADMINISTRATION SECTION - National Unavailable Reason Edit page (National Unavailable Reason Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminUnavailableReason, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button on ADMINISTRATION SECTION - National Unavailable Reason page (National Unavailable Reason Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWaitingArea, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link on ADMINISTRATION SECTION - National Waiting Areas Parameter page (National Waiting Area Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWaitingArea, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link on ADMINISTRATION SECTION - National Waiting Areas Parameter page (National Waiting Area Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWaitingArea, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'National Waiting Area' Link on ADMINISTRATION SECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWaitingArea, DeleteAction Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button on ADMINISTRATION SECTION</p>
<p>- National Waiting Area Parameter Delete page (National Waiting Area Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWaitingArea, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button on ADMINISTRATION SECTION - National Waiting Area Parameter Edit page (National Waiting Area Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWaitingArea, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button on ADMINISTRATION SECTION - National Waiting Area Parameter page (National Waiting Area</p>
<p>Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWhiteboardReport, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link on ADMINISTRATION SECTION - Whiteboard Report page (Background Processor</p>
<p>Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWhiteboardReport, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link on ADMINISTRATION SECTION - Whiteboard Report page (Background Processor Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWhiteboardReport, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Whiteboard Report' tab on ADMINISTRATION SECTION - Background Processor page</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdminWhiteboardReport, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button on ADMINISTRATION SECTION</p>
<p>- Whiteboard Report Delete page (Background Processor Submenu)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdminWhiteboardReport, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on ADMINISTRATION SECTION - Whiteboard Report Edit page (Background Processor Submenu)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdtOrderableItems, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, ADT Orderable Items Add/Delete hyperlink</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AdtOrderableItems, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' hyperlink from the list of orderable items.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AdtOrderableItems, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Bed Board ADT Orderable Items Configuration.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>BackgroundProcessors, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Backgroung Processors' hyperlink from Site Options page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BackgroundProcessors, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save Scheduler' button from Background Processors page within Site Options.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AuditLogReport, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'View audit log' link on ADMINISTRATION SECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Audit Log Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Audit Log Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedBoard, ChangeFacility Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a facility link from the VISN Network Bed Boards list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedBoard, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Return to VISN Network' hyperlink from the home page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedBoard, ShowFacilityBedSummaryReport Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a Facility Summary Report on VISN Network Bed Boards list</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedBoard, ShowVISNBedSummaryReport Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a VISN Summary Report on VISN Network Bed Boards list</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedBoardModule, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Bed Board Module Enable/Disable link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedBoardModule, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Bed Board Module Activation and Configuration page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedInformation, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Ward Occupancy, click on a hyperlink from the BED column.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedInformation, ClearAll Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on button 'Clear ALL Comments For ALL Wards Associate To This Bed…'.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BedInformation, NotifyChange Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Add/Edit Bed Unavailable Reason page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BedInformation, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on buttons 'Submit' and/or 'Update Reason and Comments'.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ContingencySettings, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Contingency Settings" link on Site Settings pages.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ContingencySettings, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on Contingency Settings page on Site Settings pages.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DischargeClinic, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'Discharge Appt Clinics Add/Delete' hyperlink.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DischargeClinic, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'Discharge Appt Clinics Add/Delete' hyperlink, 'Delete' button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DischargeClinic, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'Discharge Appt Clinics Add/Delete' hyperlink, 'Add' button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin, EMS Supervisor Read/Update</p>
</blockquote></td>
<td><blockquote>
<p>'Assigned To' drop down on EMS Bed Edit page</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsBedStatusAdmin, EMSBatchAssign Read</p>
</blockquote></td>
<td><blockquote>
<p>'Batch Assign' button on Ems Bed Status Admin page</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin, EMSBatchAssign Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button on EMS Bed Edit page on EMS Bed Status Admin page</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsBedStatusAdmin, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>RoomBed column link click.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Return to VISN Network' link from the home page, 'Return to Regional Page' link, 'Go To Facility Bed</p>
<p>Cleaning Page (EMS Staff Only) button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsBedStatusAdmin, SaveConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button click in the Environmental Management Service Bed Status page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsBedStatusAdmin, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button click in the Environmental Management Service Bed Status page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EMSMobile, EMSList Read</p>
</blockquote></td>
<td><blockquote>
<p>Load Bed Clean Requests on EMS Mobile Pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMSMobile, Users Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a User button on EMS Mobile Pages</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EMSMobile, EMSList Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on a Bed Clean Request button on EMS Mobile Pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMSMobile, Users Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on Submit button after entering a PIN on EMS Mobile Pages</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EmsNotification, AddEdit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Current Locations table (EMS Bed Notification).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsNotification, AddEditAction Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the EMS Bed Notification Edit page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsNotification, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Current Locations table (EMS Bed Notification).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsNotification, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'EMS Notification Add/Edit' link</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsNotification, DeleteAction Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button from the EMS Bed Status Notification Delete page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsNotification, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the EMS Bed Notification Edit page or Notifications Add page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsStaff, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link on EMS Staff page on Site Options pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsStaff, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link on EMS Staff page on Site Options pages</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsStaff, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>EMS Staff link on Site Options page</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EmsStaff, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button on Ems Staff Delete page on Site Options pages</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EmsStaff, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button on Ems Staff Edit page on Site Options pages</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EventNotification, AddConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Event Notification Add page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EventNotification, AddEdit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button or 'Edit' link from the Event Notifications page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EventNotification, EditConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Event Notifications Edit page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EventNotification, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, 'Event Notification Add/Edit' hyperlink.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EventNotification, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Event Notification Add page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Exception, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Appears when an exception occurs.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, Add Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Facility Diversion page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilityDiversion, AddConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Add New Diversion Status page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Facility Diversion page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilityDiversion, EditConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from the Diversion Status edit page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, FilterDiversions Read</p>
</blockquote></td>
<td><blockquote>
<p>'Current Diversions' or 'All Diversions' button from the main Facility Diversions page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilityDiversion, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Facility Diversion' hyperlink from the home page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilityDiversion, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button or 'Edit' link from the Facility Diversion page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FacilitySettings, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Facility Settings link</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FacilitySettings, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Facility Settings link, Submit button</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home, Index2 Read</p>
</blockquote></td>
<td><blockquote>
<p>Current, Past 30-Days, Past 60-Days, Past 90-Days home page's buttons.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, PatientInquiry Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on the patient link from the Patients Pending Placement list (Home page).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home, RemoveAdmission Read</p>
</blockquote></td>
<td><blockquote>
<p>Remove link from the Patients Pending Placement list (Home page).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Home, UndoRemoveAdmission Read</p>
</blockquote></td>
<td><blockquote>
<p>Undo link from the Patients Pending Placement list (Home page).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Home, RemoveAdmissionPost Update</p>
</blockquote></td>
<td><blockquote>
<p>Remove link from the Patients Pending Placement list (Home page), Remove button from the confirmation</p>
<p>page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Home, UndoRemoveAdmissionPost Update</p>
</blockquote></td>
<td><blockquote>
<p>'Undo' button on Undo Remove Admission Page on Facility HomePage</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IconLegend, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Icon Legend' link from the bottom of the Home page or Site Options, BMS Icon Legend link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IconLibrary, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' Link on Site Options - Site Configurable Icons page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IconLibrary, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Site Configurable Icons link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IconLibrary, ResetConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>'Reset' button on Edit Site Configurable Icon page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IconLibrary, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on Site Options - Site Configurable Icons page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IconLibrary, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Up/Down arrow' buttons on Site Options - Site Configurable Icons page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IconLibrary, ResetConfirmation Update</p>
</blockquote></td>
<td><blockquote>
<p>'Reset' button on Reset Site Configurable Icon page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Information, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Information' link from the bottom of the Home page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MaintainMarquee, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Maintain Marquee Text' link from the Administration Section's menu.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MaintainMarquee, ChangeMarquee Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the ADMINISTRATION SECTION - MAINTAIN MARQUEE TEXT page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NationalAndRegional, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, Return to VISN Network link, Return to Regional Page link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NewEvents, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, New Events link.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Numi, Add Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Numi, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' Link on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Numi, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' Link on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Numi, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Numi' tab on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Numi, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete Record' button on ADMINISTRATION SECTION</p>
<p>- Background Processors Delete page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Numi, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button on ADMINISTRATION SECTION - Background Processors Add/Edit page (Background<br />
Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetDomain">http://tempuri.org/IAdministrativeFunctions/GetDomain</a> s</p>
</blockquote></td>
<td rowspan="6"><blockquote>
<p>Functions used in the Administration Section, Add/Edit BMS User and Edit BMS Site submenus.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetCurrent">http://tempuri.org/IAdministrativeFunctions/GetCurrent</a> Domain</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoles">http://tempuri.org/IAdministrativeFunctions/GetRoles</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetBulkPoli">http://tempuri.org/IAdministrativeFunctions/GetBulkPoli</a> cies</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GrantPermi">http://tempuri.org/IAdministrativeFunctions/GrantPermi</a> ssion</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/RevokePer">http://tempuri.org/IAdministrativeFunctions/RevokePer</a> mission</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleBy">http://tempuri.org/IAdministrativeFunctions/GetRoleBy</a> Name</p>
</blockquote></td>
<td rowspan="30"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetPermiss">http://tempuri.org/IAdministrativeFunctions/GetPermiss</a> ionsByResourceType</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetAllUser">http://tempuri.org/IAdministrativeFunctions/GetAllUser</a> sAndDomain</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetAllUser">http://tempuri.org/IAdministrativeFunctions/GetAllUser</a> Roles</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AssignUser">http://tempuri.org/IAdministrativeFunctions/AssignUser</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeassignU">http://tempuri.org/IAdministrativeFunctions/DeassignU</a> ser</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetPolicy">http://tempuri.org/IAdministrativeFunctions/GetPolicy</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/ClearPermi">http://tempuri.org/IAdministrativeFunctions/ClearPermi</a> ssionsForResource</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddActionE">http://tempuri.org/IAdministrativeFunctions/AddActionE</a> ntityType</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddOperati">http://tempuri.org/IAdministrativeFunctions/AddOperati</a> on</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddRole">http://tempuri.org/IAdministrativeFunctions/AddRole</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AddTask">http://tempuri.org/IAdministrativeFunctions/AddTask</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AssignOper">http://tempuri.org/IAdministrativeFunctions/AssignOper</a> ations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/AssignRole">http://tempuri.org/IAdministrativeFunctions/AssignRole</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/ChangeUse">http://tempuri.org/IAdministrativeFunctions/ChangeUse</a> rPassword</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeassignO">http://tempuri.org/IAdministrativeFunctions/DeassignO</a> perations</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeassignR">http://tempuri.org/IAdministrativeFunctions/DeassignR</a> ole</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteActio">http://tempuri.org/IAdministrativeFunctions/DeleteActio</a> nEntityType</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteOper">http://tempuri.org/IAdministrativeFunctions/DeleteOper</a> ation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeletePerm">http://tempuri.org/IAdministrativeFunctions/DeletePerm</a> issionForResourceAndOperation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeletePerm">http://tempuri.org/IAdministrativeFunctions/DeletePerm</a> issionsForResourcesAndOperations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteRole">http://tempuri.org/IAdministrativeFunctions/DeleteRole</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/DeleteTask">http://tempuri.org/IAdministrativeFunctions/DeleteTask</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetActionE">http://tempuri.org/IAdministrativeFunctions/GetActionE</a> ntityTypes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetAvailabl">http://tempuri.org/IAdministrativeFunctions/GetAvailabl</a> eDomains</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetCallerIs">http://tempuri.org/IAdministrativeFunctions/GetCallerIs</a> SuperUser</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetConnec">http://tempuri.org/IAdministrativeFunctions/GetConnec</a> tedRolesAndOperations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetEntityTy">http://tempuri.org/IAdministrativeFunctions/GetEntityTy</a> pes</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetOperati">http://tempuri.org/IAdministrativeFunctions/GetOperati</a> onByName</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetOperati">http://tempuri.org/IAdministrativeFunctions/GetOperati</a> onByNameExcludingId</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetOperati">http://tempuri.org/IAdministrativeFunctions/GetOperati</a> ons</p>
</blockquote></td>
<td rowspan="26"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleBy">http://tempuri.org/IAdministrativeFunctions/GetRoleBy</a> NameExcludingId</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleDef">http://tempuri.org/IAdministrativeFunctions/GetRoleDef</a> inition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRolesD">http://tempuri.org/IAdministrativeFunctions/GetRolesD</a> efinitionIntersect</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetRoleUs">http://tempuri.org/IAdministrativeFunctions/GetRoleUs</a> ers</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetSubscri">http://tempuri.org/IAdministrativeFunctions/GetSubscri</a> ptions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTaskBy">http://tempuri.org/IAdministrativeFunctions/GetTaskBy</a> Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTaskBy">http://tempuri.org/IAdministrativeFunctions/GetTaskBy</a> NameExcludingId</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTaskDe">http://tempuri.org/IAdministrativeFunctions/GetTaskDe</a> finition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetTasks">http://tempuri.org/IAdministrativeFunctions/GetTasks</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserBy">http://tempuri.org/IAdministrativeFunctions/GetUserBy</a> Sid</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserBy">http://tempuri.org/IAdministrativeFunctions/GetUserBy</a> UserName</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserDef">http://tempuri.org/IAdministrativeFunctions/GetUserDef</a> inedRoles</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserGr">http://tempuri.org/IAdministrativeFunctions/GetUserGr</a> oupId</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/GetUserRol">http://tempuri.org/IAdministrativeFunctions/GetUserRol</a> es</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/InsertPermi">http://tempuri.org/IAdministrativeFunctions/InsertPermi</a> ssionForResourceAndOperation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/InsertPermi">http://tempuri.org/IAdministrativeFunctions/InsertPermi</a> ssionsForResourcesAndOperations</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/InsertReso">http://tempuri.org/IAdministrativeFunctions/InsertReso</a> urce</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/IsChild">http://tempuri.org/IAdministrativeFunctions/IsChild</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/RefreshCac">http://tempuri.org/IAdministrativeFunctions/RefreshCac</a> he</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/SearchUser">http://tempuri.org/IAdministrativeFunctions/SearchUser</a>s</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/SetCurrent">http://tempuri.org/IAdministrativeFunctions/SetCurrent</a> Domain</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/Syncronize">http://tempuri.org/IAdministrativeFunctions/Syncronize</a> AllSubscribers</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/UpdateOpe">http://tempuri.org/IAdministrativeFunctions/UpdateOpe</a> ration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/UpdateRole">http://tempuri.org/IAdministrativeFunctions/UpdateRole</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="http://tempuri.org/IAdministrativeFunctions/UpdateTas">http://tempuri.org/IAdministrativeFunctions/UpdateTas</a>k</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient, Admission Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Home page, Patients Pending Placement list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient, Select Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add New Patient' link from the Home page, Patients Pending Placement section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient, Admission Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from ADD/EDIT Patients Pending Placement page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>rep, Active Admission Orders Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Active Admission Orders Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Active Discharge Orders Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Active Discharge Orders Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Active Transfer Orders Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Active Transfer Orders Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Antic Discharge Orders Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Antic Discharge Orders Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Audit Log Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Audit Log Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, BED AVAILABILITY STATUS REPORTQu</p>
</blockquote></td>
<td><blockquote>
<p>Access the BED AVAILABILITY STATUS REPORT.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Bed Specialty Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Bed Specialty Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Bed Specialty Roster</p>
</blockquote></td>
<td><blockquote>
<p>Access the Bed Specialty Roster.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Bed Summary Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Bed Summary Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Bed Turnaround Time Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Bed Turnaround Time Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Beds Out of Service Report (All)</p>
</blockquote></td>
<td><blockquote>
<p>Access the Beds Out of Service Report (All).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Beds Out of Service Report (By Date)</p>
</blockquote></td>
<td><blockquote>
<p>Access the Beds Out of Service Report (By Date).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Discharge Order Difference Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Discharge Order Difference Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Discharges In Progress</p>
</blockquote></td>
<td><blockquote>
<p>Access the Discharges In Progress.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Emergency Management Report</p>
</blockquote></td>
<td><blockquote>
<p>Access Emergency Management Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, EMS Bed Status Report (Admin)</p>
</blockquote></td>
<td><blockquote>
<p>Access the EMS Bed Status Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Facility Diversion Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Facility Diversion Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Icon Usage Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Icon Usage Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Patient Inquiry</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patient Inquiry report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Patient Movement Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patient Movement Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Patient Movements by Date</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patient Movements by Date.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Patients w Discharge Appointments</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patients w Discharge Appointments.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Rep, PPBP by Date Range Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the PPBP By Date Range Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Scheduled Admissions by Date</p>
</blockquote></td>
<td><blockquote>
<p>Access the Scheduled Admissions by Date.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, Scheduled Admissions Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Scheduled Admissions Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, UserAccess</p>
</blockquote></td>
<td><blockquote>
<p>Access the UserAccess Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, VISN Bed Summary Report</p>
</blockquote></td>
<td><blockquote>
<p>Access VISN Bed Summary Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, VISN Emergency Management Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Emergency Management Report</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, VISN Diversion Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Diversion Report</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, VISN Network Active Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Network Active Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, VISN Network Audit Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Network Audit Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, VISN Network Contract Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Network Contract Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>rep, VISN Network Disposition Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the VISN Network Disposition Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>rep, Wait List Status Report</p>
</blockquote></td>
<td><blockquote>
<p>Access the Patients Pending Placement Status Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Reports, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' buttons from the Home page corresponding to the reports.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SiteOptions, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, Site Options link.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SiteOptions, EvacuationConfirmation Read</p>
</blockquote></td>
<td><blockquote>
<p>Access to Evacuation Confirmation page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SiteOptions, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from Site Options page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SiteOptions, EvacuationConfirmation Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from Evacuation Confirmation page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transfer, AddTransfer Read</p>
</blockquote></td>
<td><blockquote>
<p>VISN page, Add New Patient button, Submit button from the Select Patient page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, EditTransfer Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the VISN page, Patients in Community</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Hospitals list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transfer, FinalizeTransfer Read</p>
</blockquote></td>
<td><blockquote>
<p>'Finalize' link from the VISN page, Patients in Community Hospitals list.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>VISN page, Add New Patient button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transfer, AddTransfer Update</p>
</blockquote></td>
<td><blockquote>
<p>VISN page, Add New Patient button, Submit button from the Select Patient page, and Submit button from the Enter Patient Data page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Transfer, EditTransfer Update</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the VISN page's Patients in Community Hospitals list and then Submit button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transfer, FinalizeTransfer Update</p>
</blockquote></td>
<td><blockquote>
<p>'Finalize' link from the VISN page's Patients in Community Hospitals list and then Submit button from the Finalize Patient Data page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UnavailableReason, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Bed Board Site Unavailable Reason page's list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UnavailableReason, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Bed Board Site Unavailable Reason page's list.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UnavailableReason, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Unavailable Reason Add/Edit link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UnavailableReason, Delete Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Bed Board Site Unavailable Reason page's list and then 'Delete Record' button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UnavailableReason, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Bed Board Site Unavailable Reason page's list and then Submit button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UnavailableReason, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Bed Board Site Unavailable Reason page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UserConfiguration, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Add/Edit BMS User link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UserConfiguration, SearchUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Find and Save' buttons from the 'Select user' page ('Select Existing NT User Name' button from the Site</p>
<p>Options, 'Add/Edit BMS User' link ).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UserConfiguration, SelectUser Read</p>
</blockquote></td>
<td><blockquote>
<p>'Select Existing NT User Name' button from the Site Options - Add/Edit BMS User page.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UserConfiguration, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Site Options - Add/Edit BMS User page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, Audit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Audit' tab on ADMINISTRATION SECTION -</p>
<p>Background Processors page (Background Processors Submenu) and 'Filter By' button from the 'Audit' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, Categories Read</p>
</blockquote></td>
<td><blockquote>
<p>'VistA Integration' tab on ADMINISTRATION SECTION - Background Processors page (Background Processors Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, DeleteScheduler Read</p>
</blockquote></td>
<td><blockquote>
<p>'Add new scheduler' link and select a scheduled name from the 'Scheduled' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Background Processors' link on ADMINISTRATION SECTION.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, Schedulers Read</p>
</blockquote></td>
<td><blockquote>
<p>'Schedulers' tab on ADMINISTRATION SECTION - Background Processors page (Background Processors<br />
Submenu).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, TestMDWSConnection Read</p>
</blockquote></td>
<td><blockquote>
<p>'TestMDWSConnection' button from the 'VistA Sites' tab.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, TestODBCConnection Read</p>
</blockquote></td>
<td><blockquote>
<p>'TestODBCConnection' button from the 'VistA Sites' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, VistASites Read</p>
</blockquote></td>
<td><blockquote>
<p>'VistA Sites' tab on ADMINISTRATION SECTION - Background Processors page (Background Processors<br />
Submenu).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, Categories Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save and Run' buttons from the 'VistA Integration' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, DeleteScheduler Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the 'Scheduled' tab and then 'Delete Record' button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Operation Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operation Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VistaIntegration, Schedulers Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from the 'Scheduled' tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistaIntegration, VistASites Update</p>
</blockquote></td>
<td><blockquote>
<p>'Save' button from the 'VistA Sites' tab.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WaitingArea, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Patient Waiting Areas page's list of Current Waiting Areas.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WaitingArea, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Patient Waiting Areas page's list of Current Waiting Areas.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WaitingArea, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Waiting Area Add/Delete link.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WaitingArea, DeleteAction Update</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Patient Waiting Areas page's list of Current Waiting Areas and then 'Delete Record button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WaitingArea, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>'Edit' link from the Patient Waiting Areas page's list of Current Waiting Areas and then Submit button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WaitingArea, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>'Add' button from the Patient Waiting Areas page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardConfiguration, Delete Read</p>
</blockquote></td>
<td><blockquote>
<p>'Delete' link from the Bed Board Ward Configuration, Current Vista Wards list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardConfiguration, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Vista Ward Add/Edit link.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardConfiguration, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Vista Ward Add/Edit link, Save button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardConfiguration, DeleteWard Update</p>
</blockquote></td>
<td><blockquote>
<p>Site Options, Vista Ward Add/Edit link, Delete operation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardOccupancy, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the Home page corresponding to the Ward Occupancy.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, Edit Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the BED column from WARD Whiteboard Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, EditPT Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the PT column from the WARD Whiteboard Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, 'Ward Whiteboard' link.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, NotifyChange Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the BED column from WARD Whiteboard Report and then on the Submit button.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WhiteboardStaff, Index Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on the checkbox from the STAFF column from the WARD Whiteboard Home.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, ShowReport Read</p>
</blockquote></td>
<td><blockquote>
<p>'Export Report' link from the right of the WARD Whiteboard Home page or WARD Whiteboard Report page, Export Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, Submit Read</p>
</blockquote></td>
<td><blockquote>
<p>'Submit' button from the WARD Whiteboard Home page.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteBoard, WardWhiteBoard Read</p>
</blockquote></td>
<td><blockquote>
<p>Home page, 'Ward Whiteboard' link, Submit button from the WARD Whiteboard Home.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WardWhiteboard, ClearAll Read</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the BED column from WARD Whiteboard Report and then click on the button 'Clear ALL Comments For ALL Wards Associate To This<br />
Bed…'.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteBoard, WardWhiteBoard Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on a staff name from the STAFF column from the WARD WhiteBoard Report and then click on the image<br />
'Save Staff'.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WhiteboardStaff, Index Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on the checkbox from the STAFF column from WARD Whiteboard Report and then on the 'Save' button.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WardWhiteboard, Edit Update</p>
</blockquote></td>
<td><blockquote>
<p>Click on a link from the BED column from WARD Whiteboard Report and then on the Submit button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## BMS Authentication and Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Authentication - BMS connects with single sign-on (SSOi) and the user inputs their PIV pin. The SSOi headers are supplied by the SSOi service validating their user credentials to the BMS Application. Their user credentials are parsed from the SSOi headers in order to verify that the user is authenticated and has a role in the BMS application. If the user does NOT have a role in BMS, the login is rejected.
- Authorization - Authorization occurs within the BMS Service layer. The application utilizes the Security Wrapper to Check Action and Check Permission for the user's account. The Security Wrapper queries the BMS database and the new Auth tables defined beginning in section 7.1.
- Check Action - Check Action queries the BMS database via the Security Wrapper for User Roles (BMS.AuthRole and BMS.AuthUserRoles) against the defined Actions (BMS.AuthAction and BMS.AuthRoleActions).
- Check Permission - The BMS Application validates the user's permission via the Security Wrapper by calling the CheckPermission to determine Read or Write access to a specific facility. This functionality is primarily reading the BMS.AuthUser and BMS.AuthPermissions tables.

<span id="_Toc536425835" class="anchor"></span>Figure -Class Diagram for Data Contracts in PAP and PDP

![](bed-management-solution-version-2-8-technical-manual/087.png)

## Symptom 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you try to load the BMS application, one of the following error messages appear:

<span id="_Toc72939430" class="anchor"></span>Figure -500 Server Error

![](bed-management-solution-version-2-8-technical-manual/088.png)

Problem

IIS is not started/running.

Diagnoses and Solutions

Start the IIS Manager and check if the Application Pool Identity is set to the correct service account. (). Verify the BMS pool is started, If stopped right click on the BMS, Select 'Start'.

## Symptom 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When trying to load the BMS application, one of the following error messages appears:

<span id="_Toc536425837" class="anchor"></span>Figure -No Facilities Error

> ![](bed-management-solution-version-2-8-technical-manual/089.png)

Diagnoses and Solutions

Go to the MULx5 machine and check if the BMS.ServiceHost service is stopped. Start the services.msc console and start the service.

## Symptom 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When trying to load the BMS application, one of the following error messages appears:

<span id="_Toc71031318" class="anchor"></span>Figure -Unhandled Exception

> ![](bed-management-solution-version-2-8-technical-manual/090.png)

Diagnoses and Solutions

- Check if BMS.BMService service is stopped or SQL Server might also have stopped.
- Go to the SQL Server machine and start the SQL Server from the SQL Server Configuration Manager. Verify if the connection string to the database server is set properly.
- Then go to the services' machine, start the services.msc console and start the BMS.BMService service.

## Symptom 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When trying to log-in to the BMS application, the following error is displayed:

<span id="_Toc71031319" class="anchor"></span>Figure -Login Unsuccessful

![](bed-management-solution-version-2-8-technical-manual/091.png)

Diagnoses and Solutions

Check if BMS.BMService service is stopped. Go to the services' machine, start the services.msc console and start the service.

## Symptom 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data does not appear in the reports. Data does not get refreshed in the reports.

Diagnoses and Solutions

In SQL Configuration Manager, check if the SQL Server Agent is started, and if it isn't start it; then, in the SQL Server Management Studio, check if the *BMS - Reports Full* and *BMS - Reports Incremental* are deployed and run without errors. If the jobs are not deployed, install them.

## Symptom 6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A report is missing from Other Reports section on the Facility Home Page (e.g. *EMS Bed Status Report (Admin)*).

<span id="_Toc71031320" class="anchor"></span>Figure - EMS Bed Status Report is Missing

![](bed-management-solution-version-2-8-technical-manual/092.png)

Diagnoses and Solutions

Check if the report is missing from the SQL Server Reporting Services. Go to the management web page and add the missing report (Upload File).

## Symptom 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When trying to view one of the reports (other than the *Other Reports*) the following error appears:

<span id="_Toc71031321" class="anchor"></span>Figure - Report Cannot be Found

![](bed-management-solution-version-2-8-technical-manual/093.png)

Diagnoses and Solutions

Check if the mentioned report is missing from the Reporting Services. Go to the management web page and add the specified report.

## BMS Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are five log files available to anyone supporting the BMS system, the WinServiceHost, the SecurityHost, the BMS.ServiceHost, the BMS.VI.ServiceHost and the WebTrace log.

- The WinServiceHost log file is named BMS-Services.log and its location is on the application server (vaausbmsmulx5) D:\BMS\Bin.
- The BMS.ServiceHost logfile is named BMS.trace.log and its location is on the application server (vaausbmsmulx5) at D:\BMS\Bin\BMS.
- The BMS.VI.ServiceHost logfile is named BMS.VI.trace.log and its location is on the application server (vaausbmsmulx6) at D:\BMS\Bin\BMS.
- The Web trace log is named WebTrace.log and its location is on the web server (vaausbmswebx5) at D:\BMS\BMS.Web.

These logs contain various types of information (informational, warnings, and errors) with the exception of the web trace log, which only contains error messages.

There is no log file for MDWS, those errors are captured through our integration calls and posted in the BMS.ServiceHost log file (Trace.log). These are bit trickier to debug as in any attempt requires the exact parameters to be passed to MDWS.

### From: Bed Management Solution Version 2.9 Technical Manual

## BMS AuthRoleActions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AuthRoleActions table associates the AuthActionId from the AuthActions table and the AuthRoleId from the AuthRoles table for purposes of tying the Roles and Actions together.

<span id="_Toc84579883" class="anchor"></span>Figure -AuthRoleActions table

![](bed-management-solution-version-2-9-technical-manual/081.png)

### From: Bed Management Solution Version 2.11 Technical Manual

## Inflow Architectural Removal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Beginning in the summer of 2020, the technical development team was tasked with the complete removal of the Inflow third party service component within BMS. This was a proprietary and poorly performing service layer/architecture which was impeding the progression of the BMS application as a whole.

Other aspects of this project were to remove the reliance and re-architect the following:

- DataWarehouse – the database(s) BMS_DW and BMS_DS were utilized to enable reporting to access database(s) separate from the application's database.
- Report Jobs – both nightly and incremental (every 15 minute) jobs responsible for constantly feeding the BMS_DW (data warehouse) database which affected performance and often failures would result in end users not being able to run reports effectively.

Changes to just about every aspect of BMS were necessary to allow for this removal, except for the User Interface. The goal was to maintain the same user functionality but also to make BMS more efficient and less hardware dependent.

This was accomplished as part of the 2\*25 release by utilizing the following high-level strategies:

- For every line of code and stored procedure which touched the following databases, we had to recode to utilize the new source and target database while maintaining the exact same functionality.
- Remove/Rebuild the following databases and relocate them to an appropriate new dataset(s) within other table(s)
  - BMS_AUTHZ.
  - BMS_EVS
  - BMS_EIS database
- Utilize and enhance the database replication that was being used by other reporting teams which was created by a previous BMS development team. This would remove the need for the BMS_DW and BMS_DS databases as well as the ReportJobs (Full and Incremental)
- Remove the need for database triggers to populate the previously existing BMS_History database tables by utilizing Change Data Capture (CDC) as well as create new BMS_HISTORY tables to reflect the new tables added as part of the Inflow removal.

The image below represents a high-level database architecture of BMS with the Inflow service/database architecture:

<span id="_Toc103783357" class="anchor"></span>Figure - Previous version of BMS (with Inflow)

![](bed-management-solution-version-2-11-technical-manual/046.png)

The next diagram represents the newly architected version of BMS without Inflow.

<span id="_Toc103783358" class="anchor"></span>Figure - Current version of BMS (without Inflow)

![](bed-management-solution-version-2-11-technical-manual/047.png)

### From: Bed Management Solution Version 3.10 Technical Manual

### # # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Bed Management Solution Contingency Report Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps will need to be completed in order to setup the BMS Contingency Report

- Create snapshot folder
- Define network share
- Assign rights to user
- Assign snapshot folder path to ward group
- Associate scheduler with the whiteboard report

### Create Snapshot Folder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To create the Snapshot Folder on Windows 10:

- Open File Explorer
- Go to the C Drive (or alternate drive letter if appropriate)
- Click New Folder
- Enter the Name of the folder, e.g., WhiteBoardSnapshot
  - Do not use spaces in the folder name

<span id="_Toc536425802" class="anchor"></span>

Figure - Whiteboard Snapshot Folder

> ![](bed-management-solution-version-3-10-technical-manual/019.png)

### Define Network Share

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Admin rights to the machine are required for this step.

- Navigate to the "WhiteboardSnapshot" folder, right-click it and choose Properties

<span id="_Toc132648101" class="anchor"></span>Figure - Whiteboard Snapshot Folder Properties

> ![](bed-management-solution-version-3-10-technical-manual/020.png)

- *Go to Sharing tab and select Advance Sharing option.*

<span id="_Toc536425804" class="anchor"></span>

Figure - Advanced Sharing Option

> ![](bed-management-solution-version-3-10-technical-manual/021.png)

- In Advanced Sharing dialog, enable Share this folder option. It will automatically add folder's name as Share name.

<span id="_Toc132648103" class="anchor"></span>Figure - Share this Folder Option

> ![](bed-management-solution-version-3-10-technical-manual/022.png)

- Click OK
- Verify the network path is now populated with the computer name and folder

<span id="_Toc132648104" class="anchor"></span>Figure - Verify Network Path

![](bed-management-solution-version-3-10-technical-manual/023.png)

### Assign Rights to Master BMS Service Account User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Admin rights to the machine are required for this step.

The BMS Application runs under a service account. AITC has created the Windows User (aac\OITAUSBMSPRD) as the master service account that the BMS Services runs under. The Windows user (aac\OITAUSBMSPRD) that is configured to be the Login that runs the four BMS Windows Services needs to have full rights to these shares.

This user must have full control on each facilities file folder that is used to store the Whiteboard Contingency Reports.

> *On Windows 10 the needed operations are:*

- Using the Advanced Sharing window (re-open from the previous steps), click Permissions
- Click Add
- Type in "AAC\OITAUSBMSPRD" and click Check Names

<span id="_Toc132648105" class="anchor"></span>Figure - Permissions for Whiteboard Snapshot

> ![](bed-management-solution-version-3-10-technical-manual/024.png)

- Click OK
- Select the Service Account and check the "Full Control" box

<span id="_Toc132648106" class="anchor"></span>Figure - Permissions for Whiteboard Snapshot

![](bed-management-solution-version-3-10-technical-manual/025.png)

- Click OK through the rest of the open Folder Properties windows
- Using the Windows Start button and Search, open "edit local users and groups"
  - Make sure to open as Administrator
- Click Groups
- Double click the Remote Desktop Users group
- Add the BMS Service Account

<span id="_Toc132648107" class="anchor"></span>Figure - Select Users

![](bed-management-solution-version-3-10-technical-manual/026.png)

- Click OK

<span id="_Toc132648108" class="anchor"></span>Figure - Remote Desktop Users Properties

![](bed-management-solution-version-3-10-technical-manual/027.png)

- Click OK

### Assign Snapshot Folder Path to Ward Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Open BMS and navigate to the Facility Home Page
- Click Site Options
- Click Contingency Settings
- Add the Fully Qualified Domain Name for the configured Whiteboard Snapshot folder
  - \\XYZ-CMP12345.v06.med.va.gov\WhiteboardSnapshot
- Click Save

<span id="_bookmark85" class="anchor"></span>Figure - Contingency Settings Page

![](bed-management-solution-version-3-10-technical-manual/028.png)

### Associate Scheduler with Whiteboard Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Open BMS and navigate to the Facility Home Page
- Click Site Options
- Click Background Processors
- Change the drop-down selection for Add/Update Scheduler to the desired schedule

<span id="_bookmark87" class="anchor"></span>Figure - Add Scheduler for Background Processors

![](bed-management-solution-version-3-10-technical-manual/029.png)

- Click Save Scheduler

### Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authorization occurs within the BMS Service layer. The application utilizes the Security Wrapper to Check Action and Check Permission for the user's account. The Security Wrapper queries the BMS database and the new Auth tables defined beginning in section 7.1.

- Check Action

> Check Action queries the BMS database via the Security Wrapper for User Roles (BMS.AuthRole and BMS.AuthUserRoles) against the defined Actions (BMS.AuthAction and BMS.AuthRoleActions).

- Check Permission

> The BMS Application validates the user's permission via the Security Wrapper by calling the CheckPermission to determine Read or Write access to a specific facility. This functionality is primarily reading the BMS.AuthUser and BMS.AuthPermissions tables.

### From: Bed Management Solution Version 5.0 Technical Manual

### Adding a New VistA Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a VA facility site to a VistA instance, follow the steps presented below.

- From the Background Processors page of Admin section select VistA Sites to display the page in the following image. A list of VA facility sites is displayed in the column to the left of the page.

<span id="_Toc536425820" class="anchor"></span>Figure 33-Adding a VistA Site

> ![](bed-management-solution-version-5-0-technical-manual/033.png)

- Click the Add new VistA site link then from the VistA Site area use the Name field to select the code of the site you want to add to the current VistA instance, and then select the Time Zone.
- Press Save to enter new data into the system.

The newly added site will be added in the sites list to the left of the screen.

## PPMS Integration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PPMS tab is for scheduling an extract of in-network Community Care Facilities from an external Provider Profile Management System. These facility records are visible from the Community Care Facility field located in a Patients Pending Bed Placement or Community Care Tracking List record and can be reviewed via [Community Care Sites](\l).

The PPMS job can be scheduled to run as frequently as monthly (or on-demand), but is recommended to run on a quarterly basis.

The PPMS tab is displayed as in the following image:

<span id="_Toc204758294" class="anchor"></span>Figure 40-PPMS page

![](bed-management-solution-version-5-0-technical-manual/040.png)

If necessary, make changes to the Recurs every, Start Time and Time Zone fields, then press the Save button. If an ad-hoc run of the PPMS job is necessary, select the Run Today checkbox, then press the Save button.

![](bed-management-solution-version-5-0-technical-manual/041.png) The Run Today option kicks off the PPMS job within 5 minutes.

![](bed-management-solution-version-5-0-technical-manual/042.png) Pressing the Clear Schedule button will remove the Next Run Date and Job Status information.

| Column        | Description                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------|
| Recurs every  | Frequency of PPMS job run by number of months.                                                        |
| Start Time    | Hour and minute when the next PPMS job is schedule to run.                                            |
| Time Zone     | The time zone of the Start Time.                                                                      |
| Run Today     | A checkbox for running the PPMS job one hour after pressing the Save button.                          |
| Next Run Date | The date and time when the PPMS job is scheduled to run.                                              |
| Last Run Date | The date and time when the PPMS job last ran.                                                         |
| Job Status    | The status of the previous PPMS job. Possible values are Not Yet Run, Running, Successful and Failed. |

<span id="_bookmark122" class="anchor"></span>Table 13-BMS Database Files

## Application Flow Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc204758325" class="anchor"></span>Figure 71 - Application Flow Map

> ![](bed-management-solution-version-5-0-technical-manual/074.png)
