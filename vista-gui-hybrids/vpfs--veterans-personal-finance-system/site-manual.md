---
title: VPFS Version 1.2 Systems Management Guide
doc_type: SM
doc_label: Site Manual / Systems Management Guide
doc_layer: anchor
doc_subject: Systems Management Guide
app_code: VPFS
app_name: Veterans Personal Finance System
section: GUI
app_status: active
pkg_ns: VPFS
patch_ver: 1.2
patch_id: VPFS*1.2
group_key: "VPFS:VPFS:1.2"
file_numbers: []
security_keys: []
menu_options: 4
description: > Veterans Personal Finance System (VPFS) is the reengineered version of VistA Personal Funds of Patients (PFOP) system, also known as Integrated Patient Funds (IPF), the mini-banking system that manages the accounts of patients in the VA hospital system.
audience: 
keywords: 
  - blockquote
  - class
  - strong
  - table
  - style
  - width
  - vpfs
  - patient
  - contents
  - even
page_count: 0
word_count: 21836
section_count: 37
table_count: 0
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: July 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/vpfs_systems_management_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/vpfs_systems_management_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=170"
---

> ![](vpfs-version-1-2-systems-management-guide/001.png)

Veterans Personal Finance System (VPFS)

Systems Management Guide

> Version 1.2.0

> July 2020

> Department of Veterans Affairs (VA) Office of Information and Technology (OIT)

> Enterprise Program Management Office (EPMO)

> Revision History

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Chapter Descriptions and Roles](#chapter-descriptions-and-roles)
- [System Requirements](#system-requirements)
  - [Server Environment](#server-environment)
    - [Oracle Server](#oracle-server)
    - [WebLogic Server](#weblogic-server)
  - [Developer Environment](#developer-environment)
    - [Development Platform](#development-platform)
    - [Development Tools](#development-tools)
    - [Frameworks and Libraries](#frameworks-and-libraries)
    - [VA Services](#va-services)
    - [Builds](#builds)
- [VPFS Application](#vpfs-application)
  - [Enterprise Archive](#enterprise-archive)
    - [Application.xml](#applicationxml)
    - [Weblogic-application.xml](#weblogic-applicationxml)
    - [Web Application](#web-application)
  - [HealtheVet Configuration Files](#healthevet-configuration-files)
  - [Other Configuration Properties](#other-configuration-properties)
  - [Logging](#logging)
    - [Application Server Log File](#application-server-log-file)
    - [VPFS Log File](#vpfs-log-file)
    - [PSL Log Files](#psl-log-files)
    - [PSC Log File](#psc-log-file)
    - [VistALink Log File](#vistalink-log-file)
  - [Exceptions](#exceptions)
  - [Service Imports](#service-imports)
    - [Electronic Signature](#electronic-signature)
    - [KAAJEE](#kaajee)
    - [VistALink for Java](#vistalink-for-java)
  - [Source Code](#source-code)
  - [Javadoc](#javadoc)
  - [Business Rules Implementation](#business-rules-implementation)
    - [Security](#security)
    - [Transactions](#transactions)
    - [Email Notifications](#email-notifications)
    - [Table Maintenance](#table-maintenance)
    - [Electronic Signature](#electronic-signature-1)
- [Database - M VistA](#database-m-vista)
  - [Namespace](#namespace)
  - [Routines](#routines)
  - [Options](#options)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [Online Documentation](#online-documentation)
  - [Checksum Values for Routines](#checksum-values-for-routines)
  - [Security and Keys](#security-and-keys)
- [Database - Oracle](#database-oracle)
  - [Database](#database)
  - [Schemas](#schemas)
  - [Users](#users)
  - [Roles](#roles)
  - [Tablespaces](#tablespaces)
  - [Tables](#tables)
    - [Tables in the VPFS Schema](#tables-in-the-vpfs-schema)
    - [Tables in the VISTAMIGRATE Schema](#tables-in-the-vistamigrate-schema)
  - [Field Information](#field-information)
  - [Views](#views)
    - [Views in the VPFS Schema](#views-in-the-vpfs-schema)
  - [![](vpfs-version-1-2-systems-management-guide/030.png)![](vpfs-version-1-2-systems-management-guide/031.png)![](vpfs-version-1-2-systems-management-guide/032.png)![](vpfs-version-1-2-systems-management-guide/033.png)Procedures](#vpfs-version-1-2-systems-management-guide030pngvpfs-version-1-2-systems-management-guide031pngvpfs-version-1-2-systems-management-guide032pngvpfs-version-1-2-systems-management-guide033pngprocedures)
    - [Stored Procedures in the VPFS Schema](#stored-procedures-in-the-vpfs-schema)
    - [![](vpfs-version-1-2-systems-management-guide/034.png)Stored Procedures in the VISTAMIGRATE Schema](#vpfs-version-1-2-systems-management-guide034pngstored-procedures-in-the-vistamigrate-schema)
  - [Triggers](#triggers)
    - [Triggers in the VPFS Schema](#triggers-in-the-vpfs-schema)
  - [![](vpfs-version-1-2-systems-management-guide/088.png)![](vpfs-version-1-2-systems-management-guide/089.png)![](vpfs-version-1-2-systems-management-guide/090.png)![](vpfs-version-1-2-systems-management-guide/091.png)![](vpfs-version-1-2-systems-management-guide/092.png)![](vpfs-version-1-2-systems-management-guide/093.png)![](vpfs-version-1-2-systems-management-guide/094.png)![](vpfs-version-1-2-systems-management-guide/095.png)![](vpfs-version-1-2-systems-management-guide/096.png)![](vpfs-version-1-2-systems-management-guide/097.png)Scheduled Jobs](#vpfs-version-1-2-systems-management-guide088pngvpfs-version-1-2-systems-management-guide089pngvpfs-version-1-2-systems-management-guide090pngvpfs-version-1-2-systems-management-guide091pngvpfs-version-1-2-systems-management-guide092pngvpfs-version-1-2-systems-management-guide093pngvpfs-version-1-2-systems-management-guide094pngvpfs-version-1-2-systems-management-guide095pngvpfs-version-1-2-systems-management-guide096pngvpfs-version-1-2-systems-management-guide097pngscheduled-jobs)
    - [Jobs in the VPFS Schema](#jobs-in-the-vpfs-schema)
  - [External Dependencies](#external-dependencies)
    - [Standard Data Service (SDS)](#standard-data-service-sds)
  - [Locking](#locking)
- [Integration Agreements](#integration-agreements)
    - [Supported](#supported)
    - [Controlled Subscription](#controlled-subscription)
    - [Private](#private)
- [Patient Demographics Updates](#patient-demographics-updates)
  - [Data Updated](#data-updated)
  - [On-demand Update](#on-demand-update)
  - [Scheduled Update](#scheduled-update)
- [Data Migration](#data-migration)
  - [Configuration](#configuration)
- [VPFS Troubleshooting](#vpfs-troubleshooting)
- [VistAMigrate Troubleshooting](#vistamigrate-troubleshooting)
- [Appendix B VPFS Security Roles Matrix](#appendix-b-vpfs-security-roles-matrix)
> The following table displays the revision history for this document. Revisions to the documentation are based on continuous dialogue with the VPFS development team.
<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 47%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revision</strong></p>
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
<p>12/1/06</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Initial release of document</p>
</blockquote></td>
<td><blockquote>
<p>Project Manager: <mark>REDACTED</mark></p>
<p>Developers:</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>06/03/10</p>
</blockquote></td>
<td><blockquote>
<p>1.1.2</p>
</blockquote></td>
<td><blockquote>
<p>Page 5 – Modified EVS to EPS.</p>
<p>Page 9, 14 -- Updated SDS, VLJ and KAAJEE versions.</p>
<p>Page 16 – Updated Data Base version.</p>
<p>Section 4.6 – Replaced PATS with VPFS. Page 5,7,26- Replaced EMC with EIE</p>
<p>Paragraph 5.12.1- added the missing table</p>
<p>„std_facilitytype‟</p>
<p>These changes are associated with the VPFS patch release 1.1.2</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/28/10</p>
<p>12/22/10</p>
</blockquote></td>
<td><blockquote>
<p>1.1.3</p>
</blockquote></td>
<td><blockquote>
<p>Page 9, 14 -- Updated SDS version from 13</p>
<p>to 18.</p>
<p>Page 9 –Added Java version</p>
<p>These changes are associated with the VPFS patch release 1.1.3</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>From 01/05/2019 –</p>
<p>02/05/2020</p>
</blockquote></td>
<td><blockquote>
<p>1.2.0</p>
</blockquote></td>
<td><blockquote>
<p>Software &amp; Plug-in updates</p>
</blockquote></td>
<td><blockquote>
<p>Developers: <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Veterans Personal Finance System (VPFS) is the reengineered version of VistA Personal Funds of Patients (PFOP) system, also known as Integrated Patient Funds (IPF), the mini-banking system that manages the accounts of patients in the VA hospital system.

> The VPFS Systems Management Guide gives a technical overview of VPFS for supporting and maintaining the application. The intended audience of this guide is: Information Resource Management (IRM), Enterprise Infrastructure Engineering (EIE) Health Solutions, and Enterprise Product Support (EPS).

> VPFS is a web-based application. Both the VPFS application and database are maintained at the EIE in Falling Waters, VA.

## Chapter Descriptions and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The guide is divided into the following sections:

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 41%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Chapter Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Intended Audience</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>Introduction</p>
</blockquote></td>
<td><blockquote>
<p>Java developers and System Admin</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>System Requirements</p>
</blockquote></td>
<td><blockquote>
<p>Java developers and System Admin</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>VPFS Application</p>
</blockquote></td>
<td><blockquote>
<p>Java developers and System Admin</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>Business Rules Implementation</p>
</blockquote></td>
<td><blockquote>
<p>Business layer developer at EIE, Maintenance and EPS Support</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>Database – M VistA</p>
</blockquote></td>
<td><blockquote>
<p>IRM staff, Maintenance, and EPS Support</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>Database – Oracle</p>
</blockquote></td>
<td><blockquote>
<p>Database Administrator (DBA) at the EIE, Maintenance, and EPS Support</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>Integration Agreements</p>
</blockquote></td>
<td><blockquote>
<p>EIE, Maintenance, and EPS Support</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td><blockquote>
<p>Patient Demographics Updates</p>
</blockquote></td>
<td><blockquote>
<p>EIE, Maintenance, and EPS Support</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 41%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>8</p>
</blockquote></th>
<th><blockquote>
<p>Data Migration</p>
</blockquote></th>
<th><blockquote>
<p>EIE and EPS Support</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>VPFS Troubleshooting</p>
</blockquote></td>
<td><blockquote>
<p>EIE and EPS Support</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>VistAMigrate Troubleshooting</p>
</blockquote></td>
<td><blockquote>
<p>EIE and EPS Support</p>
</blockquote></td>
</tr>
</tbody>
</table>

> This page is left blank intentionally.

> System Requirements

# System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Server Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vpfs-version-1-2-systems-management-guide/002.png)The following components are required for the production VPFS environment: Oracle 12g Server

> ![](vpfs-version-1-2-systems-management-guide/003.png)![](vpfs-version-1-2-systems-management-guide/004.png)WebLogic Server 10.3.6 (or later) VistA Server

> Additional components such as a hardware load balancer and Secure Sockets Layer (SSL) server are being managed by the EIE.

### Oracle Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Oracle server must have Oracle 10g Server installed.

> ![](vpfs-version-1-2-systems-management-guide/005.png)VPFS requires the following schemas installed in an Oracle instance accessible by the WebLogic server: VPFS – Primary schema used by VPFS. All VPFS data is stored in this schema.

> ![](vpfs-version-1-2-systems-management-guide/006.png)VistAMigrate – Required to perform migrations from PFOP. After all stations have been migrated, the VistAMigrate schema can be removed.

> ![](vpfs-version-1-2-systems-management-guide/007.png)SDS – The VPFS schema has a view that references certain Standard Data Service (SDS) tables, therefore this schema must be accessible from the VPFS schema.

> ![](vpfs-version-1-2-systems-management-guide/008.png)KAAJEE – The KAAJEE schema is used by the Kernel Authentication & Authorization for J2EE (KAAJEE) Security Service Provider Interfaces (SSPI), not VPFS directly. Typically, it would be installed in the same database instance as VPFS, although technically, it does not have to be.

### WebLogic Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> WebLogic 10.3.6 was used during development and has been identified as the target production version.

> All dependencies must be installed and configured in the WebLogic domain designated for VPFS. This includes VistALink, KAAJEE SSPIs, Person Service Lookup (PSL), and Person Service Construct (PSC). (Electronic Signature does not have any installable components on the application server.) Refer to the documentation for each dependency for any specific requirements for that dependency.

> Database connection pools and datasources must be installed for VPFS, VistAMigrate, and SDS.

> Note: This version of VPFS uses VistALink libraries that have reverse-IP check enabled. Confirm all entries in the VistALink connectorConfig.xml file have the reverse IP information configured. Otherwise VistALink connector will not be able to connect out to those systems. This was done for security purposes and to pass Fortify compliance.

## Developer Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS Java Enterprise developer workstations are dependent on remote and local services. All VA Java service dependencies are deployed locally. Oracle databases were available both locally and remotely. VistA databases were utilized remotely.

### Development Platform

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS was developed using the following infrastructure on Windows workstations:

> *7*

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Application</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>WebLogic 10.3.6</p>
</blockquote></td>
<td><blockquote>
<p>All service dependencies are required to be setup on a local WebLogic server.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Oracle 12g</p>
</blockquote></td>
<td><blockquote>
<p>Individual development and test database installed locally</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>InterSystems Caché</p>
</blockquote></td>
<td><blockquote>
<p>Individual development and test VistA database installed locally</p>
<p><em>(for M developers)</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Development Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following tools were used for VPFS development:

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Application</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Eclipse 3.1 and MyEclipse 4.0</p>
</blockquote></td>
<td><blockquote>
<p>Integration of Eclipse and WebLogic 10.3.6 allowed hot deployment and hotswap debugging.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Ant 1.6</p>
</blockquote></td>
<td><blockquote>
<p>Automated build tool used for VPFS and VistAMigrate. Each project root directory contains a build file named build.xml.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Microsoft Visual Source Safe</p>
</blockquote></td>
<td><blockquote>
<p>Source Control Management</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Quest Software TOAD 8.0</p>
</blockquote></td>
<td><blockquote>
<p>TOAD was used to connect to the Oracle database(s) to verify that data was updated correctly. TOAD can also be used to generate database scripts from a developed schema, and has a PL/SQL editor for editing stored procedures, triggers, etc.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Oracle Enterprise Manager Console</p>
</blockquote></td>
<td><blockquote>
<p>Installed with Oracle 10g Server. Allows DBA to manage Oracle database instances.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SmarTerm</p>
</blockquote></td>
<td><blockquote>
<p>Terminal emulation software for connecting to remote VistA servers. <em>(for M developers)</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Frameworks and Libraries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Development Frameworks

> The following development frameworks are used in the VPFS application:

> ![](vpfs-version-1-2-systems-management-guide/009.png)Log4J – Logging framework

![](vpfs-version-1-2-systems-management-guide/010.png)Struts – Servlet framework implementing a variation of the classic Model-

View-

> Controller (MVC) design paradigm

> ![](vpfs-version-1-2-systems-management-guide/011.png)Tiles – JavaServer Pages (JSP) templating framework

2.  Additional Libraries

> All libraries required for building VPFS are included in the project lib directory except the following system libraries, included with WebLogic:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Library Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>J2EE v 1.7_80</p>
</blockquote></td>
<td><blockquote>
<p>Java Enterprise Edition, Java Development Kit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JRE System Library 1.8</p>
</blockquote></td>
<td><blockquote>
<p>General Java Runtime Environment (JRE) class library</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WebLogic 10.3.6</p>
</blockquote></td>
<td><blockquote>
<p>WebLogic tools, drivers, etc.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### VA Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vpfs-version-1-2-systems-management-guide/012.png)The following VA services are deployed locally in a development Weblogic server: Standard Data Service (SDS) API jars 18.0

> ![](vpfs-version-1-2-systems-management-guide/013.png)VistALink for Java (VLJ) 1.6

> ![](vpfs-version-1-2-systems-management-guide/014.png)![](vpfs-version-1-2-systems-management-guide/015.png)Kernel Authentication Authorization Java Enterprise Environment (KAAJEE) 1.0.1.003 Person Service Lookup (PSL) 4.0.4.3

> ![](vpfs-version-1-2-systems-management-guide/016.png)![](vpfs-version-1-2-systems-management-guide/017.png)Patient Service Construct (PSC) 2.0.0.8 Electronic Signature (eSig) 1.0.0.024

### Builds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Ant is used as the build tool for the VPFS and VistAMigrate applications, as well as to assemble the database script zip file and the release package.

> Each project has its own build file (build.xml) containing *targets*, or different actions to take on that project. For example, the *ear* target in the VPFS build.xml will compile the application, prepare the application for WebLogic deployment, and update the build date, all before creating the ear file.

3.  VPFS Build Targets

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Target</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 20%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="7"></th>
<th><blockquote>
<p>build</p>
</blockquote></th>
<th><blockquote>
<p>Compiles the application source code, prepares the application for WebLogic deployment (calls weblogic.appc), and updates the build date in the Version.properties file.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>clean</p>
</blockquote></th>
<th><blockquote>
<p>Removes all compiled files to ensure all classes are recompiled.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ear</p>
</blockquote></th>
<th><blockquote>
<p>Builds the application prior to creating the application ear file.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>javadoc</p>
</blockquote></th>
<th><blockquote>
<p>Generates javadoc for all VPFS classes (gov.va.med.vpfs.* package).</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>release</p>
</blockquote></th>
<th><blockquote>
<p>Performs a clean rebuild of the application, creates the application ear file, generates the versioned readme and Release Notes from the templates, then generates a MD5 checksum for the ear file.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>verifychecksum</p>
</blockquote></th>
<th><blockquote>
<p>Verifies the MD5 checksum for the application ear to ensure the ear file has not changed since the checksum was generated.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>version</p>
</blockquote></th>
<th><blockquote>
<p>Increments the build number in the Version.properties file.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  VistAMigrate Build Targets

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Target</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>build</p>
</blockquote></td>
<td><blockquote>
<p>Compiles the application source code, prepares the application for WebLogic deployment (calls weblogic.appc), and updates the build date in the Version.properties file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>clean</p>
</blockquote></td>
<td><blockquote>
<p>Removes all compiled files to ensure all classes are recompiled.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ear</p>
</blockquote></td>
<td><blockquote>
<p>Builds the application prior to creating the application ear file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>release</p>
</blockquote></td>
<td><blockquote>
<p>Performs a clean rebuild of the application, creates the application ear file, generates the versioned readme and Release Notes from the templates, then generates a MD5 checksum for the ear file.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>verifychecksum</p>
</blockquote></td>
<td><blockquote>
<p>Verifies the MD5 checksum for the application ear to ensure the ear file has not changed since the checksum was generated.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>version</p>
</blockquote></td>
<td><blockquote>
<p>Increments the build number in the Version.properties file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VPFS Application

# VPFS Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS is designed to run on a Java Enterprise Edition (J2EE) 1.3 compliant application server running on a

> 1.4 Java Virtual Machine (JVM).

> ![](vpfs-version-1-2-systems-management-guide/018.png)VPFS can be deployed in two basic ways on Weblogic: an Enterprise Archive (.ear) file, or

> ![](vpfs-version-1-2-systems-management-guide/019.png)an “exploded” ear directory structure

## Enterprise Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS deploys as a Java Enterprise Archive named VPFS-*major.minor.revision.build*.ear containing the following elements.

> ![](vpfs-version-1-2-systems-management-guide/020.png)

### Application.xml

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file exists in the META-INF directory per the J2EE 1.3 specifications. The contents are the modules and logical security roles of the VPFS application.

### Weblogic-application.xml

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This file exists in the META-INF directory. No special settings in this deployment descriptor

### Web Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VPFS enterprise archive contains the VPFS web application.

> The VPFS directory is the web context root. The web context root contains the following application directories: (The files in bold text contain elements that are configurable during deployment.)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Directory</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>etc</p>
</blockquote></th>
<th><blockquote>
<p>Contains common cascading stylesheets (CSS) and JavaScript files for VPFS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Directory</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>images</p>
</blockquote></td>
<td><blockquote>
<p>Contains application images (gif and jpeg files) for VPFS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>login</p>
</blockquote></td>
<td><blockquote>
<p>Contains KAAJEE login pages. These pages are used to authenticate users.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>plu</p>
</blockquote></td>
<td><blockquote>
<p>Contains PSL pages. These pages are used to look-up and register patients in VPFS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>stylesheets</p>
</blockquote></td>
<td><blockquote>
<p>Contains common CSS stylesheets for PSL (not VPFS).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WEB-INF</p>
</blockquote></td>
<td><blockquote>
<p>Contains web.xml, <strong>weblogic.xml</strong>, and various configuration files, taglibs, classes, JSPs, and libraries per the Servlet and JSP specifications.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WEB-INF/classes</p>
</blockquote></td>
<td><blockquote>
<p>Contains the configuration property files for PSL (<strong>PatientLookup.properties</strong>) and PSC (<strong>PatSvcPkg.properties</strong>).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WEB-INF/config</p>
</blockquote></td>
<td><blockquote>
<p>Contains KAAJEE (<strong>kaajeeConfig.xml</strong>) and log4j (<strong>log4j.xml</strong>) configuration files.</p>
<p>Also contains application configuration files for Struts, Tiles, etc. Any modification of these files shall be considered a change to application code and should be managed accordingly.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WEB-INF/jsps</p>
</blockquote></td>
<td><blockquote>
<p>Contains the JSP pages for VPFS.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WEB-INF/lib</p>
</blockquote></td>
<td><blockquote>
<p>Contains the external jar files used by the web application.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WEB-INF/templates</p>
</blockquote></td>
<td><blockquote>
<p>Contains the JSP Tiles for VPFS.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WEB-INF/tlds</p>
</blockquote></td>
<td><blockquote>
<p>Contains the tag library descriptors.</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Web.xml and Weblogic.xml

> Web.xml is the main configuration file for the VPFS web application. Web.xml contains:

- context parameters servlets
- servlet mappings
- security roles
- security constraints
- login configuration
- taglib declarations
- welcome files
- error pages, mime mappings, listeners, and environment entries

> Weblogic.xml contains the mapping of the application role to the actual WebLogic security realm. It also contains the security role assignment for the KAAJEE LoginController.

2.  PSL and PSC Configuration Files

> The PatientLookup.properties and PatSvcPkg.properties files are the configuration files for PSL and PSC, respectively, located in the WEB-INF/classes directory. These files contain the providerURL, securityProvider and securityCredentials properties that must be updated to reference the correct location and security information for connecting to the PSL and PSC Enterprise JavaBeans (EJBs).

> Refer to PSL and PSC documentation for more information about the contents of these files.

3.  KAAJEE Configuration File

> The kaajeeConfig.xml file is the configuration file for KAAJEE, located in the WEBINF/config directory. This file contains the list of station numbers that will appear in the Institution drop-down list on the KAAJEE login page.

> Refer to KAAJEE documentation for more information about the contents of this file.

4.  Other Configuration Files

> VPFS uses the Struts framework with the Tiles templating framework internally. The struts-config.xml and tiles-defs.xml files for configuring these frameworks are located in the WEB-INF/config folder.

5.  Stylesheets

> The main CSS stylesheet for VPFS is vpfs.css, located in the /etc directory. The main CSS stylesheet for the text-only (508-compliant) mode is vpfs508.css, also located in the /etc directory. These stylesheets are used to maintain a consistent look and feel throughout VPFS.

6.  Libraries

> The following libraries define application programming interfaces (APIs) that are included and required by VPFS, and are located in the WEB-INF/lib directory:

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Library Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CAIP.jar</p>
</blockquote></td>
<td><blockquote>
<p>Used by PSL/PSC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>commons-beanutils.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library, used by Struts/Tiles</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>commons-collections-3.1.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library, used by Struts/Tiles</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>commons-dbcp-1.2.1.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>commons-digester.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library, used by Struts/Tiles</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>commons-fileupload.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library, used by Struts/Tiles</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>commons-httpclient-2.0.1.jar</p>
</blockquote></th>
<th><blockquote>
<p>Jakarta Commons library</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>commons-lang-2.0.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>commons-lang.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Library Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>commons-logging-1.0.3.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>commons-pool-1.2.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>commons-resources.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>commons-services.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>commons-validator.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library, used by Struts/Tiles</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>dbunit-2.0.jar</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>displaytag-1.0-b2.jar</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>esig-1.0.0.024.jar</p>
</blockquote></td>
<td><blockquote>
<p>Electronic Signature</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>jakarta-oro.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library, used by Struts/Tiles</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>jakarta-regexp-1.3.jar</p>
</blockquote></td>
<td><blockquote>
<p>Jakarta Commons library</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>jaxen-core.jar</p>
</blockquote></td>
<td><blockquote>
<p>XML (eXtensible Markup Language) parsing API</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>jaxen-dom.jar</p>
</blockquote></td>
<td><blockquote>
<p>XML parsing API</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>jstl.jar</p>
</blockquote></td>
<td><blockquote>
<p>JSTL (Java Standard Template Library)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>junit-3.8.1.jar</p>
</blockquote></td>
<td><blockquote>
<p>Unit Testing API</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>kaajee-1.0.1.003.jar</p>
</blockquote></td>
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>local_policy.jar</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>log4j-app.2.10.0.jar</p>
</blockquote></td>
<td><blockquote>
<p>Log4j</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>log4j-core.2.10.0.jar</p>
</blockquote></td>
<td><blockquote>
<p>Log4j</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LongList.jar</p>
</blockquote></td>
<td><blockquote>
<p>Used by PSL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NamingDirectoryService-client.jar</p>
</blockquote></td>
<td><blockquote>
<p>Used by PSL/PSC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PatientServiceR2.jar</p>
</blockquote></td>
<td><blockquote>
<p>PSC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>pslWeb_4.0.4.3.jar</p>
</blockquote></td>
<td><blockquote>
<p>PSL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>standard.jar</p>
</blockquote></td>
<td><blockquote>
<p>JSTL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>struts.jar</p>
</blockquote></td>
<td><blockquote>
<p>Struts</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>US_export_policy.jar</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>vha-stddata-basic-18.0.jar</p>
</blockquote></td>
<td><blockquote>
<p>SDS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>vha-stddata-client-18.0.jar</p>
</blockquote></td>
<td><blockquote>
<p>SDS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>vha-stddata.jar</p>
</blockquote></td>
<td><blockquote>
<p>SDS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>vpfsTags.jar</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>wlclient.jar</p>
</blockquote></td>
<td><blockquote>
<p>Standard J2EE classes</p>
</blockquote></td>
</tr>
</tbody>
</table>

7.  Classes

> The class files for the VPFS web archive are located by package under the WEBINF/classes directory. The class packages are described in the following table.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Action handler (Servlet <em>controller</em>) classes called by Struts.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Business logic classes; perform non-form-based data validation, manage calls to the database access layer.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Data access objects; classes and interfaces for reading from or writing to the database.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>JSP-specific classes used by Tiles to build menu items.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>VPFS taglib, custom controls.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Common utility classes: formatters, service locators, etc.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Value object classes; basic data objects.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## HealtheVet Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS depends on the following service dependency configuration files that may need updating during deployment. Refer to the documentation for these dependencies for more information about the configuration properties. These files are currently packaged in the VPFS application enterprise archive (ear) file, however may alternatively reside in the Health*<u>e</u>*Vet common configuration location:

> ![](vpfs-version-1-2-systems-management-guide/021.png)![](vpfs-version-1-2-systems-management-guide/022.png)![](vpfs-version-1-2-systems-management-guide/023.png)![](vpfs-version-1-2-systems-management-guide/024.png)kaajeeConfig.xml – a KAAJEE configuration file (must remain in the ear file) PatientLookup.properties – a PSL configuration file PersonLookupResources.properties – a PSL configuration file PatSvcPkg.properties – a PSC configuration file

> ![](vpfs-version-1-2-systems-management-guide/025.png)These files are installed on the WebLogic server in the installation directory for the specified component: KaajeeDatabase.properties – a KAAJEE configuration file (SSPI)

> <span class="mark">REDACTED</span>vistalink.connectorConfig.xml – a VLJ configuration file

## Other Configuration Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are a number of configuration properties for VPFS in the VSYSTEM_PARAMETER table. Changes to these properties should be made with care and a full understanding of how the parameter effects the VPFS application.

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 24%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Parameter Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Default Value</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>APPLICATION_PROXY_USER</p>
</blockquote></td>
<td><blockquote>
<p>VistALink application proxy user account, required for PSC to be</p>
<p>able to connect to the</p>
</blockquote></td>
<td><blockquote>
<p>VPFS,APPLICATION PROXY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Parameter Name</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Default Value</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>VistA sites.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DB_VERSION</p>
</blockquote></td>
<td><blockquote>
<p><strong>Internal.</strong> Must match database version in web.xml.</p>
</blockquote></td>
<td><blockquote>
<p>1.0.5.001</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EMAIL_ENABLED</p>
</blockquote></td>
<td><blockquote>
<p>Set whether email notifications of override conditions are enabled. Allowed values are “true” and</p>
<p>“false”. If true, SMTP_SERVER must also be specified.</p>
</blockquote></td>
<td><blockquote>
<p>false</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATIENTUPDATE_SCHEDULE_TIME</p>
</blockquote></td>
<td><blockquote>
<p>Start time of the scheduled update process.</p>
</blockquote></td>
<td><blockquote>
<p>1:00 am</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRODUCTION_MODE</p>
</blockquote></td>
<td><blockquote>
<p><strong>Internal.</strong></p>
</blockquote></td>
<td><blockquote>
<p>true</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SMTP_SERVER</p>
</blockquote></td>
<td><blockquote>
<p>DNS hostname or IP address of the SMTP server (to send email).</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VISTALINK_ACTIVE</p>
</blockquote></td>
<td><blockquote>
<p><strong>Internal.</strong></p>
</blockquote></td>
<td><blockquote>
<p>true</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Log4j is the logging framework used in VPFS. Logging is configured via the log4j.xml configuration file located in the Health*<u>e</u>*Vet common configuration location, specified for each server using the

> -Dlog4j.configuration JVM argument. Log4j defines the concepts of “appenders” that define individual log files and the layout of log data in those files, and “loggers” that define what log types and levels are sent to the various appenders. Refer to log4j documentation for more information about the contents of this file.

> A sample log4j configuration file (log4j_sample.xml) is provided in the VPFS distribution package.

> The default log file location is the log directory. This directory is created under the Node Manager root when running on a managed server (e.g. /u0*n*/app/bea/weblogic81/common/nodemanager/log/). When running on an admin server (not recommended for production environments!), this directory is created under the domain root (e.g. /u0*n*/app/bea/user_projects/domains/domVpfs/log/).

### Application Server Log File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> WebLogic creates various log files for each admin or managed server started. Log4j can be configured to write to these files by sending log to the Console appender. The location and name of these log files is dependent on the type of server:

> Managed Servers – There are 2 log files created for each managed server. These files are located in a NodeManagerLogs/*\<domain-name\>*\_*\<server_name\>* directory under the Node Manager root.

> ![](vpfs-version-1-2-systems-management-guide/026.png)Administration Server – The admin server log is *\<server-name\>*.log, located in the domain root directory.

> The application server log is configured as the root logger in the default VPFS log4j configuration, meaning any uncaught exceptions or errors will be written to this log.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 16%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Level</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>SDS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>SDS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>VistALink*</p>
</blockquote></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \*VistALink has its own log4j configuration file that may record VistALink log information in another location. Refer to VistALink documentation for more information.

### VPFS Log File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The default VPFS log file is vpfs.log. Any VPFS generated errors or log messages will be written to this log.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 16%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Level</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>User Interface exception handler</p>
</blockquote></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>Business layer exception handler</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>Data access exception handler</p>
</blockquote></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>General VPFS exception handler</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PSL Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are two standard log files configured for PSL: psl.log for general PSL errors or log messages, pslmetrics.log for PSL metrics.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 16%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Level</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>PSL exception handler, writes to general PSL log</p>
</blockquote></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>PSL Metrics handler, writes to metrics PSL log</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PSC Log File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The standard PSC log file is PatSvc.log. Any PSC generated errors or log messages will be written to this log.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 16%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Level</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 16%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></th>
<th><blockquote>
<p>Info</p>
</blockquote></th>
<th><blockquote>
<p>PSC exception handler</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### VistALink Log File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The standard VistALink log file is vlj.log. Any VistALink generated errors or log messages will be written to this log.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 16%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Level</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p>Info</p>
</blockquote></td>
<td><blockquote>
<p>PSC exception handler</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS internal checked exceptions are described in Javadoc:

> <span class="mark">REDACTED</span>

## Service Imports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS imports the following classes from VA services:

> Standard Data Service (SDS)

> <span class="mark">REDACTED</span>

### Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span class="mark">REDACTED</span>

### KAAJEE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span class="mark">REDACTED</span>

### VistALink for Java

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span class="mark">REDACTED</span>

> Patient Service Lookup (PSL) <span class="mark">REDACTED</span>

> Patient Service Construct (PSC) <span class="mark">REDACTED</span>

> <span class="mark">REDACTED</span>

## Source Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Source code for VPFS is available in the VPFS SourceSafe database.

## Javadoc

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Javadoc for VPFS is available in the VPFS SourceSafe database.

## Business Rules Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Application security is managed via constraints placed on the URLs that a user may access in the web.xml configuration file. Security keys assigned to users in VistA are retrieved by KAAJEE and mapped to roles by the application server. A list of VPFS security keys is available in the *VPFS User Guide* and in Section

> 4.9 of this document.

> Programmatic security is used for hiding invalid options on individual pages. The tags defined in the VPFS tag library are all role-aware. Availability is determined by checking if the user has one of the roles specified in the tag roles attribute by calling request.isUserInRole().

### Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> User transactions are used when updating the database. The JTAUtil class provides methods to begin, commit, or rollback transactions. The Business Delegate layer manages the transaction context.

> VPFS uses Oracle transactions in those stored procedures triggered by a scheduled job or trigger.

### Email Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Notifications are sent via email when a transaction override condition occurs (in TransactionBD). Email settings are configured in the Maintain System Parameters page in VPFS (EMAIL_ENABLED and

> SMTP_SERVER parameters) and the BDResources.properties file

> (WEBINF/ <span class="mark">REDACTED</span>/vpfs/biz/BDResources.properties).

### Table Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Many of the drop-down lists in VPFS are configurable via the Administration options in VPFS. The income source, form, remark, payee, and reference types are configurable at the station level, while patient status, patient type, and payment type are configurable at the national level.

### Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Electronic Signatures are used to authenticate the user when posting transactions or editing a transaction deferral date. VistA serves as the authoritative source of electronic signatures. VPFS does not store the electronic signature, but simply uses the Electronic Signature API to verify the electronic signature entered by the user. VPFS also allows the user to change their electronic signature via the Electronic Signature API.s

> Database - M VistA

# Database - M VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Prior to using the VPFS or VistAMigrate application at a given site, the site must install two KIDS builds PRPF\*3.0\*15 and PRPF\*3.0\*16 that are associated with the Patient Funds package. These KIDS builds bring in routines, options, remote procedure calls (RPCs), and security keys. No new data files are brought in with this installation, and the existing Patient Funds files, routines, options and security keys are not changed by these patch installations. See the patch descriptions for instructions on the installation and setup.

> The objective of PRPF\*3.0\*15 (Diagnostic Patch) is to allow sites to diagnose and resolve as many issues as possible before they migrate from VistA legacy Personal Funds of Patients (PFOP) to the Veterans Personal Funds System (VPFS). Install and use Diagnostic Patch 15 well in advance of your actual data migration date to allow time to run the diagnostic routine, review the reports, and make corrections in the M environment repeatedly to narrow down the count of errors.

> Migration Patch PRPF\*3.0\*16 is used during the migration of data from PFOP to VPFS. This patch includes the following Remote Procedure Calls (RPC) functionality that enables the VPFS migration application to transfer specific Patient Funds legacy data to the reengineered VPFS system. This new functionality is not added to the legacy Patient Funds menu because this functionality is intended for use as an RPC only. This RPC is invoked by VistALink from an outside migration server. Proxy User for Nightly Updates: This patch uses a post install routine PRPFMR2 that will create a proxy user account for the VPFS application to use during nightly updates with all legacy systems. The post install results create entries in the Patch 16 installation report. The patch installation report will always contain one of three possible responses from the proxy account install process:

1.  THE VPFS APPLICATION PROXY USER ACCOUNT HAS BEEN SUCCESSFULLY CREATED!

> ![](vpfs-version-1-2-systems-management-guide/027.png)The account was created and no further action is required.

2.  WARNING: THE VPFS APPLICATION PROXY USER ACCOUNT ALREADY PRESENT!!

> ![](vpfs-version-1-2-systems-management-guide/028.png)The account was already present and the reason for this should be known by IRM. If there are any questions as to why the account is already present it should be investigated.

3.  ERROR: THE VPFS APPLICATION PROXY USER ACCOUNT COULD NOT BE CREATED!!!

> ![](vpfs-version-1-2-systems-management-guide/029.png)There was a problem and IRM should be approached for a resolution and patch 16 should be re-installed.

> The purpose of patch PRPF\*3.0\*17 is to partially disable the legacy Patient Funds package. This patch is

> -ONLY- intended for installation in a VistA environment that has successfully completed the VPFS migration process for the Patient Funds package. If migration has been completed and the site is ready to DISABLE all standard user write or delete privileges to their legacy VistA Patient Funds package then proceed with installation of this patch.

> All Patient Funds options and functionality that either adds, updates, or deletes Patient Funds data will be disabled for standard VistA users (Guardian address edit will still function normally). All other Patient Funds menu options, such as reporting, will continue to function normally and it is intended that the legacy VistA Patient Funds package still remain available for historical reporting purposes indefinitely.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Routines, options, and remote procedures beginning with PRPF are used to migrate legacy data into VPFS. Routines, remote procedures and security keys beginning with PRFP are used during normal operation of the VPFS application.

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Routine Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRPF*3.0*15</p>
</blockquote></td>
<td><blockquote>
<p>PRPFDR1</p>
</blockquote></td>
<td><blockquote>
<p>This routine is used to report diagnostic information related to Patient Funds data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRPF*3.0*15</p>
</blockquote></td>
<td><blockquote>
<p>PRPFDR2</p>
</blockquote></td>
<td><blockquote>
<p>This is the main entry routine that is used to report diagnostic information related to Patient Funds data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRPF*3.0*15</p>
</blockquote></td>
<td><blockquote>
<p>PRPFDR3</p>
</blockquote></td>
<td><blockquote>
<p>This routine is used to report diagnostic information related to Patient Funds data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRPF*3.0*15</p>
</blockquote></td>
<td><blockquote>
<p>PRPFDR4</p>
</blockquote></td>
<td><blockquote>
<p>This routine is used to report diagnostic information related to Patient</p>
<p>Funds data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRPF*3.0*15</p>
</blockquote></td>
<td><blockquote>
<p>PRPFDR5</p>
</blockquote></td>
<td><blockquote>
<p>This routine is used to report diagnostic information related to Patient Funds data.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRPF*3.0*15</p>
</blockquote></td>
<td><blockquote>
<p>PRPFDR6</p>
</blockquote></td>
<td><blockquote>
<p>This routine is used to report diagnostic information related to Patient</p>
<p>Funds data.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRPF*3.0*16</p>
</blockquote></td>
<td><blockquote>
<p>PRPFMR1</p>
</blockquote></td>
<td><blockquote>
<p>This routine is used to extract and move Patient funds data to the migration server.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRPF*3.0*16</p>
</blockquote></td>
<td><blockquote>
<p>PRPFMR2</p>
</blockquote></td>
<td><blockquote>
<p>This routine is used to create the VPFS proxy user for nightly updates.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRPF*3.0*17</p>
</blockquote></td>
<td><blockquote>
<p>PRPFMR3</p>
</blockquote></td>
<td><blockquote>
<p>This routine is used to disable ADD, EDIT, or Delete privileges for all Patient Funds users.</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  <span id="_bookmark2" class="anchor"></span>*Temporary Globals*

> The ^TMP global is used to store information during the data migration process. Each time the user runs either the Data Diagnostic or the Data Migration the data contained in ^TMP is purged. If the data does not get purged, there is also a purge all at the beginning of each process to ensure that no previous data is present.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Temporary Global Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>^TMP("PRPF_DIAGX",$J,0)</p>
</blockquote></td>
<td><blockquote>
<p>Holds the purge date and the date the Diagnostic was last performed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>^TMP("PRPF_DIAGX",$J,PFSTAID,<em>error#</em></p>
</blockquote></td>
<td><blockquote>
<p>Holds each record error type on the Diag report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>^TMP("PRPF_EXTDATA",$J,0)</p>
</blockquote></td>
<td><blockquote>
<p>Holds the purge date and the date the Extraction was last performed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>^TMP("PRPF_EXTDATA",$J,1,0)</p>
</blockquote></td>
<td><blockquote>
<p>Holds the single header record that is used by VistAMigrate</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>^TMP("PRPF_EXTDATA",$J,CNTSEG,CNTREC)</p>
</blockquote></td>
<td><blockquote>
<p>Holds each data record of the extraction file</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> New options are brought in to support migration of the legacy Patient Funds data into VPFS.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
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
<p>Database Diagnostic Report [PRPF DATA DIAGNOSTIC REPORT]</p>
</blockquote></td>
<td><blockquote>
<p>Legacy Diagnostics menu option contained in Supervisors menu options.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[PRPF RPC UTILS]</p>
</blockquote></td>
<td><blockquote>
<p>Broker type option used to register VPFS Remote Procedure Calls used during the Data Migration process and control access to Diag and Extract RPC‟s.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRPF DATABASE DIAG</p>
</blockquote></td>
<td><blockquote>
<p>Broker type option used to register VPFS Remote Procedure Calls, which Data Diagnostic reports that are displayed in VistAMigrate.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>[PRPF DATABASE EXTR]</p>
</blockquote></td>
<td><blockquote>
<p>Broker type option used to register VPFS Remote Procedure Call used during Data Migration</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  <span id="_bookmark5" class="anchor"></span>*External Relations*

> KAAJEE: VPFS uses the Kernel Authentication Authorization Java Enterprise Environment, a Security service located on VistA for use by reengineered web applications, for authenticating users during sign on, and for allowing them access to various VPFS options based on roles. KAAJEE has a VistA component that must be installed in order to run VPFS. The roles-based access is controlled by the use of new security keys created for VPFS. See „Security Key‟ section below for details. The list of accessible divisions data is retrieved by KAAJEE from the DIVISION multiple on the VistA NEW PERSON file.

> VistALink: VPFS uses VistALink, a communications bridge between VistA and J2EE application Servers, to retrieve data. VistALink has a VistA component that must be installed in order to run VPFS.

> Person Services Lookup: VPFS uses Person Services Lookup service when the user needs to add a patient to VPFS. The service includes a User Interface (UI) that is incorporated within VPFS. The UI prompts for patient information, displays a list of matching patients, then when one is selected, displays any patient related warnings and additional information. The identifier for the patient is then returned to the VPFS application and stored in a local VPFS table. Person Services Lookup has a VistA component that must be installed in order to run VPFS.

> Patient Services Construct: After a patient has been selected, VPFS calls Patient Services Construct service to get patient demographics information for the patient. This information is stored on a local VPFS table to support reporting. Patient Service Construct has a VistA component that must be installed in order to run VPFS.

> Note: None of the new VistA routines, options or remote procedure calls brought in with the VPFS installation should be called by any application outside of VPFS.

## Online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VPFS options used for data migration use standard FileMan conventions for online help.

## Checksum Values for Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to the patch description for each patch for routine checksums.

## Security and Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS uses the KAAJEE security service to authenticate users during sign on and authorize access to the VPFS application based on their assigned roles. The same access and verify codes used for VistA are also used to sign on to VPFS.

> Security Keys stored in the VistA system are mapped to roles in the application server to control access to various options within the VPFS system.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Keys</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Access Level</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRPF_BASIC_OFFICIAL_USER</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to view selected patient and account information, no reporting privileges.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRPF_BASIC_PFC</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to register patients, search for patients, edit patient information, post transactions, request patient transfers.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRPF_LEAD_PFC</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to register patients, search for patients, edit patient information, post transactions, request and authorize patient transfers.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRPF_PFC_SUPER</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to register patients, search for patients, edit patient information, post transactions, request and authorize patient transfers, request application changes through Administration area.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRPF_FISCAL_MANAGEMENT</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to view selected patient and account information, no reporting privileges.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRPF_VPFS_SECURITY_ADMIN</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to view selected patient and account information for purposes of data security.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRPF_VPFS_SYSTEM_ADMIN</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to implement authorized changes to common reference data, no patient record access. <strong>This is a restricted role.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRPF_ACCOUNT_OVERDRAW</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to overdraw any patient account.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRPF_DEFERRAL_OVERRIDE</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to override deferred transactions.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRPF_RESTRICTION_OVERRIDE</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to override patient restrictions.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRPF_DATA_MIGRATION_USERS</p>
</blockquote></td>
<td><blockquote>
<p>User has the ability to migrate legacy Patient Funds data. <strong>This is a restricted role.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Database - Oracle

# Database - Oracle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VPFS persistent data is stored in Oracle tables maintained on a central server. The version at the time of VPFS initial installation is Oracle 12g.

## Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VPFS production database is located at the Falling Waters EIE.

## Schemas

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS – Owns all of the tables and procedures for the VPFS application. Also owns the data staging tables and conversion stored procedure needed for VistAMigrate.

> VISTA_MIGRATE – Owns all of the tables and procedures for the VistAMigrate application.

## Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS – Owns all of the tables and procedures for the VPFS application. All database connections from the VPFS application user interface are made as the VPFS user.

> VISTA_MIGRATE – Owns all of the tables and procedures for the VistAMigrate application. All database connections from the VistAMigrate application user interface are made as the VISTA_MIGRATE user.

## Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No roles are created for VPFS.

## Tablespaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No tablespaces are created for VPFS. (The VPFS schema can be installed into its own tablespace if one is created prior to starting installation and the VPFS user is assigned this tablespace as its default tablespace.)

## Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Tables in the VPFS Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All of the data tables used in the VPFS application are in the VPFS schema.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Table Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ACCOUNT_TRANSACTION</p>
</blockquote></td>
<td><blockquote>
<p>Patient transaction records</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FREQUENCY</p>
</blockquote></td>
<td><blockquote>
<p>System-wide list of income frequency types (daily, weekly, monthly, etc.)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GUARDIAN</p>
</blockquote></td>
<td><blockquote>
<p>Patient guardian records (VA and civil)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INCOME_SOURCE</p>
</blockquote></td>
<td><blockquote>
<p>Patient income source records</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>INCOME_SOURCE_TYPE</p>
</blockquote></td>
<td><blockquote>
<p>Institution-specific list of income source types (apportionee, guardian, institutional award, etc.)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATIENT_ACCOUNT</p>
</blockquote></td>
<td><blockquote>
<p>Patient account records</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 37%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="23"></th>
<th><blockquote>
<p><strong>Table Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PATIENT_EVENT_LOG</p>
</blockquote></th>
<th><blockquote>
<p>Patient event log records</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PATIENT_FUNDS_FORM</p>
</blockquote></th>
<th><blockquote>
<p>Institution-specific list of form types</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PATIENT_FUNDS_REMARK</p>
</blockquote></th>
<th><blockquote>
<p>Institution-specific list of remark types, when posting transactions</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PATIENT_STATUS</p>
</blockquote></th>
<th><blockquote>
<p>System-wide list of patient status types (competent, etc.)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PATIENT_TRANSFER</p>
</blockquote></th>
<th><blockquote>
<p>Pending patient transfer details</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PATIENT_TYPE</p>
</blockquote></th>
<th><blockquote>
<p>System-wide list of patient types (restricted, limited restricted, unrestricted, unknown)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PAYEE_TYPE</p>
</blockquote></th>
<th><blockquote>
<p>Institution-specific list of payee types</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PAYMENT_TYPE</p>
</blockquote></th>
<th><blockquote>
<p>System-wide list of payment types (check/cash/other)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PERSON</p>
</blockquote></th>
<th><blockquote>
<p>Person identity records</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>REFERENCE_TYPE</p>
</blockquote></th>
<th><blockquote>
<p>Institution-specific list of transaction reference types (ACP, PFO, etc.)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>STANDARD_INCOME_ SOURCE_TYPE</p>
</blockquote></th>
<th><blockquote>
<p>Standard list of income source types, available at every institution</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>STANDARD_PATIENT_ FUNDS_FORM</p>
</blockquote></th>
<th><blockquote>
<p>Standard list of form types, available at every institution</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>STANDARD_PATIENT_ FUNDS_REMARK</p>
</blockquote></th>
<th><blockquote>
<p>Standard list of remark types, when posting transactions, available at every institution</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>STANDARD_PAYEE_TYPE</p>
</blockquote></th>
<th><blockquote>
<p>Standard list of payee types, available at every institution</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>STANDARD_REFERENCE_TYPE</p>
</blockquote></th>
<th><blockquote>
<p>Standard list of reference types, available at every institution</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SUSPENSE</p>
</blockquote></th>
<th><blockquote>
<p>Patient suspense item records</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SYSTEM_ERROR_LOG</p>
</blockquote></th>
<th><blockquote>
<p>Error log available for use via log4j appender</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>USER_INSTITUTION</p>
</blockquote></th>
<th><blockquote>
<p>Cache for default child institution for application user</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>VPAGE</p>
</blockquote></th>
<th><blockquote>
<p>System table; list of individual application pages</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>VPAGE_FIELD</p>
</blockquote></th>
<th><blockquote>
<p>System table; page and field level help text</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>VPFS_INSTITUTION</p>
</blockquote></th>
<th><blockquote>
<p>System table; institution-specific data used by the application, including email address lists and messages for override notifications</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>VREPORT</p>
</blockquote></th>
<th><blockquote>
<p>System table; list of available reports, which roles can access them, and what parameters are available for them</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 37%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"></th>
<th><blockquote>
<p>VREPORT_PARAMETER</p>
</blockquote></th>
<th><blockquote>
<p>Deprecated</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>VSYSTEM_PARAMETER</p>
</blockquote></th>
<th><blockquote>
<p>System table; application configuration parameters</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> These tables are used by the VistAMigrate application for staging PFOP data prior to conversion. After data migration has been completed for all stations, these tables will no longer be needed.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Table Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DM_A1</p>
</blockquote></td>
<td><blockquote>
<p>Data migration header records</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DM_B1</p>
</blockquote></td>
<td><blockquote>
<p>Patient balance records (1 of 2)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DM_B2</p>
</blockquote></td>
<td><blockquote>
<p>Patient balance records (2 of 2)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DM_D1</p>
</blockquote></td>
<td><blockquote>
<p>Patient detail / demographic records (1 of 2)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DM_D2</p>
</blockquote></td>
<td><blockquote>
<p>Patient detail / demographic records (2 of 2)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DM_I1</p>
</blockquote></td>
<td><blockquote>
<p>Patient income source records</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DM_R1_R2</p>
</blockquote></td>
<td><blockquote>
<p>Patient general remarks</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DM_S123</p>
</blockquote></td>
<td><blockquote>
<p>Patient suspense items</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DM_T1</p>
</blockquote></td>
<td><blockquote>
<p>Patient deferred transactions being migrated</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DM_X1_X2</p>
</blockquote></td>
<td><blockquote>
<p>Patient special remarks</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DM_ERRORS</p>
</blockquote></td>
<td><blockquote>
<p>List of errors encountered during the Analyze step of migration</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Tables in the VISTA_MIGRATE Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All of the data tables used in the VistAMigrate application are in the VistAMigrate schema.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Table Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DM_SETUP</p>
</blockquote></td>
<td><blockquote>
<p>Project parameters, RPC names, database connection information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DM_SETUP_INSTITUTION</p>
</blockquote></td>
<td><blockquote>
<p>Migration statistics and progress status per institution</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VSYSTEM_PARAMETER</p>
</blockquote></td>
<td><blockquote>
<p>System table; application configuration parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DM_CONVERSION_EVENT_LOG</p>
</blockquote></td>
<td><blockquote>
<p>Event log for conversion step</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DM_CONVERSION_ERROR_LOG</p>
</blockquote></td>
<td><blockquote>
<p>Error log for conversion step</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Field Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IDs: The primary data tables (person, patient_account, account_transaction, suspense, income_source, guardian) have a sequential integer ID field as the primary key. This field value is automatically incremented from an Oracle sequence for that table.

> User IDs: Each table has a user_id field and last_modified_dt field to maintain the name of the user and date of the last update to the corresponding record.

## Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Views in the VPFS Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following views used by the VPFS application are owned by the VPFS schema.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>View Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td><blockquote>
<p>Pick list of the distinct wards present in the patient accounts, by institution.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INSTITUTION</p>
</blockquote></td>
<td><blockquote>
<p>Consolidated view of institution data from the SDS STD_INSTITUTION table with VPFS-specific institution data from the VPFS_INSTITUTION table.</p>
<p>The INSTITUTION view references the following SDS tables:</p>
<p>STD_INSTITUTION STD_STATE STD_COUNTRY STD_FACILITYTYPE</p>
</blockquote></td>
</tr>
</tbody>
</table>

## ![](vpfs-version-1-2-systems-management-guide/030.png)![](vpfs-version-1-2-systems-management-guide/031.png)![](vpfs-version-1-2-systems-management-guide/032.png)![](vpfs-version-1-2-systems-management-guide/033.png)Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Stored Procedures in the VPFS Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following procedures used by the VPFS application are owned by the VPFS schema.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Procedure Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>sp_deactivateAccount</p>
</blockquote></td>
<td><blockquote>
<p>Checks if an account needs to be deactivated (if there is zero balance and there are no transactions for 30 days). Scheduled to run daily.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sp_instnOrderNbrOnAfterDelete</p>
</blockquote></td>
<td><blockquote>
<p>Reorder the sequence numbers of rows in an institution-specific maintenance table AFTER the deletion of a record.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>sp_instnOrderNbrOnBeforeInsert</p>
</blockquote></td>
<td><blockquote>
<p>Reorder the sequence numbers of rows in an institution-specific maintenance table BEFORE the insert of a new record.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sp_instnOrderNbrOnBeforeUpdate</p>
</blockquote></td>
<td><blockquote>
<p>Reorder the sequence numbers of rows in an institution-specific maintenance table when updating a record.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>sp_redoOrderNbrOnAfterDelete</p>
</blockquote></td>
<td><blockquote>
<p>Reorder the sequence numbers of rows in a maintenance table AFTER the deletion of a record.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sp_redoOrderNbrOnBeforeInsert</p>
</blockquote></td>
<td><blockquote>
<p>Reorder the sequence numbers of rows in a maintenance table BEFORE the insert of a new record.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>sp_redoOrderNbrOnBeforeUpdate</p>
</blockquote></td>
<td><blockquote>
<p>Reorder the sequence numbers of rows in a</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 38%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="6"></th>
<th><blockquote>
<p><strong>Procedure Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p>maintenance table when updating a record.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>sp_updateDeferrals</p>
</blockquote></th>
<th><blockquote>
<p>Checks all deferral dates and updates the proper balances. Scheduled to run daily.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>sp_updateMonthlyRestriction</p>
</blockquote></th>
<th><blockquote>
<p>Update the actual_monthly_restriction_amt to 0. Scheduled to run monthly.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>sp_updateWeeklyRestriction</p>
</blockquote></th>
<th><blockquote>
<p>Update the actual_weekly_restriction_amt to 0. Scheduled to run weekly.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>logError</p>
</blockquote></th>
<th><blockquote>
<p>This procedure is called only by other stored procedures to log an error to the system error log table.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The following procedures are used for data migration (VistAMigrate) only.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Procedure Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>pk_convertLegacyData</p>
</blockquote></td>
<td><blockquote>
<p>Package of procedures used to convert the data in the staging tables (DM_*) for the VPFS production tables. mainVPFS is called by VistAMigrate during the Conversion step. The remaining procedures (in <em>italics</em>) are called only by mainVPFS.</p>
<p><strong>Contents</strong>: mainVPFS <em>preConversionCheck prepDates insertPerson insertPatientAccount insertIncomeSource insertAccountTransaction insertSuspense updateRunningBalance updateDeferredAvailableBalance updateGeneralRemarks updateSpecialRemarks postConversionCheck logConversionError logConversionEvent</em></p>
<p>logConversionError and logConversionEvent call the logError and logEvent procedures, respectively, in the DM_UTILS package in the VISTA_MIGRATE schema. The VPFS user must have been granted execute privileges to the DM_UTILS package in the VISTA_MIGRATE schema.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sp_vpfs_cleanup_dm</p>
</blockquote></td>
<td><blockquote>
<p>Removes data for the specified station_id from the</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 38%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="5"></th>
<th><blockquote>
<p><strong>Procedure Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p>staging tables.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>sp_vpfs_cleanup_production</p>
</blockquote></th>
<th><blockquote>
<p>Removes data for the specified station_id and the children of the specified station_id from the production tables.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>sp_vpfs_converted_count</p>
</blockquote></th>
<th><blockquote>
<p>Returns the number of converted patient accounts and the total number of converted patient records (including transactions, income sources, etc.).</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>sp_vpfs_stage_count</p>
</blockquote></th>
<th><blockquote>
<p>Returns the number of staged patient accounts and the total number of staged patient records (including transactions, income sources, etc.).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### ![](vpfs-version-1-2-systems-management-guide/034.png)Stored Procedures in the VISTA_MIGRATE Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following procedures used by the VistAMigrate application are owned by the VISTA_MIGRATE schema.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Procedure Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>pk_DM_UTILS</p>
</blockquote></td>
<td><blockquote>
<p>Package of procedures used by VistAMigrate to update various record counts and manage migration event and error logs.</p>
<p><strong>Contents</strong>: dmSetup</p>
<p>updateExtractionCount updateLoadCount updateMoveCount cleanupLogs logError logEvent</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Triggers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Triggers in the VPFS Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vpfs-version-1-2-systems-management-guide/035.png)![](vpfs-version-1-2-systems-management-guide/036.png)The following triggers are defined in the VPFS schema. These triggers provide pre- and postprocessing for deletes, inserts, or updates on data in the VPFS tables.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Trigger Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>del_standard_income_src_type</p>
</blockquote></td>
<td><blockquote>
<p>Fired when a row is deleted from the standard_income_source_type table.</p>
<p>Updates the standard_data_ind flag on rows in the income_source_type table having the same income_source_type_cd as the row being deleted</p>
<p>from the standard_income_source_type table. Allows individual stations to choose to include or</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 38%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="7"></th>
<th><blockquote>
<p><strong>Trigger Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p>not include the deleted standard income source type.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>del_standard_patient_funds_frm</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is deleted from the standard_patient_funds_form table.</p>
<p>Updates the standard_data_ind flag on rows in the patient_fund_form table having the same form_id as the row being deleted from the standard_patient_funds_form table.</p>
<p>Allows individual stations to choose to include or not include the deleted standard patient funds form type.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>del_standard_patient_funds_rmk</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is deleted from the standard_patient_funds_remark table.</p>
<p>Updates the standard_data_ind flag on rows in the patient_funds_remark table having the same rmks_cd as the row being deleted from the standard_patient_funds_remark table.</p>
<p>Allows individual stations to choose to include or not include the deleted standard remark type.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>del_standard_payee_type</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is deleted from the standard_payee_type table.</p>
<p>Updates the standard_data_ind flag on rows in the payee_type table having the same payee_type_cd as the row being deleted from the standard_payee_type table.</p>
<p>Allows individual stations to choose to include or not include the deleted standard payee type.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>del_standard_reference_type</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is deleted from the standard_reference_type table.</p>
<p>Updates the standard_data_ind flag on rows in the reference_type table having the same reference_txt as the row being deleted from the standard_reference_type table.</p>
<p>Allows individual stations to choose to include or not include the deleted standard reference type.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ins_acct_amt</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is inserted into the account_transaction table.</p>
<p>Updates the total balance, available balance, deferred balance, private source and gratuitous balances, and actual monthly and weekly restriction amounts of the patient_account associated with the transaction.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](vpfs-version-1-2-systems-management-guide/037.png)![](vpfs-version-1-2-systems-management-guide/038.png)![](vpfs-version-1-2-systems-management-guide/039.png)![](vpfs-version-1-2-systems-management-guide/040.png)![](vpfs-version-1-2-systems-management-guide/041.png)![](vpfs-version-1-2-systems-management-guide/042.png)![](vpfs-version-1-2-systems-management-guide/043.png)![](vpfs-version-1-2-systems-management-guide/044.png)![](vpfs-version-1-2-systems-management-guide/045.png)![](vpfs-version-1-2-systems-management-guide/046.png)![](vpfs-version-1-2-systems-management-guide/047.png)![](vpfs-version-1-2-systems-management-guide/048.png)![](vpfs-version-1-2-systems-management-guide/049.png)![](vpfs-version-1-2-systems-management-guide/050.png)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 38%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="9"></th>
<th><blockquote>
<p><strong>Trigger Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p>Updates the running balance in the transaction</p>
<p>Sets the account status of the patient account to active („A‟).</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ins_acct_trans</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is inserted into the account_transaction table.</p>
<p>Updates the default institution for transaction for the current user.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ins_standard_income_src_type</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is inserted into the standard_income_source_type table.</p>
<p>Adds the new standard income source type to the income source type list for each institution <em>or</em> Sets the standard_data_ind flag to „Y‟ if the income_source_type_cd already exists at the institution.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ins_standard_patient_funds_frm</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is inserted into the standard_patient_funds_form table.</p>
<p>Adds the new standard form type to the form type list for each institution <em>or</em></p>
<p>Sets the standard_data_ind flag to „Y‟ if the form_id already exists at the institution.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ins_standard_patient_funds_rmk</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is inserted into the standard_patient_funds_remark table.</p>
<p>Adds the new standard remark type to the remark type list for each institution <em>or</em></p>
<p>Sets the standard_data_ind flag to „Y‟ if the rmks_cd already exists at the institution.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ins_standard_payee_type</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is inserted into the standard_payee_type table.</p>
<p>Adds the new standard payee type to the payee type list for each institution <em>or</em></p>
<p>Sets the standard_data_ind flag to „Y‟ if the payee_type_cd already exists at the institution.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>ins_standard_reference_type</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is inserted into the standard_reference_type table.</p>
<p>Adds the new standard reference type to the reference type list for each institution <em>or</em></p>
<p>Sets the standard_data_ind flag to „Y‟ if the</p>
<p>reference_txt already exists at the institution.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>ins_suspense</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is inserted into the suspense table.</p>
<p>Updates the max suspense date</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](vpfs-version-1-2-systems-management-guide/051.png)![](vpfs-version-1-2-systems-management-guide/052.png)![](vpfs-version-1-2-systems-management-guide/053.png)![](vpfs-version-1-2-systems-management-guide/054.png)![](vpfs-version-1-2-systems-management-guide/055.png)![](vpfs-version-1-2-systems-management-guide/056.png)![](vpfs-version-1-2-systems-management-guide/057.png)![](vpfs-version-1-2-systems-management-guide/058.png)![](vpfs-version-1-2-systems-management-guide/059.png)![](vpfs-version-1-2-systems-management-guide/060.png)![](vpfs-version-1-2-systems-management-guide/061.png)![](vpfs-version-1-2-systems-management-guide/062.png)![](vpfs-version-1-2-systems-management-guide/063.png)![](vpfs-version-1-2-systems-management-guide/064.png)![](vpfs-version-1-2-systems-management-guide/065.png)![](vpfs-version-1-2-systems-management-guide/066.png)![](vpfs-version-1-2-systems-management-guide/067.png)![](vpfs-version-1-2-systems-management-guide/068.png)![](vpfs-version-1-2-systems-management-guide/069.png)![](vpfs-version-1-2-systems-management-guide/070.png)![](vpfs-version-1-2-systems-management-guide/071.png)

> ![](vpfs-version-1-2-systems-management-guide/072.png)![](vpfs-version-1-2-systems-management-guide/073.png)![](vpfs-version-1-2-systems-management-guide/074.png)![](vpfs-version-1-2-systems-management-guide/075.png)![](vpfs-version-1-2-systems-management-guide/076.png)![](vpfs-version-1-2-systems-management-guide/077.png)![](vpfs-version-1-2-systems-management-guide/078.png)![](vpfs-version-1-2-systems-management-guide/079.png)![](vpfs-version-1-2-systems-management-guide/080.png)![](vpfs-version-1-2-systems-management-guide/081.png)![](vpfs-version-1-2-systems-management-guide/082.png)![](vpfs-version-1-2-systems-management-guide/083.png)![](vpfs-version-1-2-systems-management-guide/084.png)![](vpfs-version-1-2-systems-management-guide/085.png)![](vpfs-version-1-2-systems-management-guide/086.png)![](vpfs-version-1-2-systems-management-guide/087.png)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Trigger Name</strong></p>
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
<p>(max_suspense_dt) for the patient account associated with the suspense item.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ins_upd_acct_trans</p>
</blockquote></td>
<td><blockquote>
<p>Fired when a row is inserted or updated in the account_transaction table.</p>
<p>Updates the last transaction date (last_trans_entered_dt) and last activity date (last_activity_dt) for the patient account associated with the transaction.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ins_upd_pat_acct</p>
</blockquote></td>
<td><blockquote>
<p>Fired when a row is inserted or updated in the patient_account table.</p>
<p>Updates the patient account station_cd to ensure consistency with the current instn_id by crossreferencing the institution view (which references the SDS std_institution table).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>upd_deferral_dt</p>
</blockquote></td>
<td><blockquote>
<p>Fired when the deferral_dt is changed in an account_transaction record.</p>
<p>Updates the available and deferred balances for the patient account associated with the transaction based on the old and new deferral dates.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>upd_director_payee_ind</p>
</blockquote></td>
<td><blockquote>
<p>Fired when the director_payee_ind is changed in a guardian record.</p>
<p>Updates the (internal) director_payee_exists_ind indicator in patient_account.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>upd_patient_instn</p>
</blockquote></td>
<td><blockquote>
<p>Fired when the instn_id is changed in a patient_account record.</p>
<p>Adds an entry to the patient event log when the patient is assigned to a different institution.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>upd_patient_status</p>
</blockquote></td>
<td><blockquote>
<p>Fired when the patient_status_cd is changed in a patient_account record.</p>
<p>Adds an entry to the patient event log when the patient status is changed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>upd_patient_type</p>
</blockquote></td>
<td><blockquote>
<p>Fired when the patient_type_cd is changed in a patient_account record.</p>
<p>Adds an entry to the patient event log when the patient type is changed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>upd_standard_income_src_type</p>
</blockquote></td>
<td><blockquote>
<p>Fired when a row is updated in the</p>
<p>standard_income_source_type table. Updates the data for rows in the patient_funds_form table having the same income_source_type_cd as the row being updated.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 38%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="7"></th>
<th><blockquote>
<p>upd_standard_patient_funds_frm</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is updated in the</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><strong>Trigger Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th></th>
<th><blockquote>
<p>standard_patient_funds_form table. Updates the data for rows in the patient_funds_form table having the same form_id as the row being updated.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>upd_standard_patient_funds_rmk</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is updated in the</p>
<p>standard_patient_funds_remark table. Updates the data for rows in the patient_funds_remark table having the same rmks_cd as the row being updated.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>upd_standard_payee_type</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is updated in the standard_payee_type table.</p>
<p>Updates the data for rows in the patient_funds_remark table having the same payee_type_cd as the row being updated.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>upd_standard_reference_type</p>
</blockquote></th>
<th><blockquote>
<p>Fired when a row is updated in the standard_reference_type table.</p>
<p>Updates the data for rows in the patient_funds_remark table having the same reference_txt as the row being updated.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>upd_ward_nm</p>
</blockquote></th>
<th><blockquote>
<p>Fired when the ward_nm is changed in a patient_account record.</p>
<p>Adds an entry to the patient event log when the patient ward is changed.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## ![](vpfs-version-1-2-systems-management-guide/088.png)![](vpfs-version-1-2-systems-management-guide/089.png)![](vpfs-version-1-2-systems-management-guide/090.png)![](vpfs-version-1-2-systems-management-guide/091.png)![](vpfs-version-1-2-systems-management-guide/092.png)![](vpfs-version-1-2-systems-management-guide/093.png)![](vpfs-version-1-2-systems-management-guide/094.png)![](vpfs-version-1-2-systems-management-guide/095.png)![](vpfs-version-1-2-systems-management-guide/096.png)![](vpfs-version-1-2-systems-management-guide/097.png)Scheduled Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Jobs in the VPFS Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following scheduled jobs are defined in the VPFS schema.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 40%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Job Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Schedule</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>sp_deactivateAccount</p>
</blockquote></td>
<td><blockquote>
<p>Checks if an account needs to be deactivated (if there is zero balance and there are no transactions for 30 days).</p>
</blockquote></td>
<td><blockquote>
<p>Daily, at 2:00 AM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sp_updateDeferrals</p>
</blockquote></td>
<td><blockquote>
<p>Checks all deferral dates and updates the proper balances.</p>
</blockquote></td>
<td><blockquote>
<p>Daily, at 2:00 AM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>sp_updateMonthlyRestriction</p>
</blockquote></td>
<td><blockquote>
<p>Update the patient_account actual_monthly_restriction_amt to 0.</p>
</blockquote></td>
<td><blockquote>
<p>Monthly, on the 1<sup>st</sup> of the month</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>sp_updateWeeklyRestriction</p>
</blockquote></td>
<td><blockquote>
<p>Update the patient_account actual_weekly_restriction_amt to 0.</p>
</blockquote></td>
<td><blockquote>
<p>Weekly, Sunday morning at midnight</p>
</blockquote></td>
</tr>
</tbody>
</table>

## External Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS requires that the following dependencies be installed in the VPFS Oracle database.

### Standard Data Service (SDS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS has subscribed to the SDS group to load their standard data tables into the SDSADM schema on the VPFS Oracle database. The data will be automatically refreshed by the SDS application. VPFS uses supported SDS APIs to extract data from the tables as needed.

> The INSTITUTION view in the VPFS schema references the std_institution, std_state, std_country and std_facilitytype tables. This view is used throughout the application.

## Locking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VPFS application uses optimistic locking, meaning for most cases, “last in wins”. If, for example, you have two users accessing the same patient (“A”), and they both attempt to update the same value

> (“Type”) at the same time, the updates will be processed in the order received, so the user whose update is processed *last* will see their value as the new value.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>(1)</strong> Page displayed: Type is “U”</p>
</blockquote></th>
<th><blockquote>
<p><strong>(2)</strong> User 1 changes Type to “L”</p>
</blockquote></th>
<th><blockquote>
<p><strong>(3)</strong> User 2 changes Type to “R”</p>
</blockquote></th>
<th><blockquote>
<p><strong>(4)</strong> Page redisplayed: Type is “R”</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>User 1</p>
</blockquote></td>
<td>“U”</td>
<td>“L”</td>
<td><blockquote>
<p>“L”</p>
</blockquote></td>
<td>“R”</td>
</tr>
<tr class="even">
<td><blockquote>
<p>User 2</p>
</blockquote></td>
<td>“U”</td>
<td>“U”</td>
<td><blockquote>
<p>“R”</p>
</blockquote></td>
<td>“R”</td>
</tr>
</tbody>
</table>

> ![](vpfs-version-1-2-systems-management-guide/098.png)TIME

> In this case, User 2‟s update was processed last, so when the page is redisplayed, both users will see User 2‟s update.

> When posting a patient funds transaction, however, the database transaction must be controlled more carefully. To make sure the account cannot be overdrawn if two users were to attempt to post transactions for the same patient at the same time (without requiring authorization from the user), the account balance is checked just prior to inserting the transaction in the database, using same database transaction. This ensures that the balance has not changed between the time the balance was initially read and when the balance is updated after posting the transaction.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>(1)</strong> Page displayed: Balance $100</p>
</blockquote></th>
<th><blockquote>
<p><strong>(2)</strong> User 1 withdraws</p>
<p>$75</p>
</blockquote></th>
<th><blockquote>
<p><strong>(3)</strong> User 2 withdraws</p>
<p>$50</p>
</blockquote></th>
<th><blockquote>
<p><strong>(4)</strong> Page redisplayed: Balance $25</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>User 1</p>
</blockquote></td>
<td><blockquote>
<p>$100</p>
</blockquote></td>
<td>$25</td>
<td><blockquote>
<p>$25</p>
</blockquote></td>
<td><blockquote>
<p>$25</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>User 2</p>
</blockquote></td>
<td><blockquote>
<p>$100</p>
</blockquote></td>
<td>$100</td>
<td><blockquote>
<p>Error: Overdrawal</p>
</blockquote></td>
<td><blockquote>
<p>$25</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](vpfs-version-1-2-systems-management-guide/099.png)TIME

> In this case, User 2 sees an overdrawal error (step 3) because when the balance is re-read prior to posting the transaction, User 1‟s transaction has already posted (step 2), reducing the actual balance to \$25, therefore there are no longer sufficient funds to process User 2‟s transaction

> Integration Agreements

# Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Integration Agreements for Health*<u>e</u>*Vet dependency services are still being developed. Those that have been made available are listed in this section.

### Supported

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 4851 – KAAJEE – VPFS consumes the KAAJEE service to manage authentication and authorization controls. Interaction with this service occurs via documented objects and APIs.

> 4955 – Electronic Signature – VPFS consumes the Electronic Signature (ESig) service to handle Electronic Signature verification and updating. Interaction with this service occurs via documented objects and APIs.

### Controlled Subscription

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable at this time.

### Private

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 4949 – Standard Data Service – VPFS consumes the Standard Data Service (SDS) to retrieve institution data. Interaction with this service occurs via documented objects and APIs. This agreement also documents the use of a read-only database view in the VPFS schema that incorporates the following tables owned by SDS: std_institution, std_facilitytype, std_state, and std_country.

> 4951 – Person Service Lookup – VPFS consumes the Person Service Lookup (PSL) service to manage patient and provider lookups from VistA. Interaction with this service occurs via documented objects and APIs.

> 4952 – Person Service Construct – VPFS consumes the Person Service Construct (PSC) service to retrieve patient demographic data from VistA. Interaction with this service occurs via documented objects and APIs.

> 4974 – VistALink (Java API) – VPFS consumes the VistALink service as required by the Person Service Lookup, Person Service Construct, Electronic Signature, and KAAJEE services.

> VistAMigrate consumes the VistALink service to execute the M Diagnostic and M Extract RPCs as part of the migration process. Interaction with this service occurs via documented objects and APIs.

# Patient Demographics Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS stores some patient demographic data to facilitate user and reporting needs. However, VPFS does not “own” this data and is not the authoritative source of patient demographic data. Therefore, a couple processes were developed to ensure the patient demographic data stored remains current by retrieving that data from the owning VistA site.

## Data Updated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following patient demographic data is updated by the patient update process: Identity – name, SSN, ICN, DFN/IEN, date of birth

> ![](vpfs-version-1-2-systems-management-guide/100.png)Address\* – main and temporary patient addresses Primary Demographics – gender, date of death

> ![](vpfs-version-1-2-systems-management-guide/101.png)ADT – admission and discharge dates, ward, room/bed

> ![](vpfs-version-1-2-systems-management-guide/102.png)![](vpfs-version-1-2-systems-management-guide/103.png)Eligibility Information – service connected percent, claim number, person type, veteran status Incompetence Information\* – date ruled incompetent, VA and civil guardian name and addresses

> This data is in the PERSON, PATIENT_ACCOUNT, and GUARDIAN tables. Refer to Appendix A for more detail.

> \* This information is only updated on-demand. It is not updated during the scheduled update.

## On-demand Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Whenever a patient is selected in the VPFS application from the Select Patient page, or by using the Next/Previous buttons available from any Patient tab page, the patient demographic data for the selected patient, including address and incompetence information, is updated from the owning VistA site using the Patient Service (PSC).

> The patient update process starts by getting the ICN of the selected patient. The PSC retrievePatientData method is used to retrieve the patient data for the patient with the specified ICN. If a patient with the specified ICN could not be found, the lookup is repeated using the patient DFN. If the patient still could not be found, an error results, otherwise the patient data is updated in the VPFS database.

## Scheduled Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A Scheduled Patient Update process is started when the application is started on the application server. This process handles updating the patient demographic data for patients registered in VPFS. Address and incompetence information is not updated during the scheduled patient update process. This information is updated on-demand.

> Patient demographics for *active* patients are updated daily.

> Patient demographics for *inactive, non-deceased* patients are updated weekly (over the weekend).

> Patient demographics for *inactive, deceased* patients are only updated on-demand when their account is selected by a user in VPFS.

> The following parameters are used to configure the update process. These parameters can be modified via the Maintain System Parameters page in VPFS.

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 24%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Parameter Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Default Value</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PATIENTUPDATE_SCHEDULE_TIME</p>
</blockquote></td>
<td><blockquote>
<p>Start time of the scheduled update process.</p>
</blockquote></td>
<td><blockquote>
<p>1:00 am</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>APPLICATION_PROXY_USER</p>
</blockquote></td>
<td><blockquote>
<p>VistALink application proxy user account, required for PSC to be able to connect to the VistA sites.</p>
</blockquote></td>
<td><blockquote>
<p>VPFS,APPLICATION PROXY</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note: The application proxy user name must exist on every VistA site VPFS will connect to in order to update patient demographic data at that site.

> The scheduled patient update process is a batch version of the on-demand update that runs in a separate timer thread that is scheduled when VPFS is started in the application server. This process can take a significant amount of time due to the amount of data being processed.

> The process starts by retrieving a list of station numbers of patients present in the VPFS database. For

> each station, the ICNs of patients at that station are retrieved. These are then “chunked” into 1000 patient batches and passed to the PSC retrieveMultiplePatients method. Any patient not found via ICN lookup will be processed singly (using the on-demand update process) using their DFN. An error message will be written to the VPFS log file for any patient that could not be found or updated.

> Because the scheduled patient update process is executed outside of an active user session, an application proxy user account is used. The same application proxy user account name must be present in the VistA database for every station. This account is created automatically during the installation of PRPF\*3.0\*16.

> Data Migration

# Data Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VPFS Data Migration process is documented in the *VistAMigrate Data Migration Guide*.

## Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistAMigrate configuration is documented in the *VPFS Installation Guide*.

> The following parameters are configurable for the VPFS project in VistAMigrate.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 23%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Location</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Parameter Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>DM_SETUP</p>
</blockquote></td>
<td><blockquote>
<p>DB_USER_NM</p>
</blockquote></td>
<td><blockquote>
<p>VPFS database username (user with read/write access to the VPFS schema, e.g. VPFS)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DM_SETUP</p>
</blockquote></td>
<td><blockquote>
<p>DB_USER_PASS_TXT</p>
</blockquote></td>
<td><blockquote>
<p>VPFS database password (password for the user specified in DB_USER_NM)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DM_SETUP</p>
</blockquote></td>
<td><blockquote>
<p>DB_DATA_SRC_TXT</p>
</blockquote></td>
<td><blockquote>
<p>TNS name defined on the application server for the VPFS database (user/password@<strong>tnsname</strong> when using SQL*Plus).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistAMigrateResources.properties (in WEB-INF/classes)</p>
</blockquote></td>
<td><blockquote>
<p>migrationRootPath</p>
</blockquote></td>
<td><blockquote>
<p>Path to the VistAMigrate root path (directory containing the VPFS/CODE directory, e.g.</p>
<p>/path/to/vistamigrateroot).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>setenv (in VistAMigrate root VPFS/CODE directory)</p>
</blockquote></td>
<td><blockquote>
<p>VM_ORACLE_HOME</p>
</blockquote></td>
<td><blockquote>
<p>Path to the Oracle installation root path (directory containing the bin directory, e.g.</p>
<p>/path/to/oracle/product/10.2.0/client_1).</p>
</blockquote></td>
</tr>
</tbody>
</table>

# VPFS Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Component</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KAAJEE</strong></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p><strong>Refer to the KAAJEE Deployment Guide for additional information about these KAAJEE related errors or for a loginrelated error not listed here.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>KAAJEE</p>
</blockquote></th>
<th><blockquote>
<p><strong>Error: Not a valid ACCESS CODE/VERIFY CODE pair</strong></p>
</blockquote></th>
<th><blockquote>
<p>The user has entered an incorrect access and/or verify code or does not have access to the selected VistA M Server.</p>
</blockquote></th>
<th><blockquote>
<p>The user should re-enter their access and verify codes.</p>
<p>If the error persists, the user <em>must</em> contact IRM or the System Administrator to verify that they are allowed access to the VistA M Server account in question and have been granted appropriate access.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
<td><blockquote>
<p><strong>Error: Your verify code has expired or needs changing</strong></p>
</blockquote></td>
<td><blockquote>
<p>The user's verify code has expired or the user has been given a temporary verify code because they are new to the VistA M Server or asked IRM to give them new access. Upon their first login, this temporary Verify code expires immediately and <em>must</em> be changed.</p>
</blockquote></td>
<td><blockquote>
<p>KAAJEE-enabled Web-based applications do <em>not</em> support changing the user‟s verify code at this time, users <em>must</em> use another <em>non</em>-KAAJEE-based application to change their Verify code.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
<td><blockquote>
<p><strong>Error: Institution/division you selected for login is not valid for your M user account</strong></p>
</blockquote></td>
<td><blockquote>
<p>The user does not have the selected Institution/Division entry in the DIVISION Multiple field (#16) in the NEW PERSON file (#200) entry.</p>
</blockquote></td>
<td><blockquote>
<p>The user <em>must</em> contact IRM or the System Administrator to verify that they are allowed access to the Institution/Division in question and have been granted appropriate access.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Component</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
<td><blockquote>
<p><strong>Error: Forms authentication login failed</strong></p>
</blockquote></td>
<td><blockquote>
<p>The user's account does not have the necessary VistA M Server J2EE Security Keys required to access the requested page.</p>
</blockquote></td>
<td><blockquote>
<p>Get the necessary VistA M Server J2EE Security Keys assigned.</p>
<p><strong>VistAMigrate Keys:</strong></p>
<p>PRPF_DATA_MIGRATION_USER</p>
<p><strong>VPFS Keys:</strong> PRPF_BASIC_OFFICIAL_USER PRPF_BASIC_PFC PRPF_LEAD_PFC PRPF_PFC_SUPER PRPF_FISCAL_MANAGEMENT PRPF_VPFS_SYSTEM_ADMIN PRPF_VPFS_SECURITY_ADMIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
<td><blockquote>
<p><strong>Error: Login failed due to too many invalid logon attempts</strong></p>
</blockquote></td>
<td><blockquote>
<p>The user has exceeded the allowed number of login attempts to the VistA M Server and <em>must</em> wait a prescribed period of time before attempting another login.</p>
</blockquote></td>
<td><blockquote>
<p>If after the prescribed wait period has passed and the user tries to log back into the VistA M Server, and again fails in the attempt, the user <em>must</em> contact IRM or the System Administrator for assistance.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
<td><blockquote>
<p><strong>Error: Logins are disabled on the M system</strong></p>
</blockquote></td>
<td><blockquote>
<p>IRM or the System Administrator has disabled logins on the VistA M Server. Logins are sometimes disabled in order to install new software or perform system maintenance.</p>
</blockquote></td>
<td><blockquote>
<p>The user should wait and try to log into the VistA M Server at a later time. If the user feels the time period to log back into the system is excessive, the user should contact IRM or the System Administrator for assistance.</p>
</blockquote></td>
</tr>
</tbody>
</table>

![](vpfs-version-1-2-systems-management-guide/104.png)![](vpfs-version-1-2-systems-management-guide/105.png)![](vpfs-version-1-2-systems-management-guide/106.png)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Component</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
<td><blockquote>
<p><strong>Error: Could not get a connection from connector pool</strong></p>
</blockquote></td>
<td><blockquote>
<p>No VistALink connector is configured for the Station Number selected or the VistA M Server to which the connector is connecting is down.</p>
</blockquote></td>
<td><blockquote>
<p>Contact the Systems Administrator for assistance. Check that a VistALink connector is deployed for the specified Station Number and that the VistA M Server is available.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VPFS</strong></p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p><strong>System Error</strong></p>
</blockquote></td>
<td><blockquote>
<p>An unexpected error occurred.</p>
<p>The most common causes for this error include:</p>
<p>System configuration problem.</p>
<p>VPFS Oracle database is unavailable.</p>
<p>VistA M Server is unavailable.</p>
</blockquote></td>
<td><blockquote>
<p>Contact the Systems Administrator for assistance.</p>
<p>Check the application log file for error details.</p>
<p>Refer to the Logging section of this document for additional information about how errors are logged.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p><strong>The application encountered a general VPFS Exception.</strong></p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p>An unexpected error occurred.</p>
<p>These errors are truly exceptional conditions that generally point to a defect in the application.</p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p>Contact the Systems Administrator for assistance.</p>
<p>Check the application log file for error details.</p>
<p>Refer to the Logging section of this document for additional information about how errors are logged.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>The application encountered a Business Delegate Code Exception.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p><strong>The application encountered a VPFS System Exception.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>The application encountered a Security Exception.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

![](vpfs-version-1-2-systems-management-guide/107.png)![](vpfs-version-1-2-systems-management-guide/108.png)![](vpfs-version-1-2-systems-management-guide/109.png)![](vpfs-version-1-2-systems-management-guide/110.png)![](vpfs-version-1-2-systems-management-guide/111.png)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>The application encountered a JSP Tag Exception.</strong></p>
</blockquote></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th></th>
<th><blockquote>
<p><strong>The application encountered a Service Locator Exception.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Component</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>The application encountered a Database Exception.</strong></p>
</blockquote></td>
<td><blockquote>
<p>Possible causes include:</p>
<p>VPFS Oracle database is unavailable</p>
<p>Key violation (duplicate, foreign)</p>
</blockquote></td>
<td><blockquote>
<p>Contact the Systems Administrator for assistance.</p>
<p>Check the application log file for error details.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p><strong>Foreign Key Exception</strong></p>
</blockquote></td>
<td><blockquote>
<p>Foreign Key Exception when starting VPFS after logging in.</p>
</blockquote></td>
<td><blockquote>
<p>The station number the user is attempting to log into exists in the SDS institution table but does not exist in the vpfs_institution table.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p><strong>The demographics information for this patient could not be updated. {x} Please notify the system administrator of this problem.</strong></p>
</blockquote></td>
<td><blockquote>
<p>Possible causes include:</p>
<p>Patient SSN has changed</p>
<p>Patient IEN has changed</p>
<p>Patient Name has been set to blank.</p>
</blockquote></td>
<td><blockquote>
<p>To maintain integrity of the patient data, the patient SSN and IEN cannot be changed as part of the demographic update.</p>
<p>If the SSN or IEN need to be changed, contact the DBA for assistance.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p><strong>There is a discrepancy between the computed and stored balances for patient {x}.</strong></p>
</blockquote></td>
<td><blockquote>
<p>The patient account balance does not reconcile with the transaction data for that patient.</p>
<p>This is a major problem that indicates the stored balance(s) on the patient account may have been changed or one or more transactions may have been deleted.</p>
</blockquote></td>
<td><blockquote>
<p>Review the patient account. The cause for the discrepancy must be accounted for and the balance or transactions must be corrected.</p>
<p>Any changes to the patient account balances would need to be made by the DBA and logged for auditing purposes.</p>
</blockquote></td>
</tr>
</tbody>
</table>

![](vpfs-version-1-2-systems-management-guide/112.png)![](vpfs-version-1-2-systems-management-guide/113.png)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>VPFS</p>
</blockquote></th>
<th><blockquote>
<p><strong>There is a problem verifying the integrity of the transactions for patient {x}.</strong></p>
</blockquote></th>
<th><blockquote>
<p>The transaction checksum could not be verified; transaction data has been modified.</p>
<p>This is a major problem that indicates the transaction data may have been changed.</p>
</blockquote></th>
<th><blockquote>
<p>Review the patient account. The cause for the discrepancy must be accounted for.</p>
<p>Any changes to the patient account or transactions would need to be made by the DBA and logged for auditing purposes.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Component</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p><strong>The application encounted a problem sending email. Please contact your System Administrator. {x}</strong></p>
</blockquote></td>
<td><blockquote>
<p>This exception can occur when posting transactions that have caused an overdrawal, or overridden a restriction or deferral.</p>
<p>Possible causes include:</p>
<p>The SMTP server has not been configured correctly or is unavailable.</p>
<p>No recipients have been listed for the current institution.</p>
</blockquote></td>
<td><blockquote>
<p>Have the VPFS System Administrator check the SMTP_SERVER property in the Maintain System Parameters page. Ensure the server is correct and available.</p>
<p>Check the list of recipients for the current institution in the Maintain Institutions page. If no recipients have been specified, determine who should receive override messages and add their complete email address to this list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p><strong>A patient with this ICN or SSN is already registered in VPFS at station</strong></p>
<p><strong>{x}.</strong></p>
</blockquote></td>
<td><blockquote>
<p>VPFS does not allow a patient to be registered at multiple stations.</p>
<p>VA policy states that a patient may have only one patient funds account. However, PFOP, which is installed at each site, has no way of knowing if a patient has a patient funds account at another site.</p>
<p>VPFS, being a centralized application, can determine what the “owning station” is for the patient funds account.</p>
</blockquote></td>
<td><blockquote>
<p>If the patient is currently registered in VPFS and has been assigned to a station that is not the “owning station”, contact the PFC at the station the patient is currently assigned to. That PFC can change the station the patient is assigned to via the Station list on the Patient tab.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>VPFS</p>
</blockquote></th>
<th><blockquote>
<p><strong>This patient has a pending transfer request by {x} at station {x}.</strong></p>
</blockquote></th>
<th><blockquote>
<p>The user requested the transfer of a patient that has a pending transfer request.</p>
</blockquote></th>
<th><blockquote>
<p>There can only be one pending transfer request for a patient at a time. If the user would like to transfer a patient that has a pending transfer request, they need to wait for that transfer to be completed or cancelled. They can contact the PFC at the station responsible for completing the outstanding request.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Component</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p><strong>You have not been authorized to access this patient. Contact the Patient Funds department at station</strong></p>
<p><strong>{x}.</strong></p>
</blockquote></td>
<td><blockquote>
<p>The user clicked the View Patient button on the Request Transfer page, however the transfer has not yet been authorized by</p>
<p>the station the patient is currently assigned to.</p>
</blockquote></td>
<td><blockquote>
<p>Contact the PFC at the station that the patient is being requested to transfer <em>from</em> to have them authorize the transfer. Once they have authorized the transfer, the requestor will be able to click the View Patient button.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VistAMigrate Troubleshooting

# VistAMigrate Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Component</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KAAJEE</strong></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p><strong>Possible KAAJEE errors are the same as in VPFS.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VistAMigrate</strong></p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistAMigrate</p>
</blockquote></td>
<td><blockquote>
<p><strong>The M Diagnostic or M Extract step fails, the step number is in a red circle.</strong></p>
</blockquote></td>
<td><blockquote>
<p>The migration root path is not set correctly or the WebLogic server does not have write permissions to that directory.</p>
<p>The user account for the current user has not been completely set up and may not have the appropriate security keys or menu options to run VistAMigrate.</p>
</blockquote></td>
<td><blockquote>
<p>Review the VPFS Installation Guide to ensure VistAMigrate has been completely set up. Ensure the WebLogic server migration root path has write privileges.</p>
<p>Check that the user account has the PRPF RPC UTIL secondary menu option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistAMigrate</p>
</blockquote></td>
<td><blockquote>
<p><strong>The Stage Data step fails, the step number is in a red circle.</strong></p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>The migration root path is not set correctly</p>
<p>The database username, password, or data source (TNS) name are not set correctly The Oracle home path is not set correctly.</p>
<p>The weblogic user does not have permissions to execute the Oracle client tools (sqlldr, sqlplus).</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Ensure that all paths and database connection information are set correctly and the weblogic user has execute permissions on the Oracle client tools.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistAMigrate</p>
</blockquote></td>
<td><blockquote>
<p><strong>The Analyze Data step fails, the step number is in a red circle.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Component</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Message</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cause</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VistAMigrate</p>
</blockquote></td>
<td><blockquote>
<p><strong>The Convert Data step fails, the step number is in a red circle.</strong></p>
</blockquote></td>
<td><blockquote>
<p>Check the number of D1 records, the number of B1 records, and the number of patients in the A1 (header) record are not equal</p>
</blockquote></td>
<td><blockquote>
<p>Check the Stage Data log. If any D1 records were dropped, the data that caused the record to be dropped must be corrected.</p>
<p>Typical causes for a D1 record to be dropped include control characters (carriage return or line feed) or field value too long.</p>
<p>Also check for dropped B1 records, however this condition should be caught in the Analyze Data step and cause the patient not to be migrated.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark43" class="anchor"></span>Appendix A Patient Data Field Mapping

> The following table maps where patient data retrieved from VistA via PSC is updated in the VPFS database.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 16%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="3"><blockquote>
<p><strong>PSC Field(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Database Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="5"><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/114.png)</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>full name</p>
</blockquote></td>
<td><blockquote>
<p>person.full_nm, patient_account.patient_full_nm, patient_account.patient_upper_last_nm</p>
<p>patient_account.patient_cd (partial)</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>DOB</p>
</blockquote></td>
<td><blockquote>
<p>patient_account.birth_dt</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>IEN / DFN</p>
</blockquote></td>
<td><blockquote>
<p>person.ien_id patient_account.ien_id</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>ICN</p>
</blockquote></td>
<td><blockquote>
<p>person.icn patient_account.icn</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>person.ssn_nbr patient_account.patient_cd (partial)</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5"><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/115.png)</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p><em>Main Address</em></p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>patient_account:</p>
<p>addrs_one_txt, addrs_two_txt, addrs_three_txt, city_nm, postal_cd, zip_prefix_nbr, home_phone_nbr, work_phone_nbr</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>addressOne addressTwo addressThree</p>
</blockquote></td>
<td><blockquote>
<p>city state zip</p>
</blockquote></td>
<td><blockquote>
<p>homePhone workPhone</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p><em>VA Guardian Address</em></p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>guardian:</p>
<p>addrs_one_txt, addrs_two_txt, addrs_three_txt, city_nm, postal_cd, zip_prefix_nbr, home_phone_nbr, work_phone_nbr</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>addressOne addressTwo addressThree</p>
</blockquote></td>
<td><blockquote>
<p>city state zip</p>
</blockquote></td>
<td><blockquote>
<p>homePhone workPhone</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p><em>Civil Guardian Address</em></p>
</blockquote></td>
<td><blockquote>
<p>guardian:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 38%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"></th>
<th><blockquote>
<p>addressOne addressTwo addressThree</p>
</blockquote></th>
<th><blockquote>
<p>city state zip</p>
</blockquote></th>
<th><blockquote>
<p>homePhone workPhone</p>
</blockquote></th>
<th><blockquote>
<p>addrs_one_txt, addrs_two_txt, addrs_three_txt, city_nm, postal_cd, zip_prefix_nbr, home_phone_nbr, work_phone_nbr</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p><em>Temporary Patient Address</em></p>
</blockquote></th>
<th><blockquote>
<p>patient_account:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 16%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="3"><blockquote>
<p><strong>PSC Field(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Database Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>addressOne addressTwo addressThree</p>
</blockquote></td>
<td><blockquote>
<p>city state zip</p>
</blockquote></td>
<td><blockquote>
<p>homePhone workPhone</p>
</blockquote></td>
<td><blockquote>
<p>temp_addrs_one_txt, temp_addrs_two_txt, temp_addrs_three_txt, temp_city_nm, temp_postal_cd, temp_zip_prefix_nbr,</p>
<p>temp_home_phone_nbr, temp_work_phone_nbr</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/116.png)</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>gender</p>
</blockquote></td>
<td><blockquote>
<p>patient_account.gender_cd</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>DOD</p>
</blockquote></td>
<td><blockquote>
<p>patient_account.death_dt</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="4"></td>
<td colspan="3"><blockquote>
<p>admission date</p>
</blockquote></td>
<td><blockquote>
<p>patient_account.admission_dt</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>discharge date</p>
</blockquote></td>
<td><blockquote>
<p>patient_account.discharge_dt</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>room / bed</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>ward</p>
</blockquote></td>
<td><blockquote>
<p>patient_account.ward_nm</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5"></td>
<td colspan="3"><blockquote>
<p>service connected %</p>
</blockquote></td>
<td><blockquote>
<p>patient_account.service_connected_percent_nbr</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>primary eligibility code</p>
</blockquote></td>
<td><blockquote>
<p>patient_account.primary_eligibility_txt</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>claim#</p>
</blockquote></td>
<td><blockquote>
<p>person.claim_nbr</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>person type code</p>
</blockquote></td>
<td><blockquote>
<p>person.person_type_cd patient_account.person_type_cd</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>Veteran status</p>
</blockquote></td>
<td><blockquote>
<p>patient_account.veteran_status_ind</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="6"><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/117.png)</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>civil date ruled incompetent</p>
</blockquote></td>
<td><blockquote>
<p>guardian.rule_incompetent_dt</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>civil guardian name</p>
</blockquote></td>
<td><blockquote>
<p>guardian.full_nm</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>civil guardian relationship</p>
</blockquote></td>
<td><blockquote>
<p>guardian.rlnshp_nm</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>civil guardian address</p>
</blockquote></td>
<td><blockquote>
<p>guardian (see Civil Guardian Address, above)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>VA guardian name</p>
</blockquote></td>
<td><blockquote>
<p>guardian.full_nm</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>VA guardian relationship</p>
</blockquote></td>
<td><blockquote>
<p>guardian.rlnshp_nm</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 41%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>PSC Field(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Database Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>VA guardian address</p>
</blockquote></td>
<td><blockquote>
<p>guardian (see VA Guardian Address, above)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VPFS Security Roles Matrix

# Appendix B VPFS Security Roles Matrix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table maps available VPFS functions by role. A user account may have access to one or more roles, as determined by the security keys assigned to that user account in VistA. For more information about the security keys for VPFS, see the VPFS User Guide.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Menu Item</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sub Item 1</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sub Item 2</strong></p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/118.png)</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/119.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/120.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/121.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/122.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/123.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/124.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="13"><blockquote>
<p><strong>Select Patient</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Search and Filter</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>View All Patients (per Institution)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Select Patient, go to Account page for patient record</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Show Patient Cards</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Register Patient</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
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
<p>Request Patient Transfer</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Post Multiple Transactions</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Overdraw Account</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>+</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Override Restriction</p>
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
<td>+</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Override Deferral Date</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>+</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>Verify Balances</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th>X</th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="13"><blockquote>
<p><strong>Account Tab</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>View Account Balance</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Post Transaction</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Overdraw Account</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>+</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Override Restriction</p>
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
<td>+</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Menu Item</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sub Item 1</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sub Item 2</strong></p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/125.png)</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/126.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/127.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/128.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/129.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/130.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/131.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Override Deferral Date</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>+</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Verify Balance</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Transfer Patient</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="13"><blockquote>
<p><strong>Patient Tab</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Edit Patient Information</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Edit Special Remarks</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Edit Station (Transfer Patient)</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>View Patient Information</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>View Special Remarks</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="13"><blockquote>
<p><strong>Guardian Tab</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Add/Edit Guardian Information</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>View Guardian Information</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="13"><blockquote>
<p><strong>Transactions Tab</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>Search and Filter</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th>X</th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th></th>
<th>X</th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>View Transaction History</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>View Transaction Reports</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Edit Deferral Date</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="13"><blockquote>
<p><strong>Suspense Tab</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Add Item</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Cancel Item</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Menu Item</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sub Item 1</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sub Item 2</strong></p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/132.png)</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/133.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/134.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/135.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/136.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/137.png)</p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/138.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Cancel Recurrences of Item</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Cancel Items for Date</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
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
<p>Review Suspense Items per Patient (Select Suspense)</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="13"><blockquote>
<p><strong>Log Tab</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>View Patient Log</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="13"><blockquote>
<p><strong>Administration</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>Perform Table Maintenance</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Award Frequencies</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Form Types</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Help Text</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Income Source Types</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Institutions</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Patient Statuses</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Patient Types</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Payee Types</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Payment Types</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Remarks</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>References</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>System Parameters</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>User Account / Elect. Signature</p>
</blockquote></td>
<td></td>
<td></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Menu Item</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sub Item 1</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sub Item 2</strong></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="13"><blockquote>
<p><strong>Reports</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Patient Card (Selected Patient)</p>
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
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Print Selected Cards</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Print All Cards</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Transaction Display</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Information Display</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Master Transaction Review</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
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
<p>Standard Reports</p>
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
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Activity Audit Listing</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Dormant Account Listing</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Indigent Patient Listing</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Overdue Restriction Search</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Patient Summary</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Search for Min/Max Restrictions</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Patient Listing</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Account Balances</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Transaction Listing</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Fiscal Audit</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>Fiscal Transaction Summary</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th>X</th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Date Variance</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Productivity</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Menu Item</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Sub Item 1</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Sub Item 2</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/139.png)</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/140.png)</p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/141.png)</p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/142.png)</p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/143.png)</p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/144.png)</p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-version-1-2-systems-management-guide/145.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Negative Balances</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Deceased Patient w/ Balance</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Discharged Patient w/ Balance</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>Inactive Withdrawal Listing</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Station Balances</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="13"><blockquote>
<p><strong>Select Suspense</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Search and Filter</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>View Suspense Records across Patients</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Select Suspense Item, go to Suspense page for patient record</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>Cancel Suspense Item</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th>X</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Logout</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td colspan="3"><blockquote>
<p>X X X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>