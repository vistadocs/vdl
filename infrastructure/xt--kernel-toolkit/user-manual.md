---
title: VistA Package Size Reporting Tool (VPSRT) User Guide (XT*7.3*143)
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: 
app_code: XT
app_name: Kernel Toolkit
section: INF
app_status: active
pkg_ns: XT
patch_ver: 7.3
patch_id: XT*7.3
group_key: "XT:XT:7.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - package
  - span
  - vista
  - size
  - parameter
  - action
  - class
  - extract
  - xtmpsize
  - xtvs
page_count: 0
word_count: 28660
section_count: 15
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2021
revision_count: 1
revision_newest: 04/19/2021
revision_oldest: 04/19/2021
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Toolkit/xtvs_vpsrt_ug_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Toolkit/xtvs_vpsrt_ug_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=12"
---

---
title: |
  VistA Package Size Reporting Tool (VPSRT)

  Kernel Toolkit Patch XT\*7.3\*143

  User Guide (REDACTED)
---

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/001.png)

April 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

<span id="revision_history" class="anchor"></span>Revision History

| Date       | Revision | Description                                                                                       | Author                                                                        |
|------------|----------|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 04/19/2021 | 1.0      | Initial *VistA Package Size Reporting Tool (VPSRT) Kernel Toolkit Patch XT\*7.3\*143 User Guide*. | VistA Infrastructure (VI) / VistA Kernel Development Team: Patch XU\*8.0\*143 |

Table 1: Documentation Symbol Descriptions

<span id="_Toc69720124" class="anchor"></span>Table of Contents

<span id="_Toc69720125" class="anchor"></span>List of Figures

<span id="_Toc69720126" class="anchor"></span>Orientation

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of the VistA Package Size Reporting Tool (VPSRT) and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA).

Intended Audience

The intended audience of this manual is the following stakeholders:

- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) regional and local sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/002.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of this software for *non*-VistA use should be referred to the VistA site’s local Office of Information and Technology Field Office (OITFO).

Documentation Disclaimer

This manual provides an overall explanation of VPSRT and the functionality contained in VPSRT; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) VistA Development Intranet website.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/003.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/004.png)       | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/005.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666.”
- Patient and user names are formatted as follows:
- *\[Application Name\]*PATIENT,*\[N\]*
- *\[Application Name\]*USER,*\[N\]*

Where “*\[Application Name\]*” is defined in the Approved Application Abbreviations document and “*\[N\]*” represents the first name as a number spelled out and incremented with each new entry.

For example, in Kernel (XU) test patient names would be documented as follows:

XUPATIENT,ONE; XUPATIENT,TWO; XUPATIENT,14, etc.

For example, in Kernel (XU) test user names would be documented as follows:

XUUSER,ONE; XUUSER,TWO; XUUSER,14, etc.

- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code are shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are in boldface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box is in boldface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are in boldface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (circle with arrow pointing left).
6.  Select/Highlight the Back command and press Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (circle with arrow pointing right).
8.  Select/Highlight the Forward command and press Add to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when selecting hyperlinks within the document.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/007.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/008.png) NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/009.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment

References

Readers who wish to learn more about VistA Package Size Reporting Tool (VPSRT) should consult the following:

- *VistA Package Size Reporting Tool (VPSRT) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)*
- *VistA Package Size Reporting Tool (VPSRT) User Guide* (this manual)
- *VistA Package Size Reporting Tool (VPSRT) Technical Manual*

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) website: <http://www.va.gov/vdl/>

The VPSRT documentation is located on the VDL at: [<u>VA Software Document Library - Kernel Toolkit</u>](https://www.va.gov/vdl/application.asp?appid=12)

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [System Overview](#system-overview)
  - [Generating VistA Package Size Statistics](#generating-vista-package-size-statistics)
    - [Extract FORUM Package Data from PACKAGE (9.4) File](#extract-forum-package-data-from-package-94-file)
    - [Update VistA Package Size Package Parameters Data File](#update-vista-package-size-package-parameters-data-file)
    - [Report VistA Package Size Statistics](#report-vista-package-size-statistics)
  - [VistA Package Size Reporting Tool (VPSRT) Options](#vista-package-size-reporting-tool-vpsrt-options)
  - [VistA Package Size Reporting Tool (VPSRT) Protocols](#vista-package-size-reporting-tool-vpsrt-protocols)
    - [ListMan Menu Type Protocols](#listman-menu-type-protocols)
    - [ListMan Action Type Protocols](#listman-action-type-protocols)
  - [Security Key](#security-key)
  - [Lock Function](#lock-function)
  - [Temporary Globals](#temporary-globals)
    - [^TMP Globals Used by Report of All Packages](#tmp-globals-used-by-report-of-all-packages)
    - [^TMP Globals Used by Report of Single Packages](#tmp-globals-used-by-report-of-single-packages)
    - [^TMP Globals Used by Report for both All & Single Packages](#tmp-globals-used-by-report-for-both-all-single-packages)
  - [Data Flow](#data-flow)
  - [Run-Time Components](#run-time-components)
- [Using the VistA Package Size Reporting Tool](#using-the-vista-package-size-reporting-tool)
  - [Package Parameter Generation and Statistics Reporting Flow—Overview](#package-parameter-generation-and-statistics-reporting-flowoverview)
    - [Create New Package Parameter File](#create-new-package-parameter-file)
    - [Update Existing Package Parameter File](#update-existing-package-parameter-file)
  - [Package Parameter Generation and Statistics Reporting Flow—Detail](#package-parameter-generation-and-statistics-reporting-flowdetail)
    - [Extract Package File Data](#extract-package-file-data)
    - [Unload Package Extract Global on VistA](#unload-package-extract-global-on-vista)
    - [Invoke Vista Package Size Analysis Manager](#invoke-vista-package-size-analysis-manager)
    - [Extract Management](#extract-management)
    - [Convert Extract to Parameter List](#convert-extract-to-parameter-list)
    - [Create Parameter File from Package File Extract](#create-parameter-file-from-package-file-extract)
    - [Return to VistA Package Size Analysis Manager & Review/Edit Parameter File](#return-to-vista-package-size-analysis-manager-reviewedit-parameter-file)
    - [Display Package Parameter List](#display-package-parameter-list)
    - [Analyze Package Parameter Data for Correctness](#analyze-package-parameter-data-for-correctness)
    - [Edit Package Parameter Data (As Needed)](#edit-package-parameter-data-as-needed)
    - [Edit Package Parameters Process](#edit-package-parameters-process)
    - [Save Edited Package Parameter List](#save-edited-package-parameter-list)
    - [Create VistA Package Size Report](#create-vista-package-size-report)
    - [Query a Remote VistA](#query-a-remote-vista)
    - [Change Host File Directory](#change-host-file-directory)
    - [Unlock Parameter File](#unlock-parameter-file)
    - [Swapping Headers](#swapping-headers)
- [Appendix A—System MailMan Messages](#appendix-asystem-mailman-messages)
  - [Warning Message—When Create Report of a Single Package Remotely](#warning-messagewhen-create-report-of-a-single-package-remotely)
  - [Warning Message—When Create Report of All Packages Locally](#warning-messagewhen-create-report-of-all-packages-locally)
  - [Clean Up Message—When Request Extract from Remote or Local VistA](#clean-up-messagewhen-request-extract-from-remote-or-local-vista)
The Veterans Health Information Systems and Technology Architecture (VistA) Package Size Reporting Tool (VPSRT) is used to report the number of technical components used to build any legacy VistA package. The package uses the package definition from the VistA PACKAGE (#9.4) file to identify package components. The VistA Package Size Reporting Tool includes a suite of analytical tools to assist a user with validating the package definitions in the VistA Package file. This document outlines the steps needed to deploy and use the VPS Reporting Tool.
![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/010.png) NOTE: This tool is being developed and released under the Kernel Toolkit “XTVS” namespace as a Class I application. It will be installed on FORUM and made available to all project teams. Eventually, this tool may become a Web service.
Kernel Patch XT\*7.3\*143 provides the following functionality:
- Extract VistA PACKAGE (#9.4) file data from one system and move it to another system where it may be written to a local text (parameter) file.
- Edit, share, and delete parameter (text) files.
- Report data inconsistencies in a selected parameter (text) file or differences between it and another parameter (text) file. Share the reports.
- Create a VistA Package size report based on the parameter (text) file that can be written into a delimited file (for input to another computer application) or written into a captioned file (that can be read by a human).
- Control access to extract and Package Parameter files within the application.
- Prevent multiple users accessing the same Package Parameter file at the same time.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XT\*7.3\*143 enhances Kernel Toolkit by adding a legacy VistA package definition and size reporting system. This enhancement does *not* measure package use or capacity requirements. It provides statistics on the “technical footprint” for a VistA Package, where “technical footprint” is the following:

- Number of routines
- Size of routines
- Number of files
- Number of fields
- Number of options
- Number of protocols
- Number of remote procedure calls (RPCs)
- Number of VA FileMan templates included in the reported package

This package is new and does *not* exist in production VistA prior to installation of Patch XT\*7.3\*143. The report depends on accurate package definitions to provide correct statistics for a package.

<span id="_Ref480264132" class="anchor"></span>Figure 1: VPS Reporting Tool—Integration

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/011.png)

<span id="_Ref480957623" class="anchor"></span>Figure 2: VPS Reporting Tool—System Layers

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/012.png)

<span id="_Ref480273639" class="anchor"></span>Figure 3: VPS Reporting Tool—Extract Manager Use Cases

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/013.png)

## Generating VistA Package Size Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three basic processes in generating VistA Package Size statistics:

- <u>Extract FORUM Package Data from PACKAGE (9.4) File</u>
- <u>Update VistA Package Size Package Parameters Data File</u>
- <u>Report VistA Package Size Statistics</u>

### Extract FORUM Package Data from PACKAGE (9.4) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Extract FORUM package data from the PACKAGE (9.4) file for all packages that meet the following criteria.

- Have a status of any of the following:
- ASSIGNED
- PENDING
- TEMPORARY
- Are any of the following classes:
- CLASS 1/EPMO
- CLASS 1/C3-\>C1
- CLASS 1/NON-VA
- CLASS 1/INNOVATIONS

The Class entries are:

- I CLASS 1/EPMO
- II CLASS 2/FIELD
- III CLASS 3/FIELD
- Ia CLASS 1/C3-\>C1
- Ib CLASS 1/NON-VA
- Ic CLASS 1/INNOVATIONS

The data in the following fields are extracted from the FORUM PACKAGE (9.4) file:

- NAME \[.01\]
- PREFIX \[1\]
- \*LOWEST FILE NUMBER \[10.6\]
- \*HIGHEST FILE NUMBER \[11\]
- ADDITIONAL PREFIXES multiple \[#14\]

ADDITIONAL PREFIXES \[.01\]

- EXCLUDED NAME SPACE multiple \[919\]

EXCLUDED NAME SPACE \[.01\]

- FILE NUMBER multiple \[15001\]

FILE NUMBER \[.01\]

- LOW-HIGH RANGE multiple \[15001.1\]
- LOW FILE NUMBER \[.01\]
- HIGH FILE NUMBER \[.02\]
- PARENT PACKAGE \[15003\]

### Update VistA Package Size Package Parameters Data File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Package Size Report Tools include a suite of tools for managing the package parameters used to generate the package size report. These tools include:

- Package Parameter file comparisons
- Package component add, change, and delete
- Package add and delete
- Package Parameter file creation and deletion
- VistA MailMan functions

### Report VistA Package Size Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Report VistA package size statistics using the VistA Package Size Parameters data file and the configuration of the VistA instance where the report is created. The report should be created on a fully patched "gold" instance of VistA. The statistics can be reported in various forms. The statistic report formats include:

- Single VistA Package (human readable)
- All packages sorted by Package Name (human readable)
- All packages sorted on Number of Routines (human readable)
- All packages sorted on Total Routine Size (human readable)
- All packages sorted on Package Name with caret delimited data (computer readable)
- All packages sorted on Package name with caret delimited data, parent package is included (computer readable)

These reports can be emailed or written to a text file.

## VistA Package Size Reporting Tool (VPSRT) Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Package Size Reporting Tool (VPSRT) has three options:

- VistA Package Extract Manager \[XTVS VISTA PACKAGE EXTRACT MGR\]

This option invokes the “VistA Package Size Analysis Manager” screen (aka VistA Package Extract & Rpt Manager).

- Send Package File Extract via Packman \[XTVS PKG MGR EXT PACKAGE MSG\]

This option does the following:

- Extracts the VistA Package Size relevant data from the PACKAGE (#9.4) file.
- Loads it into an ^XTMP global.
- Bundles the ^XTMP global in a PackMan message.
- Allows the user to send it to a VA MailMan email address on a VistA environment.
- Process XTVS Request Message \[XTVS PKG EXTRACT SERVER\]

This server option processes a Kernel Toolkit VistA Package Size request message. The VistA Package Size Reporting Tool (VPSRT) can request the following information from a remote VistA via a request message to this option:

- Size report for a single VistA package on another production VistA.
- Package file extract from any production VistA. Optionally, a size a report for all packages can be requested from FORUM in addition to a Package file extract.

## VistA Package Size Reporting Tool (VPSRT) Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ListMan Menu Type Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the VistA Package Size Reporting Tool (VPSRT) Analysis Manager ListMan menus:

- VistA Package Mgr Menu \[XTVS PACKAGE MANAGER MENU\]: This menu allows access to VistA Package Manager actions. The XTVS PACKAGE MANAGER List Manager template uses this menu protocol. This menu includes the following actions:
- EM—Extract Manager \[XTVS PKG MGR EXT MNGR ACTION\]
- PMD—Display/Edit Package Parameters \[XTVS PKG MGR PARAM DISP/EDIT ACTION\]
- VSR—Display VistA Size Report \[XTVS PKG MGR VISTA SIZE RPT\]
- DPF—Delete Package Parameter File \[XTVS PKG MGR PARAM FILE DELETE ACTION\]
- CHD—Change Host Directory \[XTVS SITE PARAMETERS\]
- UNL—Unlock Parameter File \[XTVS PKG MGR PARAM UNLOCK ACTION\]
- Extract Display/Delete \[XTVS PKG MGR EXT DISP MENU\]: This menu displays a selected extract and related actions for the extract. The XTVS PKG MGR EXT DISP List Manager template uses this menu protocol. This menu includes the following actions:
- DE—Delete Displayed Extract \[XTVS PKG EXT DISP DEL ACTION\]
- VALM BLANK 1
- Extract Manager Menu \[XTVS PKG MGR EXTRACT MENU\]: This menu allows access to the Package File Extract tools. The XTVS PKG MGR EXTRACT MNGR List Manager template uses this menu protocol. This menu includes the following actions:
- CE—Extract Package Data \[XTVS PKG EXTRACT CREATE ACTION\]
- ED—Display Extract \[XTVS PKG MGR EXT DISP ACTION\]
- ME—Email Extract Global \[XTVS PKG EXT EMAIL ACTION\]
- DEL—Delete Extract \[XTVS PKG EXTRACT DEL ACTION\]
- CXP—Convert Extract to Parameter List \[XTVS PKG EXT CRT PARAM ACTION\]
- VALM BLANK 1
- New Parameter File Menu \[XTVS PKG MGR NEW PARAM MENU\]: This menu allows access to the new Package Parameter file management actions. The XTVS PKG EXT CRT PARAM List Manager template uses this menu protocol. This menu includes the following actions:
- RPL—Display Parameter List \[XTVS PKG EXT REDISP PARAM ACTION\]
- DPC—Display Parameter Corrections \[XTVS PKG EXT DISP CORRECTIONS ACTION\]
- WPF—Write Parameter List to File \[XTVS PKG EXT PARAM WRT ACTION\]
- EPC—Email Corrections Rpt & Parameters \[XTVS PKG MGR NEW PARAM MAIL ACTION\]
- Compare Parameters to Existing File \[XTVS PKG MGR PARAM CMPR MENU\]: The menu allows selection of an existing XTMPSIZE.DAT file for comparison to a displayed file. Differences are reported in a ListMan user interface. The XTVS PKG MGR PARAM COMPARE List Manager template uses this menu protocol. This menu includes the following actions:
- ECR—Email Comparison Report \[XTVS PKG MGR PARAM COMPR MAIL ACTION\]
- VALM BLANK 2
- Parameter Caption Display Menu \[XTVS PKG MGR PARAM DISP CAPTN MENU\]: This menu contains the list of actions available from the XTVS PKG MGR PARAM CAPTN DISP list template. This menu includes the following actions:
- EPP—Edit Package Parameters \[XTVS PKG MGR EDIT PACKAGE PARM ACTION\]
- DPE—Delete Package Parameter Entry \[XTVS PKG MGR DEL PACKAGE PARM ACTION\]
- SPP—Save Package Parameter Changes \[XTVS PKG MGR SAVE PACKAGE PARM ACTION\]
- VALM BLANK 1
- Package Parameter Display Menu \[XTVS PKG MGR PARAM DISP MENU\]: This menu contains the list of actions available from the XTVS PKG MGR PARAM DISPLAY list template. This menu includes the following actions:
- DO—Display Package Overlap List \[XTVS PKG MGR PARAM ERR DISP ACTION\]
- DM—Display Parameter File Data Map \[XTVS PKG MGR PARAM DATA MAP HELP ACTION\]
- DC—Display Captioned Parameters \[XTVS PKG MGR PARAM DISP CAPTION ACTION\]
- CPF—Parameter File Comparison \[XTVS PKG MGR PARAM COMPARE ACTION\]
- List Package Errors \[XTVS PKG MGR PARAM ERROR MENU\]: This menu allows access to the Package Parameter file error reporting actions. The XTVS PKG MGR PARAM ERROR DISP List Manager template uses this menu protocol. This menu includes the following actions:
- PL—Display Prefix Overlap List \[XTVS PKG MGR PREFIX OVERLAP ACTION\]
- FL—Display File Overlap List \[XTVS PKG MGR FILE OVERLAP ACTION\]
- EL—Email Displayed Report \[XTVS PKG MGR EMAIL OVRLAP RPT ACTION\]
- RL—\[Re\] Display Package Overlap List \[XTVS PKG MGR PARAM OVRLP REDISP ACTION\]
- VistA Size Report Menu \[XTVS PKG MGR RPT MENU\]: This menu allows access to VistA Package Manager statistics report actions. The XTVS PKG MGR VISTA SIZE RPT List Manager template uses this menu protocol. This menu includes the following actions:
- CTF—Create Text File \[XTVS PKG MGR RPT WRT ACTION\]
- ER—Email Rpt Attachment \[XTVS PKG MGR RPT MAIL ACTION\]

### ListMan Action Type Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the VistA Package Size Reporting Tool (VPSRT) Analysis Manager ListMan actions:

- <span id="cpf_create_parameter_file_from_extract" class="anchor"></span>CXP—Convert Extract to Parameter List \[XTVS PKG EXT CRT PARAM ACTION\]: Prompts the user for the \$JOB Process ID of the extract and displays the Extract Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) on the “VistA Package Size Analysis Manager – Package Parameters” screen (see Section <u>2.2.5</u>).
- <span id="dpc_display_parameter_corrections" class="anchor"></span>DPC—Display Parameter Corrections \[XTVS PKG EXT DISP CORRECTIONS ACTION\]: Allows users to review the changes the [CXP—Convert Extract to Parameter List](#cpf_create_parameter_file_from_extract) \[XTVS PKG EXT CRT PARAM ACTION\] action made to the data written in the Package Parameters list when it was created from the raw PACKAGE (#9.4) file extract (see Section <u>2.2.5.2</u>).

Creation of Package Parameters from the PACKAGE (#9.4) file extract extends file range numbers out to four (4) decimal places (nines). For example, 1.5 becomes 1.5999. It also reports omissions and data integrity problems in the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)).

- <span id="de_delete_displayed_extract" class="anchor"></span>DE—Delete Displayed Extract \[XTVS PKG EXT DISP DEL ACTION\]: Allows the user to delete the ^XTMP(“XTVS”) global extract displayed on the “VistA Package Size Analysis Manager - Display Extract” screen (see Section <u>2.2.4.2.1</u>). This action prompts the user to confirm deletion of the ^XTMP global displayed in the list:
- NO—Displays a message and redisplays the extract global.
- YES—Deletes the global and returns to the “VistA Package Size Analysis Manager - Extract Manager” screen.

To display an extract for deletion, use the [ED—Display Extract](\l) \[XTVS PKG MGR EXT DISP ACTION\] action (see Section <u>2.2.4.2</u>).

- <span id="me_e_mail_extract_global" class="anchor"></span>ME—Email Extract Global \[XTVS PKG EXT EMAIL ACTION\]: Prompts the user for the \$JOB Process ID number of the extract to mail and then prompts the user for recipients (see Section <u>2.2.4.3</u>).

This serves as an alternate to the Send Package File Extract via Packman \[XTVS PKG MGR EXT PACKAGE MSG\] option (see Section <u>2.2.1</u>).

- <span id="wpf_write_parameter_list_to_file" class="anchor"></span>WPF—Write Parameter List to File \[XTVS PKG EXT PARAM WRT ACTION\]: Creates a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) from the Package Parameters displayed with the following file name format (see Section <u>2.2.6</u>):

<span id="package_parameter_file_name_format" class="anchor"></span>XTMPSIZE\_*\<user initials\>\<mm-dd-yy_hhmm\>*.DAT

It is written to the VistA Package Size default directory for further editing with the VistA Package Analysis Manager for further editing with the VistA Package Analysis Manager.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/014.png) REF: For more information on setting the VistA Package Size default directory, see Section <u>2.2.15</u>, “<u>Change Host File Directory</u>.”

- <span id="rpl_display_parameter_list" class="anchor"></span>RPL—Display Parameter List \[XTVS PKG EXT REDISP PARAM ACTION\]: Executed after users review corrections with the [DPC—Display Parameter Corrections](#dpc_display_parameter_corrections) \[XTVS PKG EXT DISP CORRECTIONS ACTION\] action. It redisplays the package parameters as defined by the selected package extract file (see Section <u>2.2.5.1</u>).
- <span id="ce_extract_package_data" class="anchor"></span>CE—Extract Package Data \[XTVS PKG EXTRACT CREATE ACTION\]: Extracts PACKAGE (#9.4) file data into ^XTMP(“XTVS”) global (see Section <u>2.2.4.1</u>).
- <span id="del_delete_extract" class="anchor"></span>DEL—Delete Extract \[XTVS PKG EXTRACT DEL ACTION\]: Prompts the user for the \$JOB Process ID number of the extract and deletes the ^XTMP(“XTSIZE”) global extract (see Section <u>2.2.4.4</u>).
- <span id="dpe_delete_package_parameter_entry" class="anchor"></span>DPE—Delete Package Parameter Entry \[XTVS PKG MGR DEL PACKAGE PARM ACTION\]: Prompts users to enter a package to delete. The user is reminded that deletion removes the package from the size report created with the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) being edited (see Section <u>2.2.11.2</u>).
- <span id="epp_edit_package_parameters" class="anchor"></span>EPP—Edit Package Parameters \[XTVS PKG MGR EDIT PACKAGE PARM ACTION\]: Prompts users to enter a package to add/edit. The user is then prompted to edit the parameters required for Package Size Reporting (see Section <u>2.2.11.1</u>).
- <span id="el_e_mail_displayed_report" class="anchor"></span>EL—Email Displayed Report \[XTVS PKG MGR EMAIL OVRLAP RPT ACTION\]: Prompts the user for email recipients to send the displayed report. This action allows the report to be sent to a specific Package SME for review (see Step 2 in Section <u>2.2.9</u>).

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/015.png) NOTE: This action sends the displayed report. For example, if the “VistA Package Size Analysis Manager – File Overlap” screen is displayed, then the “File Overlap” report is sent to the recipient.

- <span id="ed_display_extract" class="anchor"></span>ED—Display Extract \[XTVS PKG MGR EXT DISP ACTION\]: Allows users to enter the \$J Process number for the ^XTMP(“XTVS”) global and display its data (see Section <u>2.2.4.2</u>). The “VistA Package Size Analysis Manager – Display Extract” screen is displayed and presents a report of each Package with captioned parameter data. Use this report to review the extracted PACKAGE (#9.4) file data to determine what parameter changes and corrections need to be made.

To delete a displayed extract, use the [DE—Delete Displayed Extract](#de_delete_displayed_extract) \[XTVS PKG EXT DISP DEL ACTION\] action.

- <span id="em_extract_manager" class="anchor"></span>EM—Extract Manager \[XTVS PKG MGR EXT MNGR ACTION\]: Invokes a utility for managing the ^XTMP(“XTSIZE”) global (see Section <u>2.2.4</u>).

This action is locked with the XTVS EDITOR security key.

- <span id="fl_display_file_overlap_list" class="anchor"></span>FL—Display File Overlap List \[XTVS PKG MGR FILE OVERLAP ACTION\]: Sorts out and displays only the packages that have file overlaps (intersections) (see Section <u>2.2.9.2</u>). The “VistA Package Size Analysis Manager – File Overlap” screen is then displayed.
- <span id="epc_email_corrections_rpt_and_parameters" class="anchor"></span>EPC—Email Corrections Rpt & Parameters \[XTVS PKG MGR NEW PARAM MAIL ACTION\]: Prompts the user for recipients and sends the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) as an attachment and the corrections report in the mail message (see Section <u>2.2.5.3</u>). Use this information as a starting point for correcting package information in the Parameters file.
- <span id="cpf_parameter_file_comparison" class="anchor"></span>CPF—Parameter File Comparison \[XTVS PKG MGR PARAM COMPARE ACTION\]: Prompts the user to select a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) for comparison (see Step 4 in Section <u>2.2.9</u>). Displays a report of differences between the new Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) and the selected Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)).
- ECR—Email Comparison Report \[XTVS PKG MGR PARAM COMPR MAIL ACTION\]: Allows users to email a comparison report on the “VistA Package Size Analysis Manager - Parameter Compare” screen using VistA MailMan (see Section <u>2.2.9.4</u>).
- <span id="dm_display_parameter_file_data_map" class="anchor"></span>DM—Display Parameter File Data Map \[XTVS PKG MGR PARAM DATA MAP HELP ACTION\]: Displays a data map of the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) list data (see Section <u>2.2.8.1</u>).
- <span id="dc_display_captioned_parameters" class="anchor"></span>DC—Display Captioned Parameters \[XTVS PKG MGR PARAM DISP CAPTION ACTION\]: Displays the list of packages with captioned data elements. It also supports Package Parameter editing actions (see Section <u>2.2.10</u>).
- <span id="pmd_display_edit_package_parameters" class="anchor"></span>PMD—Display/Edit Package Parameters \[XTVS PKG MGR PARAM DISP/EDIT ACTION\]: This action prompts the user to select a [XTMPSIZE\*.DAT](#package_parameter_file_name_format) Package Parameter file form a list of Package Parameter files (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)). It then invokes the “VistA Package Size Analysis Manager – Parameter Display” screen for editing and managing Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) data (see Section <u>2.2.8</u>).

This action is locked with the XTVS EDITOR security key.

- <span id="de_display_package_overlap_list" class="anchor"></span>DO—Display Package Overlap List \[XTVS PKG MGR PARAM ERR DISP ACTION\]: Displays the “VistA Package Size Analysis Manager – Prefix/File Overlap” screen. It includes data analysis support actions that allow users to review PACKAGE (#9.4) file and PREFIX (#1) field (i.e., unique namespace prefix assigned to the package) overlap information (see Section <u>2.2.9</u>).
- <span id="dpf_delete_package_parameter_file" class="anchor"></span>DPF—Delete Package Parameter File \[XTVS PKG MGR PARAM FILE DELETE ACTION\]: Deletes from the system a selected Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) listed on the “VistA Package Size Analysis Manager” screen (see Section <u>2.2.3.1</u>).

This action is locked with the XTVS EDITOR security key.

- <span id="rl_re_display_package_overlap_list" class="anchor"></span>RL—\[Re\] Display Package Overlap List \[XTVS PKG MGR PARAM OVRLP REDISP ACTION\]: Displays both prefix (namespace) and file overlaps for packages that intersect (see Section <u>2.2.9.3</u>). The “VistA Package Size Analysis Manager – Prefix/File Overlap” screen is re-displayed.
- <span id="pl_display_prefix_overlap_list" class="anchor"></span>PL—Display Prefix Overlap List \[XTVS PKG MGR PREFIX OVERLAP ACTION\]: Sorts out and displays only the packages that have prefix (namespace) overlap (intersections) (see Section <u>2.2.9.1</u>). The “VistA Package Size Analysis Manager – Prefix Overlap” screen is displayed.
- <span id="er_email_rpt_attachment" class="anchor"></span>ER—Email Rpt Attachment \[XTVS PKG MGR RPT MAIL ACTION\]: Prompts the user for email addresses to receive the report (see Section <u>2.2.13</u>).
- <span id="ctf_create_text_file" class="anchor"></span>CTF—Create Text File \[XTVS PKG MGR RPT WRT ACTION\]: Prompts users to enter the following (see Section <u>2.2.13</u>):
- Directory to write the report file. The default is the VistA Package Size default directory.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/016.png) REF: For more information on setting the VistA Package Size default directory, see Section <u>2.2.15</u>, “<u>Change Host File Directory</u>.”

- Name of the host file that will contain the report. The default name is:

VistAPkgSize\_*\<VA FileMan internal date/time\>*.txt

- <span id="spp_save_package_parameter_changes" class="anchor"></span>SPP—Save Package Parameter Changes \[XTVS PKG MGR SAVE PACKAGE PARM ACTION\]: Allows users to overwrite the displayed Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) or create a new Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) (see Section <u>2.2.12</u>).

After the XTMPSIZE\*.DAT file has been edited, this action prompts the user to indicate if they want to create a new Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)). If the user selects to create a new Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)), the file is written to the XTMPSIZE\*.DAT default directory with the following file name format:

XTMPSIZE\_*\<user initials\>\<mm-dd-yy_hhmm\>*.DAT

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/017.png) REF: For more information on setting the VistA Package Size default directory, see Section <u>2.2.15</u>, “<u>Change Host File Directory</u>.”

If the user does *not* choose to create a new Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)), the currently displayed Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) is overwritten.

- <span id="vsr_display_vista_size_report" class="anchor"></span>VSR—Display VistA Size Report \[XTVS PKG MGR VISTA SIZE RPT\]: Reports VistA package size statistics (see Sections <u>2.2.13</u> and <u>2.2.13.2</u>).
- <span id="chd_change_host_directory" class="anchor"></span>CHD—Change Host Directory \[XTVS SITE PARAMETERS\]: Allows users to change the default host file directory (see Section <u>2.2.15</u>) retaining the following files:
- [XTMPSIZE\*.DAT](#package_parameter_file_name_format)
- XTMPSIZE\*.BAK
- VistA Size Statistic Report

This action is locked with the XTVS EDITOR security key.

- <span id="unl_unlock_parameter_file" class="anchor"></span>UNL—Unlock Parameter File \[XTVS PKG MGR PARAM UNLOCK ACTION\]: Displays a list of lock files (.LCK) for Package Parameter files and prompts the user for the number of the Extract Package Parameter file (i.e., XTMPSIZE\*.LCK) to delete (see Section <u>2.2.16</u>). Deletion of a lock file unlocks the Package Parameter file. The lock files have the following file name format:

XTMPSIZE\_*\<user initials\>\<mm-dd-yy_hhmm\>*.LCK

This action is locked with the XTVS EDITOR security key.

- <span id="req_remote_vista_extract_query" class="anchor"></span>REQ—Remote VistA Extract Query \[XTVS PKG EXT QUERY REMOTE ACTION\]: Allows a user to request a Package file extract from any Production VistA (see Section <u>2.2.1.2</u>). If a Package file extract is requested from FORUM, the user can also request a VistA Package size report for all packages on FORUM.
- <span id="rvq_remote_Vista_size_query" class="anchor"></span>RVQ—Remote VistA Size Query \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\]: Prompts the user for a package and a VistA domain to request a size report for the selected package (see Section <u>2.2.14</u>). A size report query message is sent to the selected VistA domain. These actions are available from the “VistA Package Size Analysis Manager” and the “VistA Package Size Analysis Manager - Package Statistics” screens:
- “VistA Package Size Analysis Manager” Screen—When the RVQ action is run from this screen, the request prompts the user to select a Package Parameter file and sends the request to the remote VistA, so the report can be created on the remote VistA.
- “VistA Package Size Analysis Manager - Package Statistics” Screen—When the RVQ action is run from this screen, the request sends the Package Parameter file used to create the displayed report to the remote VistA, so that an apples-to-apples size report is returned from the remote VistA. That is the same package parameters that are used to create the report.
- <span id="shd_swap_header" class="anchor"></span>SHD—Swap Header \[XTVS PKG RPT SWAP HEADER\]: Changes the ListMan header section on the VistA Package Size Report for all packages to the alternate header (see Section <u>2.2.17</u>). This action is only active when a user readable report for all packages is displayed. For example, this action is *not* active on a screen if the date headings are displayed next to the data on the VistA Size Report for a single package.
- \[XTVS BLANK 1\]: This protocol is used to format spaces in ListMan menu lists. It is *not* a user-selectable action.

## Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Package Size Reporting Tool has one Security key:

XTVS EDITOR

Users *must* hold the XTVS EDITOR security key in order to execute the following VistA Package Size Reporting Tool (VPSRT) Analysis Manager actions and menus:

- [EM—Extract Manager](#em_extract_manager) \[XTVS PKG MGR EXT MNGR ACTION\] action
- [DPF—Delete Package Parameter File](#dpf_delete_package_parameter_file) \[XTVS PKG MGR PARAM FILE DELETE ACTION\] action
- [CHD—Change Host Directory](#chd_change_host_directory) \[XTVS SITE PARAMETERS\] action
- [PMD—Display/Edit Package Parameters](#pmd_display_edit_package_parameters) \[XTVS PKG MGR PARAM DISP/EDIT ACTION\] action
- [UNL—Unlock Parameter File](#unl_unlock_parameter_file) \[XTVS PKG MGR PARAM UNLOCK ACTION\] action

## Lock Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Package Size Reporting Tool (VPSRT) includes a Lock function via the [UNL—Unlock Parameter File](#unl_unlock_parameter_file) \[XTVS PKG MGR PARAM UNLOCK ACTION\] action. If a lock is obtained by the action, it indicates the lock was obtained and then continues. If the Package Parameter file is locked by another user, a message is displayed to the user indicating that the file is locked by another user.

The following VistA Package Size Reporting Tool (VPSRT) Analysis Manager actions and menus check the selected Extract Package Parameter file lock before continuing:

- [PMD—Display/Edit Package Parameters](#pmd_display_edit_package_parameters) \[XTVS PKG MGR PARAM DISP/EDIT ACTION\]
- [VSR—Display VistA Size Report](#vsr_display_vista_size_report) \[XTVS PKG MGR VISTA SIZE RPT\]
- [DPF—Delete Package Parameter File](#dpf_delete_package_parameter_file) \[XTVS PKG MGR PARAM FILE DELETE ACTION\]
- [DC—Display Captioned Parameter](#dc_display_captioned_parameters) \[XTVS PKG MGR PARAM DISP CAPTION ACTION\]
- [EPP—Edit Package Parameters](#epp_edit_package_parameters) \[XTVS PKG MGR EDIT PACKAGE PARM ACTION\]
- [DPE—Delete Package Parameter Entry](#dpe_delete_package_parameter_entry) \[XTVS PKG MGR DEL PACKAGE PARM ACTION\]
- [SPP—Save Package Parameter Changes](#spp_save_package_parameter_changes) \[XTVS PKG MGR SAVE PACKAGE PARM ACTION\]
- [RVQ—Remote VistA Size Query](#rvq_remote_Vista_size_query) \[XTVS PKG MGR RPT QUERY REMOTE ACTION\] and \[XTVS PKG QUERY REMOTE VISTA SIZE ACTION\]

When a lock is requested and received, the text in <u>Figure 4</u> is displayed:

<span id="_Ref52283235" class="anchor"></span>Figure 4: Lock Function Message—Lock Obtained (Requested and Received)

   XTMPSIZE_QG_Demo.DAT LOCK obtained.

Press Return to continue:

When a file lock is released, the text in <u>Figure 5</u> is displayed:

<span id="_Ref52283246" class="anchor"></span>Figure 5: Lock Function Message—Lock Released

   Parameter file XTMPSIZE_QG_Demo.DAT LOCK released.

Press Return to continue:

When a lock request is denied, the text in <u>Figure 6</u> is displayed:

<span id="_Ref52283258" class="anchor"></span>Figure 6: Lock Function Message—Lock Request Denied

\<\* LOCK request denied! Try again later. \*\>

   Parameter file XTMPSIZE_QG_Demo.DAT LOCKED by \$JOB PID \####

Press Return to continue:

If a lock becomes corrupted while a Package Parameter file is being used, the message in <u>Figure 7</u> is displayed:

<span id="_Ref52283273" class="anchor"></span>Figure 7: Lock Function Message—Lock Error: Corrupted while Package Parameter File in Use

\<\* LOCK ERROR. LOCK required to proceed. Check LOCK file Integrity. \*\>

   LOCK Check Failure: Parameter file has been UNLOCKED by another process!

Press Return to continue:

When a lock is being released, it is checked to confirm it is still held by the releasing user. If the release check finds the lock corrupted, the message in <u>Figure 8</u> is displayed:

<span id="_Ref52283326" class="anchor"></span>Figure 8: Lock Function Message—Lock Check Failure

   LOCK Check Failure: Parameter file has been UNLOCKED by another process!

Press Return to continue:

## Temporary Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the ^TMP globals used to sort and count the package data. The VistA Package Size Reporting Tool (VPSRT) uses these ^TMP global arrays to build screens for double counting Package Prefixes. These arrays serve as indexes for package prefixes from both KIDS patch build entries and the Package Parameter file initialized from the PACKAGE (#9.4) file on FORUM.

These ^TMP global indexes are used to improve the accuracy of package report statistics.

The system is designed to identify and eliminate Prefixes assigned to multiple packages from being used to identify components counted in both packages.

The following three conditions affect the package size report for a multiply assigned Prefix:

- Packages assigned the Prefix are both in the Package Parameter file.
- Prefix is or is not a Primary Prefix for one of the packages.
- Prefix is or is not used in the name of the KIDS builds for one of the packages.

Prefix Types

The following are the different Prefix types:

- Primary Prefix—Always used to identify package components.
- KIDS Build Prefix—Always used to identify package components. The KIDS Build Prefix is the prefix used by a package in the Package Parameter file to name KIDS builds for that packages' patches.
- Additional Prefix—Used to identify components in multiple packages when the Prefix is defined for those packages.

Special Conditions

- When a Prefix is used as a Primary Prefix for one package and a KIDS Build Prefix for a different package, the Prefix is used to count components for *both* packages.
- An Additional Prefix is *not* used to identify components in a package when another package in the Package Parameter file defines the Prefix as either the KIDS Build Prefix or Primary Prefix.
- An Additional Prefix is used to identify components in a package when it is a subset of a Primary Prefix or a KIDS Build Prefix for a package in the Package Parameter file.

### ^TMP Globals Used by Report of All Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ^TMP(“XTVS-FORUMPKG” ,\$J,) Array

The ^TMP(“XTVS-FORUMPKG”,\$J,*\<XTMP\*.DAT line item \#\>*) array is an array of lines loaded from the selected XTMP\*.DAT file.

Each line contains a caret (^)-delimited data elements with some fields containing a pipe character (\|)-delimited sub-elements.

The array is used to extract package parameter data for each package defined in the selected XTMP\*.DAT text file.

Created by a FOR loop that reads each line of the XTMP\*.DAT text file or line of text in the XTVS: PACKAGE FILE EXTRACT & REPORT REQUEST server message.

Code is in LOOP^XTVSRFL and SRVREXT^XTVSSVR.

Format:

^TMP(“XTVS-FORUMPKG”,\$J,*\<XTMP\*.DAT line item \#\>*)=Package parameter data for a single VistA package.

### ^TMP Globals Used by Report of Single Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ^TMP(“XTVS-PARAM-CAP”,\$J,) Array

The ^TMP(“XTVS-PARAM-CAP”,\$J) array is a set single line array and caption display array for action processing. This array is used to select a package to report.

Created by the SCAPARY^XTVSLP and CHKX^XTVSLPDC APIs.

Format:

^TMP(“XTVS-PARAM-CAP”,\$J,*\<pkg name\>*)=*\<Data line read from the selected XTMP\*.DAT file\>*^TMP(“XTVS-PARAM-CAP”,\$J, *\<pkg name\>*,1, “Package Name”)=*\<1st piece of XTMP\*.DAT file\>*^TMP(“XTVS-PARAM-CAP”,\$J, *\<pkg name\>*,2,“Primary Prefix”)=*\<2nd piece of XTMP\*.DAT file\>*^TMP(“XTVS-PARAM-CAP”,\$J, *\<pkg name\>*,3,“\*Lowest File#”)=*\<3rd piece of XTMP\*.DAT file\>*^TMP(“XTVS-PARAM-CAP”,\$J, *\<pkg name\>*,4,“\*Highest File#”)=*\<4th piece of XTMP\*.DAT file\>*^TMP(“XTVS-PARAM-CAP”,\$J, *\<pkg name\>*,5,“Additional Prefixes”)=*\<5th piece of XTMP\*.DAT file\>*^TMP(“XTVS-PARAM-CAP”,\$J, *\<pkg name\>*,6,“Excepted Prefixes”)=*\<6th piece of XTMP\*.DAT file\>*^TMP(“XTVS-PARAM-CAP”,\$J, *\<pkg name\>*,7,“File Numbers”)=*\<7th piece of XTMP\*.DAT file\>*^TMP(“XTVS-PARAM-CAP”,\$J, *\<pkg name\>*,8,“File Ranges”)=*\<8th piece of XTMP\*.DAT file\>*^TMP(“XTVS-PARAM-CAP”,\$J, *\<pkg name\>*,9,“Parent Package”)=*\<9th piece of XTMP\*.DAT file\>*

### ^TMP Globals Used by Report for both All & Single Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ^TMP(“XTVS-KIDSPFX-IDX” ,\$J,) Array

The ^TMP(“XTVS-KIDSPFX-IDX”,\$J,KIDSPRFX) array creates Prefix-Package Indexes from KIDS. This array is used as a check to screen double counting overlap package components by Primary Prefix. Each KIDS’ primary prefix node is assigned to the Package Name in the local Package File pointed to by a KIDS build in the BUILD (#9.6) file.

Created by KIDSIDX^XTVSRFL1.

Format:

^TMP(“XTVS-KIDSPFX-IDX”,\$J,*\<prefix used in KIDS build name\>*)=*\<Package name from Package file entry pointed to by KIDS build\>*

#### ^TMP(“XTVS-IDX-PKG”,\$J,,) Array

The ^TMP(“XTVS-IDX-PKG”,\$J,*\<pkg -primary/additional- prefix\>*,*\<pkg name\>*) array sets an array index node for each prefix assigned to the Package from the Package Parameter file equal to the KIDS build patch assigned to the package. This array is used to identify multiple packages using the same prefix.

Created by a FOR loop through ^TMP(“XTVS-PARAM-CAP”,\$J,*\<pkg name\>*) arrays.

Code is in TALLYRPT^XTVSRFL and PARAMIDX^XTVSRFL1.

Format:

^TMP(“XTVS-IDX-PKG”,\$J,*\<pkg -primary/additional prefix\>*,*\<pkg name\>*)=1 or “” to indicate if the prefix is a KIDS build prefix for the package

#### ^TMP(“XTVS-PREFIX-IDX” ,\$J,,) Array

The ^TMP(“XTVS-PREFIX-IDX”,\$J,*\<XTMP\*.DAT package name\>*,*\<XTMP\*.DAT package primary prefix\>*) array creates a Package-Prefix index from the package parameters for each application in the selected XTMP\*.DAT file. The array is used to identify primary prefixes defined in the selected XTMP\*.DAT file.

Created by a FOR loop through the ^TMP(“XTVS-FORUMPKG”,\$J,*\<pkg name\>*,*\<pkg prefix\>*) and ^TMP(“XTVS-PARAM-CAP”,\$J,*\<pkg name\>*,*\<pkg prefix\>*) arrays.

Code is in TALLYRPT^XTVSRFL and PARAMIDX^XTVSRFL1, respectively.

Format:

^TMP(“XTVS-PREFIX-IDX”,\$J,*\<XTMP\*.DAT package name\>*,*\<XTMP\*.DAT package primary prefix\>*)=*\<NULL\>*

#### ^TMP(“XTVS-FORUM-PFXS” ,\$J,) Array

The ^TMP(“XTVS-FORUM-PFXS”,\$J,*\<XTMP\*.DAT package primary prefix\>*) array creates a Prefix index from package parameters for each application in the selected ^XTMP\*.DAT file. The array is used to identify primary and additional prefix extensions that are primary prefixes for any package.

Created by TALLYRPT^XTVSRFL and PARAMIDX^XTVSRFL1.

Format:

^TMP(“XTVS-FORUM-PFXS”,\$J,PKGPFX)=*\<NULL\>*

## Data Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 9</u> describes the VistA Package Size Reporting Tool (VPSRT) data flow.

<span id="_Ref467071216" class="anchor"></span>Figure 9: VPS Reporting Tool—Data Flow and Basic Process Overview

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/018.png)

<span id="_Ref480273707" class="anchor"></span>Figure 10: VPS Reporting Tool—Package Changes Flow (1 of 2)

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/019.png)

<span id="_Ref480273713" class="anchor"></span>Figure 11: VPS Reporting Tool—Package Changes Flow (2 of 2)

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/020.png)

<span id="_Ref2678657" class="anchor"></span>Figure 12: VPS Reporting Tool—Data Usage Map: Package File and Extract Global Data Elements

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/021.png)

<span id="_Ref2678658" class="anchor"></span>Figure 13: VPS Reporting Tool—Data Usage Map: Extract Global and Package Parameter File Data Elements

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/022.png)

## Run-Time Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 14</u> is a diagram of the VPS Reporting Tool run-time components:

<span id="_Ref2678659" class="anchor"></span>Figure 14: VPS Reporting Tool—Run-Time Components

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/023.png)

# Using the VistA Package Size Reporting Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Package Size Reporting Tool (VPSRT) contains a suite of functionality that allows users to configure package parameters to report package size statistics without changing data in the Veterans Health Information Systems and Technology Architecture (VistA) PACKAGE (#9.4) file.

## Package Parameter Generation and Statistics Reporting Flow—Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Create New Package Parameter File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a *new* Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)), do the following:

1.  Extract the most current and accurate PACKAGE (#9.4) file data available. Currently, the most accurate PACKAGE (#9.4) file is located on FORUM (see Section <u>2.2.1</u>). This extract be completed by either of the following methods:
- From FORUM via the CE—Extract Package Data \[XTVS PKG EXTRACT CREATE ACTION\] action on the “VistA Package Size Analysis Manager – Extract Manager” screen.  
    
  Or:
- From any VistA with VA MailMan access to FORUM via the REQ—Remote VistA Extract Query \[XTVS PKG EXT QUERY REMOTE ACTION\] action on the same ListMan screen.

If any of package names in the extract contain a double quote (“), the following occurs:

1.  Double quote is converted to two single quotes to allow string parsing through the name.
2.  User receives a VA MailMan message indicating the changes applied in the extract (see <u>Figure 15</u> and <u>Figure 29</u>).
10. Send a PackMan message of the extracted PACKAGE (#9.4) file global to a “Platinum VistA” system, which is a fully-patched Class I instance of VistA where the package size report functions are executed (see Section <u>2.2.1</u>).
11. Read the FORUM PackMan message on the “Platinum VistA” system and extract the global from the message (see Section <u>2.2.2</u>).
12. Invoke the VistA Package Extract Manager \[XTVS VISTA PACKAGE EXTRACT MGR\] option (see Section <u>2.2.3</u>). This opens the “VistA Package Size Analysis Manager” screen.
13. From the “VistA Package Size Analysis Manager” screen, invoke the EM—Extract Manager \[XTVS PKG MGR EXT MNGR ACTION\] action (see Section 2.2.4). This opens the “VistA Package Size Analysis Manager - Extract Manager” screen.
14. From the “VistA Package Size Analysis Manager - Extract Manager” screen, select the CXP—Convert Extract to Parameter List \[XTVS PKG EXT CRT PARAM ACTION\] action to create a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) list (see Section <u>2.2.5</u>).
15. The system displays the “VistA Package Size Analysis Manager – Package Parameters” screen with a list of the Extract Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) created from the raw PACKAGE (#9.4) file extract data. The following actions are included:
- [RPL—Display Parameter List](#rpl_display_parameter_list) \[XTVS PKG EXT REDISP PARAM ACTION\] (see Section <u>2.2.5.1</u>)
- [DPC—Display Parameter Corrections](#dpc_display_parameter_corrections) \[XTVS PKG EXT DISP CORRECTIONS ACTION\] (see Section <u>2.2.5.2</u>)
- [WPF—Write Parameter List to File](#wpf_write_parameter_list_to_file) \[XTVS PKG EXT PARAM WRT ACTION\] (see Section <u>2.2.6</u>)
- [EPC—Email Corrections Rpt & Parameters](#epc_email_corrections_rpt_and_parameters) \[XTVS PKG MGR NEW PARAM MAIL ACTION\] (see Section <u>2.2.5.3</u>)

Use these actions as necessary to review the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) created (see Section <u>2.2.5</u>).

16. When satisfied with the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) created, invoke the WPF—Write Parameter List to File \[XTVS PKG EXT PARAM WRT ACTION\] action (see Section <u>2.2.6</u>). This creates a .DAT file in the VistA Package Size default directory with the following file name format:

XTMPSIZE\_*\<user initials\>\<mm-dd-yy_hhmm\>*.DAT

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/024.png) REF: For more information on setting the VistA Package Size default directory, see Section <u>2.2.15</u>, “<u>Change Host File Directory</u>.”.

Alternately, invoke the EPC—Email Corrections Rpt & Parameters \[XTVS PKG MGR NEW PARAM MAIL ACTION\] action (see Section <u>2.2.5.3</u>) to send the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) and corrections report to another server and move it to an alternate Package Parameters reporting system.

17. Return to the “VistA Package Size Analysis Manager” screen:
1.  Enter Quit in the “VistA Package Size Analysis Manager - Package Parameters” screen.
3.  Enter Quit again in the “VistA Package Size Analysis Manager - Extract Manager” screen.
18. Verify the new Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) has been added to the list for editing (see Section <u>2.2.7</u>).
19. Do a comparison to identify the differences between the *previous* FORUM Extract XTMPSIZE\*.DAT file and the *new* FORUM Extract XTMPSIZE\*.DAT file (see Section <u>2.2.8</u>):
1.  From the “VistA Package Size Analysis Manager – Parameter Display” screen, select the DO—Display Package Overlap List \[XTVS PKG MGR PARAM ERR DISP ACTION\] action (see Section <u>2.2.9</u>).
4.  If you need to change package parameters, from the “VistA Package Size Analysis Manager – Parameter Display” screen, select the DC—Display Captioned Parameters \[XTVS PKG MGR PARAM DISP CAPTION ACTION\] action (see Section <u>2.2.10</u>).
20. Once the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) has been updated to better reflect package definitions (see Sections <u>2.2.11</u> and <u>2.2.12</u>), return to the “VistA Package Size Analysis Manager” screen and find the newly updated Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) in the list.
21. From the “VistA Package Size Analysis Manager” screen, select the VSR—Display VistA Size Report \[XTVS PKG MGR VISTA SIZE RPT\] action (see Section <u>2.2.13</u>). It prompts the user for the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) to use for reporting size statistics.

After choosing a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)), the user selects one of the following report options:

- Selected VistA Package—Reports statistics for just the *selected* VistA package (see Section <u>2.2.13</u>)
- ALL VistA Packages—Reports statistics for *all* VistA packages according to the format of one of five report selections (see Section <u>2.2.13.2</u>).

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/025.png) NOTE: Reporting for “ALL VistA Packages” can take several minutes to complete.

22. When the report is displayed on the “VistA Package Size Analysis Manager – Package Statistics” screen, the user can select either of the following actions (see Section <u>2.2.13</u>):
- [CTF—Create Text File](#ctf_create_text_file) \[XTVS PKG MGR RPT WRT ACTION\] (see <u>Figure 70</u> in Section <u>2.2.13</u>)
- [RVQ—Remote VistA Size Query](#rvq_remote_Vista_size_query) \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] (see Section <u>2.2.14</u>)
- [ER—Email Rpt Attachment](#er_e_mail_rpt_attachment) \[XTVS PKG MGR RPT MAIL ACTION\] (see <u>Figure 71</u> in Section <u>2.2.13</u>)
- [SHD—Swap Header](#shd_swap_header) \[XTVS PKG RPT SWAP HEADER\] (see Section <u>2.2.17</u>)

These actions allow users to write text files that can be input to other applications (e.g., Health Product Support \[HPS\] Parametric Estimation Model).

### Update Existing Package Parameter File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To update an *existing* Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)), do the following:

1.  Extract the most current and accurate PACKAGE (#9.4) file data available. Currently, the most accurate PACKAGE (#9.4) file is located on FORUM (see Section <u>2.2.1</u>).
23. Send a PackMan message of the extracted PACKAGE (#9.4) file global to a “Platinum VistA” system, which is a fully patched Class I instance of VistA where the package size report functions are executed (see Section <u>2.2.1</u>).
24. Read the FORUM PackMan message on the “Platinum VistA” system and extract the global from the message (see Section <u>2.2.2</u>).
25. Invoke the VistA Package Extract Manager \[XTVS VISTA PACKAGE EXTRACT MGR\] option (see Section <u>2.2.3</u>). This opens the “VistA Package Size Analysis Manager” screen.
26. From the “VistA Package Size Analysis Manager” screen, invoke the EM—Extract Manager \[XTVS PKG MGR EXT MNGR ACTION\] action (see Section <u>2.2.4</u>). This opens the “VistA Package Size Analysis Manager - Extract Manager” screen.
27. From the “VistA Package Size Analysis Manager - Extract Manager” screen, select the CXP—Convert Extract to Parameter List \[XTVS PKG EXT CRT PARAM ACTION\] action to create a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) list (see Section <u>2.2.5</u>).
28. When satisfied with the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) created, invoke the WPF—Write Parameter List to File \[XTVS PKG EXT PARAM WRT ACTION\] action (see Section 2.2.6).

This creates a .DAT file in the VistA Package Size default directory with the following file name format:

XTMPSIZE\_*\<user initials\>\<mm-dd-yy_hhmm\>*.DAT

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/026.png) REF: For more information on setting the VistA Package Size default directory, see Section <u>2.2.15</u>, “<u>Change Host File Directory</u>.”

Alternately, invoke the EPC—Email Corrections Rpt & Parameters \[XTVS PKG MGR NEW PARAM MAIL ACTION\] action (see Section <u>2.2.5.3</u>) to send the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) and corrections report to another server and move it to an alternate Package Parameters reporting system.

29. Return to the “VistA Package Size Analysis Manager” screen:
1.  Enter Quit on the “VistA Package Size Analysis Manager - Package Parameters” screen.
5.  Enter Quit again on the “VistA Package Size Analysis Manager - Extract Manager” screen.
30. Verify the new Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) has been added to the list for editing (see Section <u>2.2.7</u>).
31. Do a comparison to identify the differences between the *previous* FORUM Extract XTMPSIZE\*.DAT file and the *new* FORUM Extract XTMPSIZE\*.DAT file (see Section <u>2.2.8</u>).
1.  From the “VistA Package Size Analysis Manager – Parameter Display” screen, select the DO—Display Package Overlap List \[XTVS PKG MGR PARAM ERR DISP ACTION\] action (see Step 1 in Section <u>2.2.9</u>).
6.  From the “VistA Package Size Analysis Manager – Parameter Display” screen, invoke the CPF—Parameter File Comparison \[XTVS PKG MGR PARAM COMPARE ACTION\] action and select the previous FORUM extract Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) (see Step 4 in Section <u>2.2.9</u>).
7.  If you need to change package parameters, from the “VistA Package Size Analysis Manager – Parameter Display” screen, select the DC—Display Captioned Parameters \[XTVS PKG MGR PARAM DISP CAPTION ACTION\] action (see Section <u>2.2.10</u>).
32. From the “VistA Package Size Analysis Manager” screen, invoke the PMD—Display/Edit Package Parameters \[XTVS PKG MGR PARAM DISP/EDIT ACTION\] action. Select the previous Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) used to generate the last VistA Size Report (see Section <u>2.2.8</u>).

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/027.png) NOTE: The PMD—Display/Edit Package Parameters \[XTVS PKG MGR PARAM DISP/EDIT ACTION\] action is locked with the XTVS EDITOR security key.

33. From the “VistA Package Size Analysis Manager – Parameter Display” screen, invoke the DC—Display Captioned Parameters \[XTVS PKG MGR PARAM DISP CAPTION ACTION\] action to apply the necessary changes identified from the comparison of the new FORUM Package Extract to the previous FORUM Package Extract (see Section <u>2.2.10</u>).
34. From the “VistA Package Size Analysis Manager - Parameter Display” screen, use the DO—Display Package Overlap List \[XTVS PKG MGR PARAM ERR DISP ACTION\] action (see Step 1 in Section <u>2.2.9</u>).

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/028.png) NOTE: If package edits are made, be sure to save the changes with the SPP—Save Package Parameter Changes \[XTVS PKG MGR SAVE PACKAGE PARM ACTION\] action on the “VistA Package Size Analysis Manager – Captioned List” screen (see Section <u>2.2.12</u>). Make sure that you save the file to the *same* name.

35. Once the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) has been updated to better reflect package definitions, the user can return to the “VistA Package Size Analysis Manager” screen and find the newly updated Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) from the list (see Step 3 in Section <u>2.2.12</u>).
36. From the “VistA Package Size Analysis Manager” screen, select the VSR—Display VistA Size Report \[XTVS PKG MGR VISTA SIZE RPT\] action (see Section <u>2.2.13</u>). It prompts the user for the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) to use for reporting size statistics.

After choosing a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)), the user selects one of the following report options:

- Selected VistA Package—Reports statistics for just the *selected* VistA package (see Section <u>2.2.13</u>)
- ALL VistA Packages—Reports statistics for *all* VistA packages according to the format of one of five report selections (see Section <u>2.2.13.2</u>).

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/029.png) NOTE: Reporting for “ALL VistA Packages” can take several minutes to complete.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/030.png) NOTE: This step reports a VistA Package Size on the *local* VistA instance. A size report for a single VistA package can be requested from a *remote* VistA instance via the RVQ—Remote VistA Size Query \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] action on the “VistA Package Size Analysis Manager” screen.

37. When the report is displayed on the “VistA Package Size Analysis Manager – Package Statistics” screen, users can select either of the following actions (see Section <u>2.2.13</u>):
- [CTF—Create Text File](#ctf_create_text_file) \[XTVS PKG MGR RPT WRT ACTION\] (see <u>Figure 70</u> in Section <u>2.2.13</u>)
- [RVQ—Remote VistA Size Query](#rvq_remote_Vista_size_query) \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] (see Section <u>2.2.14</u>)
- [ER—Email Rpt Attachment](#er_e_mail_rpt_attachment) \[XTVS PKG MGR RPT MAIL ACTION\] (see <u>Figure 71</u> in Section <u>2.2.13</u>)
- [SHD—Swap Header](#shd_swap_header) \[XTVS PKG RPT SWAP HEADER\] (see Section <u>2.2.17</u>)

These actions allow users to write text files that can be input to other applications (e.g., Health Product Support \[HPS\] Parametric Estimation Model).

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/031.png) NOTE: The “VistA Package Size Analysis Manager – Package Statistics” ListMan screen also includes the RVQ—Remote VistA Size Query \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] action, which allows the user to query another VistA instance for a single package size report. That report could be used to compare to the size reported for the same package on the local VistA.

## Package Parameter Generation and Statistics Reporting Flow—Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/032.png) NOTE: The names of packages should *not* contain double quotation marks. If a PACKAGE (#9.4) file extract includes a package name that contains double quotation marks (“), the tool *cannot* parse the name of the package. Double quotation marks (“) need to be “cleaned up” from package names *before* the extract is completed.

### Extract Package File Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Extract the most current and accurate PACKAGE (#9.4) file data available. Currently, the most accurate PACKAGE (#9.4) file is located on FORUM.

To extract package file data, use either of the following methods:

- <u>Send Package File Extract via Packman Option</u> \[XTVS PKG MGR EXT PACKAGE MSG\]
- <u>Remote VistA Extract Query Action</u> \[XTVS PKG EXT QUERY REMOTE ACTION\]

If any of package names in the extract contain a double quote (“), the following occurs:

1.  Double quote is converted to two single quotes to allow string parsing through the name.
2.  User receives a VA MailMan message, as shown in <u>Figure 15</u>:

> <span id="_Ref53652217" class="anchor"></span>Figure 15: Sample VA MailMan Message—Double Quote Edits

Subj: PACKAGE EXTRACT (*SITE1PRO*) ; data cleanup! \[#160427\] 10/08/20@13:36

3 lines

From: POSTMASTER In 'IN' basket. Page 1

----------------------------------------------------------------------------

Notice for Package Extract on *SITE1PRO*.

Data was cleaned up on ABC 4'' LABEL extract.

<span class="mark">Double Quotes changed to 2 single quotes in the ABC 4'' LABEL Package name.</span>

Enter message action (in IN basket): Ignore//

#### Send Package File Extract via Packman Option

To extract the most current and accurate PACKAGE (#9.4) file data using the Send Package File Extract via Packman \[XTVS PKG MGR EXT PACKAGE MSG\] option, do the following:

1.  Execute the Send Package File Extract via Packman \[XTVS PKG MGR EXT PACKAGE MSG\] option, as shown in <u>Figure 16</u>.
38. Send the PackMan message of the PACKAGE (#9.4) file global extract to the user who will extract the global on a “Platinum VistA” system (e.g., HPS “Platinum VistA” system).

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/033.png) NOTE: A “Platinum VistA” system is a fully patched Class I instance of VistA where the package size report functions are executed.

> <span id="_Ref482254747" class="anchor"></span>Figure 16: Send Package File Extract via Packman Option—Package File Extract

Select OPTION NAME: <span class="mark">XTVS PKG MGR EXT PACKAGE MSG</span>

Send Package File Extract via Packman

Send mail to: XUUSER,ONE// <span class="mark">\<Enter\></span> XUUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">ONE.XUUSER@VA.GOV</span>

Looking in Internet Suffix file... US GOVERNMENT via REDACTED.VA.GOV

And Send to: <span class="mark">\<Enter\></span>

Created by XUUSER,ONE at *SITE1PRO*.REDACTED.VA.GOV on Monday, 10/31/16 at 14:21......

^XTMP("XTSIZE",7032) Emailed via PackMan. \[MSG \#:77320\]

Press Return to continue:

#### Remote VistA Extract Query Action

Alternatively, to request a Package file extract from FORUM using the REQ—Remote VistA Extract Query \[XTVS PKG EXT QUERY REMOTE ACTION\] action, do the following:

1.  Navigate to the “VistA Package Size Analysis Manager – Extract Manager” screen, as shown in <u>Figure 17</u>.
2.  From the “VistA Package Size Analysis Manager – Extract Manager” screen, select the REQ—Remote VistA Extract Query \[XTVS PKG EXT QUERY REMOTE ACTION\] action.
3.  At the “Do you want to query the Forum Package File? YES//” prompt, enter YES (default).
4.  At the “Do you want a VistA Package Size Report for all packages on Forum? NO//” prompt, enter NO (default). If you answer YES to this prompt, the system sends a VistA Package Size Report for all packages on FORUM.

> <span id="_Ref52203929" class="anchor"></span>Figure 17: “VistA Package Size Analysis Manager – Extract Manager” Screen—Remote VistA Extract Query Action

Select OPTION NAME: <span class="mark">XTVS VISTA PACKAGE EXTRACT MGR \<Enter\></span> VistA Package Extract Manager

Do you want to Display XTMPSIZE\*.BAK (backup files)? NO// <span class="mark">\<Enter\></span>

VistA Package Size Manager Jul 29, 2020@09:44:36 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 7.3 Build: 90

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

XTMPSIZE.DAT Package Parameter file list in /srv/vista/*\<scd\>*/user/hfs/:

--------------------------------------------------------------------

1\) XTMPSIZE_GTS11-15-16_1436.DAT

2\) XTMPSIZE_GTS4-2-20_0944.DAT

3\) XTMPSIZE_GTS5-14-20_1023.DAT

4\) XTMPSIZE_GTS5-14-20_1025.DAT

5\) XTMPSIZE_GTS6-29-20_0712.DAT

6\) XTMPSIZE_QG_Demo.DAT

Enter ?? : more actions & Help, ??? : Process Help

<span class="mark">EM Extract Manager</span> DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Quit// <span class="mark">EM \<Enter\></span> Extract Manager

Package Extract Manager Jul 29, 2020@09:44:38 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 7.3 Build: 90

Extracted package ^XTMP global list

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

Process ID System Date/Time

----------------------------------------------------

No Extracts defined.

Enter ?? for more actions and Help

CE Extract Package Data DEL (Delete Extract)

ED (Display Extract) CXP (Convert Extract to Parameter list)

ME (E Mail Extract Global) <span class="mark">REQ Remote VistA Extract Query</span>

Select Action:Quit// <span class="mark">REQ \<Enter\></span> Remote VistA Extract Query

The response from a remote VistA can take some time.

Do you want to query the Forum Package File? YES// <span class="mark">\<Enter\></span>

Do you want a VistA Package Size Report for all packages on Forum? NO// <span class="mark">\<Enter\></span>

Query message sent! Message \# 91525

Press Return to continue: <span class="mark">\<Enter\></span>

Package Extract Manager Jul 29, 2020@09:45:10 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 7.3 Build: 90

<span class="mark">Extracted package ^XTMP global list</span>

<span class="mark">XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/</span>

Process ID System Date/Time

----------------------------------------------------

<span class="mark">No Extracts defined.</span>

Enter ?? for more actions and Help

CE Extract Package Data DEL (Delete Extract)

ED (Display Extract) CXP (Convert Extract to Parameter list)

ME (E Mail Extract Global) REQ Remote VistA Extract Query

Select Action:Quit//

#### Package Extract Errors

Error messages are returned to the requesting user when the remote server fails to return the requested extract.

The package extract errors in <u>Figure 18</u> are also added to the Kernel error trap on the remote VistA when the error occurs:

<span id="_Ref61506485" class="anchor"></span>Figure 18: Sample Package Extract Errors Added to Kernel Error Trap

16)  ONERPT^XTVSSVR : Package extract error10:14:40  SITE1PRO:DEVR0TSVR    31493
13)  RPTSIZE^XTVSSVR : Package extract error10:14:34  SITE1PRO:DEVR0TSVR    31493
12)  EEXT^XTVSSVR : Package extract error10:14:33  SITE1PRO:DEVR0TSVR    31493
11)  EEXT^XTVSSVR : Package extract error10:14:32  SITE1PRO:DEVR0TSVR    31493

The Package Extract error is broken into the following components (see <u>Figure 18</u>):

- Item Number—The item number for the Error entry. Developers enter this number to select an error for view (e.g., 16, 15, 14,…).
- Tag^Routine—This is the Tag^Routine that generated the error (e.g., ONERPT^XTVSSVR).
- Text following the colon:
- Error Description—The is the error description (e.g., Package extract error).
- Error Time—Time the error occurred (e.g., 10:14:40)
- Cache/IRIS Namespace (e.g., SITE1PRO).
- Name of the Server Host (e.g., DEVR0TSVR).
- Job Process ID (e.g., 31493).

<span id="_Ref63059044" class="anchor"></span>Figure 19: Sample Package Size Report Error Message—Extract Failed: ^XTMP Not Created on Server

Subj: PACKAGE SIZE REPORT (*SITE1PRO* ; remote request FAILED!  \[#91771\]

08/21/20@10:27  2 lines

From: XTUSER,ONE  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Remote package size report on *SITE1PRO* failed!!

Extract failed!  ^XTMP("XTSIZE",123) not created on Server!

Enter message action (in IN basket): Ignore//

### Unload Package Extract Global on VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Extracting the global from the PackMan message creates an ^XTMP(“XTSIZE”,\$JOB) global. \$JOB is assigned by the Caché process on FORUM from which the PackMan message was created. Extracting the message overwrites any existing ^XTMP(“XTSIZE”) global with the same \$JOB process number.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/034.png) NOTE: You should *not* overwrite an existing ^XTMP(“XTSIZE”) global if it has more current and accurate PACKAGE (#9.4) file data than that which is extracted from the current PackMan message.

To unload the Package Extract global on the “Platinum VistA” system, do the following:

1.  On the “Platinum VistA” system:
1.  Open VistA MailMan 8.0.
8.  Read the PackMan message containing the PACKAGE (#9.4) file global extract, as shown in <u>Figure 20</u>:

> <span id="_Ref482364466" class="anchor"></span>Figure 20: VistA MailMan PackMan Message Extract: Example (REDACTED)

> ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/035.png)

39. At the Enter message action (in IN basket): Ignore//” prompt enter X or Xtract PackMan to bring up the Load PackMan Message \[XMPACK\] option.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/036.png) NOTE: The Load PackMan Message \[XMPACK\] option is defined in the ^DOPT global. This global supports VA FileMan but is *not* editable from VA FileMan (i.e., it is *not* a VA FileMan compatible global.)

40. From the Load PackMan Message \[XMPACK\] option, select the Install/Check Message option to load the ^XTMP(“XTSIZE”) global onto the VistA system.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/037.png) NOTE: The Install/Check Message option requires the user to hold the XUPROGMODE security key and have VA FileMan programmer privileges \[DUZ(0)=“@”\].

41. The system installs the most updated PACKAGE (#9.4) file data from FORUM into a temporary global where it can be loaded and further modified to report the most current and accurate package size data from the VistA system.

### Invoke Vista Package Size Analysis Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the VistA system, do the following:

1.  Use the VistA Package Extract Manager \[XTVS VISTA PACKAGE EXTRACT MGR\] option to invoke the “VistA Package Size Analysis Manager” screen (aka “VistA Package Extract & Rpt Manager”).
42. At the “Do you want to Display XTMPSIZE\*.BAK (backup files)? NO//” prompt, enter NO (default), as shown in <u>Figure 21</u>:

> <span id="_Ref467071974" class="anchor"></span>Figure 21: VistA Package Extract Manager Option—Sample User Prompts and Responses

Select OPTION NAME: <span class="mark">XTVS VISTA PACKAGE EXTRACT MGR</span>

VistA Package Extract & Rpt Manager

Do you want to Display XTMPSIZE\*.BAK (backup files)? NO// <span class="mark">\<Enter\></span>

In most cases, accept the NO default, so \*.BAK files are *not* displayed.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/038.png) NOTE: Generally, only \*.BAK files would be displayed for selection and rewritten to another file when a Package Parameter “rollback” situation is necessary.

43. The system displays the “VistA Package Size Analysis Manager” screen with the list of Package Parameter files (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)), as shown in <u>Figure 22</u>:

> <span id="_Ref467071949" class="anchor"></span>Figure 22: “VistA Package Size Analysis Manager” Screen—ListMan Screen

<u>Vista Package Size Manager Apr 14, 2017@13:59:46 Page: 1 of 4</u>

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 1 Build: 0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

XTMPSIZE.DAT default directory: VA3\$:\[XUUSER\]

XTMPSIZE.DAT Package Parameter file list in VA3\$:\[XUUSER\]:

----------------------------------------------------------

1\) XTMPSIZE.DAT;1

2\) XTMPSIZE_FORUM_11-17-16.DAT;1

3\) XTMPSIZE_FORUM_12-15-16_1017.DAT;1

4\) XTMPSIZE_FORUM_4-11-17_0939.DAT;1

5\) XTMPSIZE_FOR_HPS_REPORT_12-19-16.DAT;1

6\) XTMPSIZE_FOR_HPS_REPORT_4-11-17.DAT;1

7\) XTMPSIZE_GTS1-12-17_0949.DAT;1

8\) XTMPSIZE_GTS1-18-17_1500.DAT;1

\+ Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Next Screen//

The following actions are available on the “VistA Package Size Analysis Manager” screen:

- [EM—Extract Manager](#em_extract_manager) \[XTVS PKG MGR EXT MNGR ACTION\] (see Section <u>2.2.4</u>)
- [PMD—Display/Edit Package Parameters](#pmd_display_edit_package_parameters) \[XTVS PKG MGR PARAM DISP/EDIT ACTION\] (see Section <u>2.2.8</u>)
- [VSR—Display VistA Size Report](#vsr_display_vista_size_report) \[XTVS PKG MGR VISTA SIZE RPT\] (see Section <u>2.2.13</u> and <u>2.2.13.2</u>)
- [RVQ—Remote VistA Size Query](#rvq_remote_Vista_size_query) \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] (see Section <u>2.2.14</u>)
- [DPF—Delete Package Parameter File](#dpf_delete_package_parameter_file) \[XTVS PKG MGR PARAM FILE DELETE ACTION\] (see Section <u>2.2.3.1</u>)
- [CHD—Change Host Directory](#chd_change_host_directory) \[XTVS SITE PARAMETERS\] (see Section <u>2.2.15</u>)
- [UNL—Unlock Parameter File](#unl_unlock_parameter_file) \[XTVS PKG MGR PARAM UNLOCK ACTION\] (see Section <u>2.2.16</u>)

#### DPF—Delete Package Parameter File

On the “VistA Package Size Analysis Manager” screen, use the DPF—Delete Package Parameter File \[XTVS PKG MGR PARAM FILE DELETE ACTION\] action to delete from the system a selected Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) listed, as shown in <u>Figure 23</u>.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/039.png) NOTE: The DPF—Delete Package Parameter File \[XTVS PKG MGR PARAM FILE DELETE ACTION\] action is locked with the XTVS EDITOR security key.

<span id="_Ref482697255" class="anchor"></span>Figure 23: DPF—Delete Package Parameter File Action: Example

<u>Vista Package Size Manager Apr 14, 2017@14:07:04 Page: 1 of 4</u>

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 1 Build: 0

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

XTMPSIZE.DAT default directory: VA3\$:\[XUUSER\]

XTMPSIZE.DAT Package Parameter file list in VA3\$:\[XUUSER\]:

----------------------------------------------------------

1\) XTMPSIZE.DAT;1

2\) XTMPSIZE_FORUM_11-17-16.DAT;1

3\) XTMPSIZE_FORUM_12-15-16_1017.DAT;1

4\) XTMPSIZE_FORUM_4-11-17_0939.DAT;1

5\) XTMPSIZE_FOR_HPS_REPORT_12-19-16.DAT;1

6\) XTMPSIZE_FOR_HPS_REPORT_4-11-17.DAT;1

7\) XTMPSIZE_GTS1-12-17_0949.DAT;1

8\) XTMPSIZE_GTS1-18-17_1500.DAT;1

9\) XTMPSIZE_GTS1-30-17_1235.DAT;1

10\) XTMPSIZE_GTS10-11-16_1204.DAT;1

11\) XTMPSIZE_GTS10-11-16_1208.DAT;1

12\) XTMPSIZE_GTS10-28-16_1537.DAT;1

13\) XTMPSIZE_GTS10-31-16_1535.DAT;1

14\) XTMPSIZE_GTS11-17-16_1332.DAT;1

15\) XTMPSIZE_GTS12-13-16_1102.DAT;1

16\) XTMPSIZE_GTS12-15-16_1130.DAT;1

17\) XTMPSIZE_GTS12-15-16_1348.DAT;1

18\) XTMPSIZE_GTS12-16-16_0940.DAT;1

19\) XTMPSIZE_GTS12-19-16_1005.DAT;1

20\) XTMPSIZE_GTS2-10-17_1021.DAT;1

21\) XTMPSIZE_GTS2-10-17_1347.DAT;1

22\) XTMPSIZE_GTS2-9-17_1627.DAT;1

23\) XTMPSIZE_GTS3-6-17_0922.DAT;1

24\) XTMPSIZE_GTS4-10-17_0839.DAT;1

<span class="mark">25) XTMPSIZE_GTS4-14-17_1336.DAT;1</span>

26\) XTMPSIZE_GTS4-14-17_1400.DAT;1

27\) XTMPSIZE_GTS7-26-16_1054.DAT;1

28\) XTMPSIZE_GTS7-26-16_1119.DAT;1

29\) XTMPSIZE_GTS7-26-16_1527.DAT;1

30\) XTMPSIZE_GTS7-26-16_1531.DAT;1

31\) XTMPSIZE_GTS7-27-16_1016.DAT;1

32\) XTMPSIZE_GTS8-11-16_0838.DAT;1

33\) XTMPSIZE_GTS8-18-16_1014.DAT;1

34\) XTMPSIZE_GTS8-3-16_1545.DAT;1

\+ Enter ?? : more actions and Help, : ??? : Process Help

EM Extract Manager <span class="mark">DPF Delete Package Parameter File</span>

PMD Display/Edit Package Parameters CHD Change Host Directory

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Next Screen// <span class="mark">DPF \<Enter\></span> Delete Package Parameter File

Select the XTMPSIZE\*.DAT Package Parameter file item number: <span class="mark">25</span>

Do you want to PERMANENTLY DELETE XTMPSIZE_GTS4-14-17_1336.DAT;1? NO// <span class="mark">YES</span>

### Extract Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a *new* Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) with the data in the unloaded ^XTMP(“XTSIZE”) global, do the following:

1.  From the “VistA Package Size Analysis Manager” screen, select the EM—Extract Manager \[XTVS PKG MGR EXT MNGR ACTION\] action, as shown in <u>Figure 24</u>.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/040.png) NOTE: The EM—Extract Manager \[XTVS PKG MGR EXT MNGR ACTION\] action is locked with the XTVS EDITOR security key.

> <span id="_Ref482280790" class="anchor"></span>Figure 24: EM—Extract Manager Action: Example

<u>Vista Package Size Manager Apr 14, 2017@13:59:46 Page: 1 of 4</u>

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 1 Build: 0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

XTMPSIZE.DAT default directory: VA3\$:\[XUUSER\]

XTMPSIZE.DAT Package Parameter file list in VA3\$:\[XUUSER\]:

----------------------------------------------------------

1\) XTMPSIZE.DAT;1

2\) XTMPSIZE_FORUM_11-17-16.DAT;1

3\) XTMPSIZE_FORUM_12-15-16_1017.DAT;1

4\) XTMPSIZE_FORUM_4-11-17_0939.DAT;1

5\) XTMPSIZE_FOR_HPS_REPORT_12-19-16.DAT;1

6\) XTMPSIZE_FOR_HPS_REPORT_4-11-17.DAT;1

7\) XTMPSIZE_GTS1-12-17_0949.DAT;1

8\) XTMPSIZE_GTS1-18-17_1500.DAT;1

\+ Enter ?? : more actions & Help, ??? : Process Help

<span class="mark">EM Extract Manager</span> DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Next Screen// <span class="mark">EM \<Enter\></span> Extract Manager

44. The “VistA Package Size Analysis Manager – Extract Manager” screen displays, as shown in <u>Figure 25</u>:

> <span id="_Ref467071924" class="anchor"></span>Figure 25: “VistA Package Size Analysis Manager – Extract Manager” Screen—ListMan Screen

<u>Package Extract Manager Apr 14, 2017@13:59:51 Page: 1 of 1</u>

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 1 Build: 0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Extracted package ^XTMP global list

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

Process ID System Date/Time

----------------------------------------------------

543597941 FOR Apr 06, 2017

Enter ?? for more actions and Help

CE Extract Package Data DEL Delete Extract

ED Display Extract CXP Convert Extract to Parameter List

ME Email Extract Global REQ Remote VistA Extract Query

Select Action:Quit//

The following actions are available on the “VistA Package Size Analysis Manager – Extract Manager” screen:

- [CE—Extract Package Data](#ce_extract_package_data) \[XTVS PKG EXTRACT CREATE ACTION\] (see Section <u>2.2.4.1</u>)
- [ED—Display Extract](#ed_display_extract) \[XTVS PKG MGR EXT DISP ACTION\] (see Section <u>2.2.4.2</u>)
- [ME—Email Extract Global](#me_e_mail_extract_global) \[XTVS PKG EXT EMAIL ACTION\] (see Section <u>2.2.4.3</u>)
- [DEL—Delete Extract](#del_delete_extract) \[XTVS PKG EXTRACT DEL ACTION\] (see Section <u>2.2.4.4</u>)
- [CXP—Convert Extract to Parameter List](#cpf_create_parameter_file_from_extract) \[XTVS PKG EXT CRT PARAM ACTION\] (see Section <u>2.2.5</u>)
- [REQ—Remote VistA Extract Query](#req_remote_vista_extract_query) \[XTVS PKG EXT QUERY REMOTE ACTION\] (see Section <u>2.2.1.2</u>)

#### CE—Extract Package Data

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/041.png) NOTE: The names of packages should *not* contain double quotation marks. If a PACKAGE (#9.4) file extract includes a package name that contains double quotation marks (“), the tool *cannot* parse the name of the Package. Double quotation marks (“) need to be “cleaned up” from package names before the extract is completed.

On the “VistA Package Size Analysis Manager - Extract Manager” screen, use the CE—Extract Package Data \[XTVS PKG EXTRACT CREATE ACTION\] action to extract PACKAGE (#9.4) file data into ^XTMP(“XTVS”) global, as shown in <u>Figure 26</u> and <u>Figure 27</u>:

<span id="_Ref484587160" class="anchor"></span>Figure 26: CE—Extract Package Data Action—Example: File Does Not Already Exist (1 of 2)

<u>Package Extract Manager Jun 02, 2017@09:29:45 Page: 1 of 1</u>

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 1 Build: 25

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

Extracted package ^XTMP global list

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

Process ID System Date/Time

----------------------------------------------------

3128 PLA Apr 07, 2017 7:52:57 am

Enter ?? for more actions and Help

<span class="mark">CE Extract Package Data</span> DEL Delete Extract

ED Display Extract CXP Convert Extract to Parameter List

ME Email Extract Global REQ Remote VistA Extract Query

Select Action:Quit// <span class="mark">CE \<Enter\></span> Extract Package Data

<span id="_Ref484587170" class="anchor"></span>Figure 27: CE—Extract Package Data Action—Example: File Does Not Already Exist (2 of 2)

<u>Package Extract Manager Jun 02, 2017@09:29:51 Page: 1 of 1</u>

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 1 Build: 25

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

Extracted package ^XTMP global list

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

Process ID System Date/Time

----------------------------------------------------

3128 PLA Apr 07, 2017 7:52:57 am

<span class="mark">12756 PLA Jun 02, 2017 9:29:50 am</span>

Enter ?? for more actions and Help

CE Extract Package Data DEL Delete Extract

ED Display Extract CXP Convert Extract to Parameter List

ME Email Extract Global REQ Remote VistA Extract Query

Select Action:Quit//

If the file already exists, you will see the following system response after selecting the CE—Extract Package Data \[XTVS PKG EXTRACT CREATE ACTION\] action, as shown in <u>Figure 28</u>:

<span id="_Ref482693377" class="anchor"></span>Figure 28: CE—Extract Package Data Action—Example: File Already Exists

<u>Package Extract Manager Apr 14, 2017@14:03:39 Page: 1 of 1</u>

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 1 Build: 0

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

Extracted package ^XTMP global list

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

Process ID System Date/Time

----------------------------------------------------

543209920 *SITE1PRO* Apr 14, 2017 1:59:54 pm

543597941 FOR Apr 06, 2017

Enter ?? for more actions and Help

<span class="mark">CE Extract Package Data</span> DEL Delete Extract

ED Display Extract CXP Convert Extract to Parameter List

ME Email Extract Global REQ Remote VistA Extract Query

Select Action:Quit// <span class="mark">CE \<Enter\></span> Extract Package Data

^XTMP("XTSIZE",543209920) already exists!

Do you want to delete ^XTMP("XTSIZE",543209920) and recreate it? NO// <span class="mark">YES</span>

If any of package names in the extract contain a double quote (“), the following occurs:

1.  Double quote is converted to two single quotes to allow string parsing through the name.
3.  User receives a VA MailMan message, as shown in <u>Figure 29</u>:

> <span id="_Ref53653971" class="anchor"></span>Figure 29: Sample VA MailMan Message—Double Quote Edits

Subj: PACKAGE EXTRACT (*SITE1PRO*) ; data cleanup! \[#160427\] 10/08/20@13:36

3 lines

From: POSTMASTER In 'IN' basket. Page 1

----------------------------------------------------------------------------

Notice for Package Extract on *SITE1PRO*.

Data was cleaned up on ABC 4'' LABEL extract.

<span class="mark">Double Quotes changed to 2 single quotes in the ABC 4'' LABEL Package name.</span>

Enter message action (in IN basket): Ignore//

#### ED—Display Extract

On the “VistA Package Size Analysis Manager - Extract Manager” screen, use the ED—Display Extract \[XTVS PKG MGR EXT DISP ACTION\] action to enter the \$J Process number for the ^XTMP(“XTVS”) global and display its data, as shown in <u>Figure 30</u>:

<span id="_Ref482694265" class="anchor"></span>Figure 30: ED—Display Extract Action: Example

<u>Package Extract Manager Apr 14, 2017@14:03:55 Page: 1 of 1</u>

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 1 Build: 0

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

Extracted package ^XTMP global list

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

Process ID System Date/Time

----------------------------------------------------

543209920 *SITE1PRO* Apr 14, 2017 2:03:55 pm

543597941 FOR Apr 06, 2017

Enter ?? for more actions and Help

CE Extract Package Data DEL Delete Extract

<span class="mark">ED Display Extract</span> CXP Convert Extract to Parameter List

ME Email Extract Global REQ Remote VistA Extract Query

Select Action:Quit// <span class="mark">ED \<Enter\></span> Display Extract

Enter the Extract Process ID (\$JOB) number: <span class="mark">543209920</span>

This opens the “VistA Package Size Analysis Manager - Display Extract” screen and presents a report of each package with captioned parameter data, as shown in <u>Figure 31</u>. Use this report to review the extracted PACKAGE (#9.4) file data to determine what parameter changes and corrections need to be made.

The “VistA Package Size Analysis Manager - Display Extract” screen has the following action:

[DE—Delete Displayed Extract](#de_delete_displayed_extract) \[XTVS PKG EXT DISP DEL ACTION\] (see Section <u>2.2.4.2.1</u>)

#### DE—Delete Displayed Extract

On the “VistA Package Size Analysis Manager - Display Extract” screen, use the DE—Delete Displayed Extract \[XTVS PKG EXT DISP DEL ACTION\] action to delete the ^XTMP(“XTVS”) global extract displayed, as shown in <u>Figure 31</u>:

<span id="_Ref482631138" class="anchor"></span>Figure 31: DE—Delete Displayed Extract Action: Example

<u>Package File Extract Display Apr 14, 2017@14:04:30 Page: 1 of 100</u>

<span class="mark">VistA Package Size Analysis Manager - Display Extract</span>

Version: 1 Build: 0

System: *SITE1PRO* PID:543209920 Date: Apr 14, 2017 2:03:55 pm

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

Package data in ^XTMP extract

ACCOUNTS RECEIVABLE

Prefix: PRCA

\*Low File#: \*High File#:

File List:

Added Prefixes: PRY\|RC\|

Excluded Prefixes:

File Ranges:

Parent Package:

ADP MODULE

\+ Enter ?? for more actions and Help

<span class="mark">DE Delete Displayed Extract</span>

Select Action:Next Screen// <span class="mark">DE \<Enter\></span> Delete Displayed Extract

Do you want to delete ^XTMP("XTSIZE",543209920)? NO// <span class="mark">YES</span>

#### ME—Email Extract Global

On the “VistA Package Size Analysis Manager - Extract Manager” screen, use the ME—Email Extract Global \[XTVS PKG EXT EMAIL ACTION\] action to enter the \$JOB Process ID number of the extract to mail and the recipients to receive it, as shown in <u>Figure 32</u>.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/042.png) NOTE: This serves as an alternate to the Send Package File Extract via Packman \[XTVS PKG MGR EXT PACKAGE MSG\] option (see Section <u>2.2.1</u>).

<span id="_Ref482692608" class="anchor"></span>Figure 32: ME—Email Extract Global Action: Example

<u>Package Extract Manager Apr 14, 2017@14:04:59 Page: 1 of 1</u>

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 1 Build: 0

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

Extracted package ^XTMP global list

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

Process ID System Date/Time

----------------------------------------------------

543597941 FOR Apr 06, 2017

Enter ?? for more actions and Help

CE Extract Package Data DEL Delete Extract

ED Display Extract CXP Convert Extract to Parameter List

<span class="mark">ME Email Extract Global</span> REQ Remote VistA Extract Query

Select Action:Quit// <span class="mark">ME \<Enter\></span> Email Extract Global

The message can take some time to be sent.

Enter the Extract Process ID (\$JOB) number: <span class="mark">543597941</span>

Send mail to: XUUSER,ONE// <span class="mark">\<Enter\></span> XUUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

Created by XUUSER,ONE at REDACTED.VA.GOV on Friday, 04/14/17

at 14:05.........................................

^XTMP("XTSIZE",543597941) Emailed via PackMan. \[MSG \#:78619\]

Press Return to continue:

#### DEL—Delete Extract

On the “VistA Package Size Analysis Manager - Extract Manager” screen, use the DEL—Delete Extract \[XTVS PKG EXTRACT DEL ACTION\] action to enter the \$JOB Process ID number of the ^XTMP(“XTSIZE”) global extract to be deleted, as shown in <u>Figure 33</u>:

<span id="_Ref482693549" class="anchor"></span>Figure 33: DEL—Delete Extract Action: Example

<u>Package Extract Manager Apr 14, 2017@14:06:14 Page: 1 of 1</u>

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 1 Build: 0

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

Extracted package ^XTMP global list

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

Process ID System Date/Time

----------------------------------------------------

<span class="mark">543597941</span> FOR Apr 06, 2017

Enter ?? for more actions and Help

CE Extract Package Data <span class="mark">DEL Delete Extract</span>

ED Display Extract CXP Convert Extract to Parameter List

ME Email Extract Global REQ Remote VistA Extract Query

Select Action:Quit// <span class="mark">DEL \<Enter\></span> Delete Extract

Enter the Extract Process ID (\$JOB) number: <span class="mark">543597941</span>

Do you want to delete ^XTMP("XTSIZE",543597941)? NO// <span class="mark">YES</span>

### Convert Extract to Parameter List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a *new* Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) from the data in a ^XTMP(“XTSIZE”) global, do the following:

1.  From the “VistA Package Size Analysis Manager – Extract Manager” screen, select the CXP—Convert Extract to Parameter List \[XTVS PKG EXT CRT PARAM ACTION\] action, as shown in <u>Figure 34</u>.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/043.png) NOTE: The CXP—Convert Extract to Parameter List \[XTVS PKG EXT CRT PARAM ACTION\] action is locked with the XTVS EDITOR security key.

45. At the “Enter the Extract Process ID (\$JOB) number:” prompt, enter the \$JOB Process ID of the extract, as shown in <u>Figure 34</u>.

> <span id="_Ref467071832" class="anchor"></span>Figure 34: CXP—Convert Extract to Parameter List Action: Example

<u><span class="mark">Package Extract Manager</span> Apr 14, 2017@13:59:55 Page: 1 of 1</u>

<span class="mark">VistA Package Size Analysis Manager - Extract Manager</span>

Version: 1 Build: 0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Extracted package ^XTMP global list

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

Process ID System Date/Time

----------------------------------------------------

543209920 *SITE1PRO* Apr 14, 2017 1:59:54 pm

543597941 FOR Apr 06, 2017

Enter ?? for more actions and Help

CE Extract Package Data DEL Delete Extract

ED Display Extract <span class="mark">CXP Convert Extract to Parameter List</span>

ME Email Extract Global REQ Remote VistA Extract Query

Select Action:Quit// <span class="mark">CXP \<Enter\></span> Convert Extract to Parameter List

Enter the Extract Process ID (\$JOB) number: <span class="mark">999999999</span>

46. The “VistA Package Size Analysis Manager – Package Parameters” screen displays (see <u>Figure 35</u>). This interface allows users to review the Package Parameters defined from the PACKAGE (#9.4) file extract.

> <span id="_Ref467077123" class="anchor"></span>Figure 35: “VistA Package Size Analysis Manager – Package Parameters” Screen—ListMan Screen and Report

<u>Parameter File List Apr 14, 2017@14:00:27 Page: 1 of 45</u>

<span class="mark">VistA Package Size Analysis Manager - Package Parameters</span>

Version: 1 Build: 0

System: FOR Extract PID:543597941 Date: Apr 06, 2017

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ACCOUNTS RECEIVABLE^PRCA^412^439^PRY\|RC\|^^412\|430\|431\|432\|433\|434\|435\|436\|437\|43

8\|439\|^412-439.9999\|^

AR (ACCOUNTS RECEIVABLE)^RC^330^349^^^330\|331\|332\|333\|334\|335\|336\|337\|338\|339\|34

0\|341\|342\|343\|344\|345\|346\|347\|348\|349\|^330-349.9999\|^ACCOUNTS RECEIVABLE

MCCR NATIONAL DATABASE^PRQ^465^469^^PRQS\|^465\|466\|467\|468\|469\|^465-469.9999\|^ADMINISTRATIVE MODULES

ADVERSE REACTION TRACK (GMA)^GMA^^^^^^^

ADVERSE REACTION TRACKING^GMRA^120^120^GMA\|^^120\|^120-120.9999\|^ADVERSE REACTION TRACK (GMA)

\+ Enter ?? : more actions & Help, ??? : Process Help

RPL Display Parameter List WPF Write Parameter List to File

DPC Display Parameter Corrections EPC Email Corrections Rpt & Parameters

Select Action:Next Screen//

The following actions are available on the “VistA Package Size Analysis Manager – Package Parameters” or “VistA Package Size Analysis Manager – Package Parameter Corrections” screens:

- [RPL—Display Parameter List](#rpl_display_parameter_list) \[XTVS PKG EXT REDISP PARAM ACTION\] (see Section <u>2.2.5.1</u>)
- [DPC—Display Parameter Corrections](#dpc_display_parameter_corrections) \[XTVS PKG EXT DISP CORRECTIONS ACTION\] (see Section <u>2.2.5.2</u>)
- [WPF—Write Parameter List to File](#wpf_write_parameter_list_to_file) \[XTVS PKG EXT PARAM WRT ACTION\] (see Section <u>2.2.6</u>)
- [EPC—Email Corrections Rpt & Parameters](#epc_email_corrections_rpt_and_parameters) \[XTVS PKG MGR NEW PARAM MAIL ACTION\] (see Section <u>2.2.5.3</u>)

These actions allow users to review the parameters that would be created from the selected Package Extract and write that extract to a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)).

> <span id="_Ref482344432" class="anchor"></span>Figure 36: “VistA Package Size Analysis Manager - Package Parameter Corrections” Screen—ListMan Screen and Report

Parameter File List Apr 14, 2017@14:01:32 Page: 1 of 74

<span class="mark">VistA Package Size Analysis Manager - Package Parameter Corrections</span>

Version: 1 Build: 0

System: FOR Extract PID:543597941 Date: Apr 06, 2017

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ACCOUNTS RECEIVABLE Package entry file number notes:

412-439.9999 \[Decimal on Range End extended by nine(s)\]

ADVERSE REACTION TRACK (GMA) Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

ADVERSE REACTION TRACKING Package entry file number notes:

120-120.9999 \[Decimal on Range End extended by nine(s)\]

AIRBORNE HAZARD & OPEN BURN PIT REGISTRY Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

\+ Enter ?? : more actions & Help, ??? : Process Help

RPL Display Parameter List WPF Write Parameter List to File

DPC Display Parameter Corrections EPC Email Corrections Rpt & Parameters

Select Action:Next Screen//

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/044.png) NOTE: The screen header displays either of the following utilities:

- VistA Package Size Analysis Manager - Package Parameters
- VistA Package Size Analysis Manager - Package Parameter Corrections

The [RPL—Display Parameter List](#rpl_display_parameter_list) \[XTVS PKG EXT REDISP PARAM ACTION\] (see Section <u>2.2.5.1</u>) and [DPC—Display Parameter Corrections](#dpc_display_parameter_corrections) \[XTVS PKG EXT DISP CORRECTIONS ACTION\] (see Section <u>2.2.5.2</u>) actions are a toggle between what header is displayed.

#### RPL—Display Parameter List

On the “VistA Package Size Analysis Manager - Package Parameters” or “VistA Package Size Analysis Manager - Package Parameter Corrections” screens, use the RPL—Display Parameter List \[XTVS PKG EXT REDISP PARAM ACTION\] action (see <u>Figure 37</u>) after users review corrections with the [DPC—Display Parameter Corrections](#dpc_display_parameter_corrections) \[XTVS PKG EXT DISP CORRECTIONS ACTION\] action (see Section <u>2.2.5.2</u>). It redisplays the package parameters as defined by the selected package extract file.

<span id="_Ref482693003" class="anchor"></span>Figure 37: RPL—Display Parameter List Action: Example

<u>Parameter File List Apr 14, 2017@14:01:32 Page: 1 of 74</u>

<span class="mark">VistA Package Size Analysis Manager - Package Parameter Corrections</span>

Version: 1 Build: 0

System: FOR Extract PID:543597941 Date: Apr 06, 2017

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

ACCOUNTS RECEIVABLE Package entry file number notes:

412-439.9999 \[Decimal on Range End extended by nine(s)\]

ADVERSE REACTION TRACK (GMA) Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

ADVERSE REACTION TRACKING Package entry file number notes:

120-120.9999 \[Decimal on Range End extended by nine(s)\]

AIRBORNE HAZARD & OPEN BURN PIT REGISTRY Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

\+ Enter ?? : more actions & Help, ??? : Process Help

<span class="mark">RPL Display Parameter List</span> WPF Write Parameter List to File

DPC Display Parameter Corrections EPC Email Corrections Rpt & Parameters

Select Action:Next Screen// <span class="mark">RPL \<Enter\></span> Display Parameter List

The RPL—Display Parameter List \[XTVS PKG EXT REDISP PARAM ACTION\] action displays the “VistA Package Size Analysis Manager - Package Parameters” screen and report.

#### DPC—Display Parameter Corrections

On the “VistA Package Size Analysis Manager - Package Parameters” or “VistA Package Size Analysis Manager - Package Parameter Corrections” screens, use the DPC—Display Parameter Corrections \[XTVS PKG EXT DISP CORRECTIONS ACTION\] action to review the changes that the [CXP—Convert Extract to Parameter List](#cpf_create_parameter_file_from_extract) \[XTVS PKG EXT CRT PARAM ACTION\] action made to the data written in the Package Parameters list when it was created from the raw PACKAGE (#9.4) file extract, as shown in <u>Figure 38</u>.

Creation of Package Parameters from the PACKAGE (#9.4) file extract extends file range numbers out to four (4) decimal places (nines). For example, 1.5 becomes 1.5999. It also reports omissions and data integrity problems in the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)).

<span id="_Ref482692262" class="anchor"></span>Figure 38: DPC—Display Parameter Corrections Action: Example

<u>Parameter File List Apr 14, 2017@14:00:27 Page: 1 of 45</u>

<span class="mark">VistA Package Size Analysis Manager - Package Parameters</span>

Version: 1 Build: 0

System: FOR Extract PID:543597941 Date: Apr 06, 2017

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

ACCOUNTS RECEIVABLE^PRCA^412^439^PRY\|RC\|^^412\|430\|431\|432\|433\|434\|435\|436\|437\|43

8\|439\|^412-439.9999\|^

AR (ACCOUNTS RECEIVABLE)^RC^330^349^^^330\|331\|332\|333\|334\|335\|336\|337\|338\|339\|34

0\|341\|342\|343\|344\|345\|346\|347\|348\|349\|^330-349.9999\|^ACCOUNTS RECEIVABLE

MCCR NATIONAL DATABASE^PRQ^465^469^^PRQS\|^465\|466\|467\|468\|469\|^465-469.9999\|^ADM

INISTRATIVE MODULES

ADVERSE REACTION TRACK (GMA)^GMA^^^^^^^

ADVERSE REACTION TRACKING^GMRA^120^120^GMA\|^^120\|^120-120.9999\|^ADVERSE REACTION

TRACK (GMA)

\+ Enter ?? : more actions & Help, ??? : Process Help

RPL Display Parameter List WPF Write Parameter List to File

<span class="mark">DPC Display Parameter Corrections</span> EPC Email Corrections Rpt & Parameters

Select Action:Next Screen// <span class="mark">DPC \<Enter\></span> Display Parameter Corrections

The DPC—Display Parameter Corrections \[XTVS PKG EXT DISP CORRECTIONS ACTION\] action displays the “VistA Package Size Analysis Manager - Package Parameter Corrections” screen and report, as shown in <u>Figure 36</u>.

#### EPC—Email Corrections Rpt & Parameters

On the “VistA Package Size Analysis Manager - Package Parameters” or “VistA Package Size Analysis Manager - Package Parameter Corrections” screens, use the EPC—Email Corrections Rpt & Parameters \[XTVS PKG MGR NEW PARAM MAIL ACTION\] action to enter email recipients and send the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) optionally in an attachment file or in text with the corrections report in a mail message. Use this information as a starting point for correcting package information in the Parameters file.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/045.png) NOTE: You can forward a message with an attachment file to a MailMan recipient. They will be able to read the Corrections report; however, the Package Parameter file (i.e., XTMPSIZE\*.DAT) attachment will be encoded as an attachment. There are no MailMan tools available to the end-user to extract attachments. Thus, the message needs to be forwarded to a Microsoft<sup>®</sup> Outlook recipient, so the attachment can also be read. You have the option of creating the message with the Package Parameter file as text along with the Corrections report. This message form will allow a MailMan recipient to read the Package Parameter file text in MailMan.

<span id="_Ref1125732" class="anchor"></span>Figure 39: EPC—Email Corrections Rpt & Parameters Action: Attachment Example

<u>Parameter File List Apr 14, 2017@14:01 Page: 1 of 74</u>

<span class="mark">VistA Package Size Analysis Manager - Package Parameter Corrections</span>

Version: 1 Build: 0

System: FOR Extract PID:543597941 Date: Apr 06, 2017

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

ACCOUNTS RECEIVABLE Package entry file number notes:

412-439.9999 \[Decimal on Range End extended by nine(s)\]

ADVERSE REACTION TRACK (GMA) Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

ADVERSE REACTION TRACKING Package entry file number notes:

120-120.9999 \[Decimal on Range End extended by nine(s)\]

AIRBORNE HAZARD & OPEN BURN PIT REGISTRY Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

\+ Enter ?? : more actions & Help, ??? : Process Help

RPL Display Parameter List WPF Write Parameter List to File

DPC Display Parameter Corrections <span class="mark">EPC Email Corrections Rpt & Parameters</span>

Select Action:Next Screen// <span class="mark">EPC \<Enter\></span> Email Corrections Rpt & Parameters

The message can take some time to be sent.

Send mail to: XUUSER,ONE// <span class="mark">\<Enter\></span> XUUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">ONE.XUUSER@VA.GOV</span>

Looking in Internet Suffix file... US GOVERNMENT via REDACTED.VA.GOV

And Send to: <span class="mark">\<Enter\></span>

> **NOTE:** Attachments sent to VA MailMan addresses will be unreadable.

Send the parameters in the message if sending to a VA MailMan address.

Send the VistA Pkg Parameter File as a message or a text file attachment: A// <span class="mark">\<Enter\></span> ttachment

\[Creating attachments... /

<span id="_Ref59199121" class="anchor"></span>Figure 40: EPC—Email Corrections Rpt & Parameters Action: Message Example

<u>Parameter File List Apr 14, 2017@14:01 Page: 1 of 74</u>

<span class="mark">VistA Package Size Analysis Manager - Package Parameter Corrections</span>

Version: 1 Build: 0

System: FOR Extract PID:543597941 Date: Apr 06, 2017

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

ACCOUNTS RECEIVABLE Package entry file number notes:

412-439.9999 \[Decimal on Range End extended by nine(s)\]

ADVERSE REACTION TRACK (GMA) Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

ADVERSE REACTION TRACKING Package entry file number notes:

120-120.9999 \[Decimal on Range End extended by nine(s)\]

AIRBORNE HAZARD & OPEN BURN PIT REGISTRY Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

\+ Enter ?? : more actions & Help, ??? : Process Help

RPL Display Parameter List WPF Write Parameter List to File

DPC Display Parameter Corrections <span class="mark">EPC Email Corrections Rpt & Parameters</span>

Select Action:Next Screen// <span class="mark">EPC \<Enter\></span> Email Corrections Rpt & Parameters

The message can take some time to be sent.

Send mail to: XUUSER,ONE// <span class="mark">\<Enter\></span> XUUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">ONE.XUUSER@VA.GOV</span>

Looking in Internet Suffix file... US GOVERNMENT via REDACTED.VA.GOV

And Send to: <span class="mark">\<Enter\></span>

> **NOTE:** Attachments sent to VA MailMan addresses will be unreadable.

Send the parameters in the message if sending to a VA MailMan address.

Send the VistA Pkg Parameter File as a message or a text file attachment: A// <span class="mark">??</span>

Enter 'M' to send the report in a message or 'A' to send in a file

attached to a message.

Select one of the following:

<span class="mark">M Message</span>

A Attachment

Send the VistA Pkg Parameter File as a message or a text file attachment: A// <span class="mark">M</span> <span class="mark">\<Enter\></span> essage

\[Creating attachments... /

### Create Parameter File from Package File Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “VistA Package Size Analysis Manager – Package Parameter Corrections” and “VistA Package Size Analysis Manager – Package Parameters” screens display data integrity problems/corrections *or* the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) created from the PACKAGE (#9.4) file extract; respectively.

To create a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)), do the following:

1.  On the “VistA Package Size Analysis Manager - Package Parameters” or “VistA Package Size Analysis Manager - Package Parameter Corrections” screens, invoke the WPF—Write Parameter List to File \[XTVS PKG EXT PARAM WRT ACTION\] action, which creates the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)), as shown in <u>Figure 41</u>.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/046.png) NOTE: The WPF—Write Parameter List to File \[XTVS PKG EXT PARAM WRT ACTION\] action is locked with the XTVS EDITOR security key.

The Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) can be edited and used for package size reporting with other tool functions.

47. The system adds the indicated Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) to the VistA Package Size default directory for further editing with the VistA Package Analysis Manager.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/047.png) REF: For more information on setting the VistA Package Size default directory, see Section <u>2.2.15</u>, “<u>Change Host File Directory</u>.”

48. Once the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) is created, the user can review and edit the package parameters defined in the file by returning to the “VistA Package Size Analysis Manager” screen:
1.  Enter Quit on the “VistA Package Size Analysis Manager - Package Parameters” screen.
9.  Enter Quit again on the “VistA Package Size Analysis Manager - Extract Manager” screen.

> <span id="_Ref482344910" class="anchor"></span>Figure 41: WPF—Write Parameter List to File Action: Example

<u>Parameter File List Apr 14, 2017@14:00:38 Page: 1 of 74</u>

<span class="mark">VistA Package Size Analysis Manager - Package Parameter Corrections</span>

Version: 1 Build: 0

System: FOR Extract PID:543597941 Date: Apr 06, 2017

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ACCOUNTS RECEIVABLE Package entry file number notes:

412-439.9999 \[Decimal on Range End extended by nine(s)\]

ADVERSE REACTION TRACK (GMA) Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

ADVERSE REACTION TRACKING Package entry file number notes:

120-120.9999 \[Decimal on Range End extended by nine(s)\]

AIRBORNE HAZARD & OPEN BURN PIT REGISTRY Package entry file number notes:

No File List \[No File Multiple Entries defined\]

Ranges Undefined \[No File Ranges or High/Low Fields\]

\+ Enter ?? : more actions and Help, ??? : Process Help

RPL Display Parameter List <span class="mark">WPF Write Parameter List to File</span>

DPC Display Parameter Corrections EPC Email Corrections Rpt & Parameters

Select Action:Next Screen// <span class="mark">WPF \<Enter\></span> Write Parameter List to File

Parameter file: XTMPSIZE_GTS4-14-17_1400.DAT, will be created.

Press Return to continue: <span class="mark">\<Enter\></span>

### Return to VistA Package Size Analysis Manager & Review/Edit Parameter File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 42</u> shows the “VistA Package Size Analysis Manager – Parameter Display” screen display for the newly created (or updated) Package Parameter files (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)):

<span id="_Ref467077046" class="anchor"></span>Figure 42: “VistA Package Size Analysis Manager – Parameter Display” Screen—ListMan Screen

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/048.png)

In the example in <u>Figure 42</u>, the demonstration file is XTMPSIZE_QG_Demo.DAT (#6 in the list).

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/049.png) NOTE: From the operating system (OS), you can rename the new Package Parameter file (i.e., XTMPSIZE\*.DAT) to something that reflects this is the *new* FORUM Package Parameters extract file.

The following actions are available on the “VistA Package Size Analysis Manager” screen:

- [EM—Extract Manager](#em_extract_manager) \[XTVS PKG MGR EXT MNGR ACTION\] (see Section <u>2.2.4</u>)
- [PMD—Display/Edit Package Parameters](#pmd_display_edit_package_parameters) \[XTVS PKG MGR PARAM DISP/EDIT ACTION\] (see Section <u>2.2.8</u>)
- [VSR—Display VistA Size Report](#vsr_display_vista_size_report) \[XTVS PKG MGR VISTA SIZE RPT\] (see Section <u>2.2.13</u> and <u>2.2.13.2</u>)
- [RVQ—Remote VistA Size Query](#rvq_remote_Vista_size_query) \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] (see Section <u>2.2.14</u>)
- [DPF—Delete Package Parameter File](#dpf_delete_package_parameter_file) \[XTVS PKG MGR PARAM FILE DELETE ACTION\] (see Section <u>2.2.3.1</u>)
- [CHD—Change Host Directory](#chd_change_host_directory) \[XTVS SITE PARAMETERS\] (see Section <u>2.2.15</u>)
- [UNL—Unlock Parameter File](#unl_unlock_parameter_file) \[XTVS PKG MGR PARAM UNLOCK ACTION\] (see Section <u>2.2.16</u>)

### Display Package Parameter List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To review and edit the new Package Parameter file (e.g., XTMPSIZE_QG_Demo.DAT), do the following:

1.  From the “VistA Package Size Analysis Manager” screen, invoke the PMD—Display/Edit Package Parameters \[XTVS PKG MGR PARAM DISP/EDIT ACTION\] action.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/050.png) NOTE: The PMD—Display/Edit Package Parameters \[XTVS PKG MGR PARAM DISP/EDIT ACTION\] action is locked with the XTVS EDITOR security key.

49. At the “Select the XTMPSIZE\*.DAT Package Parameter file item number:” prompt, select the newly added XTMPSIZE\*.DAT file, as shown in <u>Figure 43</u>:

> <span id="_Ref481057089" class="anchor"></span>Figure 43: PMD—Display/Edit Package Parameters Action: Example

Vista Package Size Manager Apr 14, 2017@14:07:52 Page: 3 of 4

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 1 Build: 0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

23\) XTMPSIZE_GTS3-6-17_0922.DAT;1

24\) XTMPSIZE_GTS4-10-17_0839.DAT;1

25\) XTMPSIZE_GTS7-26-16_1054.DAT;1

26\) XTMPSIZE_GTS7-26-16_1119.DAT;1

27\) XTMPSIZE_GTS7-26-16_1527.DAT;1

28\) XTMPSIZE_GTS7-26-16_1531.DAT;1

29\) XTMPSIZE_GTS7-27-16_1016.DAT;1

30\) XTMPSIZE_GTS8-11-16_0838.DAT;1

31\) XTMPSIZE_GTS8-18-16_1014.DAT;1

32\) XTMPSIZE_GTS8-3-16_1545.DAT;1

33\) XTMPSIZE_GTS8-4-16_1321.DAT;1

34\) XTMPSIZE_GTS8-8-16_1532.DAT;1

<span class="mark">35) XTMPSIZE_QG_Demo.DAT;1</span>

\+ Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

<span class="mark">PMD Display/Edit Package Parameters</span> CHD Change Host Directory

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Next Screen// <span class="mark">PMD \<Enter\></span> Display/Edit Package Parameters

Select the XTMPSIZE\*.DAT Package Parameter file item number: <span class="mark">35</span>

50. This displays the “VistA Package Size Analysis Manager – Parameter Display” screen, as shown in <u>Figure 44</u>:

> <span id="_Ref467076960" class="anchor"></span>Figure 44: “VistA Package Size Analysis Manager – Parameter Display” Screen—ListMan Screen

> ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/051.png)

The “VistA Package Size Analysis Manager – Parameter Display” screen includes the following actions:

- [DO—Display Package Overlap List](#de_display_package_overlap_list) \[XTVS PKG MGR PARAM ERR DISP ACTION\] (see Section <u>2.2.9</u>)
- [DM—Display Parameter File Data Map](#dm_display_parameter_file_data_map) \[XTVS PKG MGR PARAM DATA MAP HELP ACTION\] (see Section <u>2.2.8.1</u>)
- [DC—Display Captioned Parameters](#dc_display_captioned_parameters) \[XTVS PKG MGR PARAM DISP CAPTION ACTION\] (see Section <u>2.2.10</u>)
- [CPF—Parameter File Comparison](#cpf_parameter_file_comparison) \[XTVS PKG MGR PARAM COMPARE ACTION\] (see Section <u>2.2.9</u>)

Use these actions to review the parameters defined from the extracted package data. This allows users to report potential problems with the parameters defined in the selected XTMPSIZE\*.DAT file.

#### DM—Display Parameter File Data Map

On the “VistA Package Size Analysis Manager - Parameter Display” screen, use the DM—Display Parameter File Data Map \[XTVS PKG MGR PARAM DATA MAP HELP ACTION\] action to display a data map of the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) list data, as shown in <u>Figure 45</u>:

<span id="_Ref482696549" class="anchor"></span>Figure 45: DM—Display Parameter File Data Map Action: Example

<u>Package Parameter Display Apr 14, 2017@14:14:30 Page: 1 of 45</u>

<span class="mark">VistA Package Size Analysis Manager - Parameter Display</span>

Version: 1 Build: 0

Default Directory: VA3\$:\[XUUSER\]

Parameter file: XTMPSIZE_OLD1.DAT;1

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

ACCOUNTS RECEIVABLE^PRCA^412^439^PRY\|RC\|^^412\|430\|431\|432\|433\|434\|435\|436\|437\|43

8\|439\|^412-439.9999\|^

AR (ACCOUNTS RECEIVABLE)^RC^330^349^^^330\|331\|332\|333\|334\|335\|336\|337\|338\|339\|34

0\|341\|342\|343\|344\|345\|346\|347\|348\|349\|^330-349.9999\|^ACCOUNTS RECEIVABLE

MCCR NATIONAL DATABASE^PRQ^465^469^^PRQS\|^465\|466\|467\|468\|469\|^465-469.9999\|^ADM

INISTRATIVE MODULES

ADP PLANNING^PRA^490^499^^^490\|491\|492\|493\|494\|495\|496\|497\|498\|499\|^490-499.9999

\|^

ADP PLANNING STATION^PRAS^^^^^^^ADP PLANNING

\+ Enter ?? for more actions and Help

DO Display Package Overlap List DC Display Captioned Parameters

<span class="mark">DM Display Parameter File Data Map</span> CPF Parameter File Comparison

Select Action:Next Screen// <span class="mark">DM \<Enter\></span> Display Parameter File Data Map

Parameter List data map from Package file:

------------------------------------------

^ pce 1 : Package Name

\[Source: NAME (#.01)\]

^ pce 2 : Primary Prefix

\[Source: PREFIX (#1)\]

^ pce 3 : \*Lowest File \#

\[Source: \*LOWEST FILE NUMBER (#10.6)\]

^ pce 4 : \*Highest File \#

\[Source: \*HIGHEST FILE NUMBER (#11)\]

^ pce 5 : Pipe character (\|) delimited list of Additional Prefixes

\[Source: ADDITIONAL PREFIXES multiple (#14)\]

^ pce 6 : Pipe character (\|) delimited list of Excepted Prefixes

\[Source: EXCLUDED NAME SPACE multiple (#919)\]

^ pce 7 : Pipe character (\|) delimited list of File entries

\[Source: FILE NUMBER multiple (#15001)\]

^ pce 8 : Pipe character (\|) delimited list of File Range entries

\[Source: LOW-HIGH RANGE multiple (#15001.1)\]

^ pce 9 : Parent Package

\[Source: PARENT PACKAGE field (#15003)\]

Press Return to continue:

### Analyze Package Parameter Data for Correctness

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several tools to assist users in analysis of the Package Parameter data files. Review of the Package Parameter data could begin with checking the list of packages with intersecting prefixes (namespaces) and file ranges.

To analyze the package parameter data for correctness, do the following:

1.  From the “VistA Package Size Analysis Manager – Parameter Display” screen, select the DO—Display Package Overlap List \[XTVS PKG MGR PARAM ERR DISP ACTION\] action, as shown in <u>Figure 46</u>:

> <span id="_Ref482355088" class="anchor"></span>Figure 46: DO—Display Package Overlap List Action: Example

Package Parameter Display Apr 14, 2017@14:09:40 Page: 1 of 45

<span class="mark">VistA Package Size Analysis Manager - Parameter Display</span>

Version: 1 Build: 24

Default Directory: C:\TEMP

Parameter file: XTMPSIZE_QG_Demo.DAT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ACCOUNTS RECEIVABLE^PRCA^412^439^PRY\|RC\|^^412\|430\|431\|432\|433\|434\|435\|436\|437\|438\|439\|^412-439.9999\|330-349.9999^

ADVERSE REACTION TRACKING^GMRA^120^120^GMA\|^^120\|^120-120.9999\|^ADVERSE REACTION TRACK (GMA)

ALERTS^XQAL^^^^^^^MENU DRIVER

ANTICOAGULATION MANAGEMENT^ORAM^^^^^^^ORDER ENTRY/RESULTS REPORTING

ASISTS^OOPS^2260^2264^^^2260\|2261\|2262\|2263\|2264\|^2260-2264.9999\|^GRAPHICS FOR KERNEL

AUT^AUT^^^^^^^

\+ Enter ?? for more actions and Help

<span class="mark">DO Display Package Overlap List</span> DC Display Captioned Parameters

DM Display Parameter File Data Map CPF Parameter File Comparison

Select Action:Next Screen// <span class="mark">DO \<Enter\></span> Display Package Overlap List

51. This displays the “VistA Package Size Analysis Manager – Prefix/File Overlap” screen, which supports review of package component overlap of the Package Parameter file: (e.g., XTMPSIZE_QG_Demo.DAT), as shown in <u>Figure 47</u>. Use the information provided to change package parameters, so they better reflect the package definitions.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/052.png) NOTE: The overlap report varies for different XTMPSIZE\*.DAT files.

> <span id="_Ref467076914" class="anchor"></span>Figure 47: “VistA Package Size Analysis Manager – Prefix/File Overlap” Screen—ListMan Screen and Report

> ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/053.png)

The “Prefix/File Overlap” report displays prefix (namespace) and file intersections common to multiple packages (e.g., Package A and Package B both reference File \#1000 and Prefix ABC). Use the information provided to change package parameters, so they better reflect the package definitions.

To report the components for a package, the VistA Package Size Reporting tool uses the XTMPSIZE\*.DAT file to determine which components belong to a package. If a file range or a prefix (namespace) belongs to multiple packages, those components are counted for both packages.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/054.png) NOTE: To create a report with better integrity, users with package knowledge should review the overlap report to determine if the package prefix and file intersections need to be removed.

The “VistA Package Size Analysis Manager – Prefix/File Overlap” screen includes the following actions:

- [PL—Display Prefix Overlap List](#pl_display_prefix_overlap_list) \[XTVS PKG MGR PREFIX OVERLAP ACTION\] (see Section <u>2.2.9.1</u>)
- [FL—Display File Overlap List](#fl_display_file_overlap_list) \[XTVS PKG MGR FILE OVERLAP ACTION\] (see Section <u>2.2.9.2</u>)
- [RL—\[Re\] Display Package Overlap List](#rl_re_display_package_overlap_list) \[XTVS PKG MGR PARAM OVRLP REDISP ACTION\] (see Section <u>2.2.9.3</u>)
- [EL—Email Displayed Report](#el_e_mail_displayed_report) \[XTVS PKG MGR EMAIL OVRLAP RPT ACTION\] (see <u>Figure 48</u>)

For example: Use the EL—Email Displayed Report \[XTVS PKG MGR EMAIL OVRLAP RPT ACTION\] action to send the overlap report to package SMEs for review, as shown in <u>Figure 48</u>:

<span id="_Ref481069245" class="anchor"></span>Figure 48: EL—Email Displayed Report Action: Example

Package Parameter Overlap Apr 14, 2017@14:10:54 Page: 1 of 79

<span class="mark">VistA Package Size Analysis Manager - Prefix/File Overlap</span>

Version: 1 Build: 0

Default Directory: C:\TEMP

Parameter file: XTMPSIZE_QG_Demo.DAT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

The Package Prefixes are overlapped by the subsequent package(s) listed.

The Packages Files overlapping the reported package are listed and identified by comparing assigned files for the reported package to the overlap package.

The VistA Size Report tool uses File assignments to count files in a package.

The Parameter File defines file assignments in 'File Ranges', '\*Lowest File#' to '\*Highest File#, and 'File Numbers' (List). Only one of these data elements is used to count files in a package and package file overlap as follows:

1\) File Ranges ; 2) \*Low/\*High file numbers ; 3) File Numbers (List)

The data element used is indicated in the File Overlap portion of this report

ACCOUNTS RECEIVABLE \[Primary Prefix: PRCA\]

Parent: None indicated

File Range: 412-439.9999, assignment intersects the following packages...

\+ Enter ?? for more actions and Help

PL Display Prefix Overlap List RL \[Re\] Display Package Overlap List

FL Display File Overlap List <span class="mark">EL Email Displayed Report</span>

Select Action:Next Screen// <span class="mark">EL \<Enter\></span> Email Displayed Report

The message can take some time to be sent.

Send mail to: XUUSER,ONE// <span class="mark">ONE.XUUSER@VA.GOV</span>

Looking in Internet Suffix file... US GOVERNMENT via REDACTED.VA.GOV

And Send to: <span class="mark">\<Enter\></span>

Prefix/File Overlap Emailed. \[MSG \#:78620\]

Press Return to continue:

The report can also be used with the DC—Display Captioned Parameters \[XTVS PKG MGR PARAM DISP CAPTION ACTION\] action on the “VistA Package Size Analysis Manager – Parameter Display” screen to change package definitions (see Section <u>2.2.10</u>).

52. Return to the “VistA Package Size Analysis Manager – Parameter Display” screen.
53. From the “VistA Package Size Analysis Manager – Parameter Display” screen, invoke the CPF—Parameter File Comparison \[XTVS PKG MGR PARAM COMPARE ACTION\] action, as shown in <u>Figure 49</u>:

> <span id="_Ref481066707" class="anchor"></span>Figure 49: CPF—Parameter File Comparison Action: Example

<u><span class="mark">Package Parameter Display</span> Apr 14, 2017@14:20:46 Page: 1 of 36</u>

<span class="mark">VistA Package Size Analysis Manager - Parameter Display</span>

Version: 1 Build: 24

Default Directory: C:\TEMP

Parameter file: XTMPSIZE_QG_Demo.DAT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ACCOUNTS RECEIVABLE^PRCA^412^439^PRY\|RC\|^^412\|430\|431\|432\|433\|434\|435\|436\|437\|438\|439\|^412-439.9999\|330-349.9999^

ADVERSE REACTION TRACKING^GMRA^120^120^GMA\|^^120\|^120-120.9999\|^ADVERSE REACTION TRACK (GMA)

ALERTS^XQAL^^^^^^^MENU DRIVER

ANTICOAGULATION MANAGEMENT^ORAM^^^^^^^ORDER ENTRY/RESULTS REPORTING

ASISTS^OOPS^2260^2264^^^2260\|2261\|2262\|2263\|2264\|^2260-2264.9999\|^GRAPHICS FOR KERNEL

AUT^AUT^^^^^^^

\+ Enter ?? for more actions and Help

DO Display Package Overlap List DC Display Captioned Parameters

DM Display Parameter File Data Map <span class="mark">CPF Parameter File Comparison</span>

Select Action:Next Screen// <span class="mark">CPF \<Enter\></span> Parameter File Comparison

1: XTMPSIZE.BAK;1

<span class="mark">2: XTMPSIZE.DAT;1</span>

3: XTMPSIZE_FORUM_11-17-16.BAK;1

4: XTMPSIZE_FORUM_11-17-16.DAT;1

5: XTMPSIZE_FORUM_12-15-16_1017.DAT;1

6: XTMPSIZE_FORUM_4-11-17_0939.DAT;1

7: XTMPSIZE_FOR_HPS_REPORT_12-19-16.DAT;1

8: XTMPSIZE_FOR_HPS_REPORT_4-11-17.DAT;1

9: XTMPSIZE_GTS1-12-17_0949.DAT;1

.

.

.

Enter RETURN to continue or '^' to exit: <span class="mark">^</span>

Select File: <span class="mark">2 \<Enter\></span> XTMPSIZE.DAT;1

1.  Ideally, select the most current Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) to compare to the current file. <u>Figure 50</u> displays the Package Parameter file (e.g., XTMPSIZE_QG_Demo.DAT).
2.  This displays the “VistA Package Size Analysis Manager - Parameter Compare” screen displaying the PACKAGE (#9.4) file changes that have occurred on FORUM since the last Package Extract occurred, as shown in <u>Figure 50</u>:

> <span id="_Ref470241085" class="anchor"></span>Figure 50: “VistA Package Size Analysis Manager - Parameter Compare” Screen—ListMan Screen and Report

> ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/055.png)

The “VistA Package Size Analysis Manager - Parameter Compare” screen includes the following action:

[ECR—Email Comparison Report](\l) \[XTVS PKG MGR PARAM COMPR MAIL ACTION\]—Use this action to send you and others an email copy of the comparison report (see Section <u>2.2.9.4</u>).

10. The “Parameter Compare” report (<u>Figure 50</u>) allows users to quickly identify the differences between the current Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) and a selected Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)).

Review the Changed, Added, and Deleted packages:

- Changed and Deleted Packages—You can confirm changed or deleted packages with the package developers; however, it is expected the edits or deletions were needed on FORUM and should continue in the updated Package Parameters XTMPFILE for Health Product Support. You can anticipate it will be necessary to apply these changes to the updated XTMPSIZE\*.DAT file.
- Added Packages—Determine if added packages are released and need to be reported with the VistA Package Size reporting tool. Since they have been added, it is expected a development effort was started on the packages since the last FORUM Package extract. Confirm with Health Product Support; however, it is expected that only released packages need to be added to the updated XTMPSIZE\*.DAT file.
54. After comparisons and appropriate action has been determined, exit from the “VistA Package Size Analysis Manager - Parameter Compare” screen, and exit the “VistA Package Size Analysis Manager - Parameter Display” interface. This returns you to the “VistA Package Size Analysis Manager” screen.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/056.png) NOTE: It is a good idea to retain the most recent Package Parameter files (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) for historical reference. The CPF—Parameter File Comparison \[XTVS PKG MGR PARAM COMPARE ACTION\] action can be used to compare Package Parameter files. Comparing the a new Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) (from FORUM) to an older Package Parameter file can show the changes applied to package parameters during a period of time.  
  
REF: To review the defined process, see the “<u>Update Existing Package Parameter File</u>” section.

#### PL—Display Prefix Overlap List

On the “VistA Package Size Analysis Manager - Prefix/File Overlap,” “VistA Package Size Analysis Manager - Prefix Overlap,” or “VistA Package Size Analysis Manager - File Overlap” screens, use the PL—Display Prefix Overlap List \[XTVS PKG MGR PREFIX OVERLAP ACTION\] action to sort out and display only the packages that have prefix (namespace) overlaps (intersections), as shown in <u>Figure 51</u>:

<span id="_Ref482698005" class="anchor"></span>Figure 51: PL—Display Prefix Overlap List Action: Example

<u>Package Parameter Overlap Apr 14, 2017@14:09:57 Page: 1 of 77</u>

<span class="mark">VistA Package Size Analysis Manager - Prefix/File Overlap</span>

Version: 1 Build: 0

Default Directory: VA3\$:\[XUUSER\]

Parameter file: XTMPSIZE_FORUM_4-11-17_0939.DAT;1

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

The Package Prefixes are overlapped by the subsequent package(s) listed.

The Packages Files overlapping the reported package are listed and identified

by comparing assigned files for the reported package to the overlap package.

The VistA Size Report tool uses File assignments to count files in a package.

The Parameter File defines file assignments in 'File Ranges', '\*Lowest File#'

to '\*Highest File#, and 'File Numbers' (List). Only one of these data elements

is used to count files in a package and package file overlap as follows:

1\) File Ranges ; 2) \*Low/\*High file numbers ; 3) File Numbers (List)

The data element used is indicated in the File Overlap portion of this report.

ACCOUNTS RECEIVABLE \[Primary Prefix: PRCA\]

Parent: None indicated

File Range: 412-439.9999, assignment intersects the following packages...

\+ Enter ?? for more actions and Help

<span class="mark">PL Display Prefix Overlap List</span> RL \[Re\] Display Package Overlap List

FL Display File Overlap List EL Email Displayed Report

Select Action:Next Screen// <span class="mark">PL \<Enter\></span> Display Prefix Overlap List

The system displays the “VistA Package Size Analysis Manager – Prefix Overlap” screen.

#### FL—Display File Overlap List

On the “VistA Package Size Analysis Manager – Prefix/File Overlap” or “VistA Package Size Analysis Manager - Prefix Overlap” screens, use the FL—Display File Overlap List \[XTVS PKG MGR FILE OVERLAP ACTION\] action to sort out and display only those packages that have file overlaps (intersections), as shown in <u>Figure 52</u>:

<span id="_Ref482694859" class="anchor"></span>Figure 52: FL—Display File Overlap List Action: Example

<u>Package Parameter Overlap     Dec 07, 2018@10:03:22          Page:    1 of   23</u>

           <span class="mark">VistA Package Size Analysis Manager - Prefix Overlap</span>

                         Version: 7.3     Build: 39

                 Default Directory: /srv/vista/*\<scd\>*/user/hfs/

                     Parameter file: XTMPSIZE_QG_Demo.DAT

                                                                                

<u>                                                                                </u>

The Package Prefixes are overlapped by the subsequent package(s) listed:       

                                                                                

                                                                                

 CAPACITY MANAGEMENT \[Primary Prefix: KMP\]                                     

   Parent: None indicated                                                       

   Prefix: KMP ; intersects the following packages...                          

        .  CAPACITY MANAGEMENT TOOLS \[KMPD\]                                    

        .  CAPACITY MANAGEMENT - RUM \[KMPR\]                                     

        .  SAGG PROJECT \[KMPS\]                                                 

                                                                                

                                                                                

 CLINICAL CASE REGISTRIES \[Primary Prefix: ROR\]                                

   Parent: None indicated                                                      

   Prefix: IMR ; intersects the following packages...                          

\+ Enter ?? for more actions and Help

PL Display Prefix Overlap List RL \[Re\] Display Package Overlap List

<span class="mark">FL Display File Overlap List</span> EL Email Displayed Report

Select Action:Next Screen// <span class="mark">FL \<Enter\></span> Display File Overlap List

The system displays the “VistA Package Size Analysis Manager – File Overlap” screen (see <u>Figure 53</u>).

#### RL—\[Re\] Display Package Overlap List

On the “VistA Package Size Analysis Manager - Prefix/File Overlap,” “VistA Package Size Analysis Manager - Prefix Overlap,” or “VistA Package Size Analysis Manager - File Overlap” screens, use the RL—\[Re\] Display Package Overlap List \[XTVS PKG MGR PARAM OVRLP REDISP ACTION\] action to display both prefix (namespace) and file overlaps for packages that intersect, as shown in <u>Figure 53</u>:

<span id="_Ref482694871" class="anchor"></span>Figure 53: RL—\[Re\] Display Package Overlap List Action: Example

<u>Package Parameter Overlap DEc 07, 2018@10:10:43 Page: 1 of 40</u>

<span class="mark">VistA Package Size Analysis Manager - File Overlap</span>

Version: 7.3 Build: 39

Default Directory: /srv/vista/*\<scd\>*/user/hfs/

Parameter file: XTMPSIZE_GG_Demo.DAT;1

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

The Packages Files overlapping the reported package are listed and identified

by comparing assigned files for the reported package to the overlap package.

File assignments are used by the VistA Size Report to count files in a package.

The Parameter File indicates file assignments by 'File Ranges', '\*Lowest File#'

to '\*Highest File#, and 'File Numbers' (List). Only one of these data elements

is used to count files in a package and package file overlap as follows:

1\) File Ranges ; 2) \*Low/\*High file numbers ; 3) File Numbers (List)

The data element used is indicated in the File Overlap portion of this report.

ACCOUNTS RECEIVABLE \[Primary Prefix: PRCA\]

Parent: None indicated

File Range: 412-439.9999, assignment intersects the following packages...

. IFCAP \[File Range: 410-449.9999\]

\+ Enter ?? for more actions and Help

PL Display Prefix Overlap List <span class="mark">RL \[Re\] Display Package Overlap List</span>

FL Display File Overlap List EL Email Displayed Report

Select Action:Next Screen// <span class="mark">RL \<Enter\></span> \[Re\] Display Package Overlap List

The system displays the “VistA Package Size Analysis Manager – Prefix/File Overlap” screen.

#### ECR—Email Comparison Report

On the “VistA Package Size Analysis Manager - Parameter Compare” screen, use the ECR—Email Comparison Report \[XTVS PKG MGR PARAM COMPR MAIL ACTION\] action to email a comparison report using VistA MailMan, as shown in <u>Figure 54</u>:

<span id="_Ref482691847" class="anchor"></span>Figure 54: ECR—Email Comparison Report Action: Example

<u>Package Parameter Compare Apr 14, 2017@14:22:56 Page: 1 of 75</u>

<span class="mark">VistA Package Size Analysis Manager - Parameter Compare</span>

Version: 1 Build: 0

Default Directory: VA3\$:\[XUUSER\]

Current \[New\] file: XTMPSIZE_GTS4-14-17_1418.DAT;1

Comparison \[Old\] file: XTMPSIZE_FOR_HPS_REPORT_4-11-17.DAT;1

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

CHANGED PACKAGES

Package: CAPACITY MANAGEMENT

New Low File \#: 8970 Old Low File \#: {none}

New High File \#: 8974 Old High File \#: {none}

Files

Added entire list in New file:

8970\|8971\|8972\|8973\|8974\|

File Ranges

Old List: 8969-8974.9999\|

8969-8974.9999 ...deleted in New file

8970-8974.9999 ...added in New file

\+ Enter ?? for more actions and Help

<span class="mark">ECR Email Comparison Report</span>

Select Action:Next Screen// <span class="mark">ECR \<Enter\></span> Email Comparison Report

The message can take some time to be sent.

Send mail to: XUUSER,ONE// <span class="mark">\<Enter\></span> XUUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

Parameter Compare Emailed. \[MSG \#:78621\]

Press Return to continue:

### Edit Package Parameter Data (As Needed)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) has been reviewed to determine what package intersections need correction and further package definition necessary, the user can make edits.

To edit Package Parameter file data, do the following:

1.  From the “VistA Package Size Analysis Manager – Parameter Display” screen, select the DC—Display Captioned Parameters \[XTVS PKG MGR PARAM DISP CAPTION ACTION\] action, as shown in <u>Figure 55</u>:

<span id="_Ref481069474" class="anchor"></span>Figure 55: DC—Display Captioned Parameters Action: Example

Package Parameter Display Apr 14, 2017@14:14:34 Page: 1 of 45

<span class="mark">VistA Package Size Analysis Manager - Parameter Display</span>

Version: 1 Build: 24

Default Directory: C:\TEMP

Parameter file: XTMPSIZE_QG_Demo.DAT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ACCOUNTS RECEIVABLE^PRCA^412^439^PRY\|RC\|^^412\|430\|431\|432\|433\|434\|435\|436\|437\|438\|439\|^412-439.9999\|330-349.9999^

ADVERSE REACTION TRACKING^GMRA^120^120^GMA\|^^120\|^120-120.9999\|^ADVERSE REACTION TRACK (GMA)

ALERTS^XQAL^^^^^^^MENU DRIVER

ANTICOAGULATION MANAGEMENT^ORAM^^^^^^^ORDER ENTRY/RESULTS REPORTING

ASISTS^OOPS^2260^2264^^^2260\|2261\|2262\|2263\|2264\|^2260-2264.9999\|^GRAPHICS FOR KERNEL

AUT^AUT^^^^^^^

\+ Enter ?? for more actions and Help

DO Display Package Overlap List <span class="mark">DC Display Captioned Parameters</span>

DM Display Parameter File Data Map CPF Parameter File Comparison

Select Action:Next Screen// <span class="mark">DC \<Enter\></span> Display Captioned Parameters

55. This opens the “VistA Package Size Analysis Manager – Captioned List” screen. It displays the list of packages (alphabetically) with captioned data elements, as shown in <u>Figure 56</u>. It also supports Package Parameter editing actions.

> <span id="_Ref467076716" class="anchor"></span>Figure 56: “VistA Package Size Analysis Manager – Captioned List” Screen—ListMan Screen

> ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/057.png)

The following actions are available on the “VistA Package Size Analysis Manager – Captioned List” screen:

- [EPP—Edit Package Parameters](#epp_edit_package_parameters) \[XTVS PKG MGR EDIT PACKAGE PARM ACTION\]—Use this action to apply any changes made to a Package definition on FORUM to the definition of the package in the (*new*) Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)). This includes adding any new packages created on FORUM, since the last extract, that need to be included in an updated VistA Package Size report (see Section <u>2.2.11.1</u>).
- [DPE—Delete Package Parameter Entry](#dpe_delete_package_parameter_entry) \[XTVS PKG MGR DEL PACKAGE PARM ACTION\]—Use this action to delete any “Added Package” identified as *not* part of the set of packages Health Product Support needs to size (see Section <u>2.2.11.2</u>).
- [SPP—Save Package Parameter Changes](#spp_save_package_parameter_changes) \[XTVS PKG MGR SAVE PACKAGE PARM ACTION\]—Use this action and save the file in a *new* name (see Section <u>2.2.12</u>).

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/058.png) NOTE: From the operating system (OS), you can rename the new Package Parameter file (i.e., XTMPSIZE\*.DAT) to something that reflects this is the Package Parameter file (i.e., XTMPSIZE\*.DAT) used to generate an updated VistA size report for Health Product Support (HPS).

These actions allow redefinition of packages and updating a Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) that can be used for creating the VistA Package Size Report.

### Edit Package Parameters Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “VistA Package Size Analysis Manager – Captioned List” screen includes the following actions (see <u>Figure 56</u>):

- [EPP—Edit Package Parameters](#epp_edit_package_parameters) \[XTVS PKG MGR EDIT PACKAGE PARM ACTION\] (see Section <u>2.2.11.1</u>)
- [DPE—Delete Package Parameter Entry](#dpe_delete_package_parameter_entry) \[XTVS PKG MGR DEL PACKAGE PARM ACTION\] (see Section <u>2.2.11.2</u>)
- [SPP—Save Package Parameter Changes](#spp_save_package_parameter_changes) \[XTVS PKG MGR SAVE PACKAGE PARM ACTION\] (see Section <u>2.2.12</u>)

If the displayed Package Parameter files (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) have been edited but *not* saved, “{EDITED}” is displayed next to the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) name on the “VistA Package Size Analysis Manager – Captioned List” screen heading. For example:

<span id="_Toc69721200" class="anchor"></span>Figure 57: Package Parameter Files Edited but Not Yet Saved: Example

Parameter file: XTMPSIZE_QG_Demo.DAT <span class="mark">{EDITED}</span>

Editing Package Parameters to correctly reflect the set of components included in the package requires review of the package definition by a package expert. The actions available on the “VistA Package Size Analysis Manager – Prefix/File Overlap” screen can aid analysis of the package definitions.

For example, the definition of the (sample) Accounts Receivable package (<u>Figure 56</u>) is shown in <u>Figure 58</u>:

<span id="_Ref467076734" class="anchor"></span>Figure 58: Accounts Receivable Captioned Parameter List: Example

Package Name: <span class="mark">ACCOUNTS RECEIVABLE</span>

Primary Prefix: PRCA

\*Lowest File#: 412

\*Highest File#: 439

Additional Prefixes: PRY\|RC\|

Excepted Prefixes:

File Numbers: 412\|430\|431\|432\|433\|434\|435\|436\|437\|438\|439\|

File Ranges: 412-439.9999\|330-349.9999\|

Parent Package:

The “VistA Package Size Analysis Manager – Prefix/File Overlap” screen report indicates no prefix (namespace) overlap, but it does note file range overlap as shown in <u>Figure 59</u>:

<span id="_Ref467076690" class="anchor"></span>Figure 59: Accounts Receivable Overlap Report Item: Example

ACCOUNTS RECEIVABLE \[Primary Prefix: PRCA\]

Parent: None indicated

<span class="mark">File range, 412-439.9999, overlaps with the following packages...</span>

. <span class="mark">IFCAP \[410-449.9999\]</span>

. <span class="mark">EQUIPMENT/TURN-IN REQUEST \[413-413.9\] (Parent: IFCAP)</span>

Notice that Accounts Receivable has file range overlaps with IFCAP and EQUIPMENT/TURN-IN REQUEST.

IFCAP and EQUIPMENT/TURN-IN REQUEST package definitions are defined in <u>Figure 60</u>:

<span id="_Ref467076204" class="anchor"></span>Figure 60: EQUIPMENT/TURN-IN REQUEST & IFCAP Captioned Parameter List: Examples

Package Name: <span class="mark">EQUIPMENT/TURN-IN REQUEST</span>

Primary Prefix: PRCN

\*Lowest File#: 413

\*Highest File#: 413.9

Additional Prefixes:

Excepted Prefixes:

File Numbers: 413\|

File Ranges: 413-413.9\|

Parent Package: IFCAP

Package Name: <span class="mark">IFCAP</span>

Primary Prefix: PRC

\*Lowest File#: 410

\*Highest File#: 449

Additional Prefixes: PRX\|

Excepted Prefixes: PRCA\|PRCN\|

File Numbers: 410\|411\|412\|413\|414\|415\|416\|417\|418\|419\|420\|421\|422\|423\|424\|425\|4

26\|427\|428\|429\|430\|431\|432\|433\|434\|435\|436\|437\|438\|439\|440\|441\|442\|443\|444\|445\|4

46\|447\|448\|449\|

File Ranges: 410-449.9999\|

Parent Package:

A Subject Matter Expert (SME) would need to look at these packages to determine if the File Numbers defined for each package should overlap. If the intersecting set of File Numbers remains, the Package Size Report counts the overlapping files under reports for both Packages. The package definition can be edited with the EPP—Edit Package Parameters \[XTVS PKG MGR EDIT PACKAGE PARM ACTION\] action (see Section <u>2.2.11.1</u>).

An SME can also determine if any of the packages can be deleted. The DPE—Delete Package Parameter Entry \[XTVS PKG MGR DEL PACKAGE PARM ACTION\] action (see Section <u>2.2.11.2</u>) allows deletion of a selected package from the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)).

<u>Figure 61</u> is an example of a report for the PATIENT (#2) file from the “VistA Package Size Analysis Manager – Prefix/File Overlap” screen. It shows a package definition that overlaps both files and prefixes (namespaces) with another package.

<span id="_Ref467076167" class="anchor"></span>Figure 61: PATIENT FILE Accounts Receivable Overlap Report Item: Example

PATIENT FILE \[Primary Prefix: DPT\]

Parent: REGISTRATION

<span class="mark">Prefix: DPT ; intersects the following packages...</span>

. <span class="mark">REGISTRATION \[DPT\]</span>

<span class="mark">File range, 2-2.9999, overlaps with the following packages...</span>

. <span class="mark">KERNEL WITHOUT MAILMAN \[0-41\]</span>

. <span class="mark">REGISTRATION \[2-2.9999\]</span>

Consider the prefix (namespace) overlap between the PATIENT FILE and REGISTRATION packages. The PATIENT FILE and REGISTRATION package parameters are defined as shown in <u>Figure 62</u>:

<span id="_Ref467076480" class="anchor"></span>Figure 62: PATIENT FILE and REGISTRATION Captioned Parameter List: Examples

Package Name: <span class="mark">PATIENT FILE</span>

Primary Prefix: DPT

\*Lowest File#: 2

\*Highest File#: 2

Additional Prefixes:

Excepted Prefixes:

File Numbers: 2\|

File Ranges: 2-2.9999\|

Parent Package: REGISTRATION

Package Name: <span class="mark">REGISTRATION</span>

Primary Prefix: DG

\*Lowest File#: 8

\*Highest File#: 409

Additional Prefixes: DGQE\|DPT\|VA\|VIC\|DGPT\|

Excepted Prefixes: DGYA\|DGJ\|DGBT\|VALM\|

File Numbers: 2\|8\|10\|11\|12\|13\|21\|22\|23\|24\|25\|30\|32\|33\|35\|37\|38\|39\|45\|46\|47\|48\|391\|392\|393\|394\|398\|399\|400\|401\|402\|405\|406\|408\|

File Ranges: 8-48.9999\|389-391.9999\|398-408.9999\|393-394.9999\|2-2.9999\|392-392.9999\|

Parent Package:

Again, an SME would need to review these packages to determine if both should be reported on the VistA Size Report. If so, further decisions would be needed to reconcile the prefix (namespace) and file intersections between the two packages so that the package size report includes the correct number of components for each package.

#### EPP—Edit Package Parameters

On the “VistA Package Size Analysis Manager - Captioned List” screen, use the EPP—Edit Package Parameters \[XTVS PKG MGR EDIT PACKAGE PARM ACTION\] action to enter a package to add/edit. The user is then prompted to edit the parameters required for Package Size Reporting, as shown in <u>Figure 63</u>:

<span id="_Ref482694031" class="anchor"></span>Figure 63: EPP—Edit Package Parameters Action: Example

<u>Package Parameter Details Apr 14, 2017@14:14:43 Page: 1 of 218</u>

<span class="mark">VistA Package Size Analysis Manager - Captioned List</span>

Version: 1 Build: 0

Default Directory: VA3\$:\[XUUSER\]

Parameter file: XTMPSIZE_OLD1.DAT;1

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

Package Name: ACCOUNTS RECEIVABLE

Primary Prefix: PRCA

\*Lowest File#: 412

\*Highest File#: 439

Additional Prefixes: PRY\|RC\|

Excepted Prefixes:

File Numbers: 412\|430\|431\|432\|433\|434\|435\|436\|437\|438\|439\|

File Ranges: 412-439.9999\|

Parent Package:

Package Name: ADP PLANNING

\+ Enter ?? for more actions and Help

<span class="mark">EPP Edit Package Parameters</span> SPP Save Package Parameter Changes

DPE Delete Package Parameter Entry

Select Action:Next Screen// <span class="mark">EPP \<Enter\></span> Edit Package Parameters

Select Package: <span class="mark">ACCOUNTS RECE</span>

ADD ENTRY? NO// <span class="mark">\<Enter\></span>

1: ACCOUNTS RECEIVABLE

Enter number for Selected Package: <span class="mark">1 \<Enter\></span> ACCOUNTS RECEIVABLE

Primary Prefix: PRCA// <span class="mark">\<Enter\></span>

\*Lowest File#: 412// <span class="mark">\<Enter\></span>

\*Highest File#: 439// <span class="mark">\<Enter\></span>

Additional Prefixes:

PRY\|RC\|

Enter Additional Prefix: <span class="mark">ZRC</span>

Prefix: ZRC// <span class="mark">\<Enter\></span>

ADD ENTRY? NO// <span class="mark">YES</span>

Additional Prefixes:

PRY\|RC\|ZRC\|

Enter Additional Prefix: <span class="mark">\<Enter\></span>

Excepted Prefixes:

{no data list}

Enter Excepted Prefix: <span class="mark">ZRCX</span>

Prefix: ZRCX// <span class="mark">\<Enter\></span>

ADD ENTRY? NO// <span class="mark">YES</span>

Excepted Prefixes:

ZRCX\|

Enter Excepted Prefix: <span class="mark">\<Enter\></span>

File Numbers:

412\|430\|431\|432\|433\|434\|435\|436\|437\|438\|439\|

Enter File Number: <span class="mark">438</span>

File Number: 438// <span class="mark">\<Enter\></span>

File Numbers:

412\|430\|431\|432\|433\|434\|435\|436\|437\|438\|439\|

Enter File Number: <span class="mark">438</span>

File Number: 438// <span class="mark">@</span>

DELETE ENTRY? NO// <span class="mark">YES</span>

File Numbers:

412\|430\|431\|432\|433\|434\|435\|436\|437\|439\|

Enter File Number: <span class="mark">438</span>

File Number: 438// <span class="mark">\<Enter\></span>

ADD ENTRY? NO// <span class="mark">YES</span>

File Numbers:

412\|430\|431\|432\|433\|434\|435\|436\|437\|439\|438\|

Enter File Number: <span class="mark">\<Enter\></span>

File Ranges:

412-439.9999\|

Enter File Number Range: <span class="mark">1-2.9999</span>

File Number Range: 1-2.9999// <span class="mark">\<Enter\></span>

ADD ENTRY? NO// <span class="mark">YES</span>

File Ranges:

412-439.9999\|1-2.9999\|

Enter File Number Range: <span class="mark">\<Enter\></span>

Parent Package: <span class="mark">ACCOUNTS REC</span>

1: ACCOUNTS RECEIVABLE

Enter number for Selected Package: <span class="mark">1 \<Enter\></span> ACCOUNTS RECEIVABLE

#### DPE—Delete Package Parameter Entry

On the “VistA Package Size Analysis Manager - Captioned List” screen, use the DPE—Delete Package Parameter Entry \[XTVS PKG MGR DEL PACKAGE PARM ACTION\] action to enter a package to delete. The user is reminded that deletion removes the package from the size report created with the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) being edited, as shown in <u>Figure 64</u>:

<span id="_Ref482693875" class="anchor"></span>Figure 64: DPE—Delete Package Parameter Entry Action: Example

<u>Package Parameter Details Apr 14, 2017@14:15:52 Page: 1 of 218</u>

<span class="mark">VistA Package Size Analysis Manager - Captioned List</span>

Version: 1 Build: 0

Default Directory: VA3\$:\[XUUSER\]

Parameter file: XTMPSIZE_OLD1.DAT;1 {EDITED}

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

Package Name: ACCOUNTS RECEIVABLE

Primary Prefix: PRCA

\*Lowest File#: 412

\*Highest File#: 439

Additional Prefixes: PRY\|RC\|ZRC\|

Excepted Prefixes: ZRCX\|

File Numbers: 412\|430\|431\|432\|433\|434\|435\|436\|437\|439\|438\|

File Ranges: 412-439.9999\|1-2.9999\|

Parent Package: ACCOUNTS RECEIVABLE

Package Name: ADP PLANNING

\+ Enter ?? for more actions and Help

EPP Edit Package Parameters SPP Save Package Parameter Changes

<span class="mark">DPE Delete Package Parameter Entry</span>

Select Action:Next Screen// <span class="mark">DPE \<Enter\></span> Delete Package Parameter Entry

Select Package: <span class="mark">ACCOUNTS</span>

1: ACCOUNTS RECEIVABLE

Enter number for Selected Package: <span class="mark">1 \<Enter\></span> ACCOUNTS RECEIVABLE

You have chosen to delete the ACCOUNTS RECEIVABLE entry

from the XTMPSIZE_OLD1.DAT;1 Package Parameter file.

\[If deleted, ACCOUNTS RECEIVABLE will not be included

in the VistA Size Report!\]

Are you SURE you want to delete the parameters for this package? NO// <span class="mark">YES</span>

### Save Edited Package Parameter List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To save the edited Package Parameter list, do the following:

1.  From the “VistA Package Size Analysis Manager – Captioned List” screen, select the SPP—Save Package Parameter Changes \[XTVS PKG MGR SAVE PACKAGE PARM ACTION\] action. It allows users to overwrite the displayed Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) or create a new Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)).

> <span id="_Ref1136945" class="anchor"></span>Figure 65: SPP—Save Package Parameter Changes Action: Example

> ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/059.png)

56. If you choose to save the edited parameters to a new XTMPSIZE\*.DAT file, the system creates a new file with the following file name format:

XTMPSIZE\_*\<user initials\>\<mm-dd-yy_hhmm\>*.DAT

The name of the new file is listed on the “VistA Package Size Analysis Manager – Captioned List” screen. For example:

Parameter file: <span class="mark">XTMPSIZE_GTS11-15-16_1436.DAT</span>

57. The edited (and saved) Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) is then displayed on the “VistA Package Size Analysis Manager” screen, as shown in <u>Figure 66</u>:

> <span id="_Ref467076023" class="anchor"></span>Figure 66: “VistA Package Size Analysis Manager” Screen: Updated

> ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/060.png)

### Create VistA Package Size Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can create a VistA Package Size Report for the following:

- <u>Single Package</u>
- <u>All Packages</u>

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/061.png) REF: For a list of Package Size Report errors, see the “<u>Package Size Report Errors</u>” section.

#### Single Package

To create a VistA Package Size Report for a single package, do the following:

1.  From the “VistA Package Size Analysis Manager” screen, select the VSR—Display VistA Size Report \[XTVS PKG MGR VISTA SIZE RPT\] action, as shown in <u>Figure 67</u>.
58. At the “Select the XTMPSIZE\*.DAT Package Parameter file item number:” prompt, enter the number corresponding to the desired Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) from a list of .DAT file, as shown in <u>Figure 67</u>.
59. At the “Do you want to display Sizing Information for ALL VistA Packages? NO//” prompt, enter NO (default), as shown in <u>Figure 67</u>.
60. At the “Select Package:” prompt, enter a package name, as shown in <u>Figure 67</u>.

> <span id="_Ref481069630" class="anchor"></span>Figure 67: VSR—Display VistA Size Report Action: Example: Single Package

Vista Package Size Manager Apr 14, 2017@14:24:07 Page: 2 of 4

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 1 Build: 13

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

10: XTMPSIZE_GTS1-18-17_1500.DAT;1

11: XTMPSIZE_GTS1-30-17_1235.DAT;1

12: XTMPSIZE_GTS10-11-16_1204.DAT;1

13: XTMPSIZE_GTS10-11-16_1208.DAT;1

14: XTMPSIZE_GTS10-28-16_1537.DAT;1

15: XTMPSIZE_GTS10-31-16_1535.DAT;1

16: XTMPSIZE_GTS11-17-16_1332.DAT;1

17: XTMPSIZE_GTS12-13-16_1102.BAK;1

18: XTMPSIZE_GTS12-13-16_1102.DAT;1

19: XTMPSIZE_GTS12-15-16_1130.BAK;1

<span class="mark">20: XTMPSIZE_QG_Demo.DAT</span>

\+ Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

<span class="mark">VSR Display VistA Size Report</span> UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Next Screen// <span class="mark">VSR \<Enter\></span> Display VistA Size Report

Select the XTMPSIZE\*.DAT Package Parameter file item number: <span class="mark">20</span>

VistA Package Sizing Report

Do you want to display Sizing Information for ALL VistA Packages? NO// <span class="mark">\<Enter\></span>

Select Package: <span class="mark">ACCOUNTS RECEIV</span>

1: ACCOUNTS RECEIVABLE

Enter number for Selected Package: <span class="mark">1 \<Enter\></span> ACCOUNTS RECEIVABLE

...counting...

...files...

...routines...

...options...

...remote procedures...

...edit, print, & sort templates...

When using the VSR—Display VistA Size Report \[XTVS PKG MGR VISTA SIZE RPT\] action, if a package is selected from the Package Parameter file that does *not* have the same name in the PACKAGE (#9.4) file, the message in <u>Figure 68</u> is displayed to the user:

> <span id="_Ref53658382" class="anchor"></span>Figure 68: Sample Error Message—Package Not Defined

Selected package is not defined in the Package file (#9.4) on this VistA.

Protocol count may be incorrect.

61. The package statistics are reported on the “VistA Package Size Analysis Manager – Package Statistics” screen, as shown in <u>Figure 69</u>:

> <span id="_Ref467075983" class="anchor"></span>Figure 69: “VistA Package Size Analysis Manager – Package Statistics” Screen—ListMan Screen

> ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/062.png)

62. When the report is displayed on the “VistA Package Size Analysis Manager – Package Statistics” screen, the user can select any of the following actions:
- [CTF—Create Text File](#ctf_create_text_file) \[XTVS PKG MGR RPT WRT ACTION\] (see <u>Figure 70</u> in Section <u>2.2.13</u>)
- [RVQ—Remote VistA Size Query](#rvq_remote_Vista_size_query) \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] (see Section <u>2.2.14</u>)
- [ER—Email Rpt Attachment](#er_email_rpt_attachment) \[XTVS PKG MGR RPT MAIL ACTION\] (see <u>Figure 71</u>)
- [SHD—Swap Header](#shd_swap_header) \[XTVS PKG RPT SWAP HEADER\] (see Section <u>2.2.17</u>)

These actions allow users to write text files that can be input to other applications (e.g., HPS Parametric Estimation Model).

> <span id="_Ref481069836" class="anchor"></span>Figure 70: CTF—Create Text File Action: Example

VistA Package Size Report Nov 15, 2016@15:19:30 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager - Package Statistics</span>

Version: 1 Build: 13

Default Directory: C:\TEMP

Parameter file: XTMPSIZE_QG_Demo.DAT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

VistA Application Sizing Information

Run Date: NOV 15, 2016

VistA Application: ACCOUNTS RECEIVABLE

==================

Number of Routines: 544

Size of Routines: 2709216

Number of Files: 121

Number of Fields: TBD

Number of Options: 275

Number of Protocols: 146

Number of RPCs: 0

Number of Templates: 82

Enter ?? for more actions and Help <span class="mark"></span>

<span class="mark">CTF Create Text File</span> ER Email Rpt Attachment

RVQ Remote VistA Size Query SHD (Swap Header)

Select Action:Quit// <span class="mark">CTF \<Enter\></span> Create Text File

Enter directory to write report file: VA3\$:\[XUUSER\]// <span class="mark">\<Enter\></span>

Enter the name of the Host File VistAPkgSize_31704141425.txt// <span class="mark">\<Enter\></span>

> <span id="_Ref481069837" class="anchor"></span>Figure 71: ER—Email Rpt Attachment Action: Example

VistA Package Size Report Nov 15, 2016@15:19:30 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager - Package Statistics</span>

Version: 1 Build: 13

Default Directory: C:\TEMP

Parameter file: XTMPSIZE_QG_Demo.DAT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

VistA Application Sizing Information

Run Date: NOV 15, 2016

VistA Application: ACCOUNTS RECEIVABLE

==================

Number of Routines: 544

Size of Routines: 2709216

Number of Files: 121

Number of Fields: TBD

Number of Options: 275

Number of Protocols: 146

Number of RPCs: 0

Number of Templates: 82

Enter ?? for more actions and Help

CTF Create Text File <span class="mark">ER Email Rpt Attachment</span>

RVQ Remote VistA Size Query SHD (Swap Header)

Select Action:Quit// <span class="mark">ER \<Enter\></span> Email Rpt Attachment

The message can take some time to be sent.

Send mail to: XUUSER,ONE// <span class="mark">ONE.XUUSER@VA.GOV</span>

Looking in Internet Suffix file... US GOVERNMENT via REDACTED.VA.GOV

And Send to: <span class="mark">\<Enter\></span>

> **NOTE:** Attachments sent to VA Mailman addresses will be unreadable.

Send the report in a message if sending to a VA MailMan address.

Send the VistA Size Report as a message or a text file attachment: A// <span class="mark">\<Enter\></span> ttachment

\[Creating attachments...

#### All Packages

To create a VistA Package Size Report of *all* packages on the VistA instance, do the following:

1.  From the “VistA Package Size Analysis Manager” screen, select the VSR—Display VistA Size Report \[XTVS PKG MGR VISTA SIZE RPT\] action, as shown in <u>Figure 72</u>.
63. At the “Select the XTMPSIZE\*.DAT Package Parameter file item number:” prompt, enter the number corresponding to the desired Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) from a list of .DAT file, as shown in <u>Figure 72</u>.
64. At the “Do you want to display Sizing Information for ALL VistA Packages? NO//” prompt, enter “YES” to display the report for *all* packages, as shown in <u>Figure 72</u>.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/063.png) NOTE: Reporting for “ALL VistA Packages” can take several minutes to complete.

65. The system prompts the user to select the type of report (for all packages), as shown in <u>Figure 72</u>.

Selection of any of these report options can take 3 to 5 minutes to complete the counting process for all components in all of the packages.

> <span id="_Ref482360681" class="anchor"></span>Figure 72: VSR—Display VistA Size Report Action: Example: All Packages

Vista Package Size Manager Apr 14, 2017@14:24:07 Page: 2 of 4

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 1 Build: 24

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

10: XTMPSIZE_GTS1-18-17_1500.DAT;1

11: XTMPSIZE_GTS1-30-17_1235.DAT;1

12: XTMPSIZE_GTS10-11-16_1204.DAT;1

13: XTMPSIZE_GTS10-11-16_1208.DAT;1

14: XTMPSIZE_GTS10-28-16_1537.DAT;1

15: XTMPSIZE_GTS10-31-16_1535.DAT;1

16: XTMPSIZE_GTS11-17-16_1332.DAT;1

17: XTMPSIZE_GTS12-13-16_1102.BAK;1

18: XTMPSIZE_GTS12-13-16_1102.DAT;1

19: XTMPSIZE_GTS12-15-16_1130.BAK;1

<span class="mark">20: XTMPSIZE_QG_Demo.DAT</span>

\+ Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

<span class="mark">VSR Display VistA Size Report</span> UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Next Screen// <span class="mark">VSR \<Enter\></span> Display VistA Size Report

Select the XTMPSIZE\*.DAT Package Parameter file item number: <span class="mark">20</span>

VistA Package Sizing Report

Do you want to display Sizing Information for ALL VistA Packages? NO// <span class="mark">YES</span>

Select which method to display the package size data:

1\. Sorted on PACKAGE NAME

2\. Sorted on NUMBER of ROUTINES (Highest to Lowest)

3\. Sorted on TOTAL ROUTINE SIZE (Highest to Lowest)

<span class="mark">4. Delimited (^) Data, Sorted on PACKAGE NAME</span>

5\. Delimited (^) Data with PARENT PKG, Sorted by PACKAGE NAME

Select VistA Size Report: <span class="mark">4 \<Enter\></span> SORT ON PKG NAME, CARET DELIMITED DATA

Compiling component totals for selected Package data file... \\

To generate the input report for the HPS Parametric Estimation Model, select one of the “Delimited” options shown in <u>Figure 73</u>:

> <span id="_Ref53662705" class="anchor"></span>Figure 73: VSR—Display VistA Size Report Action: Choosing Option 4, Delimited (^) Data, Sorted on PACKAGE NAME

<span class="mark">4. Delimited (^) Data, Sorted on PACKAGE NAME</span>

<span class="mark">5. Delimited (^) Data with PARENT PKG, Sorted by PACKAGE NAME</span>

Select VistA Size Report: <span class="mark">4 \<Enter\></span> SORT ON PKG NAME, CARET DELIMITED DATA

Compiling component totals for selected Package data file... \\

For example, Option 4—Delimited (^) Data, Sorted on PACKAGE NAME is used to generate the text file for input to the HPS Parametric Estimation Model.

66. The package statistics are reported on the “VistA Package Size Analysis Manager – Package Statistics” screen, as shown in <u>Figure 74</u>:

> <span id="_Ref467149814" class="anchor"></span>Figure 74: VSR—Display VistA Size Report Action: Sample Delimited (^) Data, Sorted on PACKAGE NAME Output: Package Statistics

> ![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/064.png)

The output from the Delimited (^) Data, Sorted on PACKAGE NAME option contains a caret delimited report of package size data that is displayed on the “VistA Package Size Analysis Manager – Package Statistics” screen.

If a report of all packages encounters package names in the Package Parameter file that are *not* defined in the local Package Parameter file, the user receives a VA MailMan message listing the package names missing from the PACKAGE (#9.4) file, as shown in <u>Figure 75</u>:

<span id="_Ref53662608" class="anchor"></span>Figure 75: Sample VA MailMan Message—Missing Package Names

Subj: PACKAGE REPORT NOTICE (*SITE1PRO*) ; Report process warning. \[#160415\] 10/08/20@12:53 5 lines

From: VISTA PACKAGE SIZE ANALYSIS MANAGER In 'IN' basket. Page 1

-------------------------------------------------------------------

Package Size Report warning for *SITE1PRO*.

The following package(s) are not found on this VistA.

(The number of protocols reported may be incorrect.)

\- MY LOCAL PACKAGE

\- ABC 4'' LABEL

67. When the report is displayed on the “VistA Package Size Analysis Manager – Package Statistics” screen, the user can select any of the following actions:
- [CTF—Create Text File](#ctf_create_text_file) \[XTVS PKG MGR RPT WRT ACTION\] (see Section <u>2.2.13</u>)
- [RVQ—Remote VistA Size Query](#rvq_remote_Vista_size_query) \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] (see Section <u>2.2.14</u>)
- [ER—Email Rpt Attachment](#er_email_rpt_attachment) \[XTVS PKG MGR RPT MAIL ACTION\] (see Section <u>2.2.13</u>)
- [SHD—Swap Header](#shd_swap_header) \[XTVS PKG RPT SWAP HEADER\] (see Section <u>2.2.17</u>)

These actions allow users to write text files that can be input to other applications (e.g., HPS Parametric Estimation Model).

#### Package Size Report Errors

Error messages are returned to the requesting user when the remote server fails to return the requested report.

The package size report errors in <u>Figure 76</u> are also added to the VistA error trap on the remote VistA when the error occurs:

<span id="_Ref61508017" class="anchor"></span>Figure 76: Sample Package Size Report Errors Added to VistA Error Trap

15)  ONEPKGSZ^XTVSSVR : Package Size Rpt error10:14:36  SITE1PRO:DEVR0TSVR    31
14)  ONEPKGSZ^XTVSSVR : Package Size Rpt error10:14:35  SITE1PRO:DEVR0TSVR    31
10)  SRVREXT^XTVSSVR : Package Size Rpt error10:14:31  SITE1PRO:DEVR0TSVR    314

<span id="_Toc69721220" class="anchor"></span>Figure 77: Sample Package Size Report Error Message—MISSING PACKAGE NAME

Subj: PACKAGE SIZE REPORT (FOR ; remote request FAILED!  \[#91770\]

08/21/20@10:27  3 lines

From: XTUSER,ONE  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Notice for Remote Package size report on FOR.

Remote size report request FAILED for {MISSING PACKAGE NAME}.

Parameters for a selected package not sent in server request.

Enter message action (in IN basket): Ignore//

<span id="_Toc69721221" class="anchor"></span>Figure 78: Sample Package Size Report Error Message—^XTMP Not Sent in PackMan

Subj: PACKAGE SIZE REPORT (FOR ; remote request FAILED! \[#91772\]

08/21/20@10:27 2 lines

From: XTUSER,ONE In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Remote package size report on FOR failed!!

Error: ^XTMP("XTSIZE",123) not sent in Packman to XTUSER.ONE@REDACTED.VA.GOV!

Enter message action (in IN basket): Ignore//

<span id="_Toc69721222" class="anchor"></span>Figure 79: Sample Package Size Report Error Message—Remote Size Report Request FAILED for ALL Packages

Subj: PACKAGE SIZE REPORT (FOR ; remote request FAILED!  \[#91773\]

08/21/20@10:27  3 lines

From: XTUSER,ONE  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Notice for Remote Package size report on FOR.

Remote size report request FAILED for ALL Packages.

Error: ^XTMP("XTVS-REMOTE-SIZE",31493) not sent in Packman to XTUSER.ONE@REDACTED.VA.GOV!

Enter message action (in IN basket): Ignore//

<span id="_Toc69721223" class="anchor"></span>Figure 80: Sample Package Size Report Error Message—Remote Size Report Request FAILED: Selected Package is Not Defined in the PACKAGE (#9.4) File on this VistA

Subj: PACKAGE SIZE REPORT (FOR ; remote request FAILED!  \[#91774\]

08/21/20@10:27  3 lines

From: XTUSER,ONE  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Notice for Remote Package size report on FOR.

Remote size report request FAILED for ZGTS TEST 2.

Selected package is not defined in the Package file (#9.4) on this VistA.

Enter message action (in IN basket): Ignore//

<span id="_Toc69721224" class="anchor"></span>Figure 81: Sample Package Size Report Error Message—Remote Size Report Request FAILED: PREFIX Not Found for Package Selected

Subj: PACKAGE SIZE REPORT (FOR ; remote request FAILED!  \[#91775\]

08/21/20@10:27  3 lines

From: XTUSER,ONE  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Notice for Remote Package size report on FOR.

Remote size report request FAILED for ZGTS TEST 2.

PREFIX not found for package selected.

Enter message action (in IN basket): Ignore//

<span id="_Toc69721225" class="anchor"></span>Figure 82: Sample Package Size Report Error Message—Remote Size Report Request FAILED: ^XTMP Not Sent in PackMan

Subj: PACKAGE SIZE REPORT (FOR ; remote request FAILED!  \[#91776\]

08/21/20@10:27  3 lines

From: XTUSER,ONE  In 'IN' basket.   Page 1

-------------------------------------------------------------------------------

Notice for Remote Package size report on PFOR.

Remote size report request FAILED for ZGTS TEST 2.

Error: ^XTMP("XTVS-REMOTE-RPT") not sent in Packman to XTUSER.ONE@REDACTED.VA.GOV!

Enter message action (in IN basket): Ignore//

### Query a Remote VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RVQ—Remote VistA Size Query \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] action is available from the following screens:

- VistA Package Size Analysis Manager - Package Statistics
- VistA Package Size Analysis Manager

This action allows a user to request a VistA Package Size report for a single package from a selected remote VistA.

When exercising this action from the “VistA Package Size Analysis Manager - Package Statistics” screen, the request sends the Package Parameter file used to create the displayed report to the remote VistA so that an apples-to-apples size report is returned from the remote VistA. That is the same package parameters are used to create the report.

When exercising this action from the “VistA Package Size Analysis Manager” screen, the request prompts the user to select a Package Parameter file and send in the request to the remote VistA so the report can be created on the remote VistA.

If the remote VistA does *not* have a package in the PACKAGE (#9.4) file with a name that matches the package name selected for reporting, the user receives a VA MailMan message similar to <u>Figure 83</u>:

<span id="_Ref53667097" class="anchor"></span>Figure 83: Sample VA MailMan Message—Missing Package

Subj: PACKAGE REPORT NOTICE (*SITE1PRO*) ; Report process warning. \[#160374\]

10/08/20@12:19 2 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Package Size Report warning for *SITE1PRO*.

Package: GTS LOCAL PACKAGE...not found! Protocol count may be incorrect.

In addition to selecting the package to report and the VistA to report, the user needs to select the Package Parameter file to use for creating the Package size on the remote VistA.

<span id="_Ref59200593" class="anchor"></span>Figure 84: RVQ—Remote VistA Size Query Action: Example 1

Do you want to Display XTMPSIZE\*.BAK (backup files)? NO// <span class="mark">\<Enter\></span>

VistA Package Size Manager Jul 30, 2020@09:29:23 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 7.3 Build: 93

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

XTMPSIZE.DAT Package Parameter file list in /srv/vista/*\<scd\>*/user/hfs/:

--------------------------------------------------------------------

1\) XTMPSIZE_GTS11-15-16_1436.DAT

2\) XTMPSIZE_GTS4-2-20_0944.DAT

3\) XTMPSIZE_GTS5-14-20_1023.DAT

4\) XTMPSIZE_GTS5-14-20_1025.DAT

5\) XTMPSIZE_GTS6-29-20_0712.DAT

6\) XTMPSIZE_QG_Demo.DAT

Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

VSR Display VistA Size Report UNL Unlock Parameter File

<span class="mark">RVQ Remote VistA Size Query</span>

Select Action:Quit// <span class="mark">RVQ \<Enter\></span> Remote VistA Size Query

Select the XTMPSIZE\*.DAT Package Parameter file item number: (1-6): <span class="mark">1</span>

The response from a remote VistA can take some time.

Do you want to request a report from a remote VistA? YES// <span class="mark">\<Enter\></span>

XTMPSIZE_GTS11-15-16_1436.DAT LOCK obtained.

Press Return to continue: <span class="mark">\<Enter\></span>

...Loading Parameters...

Parameter file XTMPSIZE_GTS11-15-16_1436.DAT LOCK released.

Press Return to continue: <span class="mark">\<Enter\></span>

Select Package: <span class="mark">ACCOUNTS R</span>

1: ACCOUNTS RECEIVABLE

Enter number for Selected Package: <span class="mark">1 \<Enter\></span> ACCOUNTS RECEIVABLE

Domain server to query: <span class="mark">*SITE1PRO*.REDACTED.VA.GOV</span>

Query message sent! Message \# 91549

Press Return to continue: <span class="mark">\<Enter\></span>

VistA Package Size Manager Jul 30, 2020@09:30 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 7.3 Build: 93

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

XTMPSIZE.DAT Package Parameter file list in /srv/vista/*\<scd\>*/user/hfs/:

--------------------------------------------------------------------

1\) XTMPSIZE_GTS11-15-16_1436.DAT

2\) XTMPSIZE_GTS4-2-20_0944.DAT

3\) XTMPSIZE_GTS5-14-20_1023.DAT

4\) XTMPSIZE_GTS5-14-20_1025.DAT

5\) XTMPSIZE_GTS6-29-20_0712.DAT

6\) XTMPSIZE_QG_Demo.DAT

Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Quit//

The user only needs to select the package to report and the VistA to report. The Package Parameter file was selected when creating the local report to execute the VSR—Display VistA Size Report \[XTVS PKG MGR VISTA SIZE RPT\] action.

<span id="_Ref59200771" class="anchor"></span>Figure 85: RVQ—Remote VistA Size Query Action: Example 2

Do you want to Display XTMPSIZE\*.BAK (backup files)? NO// <span class="mark">\<Enter\></span>

VistA Package Size Manager Jul 30, 2020@12:01:55 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 7.3 Build: 93

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

XTMPSIZE.DAT Package Parameter file list in /srv/vista/*\<scd\>*/user/hfs/:

--------------------------------------------------------------------

1\) XTMPSIZE_GTS11-15-16_1436.DAT

2\) XTMPSIZE_GTS4-2-20_0944.DAT

3\) XTMPSIZE_GTS5-14-20_1023.DAT

4\) XTMPSIZE_GTS5-14-20_1025.DAT

5\) XTMPSIZE_GTS6-29-20_0712.DAT

6\) XTMPSIZE_QG_Demo.DAT

Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

<span class="mark">VSR Display VistA Size Report</span> UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Quit// <span class="mark">VSR \<Enter\></span> Display VistA Size Report

Select the XTMPSIZE\*.DAT Package Parameter file item number: (1-6): <span class="mark">1</span>

XTMPSIZE_GTS11-15-16_1436.DAT LOCK obtained.

Press Return to continue: <span class="mark">\<Enter\></span>

VistA Package Sizing Report

Do you want to display Sizing Information for ALL VistA Packages? NO// <span class="mark">\<Enter\></span>

Select Package: <span class="mark">ACCOUNTS</span>

1: ACCOUNTS RECEIVABLE

Enter number for Selected Package: <span class="mark">1 \<Enter\></span> ACCOUNTS RECEIVABLE

...counting...

...files and fields...

...routines...

...options...

...protocols...

...remote procedures...

...edit, print, & sort templates...

Parameter file XTMPSIZE_GTS11-15-16_1436.DAT LOCK released.

Press Return to continue: <span class="mark">\<Enter\></span>

VistA Package Size Report Jul 30, 2020@12:02:14 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager - Package Statistics</span>

Version: 7.3 Build: 93

Default Directory: /srv/vista/*\<scd\>*/user/hfs/

Parameter file: XTMPSIZE_GTS11-15-16_1436.DAT

VistA Application Sizing Information

Run Date: JUL 30, 2020

VistA Application: ACCOUNTS RECEIVABLE

==================

Number of Routines: 605

Size of Routines: 2419858

Number of Files: 110

Number of Fields: 2307

Number of Options: 260

Number of Protocols: 0

Number of RPCs: 1

Number of Templates: 128

Enter ?? for more actions and Help

CTF Create Text File ER Email Rpt Attachment

RVQ Remote VistA Size Query SHD (Swap Header)

Select Action:Quit// <span class="mark">RVQ \<Enter\></span> Remote VistA Size Query

The response from a remote VistA can take some time.

Do you want to request a report from a remote VistA? YES// <span class="mark">\<Enter\></span>

XTMPSIZE_GTS11-15-16_1436.DAT LOCK obtained.

Press Return to continue: <span class="mark">\<Enter\></span>

...Loading Parameters...

Parameter file XTMPSIZE_GTS11-15-16_1436.DAT LOCK released.

Press Return to continue: <span class="mark">\<Enter\></span>

Select Package: <span class="mark">ACCOUNTS RE</span>

1: ACCOUNTS RECEIVABLE

Enter number for Selected Package: <span class="mark">1 \<Enter\></span> ACCOUNTS RECEIVABLE

Domain server to query: <span class="mark">*SITE1PRO*.REDACTED.VA.GOV</span>

Query message sent! Message \# 91553

Press Return to continue: <span class="mark">\<Enter\></span>

VistA Package Size Report Jul 30, 2020@12:02:44 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager - Package Statistics</span>

Version: 7.3 Build: 93

Default Directory: /srv/vista/*\<scd\>*/user/hfs/

Parameter file: XTMPSIZE_GTS11-15-16_1436.DAT

VistA Application Sizing Information

Run Date: JUL 30, 2020

VistA Application: ACCOUNTS RECEIVABLE

==================

Number of Routines: 605

Size of Routines: 2419858

Number of Files: 110

Number of Fields: 2307

Number of Options: 260

Number of Protocols: 0

Number of RPCs: 1

Number of Templates: 128

Enter ?? for more actions and Help

CTF Create Text File ER Email Rpt Attachment

RVQ Remote VistA Size Query SHD (Swap Header)

Select Action:Quit//

<u>Figure 86</u> is an example of the RVQ—Remote VistA Size Query \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] action when executed from a local size report for all packages.

<span id="_Ref55829548" class="anchor"></span>Figure 86: RVQ—Remote VistA Size Query Action: Example 3

Do you want to Display XTMPSIZE\*.BAK (backup files)? NO// \<Enter\>

VistA Package Size Manager Jul 30, 2020@12:05:17 Page: 1 of 1

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 7.3 Build: 93

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

XTMPSIZE.DAT Package Parameter file list in /srv/vista/*\<scd\>*/user/hfs/:

--------------------------------------------------------------------

1\) XTMPSIZE_GTS11-15-16_1436.DAT

2\) XTMPSIZE_GTS4-2-20_0944.DAT

3\) XTMPSIZE_GTS5-14-20_1023.DAT

4\) XTMPSIZE_GTS5-14-20_1025.DAT

5\) XTMPSIZE_GTS6-29-20_0712.DAT

6\) XTMPSIZE_QG_Demo.DAT

Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Quit// <span class="mark">VSR \<Enter\></span> Display VistA Size Report

Select the XTMPSIZE\*.DAT Package Parameter file item number: (1-6): <span class="mark">1</span>

XTMPSIZE_GTS11-15-16_1436.DAT LOCK obtained.

Press Return to continue: <span class="mark">\<Enter\></span>

VistA Package Sizing Report

Do you want to display Sizing Information for ALL VistA Packages? NO// <span class="mark">YES</span>

Select which method to display the package size data:

1\. Sorted on PACKAGE NAME

2\. Sorted on NUMBER of ROUTINES (Highest to Lowest)

3\. Sorted on TOTAL ROUTINE SIZE (Highest to Lowest)

<span class="mark">4. Delimited (^) Data, Sorted on PACKAGE NAME</span>

5\. Delimited (^) Data with PARENT PKG, Sorted by PACKAGE NAME

Select VistA Size Report: <span class="mark">4 \<Enter\></span> SORT ON PKG NAME, CARET DELIMITED DATA

Compiling component totals for selected Package data file... -

Parameter file XTMPSIZE_GTS11-15-16_1436.DAT LOCK released.

Press Return to continue: <span class="mark">\<Enter\></span>

VistA Package Size Report Jul 30, 2020@12:05:42 Page: 1 of 16

<span class="mark">VistA Package Size Analysis Manager - Package Statistics</span>

Version: 7.3 Build: 93

Default Directory: /srv/vista/*\<scd\>*/user/hfs/

Parameter file: XTMPSIZE_GTS11-15-16_1436.DAT

{package name}^{prefix}^{#rtns}^{size of rtns}^{#files}^{#fields}^{#options}^{#p

ACCOUNTS RECEIVABLE^PRCA^605^2419858^110^2307^260^0^1^128

ADVERSE REACTION TRACKING^GMRA^161^488568^13^273^44^18^0^4

ALERTS^XQAL^15^88760^0^0^16^0^1^1

ANTICOAGULATION MANAGEMENT^ORAM^8^84188^0^0^13^0^35^3

ASISTS^OOPS^88^485014^32^551^10^0^65^0

AUT^AUT^1^531^0^0^0^0^0^0

AUTHORIZATION/SUBSCRIPTION^USR^36^92658^7^49^11^0^0^4

AUTO REPLENISHMENT/WARD STOCK^PSGW^105^252050^23^590^82^0^0^50

AUTOMATED INFO COLLECTION SYS^IBD^851^4180518^101^1742^48^1^16^32

AUTOMATED LAB INSTRUMENTS^LA^393^1380289^0^0^77^35^0^14

AUTOMATED MED INFO EXCHANGE^DVBA^929^3525741^16^342^88^1^70^28

BAR CODE EXPANSION^MJCF^0^0^0^0^0^0^0^0

BAR CODE MED ADMIN^PSB^92^650944^0^0^46^21^43^0

\+ Enter ?? for more actions and Help

CTF Create Text File ER Email Rpt Attachment

RVQ Remote VistA Size Query SHD (Swap Header)

Select Action:Next Screen// <span class="mark">RVQ \<Enter\></span> Remote VistA Size Query

The response from a remote VistA can take some time.

Do you want to request a report from a remote VistA? YES// <span class="mark">\<Enter\></span>

XTMPSIZE_GTS11-15-16_1436.DAT LOCK obtained.

Press Return to continue: <span class="mark">\<Enter\></span>

...Loading Parameters...

Parameter file XTMPSIZE_GTS11-15-16_1436.DAT LOCK released.

Press Return to continue: <span class="mark">\<Enter\></span>

Select Package: <span class="mark">ACCOUNTS RE</span>

1: ACCOUNTS RECEIVABLE

Enter number for Selected Package: <span class="mark">1 \<Enter\></span> ACCOUNTS RECEIVABLE

Domain server to query: <span class="mark">*SITE1PRO*.REDACTED.VA.GOV</span>

Query message sent! Message \# 91555

Press Return to continue: <span class="mark">\<Enter\></span>

VistA Package Size Report Jul 30, 2020@12:06:10 Page: 1 of 16

<span class="mark">VistA Package Size Analysis Manager - Package Statistics</span>

Version: 7.3 Build: 93

Default Directory: /srv/vista/*\<scd\>*/user/hfs/

Parameter file: XTMPSIZE_GTS11-15-16_1436.DAT

{package name}^{prefix}^{#rtns}^{size of rtns}^{#files}^{#fields}^{#options}^{#p

ACCOUNTS RECEIVABLE^PRCA^605^2419858^110^2307^260^0^1^128

ADVERSE REACTION TRACKING^GMRA^161^488568^13^273^44^18^0^4

ALERTS^XQAL^15^88760^0^0^16^0^1^1

ANTICOAGULATION MANAGEMENT^ORAM^8^84188^0^0^13^0^35^3

ASISTS^OOPS^88^485014^32^551^10^0^65^0

AUT^AUT^1^531^0^0^0^0^0^0

AUTHORIZATION/SUBSCRIPTION^USR^36^92658^7^49^11^0^0^4

AUTO REPLENISHMENT/WARD STOCK^PSGW^105^252050^23^590^82^0^0^50

AUTOMATED INFO COLLECTION SYS^IBD^851^4180518^101^1742^48^1^16^32

AUTOMATED LAB INSTRUMENTS^LA^393^1380289^0^0^77^35^0^14

AUTOMATED MED INFO EXCHANGE^DVBA^929^3525741^16^342^88^1^70^28

BAR CODE EXPANSION^MJCF^0^0^0^0^0^0^0^0

BAR CODE MED ADMIN^PSB^92^650944^0^0^46^21^43^0

\+ Enter ?? for more actions and Help

CTF Create Text File ER Email Rpt Attachment

RVQ Remote VistA Size Query SHD (Swap Header)

Select Action:Quit//

<u>Figure 87</u> is an example of the Remote VistA Size Report message received when the RVQ—Remote VistA Size Query \[XTVS PKG MGR RPT QUERY REMOTE ACTION and XTVS PKG QUERY REMOTE VISTA SIZE ACTION\] action is completed.

<span id="_Ref63061131" class="anchor"></span>Figure 87: VA MailMan—Sample Remote VistA Size Report Message Received

Select MailMan Option: <span class="mark">??</span>

Choose from:

1 SEND A MESSAGE

2 READ/MANAGE MESSAGES

3 NEW MESSAGES AND RESPONSES

4 LOAD PACKMAN MESSAGE

5 EDIT USER OPTIONS

6 PERSONAL MAIL GROUP EDIT

7 JOIN MAIL GROUP

8 MAILBOX CONTENTS LIST

9 LOG-IN TO ANOTHER SYSTEM (TalkMan)

10 QUERY/SEARCH FOR MESSAGES

11 BLOB SEND

Select MailMan Option: <span class="mark">NEW MESSAGES AND RESPONSES</span>

Select New mail option: Read new mail by basket// <span class="mark">\<Enter\></span>

Subj: PACKAGE SIZE REPORT (*SITE1PRO* ; Jul 29, 2020 12:56:26 pm ; \$JOB#: 9

\[#91530\] 07/29/20@12:56 16 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

VistA Application Sizing Information

Site Domain: *SITE1PRO*.REDACTED.VA.GOV

Run Date: JUL 29, 2020

VistA Application: ACCOUNTS RECEIVABLE

==================

Number of Routines: 605

Size of Routines: 2419858

Number of Files: 110

Number of Fields: 2307

Number of Options: 260

Number of Protocols: 0

Number of RPCs: 1

Number of Templates: 128

Enter message action (in IN basket): Ignore//

### Change Host File Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the “VistA Package Size Analysis Manager” screen, set the Package Parameter file (i.e., [XTMPSIZE\*.DAT](#package_parameter_file_name_format)) default directory as follows:

1.  Invoke the VistA Package Extract Manager \[XTVS VISTA PACKAGE EXTRACT MGR\] option.
2.  At the “Do you want to Display XTMPSIZE\*.BAK (backup files)? NO//” prompt, press Enter to accept the NO default response.
3.  From the “VistA Package Size Analysis Manager” screen, select the CHD—Change Host Directory \[XTVS SITE PARAMETERS\] action, as shown in <u>Figure 88</u>.

![](vista-package-size-reporting-tool-vpsrt-user-guide-xt-7-3-143/065.png) NOTE: The CHD—Change Host Directory \[XTVS SITE PARAMETERS\] action is locked with the XTVS EDITOR security key.

4.  Set the “VistA Package Size default directory” to a directory on the VistA server host system that the user, who will be managing package parameters and creating package size reports, has READ and WRITE privileges.

<span id="_Ref480957390" class="anchor"></span>Figure 88: CHD—Change Host Directory Action: Example

Vista Package Size Manager Apr 14, 2017@14:07:44 Page: 3 of 4

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 1 Build: 0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

22\) XTMPSIZE_GTS2-9-17_1627.DAT;1

23\) XTMPSIZE_GTS3-6-17_0922.DAT;1

24\) XTMPSIZE_GTS4-10-17_0839.DAT;1

25\) XTMPSIZE_GTS7-26-16_1054.DAT;1

26\) XTMPSIZE_GTS7-26-16_1119.DAT;1

27\) XTMPSIZE_GTS7-26-16_1527.DAT;1

28\) XTMPSIZE_GTS7-26-16_1531.DAT;1

29\) XTMPSIZE_GTS7-27-16_1016.DAT;1

30\) XTMPSIZE_GTS8-11-16_0838.DAT;1

31\) XTMPSIZE_GTS8-18-16_1014.DAT;1

32\) XTMPSIZE_GTS8-3-16_1545.DAT;1

33\) XTMPSIZE_GTS8-4-16_1321.DAT;1

34\) XTMPSIZE_GTS8-8-16_1532.DAT;1

\+ Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters <span class="mark">CHD Change Host Directory</span>

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Next Screen// <span class="mark">CHD \<Enter\></span> Change Host Directory

Package Size Parameter Edit for System: REDACTED.VA.GOV

------------------------------------------------------------------------------

VistA Package Size default directory VA3\$:\[XUUSER\]

------------------------------------------------------------------------------

VistA Package Size default directory: VA3\$:\[XUUSER\]//

### Unlock Parameter File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The UNL—Unlock Parameter File \[XTVS PKG MGR PARAM UNLOCK ACTION\] action deletes the lock file for the Package Parameter file. Typical use of unlock would occur when a system-level problem removes a lock while a file is being used. To display and unlock a LOCKED Package Parameter file, do the following:

1.  From the “VistA Package Size Manager” screen, invoke the UNL—Unlock Parameter File \[XTVS PKG MGR PARAM UNLOCK ACTION\] action.
2.  A list of LOCKED files is displayed, as shown in <u>Figure 89</u>:

> <span id="_Ref12943382" class="anchor"></span>Figure 89: Sample List of LOCKED Files

1: XTMPSIZE_GTS5-16-19_1052.LCK

Select File:

3.  Select the file that was LOCKED.
4.  At the “Do you want to UNLOCK XTMPSIZE\_*\<your initials\>mm*-*dd*-*yy*\_*hhss*.DAT?” prompt, enter YES. This removes the lock on that file.

### Swapping Headers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SHD—Swap Header \[XTVS PKG RPT SWAP HEADER\] action swaps the “List Manager” header on a displayed VistA size report for all packages. The user can display either of the following headers:

- Default report header format (<u>Figure 90</u>).
- Column headings for the listed packages (<u>Figure 91</u>).

This action is *not* active (displayed in parenthesis) from the “VistA Package Size Analysis Manager - Package Statistics” screen for a single package (see <u>Figure 86</u>), because the date headings are displayed next to the data. The SHD—Swap Header \[XTVS PKG RPT SWAP HEADER\] action is only active when a user readable report for all packages is displayed.

Specifically, the display of the sample report headings in <u>Figure 90</u> and <u>Figure 91</u> is toggled by the SHD—Swap Header \[XTVS PKG RPT SWAP HEADER\] action:

<span id="_Ref55828877" class="anchor"></span>Figure 90: “List Manager” Header Format—Example 1

VistA Package Size Analysis Manager - Package Statistics

Version: 7.3 Build: 108

Default Directory: /srv/vista/*\<scd\>*/user/hfs/

Parameter file: XTMPSIZE_QG_Demo.DAT

<span id="_Ref55828918" class="anchor"></span>Figure 91: “List Manager” Header Format—Example 2

Total

Application Rtn

(Namespace) Routines Size Files Fields Options Protocols RPCs Templates

When the SHD—Swap Header \[XTVS PKG RPT SWAP HEADER\] action is executed, it would change the “first” header format (<u>Figure 90</u>) to the “second” header format (<u>Figure 91</u>).

<span id="_Ref59433298" class="anchor"></span>Figure 92: SHD—Swap Header Action: Example 1

Select OPTION NAME: <span class="mark">XTVS VISTA PACKAGE EXTRACT MGR \<Enter\></span> VistA Package Extract Manager

VistA Package Extract Manager

Do you want to Display XTMPSIZE\*.BAK (backup files)? NO// <span class="mark">\<Enter\></span>

VistA Package Size Manager Sep 09, 2020@07:26:31 Page: 1 of 2

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 7.3 Build: 96

XTMPSIZE.DAT default directory: /srv/vista/*\<scd\>*/user/hfs/

XTMPSIZE.DAT Package Parameter file list in /srv/vista/*\<scd\>*/user/hfs/:

--------------------------------------------------------------------

1\) XTMPSIZE_GTS11-15-16_1436.DAT

2\) XTMPSIZE_GTS4-2-20_0944.DAT

3\) XTMPSIZE_GTS5-14-20_1023.DAT

4\) XTMPSIZE_GTS5-14-20_1025.DAT

5\) XTMPSIZE_GTS6-29-20_0712.DAT

6\) XTMPSIZE_GTS8-11-20_1305.DAT

7\) XTMPSIZE_GTS8-11-20_1318.DAT

8\) XTMPSIZE_QG_Demo.DAT

\+ Enter ?? : more actions & Help, ??? : Process Help

EM Extract Manager DPF Delete Package Parameter File

PMD Display/Edit Package Parameters CHD Change Host Directory

VSR Display VistA Size Report UNL Unlock Parameter File

RVQ Remote VistA Size Query

Select Action:Next Screen// <span class="mark">VSR \<Enter\></span> Display VistA Size Report

Select the XTMPSIZE\*.DAT Package Parameter file item number: (1-10): 8

XTMPSIZE_QG_Demo.DAT LOCK obtained.

Press Return to continue: <span class="mark">\<Enter\></span>

VistA Package Sizing Report

Do you want to display Sizing Information for ALL VistA Packages? NO// <span class="mark">YES</span>

Select which method to display the package size data:

<span class="mark">1. Sorted on PACKAGE NAME</span>

2\. Sorted on NUMBER of ROUTINES (Highest to Lowest)

3\. Sorted on TOTAL ROUTINE SIZE (Highest to Lowest)

4\. Delimited (^) Data, Sorted on PACKAGE NAME

5\. Delimited (^) Data with PARENT PKG, Sorted by PACKAGE NAME

Select VistA Size Report: <span class="mark">1 \<Enter\></span> SORT ON PKG NAMES

Compiling component totals for selected Package data file... -

Parameter file XTMPSIZE_QG_Demo.DAT LOCK released.

Press Return to continue: <span class="mark">\<Enter\></span>

VistA Package Size Report Sep 09, 2020@07:26:54 Page: 1 of 47

VistA Package Size Analysis Manager - Package Statistics

Version: 7.3 Build: 96

Default Directory: /srv/vista/*\<scd\>*/user/hfs/

Parameter file: XTMPSIZE_QG_Demo.DAT

VistA Application Sizing Information Sort Type: 1

Total

Application Rtn

(Namespace) Routines Size Files Fields Options Protocols RPCs Templates

================================================================================

ACCOUNTS RECEIVABLE

(PRCA) 605 2419858 110 2307 260 0 1 128

--------------------------------------------------------------------------------

ADVERSE REACTION TRACKING

(GMRA) 161 488568 13 273 44 18 0 4

--------------------------------------------------------------------------------

ALERTS

(XQAL) 15 88760 0 0 16 0 1 1

--------------------------------------------------------------------------------

ANTICOAGULATION MANAGEMENT

(ORAM) 8 84188 0 0 13 0 35 3

--------------------------------------------------------------------------------

ASISTS

(OOPS) 88 485014 32 551 10 0 65 0

--------------------------------------------------------------------------------

AUT

(AUT) 1 531 0 0 0 0 0 0

--------------------------------------------------------------------------------

AUTHORIZATION/SUBSCRIPTION

(USR) 36 92658 7 49 11 0 0 4

--------------------------------------------------------------------------------

AUTO REPLENISHMENT/WARD STOCK

\+ Enter ?? for more actions and Help

CTF Create Text File ER Email Rpt Attachment

RVQ Remote VistA Size Query <span class="mark">SHD Swap Header</span>

Select Action:Next Screen// <span class="mark">SHD \<Enter\></span> Swap Header

<span id="_Toc69721236" class="anchor"></span>Figure 93: SHD—Swap Header Action: Example 2

Select Action:Next Screen// <span class="mark">SHD \<Enter\></span> Swap Header

VistA Package Size Report Sep 09, 2020@07:27:06 Page: 3 of 47

Total

Application Rtn

(Namespace) Routines Size Files Fields Options Protocols RPCs Templates

\+

(PSGW) 105 252050 23 590 82 0 0 50

--------------------------------------------------------------------------------

AUTOMATED INFO COLLECTION SYS

(IBD) 851 4180518 101 1742 48 1 16 32

--------------------------------------------------------------------------------

AUTOMATED LAB INSTRUMENTS

(LA) 393 1380289 0 0 77 35 0 14

--------------------------------------------------------------------------------

AUTOMATED MED INFO EXCHANGE

(DVBA) 929 3525741 16 342 88 1 70 28

--------------------------------------------------------------------------------

BAR CODE EXPANSION

(MJCF) 0 0 0 0 0 0 0 0

--------------------------------------------------------------------------------

\+ Enter ?? for more actions

CTF Create Text File ER Email Rpt Attachment

RVQ Remote VistA Size Query SHD Swap Header

Select Action:Next Screen// <span class="mark">SHD \<Enter\></span> Swap Header

<span id="_Ref59433307" class="anchor"></span>Figure 94: SHD—Swap Header Action: Example 3

Select Action:Next Screen// <span class="mark">SHD \<Enter\></span> Swap Header

VistA Package Size Report Sep 09, 2020@07:27:17 Page: 3 of 47

VistA Package Size Analysis Manager - Package Statistics

Version: 7.3 Build: 96

Default Directory: /srv/vista/*\<scd\>*/user/hfs/

Parameter file: XTMPSIZE_QG_Demo.DAT

\+

(PSGW) 105 252050 23 590 82 0 0 50

--------------------------------------------------------------------------------

AUTOMATED INFO COLLECTION SYS

(IBD) 851 4180518 101 1742 48 1 16 32

--------------------------------------------------------------------------------

AUTOMATED LAB INSTRUMENTS

(LA) 393 1380289 0 0 77 35 0 14

--------------------------------------------------------------------------------

AUTOMATED MED INFO EXCHANGE

(DVBA) 929 3525741 16 342 88 1 70 28

--------------------------------------------------------------------------------

BAR CODE EXPANSION

(MJCF) 0 0 0 0 0 0 0 0

--------------------------------------------------------------------------------

\+ Enter ?? for more actions

CTF Create Text File ER Email Rpt Attachment

RVQ Remote VistA Size Query SHD Swap Header

# Appendix A—System MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The examples in this section are VistA Package Size Reporting Tool (VPSRT) messages that can be received by the user via VA MailMan. These messages are sent from VPSRT to notify the user of special package configuration circumstances.

## Warning Message—When Create Report of a Single Package Remotely

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref63061176" class="anchor"></span>Figure 95: VPSRT MailMan Message—Warning Message: When Create Report of a Single Package Remotely

Subj: PACKAGE REPORT NOTICE (*SITE1PRO*) ; Report process warning. \[#160374\]

10/08/20@12:19 2 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

Package Size Report warning for *SITE1PRO*.

Package: MY LOCAL PACKAGE...not found! Protocol count may be incorrect.

Enter message action (in IN basket): Ignore//

## Warning Message—When Create Report of All Packages Locally

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref63061184" class="anchor"></span>Figure 96: VPSRT MailMan Message—Warning Message: When Create Report of All Packages Locally

Subj: PACKAGE REPORT NOTICE (*SITE1PRO*) ; Report process warning. \[#160415\]

10/08/20@12:53 5 lines

From: VISTA PACKAGE SIZE ANALYSIS MANAGER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

Package Size Report warning for *SITE1PRO*.

The following package(s) are not found on this VistA.

(The number of protocols reported may be incorrect.)

\- MY LOCAL PACKAGE

\- ABC 4'' LABEL

Enter message action (in IN basket): Ignore//

## Clean Up Message—When Request Extract from Remote or Local VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc69721240" class="anchor"></span>Figure 97: VPSRT MailMan Message—Clean Up Message: When Request Extract from Remote or Local VistA

Subj: PACKAGE EXTRACT (FOR) ; data cleanup! \[#160427\] 10/08/20@13:36

3 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

Notice for Package Extract on FOR.

Data was cleaned up on ABC 4'' LABEL extract.

Double Quotes changed to 2 single quotes in the ABC 4'' LABEL Package name.

Enter message action (in IN basket): Ignore//