---
title: PSO*7*521 Java-FDA Medication Guides Automatic Printing Project Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Java-FDA Medication Guides Automatic Printing Project
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*521
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: This Installation Guide provides a description of the installation and deployment procedures for the Department of Veterans Affairs (VA) Food and Drug Administration (FDA) Medication Guides Increment 3 project. This section focuses on the project’s Java FDA Med Guides Printer Tool. The FDA Med Guide
audience: 
keywords: 
  - guides
  - installation
  - java
  - table
  - contents
  - figure
  - task
  - printing
  - automatic
  - account
page_count: 0
word_count: 7685
section_count: 26
table_count: 11
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/PHAR_FDA_MED_GUIDE_AUTO_PSO_7_521_IG.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/PHAR_FDA_MED_GUIDE_AUTO_PSO_7_521_IG.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>FDA Medication Guides Project

  Automatic Printing

  Java Component

  <span id="_Toc78348893" class="anchor"></span>INSTALLATION GUIDE
---

![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/001.png)

XU\*8\*566

PSN\*4\*264

PSO\*7\*367

PSX\*2\*70

PSS\*1\*177

PSN\*4\*364

PSO\*7\*428

PSO\*7\*439

PSO\*7\*483

PSO\*7\*489

PSO\*7\*521

April 2018

Version 1.0.1.0

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Pre-installation Considerations](#pre-installation-considerations)
  - [Deployment scenarios](#deployment-scenarios)
  - [Destination printers](#destination-printers)
  - [Third-party software Pre-requisites](#third-party-software-pre-requisites)
    - [Windows Server 2012 or 2008](#windows-server-2012-or-2008)
    - [Java Runtime Environment Version 1.8 for Windows](#java-runtime-environment-version-18-for-windows)
    - [### Adobe Acrobat Reader DC version 18 for Windows](#adobe-acrobat-reader-dc-version-18-for-windows)
  - [## Domain Service Account](#domain-service-account)
    - [Create Domain Service Account for FDA Med Guides](#create-domain-service-account-for-fda-med-guides)
- [Deployment package contents](#deployment-package-contents)
- [Installation Procedure](#installation-procedure)
  - [Obtain ZIP distribution file](#obtain-zip-distribution-file)
  - [Deploy files from the distribution file](#deploy-files-from-the-distribution-file)
    - [Extract ZIP file contents into C:\\](#extract-zip-file-contents-into-c)
  - [Edit the properties configuration file](#edit-the-properties-configuration-file)
    - [Verify path to Adobe Reader program](#verify-path-to-adobe-reader-program)
    - [Confirm DailyPurgeTime](#confirm-dailypurgetime)
  - [Run the CMOP SSL Certificate installation batch file](#run-the-cmop-ssl-certificate-installation-batch-file)
  - [Create a new FDAMedGuidePrinterTask task](#create-a-new-fdamedguideprintertask-task)
    - [Import a new Scheduler Task configuration file](#import-a-new-scheduler-task-configuration-file)
    - [Confirm or fine-tune the scheduled task configuration](#confirm-or-fine-tune-the-scheduled-task-configuration)
  - [Import customized Adobe Reader Windows Registry settings](#import-customized-adobe-reader-windows-registry-settings)
  - [Confirm correct deployment of program files](#confirm-correct-deployment-of-program-files)
    - [Run the verifying batch file](#run-the-verifying-batch-file)
  - [Starting or stopping the FDAMedGuidePrinterTask task manually](#starting-or-stopping-the-fdamedguideprintertask-task-manually)
  - [Steps to Install a Network Printer via a Local Spooler](#steps-to-install-a-network-printer-via-a-local-spooler)
- [Back-out/Uninstall Procedures](#back-outuninstall-procedures)
- [Upgrading to a new version of Automatic Printing](#upgrading-to-a-new-version-of-automatic-printing)
- [Troubleshooting](#troubleshooting)
  - [Session 0 Isolation](#session-0-isolation)
  - [Cannot find Adobe Reader](#cannot-find-adobe-reader)
  - [Cannot download Med Guides from CMOP Portal](#cannot-download-med-guides-from-cmop-portal)
  - [Nothing is sent to the destination printer spool](#nothing-is-sent-to-the-destination-printer-spool)
  - [Exception when running batch file](#exception-when-running-batch-file)
  - [Protected Mode is enabled in Adobe Reader](#protected-mode-is-enabled-in-adobe-reader)
  - [Network Service account and Adobe Reader 9](#network-service-account-and-adobe-reader-9)
  - [Reinstall SSL Certificate](#reinstall-ssl-certificate)
  - [Issues with Network Service account](#issues-with-network-service-account)
  - [Printing Issues](#printing-issues)
  - [Nightly Server Reboot recommendation](#nightly-server-reboot-recommendation)
  - [Increase the priority of java.exe and AcroRd32.exe](#increase-the-priority-of-javaexe-and-acrord32exe)
- [Appendix](#appendix)
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 41%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Version</td>
<td>Description</td>
<td>Author</td>
</tr>
<tr class="even">
<td>03/2018</td>
<td>1.0.1.0</td>
<td><p>Updated the version numbers of the Adobe Reader and Java. Updated screenshots from Windows 2012.</p>
<p>Added the new Informational patch number PSO*7*521 and changed the date everywhere.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/2017</td>
<td>1.0.1.0</td>
<td><p>Updated the name of the SSL certificate and made other minor updates.</p>
<p>Added the new Informational patch number PSO*7*489 and changed the date everywhere.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/2017</td>
<td>1.0.1.0</td>
<td>Review changes and made minor updates. Added the new Informational patch number PSO*7*483 and changed the date everywhere.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>01/2017</td>
<td>1.0.1.0</td>
<td><p>Removed FTP file location for Adobe download and added instructions for standard download from the Adobe website.</p>
<p>Added Windows Server 2012 support.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>06/2015</td>
<td>1.0.1.0</td>
<td><p>Added a section and information related to creating the Domain Service account.</p>
<p>Made changes according to the suggestions given by Product Support team.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>02/2015</td>
<td>1.0.1.0</td>
<td>Added support for Acrobat 11.0 by updating the Adobe registry keys. Informational Patch Number is PSO*7.0*439.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/2014</td>
<td>1.0.1.0</td>
<td><p>Support the new secure CMOP Server using HTTPS functionality released with patches PSS*1.0*177, PSN*4*364 and PSO*7.0*428.</p>
<p>Added information in the Troubleshooting section, added a section with instructions to Add Printer and made some formatting changes.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/2012</td>
<td>1.0</td>
<td>Original Version</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
*(This page included for two-sided copying.)*
Table of Contents
*(This page included for two-sided copying.)*

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Installation Guide provides a description of the installation and deployment procedures for the Department of Veterans Affairs (VA) Food and Drug Administration (FDA) Medication Guides Increment 3 project. This section focuses on the project’s Java FDA Med Guides Printer Tool. The FDA Med Guides Printer Tool is a Java-based program that automatically prints a copy of an FDA medication guide document when one exists for a requested prescription. The program retrieves copies from original med guides found in a local repository on the host server. <span class="mark">REDACTED</span>

| Important:                                                                                                     | To successfully deploy this software it is critical that proper access permissions are set correctly. The host server, the assigned user account, and the deployed software must all have access to either local or remote printers, and have the ability to download med guide files from the [CMOP Portal](https://vaww.cmopnational.va.gov/CR/FDAMedGuides/Forms/AllItems.aspx). |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/002.png) |                                                                                                                                                                                                                                                                                                                                                                                     |

| Important:                                                                                                     | Sites that are currently running the FDA Med Guides Automatic Printing software can go directly to section [6. Upgrading to a new version of Automatic Printing](#upgrading-to-a-new-version-of-automatic-printing). |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/003.png) |                                                                                                                                                                                                                      |

| Note:                                                                                                          | A Domain Service account for FDA Med Guides Automatic Printing application must be created in Active Directory. Refer to section [2.4. Domain Service Account](#section-2). |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/004.png) |                                                                                                                                                                             |

The intended audience for this document is the Information Resources Management Service (IRMS) staff responsible for installing and configuring software on VA Windows servers. Some of the procedures listed below may require System Administrator privileges on target systems.

The installation procedure, including installing the third-party products listed in the pre-installation procedures, should take about an hour or less to complete.

After installation is complete, the host server should be rebooted. Any logged-on users should be advised to log off.

# Pre-installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Tool depends on third-party components to process and print Portable Document Format (PDF) documents. These components are the Windows Server, the Java Runtime Environment (JRE) and Adobe Reader. These components must be properly installed and configured prior to installing and running the FDA Med Guides Printer Tool.

## Deployment scenarios

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of scenarios in which the FDA Med Guides Printer Tool can be deployed successfully. The recommended scenario is to deploy the FDA Med Guides Printer Tool, the Java JRE and Adobe Reader on a print server near the target service area. However, identifying and selecting the best scenario for a particular site is left to the discretion of individual local system administrators who are tasked with installing this package.

## Destination printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any printer used to print med guides must be defined as a local printer on the Windows server hosting the software. That is, the printer spooler must be hosted on the same server where the FDA Med Guides Printer Tool software is running.

## Third-party software Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Windows Server 2012 or 2008

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Microsoft’s Windows Server 2008 or 2012 software must be properly installed and configured on the server hardware. Consult the vendor’s documentation for instructions on installing Server 2012 or 2008, if not already installed.

According to the Technical Reference Model (TRM) forecast, Windows Server 2012 or 2008 is supported as of this writing: <span class="mark">REDACTED</span>. Therefore, instructions provided here are based on Windows Server 2008 or 2012 only. While similar procedures might work for setting up on Windows Server 2003, this is discouraged.

### Java Runtime Environment Version 1.8 for Windows 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>If Java Standard Edition JRE 1.8 or higher is already installed on the server, you may skip this step. To confirm whether java is already installed on the server, or was installed correctly, open a command window and type the command:</p>
<p>Java -version</p>
<p>Information text, similar to that pictured below should appear in the command window, indicating the nomenclature of the java version. If Java is not installed, or not installed properly, the message returned will indicate that “Java is not a recognized system command.”</p>
<p>![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/005.png)</p>
<p>Figure 1 Screen indicating properly installed Java software</p></th>
</tr>
<tr class="odd">
<th>![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/006.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The FDA Med Guides project requires that the Java JRE be installed on the host server. Either one of the x86 or x64 Windows platforms will work. The JRE is not distributed as part of this package and must be downloaded separately from the Oracle website. Download the Java SE version 1.8 or higher version for Windows. To install the Java JRE, simply follow the instructions posted on the Oracle/Java website.

| Important:                                                                                                     | Be sure that you install the Java Runtime Environment (JRE) and not the Java Development Kit (JDK.) These are two distinct and separate installation packages. |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/007.png) |                                                                                                                                                                |

### ### Adobe Acrobat Reader DC version 18 for Windows 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Tool requires that Adobe Reader software be installed on the host server. Adobe Reader is used to print chosen med guides. Adobe Reader is not distributed as part of this package and must be separately downloaded from the Adobe website.

| Note:                                                                                                          | Acrobat Reader DC version 18 is recommended. If a Reader version other than 18 is chosen, then path adjustments must be made in the contents of the installation, configuration and batch files. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/008.png) |                                                                                                                                                                                                  |

| Important:                                                                                                     | DOWNLOAD THE STANDARD READER VERSION FROM THE SCCM SOFTWARE LOCATION GIVEN BELOW OR FROM WWW.ADOBE.COM. |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/009.png) |                                                                                                             |

#### #### Download Adobe Reader

Download the TRM-approved Acrobat Reader DC version 18 software from the following SCCM Approved Software location.

<span class="mark">REDACTED</span>

#### Install Adobe Reader

Install Adobe Reader using the downloaded software. Complete the Adobe Reader installation by responding to displayed prompts.

> **NOTE:** Select “Manually check for and install updates” as shown below.

![Figure 2 Example of Adobe Reader installation prompt with “Manually check…” option selected](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/010.png)

*Figure 2 Example of Adobe Reader installation prompt with “Manually check…” option selected*

> **NOTE:** Select “Import” if Adobe displays the following prompt.

![Figure 3 Example of Adobe Reader Security prompt with “Import” option to import Trusted certificates from the previous version](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/011.png)

*Figure 3 Example of Adobe Reader Security prompt with “Import” option to import Trusted certificates from the previous version*

## ## Domain Service Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Domain Service account must be created in Active Directory for the FDA Med Guides Automatic Printing application to work properly. The FDA Med Guides Automatic Printing task must be run using this Domain Service account as described in section 4.5.2.1.

### Create Domain Service Account for FDA Med Guides

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A Domain Service account for FDA Med Guides Automatic Printing application must be created in Active Directory.
- Add Domain Service account to the Administrator group on the server as it needs Administrative privileges.
- Add Domain Service account to the Server Security Admin group (for example, V21PAL IRMS-SERVERSECADMIN) and the Print Operators group so that it has permissions to invoke Acrobat and send print jobs to the network printers.
- Ensure Domain Service account has permissions to view and download files from the [CMOP portal](https://vaww.cmopnational.va.gov/CR/FDAMedGuides/Forms/AllItems.aspx).

# Deployment package contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Tool deployment package consists of a single archive (ZIP) file that contains a number of folders, each containing a number of files. All the needed components, and file paths, are stored in this archive. A listing and description of these folders and files is found in the [Appendix.](#appendix)

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation steps listed below are specific to the FDA Med Guides Printer Tool Java component.

## Obtain ZIP distribution file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download the file from an official source site and save it to the C:\temp folder.

The files listed below may be obtained via Secure File Transfer Protocol (SFTP). The preferred method is to access the files from: <span class="mark">REDACTED</span>.

This transmits the files from the first available server. Sites may also elect to retrieve software directly from a specific server as follows:

CIO FIELD OFFICE ADDRESS DIRECTORY

---------------- ------------------------- --------------------

<span class="mark">REDACTED</span>

File Name Retrieval Format

-------------- -------------------------

PSO_7_P521.zip BINARY

## Deploy files from the distribution file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Extract ZIP file contents into C:\\

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Extract the contents of the distribution ZIP file into the root folder of the C drive (C:\\. The embedded file structure will be recreated and the files placed in the proper folders.

| Note:                                                                                                          | The file name of the downloaded distribution ZIP file may be a variation from that shown in the following screen captures. |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/012.png) |                                                                                                                            |

![Figure 4 Navigate to C:	emp and Select the Distribution File](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/013.png)

*Figure 4 Navigate to C:\temp and Select the Distribution File*

![Figure 5 Initiate the Extract All wizard](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/014.png)

*Figure 5 Initiate the Extract All wizard*

![Figure 6 Clear the Text for Default Path to Destination Folder](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/015.png)

*Figure 6 Clear the Text for Default Path to Destination Folder*

![Figure 7 Enter the New Destination Path, toggle the Checkbox on and click the "Extract" Button](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/016.png)

*Figure 7 Enter the New Destination Path, toggle the Checkbox on and click the "Extract" Button*

![Figure 8 Windows Explorer Opens on C:\ folder](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/017.png)

*Figure 8 Windows Explorer Opens on C:\\ folder*

## Edit the properties configuration file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Tool needs to locate the Adobe Reader executable so that it can instruct Reader to print a med guide. The path to Adobe Reader is stored in a properties file named “fda_med_guides.properties”. This entry is set with a default value assuming an Adobe Reader DC version 18 installation on a Server 2012 or 2008 host. However, the path must be confirmed to be valid, or adjusted if necessary.

### Verify path to Adobe Reader program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm that the path indicated in the following property file is correct.

| File                                             | Element           | Description                                  |
|--------------------------------------------------|-------------------|----------------------------------------------|
| C:\FDAMedGuidesPrinter\fda_med_guides.properties | AcrobatReaderPath | The path to the Adobe Reader executable file |

Open file C:\FDAMedGuidesPrinter\fda_med_guides.properties for editing. This is a text file and using a text editor like Notepad will be adequate.

Locate the AcrobatReaderPath element in the list. For example:

![Figure 9 Sample Contents of Properties File](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/018.png)

*Figure 9 Sample Contents of Properties File*

Confirm that the path to AcroRd32.exe is correct, for your version of Adobe Reader. If not, make proper adjustments and save your changes.

### Confirm DailyPurgeTime

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DailyPurgeTime element in the properties file represents the time of a 24-hour day when the folder containing temporary work files is cleared of all files. This is an automatic clean-up process performed at the indicated time. Adjust this entry as needed to list the most convenient time to perform this operation, based on the time when system use is at a minimal.

![Figure 10 DailyPurgeTime Setting in Properties File](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/019.png)

*Figure 10 DailyPurgeTime Setting in Properties File*

## Run the CMOP SSL Certificate installation batch file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Tool needs the CMOP SSL certificate to download FDA Medication guides from the new CMOP server. The script adds the certificate to the Java trust store.

The following steps must be executed:

- Go to C:\FDAMedGuidesPrinter\installation
- Right click on SSL_Certificate_installation.bat again and select Run as administrator.
- NOTE: You need to run the script as an Administrator or be an Administrator in order for it to work.

The following window will be displayed. Press any key to close the window.

![Figure 11 SSL Certificate Installation window](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/020.png)

*Figure 11 SSL Certificate Installation window*

If the SSL Certificate already exists, the error message shown in Figure 11-2 will be displayed to the user. If the certificate already exists, the user can proceed to the next step in the installation process.

![Figure 12 SSL Certificate already exists](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/021.png)

*Figure 12 SSL Certificate already exists*

If the error message in the screenshot below appears, the user can proceed as the certificate has been installed. The error message results when the script cannot find a JRE version installed. If JRE exists, the Automatic Printing will work and the user can proceed with the installation.

![Figure 13 SSL Certificate added to the Java keystore](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/022.png)

*Figure 13 SSL Certificate added to the Java keystore*

If there is no JRE, then the script will display error message “*Failed to locate any installed Java environments, please install a Java Runtime Environment*”. The server administrator needs to install JRE 1.8 or higher on the server in this case.

## Create a new FDAMedGuidePrinterTask task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Tool is deployed to run as a non-interactive background process (Windows Scheduled Task) and is listed on the server’s list of scheduled tasks. This program runs in the background, and is therefore not evident to end-users, logged on or not. There is no user interface associated with the FDA Med Guides Printer Tool; therefore there is no user interactivity.

The following characteristics apply to the task configuration:

- The name of the scheduled task is FDAMedGuidePrinterTask.
- By default, the Automatic Printing application runs under NT AUTHORITY\NETWORK SERVICE account. The Network Service account on the server may or may not have adequate permissions based on your server settings. The account MUST have permissions to download files from the [CMOP portal](https://vaww.cmopnational.va.gov/CR/FDAMedGuides/Forms/AllItems.aspx) and also requires permissions to print to the network printers.
- We strongly recommend that you use a Domain Service account created for the FDA Med Guides Automatic Printing application as suggested in section <u>2.4</u>. To change the user account associated with FDA Med Guides from Network Service account to Domain Service account see instructions given in section <u>4.5.2.1</u>.
- The C:\FDAMedGuidesPrinter\START_fda_med_guides_automatic_printing.bat batch file will be run by the task.
- The task starts in the C:\FDAMedGuidesPrinter (application) folder.
- The task is configured to run whether the assigned user is logged in or not. Typically, no user is logged in.

### Import a new Scheduler Task configuration file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A predefined task configuration XML file is distributed as part of this installation package. The file is named FDAMedGuidePrinterTask.xml, and it is located in the C:\FDAMedGuidesPrinter\installation folder.

Importing this file into Task Scheduler automatically configures the FDAMedGuidePrinterTask with default settings. After importing the settings file, saving the task creates the new task in Task Scheduler.

Follow the steps in the screenshots below to create the FDAMedGuidePrinterTask task.

![Figure 14 Task Scheduler shown within Computer Management](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/023.png)

*Figure 14 Task Scheduler shown within Computer Management*

![Figure 15 Import an Existing Task Configuration File](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/024.png)

*Figure 15 Import an Existing Task Configuration File*

![Figure 16 Select and Open FDAMedGuidePrinterTask XML File](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/025.png)

*Figure 16 Select and Open FDAMedGuidePrinterTask XML File*

![Figure 17 Create Task Dialog to Add the New Task](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/026.png)

*Figure 17 Create Task Dialog to Add the New Task*

### Confirm or fine-tune the scheduled task configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After creating the FDAMedGuidePrinterTask, you should verify that the imported settings are correct.

The following screen captures represent the desired configuration settings for the FDAMedGuidePrinterTask task on a Windows Server 2012 system. Your system should be set up in a similar fashion. Compare the following screenshots with your setting and adjust accordingly—if necessary.

![Figure 18 FDAMedGuidePrinterTask in Task Library](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/027.png)

*Figure 18 FDAMedGuidePrinterTask in Task Library*

#### Change User account associated with the FDAMedGuidePrinterTask

- The default user is set to NT AUTHORITY\NETWORK SERVICE account. The Network Service account on the server may or may not have adequate permissions based on your server settings. In the General tab, the user account associated with the FDAMedGuidePrinterTask task can be changed from the default Windows Network Service account to the Domain Service account created for the FDA Med Guides Automatic Printing application, as shown in Figures 19 and 20 below.
- Right click on the FDAMedGuidePrinterTask task and select Properties.
- In the General tab, click on the “Change User or Group…” button.
- Enter the Domain Service account user name created or the FDA Med Guides Automatic Printing application as give in section <u>2.4</u> and select the location (for example, Entire Directory).
- Enter the password when prompted.
- The Domain Service account needs to have Administrative privileges on the server and should be added to the appropriate Printer groups and the Server Security Admin group so that it has permissions to invoke Acrobat and send print jobs to the network printers.

![Figure 19 General Tab Settings](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/028.png)

*Figure 19 General Tab Settings*

![Figure 20 Select User, Service Account or Group](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/029.png)

*Figure 20 Select User, Service Account or Group*

![Figure 21 Triggers Tab Settings](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/030.png)

*Figure 21 Triggers Tab Settings*

![Figure 22 Edit Trigger Settings](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/031.png)

*Figure 22 Edit Trigger Settings*

![Figure 23 Actions Tab Settings](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/032.png)

*Figure 23 Actions Tab Settings*

![Figure 24 Edit Action Settings](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/033.png)

*Figure 24 Edit Action Settings*

![Figure 25 Conditions Tab Settings](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/034.png)

*Figure 25 Conditions Tab Settings*

![Figure 26 Settings Tab Settings](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/035.png)

*Figure 26 Settings Tab Settings*

![Figure 27 Sample History Tab](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/036.png)

*Figure 27 Sample History Tab*

## Import customized Adobe Reader Windows Registry settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Tool controls Adobe Reader in the background, while no interactive user is logged in. Adobe Reader sometimes tries to interact with a user when no user is available to reply to Adobe Reader prompts. An example of this is when Adobe Reader presents the End-User License Agreement (EULA) screen. There are Registry settings that can be set to inhibit these prompts. These are listed in the included Windows Registry Editor file.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>Important:</th>
<th rowspan="2"><p>If the FDAMedGuidePrinterTask task is configured to run using a <strong>Domain Service account</strong>, instead of the Network Service account, one of the following options must be executed.</p>
<p><em><u>Option 1:</u></em> <strong>Login to the server using the</strong> <strong>Domain Service account</strong> that is being assigned to the FDAMedGuidePrinterTask task and <strong>apply the registry keys</strong> by executing the NetworkServiceTaskSettings.reg file according to the instructions given below.</p>
<p><em><u>Option 2:</u></em> The NetworkServiceTaskSettings.reg file must be edited to <strong>replace HKEY_USERS\S-1-5-20 with the SID of the Service account</strong>, which looks like S-1-5-20, from the windows registry at the path HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList. Then <strong>apply the registry keys</strong> by executing the NetworkServiceTaskSettings.reg file according to the instructions given below.</p></th>
</tr>
<tr class="odd">
<th>![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/037.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Before starting the task (first use), you must import these Registry settings. Locate the NetworkServiceTaskSettings.reg file in the C:\FDAMedGuidesPrinter\installation folder. Then, import the settings as indicated in the screen captures below.

![Figure 28 NetworkServiceTaskSettings.reg Registry Settings File](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/038.png)

*Figure 28 NetworkServiceTaskSettings.reg Registry Settings File*

![Figure 29 Merge Menu Item](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/039.png)

*Figure 29 Merge Menu Item*

![Figure 30 Confirmation Dialog. Click on “Yes” Button](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/040.png)

*Figure 30 Confirmation Dialog. Click on “Yes” Button*

![Figure 31 Confirmation Dialog. Click on “Yes” Button](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/041.png)

*Figure 31 Confirmation Dialog. Click on “Yes” Button*

![Figure 32 Notification Dialog. Click on “OK” Button](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/042.png)

*Figure 32 Notification Dialog. Click on “OK” Button*

## Confirm correct deployment of program files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A batch file automates the process of confirming that the necessary folders and files were deployed correctly. Confirmation is made only on files belonging to the FDA Med Guides Printer Tool.

### Run the verifying batch file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Execute the batch file as administrator located in C:\FDAMedGuidesPrinter\installation\Verify_installation.bat. Right click and select the ‘Run as administrator’ option. The resulting display should look similar to the one below. Any missing files or configuration errors should be listed in the results.

> **NOTE:** The Java JRE 1.8 version in the screenshot below would change based the 1.8.0_xx you have installed on your server.

![Figure 33 Verify_installation.bat file](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/043.png)

*Figure 33 Verify_installation.bat file*

![Figure 34 Run Verify_installation.bat file as Administrator](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/044.png)

*Figure 34 Run Verify_installation.bat file as Administrator*

![Figure 35 Display of Installation Confirmation results with no errors reported](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/045.png)

*Figure 35 Display of Installation Confirmation results with no errors reported*

![Figure 36 Display of Installation Confirmation results with some errors reported](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/046.png)

*Figure 36 Display of Installation Confirmation results with some errors reported*

## Starting or stopping the FDAMedGuidePrinterTask task manually

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing and configuring the FDA Med Guides Printer Tool system, it is strongly recommended that you reboot the server to start the FDAMedGuidePrinterTask task—the task is configured to start with the system. However, you can also start or stop the task manually.

The procedure appears in the following screen captures. To start the task, select “Run” from the pop-up menu. To stop the task, select “End”. To confirm that the task is running, see the text indicated in the Status column. Ready means that the task is active, but not running. Running means that the task is running.

![Figure 37 FDAMedGuidePrinterTask Task Listed in Task Scheduler List](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/047.png)

*Figure 37 FDAMedGuidePrinterTask Task Listed in Task Scheduler List*

![Figure 38 Select Task and Open Menu](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/048.png)

*Figure 38 Select Task and Open Menu*

![Figure 39 Select Run from the Menu](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/049.png)

*Figure 39 Select Run from the Menu*

![Figure 40 Task is shown in “Running” state. Application is ready to receive Print Requests](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/050.png)

*Figure 40 Task is shown in “Running” state. Application is ready to receive Print Requests*

## Steps to Install a Network Printer via a Local Spooler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a Network printer via a Local spooler:

- Go to Control Panel -\> Hardware -\> Devices and Printers
- Click ‘Add a Printer’
- Select ‘Add a local or network printer as an administrator’
- Select ‘Add a local printer’
- Select ‘Create a new port’
- Type of port: Local Port
- Click ‘Next’
- Enter a port name: *Enter the IP address of the Network Printer*
- Click ‘Ok’
- Select the correct printer driver for the network printer
- Click ‘Next’
- Select ‘Use the driver that is currently installed (recommended)’ OR as appropriate for your machine
- Type a printer name: \<enter a printer name\>
- Note: This will later be added to the VistA Device File (#3.5) entry in the “WINDOWS NETWORK PRINTER NAME” field (#75).
- Click ‘Next’
- Select ‘Share this printer…’
- Click ‘Next’ and then ‘Finish’

| Note:                                                                                                          | At this point, test the FDA Med Guides Printer Tool by sending a print request. A test is successful if the expected output is found at the destination printer. |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/051.png) |                                                                                                                                                                  |

![Figure 41 After a Print Job Request is sent, Adobe Reader is listed in the Task Manager](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/052.png)

*Figure 41 After a Print Job Request is sent, Adobe Reader is listed in the Task Manager*

# Back-out/Uninstall Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Stop the FDAMedGuidesPrinterTask task in the Task Scheduler.

> ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/053.png)

> Figure 42 Stopping the FDAMedGuidesPrinterTask in the Task Scheduler

- Delete the FDAMedGuidesPrinterTask task from the Scheduler list.

> ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/054.png)

> Figure 43 Deleting the FDAMedGuidesPrinterTask in the Task Scheduler

- In the Task Manager:
- Click on the Details tab
- Find the task named AcroRd32.exe running under the FDA Med Guides user account (that is, the account used to run the FDAMedGuidePrinter Task).
- Right-click and select End Task. Click End Process in the conformation dialog.
- Find the task named java.exe running under the FDA Med Guides user account
- Right-click and select End Process. Click End Process in the conformation dialog.

![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/055.png)

> Figure 44 Acrobat Reader process in the Task Manager

> ![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/056.png)

> Figure 45 Deleting Acrobat Reader process in the Task Manager

- Delete the C:\FDAMedGuidesPrinter folder and all its contents.

# Upgrading to a new version of Automatic Printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Uninstall the old version of FDA Med Guides as shown in [Section 5](#back-outuninstall-procedures).
- Do not uninstall the Java 1.8.
- Uninstall Acrobat Reader version 11.
- Install Acrobat Reader DC version 18 by following the instructions given in [Section 2.3.3](#section).
- Follow the installation steps in [Section 4](#installation-procedure) to install the new version of FDA Med Guides Automatic Printing.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you encounter errors in this system, they are likely to be deployment-related malfunctions. Using Adobe Reader in a non-interactive fashion risks encountering a Server 2008 condition known as Session 0 Isolation. Similarly, using the Network Service account for the FDAMedGuidePrinterTask task has risks that the task may not have sufficient permissions to access needed network resources, like printers or the CMOP Portal. These two risks are the most likely source of a malfunction. The main symptoms are:

- No output reaches the destination printer spool.
- No file is downloaded to the C:\FDAMedGuidesPrinter\workspace\medguides folder from the CMOP Portal.
- No temporary PDF file is created in the C:\FDAMedGuidesPrinter\workspace\temp folder.
- Adobe Reader isn’t responding or is responding incorrectly. Again, the symptom is that no output reaches the destination printer spool.
- The user assigned to the FDAMedGuidePrinterTask task is unable to connect to CMOP.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>One useful troubleshooting technique is to run the FDA Med Guides Printer Tool while bypassing the FDAMedGuidePrinterTask task. This is done in interactive mode by logging in as an interactive user and following these steps:</p>
<ol type="1">
<li><p>End the FDAMedGuidePrinterTask task, if it is running.</p></li>
<li><p>Start the C:\FDAMedGuidesPrinter\START_fda_med_guides_automatic_printing.bat batch file.</p></li>
</ol></th>
</tr>
<tr class="odd">
<th>![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/057.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The following sections list the possible malfunctions and remedies.

## Session 0 Isolation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Session 0 Isolation is a new security feature in Windows 7 and Windows Server 2008 or 2012. It affects non-interactive sessions by restricting a program’s ability to interact with the console. This feature directly affects the way that Adobe Reader is used in this system, and a problem may occur when Adobe Reader presents interactive dialogs while expecting a user response.

These events are rare and occur as a result of a new Adobe Reader installation or upgrade. Typically, these are the request to agree to a EULA or a Product Improvement Program opt-in message. Session 0 Isolation is complex and is explained in the links below.

The installation step labeled “Import customized Adobe Reader Windows Registry settings” addresses this problem by importing Registry keys that prevent known prompting events. These Registry settings are bound to individual user accounts and must be applied to the user account selected to control the FDAMedGuidePrinterTask task. You may need to make adjustments to the NetworkServiceTaskSettings.reg file to reflect the correct user account.

![Figure 46 Example Adobe Reader Prompt to User](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/058.png)

*Figure 46 Example Adobe Reader Prompt to User*

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Symptom</th>
<th>Possible solution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Adobe Reader doesn’t seem to respond to print requests.</td>
<td>Log on as an interactive user and determine whether Adobe Reader is requesting a response from the user.</td>
</tr>
<tr class="even">
<td></td>
<td><p>This interaction is not visible to the non-interactive user, giving the impression that the med guide’s application is malfunctioning. Therefore, no output is generated at the printer spool. The server’s system administrator must identify the user account associated with the FDA Med Guides scheduled task, log on as that user, start Adobe Reader manually, and respond to all prompts generated. For Network Service, this can only be resolved via Registry adjustments on that account</p>
<p>![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/059.png)</p>
<p><strong>Figure 47 Session 0 Isolation Symptom Message</strong></p>
<p>The following Web links offer information on this topic.</p>
<p><a href="http://efreedom.com/Question/1-4618833/Delphi-Win32-Service-Printer-Selected-Valid-Error-2008-64bit-Standard-Server?showall=true#additionalAnswersMarker">http://efreedom.com/Question/1-4618833/Delphi-Win32-Service-Printer-Selected-Valid-Error-2008-64bit-Standard-Server?showall=true#additionalAnswersMarker</a></p>
<p><a href="http://msdn.microsoft.com/en-us/gg465126">http://msdn.microsoft.com/en-us/gg465126</a></p>
<p><a href="http://blogs.technet.com/b/askperf/archive/2007/04/27/application-compatibility-session-0-isolation.aspx">http://blogs.technet.com/b/askperf/archive/2007/04/27/application-compatibility-session-0-isolation.aspx</a></p>
<p><a href="http://msdn.microsoft.com/en-us/library/bb756986.aspx">http://msdn.microsoft.com/en-us/library/bb756986.aspx</a></p>
<p><a href="http://www.beingmanan.com/wp/2008/06/create-uac-white-list/">http://www.beingmanan.com/wp/2008/06/create-uac-white-list/</a></p>
<p><a href="http://msdn.microsoft.com/en-us/windows/hardware/gg463353.aspx">http://msdn.microsoft.com/en-us/windows/hardware/gg463353.aspx</a></p>
<p><a href="http://www.firedaemon.com/manual/index.html?WindowsVista">http://www.firedaemon.com/manual/index.html?WindowsVista</a></p></td>
</tr>
</tbody>
</table>

## Cannot find Adobe Reader

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Symptom                                                           | Possible solution                                                                                                              |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| An error indicates that Adobe Reader executable can’t be located. | Verify that the path pointing to the Reader executable is correct in the C:\FDAMedGuidesPrinter\fda_med_guides.properties file |

## Cannot download Med Guides from CMOP Portal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a med guide request is made and no med guide file appears in C:\FDAMedGuidesPrinter\workspace\medguides, the application is likely unable to connect to the CMOP SharePoint site. Reasons for this to occur are as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Symptom</th>
<th>Possible solution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CMOP site is down</td>
<td>Try again later.</td>
</tr>
<tr class="even">
<td>User assigned to task has insufficient privileges to access CMOP site.</td>
<td>Adjust permissions, or create a new user with appropriate access.</td>
</tr>
<tr class="odd">
<td>Unable to write downloaded med guide to local folder.</td>
<td>Confirm that user has write access to folder.</td>
</tr>
<tr class="even">
<td>An error page is printed instead of the expected med guide.</td>
<td>The med guide name is invalid or the med guide PDF file doesn’t exist at the CMOP Portal. Verify that the PDF file exists, or that the PDF file name indicated in the print request is correct.</td>
</tr>
<tr class="odd">
<td>Java uninstall/reinstall</td>
<td><p>If Java is uninstalled and reinstalled on the FDA Med Guides print server, execute the following SSL script to add CMOP SSL certificate to the Java trust store.</p>
<ul>
<li><p>C:\FDAMedGuidesPrinter\installation\ SSL_Certificate_installation.bat</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Adobe Acrobat Reader uninstall/reinstall</td>
<td><p>If the Adobe Acrobat Reader is uninstalled and reinstalled on the FDA Med Guides print server, execute the following scripts to add Adobe keys to the Windows registry and to verify the FDA Med Guides installation.</p>
<ul>
<li><p>C:\FDAMedGuidesPrinter\installation\ NetworkServiceTaskSettings.reg</p></li>
<li><p>C:\FDAMedGuidesPrinter\installation\ Verify_installation.bat</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Nothing is sent to the destination printer spool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Symptom                                                    | Possible solution                                                                            |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Adobe Reader is malfunctioning                             | Using Task Manager, kill any AcroRd32.exe processes belonging to the pertinent user account. |
| Destination printer name in med guide request is incorrect | Verify that the printer name is correct.                                                     |

## Exception when running batch file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th>Symptom</th>
<th>Possible solution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Invoking the START_fda_med_guides_automatic_printing.bat</p>
<p>batch file fails to start the Java application and indicates: Exception in thread "main" java.lang.NoClassDefFoundError</p>
<p>![](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/060.png)</p>
<p><strong>Figure 48 JAR File Error</strong></p></td>
<td>Verify that paths indicated in batch and properties files are correct, particularly the path to the JAR file.</td>
</tr>
</tbody>
</table>

## Protected Mode is enabled in Adobe Reader

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are using the Network Service account, you can skip this procedure--this setting is already toggled off by the Registry settings import procedure listed above. If you are using any other account, Protected Mode is toggled on by default in Adobe Reader DC. This setting interferes with the proper functioning of the Java component, so you must toggle it off while logged on as that account.

![Figure 49 Disabling Protected Mode at Startup](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/061.png)

*Figure 49 Disabling Protected Mode at Startup*

## Network Service account and Adobe Reader 9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a known “ROAMING PROFILE” issue with Adobe Reader 9.x that causes it to malfunction under certain circumstances while assigning the NETWORK SERVICE account to the FDAMedGuidePrinterTask task. For this reason, Adobe Reader 9.x is not recommended for this application. Use Adobe Reader DC version 18 instead.

## Reinstall SSL Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Java/JRE is reinstalled, the CMOP SSL certificate also needs to be reinstalled according to the instructions given in [Section 4.4](#run-the-cmop-ssl-certificate-installation-batch-file).

## Issues with Network Service account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the FDAMedGuidePrinterTask is run under the NETWORK SERVICE account:

- If there are delays in printing or if the Med Guides do not print, a Domain Service account with the highest privileges should be created and used instead of using the NETWORK SERVICE account.
- If Domain Service account cannot be created, the FDAMedGuidePrinterTask can be run under the Administrator account. This would require the Administrator to be logged in, while the task is running. This is not a recommended approach.

## Printing Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you experience print issues or delays with the NETWORK SERVICE account, we strongly recommend that you use a Domain Service account created for the FDA Med Guides Automatic Printing application. This account needs to have Administrative privileges on the server.

- Add the NETWORK SERVICE account or the Service account to the Server Security Admin group so that it has permissions to invoke Acrobat and send print jobs to the network printers.
- Check if the NETWORK SERVICE account or the Service account has permissions to access the Printer.
- Add NETWORK SERVICE account or the Service account to the ‘Users’ and ‘Print Operators’ groups.

![Figure 50 Add Service account to Administrators, Users and Print Operators groups](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/062.png)

*Figure 50 Add Service account to Administrators, Users and Print Operators groups*

![Figure 51 Example of adding the NETWORK SERVICE account to Administrators group](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/063.png)

*Figure 51 Example of adding the NETWORK SERVICE account to Administrators group*

- If Med Guides appear in the temp folder but do not go to the printer queue, go to Services and stop the Print Spooler service and start it again.

![Figure 52 Restarting Print Spooler service](pso-7-521-java-fda-medication-guides-automatic-printing-project-installation-gui/064.png)

*Figure 52 Restarting Print Spooler service*

- Restart FDAMedGuidePrinterTask
- Go to Task Scheduler and stop the FDAMedGuidePrinterTask task by selecting ‘End’.
- Go to Windows Task Manager. Find any AcorRd32.exe and java.exe tasks running under the NETWORK SERVICE account or the Service account and stop them by clicking ‘End Process’.
- Go to Task Scheduler again and start the FDAMedGuidePrinterTask task by selecting ‘Run’.

## Nightly Server Reboot recommendation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Given the number of Med Guides that are printed each day and due to the load on the server, it is recommended that the Windows server be rebooted every night to free up resources and to cleanup any hung tasks.

## Increase the priority of java.exe and AcroRd32.exe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run a PowerShell script that increases the priority of java.exe and AcroRd32.exe from Below Normal to High. This may speed up the execution of printing under the NETWORK SERVICE account.  Below are the lines to run in PowerShell. This needs to be run after the server starts the FDAMedGuidePrinterTask task.

\$processname="java.exe"

\$process=Get-WmiObject win32_process -f "name='\$processname'"

\$process.SetPriority(128)

\$processname="AcroRd32.exe"

\$process=Get-WmiObject win32_process -f "name='\$processname'"

\$process.SetPriority(128)

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After extracting the contents of the ZIP file, the below FDA Med Guides Printer folder structure and files should be available on the C:\\ drive.

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 17%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Path</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter</td>
<td>Folder</td>
<td>Main folder. Root folder for application files. These include the JAR, batch and properties files.</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib</td>
<td>Folder</td>
<td>Sub-folder containing supporting third-party Java libraries</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\installation</td>
<td>Folder</td>
<td>Folder containing pre-defined configuration files</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\CMOP_SSL_Certificate</td>
<td>Folder</td>
<td>Folder containing CMOP SSL certificate</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\workspace</td>
<td>Folder</td>
<td>Workspace main folder.</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\workspace\medguides</td>
<td>Folder</td>
<td>Path to med guides local repository. Folder contains copies of original FDA Med Guides as downloaded from the CMOP Portal Site.</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\workspace\temp</td>
<td>Folder</td>
<td>Path to area for temporarily processing stamped med guides. Folder contains scratch files of altered med guides</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\START_fda_med_guides_automatic_printing.bat</td>
<td>Batch file</td>
<td>Batch file to initiate the FDA Med Guides Printer Tool Java program</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\fda_med_guides.properties</td>
<td>Configuration file</td>
<td>User-configurable items for the FDA Med Guides Printer Tool</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\fda_med_guides_logging.properties</td>
<td>Configuration file</td>
<td>User-configurable items for the logging engine</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\fda_med_guides_automatic_printing_1.0.1.0.jar</td>
<td>Java archive</td>
<td>Main jar file containing all Java code for the FDA Med Guides Printer Tool</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\ SSL_Certificate_installation.bat</td>
<td>Batch file</td>
<td>Batch file to add CMOP SSL certificate to the Java trust store and set JRE_HOME</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\installation\CMOP_SSL_Certificate\VA-Internal-S2-RCA1-v1.cer</td>
<td>Certificate file</td>
<td>SSL Certificate that is issued by VA which will be added to the Java trust store</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\ FDAMedGuidePrinterTask.xml</td>
<td>XML file</td>
<td>Configuration file used to create the FDAMedGuidePrinterTask task</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\installation\ NetworkServiceTaskSettings.reg</td>
<td>Windows Registry import file</td>
<td>Configuration file used to set up the Adobe Reader setting for use by the NT AUTHORITY\NETWORKSERVICE user</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\ Verify_installation.bat</td>
<td>Batch file</td>
<td>Batch file used to confirm a successful deployment of the FDA Med Guides Printer Tool</td>
</tr>
<tr class="odd">
<td>Path</td>
<td>Type</td>
<td>Description</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib\commons-io-2.4.jar</td>
<td>Java archive</td>
<td><p>Supporting third-party Apache Commons</p>
<p>Java library</p></td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\lib\commons-lang3-3.3.2.jar</td>
<td>Java archive</td>
<td><p>Supporting third-party Apache Commons</p>
<p>Java library</p></td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib\commons-logging-1.1.3.jar</td>
<td>Java archive</td>
<td><p>Supporting third-party Apache Commons</p>
<p>Java library</p></td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\lib\fontbox-1.8.5.jar</td>
<td>Java archive</td>
<td>Supporting third-party PDFBox Java library.</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib\jempbox-1.8.5.jar</td>
<td>Java archive</td>
<td>Supporting third-party PDFBox Java library.</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\lib\pdfbox-1.8.5.jar</td>
<td>Java archive</td>
<td>Supporting third-party PDFBox Java library.</td>
</tr>
<tr class="even">
<td>Log files in folder C:\FDAMedGuidesPrinter</td>
<td>*.log</td>
<td>Log files are used for debugging purposes only and are created AFTER the initial use of the program.</td>
</tr>
</tbody>
</table>

#