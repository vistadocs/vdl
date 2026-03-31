---
title: Capacity Management Tools Version 3 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: KMPD
app_name: Capacity Management Tools
section: INF
app_status: active
pkg_ns: KMPD
patch_ver: 3
patch_id: KMPD*3
group_key: "KMPD:KMPD:3"
file_numbers: []
security_keys: []
menu_options: 6
description: The purpose of this guide is to provide instructions for installing the Veterans Health Information Systems and Technology Architecture (VistA) Capacity Planning (CP) Service's Capacity Management Tools software, Version 3.0.
audience: 
keywords: 
  - tools
  - software
  - table
  - installation
  - contents
  - capacity
  - vista
  - management
  - server
  - required
page_count: 0
word_count: 6635
section_count: 19
table_count: 64
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Capacity_Mgmt_Tools/kmpd3_0ig_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Capacity_Mgmt_Tools/kmpd3_0ig_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=129"
---

![](capacity-management-tools-version-3-installation-guide/001.png)

Capacity Management Tools

Release Notes &  
Installation Guide

September 2012

Department of Veterans Affairs (VA)

Testing Services (TS)

Capacity Planning (CP) Service

<span id="_Toc44314817" class="anchor"></span>Revision History

Documentation Revisions

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

Table i: Documentation revision history

<table>
<caption><p><span id="_Toc335891672" class="anchor"></span>Table 1: CM Tools-related software distribution files</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 42%" />
<col style="width: 32%" />
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
<td>08/08/2012</td>
<td>1.0</td>
<td><p>Initial Capacity Management (CM) Tools software and documentation release.</p>
<p>Software: <strong>CM Tools 3.0</strong></p></td>
<td><p>Capacity Planning Development Team</p>
<ul>
<li><p>Development Manager— REDACTED</p></li>
<li><p>Developer—REDACTED</p></li>
<li><p>Software Quality Assurance (SQA)—REDACTED</p></li>
<li><p>Technical Writer—REDACTED</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc335891672" class="anchor"></span>Table 1: CM Tools-related software distribution files

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Contents

<span id="_Toc335891626" class="anchor"></span>Figures and Tables

Figures

[Figure 1: Sample CM Tools 3.0 distribution load [11](#_Toc335891666)](#_Toc335891666)

[Figure 2: Sample CM Tools 3.0 installation (test) [13](#_Toc335891667)](#_Toc335891667)

[Figure 3: Post installation informational message—Existing KMPD BACKGROUND DRIVER  
installed [15](#_Toc335891668)](#_Toc335891668)

Tables

## <span id="_Toc18284794" class="anchor"></span>Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of Capacity Management (CM) Tools software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Information Resource Management (IRM) is the primary stakeholder who is responsible for the management of VistA M software.
- VistA M application developers who develop VistA software and patches.
- Product Support (PS).

Legal Requirements

There are no special legal requirements involved in the use of Capacity Management (CM) Tools.

Disclaimers

This manual provides an overall explanation of how to install and configure the Capacity Management (CM) Tools interface and the changes contained in Capacity Management Tools Version 3.0; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Websites on the Internet and VA Intranet for a general orientation to Health*<u>e</u>*Vet. For example, visit the Office of Information & Technology (OIT) VistA Development VA Intranet Website: http://vaww.vista.med.va.gov

|                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/002.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

<span id="_Toc335891674" class="anchor"></span>Table 3. Client workstation minimum software/network tools/utilities required for CM Tools 3.0

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols/terms are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols/terms:

Table ii: Documentation symbol/term descriptions

|                                                                                                                                     |                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                                              | Description                                                                                                         |
| ![](capacity-management-tools-version-3-installation-guide/003.png)                      | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](capacity-management-tools-version-3-installation-guide/004.png)                                                                                   | CAUTION or DISCLAIMER: Used to caution the reader to take special notice of critical information.               |
| ![](capacity-management-tools-version-3-installation-guide/005.png) | Used to denote special installation instructions only (e.g. platform-specific steps).                               |

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
- Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- "Snapshots" of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft® Windows images (i.e., dialogues or forms).
- User's responses to online prompts will be bold typeface and highlighted using <span class="mark">yellow blocking</span> (e.g., <span class="mark">\<Enter\></span>).
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard.
- Emphasis within a dialogue box will be bold typeface and highlighted in <span class="mark">blue blocking</span> (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words will be bold typeface with alternate color font.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/006.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- Besides established styles and conventions, the following additional text formatting will be used to further highlight or emphasize specific document content:
- Bold Typeface:
- All values entered or selected by the user in computer dialogues (e.g., "Enter 'xyz' in the Server Name field" or "Choose the ABCD folder entry from the list").
- All computer keys when referenced with a command (e.g., "press Enter" or "click OK"). Other special keys are represented within angle brackets (\< \>). For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- All references to computer dialogue tab or menu names (e.g., "go to the General tab" or "choose Properties from the Action menu").
- All user text (e.g., commands) typed or entered in a Command-Line prompt (e.g., "Enter the following command: <span class="mark">CD xyz</span>").
- Italicized Typeface:
- Emphasis (e.g., do *not* proceed or you *must* do the following steps).
- All reference to computer dialogue or screen titles (e.g., "in the *Add Entries* dialogue…").
- All document or publication titles and references (e.g., "see the *ABC Installation Guide*").
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

Documentation Navigation

Document Navigation—This document uses Microsoft<sup>®</sup> Word's built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word 2007 (not the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the dropdown arrow in the "Choose commands from:" box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Click/Highlight the Back command and press Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Click/Highlight the Forward command and press Add to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

|                                                                                                                |                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/007.png) | NOTE: This is a one-time setup and will automatically be available in any other Word document once you install it on the Toolbar. |

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](capacity-management-tools-version-3-installation-guide/008.png)</td>
<td><p><strong>NOTE:</strong> Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic.</p>
<p><strong>REF:</strong> See the <em>Capacity Management Tools Technical Manual</em> for further information.</p></td>
</tr>
</tbody>
</table>

Help at Prompts

VistA M-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/009.png) | REF: For details about obtaining data dictionaries and about the formats available, see the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft® Windows
- M programming language

Reference Materials

Readers who wish to learn more about the Capacity Management Tools software should consult the following:

- *Capacity Management Tools Installation Guide* (this manual)
- *Capacity Management Tools User Manual*
- *Capacity Management Tools Technical Manual*
- Capacity Management (CM) Tools Online Help file (i.e., CM_Tools_3_0.chm)
- The Capacity Planning (CP) Service's Intranet Website: http://vaww.vista.med.va.gov/capman/default.asp

This site contains additional information and documentation.

VistA documentation is made available online in Microsoft Word format and Adobe® Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe® Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe® Systems Incorporated at the following Website: <http://www.adobe.com/>

VistA documentation can be downloaded from the VHA Software Document Library (VDL) Website: <http://www4.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Product Support (PS) anonymous directories:

- Preferred Method download.vista.med.va.gov

|                                                                                                                |                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/010.png) | NOTE: This method transmits the files from the first available File Transfer Protocol (FTP) server. |

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED

# Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [<span id="Toc18284794" class="anchor"></span>Orientation](#span-idtoc18284794-classanchorspanorientation)
- [Release Notes](#release-notes)
  - [GUI Front-end](#gui-front-end)
  - [GUI Options Added](#gui-options-added)
  - [Files Added](#files-added)
- [Preliminary Consideration](#preliminary-consideration)
  - [Purpose](#purpose)
  - [About the Installation Procedures](#about-the-installation-procedures)
  - [Distribution Files](#distribution-files)
  - [VistA M Server Requirements](#vista-m-server-requirements)
  - [Client Workstation Requirements](#client-workstation-requirements)
  - [Skills Needed for Installation](#skills-needed-for-installation)
- [VistA M Server Installation Instructions](#vista-m-server-installation-instructions)
  - [Version 3.0 Installation](#version-30-installation)
    - [Retrieve the CM Tools VistA M Server Distribution File (required)](#retrieve-the-cm-tools-vista-m-server-distribution-file-required)
    - [Verify KIDS Install Platform (required)](#verify-kids-install-platform-required)
    - [Load KMPD30.KID File (required)](#load-kmpd30kid-file-required)
    - [Install Capacity Management Tools 3.0 Software (required)](#install-capacity-management-tools-30-software-required)
    - [Post Installation Routine (required)](#post-installation-routine-required)
    - [Install All Released Patches (required)](#install-all-released-patches-required)
    - [Review Capacity Management Tools Settings (recommended)](#review-capacity-management-tools-settings-recommended)
  - [Version 3.0 Virgin Installation](#version-30-virgin-installation)
    - [Review Translation Table Settings (required)](#review-translation-table-settings-required)
    - [Follow Steps 3.1.1- 3.1.7 Under "Version 3.0 Installation" (required)](#follow-steps-311-317-under-version-30-installation-required)
- [(Optional) Client Workstation Installation Instructions](#optional-client-workstation-installation-instructions)
  - [Retrieve the CM Tools GUI Software Distribution File (required)](#retrieve-the-cm-tools-gui-software-distribution-file-required)
  - [Uninstall Previous Version of CM Tools GUI Software (required)](#uninstall-previous-version-of-cm-tools-gui-software-required)
  - [Shut Down Microsoft Windows Applications (required)](#shut-down-microsoft-windows-applications-required)
  - [Run the Installation Program (required)](#run-the-installation-program-required)
  - [Set Up Server IP and Port Connections (required)](#set-up-server-ip-and-port-connections-required)
    - [Review, Add, or Edit Servers in the Workstation Registry](#review-add-or-edit-servers-in-the-workstation-registry)
    - [Create Shortcut to CM Tools Executable with Predefined Server Information](#create-shortcut-to-cm-tools-executable-with-predefined-server-information)
  - [Add CM Tools RPC Broker "B"-type Option to the User's Secondary Menu (required)](#add-cm-tools-rpc-broker-b-type-option-to-the-users-secondary-menu-required)
The Capacity Management (CM) Tools software is a fully automated support tool developed by Capacity Planning (CP) Service. CM Tools are designed for Information Resource Management (IRM) and system administrators responsible for the capacity planning functions at their site, as well as Veterans Health Information Systems and Technology Architecture (VistA) software developers.
The CM Tools are used to measure system performance, data growth, Computerized Patient Record System (CPRS) coversheet load times, option and protocol execution, and provide various data reports. There are also tools for developers: Global Lister, Error Lister, Routine Search, and an M Code Evaluator.
The Veterans Health Information Systems and Technology Architecture (VistA) Capacity Management (CM) Tools Version 3.0 software is now available. The enhanced software has the following features.

## GUI Front-end

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Delphi-based Graphical User Interface (GUI) front-end has been added to provide access to the various functions available with the following Capacity Planning (CP) Services software:

- Capacity Management (CM) Tools 3.0
- Resource Usage Monitor (RUM) 2.0
- Statistical Analysis of global Growth (SAGG) 2.0

The GUI front-end specifically provides access to the following functionality via tab selection:

- Timing Monitor
- Environment Check
- CM Tools Parameters
- Code Evaluator
- Code Stats
- Error Lister
- Global Lister
- Routine Search
- Reports:
- TMG—Timing Reports

|                                                                                                                   |                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/011.png) | DISCLAIMER: The CM Tools 3.0 GUI software, including the CM_Tools_3_0.chm help file, has only been tested on Microsoft® Windows XP. It is not currently supported on Windows 7. |

## GUI Options Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following GUI options were added to the CM Tools 3.0 software:

- Code Evaluator
- Code Stats
- Error Lister
- Global Lister
- Routine Search

|                                                                                                                |                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/012.png) | REF: These are GUI client-only options added with CM Tools 3.0; there are no equivalent CM Tools VistA M server options. For a list of CM Tools VistA M server options, see Chapter 3, "CM Tools Options," in the *Capacity Management Tools User Manual*. |

## Files Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP REPORTS file (#8973.3) file was added in the CM Tools 3.0 software:

|                                                                                                                |                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/013.png) | REF: For more information on these files, see Chapter 3, "Files," in the *Capacity Management Tools Technical Manual*. |

# Preliminary Consideration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for installing the Veterans Health Information Systems and Technology Architecture (VistA) Capacity Planning (CP) Service's Capacity Management Tools software, Version 3.0.

## About the Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Separate installation procedures are provided in this guide based on the installation type:

- VistA M Server Installation Instructions
- Version 3.0 Installation—Previous version of software installed.
- Version 3.0 *Virgin* Installation—Software never installed.
- (Optional) Client Workstation Installation Instructions—GUI front-end software installation.

|                                                                                                                   |                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/014.png) | DISCLAIMER: The CM Tools 3.0 GUI software, including the CM_Tools_3_0.chm help file, has only been tested on Microsoft® Windows XP. It is not currently supported on Windows 7. |

We recommend sites take the following approach to installing the CM Tools software:

1.  Obtain the CM Tools 3.0 documentation.

|                                                                                                                |                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/015.png) | REF: For more information on the CM Tools documentation, see the "<u>Reference Materials</u>" topic in the "<u>Orientation</u>" section in this manual. |

2.  Install the CM Tools 3.0 server software in a Test account prior to installing it in a Production account.
3.  Obtain and install all released patches for the CM Tools 3.0 software.

|                                                                                                                |                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/016.png) | REF: For the current patch history related to this software, see the Patch Module on FORUM. |

There are no special legal requirements involved in the use of the CM Tools' interface.

## Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CM Tools 3.0 software distribution includes the following files:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 9%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KMPD3_0README.TXT</td>
<td>ASCII</td>
<td><p><strong>Readme File.</strong> This file provides any pre-installation instructions, last minute changes, new instructions, and additional information to supplement the manuals.</p>
<p>Read all sections of this file prior to following the installation instructions in the Capacity Management (CM) Tools Installation Guide (i.e., KMPD3_0IG.PDF).</p></td>
</tr>
<tr class="even">
<td>KMPD3_0IG.PDF</td>
<td>Binary</td>
<td><strong>Installation Guide.</strong> Use this manual in conjunction with the Readme text file (i.e., KMPD3_0README.TXT) to install the CM Tools 3.0 software.</td>
</tr>
<tr class="odd">
<td>KMPD3_0UM.PDF</td>
<td>Binary</td>
<td><strong>User Manual</strong>. Use this manual</td>
</tr>
<tr class="even">
<td>KMPD3_0TM.PDF</td>
<td>Binary</td>
<td><strong>Technical Manual</strong>. Use this manual</td>
</tr>
<tr class="odd">
<td>KMPD3_0.KID</td>
<td>ASCII</td>
<td><p><strong>KIDS Distribution—VistA M Server Software.</strong> Required for all VistA M Server installations. Contains the Capacity Management (CM) Tools 3.0 VistA M Server software:</p>
<ul>
<li><p>Global (^KMPD) and VA FileMan files</p></li>
<li><p>Server Routines</p></li>
<li><p>Capacity Management Tools Options</p></li>
</ul>
<p>Follow normal procedures to obtain and install all CM Tools VistA M Server software (see FORUM).</p></td>
</tr>
<tr class="even">
<td>CM_Tools_3_0.zip</td>
<td>Binary</td>
<td><p><strong>Client Workstation Software Distribution.</strong> Required for all installations of the CM Tools GUI software. This is a zip distribution file that contains the following installation files:</p>
<ul>
<li><p>CMToolsSetup.exe—Self-installing executable to install the CM Tools software.</p></li>
<li><p>0x0409.ini—Software initialization and configuration file.</p></li>
<li><p>CM Tools 3.0.msi—Microsoft® Windows installer that is the engine for the installation, maintenance, and removal of software on Microsoft® Windows systems.</p></li>
<li><p>Data1.cab—Zip distribution containing the CM Tools 3.0 report framework.</p></li>
<li><p>Setup.ini</p></li>
</ul>
<p>After running the CMToolsSetup.exe, the following files and folders will be installed on the client workstation:</p>
<ul>
<li><p>kmpdTools.exe—CM Tools 3.0 software executable.</p></li>
<li><p>CM_Tools_3_0.CHM—CM Tools 3.0 client GUI HTML Help file.</p></li>
<li><p>ServerList.exe &amp; ServerList.hlp—RPC Broker Edit Broker Servers application and associated help file.</p></li>
</ul>
<p>![](capacity-management-tools-version-3-installation-guide/017.png) <strong>NOTE:</strong> These files are owned and maintained by the RPC Broker development team. CM Tools has included these files in its distribution as a convenience when updating servers in the Microsoft® Windows registry.</p>
<ul>
<li><p>Reports— CM Tools 3.0 report framework.</p></li>
</ul>
<p>![](capacity-management-tools-version-3-installation-guide/018.png) <strong>NOTE:</strong> CM Tools uses the FastReports® software to display reports in a separate browser window, which allows users to save or print the report</p>
<p>![](capacity-management-tools-version-3-installation-guide/019.png) CAUTION: Users should <em>not</em> modify, add, or delete files in this folder.</p>
<p>![](capacity-management-tools-version-3-installation-guide/020.png) DISCLAIMER: The CM Tools 3.0 GUI software, including the CM_Tools_3_0.chm help file, has only been tested on Microsoft® Windows XP. It is not currently supported on Windows 7.</p></td>
</tr>
</tbody>
</table>

## VistA M Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools and network configuration are required on the VistA M Server in order to install and use the Capacity Management Tools software:

<span id="_Toc335891673" class="anchor"></span>Table 2. VistA M Server minimum software/network tools/utilities required for CM Tools 3.0

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Minimum Software/Hardware Configuration</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Operating System Software</td>
<td><p>InterSystems Caché operating system.</p>
<p>![](capacity-management-tools-version-3-installation-guide/021.png) <strong>NOTE:</strong> The VistA M Server need not be an NT system.</p></td>
</tr>
<tr class="even">
<td>Fully Patched M Accounts</td>
<td><p>You should have both a development Test account and a Production account for the CM Tools software.</p>
<p>The accounts <em>must</em> contain the <em>fully</em> patched versions of the following software (listed alphabetically):</p>
<ul>
<li><p>Resource Usage Monitor (RUM)—KMPR*2.0*1</p></li>
<li><p>Statistical analysis of Global Growth (SAGG)—KMPS*1.8*3</p></li>
<li><p>Computerized Patient Record System (CPRS) GUI 23.0 (or higher) and Order Entry/Results Reporting (OE/RR) 3.0 (or higher)</p></li>
</ul>
<p>![](capacity-management-tools-version-3-installation-guide/022.png) CAUTION: The CM Tools software loads without CPRS GUI 23 and OE/RR 3.0; however, in order to start collecting timing data and enable the data collection and report-related CM Tools software options, Patch OR*3.0*209 <em>must</em> also be installed.</p>
<ul>
<li><p>Health Level Seven (HL7) 1.6</p></li>
</ul>
<p>![](capacity-management-tools-version-3-installation-guide/023.png) CAUTION: The CM Tools software loads without HL7 Patch #79 (i.e., HL*1.6*79); however, in order to start collecting HL7 statistics, HL7 Patch #79 <em>must</em> also be installed.<br />
<br />
HL*1.6*79 installs the $$CM^HLUCM API. The $$CM^HLUCM API contains code that enables the collection of HL7 usage information from the VistA environment.</p>
<ul>
<li><p>Kernel 8.0</p></li>
<li><p>Kernel Toolkit 7.3</p></li>
<li><p>MailMan 8.0</p></li>
<li><p>RPC Broker 1.1</p></li>
<li><p>VA FileMan 22.0</p></li>
</ul>
<p>![](capacity-management-tools-version-3-installation-guide/024.png) <strong>NOTE:</strong> These software applications <em>must</em> be properly installed and <em>fully</em> patched prior to installing CM Tools 3.0. You can obtain all released GUI and VistA M server software via the Product Support (PS) Anonymous Directories.<br />
<br />
VistA M server patches (including patch description and installation instructions) are available from the Patch module on FORUM or through normal procedures. Patches <em>must</em> be installed in published sequence.</p></td>
</tr>
<tr class="odd">
<td>Network Communications Software</td>
<td>The VistA M Server needs to have TCP/IP running.</td>
</tr>
</tbody>
</table>

## Client Workstation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools and network configuration are required on the Client Workstation in order to install and use the Capacity Management Tools software:

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>Minimum Software/Hardware Configuration</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Hardware</td>
<td>80x86-based client workstation.</td>
</tr>
<tr class="even">
<td>Operating System</td>
<td>Microsoft® Windows XP.</td>
</tr>
<tr class="odd">
<td>Network Communications Software</td>
<td>The CM Tools software requires networked client workstations running Microsoft's native TCP/IP stack.</td>
</tr>
<tr class="even">
<td>VistA software</td>
<td><p>RPC Broker 1.0 (or higher) Client Agent (i.e., CLAGENT.exe)</p>
<p>![](capacity-management-tools-version-3-installation-guide/025.png) <strong>NOTE:</strong> The CLAGENT.exe <em>must</em> be running in the background. This software is distributed with the CPRS GUI software.</p></td>
</tr>
</tbody>
</table>

|                                                                                                                   |                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/026.png) | DISCLAIMER: The CM Tools 3.0 GUI software, including the CM_Tools_3_0.chm help file, has only been tested on Microsoft® Windows XP. It is not currently supported on Windows 7. |

## Skills Needed for Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Skills required to perform the installation are listed below. Instructions for performing these functions are provided in vendor-supplied operating system manuals as well as VistA publications.

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/027.png) | REF: Caché for NT and OpenVMS sites should refer to the Caché Resources Intranet Website: http://vaww.va.gov/custsvc/cssupp/axp/Cache_Resource.asp |

Users need to know how to do the following:

- Back up the system
- Copy files using commands of the host file system
- Run a Kernel Installation & Distribution System (KIDS) installation
- Switch User Class Identification (UCI) accounts
- Enable/Disable routine mapping and journaling
- Manage globals, including global placement, protection, and translation
- Run a system status and restore a job
- Install/Uninstall Windows® XP GUI software applications

# VistA M Server Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of Capacity Management Tools Version 3.0 only affects the CM Tools options. Therefore, this installation can be performed at any time of the day with minimal disruption. Aside from implementing any of the applicable items that are listed below, installation should not take longer than 10-15 minutes.

The instructions in this section are applicable for the Test/Production accounts in the Caché environment. Any unique instructions for a specific environment will be notated within the procedure.

|                                                                                                                |                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/028.png) | NOTE: All Caché for Microsoft® Windows NT or Caché for OpenVMS sites should install this software. |

The Capacity Management Tools 3.0 software installation creates the ^KMPD global to store the CM HL7 DATA (#8973.1) and CP TIMING (#8973.2) files. This global will automatically be trimmed (records deleted) by the CM Tools Background Driver option to contain the maximum amount of data as prescribed by the CP parameters.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/029.png) | REF: For more information on the CM Tools Background Driver option and CP parameters, see Chapter 3, "CM Tools: Options," in the *Capacity Management Tools User Manual*. |

This installation will automatically set up the CM Tools Background Driver \[KMPD BACKGROUND DRIVER\] option within the OPTION SCHEDULING file (#19.2). This option will be scheduled to run tomorrow at 1:30 a.m. with a reschedule frequency of every day (i.e., 1D).

|                                                   |                                                                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/030.png) | CAUTION: All sites should ensure that the CM Tools Background Driver \[KMPD BACKGROUND DRIVER\] option is *not* currently running during the installation. |

## Version 3.0 Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Retrieve the CM Tools VistA M Server Distribution File *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Obtain the Capacity Management (CM) Tools 3.0 VistA M Server software distribution file (i.e., KMPD3_0.KID) from the Product Support (PS) ANONYMOUS.SOFTWARE directory located at:

- Preferred Method download.vista.med.va.gov

This method transmits the files from the first available FTP server.

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED

### Verify KIDS Install Platform *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that the Kernel Installation and Distribution System (KIDS) platform on your system is ready to install VistA M Server patches.

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/031.png) | REF: For more information on KIDS, see the KIDS section in the *Kernel Systems Management Guide* located on the VDL at the following Website: <http://www4.va.gov/vdl/application.asp?appid=10> |

1.  Verify Host File Server (HFS) Device in the DEVICE File (#3.5)—Verify that you have a Host File Server (HFS) device in the DEVICE file (#3.5) named "HFS". If you have performed KIDS installations on the VistA M Server before, you probably already have an appropriate HFS device set up. If you don't have an entry for this device, you *must* create one.

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/032.png) | REF: For information on how to create an HFS device, see Chapter 18, "Host Files," in the *Kernel Systems Management Guide*. |

2.  Verify Null Device in the DEVICE File (#3.5)—Verify that you have a Null device in the DEVICE file (#3.5) named "NULL" (or whose mnemonic is named "NULL").

You can have other devices with similar names, but one device is needed whose name or mnemonic is "NULL." The subtype should be a "P-" subtype (e.g., P-OTHER), the margin should be a minimum of 80, and the page length should be a minimum of 60.

|                                                                                                                |                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/033.png) | REF: For sample device setups, see Chapter 15, "Device Handler: System Management," in the *Kernel Systems Management Guide*. |

### Load KMPD3_0.KID File *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Kernel Installation & Distribution System (KIDS) to load the distribution. From the KIDS menu, select the Installation menu option. Invoke the Load a Distribution option to load the following software:

KMPD3_0.KID

The following is sample dialogue of a load of the CM Tools 3.0 software done at the Oakland OIFO:

|                                                                                                                |                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/034.png) | NOTE: The Capacity Management Tools 3.0 KIDS installation build name is "KMPD 3.0." |

<span id="_Toc335891666" class="anchor"></span>Figure 1: Sample CM Tools 3.0 distribution load

> Select Kernel Installation & Distribution System Option: <span class="mark">INSTALLATION</span>

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: <span class="mark">1 \<Enter\></span> Load a Distribution

> Enter a Host File: <span class="mark">USR\$:\[ANONYMOUS\]KMPD3_0.KID;1</span>

> KIDS Distribution saved on Jun 22, 2009@14:35:22

> Comment: KMPD 3.0

> This Distribution contains Transport Globals for the following Package(s):

> Build KMPD 3.0 has been loaded before, here is when:

> KMPD 3.0 Install Completed

> was loaded on Jun 22, 2009@14:35:22

> OK to continue with Load? NO// <span class="mark">YES</span>

> Distribution OK!

> Want to Continue with Load? YES// <span class="mark">\<Enter\></span>

> Loading Distribution...

> KMPD 3.0

> Use INSTALL NAME: KMPD 3.0 to install this Distribution.

|                                                                                                                |                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/035.png) | NOTE: If you are prompted with "Want to RUN the Environment Check Routine? YES//", you should respond with YES. |

### Install Capacity Management Tools 3.0 Software *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use KIDS to Install the CM Tools 3.0 software. Follow the KIDS installation prompts as you would any other KIDS installation. Specific prompts and suggested responses are notated below:

1.  Users may be on the system during installation of this patch and software. However, this software should be installed during off-hours, when a minimal number of users are on the system.
2.  You do not need to stop TaskMan.
3.  You may elect to use any of the following options within the KIDS Installation menu:
- Verify Checksums in Transport Global—This option allows you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global.
- Compare Transport Global to Current System—This option allows you to view all changes that will be made when the release is installed. It compares all components of the release (routines, DDs, templates, etc.).
- Backup a Transport Global—This option creates a backup message of any routines exported with this release. It will *not* back up any other changes such as DDs or templates.
- Install Package(s).
4.  When prompted for the INSTALL NAME, enter the following:

KMPD 3.0

5.  When prompted to rebuild menu trees:

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

You can respond with NO and not rebuild the menus until the normal scheduled menu rebuild takes place or YES to rebuild the menus immediately after the installation.

6.  When prompted to inhibit logons:

Want KIDS to INHIBIT LOGONs during the install? YES//

You can respond with NO.

7.  When prompted to disable options and protocols:

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

You can respond with NO.

8.  If the Timing Collection background job is not turned on, you will get the following prompt:

I will start the Timing Collection background job when the install is complete? Yes// YES

You should respond with YES.

#### CM Tools 3.0 Software Installation Sample

The following is sample dialogue of an installation of the CM Tools 3.0 software done at the Oakland OIFO:

|                                                                                                                |                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/036.png) | NOTE: The Capacity Management Tools 3.0 KIDS installation build name is "KMPD 3.0." |

<span id="_Toc335891667" class="anchor"></span>Figure 2: Sample CM Tools 3.0 installation (test)

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: <span class="mark">INSTALL PACKAGE(S)</span>

> Select INSTALL NAME: <span class="mark">KMPD 3.0 \<Enter\></span> Loaded from Distribution Loaded from Distribution 6/22/09@14:35:22

> =\> KMPD 3 TEST v12

> <span class="mark">This Distribution was loaded on Jun 22, 2009@14:35:22 with header of</span>

> <span class="mark">KMPD 3 TEST v12</span>

> <span class="mark">It consisted of the following Install(s):</span>

> <span class="mark">KMPD 3.0</span>

> Checking Install for Package KMPD 3.0

> Install Questions for KMPD 3.0

> Incoming Files:

> 8972.1 CP CODE EVALUATOR

> Note: You already have the 'CP CODE EVALUATOR' File.

> 8972.3 CP DATA ELEMENTS

> Note: You already have the 'CP DATA ELEMENTS' File.

> 8973 CP PARAMETERS

> Note: You already have the 'CP PARAMETERS' File.

> 8973.1 CM HL7 DATA

> Note: You already have the 'CM HL7 DATA' File.

> 8973.2 CP TIMING

> Note: You already have the 'CP TIMING' File.

> 8973.3 CP REPORTS (including data)

> Note: You already have the 'CP REPORTS' File.

> I will OVERWRITE your data with mine.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// <span class="mark">\<Enter\></span>

> Want KIDS to INHIBIT LOGONs during the install? NO// <span class="mark">\<Enter\></span>

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// <span class="mark">\<Enter\></span>

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// <span class="mark">\<Enter\></span> Telnet terminal

> Install Started for KMPD 3.0 :

> Jun 22, 2009@14:36:07

> Build Distribution Date: Jun 12, 2009

> Installing Routines:

> Jun 22, 2009@14:36:08

> Installing Data Dictionaries: ...

> Jun 22, 2009@14:36:08

> Installing Data:

> Jun 22, 2009@14:36:09

> Installing PACKAGE COMPONENTS:

> Installing BULLETIN

> Installing FORM

> Installing REMOTE PROCEDURE

> Installing LIST TEMPLATE

> Installing OPTION

> RPC KMPD REPORT LIST in Option KMPD CM DEVELOPER TOOLS \*\*NOT FOUND\*\*

> KMPD 3.0

> --------------------------------------------------------------------------------

> Installing PARAMETER DEFINITION

> Jun 22, 2009@14:36:09

> Running Post-Install Routine: EN^KMPDPOST

> CM TOOLS CURRENT VERSION field in CP PARAMETERS file has been updated!

> \[KMPD BACKGROUND DRIVER\] is scheduled in the OPTION SCHEDULING file!

> \[KMPD BACKGROUND DRIVER\] has been scheduled to run each day at 1:30am!

> Updating Routine file...

> Updating KIDS files...

> KMPD 3.0 Installed.

> Jun 22, 2009@14:36:10

> Not a production UCI

> NO Install Message sent

> --------------------------------------------------------------------------------

> +------------------------------------------------------------+

> 100% ¦ 25 50 75 ¦

> Complete +------------------------------------------------------------+

> <span class="mark">Install Completed</span>

### Post Installation Routine *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of the informational message that you may receive while the post-installation routine is running:

<span id="_Toc335891668" class="anchor"></span>Figure 3: Post installation informational message—Existing KMPD BACKGROUND DRIVER installed

Running Post-Install Routine: ^KMPDPOST

CM TOOLS CURRENT VERSION field in CP PARAMETERS file has been updated!

\[KMPD BACKGROUND DRIVER\] is scheduled in the OPTION SCHEDULING file!

Complete!

<span id="_Toc335891669" class="anchor"></span>Figure 4: Post installation informational message—No KMPD BACKGROUND DRIVER installed

Running Post-Install Routine: ^KMPDPOST

CM TOOLS CURRENT VERSION field in CP PARAMETERS file has been updated!

\[KMPD BACKGROUND DRIVER\] has been scheduled to run each day at 1:30am!

Complete!

An informational message indicates that the post-installation routine is updating the schedule frequency of the KMPD BACKGROUND DRIVER background task to run nightly at 1:30 a.m.

### Install All Released Patches *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the time of publication of this manual, several VistA M Server-side patches have been released with the CM Tools 3.0 software.

1.  Obtain all released CM Tool patches. Follow the normal procedures to obtain released patches from the Patch Module on FORUM.
2.  All VistA M Server patches are distributed in Kernel 8.0 KIDS format. Using KIDS, load and install the CM Tools-related VistA M Server patches.
3.  Follow the instructions under the "Installation Instructions" section in the patch description in order to install each patch.

### Review Capacity Management Tools Settings *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\] under the Capacity Planning menu \[XTCM MAIN\] located on the Operations Management menu \[XUSITEMGR\] on Kernel's Systems Manager Menu \[Eve\] to review CM HL7 data collection.

Invoke the CP Environment Check option \[KMPD STATUS\] and select either the HL7 or Timing report options to ensure that the CM Tools Background Driver \[KMPD BACKGROUND DRIVER\] is scheduled to run daily at 1:30 a.m. Review the other items in the status display for information regarding the CM HL7 DATA (#8973.1) and CP TIMING (#8973.2) files. Specifically:

- QUEUED TO RUN AT = 01:30 a.m. (or the appropriate time for your site)
- CM TOOLS BACKGROUND DRIVER = KMPD BACKGROUND DRIVER
- RESCHEDULING FREQUENCY = 1D
- TASK ID = TaskMan ID number is present
- QUEUED BY = An active user
- CM Tools routines displays no problems

|                                                                                                                |                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/037.png) | REF: For more information on the CP Environment Check option \[KMPD STATUS\] and the CM Tools Background Driver \[KMPD BACKGROUND DRIVER\], see "CM Tools Options" chapter in the *Capacity Management Tools User Manual*. |

If the CM Tools Background Driver \[KMPD BACKGROUND DRIVER\] is not shown as being scheduled to run in the future, use the Schedule/Unschedule Options option \[XUTM SCHEDULE\] located under the Taskman Management menu \[XUTM MGR\] to schedule the KMPD BACKGROUND DRIVER option \[KMPR BACKGROUND DRIVER\] to run daily at 1:30 a.m.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](capacity-management-tools-version-3-installation-guide/038.png)</td>
<td><p>CAUTION: Capacity Planning Service <em>strongly</em> recommends that the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] be scheduled to run daily at 1:30 a.m., because this background driver is the main mechanism by which the following sub-globals are purged nightly:</p>
<ul>
<li><p>^KMPD(8973.1)—CM HL7 DATA file (#8973.1): Records are purged as prescribed by the Purge HL7 Data After CP parameter, which is stored in the HL7 WEEKS TO KEEP DATA field (#3.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option [KMPD PARAM EDIT].</p></li>
<li><p>^KMPD(8973.2)—CP TIMING file (#8973.2): Records are purged as prescribed by the Purge Timing Data After CP parameter, which is stored in the TIMING WEEKS TO KEEP DATA field (#4.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option [KMPD PARAM EDIT].</p></li>
</ul>
<p>Modification of the frequency and time may have adverse effects on the size of the temporary ^KMPD(8973.1) and ^KMPD(8973.2) sub-globals and on the number of entries within the CM HL7 DATA file (#8973.1) and CP TIMING (#8973.2) files.</p></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/039.png) | REF: For more information on the CP parameters, see the "Edit CP Parameters File" topic in Chapter 3, "CM Tools: Options," in the *Capacity Management Tools User Manual*. |

|                                                                                                                 |                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/040.png) | CONGRATULATIONS: You have now completed the installation of the CM Tools software on the VistA M Server. |

## Version 3.0 *Virgin* Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Review Translation Table Settings *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Planning (CP) Service has been given the KMP\* namespace for both routines and globals. Therefore, you should review your translation table settings to determine the proper placement for the KMP\* global namespace.

Capacity Planning Service advises that sites should locate this global on a volume set that has a lesser overall level of activity. There are a couple of approaches by which the degree of activity can be ascertained by monitoring:

- Global Growth—Review the output of the Statistical Analysis of Global Growth (SAGG) Top Globals Display option \[KMP1 ISC SITE TOP GBL TREND\]. This option displays the top 10 globals in terms of growth over a selected time period. There is a very high correlation between the activity rate of a global and the corresponding rate of growth. This approach will yield many of the usual highly accessed globals. These highly accessed globals include: ^OR, ^TIU, ^XMB, ^ECX, ^LRO, ^PSB, ^PSRX, ^HL, ^LR, ^PRCA, and DIA.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](capacity-management-tools-version-3-installation-guide/041.png)</td>
<td><p><strong>REF:</strong> The KMP1 ISC SITE TOP GBL TREND option can be found in the following menu tree on FORUM:</p>
<blockquote>
<p>|-SAGG Menu at Albany CIOFO ... [KMP99 SAGG FORUM ACCESS]</p>
<p>|</p>
<p>|-Trending Statistics Menu ... [A1B9 ISC TRENDING MENU]</p>
<p>|</p>
<p>|- Site Trending Menu ... [A1B9 ISC SITE TRENDING MENU]</p>
<p>|</p>
<p>|- Top Globals Display [KMP1 ISC SITE TOP GBL TREND]</p>
</blockquote></td>
</tr>
</tbody>
</table>

- Global Accesses—Review the number of global accesses for *all* globals across *all* volume sets. When considering global placements, in addition to global growth potential, sites should also avoid co-locating highly accessed globals on the same volume set (e.g., ^DIC and ^DD).

### Follow Steps 3.1.1- 3.1.7 Under "Version 3.0 Installation" *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                 |                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/042.png) | CONGRATULATIONS: You have now completed the installation of the CM Tools software on the VistA M Server. |

# (Optional) Client Workstation Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Retrieve the CM Tools GUI Software Distribution File *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Obtain the Capacity Management (CM) Tools 3.0 GUI software distribution file (i.e., CM_Tools_3_0.zip) from the Product Support (PS) ANONYMOUS.SOFTWARE directory located at:

- Preferred Method download.vista.med.va.gov

This method transmits the files from the first available File Transfer Protocol (FTP) server.

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED

Download the zip distribution file and extract the contents to your client workstation in a temporary directory/folder of your choice; this will be referred to as the \<STAGING_DIRECTORY\> in this document.

|                                                                                                                   |                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/043.png) | DISCLAIMER: The CM Tools 3.0 GUI software, including the CM_Tools_3_0.chm help file, has only been tested on Microsoft® Windows XP. It is not currently supported on Windows 7. |

## Uninstall Previous Version of CM Tools GUI Software *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                   |                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/044.png) | CAUTION: For sites that have previously installed the CM Tools GUI software (e.g., test sites), *before* installing a later version of the CM Tools GUI software, you *must* first uninstall/remove any existing/previous version of the CM Tools GUI software. |

For example, to uninstall the CM Tools GUI software from a Microsoft® Windows XP system, do the following:

1.  Go to the Start menu.
2.  Select the AllPrograms (or Programs) menu option.
3.  Select the VistA option.
4.  Select the CM Tools 3.0 option.
5.  Select the Uninstall CM Tools 3.0 option.
6.  Answer Yes when prompted to confirm the uninstall.

Or:

1.  Go to the Start menu.
2.  Select the Settings option.
3.  Select Control Panel option.
4.  Select the Add or Remove Programs option.
5.  Look through the list and highlight "CM Tools 3.x".
6.  Press Remove to uninstall the CM Tools 3.x software.

## Shut Down Microsoft Windows Applications *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We recommend shutting down all other Microsoft® Windows-based applications running on the client workstation upon which you are installing the CM Tools GUI software. In particular, you must *not* be running the CM Tools GUI software.

## Run the Installation Program *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run the CMToolsSetup.exe located in the \<STAGING_FOLDER\> on the client workstation (see Section <u>4.1</u>). This will start the interactive client workstation installation wizard. For example, on a Microsoft® Windows XP system:

1.  Go to the Start menu.
2.  Select the Run option.
3.  Press Browse to locate the CM Tools 3.0 CMToolsSetup.exe file.
4.  Press OK to run the CM Tools 3.0 CMToolsSetup.exe

Follow the online instructions provided when you run the installation program. We *strongly* recommend that you accept the default installation directory.

## Set Up Server IP and Port Connections *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to running the CM Tools client application, you need to populate the server IP and port connection information for any severs to which the workstation can connect. To do this, use either of the following methods:

- <u>Review, Add, or Edit Servers in the Workstation Registry</u>
- <u>Create Shortcut to CM Tools Executable with Predefined Server Information</u>

### Review, Add, or Edit Servers in the Workstation Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the RPC Broker Edit Broker Servers application (i.e., ServerList.exe) to review, add, or edit server IPs and listener ports in your client workstation registry. By updating your registry, you can run the CM Tools application directly by double clicking on the kmpdTools.exe file and choosing the desired server connection from the registry list, as shown below:

<span id="_Toc335891670" class="anchor"></span>Figure 5. "Connect To" dialogue— Sample server connection register entries

![](capacity-management-tools-version-3-installation-guide/045.png)

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/046.png) | REF: For more detailed information on the RPC Broker "Connect To" dialogue, see the *RPC Broker Systems Management Guide*. |

#### Locate and Run the RPC Broker ServerList.exe File

The RPC Broker 1.1 Edit Broker Servers application (i.e., ServerList.exe and ServerList.hlp) is distributed with the CM Tools 3.0 software or available for download on the "RPC Broker Archive Downloads: BDK Software and Documentation" Intranet Website: http://vaww.vista.med.va.gov/broker/archive/internal/v_1_1/ServerList.exe

#### Edit the Broker Servers

After running the Edit Broker Servers application (i.e., ServerList.exe), review the current list of servers, as shown below:

<span id="_Toc335891671" class="anchor"></span>Figure 6. Edit Broker Servers application—Sample entries

![](capacity-management-tools-version-3-installation-guide/047.png)

To add server entries to which the workstation can connect, do the following:

> 1\. Add a server entry in one of the following ways:

- Select a server or servers from the Servers in Hosts file list, and then press Add Hosts Server.
- Press Add Servers (this lets you add a server entry that is not in the HOSTS file).

> 2\. For each new server entry created, fill in the appropriate server DNS or IP address and port to connect to for that server entry.

> 3\. When your entries are complete, press OK. This closes the Edit Broker Servers application (i.e., ServerList.exe) and adds the specified servers.

|                                                                                                                |                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/048.png) | REF: For more detailed information on the RPC Broker Edit Broker Servers application (i.e., ServerList.exe), see the *RPC Broker Systems Management Guide*. |

### Create Shortcut to CM Tools Executable with Predefined Server Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a shortcut to the CM Tools executable file (i.e., kmpdTools.exe) on your client workstation desktop. This allows you to run the CM Tools application indirectly by double clicking on the shortcut to the kmpdTools.exe file with a pre-defined server connection identifier. You should create shortcuts for each server IP and port combination.

#### Locate kmpdTools.exe File

If you accepted the default directory during the installation (see Section <u>4.3</u>) the kmpdTools.exe file will be located in the following directory:

C:\Program Files\vista\CM_Tools\3_0

Otherwise, navigate to the directory where you installed the kmpdTools.exe file.

#### Create kmpdTools.exe Desktop Shortcut

Create a shortcut to the CM Tools executable file (i.e., kmpdTools.exe) on the client workstation desktop. For example, on a Microsoft® Windows XP system:

1.  In the directory folder (see Section <u>4.5.2.1</u>), highlight and right click (secondary menu) on the kmpdTools.exe file.
2.  Select the Send To option.
3.  Select Desktop (create shortcut) option.

#### Edit Shortcut Properties

Edit the shortcut properties to point to the appropriate VistA M Server.

1.  On the desktop, highlight and right click (secondary menu) on the kmpdTools.exe shortcut icon: ![](capacity-management-tools-version-3-installation-guide/049.png)
2.  Select the Properties option; if not already there, go to the Shortcut tab.
3.  In the Target field, after the full directory path (in quotes) ending with kmpdTools.exe, do the following:
1.  Enter one space.
2.  Enter the IP address or Domain Name Service (DNS; e.g., test.oakland.med.va.gov).
3.  Enter one space.
4.  Enter the port (e.g., 9999).
5.  Press Apply and then OK.

For example, when completed the Target field entry will look like the following:

"C:\Program Files\vista\CM_Tools\3_0\kmpdTools.exe" *test.oakland.med.va.gov9999*

## Add CM Tools RPC Broker "B"-type Option to the User's Secondary Menu *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information Resource Management (IRM) must add the CM Tools KMPD CM DEVELOPER TOOLS RPC Broker "B"-type option to the user's Secondary Menu.

|                                                                                                                 |                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-installation-guide/050.png) | CONGRATULATIONS: You have now completed the installation of the CM Tools GUI software on the client workstation. |

> Upon completing the installation of the CM Tools software on the VistA M Server (required) and client workstations (optional), you are now ready to work with the CM Tools software.