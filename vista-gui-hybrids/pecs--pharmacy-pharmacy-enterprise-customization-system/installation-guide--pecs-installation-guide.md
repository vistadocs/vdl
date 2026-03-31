---
consolidated_title: "pecs installation guide"
app_code: PECS
doc_type: IG
master_source: "PECS Installation Guide (PREC*6.2*1)"
master_pub_date: June 2021
consolidated_from: 2 versions
prior_versions:
  - "PECS Version 6.2 Installation Guide (Updated PREC* 6.2*3)"
---

# Pharmacy Reengineering

# Pharmacy Enterprise Customization System
(PECS) v6.2

# Installation Guide

<!-- image -->


June 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date       |   Version | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     | Author                                                            |
|------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| June 2021  |      3.4  | PREC*6.2*1:  - Updated PECS 6.1 version references to 6.2 - Updated **Figure 1** and **Figure 10** - Updated the entire section of **5.7 Configure log4j2.xml** - Updated the entire section of **Properties of log4j2** - Updated formatting throughout the document - Updated Title page, Revision History, Table of Contents, and Footers - See the non-redacted prec\_6\_2\_p1\_ig on the SOFTWARE library for viewing REDACTED information | Liberty ITS                                                       |
| July 2017  |      3.31 | Made updates for PECS v6.1 which addresses 2FA Compliance and IAM SSOi intergration for PIV authentication                                                                                                                                                                                                                                                                                                                                      | REDACTED  Enterprise Application Maintenance                      |
| May 2016   |      3.3  | Made updates to PECS 6.0.01 508 conformance edit                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED REDACTED                                                 |
| 06/24/2013 |      3.26 | Minor text and graphics updates;                                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED                                                          |
| 12/19/2013 |      3.25 | Updated the Database Installation Instructions                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED                                                          |
| 11/22/2013 |      3.24 | Updated Database Installation diagram, removed FDB_DIF schema from rollback process and clarified instruction.                                                                                                                                                                                                                                                                                                                                  | REDACTED                                                          |
| 11/21/2013 |      3.22 | Updated Database Installation and Migration instructions                                                                                                                                                                                                                                                                                                                                                                                        | REDACTED                                                          |
| 11/19/2013 |      3.21 | Added Appendix G                                                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED                                                          |
| 11/15/2013 |      3.2  | Added parameters in exporfile.properties for quartz scheduler, and updated log4j.xml                                                                                                                                                                                                                                                                                                                                                            | REDACTED                                                          |
| 05/20/2013 |      3.19 | Tech Writer edits (footers)                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED                                                          |
| 04/25/2013 |      3.18 | Minor Updates to the Load Production Section                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED                                                          |
| 02/06/2013 |      3.17 | More Tech Writer Edits                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED                                                          |
| 02/06/2013 |      3.16 | Technical Writer Edits                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED                                                          |
| 02/06/2013 |      3.15 | Technical Updates to various sections(for PECS 3.0)                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                                                          |
| 2/6/2013   |      3.14 | Technical Updates to various sections(for PECS 2.2)                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                                                          |
| 11/07/2012 |      3.13 | Updated Revision History Numbering, updated dates                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED                                                          |
| 10/16/2012 |      3.12 | Updated links, minor text updates                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED                                                          |
| 10/15/2012 |      3.11 | Updated various section(Log4j template updated, help deployment section updated)                                                                                                                                                                                                                                                                                                                                                                | REDACTED                                                          |
| 09/14/2012 |      3.1  | Added additional configure.exportfile.properties                                                                                                                                                                                                                                                                                                                                                                                                | REDACTED, REDACTED                                                |
| 09/11/2012 |      3.9  | Updated various sections to deploy PECS Help Build file                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED                                                          |
| 09/10/2012 |      3.8  | Formatting updates                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED                                                          |
| 08/17/2012 |      3.7  | Modified the import data production steps to disable database constraints when loading data and re-enable them once complete.                                                                                                                                                                                                                                                                                                                   | REDACTED                                                          |
| 07/20/2012 |      3.6  | Formatting updates; update TOC, Footers, etc.                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED                                                          |
| 07/19/2012 |      3.5  | Added Appendix E – Rollback Process                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                                                          |
| 07/10/2012 |      3.4  | Updated formatting and pagination; updated date references; minor spelling and grammatical edits; updated Revision History                                                                                                                                                                                                                                                                                                                      | REDACTED                                                          |
| 07/09/2012 |      3.3  | Updated version references; added instructions regarding the data listener; added step to the post-migration procedure                                                                                                                                                                                                                                                                                                                          | REDACTED                                                          |
| 07/05/2012 |      3.2  | Changed component deployment order                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED                                                          |
| 06/21/2012 |      3.1  | Minor updates (table captions, step numbering, etc.)                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED                                                          |
| 6/14/2012  |      3    | Updated various Sections for database changes for v2.2.                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED                                                          |
| 1/20/2012  |      2.6  | Updated pagination, edits, TOC, and release date (back to November 2011)                                                                                                                                                                                                                                                                                                                                                                        | REDACTED                                                          |
| 1/12/2012  |      2.5  | Updated database configuration section to reflect lessons learned during the initial load by testing services                                                                                                                                                                                                                                                                                                                                   | REDACTED                                                          |
| 12/08/2011 |      2.4  | Updated TOC and formatting                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED                                                          |
| 12/07/2011 |      2.3  | Updated database configuration section to include procedure for importing production data and database rollback procedures                                                                                                                                                                                                                                                                                                                      | REDACTED                                                          |
| 11/29/2011 |      2.2  | Updated document version number                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                                                          |
| 11/28/2011 |      2.1  | Updated database configuration procedures to clarify installation and migration steps.                                                                                                                                                                                                                                                                                                                                                          | REDACTED                                                          |
| 11/10/2011 |      2    | Updated various Sections for configuration changes for v2.1.  Updated formatting, acronym table, footers, and TOC.                                                                                                                                                                                                                                                                                                                              | REDACTED, REDACTED                                                |
| 9/27/2011  |      1.18 | Updated database configuration steps to reflect current Oracle environment and PECS installation requirements                                                                                                                                                                                                                                                                                                                                   | REDACTED                                                          |
| 07/19/2011 |      1.17 | Updated formatting, edits.                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED                                                          |
| 07/11/2011 |      1.16 | Updated various Sections. (removed section 5.2- JMS configuration and C4 as no longer needed)                                                                                                                                                                                                                                                                                                                                                   | REDACTED                                                          |
| 05/29/2011 |      1.15 | Updated JMS Section                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED                                                          |
| 04/22/2011 |      1.14 | Edit formatting, apply template                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED                                                          |
| 04/17/2011 |      1.13 | Updated for PECS 2.0, added Logical Deployment section                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED                                                          |
| 04/17/2011 |      1.12 | Added WebLogic JTA section                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED                                                          |
| 10/13/2010 |      1.11 | Adjustments to JMS configurations due to a database user change.                                                                                                                                                                                                                                                                                                                                                                                | PECS Team                                                         |
| 08/04/2010 |      1.1  | Added section on configuring JMS related to CCR 2902.                                                                                                                                                                                                                                                                                                                                                                                           | PECS Team                                                         |
| 03/31/2010 |      1.9  | Added the creation of the exportfile.properties to support the sending of custom update files to an FTP server.                                                                                                                                                                                                                                                                                                                                 | PECS Team                                                         |
| 02/10/2010 |      1.8  | Updated Various Sections as per AITC Input                                                                                                                                                                                                                                                                                                                                                                                                      | PECS Team-(Database Section REDACTED, WebLogic Section REDACTED.) |
| 12/14/2009 |      1.7  | Updated Various Sections                                                                                                                                                                                                                                                                                                                                                                                                                        | PECS Team                                                         |
| 12/7/2009  |      1.6  | Updated Various sections                                                                                                                                                                                                                                                                                                                                                                                                                        | SwRI                                                              |
| 9/30/2009  |      1.5  | Removed content for installation of WebLogic and KAAJEE.  Updated Appendix A to contain log4j configuration                                                                                                                                                                                                                                                                                                                                     | PECS Team                                                         |
| 08/26/2009 |      1.4  | Added Appendix B: Custom Update File Installation                                                                                                                                                                                                                                                                                                                                                                                               | PECS Team                                                         |
| 08/12/2009 |      1.3  | Removed jdbc.properties reference, as this file will be accessed on the server.  Removed Post-Installation section, as no longer needed.  Added section “4.5 Add CT\_VERSION table to FDB schema”.                                                                                                                                                                                                                                              | PECS Team                                                         |
| 01/06/2009 |      1.2  | Updated database datasource driver in WebLogic setup section.                                                                                                                                                                                                                                                                                                                                                                                   | PECS Team                                                         |
| 12/02/2008 |      1.1  | Added log4j.properties reference.  Added KAAJEE jdbc.properties reference.  Added kaajeeConfig.xml reference.  Added user\_staged\_config WebLogic KAAJEE library directory reference.                                                                                                                                                                                                                                                          | PECS Team                                                         |
| 11/24/2008 |      1    | Initial version                                                                                                                                                                                                                                                                                                                                                                                                                                 | PECS Team                                                         |

ProPath Template used v1.6, June 2012

Table of Contents

1.	Introduction	1

1.1.	Assumptions	1

1.2.	Scope	1

1.3.	Definitions, Acronyms, and Abbreviations	2

1.4.	Overview	3

2.	Installation Prerequisites	3

3.	Database Tier Installation	4

3.1.	Oracle Database	4

3.1.1.	Oracle Installation	4

3.1.2.	Oracle Configuration	4

3.2.	CTSTAGING Installation Instructions	5

3.2.1.	Create the Users	6

3.2.2.	Create Staging Tables and Database Objects	7

3.2.3.	Modification of the FDB\_DIF Database	7

3.2.4.	Create Public Synonyms	8

3.2.5.	PECS Application Users	8

3.2.6.	PECS v6.2 Database Migration	9

3.2.7.	PECS v6.2 Database Migration Rollback	10

3.2.8.	PECS v6.2 Database Migration	11

4.	Users	13

5.	WebLogic Application Server Configuration	13

5.1.	Dependency Installation	13

5.2.	Configure WebLogic Data Sources	14

5.3.	WebLogic Server Startup Configuration	14

5.4.	Configure WebLogic JTA	17

5.5.	Configure exportfile.properties	17

5.6.	Application Deployment	18

5.6.1.	PECS Application Deployment	18

5.6.2.	PECS Help Application Deployment	19

5.7.	Configure log4j2.xml	19

6.	Post-Installation Notes	21

A.	Properties of log4j2	22

B.	Custom Update File Installation	28

B.1.	Introduction	28

B.2.	Scope	28

B.3.	Update Process Prerequisites	28

B.4.	Apply FDB-DIF Update File	28

B.5.	Apply Custom Tables Update File	30

B.6.	Recover FDB-DIF Custom Tables from Load Failure	31

C.	PECS Logical Deployment Architecture	32

C.1.	Logical Deployment Design – PECS	32

C.2.	SiteMinder Web Agent on Apache Web Server – PECS	33

D.	PECS Database Installation Process	34

D.1.	Database Installation Process Flow – PECS	34

E.	Rollback Process	35

F.	PECS Upgrade Installation Instructions	35

## Introduction

This document describes the process used to install the VA PECS application on an instance of a WebLogic server. The PECS software is a Web-based application, packaged as a Java 2 Platform Enterprise Edition (J2EE) standardized Enterprise Application Archive (EAR) file, which is then deployed on the WebLogic server using the server’s standard deployment process. The installation described in this document also outlines the steps necessary to install and configure the application’s database. This includes the installation of the database schema on an Oracle server and loading data into configuration tables. The document outlines the configuration of two data sources, and the deployment of the EAR file on the WebLogic server. The installation of the PECS application assumes that the servers necessary to execute the software are configured and running as per any applicable VA standards.

In order to understand the installation and verification process, the installer should be familiar with the WebLogic console administration and Oracle 11g Database configuration.

### Assumptions

For successful deployment of the Pharmacy Reengineering (PRE) PECS software at a site, the following assumptions must be met:

Red Hat Enterprise Linux 5 operating system is properly installed.

The WebLogic Server 12.1.3 is configured and running.

Access to the WebLogic console is by means of a valid administrative user name and password.

Oracle 11g Database Server is configured and running.

Java JDK version used is 1.8.

First Databank (FDB) Drug Information Framework (DIF) v3.3 database is installed. Installation instructions are provided in FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project’s Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.

The installation instructions are followed in the order that the sections are presented within this Installation Guide.

### Scope

Installation steps in scope include:

Installation of the PECS database staging schema on an existing Oracle server, and a data load into configuration tables.

Configuration of database data sources on an existing WebLogic application server.

Deployment of the PECS application EAR file on a configured WebLogic application server.

Processes out of scope include:

Installation and configuration of server environments including the operating system, database server, application server, and/or any other network component as may be required to host the PECS application on the VA network.

SiteMinder Web Agent installation and configuration, Identity and Access Management (IAM), and Single Sign On internal (SSOi) environment setup.

FDB-DIF database installation/migration or update process.

Process to check out the PECS codebase from the ClearCase repository and/or the build process.

Installation details of the Java Runtime environment.

Initial load of Pharmacy Benefits Management (PBM) customized order checks.

### Definitions, Acronyms, and Abbreviations

Here is a list of terms and acronyms and their definitions.

Table 1: Definitions

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

### Overview

The steps necessary to install and configure the components required by the PECS application are outlined in the following pages. The order that the components appear in the outlined steps is the suggested installation order. Installation Prerequisites should be installed or verified on the build environment first followed by the installation of the database schema, application server configuration, and the deployment of the PECS application.

## Installation Prerequisites

Installation and configuration of server environments including the operating system, database server, application server, and/or any other network component as may be required to host the PECS application on the VA network.

SiteMinder Web Agent must be installed on the Apache web server in the PECS environment and SSL must be enabled.

SiteMinder Web Agent on the Apache server must be configured to communicate with the IAM Policy server. IAM and SSOi services must be up and available for PECS to work.

All Active Directory users have read-only or Requestor access to PECS. The users must have their VAUID, first and last names set in Active Directory and in the IAM Provisioning Server.

The target production FDB-DIF database is available.

## Database Tier Installation

This section describes the operating system and software for the PRE PECS V.6.2 Database Tier installation and configuration. Initially install and configure the operating system and software according to the manufacturer’s specifications.

### Oracle Database

The CT staging schema or PECS Database is designed to be operating system independent. The only constraint is that Oracle 11g Database Enterprise Edition Release 11.2.0.4 – Production must be properly installed and configured. The following sections describe the installation, features, user creation, and configuration for the Oracle database.

The PECS staging database user should be configured as “CTSTAGING” (CTSTAGING schema) and the FDB-DIF database user should be configured as “FDB\_DIF” (FDB\_DIF schema).

#### Oracle Installation

Proper installation of the Oracle Relational Database Management System (RDBMS) is one in which the Oracle Universal Installer was used to perform an error-free installation and a general-purpose instance was created. A properly configured Oracle RDBMS is one in which the associated Oracle application development and configuration tools, namely Structured Query Language (SQL)*Plus and Oracle Enterprise Manager, can be used to connect to the instance through a Transparent Network Substrate alias.

#### Oracle Configuration

The CT staging schema or PECS Database is the primary data repository for the PECS application. The database should be installed and configured appropriately for the PECS operating environment.

Two schemas must be created for the PECS Environment within the same database instance: FDB\_DIF and CTSTAGING. Prior to creation of the schemas, logical and physical environment structures must be set up for storage of the schemas database objects: tablespaces and data files. For the PECS database configuration, data and index storage are separated for each schema. Separating indexes and table data is considered an Oracle best practice and provides improved run-time performance, reporting/monitoring, and manageability.

**Note:** For PECS v6.2, since there is no FDB change, this would involve installation of PECS v6.2 component only unlike in PECS v6.1.

*[Not Applicable for PECS 6.2: There are two components to PECS 6.2 National database installation process. The first component involves the installation of the FDB\_DIF v3.3. The second component installation of the PECS 6.2 schema. The first component, installation of FDB\_DIF v3.3, must be completed prior to moving forward with the PECS 6.2 installation component. Installation instructions are provided in FDB-DIF Installation/Migration guide. Contact the PRE Configuration Manager who should be identified on the project’s Technical Services Project Repository (TSPR) site for a copy of the guide and installations/migration scripts.]*

### CTSTAGING Installation Instructions

This section describes the database scripts necessary for the installation of the PECS CTSTAGING database, and the order in which they should be executed. It is highly recommended that the PECS staging database user be configured as “CTSTAGING” and the FDB-DIF database user be configured as “FDB\_DIF” as that is the usernames that are used throughout the remainder of the PECS installation documentation. **Executing steps 3.2.1 – 3.2.5 in this section will result in the creation of a PECS 6.2 database. Executing step 3.2.6 will migrate an existing PECS v6.1 database to PECS v6.2 compatibility.** If migrating from an existing PECS 6.1 schema with production data, then skip to 3.2.6 to migrate to PECS 6.2 compatibility. The complete PECS Database Installation Process is graphically depicted below and in Appendix E – The PECS Database Installation Process.

Figure 1: PECS 6.2 Database Installation Process

<!-- image -->

To migrate an existing PECS 6.1 database schema, skip to Section 3.2.6 – PECS 6.2 Database Migration.

Prior to executing the following sections, the Oracle 11g database needs to be installed and a Database Administrator login generated with sys\_dba privileges. The DBA login is necessary to run the first database script to create the tablespaces and user accounts for the remainder of the installation.

To get Install Scripts, please contact the PRE Configuration Manager, who should be identified on the project’s TSPR site.

#### Create the Users

Prior to creation of the schemas, logical and physical environment structures must be setup for storage of the schemas database objects: tablespaces and data files. For the PECS Database configuration data and index storage are separated for each schema. For the CTSTAGING schema two tablespaces must be created:

CTSTAGING\_DATA

CTSTAGING\_INDEX

LOB\_DATA

LOB\_INDEX

In addition, user profiles are used to standardize resource limits for PECS schemas. There are two user profiles that must be created:

SERVICE\_ACCOUNT

USER\_ACCOUNT

Before the user profiles can be created the script **utlpwdmg.sql** has to be executed. The script is in the RDBMS\ADMIN directory within the installation home. Consult the Oracle installation manual for the full directory path for the proposed environment.

To create the users in the database for the PECS application, the DBA will need to execute the **pecs5\_creation\_pkg1.sql** script as **SYSTEM** . This script will execute other scripts that will create the tablespaces, user profiles and create the CT Staging User:

PECS5\_Create\_CTSTAGING\_Tablespaces.sql

pecs5\_create\_user\_profiles\_ddl.sql

pecs5\_create\_user\_modified.sql

Modifications should be made tailored for the current installation environment prior to running the scripts. The following steps should be followed:

Open a text editor and open the PECS5\_Create\_CTSTAGING\_Tablespaces.sql script. **Replace %DATAFILE\_LOCATION% with the data file directory** the directory entered should already exist on the database server.

**Note:** If creating a development environment, then use PECS5\_Create\_CTSTAGING\_Tablespaces\_Dev.sql instead.

Login to the SQL client using a database account that has sys\_dba privileges.

Execute the “pecs5\_creation\_pkg1.sql” script.

Open the “pecs5\_creation\_pkg1.log” file and search the log file for any errors.

This process creates the temporary file dif5ctstaging.sql. Open this file and scroll to the bottom and verify the following entry at the bottom of the file ‘GRANT SELECT ON FDB\_DIF.FDB\_VERSION TO CTSTAGING’. This will ensure that all necessary privileges were granted to the FDB tables that the CTSTAGING user needs to access.

#### Create Staging Tables and Database Objects

To create the CTSTAGING database for the PECS application, the administrator will need to execute the **pecs5\_creation\_pkg2.sql** script. This script will execute 39 other scripts that create the CTSTAGING tables and populate those tables with some initial data values. The following steps should be followed:

1. Login to the SQL client using the CTSTAGING user account.

Execute the “pecs5\_creation\_pkg2.sql” script.

Open the pecs5\_creation\_pkg2.log file and search the log file for any errors.

#### Modification of the FDB\_DIF Database

To modify the FDB-DIF data repository to work with the PECS application, the administrator will need to execute the **fdb\_modification\_pkg3.sql** script. This script will create a new table in the FDB-DIF data repository and modify one of the existing tables to change the constraints add an index.

1. Login to the SQL client using the FDB\_DIF user account.

Execute the “fdb\_modification\_pkg3.sql” script.

Open the fdb\_modification\_pkg3.log file and search the log file for any errors.

#### Create Public Synonyms

The PECS application access spans both FDB\_DIF and CTSTAGING schema objects. Public synonyms are utilized to provide seamless application access across PECS application components. To create the public synonyms, the administrator will need to execute the **PECS5\_Create\_Public\_Synonyms.sql** script. This script executes two scripts: **PECS5\_Create\_FDB\_Synonyms.sql** , **PECS5\_Create\_CTSTAGING\_Synonyms.sql** . The following steps should be followed:

1. Login to the SQL client using the SYSTEM account.

Execute the “PECS5\_Create\_Public\_Synonyms.sql” script.

Open the PECS5\_Create\_Public\_Synonyms\_create\_ public\_synonyms.log file and search the log file for any errors.

#### PECS Application Users

The PECS database schemas have been devised to provide separation of ownership and CRUD data access levels with user/schemas and access roles assigned. Schemas/Roles that are required by the application are depicted in the cross-reference table listed below:

Table 3: FDB-DIF Database Users and Roles

| User                | Schema   | Schema Owner   | Assigned Role            |
|---------------------|----------|----------------|--------------------------|
| FDB_DIF_APP_USER    | FDB_DIF  | Read Only user | FDB_DIF_READ_ONLY_ROLE   |
| FDB_DIF_UPDATE_USER | FDB_DIF  | CRUD user      | FDB_DIF_UPDATE_USER_ROLE |

Table 4: CTSTAGING Database Users and Roles

| User                  | Schema    | Schema Owner   | Assigned Role                                             |
|-----------------------|-----------|----------------|-----------------------------------------------------------|
| CTSTAGING_READ_ONLY   | CTSTAGING | Read Only user | CTSTAGING_READ_ONLY_ROLE                                  |
| CTSTAGING_UPDATE_USER | CTSTAGING | CRUD user      | CTSTAGING\_UPDATE\_USER\_ROLE  FDB\_DIF\_READ\_ONLY\_ROLE |

Table 5: PECSJMS Database Users and Roles

| User             | Schema   | Schema Owner   | Assigned Role         |
|------------------|----------|----------------|-----------------------|
| PECSJMS_APP_USER | PECSJMS  | CRUD user      | PECSJMS_APP_USER_ROLE |

Both FDB\_DIF and CTSTAGING schema owners have been created prior to this step, however, additional users are required by the application. To create the PECS application user roles and users, the administrator will need to execute the **PECS5\_Create\_Application\_Roles\_Users.sql** script. This script will execute scripts that create the required PECS user roles and application users. Additionally, the script will create the PECSJMS schema objects that are required by the PECS application by executing **pecs\_create\_jms\_process.sql** script.

Prior to running the driver script, **PECS5\_Create\_Application\_Roles\_Users.sql,** modifications should be made to **CreateTablespacePECSJMS.sql** to tailor for the current installation environment.

The following steps should be followed:

1. Open a text editor and open the CreateTablespacePECSJMS.sql script. Replace %DATAFILE\_LOCATION% with the data file directory for the current installation environment. The directory entered should already exist on the database server.

Login to the SQL client using the SYSTEM account.

Execute the “ **PECS5\_Create\_Application\_Roles\_Users** \_create\_application\_roles\_users.sql” script.

Open the “PECS5\_Create\_Application\_Roles\_User.log” file and search the log file for any errors.

A complete listing of the PECS Schema Creation SQL Scripts invoked from the driver scripts are listed below.

Table 6: List of PECS Schema Creation SQL Scripts

| Script Description                                                                 | File Name                 |
|------------------------------------------------------------------------------------|---------------------------|
| A Master script to create the tablespace and user package script.                  | pecs5_creation_pkg1.sql   |
| Master script to create the CT staging tables and database objects package script. | pecs5_creation_pkg2.sql   |
| Master script to modify the FDB schema package script.                             | fdb_modification_pkg3.sql |

#### PECS v6.2 Database Migration

Prior to migrating PECS v6.1 database schema to PECS v6.2 compatibility, a backup of the database should be performed either using RMAN or Oracle 11g DataPump export utility. Securing a backup of the database is integral to the database rollback procedures in the event that the upgrade/migration needs to revert back to the prior version. Oracle DataPump utilities provide more granularity to backup specific schemas. PECS v6.1 consists of two database schemas: CTSTAGING, FDB\_DIF. To back up the PECS v56.1database using Oracle DataPump utility, issue the following command logged in as a USER with DBA privileges:

- **expdp DUMPFILE** =&lt;dumpfilename.dmp&gt; **SCHEMAS** =CTSTAGING,FDB\_DIF **CONTENT** =ALL **LOGFILE** =&lt;logfilename.log&gt;

*When prompted, enter the SYSTEM user id and password to complete the export and note the dump and log files for future use.*

Prior to performing the steps needed to migrate a PECS v6.1 database to PECS v6.2 compatibility, the Oracle listener for the PECS database instance should be brought down to ensure consistency and limit access during the conversion efforts. As an Oracle Administrator, the following command can be issued from the LINUX command prompt to stop the listener for the current instance: **lsnrctl stop** .

To migrate PECS v6.1 database schema to PECS v6.2 compatibility, the database administrator will need to execute the following database scripts as the USER specified below. Each of these scripts acts as a driver script to initiate and log migration activities. At the completion of each of the steps. Check the log file for any errors or anomalies in processing the required transactions.

Table 7: List of PECS 6.2 Driver SQL Script

| Script Description           | File Name           | User      | Log File            |
|------------------------------|---------------------|-----------|---------------------|
| PECS Migration Driver script | PECS6_migration.sql | CTSTAGING | PECS6_migration.log |

Step by Step procedure to accomplish the migration is as follows:

1. Login to the SQL client using the CTSTAGING user account.

Execute the “PECS6\_migration.sql” script.

Open the “PECS6\_migration.log” file and search the log file for any errors.

After all the migration steps have been completed without error, the Oracle listener for the PECS database instance should be restarted. As an Oracle Administrator, the following command can be issued from the LINUX command prompt to start the listener for the current instance: **lsnrctl start** .

A complete listing of the scripts invoked from the driver scripts are listed below.

Table 8: List of PECS 6.2 SQL Scripts

| PECS 6.2 Driver Scripts   | Description                                               | Purpose                           |
|---------------------------|-----------------------------------------------------------|-----------------------------------|
| PECS6_migration.sql       | Driver Script to migrate from PECS 6.1 to PECS 6.2 schema | Database Migration Driver Scripts |

#### PECS v6.2 Database Migration Rollback

Prior to migrating PECS v6.1 database schema to PECS v6.2 compatibility, a backup of the database was performed to ensure rollback capability. This section addresses the steps needed to rollback to PECS v6.1 using the secured backup.

To restore the PECS v6.1 schema from the backup taken prior to the migration, follow the procedures outlined in the Data Import Guide for platform specific instructions (Unix, Windows).

Procedures for restoring/loading production data include the following steps regardless of platform:

Prepare database for restoring production data

- Drop existing schema objects (tables, sequences) for each schema using the Build\_Script\_to\_Drop\_CTSTAGING\_objects.sql to drop all the database objects in the CTSTAGING schema. Execute the Build\_Script\_to\_Drop\_CTSTAGING\_objects.sql script using the SYSTEM id and password.

Import the CTSTAGING schema by issuing the following commands logged in as a USER with DBA privileges preferably SYSTEM:

- **impdp DUMPFILE** =&lt;dumpfilename.dmp&gt; **SCHEMAS** =CTSTAGING **LOGFILE** =&lt;logfilename.log&gt; **CONTENT** =ALL **TABLE\_EXISTS\_ACTION** =REPLACE

*When prompted, enter the SYSTEM user id and password to complete the import. Review log files for each import to verify the successful completion of the rollback.*

**Note:** The migration and rollback process for the PECS database does not impact the FDB\_DIF schema.

#### PECS v6.2 Database Migration

PECS v6.2 is integrated with IAM SSOi through the SiteMinder Web Agent for PIV authentication. PECS no longer uses KAAJEE and VistA for user authentication. The user name and VAUID from Active Directory are stored in the PECS database and the user roles are managed within the PECS application.

#### PECS Database Backup

Prior to migrating PECS v6.1 database schema to PECS v6.2 compatibility, a backup of the database should be performed either using RMAN or Oracle 11g DataPump export utility. Securing a backup of the database is integral to the database rollback procedures in the event that the upgrade/migration needs to revert back to the prior version. Oracle DataPump utilities provide more granularity to backup specific schemas. PECS v6.1 consists of two database schemas: CTSTAGING, FDB\_DIF. To back up the PECS v6.1 database using Oracle DataPump utility, issue the following command logged in as a USER with DBA privileges:

**expdp DUMPFILE** =&lt;dumpfilename.dmp&gt; **SCHEMAS** =CTSTAGING,FDB\_DIF **CONTENT** =ALL **LOGFILE** =&lt;logfilename.log&gt;

*When prompted, enter the SYSTEM user id and password to complete the export and note the dump and log files for future use.*

#### PECS v6.2 Database Changes

The following Database changes are needed for PECS v6.2:

A new column VAUID has been added to the PECS User table.

The initial set of PBM NDF users with all the roles must be inserted into the PECS User table.

The following steps should be followed to alter the PECS User table:

1. Login to the SQL client using the CTSTAGING user account.

Execute the “PECS61\_Alter\_CT\_USERS\_VA\_Table.sql” script.

Open the log file and search the log file for any errors.

The following steps should be followed to insert the initial set of users into the PECS User table:

1. Login to the SQL client using the CTSTAGING user account.
2. Execute the “PECS61\_Insert\_PBM\_Users \_CT\_USERS\_VA\_Table.sql” script.
3. Open the log file and search the log file for any errors.

#### PECS v6.2 Database Migration Rollback

To restore the PECS v6.1 schema from the backup taken prior to the migration in section 3.2.8.1, follow the procedures outlined in the Data Import Guide for platform specific instructions (Unix, Windows).

Procedures for restoring/loading production data include the following steps regardless of platform:

Prepare database for restoring production data

- Drop existing schema objects (tables, sequences) for each schema using the Build\_Script\_to\_Drop\_CTSTAGING\_objects.sql to drop all the database objects in the CTSTAGING schema. Execute the Build\_Script\_to\_Drop\_CTSTAGING\_objects.sql script using the SYSTEM id and password.

Import the CTSTAGING schema by issuing the following commands logged in as a USER with DBA privileges preferably SYSTEM:

- **impdp DUMPFILE** =&lt;dumpfilename.dmp&gt; **SCHEMAS** =CTSTAGING **LOGFILE** =&lt;logfilename.log&gt; **CONTENT** =ALL **TABLE\_EXISTS\_ACTION** =REPLACE

*When prompted, enter the SYSTEM user id and password to complete the import. Review log files for each import to verify the successful completion of the rollback.*

**Note:** The migration and rollback process for the PECS database does not impact the FDB\_DIF schema.

## Users

PECS uses the IAM SSOi service for user authorization. IAM SSOi authenticates users against Active Directory. PECS can be accessed by all VA users authenticated using the PIV. The user roles are managed with the PECS application. Access to user is initially limited to read-only or Requestor role in the PECS Database. If the users need additional privileges, they need to contact the PBM NDF managers to get roles with higher access privileges.

## WebLogic Application Server Configuration

The WebLogic server configuration assumes that there is an existing WebLogic server installed and domain configured for use by the PECS application. Configuration steps to set up data sources will depend on the version of the WebLogic server. Furthermore, it is assumed that the installation of the WebLogic server and domain follows existing standards for a production environment installation. The configuration steps detailed below include the configuration of two data sources and the deployment of the PECS EAR archive.

### Dependency Installation

VistALink Version 1.6.0.028 and KAAJEE Version 1.1.0.007 software packages must be installed prior to deployment of PECS on the WebLogic server. Follow the respective installation guides supplied by the VA for this software prior to continuing with this installation.

Please read Appendix C and ensure the administrative KAAJEE user is installed prior to installing the PECS EAR file.

**Note:** Prior to the PECS EAR file deployment, the KAAJEE station ID configuration information must be updated to refer to the target VistA server. This information is updated in the &lt;station-number&gt; section of the WEB-INF\kaajeeConfig.xml file that is in the EAR deployment archive. Example steps to perform this process are outlined below (*NIX based):

Explode the CT\_EAR.ear file, explode CT\_WEB.war inside the exploded CT\_EAR.file, then edit CT\_EAR.ear/CT\_WEB.war/WEB-INF/ kaajeeConfig.xml to set the institution IDs.

The steps described above would literally translate to the following Linux commands:

Edit the file:

cp CT\_EAR.ear /tmp

cd /tmp

mkdir CT\_EAR

cd CT\_EAR

jar -xvf ../CT\_EAR.ear

jar -xvf CT\_WEB.war WEB-INF/kaajeeConfig.xml

vi WEB-INF/kaajeeConfig.xml

Save and restore the modified EAR file:

jar -uvf CT\_WEB.war WEB-INF/kaajeeConfig.xml

rm -rf WEB-INF/

mv ../CT\_EAR.ear ../CT\_EAR.ear.orig

jar -cvf ../CT\_EAR.ear *

cd ..

rm -rf CT\_EAR

### Configure WebLogic Data Sources

There are two data sources that need to be configured on the WebLogic administration server for the PECS application. Configuration values for the URL, Username, and Password will be dependent on where the FDB and STAGING databases have been installed. The configuration for each data source is summarized below:

**Note:** Contact the DBA for the HOST\_SERVER, DATABASE\_SID and passwords used below. These items are bolded surrounded by percent signs below. When entering the information, do not enter the percent signs.

Name: CTFdbData source

JNDI Name: jdbc/CTFdbData source

URL: jdbc:oracle:thin:@ **%HOST\_SERVER%** :%port%: **%DATABASE\_SID%**

Driver: oracle.jdbc.xa.client.OracleXAData source

Username: FDB\_DIF\_APP\_USER

Password: **%FDB\_DIF\_APP\_USER\_PASSWORD%**

Name: CTStagingData source

JNDI Name: jdbc/CTStagingData source

URL: jdbc:oracle:thin:@ **%HOST\_SERVER%** :%port%: **%DATABASE\_SID%**

Driver: oracle.jdbc.xa.client.OracleXAData source

Username: CTSTAGING\_UPDATE\_USER

Password: **%CTSTAGING\_UPDATE\_USER\_PASSWORD%**

### WebLogic Server Startup Configuration

PECS requires additional arguments added to the WebLogic Server’s Server Start properties. This section details the steps to add the arguments to the server.

1. Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://&lt;Deployment Machine&gt;:7001/console.

Click on **Environment** and then **Servers** on the panel found in the right column of the WebLogic console. Click on the server name corresponding to the deployment server in the **Summary of Servers** panel found in the right column of the WebLogic console. **For reference only** , see the figure below.

Figure 2: Summary of Servers

<!-- image -->

WebLogic will now display the panel **Settings for Deployment Server** in the right column of the console, where configuration of the Deployment Server is set. For reference, see the figure below.

Figure 3: Settings for Deployment Server

<!-- image -->

Click on the **Server Start** tab.

WebLogic will now display the panel Server Start tab in the **Settings for Deployment Server** in the right column of the console, where configuration of the Deployment Server is set. For reference, see the figure below.

Figure 4: Server Start Tab

<!-- image -->

Insert the following text in the **Arguments** box:

**-d64 -server -Xms768m -Xmx4096m -XX:PermSize=256m -XX:MaxPermSize=512m -Djava.awt.headless=true**

Also add an argument for Log4j2 file. (See example below. Modify path per the server configuration.)

**-Dlog4j.configuration=file:/u01/app/user\_projects/domains/sqa\_PECS/log4j2.xml**

Click **Save** .

### Configure WebLogic JTA

The application requires the Setting the JTA Transaction Timeout for processing of reports.

1. In the WebLogic Administration Console, expand **Services** .

Click on **JTA** .

On the Configuration tab, for “Timeout Seconds”, change the value to **600** (see below Console screen).

Click the **Save** button.

The WebLogic Administration Console screen should look like the following:

Figure 5: WebLogic Console Screen -- Completion

<!-- image -->

### Configure exportfile.properties

One functional piece of PECS allows a Release Manager to export data from the Oracle database so that it can be imported at various sites to support the Order Check process. The export file can be downloaded to the user’s desktop, but a copy needs to be sent to a File Transfer Protocol (FTP) server so that it can be utilized in other server processes. To know where to place the file, a property file named exportfile.properties needs to be created. This file should reside in the DOMAIN\_HOME/user\_staged\_config directory and be readable by the user who runs the WebLogic application server.

Configure the parameters in this file to match the settings of the particular environment where the installation is to be held. The export.file.server, export.file.dir, export.user.name, and export.user.pw much match the configuration of the sftp server.

The export.file.name.fragment and export.file.search.type values should both be set for the production values in the production environment, and to the Non-production values for all other environments.

The fdb.flag.provider.url value should be configured with the servername and port where DATUP National is running.

This sample exportfile.properties file is provided as an example. All parameter values should be configured for the environment where PECS is installed.

# Configure the following 4 sftp connection parameters to match

# the sftp server properties

export.file.server=vaauspresftp02.aac.REDACTED

export.file.dir=/home/presftp/pecs\_ioc/fdb\_dif

export.user.name=presftp

export.user.pw=password

# Cron hour 0-23

scheduled.time.hour=06

# Cron minute 0-59

scheduled.time.minute=00

#Production Value File Name

#export.file.name.fragment=UPD

#Production Values Search type

#export.file.search.type=contains

#Non-production Value File Name

export.file.name.fragment=I

#Non-production Values Search type

export.file.search.type=starts\_with

fdb.flag.provider.url=t3://vaauspecapp60.aac.REDACTED:8007

### Application Deployment

The following sections explain how to deploy the PECS Application and the PECS Help Application.

#### PECS Application Deployment

Specific deployment steps will vary depending on the version of the WebLogic server the PECS application will be deployed on. The PECS application is a J2EE application packaged in a standard EAR file format. The application should be deployed following the recommended process for deploying EAR files for the WebLogic server version platform. Use default values to deploy the Ear file and associate it with domain/server as per WebLogic install for PECS.

See Appendix G for recommended steps when upgrading from a previous release of PECS.

**Note:** Associate the application with the target server, and activate the application after deployment, before it can service any requests.

#### PECS Help Application Deployment

Specific deployment steps will vary depending on the version of the WebLogic server the PECS Help application will be deployed on. The PECS Help application is a RoboHelp application packaged in a standard EAR file format. The Help application should be deployed following the recommended process for deploying EAR files for the WebLogic server version platform. Use default values to deploy the Ear file and associate it with domain/server as per WebLogic install for PECS. Some recommended pointers for install of pecs-hlp.xxx.ear file:

Install the deployment as an application (PECS Help application is accessible at the context root “pecsHelp”).

On deployment targets page, select the PECS managed server.

On Optional Settings page, name the deployment – “pecs-Help”.

**Note:** Associate the Help application with the target server, and activate the application after deployment, before it can service any requests.

### Configure log4j2.xml

1. Copy log4j-1.2.17.jar and slf4j-api-1.7.10.jar to server/lib folder where WebLogic is installed - /u01/app/Oracle\_Home/wlserver/server/lib, for example.

Follow the steps in Section 5.3 to add the path to the log4j-1.2.17.jar, slf4j-api-1.7.10.jar and wllog4j.jar on the Server Start tab of the PECS managed server.

Example: /u01/app/Oracle\_Home/wlserver/server/lib/ log4j-api-2.10.0.jar:/u01/app/Oracle\_Home/wlserver/server/lib/wllog4j.jar

Follow the steps in Section 5.3 to add the follow argument on the Server Start tab of the PECS managed server: -Dweblogic.log.Log4jLoggingEnabled=true.

Open and log into the WebLogic console, using an administrative user name and password. The WebLogic console is located at: http://&lt;Deployment Machine&gt;:7001/console.

Click on Environment and then Servers on the panel found in the right column of the WebLogic console. Click on the server name corresponding to the deployment server in the Summary of Servers panel found in the right column of the WebLogic console. For reference only, see the figure below.

Figure 6: Summary of Servers

<!-- image -->

WebLogic will now display the panel **Settings for Deployment Server** in the right column of the console, where configuration of the Deployment Server is set. For reference, see the figure below.

Figure 7: Settings for Deployment Server

<!-- image -->

Click on the **Logging** tab.

Click Advanced to expand the advanced settings.

Select Log4J as the Logging Implementation.

Figure 8: Advanced Logging Settings

<!-- image -->

Click Save.

The PECS application uses log4j loggers to create and write log information to application event logs. The logging properties for the PECS application are included in Appendix A. Logger and appender configuration is included for the PECS application, and optionally the Hibernate API. Update logging properties as appropriate to the host server:

Set logging level to “info” for production mode.

Set “File” properties to the identified log directory on the server.

Set “ConversionPattern” to the standard VA pattern.

The properties in Appendix A should be inserted into the existing log4j properties file that exists at the beginning of the WebLogic server class path (please use log4j.xml for reference from Appendix A).

## Post-Installation Notes

**Note:** Due to policy constraints, active links cannot be included in this document. Please copy and paste the URLs into the browser.

The entrance URL for the application is: http://%SERVER%:%PORT%/ct/public/Welcome.html.

This is a generic URL for PECS. Replace the %SERVER% and %PORT% with the server name and port number assigned to the deployment.

For example, the entrance URL for the AITC SQA server is as follows: *http://vaww.oed.portal. REDACTED/projects/pre/PRE\_IPT\_Rev/PRE\_IPT\_Rev\_PECS2-1/default.aspx*

## Properties of log4j2

&lt;?xml version="1.0" encoding="UTF-8"?&gt;

&lt;!-- Configuration has an attribute named status that you can set to trace or debug to get configuration messages from Log4J2. --&gt;

&lt;!-- monitorInterval: Configure log4j to refresh the configuration periodically. --&gt;

&lt;Configuration monitorInterval="30"&gt;

&lt;Properties&gt;

&lt;Property name="logDir"&gt;PECSLogs&lt;/Property&gt;

&lt;Property name="maxFileSize"&gt;10 MB&lt;/Property&gt;

&lt;Property name="maxRolloverFiles"&gt;10&lt;/Property&gt;

&lt;Property name="logPattern"&gt;%d{DEFAULT} %-5p [%t] [%c:%M] %m%n&lt;/Property&gt;

&lt;/Properties&gt;

&lt;Appenders&gt;

&lt;RollingFile name="Server" filename="${logDir}/server.log" filePattern="${logDir}/server-%i.log"&gt;

&lt;PatternLayout&gt;

&lt;Pattern&gt;${logPattern}&lt;/Pattern&gt;

&lt;/PatternLayout&gt;

&lt;Policies&gt;

&lt;OnStartupTriggeringPolicy /&gt;

&lt;SizeBasedTriggeringPolicy size="${maxFileSize}" /&gt;

&lt;/Policies&gt;

&lt;DefaultRolloverStrategy max="${maxRolloverFiles}"/&gt;

&lt;/RollingFile&gt;

&lt;RollingFile name="Hibernate" fileName="${logDir}/hibernate.log" filePattern="${logDir}/hibernate-%i.log"&gt;

&lt;PatternLayout&gt;

&lt;Pattern&gt;${logPattern}&lt;/Pattern&gt;

&lt;/PatternLayout&gt;

&lt;Policies&gt;

&lt;OnStartupTriggeringPolicy /&gt;

&lt;SizeBasedTriggeringPolicy size="${maxFileSize}" /&gt;

&lt;/Policies&gt;

&lt;DefaultRolloverStrategy max="${maxRolloverFiles}"/&gt;

&lt;/RollingFile&gt;

&lt;RollingFile name="Peps" fileName="${logDir}/peps.log" filePattern="${logDir}/peps-%i.log"&gt;

&lt;PatternLayout&gt;

&lt;Pattern&gt;${logPattern}&lt;/Pattern&gt;

&lt;/PatternLayout&gt;

&lt;Policies&gt;

&lt;OnStartupTriggeringPolicy /&gt;

&lt;SizeBasedTriggeringPolicy size="${maxFileSize}" /&gt;

&lt;/Policies&gt;

&lt;DefaultRolloverStrategy max="${maxRolloverFiles}"/&gt;

&lt;/RollingFile&gt;

&lt;RollingFile name="Spring" fileName="${logDir}/spring.log" filePattern="${logDir}/spring-%i.log"&gt;

&lt;PatternLayout&gt;

&lt;Pattern&gt;${logPattern}&lt;/Pattern&gt;

&lt;/PatternLayout&gt;

&lt;Policies&gt;

&lt;OnStartupTriggeringPolicy /&gt;

&lt;SizeBasedTriggeringPolicy size="${maxFileSize}" /&gt;

&lt;/Policies&gt;

&lt;DefaultRolloverStrategy max="${maxRolloverFiles}"/&gt;

&lt;/RollingFile&gt;

&lt;RollingFile name="Struts" fileName="${logDir}/struts.log" filePattern="${logDir}/struts-%i.log"&gt;

&lt;PatternLayout&gt;

&lt;Pattern&gt;${logPattern}&lt;/Pattern&gt;

&lt;/PatternLayout&gt;

&lt;Policies&gt;

&lt;OnStartupTriggeringPolicy /&gt;

&lt;SizeBasedTriggeringPolicy size="${maxFileSize}" /&gt;

&lt;/Policies&gt;

&lt;DefaultRolloverStrategy max="${maxRolloverFiles}"/&gt;

&lt;/RollingFile&gt;

&lt;RollingFile name="CT"  fileName="${logDir}/ct\_prod.log" filePattern="${logDir}/ct\_prod-%i.log"&gt;

&lt;PatternLayout&gt;

&lt;Pattern&gt;${logPattern}&lt;/Pattern&gt;

&lt;/PatternLayout&gt;

&lt;Policies&gt;

&lt;OnStartupTriggeringPolicy /&gt;

&lt;SizeBasedTriggeringPolicy size="${maxFileSize}" /&gt;

&lt;/Policies&gt;

&lt;DefaultRolloverStrategy max="${maxRolloverFiles}"/&gt;

&lt;/RollingFile&gt;

&lt;RollingFile name="PECS"  fileName="${logDir}/pecs\_prod.log" filePattern="${logDir}/pecs\_prod-%i.log"&gt;

&lt;PatternLayout&gt;

&lt;Pattern&gt;${logPattern}&lt;/Pattern&gt;

&lt;/PatternLayout&gt;

&lt;Policies&gt;

&lt;OnStartupTriggeringPolicy /&gt;

&lt;SizeBasedTriggeringPolicy size="${maxFileSize}" /&gt;

&lt;/Policies&gt;

&lt;DefaultRolloverStrategy max="${maxRolloverFiles}"/&gt;

&lt;/RollingFile&gt;

&lt;/Appenders&gt;

&lt;Loggers&gt;

&lt;Logger name="REDACTED.pharmacy.ct" level="debug" additivity="false"&gt;

&lt;AppenderRef ref="CT" /&gt;

&lt;/Logger&gt;

&lt;Logger name="REDACTED.pharmacy.ct.web" level="debug" additivity="false"&gt;

&lt;AppenderRef ref="CT" /&gt;

&lt;/Logger&gt;

&lt;Logger name="REDACTED.monitor.time.AuditTimer" level="info" additivity="false"&gt;

&lt;AppenderRef ref="Server" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.apache.beehive.netui.pageflow.internal.AdapterManager" level="warn" additivity="false"&gt;

&lt;AppenderRef ref="Server" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.apache.logging.log4j" level="warn" additivity="false"&gt;

&lt;AppenderRef ref="Server" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.apache.commons" level="warn" additivity="false"&gt;

&lt;AppenderRef ref="Server" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.hibernate.engine.jdbc" level="info" additivity="false"&gt;

&lt;AppenderRef ref="Hibernate" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.hibernate.jdbc" level="debug" additivity="false"&gt;

&lt;AppenderRef ref="Hibernate" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.hibernate.SQL" level="debug" additivity="false"&gt;

&lt;AppenderRef ref="Hibernate" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.hibernate.hql" level="debug" additivity="false"&gt;

&lt;AppenderRef ref="Hibernate" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.hibernate" level="info" additivity="false"&gt;

&lt;AppenderRef ref="Hibernate" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.hibernate.type" level="warn" additivity="false"&gt;

&lt;AppenderRef ref="Hibernate" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.hibernate.loader" level="warn" additivity="false"&gt;

&lt;AppenderRef ref="Hibernate" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.hibernate.impl" level="warn" additivity="false"&gt;

&lt;AppenderRef ref="Hibernate" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.springframework" level="error" additivity="false"&gt;

&lt;AppenderRef ref="Spring" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.apache.struts2" level="error" additivity="false"&gt;

&lt;AppenderRef ref="Struts" /&gt;

&lt;/Logger&gt;

&lt;Logger name="com.opensymphony.xwork2" level="error" additivity="false"&gt;

&lt;AppenderRef ref="Struts" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.apache.commons.digester" level="error" additivity="false"&gt;

&lt;AppenderRef ref="Struts" /&gt;

&lt;/Logger&gt;

&lt;Logger name="freemarker.cache" level="error" additivity="false"&gt;

&lt;AppenderRef ref="Struts" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.apache.tiles" level="error" additivity="false"&gt;

&lt;AppenderRef ref="Struts" /&gt;

&lt;/Logger&gt;

&lt;Logger name="net.sf.navigator" level="error" additivity="false"&gt;

&lt;AppenderRef ref="Struts" /&gt;

&lt;/Logger&gt;

&lt;Logger name="org.displaytag" level="error" additivity="false"&gt;

&lt;AppenderRef ref="Struts" /&gt;

&lt;/Logger&gt;

&lt;Logger name="REDACTED pharmacy.peps" level="error" additivity="false"&gt;

&lt;AppenderRef ref="Peps" /&gt;

&lt;/Logger&gt;

&lt;!-- ================================================== --&gt;

&lt;!-- Loggers for PECS --&gt;

&lt;!-- ================================================== --&gt;

&lt;Logger name="REDACTED.pharmacy.pecs" level="info" additivity="false"&gt;

&lt;AppenderRef ref="PECS" /&gt;

&lt;/Logger&gt;

&lt;Logger name="REDACTED.pharmacy.pecs" level="debug" additivity="false"&gt;

&lt;AppenderRef ref="PECS" /&gt;

&lt;/Logger&gt;

&lt;Logger name="REDACTED.pharmacy.pecs.web" level="info" additivity="false"&gt;

&lt;AppenderRef ref="PECS" /&gt;

&lt;/Logger&gt;

&lt;Logger name="REDACTED.pharmacy.pecs.web" level="debug" additivity="false"&gt;

&lt;AppenderRef ref="PECS" /&gt;

&lt;/Logger&gt;

&lt;!-- ================================================== --&gt;

&lt;!-- Loggers for CT --&gt;

&lt;!-- ================================================== --&gt;

&lt;Logger name="REDACTED.pharmacy.ct" level="info" additivity="false"&gt;

&lt;AppenderRef ref="CT" /&gt;

&lt;/Logger&gt;

&lt;Logger name="REDACTED.pharmacy.ct.web" level="info"

additivity="false"&gt;

&lt;AppenderRef ref="CT" /&gt;

&lt;/Logger&gt;

&lt;Root level="Info"&gt;

&lt;AppenderRef ref="Server" /&gt;

&lt;AppenderRef ref="Hibernate" /&gt;

&lt;AppenderRef ref="Spring" /&gt;

&lt;AppenderRef ref="Struts" /&gt;

&lt;AppenderRef ref="CT" /&gt;

&lt;AppenderRef ref="PECS" /&gt;

&lt;/Root&gt;

&lt;/Loggers&gt;

&lt;/log4j:configuration&gt;

## Custom Update File Installation

Introduction

This appendix describes the process to load the FDB-DIF and PECS update files into an existing FDB-DIF Oracle database using the FDB Updater Tool. The FDB-DIF update file is received on a schedule from FDB every two weeks and must be loaded in sequence. The PECS update file can be generated from the PECS application interface at any time by a user in the Release Manager role and loaded with the FDB Update Tool.

Scope

This appendix will include the process to update the FDB-DIF Oracle database with the FDB and PECS Update files using the FDB Update Tool.

Processes in scope will include:

The process to load the FDB-DIF file using the FDB Update Tool.

The process to load the PECS update file using the FDB Update Tool.

The process to recover the FDB-DIF FDB\_CUSTOM\_* tables if a Custom Tables update file load failure should occur.

Processes out of scope will *include* :

The process to receive the FDB-DIF update file from FDB.

The process to generate the PECS update file from the Custom Tables application.

The process to recover the FDB-DIF database if a FDB-DIF update file load failure should occur.

Update Process Prerequisites

The FDB Updater Tool is installed on the machine performing the update process.

The FDB and PECS update files are available and/or have been generated.

The FDB-DIF update file must be loaded in sequence. The version number of the new file must be the next in sequence.

The user performing Oracle operations must have sufficient rights to delete data, drop, and create tables.

The PECS preparation and recovery SQL scripts are available.

An Oracle tool such as SQLPlus, must be installed on the machine executing the FDB Updater tool.

Apply FDB-DIF Update File

Here are the steps required to execute the FDB update tool:

1. Obtain the FDB-DIF Update File
    - Either download the update file from the FTP directory or insert the update CD into drive.

Start FDB Update Tool GUI

- Navigate to where the FDB Update Tool has been installed and click on the GUI.bat file.

Configure Connection

- Select the View  Setting menu option on the GUI and input the connection data relevant to your location and select the “Save” button. A sample screen is shown.

Figure 6: Update Settings - Configure Connection

<!-- image -->

Provide File Paths

- Enter the path to the update and log files relevant your location. Select whether the update is incremental or complete, then the Start button. A sample screen is shown:

Figure 7: Add Paths to FDB Data Updater

<!-- image -->

Apply Custom Tables Update File

This section describes the two major steps necessary to apply the Custom Tables Update File.

1. Verify CT\_VERSION Table:

The CT\_VERSION table is an additional table added to the FDB schema (as recommended by FDB) to track the PECS update file version. If the table does not exist, execute the following DDL:

CREATE TABLE FDB.CT\_VERSION

(

VERSIONKEY NUMBER(6) NOT NULL,

DBVERSION VARCHAR2(5) NULL,

BUILDVERSION VARCHAR2(5) NULL,

FREQUENCY VARCHAR2(1) NULL,

ISSUEDATE VARCHAR2(8) NULL,

VERSIONCOMMENT VARCHAR2(80) NULL,

DBTYPE VARCHAR2(10) NULL

)

CREATE UNIQUE INDEX PKCTVERSION ON FDB.CT\_VERSION(VERSIONKEY)

Execute FDB Update Tool:

The steps to apply the Custom Tables Update file are the same steps as outlined in Apply FDBDIF Update File. Instead of entering the path to the FDB-DIF update file, enter the path to the Custom Tables Update file, relevant to your location. Select whether the update is incremental or complete. Click the Start button.

Recover FDB-DIF Custom Tables from Load Failure

The recover process may be necessary if a failure has occurred during the application of the PECS Update file (see Apply Custom Tables Update File step). The recovery process involves the execution of a SQL script, and verification that the data has been recovered.

Execute Recovery

- The recovery entails the deletion of any data that may have been loaded to the FDB\_CUSTOM\_* tables during the execution of the update process.

Verify Data Recovery

- Verify that the data in the FDB\_CUSTOM\_* tables has been deleted.

Generate Full PECS Update File

- After logging into the PECS application, a user in the Release Manager role will navigate to the Custom Update tab and click the Download New Full Update button. This will generate a PECS update file with all currently approved order check customizations.

## PECS Logical Deployment Architecture

Logical Deployment Design – PECS

**Application Server:**

The WebLogic Application Server 12.1.3 will host PECS and its business services.

**Database Server:**

The Database Server- Oracle 11g will have Red Hat Linux Enterprise version RHEL5 as its OS. It will host the Custom Table Staging database and FDB-DIF database.

**Failover Server:**

There will be a Failover server. It will host both Oracle WebLogic Application Server and Oracle Database Server to provide redundancy. The figure below shows the overview of Logical Deployment Design for the PRE PECS Application.

Figure 8: PECS Deployment

<!-- image -->

SiteMinder Web Agent on Apache Web Server – PECS

Figure : Web Agent High-Level Diagram

<!-- image -->

## PECS Database Installation Process

Database Installation Process Flow – PECS

Figure 10: Database Installation Process

<!-- image -->

## Rollback Process

If the installation process must be stopped when updating an environment from a previous version of PECS, use the following to determine and follow the steps outlined in order to roll back the application.

If both the database and the application have been deployed:

1. Shutdown the WebLogic domain.

Follow the instructions in section 3.2.8.3 PECS v6.2 Database Migration Rollback in this document.

Start the WebLogic domain.

Deploy the prior version of PECS using the instructions in section 5.6 Application Deployment in this document.

If only the database has been deployed

1. Shutdown the WebLogic domain.

Follow the instructions in section 3.2.8.3 PECS v6.2 Database Migration Rollback in this document.

Start the WebLogic domain.

## PECS Upgrade Installation Instructions

1. Stop the WebLogic managed server.

Delete the previous PECS deployment.

From the Linux server, navigate to the managed server directory that contains the tmp and stage folders. For example: /u01/app/user\_projects/domains/DEVPHARMACYPECS/servers/PECS\_MS1

Remove the tmp and stage folders and their contents from this directory.

Start the managed server.

Stop the managed server.

Proceed with the deployment of the new PECS ear file.