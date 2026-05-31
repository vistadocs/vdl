---
title: VistALink Version 1.6 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: null
app_code: XOBV
app_name: VistALink
section: INF
app_status: active
pkg_ns: XOBV
patch_ver: 1.6
patch_id: XOBV*1.6
group_key: XOBV:XOBV:1.6
file_numbers:
- '3.5'
- '18'
- '200'
- '8989.3'
security_keys:
- CTRL
menu_options: 2
description: '- Revision History - Contents - Tables - Figures - Orientation - Document Overview - Introduction - About VistALink - [WebLogic Updates...'
audience: System administrators performing installation
keywords: []
page_count: 0
word_count: 17203
section_count: 31
table_count: 53
figure_count: 0
appendix_count: 2
has_toc: false
is_stub: false
pub_date: July 2020
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Infrastructure/VistALink/vistalink_1_6_ig.docx
pdf_url: https://www.va.gov/vdl/documents/Infrastructure/VistALink/vistalink_1_6_ig.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=163
audit_applied: '2026-05-31'
master_source: VistALink Version 1.6 Installation Guide
master_pub_date: July 2020
consolidated_from: 3 versions
prior_versions:
- VistALink Version 1.5 Installation Guide
- VistaLink Version 1.6.7 Installation Guide
consolidated_title: vistalink installation guide
---

![](vistalink-version-1-6-installation-guide/001.png)

VISTALINKINSTALLATION GUIDE

July 2020

Office of Information and Technology

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Contents](#contents)
- [Tables](#tables)
- [Figures](#figures)
- [Orientation](#orientation)
  - [Document Overview](#document-overview)
- [Introduction](#introduction)
  - [About VistALink](#about-vistalink)
    - [WebLogic Updates Project](#weblogic-updates-project)
  - [VistALink Version Compatibility](#vistalink-version-compatibility)
    - [J2EE/WebLogic Version Compatibility](#j2eeweblogic-version-compatibility)
    - [M Listener Backwards/Forwards Version Compatibility](#m-listener-backwardsforwards-version-compatibility)
  - [Known Issues and Limitations](#known-issues-and-limitations)
- [Installation Overview](#installation-overview)
  - [Restrictions](#restrictions)
  - [Assumptions about Installers](#assumptions-about-installers)
  - [Separation of M and J2EE Server Installation Procedures](#separation-of-m-and-j2ee-server-installation-procedures)
  - [VistALink Distribution ZIP File \<DIST FOLDER\> Structure (new structure)](#vistalink-distribution-zip-file-dist-folder-structure-new-structure)
  - [M Routine Checksum Information](#m-routine-checksum-information)
  - [Installation Synopsis](#installation-synopsis)
    - [VistA/M Server](#vistam-server)
    - [J2EE Application Server](#j2ee-application-server)
- [VistA/M Server Installation Procedures](#vistam-server-installation-procedures)
  - [Preparation](#preparation)
    - [Software Installation Time](#software-installation-time)
    - [Virgin Installations](#virgin-installations)
    - [System Requirements](#system-requirements)
    - [System Preparation](#system-preparation)
    - [HFS and Null Devices](#hfs-and-null-devices)
    - [Deletion of Obsolete File \#18](#deletion-of-obsolete-file-18)
  - [Install VistALink KIDS Distribution](#install-vistalink-kids-distribution)
    - [Preliminary Steps](#preliminary-steps)
    - [Stop VistALink System Processes](#stop-vistalink-system-processes)
    - [Install Kernel Installation and Distribution System (KIDS) Distribution](#install-kernel-installation-and-distribution-system-kids-distribution)
  - [(Optional) Configure VistALink Listener](#optional-configure-vistalink-listener)
    - [Do I Need to Configure Listeners As Part of the VistALink Installation?](#do-i-need-to-configure-listeners-as-part-of-the-vistalink-installation)
    - [Listener Introduction](#listener-introduction)
    - [Recommended VistALink Ports (all operating systems)](#recommended-vistalink-ports-all-operating-systems)
    - [OS-Based Listener Configuration for Caché/VMS Systems](#os-based-listener-configuration-for-cachévms-systems)
    - [OS-Based Listener Configuration for Caché/Linux Systems](#os-based-listener-configuration-for-cachélinux-systems)
    - [M-Based Listener Configuration for Caché/NT (Windows) Systems](#m-based-listener-configuration-for-cachént-windows-systems)
  - [(Optional) Verify Listener Connectivity](#optional-verify-listener-connectivity)
    - [Telnet Test](#telnet-test)
    - [VistALink J2SE SwingTester Sample Application Test (optional)](#vistalink-j2se-swingtester-sample-application-test-optional)
  - [(Optional) Configure Connector Proxy User(s) for J2EE Access](#optional-configure-connector-proxy-users-for-j2ee-access)
    - [Connector Proxy Overview](#connector-proxy-overview)
    - [How to Create Connector Proxy User Kernel Accounts](#how-to-create-connector-proxy-user-kernel-accounts)
  - [Installation Back-Out/Roll-Back Procedure](#installation-back-outroll-back-procedure)
    - [Reinstall v1.5](#reinstall-v15)
    - [Optional Deletions of v1.6-Only Components](#optional-deletions-of-v16-only-components)
- [Oracle WebLogic Application Server: Installation Procedures](#oracle-weblogic-application-server-installation-procedures)
  - [Overview](#overview)
    - [Adapter Deployment Descriptors](#adapter-deployment-descriptors)
    - [VistALink 1.6.1 Adapter Changes](#vistalink-161-adapter-changes)
    - [VistALink Adapters and Classloading](#vistalink-adapters-and-classloading)
  - [Preparation](#preparation-1)
    - [Software Installation Time (Varies)](#software-installation-time-varies)
    - [System Requirements](#system-requirements-1)
    - [Deployer Requirements](#deployer-requirements)
    - [Obtain the VistALink Distribution File](#obtain-the-vistalink-distribution-file)
    - [Obtain M Connector Proxy User and Listener Information](#obtain-m-connector-proxy-user-and-listener-information)
  - [Upgrading a WebLogic 8.1 Domain w/Existing VistALink Adapters](#upgrading-a-weblogic-81-domain-wexisting-vistalink-adapters)
    - [Back Up Exploded RAR Directories and VistALink Configuration File](#back-up-exploded-rar-directories-and-vistalink-configuration-file)
    - [If Running the Domain Upgrade Wizard](#if-running-the-domain-upgrade-wizard)
  - [WebLogic 10.3.6/12.1.2 Server Configuration](#weblogic-10361212-server-configuration)
    - [Create \<HEV Configuration Folder\>](#create-hev-configuration-folder)
    - [Create/Copy VistALink Configuration File](#createcopy-vistalink-configuration-file)
    - [Place \<HEV Configuration Folder\> on Server Classpath(s)](#place-hev-configuration-folder-on-server-classpaths)
    - [Create/Update Server log4j Configurations](#createupdate-server-log4j-configurations)
    - [Server JVM Argument: gov.va.med.environment.production](#server-jvm-argument-govvamedenvironmentproduction)
    - [Server JVM Argument: gov.va.med.environment.servertype](#server-jvm-argument-govvamedenvironmentservertype)
  - [## WebLogic 10.3.6/12.1.2: Install the Standalone Console EAR (Admin Server)](#weblogic-10361212-install-the-standalone-console-ear-admin-server)
    - [Copy Console EAR file](#copy-console-ear-file)
    - [Deploy Console EAR](#deploy-console-ear)
    - [Access Standalone VistALink Console](#access-standalone-vistalink-console)
    - [Check Configuration Editor Access to Configuration File](#check-configuration-editor-access-to-configuration-file)
  - [Deploy Shared J2EE Libraries (Production Domains Only)](#deploy-shared-j2ee-libraries-production-domains-only)
  - [Create/Deploy VistALink Adapter(s)](#createdeploy-vistalink-adapters)
    - [Add Connector Entry to VistALink Configuration File](#add-connector-entry-to-vistalink-configuration-file)
    - [Create New or Update Existing Adapter Folder on Admin Server](#create-new-or-update-existing-adapter-folder-on-admin-server)
    - [Back Up Deployment Descriptors](#back-up-deployment-descriptors)
    - [Copy New 1.6 Files](#copy-new-16-files)
    - [Update Deployment Descriptors](#update-deployment-descriptors)
    - [Deploy Adapter](#deploy-adapter)
    - [Monitor Adapter in VistALink Console](#monitor-adapter-in-vistalink-console)
  - [Troubleshooting](#troubleshooting)
  - [Test with J2EE Sample Application (Development Systems Only)](#test-with-j2ee-sample-application-development-systems-only)
    - [Deploy the Sample Web Application](#deploy-the-sample-web-application)
- [Rollback Instructions](#rollback-instructions)
- [Appendix A: Installing and Running the J2SE Sample Apps](#appendix-a-installing-and-running-the-j2se-sample-apps)
  - [Overview](#overview-1)
  - [Installation Instructions](#installation-instructions)
- [Appendix B: DSM/VMS-Specific Install Information](#appendix-b-dsmvms-specific-install-information)
  - [Operating System Requirements](#operating-system-requirements)
  - [Global Protection](#global-protection)
  - [Listener Management for Caché/VMS Systems](#listener-management-for-cachévms-systems)
- [Glossary](#glossary)
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 50%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/08/20</td>
<td>XOBV*1.6*5 – VistALink Version 1.6.1 release</td>
<td><blockquote>
<p>Health Product Support Tier 3 Sustainment team.</p>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/24/19</td>
<td>XOBV/S*1.6*4 N/A Changes</td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/03/10</td>
<td>VistALink Version 1.6 release.</td>
<td><blockquote>
<p>Product Development Services Security Program VistALink development team.</p>
<p>Albany, NY OIFO:</p>
</blockquote>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul>
<blockquote>
<p>Bay Pines, FL OIFO:</p>
</blockquote>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul>
<blockquote>
<p>Oakland, CA OIFO:</p>
</blockquote>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul>
<blockquote>
<p>Technical Writer—REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>
<span id="_Toc280220931" class="anchor"></span>Table i. Revision History

# Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*This page is left blank intentionally.*

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Document Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides information for installing the VistALink 1.6.1 resource adapter and Mumps (M)-side listener. Its intended audience includes Java 2 Enterprise Edition (J2EE) application server administrators, Information Resource Management (IRM) Information Technology (IT) Specialists at Department of Veterans Affairs (VA) facilities, and developers of Java applications requiring communication with Veterans Health Information Systems and Technology Architecture (VistA)/M (Massachusetts General Hospital Utility Multi-Programming System) systems.

System administrators and developers should use this document in conjunction with the *VistALink 1.6 System Management Guide,* which contains detailed information on the Java 2 Platform, Enterprise Edition (J2EE) application server management, institution mapping, the VistALink console, M listener management, and VistALink security, logging, and troubleshooting.

Terminology

The term *resource adapter* is often shortened in this guide to "adapter*,*" and is also used interchangeably with the term *connector*.

Text Conventions

File names and directory names are set off from other text using bold font (e.g., config.xml). Bold is also used to indicate Graphical User Interface (GUI) elements, such as tab, field, and button names (

e.g., "press Delete").

All caps are used to indicate M routines and option names (e.g., XMINET). All caps used inside angle brackets indicate file names to be supplied by the user. Example:

> \<JAVA_HOME\>\bin\java -Dlog4j.configuration=file:///c:/localConfigs/mylog4j.xml

Names for Java objects, methods, and variables are indicated by Courier font. Snapshots of computer displays also appear in Courier, surrounded by a border:

Select Installation Option: LOAD a Distribution

Enter a Host File: XOB_1_6_Bxx.KID

In these examples, the response that the user enters at a prompt appears in bold font:

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME;80;999 \<Enter\> TELNET PORT

Boldface text is also used in code and file samples to indicate lines of particular interest, discussed in the preceding text:

> \<?xml version="1.0"?\>

> \<weblogic-connector xmlns="http://www.bea.com/ns/weblogic/90" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.bea.com/ns/weblogic/90

> http://www.bea.com/ns/weblogic/90/weblogic-ra.xsd"\>

> \

- *VistALink 1.6 Developer Guide*: Contains detailed information about workstation setup, re-authentication, institution mapping, executing requests, VistALink exceptions, Foundations Library utilities, and other topics pertaining to writing code that uses VistALink.
- *VistALink 1.6 Release Notes*: Lists all new features included in the VistALink 1.6 release.

VistALink 1.6 end-user documentation and software can be downloaded any of the anonymous.software directories on the Office of Information & Technology (OI&T) File Transfer Protocol (FTP) download sites:

- Preferred Method REDACTED

> This method transmits the files from the first available FTP server.

- Albany OIFO REDACTED
- Hines OIFO [REDACTED](ftp://ftp.fo-hines.med.va.gov/)
- Salt Lake City OIFO REDACTED

The documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

|                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/004.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

*This page is left blank intentionally.*

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## About VistALink

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink resource adapter is a transport layer that provides communication between Health*<u>e</u>*Vet- Veterans Information Systems and Technology Architecture (VistA) Java applications and VistA/M servers, in both client-server and n-tier environments. It is a runtime and development tool that allows java applications to execute remote procedure calls (RPCs) on the VistA/M system and retrieve results, synchronously. VistALink is also referred to as VistALink J2M.

VistALink consists of Java-side adapter libraries and an M-side listener:

- The adapter libraries use the J2EE Connector Architecture (J2CA) 1.7 specification to integrate Java applications with legacy systems.
- The M listener process receives and processes requests from client applications.
- Java applications can call Remote Procedure Calls (RPCs) on the M server, executing RPC Broker RPCs on the M server without modification.

The previous version of VistALink, 1.5, was released in June of 2006, and provided project developers with J2EE and Java Platform, Standard Edition (J2SE) application connectivity to VistA/M servers. It was designed specifically for J2EE 1.3 application servers (e.g., WebLogic 8.1).

### WebLogic Updates Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In support of the Department of Veterans Affairs Information Technology application Modernization effort, the three applications Fat-client Kernel Authentication and Authorization (FatKAAT), Kernel Authentication and Authorization for the Java 2 Enterprise Edition (KAAJEE) and VistALink have been developed. Based on the direction of the Technical Review Model (TRM) and to support applications that upgrade to the new WebLogic Server versions. 10.3.6/12.1.2, this project is required. The scope of the project is to upgrade these three applications to work with the WebLogic Server 10.3.6/12.1.2.

## VistALink Version Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### J2EE/WebLogic Version Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant changes to the J2CA specification were made in J2EE 1.7, and additional changes in WebLogic classes (e.g., console extensions) were also made for WebLogic 10.3.6/12.1.2. As a result, some components of VistALink 1.6.1 are not compatible with WebLogic 10.3.6/12.1.2. All components of VistALink 1.6.1 are compatible with WebLogic 10.3.6/12.1.2.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistALink version</strong></th>
<th><strong>J2EE 1.4+<br />
WebLogic 9.x, 10.x, 11g</strong></th>
<th><strong>J2EE 1.7<br />
WebLogic 10.3.6/12.1.2</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1.6.1</td>
<td><strong>yes</strong></td>
<td><em>no</em></td>
</tr>
<tr class="even">
<td>1.6.1</td>
<td><em>No</em></td>
<td><strong>Yes</strong></td>
</tr>
</tbody>
</table>

### M Listener Backwards/Forwards Version Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 1.5 and 1.6 M listeners are backwards and forwards compatible, as follows:

- 1.6 clients cannot execute requests against 1.5 M listeners
- 1.5 clients can execute requests against 1.6 M listeners
- 1.0 clients can execute requests against 1.5 and 1.6 listeners

## Known Issues and Limitations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>VistALink console plug-in on WebLogic v10.0</u>: In WebLogic v10.0, there is no navigation link for the VistALink console extension in the WebLogic console navigation tree (left hand side of the console). A possible bug has been reported to Oracle (formerly BEA).

> Workaround: An alternate route to the VistALink console is to click on the top link of the navigation tree, which is the domain name. On the right-hand page, one of the tabs is 'VistALink J2M'.

- <u>VistALink console plug-in on WebLogic v10.3</u>: In WebLogic v10.3, the navigation link and tab link to access the VistALink console extension may not be displayed in the WebLogic console on some systems, upon subsequent logins after initial deployment, leaving the console extension inaccessible.

> Workaround: An alternative version of the VistALink console has been provided as a standalone EAR. Use the standalone EAR version of the VistALink console for WebLogic 10.3 (and any other future version of WebLogic that has the same problem).

- <u>Anomaly: Unexplained Production/Test Mismatch Error During Testing</u>: One unexplained anomaly was reported during testing with CHDR 2.0. VistALink connections to VistA sites began failing on one of the 6 CHDR WebLogic servers, with the logger error being a production/test mismatch, where VistALink requests were incorrectly reporting that the CHDR server in question was not a production server. The setting used by VistALink to determine if a given WebLogic server is test or production is a server-specific Java Virtual Machine (JVM) configuration argument configured by the data center. The argument appeared to be set correctly on the server in this case.  
    
  The anomaly has occurred once on one server, after 5 months of running in production. The impact was that the affected WebLogic server could not access production VistA servers, and that each failed connection attempt added an error to each VistA site's error log. After a number of server restarts, and examinations / possible updates to the server configuration, the problem resolved itself. Without a deeper investigation, it was not possible to isolate which system component was responsible for the observed failure.  
    
  Workaround: None.

> *This page is left blank intentionally.*

# Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Restrictions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.6.1 has been tested and is supported on Oracle WebLogic Server 10.3.6/12.1.2, only.

## Assumptions about Installers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These instructions assume that installers will have a basic working knowledge of J2EE and M systems, including application deployments.

## Separation of M and J2EE Server Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides VistALink installation instructions. Because VistALink consists of modules for both a Java 2 Enterprise Edition (J2EE) application server and a VistA/M server, separate sets of instructions are provided to set up, configure, and install the appropriate module(s) on each type of server.

At production facilities in particular, different administrators may be responsible for the two server types (M and J2EE); thus, separate parts of the installation process. At such sites, completing both sides of a VistALink installation will require ongoing communication and coordination between the two types of system administrators. Developers, on the other hand, may be responsible for both sides of the installation process, M *and* J2EE.

Though the VistA/M server instructions are presented first in this document, the order is arbitrary—most of the steps for the two servers are not dependent on each other.

## VistALink Distribution ZIP File \<DIST FOLDER\> Structure (new structure)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink distribution ZIP file contains:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Directory Structure of the VistALink 1.6 Distribution ZIP File</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>/vlj-1.6.1.xxx</strong></p>
<p>      /app-j2ee               Application components for J2EE installation</p>
<p>          /configFile-j2ee    sample gov.va.med.vistalink.connectorConfig.xml<br />
configuration file</p>
<p>          /console-ext        Console plug-ins and standalone EAR version</p>
<p>          /Rar-Dev-Template   RAR for development systems</p>
<p>          /Rar-Prod-Template  RAR for production systems</p>
<p>          /sample             J2EE sample application</p>
<p>          /shared-lib         shared libraries for production systems</p>
<p>      /javadoc                javadoc for public java-side VistALink APIs</p>
<p>      /lib-deprecated         contains supporting jar no longer needed in most<br />
cases</p>
<p>      /log4j                  configuration file examples, VistALink logger<br />
spreadsheet</p>
<p>      /m                      KIDS distribution containing M side of VistALink</p>
<p>      /rpc-doc                extract of RPC Broker documentation on how to write<br />
RPCs</p>
<p>      /samples-J2SE           sample J2SE rich client applications</p></td>
</tr>
</tbody>
</table>

<span id="_Toc519236699" class="anchor"></span>Figure 2‑1. Directory structure of the VistALink 1.6 Distribution ZIP File

## M Routine Checksum Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine name and corresponding checksum value for each M routine contained within the VistALink 1.6.1 software package is provided in the README.TXT file in the \<DIST_FOLDER\>'s root folder.

## Installation Synopsis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA/M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The detailed instructions for installing VistALink on the VistA/M server are presented in chapter 3, "[VistA/M Server Installation Procedures](#vistam-server-installation-procedures)." The general steps for installing VistALink on the VistA/M server are as follows:

1.  Preparation
2.  Install VistALink Kernel Installation and Distribution System (KIDS) Distribution
3.  (Optional) Configure VistALink Listener – not necessary when upgrading an existing configuration
4.  (Optional) Verify Listener Connectivity
5.  (Optional) Configure Connector Proxy User(s) for J2EE Access – not necessary when upgrading an existing configuration

### J2EE Application Server 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The detailed instructions for installing VistALink on the J2EE application server are presented in chapter 4, "[Oracle WebLogic Application Server: Installation Procedures](#_WebLogic_Application_Server_ Instal)." The general steps for installing VistALink on the J2EE application are as follows:

1.  Preparation
2.  Upgrading a Previous Installation
3.  Server Preparation
4.  Install the Console Plug-In or Standalone Console (Admin Server)
5.  Create/Deploy VistALink Adapters
6.  Test with J2EE Sample Application (Development Systems Only)

# VistA/M Server Installation Procedures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The estimated time for the installation of the VistALink KIDS distribution is less than five minutes.

### Virgin Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is not necessary for a previous version of VistALink to be installed on your VistA/M server before you install VistALink 1.6.

### System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Patch Requirements

Before the VistALink 1.6.1 installation, the following packages and patches must be installed:

|                |             |                       |
|----------------|-------------|-----------------------|
| Software   | Version | Patch Information |
| Kernel         | 8.0         | Fully patched.        |
| Kernel Toolkit | 7.3         | Fully patched.        |
| MailMan        | 8.0         | Fully patched.        |
| RPC Broker     | 1.1         | Fully patched.        |
| VA FileMan     | 22.2        | Fully patched.        |

<span id="_2_Software_Retrieval" class="anchor"></span>Table 3‑1. VistA Software Dependencies for VistALink 1.6 installation

#### Operating System Requirements

- Caché/Linux: Caché (version 2014.1.3 or greater)

|     |     |
|-----|-----|
|     |     |

#### VistA/M Server Permissions

Kernel-level programmer access (DUZ(0)="@") is required for installing VistALink 1.6.

On a Virtual Memory System (VMS), the installer must have a VMS account. Installers who are also configuring Transmission Control Protocol (TCP) services for VistALink listeners must also hold sufficient VMS privileges (e.g., SYSPRV).

#### Namespaces

VistALink has been assigned the XOB\* namespace.

#### File and Global Information

VistALink 1.6.1 installs the following files:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 39%" />
<col style="width: 19%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File #</strong></td>
<td><strong>File Name</strong></td>
<td><strong>Root Global</strong></td>
<td><p><strong>FileMan</strong></p>
<p><strong>Protection</strong></p></td>
</tr>
<tr class="even">
<td>18.01</td>
<td>FOUNDATIONS SITE PARAMETERS</td>
<td>^XOB(18.01,</td>
<td>@</td>
</tr>
<tr class="odd">
<td>18.03</td>
<td>VISTALINK LISTENER CONFIGURATION</td>
<td>^XOB(18.03,</td>
<td>@</td>
</tr>
<tr class="even">
<td>18.04</td>
<td>VISTALINK LISTENER STARTUP LOG</td>
<td>^XOB(18.04,</td>
<td>@</td>
</tr>
<tr class="odd">
<td>18.05</td>
<td>VISTALINK MESSAGE TYPE</td>
<td>^XOB(18.05,</td>
<td>@</td>
</tr>
</tbody>
</table>

<span id="_Toc280220933" class="anchor"></span>Table 3‑2. VistALink 1.6 file and global installation

### System Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Global Placement, Mapping, and Translation

VistALink utilizes one VistALink-specific global, ^XOB. For virgin installs, ^XOB should be placed in a database location appropriate for a small, static global, prior to installation.

For M configurations with multiple databases or volume sets, any necessary mapping or translation should be set up at this time as well.

#### Journaling

Because the ^XOB global is relatively static, journaling of this global is not required.

#### Global Protection

|                 |           |     |
|-----------------|-----------|-----|
| Global Name | Caché |     |
| ^XOB            | Owner:    | RWD |
|                 | Group:    | N   |
|                 | World:    | N   |
|                 | Network:  | RWD |

<span id="_Toc280220934" class="anchor"></span>Table 3‑3. Global protection

### HFS and Null Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that you have a Host File Server (HFS) device named "HFS" and a Null device named "NULL" in the DEVICE file (#3.5).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/005.png)</td>
<td><blockquote>
<p><strong>NOTE:</strong> You can have other devices with similar names, but one device is needed whose name or mnemonic is "NULL."</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Deletion of Obsolete File \#18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the original testing of VistALink 1.0, it was discovered that some sites might still have an old Kernel file residing on their system called SYSTEM file (#18). To support virgin installs, VistALink 1.6 still includes steps to check and clean up File \#18.

If your system already has VistALink 1.0 or 1.5 installed, this file has already been removed. Otherwise, if present on your system, you may wish to manually back up and delete SYSTEM file (#18). If this file is on your system at the time of installing VistALink 1.6.1, the environment check will delete the file for you.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/006.png)</td>
<td><blockquote>
<p><strong>NOTE:</strong> This file was created in the early 1980s and was a precursor to the current KERNEL SYSTEM PARAMETERS file (#8989.3). However, it is now obsolete and must be removed from your system before the VistALink package can be installed, because it shares the same number space that VistALink was assigned.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Install VistALink KIDS Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the steps in this section to install VistALink KIDS distribution.

### Preliminary Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Obtain the VistALink KIDS distribution. Download either the entire VistALink ZIP distribution file (XOB_1.6.1.xx.ZIP), or just the standalone KIDS build (XOB_1_6_Bxx.KID) from the anonymous.software directory on any of the OI&T FTP download sites. For 2FA functionality support refer to the XOB_1P6_3.KID build and patch description.

|                                                                                                                |                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/007.png) | NOTE: If you download the entire ZIP distribution, after unzipping it, the KIDS build is located in the unzipped m subfolder. |

2.  FTP (or otherwise transfer) the KIDS build file to the intended VistA/M server.
3.  Log on to your VistA/M server. Select the Programmer Options . . . menu from the Systems Manager Menu option (EVE).

### Stop VistALink System Processes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If a previous version of VistALink is running on your system, stop the VistALink Listener on the server. Follow your normal procedures to stop the VistALink Listener:
  - If your VistALink listener runs via VMS TCP Services, use VMS TCP services to disable the service (listener)
  - If your VistALink listener process runs within Caché (not via VMS TCP services), use the Foundations menu to stop the listener.
- VistALink users must be stopped.

|                                                                                                                |                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/008.png) | NOTE: Check the system status for any XOBVSKT routines that are running (e.g., VistALink Handler). If you find any of these jobs running on the system, notify users to log off or FORCEX the jobs. Active users may get NOSOURCE or CLOBBER errors. |

- While installing this package on the server, do not run any VistALink-based Client/Server software (e.g., Care Management).
- Roll-and-scroll and Remote Procedure Call (RPC) Broker users may remain on the system
- TaskMan does not need to be put into a wait state

|                                                                                                             |                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/009.png) | CAUTION: If you accept a risk of VistALink clients getting a CLOBBER/EDITED error, VistALink/Care Management users may remain running. Otherwise stop all other VistALink/Care Management jobs on the system. |

### Install Kernel Installation and Distribution System (KIDS) Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/010.png) | NOTE: XOB_1_6_Bxx.KID distribution exports 3 VistALink packages/transport globals: XOBU 1.6, XOBV 1.6, and XOBS 1.6. For installation, KIDS works with them as a single unit. When prompted by KIDS to enter a package for loading/installing, always enter XOBU 1.6. Doing this will load/install all 3 packages contained in the distribution, in the correct order. The XOB_1P6_3.KID introduces 2FA functionality support – for installation information see the corresponding patch description. |

1.  Load Distribution.

> Use the KIDS Installation option, Load a Distribution \[XPD LOAD DISTRIBUTION\].

> Enter " XOB_1P6_3.KID" as the name of the Host file (where xx is a build number). If the KIDS file is not in the Kernel's default HFS directory on the host file system, you will need to include the directory path to the file as well.

> The Load a Distribution option will load three transport globals contained within the distribution:

1.  XOBU 1.6 Common files and libraries used by all the XOB\* packages and menu options to manage site parameters/operations
2.  XOBV 1.6 Handles system and RPC requests
3.  XOBS 1.6 M-side security module
2.  Verify Checksums.  
    >   
    > Run the KIDS Installation option, Verify Checksums in Transport Global\[XPD PRINT CHECKSUM\]. This option will ensure the transport global was not corrupted in transit.  
    >   
    > At the Select Select INSTALL NAME: prompt, enter XOBU 1.6. Checksums for all 3 VistALink packages (XOBU 1.6, XOBV 1.6 and XOBS 1.6) will be displayed.

|                                                                                                                |                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/011.png) | NOTE: When executing the Verify Checksums option, the checksums for all three packages (XOBU, XOBV, and XOBS) are displayed. However, due to page feeds, you may need to scroll back up to see the checksums for the first two packages. |

> Follow the example below:

Select Installation Option: Verify Checksums in Transport Global

Select INSTALL NAME: XOBU 1.6\<ENTER\> Loaded from Distribution 4/3/08@09:54:49

=\> Foundations, VistALink and VistALink Security v1.6 ;Created on Apr 03

This Distribution was loaded on Apr 03, 2008@09:54:49 with header of

Foundations, VistALink and VistALink Security v1.6 ;Created on Apr 03, 2008@

09:34:33

It consisted of the following Install(s):

XOBU 1.6 XOBV 1.6 XOBS 1.6

Want each Routine Listed with Checksums: Yes// NO

DEVICE: HOME// TELNET

PACKAGE: XOBU 1.6 Apr 03, 2008 9:58 am PAGE 1

-------------------------------------------------------------------------------

8 Routines checked, 0 failed.

PACKAGE: XOBV 1.6 Apr 03, 2008 9:58 am PAGE 1

-------------------------------------------------------------------------------

16 Routines checked, 0 failed.

PACKAGE: XOBS 1.6 Apr 03, 2008 9:58 am PAGE 1

-------------------------------------------------------------------------------

7 Routines checked, 0 failed.

<span id="_Toc519236700" class="anchor"></span>Figure 3‑1. KIDS Installation option: Verify Checksums in Transport Global \[XPD PRINT CHECKSUM\]

3.  Backup Transport Global.  
    >   
    > Use the KIDS Installation option, Backup a Transport Global \[XPD BACKUP\]. This option creates a MailMan message that will back-up all current routines on your VistA/M system that will be replaced by the packages in this transport global. (If you need to preserve components that are not routines, you must back them up separately.)  
    >   
    > At the Select INSTALL NAME: prompt, enter XOBU 1.6. All 3 VistALink packages (XOBU 1.6, XOBV 1.6 and XOBS 1.6) will be backed up.

> Follow the example below:

Select Installation Option: Backup a Transport Global

Select INSTALL NAME: XOBU 1.6\<ENTER\> Loaded from Distribution 4/3/08@09:54:49

=\> Foundations, VistALink and VistALink Security v1.6 ;Created on Apr 03

This Distribution was loaded on Apr 03, 2008@09:54:49 with header of

Foundations, VistALink and VistALink Security v1.6 ;Created on Apr 03, 2008@

09:34:33

It consisted of the following Install(s):

XOBU 1.6 XOBV 1.6 XOBS 1.6

Subject: Backup of XOBU 1.6 install on Apr 03, 2008

Replace \<ENTER\>

Loading Routines for XOBU 1.6.....

Routine XOBUZAP is not on the disk..

Routine XOBUZAP0 is not on the disk..

Routine XOBUZAP1 is not on the disk..

Loading Routines for XOBV 1.6.................

Loading Routines for XOBS 1.6.......

Send mail to: VLUSER,ONE// \<ENTER\>

Select basket to send to: IN// \<ENTER\>

And Send to: \<ENTER\>

<span id="_Toc519236701" class="anchor"></span>Figure 3‑2. KIDS Installation option: Backup a Transport Global \[XPD BACKUP\]

4.  Use the KIDS Installation option, Install Package(s) \[XPD INSTALL BUILD\] to install VistALink 1.6.

> At the Select INSTALL NAME: prompt, enter XOBU 1.6. All 3 VistALink packages (XOBU 1.6, XOBV 1.6 and XOBS 1.6) will be installed.  

> Answer the following install questions as follows:

- Although typically the answer is "No," you can answer "Yes," to the question

> Want KIDS to Rebuild Menu Trees Upon Completion of Install?

> Just remember that rebuilding menu trees will increase patch installation time.

- Answer "No" to the question:

> Want KIDS to INHIBIT LOGONs during the install?

- Answer "No" to the question:

> Want to DISABLE Scheduled Options, Menu Options, and Protocols?

> The following is an example of a VistALink 1.6.1 installation on a VistA/M server (that has VistALink 1.5 previously installed):

Select Installation Option: 6 \<ENTER\> Install Package(s)

Select INSTALL NAME: XOBU 1.6 \<ENTER\> Loaded from Distribution 4/3/08@12:00:46

=\> Foundations, VistALink, and VistALink Security v1.6 ;Created on Apr 0

This Distribution was loaded on Apr 03, 2008@12:00:46 with header of

Foundations, VistALink, and VistALink Security v1.6 ;Created on Apr 03, 2008

@11:54:01

It consisted of the following Install(s):

XOBU 1.6 XOBV 1.6 XOBS 1.6

Checking Install for Package XOBU 1.6

Will first run the Environment Check Routine, XOBUENV

\>\>\> Performing environment check...

All running VistALink listeners should be stopped before proceeding with

this installation. Enter ? for help on stopping VistALink listeners.

Have all VistALink listeners been stopped? NO// YES\<ENTER\> YES

\>\>\> VistALink environment check completed for KIDS Install Package option.

Install Questions for XOBU 1.6

Incoming Files:

18.01 FOUNDATIONS SITE PARAMETERS

> **NOTE:** You already have the 'FOUNDATIONS SITE PARAMETERS' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<ENTER\>

Checking Install for Package XOBV 1.6

Install Questions for XOBV 1.6

Incoming Files:

18.03 VISTALINK LISTENER CONFIGURATION

> **NOTE:** You already have the 'VISTALINK LISTENER CONFIGURATION' File.

18.04 VISTALINK LISTENER STARTUP LOG

> **NOTE:** You already have the 'VISTALINK LISTENER STARTUP LOG' File.

18.05 VISTALINK MESSAGE TYPE (including data)

> **NOTE:** You already have the 'VISTALINK MESSAGE TYPE' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<ENTER\>

Checking Install for Package XOBS 1.6

Install Questions for XOBS 1.6

Want KIDS to INHIBIT LOGONs during the install? NO// \<ENTER\>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// \<ENTER\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<ENTER\> TELNET

Install Started for XOBU 1.6 :

Apr 03, 2008@12:22:04

Build Distribution Date: Apr 03, 2008

Installing Routines:

Apr 03, 2008@12:22:04

Running Pre-Install Routine: EN^XOBUPRE

Installing Data Dictionaries:

Apr 03, 2008@12:22:04

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing PROTOCOL

Installing LIST TEMPLATE

Installing OPTION

Apr 03, 2008@12:22:04

Running Post-Install Routine: EN^XOBUPOST

Updating Routine file...

Updating KIDS files...

XOBU 1.6 Installed.

Apr 03, 2008@12:22:04

Install Message sent \#159

Install Started for XOBV 1.6 :

Apr 03, 2008@12:22:04

Build Distribution Date: Apr 03, 2008

Installing Routines:

Apr 03, 2008@12:22:04

Running Pre-Install Routine: EN^XOBVPRE

Installing Data Dictionaries:

Apr 03, 2008@12:22:04

Installing Data:

Apr 03, 2008@12:22:04

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing DIALOG

Installing PROTOCOL

Installing REMOTE PROCEDURE

Installing OPTION

Apr 03, 2008@12:22:05

Running Post-Install Routine: EN^XOBVPOST

\>\>\> Scheduling the XOBV LISTENER STARTUP option...

\>\>\> The XOBV LISTENER STARTUP option has previously been scheduled:

Updating Routine file...

Updating KIDS files...

XOBV 1.6 Installed.

Apr 03, 2008@12:22:05

Install Message sent \#161

Install Started for XOBS 1.6 :

Apr 03, 2008@12:22:05

Build Distribution Date: Apr 03, 2008

Installing Routines:

Apr 03, 2008@12:22:05

Installing PACKAGE COMPONENTS:

Installing DIALOG

Apr 03, 2008@12:22:05

Updating Routine file...

Updating KIDS files...

XOBS 1.6 Installed.

Apr 03, 2008@12:22:05

Install Message sent \#163

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

<span id="_Toc519236702" class="anchor"></span>Figure 3‑3. VistALink J2M Installation Example

|                                                                                                                |                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/012.png) | NOTE: The option XOBV LISTENER STARTUP will be scheduled for Task Manager startup on Caché/NT systems only. |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/013.png) | NOTE: The installation adds a new Kernel Application Proxy User named "XOBVTESTER,APPLICATION PROXY" to the NEW PERSON file (#200), if not already present. This application proxy user account is used in the VistALink sample Web application to demonstrate usage of the VistaLinkAppProxyConnectionSpec connection spec. |

5\. <u>Restart listeners</u>: If VistALink has already been set up on your server, and you want your server to resume servicing VistALink client requests, restart the VistALink Listener on the server. Follow your normal procedures to start the listener. Otherwise, configuring the listener is a follow-on task (see the section "Configure VistALink Listener"):

- If your VistALink listener runs via VMS TCP services, use VMS TCP services to enable the service (listener).
- If your VistALink listener is started within Caché (not via VMS TCP services), use the Foundations menu to start the listener.

## (Optional) Configure VistALink Listener 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Do I Need to Configure Listeners As Part of the VistALink Installation?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are <u>upgrading</u> an existing VistALink installation, you likely have one or more listeners already configured on your system. *You should not need to add to or change your listener configuration in any way*. Your existing listener configurations will continue to function, without reconfiguration, after upgrading VistALink.

For <u>Caché/Linux sites only</u>, with existing listeners, you may want to switch from the M-only listener (started from the Foundations menu) to the XINETD version of the listener (started from the OS level). You can do this switch at any time, however; it does not need to be done as part of the installation of VistALink v1.6.1.

For sites where VistALink is being <u>installed for the first time</u>, you will need to configure at least one new listener in order to support VistALink-based requests. You can do this as part of the installation, or at later time as is convenient.

### Listener Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VistALink listener runs on your M system, in order for Java applications to connect to your M system using VistALink. The listener waits for and accepts incoming client connections on a specified TCP port, and spawns off handler jobs to service those connection requests.

There are two styles of listeners:

- OS-Based Service (the listener runs as an operating system process, i.e., a VMS TCP Service, or an Linux XINETD service)
- M-Based (the listener starts, stops and runs as an M process)

Recommendations for which type of listener to use are based on operating system type, and account type:

- Production VMS systems: Run as a VMS-based TCPIP service
- Production Linux systems: Run as a Linux-based XINETD service
- Windows systems: The M-based listener must be used, including for production.
- Non-production VMS and Linux systems: Either the M-based or OS service-based listener can be used

The sections below provide setup requirements for the Caché/VMS and Caché/NT operating systems, as well as general information for all operating systems.

### Recommended VistALink Ports (all operating systems)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Though any available TCP port may be used, the recommended port for the VistALink Listener is 8000 for production systems and 8001 for test systems. This recommendation comes from the DBA's list of reserved ports, published on FORUM at DBA Option \| Port Assignments for TCP.

|                                                                                                                |                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/014.png) | NOTE: The recommended port for the VistALink listener is 8000 for production systems and 8001 for test systems. |

#### Avoiding Port Conflicts

Within a single IP address/system, VistALink listeners can be set up as:

- A single VistALink listener, running on any available port.
- Multiple VistALink listeners running on the same IP address/system, but listening on *different* ports.

To run one listener in a production account and another in a test account on the same IP address/system, you must configure them to listen on different ports (e.g., 8000 for production and 8001 for test). If, on the other hand, you are running the listeners on different IP addresses/systems, the ports can be the same (e.g., one VistALink listener on every system listening on port 8000).

### OS-Based Listener Configuration for Caché/VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For production Caché/VMS systems, it is recommended to run the VistALink listener as a VMS TCP/IP service. The advantages include:

- The ability to run the TCP/IP service on multiple nodes in a cluster. This allows for an uninterrupted listening process, by redirecting the job if one of the nodes in the cluster goes down.
- Since TaskMan is not used to start the listener, it doesn't matter if the TaskMan process is running on the same node(s) as the VistALink listener(s).

|                                                                                                                |                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/015.png) | REF: For further assistance with set-up of a VMS TCP/IP service for VistALink, and for the latest information on recommended configuration, we strongly recommend that you log a Remedy ticket so that the appropriate Product Support team (currently HSTS) can assist you. |

The methodology for running VistALink as a TCP listener was developed and written into a cookbook by the HSTS Product Support team, to aid IRM support staff. The cookbook, as a document named VISTALINK_TCPIP_COOKBOOK.DOC, can be obtained from the HSTS team or downloaded from the standard Product Support ftp download directories.

When configuring VMS TCP Services, some issues to consider include:

- Many of the operations require elevated VMS privileges, specifically, SYSPRV. Before you begin, use the VMS SHOW PROCESS/ALL command to verify that you are logged into an account that has SYSPRV.
- If you need to create a new service, refer to VISTALINK_TCPIP_COOKBOOK.DOC for step-by-step instructions.
- To modify an already-existing VistALink service:
  - Use the TCP/IP utilities to disable the service, e.g., VLINK:

> TCPIP\> DISABLE SERVICE VLINK

- Copy any updated command file to the directory used by the service.
- Modify the command files to match your environment. You'll need to remove the comment from the appropriate line in the 'command line:' section and then modify it to match your configuration. Refer to the comments for examples of how the line should be modified.
- Save the file(s).
- Enable the VistALink service, e.g., VLINK:

> TCPIP\> ENABLE SERVICE VLINK

In general, use VISTALINK_TCPIP_COOKBOOK.DOC to help you:

- Set up VistALink as a TCP/IP service in VMS
- Modify the service command file templates to match your environment
- Create and update a dedicated VMS user account, e.g., VLINK with the proper authorized and default privileges (e.g., remove OPER privilege).

### OS-Based Listener Configuration for Caché/Linux Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For production Caché/Linux systems, it is recommended to run the VistALink listener as a XINETD (Linux) service.

The advantages include a uniform method for starting and stopping VistALink as one of many different types of listener processes on Linux.

|                                                                                                                |                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/016.png) | NOTE: For further assistance with set-up of an XINETD service for VistALink, and for the latest information on recommended configuration, we strongly recommend that you log a Remedy ticket so that the appropriate Product Support team can assist you. |

An example of an XINETD configuration file for a VistALink listener is provided below.

\#description: VA VistALink Listener for Port 8000

\#

service las_vlkp

{

type = UNLISTED

disable = no

flags = REUSE

socket_type = stream

protocol = tcp

port = 8000

wait = no

user = lastcpip

env = TZ=/usr/share/zoneinfo/US/Pacific

server = /usr/local/cachesys/system01/bin/csession

server_args = system01 -ci -U OEX CACHELNX^XOBVTCP

instances = UNLIMITED

}

<span id="_Toc519236703" class="anchor"></span>Figure 3‑4: Example XINETD Service Configuration

You will need to adjust certain values to match your system environment:

- port
- user
- env
- server
- server_args

### M-Based Listener Configuration for Caché/NT (Windows) Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Appendix A, "Listener Management for Caché NT," in the *VistALink 1.6 System Management Guide*. This approach starts, manages and stops the listener entirely within M (as opposed to using VMS (TCP/IP utility) or Linux (XINETD) to start/stop the listener.

> **NOTE:** You can also use the same instructions to set up an M-based (rather than OS service based) listener on Linux and/or VMS system, i.e., for non-production systems.

## (Optional) Verify Listener Connectivity 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The general process for testing the listener is as follows:

1.  Telnet test
2.  VistALink J2SE SwingTester sample application test

### Telnet Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Telnet from your workstation to the IP address and port of the VistALink listener. On most workstations you can do this simply by entering the telnet IP address port in a command window, e.g.:

> c:\\ telnet 10.21.1.85 8000 \<Enter\>

1.  When you connect, press \<Enter\>. If a VistALink listener is running on that port, you should see echoed something similar to this example:

\<?xml version="1.0" encoding="utf-8" ?\>\<VistaLink messageType="gov.va.med.founda  
tions.vistalink.system.fault" version="1.5" xmlns:xsi="<http://www.w3.org/2001/XM>  
LSchema-instance" xsi:noNamespaceSchemaLocation="vlFault.xsd"\>\<Fault\>\<FaultCode\>  
Server\</FaultCode\>\<FaultString\>System Error\</FaultString\>\<FaultActor\>Request Man  
ager\</FaultActor\>\<Detail\>\<Error type="Request Manager" code="184001" \>\<Message\>R  
equest Handler Loading Error: No message type defined\</Message\>\</Error\>\</Detail\>  
\</Fault\>\</VistaLink\>

> Although there is an error message echoed in this display, the error is due to the fact that you are connecting from telnet rather than from a VistALink client. If an Extensible Markup Language (XML) message similar to the one above is echoed back, the network connection between your workstation and the VistALink listener at the requested IP address and port is valid.

If you cannot make the telnet connection, there may be a problem somewhere in the network / firewall / machine TCP configuration.

If you connect but do not see XML output similar to that in the sample in step 2 above when you press \<Enter\>, check the type of listener that is running in the port. (It may be a Broker, Health Level 7 \[HL7\], or other type of listener.)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/017.png)</td>
<td><p><strong>NOTE:</strong> To disconnect the session, press and hold the CTRL key then press the right brace "]" key: CTRL + ]</p>
<p>This will properly disconnect the telnet connection.</p></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/018.png) | NOTE: Errors (at SETMSG+5^XOBVRH) will be logged in the Kernel error trap when you use telnet to test the VistALink listener. Such errors can be ignored when Telnet testing is the source. |

### VistALink J2SE SwingTester Sample Application Test (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To test your M listener with the SwingTester sample application, follow the instructions provided in Appendix A of this document, "[Installing and Running the J2SE Sample Applications](#appendix-a-installing-and-running-the-j2se-sample-apps)."

> The SwingTester Java 2 Platforms Standard Edition (J2SE) (client/server) sample application is supplied in the vljSamples_1.6.1.nnn.jar file.

You can use the SwingTester sample application to perform a standalone test of the M VistALink listener before proceeding with the app server installation.

## (Optional) Configure Connector Proxy User(s) for J2EE Access 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow this step only if you are setting up a brand new VistALink implementation on your VistA/M system for immediate access by one or more specific J2EE servers. <u>This step is not necessary if you are upgrading an existing VistALink implementation.</u>

### Connector Proxy Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To allow a J2EE system to access resources on your M system via VistALink, you need to an M Kernel "connector proxy user" account for the J2EE system to connect/login to your M system. A connector proxy account represents a specific application server (not an end-user). A VistALink adapter on a J2EE system logs on to your VistA/M server using the assigned Kernel connector proxy user account, authenticating with an access/verify code pair.

### How to Create Connector Proxy User Kernel Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the *Security* chapter, "*Creating Connector Proxy Users for J2EE Systems*" section, in the *VistALink 1.6 System Management Guide*, for complete instructions on how to create connector proxy users.

## Installation Back-Out/Roll-Back Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there is an unforeseen problem with the installation of VistALink v1.6.1, it is possible to reinstall VistALink v1.5. Possible losses of functionality with a rollback to v1.5 include:

- Inability of any client applications that have upgraded to VistALink v1.6.1 (client-side) to connect to your site.

|                                                                                                                |                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/019.png) | NOTE: There are no FileMan data dictionary changes between v1.5 and v1.6.1. |

### Reinstall v1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To re-install v1.5:

1.  Obtain the v1.5 KIDS distribution from the EIE ftp server (XOB_1_5.KID).
2.  Obtain the v1.5 Install Guide from the EIE ftp server and follow the installation steps in chapter 2 (VistA/M Server Installation Procedures) to reinstall VistALink v1.5. Or:
    1.  Stop any running VistALink listeners (if any are running at all).
    2.  Use KIDS to install the XOB_1_5.KID distribution. The install package is XOBU 1.5.
    3.  Start any listeners after the installation, either from the operating system level or Mumps level, depending on how VistALink listeners have been configured at your site.
    4.  Optionally verify listener connectivity – with telnet and/or with a v1.5 VistALink client application

### Optional Deletions of v1.6-Only Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Optionally delete the following v1.6-only components:

- Routines:
  - XOBUZAP
  - XOBUZAP0
  - XOBUZAP1
- Protocols
  - XOBU TERMINATE A JOB
  - XOBU TERMINATE ALL JOBS
  - XOBU TERMINATE CONNECTION MANAGER
  - XOBU TERMINATE JOBS REFRESH
  - XOBU TERMINATE JOBS UTILITY MENU
  - XOBU TERMINATE SYSTEM STATUS
- List Templates
  - XOBU TERMINATE JOBS UTILITY
- Dialogs
  - 182010

# Oracle WebLogic Application Server: Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Goal: Install VistALink adapter(s) on application servers so that J2EE applications running on those servers can execute requests against one or more M systems.

Main installation tasks:

- Admin server:
  - Make VistALink configuration file accessible on classpath
  - Install VistALink-specific monitoring plug-in into WebLogic console
- Servers targeted for adapter(s):
  - Make a copy of VistALink configuration file accessible on classpath
  - Install supporting jars as J2EE Shared Libraries (production servers only)
  - Install VistALink adapters (one per unique M system IP address/port combination)

### Adapter Deployment Descriptors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink resource adapters have deployment descriptors that control configuration of the adapter. Text editors are the recommended tool for editing deployment descriptors. These files are located in the META-INF directory in each adapter archive (RAR):

- ra.xml: The standard J2EE deployment descriptor for J2CA resource adapters.
- weblogic-ra.xml: Contains WebLogic-specific extended configuration information.
- MANIFEST.MF: Manifest file defining information about the files packaged in the RAR.

### VistALink 1.6.1 Adapter Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.6.1 adapters are updated to support the new J2EE 1.7 specifications for J2EE connectors, supported in WebLogic 10.3.6/12.1.2. Changes significant to the installation process are:

- <u>Deployment Descriptors</u>. The format of both the ra.xml and weblogic-ra.xml descriptors is different. Existing adapters' deployment descriptors need to be updated.
- <u>Linked Adapters replaced by J2EE Shared Libraries</u>. The primary benefit of the WebLogic 8.1 linked adapter was the re-use of one adapter's resources (jars) by other adapters. The linked adapter feature is not supported for upgraded adapters in WebLogic 10.3.6/12.1.2. However, for production servers that need to minimize resource consumption, the replacement feature for linked adapters is to deploy the adapter jars as "J2EE shared libraries".

### VistALink Adapters and Classloading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink resource adapters are intended to be deployed and run as standalone deployments in WebLogic. The adapter is then made available for use by any application on the server. To support this, the application server places java classes used in the VistALink RAR on high-level classloaders visible by all applications.

## Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Installation Time (Varies)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The estimated installation time installing VistALink adapters in a WebLogic domain varies, depending in part on whether it is a first-time installation, and in part on how many new or existing adapters need to be deployed or upgraded. As such, a time estimate for individual tasks is provided below, from which you can estimate on how much time is required for the installation tasks necessary on your system.

- Place VistALink configuration file on server classpath: 5 minutes per server
- Install console plug-in or standalone EAR (admin server): 5 minutes
- Update existing 10.3.6/12.1.2 RAR deployment descriptors: 5-10 minutes per adapter
- Install J2EE shared libraries (production servers only): 20 minutes
- Install new adapters: 5-15 minutes per adapter

### System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.6.1 is supported only on WebLogic at the current time. This is the requirement for installation:

- Oracle WebLogic Server (WLS) 10.3.6/12.1.2

### Deployer Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The WebLogic administrator/deployer should have prior WebLogic administration experience, and be comfortable with (and have the privileges for) the following tasks:

- Modify server startup scripts
- Set "Remote Start" options for managed servers started by Node Manager
- Set JVM arguments for WebLogic servers
- Modify the classpath for WebLogic servers
- Configure log4j
- Deploy and undeploy applications
- Bounce servers

### Obtain the VistALink Distribution File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can obtain the VistALink distribution ZIP file from any of the anonymous.software directories on the Office of Information & Technology (OI&T) File Transfer Protocol (FTP) download sites. You should unzip it to a folder in a good working location for your WebLogic Server installation process, most likely on a drive of the administration server for your WebLogic domain. This location will be referred to as the "\<DIST FOLDER\>" for the rest of the instructions.

### Obtain M Connector Proxy User and Listener Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are configuring a new adapter, contact the VistA/M system's Information Security Officer (ISO) and/or the VistA/M system manager to obtain the connector proxy user's credentials for the VistA/M system to which you intend to connect. This information includes:

- Access/verify codes for connector proxy user
- VistALink listener port
- IP address of the VistA/M system

See the section ["Post Install: Configure Connector Proxy User(s) for J2EE Access"](#optional-configure-connector-proxy-users-for-j2ee-access) in this guide for more information on the connector proxy user.

## Upgrading a WebLogic 8.1 Domain w/Existing VistALink Adapters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Back Up Exploded RAR Directories and VistALink Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You should back up (copy) all of your exploded RAR directories, and also the VistALink configuration file. You will need these to recreate your adapters in the WebLogic 10.3.6/12.1.2 domain.

### If Running the Domain Upgrade Wizard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two approaches to moving from a WebLogic 9/10 domain to a WebLogic 10.3.6/12.1.2 domain (and only you can decide which is best):

- Create a new WebLogic 10.3.6/12.1.2 domain from scratch and redeploy all applications to it that you want carried forward, or
- Run Oracle's domain upgrade wizard to upgrade your WebLogic 9/10 domain to WebLogic 10.3.6/12.1.2.

If you choose to upgrade your domain by running the upgrade wizard (rather than starting from scratch with a new domain), we recommend you perform the following steps, before shutting down your WebLogic 8.1 domain and running the wizard.

#### Undeploy RARs

If you have any VistALink adapters deployed, delete them from the WebLogic configuration by navigating to:

> mydomain\>Deployments\>Connector Modules

Then select each adapter, and click on the Delete button.

#### Undeploy VistALink Console

If you have deployed the VistALink Console, delete it from the WebLogic configuration by navigating to:

> mydomain\>Deployments\>Web Application Modules

Then select the VistaLink console web application, and click on the Delete button.

#### Undeploy Sample Application

If you have deployed the VistALink sample web application, delete it from the WebLogic configuration by navigating to:

> mydomain\>Deployments\>Applications

Then select the VistALink sample web application, and click on the Delete button.

## WebLogic 10.3.6/12.1.2 Server Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the domain's admin server, and for each managed server that will run VistALink adapters, perform the following steps:

### Create \<HEV Configuration Folder\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We recommend using a single folder to hold any external configuration files for all Health*<u>e</u>*Vet (HEV) applications, including VistALink. If it is not already present, you should create this folder, on each physical WebLogic server.

- If not already present, create a secure, protected directory to place on the server classpath for each of your WebLogic servers running VistALink. This folder will be referred to as the \<HEV CONFIGURATION FOLDER\> in the following steps.
- Ensure that this folder is secure and protected. The gov.va.med.vistalink.connectorConfig.xml file it will contain holds login credentials for accessing VistA/M systems. On Linux systems, access to the folder should be restricted to the account or group under which WebLogic runs. On all J2EE systems, access to the host file system should be protected.

### Create/Copy VistALink Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink makes use of its own configuration file to load VistALink-specific connector settings. When configured for your system, it will contain one entry for each VistALink adapter.

1.  Copy the *gov.va.med.vistalink.connectorConfig.xml* configuration file into the \<HEV CONFIGURATION FOLDER\> on each physical server that will be running VistALink adapters. Also do this on the admin server:
- If upgrading a previous domain, copy the existing gov.va.med.vistalink.connectorConfig.xml from that domain

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/020.png)</td>
<td><p><strong>Obsolete Setting:</strong> primaryStationSuffix: This attribute has been eliminated. Any primary station numbers requiring an alpha suffix, should instead be entered as part of the "primaryStation" attribute, i.e., primaryStation="200M".</p>
<p>Note: If VA institution rules are being used, only 200-series (Austin Information Technology Center) station numbers can have alpha suffixes for the <u>primary</u> station number.</p>
<p>If any entries have primaryStationSuffix, they should remove that attribute and append the value of the suffix into the existing primaryStation attribute.</p></td>
</tr>
</tbody>
</table>

- If this is a brand new VistALink deployment, copy the example configuration file from the \<DIST FOLDER\>/app-j2ee/configFile-j2ee folder.

|                                                                                                                |                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/021.png) | NOTE: For additional information on setting up a connector configuration file, see the section "VistALink Connector Configuration File," in the *VistALink 1.6 System Management Guide*. |

### Place \<HEV Configuration Folder\> on Server Classpath(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Admin Server. On admin servers, modify the server classpath by updating the appropriate variable in either the setDomainEnv.cmd/.sh (preferred) script, or in the startWebLogic.cmd/.sh script (both scripts are in the domain root's /bin folder). Add the \<HEV Configuration Folder\> classpath folder to the PRE_CLASSPATH (setDomainEnv) or CLASSPATH (startWebLogic) variable.  
    >   
    > The following example shows example modifications for a Windows (.cmd) setDomainEnv script:

. . .

@REM ADD EXTENSIONS TO CLASSPATHS

@REM for VISTALINK

set PRE_CLASSPATH=%PRE_CLASSPATH%;C:\Data\bea103-stage\admin\ClasspathFolder;

. . .

<span id="_Toc519236704" class="anchor"></span>Figure 4‑1. Admin Server: Add the classpath folder to the server classpath in the setDomainEnv script

2.  Managed Servers. On any managed servers started by Node Manager, update the server classpath in the Configuration \| Server Start tab of the console. Adding a classpath folder to the server classpath will also necessitate specifying the complete server startup classpath, which typically means, at a minimum, including the following jars:

> weblogic_sp.jar e.g., c:/bea/weblogic92/server/lib/weblogic_sp.jar

> weblogic. e.g., c:/bea/weblogic92/server/lib/weblogic.jar

> webservices.jar e.g., c:/bea/weblogic92/server/lib/webservices.jar

> tools.jar e.g., c:/bea/jdk150_04/lib/tools.jar (required only if server compilation needed, e.g., JSPs)

> \<HEV Configuration Folder\> (the point of this exercise)

|                                                                                                                |                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/022.png) | NOTE: You can find the exact classpath used to start any given managed server by examining the log files (.out, .log) stored in the domain folder, servers/\<SERVER NAME\> subdirectory and looking for the value of the *java.class.path* property. |

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/023.png)</td>
<td><p><strong>NOTE:</strong> No other classpath changes are necessary to support VistALink on WebLogic 10.3.6/12.1.2. On WebLogic 10.3.6/12.1.2, jars for adapters are loaded either as:</p>
<ul>
<li><p>J2EE shared libraries (production systems), or</p></li>
<li><p>Automatically from the adapter RAR folder (development systems)</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Create/Update Server log4j Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink uses log4j for logging. To enable VistALink logging, you should create (or if upgrading from a previous domain, update the existing) log4j configuration file(s) for each server that will have VistALink components installed:

- admin server (VistALink console application, and/or adapters)
- managed servers (adapters)

To help with configuring log4j, in the VistALink \<DIST FOLDER\>/log4j directory, VistALink-specific log4j information is provided, including:

- vistalink_1_6_loggers.xls (describes VistALink supported logger categories/levels)
- log4jSampleJ2EEConfig.xml (example log4j configuration file for VistALink for J2EE)

To enable logging:

1.  Create/update a log4j configuration file on each J2EE server (admin and managed servers)
2.  Configure each server to find log4j configuration file. Methods include:
    - Name the file log4j.xml and place in a folder that is on the server classpath, such as the \<HEV CONFIGURATION FOLDER\> (WebLogic will find automatically), or
    - Name the file anything, and put it in any location on the server file system. Then configure each server's JVM to start with the following JVM argument to explicitly provide the full filepath for the log4j configuration file:

> –Dlog4j.configurationFile=directory/filename

|                                                                                                                |                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/024.png) | NOTE: Due to the fact that using deploying VistALink adapters place the log4j library on a classloader higher than all deployed applications, log4j configuration on all servers with VistALink adapters deployed must contain the logger and appender log4j configurations for ALL applications deployed to that server. |

### Server JVM Argument: gov.va.med.environment.production 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *gov.va.med.environment.production* JVM system property configures whether the WebLogic server is considered a Test or Production server, and is used in VistALink and made available to other applications through the gov.va.med.environment.Environment Application Program Interface (API). Optionally add the following JVM argument to your server startup(s):

| JVM Argument                    | Value     | Default Value |
|-------------------------------------|---------------|-------------------|
| -Dgov.va.med.environment.production | false \| true | false             |

1.  For production servers only, set the "-Dgov.va.med.environment.production" JVM argument to true. Modify one of the following locations to set this argument:
- Admin server: modify the setDomainEnv.cmd/.sh (preferred) or startWebLogic.cmd/.sh script (both scripts are in the domain home, /bin subdirectory). Modify the JAVA_OPTIONS variable.
- Managed servers started by node manager: In the WebLogic console, go to the \<Server Name\> \| Configuration \| Remote Start tab, and modify the "Arguments" field.

|                                                                                                                |                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/025.png) | NOTE: The *gov.va.med.environment.production* setting marks a J2EE system as being a "production" or "test" system, and is used by VistALink adapters to prevent a test J2EE system from connecting to a production M system, and vice versa. |

2\. On non-production WebLogic servers, the argument does not need to be set, since the API using it defaults to false.

### Server JVM Argument: gov.va.med.environment.servertype 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On WebLogic servers, in most cases the argument does not need to be set (a change since VistALink 1.5), because automatic servertype detection is performed on WebLogic servers, and will succeed (except with unusual classloader configurations.) If set, however, the value of the JVM argument still overrides the automatically detected value.

The *gov.va.med.environment.servertype* JVM system property configures the value of the "current" server type returned to VistALink and other applications by gov.va.med.environment.Environment API. Optionally add the following JVM argument to your server startup(s):

| JVM Argument                    | Value                                      | Default Value                                          |
|-------------------------------------|------------------------------------------------|------------------------------------------------------------|
| -Dgov.va.med.environment.servertype | weblogic, websphere, jboss, oracle, j2se, etc. | auto-detects for weblogic, otherwise defaults to "unknown" |

1.  If you decide to pass this argument to the server JVMs, optionally modify one of the following locations to set this argument:
- Admin server: modify the setDomainEnv (preferred) or startWebLogic script (both are in the domain home, /bin subdirectory).
- Managed servers started by node manager: In the WebLogic console, go to the \<Server Name\> \| Configuration \| Remote Start tab, and modify the "Arguments" field.

## ## WebLogic 10.3.6/12.1.2: Install the Standalone Console EAR (Admin Server)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For WebLogic 10.3.6/12.1.2 we recommend installing the standalone VistALink console EAR application, rather than the console plug-in, due to difficulties integrating with the WebLogic console navigation tree and tab set.

The VistALink console is helpful to monitor and troubleshoot VistALink adapters. As such it is useful to install it prior to installing any VistALink adapters.

### Copy Console EAR file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Copy the console EAR file from the \<DIST FOLDER\>/app-j2ee/console-ext folder to a staging folder on your admin server:

- VistaLinkConsole-1.6.1.xxx.ear

### Deploy Console EAR 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Target the deployment to the domain admin server only.
2.  Finish the deployment, and activate changes. In the main "Deployments" listing, the state of the VistaLinkConsole application should be *New* or *Prepared* (depending on whether targeted servers are running or not).
3.  Start the application (in the Deployment list, choose Start \| Servicing all requests for the VistaLinkConsole application). The state of the application should now be *Active*.

### Access Standalone VistALink Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If successfully deployed, the standalone VistALink console will be reachable at the following URL:

- http://\<adminserver\>:\<port\>/vlconsole

You'll be prompted for a user name and password. Use the same credentials as you would use to login to the WebLogic administration console. From that point on, the standalone VistALink console application will look almost identical to the console extension plug-in version.

Click on the link to open the VistALink console plug-in main page. You should see a page like the following:

![](vistalink-version-1-6-installation-guide/026.png)

<span id="_Toc519236705" class="anchor"></span>Figure 4‑2. Standalone VistALink 1.6 Console

### Check Configuration Editor Access to Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the main page of the VistALink console, click the "Configuration File Editor" link:

- If the server classpath on the admin server file system is set up correctly, you should be presented with a list of entries from the copy of the VistALink configuration file on your admin server's file system.
- Otherwise, if there is a problem, you will see an error message, for example, "Error while retrieving configuration file: 'Missing configuration file path.'.". If you see this or similar error message, check:
  - Is the configuration file present on the host file system of the admin server?
  - Is the configuration file named "gov.va.med.vistalink.connectorConfig.xml"?
  - Is the folder containing the configuration file on the classpath specified in the setDomainEnv or startWebLogic script of the admin server?

## Deploy Shared J2EE Libraries (Production Domains Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Copy the following jars from \<DIST FOLDER\>\>/app-j2ee/shared-lib to your deployment staging area, and deploy each of them as shared libraries:

- log4j-api-2.10.0.jar
- log4j-core-2.10.0.jar
- vljFoundationsLib-1.6.1.xxx.jar
- vljConnector-1.6.1.xxx.jar

On production domains only, and for servers that will host adapters only, deploy these jars as J2EE shared libraries:

1.  Copy each jar listed above to a file location on the admin server's file system.
2.  Perform a deployment in the WebLogic console for each jar, using the same steps as you would for deploying an EAR. Accept the defaults presented by the WebLogic console.
3.  Target the deployment to all servers that will be hosting VistALink adapters.
4.  Activate changes, either individually or after all libraries are deployed.

|                                                                                                                |                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/027.png) | NOTE: For J2CA adapters, J2EE shared libraries serve as a replacement for WebLogic 8.1's "linked adapter" feature. Linked adapters in WebLogic 8.1 allowed the sharing of jar resources across multiple adapters, reducing the amount of systems resources consumed by multiple adapters. |

For development systems, deploying the jars as J2EE shared libraries is not necessary. Instead, the jars can be deployed with each adapter, inside each adapter's RAR folder.

## Create/Deploy VistALink Adapter(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Repeat the steps in this section for each adapter you need to deploy. You would deploy one adapter for every M system that applications on your domain need to communicate with.

### Add Connector Entry to VistALink Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If this is a new adapter, use the VistaLink console's configuration editor to add a new configuration entry for the new adapter. You will need to provide:
- A unique Java Naming and Directory Interface (JNDI) name for the adapter to be deployed under, (e.g., *vlj/Salem658*) in the jndiName attribute.
- The primary station number of the M system being connected to, in the primaryStation attribute.
- The IP and port of the VistALink listener on the M system being connected to (ip and port attributes)
- The access and verify code for the connector proxy user assigned by the M system administrator (access-code and verify-code attributes)
  1.  Be sure to set the "enabled" attribute to true.
  2.  Save the new entry.
  3.  Copy the updated configuration file to all managed servers that will be hosting the adapter (if it is a multi-server domain).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/028.png)</td>
<td><blockquote>
<p><strong>NOTE:</strong> Use of the VistaLink console's configuration editor is not mandatory. The VistALink configuration file can also be edited directly using a text editor.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Create New or Update Existing Adapter Folder on Admin Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If this is a new adapter, on the admin server, create a new, empty folder for the adapter, with a folder name that easily identifies the adapter (e.g., "vlj/Salem658").

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/029.png)</td>
<td><blockquote>
<p><strong>NOTE:</strong> The folder name will become the default deployment name for the adapter when displayed in the WebLogic console. So choose folder names that will identify the adapter mnemonically to the administrators viewing them in the WebLogic console later.</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  If you are updating an existing adapter folder from a previous WebLogic 8.1 domain, delete:
- all jar files in the root directory of the folder
- all jar files in the /lib subdirectory

### Back Up Deployment Descriptors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If you are updating an existing adapter folder from a previous WebLogic 8.1 domain,, move elsewhere, rename or otherwise back up the following files in the existing META-INF directory:
- ra.xml
- weblogic-ra.xml

### Copy New 1.6 Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Copy the updated 1.6 files needed for the RAR from the VistALink zip distribution to the existing or new RAR folder:
- Production Systems: Copy the entire contents of the \<DIST FOLDER\>/app-j2ee/Rar-Prod-Template folder from the VistALink zip distribution to the new RAR folder, including the entire META-INF subfolder.
- Non-production systems: \<DIST FOLDER\>/app-j2ee/Rar-Dev-Template folder from the VistALink zip distribution to the new RAR folder, including the entire lib and META-INF subfolders.

### Update Deployment Descriptors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The new ra.xml deployment descriptor no longer needs to be modified. Leave as-is the template ra.xml descriptor copied above.
2.  If creating a new adapter, determine the The Java Naming and Directory Interface (JNDI) name you want to deploy the adapter and connection-instance under. Otherwise, get the existing JNDI name from the old deployment descriptors. This value should match the value used for the adapter's entry in the VistaLink configuration file earlier (e.g., *vlj/Salem658*).
3.  Edit the weblogic-ra.xml descriptor copied above, as follows:
    1.  In the \<connection-instance\> section, \<jndi-name\> element, replace the placeholder value *"\${vlj.jndi.name}"* with the chosen JNDI name.
    2.  In the \<connection-instance\> section, \<connection-properties\> element, \<properties\> element, \<property\> element, \<value\> element, replace the placeholder value *"\${vlj.jndi.name}"* with the chosen JNDI name.
    3.  Near the top of the file, in the first, first-level \<jndi-name\> property, replace the placeholder value *"\${vlj.jndi.name}"*: we recommend using the chosen JNDI name appended with "Adapter".

|                                                                                                                |                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/030.png) | NOTE: This JNDI name (for the entire adapter) must be *different* than the JNDI name of the connection instance, that was configured in previous steps a) and b). |

4.  If updating an existing adapter, for other any properties you changed from the defaults in the old descriptors, update the corresponding values in the new descriptors.

|                                                                                                                |                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/031.png) | NOTE: Linked adapters are not supported (i.e., via the WebLogic 8.1 \<ra-link-ref\> mechanism). Any existing linked adapters should be changed to standalone adapters before upgrading. |

Example weblogic-ra.xml deployment descriptor:

\<?xml version="1.0"?\>

\<weblogic-connector xmlns="http://www.bea.com/ns/weblogic/90" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.bea.com/ns/weblogic/90

http://www.bea.com/ns/weblogic/90/weblogic-ra.xsd"\>

\<!-- Warning: The order the elements appear in complex elements is usually important.

It is a good idea to validate and test the weblogic-ra.xml document before committing. --\>

\<!-- For new ADAPTER-level jndi-name, recommend using value of connection instance JNDI name, appended with "Adapter" --\>

\<jndi-name\>vljtestconnectorAdapter\</jndi-name\>

\<enable-global-access-to-classes\>true\</enable-global-access-to-classes\>

\<outbound-resource-adapter\>

\<connection-definition-group\>

\<connection-factory-interface\>javax.resource.cci.ConnectionFactory\</connection-factory-interface\>

\<default-connection-properties\>

\<pool-params\>

\<initial-capacity\>1\</initial-capacity\>

\<max-capacity\>5\</max-capacity\>

\<capacity-increment\>1\</capacity-increment\>

\<shrinking-enabled\>true\</shrinking-enabled\>

\<shrink-frequency-seconds\>1800\</shrink-frequency-seconds\>

\<highest-num-waiters\>2147483647\</highest-num-waiters\>

\<connection-creation-retry-frequency-seconds\>30\</connection-creation-retry-frequency-seconds\>

\<connection-reserve-timeout-seconds\>0\</connection-reserve-timeout-seconds\>

\<test-frequency-seconds\>3600\</test-frequency-seconds\>

\<profile-harvest-frequency-seconds\>30\</profile-harvest-frequency-seconds\>

\<ignore-in-use-connections-enabled\>false\</ignore-in-use-connections-enabled\>

\<match-connections-supported\>true\</match-connections-supported\>

\</pool-params\>

\<transaction-support\>NoTransaction\</transaction-support\>

\<reauthentication-support\>false\</reauthentication-support\>

\</default-connection-properties\>

\<connection-instance\>

\<description\>This is the connection and JNDI name that applications will be accessing.\</description\>

\<jndi-name\>vljtestconnector\</jndi-name\>

\<connection-properties\>

\<properties\>

\<property\>

\<!-- connectorJndiName value should be the same value as connection instance jndi-name a few lines above --\>

\<name\>connectorJndiName\</name\>

\<value\>vljtestconnector\</value\>

\</property\>

\</properties\>

\</connection-properties\>

\</connection-instance\>

\</connection-definition-group\>

\</outbound-resource-adapter\>

\</weblogic-connector\>

<span id="_Toc519236706" class="anchor"></span>Figure 4‑3. weblogic-ra.xml sample deployment descriptor

### Deploy Adapter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Perform a deployment in the WebLogic console for the new RAR folder (i.e., an exploded RAR). Accept the defaults presented by the WebLogic console.
2.  Target the deployment to all servers that will be hosting the VistALink adapter.
3.  Finish the deployment, and activate the changes. In the main "Deployments" listing, the state of the deployed adapter should be *New* or *Prepared* (depending on whether targeted servers are running or not).
4.  Start the server(s) the adapter is targeted to, if they aren't running. The state of the deployed adapter should now be *Prepared*.
5.  Start the adapter itself (in the Deployment list, choose Start \| Servicing all requests for the adapter). The state of the deployed adapter should now be *Active*.

### Monitor Adapter in VistALink Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With a successfully configured adapter and a successful deployment, you will be able to:

- See the adapter listed in the "Live Connector Status" section of the VistALink console for every running server it was deployed on
- On the list of connectors for any given server, under "M System Info", you should see the IP address and port for the connector. This means the adapter was able to find and load settings from an entry in the VistALink configuration file on that server.
- If you click on hyperlinked JNDI name for each connector, you should be able to access a detail page for the connector, showing additional information and performing a live query against the M system to retrieve a number of settings, including the introductory text for the M server.
- The failure counts under health monitoring should be '0'. Otherwise, an error condition exists that should be corrected.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the adapter does not appear to be correctly configured or deployed, please refer to the "Troubleshooting VistALink" section of the *System Management Guide* for further guidance.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/032.png)</td>
<td><p><strong>NOTE:</strong> Some of the first places to look when troubleshooting a non-working adapter:</p>
<ul>
<li><blockquote>
<p>VistALink console (what error messages if any are displayed when you try to view the adapter and perform a live query?)</p>
</blockquote></li>
<li><blockquote>
<p>WebLogic server log files (per server)</p>
</blockquote></li>
<li><blockquote>
<p>WebLogic console "out" output</p>
</blockquote></li>
<li><blockquote>
<p>log4j log files</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

## Test with J2EE Sample Application (Development Systems Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Deploy the Sample Web Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A sample J2EE application is provided to developers to demonstrate the use of VistALink in a J2EE environment. The sample application is also a way to test your basic adapter setup.

The sample applications is provided in the \<DIST FOLDER\>/app-j2ee/sample folder.

To deploy the sample J2EE application:

1.  Copy the sample application's EAR file (VistaLinkSamples-1.6.1.xxx.ear) to the admin server's host file system.
2.  Perform a deployment in the WebLogic console for the sample application's EAR. Accept the defaults presented by the WebLogic console.
3.  Target the deployment to any or all servers hosting VistALink adapters.
4.  Finish the deployment, and activate changes. In the main "Deployments" listing, the state of the sample application should be *New* or *Prepared* (depending on whether targeted servers are running or not).
5.  Start the server(s) the application is targeted to, if they aren't running. The state of the sample application should now be *Prepared*.
6.  Start the application (in the Deployment list, choose Start \| Servicing all requests for the sample application). The state of the application should now be *Active*.

To run the sample J2EE application:

1.  Point your browser to

http://\<yourserver\>:\<yourport\>/VistaLinkSamples

> Example: <http://localhost:7001/VistaLinkSamples>.

2.  If the install is successful, you should reach a page titled "VistALink Sample/Demo J2EE Application."

> ![](vistalink-version-1-6-installation-guide/033.png)

<span id="_Toc519236707" class="anchor"></span>Figure 4‑4. VistALink Sample Application

3.  Choose a re-authentication method (VA Person ID, or VPID, Application Proxy, or User Number, also called a DUZ) that will allow you to invoke a valid user identity on the target M system to run RPCs under.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/034.png)</td>
<td><blockquote>
<p><strong>NOTE:</strong> This user must hold the [XOBV VISTALINK TESTER] "B"-type option.</p>
<p>Note also that if you select default application proxy user "XOBV VISTALINK TESTER", which is distributed/installed by VistALink, that this user is not assigned this "B"-type option by default.</p>
</blockquote></td>
</tr>
</tbody>
</table>

4.  Enter the division (for DUZ(2)) valid for both the user you selected, and the M system you're connecting to.
5.  Choose the connector to use, either by using institution mapping feature, or selecting from the list of deployed connectors.

![](vistalink-version-1-6-installation-guide/035.png)

<span id="_Toc519236708" class="anchor"></span>Figure 4‑5. VistALink Sample Application Re-authentication Page

6.  Press Submit to attempt to run a set of sample RPCs using the end-user and connector criteria specified.
7.  The results, successful or not, are displayed on a result page:

![](vistalink-version-1-6-installation-guide/036.png)

<span id="_Toc519236709" class="anchor"></span>Figure 4‑6. VistALink J2EE Sample Application Results Page

# Rollback Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Stop the new connector using the WebLogic Console.
2.  Start the old connector using the WebLogic Console.

# Appendix A: Installing and Running the J2SE Sample Apps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The instructions in this section for setting up the SwingTester and other sample applications assume the use of a Windows workstation. However, because VistALink is a pure Java application, it is not particularly tied to the Windows client environment.

Four batch files are supplied in the samples-J2SE folder of the distribution, one for each of the four sample applications:

- runSwingTester.bat (runs VistaLinkRpcSwingTester)
- runSwingSimple.bat (runs VistaLinkRpcSwingSimple)
- runSwingSimpleCcow.bat (runs VistaLinkRpcSwingSimpleCcow)
- runRpcConsole.bat (runs VistaLinkRpcConsole)

A fourth batch file manages the environment settings used by each of the three batch files above:

> • setVistaLinkEnvironment.bat

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Install the Java Runtime Environment (JRE)

VistALink 1.6.1 requires the J2SE Java Runtime Environment (JRE) 5.0 (or higher) or the Java Development Kit (JDK) to be installed on the client workstation.

2.  Select J2SE Sample Application Location

To install the J2SE Sample Application files, you should either:

- Configure and run the samples directly in the unzipped distribution folder set, or
- Create a new folder to hold the sample application files, and copy the contents of the \samples-J2SE folder in the distribution file to the new folder.
3.  Configure JAVA_HOME

The JAVA_HOME variable in the provided setVistaLinkEnvironment batch file must be modified to match the location of the Java executable to use on your workstation. You may have multiple Java Runtime Environments (JREs) or Java Development Kits (JDKs) installed on your workstation. The selected JRE for the JAVA_HOME variable must be version 1.5 or higher.

In the setVistaLinkEnvironment.bat file, replace default location for the JAVA_HOME environment variable with the location to use on your system, e.g.:

> REM -- set directory with bin subdirectory containing java.exe

> REM -- (don't include the /bin subdirectory)

> REM -- Note: in general you should obtain the latest v5 JRE available

> set JAVA_HOME=C:\Program Files\Java\jre1.5.0_11

4.  Configure Jar Classpaths

If you are running the sample directly out of the unzipped distribution folder set, you can skip this step (classpaths setVistaLInkEnvironment.bat map to the correct relative folder locations.)

Otherwise, ensure the individual classpath settings in the setVistaLinkEnvironment batch file correctly reflect the locations of each of the following files:

- log4j-core -2.10.0.jar
- log4j-api -2.10.0.jar
- vljConnector-1.6.1.nnn.jar
- vljFoundationsLib-1.6.1.nnn.jar
- vljSecurity-1.6.1.nnn.jar

> Each entry added to the CLASSPATH variable needs to be modified to match the file name and location of the corresponding library on your system, as you installed them above. For example:

> REM -- classpath for log4j

> set CLASSPATH=%CLASSPATH%;./log4j-core-2.10.0.jar;./log4j-api-2.10.0.jar

5.  Grant Yourself Kernel Access to the Sample Application

<span class="mark">The Kernel "B"-type option, VistALink Tester \[XOBV VISTALINK TESTER\] was created as part of the M-side KIDS install. To run the sample application, you will need to grant yourself access to the \[XOBV VISTALINK TESTER</span>\] on the VistA/M server to which you will be connecting (unless you already have Kernel programmer access on the M server).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/037.png)</td>
<td><blockquote>
<p><strong>REF:</strong> For more information on granting yourself access to RPCs, see the <em>RPC Broker Systems Manual</em> on the VistA Documentation Library (VDL) at <a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

6.  Run the SwingTester Sample Application

This version of VistALink includes the SwingTester sample application, which is a diagnostic tool for the client workstation. You can use this sample application to verify and test the VistALink client/server connection and sign-on process. Use the following instructions to use this tool.

To run the SwingTester sample application:

1.  Launch the batch file runSwingTester.bat by double-clicking on it, or run it in a command window. This launches the main sample application, designed to demonstrate VistALink functionality and test server connectivity.
    1.  If the GUI application window opens, the JAVA_HOME and classpath locations have probably been set correctly.
    2.  If the GUI application window does not open, look in the command window output for the reason for failure. Most likely the Java executable was not found at the location specified by JAVA_HOME, or one of the supporting jar files is not in its specified classpath location.
2.  In the ip and port fields, enter the IP and port of the M listener your want to connect to, and press Connect. (Alternatively, you could select an entry in a jaas.config settings file to set the IP and port.)
3.  Click Connect on the Access/Verify Code interface.
4.  Enter the Access / Verify code pair you have been assigned. Click OK.

> ![](vistalink-version-1-6-installation-guide/038.png)

<span id="_Toc41200449" class="anchor"></span>Figure A-2. Test Program Access/Verify Code Entry

5.  If logon is successful, the status changes to "Connected." You can ping the M server, and also execute RPCs using the various tab options in the SwingTester application.
6.  An interface with multiple tabs will display. Click on the RPC List tab. Type "X" in the Enter namespace box. Then click Get RPC List to display the information in the figure below.

> ![](vistalink-version-1-6-installation-guide/039.png)

<span id="_Toc41200450" class="anchor"></span>Figure A-3. SwingTester RPC List

7.  To disconnect, press Disconnect.

Troubleshooting

If the application is unable to launch, check for errors in the command-window output. The most likely source of the problem is incorrect classpath locations set in the batch file.

When connected, you can also use the SwingTester sample app to display and verify your user information.

1.  Click on the User Info tab in the interface shown in the figure below.

> ![](vistalink-version-1-6-installation-guide/040.png)

<span id="_Toc41200451" class="anchor"></span>Figure A-4. Test Program User Information

2.  Click Get user information to display your user data.

Running the Other Sample Applications

In addition to SwingTester, other sample applications are provided. Follow the steps provided in the section on the SwingTester sample application to modify setVistaLinkEnvironment.bat for your JAVA_HOME and for the locations of various libraries.

Unlike the SwingTester sample application, the remaining sample applications require the file jaas.config to be set up with configurations for your M server. (SwingTester allows free-form entry of M server IP and port to connect to.)

To set up jaas.config to hold the configuration for your M server's IP and port:

1.  Modify the jaas.config file in your copied samples files, so that the settings for ServerAddress and ServerPortKey are correct for connecting to your M system.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/041.png)</td>
<td><blockquote>
<p><strong>runRpcConsole.bat</strong> and <strong>runSwingSimple.bat</strong> are hard-coded to load a configuration named "DemoServer" from the <strong>jaas.config</strong> file. Either modify the DemoServer configuration with the settings needed for your M system, or, if you add a different configuration and configuration name, modify <strong>runRpcConsole.bat</strong> and <strong>runSwingSimple.bat</strong> to use your configuration name. (The -s parameter at the end of the command line that launches the application.)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> With jaas.config and setVistaLinkEnvironment.bat configured, you can then use the batch files described below to launch the other two sample applications.

#### runSwingSimple.bat

> runSwingSimple.bat is a simpler Swing application than SwingTester. It is a better programming example program because it lacks the "bells and whistles" of SwingTester. It passes a command line parameter to specify which configuration in the jaas.config file should be used to connect to.

#### runRpcConsole.bat

> runRpcConsole.bat is a console-only sample application. In addition to requiring a command-line parameter to specify the JAAS configuration to connect to, it is dependent on passing an access and verify code on the command line, unless the defaults embedded in the application work (they probably will not).

> You can pass in access and verify codes with additional "-a" and "-v" command-line parameters.

Enabling Log4J Logging for Client Sample Applications (optional)

1.  Assume that c:\Program Files\vistalink\samples is the current directory.
2.  Folder c:\Program Files\vistalink\samples\props contains a sample log4jconfig.xml configuration file with various log4j configuration options.
3.  Each sample application will try to load the log4j configuration from the file named "props\log4jconfig.xml," relative to the current directory. Therefore c:\Program Files\vistalink\samples\props\log4jconfig.xml will be loaded.
4.  The log4j2config.xml file within the c:\Program Files\vistalink\samples\props\\ folder contains extensive information on various log4j configuration options. Look at this simple example of a log4j2config.xml file:

<span id="_Toc519236713" class="anchor"></span>\<?xml version=*"1.0"* encoding=*"UTF-8"*?\>

\<Configuration status=*"WARN"*\>

\<Appenders\>

\<Console name=*"Console"* target=*"SYSTEM_OUT"*\>

\<PatternLayout pattern=*"%d{HH:mm:ss.SSS} \[%t\] %-5level %logger{36} - %msg%n"*/\>

\</Console\>

\</Appenders\>

\<Loggers\>

\<Logger name=*"gov.va.med.vistalink"* level=*"trace"* additivity=*"false"*\>

\<AppenderRef ref=*"Console"*/\>

\</Logger\>

\<Root level=*"error"*\>

\<AppenderRef ref=*"Console"*/\>

\</Root\>

\</Loggers\>

\</Configuration\>

Figure A‑5. log4jconfig.xml file contains extensive information on log4j configuration options

5.  When you run the sample application, you should see "logger" output for debug and error information being displayed on the console window (the window in which you are starting up the application).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/042.png)</td>
<td><blockquote>
<p><strong>An example log4J properties file is provided in the<br />
</strong>&lt;DIST FOLDER&gt;samples-J2SE\props <strong>folder in the distribution ZIP file.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### #### Sample Application Loggers

The following table lists all the loggers used by VistALink sample applications and log levels. System administrators may need to use this list when deciding which loggers to activate in the site's log4j configuration file.

*This page is left blank intentionally.*

<table style="width:100%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><strong>Logger Name</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td><p><strong>Environment</strong></p>
<p><strong>(J2EE | J2SE )</strong></p></td>
<td><strong><br />
Package</strong></td>
<td><strong>Class</strong></td>
<td><strong>Log Levels</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Loggers for the sample applications that demonstrate VistALink functionality</td>
<td>J2SE</td>
<td>gov.va.med.vistalink.samples</td>
<td>VistaLinkRpcSwingSimple</td>
<td>Debug<br />
Error</td>
</tr>
<tr class="odd">
<td></td>
<td>J2SE</td>
<td>"</td>
<td>VistaLinkRpcSwingSimpleCcow</td>
<td>Debug<br />
Error</td>
</tr>
<tr class="even">
<td></td>
<td>J2SE</td>
<td>"</td>
<td>VistaLinkRpcConsole</td>
<td>Debug<br />
Error</td>
</tr>
<tr class="odd">
<td></td>
<td>J2SE</td>
<td>"</td>
<td>VistaLinkRpcConsole.Other</td>
<td>Error</td>
</tr>
<tr class="even">
<td></td>
<td>J2SE</td>
<td>"</td>
<td>VistaLinkRpcSwingTester</td>
<td>Debug</td>
</tr>
<tr class="odd">
<td></td>
<td>J2EE</td>
<td>"</td>
<td>VistaLinkJ2EESample</td>
<td>Debug<br />
Error</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc135124740" class="anchor"></span>Table A-6. VistALink Sample Application Loggers

This page is left blank intentionally.

# Appendix B: DSM/VMS-Specific Install Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/043.png) | NOTE: Most Office of Information and Technology (OI&T) sites have upgraded from Digital Standard Mumps (DSM)/VMS to Caché for VMS. DSM-specific installation information has been retained in this appendix. |

## Operating System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- DSM/VMS: DSM (version 7.2.1 for OpenVMS or greater)

|                                                                                                                |                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| ![](vistalink-version-1-6-installation-guide/044.png) | NOTE: Most DSM/VMS systems in VA OI&T have been converted to Caché/VMS. |

## Global Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 41%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Global Name</strong></td>
<td colspan="2"><p><strong>DSM</strong></p>
<p><strong>for OpenVMS *</strong></p></td>
</tr>
<tr class="even">
<td rowspan="4">^XOB</td>
<td>System:</td>
<td>RWP</td>
</tr>
<tr class="odd">
<td>World:</td>
<td>RW</td>
</tr>
<tr class="even">
<td>Group:</td>
<td>RW</td>
</tr>
<tr class="odd">
<td>UCI:</td>
<td>RW</td>
</tr>
</tbody>
</table>

<span id="_Toc519236714" class="anchor"></span>Figure B‑1. Global protection

## Listener Management for Caché/VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We recommend running VistALink on DSM/VMS systems as a TCP/IP service. See Appendix B, "Listener Management for DSM/VMS Systems," in the *VistALink 1.6 System Management Guide.*

This page is left blank intentionally.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Access Code</th>
<th>A password used by the Kernel system to identify the user. It is used with the verify code.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Adapter</td>
<td>Another term for <em>resource adapter</em> or <em>connector.</em></td>
</tr>
<tr class="even">
<td>Administration Server</td>
<td>Each Oracle WebLogic server domain must have one server instance that acts as the administration server. This server is used to configure all other server instances in the domain.</td>
</tr>
<tr class="odd">
<td>Alias</td>
<td>An alternative filename.</td>
</tr>
<tr class="even">
<td>Alpha/VMS</td>
<td><p>Alpha: Hewlett Packard computer system</p>
<p>VMS: Virtual Memory System</p></td>
</tr>
<tr class="odd">
<td>Anonymous Software Directories</td>
<td>Directories where VHA application, documentation, and patch files are placed for distribution.</td>
</tr>
<tr class="even">
<td>API</td>
<td>Application Program Interface</td>
</tr>
<tr class="odd">
<td>Application Proxy User</td>
<td>A Kernel user account designed for use by an application rather than an end-user.</td>
</tr>
<tr class="even">
<td>Application Server</td>
<td>Software/hardware for handling complex interactions between users, business logic, and databases in transaction-based, multi-tier applications. Application servers, also known as app servers, provide increased availability and higher performance.</td>
</tr>
<tr class="odd">
<td>Authentication</td>
<td>Verifying the identity of the end-user.</td>
</tr>
<tr class="even">
<td>Authorization</td>
<td>Granting or denying user access or permission to perform a function.</td>
</tr>
<tr class="odd">
<td>Base Adapter</td>
<td>Version 8.1 of WebLogic introduced a "link-ref" mechanism enabling the resources of a single "base" adapter to be shared by one or more "linked" adapters. The base adapter is a completely set up standalone adapter. Its resources (classes, jars, etc.) can be linked to and reused by other resource adapters (linked adapters), and the deployer only needs to modify a subset of linked adapters' deployment descriptor settings.</td>
</tr>
<tr class="even">
<td>BEA WebLogic</td>
<td>BEA WebLogic is a J2EE Platform application server. Oracle has acquired BEA Systems, Inc. From here forward it will be referred to as Oracle.</td>
</tr>
<tr class="odd">
<td>Caché/VMS</td>
<td><p>Cache: InterSystems Caché object database that runs SQL</p>
<p>VMS: Virtual Memory System</p></td>
</tr>
<tr class="even">
<td>CCOW</td>
<td>The <em>Clinical Context Object Workgroup</em> is a standard defining the use of a technique called "context management," providing the clinician with a unified view on information held in separate and disparate healthcare applications that refer to the same patient, encounter or user. </td>
</tr>
<tr class="odd">
<td>Classpath</td>
<td>The path searched by the JVM for class definitions. The class path may be set by a command-line argument to the JVM or via an environment variable.</td>
</tr>
<tr class="even">
<td>Client</td>
<td>Can refer to both the client workstation and the client portion of the program running on the workstation.</td>
</tr>
<tr class="odd">
<td>Connection Factory</td>
<td>A J2CA class for creating connections on request.</td>
</tr>
<tr class="even">
<td>Connection Pool</td>
<td>A cached store of connection objects that can be available on demand and reused, increasing performance and scalability. VistALink 1.5 uses connection pooling.</td>
</tr>
<tr class="odd">
<td>Connector</td>
<td>A system-level driver that integrates J2EE application servers with Enterprise Information Systems (EIS). VistALink is a J2EE connector module designed to connect to Java applications with VistA/M systems. The term is used interchangeably with <em>connector module</em>, adapter, <em>adapter module</em>, and <em>resource adapter</em>.</td>
</tr>
<tr class="even">
<td>Connector Proxy User</td>
<td>For security purposes, each instance of a J2EE connector must be granted access to the M server it connects to. This is done via a Kernel user account set up on the M system. This provides initial authentication for the app server and establishes a trusted connection. The M system manager must set up the connector user account and communicate the access code, verify code and listener IP address and port to the J2EE system manager.</td>
</tr>
<tr class="odd">
<td>COTS</td>
<td>Commercial, Off-The-Shelf</td>
</tr>
<tr class="even">
<td>DBF</td>
<td><em>Database file</em> format underlying many database applications (originally dBase)</td>
</tr>
<tr class="odd">
<td>DCL</td>
<td><em>Digital Command Language</em>. An interactive command and scripting language for VMS.</td>
</tr>
<tr class="even">
<td>Division</td>
<td>VHA sites are also called <em>institutions</em>. Each institution has a <em>station number</em> associated with it. Occasionally a single institution is made up of multiple sites, known as <em>divisions</em>. To make a connection, VistALink needs a station number from the end-user's New Person entry in the KERNEL SYSTEM PARAMETERS file (#8989.3). It looks first for a division station number and if it can't find one, uses the station number associated with default institution.</td>
</tr>
<tr class="odd">
<td>DSM</td>
<td><em>Digital Standard MUMPS.</em> An M environment, a product of InterSystems Corp.</td>
</tr>
<tr class="even">
<td>DUZ</td>
<td>Unknown acronym. A local variable holding a number that identifies the signed-on user. The number is the Internal Entry Number (IEN) of the user's record in the NEW PERSON file (file #200)</td>
</tr>
<tr class="odd">
<td>EAR file</td>
<td><em>Enterprise archive</em> file. An enterprise application archive file that contains a J2EE application.</td>
</tr>
<tr class="even">
<td>EIS</td>
<td>Enterprise Information System</td>
</tr>
<tr class="odd">
<td>FatKAAT</td>
<td>Fat-Client (i.e. Rich client) Kernel Authentication and Authorization</td>
</tr>
<tr class="even">
<td>File #18</td>
<td>SYSTEM file #18 was the precursor to the KERNEL SYSTEM PARAMETERS file (#8989.3), and is now obsolete. It uses the same number space that is now assigned to VistALink. Therefore, file #18 must be deleted before VistALink can be installed.</td>
</tr>
<tr class="odd">
<td>FTP</td>
<td>File Transfer Protocol</td>
</tr>
<tr class="even">
<td>Global</td>
<td>A multi-dimensional data storage structure -- the mechanism for persistent data storage in a MUMPS database.</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphical User Interface</td>
</tr>
<tr class="even">
<td>Health<em><u>e</u></em>Vet-VistA</td>
<td>The VHA is converting its MUMPS-based VistA healthcare system to a new J2EE-based platform and application suite. The new system is known as Health<em><u>e</u></em>Vet-VistA.</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>Health Level 7</td>
</tr>
<tr class="even">
<td>IDE</td>
<td><em>Integrated development environment.</em> A suite of software tools to support writing software.</td>
</tr>
<tr class="odd">
<td>Institution</td>
<td>VHA sites are also called <em>institutions</em>. Each institution has a <em>station number</em> associated with it. Occasionally a single institution is made up of multiple sites, known as <em>divisions</em>. To make a connection, VistALink needs a station number from the end-user's New Person entry in the KERNEL SYSTEM PARAMETERS file (#8989.3). It looks first for a division station number and if it can't find one, uses the station number associated with default institution.</td>
</tr>
<tr class="even">
<td>Institution Mapping</td>
<td>The VistALink includes a small utility that administrators can use to associate station numbers with JNDI names, and which allows runtime code to retrieve the a VistALink connection factory based on station number.</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>Information Resource Management</td>
</tr>
<tr class="even">
<td>ISO</td>
<td>Information Security Officer</td>
</tr>
<tr class="odd">
<td>J2CA</td>
<td><em>J2EE Connector Architecture</em>. J2CA is a framework for integrating J2EE-compliant application servers with Enterprise Information Systems, such as the VHA's VistA/M systems. It is the framework for J2EE connector modules that plug into J2EE application servers, such as the VistALink adapter.</td>
</tr>
<tr class="even">
<td>J2CA</td>
<td>J2EE Connector Architecture</td>
</tr>
<tr class="odd">
<td>J2CA CCI</td>
<td>J2EE Connector Architecture Common Client Interface</td>
</tr>
<tr class="even">
<td>J2EE</td>
<td>The <em>Java 2 Platform, Enterprise Edition (J2EE)</em> is an environment for developing and deploying enterprise applications. The J2EE platform consists of a set of services, APIs, and protocols that provide the functionality for developing multi-tiered, Web-based applications. A J2EE Connector Architecture specification for building adapters to connect J2EE systems to non-J2EE enterprise information systems.</td>
</tr>
<tr class="odd">
<td>J2SE</td>
<td><em>Java 2 Standard Edition.</em> Sun Microsystem's programming platform based on the Java programming language. It is the blueprint for building Java applications, and includes the Java Development Kit (JDK) and Java Runtime Environment (JRE).</td>
</tr>
<tr class="even">
<td>JAAS</td>
<td><em>Java Authentication and Authorization Service.</em> JAAS is a pluggable Java framework for user authentication and authorization, enabling services to authenticate and enforce access controls upon users.</td>
</tr>
<tr class="odd">
<td>JAR file</td>
<td>Java archive file. It is a file format based on the ZIP file format, used to aggregate many files into one.</td>
</tr>
<tr class="even">
<td>Java Library</td>
<td>A library of Java classes usually distributed in JAR format.</td>
</tr>
<tr class="odd">
<td>Javadoc</td>
<td>Javadoc is a tool for generating API documentation in HTML format from doc comments in source code. Documentation produced with this tool is typically called Javadoc.</td>
</tr>
<tr class="even">
<td>JBoss</td>
<td>JBoss is a free software / open source Java EE-based application server.</td>
</tr>
<tr class="odd">
<td>JDK</td>
<td><em>Java Development Kit</em>. A set of programming tools for developing Java applications.</td>
</tr>
<tr class="even">
<td>JMX</td>
<td><em>Java Management eXtensions.</em> A java specification for building manageability into java applications, including J2EE-based ones.</td>
</tr>
<tr class="odd">
<td>JNDI</td>
<td><em>Java Naming and Directory Interface</em>. A protocol to a set of APIs for multiple naming and directory services.</td>
</tr>
<tr class="even">
<td>JRE</td>
<td>The <em>Java Runtime Environment</em> consists of the Java virtual machine, the Java platform core classes, and supporting files. JRE is bundled with the JDK but also available packaged separately.</td>
</tr>
<tr class="odd">
<td>JSP</td>
<td><em>Java Server Pages</em>. A language for building web interfaces for interacting with web applications.</td>
</tr>
<tr class="even">
<td>JVM</td>
<td><em>Java Virtual Machine.</em> The JVM interprets compiled Java binary code (byte code) for specific computer hardware.</td>
</tr>
<tr class="odd">
<td>KAAJEE</td>
<td>Kernel Authentication and Authorization for Java 2 Enterprise Edition</td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>Kernel functions as an intermediary between the host M operating system and VistA M applications. It consists of a standard user and program interface and a set of utilities for performing basic VA computer system tasks, e.g., Menu Manager, Task Manager, Device Handler, and security.</td>
</tr>
<tr class="odd">
<td>KIDS</td>
<td><em>Kernel Installation and Distribution System</em>. The VistA/M module for exporting new VistA software packages.</td>
</tr>
<tr class="even">
<td>LDAP</td>
<td>Acronym for <em>Lightweight Directory Access Protocol.</em> LDAP is an open protocol that permits applications running on various platforms to access information from directories hosted by any type of server.</td>
</tr>
<tr class="odd">
<td>Linked Adapter</td>
<td>Version 8.1 of WebLogic introduced a "link-ref" mechanism enabling the resources of a single "base" adapter to be shared by one or more "linked" adapters. The base adapter is a completely set up standalone adapter. Its resources (classes, jars, etc.) can be linked to and reused by other resource adapters (linked adapters), and the deployer only needs to modify a subset of linked adapters' deployment descriptor settings.</td>
</tr>
<tr class="even">
<td>Linux</td>
<td>An <a href="http://www.webopedia.com/TERM/L/open_source.html">open-source</a> Unix-like computer operating system that runs on various types of hardware <a href="http://www.webopedia.com/TERM/L/platform.html">platforms</a>. Linux is one of the most prominent examples of free software and open source development; typically all underlying source code can be freely modified, used, and redistributed. Health<em><u>e</u></em>Vet-VistA servers use both Linux and Windows operating systems.</td>
</tr>
<tr class="odd">
<td>Listener</td>
<td>A socket routine that runs continuously at a specified port to field incoming requests. It sends requests to a front controller for processing. The controller returns its response to the client through the same port. The listener creates a separate thread for each request, so it can accept and forward requests from multiple clients concurrently.</td>
</tr>
<tr class="even">
<td>log4J Utility</td>
<td>An open-source logging package distributed under the Apache Software license. Reviewing log files produced at runtime can be helpful in debugging and troubleshooting.</td>
</tr>
<tr class="odd">
<td>logger</td>
<td>In log4j, a logger is a named entry in a hierarchy of loggers. The names in the hierarchy typically follow Java package naming conventions. Application code can select a particular logger by name to write output to, and administrators can configure where a particular named logger's output is sent.</td>
</tr>
<tr class="even">
<td>M (MUMPS)</td>
<td><em>Massachusetts General Hospital Utility Multi-Programming System</em>, abbreviated M. M is a high-level procedural programming computer language, especially helpful for manipulating textual data.</td>
</tr>
<tr class="odd">
<td>Managed Server</td>
<td>A server instance in a Oracle WebLogic domain that is not an administration server, i.e., not used to configure all other server instances in the domain.</td>
</tr>
<tr class="even">
<td>MBeans</td>
<td>In the Java programming language, an MBean (managed bean) is a Java object that represents a manageable resource, such as an application, a service, a component, or a device. MBeans must be concrete Java classes.</td>
</tr>
<tr class="odd">
<td>Messaging</td>
<td>A framework for one application to asynchronously deliver data to another application, typically using a queuing mechanism.</td>
</tr>
<tr class="even">
<td>Multiple</td>
<td>A VA FileMan data type that allows more than one value for a single entry.</td>
</tr>
<tr class="odd">
<td>Namespace</td>
<td>A unique 2-4 character prefix for each VistA package. The DBA assigns this character string for developers to use in naming a package's routines, options, and other elements. The namespace includes a <em>number space</em>, a pre-defined range of numbers that package files must stay within.</td>
</tr>
<tr class="even">
<td>NEW PERSON File #200</td>
<td>The NEW PERSON file contains information for all valid users on an M system.</td>
</tr>
<tr class="odd">
<td>NIST</td>
<td>National Institute for Standards and Technology</td>
</tr>
<tr class="even">
<td>OI&amp;T</td>
<td>Office of Information &amp; Technology</td>
</tr>
<tr class="odd">
<td>Oracle WebLogic</td>
<td>Oracle WebLogic is a J2EE Platform application server. Oracle has acquired BEA Systems, Inc.</td>
</tr>
<tr class="even">
<td>OS</td>
<td>Operating System</td>
</tr>
<tr class="odd">
<td>Patch</td>
<td>An update to a VistA software package that contains an enhancement or bug fix. Patches can include code updates, documentation updates, and information updates. Patches are applied to the programs on M systems by IRM services.</td>
</tr>
<tr class="even">
<td>Plug-in</td>
<td>A component that can interact with or be added to an application without recompiling the application.</td>
</tr>
<tr class="odd">
<td>ra.xml</td>
<td>ra.xml is the standard J2EE deployment descriptor for J2CA connectors. It describes connector-related attributes and its deployment properties using a standard DTD (Document Type Definition) from Sun.</td>
</tr>
<tr class="even">
<td>Re-authentication</td>
<td>When using a J2CA connector, the process of switching the security context of the connector from the original application connector "user" to the actual end-user<em>.</em> This is done by the calling application supplying a proper set of user credentials.</td>
</tr>
<tr class="odd">
<td>Resource Adapter</td>
<td>J2EE resource adapter modules are system-level drivers that integrate J2EE application servers with Enterprise Information Systems (EIS). This term is used interchangeably with <em>resource adapter</em> and <em>connector</em>.</td>
</tr>
<tr class="even">
<td>Routine</td>
<td>A program or sequence of computer instructions that may have some general or frequent use. M routines are groups of program lines that are saved, loaded, and called as a single unit with a specific name.</td>
</tr>
<tr class="odd">
<td>RPC</td>
<td><em>Remote Procedure Call</em>. A defined call to M code that runs on an M server. A client application, through the RPC Broker, can make a call to the M server and execute an RPC on the M server. Through this mechanism a client application can send data to an M server, execute code on an M server, or retrieve data from an M server</td>
</tr>
<tr class="even">
<td>RPC Broker</td>
<td>The RPC Broker is a client/server system within VistA. It establishes a common and consistent framework for client-server applications to communicate and exchange data with VistA/M servers.</td>
</tr>
<tr class="odd">
<td>RPC Security</td>
<td>All RPCs are secured with an RPC context (a "B"-type option). An end-user executing an RPC must have the "B"-type option associated with the RPC in the user's menu tree. Otherwise an exception is thrown.</td>
</tr>
<tr class="even">
<td>SAD</td>
<td>Software Architecture Document</td>
</tr>
<tr class="odd">
<td>SE&amp;I</td>
<td>Software Engineering &amp; Integration</td>
</tr>
<tr class="even">
<td>Servlet</td>
<td>A Java program that resides on a server and executes requests from client web pages.</td>
</tr>
<tr class="odd">
<td>Socket</td>
<td>An operating system object that connects application requests to network protocols.</td>
</tr>
<tr class="even">
<td>SRS</td>
<td>Software Requirements Specification</td>
</tr>
<tr class="odd">
<td>TCP/IP</td>
<td>Transmission Control Protocol (TCP) and the Internet Protocol (IP),</td>
</tr>
<tr class="even">
<td>TXT</td>
<td>Text file format</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>VACO</td>
<td>Veterans Affairs Central Office</td>
</tr>
<tr class="odd">
<td>Verify Code</td>
<td>A password used in tandem with the access code to provide secure user access. The Kernel's Sign-on/Security system uses the verify code to validate the user's identity.</td>
</tr>
<tr class="even">
<td>VistA</td>
<td><em>Veterans Health Information Systems and Technology Architecture</em>. The VHA's portfolio of M-based application software used by all VA medical centers and associated facilities.</td>
</tr>
<tr class="odd">
<td>VistALink Libraries</td>
<td>Classes written specifically for VistALink.</td>
</tr>
<tr class="even">
<td>VL</td>
<td><em>VistaLink</em> is a runtime and development tool providing connection and data conversion between Java and M applications in client-server and n-tier architectures, to which this document describes the architecture and design.</td>
</tr>
<tr class="odd">
<td>VMS</td>
<td><em>Virtual Memory System</em>. An operating system, originally designed by DEC (now owned by Hewlett-Packard), that operates on the VAX and Alpha architectures.</td>
</tr>
<tr class="even">
<td>VPID</td>
<td><em>VA Person Identifier</em>. A new enterprise-level identifier uniquely identifying VA 'persons' across the entire VA domain.</td>
</tr>
<tr class="odd">
<td>WAR file</td>
<td><em>Web archive</em> file. Contains the class files for servlets and JSPs.</td>
</tr>
<tr class="even">
<td>WebLogic Server</td>
<td>A J2EE application server manufactured by Oracle WebLogic Systems.</td>
</tr>
<tr class="odd">
<td>WebSphere</td>
<td>WebSphere Application Server (WAS) is and IBM application server.</td>
</tr>
<tr class="even">
<td>XLS</td>
<td>Microsoft Office XL worksheet and workbook file format</td>
</tr>
<tr class="odd">
<td>XML</td>
<td>Extensible Markup Language</td>
</tr>
<tr class="even">
<td>XmlBeans</td>
<td>XMLBeans is a Java-to-XML binding framework which is part of the Apache Software Foundation XML project.</td>
</tr>
<tr class="odd">
<td>XOB Namespace</td>
<td>The VistALink namespace. All VistALink programs and their elements begin with the characters "XOB."</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-installation-guide/045.png)</td>
<td><p><strong>REF:</strong> For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the Security and Other Common Services Glossary Web page at the following Web address:</p>
<blockquote>
<p><u>http://vista.med.va.gov/iss/glossary.asp</u></p>
</blockquote>
<p>For a comprehensive list of acronyms, please visit the Security and Other Common Services Acronyms Web site at the following Web address:</p>
<blockquote>
<p><u>http://vista/med/va/gov/iss/acronyms/index.asp</u></p>
</blockquote></td>
</tr>
</tbody>
</table>
*This page is left blank intentionally.*


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: VistALink Version 1.5 Installation Guide

## VistALink 1.5 Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink 1.5 resource adapter is a transport layer that provides communication between Health*<u>e</u>*Vet-VistA Java applications and VistA/M servers, in both client-server and n-tier environments. It allows java applications to execute remote procedure calls (RPCs) on the VistA/M system and retrieve results, synchronously. VistALink 1.5 is also referred to as VistALink J2M.

VistALink consists of Java-side adapter libraries and an M-side listener:

- The adapter libraries use the J2EE Connector Architecture (J2C) 1.0 specification to integrate Java applications with legacy systems.
- The M listener process receives and processes requests from client applications.

VistALink 1.5 can be installed on a VistA/M system with or without previous installation of VistALink 1.0. If version 1.0 is already present, only the new features of VistALink 1.5 will be installed.

### Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The term *resource adapter* is often shortened in this guide to "adapter*,*" and is also used interchangeably with the term *connector*.

### Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File names and directory names are set off from other text using bold font (e.g., config.xml). Bold is also used to indicate GUI elements, such as tab, field, and button names (e.g., "press Delete").

All caps are used to indicate M routines and option names (e.g., XMINET). All caps used inside angle brackets indicate file names to be supplied by the user. Example:

> \<JAVA_HOME\>\bin\java -Dlog4j.configuration=file:///c:/localConfigs/mylog4j.xml

Names for Java objects, methods, and variables are indicated by Courier font. Snapshots of computer displays also appear in Courier, surrounded by a border:

> Select Installation Option: LOAD a Distribution

> Enter a Host File: XOB_1_5.KID

In these examples, the response that the user enters at a prompt appears in bold font:

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

Bold font is also used in code samples to indicate lines of particular interest, discussed in the preceding text:

> \<!DOCTYPE weblogic-connection-factory-dd PUBLIC '-//BEA Systems, Inc.//DTD WebLogic 8.1.0 Connector//EN' 'http://www.bea.com/servers/wls810/dtd/weblogic810-ra.dtd'\>

> \<weblogic-connection-factory-dd\>

> \<connection-factory-name\>VistaLinkAdapter\</connection-factory-name\>

> \<jndi-name\>vlj/testconnector\</jndi-name\>

> \<pool-params\>

> \<initial-capacity\>1\</initial-capacity\>

> \<max-capacity\>1\</max-capacity\>

The following symbols appear throughout the documentation to alert the reader to special information or conditions.

|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                     | Description                                                                                                               |
| ![](vistalink-version-1-5-installation-guide/003.png) | Used to inform the reader of general information and references to additional reading material, including online information. |
| ![](vistalink-version-1-5-installation-guide/004.png)                                                              | Used to caution the reader to take special notice of critical information                                                     |

### Folder Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following logical folder names are used in the J2EE Installation section:

> \<DIST FOLDER\> The location for the unzipped VistALink file.

> \<APPLICATION STAGING FOLDER\> A folder where EAR, WAR and RAR distributions are placed on your application server prior to deployment

> \<HEV CONFIGURATION FOLDER\> A folder placed on the classpath of WebLogic servers, containing configuration files for all Health*<u>e</u>*Vet-VistA applications.

## Additional Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistALink Web Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink website (<http://vista.med.va.gov/migration/foundations/vl/index.htm>) summarizes VistALink architecture and functionality and presents status updates.

### VistALink Documentation Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents are provided in the VistALink 1.5 documentation set:

- *VistALink 1.5 Installation Guide*: Provides detailed instructions for setting up, installing, and configuring the VistALink 1.5 listener on VistA/M servers and the VistALink resource adapter on J2EE application servers. Its intended audience includes server administrators, IRM IT specialists, and Java application developers.
- *VistALink 1.5 System Management Guide*: Contains detailed information on J2EE application server management, institution mapping, the VistALink console, M listener management, and VistALink security, logging, and troubleshooting.
- *VistALink 1.5 Developer Guide*: Contains detailed information about workstation setup, re-authentication, institution mapping, executing requests, VistALink exceptions, Foundations Library utilities, and other topics pertaining to writing code that uses VistALink.
- *VistALink 1.5 Release Notes*: Lists all new features included in the VistALink 1.5 release.
- *Getting Started With the BDK, Chapter 3*: *RPC Overview*. A short guide on writing RPCs from the *RPC Broker* manual.

### BEA Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.5 has been tested and is supported on BEA WebLogic Server 8.1 (Service Pack 4) only. WebLogic product documentation can be found at the following website: <http://edocs.bea.com/>.

## System Administrators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is assumed that the administrators installing VistALink 1.5 will have basic working knowledge of the systems they are administering and deploying applications to. For VistA/M installations, the installer should have working knowledge of VistA/M system administration. Likewise, it is assumed that a J2EE installer has working knowledge of J2EE system administration. It is strongly recommend that both types of administrators obtain training necessary to administer both system types.

## VistALink Distribution Zip File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The person deploying the resource adapter can obtain the VistALink distribution zip file from one of the anonymous.software directories. The distribution zip file contains:

> (root) Readme.txt, ReleaseNotes.rtf

> console\\ VistALink console application (packaged and exploded)

> jars\\ VistALink jar files

> javadoc\\ API javadoc

> log4j\\ logger spreadsheet, and sample log4j config files

> m\\ KIDS build for VistA/M server

> rar\\ VistALink connector

> rar\configExamples\\ example configuration files

> rar\ExplodedVistaLinkRar\\ exploded VistALink connector

> samples\\

> samples\J2EE\\ Sample J2EE application (packaged and exploded)

> samples\J2SE\\ client/server sample applications

## Installation Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA/M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The detailed instructions for installing VistALink on the VistA/M server are presented in chapter 2, "[M Server Installation Procedures](#vistam-server-installation-procedures)." The general steps for installing VistALink on the VistA/M server and links to the appropriate sections in this manual are as follows:

1.  Check installation prerequisites ("[Preparation](#preparation)").
2.  Install the KIDS build ("[Installing VistAlink 1.5 KIDS Build](#_Installing_the_VistALink_1.5 Adapte)").
3.  Set up the VistALink listener ("[Setting up the Listener](#setting-up-the-listener)").
4.  Test the listener ("[Verifying Listener Connectivity](#verifying-listener-connectivity)").
5.  Create the connector proxy user for a specific J2EE server (or data center). This step creates a VistA/M user account for initial authentication for the application server ("[Post-Install: Configuring Connector Proxy User(s) for J2EE Access](#post-install-configuring-connector-proxy-users-for-j2ee-access)").

### J2EE Application Server 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The detailed instructions for installing VistALink on the J2EE application server are presented in Chapter 3, "[WebLogic Application Server Installation Procedures](#_WebLogic_Application_Server_ Instal)." The general steps for installing VistALink on the J2EE application server and links to the appropriate sections in this guide are as follows:

1.  Preparation: review system requirements, request connector proxy user credentials, and obtain VistALink 1.5 distribution file ("[Preparation](#preparation-1)").
2.  If upgrading from a previous installation, remove jars and undeploy the VistALink Console and Sample Applications before the installation ("[Upgrading a Previous Installation](#upgrading-a-previous-installation)").
3.  Install the base resource adapter/connector ("[Installing the VistALink 1.5 Adapter](#_Installing_the_VistALink_1.5 Adapte)").
4.  Verify that the installation is successful ("[Verifying Successful Adapter Installation or Upgrade](#verifying-successful-adapter-installation-or-upgrade)").
5.  Deploy the VistALink console ("[Deploying the VistALink Console](#deploying-the-vistalink-console)").
6.  Deploy the sample application ("[Deploying the Sample J2EE Application](#_Deploying_the_Sample_J2EE Applicati)").
7.  (Optional) Re-configure the adapter to connect to your M system. ("[Testing the Sample App with Your Own M Server](#_Testing_the_Sample_App with Your Ow).")

### System Processes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VistALink users must be stopped
- The VistALink TCP/IP service (VLINK) must be disabled
- Roll-and-scroll and RPC Broker users may remain on the system
- TaskMan does not need to be put into a wait state

|                                                   |                                                                                                                                                                                                |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/006.png) | If you accept a slight risk of jobs getting a CLOBBER/EDITED error, VistALink/Care Management users may remain running. Otherwise stop all other VistALink/Care Management jobs on the system. |

### Deleting File \#18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During testing of VistALink 1.0, it was discovered that some sites might still have an old Kernel file residing on their system called "System file \#18". To support virgin installs, VistALink 1.5 includes steps to check and clean up file \#18.

This file was created in the early 1980s and was a precursor to the current Kernel System Parameters file. However, it is now obsolete and must be removed from your system before the VistALink package can be installed, because it shares the same number space that VistALink was assigned.

You may wish to manually back up and delete System file \#18. If this file is on your system, the VistALink environment check will ask you a series of questions during the installation phase to either abort the installation or allow the VistALink installation to delete the file for you.

## Installing VistALink 1.5 KIDS Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the steps in this section to install VistALink 1.5. [Section 2.3.3](#sample-vistam-installation) contains an example of a complete VistALink 1.5 installation on a VistA/M server.

### Preliminary Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Find the VistALink 1.5 KIDS build (XOB_1_5.KID) in the m folder of the VistALink distribution zip file. You can download the distribution file from the anonymous.software directory on any of the OIFO FTP download sites.

|                                                                                                                |                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/008.png) | The VistALink 1.5 KIDS distribution is contained in the m folder of the VistALink distribution zip file. It is also available as a standalone file on the anonymous.software directories. |

2.  FTP the KIDS build file to the intended VistA/M server.
3.  Log on to your VistA/M server. Select the Programmer Options . . . menu from the Systems Manager Menu option (EVE).
4.  While installing this package on the server, do not run any VistALink-based Client/Server software (e.g., Care Management).

|                                                                                                                |                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/009.png) | Check the system status for any XOBVSKT routines that are running (e.g., VistALink Handler). If you find any of these jobs running on the system, notify users to log off or FORCEX the jobs. Active users may get NOSOURCE or CLOBBER errors. |

5.  If a previous version of VistALink is running on your system, stop the VistALink Listener on the server. Follow your normal procedures to stop the VistALink Listener:
- If your VistALink listener runs via VMS TCP Services, use VMS TCP services to disable the service (listener)
- If your VistALink listener process runs within Caché (not via VMS TCP services), use the Foundations menu to stop the listener.
6.  Stop all VistALink users.

### Build Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use the KIDS Installation option, Load a Distribution \[XPD LOAD DISTRIBUTION\]. Enter "XOB_1_5.KID" as the name of the Host File. This will load three transport globals contained within the distribution:
- XOBU 1.5 Common files and libraries used by all the XOB\* packages and

> menu options to manage site parameters/operations

- XOBV 1.5 Handles system and RPC requests
- XOBS 1.5 M-side security module
2.  You can run the KIDS Installation option, Verify Checksums in Transport Global\[XPD PRINT CHECKSUM\]. This option will ensure the transport global was not corrupted in transit. Use "XOBU 1.5" as the response to the Select INSTALL NAME: prompt.

Follow the example below:

Select Installation Option: Verify Checksums in Transport Global

Select INSTALL NAME: XOBU 1.5 Loaded from Distribution 12/17/05@11:46:46

=\> Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

This Distribution was loaded on Dec 17, 2005@11:46:46 with header of

Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

;Created on Sep 09, 2005@15:09:32

It consisted of the following Install(s):

XOBU 1.5 XOBV 1.5 XOBS 1.5

DEVICE: HOME// TELNET PORT

PACKAGE: XOBU 1.5 Dec 17, 2005 11:49 am PAGE 1

-------------------------------------------------------------------------------

5 Routine checked, 0 failed.

PACKAGE: XOBV 1.5 Dec 17, 2005 11:49 am PAGE 1

-------------------------------------------------------------------------------

17 Routine checked, 0 failed.

PACKAGE: XOBS 1.5 Dec 17, 2005 11:49 am PAGE 1

-------------------------------------------------------------------------------

7 Routine checked, 0 failed.

|                                                                                                                |                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/010.png) | Note: When executing the Verify Checksums option, the checksums for all three packages (XOBU, XOBV, and XOBS) are displayed. However, due to page feeds, you may need to scroll back up to see the checksums for the first two packages. |

3.  Use the KIDS Installation option, Backup a Transport Global \[XPD BACKUP\]. This option creates a MailMan message that will backup all current routines on your VistA/M system that will be replaced by the packages in this transport global. (If you need to preserve components that are not routines, you must back them up separately.)

Follow the example below:

Select Installation Option: BACKUP a Transport Global

Select INSTALL NAME: XOBU 1.5 Loaded from Distribution 12/17/04@11:46:46

=\> Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0\]

This Distribution was loaded on Dec 17, 2005@11:46:46 with header of

Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

;Created on Sep 09, 2005@15:09:35

It consisted of the following Install(s):

XOBU 1.5 XOBV 1.5 XOBS 1.5

Subject: Backup of XOBU 1.5 install on Dec 17, 2005

Replace

Loading Routines for XOBU 1.5.....

Loading Routines for XOBV 1.5.

Routine XOBVLJU is not on the disk.................

Loading Routines for XOBS 1.5....

Routine XOBSRA is not on the disk..

Routine XOBSRA1 is not on the disk..

Routine XOBSRAKJ is not on the disk..

Send mail to: CLARK,DAWN// CLARK,DAWN

Select basket to send to: IN// J2M

4.  Use the KIDS Installation option, Install Package(s) \[XPD INSTALL BUILD\] to install VistALink 1.5.

Enter "XOBU 1.5" at the Select Install Name: prompt and answer the questions as follows:

- Although typically the answer is "No," you can answer "Yes," to the question

> Want KIDS to Rebuild Menu Trees Upon Completion of Install?

> Just remember that rebuilding menu trees will increase patch installation time.

- Answer "No" to the question:

> Want KIDS to INHIBIT LOGONs during the install?

- Answer "No" to the question:

> Want to DISABLE Scheduled Options, Menu Options, and Protocols?

5.  If VistALink has already been set up on your server, restart the VistALink Listener on the server. Follow your normal procedures to start the listener. Otherwise, configuring the listener is a follow-on task (see the section ["Setting up the Listener"](#setting-up-the-listener) ):
- If your VistALink listener runs via VMS TCP services, use VMS TCP services to enable the service (listener).
- If your VistALink listener is started within Caché (not via VMS TCP services), use the Foundations menu to start the listener.

### Sample VistA/M Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of a VistALink 1.5 installation on a VistA/M server:

Installation of XOBU 1.5 on a Caché/VMS system already running XOBU 1.0

Select Kernel Installation & Distribution System Option: INSTallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Play a script

Select Installation Option: 1 Load a Distribution

Enter a Host File: USER\$:\[CLARK\]XOB_1_5.KID

KIDS Distribution saved on Sep 09, 2005@15:09:32

Comment: Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

This Distribution contains Transport Globals for the following Package(s):

XOBU 1.5

XOBV 1.5

XOBS 1.5

Distribution OK!

Want to Continue with Load? YES// y YES

Loading Distribution...

Build XOBU 1.5 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES// YES

XOBU 1.5

Will first run the Environment Check Routine, XOBUENV

\>\>\> Checking environment...

\>\>\> VistALink environment check completed for KIDS Load a Distribution option.

XOBV 1.5

XOBS 1.5

Use INSTALL NAME: XOBU 1.5 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Play a script

Select Installation Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: XOBU 1.5 Loaded from Distribution 12/28/05@09:04:06

=\> Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

This Distribution was loaded on Dec 28, 2005@09:04:06 with header of

Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

;Created on Sep 09, 2005@15:09:32

It consisted of the following Install(s):

XOBU 1.5 XOBV 1.5 XOBS 1.5

DEVICE: HOME// IP network

PACKAGE: XOBU 1.5 Dec 28, 2005 9:04 am PAGE 1

-------------------------------------------------------------------------------

5 Routine checked, 0 failed.

PACKAGE: XOBV 1.5 Dec 28, 2005 9:04 am PAGE 1

-------------------------------------------------------------------------------

17 Routine checked, 0 failed.

PACKAGE: XOBS 1.5 Dec 28, 2005 9:04 am PAGE 1

-------------------------------------------------------------------------------

7 Routine checked, 0 failed.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Play a script

Select Installation Option: Backup a Transport Global

Select INSTALL NAME: XOBU 1.5 Loaded from Distribution 12/28/05@09:04:06

=\> Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

This Distribution was loaded on Dec 28, 2005@09:04:06 with header of

Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

;Created on Sep 09, 2005@15:09:32

It consisted of the following Install(s):

XOBU 1.5 XOBV 1.5 XOBS 1.5

Subject: Backup of XOBU 1.5 install on Dec 28, 2005

Replace

Loading Routines for XOBU 1.5.....

Loading Routines for XOBV 1.5.

Routine XOBVLJU is not on the disk.................

Loading Routines for XOBS 1.5....

Routine XOBSRA is not on the disk..

Routine XOBSRA1 is not on the disk..

Routine XOBSRAKJ is not on the disk..

Send mail to: CLARK,DAWN// CLARK,DAWN

Select basket to send to: IN// J2M

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Play a script

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: XOBU 1.5 Loaded from Distribution 12/28/05@09:04:06

=\> Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

This Distribution was loaded on Dec 28, 2005@09:04:06 with header of

Foundations, VistALink, and VistALink Security v1.5 \[Build: 1.5.0.026\]

;Created on Sep 09, 2005@15:09:32

It consisted of the following Install(s):

XOBU 1.5 XOBV 1.5 XOBS 1.5

Checking Install for Package XOBU 1.5

Will first run the Environment Check Routine, XOBUENV

\>\>\> Checking environment...

\>\>\> VistALink environment check completed for KIDS Install Package option.

Install Questions for XOBU 1.5

Incoming Files:

18.01 FOUNDATIONS SITE PARAMETERS

> **NOTE:** You already have the 'FOUNDATIONS SITE PARAMETERS' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Checking Install for Package XOBV 1.5

Install Questions for XOBV 1.5

Incoming Files:

18.03 VISTALINK LISTENER CONFIGURATION

> **NOTE:** You already have the 'VISTALINK LISTENER CONFIGURATION' File.

18.04 VISTALINK LISTENER STARTUP LOG

> **NOTE:** You already have the 'VISTALINK LISTENER STARTUP LOG' File.

18.05 VISTALINK MESSAGE TYPE (including data)

> **NOTE:** You already have the 'VISTALINK MESSAGE TYPE' File.

I will OVERWRITE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Checking Install for Package XOBS 1.5

Install Questions for XOBS 1.5

Want KIDS to INHIBIT LOGONs during the install? YES//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// IP network

Install Started for XOBU 1.5 :

Dec 28, 2005@09:05:38

Build Distribution Date: Sep 09, 2005

Installing Routines:

Dec 28, 2005@09:05:38

Running Pre-Install Routine: EN^XOBUPRE

Installing Data Dictionaries:

Dec 28, 2005@09:05:38

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing PROTOCOL

Located in the XOBV (VISTALINK) namespace.

Installing LIST TEMPLATE

Installing OPTION

Dec 28, 2005@09:05:39

Running Post-Install Routine: EN^XOBUPOST

Updating Routine file...

Updating KIDS files...

XOBU 1.5 Installed.

Dec 28, 2005@09:05:39

Install Message sent \#2074

Install Started for XOBV 1.5 :

Dec 28, 2005@09:05:39

Build Distribution Date: Sep 09, 2005

Installing Routines:

Dec 28, 2005@09:05:39

Running Pre-Install Routine: EN^XOBVPRE

Installing Data Dictionaries:

Dec 28, 2005@09:05:41

Installing Data:

Dec 28, 2005@09:05:41

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing DIALOG

Installing PROTOCOL

Installing REMOTE PROCEDURE

Installing OPTION

Dec 28, 2005@09:05:41

Running Post-Install Routine: EN^XOBVPOST

Added new Kernel Application Proxy User 'XOBVTESTER,APPLICATION PROXY'.

::This application proxy user account is used in the VistALink sample web

::application, to demonstrate usage of the VistaLinkAppProxyConnectionSpec

::connection spec.

Updating Routine file...

Updating KIDS files...

XOBV 1.5 Installed.

Dec 28, 2005@09:05:41

Install Message sent \#2075

Install Started for XOBS 1.5 :

Dec 28, 2005@09:05:41

Build Distribution Date: Sep 09, 2005

Installing Routines:

Dec 28, 2005@09:05:42

Installing PACKAGE COMPONENTS:

Installing DIALOG

Dec 28, 2005@09:05:42

Updating Routine file...

Updating KIDS files...

XOBS 1.5 Installed.

Dec 28, 2005@09:05:42

Install Message sent \#2076

Call MENU rebuild

Starting Menu Rebuild: Dec 28, 2005@09:05:44

Collecting primary menus in the New Person file...

Primary menus found in the New Person file

------------------------------------------

OPTION NAME MENU TEXT \# OF LAST LAST

USERS USED BUILT

DIUSER VA FileMan 1 10/01/03 07/28/05

XMUSER MailMan Menu 17 05/17/05 07/28/05

EVE.MGT01 Main Menu for Clinical Staff 1 07/28/05

ZZUSER.MCCR MCCR Menu 6 10/28/03 07/28/05

ZZUSER.FRM01 Fileroom Menu 1 10/28/03 07/28/05

EVE.MGT02 Main Menu for Management 1 10/28/03 07/28/05

ZZ PHARMACIST Anchorage Pharmacy 15 10/28/03 07/28/05

EVE.FIS01 Fiscal Service Package Co... 4 10/28/03 07/28/05

ZZEVE.MAS MAS Main Menu 1 10/28/03 07/28/05

ZZEVE.SWS Social Work Service Coord... 2 10/28/03 07/28/05

ZZUSER.FIS01 Fiscal - Operations Menu 6 10/28/03 07/28/05

----snip-----

Building secondary menu trees....

Merging.... done.

Menu Rebuild Complete: Dec 28, 2005@09:06:14

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

> <span id="_Toc135124727" class="anchor"></span>Figure 2. VistALink J2M Installation Example

|                                                                                                                |                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/011.png) | The option XOBV LISTENER STARTUP will be scheduled for Task Manager startup on Caché/NT systems only. |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/012.png) | The installation adds a new Kernel Application Proxy User named "XOBVTESTER,APPLICATION PROXY" to the NEW PERSON file (#200), if not already present. This application proxy user account is used in the VistALink sample Web application to demonstrate usage of the VistaLinkAppProxyConnectionSpec connection spec. |

## Setting up the Listener 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Java applications to connect to your VistA/M system using VistALink, the VistALink listener(s) must be configured to start running on your M system (although not necessarily in M). It waits for and accepts incoming client connections on a specified TCP port, and spawns off handler jobs to service those connection requests.

Configuration of the listener(s) will vary depending on the operating system in use. The sections below provide setup requirements for the Caché/VMS, Caché/NT, and DSM/VMS operating systems, as well as general information for all operating systems.

### VistALink Listeners and Ports (all operating systems)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Though any available TCP port may be used, the recommended port for the VistALink Listener is 8000 for production systems and 8001 for test systems. This recommendation comes from the DBA's list of reserved ports, published on FORUM at DBA Option \| Port Assignments for TCP.

|                                                                                                                |                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/013.png) | The recommended port for the VistALink listener is 8000 for production systems and 8001 for test systems. |

#### Listener Topography

VistALink offers the following listener/Port/IP address possibilities:

- A single VistALink listener, running on any available port.
- Multiple VistALink listeners running on the same IP address/CPU, but listening on *different* ports.

To run one listener in a production account and another in a test account on the same IP address/CPU, you must configure them to listen on different ports (e.g., 8000 for production and 8001 for test). If, on the other hand, you are running the listeners on different IP addresses/CPUs, the ports can be the same (e.g., one VistALink listener on every system listening on port 8000).

Clients accessing your listener will need to be configured with the appropriate listener IP and port.

### Listener Management for Caché/VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We recommend running VistALink on Caché/VMS and DSM/VMS systems as a TCP/IP service. The advantages include the ability to run the TCP/IP service on multiple nodes in a cluster. This allows for an uninterrupted listening process, by redirecting the job if one of the nodes in the cluster goes down. The TaskMan process does not need to be running on the same node as the node the VistALink listener(s) reside on.

The method for starting the TCP listener was written in collaboration with HSITES to aid IRM support staff in running VistALink listener(s) on an M server as a TCP/IP service.

A TCP/IP cookbook and associated VLINK command files to enable and manage VistALink TCP/IP services have been written by HSITES, and can be downloaded from the \[ANONYMOUS.SOFTWARE\] directory at the following FTP sites:

<u>OIFO</u> <u>FTP ADDRESS</u> <u>DIRECTORY</u>

Download Site REDACTED anonymous.software

Albany REDACTED anonymous.software

Hines REDACTED anonymous.software

Salt Lake City REDACTED anonymous.software

The following files are available:

| FILE NAME                | DESCRIPTION                                 |
|------------------------------|-------------------------------------------------|
| VISTALINK_TCPIP_COOKBOOK.DOC | VistALink TCP/IP service cookbook               |
| VLINK_CREATE_UAF.COM         | Used to create OpenVMS user account             |
| VLINK_CREATE_SERVICE.COM     | Used to create the TCP/IP service for VistALink |
| VLINK.COM                    | Used by the VistALink service                   |

These files are provided to assist you in creating or modifying VistALink's VMS user account and command files for both test and production environments. Note that the VLINK files for VistALink 1.5 have changed (e.g., no PIPE commands) from those you might have set up for the VistALink 1.0 service.

- Many of the operations require elevated VMS privileges, specifically, SYSPRV. Before you begin, use the VMS SHOW PROCESS/ALL command to verify that you are logged into an account that has SYSPRV.
- If you need to create the VLINK service, refer to the HSITES cookbook for step-by-step instructions.
- If you have created the VLINK service:
  - Use the TCP/IP utilities to disable the service

> TCPIP\> DISABLE SERVICE VLINK

- FTP the new VLINK.COM file from the ANONYMOUS directory (remember to use ASCII mode when you get the file).
- Copy the new VLINK.com file to the directory used by the VLINK service.
- Modify the file to match the environment. You'll need to remove the comment from the appropriate line in the 'command line:' section and then modify it to match your configuration. Refer to the comments for examples of how the line should be modified.
- Save the file.
- Enable the VLINK service

> TCPIP\> ENABLE SERVICE VLINK

In general, use the VistALink TCP/IP cookbook and VLINK files to help you:

- Set up VistALink as a TCP/IP service in VMS
- Modify the new VLINK files to match your environment
- Modify the VLINK VMS user account (and the .COM file to create the account) with the proper authorized and default privileges (e.g., remove OPER from both). Here are the steps:
  - Enter the VMS authorize utility and SHOW the account to get a 'before' picture

> LASHLEYA_3A1\$ MCR AUTHORIZE

> UAF\> SHOW VLINK

> Username: VLINK Owner: VLINK

> Account: NETWORK UIC: \[50,173\] (\[VLINK\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[VLINK\]

> LGICMD: NL:

> Flags: DisCtlY Restricted DisWelcome DisNewMail DisMail DisReport

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), 9-FEB-2006 08:04 (non-interactive)

> Maxjobs: 0 Fillm: 300 Bytlm: 120000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 1024 JTquota: 4096

> Prclm: 32 DIOlm: 2048 WSdef: 13000

> Prio: 10 ASTlm: 2098 WSquo: 20000

> Queprio: 4 TQElm: 10 WSextent: 65536

> CPU: (none) Enqlm: 3005 Pgflquo: 120000

> Authorized Privileges:

> NETMBX OPER TMPMBX

> Default Privileges:

> NETMBX OPER TMPMBX

> UAF\>

- Now, use the MODIFY command to remove the OPER privilege.

> UAF\> MOD VLINK/DEFPRIVILEGES=NOOPER/PRIVILEGES=NOOPER

> %UAF-I-MDFYMSG, user record(s) updated

- SHOW the VLINK account again to verify that the privilege has been removed from the account as both an Authorized and a Default privilege.

> UAF\> SHOW VLINK

> Username: VLINK Owner: VLINK

> Account: NETWORK UIC: \[50,173\] (\[VLINK\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[VLINK\]

> LGICMD: NL:

> Flags: DisCtlY Restricted DisWelcome DisNewMail DisMail DisReport

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), 9-FEB-2006 08:04 (non-interactive)

> Maxjobs: 0 Fillm: 300 Bytlm: 120000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 1024 JTquota: 4096

> Prclm: 32 DIOlm: 2048 WSdef: 13000

> Prio: 10 ASTlm: 2098 WSquo: 20000

> Queprio: 4 TQElm: 10 WSextent: 65536

> CPU: (none) Enqlm: 3005 Pgflquo: 120000

> Authorized Privileges:

> NETMBX TMPMBX

> Default Privileges:

> NETMBX TMPMBX

- Exit the VMS authorize utility

> UAF\> EXIT

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBNOMODS, no modifications made to rights database

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/014.png) | For further assistance with set-up of a TCP/IP service, log a Remedy ticket so that the appropriate HSITES infrastructure support team can assist you. |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/015.png) | If you have implemented enhanced Caché Cube security as described in AXP INFO \#27, *Enhanced Cach*é *Cube and DCL Access Security*, you will need to grant the new VLINK account access to Caché from the VMS command prompt. Information about enhanced Caché Cube security and instructions for granting access are described in AXP INFO \#27 which can be found on the HealtheSystems Technical Support Team (HSTS) web page at: <http://vaww.va.gov/custsvc/cssupp/axp/default.asp>. The information can also be obtained from FORUM in the SHARED MAIL basket labeled AXP INFO MESSAGES. |

### Listener Management for Caché/NT Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Appendix A, "Listener Management for Caché NT," in the *VistALink 1.5 System Management Guide*.

### Listener Management for DSM/VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Appendix B, "Listener Management for DSM/VMS Systems," in the *VistALink 1.5 System Management Guide.*

## Verifying Listener Connectivity 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The general process for testing the listener is as follows:

1.  Ping the server
2.  Confirm the Listener type via Telnet
3.  Test connectivity with the VistALink J2SE SwingTester sample application

### Ping the Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To detect and avoid network problems, try the following:

1.  Make sure you can reach the VistA/M server you are trying to connect to through TCP.
2.  At the DOS/Command prompt type "PING nnn.nnn.nnn.nnn" for the VistA/M server to which you are trying to connect (where nnn.nnn.nnn.nnn equals the IP address of the server). For example:

> C:\\ PING 127.0.0.1 \<RET\>

|                                                                                                                |                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/016.png) | PING is a way to test connectivity. It sends an Internet Control Message Protocol (ICMP) packet to the server in question and requests a response. It verifies that the server is running and the network is properly configured. |

|                                                                                                                |                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/017.png) | If the VistA/M server is unreachable, there is a network problem, and you should consult with your network administrator. |

### Connect to Listener via Telnet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Telnet from your workstation to the IP address and port of the VistALink listener. On most workstations you can do this simply by entering the telnet IP address port in a command window, e.g.:

c:\\ telnet 10.21.1.85 8000 \<RET\>

2.  When you connect, press \<RET\>. If a VistALink listener is running on that port, you should see echoed something similar to this example:

> \<?xml version="1.0" encoding="utf-8" ?\>\<VistaLink messageType="gov.va.med.foundations.vistalink.system.fault" version="1.5" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"xsi:noNamespaceSchemaLocation="vlFault.xsd"\>\<Fault\>\<FaultCode\>

> Server\</FaultCode\>\<FaultString\>System Error\</FaultString\>\<FaultActor\>\</FaultActor\>\<Detail\>\<Error type="system" code="181001" \>\<Message\>\<\![CDATA\[A system error occurred in M: \<SUBSCRIPT\>SETMSG+5^XOBVRH\]\]\>\</Message\>\</Error\>\</Detail\>\</Fault\>\</

> VistaLink\>♦

> Although there is an error message echoed in this display, the error is due to the fact that you are connecting from telnet rather than from a VistALink client. If an XML message similar to the one above is echoed back, the network connection between your workstation and the VistALink listener at the requested IP address and port is valid.

If you cannot make the telnet connection, there may be a problem somewhere in the network / firewall / machine TCP configuration.

If you connect but do not see XML output similar to that in the sample in step 2 above when you press \<RETURN\>, check the type of listener that is running in the port. (It may be a Broker, HL7, or other type of listener.)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-5-installation-guide/018.png)</td>
<td><p>To disconnect the session, press and hold the CTRL key then press the right brace "]" key: CTRL + ]</p>
<p>This will properly disconnect the telnet connection.</p></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/019.png) | Errors (at SETMSG+5^XOBVRH) will be logged in the Kernel error trap when you use telnet to test the VistALink listener. Such errors can be ignored when Telnet testing is the source. |

### Test Listener with SwingTester J2SE Sample Application (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To test your M listener with the SwingTester sample application, follow the instructions provided in Appendix A of this document, "[Installing and Running the J2SE Sample Applications](#appendix-a-installing-and-running-the-j2se-sample-apps)."

> The SwingTester J2SE (client/server) sample application is supplied in the vljSamples_1.5.0.nnn.jar file.

You can use the SwingTester sample application to perform a standalone test of the M VistALink listener before proceeding with the app server installation. Or you can wait to test the entire setup with J2EE sample apps at the conclusion of the app server installation. (See "[Testing the Sample Application with Your Own M Server](#_Testing_the_Sample_App with Your Ow).")

## Post-Install: Configuring Connector Proxy User(s) for J2EE Access 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow this step only if you are setting up VistALink on your VistA/M system for immediate access by one or more specific J2EE servers.

### Security Caution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-5-installation-guide/020.png)</td>
<td><p>By setting up connector proxy users, you are granting access on your VistA/M server to execute a <u>wide variety of RPCs</u> on your system. Therefore you need to do the following:</p>
<ul>
<li><p>Create connector proxy users only for J2EE systems needing access to your M system.</p></li>
<li><p>Give the access/verify codes (credentials) of the connector proxy users to approved server administrators only.</p></li>
<li><p>Create a different connector proxy user (with different access/verify code credentials) for each J2EE cluster (or data center) that will be connecting to your VistA/M system.</p></li>
<li><p>Prevent dissemination of the access/verify codes for a connector proxy user outside of secure communication channels.</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Connector Proxy Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To allow VistALink access from a specific J2EE system (app server), you need an M Kernel "connector proxy user" account. Each connector deployed on the app server uses this account to establish initial authentication and a trusted connection. Creating this account is not part of the M-side VistALink installation per se, but needs to be performed in M before app server installation can be completed.

A connector proxy account represents a specific application server (not an end-user). A VistALink adapter logs on to the VistA/M server using the assigned Kernel connector proxy user account, authenticating with an access/verify code pair. The connector proxy user account is used by the VistALink connection pool each time it creates a new connection to your VistA/M system.

### Creating the Connector Proxy User Kernel Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vista/M system manager is the only one who can grant access to incoming VistALink connections from a J2EE system. Using the Foundations Management menu, the system manager must create a distinct Kernel account to allow VistALink access from any specific J2EE system. The Kernel account must be a "connector proxy user" account, which is created using the CONT^XUSAP entry point (provided by Kernel as part of patch XU\*8.0\*361).

The VistA/M system manager should do the following:

- Create a Kernel "connector proxy" user account for each distinct J2EE system connecting to the M server through VistALink.
- Securely communicate the access code, verify code, and listener IP address and port to (each) J2EE system manager configuring an adapter to access the VistA/M system.

|                                                                                                                |                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/021.png) | The Kernel XUMGR key is required to create the connector proxy user account. |

To create a "Connector Proxy User" account for a J2EE resource adapter, or "connector" user, follow these steps:

1.  You must hold the Kernel XUMGR key.
2.  Add a new connector proxy user by using the Foundations Management Menu \[XOBU SITE SETUP MENU\] on your VistA/M system, and choosing the Enter/Edit Connector Proxy User action.

> The account requires no more information than what is prompted for by the option.

3.  Leave the connector proxy user's Primary Menu empty.
4.  Securely communicate the access code and verify code you enter for the connector proxy user (in addition to the IP and port of your VistALink listener) to the J2EE system manager setting up access from J2EE to your system.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-5-installation-guide/022.png)</td>
<td><p>You should observe the following points when creating or editing connector proxy users:</p>
<ul>
<li><blockquote>
<p>Do not enter divisions for a connector proxy user</p>
</blockquote></li>
<li><blockquote>
<p>Do not enter a primary menu</p>
</blockquote></li>
<li><blockquote>
<p>Do not also use the connector proxy user as a test "end-user"</p>
</blockquote></li>
<li><blockquote>
<p>Utilize the user <em>only</em> as a connector proxy user</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/023.png) | To generate a list of existing proxy users on the VistA/M system, use the Operations Management…\|User Management Menu…\|Proxy User List \[XUSAP PROXY LIST\] option. |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/024.png) | The Office of Cyber and Information Security (OCIS) has provided draft guidance documents on the required means and process for securely communicating the connector proxy credentials to the J2EE application server administrator. Three draft documents are available for review: *Briefing Note*, *Memorandum*, and *Memorandum of Understanding*. Please contact Ms. Gail Belles for the status of these documents and for directions to obtain the official versions. |

The steps to create a connector proxy user account are detailed in the following example. Here, the site system manager (or designee) is creating a connector proxy user for the Falling Waters data center. Note that you can name the connector proxy user anything you wish.

![](vistalink-version-1-5-installation-guide/025.png)

> <span id="_Toc135124728" class="anchor"></span>Figure 3. Creating a Connector Proxy User Account

SP Site Parameters SL Start Listener

CFG Manage Configurations STP Stop Listener

CP Enter/Edit Connector Proxy User SB Start Box

RE Refresh CU Clean Up Log

SS System Status

Select Action: Quit// CP Enter/Edit Connector Proxy User

Enter NPF CONNECTOR PROXY name : CONNECTOR,FALLING WATERS

Are you adding 'CONNECTOR,FALLING WATERS' as

a new NEW PERSON (the 14227TH)? No// Y (Yes)

Checking SOUNDEX for matches.

CONNECTOR,TEST PROXY

CONNECTOR,AAC CHDR

CONNECTOR,HINES EMC

Do you still want to add this entry: NO//Y

Want to edit ACCESS CODE (Y/N): Y

Enter a new ACCESS CODE \<Hidden\>: \*\*\*\*\*\*\*\*\*\*\*

Please re-type the new code to show that I have it right: \*\*\*\*\*\*\*\*\*\*\*

OK, Access code has been changed!

The VERIFY CODE has been deleted as a security measure.

The user will have to enter a new one the next time they sign-on.

Want to edit VERIFY CODE (Y/N): Y

Enter a new VERIFY CODE: \*\*\*\*\*\*\*\*\*\*

Please re-type the new code to show that I have it right: \*\*\*\*\*\*\*\*\*\*

OK, Verify code has been changed!

To list existing proxy user accounts (connector and application proxy users) on the VistA/M system, use the Proxy User List option, \[XUSAP PROXY LIST\].

FIND Find a user

List users

Print Sign-on Log

Proxy User List

Release user

User Inquiry

User Status Report

Select User Management Menu Option: PROXY User List

DEVICE: IP network

PROXY USER LIST MAR 23,2006 13:28 PAGE 1

NAME User Class ISPRIMARY

------------------------------------------------------------------------

XOBVTESTER,APPLICATION PROXY APPLICATION PROXY

CONNECTOR,AAC CHDR CONNECTOR PROXY Yes

CONNECTOR,HINES EMC CONNECTOR PROXY Yes

CONNECTOR,FALLING WATERS CONNECTOR PROXY Yes

|                                                   |                                                                                                                                                                                                                                                          |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/026.png) | The connector proxy names shown above are examples to illustrate the Proxy User List option. You may choose to name the connector proxy user account(s) differently. Sites do not create and should not modify the application proxy user account names. |

### VistA/M Server Installation Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This completes the VistALink 1.5 VistA/M system installation activities. You have successfully:

- Installed the VistALink 1.5 KIDS build
- Created/modified the VLINK TCP/IP service VMS user account and command files
- Confirmed the new VLINK service is enabled
- Created a connector proxy user account (if necessary)

### J2CA Deployment Descriptor Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The structure of a resource adapter and its runtime behavior are defined in deployment descriptors. The deployment descriptors are created by programmers during the packaging process and become part of the application deployment when the application is compiled.

Resource adapters have two deployment descriptors that affect configuration of the adapter targeted at WebLogic servers. Both files are located in the META-INF directory for each VistALink RAR (packaged adapter):

- ra.xml: The standard J2EE deployment descriptor for J2EE resource adapters (connectors) such as VistALink. This file describes VistALink's connector-related attributes and its deployment properties using a standard Document Type Definition (DTD) from Sun.
- weblogic-ra.xml: Contains WebLogic-specific extended configuration information.

There are various tools available for editing these files. For example, you can use:

- *WebLogic Builder* application (packaged RARs). This tool allows you to edit the deployment descriptor files inside a packaged RAR without needing to un-jar and re-jar the RAR.
- The WLS console configuration tabs to view and modify a subset of the deployment descriptor elements (exploded RAR deployments only. Some of the descriptor element changes take effect dynamically at run-time without redeploying the resource adapter. Other descriptor elements will require redeployment.
- An XML editor such as XMLSpy (exploded RAR only)
- A text editor such as Notepad (exploded RAR only).

### Overview of Base and Linked Adapters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version 8.1 of WebLogic introduced a "link-ref" mechanism, enabling resources of a single "base" adapter to be shared by one or more "linked" adapters. The base adapter is merely a completely set up standalone adapter. Its resources (classes, jars, etc.), however, can be linked to and reused by other resource adapters (linked adapters). Each linked adapter needs only a subset of files and deployment descriptor settings.

When setting up multiple VistALink adapters, for connections to multiple VistA/M systems, we recommend setting up one adapter as a base adapter, and any additional adapters as linked adapters. You must always have at least one base adapter set up to some VistA/M system. Each linked adapter refers back to the base adapter via the weblogic-ra.xml "\<ra-link-ref\>" property.

For more information related to configuring base and linked adapters, see "Adapter Configuration," in the *VistALink 1.5 System Management Guide*.

### Obtain Connector Proxy User and Listener Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are configuring a new adapter, contact the VistA/M system's Information Security Officer (ISO) and/or the VistA/M system manager to obtain the connector proxy user's credentials for the VistA/M system to which you intend to connect. This information includes:

- Access/verify codes for connector proxy user
- VistALink listener port
- IP address of the VistA/M system

See the section ["Post Install: Configure Connector Proxy User(s) for J2EE Access"](#post-install-configuring-connector-proxy-users-for-j2ee-access) in this guide for more information on the connector proxy user.

## Upgrading a Previous Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Remove Jars in Exploded RAR Directories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To clean up existing adapters: remove or delete all jars from the exploded RAR directory of each existing adapter.

### Undeploy VistALink Console and Sample Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have an existing VistALink installation, we are currently recommending that you undeploy previous versions of the VistALink console and sample applications. Follow the steps below:

1.  If you have deployed the VistALink Console, delete it from the WebLogic configuration by navigating to

mydomain\>Deployments\>Web Application Modules

and clicking on the trashcan icon (![](vistalink-version-1-5-installation-guide/028.png)).

2.  If you have deployed the VistALink sample web applications, delete them from the WebLogic configuration by navigating to  
      
    mydomain\>Deployments\>Applications

and clicking on the trashcan icon (![](vistalink-version-1-5-installation-guide/029.png)).

## Installing the VistALink 1.5 Adapter(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The resource adapter is the central piece of the J2CA 1.0 Connector Architecture. It serves as the connector between the Java client application and a VistA/M system. Each VistALink resource adapter deployed in a J2EE application server environment allows Health*<u>e</u>*Vet applications to access a specific VistA/M system.

The next few steps are for first-time installations only. If upgrading existing adapters, skip ahead to section ["Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat)." These steps assume, for the sake of simplicity, that you are deploying a single VistALink adapter.

|                                                                                                                |                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/030.png) | In the case of first time installations, these instructions assume, for the sake of simplicity, that you are deploying a single VistALink adapter. |

|                                                                                                                |                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/031.png) | The next few steps are for first-time installations only. If upgrading existing adapters, skip ahead to section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat)." |

### Set up Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(For first-time installations only. If upgrading adapters, skip to the section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat).")

#### Create \<HEV Configuration Folder\>

(For first-time installations only. If upgrading adapters, skip to the section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat).")

We recommend using a single folder for configuration files for all HEV applications, including VistALink. If it is not already present, you should create this folder on each separate physical WebLogic server.

1.  Create a folder to place on the server classpath for each of your WebLogic servers running VistALink. This folder will be referred to as the \<HEV CONFIGURATION FOLDER\> in the following steps.

#### Create VistALink Configuration File

(For first-time installations only. If upgrading adapters, skip to the section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat).")

VistALink makes use of its own configuration file to load VistALink-specific connector settings. You will need to include one entry for each VistALink adapter. The rules for this file are as follows:

- It must be named "gov.va.med.vistalink.connectorConfig.xml"
- It must be placed in a folder on the Java classpath of the Java Virtual machine (JVM) of each WebLogic server instance on which you are deploying VistALink adapters.

The following are also recommended:

- Using this folder to hold configuration files for all Health*<u>e</u>*Vet-VistA applications
- Creating this folder for each physical server
- Ensuring that this folder is secure and protected. The gov.va.med.vistalink.connectorConfig.xml file holds login credentials for accessing VistA/M systems. On Linux systems, access to the folder should be restricted to the account or group under which WebLogic runs. On all J2EE systems, access to the host file system should be protected.

To create the VistALink configuration file:

1.  Locate the example configuration file provided in the VistALink distribution zip file:

> \<DIST FOLDER\>/RAR/configExamples/gov.va.med.vistalink.connectorConfig.xml

> This example configuration file contains a single entry, identified by the jndiName attribute vlj/testconnector. This entry is pre-configured to connect to a VistALink demo VistA/M server in Albany, NY, that runs the latest VistALink M listener.

2.  Copy the provided configuration file into the \<HEV CONFIGURATION FOLDER\> on each physical server that will be running VistALink adapters. You may want to include the administration server as well.
3.  Later in this installation procedure you will add the \<HEV CONFIGURATION FOLDER\> folder to the Java classpath of your WebLogic server JVM(s).

For additional information on setting up a connector configuration file, see the section <span class="mark"></span>"VistALink Connector Configuration File," in the *VistALink 1.5 System Management Guide*.

#### Create log4j Configuration File

(For first-time installations only. If upgrading adapters, skip to the section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat).")

To turn on logging for VistALink, you need to set up a log4j configuration file for each WebLogic server running VistALink. You also need to pass the name and location to each JVM by one of the following methods:

- Name the file "log4j.xml" and place it in the \<HEV CONFIGURATION FOLDER\>, on your server classpath. (This is probably the easier approach.)
- Give the file a name of your choice, place it anywhere on your physical file system for each physical server, and pass the location of the file to the JVM at WebLogic startup via the -Dlog4j.configuration JVM argument. (See the section below, ["Set JVM Arguments,"](#update-weblogic-server-jvm-arguments) for more information on JVM arguments.)

You may already have a log4j configuration file active for your server, possibly containing loggers and appenders for applications other than VistALink. If so, you may want to add to the existing file the logger entries for VistALink. (For HEV configurations, a single JVM-wide log4j configuration is expected to be used.)

If you need a log4j configuration file and do not already have one set up, follow these steps:

1.  Copy one of the sample log4j configuration files provided in the VistALink distribution zip file.

> These sample files may be located in the \<DIST FOLDER\>/log4j/configExamples folder. They are named:

- log4jVLJConfig.xml (minimal VistALink logging configuration)
- log4jVLJConfigDebug.xml (debug-level VistALink logging configuration).

> Note: Turning on the "debug" level can adversely affect system performance.

2.  Name the file "log4j.xml" and place it in your \<HEV CONFIGURATION FOLDER\>.

### Create VistALink Adapter(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(For first-time installations only. If upgrading adapters, skip to the section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat).")

#### Create an Application Staging Folder

(For first-time installations only. If upgrading adapters, skip to the section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat).")

A folder is needed to hold the EARs, WARs, and adapter RAR folders that you create prior to deployment. The instructions and examples in this chapter refer to this folder as the "staging folder." The name "/bea-stage" is suggested for this folder, though you can name it something else. You can use the same staging folder for other application deployments if you wish (not just VistALink).

1.  If you don't already have a staging folder, create one on each separate physical server.

> In the instructions in the rest of this document, this folder will be referred to as the \<APPLICATION STAGING FOLDER\>.

#### Create an Adapter Folder 

(For first-time installations only. If upgrading adapters, skip to the section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat).")

You must create a folder under your \<APPLICATION STAGING FOLDER\> for each adapter you are deploying (e.g., "\bea-stage\vljSalem658", "\bea-stage\vljBoston523", etc.). The folder name will become the default deployment name for the adapter when displayed in the WebLogic console. So choose folder names that will identify each adapter mnemonically to the administrators viewing them in the WebLogic console.

1.  Create a single folder in the \<APPLICATION STAGING FOLDER\> (e.g., "\bea-stage\testConnector"). Use a folder name that will readily identify the adapter.

#### Copy the VistALink RAR Adapter 

(For first-time installations only. If upgrading adapters, skip to the section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat).")

For each adapter you are deploying, copy the RAR files from the \<DIST FOLDER\>RAR folder to the new adapter staging folder(s).

The adapter is provided in the \<DIST FOLDER\>RAR folder of the VistALink distribution zip file in two formats:

- Exploded RAR: the contents of the \<DIST FOLDER\>RAR /ExplodedVistaLinkRAR folder
- Packaged RAR: one file, \<DIST FOLDER\>RAR /vljConnector-1.5.0.rar

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/032.png) | At the current time, we recommend deploying the exploded form of the adapter, to allow for easier editing of deployment descriptors. |

1.  Copy the entire file structure from inside the \<DIST FOLDER\>RAR /ExplodedVistaLinkRAR folder to your single adapter folder

> (e.g., "bea-stage/testConnector"). The contents of your adapter folder will then be preconfigured to create a "base" adapter configured to connect to the VistALink demo server in Albany.

#### Edit the Adapter Deployment Descriptor Files

(For first-time installations only. If upgrading adapters, skip to the section "[Update the WebLogic Server Classpath](#_Update_the_WebLogic_Server Classpat).")

To configure the adapter, edit the ra.xml and weblogic-ra.xml files in each adapter folder. These files are in the META-INF subfolder of each adapter folder.

If you are deploying adapters for the first time, we recommend leaving the settings in weblogic-ra.xml as they are, and making sure that ra.xml is configured to first connect to the VistALink demo server in Albany.

1.  Verify that the connectorJndiName config-property is set to "vlj/testconnector" in the ra.xml file. This way, on deployment, the adapter will retrieve the pre-configured entry of the same name from the distributed version of gov.va.med.vistalink.connectorConfig.xml.

\<config-property\>

\<config-property-name\>connectorJndiName\</config-property-name\>

\<config-property-type\>java.lang.String\</config-property-type\>

\<config-property-value\>vlj/testconnector\</config-property-value\>

\</config-property\>

2.  Proceed to the section ["Update the WebLogic Server Classpath."](#_Update_the_WebLogic_Server Configur)

### Update the WebLogic Server Classpath

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You now need to add or update several libraries on the server classpath for each server you are deploying adapters to. You may want to create a separate folder in the \<APPLICATION STAGING FOLDER\> to hold these library jar files (e.g., bea-stage\ClasspathLibraries).

You must also set several properties when launching any JVMs for WebLogic servers that VistALink adapters are deployed to.

#### Copy Jars to the WebLogic Server Classpath Locations

For both upgrades and new installations, the following jar files need to be copied from the VistALink distribution zip file to locations on the WebLogic server classpath:

- vljConnector-1.5.0.nnn.jar
- vljFoundationsLib-1.5.0.nnn.jar
- jaxen-core.jar
- jaxen-dom.jar
- log4j-1.2.8.jar
- saxpath.jar
- xbean.jar

If upgrading a previous installation, delete or archive any older versions of these files before copying the new ones. This set of jars is provided inside the rar\ExplodedVistaLinkRAR directory of the distribution zip file, in the root of that directory (vlj\*.jar) and in the lib subdirectory of the remaining jars. Place them in a location that will be easy to add to the server classpath, possibly as a single directory.

#### Single Server (One-Server Domain) 

Copy the jar files to (preferably) a single directory on the single server.

#### Managed Server (Multi-Server Domain)

Copy the jar files to (preferably) a single directory on each target server.

#### Admin Server (Multi-Server Domain)

Ordinarily, the jar files do not need to be placed on the admin server. (In a multi-server environment, VistALink connectors will usually not be run on an admin server.)

#### Update the Server Classpath.

Seven jar files and one directory need to be added to the server classpath:

- vljConnector-1.5.0.nnn.jar
- vljFoundationsLib-1.5.0.nnn.jar
- jaxen-core.jar
- jaxen-dom.jar
- log4j-1.2.8.jar
- saxpath.jar
- xbean.jar
- the \<HEV CONFIGURATION FOLDER\>, containing your gov.va.med.vistalink.connectorConfig.xml and (possibly) the log4j.xml files you created earlier in this installation.

For upgrades to existing installations, the classpath needs to be updated to reflect the new jar versions.

The method to update the server classpath depends on how you start your listener. The sections below explain how to modify the classpath for the following configurations:

- Single server (one-server domain)
- Managed server (multi-server domain)
- Administration server (multi-server domain)

#### Single Server (One-Server Domain)

You must edit the WebLogic domain's startWebLogic.cmd (Windows) or startWebLogic.sh script (Linux), used to start WebLogic for your domain. Add or update the jar file names you copied in the previous step and their directory to the classpath that is passed to the JVM that starts up the application server.

1.  After the line "set "JAVA_VENDOR=Sun" in the startWebLogic.cmd script, set up the VLJ_CP variable to match the following example:

> -------------------\<snip\>--------------------

> set JAVA_VENDOR=Sun

> @rem setup VistALink classpath variable VLJ_CP

> @rem you need to set VLJ_STAGE for your configuration

> set VLJ_STAGE=c:\\bea\bea-stage\\ClasspathLibraries

> set VLJ_CP=%VLJ_STAGE%\vljConnector-1.5.0.nnn.jar

> set VLJ_CP=%VLJ_CP%;%VLJ_STAGE%\vljFoundationsLib-1.5.0.nnn.jar

> set VLJ_CP=%VLJ_CP%;%VLJ_STAGE%\jaxen-core.jar

> set VLJ_CP=%VLJ_CP%;%VLJ_STAGE%\jaxen-dom.jar

> set VLJ_CP=%VLJ_CP%;%VLJ_STAGE%\log4j-1.2.8.jar

> set VLJ_CP=%VLJ_CP%;%VLJ_STAGE%\saxpath.jar

> set VLJ_CP=%VLJ_CP%;%VLJ_STAGE%\xbean.jar

> set VLJ_CP=%VLJ_CP%;c:\\myCommonConfigFolder

> -------------------\<snip\>--------------------

> The name of the VistALink version must be exact in lines 5 and 6 in the example above (shown in bold). If the \<APPLICATION STAGING FOLDER\> name in line 4 and the \<HEV CONFIGURATION FILE\> folder name in the last line are different than those in the example, they must be changed accordingly.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-5-installation-guide/033.png)</td>
<td><blockquote>
<p>If you are using a variable such as VLJ_STAGE in the startup script as a shortcut reference to a single folder holding all your libraries, make sure you update it to the location where you have placed all the libraries in this install.</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Add VLJ_CP variable to the WebLogic Classpath (startWebLogic.cmd). Change:

> set CLASSPATH=%WEBLOGIC_CLASSPATH%;%POINTBASE_CLASSPATH%;%JAVA_HOME%\jre\lib\rt.jar;%WL_HOME%\server\lib\webservices.jar;%CLASSPATH%

> to:

> set CLASSPATH=%WEBLOGIC_CLASSPATH%;%VLJ_CP%;%POINTBASE_CLASSPATH%;%JAVA_HOME%\jre\lib\rt.jar;%WL_HOME%\server\lib\webservices.jar;%CLASSPATH

> <u>Linux startWebLogic.sh Example</u>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-5-installation-guide/034.png)</td>
<td><p>The <strong>&lt;USER_DOMAIN_HOME&gt;/startWebLogic.sh</strong> file needs to be modified for the classes contained in the VistALink jar files and third party jar files to be found at run-time.</p>
<p><strong>1. Add the following lines after the line "JAVA_VENDOR=" line:</strong></p>
<blockquote>
<p>-------------------&lt;snip&gt;--------------------</p>
<p>JAVA_VENDOR="Sun"</p>
<p>#rem setup VistALink classpath variable VLJ_CP</p>
<p>#rem you need to set VLJ_STAGE for your configuration<br />
VLJ_STAGE="/opt/bea-stage"</p>
<p>VLJ_CP="${VLJ_STAGE}/vljConnector-1.5.0.nnn.jar"</p>
<p>VLJ_CP="${VLJ_CP}:${VLJ_STAGE}/vljFoundationsLib-1.5.0.nnn.jar"</p>
<p>VLJ_CP="${VLJ_CP}:${VLJ_STAGE}/jaxen-core.jar"</p>
<p>VLJ_CP="${VLJ_CP}:${VLJ_STAGE}/jaxen-dom.jar"</p>
<p>VLJ_CP="${VLJ_CP}:${VLJ_STAGE}/log4j-1.2.8.jar"</p>
<p>VLJ_CP="${VLJ_CP}:${VLJ_STAGE}/saxpath.jar"</p>
<p>VLJ_CP="${VLJ_CP}:${VLJ_STAGE}/xbean.jar"</p>
<p>VLJ_CP="${VLJ_CP}:/opt/myCommonConfigFolder"</p>
<p>-------------------&lt;snip&gt;--------------------</p>
</blockquote>
<p><strong>2. Modify the line</strong></p>
<blockquote>
<p>CLASSPATH="${WEBLOGIC_CLASSPATH}:${POINTBASE_CLASSPATH}:${JAVA_HOME}/jre/lib/rt.jar:${WL_HOME}/server/lib/webservices.jar:${CLASSPATH}"</p>
<p>to</p>
<p>CLASSPATH="${WEBLOGIC_CLASSPATH}<strong>:${VLJ_CP}</strong>:${POINTBASE_CLASSPATH}:${JAVA_HOME}/jre/lib/rt.jar:${WL_HOME}/server/lib/webservices.jar:${CLASSPATH}"</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Managed Server (Multi-Server Domain) 

Managed servers are started from the WebLogic console. You must modify the Configuration \| Remote Start "classpath" setting in the WebLogic console for each managed server that will have VistALink adapters deployed to it. Then you must add or update the jar file names at the locations you copied them to (see previous step) and directory to the classpath.

On Windows systems, if you set any value in the Remote Start "classpath," you must specify all the jars needed by WebLogic to start the managed server – not just the VistALink-related jars listed at the beginning of this section.

On Linux systems, you may be able to use the string \${CLASSPATH} to pick up the existing non-VistALink classpath needed by WebLogic in the Remote Start "classpath," depending on your Node Manager setup. In that case, you would only need to specify \${CLASSPATH} in addition to the jars needed for VistALink.

> <u>"Remote Start" Classpath Example</u>

> C:\bea\jdk141_05\lib\tools.jar;C:\bea\WEBLOG~1\server\lib\weblogic_sp.jar;C:\bea\WEBLOG~1\server\lib\weblogic.jar;C:\bea\WEBLOG~1\server\lib\ojdbc14.jar;C:\bea\WEBLOG~1\common\eval\pointbase\lib\pbserver44.jar;C:\bea\WEBLOG~1\common\eval\pointbase\lib\pbclient44.jar;C:\bea\jdk141_05\jre\lib\rt.jar;C:\bea\WEBLOG~1\server\lib\webservices.jar;c:/bea-stage/ClasspathLibs/jaxen-core.jar;c:/bea-stage/ClasspathLibs/jaxen-dom.jar;c:/bea-stage/ClasspathLibs/log4j-1.2.8.jar;c:/bea-stage/ClasspathLibs/saxpath.jar;c:/bea-stage/ClasspathLibs/vljConnector-1.5.0.nnn.jar;c:/bea-stage/ClasspathLibs/vljFoundationsLib-1.5.0.nnn. jar;c:/bea-stage/ClasspathLibs/xbean.jar;c:/myCommonConfigFolder;

|                                                                                                                |                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/035.png) | The values needed vary with the server configuration. One way of obtaining the classpath libraries needed for a WebLogic managed server is to use the startManagedWebLogic startup script to capture the classpath echoed to the console, and then use that classpath to fill in the Remote Start classpath value. |

<u>Linux Example</u>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-5-installation-guide/036.png)</td>
<td><p><strong>Note:</strong> On Linux systems, you may be able to use the value ${CLASSPATH} to include the existing non-VistALink classpath needed by WebLogic, depending on your Node Manager setup. If not, follow the same technique as to obtain the jars needed by WebLogic as you would on a Windows system.</p>
<blockquote>
<p>${CLASSPATH}:/u01/app/staged/vl/vljConnector-1.5.0.nnn. jar: /u01/app/staged/vl/vljFoundationsLib-1.5.0.nnn.jar:/u01/app/staged/vl/jaxen-dom.jar: /u01/app/staged/vl/jaxen-core.jar:/u01/app/staged/vl/log4j-1.2.8.jar: /u01/app/staged/vl/saxpath.jar:/u01/app/staged/vl/xbean.jar:/opt/myCommonConfigFolder:</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Admin Server (Multi-Server Domain) 

In order to make it easy to use the VistALink Configuration Editor, you should consider placing a folder containing the VistALink configuration file on the classpath of the admin server, in multi-server domain.

In a production setting, VistALink adapters will probably not be deployed on admin servers. Therefore, there is no reason to put VistALink (and supporting) libraries on the server classpath.

Likewise, there is no requirement to put a folder containing the VistALink configuration file on the admin server's classpath. However, doing so makes it easy to edit the configuration file using the Configuration Editor. If such a folder is on the admin server classpath, the Configuration Editor can load the VistALink configuration file without prompting and save it on the admin server.

> **NOTE:** After editing on the admin server, you can propagate/copy the configuration file out to the managed servers.

The Configuration Editor is deployed as part of the VistALink console, which runs on the admin server. For more information, see the section "Configuration Editor" in the "VistALink Console" section of the *VistALink 1.5 System Management Guide*.

### Update WebLogic Server JVM Arguments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(For first-time installations only. If upgrading adapters, skip this step, or simply verify that the JVM arguments are set.)

The following JVM system properties are used to store environment information that is used in VistALink and made available to other applications through the gov.va.med.environment.Environment API:

- -Dgov.va.med.environment.servertype= (weblogic \| websphere \| jboss \| oracle. Defaults to unknown if not present).

> If you are setting up a WebLogic server, for example, set servertype to "weblogic".

- -Dgov.va.med.environment.production= (true \| false. Defaults to "false" if not present).

> This setting marks a J2EE system as being a "production" or "test" system, and will be used by VistALink in the future to prevent a test J2EE system from connecting to a production M system, and vice versa.

The following JVM property is used for log4j configuration:

> -Dlog4j.configuration= (full path/filename of a log4j configuration file).

For example:

> -Dlog4j.configuration=file:/c:/bea-stage/myLog4JConfig.xml

This log4j JVM argument is required only if your log4j configuration file is both:

- not named "log4j.xml"
- not placed in a folder on the server classpath (e.g., not in the \<HEV CONFIGURATION FOLDER\>).

However, it is recommended that you do name the log4j config file "log4j.xml" and place it in a folder on the server classpath. Then you will not need the log4j JVM argument.

You must set all of these properties listed above when launching any JVMs for WebLogic servers on which VistALink adapters are going to be installed. Depending on your WebLogic domain configuration, the set of servers may include managed servers, admin servers, or both.

#### Single Server (One-Server Domain)

1.  In the startup cmd files generated by the WebLogic configuration wizard, use the JAVA_OPTIONS variable to set these JVM arguments. For example:

> @rem setup the VLJ-specific Java command-line options for running the server

> set JAVA_OPTIONS=-Dgov.va.med.environment.servertype=weblogic

> set JAVA_OPTIONS=%JAVA_OPTIONS% -Dgov.va.med.environment.production=false

#### Managed Server (Multi-Server Domain)

1.  If you launch a given WebLogic server from a command file, modify the command file to pass the JVM argument. If you launch a server from the WebLogic 8.1 console, use the Remote Start tab of the server configuration to specify these arguments. For example:

> -Dgov.va.med.environment.servertype=weblogic

> -Dgov.va.med.environment.production=false

|                                                   |                                                                                                                                                  |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/037.png) | If you have not already performed the KIDS install on the Vista/M server, you cannot establish a connection as described in the following steps. |

### Stop/Restart WebLogic Server(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restart your WebLogic server(s) to activate the new classpath settings in the running JVM(s).

### Deploy Adapter(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(For first-time installations only. If upgrading adapters, your adapters are already deployed, so you can skip this step.)

Follow the steps below to deploy each of your VistALink adapters.

|                                                                                                                |                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/038.png) | The exact prompts may vary on different WebLogic domain configurations, and between different versions of WebLogic server. |

1.  Under your domain in the navigation tree of the WebLogic console, select "Deployments \| Connector Modules."
2.  Select "Deploy a New Connector Module."
3.  Navigate to your \<APPLICATION STAGING FOLDER\>.
4.  A radio button should appear next to your "exploded" adapter staging folder where you copied the exploded RAR files. Select the radio button and choose "Target Module" or "Deploy." If you are asked to target servers, select the server(s) on which you will deploy the adapter.
5.  If prompted for "Source Accessibility," it's recommended to select "Copy this Connector Module onto every target for me."
6.  When you press Deploy, WebLogic should deploy the adapter.  
    Wait for a module status of "Active." When you see this, the adapter successfully deployed (from WebLogic's point of view).  
      
    You should also see under the Connector Modules node a new node for the adapter in the WebLogic console navigation tree.

## Verifying Successful Adapter Installation or Upgrade 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several areas to check to verify that an adapter installation or upgrade is successful:

1.  Select the node for the new adapter in the WebLogic console navigation tree. Then look on the Monitoring tab of the adapter for the number of connections listed. This number should match the Initial Capacity set in the adapter's weblogic-ra.xml.  
    >   
    > If the initial capacity is non-zero, and the number of connections shown matches, WebLogic was able to create connections to the M systems.  
    >   
    > If the numbers do not match (e.g., initial capacity is non-zero but the number of connections is zero), WebLogic may be having difficulty creating connections, most likely due to a configuration or installation issue.
2.  Look for the deployed adapter to be displayed in the VistALink console for all server(s) you deployed it to. Check if the console is able to contact the VistA/M server and return VistALink M/VistA Server Information for the adapter. This is usually a good indicator of a successful deployment. See the section below, ["Deploying the VistALink Console."](#deploying-the-vistalink-console)
3.  (Optional) If your adapter is configured to connect to your M system (as opposed to the Foundations VistA/M server at the Albany OI Field Office), and if your adapter's initial capacity is non-zero, look for XOBVSKT jobs on your VistA/M system.

> For each XOBVSKT job, check that each IO ("IP") variable matches your WLS IP address. (In Caché, use the Caché control panel to choose the Detail view to get this information.)

4.  (Optional) You can exercise the adapter by using it with the VistALink sample J2EE application. See the steps in the below, ["Deploying the J2EE Sample Application."](#_Deploying_the_Sample_J2EE Applicati)

## Deploying the VistALink Console 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink console is an optional tool for managing VistALink adapters. Currently, this console extends the WebLogic console. It is provided in the console folder of the VistALink distribution zip file in two forms:

- A packaged WAR:

> \<DIST FOLDER\>/console/VistaLinkConsole-1.5.0.nnn.war

- An exploded WAR folder:

> \<DIST FOLDER\>/console/exploded/VistaLinkConsole-1.5.0.nnn.war

The VistALink console can be deployed in either packaged or exploded format – we do not recommend one format over the other at this time. The console should be deployed only on admin servers. If you are using a one-server domain, deploy it on your single server.

The figure below shows the flow of steps for deploying the VistALink console:

![](vistalink-version-1-5-installation-guide/039.png)

> <span id="_Toc135124730" class="anchor"></span>Figure 5. Flowchart for VistALink Console Deployment on WLS 8.1

To deploy the VistALink console:

1.  You must completely undeploy any previous version of the VistALink console first.
2.  Copy either the packaged WAR or the exploded WAR folder from \<DIST FOLDER\>/console to your \<APPLICATION STAGING FOLDER\>.
3.  Using the WebLogic console, deploy the packaged or exploded WAR (via \<domain name\> \| Deployments \| Web Application Module node) :
    - Navigate to where you copied the packaged or exploded WAR (e.g.,  
      > \<APPLICATION STAGING FOLDER\>)
    - Select the packaged or exploded WAR file for the VistALink console
    - Target your admin (or single) server.
4.  If successful, the navigation tree on the left-hand side of your WebLogic console should, after a few seconds, display a new node named "VistALink" at the bottom.

> ![](vistalink-version-1-5-installation-guide/040.png)

<span id="_Toc135124731" class="anchor"></span>Figure 6. VistALink Console in the WebLogic Console

### Multi-Server Domains

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For multi-server domains, you may want to put the folder containing the VistALink configuration file on the admin server's classpath – even if adapters are not deployed on the admin server. This makes it easy for the Configuration Editor to edit the admin server's copy of the file. The Configuration Editor can load the VistALink configuration file without prompting, and save it on the admin server. Then you can propagate the changed file out to the other managed servers. 

|                                                                                                                |                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/041.png) | The Configuration Editor is deployed as part of the VistALink console, which runs on the admin server. |

## Deploying the Sample J2EE Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A sample J2EE application is provided to demonstrate the use of VistALink in a J2EE environment. The sample application is also a way to test your basic adapter setup. The figure below shows the flow of steps for deploying the sample application:

![](vistalink-version-1-5-installation-guide/042.png)

> <span id="_Toc135124732" class="anchor"></span>Figure 7. Flowchart for Sample Application Deployment

You can find the sample application as part of the VistALink distribution zip file, in the \<DIST FOLDER\>/samples/J2EE folder. Both packaged and exploded EAR formats are provided.

The sample J2EE application is configured to use the VistALink adapter with the JNDI lookup name of "vlj/testconnector." The vlj/testconnector should be deployed and operational on the same server that the sample J2EE application is installed on. It can be pointed to any VistA/M system. A default configuration is provided that points this connector to the VistALink demo VistA/M server at the Albany OI Field Office.

To deploy the sample J2EE application:

1.  If a previous version of the VistALink sample application is deployed, undeploy it completely.
2.  Copy either the packaged EAR file or the exploded EAR folder for the sample application from the \<DIST FOLDER\>/samples/J2EE folder to the \<APPLICATION STAGING FOLDER\>.
3.  Using the WebLogic console to deploy either the packaged or exploded EAR (via the \<domain name\> \| Deployments \| Applications node):
    1.  Navigate to where you copied the packaged and exploded EAR, e.g., the \<APPLICATION STAGING FOLDER\>
    2.  Select either the packaged or exploded EAR
    3.  If using managed server configuration, select as the target server the server where the vlj/testconnector is deployed

To run the sample J2EE application:

1.  Point your browser to

http://\<yourserver\>:\<yourport\>/VistaLinkSamples

> Example: <http://localhost:7001/VistaLinkSamples>.

2.  If the install is successful, you should reach a page titled "VistALink Sample/Demo J2EE Application."

![](vistalink-version-1-5-installation-guide/043.png)

> <span id="_Toc135124733" class="anchor"></span>Figure 8. VistALink Sample Application

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-5-installation-guide/044.png)</td>
<td><blockquote>
<p>Loading the top page of the application means only that the VistALink sample application has been deployed to the app server. At this point it does not mean that it has used VistALink to connect to an VistA/M system's VistALink listener.</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  Choose a re-authentication method. The choices are VPID, Application Proxy, DUZ and CCOW. At this time, the CCOW option is experimental, so choose one of the other methods.
4.  You are now asked to supply end-user re-authentication identification (DUZ or VPID

> and division) and to specify the connector to use. If your vlj/testconnector connector is pointing at the VistALinkDemo system, you can accept the defaults.

> If this connector is pointing at your own M system, you need to supply the DUZ or VPID of a valid user on your system. This user must hold the \[XOBV VISTALINK TESTER\] "B"-type option.

![](vistalink-version-1-5-installation-guide/045.png)

> <span id="_Toc135124734" class="anchor"></span>Figure 9. Sample Application Re-authentication Page

5.  Press Submit.

> The sample J2EE application will now attempt to execute a set of remote procedure calls (RPCs) on the connector module retrieved from JNDI under the name "vlj/testconnector," using the end-user re-authentication credentials specified.

6.  The results, successful or not, are displayed on a result page:

![](vistalink-version-1-5-installation-guide/046.png)

> <span id="_Toc135124735" class="anchor"></span>Figure 10. VistALink J2EE Sample Application Results Page

## Testing the Sample Application with Your Own VistA/M Server 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If this is a first-time installation, you have so far installed a single VistALink connector on the J2EE system. This connector is configured to use the default VistALink configuration file entry with the "vlj/testconnector" JNDI name. The vlj/testconnector entry is configured by default to access the VistALink demo VistA/M system at the Albany OI Field Office.

If you have a VistA/M system that you are ready to connect to (other than this demo system), you can use the VistALink sample application to point to your own VistA/M system and test the successful operation of both sides of your connector (J2EE and M). This is a four-step process:

1.  Reconfigure the vlj/testconnector adapter to access your own VistA/M listener.
2.  Use an existing user or create new one for the sample application.
3.  Grant the "B"-type option to XOBVTESTER,APPLICATION PROXY.
4.  Run the VistALink sample Web application.

### Reconfigure "vlj/testconnector" Adapter to Access Your Own VistA/M Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To reconfigure the vlj/testconnector adapter to access your own VistA/M listener:

1.  Obtain the following information from your VistA/M system administrator:
- Access code and verify code for the connector proxy user
- IP address of the listener
- Port of the listener
2.  Locate your VistALink configuration file:

> \<HEV CONFIGURATION FOLDER\>\gov.va.med.vistalink.connectorConfig.xml

3.  Under the vlj/testconnector JNDI name, update the access-code, verify-code, ip, and port values to match those of your VistA/M system.
4.  Set the encrypted value to "false."
5.  Using the WebLogic console, either restart your J2EE server or stop and redeploy the connector.

|                                                                                                                |                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-installation-guide/047.png) | You can also use set the VistALink Configuration Editor to make the changes in steps 3 and 4. |

### Create or Use an Existing VistA/M System User for the Sample App 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run the sample Web application (DUZ and VPID re-authentication pages) against your own VistA/M system, you need to either create a Kernel user account or use an existing one. The characteristics required for this user are:

- A known, valid DUZ or VPID identifier for an end-user on your VistA/M system
- An \[XOBV VISTALINK TESTER\] "B"-type option is assigned to the user
- A valid station number under which that user can log into your VistA/M system

> If the user has one or more divisions specified in their NEW PERSON file (#200) "DIVISION" multiple, a valid station number must be the station number for one of these divisions. Otherwise, the valid division for the user is the station number of DEFAULT INSTITUTION, in the KERNEL SYSTEM PARAMETERS file (#8989.3).

Your VistA/M system manager may need to create this user for you and provide you with the identifier and division information. You will be prompted to enter these values when running the sample Web application.

### Grant "B"-Type Option to the Application Proxy User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sample Web application is the Application Proxy re-authentication page. To run it against your own VistA/M system, you need to grant the "B"-type option to the application proxy user (which was added to the NEW PERSON file (#200) as part of the VistALink 1.5 install).

1.  Grant the "B"-type option "XOBV VISTALINK TESTER" to the application proxy user XOBVTESTER,APPLICATION PROXY

### Run the Sample Web App

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use each of the pages (DUZ, VPID, or Application Proxy) for which you have set up a user to run RPCs with the Sample web application. The results page for each will report whether the test, which executes a series of RPCs against your VistA/M system, has been successful or not. The value for All RPCs Executed Successfully will show "true" rather than "false," as shown in the example below:

> Report Generated at Wed Apr 06 16:28:40 PDT 2005.

> Credentials:

| <u>type</u>             | <u>value</u>  |
|-----------------------------|-------------------|
| vpid:                       | null              |
| application proxy name:     | null              |
| duz:                        | 12345             |
| access code:                | null              |
| verify code:                | null              |
| division:                   | 523               |
| CCOW handle:                | null              |
| connector used (JNDI name): | vlj/testconnector |

> All RPCs executed successfully?: true  

> RPC Results:  
> XOBV TEST PING Results:  
> Ping Successful!

### Installing the Java Runtime Environment (JRE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink requires the J2SE Java Runtime Environment (JRE) 1.4.1 (or higher) or the Java Development Kit (JDK) to be installed on the client workstation.

### Installing the J2SE Sample Application Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install the J2SE Sample Application files:

1.  Create a directory, to hold the sample application files, e.g.,

> c:\Program Files\vistalink\samples, for the sample application

2.  Copy the contents of the \samples\J2SE folder in the distribution file to

> c:\Program Files\vistalink\samples

### Copying Java Libraries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink requires certain supporting libraries to be available on the client workstation:

1.  You need either weblogic.jar or j2ee.jar. Do one of the following:
    - Download and install the 1.3.x J2EE SDK (<http://java.sun.com/j2ee/sdk_1.3/>), to get j2ee.jar (then the SDK can be un-installed)
    - If you have access to an installed WebLogic server, you can just use weblogic.jar from the WebLogic server installation directory's lib subdirectory.
2.  Copy the following library files to the same folder you copied the J2SE Sample Application files to:
- j2ee.jar or weblogic.jar – Sources: the directory where J2EE 1.3.x runtime was installed, or weblogic server's \lib folder
- jaxen-dom.jar and jaxen-core.jar – Source: VistALink distribution zip file,  
  \<DIST FOLDER\>\rar\ExplodedVistaLinkRAR\lib folder
- saxpath.jar – Source: VistALink distribution zip file,  
  > \<DIST FOLDER\>\rar\ExplodedVistaLinkRAR\lib folder
- log4j-1.2.8.jar – Source: VistALink distribution zip file,  
  \<DIST FOLDER\>\rar\ExplodedVistaLinkRAR\lib folder

### Copying VistALink Libraries 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Copy the following files from the VistALink distribution jars folder to the same folder you copied the J2SE Sample Application files to (e.g., c:\program files\vistalink\samples):

> • vljConnector-1.5.0.nnn.jar

> • vljFoundationsLib-1.5.0.nnn.jar

> • vljSecurity-1.5.0.nnn.jar

### Granting Yourself Kernel Access to the Sample Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">The Kernel "B"-type option, VistALink Tester \[XOBV VISTALINK TESTER\] was created as part of the M-side KIDS install. To run the sample application, you will need to grant yourself access to the \[XOBV VISTALINK TESTER</span>\] on the VistA/M server to which you will be connecting (unless you already have Kernel programmer access on the M server).

> **NOTE:** For more information on granting yourself access to RPCs, see the *RPC Broker Systems Manual* on the VistA Documentation Library (VDL) at <http://www.va.gov/vdl/>.

### Setting Classpath and Java Locations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three batch files are supplied in the samples folder of the distribution, one for each of the three sample applications:

> • runRpcConsole.bat (runs VistaLinkRpcConsole)

> • runSwingSimple.bat (runs VistaLinkRpcSwingSimple)

> • runSwingTester.bat (runs VistaLinkRpcSwingTester)

In addition, a fourth batch file (setVistaLinkEnvironment.bat) is supplied that sets the classpath and the location of the Java.exe executable to use on your workstation. This fourth batch file is called by each of the other three batch files listed above. So to configure the classpath and Java executable location for your workstation, you need modify only this one file. The content of this file, as distributed, is:

> REM -- you may need to adjust the locations of the various jars and

> REM other files to match the locations of these files on your

> REM system.

> REM

> REM -- set directory with bin subdirectory containing java.exe

> REM -- (don't include the \bin subdirectory)

> set JAVA_HOME=c:\j2sdk1.4.2_08

> REM

> REM -- classpath for J2EE (j2ee.jar or weblogic.jar)

> REM CLASSPATH=./weblogic.jar

> set CLASSPATH=./j2ee.jar

> REM

> REM -- classpath for XML libraries

> set CLASSPATH=%CLASSPATH%;./jaxen-core.jar

> set CLASSPATH=%CLASSPATH%;./jaxen-dom.jar

> set CLASSPATH=%CLASSPATH%;./saxpath.jar

> REM

> REM -- classpath for Log4J

> set CLASSPATH=%CLASSPATH%;./log4j-1.2.8.jar

> REM

> REM -- classpath for VistALink (replace version \#s if different)

> set CLASSPATH=%CLASSPATH%;./vljConnector-1.5.0.nnn.jar

> set CLASSPATH=%CLASSPATH%;./vljFoundationsLib-1.5.0.nnn.jar

> set CLASSPATH=%CLASSPATH%;./vljSecurity-1.5.0.nnn.jar

> REM

> REM -- classpath for sample app (replace version \# if different)

> REM \#) -- (assumes the samples jar is in the current directory)

> set CLASSPATH=%CLASSPATH%;./vljSamples-1.5.0.nnn.jar

### Modifying Sample Application Batch Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Modify the setVistaLinkEnvironment batch file to match the location of the Java executable to use on your workstation. You may have multiple Java Runtime Environments (JREs) or Java Development Kits (JDKs) installed on your workstation. Choose version 1.4.1 or higher.

> In the setVistaLinkEnvironment.bat file, replace the setting for the JAVA_HOME environment variable with the location to use on your system, e.g.:

> REM -- set the directory location containing java.exe executable

> REM -- (don't include the \bin subdirectory)

> set JAVA_HOME=c:\j2sdk1.4.1_02

> If you wish to verify that you have correctly modified the batch file, look in the bin directory of the JAVA_HOME environment variable and use the java –version command to determine what version of the JRE you are running. Use the example below as a guide.

> C:\\CD\j2sdk1.4.1_02\jre\\

> C:\j2sdk1.4.1_02\\jre\>CD BIN

> C:\\j2sdk1.4.1_02\jre\bin\>java -version

> java version "1.4.2"

> Java(TM) 2 Runtime Environment, Standard Edition (build 1.4.2-b28)

> Java HotSpot(TM) Client VM (build 1.4.2-b28, mixed mode)

2.  Modify the setVistaLinkEnvironment batch file to match the locations of the various supporting library jar files needed to run the sample application. You need to specify the locations of each of the J2EE (or weblogic), JAXEN, Log4J, saxpath, and VistALink library jar files.

> Each entry added to the CLASSPATH variable needs to be modified to match the file name and location of the corresponding library on your system, as you installed them above. For example:

> REM clear CLASSPATH and set CLASSPATH for J2EE

> set CLASSPATH=./j2ee.jar

### Running the SwingTester Sample Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of VistALink includes the SwingTester sample application, which is a diagnostic tool for the client workstation. You can use this sample application to verify and test the VistALink client/server connection and sign-on process. Use the following instructions to use this tool.

To run the SwingTester sample application:

1.  Launch the batch file runSwingTester.bat by double-clicking on it, or run it in a command window. This launches the main sample application, designed to demonstrate VistALink functionality and test server connectivity.
2.  In the ip and port fields, enter the IP and port of the M listener you want to connect to, and press Connect. (Alternatively, you could select an entry in a jaas.config settings file to set the IP and port.)
3.  Click Connect on the Access/Verify Code interface.
4.  Enter the Access / Verify code pair you have been assigned. Click OK.

> ![](vistalink-version-1-5-installation-guide/049.png)

<span id="_Toc41200449" class="anchor"></span>

> Figure 12. Test Program Access/Verify Code Entry

5.  If logon is successful, the status changes to "Connected." You can ping the M server, and also execute RPCs using the various tab options in the SwingTester application.
6.  An interface with multiple tabs will display. Click on the RPC List tab. Type "X" in the Enter namespace box. Then click Get RPC List to display the information in the figure below.

> ![](vistalink-version-1-5-installation-guide/050.png)

<span id="_Toc41200450" class="anchor"></span>

> Figure 13. SwingTester RPC List

7.  To disconnect, press Disconnect.

### Running the Other Sample Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to SwingTester, other sample applications are provided. Follow the steps provided in the section on the SwingTester sample application to modify setVistaLinkEnvironment.bat for your JAVA_HOME and for the locations of various libraries.

Unlike the SwingTester sample application, the remaining sample applications require the file jaas.config to be set up with configurations for your M server. (SwingTester allows free-form entry of M server IP and port to connect to.)

To set up jaas.config to hold the configuration for your M server's IP and port:

1.  Modify the jaas.config file in your copied samples files, so that the settings for ServerAddress and ServerPortKey are correct for connecting to your M system.  
      
    Note: runRpcConsole.bat and runSwingSimple.bat are hard-coded to load a configuration named "DemoServer" from the jaas.config file. Either modify the DemoServer configuration with the settings needed for your M system, or, if you add a different configuration and configuration name, modify runRpcConsole.bat and runSwingSimple.bat to use your configuration name. (The -s parameter at the end of the command line that launches the application.)

> With jaas.config and setVistaLinkEnvironment.bat configured, you can then use the batch files described below to launch the other two sample applications.

#### runSwing<u>S</u>imple.bat

> runSwingSimple.bat is a simpler Swing application than SwingTester. It is a better programming example program because it lacks the "bells and whistles" of SwingTester. It passes a command line parameter to specify which configuration in the jaas.config file should be used to connect to.

#### runRpcConsole.bat

> runRpcConsole.bat is a console-only sample application. In addition to requiring a command-line parameter to specify the JAAS configuration to connect to, it is dependent on passing an access and verify code on the command line, unless the defaults embedded in the application work (they probably will not).

> You can pass in access and verify codes with additional "-a" and "-v" command-line parameters.

### Enabling Log4J Logging for Client Sample Applications (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Assume that c:\Program Files\vistalink\samples is the current directory.
2.  Folder c:\Program Files\vistalink\samples\props contains a sample log4jconfig.xml configuration file with various log4j configuration options.
3.  Each sample application will try to load the log4j configuration from the file named "props\log4jconfig.xml," relative to the current directory. Therefore c:\Program Files\vistalink\samples\props\log4jconfig.xml will be loaded.
4.  The log4jconfig.xml file within the c:\Program Files\vistalink\samples\props\\ folder contains extensive information on various log4j configuration options. Look at this simple example of a log4jconfig.xml file:

> \<?xml version="1.0" encoding="UTF-8" ?\>

> \<!DOCTYPE log4j:configuration SYSTEM "log4j.dtd"\>

> \<log4j:configuration xmlns:log4j="http://jakarta.apache.org/log4j/"\>

> \<appender name="myConsoleAppender1" class="org.apache.log4j.ConsoleAppender"\>

> \<layout class="org.apache.log4j.PatternLayout"\>

> \<param name="ConversionPattern" value="%-4r \[%t\] %-5p class %C method %M

> line number %L category %c %x - %m%n"/\>

> \</layout\>

> \</appender\>

> \<root\>

> \<priority value ="info" /\>

> \<appender-ref ref="myConsoleAppender1"/\>

> \</root\>

> \</log4j:configuration\>

5.  When you run the sample application, you should see "logger" output for debug and error information being displayed on the console window (the window in which you are starting up the application).

> **NOTE:** An example log4J properties file is provided in the  
\<DIST FOLDER\>samples\J2SE\props folder in the distribution zip file.

#### Sample Application Loggers

The following table lists all the loggers used by VistALink sample applications and log levels. System administrators may need to use this list when deciding which loggers to activate in the site's log4j configuration file.

> <span id="_Toc135124740" class="anchor"></span>Table 1. VistALink Sample Application Loggers

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 21%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"><strong>Logger Name</strong></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td><p><strong>Environment</strong></p>
<p><strong>(J2EE | J2SE )</strong></p></td>
<td><strong><br />
Package</strong></td>
<td><strong>Class</strong></td>
<td><strong>Log Levels</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Loggers for the sample applications that demonstrate VistALink functionality</td>
<td>J2SE</td>
<td>gov.va.med.vistalink.samples</td>
<td>VistaLinkRpcSwingSimple</td>
<td>Debug<br />
Error</td>
</tr>
<tr class="odd">
<td></td>
<td>J2SE</td>
<td>"</td>
<td>VistaLinkRpcSwingSimpleCcow</td>
<td>Debug<br />
Error</td>
</tr>
<tr class="even">
<td></td>
<td>J2SE</td>
<td>"</td>
<td>VistaLinkRpcConsole</td>
<td>Debug<br />
Error</td>
</tr>
<tr class="odd">
<td></td>
<td>J2SE</td>
<td>"</td>
<td>VistaLinkRpcConsole.Other</td>
<td>Error</td>
</tr>
<tr class="even">
<td></td>
<td>J2SE</td>
<td>"</td>
<td>VistaLinkRpcSwingTester</td>
<td>Debug</td>
</tr>
<tr class="odd">
<td></td>
<td>J2EE</td>
<td>"</td>
<td>VistaLinkJ2EESample</td>
<td>Debug<br />
Error</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### From: VistaLink Version 1.6.7 Installation Guide

## Upgrading a WebLogic 8.1/10.3 Domain w/Existing VistALink Adapters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Back Up Exploded RAR Directories and VistALink Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You should back up (copy) all of your exploded RAR directories, and also the VistALink configuration file. You will need these to recreate your adapters in the WebLogic 10.3.6/12.1.2 domain.

### If Running the Domain Upgrade Wizard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two approaches to moving from a WebLogic 9/10 domain to a WebLogic 10.3.6/12.1.2 domain (and only you can decide which is best):

- Create a new WebLogic 12.2 domain from scratch and redeploy all applications to it that you want carried forward, or
- Run Oracle's domain upgrade wizard to upgrade your WebLogic 9/10 domain to WebLogic 12.2.

If you choose to upgrade your domain by running the upgrade wizard (rather than starting from scratch with a new domain), we recommend you perform the following steps, before shutting down your WebLogic 8.1/10.3 domain and running the wizard.

#### Undeploy RARs

If you have any VistALink adapters deployed, delete them from the WebLogic configuration by navigating to:

> mydomain\>Deployments\>Connector Modules

Then select each adapter, and click on the Delete button.

#### Undeploy VistALink Console

If you have deployed the VistALink Console, delete it from the WebLogic configuration by navigating to:

> mydomain\>Deployments\>Web Application Modules

Then select the VistaLink console web application, and click on the Delete button.

#### Undeploy Sample Application

If you have deployed the VistALink sample web application, delete it from the WebLogic configuration by navigating to:

> mydomain\>Deployments\>Applications

Then select the VistALink sample web application, and click on the Delete button.

## ## WebLogic 10.3.6/12.2: Install the Standalone Console EAR (Admin Server)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For WebLogic 10.3.6/12.2 we recommend installing the standalone VistALink console EAR application, rather than the console plug-in, due to difficulties integrating with the WebLogic console navigation tree and tab set.

The VistALink console is helpful to monitor and troubleshoot VistALink adapters. As such it is useful to install it prior to installing any VistALink adapters.

### Copy Console EAR file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Copy the console EAR file from the \<DIST FOLDER\>/app-j2ee/console-ext folder to a staging folder on your admin server:

- VistaLinkConsole-1.6.7.xxx.ear

### Deploy Console EAR 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Target the deployment to the domain admin server only.
2.  Finish the deployment, and activate changes. In the main "Deployments" listing, the state of the VistaLinkConsole application should be *New* or *Prepared* (depending on whether targeted servers are running or not).
3.  Start the application (in the Deployment list, choose Start \| Servicing all requests for the VistaLinkConsole application). The state of the application should now be *Active*.

### Access Standalone VistALink Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If successfully deployed, the standalone VistALink console will be reachable at the following URL:

- http://\<adminserver\>:\<port\>/vlconsole

You'll be prompted for a user name and password. Use the same credentials as you would use to login to the WebLogic administration console. From that point on, the standalone VistALink console application will look almost identical to the console extension plug-in version.

Click on the link to open the VistALink console plug-in main page. You should see a page like the following:

![](vistalink-version-1-6-7-installation-guide/011.png)

<span id="_Toc97638169" class="anchor"></span>Figure 3‑2. Standalone VistALink 1.6 Console

### Check Configuration Editor Access to Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the main page of the VistALink console, click the "Configuration File Editor" link:

- If the server classpath on the admin server file system is set up correctly, you should be presented with a list of entries from the copy of the VistALink configuration file on your admin server's file system.
- Otherwise, if there is a problem, you will see an error message, for example, "Error while retrieving configuration file: 'Missing configuration file path.'.". If you see this or similar error message, check:
  - Is the configuration file present on the host file system of the admin server?
  - Is the configuration file named "gov.va.med.vistalink.connectorConfig.xml"?
  - Is the folder containing the configuration file on the classpath specified in the setDomainEnv or startWebLogic script of the admin server?
