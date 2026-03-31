---
title: Java - FDA Medication Guides Automatic Printing Project - Installation Guide (Updated PSO*7*665)
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Java - FDA Medication Guides Automatic Printing Project -  (Updated PSO*7*665)
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: ![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/001.png)
audience: 
keywords: 
  - table
  - span
  - java
  - class
  - guides
  - contents
  - installation
  - task
  - figure
  - printing
page_count: 0
word_count: 6292
section_count: 21
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2022
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/PHAR_FDA_MED_GUIDE_AUTO_PSO_7_665_IG_R.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/PHAR_FDA_MED_GUIDE_AUTO_PSO_7_665_IG_R.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

FDA Medication Guides (PSO\*7\*665)

Automatic Printing Java Component

Installation Guide

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/001.png)

March 2022

Version 1.1.0.0

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc96935202" class="anchor"></span>Table 1: Downloadable File</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 43%" />
<col style="width: 24%" />
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
<td>03/17/2022</td>
<td>1.1.0.0</td>
<td><p>PSO*7*665:</p>
<ul>
<li><p>Removed all “Adobe Reader” references as the FDA Med Guide Application is no longer dependent on Adobe Reader DC software.</p></li>
<li><p>Updated <strong><u>Figure 1</u></strong>, <strong><u>Figure 2</u></strong>, <strong><u>Figure 3</u></strong>, <strong><u>Figure 6</u></strong>, <strong><u>Figure 10</u></strong>, <strong><u>Figure 11</u></strong>, <strong><u>Figure 13</u></strong>, <strong><u>Figure 14</u></strong>, <strong><u>Figure 17</u></strong>, <strong><u>Figure 18</u></strong>, <strong><u>Figure 30</u></strong>, <strong><u>Figure 33</u></strong>, <strong><u>Figure 34</u></strong>, <strong><u>Figure 35</u></strong>, <strong><u>Figure 36</u></strong>, and <strong><u>Figure 37</u></strong></p></li>
<li><p>Updated <strong><u>Table 2</u></strong>, <strong><u>Table 3</u></strong>, <strong><u>Table 4</u></strong>, and <strong><u>Table 5</u></strong></p></li>
<li><p>Added List of Tables and List of Figures</p></li>
<li><p>The unredacted version of this document is stored in the SOFTWARE library for viewing <mark>REDACTED</mark> information</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>05/05/2021</td>
<td>1.0.1.2</td>
<td><p>PSO*7*633:</p>
<p>Update CMOP SharePoint URL to new VA Share site for Med Guide retrieval. Moved Adobe custom modification section to the Adobe installation section of the document per field input request. Updated JAVA installation notes table to include a step to copy the net.properties file in the installation. Add a note to the prerequisite section indicating Amazon Corretto is an acceptable JAVA installation.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>06/23/2020</td>
<td>1.0.1.1</td>
<td><p>PSO*7*601:</p>
<p>Update Java source code for FDA Med Guides Auto print for Fortify Mitigation Q1 2020</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>02/13/2020</td>
<td>1.0.1.0</td>
<td><p>PSO*7*588:</p>
<p>Update document to include a reference to the VA Technical Reference Model (TRM) for third party pre-requisite software.</p>
<p>Updated Windows Server, Java Runtime Environment and Adobe Reader DC third party software pre-requisite section 2.3.</p>
<p>Updated the JAVA installation section (section 4) to include instructions for modifying the net.properties file included in the JAVA distribution. Added additional screenshots where applicable.</p>
<p>Figure labels added to the JAVA installation section (section 4) and alt text provided for each figure.</p>
<p>Formatted the title page and modified section (section 4)</p>
<p>Updated TOC and Footers</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>03/2018</td>
<td>1.0.1.0</td>
<td><p>Updated the version numbers of the Adobe Reader and Java. Updated screenshots from Windows 2012.</p>
<p>Added the new Informational patch number PSO*7*521 and changed the date everywhere.</p></td>
<td>HPS Sustainment Clinical</td>
</tr>
<tr class="even">
<td>06/2017</td>
<td>1.0.1.0</td>
<td><p>Updated the name of the SSL certificate and made other minor updates.</p>
<p>Added the new Informational patch number PSO*7*489 and changed the date everywhere.</p></td>
<td>HPS Sustainment Clinical</td>
</tr>
<tr class="odd">
<td>04/2017</td>
<td>1.0.1.0</td>
<td>Review changes and made minor updates. Added the new Informational patch number PSO*7*483 and changed the date everywhere.</td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="even">
<td>01/2017</td>
<td>1.0.1.0</td>
<td><p>Removed FTP file location for Adobe download and added instructions for standard download from the Adobe website.</p>
<p>Added Windows Server 2012 support.</p></td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="odd">
<td>06/2015</td>
<td>1.0.1.0</td>
<td><p>Added a section and information related to creating the Domain Service account.</p>
<p>Made changes according to the suggestions given by Product Support team.</p></td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="even">
<td>02/2015</td>
<td>1.0.1.0</td>
<td>Added support for Acrobat 11.0 by updating the Adobe registry keys. Informational Patch Number is PSO*7.0*439.</td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="odd">
<td>12/2014</td>
<td>1.0.1.0</td>
<td><p>Support the new secure CMOP Server using HTTPS functionality released with patches PSS*1.0*177, PSN*4*364 and PSO*7.0*428.</p>
<p>Added information in the</p>
<p>Troubleshooting section, added a section with instructions to Add Printer and made some formatting changes.</p></td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="even">
<td>03/2012</td>
<td>1.0</td>
<td>Original Version</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<span id="_Toc96935202" class="anchor"></span>Table 1: Downloadable File
# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Pre-installation Considerations](#pre-installation-considerations)
  - [Deployment scenarios](#deployment-scenarios)
  - [Destination printers](#destination-printers)
  - [Third-party software Pre-requisites](#third-party-software-pre-requisites)
    - [Windows Server](#windows-server)
    - [Java 1.8 Runtime Environment for Windows](#java-18-runtime-environment-for-windows)
  - [Domain Service Account](#domain-service-account)
    - [Create Domain Service Account for FDA Med Guides](#create-domain-service-account-for-fda-med-guides)
- [Deployment package contents](#deployment-package-contents)
- [Installation Procedure](#installation-procedure)
  - [Obtain ZIP distribution file](#obtain-zip-distribution-file)
  - [Deploy files from the distribution file](#deploy-files-from-the-distribution-file)
    - [Extract ZIP file contents into C:\\](#extract-zip-file-contents-into-c)
    - [Confirm DailyPurgeTime](#confirm-dailypurgetime)
  - [Configure JAVA](#configure-java)
    - [Run the SSL Certificate installation batch file](#run-the-ssl-certificate-installation-batch-file)
    - [Install the JAVA net.properties file](#install-the-java-netproperties-file)
  - [Create a new FDAMedGuidePrinterTask task](#create-a-new-fdamedguideprintertask-task)
    - [Import a new Scheduler Task configuration file](#import-a-new-scheduler-task-configuration-file)
    - [Confirm or fine-tune the scheduled task configuration](#confirm-or-fine-tune-the-scheduled-task-configuration)
    - [Change User account associated with the FDAMedGuidePrinterTask](#change-user-account-associated-with-the-fdamedguideprintertask)
  - [Confirm correct deployment of program files](#confirm-correct-deployment-of-program-files)
    - [Run the verifying batch file](#run-the-verifying-batch-file)
  - [Starting or stopping the FDAMedGuidePrinterTask task manually](#starting-or-stopping-the-fdamedguideprintertask-task-manually)
  - [Steps to Install a Network Printer via a Local Spooler](#steps-to-install-a-network-printer-via-a-local-spooler)
- [Back-out/Uninstall Procedures](#back-outuninstall-procedures)
  - [If AcroRd32 is still installed, follow these instructions](#if-acrord32-is-still-installed-follow-these-instructions)
- [Upgrading to a new version of Automatic Printing](#upgrading-to-a-new-version-of-automatic-printing)
- [Troubleshooting](#troubleshooting)
  - [Cannot download Med Guides from CMOP Portal](#cannot-download-med-guides-from-cmop-portal)
  - [Nothing is sent to the destination printer spool](#nothing-is-sent-to-the-destination-printer-spool)
  - [Exception when running batch file](#exception-when-running-batch-file)
  - [Reinstall SSL Certificate](#reinstall-ssl-certificate)
  - [Issues with Network Service account](#issues-with-network-service-account)
  - [Printing Issues](#printing-issues)
  - [Nightly Server Reboot recommendation](#nightly-server-reboot-recommendation)
  - [Increase the priority of java.exe](#increase-the-priority-of-javaexe)
- [Appendix](#appendix)
This Installation Guide provides a description of the installation and deployment procedures for the Department of Veterans Affairs (VA) Food and Drug Administration (FDA) Medication Guides. This section focuses on the project’s FDA Med Guides Auto Print Utility. The FDA Med Guides Printer Utility is a Java-based program that automatically prints a copy of an FDA medication guide document when one exists for a requested prescription. The program retrieves copies from original med guides found in a local repository on the host server. If a requested med guide is not found locally, then an attempt is made to download the med guide from the med guides share site on the VA network.
| Important:                                                                                          | To successfully deploy this software, it is critical that proper access permissions are set correctly. The host server, the assigned user account, and the deployed software must all have access to either local or remote printers, and have the ability to download med guide files from the VA Share site[.](https://vaww.cmopnational.va.gov/CR/FDAMedGuides/Forms/AllItems.aspx) |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/002.png) |                                                                                                                                                                                                                                                                                                                                                                                        |
<span id="_Ref95902226" class="anchor"></span>Table 2: FDA Med Guide Errors
| Important:                                                                                          | Sites that are currently running the FDA Med Guides Automatic Printing software can go directly to section [6. Upgrading to a new version of Automatic Printing](#upgrading-to-a-new-version-of-automatic-printing). |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/003.png) |                                                                                                                                                                                                                      |
<span id="_Ref95902227" class="anchor"></span>Table 3: Printer Spool Errors
<table>
<caption><p><span id="_Ref95902229" class="anchor"></span>Table 4: Batch File Errors</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>A Domain Service account for FDA Med Guides Automatic Printing application must be created in Active Directory. Refer to section <a href="#domain-service-account">2.4. Domain Service Account.</a></p>
<p>It is strongly recommended that a Domain Service account with the highest privileges be used to install all third party and FDA Med Guide Automatic Printing software.</p></th>
</tr>
<tr class="odd">
<th>![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/004.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<span id="_Ref95902229" class="anchor"></span>Table 4: Batch File Errors
The intended audience for this document is the Information Resources Management Service (IRMS) staff responsible for installing and configuring software on VA Windows servers.
The installation procedure, including installing the third-party products listed in the pre-installation procedures, should take about an hour or less to complete.
After installation is complete, the host server should be rebooted. Any logged-on users should be advised to log off.

# Pre-installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility depends on third-party components to process and print Portable Document Format (PDF) documents. The components used are Windows Server and Java Runtime Environment (JRE). These components must be properly installed and configured prior to installing and running the FDA Med Guides Printer Utility. Refer to the VA Technical Reference Model (TRM) for the approved versions of Windows Server and JRE: <span class="mark">REDACTED</span>

## Deployment scenarios

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several scenarios in which the FDA Med Guides Printer Utility can be deployed successfully. The recommended scenario is to deploy the FDA Med Guides Printer Utility and Java JRE on a server near the target service area. However, identifying and selecting the best scenario for a particular site is left to the discretion of individual local system administrators who are tasked with installing this package.

## Destination printers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any printer used to print med guides must be defined as a local printer on the Windows server hosting the software. That is, the printer spooler must be hosted on the same server where the FDA Med Guides Printer Utility software is running.

## Third-party software Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Windows Server and JRE are required to run the FDA Medication Guide Automatic Printing software. The required third-party software is not distributed as part of this package. Download and install a VA TRM compliant version of these applications from the vendor’s website or an approved VA web site.

> **NOTE:** All third-party software should be installed using a Domain Service account that has been granted administrator privileges and will be used to run the FDA Med Guide Automatic Printing software. Refer to Section <u>2.4 Domain Service Account</u>.

### Windows Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Microsoft’s Windows Server software must be properly installed and configured on the server hardware. Consult the vendor’s documentation for instructions on installing Server if not already installed. Windows Server versions must be compliant with the TRM.

### Java 1.8 Runtime Environment for Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides project requires a TRM compliant version of a JRE 1.8 or higher (including TRM compliant versions of Amazon Corretto 8 or higher) to be installed on the host server.

<table>
<caption><p><span id="_Ref95902230" class="anchor"></span>Table 5: FDA Med Guides Printer Folder and File Structure</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>To confirm whether Java is already installed on the server, or was installed correctly, open a command window, and enter the command:</p>
<p><strong>java -version</strong></p>
<p>Information text should appear in the command window, indicating the nomenclature of the java version. If Java is not installed, or not installed properly, the message returned will indicate:</p>
<p>“Java is not a recognized system command.”</p></th>
</tr>
<tr class="odd">
<th>![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/005.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref95902230" class="anchor"></span>Table 5: FDA Med Guides Printer Folder and File Structure

If a JRE is not installed or not a TRM compliant version, download a TRM compliant version of JRE compatible with the respective Windows version. Install the JRE per the instructions consistent with the host operating system and downloaded instance.

## Domain Service Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Domain Service account must be created in Active Directory for the FDA Med Guides Automatic Printing application to work properly. The FDA Med Guides Automatic Printing task must be run using this Domain Service account as described in Section <u>4.4 Create a new FDAMedGuidePrinterTask task</u>.

### Create Domain Service Account for FDA Med Guides

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Domain Service account for the FDA Med Guides Automatic Printing application must be created in Active Directory.

Add a Domain Service account to the Administrator group on the server as it needs Administrative privileges.

Add a Domain Service account to the Server Security Admin group (for example, V21PAL IRMSSERVERSECADMIN) and the Print Operators group permissions to send print jobs to the network printers.

Ensure the Domain Service account has permissions to view and download files from the VA Share site[.](https://vaww.cmopnational.va.gov/CR/FDAMedGuides/Forms/AllItems.aspx)

# Deployment package contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility deployment package consists of a single archive ZIP file that contains several folders, each containing the files necessary for the application’s deployment. A listing and description of these folders and files are found in the <u>Appendix</u>.

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation steps listed below are specific to the FDA Med Guides Printer Utility Java component.

## Obtain ZIP distribution file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file listed below may be obtained via Secure File Transfer Protocol (SFTP). The preferred method is to access the file from: <span class="mark">REDACTED</span>

This transmits the file from the first available server.

| File Name      | Retrieval Format |
|----------------|------------------|
| PSO_7_Pxxx.zip | BINARY           |

This table shows the file(s) that need to be downloaded

Download the file and save it to the C:\temp folder.

<span id="_Ref95901854" class="anchor"></span>Figure 1: Download and save to C:\temp

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/006.png)

## Deploy files from the distribution file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Extract ZIP file contents into C:\\

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Important

If the previous installation folder exists, rename the old installation folder “C:\FDAMedGuidesPrinter” for backup purposes and to allow creation of a new folder “C:\FDAMedGuidesPrinter” during extraction. To avoid a conflict between old and new installations, please do not extract over the existing folder.

Extract the contents of the distribution ZIP file into the root folder of the C drive (C:\\. The embedded file structure will be recreated. Locate the distribution file.

> **NOTE:** The file name of the downloaded distribution ZIP file may be a variation from that shown in the following screen captures.

<span id="_Ref95901861" class="anchor"></span>Figure 2: C:\Temp Folder

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/007.png)

Right click on the zip file and select ‘Extract All…’

<span id="_Ref95901862" class="anchor"></span>Figure 3: Initiate the Extract All Wizard

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/008.png)

Change the default destination path to C:\\ and select the ‘Show extracted files when complete’ checkbox.

<span id="_Toc96935210" class="anchor"></span>Figure 4: Default Destination Path

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/009.png)

Select Extract and observe the Post-Extraction screen.

<span id="_Toc96935211" class="anchor"></span>Figure 5: Post-Extraction Screen

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/010.png)

### Confirm DailyPurgeTime

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open the file C:\FDAMedGuidesPrinter\fda_med_guides.properties for editing. This is a text file and using a text editor like Notepad will be adequate. The DailyPurgeTime element in the properties file represents the time of a 24-hour day when the folder containing temporary work files is cleared of all files. This is an automatic clean-up process performed at the indicated time. Adjust this entry as needed to list the most convenient time to perform this operation based on the time when system use is at a minimal.

<span id="_Ref95901920" class="anchor"></span>Figure 6: DailyPurgeTime Example

<span class="mark">REDACTED</span>

## Configure JAVA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Run the SSL Certificate installation batch file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility needs the approved VA provided SSL certificates necessary to access the VA Share site to complete the downloads of the FDA Medication guides. The script adds the VA provided SSL certificates to the Java cacerts trust store and are included with this distribution.

Execute the following steps to install the certificates to the JAVA cacerts keystore:

> Go to C:\FDAMedGuidesPrinter\installation directory.

> Right click on the SSL_Certificate_installation.bat file and select Run as administrator.

> Note: The script needs to be run as an Administrator, or the user needs to be a Machine Administrator for it to work. It is recommended to complete this while logged into the server with the Domain Service account that will be used to run the FDA Med Guide Automatic Printing software. If there are issues with running the script, verify the JAVA installation from Section <u>2.3.2 Java 1.8 Runtime Environment for Windows</u>.

The following window will be displayed. Press any key to close the window.

<span id="_Toc96935213" class="anchor"></span>Figure 7: SSL Certificate Installation Window

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/011.png)

If an SSL Certificate already exists, the error message shown in the figure below will be displayed to the user. If the certificate already exists, the user can proceed to the next step in the installation process.

<span id="_Toc96935214" class="anchor"></span>Figure 8: SSL Certificate Already Exists

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/012.png)

If the error message in the screenshot below appears, the user can proceed as the certificate has been installed. The error message results when the script cannot find a JRE version installed. If JRE exists, the Automatic Printing will work, and the user can proceed with the installation.

<span id="_Hlk33515081" class="anchor"></span>Figure 9: SSL Certificate Added to the Java Keystore

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/013.png)

If there is no JRE installed, then the script will display error message, “Failed to locate any installed Java environments, please install a Java Runtime Environment.” To install a TRM compliant version of JAVA, follow the steps described in Section <u>2.3.2 Java 1.8 Runtime Environment for Windows</u>.

### Install the JAVA net.properties file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For this step, navigate to the Amazon Correto folder established from Section <u>2.3.2 Java 1.8 Runtime Environment for Windows</u>.

Navigate to the C:\Program Files\Amazon Correto\jdk…\conf directory.

<span id="_Ref95901962" class="anchor"></span>Figure : The net.properties file within the conf folder

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/014.png)

Select the net.properties file.

Open the file’s menu options (right click the file).

Select Rename.

Enter net.properties.backup.

<span id="_Ref95901993" class="anchor"></span>Figure 11: Example of renamed net.properties.backup file

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/015.png)

Navigate to the C:\FDAMedGuidesPrinter\installation directory.

<span id="_Toc95983459" class="anchor"></span>Figure : C:\FDAMedGuidesPrinter\installation folder

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/016.png)

Select the net.properties file.

Copy the net.properties file.

Paste the file into C:\Program Files\Amazon Correto\jdk…\conf.

> **NOTE:** The following screenshot is an example of the destination for the net.properties file and may vary depending on the location of the installed JRE.

<span id="_Ref95902000" class="anchor"></span>Figure : Example of the destination for the net.properties file after installation

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/017.png)

This completes the JAVA configuration.

## Create a new FDAMedGuidePrinterTask task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility is deployed to run as a non-interactive background process (Windows Scheduled Task) and is listed on the server’s list of scheduled tasks. This program runs in the background; therefore, not evident to users that are logged on. There is no user interface associated with the FDA Med Guides Printer Utility; therefore, there is no user interactivity.

The following characteristics apply to the task configuration:

> The name of the scheduled task is FDAMedGuidePrinterTask.

> By default, the Automatic Printing application runs under NT AUTHORITY\NETWORK SERVICE account. The Network Service account on the server may or may not have adequate permissions based on the server settings. The account MUST have permissions to download files from the VA Share Point and permissions to print to the network printers.

> We strongly recommend the use of a Domain Service account created for the FDA Med Guides Automatic Printing application as suggested in Section <u>2.4 Domain Service Account</u>. To change the user account associated with FDA Med Guides from a Network Service account to a Domain Service account see instructions given in Section <u>Change User account associated with the FDAMedGuidePrinterTask</u>.

> The C:\FDAMedGuidesPrinter\START_fda_med_guides_automatic_printing.bat batch file will be run by the task.

> The task starts in the C:\FDAMedGuidesPrinter (application) folder.

> The task is configured to run whether the assigned user is logged in or not. Typically, no user is logged in.

### Import a new Scheduler Task configuration file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A predefined task configuration XML file is distributed as part of this installation package. The file is named FDAMedGuidePrinterTask.xml, and it is in the C:\FDAMedGuidesPrinter\installation folder.

Importing this file into Task Scheduler automatically configures the FDAMedGuidePrinterTask with default settings. After importing the settings file, saving the task creates the new task in Task Scheduler.

Follow the steps and the screenshots below to create the FDAMedGuidePrinterTask task.

Navigate to Computer Management.

Expand the System Tools option.

Expand the Task Scheduler option.

Open the menu options for the Task Scheduler Library.

<span id="_Ref95902020" class="anchor"></span>Figure 14: Task Scheduler Shown Within Computer Management

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/018.png)

Select Import Task….

<span id="_Toc96935221" class="anchor"></span>Figure 15: Task Scheduler Library Option Menu

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/019.png)

Select FDAMedGuidePrinterTask

Select Open.

<span id="_Toc96935222" class="anchor"></span>Figure 16: FDAMedGuidePrinterTask XML File

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/020.png)

Verify settings and select OK to add the new task.

> **NOTE:** The Change User or Group field should be changed to the Domain Service account with administrator privileges that is going to be used to run the FDAMedGuidePrinterTask.

<span id="_Ref95902051" class="anchor"></span>Figure 17: Create Task Dialog Box- example

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/021.png)

### Confirm or fine-tune the scheduled task configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After creating the FDAMedGuidePrinterTask, verify that the imported settings are correct. The following screen captures represent the desired configuration settings for the FDAMedGuidePrinterTask task on a Windows Server 2012 system. The system in use should be set up in a similar fashion. Compare the following screenshots with the user’s settings and adjust accordingly—if necessary.

<span id="_Ref95902062" class="anchor"></span>Figure 18: FDAMedGuidePrinterTask in the Task Library

<span class="mark">REDACTED</span>

### Change User account associated with the FDAMedGuidePrinterTask

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The default user is set to NT AUTHORITY\NETWORK SERVICE account. The Network Service account on the server may or may not have adequate permissions based on the server settings. In the General tab, the user account associated with the FDAMedGuidePrinterTask task can be changed from the default Windows Network Service account to the Domain Service account created for the FDA Med Guides Automatic Printing application, as shown in figures below.

> Open the options menu for the FDAMedGuidePrinterTask task and select Properties.

> In the General tab, select the Change User or Group… button.

> Enter the Domain Service account username created, or the FDA Med Guides Automatic Printing application as given in Section <u>2.4 Domain Service Account</u> and select the location (for example, Entire Directory).

> Enter the password when prompted.

The Domain Service account needs to have Administrative privileges on the server and should be added to the appropriate Printer and Server Security Admin groups so that it has permissions to send print jobs to the network printers.

<span id="_Toc96935225" class="anchor"></span>Figure 19: General Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/022.png)

<span id="_Toc96935226" class="anchor"></span>Figure 20: Select User, Service Account, or Group

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/023.png)

The screenshots below are examples of the setup for the Triggers, Actions, Conditions, Settings and History Tabs.

<span id="_Toc96935227" class="anchor"></span>Figure 21: Triggers Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/024.png)

<span id="_Toc96935228" class="anchor"></span>Figure 22: Edit Trigger Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/025.png)

<span id="_Toc96935229" class="anchor"></span>Figure 23:Actions Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/026.png)

<span id="_Toc96935230" class="anchor"></span>Figure 24: Edit Action Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/027.png)

<span id="_Toc96935231" class="anchor"></span>Figure 25: Conditions Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/028.png)

<span id="_Toc96935232" class="anchor"></span>Figure 26: Settings Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/029.png)

<span id="_Toc96935233" class="anchor"></span>Figure 27: Sample History Tab

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/030.png)

## Confirm correct deployment of program files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A batch file automates the process of confirming that the necessary folders and files were deployed correctly. Confirmation is made only on files belonging to the FDA Med Guides Printer Tool.

### Run the verifying batch file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open the options menu for the file and select Run as administrator to execute the batch file located in C:\FDAMedGuidesPrinter\installation\Verify_installation.bat. The resulting display should look like <u>Figure 28</u> below. Any missing files or configuration errors should be listed in the results.

<span id="_Ref95895423" class="anchor"></span>Figure 28: File Location

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/031.png)

<span id="_Toc96935235" class="anchor"></span>Figure 29: Run as administrator Option

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/032.png)

<span id="_Ref95902067" class="anchor"></span>Figure 30: Installation Confirmation result with no Errors Reported

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/033.png)

<span id="_Ref95902071" class="anchor"></span>Figure 31: Installation Confirmation result with some Errors Reported

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/034.png)

> **NOTE:** If errors are reported, review the errors and all previous installation steps. Refer to the respective steps of the installation guide.

## Starting or stopping the FDAMedGuidePrinterTask task manually

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing and configuring the FDA Med Guides Printer Utility system, it is strongly recommended to perform a server reboot to start the FDAMedGuidePrinterTask task—the task is configured to start with the system. However, the task can be started or stopped manually.

The procedure appears in the following screen captures. To start the task, select Run from the pop-up menu. To stop the task, select End. To confirm that the task is running, see the text indicated in the Status column. Ready means that the task is active, but not running. Running means that the task is running.

<span id="_Toc96935238" class="anchor"></span>Figure 32: FDAMedGuidePrinterTask Task Listed in the Task Scheduler

![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/035.png)

<span id="_Ref95902095" class="anchor"></span>Figure 33: Select Task and Open Menu

<span class="mark">REDACTED</span>

<span id="_Ref95902099" class="anchor"></span>Figure 34: Task Menu Option Run

<span class="mark">REDACTED</span>

<span id="_Ref95902111" class="anchor"></span>Figure 35: Task Shown in Running State

<span class="mark">REDACTED</span>

## Steps to Install a Network Printer via a Local Spooler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a Network printer via a Local spooler:

> Navigate to Control Panel \> Hardware \> Devices and Printers

> Select Add a Printer

> Select Add a local or network printer as an administrator

> Select Add a local printer

> Select Create a new port

> Type of port: Local Port

> Select Next

> Enter a port name: Enter the IP address of the Network Printer

> Select Ok

> Select the correct printer driver for the network printer

> Select Next

> Select Use the driver that is currently installed (recommended) OR as appropriate for the machine

> Type a printer name: Enter a printer name

> **NOTE:** This will later be added to the VistA Device File (#3.5) entry in the WINDOWS NETWORK PRINTER NAME field (#75).

> Select Next

> Select Share this printer…

> Select Next and then Finish

> **NOTE:** At this point, test the FDA Med Guides Printer Utility by sending a print request. A test is successful if the expected output is found at the destination printer.

# Back-out/Uninstall Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Stop the FDAMedGuidesPrinterTask task in the Task Scheduler.

<span id="_Ref95902116" class="anchor"></span>Figure 36: Stopping the FDAMedGuidesPrinterTask in the Task Scheduler

<span class="mark">REDACTED</span>

Delete the FDAMedGuidesPrinterTask task from the Scheduler list.

<span id="_Ref95902120" class="anchor"></span>Figure 37: Deleting the FDAMedGuidesPrinterTask in the Task Scheduler

<span class="mark">REDACTED</span>

In the Task Manager:

Select the Details tab.

Find the task named java.exe running under the FDA Med Guides user account.

Right-click and select End Task.

Select End Process in the confirmation dialog.

Backup the C:\FDAMedGuidesPrinter folder and all its contents.

## If AcroRd32 is still installed, follow these instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Task Manager:

> Select the Details tab.

> Find the task named AcroRd32.exe running under the FDA Med Guides user account (that is, the account used to run the FDAMedGuidePrinter Task).

> <span id="_Toc96935244" class="anchor"></span>Figure 38: Acrobat Reader process in the Task Manager

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/036.png)

> Right-click and select End Task. Select End Process in the confirmation dialog.

> <span id="_Toc96935245" class="anchor"></span>Figure 39: Deleting Acrobat Reader process in the Task Manager

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/037.png)

# Upgrading to a new version of Automatic Printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Uninstall the old version of FDA Med Guides as shown in Section <u>5 Back-out/Uninstall Procedures</u>.

Do not uninstall JAVA 1.8.

To install the new version of FDA Med Guides Automatic Printing, follow the installation steps in Section <u>4 Installation Procedure</u>.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you encounter errors in this system, they are likely to be deployment-related malfunctions.

Using the Network Service account for the FDAMedGuidePrinterTask task has risks that the task may not have sufficient permissions to access needed network resources, like printers or the Consolidated Mail Outpatient Pharmacy (CMOP) Portal. These two risks are the most likely source of a malfunction. The main symptoms are:

> No output reaches the destination printer spool.

> No file is downloaded to the C:\FDAMedGuidesPrinter\workspace\medguides folder from the CMOP Portal.

> No temporary PDF file is created in the C:\FDAMedGuidesPrinter\workspace\temp folder.

> The user assigned to the FDAMedGuidePrinterTask task is unable to connect to CMOP.

Important

One useful troubleshooting technique is to run the FDA Med Guides Printer Utility while bypassing the FDAMedGuidePrinterTask task. This is done in interactive mode by logging in as an interactive user and following these steps:

End the FDAMedGuidePrinterTask task, if it is running.

Start the C:\FDAMedGuidesPrinter\START_fda_med_guides_automatic_printing.bat batch file.

The following sections list the possible malfunctions and remedies.

## Cannot download Med Guides from CMOP Portal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a med guide request is made and no med guide file appears in

C:\FDAMedGuidesPrinter\workspace\medguides, the application is likely unable to connect to the CMOP SharePoint site. Reasons for this to occur are as follows:

<table>
<caption>FDA Med Guide ErrorsThis table shows the errors by symptom and possible solution.</caption>
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
<td>The CMOP site is down.</td>
<td>Try again later.</td>
</tr>
<tr class="even">
<td>User assigned to task has insufficient privileges to access CMOP site.</td>
<td>Adjust permissions or create a new user with appropriate access.</td>
</tr>
<tr class="odd">
<td>Unable to write downloaded med guide to local folder.</td>
<td>Confirm that user has write access to folder.</td>
</tr>
<tr class="even">
<td>An error page is printed instead of the expected med guide.</td>
<td>The med guide name is invalid, or the med guide PDF file doesn’t exist at the CMOP Portal. Verify that the PDF file exists, or that the PDF file name indicated in the print request is correct.</td>
</tr>
<tr class="odd">
<td>Uninstall/reinstall Java.</td>
<td><p>If Java is uninstalled and reinstalled on the FDA Med Guides print server, execute the following SSL script to add CMOP SSL certificate to the Java trust store.</p>
<p>C:\FDAMedGuidesPrinter\installation\ SSL_Certificate_installation.bat</p>
<p>To copy the net.properties file to the newly installed JAVA instance, follow the steps described in Section <strong><u>4.3.2 Install the JAVA net.properties file</u></strong>.</p></td>
</tr>
</tbody>
</table>

FDA Med Guide ErrorsThis table shows the errors by symptom and possible solution.

## Nothing is sent to the destination printer spool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Symptom                                                     | Possible solution                          |
|-------------------------------------------------------------|--------------------------------------------|
| Destination printer name in med guide request is incorrect. | Verify that the printer’s name is correct. |

Printer Spool ErrorsThis table shows the errors by symptom and possible solution.

## Exception when running batch file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Batch File ErrorsThis table shows the errors by symptom and possible solution.</caption>
<colgroup>
<col style="width: 55%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>Symptom</th>
<th>Possible solution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Invoking the START_fda_med_guides_automatic_printing.bat batch file fails to start the Java application and indicates: Exception in thread "main" java.lang.NoClassDefFoundError</p>
<p><span id="_Toc95821740" class="anchor"></span>Figure 40: JAR File Error</p>
<p><mark>REDACTED</mark></p></td>
<td>Verify that paths indicated in batch and properties files are correct, particularly the path to the JAR file.</td>
</tr>
</tbody>
</table>

Batch File ErrorsThis table shows the errors by symptom and possible solution.

## Reinstall SSL Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Java/JRE is reinstalled, the CMOP SSL certificate also needs to be reinstalled according to the instructions given in Section <u>4.3.1 Run the SSL Certificate installation batch file</u>.

## Issues with Network Service account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the FDAMedGuidePrinterTask is run under the NETWORK SERVICE account:

> If there are delays in printing or if the Med Guides do not print, a Domain Service account with the highest privileges should be created and used instead of using the NETWORK SERVICE account.

> If Domain Service account cannot be created, the FDAMedGuidePrinterTask can be run under the Administrator account. This would require the Administrator to be logged in while the task is running. This is not a recommended approach.

## Printing Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you experience print issues or delays with the NETWORK SERVICE account, we strongly recommend that you use a Domain Service account created for the FDA Med Guides Automatic Printing application. This account needs to have Administrative privileges on the server.

> Add the NETWORK SERVICE account or the Service account to the Server Security Admin group so that it has permissions to send print jobs to the network printers.

> Check if the NETWORK SERVICE account or the Service account has permissions to access the printer.

> Add NETWORK SERVICE account or the Service account to the ‘Users’ and ‘Print Operators’ groups.

> <span id="_Toc96935247" class="anchor"></span>Figure 41: Add Service account to Administrators, Users and Print Operators groups

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/038.png)

> <span id="_Toc96935248" class="anchor"></span>Figure 42: Example of adding the NETWORK SERVICE account to Administrators group

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/039.png)

> If Med Guides appear in the temp folder but do not go to the printer queue, go to Services, and stop the Print Spooler service and start it again.

> <span id="_Toc96935249" class="anchor"></span>Figure 43: Restarting Print Spooler service

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-updated/040.png)

> Restart FDAMedGuidePrinterTask

> Go to Task Scheduler and stop the FDAMedGuidePrinterTask task by selecting End.

> Go to Windows Task Manager. Find any java.exe tasks running under the NETWORK SERVICE account or the Service account and stop them by selecting End Process.

> Go to Task Scheduler again and start the FDAMedGuidePrinterTask task by selecting Run.

## Nightly Server Reboot recommendation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Given the number of Med Guides that are printed each day and due to the load on the server, it is recommended that the Windows server be rebooted every night to free up resources and to cleanup any hung tasks.

## Increase the priority of java.exe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run a PowerShell script that increases the priority of java.exe from Below Normal to High. This may speed up the execution of printing under the NETWORK SERVICE account. Below are the lines to run in PowerShell. This needs to be run after the server starts the FDAMedGuidePrinterTask task.

\$processname="java.exe"

\$process=Get-WmiObject win32_process -f "name='\$processname'"

\$process.SetPriority(128)

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After extracting the contents of the ZIP file, the below FDA Med Guides Printer folder structure and files should be available on the C:\\ drive.

<table>
<caption>FDA Med Guides Printer Folder and File StructureThis table shows lists the folder and file strucutre by path, type, and description</caption>
<colgroup>
<col style="width: 57%" />
<col style="width: 14%" />
<col style="width: 27%" />
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
<td>Main folder. Root folder for application files. These include the JAR, batch, and properties files</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib</td>
<td>Folder</td>
<td>Sub-folder containing supporting third-party Java libraries</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\installation</td>
<td>Folder</td>
<td>Folder containing predefined configuration files</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\CMOP_SSL_Certificate</td>
<td>Folder</td>
<td>Folder containing CMOP SSL certificate</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\workspace</td>
<td>Folder</td>
<td>Workspace main folder</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\workspace\medguides</td>
<td>Folder</td>
<td>Path to med guides local repository. Folder contains copies of original FDA Med Guides as downloaded from the CMOP Portal Site</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\workspace\temp</td>
<td>Folder</td>
<td>Path to area for temporarily processing stamped med guides. Folder contains scratch files of altered med guides</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\START_fda_med_guide s_automatic_printing.bat</td>
<td>Batch file</td>
<td><p>Batch file to initiate the</p>
<p>FDA Med Guides Printer Utility Java program</p></td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\fda_med_guides.properties</td>
<td><p>Configuration</p>
<p>file</p></td>
<td>User-configurable items for the FDA Med Guides Printer Utility</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\fda_med_guides_logging .properties</td>
<td><p>Configuration</p>
<p>file</p></td>
<td>User-configurable items for the logging engine</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\fda_med_guides_autom atic_printing_1.1.0.0.jar</td>
<td>Java archive</td>
<td><p>Main jar file containing all</p>
<p>Java code for the FDA</p>
<p>Med Guides Printer Tool</p></td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\ SSL_Certificate_installation.bat</td>
<td>Batch file</td>
<td>Batch file to add CMOP SSL certificate to the Java trust store and set JRE_HOME</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\installation\CMOP_SSL_ Certificate\VA-Internal-S2-RCA1-v1.cer</td>
<td>Certificate file</td>
<td>SSL Certificate that is issued by VA which will be added to the Java trust store</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\ FDAMedGuidePrinterTask.xml</td>
<td>XML file</td>
<td>Configuration file used to create the FDAMedGuidePrinterTask task</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\installation\ Verify_installation.bat</td>
<td>Batch file</td>
<td>Batch file used to confirm a successful deployment of the FDA Med Guides Printer Utility</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib\commons-io-2.7.jar</td>
<td>Java archive</td>
<td><p>Supporting third-party</p>
<p>Apache Commons</p>
<p>Java library</p></td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\lib\commons-lang3-3.3.2.jar</td>
<td>Java archive</td>
<td><p>Supporting third-party</p>
<p>Apache Commons</p>
<p>Java library</p></td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib\commons-logging-1.1.3.jar</td>
<td>Java archive</td>
<td><p>Supporting third-party</p>
<p>Apache Commons</p>
<p>Java library</p></td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\lib\fontbox-2.0.24.jar</td>
<td>Java archive</td>
<td>Supporting third-party PDFBox Java library</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib\xmpbox-2.0.24.jar</td>
<td>Java archive</td>
<td>Supporting third-party PDFBox Java library</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\lib\pdfbox-2.0.24.jar</td>
<td>Java archive</td>
<td>Supporting third-party PDFBox Java library</td>
</tr>
<tr class="even">
<td>Log files in folder C:\FDAMedGuidesPrinter</td>
<td>*.log</td>
<td>Log files are used for debugging purposes only and are created AFTER the initial use of the program</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\installation\net.properties</td>
<td>JAVA properties file</td>
<td>JAVA Properties file for controlling access to network hosts from JAVA processes</td>
</tr>
</tbody>
</table>

FDA Med Guides Printer Folder and File StructureThis table shows lists the folder and file strucutre by path, type, and description