---
consolidated_title: "numi server setup guide"
app_code: NUMI
doc_type: base-setup
master_source: "NUMI Server Setup Guide Version 15.09"
master_pub_date: August 2021
consolidated_from: 5 versions
prior_versions:
  - "NUMI Server Setup Guide Version 15.10"
  - "NUMI Server Setup Guide Version 15.14"
  - "NUMI Server Setup Guide Version 15.15"
  - "NUMI Server Setup Guide"
---

**National Utilization Management Integration (NUMI)**

**Server Setup Guide**

**Release 1.1.15.9.1**

<!-- image -->

**Department of Veterans Affairs**

**August 2021**

# Revision History

| Date       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Author   |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 04/22/2009 | Submitted to Medora Team for                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED |
| 07/14/2009 | Updated to reflect “Release 1.1”                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED |
| 08/28/2009 | Updated document name to                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | REDACTED |
| 08/01/2011 | Updated per issues found in AITC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | REDACTED |
| 08/02/2011 | Updated section 9.9 per AITC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED |
| 08/04/2011 | Refined CERME instructions in section 6 per AITC Windows SA                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | REDACTED |
| 08/24/2011 | Refined MDWS instructions in section 6.12-6.15 per AITC                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED |
| 10/13/2011 | Updated CERME instructions in                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED |
| 04/10/2012 | Draft preliminary update for                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED |
| 07/03/2012 | Added figures to section 6.13;  Added captions to figures throughout; replaced example in section 6.12, step #10; added new section 6.14; updated cover and footers to “Release 14” per VA PM                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED |
| 01/03/2013 | Added section 6.12; updated  section 6.13 with new Fig. 19, corrected Section 6.14, Windows Event Log and updated SSL setup and config; updated 6.19 per Operational feedback; added Appendix F NUMI Exchange                                                                                                                                                                                                                                                                                                                                                                    | REDACTED |
| 03/25/2013 | Modified section 6.15 for NUMI event folder, modified section 6.19                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED |
| 3/29/2013  | Removed original highlighting and  updated per customer feedback: changed Section 2.2 Web Server (Server 2) to reference NUMI Exchange and MDWS; updated  Section 3.1 Disk Space and Devices; updated Section 5.1 to reference test environments and removed Section 5.6, Installation During Off Peak Hours. Also reordered installation steps SQL and CERMe (now section  6.1 and 6.14) and added CERMe SSL                                                                                                                                                                    | REDACTED |
| 5/13/2013  | Corrected release referenced in  section 1, removed content for Windows Server 2003 and IIS 6 setup, added content for Windows Server 2008 and IIS 7 setup, added content for MDWS 2.Xinstallation, re-organized document content.                                                                                                                                                                                                                                                                                                                                               | REDACTED |
| 5/24/2013  | Made the following corrections  per VA comments: Changed section  2.2.1 to specify SQL Server 2005, changed figures 37,  38, 39 to reflect MDWS1.2, added MDWS config information to section 6.11.3 (MDWS1.2) and  6.12.4 (MDWS2.x), added execution timeout setting for the synchronizer in section 6.18.1, step 4.                                                                                                                                                                                                                                                             | REDACTED |
| 6/17/2013  | Made the following corrections per VA comments: Changed section 2.2.1 to clarify restoring from a NUMI backup database and added replication comments, updated 3.1.3 with CPU capacity details, updated section 3.1.4 with disk space details;  changed section 5 to clarify restoring from a NUMI backup database, updated section 5.1 added synchronizer and user account information, removed original item 3, updated section 6.7 to specify version and recovery mode, updated section 6.8 removed Medora information, updated section 6.19 to add more script information. | REDACTED |
| 6/27/2013  | Updated to version number to 14.1 changed sections 2.2.1 and 5. To include 14.0 and 14.1 database information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED |
| 7/2/2013   | Changed example directory references to remove 14.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED |
| 8/2/2013   | Removed references to CERMe 2012.  Changed hard coded build name directory references to  &lt;install\_dir&gt;.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | REDACTED |
| 8/20/2013  | Added version number for MDWS in section 2.2.2, added version number for CERME in section 2.2.3, added RAM to section 3.1.3, updated Figure 68, removed MDWS 1.2 section 6.11, renamed MDWS 2.x to MDWS 2.7.3.2 in section 6.12,  renamed section 6.12 to 6.11                                                                                                                                                                                                                                                                                                                   | REDACTED |
| 5/11/2015  | Updated the version number from 14.1 to 14.2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED |
| 11/12/2015 | Updated the version number from 14.2 to 14.3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | REDACTED |
| 09/12/2016 | Updating document for NUMI 14.4 and .NET version. Made the Windows version generic                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED |
| 9/20/2016  | Updated install instructions for 15.0 and updated CERMe installation instructions and IIS and File service installation screenshots                                                                                                                                                                                                                                                                                                                                                                                                                                              | REDACTED |
| 2/3/2017   | Added steps to encrypt the configuration files                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | REDACTED |
| 3/1/2017   | Updates for IAM SSO integration changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED |
| 3/27/2017  | Added CA WebAgent setup instructions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED |
| 5/25/2017  | Reviewed document and revised                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | REDACTED |
| 11/14/2017 | Updated release version number (version 15.4) and CERME upgrade installation steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED |
| 04/23/2018 | Update release version number (15.5)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | REDACTED |
| 10/1/2018  | Updated release version number (15.6)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED |
| 02/19/2018 | Updated release version number (15.7) and new Synchronizer installation instructions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED |
| 08/28/2019 | Updated release version number and added STS integration information (Section 13).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | REDACTED |
| 2/1/2020   | Updated release version number (15.9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED |
| 5/28/2020  | Updated CERMe RM and InterQual View version (19.0/2020)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | REDACTED |
| 8/16/2021  | Updated CERMe RM 20.0 and InterQual View version 2021                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | REDACTED |

# Table of Contents

1.	Introduction	1

1.1.	Purpose	1

1.2.	Scope	1

1.3.	Target Audience	1

2.	Deployment Overview	1

2.1.	National Deployment Request	1

2.2.	Installing NUMI on the Servers	1

2.2.1.	Database Server	1

2.2.2.	Web Server	2

2.2.3.	Application Server	2

3.	Pre-Installation Instructions and Preparation	2

3.1.	Installation Process Requirements	2

3.1.1.	Minimum Software Version	2

3.1.2.	Resources Required	3

3.1.3.	CPU Capacity	3

3.1.4.	Disk Space	3

3.1.5.	Devices (Servers, etc.)	3

3.1.6.	VistA Rights Needed for NUMI Users	3

3.2.	Install Software in Test Environments	4

3.3.	Generate Pre-Installation Reports	4

3.4.	Coordinate Installation with Other Teams	4

3.5.	Install Sequence Information for Multiple Patches	4

3.6.	Logoff During Installation	4

3.7.	Average Amount of Time Required to Complete the Installation	4

4.	Database Information	5

4.1.	Instructions for Installing Database Components	5

4.1.1.	Database Installation / Restoration Procedures	5

5.	Installation Procedure for Server 2019	5

5.1.	Patch the Operating System	5

6.	SQL Server Setup (Windows Server 2019)	6

6.1.	Role Setup	6

7.	Web Server Setup (Windows Server 2019)	6

7.1.	Role Setup	6

7.2.	ASP.NET 2.0 AJAX Extensions 1.0 Setup	9

7.3.	MS Web Services Enhancements (WSE) 3.0 Setup	9

8.	Application Server Setup (Windows Server 2019)	9

8.1.	Role Setup	9

8.2.	Feature Delegation	11

8.3.	Install MS ASP.Net 2.0 AJAX Extensions 1.0	12

8.4.	Install MS Web Services Enhancements 3.0	16

9.	Install SQL Server	19

9.1.	Download all SQL Server Patches	20

9.2.	Restore the Appropriate Databases for the NUMI Application	20

10.	Installing NUMI Exchange on Server 2019	20

10.1.	Unzip/Install NUMI Exchange Distribution	20

10.2.	NUMI Exchange Website Configuration	20

10.2.1.	Application Pool Configuration	24

11.	Installing NUMI on Server 2019	27

11.1.	Software Copy Instructions	27

11.2.	NUMI Web Site Configuration	27

11.3.	Application Pool Configuration	33

12.	Install CA SiteMinder Web Agent for Single Sign On (SSO) on the Web server	37

12.1.	Agent location	37

12.2.	Agent installation	37

12.3.	Agent configuration	41

12.3.1.	Configuring for the first time	42

12.3.2.	Reconfiguration configuration	48

13.	Secure Token Service Integration for SSOi	54

13.1.	Download Certificate Chain from appropriate endpoint	54

13.2.	Export server cert to .pfx	59

2.	Find the server cert in the personal folder	59

3.	Right click and export the certificate	59

4.	Select “Yes, export private key” and choose next	60

5.	Select “Export all extended properties” and choose next	60

6.	Select a strong password.  This password will go into NumiWebApp.config later in this guide.	61

7.	Select a filename for the exported certificate and save it as a .pfx.  Select a folder not specific to a version of NUMI as this cert will be valid for future versions of the applications until expiration.  For example, if the folder structure for website is NUMI/NUMI\_15.9 select the /NUMI folder for the cert and not the specific /NUMI\_15.9 folder.  This file path will go into NumiWebApp.config later in this guide.	61

13.3.	NumiWebApp.config keys	61

14.	Installing CERMe Software and Database from CERMe Installation CD	61

14.1.	Install CERMe on the Application Server	62

14.2.	Install CERMe SSL Certificate	64

15.	Setting up NUMI Section in the Windows Event Log	68

15.1.	Validate XML Configuration File Settings	69

16.	Perform Restart	71

17.	Test NUMI Web Site Functionality	71

18.	Installing NUMI Synchronizer on the DB Server	71

18.1.	Installation Instructions	71

18.2.	Uninstall:	74

18.3.	Validate Installation:	74

18.4.	Add Jobs to the SQL Server	74

19.	Post-Installation Considerations	75

20.	Acronyms and Descriptions	76

21.	Numi Comparison Table	77

# List of Tables

Table 1: CPRS Rights	4

Table 2: CPRS Access Tabs	4

Table 3: IAM Host Configuration Object	43

Table 4: SiteMinder Policy Server IP Address	44

Table 5: SSOLogoutUri values	70

# List of Figures

Figure 1: SQL Server Role Services	6

Figure 2: NUMI Exchange Role Services	7

Figure 3: NUMI Exchange (IIS)	8

Figure 4: NUMI Role Services	9

Figure 5: NUMI Web Services IIS	10

Figure 6: IIS Feature Delegation	11

Figure 7: Feature Delegation Selection	12

Figure 8: MS ASP.Net 2.0 File Download-Security Warning Window	13

Figure 9: MS ASP.Net 2.0 Internet Explorer-Security Warning Window	13

Figure 10: MS ASP.NET 2.0 AJAX Extensions 1.0 Setup Wizard Window	14

Figure 11: MS ASP.NET 2.0 AJAX License Agreement Window	14

Figure 12: MS ASP.NET 2.0 AJAX Installation Window	15

Figure 13: MS ASP.NET 2.0 AJAX Completion window	16

Figure 14: MS WSE 3.0 File Download-Security Warning Window	16

Figure 15: MS WSE 3.0 Internet Explorer-Security Warning Window	17

Figure 16: MS WSE 3.0 InstallShield Wizard Welcome Window	17

Figure 17: MS WSE 3.0 License Agreement Window	18

Figure 18: MS WSE 3.0 InstallShield Wizard Window	18

Figure 19: MS WSE 3.0 Installation Window	19

Figure 20: MS WSE 3.0 Completion Window	19

Figure 21: Add NUMI Exchange Website	21

Figure 22: NUMI Exchange Website	21

Figure 23: NUMI Exchange Basic Settings	22

Figure 24: NUMI Advanced Settings	22

Figure 25: NUMI Exchange Bindings	23

Figure 26: NUMI Exchange Authentication Settings	23

Figure 27: NUMI Exchange SSL Settings	24

Figure 28: Application Pool Window	24

Figure 29: NUMI Exchange Application Pool Basic Settings	25

Figure 30: NUMI Exchange Pool Advanced Settings	26

Figure 31: Unblocking Restricted Files in Installation ZIP File	27

Figure 32: Add NUMI Website	28

Figure 33: NUMI Basic Settings	29

Figure 34: NUMI Advanced Settings	30

Figure 35: NUMI Bindings	31

Figure 36: NUMI Authentication Settings	31

Figure 37: NUMI SSL Settings	32

Figure 38: NUMI Compression Settings	33

Figure 39: Application Pool Window	34

Figure 40: NUMI Application Pool Basic Settings	35

Figure 41: NUMI Application Pool Advanced Settings	36

Figure 42: Security Warning	37

Figure 43: Preparing to install dialog	38

Figure 44: Web agent install wizard - Welcome screen	38

Figure 45: Web agent install wizard - License agreement screen	39

Figure 46: Web agent install wizard - Install location screen	39

Figure 47: Web agent install wizard - Review screen	40

Figure 48: Web agent install wizard - Agent configuration screen	40

Figure 49: Web agent install wizard - Install complete screen	41

Figure 50: Launch Web Agent Configuration Wizard	41

Figure 51: Web agent configuration wizard - Host registration	42

Figure 52: Web agent configuration wizard - Admin credentials	43

Figure 53: Web agent configuration wizard - Host name and configuration object	44

Figure 54: Web agent configuration wizard - Policy server IP Address	45

Figure 55: Web agent configuration wizard - FIPS mode setting	45

Figure 56: Web agent configuration wizard - Configuration file location	46

Figure 57: Web agent configuration wizard - Web server	46

Figure 58: Web agent configuration wizard - Agent configuration	47

Figure 59: Web agent configuration wizard - Sites selection	47

Figure 60: Web agent configuration wizard - Summary screen	48

Figure 61: Web agent configuration wizard - Completion screen	48

Figure 62: Web agent configuration wizard - Host registration	49

Figure 63: Web agent configuration wizard - Web server	49

Figure 64: Web agent configuration wizard - Agent configuration	50

Figure 65: Web agent configuration wizard - Sites selection	51

Figure 66: Web agent configuration wizard - Summary screen	51

Figure 67: Web agent configuration wizard - Previously configured sites	52

Figure 68: Web agent configuration wizard - Summary screen	53

Figure 69: Web agent configuration wizard - Completion screen	53

Figure 70: IIS Server Certificates	65

Figure 71: IIS Server Certificate Selection	66

Figure 72: IIS Certificate Details	66

Figure 73: keytool -keystore "C:\Certs\CERME.ks" –list	67

Figure 74: Creating a NUMI section in the Windows Event Log	69

Figure 75: Updating Settings in NUMI XML Configuration File	70

## Introduction

This Server Setup Guide explains how to install National Utilization Management Integration (NUMI), Release 1.1.15.9.1.

### Purpose

The purpose of this document is to explain the hardware and software requirements and tasks that must be performed before and after the installation process.

### Scope

The scope of this document includes explanations of the appropriate steps to install the NUMI software, and the steps that are needed to be completed before and after the installation process is started.

### Target Audience

This document is intended for the Information Technology Team and the individuals who install software in your organization.

## Deployment Overview

The following process is followed to request permission to do a National Deployment.

### National Deployment Request

The ProPath Release Management processes govern the request for a National Deployment. Refer to ProPath for guidance on requesting a release. This process must be complete before installation of services on the NUMI servers.

### Installing NUMI on the Servers

The steps to install NUMI on the servers are described below. The middle tier of NUMI is the Veterans Information Systems Technology Architecture (VistA) Integration Adapter (VIA), which is a hosted service and is not part of the NUMI deployment. The primary NUMI application servers are located at the Austin Information Technology Center (AITC) facility in Austin, Texas. The application servers run on an Internet Information Services (IIS) Application Server. The NUMI application requires Microsoft (MS) ASP.NET 2.0 Ajax Extensions 1.0 and Web Services Enhancements 3.0 to enable the interactions with the Web Services.

#### Database Server

The NUMI database as it exists now is a manifestation of multiple changes over multiple releases. This installation document has as a pre-requisite the backup of an existing NUMI database. Therefore, to install a new NUMI database, it is necessary to restore a backup of an existing NUMI database.

Database Platform installation, and Database Restoration Procedures

Install Windows Server 2019 on the database server platform

Download and install any critical patches for the Operating System

Install the 64-bit MS Structured Query Language (SQL) Server 2019 application according to local “best practices”

- 1.1. MS’s Full Text Search is required for the NUMI installation
- 1.2. Replication is necessary for the NUMI installation to use the alternate database reporting capability of NUMI
- 1.3. Reporting Services is not necessary for installation on the NUMI database server
- 1.4. NUMI’s database will function properly in cluster, but clustering is not required for the NUMI application

Apply all appropriate patches (according to local best practices) to MS SQL Server 2019

Install / restore the database components according to the instructions in section 4.1 Instructions for Installing Database Components.

#### Web Server

To install NUMI Exchange software on the Web Server (Server 2):

1. Install Windows Server 2019 on the web server platform

Download and install any critical patches for the Operating System on all web servers

Install MS ASP.NET 2.0 Ajax Extensions 1.0

Install Web Services Enhancements 3.0

Install NUMI Exchange

Change the web.config file settings as needed

#### Application Server

To install NUMI application software on the Application Server (Server 3)

1. Install Windows Server 2019 on the application server platform

Download and install any critical patches for the Operating System on all application servers

Install the Care Enhance Review Management Enterprise (CERMe) 20.0 InterQual View 2021 application

Install the NUMI application

Change the web.config file settings as needed

Install the SiteMinder Web Agent and configure it for the NUMI application Web site

## Pre-Installation Instructions and Preparation

The Pre-Installation Instructions and Preparation section explains the tasks that need to be performed before installing NUMI software. Before proceeding with the installation procedures, consult the list of requirements below.

### Installation Process Requirements

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

1 Database Server

2 Application Servers

2 Web Servers

1 Data Warehouse Server 1 SQL Reporting Server

#### VistA Rights Needed for NUMI Users

Each NUMI user must have Computerized Patient Record System (CPRS) access in their VistA menu structure, such as in their secondary menu tree. The VistA menu name is CPRSChart (or CPRS Graphical User Interface CHART). Table 1 and Table 2 identify the menus, options and settings these user accounts will need to have assigned.

It is also highly recommended that the VIAB WEB SERVICES OPTION be added to the System Command Options [XUCOMMAND] menu in each site’s VistA system. If you do not add this to the Common Menu, you will need to add it to the secondary menu of each individual NUMI user.

Table 1: CPRS Rights

| CPRS Rights                                 |
|---------------------------------------------|
| Primary Menu: XMUSER                        |
| Primary Menu: MailMan Menu                  |
| Secondary Menu: [OR CPRS GUI CHART]         |
| Secondary Menu: CPRSChart Release 1.0.30.72 |
| Keys Held                                   |
| Patient Selection                           |
| Restrict? NO                                |
| OE/RR List                                  |

Table 2: CPRS Access Tabs

| Name   | Description   | Effective Date   | Expiration Date   |
|--------|---------------|------------------|-------------------|
| RPT    | Reports tab   | Sept. 2, 2008    | N/A               |

### Install Software in Test Environments

The software will be installed in the Test environments before installing in Production.

### Generate Pre-Installation Reports

Not applicable.

### Coordinate Installation with Other Teams

The Installation Team will need to involve the Implementation/Architecture Team.

### Install Sequence Information for Multiple Patches

Not applicable.

### Logoff During Installation

End users do not need to be logged off during installation (during the act of copying files and installation executions to the server(s)). However, the users must be logged off for any updates to the software (running the executions and/or configuring the software and configuration files).

Logging off during software updates is no different from any other logoff that a user may do.

### Average Amount of Time Required to Complete the Installation

The average amount of time required to complete the NUMI installation is 2 days.

## Database Information

Refer to the NUMI Systems Management Guide for information about the structure and components of the NUMI database.

### Instructions for Installing Database Components

The NUMI database as it exists now is a manifestation of multiple changes over multiple releases. This installation document has as a pre-requisite the backup of an existing NUMI database.  Therefore, to install a new NUMI database, it is necessary to restore a backup of an existing NUMI database.

#### Database Installation / Restoration Procedures

1. Copy a backup of an existing NUMI database(s) of appropriate size and content to the new NUMI database server
    - 1.5. The application database (typically called NUMI) is necessary for proper function of the application
    - 1.6. The “auditing” database (typically called LogSyncDb) is necessary for proper functioning of the application and the synchronizer
    - 1.7. The CERMe database can be restored from an existing backup, or can be built from scratch from the CERMe installation media
        - 1.7.1. If the CERMe database is restored from an existing backup, verify that the application configuration files reference a database authenticated user that has DBO privilege on the CERMe database for proper functioning of the NUMI application
        - 1.7.2. If the CERMe database is installed from media, follow the instructions provided by Change Healthcare for installation

Restore the database backup to the existing server

- 1.1. File paths will have to be altered according to local best practices
- 1.2. User accounts may be, but are not required to be, restored with the database. NUMI requires the numi\_user account to be setup.
- 1.3. Database ownership may be altered so that the owning account for the NUMIdatabase complies with local best practices
- 1.4. A database authenticated user for the application should be configured, and granted DBO privileges on the NUMI database

Run the Install\_XX.sql if it was provided with the build, where XX is the database version for the NUMI build. This will apply changes to the database necessary for the version of NUMI that is being installed

Install the NUMI Synchronizer according to the instructions in section 17 Installing NUMI Synchronizer on the DB Server

## Installation Procedure for Server 2019

This section identifies the installation procedures that shall be followed.

### Patch the Operating System

This applies to all servers.

1. Open up an instance of Internet Explorer.

Select menu item &lt;Tools/Windows Update&gt;.

Follow the instructions on MS’s website. ( **NOTE:** A restart of the servers may be necessary).

## SQL Server Setup (Windows Server 2019)

### Role Setup

The role set-up in this section applies to the SQL database server. Use Server Manager to install the File Services with the role services shown in Figure 1: SQL Server Role Services.

<!-- image -->

Figure 1: SQL Server Role Services

## Web Server Setup (Windows Server 2019)

### Role Setup

The role setup in this section applies to the NUMI Exchange web server.

Use Server Manager to install the File Services and Web Server (IIS) roles with the role services shown in Figure 2: NUMI Exchange Role Services and Figure 3: NUMI Exchange (IIS).

<!-- image -->

Figure 2: NUMI Exchange Role Services

<!-- image -->

Figure 3: NUMI Exchange (IIS)

### ASP.NET 2.0 AJAX Extensions 1.0 Setup

Install the ASP.NET 2.0 Ajax Extensions 1.0 as detailed in section 8.3, Install MS ASP.NET 2.0 Ajax Extensions 1.0.

### MS Web Services Enhancements (WSE) 3.0 Setup

Install MS WSE 3.0 as detailed in section 8.4 Install MS Web Services Enhancements 3.0.

## Application Server Setup (Windows Server 2019)

### Role Setup

The role setup in this section applies to the NUMI app servers. Use Server Manager to install the File Services and Web Server (IIS) roles with the role services shown in Figure 4: NUMI Role Services and Figure 5: NUMI Web Services IIS.

<!-- image -->

Figure 4: NUMI Role Services

<!-- image -->

Figure 5: NUMI Web Services IIS

### Feature Delegation

Select the main node in IIS, with the server name. Then double click on “Feature Delegation” item.  Change the “Feature Delegation” settings for the server, as shown in Figure 6: IIS Feature Delegation.

<!-- image -->

Figure 6: IIS Feature Delegation

Make sure all authentication rules are set to Read/Write as shown in Figure 7: Feature Delegation Selection.

<!-- image -->

Figure 7: Feature Delegation Selection

### Install MS ASP.Net 2.0 AJAX Extensions 1.0

Installing MS ASP.NET 2.0 Ajax Extensions 1.0 applies to the web servers only.

1. Download the MS ASP.NET 2.0 Ajax Extensions 1.0  from MS’s website.

Run the ASPAJAXExtSetup.msi by double-clicking it.

When the File Download – Security Warning window displays, click the &lt;Run&gt; button (shown in Figure 8: MS ASP.Net 2.0 File Download-Security Warning Window).

<!-- image -->

Figure 8: MS ASP.Net 2.0 File Download-Security Warning Window

When the Internet Explorer – Security Warning window displays, click the &lt;Run&gt; button (shown in Figure 9: MS ASP.Net 2.0 Internet Explorer-Security Warning Window).

<!-- image -->

Figure 9: MS ASP.Net 2.0 Internet Explorer-Security Warning Window

When the MS ASP.NET 2.0 AJAX Extensions 1.0 Setup window displays, click the &lt;Next&gt; button (shown in Figure 10: MS ASP.NET 2.0 AJAX Extensions 1.0 Setup Wizard Window).

<!-- image -->

Figure 10: MS ASP.NET 2.0 AJAX Extensions 1.0 Setup Wizard Window

Click the “I accept the terms in the License Agreement” checkbox, as illustrated in Figure 11: MS ASP.NET 2.0 AJAX License Agreement Window.

1. Click the &lt;Next&gt; button.
<!-- image -->

Figure 11: MS ASP.NET 2.0 AJAX License Agreement Window

Click the &lt;Install&gt; button (shown in Figure 12: MS ASP.NET 2.0 AJAX Installation Window).

<!-- image -->

Figure 12: MS ASP.NET 2.0 AJAX Installation Window

The installation is complete. Select the &lt;Finish&gt; button by clicking on it to exit the installation wizard, as depicted in Figure 13: MS ASP.NET 2.0 AJAX Completion window.

<!-- image -->

If you do not wish to view the release notes, un-check the “Display MS ASP.NET 2.0 AJAX Extensions 1.0 Release Notes” checkbox.

<!-- image -->

Figure 13: MS ASP.NET 2.0 AJAX Completion window

### Install MS Web Services Enhancements 3.0

Installing MS Web Services Enhancements 3.0 applies to the web servers only.

1. Download the MS Web Services Enhancements 3.0 from MS’s website.

Run the MS WSE 3.0.msi by double-clicking it.

When the File Download – Security Warning window displays, click the &lt;Run&gt; button (shown in Figure 14: MS WSE 3.0 File Download-Security Warning Window).

<!-- image -->

Figure 14: MS WSE 3.0 File Download-Security Warning Window

1. When the Internet Explorer – Security Warning window displays, click the &lt;Run&gt; button (shown in Figure 15: MS WSE 3.0 Internet Explorer-Security Warning Window).
<!-- image -->

Figure 15: MS WSE 3.0 Internet Explorer-Security Warning Window

1. When the MS WSE 3.0 – InstallShield Wizard window displays, click the &lt;Next&gt; button (shown in Figure 16: MS WSE 3.0 InstallShield Wizard Welcome Window).
<!-- image -->

Figure 16: MS WSE 3.0 InstallShield Wizard Welcome Window

1. Click the “I accept the terms in the license agreement” checkbox, as illustrated in Figure 17: MS WSE 3.0 License Agreement Window.

Click the &lt;Next&gt; button.

<!-- image -->

Figure 17: MS WSE 3.0 License Agreement Window

1. Click the &lt;Administrator&gt; radio button, as illustrated in Figure 18: MS WSE 3.0 InstallShield Wizard Window.

Click the &lt;Next&gt; button.

<!-- image -->

Figure 18: MS WSE 3.0 InstallShield Wizard Window

1. Click the &lt;Install&gt; button (shown in Figure 19: MS WSE 3.0 Installation Window).
<!-- image -->

Figure 19: MS WSE 3.0 Installation Window

1. Click the &lt;Finish&gt; button (shown in Figure 20: MS WSE 3.0 Completion Window).
<!-- image -->

Figure 20: MS WSE 3.0 Completion Window

## Install SQL Server

Install the MS SQL Server 2019 Database Server software only on the database server, applying both MS installation instructions and local best practices.

Additional service packs or patches may be installed subsequent to application testing, and in accordance with local best practices.

All production NUMI databases should be run in Simple Recovery mode, to enable replication to function, and to maximize the recoverability of the databases. In non-production environments, any recovery mode is acceptable, and simple recovery mode is encouraged for development and QA testing environments due to ease of administration.

### Download all SQL Server Patches

Downloading all SQL Server Patches applies to the database server only.

### Restore the Appropriate Databases for the NUMI Application

Restoring the Appropriate Databases for the NUMI Application applies to the database server only.

Follow the instructions in section 4 Instructions for Installing Database Components.

## Installing NUMI Exchange on Server 2019

<!-- image -->

Before doing this, you must make a backup copy of the web.config file (if this is an upgrade). Settings may need to be extracted from this in the future.

### Unzip/Install NUMI Exchange Distribution

1. Using Windows Explorer, create the NumiExchange folder on the D drive, if available; otherwise create on the C drive. E.g., D:\NumiExchange

Unzip the NUMI Exchange files into the NumiExchange folder created above.

Update the application settings in the NUMI Exchange web.config file, located in the directory created above. Typically, this would involve updating the database connection string.

### NUMI Exchange Website Configuration

Using IIS Manager, add a new website and select the Secure Socket Layer (SSL) certificate as shown in Figure 21: Add NUMI Exchange Website.

<!-- image -->

Figure 21: Add NUMI Exchange Website

<!-- image -->

Figure 22: NUMI Exchange Website

The NUMI website basic and advanced settings are shown in Figure 23: NUMI Exchange Basic Settings and Figure 24: NUMI Advanced Settings.

<!-- image -->

Figure 23: NUMI Exchange Basic Settings

<!-- image -->

Figure 24: NUMI Advanced Settings

The NUMI Exchange web site bindings are shown in Figure 25: NUMI Exchange Bindings.

<!-- image -->

Figure 25: NUMI Exchange Bindings

The NUMI Exchange web site authentication settings are shown in Figure 26: NUMI Exchange Authentication Settings.

<!-- image -->

Figure 26: NUMI Exchange Authentication Settings

The NUMI Exchange website SSL settings are shown in Figure 27: NUMI Exchange SSL Settings.

<!-- image -->

Figure 27: NUMI Exchange SSL Settings

#### Application Pool Configuration

The NUMI Exchange application pool setup is shown in Figure 28: Application Pool Window.

<!-- image -->

Figure 28: Application Pool Window

The NUMI Exchange application pool basic settings are shown in Figure 29: NUMI Exchange Application Pool Basic Settings.

<!-- image -->

Figure 29: NUMI Exchange Application Pool Basic Settings

The NUMI Exchange application pool advanced settings are shown in Figure 30: NUMI Exchange Pool Advanced Settings.

<!-- image -->

Figure 30: NUMI Exchange Pool Advanced Settings

## Installing NUMI on Server 2019

### Software Copy Instructions

Right click on the zip file, select the “Unblock” if active, and select O.K. Some security schemes will block certain files from being unpacked, typically the Java files under the “web” directory. Setting the file to Unblock eliminates this problem.

<!-- image -->

Figure 31: Unblocking Restricted Files in Installation ZIP File

It is recommended that NUMI be installed in the D:\NUMI folder. Using Windows Explorer, create a NUMI folder in D drive, if available, otherwise create in C drive. E.g., D:\NUMI.

Unzip the NumiWebApp folder from the NUMI distribution zip file into the D:\NUMI folder. Rename the NumiWebApp folder using the build name of the distribution zip file.

### NUMI Web Site Configuration

Using IIS Manager, add a new web site as shown in Figure 32: Add NUMI Website.

<!-- image -->

Figure 32: Add NUMI Website

The NUMI web site basic and advanced settings are shown in Figure 33: NUMI Basic Settings and Figure 34: NUMI Advanced Settings.

<!-- image -->

Figure 33: NUMI Basic Settings

<!-- image -->

Figure 34: NUMI Advanced Settings

The NUMI web site bindings are shown in Figure 35: NUMI Bindings.

<!-- image -->

Figure 35: NUMI Bindings

The NUMI web site authentication settings are shown in Figure 36: NUMI Authentication Settings. Make sure Forms Authentication is the only one enabled.

<!-- image -->

Figure 36: NUMI Authentication Settings

The NUMI website SSL settings are shown in Figure 37: NUMI SSL Settings.

<!-- image -->

Figure 37: NUMI SSL Settings

The NUMI web site compression settings are shown in Figure 38: NUMI Compression Settings.

<!-- image -->

Figure 38: NUMI Compression Settings

### Application Pool Configuration

The NUMI application pool setup is shown in Figure 39: Application Pool Window.

<!-- image -->

Figure 39: Application Pool Window

The NUMI application pool basic settings are shown in Figure 40: NUMI Application Pool Basic Settings.

<!-- image -->

Figure 40: NUMI Application Pool Basic Settings

The NUMI application pool advanced settings are shown in Figure 41: NUMI Application Pool Advanced Settings.

<!-- image -->

Figure 41: NUMI Application Pool Advanced Settings

## Install CA SiteMinder Web Agent for Single Sign On (SSO) on the Web server

The CA SiteMinder Web Agent needs to be installed and configured on the WebServer where the NUMI web application will be setup. The VA Identity and Access Management (IAM) Team provides the software and instructions to install the CA SiteMinder Web Agent.

### Agent location

The current version of software can be found below:

[\\vaausfpciamsh61.vha.med.va.gov\Partners\_Share\CA\_SiteMinder\_WebAgents\Windows\Current](file:///vaausfpciamsh61.vha.med.va.gov/Partners_Share/CA_SiteMinder_WebAgents/Windows/Current)

Copy the 32-bit or 64-bit version of the zip file as appropriate based on the OS in the server and extracts it. You will get a file with name ‘ca-wa-12.51-cr08-win32.exe’ in case of 32-bit and ‘ca-wa-12.51-cr08-win64-64.exe’ in case of 64-bit.

### Agent installation

Follow the instructions below to install the software on the application server:

- 1.1.1.1. Run the exe file you obtained after extracting the zip file. If you get a dialog as shown in Figure 42 click on ‘Run’ button.
<!-- image -->

Figure 42: Security Warning

- 1.1.1.1. Wait for the dialog shown in Figure 43 to close. It may take little longer for the next dialog to show up.
<!-- image -->

Figure 43: Preparing to install dialog

- 1.1.1.1. Click on ‘Next’ in the dialog shown in Figure 44.
<!-- image -->

Figure 44: Web agent install wizard - Welcome screen

- 1.1.1.1. Scroll through to the bottom of the license agreement, accept it and click ‘Next’ button (as shown in Figure 45).
<!-- image -->

Figure 45: Web agent install wizard - License agreement screen

- 1.1.1.1. Leave the default location of installation (as shown in Figure 46) and click ‘Next’.
<!-- image -->

Figure 46: Web agent install wizard - Install location screen

- 1.1.1.1. Review the summary screen and click on ‘Install’ button (as shown in Figure 47).
<!-- image -->

Figure 47: Web agent install wizard - Review screen

- 1.1.1.1. Select ‘No. I would like to configure the Agent later’ option in the agent configuration screen as shown in Figure 48 and click ‘Next’.
<!-- image -->

Figure 48: Web agent install wizard - Agent configuration screen

- 1.1.1.1. Select one of the options in the Install Complete screen as shown in Figure 49 and click on ‘Done’ button. A restart is required to continue with the agent configuration steps described in the next section. If you selected ‘No’ you would need to wait until the server is restarted to continue with next steps.
<!-- image -->

Figure 49: Web agent install wizard - Install complete screen

### Agent configuration

The next steps require you to launch the agent configuration wizard from the start menu. The Figure 50 shows the one that would need to be launched.

<!-- image -->

Figure 50: Launch Web Agent Configuration Wizard

If you were configuring the agent for the first time on this specific server, you would need to register the host with the IAM server. In that case, follow the instructions in Section 12.3.1.

Otherwise, skip to Section 12.3.2. Launch the Web Agent Configuration Wizard as described in Figure 50 and continue with the steps in that section.

After you complete any of these configuration steps, you would need to reset IIS by running the following command at admin command prompt:

iisreset

**NOTE** : You may need to use different values for various options in the below steps if IAM team has provided different values.

#### Configuring for the first time

**NOTE** : The steps below are if you want to register the server with IAM. This can only be done once. If for any reason you need to reconfigure the whole server, you would need to contact the IAM Team to get the current server registration deleted before you can re-run these steps.

- 1.1.1.1. Select ‘Yes, I would like to do Host Registration now’ and click ‘Next’ in the dialog as shown in Figure 51.
<!-- image -->

Figure 51: Web agent configuration wizard - Host registration

- 1.1.1.1. Enter the following details in the Admin Registration screen (Figure 52), ensure ‘Enable Shared Secret Rollover’ is unchecked and click ‘Next’ button.
Admin User Name: threg
Admin Password: &lt;will be provided&gt;
<!-- image -->

Figure 52: Web agent configuration wizard - Admin credentials

- 1.1.1.1. Enter the FQDN of the server you are currently configuring in the ‘Trusted Host Name’ box and one of values from Table 3 based on which IAM environment you are trying to connect to for ‘Host Configuration Object’ in the next dialog as shown in Figure 53.

Table 3: IAM Host Configuration Object

| Environment   | Host Configuration Object   |
|---------------|-----------------------------|
| Environment   | Host Configuration Object   |
| DEV           | DEVHCO                      |
| SQA           | SQAHCO                      |
| Preprod       | Preprod_ext                 |
| PROD          | PROD_external_HCO           |

<!-- image -->

Figure 53: Web agent configuration wizard - Host name and configuration object

- 1.1.1.1. Add the three IP Address of Policy Server one at a time in the ‘IP Address’ box from Table 4 based on the IAM environment you are trying to connect to and click ‘Next’ in the dialog as shown in the Figure 54.

Table 4: SiteMinder Policy Server IP Address

| Environment   | SiteMinder Policy Server IP Address   |
|---------------|---------------------------------------|
| Environment   | SiteMinder Policy Server IP Address   |
| DEV           | 10.227.211.211                        |
| DEV           | 10.227.211.212                        |
| DEV           | 10.227.211.213                        |
| SQA           | 10.227.238.46                         |
| SQA           | 10.227.238.47                         |
| SQA           | 10.227.238.48                         |
| Preprod       | 10.244.91.18                          |
| Preprod       | 10.244.91.20                          |
| Preprod       | 10.244.91.21                          |
| PROD          | 10.244.90.18                          |
| PROD          | 10.244.90.20                          |
| PROD          | 10.244.90.21                          |

<!-- image -->

Figure 54: Web agent configuration wizard - Policy server IP Address

- 1.1.1.1. Select ‘FIPS Only Mode’ in the next screen as shown in Figure 55 and click ‘Next’.
<!-- image -->

Figure 55: Web agent configuration wizard - FIPS mode setting

- 1.1.1.1. Leave everything default in the next screen as shown in Figure 56 and click ‘Next’
<!-- image -->

Figure 56: Web agent configuration wizard - Configuration file location

- 1.1.1.1. Select the web server on which NUMI was installed and click ‘Next’. Usually only one will be listed in this dialog as shown in Figure 57.
<!-- image -->

Figure 57: Web agent configuration wizard - Web server

- 1.1.1.1. Enter ‘NUMIAgentConfig’ in ‘Default Agent Configuration Object,’ check ‘Enable Agent’ and uncheck ‘Manage Application Pools’ in the next screen as shown in Figure 58 and click ‘Next’.
<!-- image -->

Figure 58: Web agent configuration wizard - Agent configuration

- 1.1.1.1. Select the NUMI website and any other sites where you want to enable SSO on and click ‘Next’.
<!-- image -->

Figure 59: Web agent configuration wizard - Sites selection

- 1.1.1.1. Review the options you selected in the summary screen as shown in Figure 60 and click on ‘Install’ button.
<!-- image -->

Figure 60: Web agent configuration wizard - Summary screen

- 1.1.1.1. Click on ‘Done’ when you see the completion screen as shown in Figure 61.
<!-- image -->

Figure 61: Web agent configuration wizard - Completion screen

#### Reconfiguration configuration

**NOTE** : The steps below are if you want to reconfigure one or more websites in IIS due to say re-deployment. The server should have already been registered with IAM using the steps in Section 12.3.1.

- 1.1.1.1. Select ‘No, I would like to do Host Registration later’ and click ‘Next’ in the dialog as shown in Figure 62.
<!-- image -->

Figure 62: Web agent configuration wizard - Host registration

- 1.1.1.1. Select the web server on which NUMI was installed and click ‘Next’. Usually only one will be listed in this dialog as shown in Figure 63.
<!-- image -->

Figure 63: Web agent configuration wizard - Web server

- 1.1.1.1. Enter ‘NUMIAgentConfig’ in ‘Default Agent Configuration Object’ if not already entered, check ‘Enable Agent’ and uncheck ‘Manage Application Pools’ in the next screen as shown in Figure 64 and click ‘Next’.
<!-- image -->

Figure 64: Web agent configuration wizard - Agent configuration

- 1.1.1.1. Select the NUMI website and any other sites where you want to enable SSO on and click ‘Next’. The sites that were previously configured will remain selected and cannot be changed (unconfigured) as shown in Figure 65.
<!-- image -->

Figure 65: Web agent configuration wizard - Sites selection

- 1.1.1.1. Review the options you selected in the summary screen as shown in Figure 66 and click on ‘Install’ button.
<!-- image -->

Figure 66: Web agent configuration wizard - Summary screen

- 1.1.1.1. In the screen shown in Figure 67, select appropriate option for the site you are trying to reconfigure and click ‘Next’.

‘Overwrite’ will overwrite the previously configured settings with the new one entered in the previous steps of this wizard. ‘Preserve’ will not change any existing settings but will add missing settings back in to the site.  If ‘Unconfigure’ is selected it will remove and disable SSO for the selected site.

<!-- image -->

Figure 67: Web agent configuration wizard - Previously configured sites

- 1.1.1.1. Review the options you selected in the summary screen as shown in Figure 68 and click on ‘Install’ button.
<!-- image -->

Figure 68: Web agent configuration wizard - Summary screen

- 1.1.1.1. Click on ‘Done’ when you see the completion screen as shown in Figure 69.
<!-- image -->

Figure 69: Web agent configuration wizard - Completion screen

## Secure Token Service Integration for SSOi

NUMI supports secure token service implementation through SSOi.  Full details of the implementation can be found at SSOi Secure Token Service Playbook.

### Download Certificate Chain from appropriate endpoint

Downloading the chain can be done from any computer but installing the chain must be done as the local computer account of the server being set up.

- iDEV: [https:/redacted:9301/STS/RequestSecurityToken](https://int.services.eauth.va.gov:9301/STS/RequestSecurityToken)
- SQA: [https:// redacted:9301/STS/RequestSecurityToken](https://sqa.services.eauth.va.gov:9301/STS/RequestSecurityToken)
- PREPROD: [https:// redacted:9301/STS/RequestSecurityToken](https://preprod.services.eauth.va.gov:9301/STS/RequestSecurityToken)
- PROD: [https:// redacted 301/STS/RequestSecurityToken](https://services.eauth.va.gov:9301/STS/RequestSecurityToken)

- 1.1.1.1. Install the full certification chain from the matching IAM environment(s).  This can be obtained by visiting the link and clicking the lock icon and choosing “View Certificates”. [https://services.eauth.va.gov:9301/](https://services.eauth.va.gov:9301/STS/RequestSecurityToken)
<!-- image -->

1. Install the full certification chain from the matching IAM environment(s).  This can be obtained by visiting the link and clicking the lock icon and choosing “View Certificates”. 
https:// redacted:9301/
<!-- image -->
2. Click on the Details tab and select “Copy to file”, choose PKCS and include all certificates in the path if possible
<!-- image -->
3. Save file as &lt;endpointname\_date&gt;, click next then finish.
<!-- image -->
4. Optional – Reuse this file if another web server requires this STS endpoint’s certificate.

1. In MMC, right click Computer-Personal store and import the certificate created in Step 9.
<!-- image -->

1. Import for local machine
<!-- image -->

1. Browse to file created in step 10 and click Next

<!-- image -->

1. Place all certificates in the Personal store, click next and finish
<!-- image -->

1. The imported certificate should now be in the store (refreshing may be required).  It will follow the naming convention xxxx.services.eauth.va.gov

<!-- image -->

### Export server cert to .pfx

This is a copy of the .cer installed locally to the computer/personal account.  It should be the one served by IIS when you navigate to the website.

- 1.1.1.1. Load the Microsoft Management Console, Certificate Snap-in, for the local computer

## Find the server cert in the personal folder

<!-- image -->

## Right click and export the certificate

<!-- image -->

## Select “Yes, export private key” and choose next

<!-- image -->

## Select “Export all extended properties” and choose next

<!-- image -->

## Select a strong password.  This password will go into NumiWebApp.config later in this guide.

<!-- image -->

## Select a filename for the exported certificate and save it as a .pfx.  Select a folder not specific to a version of NUMI as this cert will be valid for future versions of the applications until expiration.  For example, if the folder structure for website is NUMI/NUMI\_15.9 select the /NUMI folder for the cert and not the specific /NUMI\_15.9 folder.  This file path will go into NumiWebApp.config later in this guide.

### NumiWebApp.config keys

&lt;!-- STS Service configuration --&gt;

&lt;add key="STSEndpoint" value="https:// redacted:9301/STS/RequestSecurityToken"/&gt;

&lt;add key="STSEnabled" value="true"/&gt; &lt;!-- Set "true" to enable STS service integration --&gt;

&lt;add key="STSCertificatePath" value="D:\\numi\_web820.pfx"/&gt;

&lt;add key="STSCertificatePassword" value="numi123"/&gt;

STSEnabled – anything but “true” will disable STS and revert to access/verify

## ## 21 Installing CERMe Software and Database from CERMe Installation CD

Refer to the RM Install Guide PDF file on the CERMe (COTS product) setup CD for detailed instructions on how to set up CERMe (DBA assistance may be required to setup the database, which must be done before application setup).

### Install CERMe on the Application Server

**NOTE:** Change Healthcare provides version updates several times a year.  The example below may not be the latest version

CERMe Review Manager (RM) 20.0 InterQual 2021 for NUMI 15.9.1 will be installed based on an existing installation of CERMe 19.1. The CERMe installation would be performed using a dump of the existing CERMe 19.1 database. Listed below are the steps to restore the database and install CERME:

1. Restore CERMe 19.1 data from the CERMe database dump obtained from the current CERMe pre-Prod/Production servers. Create database logins for orphaned users in the restored database. Write down the credentials for the new logins created. This will be required for the CERMe install.

Navigate to the CERMe install image and double click the install.htm file in the root directory to open the setup welcome page. This will open the CERMe install page in Internet Explorer.

Click on the Install Review Manager 20.0 / InterQual View 2021 link on the installation page. This will prompt to save or run the file, select Run. This will start the CERMe Install wizard.

Accept the license agreement and click Next.

On the License Information screen, enter the license information given above and click Next.

On the Select Review Manager Enterprise screen, select “Review Manager Enterprise” and click Next.

On the Installation Type screen, select “New Installation” and click Next.

Select an installation directory.

On the Choose Components screen, keep the default selection (i.e., all selected) and click Next.

On the Database Information page, enter the following info and click Next.

- Database type: SQL Server
- Server Name: Name of the SQL database server
- Database: Name of the database to which the dump restored in step 1
- Port Number: SQL Server
- Instance: leave blank
- User ID: SQL Server user ID with access to the CERMe database restored above
- Password: Password for the SQL Server user used above

On separate database to store report data screen, select No and click Next.

On the Install Jetty window, select Yes to install Jetty.

On the next screen, enter 8357 for Port Number.

On the next screen, select the hardware architecture.

Review the selections, and click Install to start the installation.

Once the installation completes, go to the URL: http://&lt;servername&gt;:8357/rm/login.

This is should open the CERMe login page.

Now follow the steps below to update CERMe to CERMe 20.0.

Stop the CERMe Service from the Windows Services.

Create a backup of the CERMe Installation folder and the CERMe database.

Make the changes to the file (below)on the CERMe Jetty Server:

#### File: &lt;CERMe Install Folder&gt;\Jetty\etc\webdefault.xml

Add the following element to &lt;session-config&gt; element.

&lt;cookie-config&gt;

&lt;http-only&gt;true&lt;/http-only&gt;

&lt;/cookie-config&gt;

Session Config element should look like the following after the change:

&lt;session-config&gt;

&lt;session-timeout&gt;30&lt;/session-timeout&gt;

**&lt;cookie-config&gt;**

**&lt;http-only&gt;true&lt;/http-only&gt;**

**&lt;/cookie-config&gt;**

&lt;/session-config&gt;

#### File: &lt;CERMe Install Folder?\Jetty\etc\jetty-rewrite.xml

Add the following &lt;Call&gt; element to the end of the &lt;New&gt; element.

&lt;Call name="addRule"&gt;

&lt;Arg&gt;

&lt;New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"&gt;

&lt;Set name="pattern"&gt;/*&lt;/Set&gt;

&lt;Set name="name"&gt;Strict-Transport-Security&lt;/Set&gt;

&lt;Set name="value"&gt;max-age=31536000; includeSubDomains&lt;/Set&gt;

&lt;/New&gt;

&lt;/Arg&gt;

&lt;/Call&gt;

The file will look like the following after the change:

&lt;Set name="handler"&gt;

&lt;New id="Rewrite" class="org.eclipse.jetty.rewrite.handler.RewriteHandler"&gt;

&lt;Set name="handler"&gt;&lt;Ref refid="oldhandler"/&gt;&lt;/Set&gt;

&lt;Set name="rewriteRequestURI"&gt;&lt;Property name="rewrite.rewriteRequestURI" default="true"/&gt;&lt;/Set&gt;

&lt;Set name="rewritePathInfo"&gt;&lt;Property name="rewrite.rewritePathInfo" default="false"/&gt;&lt;/Set&gt;

&lt;Set name="originalPathAttribute"&gt;&lt;Property name="rewrite.originalPathAttribute" default="requestedPath"/&gt;&lt;/Set&gt;

**&lt;Call name="addRule"&gt;**

**&lt;Arg&gt;**

**&lt;New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"&gt;**

**&lt;Set name="pattern"&gt;/*&lt;/Set&gt;**

**&lt;Set name="name"&gt;Strict-Transport-Security&lt;/Set&gt;**

**&lt;Set name="value"&gt;max-age=31536000; includeSubDomains&lt;/Set&gt;**

**&lt;/New&gt;**

**&lt;/Arg&gt;**

**&lt;/Call&gt;**

&lt;/New&gt;

&lt;/Set&gt;

#### File: &lt;CERMe Install Folder&gt;\Jetty\start.ini

Add the following new section to the bottom of the file:

# ===========================================================

# Enforce Strict Transport Security

# -----------------------------------------------------------

OPTIONS=rewrite

etc/jetty-rewrite.xml

#### File: &lt;CERMe Install Folder&gt;\Jetty\ReviewManager.xml

Add the content below to the end of the &lt; Config &gt; element

&lt;IntegratedLogin Enabled="true" CookieName="unifiedkey" UnifiedKey="8rzVNfLwjHWHvPctaen9dw=="

AuthenticationFailUrl="/iqm/html/rm\_integrated\_authentication\_failed.htm" GuidUserCid="IQ\_1" Guid="A1B0B165-3C18-4561-935F-5FB81BD42128"

AuthenticateWS="false"/&gt;

The modified file will look like the following:

…

&lt;Path Prefix="/rm"/&gt;

&lt;Login Check="true"/&gt;

**&lt;IntegratedLogin Enabled="true" CookieName="unifiedkey" UnifiedKey="8rzVNfLwjHWHvPctaen9dw==" AuthenticationFailUrl="/iqm/html/rm\_integrated\_authentication\_failed.htm" GuidUserCid="IQ\_1" Guid="A1B0B165-3C18-4561-935F-5FB81BD42128" AuthenticateWS="false"/&gt;**

&lt;/Config&gt;

&lt;/ReviewManager&gt;

Start CERMe Service from the Windows Services.

Go to CERMe URL: http://&lt;server&gt;:8443/rm/login Login with the credential provided, and go to the menu Help &gt; About. It should show Version InterQual Review Manager™ 19 (Build 191).

This completes the installation of the CERMe RM 20.0 InterQual 2021.

### Install CERMe SSL Certificate

NUMI will need SSL certificates for CERMe (for Jetty). NUMI uses the SSL certificate for the server that CERMe is running on. If the sever does not have a SSL certificate installed, follow the normal VA processes for obtaining SSL Certificates and install it.

1. Use IIS Manager to export the current certificate to a .pfx file. Select the server name in the Connections pane and double click on the Server Certificates in the IIS pane as shown in Figure 70.
<!-- image -->

Figure 70: IIS Server Certificates

Select the certificate to export and click on the “Export…” link in the Actions pane, as shown in Figure 71.

<!-- image -->

Figure 71: IIS Server Certificate Selection

Set the name of the .pfx file. Set the password, e.g., use numi (all lowercase) for the password, as shown in Figure 72. This password will be used in subsequent steps.

<!-- image -->

Figure 72: IIS Certificate Details

**NOTE** : For the following, the password can be whatever you choose, but please make a note of them, as they will be used later.  For this example, D:\Certs\NUMI.pfx is the file name and the password, the one that you used to export the .pfx file, e.g., numi (all lowercase).

Open a command prompt window and change the current directory to the location of the keytool executable.  In this example it would be:

D:\Program Files (x86)\Change Healthcare\CERME\Jre\bin\keytool.exe

Execute the following command:

keytool -importkeystore -srcstoretype PKCS12 -srckeystore "D:\Certs\NUMI.pfx" -destkeystore "D:\Certs\CERME.ks"

**NOTE** : -srckeystore value will be the .pfx path and filename above, -destkeystore can be whatever you choose; again, passwords can be whatever you choose, but please make a note of them.  The word “secret” is used as the keystore password in this example.

Execute the following command:

Keytool –list -keystore "D:\Certs\CERME.ks”

Make a note of the long, auto-generated alphanumeric value circled in red below. Recommended actions are to copy, paste the entire command prompt output to notepad to copy, and paste this value.

<!-- image -->

Figure 73: keytool -keystore "C:\Certs\CERME.ks" –list

Execute the following command:

keytool -changealias -keystore "D:\Certs\CERME.ks" -destalias numi –alias &lt;alphanumeric value&gt;

**NOTE:** Replace &lt;alphanumeric value&gt; with the value noted and circled from the step above. The keystore password is the password specified when creating the keystore above, secret in our example.  The key password is the password specified when creating the pfx file, numi in our example.

Execute the following command:

keytool -keypasswd -keystore "D:\Certs\CERME.ks" -alias numi

**NOTE** : With this command, we are changing the key password to “reallysecret” for this example.

Next, copy the keystore, (D:\Certs\CERME.ks), to the Jetty\etc directory.  For this example, it would be here: D:\Program Files (x86)\Change Healthcare\CERME\Jetty\etc.

Modify &lt;Jetty-home&gt;\start.ini. Uncomment the relevant lines in the SSL Context and HTTPS Connector sections of start.ini file (as shown in the example below).

#=========================================================

# SSL Context

# Create the keystore and trust store for use by

# HTTPS and SPDY

#-------------------------------------------------------------------

jetty.keystore=etc/keystore

jetty.keystore.password=(your password)

jetty.keymanager.password=(your password)

jetty.truststore=etc/keystore

jetty.truststore.password=(your password)

jetty.secure.port=(your SSL port number)

etc/jetty-ssl.xml

#===========================================================

# HTTPS Connector

# Must be used with jetty-ssl.xml

#-----------------------------------------------------------

jetty.https.port=(your SSL port number)

etc/jetty-https.xml

Open the windows services management console, (START-&gt;RUN-&gt;services.msc-&gt;OK), and restart the CERMe service.  It will take about 20 to 30 seconds for the service to restart completely but you should be able to browse directly to the secure CERMe.  Use whatever URL is used to access NUMI, e.g., https://vaww.prod.temp.numi.med.va.gov/web/home.aspx

Replace the “/web/home.aspx” portion with CERMe’ s secure port, (8443 by default), e.g., https://vaww.prod.temp.numi.med.va.gov:8443/

The CERMe website should be displayed and you should not have been warned of the security certificate problem.

## Setting up NUMI Section in the Windows Event Log

1. Change Directory - Go to command prompt (run as Administrator) and change current directory to Framework v2.0 bit folder e.g., C:\WINDOWS\MS.NET\Framework\v4.5.x

Install Command - Type InstallUtil.exe /I &lt; source folder full path &gt;\bin\NumiWebApp.dll under Framework v4.5 folder and press enter.

e.g., InstallUtil.exe /i D:\NUMI\&lt;install\_dir&gt;\bin\NumiWebApp.dll

This should create a NUMI section in the Windows Event log.

<!-- image -->

Figure 74: Creating a NUMI section in the Windows Event Log

NUMI Event Folder Properties

- 1.1. Go to NUMI Properties by right mouse.
- 1.2. Click on General Tab under NUMI Properties dialog box window. Check/Click on Overwrite events as needed.
- 1.3. Press &lt;Apply&gt; button (if needed) and Press &lt;OK&gt; button.
- 1.4. Verify Event View, if any error logs occurred during the installation.

### Validate XML Configuration File Settings

Verify that all XML configuration file settings are correct. Validate NUMI XML Configuration File Settings.

1. Edit the application settings in the web.config file in the NUMI folder. E.g., D:\NUMI\&lt;install\_dir&gt;\web.config

Settings to update:

&lt;!-- change this setting to point to the appropriate config file for the deployment. --&gt;

&lt;appSettings configSource="src\\main\\resources\\xml\\deployment\\numiwebapp.config"/&gt;

&lt;connectionStrings/&gt;

<!-- image -->

Figure 75: Updating Settings in NUMI XML Configuration File

Edit the application settings in the config file indicated in the previous entry.  Make sure to enter the VIA configuration properties listed below and the NUMI database server names, and the NUMI database password as indicated.

D:\NUMI\&lt;install\_dir&gt;\src\main\resources\xml\deployment\numiweb app.config Settings to update:

&lt;!-- VIA Service configuration --&gt;

&lt;add key="VIAServiceURL" value="&lt;VIA Service URL&gt;" /&gt;

&lt;add key="VIARequestingApp" value="&lt;Requesting App ID assigned by VIA&gt;"/&gt;

&lt;add key="VIAConsumingAppToken" value="&lt;Consuming App token assigned by VIA&gt;"/&gt;

&lt;add key="VIAConsumingAppPassword" value="&lt;Consuming app password assigned by VIA&gt;"/&gt;

&lt;add key="numiDbConnectionString" value="Data Source=&lt;enter\_database\_server&gt;;Database=NUMI;User ID=numi\_user;Password=xxxxxxxx;Trusted\_Connection=False" /&gt;

&lt;add key="SSOLogoutUri" value="…" /&gt;

Modify the value of ‘SSOLogoutUri’setting to one of the URLs from the table below which is based on the installed environment.

Table 5: SSOLogoutUri values

| Environment   | Value                   |
|---------------|-------------------------|
| DEV           | https:/ redacted t.aspx |
| SQA           | https:// redacted.aspx  |
| Preprod       | https:// redacted.aspx  |
| PROD          | https:// redacted.aspx  |

Follow the steps below to encrypt the updated NumiWebApp.config

- 1.1. Open a command prompt and change to .Net Framework 4.x directory (e.g. C:\Windows\MS.NET\Framework64\v4.x.x)
- 1.2. Run command :

.\aspnet\_regiis.exe -pef "appSettings" D:\NUMI\&lt;install\_dir&gt;

- 1.1. The command should execute successfully and give the following message:

Encrypting configuration section...

Succeeded!

- 1.1. Verify that the src\\main\\resources\\xml\\deployment\\NumiWebApp.config file does not contain any plain text passwords any more.

**NOTE:**

**Important: Make sure there is no unencrypted copy of the NumiWebApp config file in the server**

To make any future changes to the src\\main\\resources\\xml\\deployment\\NumiWebApp.config first decrypt the file by running command:

.\aspnet\_regiis.exe -pdf "appSettings" D:\NUMI\&lt;install\_dir&gt;

Make changes to the configuration as needed and follow the above steps to encrypt it again.

## Perform Restart

Restart IIS

1. Click &lt;Start&gt;.

Click the Command Prompt (or &lt;Run&gt;, depending on the Operating System)

Type:  IISReset

Click &lt;Enter&gt;.

## Test NUMI Web Site Functionality

Open Internet Explorer and type: http:// redacted.aspx e.g., https://vaausnumapp40/Web/Home.aspx

## Installing NUMI Synchronizer on the DB Server

### Installation Instructions

1. Copy the Sychronizer\_Setup.msi file to the intended environment.  This file will be provided by Tier 3 maintenance and should be stored on each environment
<!-- image -->

- If an upgrade in place, stop the existing service in task manager and uninstall from program files
<!-- image -->

<!-- image -->

1. Launch the Synchronizer Setup file

1. Click Next
<!-- image -->

1. Choose the everyone option and browse to the desired directory
<!-- image -->

1. Click next
<!-- image -->
2. Click Close
<!-- image -->

1. Enter the connection information for VIA &amp; NUMI DB into the Synchronizer.config and Sychronizer.exe.config.  Use the database server full name in source, e.g. VAAUSNUMSQLXX.aac.dva.va.gov where XX is the number of the database.

**&lt;!-- VIA Service configuration --&gt;**

&lt;add key="VIAServiceURL" value=" **https:// redacted /via-webservices/services/NumiService** " /&gt;

&lt;add key="VIARequestingApp" value=" **NumiBatch** "/&gt;

&lt;add key="VIAConsumingAppToken" value ***=*** " ***(SEE PW VAULT)"/&gt; PW Vault under “NUMI***

***Synchronizer PWs (VIARequestingApp)*** ” **Under NOTES section**

&lt;add key="VIAConsumingAppPassword" value=" ***(See PW VAULT)"/&gt; PW Vault under “NUMI 	Synchronizer PWs (VIARequestingApp)*** ” **Under NOTES section**

&lt;add key="numiDbConnectionString" value="Data Source= ***VAAUSNUMSQLXX.aac.dva.va.gov*** ;Database= ***NUMI*** ;User ID= ***numi\_user*** ;Password= ***PW Vault under “NUMI Synchronizer PWs (VIARequestingApp)”NOTES section*** ;Trusted\_Connection=False" /&gt;

&lt;add key="reportDbConnectionString" value="Data Source= ***VAAUSNUMSQLXX.aac.dva.va.gov*** ;Database= ***NUMI*** ;User ID= **numi\_user** ;Password= ***PW Vault under “NUMI Synchronizer PWs (VIARequestingApp)”*** NOTES section;Trusted\_Connection=False" /&gt;

1. Restart the service from task manager or the services mmc.
<!-- image -->

### Uninstall:

If you need to uninstall the NUMI Synchronizer services use add/remove programs and right click on the synchronizer.

<!-- image -->

### Validate Installation:

To confirm the synchronizer installation

Open MS SQL Server Management Studio after 2 hours. Open a new query and type:

Use numi go.

Select TOP 1000 * from patientstay.

Click the &lt;Execute&gt; button to run the query. New records shall display.

### Add Jobs to the SQL Server

There are 3 jobs that must be added to the SQL Server:

1. NUMI\_PhysicianAdvisorPatientReview\_AutoExpire
2. LogSynchDB\_ValidateSynchronizer
3. NUMI\_AlterIndex\_Rebuild

These jobs can be installed from scripts (included in the build) or, if you are transferring from another server, you can right click on each job and script as DROP and CREATE.

Backup the jobs before you run the scripts. Modify the scripts to replace the @owner\_login\_name with the owner login name appropriate for your installation, if necessary.

NUMI\_PhysicianAdvisorPatientReview\_AutoExpire is a job that executes the Stored Procedure usp\_PhysicianAdvisorPatientReview\_AutoExpire every day at midnight. The Stored Procedure looks for Physician UM Advisor (PUMA) Reviews that have not been completed within 14 days and marks them as Completed with a reason description of Expired.

LogSynchDB\_ValidateSynchronizer is job that executed the stored procedure LogSyncDB.dbo.usp\_LogSync\_ValidateSynchronizer every hour. This stored procedure confirms imported stays within the last 3 hours and reports the problem to a pre-defined e- mail distribution list determined by the needs of the installation.

NUMI\_AlterIndex\_Rebuild is a job that executes the stored procedure NUMI.dbo.usp\_AlterIndex\_Rebuild. This stored procedure rebuilds the indexes for the tables in the NUMI database.

## Post-Installation Considerations

If there are post-installation considerations for NUMI, this information will be provided by the appropriate project teams.

## Acronyms and Descriptions

| Acronym   | Acronym   | Description                                 | Description                                 |    |
|-----------|-----------|---------------------------------------------|---------------------------------------------|----|
|           |           |                                             |                                             |    |
| CERMe     | CERMe     | Care Enhance Review Management Enterprise   | Care Enhance Review Management Enterprise   |    |
| CPRS      | CPRS      | Computerized Patient Record System          | Computerized Patient Record System          |    |
| CPU       | CPU       | Central Processing Unit                     | Central Processing Unit                     |    |
| HTTP      | HTTP      | HyperText Transfer Protocol                 | HyperText Transfer Protocol                 |    |
| HTTPS     | HTTPS     | HyperText Transfer Protocol Secure          | HyperText Transfer Protocol Secure          |    |
| IAM       | IAM       | Identity and Access Management              | Identity and Access Management              |    |
| IIS       | IIS       | Internet Information Services               | Internet Information Services               |    |
| MDWS      | MDWS      | Medical Domain Web Services                 | Medical Domain Web Services                 |    |
| NUMI      | NUMI      | National Utilization Management Integration | National Utilization Management Integration |    |
| PM        | PM        | Project Manager                             | Project Manager                             |    |
| PUMA      | PUMA      | Physician UM Advisor                        | Physician UM Advisor                        |    |
| QA        | QA        | Quality Assurance                           | Quality Assurance                           |    |
| SQL       | SQL       | Standard Query Language                     | Standard Query Language                     |    |
| SSL       | SSL       | Secure Socket Layer                         | Secure Socket Layer                         |    |
| SSO       | SSO       | Single Sign On                              | Single Sign On                              |    |
| UM        | UM        | Utilization Management                      | Utilization Management                      |    |
| URL       | URL       | Uniform Resource Locator                    | Uniform Resource Locator                    |    |
| VIA       | VIA       | VistA Integration Adaptor                   | VistA Integration Adaptor                   |    |

## Numi Comparison Table

| NUMI Version   |   CERMe RM |   InterQual View |   CA SiteMinder | Windows Server   |   MS SQL Server |
|----------------|------------|------------------|-----------------|------------------|-----------------|
| 15.4           |       16.1 |           2017.2 |           12.51 | 2012 R2          |            2012 |
| 15.5           |       17   |           2018.1 |           12.51 | 2012 R2          |            2012 |
| 15.6           |       17   |           2018.1 |           12.51 | 2012 R2          |            2012 |
| 15.8           |       18.1 |           2019.1 |           12.51 | 2012 R2          |            2012 |
| 15.9           |       19   |           2020   |           12.51 | 2012 R2          |            2012 |
| 15.9.1         |       20   |           2021   |           12.52 | 2019             |            2019 |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: NUMI Server Setup Guide Version 15.14

## ## 15 Installing CERMe Software and Database from CERMe Installation CD

Refer to the RM Install Guide PDF file on the CERMe (COTS product) setup CD for detailed instructions on how to set up CERMe (DBA assistance may be required to setup the database, which must be done before application setup).

### Install CERMe on the Application Server

**NOTE:** Change Healthcare provides version updates several times a year.  The example below may not be the latest version

CERMe Review Manager (RM) 21.0.1 InterQual 2022 for NUMI 15.10 will be installed based on an existing installation of CERMe 20.1. The CERMe installation would be performed using a dump of the existing CERMe 20.1 database. Listed below are the steps to restore the database and install CERME:

1. Restore CERMe 20.1 data from the CERMe database dump obtained from the current CERMe pre-Prod/Production servers. Create database logins for orphaned users in the restored database. Write down the credentials for the new logins created. This will be required for the CERMe install.

Navigate to the CERMe install image and double click the install.htm file in the root directory to open the setup welcome page. This will open the CERMe install page in EDGE Browser.

Click on the Install Review Manager 21.0.1 / InterQual View 2022 link on the installation page. This will prompt to save or run the file, select Run. This will start the CERMe Install wizard.

Accept the license agreement and click Next.

On the License Information screen, enter the license information given above and click Next.

On the Select Review Manager Enterprise screen, select “Review Manager Enterprise” and click Next.

On the Installation Type screen, select “New Installation” and click Next.

Select an installation directory.

On the Choose Components screen, keep the default selection (i.e., all selected) and click Next.

On the Database Information page, enter the following info and click Next.

- Database type: SQL Server
- Server Name: Name of the SQL database server
- Database: Name of the database to which the dump restored in step 1
- Port Number: SQL Server
- Instance: leave blank
- User ID: SQL Server user ID with access to the CERMe database restored above
- Password: Password for the SQL Server user used above

On separate database to store report data screen, select No and click Next.

On the Install Jetty window, select Yes to install Jetty.

On the next screen, enter 8357 for Port Number.

On the next screen, select the hardware architecture.

Review the selections, and click Install to start the installation.

Once the installation completes, go to the URL: http://&lt;servername&gt;:8357/rm/login.

This is should open the CERMe login page.

Now follow the steps below to update CERMe to CERMe 21.0.1.

Stop the CERMe Service from the Windows Services.

Create a backup of the CERMe Installation folder and the CERMe database.

Make the changes to the file (below)on the CERMe Jetty Server:

File: &lt;CERMe Install Folder&gt;\Jetty\etc\webdefault.xml

Add the following element to &lt;session-config&gt; element.

&lt;cookie-config&gt;

&lt;http-only&gt;true&lt;/http-only&gt;

&lt;/cookie-config&gt;

Session Config element should look like the following after the change:

&lt;session-config&gt;

&lt;session-timeout&gt;30&lt;/session-timeout&gt;

**&lt;cookie-config&gt;**

**&lt;http-only&gt;true&lt;/http-only&gt;**

**&lt;/cookie-config&gt;**

&lt;/session-config&gt;

File: &lt;CERMe Install Folder?\Jetty\etc\jetty-rewrite.xml

Add the following &lt;Call&gt; element to the end of the &lt;New&gt; element.

&lt;Call name="addRule"&gt;

&lt;Arg&gt;

&lt;New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"&gt;

&lt;Set name="pattern"&gt;/*&lt;/Set&gt;

&lt;Set name="name"&gt;Strict-Transport-Security&lt;/Set&gt;

&lt;Set name="value"&gt;max-age=31536000; includeSubDomains&lt;/Set&gt;

&lt;/New&gt;

&lt;/Arg&gt;

&lt;/Call&gt;

The file will look like the following after the change:

&lt;Set name="handler"&gt;

&lt;New id="Rewrite" class="org.eclipse.jetty.rewrite.handler.RewriteHandler"&gt;

&lt;Set name="handler"&gt;&lt;Ref refid="oldhandler"/&gt;&lt;/Set&gt;

&lt;Set name="rewriteRequestURI"&gt;&lt;Property name="rewrite.rewriteRequestURI" default="true"/&gt;&lt;/Set&gt;

&lt;Set name="rewritePathInfo"&gt;&lt;Property name="rewrite.rewritePathInfo" default="false"/&gt;&lt;/Set&gt;

&lt;Set name="originalPathAttribute"&gt;&lt;Property name="rewrite.originalPathAttribute" default="requestedPath"/&gt;&lt;/Set&gt;

**&lt;Call name="addRule"&gt;**

**&lt;Arg&gt;**

**&lt;New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"&gt;**

**&lt;Set name="pattern"&gt;/*&lt;/Set&gt;**

**&lt;Set name="name"&gt;Strict-Transport-Security&lt;/Set&gt;**

**&lt;Set name="value"&gt;max-age=31536000; includeSubDomains&lt;/Set&gt;**

**&lt;/New&gt;**

**&lt;/Arg&gt;**

**&lt;/Call&gt;**

&lt;/New&gt;

&lt;/Set&gt;

File: &lt;CERMe Install Folder&gt;\Jetty\start.ini

Add the following new section to the bottom of the file:

### From: NUMI Server Setup Guide

### Microsoft EntraId Application Registration for the Web Server Configuration

Microsoft EntraId is the network based authentication method and pattern used by NUMI. Users must be authenticated with Microsoft EntraId to use NUMI. There are several key configurations from the EntraId Application Registration that need to be in the NUMI Web Server Configuration

#### Microsoft EntraId Application Registration

Each NUMI environment has its own Application Registration. The key values needed are ClientId, TenantId, ClientSecret, and RedirectUri.

The values can be found on the EntraId portal in these sections: REDACTED

Figure 42: Microsoft EntraId Application Registration

<!-- image -->

Figure 43: Application Registration Client Secret

<!-- image -->

Figure 44: EntraId Application Registration Redirect URIs

<!-- image -->

The values are then added to the NUMI Web App Config.

&lt;!-- Microsoft Entra ID (Azure AD) Configuration --&gt;

&lt;add key="owin:AutomaticAppStartup" value="true" /&gt;

&lt;add key="ida:ClientId" value="ceb38826-d7c6-4b02-a886-288e01d3b8a8" /&gt;

&lt;add key="ida:TenantId" value="e95f1b23-abaf-45ee-821d-b7ab251ab3bf" /&gt;

&lt;!--Client expires August 12th 2026 must be changed on the entraid side --&gt;

&lt;add key="ida:ClientSecret" value="REDACTED" /&gt;

&lt;add key="ida:RedirectUri" value=" REDACTED " /&gt;

&lt;add key="ida:PostLogoutRedirectUri" value="REDACTED /" /&gt;

&lt;add key="EntraIdSTSScope" value="api://idev.sts.va.gov/token"/&gt;

Important note, the ClientSecret is only viewable in the portal in the session it was created, it must be copied and passed along. The secret also expires annually.

### Installing CERMe Software and Database from CERMe Installation CD

Refer to the RM Install Guide PDF file on the CERMe (COTS product) setup CD for detailed instructions on how to set up CERMe (DBA assistance may be required to setup the database, which must be done before application setup).

#### Install CERMe on the Application Server

**NOTE:** Change Healthcare provides version updates several times a year.  The example below may not be the latest version

CERMe Review Manager (RM) 21.0.1 InterQual 2022 for NUMI 15.10 will be installed based on an existing installation of CERMe 20.1. The CERMe installation would be performed using a dump of the existing CERMe 20.1 database. Listed below are the steps to restore the database and install CERME:

1. Restore CERMe 20.1 data from the CERMe database dump obtained from the current CERMe pre-Prod/Production servers. Create database logins for orphaned users in the restored database. Write down the credentials for the new logins created. This will be required for the CERMe install.

Navigate to the CERMe install image and double click the install.htm file in the root directory to open the setup welcome page. This will open the CERMe install page in EDGE Browser.

Click on the Install Review Manager 21.0.1 / InterQual View 2022 link on the installation page. This will prompt to save or run the file, select Run. This will start the CERMe Install wizard.

Accept the license agreement and click Next.

On the License Information screen, enter the license information given above and click Next.

On the Select Review Manager Enterprise screen, select “Review Manager Enterprise” and click Next.

On the Installation Type screen, select “New Installation” and click Next.

Select an installation directory.

On the Choose Components screen, keep the default selection (i.e., all selected) and click Next.

On the Database Information page, enter the following info and click Next.

- Database type: SQL Server
- Server Name: Name of the SQL database server
- Database: Name of the database to which the dump restored in step 1
- Port Number: SQL Server
- Instance: leave blank
- User ID: SQL Server user ID with access to the CERMe database restored above
- Password: Password for the SQL Server user used above

On separate database to store report data screen, select No and click Next.

On the Install Jetty window, select Yes to install Jetty.

On the next screen, enter 8357 for Port Number.

On the next screen, select the hardware architecture.

Review the selections, and click Install to start the installation.

Once the installation completes, go to the URL: http://&lt;servername&gt;:8357/rm/login.

This is should open the CERMe login page.

Now follow the steps below to update CERMe to CERMe 21.0.1.

Stop the CERMe Service from the Windows Services.

Create a backup of the CERMe Installation folder and the CERMe database.

Make the changes to the file (below)on the CERMe Jetty Server:

#### File: &lt;CERMe Install Folder&gt;\Jetty\etc\webdefault.xml

Add the following element to &lt;session-config&gt; element.

&lt;cookie-config&gt;

&lt;http-only&gt;true&lt;/http-only&gt;

&lt;/cookie-config&gt;

Session Config element should look like the following after the change:

&lt;session-config&gt;

&lt;session-timeout&gt;30&lt;/session-timeout&gt;

**&lt;cookie-config&gt;**

**&lt;http-only&gt;true&lt;/http-only&gt;**

**&lt;/cookie-config&gt;**

&lt;/session-config&gt;

#### File: &lt;CERMe Install Folder?\Jetty\etc\jetty-rewrite.xml

Add the following &lt;Call&gt; element to the end of the &lt;New&gt; element.

&lt;Call name="addRule"&gt;

&lt;Arg&gt;

&lt;New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"&gt;

&lt;Set name="pattern"&gt;/*&lt;/Set&gt;

&lt;Set name="name"&gt;Strict-Transport-Security&lt;/Set&gt;

&lt;Set name="value"&gt;max-age=31536000; includeSubDomains&lt;/Set&gt;

&lt;/New&gt;

&lt;/Arg&gt;

&lt;/Call&gt;

The file will look like the following after the change:

&lt;Set name="handler"&gt;

&lt;New id="Rewrite" class="org.eclipse.jetty.rewrite.handler.RewriteHandler"&gt;

&lt;Set name="handler"&gt;&lt;Ref refid="oldhandler"/&gt;&lt;/Set&gt;

&lt;Set name="rewriteRequestURI"&gt;&lt;Property name="rewrite.rewriteRequestURI" default="true"/&gt;&lt;/Set&gt;

&lt;Set name="rewritePathInfo"&gt;&lt;Property name="rewrite.rewritePathInfo" default="false"/&gt;&lt;/Set&gt;

&lt;Set name="originalPathAttribute"&gt;&lt;Property name="rewrite.originalPathAttribute" default="requestedPath"/&gt;&lt;/Set&gt;

**&lt;Call name="addRule"&gt;**

**&lt;Arg&gt;**

**&lt;New class="org.eclipse.jetty.rewrite.handler.HeaderPatternRule"&gt;**

**&lt;Set name="pattern"&gt;/*&lt;/Set&gt;**

**&lt;Set name="name"&gt;Strict-Transport-Security&lt;/Set&gt;**

**&lt;Set name="value"&gt;max-age=31536000; includeSubDomains&lt;/Set&gt;**

**&lt;/New&gt;**

**&lt;/Arg&gt;**

**&lt;/Call&gt;**

&lt;/New&gt;

&lt;/Set&gt;

#### File: &lt;CERMe Install Folder&gt;\Jetty\start.ini

Add the following new section to the bottom of the file:

### Installing NUMI Synchronizer on the Web Server

#### Installation Instructions

For a new installation:

- 1.0.0.1. Open CMD in Administrator mode
- 1.0.0.2. Enter ‘cd C:\Windows\Microsoft.NET\Framework\v4.0.30319’
- 1.0.0.3. Enter ‘InstallUtil.exe D:\NUMI\Synchronizer\Synchronizer2.exe’
- 1.0.0.4. View the NUMI Synchronizer service on services.msc
- 1.0.0.5. Close the CMD prompt
- 1.0.0.6. Verify/Update the Synchronizer2.exe.config data

&lt;!-- Service configuration --&gt;

&lt;!-- VistA Service configuration --&gt;

&lt;add key="ServiceURL" value=" REDACTED

&lt;add key="RequestingApp" value="NUMI\_SYNC"/&gt;

&lt;add key="IsSynchronizer" value="true"/&gt;

&lt;add key="WSDLusername" value="vwsl\_numi"/&gt;

&lt;add key="WSDLpassword" value="&lt;PW&gt;"/&gt;

&lt;!--STS Configuration--&gt;

&lt;add key="STSEndpoint" value=" REDACTED

&lt;add key="STSEnabled" value="true"/&gt;

&lt;add key="STSCertificatePath" value="D:\\NUMI\Synchronizer\numisyncsqa.pfx"/&gt;

&lt;add key="STSCertificatePassword" value="&lt;PW&gt;"/&gt;

&lt;!--Database Connections--&gt;

&lt;add key="numiDbConnectionString" value="Data Source=VAAUSSQLNUM###.aac.dva.va.gov;Database=NUMI;User ID=numi\_user;Password=&lt;PW&gt;;Trusted\_Connection=False" /&gt;

&lt;add key="reportDbConnectionString" value="Data Source=VAAUSSQLNUM###.aac.dva.va.gov;Database=NUMI;User ID=numi\_user;Password=&lt;PW&gt;;Trusted\_Connection=False" /&gt;

- 1.0.0.1. Start the service from services.msc

<!-- image -->

For an upgrade in place:

1. Stop the existing service from services.msc
<!-- image -->
2. Copy the Sychronizer distribution folder/files to the intended environment in the NUMI directory. This folder will be provided by Tier 3 maintenance and should be stored on each environment

<!-- image -->

1. Start the service from services.msc
<!-- image -->

#### Uninstall:

If you need to uninstall the NUMI Synchronizer services use services.msc and right click on the synchronizer to stop it. Then right click the Synchronizer and go to properties and disable it. Then open CMD in Admin mode and enter ‘sc delete “NUMI Synchronizer”’.

#### Validate Installation:

To confirm the synchronizer installation

Open MS SQL Server Management Studio after 2 hours. Open a new query and type:

Use numi go.

Select TOP 1000 * from patientstay.

Click the &lt;Execute&gt; button to run the query. New records shall display.

#### Add Jobs to the SQL Server

There are 3 jobs that must be added to the SQL Server:

1. NUMI\_PhysicianAdvisorPatientReview\_AutoExpire
2. LogSynchDB\_ValidateSynchronizer
3. NUMI\_AlterIndex\_Rebuild

These jobs can be installed from scripts (included in the build) or, if you are transferring from another server, you can right click on each job and script as DROP and CREATE.

Backup the jobs before you run the scripts. Modify the scripts to replace the @owner\_login\_name with the owner login name appropriate for your installation, if necessary.

NUMI\_PhysicianAdvisorPatientReview\_AutoExpire is a job that executes the Stored Procedure usp\_PhysicianAdvisorPatientReview\_AutoExpire every day at midnight. The Stored Procedure looks for Physician UM Advisor (PUMA) Reviews that have not been completed within 14 days and marks them as Completed with a reason description of Expired.

LogSynchDB\_ValidateSynchronizer is job that executed the stored procedure LogSyncDB.dbo.usp\_LogSync\_ValidateSynchronizer every hour. This stored procedure confirms imported stays within the last 3 hours and reports the problem to a pre-defined e- mail distribution list determined by the needs of the installation.

NUMI\_AlterIndex\_Rebuild is a job that executes the stored procedure NUMI.dbo.usp\_AlterIndex\_Rebuild. This stored procedure rebuilds the indexes for the tables in the NUMI database.
