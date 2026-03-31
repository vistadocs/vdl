---
title: DATUP Version 1.0.00.003 Local Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Local Install Guide
app_code: PRED
app_name: "Pharmacy: Pharmacy Data Update (DATUP)"
section: GUI
app_status: active
pkg_ns: PRED
patch_ver: 1.0.00.003
patch_id: PRED*1.0.00.003
group_key: "PRED:PRED:1.0.00.003"
file_numbers: []
security_keys: []
menu_options: 0
description: "The following list provides a brief description of the sections included in this document:"
audience: 
keywords: 
  - figure
  - datup
  - span
  - local
  - class
  - weblogic
  - console
  - server
  - install
  - version
page_count: 0
word_count: 9919
section_count: 15
table_count: 9
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/15168_datup_igl_v1-0-00-003.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/15168_datup_igl_v1-0-00-003.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=203"
---

15168-DATUP_IGL-V1.0.00.003

Local DATA UPDATE (DATUP) COMPONENT

INSTALLATION GUIDE

Version 1.0.00.003

VETERANS HEALTH ADMINISTRATION (VHA)  
Pharmacy Reengineering and

Information Technology Support Project, Testing Support

<span class="mark">REDACTED</span>

Prepared for:

<span class="mark">REDACTED</span>

Prepared by:

<span class="mark">REDACTED</span>

SwRI<sup></sup> Project No. 10-15168

December 3, 2010

15168-DATUP_IGL-V1.0.00.003

Local DATA UPDATE (DATUP) COMPONENT

INSTALLATION GUIDE

Version 1.0.00.003

VETERANS HEALTH ADMINISTRATION (VHA)  
Pharmacy Reengineering and

Information Technology Support Project, Testing Support

<span class="mark">REDACTED</span>

Prepared for:

<span class="mark">REDACTED</span>

Prepared by:

<span class="mark">REDACTED</span>

SwRI<sup></sup> Project No. 10-15168

<span class="mark">REDACTED</span> Date

Project Manager

<span class="mark">REDACTED</span> Date

Manager

Intelligent Systems Department

TABLE OF CONTENTS

*Page*

LIST OF FIGURES

Figure 3‑1. WebLogic Console [1](#_Ref191089515)

Figure 3‑2. Caché System Management Portal [1](#_Ref205866025)

Figure 3‑3. Domain Structure [1](#_Ref256581857)

Figure 3‑4. Change Center [1](#_Ref256581858)

Figure 3‑5. Summary of Servers [1](#_Ref256581859)

Figure 3‑6. Settings for Deployment Server [1](#_Ref256581860)

Figure 3‑7. Server Start Tab [1](#_Ref256581861)

Figure 3‑8. Activate Changes [1](#_Ref256581862)

Figure 3‑9. Domain Structure [1](#_Ref184087883)

Figure 3‑10. Change Center [1](#_Ref184087925)

Figure 3‑11. Summary of JDBC Data Sources [1](#_Ref181416612)

Figure 3‑12. JDBC Data Source Properties [1](#_Ref191102359)

Figure 3‑13. Transaction Options [1](#_Ref191089711)

Figure 3‑14. Connection Properties [1](#_Ref191089804)

Figure 3‑15. Test Database Connection [1](#_Ref191089849)

Figure 3‑16. Select Targets [1](#_Ref191089523)

Figure 3‑17. Summary of JDBC Data Sources [1](#_Ref181418183)

Figure 3‑18. Statement Cache Size Parameter [1](#_Ref258586453)

Figure 3‑19. Activate Changes [1](#_Ref193865244)

Figure 3‑20. Lock & Edit [1](#_Ref195512216)

Figure 3‑21. JMS Modules [1](#_Ref195512217)

Figure 3‑22. JMS Modules [1](#_Ref195512223)

Figure 3‑23. JMS System Module Properties [1](#_Ref195512238)

Figure 3‑24. JMS System Module Targets [1](#_Ref195512256)

Figure 3‑25. Add Resources to JMS System Module [1](#_Ref195512273)

Figure 3‑26. Activate Changes [1](#_Ref195512291)

Figure 3‑27. Lock & Edit [1](#_Ref193978393)

Figure 3‑28. JMS Modules [1](#_Ref193978412)

Figure 3‑29. JMS Modules [1](#_Ref193978431)

Figure 3‑30. Summary of Resources [1](#_Ref193978452)

Figure 3‑31. Choose Type of Resource to Create [1](#_Ref193981712)

Figure 3‑32. Foreign Server Properties [1](#_Ref193977655)

Figure 3‑33. Foreign JMS Server Target [1](#_Ref193981734)

Figure 3‑34. Summary of Resources [1](#_Ref193981761)

Figure 3‑35. Foreign JMS Server General Configuration [1](#_Ref193981790)

Figure 3‑36. Activate Changes [1](#_Ref193978131)

Figure 3‑37. Lock & Edit [1](#_Ref271266366)

Figure 3‑38. JMS Modules [1](#_Ref271266392)

Figure 3‑39. JMS Modules [1](#_Ref271266409)

Figure 3‑40. Summary of Resources [1](#_Ref271266425)

Figure 3‑41. Foreign JMS Server General Configuration [1](#_Ref271266451)

Figure 3‑42. Destinations [1](#_Ref271266475)

Figure 3‑43. Foreign Connection Factory Properties [1](#_Ref271266551)

Figure 3‑44. Activate Changes [1](#_Ref271266563)

Figure 3‑45. Lock & Edit [1](#_Ref193981831)

Figure 3‑46. JMS Modules [1](#_Ref193981847)

Figure 3‑47. JMS Modules [1](#_Ref193981888)

Figure 3‑48. Summary of Resources [1](#_Ref193981910)

Figure 3‑49. Foreign JMS Server General Configuration [1](#_Ref193978585)

Figure 3‑50. Foreign JMS Server Connection Factories [1](#_Ref193979224)

Figure 3‑51. Foreign Connection Factory Properties [1](#_Ref193979563)

Figure 3‑52. Activate Changes [1](#_Ref193979715)

Figure 3‑53. Domain Structure [1](#_Ref178735721)

Figure 3‑54. Change Center [1](#_Ref181421187)

Figure 3‑55. Deployments [1](#_Ref178732223)

Figure 3‑56. Install Application Assistant [1](#_Ref178732382)

Figure 3‑57. Locate Deployment to Install and Prepare for Deployment [1](#_Ref184090181)

Figure 3‑58. Upload a Deployment to the Admin Server [1](#_Ref184090012)

Figure 3‑59. Choose Targeting Style [1](#_Ref176676787)

Figure 3‑60. Select Deployment Targets [1](#_Ref191090118)

Figure 3‑61. Optional Settings [1](#_Ref191090176)

Figure 3‑62. Review Your Choices and Click Finish [1](#_Ref191090260)

Figure 3‑63. Settings for DATUP [1](#_Ref191090327)

Figure 3‑64. Activate Changes [1](#_Ref178733999)

Figure 3‑65. Domain Structure [1](#_Ref181421306)

Figure 3‑66. Summary of Deployments [1](#_Ref191090401)

Figure 3‑67. Start Application Assistant [1](#_Ref191090464)

Figure 3‑68. Summary of Deployments – DATUP Deployment Active [1](#_Ref191090529)

Figure 4‑1. Domain Structure [1](#_Ref246231865)

Figure 4‑2. Change Center [1](#_Ref246231871)

Figure 4‑3. Summary of Deployments – Stopping DATUP [1](#_Ref246231328)

Figure 4‑4. Force Stop Application Assistant [1](#_Ref246231887)

Figure 4‑5. Summary of Deployments – DATUP Deployment Prepared [1](#_Ref246231898)

Figure 4‑6. Delete Application Assistant [1](#_Ref246231908)

Figure 4‑7. Summary of Deployments – DATUP Deployment Deleted [1](#_Ref246231916)

Figure 4‑8. Activate Changes [1](#_Ref246231924)

LIST OF TABLES

Table 3‑1. Terminology [1](#_Ref176675115)

Table 3‑2. Namespace Configuration [1](#_Ref259198676)

Table 3‑3. Advanced Parameter Configuration [1](#_Ref259197773)

Table 3‑4. Advanced Settings Configuration [1](#_Ref271302610)

Table 3‑5. Memory Management Parameters [1](#_Ref271302703)

Table 3‑6. Optional Site Configuration Properties [1](#_Ref213809714)

Appendices

Appendix A – Local DATUP Configuration

Appendix B – Combined DATUP and PECS Architecture

REVISION HISTORY

| Date              | Version    | Description                                                                                        | Author |
|-------------------|------------|----------------------------------------------------------------------------------------------------|--------|
| September 3, 2010 | 1.0.00.001 | Local PEDTUP Installation Guide: Initial version.                                                  | SwRI   |
| October 8, 2010   | 1.0.00.001 | Renamed all instances of “PEDTUP” to “DATUP.                                                       | SwRI   |
| November 12, 2010 | 1.0.00.002 | Updated the document to address change request \#CR2942.                                           | SwRI   |
| December 3, 2010  | 1.0.00.003 | No changes since last delivery. Updated the version number to reflect the latest release of DATUP. | SwRI   |

<span id="_Ref213809714" class="anchor"></span>Table 3‑. Optional Site Configuration Properties

(This Page Intentionally Left Blank)

# Project Scope


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Project Scope](#project-scope)
  - [Project Identification](#project-identification)
  - [Project Description](#project-description)
  - [PRE Project Goals and Objectives](#pre-project-goals-and-objectives)
  - [DATUP Background](#datup-background)
  - [Related Documents](#related-documents)
- [DOCUMENT Overview](#document-overview)
  - [Document Background](#document-background)
  - [Overview](#overview)
- [Installation Instructions](#installation-instructions)
  - [Terminology](#terminology)
  - [Assumptions](#assumptions)
  - [Database Installation and Configuration](#database-installation-and-configuration)
    - [Caché Features and Installation](#caché-features-and-installation)
    - [Caché Database Configuration](#caché-database-configuration)
    - [FDB DIF Instructions](#fdb-dif-instructions)
  - [WebLogic Installation Instructions](#weblogic-installation-instructions)
    - [Class Path](#class-path)
    - [WebLogic Server Startup Configuration](#weblogic-server-startup-configuration)
    - [Local JDBC Data Source Configuration](#local-jdbc-data-source-configuration)
    - [Log4j](#log4j)
    - [Site Configuration Properties](#site-configuration-properties)
    - [DATUP Configuration Properties](#datup-configuration-properties)
    - [DATUP Cleanup Script](#datup-cleanup-script)
    - [Deployment](#deployment)
- [Upgrade Installation Instructions](#upgrade-installation-instructions)
  - [Uninstall Previous Release](#uninstall-previous-release)
  - [Deploy New Release](#deploy-new-release)
- [System Verification](#system-verification)
  - [Verification](#verification)

## Project Identification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Southwest Research Institute<sup>®</sup> is developing this Pharmacy Reengineering (PRE) and Information Technology Support Project document for the PRE project Testing Support Contract No. GS‑35F‑0533L / VA118-09-F-0003.

|                     |                                                                                        |
|---------------------|----------------------------------------------------------------------------------------|
| Project Title:  | VHA Pharmacy Reengineering and Information Technology Support Project, Testing Support |
| Project Number: | <span class="mark">REDACTED</span>                                                     |
| Abbreviation:   | PRE                                                                                    |

## Project Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goal of the VHA PRE project is to design and develop a re-engineered pharmacy system, incorporating changes that have been made to the Enterprise Architecture and changes in pharmacy business processes. The intent of the PRE program is to ensure that no current system functionality is lost, but that it is either replicated in the new system or replaced by improved process and functionality. While the overall plan is still based on designing and implementing a complete pharmacy system, the scope of the effort has been defined to address a focused subset of the PRE functionality confined to the Data Update (DATUP) process.

## PRE Project Goals and Objectives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The objective of the PRE project is to facilitate the improvement of pharmacy operations, customer service, and patient safety for the VHA. The PRE project will help address the identified goals and vision for the VHA Pharmacy System.

The goal for the PRE project is a seamless and integrated nationally-supported system that is an integral part of the Health*<u>e</u>*Vet-Veterans Health Information Systems & Technology Architecture (VistA) environment. To meet this goal, the PRE project will enhance pharmacy data exchange, as well as clinical documentation capabilities, in a truly integrated fashion to improve operating efficiency and patient safety. Additionally, it will provide a flexible technical environment to adjust to future business conditions and to meet patient needs in the clinical environment. Achieving this goal will enable resolution of current pharmacy issues, improve patient safety, and facilitate long-term process stability.

## DATUP Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP supports the Medication Order Check Healthcare Application (MOCHA) by performing data source updates. MOCHA conducts order checks using First DataBank’s (FDB) Drug Information Framework (DIF) within the existing VistA pharmacy application. FDB is a data product that provides the latest identification and safety information on medications. Additionally, FDB provides the latest algorithms used to perform order checks. DATUP processes the data updates associated with FDB’s DIF. The order checks performed by MOCHA include:

- Drug-Drug Order Check – Check interactions between two or more drugs, including interaction monographs.
- Duplicate Therapy Order Check – Check for duplicated drug classifications between two or more drugs.
- Drug-Dose Order Check – Check minimum and maximum single doses, verify the dosing schedule, and provide the normal dosing range.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A complete list of documents relating to the PRE project and the DATUP development effort can be found in the Glossary and Acronym List (Version 5.0, dated September 26, 2008).

# DOCUMENT Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information contained in this Local Data Update (DATUP) Installation Guide is specific to DATUP development, which supports the MOCHA component. This section defines the layout of this document and provides an outline of the document structure.

## Document Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document details the steps required to install the DATUP software at a local site, the terminology used for the configuration and deployment of the software, and the assumptions for installing the software. Additionally, this document details how to install and configure the database environment. This document accompanies the delivery of the DATUP.v1.0.00.003 software release. The DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010) is delivered as a companion document to this Installation Guide. Refer to the Version Description Document for more information on the software inventory and versions used in the DATUP.v1.0.00.003 software release.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list provides a brief description of the sections included in this document:

Section 1: Provides introductory material delineating the purpose of the PRE project and the scope of the MOCHA effort

Section 2: Presents an overview of the layout of the document

Section 3: Presents the installation instructions for the DATUP.v1.0.00.003 software release

Section 4: Presents verification steps to verify that the installation was successful

Text in a Courier New font indicates WebLogic Console panels or text, commands, and settings that must be typed, executed, or configured to complete the installation.

(This Page Intentionally Left Blank)

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions detail the steps required to perform a *fresh* installation of the DATUP software at a local site. For *upgrade* installation instructions see Section 4. Section 3.1 details the terminology used for the configuration and deployment of the DATUP software. Section 3.2 outlines the assumptions for installing the DATUP software. While the system may be configured to run outside the given assumptions, doing so requires modifications that are not detailed in this document. Section 3.3 describes how to install and configure the DATUP software properly. Finally, Section 3.3 describes how to install and configure the database environment.

In order to understand the installation and verification process, the reader should be familiar with the WebLogic console shown in Figure 3‑1. The WebLogic console is a Web page viewable from any Internet browser; however, Internet Explorer, Version 7, is recommended. The WebLogic console is generally divided into two sections. The left section contains the Change Center, Domain Structure, and other informational panels. The right section displays panels containing additional options or configuration details. Note: With the exception of the Change Center and Domain Structure references, further references to WebLogic console panels refer to panels in the right section of the WebLogic console.

![](datup-version-1-0-00-003-local-install-guide/001.png)

<span id="_Ref191089515" class="anchor"></span>Figure ‑. WebLogic Console

## Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In an effort to make these installation instructions as general as possible for installation at any site, a few terms are used throughout the instructions with the intent that they be replaced with site-specific values.

Table 3‑1 contains a list of those terms used only within this document as well as sample site-specific values for each term. Additionally, references to the DATUP-L-1 server may be replaced with the site-specific name of the destination server at the installation site. <span id="_Ref176675115" class="anchor"></span>

Table ‑. Terminology

| Term                                                               | Definition                                                                                                                                                                             | Sample                                 |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Database Server                                                    | Machine on which Caché is installed and runs                                                                                                                                           | DATUP-L-1-DB                           |
| Deployment Machine                                                 | Site-specific machine on which WebLogic is installed and runs                                                                                                                          | DATUP-L-1                              |
| Deployment Server                                                  | WebLogic managed server where DATUP is deployed                                                                                                                                        | LocalPharmacyServer                    |
| Deployment Server Port                                             | Port on which the Deployment Server is listening                                                                                                                                       | 8010                                   |
| Deployment Server’s class path directory                           | Folder location on the Deployment Server where libraries on the class path are located (see WebLogic documentation for instructions on setting a WebLogic managed server’s class path) | /opt/bea/domains/PRE/lib               |
| Java Database Connectivity (JDBC) Universal Resource Locator (URL) | URL to connect to Caché database                                                                                                                                                       | jdbc:Cache://DATUP-l-1-db:1972/FDB_DIF |

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hardware requirements for DATUP are found in the DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010), which is delivered as a companion document to this Installation Guide.

The installation instructions found within this guide are intended to be performed on a clean installation of WebLogic 10.3, with a separate managed server to act as the Deployment Server. For details on completing the installation of the following items, please refer to each item’s installation and configuration documentation supplied by Oracle.

For successful deployment of the DATUP software at a site, the following assumptions must be met:

- The Deployment Server is configured and running.
- WebLogic is configured to run with the Java™ Standard Edition Development Kit, Version 1.6+.
- Access to the WebLogic console is by means of any valid administrative user name and password.
- The proper Caché database driver libraries for the chosen deployment environment are present on the class path for the respective Deployment Servers.
- Red Hat Enterprise Linux 5.2 operating system is properly installed.
- Domain Name Server (DNS) resolution is configured for the DATUP server.
- The installation instructions are followed in the order that the sections are presented within this Installation Guide.

## Database Installation and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the operating system and software for the DATUP database tier installation and configuration at a local site. Initially, install and configure the operating system software according to the manufacturer’s specifications. Then configure the Caché database as specified in the following sections for DATUP to function properly.

### Caché Features and Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDB DIF database used by DATUP at a local site requires Caché to be successfully installed. The Caché database has specific installation procedures and files for each operating system. Red Hat Linux must be successfully installed prior to installing the Caché database. A successful installation of a Caché database instance is one in which the installation guide procedures are followed, resulting in an error-free installation.

The installation of the Caché database is described in the *Caché Installation Guide*, Version 2008.2, Section 4, Installing Caché on UNIX and Linux. The standard installation should be used to install the Caché database server software.

To support the configuration of the Caché systems, the Caché Client should be installed on a Microsoft Windows<sup>®</sup> computer. The Windows client installation procedures are located in the *Caché Installation Guide*, Version 2008.2, Section 2.2.2, Caché Client Installation.

The following standard installation features are required for the DATUP system:

- Database Server Engine
- Client
- Open Database Connectivity (ODBC) Driver Components (Structured Query Language (SQL) Tools)

The following features are required to configure the Caché database for the DATUP system:

- Caché Terminal
- System Management Portal
  - Configuration
  - Security Management

The following extended Data and Application Server features of Caché are not required and were not tested with DATUP:

- Caché Relational Gateway
- Caché Scripting Language
- Class Projections
- Component Object Model Gateway
- Enterprise Caché Protocol
- Enterprise Java Beans
- Multidimensional Data Access
- Multidimensional Data Engine
- Object Data Access
- Performance Monitoring Application Programming Interface
- Transactional Bit-Map Indexing
- Unified Data Architecture
- Visual Caché

### Caché Database Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DATUP Caché database server will contain the FDB_DIF database installation. This database is the primary and only data repository for the DATUP application. Caché namespace configuration, advanced parameter configuration, and user creation topics are discussed in this section. Most database configuration tasks can be accomplished using the System Management Portal following instructions provided in the Caché documentation. For a Linux installation, the Caché Client (which can only be installed on Windows) is used to operate the System Management Portal interface remotely on the Linux server. The System Management Portal shown in Figure 3‑2 denotes the major configuration sections for Caché.

![](datup-version-1-0-00-003-local-install-guide/002.png)

<span id="_Ref205866025" class="anchor"></span>Figure ‑. Caché System Management Portal

#### Namespace Configuration

FDB_DIF namespace and directory structures must be created for the DATUP Caché database. This task is performed using the System Management Portal on the System Configuration – Namespaces page. The Caché System Administration Guide, Version 2008.2, Section 2.2, Configuring Namespaces provides instructions for creating and configuring namespaces. The required namespace information is listed in Table 3‑2.

<span id="_Ref259198676" class="anchor"></span>Table ‑. Namespace Configuration

| Namespace | Database Directory      | Default Database | Size (MB) | Note             |
|-----------|-------------------------|------------------|-----------|------------------|
| FDB_DIF   | /root/CACHE/mgr/FDB_DIF | FDB_DIF          | 1671      |                  |
| %SYS      | Cachelib                | CACHESYS         | N/A       | Standard Install |
| DOCBOOK   | docbook                 | DOCBOOK          | N/A       | Standard Install |
| SAMPLES   | samples                 | SAMPLES          | N/A       | Standard Install |
| USER      | user                    | USER             | N/A       | Standard Install |

#### Advanced Parameter Configuration

Some SQL options must be modified in order for the DATUP Caché installation to function properly. These modifications are performed via the System Management Portal on the System Configuration – SQL Settings page. The following SQL options should be modified as illustrated in Table 3‑3.

<span id="_Ref259197773" class="anchor"></span>Table ‑. Advanced Parameter Configuration

| Option                                                                              | Value          |
|-------------------------------------------------------------------------------------|----------------|
| Allow DDL DROP of Non-Existent Table                                                | Yes            |
| Allow DDL CREATE TABLE for Existing Table                                           | No             |
| Allow Create Primary Key Through DDL When Key Exists                                | No             |
| Does DDL DROP TABLE Delete the Table’s Data                                         | Yes            |
| Allow DDL ADD Foreign Key Constraints when Foreign Key Exists                       | No             |
| Are Primary Keys Created through DDL not ID Keys                                    | Yes            |
| SQL Security Enabled                                                                | Yes            |
| Perform Referential Integrity Checks on Foreign Keys for INSERT, UPDATE, and DELETE | Yes            |
| Default SQL Schema Name                                                             | \_CURRENT_USER |

Additional settings should be modified to avoid issues discovered during site testing. These modifications are performed via the System Management Portal on the System Configuration – Advanced Settings page. The options in Table 3‑4 are recommended.

<span id="_Ref271302610" class="anchor"></span>Table ‑. Advanced Settings Configuration

| Option          | Value    |
|-----------------|----------|
| GenericHeapSize | 51200    |
| LockTableSize   | 28311552 |

The memory option must also be set via the System Management Portal on the System Configuration - Memory and Startup menu. Select Manually for the Configure Memory Settings option. The memory management options in Table 3‑5 were recommended by InterSystems for the development database. The database administrator may use these memory management values or set other values as necessary to support the actual deployment hardware. When done making changes ensure that the Save button is selected.

<span id="_Ref271302703" class="anchor"></span>Table ‑. Memory Management Parameters

| Option                                        | Value     |
|-----------------------------------------------|-----------|
| Memory Allocated for Routine Cache (MB):      | 512       |
| Memory Allocated for 2KB Database Cache (MB): | 1024      |
| Memory Allocated for 8KB Database Cache (MB): | 1024      |
| Enable Long Strings                           | Unchecked |
| Super Server Port Number                      | 1972      |

#### User Creation

One user must be created within the DATUP Caché database to support DATUP. The *Caché Security Administration Guide*, Version 2008.2, Section 6.2, Creating and Editing Users can be used as a reference to add a new user. The user should be assigned all roles, SQL privileges, and SQL table permissions with the “Granted Admin” access rights to the FDB_DIF namespace. The same user is used to access the FDB_DIF namespace, create the tables, and load the FDB_DIF data. When the FDB_DIF tables and data are created via the FDB Data Updater utility, access rights and other permissions will already be assigned.

### FDB DIF Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event the FDB DIF database is not and cannot be installed on DATUP-L-1-DB, complete the following steps to install the FDB DIF data on the server running Caché. Although these installation steps are provided as an optional convenience to get the system up and running, it should be noted that this FDB installation will not contain the latest FDB information.

1.  Stop Caché.
2.  Create directory /root/CACHE/mgr/FDB_DIF.
3.  Change permissions to 777 for directory /root/CACHE/mgr/FDB_DIF.
4.  Insert the Installation Media into the PEPS-L-1-DB Server.
5.  Copy FDB_DIF_CACHE.DAT to /root/CACHE/mgr/FDB_DIF/CACHE.DAT.
6.  Start Caché.
7.  Utilizing the Caché System Management Portal, create and configure the FDB_DIF namespace to attach it to the to FDB_DIF database.

## WebLogic Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections detail the steps required to configure and deploy DATUP onto WebLogic at a local site.

### Class Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for the Caché JDBC data source to be added to the WebLogic configuration, the Caché JDBC driver must first be added to the Deployment Server’s class path. Use the JDBC driver provided within the Caché distribution and the WebLogic documentation to add the driver to the class path.

The local DATUP Enterprise Application Archive (EAR) file contains all the required libraries for the proper functioning of the application. If any other applications have been deployed to the Deployment Server, there may be conflicting third-party libraries in the Deployment Server's class path that will cause DATUP to operate differently than expected. If versions on the Deployment Server’s class path differ from those defined in the DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010), the preferred solution is to remove the library from the Deployment Server's class path. If that is not possible, replace the libraries with the DATUP versions.

### WebLogic Server Startup Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP requires additional arguments added to the WebLogic Server’s Server Start properties. This section details the steps to add the arguments to the server

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑3.

    ![](datup-version-1-0-00-003-local-install-guide/003.png)

<span id="_Ref256581857" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑4.

    ![](datup-version-1-0-00-003-local-install-guide/004.png)

<span id="_Ref256581858" class="anchor"></span>Figure ‑. Change Center

4.  Click on the server name corresponding to the deployment server in the Summary of Servers panel found in the right column of the WebLogic console. For reference, see Figure 3‑5.

    ![](datup-version-1-0-00-003-local-install-guide/005.png)

<span id="_Ref256581859" class="anchor"></span>Figure ‑. Summary of Servers

5.  WebLogic will now display the panel Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server are set. For reference, see Figure 3‑6.

    ![](datup-version-1-0-00-003-local-install-guide/006.png)

<span id="_Ref256581860" class="anchor"></span>Figure ‑. Settings for Deployment Server

6.  Click on the Server Start tab.
7.  WebLogic will now display the panel Server Start tab in the Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server are set. For reference, see Figure 3‑7.

    ![](datup-version-1-0-00-003-local-install-guide/007.png)

<span id="_Ref256581861" class="anchor"></span>Figure ‑. Server Start Tab

8.  Insert the following text in the Arguments box:

    -Xms1024m

    -Xmx1024m

    -XX:PermSize=1024m

    -XX:MaxPermSize=1024m

    -Dlog4j.logs.dir=servers/LocalPharmacyServer/logs

    -Dweblogic.JobScheduler=true

    -Dpeps.datup.configuration=/opt/fdb_datup_configuration.properties
9.  Click the Save Button
10. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑8.

    ![](datup-version-1-0-00-003-local-install-guide/008.png)

<span id="_Ref256581862" class="anchor"></span>Figure ‑. Activate Changes

### Local JDBC Data Source Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses a database connection by means of a data source to DIF in order to perform order checks. Complete the following steps to create a new connection pool and data source for DIF.

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑9.

    ![](datup-version-1-0-00-003-local-install-guide/009.png)

<span id="_Ref184087883" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑10.

    ![](datup-version-1-0-00-003-local-install-guide/010.png)

<span id="_Ref184087925" class="anchor"></span>Figure ‑. Change Center

4.  Click New found in the Summary of JDBC Data Sources panel found in the right column of the WebLogic console. For reference, see Figure 3‑11.

    ![](datup-version-1-0-00-003-local-install-guide/011.png)

<span id="_Ref181416612" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

5.  WebLogic will now display the panel Create a New JDBC Data Source in the right column of the console, where details of the new data source are set. For reference, see Figure 3‑12.

    ![](datup-version-1-0-00-003-local-install-guide/012.png)

<span id="_Ref191102359" class="anchor"></span>Figure ‑. JDBC Data Source Properties

6.  For the Name, type FDB-DIF.
7.  For the JNDI Name, type datasource/FDB-DIF.
8.  For the Database Type, select Cache.
9.  For the Database Driver, verify that Intersystems’s Cache Driver (Type 4) Versions: Any is selected.
10. Click Next.
11. WebLogic will now display the panel Transaction Options in the right column of the console, where the transaction attributes for this data source are set. For reference, see Figure 3‑13.

    ![](datup-version-1-0-00-003-local-install-guide/013.png)

<span id="_Ref191089711" class="anchor"></span>Figure ‑. Transaction Options

12. Select the Emulate Two-Phase Commit radio button.
13. Click Next.
14. WebLogic will now display the panel Connection Properties in the right column of the console, where the connection pool attributes are set. For reference, see Figure 3‑14.

    ![](datup-version-1-0-00-003-local-install-guide/014.png)

<span id="_Ref191089804" class="anchor"></span>Figure ‑. Connection Properties

15. For Database Name, type the name of the Caché database to which DATUP will connect. For example, FDB_DIF.
16. For Host Name, type the name of the machine on which Caché is running. For example, DATUP-L-1-DB.
17. For Port, type the port on which Caché is listening. For example, 1972.
18. For Database User Name, type the user to connect to the FDB database. For example, developer. The user entered should be the same as configured in Section 3.3.2.3.
19. For Password and Confirm Password, type the password for the user given previously. For example, pharmacy.
20. Click Next.
21. WebLogic will now display the panel Test Database Connection in the right column of the console, where the new data source can be tested. For reference, see Figure 3‑15.

    ![](datup-version-1-0-00-003-local-install-guide/015.png)

<span id="_Ref191089849" class="anchor"></span>Figure ‑. Test Database Connection

22. Leave all values as set by default, with the exception of Test Table Name. For this attribute, type fdb_version.
23. Click Next.
24. WebLogic will now display the panel Select Targets in the right column of the console, where the target server is selected for the new data source. For reference, see Figure 3‑16.

    ![](datup-version-1-0-00-003-local-install-guide/016.png)

<span id="_Ref191089523" class="anchor"></span>Figure ‑. Select Targets

25. Select the Deployment Server as the target. For example, LocalPharmacyServer.
26. Click Finish.
27. WebLogic will now display the panel Summary of JDBC Data Sources in the right column of the console, where the newly created data source is displayed. For reference, see Figure 3‑17.

    ![](datup-version-1-0-00-003-local-install-guide/017.png)

<span id="_Ref181418183" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

28. Prepared statement caching will need to be turned off to work around a defect in Cache. To do so, select the newly created data source, FDB-DIF, and navigate to the Connection Pool tab. Change the Statement Cache Size parameter to 0 then click save. For reference, see Figure 3‑18.

![](datup-version-1-0-00-003-local-install-guide/018.png)

<span id="_Ref258586453" class="anchor"></span>Figure ‑. Statement Cache Size Parameter

29. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑19.

    ![](datup-version-1-0-00-003-local-install-guide/019.png)

<span id="_Ref193865244" class="anchor"></span>Figure ‑. Activate Changes

### Log4j

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses Log4j to provide debug and error logs. Although the application will function without Log4j installed, using it can be helpful to troubleshoot potential issues. Because DATUP can operate without Log4j configured, all instructions within this section are only required if debugging deployed code.

If the installation of Log4j is desired, the Java Archive (JAR) can be found within the local DATUP EAR, or it can be downloaded from the Internet. Please refer to the DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010) for the version required.

To install Log4j, the Log4j JAR must be placed on the Deployment Server’s class path and the log4j.xml must be edited to include the DATUP appenders and loggers. Complete the following instructions to place the Log4j library on the Deployment Server’s class path. If Log4j is already installed on the Deployment Server, these steps do not need to be completed.

1.  Locate the Deployment Server’s Class Path Directory.
2.  Copy the log4j-1.2.15.jar file into a folder within the class path.
3.  Configure WebLogic to include the Log4j library in the Deployment Server’s class path. Please refer to the WebLogic documentation provided by BEA for completing this step.
4.  Restart the Deployment Server to load Log4j.

With Log4j installed on the Deployment Server, the log4j.xml file must be modified to include the DATUP configuration. Note that the appenders place the logs under a log folder. This folder must be created at the same directory level at which the Deployment Server is running. For example, /opt/bea/domains/PRE/log. Without this folder, Log4j will not be able to create the log files specified in the DATUP configuration. Alternatively, the file locations could be altered to be placed in a different location. Follow the steps below to complete this process:

1.  If Log4j has already been installed, locate the log4j.xml file used for the Deployment Server. Otherwise, create a new log4j.xml file that is either located in a folder on the Deployment Server class path, or use the log4j.configuration Java system property to set the location of the file. Please refer to the WebLogic provided by BEA and Log4j documentation provided by Apache to complete any of these operations.
2.  Add the following configuration to the log4j.xml file:

    \<appender name="PepsAppender" class="org.apache.log4j.RollingFileAppender"\>

    \<param name="File" value="log/peps.log"/\>

    \<param name="Append" value="false"/\>

    \<param name="MaxBackupIndex" value="10"/\>

    \<layout class="org.apache.log4j.PatternLayout"\>

    \<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c:%M\] %m%n"/\>

    \</layout\>

    \</appender\>

    \<appender name="SpringAppender" class="org.apache.log4j.RollingFileAppender"\>

    \<param name="File" value="log/spring.log"/\>

    \<param name="Append" value="false"/\>

    \<param name="MaxBackupIndex" value="10"/\>

    \<layout class="org.apache.log4j.PatternLayout"\>

    \<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c:%M\] %m%n"/\>

    \</layout\>

    \</appender\>

    \<logger name="org.springframework" additivity="false"\>

    \<level value="error" /\>

    \<appender-ref ref="SpringAppender"/\>

    \</logger\>

    \<logger name="<span class="mark">REDACTED</span>pharmacy.peps" additivity="false"\>

    \<level value="error" /\>

    \<appender-ref ref="PepsAppender"/\>

    \</logger\>
3.  If profiling is turned on and should be recorded, add the following configuration to the log4j.xml file:

    \<appender name="ProfileAppender" class="org.apache.log4j.RollingFileAppender"\>

    \<param name="File" value="log/profile.log" /\>

    \<param name="Append" value="false" /\>

    \<param name="MaxBackupIndex" value="10" /\>

    \<layout class="org.apache.log4j.PatternLayout"\>

    \<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c%M\] %m%n" /\>

    \</layout\>

    \</appender\>

    \<logger name="<span class="mark">REDACTED</span>pharmacy.peps.common.utility.profile" additivity=”false”\>

    \<level value="info" /\>

    \<appender-ref ref="ProfileAppender" /\>

    \</logger\>
4.  Restart the Deployment Server to load the Log4j configuration.

    The given Log4j configuration assumes that an existing log4j.xml file is being modified, as the configurations above are only a fragment of a complete Log4j configuration. In particular, the given configuration will only log messages for classes in the org.springframework and <span class="mark">REDACTED</span>pharmacy.peps packages and sub-packages. No other classes are covered. If additional logging is desired, other logger elements or the root element must be configured. In addition, the given Log4j configuration only logs error-level messages and optionally the info-level profiling messages. <span class="mark">REDACTED</span>

#### Local JMS Configuration

A DATUP local instance is comprised of a JMS module, including the remote JMS server to the DATUP national instance with destinations pointing to the local receive topic, the national receive queue, as well as, a connection factory. Complete the following instructions, in order by section, for each element of the local JMS configuration. These installation instructions must be repeated for each DATUP local site installation.

#### JMS Module

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑20.

    ![](datup-version-1-0-00-003-local-install-guide/020.png)

<span id="_Ref195512216" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑21.

    ![](datup-version-1-0-00-003-local-install-guide/021.png)

<span id="_Ref195512217" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑22.

    ![](datup-version-1-0-00-003-local-install-guide/022.png)

<span id="_Ref195512223" class="anchor"></span>Figure ‑. JMS Modules

5.  Click New.
6.  WebLogic will now display the panel Create JMS System Module in the right column of the console. Within the panel is The following properties will be used to identify your new module, where the new JMS module will be configured. For reference, see Figure 3‑23.

    ![](datup-version-1-0-00-003-local-install-guide/023.png)

<span id="_Ref195512238" class="anchor"></span>Figure ‑. JMS System Module Properties

7.  For Name, enter a unique name for the new JMS system module. For example, LocalPharmacyJmsModule.
8.  Leave Descriptor File Name and Location In Domain blank.
9.  Click Next.
10. WebLogic will now display the panel Create JMS System Module in the right column of the console. Within the panel is Targets, where the new JMS module will be configured. For reference, see Figure 3‑24.

    ![](datup-version-1-0-00-003-local-install-guide/024.png)

<span id="_Ref195512256" class="anchor"></span>Figure ‑. JMS System Module Targets

11. For Targets, select the Deployment Server for the DATUP local instance. For example, LocalPharmacyServer-1.
12. Click Next.
13. WebLogic will now display the panel Create JMS System Module in the right column of the console. Within the panel is Add resources to this JMS system module, where the new JMS module will be configured. For reference, see Figure 3‑25.

    ![](datup-version-1-0-00-003-local-install-guide/025.png)

<span id="_Ref195512273" class="anchor"></span>Figure ‑. Add Resources to JMS System Module

14. Leave the Would you like to add resources to this JMS system module? check box unchecked.
15. Click Finish.
16. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑26.

    ![](datup-version-1-0-00-003-local-install-guide/026.png)

<span id="_Ref195512291" class="anchor"></span>Figure ‑. Activate Changes

#### Foreign JMS Server

1.  Open and log on to the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑27.

    ![](datup-version-1-0-00-003-local-install-guide/027.png)

<span id="_Ref193978393" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑28.

    ![](datup-version-1-0-00-003-local-install-guide/028.png)

<span id="_Ref193978412" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑29.

    ![](datup-version-1-0-00-003-local-install-guide/029.png)

<span id="_Ref193978431" class="anchor"></span>Figure ‑. JMS Modules

5.  Click on the link to the JMS system module created in Section 3.4.4.1.1. For example, LocalPharmacyJmsModule.
6.  WebLogic will now display the panel Settings for LocalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑30.

    ![](datup-version-1-0-00-003-local-install-guide/030.png)

<span id="_Ref193978452" class="anchor"></span>Figure ‑. Summary of Resources

7.  Click New.
8.  WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Choose the type of resource you want to create, where the JMS module will be further configured. For reference, see Figure 3‑31.

    ![](datup-version-1-0-00-003-local-install-guide/031.png)

<span id="_Ref193981712" class="anchor"></span>Figure ‑. Choose Type of Resource to Create

9.  Select Foreign Server.
10. Click Next.
11. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Foreign Server Properties, where the JMS module will be further configured. For reference, see Figure 3‑32.

    ![](datup-version-1-0-00-003-local-install-guide/032.png)

<span id="_Ref193977655" class="anchor"></span>Figure ‑. Foreign Server Properties

12. For Name, enter a unique name for the foreign server. For example, RemoteNationalPharmacyJmsServer.
13. Click Next.
14. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Foreign Server Properties, where the JMS module will be further configured. For reference, see Figure 3‑33.

    ![](datup-version-1-0-00-003-local-install-guide/033.png)

<span id="_Ref193981734" class="anchor"></span>Figure ‑. Foreign JMS Server Target

15. For Targets, verify that the target chosen is the WebLogic server for this DATUP installation.
16. Click Finish.
17. WebLogic will now display the panel Settings for LocalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑34.

    ![](datup-version-1-0-00-003-local-install-guide/034.png)

<span id="_Ref193981761" class="anchor"></span>Figure ‑. Summary of Resources

18. Click on the link for the foreign JMS server just created. For example, RemoteNationalPharmacyJmsServer.
19. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Configuration - General, where the JMS module will be further configured. For reference, see Figure 3‑35.

    ![](datup-version-1-0-00-003-local-install-guide/035.png)

<span id="_Ref193981790" class="anchor"></span>Figure ‑. Foreign JMS Server General Configuration

20. For JNDI Connection URL, enter the URL to the National Deployment Server. For example, t3://test-datup-n:8021.
21. Leave the default values for the remaining settings JNDI Properties Credential, Confirm JNDI Properties Credential, JNDI Properties, and Default Targeting Enabled.
22. Click Save.
23. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑36.

    ![](datup-version-1-0-00-003-local-install-guide/036.png)

> <span id="_Ref193978131" class="anchor"></span>Figure ‑. Activate Changes

#### Destination

1.  Open and log on to the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑37.

    ![](datup-version-1-0-00-003-local-install-guide/037.png)

<span id="_Ref271266366" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑38.

    ![](datup-version-1-0-00-003-local-install-guide/038.png)

<span id="_Ref271266392" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑39.

    ![](datup-version-1-0-00-003-local-install-guide/039.png)

<span id="_Ref271266409" class="anchor"></span>Figure ‑. JMS Modules

5.  Click on the link to the JMS system module created in Section 3.4.4.1.1. For example, LocalPharmacyJmsModule.
6.  WebLogic will now display the panel Settings for LocalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑40.

    ![](datup-version-1-0-00-003-local-install-guide/040.png)

<span id="_Ref271266425" class="anchor"></span>Figure ‑. Summary of Resources

7.  Click on the link for the foreign JMS server created in Section 3.4.4.1.2. For example, RemoteNationalPharmacyJmsServer.
8.  WebLogic will now display the panel Settings for RemoteNationalPharmacyJms  
    Server in the right column of the console. Within the panel is Configuration - General, where the JMS module will be further configured. For reference, see Figure 3‑41.

    ![](datup-version-1-0-00-003-local-install-guide/041.png)

<span id="_Ref271266451" class="anchor"></span>Figure ‑. Foreign JMS Server General Configuration

9.  Select the Destinations tab.
10. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Foreign Destinations Configuration, where the JMS module will be further configured. For reference, see Figure 3‑42.

    ![](datup-version-1-0-00-003-local-install-guide/042.png)

<span id="_Ref271266475" class="anchor"></span>Figure ‑. Destinations

11. Click New.
12. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Foreign Connection Factory Properties, where the JMS module will be further configured. For reference, see Figure 3‑43.

    ![](datup-version-1-0-00-003-local-install-guide/043.png)

<span id="_Ref271266551" class="anchor"></span>Figure ‑. Foreign Connection Factory Properties

13. For Name, enter a unique name for the foreign JMS Destination. For example, DatupDestination
14. For Local JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/queue/national/  
    datup/receive.
15. For Remote JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/queue/national/  
    datup/receive.
16. Click OK.
17. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑44.

    ![](datup-version-1-0-00-003-local-install-guide/044.png)

<span id="_Ref271266563" class="anchor"></span>Figure ‑. Activate Changes

#### Connection Factory

1.  Open and log on to the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑45.

    ![](datup-version-1-0-00-003-local-install-guide/045.png)

<span id="_Ref193981831" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑46.

    ![](datup-version-1-0-00-003-local-install-guide/046.png)

<span id="_Ref193981847" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑47.

    ![](datup-version-1-0-00-003-local-install-guide/047.png)

<span id="_Ref193981888" class="anchor"></span>Figure ‑. JMS Modules

5.  Click on the link to the JMS system module created in Section 3.4.4.1.1. For example, LocalPharmacyJmsModule.
6.  WebLogic will now display the panel Settings for LocalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑48.

    ![](datup-version-1-0-00-003-local-install-guide/048.png)

<span id="_Ref193981910" class="anchor"></span>Figure ‑. Summary of Resources

7.  Click on the link for the foreign JMS server created in Section 3.4.4.1.2. For example, RemoteNationalPharmacyJmsServer.
8.  WebLogic will now display the panel Settings for RemoteNationalPharmacyJms  
    Server in the right column of the console. Within the panel is Configuration - General, where the JMS module will be further configured. For reference, see Figure 3‑49.

    ![](datup-version-1-0-00-003-local-install-guide/049.png)

<span id="_Ref193978585" class="anchor"></span>Figure ‑. Foreign JMS Server General Configuration

9.  Select the Connection Factories tab.
10. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Connection Factories Configuration, where the JMS module will be further configured. For reference, see Figure 3‑50.

    ![](datup-version-1-0-00-003-local-install-guide/050.png)

<span id="_Ref193979224" class="anchor"></span>Figure ‑. Foreign JMS Server Connection Factories

11. Click New.
12. WebLogic will now display the panel Settings for RemoteNationalPharmacy  
    JmsServer in the right column of the console. Within the panel is Foreign Connection Factory Properties, where the JMS module will be further configured. For reference, see Figure 3‑51.

    ![](datup-version-1-0-00-003-local-install-guide/051.png)

<span id="_Ref193979563" class="anchor"></span>Figure ‑. Foreign Connection Factory Properties

13. For Name, enter a unique name for the foreign connection factory. For example, DatupConnectionFactory.
14. For Local JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/factory.
15. For Remote JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/factory.
16. Click OK.
17. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑52.

    ![](datup-version-1-0-00-003-local-install-guide/052.png)

<span id="_Ref193979715" class="anchor"></span>Figure ‑. Activate Changes

### Site Configuration Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to filter FDB drug-drug interactions replaced by custom VA drug-drug interactions, the fdb_custom_ddimstrings FDB DIF table must be populated with a mapping between the FDB DIF interaction to be replaced and the custom VA drug-drug interaction. One attribute of this mapping is a configurable category code, with a default of FDB_ID. A file, <span class="mark">REDACTED</span>pharmacy.peps.siteConfig.properties, can be placed within a folder on the Deployment Server’s class path in order to override this default. Follow the BEA WebLogic documentation for adding folders to a server’s class path. Each property is set via a key/value pair. For example, fdb.id.category=FDB_ID, where fdb.id.category is the key and FDB_ID is the value. Table 3‑6 defines the optional property.

| Key             | Definition                                                                                                                                          | Sample |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| fdb.id.category | Category code used within the fdb_custom_ddimstrings table for mapping FDB DIF drug-drug interactions replaced by custom VA drug-drug interactions. | FDB_ID |

### DATUP Configuration Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to use the DATUP component, a configuration file must be configured for each WebLogic deployment. The location of this file was configured in Section 3.4.2 and is by default /opt/fdb_datup_configuration.properties. This file is self documenting and contains the list of configurable properties for DATUP. See Appendix A for a sample version.

### DATUP Cleanup Script

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP creates temporary zip files during the update process. A script has been provided in the /scripts/datupcleanup.sh file. This file provides a template to remove any files that DATUP creates during the update process. If the bash interpreter is not located at /bin/bash or the system’s default temporary directory is not located at /tmp, the script file must be updated, comments in the example file show which lines to change.

To automate this process using the CRON scheduler, copy the file to the /etc/cron.weekly/ directory for weekly execution. If you wish this script to run more often, it can be copied to the /etc/cron.daily/ directory for daily execution. The script must be given execution permissions, so the command chmod 755 datupcleanup.sh must also be run on the command line.

### Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the deployment of the DATUP application at a local site. Prior to completing these steps, the WebLogic class path, the WebLogic database configurations, and the Deployment Server must be restarted to load the changed configuration. Please refer to Sections 3.4.1 and 3.4.3 for instructions concerning these configuration items. Complete the following steps to deploy DATUP:

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 3‑53.

    ![](datup-version-1-0-00-003-local-install-guide/053.png)

<span id="_Ref178735721" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑54.

    ![](datup-version-1-0-00-003-local-install-guide/054.png)

<span id="_Ref181421187" class="anchor"></span>Figure ‑. Change Center

4.  Click Install found in the Deployments panel in the right column of the WebLogic console. For reference, see Figure 3‑55.

    ![](datup-version-1-0-00-003-local-install-guide/055.png)

<span id="_Ref178732223" class="anchor"></span>Figure ‑. Deployments

5.  WebLogic will now display the panel Install Application Assistant in the right column of the console, where the location of the DATUP deployment will be found. For reference, see Figure 3‑56.

    ![](datup-version-1-0-00-003-local-install-guide/056.png)

<span id="_Ref178732382" class="anchor"></span>Figure ‑. Install Application Assistant

6.  Select the DATUP deployment. If profiling should be turned on, select the  
    DATUP.Local.1.0.00.003-profile.ear file. If profiling should be turned off, select the DATUP.Local.1.0.00.003.ear file. Profiling should be turned off unless required. The remaining steps assume profiling is turned off and therefore use the DATUP. Local.1.0.00.003.ear file. Replace the release number for the current release.
    1.  If the DATUP deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the Location panel within the Install Application Assistant in the right column of the console. For reference, see Figure 3‑57.

        ![](datup-version-1-0-00-003-local-install-guide/057.png)

<span id="_Ref184090181" class="anchor"></span>Figure ‑. Locate Deployment to Install and Prepare for Deployment

2.  If the DATUP deployment has not been transferred to the Deployment Machine:
    1.  Click on the upload your file(s) link in the Install Application Assistant panel in the right section of the console. For reference, see Figure 3‑57.
    2.  Click the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
    3.  Click Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the Locate deployment to install and prepare for deployment panel within the Install Application Assistant. For reference, see Figure 3‑58.

        ![](datup-version-1-0-00-003-local-install-guide/058.png)

<span id="_Ref184090012" class="anchor"></span>Figure ‑. Upload a Deployment to the Admin Server

7.  Once the DATUP deployment is located and selected, click Next.
8.  WebLogic will now display the panel Choose targeting style within the Install Application Assistant in the right column of the console. Leave the default value selected, Install this deployment as an application, and click Next. For reference, see Figure 3‑59.

    ![](datup-version-1-0-00-003-local-install-guide/059.png)

<span id="_Ref176676787" class="anchor"></span>Figure 3‑59. Choose Targeting Style

9.  Within the Install Application Assistant in the right column of the console, WebLogic will now display the panel Select deployment targets, where the Deployment Server will be selected as the target in the next step. For reference, see Figure 3‑60.

    ![](datup-version-1-0-00-003-local-install-guide/060.png)

<span id="_Ref191090118" class="anchor"></span>Figure ‑. Select Deployment Targets

10. For the Target, select the Deployment Server. For example, LocalPharmacyServer.
11. Click Next.
12. Within the Install Application Assistant, WebLogic will now display the panel Optional Settings in the right column of the console, where the name of the deployment and the copy behavior are chosen. For reference, see Figure 3‑61.

    ![](datup-version-1-0-00-003-local-install-guide/061.png)

<span id="_Ref191090176" class="anchor"></span>Figure ‑. Optional Settings

13. Enter the Name for the deployment. For example, Local DATUP.
14. Verify that the following default option for Security is selected:

    DD Only: Use only roles and policies that are defined in the deployment descriptors.
15. Verify that the following default option for Source accessibility is selected:

    Use the defaults defined by the deployment's targets.
16. Click Next.
17. Within the Install Application Assistant in the right column of the console WebLogic will now display the panel Review your choices and click Finish, which summarizes the steps completed above. For reference, see Figure 3‑62.

    ![](datup-version-1-0-00-003-local-install-guide/062.png)

<span id="_Ref191090260" class="anchor"></span>Figure ‑. Review Your Choices and Click Finish

18. Verify that the values match those entered in Steps 6 through 17 and click Finish.
19. WebLogic will now display the panel Settings for Local DATUP, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order. For reference, see Figure 3‑63.

    ![](datup-version-1-0-00-003-local-install-guide/063.png)

<span id="_Ref191090327" class="anchor"></span>Figure ‑. Settings for DATUP

20. Leave all the values as defaulted by WebLogic and click Save.
21. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑64.

    ![](datup-version-1-0-00-003-local-install-guide/064.png)

<span id="_Ref178733999" class="anchor"></span>Figure ‑. Activate Changes

22. Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 3‑65.

    ![](datup-version-1-0-00-003-local-install-guide/065.png)

<span id="_Ref181421306" class="anchor"></span>Figure ‑. Domain Structure

23. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 3‑66.

    ![](datup-version-1-0-00-003-local-install-guide/066.png)

<span id="_Ref191090401" class="anchor"></span>Figure ‑. Summary of Deployments

24. Select the previously deployed DATUP deployment, click Start, and then select Servicing all requests from the drop-down list box.
25. WebLogic will now display the panel Start Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 3‑67.

    ![](datup-version-1-0-00-003-local-install-guide/067.png)

<span id="_Ref191090464" class="anchor"></span>Figure ‑. Start Application Assistant

26. Click Yes in the Start Application Assistant panel in the right column of the WebLogic console.
27. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 3‑68.

    ![](datup-version-1-0-00-003-local-install-guide/068.png)

<span id="_Ref191090529" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Active

28. Verify that the State of the DATUP deployment is Active.

# Upgrade Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions detail the steps required to perform an installation of a release for the DATUP software, when an existing release is already deployed at a local site. These steps assume a fresh installation has been completed, following the steps in Section 3.

## Uninstall Previous Release 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the uninstallation of the DATUP application. Prior to completing these steps, the DATUP application must have been deployed following the steps in Section 3. Complete the following steps to undeploy DATUP at a local site:

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 4‑1.

    ![](datup-version-1-0-00-003-local-install-guide/069.png)

<span id="_Ref246231865" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 4‑2.

    ![](datup-version-1-0-00-003-local-install-guide/070.png)

<span id="_Ref246231871" class="anchor"></span>Figure ‑. Change Center

4.  WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 4‑3.

    ![](datup-version-1-0-00-003-local-install-guide/071.png)

<span id="_Ref246231328" class="anchor"></span>Figure ‑. Summary of Deployments – Stopping DATUP

5.  Select the previously deployed DATUP deployment, click Stop, and then select Force Stop Now from the drop-down list box.
6.  WebLogic will now display the panel Force Stop Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 4‑4.

    ![](datup-version-1-0-00-003-local-install-guide/072.png)

<span id="_Ref246231887" class="anchor"></span>Figure ‑. Force Stop Application Assistant

7.  Click Yes in the Force Stop Application Assistant panel in the right column of the WebLogic console.
8.  WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 4‑5.

    ![](datup-version-1-0-00-003-local-install-guide/073.png)

<span id="_Ref246231898" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Prepared

9.  Verify that the State of the EDTUP deployment is Prepared.
10. Select the previously deployed EDTUP deployment, and then click Delete.
11. WebLogic will now display the panel Delete Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 4‑6.

    ![](datup-version-1-0-00-003-local-install-guide/074.png)

<span id="_Ref246231908" class="anchor"></span>Figure ‑. Delete Application Assistant

12. Click Yes in the Delete Application Assistant panel in the right column of the WebLogic console.
13. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 4‑7.

    ![](datup-version-1-0-00-003-local-install-guide/075.png)

<span id="_Ref246231916" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Deleted

14. Verify that the DATUP deployment is deleted and no longer present.
15. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 4‑8.

    ![](datup-version-1-0-00-003-local-install-guide/076.png)

<span id="_Ref246231924" class="anchor"></span>Figure ‑. Activate Changes

## Deploy New Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deploy the new release, follow the same deployment steps found in Section 3.4.6.

(This Page Intentionally Left Blank)

# System Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section will verify that the DATUP system is up and running at a local site.

## Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that a DATUP installation is up and running at a local site, navigate a web-browser to the logs directory on the server, for example, http://datup-l-1/logs/LocalDatupServer/logs.

Verify that the server.log file has an entry indicating the next scheduled run time for the DATUP application. The server.log entry looks like:

DEBUG \[<span class="mark">REDACTED</span>pharmacy.peps.updater.common.utility.DifUpdateScheduler:scheduleNextTimer\] Next scheduled DIF update time: Thu, 08/26/2010, 02:45:00 PM, CDT

This line indicates that the system is running.

(This Page Intentionally Left Blank)Appendix ALocal DATUP Configuration(This Page Intentionally Left Blank)

Local DATUP configuration

This appendix provides a configuration file example for a local site based on the baseline fdb_datup_configuration.properties file located on the delivery CD in the /configuration directory.

Example DATUP Configuration Properties for a Local Site

\###################################################

\#------------------- Scheduler -------------------

\###################################################

\###################################################

\# Scheduled nightly update time (military time).

\#

\# For example, "0230" schedules the nightly update

\# for 2:30 am.

\#

\# \*This parameter applies to National and Local.

\###################################################

scheduled.time=0230

\###################################################

\#------------------- FTP Server -------------------

\###################################################

\###################################################

\# FTP server hostname

\#

\# Specify the anonymous FTP server hostname.

\#

\# \*This parameter applies to National and Local.

\###################################################

ftp.hostname= <span class="mark">REDACTED</span>

\###################################################

\# FTP server port number

\#

\# Specify the anonymous FTP server port number.

\#

\# \*This parameter applies to National and Local.

\###################################################

ftp.port=21

\###################################################

\# FTP server username/password.

\#

\# Specify the anonymous account username/password.

\#

\# \*These parameters apply to National and Local.

\###################################################

ftp.username=PECS

ftp.password=

\###################################################

\# FTP server working directory

\#

\# Specify the FTP working directory, relative to

\# the FTP root directory.

\#

\# \*This parameter applies to National and Local.

\###################################################

ftp.directory.working=pharmacy

\###################################################

\# Pending FDB-DIF update storage directory.

\#

\# Specify the pending directory, relative to the

\# working directory, to the location where FDB-DIF

\# full, incremental, and custom ZIP files will be

\# placed for processing.

\#

\# \*This parameter applies to National.

\###################################################

ftp.directory.pending=fdb_dif

\###################################################

\#------------------- FDB DIF ---------------------

\###################################################

\###################################################

\# Number of random FDB-DIF verification tests

\#

\# Specify the number of random FDB-DIF verification

\# tests to run. 10 is a reasonable number. However,

\# do not specify a large number as it will cause an

\# unacceptable delay for processing new VistA order

\# checks during that time.

\#

\# \*This parameter applies to National and Local.

\###################################################

fdb.verification.test.count=10

\###################################################

\# Number of statements to batch before commit

\#

\# Specify the number of statements to batch before

\# a commit to the database. This value is database

\# vendor and JDBC driver dependent. A reasonable

\# batch size is 500. However, tests show that Cache

\# may throw system errors with a batch size greater

\# than 200.

\#

\# Specify a batch size of 0 to disable batching. A

\# single commit will be issued at the end of the

\# incremental update.

\#

\# \*This parameter applies to National and Local.

\###################################################

fdb.batch.commit.size=200

\###################################################

\#------------------- Email Server -----------------

\###################################################

\###################################################

\# Email server hostname

\#

\# \*This parameter applies to National and Local.

\###################################################

email.hostname=mail.<span class="mark">REDACTED</span>

\###################################################

\# Email sender name

\#

\# For example, "noreply@va.gov".

\#

\# \*This parameter applies to National and Local.

\###################################################

email.sender=noreply@<span class="mark">REDACTED</span>

\###################################################

\# Email username/password

\#

\# May be necessary to relay email.

\#

\# \*These parameters apply to National and Local.

\###################################################

email.username=

email.password=

\###################################################

\# Email list for success notifications

\#

\# Include individuals that should be notified about

\# successful FDB/FDB-Custom updates.

\#

\# \*This parameter applies to National and Local.

\###################################################

email.list.success=local_managers@<span class="mark">REDACTED</span>

\###################################################

\# Email template file for success notifications

\#

\# Specify the full path to the template file. The

\# specified template will override the default

\# template bundled with DATUP.

\#

\# \*This parameter applies to National and Local.

\###################################################

email.template.success=/opt/datup/local.success.txt

\###################################################

\# Email list for failure notifications

\#

\# Include individuals that should be notified about

\# failed FDB/FDB-Custom updates.

\#

\# \*This parameter applies to National and Local.

\###################################################

email.list.failure=local_managers@<span class="mark">REDACTED</span>

\###################################################

\#------------------- Locality -----------------

\###################################################

\###################################################

\# Regional Data Center (RDC) name

\#

\# Specify the name of the RDC or leave blank if

\# this installation is not part of a RDC.

\#

\# \*This parameter applies to Local.

\###################################################

locality.rdc.name=Sacramento

\###################################################

\# Site number(s)

\#

\# Specify the site number(s) for this installation.

\# If more than one site is associated with this

\# installation, separate the site numbers with a

\# comma (e.g., 423,512,211).

\#

\# \*This parameter applies to Local.

\###################################################

locality.site.number=600,662

(This Page Intentionally Left Blank)Appendix BCombined DATUP / PECS Architecture(This Page Intentionally Left Blank)

combined DATUP and peCs architecture

This appendix provides the combined DATUP / PECS architecture diagram for reference. The combined logical system components are:

1.  DATUP – Implements the FDB-DIF update business logic.
2.  Scheduler – Background process for scheduling DATUP.
3.  WebLogic – Application server environment.
4.  Configuration File – Defines the DATUP configuration settings.
5.  Email Templates – Templated emails for notifications sent to National/Local Managers.
6.  Anonymous FTP Server – FTP Server that hosts the FDB-DIF update archives.
7.  Email Server – Email relay server.
8.  PECS – Implements the FDB-Custom drug business logic.
9.  CT Staging Database – Stores PECS FDB-Custom modifications.
10. DATUP Database – Stores DATUP site update history.
11. FDB-DIF Database – Stores the FDB-DIF drug database.
12. Legacy VistA – Existing VistA server.

Figure B−1 illustrates the logical system components for the National and Local environments. The National components are responsible for verifying and publishing FDB-DIF and FDB-Custom updates to the Anonymous FTP Server. The Local components then consume and apply the verified updates in an automated manner.

![](datup-version-1-0-00-003-local-install-guide/077.png)

Figure B−1. Combined DATUP/PECS Architecture Diagram