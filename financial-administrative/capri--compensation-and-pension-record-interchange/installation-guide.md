---
title: CAPRI GUI Installation Supplemental Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: 
app_code: CAPRI
app_name: Compensation and Pension Record Interchange
section: FIN
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - capri
  - table
  - contents
  - installation
  - windows
  - class
  - files
  - reflection
  - patch
  - dvba
page_count: 0
word_count: 4176
section_count: 10
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/capri_gui_isg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/capri_gui_isg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=133"
---

![](capri-gui-installation-supplemental-guide/001.png)

Compensation and Pension Record Interchange (CAPRI)

GUI Installation Supplemental Guide

August 2015Version 3.10Department of Veterans AffairsOffice of Information and Technology (OIT)Management & Financial Systems

Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 47%" />
<col style="width: 25%" />
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
<td>May 2011</td>
<td>1.0</td>
<td>Initial Document developed for Patch DVBA *2.7*168.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>January 2012</td>
<td>2.0</td>
<td>Document reviewed for Patch DVBA*2.7*180. Additional instructions provided for Windows 7 installations.</td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>Jun 2012</td>
<td>3.0</td>
<td>Document reviewed for Patch DVBA*2.7*181. Additional information provided for new VACAPRIVVA.dll file included with CAPRI v181.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Aug 2012</td>
<td>3.1</td>
<td>Added information for new CAPRI_Help.chm file included with CAPRI v181.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Mar 2013</td>
<td>3.2</td>
<td>Added installation specific information to correct issues with certain Windows 7 fonts sizes.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>June 2013</td>
<td>3.3</td>
<td>Added instruction for installation of Microsoft Office Document Imaging 2007 for Windows 7 Workstations to view .TIFF files</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>January 2014</td>
<td>3.4</td>
<td><p>Additional information provided for new Libeay32.dll &amp; Ssleay32.dll files included with CAPRI v186.</p>
<p>Added installation instructions for the Authentication Server.</p></td>
<td><p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>March 2014</td>
<td>3.5</td>
<td>Added information for qpdf.exe, libgcc_s_dw2-1.dll, libstdc++6.dll and qpdf13.dll files for PDF Compression included with CAPRI v186 with Security enhancement.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>December 2014</td>
<td>3.6</td>
<td>Update section 3.1 to correctly describe the additional installation files</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>December 2014</td>
<td>3.7</td>
<td>Added section 3.5 <strong>Shared Network Drive or CAPRI access via CPRS Installations. Must be performed for users to access PDF documents via Get Docs from DAS</strong></td>
<td><p>REDACTED</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>January 2015</td>
<td>3.8</td>
<td>Added Install and Rollback Procedures to this guide to eliminate the similar document “Installation and Rollback Guide”</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>February 2015</td>
<td>3.9</td>
<td>Updated for Patch 190</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>April 2015</td>
<td>3.10</td>
<td><p>Updated for Patch Select FIELD: 103 REMARKS SENT TO CONTRACTOR (word-processing)</p>
<p>LABEL: REMARKS SENT TO CONTRACTOR Replace @</p>
<p>SURE YOU WANT TO DELETE THE ENTIRE 'REMARKS SENT TO CONTRACTOR' FIELD?</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>August 2015</td>
<td>3.11</td>
<td>Updated for Patch 192</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Preface

Purpose of the Installation Guide

This GUI Installation Supplemental Guide provides instruction for installation of CAPRI.exe and associated files to accommodate the introduction of Attachmate Reflection, the CAPRI .map file and address a Windows 7 font size issue.

Reference Numbering System

This document uses a numbering system to organize its topics into sections and show the reader how these topics relate to each other. For example, section 1.3 means this is the main topic for the third section of Chapter 1. If there were two subsections to this topic, they would be numbered 1.3.1 and 1.3.2. A section numbered 2.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third topic of Chapter 2. This numbering system tool allows the reader to more easily follow the logic of sections that contain several subsections.

Table of Contents

# Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Purpose](#purpose)
- [Pre-Installation](#pre-installation)
  - [Attachmate Reflection Installation Requirements](#attachmate-reflection-installation-requirements)
- [CAPRI VistA Server Installation Procedures](#capri-vista-server-installation-procedures)
  - [VistA Patch DVBA\2.7\192](#vista-patch-dvba27192)
    - [FILE BACKUP](#file-backup)
    - [VISTA INSTALLATION](#vista-installation)
  - [CAPRI GUI v192 Client Software & User Documentation](#capri-gui-v192-client-software-user-documentation)
- [CAPRI GUI Installation Procedures](#capri-gui-installation-procedures)
  - [Additional Installation Files](#additional-installation-files)
    - [VACAPRIVVA.dll](#vacaprivvadll)
    - [LIBEAY32.DLL & SSLEAY32.DLL](#libeay32dll-ssleay32dll)
    - [QPDF.EXE, QPDF13.DLL, LIBGCCSDW2-1.DLL & LIBSTDC++-6.DLL](#qpdfexe-qpdf13dll-libgccsdw2-1dll-libstdc-6dll)
    - [CAPRIHelp.chm](#caprihelpchm)
    - [CAPRI.map](#caprimap)
    - [CAPRISession.r2w](#caprisessionr2w)
    - [sshconfig](#sshconfig)
  - [CAPRI Configuration for Windows 7 and Non-standard Reflection Installations](#capri-configuration-for-windows-7-and-non-standard-reflection-installations)
    - [Windows 7 Installation](#windows-7-installation)
    - [Non-standard Reflection installations](#non-standard-reflection-installations)
  - [Windows 7 Font size on certain screens](#windows-7-font-size-on-certain-screens)
    - [Steps to correct Font size on certain screens in Windows 7](#steps-to-correct-font-size-on-certain-screens-in-windows-7)
    - [Installation of Microsoft Office Imaging 2007 (MODI) on Windows 7 workstations to view .TIFF filesSteps to correct Font size on certain screens in Windows 7](#installation-of-microsoft-office-imaging-2007-modi-on-windows-7-workstations-to-view-tiff-filessteps-to-correct-font-size-on-certain-screens-in-windows-7)
  - [Shared Network Drive or CAPRI access via CPRS Installations](#shared-network-drive-or-capri-access-via-cprs-installations)
- [CAPRI Rollback Procedures](#capri-rollback-procedures)
  - [Restore VistA server](#restore-vista-server)
  - [Restore CAPRI GUI client](#restore-capri-gui-client)
The primary purpose of this document is to provide information for installing patch CAPRI.exe and associated files to accommodate the introduction of Attachmate Reflection, the CAPRI.map file and address an issue stemming from Windows 7 using certain system fonts at 125% size instead of their normal size.
Attachmate Reflection is used as an option for providing secure shell sessions. After clicking on the the CAPRI “Vista” button, the user will be prompted with the following popup window dialog:
![](capri-gui-installation-supplemental-guide/002.png)
If the user selects “Yes,” CAPRI will launch a secure shell session utilizing Attachmate Reflection. Other than the installation notes contained within this document, no further configuration is required to use Reflection.
If the user selects “No” the traditional CAPRI Telnet form will be used to establish a session.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes potential action that is necessary to install this software.

## Attachmate Reflection Installation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CAPRI began using Attachmate Reflection to facilitate secure shell terminal sessions starting with CAPRI v168. This functionality is only available to users who connect through the CLAIMS system and initiate terminal sessions with the “Vista” button. In order to use this functionality, Attachmate Reflection must be installed on the user’s workstation.

# CAPRI VistA Server Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the patch description for patch DVBA\*2.7\*192 for complete information. This section provides the necessary steps required for installing CAPRI. The estimated installation time is less than five minutes during off peak hours.

## VistA Patch DVBA\*2.7\*192

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA server software is being distributed as a PackMan patch message through the National Patch Module (NPM). The KIDS build for this patch is DVBA\*2.7\*192.

### FILE BACKUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch adds --new information to the following Global:

- DVB(396.4, “2507 EXAM”

396.4,103 REMARKS SENT TO CONTRACTOR 6;0 WORD-PROCESSING

\#396.4103

> DESCRIPTION: This field captures the comments from the CAPRI GUI remarks sent to the contractor.

> TECHNICAL DESCR: This field saves the remarks (previously not saved) that were sent to the contractor. This enables future review and comparison to verify completion of requested actions.

> Prior to installation create a backup of these globals and store them in case the patch must be backed out.

#### Go to the Edits and Distribution option in Vista

#### Create a build and name it something descriptive like “DVBA27192 3.0” and add the above globals the build and remember include the data and the data dictionary.

#### Transport the build to your sections USER\$:\[TEMP\] directory if available.

### VISTA INSTALLATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The suggested time to install is during non-peak hours. There should be no CAPRI users on the system.

> This patch updates routines DVBACREM,DVBA192P,DVBCIRP2,DVBAB6,DVBAB82,DVBABEBD,DVBABURL,DVBARSBD,DVBCAMIS,DVBCAMRO,DVBCIUTL, and DVBCRPRT

> We suggest you begin a trail in Attachmate to record the installation. This will help you in the investigation in case of an error during installation.

> To Install DVBA\*2.7\*192

1.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu to unload

> the KIDS distribution included with this message.

2.  From the 'Kernel Installation & Distribution System' menu, select the Installation menu.
3.  From this menu, you may now elect to use the following options (when prompted for INSTALL NAME, enter DVBA\*2.7\*192).
    1.  Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT backup any changes such as DDs or templates
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.)
    3.  Verify Checksums in Transport Global - This option will allow

> you to ensure the integrity of the routines that are in the transport

> global.

4.  Print Transport Global - this option will allow you to view the components of the KIDS build.

> 4\. Use the Install Package(s) option and select package DVBA\*2.7\*192.

> 5\. If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

> Install? NO//', respond NO.

> 6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

> NO//', it is recommended you answer NO.

> 7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

> and Protocols? NO//', respond NO.

> 8\. If CAPRI GUI users have not already been upgraded to the new

> version of the CAPRI GUI v192 (CAPRI.exe \[DVBA_27_P192_02.ZIP\]),

> they should be upgraded as soon as possible upon installation of

> this patch.

> The following RPCs are added with this patch:

- None

> The following Option was updated with the above RPCs with this patch:

- None

> <span class="mark"></span>

> The following is an example installation trail of this patch:

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: DVBA\*2.7\*192 4/21/15@12:16:17

=\> DVBA\*2.7\*192

This Distribution was loaded on Apr 21, 2015@12:16:17 with header of

DVBA\*2.7\*192

It consisted of the following Install(s):

DVBA\*2.7\*192

Checking Install for Package DVBA\*2.7\*192

Install Questions for DVBA\*2.7\*192

Incoming Files:

396.4 2507 REQUEST (Partial Definition)

> **NOTE:** You already have the '2507 EXAM' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

DVBA\*2.7\*192

────────────────────────────────────────────────────────────────────────────────

Updating Routine file...

Updating KIDS files...

DVBA\*2.7\*192 Installed.

Apr 21, 2015@12:16:17

Not a production UCI

NO Install Message sent

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

## CAPRI GUI v192 Client Software & User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CAPRI GUI v192 client software is being distributed as executable CAPRI.exe (\[DVBA_27_P192_02.ZIP\]). The installed executable for this patch is client version 192.02 with a size of 16.5 MB.

The CAPRI GUI v192 client software and documentation for this patch may be retrieved directly using FTP. The preferred method is to FTP the files from:

> REDACTED

This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

| OI&T FIELD OFFICE | FTP ADDRESS | DIRECTORY              |
|-------------------|-------------|------------------------|
| Albany            | REDACTED    | \[anonymous.software\] |
| Hines             | REDACTED    | \[anonymous.software\] |
| Salt Lake City    | REDACTED    | \[anonymous.software\] |

The following files will be available:

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 54%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>FILE NAME</th>
<th>CONTENTS</th>
<th>RETRIEVAL FORMAT</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DVBA_27_P192_02.ZIP</td>
<td><p>File(s) shown below:</p>
<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>CAPRI.exe</th>
<th>CAPRI v192 executable</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VACAPRIVVA.dll</td>
<td><p>Virtual VA dynamically</p>
<p>linked library</p></td>
</tr>
<tr class="even">
<td>CAPRI_Help.chm</td>
<td>CAPRI On-line Help</td>
</tr>
<tr class="odd">
<td>CAPRI.map</td>
<td>CAPRI error map</td>
</tr>
<tr class="even">
<td>CAPRISession.r2w</td>
<td>Reflections session configuration</td>
</tr>
<tr class="odd">
<td>Ssh_config</td>
<td>Secure Shell Configuration</td>
</tr>
<tr class="even">
<td>Libeay32.dll</td>
<td><p>Required for exam data</p>
<p>transfer to DAS</p></td>
</tr>
<tr class="odd">
<td>Ssleay32.dll</td>
<td><p>Required for exam data</p>
<p>transfer to DAS</p></td>
</tr>
<tr class="even">
<td><p>QPDF.exe</p>
<p>QPDF13.dll</p></td>
<td><p>Required to support PDF Compression</p>
<p>Required to support PDF Compression</p></td>
</tr>
<tr class="odd">
<td>Libgcc_s_dw2-1.dll</td>
<td>Required to support PDF Compression</td>
</tr>
<tr class="even">
<td>Libstdc++6.dll</td>
<td>Required to support PDF Compression</td>
</tr>
<tr class="odd">
<td>CAPRI_GUI_ISG.doc</td>
<td>CAPRI GUI Installation Supplemental Guide</td>
</tr>
</tbody>
</table></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>DVBA_27_P192_RN.PDF</td>
<td>Patch Release Notes</td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>DVBA_27_P192_UM.PDF</td>
<td>Updated CAPRI User Manual</td>
<td>BINARY</td>
</tr>
</tbody>
</table>

The VistA Documentation Library (VDL) web site will also contain the 'Release Notes' and updated 'CAPRI User Manual'. This web site is usually updated within 1-3 days of the patch release date.

The VDL web address for CAPRI user documentation is:

> http://www.va.gov/vdl/application.asp?appid=133

# CAPRI GUI Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Additional Installation Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the executable file, there are other files included with the CAPRI installation zip. The general purpose of these files and where they need to be located are as follows:

### VACAPRIVVA.dll

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VACAPRIVVA.dll file is a dynamic link library that provides the web services client interface for the Virtual VA web service, which was added in patch DVBA\*2.7\*181. Important: CAPRI will not function without this file.

- VACAPRIVVA.dll is required for CAPRI to function.
- VACAPRIVVA.dll must be located in the same directory as the CAPRI executable (CAPRI.exe).

The following dialog box displays when CAPRI cannot find the VACAPRIVVA.dll file.

![](capri-gui-installation-supplemental-guide/003.png)

### LIBEAY32.DLL & SSLEAY32.DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Libeay32.dll and Ssleay32.dll are dynamic link libraries that provide the web services client interface for the VLER/DAS web service, which was added in patch DVBA\*2.7\*187. Important: CAPRI requires these files to transfer exam data to VLER/DAS.

- Libeay32.dll and Ssleay32.dll are required for exam data transfer to VLER/DAS.
- Libeay32.dll and Ssleay32.dll must be located in the same directory as the CAPRI executable (CAPRI.exe).

### QPDF.EXE, QPDF13.DLL, LIBGCC_S_DW2-1.DLL & LIBSTDC++-6.DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

QPDF.exe, QPDF13.DLL, LIBGCC_S_DW2-1.DLL & LIBSTDC++-6.DLL are files that support PDF Compression and Linearization. PDF Compression reduces the file size of the PDF Exam Results included in transmissions between CAPRI and VLER/DAS. Smaller file sizes reduce transmission times.

- QPDF.exe, QPDF13.dll, Libgcc_s_dw2-1.dll and Libstdc++-6.dll are required for PDF compression when sending exam data to VLER/DAS.
- QPDF.exe, QPDF13.dll, Libgcc_s_dw2-1.dll and Libstdc++-6.dll must be located in the same directory as the CAPRI executable (CAPRI.exe).

### CAPRI_Help.chm

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CAPRI_Help.chm file contains the on-line help functionality.

- CAPRI_Help.chm is not required for CAPRI to function, but its presence is recommended
- CAPRI_Help.chm should be located in the same directory as the CAPRI executable (CAPRI.exe)
- If CAPRI is setup to run from a disk drive that is not local to the workstation, then CAPRI should be given write permissions to the “TEMP” folder of the workstation. If the TEMP folder is not writable for any reason, then the on-line help functionality may not work properly.

### CAPRI.map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CAPRI.map file contains a list of error addresses and source code line numbers that CAPRI utilizes to provide more detailed information to the development team when an error occurs in CAPRI.

- CAPRI.map is not required for CAPRI to function, but its presence is recommended
- CAPRI.map should be located in the same directory as the CAPRI executable (CAPRI.exe)

### CAPRISession.r2w

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- CAPRISession.r2w is an Attachmate Reflection configuration file. It configures Reflection to terminate when a terminal session disconnects
- CAPRISession.r2w is not required for CAPRI to function, but its presence is recommended
- CAPRISession.r2w should be located in the same directory as the CAPRI executable (CAPRI.exe)

### ssh_config

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ssh_config file provides the parameters used by Attachmate Reflection Secure Shell to configure PC-to-host security options. CAPRI does not require this file for most functions, but it is required when establishing Reflection Secure Shell terminal sessions using the “Vista” button.

- The directory location of the ssh_config file depends on the operating system version
- Windows XP: C:\Documents and Settings\All Users\Application Data\Attachmate\Reflection
- Windows 7: C:\ProgramData\Attachmate\Reflection

*NOTE: The target folder for ssh_config is typically hidden on most systems.*

To show hidden files and folders on Windows XP, perform the following steps:

1.  Right click on the start button and select “Explore” to launch explorer
2.  From the menu at the top of explorer, select Tools\|Folder options
3.  In the resulting dialog, select the “View” tab
4.  Select “Show hidden files and folders” and click OK

![](capri-gui-installation-supplemental-guide/004.png)

To show hidden files and folders on Windows 7, perform the following steps:

1.  Click the Start button
2.  Click Control Panel
3.  Click Appearance and Personalization
4.  Click Folder Options
5.  In the Folder Options dialog, select the “View” tab
6.  Select “Show hidden files and folders” and then click OK

![](capri-gui-installation-supplemental-guide/005.png)

## CAPRI Configuration for Windows 7 and Non-standard Reflection Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to launching Reflection, CAPRI searches the directory path that contains the CAPRI executable (CAPRI.exe) for an optional plain text configuration file named "CapriTerminalEmulators.ini". The purpose of the configuration file is to specify an alternate path that contains the Reflection executable (R2win.exe). If CAPRI does not detect the configuration file, then CAPRI assumes that the Reflection executable exists in the default Windows XP Reflection installation path: "C:\Program Files\Attachmate\Reflection".

### Windows 7 Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Sites that run a mixture of Windows XP and Windows 7 workstations and access the CAPRI executable from a central location, such as a share drive or terminal server, must create a new directory on the share to contain the CAPRI executable and the configuration file. Windows 7 users should access the CAPRI executable from the new directory, while Windows XP users should continue to access the CAPRI executable from the original directory.

The example "CapriTerminalEmulators.ini" configuration file provided with patch DVBA\*2.7\*180 is configured to provide support for the default installation path of Attachmate Reflection on a Windows 7 workstation. Place the configuration file in the same directory that contains the CAPRI executable.

Alternatively, use the following procedure to create the configuration file:

1.  Create the configuration file named "CapriTerminalEmulators.ini" using a plain text editor, such as Notepad
2.  Populate the configuration file with the following two lines:

> <span class="mark">\[Config\]</span>

> <span class="mark">Application=C:\Program Files (x86)\Attachmate\Reflection\R2win.exe</span>

![](capri-gui-installation-supplemental-guide/006.png)

3.  Save the file and place it in the same directory that contains the CAPRI executable.

### Non-standard Reflection installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Reflection is installed in an alternate location, CAPRI can be configured to accommodate this. In order to do this, one should create a file named "CapriTerminalEmulators.ini" in the directory that contains the "CAPRI.exe" file. In this file, one should specify the location of the "Reflection R2Win.exe". For example, in order to specify a Reflection installation located in "C:\My Files\Attachmate\Reflection, CapriTerminalEmulators.ini" should contain the following two lines:

<span class="mark">\[Config\]</span>

<span class="mark">Application=C:\My Files\Attachmate\Reflection\R2win.exe</span>

![](capri-gui-installation-supplemental-guide/007.png)

## Windows 7 Font size on certain screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Windows 7 install process, under certain hardware and software conditions, the Windows installer may setup the default system fonts larger than the standard fonts used in prior versions of Windows. This can cause screens to display distorted in many applications. This problem affects some CAPRI screens, such as the Enterprise Search dialog.

This display distortion is being reported in many COTS applications, e.g. Microsoft Dynamics and is not specific to CAPRI.

If your workstation is affected, then can follow steps below to correct the issue if you have administrative rights to the workstation.

If you do not have administrative rights to your workstations, you may have to contact your System Administrator for assistance and do not proceed.

### Steps to correct Font size on certain screens in Windows 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Before doing the steps below, make sure that you have a good backup of the Windows Registry.

:

1.  Go to the Start menu click Run…
2.  Type “regedit” and then click OK.

![](capri-gui-installation-supplemental-guide/008.png)

3.  In the Registry Editor, click on the path: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts
4.  Click MS Sans Serif 8,10,12,14,18,24. Right-click and select Modify SSERIFF.FON to SSERIFE.FON . *Note: One character of the file name changes from F to E*
5.  Click MS Serif 8,10,12,14,18,24. Right-click and select Modify SERIFF.FON to SERIFE.FON . *Note: One character of the file name changes from F to E*
6.  Click Courier 10,12,15. Right click and select Modify COURF.FON to COURE.FON . *Note: One character of the file name changes from F to E*

> <span class="mark">Note: The above changes take effect after system reboot.</span>

### Installation of Microsoft Office Imaging 2007 (MODI) on Windows 7 workstations to view .TIFF filesSteps to correct Font size on certain screens in Windows 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*IMPORTANT NOTE\*\*\*

With the introduction of “Get Docs from Virtual VA” in patch DVBA\*2.7\*184, there was an issue discovered with opening large TIFF files with the current Windows Photo Viewer, which is the default viewer on Windows 7 workstations for TIFF files. For this reason it is imperative that prior to the installation of CAPRI Patch DVBA\*2.7\*184 from a network share drive, the system administrators (IRM Staff) \*MUST\* validate that workstations running on Windows 7 have Microsoft Office Document Imaging 2007 (MODI) installed prior to installing P184 from a network share drive. This notice does not impact workstations running on Windows XP.

If you are upgrading CAPRI in workstation’s local hard drive, this pre-requisite should already have been met by an Action Item initiated by ESE. Reference national change order CO161098FY13.

However if one or more of your workstations have windows 7 and these don’t have a CAPRI.EXE on local hard disk, i.e. in case of new installs or running CAPRI from a Network Share then on those workstations this pre-requisite has \*not\* been automatically met. You can meet this pre-requisite by following the instructions on this link

[Microsoft Office (2007) Document Imaging Build Document](http://go.va.gov/3wao)

In this document you may use either the SCCM method or the manual method.

All workstations that will run CAPRI.EXE, MUST have this MODI package installed in order to view large .TIFF files.  Even if running CAPRI from the network, this package MUST still be installed on the workstation.

## Shared Network Drive or CAPRI access via CPRS Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site installs CAPRI on a Shared Network Drive and users access a “shortcut” to launch CAPRI or if your users access CAPRI via CPRS the following <u>MUST</u> be performed to allow users to view PDF files from DAS. Users will receive the following error if this is not done.

![](capri-gui-installation-supplemental-guide/009.png)

If the “Start In” folder for CAPRI shortcut at your site is a read-only only folder, it should be changed to a writable folder. This is the folder where documents from VLER DAS are stored temporarily for users to view documents (ex: PDF).

Our recommendation is to use %TEMP% as the default starting directory.  This can be set in the shortcut that is used to launch CAPRI.

- Right-click on the (desktop) CAPRI shortcut, select Properties.
- On the Shortcut tab, in the Start in field, enter %TEMP% .
- Click OK.
- Now, when launching CAPRI, CAPRI will be able to write temporary files such as Word documents or PDFs to the temporary directory, and CAPRI will be able to display those files to the user.

> **NOTE:** This temp directory change only fixes the “access denied” problem when CAPRI is launched directly from a shortcut.

Example:

![](capri-gui-installation-supplemental-guide/010.png)

Example (CAPRI accessed via CPRS)

![](capri-gui-installation-supplemental-guide/011.png)

Benefits:

1.  Each user is guaranteed by Windows to have a unique writable folder.
2.  It is a known environment variable and also guaranteed to exist in any environment.
3.  Due to VA GPO Policy, this folder gets cleared on logon / logoff, hence no disk space impact is caused.

# CAPRI Rollback Procedures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the steps required to uninstall CAPRI v192.02 and re-install CAPRI v192_02.

## Restore VistA server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restore the routines to the VistA server that were saved in step 3 of the VistA Server Installation Procedures. The roll back of a Vista install may be required in the event an install was unsuccessful or a problem has been identified with the software..

1.  After the GUI has been restored to a Pre Patch 192 state.
    1.  Manually remove field \#103 from the “2507 EXAM” file \#396.4 using fileman. Programmer access is required.

> Select OPTION: MODIFY FILE ATTRIBUTES

> Do you want to use the screen-mode version? YES// NO

> MODIFY WHAT FILE: 2507 EXAM//

> Select FIELD: 103 REMARKS SENT TO CONTRACTOR (word-processing)

> LABEL: REMARKS SENT TO CONTRACTOR Replace @

> SURE YOU WANT TO DELETE THE ENTIRE 'REMARKS SENT TO CONTRACTOR' FIELD? Y YES

> 2\. Install the backup global made in step 3 containing the pre patch DVB\*2.7\*192 global, 396.4.

3\. Find your backup Mailman Message by number or name

a\. Select your message

b\. At the prompt select Xtract PackMan

Enter message action (in IN basket): Ignore// Xtract PackMan

Select PackMan function: ?

Answer with PackMan function NUMBER, or NAME

Choose from:

1 ROUTINE LOAD

2 GLOBAL LOAD

3 PACKAGE LOAD

4 SUMMARIZE MESSAGE

5 PRINT MESSAGE

6 INSTALL/CHECK MESSAGE

7 INSTALL SELECTED ROUTINE(S)

8 TEXT PRINT/DISPLAY

9 COMPARE MESSAGE

Select PackMan function: 6 INSTALL/CHECK MESSAGE

> **WARNING:** Installing this message will cause a permanent update of globals

and routines.

Do you really want to do this? NO//yes

4\. By answering yes you have restored the Vista servers to PRE Patch DVBA\*2.7\*192 software

## Restore CAPRI GUI client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restoring the CAPRI GUI client involves replacing the files distributed with patch DVBA\*2.7\*192 with files from patch DVBA\*2.7\*192 contained in DVBA_27_P192_02.ZIP. 

Replace the following files in their install directory:

- CAPRI.exe
- CAPRI.map
- CAPRISession.r2w
- VACAPRIVVA.dll
- CAPRI_Help.chm