---
title: EN Version 7 RTLS Enhancement Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: RTLS Enhancement
app_code: EN
app_name: Engineering (AEMS / MERS)
section: FIN
app_status: active
pkg_ns: EN
patch_ver: 7
patch_id: EN*7
group_key: "EN:EN:7"
file_numbers: []
security_keys: []
menu_options: 0
description: > The Installation, Back-Out, Rollback Guide defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product. It provides installation instructions for the Asset Tracking interfa
audience: 
keywords: 
  - table
  - contents
  - rtls
  - installation
  - application
  - back
  - class
  - mule
  - vista
  - configuration
page_count: 0
word_count: 5653
section_count: 32
table_count: 9
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/rtls_at_patch_installation_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/rtls_at_patch_installation_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=37"
---

> Real Time Location System (RTLS) Enterprise Systems Engineering (ESE) Asset Tracking Interface

# Installation, Back-Out, and Rollback Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Installation, Back-Out, and Rollback Guide](#installation-back-out-and-rollback-guide)
    - [November 2017 Department of Veterans Affairs](#november-2017-department-of-veterans-affairs)
- [Introduction](#introduction)
  - [Overview](#overview)
    - [RTLS VistA Patch (KIDS Build)](#rtls-vista-patch-kids-build)
    - [WebLogic VistaService Web Services](#weblogic-vistaservice-web-services)
    - [RTLS Mule ESB Domain Component](#rtls-mule-esb-domain-component)
    - [RTLS Mule ESB Application Component](#rtls-mule-esb-application-component)
    - [RTLS-VistA Interface Configuration Tool](#rtls-vista-interface-configuration-tool)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [References](#references)
- [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
    - [Non-VistA Required Software](#non-vista-required-software)
    - [Installation Sequencing Information](#installation-sequencing-information)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Environmental Variables](#environmental-variables)
  - [VistaService Web Services Pre-Installation](#vistaservice-web-services-pre-installation)
    - [Setup Security](#setup-security)
    - [Create WebLogic User Config Files for VistaServices](#create-weblogic-user-config-files-for-vistaservices)
    - [Create a Certificate for the Intelligent InSites Connector Server](#create-a-certificate-for-the-intelligent-insites-connector-server)
  - [RTLS ESB Application Component Pre-Installation](#rtls-esb-application-component-pre-installation)
    - [Setup Security](#setup-security-1)
    - [Create Application Directories](#create-application-directories)
    - [Configure Mule ESB Enterprise Edition for RTLS](#configure-mule-esb-enterprise-edition-for-rtls)
- [Installation Procedure](#installation-procedure)
  - [VistaService Web Services Installation](#vistaservice-web-services-installation)
    - [Add WebLogic ID to the Vistasvcs Group](#add-weblogic-id-to-the-vistasvcs-group)
    - [Create Application Directories](#create-application-directories-1)
    - [Copy install Files and Extract](#copy-install-files-and-extract)
    - [Configure HEVCONFIG/log4j.xml File](#configure-hevconfiglog4jxml-file)
    - [Modify VistA Configuration Files](#modify-vista-configuration-files)
    - [Deploy VistaLinkConsole and Other Applications](#deploy-vistalinkconsole-and-other-applications)
    - [Setup and Configure Security](#setup-and-configure-security)
  - [RTLS-VistA Interface Configuration Tool Installation](#rtls-vista-interface-configuration-tool-installation)
    - [Create SQL Server Database](#create-sql-server-database)
    - [Define SQL Server Data Sources](#define-sql-server-data-sources)
    - [Deploy the RTLS-VistA Interface Configuration Tool](#deploy-the-rtls-vista-interface-configuration-tool)
    - [Configure RTLS-VistA Interface Configuration Tool](#configure-rtls-vista-interface-configuration-tool)
  - [RTLS ESB Component Installation](#rtls-esb-component-installation)
    - [Initial Installation](#initial-installation)
    - [Deploy the RtlsDomain ESB Domain Component](#deploy-the-rtlsdomain-esb-domain-component)
    - [Populate the Asset Tracking Property File](#populate-the-asset-tracking-property-file)
    - [Start and Verify the Mule ESB Application](#start-and-verify-the-mule-esb-application)
    - [Subsequent Installation](#subsequent-installation)
- [Implementation Procedure](#implementation-procedure)
  - [System Configuration](#system-configuration)
    - [Configuring SSL/TLS](#configuring-ssltls)
    - [Configuring Site Information](#configuring-site-information)
    - [Creating Location External References in InSites](#creating-location-external-references-in-insites)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
    - [VistaService Web Services Back-Out](#vistaservice-web-services-back-out)
    - [RtlsInterfaceAdmin Application Back-Out](#rtlsinterfaceadmin-application-back-out)
    - [RTLS ESB Application Component Back-out/Uninstall](#rtls-esb-application-component-back-outuninstall)
    - [RTLS ESB Application Component Back-out/Uninstall](#rtls-esb-application-component-back-outuninstall-1)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
- [Appendix A: Troubleshooting](#appendix-a-troubleshooting)
  - [Run the Deployment Health Check](#run-the-deployment-health-check)
  - [Check the Log Files](#check-the-log-files)
    - [Template Revision History](#template-revision-history)
![](en-version-7-rtls-enhancement-installation-guide/001.png)

### November 2017 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)
1.  [Introduction 1](#introduction)
    1.  [Overview 1](#overview)
        1.  [RTLS VistA Patch (KIDS Build) 1](#rtls-vista-patch-kids-build)
        2.  [WebLogic VistaService Web Services 2](#weblogic-vistaservice-web-services)
        3.  [RTLS Mule ESB Domain Component 2](#rtls-mule-esb-domain-component)
        4.  [RTLS Mule ESB Application Component 2](#rtls-mule-esb-application-component)
        5.  [RTLS-VistA Interface Configuration Tool 3](#rtls-vista-interface-configuration-tool)
2.  [Pre-installation and System Requirements 5](#pre-installation-and-system-requirements)
    1.  [Platform Installation and Preparation 5](#platform-installation-and-preparation)
        1.  [Non-VistA Required Software 5](#non-vista-required-software)
        2.  [Installation Sequencing Information 5](#installation-sequencing-information)
    2.  [Download and Extract Files 6](#download-and-extract-files)
    3.  [Database Creation 6](#database-creation)
    4.  [Installation Scripts 6](#installation-scripts)
    5.  [Cron Scripts 6](#cron-scripts)
    6.  [Access Requirements and Skills Needed for the Installation 6](#access-requirements-and-skills-needed-for-the-installation)
    7.  [Environmental Variables 7](#environmental-variables)
    8.  [VistaService Web Services Pre-Installation 7](#vistaservice-web-services-pre-installation)
        1.  [Setup Security 7](#setup-security)
        2.  [Create WebLogic User Config Files for VistaServices 8](#create-weblogic-user-config-files-for-vistaservices)
        3.  [Create a Certificate for the Intelligent InSites Connector Server 8](#create-a-certificate-for-the-intelligent-insites-connector-server)
    9.  [RTLS ESB Application Component Pre-Installation 9](#rtls-esb-application-component-pre-installation)
        1.  [Setup Security 9](#setup-security-1)
        2.  [Create Application Directories 10](#create-application-directories)
        3.  [Configure Mule ESB Enterprise Edition for RTLS 10](#configure-mule-esb-enterprise-edition-for-rtls)
            1.  [Add Java Properties 10](#add-java-properties)
            2.  [Modify Existing Java Properties 10](#modify-existing-java-properties)
3.  [Installation Procedure 11](#installation-procedure)
    1.  [VistaService Web Services Installation 11](#vistaservice-web-services-installation)
        1.  [Add WebLogic ID to the Vistasvcs Group 11](#add-weblogic-id-to-the-vistasvcs-group)
        2.  [Create Application Directories 11](#create-application-directories-1)
        3.  [Copy install Files and Extract 11](#copy-install-files-and-extract)
        4.  [Configure HEV_CONFIG/log4j.xml File 12](#configure-hev_configlog4j.xml-file)
        5.  [Modify VistA Configuration Files 12](#modify-vista-configuration-files)
        6.  [Deploy VistaLinkConsole and Other Applications 13](#deploy-vistalinkconsole-and-other-applications)
        7.  [Setup and Configure Security 13](#setup-and-configure-security)
    2.  [RTLS-VistA Interface Configuration Tool Installation 13](#rtls-vista-interface-configuration-tool-installation)
        1.  [Create SQL Server Database 13](#create-sql-server-database)
        2.  [Define SQL Server Data Sources 14](#define-sql-server-data-sources)
        3.  [Deploy the RTLS-VistA Interface Configuration Tool 15](#deploy-the-rtls-vista-interface-configuration-tool)
        4.  [Configure RTLS-VistA Interface Configuration Tool 15](#configure-rtls-vista-interface-configuration-tool)
    3.  [RTLS ESB Component Installation 15](#rtls-esb-component-installation)
        1.  [Initial Installation 15](#initial-installation)
        2.  [Populate the RtlsDomain Property File 16](#3.3.2._Populate_the_RtlsDomain_Property_)
        3.  [Deploy the RtlsDomain ESB Domain Component 16](#deploy-the-rtlsdomain-esb-domain-component)
        4.  [Populate the Asset Tracking Property File 16](#populate-the-asset-tracking-property-file)
        5.  [Start and Verify the Mule ESB Application 19](#start-and-verify-the-mule-esb-application)
        6.  [Subsequent Installation 19](#subsequent-installation)
4.  [Implementation Procedure 20](#implementation-procedure)
    1.  [System Configuration 20](#system-configuration)
        1.  [Configuring SSL/TLS 20](#configuring-ssltls)
        2.  [Configuring Site Information 20](#configuring-site-information)
        3.  [Creating Location External References in InSites 21](#creating-location-external-references-in-insites)
    2.  [Database Tuning 22](#database-tuning)
5.  [Back-Out Procedure 23](#back-out-procedure)
    1.  [Back-Out Strategy 23](#back-out-strategy)
    2.  [Back-Out Considerations 23](#back-out-considerations)
        1.  [Load Testing 23](#load-testing)
        2.  [User Acceptance Testing 23](#user-acceptance-testing)
    3.  [Back-Out Criteria 23](#back-out-criteria)
    4.  [Back-Out Risks 23](#back-out-risks)
    5.  [Authority for Back-Out 23](#authority-for-back-out)
    6.  [Back-Out Procedure 24](#back-out-procedure-1)
        1.  [VistaService Web Services Back-Out 24](#vistaservice-web-services-back-out)
        2.  [RtlsInterfaceAdmin Application Back-Out 24](#rtlsinterfaceadmin-application-back-out)
        3.  [RTLS ESB Application Component Back-out/Uninstall 24](#rtls-esb-application-component-back-outuninstall)
        4.  [RTLS ESB Application Component Back-out/Uninstall 25](#rtls-esb-application-component-back-outuninstall-1)
6.  [Rollback Procedure 26](#rollback-procedure)
    1.  [Rollback Considerations 26](#rollback-considerations)
    2.  [Rollback Criteria 26](#rollback-criteria)
    3.  [Rollback Risks 26](#rollback-risks)
    4.  [Authority for Rollback 26](#authority-for-rollback)
    5.  [Rollback Procedure 26](#rollback-procedure-1)
7.  [Appendix A: Troubleshooting 27](#appendix-a-troubleshooting)
    1.  [Run the Deployment Health Check 27](#run-the-deployment-health-check)
    2.  [Check the Log Files 27](#check-the-log-files)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Installation, Back-Out, Rollback Guide defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product. It provides installation instructions for the Asset Tracking interface as managed through the Real Time Location System (RTLS) project.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This installation guide covers the installation and configuration of the RTLS Asset Tracking (AT) interface application. The AT interface application synchronizes AEMS-MERS equipment details and locations with Intelligent InSites RTLS.

> The environment needed to run the applications is multi-server and includes the following distinct deployment components:

- RTLS VistA Patch (KIDS build)
- WebLogic VistaService Web Services
- RTLS Mule ESB domain component
- RTLS Mule ESB application component
- RTLS-VistA Interface Configuration Tool

> Deployment and configuration of any of these components has dependencies on at least one of the others (i.e. the Mule ESB application is dependent on VistaService Web Services; VistaService is dependent on the VistA patch).

> The following sections provide descriptions of the deployment components.

### RTLS VistA Patch (KIDS Build)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS patches and a companion patch for the Engineering package (VIAA\*1\*1, VIAA\*1\*3 and EN\*7\*100) support the implementation of the project and are distributed in a Kernel Installation and Distribution System (KIDS) build. Multiple Remote Procedure Calls (RPCs) are used to support the user interfaces with the packages touched by this project.

> The RTLS patch is exporting a new option, ‘Make Web Call to Mule’ \[VIAA MAKE WEB CALL TO MULE\], to send Engineering file changes (MUMPS Style Cross Reference events) to the RTLS database via a Mule server. This option is a queue process that checks every number of minutes, configured by the site, to see if there are any record changes from files EQUIPMENT INV (#6914) and ENG SPACE file (#6928) to transmit to RTLS.

> A new file, PENDING RTLS EVENTS (#6930), is also exported by the patch. The PENDING RTLS EVENTS file holds record changes before transmission to RTLS and when the Mule server is off-line. When the Mule server comes back online, the next run of the queue transmits every record and the file is cleaned up immediately. While the file may be populated with record changes at any time, its use is limited to very shorts periods of time and will not require disk space at the local site. The PENDING RTLS EVENTS file introduces a redundancy to save record changes that could not be sent to the RTLS database when the Mule server is offline for any reason.

> Data dictionary changes to the EQUIPMENT INV file (#6914) and the ENG SPACE file (#6928) are exported by the Engineering patch.

> The following options in the Engineering package generate events after record changes have been completed by users of the package. Multiple fields in the EQUIPMENT INV file (#6914) and the ENG SPACE file (#6928) will be equipped with MUMPS cross references to monitor data changes.

- New Inventory Entry \[ENINVNEW\]
- Multiple Inventory Entry \[ENIN-ENTER-MULTI\]
- Inventory Edit \[ENINV EDIT\]
- Enter New Room Space Data \[ENSPROOM\]
- Display/Edit Room Data \[ENSPROOMD\]

> Additionally, any changes completed via the Enter/Edit option of VA FileMan for any of the fields monitored will create an event that will be sent to RTLS.

> For more information and instructions on how to install the VistA patches, see the RTLS AT Patch Installation Guide.

### WebLogic VistaService Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Communication with VistA is managed with a series of RESTful web service methods designed for the RTLS solution called VistaService. VistaService is an interface to VistA creating a uniform calling method for underlying MUMPS RPCs. The RESTful web service methods provide a mechanism to encapsulate the VistALink calls into a standard format. This improves code maintainability, de-couples the service from the interface so multiple interfaces can use it, and provides for future scalability of the interface.

> VistaService has methods for creating, retrieving, and updating VistA data over HTTP using RESTful semantics. RESTful methods are called using a URL.

### RTLS Mule ESB Domain Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Part of the RTLS solution includes an open source Enterprise Service Bus (ESB) called Mule ESB. Mule ESB is a Java-based ESB and integration platform to facilitate message routing and data transformation.

> The RTLS Domain component provides a central configuration for all domain applications to share common resources, such as the HTTP listening port. It must be installed before any domain applications are installed which reference the shared resources.

### RTLS Mule ESB Application Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS AT interface application is orchestrated by a series of ESB flows. A Mule ESB flow is a way to manage or orchestrate services. Flows provide a flexible method to build integrations by choosing building blocks from a standard list of defined components. By separating configuration information from the underlying code using building blocks, building, deploying and maintaining the interface is easier to manage.

> Within the ESB flows, RESTful web services are employed on both ends to facilitate communication between RTLS (i.e., Intelligent InSites) and VistA. Communication with VistA is managed by the VistaService Web Service methods.

### RTLS-VistA Interface Configuration Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS-VistA Interface Configuration Tool is a software utility used to configure the schedule of the AEMS-MERS/RTLS interface. The tool is designed for administrative users of RTLS to have a single location to view and manage network connections and associated jobs within the VISN. The tool is a web application hosted on the interface WebLogic server and is displayed as a Snap-in screen on the Intelligent InSites user interface.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this guide is to provide VA facility Information Resource Management Systems (IRMS) personnel, and the VistA Laboratory Information Manager (LIM) with the necessary technical information required to understand the installation and implementation of the RTLS AT interface application. This guide provides instructions for installing and configuring the following components of the applications:

- WebLogic VistaService Web Services
- RTLS Mule ESB domain component
- RTLS Mule ESB application component
- RTLS-VistA Interface Configuration Tool

> The installation of the VistA patches is covered in the RTLS AT Patch Installation Guide.

> The RTLS AT interface application is a distributed solution with multiple components each with its own deployment. Due to the complexity of the components and operating environment, as well as software release changes and local VA environment protocols, each installation may be different. Because of these differences, individual installations may vary from the instructions provided in this guide. Where possible, every effort has been made to explain the purpose of steps to aid in understanding.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The scope of this guide is limited to the technical steps required to install, configure, and implement the non-VistA components of the RTLS AT interface application. This includes:

- Installation and configuration of the VistaService Web Services
- Installation and configuration of the RTLS ESB Application Component
- Installation and configuration of the RTLS-VistA Interface Configuration Tool This guide does not include:
- Installation and configuration of the WebLogic Domain or Mule Enterprise Edition
- Installation and configuration of Intelligent InSites

> Intelligent InSites is a Commercial off-the-shelf (COTS) product. Installation and configuration are managed by the vendor as part of the overall deployment plan.

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- RTLS AT Patch Installation Guide
- VistALink System Management Guide
- VistALink Developer Guide
- VistALink Installation Guide
- RTLS ESE Deployment Plan
- RTLS ESE Formal Test Results

# Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following points are important to note about the RTLS AT interface application installation covered in this guide and the companion guide, the RTLS AT Patch Installation Guide:

- The guides represents the instructions for installing the RTLS AT interface application in a test environment.
- Installation will always occur within a test environment before being approved for installation in production.
- The difference between a test and production installation is minimal.
- Users do not have to log off the system during installation.
- The average amount of time required to install the software is 4 hours.
- This software does not have to be installed during off-peak hours.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Non-VistA Required Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following list of software represents the minimum versions required for installation:

| Software Application              | Version                         |
|---------------------------------------|-------------------------------------|
| Mule Enterprise Edition               | 3.7.3                               |
| Oracle JRockit                        | R28.2.5-4.1.0 64 bit (for WebLogic) |
| Oracle WebLogic Enterprise Edition    | 10.3.6 64 bit                       |
| Red Hat Enterprise Linux (RHEL)       | 6.7                                 |
| Sun/Oracle Java Development Kit (JDK) | 1.8                                 |
| MMC Console                           | 3.4.3                               |
| Microsoft SQL Server                  | 2012                                |
| Intelligent InSites RTLS              | 4.7                                 |

### Installation Sequencing Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The installation must be performed in the following order:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step 1: RTLS AT VistA Patches</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Follow all instructions in the RTLS AT Patch Installation Guide</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Step 2: WebLogic VistaService Web Services</strong></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>VistaService Web Services Pre-Installation (section <a href="#vistaservice-web-services-pre-installation">2.8</a>)</p></li>
<li><p><a href="#vistaservice-web-services-installation">VistaService Web Services Installation</a> (section <a href="#vistaservice-web-services-installation">3.1</a>)</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step 3: RTLS-VistA Interface Configuration Tool</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p><a href="#rtls-vista-interface-configuration-tool-installation">RTLS-VistA Interface Configuration Tool Installation</a> (section <a href="#rtls-vista-interface-configuration-tool-installation">3.2</a>)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Step 4: RTLS ESB Component</strong>s</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>RTLS ESB Application Component Pre-Installation (section <a href="#rtls-esb-application-component-pre-installation">2.9</a>)</p></li>
<li><p>RTLS ESB Application Component Installation (section <a href="#rtls-esb-component-installation">3.3</a>)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Step 5: Configure SSL/TLS</strong></td>
</tr>
<tr class="odd">
<td><ul>
<li><p><a href="#configuring-ssltls">Configuring SSL/TLS</a> (section <a href="#configuring-ssltls">4.1.1</a>)</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HPE RTLS Administration Support Organization is responsible for installing the RTLS AT Interface Application. The software installation files are stored within the VA’s Rational Repository and described within the RTLS Version Description Document (VDD).

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RtlsInterfaceAdmin application runs on SQL Server. See sec[tion 3.2.1](#create-sql-server-database) for instructions on how to create the database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The installation scripts for the deployment of the RTLS AT application interface are interspersed throughout this guide.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS AT interface application is multi-server and includes distinct deployment components. The skills needed for the installation is varied by deployment components:

- Web Services and Mule ESB components - the audience is a system administrator with a strong working knowledge of Linux, distributed systems, Java Enterprise Edition (JEE), and virtual environments.
- Configuring SSL/TLS - the audience is a systems administrator with a strong working knowledge of both Linux systems administration and enterprise security.

> The installation of the RTLS AT Interface Application, with the exception of the RTLS VistA components, will be performed by the HPE RTLS Administration Support Organization along with representatives from peer VA organizations. The installation and configuration of all RTLS VistA components will be performed by VA personnel. Contact the HPE RTLS System Administration Support Team via email: [<u>vartlsadmins@hpe.com</u>.](mailto:vartlsadmins@hpe.com)

## Environmental Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table provides a list of environmental variables used throughout this guide. An environmental variable represents the name of a directory. Directory names can vary across installations. The variables provide a method of standardizing the install process.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Environmental Variable</strong></th>
<th><strong>Definition/Origin</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>{environment}</td>
<td>Used to enable stacking multiple WebLogic environments on a Virtual Machine (VM).</td>
</tr>
<tr class="even">
<td>{MW_HOME}</td>
<td><p>Directory for middleware home (eg</p>
<p>/data/Oracle/Middleware).</p></td>
</tr>
<tr class="odd">
<td>{WL_RTLS}</td>
<td><p>Directory for RTLS WebLogic script home (eg</p>
<p>/data/rtls/weblogic). This directory is typically outside of the Middleware directory structure.</p></td>
</tr>
<tr class="even">
<td>{APPROOT}</td>
<td>Directory for VistaServices (eg /data/rtls/vistasvcs) and the RTLS ESB application depending on the component being installed.</td>
</tr>
<tr class="odd">
<td>{domain_home}</td>
<td><p>Directory for WebLogic domain home (eg</p>
<p>{MW_HOME}/user_projects/domains/{environment}_domai n).</p></td>
</tr>
<tr class="even">
<td>{MULE_HOME}</td>
<td>Directory where Mule is installed.</td>
</tr>
</tbody>
</table>

## VistaService Web Services Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistaService is a WebLogic application. Pre-installation steps for the VistaService Web Services are the configuration tasks needed to establish the application within the WebLogic domain. The installation and configuration of the WebLogic domain is outside the scope of this document.

> To perform the configuration tasks needed to establish the VistaServices web services application within the WebLogic domain, complete all of the steps in the following sections.

### Setup Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create a new group and user as the application owner for VistaServices. For ease of maintenance, consider creating group IDs (GIDs) and user IDs (UIDs) consistent across environments. GID and UID synchronization is required if using Network File System (NFS). Your local systems administrator will provide guidance. The instructions below use 550 as an example only. Change this value as appropriate for your installation. Execute instructions as root.

> 1\. Create the VistaServices group and user: groupadd -g 550 vistasvcs

> useradd -g 550 -u 550 -c "Vista Services AppId" -d /home/vistasvcs -s /bin/bash vistasvcs

### Create WebLogic User Config Files for VistaServices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create WebLogic scripts for automatically configuring, starting, and stopping VistaServices by copying generic scripts shipped with WebLogic and modifying them.

1.  Copy the supplied WebLogic scripts to the designated scripts folder in your environment (i.e.

> {WL_RTLS}).

2.  Edit the start\_{environment}.py and change the following: Change base_cluster to vs_cluster

> Change base_server\_ to vs_server\_

3.  Edit the stop\_{environment}.py and make the same changes as step 2.
4.  Verify that the entry in wlst.sh script references the valid location of wlst.sh under the WebLogic install (i.e. {MW_HOME}/wlserver_10.3/common/bin/wlst.sh \$\*)
5.  Setup the userkey files for the id used to run the scripts (typically WebLogic):
    1.  Modify install\create_userkey.py with the environment_name to name the files ({environment}) and the WebLogic password that was specified when the domain was created.
    2.  From {WL_RTLS} directory, run wlst.sh install/create_userkey.py
    3.  Respond by entering y to the one prompt that displays.

> Note: It only prompts the first time a particular userconfig is created.

4.  Remove the password from create_userkey.py
6.  Add the WebLogic startup script command to system startup file: Startup file = /etc/rc.local

> Add:

> {WL_RTLS}/vm_startup_initd.sh

7.  Restart the server and verify WebLogic servers came up.

### Create a Certificate for the Intelligent InSites Connector Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are many different methods to create an SSL certificate request. The following generalized steps are provided as one example using Microsoft Management Console (MMC). Your installation may vary. The Microsoft Management Console (MMC) with the Certificates snap-in is used to view and manage SSL server certificates. Execute instructions as root on the server the certificate will be installed on:

1.  Start MMC and select Add/Remove Snap-in.
2.  Select Certificates. Select Add.
3.  When asked for the type of account, Select Computer Account and Local Computer.
4.  In the Personal Folder, go to All Tasks and click Request New Certificates.
5.  Select the Active Directory Enrollment Policy as the Certificate Enrollment Policy.
6.  On the Request Certificates page, select VA Web Server (Manual Enroll).
7.  Provide the certificate identification information for the following parameters.

| Parameter | Definition                                                                                             | Example                                   |
|---------------|------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| CN            | Common Name – The fully qualified domain name (FQDN) of the server you are requesting the certificate for. | \<servername(FQDN)\>.\<server id\>.med.va.gov |
| O             | Organization                                                                                               | Midwest Health Care Network                   |
| OU            | Organizational Unit                                                                                        | \<City\> Vet Center                           |
| L             | Locality                                                                                                   | \<City\>                                      |
| S             | State                                                                                                      | \<State\>                                     |
| C             | Country                                                                                                    | US                                            |

> Note: The above information is required with all of the certificate request tools.

8.  Click on Enroll.

> The wizard displays a message that the certificate has been enrolled and installed on the computer. The certificate will not be available immediately. When available (may be up to 24 hours), the certificate will appear within MMC under Personal folder  Certificates.

> The Intelligent InSites connector software is aware of MMC so no keystore is necessary. Intelligent InSites interacts with MMC to verify the certificates when needed.

9.  Use the information from the enrollment process to send a request to VA to issue the certificate. Follow the VA PKI SSL/TLS Request process REDACTED

## RTLS ESB Application Component Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Setup Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create a new group and user for Mule ESB. For ease of maintenance, consider creating group IDs (GIDs) and user IDs (UIDs) consistent across environments. GID and UID synchronization is required if using Network File System (NFS). Your local systems administrator will provide guidance. The instructions below use 503 as an example only. Change this value as appropriate for your installation. Execute instructions as root.

> 1\. Create the ESB group and user: groupadd -g 503 esb

> useradd -g 503 -u 503 -c "ESB" -d /home/esb -s /bin/bash esb

### Create Application Directories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create an RTLS application directory owned by the esb group.

1.  Create the directory and change ownership as root. mkdir /data/rtls

> chown -R esb:esb /data/rtls

2.  Change to the esb owner id so all new directories and files will be owned by esb. su – esb
3.  Create directories outside of the {MULE_HOME} directory to use as {APPROOT} later in the install instructions. This will be for RTLS ESB application usage. Creating the directory outside of

> {MULE_HOME} allows new versions of {MULE_HOME} to be installed without losing environment-specific information.

> mkdir /data/rtls/esb

> mkdir /data/rtls/esb/{environment}

### Configure Mule ESB Enterprise Edition for RTLS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Add Java Properties

> 1\. Add the following properties to {MULE_HOME}/conf/wrapper.conf wrapper.java.additional.4=-Desb.config.dir="/data/rtls/esb/base" wrapper.java.additional.4.stripquotes=TRUE wrapper.java.additional.5=-Ddeployment.security.TLSv1.1=true wrapper.java.additional.6=-Ddeployment.security.TLSv1.2=true wrapper.java.additional.7=-Djdk.tls.client.protocols=TLSv1.2 wrapper.java.additional.8=-Dhttps.protocols=TLSv1.2

> Note: The numbers appended to the above property statements vary based on how many additional properties are configured in the file. Modify to the next available number.

#### Modify Existing Java Properties

> Increase the logfile size, the number of archive files, and the Java memory. The values below are recommendations only. Edit the {MULE_HOME}/conf/wrapper.conf file properties as follows:

1.  Increase the logfile size to 20 MB wrapper.logfile.maxsize=20m
2.  Increase the number of archive files to 99 wrapper.logfile.maxfiles=99
3.  Increase the Java memory to 1024 MB

> wrapper.java.maxmemory=1024

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following sections provide instructions for installing the individual components that comprise the RTLS AT interface application.

## VistaService Web Services Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The section defines the installation procedure for the following sub-components:

- VistaLinkConsole-1.6.0.028.ear – This is a VA Developed WebLogic application that enables an Administrator to monitor the health of VistaLink connectors. Once installed, the application is accessible through the WebLogic Administration console.
- VistaLinkSamples-1.6.0.028.ear (non-production environments only). – This is a VA developed sample application that can be used to test VistaLink configurations. It is only for use in test environments.
- vlj-1.6.0.028 – This is a VA Developed J2EE Resource Adapter that defines VistaLink connections and binds them to the WebLogic Server Java Naming and Directory Interface (JNDI). VistaService uses these connections to execute RPCs on a given Vista instance.
- vistaassettrackservice.war– This is the HP developed application that implements a set of RESTful Web Services invoked by the ESB in the RTLS solution.

### Add WebLogic ID to the Vistasvcs Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Add the WebLogic ID to the vistasvcs group so the VistaServices web services can write to the log files, have access to the staging area, etc.

> 1\. Add WebLogic ID to vistasvcs group usermod -a -G vistasvcs weblogic

### Create Application Directories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Create the application directory (i.e. {APPROOT}) to hold VistaServices and set permissions. As root, create the directory, change the owner and permissions.

> mkdir /data/rtls/vistasvcs

> chown vistasvcs:vistasvcs {APPROOT} chmod 775 {APPROOT}

### Copy install Files and Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Copy the VistaServices setup file into a new application directory and untar it. Unzip the VistaLink components in the staging area.

1.  As vistasvcs, make a new directory, copy the setup file and untar it: mkdir {APPROOT}/{environment}

> cd {APPROOT}/{environment}

> cp the vistasvcs_setup.tar.gz in to this directory tar -xzf vistasvcs_setup.tar.gz

2.  As vistasvcs, unzip the VistaLink components into the staging area: cd staging

> unzip vlj\*.zip

### Configure HEV_CONFIG/log4j.xml File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The log4j.xml file is a configuration file for establishing parameters important for logging application failures. Edit the file and set the file location for logging as well as the level of logging. Set the location of the log4j.xml file in the \<param\> element.

> Logging file location = {APPROOT/{environment}/HEV_CONFIG/log4j.xml

> The file directory added to the param element should match the variable name set in setDomainEnv.

> e.g. \<param name="File" value="\${log4j.log.dir}/ "/\>

2.  Set the level of logging appropriate for the log4j environment as follows: Production environment : \<level value=”warn”/\>

> Testing environment: \<level value=”debug”/\>

### Modify VistA Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Two files must be revised to include entries for each VistA instance the RTLS solution needs to communicate with:

- gov.va.med.vistalink.connectorConfig.xml – The schema definition for this file is connectorConfig.xsd. A connector element needs to be defined for each Vista instance to be configured. See the VistaLink System Management Guide, section 2.3 VistALink Connector Configuration File for details.
- weblogic-ra.xml - contains WebLogic-specific deployment descriptor configuration settings (such as initial and maximum pool sizes) and JNDI-related properties that must be modified for each adapter, to distinguish one adapter from another in JDNI. See the VistaLink System Management Guide, section 2.2.4, 1.6 Deployment Descriptor: weblogic ra.xml for details.
1.  Change the permission of the connector config file: chmod 666

> {APPROOT/{environment}/HEV_CONFIG/gov.va.med.vistalink.connectorConfig.xml

2.  For newly added site connector names, edit the following file and create new \<connection- instance\> elements by copying an existing one, and modifying the Java Naming and Directory Interface (JNDI) name with the new name. Update will include two instances for each connection.

> {APPROOT}/{environment}/staging/vlj-\*/META-INF/weblogic-ra.xml

### Deploy VistaLinkConsole and Other Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Applications are deployed using the WebLogic Administration Console. The Administration Console is the web-based management interface for a WebLogic domain. For more information on how to use the WebLogic Administration Console, visit the online Oracle documentation library ([<u>http://www.oracle.com/technetwork/indexes/documentation/index.html</u>](http://www.oracle.com/technetwork/indexes/documentation/index.html)).

> Deploy the applications and resource Adapter from {APPROOT}/{environment}/staging

1.  Deploy VistaLinkConsole to the AdminServer
2.  Deploy the exploded vlj-1 directory as a resource adapter on the AdminServer and on the Cluster.
3.  Deploy the VistaServiceEar to the cluster.
4.  For test environments, deploy vistaLinkSamples\* to the cluster. For Prod, may not want the samples loaded.

### Setup and Configure Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The create_vistasvcs_security.py script creates new user groups, security groups, and roles to support VistaServices Web Services and the RTLS-VistA Interface Configuration Tool. Verify the parameters in the VistaServices Security script, change where necessary and then run the script. Execute commands as weblogic from {WL_RTLS}:

1.  Verify params in wlst.sh install/create_vistasvcs_security.py
2.  Run the script

> wlst.sh install/create_vistasvcs_security.py

3.  Update the vistaConfig6.dat and insitesConfig6.dat files on the ESB server and configure the system connection information appropriately (See [4.1.2](#configuring-site-information)).

> Once the application is deployed the services are started.

## RTLS-VistA Interface Configuration Tool Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To install the RTLS-VistA Interface Configuration Tool, complete all steps in this section.

### Create SQL Server Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RtlsInterfaceAdmin application runs on SQL Server. Complete the following steps as the database administrator to create the database:

1.  Execute the following script to create the appropriate permission to create the database. grants.sql
2.  Create a database named admin_tool for the Application data store.
3.  Create a database named rtls_scheduler for the Quartz scheduler data store.
4.  Execute the following script to create the primary data store for the application. By default this script uses the admin_tool database to create the schema.

> MSSS2008R2_admin_tool_with_enterprise_data_Consolidated_04162014.sql

5.  Execute the following script to create the Quartz scheduler database used by the application. By default this script uses the admin_tool database to create the schema.

> rtls_scheduler_sqlserver_03282014.sql

### Define SQL Server Data Sources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Define the two SQL Server data sources using the Weblogic Admin Console. Create one Java Database Connectivity (JDBC) data source for each RtlsInterfaceAdmin database using the same user as detailed below. When prompted, select “Supports Global Transaction and Choose One- Phase Commit”.

| Application Data Store |                                                              |
|----------------------------|--------------------------------------------------------------|
| Parameter              | Value                                                    |
| Name                       | MSSqlRtlsAdmin                                               |
| JNDI Name                  | jdbc/MSSqlRtlsAdmin                                          |
| Database Type              | MS Sql Server                                                |
| Database Driver            | Oracle's MS SqlServer Driver (Type 4) Versions 7 and later   |
| Database Name              | admin_tool                                                   |
| Host Name                  | Fully qualified SQL Server host name                         |
| Port                       | 1433                                                         |
| Database User Name         | user created for this database                               |
| Password                   | account password                                             |
| Driver Class Name          | weblogic.jdbc.sqlserver.SQLServerDriver                      |
| URL                        | jdbc:weblogic:sqlserver://\[HOST_NAME\]:1433                 |
| Target                     | Assign Data Source to the "All Server of the Cluster" option |

| Quartz Scheduler Data Store |                                                |
|---------------------------------|------------------------------------------------|
| Parameter                   | Value                                      |
| Name                            | MSSqlRtlsScheduler                             |
| JNDI Name                       | jdbc/MSSqlRtlsScheduler                        |
| Database Type                   | MS Sql Server                                  |
| Database Driver                 | Oracle's MS SqlServer Driver (Type 4) Versions |
| Database Name                   | rtls_scheduler                                 |
| Host Name                       | Fully qualified SQL Server host name           |
| Port                            | 1433                                           |
| Database User Name              | user created for this database                 |

| Quartz Scheduler Data Store |                                                              |
|---------------------------------|--------------------------------------------------------------|
| Password                        | account password                                             |
| Driver Class Name               | weblogic.jdbc.sqlserver.SQLServerDriver                      |
| URL                             | jdbc:weblogic:sqlserver://\[HOST_NAME\]:1433                 |
| Target                          | Assign Data Source to the "All Server of the Cluster" option |

### Deploy the RTLS-VistA Interface Configuration Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Deploy the RTLS-VistA Interface Configuration Tool using the WebLogic Administration Console.

> Deploy the application from {APPROOT}/{environment}/staging

> 1\. Deploy RtlsInterfaceAdmin.war to the cluster.

### Configure RTLS-VistA Interface Configuration Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the RTLS-VistA Interface Configuration Tool is installed, use the tool to define your site (e.g. a VA facility) and the jobs needed to interface between AEMS-MERS and Intelligent InSites. The RTLS-VistA Interface Configuration Tool is documented in the RTLS ESE Technical Manual. The instructions for how to define a site and set up jobs is documented in the Technical Manual. Follow the high level steps below:

1.  If your VA facility is the first facility within a VISN to install RTLS, define the VISN.
2.  Add your site.
3.  Add and schedule the jobs needed to establish the interface between AEMS-MERS and RTLS.

> Warning: The VistA Engineering EQUIPMENT INV file \# 6914 requires backup before the interface jobs run to provide a snapshot of file for rollback if needed. See the RTLS AT Patch Installation Guide for backup instructions.

## RTLS ESB Component Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To install the RTLS ESB application for the first time, complete the steps in sec[tion 3.3.1](#initial-installation)- [3.3.5.](#start-and-verify-the-mule-esb-application) If you have already installed the RTLS ESB application and need to re-install, see Subsequent install section [3.3.6](#subsequent-installation).

### Initial Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Copy the setup tar file to {APPROOT} copy setup_esb.tar.gz to {APPROOT}
2.  Extract and run the setup tar file. tar -zxf setup_esb.tar.gz

> The following table lists the directories extracted and a description of each.

| Directory/File      | Description                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| {APPROOT}/prop          | A directory to hold server-specific properties (i.e. assettrax.properties). The directory persists between application deployments. |
| {APPROOT}/schemas       | A directory to hold application supplied schema.                                                                                    |
| {APPROOT}/report        | A directory to hold the current audit-type reports for the application.                                                             |
| {APPROOT}/reporthistory | A directory to hold the historical audit-type reports for the application.                                                          |

1.  <span id="3.3.2._Populate_the_RtlsDomain_Property_" class="anchor"></span>Populate the RtlsDomain Property File The Mule ESB application domain component has a property file. The file name and location are as follows:

> {APPROOT}/prop/rtls.domain.properties

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Property Key</strong></th>
<th><strong>Property Value</strong></th>
<th><strong>Definition/Origin</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>rtls.domain.host</td>
<td>localhost</td>
<td><blockquote>
<p>Server name or IP address of listener.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>rtls.domain.port</td>
<td>8082</td>
<td><blockquote>
<p>This is the authorized port for RTLS applications to listen on.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>rtls.domain.path</td>
<td>esb</td>
<td><blockquote>
<p>Base path of all RtlsDomain ESB applications.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>rtls.domain.timeout</td>
<td>60</td>
<td></td>
</tr>
</tbody>
</table>

### Deploy the RtlsDomain ESB Domain Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Mule ESB domain component declares shared resources that are utilized by all ESB applications. This component must be installed before any RTLS ESB applications. Any previously installed (non-domain) RTLS applications MUST be uninstalled and, after deploying the RtlsDomain component, the domain-enabled version of the RTLS applications must be installed. Domain applications are programmatically bound to a specific version of the RtlsDomain component.

> To deploy the domain component, the RtlsDomain-1.0.zip file should be placed in the

> \${MULE_HOME}/domains directory.

### Populate the Asset Tracking Property File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Mule ESB application component has a property file. Use the information gathered from the installation and configuration of the application components and pre-requisite software to populate the fields in the file. Only the properties values should be modified. The following table provides a list of the properties to be defined. Within the assettrax.properties file, userids and passwords are encrypted using Triple-DES cryptography (PBEWithMD5AndTripleDES) which is then encoded as base64 string values.

> The file name and location are as follows:

> {APPROOT}/prop/assettrax.properties

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Property Key</strong></th>
<th><strong>Property Value</strong></th>
<th><strong>Definition/Origin</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>async.strategy.maxBufferSize</td>
<td>5000</td>
<td>Asnc processing strategy maximum buffer size. ESB application internal usage. Do NOT modify.</td>
</tr>
<tr class="even">
<td>async.strategy.maxThreads</td>
<td>500</td>
<td>Asnc processing strategy maximum threads. ESB application internal usage. Do NOT modify.</td>
</tr>
<tr class="odd">
<td>async.strategy.minThreads</td>
<td>50</td>
<td>Asnc processing strategy minimum threads. ESB application internal usage. Do NOT modify.</td>
</tr>
<tr class="even">
<td>async.strategy.threadWaitTim eout</td>
<td>-1</td>
<td>Asnc processing strategy wait time out. ESB application internal usage. Do NOT modify.</td>
</tr>
<tr class="odd">
<td>client.ssl.password</td>
<td>cacerts.password</td>
<td>Password for the cacerts certificate. Provided by the system administrator.</td>
</tr>
<tr class="even">
<td>client.ssl.path</td>
<td>/path/to/cacerts/certificate</td>
<td>Path to the cacerts certificate. Provided by the system administrator.</td>
</tr>
<tr class="odd">
<td>insites.locator.file</td>
<td>C:/Projects/Configuration/pro p/insitesConfig6.dat</td>
<td>File path to the Insites connections configuration file.</td>
</tr>
<tr class="even">
<td><p>insites.not.responding.service</p>
<p>.interval</p></td>
<td>0</td>
<td><p>Intelligent Insites property configuration time interval usage. Do NOT modify. Corresponds to the configurable interval for an internal Insites process that determines whether or not an asset's active tag transmitter has been detected on the Wi- fi network during the past</p>
<p>interval period (specified in</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Property Key</strong></th>
<th><strong>Property Value</strong></th>
<th><strong>Definition/Origin</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>hours).</td>
</tr>
<tr class="even">
<td>base.path</td>
<td>esb</td>
<td>Base path for all RtlsDomain services</td>
</tr>
<tr class="odd">
<td>local.assettrax.path</td>
<td>assettrax/services</td>
<td>path prefix to all services, appended onto the base.path</td>
</tr>
<tr class="even">
<td>local.assettrax.host</td>
<td>localhost</td>
<td><p>The host name for the application (server name)</p>
<p>(must resolve to an address that the rtls.domain.host is configured for in the rtls.domain.properties file)</p></td>
</tr>
<tr class="odd">
<td>local.assettrax.port</td>
<td>8082</td>
<td><p>The shared port number for all RtlsDomain applications</p>
<p>(must match the rtls.domain.port value in the rtls.domain.properties file)</p></td>
</tr>
<tr class="even">
<td>local.assettrax.timeout</td>
<td>30000</td>
<td>ESB internal server transaction timeout usage. Do NOT modify.</td>
</tr>
<tr class="odd">
<td>locationreportdir</td>
<td>/data/rtls/esb/report/</td>
<td>Directory of where the unmapped report for Intelligent Insites is temporary stored.</td>
</tr>
<tr class="even">
<td>locationreporthistorydir</td>
<td>/data/rtls/esb/reporthistory/</td>
<td>Directory of where the unmapped historical reports for Intelligent InSites are stored.</td>
</tr>
<tr class="odd">
<td>rtls.timeout</td>
<td>300000</td>
<td>Connection timeout for RTLS</td>
</tr>
<tr class="even">
<td>security.filter.realm</td>
<td>default</td>
<td>authentication realm</td>
</tr>
<tr class="odd">
<td>security.user.id</td>
<td></td>
<td>Basic authentication userid for the Mule ESB endpoint.</td>
</tr>
<tr class="even">
<td>security.user.id</td>
<td></td>
<td>user id</td>
</tr>
<tr class="odd">
<td>security.user.password</td>
<td>basic.authentication.passwor d</td>
<td>Basic authentication password for the Mule ESB endpoint.</td>
</tr>
<tr class="even">
<td>vista.locator.file</td>
<td>/data/rtls/esb/prop/vistaConfig 6.dat</td>
<td>Path to the vistaConfig.dat which defines the primary/substation relationships and the connection to the corresponding WebLogic service.</td>
</tr>
</tbody>
</table>

| Property Key | Property Value | Definition/Origin        |
|------------------|--------------------|------------------------------|
| vista.timeout    | 300000             | Connection timeout for VistA |

### Start and Verify the Mule ESB Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For each of the ESB servers, start the RTLS ESB application and verify it is running correctly.

1.  Start Mule server: \${MULE_HOME}/bin/mule start.
2.  To verify mule started successfully, check to see if the esb-assettrax-1.0.x.x-anchor.txt file was created under the \${MULE_HOME}/apps.
3.  Open the log file “assettrax.log” under \${MULE_HOME}/logs. Ensure the log file looks similar to the content in the figure below.

> Figure 1 Sample of Successful Result for assettrax.log File

### Subsequent Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To re-install the RTLS ESB application, complete the following steps.

1.  Make a copy of the currently installed esb-assettrax-1.0.x.x application as a backup. If the original application package is available, use that as the backup copy.
2.  Go to the directory \${MULE_HOME}/apps and remove the application by issuing the command “rm esb-assettrax-1.0.x.x-anchor.txt”.
3.  Shutdown Mule EE by issuing the command {MULE_HOME}/bin/mule stop.
4.  Make changes to the assettrax.properties file, if needed.
5.  Place the new esb-assettrax-1.0.x.x.zip file under \${MULE_HOME}/apps.
6.  Start Mule server \${MULE_HOME}/bin/mule start.
7.  Check assettrax.log to ensure esb-assettrax-1.0.x.x application is up and running.

# Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Configuring SSL/TLS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are many different individual steps involved in configuring SSL. Expressing the full configuration of SSL is beyond the scope of this guide. A couple of items to note:

- WebLogic includes a FIPS approved crypto package for SSL that is configured for the solution.
- The current version of Mule ESB does NOT have an approved crypto module, or a facility to integrate one. The solution deploys an Apache proxy to offload the FIPS approved crypto SSL with localhost-only communication over non-SSL. A future upgrade to Mule ESB 3.5 would allow integration of FIPS SSL support with purchase of a 3rd party FIPS crypto provider.
- The AT Patch Installation Guide contains the recommended location for the imported keystore.

> The following generalized steps are provided to give the reader an understanding of the process to install a certificate.

1.  Modify configuration files to point to the new certificate.
2.  Import the certificate to create a trusted chain within your keystore by importing the Root, Sub, and then the new SSL certificate.
3.  Check to make sure the new certificate is working.

### Configuring Site Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To deploy the Asset Tracking interface, the network connection information is defined in both the vistaConfig.dat file and the insitesConfig6.dat. To establish the new connection, a Reload Locator Service is called. This allows the connection to be established without having to stop and re-start the RTLS ESB application.

> The entries below should be defined, one per primary station. The VISN field is informational only, allowing locating the correct group of entries in a multi-VISN (i.e., AITC) installation easier.

> The format of the Config.dat files is as follows:

> VISNxx; primary station; \<sites\>;\<timezone\>;reportUser; \<hostname\>\|\<port\>\|\<userid\>\|\<password\>

> Where:

- VISNxx = VISN identifier
- Primary station = the primary station that is associated with a VistA instance
- sites = a comma delimited string of all CL stations/substations hosted within the primary station’s VistA instance
- time zone = the time zone designation. Valid values are:
  - America/New_York for Eastern
  - America/Chicago for Central
  - America/Denver for Mountain
  - America/Los_Angeles for Pacific
- ReportUser = a comma delimited string of Intelligent InSites users who will receive reports.
- hostname = the Fully Qualified Domain Name (FQDN) of the WebLogic server
- port = port
- userid = the userid for the RTLS ESB application to communicate with WebLogic webservices
- password = password

> Note: The connection is encrypted. The following is an unencrypted example:

> The following is an encrypted example:

> Follow the steps below to define a new site for the Asset Tracking Interface:

1.  Copy the EncryptConnectionString.class file needed to encrypt the connection string from the code repository to the server.
2.  Edit the {MULE_HOME}/vistaConfig.dat file properties as follows:
    1.  Add a new line to represent the VISN if it doesn’t exist.
    2.  Add the site.
    3.  Encrypt the hostname, port, userid and password using the EncryptConnectionString.class file.
    4.  Insert the encrypted string into the properties file.
3.  Save the file.
4.  Run the Reload Locator Service: https://{server hostname}/locatorReload
5.  Remove the EncryptConnectionString.class file from the server.

> Note: For security reasons, it is important for the EncryptConnectionString.class file to be removed from the server after the string has been encrypted.

### Creating Location External References in InSites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The AEMS-MERS-RTLS interface relies on each location within Intelligent InSites having an

> \<esf-room-number\> location external references. Follow the steps below to establish the external references within InSites:

> 1\. Invoke the following endpoint on the ESB:

> https://{server hostname}/esb/assettrax/services/location/extref/migration?station=\<station\>&vista=\<VistA Instance\>

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The high level steps defining the back out strategy for the RTLS AT interface application are as follows:

1.  Monitor installation – use logging and other diagnostic methods to monitor and check the installation as the components are individually installed.
2.  Document errors – Document and resolve errors that occur during the installation process.
3.  If any of the installed RTLS AT application components has a severe error and needs to be backed out, the RTLS System Operations Manager contacts the RTLS Technical Director to communicate that Back- out/Uninstall Procedures are being followed.
4.  Follow the procedures for individual components as documented in Section [5.6.](#back-out-procedure-1)
5.  The RTLS Technical Director will notify VA OIT staff that the documented Back Out process was followed.
6.  Document the entire scenario in an Issue log.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> User Acceptance Testing was performed and accepted on all of the RTLS ESE Interfaces, including the Asset Tracking interface. To view the consolidated daily reports delivered at the conclusion of testing each day, see the RTLS ESE Formal Test Results.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Back-out will be necessary if any of the installed RTLS AT application components has a severe error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The risk involved with backing out of the RTLS AT interface applications is low because RTLS can function without the interface running.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS AT interface application is a subset of the larger national RTLS deployment. The acceptance of all hardware and software is documented in a formal facility acceptance plan. The facility Point of Contact (POC) responsible for acceptance would also be the person with authority to require back-out and accept potential risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following sections provide instructions on how to remove the components from the system.

### VistaService Web Services Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The steps necessary to back-out the VistaService Web Services include deleting the deployment using the WebLogic Administration Console and then manually modifying the configuration files to remove content related to the services.

1.  Undeploy the VistaService Web Services.
2.  Edit the following files to remove the references to VistaService Web Services:

| Reference Step                                                               | File(s)                                       |
|----------------------------------------------------------------------------------|---------------------------------------------------|
| [3.1.4 Configure HEV_CONFIG/log4j.xml File](#configure-hev_configlog4j.xml-file) | Log4j.xml                                         |
| [3.1.7 Setup and Configure Security](#setup-and-configure-security)              | Files referenced in: create_vistasvcs_security.py |

### RtlsInterfaceAdmin Application Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The steps necessary to back-out the RtlsInterfaceAdmin application include deleting the deployment using the WebLogic Administration Console, removing the JDNI bindings related to the application, and dropping the associated databases.

1.  Undeploy the RtlsInterfaceAdmin application.
2.  Remove the JNDI data sources related to the application
3.  Drop the following SQL databases created during the install: admin_tool

> rtls_scheduler

### RTLS ESB Application Component Back-out/Uninstall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If the application is up and running, issue the following command from \${HOME_MULE}/apps directory:

> \$rm esb-assettrax-1.0.x.x-anchor.txt The application is removed.

2.  If there is no esb-assettrax-1.0.x.x-anchor.txt, issue rm –r esb-assettrax-1.0.x.x-anchor directory.
3.  If there is no esb-assettrax-1.0.x.x-anchor directory, issue rm esb-assettrax-1.0.x.x-anchor.zip

### RTLS ESB Application Component Back-out/Uninstall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If the application is up and running, issue the following command from \${HOME_MULE}/apps directory:

> \$rm esb-assettrax-1.0.x.x-anchor.txt The application is removed.

2.  If there is no RTLSServices-anchor.txt, issue rm –r esb-assettrax-1.0.x.x directory.
3.  If there is no RTLSServices directory, issue rm esb-assettrax-1.0.x.x.zip

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RTLS AT interface application does not have a transactional database. For information on back-up and rollback of the AEMS-MERS inventory data, see the RTLS AT Patch Installation Guide.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

# Appendix A: Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To diagnose an installation problem, use the following general troubleshooting steps. In addition, check the RTLS CL Patch Installation Guide Frequently Asked Questions (FAQ) section.

## Run the Deployment Health Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To verify that the communication is working between all distributed components, the following health checks are available.

> ESB Application is up and running:

> …/esb/assettrax/services/ping/txt

> ESB Application can communicate with the Vista site:

> …/esb/assettrax/services/ping/txt?system=vista&siteId=500 ESB Application can communicate with the Insites site:

> …/esb/assettrax/services/ping/txt?system=insites&siteId=500

> If there is a problem, the response will provide some information about what to check.

## Check the Log Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> WebLogic, Mule ESB, and the RTLS Interface Application use a Java logging framework called log4j. The log files are defined in the log4j.properties file and also included below for convenience. The log4j.properties file can be used to configure different logging levels and also to enable and disable logging as needed. The log files may capture information about exceptions that arise during installation.

| Log File                         | Description                                                 |
|--------------------------------------|-----------------------------------------------------------------|
| /data/rtls/vistasvcs/{env}/log       | WebLogic log file.                                              |
| /data/mule/{env}/logs                | Mule ESB log file.                                              |
| /data/mule/{env}/logs/{flowname}.log | Log files containing information related to the Mule ESB flows. |

> Note: In the log file names above, {env} represents an environmental variable set during installation.

> {flowname} represents the process flow name associated with the interface component.

### Template Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 45%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
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
<td>February 2016</td>
<td>2.1</td>
<td><blockquote>
<p>Changed title from Installation, Back-Out, and Rollback Plan to Installation, Back- Out, and Rollback Guide as recommended by OI&amp;T Documentation Standards Committee</p>
</blockquote></td>
<td><blockquote>
<p>OI&amp;T Documentation Standards Committee</p>
</blockquote></td>
</tr>
<tr class="even">
<td>December 2015</td>
<td>2.0</td>
<td><blockquote>
<p>The OI&amp;T Documentation Standards Committee merged the</p>
</blockquote>
<p>existing <em>“Installation, Back-Out, Rollback Plan”</em> template with the content requirements in the OI&amp;T End-user Documentation Standards for a more comprehensive Installation Plan.</p></td>
<td><blockquote>
<p>OI&amp;T Documentation Standards Committee</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>February 2015</td>
<td>1.0</td>
<td><blockquote>
<p>Initial Draft</p>
</blockquote></td>
<td><blockquote>
<p>Lifecycle and Release Management</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *The Template Revision History pertains only to the format of the template. It does not apply to the content of the document or any changes or updates to the content of the document after distribution. It can be removed at the discretion of the author of the document.*