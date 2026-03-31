---
title: DATUP Version 1.0.00.003 National Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: National Install Guide
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
  - national
  - weblogic
  - console
  - class
  - panel
  - install
  - version
page_count: 0
word_count: 11278
section_count: 15
table_count: 5
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/15168_datup_ign_v1-0-00-003.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/15168_datup_ign_v1-0-00-003.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=203"
---

15168-DATUP_IGN-V1.0.00.003

National DATA UPDATE (DATUP) COMPONENT

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

15168-DATUP_IGN-V1.0.00.003

National DATA UPDATE (DATUP) COMPONENT

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

Figure 3‑1. WebLogic Console [5](#_Ref191089515)

Figure 3‑2. Domain Structure [10](#_Ref256581857)

Figure 3‑3. Change Center [10](#_Ref256581858)

Figure 3‑4. Summary of Servers [11](#_Ref256581859)

Figure 3‑5. Settings for Deployment Server [11](#_Ref256581860)

Figure 3‑6. Server Start Tab [12](#_Ref256581861)

Figure 3‑7. Activate Changes [13](#_Ref256581862)

Figure 3‑8. Domain Structure [13](#_Ref256075822)

Figure 3‑9. Change Center [14](#_Ref256075845)

Figure 3‑10. Summary of JDBC Data Sources [14](#_Ref256075871)

Figure 3‑11. JDBC Data Source Properties [15](#_Ref256075905)

Figure 3‑12. Transaction Options [16](#_Ref256075927)

Figure 3‑13. Connection Properties [17](#_Ref256075948)

Figure 3‑14. Test Database Connection [18](#_Ref256076002)

Figure 3‑15. Select Targets [19](#_Ref256076023)

Figure 3‑16. Summary of JDBC Data Sources [19](#_Ref256076041)

Figure 3‑17. Activate Changes [20](#_Ref256076051)

Figure 3‑18. Domain Structure [20](#_Ref256076100)

Figure 3‑19. Change Center [21](#_Ref256076387)

Figure 3‑20. Summary of JDBC Data Sources [21](#_Ref256076397)

Figure 3‑21. JDBC Data Source Properties [22](#_Ref256076418)

Figure 3‑22. Transaction Options [23](#_Ref256076466)

Figure 3‑23. Connection Properties [24](#_Ref256076486)

Figure 3‑24. Test Database Connection [25](#_Ref256076518)

Figure 3‑25. Select Targets [26](#_Ref256076543)

Figure 3‑26. Summary of JDBC Data Sources [26](#_Ref256076562)

Figure 3‑27. Activate Changes [27](#_Ref256076600)

Figure 3‑28. Lock & Edit [30](#_Ref193872397)

Figure 3‑29. JMS Servers [30](#_Ref193873311)

Figure 3‑30. Summary of JMS Servers [31](#_Ref193872672)

Figure 3‑31. JMS Server Properties [31](#_Ref193872971)

Figure 3‑32. Select Targets [32](#_Ref193873094)

Figure 3‑33. Activate Changes [32](#_Ref193873250)

Figure 3‑34. Lock & Edit [33](#_Ref193873424)

Figure 3‑35. JMS Modules [33](#_Ref193873406)

Figure 3‑36. JMS Modules [34](#_Ref193873674)

Figure 3‑37. JMS System Module Properties [34](#_Ref193873959)

Figure 3‑38. JMS System Module Targets [35](#_Ref193874247)

Figure 3‑39. Add Resources to JMS System Module [36](#_Ref193874345)

Figure 3‑40. Activate Changes [36](#_Ref193874550)

Figure 3‑41. Lock & Edit [37](#_Ref193875670)

Figure 3‑42. JMS Modules [37](#_Ref193875685)

Figure 3‑43. JMS Modules [38](#_Ref193875701)

Figure 3‑44. Summary of Resources [39](#_Ref193875946)

Figure 3‑45. Choose Type of Resource to Create [40](#_Ref193876213)

Figure 3‑46. Connection Factory Properties [40](#_Ref193876422)

Figure 3‑47. Connection Factory Targets [41](#_Ref207613219)

Figure 3‑48. Settings for NationalPharmacyJmsModule [42](#_Ref193876648)

Figure 3‑49. DatupConnectionFactory General Configuration [42](#_Ref193876721)

Figure 3‑50. DatupConnectionFactory Transactions Configuration [43](#_Ref193876834)

Figure 3‑51. Activate Changes [43](#_Ref193877032)

Figure 3‑52. Lock & Edit [44](#_Ref193898691)

Figure 3‑53. JMS Modules [44](#_Ref193898723)

Figure 3‑54. JMS Modules [45](#_Ref193897547)

Figure 3‑55. Summary of Resources [45](#_Ref193897570)

Figure 3‑56. Choose Type of Resource to Create [46](#_Ref193897652)

Figure 3‑57. JMS Destination Properties [46](#_Ref193899254)

Figure 3‑58. Target JMS Queue [47](#_Ref193896143)

Figure 3‑59. Subdeployment Properties [47](#_Ref193896334)

Figure 3‑60. Target JMS Queue with Subdeployment [48](#_Ref193896661)

Figure 3‑61. Activate Changes [49](#_Ref193899198)

Figure 3‑62. Lock & Edit [49](#_Ref271265065)

Figure 3‑63. JMS Modules [50](#_Ref271266157)

Figure 3‑64. JMS Modules [50](#_Ref271265151)

Figure 3‑65. Module Settings [51](#_Ref256588696)

Figure 3‑66. Settings for Queue [51](#_Ref256588964)

Figure 3‑67. Delivery Failure Settings [52](#_Ref256589024)

Figure 3‑68. Activate Changes [52](#_Ref271267581)

Figure 3‑69. Lock & Edit [53](#_Ref271265223)

Figure 3‑70. JMS Modules [53](#_Ref271266187)

Figure 3‑71. JMS Modules [54](#_Ref271265263)

Figure 3‑72. Summary of Resources [54](#_Ref271265296)

Figure 3‑73. Choose Type of Resource to Create [55](#_Ref271265339)

Figure 3‑74. JMS Destination Properties [55](#_Ref271265409)

Figure 3‑75. Target JMS Topic [56](#_Ref271265440)

Figure 3‑76. Subdeployment Properties [56](#_Ref271265452)

Figure 3‑77. Target JMS Topic with Subdeployment [57](#_Ref271265482)

Figure 3‑78. Activate Changes [58](#_Ref271265509)

Figure 3‑79. Domain Structure [59](#_Ref178735721)

Figure 3‑80. Change Center [60](#_Ref181421187)

Figure 3‑81. Deployments [60](#_Ref178732223)

Figure 3‑82. Install Application Assistant [61](#_Ref178732382)

Figure 3‑83. Locate Deployment to Install and Prepare for Deployment [62](#_Ref184090181)

Figure 3‑84. Upload a Deployment to the Admin Server [63](#_Ref184090012)

Figure 3‑85. Choose Targeting Style [63](#_Ref176676787)

Figure 3‑86. Select Deployment Targets [64](#_Ref191090118)

Figure 3‑87. Optional Settings [65](#_Ref191090176)

Figure 3‑88. Review Your Choices and Click Finish [66](#_Ref191090260)

Figure 3‑89. Settings for DATUP [67](#_Ref191090327)

Figure 3‑90. Activate Changes [68](#_Ref178733999)

Figure 3‑91. Domain Structure [68](#_Ref181421306)

Figure 3‑92. Summary of Deployments [69](#_Ref191090401)

Figure 3‑93. Start Application Assistant [69](#_Ref191090464)

Figure 3‑94. Summary of Deployments – DATUP Deployment Active [70](#_Ref191090529)

Figure 4‑1. Domain Structure [71](#_Ref246231865)

Figure 4‑2. Change Center [72](#_Ref246231871)

Figure 4‑3. Summary of Deployments – Stopping DATUP [72](#_Ref246231328)

Figure 4‑4. Force Stop Application Assistant [73](#_Ref246231887)

Figure 4‑5. Summary of Deployments – DATUP Deployment Prepared [73](#_Ref246231898)

Figure 4‑6. Delete Application Assistant [74](#_Ref246231908)

Figure 4‑7. Summary of Deployments – DATUP Deployment Deleted [74](#_Ref246231916)

Figure 4‑8. Activate Changes [75](#_Ref246231924)

LIST OF TABLES

Table 3‑1. Terminology [6](#_Ref176675115)

Table 3‑2. Optional Site Configuration Properties [58](#_Ref213809714)

Appendices

Appendix A – National DATUP Configuration

Appendix B – Combined DATUP and PECS Architecture

REVISION HISTORY

| Date              | Version    | Description                                                                                        | Author |
|-------------------|------------|----------------------------------------------------------------------------------------------------|--------|
| September 3, 2010 | 1.0.00.001 | National PEDTUP Installation Guide: Initial version.                                               | SwRI   |
| October 8, 2010   | 1.0.00.001 | Renamed all instances of “PEDTUP” to “DATUP.                                                       | SwRI   |
| November 12, 2010 | 1.0.00.002 | Updated the document to address change request \#CR2942.                                           | SwRI   |
| December 3, 2010  | 1.0.00.003 | No changes since last delivery. Updated the version number to reflect the latest release of DATUP. | SwRI   |

<span id="_Ref213809714" class="anchor"></span>Table 3‑. Optional Site Configuration Properties

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
    - [Oracle Database](#oracle-database)
  - [WebLogic Installation Instructions](#weblogic-installation-instructions)
    - [Class Path](#class-path)
    - [WebLogic Server Startup Configuration](#weblogic-server-startup-configuration)
    - [National FDB-DIF Data Source Configuration](#national-fdb-dif-data-source-configuration)
    - [National JDBC DATUP Data Source Configuration](#national-jdbc-datup-data-source-configuration)
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

Southwest Research Institute<sup>®</sup> (SwRI<sup>®</sup>) is developing this Pharmacy Reengineering (PRE) and Information Technology Support Project document for the PRE project Testing Support Contract No. GS‑35F‑0533L / VA118-09-F-0003.

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

The goal for the PRE project is a seamless and integrated nationally-supported system that is an integral part of the Health*e*Vet-Veterans Health Information Systems & Technology Architecture (VistA) environment. To meet this goal, the PRE project will enhance pharmacy data exchange, as well as clinical documentation capabilities, in a truly integrated fashion to improve operating efficiency and patient safety. Additionally, it will provide a flexible technical environment to adjust to future business conditions and to meet patient needs in the clinical environment. Achieving this goal will enable resolution of current pharmacy issues, improve patient safety, and facilitate long-term process stability.

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

The information contained in this National Data Update (DATUP) Installation Guide is specific to DATUP development, which supports the MOCHA component. This section defines the layout of this document and provides an outline of the document structure.

## Document Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document details the steps required to install the DATUP software at a national site, the terminology used for the configuration and deployment of the software, and the assumptions for installing the software. Additionally, this document details how to install and configure the database environment. This document accompanies the delivery of the DATUP.v1.0.00.003 software release. The DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010) is delivered as a companion document to this Installation Guide. Refer to the Version Description Document for more information on the software inventory and versions used in the DATUP.v1.0.00.003 software release.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list provides a brief description of the sections included in this document:

Section 1: Provides introductory material delineating the purpose of the PRE project and the scope of the MOCHA effort

Section 2: Presents an overview of the layout of the document

Section 3: Presents the installation instructions for the DATUP.v1.0.00.003 software release

Section 4: Details the steps required to perform an installation when an existing version is already deployed.

Section 5: Presents verification steps to verify that the installation was successful

Text in a Courier New font indicates WebLogic Console panels or text, commands, and settings that must be typed, executed, or configured to complete the installation.

(This Page Intentionally Left Blank)

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions detail the steps required to perform a *fresh* installation of the DATUP software at a national site. For *upgrade* installation instructions see Section 4. Section 3.1 details the terminology used for the configuration and deployment of the DATUP software. Section 3.2 outlines the assumptions for installing the DATUP software. While the system may be configured to run outside the given assumptions, doing so requires modifications that are not detailed in this document. Section 3.3 describes how to install and configure the DATUP software properly. Finally, Section 3.3 describes how to install and configure the database environment.

In order to understand the installation and verification process, the reader should be familiar with the WebLogic console shown in Figure 3‑1. The WebLogic console is a Web page viewable from any Internet browser; however, Internet Explorer, Version 7, is recommended. The WebLogic console is generally divided into two sections. The left section contains the Change Center, Domain Structure, and other informational panels. The right section displays panels containing additional options or configuration details. Note: With the exception of the Change Center and Domain Structure references, further references to WebLogic console panels refer to panels in the right section of the WebLogic console.

![](datup-version-1-0-00-003-national-install-guide/001.png)

<span id="_Ref191089515" class="anchor"></span>Figure ‑. WebLogic Console

## Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In an effort to make these installation instructions as general as possible for installation at any site, a few terms are used throughout the instructions with the intent that they be replaced with site-specific values.

Table 3‑1 contains a list of those terms used only within this document as well as sample site-specific values for each term. Additionally, references to the DATUP-N server may be replaced with the site-specific name of the destination server at the installation site. <span id="_Ref176675115" class="anchor"></span>

Table ‑. Terminology

| Term                                                               | Definition                                                                                                                                                                             | Sample                                |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Database Server                                                    | Machine on which Oracle is installed and runs                                                                                                                                          | DATUP-N-DB                            |
| Deployment Machine                                                 | Site-specific machine on which WebLogic is installed and runs                                                                                                                          | DATUP-N                               |
| Deployment Server                                                  | WebLogic managed server where DATUP is deployed                                                                                                                                        | NationalPharmacyServer                |
| Deployment Server Port                                             | Port on which the Deployment Server is listening                                                                                                                                       | 8010                                  |
| Deployment Server’s class path directory                           | Folder location on the Deployment Server where libraries on the class path are located (see WebLogic documentation for instructions on setting a WebLogic managed server’s class path) | /opt/bea/domains/PRE/lib              |
| Java Database Connectivity (JDBC) Universal Resource Locator (URL) | URL to connect to Oracle database                                                                                                                                                      | jdbc:Oracle://DATUP-N-db:1972/FDB_DIF |

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hardware requirements for DATUP are found in the DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010), which is delivered as a companion document to this Installation Guide.

The installation instructions found within this guide are intended to be performed on a clean installation of WebLogic 10.3, with a separate managed server to act as the Deployment Server. For details on completing the installation of the following items, please refer to each item’s installation and configuration documentation supplied by Oracle.

For successful deployment of the DATUP software at a national site, the following assumptions must be met:

- The Deployment Server is configured and running.
- WebLogic is configured to run with the Java™ Standard Edition Development Kit, Version 1.6+.
- Access to the WebLogic console is by means of any valid administrative user name and password.
- The proper Oracle database driver libraries for the chosen deployment environment are present on the class path for the respective Deployment Servers.
- Red Hat Enterprise Linux 5.2 operating system is properly installed.
- Domain Name Server (DNS) resolution is configured for the DATUP server.
- The installation instructions are followed in the order that the sections are presented within this Installation Guide.

## Database Installation and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the operating system and software for the DATUP database tier installation and configuration. Initially, install and configure the operating system software according to the manufacturer’s specifications. Then configure the Oracle databases as specified in the following sections for DATUP to function properly.

### Oracle Database 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DATUP database is designed to be operating system independent. The only constraint is that Oracle 10g Enterprise Edition – Production must be properly installed and configured. The following sections describe the installation, features, user creation, and configuration for the Oracle database.

#### Oracle Installation

A proper installation of the Oracle Relational Database Management System (RDBMS) is one in which the Oracle Universal Installer was used to perform an error-free installation and a general purpose instance was created. A properly configured Oracle RDBMS is one in which the associated Oracle application development and configuration tools, namely SQL\*Plus and Oracle Enterprise Manager, can be used to connect to the instance through Transparent Network Substrate alias.

#### Oracle Schema Creation for DATUP

SQL scripts are provided in the database/oracle_scripts.zip file to create the following named users:

- DATUP – Owner of the DATUP schema. The default scripted password is “DATUP”, which may be changed in the 1_CreateDatupSchema.sql script prior to installation. The script should be loaded as SYSTEM, or a user with account creation privileges.
- DATUP_APP_USER – Application user with read/update/delete access granted to the tables in the DATUP schema. The default scripted password is “DATUP_APP_USER”, which may be changed in the 3_CreateDatupAppUser.sql script prior to installation. The script should be loaded as SYSTEM, or a user with account creation privileges.  
    
  The chosen DATUP_APP_USER password must match the password used to configure the JDBC data sources in Section 3.4.4.

The default scripted DATUP tablespace path is /home/oracle/datup.dbf, which may be changed in the 1_CreateDatupSchema.sql script prior to installation.

The 2_CreateDatupTables.sql script creates the DATUP tables, sequences, triggers, and indices. The script should be loaded as DATUP, the schema owner.

The script execution order is:

- 1_CreateDatupSchema.sql (SYSTEM)
- 2_CreateDatupTables.sql (DATUP)
- 3_CreateDatupAppUser.sql (SYSTEM)

An example command line (SQL Plus) user/schema execution is provided in Oracle Installation.txt.

#### Oracle Configuration and Data Load

The DATUP Oracle Database is the primary data repository for the DATUP application on the National DATUP instance. The database should be installed and configured appropriately for the DATUP operating environment. Please refer to the PECS install guide for installing the FDB_DIF database. The FDB_DIF tables may be populated using the installation and update instructions available in the *FDB Data Updater Software Users Guide*.

The initial data load of VA Local Site data must be loaded for the national DATUP instance to function. The data can be loaded with the SQL Loader scripts provided in the database/oracle_scripts.zip file. The Sites.ctl file describes the data and the Sites.csv file contains the comma-delimited Site records. The data should be loaded as DATUP_APP_USER. An example command line load (SQL Loader) is provided in Oracle Installation.txt.

The DATUP database will need to be updated if a new local site has been brought online since the original DATUP delivery date of March 17, 2010 and is not included in the Sites.csv spreadsheet. To update the Site table, login to the database as user DATUP_APP_USER. A new row must be added to the Site table for each local site added since the system was first brought online. The site table contains three columns, a unique SITE_ID, a descriptive SITE_NAME, and the Veterans Integrated Service Network (VISN) VISN number. To update this table, execute a statement such as INSERT INTO SITE VALUES (999, 'Example Medical Center', 23) for each new site brought online.

#### Oracle Database Parameters

The following Oracle database parameters are recommended for the DATUP application:

- NLS language = American
- NLS territory = America
- Character set = WE8ISO8859P1

## WebLogic Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections detail the steps required to configure and deploy DATUP onto WebLogic at a national site.

### Class Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The national DATUP Enterprise Application Archive (EAR) file contains all the required libraries for the proper functioning of the application. If any other applications have been deployed to the Deployment Server, there may be conflicting third-party libraries in the Deployment Server's class path that will cause DATUP to operate differently than expected. If versions on the Deployment Server’s class path differ from those defined in the DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010), the preferred solution is to remove the library from the Deployment Server's class path. If that is not possible, replace the libraries with the DATUP versions.

### WebLogic Server Startup Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP requires additional arguments added to the WebLogic Server’s Server Start properties. This section details the steps to add the arguments to the server

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑2.

    ![](datup-version-1-0-00-003-national-install-guide/002.png)

<span id="_Ref256581857" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑3.

    ![](datup-version-1-0-00-003-national-install-guide/003.png)

<span id="_Ref256581858" class="anchor"></span>Figure ‑. Change Center

4.  Click on the server name corresponding to the deployment server in the Summary of Servers panel found in the right column of the WebLogic console. For reference, see Figure 3‑4.

    ![](datup-version-1-0-00-003-national-install-guide/004.png)

<span id="_Ref256581859" class="anchor"></span>Figure ‑. Summary of Servers

5.  WebLogic will now display the panel Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server are set. For reference, see Figure 3‑5.

    ![](datup-version-1-0-00-003-national-install-guide/005.png)

<span id="_Ref256581860" class="anchor"></span>Figure ‑. Settings for Deployment Server

6.  Click on the Server Start tab.
7.  WebLogic will now display the panel Server Start tab in the Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server is set. For reference, see Figure 3‑6.

    ![](datup-version-1-0-00-003-national-install-guide/006.png)

<span id="_Ref256581861" class="anchor"></span>Figure ‑. Server Start Tab

8.  Insert the following text in the Arguments box:

    -Xms1024m

    -Xmx1024m

    -XX:PermSize=1024m

    -XX:MaxPermSize=1024m

    -Dlog4j.logs.dir=servers/NationalPharmacyServer/logs

    -Dweblogic.JobScheduler=true

    -Dpeps.datup.configuration=/opt/fdb_datup_configuration.properties
9.  Click the Save Button
10. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑7.

    ![](datup-version-1-0-00-003-national-install-guide/007.png)

<span id="_Ref256581862" class="anchor"></span>Figure ‑. Activate Changes

### National FDB-DIF Data Source Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses two database connections by means of a data source to DIF in order to perform FDB updates. Complete the following steps to create a new connection pool and data source for DIF.

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑8.

    ![](datup-version-1-0-00-003-national-install-guide/008.png)

<span id="_Ref256075822" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑9.

    ![](datup-version-1-0-00-003-national-install-guide/009.png)

<span id="_Ref256075845" class="anchor"></span>Figure ‑. Change Center

4.  Click New found in the Summary of JDBC Data Sources panel found in the right column of the WebLogic console. For reference, see Figure 3‑10.

    ![](datup-version-1-0-00-003-national-install-guide/010.png)

<span id="_Ref256075871" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

5.  WebLogic will now display the panel Create a New JDBC Data Source in the right column of the console, where details of the new data source are set. For reference, see Figure 3‑11.

    ![](datup-version-1-0-00-003-national-install-guide/011.png)

<span id="_Ref256075905" class="anchor"></span>Figure ‑. JDBC Data Source Properties

6.  For the Name, type FDB-DIF.
7.  For the JNDI Name, type datasource/FDB-DIF.
8.  For the Database Type, select Oracle.
9.  For the Database Driver, verify that Oracle’s Drive (Thin) Versions:9.0.1, 9.2.0, 10, 11 is selected.
10. Click Next.
11. WebLogic will now display the panel Transaction Options in the right column of the console, where the transaction attributes for this data source are set. For reference, see Figure 3‑12.

    ![](datup-version-1-0-00-003-national-install-guide/012.png)

<span id="_Ref256075927" class="anchor"></span>Figure ‑. Transaction Options

12. Select the Emulate Two-Phase Commit radio button.
13. Click Next.
14. WebLogic will now display the panel Connection Properties in the right column of the console, where the connection pool attributes are set. For reference, see Figure 3‑13.

    ![](datup-version-1-0-00-003-national-install-guide/013.png)

<span id="_Ref256075948" class="anchor"></span>Figure ‑. Connection Properties

15. For Database Name, type the name of the Oracle database to which DATUP will connect. For example, FDB_DI
16. For Host Name, type the name of the machine on which Oracle is running. For example, <span class="mark">REDACTED</span>.
17. For Port, type the port on which Oracle is listening. For example, 1521.
18. For Database User Name, type the user to connect to the FDB database. For example, FDB-DIF. The user entered should be the same as configured in Section 3.3.1.3
19. For Password and Confirm Password, type the password for the user given previously. For example, FDB-DIF.
20. Click Next.
21. WebLogic will now display the panel Test Database Connection in the right column of the console, where the new data source can be tested. For reference, see Figure 3‑14.

    ![](datup-version-1-0-00-003-national-install-guide/014.png)

<span id="_Ref256076002" class="anchor"></span>Figure ‑. Test Database Connection

22. Leave all values as set by default, with the exception of Test Table Name. For this attribute, type fdb_version.
23. Click Next.
24. WebLogic will now display the panel Select Targets in the right column of the console, where the target server is selected for the new data source. For reference, see Figure 3‑15.

    ![](datup-version-1-0-00-003-national-install-guide/015.png)

<span id="_Ref256076023" class="anchor"></span>Figure ‑. Select Targets

25. Select the Deployment Server as the target. For example, NationalPharmacyServer.
26. Click Finish.
27. WebLogic will now display the panel Summary of JDBC Data Sources in the right column of the console, where the newly created data source is displayed. For reference, see Figure 3‑16.

    ![](datup-version-1-0-00-003-national-install-guide/016.png)

<span id="_Ref256076041" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

28. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑17.

    ![](datup-version-1-0-00-003-national-install-guide/017.png)

<span id="_Ref256076051" class="anchor"></span>Figure ‑. Activate Changes

### National JDBC DATUP Data Source Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses two database connections by means of a data source to perform the automated DATUP update process. Complete the following steps to create a new connection pool and data source for DIF.

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑18.

    ![](datup-version-1-0-00-003-national-install-guide/018.png)

<span id="_Ref256076100" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑19.

    ![](datup-version-1-0-00-003-national-install-guide/019.png)

<span id="_Ref256076387" class="anchor"></span>Figure ‑. Change Center

4.  Click New found in the Summary of JDBC Data Sources panel found in the right column of the WebLogic console. For reference, see Figure 3‑20.

    ![](datup-version-1-0-00-003-national-install-guide/020.png)

> <span id="_Ref256076397" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

5.  WebLogic will now display the panel Create a New JDBC Data Source in the right column of the console, where details of the new data source are set. For reference, see Figure 3‑21.

    ![](datup-version-1-0-00-003-national-install-guide/021.png)

<span id="_Ref256076418" class="anchor"></span>Figure ‑. JDBC Data Source Properties

6.  For the Name, type DATUP.
7.  For the JNDI Name, type datasource/DATUP.
8.  For the Database Type, select Oracle.
9.  For the Database Driver, verify that Oracle’s Drive (Thin) Versions:9.0.1, 9.2.0, 10, 11 is selected.
10. Click Next.
11. WebLogic will now display the panel Transaction Options in the right column of the console, where the transaction attributes for this data source are set. For reference, see Figure 3‑22.

    ![](datup-version-1-0-00-003-national-install-guide/022.png)

<span id="_Ref256076466" class="anchor"></span>Figure ‑. Transaction Options

12. Select the Emulate Two-Phase Commit radio button
13. Click Next.
14. WebLogic will now display the panel Connection Properties in the right column of the console, where the connection pool attributes are set. For reference, see Figure 3‑23.

    ![](datup-version-1-0-00-003-national-install-guide/023.png)

<span id="_Ref256076486" class="anchor"></span>Figure ‑. Connection Properties

15. For Database Name, type the name of the Oracle database to which DATUP will connect. For example, DATUP
16. For Host Name, type the name of the machine on which Oracle is running. For example, XXXXXXXXXX.
17. For Port, type the port on which Oracle is listening. For example, 1521.
18. For Database User Name, type the user to connect to the FDB database. For example, DATUP. The user entered should be the same as configured in Section 3.3.1.2
19. For Password and Confirm Password, type the password for the user given previously. For example, DATUP.
20. Click Next.
21. WebLogic will now display the panel Test Database Connection in the right column of the console, where the new data source can be tested. For reference, see Figure 3‑24.

    ![](datup-version-1-0-00-003-national-install-guide/024.png)

<span id="_Ref256076518" class="anchor"></span>Figure ‑. Test Database Connection

22. Leave all values as set by default.
23. Click Next.
24. WebLogic will now display the panel Select Targets in the right column of the console, where the target server is selected for the new data source. For reference, see Figure 3‑25.

    ![](datup-version-1-0-00-003-national-install-guide/025.png)

<span id="_Ref256076543" class="anchor"></span>Figure ‑. Select Targets

25. Select the Deployment Server as the target. For example, NationalPharmacyServer.
26. Click Finish.
27. WebLogic will now display the panel Summary of JDBC Data Sources in the right column of the console, where the newly created data source is displayed. For reference, see Figure 3‑26.

    ![](datup-version-1-0-00-003-national-install-guide/026.png)

<span id="_Ref256076562" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

28. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑27.

    ![](datup-version-1-0-00-003-national-install-guide/027.png)

<span id="_Ref256076600" class="anchor"></span>Figure ‑. Activate Changes

### Log4j

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses Log4j to provide debug and error logs. Although the application will function without Log4j installed, using it can be helpful to troubleshoot potential issues. Because DATUP can operate without Log4j configured, all instructions within this section are only required if debugging deployed code.

If the installation of Log4j is desired, the Java Archive (JAR) can be found within the national DATUP EAR, or it can be downloaded from the Internet. Please refer to the DATUP Version Description Document (Version 1.0.00.003, dated December 3, 2010) for the version required.

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

    \<logger name="gov.va.med.pharmacy.peps" additivity="false"\>

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

    \<logger name="gov.va.med.pharmacy.peps.common.utility.profile" additivity=”false”\>

    \<level value="info" /\>

    \<appender-ref ref="ProfileAppender" /\>

    \</logger\>
4.  Restart the Deployment Server to load the Log4j configuration.

    The given Log4j configuration assumes that an existing log4j.xml file is being modified, as the configurations above are only a fragment of a complete Log4j configuration. In particular, the given configuration will only log messages for classes in the org.springframework and gov.va.med.pharmacy.peps packages and sub-packages. No other classes are covered. If additional logging is desired, other logger elements or the root element must be configured. In addition, the given Log4j configuration only logs error-level messages and optionally the info-level profiling messages. For further information, reference <http://wiki.apache.org/logging-log4j/Log4jXmlFormat>.

#### National JMS Configuration

The national DATUP instance is comprised of a JMS server and a JMS module including a connection factory, JMS template, and national receive queue. Complete the following instructions, in order by section, for each element of the National JMS configuration.

#### JMS Server

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑28.

    ![](datup-version-1-0-00-003-national-install-guide/028.png)

<span id="_Ref193872397" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Servers node. For reference, see Figure 3‑29.

    ![](datup-version-1-0-00-003-national-install-guide/029.png)

<span id="_Ref193873311" class="anchor"></span>Figure ‑. JMS Servers

4.  WebLogic will now display the panel Summary of JMS Servers in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑30.

    ![](datup-version-1-0-00-003-national-install-guide/030.png)

<span id="_Ref193872672" class="anchor"></span>Figure ‑. Summary of JMS Servers

5.  Click New.
6.  WebLogic will now display the panel Create a New JMS Server in the right column of the console. Within the panel is the JMS Server Properties, where the new JMS server will be configured. For reference, see Figure 3‑31.

    ![](datup-version-1-0-00-003-national-install-guide/031.png)

<span id="_Ref193872971" class="anchor"></span>Figure ‑. JMS Server Properties

7.  For the Name, enter a unique name for the new JMS server. For example, NationalPharmacyJmsServer.
8.  Verify that the following default option for Persistent Store is selected: (none)
9.  Click Next.
10. WebLogic will now display the panel Create a New JMS Server in the right column of the console. Within the panel is Select targets, where the new JMS server will be configured. For reference, see Figure 3‑32.

    ![](datup-version-1-0-00-003-national-install-guide/032.png)

<span id="_Ref193873094" class="anchor"></span>Figure ‑. Select Targets

11. For the Target, select the Deployment Server for the national DATUP instance. For example, NationalPharmacyServer.
12. Click Finish.
13. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑33.

    ![](datup-version-1-0-00-003-national-install-guide/033.png)

<span id="_Ref193873250" class="anchor"></span>Figure ‑. Activate Changes

#### JMS Module

1.  Open and log onto the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑34.

    ![](datup-version-1-0-00-003-national-install-guide/034.png)

<span id="_Ref193873424" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑35.

    ![](datup-version-1-0-00-003-national-install-guide/035.png)

<span id="_Ref193873406" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑36.

    ![](datup-version-1-0-00-003-national-install-guide/036.png)

<span id="_Ref193873674" class="anchor"></span>Figure ‑. JMS Modules

5.  Click New.
6.  WebLogic will now display the panel Create JMS System Module in the right column of the console. Within the panel is The following properties will be used to identify your new module, where the new JMS module will be configured. For reference, see Figure 3‑37.

    ![](datup-version-1-0-00-003-national-install-guide/037.png)

<span id="_Ref193873959" class="anchor"></span>Figure ‑. JMS System Module Properties

7.  For Name, enter a unique name for the new JMS system module. For example, NationalPharmacyJmsModule.
8.  Leave Descriptor File Name and Location In Domain blank.
9.  Click Next.
10. WebLogic will now display the panel Create JMS System Module in the right column of the console. Within the panel is Targets, where the new JMS module will be configured. For reference, see Figure 3‑38.

    ![](datup-version-1-0-00-003-national-install-guide/038.png)

<span id="_Ref193874247" class="anchor"></span>Figure ‑. JMS System Module Targets

11. For Targets, select the Deployment Server for the national DATUP instance. For example, NationalPharmacyServer.
12. Click Next.
13. WebLogic will now display the panel Create JMS System Module in the right column of the console. Within the panel is Add resources to this JMS system module, where the new JMS module will be configured. For reference, see Figure 3‑39.

    ![](datup-version-1-0-00-003-national-install-guide/039.png)

<span id="_Ref193874345" class="anchor"></span>Figure ‑. Add Resources to JMS System Module

14. Leave the Would you like to add resources to this JMS system module? check box unchecked.
15. Click Finish.
16. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑40.

    ![](datup-version-1-0-00-003-national-install-guide/040.png)

<span id="_Ref193874550" class="anchor"></span>Figure ‑. Activate Changes

#### Connection Factory

1.  Open and log onto the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑41.

    ![](datup-version-1-0-00-003-national-install-guide/041.png)

<span id="_Ref193875670" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑42.

    ![](datup-version-1-0-00-003-national-install-guide/042.png)

<span id="_Ref193875685" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑43.

    ![](datup-version-1-0-00-003-national-install-guide/043.png)

<span id="_Ref193875701" class="anchor"></span>Figure ‑. JMS Modules

5.  Click on the link to the JMS system module created in Section 3.4.5.1.2. For example, NationalPharmacyJmsModule.
6.  WebLogic will now display the panel Settings for NationalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑44.

    ![](datup-version-1-0-00-003-national-install-guide/044.png)

<span id="_Ref193875946" class="anchor"></span>Figure ‑. Summary of Resources

7.  Click New.
8.  WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Choose the type of resource you want to create, where the JMS module will be further configured. For reference, see Figure 3‑45.

    ![](datup-version-1-0-00-003-national-install-guide/045.png)

<span id="_Ref193876213" class="anchor"></span>Figure ‑. Choose Type of Resource to Create

9.  Select Connection Factory.
10. Click Next.
11. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Connection Factory Properties, where the JMS module will be further configured. For reference, see Figure 3‑46.

    ![](datup-version-1-0-00-003-national-install-guide/046.png)

<span id="_Ref193876422" class="anchor"></span>Figure ‑. Connection Factory Properties

12. For Name, enter a unique name for the connection factory. For example, DatupConnectionFactory.
13. For JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/factory.
14. Click Next.
15. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Connection Factory Targets, where the JMS module will be further configured. For reference, see Figure 3‑47.

    ![](datup-version-1-0-00-003-national-install-guide/047.png)

<span id="_Ref207613219" class="anchor"></span>Figure ‑. Connection Factory Targets

16. Verify that the selected Targets match the National Deployment Server.
17. Click Finish.
18. WebLogic will now display the panel Settings for NationalPharmacyJmsModule in the right column of the console. Within the panel is Connection Factory Configuration, where the JMS module will be further configured. For reference, see Figure 3‑48.

    ![](datup-version-1-0-00-003-national-install-guide/048.png)

<span id="_Ref193876648" class="anchor"></span>Figure ‑. Settings for NationalPharmacyJmsModule

19. Click on the link for the JMS connection factory created. For example, DatupConnectionFactory.
20. WebLogic will now display the panel Settings for DatupConnectionFactory in the right column of the console. Within the panel is Configuration - General, where the JMS module will be further configured. For reference, see Figure 3‑49.

    ![](datup-version-1-0-00-003-national-install-guide/049.png)

<span id="_Ref193876721" class="anchor"></span>Figure ‑. DatupConnectionFactory General Configuration

21. Select the Transactions tab.
22. WebLogic will now display the panel Settings for DatupConnectionFactory in the right column of the console. Within the panel is Transactions within the Configuration tab, where the JMS module will be further configured. For reference, see Figure 3‑50.

    ![](datup-version-1-0-00-003-national-install-guide/050.png)

<span id="_Ref193876834" class="anchor"></span>Figure ‑. DatupConnectionFactory Transactions Configuration

23. Check the XA Connection Factory Enabled check box.
24. Click Save.
25. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑51.

    ![](datup-version-1-0-00-003-national-install-guide/051.png)

<span id="_Ref193877032" class="anchor"></span>Figure ‑. Activate Changes

#### JMS Message Queue

1.  Open and log on to the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑52.

    ![](datup-version-1-0-00-003-national-install-guide/052.png)

<span id="_Ref193898691" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑53.

    ![](datup-version-1-0-00-003-national-install-guide/053.png)

<span id="_Ref193898723" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑54.

    ![](datup-version-1-0-00-003-national-install-guide/054.png)

<span id="_Ref193897547" class="anchor"></span>Figure ‑. JMS Modules

5.  Click on the link to the JMS system module created in Section 3.4.5.1.2. For example, NationalPharmacyJmsModule.
6.  WebLogic will now display the panel Settings for NationalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑55.

    ![](datup-version-1-0-00-003-national-install-guide/055.png)

<span id="_Ref193897570" class="anchor"></span>Figure ‑. Summary of Resources

7.  Click New.
8.  WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Choose the type of resource you want to create, where the JMS module will be further configured. For reference, see Figure 3‑56.

    ![](datup-version-1-0-00-003-national-install-guide/056.png)

<span id="_Ref193897652" class="anchor"></span>Figure ‑. Choose Type of Resource to Create

9.  Select Queue.
10. Click Next.
11. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is JMS Destination Properties, where the JMS module will be further configured. For reference, see Figure 3‑57.

    ![](datup-version-1-0-00-003-national-install-guide/057.png)

<span id="_Ref193899254" class="anchor"></span>Figure ‑. JMS Destination Properties

12. For Name, enter DatupNationalQueue.
13. For JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/queue/national/datup/receive.
14. For Template, select None.
15. Click Next.
16. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is The following properties will be used to target your new JMS system module resource, where the JMS module will be further configured. For reference, see Figure 3‑58.

    ![](datup-version-1-0-00-003-national-install-guide/058.png)

<span id="_Ref193896143" class="anchor"></span>Figure ‑. Target JMS Queue

17. Click Create a New Subdeployment.
18. WebLogic will now display the panel Create a New Subdeployment in the right column of the console. Within the panel is Subdeployment Properties, where the JMS module will be further configured. For reference, see Figure 3‑59.

    ![](datup-version-1-0-00-003-national-install-guide/059.png)

<span id="_Ref193896334" class="anchor"></span>Figure ‑. Subdeployment Properties

19. For Subdeployment Name, enter DatupQueue.
20. Click OK.
21. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is The following properties will be used to target your new JMS system module resource, where the JMS module will be further configured. For reference, see Figure 3‑60.

    ![](datup-version-1-0-00-003-national-install-guide/060.png)

<span id="_Ref193896661" class="anchor"></span>Figure ‑. Target JMS Queue with Subdeployment

22. For Subdeployments, verify that the subdeployment just created is selected. For example, NationalPharmacySubdeployment.
23. For Targets, verify that the JMS server created in Section 3.4.5.1.1 is selected. For example, NationalDatup.
24. Click Finish.
25. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑61.

    ![](datup-version-1-0-00-003-national-install-guide/061.png)

<span id="_Ref193899198" class="anchor"></span>Figure 3‑61. Activate Changes

26. Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑62.

    ![](datup-version-1-0-00-003-national-install-guide/062.png)

<span id="_Ref271265065" class="anchor"></span>Figure ‑. Lock & Edit

27. Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑63.

    ![](datup-version-1-0-00-003-national-install-guide/063.png)

<span id="_Ref271266157" class="anchor"></span>Figure ‑. JMS Modules

28. WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑64.

    ![](datup-version-1-0-00-003-national-install-guide/064.png)

<span id="_Ref271265151" class="anchor"></span>Figure ‑. JMS Modules

29. Click on the link to the JMS system module created in Section 3.4.5.1.2. For example, NationalPharmacyJmsModule.
30. WebLogic will now display the panel Settings for NationalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑65

![](datup-version-1-0-00-003-national-install-guide/065.png)

<span id="_Ref256588696" class="anchor"></span>Figure ‑. Module Settings

31. Click on the DatupQueue that was just created
32. WebLogic will now display the Settings for DatupQueue in the right column of the console, where the Queue will be configured more. For Reference, see Figure 3‑66.

    ![](datup-version-1-0-00-003-national-install-guide/066.png)

<span id="_Ref256588964" class="anchor"></span>Figure ‑. Settings for Queue

33. Click on the Delivery Failure Tab.
34. WebLogic will display the Delivery Failure settings in the right column of the console, for reference see Figure 3‑67

    ![](datup-version-1-0-00-003-national-install-guide/067.png)

<span id="_Ref256589024" class="anchor"></span>Figure ‑. Delivery Failure Settings

35. Set the Redelivery Limit to 0
36. Click Save
37. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑68.

    ![](datup-version-1-0-00-003-national-install-guide/068.png)

<span id="_Ref271267581" class="anchor"></span>Figure 3‑68. Activate Changes

#### JMS Message Topic

1.  Open and log on to the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑69.

    ![](datup-version-1-0-00-003-national-install-guide/069.png)

<span id="_Ref271265223" class="anchor"></span>Figure ‑. Lock & Edit

3.  Within the Domain Structure panel in the left column of the WebLogic console, click the Services \> Messaging \> JMS Modules node. For reference, see Figure 3‑70.

    ![](datup-version-1-0-00-003-national-install-guide/070.png)

<span id="_Ref271266187" class="anchor"></span>Figure ‑. JMS Modules

4.  WebLogic will now display the panel JMS Modules in the right column of the console, where the currently configured JMS servers will be found. For reference, see Figure 3‑71.

    ![](datup-version-1-0-00-003-national-install-guide/071.png)

<span id="_Ref271265263" class="anchor"></span>Figure ‑. JMS Modules

5.  Click on the link to the JMS system module created in Section 3.4.5.1.2. For example, NationalPharmacyJmsModule.
6.  WebLogic will now display the panel Settings for NationalPharmacyJmsModule in the right column of the console. Within the panel is Summary of Resources, where the JMS module will be further configured. For reference, see Figure 3‑72.

    ![](datup-version-1-0-00-003-national-install-guide/072.png)

<span id="_Ref271265296" class="anchor"></span>Figure ‑. Summary of Resources

7.  Click New.
8.  WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is Choose the type of resource you want to create, where the JMS module will be further configured. For reference, see Figure 3‑73.

    ![](datup-version-1-0-00-003-national-install-guide/073.png)

<span id="_Ref271265339" class="anchor"></span>Figure ‑. Choose Type of Resource to Create

9.  Select Topic.
10. Click Next.
11. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is JMS Destination Properties, where the JMS module will be further configured. For reference, see Figure 3‑74.

    ![](datup-version-1-0-00-003-national-install-guide/074.png)

<span id="_Ref271265409" class="anchor"></span>Figure ‑. JMS Destination Properties

12. For Name, enter ExternalDatupTopic.
13. For JNDI Name, enter: jms/gov/va/med/pharmacy/peps/messagingservice/topic/external/datup.
14. For Template, select None.
15. Click Next.
16. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is The following properties will be used to target your new JMS system module resource, where the JMS module will be further configured. For reference, see Figure 3‑75.

    ![](datup-version-1-0-00-003-national-install-guide/075.png)

<span id="_Ref271265440" class="anchor"></span>Figure ‑. Target JMS Topic

17. Click Create a New Subdeployment.
18. WebLogic will now display the panel Create a New Subdeployment in the right column of the console. Within the panel is Subdeployment Properties, where the JMS module will be further configured. For reference, see Figure 3‑76.

    ![](datup-version-1-0-00-003-national-install-guide/076.png)

<span id="_Ref271265452" class="anchor"></span>Figure ‑. Subdeployment Properties

19. For Subdeployment Name, enter DatupQueue.
20. Click OK.
21. WebLogic will now display the panel Create a New JMS System Module Resource in the right column of the console. Within the panel is The following properties will be used to target your new JMS system module resource, where the JMS module will be further configured. For reference, see Figure 3‑77.

    ![](datup-version-1-0-00-003-national-install-guide/077.png)

<span id="_Ref271265482" class="anchor"></span>Figure ‑. Target JMS Topic with Subdeployment

22. For Subdeployments, verify that the subdeployment just created is selected. For example, ExternalDatupTopic.
23. For Targets, verify that the JMS server created in Section 3.4.5.1.1 is selected. For example, NationalDatup.
24. Click Finish.
25. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑78.

    ![](datup-version-1-0-00-003-national-install-guide/078.png)

> <span id="_Ref271265509" class="anchor"></span>Figure 3‑78. Activate Changes

26. Additional configuration for the topic may be needed for the consuming application of this topic, please consult the user guide of any external application that uses this message topic for any information on those settings.

### Site Configuration Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to filter FDB drug-drug interactions replaced by custom VA drug-drug interactions, the fdb_custom_ddimstrings FDB DIF table must be populated with a mapping between the FDB DIF interaction to be replaced and the custom VA drug-drug interaction. One attribute of this mapping is a configurable category code, with a default of FDB_ID. A file, gov.va.med.pharmacy.peps.siteConfig.properties, can be placed within a folder on the Deployment Server’s class path in order to override this default. Follow the BEA WebLogic documentation for adding folders to a server’s class path. Each property is set via a key/value pair. For example, fdb.id.category=FDB_ID, where fdb.id.category is the key and FDB_ID is the value. Table 3‑2 defines the optional property.

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

The following steps detail the deployment of the DATUP component. Prior to completing these steps, the WebLogic class path, the WebLogic database configurations, and the Deployment Server must be restarted to load the changed configuration. Please refer to Sections 3.4.1 and 3.4.3 for instructions concerning these configuration items. Complete the following steps to deploy DATUP:

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 3‑79.

    ![](datup-version-1-0-00-003-national-install-guide/079.png)

<span id="_Ref178735721" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑80.

    ![](datup-version-1-0-00-003-national-install-guide/080.png)

<span id="_Ref181421187" class="anchor"></span>Figure ‑. Change Center

4.  Click Install found in the Deployments panel in the right column of the WebLogic console. For reference, see Figure 3‑81.

    ![](datup-version-1-0-00-003-national-install-guide/081.png)

<span id="_Ref178732223" class="anchor"></span>Figure ‑. Deployments

5.  WebLogic will now display the panel Install Application Assistant in the right column of the console, where the location of the DATUP deployment will be found. For reference, see Figure 3‑82.

    ![](datup-version-1-0-00-003-national-install-guide/082.png)

<span id="_Ref178732382" class="anchor"></span>Figure ‑. Install Application Assistant

6.  Select the DATUP deployment. If profiling should be turned on, select the  
    DATUP.National.1.0.00.003-profile.ear file. If profiling should be turned off, select the DATUP.National.1.0.00.003.ear file. Profiling should be turned off unless required. The remaining steps assume profiling is turned off and therefore use the DATUP.National.1.0.00.003.ear file. Replace the release number for the current release.
    1.  If the DATUP deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the Location panel within the Install Application Assistant in the right column of the console. For reference, see Figure 3‑83.

        ![](datup-version-1-0-00-003-national-install-guide/083.png)

<span id="_Ref184090181" class="anchor"></span>Figure ‑. Locate Deployment to Install and Prepare for Deployment

2.  If the DATUP deployment has not been transferred to the Deployment Machine:
    1.  Click on the upload your file(s) link in the Install Application Assistant panel in the right section of the console. For reference, see Figure 3‑83.
    2.  Click the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
    3.  Click Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the Locate deployment to install and prepare for deployment panel within the Install Application Assistant. For reference, see Figure 3‑84.

        ![](datup-version-1-0-00-003-national-install-guide/084.png)

<span id="_Ref184090012" class="anchor"></span>Figure ‑. Upload a Deployment to the Admin Server

7.  Once the DATUP deployment is located and selected, click Next.
8.  WebLogic will now display the panel Choose targeting style within the Install Application Assistant in the right column of the console. Leave the default value selected, Install this deployment as an application, and click Next. For reference, see Figure 3‑85.

    ![](datup-version-1-0-00-003-national-install-guide/085.png)

<span id="_Ref176676787" class="anchor"></span>Figure 3‑85. Choose Targeting Style

9.  Within the Install Application Assistant in the right column of the console, WebLogic will now display the panel Select deployment targets, where the Deployment Server will be selected as the target in the next step. For reference, see Figure 3‑86.

    ![](datup-version-1-0-00-003-national-install-guide/086.png)

<span id="_Ref191090118" class="anchor"></span>Figure ‑. Select Deployment Targets

10. For the Target, select the Deployment Server. For example, NationalPharmacyServer
11. Click Next.
12. Within the Install Application Assistant, WebLogic will now display the panel Optional Settings in the right column of the console, where the name of the deployment and the copy behavior are chosen. For reference, see Figure 3‑87.

    ![](datup-version-1-0-00-003-national-install-guide/087.png)

<span id="_Ref191090176" class="anchor"></span>Figure ‑. Optional Settings

13. Enter the Name for the deployment. For example, DATUP.
14. Verify that the following default option for Security is selected:

    DD Only: Use only roles and policies that are defined in the deployment descriptors.
15. Verify that the following default option for Source accessibility is selected:

    Use the defaults defined by the deployment's targets.
16. Click Next.
17. Within the Install Application Assistant in the right column of the console WebLogic will now display the panel Review your choices and click Finish, which summarizes the steps completed above. For reference, see Figure 3‑88.

    ![](datup-version-1-0-00-003-national-install-guide/088.png)

<span id="_Ref191090260" class="anchor"></span>Figure ‑. Review Your Choices and Click Finish

18. Verify that the values match those entered in Steps 6 through 17 and click Finish.
19. WebLogic will now display the panel Settings for DATUP, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order. For reference, see Figure 3‑89.

    ![](datup-version-1-0-00-003-national-install-guide/089.png)

<span id="_Ref191090327" class="anchor"></span>Figure ‑. Settings for DATUP

20. Leave all the values as defaulted by WebLogic and click Save.
21. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑90.

    ![](datup-version-1-0-00-003-national-install-guide/090.png)

<span id="_Ref178733999" class="anchor"></span>Figure ‑. Activate Changes

22. Within the Domain Structure panel in the left column of the WebLogic console, click the PRE \> Deployments node. For reference, see Figure 3‑91.

    ![](datup-version-1-0-00-003-national-install-guide/091.png)

<span id="_Ref181421306" class="anchor"></span>Figure ‑. Domain Structure

23. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 3‑92.

    ![](datup-version-1-0-00-003-national-install-guide/092.png)

<span id="_Ref191090401" class="anchor"></span>Figure ‑. Summary of Deployments

24. Select the previously deployed DATUP deployment, click Start, and then select Servicing all requests from the drop-down list box.
25. WebLogic will now display the panel Start Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 3‑93.

    ![](datup-version-1-0-00-003-national-install-guide/093.png)

<span id="_Ref191090464" class="anchor"></span>Figure ‑. Start Application Assistant

26. Click Yes in the Start Application Assistant panel in the right column of the WebLogic console.
27. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 3‑94.

    ![](datup-version-1-0-00-003-national-install-guide/094.png)

<span id="_Ref191090529" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Active

28. Verify that the State of the DATUP deployment is Active.

# Upgrade Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions detail the steps required to perform an installation of a release for the DATUP software when an existing release is already deployed at a national site. These steps assume a fresh installation has been completed, following the steps in Section 3.

## Uninstall Previous Release 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the uninstallation of the DATUP application. Prior to completing these steps, the DATUP application must have been deployed following the steps in Section 3. Complete the following steps to undeploy DATUP:

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 4‑1.

    ![](datup-version-1-0-00-003-national-install-guide/095.png)

<span id="_Ref246231865" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 4‑2.

    ![](datup-version-1-0-00-003-national-install-guide/096.png)

<span id="_Ref246231871" class="anchor"></span>Figure ‑. Change Center

4.  WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 4‑3.

    ![](datup-version-1-0-00-003-national-install-guide/097.png)

<span id="_Ref246231328" class="anchor"></span>Figure ‑. Summary of Deployments – Stopping DATUP

5.  Select the previously deployed DATUP deployment, click Stop, and then select Force Stop Now from the drop-down list box.
6.  WebLogic will now display the panel Force Stop Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 4‑4.

    ![](datup-version-1-0-00-003-national-install-guide/098.png)

<span id="_Ref246231887" class="anchor"></span>Figure ‑. Force Stop Application Assistant

7.  Click Yes in the Force Stop Application Assistant panel in the right column of the WebLogic console.
8.  WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 4‑5.

    ![](datup-version-1-0-00-003-national-install-guide/099.png)

<span id="_Ref246231898" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Prepared

9.  Verify that the State of the DATUP deployment is Prepared.
10. Select the previously deployed DATUP deployment, and then click Delete.
11. WebLogic will now display the panel Delete Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 4‑6.

    ![](datup-version-1-0-00-003-national-install-guide/100.png)

<span id="_Ref246231908" class="anchor"></span>Figure ‑. Delete Application Assistant

12. Click Yes in the Delete Application Assistant panel in the right column of the WebLogic console.
13. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 4‑7.

    ![](datup-version-1-0-00-003-national-install-guide/101.png)

<span id="_Ref246231916" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Deleted

14. Verify that the DATUP deployment is deleted and no longer present.
15. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 4‑8.

    ![](datup-version-1-0-00-003-national-install-guide/102.png)

<span id="_Ref246231924" class="anchor"></span>Figure ‑. Activate Changes

## Deploy New Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deploy the new release, follow the same deployment steps found in Section 3.4.7.

(This Page Intentionally Left Blank)

# System Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section will verify that the DATUP system is up and running at a national site.

## Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the national DATUP installation is up and running, navigate a web-browser to the logs directory on your server, example http://DATUP-n/logs/NationalDatupServer/logs.

Verify that the server.log file has an entry indicating the next scheduled run time of the DATUP application. The server.log entry looks like:

DEBUG \[gov.va.med.pharmacy.peps.updater.common.utility.DifUpdateScheduler:scheduleNextTimer\] Next scheduled DIF update time: Thu, 08/26/2010, 02:45:00 PM, CDT

This line indicates that the system is running. In addition, the version report can be checked by navigating to the /DATUP/ directory on the installed server, example http://DATUP:8021/DATUP/. This provides the versioning history report and indicates that the national DATUP instance is running.

(This Page Intentionally Left Blank)Appendix ANational DATUP Configuration(This Page Intentionally Left Blank)

National DATUP configuration

This appendix provides National configuration file examples based on the baseline fdb_datup_configuration.properties file located on the delivery CD in the /configuration directory.

Example National DATUP Configuration File

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

scheduled.time=0100

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

ftp.hostname=10.3.29.201

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

\# Number of retained FDB-DIF incremental archives

\#

\# Due to potential site outages, it is necessary

\# to retain a certain number of FDB-DIF archives.

\#

\# \*This parameter applies to National.

\###################################################

fdb.retention=7

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

fdb.batch.commit.size=0

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

\# For example, "noreply@<span class="mark">REDACTED</span>".

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

email.list.success=national_managers@<span class="mark">REDACTED</span>

\###################################################

\# Email list for failure notifications

\#

\# Include individuals that should be notified about

\# failed FDB/FDB-Custom updates.

\#

\# \*This parameter applies to National and Local.

\###################################################

email.list.failure=national_managers@<span class="mark">REDACTED</span>

\###################################################

\# Email template file for failure notifications

\#

\# Specify the full path to the template file. The

\# specified template will override the default

\# template bundled with DATUP.

\#

\# \*This parameter applies to National and Local.

\###################################################

email.template.failure=/opt/datup/national.failure.txt

\###################################################

\# Email list for available update notifications

\#

\# Include individuals that should be notified about

\# available FDB/FDB-Custom updates once they are

\# applied and tested and National. This list should

\# include the local site managers.

\#

\# \*This parameter applies to National.

\###################################################

email.list.update.available=local_managers@<span class="mark">REDACTED</span>

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

![](datup-version-1-0-00-003-national-install-guide/103.png)

Figure B−1. Combined DATUP/PECS Architecture Diagram