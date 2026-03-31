---
title: PATS Installation Guide for EIE group
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: PATS  for EIE group
app_code: QAC
app_name: Patient Advocate Tracking System (PATS)
section: GUI
app_status: active
pkg_ns: QAC
patch_ver: 1.6
patch_id: QAC*1.6
group_key: "QAC:QAC:1.6"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 13%\\" /> <col style=\\"width: 15%\\" /> <col style=\\"width: 44%\\" /> <col style=\\"width: 26%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><strong>Date</strong></td> <td><strong>Revision</strong></td> <td><strong>Description</strong></td> <td><strong>Author</strong></td>"
audience: 
keywords: 
  - pats
  - table
  - contents
  - database
  - application
  - objects
  - server
  - copy
  - installation
  - weblogic
page_count: 0
word_count: 5077
section_count: 14
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Patient_Advocate_Track/pats_1_6_installguideforeie.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Patient_Advocate_Track/pats_1_6_installguideforeie.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=172"
---

![](pats-installation-guide-for-eie-group/001.png)

PATIENT ADVOCATE TRACKING SYSTEM (PATS)INSTALLATION GUIDE FOREIE STAFF

April 2013

Office of Enterprise Development (OED)

Veterans Health Information Technology (VHIT)

*This page is left blank intentionally*Revision History

The following table displays the revision history for this document.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>3-21-07</td>
<td>Initial – 1.0</td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>1-15-08</td>
<td>1.1</td>
<td>Added information in regards to DB patch 1.0.2.2</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6-2-09</td>
<td>1.2</td>
<td>Added information related to KAAJEE upgrade</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7-10-2010</td>
<td>1.3</td>
<td>Revised the document in relation to SDS version and EIE group name changes</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6-08-2011</td>
<td>1.4</td>
<td>Updated the guide with root context information</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11-21-11</td>
<td>1.5</td>
<td><p>Changed the formatting of the document,</p>
<p>Updated Oracle version information</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04-01-13</td>
<td>1.6</td>
<td>Added information regarding the addition of the PAD servlet API</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

  
Table of Contents

# # # # # # # # # # # # # # # # # # # # # # # *This page is left blank intentionally* About this Document


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# # # # # # # # # # # # # # # # # # # # # # This page is left blank intentionally About this Document](#this-page-is-left-blank-intentionally-about-this-document)
  - [Other Resources](#other-resources)
  - [The PATS Installation Process](#the-pats-installation-process)
- [# # # # # # # # # # # # # # # # # # # # # # # This page is left blank intentionally](#this-page-is-left-blank-intentionally)
- [Chapter 1 – Download PATS Compressed File](#chapter-1-download-pats-compressed-file)
- [Chapter 2 – Install the PATS Database](#chapter-2-install-the-pats-database)
  - [Before You Begin](#before-you-begin)
  - [Installation Instructions for Upgrading an Existing PATS Database](#installation-instructions-for-upgrading-an-existing-pats-database)
  - [Installation Instructions for Performing a Full Database Installation](#installation-instructions-for-performing-a-full-database-installation)
- [Chapter 3 – Install the PATS Data Migration Application](#chapter-3-install-the-pats-data-migration-application)
- [## Before You Begin](#before-you-begin-1)
  - [Installation Instructions](#installation-instructions)
    - [Configure the WebLogic Server JMS Queues](#configure-the-weblogic-server-jms-queues)
    - [Copy and Update Health<u>e</u>Vet Configuration Files](#copy-and-update-healthueuvet-configuration-files)
    - [Copy and Deploy the PATS Data Migration Application](#copy-and-deploy-the-pats-data-migration-application)
- [Chapter 4 – Install the PATS Download to VistA Application](#chapter-4-install-the-pats-download-to-vista-application)
- [## Before You Begin](#before-you-begin-2)
  - [Installation Instructions](#installation-instructions-1)
    - [Configure the WebLogic Server JMS Queue](#configure-the-weblogic-server-jms-queue)
    - [Copy and Update Health<u>e</u>Vet Configuration Files](#copy-and-update-healthueuvet-configuration-files-1)
    - [Copy and Deploy the PATS Download to VistA Application](#copy-and-deploy-the-pats-download-to-vista-application)
- [Chapter 5 – Install the PATS Application](#chapter-5-install-the-pats-application)
  - [Before You Begin](#before-you-begin-3)
    - [Ensure the network firewall is configured for PAD messages](#ensure-the-network-firewall-is-configured-for-pad-messages)
  - [Installation Instructions](#installation-instructions-2)
    - [Configure the WebLogic Connection Pool](#configure-the-weblogic-connection-pool)
    - [Configure the WebLogic Data Source](#configure-the-weblogic-data-source)
    - [Copy and Update Health<u>e</u>Vet Configuration Files](#copy-and-update-healthueuvet-configuration-files-2)
    - [1\. In the temporary directory’s etc directory, copy the following files to the Health<u>e</u>Vet configuration directory for the WebLogic domain where PATS will be deployed:](#1-in-the-temporary-directorys-etc-directory-copy-the-following-files-to-the-healthueuvet-configuration-directory-for-the-weblogic-domain-where-pats-will-be-deployed)
    - [Copy and Deploy the PATS Application](#copy-and-deploy-the-pats-application)
- [Chapter 6 – Setting up Business Objects Enterprise Repository](#chapter-6-setting-up-business-objects-enterprise-repository)
  - [Before You Begin](#before-you-begin-4)
  - [Load Objects into the Repository](#load-objects-into-the-repository)
    - [Log onto the BOEXI Central Management Console as the Administrator](#log-onto-the-boexi-central-management-console-as-the-administrator)
    - [Previously Imported PATS Repository Objects](#previously-imported-pats-repository-objects)
    - [Import PATS repository objects for the first time](#import-pats-repository-objects-for-the-first-time)
  - [Verify Import](#verify-import)
    - [Verify repository objects were installed](#verify-repository-objects-were-installed)
    - [Verify database connection information](#verify-database-connection-information)
  - [Add JSP file for Ad Hoc Reporting](#add-jsp-file-for-ad-hoc-reporting)
*Introduction*
The Patient Advocate Tracking System (PATS) provides a way of documenting and tracking patient-related issues.
*The Patient Advocate Tracking System Installation Guide* is intended for individuals in the Enterprise Infrastructure Engineering (EIE) who are responsible for installing the PATS application and its related components. The concepts and step-by-step instructions will help the hosting site install and configure the PATS application.

## *Other Resources*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional PATS documentation resources can be found on the PATS Technical Services Project Repository at: <span class="mark">REDACTED</span>.

Additional PAD project documentation can be found on the PAD Technical Services Project Repository at: <span class="mark">REDACTED</span>

## *The PATS Installation Process*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installing PATS is seven-stage process. Stages 1 – 6 are performed at the EIE. Stage 7 is performed by the IRM staff at field sites.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 59%" />
<col style="width: 31%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p id="stage" class="heading">Stage</p></td>
<td><strong>Process</strong></td>
<td><strong>Role Performing Task</strong></td>
</tr>
<tr class="even">
<td><p id="section-24" class="heading">1</p></td>
<td>Download the PATS compressed file (bundle) and extract it to a temporary directory at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="odd">
<td><p id="section-25" class="heading">2</p></td>
<td>Install the PATS database at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="even">
<td><p id="section-26" class="heading">3</p></td>
<td>Install the PATS Data Migration application at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="odd">
<td><p id="section-27" class="heading">4</p></td>
<td>Install the PATS Download to VistA application at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="even">
<td><p id="section-28" class="heading">5</p></td>
<td>Install the PATS application at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="odd">
<td><p id="section-29" class="heading">6</p></td>
<td>Install and set up Business Objects Enterprise XI at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="even">
<td><p id="section-30" class="heading">7</p></td>
<td>Install the PATS KIDS build at the field sites.</td>
<td>IRM</td>
</tr>
</tbody>
</table>

# # # # # # # # # # # # # # # # # # # # # # # # *This page is left blank intentionally*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Chapter 1 – Download PATS Compressed File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you can begin the installation of PATS, you must download the PATS compressed file (i.e., the bundle) and extract it to a temporary directory. This will create a directory structure with a top level directory named PATS-PKG-n.n.n.nn (n indicates the major, minor, patch and the build number). Inside the extracted directory you will find PATS_nn directory, where nn is the build number. This is a root level for your installation.

# Chapter 2 – Install the PATS Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Before You Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before you can begin the installation process for PATS at the EIE hosting center, verify that the following tasks have been completed:

- Oracle 11g database management system software has been installed on the server where the PATS database will be installed.
- Oracle database has been created on the server.
- SDS Version 18.0 has been installed. The SDS tables must reside in the SDSADM schema on the Oracle database where PATS will be installed.
- Determine whether you are performing an upgrade to an existing PATS database, or whether you are performing a full installation. If you have previously installed the PATS database and data has been loaded into the database, you want to upgrade the existing database instead of performing a full database installation. Performing a full database installation will delete all of the PATS data.

## Installation Instructions for Upgrading an Existing PATS Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Read the Bundle_ReleaseNotes.txt file in the folder created when you extracted the PATS compressed file (top level directory) to see whether the bundle includes a database upgrade. If there is an upgrade, the note includes the words PATS-DB-PATCH-n.n.n.n (e.g., PATS-DB –PATCH-1.0.1.13). Refer to the PATSDB_ReleaseNotes.txt file in the same folder to see what defects are corrected by the upgrade.

> If a bundle contains a PATS database upgrade, the DB folder in PATS_nn contains a zip file for installing the database upgrade (e.g., PATS-DB-PATCH-1.0.2.2.zip). The README file in the DB folder contains instructions for installing the upgrade.

## Installation Instructions for Performing a Full Database Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the PATS database installation, you will install all database structures used by PATS into the Oracle database. The procedure will also load nationally-maintained data into the PATS tables: Contacting Entity, Method of Contact, Treatment Status, Issue Category, Issue Code, and National PATS Parameters.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th>![](pats-installation-guide-for-eie-group/002.png)</th>
<th><p>Read the <strong>Bundle_ReleaseNotes.txt</strong> file in the folder created when you extracted the PATS compressed file to see whether the bundle includes a database upgrade. If there is an upgrade, the note includes the words <strong>PATS- DB- PATCH-n.n.n.n</strong> (e.g., PATS-DB-PATCH-1.0.2.2).</p>
<p>If you have previously installed the PATS database and data has been loaded into your PATS tables, DO NOT perform a full database installation. Instead, see the instructions for Upgrading an Existing PATS Database.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> To install the PATS database, complete the following tasks:

1.  In the root level folder created where you extracted the PATS compressed file, you will see a folder named db. Select that folder.
2.  The db folder contains a zip file containing the full installation of the PATS database including, as well as any upgrades (e.g., PATS-DB-1.0.1.13.zip, PATS-DB-PATCH-1.0.2.2.zip) under respective folders.
3.  Unzip the zip file to a directory of your choosing.
4.  Edit the cr8_pats_tblsp.sql file as needed to update the path information. This should contain the path where the tablespaces for the PATS application will reside on your server, within the Oracle home.

> For example:

> datafile '/u04/oradata/PATSUAT/PATS_DATA.dbf' size 200M

- u04/oradata/ = pathname for the “oradata” directory
- PATSUAT = directory where the tablespace file resides; it should be the same name as your database
5.  If this is the first time PATS has been installed, go to Step 6.

> If this is not the first time PATS has been installed, use the Oracle Enterprise Manager Console to remove existing roles, users, and tablespaces as follows:

> a\. Stop the WebLogic managed servers that have connections to the PATS database to remove the connection between WebLogic and objects in the Oracle tables.

> b\. Remove the following roles: PATSHOST_ROLE and PATSUSER_ROLE.

> Note: If you are prompted that the object is in use, you must drop any connections to the PATS database. To drop the connection, stop and restart  
> the database instance or stop the Oracle jobs that keep these connections open.

> c\. Remove the following users: PATS, PATSHOST, PATSROLLUP, PATSRPTS, PATSUSER.

> Note: You will get an additional warning for PATSRPTS and PATS that the user’s objects will also be removed.

> d\. Remove the following tablespaces: PATSRPTS_DATA, PATSRPTS_NDX, PATS_DATA, PATS_NDX.

> Note: For each tablespace, verify that the box is checked: Delete associated datafiles from the OS.

> e\. Disconnect from the database.

6.  From command mode, navigate to the directory where you unzipped the PATS database scripts.
7.  To connect to SQL Plus, enter sqlplus /nolog.
8.  From the SQL\> prompt, connect as the sysdba by entering:

> connect sys@(your database name\*)as sysdba

> \* If your database name is “PATSUAT.vha.med.va.gov”, you would enter connect sys@PATSUAT.vha.med.va.gov as sysdba

9.  Enter your sysdba password and click Enter.
10. Enter @cr8_pats_tblsp.sql to run the script that creates the table spaces.

> *Result: After the script runs, it logs you off and disconnects from SQLPlus. A log file named PATS_cr8_tablespace.log is created in the directory where you unzipped the PATS installation file.*

> Note: You can check the log file to make sure the tablespaces were created with no errors.

11. Re-connect to SQL PLUS by entering sqlplus /nolog.
12. Enter @build_pats.sql to run the script that will build the rest of the PATS schemas and objects.

> Note: You do not need to connect to the database. The script will prompt you for the information to make the database connections as follows:

- Enter Database Connection Info for your database (e.g., @patsuat.vha.med.va.gov).
- Enter the password for your SYS DBA.

> *Result: A log file named PATS_install.log is created in the directory where you unzipped the installation file.*

13. To verify that the install was correct, check the install log file (PATS_install.log) for errors.
14. You can use the Oracle Enterprise Manager or another DBMS tool such as TOAD to verify that the PATS database structures were properly installed. Detailed information about the PATS objects in the Oracle database can be found in the *PATS Systems Management Guide,* Chapter 5 Database – Oracle.
1.  Verify you have the following roles: PATSHOST_ROLE and PATSUSER_ROLE.
2.  Verify you have the following users: PATS, PATSHOST, PATSROLLUP, PATSRPTS, PATSUSER.
3.  Verify you have the following tablespaces: PATSRPTS_DATA, PATSRPTS_NDX, PATS_DATA, PATS_NDX.
4.  Verify you have the following schemas: PATS, PATSRPTS.
5.  The PATS schema should own tables, sequences, triggers, constraints, indexes, functions, packages and package bodies, and one scheduled job.
6.  Spot check a few PATS national data tables such as treatment_status and issue_code to make sure they contain data.
7.  The PATSRPTS schema should own tables, indexes, constraints, functions, procedures, packages, and two scheduled jobs.

> Note: The script has installed users (see 14b above). The script has set the password for each of those users to passw0rd (0 = zero). You will want to change the password for each of these users after you complete the installation.

> 15\. To support the rollup of data to the Austin VISN Support Service Center (VSSC) for national reporting, a weekly scheduled job has been installed in the PATS schema in your Oracle database. The VSSC will make a connection to your PATS database in order to pull the rollup data as described below. Detailed information about the objects used in the rollup can be found in the *PATS Systems Management Guide,* Chapter 7 Rollup PATS Data to VSSC.

> Note: The VSSC will determine the day of the week and the time the rollup will occur. The VSSC also needs to let the EIE know when they are ready to start pulling rollup data from PATS. Do not enable the scheduled job to build the rollup data until the VSSC is ready to pull that data from the first site.

1.  The job named BUILD_ROLLUP_DATA_JOB builds the weekly rollup data into the table pats.pats_rollup_natl_data. It will be disabled when you receive it (Enabled = FALSE); you must enable the job to start the rollup. This job is currently scheduled to run at 6:00 PM Eastern time but can be rescheduled, if necessary.
2.  Give the VSSC information from the TNSNAMES.ORA file for your database, including the IP address for your server and the port. They will need this in order to make a connection to your database.
3.  To facilitate this data pull, a special user PATSROLLUP has been created in your Oracle database. This user has SELECT access only to the pats.pats_rollup_natl_data table. Give the VSSC the password to sign on as the PATSROLLUP user.
4.  The VSSC will pull the rollup data once a week on a date and time agreed upon between VSSC and the EIE.

> 16\. To support ad hoc reporting, a nightly scheduled job has been installed in the PATSRPTS schema in your Oracle database. The job is named BUILD_ROC_ADHOC_DATA_JOB. It will be enabled after the installation of the PATS database. You can leave it enabled as it refreshes data in the ROC_COMBO_DATA_VIEW table that is used to support the WEBI Universe used for ad hoc reporting.

> 17\. To support standard reporting, a nightly scheduled job has been installed in the PATSRPTS schema in your Oracle database. The job is named BUILD_STD_REPORT_DATA_JOB. It will be enabled after the installation of the PATS database. You can leave it enabled as it refreshes data in all of the tables that support the standard reports.

| ![](pats-installation-guide-for-eie-group/003.png) | Note to the Oracle Data Base Administrator: The tablespaces and datafiles used by the PATS application (PATS_DATA, PATS_NDX, PATSRPTS_DATA and PATSRPTS_NDX) are initialized by running these scripts. You need to monitor and increase the storage size as sites add data to the PATS tables. |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# Chapter 3 – Install the PATS Data Migration Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ## Before You Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before you begin the PATS Data Migration application installation, verify that the following applications have been installed:

- VistALink 1.5.2.004
- KAAJEE SSPI Version 1.0.1.003
- WebLogic server 8.1 sp4 (or higher SP level)
- Oracle RDBMS version 11g

> In addition: Create a WebLogic user account with administrative privileges (if one doesn’t already exist) named weblogic with password weblogic.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: The following instructions are the necessary steps required to deploy PATS Data Migration. The application is deployed as an exploded enterprise archive to a single WebLogic server instance.

> To install the Data Migration application, complete the following tasks:

1.  Configure the WebLogic Server JMS queues
2.  Copy and update Health*<u>e</u>*Vet configuration files
3.  Copy and deploy the PATS Data Migration application

### Configure the WebLogic Server JMS Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To add the PATS DM JMS server, use the WebLogic console and navigate to Services \> JMS \> Servers folder. Select *Configure a new JMS Server*.
2.  Name: Enter PATS Data Migration JMS Server

> Note: Accept the default value of all other parameters on the page.

3.  Click Create.
4.  Under the Target and Deploy tab for this JMS server, target the JMS server to a WebLogic instance where PATS DM will be deployed.
5.  Click Apply.
6.  You need to add two JMS queues. Go to the Destinations folder for the newly created JMS server and select *Configure a new JMS Queue*.
7.  Name: Enter a descriptive name for the queue.

> JNDI Name: Enter jms.PATSDMQ

> Note: Accept the default value of all other parameters on the page.

8.  Click Create.
9.  Repeat Steps 6 and 7 to create the second JMS queue.
10. JNDI Name: Enter jms.PATSInstitutionDeleteQueue
11. Click Create.
12. To verify that the queues have been successfully created, complete the following:
1.  Select the WebLogic server where you deployed the JMS Server.
2.  Right click the server name.
3.  Select *View JNDI tree*.

> *Result: A pop-up window displays.*

4.  Expand the JMS folder to see the queues you created.

### Copy and Update Health*<u>e</u>*Vet Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: Contact the DBA responsible for installing the PATS database to obtain the necessary connection information for the database.

1.  Copy the gov.va.med.pats.migration.db.oracle.properties file from the etc folder in the temporary directory to the Health*<u>e</u>*Vet configuration directory.
2.  In the Health*<u>e</u>*Vet configuration directory, you must edit fields in the gov.va.med.pats.migration.db.oracle.properties configuration file. The properties file has comments that instruct you which fields to edit. This file contains information used to connect to the Oracle database during data migration. Note that directory location and file names are case sensitive.
3.  The root logger for PATSDM is gov.va.med.pats.migration. Add this logger and the corresponding appender to the log4j configuration file on the server where PATSDM will be deployed. Add the logger entry to the logger section of the log4j configuration file, and add the appender entry to the appender section.

> \<logger name="gov.va.med.pats.migration" additivity="false"\>  
> \<level value="debug"/\>  
> \<appender-ref ref="patsdmDailyFileAppender"/\>  
> \</logger\>

> \<appender name="patsdmDailyFileAppender"

> class="org.apache.log4j.DailyRollingFileAppender"\>

> \<param name="file"

> value="(your path to the log area)/patsdm.log"/\>

> \<layout class="org.apache.log4j.PatternLayout"\>

> \<param name="ConversionPattern"

> value="%d %-5p \[%t\] %C{2} (%F:%L) - %m%n"/\>

> \</layout\>

> \</appender\>

4.  Restart the server where PATSDM is deployed.

> Note: Log4j changes will be made to PATS, PATSDV and PATSDM. You can wait to restart the server until all changes have been made.

### Copy and Deploy the PATS Data Migration Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Copy the PATS Data Migration enterprise archive file  
    PATS-DM-1.0.0.3.ear from the temporary directory to the application deployment directory in the WebLogic domain where PATSDM will be deployed.
2.  Update the kaajeeConfig.xml to accommodate your environment.

> a\. Uncompress (explode) the ear file in the application deployment directory.

- For Windows: Right-click on the file, choose Open With…, select WinZip.
- For Unix/Linux: Extract the ear file using one of the following instructions:

> − On the command line, enter unzip filename,

> OR

> − For RedHat Linux: Double click on the ear file; File Roller automatically comes up. Select Extract to decompress the archived file.

> Note: After you explode the ear file, move the ear file to a directory outside the deployment directory.

> b\. Open the patsdm\\WEB-INF folder.

> c\. Edit the kaajeeConfig.xml file adding the appropriate site numbers and save it.

> Note: For instructions, see the *KAAJEE Installation Guide for Weblogic Application Server* (*kaajee_1.0.1.xxx_installguide)*

> Note: For the data migration application, you only need to add the 3-digit default institution number. You do not need to add any of the divisions within the default institution.

> 3\. In the WebLogic console, navigate to Deployments\>Applications folder and select *Deploy a new Application*.

> 4\. Browse to the directory where you copied the PATS Data Migration application.

> 5\. Select the application deployment directory for the PATS Data Migration application and click Target Application.

> 6\. On the Deploy an Application page, select the server where PATS Data Migration will be deployed.

> 7\. Click Continue.

> 8\. In the Source Accessibility section, click the appropriate radio button:

- Copy this application onto every target for me (default)
- I will make the application accessible from the following location

> 9\. In the Identity section, Name: Enter or accept the directory where you uncompressed the PATS ear file and click Deploy.

> Note: If the name has any spaces, remove them before you deploy (spaces in the name will cause errors.)

> 10\. After a few seconds, Status of Last Action for each module should read <u>Success</u>.

> 11\. To verify the deployment was successful, complete the following tasks:

1.  Click Web Module PATS DM.
2.  Click the Testing tab.
3.  Click one of the URLs.

> *Result: The PATS Data Migration logon screen appears.*

# Chapter 4 – Install the PATS Download to VistA Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ## Before You Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Refer to the Before You Begin instructions in Chapter 3, *Install the PATS Data Migration Application*.
- Install the PATS Data Migration Application using instructions in Chapter 3, *Install the PATS Data Migration Application*.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: The following instructions are the necessary steps required to deploy the PATS Download to VistA application. The application is deployed as an exploded enterprise archive to a single WebLogic server instance.

> To install the Download to VistA application, complete the following tasks:

1.  Configure the WebLogic Server JMS queues
2.  Copy and update Health*<u>e</u>*Vet configuration files
3.  Copy and deploy the PATS Download to VistA application

### Configure the WebLogic Server JMS Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To add the PATS DV JMS server queue, use the WebLogic console and navigate to Services \> JMS \> Servers folder. Select *Configure a new JMS Server*.
2.  Name: Enter PATS Download to Vista JMS

> Note: Accept the default value of all other parameters on the page.

3.  Click Create.
4.  Under the Target and Deploy tab for this JMS server, target the JMS server to a WebLogic instance where PATS DV will be deployed.
5.  Click Apply.
6.  You need to add a JMS queue. Go to the Destinations folder for the newly created JMS server and select *Configure a new JMS Queue*.
7.  Name: Enter a descriptive name for the queue.

> JNDI Name: Enter jms/PATSDVQ

> Note: Accept the default value of all other parameters on the page.

8.  Click Create.
9.  To verify that the queue has been successfully created, complete the following:
1.  Select the WebLogic server where you deployed the JMS Server.
2.  Right click the server name.
3.  Select *View JNDI tree*.

> *Result: A pop-up window displays.*

4.  Expand the JMS folder to see the queue you created.

### Copy and Update Health*<u>e</u>*Vet Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: Contact the DBA responsible for installing the PATS database to obtain the necessary connection information for the database.

The Download to VistA application uses the same configuration files as the PATS Data Migration Application. After you install the PATS Data Migration application, complete the following instructions to copy and deploy the PATS Download to VistA application.

1.  The root logger for PATSDV is gov.va.med.pats.download. Add this logger and the corresponding appender to the log4j configuration file on the server where PATSDV will be deployed. Add the logger entry to the logger section of the log4j configuration file, and add the appender entry to the appender section.

> \<logger name="gov.va.med.pats.download" additivity="false"\>  
> \<level value="debug"/\>  
> \<appender-ref ref="patsdvDailyFileAppender"/\>  
> \</logger\>

> \<appender name="patsdvDailyFileAppender"

> class="org.apache.log4j.DailyRollingFileAppender"\>

> \<param name="file"

> value="(your path to the log area)/patsdv.log"/\>

> \<layout class="org.apache.log4j.PatternLayout"\>

> \<param name="ConversionPattern"

> value="%d %-5p \[%t\] %C{2} (%F:%L) - %m%n"/\>

> \</layout\>

> \</appender\>

2.  Restart the server where PATSDV is deployed.

> Note: Log4j changes will be made to PATS, PATSDV and PATSDM. You can wait to restart the server until all changes have been made.

### Copy and Deploy the PATS Download to VistA Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Copy the PATS Download to VistA enterprise archive file  
    patsdv-1.0.0.2.ear from the temporary directory to the application deployment directory in the WebLogic domain where PATSDV will be deployed.
2.  Update the kaajeeConfig.xml to accommodate your environment.

> a\. Uncompress (explode) the ear file in the application deployment directory.

- For Windows: Right-click on the file, choose Open With…, select WinZip.
- For Unix/Linux: Extract the ear file using one of the following instructions:

> − On the command line, enter unzip filename,

> OR

> − For RedHat Linux: Double click on the ear file; File Roller automatically comes up. Select Extract to decompress the archived file.

> Note: After you explode the ear file, move the ear file to a directory outside the deployment directory.

> b\. Open the patsdv\\WEB-INF folder.

> c\. Edit the kaajeeConfig.xml file adding the appropriate site numbers and save it.

> Note: For instructions, see the *KAAJEE Installation Guide for Weblogic Application Server* (*kaajee_1.0.1.xxx_installguide)*.

> Note: For the Download to VistA application, you only need to add the 3-digit default institution number. You do not need to add any of the divisions within the default institution.

> 3\. In the WebLogic console, navigate to Deployments\>Applications folder and select *Deploy a new Application*.

> 4\. Browse to the directory where you copied the PATS Download to VistA application.

> 5\. Select the application deployment directory for the PATS Download to VistA application and click Target Application.

> 6\. On the Deploy an Application page, select the server where PATS Download to VistA will be deployed.

> 7\. Click Continue.

> 8\. In the Source Accessibility section, click the appropriate radio button:

- Copy this application onto every target for me (default)
- I will make the application accessible from the following location

> 9\. In the Identity section, Name: Enter or accept the directory where you uncompressed the ear file and click Deploy.

> Note: If the name has any spaces, remove them before you deploy (spaces in the name will cause errors).

> 10\. After a few seconds, Status of Last Action for each module should read <u>Success</u>.

> 11\. To verify the deployment was successful, complete the following tasks:

1.  Click Web Module PATS DV.
2.  Click the Testing tab.
3.  Click one of the URLs.

> *Result: The PATS Download to VistA logon screen appears.*

# Chapter 5 – Install the PATS Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Before You Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before you begin the PATS application installation, verify that the following applications have been installed:

- VistALink 1.5.2.004
- KAAJEE SSPI Version 1.0.1.003
- Patient Service Lookup Version 4.0.4.3 (EJB only)
- Person Service Construct Version 2.0.0.8 (EJB only)
- WebLogic server 8.1 sp4 (or higher SP level)
- Oracle RDBMS version 11g

> Download the PATS compressed file and extract it to a temporary directory.

### Ensure the network firewall is configured for PAD messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PAD servlet API functionality in PATS depends on successful XML SOAP communication between the external Inquiry Routing and Information System (IRIS) and the PATS server. The VA firewall must be configured to allow incoming requests to the PAD servlet URL to be passed through to the PATS server.

> IRIS-PAD SOAP Communication Exchange

> ![](pats-installation-guide-for-eie-group/004.png)

> Coordinate with the PATS system administrator and the VA NSOC to ensure existing FQDN fowarding rules and server certificates are valid for this installation. If changes to the request FQDN are required, ensure the IRIS system administrator is provided the public FQDN configured in the firewall settings in order to initiate the request to the PATS server.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: The following instructions are the necessary steps required to deploy PATS. The application is deployed as an exploded enterprise archive to a WebLogic cluster.

> To install the PATS application, complete the following tasks:

1.  Configure the WebLogic connection pool
2.  Configure the WebLogic data source
3.  Copy and update Health*<u>e</u>*Vet configuration files
4.  Copy and deploy the PATS application

### Configure the WebLogic Connection Pool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: Contact the DBA responsible for installing the PATS database to obtain the necessary connection information for the database.

1.  To add the PATS Connection pool, use the WebLogic console and navigate to Services \> JDBC \> Connection Pools folder. Select *Configure a new JDBC Connection Pool*.
2.  Database Type: Select *Oracle*.
3.  Database Driver: Select \Oracle’s Driver (Thin) Versions 9.0.1,9.2.0,10.*
4.  Click Continue.
5.  Name: Enter PATS Connection Pool(the name of the new connection).
6.  Database Name: Enter the name of the Oracle database you want to connect to.
7.  Host Name: Enter the name or IP address of the database server.
8.  Port: Enter the Port number. (Oracle’s default port number is 1521.)
9.  Database User Name: Enter patsuser (the database user name used in the physical database connection).
10. Password: Enter the password you have assigned to patsuser.
11. Confirm Password: Enter the user password again to confirm.
12. Click Continue.
13. You have the option to test the connection pool configuration.
- If you don’t want to do test the configuration, click Skip this Step.
- To test the configuration, click Test Driver Configuration.
14. Targets: Target the cluster to deploy the new connection pool.
15. Click Createanddeploy.
16. On the JDBC Connection Pools page, the Deployed column should display true (the connection was successful).

> Note: You need a JDBC Connection Pool for SDS. For instructions, see the *SDS Server Administrator Installation Guide*, section 2.5.

### Configure the WebLogic Data Source

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To add the PATS Data Source, use the WebLogic console and navigate to Services \> JDBC \> Data Sources option. Select *Configure a new JDBC Data Source*.
2.  Name: Enter PATS Data Source (the name of the new data source).
3.  JNDI Name: Enter jdbc.PATSUSER (the JNDI name for the new data Source).
4.  Click Continue.
5.  Pool Name: From the drop down list, select the connection pool created in the previous section.
6.  Click Continue.
7.  Targets: Select a target cluster to deploy the new data source.
8.  Click Create.

> Note: You need a JDBC Data Source for SDS. For instructions, see the *SDS Server Administrator Installation Guide*, section 2.5.

### Copy and Update Health*<u>e</u>*Vet Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### 1\. In the temporary directory’s etc directory, copy the following files to the Health*<u>e</u>*Vet configuration directory for the WebLogic domain where PATS will be deployed:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- gov.va.med.pats.businessobjects.enterprise.properties
- gov.va.med.pats.notification.properties
- gov.va.med.pats.application.properties

> 2\. In the Health*<u>e</u>*Vet configuration directory, you must edit fields in the gov.va.med.pats.businessobjects.enterprise.properties configuration file. The properties file has comments that instruct you which fields to edit. This configuration file is used to manage Business Objects properties for PATS Standard and Ad Hoc reporting. Note that directory location and file names are case sensitive.

> 3\. In the Health*<u>e</u>*Vet configuration directory, you must edit fields in the gov.va.med.pats.notification.properties configuration file. The properties file has comments that instruct you which fields to edit. This file is used by the PATS Notification subsystem. Properties in this file are used by PATS to connect to an LDAP server to send PATS Notifications via Outlook mail, to look up users in the Global Address List (GAL), and to automatically build the information in the Notification mail messages. Note that directory location and file names are case sensitive.

> 4\. In the Health*<u>e</u>*Vet configuration directory, you must edit one field in the gov.va.med.pats.application.properties configuration file. Edit the ROC.business.rule.year property value from 2008 to 2007.

> 5\. The root logger for pats is gov.va.med.pats. Add this logger and the corresponding appender to the log4j configuration file for the server PATS will be deployed to. Add the logger entry to the logger section of the log4j configuration file, and add the appender entry to the appender section.

> \<logger name="gov.va.med.pats" additivity="false"\>  
> \<level value="debug"/\>  
> \<appender-ref ref="patsDailyFileAppender"/\>  
> \</logger\>

> \<appender name="patsDailyFileAppender"

> class="org.apache.log4j.DailyRollingFileAppender"\>

> \<param name="file"

> value="(your path to the log area)/pats.log"/\>

> \<layout class="org.apache.log4j.PatternLayout"\>

> \<param name="ConversionPattern"

> value="%d %-5p \[%t\] %C{2} (%F:%L) - %m%n"/\>

> \</layout\>

> \</appender\>

> Note: Log4j changes will be made to PATS, PATSDV and PATSDM. You can wait to restart the server until all changes have been made.

> 6\. Restart the server where PATS will be deployed.

### Copy and Deploy the PATS Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. Copy the PATS enterprise archive file (ear) from the temporary directory to the application deployment directory in the WebLogic domain where PATS will be deployed.

> 2\. Update the kaajeeConfig.xml to accommodate your environment.

> a\. Uncompress (explode) the ear file in the application deployment directory.

- For Windows: Right-click on the file, choose Open With…, select WinZip.
- For Unix/Linux: Extract the ear file using one of the following instructions.

> − On the command line, enter unzip filename.

> OR

> − For RedHat Linux: Double click on the ear file; File Roller automatically comes up. Select Extract to decompress the archived file.

> Note: After you explode the ear file, move the ear file to a directory outside the deployment directory.

> b\. Open the PATS\\WEB-INF folder.

> c\. Edit the kaajeeConfig.xml file adding the appropriate site numbers and save it.

> Note: The *PATS Installation Guide for IRM Staff* instructs the sites to send you a list of station numbers generated from their MEDICAL CENTER DIVISION file.

> Note: For instructions see the *KAAJEE Installation Guide for Weblogic Application Server* (*kaajee_1.0.1.xxx_installguide)*.

3\. Update the patsweb.properties file to configure the PAD servlet

a\. Open the PATS/WEB-INF folder

b\. Edit the patsweb.properties file and set the property for “iris.ips” to include the production IP address for the IRIS server that will be sending ROCs to PATS

c\. Set the patsweb.properties file property for “enable.pad.tools” to false.

4\. In the WebLogic console, navigate to Deployments\>Applications folder and select *Deploy a new Application*.

> 5\. Browse to the directory where the PATS application was copied.

> 6\. Select the application deployment directory where you uncompressed the PATS ear file and click Target Application.

> 7\. On the Deploy an Application page, select the cluster where you want to deploy PATS.

> 8\. Click Continue.

> 9\. Identity section, Name: Enter or accept the directory where you uncompressed the PATS ear file and click Deploy.

> Note: If the name has any spaces, remove them before you deploy (spaces in the name will cause errors.)

> 10\. Click Deploy.

> 11\. After a few seconds, Status of Last Action for each module should read <u>Success</u>.

> 12\. To verify the deployment was successful, complete the following tasks:

1.  Click Web Module PATS
2.  Click the Testing tab.
3.  Click one of the URLs.

> *Result: The PATS logon screen appears.*

# Chapter 6 – Setting up Business Objects Enterprise Repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Business Objects Repository objects for the PATS application cannot be deployed in the zip file with the rest of the application. In order to populate your local Business Objects Repository with the PATS objects (report files, universe, universe connection), you must use the Business Objects Import tool.

## Before You Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before starting these steps verify that the following packages have been installed on your reports server:

- Business Objects Enterprise XI with SP1 (BOEXI) including the Tomcat J2EE server
- Oracle 11g Client software

> For detailed documentation on the BOEXI Import Wizard, *in the PATS TSPR* <span class="mark">REDACTED</span> see the *BOEXI Administrative Guide,* Chapter 16 (Importing Objects to Business Objects Enterprise, in the section called Importing with the Import Wizard).

## Load Objects into the Repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The BOEXI Import Wizard will be used to import the objects needed for PATS standard and ad hoc reporting into the BOEXI Repository. This includes a user group, folders, report objects (templates) for standard reports; the universe connectors and universe to be used for ad hoc reporting; and the access rights structure for PATS users.

> Detailed information about the objects in the repository can be found in the *PATS Systems Management Guide,* Chapter 6 Business Objects XI*.*

### Log onto the BOEXI Central Management Console as the Administrator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Start\>All Programs\>BusinessObjects 11\>BusinessObjects Enterprise\> BusinessObjects Enterprise Java Administration Launchpad.
2.  Select Central Management Console to display the Central Management Console (CMC) logon window.

### Previously Imported PATS Repository Objects 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you previously imported the PATS repository objects, you should delete the following repository objects prior to performing the import a subsequent time.

1.  Log onto the CMC as the Administrator.
2.  Delete the following objects:
- Users: Delete all users whose Account Name begins with PATS.
- Groups: Delete PATS_REPORTS_GROUP.
- Universe Connections: Delete older PATS Oracle 10G or newer PATS Oracle 11g.
- Universes: Delete PATS Universe.
- Folders: Delete PATS.

### Import PATS repository objects for the first time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you’re importing the repository objects for the first time, complete the following tasks from the destination server:

1.  From the Business Objects Enterprise program group, select Import Wizard.
2.  Specify source environment
    1.  From the Source list, select BusinessObjects Enterprise XI (Note: this may say BusinessObjects Enterprise 11 depending on the version you’re running).
    2.  CMS Name: Enter the name of the source server the PATS developers gave to you.
    3.  User Name: Enter Administrator.
    4.  Password: Enter the password the PATS developers gave to you.
    5.  Click Next.
3.  Specify destination environment
    1.  CMS Name: Enter the name of the EIE server where BOEXI is installed.
    2.  User Name: Enter Administrator.
    3.  Password: Enter the password the EIE uses to log on to BOEXI as the administrator.
    4.  Click Next.
4.  Choose objects to import

> Specify the categories of objects to import. *Check only boxes that are specified below; uncheck all other boxes.*

1.  Check Import users and user groups; uncheck all of the subcategories except for Import applications rights. Leave Import applications rights checked.
2.  Check Import folders and objects; uncheck the subcategory.
3.  Check Import repository objects.
4.  Check Import universes.
5.  Uncheck all other boxes.
6.  Click Next.
5.  Import universe and connection objects options

> Since you’re importing universes, BOEXI wants to know whether to import all universes or just those referenced by WEBI reports. Because this is an ad hoc tool, the WEBI reports are not pre-defined.

1.  Click the radio button next to Import all universe and connection objects.
2.  Click Next.
6.  Import Object Principals Option

> This section controls how users or groups are assigned rights to the objects being sent. You want to guarantee that the rights assigned to users within the new PATS_REPORTS_GROUP group on the destination system match those from the source system.

1.  Check the Enforce rights fidelity box. This will preserve the rights from the source system.
2.  Click Next.
7.  Please choose an import scenario

> This section tells BOEXI what to do if objects are brought in from the source, and the same objects already exist on the destination system.

1.  Check I want to update the destination system by using the source system as a reference. This will cause objects from the source system to overwrite objects in the destination system that have the same unique identifier.
2.  Uncheck the box that says Automatically rename objects if an object with that title already exists in the destination folder. This will cause the copy of an object to fail if the object has the same title as an existing object in the same folder, but has a different unique internal identifier.
3.  Click Next.
8.  Select Users and Groups

> You are allowed to specify individually the groups and users you want to import.

1.  From the Groups section, check the PATS_REPORTS_GROUP. Under the Subgroups and Users for that group, *leave at least one user checked in order to include the group in the import*. *Delete that user from your repository after completing the import.*
2.  From the Groups section, check the Administrators group. Under the Subgroups and Users for that group, leave the Administrator user checked.
3.  From the Groups section, check the Universe Designer Users groups.
4.  Click Next.
9.  Select Folders and Objects

> You are allowed to specify individually the folders and the objects within them that you want to import.

1.  Check and expand the PATS folder.
2.  The system automatically checks the PATS Reports subfolder, and all subfolders/reports within it. Leave all of these checked so that the templates for all the standard reports will be imported to the destination repository.
3.  Check and expand the Ad Hoc subfolder. *Uncheck* any ad hoc reports created under that subfolder. Any ad hoc reports in this folder are test reports and should not be imported to the destination repository.
4.  Leave the box Import all instances of each selected report and object package unchecked. Instances are results from running the reports. Any instances in the source repository are test results and should not be imported to the destination repository.
5.  Click Next.
10. Import repository objects options

> Repository objects are standard objects that can be used in multiple reports to provide a consistent look and feel (such as the standard header on standard reports).

1.  Click the radio button next to Import repository objects that the selected reports use directly, as well as any other repository objects they depend on.
2.  Click Next.
11. When the Information Collection Complete dialogue box appears and the Finish button is no longer greyed-out, click Finish to begin importing the information.
12. Monitor the progress: As the import is taking place, you will see a progress screen showing each of the categories of repository items being imported. On the left hand side you’ll see a count of the items as they’re imported, on the right you’ll see a count of warnings.
13. View the detail log: After the import finishes, you can click the button to view the detail log. Detailed information about any warnings that occurred during the import will appear in the log.

> Note: You may see one warning under e-Portfolio. The warning says: Failed to set object security. Reason: Application object is not found in the destination system. Since e-Portfolio isn’t running, this error is not a problem. Report any other errors to the PATS development team.

14. Click Done to close the Import window.
15. Give PATS_REPORTS_GROUP access to PATS Universe
1.  Log onto the Central Management Console (CMC) as the Administrator as described at the beginning of this section.
2.  From the CMC home page, select Universes\>PATS Universe.
3.  Select the Rights tab.
4.  Select Add/Remove.
5.  Select the Operation Add/Remove Groups and move the PATS_REPORTS_GROUP from the list of available groups on the left to the Groups with an access level for PATS Universe.
6.  Click OK.
7.  From the drop-down list under the Access Level heading for the PATS_REPORTS_GROUP, select View on Demand.
8.  Click Update.
16. Delete users transferred from development repository
1.  Return to the CMC home page.
2.  Select Users
3.  Delete any users that were imported from the development server by selecting the check box beside the users name and clicking the Delete button.

> Note: As new users log onto PATS, they will automatically be added to the BOEXI repository as a user within the PATS_REPORTS_GROUP. This will give them access to all of the PATS reports and to the PATS Universe. Each of the programmatically created users will be given the same password which will never change. DO NOT alter this password or other user data. If you delete a user, all the reports in the user’s private folder will also be deleted.

17. Restart the Business Objects Servers: Log on to the Business Objects Central Configuration Manager and restart all of the servers.

## Verify Import

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Verify repository objects were installed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After importing the objects into the Business Objects Repository, check to make sure that the objects have been imported successfully. Detailed information about the setup of all the PATS objects in the repository can be found in the *Patient Advocate Tracking System (PATS) Systems Management Guide,* Repository and Central Management Console section within the Business Objects XI chapter.

### Verify database connection information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You must verify that the database connection information for standard reports and the ad hoc universe connection all reference your database. Prior to the Import at the EIE, the PATS developers will change all of the database connection information that previously pointed to the PATS development database, to point to the EIE database.

1.  In the CMC, navigate to each of the standard reports and verify that the database source references your Oracle database. Run a preview of each report to verify that you can connect to the database and that the password is correct. For more information, see the *PATS Systems Management Guide (Business Objects XI* chapter*, Canned Report Database Source* section)*.*
2.  Open the Business Objects XI Designer by navigating to Start\>All Programs\>BusinessObjects 11\>BusinessObjects Enterprise\>Designer.
3.  Verify that the Universe Connection Pats Oracle 10G references your Oracle database.
    1.  Select Tools\>Connections.
    2.  Select PATS Oracle 10g Connection.
    3.  Click Edit; the first screen shows the database information.
    4.  Edit the information or Click Cancel to exit.

> For more information, see the *PATS Systems Management Guide* (*WebIntelligence* chapter*, Universe Connection* section)*.*

## Add JSP file for Ad Hoc Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for Ad hoc reporting to work correctly, the openQueryPanelWithToken.jsp file must be added to the Tomcat home on the server where Business Objects Enterprise XI was installed. This jsp file is needed to seamlessly integrate WebIntelligence into PATS. The Tomcat home is the location where Tomcat was deployed—usually into a folder named Tomcat. The Tomcat home is referred to below as \<path_to_tomcat\>.

To add the openQueryPanelWithToken.jsp file:

> 1\. Open the Tomcat folder that was created when you unzipped the PATS application. In the tomcat folder, you will see the webapps.exe file. The openQueryPanelWithToken.jsp file is contained within this zip file.

2.  Follow the instructions below to install the file openQueryPanelWithToken.jsp in the path \<path_to_tomcat\>/webapps/businessobjects/enterprise11/desktoplaunch/ viewers/cdz_adv.
    1.  Double-click webapps.exe.
    2.  Set the Unzip to folder to the \<path_to_tomcat\>.
    3.  Leave Overwrite files without prompting checked.
    4.  Click Unzip.
    5.  Click OK.
    6.  Click Close.
    7.  Verify the file called openQueryPanelWithToken.jsp is located in the /cdz_adv directory in the path mentioned above.

> Note: After completing the instructions in this chapter, the Business Objects Repository objects for PATS will be installed and configured on your local server. However, before the PATS application will be able to access this repository, you must configure the information in the PATS properties file gov.va.med.pats.businessobjects.enterprise.properties as documented in Chapter 2.