---
title: DATUP Installation Guide - National
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: DATUP  - National
app_code: PRED
app_name: "Pharmacy: Pharmacy Data Update (DATUP)"
section: GUI
app_status: active
pkg_ns: PRED
patch_ver: 3.1
patch_id: PRED*3.1
group_key: "PRED:PRED:3.1"
file_numbers: []
security_keys: []
menu_options: 0
description: "The following list provides a brief description of the sections included in this document:"
audience: 
keywords: 
  - datup
  - figure
  - span
  - national
  - installation
  - class
  - weblogic
  - table
  - console
  - contents
page_count: 0
word_count: 9479
section_count: 15
table_count: 2
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: March 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/pred_3_1_01_p3_ign.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Data_Update/pred_3_1_01_p3_ign.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=203"
---

Data Update (DATUP) 3.1.01Installation Guide - National

![](datup-installation-guide-national/001.png)

March 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

REVISION HISTORY

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revised Pages</th>
<th>Patch Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>03/15/2021</td>
<td>Title, i, iv, v, vi, 13, 33, 34, 35,36, 37, 38, 39, 42, 43, 44, 47, C-1 – C-5, all</td>
<td>PRED*3*3</td>
<td><ul>
<li><p>Updated DATUP version to 3.1.01 for RTM and Fortify mitigations fixes</p></li>
<li><p>Updated the entire step 8, “<strong><u>Insert</u></strong>…” of section 3.4.2, Weblogic Server Startup Configuration</p></li>
<li><p>Updated the entire section of <strong><u>3.4.5</u></strong>, <strong><u>Log4j2</u></strong></p></li>
<li><p>Updated Figure 3‑6. Server Start Tab<strong><u>Figure 3‑6</u></strong>, <strong><u>Figure 3‑30</u></strong>, <strong><u>Figure 3‑31</u></strong>, <strong><u>Figure 3‑32</u></strong>, <strong><u>Figure 3‑33</u></strong>, <strong><u>Figure 3‑34</u></strong>, <strong><u>Figure 3‑35</u></strong>, <strong><u>Figure 3‑36</u></strong>, <strong><u>Figure 3‑39</u></strong>, <strong><u>Figure 3‑40</u></strong>, <strong><u>Figure 3‑41</u></strong>, <strong><u>Figure 4‑3</u></strong>, <strong><u>Figure 4‑4</u></strong>, <strong><u>Figure 4‑5</u></strong>, <strong><u>Figure 4‑6</u></strong></p></li>
<li><p>Updated the entire section of <strong><u>5.1</u></strong>, <strong><u>Verification</u></strong></p></li>
<li><p>Updated the entire <strong><u>Appendix C: log4j2</u></strong></p></li>
<li><p>Updated the Title page, Revision History, Table of Contents, List of Figures, List of Tables, and Footers</p></li>
</ul>
<p>(Liberty ITS)</p></td>
</tr>
<tr class="even">
<td>February, 2017</td>
<td>Many</td>
<td>N/A</td>
<td><p>Updated Version number for DATUP v3.0.01 which has the code changes to fix the SFTP connection issue with Centrify/Active Directory.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>April, 2016</td>
<td>All</td>
<td>N/A</td>
<td>Tech edited<br />
<mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>March 31, 2016</td>
<td>Many</td>
<td>N/A</td>
<td>Updated references to build number; added backout steps.</td>
</tr>
<tr class="odd">
<td>January 19, 2015</td>
<td>All</td>
<td>N/A</td>
<td>Tech edited<br />
<mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>December 18, 2015</td>
<td></td>
<td>N/A</td>
<td>Updated<br />
<mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>May 28, 2015</td>
<td>All</td>
<td>N/A</td>
<td><p>Updated for DATUP 3.0</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>May 27, 2015</td>
<td>All</td>
<td>N/A</td>
<td>Tech edit performed.<br />
<mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 18, 2014</td>
<td>All</td>
<td>N/A (First Release</td>
<td><p>Updated date to reflect real release date.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>June 6, 2014</td>
<td>All</td>
<td>N/A (First Release</td>
<td>Updated TOC</td>
</tr>
<tr class="odd">
<td>June 3, 2014</td>
<td>All</td>
<td>N/A (First Release</td>
<td><p>Fixed pagination, added table caption.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>May 30, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Added footnote describing relationship between FDB MedKnowledge Framework and FDB-DIF, updated text appropriately. Updated TOC.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>May 28, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated images for 508 compliance; changed FDB MedKnowledge Framework back to FDB-DIF. Updated TOC</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>May 27, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated Revision History format; did a partial search and replace on FDB-DIF (and similar phrases) to FDB MedKnowledge Framework, though not in the instructions as the tool may not be updated yet. Removed extraneous definitions of FDB. Minor text edits.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>May 21, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated Title Page, Changed Pagination for Table of Figures, Updated Version number on Overview, Corrected missing graphics</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>May 19, 2014</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated diagrams, minor formatting changes.</p>
<p><mark>REDACTED</mark>, <mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>May 13, 2014</td>
<td>All</td>
<td></td>
<td><p>Changed per CPS and changed the version number of the application throughout; fixed footers &amp; TOC</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>May 22, 2013</td>
<td>E-1</td>
<td></td>
<td><p>Edited to include rollback procedures</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>February 7, 2013</td>
<td>All</td>
<td></td>
<td><p>Tech Writer Edits</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>February 5, 2013</td>
<td>All</td>
<td></td>
<td><p>Updates to various sections for DATUP 2.0 and added Appendix D to address Image Processing Workaround.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>February 1, 2013</td>
<td>All</td>
<td></td>
<td><p>Incorporated changes to the database section to clarify instructions, updated title page and footer to reflect updates for DATUP 2.0</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>August 27, 2012</td>
<td>All</td>
<td></td>
<td><p>Changed formatting and edited document</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>May 29,2012</td>
<td>D-1</td>
<td></td>
<td><p>Updated the document to address change request #CR5172 (Image Processing for PPS)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>Sept 14,2012</td>
<td>All</td>
<td></td>
<td><p>Updates to various section to address minor configuration changes</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>November 12, 2010</td>
<td>All</td>
<td></td>
<td><p>Updated the document to address change request #CR2942.</p>
<p>SwRI</p></td>
</tr>
<tr class="even">
<td>October 8, 2010</td>
<td>All</td>
<td></td>
<td><p>Renamed all instances of “PEDTUP” to “DATUP.</p>
<p>SwRI</p></td>
</tr>
<tr class="odd">
<td>September 3, 2010</td>
<td>All</td>
<td></td>
<td><p>National PEDTUP Installation Guide: Initial version.</p>
<p>SwRI</p></td>
</tr>
</tbody>
</table>

ProPath Template used v1.6, June 2012

TABLE OF CONTENTS

List of Figures

Figure 3‑1. WebLogic Console [5](#_Ref191089515)

Figure 3‑2. Domain Structure [10](#_Ref256581857)

Figure 3‑3. Change Center [11](#_Ref256581858)

Figure 3‑4. Summary of Servers [11](#_Ref256581859)

Figure 3‑5. Settings for Deployment Server [12](#_Ref256581860)

Figure 3‑6. Server Start Tab [13](#_Ref256581861)

Figure 3‑7. Activate Changes [14](#_Ref256581862)

Figure 3‑8. Domain Structure [14](#_Ref256075822)

Figure 3‑9. Change Center [15](#_Ref256075845)

Figure 3‑10. Summary of JDBC Data Sources [15](#_Ref256075871)

Figure 3‑11. JDBC Data Source Properties [16](#_Ref256075905)

Figure 3‑12. Transaction Options [17](#_Ref256075927)

Figure 3‑13. Connection Properties [18](#_Ref256075948)

Figure 3‑14. Test Database Connection [19](#_Ref256076002)

Figure 3‑15. Select Targets [20](#_Ref256076023)

Figure 3‑16. Summary of JDBC Data Sources [21](#_Ref256076041)

Figure 3‑17. Domain Structure [22](#_Ref256076100)

Figure 3‑18. Change Center [22](#_Ref256076387)

Figure 3‑19. Summary of JDBC Data Sources [23](#_Ref256076397)

Figure 3‑20. JDBC Data Source Properties [24](#_Ref256076418)

Figure 3‑21. Transaction Options [25](#_Ref256076466)

Figure 3‑22. Connection Properties [26](#_Ref256076486)

Figure 3‑23. Test Database Connection [27](#_Ref256076518)

Figure 3‑24. Select Targets [28](#_Ref256076543)

Figure 3‑25. Summary of JDBC Data Sources [29](#_Ref256076562)

Figure 3‑26. Activate Changes [30](#_Ref256076600)

Figure 3‑27. Domain Structure [31](#_Ref178735721)

Figure 3‑28. Change Center [32](#_Ref181421187)

Figure 3‑29. Deployments [32](#_Ref178732223)

Figure 3‑30. Install Application Assistant [33](#_Ref178732382)

Figure 3‑31. Locate Deployment to Install and Prepare for Deployment [33](#_Ref184090181)

Figure 3‑32. Choose Targeting Style [34](#_Ref176676787)

Figure 3‑33. Select Deployment Targets [34](#_Ref191090118)

Figure 3‑34. Optional Settings [35](#_Ref191090176)

Figure 3‑35. Review Your Choices and Click Finish [36](#_Ref191090260)

Figure 3‑36. Settings for DATUP [37](#_Ref191090327)

Figure 3‑37. Activate Changes [37](#_Ref178733999)

Figure 3‑38. Domain Structure [38](#_Ref181421306)

Figure 3‑39. Summary of Deployments [38](#_Ref191090401)

Figure 3‑40. Start Application Assistant [38](#_Ref191090464)

Figure 3‑41. Summary of Deployments – DATUP Deployment Active [39](#_Ref191090529)

Figure 4‑1. Domain Structure [41](#_Ref246231865)

Figure 4‑2. Change Center [42](#_Ref246231871)

Figure 4‑3. Summary of Deployments – Stopping DATUP [42](#_Ref246231328)

Figure 4‑4. Force Stop Application Assistant [43](#_Ref246231887)

Figure 4‑5. Summary of Deployments – DATUP Deployment Prepared [43](#_Ref246231898)

Figure 4‑6. Delete Application Assistant [44](#_Ref246231908)

Figure 4‑7. Summary of Deployments – DATUP Deployment Deleted [44](#_Ref246231916)

Figure 4‑8. Activate Changes [45](#_Ref246231924)

Figure B‑1: Combined DATUP/PECS Architecture Diagram [2](#_Toc66785352)

List of Tables

Table 3‑1. Terminology [6](#_Ref176675115)

Table 3‑2: Summary of Steps for Creating Oracle Schema [8](#_Toc66785354)

*(This page included for two-sided copying.)*

# Project Scope


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Project Scope](#project-scope)
  - [Project Description](#project-description)
  - [PRE Project Goals and Objectives](#pre-project-goals-and-objectives)
  - [DATUP Background](#datup-background)
  - [Related Documents](#related-documents)
- [Document Overview](#document-overview)
  - [Document Background](#document-background)
  - [Overview](#overview)
- [Installation Instructions](#installation-instructions)
  - [Terminology](#terminology)
  - [Assumptions](#assumptions)
  - [Database Installation and Configuration](#database-installation-and-configuration)
    - [Oracle Database](#oracle-database)
    - [Oracle Installation](#oracle-installation)
    - [Oracle Schema Creation for DATUP](#oracle-schema-creation-for-datup)
    - [Oracle Configuration and Data Load](#oracle-configuration-and-data-load)
  - [WebLogic Installation Instructions](#weblogic-installation-instructions)
    - [Class Path](#class-path)
    - [WebLogic Server Startup Configuration](#weblogic-server-startup-configuration)
    - [National FDB-DIF Data Source Configuration](#national-fdb-dif-data-source-configuration)
    - [National JDBC DATUP Data Source Configuration](#national-jdbc-datup-data-source-configuration)
    - [Log4j2](#log4j2)
    - [DATUP Cleanup Script](#datup-cleanup-script)
    - [Deployment](#deployment)
- [Upgrade Installation Instructions](#upgrade-installation-instructions)
  - [Uninstall Previous Release](#uninstall-previous-release)
  - [Deploy New Release](#deploy-new-release)
  - [Backout Build](#backout-build)
- [System Verification](#system-verification)
  - [Verification](#verification)
- [Appendix A: National DATUP Configuration](#appendix-a-national-datup-configuration)
- [Appendix B: Combined DATUP / PECS Architecture](#appendix-b-combined-datup-pecs-architecture)
- [Appendix C: log4j2](#appendix-c-log4j2)
- [Appendix D: Rollback Process](#appendix-d-rollback-process)

## Project Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goal of the VHA PRE project is to design and develop a re-engineered pharmacy system, incorporating changes that have been made to the Enterprise Architecture and changes in pharmacy business processes. The intent of the PRE program is to ensure that no current system functionality is lost, but that it is either replicated in the new system or replaced by improved process and functionality. While the overall plan is still based on designing and implementing a complete pharmacy system, the scope of the effort has been defined to address a focused subset of the PRE functionality confined to the Data Update (DATUP) process.

## PRE Project Goals and Objectives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The objective of the PRE project is to facilitate the improvement of pharmacy operations, customer service, and patient safety for the VHA. The PRE project will help address the identified goals and vision for the VHA Pharmacy System.

The goal for the PRE project is a seamless and integrated nationally-supported system that is an integral part of the Health*<u>e</u>*Vet-Veterans Health Information Systems & Technology Architecture (VistA) environment. To meet this goal, the PRE project will enhance pharmacy data exchange, as well as clinical documentation capabilities, in a truly integrated fashion to improve operating efficiency and patient safety. Additionally, it will provide a flexible technical environment to adjust to future business conditions and to meet patient needs in the clinical environment. Achieving this goal will enable resolution of current pharmacy issues, improve patient safety, and facilitate long-term process stability.

## DATUP Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP supports the Medication Order Check Healthcare Application (MOCHA) by performing data source updates. MOCHA conducts order checks using First Databank (FDB) MedKnowledge Framework[^1] within the existing VistA pharmacy application. FDB is a data product that provides the latest identification and safety information on medications. Additionally, FDB provides the latest algorithms used to perform order checks. DATUP processes the data updates associated with FDB MedKnowledge Framework. The order checks performed by MOCHA include:

- Drug-Drug Order Check – Check interactions between two or more drugs, including interaction monographs.
- Duplicate Therapy Order Check – Check for duplicated drug classifications between two or more drugs.
- Drug-Dose Order Check – Check minimum and maximum single doses, verify the dosing schedule, and provide the normal dosing range.

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A complete list of documents relating to the PRE project and the DATUP development effort can be found in the Glossary and Acronym List (Version 5.0, dated September 26, 2008).

# Document Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information contained in this National Data Update (DATUP) Installation Guide is specific to DATUP development, which supports the MOCHA component. This section defines the layout of this document and provides an outline of the document structure.

## Document Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document details the steps required to install the DATUP software at a national site, the terminology used for the configuration and deployment of the software, and the assumptions for installing the software. Additionally, this document details how to install and configure the database environment. This document accompanies the delivery of the DATUP v3.1.01 software release. The DATUP Version Description Document (Version 1.7) is delivered as a companion document to this Installation Guide. Refer to the Version Description Document for more information on the software inventory and versions used in the DATUP V3.1.01 software release.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list provides a brief description of the sections included in this document:

Section 1: Provides introductory material delineating the purpose of the PRE project and the scope of the MOCHA effort

Section 2: Presents an overview of the layout of the document

Section 3: Presents the installation instructions for the DATUP v3.1.01 software release

Section 4: Details the steps required to perform an installation when an existing version is already deployed.

Section 5: Presents verification steps to verify that the installation was successful

Text in a Courier New font indicates WebLogic Console panels or text, commands, and settings that must be typed, executed, or configured to complete the installation.

*(This page included for two-sided copying.)*

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions detail the steps required to perform a *fresh* installation of the DATUP software at a national site. For *upgrade* installation instructions see Section 4. Section 3.1 details the terminology used for the configuration and deployment of the DATUP software. Section 3.2 outlines the assumptions for installing the DATUP software. While the system may be configured to run outside the given assumptions, doing so requires modifications that are not detailed in this document. Section 3.3 describes how to install and configure the DATUP software properly. Finally, Section 3.3 describes how to install and configure the database environment.

In order to understand the installation and verification process, the reader should be familiar with the WebLogic console shown in Figure 3‑1. The WebLogic console is a Web page viewable from any Internet browser; however, Internet Explorer, Version 7, is recommended. The WebLogic console is generally divided into two sections. The left section contains the Change Center, Domain Structure, and other informational panels. The right section displays panels containing additional options or configuration details. Note: With the exception of the Change Center and Domain Structure references, further references to WebLogic console panels refer to panels in the right section of the WebLogic console.

![](datup-installation-guide-national/002.png)

<span id="_Ref191089515" class="anchor"></span>Figure ‑. WebLogic Console

## Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In an effort to make these installation instructions as general as possible for installation at any site, a few terms are used throughout the instructions with the intent that they be replaced with site-specific values.

Table 3‑1 contains a list of those terms used only within this document as well as sample site-specific values for each term. Additionally, references to the DATUP-N server may be replaced with the site-specific name of the destination server at the installation site. <span id="_Ref176675115" class="anchor"></span>

Table ‑. Terminology

| Term                                                               | Definition                                                                                                                                                                             | Sample                                   |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| Database Server                                                    | Machine on which Oracle is installed and runs                                                                                                                                          | DATUP-N-DB                               |
| Deployment Machine                                                 | Site-specific machine on which WebLogic is installed and runs                                                                                                                          | DATUP-N                                  |
| Deployment Server                                                  | WebLogic managed server where DATUP is deployed                                                                                                                                        | National_DATUP                           |
| Deployment Server Port                                             | Port on which the Deployment Server is listening                                                                                                                                       | 8010                                     |
| Deployment Server’s class path directory                           | Folder location on the Deployment Server where libraries on the class path are located (see WebLogic documentation for instructions on setting a WebLogic managed server’s class path) | /u01/app/Oracle_Home/wlserver/server/lib |
| Java Database Connectivity (JDBC) Universal Resource Locator (URL) | URL to connect to Oracle database                                                                                                                                                      | jdbc:Oracle://DATUP-N-db:1972/FDB_DIF    |

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation instructions found within this guide are intended to be performed on a clean installation of WebLogic 12.1.1, with a separate managed server to act as the Deployment Server. For details on completing the installation of the following items, please refer to each item’s installation and configuration documentation supplied by Oracle.

For successful deployment of the DATUP software at a national site, the following assumptions must be met:

- The Deployment Server is configured and running.
- WebLogic is configured to run with the Java™ Standard Edition Development Kit, Version 1.7+.
- Access to the WebLogic console is by means of any valid administrative user name and password.
- The proper Oracle database driver libraries for the chosen deployment environment are present on the class path for the respective Deployment Servers.
- Red Hat Enterprise Linux 6.x operating system is properly installed.
- Domain Name Server (DNS) resolution is configured for the DATUP server.
- The installation instructions are followed in the order that the sections are presented within this Installation Guide.
- FDB-DIF v3.3 database is installed on the Database Server. Installation instructions are provided in FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project’s Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.

## Database Installation and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the operating system and software for the DATUP database tier installation and configuration. Initially, install and configure the operating system software according to the manufacturer’s specifications. Then configure the Oracle databases as specified in the following sections for DATUP to function properly.

### Oracle Database 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DATUP database is designed to be operating system independent. The only constraint is that Oracle 11g Enterprise Edition – Production must be properly installed and configured. The following sections describe the installation, features, user creation, and configuration for the Oracle database.

For successful deployment of the DATUP v3.1.01 application on the National DATUP instance, the FDB-DIF v3.3 database must be installed. Installation instructions are provided in FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project’s Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.

### Oracle Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A proper installation of the Oracle Relational Database Management System (RDBMS) is one in which the Oracle Universal Installer was used to perform an error-free installation and a general purpose instance was created. A properly configured Oracle RDBMS is one in which the associated Oracle application development and configuration tools, namely SQL\*Plus and Oracle Enterprise Manager, can be used to connect to the instance through Transparent Network Substrate alias.

Oracle Database Parameters

The following Oracle database parameters are recommended for the DATUP application:

- NLS language = American
- NLS territory = America
- Character set = WE8ISO8859P1

### Oracle Schema Creation for DATUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following are the steps needed to setup the DATUP schema on a national instance. Additionally, an example session is provided is provided in Oracle Installation.txt detailing the commands issued, sequence performed, and expected results at each step. This file and the SQL scripts needed to create the DATUP schema are provided in the database/oracle_scripts.zip file. The following table provides a summary of each step that will be detailed below:

<span id="_Toc66785354" class="anchor"></span>Table ‑: Summary of Steps for Creating Oracle Schema

| Step | Brief Description              | Script File          | User to Run Script File |
|----------|------------------------------------|--------------------------|-----------------------------|
| 1        | Create tablespace and schema owner | 1_CreateDatupSchema.sql  | SYSTEM                      |
| 2        | Create schema objects              | 2_CreateDatupTables.sql  | DATUP                       |
| 3        | Create application user            | 3_CreateDatupAppUser.sql | SYSTEM                      |

Summary of steps for creating Oracle schema.

Step 1 – Create Tablespace and Schema Owner

Prior to creation of the schema, logical and physical environment structures must be setup for storage of the schema database objects: tablespaces and data files. For the DATUP schema one tablespace must be created, DATUP. The default scripted DATUP tablespace path is /home/oracle/datup.dbf, which may be changed in the 1_CreateDatupSchema.sql script to match the installation environment prior to execution. This script also creates the schema owner DATUP as described below:

- DATUP – Owner of the DATUP schema. The default scripted password is “DATUP”, which may be changed in the 1_CreateDatupSchema.sql script prior to installation. The script should be loaded as SYSTEM, or a user with account creation privileges.

  Step by Step Commands
1.  Open a text editor and open the 1_CreateDatupSchema.sql script. Replace /home/oracle with the data file directory. The directory entered should already exist on the database server.
1.  Login to the SQL client using a database account that has SYSDBA privileges (SYSTEM).
2.  Execute the “1_CreateDatupSchema.sql” script.
3.  Check for errors.

Step 2 – Create Schema Objects

Once the storage structures and schema have been created, execute the script 2_CreateDatupTables.sql to create the DATUP tables, sequences, triggers, and indices. The script should be executed as DATUP, the schema owner.

Step by Step Commands

1.  Login to the SQL client using the DATUP user account.
4.  Execute the “2_CreateDatupTables.sql” script.
5.  Check for errors.

Step 3 – Create Application User

Once the schema objects have been established, create the required DATUP application user by executing the script 3_CreateDatupAppUser.sql.

- DATUP_APP_USER – Application user with read/update/delete access granted to the tables in the DATUP schema. The default scripted password is “DATUP_APP_USER”, which may be changed in the 3_CreateDatupAppUser.sql script prior to installation. The script should be loaded as SYSTEM, or a user with account creation privileges. The chosen DATUP_APP_USER password must match the password used to configure the JDBC data sources in Section 3.4.4.

  Step by Step Commands
1.  Login to the SQL client using a database account that has SYSDBA privileges (SYSTEM).
6.  Execute the “3_CreateDatupAppUser.sql” script.
7.  Check for errors.

### Oracle Configuration and Data Load

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DATUP Oracle Database is the primary data repository for the DATUP application on the National DATUP instance. The database should be installed and configured appropriately for the DATUP operating environment.

The initial data load about the regionally-managed MOCHA Servers must be loaded for the national DATUP instance to function. The data can be loaded with the SQL Loader scripts provided in the database/oracle_scripts.zip file. The Sites.ctl file describes the data and the Sites.csv file contains the comma-delimited Site records. The data should be loaded as DATUP_APP_USER. Execute the following steps to load the DATUP schema:

Step by Step Commands

1.  Ensure the Sites.ctl file is in the current directory.
8.  Type the following command from the Linux command prompt to invoke SQL Loader:

    \$sqlldr datup_app_user/datup_app_user@ORACLE control=Sites.ctl
9.  Check for errors.

The DATUP database will need to be updated if a new MOCHA Server has been brought online since the original DATUP delivery date of March 17, 2010 and is not included in the Sites.csv spreadsheet. To update the Site table, login to the database as user DATUP_APP_USER. A new row must be added to the Site table for each MOCHA Server added since the system was first brought online. The site table contains three columns, a unique SITE_ID, a descriptive SITE_NAME, and the Veterans Integrated Service Network (VISN) VISN number. To update this table, execute a statement such as INSERT INTO SITE VALUES (999, 'Example Medical Center', 23) for each MOCHA Server brought online.

## WebLogic Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections detail the steps required to configure and deploy DATUP onto WebLogic at a national site.

### Class Path

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The national DATUP Enterprise Application Archive (EAR) file contains all the required libraries for the proper functioning of the application. If any other applications have been deployed to the Deployment Server, there may be conflicting third-party libraries in the Deployment Server's class path that will cause DATUP to operate differently than expected. If versions on the Deployment Server’s class path differ from those defined in the DATUP Version Description Document (Version 3.1.01, dated February, 2017), the preferred solution is to remove the library from the Deployment Server's class path. If that is not possible, replace the libraries with the DATUP versions.

### WebLogic Server Startup Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP requires additional arguments added to the WebLogic Server’s Server Start properties. This section details the steps to add the arguments to the server

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑2.

    ![](datup-installation-guide-national/003.png)

<span id="_Ref256581857" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑3.

    ![](datup-installation-guide-national/004.png)

<span id="_Ref256581858" class="anchor"></span>Figure ‑. Change Center

4.  Click on the server name corresponding to the deployment server in the Summary of Servers panel found in the right column of the WebLogic console. For reference, see Figure 3‑4.

    ![](datup-installation-guide-national/005.png)

<span id="_Ref256581859" class="anchor"></span>Figure ‑. Summary of Servers

5.  WebLogic will now display the panel Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server are set. For reference, see Figure 3‑5.

    ![](datup-installation-guide-national/006.png)

<span id="_Ref256581860" class="anchor"></span>Figure ‑. Settings for Deployment Server

6.  Click on the Server Start tab.
7.  WebLogic will now display the panel Server Start tab in the Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server is set. For reference, see Figure 3‑6.

    ![](datup-installation-guide-national/007.png)

<span id="_Ref256581861" class="anchor"></span>Figure ‑. Server Start Tab

8.  Insert the following text in the Arguments box:

> -server -Xms4g -Xmx4g -XX:PermSize=256m -XX:MaxPermSize=512m -Dweblogic.nodemanager.ServiceEnabled=true –

> Also add arguments (for reference, see the examples below, modify path per your server configuration) :-

-Dpeps.datup.configuration=:/u01/app/OracleHome/user_projects/domains/pps_dev2/datupconfig/fdb_datup_configuration.properties

9.  Click the Save Button
10. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑7.

    ![](datup-installation-guide-national/008.png)

<span id="_Ref256581862" class="anchor"></span>Figure ‑. Activate Changes

### National FDB-DIF Data Source Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses two database connections by means of a data source to FDB-DIF in order to perform FDB updates. Complete the following steps to create a new connection pool and data source for FDB-DIF.

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑8.

    ![](datup-installation-guide-national/009.png)

<span id="_Ref256075822" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑9.

    ![](datup-installation-guide-national/010.png)

<span id="_Ref256075845" class="anchor"></span>Figure ‑. Change Center

4.  Click New – Generic Data Source found in the Summary of JDBC Data Sources panel found in the right column of the WebLogic console. For reference, see Figure 3‑10.

    ![](datup-installation-guide-national/011.png)

<span id="_Ref256075871" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

5.  WebLogic will now display the panel Create a New JDBC Data Source in the right column of the console, where details of the new data source are set. For reference, see Figure 3‑11.

    ![](datup-installation-guide-national/012.png)

<span id="_Ref256075905" class="anchor"></span>Figure ‑. JDBC Data Source Properties

6.  For the Name, type FDB-DIF.
7.  For the JNDI Name, type datasource/FDB-DIF.
8.  For the Database Type, select Oracle.
9.  Click Next.
10. For the Database Driver, verify that Oracle’s Driver (Thin) for Instance Connections; Versions:9.0.1 and later is selected.
11. Click Next.
12. WebLogic will now display the panel Transaction Options in the right column of the console, where the transaction attributes for this data source are set. For reference, see Figure 3‑12.

    ![](datup-installation-guide-national/013.png)

<span id="_Ref256075927" class="anchor"></span>Figure ‑. Transaction Options

13. Select the Emulate Two-Phase Commit radio button.
14. Click Next.
15. WebLogic will now display the panel Connection Properties in the right column of the console, where the connection pool attributes are set. For reference, see Figure 3‑13.

    ![](datup-installation-guide-national/014.png)

<span id="_Ref256075948" class="anchor"></span>Figure ‑. Connection Properties

16. For Database Name, type the name of the Oracle database to which DATUP will connect. For example, PECS.
17. For Host Name, type the name of the machine on which Oracle is running. For example, vaauspecapp80.aac.va.gov.
18. For Port, type the port on which Oracle is listening. For example, 1521.
19. For Database User Name, type the user to connect to the FDB database. For example, FDB-DIF. The user entered should be the same as configured in Section
20. For Password and Confirm Password, type the password for the user given previously.
21. Click Next.

WebLogic will now display the panel Test Database Connection in the right column of the console, where the new data source can be tested. For reference, see Figure 3‑14.

![](datup-installation-guide-national/015.png)

<span id="_Ref256076002" class="anchor"></span>Figure ‑. Test Database Connection

22. Leave all values as set by default, with the exception of Test Table Name. For this attribute, type fdb_version.
23. Click Next.
24. WebLogic will now display the panel Select Targets in the right column of the console, where the target server is selected for the new data source. For reference, see Figure 3‑15.

    ![](datup-installation-guide-national/016.png)

<span id="_Ref256076023" class="anchor"></span>Figure ‑. Select Targets

25. Select the Deployment Server as the target. For example, National_DATUP.
26. Click Finish.
27. Click Activate Changes.
28. WebLogic will now display the panel Summary of JDBC Data Sources in the right column of the console, where the newly created data source is displayed. For reference, see Figure 3‑16.

    ![](datup-installation-guide-national/017.png)

<span id="_Ref256076041" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

### National JDBC DATUP Data Source Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses two database connections by means of a data source to perform the automated DATUP update process. Complete the following steps to create a new connection pool and data source for MedKnowledge Framework.

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel found in the left column of the WebLogic console, click on the Services \> JDBC \> Data Sources node. For reference, see Figure 3‑17.

    ![](datup-installation-guide-national/018.png)

<span id="_Ref256076100" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel found in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑18.

    ![](datup-installation-guide-national/019.png)

<span id="_Ref256076387" class="anchor"></span>Figure ‑. Change Center

4.  Click New – Generic Datasource found in the Summary of JDBC Data Sources panel found in the right column of the WebLogic console. For reference, see Figure 3‑19.

    ![](datup-installation-guide-national/020.png)

> <span id="_Ref256076397" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

5.  WebLogic will now display the panel Create a New JDBC Data Source in the right column of the console, where details of the new data source are set. For reference, see Figure 3‑20.

    ![](datup-installation-guide-national/021.png)

<span id="_Ref256076418" class="anchor"></span>Figure ‑. JDBC Data Source Properties

6.  For the Name, type DATUP.
7.  For the JNDI Name, type datasource/DATUP.
8.  For the Database Type, select Oracle.
9.  Click Next.
10. For the Database Driver, verify that Oracle’s Driver (Thin) for Instance connections; Versions: 9.0.1 and later is selected.
11. Click Next.
12. WebLogic will now display the panel Transaction Options in the right column of the console, where the transaction attributes for this data source are set. For reference, see Figure 3‑21.

    ![](datup-installation-guide-national/022.png)

<span id="_Ref256076466" class="anchor"></span>Figure ‑. Transaction Options

13. Select the Emulate Two-Phase Commit radio button
14. Click Next.
15. WebLogic will now display the panel Connection Properties in the right column of the console, where the connection pool attributes are set. For reference, see Figure 3‑22.

    ![](datup-installation-guide-national/023.png)

<span id="_Ref256076486" class="anchor"></span>Figure ‑. Connection Properties

16. For Database Name, type the name of the Oracle database to which DATUP will connect. For example, PECS.
17. For Host Name, type the name of the machine on which Oracle is running. For example, vaauspecapp80.aac.va.gov.
18. For Port, type the port on which Oracle is listening. For example, 1521.
19. For Database User Name, type the user to connect to the FDB database. For example, DATUP. The user entered should be the same as configured in Section 
20. For Password and Confirm Password, type the password for the user given previously.
21. Click Next.

WebLogic will now display the panel Test Database Connection in the right column of the console, where the new data source can be tested. For reference, see Figure 3‑23.

![](datup-installation-guide-national/024.png)

<span id="_Ref256076518" class="anchor"></span>Figure ‑. Test Database Connection

22. Leave all values as set by default.
23. Click Next.
24. WebLogic will now display the panel Select Targets in the right column of the console, where the target server is selected for the new data source. For reference, see Figure 3‑24.

    ![](datup-installation-guide-national/025.png)

<span id="_Ref256076543" class="anchor"></span>Figure ‑. Select Targets

25. Select the Deployment Server as the target. For example, National_DATUP.
26. Click Finish.
27. WebLogic will now display the panel Summary of JDBC Data Sources in the right column of the console, where the newly created data source is displayed. For reference, see Figure 3‑25.

    ![](datup-installation-guide-national/026.png)

<span id="_Ref256076562" class="anchor"></span>Figure ‑. Summary of JDBC Data Sources

28. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑26.

    ![](datup-installation-guide-national/027.png)

<span id="_Ref256076600" class="anchor"></span>Figure ‑. Activate Changes

### Log4j2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP uses Log4j2 to provide debug and error logs. Although the application will function without Log4j2 installed, using it can be helpful to troubleshoot potential issues. Because DATUP can operate without Log4j2 configured, all instructions within this section are only required if debugging deployed code.

To install Log4j2, the log4j2.xml must be edited to include the DATUP appenders and loggers.

1.  Create the log folder defined in the Deployment Server arguments. For example, /u01/app/Oracle_Home/user_projects/domains/ppsn/DATUPLogs. Without this folder, Log4j2 will not be able to create the log files specified in the DATUP configuration.
2.  Create the log4j2.xml file that is located in the path specified in the Deployment Server arguments.
3.  Configure the log4j2.xml using Appendix C as a reference.
4.  Refer log4j2.xml at /u01/app/OracleHome/user_projects/domains/pps_dev2/datupconfig
5.  Restart the Deployment Server to load the Log4j2 configuration.

DATUP Configuration Properties

In order to use the DATUP component, a configuration file must be configured for each WebLogic deployment. The location of this file was configured in Section 3.4.2. This file is self-documenting and contains the list of configurable properties for DATUP. See Appendix A for a sample version and notes on new parameters.

### DATUP Cleanup Script

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DATUP creates temporary zip files during the update process. Create a cron job to remove /tmp/datup\*.zip files once a day.

### Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the deployment of the DATUP component. Prior to completing these steps, the WebLogic class path, the WebLogic database configurations, and the Deployment Server must be restarted to load the changed configuration. Please refer to Sections 3.4.1 and 3.4.3 for instructions concerning these configuration items. Complete the following steps to deploy DATUP:

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 3‑27.

    ![](datup-installation-guide-national/028.png)

<span id="_Ref178735721" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 3‑28.

    ![](datup-installation-guide-national/029.png)

<span id="_Ref181421187" class="anchor"></span>Figure ‑. Change Center

4.  Click Install found in the Deployments panel in the right column of the WebLogic console. For reference, see Figure 3‑29.

    ![](datup-installation-guide-national/030.png)

<span id="_Ref178732223" class="anchor"></span>Figure ‑. Deployments

5.  WebLogic will now display the panel Install Application Assistant in the right column of the console, where the location of the DATUP deployment will be found. For reference, see Figure 3‑30.

    ![](datup-installation-guide-national/031.png)

<span id="_Ref178732382" class="anchor"></span>Figure ‑. Install Application Assistant

6.  Navigate to the deployment file location using the links and file structure displayed within the Location panel within the Install Application Assistant in the right column of the console, and select the DATUP deployment, select the datup-national-3.1.01.ear file. (Replace the release number for the current release.)

    For reference, see Figure 3‑31.

    ![](datup-installation-guide-national/032.png)

<span id="_Ref184090181" class="anchor"></span>Figure ‑. Locate Deployment to Install and Prepare for Deployment

7.  Once the DATUP deployment is located and selected, click Next.
8.  WebLogic will now display the panel Choose targeting style within the Install Application Assistant in the right column of the console. Leave the default value selected, Install this deployment as an application, and click Next. For reference, see Figure 3‑32.

    ![](datup-installation-guide-national/033.png)

<span id="_Ref176676787" class="anchor"></span>Figure ‑. Choose Targeting Style

9.  Within the Install Application Assistant in the right column of the console, WebLogic will now display the panel Select deployment targets, where the Deployment Server will be selected as the target in the next step. For reference, see Figure 3‑33.

    ![](datup-installation-guide-national/034.png)

<span id="_Ref191090118" class="anchor"></span>Figure ‑. Select Deployment Targets

10. For the Target, select the Deployment Server. For example, NationalPharmacyServer
11. Click Next.
12. Within the Install Application Assistant, WebLogic will now display the panel Optional Settings in the right column of the console, where the name of the deployment and the copy behavior are chosen. For reference, see Figure 3‑34.

    ![](datup-installation-guide-national/035.png)

<span id="_Ref191090176" class="anchor"></span>Figure ‑. Optional Settings

13. Enter the Name for the deployment. For example, DATUP.
14. Verify that the following default option for Security is selected:

    DD Only: Use only roles and policies that are defined in the deployment descriptors.
15. Verify that the following default option for Source accessibility is selected:

    Use the defaults defined by the deployment's targets.
16. Click Next.
17. Within the Install Application Assistant in the right column of the console WebLogic will now display the panel Review your choices and click Finish, which summarizes the steps completed above. For reference, see Figure 3‑35.

    ![](datup-installation-guide-national/036.png)

<span id="_Ref191090260" class="anchor"></span>Figure ‑. Review Your Choices and Click Finish

18. Verify that the values match those entered in Steps 1 through 17 and click Finish.
19. WebLogic will now display the panel Settings for DATUP, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order. For reference, see Figure 3‑36.

    ![](datup-installation-guide-national/037.png)

<span id="_Ref191090327" class="anchor"></span>Figure ‑. Settings for DATUP

20. Leave all the values as defaulted by WebLogic and click Save.
21. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 3‑37.

    ![](datup-installation-guide-national/038.png)

<span id="_Ref178733999" class="anchor"></span>Figure ‑. Activate Changes

22. Within the Domain Structure panel in the left column of the WebLogic console, click the PRE \> Deployments node. For reference, see Figure 3‑38.

    ![](datup-installation-guide-national/039.png)

<span id="_Ref181421306" class="anchor"></span>Figure ‑. Domain Structure

23. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 3‑39.

    ![](datup-installation-guide-national/040.png)

<span id="_Ref191090401" class="anchor"></span>Figure ‑. Summary of Deployments

24. Select the previously deployed DATUP deployment, click Start, and then select Servicing all requests from the drop-down list box.
25. WebLogic will now display the panel Start Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 3‑40.

    ![](datup-installation-guide-national/041.png)

<span id="_Ref191090464" class="anchor"></span>Figure ‑. Start Application Assistant

26. Click Yes in the Start Application Assistant panel in the right column of the WebLogic console.
27. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 3‑41.

    ![](datup-installation-guide-national/042.png)

<span id="_Ref191090529" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Active

28. Verify that the State of the DATUP deployment is Active.

*(This page included for two-sided copying.)*

# Upgrade Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following instructions detail the steps required to perform an installation of a release for the DATUP software when an existing release is already deployed at a national site. These steps assume a fresh installation has been completed, following the steps in Section 3.

## Uninstall Previous Release 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the un-installation of the DATUP application. Prior to completing these steps, the DATUP application must have been deployed following the steps in Section 3. Complete the following steps to un-deploy DATUP:

1.  Open and log into the WebLogic console. This is located at: http://\<Deployment Machine\>:7001/console.
2.  Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node. For reference, see Figure 4‑1.

    ![](datup-installation-guide-national/043.png)

<span id="_Ref246231865" class="anchor"></span>Figure ‑. Domain Structure

3.  Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit. For reference, see Figure 4‑2.

    ![](datup-installation-guide-national/044.png)

<span id="_Ref246231871" class="anchor"></span>Figure ‑. Change Center

4.  WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed. For reference, see Figure 4‑3.

    ![](datup-installation-guide-national/045.png)

<span id="_Ref246231328" class="anchor"></span>Figure ‑. Summary of Deployments – Stopping DATUP

5.  Select the previously deployed DATUP deployment, click Stop, and then select Force Stop Now from the drop-down list box.
6.  WebLogic will now display the panel Force Stop Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 4‑4.

    ![](datup-installation-guide-national/046.png)

<span id="_Ref246231887" class="anchor"></span>Figure ‑. Force Stop Application Assistant

7.  Click Yes in the Force Stop Application Assistant panel in the right column of the WebLogic console.
8.  WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 4‑5.

    ![](datup-installation-guide-national/047.png)

<span id="_Ref246231898" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Prepared

9.  Verify that the State of the DATUP deployment is Prepared.
10. Select the previously deployed DATUP deployment, and then click Delete.
11. WebLogic will now display the panel Delete Application Assistant in the right column of the console for confirmation to start servicing requests. For reference, see Figure 4‑6.

    ![](datup-installation-guide-national/048.png)

<span id="_Ref246231908" class="anchor"></span>Figure ‑. Delete Application Assistant

12. Click Yes in the Delete Application Assistant panel in the right column of the WebLogic console.
13. WebLogic now returns to the Summary of Deployments panel in the right column of the console. For reference, see Figure 4‑7.

    ![](datup-installation-guide-national/049.png)

<span id="_Ref246231916" class="anchor"></span>Figure ‑. Summary of Deployments – DATUP Deployment Deleted

14. Verify that the DATUP deployment is deleted and no longer present.
15. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes. For reference, see Figure 4‑8.

    ![](datup-installation-guide-national/050.png)

<span id="_Ref246231924" class="anchor"></span>Figure ‑. Activate Changes

## Deploy New Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deploy the new release, follow the same deployment steps found in Section [30](#deployment)3.4.7.

## Backout Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To backout the current DATUP build, follow the steps in Section 4.1 to uninstall the build. Then, follow the steps in Section 4.2 to deploy the previous build.

*(This page included for two-sided copying.)*

# System Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section will verify that the DATUP system is up and running at a national site.

## Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the national DATUP installation is up and running, navigate a web-browser to the logs directory on your server, example: /u01/app/OracleHome/user_projects/domains/ppsn/DATUPLOGS.

Verify that the server.log file has an entry indicating the next scheduled run time of the DATUP application. The server.log entry looks like:

DEBUG \[<span class="mark">REDACTED</span>pharmacy.peps.updater.common.utility.DifUpdateScheduler:scheduleNextTimer\] Next scheduled DIF update time: Thu, 4/16/2010, 02:45:00 PM, CDT

This line indicates that the system is running.

*(This page included for two-sided copying.)*

# Appendix A: National DATUP Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix provides National configuration file examples based on the baseline fdb_datup_configuration.properties file. Configure the parameters in this file to match the settings of the particular environment into which you are installing. The sftp.hostname, sftp.port, sftp.username, sftp.password, sftp.base.directory, and sftp.fdb.directory much match the configuration of the sftp server.

The fdb.flag.provider.url value should be configured with the servername and port where DATUP National is running.

The file.name.fragment and file.search.type should be configured to match the environment in which DATUP is being installed.

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

scheduled.time=0630

\###################################################

\#------------------- sFTP Server -------------------

\###################################################

\###################################################

\# SFTP server hostname

\#

\# Specify the SFTP server hostname.

\#

\# \*This parameter applies to National and Local.

\###################################################

sftp.hostname=vaauspresftp01.aac.va.gov

\###################################################

\# SFTP server port number

\#

\# Specify the SFTP server port number.

\#

\# \*This parameter applies to National and Local.

\###################################################

sftp.port=22

\###################################################

\# SFTP server username/password.

\#

\# Specify the anonymous account username/password.

\#

\# \*These parameters apply to National and Local.

\###################################################

sftp.username=presftp

sftp.password=password

\###################################################

\# SFTP server working directory

\#

\# Specify the SFTP working directory, relative to

\# the SFTP root directory.

\#

\# \*This parameter applies to National and Local.

\###################################################

sftp.base.directory=/home/presftp/pecs_preprod/

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

sftp.fdb.directory=/home/presftp/pecs_preprod/fdb_dif

\###################################################

\# File Name Fragment

\#

\# Specify the fragment of the file name to be used when searching for files to process.

\# Production Environment value of "UPD"

\# All Other Environments value of "I"

\#

\# \*The search is case insensitive.

\# \*This parameter is used in conjunction with File Search Type (file.search.type)

\# \*This parameter applies to National.

\###################################################

\#file.name.fragment=UPD

file.name.fragment=I

\###################################################

\# File Search Type

\#

\# Specify the search type that should be used.

\#

\# Production Environment value of "contains"

\# All Other Environments value of "starts_with"

\#

\# \*This parameter is used in conjunction with File Name Fragment (file.name.fragment)

\# \*This parameter applies to National.

\###################################################

\#file.search.type=contains

file.search.type=starts_with

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

fdb.verification.test.count=5

\###################################################

\# Comparison Reports Property

\#

\# This property is to be set to true if DATUP will

\# need to wait on the PECS Application to finish

\# running the Comparison Reports.

\#

\# In environments where PECS is not installed,

\# set this to false to eliminate the dependency

\# on PECS Comparison Reports running.

\#

\# \*This parameter applies to National.

\###################################################

comparison.reports=true

\###################################################

\# FDB Comparison Report Created Flag

\#

\# This property sets the default value for a boolean

\# JNDI resource that will be created on the Weblogic

\# Domain at startup.

\# This boolean value (or flag) will be used by both

\# Datup National and PECS to coordinate the processing

\# of fdb files so PECS can make appropriate use

\# such files before they are deleted by DATUP.

\#

\# \*If this property is not defined, the default value

\# will be set to false.

\# \*This parameter applies to National.

\###################################################

fdb.comparison.report.created.flag=false

\###################################################

\#fdb.flag.provider.url

\#

\# Specifies the URL of the WebLogic Server that

\# provides the naming context where the

\# fdb_comparison_report_created_flag resource resides.

\# i.e. t3://servername:port (t3 is Weblogic's protocol)

\# This property is also defined in PECS, so the

\# value on both properties should be the same.

\###################################################

fdb.flag.provider.url=t3://vaauspecapp93.aac.va.gov:8007

\###################################################

\# FDB wait time for PECS run

\#

\# Specify the number of minutes that DATUP will

\# wait for PECS to generate its FDB Customization

\# report before trying to process the FDB-DIF

\# files again.

\#

\# Default value will be 20 minutes

\# \*This parameter applies to National.

\###################################################

fdb.pecs.wait.time=180

\###################################################

\#------------------- Email Server -----------------

\###################################################

\###################################################

\# Email server hostname

\#

\# \*This parameter applies to National and Local.

\###################################################

email.hostname=SMTP.VA.GOV

\###################################################

\# Email sender name

\#

\# For example, "noreply@va.gov".

\#

\# \*This parameter applies to National and Local.

\###################################################

email.sender=PECS_PreProd_AITC@<span class="mark">REDACTED</span>

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

email.list.success=SDDPREArch@<span class="mark">REDACTED</span>

\###################################################

\# Email list for failure notifications

\#

\# Include individuals that should be notified about

\# failed FDB/FDB-Custom updates.

\#

\# \*This parameter applies to National and Local.

\###################################################

email.list.failure=SDDPREArch@<span class="mark">REDACTED</span>

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

email.list.update.available=SDDPREArch@<span class="mark">REDACTED</span>

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

locality.rdc.name=

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

locality.site.number=

\###################################################

\# Number of retained FDB-DIF incremental archives

\#

\# Due to potential site outages, it is necessary

\# to retain a certain number of FDB-DIF archives.

\#

\# \*This parameter applies to National.

\###################################################

fdb.retention=20

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

\#------------------- IMAGE PROCESSING--------------

\###################################################

image.processing.national=TRUE

image.processing.local=FALSE

\###################################################

\# The location where the image files will be stored

\#

\#

\# \*This parameter applies to National only

\###################################################

image.directory.national=/tmp/imaging/

\###################################################

\# The location where the image files will be stored

\#

\#

\# \*This parameter applies to local only

\###################################################

image.directory.local=/tmp/imaging/

\###################################################

\# The emai to send to names or group

\#

\#

\# \*This parameter applies to National only

\###################################################

image.email.sendto.national=SDDPREArch@<span class="mark">REDACTED</span>

\###################################################

\# The emai to send to names or group

\#

\#

\# \*This parameter applies to local only

\###################################################

image.email.sendto.local=SDDPREArch@<span class="mark">REDACTED</span>

# Appendix B: Combined DATUP / PECS Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

![](datup-installation-guide-national/051.png)

<span id="_Toc66785352" class="anchor"></span>Figure B‑: Combined DATUP/PECS Architecture Diagram

# Appendix C: log4j2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<?xml version="1.0" encoding="UTF-8"?\>

\<!-- Configuration has an attribute named status that you can set to trace or debug to get configuration messages from Log4J2. --\>

\<Configuration\>

\<Properties\>

\<Property name="logDir"\>DATUPLOGS\</Property\>

\<Property name="maxFileSize"\>10 MB\</Property\>

\<Property name="maxRolloverFiles"\>10\</Property\>

\<Property name="logPattern"\>%d{DEFAULT} %-5p \[%t\] \[%c:%M\] %m%n\</Property\>

\</Properties\>

\<Appenders\>

\<Console name="ConsoleAppender" target="SYSTEM_OUT"\>

\<PatternLayout\>

\<Pattern\>\${logPattern}\</Pattern\>

\</PatternLayout\>

\</Console\>

\<RollingFile name="ApacheAppender" filename="\${logDir}/apache.log" filePattern="\${logDir}/apache-%i.log"\>

\<PatternLayout\>

\<Pattern\>\${logPattern}\</Pattern\>

\</PatternLayout\>

\<Policies\>

\<OnStartupTriggeringPolicy /\>

\<SizeBasedTriggeringPolicy size="\${maxFileSize}" /\>

\</Policies\>

\<DefaultRolloverStrategy max="\${maxRolloverFiles}"/\>

\</RollingFile\>

\<RollingFile name="PepsAppender" fileName="\${logDir}/peps.log" filePattern="\${logDir}/peps-%i.log"\>

\<PatternLayout\>

\<Pattern\>\${logPattern}\</Pattern\>

\</PatternLayout\>

\<Policies\>

\<OnStartupTriggeringPolicy /\>

\<SizeBasedTriggeringPolicy size="\${maxFileSize}" /\>

\</Policies\>

\<DefaultRolloverStrategy max="\${maxRolloverFiles}"/\>

\</RollingFile\>

\<RollingFile name="FileAppender" fileName="\${logDir}/server.log" filePattern="\${logDir}/server-%i.log"\>

\<PatternLayout\>

\<Pattern\>\${logPattern}\</Pattern\>

\</PatternLayout\>

\<Policies\>

\<OnStartupTriggeringPolicy /\>

\<SizeBasedTriggeringPolicy size="\${maxFileSize}" /\>

\</Policies\>

\<DefaultRolloverStrategy max="\${maxRolloverFiles}"/\>

\</RollingFile\>

\<RollingFile name="HibernateAppender" fileName="\${logDir}/hibernate.log" filePattern="\${logDir}/hibernate-%i.log"\>

\<HTMLLayout\>

\<LocationInfo\>true\</LocationInfo\>

\<Title\>DATUP Log\</Title\>

\</HTMLLayout\>

\<Policies\>

\<OnStartupTriggeringPolicy /\>

\<SizeBasedTriggeringPolicy size="1000 MB" /\>

\</Policies\>

\<DefaultRolloverStrategy max="\${maxRolloverFiles}"/\>

\</RollingFile\>

\<RollingFile name="SpringAppender" fileName="\${logDir}/spring.log" filePattern="\${logDir}/spring-%i.log"\>

\<PatternLayout\>

\<Pattern\>\${logPattern}\</Pattern\>

\</PatternLayout\>

\<Policies\>

\<OnStartupTriggeringPolicy /\>

\<SizeBasedTriggeringPolicy size="\${maxFileSize}" /\>

\</Policies\>

\<DefaultRolloverStrategy max="\${maxRolloverFiles}"/\>

\</RollingFile\>

\<RollingFile name="StrutsAppender" fileName="\${logDir}/struts.log" filePattern="\${logDir}/struts-%i.log"\>

\<PatternLayout\>

\<Pattern\>\${logPattern}\</Pattern\>

\</PatternLayout\>

\<Policies\>

\<OnStartupTriggeringPolicy /\>

\<SizeBasedTriggeringPolicy size="\${maxFileSize}" /\>

\</Policies\>

\<DefaultRolloverStrategy max="\${maxRolloverFiles}"/\>

\</RollingFile\>

\<RollingFile name="CT" fileName="\${logDir}/ct_prod.log" filePattern="\${logDir}/ct_prod-%i.log"\>

\<PatternLayout\>

\<Pattern\>\${logPattern}\</Pattern\>

\</PatternLayout\>

\<Policies\>

\<OnStartupTriggeringPolicy /\>

\<SizeBasedTriggeringPolicy size="\${maxFileSize}" /\>

\</Policies\>

\<DefaultRolloverStrategy max="\${maxRolloverFiles}"/\>

\</RollingFile\>

\</Appenders\>

\<Loggers\>

\<logger name="org.apache.commons" level="warm" additivity="false"\>

\<AppenderRef ref="ApacheAppender" /\>

\</logger\>

\<logger name="<span class="mark">REDACTED</span>pharmacy.peps" level="debug" additivity="false"\>

\<AppenderRef ref="PepsAppender" /\>

\</logger\>

\<logger name="<span class="mark">REDACTED</span>pharmacy.ct" level="debug" additivity="false"\>

\<AppenderRef ref="PepsAppender" /\>

\</logger\>

\<logger name="<span class="mark">REDACTED</span>monitor.time.AuditTimer" level="info" additivity="false"\>

\<AppenderRef ref="FileAppender"/\>

\</logger\>

\<logger name="org.apache.beehive.netui.pageflow.internal.AdapterManager" level="warm" additivity="false"\>

\<AppenderRef ref="FileAppender"/\>

\</logger\>

\<logger name="org.hibernate" level="error" additivity="false"\>

\<AppenderRef ref="HibernateAppender" /\>

\</logger\>

\<logger name="org.aspectj" level="error" additivity="false"\>

\<AppenderRef ref="SpringAppender" /\>

\</logger\>

\<logger name="org.springframework" level="error" additivity="false"\>

\<AppenderRef ref="SpringAppender" /\>

\</logger\>

\<logger name="org.apache.struts2" level="error" additivity="false"\>

\<AppenderRef ref="StrutsAppender" /\>

\</logger\>

\<logger name="com.opensymphony.xwork2" level="error" additivity="false"\>

\<AppenderRef ref="StrutsAppender" /\>

\</logger\>

\<logger name="org.apache.commons.digester" level="error" additivity="false"\>

\<AppenderRef ref="StrutsAppender" /\>

\</logger\>

\<logger name="org.apache.tiles" level="error" additivity="false"\>

\<AppenderRef ref="StrutsAppender" /\>

\</logger\>

\<logger name="net.sf.navigator" level="error" additivity="false"\>

\<AppenderRef ref="StrutsAppender" /\>

\</logger\>

\<Root level="error"\>

\<AppenderRef ref="ConsoleAppender"/\>

\</Root\>

\</Loggers\>

\</Configuration\>

# Appendix D: Rollback Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the installation process must be stopped when updating an environment from a previous version of DATUP National, follow the steps outlined in order to rollback the application.

1.  Follow the PECS and PPS-N Rollback Process. The PECS Rollback Process is found in the *PECS_Installation_Guide.docx*. The PPS-N Rollback Process is found in the PPS-N Install Guide, titled *PPS-N_V1.1.10_IG.docx*. Both documents can be found on the PECS TSPR site: http://tspr.vista.<span class="mark">REDACTED</span>/warboard/anotebk.asp?proj=1474&Type=Active
2.  Deploy the old DATUP National EAR file.

[^1]: At the time of development, this product was known as FDB Drug Information Framework (commonly abbreviated as FDB-DIF). The references to FDB-DIF in this manual are necessary due to previously completed code and instructions that could not be changed to match the new product name.