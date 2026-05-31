---
title: NUMI Server Setup Guide Version 15.10
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: anchor
doc_subject: null
app_code: NUMI
app_name: National Utilization Management Integration
section: GUI
app_status: archive
pkg_ns: NUMI
patch_ver: 15.1
patch_id: NUMI*15.10
group_key: NUMI:NUMI:15.10
file_numbers:
- '3'
security_keys: []
menu_options: 0
description: 08/04/2011 Refined CERME instructions in section 6 per AITC Windows SA
audience: ''
keywords: []
page_count: 0
word_count: 9781
section_count: 42
table_count: 8
figure_count: 0
appendix_count: 1
has_toc: false
is_stub: false
pub_date: null
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/National_Utilization_Management_Integration_Archive/numi_server_setup_guide_15_10.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/National_Utilization_Management_Integration_Archive/numi_server_setup_guide_15_10.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=285
audit_applied: '2026-05-31'
master_source: NUMI Server Setup Guide Version 15.10
master_pub_date: 'null'
consolidated_from: 5 versions
prior_versions:
- NUMI Server Setup Guide Version 15.09
- NUMI Server Setup Guide Version 15.14
- NUMI Server Setup Guide Version 15.15
- NUMI Server Setup Guide
consolidated_title: numi server setup guide
---

> National Utilization Management Integration (NUMI)

> Server Setup Guide

> Release 1.1.15.10

![](numi-server-setup-guide-version-15-10/001.png)

Department of Veterans AffairsJuly 2022

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 59%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>04/22/2009</td>
<td>Submitted to Medora Team for</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/14/2009</td>
<td>Updated to reflect "Release 1.1"</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/28/2009</td>
<td>Updated document name to</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/01/2011</td>
<td>Updated per issues found in AITC</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/02/2011</td>
<td>Updated section 9.9 per AITC</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/04/2011</td>
<td>Refined CERME instructions in section 6 per AITC Windows SA</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/24/2011</td>
<td>Refined MDWS instructions in section 6.12-6.15 per AITC</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/13/2011</td>
<td>Updated CERME instructions in</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/10/2012</td>
<td>Draft preliminary update for</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/03/2012</td>
<td><p>Added figures to section 6.13;</p>
<p>Added captions to figures throughout; replaced example in section 6.12, step #10; added new section 6.14; updated cover and footers to "Release 14" per VA PM</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/03/2013</td>
<td><p>Added section 6.12; updated</p>
<p>section 6.13 with new Fig. 19, corrected Section 6.14, Windows Event Log and updated SSL setup and config; updated 6.19 per Operational feedback; added Appendix F NUMI Exchange</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/25/2013</td>
<td>Modified section 6.15 for NUMI event folder, modified section 6.19</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3/29/2013</td>
<td><p>Removed original highlighting and</p>
<p>updated per customer feedback: changed Section 2.2 Web Server (Server 2) to reference NUMI Exchange and MDWS; updated</p>
<p>Section 3.1 Disk Space and Devices; updated Section 5.1 to reference test environments and removed Section 5.6, Installation During Off Peak Hours. Also reordered installation steps SQL and CERMe (now section</p>
<p>6.1 and 6.14) and added CERMe SSL</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/13/2013</td>
<td><p>Corrected release referenced in</p>
<p>section 1, removed content for Windows Server 2003 and IIS 6 setup, added content for Windows Server 2008 and IIS 7 setup, added content for MDWS 2.Xinstallation, re-organized document content.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/24/2013</td>
<td><p>Made the following corrections</p>
<p>per VA comments: Changed section</p>
<p>2.2.1 to specify SQL Server 2005, changed figures 37,</p>
<p>38, 39 to reflect MDWS1.2, added MDWS config information to section 6.11.3 (MDWS1.2) and</p>
<p>6.12.4 (MDWS2.x), added execution timeout setting for the synchronizer in section 6.18.1, step 4.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/17/2013</td>
<td><p>Made the following corrections per VA comments: Changed section 2.2.1 to clarify restoring from a NUMI backup database and added replication comments, updated 3.1.3 with CPU capacity details, updated section 3.1.4 with disk space details;</p>
<p>changed section 5 to clarify restoring from a NUMI backup database, updated section 5.1 added synchronizer and user account information, removed original item 3, updated section 6.7 to specify version and recovery mode, updated section 6.8 removed Medora information, updated section 6.19 to add more script information.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/27/2013</td>
<td>Updated to version number to 14.1 changed sections 2.2.1 and 5. To include 14.0 and 14.1 database information.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/2/2013</td>
<td>Changed example directory references to remove 14.0</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>8/2/2013</td>
<td><p>Removed references to CERMe 2012. Changed hard coded build name directory references to</p>
<p>&lt;install_dir&gt;.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>8/20/2013</td>
<td><p>Added version number for MDWS in section 2.2.2, added version number for CERME in section 2.2.3, added RAM to section 3.1.3, updated Figure 68, removed MDWS 1.2 section 6.11, renamed MDWS 2.x to MDWS 2.7.3.2 in section 6.12,</p>
<p>renamed section 6.12 to 6.11</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/11/2015</td>
<td>Updated the version number from 14.1 to 14.2</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/12/2015</td>
<td>Updated the version number from 14.2 to 14.3</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/12/2016</td>
<td>Updating document for NUMI 14.4 and .NET version. Made the Windows version generic</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/20/2016</td>
<td>Updated install instructions for 15.0 and updated CERMe installation instructions and IIS and File service installation screenshots</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2/3/2017</td>
<td>Added steps to encrypt the configuration files</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/1/2017</td>
<td>Updates for IAM SSO integration changes</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3/27/2017</td>
<td>Added CA WebAgent setup instructions</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/25/2017</td>
<td>Reviewed document and revised</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/14/2017</td>
<td>Updated release version number (version 15.4) and CERME upgrade installation steps</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/23/2018</td>
<td>Update release version number (15.5)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/1/2018</td>
<td>Updated release version number (15.6)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>02/19/2018</td>
<td>Updated release version number (15.7) and new Synchronizer installation instructions.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/28/2019</td>
<td>Updated release version number and added STS integration information (Section 13).</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/1/2020</td>
<td>Updated release version number (15.9)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/28/2020</td>
<td>Updated CERMe RM and InterQual View version (19.0/2020)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/03/2020</td>
<td><p>Updated release version number (15.9.1) in footer and title.</p>
<p>Month and year updated both in title and footer.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>8/16/2021</td>
<td>Updated CERMe RM 20.0 and InterQual View version 2021</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/15/2021</td>
<td>Updated release version number to 15.10</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/7/2022</td>
<td>Updated CERMe RM 21.0.1 and InterQual View version 2022</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [Target Audience](#target-audience)
- [Deployment Overview](#deployment-overview)
  - [National Deployment Request](#national-deployment-request)
  - [Installing NUMI on the Servers](#installing-numi-on-the-servers)
    - [Database Server](#database-server)
    - [Web Server](#web-server)
    - [Application Server](#application-server)
- [Pre-Installation Instructions and Preparation](#pre-installation-instructions-and-preparation)
  - [Installation Process Requirements](#installation-process-requirements)
    - [Minimum Software Version](#minimum-software-version)
    - [Resources Required](#resources-required)
    - [CPU Capacity](#cpu-capacity)
    - [Disk Space](#disk-space)
    - [Devices (Servers, etc.)](#devices-servers-etc)
    - [VistA Rights Needed for NUMI Users](#vista-rights-needed-for-numi-users)
  - [Install Software in Test Environments](#install-software-in-test-environments)
  - [Generate Pre-Installation Reports](#generate-pre-installation-reports)
  - [Coordinate Installation with Other Teams](#coordinate-installation-with-other-teams)
  - [Install Sequence Information for Multiple Patches](#install-sequence-information-for-multiple-patches)
  - [Logoff During Installation](#logoff-during-installation)
  - [Average Amount of Time Required to Complete the Installation](#average-amount-of-time-required-to-complete-the-installation)
- [Database Information](#database-information)
  - [Instructions for Installing Database Components](#instructions-for-installing-database-components)
    - [Database Installation / Restoration Procedures](#database-installation-restoration-procedures)
- [Installation Procedure for Server 2019](#installation-procedure-for-server-2019)
  - [Patch the Operating System](#patch-the-operating-system)
- [SQL Server Setup (Windows Server 2019)](#sql-server-setup-windows-server-2019)
  - [Role Setup](#role-setup)
- [Web Server Setup (Windows Server 2019)](#web-server-setup-windows-server-2019)
  - [Role Setup](#role-setup-1)
  - [ASP.NET 2.0 AJAX Extensions 1.0 Setup](#aspnet-20-ajax-extensions-10-setup)
  - [MS Web Services Enhancements (WSE) 3.0 Setup](#ms-web-services-enhancements-wse-30-setup)
- [Application Server Setup (Windows Server 2019)](#application-server-setup-windows-server-2019)
  - [Role Setup](#role-setup-2)
  - [Feature Delegation](#feature-delegation)
  - [Install MS ASP.Net 2.0 AJAX Extensions 1.0](#install-ms-aspnet-20-ajax-extensions-10)
  - [Install MS Web Services Enhancements 3.0](#install-ms-web-services-enhancements-30)
- [Install SQL Server](#install-sql-server)
  - [Download all SQL Server Patches](#download-all-sql-server-patches)
  - [Restore the Appropriate Databases for the NUMI Application](#restore-the-appropriate-databases-for-the-numi-application)
- [Installing NUMI Exchange on Server 2019](#installing-numi-exchange-on-server-2019)
  - [Unzip/Install NUMI Exchange Distribution](#unzipinstall-numi-exchange-distribution)
  - [NUMI Exchange Website Configuration](#numi-exchange-website-configuration)
    - [Application Pool Configuration](#application-pool-configuration)
- [Installing NUMI on Server 2019](#installing-numi-on-server-2019)
  - [Software Copy Instructions](#software-copy-instructions)
  - [NUMI Web Site Configuration](#numi-web-site-configuration)
  - [Application Pool Configuration](#application-pool-configuration-1)
- [Install CA SiteMinder Web Agent for Single Sign On (SSO) on the Web server](#install-ca-siteminder-web-agent-for-single-sign-on-sso-on-the-web-server)
  - [Agent location](#agent-location)
  - [Agent installation](#agent-installation)
  - [Agent configuration](#agent-configuration)
    - [Configuring for the first time](#configuring-for-the-first-time)
    - [Reconfiguration configuration](#reconfiguration-configuration)
- [Secure Token Service Integration for SSOi](#secure-token-service-integration-for-ssoi)
  - [Download Certificate Chain from appropriate endpoint](#download-certificate-chain-from-appropriate-endpoint)
  - [Export server cert to .pfx](#export-server-cert-to-pfx)
- [Find the server cert in the personal folder](#find-the-server-cert-in-the-personal-folder)
- [Right click and export the certificate](#right-click-and-export-the-certificate)
- [Select "Yes, export private key" and choose next](#select-yes-export-private-key-and-choose-next)
- [Select "Export all extended properties" and choose next](#select-export-all-extended-properties-and-choose-next)
- [Select a strong password. This password will go into NumiWebApp.config later in this guide.](#select-a-strong-password-this-password-will-go-into-numiwebappconfig-later-in-this-guide)
- [Select a filename for the exported certificate and save it as a .pfx. Select a folder not specific to a version of NUMI as this cert will be valid for future versions of the applications until expiration. For example, if the folder structure for website is NUMI/NUMI15.9 select the /NUMI folder for the cert and not the specific /NUMI15.9 folder. This file path will go into NumiWebApp.config later in this guide.](#select-a-filename-for-the-exported-certificate-and-save-it-as-a-pfx-select-a-folder-not-specific-to-a-version-of-numi-as-this-cert-will-be-valid-for-future-versions-of-the-applications-until-expiration-for-example-if-the-folder-structure-for-website-is-numinumi159-select-the-numi-folder-for-the-cert-and-not-the-specific-numi159-folder-this-file-path-will-go-into-numiwebappconfig-later-in-this-guide)
  - [NumiWebApp.config keys](#numiwebappconfig-keys)
  - [Install CERMe SSL Certificate](#install-cerme-ssl-certificate)
- [Setting up NUMI Section in the Windows Event Log](#setting-up-numi-section-in-the-windows-event-log)
  - [Validate XML Configuration File Settings](#validate-xml-configuration-file-settings)
- [Test NUMI Web Site Functionality](#test-numi-web-site-functionality)
- [Installing NUMI Synchronizer on the DB Server](#installing-numi-synchronizer-on-the-db-server)
  - [Installation Instructions](#installation-instructions)
  - [Uninstall:](#uninstall)
  - [Validate Installation:](#validate-installation)
  - [Add Jobs to the SQL Server](#add-jobs-to-the-sql-server)
- [Post-Installation Considerations](#post-installation-considerations)
- [Acronyms and Descriptions](#acronyms-and-descriptions)
- [NUMI Comparison Table](#numi-comparison-table)
This Server Setup Guide explains how to install National Utilization Management Integration (NUMI), Release 1.1.15.10.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to explain the hardware and software requirements and tasks that must be performed before and after the installation process.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of this document includes explanations of the appropriate steps to install the NUMI software, and the steps that are needed to be completed before and after the installation process is started.

## Target Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is intended for the Information Technology Team and the individuals who install software in your organization.

# Deployment Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following process is followed to request permission to do a National Deployment.

## National Deployment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ProPath Release Management processes govern the request for a National Deployment. Refer to ProPath for guidance on requesting a release. This process must be complete before installation of services on the NUMI servers.

## Installing NUMI on the Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps to install NUMI on the servers are described below. The middle tier of NUMI is the Veterans Information Systems Technology Architecture (VistA) Integration Adapter (VIA), which is a hosted service and is not part of the NUMI deployment. The primary NUMI application servers are located at the Austin Information Technology Center (AITC) facility in Austin, Texas. The application servers run on an Internet Information Services (IIS) Application Server. The NUMI application requires Microsoft (MS) ASP.NET 2.0 Ajax Extensions 1.0 and Web Services Enhancements 3.0 to enable the interactions with the Web Services.

### Database Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI database as it exists now is a manifestation of multiple changes over multiple releases. This installation document has as a pre-requisite the backup of an existing NUMI database. Therefore, to install a new NUMI database, it is necessary to restore a backup of an existing NUMI database.

Database Platform installation, and Database Restoration Procedures

1.  Install Windows Server 2019 on the database server platform
2.  Download and install any critical patches for the Operating System
3.  Install the 64-bit MS Structured Query Language (SQL) Server 2019 application according to local "best practices"
    1.  MS's Full Text Search is required for the NUMI installation
    2.  Replication is necessary for the NUMI installation to use the alternate database reporting capability of NUMI
    3.  Reporting Services is not necessary for installation on the NUMI database server
    4.  NUMI's database will function properly in cluster, but clustering is not required for the NUMI application
4.  Apply all appropriate patches (according to local best practices) to MS SQL Server 2019
5.  Install / restore the database components according to the instructions in section 4.1 Instructions for Installing Database Components.

### Web Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install NUMI Exchange software on the Web Server (Server 2):

1.  Install Windows Server 2019 on the web server platform
6.  Download and install any critical patches for the Operating System on all web servers
7.  Install MS ASP.NET 2.0 Ajax Extensions 1.0
8.  Install Web Services Enhancements 3.0
9.  Install NUMI Exchange
10. Change the web.config file settings as needed

### Application Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install NUMI application software on the Application Server (Server 3)

1.  Install Windows Server 2019 on the application server platform
11. Download and install any critical patches for the Operating System on all application servers
12. Install the Care Enhance Review Management Enterprise (CERMe) 21.0.1 InterQual View 2022 application
13. Install the NUMI application
14. Change the web.config file settings as needed
15. Install the SiteMinder Web Agent and configure it for the NUMI application Web site

# Pre-Installation Instructions and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pre-Installation Instructions and Preparation section explains the tasks that need to be performed before installing NUMI software. Before proceeding with the installation procedures, consult the list of requirements below.

## Installation Process Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An assumption is made that the person responsible for doing installations at your site has performed appropriate pre-installation planning.

### Minimum Software Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Operating System: Windows Server 2019

Database: SQL Server 2019

### Resources Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sys Admin, DBA

### CPU Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

64GB RAM, Dual 2.20 GHz Intel Xeon®E5-2698 v4 – Database Server

12GB RAM, Dual 2.20 GHz Intel Xeon®E5-2698 v4 – Application Server

12GB RAM, Dual 2.20 GHz Intel Xeon®E5-2698 v4 – Web Server

### Disk Space

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application server – 100 GB Web Services server – 100 GB

Database – E:900 GB, F:700 GB, L:200 GB, O:400 GB (This includes space needed for the backups and data storage.)

### Devices (Servers, etc.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1 Database Server

> 2 Application Servers

> 2 Web Servers

> 1 Data Warehouse Server 1 SQL Reporting Server

### VistA Rights Needed for NUMI Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each NUMI user must have Computerized Patient Record System (CPRS) access in their VistA menu structure, such as in their secondary menu tree. The VistA menu name is CPRSChart (or CPRS Graphical User Interface CHART). Table 1 and Table 2 identify the menus, options and settings these user accounts will need to have assigned.

It is also highly recommended that the VIAB WEB SERVICES OPTION be added to the System Command Options \[XUCOMMAND\] menu in each site's VistA system. If you do not add this to the Common Menu, you will need to add it to the secondary menu of each individual NUMI user.

<span id="_bookmark18" class="anchor"></span>­Table 1: CPRS Rights

| CPRS Rights                                 |
|---------------------------------------------|
| Primary Menu: XMUSER                        |
| Primary Menu: MailMan Menu                  |
| Secondary Menu: \[OR CPRS GUI CHART\]       |
| Secondary Menu: CPRSChart Release 1.0.30.72 |
| Keys Held                                   |
| Patient Selection                           |
| Restrict? NO                                |
| OE/RR List                                  |

<span id="_bookmark19" class="anchor"></span>Table 2: CPRS Access Tabs

| Name | Description | Effective Date | Expiration Date |
|------|-------------|----------------|-----------------|
| RPT  | Reports tab | Sept. 2, 2008  | N/A             |

## Install Software in Test Environments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software will be installed in the Test environments before installing in Production.

## Generate Pre-Installation Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Coordinate Installation with Other Teams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Installation Team will need to involve the Implementation/Architecture Team.

## Install Sequence Information for Multiple Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Logoff During Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

End users do not need to be logged off during installation (during the act of copying files and installation executions to the server(s)). However, the users must be logged off for any updates to the software (running the executions and/or configuring the software and configuration files).

Logging off during software updates is no different from any other logoff that a user may do.

## Average Amount of Time Required to Complete the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The average amount of time required to complete the NUMI installation is 2 days.

# Database Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the NUMI Systems Management Guide for information about the structure and components of the NUMI database.

## Instructions for Installing Database Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI database as it exists now is a manifestation of multiple changes over multiple releases. This installation document has as a pre-requisite the backup of an existing NUMI database. Therefore, to install a new NUMI database, it is necessary to restore a backup of an existing NUMI database.

### Database Installation / Restoration Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Copy a backup of an existing NUMI database(s) of appropriate size and content to the new NUMI database server
    1.  The application database (typically called NUMI) is necessary for proper function of the application
    2.  The "auditing" database (typically called LogSyncDb) is necessary for proper functioning of the application and the synchronizer
    3.  The CERMe database can be restored from an existing backup, or can be built from scratch from the CERMe installation media
        1.  If the CERMe database is restored from an existing backup, verify that the application configuration files reference a database authenticated user that has DBO privilege on the CERMe database for proper functioning of the NUMI application
        2.  If the CERMe database is installed from media, follow the instructions provided by Change Healthcare for installation
16. Restore the database backup to the existing server
    1.  File paths will have to be altered according to local best practices
    2.  User accounts may be, but are not required to be, restored with the database. NUMI requires the numi_user account to be setup.
    3.  Database ownership may be altered so that the owning account for the NUMIdatabase complies with local best practices
    4.  A database authenticated user for the application should be configured, and granted DBO privileges on the NUMI database
17. Run the Install_XX.sql if it was provided with the build, where XX is the database version for the NUMI build. This will apply changes to the database necessary for the version of NUMI that is being installed
18. Install the NUMI Synchronizer according to the instructions in section 17 Installing NUMI Synchronizer on the DB Server

# Installation Procedure for Server 2019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section identifies the installation procedures that shall be followed.

## Patch the Operating System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This applies to all servers.

1.  Open up an instance of Internet Explorer.
19. Select menu item \<Tools/Windows Update\>.
20. Follow the instructions on MS's website. (NOTE: A restart of the servers may be necessary).

# SQL Server Setup (Windows Server 2019)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Role Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The role set-up in this section applies to the SQL database server. Use Server Manager to install the File Services with the role services shown in Figure 1: SQL Server Role Services.

![](numi-server-setup-guide-version-15-10/002.png)

<span id="_bookmark33" class="anchor"></span>Figure 1: SQL Server Role Services

# Web Server Setup (Windows Server 2019)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Role Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The role setup in this section applies to the NUMI Exchange web server.

Use Server Manager to install the File Services and Web Server (IIS) roles with the role services shown in Figure 2: NUMI Exchange Role Services and Figure 3: NUMI Exchange (IIS).

![](numi-server-setup-guide-version-15-10/003.png)

<span id="_bookmark36" class="anchor"></span>Figure 2: NUMI Exchange Role Services

![](numi-server-setup-guide-version-15-10/004.png)

<span id="_bookmark37" class="anchor"></span>Figure 3: NUMI Exchange (IIS)

## ASP.NET 2.0 AJAX Extensions 1.0 Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install the ASP.NET 2.0 Ajax Extensions 1.0 as detailed in section 8.3, Install MS ASP.NET 2.0 Ajax Extensions 1.0.

## MS Web Services Enhancements (WSE) 3.0 Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install MS WSE 3.0 as detailed in section 8.4 Install MS Web Services Enhancements 3.0.

# Application Server Setup (Windows Server 2019)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Role Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The role setup in this section applies to the NUMI app servers. Use Server Manager to install the File Services and Web Server (IIS) roles with the role services shown in Figure 4: NUMI Role Services and Figure 5: NUMI Web Services IIS.

![](numi-server-setup-guide-version-15-10/005.png)

<span id="_bookmark42" class="anchor"></span>Figure 4: NUMI Role Services

![](numi-server-setup-guide-version-15-10/006.png)

<span id="_bookmark43" class="anchor"></span>Figure 5: NUMI Web Services IIS

## Feature Delegation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select the main node in IIS, with the server name. Then double click on "Feature Delegation" item. Change the "Feature Delegation" settings for the server, as shown in Figure 6: IIS Feature Delegation.

![](numi-server-setup-guide-version-15-10/007.png)

<span id="_bookmark45" class="anchor"></span>Figure 6: IIS Feature Delegation

Make sure all authentication rules are set to Read/Write as shown in Figure 7: Feature Delegation Selection.

![](numi-server-setup-guide-version-15-10/008.png)

<span id="_bookmark46" class="anchor"></span>Figure 7: Feature Delegation Selection

## Install MS ASP.Net 2.0 AJAX Extensions 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installing MS ASP.NET 2.0 Ajax Extensions 1.0 applies to the web servers only.

1.  Download the MS ASP.NET 2.0 Ajax Extensions 1.0 from MS's website.
21. Run the ASPAJAXExtSetup.msi by double-clicking it.
22. When the File Download – Security Warning window displays, click the \<Run\> button (shown in Figure 8: MS ASP.Net 2.0 File Download-Security Warning Window).
23. 

![](numi-server-setup-guide-version-15-10/009.png)

<span id="_bookmark48" class="anchor"></span>Figure 8: MS ASP.Net 2.0 File Download-Security Warning Window

24. When the Internet Explorer – Security Warning window displays, click the \<Run\> button (shown in Figure 9: MS ASP.Net 2.0 Internet Explorer-Security Warning Window).

![](numi-server-setup-guide-version-15-10/010.png)

<span id="_bookmark49" class="anchor"></span>Figure 9: MS ASP.Net 2.0 Internet Explorer-Security Warning Window

25. When the MS ASP.NET 2.0 AJAX Extensions 1.0 Setup window displays, click the \<Next\> button (shown in Figure 10: MS ASP.NET 2.0 AJAX Extensions 1.0 Setup Wizard Window).

![](numi-server-setup-guide-version-15-10/011.png)

<span id="_bookmark50" class="anchor"></span>Figure 10: MS ASP.NET 2.0 AJAX Extensions 1.0 Setup Wizard Window

Click the "I accept the terms in the License Agreement" checkbox, as illustrated in Figure 11: MS ASP.NET 2.0 AJAX License Agreement Window.

1.  Click the \<Next\> button.

![](numi-server-setup-guide-version-15-10/012.png)

<span id="_bookmark51" class="anchor"></span>Figure 11: MS ASP.NET 2.0 AJAX License Agreement Window

26. Click the \<Install\> button (shown in Figure 12: MS ASP.NET 2.0 AJAX Installation Window).

![](numi-server-setup-guide-version-15-10/013.png)

<span id="_bookmark52" class="anchor"></span>Figure 12: MS ASP.NET 2.0 AJAX Installation Window

27. The installation is complete. Select the \<Finish\> button by clicking on it to exit the installation wizard, as depicted in Figure 13: MS ASP.NET 2.0 AJAX Completion window.

![](numi-server-setup-guide-version-15-10/014.png) If you do not wish to view the release notes, un-check the "Display MS ASP.NET 2.0 AJAX Extensions 1.0 Release Notes" checkbox.

![](numi-server-setup-guide-version-15-10/015.png)

<span id="_bookmark53" class="anchor"></span>Figure 13: MS ASP.NET 2.0 AJAX Completion window

## Install MS Web Services Enhancements 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installing MS Web Services Enhancements 3.0 applies to the web servers only.

1.  Download the MS Web Services Enhancements 3.0 from MS's website.
28. Run the MS WSE 3.0.msi by double-clicking it.
29. When the File Download – Security Warning window displays, click the \<Run\> button (shown in Figure 14: MS WSE 3.0 File Download-Security Warning Window).

![](numi-server-setup-guide-version-15-10/016.png)

<span id="_bookmark55" class="anchor"></span>Figure 14: MS WSE 3.0 File Download-Security Warning Window

2.  When the Internet Explorer – Security Warning window displays, click the \<Run\> button (shown in Figure 15: MS WSE 3.0 Internet Explorer-Security Warning Window).

![](numi-server-setup-guide-version-15-10/017.png)

<span id="_bookmark56" class="anchor"></span>Figure 15: MS WSE 3.0 Internet Explorer-Security Warning Window

3.  When the MS WSE 3.0 – InstallShield Wizard window displays, click the \<Next\> button (shown in Figure 16: MS WSE 3.0 InstallShield Wizard Welcome Window).

![](numi-server-setup-guide-version-15-10/018.png)

<span id="_bookmark57" class="anchor"></span>Figure 16: MS WSE 3.0 InstallShield Wizard Welcome Window

4.  Click the "I accept the terms in the license agreement" checkbox, as illustrated in Figure 17: MS WSE 3.0 License Agreement Window.
30. Click the \<Next\> button.

![](numi-server-setup-guide-version-15-10/019.png)

<span id="_bookmark58" class="anchor"></span>Figure 17: MS WSE 3.0 License Agreement Window

5.  Click the \<Administrator\> radio button, as illustrated in Figure 18: MS WSE 3.0 InstallShield Wizard Window.
31. Click the \<Next\> button.

![](numi-server-setup-guide-version-15-10/020.png)

<span id="_bookmark59" class="anchor"></span>Figure 18: MS WSE 3.0 InstallShield Wizard Window

6.  Click the \<Install\> button (shown in Figure 19: MS WSE 3.0 Installation Window).

![](numi-server-setup-guide-version-15-10/021.png)

<span id="_bookmark60" class="anchor"></span>Figure 19: MS WSE 3.0 Installation Window

7.  Click the \<Finish\> button (shown in Figure 20: MS WSE 3.0 Completion Window).

![](numi-server-setup-guide-version-15-10/022.png)

<span id="_bookmark61" class="anchor"></span>Figure 20: MS WSE 3.0 Completion Window

# Install SQL Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install the MS SQL Server 2019 Database Server software only on the database server, applying both MS installation instructions and local best practices.

Additional service packs or patches may be installed subsequent to application testing, and in accordance with local best practices.

All production NUMI databases should be run in Simple Recovery mode, to enable replication to function, and to maximize the recoverability of the databases. In non-production environments, any recovery mode is acceptable, and simple recovery mode is encouraged for development and QA testing environments due to ease of administration.

## Download all SQL Server Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Downloading all SQL Server Patches applies to the database server only.

## Restore the Appropriate Databases for the NUMI Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restoring the Appropriate Databases for the NUMI Application applies to the database server only.

Follow the instructions in section 4 Instructions for Installing Database Components.

# Installing NUMI Exchange on Server 2019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](numi-server-setup-guide-version-15-10/023.png) Before doing this, you must make a backup copy of the web.config file (if this is an upgrade). Settings may need to be extracted from this in the future.

## Unzip/Install NUMI Exchange Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Using Windows Explorer, create the NumiExchange folder on the D drive, if available; otherwise create on the C drive. E.g., D:\NumiExchange
32. Unzip the NUMI Exchange files into the NumiExchange folder created above.
33. Update the application settings in the NUMI Exchange web.config file, located in the directory created above. Typically, this would involve updating the database connection string.

## NUMI Exchange Website Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using IIS Manager, add a new website and select the Secure Socket Layer (SSL) certificate as shown in Figure 21: Add NUMI Exchange Website.

![](numi-server-setup-guide-version-15-10/024.png)

<span id="_bookmark68" class="anchor"></span>Figure 21: Add NUMI Exchange Website

![](numi-server-setup-guide-version-15-10/025.png)

<span id="_bookmark69" class="anchor"></span>Figure 22: NUMI Exchange Website

The NUMI website basic and advanced settings are shown in Figure 23: NUMI Exchange Basic Settings and Figure 24: NUMI Advanced Settings.

![](numi-server-setup-guide-version-15-10/026.png)

<span id="_bookmark70" class="anchor"></span>Figure 23: NUMI Exchange Basic Settings

![](numi-server-setup-guide-version-15-10/027.png)

<span id="_bookmark71" class="anchor"></span>Figure 24: NUMI Advanced Settings

The NUMI Exchange web site bindings are shown in Figure 25: NUMI Exchange Bindings.

![](numi-server-setup-guide-version-15-10/028.png)

<span id="_bookmark72" class="anchor"></span>Figure 25: NUMI Exchange Bindings

The NUMI Exchange web site authentication settings are shown in Figure 26: NUMI Exchange Authentication Settings.

![](numi-server-setup-guide-version-15-10/029.png)

<span id="_bookmark73" class="anchor"></span>Figure 26: NUMI Exchange Authentication Settings

The NUMI Exchange website SSL settings are shown in Figure 27: NUMI Exchange SSL Settings.

![](numi-server-setup-guide-version-15-10/030.png)

<span id="_bookmark74" class="anchor"></span>Figure 27: NUMI Exchange SSL Settings

### Application Pool Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI Exchange application pool setup is shown in Figure 28: Application Pool Window.

![](numi-server-setup-guide-version-15-10/031.png)

<span id="_bookmark76" class="anchor"></span>Figure 28: Application Pool Window

The NUMI Exchange application pool basic settings are shown in Figure 29: NUMI Exchange Application Pool Basic Settings.

![](numi-server-setup-guide-version-15-10/032.png)

<span id="_bookmark77" class="anchor"></span>Figure 29: NUMI Exchange Application Pool Basic Settings

The NUMI Exchange application pool advanced settings are shown in Figure 30: NUMI Exchange Pool Advanced Settings.

![](numi-server-setup-guide-version-15-10/033.png)

![](numi-server-setup-guide-version-15-10/034.png)

![](numi-server-setup-guide-version-15-10/035.png)

<span id="_bookmark78" class="anchor"></span>Figure 30: NUMI Exchange Pool Advanced Settings

# Installing NUMI on Server 2019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Software Copy Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Right click on the zip file, select the "Unblock" if active, and select O.K. Some security schemes will block certain files from being unpacked, typically the Java files under the "web" directory. Setting the file to Unblock eliminates this problem.

![](numi-server-setup-guide-version-15-10/036.png)

<span id="_bookmark99" class="anchor"></span>Figure 31: Unblocking Restricted Files in Installation ZIP File

It is recommended that NUMI be installed in the D:\NUMI folder. Using Windows Explorer, create a NUMI folder in D drive, if available, otherwise create in C drive. E.g., D:\NUMI.

Unzip the NumiWebApp folder from the NUMI distribution zip file into the D:\NUMI folder. Rename the NumiWebApp folder using the build name of the distribution zip file.

## NUMI Web Site Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using IIS Manager, add a new web site as shown in Figure 32: Add NUMI Website.

![](numi-server-setup-guide-version-15-10/037.png)

<span id="_bookmark101" class="anchor"></span>Figure 32: Add NUMI Website

The NUMI web site basic and advanced settings are shown in Figure 33: NUMI Basic Settings and Figure 34: NUMI Advanced Settings.

![](numi-server-setup-guide-version-15-10/038.png)

<span id="_bookmark102" class="anchor"></span>Figure 33: NUMI Basic Settings

![](numi-server-setup-guide-version-15-10/039.png)

<span id="_bookmark103" class="anchor"></span>Figure 34: NUMI Advanced Settings

The NUMI web site bindings are shown in Figure 35: NUMI Bindings.

![](numi-server-setup-guide-version-15-10/040.png)

<span id="_bookmark104" class="anchor"></span>Figure 35: NUMI Bindings

The NUMI web site authentication settings are shown in Figure 36: NUMI Authentication Settings. Make sure Forms Authentication is the only one enabled.

![](numi-server-setup-guide-version-15-10/041.png)

<span id="_bookmark105" class="anchor"></span>Figure 36: NUMI Authentication Settings

The NUMI website SSL settings are shown in Figure 37: NUMI SSL Settings.

![](numi-server-setup-guide-version-15-10/042.png)

<span id="_bookmark107" class="anchor"></span>Figure 37: NUMI SSL Settings

The NUMI web site compression settings are shown in Figure 38: NUMI Compression Settings.

![](numi-server-setup-guide-version-15-10/043.png)

<span id="_bookmark108" class="anchor"></span>Figure 38: NUMI Compression Settings

## Application Pool Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI application pool setup is shown in Figure 39: Application Pool Window.

![](numi-server-setup-guide-version-15-10/044.png)

<span id="_bookmark111" class="anchor"></span>Figure 39: Application Pool Window

The NUMI application pool basic settings are shown in Figure 40: NUMI Application Pool Basic Settings.

![](numi-server-setup-guide-version-15-10/045.png)

<span id="_bookmark112" class="anchor"></span>Figure 40: NUMI Application Pool Basic Settings

The NUMI application pool advanced settings are shown in Figure 41: NUMI Application Pool Advanced Settings.

![](numi-server-setup-guide-version-15-10/046.png)

<span id="_bookmark113" class="anchor"></span>Figure 41: NUMI Application Pool Advanced Settings

# Install CA SiteMinder Web Agent for Single Sign On (SSO) on the Web server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CA SiteMinder Web Agent needs to be installed and configured on the WebServer where the NUMI web application will be setup. The VA Identity and Access Management (IAM) Team provides the software and instructions to install the CA SiteMinder Web Agent.

## Agent location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current version of software can be found at SiteMinder Webagent share drive.

Copy the 32-bit or 64-bit version of the zip file as appropriate based on the OS in the server and extracts it. You will get a file with name 'ca-wa-12.51-cr08-win32.exe' in case of 32-bit and 'ca-wa-12.51-cr08-win64-64.exe' in case of 64-bit.

## Agent installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the instructions below to install the software on the application server:

1.  Run the exe file you obtained after extracting the zip file. If you get a dialog as shown in Figure 42 click on 'Run' button.

![](numi-server-setup-guide-version-15-10/047.png)

<span id="_Ref478045423" class="anchor"></span>Figure 42: Security Warning

2.  Wait for the dialog shown in Figure 43 to close. It may take little longer for the next dialog to show up.

![](numi-server-setup-guide-version-15-10/048.png)

<span id="_Ref478045780" class="anchor"></span>Figure 43: Preparing to install dialog

3.  Click on 'Next' in the dialog shown in Figure 44.

![](numi-server-setup-guide-version-15-10/049.png)

<span id="_Ref478048631" class="anchor"></span>Figure 44: Web agent install wizard - Welcome screen

4.  Scroll through to the bottom of the license agreement, accept it and click 'Next' button (as shown in Figure 45).

![](numi-server-setup-guide-version-15-10/050.png)

<span id="_Ref478131899" class="anchor"></span>Figure 45: Web agent install wizard - License agreement screen

5.  Leave the default location of installation (as shown in Figure 46) and click 'Next'.

![](numi-server-setup-guide-version-15-10/051.png)

<span id="_Ref478131957" class="anchor"></span>Figure 46: Web agent install wizard - Install location screen

6.  Review the summary screen and click on 'Install' button (as shown in Figure 47).

![](numi-server-setup-guide-version-15-10/052.png)

<span id="_Ref478132065" class="anchor"></span>Figure 47: Web agent install wizard - Review screen

7.  Select 'No. I would like to configure the Agent later' option in the agent configuration screen as shown in Figure 48 and click 'Next'.

![](numi-server-setup-guide-version-15-10/053.png)

<span id="_Ref478132208" class="anchor"></span>Figure 48: Web agent install wizard - Agent configuration screen

8.  Select one of the options in the Install Complete screen as shown in Figure 49 and click on 'Done' button. A restart is required to continue with the agent configuration steps described in the next section. If you selected 'No' you would need to wait until the server is restarted to continue with next steps.

![](numi-server-setup-guide-version-15-10/054.png)

<span id="_Ref478132458" class="anchor"></span>Figure 49: Web agent install wizard - Install complete screen

## Agent configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The next steps require you to launch the agent configuration wizard from the start menu. The Figure 50 shows the one that would need to be launched.

![](numi-server-setup-guide-version-15-10/055.png)

<span id="_Ref478132751" class="anchor"></span>Figure 50: Launch Web Agent Configuration Wizard

If you were configuring the agent for the first time on this specific server, you would need to register the host with the IAM server. In that case, follow the instructions in Section 12.3.1.

Otherwise, skip to Section 12.3.2. Launch the Web Agent Configuration Wizard as described in Figure 50 and continue with the steps in that section.

After you complete any of these configuration steps, you would need to reset IIS by running the following command at admin command prompt:

iisreset

> **NOTE:** You may need to use different values for various options in the below steps if IAM team has provided different values.

### Configuring for the first time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The steps below are if you want to register the server with IAM. This can only be done once. If for any reason you need to reconfigure the whole server, you would need to contact the IAM Team to get the current server registration deleted before you can re-run these steps.

9.  Select 'Yes, I would like to do Host Registration now' and click 'Next' in the dialog as shown in Figure 51.

![](numi-server-setup-guide-version-15-10/056.png)

<span id="_Ref478133519" class="anchor"></span>Figure 51: Web agent configuration wizard - Host registration

10. Enter the following details in the Admin Registration screen (Figure 52), ensure 'Enable Shared Secret Rollover' is unchecked and click 'Next' button.  
    Admin User Name: threg  
    Admin Password: \<will be provided\>

![](numi-server-setup-guide-version-15-10/057.png)

<span id="_Ref478133901" class="anchor"></span>Figure 52: Web agent configuration wizard - Admin credentials

11. Enter the FQDN of the server you are currently configuring in the 'Trusted Host Name' box and one of values from Table 3 based on which IAM environment you are trying to connect to for 'Host Configuration Object' in the next dialog as shown in Figure 53.

<span id="_Ref478135595" class="anchor"></span>Table 3: IAM Host Configuration Object

| Environment | Host Configuration Object |
|-------------|---------------------------|
|             |                           |
| DEV         | DEVHCO                    |
| SQA         | SQAHCO                    |
| Preprod     | Preprod_ext               |
| PROD        | PROD_external_HCO         |

![](numi-server-setup-guide-version-15-10/058.png)

<span id="_Ref478134515" class="anchor"></span>Figure 53: Web agent configuration wizard - Host name and configuration object

12. Add the three IP Address of Policy Server one at a time in the 'IP Address' box from Table 4 based on the IAM environment you are trying to connect to and click 'Next' in the dialog as shown in the Figure 54.

<span id="_Ref478135706" class="anchor"></span>Table 4: SiteMinder Policy Server IP Address

| Environment | SiteMinder Policy Server IP Address |
|-------------|-------------------------------------|
|             |                                     |
| DEV         | xxx.xxx.xxx.xxx                     |
|             | xxx.xxx.xxx.xxx                     |
|             | xxx.xxx.xxx.xxx                     |
| SQA         | xxx.xxx.xxx.xxx                     |
|             | xxx.xxx.xxx.xxx                     |
|             | xxx.xxx.xxx.xxx                     |
| Preprod     | xxx.xxx.xxx.xxx                     |
|             | xxx.xxx.xxx.xxx                     |
|             | xxx.xxx.xxx.xxx                     |
| PROD        | xxx.xxx.xxx.xxx                     |
|             | xxx.xxx.xxx.xxx                     |
|             | xxx.xxx.xxx.xxx                     |

![](numi-server-setup-guide-version-15-10/059.png)

<span id="_Ref478134915" class="anchor"></span>Figure 54: Web agent configuration wizard - Policy server IP Address

13. Select 'FIPS Only Mode' in the next screen as shown in Figure 55 and click 'Next'.

![](numi-server-setup-guide-version-15-10/060.png)

<span id="_Ref478136868" class="anchor"></span>Figure 55: Web agent configuration wizard - FIPS mode setting

14. Leave everything default in the next screen as shown in Figure 56 and click 'Next'

![](numi-server-setup-guide-version-15-10/061.png)

<span id="_Ref478137101" class="anchor"></span>Figure 56: Web agent configuration wizard - Configuration file location

15. Select the web server on which NUMI was installed and click 'Next'. Usually only one will be listed in this dialog as shown in Figure 57.

![](numi-server-setup-guide-version-15-10/062.png)

<span id="_Ref478137418" class="anchor"></span>Figure 57: Web agent configuration wizard - Web server

16. Enter 'NUMIAgentConfig' in 'Default Agent Configuration Object,' check 'Enable Agent' and uncheck 'Manage Application Pools' in the next screen as shown in Figure 58 and click 'Next'.

![](numi-server-setup-guide-version-15-10/063.png)

<span id="_Ref478137772" class="anchor"></span>Figure 58: Web agent configuration wizard - Agent configuration

17. Select the NUMI website and any other sites where you want to enable SSO on and click 'Next'.

![](numi-server-setup-guide-version-15-10/064.png)

<span id="_Toc478591166" class="anchor"></span>Figure 59: Web agent configuration wizard - Sites selection

18. Review the options you selected in the summary screen as shown in Figure 60 and click on 'Install' button.

![](numi-server-setup-guide-version-15-10/065.png)

<span id="_Ref478377425" class="anchor"></span>Figure 60: Web agent configuration wizard - Summary screen

19. Click on 'Done' when you see the completion screen as shown in Figure 61.

![](numi-server-setup-guide-version-15-10/066.png)

<span id="_Ref478378873" class="anchor"></span>Figure 61: Web agent configuration wizard - Completion screen

### Reconfiguration configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The steps below are if you want to reconfigure one or more websites in IIS due to say re-deployment. The server should have already been registered with IAM using the steps in Section 12.3.1.

20. Select 'No, I would like to do Host Registration later' and click 'Next' in the dialog as shown in Figure 62.

![](numi-server-setup-guide-version-15-10/067.png)

<span id="_Ref478480339" class="anchor"></span>Figure 62: Web agent configuration wizard - Host registration

21. Select the web server on which NUMI was installed and click 'Next'. Usually only one will be listed in this dialog as shown in Figure 63.

![](numi-server-setup-guide-version-15-10/068.png)

<span id="_Ref478480311" class="anchor"></span>Figure 63: Web agent configuration wizard - Web server

22. Enter 'NUMIAgentConfig' in 'Default Agent Configuration Object' if not already entered, check 'Enable Agent' and uncheck 'Manage Application Pools' in the next screen as shown in Figure 64 and click 'Next'.

![](numi-server-setup-guide-version-15-10/069.png)

<span id="_Ref478480272" class="anchor"></span>Figure 64: Web agent configuration wizard - Agent configuration

23. Select the NUMI website and any other sites where you want to enable SSO on and click 'Next'. The sites that were previously configured will remain selected and cannot be changed (unconfigured) as shown in Figure 65.

![](numi-server-setup-guide-version-15-10/070.png)

<span id="_Ref478480597" class="anchor"></span>Figure 65: Web agent configuration wizard - Sites selection

24. Review the options you selected in the summary screen as shown in Figure 66 and click on 'Install' button.

![](numi-server-setup-guide-version-15-10/071.png)

<span id="_Ref478480624" class="anchor"></span>Figure 66: Web agent configuration wizard - Summary screen

25. In the screen shown in Figure 67, select appropriate option for the site you are trying to reconfigure and click 'Next'.

> 'Overwrite' will overwrite the previously configured settings with the new one entered in the previous steps of this wizard. 'Preserve' will not change any existing settings but will add missing settings back in to the site. If 'Unconfigure' is selected it will remove and disable SSO for the selected site.

![](numi-server-setup-guide-version-15-10/072.png)

<span id="_Ref478480885" class="anchor"></span>Figure 67: Web agent configuration wizard - Previously configured sites

26. Review the options you selected in the summary screen as shown in Figure 68 and click on 'Install' button.

![](numi-server-setup-guide-version-15-10/073.png)

<span id="_Ref478481585" class="anchor"></span>Figure 68: Web agent configuration wizard - Summary screen

27. Click on 'Done' when you see the completion screen as shown in Figure 69.

![](numi-server-setup-guide-version-15-10/074.png)

<span id="_Ref478481157" class="anchor"></span>Figure 69: Web agent configuration wizard - Completion screen

# Secure Token Service Integration for SSOi

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI supports secure token service implementation through SSOi. Full details of the implementation can be found at SSOi Secure Token Service Playbook.

## Download Certificate Chain from appropriate endpoint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Downloading the chain can be done from any computer but installing the chain must be done as the local computer account of the server being set up.

- iDEV:  [RequestSecurityToken](https://int.services.eauth.va.gov:9301/STS/RequestSecurityToken) dev url
- SQA: [RequestSecurityToken](https://sqa.services.eauth.va.gov:9301/STS/RequestSecurityToken) SQA url
- PREPROD: [RequestSecurityToken](https://preprod.services.eauth.va.gov:9301/STS/RequestSecurityToken) Pre-Prod url
- PROD: [RequestSecurityToken](https://services.eauth.va.gov:9301/STS/RequestSecurityToken)
  1.  Install the full certification chain from the matching IAM environment(s). This can be obtained by visiting the link and clicking the lock icon and choosing "View Certificates".  
      https://<span class="mark">redacted</span>:9301/

> ![](numi-server-setup-guide-version-15-10/075.png)

1.  Install the full certification chain from the matching IAM environment(s). This can be obtained by visiting the link and clicking the lock icon and choosing "View Certificates".  
    https:// <span class="mark">redacted</span>:9301/

> ![](numi-server-setup-guide-version-15-10/076.png)

2.  Click on the Details tab and select "Copy to file", choose PKCS and include all certificates in the path if possible

> ![](numi-server-setup-guide-version-15-10/077.png)

3.  Save file as \<endpointname_date\>, click next then finish.

> ![](numi-server-setup-guide-version-15-10/078.png)

4.  Optional – Reuse this file if another web server requires this STS endpoint's certificate.
5.  In MMC, right click Computer-Personal store and import the certificate created in Step 9.

> ![](numi-server-setup-guide-version-15-10/079.png)

6.  Import for local machine

> ![](numi-server-setup-guide-version-15-10/080.png)

7.  Browse to file created in step 10 and click Next

> ![](numi-server-setup-guide-version-15-10/081.png)

8.  Place all certificates in the Personal store, click next and finish

> ![](numi-server-setup-guide-version-15-10/082.png)

9.  The imported certificate should now be in the store (refreshing may be required). It will follow the naming convention xxxx.services.eauth.va.gov

> ![](numi-server-setup-guide-version-15-10/083.png)

## Export server cert to .pfx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a copy of the .cer installed locally to the computer/personal account. It should be the one served by IIS when you navigate to the website.

1.  Load the Microsoft Management Console, Certificate Snap-in, for the local computer

# Find the server cert in the personal folder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](numi-server-setup-guide-version-15-10/084.png)

# Right click and export the certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](numi-server-setup-guide-version-15-10/085.png)

# Select "Yes, export private key" and choose next

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](numi-server-setup-guide-version-15-10/086.png)

# Select "Export all extended properties" and choose next

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](numi-server-setup-guide-version-15-10/087.png)

# Select a strong password. This password will go into NumiWebApp.config later in this guide.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](numi-server-setup-guide-version-15-10/088.png)

# Select a filename for the exported certificate and save it as a .pfx. Select a folder not specific to a version of NUMI as this cert will be valid for future versions of the applications until expiration. For example, if the folder structure for website is NUMI/NUMI_15.9 select the /NUMI folder for the cert and not the specific /NUMI_15.9 folder. This file path will go into NumiWebApp.config later in this guide.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## NumiWebApp.config keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\

34. Navigate to the CERMe install image and double click the install.htm file in the root directory to open the setup welcome page. This will open the CERMe install page in Internet Explorer.
35. Click on the Install Review Manager 21.0.1 / InterQual View 2022 link on the installation page. This will prompt to save or run the file, select Run. This will start the CERMe Install wizard.
36. Accept the license agreement and click Next.
37. On the License Information screen, enter the license information given above and click Next.
38. On the Select Review Manager Enterprise screen, select "Review Manager Enterprise" and click Next.
39. On the Installation Type screen, select "New Installation" and click Next.
40. Select an installation directory.
41. On the Choose Components screen, keep the default selection (i.e., all selected) and click Next.
42. On the Database Information page, enter the following info and click Next.
- Database type: SQL Server
- Server Name: Name of the SQL database server
- Database: Name of the database to which the dump restored in step 1
- Port Number: SQL Server
- Instance: leave blank
- User ID: SQL Server user ID with access to the CERMe database restored above
- Password: Password for the SQL Server user used above
43. On separate database to store report data screen, select No and click Next.
44. On the Install Jetty window, select Yes to install Jetty.
45. On the next screen, enter 8357 for Port Number.
46. On the next screen, select the hardware architecture.
47. Review the selections, and click Install to start the installation.
48. Once the installation completes, go to the URL: http://\<servername\>:8357/rm/login.

    This is should open the CERMe login page.
49. Now follow the steps below to update CERMe to CERMe 21.0.1.
50. Stop the CERMe Service from the Windows Services.
51. Create a backup of the CERMe Installation folder and the CERMe database.
52. Make the changes to the file (below)on the CERMe Jetty Server:

#### File: \<CERMe Install Folder\>\Jetty\etc\webdefault.xml

Add the following element to \<session-config\> element.

\<cookie-config\>

\<http-only\>true\</http-only\>

\</cookie-config\>

Session Config element should look like the following after the change:

\<session-config\>

\<session-timeout\>30\</session-timeout\>

\<cookie-config\>\<http-only\>true\</http-only\>\</cookie-config\>

\</session-config\>

#### File: \<CERMe Install Folder?\Jetty\etc\jetty-rewrite.xml

Add the following \<Call\> element to the end of the \<New\> element.

\<Call name="addRule"\>

\<Arg\>

\<New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"\>

\<Set name="pattern"\>/\*\</Set\>

\<Set name="name"\>Strict-Transport-Security\</Set\>

\<Set name="value"\>max-age=31536000; includeSubDomains\</Set\>

\</New\>

\</Arg\>

\</Call\>

The file will look like the following after the change:

\<Set name="handler"\>

\<New id="Rewrite" class="org.eclipse.jetty.rewrite.handler.RewriteHandler"\>

\<Set name="handler"\>\<Ref refid="oldhandler"/\>\</Set\>

\<Set name="rewriteRequestURI"\>\<Property name="rewrite.rewriteRequestURI" default="true"/\>\</Set\>

\<Set name="rewritePathInfo"\>\<Property name="rewrite.rewritePathInfo" default="false"/\>\</Set\>

\<Set name="originalPathAttribute"\>\<Property name="rewrite.originalPathAttribute" default="requestedPath"/\>\</Set\>

\<Call name="addRule"\>\<Arg\>\<New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"\>\<Set name="pattern"\>/\*\</Set\>\<Set name="name"\>Strict-Transport-Security\</Set\>\<Set name="value"\>max-age=31536000; includeSubDomains\</Set\>\</New\>\</Arg\>\</Call\>

\</New\>

\</Set\>

#### File: \<CERMe Install Folder\>\Jetty\start.ini

Add the following new section to the bottom of the file:

\# ===========================================================

\# Enforce Strict Transport Security

\# -----------------------------------------------------------

OPTIONS=rewrite

etc/jetty-rewrite.xml

#### File: \<CERMe Install Folder\>\Jetty\ReviewManager.xml

Add the content below to the end of the \< Config \> element

\<IntegratedLogin Enabled="true" CookieName="unifiedkey" UnifiedKey="8rzVNfLwjHWHvPctaen9dw=="

AuthenticationFailUrl="/iqm/html/rm_integrated_authentication_failed.htm" GuidUserCid="IQ_1" Guid="A1B0B165-3C18-4561-935F-5FB81BD42128"

AuthenticateWS="false"/\>

The modified file will look like the following:

…

\<Path Prefix="/rm"/\>

\<Login Check="true"/\>

\<IntegratedLogin Enabled="true" CookieName="unifiedkey" UnifiedKey="8rzVNfLwjHWHvPctaen9dw==" AuthenticationFailUrl="/iqm/html/rm_integrated_authentication_failed.htm" GuidUserCid="IQ_1" Guid="A1B0B165-3C18-4561-935F-5FB81BD42128" AuthenticateWS="false"/\>

\</Config\>

\</ReviewManager\>

53. Start CERMe Service from the Windows Services.
54. Go to CERMe URL: https://\<server\>:8443/rm/login Login with the credential provided, and go to the menu Help \> About. It should show Version InterQual Review Manager™ 21.0.1 (Build 4).
55. This completes the installation of the CERMe RM 21.0.1 InterQual View 2022.

## Install CERMe SSL Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI will need SSL certificates for CERMe (for Jetty). NUMI uses the SSL certificate for the server that CERMe is running on. If the sever does not have a SSL certificate installed, follow the normal VA processes for obtaining SSL Certificates and install it.

1.  Use IIS Manager to export the current certificate to a .pfx file. Select the server name in the Connections pane and double click on the Server Certificates in the IIS pane as shown in Figure 70.

![](numi-server-setup-guide-version-15-10/089.png)

<span id="_bookmark117" class="anchor"></span>Figure 70: IIS Server Certificates

56. Select the certificate to export and click on the "Export…" link in the Actions pane, as shown in Figure 71.

![](numi-server-setup-guide-version-15-10/090.png)

<span id="_bookmark118" class="anchor"></span>Figure 71: IIS Server Certificate Selection

57. Set the name of the .pfx file. Set the password, e.g., use numi (all lowercase) for the password, as shown in Figure 72. This password will be used in subsequent steps.

![](numi-server-setup-guide-version-15-10/091.png)

<span id="_bookmark119" class="anchor"></span>Figure 72: IIS Certificate Details

> **NOTE:** For the following, the password can be whatever you choose, but please make a note of them, as they will be used later. For this example, D:\Certs\NUMI.pfx is the file name and the password, the one that you used to export the .pfx file, e.g., numi (all lowercase).

58. Open a command prompt window and change the current directory to the location of the keytool executable. In this example it would be:

D:\Program Files (x86)\Change Healthcare\CERME\Jre\bin\keytool.exe

59. Execute the following command:

keytool -importkeystore -srcstoretype PKCS12 -srckeystore "D:\Certs\NUMI.pfx" -destkeystore "D:\Certs\CERME.ks"

> **NOTE:** -srckeystore value will be the .pfx path and filename above, -destkeystore can be whatever you choose; again, passwords can be whatever you choose, but please make a note of them. The word "secret" is used as the keystore password in this example.

60. Execute the following command:

Keytool –list -keystore "D:\Certs\CERME.ks"

Make a note of the long, auto-generated alphanumeric value circled in red below. Recommended actions are to copy, paste the entire command prompt output to notepad to copy, and paste this value.

![](numi-server-setup-guide-version-15-10/092.png)

<span id="_bookmark120" class="anchor"></span>Figure 73: keytool -keystore "C:\Certs\CERME.ks" –list

61. Execute the following command:

keytool -changealias -keystore "D:\Certs\CERME.ks" -destalias numi –alias \<alphanumeric value\>

> **NOTE:** Replace \<alphanumeric value\> with the value noted and circled from the step above. The keystore password is the password specified when creating the keystore above, secret in our example. The key password is the password specified when creating the pfx file, numi in our example.

62. Execute the following command:

keytool -keypasswd -keystore "D:\Certs\CERME.ks" -alias numi

> **NOTE:** With this command, we are changing the key password to "reallysecret" for this example.

63. Next, copy the keystore, (D:\Certs\CERME.ks), to the Jetty\etc directory. For this example, it would be here: D:\Program Files (x86)\Change Healthcare\CERME\Jetty\etc.
64. Modify \<Jetty-home\>\start.ini. Uncomment the relevant lines in the SSL Context and HTTPS Connector sections of start.ini file (as shown in the example below).

\#=========================================================

\# SSL Context

\# Create the keystore and trust store for use by

\# HTTPS and SPDY

\#-------------------------------------------------------------------

jetty.keystore=etc/keystore

jetty.keystore.password=(your password)

jetty.keymanager.password=(your password)

jetty.truststore=etc/keystore

jetty.truststore.password=(your password)

jetty.secure.port=(your SSL port number)

etc/jetty-ssl.xml

\#===========================================================

\# HTTPS Connector

\# Must be used with jetty-ssl.xml

\#-----------------------------------------------------------

jetty.https.port=(your SSL port number)

etc/jetty-https.xml

65. Open the windows services management console, (START-\>RUN-\>services.msc-\>OK), and restart the CERMe service. It will take about 20 to 30 seconds for the service to restart completely but you should be able to browse directly to the secure CERMe. Use whatever URL is used to access NUMI, e.g., https://vaww.prod.temp.numi.med.va.gov/web/home.aspx
66. Replace the "/web/home.aspx" portion with CERMe' s secure port, (8443 by default), e.g., https://vaww.prod.temp.numi.med.va.gov:8443/

The CERMe website should be displayed and you should not have been warned of the security certificate problem.

# Setting up NUMI Section in the Windows Event Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Change Directory - Go to command prompt (run as Administrator) and change current directory to Framework v2.0 bit folder e.g., C:\WINDOWS\MS.NET\Framework\v4.5.x
67. Install Command - Type InstallUtil.exe /I \< source folder full path \>\bin\NumiWebApp.dll under Framework v4.5 folder and press enter.

e.g., InstallUtil.exe /i D:\NUMI\\install_dir\>\bin\NumiWebApp.dll

68. This should create a NUMI section in the Windows Event log.

![](numi-server-setup-guide-version-15-10/093.png)

<span id="_bookmark122" class="anchor"></span>Figure 74: Creating a NUMI section in the Windows Event Log

69. NUMI Event Folder Properties
    1.  Go to NUMI Properties by right mouse.
    2.  Click on General Tab under NUMI Properties dialog box window. Check/Click on Overwrite events as needed.
    3.  Press \<Apply\> button (if needed) and Press \<OK\> button.
    4.  Verify Event View, if any error logs occurred during the installation.

## Validate XML Configuration File Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that all XML configuration file settings are correct. Validate NUMI XML Configuration File Settings.

1.  Edit the application settings in the web.config file in the NUMI folder. E.g., D:\NUMI\\install_dir\>\web.config

Settings to update:

\

72. Click the Command Prompt (or \<Run\>, depending on the Operating System)
73. Type: IISReset
74. Click \<Enter\>.

# Test NUMI Web Site Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open Internet Explorer and type: http:// <span class="mark">redacted</span>.aspx e.g., https:// <span class="mark">redacted</span>.aspx

# Installing NUMI Synchronizer on the DB Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Copy the Sychronizer_Setup.msi file to the intended environment. This file will be provided by Tier 3 maintenance and should be stored on each environment

![](numi-server-setup-guide-version-15-10/095.png)

- If an upgrade in place, stop the existing service in task manager and uninstall from program files

![](numi-server-setup-guide-version-15-10/096.png)

![](numi-server-setup-guide-version-15-10/097.png)

2.  Launch the Synchronizer Setup file
3.  Click Next

![](numi-server-setup-guide-version-15-10/098.png)

4.  Choose the everyone option and browse to the desired directory

![](numi-server-setup-guide-version-15-10/099.png)

5.  Click next

> ![](numi-server-setup-guide-version-15-10/100.png)

6.  Click Close

> ![](numi-server-setup-guide-version-15-10/101.png)

7.  Enter the connection information for VIA & NUMI DB into the Synchronizer.config and Sychronizer.exe.config. Use the database server full name in source, e.g. VAAUSNUMSQLXX.aac.dva.va.gov where XX is the number of the database.

\<!-- VIA Service configuration --\>

\<add key="VIAServiceURL" value="<u>\<VIA Endpoint URL\></u>" /\>

\<add key="VIARequestingApp" value="NumiBatch"/\>

\<add key="VIAConsumingAppToken" value*=*"*(SEE PW VAULT)"/\> PW Vault under "NUMISynchronizer PWs (VIARequestingApp)*" <u>Under NOTES section</u>

\<add key="VIAConsumingAppPassword" value="*(See PW VAULT)"/\> PW Vault under "NUMI Synchronizer PWs (VIARequestingApp)*" <u>Under NOTES section</u>

\<add key="numiDbConnectionString" value="Data Source=*VAAUSNUMSQLXX.aac.dva.va.gov*;Database=*NUMI*;User ID=*numi_user*;Password= *PW Vault under "NUMI Synchronizer PWs (VIARequestingApp)"NOTES section* ;Trusted_Connection=False" /\>

\<add key="reportDbConnectionString" value="Data Source=*VAAUSNUMSQLXX.aac.dva.va.gov*;Database=*NUMI*;User ID=<u>numi_user</u>;Password=*PW Vault under "NUMI Synchronizer PWs (VIARequestingApp)"* NOTES section;Trusted_Connection=False" /\>

8.  Restart the service from task manager or the services mmc.

![](numi-server-setup-guide-version-15-10/102.png)

## Uninstall:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to uninstall the NUMI Synchronizer services use add/remove programs and right click on the synchronizer.

![](numi-server-setup-guide-version-15-10/103.png)

## Validate Installation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To confirm the synchronizer installation

Open MS SQL Server Management Studio after 2 hours. Open a new query and type:

Use numi go.

Select TOP 1000 \* from patientstay.

Click the \<Execute\> button to run the query. New records shall display.

## Add Jobs to the SQL Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 3 jobs that must be added to the SQL Server:

1.  NUMI_PhysicianAdvisorPatientReview_AutoExpire
2.  LogSynchDB_ValidateSynchronizer
3.  NUMI_AlterIndex_Rebuild

These jobs can be installed from scripts (included in the build) or, if you are transferring from another server, you can right click on each job and script as DROP and CREATE.

Backup the jobs before you run the scripts. Modify the scripts to replace the @owner_login_name with the owner login name appropriate for your installation, if necessary.

NUMI_PhysicianAdvisorPatientReview_AutoExpire is a job that executes the Stored Procedure usp_PhysicianAdvisorPatientReview_AutoExpire every day at midnight. The Stored Procedure looks for Physician UM Advisor (PUMA) Reviews that have not been completed within 14 days and marks them as Completed with a reason description of Expired.

LogSynchDB_ValidateSynchronizer is job that executed the stored procedure LogSyncDB.dbo.usp_LogSync_ValidateSynchronizer every hour. This stored procedure confirms imported stays within the last 3 hours and reports the problem to a pre-defined e- mail distribution list determined by the needs of the installation.

NUMI_AlterIndex_Rebuild is a job that executes the stored procedure NUMI.dbo.usp_AlterIndex_Rebuild. This stored procedure rebuilds the indexes for the tables in the NUMI database.

# Post-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are post-installation considerations for NUMI, this information will be provided by the appropriate project teams.

# Acronyms and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym |     | Description                                          |     |
|---------|-----|------------------------------------------------------|-----|
| CERMe   |     | Care Enhance Review Management Enterprise            |     |
| CPRS    |     | Computerized Patient Record System                   |     |
| CPU     |     | Central Processing Unit                              |     |
| HTTP    |     | HyperText Transfer Protocol                          |     |
| HTTPS   |     | HyperText Transfer Protocol Secure                   |     |
| IAM     |     | Identity and Access Management                       |     |
| IIS     |     | Internet Information Services                        |     |
| MDWS    |     | Medical Domain Web Services                          |     |
| NUMI    |     | National Utilization Management Integration          |     |
| PM      |     | Project Manager                                      |     |
| PUMA    |     | Physician UM Advisor                                 |     |
| QA      |     | Quality Assurance                                    |     |
| SQL     |     | Standard Query Language                              |     |
| SSL     |     | Secure Socket Layer                                  |     |
| SSO     |     | Single Sign On                                       |     |
| UM      |     | Utilization Management                               |     |
| URL     |     | Uniform Resource Locator                             |     |
| VIA     |     | VistA Integration Adaptor                            |     |
| VistA   |     | Veterans Information Systems Technology Architecture |     |

# NUMI Comparison Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| NUMI Version | CERMe RM | InterQual View | CA SiteMinder | Windows Server | MS SQL Server |
|--------------|----------|----------------|---------------|----------------|---------------|
| 15.4         | 16.1     | 2017.2         | 12.51         | 2012 R2        | 2012          |
| 15.5         | 17       | 2018.1         | 12.51         | 2012 R2        | 2012          |
| 15.6         | 17       | 2018.1         | 12.51         | 2012 R2        | 2012          |
| 15.8         | 18.1     | 2019.1         | 12.51         | 2012 R2        | 2012          |
| 15.9         | 19.0     | 2020           | 12.51         | 2012 R2        | 2012          |
| 15.9.1       | 20.0     | 2021           | 12.52         | 2019           | 2019          |
| 15.10        | 21.0.1   | 2022           | 12.52         | 2019           | 2019          |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: NUMI Server Setup Guide

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Server Setup Guide explains how to install National Utilization Management Integration (NUMI).

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to explain the hardware and software requirements and tasks that must be performed before and after the installation process.

### Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of this document includes explanations of the appropriate steps to install the NUMI software, and the steps that are needed to be completed before and after the installation process is started.

### Target Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is intended for the Information Technology Team and the individuals who install software in your organization.

## Deployment Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following process is followed to request permission to do a National Deployment.

### National Deployment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ProPath Release Management processes govern the request for a National Deployment. Refer to ProPath for guidance on requesting a release. This process must be complete before installation of services on the NUMI servers.

### Installing NUMI on the Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps to install NUMI on the servers are described below. The middle tier of NUMI is the Veterans Information Systems Technology Architecture (VistA) Integration Adapter (VIA), which is a hosted service and is not part of the NUMI deployment. The primary NUMI application servers are located at the Austin Information Technology Center (AITC) facility in Austin, Texas. The application servers run on an Internet Information Services (IIS) Application Server. The NUMI application requires Microsoft (MS) ASP.NET 2.0 Ajax Extensions 1.0 and Web Services Enhancements 3.0 to enable the interactions with the Web Services.

#### Database Server

The NUMI database as it exists now is a manifestation of multiple changes over multiple releases. This installation document has as a pre-requisite the backup of an existing NUMI database. Therefore, to install a new NUMI database, it is necessary to restore a backup of an existing NUMI database.

Database Platform installation, and Database Restoration Procedures

1.  Install Windows Server 2019 on the database server platform
2.  Download and install any critical patches for the Operating System
3.  Install the 64-bit MS Structured Query Language (SQL) Server 2019 application according to local "best practices"
    1.  MS's Full Text Search is required for the NUMI installation
    2.  Replication is necessary for the NUMI installation to use the alternate database reporting capability of NUMI
    3.  Reporting Services is not necessary for installation on the NUMI database server
    4.  NUMI's database will function properly in cluster, but clustering is not required for the NUMI application
4.  Apply all appropriate patches (according to local best practices) to MS SQL Server 2019
5.  Install / restore the database components according to the instructions in section 4.1 Instructions for Installing Database Components.

#### Web Server

To install NUMI Exchange software on the Web Server (Server 2):

1.  Install Windows Server 2019 on the web server platform
6.  Download and install any critical patches for the Operating System on all web servers
7.  Install MS ASP.NET 2.0 Ajax Extensions 1.0
8.  Install Web Services Enhancements 3.0
9.  Install NUMI Exchange
10. Change the web.config file settings as needed

#### Application Server

To install NUMI application software on the Application Server (Server 3)

1.  Install Windows Server 2019 on the application server platform
11. Download and install any critical patches for the Operating System on all application servers
12. Install the Care Enhance Review Management Enterprise (CERMe) 22.0 InterQual View 2025 application
13. Install the NUMI application
14. Change the web.config file settings as needed

## Pre-Installation Instructions and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pre-Installation Instructions and Preparation section explains the tasks that need to be performed before installing NUMI software. Before proceeding with the installation procedures, consult the list of requirements below.

### Installation Process Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An assumption is made that the person responsible for doing installations at your site has performed appropriate pre-installation planning.

#### Minimum Software Version

Operating System: Windows Server 2019

Database: SQL Server 2019

#### Resources Required

Sys Admin, DBA

#### CPU Capacity

64GB RAM, Dual 2.20 GHz Intel Xeon®E5-2698 v4 – Database Server

12GB RAM, Dual 2.20 GHz Intel Xeon®E5-2698 v4 – Application Server

12GB RAM, Dual 2.20 GHz Intel Xeon®E5-2698 v4 – Web Server

#### Disk Space

Application server – 100 GB Web Services server – 100 GB

Database – E:900 GB, F:700 GB, L:200 GB, O:400 GB (This includes space needed for the backups and data storage.)

#### Devices (Servers, etc.)

> 1 Database Server

> 2 Application Servers

> 2 Web Servers

> 1 Data Warehouse Server 1 SQL Reporting Server

#### VistA Rights Needed for NUMI Users

Each NUMI user must have Computerized Patient Record System (CPRS) access in their VistA menu structure, such as in their secondary menu tree. The VistA menu name is CPRSChart (or CPRS Graphical User Interface CHART). Table 1 and Table 2 identify the menus, options and settings these user accounts will need to have assigned.

It is also highly recommended that the VIAB WEB SERVICES OPTION be added to the System Command Options \[XUCOMMAND\] menu in each site's VistA system. If you do not add this to the Common Menu, you will need to add it to the secondary menu of each individual NUMI user.

| CPRS Rights                                 |
|---------------------------------------------|
| Primary Menu: XMUSER                        |
| Primary Menu: MailMan Menu                  |
| Secondary Menu: \[OR CPRS GUI CHART\]       |
| Secondary Menu: CPRSChart Release 1.0.30.72 |
| Keys Held                                   |
| Patient Selection                           |
| Restrict? NO                                |
| OE/RR List                                  |

<span id="_bookmark19" class="anchor"></span>Table 2: CPRS Access Tabs

| Name | Description | Effective Date | Expiration Date |
|------|-------------|----------------|-----------------|
| RPT  | Reports tab | Sept. 2, 2008  | N/A             |

### Install Software in Test Environments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software will be installed in the Test environments before installing in Production.

### Generate Pre-Installation Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

### Coordinate Installation with Other Teams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Installation Team will need to involve the Implementation/Architecture Team.

### Install Sequence Information for Multiple Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

### Logoff During Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

End users do not need to be logged off during installation (during the act of copying files and installation executions to the server(s)). However, the users must be logged off for any updates to the software (running the executions and/or configuring the software and configuration files).

Logging off during software updates is no different from any other logoff that a user may do.

### Average Amount of Time Required to Complete the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The average amount of time required to complete the NUMI installation is 2 days.

## Database Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the NUMI Systems Management Guide for information about the structure and components of the NUMI database.

### Instructions for Installing Database Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI database as it exists now is a manifestation of multiple changes over multiple releases. This installation document has as a pre-requisite the backup of an existing NUMI database. Therefore, to install a new NUMI database, it is necessary to restore a backup of an existing NUMI database.

#### Database Installation / Restoration Procedures

1.  Copy a backup of an existing NUMI database(s) of appropriate size and content to the new NUMI database server
    1.  The application database (typically called NUMI) is necessary for proper function of the application
    2.  The "auditing" database (typically called LogSyncDb) is necessary for proper functioning of the application and the synchronizer
    3.  The CERMe database can be restored from an existing backup, or can be built from scratch from the CERMe installation media
        1.  If the CERMe database is restored from an existing backup, verify that the application configuration files reference a database authenticated user that has DBO privilege on the CERMe database for proper functioning of the NUMI application
        2.  If the CERMe database is installed from media, follow the instructions provided by Change Healthcare for installation
15. Restore the database backup to the existing server
    1.  File paths will have to be altered according to local best practices
    2.  User accounts may be, but are not required to be, restored with the database. NUMI requires the numi_user account to be setup.
    3.  Database ownership may be altered so that the owning account for the NUMIdatabase complies with local best practices
    4.  A database authenticated user for the application should be configured, and granted DBO privileges on the NUMI database
16. Run the Install_XX.sql if it was provided with the build, where XX is the database version for the NUMI build. This will apply changes to the database necessary for the version of NUMI that is being installed
17. Install the NUMI Synchronizer according to the instructions in section 17 Installing NUMI Synchronizer on the DB Server

## Installation Procedure for Server 2019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section identifies the installation procedures that shall be followed.

### Patch the Operating System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This applies to all servers.

1.  Open up an instance of Internet Explorer.
18. Select menu item \<Tools/Windows Update\>.
19. Follow the instructions on MS's website. (NOTE: A restart of the servers may be necessary).

## SQL Server Setup (Windows Server 2019)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Role Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The role set-up in this section applies to the SQL database server. Use Server Manager to install the File Services with the role services shown in Figure 1: SQL Server Role Services.

<span id="_Hlk166518008" class="anchor"></span>Figure 1: SQL Server Role Services

![](numi-server-setup-guide/002.png)

## Web Server Setup (Windows Server 2019)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Role Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The role setup in this section applies to the NUMI Exchange web server.

Use Server Manager to install the File Services and Web Server (IIS) roles with the role services shown in Figure 2: NUMI Exchange Role Services and

Figure 3: NUMI Exchange (IIS).

<span id="_Hlk166518017" class="anchor"></span>Figure 2: NUMI Exchange Role Services

![](numi-server-setup-guide/003.png)

<span id="_bookmark36" class="anchor"></span>

Figure 3: NUMI Exchange (IIS)

![](numi-server-setup-guide/004.png)

### ASP.NET 2.0 AJAX Extensions 1.0 Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install the ASP.NET 2.0 Ajax Extensions 1.0 as detailed in section 8.3, Install MS ASP.NET 2.0 Ajax Extensions 1.0.

### MS Web Services Enhancements (WSE) 3.0 Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install MS WSE 3.0 as detailed in section 8.4 Install MS Web Services Enhancements 3.0.

## Application Server Setup (Windows Server 2019)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Role Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The role setup in this section applies to the NUMI app servers. Use Server Manager to install the File Services and Web Server (IIS) roles with the role services shown in Error! Not a valid bookmark self-reference. and Figure 5: NUMI Web Services IIS.

<span id="_Toc225235838" class="anchor"></span>Figure 4: NUMI Role Services

![](numi-server-setup-guide/005.png)

<span id="_bookmark42" class="anchor"></span>Figure 5: NUMI Web Services IIS

![](numi-server-setup-guide/006.png)

### Feature Delegation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select the main node in IIS, with the server name. Then double click on "Feature Delegation" item. Change the "Feature Delegation" settings for the server, as shown in Figure 6: IIS Feature Delegation.

<span id="_Hlk166518039" class="anchor"></span>Figure 6: IIS Feature Delegation

![](numi-server-setup-guide/007.png)

Make sure all authentication rules are set to Read/Write as shown in Figure 7: Feature Delegation Selection.

<span id="_Hlk166518044" class="anchor"></span>Figure 7: Feature Delegation Selection

![](numi-server-setup-guide/008.png)

### Install MS ASP.Net 2.0 AJAX Extensions 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installing MS ASP.NET 2.0 Ajax Extensions 1.0 applies to the web servers only.

1.  Download the MS ASP.NET 2.0 Ajax Extensions 1.0 from MS's website.
20. Run the ASPAJAXExtSetup.msi by double-clicking it.
21. When the File Download – Security Warning window displays, click the \<Run\> button (shown in Figure 8: MS ASP.Net 2.0 File Download-Security Warning Window).
22. 

<span id="_Hlk166518053" class="anchor"></span>Figure 8: MS ASP.Net 2.0 File Download-Security Warning Window

![](numi-server-setup-guide/009.png)

23. When the Internet Explorer – Security Warning window displays, click the \<Run\> button (shown in Figure 9: MS ASP.Net 2.0 Internet Explorer-Security Warning Window).

<span id="_Hlk166518057" class="anchor"></span>Figure 9: MS ASP.Net 2.0 Internet Explorer-Security Warning Window

![](numi-server-setup-guide/010.png)

24. When the MS ASP.NET 2.0 AJAX Extensions 1.0 Setup window displays, click the \<Next\> button (shown in Figure 10: MS ASP.NET 2.0 AJAX Extensions 1.0 Setup Wizard Window).

<span id="_Hlk166518062" class="anchor"></span>Figure 10: MS ASP.NET 2.0 AJAX Extensions 1.0 Setup Wizard Window

![](numi-server-setup-guide/011.png)

Click the "I accept the terms in the License Agreement" checkbox, as illustrated in Figure 11: MS ASP.NET 2.0 AJAX License Agreement Window.

1.  Click the \<Next\> button.

<span id="_Hlk166518067" class="anchor"></span>Figure 11: MS ASP.NET 2.0 AJAX License Agreement Window

![](numi-server-setup-guide/012.png)

25. Click the \<Install\> button (shown in Figure 12: MS ASP.NET 2.0 AJAX Installation Window).

<span id="_Hlk166518072" class="anchor"></span>Figure 12: MS ASP.NET 2.0 AJAX Installation Window

![](numi-server-setup-guide/013.png)

26. The installation is complete. Select the \<Finish\> button by clicking on it to exit the installation wizard, as depicted in Figure 13: MS ASP.NET 2.0 AJAX Completion window.

![](numi-server-setup-guide/014.png) If you do not wish to view the release notes, un-check the "Display MS ASP.NET 2.0 AJAX Extensions 1.0 Release Notes" checkbox.

<span id="_Hlk166518078" class="anchor"></span>Figure 13: MS ASP.NET 2.0 AJAX Completion window

![](numi-server-setup-guide/015.png)

### Install MS Web Services Enhancements 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installing MS Web Services Enhancements 3.0 applies to the web servers only.

1.  Download the MS Web Services Enhancements 3.0 from MS's website.
27. Run the MS WSE 3.0.msi by double-clicking it.
28. When the File Download – Security Warning window displays, click the \<Run\> button (shown in Figure 14: MS WSE 3.0 File Download-Security Warning Window).

<span id="_Hlk166518086" class="anchor"></span>Figure 14: MS WSE 3.0 File Download-Security Warning Window

![](numi-server-setup-guide/016.png)

2.  When the Internet Explorer – Security Warning window displays, click the \<Run\> button (shown in Figure 15: MS WSE 3.0 Internet Explorer-Security Warning Window).

<span id="_Hlk166518091" class="anchor"></span>Figure 15: MS WSE 3.0 Internet Explorer-Security Warning Window

![](numi-server-setup-guide/017.png)

3.  When the MS WSE 3.0 – InstallShield Wizard window displays, click the \<Next\> button (shown in Figure 16: MS WSE 3.0 InstallShield Wizard Welcome Window).

<span id="_Hlk166518095" class="anchor"></span>Figure 16: MS WSE 3.0 InstallShield Wizard Welcome Window

![](numi-server-setup-guide/018.png)

4.  Click the "I accept the terms in the license agreement" checkbox, as illustrated in Figure 17: MS WSE 3.0 License Agreement Window.
29. Click the \<Next\> button.

<span id="_Hlk166518101" class="anchor"></span>Figure 17: MS WSE 3.0 License Agreement Window

![](numi-server-setup-guide/019.png)

5.  Click the \<Administrator\> radio button, as illustrated in Figure 18: MS WSE 3.0 InstallShield Wizard Window.
30. Click the \<Next\> button.

<span id="_Hlk166518106" class="anchor"></span>Figure 18: MS WSE 3.0 InstallShield Wizard Window

![](numi-server-setup-guide/020.png)

6.  Click the \<Install\> button (shown in Figure 19: MS WSE 3.0 Installation Window).

<span id="_Hlk166518111" class="anchor"></span>Figure 19: MS WSE 3.0 Installation Window

![](numi-server-setup-guide/021.png)

7.  Click the \<Finish\> button (shown in Figure 20: MS WSE 3.0 Completion Window).

<span id="_Hlk166518115" class="anchor"></span>Figure 20: MS WSE 3.0 Completion Window

![](numi-server-setup-guide/022.png)

## Install SQL Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install the MS SQL Server 2019 Database Server software only on the database server, applying both MS installation instructions and local best practices.

Additional service packs or patches may be installed subsequent to application testing, and in accordance with local best practices.

All production NUMI databases should be run in Simple Recovery mode, to enable replication to function, and to maximize the recoverability of the databases. In non-production environments, any recovery mode is acceptable, and simple recovery mode is encouraged for development and QA testing environments due to ease of administration.

### Download all SQL Server Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Downloading all SQL Server Patches applies to the database server only.

### Restore the Appropriate Databases for the NUMI Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restoring the Appropriate Databases for the NUMI Application applies to the database server only.

Follow the instructions in section 4 Instructions for Installing Database Components.

## Installing NUMI Exchange on Server 2019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](numi-server-setup-guide/023.png) Before doing this, you must make a backup copy of the web.config file (if this is an upgrade). Settings may need to be extracted from this in the future.

### Unzip/Install NUMI Exchange Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Using Windows Explorer, create the NumiExchange folder on the D drive, if available; otherwise create on the C drive. E.g., D:\NumiExchange
31. Unzip the NUMI Exchange files into the NumiExchange folder created above.
32. Update the application settings in the NUMI Exchange web.config file, located in the directory created above. Typically, this would involve updating the database connection string.

### NUMI Exchange Website Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using IIS Manager, add a new website and select the Secure Socket Layer (SSL) certificate as shown in Figure 21: Add NUMI Exchange Website.

<span id="_Hlk166518136" class="anchor"></span>Figure 21: Add NUMI Exchange Website

![](numi-server-setup-guide/024.png)

<span id="_bookmark68" class="anchor"></span>Figure 22: NUMI Exchange Website

![](numi-server-setup-guide/025.png)

The NUMI website basic and advanced settings are shown in Figure 23: NUMI Exchange Basic Settings and Figure 24: NUMI Advanced Settings.

<span id="_Hlk166518144" class="anchor"></span>Figure 23: NUMI Exchange Basic Settings

![](numi-server-setup-guide/026.png)

<span id="_bookmark70" class="anchor"></span>Figure 24: NUMI Advanced Settings

![](numi-server-setup-guide/027.png)

The NUMI Exchange web site bindings are shown in Figure 25: NUMI Exchange Bindings.

<span id="_Hlk166518151" class="anchor"></span>Figure 25: NUMI Exchange Bindings

![](numi-server-setup-guide/028.png)

The NUMI Exchange web site authentication settings are shown in Figure 26: NUMI Exchange Authentication Settings.

<span id="_Hlk166518155" class="anchor"></span>Figure 26: NUMI Exchange Authentication Settings

![](numi-server-setup-guide/029.png)

The NUMI Exchange website SSL settings are shown in Figure 27: NUMI Exchange SSL Settings.

<span id="_Hlk166518160" class="anchor"></span>Figure 27: NUMI Exchange SSL Settings

![](numi-server-setup-guide/030.png)

#### Application Pool Configuration

The NUMI Exchange application pool setup is shown in Figure 28: Application Pool Window.

<span id="_Hlk166518165" class="anchor"></span>Figure 28: Application Pool Window

![](numi-server-setup-guide/031.png)

The NUMI Exchange application pool basic settings are shown in Figure 29: NUMI Exchange Application Pool Basic Settings.

<span id="_Hlk166518170" class="anchor"></span>Figure 29: NUMI Exchange Application Pool Basic Settings

![](numi-server-setup-guide/032.png)

The NUMI Exchange application pool advanced settings are shown in Figure 30: NUMI Exchange Pool Advanced Settings.

<span id="_Hlk166518175" class="anchor"></span>Figure 30: NUMI Exchange Pool Advanced Settings

![](numi-server-setup-guide/033.png)

![](numi-server-setup-guide/034.png)

![](numi-server-setup-guide/035.png)

## Installing NUMI on Server 2019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Copy Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Right click on the zip file, select the "Unblock" if active, and select O.K. Some security schemes will block certain files from being unpacked, typically the Java files under the "web" directory. Setting the file to Unblock eliminates this problem.

<span id="_Hlk166518180" class="anchor"></span>Figure 31: Unblocking Restricted Files in Installation ZIP File

![](numi-server-setup-guide/036.png)

It is recommended that NUMI be installed in the D:\NUMI folder. Using Windows Explorer, create a NUMI folder in D drive, if available, otherwise create in C drive. E.g., D:\NUMI.

Unzip the NumiWebApp folder from the NUMI distribution zip file into the D:\NUMI folder. Rename the NumiWebApp folder using the build name of the distribution zip file.

### NUMI Web Site Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using IIS Manager, add a new web site as shown in Figure 32: Add NUMI Website.

<span id="_Hlk166518188" class="anchor"></span>Figure 32: Add NUMI Website

![](numi-server-setup-guide/037.png)

The NUMI web site basic and advanced settings are shown in Figure 33: NUMI Basic Settings and Figure 34: NUMI Advanced Settings.

<span id="_Hlk166518194" class="anchor"></span>Figure 33: NUMI Basic Settings

![](numi-server-setup-guide/038.png)

<span id="_bookmark102" class="anchor"></span>

Figure 34: NUMI Advanced Settings

![](numi-server-setup-guide/039.png)

The NUMI web site bindings are shown in Figure 35: NUMI Bindings.

<span id="_Hlk166518202" class="anchor"></span>Figure 35: NUMI Bindings

![](numi-server-setup-guide/040.png)

The NUMI web site authentication settings are shown in Figure 36: NUMI Authentication Setting. Make sure Forms Authentication is the only one enabled.

<span id="_Hlk166518206" class="anchor"></span>Figure 36: NUMI Authentication Settings

![](numi-server-setup-guide/041.png)

The NUMI website SSL settings are shown in Figure 37: NUMI SSL Settings.

<span id="_Hlk166518211" class="anchor"></span>Figure 37: NUMI SSL Settings

![](numi-server-setup-guide/042.png)

The NUMI web site compression settings are shown in Figure 38: NUMI Compression Settings.

<span id="_Hlk166518216" class="anchor"></span>Figure 38: NUMI Compression Settings

![](numi-server-setup-guide/043.png)

### Application Pool Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI application pool setup is shown in Figure 39: Application Pool Window.

<span id="_Hlk166518222" class="anchor"></span>Figure 39: Application Pool Window

![](numi-server-setup-guide/044.png)

The NUMI application pool basic settings are shown in Figure 40: NUMI Application Pool Basic Settings.

<span id="_Hlk166518227" class="anchor"></span>Figure 40: NUMI Application Pool Basic Settings

![](numi-server-setup-guide/045.png)

The NUMI application pool advanced settings are shown in Error! Not a valid bookmark self-reference..

<span id="_Ref188530969" class="anchor"></span>Figure 41: NUMI Application Pool Advanced Settings

![](numi-server-setup-guide/046.png)

## Microsoft EntraId Application Registration for the Web Server Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Microsoft EntraId is the network based authentication method and pattern used by NUMI. Users must be authenticated with Microsoft EntraId to use NUMI. There are several key configurations from the EntraId Application Registration that need to be in the NUMI Web Server Configuration

### Microsoft EntraId Application Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each NUMI environment has its own Application Registration. The key values needed are ClientId, TenantId, ClientSecret, and RedirectUri.

The values can be found on the EntraId portal in these sections: REDACTED

<span id="_Toc225235876" class="anchor"></span>Figure 42: Microsoft EntraId Application Registration

![](numi-server-setup-guide/047.png)

<span id="_Toc225235877" class="anchor"></span>Figure 43: Application Registration Client Secret

![](numi-server-setup-guide/048.png)

<span id="_Toc225235878" class="anchor"></span>Figure 44: EntraId Application Registration Redirect URIs

![](numi-server-setup-guide/049.png)

The values are then added to the NUMI Web App Config.

\

33. Navigate to the CERMe install image and double click the install.htm file in the root directory to open the setup welcome page. This will open the CERMe install page in EDGE Browser.
34. Click on the Install Review Manager 21.0.1 / InterQual View 2022 link on the installation page. This will prompt to save or run the file, select Run. This will start the CERMe Install wizard.
35. Accept the license agreement and click Next.
36. On the License Information screen, enter the license information given above and click Next.
37. On the Select Review Manager Enterprise screen, select "Review Manager Enterprise" and click Next.
38. On the Installation Type screen, select "New Installation" and click Next.
39. Select an installation directory.
40. On the Choose Components screen, keep the default selection (i.e., all selected) and click Next.
41. On the Database Information page, enter the following info and click Next.
- Database type: SQL Server
- Server Name: Name of the SQL database server
- Database: Name of the database to which the dump restored in step 1
- Port Number: SQL Server
- Instance: leave blank
- User ID: SQL Server user ID with access to the CERMe database restored above
- Password: Password for the SQL Server user used above
42. On separate database to store report data screen, select No and click Next.
43. On the Install Jetty window, select Yes to install Jetty.
44. On the next screen, enter 8357 for Port Number.
45. On the next screen, select the hardware architecture.
46. Review the selections, and click Install to start the installation.
47. Once the installation completes, go to the URL: http://\<servername\>:8357/rm/login.

    This is should open the CERMe login page.
48. Now follow the steps below to update CERMe to CERMe 21.0.1.
49. Stop the CERMe Service from the Windows Services.
50. Create a backup of the CERMe Installation folder and the CERMe database.
51. Make the changes to the file (below)on the CERMe Jetty Server:

#### File: \<CERMe Install Folder\>\Jetty\etc\webdefault.xml

Add the following element to \<session-config\> element.

\<cookie-config\>

\<http-only\>true\</http-only\>

\</cookie-config\>

Session Config element should look like the following after the change:

\<session-config\>

\<session-timeout\>30\</session-timeout\>

\<cookie-config\>\<http-only\>true\</http-only\>\</cookie-config\>

\</session-config\>

#### File: \<CERMe Install Folder?\Jetty\etc\jetty-rewrite.xml

Add the following \<Call\> element to the end of the \<New\> element.

\<Call name="addRule"\>

\<Arg\>

\<New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"\>

\<Set name="pattern"\>/\*\</Set\>

\<Set name="name"\>Strict-Transport-Security\</Set\>

\<Set name="value"\>max-age=31536000; includeSubDomains\</Set\>

\</New\>

\</Arg\>

\</Call\>

The file will look like the following after the change:

\<Set name="handler"\>

\<New id="Rewrite" class="org.eclipse.jetty.rewrite.handler.RewriteHandler"\>

\<Set name="handler"\>\<Ref refid="oldhandler"/\>\</Set\>

\<Set name="rewriteRequestURI"\>\<Property name="rewrite.rewriteRequestURI" default="true"/\>\</Set\>

\<Set name="rewritePathInfo"\>\<Property name="rewrite.rewritePathInfo" default="false"/\>\</Set\>

\<Set name="originalPathAttribute"\>\<Property name="rewrite.originalPathAttribute" default="requestedPath"/\>\</Set\>

\<Call name="addRule"\>\<Arg\>\<New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"\>\<Set name="pattern"\>/\*\</Set\>\<Set name="name"\>Strict-Transport-Security\</Set\>\<Set name="value"\>max-age=31536000; includeSubDomains\</Set\>\</New\>\</Arg\>\</Call\>

\</New\>

\</Set\>

#### File: \<CERMe Install Folder\>\Jetty\start.ini

Add the following new section to the bottom of the file:

\# ===========================================================

\# Enforce Strict Transport Security

\# -----------------------------------------------------------

OPTIONS=rewrite

etc/jetty-rewrite.xml

#### File: \<CERMe Install Folder\>\Jetty\ReviewManager.xml

Add the content below to the end of the \< Config \> element

\<IntegratedLogin Enabled="true" CookieName="unifiedkey" UnifiedKey="8rzVNfLwjHWHvPctaen9dw=="

AuthenticationFailUrl="/iqm/html/rm_integrated_authentication_failed.htm" GuidUserCid="IQ_1" Guid="A1B0B165-3C18-4561-935F-5FB81BD42128"

AuthenticateWS="false"/\>

The modified file will look like the following:

\<Path Prefix="/rm"/\>

\<Login Check="true"/\>

\<IntegratedLogin Enabled="true" CookieName="unifiedkey" UnifiedKey="8rzVNfLwjHWHvPctaen9dw==" AuthenticationFailUrl="/iqm/html/rm_integrated_authentication_failed.htm" GuidUserCid="IQ_1" Guid="A1B0B165-3C18-4561-935F-5FB81BD42128" AuthenticateWS="false"/\>

\</Config\>

\</ReviewManager\>

52. Start CERMe Service from the Windows Services.
53. Go to CERMe URL: http://\<server\>:8357/rm/login Login with the credential provided, and go to the menu Help \> About. It should show Version InterQual Review Manager™ 21.0.1 (Build 4).
54. This completes the installation of the CERMe RM 21.0.1 InterQual View 2022.

### Install CERMe SSL Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI will need SSL certificates for CERMe (for Jetty). NUMI uses the SSL certificate for the server that CERMe is running on. If the sever does not have a SSL certificate installed, follow the normal VA processes for obtaining SSL Certificates and install it.

1.  Use IIS Manager to export the current certificate to a .pfx file. Select the server name in the Connections pane and double click on the Server Certificates in the IIS pane as shown in Figure 45.

<span id="_Hlk166518546" class="anchor"></span>Figure 45: IIS Server Certificates

![](numi-server-setup-guide/064.png)

55. Select the certificate to export and click on the "Export…" link in the Actions pane, as shown in Figure 46.

<span id="_Hlk166518551" class="anchor"></span>Figure 46: IIS Server Certificate Selection

![](numi-server-setup-guide/065.png)

56. Set the name of the .pfx file. Set the password, e.g., use numi (all lowercase) for the password, as shown in Figure 47. This password will be used in subsequent steps.

<span id="_Hlk166518555" class="anchor"></span>Figure 47: IIS Certificate Details

![](numi-server-setup-guide/066.png)

> **NOTE:** For the following, the password can be whatever you choose, but please make a note of them, as they will be used later. For this example, D:\Certs\NUMI.pfx is the file name and the password, the one that you used to export the .pfx file, e.g., numi (all lowercase).

57. Open a command prompt window and change the current directory to the location of the keytool executable. In this example it would be:

D:\Program Files (x86)\Change Healthcare\CERME\Jre\bin\keytool.exe

58. Execute the following command:

keytool -importkeystore -srcstoretype PKCS12 -srckeystore "D:\Certs\NUMI.pfx" -destkeystore "D:\Certs\CERME.ks"

> **NOTE:** -srckeystore value will be the .pfx path and filename above, -destkeystore can be whatever you choose; again, passwords can be whatever you choose, but please make a note of them. The word "secret" is used as the keystore password in this example.

59. Execute the following command:

Keytool –list -keystore "D:\Certs\CERME.ks"

Make a note of the long, auto-generated alphanumeric value circled in red below. Recommended actions are to copy, paste the entire command prompt output to notepad to copy, and paste this value.

<span id="_Hlk166518566" class="anchor"></span>Figure 48: keytool -keystore "C:\Certs\CERME.ks" –list

![](numi-server-setup-guide/067.png)

60. Execute the following command:

keytool -changealias -keystore "D:\Certs\CERME.ks" -destalias numi –alias \<alphanumeric value\>

> **NOTE:** Replace \<alphanumeric value\> with the value noted and circled from the step above. The keystore password is the password specified when creating the keystore above, secret in our example. The key password is the password specified when creating the pfx file, numi in our example.

61. Execute the following command:

keytool -keypasswd -keystore "D:\Certs\CERME.ks" -alias numi

> **NOTE:** With this command, we are changing the key password to "reallysecret" for this example.

62. Next, copy the keystore, (D:\Certs\CERME.ks), to the Jetty\etc directory. For this example, it would be here: D:\Program Files (x86)\Change Healthcare\CERME\Jetty\etc.
63. Modify \<Jetty-home\>\start.ini. Uncomment the relevant lines in the SSL Context and HTTPS Connector sections of start.ini file (as shown in the example below).

\#=========================================================

\# SSL Context

\# Create the keystore and trust store for use by

\# HTTPS and SPDY

\#-------------------------------------------------------------------

jetty.keystore=etc/keystore

jetty.keystore.password=(your password)

jetty.keymanager.password=(your password)

jetty.truststore=etc/keystore

jetty.truststore.password=(your password)

jetty.secure.port=(your SSL port number)

etc/jetty-ssl.xml

\#===========================================================

\# HTTPS Connector

\# Must be used with jetty-ssl.xml

\#-----------------------------------------------------------

jetty.https.port=(your SSL port number)

etc/jetty-https.xml

64. Open the windows services management console, (START-\>RUN-\>services.msc-\>OK), and restart the CERMe service. It will take about 20 to 30 seconds for the service to restart completely but you should be able to browse directly to the secure CERMe. Use whatever URL is used to access NUMI, e.g., REDACTED
65. Replace the "/web/home.aspx" portion with CERMe' s secure port, (8443 by default), e.g REDACTED

The CERMe website should be displayed and you should not have been warned of the security certificate problem.

## Setting up NUMI Section in the Windows Event Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Change Directory - Go to command prompt (run as Administrator) and change current directory to Framework v2.0 bit folder e.g., C:\WINDOWS\MS.NET\Framework\v4.5.x
66. Install Command - Type InstallUtil.exe /I \< source folder full path \>\bin\NumiWebApp.dll under Framework v4.5 folder and press enter.

e.g., InstallUtil.exe /i D:\NUMI\\install_dir\>\bin\NumiWebApp.dll

67. This should create a NUMI section in the Windows Event log.

<span id="_Hlk166518603" class="anchor"></span>Figure 49: Creating a NUMI section in the Windows Event Log

![](numi-server-setup-guide/068.png)

68. NUMI Event Folder Properties
    1.  Go to NUMI Properties by right mouse.
    2.  Click on General Tab under NUMI Properties dialog box window. Check/Click on Overwrite events as needed.
    3.  Press \<Apply\> button (if needed) and Press \<OK\> button.
    4.  Verify Event View, if any error logs occurred during the installation.

### Validate XML Configuration File Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that all XML configuration file settings are correct. Validate NUMI XML Configuration File Settings.

1.  Edit the application settings in the web.config file in the NUMI folder. E.g., D:\NUMI\\install_dir\>\web.config

Settings to update:

\

71. Click the Command Prompt (or \<Run\>, depending on the Operating System)
72. Type: IISReset
73. Click \<Enter\>.

## Test NUMI Web Site Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open Internet Explorer and type REDACTED e.g., REDACTED

## Installing NUMI Synchronizer on the Web Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a new installation:

1.  Open CMD in Administrator mode
2.  Enter 'cd C:\Windows\Microsoft.NET\Framework\v4.0.30319'
3.  Enter 'InstallUtil.exe D:\NUMI\Synchronizer\Synchronizer2.exe'
4.  View the NUMI Synchronizer service on services.msc
5.  Close the CMD prompt
6.  Verify/Update the Synchronizer2.exe.config data

> \<!-- Service configuration --\>

> \<!-- VistA Service configuration --\>

> \<add key="ServiceURL" value=" REDACTED

> \<add key="RequestingApp" value="NUMI_SYNC"/\>

> \<add key="IsSynchronizer" value="true"/\>

> \<add key="WSDLusername" value="vwsl_numi"/\>

> \<add key="WSDLpassword" value="\<PW\>"/\>

> \<!--STS Configuration--\>

> \<add key="STSEndpoint" value=" REDACTED

> \<add key="STSEnabled" value="true"/\>

> \<add key="STSCertificatePath" value="D:\\NUMI\Synchronizer\numisyncsqa.pfx"/\>

> \<add key="STSCertificatePassword" value="\<PW\>"/\>

> \<!--Database Connections--\>

> \<add key="numiDbConnectionString" value="Data Source=VAAUSSQLNUM###.aac.dva.va.gov;Database=NUMI;User ID=numi_user;Password=\<PW\>;Trusted_Connection=False" /\>

> \<add key="reportDbConnectionString" value="Data Source=VAAUSSQLNUM###.aac.dva.va.gov;Database=NUMI;User ID=numi_user;Password=\<PW\>;Trusted_Connection=False" /\>

7.  Start the service from services.msc

> ![](numi-server-setup-guide/070.png)

> For an upgrade in place:

1.  Stop the existing service from services.msc

> ![](numi-server-setup-guide/071.png)

2.  Copy the Sychronizer distribution folder/files to the intended environment in the NUMI directory. This folder will be provided by Tier 3 maintenance and should be stored on each environment

> ![](numi-server-setup-guide/072.png)

3.  Start the service from services.msc

> ![](numi-server-setup-guide/073.png)

### Uninstall:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to uninstall the NUMI Synchronizer services use services.msc and right click on the synchronizer to stop it. Then right click the Synchronizer and go to properties and disable it. Then open CMD in Admin mode and enter 'sc delete "NUMI Synchronizer"'.

### Validate Installation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To confirm the synchronizer installation

Open MS SQL Server Management Studio after 2 hours. Open a new query and type:

Use numi go.

Select TOP 1000 \* from patientstay.

Click the \<Execute\> button to run the query. New records shall display.

### Add Jobs to the SQL Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 3 jobs that must be added to the SQL Server:

1.  NUMI_PhysicianAdvisorPatientReview_AutoExpire
2.  LogSynchDB_ValidateSynchronizer
3.  NUMI_AlterIndex_Rebuild

These jobs can be installed from scripts (included in the build) or, if you are transferring from another server, you can right click on each job and script as DROP and CREATE.

Backup the jobs before you run the scripts. Modify the scripts to replace the @owner_login_name with the owner login name appropriate for your installation, if necessary.

NUMI_PhysicianAdvisorPatientReview_AutoExpire is a job that executes the Stored Procedure usp_PhysicianAdvisorPatientReview_AutoExpire every day at midnight. The Stored Procedure looks for Physician UM Advisor (PUMA) Reviews that have not been completed within 14 days and marks them as Completed with a reason description of Expired.

LogSynchDB_ValidateSynchronizer is job that executed the stored procedure LogSyncDB.dbo.usp_LogSync_ValidateSynchronizer every hour. This stored procedure confirms imported stays within the last 3 hours and reports the problem to a pre-defined e- mail distribution list determined by the needs of the installation.

NUMI_AlterIndex_Rebuild is a job that executes the stored procedure NUMI.dbo.usp_AlterIndex_Rebuild. This stored procedure rebuilds the indexes for the tables in the NUMI database.

## Post-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are post-installation considerations for NUMI, this information will be provided by the appropriate project teams.

## Acronyms and Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym |     | Description                                          |     |
|---------|-----|------------------------------------------------------|-----|
| CERMe   |     | Care Enhance Review Management Enterprise            |     |
| CPRS    |     | Computerized Patient Record System                   |     |
| CPU     |     | Central Processing Unit                              |     |
| HTTP    |     | HyperText Transfer Protocol                          |     |
| HTTPS   |     | HyperText Transfer Protocol Secure                   |     |
| IAM     |     | Identity and Access Management                       |     |
| IIS     |     | Internet Information Services                        |     |
| MDWS    |     | Medical Domain Web Services                          |     |
| NUMI    |     | National Utilization Management Integration          |     |
| PM      |     | Project Manager                                      |     |
| PUMA    |     | Physician UM Advisor                                 |     |
| QA      |     | Quality Assurance                                    |     |
| SQL     |     | Standard Query Language                              |     |
| SSL     |     | Secure Socket Layer                                  |     |
| SSO     |     | Single Sign On                                       |     |
| UM      |     | Utilization Management                               |     |
| URL     |     | Uniform Resource Locator                             |     |
| VIA     |     | VistA Integration Adaptor                            |     |
| VistA   |     | Veterans Information Systems Technology Architecture |     |

## NUMI Comparison Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| NUMI Version | CERMe RM | InterQual View | Windows Server | MS SQL Server |
|--------------|----------|----------------|----------------|---------------|
| 15.4         | 16.1     | 2017.2         | 2012 R2        | 2012          |
| 15.5         | 17       | 2018.1         | 2012 R2        | 2012          |
| 15.6         | 17       | 2018.1         | 2012 R2        | 2012          |
| 15.8         | 18.1     | 2019.1         | 2012 R2        | 2012          |
| 15.9         | 19.0     | 2020           | 2012 R2        | 2012          |
| 15.9.1       | 20.0     | 2021           | 2019           | 2019          |
| 15.10        | 21.0.1   | 2022           | 2019           | 2019          |
| 15.11        | 21.0.1   | 2022           | 2019           | 2019          |
| 15.14        | 21.0.1   | 2022           | 2019           | 2019          |
| 15.15        | 22.0     | 2024           | 2019           | 2019          |
| 15.16        | 22.0     | 2024           | 2019           | 2019          |
| 15.17        | 22.0     | 2025           | 2019           | 2019          |
