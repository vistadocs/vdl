---
title: OR*3*418 Installation Guide CPRS GUI 30A
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: CPRS GUI 30A
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*418
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 1
description: The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order la
audience: 
keywords: 
  - installation
  - table
  - contents
  - cprs
  - sample
  - install
  - patch
  - executable
  - class
  - test
page_count: 0
word_count: 2319
section_count: 11
table_count: 18
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: September 2015
revision_count: 1
revision_newest: 8/25/2015
revision_oldest: 8/25/2015
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_418_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_418_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Computerized Patient Record System Graphical User Interface (CPRS GUI)
---

Installation Guide

OR\*3.0\*418

![](or-3-418-installation-guide-cprs-gui-30a/001.png)

September 2015

Office of Information & Technology (OI&T)

Product Development (PD)

This page left intentionally blank.  

Revision History

| Date      | Version | Description     | Author                             |
|-----------|---------|-----------------|------------------------------------|
| 8/25/2015 | 1.0     | Initial version | <span class="mark">REDACTED</span> |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |
|           |         |                 |                                    |

This page left blank intentionally.

Table of Contents

This page left blank intentionally.

# Computerized Patient Record System Graphical User Interface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Computerized Patient Record System Graphical User Interface](#computerized-patient-record-system-graphical-user-interface)
  - [Overview](#overview)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [National Deployment](#national-deployment)
  - [Document Conventions](#document-conventions)
- [Pre-requisite Patches for OR\3.0\418](#pre-requisite-patches-for-or30418)
- [OR\3.0\418 and CPRS GUI Executable Installation Checklist](#or30418-and-cprs-gui-executable-installation-checklist)
  - [Software Retrieval](#software-retrieval)
  - [Installation Sequence](#installation-sequence)
    - [Patch OR\3.0\418](#patch-or30418)
    - [CPRS GUI Executable (OR30418.zip)](#cprs-gui-executable-or30418zip)
- [Installation Sequence](#installation-sequence-1)
  - [CPRS GUI Executable (OR30418.zip)](#cprs-gui-executable-or30418zip-1)
    - [Changes to the Installation Procedure for the CPRS GUI](#changes-to-the-installation-procedure-for-the-cprs-gui)
    - [Methods of installation](#methods-of-installation)
    - [Manual or Test Installation](#manual-or-test-installation)
  - [CPRS Documentation](#cprs-documentation)
  - [Appendix A: OR\3.0\418 Software Installation Sample](#appendix-a-or30418-software-installation-sample)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

This installation guide deals specifically with the installation of patch OR\*3.0\*418, which is an emergency patch to CPRS GUI v30.A. It will include instructions for the installation of patch OR\*3.0\*418, which only increments the version number of the patch, and then the CPRS Windows executable CPRSChart.exe (1.0.30.69).

The changes to CPRSChart.exe resolves two issues in CPRS GUI 30.A related to International Classification of Diseases, Tenth Revision (ICD-10) diagnosis codes.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) Information Resource Management (IRM) staff.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation guide provides instructions for:

- Installing application components that run on M servers at VAMC facilities
- Installing Windows executable programs on workstations or application servers at VAMC facilities

## National Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the emergent nature of this deployment, there are some deviations from the typical implementation. There will be no phased deployment and no .MSI or .MSP files.

National deployment of this patch will be in two parts: Patch OR\*3.0\*418 will be distributed as a Packman message and a .zip file (containing the CPRS GUI executable and the installation guide) from the anonymous directories. Sites or Region support will install patch OR\*3.0\*418 into accounts using normal procedures.

For the executable, this installation will be different from the last two installations. For the installation of CPRSChart.exe (1.0.30.69), DO NOT USE AN .MSI or .MSP file! This installation will simply copy the new CPRS executable (1.0.30.69) over the previous version (1.0.30.16).

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Examples of VistA “Roll and Scroll” interface actions will be shown in a box such as this:

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

Emphasis of important points may be displayed in this manner:

1.  This is an important point and must not be omitted.

Call-outs may be used to draw attention to part of a block of text or a table without disrupting the flow of the block or table. For example:

Sample text, Sample text, Sample text, Sample text

Sample text, Sample text, Sample text

Sample text, Sample text, Sample text

Sample text, Sample text, Sample text

Sample text, Sample text

Sample text, Sample text, Sample text, Sample text

Sample text

Sample text, Sample text, Sample text, SOMETHING OF NOTE!!

Sample text, Sample text, Sample text, Sample text, Sample text, Sample text

Sample text, Sample text, Sample text, Sample text, Sample text

# Pre-requisite Patches for OR\*3.0\*418

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that the following patch is installed on your system:

- OR\*3.0\*404

# OR\*3.0\*418 and CPRS GUI Executable Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

Table 1 OR\*3.0\*418 and CPRS GUI 30.69—Installation Checklist

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 82%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th>Item</th>
<th>Done</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3">Test/Mirror System Installation</td>
</tr>
<tr class="even">
<td><ol type="1">
<li></li>
</ol></td>
<td>Confirm that patch OR*3.0*404 has been installed in your Test/Mirror system.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td>Download CPRS GUI installation package files, including OR_30_418.zip</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Install the OR*3.0*418 patch using the instructions in Section 3.2.1, Patch OR*3.0*418.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Install the latest version of the CPRS GUI (1.0.30.69). (See Section 4.1, CPRS GUI Executable (OR_30_418.zip), below),install per the instructions in that section, and point user shortcuts to your Test/Mirror system</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Test/Mirror system has been successful</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">Production/Live System Installation</td>
</tr>
<tr class="even">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Confirm that patch OR*3.0*404 has been installed in your Production/Live system.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="7" type="1">
<li></li>
</ol></td>
<td>Install the OR*3.0*418 patch using the instructions in Section 3.2.1, Patch OR*3.0*418.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="8" type="1">
<li></li>
</ol></td>
<td>Install the latest CPRSChart.exe from the OR_30_418.zip according to the instructions in Section 4.1, CPRS GUI Executable (OR_30_418.zip), below) and point user shortcuts to your Production/Live system</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="9" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Production/Live system has been successful</td>
<td></td>
</tr>
</tbody>
</table>

## Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OR\*3.0\*418 patch will be distributed as a PackMan message to the site when the patch is nationally released. Your site needs to install patch OR_30_418 and download and install the GUI executable along with its supporting installation guide (all listed in Table 2 OR\*3.0\*418 files).

Table 2 OR\*3.0\*418 files

| Filename         | File Contents                                                                                      |
|------------------|----------------------------------------------------------------------------------------------------|
| OR_30_418        | This patch will be distributed as a PackMan message                                                |
| OR_30_418.zip    | CPRSChart.exe                                                                                      |
| OR_30_418_IG.doc | Installation Guide for OR\*3.0\*418 (this file will be in the .zip file)                           |
| OR_30_418_IG.pdf | PDF (Portable Document Format) copy of the Installation Guide (this file will be in the .zip file) |

## Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section refers only to the installation of OR\*3.0\*418 and CPRSChart.exe version 1.0.30.69.

### Patch OR\*3.0\*418

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

-------------------------

This patch may be installed with users on the system although it is

recommended that it be installed during non-peak hours to minimize

potential disruption to users. This patch should take less than 5 minutes

to install.

 

 

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option. 
3.  From the Kernel Installation and Distribution System Menu, select

    the Installation Menu.  From this menu, you may elect to use the

    following options. When prompted for the INSTALL NAME enter the patch

    # OR\*3\*418:
    a.  Backup a Transport Global - This option will create a backup

        message of any routines exported with this patch. It will not

        backup any other changes such as DDs or templates.
    b.  Compare Transport Global to Current System - This option will

        allow you to view all changes that will be made when this patch

        is installed.  It compares all components of this patch

        (routines, DDs, templates, etc.).
    c.  Verify Checksums in Transport Global - This option will allow

        you to ensure the integrity of the routines that are in the

        transport global.
4.  From the Installation Menu, select the Install Package(s) option and

    choose the patch to install.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

    Install? NO//'

    Respond: NO    
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install?

    NO//'

    Respond: NO
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options,

    and Protocols? NO//'

    Respond: NO
8.  If prompted 'Delay Install (Minutes):  (0 - 60): 0//'

    Respond 0.

See an example of the host file installation capture, Appendix A: OR\*3.0\*418 Software Installation Sample, below.

### CPRS GUI Executable (OR_30_418.zip)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 4.1, CPRS GUI Executable (OR_30_418.zip) and the following sections for instructions on installing the CPRS GUI executable (1.0.30.69).

# Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide gives instructions for installing the latest version of CPRS GUI 30.A, which includes the following:

- OR\*3.0\*418
- CPRSChart.exe
- The documentation files (which is this installation guide in either a Microsoft Word or Adobe Acrobat format)

## CPRS GUI Executable (OR_30_418.zip)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide basic CPRS GUI installation instructions for the CPRSChart.exe.

Use FTP to retrieve OR_30_418.ZIP from one of the following OI Field Offices' ANONYMOUS.SOFTWARE directories:

<u>OI Field Office</u> <u>FTP Address</u> <u>Directory</u>

Albany [REDACTED](ftp://ftp.fo-albany.med.va.gov) [REDACTED](ftp://ftp.fo-albany.med.va.gov)

Hines [REDACTED](ftp://ftp.fo-albany.med.va.gov) [REDACTED](ftp://ftp.fo-albany.med.va.gov)

Salt Lake City [REDACTED](ftp://ftp.fo-albany.med.va.gov) [REDACTED](ftp://ftp.fo-albany.med.va.gov)

The software distribution includes these files:

<u>File Name Contents Retrieval Format</u>

OR_30_418.ZIP CPRSCHART.EXE Binary

OR_30_418_IG.doc

OR_30_418_IG.pdf

OR_30_418_SRC.ZIP Source files Binary

### Changes to the Installation Procedure for the CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">Note: There is no Microsoft Installation file (.msi) nor Microsoft Patch file (.msp) for this version.</span>

Local sites or region support staff will install the OR\*3.0\*418 patch and then update the CPRSChart.exe as needed. Distribution of the CPRS GUI executable file (CPRSChart.exe) will be done by means of an SCCM push or other method that local sites have used in the past.

<span class="mark">WARNING: You should remove or rename the .MSP file in the Gold path. If you do not, the CPRSLoader will access it and change the registry entry on the workstation to report that 30.16 is still installed.</span>

### Methods of installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">WARNING: DO NOT use the gold path installation method on a production machine, or it will override their production install. On a test machine that also has a production install, you must MANUALLY install it.</span>

> **NOTE:** \*\*\*Rename or Remove the .MSP file on the Gold path\*\*\*NOTE: Users should be out of the CPRS GUI during distribution of the new CPRSChart.exe to ensure the executable is updated.

Sites are generally using the following four methods to distribute the application:

- Network (shared) installation:  
  The executable is placed on a network drive, with a shortcut for each Vista account to be accessed by the user on the users’ desktops. The executable is replaced when no users are accessing the GUI program.
- Citrix installation:  
  The executable is run on a remote workstation and the user views the screen remotely.
- SCCM Push:

> The Enterprise Systems Engineering (ESE) team has developed a national package for the SCCM push of 30.69. Details are located at:

> [REDACTED](ftp://ftp.fo-albany.med.va.gov)

-   
  Manual installation:

  Used primarily for advanced users and at testing locations. This method is somewhat changed from that used previously. For more detail please refer to section 4.1.3, Manual or Test Installation, below.

### Manual or Test Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Things that should be done beforehand:

1.  Determine the DNS server name or IP address for the appropriate VistA server.
2.  Determine the Broker RPC port for the VistA account.
3.  Acquire the CPRSChart.exe file and related dlls (the minimum is borlndmm.dll).

#### To install manually on a workstation, follow these steps:

1.  Copy CPRSChart.exe into the appropriate location on the workstation. For a production instance running on a 64-bit machine, C:\Program Files (x86)\vista\CPRS is recommended; and any other location is used for a test instance.
2.  Create a shortcut to CPRSChart.exe, putting s=\[vista server\] p=\[vista port\] on the command line.

## CPRS Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents are provided, as part of the CPRS v30.A installation package. Please place these files in a location that can be accessed by the appropriate CPRS users or support personnel.

Table 4 CPRS v30.A documentation

| OR_30_418_IG.doc | CPRS GUI v30.A Installation Guide (this document ) |
|------------------|----------------------------------------------------|
| OR_30_418_IG.pdf | CPRS GUI v30.A Installation Guide (this document ) |

## Appendix A: OR\*3.0\*418 Software Installation Sample

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: OR\*3.0\*418 8/25/15@09:12:52

=\> OR\*3.0\*418 Test v2 ;Created on August 25, 2015@14:27

This Distribution was loaded on Aug 25, 2015@09:12:52 with header of

OR\*3.0\*418 Test v2 ;Created on August 25, 2015@14:27

It consisted of the following Install(s):

OR\*3.0\*418

Checking Install for Package OR\*3.0\*418

Install Questions for OR\*3.0\*418

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// NO

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TEMINAL

-------------------------------------------------------------------------------

Install Started for OR\*3.0\*418 :

Aug 25, 2015@09:45:33

Build Distribution Date: Aug 25, 2015

Installing Routines:

Aug 25, 2015@09:45:33

Installing PACKAGE COMPONENTS:

Installing REMOTE PROCEDURE

Installing OPTION

Aug 25, 2015@09:45:35

Updating Routine file...

Updating KIDS files...

OR\*3.0\*418 Installed.

Aug 25, 2015@09:45:35

Install Message \#2519

Install Completed