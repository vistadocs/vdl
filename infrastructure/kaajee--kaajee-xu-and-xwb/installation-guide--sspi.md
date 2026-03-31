---
consolidated_title: "kaajee sspi installation guide"
app_code: KAAJEE
doc_type: IG
master_source: "KAAJEE SSPI Installation Guide 1.3 (WebLogic 10.3.6 and higher)"
master_pub_date: February 2021
consolidated_from: 2 versions
prior_versions:
  - "KAAJEE SSPI 8.0.781 Installation Guide (WebLogic 12.2)"
---

![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/001.png)

KERNEL AUTHENTICATION & AUTHORIZATION FOR J2EE (KAAJEE) VERSION 1.2.0andSECURITY SERVICE PROVIDER INTERFACE (SSPI)VERSION 1.3.0FOR WEBLOGIC (WL) VERSIONS 10.3.6 AND HIGHERINSTALLATION GUIDE

February 2021

Office of Information and Technology

Product Development

*This page is left blank intentionally.*

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Figures](#figures)
- [Tables](#tables)
- [Orientation](#orientation)
- [Pre-Installation Instructions](#pre-installation-instructions)
  - [Purpose](#purpose)
  - [Distribution Files](#distribution-files)
  - [Installer/Developer Notes—KAAJEE Software First-Time Installations and Upgrades](#installerdeveloper-noteskaajee-software-first-time-installations-and-upgrades)
  - [Application Server Environment Requirements](#application-server-environment-requirements)
- [Installation Overview](#installation-overview)
  - [WebLogic v 10.3 and Higher Server Preparation](#weblogic-v-103-and-higher-server-preparation)
  - [KAAJEE SSPI Installation](#kaajee-sspi-installation)
  - [This page is left blank intentionally.](#this-page-is-left-blank-intentionally)
  - [KAAJEE SSPI 1.3 rollback](#kaajee-sspi-13-rollback)
    - [Re-Deploy SSPI 1.2 Software](#re-deploy-sspi-12-software)
  - [Undeploy SSPI 1.2 and before](#undeploy-sspi-12-and-before)
Documentation Revisions
The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.
<span id="_Toc44314849" class="anchor"></span>Table i. Documentation revision history
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 59%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author(s)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/2020</td>
<td>Updated the guide with relation to the KAAJEE SSPI 1.3 release</td>
<td><p>Health Product Support (HPS)</p>
<p>(REDACTED)</p></td>
</tr>
<tr class="even">
<td>07/2020</td>
<td><p>Updated software and documentation with TRM and Fortify compliance items.</p>
<p><strong>Software Version: 1.2.0.005</strong></p>
<p><strong>Security Service Provider Interface (SSPI) Version: 1.2.0.005</strong></p>
<p><strong>Kernel Patches: XU*8.0*694 and XU*8.0*696</strong></p></td>
<td><p>Health Product Support (HPS)</p>
<p>(REDACTED)</p></td>
</tr>
<tr class="odd">
<td>03/2011</td>
<td><p>Software and documentation for KAAJEE 1.1.0.007 and KAAJEE Security Service Provider Interface (SSPI) 1.1.0.002, referencing VistALink 1.6 and WebLogic 10.3.6 and higher.</p>
<p><strong>Software Version: 1.1.0.007</strong></p>
<p><strong>Security Service Provider Interface (SSPI) Version: 1.1.0.002</strong></p>
<p><strong>Kernel Patch: XU*8.0*504</strong></p></td>
<td><p>Product Development Services Security Program HWSC development team.</p>
<p>(REDACTED)</p></td>
</tr>
<tr class="even">
<td>05/2006</td>
<td><p>Initial software and documentation for KAAJEE 1.0.0.019 and KAAJEE Security Service Provider Interface (SSPI) 1.0.0.010, referencing VistALink 1.5 and WebLogic 8.1.</p>
<p><strong>Software Version: 1.0.0.019</strong></p>
<p><strong>Security Service Provider Interface (SSPI) Version: 1.0.0.010</strong></p>
<p>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/002.png) <strong>NOTE:</strong> For a description of the current KAAJEE software version numbering scheme, please review the readme.txt file distributed with the KAAJEE software.</p>
<p>In the future, the Development Technology Advisory Committee (DTAC) will be the authoritative source for determining future version numbering schemes for all Health<em><u>e</u></em>Vet-VistA software file and folder names.</p></td>
<td><p>ISS KAAJEE Development Team</p>
<p>(REDACTED)</p></td>
</tr>
</tbody>
</table>
Patch Revisions
For a complete list of patches related to this software, please refer to the Patch Module on FORUM.
Contents

# Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the installation and use of KAAJEE and the functionality it provides for Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA) software products.

The installation instructions for KAAJEE are organized and described in this guide as follows:

1.  Pre-Installation Instructions.
2.  Installation Overview
3.  Error! Reference source not found.
4.  Java 2 Platforms, Enterprise Edition (J2EE) Application Server Installation Instructions

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/003.png)</th>
<th><p>Where necessary, separate steps for the following two supported operating systems are provided:</p>
<ul>
<li><p>Linux (i.e., Red Hat Enterprise ES 6.0 or higher)</p></li>
<li><p>Windows</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

There are no special legal requirements involved in the use of KAAJEE.

This manual uses several methods to highlight different aspects of the material:

- Various symbols/terms are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols/terms:

<span id="_Ref345831418" class="anchor"></span>Table ii. Documentation symbol/term descriptions

| Symbol                                                                                                                                         | Description                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/004.png)                                     | NOTE/REF: Used to inform the reader of general information including references to additional reading material.                                                   |
| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/005.png)                                  | CAUTION or DISCLAIMER: Used to inform the reader to take special notice of critical information.                                                                  |
| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/006.png) | UPGRADES/FIRST-TIME INSTALLATION: Used to denote Upgrade or First-time installation instructions only.                                                            |
| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/007.png)                                                                                                  | Skip forward to the referenced step or procedure that is indicated.                                                                                                   |
| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/008.png)                                                                                                  | Instructions that only apply to the Linux operating systems (i.e., Red Hat Enterprise ES 3.0 or higher) are set off and indicated with this Linux "Tux" penguin icon. |
|                                                                                                                                                    | Instructions that only apply to Microsoft Windows operating systems (i.e., Microsoft Windows 2000 or XP) are set off and indicated with this stylized "Windows" icon. |

- Descriptive text is presented in a proportional font (as represented by this font).
- "Snapshots" of computer online displays (i.e., roll-and-scroll screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts and some software code reserved/key words will be bold typeface.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/009.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|

- Java software code, variables, and file/folder names can be written in lower or mixed case.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistALink—VistA M Server and Application Server software
- Linux (i.e., Red Hat Enterprise ES 6.0 or higher) or Microsoft Windows environment
- Java Programming languageJava 1.7 Standard Edition (J2SE) Java Development Kit (JDK, a.k.a. Java Software Development Kit \[SDK\])
- WebLogic 10.3.6 and higher—Application server
- Oracle Database 11*g*—Database (e.g., Security Service Provider Interface \[SSPI\] or Standard Data Services \[SDS\] 13.0 (or higher) database/tables)
- Oracle SQL\*Plus Software 11 (or higher)

This manual provides an overall explanation of the installation procedures and functionality provided by the Kernel Authentication & Authorization for J2EE (KAAJEE) on Weblogic Application Server Versions 10.3.6 and higher software; however, no attempt is made to explain how the overall HealtheVet-VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the VA Intranet for a general orientation to HealtheVet-VistA at the following address:

> redacted

Reference Materials

Readers who wish to learn more about KAAJEE should consult the following:

- *Kernel Authentication & Authorization for J2EE (KAAJEE) Installation Guide  
  > (SSPI 1.3.0.xxx)*, this manual
- *Kernel Authentication & Authorization for J2EE (KAAJEE) Deployment Guide  
  > (SSPI 1.3.0.xxx)*
- *VistALink Installation Guide*
- *VistALink System Management Guide*
- *VistALink Developer Guide*

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/010.png)</th>
<th><p><strong>REF:</strong> For more information on VistALink, please refer to the Application Modernization Foundations Web site located at the following Web address:</p>
<blockquote>
<p>redacted</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Health*<u>e</u>*Vet-VistA documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

Health*<u>e</u>*Vet-VistA documentation can be downloaded from the VHA Software Document Library (VDL) Web site:

> <http://www.va.gov/vdl/>

Health*<u>e</u>*Vet-VistA documentation and software can also be downloaded from the Enterprise Product Support (EPS) anonymous directories:

- Preferred Method (REDACTED)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/011.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for installing the Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA) Kernel Authentication and Authorization for Java (2) Enterprise Edition (KAAJEE) and related software.

KAAJEE is *not* an application but a framework. Users of the software need to understand how it integrates in their working environment. Thus, installing KAAJEE means to understand what jars and files need to be put where and what are the configuration files that you need to have and edit.

KAAJEE provides secure sign-on architecture for Health*<u>e</u>*Vet-VistA Web-based applications.

These Health*<u>e</u>*Vet-VistA Web-based applications are able to authenticating against Kernel on the VistA M Server via an Internet Browser on the client workstation and a middle tier application server (e.g., WebLogic).

## Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/012.png) | NOTE: Please refer to "Table 1‑1. Application server minimum software/network tools/documentation required for KAAJEE" for confirmation of all KAAJEE and related software and documentation files. |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/013.png)</th>
<th><p><strong>REF:</strong> For the KAAJEE software preview/test release, all distribution files are available at the following Web address:</p>
<blockquote>
<p>(REDACTED)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Installer/Developer Notes—KAAJEE Software First-Time Installations and Upgrades

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

First-time KAAJEE installers *must* perform *all* installation steps/procedures, except where noted. Those installation steps/procedures that can be skipped during a first-time installation will be displayed as follows:

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/014.png) | FIRST-Time INSTALLATION: *First-time installation-specific instructions or information that can be skipped will be found here.* |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|

If you were a test site prior to the final release of KAAJEE, we have notated those installation steps/procedures that have special information based on the final software upgrades that may affect how you install the released version of KAAJEE or provide other pertinent information. The upgrade information will be displayed as follows:

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/015.png) | UPGRADES: *Upgrade-specific instructions or information will be found here.* |
|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|

In addition, we will use this section to also highlight any KAAJEE code changes from previous test/preview versions of the software to the released version of the software that may affect development teams coding KAAJEE-enabled applications.

## Application Server Environment Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/016.png) | NOTE: The information in this topic is directed at the systems management personnel responsible for maintaining the application servers. |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|

The following minimum software tools and files are required to install the KAAJEE software and documentation for application servers running KAAJEE-based Web applications:

<span id="_Ref193265772" class="anchor"></span>Table 1‑1. Application server minimum software/network tools/documentation required for KAAJEE

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Minimum Software/Configuration/<br />
Documentation</strong></th>
<th><strong>Version and Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Operating System Software</td>
<td><p>One of the following operating systems:</p>
<ul>
<li><blockquote>
<p>Linux (i.e., Red Hat Enterprise ES 3.0 or higher)</p>
</blockquote></li>
<li><blockquote>
<p>Microsoft Windows XP or 2000</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Application Server Software</td>
<td>WebLogic Versions 10.3 and higher application servers.</td>
</tr>
<tr class="odd">
<td>SSPI Software</td>
<td><p>KAAJEE SSPI 1.3</p>
<p>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/017.png) <strong>REF:</strong> Installation and configuration instructions are included in the Chapter 3, "<strong>Error! Reference source not found.</strong>," in this manual.</p></td>
</tr>
<tr class="even">
<td>VistALink Software</td>
<td>Version 1.6</td>
</tr>
<tr class="odd">
<td>VistA Kernel Software</td>
<td>Patch XU*8*504</td>
</tr>
<tr class="even">
<td>KAAJEE_1_3_RELEASENOTES.PDF</td>
<td><strong>Release Notes</strong> describes the changes to KAAJEE 1.1 to include new features and enhancements.</td>
</tr>
<tr class="odd">
<td>KAAJEE_1_3_INSTALLGUIDE.PDF</td>
<td><blockquote>
<p><strong>Installation Guide</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>KAAJEE_1_3_DEPLOYGUIDE.PDF</td>
<td><blockquote>
<p><strong>Deployment Guide</strong> outlines the details of KAAJEE-related software and gives guidelines on how the software is used within Health<em><u>e</u></em>Vet-Veterans Health Information Systems and Technology Architecture (VistA). It contains the User Manual, Programmer Manual, and Technical Manual information for KAAJEE.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XU_8_708.zip</td>
<td><blockquote>
<p><strong>Security Provider Interface (SSPI) Software.</strong> The KAAJEE SSPI software download Zip file for installation on the application server.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XU_8_708.zip.MD5</td>
<td><blockquote>
<p><strong>Security Service Provider Interface (SSPI) Software Checksum.</strong> The MD5 checksum value for the KAAJEE SSPI software download Zip file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

*This page is left blank intentionally.*

# Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides an overview of the installation procedures for the Kernel Authentication and Authorization for Java (2) Enterprise Edition (KAAJEE). The chapters that follow address the specific installations that comprise KAAJEE:

- Error! Reference source not found.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/018.png) | NOTE: Instructions for the VistA M Server installation can also be found in the description for Kernel Patch XU\*8\*504, located in the Patch Module on FORUM. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|

- Error! Reference source not found.

## WebLogic v 10.3 and Higher Server Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the VistALink 1.6 instructions to deploy your VistALink connector(s).

## KAAJEE SSPI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Unzip the Kaajee Security Provider zip distribution into a staging folder.

![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/019.png) FIRST-TIME INSTALLATIONS: Execute steps 2 and 3 if you have *never* deployed KAAJEE SSPIs on the WebLogic Application Server.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/020.png) | UPGRADES: Skip steps 2 and 3 if you have previously deployed KAAJEE SSPIs on the WebLogic Application Server and will be installing a newer version of the KAAJEE SSPIs. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

2.  New installation only - Create KAAJEE Schema & SSPI Tables –
1.  Contact the \*\*DBA to create the KAAJEE user ID, schema, and SSPI tables on the Oracle database.
2.  Create KAAJEE User ID & Schema.
3.  To create the SSPI tables, run the OracleTables.sql script, which can be found in the KAAJEE SSPI distribution zip file.
4.  Validate/Verify the Creation of the KAAJEE Database Schema & Tables. In summary, the DBA will need to perform the following procedures:
    - Identify and create an Oracle Tablespace to hold the KAAJEE schema.
    - Create a user account KAAJEE.
    - Give "connect" and "resource" and "unlimited tablespace" privileges to the user account.
    - The user account should have a "default" profile.
    - Set the default tablespace for the KAAJEE user to the one created earlier.
    - Set the default "TEMP" tablespace for the KAAJEE user.

#### New installation only - Create KAAJEE SSPI Tables

> KAAJEE requires the following two SSPI SQL database tables:

> <span id="_Ref78189754" class="anchor"></span>Table 2‑1. Caché Database—KAAJEE SSPI SQL table definitions

| KAAJEE SSPI Table Name | Description                                                      |
|----------------------------|----------------------------------------------------------------------|
| PRINCIPALS                 | This table has users and group data and is stored in a database.     |
| GROUPMEMBERS               | This table has users and group mappings and is stored in a database. |

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/021.png) | NOTE: We recommend that you create the KAAJEE SSPI database tables in the same schema created in the previous step. |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|

> Run the createSchema.sql script, which can be found in the KAAJEE SSPI distribution zip file (i.e., XU_8_708.zip) in the following directory:

> (REDACTED)

> This SQL script creates the required KAAJEE SSPI SQL table definitions.

> Use the terminal, or other similar software of your choice, to import the SQL script and run it to create/edit the SSPI SQL table definitions (Table 2‑1):

> <span id="_Ref120506928" class="anchor"></span>Figure 2‑1. Database—Sample SSPI SQL script for KAAJEE table definitions

> drop table Principals;

> drop table GroupMembers;

> create table Principals ( name varchar(32) not null, isuser varchar(10) not null, password varchar(40), CONSTRAINT Principals_pk PRIMARY KEY (name,isuser));

> create table GroupMembers ( principal varchar(32) not null, mygroup varchar(32) not null, CONSTRAINT GroupMembers_pk PRIMARY KEY (principal, mygroup));

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/022.png) | UPGRADES: You *must* perform steps 4 and 5 if you have previously deployed KAAJEE SSPIs on the WebLogic Application Server and will be installing a newer version of the KAAJEE SSPIs. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

> ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/023.png) FIRST-TIME INSTALLATIONS: Skip steps 4 and 5 if you have *never* deployed KAAJEE SSPIs on the WebLogic Application Server.

3.  Upgrade only – remove existing SSPI (Version 1.2 and prior) - [Undeploy prior version of SSPI Software](#undeploy-sspi-1.2-and-before)
4.  Upgrade only - Connect to the database with required privileges and execute the following commands (updateSchema.sql):

> alter table KAAJEE.PRINCIPALS MODIFY PASSWORD varchar2(40);

> commit();

> This command “upgrades” the database field to work with the upgraded security hashing algorithm that comes with a build-in SQAAuthenticationProvider.

#### Edit the createDSSSPI.properties file with information pertaining to your environment:

> There are several property values to edit. Pay special attention to the case and whitespace.

> The ds.name and the ds.jndi.name is better left unchanged. The rest of the datasource information gets copied from the existing KaajeeDatabase.properties file (for upgrades).

> (REDACTED)

5.  Locate and Run the setWLSEnv.sh script on the application server Ex(12.2):

(REDACTED)

> The file is located under the server/bin directory by default (Ex: REDACTED)

#### Run the java weblogic.WLST and pass the required properties file to the createDSSSPI.py

> java weblogic.WLST createDSSSPI.py -p createDSSSPI.properties

#### The script will attempt to create a new datasource, wire it up to a database and instantiate an instance of SQLAuthenticationProvider. Upon successful script completion, you will be asked to shutdown an admin server.

6.  Start the server; Log onto admin console.
7.  Navigate to the Authentication Directory:
    1.  Select Security Realms under Domain Structure.
    2.  Navigate to the Providers tab, as shown below:

\- Home \> Summary of Security Realms \> myrealm \> Providers

3.  Click on New in the Authentication tab
8.  Find the KaajeeManageableAuthenticator, ensure Control Flag is set to 'OPTIONAL'.
    1.  When returned to the Authentication page, select and edit the DefaultAuthenticator Authentication Provider.
    2.  Ensure that Control Flag is 'SUFFCIENT'.

> ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/024.png)

9.  Restart the admin server, if any changes to the Authentication Providers has been made.
10. Verify all Changes Have Taken Place:
    1.  Use the WebLogic console software (i.e., WebLogic Server 10.3.6 Console Login) to navigate to the following locations:
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Users tab)
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Groups tab)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/025.png) | NOTE: If this is a first-time install, you will not see users populated in the Oracle tables or in the WebLogic console. |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                |                                                                                                                              |

2.  Confirm presence of application-level users retrieved by the KaajeeManageableAuthenticator –

> (REDACTED)

## This page is left blank intentionally.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

######### Appendix A: Installation Back-Out or Roll-Back Procedure

## KAAJEE SSPI 1.3 rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate and Run the setWLSEnv.sh script on the application server

(REDACTED)

> The file is located under the server/bin directory by default (Ex: REDACTED)

#### Run the java weblogic.WLST and pass the required properties file to the deleteDSSSPI.py

> java weblogic.WLST deleteDSSSPI.py -p createDSSSPI.properties

#### The script will attempt to remove a datasource as well as the SQLAuthenticationProvider. It will use the same properties file. Upon successful script completion, you will be offered to shutdown an admin server. 

2.  Start the server; Log onto admin console.
3.  Navigate to the Authentication Directory:
    1.  Select Security Realms under Domain Structure.
    2.  Navigate to the Providers tab, as shown below:

\- Home \> Summary of Security Realms \> myrealm \> Providers \> Authentication tab

4.  Confirm absence of the KaajeeManageableAuthenticator.
    1.  When returned to the Authentication page, select and edit the DefaultAuthenticator Authentication Provider. Ensure that Control Flag is 'REQUIRED'.
5.  Restart the admin server, if any changes to the Authentication Providers has been made.
6.  Verify all Changes Have Taken Place:
    1.  Use the WebLogic console software (i.e., WebLogic Server 10.3.6 Console Login) to navigate to the following locations:
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Users tab)
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Groups tab)
    - Confirm absense of application-level users retrieved by the KaajeeManageableAuthenticator

KAAJEE SSPI 1.2 re-install

### Re-Deploy SSPI 1.2 Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install the KAAJEE SSPIs on the WebLogic server, perform the following procedures:

#### Download/Obtain SSPI Software

Download the kaajee_security_provider_1.1.0.xxx.zip software from the EVS anonymous directories.

#### Create SSPI Staging Area on the Application Server

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/026.png) | UPGRADES: Skip this step if you have already created an SSPI staging area on the WebLogic Application Server. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|

Create a KAAJEE SSPI staging directory under the WebLogic Application Server:

> \<SSPI_STAGING_FOLDER\>

#### Load/Install the SSPI Software on the Application Server

Extract all files/folders contained inside the \<SSPI_STAGING_FOLDER\> staging directory.

After unzipping/exploding the kaajee_security_provider_1.1.0.xxx.zip file in the \<SSPI_STAGING_FOLDER\> directory, you will see the following contents/folder structure:

<span id="OLE_LINK26" class="anchor"></span>

Table ‑. kaajee-1.1.0.xxx—KAAJEE folder structure

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Folder/Structure</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>..\kaajee_security_provider</td>
<td><blockquote>
<p>This folder is the KAAJEE SSPI &lt;root&gt; level. This folder contains the following files:</p>
</blockquote>
<ul>
<li><blockquote>
<p>build.xml—KAAJEE SSPI Ant build script.</p>
</blockquote></li>
<li><blockquote>
<p>readme.txt—KAAJEE SSPI documentation (manual), which includes an introduction, change history, any special installation instructions, and any known issues/limitations.</p>
</blockquote></li>
<li><blockquote>
<p>wlKaajeeSecurityProviders-1.1.0.xxx.jar—The KAAJEE SSPI software deployment jar file.</p>
</blockquote></li>
<li><blockquote>
<p>wlKaajeeSecurityProviders-1.1.0.xxx.jar.MD5—The MD5 checksum value for the KAAJEE SSPI software deployment jar file.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>..\common_pool_jars</td>
<td><blockquote>
<p>This folder contains the following files:</p>
</blockquote>
<ul>
<li><blockquote>
<p>commons-collections-3.1.jar</p>
</blockquote></li>
<li><blockquote>
<p>commons-dbcp-1.2.1.jar</p>
</blockquote></li>
<li><blockquote>
<p>commons-pool-1.2.jar</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>..\props</td>
<td><blockquote>
<p>This properties folder contains the following files:</p>
</blockquote>
<ul>
<li><blockquote>
<p>KaajeeDatabase.properties</p>
</blockquote></li>
<li><blockquote>
<p>KaajeeManageableAuthenticator.xml</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>..\sql</td>
<td><blockquote>
<p>This folder contains the SQL scripts for the following databases:</p>
</blockquote>
<ul>
<li><blockquote>
<p>CacheTables.sql</p>
</blockquote></li>
<li><blockquote>
<p>OracleTables.sql</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>..\src</td>
<td><blockquote>
<p>This folder contains the KAAJEE SSPI Java source code (i.e., the application server software).</p>
</blockquote></td>
</tr>
</tbody>
</table>

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/027.png) | BEGIN: Linux Instructions |
|---------------------------------------------------|-------------------------------|

Use the "jar" command to decompress the kaajee_security_provider_1.1.0.xxx.zip distribution file in the \<SSPI_STAGING_FOLDER\> staging directory:

> (REDACTED)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/028.png) | END: Linux Instructions |
|---------------------------------------------------|-----------------------------|

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/029.png) | Linux users, skip to 2.2.1.4. |
|---------------------------------------------------|-------------------------------|

|     | BEGIN: Microsoft Windows Instructions |
|-----|-------------------------------------------|

Unzip the kaajee_security_provider_1.1.0.xxx.zip distribution file in the \<SSPI_STAGING_FOLDER\> staging directory.

|     | END: Microsoft Windows Instructions |
|-----|-----------------------------------------|

#### Configure the SSPI Software on the Application Server

Configure the SSPI software on the WebLogic 9.2 and higher Application Servers, in both the Admin and Managed Servers.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/030.png) | Shut down the WebLogic Admin and Managed Servers. Shutting down the servers ensures that the domain servers will refresh their configuration values, etc. upon startup and that the new configuration changes take effect. |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/031.png) | BEGIN: Linux Instructions |
|---------------------------------------------------|-------------------------------|

#### (Linux: Admin Server) Modify the Startup Script

For Linux, the setDomainEnv.sh startup script needs to be modified in order for the classes contained in the SSPI, Apache connection pool jar files, and third party jar files to be found at run-time. This script is located in the following directory:

(REDACTED)

For example:

(REDACTED)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/032.png) | NOTE: In the examples that follow, some of the directory paths are represented by their \<Alias\>, as described in Error! Reference source not found.. You can copy and paste these examples for your own use but *must* substitute the \<Alias\> placeholder with the directory information specific to your workstation. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Add SSPI Jar File to the SSPI Classpath

The KAAJEE SSPI jar file is named as follows (“xxx” is a placeholder for the build number which varies):

- wlKaajeeSecurityProviders-1.1.0.xxx.jar

This file is located in the following directory:

(REDACTED)

#### Add Apache Connection Pool Jar Files to the SSPI Classpath

The Apache connection pool jar files listed below are located in the directory named (REDACTED)

- commons-collections-3.1.jar
- commons-dbcp-1.2.1.jar
- commons-pool-1.2.jar

These files *must* be added to the SSPI classpath.

#### Edit the setDomainEnv.sh file – Create KAAJEE variables

Edit the setDomainEnv.sh file to include the classpath to the three files listed in the section above "Add Apache Connection Pool Jar Files to the SSPI Classpath," instructed as follows:

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/033.png) | NOTE: Only the sections of setDomainEnv.sh script pertinent to demarcating file updates are displayed below. |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|

Immediately following the standard “ADD EXTENSIONS TO CLASSPATHS” comment statement in the standard generated setDomainEnv script below,

\# ADD EXTENSIONS TO CLASSPATHS

Add the following lines of code (Figure 2‑2):

<span id="_Ref193196349" class="anchor"></span>Figure ‑. Linux Admin Server—KAAJEE SSPI classpath additions to the setDomainEnv.sh file  
(*Generic* example *with* \<Alias\> placeholders)

\# ADD EXTENSIONS TO CLASSPATHS

\# Create KAAJEE variables (REDACTED)

For the following example, we substituted the \<Alias\> placeholder as shown below:

(REDACTED)

<span id="_Toc63681299" class="anchor"></span>Figure ‑. Linux Admin Server—KAAJEE SSPI classpath additions to the setDomainEnv.sh file  
(*Alias placeholders resolved with actual path names.*)

\# ADD EXTENSIONS TO CLASSPATHS

\# Create KAAJEE variables (REDACTED)

#### Add Variables to the PRE_CLASSPATH

Add the following variables (that you created in the previous steps) to the script’s PRE_CLASSPATH variable:

- propertiesdir (this directory points to the KaajeeDatabase.properties file)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/034.png) | NOTE: For more information on the KaajeeDatabase.properties file, please refer to the "Error! Reference source not found." topic in this chapter. |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

- sspidir (this directory points to the location where you decompressed the SSPI software.)
- sspijar (this includes the directory path listed in sspidir above plus the SSPI JAR file: wlKaajeeSecurityProviders-1.1.0.xxx.jar)
- commonpool
- commondbcp
- commoncollection

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/035.png)</th>
<th><p><strong>NOTE:</strong> KAAJEE allows users to locate the file(s) pointed to by the propertiesdir and sspidir as follows:</p>
<ul>
<li><blockquote>
<p>Co-located together in the same directory—Only one classpath is required.</p>
</blockquote></li>
<li><blockquote>
<p>Located in separate directories—Two separate classpaths are required.</p>
</blockquote></li>
</ul>
<p>For these examples, the propertiesdir and sspidir classpaths are listed separately because they are located in separate directories.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Edit PRE_CLASSPATH

In the setDomainEnv.sh script, immediately after the “ADD EXTENSIONS TO CLASSPATHS” comment, and following the KAAJEE-specific variables that you set up in the preceding steps, append the following KAAJEE-specific items to the PRE_CLASSPATH variable:

\# ADD EXTENSIONS TO CLASSPATHS

\# Create KAAJEE variables (REDACTED)

If you've already installed VistALink V 1.6, you may already have an addition to the PRE_CLASSPATH containing the directory location where the VistALink connectorConfig.xml file resides.

#### Add the sspidir Argument

Add the following sspidir argument:

> -Dweblogic.alternateTypesDirectory=\${sspidir}

This Java Virtual Machine (JVM) argument is significant because it allows WebLogic to find the appropriate directory where the custom SSPIs are located. Otherwise, WebLogic assumes that the custom SSPIs are located in the mbeantypes directory (e.g. (REDACTED)). Classpaths are used by the Health*<u>e</u>*Vet-VistA applications.

Somewhere AFTER the script lines setting the KAAJEE variables in the setDomainEnv.sh script (but before the final “export JAVA_OPTIONS” statement in the script), add the following lines of code:

\# for KAAJEE (REDACTED)

SetDomainEnv.sh Script Changes Summary

After completing the previous steps, the complete section of modified script should look similar to the following:

\# ADD EXTENSIONS TO CLASSPATHS

\# Create KAAJEE variables

(REDACTED)

\# for KAAJEE

(REDACTED)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/036.png) | END: Linux Instructions |
|---------------------------------------------------|-----------------------------|

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/037.png) | Linux users, skip to 2.2.1.4.3. |
|---------------------------------------------------|---------------------------------|

|     | BEGIN: Microsoft Windows Instructions |
|-----|-------------------------------------------|

#### (Windows: Admin Server) Modify the setDomainEnv.cmd File

For Windows, the setDomainEnv.cmd file needs to be modified in order for the classes contained in the SSPI, Apache connection pool jar files, and third party jar files to be found at run-time. This file is located in the following directory:

(REDACTED)

For example:

(REDACTED)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/038.png) | NOTE: In the examples that follow, some of the directory paths are represented by their \<Alias\>, as described in Error! Reference source not found.. You can copy and paste these examples for your own use but *must* substitute the \<Alias\> placeholder with the directory information specific to your workstation. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Add SSPI Jar File to the SSPI Classpath

The KAAJEE SSPI jar file is named as follows (“xxx” is a placeholder for the build number which varies):

(REDACTED)

This file is located in the following directory:

> (REDACTED)

#### Add Apache Connection Pool Jar Files to the SSPI Classpath

The Apache connection pool jar files listed below are located in the directory named (REDACTED)

- commons-collections-3.1.jar
- commons-dbcp-1.2.1.jar
- commons-pool-1.2.jar

These files *must* be added to the SSPI classpath.

#### Edit the setDomainEnv.cmd file – Create KAAJEE variables

Edit the setDomainEnv.cmd file to include the classpath to the three files listed in the section above "Add Apache Connection Pool Jar Files to the SSPI Classpath," instructed as follows:

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/039.png) | NOTE: Only the sections of setDomainEnv.cmd script pertinent to demarcating file updates are displayed below. |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|

Immediately following the standard “ADD EXTENSIONS TO CLASSPATHS” comment statement in the standard generated setDomainEnv script below,

@REM ADD EXTENSIONS TO CLASSPATHS

Add the following lines of code(Figure 2‑4):

<span id="_Ref193200793" class="anchor"></span>Figure ‑. Windows Admin Server—KAAJEE SSPI classpath additions to the setDomainEnv.cmd file  
(*Generic* example *with* \<Alias\> placeholders)

@REM ADD EXTENSIONS TO CLASSPATHS

@REM Create KAAJEE variables

set ApacheConnPool=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider\common_pool_jars

set commonpool=%ApacheConnPool%\commons-pool-1.2.jar

set commondbcp=%ApacheConnPool%\commons-dbcp-1.2.1.jar

set commoncollection=%ApacheConnPool%\commons-collections-3.1.jar

set propertiesdir=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider\props

set sspidir=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider

set sspijar=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider\\ wlKaajeeSecurityProviders-1.1.0.xxx.jar

#### Add Variables to the PRE_CLASSPATH

Add the following variables (that you created in the previous steps) to the script’s PRE_CLASSPATH variable:

- propertiesdir (this directory points to the KaajeeDatabase.properties file)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/040.png) | NOTE: For more information on the KaajeeDatabase.properties file, please refer to the "Error! Reference source not found." topic in this chapter. |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

- sspidir (this directory points to the location where you unzipped the SSPI software.)
- sspijar (this includes the directory path listed in sspidir above plus the SSPI JAR file: wlKaajeeSecurityProviders-1.1.0.xxx.jar)
- commonpool
- commondbcp
- commoncollection

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/041.png)</th>
<th><p><strong>NOTE:</strong> KAAJEE allows users to locate the file(s) pointed to by the propertiesdir and sspidir as follows:</p>
<ul>
<li><blockquote>
<p>Co-located together in the same directory—Only one classpath is required.</p>
</blockquote></li>
<li><blockquote>
<p>Located in separate directories—Two separate classpaths are required.</p>
</blockquote></li>
</ul>
<p>For these examples, the propertiesdir and sspidir classpaths are listed separately because they are located in separate directories.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Edit PRE_CLASSPATH

In the setDomainEnv.cmd script, immediately following the “ADD EXTENSIONS TO CLASSPATHS” comment, and following the KAAJEE-specific variables that you set up in the preceding steps, append the following KAAJEE-specific items to the PRE_CLASSPATH variable:

@REM ADD EXTENSIONS TO CLASSPATHS

@REM Create KAAJEE variables

set ApacheConnPool=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider\common_pool_jars

set commonpool=%ApacheConnPool%\commons-pool-1.2.jar

set commondbcp=%ApacheConnPool%\commons-dbcp-1.2.1.jar

set commoncollection=%ApacheConnPool%\commons-collections-3.1.jar

set propertiesdir=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider\props

set sspidir=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider

set sspijar=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider\\ wlKaajeeSecurityProviders-1.1.0.xxx.jar

@REM Append KAAJEE items to PRE_CLASSPATH

set PRE_CLASSPATH=%PRE_CLASSPATH%;%propertiesdir%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%sspidir%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%sspijar%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%commonpool%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%commondbcp%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%commoncollection%

If you've already installed VistALink 1.6, you may already have an addition to the PRE_CLASSPATH variable containing the directory location where the VistALink connectorConfig.xml file resides.

#### Add the sspidir Argument

Add the following sspidir argument:

> -Dweblogic.alternateTypesDirectory=%sspidir%

This Java Virtual Machine (JVM) argument is significant because it allows WebLogic to find the appropriate directory where the custom SSPIs are located. Otherwise, WebLogic assumes that the custom SSPIs are located in the mbeantypes directory (e.g. (REDACTED)). Classpaths are used by the Health*<u>e</u>*Vet-VistA applications.

Somewhere AFTER the script lines setting the KAAJEE variables in the setDomainEnv.cmd script (but before the final “set JAVA_OPTIONS=%JAVA_OPTIONS%” statement in the script), add the following lines of code:

@REM for KAAJEE

set JAVA_OPTIONS=%JAVA_OPTIONS% -Dweblogic.alternateTypesDirectory=%sspidir%

#### SetDomainEnv.cmd Script Changes Summary

After completing the previous steps, the complete section of modified script should look similar to the following:

@REM ADD EXTENSIONS TO CLASSPATHS

@REM Create KAAJEE variables

set ApacheConnPool=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider\common_pool_jars

set commonpool=%ApacheConnPool%\commons-pool-1.2.jar

set commondbcp=%ApacheConnPool%\commons-dbcp-1.2.1.jar

set commoncollection=%ApacheConnPool%\commons-collections-3.1.jar

set propertiesdir=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider\props

set sspidir=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider

set sspijar=\<SSPI_STAGING_FOLDER\>\kaajee_security_provider\\ wlKaajeeSecurityProviders-1.1.0.xxx.jar

@REM Append KAAJEE items to PRE_CLASSPATH

set PRE_CLASSPATH=%PRE_CLASSPATH%;%propertiesdir%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%sspidir%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%sspijar%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%commonpool%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%commondbcp%

set PRE_CLASSPATH=%PRE_CLASSPATH%;%commoncollection%

@REM for KAAJEE

set JAVA_OPTIONS=%JAVA_OPTIONS% -Dweblogic.alternateTypesDirectory=%sspidir%

|     | END: Microsoft Windows Instructions |
|-----|-----------------------------------------|

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/042.png) | Windows users, skip to 2.2.1.4.4. |
|---------------------------------------------------|-----------------------------------|

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/043.png) | BEGIN: Linux Instructions |
|---------------------------------------------------|-------------------------------|

#### (Linux: Managed Servers) Modify the KAAJEE SSPI-related Classpath, Arguments, and Security Policy

Use the WebLogic Server Console to navigate to the Server Start tab on the Configuration tab to update the Managed Server(s) KAAJEE SSPI-related classpath and arguments.

Home \> Summary of Servers \> kjm92L_ManagedSvr1

<span id="_Toc63681301" class="anchor"></span>Figure ‑. WebLogic Server Administration Console: Managed Server Start tab settings

(REDACTED)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/044.png)</th>
<th><strong>NOTE:</strong> In the examples that follow, some of the directory paths are represented by their <strong>&lt;Alias</strong>&gt;, as described in <strong>Error! Reference source not found.</strong>. You can copy and paste these examples for your own use but <em>must</em> substitute the <strong>&lt;Alias&gt;</strong> placeholder with the directory information specific to your workstation.<br />
<br />
Users <em>must</em> repeat the following procedures for <em>each</em> Managed Server.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Add/Replace the KAAJEE SSPI Directories/Files to the Managed Server Classpath

Add or replace the following KAAJEE SSPI-related classpaths in the Class Path field (i.e., the classpath used to start the Managed Server) on the Server Start tab on the Managed Server(s):

- propertiesdir (this directory points to the KaajeeDatabase.properties file)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/045.png) | NOTE: For more information on the KaajeeDatabase.properties file, please refer to the "Error! Reference source not found." topic in this chapter. |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

- sspidir (this directory points to the location where you decompressed the SSPI software.)
- wlKaajeeSecurityProviders-1.1.0.xxx.jar(SSPI JAR file)
- commons-pool-1.2.jar (file)
- commons-dbcp-1.2.1.jar (file)
- commons-collections-3.1.jar (file)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/046.png)</th>
<th><p><strong>NOTE:</strong> KAAJEE allows users to locate the file(s) pointed to by the propertiesdir and sspidir as follows:</p>
<ul>
<li><blockquote>
<p>Co-located together in the same directory—Only one classpath is required.</p>
</blockquote></li>
<li><blockquote>
<p>Located in separate directories—Two separate classpaths are required.</p>
</blockquote></li>
</ul>
<p>For these examples, the propertiesdir and sspidir classpaths are listed separately because they are located in separate directories.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc63681302" class="anchor"></span>Figure ‑. Linux Managed Server—KAAJEE SSPI classpath additions on the Server Start tab  
(*Generic* example *with* \<Alias\> placeholders)

(REDACTED).

.

.

.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/047.png) | NOTE: Other VistALink- and WebLogic-specific classpaths will also be displayed in this field. |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

For the following example, we substituted the \<Alias\> placeholders with the values as shown below:

- \<JAVA_HOME\> = (REDACTED)
- \<BEA_HOME\> = (REDACTED)
- \<SSPI_STAGING_FOLDER\>= (REDACTED)
- \<MANAGED_SERVER_NAME\> = (REDACTED)
- \<BEA_STAGE\> = (REDACTED)

> (Staging area for applications, JCA Connectors, and configuration files)

<span id="_Toc63681303" class="anchor"></span>Figure ‑. Linux Managed Server—KAAJEE SSPI classpath additions/replacements on the Server Start tab  
(*Actual* example *without* \<Alias\> placeholders)

(REDACTED).

.

.

.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/048.png) | NOTE: Other VistALink- and WebLogic-specific classpaths will also be displayed in this field. |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

#### Add/Replace the KAAJEE SSPI-related Arguments on the Managed Server(s)

Add or replace the following KAAJEE SSPI-related arguments on the Managed Server(s):

(REDACTED)

The KAAJEE SSPI-related arguments are added/replaced in the Arguments field (i.e., the arguments used to start the Managed Server) on the Server Start tab on the Managed Server(s). The arguments are added or replaced in one long string, as shown below:

<span id="_Toc63681304" class="anchor"></span>Figure ‑. Linux Managed Server—KAAJEE SSPI argument additions/replacements on the Server Start tab  
(*Generic* example *with* \<Alias\> placeholders)

(REDACTED)

For the following example, we substituted the \<Alias\> placeholders as shown below:

(REDACTED)

<span id="_Toc63681305" class="anchor"></span>Figure ‑. Linux Managed Server—KAAJEE SSPI argument additions/replacements on the Server Start tab  
(*Actual* example *without* \<Alias\> placeholders)

(REDACTED)

#### Add/Replace the KAAJEE SSPI-related Security Policy File Reference

Add or replace the following KAAJEE SSPI-related security policy (permissions) file reference in the Security Policy File field (i.e., the security policy file used to start the Managed Server) on the Server Start tab on the Managed Server(s):

<span id="_Toc63681306" class="anchor"></span>Figure ‑. Linux Managed Server—KAAJEE SSPI Security Policy File field addition/replacement on the Server Start tab  
(*Generic* example *with* \<Alias\> placeholders)

(REDACTED)

For the following example, we substituted the \<Alias\> placeholder as shown below:

(REDACTED)

<span id="_Toc63681307" class="anchor"></span>Figure ‑. Linux Managed Server—KAAJEE SSPI Security Policy File field addition/replacement on the Server Start tab  
(*Actual* example *without* \<Alias\> placeholders)

(REDACTED)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/049.png) | END: Linux Instructions |
|---------------------------------------------------|-----------------------------|

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/050.png) | Linux users, skip to Error! Reference source not found.. |
|---------------------------------------------------|--------------------------------------------------------------|

|     | BEGIN: Microsoft Windows Instructions |
|-----|-------------------------------------------|

#### (Windows: Managed Servers) Modify the KAAJEE SSPI-related Classpath, Arguments, and Security Policy File

Use the WebLogic Server Console to navigate to the Server Start tab on the Configuration tab to update the Managed Server(s) KAAJEE SSPI-related classpath and arguments.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/051.png)</th>
<th><strong>NOTE:</strong> In the examples that follow, some of the directory paths are represented by their <strong>&lt;Alias&gt;</strong>, as described in <strong>Error! Reference source not found.</strong>. You can copy and paste these examples for your own use but <em>must</em> substitute the <strong>&lt;Alias&gt;</strong> placeholder with the directory information specific to your workstation.<br />
<br />
You <em>must</em> repeat the following procedures for <em>each</em> Managed Server.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Add/Replace the KAAJEE SSPI Directories/Files to the Managed Server Classpath

Add or replace the following KAAJEE SSPI-related classpaths in the Class Path field (i.e., the classpath used to start the Managed Server) on the Server Start tab on the Managed Server(s):

- propertiesdir (this directory points to the KaajeeDatabase.properties file)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/052.png) | NOTE: For more information on the KaajeeDatabase.properties file, please refer to the "Error! Reference source not found." topic in this chapter. |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

- sspidir (this directory points to the location where you unzipped the SSPI software.)
- wlKaajeeSecurityProviders-1.1.0.xxx.jar(SSPI JAR file)
- commons-pool-1.2.jar (file)
- commons-dbcp-1.2.1.jar (file)
- commons-collections-3.1.jar (file)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th>![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/053.png)</th>
<th><p><strong>NOTE:</strong> KAAJEE allows users to locate the file(s) pointed to by the propertiesdir and sspidir as follows:</p>
<ul>
<li><blockquote>
<p>Co-located together in the same directory—Only one classpath is required.</p>
</blockquote></li>
<li><blockquote>
<p>Located in separate directories—Two separate classpaths are required.</p>
</blockquote></li>
</ul>
<p>For these examples, the propertiesdir and sspidir classpaths are listed separately because they are located in separate directories.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc63681308" class="anchor"></span>Figure ‑. Windows Managed Server—KAAJEE SSPI classpath additions/replacements on the Server Start tab  
(*Generic* example *with* \<Alias\> placeholders)

(REDACTED).

.

.

.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/054.png) | NOTE: Other VistALink- and WebLogic-specific classpaths will also be displayed in this field. |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

For the following example, we substituted the \<Alias\> placeholders as shown below:

(REDACTED)

<span id="_Toc63681309" class="anchor"></span>Figure ‑. Windows Managed Server—KAAJEE SSPI classpath additions/replacements on the Server Start tab (Actual example without \<Alias\> placeholders)

(REDACTED).

.

.

.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/055.png) | NOTE: Other VistALink- and WebLogic-specific classpaths will also be displayed in this field. |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

#### Add/Replace the KAAJEE SSPI-related Arguments on the Managed Server(s)

Add or replace the following KAAJEE SSPI-related arguments on the Managed Server(s):

(REDACTED)

The KAAJEE SSPI-related arguments are added/replaced in the Arguments field (i.e., the arguments used to start the Managed Server) on the Server Start tab on the Managed Server(s). The arguments are added or replaced in one long string, as shown below:

<span id="_Toc63681310" class="anchor"></span>Figure ‑. Windows Managed Server—KAAJEE SSPI argument additions/replacements on the Server Start tab (*Generic* example *with* \<Alias\> placeholders)

For the following example, we substituted the \<Alias\> placeholders as shown below:

(REDACTED)

<span id="_Toc63681311" class="anchor"></span>Figure ‑. Windows Managed Server—KAAJEE SSPI argument additions/replacements on the Server Start tab (*Actual* example *without* \<Alias\> placeholders)

> (REDACTED)

#### Add/Replace the KAAJEE SSPI-related Security Policy File Reference

Add or replace the following KAAJEE SSPI-related security policy (permissions) file reference in the Security Policy File field (i.e., the security policy file used to start the Managed Server) on the Server Start tab on the Managed Server(s):

<span id="_Toc63681312" class="anchor"></span>Figure ‑. Windows Managed Server—KAAJEE SSPI Security Policy File field addition/replacement on the Server Start tab (*Generic* example *with* \<Alias\> placeholders)

(REDACTED)

For the following example, we substituted the \<Alias\> placeholder as shown below:

(REDACTED)

<span id="_Toc63681313" class="anchor"></span>Figure ‑. Windows Managed Server—KAAJEE SSPI Security Policy File field addition/replacement on the Server Start tab (*Actual* example *without* \<Alias\> placeholders)

(REDACTED)

|     | END: Microsoft Windows Instructions |
|-----|-----------------------------------------|

## Undeploy SSPI 1.2 and before

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/056.png) | FIRST-TIME INSTALLATIONS: Skip this step if you have *never* deployed KAAJEE SSPIs on the WebLogic Application Server. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/057.png) | UPGRADES: You *must* perform this step if you have previously deployed KAAJEE SSPIs on the WebLogic Application Server and will be installing a newer version of the KAAJEE SSPIs. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Before installing any new version of the KAAJEE SSPIs on the WebLogic server, users *must* remove any previously installed KAAJEE SSPIs. To do this, perform the following procedures:

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/058.png) | NOTE: Before starting, users should shut down all Managed Servers running on the WebLogic Application Server. Shutting down the server ensures that the domain server will refresh its configuration values, etc. upon startup and that the new configuration changes take effect. |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Delete kaajeeManageableAuthenticator

On the WebLogic Admin Server, use the console to navigate to the following directory:

Home \> Summary of Security Realms \> myrealm \> Providers

Delete kaajeeManageableAuthenticator. Confirm the delete when prompted.

#### Modify DefaultAuthenticator Control Flag

In the same directory, select DefaultAuthenticator. Use the dropdown box next to the Control Flag field to change the setting to REQUIRED and then click Save.

#### Shut Down the Admin Server on the Application Server

Users should shut down the Admin Server running on the WebLogic Application Server. Shutting down the server ensures that the domain server will refresh its configuration values, etc. upon startup and that the new configuration changes take effect.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/059.png) | BEGIN: Linux Instructions |
|---------------------------------------------------|-------------------------------|

#### (Linux: Admin Server) Edit the startWebLogic.sh File

> On the application server, users need to edit the startWebLogic.sh file. This file is located in the following directory:

> (REDACTED)

> For example:

> (REDACTED)

> In the startWebLogic.sh file, delete the following argument:

> (REDACTED)

> Save and close the file.

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/060.png) | END: Linux Instructions |
|---------------------------------------------------|-----------------------------|

| ![](kaajee-sspi-installation-guide-1-3-weblogic-10-3-6-and-higher/061.png) | Linux users, skip to 0. |
|---------------------------------------------------|-------------------------|

|     | BEGIN: Microsoft Windows Instructions |
|-----|-------------------------------------------|

#### (Windows: Admin Server) Edit the startWebLogic.cmd File

On the application server, users need to edit the startWebLogic.cmd file. This file is located in the following directory:

(REDACTED)

For example:

(REDACTED)

In the startWebLogic.cmd file, delete the following argument:

(REDACTED)

Save and close the file.

|     | END: Microsoft Windows Instructions |
|-----|-----------------------------------------|

#### Start the Admin Server on the Application Server

Users should start the Admin Server on the WebLogic Application Server and then log into the WebLogic Console.

#### Verify Removal of the kaajeeManageableAuthenticator

Users should navigate to the following directory:

Home \> Summary of Security Realms \> myrealm \> Providers

Verify that the kaajeeManageableAuthenticator is no longer listed.

#### Shut Down the Admin Server on the Application Server

Users should shut down the Admin Server running on the WebLogic Application Server. Shutting down the server ensures that the domain server will refresh its configuration values, etc. upon startup and that the new configuration changes take effect.

#### Move and Back Up the wlKaajeeSecurityProviders-1.2.0.xxx.jar File

On the application server, users should navigate to the \<SSPI_STAGING_FOLDER\> staging directory. To complete the cleanup and create a backup, locate and move the wlKaajeeSecurityProviders-1.2.0.xxx.jar file to a backup directory.

#### KAAJEE SSPI Successfully Undeployed

*This page is left blank intentionally.*

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: KAAJEE SSPI 8.0.781 Installation Guide (WebLogic 12.2)

### UPGRADE and continuing the FIRST-TIME Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Edit the createDSSSPI.properties file with information pertaining to your environment:

> There are several property values to edit. Pay special attention to the case and whitespace.

> The ds.name and the ds.jndi.name should be left unchanged. The rest of the datasource information gets copied from the existing KaajeeDatabase.properties file (for upgrades).

> ![](kaajee-sspi-8-0-781-installation-guide-weblogic-12-2/021.png)

#### Locate and Run the setWLSEnv.sh script on the application server Ex(12.2):

![](kaajee-sspi-8-0-781-installation-guide-weblogic-12-2/022.png)

> The file is located under the server/bin directory by default (Ex: /u01/app/oracle/weblogic-server-12.2.1.4/wlserver/server/bin/setWLSEnv.sh for the 12.2 version of application server)

#### Run the java weblogic.WLST and pass the required properties file to the createDSSSPI.py

> java weblogic.WLST createDSSSPI.py -p createDSSSPI.properties

#### The script will attempt to create a new datasource, wire it up to a database and instantiate an instance of SQLAuthenticationProvider. Upon successful script completion, you will be asked to shutdown an admin server. Type “Y” to agree.

1.  Start the server; Log onto admin console.
1.  Navigate to the Authentication Directory:
    1.  Select Security Realms under Domain Structure.
    2.  Navigate to the Providers tab, as shown below:

\- Home \> Summary of Security Realms \> myrealm \> Providers

3.  Click on New in the Authentication tab
2.  Find the KaajeeManageableAuthenticator, ensure Control Flag is set to 'OPTIONAL'.
    1.  When returned to the Authentication page, select the DefaultAuthenticator Authentication Provider.
    2.  Ensure that Control Flag is 'SUFFICIENT'.

> ![](kaajee-sspi-8-0-781-installation-guide-weblogic-12-2/023.png)

3.  Restart the admin server, if any changes to the Authentication Providers has been made.
3.  Verify all Changes Have Taken Place:
    1.  Use the WebLogic console software (i.e., WebLogic Server 10.3.6 Console Login) to navigate to the following locations:
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Users tab)
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Groups tab)

|                                                                                                                |                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-sspi-8-0-781-installation-guide-weblogic-12-2/024.png) | NOTE: If this is a first-time install, you will not see users populated in the Oracle tables or in the WebLogic console. |
|                                                                                                                |                                                                                                                              |

2.  Confirm presence of application-level users retrieved by the KaajeeManageableAuthenticator –

> ![](kaajee-sspi-8-0-781-installation-guide-weblogic-12-2/025.png)

## KAAJEE SSPI rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate and Run the setWLSEnv.sh script on the application server

![](kaajee-sspi-8-0-781-installation-guide-weblogic-12-2/026.png)

> The file is located under the server/bin directory by default (Ex: /u01/app/oracle/weblogic-server-12.2.1.4/wlserver/server/bin/setWLSEnv.sh)

#### Run the java weblogic.WLST and pass the required properties file to the deleteDSSSPI.py

> java weblogic.WLST deleteDSSSPI.py -p createDSSSPI.properties

#### The script will attempt to remove a datasource as well as the SQLAuthenticationProvider. It will use the same properties file. Upon successful script completion, you will be offered to shutdown an admin server. 

2.  Start the server; Log onto admin console.
3.  Navigate to the Authentication Directory:
    1.  Select Security Realms under Domain Structure.
    2.  Navigate to the Providers tab, as shown below:

\- Home \> Summary of Security Realms \> myrealm \> Providers \> Authentication tab

4.  Confirm absence of the KaajeeManageableAuthenticator.
    1.  When returned to the Authentication page, select and edit the DefaultAuthenticator Authentication Provider. Ensure that Control Flag is 'REQUIRED'.
5.  Restart the admin server, if any changes to the Authentication Providers has been made.
6.  Verify all Changes Have Taken Place:
    1.  Use the WebLogic console software (i.e., WebLogic Server 10.3.6 Console Login) to navigate to the following locations:
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Users tab)
        - Home \> Summary of Security Realms \> myrealm \> Users and Groups  
          > (Groups tab)
    - Confirm absence of application-level users retrieved by the KaajeeManageableAuthenticator

*This page is left blank intentionally.*
