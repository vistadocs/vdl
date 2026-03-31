---
consolidated_title: "install guide"
app_code: PECS
doc_type: IG
master_source: "PREC*3*714 INSTALL GUIDE"
master_pub_date: July 2014
consolidated_from: 4 versions
prior_versions:
  - "PREC*5*1114 INSTALL GUIDE"
  - "PREC*6.1*717 INSTALL GUIDE"
  - "PREC*6*516 INSTALL GUIDE"
---

Pharmacy Reengineering

Pharmacy Enterprise Customization System (PECS) v3.0

Installation Guide

![](prec-3-714-install-guide/001.png)

July 2014

Office of Information and Technology (OIT)

Product Development (PD)

Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. No Change Pages document is created for this manual. Replace any previous copy with this updated version.

<table>
<caption><p><span id="_Toc347999041" class="anchor"></span>Table 1: Definitions</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 21%" />
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
<td>07/29/2014</td>
<td>All</td>
<td>PREC*3.0*1</td>
<td>Change date to actual month released</td>
</tr>
<tr class="even">
<td>05/30/2014</td>
<td>All</td>
<td>PREC*3.0*1</td>
<td><p>Added footnote describing relationship between FDB MedKnowledge Framework and FDB-DIF, updated text appropriately. Updated TOC.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/27/2014</td>
<td>All</td>
<td>PREC*3.0*1</td>
<td>Reformatted Revision History Table; fixed graphics for Section 508 compliance</td>
</tr>
<tr class="even">
<td>05/20/2013</td>
<td>All</td>
<td>PREC*3.0*1</td>
<td><p>Tech Writer edits (footers)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/25/2013</td>
<td>11</td>
<td>PREC*3.0*1</td>
<td><p>Minor Updates to the Load Production Section</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/06/2013</td>
<td>All</td>
<td>PREC*3.0*1</td>
<td><p>More Tech Writer Edits</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>02/06/2013</td>
<td>All</td>
<td>PREC*3.0*1</td>
<td><p>Technical Writer Edits</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/06/2013</td>
<td>All</td>
<td>PREC*3.0*1</td>
<td><p>Technical Updates to various sections(for PECS 3.0)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>2/6/2013</td>
<td>All</td>
<td>PREC*2.2*1</td>
<td><p>Technical Updates to various sections(for PECS 2.2)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/07/2012</td>
<td>All</td>
<td>PREC*2.2*1</td>
<td><p>Updated Revision History Numbering, updated dates</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>10/16/2012</td>
<td>All</td>
<td>PREC*2.2*1</td>
<td><p>Updated links, minor text updates</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>10/15/2012</td>
<td>A-1- A-2</td>
<td>PREC*2.2*1</td>
<td><p>Updated various section(Log4j template updated, help deployment section updated)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>09/14/2012</td>
<td>23</td>
<td>PREC*2.2*1</td>
<td><p>Added additional configure.exportfile.properties</p>
<p><mark>REDACTED</mark>, <mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>09/11/2012</td>
<td>23</td>
<td>PREC*2.2*1</td>
<td><p>Updated various sections to deploy PECS Help Build file</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>09/10/2012</td>
<td>All</td>
<td>PREC*2.2*1</td>
<td><p>Formatting updates</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/17/2012</td>
<td>11</td>
<td>PREC*2.2*1</td>
<td><p>Modified the import data production steps to disable database constraints when loading data and re-enable them once complete.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>07/20/2012</td>
<td>All</td>
<td>PREC*2.2*1</td>
<td><p>Formatting updates; update TOC, Footers, etc.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/19/2012</td>
<td></td>
<td>PREC*2.2*1</td>
<td><p>Added Appendix E – Rollback Process</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>07/10/2012</td>
<td>All</td>
<td>PREC*2.2*1</td>
<td><p>Updated formatting and pagination; updated date references; minor spelling and grammatical edits; updated Revision History</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/09/2012</td>
<td>All; 12-13</td>
<td>PREC*2.2*1</td>
<td><p>Updated version references; added instructions regarding the data listener; added step to the post-migration procedure</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>07/05/2012</td>
<td>22-23</td>
<td>PREC*2.2*1</td>
<td><p>Changed component deployment order</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>06/21/2012</td>
<td>All</td>
<td>PREC*2.2*1</td>
<td><p>Minor updates (table captions, step numbering, etc.)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>6/14/2012</td>
<td>All</td>
<td>PREC*2.2*1</td>
<td><p>Updated various Sections for database changes for v2.2.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>1/20/2012</td>
<td>All</td>
<td>N/A – no namespace</td>
<td><p>Updated pagination, edits, TOC, and release date (back to November 2011)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>1/12/2012</td>
<td>16-23</td>
<td>N/A no namespace</td>
<td><p>Updated database configuration section to reflect lessons learned during the initial load by testing services</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/08/2011</td>
<td>All</td>
<td>N/A no namespace</td>
<td><p>Updated TOC and formatting</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>12/07/2011</td>
<td>16-23</td>
<td>N/A no namespace</td>
<td><p>Updated database configuration section to include procedure for importing production data and database rollback procedures</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/29/2011</td>
<td>All</td>
<td>N/A no namespace</td>
<td><p>Updated document version number</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/28/2011</td>
<td>16-23</td>
<td>N/A no namespace</td>
<td><p>Updated database configuration procedures to clarify installation and migration steps.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/10/2011</td>
<td>All</td>
<td>N/A no namespace</td>
<td><p>Updated various Sections for configuration changes for v2.1.</p>
<p>Updated formatting, acronym table, footers, and TOC.</p>
<p><mark>REDACTED</mark>, Gina Scorca</p></td>
</tr>
<tr class="odd">
<td>9/27/2011</td>
<td>16-23</td>
<td>N/A no namespace</td>
<td><p>Updated database configuration steps to reflect current Oracle environment and PECS installation requirements</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>07/19/2011</td>
<td>All</td>
<td>N/A no namespace</td>
<td><p>Updated formatting, edits.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>07/11/2011</td>
<td>All</td>
<td>N/A no namespace</td>
<td><p>Updated various Sections. (removed section 5.2- JMS configuration and C4 as no longer needed)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>05/29/2011</td>
<td>All</td>
<td>N/A no namespace</td>
<td><p>Updated JMS Section</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/22/2011</td>
<td>All</td>
<td>N/A no namespace</td>
<td><p>Edit formatting, apply template</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/17/2011</td>
<td>23</td>
<td>N/A (First Release)</td>
<td><p>Updated for PECS 2.0, added Logical Deployment section</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>04/17/2011</td>
<td>21</td>
<td>N/A (First Release)</td>
<td><p>Added WebLogic JTA section</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>10/13/2010</td>
<td>16</td>
<td>N/A (First Release)</td>
<td><p>Adjustments to JMS configurations due to a database user change.</p>
<p>PECS Team</p></td>
</tr>
<tr class="odd">
<td>08/04/2010</td>
<td>16</td>
<td>N/A (First Release)</td>
<td><p>Added section on configuring JMS related to CCR 2902.</p>
<p>PECS Team</p></td>
</tr>
<tr class="even">
<td>03/31/2010</td>
<td>23</td>
<td>N/A (First Release)</td>
<td><p>Added the creation of the exportfile.properties to support the sending of custom update files to an FTP server.</p>
<p>PECS Team</p></td>
</tr>
<tr class="odd">
<td>02/10/2010</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated Various Sections as per AITC Input</p>
<p>PECS Team-(Database Section Sreedhar, WebLogic Section <mark>REDACTED</mark>.)</p></td>
</tr>
<tr class="even">
<td>12/14/2009</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated Various Sections</p>
<p>PECS Team</p></td>
</tr>
<tr class="odd">
<td>12/7/2009</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated Various sections</p>
<p>SwRI</p></td>
</tr>
<tr class="even">
<td>9/30/2009</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Removed content for installation of WebLogic and KAAJEE.</p>
<p>Updated Appendix A to contain log4j configuration</p>
<p>PECS Team</p></td>
</tr>
<tr class="odd">
<td>08/26/2009</td>
<td>B-1</td>
<td>N/A (First Release)</td>
<td><p>Added Appendix B: Custom Update File Installation</p>
<p>PECS Team</p></td>
</tr>
<tr class="even">
<td>08/12/2009</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Removed jdbc.properties reference, as this file will be accessed on the server.</p>
<p>Removed Post-Installation section, as no longer needed.</p>
<p>Added section “4.5 Add CT_VERSION table to FDB schema”.</p>
<p>PECS Team</p></td>
</tr>
<tr class="odd">
<td>01/06/2009</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Updated database datasource driver in WebLogic setup section.</p>
<p>PECS Team</p></td>
</tr>
<tr class="even">
<td>12/02/2008</td>
<td>A-1</td>
<td>N/A (First Release)</td>
<td><p>Added log4j.properties reference.</p>
<p>Added KAAJEE jdbc.properties reference.</p>
<p>Added kaajeeConfig.xml reference.</p>
<p>Added user_staged_config WebLogic KAAJEE library directory reference.</p>
<p>PECS Team</p></td>
</tr>
<tr class="odd">
<td>11/24/2008</td>
<td>All</td>
<td>N/A (First Release)</td>
<td><p>Initial version</p>
<p>PECS Team</p></td>
</tr>
</tbody>
</table>

<span id="_Toc347999041" class="anchor"></span>Table 1: Definitions

ProPath Template used v1.6, June 2012

*(This page included for two-sided copying.)*

Table of Contents

List of Tables

List of Figures

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Assumptions](#assumptions)
  - [Scope](#scope)
  - [Definitions, Acronyms and Abbreviations](#definitions-acronyms-and-abbreviations)
    - [Definitions](#definitions)
    - [Acronyms](#acronyms)
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
    - [Import PECS Production Data](#import-pecs-production-data)
    - [PECS v2.2 Database Migration](#pecs-v22-database-migration)
    - [PECS v3.0 Database Migration Rollback](#pecs-v30-database-migration-rollback)
- [Users](#users)
- [WebLogic Application Server Configuration](#weblogic-application-server-configuration)
  - [Dependency Installation](#dependency-installation)
  - [Configure WebLogic Datasources](#configure-weblogic-datasources)
  - [WebLogic Server Startup Configuration](#weblogic-server-startup-configuration)
  - [Configure WebLogic JTA](#configure-weblogic-jta)
  - [Configure exportfile.properties](#configure-exportfileproperties)
  - [Application Deployment](#application-deployment)
    - [PECS Application Deployment](#pecs-application-deployment)
    - [PECS Help Application Deployment](#pecs-help-application-deployment)
  - [Configure log4j.properties](#configure-log4jproperties)
- [Post-Installation Notes](#post-installation-notes)
- [Appendix A: log4j Properties](#appendix-a-log4j-properties)
- [Appendix B: Custom Update File Installation](#appendix-b-custom-update-file-installation)
  - [B.1 Introduction](#b1-introduction)
  - [B.2 Scope](#b2-scope)
  - [B.3 Update Process Prerequisites](#b3-update-process-prerequisites)
  - [B.4 Apply FDB-DIF Update File](#b4-apply-fdb-dif-update-file)
    - [B.4.1 Execute FDB Update Tool](#b41-execute-fdb-update-tool)
  - [B.5 Apply Custom Tables Update File](#b5-apply-custom-tables-update-file)
    - [B.5.1 Verify CTVERSION Table](#b51-verify-ctversion-table)
    - [B.5.2 Execute FDB Update Tool](#b52-execute-fdb-update-tool)
  - [B.6 Recover FDB-DIF Custom Tables from Load Failure](#b6-recover-fdb-dif-custom-tables-from-load-failure)
    - [B.6.1 Execute Recovery](#b61-execute-recovery)
    - [B.6.2 Verify Data Recovery](#b62-verify-data-recovery)
    - [B.6.3 Generate Full PECS Update File](#b63-generate-full-pecs-update-file)
- [Appendix C: KAAJEE](#appendix-c-kaajee)
  - [C.1 Security Keys](#c1-security-keys)
  - [C.2 Administrator User Role](#c2-administrator-user-role)
  - [C.3 Resource Adapter](#c3-resource-adapter)
- [Appendix D: PECS Logical Deployment Architecture](#appendix-d-pecs-logical-deployment-architecture)
  - [D.1 Logical Deployment Design – PECS](#d1-logical-deployment-design-pecs)
- [Appendix E: PECS Database Installation Process](#appendix-e-pecs-database-installation-process)
  - [E.1 Database Installation Process Flow – PECS](#e1-database-installation-process-flow-pecs)
- [Appendix F: Rollback Process](#appendix-f-rollback-process)
This document describes the process used to install the Department of Veterans Affairs (VA) Pharmacy Enterprise Customization System (PECS) application on an instance of a WebLogic server. The PECS software is a Web-based application, packaged as a J2EE standardized Enterprise Application Archive (EAR) file, which is then deployed on the WebLogic server using the server’s standard deployment process. The installation described in this document also outlines the steps necessary to install and configure the application’s database. This includes the installation of the database schema on an Oracle server, and loading data into configuration tables. The document outlines the configuration of two data sources, and the deployment of the EAR file on the WebLogic server. The installation of the PECS application assumes that the servers necessary to execute the software are configured and running as per any applicable VA standards.
In order to understand the installation and verification process, the installer should be familiar with the WebLogic 10.3 console administration and Oracle 11g Database configuration.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For successful deployment of the Pharmacy Reengineering (PRE) PECS software at a site, the following assumptions must be met:

- Red Hat Enterprise Linux 5 operating system is properly installed.
- The WebLogic Server 10.3.2 is configured and running.
- Access to the WebLogic console is by means of a valid administrative user name and password.
- Oracle 11g Database Server is configured and running.
- Java JDK version used is 1.6.0_14.
- FDB (First Databank) MedKnowledge[^1] v3.3 database is installed. Installation instructions are provided in the FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project’s Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.
- Kernel Authentication & Authorization for J2EE (KAAJEE) security Application Program Interface (API) setup and configured on the WebLogic Server.
- The KAAJEE(v1.1.0.007) installation documents can be reference at KAAJEE website: <span class="mark">REDACTED</span>
- The KAAJEE(v1.1.0.007) Software/API can be downloaded from KAAJEE website : <span class="mark">REDACTED</span>
- Please note that KAAJEE installation includes the KAAJEE security provider System Design Specifications (SDS) datasource on the target WebLogic server. The KAAJEE and SDS database should be configured as specified in the KAAJEE and SDS install guides respectively.
- For Configuring SDS Datasource, please contact the Technical PRE-PECS point of contact at Austin Information Technology Center (AITC). (The Uniform Resource Locator (URL), username, password will be provided).
- The above links are provided as reference; the Install Guides and Documentation are maintained by respective projects – KAAJEE, VistALink, SDS. If you are not able to reach the link (or any issue with documentation), please contact the respective group. (PRE-PECS team can also help to co-ordinate with above groups if required).
- The installation instructions are followed in the order that the sections are presented within this Installation Guide.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation steps in scope include:

- Installation of the PECS database staging schema on an existing Oracle server, and a data load into configuration tables.
- Configuration of database data sources on an existing WebLogic application server.
- Deployment of the PECS application EAR file on a configured WebLogic application server.

Processes out of scope include:

- Installation and configuration of server environments, including the operating system, database server, and application server, and/or any other network component as may be required to host the PECS application on the VA network.
- KAAJEE security API setup and configuration on the WebLogic server.
- FDB-DIF database installation/migration or update process.
- Process to add or configure users in the VistA application for authentication and authorization to the PECS application.
- Process to check out the PECS codebase from the ClearCase repository and/or the build process.
- Installation details of the Java Runtime environment.
- Initial load of Pharmacy Benefits Management (PBM) customized order checks.

## Definitions, Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here is a list of terms and acronyms and their definitions.

### Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term                     | Definition                                                                              |
|--------------------------|-----------------------------------------------------------------------------------------|
| %DATAFILE_LOCATION%      | The directory location where the PECS database schema file will be located.             |
| Data Definition Language | A computer language for describing the records, fields, and "sets" making up a database |
| Datasource               | Database connection definition, including connection pool on an application server.     |
| Deployment Archive       | A compressed file organized in the J2EE deployment standard.                            |

<span id="_Toc347999042" class="anchor"></span>Table 2: Acronyms

### Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term             | Definition                                                                                                              |
|------------------|-------------------------------------------------------------------------------------------------------------------------|
| AITC             | Austin Information Technology Center                                                                                    |
| API              | Application Program Interface                                                                                           |
| CT               | Custom Table                                                                                                            |
| DBA              | Database Administrator                                                                                                  |
| DDL              | Data Definition Language..                                                                                              |
| EAR              | J2EE Enterprise Application Archive file.                                                                               |
| FDB-DIF          | First Databank Drug Information Framework – name of database currently in use with the PECS/MOCHA Server/DATUP products |
| FDB MedKnowledge | New Name for FDB-DIF; used only for descriptions as schemas and instructions are not yet changed                        |
| FTP              | File Transfer Protocol                                                                                                  |
| GUI              | Graphical User Interface                                                                                                |
| J2EE             | Java 2 Enterprise Edition                                                                                               |
| JMS              | Java Messaging Service                                                                                                  |
| KAAJEE           | Kernel Authentication and Authorization for J2EE                                                                        |
| PECS             | Pharmacy Enterprise Customization System                                                                                |
| PBM              | Pharmacy Benefits Management                                                                                            |
| PRE              | Pharmacy Reengineering                                                                                                  |
| RDBMS            | Relational Database Management System                                                                                   |
| SDS              | System Development Support                                                                                              |
| SQL              | Structured Query Language                                                                                               |
| SSPI             | Security Service Provider Interface                                                                                     |
| TSPR             | Technical Services Project Repository                                                                                   |
| URL              | Uniform Resource Locator                                                                                                |
| VA               | Department of Veterans Affairs                                                                                          |
<span id="_Toc347999043" class="anchor"></span>Table 3 - Database Users and Roles

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps necessary to install and configure the components required by the PECS application are outlined in the following pages. The order that the components appear in the outlined steps is the suggested installation order. Installation Prerequisites should be installed or verified on the build environment first, followed by the installation of the database schema, application server configuration, and the deployment of the PECS application.

# Installation Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Installation and configuration of server environments, including the operating system, database server, and application server, and/or any other network component as may be required to host the PECS application on the VA network.
- Target production VistA implementation must have PECS users and their security keys installed.
- KAAJEE Security Service Provider Interface (SSPI) Software, VistALink Software, and the KAAJEE Security Provider installed on the WebLogic application server.
- The target production FDB-DIF database is available.

# Database Tier Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the operating system and software for the PRE PECS V.3.0 Database Tier installation and configuration. Initially, install and configure the operating system and software according to the manufacturer’s specifications.

## Oracle Database 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Custom Table (CT) staging schema or PECS Database is designed to be operating system independent. The only constraint is that Oracle 11g Database Enterprise Edition Release 11.2.0.2.0 – Production must be properly installed and configured. The following sections describe the installation, features, user creation, and configuration for the Oracle database.

| Note:                                         | Please note that the PECS staging database user should be configured as “CTSTAGING” (CTSTAGING schema) and the FDB-DIF database user should be configured as “FDB_DIF” (FDB_DIF schema). |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](prec-3-714-install-guide/002.png) |                                                                                                                                                                                          |

<span id="_Toc347999044" class="anchor"></span>Table 4. List of PECS Schema Creation SQL Scripts (TBD)

### Oracle Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Proper installation of the Oracle Relational Database Management System (RDBMS) is one in which the Oracle Universal Installer was used to perform an error-free installation and a general purpose instance was created. A properly configured Oracle RDBMS is one in which the associated Oracle application development and configuration tools, namely Structured Query Language (SQL)\*Plus and Oracle Enterprise Manager, can be used to connect to the instance through a Transparent Network Substrate alias.

### Oracle Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CT staging schema or PECS Database is the primary data repository for the PECS application. The database should be installed and configured appropriately for the PECS operating environment.

Two schemas must be created for the PECS Environment within the same database instance: FDB_DIF and CTSTAGING. Prior to creation of the schemas, logical and physical environment structures must be set up for storage of the schemas database objects: tablespaces and data files. For the PECS database configuration, data and index storage are separated for each schema. Separating indexes and table data is considered an Oracle best practice and provides improved run-time performance, reporting/monitoring, and manageability.

There are two components to PECS 3.0 National database installation process. The first component involves the installation of the FDB_DIF v3.3. The second component installation of the PECS 3.0 schema. The first component, installation of FDB_DIF v3.3, must be completed prior to moving forward with the PECS 3.0 installation component. Installation instructions are provided in FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project’s Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.

Below are the procedures to accomplish the installation of the PECS 3.0 component.

## CTSTAGING Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the database scripts necessary for the installation of the PECS CTSTAGING database, and the order in which they should be executed. It is highly recommended that the PECS staging database user be configured as “CTSTAGING” and the FDB-DIF database user be configured as “FDB_DIF” as that is the usernames that are used throughout the remainder of the PECS installation documentation. Executing steps 3.2.1 – 3.2.6 in this section will result in the creation of a PECS 3.0 database. Executing step 3.2.7 will migrate an existing PECS v2.2 database to PECS 3.0 compatibility. If you are migrating from an existing PECS 2.2 schema with production data, skip to 3.2.7 to migrate to PECS 3.0 compatibility. The complete PECS Database Installation Process is graphically depicted below and in Appendix E – The PECS Database Installation Process.

![](prec-3-714-install-guide/003.png)

<span id="_Toc347999047" class="anchor"></span>Figure 1: PECS 3.0 Database Installation Process

| Note:                                         | To migrate an existing PECS 2.2 database schema, skip to Section 3.2.7 – PECS 2.2 Database Migration. |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![](prec-3-714-install-guide/004.png) |                                                                                                       |

<span id="_Toc347999045" class="anchor"></span>Table 5: List of PECS 3.0 Driver SQL Script

Prior to executing the following sections, the Oracle 11g database needs to be installed and a Database Administrator login generated with sys_dba privileges is generated. The DBA login is necessary to run the first database script to create the tablespaces and user accounts for the remainder of the installation.

| Note:                                         | To get Install Scripts, please contact the PRE Configuration Manager, who should be identified on the project’s TSPR site. |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](prec-3-714-install-guide/005.png) |                                                                                                                            |

<span id="_Toc347999046" class="anchor"></span>Table 6: List of PECS 3.0 SQL Scripts

### Create the Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to creation of the schemas, logical and physical environment structures must be setup for storage of the schemas database objects: tablespaces and data files. For the PECS Database configuration data and index storage are separated for each schema. For the CTSTAGING schema two tablespaces must be created:

- CTSTAGING_DATA
- CTSTAGING_INDEX
- LOB_DATA
- LOB_INDEX

In addition, user profiles are used to standardize resource limits for PECS schemas. There are 2 user profiles that have to be created:

- SERVICE_ACCOUNT
- USER_ACCOUNT

Before the user profiles can be created the script utlpwdmg.sql has to be executed. The script is located in the RDBMS\ADMIN directory within your installation home. Consult Oracle installation manual for the full directory path for the proposed environment.

To create the users in the database for the PECS application, the database administrator will need to execute the pecs3_creation_pkg1.sql script as SYSTEM. This script will execute other scripts that will create the tablespaces, user profiles and create the CT Staging User:

- PECS3_Create_CTSTAGING_Tablespaces.sql
- pecs3_create_user_profiles_ddl.sql
- pecs3_create_user_modified.sql

Prior to running the scripts, modifications should be made to tailor for the current installation environment. The following steps should be followed:

1.  Open a text editor and open the PECS3_Create_CTSTAGING_Tablespaces.sql script. Replace %DATAFILE_LOCATION% with the data file directory the directory entered should already exist on the database server.

| Note:                                         | Note: If you are creating a development environment, use PECS3_Create_CTSTAGING_Tablespaces_Dev.sql instead . |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ![](prec-3-714-install-guide/006.png) |                                                                                                               |

1.  Login to the SQL client using a database account that has sys_dba privileges
2.  Execute the “pecs3_creation_pkg1.sql” script.
3.  Open the “pecs3_creation_pkg1.log” file and search the log file for any errors.
4.  This process creates the temporary file fdb_dif2ctstaging.sql. Open this file and scroll to the bottom and verify the following entry at the bottom of the file ‘GRANT SELECT ON FDB_DIF.FDB_VERSION TO CTSTAGING’. This will ensure that all necessary privileges were granted to the FDB tables that the CTSTAGING user needs to access.

### Create Staging Tables and Database Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create the CTSTAGING database for the PECS application, the administrator will need to execute the pecs3_creation_pkg2.sql script. This script will execute thirteen other scripts that create the CTSTAGING tables and populate those tables with some initial data values. The following steps should be followed:

1.  Login to the SQL client using the CTSTAGING user account.
5.  Execute the “pecs3_creation_pkg2.sql” script.
6.  Open the pecs3_creation_pkg2.log file and search the log file for any errors.

### Modification of the FDB_DIF Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To modify the FDB-DIF data repository to work with the PECS application, the administrator will need to execute the fdb_modification_pkg3.sql script. This script will create a new table in the FDB-DIF data repository and modify one of the existing tables to change the constraints add an index.

1.  Login to the sql client using the FDB_DIF user account.
7.  Execute the “fdb_modification_pkg3.sql” script.
8.  Open the fdb_modification_pkg3.log file and search the log file for any errors.

### Create Public Synonyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS application access spans both FDB_DIF and CTSTAGING schema objects. Public synonyms are utilized to provide seamless application access across PECS application components. To create the public synonyms, the administrator will need to execute the pecs3_create_public_synonyms.sql script. This scripts executes two scripts: pecs3_create_FDB_synonyms.sql, pecs3_create_CTSTAGING_synonyms.sql. The following steps should be followed:

1.  Login to the SQL client using the SYSTEM account.
2.  Execute the “pecs3_create_public_synonyms.sql” script.
3.  Open the pecs3_create\_ public_synonyms.log file and search the log file for any errors.

### PECS Application Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS database schemas have been devised to provide separation of ownership and CRUD data access levels thru the use of user/schemas and access roles assigned. Schemas/Roles that are required by the application are depicted in the cross-reference table listed below:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>User</strong></th>
<th><strong>Schema</strong></th>
<th><strong>Access Level</strong></th>
<th><strong>Assigned Role</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FDB_DIF</td>
<td>FDB_DIF</td>
<td>Schema Owner</td>
<td></td>
</tr>
<tr class="even">
<td>FDB_DIF_APP_USER</td>
<td>FDB_DIF</td>
<td>Read Only user</td>
<td>FDB_DIF_READ_ONLY_ROLE</td>
</tr>
<tr class="odd">
<td>FDB_DIF_UPDATE_USER</td>
<td>FDB_DIF</td>
<td>CRUD user</td>
<td>FDB_DIF_UPDATE_USER_ROLE</td>
</tr>
<tr class="even">
<td>CTSTAGING</td>
<td>CTSTAGING</td>
<td>Schema Owner</td>
<td></td>
</tr>
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
<tr class="odd">
<td>PECSJMS</td>
<td>PECSJMS</td>
<td>Schema Owner</td>
<td></td>
</tr>
<tr class="even">
<td>PECSJMS_APP_USER</td>
<td>PECSJMS</td>
<td>CRUD user</td>
<td>PECSJMS_APP_USER_ROLE</td>
</tr>
</tbody>
</table>

Both FDB_DIF and CTSTAGING schema owners have been create prior to this step, however, additional users are required by the application. To create the PECS application user roles and users, the administrator will need to execute the pecs3_create_application_roles_users.sql script. This script will execute scripts that create the required PECS user roles and application users. Additionally, the script will create the PECSJMS schema objects that are required by the PECS application by executing pecs_create_jms_process.sql script.

Prior to running the driver script, pecs3_create_application_roles_users.sql, modifications should be made to CreateTablespacePECSJMS.sql to tailor for the current installation environment. .

The following steps should be followed:

1.  Open a text editor and open the CreateTablespacePECSJMS.sql script. Replace %DATAFILE_LOCATION% with the data file directory for the current installation environment. The directory entered should already exist on the database server.
2.  Login to the SQL client using the SYSTEM account.
3.  Execute the “pecs3_create_application_roles_users.sql” script.
4.  Open the “pecs3_create_application_roles_users.log” file and search the log file for any errors.

VA Standard Data Services (SDS) has created and maintains standardized tables in an Oracle database (e.g., VA Institutions). These tables must be accessible to PECS as a Web-based application. Please refer to the SDS Database Installation Guide for the information necessary to install the SDS Data Service database tables, indexes and data.

KAAJEE makes internal API calls to the SDS Database/Tables located on an Oracle database. PECS is KAAJEE-enabled. The KAAJEE user ID, schema, and SSPI tables must be accessible to PECS as a Web-based application. Please refer to the KAAJEE Database Installation Guide for the information necessary to install the KAAJEE database tables, indexes and data.

A complete listing of the PECS Schema Creation SQL Scripts invoked from the driver scripts are listed below.

| Script Description                                                                | File Name                 |
|-----------------------------------------------------------------------------------|---------------------------|
| A Master script to create the tablespace and user package script.                 | pecs_creation_pkg1.sql    |
| Master script to create the ctstaging tables and database objects package script. | pecs_creation_pkg2.sql    |
| Master script to modify the FDB schema package script.                            | fdb_modification_pkg3.sql |

### Import PECS Production Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Production data from a PECS 2.2 database or development data from a PECS 3.0 database can be loaded into a newly created PECS 3.0 database using the following procedures. Once loaded, the PECS 3.0 database is fully functional and no further installation steps are necessary. Section 3.2.7 of this document is not required for this installation path.

To load Production Data from a PECS 2.2 database:

1.  Download dump file from PRE share and place in the DPDUMP directory within your environment: <span class="mark">REDACTED</span>
2.  Disable constraints prior to the load by running the following script file as SYSTEM, Build_Script_to_Disable_Constraints.sql.
3.  Truncate the concept tables from the CTSTAGING schema by running the following script file as SYSTEM, Truncate_PECS22_Concept_Tables.sql.
4.  From the command prompt, issue the following command to load PECS data from the import file: impdp parfile=PECS_Import.par. Enter SYSTEM username/password when prompted.
5.  After the load has been completed, enable constraints by running the following script file as SYSTEM, Build_Script_to_Enable_Constraints.sql. Check the log Build_Script_to_Enable_Constraints.log for errors, if any constraints failed then re-run this step after the objects have been recompiled in Step 8.
6.  Reset PECS sequences by running the command file, PECS3_Rebuild_Sequences_After_Load.sql. Run as CTSTAGING user.
7.  Create new PECS 3.0 reference table entries and modified Dose_Route label running the command file, Add_Reference_Tables_Entries_After_Load.sql. Run as CTSTAGING user.
8.  Run script to compile all schema objects and gather fresh statistics as SYSTEM, Recompile_Schema.sql.

| Note:                                         | To get the Data Import Guide and access to an export file, please contact the PRE Configuration Manager, who should be identified on the project’s TSPR site. |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](prec-3-714-install-guide/007.png) |                                                                                                                                                               |

### PECS v2.2 Database Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to migrating PECS v2.2 database schema to PECS v3.0 compatibility, a backup of the database should be performed either using RMAN or Oracle 11g DataPump export utility. Securing a backup of the database is integral to the database rollback procedures in the event that the upgrade/migration needs to revert back to the prior version. Oracle DataPump utilities provide more granularity to backup specific schemas. PECS v2.2 consists of two database schemas: CTSTAGING, FDB_DIF. To backup the PECS v2.1 database using Oracle DataPump utility, issue the following command logged in as a USER with DBA privileges:

- expdpDUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING,FDB_DIF CONTENT=ALL LOGFILE=\<logfilename.log\>

> *When prompted, enter the SYSTEM userid and password to complete the export and note the dump and log files for future use.*

Prior to performing the steps needed to migrate a PECS v2.2 database to PECS v3.0 compatibility, the Oracle listener for the PECS database instance should be brought down to ensure consistency and limit access during the conversion efforts. As an Oracle Administrator, the following command can be issued from the LINUX command prompt to stop the listener for the current instance: lsnrctl stop.

To migrate PECS v2.2 database schema to PECS v3.0 compatibility, the database administrator will need to execute the following database scripts as the USER specified below. Each of these scripts acts as a driver script to initiate and log migration activities. At the completion of each of the steps. check the log file for any errors or anomalies in processing the required transactions.

| List of PECS 3.0 Driver SQL Scripts |                     |           |                     |
|-------------------------------------|---------------------|-----------|---------------------|
| Script Description                  | File Name           | User      | Log File            |
| PECS Migration Driver script        | PECS3_migration.sql | CTSTAGING | PECS3_migration.log |

Step by Step procedure to accomplish the migration is as follows:

1.  Login to the sql client using the CTSTAGING user account.
9.  Execute the “PECS3_migration.sql” script.
10. Open the “PECS3_migration.log” file and search the log file for any errors.

After all the migration steps have been completed without error, the Oracle listener for the PECS database instance should be restarted. As an Oracle Administrator, the following command can be issued from the LINUX command prompt to start the listener for the current instance: lsnrctl start.

A complete listing of the scripts invoked from the driver scripts are listed below.

| PECS 3.0 Driver Scripts             | Description                                                                                            | Purpose                       |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------|-----------------------------------|
| PECS3_migration.sql                     | Driver Script to migrate from PECS 2.2 to PECS 3.0 schema                                                  | Database Migration Driver Scripts |
|                                         |                                                                                                            |                                   |
| New PECS 3.0 Components             | Definition                                                                                             | Purpose                       |
| CTSTAGING_3-0_Updates_DDL.sql           | Modify/Add new columns to tables                                                                           | New in PECS 3.0                   |
| FieldMetadata_DATA.sql                  | Add new FieldMetaData entries for PECS 3.0                                                                 | New in PECS 3.0                   |
| Update_Dose_Range_Labels.sql            | Modify dose range labels in FieldMetaData tables                                                           | New in PECS 3.0                   |
|                                         |                                                                                                            |                                   |
| Data Load Processing                | Description                                                                                            | Purpose                       |
| PECS22_Rebuild_Sequences_After_Load.sql | Rebuild sequences after data load                                                                          |  Data load                        |
| pecs22.par                              | PECS 3.0 data migration parameter file to be used to import data from an existing PECS 2.2 database export |  Data load                        |
| Pecs3.par                               | PECS 3.0 data migration parameter file to be used to import data from an existing PECS 3.0 database export |  Data load                        |
|                                         |                                                                                                            |                                   |

### PECS v3.0 Database Migration Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to migrating PECS v2.2 database schema to PECS v3.0 compatibility, a backup of the database was performed to ensure rollback capability. This section addresses the steps needed to rollback to PECS v2.2 using the secured backup.

To restore the PECS v2.2 schema from the backup taken prior to the migration, follow the procedures outlined in the Data Import Guide for platform specific instructions (Unix, Windows).

Procedures for restoring/loading production data include the following steps regardless of platform:

- Prepare database for restoring production data
  - Drop existing schema objects (tables, sequences) for each schema
- Import each schema by issuing the following commands logged in as a USER with DBA privileges preferably SYSTEM:
  - impdp DUMPFILE=\<dumpfilename.dmp\> SCHEMAS=FDB_DIF LOGFILE=\<logfilename.log\> CONTENT=ALL TABLE_EXISTS_ACTION=REPLACE
  - impdp DUMPFILE=\<dumpfilename.dmp\> SCHEMAS=CTSTAGING LOGFILE=\<logfilename.log\> CONTENT=ALL TABLE_EXISTS_ACTION=REPLACE

> *When prompted, enter the SYSTEM userid and password to complete the import. Review log files for each import to verify the successful completion of the rollback.*

| Note:                                         | To get the Data Import Guide, please contact the PRE Configuration Manager, who should be identified on the project’s TSPR site. |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](prec-3-714-install-guide/008.png) |                                                                                                                                  |

# Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS uses the KAAJEE framework for user authorization. KAAJEE authenticates users against the Local VistA. Access to PECS is limited to the users in the PECS VistA that are configured to have the PECS security keys. When a new users need to be added, contact an experienced Local VistA administrator. Provide the administrator with a list of users that will be needed along with their required security keys. PECS security keys are discussed in Appendix C.

# WebLogic Application Server Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The WebLogic server configuration assumes that there is an existing WebLogic server installed and domain configured for use by the PECS application. Configuration steps to set up data sources will depend on the version of the WebLogic server. Furthermore, it is assumed that the installation of the WebLogic server and domain follows existing standards for a production environment installation. The configuration steps detailed below include the configuration of two data sources and the deployment of the PECS EAR archive.

## Dependency Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink Version 1.6.0.028 and KAAJEE Version 1.1.0.007 software packages must be installed prior to deployment of PECS on the WebLogic server. Follow the respective installation guides supplied by the VA for this software prior to continuing with this installation.

Please read Appendix C and ensure the administrative KAAJEE user is installed prior to installing the PECS EAR file.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Note:</strong></th>
<th rowspan="2"><p>Please note that prior to the PECS EAR file deployment, the KAAJEE station ID configuration information must be updated to refer to the target VistA server. This information is updated in the &lt;station-number&gt; section of the WEB-INF\kaajeeConfig.xml file that is in the EAR deployment archive. Example steps to perform this process are outlined below (*NIX based):</p>
<p>Explode the CT_EAR.ear file, explode CT_WEB.war inside the exploded CT_EAR.file, then edit CT_EAR.ear/CT_WEB.war/WEB-INF/ kaajeeConfig.xml to set the institution IDs.</p></th>
</tr>
<tr class="odd">
<th>![](prec-3-714-install-guide/009.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

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

## Configure WebLogic Datasources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three datasources that need to be configured on the WebLogic administration server for the PECS application. Configuration values for the URL, Username, and Password will be dependent on where the FDB and STAGING databases have been installed. The configuration for each datasource is summarized below:

| Note:                                         | Contact the DBA for the HOST_SERVER, DATABASE_SID and passwords used below. These items are bolded surrounded by percent signs below. When entering the information, do not enter the percent signs. |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](prec-3-714-install-guide/010.png) |                                                                                                                                                                                                      |

Name: CTFdbDataSource

JNDI Name: jdbc/CTFdbDataSource

URL: jdbc:oracle:thin:@%HOST_SERVER%:1521:%DATABASE_SID%

Driver: oracle.jdbc.xa.client.OracleXADataSource

Username: FDB_DIF_APP_USER

Password: %FDB_DIF_APP_USER_PASSWORD%

Name: CTStagingDataSource

JNDI Name: jdbc/CTStagingDataSource

URL: jdbc:oracle:thin:@%HOST_SERVER%:1521:%DATABASE_SID%

Driver: oracle.jdbc.xa.client.OracleXADataSource

Username: CTSTAGING_UPDATE_USER

Password: %CTSTAGING_UPDATE_USER_PASSWORD%

Name: PECSJMS Data Source

JNDI Name: jdbc/PecsJmsDataSource

URL: jdbc:oracle:thin:@%HOST_SERVER%:1521:%DATABASE_SID%

Driver: oracle.jdbc.OracleDriver

Username: PECSJMS_APP_USER

Password: %PECSJMS_APP_USER_PASSWORD

## WebLogic Server Startup Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS requires additional arguments added to the WebLogic Server’s Server Start properties. This section details the steps to add the arguments to the server .

1.  Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://\<Deployment Machine\>:7001/console.
2.  Click on Environment and then Servers on the panel found in the right column of the WebLogic console. Click on the server name corresponding to the deployment server in the Summary of Servers panel found in the right column of the WebLogic console. For reference only, see the figure below.

    ![](prec-3-714-install-guide/011.png)

<span id="_Toc347999048" class="anchor"></span>Figure 2: Summary of Servers

3.  WebLogic will now display the panel Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server are set. For reference, see the figure below.

    ![](prec-3-714-install-guide/012.png)

<span id="_Toc347999049" class="anchor"></span>Figure 3: Settings for Deployment Server

4.  Click on the Server Start tab.
5.  WebLogic will now display the panel Server Start tab in the Settings for Deployment Server in the right column of the console, where configuration of the Deployment Server is set. For reference, see the figure below.

    ![](prec-3-714-install-guide/013.png)

<span id="_Toc277321431" class="anchor"></span>Figure 4: Server Start Tab

6.  Insert the following text in the Arguments box:
7.  -d64 -server -Xms768m -Xmx4096m -XX:PermSize=256m -XX:MaxPermSize=512m -Djava.awt.headless=true –

> Also add an argument for Log4j file. (see for reference below, modify path per your server configuration) :-

> Dlog4j.configuration=file:/u01/app/user_projects/domains/sqa_PECS/log4j.xml

8.  Click Save.

## Configure WebLogic JTA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application requires the Setting the JTA Transaction Timeout for processing of reports.

Step 1: Configure JTA

1.  In the WebLogic Administration Console, expand Services.
2.  Click on JTA.
3.  On the Configuration tab, for “Timeout Seconds”, change the value to 600.(see below Console screen)
4.  Click the Save button.

The WebLogic Administration Console screen should look similar to the following:

![](prec-3-714-install-guide/014.png)

<span id="_Toc347999051" class="anchor"></span>Figure 5: WebLogic Console Screen -- Completion

WebLogic JTA Configuration is complete.

## Configure exportfile.properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One functional piece of PECS allows a Release Manager to export data from the Oracle database so that it can be imported at various sites to support the Order Check process. The export file can be downloaded to the user’s desktop, but a copy needs to be sent to an File Transfer Protocol (FTP) server so that it can be utilized in other server processes. To know where to place the file, a property file named exportfile.properties needs to be created. This file should reside in the DOMAIN_HOME/user_staged_config directory. The properties that need to be entered in to this file are(see below for reference. Also please configure with or without leading “/” depending on relative or absolute path):

> export.file.server= <span class="mark">REDACTED</span>

> export.file.dir=/pharmacy/fdb_dif

> export.user.name=PECS

> fdb.file.dir=/pharmacy

> scheduled.time=2230

The exportfile.properties file will need to be readable by the user who runs the WebLogic application server.

## Application Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections explain how to deploy the PECS Application and the PECS Help Application.

### PECS Application Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific deployment steps will vary depending on the version of the WebLogic server the PECS application will be deployed on. The PECS application is a J2EE application packaged in a standard EAR file format. The application should be deployed following the recommended process for deploying EAR files for the WebLogic server version platform. Use default values to deploy the Ear file and associate it with domain/server as per WebLogic install for PECS.

| Note: | Please note that you must associate the application with the target server, and activate the application after deployment, before it can service any requests. |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|

### PECS Help Application Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific deployment steps will vary depending on the version of the WebLogic server the PECS Help application will be deployed on. The PECS Help application is a RoboHelp application packaged in a standard EAR file format. The Help application should be deployed following the recommended process for deploying EAR files for the WebLogic server version platform. Use default values to deploy the Ear file and associate it with domain/server as per WebLogic install for PECS. Some recommended pointers for install of pecs-hlp.xxx.ear file:

- Install the deployment as an application. (PECS Help application is accessible at the context root “pecsHelp”)
- On deployment targets page, select the PECS managed server.
- On Optional Settings page, name the deployment – “pecs-Help”

| Note:                                         | Please note that you must associate the Help application with the target server, and activate the application after deployment, before it can service any requests. |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](prec-3-714-install-guide/015.png) |                                                                                                                                                                     |

## Configure log4j.properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PECS application uses log4j loggers to create and write log information to application event logs. The logging properties for the PECS application are included in Appendix A. Logger and appender configuration is included for the PECS application, and optionally the Hibernate API. Update logging properties as appropriate to the host server:

- Set logging level to “info” for production mode
- Set “File” properties to the identified log directory on the server.
- Set “ConversionPattern” to the standard VA pattern.

The properties in Appendix A should be inserted into the existing log4j properties file that exists at the beginning of the WebLogic server classpath. (please use log4j.xml for reference from Appendix A).

# Post-Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note: Due to policy constraints, active links cannot be included in this document. Please copy and paste the URLs into your browser.*

The entrance URL for the application is: *<u>http://%SERVER%:%PORT%/ct/public/Welcome.html</u>.*

This is a generic URL for PECS. You need to replace the %SERVER% and %PORT% with the server name and port number assigned to your deployment.

For example, the entrance URL for the AITC SQA server is as follows: <span class="mark">REDACTED</span>

# Appendix A: log4j Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<?xml version="1.0" encoding="UTF-8" ?\>

\<!DOCTYPE log4j:configuration SYSTEM "log4j.dtd"\>

\<log4j:configuration xmlns:log4j="http://jakarta.apache.org/log4j/"\>

\<appender name="STDOUT" class="org.apache.log4j.ConsoleAppender"\>

\<layout class="org.apache.log4j.PatternLayout"\>

\<param name="ConversionPattern" value="%d %-5p \[%t\] %C{2} (%F:%L) - %m%n"/\>

\</layout\>

\</appender\>

\<appender name="FileAppender" class="org.apache.log4j.RollingFileAppender"\>

\<param name="File" value="PECSLogs/server.log"/\>

\<param name="Append" value="false"/\>

\<param name="MaxBackupIndex" value="10"/\>

\<layout class="org.apache.log4j.PatternLayout"\>

\<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c:%M\] %m%n"/\>

\</layout\>

\</appender\>

\<appender name="HibernateAppender" class="org.apache.log4j.RollingFileAppender"\>

\<param name="File" value="PECSLogs/hibernate.log"/\>

\<param name="Append" value="false"/\>

\<param name="MaxBackupIndex" value="10"/\>

\<layout class="org.apache.log4j.PatternLayout"\>

\<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c:%M\] %m%n"/\>

\</layout\>

\</appender\>

\<appender name="PepsAppender" class="org.apache.log4j.RollingFileAppender"\>

\<param name="File" value="PECSLogs/peps.log"/\>

\<param name="Append" value="false"/\>

\<param name="MaxBackupIndex" value="10"/\>

\<layout class="org.apache.log4j.PatternLayout"\>

\<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c:%M\] %m%n"/\>

\</layout\>

\</appender\>

\<appender name="SpringAppender" class="org.apache.log4j.RollingFileAppender"\>

\<param name="File" value="PECSLogs/spring.log"/\>

\<param name="Append" value="false"/\>

\<param name="MaxBackupIndex" value="10"/\>

\<layout class="org.apache.log4j.PatternLayout"\>

\<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c:%M\] %m%n"/\>

\</layout\>

\</appender\>

\<appender name="StrutsAppender" class="org.apache.log4j.RollingFileAppender"\>

\<param name="File" value="PECSLogs/struts.log"/\>

\<param name="Append" value="false"/\>

\<param name="MaxBackupIndex" value="10"/\>

\<layout class="org.apache.log4j.PatternLayout"\>

\<param name="ConversionPattern" value="%d{dd MMM yyyy hh:mm:ss a} %-5p \[%c:%M\] %m%n"/\>

\</layout\>

\</appender\>

\<appender name="CT" class="org.apache.log4j.RollingFileAppender"\>

\<param name="file" value="PECSLogs/ct_prod.log"/\>

\<param name="MaxFileSize" value="10000KB"/\>

\<param name="MaxBackupIndex" value="10"/\>

\<layout class="org.apache.log4j.PatternLayout"\>

\<param name="ConversionPattern" value="%d %5p %l - %m%n"/\>

\</layout\>

\</appender\>

\<appender name="PECS" class="org.apache.log4j.RollingFileAppender"\>

\<param name="file" value="PECSLogs/pecs_prod.log"/\>

\<param name="MaxFileSize" value="10000KB"/\>

\<param name="MaxBackupIndex" value="10"/\>

\<layout class="org.apache.log4j.PatternLayout"\>

\<param name="ConversionPattern" value="%d %5p %l - %m%n"/\>

\</layout\>

\</appender\>

\<logger name="<span class="mark">REDACTED</span>pharmacy.ct" additivity="false"\>

\<level value="debug"/\>

\<appender-ref ref="CT" /\>

\</logger\>

\<logger name="<span class="mark">REDACTED</span>pharmacy.pecs" additivity="false"\>

\<level value="debug"/\>

\<appender-ref ref="PECS" /\>

\</logger\>

\<logger name="<span class="mark">REDACTED</span>pharmacy.ct.web" additivity="false"\>

\<level value="debug"/\>

\<appender-ref ref="CT" /\>

\</logger\>

\<!-- INFO-level logger: turn on to record timing audit information --\>

\<logger name="<span class="mark">REDACTED</span>monitor.time.AuditTimer" additivity="false" \>

\<level value="info" /\>

\<appender-ref ref="FileAppender"/\>

\</logger\>

\<logger name="org.apache.beehive.netui.pageflow.internal.AdapterManager" additivity="false" \>

\<level value="warn" /\>

\<appender-ref ref="FileAppender"/\>

\</logger\>

\<logger name="org.apache.log4j"\>

\<level value="info" /\>

\</logger\>

\<logger name="org.hibernate" additivity="false"\>

\<level value="info" /\>

\<appender-ref ref="HibernateAppender"/\>

\</logger\>

\<logger name="org.hibernate.type" additivity="false"\>

\<level value="warn" /\>

\<appender-ref ref="HibernateAppender"/\>

\</logger\>

\<logger name="org.hibernate.loader" additivity="false"\>

\<level value="warn" /\>

\<appender-ref ref="HibernateAppender"/\>

\</logger\>

\<logger name="org.hibernate.impl" additivity="false"\>

\<level value="warn" /\>

\<appender-ref ref="HibernateAppender"/\>

\</logger\>

\<logger name="org.springframework" additivity="false"\>

\<level value="error" /\>

\<appender-ref ref="SpringAppender"/\>

\</logger\>

\<logger name="org.apache.struts2" additivity="false"\>

\<level value="error" /\>

\<appender-ref ref="StrutsAppender" /\>

\</logger\>

\<logger name="com.opensymphony.xwork2" additivity="false"\>

\<level value="error" /\>

\<appender-ref ref="StrutsAppender" /\>

\</logger\>

\<logger name="org.apache.commons.digester" additivity="false"\>

\<level value="error" /\>

\<appender-ref ref="StrutsAppender" /\>

\</logger\>

\<logger name="freemarker.cache" additivity="false"\>

\<level value="error" /\>

\<appender-ref ref="StrutsAppender" /\>

\</logger\>

\<logger name="org.apache.tiles" additivity="false"\>

\<level value="error" /\>

\<appender-ref ref="StrutsAppender" /\>

\</logger\>

\<logger name="net.sf.navigator" additivity="false"\>

\<level value="error" /\>

\<appender-ref ref="StrutsAppender" /\>

\</logger\>

\<logger name="org.displaytag" additivity="false"\>

\<level value="error" /\>

\<appender-ref ref="StrutsAppender" /\>

\</logger\>

\<logger name="org.apache.commons"\>

\<level value="warn" /\>

\</logger\>

\<logger name="<span class="mark">REDACTED</span>pharmacy.peps" additivity="false"\>

\<level value="error" /\>

\<appender-ref ref="PepsAppender"/\>

\</logger\>

\<root\>

\<priority value="info" /\>

\<appender-ref ref="FileAppender"/\>

\<appender-ref ref="HibernateAppender"/\>

\<appender-ref ref="SpringAppender"/\>

\<appender-ref ref="StrutsAppender"/\>

\<appender-ref ref="STDOUT"/\>

\<appender-ref ref="CT"/\>

\<appender-ref ref="PECS"/\>

\</root\>

\</log4j:configuration\>

# Appendix B: Custom Update File Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## B.1 Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix describes the process to load the FDB-DIF and PECS update files into an existing FDB-DIF Oracle database using the FDB Updater Tool. The FDB-DIF update file is received on a schedule from FDB every two weeks and must be loaded in sequence. The PECS update file can be generated from the PECS application interface at any time by a user in the Release Manager role, and loaded with the FDB Update Tool.

## B.2 Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix will include the process to update the FDB-DIF Oracle database with the FDB and PECS Update files using the FDB Update Tool

Processes in scope will include:

- The process to load the FDB-DIF file using the FDB Update Tool.
- The process to load the PECS update file using the FDB Update Tool.
- The process to recover the FDB-DIF FDB_CUSTOM\_\* tables if a Custom Tables update file load failure should occur.

Processes out of scope will include:

- The process to receive the FDB-DIF update file from FDB.
- The process to generate the PECS update file from the Custom Tables application.
- The process to recover the FDB-DIF database if an FDB-DIF update file load failure should occur.

## B.3 Update Process Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The FDB Updater Tool is installed on the machine performing the update process.
- The FDB and PECS update files are available and/or have been generated.
- The FDB-DIF update file must be loaded in sequence. The version number of the new file must be the next in sequence.
- The user performing Oracle operations must have sufficient rights to delete data, drop, and create tables.
- The PECS preparation and recovery SQL scripts are available.
- An Oracle tool such as SQLPlus, must be installed on the machine executing the FDB Updater tool.

## B.4 Apply FDB-DIF Update File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the steps necessary to apply the FDB-DIF Update file.

### B.4.1 Execute FDB Update Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here are the steps required to execute the FDB update tool (four steps):

Obtain the FDB-DIF Update File

Either download the update file from the FTP directory, or insert the update CD into drive.

Start FDB Update Tool GUI

Navigate to where the FDB Update Tool has been installed, and click on the GUI.bat file.

Configure Connection

Select the View -\> Setting menu option on the GUI and input the connection data relevant to your location and click the “Save” button. A sample screen is shown.

![](prec-3-714-install-guide/016.png)

Provide File Paths

Enter the path to the update and log files relevant to your location. Select whether the update is incremental or complete. Click the “Start” button. A sample screen is shown:

![](prec-3-714-install-guide/017.png)

## B.5 Apply Custom Tables Update File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the two major steps necessary to apply the Custom Tables Update File.

### B.5.1 Verify CT_VERSION Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CT_VERSION table is an additional table added to the FDB schema (as recommended by FDB) to track the PECS update file version. If the table does not exist, execute the following DDL:

CREATE TABLE FDB.CT_VERSION

(

VERSIONKEY NUMBER(6) NOT NULL,

DBVERSION VARCHAR2(5) NULL,

> BUILDVERSION VARCHAR2(5) NULL,

FREQUENCY VARCHAR2(1) NULL,

ISSUEDATE VARCHAR2(8) NULL,

VERSIONCOMMENT VARCHAR2(80) NULL,

DBTYPE VARCHAR2(10) NULL

)

CREATE UNIQUE INDEX PKCTVERSION ON FDB.CT_VERSION(VERSIONKEY)

### B.5.2 Execute FDB Update Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps to apply the Custom Tables Update file are the same steps as outlined in [Apply FDB DIF Update File](#b.4-apply-fdb-dif-update-file). Instead of entering the path to the FDB-DIF update file, enter the path to the Custom Tables Update file, relevant to your location. Select whether the update is incremental or complete. Click the “Start” button.

## B.6 Recover FDB-DIF Custom Tables from Load Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The recover process may be necessary if a failure has occurred during the application of the PECS Update file (see [Apply Custom Tables Update File](#b.5-apply-custom-tables-update-file) step). The recovery process involves the execution of a SQL script, and verification that the data has been recovered.

### B.6.1 Execute Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The recovery entails the deletion of any data that may have been loaded to the FDB_CUSTOM\_\* tables during the execution of the update process.

### B.6.2 Verify Data Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that the data in the FDB_CUSTOM\_\* tables has been deleted.

### B.6.3 Generate Full PECS Update File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After logging into the PECS application, a user in the Release Manager role will navigate to the “Custom Update” tab, and click the “Download New Full Update” button. This will generate a PECS update file with all currently approved order check customizations.

# Appendix C: KAAJEE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS uses the KAAJEE framework for user authorization and authentication. KAAJEE authenticates users against the Local VistA. Access to PECS is limited to known users with the security role. If new users need to be added, contact an experienced Local VistA administrator. Provide the administrator with a list of users that will be needed along with their required security keys. PECS security keys are discussed in the next section.

## C.1 Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After a user is authenticated, KAAJEE retrieves his or her security keys from VistA and maps them to WebLogic security roles. The PECS application is secured so that only users running with the PECS security roles may access the PECS application.

PECS relies on the following four security keys, which must be added to VistA:

- PSS_CUSTOM_TABLES_ADMIN
- PSS_CUSTOM_TABLES_APPROVER
- PSS_CUSTOM_TABLES_REL_MAN
- PSS_CUSTOM_TABLES_REQUESTOR

PRE will rollout VISTA Patch, PSS\*1\*147 which exports the Security Keys, and those Security Keys are technically in the PSS namespace. These security keys have to be associated with the user accounts that will be set up on a VistA M server. The process for setting up the user accounts and the security keys is a part of the VistALink API setup mentioned in the VistALink Installation Manual available with the API software at: <span class="mark">REDACTED</span>

*Note:* <span class="mark">REDACTED</span>

## C.2 Administrator User Role

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PECS is configured to use the KAAJEE administrator user role by default. This requires the creation of a KAAJEE administrator account in WebLogic if one does not exist.

## C.3 Resource Adapter 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Resource Adapter with the supporting jars included in it and do not deploy jars as library files. The deployment order for the Resource Adapter must be at a lower number than the deployment order for PECS. This is to make sure the Resource Adapter is loaded and that the classes in the Resource Adapter are available when PECS is started. It is recommended to set the deployment order for the Resource Adapter to 95 or 99. This is because the default deployment order is 100.

*(This page included for two-sided copying.)*

# Appendix D: PECS Logical Deployment Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## D.1 Logical Deployment Design – PECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application Server:

The WebLogic Application Server 10.3 will host PECS and its business services.

Database Server:

The Database Server- Oracle 11g will have Red Hat Linux Enterprise version RHEL5 as it OS. It will host the Custom Table Staging database and FDB-DIF (eventually MedKnowledge) database.

Failover Server:

There will be a Failover server. It will host both BEA WebLogic Application Server and Oracle Database Server to provide redundancy.

Legacy Interface:

There will be an existing VistA server which will host legacy KAAJEE and VistALink interface.

The figure below shows the overview of Logical Deployment Design for the PRE PECS Application.

![](prec-3-714-install-guide/018.png)

<span id="_Toc347999052" class="anchor"></span>Figure 6: PECS Deployment

# Appendix E: PECS Database Installation Process 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## E.1 Database Installation Process Flow – PECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prec-3-714-install-guide/019.png)

<span id="_Toc347999053" class="anchor"></span>Figure 7: Database Installation Process

*(This page included for two-sided copying.)*

# Appendix F: Rollback Process 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the installation process must be stopped when updating an environment from a previous version of PECS, use the following to determine and follow the steps outlined in order to rollback the application.

If both the database and the application have been deployed…

1.  Shutdown the WebLogic domain.
2.  Follow the instructions in section 3.2.8 PECS v3.0 Database Migration Rollback in this document.
3.  Start the WebLogic domain.
4.  Deploy the prior version of PECS using the instructions in section 5.6 Application Deployment in this document.

If only the database has been deployed

1.  Shutdown the WebLogic domain.
2.  Follow the instructions in section 3.2.8 PECS v3.0 Database Migration Rollback in this document.
3.  Start the WebLogic domain.

*(This page included for two-sided copying.)*

[^1]: At the time of development, this product was known as FDB Drug Information Framework (commonly abbreviated as FDB-DIF). The references to FDB-DIF in this manual are necessary due to previously completed code and instructions that could not be changed to match the new product name.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PREC*6.1*717 INSTALL GUIDE

## Definitions, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here is a list of terms and acronyms and their definitions.

### Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term                     | Definition                                                                               |
|--------------------------|------------------------------------------------------------------------------------------|
| %DATAFILE_LOCATION%      | The directory location where the PECS database schema file will be located.              |
| Data Definition Language | A computer language for describing the records, fields, and "sets" making up a database. |
| Datasource               | Database connection definition, including connection pool on an application server.      |
| Deployment Archive       | A compressed file organized in the J2EE deployment standard.                             |

Table : Acronyms

### Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
Table 3 - Database Users and Roles

### From: PREC*5*1114 INSTALL GUIDE

### June 2014

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs Office of Information and Technology (OIT)

### Product Development (PD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Revision History

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 55%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
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
<td>06/24/2014</td>
<td><blockquote>
<p>Minor text and graphics updates;</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>12/19/2013</td>
<td><blockquote>
<p>Updated the Database Installation Instructions</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11/22/2013</td>
<td><blockquote>
<p>Updated Database Installation diagram, removed FDB_DIF schema from rollback process and clarified instruction.</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>11/21/2013</td>
<td><blockquote>
<p>Updated Database Installation and Migration instructions</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11/19/2013</td>
<td><blockquote>
<p>Added Appendix G</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>11/15/2013</td>
<td><blockquote>
<p>Added parameters in exporfile.properties for quartz scheduler, and updated log4j.xml</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>05/20/2013</td>
<td><blockquote>
<p>Tech Writer edits (footers)</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/25/2013</td>
<td><blockquote>
<p>Minor Updates to the Load Production Section</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>02/06/2013</td>
<td><blockquote>
<p>More Tech Writer Edits</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>02/06/2013</td>
<td><blockquote>
<p>Technical Writer Edits</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>02/06/2013</td>
<td><blockquote>
<p>Technical Updates to various sections(for PECS 3.0)</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>2/6/2013</td>
<td><blockquote>
<p>Technical Updates to various sections(for PECS 2.2)</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11/07/2012</td>
<td><blockquote>
<p>Updated Revision History Numbering, updated dates</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/16/2012</td>
<td><blockquote>
<p>Updated links, minor text updates</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10/15/2012</td>
<td><blockquote>
<p>Updated various section(Log4j template updated, help deployment section updated)</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>09/14/2012</td>
<td><blockquote>
<p>Added additional configure.exportfile.properties</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark>, <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>09/11/2012</td>
<td><blockquote>
<p>Updated various sections to deploy PECS Help Build file</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>09/10/2012</td>
<td><blockquote>
<p>Formatting updates</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>08/17/2012</td>
<td><blockquote>
<p>Modified the import data production steps to disable database constraints when loading data and re-enable them once complete.</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>07/20/2012</td>
<td><blockquote>
<p>Formatting updates; update TOC, Footers, etc.</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 55%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
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
<td>07/19/2012</td>
<td><blockquote>
<p>Added Appendix E – Rollback Process</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>07/10/2012</td>
<td><blockquote>
<p>Updated formatting and pagination; updated date references; minor spelling and grammatical edits; updated Revision History</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>07/09/2012</td>
<td><blockquote>
<p>Updated version references; added instructions regarding the data listener; added step to the post-migration procedure</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>07/05/2012</td>
<td><blockquote>
<p>Changed component deployment order</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>06/21/2012</td>
<td><blockquote>
<p>Minor updates (table captions, step numbering, etc.)</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>6/14/2012</td>
<td><blockquote>
<p>Updated various Sections for database changes for v2.2.</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>1/20/2012</td>
<td><blockquote>
<p>Updated pagination, edits, TOC, and release date (back to November 2011)</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>1/12/2012</td>
<td><blockquote>
<p>Updated database configuration section to reflect lessons learned during the initial load by testing services</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/08/2011</td>
<td><blockquote>
<p>Updated TOC and formatting</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>12/07/2011</td>
<td><blockquote>
<p>Updated database configuration section to include procedure for importing production data and database rollback procedures</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11/29/2011</td>
<td><blockquote>
<p>Updated document version number</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>11/28/2011</td>
<td><blockquote>
<p>Updated database configuration procedures to clarify installation and migration steps.</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11/10/2011</td>
<td><blockquote>
<p>Updated various Sections for configuration changes for v2.1.</p>
<p>Updated formatting, acronym table, footers, and TOC.</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark>, <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>9/27/2011</td>
<td><blockquote>
<p>Updated database configuration steps to reflect current Oracle environment and PECS installation requirements</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>07/19/2011</td>
<td><blockquote>
<p>Updated formatting, edits.</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>07/11/2011</td>
<td><blockquote>
<p>Updated various Sections. (removed section 5.2- JMS configuration and C4 as no longer needed)</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>05/29/2011</td>
<td><blockquote>
<p>Updated JMS Section</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/22/2011</td>
<td><blockquote>
<p>Edit formatting, apply template</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 55%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
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
<td>04/17/2011</td>
<td><blockquote>
<p>Updated for PECS 2.0, added Logical Deployment section</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/17/2011</td>
<td><blockquote>
<p>Added WebLogic JTA section</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>10/13/2010</td>
<td><blockquote>
<p>Adjustments to JMS configurations due to a database user change.</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/04/2010</td>
<td><blockquote>
<p>Added section on configuring JMS related to CCR 2902.</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>03/31/2010</td>
<td><blockquote>
<p>Added the creation of the exportfile.properties to support the sending of custom update files to an FTP server.</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td>02/10/2010</td>
<td><blockquote>
<p>Updated Various Sections as per AITC Input</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team- (Database Section Sreedhar, WebLogic Section <mark>REDACTED</mark>.)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/14/2009</td>
<td><blockquote>
<p>Updated Various Sections</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12/7/2009</td>
<td><blockquote>
<p>Updated Various sections</p>
</blockquote></td>
<td><blockquote>
<p>SwRI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9/30/2009</td>
<td><blockquote>
<p>Removed content for installation of WebLogic and KAAJEE.</p>
<p>Updated Appendix A to contain log4j configuration</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/26/2009</td>
<td><blockquote>
<p>Added Appendix B: Custom Update File Installation</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>08/12/2009</td>
<td><blockquote>
<p>Removed jdbc.properties reference, as this file will be accessed on the server.</p>
</blockquote>
<p>Removed Post-Installation section, as no longer needed.</p>
<p>Added section “4.5 Add CT_VERSION table to FDB schema”.</p></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td>01/06/2009</td>
<td><blockquote>
<p>Updated database datasource driver in WebLogic setup section.</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/02/2008</td>
<td><blockquote>
<p>Added log4j.properties reference.</p>
<p>Added KAAJEE jdbc.properties reference. Added kaajeeConfig.xml reference.</p>
<p>Added user_staged_config WebLogic KAAJEE library directory reference.</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11/24/2008</td>
<td><blockquote>
<p>Initial version</p>
</blockquote></td>
<td><blockquote>
<p>PECS Team</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ProPath Template used v1.6, June 2012

> *(This page included for two-sided copying.)*

1.  [Introduction 1](#introduction)
    1.  [Assumptions 1](#assumptions)
    2.  [Scope 2](#scope)
    3.  [Definitions, Acronyms and Abbreviations 3](#definitions-acronyms-and-abbreviations)
        1.  [Definitions 3](#definitions)
        2.  [Acronyms 3](#acronyms)
    4.  [Overview 4](#overview)
2.  [Installation Prerequisites 5](#installation-prerequisites)
3.  [Database Tier Installation 6](#database-tier-installation)
    1.  [Oracle Database 6](#oracle-database)
        1.  [Oracle Installation 6](#oracle-installation)
        2.  [Oracle Configuration 6](#oracle-configuration)
    2.  [CTSTAGING Installation Instructions 7](#ctstaging-installation-instructions)
        1.  [Create the Users 9](#create-the-users)
        2.  [Create Staging Tables and Database Objects 10](#create-staging-tables-and-database-objects)
        3.  [Modification of the FDB_DIF Database 10](#modification-of-the-fdb_dif-database)
        4.  [Create Public Synonyms 11](#create-public-synonyms)
        5.  [PECS Application Users 11](#pecs-application-users)
        6.  [PECS v3.0 Database Migration 12](#pecs-v3.0-database-migration)
        7.  [PECS v5.0 Database Migration Rollback 13](#pecs-v5.0-database-migration-rollback)
4.  [Users 16](#users)
5.  [WebLogic Application Server Configuration 18](#weblogic-application-server-configuration)
    1.  [Dependency Installation 18](#dependency-installation)
    2.  [Configure WebLogic Datasources 19](#configure-weblogic-datasources)
    3.  [WebLogic Server Startup Configuration 20](#weblogic-server-startup-configuration)
    4.  [Configure WebLogic JTA 23](#configure-weblogic-jta)
    5.  [Configure exportfile.properties 24](#configure-exportfile.properties)
    6.  [Application Deployment 24](#application-deployment)
        1.  [PECS Application Deployment 24](#pecs-application-deployment)
        2.  [PECS Help Application Deployment 25](#pecs-help-application-deployment)
    7.  [Configure log4j.properties 25](#configure-log4j.properties)
6.  [Post-Installation Notes 26](#post-installation-notes)

> [Appendix A: log4j Properties ................................................. A-1](#appendix-a-log4j-properties)

> [Appendix B: Custom Update File Installation ...................... B-1](#appendix-b-custom-update-file-installation)

> [B.2 Scope ............................................................................................................ B-1](#scope-1) [B.3 Update Process Prerequisites .................................................................... B-1](#update-process-prerequisites)

[B.4.1 Execute FDB Update Tool ........................................................................B-2](#b.4.1-execute-fdb-update-tool)

[B.5.1 Verify CT_VERSION Table.......................................................................B-4](#verify-ct_version-table)

[B.5.2 Execute FDB Update Tool ........................................................................B-4](#execute-fdb-update-tool)

> [B.6 Recover FDB-DIF Custom Tables from Load Failure ................................ B-4](#recover-fdb-dif-custom-tables-from-load-failure) [B.6.1 Execute Recovery ....................................................................................B-4](#execute-recovery) [B.6.2 Verify Data Recovery................................................................................B-4](#verify-data-recovery) [B.6.3 Generate Full PECS Update File ..............................................................B-4](#generate-full-pecs-update-file)

> [C.2 Administrator User Role .............................................................................. C-1](#administrator-user-role)

> [C.3 Resource Adapter ........................................................................................ C-1](#resource-adapter)

[D.1 Logical Deployment Design – PECS ........................................................ D-01](#d.1-logical-deployment-design-pecs)

[E.1 Database Installation Process Flow – PECS...............................................E-1](#database-installation-process-flow-pecs)

> [Appendix G: PECS Upgrade Installation Instructions ......... G-1](#appendix-g-pecs-upgrade-installation-instructions)

### List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table 1: Definitions 3](#_bookmark5)
> [Table 2: Acronyms 3](#_bookmark7)
> [Table 3 – Database Users and Roles 11](#_bookmark21)
> [Table 4. List of PECS Schema Creation SQL Scripts (TBD) 12](#_bookmark22)
> [Table 5: List of PECS 5.0 Driver SQL Script 13](#_bookmark24)
> [Table 6: List of PECS 5.0 SQL Scripts 13](#_bookmark25)

### List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Figure 1: PECS 5.0 Database Installation Process 7](#_bookmark15)
> [Figure 2: Summary of Servers 20](#_bookmark32)
> [Figure 3: Settings for Deployment Server 21](#_bookmark33)
> [Figure 4: Server Start Tab 22](#_bookmark34)
> [Figure 5: WebLogic Console Screen – Completion 23](#_bookmark36)
> [Figure 6: Update Settings – Configure Connection .................................................................................. B-2](#_bookmark51)
> [Figure 7: Add Paths to FirstDatabank Data Updater ................................................................................ B-3](#_bookmark52) [Figure 8: PECS Deployment..................................................................................................................... D-2](#_bookmark67)
> *(This page included for two-sided copying.)*

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This appendix describes the process to load the FDB-DIF and PECS update files into an existing FDB- DIF Oracle database using the FDB Updater Tool. The FDB-DIF update file is received on a schedule from FDB every two weeks and must be loaded in sequence. The PECS update file can be generated from the PECS application interface at any time by a user in the Release Manager role, and loaded with the FDB Update Tool.

## Update Process Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The FDB Updater Tool is installed on the machine performing the update process.
- The FDB and PECS update files are available and/or have been generated.
- The FDB-DIF update file must be loaded in sequence. The version number of the new file must be the next in sequence.
- The user performing Oracle operations must have sufficient rights to delete data, drop, and create tables.
- The PECS preparation and recovery SQL scripts are available.
- An Oracle tool such as SQLPlus, must be installed on the machine executing the FDB Updater tool.

## Apply FDB-DIF Update File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists the steps necessary to apply the FDB-DIF Update file.

### B.4.1 Execute FDB Update Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Here are the steps required to execute the FDB update tool (four steps):

#### Obtain the FDB-DIF Update File

> Either download the update file from the FTP directory, or insert the update CD into drive.

#### Start FDB Update Tool GUI

> Navigate to where the FDB Update Tool has been installed, and click on the GUI.bat file.

#### Configure Connection

> ![](prec-5-1114-install-guide/015.png)Select the View -\> Setting menu option on the GUI and input the connection data relevant to your location and click the “Save” button. A sample screen is shown.

> <span id="_bookmark51" class="anchor"></span>Figure 6: Update Settings - Configure Connection

#### Provide File Paths

> ![](prec-5-1114-install-guide/016.png)Enter the path to the update and log files relevant to your location. Select whether the update is incremental or complete. Click the “Start” button. A sample screen is shown:

> <span id="_bookmark52" class="anchor"></span>Figure 7: Add Paths to FirstDatabank Data Updater

## Apply Custom Tables Update File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the two major steps necessary to apply the Custom Tables Update File.

### Verify CT_VERSION Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CT_VERSION table is an additional table added to the FDB schema (as recommended by FDB) to track the PECS update file version. If the table does not exist, execute the following DDL:

> CREATE TABLE FDB.CT_VERSION (

> VERSIONKEY NUMBER(6) NOT NULL, DBVERSION VARCHAR2(5) NULL, BUILDVERSION VARCHAR2(5) NULL, FREQUENCY VARCHAR2(1) NULL, ISSUEDATE VARCHAR2(8) NULL, VERSIONCOMMENT VARCHAR2(80) NULL,

> DBTYPE VARCHAR2(10) NULL

> )

> CREATE UNIQUE INDEX PKCTVERSION ON FDB.CT_VERSION(VERSIONKEY)

### Execute FDB Update Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The steps to apply the Custom Tables Update file are the same steps as outlined in [Apply FDB DIF](#apply-fdb-dif-update-file) [Update File.](#apply-fdb-dif-update-file) Instead of entering the path to the FDB-DIF update file, enter the path to the Custom Tables Update file, relevant to your location. Select whether the update is incremental or complete. Click the “Start” button.

## Recover FDB-DIF Custom Tables from Load Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The recover process may be necessary if a failure has occurred during the application of the PECS Update file (see [Apply Custom Tables Update File](#apply-custom-tables-update-file) step). The recovery process involves the execution of a SQL script, and verification that the data has been recovered.

### Execute Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The recovery entails the deletion of any data that may have been loaded to the FDB_CUSTOM\_\* tables during the execution of the update process.

### Verify Data Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Verify that the data in the FDB_CUSTOM\_\* tables has been deleted.

### Generate Full PECS Update File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After logging into the PECS application, a user in the Release Manager role will navigate to the “Custom Update” tab, and click the “Download New Full Update” button. This will generate a PECS update file with all currently approved order check customizations.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After a user is authenticated, KAAJEE retrieves his or her security keys from VistA and maps them to WebLogic security roles. The PECS application is secured so that only users running with the PECS security roles may access the PECS application.

> PECS relies on the following four security keys, which must be added to VistA:

- PSS_CUSTOM_TABLES_ADMIN
- PSS_CUSTOM_TABLES_APPROVER
- PSS_CUSTOM_TABLES_REL_MAN
- PSS_CUSTOM_TABLES_REQUESTOR

> PRE will rollout VISTA Patch, PSS\*1\*147 which exports the Security Keys, and those Security Keys are technically in the PSS namespace. These security keys have to be associated with the user accounts that will be set up on a VistA M server. The process for setting up the user accounts and the security keys is a part of the VistALink API setup mentioned in the VistALink Installation Manual available with the API software at: [*<u>http://vista.med.<span class="mark">REDACTED</span>/kernel/kaajee/download_9-10.asp#vista_m_server</u>*](http://vista.med.va.gov/kernel/kaajee/download_9-10.asp#vista_m_server)

> *Note: Due to policy constraints, active links cannot be included in this document. Please copy and paste the URLs into your browser.*

## Administrator User Role

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PECS is configured to use the KAAJEE administrator user role by default. This requires the creation of a KAAJEE administrator account in WebLogic if one does not exist.

## Resource Adapter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use Resource Adapter with the supporting jars included in it and do not deploy jars as library files. The deployment order for the Resource Adapter must be at a lower number than the deployment order for PECS. This is to make sure the Resource Adapter is loaded and that the classes in the Resource Adapter are available when PECS is started. It is recommended to set the deployment order for the Resource Adapter to 95 or 99. This is because the default deployment order is 100.

> *(This page included for two-sided copying.)*

## Database Installation Process Flow – PECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](prec-5-1114-install-guide/018.png)

> Figure 9: Database Installation Process

> *(This page included for two-sided copying.)*
