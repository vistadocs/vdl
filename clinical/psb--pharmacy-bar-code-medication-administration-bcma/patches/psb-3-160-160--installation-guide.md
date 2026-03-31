---
title: BCBU IRISHealth Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: BCBU IRISHealth
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3.160
patch_id: PSB*3.160*160
group_key: "PSB:PSB:3.160"
file_numbers: []
security_keys: []
menu_options: 3
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - bcbu
  - installation
  - table
  - contents
  - irishealth
  - guide
  - iris
  - bcma
  - workstation
  - printer
page_count: 0
word_count: 2723
section_count: 13
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/PSB_3_160_BCBU_Workstation_IrisHealth_install_2026_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/PSB_3_160_BCBU_Workstation_IrisHealth_install_2026_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

Bar Code Medication Administration (BCMA) BCMA Backup System (BCBU) InterSystemsIRISHealth Installation and Setup Guide

![](bcbu-irishealth-installation-guide/001.png)

> February 2026

> Department of Veterans Affairs (VA)

> Office of Information and Technology (OIT)Product Development (PD)

Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 23%" />
<col style="width: 40%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/2026</td>
<td>PSB*3*160</td>
<td><p>Rewrote file download</p>
<p>Rewrote installation process</p>
<p>Created UsersExport.xml</p>
<p>Created ServicesExport.xml</p>
<p>Created IRIS configuration script</p>
<p>Clarified ambiguities</p>
<p>Removed outdated contents</p>
<p>Made shortcut optional</p>
<p>Regenerated Table of Contents</p></td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>10/2022</td>
<td>PSB*3*138</td>
<td><p>Document updated for IRISHealth</p>
<p>Image caption updates</p>
<p>Fixed Table of Contents</p>
<p>Renumbered steps</p></td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>3/2019</td>
<td>PSB*3*122</td>
<td>Document updated for Cache version 2017</td>
<td>Redacted</td>
</tr>
<tr class="even">
<td>4/2015</td>
<td>PSB*3*84</td>
<td>Document updated by Kevin Cownie. Entire document reformatted.</td>
<td>Redacted</td>
</tr>
<tr class="odd">
<td>07/11</td>
<td>PSB*3*65</td>
<td><p>Footers updated; removed</p>
<p>HSITES and added Product Development, removed VistA.</p>
<p>Renamed instances of CACHE to CACHE throughout the document. Updated version to reflect BCMA v3.0 version.</p></td>
<td></td>
</tr>
<tr class="even">
<td>08/03</td>
<td>PSB*2*17</td>
<td><p>Original Released Bar Code</p>
<p>Medication Administration</p>
<p>Backup System (BCBU)</p>
<p>InterSystems CACHE</p>
<p>Workstation Installation Setup Guide.</p></td>
<td></td>
</tr>
</tbody>
</table>
# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [General Background Information](#general-background-information)
    - [Intended Audience](#intended-audience)
    - [Software Disclaimer](#software-disclaimer)
    - [Documentation Disclaimer](#documentation-disclaimer)
    - [Document Conventions](#document-conventions)
  - [Prerequisites](#prerequisites)
- [Gather Installation Files](#gather-installation-files)
  - [Obtain License File](#obtain-license-file)
  - [Download Installation Files](#download-installation-files)
- [Install BCBU](#install-bcbu)
  - [Install IRIS](#install-iris)
    - [Run the EXE file as Administrator](#run-the-exe-file-as-administrator)
  - [Stop IRIS Service](#stop-iris-service)
  - [Copy files to “C:\InterSystems\IRISHealth”](#copy-files-to-cintersystemsirishealth)
  - [Start IRIS Service](#start-iris-service)
  - [Configure IRIS](#configure-iris)
- [Set Up BCBU Shortcut (Optional)](#set-up-bcbu-shortcut-optional)
- [Set Up BCBU Printer](#set-up-bcbu-printer)
  - [Connect the printer to the workstation](#connect-the-printer-to-the-workstation)
  - [![](bcbu-irishealth-installation-guide/038.png)5.2. Install the Windows printer drivers. Use Generic Drivers (Recommended)](#bcbu-irishealth-installation-guide038png52-install-the-windows-printer-drivers-use-generic-drivers-recommended)
  - [Rename Windows printer to BCBU PRINTER](#rename-windows-printer-to-bcbu-printer)
- [Initialize New BCBU with User and Patient Data](#initialize-new-bcbu-with-user-and-patient-data)
This document contains instructions for the installation of IRISHealth on Microsoft Windows workstations.

## General Background Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These instructions are specific to installing IRIS on Windows workstations for the use of IRISHealth with BCMA Backup system (BCBU).

### Intended Audience 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is intended for VA personnel responsible for the installation of IRISHealth for the use of IRISHealth with BCMA Backup (BCBU) system.

This document presumes a working knowledge of Microsoft Windows Operating Systems.

### Software Disclaimer 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software was developed at the Department of Veterans Affairs (VA) by employees of the

Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software were used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

### Documentation Disclaimer 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of VA.

### Document Conventions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document uses the following typographic conventions:

- Controls, options, and button names are shown in Bold.
- A vertical bar is used to separate successive menu choices. For example: “Click File \|

Open” means: “Click the File menu; then click the Open option.”  Keyboard key names are shown in bold and in brackets.

- Sample output is shown in monospace. For example: BCBUIRISDATmmddyy.zip
- Important or required information is shown in a Note.

## Prerequisites 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation requires administrator privileges through local admin account logon.

This document provides instructions for installing InterSystems IRISHealth on workstations without a prior instance. If you have existing IRISHealth, uninstall it first via Settings - Installed Apps – Uninstall, delete the C:\InterSystems folder, then come back to this instruction. Installation will fail if C:\InterSystems folder exists.

# Gather Installation Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Obtain License File 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA BU systems require an IRIS license – also referred to as a “key” – to run properly. Please note the following about the license:

- Each site has one point of contact (POC) for IRIS Licenses
- Each site has a single key for all their BCMA BU workstations, i.e. one key per site
- Keys have a 30-year expiration date

For new licenses enter a Service Now Ticket to group:

IO.HBMC.FO.APP.VADCLIN.Triage

Once you receive the key, save it as “iris.key” to folder “C:\BCMABU” on the BCBU workstation. Create the folder “C:\BCMABU” if it doesn’t exist.

## Download Installation Files 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download files via the links below, and save them in the C:\BCMABU folder:

<https://download.vista.med.va.gov/index.html/SOFTWARE/PSB_3_BCBU_DAT_SYSTEM_R022526_PSB_3_160.zip>

<https://download.vista.med.va.gov/index.html/SOFTWARE/PSB_3_BCBU_IG_EXE_IRIS24_R022526_PSB_3_160.zip>

Unzip both files into the C:\BCMABU folder. Below is the list of required files for installation:

- bcma.ico
- cube.ico
- export.ro
- iris.cpf
- IRIS.DAT
- iris.key
- IRISHealth-2024.1.2.398.0.24281-win_x64.exe
- PSB_3_160_BCBU_Workstation_IrisHealth_install_2026.docx (This file)
- ServicesExport.xml
- UsersExport.xml

# Install BCBU 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Install IRIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Run the EXE file as Administrator 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Right-click the file C:\BCMABU\\ IRI SHealth-2024.1.2.398.0.24281-win_x64.exe and Select “Run as administrator”.

Be patient. The software may take quite a while to show signs of action.

> ![](bcbu-irishealth-installation-guide/002.png)

Provide username and password for a privileged account on this computer. If you don’t have it, seek assistance from a privileged workstation administrator.

> 2\. Accept the license agreement, then click “Next”

![](bcbu-irishealth-installation-guide/003.png)

3.  At “InterSystems IRIS Instance Name” pop-up, overwrite the default “IRISHEALTH” by entering “CACHE”, then click “Next”

![](bcbu-irishealth-installation-guide/004.png)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> **NOTE:** Be sure to change the Instance Name from the default value to CACHE. Failure to do so will result in an improperly configured BCMA BU system which may not work correctly. If this happens, the recommendation is to uninstall IRISHealth, delete the C:\InterSystems folder and start the installation from scratch.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.  At the “Destination Folder” box, click “Next”

> ![](bcbu-irishealth-installation-guide/005.png)

5.   At the “Setup Type” box, select “Development”, click “Next”

![](bcbu-irishealth-installation-guide/006.png)

6.  ![](bcbu-irishealth-installation-guide/007.png)At the “Local Web Server” box, select “Continue the installation without Web Gateway”, then click “Next”
7.  ![](bcbu-irishealth-installation-guide/008.png)At “Install Unicode Support” box, select “8-bit”, then click “Next”
8.  ![](bcbu-irishealth-installation-guide/009.png)At “Initial Security Settings” box, select “Normal”, then click “Next”.
9.  ![](bcbu-irishealth-installation-guide/010.png)At “Enter Credentials for InterSystems IRIS Service” box, select “Run InterSystems IRIS under default SYSTEM account”, then click “Next”.
10. ![](bcbu-irishealth-installation-guide/011.png)At “InterSystems IRIS Users configuration”, input a password and record it. It’s recommended to use this same password in the next step. Click “Next”.
11. At “InterSystems IRIS Users configuration” (again), input the same password, then click “Next”.

> ![](bcbu-irishealth-installation-guide/012.png)

12. ![](bcbu-irishealth-installation-guide/013.png)At “Ready to Install the Program”, verify the entries, then click “Install”

> 13\. It takes about 8-10 minutes to finish.

## Stop IRIS Service 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to stop then restart the IRIS application to configure IRIS for BCMA BCBU.

1.  ![](bcbu-irishealth-installation-guide/014.png)In the Windows Start menu, type “stop”
2.  In the pop-up menu, select the “Stop InterSystems IRIS \[CACHE\]

![](bcbu-irishealth-installation-guide/015.png)

3.  ![](bcbu-irishealth-installation-guide/016.png)In the pop-up window, make sure “Shut down” is selected, then click “OK”
4.  ![](bcbu-irishealth-installation-guide/017.png)Wait for it to stop and disappear.

## Copy files to “C:\InterSystems\IRISHealth” 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While IRIS is shut down, copy below files from C:\BCMABU to target folders:

| Copy This File     | To This Folder                   |
|--------------------|----------------------------------|
| C:\BCMABU\iris.cpf | C:\InterSystems\IRISHealth\\     |
| C:\BCMABU\iris.key | C:\InterSystems\IRISHealth\mgr\\ |

## Start IRIS Service 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the above 2 files have been copied over, start IRIS.

1.  ![](bcbu-irishealth-installation-guide/018.png)In the Windows search menu, type “start”
2.  ![](bcbu-irishealth-installation-guide/019.png)In the pop-up menu, select “Start InterSystems IRIS \[CACHE\]”
3.  ![](bcbu-irishealth-installation-guide/020.png)Below pop-up will display momentarily and disappear.

## Configure IRIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Starting with this version, IRIS no longer has a built-in web server and thus the Management Portal web configurations will be no longer available. All configurations are manually performed now via the BCBU terminal. A script was created to facilitate the work.

1.  ![](bcbu-irishealth-installation-guide/021.png)While BCBU is running, type “Terminal” in the Windows search field:
2.  Select the “Terminal \[CACHE\]” application:

![](bcbu-irishealth-installation-guide/022.png)

3.  BCBU will launch a terminal like below:

> ![](bcbu-irishealth-installation-guide/023.png)

4.  Log in to the BCBU terminal as user “\_system”, its password is the one you set during the installation, as shown below:

> ![](bcbu-irishealth-installation-guide/024.png)

5.  After successful login, one should see something like “VISTA\>” or “USER\>” or “SYS\>” prompt. This is where IRIS configuration script will be run to configure the system. The script is stored in a protected Excel file to prevent accidental changes to the commands.
6.  Open the Excel file below:

> ![](bcbu-irishealth-installation-guide/025.png)

![](bcbu-irishealth-installation-guide/026.png)and copy the command texts (One column only!) under the “Commands” column from rows 4-8 (No more no less):

7.  Then paste them at the BCBU terminal prompt. The pasted commands will be executed in the terminal. After it finishes, it should look like below:

![](bcbu-irishealth-installation-guide/027.png)

8.  At the “%SYS\>” prompt, type “h” for halt and press Enter, the terminal should disappear.
9.  Now, restart IRIS using the “Stop InterSystems IRIS \[CACHE\]” menu command:

![](bcbu-irishealth-installation-guide/028.png)

At this stage, IRIS configuration is complete.

# Set Up BCBU Shortcut (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the BCBU workstation has the previous BCMA BACKUP shortcut, it should still work after this installation because it points to the same executable and it has the same command option. In this case, you can skip this entire section 4.

In this section you will create the desktop shortcut to the BCMA Backup software.

1.  Delete existing BCMA Backup Icon

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> **NOTE:** This step should only be performed on workstations which did a conversion from Cache to IRISHealth.

Workstations which did a new installation of IRISHealth should skip this step.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Delete the existing “BCMA Backup” icon on the workstation desktop. This icon only works with Cache and will not work with the IRISHealth software and so should be deleted.

2.  Create shortcut on desktop

![](bcbu-irishealth-installation-guide/029.png)To create the shortcut, right click anywhere on the desktop and select “New/Shortcut”.

3.  Enter path to shortcut location
- In the “Type the location of the item” dialog box, type

C:\InterSystems\IRISHealth\bin\Iristerm.exe /console=cn_ap:cache\[VISTA\]

![](bcbu-irishealth-installation-guide/030.png)Then click “Next”

4.  Enter shortcut name
- ![](bcbu-irishealth-installation-guide/031.png)When prompted, enter a name that will be displayed with the shortcut. A suggested name is “BCMA BACKUP” but sites can use any name they choose. Then click “Finish”.
5.  Change BCBU icon
    - ![](bcbu-irishealth-installation-guide/032.png)Click the right mouse button on the new icon, then select “Properties”
6.  ![](bcbu-irishealth-installation-guide/033.png)Click “Change Icon”
7.  ![](bcbu-irishealth-installation-guide/034.png)Select “C:\BCMABU\bcma.ico” or sites may choose their own icon. Included icons are “bcma.ico” and “cube.ico” (old Cache), then click OK
8.  Click Apply and then OK

![](bcbu-irishealth-installation-guide/035.png)

9.  ![](bcbu-irishealth-installation-guide/036.png)If you used the “bcma.ico” icon provided with the ZIP file, it will look like this on the desktop:
10. Copy shortcut BCBU icon to “All User” desktop
    - Double-Click the BCBU shortcut icon to enter the Backup system on the PC Workstation. Use the appropriate access and verify code to access the system.

> ![](bcbu-irishealth-installation-guide/037.png)

11. Workstation setup is complete

This completes the setup of InterSystems IRISHealth on the BCBU contingency workstation. Refer to the “BCMA V.3.0 Backup System (BCBU) Version 3 Installation Guide” to complete the VistA side of the package setup.

# Set Up BCBU Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Connect the printer to the workstation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ![](bcbu-irishealth-installation-guide/038.png)5.2. Install the Windows printer drivers. Use Generic Drivers (Recommended) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Some workstations may work correctly with the model specific printer driver. If printing still does not work, then this is often fixed by changing the printer driver to “Generic / Text Only”.

## Rename Windows printer to BCBU PRINTER 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Windows printer name should be renamed to “BCBU PRINTER” (case sensitive) in order to match the name of the printer defined within the BCBU application.

# Initialize New BCBU with User and Patient Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On a new BCBU system installation, the BCBU database is not populated with patients or users. It must be initialized with this information from the site’s VistA system before patient data is available and users can access the new BCBU system. The tasks for initializing a new BCBU system are described in detail in the “BCMA V.3.0 Backup System (BCBU) Version 3 Installation Guide” section “Sample PC Workstation Database Initialization”. This document can be found in the VistA Virtual Documentation Library at <https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/PSB_3_0_P108_ig.docx><u>.</u>

As an overview, initializing a new system consists of performing the following tasks on the site’s VistA system. You may need to contact your VistA support personnel for assistance.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 45%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>Task</th>
<th>VistA Option</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1. Configure the HL7 logical links</td>
<td>Link Edit [HL EDIT LOGICAL LINKS]</td>
<td>Defines the IP address or DNS name of the BCBU workstation</td>
</tr>
<tr class="even">
<td>2. Associate the HL7 logical link to VistA BCBU application</td>
<td><p>Associate Backup Workstations with a</p>
<p>Division [PSB BCBU LINK</p>
<p>ASSOCIATIONS]</p></td>
<td>Associates the HL7 logical link as a subscriber to the VistA BCMA Backup software so the workstation will receive BCMA HL7 messages from VistA</td>
</tr>
<tr class="odd">
<td>3. Run workstation initialization to populate patient data</td>
<td><p>Depending upon your site’s configuration, run ONE of the following options:</p>
<p>Default Workstation Initialize [PSB BCBU INIT WRKSTN DFT]</p>
<p>OR</p>
<p>Divisional Workstation Initialize</p>
<p>[PSB BCBU INIT WRKSTN DIV</p></td>
<td>Sends current patient demographics and Inpatient Pharmacy orders to the BCBU workstations</td>
</tr>
<tr class="even">
<td><p>4. Run the VistA user</p>
<p>initialization to populate users’ access/verify codes:</p></td>
<td>Initialize a Backup Workstation with BCMA User [PSB BCBU USER INIT]</td>
<td>Sends all BCMA authorized users’ access/verify code information to the BCBU workstations</td>
</tr>
</tbody>
</table>

Initialization options 3 and 4 are under menu option BCMA Backup System (Vista) \[PSB BCBU VISTA MAIN\]. Vista SECURITY KEY assignment of PSB BUMGR is required.

Select OPTION NAME: PSB BCBU VISTA MAIN BCMA Backup System (Vista)

LNK Associate Backup Workstations with a Division

DFT Default Workstation Initialize

DIV Divisional Workstation Initialize

USR Initialize a Backup Workstation with BCMA Users PAT Single Patient Init