---
title: Java-FDA Medication Guides Automatic Printing Project - Installation Guide (PSS*7*633)
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Java-FDA Medication Guides Automatic Printing Project -  (PSS*7*633)
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - java
  - table
  - guides
  - installation
  - contents
  - printing
  - automatic
  - guide
  - adobe
  - task
page_count: 0
word_count: 7261
section_count: 24
table_count: 5
figure_count: 5
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/PHAR_FDA_MED_GUIDE_AUTO_PSO_7_633_IG_R.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/PHAR_FDA_MED_GUIDE_AUTO_PSO_7_633_IG_R.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

FDA Medication Guides (PSO\*7\*633)

Automatic Printing Java Component

Installation Guide

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/001.png)

May 2021

Version 1.0.1.2

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p>Table : Downloadable File</p></caption>
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
<td>05/05/2021</td>
<td>1.0.1.2</td>
<td><p>PSO*7*633:</p>
<p>Update CMOP SharePoint URL to new VA Share site for Med Guide retrieval. Moved Adobe custom modification section to the Adobe installation section of the document per field input request. Updated JAVA installation notes table to include a step to copy the net.properties file in the installation. Add a note to the prerequisite section indicating Amazon Corretto is an acceptable JAVA installation.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>06/23/2020</td>
<td>1.0.1.1</td>
<td><p>PSO*7*601:</p>
<p>Update Java source code for FDA Med Guides Auto print for Fortify Mitigation Q1 2020</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
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
<tr class="even">
<td>03/2018</td>
<td>1.0.1.0</td>
<td><p>Updated the version numbers of the Adobe Reader and Java. Updated screenshots from Windows 2012.</p>
<p>Added the new Informational patch number PSO*7*521 and changed the date everywhere.</p></td>
<td>HPS Sustainment Clinical</td>
</tr>
<tr class="odd">
<td>06/2017</td>
<td>1.0.1.0</td>
<td><p>Updated the name of the SSL certificate and made other minor updates.</p>
<p>Added the new Informational patch number PSO*7*489 and changed the date everywhere.</p></td>
<td>HPS Sustainment Clinical</td>
</tr>
<tr class="even">
<td>04/2017</td>
<td>1.0.1.0</td>
<td>Review changes and made minor updates. Added the new Informational patch number PSO*7*483 and changed the date everywhere.</td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="odd">
<td>01/2017</td>
<td>1.0.1.0</td>
<td><p>Removed FTP file location for Adobe download and added instructions for standard download from the Adobe website.</p>
<p>Added Windows Server 2012 support.</p></td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="even">
<td>06/2015</td>
<td>1.0.1.0</td>
<td><p>Added a section and information related to creating the Domain Service account.</p>
<p>Made changes according to the suggestions given by Product Support team.</p></td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="odd">
<td>02/2015</td>
<td>1.0.1.0</td>
<td>Added support for Acrobat 11.0 by updating the Adobe registry keys. Informational Patch Number is PSO*7.0*439.</td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="even">
<td>12/2014</td>
<td>1.0.1.0</td>
<td><p>Support the new secure CMOP Server using HTTPS functionality released with patches PSS*1.0*177, PSN*4*364 and PSO*7.0*428.</p>
<p>Added information in the</p>
<p>Troubleshooting section, added a section with instructions to Add Printer and made some formatting changes.</p></td>
<td><p>Enterprise Application</p>
<p>Maintenance</p></td>
</tr>
<tr class="odd">
<td>03/2012</td>
<td>1.0</td>
<td>Original Version</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table : Downloadable File
# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pre-installation Considerations](#pre-installation-considerations)
  - [Deployment scenarios](#deployment-scenarios)
  - [Destination printers](#destination-printers)
  - [Third-party software Pre-requisites](#third-party-software-pre-requisites)
    - [Windows Server](#windows-server)
    - [Java 1.8 Runtime Environment for Windows](#java-18-runtime-environment-for-windows)
    - [Adobe Reader DC for Windows](#adobe-reader-dc-for-windows)
  - [Domain Service Account](#domain-service-account)
    - [Create Domain Service Account for FDA Med Guides](#create-domain-service-account-for-fda-med-guides)
- [Deployment package contents](#deployment-package-contents)
- [Installation Procedure](#installation-procedure)
  - [Obtain ZIP distribution file](#obtain-zip-distribution-file)
  - [Deploy files from the distribution file](#deploy-files-from-the-distribution-file)
    - [Extract ZIP file contents into C:\\](#extract-zip-file-contents-into-c)
  - [Edit the properties configuration file](#edit-the-properties-configuration-file)
    - [Verify path to Adobe Reader DC program](#verify-path-to-adobe-reader-dc-program)
    - [Confirm DailyPurgeTime](#confirm-dailypurgetime)
  - [Import customized Adobe Reader DC Windows Registry settings](#import-customized-adobe-reader-dc-windows-registry-settings)
  - [Configure JAVA](#configure-java)
    - [Run the SSL Certificate installation batch file](#run-the-ssl-certificate-installation-batch-file)
    - [Install the JAVA net.properties file](#install-the-java-netproperties-file)
  - [Create a new FDAMedGuidePrinterTask task](#create-a-new-fdamedguideprintertask-task)
    - [Import a new Scheduler Task configuration file](#import-a-new-scheduler-task-configuration-file)
    - [Confirm or fine-tune the scheduled task configuration](#confirm-or-fine-tune-the-scheduled-task-configuration)
  - [Confirm correct deployment of program files](#confirm-correct-deployment-of-program-files)
    - [Run the verifying batch file](#run-the-verifying-batch-file)
  - [Starting or stopping the FDAMedGuidePrinterTask task manually](#starting-or-stopping-the-fdamedguideprintertask-task-manually)
  - [Steps to Install a Network Printer via a Local Spooler](#steps-to-install-a-network-printer-via-a-local-spooler)
- [Back-out/Uninstall Procedures](#back-outuninstall-procedures)
- [Upgrading to a new version of Automatic Printing](#upgrading-to-a-new-version-of-automatic-printing)
- [Troubleshooting](#troubleshooting)
  - [Adobe issues](#adobe-issues)
  - [Cannot download Med Guides from CMOP Portal](#cannot-download-med-guides-from-cmop-portal)
  - [Nothing is sent to the destination printer spool](#nothing-is-sent-to-the-destination-printer-spool)
  - [Exception when running batch file](#exception-when-running-batch-file)
  - [Network Service account and Adobe Reader 9](#network-service-account-and-adobe-reader-9)
  - [Reinstall SSL Certificate](#reinstall-ssl-certificate)
  - [Issues with Network Service account](#issues-with-network-service-account)
  - [Printing Issues](#printing-issues)
  - [Nightly Server Reboot recommendation](#nightly-server-reboot-recommendation)
  - [Increase the priority of java.exe and AcroRd32.exe](#increase-the-priority-of-javaexe-and-acrord32exe)
- [Appendix](#appendix)
This Installation Guide provides a description of the installation and deployment procedures for the
Department of Veterans Affairs (VA) Food and Drug Administration (FDA) Medication Guides
Increment 3 project. This section focuses on the project’s FDA Med Guides Auto Print Utility. The FDA Med Guides Printer Utility is a Java-based program that automatically prints a copy of an FDA medication guide document when one exists for a requested prescription. The program retrieves copies from original med guides found in a local repository on the host server. If a requested med guide is not found locally, then an attempt is made to download the med guide from the Share Point Online (SPO) site on the VA network.
| Important:                                                                                                                                            | To successfully deploy this software, it is critical that proper access permissions are set correctly. The host server, the assigned user account, and the deployed software must all have access to either local or remote printers, and have the ability to download med guide files from the VA Share site[.](https://vaww.cmopnational.va.gov/CR/FDAMedGuides/Forms/AllItems.aspx) |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/002.png) |                                                                                                                                                                                                                                                                                                                                                                                        |
Table : Property File
| Important:                                                                                                                                            | Sites that are currently running the FDA Med Guides Automatic Printing software can go directly to section [6. Upgrading to a new version of Automatic Printing](#upgrading-to-a-new-version-of-automatic-printing). |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/003.png) |                                                                                                                                                                                                                      |
Table : Adobe Errors
<table>
<caption><p>Table : FDA Med Guide Errors</p></caption>
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
<th>![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/004.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
Table : FDA Med Guide Errors
The intended audience for this document is the Information Resources Management Service (IRMS) staff responsible for installing and configuring software on VA Windows servers.
The installation procedure, including installing the third-party products listed in the pre-installation procedures, should take about an hour or less to complete.
After installation is complete, the host server should be rebooted. Any logged-on users should be advised to log off.

# Pre-installation Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility depends on third-party components to process and print Portable

Document Format (PDF) documents. These components are Windows Server, Java Runtime Environment (JRE) and Adobe Reader DC. These components must be properly installed and configured prior to installing and running the FDA Med Guides Printer Utility.

Refer to the VA Technical Reference Model (TRM) <span class="mark">REDACTED</span> for the approved versions of Windows Server, Java Runtime Environment (JRE) and Adobe Reader DC.

## Deployment scenarios 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several scenarios in which the FDA Med Guides Printer Utility can be deployed successfully. The recommended scenario is to deploy the FDA Med Guides Printer Utility, Java JRE and Adobe Reader DC on a server near the target service area. However, identifying and selecting the best scenario for a particular site is left to the discretion of individual local system administrators who are tasked with installing this package.

## Destination printers 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any printer used to print med guides must be defined as a local printer on the Windows server hosting the software. That is, the printer spooler must be hosted on the same server where the FDA Med Guides Printer Utility software is running.

## Third-party software Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Windows Server, Java Runtime Environment (JRE) and Adobe Reader DC are required to run the FDA Medication Guide Automatic Printing software. The required third-party software is not distributed as part of this package. Download and install a VA TRM compliant version of these applications from the vendors website or an approved VA web site.

All third party software should be installed using a Domain Service account that has been granted administrator privileges and will be used to run the FDA Med Guide Automatic Printing software.Refer to [Section 2.4](#domain-service-account).

### Windows Server 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Microsoft’s Windows Server software must be properly installed and configured on the server hardware. Consult the vendor’s documentation for instructions on installing Server if not already installed.

Windows Server versions must be compliant with the VA Technical Reference Model (TRM).

### Java 1.8 Runtime Environment for Windows 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides project requires a TRM compliant version of a Java Runtime Environment (JRE) 1.8 or higher (including TRM compliant versions of Amazon Corretto 8 or higher) to be installed on the host server.

<table>
<caption><p>Table : Printer Spool Errors</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>To confirm whether Java is already installed on the server, or was installed correctly, open a command window and type the command:</p>
<p><strong>java -version</strong></p>
<p>Information text should appear in the command window, indicating the nomenclature of the java version. If Java is not installed, or not installed properly, the message returned will indicate:</p>
<p>“Java is not a recognized system command.”</p></th>
</tr>
<tr class="odd">
<th>![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/005.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Table : Printer Spool Errors

If a Java Runtime Environment (JRE) is not installed or not a TRM compliant version, download a TRM compliant version of JRE compatible with the respective Windows version. Install JAVA JRE per the instructions consistent with the host operating system and downloaded instance.

> **NOTE:** The JAVA versions in the screen shots do not indicate the TRM compliant version. They are only displayed as an example.

1.  Verify a TRM compliant version of Java is downloaded and installed
    1.  If neither folder exists, or if the version is not TRM compliant, download a TRM compliant version of JAVA and install it.

> Figure : Example of Java Oracle download

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/006.png)

> Figure 2: Example of Amazon Corretto download

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/007.png)

2.  Once a TRM compliant version of Java exists, please verify the JAVA_HOME environment variable is set appropriately by following these steps.
    1.  From the File Explorer, right click on “This PC” and click Properties. The System window appears.

> Figure : Example of System Window with Advanced system settings

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/008.png)

2.  Click on Advanced System Settings to open the System Properties window:

> Figure : Example of System Properties window with Environment Variables box

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/009.png)

3.  Click the Environment Variables button.Verify a JAVA_HOME environment variable exists in the System variables section and is assigned a value consistent with the path of the installed JAVA as shown in the example screen here:

> Figure : Example of JAVA_HOME System Variable with path value

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/010.png)

> If necessary, edit the JAVA_HOME path to match the installation path of the installed JAVA.

### Adobe Reader DC for Windows 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility requires that a TRM compliant Adobe Reader DC software be installed on the host server. Adobe Reader DC is used to print chosen med guides.

#### Download Adobe Reader DC

Download a VA TRM approved version of Adobe Reader DC software and follow the installation instructions associated with the version downloaded.

#### Install Adobe Reader DC

Install Adobe Reader DC using the downloaded software. Complete the Adobe Reader DC installation by responding to the prompts as shown below.

> **NOTE:** Select “Manually check for and install updates” as shown below.

Figure : Adobe Reader DC Installation Display Prompt

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/011.png)

> **NOTE:** Select Import if Adobe displays the following prompt.

Figure : Adobe Reader DC Security Prompt

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/012.png)

## Domain Service Account 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Domain Service account must be created in Active Directory for the FDA Med Guides Automatic Printing application to work properly. The FDA Med Guides Automatic Printing task must be run using this Domain Service account as described in [Section 4.6](#create-a-new-fdamedguideprintertask-task)

### Create Domain Service Account for FDA Med Guides 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Domain Service account for the FDA Med Guides Automatic Printing application must be created in Active Directory.

Add a Domain Service account to the Administrator group on the server as it needs Administrative privileges.

Add a Domain Service account to the Server Security Admin group (for example, V21PAL IRMSSERVERSECADMIN) and the Print Operators group permissions to invoke Adobe Reader DC and send print jobs to the network printers.

Ensure the Domain Service account has permissions to view and download files from the VA Share site[.](https://vaww.cmopnational.va.gov/CR/FDAMedGuides/Forms/AllItems.aspx)

# Deployment package contents 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility deployment package consists of a single archive (ZIP) file that contains several folders, each containing the files necessary for the applications deployment. A listing and description of these folders and files are found in the Appendix.

# Installation Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation steps listed below are specific to the FDA Med Guides Printer Utility Java component.

## Obtain ZIP distribution file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The file listed below may be obtained via Secure File Transfer Protocol (SFTP). The preferred method is to access the file from the SOFTWARE directory, <span class="mark">REDACTED</span>.

This transmits the file from the first available server.

| File Name      | Retrieval Format |
|----------------|------------------|
| PSO_7_Pxxx.zip | BINARY           |

Table : Batch File Errors

Download the file and save it to the C:\temp folder.

> **NOTE:** The file name of the downloaded distribution ZIP file may be a variation from that shown in the following screen captures.

Figure : Download and save to C:\temp

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/013.png)

## Deploy files from the distribution file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Extract ZIP file contents into C:\\ 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Extract the contents of the distribution ZIP file into the root folder of the C drive (C:\\. The embedded file structure will be recreated. Locate the distribution file.

Figure : C:\Temp Folder

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/014.png)

Right click on the zip file and select ‘Extract All…’

Figure 10: Initiate the Extract All Wizard

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/015.png)

Change the default destination path to C:\\ and select the ‘Show extracted files when complete’ checkbox.

Figure : Default Destination Path

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/016.png)

Select Extract and observe the Post-Extraction screen.

Figure : Post-Extraction Screen

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/017.png)

## Edit the properties configuration file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility needs to locate the Adobe Reader DC executable so that it can instruct Adobe Reader DC to print a med guide. The path to Adobe Reader DC is stored in a properties file named fda_med_guides.properties. The default entry in the properties file is consistent with a TRM compliant Adobe Reader DC installation on a Windows Server 2012. For any other TRM compliant Windows Server versions the path’s validity must be confirmed or adjusted where applicable.

### Verify path to Adobe Reader DC program 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm that the path indicated in the following property file is correct.

| File                                              | Element           | Description                                     |
|---------------------------------------------------|-------------------|-------------------------------------------------|
| C:\FDAMedGuidesPrinter\fda_med_gui des.properties | AcrobatReaderPath | The path to the Adobe Reader DC executable file |

Table : FDA Med Guides Printer Folder and File Structure

Open the file C:\FDAMedGuidesPrinter\fda_med_guides.properties for editing. This is a text file and using a text editor like Notepad will be adequate. Locate the AcrobatReaderPath element in the list.

Figure : Example AcrobatReaderPath Element

<span class="mark">REDACTED</span>

Confirm that the path to AcroRd32.exe is correct for the installed version of Adobe Reader DC. Make proper adjustments if needed and save the changes.

### Confirm DailyPurgeTime 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DailyPurgeTime element in the properties file represents the time of a 24-hour day when the folder containing temporary work files is cleared of all files. This is an automatic clean-up process performed at the indicated time. Adjust this entry as needed to list the most convenient time to perform this operation, based on the time when system use is at a minimal.

Figure : DailyPurgeTime Example

<span class="mark">REDACTED</span>

## Import customized Adobe Reader DC Windows Registry settings 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility controls Adobe Reader in the background, while no interactive user is logged in. Adobe Reader sometimes tries to interact with a user when no user is available to reply to Adobe Reader prompts. An example of this is when Adobe Reader presents the End-User License Agreement (EULA) screen. There are Registry settings that can be set to inhibit these prompts. These are listed in the included Windows Registry Editor file.

Before starting the task (first use), the following Registry settings must be imported. Locate the NetworkServiceTaskSettings.reg file in the C:\FDAMedGuidesPrinter\installation folder, then import the settings as indicated in the screen captures below.

Figure : NetworkServiceTaskSettings.reg Registry Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/018.png)

Figure : Merge Menu Option

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/019.png)

Figure : User Account Control Dialog Box

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/020.png)

Figure : Registry Editor Dialog Box

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/021.png)

Figure : Follow Up Dialog Box for Registry Editor

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/022.png)

## Configure JAVA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Run the SSL Certificate installation batch file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility needs the approved VA provided SSL certificates necessary to access the VA Share site to complete the downloads of the FDA Medication guides. The script adds the VA provided SSL certificates to the Java cacerts trust store and are included with this distribution.

Execute the following steps to install the certificates to the JAVA cacerts keystore:

> Go to C:\FDAMedGuidesPrinter\installation directory.

> Right click on the SSL_Certificate_installation.bat file and select Run as administrator.

> Note: The script needs to be run as an Administrator, or the user needs to be a Machine Administrator in order for it to work. It is recommended to complete this while logged into the server with the Domain Service account that will be used to run the FDA Med Guide Automatic Printing software. If there are issues with running the script, refer to [Section 2.3.2](#java-1.8-runtime-environment-for-windows) for verification of the JAVA installation.

The following window will be displayed. Press any key to close the window.

Figure : SSL Certificate Installation Window

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/023.png)

If an SSL Certificate already exists, the error message shown in the figure below will be displayed to the user. If the certificate already exists, the user can proceed to the next step in the installation process.

Figure : SSL Certificate Already Exists

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/024.png)

If the error message in the screenshot below appears, the user can proceed as the certificate has been installed. The error message results when the script cannot find a JRE version installed. If JRE exists, the Automatic Printing will work, and the user can proceed with the installation.

Figure : SSL Certificate Added to the Java Keystore

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/025.png)

If there is no JRE installed, then the script will display error message, “Failed to locate any installed Java environments, please install a Java Runtime Environment”. Follow the steps as described in [Section 2.3.2](#java-1.8-runtime-environment-for-windows) to install a TRM compliant version of Java.

### Install the JAVA net.properties file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The version numbers in these figures are examples only. To verify which JAVA is installed and in which directory JAVA is installed ( e.g Program Files or Program Files x86), refer to [Section 2.3.2](#java-1.8-runtime-environment-for-windows).

For this step, navigate to the Java installation folder as described and noted in [Section 2.3.2](#java-1.8-runtime-environment-for-windows).

Navigate to the \<java installation folder\>\lib directory and locate the net.properties file.

Figure : Location of net.properties file![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/026.png)

Select the net.properties file, right click and select ‘Rename’. Rename the file net.properties.backup.

Figure 24: Example of renamed net.properties file

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/027.png)

Navigate to the C:\FDAMedGuidesPrinter\installation directory.

Figure : C:\FDAMedGuidesPrinter\installation folder

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/028.png)

Copy the net.properties file to the .\lib directory under the JRE installation path noted in [Section 2.3.2](#java-1.8-runtime-environment-for-windows).

> **NOTE:** The following screenshot is an example of the destination for the net.properties file and may vary depending on the location of the installed JRE.

Figure : Example of the Destination for the net.properties File after installation

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/029.png)

This completes the JAVA configuration.

## Create a new FDAMedGuidePrinterTask task 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FDA Med Guides Printer Utility is deployed to run as a non-interactive background process (Windows Scheduled Task) and is listed on the server’s list of scheduled tasks. This program runs in the background; therefore, not evident to users that are logged on. There is no user interface associated with the FDA Med Guides Printer Utility; therefore, there is no user interactivity.

The following characteristics apply to the task configuration:

> The name of the scheduled task is FDAMedGuidePrinterTask.

> By default, the Automatic Printing application runs under NT AUTHORITY\NETWORK SERVICE account. The Network Service account on the server may or may not have adequate permissions based on the server settings. The account MUST have permissions to download files from the VA Share Point and also requires permissions to print to the network printers.

> We strongly recommend the use of a Domain Service account created for the FDA Med Guides Automatic Printing application as suggested in [Section 2.4](#domain-service-account). To change the user account associated with FDA Med Guides from a Network Service account to a Domain Service account see instructions given in [Section 4.6.2.1](#change-user-account-associated-with-the-fdamedguideprintertask). Change User account associated with the FDAMedGuidePrinterTask.

> The C:\FDAMedGuidesPrinter\START_fda_med_guides_automatic_printing.bat batch file will be run by the task.

> The task starts in the C:\FDAMedGuidesPrinter (application) folder.

> The task is configured to run whether the assigned user is logged in or not. Typically, no user is logged in.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Important:</th>
<th rowspan="2"><p>If the FDAMedGuidePrinterTask task is configured to run using a <strong>Domain Service account</strong>, instead of the Network Service account, one of the following options must be executed.</p>
<p><em><u>Option 1:</u></em> <strong>Login to the server using the</strong> <strong>Domain Service account</strong> that is being assigned to the FDAMedGuidePrinterTask task and <strong>apply the registry keys</strong> by executing the NetworkServiceTaskSettings.reg file according to the instructions given below.</p>
<p><em><u>Option 2:</u></em> The NetworkServiceTaskSettings.reg file must be edited to <strong>replace HKEY_USERS\S-1-5-20 with the SID of the Service account</strong>, which looks like S-1-5-20, from the windows registry at the path</p>
<p>HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows</p>
<p>NT\CurrentVersion\ProfileList. Then <strong>apply the registry keys</strong> by executing the NetworkServiceTaskSettings.reg file according to the instructions given below.</p></th>
</tr>
<tr class="odd">
<th>![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/030.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Import a new Scheduler Task configuration file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A predefined task configuration XML file is distributed as part of this installation package. The file is named FDAMedGuidePrinterTask.xml, and it is located in the C:\FDAMedGuidesPrinter\installation folder.

Importing this file into Task Scheduler automatically configures the FDAMedGuidePrinterTask with default settings. After importing the settings file, saving the task creates the new task in Task Scheduler.

Follow the steps and the screenshots below to create the FDAMedGuidePrinterTask task.

Select Task Scheduler Library from Computer Management.

Figure : Task Scheduler Shown Within Computer Management

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/031.png)

Select Import Task….

Figure : Task Scheduler Library Option Menu

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/032.png)

Select FDAMedGuidePrinterTask and select Open.

Figure : FDAMedGuidePrinterTask XML File

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/033.png)

Verify settings and select OK to add the new task.

> **NOTE:** The Change User or Group field should be changed to the Domain Service account with administrator privileges that is going to be used to run the FDAMedGuidePrinterTask.

Figure : Create Task Dialog Box- example

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/034.png)

### Confirm or fine-tune the scheduled task configuration 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After creating the FDAMedGuidePrinterTask, verify that the imported settings are correct. The following screen captures represent the desired configuration settings for the FDAMedGuidePrinterTask task on a Windows Server 2012 system. The system in use should be set up in a similar fashion. Compare the following screenshots with the user’s settings and adjust accordingly—if necessary.

Figure : FDAMedGuidePrinterTask in the Task Library![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/035.png)

#### Change User account associated with the FDAMedGuidePrinterTask 

The default user is set to NT AUTHORITY\NETWORK SERVICE account. The Network Service account on the server may or may not have adequate permissions based on the server settings. In the General tab, the user account associated with the FDAMedGuidePrinterTask task can be changed from the default Windows Network Service account to the Domain Service account created for the FDA Med Guides Automatic Printing application, as shown in figures below.

> Open the options menu for the FDAMedGuidePrinterTask task and select Properties.

> In the General tab, select the Change User or Group… button.

> Enter the Domain Service account username created, or the FDA Med Guides Automatic Printing application as given in Section 2.4 and select the location (for example, Entire Directory).

> Enter the password when prompted.

The Domain Service account needs to have Administrative privileges on the server and should be added to the appropriate Printer and Server Security Admin groups so that it has permissions to invoke Adobe Reader DC and send print jobs to the network printers.

Figure 32: General Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/036.png)

Figure : Select User, Service Account, or Group

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/037.png)

The screenshots below are examples of the setup for the Triggers, Actions, Conditions, Settings and History Tabs.

Figure : Triggers Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/038.png)

Figure : Edit Trigger Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/039.png)

Figure :Actions Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/040.png)

Figure : Edit Action Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/041.png)

Figure : Conditions Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/042.png)

Figure : Settings Tab Settings

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/043.png)

Figure : Sample History Tab

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/044.png)

## Confirm correct deployment of program files 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A batch file automates the process of confirming that the necessary folders and files were deployed correctly. Confirmation is made only on files belonging to the FDA Med Guides Printer Tool.

### Run the verifying batch file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Open the options menu for the file and select Run as administrator to execute the batch file located in C:\FDAMedGuidesPrinter\installation\Verify_installation.bat. The resulting display should look like Figure 40 below. Any missing files or configuration errors should be listed in the results.

Figure : File Location

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/045.png)

Figure : Run as administrator Option

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/046.png)

Figure : Installation Confirmation result with no Errors Reported

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/047.png)

Figure : Installation Confirmation result with some Errors Reported

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/048.png)

> **NOTE:** If errors are reported, review the errors and all previous installation steps. Refer to the respective steps of the installation guide.

## Starting or stopping the FDAMedGuidePrinterTask task manually

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing and configuring the FDA Med Guides Printer Utility system, it is strongly recommended to perform a server reboot to start the FDAMedGuidePrinterTask task—the task is configured to start with the system. However, the task can be started or stopped manually.

The procedure appears in the following screen captures. To start the task, select Run from the pop-up menu. To stop the task, select End. To confirm that the task is running, see the text indicated in the Status column. Ready means that the task is active, but not running. Running means that the task is running.

Figure : FDAMedGuidePrinterTask Task Listed in the Task Scheduler

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/049.png)

Figure : Select Task and Open Menu

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/050.png)

Figure : Task Menu Option Run

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/051.png)

Figure : Task Shown in Running State

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/052.png)

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

Figure : Adobe Reader DC is listed in the Task Manager After a Print Job Request is Sent

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/053.png)

# Back-out/Uninstall Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Stop the FDAMedGuidesPrinterTask task in the Task Scheduler.

Figure 50: Stopping the FDAMedGuidesPrinterTask in the Task Scheduler ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/054.png)

Delete the FDAMedGuidesPrinterTask task from the Scheduler list.

Figure 51: Deleting the FDAMedGuidesPrinterTask in the Task Scheduler ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/055.png)

In the Task Manager:

> Select the Details tab.

> Find the task named AcroRd32.exe running under the FDA Med Guides user account (that is, the account used to run the FDAMedGuidePrinter Task).

> Figure : Acrobat Reader process in the Task Manager

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/056.png)

> Right-click and select End Task. Select End Process in the confirmation dialog.

> Figure : Deleting Acrobat Reader process in the Task Manager

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/057.png)

> Find the task named java.exe running under the FDA Med Guides user account.. Right-click and select End Task. Select End Process in the confirmation dialog. Delete the C:\FDAMedGuidesPrinter folder and all its contents.

# Upgrading to a new version of Automatic Printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Uninstall the old version of FDA Med Guides as shown in [Section 5](#back-outuninstall-procedures).

> Do not uninstall Java or Adobe unless a TRM compliant version needs installed.

> If needed, install a TRM compliant version of Adobe Reader DC and/or Java by following the instructions given in [Section 2.3.3](#adobe-reader-dc-for-windows) and/or [Section 2.3.2](#java-1.8-runtime-environment-for-windows) respectively.

> Follow the installation steps in [Section 4](#installation-procedure) to install the new version of FDA Med Guides Automatic Printing.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some of the most common issues found in the FDA Med Guides application are listed here:

> No output reaches the destination printer spool.

> No file is downloaded to the C:\FDAMedGuidesPrinter\workspace\medguides folder from the CMOP Portal.

> No temporary PDF file is created in the C:\FDAMedGuidesPrinter\workspace\temp folder.

> Adobe Reader isn’t responding or is responding incorrectly.

> The Service Account assigned to the FDAMedGuidePrinterTask task is unable to connect to CMOP URL.

If any of these issues or others occur on a new install it is recommended to re-trace each step described in this document and ensure a proper installation took place.

For failures of an existing deployment it is best to open the C:\FDAMedGuidesPrinter\debugging—0.log file and attempt to identify the actual cause of the failure in hopes of pinpointing the issue.

## Adobe issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a new version of Adobe is installed or the current version is re-installed, ensure the steps to update the windows registry have been performed as described in [Section 4.4](#import-customized-adobe-reader-dc-windows-registry-settings) of this document. These registry settings ensure that Adobe will not prompt for user interaction in the background thus halting Adobe functionality.

These Registry settings are bound to individual user accounts and must be applied to the user account selected to control the FDAMedGuidePrinterTask task. You may need to adjust the NetworkServiceTaskSettings.reg file to reflect the correct user account.

During any installation of Adobe, if and/or when prompted to perform automatic updates, provide the answer to DISABLE automatic updates. Accepting any type of automatic Adobe processing could cause Adobe to stall.

Cannot find Adobe Reader DC

<table>
<caption>Adobe ErrorsThis tables shows the errors by symptom and possible solution.</caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>Symptom</th>
<th>Possible solution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>An error indicates that Adobe Reader DC executable can’t be located.</td>
<td><p>Verify that the path pointing to the Reader executable is correct in the</p>
<p>C:\FDAMedGuidesPrinter\fda_med_guides.properties file</p></td>
</tr>
</tbody>
</table>

Adobe ErrorsThis tables shows the errors by symptom and possible solution.

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
<td>CMOP site is down.</td>
<td>Verify by attempting to access the CMOP SharePoint site by copying the Test URL found in the fda_med_guides.properties file beginning with https through and including FDAMedGuides. Paste the URL in a browser on the print server.</td>
</tr>
<tr class="even">
<td>Service account user is inconsistent or invalid.</td>
<td>Verify the service account has the correct permissions to access the CMOP server.</td>
</tr>
<tr class="odd">
<td>An error page is printed instead of the expected med guide.</td>
<td><p>The Med Guide PDF file doesn’t exist at the CMOP Portal or the print server cannot access the CMOP URL.</p>
<p>Verify that the PDF file exists, or that the PDF file name indicated in the print request is correct by copying the Test URL found in the fda_med_guides.properties file beginning with https through and including FDAMedGuides. Paste the URL in a browser on the print server and locate the desired Med Guide.</p>
<p>Open the C:\FDAMedGuidesPrinter\debugging—0.log file to determine if any http 401 or SSL PKI errors exist.</p>
<p>For http 401 errors verify the JAVA installation steps and the net.properties file were installed properly as described in <a href="#install-the-java-net.properties-file">Section 4.5.2</a></p>
<p>For PKI errors, execute the C:\FDAMedGuidesPrinter\installation\ SSL_Certificate_installation.bat to ensure the proper certificates are being referenced by JAVA.</p></td>
</tr>
<tr class="even">
<td>Java uninstall/reinstall</td>
<td><p>If Java is uninstalled and reinstalled on the FDA Med Guides print server, execute the following SSL script to add CMOP SSL certificate to the Java trust store.</p>
<p>C:\FDAMedGuidesPrinter\installation\ SSL_Certificate_installation.bat</p>
<p>Follow the steps described in <a href="#install-the-java-net.properties-file">Section 4.5.2</a> of this document to copy the net.properties file to the newly installed JAVA instance.</p></td>
</tr>
<tr class="odd">
<td>Adobe Acrobat Reader uninstall/reinstall</td>
<td><p>If the Adobe Acrobat Reader is uninstalled and reinstalled on the FDA Med Guides print server, execute the following scripts to add Adobe keys to the Windows registry and to verify the FDA Med Guides installation.</p>
<p>C:\FDAMedGuidesPrinter\installation\ NetworkServiceTaskSettings.reg</p>
<p>C:\FDAMedGuidesPrinter\installation\ Verify_installation.bat</p></td>
</tr>
</tbody>
</table>

FDA Med Guide ErrorsThis table shows the errors by symptom and possible solution.

## Nothing is sent to the destination printer spool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Symptom                                                    | Possible solution                                                                            |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Adobe Reader DC is malfunctioning                          | Using Task Manager, kill any AcroRd32.exe processes belonging to the pertinent user account. |
| Destination printer name in med guide request is incorrect | Verify that the printer name is correct.                                                     |

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
<td><p>Invoking the</p>
<p>START_fda_med_guides_automatic_printing.bat batch file fails to start the Java application and</p>
<p>indicates: Exception in thread "main" java.lang.NoClassDefFoundError</p>
<p>Figure : JAR File Error</p>
<p>![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/058.png)</p></td>
<td>Verify that paths indicated in batch and properties files are correct, particularly the path to the JAR file.</td>
</tr>
</tbody>
</table>

Batch File ErrorsThis table shows the errors by symptom and possible solution.

Figure : Disabling Protected Mode at Startup

![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/059.png)

## Network Service account and Adobe Reader 9 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a known “ROAMING PROFILE” issue with Adobe Reader 9.x that causes it to malfunction under certain circumstances while assigning the NETWORK SERVICE account to the FDAMedGuidePrinterTask task. For this reason, Adobe Reader 9.x is not recommended for this application. Use a TRM approved version Adobe Reader DC instead.

## Reinstall SSL Certificate 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Java/JRE is reinstalled, the CMOP SSL certificates also need to be reinstalled into the JAVA keystore according to the instructions given in [Section 4.5](#configure-java).

## Issues with Network Service account 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the FDAMedGuidePrinterTask is run under the NETWORK SERVICE account:

> If there are delays in printing or if the Med Guides do not print, a Domain Service account with the highest privileges should be created and used instead of using the NETWORK SERVICE account.

> If Domain Service account cannot be created, the FDAMedGuidePrinterTask can be run under the Administrator account. This would require the Administrator to be logged in while the task is running. This is not a recommended approach.

## Printing Issues 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you experience print issues or delays with the NETWORK SERVICE account, we strongly recommend that you use a Domain Service account created for the FDA Med Guides Automatic Printing application. This account needs to have Administrative privileges on the server.

> Add the NETWORK SERVICE account or the Service account to the Server Security Admin group so that it has permissions to invoke Acrobat and send print jobs to the network printers.

> Check if the NETWORK SERVICE account or the Service account has permissions to access the printer.

> Add NETWORK SERVICE account or the Service account to the ‘Users’ and ‘Print Operators’ groups.

> Figure : Add Service account to Administrators, Users and Print Operators groups

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/060.png)

> Figure : Example of adding the NETWORK SERVICE account to Administrators group

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/061.png)

> If Med Guides appear in the temp folder but do not go to the printer queue, go to Services and stop the Print Spooler service and start it again.

> Figure : Restarting Print Spooler service

> ![](java-fda-medication-guides-automatic-printing-project-installation-guide-pss-7-6/062.png)

> Restart FDAMedGuidePrinterTask

> Go to Task Scheduler and stop the FDAMedGuidePrinterTask task by selecting End.

> Go to Windows Task Manager. Find any AcroRd32.exe and java.exe tasks running under the NETWORK SERVICE account or the Service account and stop them by selecting End Process.

> Go to Task Scheduler again and start the FDAMedGuidePrinterTask task by selecting Run.

## Nightly Server Reboot recommendation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Given the number of Med Guides that are printed each day and due to the load on the server, it is recommended that the Windows server be rebooted every night to free up resources and to cleanup any hung tasks.

## Increase the priority of java.exe and AcroRd32.exe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run a PowerShell script that increases the priority of java.exe and AcroRd32.exe from Below Normal to High. This may speed up the execution of printing under the NETWORK SERVICE account. Below are the lines to run in PowerShell. This needs to be run after the server starts the FDAMedGuidePrinterTask task.

\$processname="java.exe"

\$process=Get-WmiObject win32_process -f "name='\$processname'"

\$process.SetPriority(128)

\$processname="AcroRd32.exe"

\$process=Get-WmiObject win32_process -f "name='\$processname'" \$process.SetPriority(128)

# Appendix 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After extracting the contents of the ZIP file, the below FDA Med Guides Printer folder structure and files should be available on the C:\\ drive.

<table>
<caption>FDA Med Guides Printer Folder and File StructureThis table shows lists the folder and file strucutre by path, type, and description</caption>
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
<td>Folder containing predefined configuration files</td>
</tr>
<tr class="even">
<td><p>C:\FDAMedGuidesPrinter\installation\CMOP_SSL_</p>
<p>Certificate</p></td>
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
<td>C:\FDAMedGuidesPrinter\fda_med_guides_autom atic_printing_1.0.1.x.jar</td>
<td>Java archive</td>
<td><p>Main jar file containing all</p>
<p>Java code for the FDA</p>
<p>Med Guides Printer Tool</p></td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\ SSL_Certificate_installation.bat</td>
<td>Batch file</td>
<td><p>Batch file to add CMOP SSL certificate to the Java trust store and set</p>
<p>JAVA_HOME</p></td>
</tr>
<tr class="odd">
<td><p>C:\FDAMedGuidesPrinter\installation\CMOP_SSL_ Certificate\</p>
<p>VA-Internal-S2-RCA1-v1.cer</p>
<p>VA-Internal-S2-ICA1-v1.cer</p>
<p>VA-Internal-S2-ICA2-v1.cer</p>
<p>VA-Internal-S2-ICA3-v1.cer</p>
<p>VA-Internal-S2-ICA4.cer</p>
<p>VA-Internal-S2-ICA5.cer</p>
<p>VA-Internal-S2-ICA6.cer</p>
<p>VA-Internal-S2-ICA7.cer</p>
<p>VA-Internal-S2-ICA8.cer</p>
<p>VA-Internal-S2-ICA9.cer</p></td>
<td>Certificate files</td>
<td>SSL Certificates that are issued by VA which will be added to the Java trust store</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\ FDAMedGuidePrinterTask.xml</td>
<td>XML file</td>
<td><p>Configuration file used to create the</p>
<p>FDAMedGuidePrinterTask task</p></td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\installation\ NetworkServiceTaskSettings.reg</td>
<td><p>Windows</p>
<p>Registry import</p>
<p>file</p></td>
<td><p>Configuration file used to set up the Adobe Reader DC</p>
<p>setting for use by the NT</p>
<p>AUTHORITY\NETWORKS</p>
<p>ERVICE user</p></td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\ Verify_installation.bat</td>
<td>Batch file</td>
<td>Batch file used to confirm a successful deployment of the FDA Med Guides Printer Utility</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\lib\commons-io-2.4.jar</td>
<td>Java archive</td>
<td><p>Supporting third-party</p>
<p>Apache Commons</p>
<p>Java library</p></td>
</tr>
<tr class="even">
<td><p>C:\FDAMedGuidesPrinter\lib\commons-lang3-</p>
<p>3.3.2.jar</p></td>
<td>Java archive</td>
<td><p>Supporting third-party</p>
<p>Apache Commons</p>
<p>Java library</p></td>
</tr>
<tr class="odd">
<td><p>C:\FDAMedGuidesPrinter\lib\commons-logging-</p>
<p>1.1.3.jar</p></td>
<td>Java archive</td>
<td><p>Supporting third-party</p>
<p>Apache Commons</p>
<p>Java library</p></td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib\fontbox-1.8.5.jar</td>
<td>Java archive</td>
<td>Supporting third-party PDFBox Java library.</td>
</tr>
<tr class="odd">
<td>C:\FDAMedGuidesPrinter\lib\jempbox-1.8.5.jar</td>
<td>Java archive</td>
<td>Supporting third-party PDFBox Java library.</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\lib\pdfbox-1.8.5.jar</td>
<td>Java archive</td>
<td>Supporting third-party PDFBox Java library.</td>
</tr>
<tr class="odd">
<td>Log files in folder C:\FDAMedGuidesPrinter</td>
<td>*.log</td>
<td>Log files are used for debugging purposes only and are created AFTER the initial use of the program.</td>
</tr>
<tr class="even">
<td>C:\FDAMedGuidesPrinter\installation\net.properties</td>
<td>JAVA properties file</td>
<td>JAVA Properties file for controlling access to network hosts from JAVA processes.</td>
</tr>
</tbody>
</table>

FDA Med Guides Printer Folder and File StructureThis table shows lists the folder and file strucutre by path, type, and description