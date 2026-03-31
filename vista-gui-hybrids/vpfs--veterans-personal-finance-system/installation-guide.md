---
title: VPFS Version 1.2 Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Install Guide
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
menu_options: 1
description: > The purpose of the System Administration/Installation Guide is to provide step-by-step instructions for installing the various components for the Veterans Personal Finance System (VPFS).
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - blockquote
  - vpfs
  - class
  - table
  - contents
  - installation
  - application
  - connection
  - vistamigrate
  - even
page_count: 0
word_count: 7873
section_count: 12
table_count: 0
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: July 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/vpfs_install_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/vpfs_install_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=170"
---

---
title: |
  Veterans Personal Finance System (VPFS)

  Installation Guide
---

Version 1.2.0

![](vpfs-version-1-2-install-guide/001.png)

July 2020

> Department of Veterans Affairs (VA) Office of Information and Technology (OIT)

> Enterprise Program Management Office (EPMO)

#### Document Approval Signatures

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 44%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Title: Project Manager</p>
</blockquote></th>
<th><blockquote>
<p>Signed: [signature on file] Typed: <mark>redacted</mark></p>
</blockquote></th>
<th><blockquote>
<p>Date:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Title: SQA Manager</p>
</blockquote></td>
<td><blockquote>
<p>Signed: [signature on file] Typed: <mark>redacted</mark></p>
</blockquote></td>
<td><blockquote>
<p>Date:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> History of Revisions

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 31%" />
<col style="width: 19%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section Changed</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description of Change</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Effective Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Contacts</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Initial release of document</p>
</blockquote></td>
<td><blockquote>
<p>12/1/06</p>
</blockquote></td>
<td><blockquote>
<p>Project Manager: <mark>redacted</mark></p>
<p>Developers: <mark>redacted</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.1.2</p>
</blockquote></td>
<td><blockquote>
<p>2.3</p>
</blockquote></td>
<td><blockquote>
<p>Dependency services upgrade</p>
<p>These changes are associated with the VPFS patch release 1.1.2</p>
</blockquote></td>
<td><blockquote>
<p>06/24/09</p>
</blockquote></td>
<td><blockquote>
<p><mark>redacted</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 31%" />
<col style="width: 19%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1.1.3</p>
</blockquote></th>
<th><blockquote>
<p>2.3</p>
<p>Dependencies</p>
<p>6.4.1</p>
<p>Before You Begin</p>
</blockquote></th>
<th><blockquote>
<p>Added note about SDS 18 upgrade</p>
<p>Updated VPFS dependency components version.</p>
<p>Updated Footer v 1.1.3</p>
<p>Step 7.</p>
<p>Added notes about context-root</p>
<p>These changes are associated with the VPFS patch release 1.1.3</p>
</blockquote></th>
<th><blockquote>
<p>06/28/2010</p>
<p>12/21/2010</p>
<p>04/12/2011</p>
</blockquote></th>
<th><mark>redacted</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.2.0</p>
</blockquote></td>
<td rowspan="7"></td>
<td></td>
<td><blockquote>
<p>1/7/2019 –</p>
</blockquote></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>02/05/2020</p>
</blockquote></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Incorporating 2FA Functionality and TRM Upgrades</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

ii VPFS System Administration/Installation Guide Table of Contents

#### Table of Contents

1.  [Overview 2](#overview)
    1.  [Application Modernization Project 2](#application-modernization-project)
2.  [Pre-Requisites/Conditions 3](#pre-requisitesconditions)
    1.  [Target Installation Environment 3](#target-installation-environment)
    2.  [Software Tools 3](#software-tools)
    3.  [Dependencies 4](#dependencies)
3.  [Upgrading a Prior Installation. 6](#upgrading-a-prior-installation)
[4. Dependency Installation Notes ..................................................................................... .........................................](#dependency-installation-notes)
7 4.1 Interface Installation Notes 7
1.  [VistALink 7](#vistalink)
2.  [Standard Data Service (SDS) 8](#standard-data-service-sds)
3.  [KAAJEE 8](#kaajee)
4.  [Person Service Lookup (PSL) / Person Service Construct (PSC) 8](#person-service-lookup-psl-person-service-construct-psc)
5.  [Electronic Signature 9](#electronic-signature)
5.  [Database Setup 10](#database-setup)
[Using an Installation Log 10](#using-an-installation-log)
1.  [Preparing the Installation Scripts 10](#preparing-the-installation-scripts)
2.  [Creating VistAMigrate Schema 11](#creating-vistamigrate-schema)
3.  [Creating Objects for VistAMigrate User 11](#creating-objects-for-vistamigrate-user)
4.  [Creating VPFS Schema 11](#creating-vpfs-schema)
5.  [Granting Access to SDS Objects for VPFS 12](#granting-access-to-sds-objects-for-vpfs)
6.  [Creating Objects for VPFS User 12](#creating-objects-for-vpfs-user)
7.  [Creating Jobs for the Stored Procedures 13](#creating-jobs-for-the-stored-procedures)
8.  [Creating VPFS Project in VistAMigrate 14](#creating-vpfs-project-in-vistamigrate)
6.  [VPFS Application Installation 15](#vpfs-application-installation)
    1.  [Signing into the WebLogic Server Administration Console 15](#signing-into-the-weblogic-server-administration-console)
    2.  [Creating a JDBC Connection Pool for VPFS 16](#creating-a-jdbc-connection-pool-for-vpfs)
    3.  [Creating a Data Source for the Connection Pool 22](#creating-a-data-source-for-the-connection-pool)
    4.  [Deploying the VPFS Application 25](#deploying-the-vpfs-application)
        1.  [Before You Begin 25](#before-you-begin)
        2.  [Steps to Deploy 26](#steps-to-deploy)
    5.  [Logging 27](#logging)
[7. VPFS VistAMigrate Installation .........................................................................................................................](#vpfs-vistamigrate-installation)
29
1.  [Logging in to the WebLogic Server Administration Console 29](#logging-in-to-the-weblogic-server-administration-console)
2.  [Creating a JDBC Connection Pool for VistAMigrate 30](#creating-a-jdbc-connection-pool-for-vistamigrate)
3.  [Creating a Data Source for the Connection Pool 36](#creating-a-data-source-for-the-connection-pool-1)
> List of Figures
> iii
4.  Root and Code Folders Setup 38
5.  Deploying the VistAMigrate Application 39
    1.  Before You Begin 39
    2.  Steps to Deploy 40
6.  Logging 41
8.  Post-Installation Steps 42
    1.  Post Interface Installation Steps 42
        1.  Connecting to VistA Sites. 42
9.  Testing the VPFS Application Installation 43
    1.  Testing the Installation of the VPFS Application 43
    2.  Testing the Installation of the VistAMigrate Application 43
    3.  Testing the SMTP Connection 44
10. Rolling Back the VPFS Application Install. 45
> Appendix A. References 46
> VPFS Project Documents 46
> Non-VPFS Project Documents 46
> Appendix B. Acronyms and Abbreviations 47List of Figures
> Figure 6-1. WebLogic Server Administration Console Sign-In Page 15
> Figure 6-2. JDBC Connection Pool Configuration page 16
> Figure 6-3. Choose Database page 16
> Figure 6-4. Define Connection Properties page 17
> Figure 6-5. Create and Deploy page 18
> Figure 6-6. JDBC Connection Pools configuration page 18
> Figure 6-7. General page for the connection pool 19
> Figure 6-8. Connection page 19
> Figure 6-9. Advanced Options page 21
> Figure 6-10. JDBC Data Sources page 22
> Figure 6-11. Configure the data source page 23
> Figure 6-12. Connect to connection pool page 23
> Figure 6-13. Target the data source page 24
> Figure 6-14. Configuration page table 24
> Figure 7-1. WebLogic Server Administration Console Sign-In Page 29
> Figure 7-2. JDBC Connection Pool Configuration page 30
> Figure 7-3. Choose Database page 30
> Figure 7-4. Define Connection Properties page 31
> Figure 7-5. Create and Deploy page 32
> Figure 7-6. JDBC Connection Pools configuration page 32
> Figure 7-7. General page for the connection pool 33
> Figure 7-8. Connection page 33
> Figure 7-9. Advanced Options page 35
> Figure 7-10. JDBC Data Sources page 36
> Figure 7-11. Configure the data source page 36
> Figure 7-12. Connect to connection pool page 37
> Figure 7-13. Target the data source page 37
> Figure 7-14. Configuration page table 38
> Figure 9-1. Welcome to the Veterans Personal Finance System Page 43
> Figure 9-2. VistAMigrate Pick Project Page 44
List of Tables

#### List of Tables

Table 1-1. The Installation Process 2
Table 4-1. Sample Grid for Recording M Connection Information for VistaLink 8
This page is left blank intentionally.
About This Document

## About This Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of the System Administration/Installation Guide is to provide step-by-step instructions for installing the various components for the Veterans Personal Finance System (VPFS).

### Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document is intended to be used by system administrators for installing and maintaining the Oracle database, VPFS and VistAMigrate.

### Conventions Used in this Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indicates…</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>bold</strong></p>
</blockquote></td>
<td><blockquote>
<p>A control that you click, such as a button, icon, or link, or a field label.</p>
<p>Example: Click <strong>Deploy</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Courier - normal</p>
</blockquote></td>
<td><blockquote>
<p>Text that appears on the screen or in a log file.</p>
<p>Example: Table created.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Courier - <strong>bold</strong></p>
</blockquote></td>
<td><blockquote>
<p>Text that you type.</p>
<p>SQL&gt; <strong>quit</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>&lt;<em>Courier&gt;</em> italic and enclosed in angle brackets</p>
</blockquote></td>
<td><blockquote>
<p>A variable that you replace with the specified text</p>
<p>Enter password: &lt;<em>SYSDBA password</em>&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

1

> .

1.  Overview

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Application Modernization Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Department of Veterans Hospital Administration (VHA) is in the process of re-hosting a number of legacy applications, moving from the MUMPS-based VistA environment to the VA‟s standard modern environment, which includes Oracle for the database environment and the Java 2 Platform, Enterprise Edition (J2EE) for the application software environment. The redesigned system, the Veterans Personal Financial System (VPFS), uses the Oracle 11g database and the BEA WebLogic 10.3.6 Application Server, built using the J2EE open source platform running on Red Hat Linux servers. The database is centralized for all facilities at the VA Enterprise Management Center, and the application is accessible via a secure, 508-compliant Web browser front end.

> ![](vpfs-version-1-2-install-guide/002.png)Table 1-1. The Installation Process

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 47%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task Sequence</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>For information, see…</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>Verify that all pre-requisites and pre-conditions are met.</p>
</blockquote></td>
<td><blockquote>
<p><u>Chapter 2. Pre-Requisites/Conditions</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>Install all dependent interfaces.</p>
</blockquote></td>
<td><blockquote>
<p><u>Chapter 4. Dependency Installation</u> <u>Notes</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>Install the VPFS database using SQL*Plus scripts provided in the distribution package.</p>
<p>Use the batch script that prompts you through all steps, or</p>
<p>Use an individual script for each step.</p>
</blockquote></td>
<td><blockquote>
<p><u>Chapter 6. Database Setup</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>Install the VPFS application using the WebLogic Application Server Console.</p>
</blockquote></td>
<td><blockquote>
<p><u>Chapter 7. VPFS Application Installation</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>Install the VistAMigrate application using the WebLogic Application Server Console.</p>
</blockquote></td>
<td><blockquote>
<p><u>Chapter 8. VPFS VistAMigrate</u> <u>Installation</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>Perform all post-installation steps.</p>
</blockquote></td>
<td><blockquote>
<p><u>Chapter 9. Post-Installation Steps</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>Test the installation.</p>
</blockquote></td>
<td><blockquote>
<p><u>Chapter 10. Testing the VPFS</u> <u>Application Installation</u></p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  ![](vpfs-version-1-2-install-guide/003.png)Pre-Requisites/Conditions

## Pre-Requisites/Conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides a checklist for the pre-requisites and conditions that must be met before you can install and run the Veterans Personal Funds System (VPFS) application.

### Target Installation Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following environment must be in place:

- A BEA cluster of managed WebLogic servers (v 10.3.6 or higher) running on Red Hat Linux Advanced Server 4.0 or higher
- A load balancer (either hardware or software)
- A database server running Oracle Enterprise Database 10g

### Software Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following applications must be installed as part of the BEA WebLogic install:

- Java Development Kit (JDK) v1.7.0_80 or higher
- J2EE v1.7 or higher
- the Sun Java Virtual Machine (Sun JVM)

> The following tools must be installed on the application server used by VistAMigrate. It is recommended that an Oracle administrator perform this install. This installation requires system database administrator privileges:

- Oracle SQL\*Loader
- Oracle SQL\*Plus

> Note: These tools are included in the suite of administration tools that is installed when you select the Administrator installation option of the Oracle client. The Oracle client is provided in the Oracle Database Client Release for Linux or Windows download available on Oracle's web site.

2.  Pre-Requisites/Conditions

### Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following dependencies and services must be installed and configured:

> Note: For detailed installation instructions regarding Java and M dependencies, see the corresponding product documentation.

#### Services

- VistALink v1.6
- SDS v13.0 or higher (including SDS schema)
- Person Service Lookup v4.0.4.4 or higher

> .

- Person Service Construct v2.0.0.8 or higher
- E-Signature v1.0.0.024 or higher
- SSOI v1.0.0

#### Kernel Authentication and Authorization for J2EE (KAAJEE)

- KAAJEE v1.0.1.003, KAAJEE SSPI v1.0 or higher
- VistA users are assigned to roles and granted access permissions in KAAJEE.

> For information about user groups and permission, see the *VPFS Software Design Document (SDD) Appendix E – User Roles and Access*. Vista Legacy

- All M connection information must be available (such as IP address, port number, and access and verify codes) for each M system with which VPFS will interface.
- All required M patches (for RPCs, migration, etc.) must be applied to the VistA systems with which VPFS will communicate.

> Note: With the latest release of VPFS version 1.2.0, SDS API jar has been upgraded to v18.0.

> The interface interdependencies (on the Java side) are:

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Interface Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Dependent Interfaces</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VistALink 1.6</p>
</blockquote></td>
<td><blockquote>
<p>None</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Standard Data Service (SDS)</p>
</blockquote></td>
<td><blockquote>
<p>None</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
<td><blockquote>
<p>VistALink 1.6, SDS Institution API</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient Service Construct</p>
</blockquote></td>
<td><blockquote>
<p>VistALink 1.6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient Service Lookup</p>
</blockquote></td>
<td><blockquote>
<p>VistALink 1.6</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>E-Signature</p>
</blockquote></td>
<td><blockquote>
<p>VistALink 1.6</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note: VistALink is required by any interface that connects to VistA. KAAJEE uses VistALink and SDS internally. These two interfaces should be installed before the others. Once these two interfaces are installed, the other interfaces may be installed in any order.

> This version of VPFS uses VistALink libraries that have reverse-IP check enabled.

> Confirm all entries in the VistALink connectorConfig.xml file have the reverse IP information configured. Otherwise VistALink connector will not be able to connect out to those systems. This was done for security purposes and to pass Fortify compliance.

3.  Upgrading a Prior Installation

## Upgrading a Prior Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a newer version of any component of VPFS or any of the dependencies becomes available, please refer to the readme or release notes for that component.

> VPFS Database upgrades will be distributed as patches for existing installations, as well as updated installation scripts for new installations. Each database patch is supplied with an associated readme file with specific installation instructions for that patch.

> Upgrades to the VPFS or VistAMigrate applications can generally be performed by following the process outlined in sections 6.4 (Deploying the VPFS Application) or 7.5 (Deploying the VistAMigrate Application), respectively. Please refer to the readme file that is distributed with each application for any additional steps that may be required.

> .

2.  Dependency Installation Notes

## Dependency Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Install interfaces in accordance with the installation instructions provided with the interface. Installation notes are provided in this section, as needed, only if specific installation information is needed for the VPFS installation.

> Install the following interfaces in the same domain that you are using to deploy VPFS:

- VistALink
- SDS
- KAAJEE
- Patient Service Lookup
- Patient Service Construct

### Interface Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VistALink

> VistALink is the transport mechanism for any interface that connects to the legacy system. Detailed installation instructions for both the Java and M components are included in the VistALink distribution.

> ![](vpfs-version-1-2-install-guide/004.png)Before installing VistALink, make sure you have the M connection information (IP address, port number, access and verify code) for each M system with which VPFS will interface. These settings are used in the VistALink connectorConfig.xml configuration file to establish the VistALink connections.

> Note: Table 4-1 provides a sample grid that you could use to record M connection information.

> ![](vpfs-version-1-2-install-guide/005.png)Install and configure VistALink before deploying VPFS. If you deploy VPFS before you install VistALink you will receive an error when attempting to deploy VPFS.

> ![](vpfs-version-1-2-install-guide/006.png)Ensure that M users are assigned to groups and roles so that they will have the proper permissions to access the VistALink menu options, otherwise VistALink RPC calls will fail. This is documented in detail in the VistALink installation instructions.

> ![](vpfs-version-1-2-install-guide/007.png)VistALink has special installation steps to successfully deploy on WebLogic. See the VistALink documentation for installation instructions.

> 4 Dependency Installation Notes

> Table 4-1. Sample Grid for Recording M Connection Information for VistaLink

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 30%" />
<col style="width: 17%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>M Connection:</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>M Connection:</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>IP Address:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>IP Address:</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 30%" />
<col style="width: 17%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Port number:</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Port number:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Access code:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Access code:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Verify code:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Verify code:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>M Connection:</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>M Connection:</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IP Address:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>IP Address:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Port number:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Port number:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Access code:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Access code:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Verify code:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Verify code:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Standard Data Service (SDS)

> The SDS API is a core service component that provides standard reference data that describes the VHA organizational structure.

> ![](vpfs-version-1-2-install-guide/008.png)Create/modify the SDS schema. The SDS schema/user is referenced in the VPFS database scripts and may need to be changed to match the actual schema name.

> ![](vpfs-version-1-2-install-guide/009.png)Pay close attention to the Standard Data Service Server Administration Installation Guide, which describes how the component is configured. VPFS will not function unless SDS is properly configured.

#### KAAJEE

> ![](vpfs-version-1-2-install-guide/010.png)After installing the KAAJEE SSPI, be sure to update the KaajeeDatabase.properties to access the correct database.

> ![](vpfs-version-1-2-install-guide/011.png)Prior to deploying the VPFS and VistAMigrate applications, make sure the kaajeeConfig.xml file is updated with appropriate STS service address and with the station numbers of the sites you need to access. This is covered in more detail during VPFS and VistAMigrate installation.

#### Person Service Lookup (PSL) / Person Service Construct (PSC)

> ![](vpfs-version-1-2-install-guide/012.png)To use Person Service Lookup (PSL) and Person Service Construct (PSC) with VPFS special broker type configurations must be set for legacy VistA user accounts. See the Person Service installation guides for specific legacy account setup instructions.

> ![](vpfs-version-1-2-install-guide/013.png)Prior to deploying the VPFS and VistAMigrate applications, make sure the PSL and PSC properties are updated as needed for your server configuration. This is covered in more detail in Section 6.4.1.

4.  Dependency Installation Notes

#### Electronic Signature

> ![](vpfs-version-1-2-install-guide/014.png)The Java interface for Electronic Signature (e-signature) is incorporated in the VPFS application. No additional Java-side installation is required.

> .

> ![](vpfs-version-1-2-install-guide/015.png)To use Electronic Signature with VPFS a special broker type configuration must be set for legacy VistA user accounts. See the Electronic Signature installation guide for specific legacy account setup instructions.

## Database Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the steps in this section to execute the SQL\*Plus scripts and set up the VPFS database on the Oracle database server. The scripts used for the VPFS database refer to the default tablespace. If your site is using another tablespace for VPFS, edit the scripts to point to the correct tablespace prior to executing these scripts.

> Note: You may prefer to group tasks differently than the sequence presented in this chapter based on user privileges or some other criteria. For example: A user with SYSDBA privileges may choose to log on as SYSDBA and create both schemas (VPFS and VistAMigrate) before creating the objects or granting privileges for those schemas. Be aware that there may be prerequisites, as noted.

> Note: This procedure is written for new installations. Database patches may be available to upgrade an existing installation. Please refer to section 3 (Upgrading a Prior Installation) for upgrade installations.

### Using an Installation Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> SQL\*Plus allows you to create an installation log containing the output of the SQL script commands. After logging into the Oracle database using SQL\*Plus, use the SPOOL command to generate a log file.

> Note: Any time you restart SQL\*Plus, you will need to set the spool output again. This setting is not maintained when you quit.

1.  Create the log file. If you are using Oracle 10g and have an existing log file you want to append to, include “append” at the end of the command.

> SQL\> spool install_vpfs.log

2.  Execute the script(s) specified in the steps below.
3.  Close the log file or quit SQL\*Plus.

> After installation is complete, view the installation log using your preferred text viewer. You can use the

> more command or an application such as gedit (Linux) or Notepad (Windows).

### Preparing the Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VPFS scripts need to be extracted to a machine that has SQL\*Plus access to the Oracle database where the VPFS and VistAMigrate schemas will be created:

1.  Create a temporary directory on your local drive.

> Note: A temporary directory can be on the SAN or on another drive as long as you are able to access the scripts and run the scripts for the database server.

2.  Extract the contents from the database scripts distribution package to the temporary directory created above.

> 5\. Database Setup

> 5\. Database Setup

### Creating VistAMigrate Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Requires DBA: To complete this step you must be logged on to the Oracle database as a user with DBA privileges.

> Note: The script in this procedure creates a database user with username “vista_migrate” and password

> “vista_migrate” in the “USERS” tablespace. If you choose to change the username and password, or default or temporary tablespaces, be sure to edit the cr_vista_migrate_schema.sql and cr_vista_migrate_objects.sql scripts to match prior to executing them. Also make sure these changes are reflected in the Data Source section.

> To create the VistAMigrate schema:

3.  Change to the vistamigrate/scripts directory.
4.  Start SQL\*Plus and log on to the Oracle database as a user with DBA privileges.

> \$ sqlplus

> Enter user-name: sys/password@databasename \[as sysdba\]

5.  Run cr_vista_migrate_schema.sql to create the VistAMigrate schema:

> SQL\> @cr_vista_migrate_schema.sql

6.  Continue with the next section of this document or log out (SQL\> quit).

### Creating Objects for VistAMigrate User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Notes: The VistAMigrate schema should already have been created. If this is not the case, create it before continuing.

> The script in this procedure creates database objects in the “vista_migrate” schema. If you chose a different VistAMigrate schema name, be sure to edit the cr_vista_migrate_objects.sql and pk_DM_UTILS.sql scripts before continuing.

> To create objects for VistAMigrate User:

7.  Start SQL\*Plus (if not already running) and log on to the Oracle database as the VistAMigrate user.

> SQL\> connect vista_migrate/vista_migrate@databasename

8.  Run cr_vista_migrate_objects.sql to create all the relevant tables and objects for VistAMigrate.

> SQL\> start cr_vista_migrate_objects.sql

9.  Continue with the next section of this document or log out (SQL\> quit).

### Creating VPFS Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Requires DBA: To complete this step you must be logged on to the Oracle database as a user with DBA privileges.

> Note: The script in this procedure creates a database user with username “vpfs” and password “vpfs” in the “USERS” tablespace. If you choose to change the username and password, or default or temporary tablespaces, be sure to edit the cr_vpfs_schema.sql and cr_all_objects.sql scripts to match prior to executing them. Also make sure these changes are reflected in the Data Source section.

> To create the VPFS Schema:

10. Change to the vpfs/scripts directory.
11. Start SQL\*Plus and log on to the Oracle database as a user with DBA privileges.

> \$ sqlplus

> Enter user-name: sys/password@databasename \[as sysdba\]

12. Run cr_vpfs_schema.sql to create the VPFS schema.

> SQL\> @cr_vpfs_schema.sql

13. Continue with the next section of this document or log out (SQL\> quit).

### Granting Access to SDS Objects for VPFS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Notes: The SDS and VPFS schemas should already have been created. If this is not the case, create them before continuing. Contact the Health System Design & Development Standard Data Service for SDS database installation instructions.

> The script in this procedure grants SELECT permissions on tables in the “sdsadm” schema to the “vpfs” user. If you chose different schema names for SDS or VPFS, be sure to edit the grant_sds_access.sql script to match prior to executing it.

> To grant access to SDS objects:

14. Start SQL\*Plus (if not already running) and log on to the Oracle database as a user with DBA privileges or the SDS user.

> SQL\> connect sys/password@databasename \[as sysdba\]

15. Run grant_sds_access.sql to grant read access to the SDS tables to the VPFS user.

> SQL\> start grant_sds_access.sql

16. Continue with the next section of this document or log out (SQL\> quit).

### Creating Objects for VPFS User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 5\. Database Setup

> Notes: The SDS and VPFS schemas should already have been created. If this is not the case, create them before continuing.

> The scripts in this procedure create database objects in the “vpfs” schema and reference the SDS and VistAMigrate schemas. The following scripts may need to be edited prior to executing them:

1.  If you chose a different VPFS schema name, edit the create_objects/cr_all_objects.sql script.

> 5\. Database Setup

2.  If you chose a different SDS schema name (default is “sdsadm”), edit the create_objects/cr_all_objects.sql and reference_data/ins_vpfs_institution.sql scripts to match.
3.  If you chose a different VistAMigrate schema name (default is “vista_migrate”), edit the stored_procedures/pk_convertPFOPData_body.sql script to match.

> To create objects for VPFS User:

1.  Start SQL\*Plus (if not already running) and log on to the Oracle database as the VPFS user.

> SQL\> connect vpfs/vpfs@databasename

2.  From the scripts/create_objects folder, run cr_all_objects.sql to create all the relevant tables and objects for VPFS.

> SQL\> start create_objects/cr_all_objects.sql

3.  From the scripts/stored_procedures folder, run cr_all_spObjects.sql to create all the stored procedures required for VPFS.

> SQL\> start stored_procedures/cr_all_spObjects.sql

4.  From the scripts/triggers folder, run cr_all_triggers.sql, to create all the triggers required for VPFS.

> SQL\> start triggers/cr_all_triggers.sql

5.  From the scripts/reference_data folder, run ins_all_reference_data.sql script to insert the reference data to the appropriate tables.

> SQL\> start reference_data/ins_all_reference_data.sql

6.  To enable the sending of email notifications by VPFS, type the following commands at the

> SQL\> prompt to set the email_enabled flag and the address for the SMTP server:

> SQL\> UPDATE vsystem_parameter SET parameter_txt='true' WHERE parameter_cd='EMAIL_ENABLED';

> Replace the italicized text in brackets with the name of your SMTP server:

> SQL\> UPDATE vsystem_parameter SET parameter_txt='*\[SMTP_SERVER\]*' WHERE parameter_cd='SMTP_SERVER';

> Example: if the SMTP server is smtp.va.gov, then the above SQL statement would read:

> SQL\> UPDATE vsystem_parameter SET parameter_txt='smtp.va.gov' WHERE parameter_cd='SMTP_SERVER';

7.  Commit the changes to the database.

> SQL\> commit;

8.  Continue with the next section of this document or log out (SQL\> quit).

### Creating Jobs for the Stored Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: The objects for the VPFS user should already have been created. If this is not the case, create them before continuing.

> To create jobs for VPFS User:

1.  Start SQL\*Plus (if not already running) and log on to the Oracle database as the VPFS user.

> SQL\> connect vpfs/vpfs@databasename

2.  From the scripts/jobs folder, run cr_jobs.sql to create jobs for all stored procedures.

> SQL\> start jobs/cr_jobs.sql

> (Optional) To verify that the jobs were created successfully, run the list_jobs.sql script.

> SQL\> start jobs/list_jobs.sql

3.  Continue with the next section of this document or log out (SQL\> quit).

### Creating VPFS Project in VistAMigrate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Notes: The objects for the VPFS and VistAMigrate users should already have been created. If this is not the case, create them before continuing.

> The script in this procedure grants EXECUTE permissions on VistAMigrate stored procedures to the VPFS user. If you chose different schema names for VistAMigrate or VPFS, be sure to edit the ins_vpfs_data.sql script to match prior to executing it.

> To create the VPFS project in VistAMigrate:

4.  Change to the vistamigrate/scripts directory.
5.  Start SQL\*Plus and log on to the Oracle database as the VistAMigrate user.

> \$ sqlplus

> Enter user-name: vista_migrate/vista_migrate@databasename

6.  Run ins_vpfs_data.sql to create the VPFS project in VistAMigrate.

> SQL\> start ins_vpfs_data.sql

7.  Log out of SQL\*Plus (SQL\> quit).

> 6\. VPFS Application Installation

## VPFS Application Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Important: The VPFS application relies on nightly updates from PSC through VistALink. A VistALink application proxy user account (e.g. VPFS, APPLICATION PROXY) must be present for nightly updates to take place. This user account is created during the installation of Patch PRPF\*3.0\*16 in the legacy VistA database. If problems are encountered running the nightly update, contact IRM to verify that the application proxy user account was created successfully.

> Perform the following steps from the WebLogic Server Administration Console:

1.  Create a JDBC connection pool for VPFS.
2.  Create a Data Source for the VPFS connection pool.
3.  Deploy the VPFS application.
4.  Create the VPFS logging directory.

### Signing into the WebLogic Server Administration Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To sign into the WebLogic Server Administration Console:

1.  Open a web browser and go to http://\<*host\>*:\<*port\>*/console/ The WebLogic Server Administration Console sign in page opens.

> ![Figure 6-1. WebLogic Server Administration Console Sign In Page](vpfs-version-1-2-install-guide/016.png)

*Figure 6-1. WebLogic Server Administration Console Sign In Page*

2.  Sign in as the administration user:
    1.  Username: Enter your administration username.
    2.  Password: Enter your administration password.

6\. VPFS Application Installation

### Creating a JDBC Connection Pool for VPFS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS connects to the Oracle database through WebLogic using JDBC connection pools. JDBC connection pools manage resources by holding connections to the database open until they are needed by HealtheVet VistA applications.

> Use the WebLogic Server Administration Console to create a JDBC connection pool for VPFS.

3.  In the navigation tree on the left of the console, expand Services \> JDBC.
4.  Click the Connection Pools link.

> The JDBC Connection Pool Configuration page displays the list of connection pools that already exist.

> ![Figure 6-2. JDBC Connection Pool Configuration page](vpfs-version-1-2-install-guide/017.png)

*Figure 6-2. JDBC Connection Pool Configuration page*

5.  From the main panel, click the Configure a new JDBC Connection Pool link. The Choose Database page opens.

![Figure 6-3. Choose Database page](vpfs-version-1-2-install-guide/018.png)

*Figure 6-3. Choose Database page*

6.  Select the database type and driver:
    1.  Database Type: Select Oracle.
6.  VPFS Application Installation
    1.  Database Driver: Select \*Oracle’s Driver (Thin XA) Versions: 8.1.7,9.0.1,9.2.0,10
    5.  Click Continue.

> The Define Connection Properties page opens.

![Figure 6-4. Define Connection Properties page](vpfs-version-1-2-install-guide/019.png)

*Figure 6-4. Define Connection Properties page*

6.  Enter Connection Properties:
    1.  Name: Enter the name of the VPFS JDBC connection pool you are defining.
    2.  Database Name: Enter the name of the database (or service name) to connect to.
    3.  Host Name: Enter the name or IP address of the host machine.
    4.  Port: Enter the port of the database server used to connect to the database. The Oracle default port is 1521.
    5.  Database User Name: Enter your database username.
    6.  Password: Enter your password.
    7.  Confirm Password: Enter your password again to confirm.
7.  Click Continue.
8.  To test the database connection, click Test Driver Configuration.

![](vpfs-version-1-2-install-guide/020.png)If the configuration is correct, the Create and Deploy page opens. Continue with step

![](vpfs-version-1-2-install-guide/021.png)9.

If an error message appears at the top of the page, correct the error before you continue.

6\. VPFS Application Installation

![Figure 6-5. Create and Deploy page](vpfs-version-1-2-install-guide/022.png)

*Figure 6-5. Create and Deploy page*

9.  Select the radio button for All servers in the cluster to target the connection pool to the cluster.
10. Click Create and deploy.

> Once created successfully, the JDBC Connection Pools configuration page opens. The new JDBC Connection Pool is added to the table on the JDBC Connection Pools configuration page.

> ![Figure 6-6. JDBC Connection Pools configuration page](vpfs-version-1-2-install-guide/023.png)

*Figure 6-6. JDBC Connection Pools configuration page*

11. Set the Advanced Options:
    1.  Click the name of the JDBC Connection Pool that you created. The General page opens for the connection pool you requested.

> 6\. VPFS Application Installation

![Figure 6-7. General page for the connection pool](vpfs-version-1-2-install-guide/024.png)

*Figure 6-7. General page for the connection pool*

2.  Click the Connections tab. The Connection page opens.

![Figure 6-8. Connection page](vpfs-version-1-2-install-guide/025.png)

*Figure 6-8. Connection page*

3.  Click the Show link to the right of Advanced Options. The Advanced Options page opens.

6\. VPFS Application Installation

![](vpfs-version-1-2-install-guide/026.png)

6.  VPFS Application Installation

![](vpfs-version-1-2-install-guide/027.png)

12. Check to select all of the following advanced features:

#### Test Reserved Connections

1.  Test Created Connections

#### Test Released Connections

2.  Supports Local Transaction.
13. Click Apply.

> The advanced options that you selected are applied.

6\. VPFS Application Installation

### Creating a Data Source for the Connection Pool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the WebLogic Server Administration Console to create a data source for the JDBC connection pool for VPFS.

1.  In the navigation tree on the left of the console, expand Services \> JDBC.
2.  Click the Data Source link.

> ![Figure 6-10. JDBC Data Sources page](vpfs-version-1-2-install-guide/028.png)

*Figure 6-10. JDBC Data Sources page*

3.  Click the Configure a new JDBC Data Source link. The Configure the data source page opens.
6.  VPFS Application Installation

![Figure 6-11. Configure the data source page](vpfs-version-1-2-install-guide/029.png)

*Figure 6-11. Configure the data source page*

4.  Define the new JDBC data source:
    1.  Name: Enter the VPFS data source name.
    2.  JNDI Name: Enter jdbc/vpfsCoreDS. (Required by VPFS code.)
5.  Leave the default settings for the rest of the fields.
6.  Click Continue.
7.  Connect to connection pool:
    1.  For the Pool Name, select the JDBC connection pool created for VPFS.
    2.  Click Continue.

> The Connect to connection pool page opens.

![Figure 6-12. Connect to connection pool page](vpfs-version-1-2-install-guide/030.png)

*Figure 6-12. Connect to connection pool page*

6\. VPFS Application Installation

8.  Select the Pool Name for the VPFS pool you created.
9.  Click Continue.

> The Target the data source page opens.

![Figure 6-13. Target the data source page](vpfs-version-1-2-install-guide/031.png)

*Figure 6-13. Target the data source page*

10. Target the data source:
    1.  Select the radio button next to All servers in the cluster to target the data source to the cluster.
    2.  Click Create.

> ![](vpfs-version-1-2-install-guide/032.png)The Configuration page opens. The new JDBC Data Source you created is listed in the table.

Figure 6-14. Configuration page table

### Deploying the VPFS Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section presents the steps necessary to deploy the application to the Application Server.

#### Before You Begin

> Before you can display VPFS on the application server, you must:

6.  VPFS Application Installation

> ![](vpfs-version-1-2-install-guide/033.png)Update the PatientLookup.properties file to specify the location of the Person Service Lookup EJBs (pslEJB_4.0.x.x.ear) and authentication credentials.

> ![](vpfs-version-1-2-install-guide/034.png)Update the PatSvcPkg.properties file to specify the location of the Person Service Construct EJBs (PatientServiceR2.ear) and authentication credentials.

> ![](vpfs-version-1-2-install-guide/035.png)Update the kaajeeConfig.xml file to contain the station numbers for the VistA systems you need to access.

> ![](vpfs-version-1-2-install-guide/036.png)Update the KAAJEE_CONTROLLER role in the weblogic.xml file with the WebLogic boot username.

#### To update the application configuration files:

> The files that need to be edited are located in the VPFS .ear file. To edit them, you will need to extract the contents of the .ear file to a temporary directory. Be sure to preserve the directory structure when extracting the contents of the .ear file.

> Note: An .ear file is basically a .zip file with a specific file and directory structure. You can use an application such as File Roller, WinZip, or the jar utility to work with .ear files as you would with a .zip file.

1.  Create a temporary directory to extract the contents of the .ear file to. Copy the VPFS .ear file into this directory.

> \# mkdir vpfstemp

2.  Change directory to the temporary directory. Extract the VPFS .ear file to this directory.

> \# cd vpfstemp

> \# jar xf vpfs.ear

3.  Update the PatientLookup.properties file in VPFS/WEB-INF/classes to specify the location of the Person Service Lookup EJBs (pslEJB_4.0.x.x.ear) and authentication credentials.

> ![](vpfs-version-1-2-install-guide/037.png)Set the providerURL property to the host and port of the server where the Person Service Lookup EJBs are deployed.

> ![](vpfs-version-1-2-install-guide/038.png)Set the securityPrincipal and securityCredentials properties to the username and password of the WebLogic console user or administrator.

> Refer to the Person Service Lookup documentation for detailed instructions as needed.

4.  Update the PatSvcPkg.properties file in VPFS/WEB-INF/classes to specify the location of the Person Service Construct EJBs (PatientServiceR2.ear) and authentication credentials.

> ![](vpfs-version-1-2-install-guide/039.png)Set the providerURL property to the host and port of the server where the Person Service Lookup EJBs are deployed.

> ![](vpfs-version-1-2-install-guide/040.png)Set the securityPrincipal and securityCredentials properties to the username and password of the WebLogic console user or administrator.

> Refer to the Person Service Construct documentation for detailed instructions as needed.

5.  To change the STS service address (e.g. from DEV to SQA), open the kaajeeConfig.xml file and edit the \<sts-service-address\> element with the appropriate value.
6.  VPFS Application Installation
6.  Update the kaajeeConfig.xml file in VPFS/WEB-INF/config to contain the appropriate

> \<station-number\> entries for the VistA systems you need to access. Ensure the appropriate VistaLink connector has been created for each station in this list. See VistaLink documentation for instructions on how to define a new connector.

> ![](vpfs-version-1-2-install-guide/041.png)Add or edit \<station-number\> entries as needed. There must be one entry per station number you need to access.

> \<station-number\>500\</station-number\>

> Refer to the KAAJEE Installation Guide for detailed instructions as needed.

7.  Update the weblogic.xml file in VPFS/WEB-INF to set the KAAJEE_CONTROLLER role principal name to the username of a WebLogic Administrator user (or the WebLogic boot user). KAAJEE requires this to function correctly.

> ![](vpfs-version-1-2-install-guide/042.png)Look for a \<security-role-assignment\> with a \<role-name\> of KAAJEE_CONTROLLER. Change the \<principal-name\> to the name of a WebLogic Administrator user.

> \<principal-name\>weblogic\</principal-name\>

> ![](vpfs-version-1-2-install-guide/043.png)Look for a \<run-as-role-assignment\> with a \<role-name\> of KAAJEE_CONTROLLER. Change the \<run-as-principal-name\> to the name of a WebLogic Administrator user.

> \<run-as-principal-name\>weblogic\</run-as-principal-name\>

8.  (Optional) Context-root „vpfs’ in the META-INF/application.xml is the default context root URL for the VPFS application. This entry in the deployment descriptor can be updated appropriately based on the server URL requirements.
9.  (Optional) If you are going to deploy VPFS as an .ear file, freshen the VPFS .ear file to update the changed files.

> \# jar uf vpfs.ear \*

#### Steps to Deploy

> VPFS can be deployed as either an .ear file or an “exploded” deployment. To use the exploded deployment option, the contents of the temporary directory used above must be copied to the server. To use the .ear file deployment option, the vpfs.ear file may either be on the server or uploaded during deployment.

> Complete these steps to deploy the application:

1.  Using a web browser, connect to the WebLogic Server console.
2.  Sign in as the administration user and supply the appropriate password.
3.  From the left panel, expand the Deployments node and click the Applications link.
4.  From the main panel, click the Deploy a new Application… link.
5.  Select the archive for this application. Do one of the following:
    1.  Navigate to the location of the vpfs.ear file or root directory of the exploded .ear file.
6.  VPFS Application Installation
6.  Click the upload your file(s) link.

> Click Browse… button and navigate to where the VPFS .ear file is located. Select the VPFS .ear file and click the Open button.

> Click Upload.

7.  Select the VPFS application (.ear file or root directory) and click Target Application.
8.  Select targets for this application:
    1.  Click the radio button next to the All servers in the cluster to target the application to the cluster.
    2.  Click Continue.
9.  Review your choices and click Deploy.

> Deployment status: During the process of the deployment, the screen will refresh itself periodically until the application is deployed.

### Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Logging for VPFS is configured in the log4j configuration file, log4j.xml. This file must be specified for each server using the JVM argument -Dlog4j.configuration (example: Dlog4j.configuration=file:///u01/app/bea/user_projects/domains/domVPFS

> /log4j.xml). There should only be a single log4j configuration file in use for any server. You can edit this file to change the default logging level or log file location if needed.

> Log4j is configured by defining \<appender\>s and \<logger\>s. The default appenders and loggers for VPFS are defined in the log4j_VPFS.xml file supplied with the VPFS distribution package. These can be copied into the correct locations in an existing log4j configuration file. A sample log4j configuration file (log4j_sample.xml) is also provided that also includes sample appenders and loggers for our dependencies.

> The default VPFS log file is called vpfs.log. To reduce the size of the log file and facilitate the job of the system admin, the log file is configured to automatically rollover every day. For example, at midnight of every day, the current vpfs.log will be rolled over to vpfs.log.yyyy-MM-dd (yyyy: 4-digit year, MM: 2digit month, and dd: 2-digit day) and a new vpfs.log will be created to log the new day’s events.

> The default configuration creates this file in the log directory. To create the VPFS logging directory:

1.  Log in to one of the machines in the cluster VPFS was deployed to.
2.  Create a directory named “log”. As this is a common logging directory for the server, it may already exist in which case you do not need to try to create it again.

> ![](vpfs-version-1-2-install-guide/044.png)If VPFS is deployed on a managed server, create the directory under the node manager directory.

> \# cd \<BEA_HOME\>/weblogic81/common/nodemanager

> \# mkdir log

> ![](vpfs-version-1-2-install-guide/045.png)If VPFS is deployed on the domain admin server, create the directory in the root directory for the domain..

> \# cd \<BEA_HOME\>/user_projects/domains/vpfsDomain

> \# mkdir log

6\. VPFS Application Installation

3.  Repeat these steps as needed to create the log folder on each machine in the cluster.

> 7\.

## VPFS VistAMigrate Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: Migrated VistA data will be stored in the staging environment on the hardware where VistAMigrate is deployed and that data contains sensitive patient information that must be kept secure. To provide maximum security, consider installing and using VistAMigrate on a computer that can be physically secured in a locked cabinet or secure room and powering off or disconnecting the computer from the network when not in use.

> To install the VistAMigrate application, perform the following tasks from the WebLogic Server Administration Console:

1.  Create a JDBC connection pool for VistMigrate.
2.  Create a Data Source for the VistAMigrate Connection Pool.
3.  Deploy the VistAMigrate application.
4.  Create the VistAMigrate logging directory.

### Logging in to the WebLogic Server Administration Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To log in to the WebLogic Server Administration Console:

1.  Open a web browser and go to http://\<*host\>*:\<*port\>*/console/ The WebLogic Server Administration Console sign in page opens.

> ![Figure 7-1. WebLogic Server Administration Console Sign In Page](vpfs-version-1-2-install-guide/046.png)

*Figure 7-1. WebLogic Server Administration Console Sign In Page*

2.  Log in as the administration user:
    1.  Username: Enter your administration username.
    2.  Password: Enter your administration password.

> VPFS VistAMigrate Installation

7\. VPFS VistAMigrate Installation

### Creating a JDBC Connection Pool for VistAMigrate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS connects to the Oracle database through WebLogic using JDBC connection pools. JDBC connection pools manage resources by holding connections to the database open until they are needed by HealtheVet VistA applications.

> Use the WebLogic Server Administration Console to create a JDBC connection pool for VistAMigrate.

3.  In the navigation tree on the left of the console, expand Services \> JDBC.
4.  Click the Connection Pools link.

> The JDBC Connection Pool Configuration page displays the list of connection pools that already exist.

> ![Figure 7-2. JDBC Connection Pool Configuration page](vpfs-version-1-2-install-guide/047.png)

*Figure 7-2. JDBC Connection Pool Configuration page*

5.  From the main panel, click the Configure a new JDBC Connection Pool link. The Choose Database page opens.

![Figure 7-3. Choose Database page](vpfs-version-1-2-install-guide/048.png)

*Figure 7-3. Choose Database page*

6.  Select the database type and driver:
    1.  Database Type: Select Oracle.
    2.  Database Driver: Select \*Oracle’s Driver (Thin XA) Versions: 8.1.7,9.0.1,9.2.0,10

> 7\.

7.  Click Continue.

> The Define Connection Properties page opens.

![Figure 7-4. Define Connection Properties page](vpfs-version-1-2-install-guide/049.png)

*Figure 7-4. Define Connection Properties page*

8.  Enter Connection Properties:
    1.  Name: Enter the name of the VistAMigrate JDBC connection pool you are defining.
    2.  Database Name: Enter the name of the database (or service name) to connect to.
    3.  Host Name: Enter the name or IP address of the host machine.
    4.  Port: Enter the port of the database server used to connect to the database. The Oracle default port is 1521.
    5.  Database User Name: Enter your database username.
    6.  Password: Enter your password.
    7.  Confirm Password: Enter your password again to confirm.
9.  Click Continue.
10. To test the database connection, click Test Driver Configuration.

![](vpfs-version-1-2-install-guide/050.png)If the configuration is correct, the Create and Deploy page opens. Continue with step

16\.

If an error message appears at the top of the page, correct the error before you continue.

> VPFS VistAMigrate Installation

![](vpfs-version-1-2-install-guide/051.png)7. VPFS VistAMigrate Installation

Figure 7-5. Create and Deploy page

11. Select the radio button for All servers in the cluster to target the connection pool to the cluster.
12. Click Create and deploy.

> Once created successfully, the JDBC Connection Pools configuration page appears. The new JDBC Connection Pool is added to the table on the JDBC Connection Pools configuration page.

> ![Figure 7-6. JDBC Connection Pools configuration page](vpfs-version-1-2-install-guide/052.png)

*Figure 7-6. JDBC Connection Pools configuration page*

13. Set the Advanced Options:
    1.  Click the name of the JDBC Connection Pool that you created. The General page opens for the connection pool you requested.

> ![](vpfs-version-1-2-install-guide/053.png)7.

Figure 7-7. General page for the connection pool

2.  Click the Connections tab. The Connection page opens.

![Figure 7-8. Connection page](vpfs-version-1-2-install-guide/054.png)

*Figure 7-8. Connection page*

3.  Click the Show link to the right of Advanced Options. The Advanced Options page opens.

> VPFS VistAMigrate Installation

![](vpfs-version-1-2-install-guide/055.png)7. VPFS VistAMigrate Installation

> ![](vpfs-version-1-2-install-guide/056.png)7.

14. Check all of the following advanced features:

#### Test Reserved Connections

1.  Test Created Connections

#### Test Released Connections

2.  Supports Local Transaction.
15. Click Apply.

> The advanced options that you selected are applied.

7\. VPFS VistAMigrate Installation

### Creating a Data Source for the Connection Pool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the WebLogic Server Administration Console to create a data source for the JDBC connection pool for VistAMigrate.

16. Click the Data Source link.

> ![Figure 7-10. JDBC Data Sources page](vpfs-version-1-2-install-guide/057.png)

*Figure 7-10. JDBC Data Sources page*

17. Click the Configure a new JDBC Data Source link. The Configure the data source page opens.

> ![Figure 7-11. Configure the data source page](vpfs-version-1-2-install-guide/058.png)

*Figure 7-11. Configure the data source page*

7.  VPFS VistAMigrate Installation
    3.  Define the new JDBC data source:
        1.  Name: Enter the VPFS data source name.
        2.  JNDI Name: Enter jdbc/vistaMigrateCoreDS. (Required by VPFS code.)
    4.  Leave the default settings for the rest of the fields.
    5.  Click Continue.
    6.  Connect to connection pool:
        1.  For the Pool Name, select the JDBC connection pool created for VistAMigrate.
        2.  Click Continue.

> The Connect to connection pool page opens.

![Figure 7-12. Connect to connection pool page](vpfs-version-1-2-install-guide/059.png)

*Figure 7-12. Connect to connection pool page*

7.  Select the Pool Name for the VistAMigrate pool you created.
8.  Click Continue.

> The Target the data source page opens.

![Figure 7-13. Target the data source page](vpfs-version-1-2-install-guide/060.png)

*Figure 7-13. Target the data source page*

7\. VPFS VistAMigrate Installation

9.  Target the data source:
    1.  Select the radio button next to the All servers in the cluster to target the data source to the cluster.
    2.  Click Create.

> The Configuration page opens. The new JDBC Data Source you created is listed in the table.

![Figure 7-14. Configuration page table](vpfs-version-1-2-install-guide/061.png)

*Figure 7-14. Configuration page table*

### Root and Code Folders Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section presents the steps necessary to set up the root folder and code folder on the machine where VistAMigrate is deployed.

> SQL\*Loader and SQL\*Plus must be installed for VistAMigrate to run. Install the Oracle client tools to install SQL\*Loader and SQL\*Plus.

1.  Create a root folder where VistAMigrate will have full access permission (read, write, and execute). For example, /home/bea/vistaMigrate.

> \# mkdir vistaMigrate

2.  Create a VPFS project folder under the root folder.

> VistAMigrate requires a strict file hierarchy to operate. Each project (in this case, the migration for VPFS) requires a folder under the VistAMigrate folder created in the above step. For VPFS migration, create a VPFS folder under the root folder. For example,

> /home/bea/vistaMigrate/VPFS.

> \# cd vistaMigrate

> \# mkdir VPFS

3.  Create a folder called CODE under the project folder. For example,

> /home/bea/vistaMigrate/VPFS/CODE.

> \# cd VPFS

> \# mkdir CODE

4.  Copy the following files into the CODE folder from the distribution:
7.  VPFS VistAMigrate Installation

> ![](vpfs-version-1-2-install-guide/062.png)setenv (Linux) or setenv.bat (Windows) runsqlldr.sh / runsqlldr.bat runsqlplus.sh / runsqlplus.bat vpfs_load_temp.ctl vpfs_analyze_data.sql vpfs_extract_errors.sql vpfs_verify_data.sql

5.  Edit the setenv script to change the VM_ORACLE_HOME variable to point to the Oracle home where the Oracle client tools have been installed.

> Example: VM_ORACLE_HOME='/home/oracle/product/10.1.0/OraClient_1'

6.  Start SQL\*Plus (if not already running) and log on to the Oracle database as the VistAMigrate user.

> SQL\> connect vista_migrate/vista_migrate@databasename

7.  Update the username, password, and data source name to connect to the VPFS database. (Replace vpfs, vpfspassword, and vpfsdatabase as appropriate.)

> SQL\> update dm_setup set db_user_nm='*vpfs*', db_user_pass_txt='*vpfspassword*', db_data_src_txt='*vpfsdatabase*' where project_nm='VPFS';

> SQL\> commit;

### Deploying the VistAMigrate Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Before You Begin

> Before you can display VPFS on the application server, you must:

> ![](vpfs-version-1-2-install-guide/063.png)Update the kaajeeConfig.xml file to contain the station numbers for the VistA systems you need to access.

> ![](vpfs-version-1-2-install-guide/064.png)Update the KAAJEE_CONTROLLER role in the weblogic.xml file with the WebLogic boot username.

> ![](vpfs-version-1-2-install-guide/065.png)Update the VistaMigrateResources.properties file to set the location of the migration root folder.

> The files that need to be edited are located in the VistAMigrate .ear file. To edit them, you will need to extract the contents of the .ear file to a temporary directory. Be sure to preserve the directory structure when extracting the contents of the .ear file.

1.  Create a temporary directory to extract the contents of the .ear file to. Copy the VistAMigrate

> .ear file into this directory.

> \# mkdir vmtemp

2.  Change directory to the temporary directory. Extract the VistAMigrate .ear file to this directory.

> \# cd vmtemp

> \# jar xf vistaMigrate.ear

7\. VPFS VistAMigrate Installation

3.  Update the kaajeeConfig.xml file in VistAMigrate/WEB-INF/config to contain the appropriate \<station-number\> entries for the VistA systems you need to access. Ensure the appropriate VistaLink connector has been created for each station in this list. See

> VistaLink documentation for instructions on how to define a new connector.

> ![](vpfs-version-1-2-install-guide/066.png)Add or edit \<station-number\> entries as needed. There must be one entry per station number you need to access.

> \<station-number\>500\</station-number\>

> Refer to the KAAJEE Installation Guide for detailed instructions as needed.

4.  Update the weblogic.xml file in VistAMigrate/WEB-INF to set the KAAJEE_CONTROLLER role principal name to the username of a WebLogic Administrator user (or the WebLogic boot user). KAAJEE requires this to function correctly.

> ![](vpfs-version-1-2-install-guide/067.png)Look for a \<security-role-assignment\> with a \<role-name\> of KAAJEE_CONTROLLER. Change the \<principal-name\> to the name of a WebLogic Administrator user.

> \<principal-name\>weblogic\</principal-name\>

> ![](vpfs-version-1-2-install-guide/068.png)Look for a \<run-as-role-assignment\> with a \<role-name\> of KAAJEE_CONTROLLER. Change the \<run-as-principal-name\> to the name of a WebLogic Administrator user.

> \<run-as-principal-name\>weblogic\</run-as-principal-name\>

5.  Update the VistaMigrateResources.properties file in VistAMigrate/WEB-INF/classes to specify the location of the migration root folder.

> ![](vpfs-version-1-2-install-guide/069.png)Set the migrationRootPath property to the path of the migration root folder created in section 7.4.

> migrationRootPath=/home/bea/vistaMigrate

> Note: If you are running VistAMigrate on a Windows server, you need to use double backslashes in the migrationRootPath property. For example, if you have created the migration root directory at C:\vistaMigrate, this property would be:

> migrationRootPath=C:\\vistaMigrate

6.  (Optional) If you are going to deploy VistAMigrate as an .ear file, freshen the VistAMigrate

> .ear file to update the changed files.

> \# jar uf vistaMigrate.ear \*

#### Steps to Deploy

> VistAMigrate can be deployed as either an .ear file or an “exploded” deployment. To use the exploded deployment option, the contents of the temporary directory used above must be copied

7.  VPFS VistAMigrate Installation

> to the server. To use the .ear file deployment option, the vistaMigrate.ear file may either be on the server or uploaded during deployment.

> The VistAMigrate application must be deployed to a standalone managed server instead of the cluster to access server specific resources.

> Complete these steps to deploy the application:

1.  Using a web browser, connect to the WebLogic Server console.
2.  Sign in as the administration user and supply the appropriate password.
3.  From the left panel, expand the Deployments node and click the Applications link.
4.  From the main panel, click the Deploy a new Application… link.
5.  Select the archive for this application. Do one of the following:
    1.  Navigate to the location of the vistaMigrate.ear file or root directory of the exploded .ear file. (WebLogic will recognize the root directory of an exploded .ear file as an application.)
    2.  Click the upload your file(s) link.

> Click Browse… button and navigate to where the VistAMigrate .ear file is located. Select the VistAMigrate .ear file and click the Open button.

> Click Upload.

6.  Select the VistAMigrate application (.ear file or root directory) and click Target Application.
7.  Select targets for this application:
    1.  Click the radio button next to the server on which the application will be hosted. (Do *not*

> specify the cluster.)

2.  Click Continue.
8.  Review your choices and click Deploy.

> Deployment status: During the process of the deployment, the screen will refresh itself periodically until the application is deployed.

### Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Logging for VistAMigrate is configured in the log4j configuration file, log4j.xml. See <u>section 6.5</u> for additional details.

> Log4j is configured by defining \<appender\>s and \<logger\>s. The default appenders and loggers for VistAMigrate are defined in the log4j_VistAMigrate.xml file supplied with the VPFS distribution package. These can be copied into the correct locations in an existing log4j configuration file.

> The default VistAMigrate log file is called vistaMigrate.log. See section <u>6.5</u> for additional details.

8.  Post-Installation Steps

## Post-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vpfs-version-1-2-install-guide/070.png)The interfaces that may require post-installation steps to integrate with VPFS are: VistALink

> ![](vpfs-version-1-2-install-guide/071.png)KAAJEE

> The post-installation steps for each interface are detailed in the following sections.

### Post Interface Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides the steps that must be performed to integrate VPFS with the interfaces.

#### Connecting to VistA Sites

> Ensure VistALink connectors have been created for the sites you need access to. VistALink requires an entry in the VistALink connectorConfig.xml for each VistA site to which you will connect to. Make sure to have the IP, port, access and verify codes for each site handy before you start adding new connections.

> Be sure to include station numbers for any added VistA sites to the KAAJEE configuration file (kaajeeConfig.xml) also. This file is in VistAMigrate/WEB-INF/config for VistAMigrate and in VPFS/WEB-INF/config for VPFS.

> .

8.  Testing the VPFS Application Installation

## Testing the VPFS Application Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Testing the Installation of the VPFS Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Using a web browser, connect to the VPFS application through the proxy server or load balancer that points marshals’ connections to the cluster.

> http://*\[host\]*:*\[port\]*/vpfs

2.  After pressing *Sign In with VA PV Card*, you will be prompted to choose a certificate and for your PIV Pin. Upon pressing *Proceed*, you will be authenticated automatically.
3.  Upon authentication with the system, you will see the VPFS welcome page, as shown in the following figure.

> ![Figure 9-1. Welcome to the Veterans Personal Finance System Page](vpfs-version-1-2-install-guide/072.png)

*Figure 9-1. Welcome to the Veterans Personal Finance System Page*

4.  Click on Start VPFS to start the application.

### Testing the Installation of the VistAMigrate Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5.  Using a web browser, connect to the VistAMigrate application through the proxy server or load balancer that points marshals’ connections to the cluster.

> http://*\[host\]*:*\[port\]*/vistaMigrate

9.  Testing the VPFS Application Installation
    1.  KAAJEE will prompt you for a VistA access and verify code pair.
    2.  Upon authentication with the VistA system, you will see the VistAMigrate Pick Project page, as shown in the following figure.

![Figure 9-2. VistAMigrate Pick Project Page](vpfs-version-1-2-install-guide/073.png)

*Figure 9-2. VistAMigrate Pick Project Page*

### Testing the SMTP Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section will show how to test the SMTP connection. The SMTP connection is used to process the automated e-mails that are generated as part of the VPFS application.

3.  Log on to any server in the cluster.
4.  Open command prompt.
5.  Telnet to the SMTP server via port 25.

> \$ telnet smtp.\[domain\].gov 25

6.  You will see the following:

> Trying 127.0.0.1...

> Connected to smtp.\[domain\].gov Escape character is '^\]'

7.  At the blank line type the following:

> EHLO localhost

> .

8.  To test sending e-mail type the following. A period (.) will end the message and send the message to the rcpt (recipient) list. To send multiple messages, enter each e-mail address one per line with rcpt to: command repeated.

> MAIL FROM: [<u>abc@myserver.com</u>](mailto:abc@myserver.com) RCPT TO: [<u>xyz@myserver.com</u>](mailto:xyz@myserver.com)

9.  Testing the VPFS Application Installation

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><p>DATA</p>
<p>Subject: Testing</p>
<p>&lt;cr&gt; (This signifies that a blank line is separating the header from the body of the message.)</p>
<p>Test message</p>
<p>. (A period at the beginning of a line signifies the end of the message.)</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Note:</strong></p>
</blockquote></td>
<td>You should get a successful indication and a message should be delivered to recipient user.</td>
</tr>
</tbody>
</table>

## Rolling Back the VPFS Application Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Using WebLogic Console Deployments section: Click the checkbox next to the current deployment of the VPFS and click the Stop button above or below.
2.  Click the checkbox next to the previous deployment of VPFS and click the Start button above or below.
3.  You may need to click the Update button above or below once this is done.

> Appendix A*.* References

# Appendix A. References


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [About This Document](#about-this-document)
    - [Purpose](#purpose)
    - [Audience](#audience)
    - [Conventions Used in this Document](#conventions-used-in-this-document)
  - [Overview](#overview)
    - [Application Modernization Project](#application-modernization-project)
  - [Pre-Requisites/Conditions](#pre-requisitesconditions)
    - [Target Installation Environment](#target-installation-environment)
    - [Software Tools](#software-tools)
    - [Dependencies](#dependencies)
  - [Upgrading a Prior Installation](#upgrading-a-prior-installation)
  - [Dependency Installation Notes](#dependency-installation-notes)
    - [Interface Installation Notes](#interface-installation-notes)
  - [Database Setup](#database-setup)
    - [Using an Installation Log](#using-an-installation-log)
    - [Preparing the Installation Scripts](#preparing-the-installation-scripts)
    - [Creating VistAMigrate Schema](#creating-vistamigrate-schema)
    - [Creating Objects for VistAMigrate User](#creating-objects-for-vistamigrate-user)
    - [Creating VPFS Schema](#creating-vpfs-schema)
    - [Granting Access to SDS Objects for VPFS](#granting-access-to-sds-objects-for-vpfs)
    - [Creating Objects for VPFS User](#creating-objects-for-vpfs-user)
    - [Creating Jobs for the Stored Procedures](#creating-jobs-for-the-stored-procedures)
    - [Creating VPFS Project in VistAMigrate](#creating-vpfs-project-in-vistamigrate)
  - [VPFS Application Installation](#vpfs-application-installation)
    - [Signing into the WebLogic Server Administration Console](#signing-into-the-weblogic-server-administration-console)
    - [Creating a JDBC Connection Pool for VPFS](#creating-a-jdbc-connection-pool-for-vpfs)
    - [Creating a Data Source for the Connection Pool](#creating-a-data-source-for-the-connection-pool)
    - [Deploying the VPFS Application](#deploying-the-vpfs-application)
    - [Logging](#logging)
  - [VPFS VistAMigrate Installation](#vpfs-vistamigrate-installation)
    - [Logging in to the WebLogic Server Administration Console](#logging-in-to-the-weblogic-server-administration-console)
    - [Creating a JDBC Connection Pool for VistAMigrate](#creating-a-jdbc-connection-pool-for-vistamigrate)
    - [Creating a Data Source for the Connection Pool](#creating-a-data-source-for-the-connection-pool-1)
    - [Root and Code Folders Setup](#root-and-code-folders-setup)
    - [Deploying the VistAMigrate Application](#deploying-the-vistamigrate-application)
    - [Logging](#logging-1)
  - [Post-Installation Steps](#post-installation-steps)
    - [Post Interface Installation Steps](#post-interface-installation-steps)
  - [Testing the VPFS Application Installation](#testing-the-vpfs-application-installation)
    - [Testing the Installation of the VPFS Application](#testing-the-installation-of-the-vpfs-application)
    - [Testing the Installation of the VistAMigrate Application](#testing-the-installation-of-the-vistamigrate-application)
    - [Testing the SMTP Connection](#testing-the-smtp-connection)
  - [Rolling Back the VPFS Application Install](#rolling-back-the-vpfs-application-install)
- [Appendix A. References](#appendix-a-references)
    - [VPFS Project Documents](#vpfs-project-documents)
    - [Non-VPFS Project Documents](#non-vpfs-project-documents)
- [Appendix B. Acronyms and Abbreviations](#appendix-b-acronyms-and-abbreviations)

### VPFS Project Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Final Detailed Overall System Architecture Document for the Veterans Personal Finance System (VPFS)
> *776-C21282 VPFS Software Design Document (SDD)*

### Non-VPFS Project Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *KAAJEE Installation Guide SDS API Installation Guide VistALink Installation Guide*
> *Person Service Lookup System Administrator / Developer Guide Patient Service Installation Guide*
> *Electronic Signature Installation Guide*
> Appendix B*.* Acronyms and Abbreviations

# Appendix B. Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>API</td>
<td><blockquote>
<p>Application Program Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td>C&amp;A</td>
<td><blockquote>
<p>Certification and Accreditation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CHISS</td>
<td><blockquote>
<p>Common Health Information Security Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CI</td>
<td><blockquote>
<p>Configuration Item</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>COTS</td>
<td><blockquote>
<p>Commercial Off The Shelf</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CPU</td>
<td><blockquote>
<p>Central Processing Unit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CRUD</td>
<td><blockquote>
<p>Create, Read, Update, Delete</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DAS</td>
<td><blockquote>
<p>Delegated Administration Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DBMS</td>
<td><blockquote>
<p>Database Management System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DHTML</td>
<td><blockquote>
<p>Dynamic HyperText Markup Language</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DN</td>
<td><blockquote>
<p>Distinguished Name</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DOS</td>
<td><blockquote>
<p>Disk Operating System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DSS</td>
<td><blockquote>
<p>Decision Support System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>EAR</td>
<td><blockquote>
<p>Enterprise Archive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>EJB</td>
<td><blockquote>
<p>Enterprise Java Bean</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ERD</td>
<td><blockquote>
<p>Entity Relationship Diagram</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ETL</td>
<td><blockquote>
<p>Extract, Transform, Load</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FK</td>
<td><blockquote>
<p>Foreign Key</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FTP</td>
<td><blockquote>
<p>File Transfer Protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HIPAA</td>
<td><blockquote>
<p>Health Insurance Portability and Accountability Act</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HIS</td>
<td><blockquote>
<p>Health Information System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HL7</td>
<td><blockquote>
<p>Health Level 7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HTML</td>
<td><blockquote>
<p>HyperText Markup Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HTTP</td>
<td><blockquote>
<p>HyperText Transfer Protocol</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HTTPS</td>
<td><blockquote>
<p>HyperText Transfer Protocol Secure</p>
</blockquote></td>
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
<th>ICN</th>
<th><blockquote>
<p>Integration Control Number</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IIG</td>
<td><blockquote>
<p>Impact Innovations Group</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IP</td>
<td><blockquote>
<p>Internet Protocol</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IFCAP</td>
<td><blockquote>
<p>Integrated Patient Funds Distribution, Control Point Activity, Accounting and Procurement</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IPF</td>
<td><blockquote>
<p>Integrated Patient Funds</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>J2EE</td>
<td><blockquote>
<p>Java TM 2 Platform, Enterprise Edition</p>
</blockquote></td>
</tr>
<tr class="even">
<td>JAAS</td>
<td><blockquote>
<p>Java Authentication and Authorization Service</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Appendix B*.* Acronyms and Abbreviations

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>JCA</td>
<td><blockquote>
<p>Java Connector Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td>JDBC</td>
<td><blockquote>
<p>Java Database Connectivity</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>JDK</td>
<td><blockquote>
<p>Java Development Kit</p>
</blockquote></td>
</tr>
<tr class="even">
<td>JMS</td>
<td><blockquote>
<p>Java Message Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>JNDI</td>
<td><blockquote>
<p>Java Naming Directory Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td>JSP</td>
<td><blockquote>
<p>Java Server Page</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>JSTL</td>
<td><blockquote>
<p>Java Standard Tag Library</p>
</blockquote></td>
</tr>
<tr class="even">
<td>JTA</td>
<td><blockquote>
<p>Java Transaction API</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>JVM</td>
<td><blockquote>
<p>Java Virtual Machine</p>
</blockquote></td>
</tr>
<tr class="even">
<td>KAAJEE</td>
<td><blockquote>
<p>Kernel Authentication and Authorization for J2EE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>LAN</td>
<td><blockquote>
<p>Local Area Network</p>
</blockquote></td>
</tr>
<tr class="even">
<td>LDAP</td>
<td><blockquote>
<p>Lightweight Directory Access Protocol</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>LLC</td>
<td><blockquote>
<p>Limited Liability Corporation</p>
</blockquote></td>
</tr>
<tr class="even">
<td>M</td>
<td><blockquote>
<p>MUMPS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAC</td>
<td><blockquote>
<p>Media Access Controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td><blockquote>
<p>Massachusetts Universal Multi Programming System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MVC</td>
<td><blockquote>
<p>Model View Controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OCI</td>
<td><blockquote>
<p>Oracle Call Interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OCS</td>
<td><blockquote>
<p>Office of Cyber Security</p>
</blockquote></td>
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
<th>PFC</th>
<th><blockquote>
<p>Patient Funds Clerk</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PFCS</td>
<td><blockquote>
<p>Patient Funds Clerk Supervisor</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PATS</td>
<td><blockquote>
<p>Patient Advocate Tracking System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PFOP</td>
<td><blockquote>
<p>Personal Funds of Patients</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PK</td>
<td><blockquote>
<p>Primary Key</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PKI</td>
<td><blockquote>
<p>Public Key Infrastructure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PM</td>
<td><blockquote>
<p>Project Manager</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>QA</td>
<td><blockquote>
<p>Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="even">
<td>QCI</td>
<td><blockquote>
<p>Quality Control Inspector</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>QCP</td>
<td><blockquote>
<p>Quality Control Plan</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RBAC</td>
<td><blockquote>
<p>Role Based Access Control</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RDBMS</td>
<td><blockquote>
<p>Relational Database Management System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RO</td>
<td><blockquote>
<p>Regional Office</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RPC</td>
<td><blockquote>
<p>Remote Procedure Call</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SCM</td>
<td><blockquote>
<p>Software Configuration Management</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Appendix B*.* Acronyms and Abbreviations

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SCMP</td>
<td><blockquote>
<p>Software Configuration Management Plan</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SD&amp;D</td>
<td><blockquote>
<p>System Design &amp; Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SDD</td>
<td><blockquote>
<p>System Design Document</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SDK</td>
<td><blockquote>
<p>Software Development Kit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SDL</td>
<td><blockquote>
<p>Software Development Library</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SDLC</td>
<td><blockquote>
<p>Software Development Life Cycle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SDS</td>
<td><blockquote>
<p>Standard Data Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SEPG</td>
<td><blockquote>
<p>Software Engineering Process Group</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SI</td>
<td><blockquote>
<p>System Implementation</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SME</td>
<td><blockquote>
<p>Subject Matter Expert</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SOAP</td>
<td><blockquote>
<p>Simple Object Access Protocol</p>
</blockquote></td>
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
<th>SOW</th>
<th><blockquote>
<p>Statement of Work</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SQA</td>
<td><blockquote>
<p>Software Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SQAP</td>
<td><blockquote>
<p>Software Quality Assurance Plan</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SQL</td>
<td><blockquote>
<p>Standard Query Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRS</td>
<td><blockquote>
<p>Software Requirements Specification</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SSL</td>
<td><blockquote>
<p>Secure Sockets Layer</p>
</blockquote></td>
</tr>
<tr class="even">
<td>TBD</td>
<td><blockquote>
<p>To Be Determined</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>TLD</td>
<td><blockquote>
<p>Tag Descriptor Library</p>
</blockquote></td>
</tr>
<tr class="even">
<td>URI</td>
<td><blockquote>
<p>Uniform Resource Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>URL</td>
<td><blockquote>
<p>Uniform Resource Locator</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA</td>
<td><blockquote>
<p>Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VAX</td>
<td><blockquote>
<p>VAX (Virtual Address eXtension) is an established line of mid-range server computers from the Digital Equipment Corporation (DEC).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VHA</td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VistA</td>
<td><blockquote>
<p>Veterans Information Systems Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VMS</td>
<td><blockquote>
<p>Virtual Machine System (operating system for VAX computers)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VPFS</td>
<td><blockquote>
<p>Veterans Personal Finance System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>WAN</td>
<td><blockquote>
<p>Wide Area Network</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>WAR</td>
<td><blockquote>
<p>Web Archive</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XDE</td>
<td><blockquote>
<p>Extensible Development Environment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XHTML</td>
<td><blockquote>
<p>Extensible HyperText Markup Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XML</td>
<td><blockquote>
<p>Extensible Markup Language</p>
</blockquote></td>
</tr>
</tbody>
</table>