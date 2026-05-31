---
title: PECS Version 6.2 Installation Guide (Updated PREC* 6.2*3)
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: (Updated PREC* 6.2*3)
app_code: PECS
app_name: 'Pharmacy: Pharmacy Enterprise Customization System'
section: GUI
app_status: active
pkg_ns: PECS
patch_ver: 6.2
patch_id: PECS*6.2
group_key: PECS:PECS:6.2
file_numbers: []
security_keys: []
menu_options: 0
description: Refer to the SOFTWARE library version of this document to view REDACTED
audience: System administrators performing installation
keywords: []
page_count: 0
word_count: 7793
section_count: 14
table_count: 7
figure_count: 10
appendix_count: 5
has_toc: false
is_stub: false
pub_date: April 2022
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/pecs_installation_guide_r.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Pharm_Enterprise_Custom_Sys/pecs_installation_guide_r.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=204
audit_applied: '2026-05-31'
master_source: PECS Version 6.2 Installation Guide (Updated PREC* 6.2*3)
master_pub_date: April 2022
consolidated_from: 3 versions
prior_versions:
- PECS Installation Guide (PREC*6.2*1)
- PREC*7*1 PECS Installation Guide
consolidated_title: pecs installation guide
---

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/001.png)

April 2022

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

Refer to the SOFTWARE library version of this document to view <span class="mark">REDACTED</span> information.

<table>
<caption><p>Table 1: Definitions</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 51%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>April 2022</td>
<td>3.41</td>
<td><p>PREC*6.2*3:</p>
<ul>
<li><p>Updated the WebLogic version to 12.2.1.4 in sections <strong><u>1.1 Assumptions</u></strong> and <strong><u>C.1 Logical Deployment Design – PECS</u></strong></p></li>
<li><p>Updated <strong><u>Figure 4</u></strong></p></li>
<li><p>Updated Log4j versions to 2.17.1, removed step 1, and updated step 2,3 and 4 in section, <strong><u>5.7 Configure log4j2.xml</u></strong></p></li>
<li><p>Updated Title page, Revision History, Table of Contents, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>June 2021</td>
<td>3.40</td>
<td><p>PREC*6.2*1:</p>
<ul>
<li><p>Updated PECS 6.1 version references to 6.2</p></li>
<li><p>Updated <strong><u>Figure 1</u></strong> and <strong><u>Figure 10</u></strong></p></li>
<li><p>Updated the entire section of <strong><u>5.7 Configure log4j2.xml</u></strong></p></li>
<li><p>Updated the entire section of <strong><u>Properties of log4j2</u></strong></p></li>
<li><p>Updated formatting throughout the document</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, and Footers</p></li>
<li><p>See the non-redacted prec_6_2_p1_ig on the SOFTWARE library for viewing <mark>REDACTED</mark> information</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>July 2017</td>
<td>3.31</td>
<td>Made updates for PECS v6.1 which addresses 2FA Compliance and IAM SSOi intergration for PIV authentication</td>
<td><p><mark>REDACTED</mark></p>
<p>Enterprise Application Maintenance</p></td>
</tr>
<tr class="even">
<td>May 2016</td>
<td>3.30</td>
<td>Made updates to PECS 6.0.01<br />
508 conformance edit</td>
<td><mark>REDACTED</mark><br />
<mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/24/2013</td>
<td>3.26</td>
<td>Minor text and graphics updates;</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/19/2013</td>
<td>3.25</td>
<td>Updated the Database Installation Instructions</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/22/2013</td>
<td>3.24</td>
<td>Updated Database Installation diagram, removed FDB_DIF schema from rollback process and clarified instruction.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/21/2013</td>
<td>3.22</td>
<td>Updated Database Installation and Migration instructions</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/19/2013</td>
<td>3.21</td>
<td>Added Appendix G</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/15/2013</td>
<td>3.20</td>
<td>Added parameters in exporfile.properties for quartz scheduler, and updated log4j.xml</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/20/2013</td>
<td>3.19</td>
<td>Tech Writer edits (footers)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/25/2013</td>
<td>3.18</td>
<td>Minor Updates to the Load Production Section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>02/06/2013</td>
<td>3.17</td>
<td>More Tech Writer Edits</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>02/06/2013</td>
<td>3.16</td>
<td>Technical Writer Edits</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>02/06/2013</td>
<td>3.15</td>
<td>Technical Updates to various sections(for PECS 3.0)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/6/2013</td>
<td>3.14</td>
<td>Technical Updates to various sections(for PECS 2.2)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/07/2012</td>
<td>3.13</td>
<td>Updated Revision History Numbering, updated dates</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/16/2012</td>
<td>3.12</td>
<td>Updated links, minor text updates</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/15/2012</td>
<td>3.11</td>
<td>Updated various section(Log4j template updated, help deployment section updated)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/14/2012</td>
<td>3.10</td>
<td>Added additional configure.exportfile.properties</td>
<td><mark>REDACTED</mark>, <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/11/2012</td>
<td>3.9</td>
<td>Updated various sections to deploy PECS Help Build file</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/10/2012</td>
<td>3.8</td>
<td>Formatting updates</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/17/2012</td>
<td>3.7</td>
<td>Modified the import data production steps to disable database constraints when loading data and re-enable them once complete.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/20/2012</td>
<td>3.6</td>
<td>Formatting updates; update TOC, Footers, etc.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/19/2012</td>
<td>3.5</td>
<td>Added Appendix E – Rollback Process</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/10/2012</td>
<td>3.4</td>
<td>Updated formatting and pagination; updated date references; minor spelling and grammatical edits; updated Revision History</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/09/2012</td>
<td>3.3</td>
<td>Updated version references; added instructions regarding the data listener; added step to the post-migration procedure</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/05/2012</td>
<td>3.2</td>
<td>Changed component deployment order</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/21/2012</td>
<td>3.1</td>
<td>Minor updates (table captions, step numbering, etc.)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/14/2012</td>
<td>3.0</td>
<td>Updated various Sections for database changes for v2.2.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1/20/2012</td>
<td>2.6</td>
<td>Updated pagination, edits, TOC, and release date (back to November 2011)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1/12/2012</td>
<td>2.5</td>
<td>Updated database configuration section to reflect lessons learned during the initial load by testing services</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/08/2011</td>
<td>2.4</td>
<td>Updated TOC and formatting</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/07/2011</td>
<td>2.3</td>
<td>Updated database configuration section to include procedure for importing production data and database rollback procedures</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/29/2011</td>
<td>2.2</td>
<td>Updated document version number</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>11/28/2011</td>
<td>2.1</td>
<td>Updated database configuration procedures to clarify installation and migration steps.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/10/2011</td>
<td>2.0</td>
<td><p>Updated various Sections for configuration changes for v2.1.</p>
<p>Updated formatting, acronym table, footers, and TOC.</p></td>
<td><mark>REDACTED</mark>, <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/27/2011</td>
<td>1.18</td>
<td>Updated database configuration steps to reflect current Oracle environment and PECS installation requirements</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/19/2011</td>
<td>1.17</td>
<td>Updated formatting, edits.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/11/2011</td>
<td>1.16</td>
<td>Updated various Sections. (removed section 5.2- JMS configuration and C4 as no longer needed)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/29/2011</td>
<td>1.15</td>
<td>Updated JMS Section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/22/2011</td>
<td>1.14</td>
<td>Edit formatting, apply template</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/17/2011</td>
<td>1.13</td>
<td>Updated for PECS 2.0, added Logical Deployment section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/17/2011</td>
<td>1.12</td>
<td>Added WebLogic JTA section</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/13/2010</td>
<td>1.11</td>
<td>Adjustments to JMS configurations due to a database user change.</td>
<td>PECS Team</td>
</tr>
<tr class="even">
<td>08/04/2010</td>
<td>1.10</td>
<td>Added section on configuring JMS related to CCR 2902.</td>
<td>PECS Team</td>
</tr>
<tr class="odd">
<td>03/31/2010</td>
<td>1.9</td>
<td>Added the creation of the exportfile.properties to support the sending of custom update files to an FTP server.</td>
<td>PECS Team</td>
</tr>
<tr class="even">
<td>02/10/2010</td>
<td>1.8</td>
<td>Updated Various Sections as per AITC Input</td>
<td>PECS Team-(Database Section <mark>REDACTED</mark>, WebLogic Section <mark>REDACTED</mark>.)</td>
</tr>
<tr class="odd">
<td>12/14/2009</td>
<td>1.7</td>
<td>Updated Various Sections</td>
<td>PECS Team</td>
</tr>
<tr class="even">
<td>12/7/2009</td>
<td>1.6</td>
<td>Updated Various sections</td>
<td>SwRI</td>
</tr>
<tr class="odd">
<td>9/30/2009</td>
<td>1.5</td>
<td><p>Removed content for installation of WebLogic and KAAJEE.</p>
<p>Updated Appendix A to contain log4j configuration</p></td>
<td>PECS Team</td>
</tr>
<tr class="even">
<td>08/26/2009</td>
<td>1.4</td>
<td>Added Appendix B: Custom Update File Installation</td>
<td>PECS Team</td>
</tr>
<tr class="odd">
<td>08/12/2009</td>
<td>1.3</td>
<td><p>Removed jdbc.properties reference, as this file will be accessed on the server.</p>
<p>Removed Post-Installation section, as no longer needed.</p>
<p>Added section "4.5 Add CT_VERSION table to FDB schema".</p></td>
<td>PECS Team</td>
</tr>
<tr class="even">
<td>01/06/2009</td>
<td>1.2</td>
<td>Updated database datasource driver in WebLogic setup section.</td>
<td>PECS Team</td>
</tr>
<tr class="odd">
<td>12/02/2008</td>
<td>1.1</td>
<td><p>Added log4j.properties reference.</p>
<p>Added KAAJEE jdbc.properties reference.</p>
<p>Added kaajeeConfig.xml reference.</p>
<p>Added user_staged_config WebLogic KAAJEE library directory reference.</p></td>
<td>PECS Team</td>
</tr>
<tr class="even">
<td>11/24/2008</td>
<td>1.0</td>
<td>Initial version</td>
<td>PECS Team</td>
</tr>
</tbody>
</table>

Table 1: Definitions

ProPath Template used v1.6, June 2012

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Assumptions](#assumptions)
  - [Scope](#scope)
  - [Definitions, Acronyms, and Abbreviations](#definitions-acronyms-and-abbreviations)
  - [Overview](#overview)
- [Installation Prerequisites](#installation-prerequisites)
- [Database Tier Installation](#database-tier-installation)
  - [Oracle Database](#oracle-database)
    - [Oracle Installation](#oracle-installation)
    - [Oracle Configuration](#oracle-configuration)
  - [CTSTAGING Installation Instructions](#ctstaging-installation-instructions)
    - [Create the Users](#create-the-users)
    - [Create Staging Tables and Database Objects](#create-staging-tables-and-database-objects)
    - [Modification of the FDBDIF Database](#modification-of-the-fdbdif-database)
    - [Create Public Synonyms](#create-public-synonyms)
    - [PECS Application Users](#pecs-application-users)
    - [PECS v6.2 Database Migration](#pecs-v62-database-migration)
    - [PECS v6.2 Database Migration Rollback](#pecs-v62-database-migration-rollback)
    - [PECS v6.2 Database Migration](#pecs-v62-database-migration-1)
- [Users](#users)
- [WebLogic Application Server Configuration](#weblogic-application-server-configuration)
  - [Dependency Installation](#dependency-installation)
  - [Configure WebLogic Data Sources](#configure-weblogic-data-sources)
  - [WebLogic Server Startup Configuration](#weblogic-server-startup-configuration)
  - [Configure WebLogic JTA](#configure-weblogic-jta)
  - [Configure exportfile.properties](#configure-exportfileproperties)
  - [Application Deployment](#application-deployment)
    - [PECS Application Deployment](#pecs-application-deployment)
    - [PECS Help Application Deployment](#pecs-help-application-deployment)
  - [Configure log4j2.xml](#configure-log4j2xml)
- [Post-Installation Notes](#post-installation-notes)
- [Properties of log4j2](#properties-of-log4j2)
- [Apply Custom Tables Update File](#apply-custom-tables-update-file)
- [Recover FDB-DIF Custom Tables from Load Failure](#recover-fdb-dif-custom-tables-from-load-failure)
- [PECS Logical Deployment Architecture](#pecs-logical-deployment-architecture)
- [Logical Deployment Design – PECS](#logical-deployment-design-pecs)
- [SiteMinder Web Agent on Apache Web Server – PECS](#siteminder-web-agent-on-apache-web-server-pecs)
- [PECS Database Installation Process](#pecs-database-installation-process)
- [Database Installation Process Flow – PECS](#database-installation-process-flow-pecs)
- [Rollback Process](#rollback-process)
- [PECS Upgrade Installation Instructions](#pecs-upgrade-installation-instructions)
This document describes the process used to install the VA PECS application on an instance of a WebLogic server. The PECS software is a Web-based application, packaged as a Java 2 Platform Enterprise Edition (J2EE) standardized Enterprise Application Archive (EAR) file, which is then deployed on the WebLogic server using the server's standard deployment process. The installation described in this document also outlines the steps necessary to install and configure the application's database. This includes the installation of the database schema on an Oracle server and loading data into configuration tables. The document outlines the configuration of two data sources, and the deployment of the EAR file on the WebLogic server. The installation of the PECS application assumes that the servers necessary to execute the software are configured and running as per any applicable VA standards.
In order to understand the installation and verification process, the installer should be familiar with the WebLogic console administration and Oracle 11g Database configuration.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For successful deployment of the Pharmacy Reengineering (PRE) PECS software at a site, the following assumptions must be met:

- Red Hat Enterprise Linux 5 operating system is properly installed.
- The WebLogic Server 12.2.1.4 is configured and running.
- Access to the WebLogic console is by means of a valid administrative user name and password.
- Oracle 11g Database Server is configured and running.
- Java JDK version used is 1.8.
- First Databank (FDB) Drug Information Framework (DIF) v3.3 database is installed. Installation instructions are provided in FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project's Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.
- The installation instructions are followed in the order that the sections are presented within this Installation Guide.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation steps in scope include:

- Installation of the PECS database staging schema on an existing Oracle server, and a data load into configuration tables.
- Configuration of database data sources on an existing WebLogic application server.
- Deployment of the PECS application EAR file on a configured WebLogic application server.

Processes out of scope include:

- Installation and configuration of server environments including the operating system, database server, application server, and/or any other network component as may be required to host the PECS application on the VA network.
- SiteMinder Web Agent installation and configuration, Identity and Access Management (IAM), and Single Sign On internal (SSOi) environment setup.
- FDB-DIF database installation/migration or update process.
- Process to check out the PECS codebase from the ClearCase repository and/or the build process.
- Installation details of the Java Runtime environment.
- Initial load of Pharmacy Benefits Management (PBM) customized order checks.

## Definitions, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here is a list of terms and acronyms and their definitions.

| Term                     | Definition                                                                               |
|--------------------------|------------------------------------------------------------------------------------------|
| %DATAFILE_LOCATION%      | The directory location where the PECS database schema file will be located.              |
| Data Definition Language | A computer language for describing the records, fields, and "sets" making up a database. |
| Data Source              | Database connection definition, including connection pool on an application server.      |
| Deployment Archive       | A compressed file organized in the J2EE deployment standard.                             |

Table 2: Acronyms

| Term    | Definition                                         |
|---------|----------------------------------------------------|
| AcS     | Access Services                                    |
| AITC    | Austin Information Technology Center               |
| API     | Application Program Interface                      |
| CT      | Custom Table                                       |
| DBA     | Database Administrator                             |
| DDL     | Data Definition Language                           |
| EAR     | J2EE Enterprise Application Archive file.          |
| FDB-DIF | First Databank Drug Information Framework database |
| FTP     | File Transfer Protocol                             |
| GUI     | Graphical User Interface                           |
| IAM     | Identity and Access Management                     |
| J2EE    | Java 2 Enterprise Edition                          |
| JMS     | Java Messaging Service                             |
| KAAJEE  | Kernel Authentication and Authorization for J2EE   |
| PBM     | Pharmacy Benefits Management                       |
| PECS    | Pharmacy Enterprise Customization System           |
| PIV     | Personal Identity Verification                     |
| PRE     | Pharmacy Reengineering                             |
| RDBMS   | Relational Database Management System              |
| SDS     | System Development Support                         |
| SQL     | Structured Query Language                          |
| SSOi    | Single Sign On internal                            |
| SSPI    | Security Service Provider Interface                |
| TSPR    | Technical Services Project Repository              |
| URL     | Uniform Resource Locator                           |
| VA      | Department of Veterans Affairs                     |
| 2FA     | Two Factor Authentication                          |

Table 3: FDB-DIF Database Users and Roles

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps necessary to install and configure the components required by the PECS application are outlined in the following pages. The order that the components appear in the outlined steps is the suggested installation order. Installation Prerequisites should be installed or verified on the build environment first followed by the installation of the database schema, application server configuration, and the deployment of the PECS application.

# Installation Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Installation and configuration of server environments including the operating system, database server, application server, and/or any other network component as may be required to host the PECS application on the VA network.
- SiteMinder Web Agent must be installed on the Apache web server in the PECS environment and SSL must be enabled.
- SiteMinder Web Agent on the Apache server must be configured to communicate with the IAM Policy server. IAM and SSOi services must be up and available for PECS to work.
- All Active Directory users have read-only or Requestor access to PECS. The users must have their VAUID, first and last names set in Active Directory and in the IAM Provisioning Server.
- The target production FDB-DIF database is available.

# Database Tier Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the operating system and software for the PRE PECS V.6.2 Database Tier installation and configuration. Initially install and configure the operating system and software according to the manufacturer's specifications.

## Oracle Database 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CT staging schema or PECS Database is designed to be operating system independent. The only constraint is that Oracle 11g Database Enterprise Edition Release 11.2.0.4 – Production must be properly installed and configured. The following sections describe the installation, features, user creation, and configuration for the Oracle database.

The PECS staging database user should be configured as "CTSTAGING" (CTSTAGING schema) and the FDB-DIF database user should be configured as "FDB_DIF" (FDB_DIF schema).

### Oracle Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Proper installation of the Oracle Relational Database Management System (RDBMS) is one in which the Oracle Universal Installer was used to perform an error-free installation and a general-purpose instance was created. A properly configured Oracle RDBMS is one in which the associated Oracle application development and configuration tools, namely Structured Query Language (SQL)\*Plus and Oracle Enterprise Manager, can be used to connect to the instance through a Transparent Network Substrate alias.

### Oracle Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CT staging schema or PECS Database is the primary data repository for the PECS application. The database should be installed and configured appropriately for the PECS operating environment.

Two schemas must be created for the PECS Environment within the same database instance: FDB_DIF and CTSTAGING. Prior to creation of the schemas, logical and physical environment structures must be set up for storage of the schemas database objects: tablespaces and data files. For the PECS database configuration, data and index storage are separated for each schema. Separating indexes and table data is considered an Oracle best practice and provides improved run-time performance, reporting/monitoring, and manageability.

> **NOTE:** For PECS v6.2, since there is no FDB change, this would involve installation of PECS v6.2 component only unlike in PECS v6.1.

*\[Not Applicable for PECS 6.2: There are two components to PECS 6.2 National database installation process. The first component involves the installation of the FDB_DIF v3.3. The second component installation of the PECS 6.2 schema. The first component, installation of FDB_DIF v3.3, must be completed prior to moving forward with the PECS 6.2 installation component. Installation instructions are provided in FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project's Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.\]*

## CTSTAGING Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the database scripts necessary for the installation of the PECS CTSTAGING database, and the order in which they should be executed. It is highly recommended that the PECS staging database user be configured as "CTSTAGING" and the FDB-DIF database user be configured as "FDB_DIF" as that is the usernames that are used throughout the remainder of the PECS installation documentation. Executing steps 3.2.1 – 3.2.5 in this section will result in the creation of a PECS 6.2 database. Executing step 3.2.6 will migrate an existing PECS v6.1 database to PECS v6.2 compatibility. If migrating from an existing PECS 6.1 schema with production data, then skip to 3.2.6 to migrate to PECS 6.2 compatibility. The complete PECS Database Installation Process is graphically depicted below and in Appendix E – The PECS Database Installation Process.

Figure 1: PECS 6.2 Database Installation Process

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/002.png)

To migrate an existing PECS 6.1 database schema, skip to Section 3.2.6 – PECS 6.2 Database Migration.

Prior to executing the following sections, the Oracle 11g database needs to be installed and a Database Administrator login generated with sys_dba privileges. The DBA login is necessary to run the first database script to create the tablespaces and user accounts for the remainder of the installation.

To get Install Scripts, please contact the PRE Configuration Manager, who should be identified on the project's TSPR site.

### Create the Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to creation of the schemas, logical and physical environment structures must be setup for storage of the schemas database objects: tablespaces and data files. For the PECS Database configuration data and index storage are separated for each schema. For the CTSTAGING schema two tablespaces must be created:

- CTSTAGING_DATA
- CTSTAGING_INDEX
- LOB_DATA
- LOB_INDEX

In addition, user profiles are used to standardize resource limits for PECS schemas. There are two user profiles that must be created:

- SERVICE_ACCOUNT
- USER_ACCOUNT

Before the user profiles can be created the script utlpwdmg.sql has to be executed. The script is in the RDBMS\ADMIN directory within the installation home. Consult the Oracle installation manual for the full directory path for the proposed environment.

To create the users in the database for the PECS application, the DBA will need to execute the pecs5_creation_pkg1.sql script as SYSTEM. This script will execute other scripts that will create the tablespaces, user profiles and create the CT Staging User:

- PECS5_Create_CTSTAGING_Tablespaces.sql
- pecs5_create_user_profiles_ddl.sql
- pecs5_create_user_modified.sql

Modifications should be made tailored for the current installation environment prior to running the scripts. The following steps should be followed:

1.  Open a text editor and open the PECS5_Create_CTSTAGING_Tablespaces.sql script. Replace %DATAFILE_LOCATION% with the data file directory the directory entered should already exist on the database server.

> **NOTE:** If creating a development environment, then use PECS5_Create_CTSTAGING_Tablespaces_Dev.sql instead.

2.  Login to the SQL client using a database account that has sys_dba privileges.
3.  Execute the "pecs5_creation_pkg1.sql" script.
4.  Open the "pecs5_creation_pkg1.log" file and search the log file for any errors.
5.  This process creates the temporary file dif5ctstaging.sql. Open this file and scroll to the bottom and verify the following entry at the bottom of the file 'GRANT SELECT ON FDB_DIF.FDB_VERSION TO CTSTAGING'. This will ensure that all necessary privileges were granted to the FDB tables that the CTSTAGING user needs to access.

### Create Staging Tables and Database Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create the CTSTAGING database for the PECS application, the administrator will need to execute the pecs5_creation_pkg2.sql script. This script will execute 39 other scripts that create the CTSTAGING tables and populate those tables with some initial data values. The following steps should be followed:

1.  Login to the SQL client using the CTSTAGING user account.
6.  Execute the "pecs5_creation_pkg2.sql" script.
7.  Open the pecs5_creation_pkg2.log file and search the log file for any errors.

### Modification of the FDB_DIF Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To modify the FDB-DIF data repository to work with the PECS application, the administrator will need to execute the fdb_modification_pkg3.sql script. This script will create a new table in the FDB-DIF data repository and modify one of the existing tables to change the constraints add an index.

1.  Login to the SQL client using the FDB_DIF user account.
8.  Execute the "fdb_modification_pkg3.sql" script.
9.  Open the fdb_modification_pkg3.log file and search the log file for any errors.

### Create Public Synonyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS application access spans both FDB_DIF and CTSTAGING schema objects. Public synonyms are utilized to provide seamless application access across PECS application components. To create the public synonyms, the administrator will need to execute the PECS5_Create_Public_Synonyms.sql script. This script executes two scripts: <span class="mark">PECS5_Create_FDB_Synonyms</span>.sql, <span class="mark">PECS5_Create_CTSTAGING_Synonyms</span>.sql. The following steps should be followed:

1.  Login to the SQL client using the SYSTEM account.
10. Execute the "PECS5_Create_Public_Synonyms.sql" script.
11. Open the PECS5_Create_Public_Synonyms_create\_ public_synonyms.log file and search the log file for any errors.

### PECS Application Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS database schemas have been devised to provide separation of ownership and CRUD data access levels with user/schemas and access roles assigned. Schemas/Roles that are required by the application are depicted in the cross-reference table listed below:

| User                | Schema  | Schema Owner   | Assigned Role            |
|---------------------|---------|----------------|--------------------------|
| FDB_DIF_APP_USER    | FDB_DIF | Read Only user | FDB_DIF_READ_ONLY_ROLE   |
| FDB_DIF_UPDATE_USER | FDB_DIF | CRUD user      | FDB_DIF_UPDATE_USER_ROLE |

Table 4: CTSTAGING Database Users and Roles

<table style="width:100%;">
<caption><p>Table 5: PECSJMS Database Users and Roles</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th>User</th>
<th>Schema</th>
<th>Schema Owner</th>
<th>Assigned Role</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CTSTAGING_READ_ONLY</td>
<td>CTSTAGING</td>
<td>Read Only user</td>
<td>CTSTAGING_READ_ONLY_ROLE</td>
</tr>
<tr class="even">
<td>CTSTAGING_UPDATE_USER</td>
<td>CTSTAGING</td>
<td>CRUD user</td>
<td><p>CTSTAGING_UPDATE_USER_ROLE</p>
<p>FDB_DIF_READ_ONLY_ROLE</p></td>
</tr>
</tbody>
</table>

Table 5: PECSJMS Database Users and Roles

| User             | Schema  | Schema Owner | Assigned Role         |
|------------------|---------|--------------|-----------------------|
| PECSJMS_APP_USER | PECSJMS | CRUD user    | PECSJMS_APP_USER_ROLE |

Table 6: List of PECS Schema Creation SQL Scripts

Both FDB_DIF and CTSTAGING schema owners have been created prior to this step, however, additional users are required by the application. To create the PECS application user roles and users, the administrator will need to execute the PECS5_Create_Application_Roles_Users.sql script. This script will execute scripts that create the required PECS user roles and application users. Additionally, the script will create the PECSJMS schema objects that are required by the PECS application by executing pecs_create_jms_process.sql script.

Prior to running the driver script, PECS5_Create_Application_Roles_Users.sql, modifications should be made to CreateTablespacePECSJMS.sql to tailor for the current installation environment.

The following steps should be followed:

1.  Open a text editor and open the CreateTablespacePECSJMS.sql script. Replace %DATAFILE_LOCATION% with the data file directory for the current installation environment. The directory entered should already exist on the database server.
12. Login to the SQL client using the SYSTEM account.
13. Execute the "<span class="mark">PECS5_Create_Application_Roles_Users</span>\_create_application_roles_users.sql" script.
14. Open the "<span class="mark">PECS5_Create_Application_Roles_User</span>.log" file and search the log file for any errors.

A complete listing of the PECS Schema Creation SQL Scripts invoked from the driver scripts are listed below.

| Script Description                                                                 | File Name                 |
|------------------------------------------------------------------------------------|---------------------------|
| A Master script to create the tablespace and user package script.                  | pecs5_creation_pkg1.sql   |
| Master script to create the CT staging tables and database objects package script. | pecs5_creation_pkg2.sql   |
| Master script to modify the FDB schema package script.                             | fdb_modification_pkg3.sql |

Table 7: List of PECS 6.2 Driver SQL Script

### PECS v6.2 Database Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to migrating PECS v6.1 database schema to PECS v6.2 compatibility, a backup of the database should be performed either using RMAN or Oracle 11g DataPump export utility. Securing a backup of the database is integral to the database rollback procedures in the event that the upgrade/migration needs to revert back to the prior version. Oracle DataPump utilities provide more granularity to backup specific schemas. PECS v6.1 consists of two database schemas: CTSTAGING, FDB_DIF. To back up the PECS v56.1database using Oracle DataPump utility, issue the following command logged in as a USER with DBA privileges:

- expdpDUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING,FDB_DIF CONTENT=ALL LOGFILE=\<logfilename.log\>

> *When prompted, enter the SYSTEM user id and password to complete the export and note the dump and log files for future use.*

Prior to performing the steps needed to migrate a PECS v6.1 database to PECS v6.2 compatibility, the Oracle listener for the PECS database instance should be brought down to ensure consistency and limit access during the conversion efforts. As an Oracle Administrator, the following command can be issued from the LINUX command prompt to stop the listener for the current instance: lsnrctl stop.

To migrate PECS v6.1 database schema to PECS v6.2 compatibility, the database administrator will need to execute the following database scripts as the USER specified below. Each of these scripts acts as a driver script to initiate and log migration activities. At the completion of each of the steps. Check the log file for any errors or anomalies in processing the required transactions.

| Script Description           | File Name           | User      | Log File            |
|------------------------------|---------------------|-----------|---------------------|
| PECS Migration Driver script | PECS6_migration.sql | CTSTAGING | PECS6_migration.log |

Table 8: List of PECS 6.2 SQL Scripts

Step by Step procedure to accomplish the migration is as follows:

1.  Login to the SQL client using the CTSTAGING user account.
15. Execute the "PECS6_migration.sql" script.
16. Open the "PECS6_migration.log" file and search the log file for any errors.

After all the migration steps have been completed without error, the Oracle listener for the PECS database instance should be restarted. As an Oracle Administrator, the following command can be issued from the LINUX command prompt to start the listener for the current instance: lsnrctl start.

A complete listing of the scripts invoked from the driver scripts are listed below.

| PECS 6.2 Driver Scripts | Description                                               | Purpose                           |
|-------------------------|-----------------------------------------------------------|-----------------------------------|
| PECS6_migration.sql     | Driver Script to migrate from PECS 6.1 to PECS 6.2 schema | Database Migration Driver Scripts |

Shows the PECS v6.2 SQL script

### PECS v6.2 Database Migration Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to migrating PECS v6.1 database schema to PECS v6.2 compatibility, a backup of the database was performed to ensure rollback capability. This section addresses the steps needed to rollback to PECS v6.1 using the secured backup.

To restore the PECS v6.1 schema from the backup taken prior to the migration, follow the procedures outlined in the Data Import Guide for platform specific instructions (Unix, Windows).

Procedures for restoring/loading production data include the following steps regardless of platform:

- Prepare database for restoring production data
  - Drop existing schema objects (tables, sequences) for each schema using the Build_Script_to_Drop_CTSTAGING_objects.sql to drop all the database objects in the CTSTAGING schema. Execute the Build_Script_to_Drop_CTSTAGING_objects.sql script using the SYSTEM id and password.
- Import the CTSTAGING schema by issuing the following commands logged in as a USER with DBA privileges preferably SYSTEM:
  - impdp DUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING LOGFILE=\<logfilename.log\> CONTENT=ALL TABLE_EXISTS_ACTION=REPLACE

> *When prompted, enter the SYSTEM user id and password to complete the import. Review log files for each import to verify the successful completion of the rollback.*Note: The migration and rollback process for the PECS database does not impact the FDB_DIF schema.

### PECS v6.2 Database Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS v6.2 is integrated with IAM SSOi through the SiteMinder Web Agent for PIV authentication. PECS no longer uses KAAJEE and VistA for user authentication. The user name and VAUID from Active Directory are stored in the PECS database and the user roles are managed within the PECS application.

#### PECS Database Backup

Prior to migrating PECS v6.1 database schema to PECS v6.2 compatibility, a backup of the database should be performed either using RMAN or Oracle 11g DataPump export utility. Securing a backup of the database is integral to the database rollback procedures in the event that the upgrade/migration needs to revert back to the prior version. Oracle DataPump utilities provide more granularity to backup specific schemas. PECS v6.1 consists of two database schemas: CTSTAGING, FDB_DIF. To back up the PECS v6.1 database using Oracle DataPump utility, issue the following command logged in as a USER with DBA privileges:

- expdpDUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING,FDB_DIF CONTENT=ALL LOGFILE=\<logfilename.log\>

> *When prompted, enter the SYSTEM user id and password to complete the export and note the dump and log files for future use.*

#### PECS v6.2 Database Changes

The following Database changes are needed for PECS v6.2:

- A new column VAUID has been added to the PECS User table.
- The initial set of PBM NDF users with all the roles must be inserted into the PECS User table.

The following steps should be followed to alter the PECS User table:

1.  Login to the SQL client using the CTSTAGING user account.
17. Execute the "PECS61_Alter_CT_USERS_VA_Table.sql" script.
18. Open the log file and search the log file for any errors.

The following steps should be followed to insert the initial set of users into the PECS User table:

1.  Login to the SQL client using the CTSTAGING user account.
2.  Execute the "PECS61_Insert_PBM_Users \_CT_USERS_VA_Table.sql" script.
3.  Open the log file and search the log file for any errors.

#### PECS v6.2 Database Migration Rollback

To restore the PECS v6.1 schema from the backup taken prior to the migration in [section 3.2.8.1](#pecs-database-backup), follow the procedures outlined in the Data Import Guide for platform specific instructions (Unix, Windows).

Procedures for restoring/loading production data include the following steps regardless of platform:

- Prepare database for restoring production data
  - Drop existing schema objects (tables, sequences) for each schema using the Build_Script_to_Drop_CTSTAGING_objects.sql to drop all the database objects in the CTSTAGING schema. Execute the Build_Script_to_Drop_CTSTAGING_objects.sql script using the SYSTEM id and password.
- Import the CTSTAGING schema by issuing the following commands logged in as a USER with DBA privileges preferably SYSTEM:
  - impdp DUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING LOGFILE=\<logfilename.log\> CONTENT=ALL TABLE_EXISTS_ACTION=REPLACE

> *When prompted, enter the SYSTEM user id and password to complete the import. Review log files for each import to verify the successful completion of the rollback.*Note: The migration and rollback process for the PECS database does not impact the FDB_DIF schema.

# Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS uses the IAM SSOi service for user authorization. IAM SSOi authenticates users against Active Directory. PECS can be accessed by all VA users authenticated using the PIV. The user roles are managed with the PECS application. Access to user is initially limited to read-only or Requestor role in the PECS Database. If the users need additional privileges, they need to contact the PBM NDF managers to get roles with higher access privileges.

# WebLogic Application Server Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The WebLogic server configuration assumes that there is an existing WebLogic server installed and domain configured for use by the PECS application. Configuration steps to set up data sources will depend on the version of the WebLogic server. Furthermore, it is assumed that the installation of the WebLogic server and domain follows existing standards for a production environment installation. The configuration steps detailed below include the configuration of two data sources and the deployment of the PECS EAR archive.

## Dependency Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink Version 1.6.0.028 and KAAJEE Version 1.1.0.007 software packages must be installed prior to deployment of PECS on the WebLogic server. Follow the respective installation guides supplied by the VA for this software prior to continuing with this installation.

Please read Appendix C and ensure the administrative KAAJEE user is installed prior to installing the PECS EAR file.

> **NOTE:** Prior to the PECS EAR file deployment, the KAAJEE station ID configuration information must be updated to refer to the target VistA server. This information is updated in the \<station-number\> section of the WEB-INF\kaajeeConfig.xml file that is in the EAR deployment archive. Example steps to perform this process are outlined below (\*NIX based):

Explode the CT_EAR.ear file, explode CT_WEB.war inside the exploded CT_EAR.file, then edit CT_EAR.ear/CT_WEB.war/WEB-INF/ kaajeeConfig.xml to set the institution IDs.

The steps described above would literally translate to the following Linux commands:

> Edit the file:

> cp CT_EAR.ear /tmp

> cd /tmp

> mkdir CT_EAR

> cd CT_EAR

> jar -xvf ../CT_EAR.ear

> jar -xvf CT_WEB.war WEB-INF/kaajeeConfig.xml

> vi WEB-INF/kaajeeConfig.xml

> Save and restore the modified EAR file:

> jar -uvf CT_WEB.war WEB-INF/kaajeeConfig.xml

> rm -rf WEB-INF/

> mv ../CT_EAR.ear ../CT_EAR.ear.orig

> jar -cvf ../CT_EAR.ear \*

> cd ..

> rm -rf CT_EAR

## Configure WebLogic Data Sources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two data sources that need to be configured on the WebLogic administration server for the PECS application. Configuration values for the URL, Username, and Password will be dependent on where the FDB and STAGING databases have been installed. The configuration for each data source is summarized below:

> **NOTE:** Contact the DBA for the HOST_SERVER, DATABASE_SID and passwords used below. These items are bolded surrounded by percent signs below. When entering the information, do not enter the percent signs.

> Name: CTFdbData source

> JNDI Name: jdbc/CTFdbData source

> URL: jdbc:oracle:thin:@%HOST_SERVER%:%port%:%DATABASE_SID%

> Driver: oracle.jdbc.xa.client.OracleXAData source

> Username: FDB_DIF_APP_USER

> Password: %FDB_DIF_APP_USER_PASSWORD%

> Name: CTStagingData source

> JNDI Name: jdbc/CTStagingData source

> URL: jdbc:oracle:thin:@%HOST_SERVER%:%port%:%DATABASE_SID%

> Driver: oracle.jdbc.xa.client.OracleXAData source

> Username: CTSTAGING_UPDATE_USER

> Password: %CTSTAGING_UPDATE_USER_PASSWORD%

## WebLogic Server Startup Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS requires additional arguments added to the WebLogic Server's Server Start properties. This section details the steps to add the arguments to the server.

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
19. Click on Environment and then Servers on the panel found in the right column of the WebLogic console. Click on the server name corresponding to the deployment server in the Summary of Servers panel found in the right column of the WebLogic console. For reference only, see the figure below.

Figure 2: Summary of Servers

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/003.png)

20. WebLogic will now display the panel Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server is set. For reference, see the figure below.

Figure 3: Settings for Deployment Server

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/004.png)

21. Click on the Server Start tab.
22. WebLogic will now display the panel Server Start tab in the Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server is set. For reference, see the figure below.

Figure 4: Server Start Tab

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/005.png)

23. Insert the following text in the Arguments box:

    -d64 -server -Xms768m -Xmx4096m -XX:PermSize=256m -XX:MaxPermSize=512m -Djava.awt.headless=true
24. Click Save.

## Configure WebLogic JTA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application requires the Setting the JTA Transaction Timeout for processing of reports.

1.  In the WebLogic Administration Console, expand Services.
25. Click on JTA.
26. On the Configuration tab, for "Timeout Seconds", change the value to 600 (see below Console screen).
27. Click the Save button.

The WebLogic Administration Console screen should look like the following:

Figure 5: WebLogic Console Screen -- Completion

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/006.png)

## Configure exportfile.properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One functional piece of PECS allows a Release Manager to export data from the Oracle database so that it can be imported at various sites to support the Order Check process. The export file can be downloaded to the user's desktop, but a copy needs to be sent to a File Transfer Protocol (FTP) server so that it can be utilized in other server processes. To know where to place the file, a property file named exportfile.properties needs to be created. This file should reside in the DOMAIN_HOME/user_staged_config directory and be readable by the user who runs the WebLogic application server.

Configure the parameters in this file to match the settings of the particular environment where the installation is to be held. The export.file.server, export.file.dir, export.user.name, and export.user.pw much match the configuration of the sftp server.

The export.file.name.fragment and export.file.search.type values should both be set for the production values in the production environment, and to the Non-production values for all other environments.

The fdb.flag.provider.url value should be configured with the servername and port where DATUP National is running.

This sample exportfile.properties file is provided as an example. All parameter values should be configured for the environment where PECS is installed.

> \# Configure the following 4 sftp connection parameters to match

> \# the sftp server properties

> export.file.server=vaauspresftp02.aac.<span class="mark">REDACTED</span>

> export.file.dir=/home/presftp/pecs_ioc/fdb_dif

> export.user.name=presftp

> export.user.pw=password

> \# Cron hour 0-23

> scheduled.time.hour=06

> \# Cron minute 0-59

> scheduled.time.minute=00

> \#Production Value File Name

> \#export.file.name.fragment=UPD

> \#Production Values Search type

> \#export.file.search.type=contains

> \#Non-production Value File Name

> export.file.name.fragment=I

> \#Non-production Values Search type

> export.file.search.type=starts_with

> fdb.flag.provider.url=t3://vaauspecapp60.aac.<span class="mark">REDACTED</span>:8007

## Application Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections explain how to deploy the PECS Application and the PECS Help Application.

### PECS Application Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific deployment steps will vary depending on the version of the WebLogic server the PECS application will be deployed on. The PECS application is a J2EE application packaged in a standard EAR file format. The application should be deployed following the recommended process for deploying EAR files for the WebLogic server version platform. Use default values to deploy the Ear file and associate it with domain/server as per WebLogic install for PECS.

See Appendix G for recommended steps when upgrading from a previous release of PECS.

> **NOTE:** Associate the application with the target server, and activate the application after deployment, before it can service any requests.

### PECS Help Application Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific deployment steps will vary depending on the version of the WebLogic server the PECS Help application will be deployed on. The PECS Help application is a RoboHelp application packaged in a standard EAR file format. The Help application should be deployed following the recommended process for deploying EAR files for the WebLogic server version platform. Use default values to deploy the Ear file and associate it with domain/server as per WebLogic install for PECS. Some recommended pointers for install of pecs-hlp.xxx.ear file:

- Install the deployment as an application (PECS Help application is accessible at the context root "pecsHelp").
- On deployment targets page, select the PECS managed server.
- On Optional Settings page, name the deployment – "pecs-Help".

> **NOTE:** Associate the Help application with the target server, and activate the application after deployment, before it can service any requests.

## Configure log4j2.xml

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Follow the steps in Section 5.3 to add the path to the log4j-api-2.17.1.jar and log4j-core-2.17.1.jar, slf4j-api-1.7.10.jar and wllog4j.jar on the Server Start tab of the PECS managed server.
    1.  /u01/app/Oracle_Home/wlserver/server/lib/log4j-api-2.17.1.jar
    2.  /u01/app/Oracle_Home/wlserver/server/lib/log4j-core-2.17.1.jar
    3.  /u01/app/Oracle_Home/wlserver/server/lib/slf4j-api-1.7.10.jar
    4.  /u01/app/Oracle_Home/wlserver/server/lib/wllog4j.jar
1.  Follow the steps in Section 5.3 to add the follow argument on the Server Start tab of the PECS managed server:
    1.  -Dweblogic.log.Log4jLoggingEnabled=true.
2.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at:
    1.  http://\<Deployment Machine\>:7001/console.
28. Click on Environment and then Servers on the panel found in the right column of the WebLogic console. Click on the server name corresponding to the deployment server in the Summary of Servers panel found in the right column of the WebLogic console. For reference only, see the figure below.

Figure 6: Summary of Servers

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/007.png)

29. WebLogic will now display the panel Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server is set. For reference, see the figure below.

Figure 7: Settings for Deployment Server

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/008.png)

30. Click on the Logging tab.
31. Click Advanced to expand the advanced settings.
32. Select Log4J as the Logging Implementation.

Figure 8: Advanced Logging Settings

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/009.png)

33. Click Save.

The PECS application uses log4j loggers to create and write log information to application event logs. The logging properties for the PECS application are included in Appendix A. Logger and appender configuration is included for the PECS application, and optionally the Hibernate API. Update logging properties as appropriate to the host server:

- Set logging level to "info" for production mode.
- Set "File" properties to the identified log directory on the server.
- Set "ConversionPattern" to the standard VA pattern.

The properties in Appendix A should be inserted into the existing log4j properties file that exists at the beginning of the WebLogic server class path (please use log4j.xml for reference from Appendix A).

# Post-Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to policy constraints, active links cannot be included in this document. Please copy and paste the URLs into the browser.

The entrance URL for the application is: http://%SERVER%:%PORT%/ct/public/Welcome.html.

This is a generic URL for PECS. Replace the %SERVER% and %PORT% with the server name and port number assigned to the deployment.

For example, the entrance URL for the AITC SQA server is as follows: *http://vaww.oed.portal.<span class="mark">REDACTED</span>/projects/pre/PRE_IPT_Rev/PRE_IPT_Rev_PECS2-1/default.aspx*

# Properties of log4j2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<?xml version="1.0" encoding="UTF-8"?\>

\

34. Start FDB Update Tool GUI
    - Navigate to where the FDB Update Tool has been installed and click on the GUI.bat file.
35. Configure Connection
    - Select the View Setting menu option on the GUI and input the connection data relevant to your location and select the "Save" button. A sample screen is shown.

Figure 6: Update Settings - Configure Connection

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/010.png)

36. Provide File Paths
    - Enter the path to the update and log files relevant your location. Select whether the update is incremental or complete, then the Start button. A sample screen is shown:

Figure 7: Add Paths to FDB Data Updater

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/011.png)

# Apply Custom Tables Update File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the two major steps necessary to apply the Custom Tables Update File.

1.  Verify CT_VERSION Table:

The CT_VERSION table is an additional table added to the FDB schema (as recommended by FDB) to track the PECS update file version. If the table does not exist, execute the following DDL:

CREATE TABLE FDB.CT_VERSION

(

VERSIONKEY NUMBER(6) NOT NULL,

DBVERSION VARCHAR2(5) NULL,

BUILDVERSION VARCHAR2(5) NULL,

FREQUENCY VARCHAR2(1) NULL,

ISSUEDATE VARCHAR2(8) NULL,

VERSIONCOMMENT VARCHAR2(80) NULL,

DBTYPE VARCHAR2(10) NULL

)

CREATE UNIQUE INDEX PKCTVERSION ON FDB.CT_VERSION(VERSIONKEY)

37. Execute FDB Update Tool:

The steps to apply the Custom Tables Update file are the same steps as outlined in [Apply FDBDIF Update File](#apply-fdb-dif-update-file). Instead of entering the path to the FDB-DIF update file, enter the path to the Custom Tables Update file, relevant to your location. Select whether the update is incremental or complete. Click the Start button.

# Recover FDB-DIF Custom Tables from Load Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The recover process may be necessary if a failure has occurred during the application of the PECS Update file (see [Apply Custom Tables Update File](#apply-custom-tables-update-file) step). The recovery process involves the execution of a SQL script, and verification that the data has been recovered.

- Execute Recovery
  - The recovery entails the deletion of any data that may have been loaded to the FDB_CUSTOM\_\* tables during the execution of the update process.
- Verify Data Recovery
  - Verify that the data in the FDB_CUSTOM\_\* tables has been deleted.
- Generate Full PECS Update File
  - After logging into the PECS application, a user in the Release Manager role will navigate to the Custom Update tab and click the Download New Full Update button. This will generate a PECS update file with all currently approved order check customizations.

# PECS Logical Deployment Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Logical Deployment Design – PECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application Server:

The WebLogic Application Server 12.2.1.4 will host PECS and its business services.

Database Server:

The Database Server- Oracle 11g will have Red Hat Linux Enterprise version RHEL5 as its OS. It will host the Custom Table Staging database and FDB-DIF database.

Failover Server:

There will be a Failover server. It will host both Oracle WebLogic Application Server and Oracle Database Server to provide redundancy. The figure below shows the overview of Logical Deployment Design for the PRE PECS Application.

Figure 8: PECS Deployment

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/012.png)

# SiteMinder Web Agent on Apache Web Server – PECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 9: Web Agent High-Level Diagram

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/013.png)

# PECS Database Installation Process 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Database Installation Process Flow – PECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 10: Database Installation Process

![](pecs-version-6-2-installation-guide-updated-prec-6-2-3/014.png)

# Rollback Process 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the installation process must be stopped when updating an environment from a previous version of PECS, use the following to determine and follow the steps outlined in order to roll back the application.

If both the database and the application have been deployed:

1.  Shutdown the WebLogic domain.
38. Follow the instructions in section 3.2.8.3 PECS v6.2 Database Migration Rollback in this document.
39. Start the WebLogic domain.
40. Deploy the prior version of PECS using the instructions in section 5.6 Application Deployment in this document.

If only the database has been deployed

1.  Shutdown the WebLogic domain.
41. Follow the instructions in section 3.2.8.3 PECS v6.2 Database Migration Rollback in this document.
42. Start the WebLogic domain.

# PECS Upgrade Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Stop the WebLogic managed server.
43. Delete the previous PECS deployment.
44. From the Linux server, navigate to the managed server directory that contains the tmp and stage folders. For example: /u01/app/user_projects/domains/DEVPHARMACYPECS/servers/PECS_MS1
45. Remove the tmp and stage folders and their contents from this directory.
46. Start the managed server.
47. Stop the managed server.
48. Proceed with the deployment of the new PECS ear file.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PREC*7*1 PECS Installation Guide

### FDB Updater Tool Procedure on Oracle Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

First Databank (FDB) is a major provider of drug and medical device databases that help inform healthcare professionals to make decisions. FDB partners with information system developers to deliver useful medication and medical device-related information to clinicians, business associates, and patients. FDB provides its customers a Data Updater Java application that can be used to bulk load full and incremental data supplied by FDB. It can be invoked via command line interface (CLI) or graphical interface (this document assumes invoking it via CLI). Department of Veterans Affairs clinical applications (e.g., Pharmacy Product System (PPS), Pharmacy Enterprise Customization System (PECS)) make use of the data that is maintained and provided by FDB to help personnel choose, dose, prescribe, and use medications properly and ensure the best possible health outcomes for VA patients.

| Relational Database Management System (RDBMS) | Oracle                                                              |
|-----------------------------------------------|---------------------------------------------------------------------|
| Version                                       | 11.2.0.4 / 19c                                                      |
| Utility                                       | Oracle RDBMS                                                        |
| Activity                                      | First Databank Updater Tool (FDB Vendor: https://www.fdbhealth.com) |
| Java                                          | Java 8, 11                                                          |
| OJDBC driver                                  | Ojdbc8.jar                                                          |

<span id="_Toc391381524" class="anchor"></span>Table 4: FDB45_DIF Database Users and Roles

- Hostname:
- vaausdbspec900.aac.va.gov,
- vaausdbspec901.aac.va.gov
- Database Name:
- PECDEV
- PECSQA

Pre-requisite Checks to Run FDB Updater Tool

Make sure the server is installed with has Java JDK installed (version – 8 (is preferred).

Check and confirm the Oracle home has the OJDBC jar file. If not, OJDBC jar file is required to run the updater tool. (ojdbc8.jar preferred).

The updater tool jar files along with full and incremental load files can be found on File Transfer Protocol (FTP) server:

- vaauspresftp01.aac.va.gov

Installation Procedure

Contact sys admin if the required version of Java is not installed on the DB server.

Command below should show if java is installed along with the version.

- which java

Once Java is installed, copy the FDB files from FTP server to local government furnished equipment (GFE) computer and over to the DB server where the Data load is required.

The following tools can be used to copy and transfer the files between the servers and server-local GFE

- WINSCP
- FTP client
- File-transfer-user

Create the user for transferring the files on the DB server if it doesn't exist. Files can only be copied to /tmp location.

Once the files are copied to the server, check to make sure the file permissions are intact and make sure all the files are owned by "Oracle".

- User – Oracle
- Group – oracle:dba

Below are the set of environmental variables to set on the server before running the tool:

<u>Example</u>:

Java is installed in below location:

- /u01/java/latest/

FDB Updater tool jar files are installed in below location:

- /home/oracle/updater_tool/Current/Java/

Below are the set of env variables that should be set:

export CLASSPATH=.

> export PATH=/u01/java/latest/bin:\$PATH

> export CLASSPATH=\$CLASSPATH:/home/oracle/updater_tool/Current/Java/FDBDataUpdater.jar

> export CLASSPATH=\$CLASSPATH:/u01/oracle/190/jdbc/lib

> export CLASSPATH=\$CLASSPATH:/u01/oracle/190/jdbc/lib/ojdbc10.jar

> export CLASSPATH=\$CLASSPATH:/home/oracle/updater_tool/Current/Java/FDBDataUpdaterGUI.jar

Attached below are the contents of DataSettings.txt. This file is important for the updater tool to run. Updater tool parses the file to invoke a full or incremental data load.

Specified below is an example of the data settings file (note: server hostnames, ports, and user IDs, and passwords are dummy data):

Driver=oracle.jdbc.pool.OracleDataSource

> URL=jdbc:oracle:thin:@vaausdbspps800.aac.va.gov:1651:PPSDEV91

> UID=FDBxx_xxx

> PWD=\*\*\*\*\*\*\*\*\*

> CommitMode=0

> DatabaseConnections=10

> LoadType=1

> Location=/home/oracle/updater_tool/Current/MKF45_DB/MKF45_DB.zip

> LogFile=/home/oracle/updater_tool/Current/MKF45_DB/full_load.log

> UsePreparedStatements=1

Below are additional necessary changes to be made along with the path names before running the data updater utility on the DB server where the full or incremental load along with custom tables will be processed.

Below are the options for:

Full load

- LoadType=1

Incremental Load

- LoadType=0

<u>Command to invoke the FDB Updater tool</u>

Below are the available set of command line arguments that can be used to invoke the FDB updater tool to run incremental or full loads:

> java firstdatabank.fdbdataupdater.CLI Dataupdatersettings.txt

> java -classpath "FDBDataUpdater.jar;FDBDataUpdaterGUI.jar;/u01/oracle/190/jdbc/lib/ojdbc10.jar" firstdatabank.fdbdataupdater.CLI "DataUpdaterSettings.txt"

Once the updater tool is invoked and is running, the log of the updater tool can be found in the log location specified in the datasetttings file.

The log file should provide complete details about the table names and amount of records inserted during the process.

Below is an example screenshot of the log file showing the tables and amount of records inserted:

![](prec-7-1-pecs-installation-guide/002.png)

The log file will also show if the load completed successfully with the timestamp of completion as shown in the example screenshot below:

![](prec-7-1-pecs-installation-guide/003.png)

> **NOTE:** If any table or data load errors are encountered, contact database administrator (DBA).

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation scripts needed for the software and database installation, as well as the procedure on how to set up FDB Fwk v4.5, are provided in VA GitHub EC, located in the [pecs-code](https://github.ec.va.gov/EPMO/pecs-code/tree/master/) repository docs folder.

<span id="_Toc196296885" class="anchor"></span>Figure 1: PECS Installation Scripts

![](prec-7-1-pecs-installation-guide/004.png)

### CTSTAGING Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the database scripts necessary for the installation of the PECS CTSTAGING database, and the order in which they should be executed. It is highly recommended that the PECS staging database user be configured as "CTSTAGING" and the FDB45_DIF database user be configured as "FDB45_DIF" as that is the usernames that are used throughout the remainder of the PECS installation documentation. Executing steps 3.2.1 – 3.2.5 in this section will result in the creation of a PECS 7.0 database. Executing step 3.2.6 will migrate an existing PECS v6.2 database to PECS v7.0 compatibility. If migrating from an existing PECS 6.2 schema with production data, then skip to 3.2.6 to migrate to PECS 7.0 compatibility. The complete PECS Database Installation Process is graphically depicted below.

<span id="_Ref75527382" class="anchor"></span>Figure 2: PECS 7.0 Database Installation Process

![](prec-7-1-pecs-installation-guide/005.png)

To migrate an existing PECS 6.2 database schema, skip to Section 3.2.7 PECS 7.0 Database Migration.

Prior to executing the following sections, the Oracle 19c database needs to be installed and a Database Administrator (DBA) login generated with sys_dba privileges. The DBA login is necessary to run the first database script to create the tablespaces and user accounts for the remainder of the installation.

### Create the Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to creation of the schemas, logical and physical environment structures must be setup for storage of the schemas database objects: tablespaces and data files. For the PECS Database configuration data and index storage are separated for each schema. For the CTSTAGING schema two tablespaces must be created:

- CTSTAGING_DATA
- CTSTAGING_INDEX
- LOB_DATA
- LOB_INDEX

In addition, user profiles are used to standardize resource limits for PECS schemas. There are two user profiles that must be created:

- SERVICE_ACCOUNT
- USER_ACCOUNT

Before the user profiles can be created the script utlpwdmg.sql has to be executed. The script is in the RDBMS\ADMIN directory within the installation home. Consult the Oracle installation manual for the full directory path for the proposed environment.

To create the users in the database for the PECS application, the DBA will need to execute the pecs_creation_pkg1.sql script as SYSTEM. This script will execute other scripts that will create the tablespaces, user profiles and create the CT Staging User:

- PECS_Create_CTSTAGING_Tablespaces.sql
- pecs_create_user_profiles_ddl.sql
- pecs_create_user_modified.sql

Modifications should be made tailored for the current installation environment prior to running the scripts. The following steps should be followed:

1.  Open a text editor and open the PECS_Create_CTSTAGING_Tablespaces.sql script. Replace %DATAFILE_LOCATION% with the data file directory the directory entered should already exist on the database server.
    1.  Note: If creating a development environment, then use: PECS_Create_CTSTAGING_Tablespaces_Dev.sql instead.
2.  Login to the SQL client using a database account that has sys_dba privileges.
3.  Execute the "pecs_creation_pkg1.sql" script.
4.  Open the "pecs_creation_pkg1.log" file and search the log file for any errors.
5.  This process creates the temporary file dif5ctstaging.sql. Open this file and scroll to the bottom and verify the following entry at the bottom of the file 'GRANT SELECT ON FDB_DIF.FDB_VERSION TO CTSTAGING'. This will ensure that all necessary privileges were granted to the FDB tables that the CTSTAGING user needs to access.

### Create Staging Tables and Database Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create the CTSTAGING database for the PECS application, the administrator will need to execute the pecs_creation_pkg2.sql script. This script will execute 39 other scripts that create the CTSTAGING tables and populate those tables with some initial data values. The following steps should be followed:

1.  Login to the SQL client using the CTSTAGING user account.
6.  Execute the "pecs_creation_pkg2.sql" script.
7.  Open the pecs_creation_pkg2.log file and search the log file for any errors.

### Modification of the FDB45_DIF Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To modify the FDB45_DIF data repository to work with the PECS application, the administrator will need to execute the fdb_modification_pkg3.sql script. This script will create a new table in the FDB45_DIF data repository and modify one of the existing tables to change the constraints add an index.

1.  Login to the SQL client using the FDB45_DIF user account.
8.  Execute the "fdb_modification_pkg3.sql" script.
9.  Open the fdb_modification_pkg3.log file and search the log file for any errors.

### Create Public Synonyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS application access spans both FDB45_DIF and CTSTAGING schema objects. Public synonyms are utilized to provide seamless application access across PECS application components. To create the public synonyms, the administrator will need to execute the PECS6_Create_Public_Synonyms.sql script. This script executes two scripts: <span class="mark">PECS6_Create_FDB_Synonyms</span>.<span class="mark">sql</span>, <span class="mark">PECS6_Create_CTSTAGING_Synonyms</span>.<span class="mark">sql.</span> The following steps should be followed:

1.  Login to the SQL client using the SYSTEM account.
10. Execute the "PECS5_Create_Public_Synonyms.sql" script.
11. Open the PECS5_Create_Public_Synonyms_create\_ public_synonyms.log file and search the log file for any errors.

### PECS Application Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS database schemas have been devised to provide separation of ownership and CRUD data access levels with user/schemas and access roles assigned. Schemas/Roles that are required by the application are depicted in the cross-reference table listed below:

| User                  | Schema    | Schema Owner   | Assigned Role              |
|-----------------------|-----------|----------------|----------------------------|
| FDB45_DIF_APP_USER    | FDB45_DIF | Read Only user | FDB45_DIF_READ_ONLY_ROLE   |
| FDB45_DIF_UPDATE_USER | FDB45_DIF | CRUD user      | FDB45_DIF_UPDATE_USER_ROLE |

<span id="_Toc965306" class="anchor"></span>Table 5: CTSTAGING Database Users and Roles

| User                  | Schema    | Schema Owner   | Assigned Role                                      |
|-----------------------|-----------|----------------|----------------------------------------------------|
| CTSTAGING_READ_ONLY   | CTSTAGING | Read Only user | CTSTAGING_READ_ONLY_ROLE                           |
| CTSTAGING_UPDATE_USER | CTSTAGING | CRUD user      | CTSTAGING_UPDATE_USER_ROLEFDB45_DIF_READ_ONLY_ROLE |

<span id="_Toc965307" class="anchor"></span>Table 6: PECSJMS Database Users and Roles

| User             | Schema  | Schema Owner | Assigned Role         |
|------------------|---------|--------------|-----------------------|
| PECSJMS_APP_USER | PECSJMS | CRUD user    | PECSJMS_APP_USER_ROLE |

<span id="_Toc391381525" class="anchor"></span>Table 7: List of PECS Schema Creation SQL Scripts

Both FDB45_DIF and CTSTAGING schema owners have been created prior to this step, however, additional users are required by the application. To create the PECS application user roles and users, the administrator will need to execute the PECS6_Create_Application_Roles_Users.sql script. This script will execute scripts that create the required PECS user roles and application users. Additionally, the script will create the PECSJMS schema objects that are required by the PECS application by executing pecs_create_jms_process.sql script.

Prior to running the driver script, PECS6_Create_Application_Roles_Users.sql, modifications should be made to CreateTablespacePECSJMS.sql to tailor for the current installation environment.

The following steps should be followed:

1.  Open a text editor and open the CreateTablespacePECSJMS.sql script. Replace %DATAFILE_LOCATION% with the data file directory for the current installation environment. The directory entered should already exist on the database server.
12. Login to the SQL client using the SYSTEM account.
13. Execute the "<span class="mark">PECS6_Create_Application_Roles_Users</span>\_create_application_roles_users.sql" script.
14. Open the "<span class="mark">PECS5_Create_Application_Roles_User.log</span>" file and search the log file for any errors.

A complete listing of the PECS Schema Creation SQL Scripts invoked from the driver scripts are listed below.

| Script Description                                                                 | File Name                 |
|------------------------------------------------------------------------------------|---------------------------|
| A Master script to create the tablespace and user package script.                  | pecs5_creation_pkg1.sql   |
| Master script to create the CT staging tables and database objects package script. | pecs5_creation_pkg2.sql   |
| Master script to modify the FDB schema package script.                             | fdb_modification_pkg3.sql |

<span id="_Toc391381526" class="anchor"></span>Table 8: List of PECS 7.0 Driver SQL Script

### PECS v7.0.1 Database Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to migrating PECS v6.2 database schema to PECS v7.0 compatibility, a backup of the database should be performed either using RMAN or Oracle 19c DataPump export utility. Securing a backup of the database is integral to the database rollback procedures in the event that the upgrade/migration needs to revert back to the prior version. Oracle DataPump utilities provide more granularity to backup specific schemas. PECS v6.2 consists of two database schemas: CTSTAGING, FDB45_DIF. To back up the PECS v6.2 database using Oracle DataPump utility, issue the following command logged in as a USER with DBA privileges:

- expdpDUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING,FDB45_DIF CONTENT=ALL LOGFILE=\<logfilename.log\>

> *When prompted, enter the SYSTEM user id and password to complete the export and note the dump and log files for future use.*

Prior to performing the steps needed to migrate a PECS v6.2 database to PECS v7.0 compatibility, the Oracle listener for the PECS database instance should be brought down to ensure consistency and limit access during the conversion efforts. For Oracle Administrator's, the following command can be issued from the LINUX command prompt to stop the listener for the current instance:.

To migrate PECS v6.2 database schema to PECS v7.0 compatibility, the database administrator will need to execute the following database scripts as the USER specified below. Each of these scripts acts as a driver script to initiate and log migration activities. At the completion of each of the steps. Check the log file for any errors or anomalies in processing the required transactions.

| Script Description | File Name | User | Log File |
|--------------------|-----------|------|----------|

<span id="_Toc391381527" class="anchor"></span>Table 9: List of PECS 7.0 SQL Scripts

| PECS Migration Driver script | PECS6_migration.sql | CTSTAGING | PECS_migration.log |
|------------------------------|---------------------|-----------|--------------------|

Shows the PECS v6.1 driver SQL script.

Step by Step procedure to accomplish the migration is as follows:

1.  Login to the SQL client using the CTSTAGING user account.
15. Execute the "PECS6_migration.sql" script.
16. Open the "PECS6_migration.log" file and search the log file for any errors.

After all the migration steps have been completed without error, the Oracle listener for the PECS database instance should be restarted. For Oracle Administrator's, the following command can be issued from the LINUX command prompt to start the listener for the current instance: lsnrctl start.

A complete listing of the scripts invoked from the driver scripts are listed below.

| PECS 7. Driver Scripts | Description                                               | Purpose                           |
|------------------------|-----------------------------------------------------------|-----------------------------------|
| PECS_migration.sql     | Driver Script to migrate from PECS 6.2 to PECS 7.0 schema | Database Migration Driver Scripts |

Shows the PECS v6.2 SQL script

### PECS v7.0.1 Database Migration Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to migrating PECS v6.2 database schema to PECS v7.0 compatibility, a backup of the database was performed to ensure rollback capability. This section addresses the steps needed to rollback to PECS v6.2 using the secured backup.

To restore the PECS v6.2 schema from the backup taken prior to the migration, follow the procedures outlined in the Data Import Guide for platform specific instructions (Linux, Windows).

Procedures for restoring/loading production data include the following steps regardless of platform:

- Prepare database for restoring production data
  - Drop existing schema objects (tables, sequences) for each schema using the Build_Script_to_Drop_CTSTAGING_objects.sql to drop all the database objects in the CTSTAGING schema. Execute the Build_Script_to_Drop_CTSTAGING_objects.sql script using the SYSTEM id and password.
- Import the CTSTAGING schema by issuing the following commands logged in as a USER with DBA privileges preferably SYSTEM:
  - impdp DUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING LOGFILE=\<logfilename.log\> CONTENT=ALL TABLE_EXISTS_ACTION=REPLACE

> *When prompted, enter the SYSTEM user id and password to complete the import. Review log files for each import to verify the successful completion of the rollback.*Note: The migration and rollback process for the PECS database does not impact the FDB45_DIF schema.

### PECS v7.0.1 Database Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS v7.0 is integrated with IAM SSOi through the SiteMinder Web Agent for PIV authentication. PECS no longer uses KAAJEE and VistA for user authentication. The user name and VAUID from Active Directory are stored in the PECS database and the user roles are managed within the PECS application.

#### PECS Database Backup

Prior to migrating PECS v6.2 database schema to PECS v7.0 compatibility, a backup of the database should be performed either using RMAN or Oracle 19c DataPump export utility. Securing a backup of the database is integral to the database rollback procedures in the event that the upgrade/migration needs to revert back to the prior version. Oracle DataPump utilities provide more granularity to backup specific schemas. PECS v6.2 consists of two database schemas: CTSTAGING, FDB45_DIF. To back up the PECS v6.2 database using Oracle DataPump utility, issue the following command logged in as a USER with DBA privileges:

- expdpDUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING,FDB45_DIF CONTENT=ALL LOGFILE=\<logfilename.log\>

> *When prompted, enter the SYSTEM user id and password to complete the export and note the dump and log files for future use.*

#### PECS v7.0 Database Migration Rollback

To restore the PECS v6.2 schema from the backup taken prior to the migration in [section 3.2.8.1](#pecs-database-backup), follow the procedures outlined in the Data Import Guide for platform specific instructions (Unix, Windows).

Procedures for restoring/loading production data include the following steps regardless of platform:

- Prepare database for restoring production data
  - Drop existing schema objects (tables, sequences) for each schema using the Build_Script_to_Drop_CTSTAGING_objects.sql to drop all the database objects in the CTSTAGING schema. Execute the Build_Script_to_Drop_CTSTAGING_objects.sql script using the SYSTEM id and password.
- Import the CTSTAGING schema by issuing the following commands logged in as a USER with DBA privileges preferably SYSTEM:
  - impdp DUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING LOGFILE=\<logfilename.log\> CONTENT=ALL TABLE_EXISTS_ACTION=REPLACE

> *When prompted, enter the SYSTEM user id and password to complete the import. Review log files for each import to verify the successful completion of the rollback.*Note: The migration and rollback process for the PECS database does not impact the FDB45_DIF schema.
