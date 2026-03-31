---
title: VistA Package Size Reporting Tool (VPSRT) Technical Manual (XT*7.3*143)
doc_type: TM
doc_label: Technical Manual
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
menu_options: 2
description: 
audience: 
keywords: 
  - strong
  - package
  - action
  - vista
  - table
  - xtvs
  - blockquote
  - size
  - contents
  - vpsrt
page_count: 0
word_count: 9466
section_count: 26
table_count: 9
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2021
revision_count: 1
revision_newest: 04/19/2021
revision_oldest: 04/19/2021
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Toolkit/xtvs_vpsrt_tm_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Toolkit/xtvs_vpsrt_tm_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=12"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>VistA Package Size Reporting Tool (VPSRT)

  Kernel Toolkit Patch XT\*7.3\*143

  Technical Manual (REDACTED)
---

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/001.png)

April 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

VistA Infrastructure (VI)

<span id="revision_history" class="anchor"></span>Revision History

| Date       | Revision | Description                                                                                                                                                 | Author                                                                        |
|------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| 04/19/2021 | 1.0      | Initial *VistA Package Size Reporting Tool (VPSRT) Kernel Toolkit Patch XT\*7.3\*143 Technical Manual* based on the template V. 1.1, released on July 2016. | VistA Infrastructure (VI) / VistA Kernel Development Team: Patch XU\*8.0\*143 |

<span id="_Ref449364879" class="anchor"></span>Table : Documentation Symbol Descriptions

Table of Contents

<span id="_Toc69717855" class="anchor"></span>List of Figures

<span id="_Toc69717856" class="anchor"></span>List of Tables

<span id="_Toc97018442" class="anchor"></span>Orientation

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

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/002.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of this software for *non*-VistA use should be referred to the VistA site’s local Office of Information and Technology Field Office (OITFO).

Documentation Disclaimer

This manual provides an overall explanation of VPSRT and the functionality contained in VPSRT; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) VistA Development Intranet website.

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/003.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/004.png)       | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/005.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Ref373317182" class="anchor"></span>Table : VistA M Server—Minimum Software Requirements

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

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

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

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/007.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/008.png) NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/009.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment

References

Readers who wish to learn more about VistA Package Size Reporting Tool (VPSRT) should consult the following:

- *VistA Package Size Reporting Tool (VPSRT) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)*
- *VistA Package Size Reporting Tool (VPSRT) User Guide*
- *VistA Package Size Reporting Tool (VPSRT) Technical Manual* (this manual)

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) website: <http://www.va.gov/vdl/>

The VPSRT documentation is located on the VDL at: [<u>VA Software Document Library - Kernel Toolkit</u>](https://www.va.gov/vdl/application.asp?appid=12)

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Namespace](#namespace)
  - [System Requirements](#system-requirements)
    - [Hardware Requirements](#hardware-requirements)
    - [Software Requirements](#software-requirements)
    - [Database Requirements](#database-requirements)
  - [System Setup and Configuration](#system-setup-and-configuration)
    - [Allocate XTVS EDITOR Security Key](#allocate-xtvs-editor-security-key)
    - [Review Configure XTVS PKG EXTRACT SERVER Option Configuration](#review-configure-xtvs-pkg-extract-server-option-configuration)
    - [Set Default Directory](#set-default-directory)
- [Files and Templates](#files-and-templates)
  - [Files](#files)
  - [Templates](#templates)
- [Routines](#routines)
- [Exported Options and Protocols](#exported-options-and-protocols)
  - [Options](#options)
  - [Protocols](#protocols)
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [Integration Control Registrations](#integration-control-registrations)
  - [Application Programming Interfaces](#application-programming-interfaces)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [HL7 Messaging](#hl7-messaging)
  - [Web Services](#web-services)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
  - [Internal Relationships](#internal-relationships)
  - [Software-Wide Variables](#software-wide-variables)
- [Security](#security)
  - [Security Menus and Options](#security-menus-and-options)
  - [Security Keys and Roles](#security-keys-and-roles)
  - [File Security](#file-security)
  - [Electronic Signatures](#electronic-signatures)
  - [Secure Data Transmission](#secure-data-transmission)
- [Archiving](#archiving)
- [Non-Standard Cross-References](#non-standard-cross-references)
- [Troubleshooting](#troubleshooting)
  - [Common Issues and Resolutions](#common-issues-and-resolutions)
  - [Frequently Asked Questions (FAQs)](#frequently-asked-questions-faqs)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
  - [Enterprise Service Desk and Organizational Contacts](#enterprise-service-desk-and-organizational-contacts)
    - [VA Enterprise Service Desk](#va-enterprise-service-desk)
    - [Tier 2](#tier-2)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
The *VistA Package Size Reporting Tool (VPSRT) Kernel Toolkit Patch XT\*7.3\*143 Technical Manual* provides descriptive information and instructions on the use of the VPSRT software within the VA’s Veterans Health Information Systems and Technology Architecture (VistA) environment.
It acquaints users with the utilities, software structure, and functionality of the VPSRT, including information about the files, options, and routines that comprise this software. It also has information about the software’s structure and recommendations regarding its efficient use. Additional information on security, management features, and other requirements is also included.
The intended audience for this document is:
- System Administrators—System administrators at Department of Veterans Affairs (VA) regional and local sites who are responsible for computer management and system security on the VistA M Servers.
- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- Product Support (PS).

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide sufficient technical information about the software for developers and technical personnel to operate and maintain the software with only minimal assistance from Product Support staff.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XT\*7.3\*143 enhances Kernel Toolkit by adding a legacy VistA package definition and size reporting system. This enhancement does *not* measure package use or capacity requirements. It provides statistics on the technical footprint for a VistA Package, where “technical footprint” is the following:

- Number of routines
- Size of routines
- Number of files
- Number of fields
- Number of options
- Number of protocols
- Number of remote procedure calls (RPCs)
- Number of VA FileMan templates included in the reported package

VPSRT is new and does *not* exist in Production VistA prior to installation of Patch XT\*7.3\*143. The report depends on accurate package definitions to provide correct statistics for a package.

<span id="_Ref480264132" class="anchor"></span>Figure : VPS Reporting Tool—Integration

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/010.png)

<span id="_Ref480957623" class="anchor"></span>Figure : VPS Reporting Tool—System Layers

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/011.png)

<span id="_Ref480273639" class="anchor"></span>Figure : VPS Reporting Tool—Extract Manager Use Cases

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/012.png)

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*143 Patch Description (PD) document and the *VPSRT Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)* provides detailed information regarding the installation of the VPSRT. It also contains requirements and recommendations regarding how the VPSRT should be configured.

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/013.png) REF: Before attempting to install the VPSRT, be sure to read the Kernel Toolkit Patch XT\*7.3\*143 PD and the VPSRT DIBRG.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPSRT namespace is XTVS.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*143 should be installed on FORUM and all VistA M Servers.

All VistA Infrastructure patches *must* be installed within 30 days of national release.

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific hardware requirements for installation of Kernel Toolkit Patch XT\*7.3\*143 as it runs in a typical VistA M Server environment. There is also no need for specific hardware to assist in the deployment of Kernel Toolkit Patch XT\*7.3\*143.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of Kernel Toolkit Patch XT\*7.3\*143 is a typical Kernel Installation & Distribution System (KIDS) install of a VistA patch in the VistA M Server environment.

<u>Table 2</u> lists the *minimum* software requirements for the VistA M Server in order to install and use Kernel Toolkit Patch XT\*7.3\*143:

| Software       | Version | Description                                                                             |
|----------------|---------|-----------------------------------------------------------------------------------------|
| Kernel         | 8.0     | VistA Legacy Software [<sup>\*</sup>Fully Patched M Accounts](#fully_patched_note). |
| Kernel Toolkit | 7.3     | VistA Legacy Software [<sup>\*</sup>Fully Patched M Accounts](#fully_patched_note). |
| VA FileMan     | 22.2    | VistA Legacy Software [<sup>\*</sup>Fully Patched M Accounts](#fully_patched_note). |
| MailMan        | 8.0     | VistA Legacy Software [<sup>\*</sup>Fully Patched M Accounts](#fully_patched_note). |

<span id="_Toc69717911" class="anchor"></span>Table : VPSRT—ListMan Templates

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/014.png) <span id="fully_patched_note" class="anchor"></span><sup>\*</sup>NOTE: All software listed in <u>Table 2</u> *must* be fully patched, which means that all patches *must* be installed up to the most recent patch released at the time of the installation of Kernel Toolkit Patch XT\*7.3\*143.

### Database Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 uses the already installed VA FileMan database. VPSRT does *not* create any new databases.

## System Setup and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Allocate XTVS EDITOR Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Allocation of Security Keys \[XUKEYALL\] option to allocate the XTVS EDITOR security key to the users who manage package parameters used to create the package size reports. Users that only need to create package size reports do *not* need this security key.

To allocate the XTVS EDITOR security key, do the following:

1.  Select the System Manager Menu \[EVE\].
2.  Select the Menu Management \[XUMAINT\] menu.
3.  Select the Key Management \[XUKEYMGMT\] menu.
4.  Select the Allocation of Security Keys \[XUKEYALL\] option.
5.  At the “Allocate key:” prompt enter XTVS EDITOR.

### Review Configure XTVS PKG EXTRACT SERVER Option Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Process XTVS Request Message \[XTVS PKG EXTRACT SERVER\] option responds to remote VistA requests to return size reports; and on FORUM, PACKAGE (#9.4) file extracts. System administrators can decide to prevent a remote user from running a report on the VistA and returning it to the requester. This option can help remote support staff assist the site.

The SERVER ACTION (#221) field in the OPTION (#19) file is set to “RUN IMMEDIATELY” for the XTVS PKG EXTRACT SERVER option when the patch is installed. Configuration of this option allows remote support staff to receive requested size messages (or in the case of FORUM, PACKAGE \[#9.4\] file extract messages in addition to package size messages).

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/015.png) CAUTION: Production system administrators should review the setting and determine whether to leave the option configured to “RUN IMMEDIATELY” or change the configuration. The SERVER ACTION (#221) field can be set to one of the following:

- R—RUN IMMEDIATELY
- Q—QUEUE SERVER ROUTINE
- N—NOTIFY MAIL GROUP (DO NOT RUN)
- I—IGNORE REQUESTS

To change the SERVER ACTION (#221) field on the XTVS PKG EXTRACT SERVER option:

Use the FileMan ENTER OR EDIT FILE ENTRIES \[DIEDIT\] option to change the value of the SERVER ACTION (#221) field in the OPTION (#19) file.

### Set Default Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the “VistA Package Size Analysis Manager” screen, set the Package Parameter file (i.e., XTMPSIZE\*.DAT) default directory as follows:

1.  Invoke the VistA Package Extract Manager \[XTVS VISTA PACKAGE EXTRACT MGR\] option.
2.  At the “Do you want to Display XTMPSIZE\*.BAK (backup files)? NO//” prompt, press Enter to accept the NO default response.
3.  From the “VistA Package Size Analysis Manager” screen, select the CHD—Change Host Directory action, as shown in <u>Figure 4</u>.

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/016.png) NOTE: The CHD—Change Host Directory action is locked with the XTVS EDITOR security key.

4.  Set the “VistA Package Size default directory” to a directory on the VistA server host system that the user, who will be managing package parameters and creating package size reports, has READ and WRITE privileges.

<span id="_Ref480957390" class="anchor"></span>Figure 4: CHD—Change Host Directory Action: Example

Vista Package Size Manager Apr 14, 2017@14:07:44 Page: 3 of 4

<span class="mark">VistA Package Size Analysis Manager</span>

Version: 1 Build: 0

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

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

--------------------------------------------------------------------------

VistA Package Size default directory VA3\$:\[XUUSER\]

--------------------------------------------------------------------------

VistA Package Size default directory: VA3\$:\[XUUSER\]//

# Files and Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new globals, files, or fields exported with VPSRT and Kernel Toolkit Patch XT\*7.3\*143.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 4</u> lists the ListMan templates exported with VPSRT and Kernel Toolkit Patch XT\*7.3\*143. A brief description of the templates is provided.

| Template                      | Description                                                                                                     |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------|
| XTVS PACKAGE MANAGER          | This template uses the VistA Package Mgr Menu \[XTVS PACKAGE MANAGER MENU\] menu protocol.                  |
| XTVS PKG EXT CRT PARAM        | This template uses the New Parameter File Menu \[XTVS PKG MGR NEW PARAM MENU\] menu protocol.               |
| XTVS PKG MGR EXT DISP         | This template uses the Extract Display/Delete \[XTVS PKG MGR EXT DISP MENU\] menu protocol.                 |
| XTVS PKG MGR EXTRACT MNGR     | This template uses the Extract Manager Menu \[XTVS PKG MGR EXTRACT MENU\] menu protocol.                    |
| XTVS PKG MGR PARAM CAPTN DISP | This template uses the Parameter Caption Display Menu \[XTVS PKG MGR PARAM DISP CAPTN MENU\] menu protocol. |
| XTVS PKG MGR PARAM COMPARE    | This template uses the Compare Parameters to Existing File \[XTVS PKG MGR PARAM CMPR MENU\] menu protocol.  |
| XTVS PKG MGR PARAM DISPLAY    | This template uses the Package Parameter Display Menu \[XTVS PKG MGR PARAM DISP MENU\] menu protocol.       |
| XTVS PKG MGR PARAM ERROR DISP | This template uses the List Package Errors \[XTVS PKG MGR PARAM ERROR MENU\] menu protocol.                 |
| XTVS PKG MGR VISTA SIZE RPT   | This template uses the VistA Size Report Menu \[XTVS PKG MGR RPT MENU\] menu protocol.                      |

<span id="_Ref473123184" class="anchor"></span>Table : VPSRT—Routines

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 4</u> lists the routines exported with VPSRT and Kernel Toolkit Patch XT\*7.3\*143. A brief description of the routines is provided.

| Routine  | Description                                                                       |
|----------|-----------------------------------------------------------------------------------|
| XT73A143 | Pre-transportation routine for XT\*7.3\*143.                                      |
| XT73P143 | Post-transportation routine for XT\*7.3\*143.                                     |
| XTVSCP   | Protocol code for XTVS PKG EXT CRT PARAM.                                         |
| XTVSHELP | This routine contains Help text.                                                  |
| XTVSHLP1 | This routine contains Help text.                                                  |
| XTVSHLP2 | This routine contains Help text.                                                  |
| XTVSLAPI | API code.                                                                         |
| XTVSLDE  | Protocol code for XTVS PKG MGR EXT DISP ACTION.                                   |
| XTVSLM   | Protocol code for XTVS PACKAGE MANAGER.                                           |
| XTVSLN   | Protocol code for XTVS PKG MGR EXTRACT MNGR.                                      |
| XTVSLNA1 | Protocol code for XTVS PKG MGR EXTRACT MNGR \#2.                                  |
| XTVSLP   | Protocol code for XTVS PKG MGR PARAM DISPLAY.                                     |
| XTVSLPC  | Protocol code for XTVS PKG MGR PARAM COMPARE.                                     |
| XTVSLPD1 | API code \#1 for XTVS PKG MGR PARAM COMPARE protocol.                             |
| XTVSLPD2 | API code \#2 for XTVS PKG MGR PARAM COMPARE protocol.                             |
| XTVSLPDC | Protocol code for XTVS PKG MGR PARAM CAPTN DISP.                                  |
| XTVSLPER | Protocol code for XTVS PKG MGR PARAM ERROR DISP.                                  |
| XTVSLPR1 | API code for XTVS PKG MGR PARAM ERROR DISP protocol.                              |
| XTVSLR   | Protocol code for XTVS VISTA SIZE RPT.                                            |
| XTVSRFL  | API code for XTVS VISTA SIZE RPT protocol.                                        |
| XTVSRFL1 | API code for XTVS VISTA SIZE RPT protocol and the XTVS PKG EXTRACT SERVER option. |
| XTVSSVR  | XTVS PKG EXTRACT SERVER option code.                                              |

<span id="_Ref324243012" class="anchor"></span>Table : Options—Exported VPSRT Options

# Exported Options and Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 5</u> list the XTVS namespaced options that are distributed with VPSRT (listed alphabetically by option name):

<table>
<caption><p><span id="_Ref69128449" class="anchor"></span>Table : Protocols—Exported VPSRT Protocols</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Text</th>
<th>Type</th>
<th>Routine / Action / RPC / Other<br />
(Based on Type)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XTVS PKG EXTRACT SERVER</td>
<td><strong>Process XTVS Request Message</strong></td>
<td>Server</td>
<td><strong>SRVREXT^XTVSSVR</strong></td>
<td><p>This server option processes a Kernel Toolkit VistA Package Size request message. The VistA Package Size Reporting Tool (VPSRT) can request the following information from a remote VistA via a request message to this option:</p>
<ul>
<li><blockquote>
<p>Size report for a single VistA package on another production VistA.</p>
</blockquote></li>
<li><blockquote>
<p>Package file extract from any production VistA. Optionally, a size a report for all packages can be requested from FORUM in addition to a Package file extract.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>XTVS PKG MGR EXT PACKAGE MSG</td>
<td><strong>Send Package File Extract via Packman</strong></td>
<td>Run Routine</td>
<td><strong>EMAILEXT^XTVSLAPI</strong></td>
<td><p>This option does the following:</p>
<ul>
<li><blockquote>
<p>Extracts the VistA Package Size relevant data from the PACKAGE (#9.4) file.</p>
</blockquote></li>
<li><blockquote>
<p>Loads it into an <strong>^XTMP</strong> global.</p>
</blockquote></li>
<li><blockquote>
<p>Bundles the <strong>^XTMP</strong> global in a PackMan message.</p>
</blockquote></li>
<li><blockquote>
<p>Allows the user to send it to a VA MailMan email address on a VistA environment.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>XTVS VISTA PACKAGE EXTRACT MGR</td>
<td><strong>VistA Package Extract Manager</strong></td>
<td>Run Routine</td>
<td><strong>EN^XTVSLM</strong></td>
<td>This option invokes the “<strong>VistA Package Size Analysis Manager</strong>” screen (aka <strong>VistA Package Extract &amp; Rpt Manager</strong>).</td>
</tr>
</tbody>
</table>

<span id="_Ref69128449" class="anchor"></span>Table : Protocols—Exported VPSRT Protocols

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 6</u> list the XTVS namespaced protocols that are distributed with VPSRT (listed alphabetically by protocol name):

<table>
<caption><p><span id="_Ref355083482" class="anchor"></span>Table : VPSRT—Security Keys</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>Protocol Name</th>
<th>Option Text</th>
<th>Type</th>
<th>Routine / Action / RPC / Other<br />
(Based on Type)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XTVS BLANK 1</td>
<td>N/A</td>
<td>Action</td>
<td>N/A</td>
<td>This protocol is used to format spaces in ListMan menu lists. It is <em>not</em> a user-selectable action.</td>
</tr>
<tr class="even">
<td>XTVS PACKAGE MANAGER MENU</td>
<td><strong>VistA Package Mgr Menu</strong></td>
<td>Menu</td>
<td>Header:<br />
<strong>D SHOW^VALM</strong></td>
<td><p>This menu allows access to VistA Package Manager actions. The <strong>XTVS PACKAGE MANAGER</strong> List Manager template uses this menu protocol. This menu includes the following actions:</p>
<ul>
<li><blockquote>
<p><strong>XTVS PKG MGR EXT MNGR ACTION</strong><br />
MNEMONIC: <strong>EM</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR PARAM DISP/EDIT ACTION</strong><br />
MNEMONIC: <strong>PMD</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR VISTA SIZE RPT</strong><br />
MNEMONIC: <strong>VSR</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR PARAM FILE DELETE ACTION</strong><br />
MNEMONIC: <strong>DPF</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS SITE PARAMETERS</strong><br />
MNEMONIC: <strong>CHD</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR PARAM UNLOCK ACTION</strong><br />
MNEMONIC: <strong>UNL</strong></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>XTVS PKG EXT CRT PARAM ACTION</td>
<td><strong>CXP—Convert Extract to Parameter List</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D CRTPARM^XTVSLN</strong></td>
<td>Prompts the user for the <strong>$JOB</strong> Process ID of the extract and displays the Extract Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) on the “<strong>VistA Package Size Analysis Manager – Package Parameters</strong>” screen.</td>
</tr>
<tr class="even">
<td>XTVS PKG EXT DISP CORRECTIONS ACTION</td>
<td><strong>DPC—Display Parameter Corrections</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>DO REDISCRT^XTVSCP</strong></td>
<td>Allows users to review the changes the <strong>CXP—Convert Extract to Parameter List</strong> action made to the data written in the Package Parameters list when it was created from the raw PACKAGE (#9.4) file extract.</td>
</tr>
<tr class="odd">
<td>XTVS PKG EXT DISP DEL ACTION</td>
<td><strong>DE—Delete Displayed Extract</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D DEL^XTVSLDE</strong></td>
<td><p>Allows the user to delete the <strong>^XTMP(“XTVS”)</strong> global extract displayed on the “<strong>VistA Package Size Analysis Manager - Display Extract</strong>” screen. This action prompts the user to confirm deletion of the <strong>^XTMP</strong> global displayed in the list:</p>
<ul>
<li><blockquote>
<p><strong>NO—</strong>Displays a message and redisplays the extract global.</p>
</blockquote></li>
<li><blockquote>
<p><strong>YES—</strong>Deletes the global and returns to the “<strong>VistA Package Size Analysis Manager - Extract Manager</strong>” screen.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>XTVS PKG EXT EMAIL ACTION</td>
<td><strong>ME—Email Extract Global</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D EEXT^XTVSLN</strong></td>
<td><p>Prompts the user for the <strong>$JOB</strong> Process ID number of the extract to mail and then prompts the user for recipients.</p>
<p>This serves as an alternate to the <strong>Send Package File Extract via Packman</strong> [XTVS PKG MGR EXT PACKAGE MSG] option.</p></td>
</tr>
<tr class="odd">
<td>XTVS PKG EXT PARAM WRT ACTION</td>
<td><strong>WPF—Write Parameter List to File</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D WRPARMFL^XTVSCP</strong></td>
<td><p>Creates a Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) from the Package Parameters displayed with the following file name format:</p>
<p><strong>XTMPSIZE_<em>&lt;user initials&gt;&lt;mm-dd-yy_hhmm&gt;</em>.DAT</strong></p>
<p>It is written to the VistA Package Size default directory for further editing with the VistA Package Analysis Manager.</p></td>
</tr>
<tr class="even">
<td>XTVS PKG EXT QUERY REMOTE ACTION</td>
<td><strong>REQ—Remote VistA Extract Query</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D QRYEXT^XTVSLN</strong></td>
<td>Allows a user to request a Package file extract from any Production VistA. If a Package file extract is requested from FORUM, the user can also request a VistA Package size report for all packages on FORUM.</td>
</tr>
<tr class="odd">
<td>XTVS PKG EXT REDISP PARAM ACTION</td>
<td><strong>RPL—Display Parameter List</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>DO REDISPRM^XTVSCP</strong></td>
<td>Executed after users review corrections with the <strong>DPC—Display Parameter Corrections</strong> action. It redisplays the package parameters as defined by the selected package extract file.</td>
</tr>
<tr class="even">
<td>XTVS PKG EXTRACT CREATE ACTION</td>
<td><strong>CE—Extract Package Data</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D PEXT^XTVSLN</strong></td>
<td>Extracts PACKAGE (#9.4) file data into <strong>^XTMP(“XTVS”)</strong> global.</td>
</tr>
<tr class="odd">
<td>XTVS PKG EXTRACT DEL ACTION</td>
<td><strong>DEL—Delete Extract</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D DE^XTVSLN</strong></td>
<td>Prompts the user for the <strong>$JOB</strong> Process ID number of the extract and deletes the <strong>^XTMP(“XTSIZE”)</strong> global extract.</td>
</tr>
<tr class="even">
<td>XTVS PKG MGR DEL PACKAGE PARM ACTION</td>
<td><strong>DPE—Delete Package Parameter Entry</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D DELPMPKG^XTVSLPDC</strong></td>
<td>Prompts users to enter a package to delete. The user is reminded that deletion removes the package from the size report created with the Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) being edited.</td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR EDIT PACKAGE PARM ACTION</td>
<td><strong>EPP—Edit Package Parameters</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D EDITPRM^XTVSLPDC</strong></td>
<td>Prompts users to enter a package to add/edit. The user is then prompted to edit the parameters required for Package Size Reporting.</td>
</tr>
<tr class="even">
<td>XTVS PKG MGR EMAIL OVRLAP RPT ACTION</td>
<td><strong>EL—Email Displayed Report</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D ERPT^XTVSLPER</strong></td>
<td><p>Prompts the user for email recipients to send the displayed report. This action allows the report to be sent to a specific Package SME for review.</p>
<p>![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/017.png) <strong>NOTE:</strong> This action sends the displayed report. For example, if the “<strong>VistA Package Size Analysis Manager – File Overlap</strong>” screen is displayed, then the “File Overlap” report is sent to the recipient.</p></td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR EXT DISP ACTION</td>
<td><strong>ED—Display Extract</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D ED^XTVSLN</strong></td>
<td>Allows users to enter the <strong>$J</strong> Process number for the <strong>^XTMP(“XTVS”)</strong> global and display its data. The “<strong>VistA Package Size Analysis Manager – Display Extract</strong>” screen is displayed and presents a report of each Package with captioned parameter data. Use this report to review the extracted PACKAGE (#9.4) file data to determine what parameter changes and corrections need to be made.</td>
</tr>
<tr class="even">
<td>XTVS PKG MGR EXT DISP MENU</td>
<td><strong>Extract Display/Delete</strong></td>
<td>Menu</td>
<td>HEADER:<br />
<strong>D SHOW^VALM</strong></td>
<td><p>This action displays a selected extract and related actions for the extract. The <strong>XTVS PKG MGR EXT DISP</strong> List Manager template uses this menu protocol. This menu includes the following actions:</p>
<ul>
<li><blockquote>
<p><strong>XTVS PKG EXT DISP DEL ACTION</strong><br />
MNEMONIC: <strong>DE</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>VALM BLANK 1</strong></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR EXT MNGR ACTION</td>
<td><strong>EM—Extract Manager</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D EA^XTVSLM</strong></td>
<td><p>Invokes a utility for managing the <strong>^XTMP(“XTSIZE”)</strong> global.</p>
<p>This action is locked with the <strong>XTVS EDITOR</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XTVS PKG MGR EXTRACT MENU</td>
<td><strong>Extract Manager Menu</strong></td>
<td>Menu</td>
<td>HEADER:<br />
<strong>D SHOW^VALM</strong></td>
<td><p>This menu allows access to the Package File Extract tools. The <strong>XTVS PKG MGR EXTRACT MNGR</strong> List Manager template uses this menu protocol. This menu includes the following actions:</p>
<ul>
<li><blockquote>
<p><strong>XTVS PKG EXTRACT CREATE ACTION</strong><br />
MNEMONIC: <strong>CE</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR EXT DISP ACTION</strong><br />
MNEMONIC: <strong>ED</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG EXT EMAIL ACTION</strong><br />
MNEMONIC: <strong>ME</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG EXTRACT DEL ACTION</strong><br />
MNEMONIC: <strong>DEL</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG EXT CRT PARAM ACTION</strong><br />
MNEMONIC: <strong>CXP</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>VALM BLANK 1</strong></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR FILE OVERLAP ACTION</td>
<td><strong>FL—Display File Overlap List</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D DRNGERR^XTVSLPER</strong></td>
<td>Sorts out and displays only the packages that have file overlaps (intersections). The “<strong>VistA Package Size Analysis Manager – File Overlap</strong>” screen is then displayed.</td>
</tr>
<tr class="even">
<td>XTVS PKG MGR NEW PARAM MAIL ACTION</td>
<td><strong>EPC—Email Corrections Rpt &amp; Parameters</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D SNDNPFLE^XTVSCP</strong></td>
<td>Prompts the user for recipients and sends the Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) as an attachment and the corrections report in the mail message. Use this information as a starting point for correcting package information in the Parameters file.</td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR NEW PARAM MENU</td>
<td><strong>New Parameter File Menu</strong></td>
<td>Menu</td>
<td>HEADER:<br />
<strong>D SHOW^VALM</strong></td>
<td><p>This menu allows access to the new parameter file management actions. The <strong>XTVS PKG EXT CRT PARAM</strong> List Manager template uses this menu protocol. This menu includes the following actions:</p>
<ul>
<li><blockquote>
<p><strong>XTVS PKG EXT REDISP PARAM ACTION</strong><br />
MNEMONIC: <strong>RPL</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG EXT DISP CORRECTIONS ACTION</strong><br />
MNEMONIC: <strong>DPC</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG EXT PARAM WRT ACTION</strong><br />
MNEMONIC: <strong>WPF</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR NEW PARAM MAIL ACTION</strong><br />
MNEMONIC: <strong>EPC</strong></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>XTVS PKG MGR PARAM CMPR MENU</td>
<td><strong>Compare Parameters to Existing File</strong></td>
<td>Menu</td>
<td>HEADER:<br />
<strong>D SHOW^VALM</strong></td>
<td><p>This action allows selection of an existing <strong>XTMPSIZE.DAT</strong> file for comparison to a displayed file. Differences are reported in a ListMan user interface. The <strong>XTVS PKG MGR PARAM COMPARE</strong> List Manager template uses this menu protocol. This menu includes the following actions:</p>
<ul>
<li><blockquote>
<p><strong>XTVS PKG MGR PARAM COMPR MAIL ACTION</strong><br />
MNEMONIC: <strong>ECR</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>VALM BLANK 2</strong></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR PARAM COMPARE ACTION</td>
<td><strong>CPF—Parameter File Comparison</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D PARAMCMP^XTVSLP</strong></td>
<td>Prompts the user to select a Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) for comparison. Displays a report of differences between the new Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) and the selected Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>).</td>
</tr>
<tr class="even">
<td>XTVS PKG MGR PARAM COMPR MAIL ACTION</td>
<td><strong>ECR—Email Comparison Report</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D MAILRPT^XTVSLPC</strong></td>
<td>Allows users to email a comparison report on the “<strong>VistA Package Size Analysis Manager - Parameter Compare</strong>” screen using VistA MailMan.</td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR PARAM DATA MAP HELP ACTION</td>
<td><strong>DM—Display Parameter File Data Map</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D PARAMAP^XTVSLP</strong></td>
<td>Displays a data map of the Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) list data.</td>
</tr>
<tr class="even">
<td>XTVS PKG MGR PARAM DISP CAPTION ACTION</td>
<td><strong>DC—Display Captioned Parameters</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D PARAMRPT^XTVSLP</strong></td>
<td>Displays the list of packages with captioned data elements. It also supports Package Parameter editing actions.</td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR PARAM DISP CAPTN MENU</td>
<td><strong>Parameter Caption Display Menu</strong></td>
<td>Menu</td>
<td>HEADER:<br />
<strong>D SHOW^VALM</strong></td>
<td><p>This Menu protocol contains the list of actions available from the <strong>XTVS PKG MGR PARAM CAPTN DISP</strong> list template. This menu includes the following actions:</p>
<ul>
<li><blockquote>
<p><strong>XTVS PKG MGR EDIT PACKAGE PARM ACTION</strong><br />
MNEMONIC: <strong>EPP</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR DEL PACKAGE PARM ACTION</strong><br />
MNEMONIC: <strong>DPE</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR SAVE PACKAGE PARM ACTION</strong><br />
MNEMONIC: <strong>SPP</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>VALM BLANK 1</strong></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>XTVS PKG MGR PARAM DISP MENU</td>
<td><strong>Package Parameter Display Menu</strong></td>
<td>Menu</td>
<td>HEADER:<br />
<strong>D SHOW^VALM</strong></td>
<td><p>This Menu protocol contains the list of actions available from the <strong>XTVS PKG MGR PARAM DISPLAY</strong> list template. This menu includes the following actions:</p>
<ul>
<li><blockquote>
<p><strong>XTVS PKG MGR PARAM ERR DISP ACTION</strong><br />
MNEMONIC: <strong>DO</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR PARAM DATA MAP HELP ACTION</strong><br />
MNEMONIC: <strong>DM</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR PARAM DISP CAPTION ACTION</strong><br />
MNEMONIC: <strong>DC</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR PARAM COMPARE ACTION</strong><br />
MNEMONIC: <strong>CPF</strong></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR PARAM DISP/EDIT ACTION</td>
<td><strong>PMD—Display/Edit Package Parameters</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D PRMD^XTVSLM</strong></td>
<td><p>This action prompts the user to select a <strong>XTMPSIZE*.DAT</strong> Package Parameter file form a list of Package Parameter files (i.e., <strong>XTMPSIZE*.DAT</strong>). It then invokes the “<strong>VistA Package Size Analysis Manager – Parameter Display</strong>” screen for editing and managing Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) data.</p>
<p>This action is locked with the <strong>XTVS EDITOR</strong> security key.</p></td>
</tr>
<tr class="even">
<td>XTVS PKG MGR PARAM ERR DISP ACTION</td>
<td><strong>DO—Display Package Overlap List</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D PKGERR^XTVSLP</strong></td>
<td>Displays the “<strong>VistA Package Size Analysis Manager – Prefix/File Overlap</strong>” screen. It includes data analysis support actions that allow users to review PACKAGE (#9.4) file and PREFIX (#1) field (i.e., unique namespace prefix assigned to the package) overlap information.</td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR PARAM ERROR MENU</td>
<td><strong>List Package Errors</strong></td>
<td>Menu</td>
<td>HEADER:<br />
<strong>D SHOW^VALM</strong></td>
<td><p>This protocol allows access to the Package Parameter File error reporting actions. The <strong>XTVS PKG MGR PARAM ERROR DISP</strong> List Manager template uses this menu protocol. This menu includes the following actions:</p>
<ul>
<li><blockquote>
<p><strong>XTVS PKG MGR PREFIX OVERLAP ACTION</strong><br />
MNEMONIC: <strong>PL</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR FILE OVERLAP ACTION</strong><br />
MNEMONIC: <strong>FL</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR EMAIL OVRLAP RPT ACTION</strong><br />
MNEMONIC: <strong>EL</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR PARAM OVRLP REDISP ACTION</strong><br />
MNEMONIC: <strong>RL</strong></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>XTVS PKG MGR PARAM FILE DELETE ACTION</td>
<td><strong>DPF—Delete Package Parameter File</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D DELPRM^XTVSLM</strong></td>
<td><p>Deletes from the system a selected Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) listed on the “<strong>VistA Package Size Analysis Manager</strong>” screen.</p>
<p>This action is locked with the <strong>XTVS EDITOR</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR PARAM OVRLP REDISP ACTION</td>
<td><strong>RL—[Re] Display Package Overlap List</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D CMBERR^XTVSLPER</strong></td>
<td>Displays both prefix (namespace) and file overlaps for packages that intersect. The “<strong>VistA Package Size Analysis Manager – Prefix/File Overlap</strong>” screen is re-displayed.</td>
</tr>
<tr class="even">
<td>XTVS PKG MGR PARAM UNLOCK ACTION</td>
<td><strong>UNL—Unlock Parameter File</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D RMVLCK^XTVSLM</strong></td>
<td><p>Displays a list of lock files (<strong>.LCK</strong>) for Parameter files and prompts the user for the number of the Extract Package Parameter file (i.e., <strong>XTMPSIZE*.LCK</strong>) to delete. Deletion of a lock file unlocks the parameter file. The lock files have the following file name format:</p>
<p><strong>XTMPSIZE_&lt;user initials&gt;&lt;mm-dd-yy_hhmm&gt;.LCK</strong></p>
<p>This action is locked with the <strong>XTVS EDITOR</strong> security key.</p></td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR PREFIX OVERLAP ACTION</td>
<td><strong>PL—Display Prefix Overlap List</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>DO DPFXERR^XTVSLPER</strong></td>
<td>Sorts out and displays only the packages that have prefix (namespace) overlap (intersections). The “<strong>VistA Package Size Analysis Manager – Prefix Overlap</strong>” screen is displayed.</td>
</tr>
<tr class="even">
<td>XTVS PKG MGR RPT MAIL ACTION</td>
<td><strong>ER—Email Rpt Attachment</strong></td>
<td>Action</td>
<td><p>ENTRY ACTION:<br />
<strong>D SNDEXT^XTVSLAPI("VistA Size Report",DUZ,"^TMP(""XTVS PKG MGR R</strong></p>
<p><strong>PT"","_$J_")")</strong></p></td>
<td>Prompts the user for email addresses to receive the report.</td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR RPT MENU</td>
<td><strong>VistA Size Report Menu</strong></td>
<td>Menu</td>
<td>HEADER:<br />
<strong>D SHOW^VALM</strong></td>
<td><p>This menu allows access to VistA Package Manager statistics report actions. The <strong>XTVS PKG MGR VISTA SIZE RPT</strong> List Manager template uses this menu protocol. This menu includes the following actions:</p>
<ul>
<li><blockquote>
<p><strong>XTVS PKG MGR RPT WRT ACTION</strong><br />
MNEMONIC: <strong>CTF</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTVS PKG MGR RPT MAIL ACTION</strong><br />
MNEMONIC: <strong>ER</strong></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>XTVS PKG MGR RPT QUERY REMOTE ACTION</td>
<td><strong>RVQ—Remote VistA Size Query</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D REMREQ^XTVSLR</strong></td>
<td><p>Prompts the user for a package and a VistA domain to request a size report for the selected package. A size report query message is sent to the selected VistA domain. These actions are available from the “<strong>VistA Package Size Analysis Manager</strong>” and the “<strong>VistA Package Size Analysis Manager - Package Statistics</strong>” screens:</p>
<ul>
<li><blockquote>
<p><strong>“VistA Package Size Analysis Manager” Screen—</strong>When the <strong>RVQ</strong> action is run from this screen, the request prompts the user to select a Package Parameter file and sends the request to the remote VistA, so the report can be created on the remote VistA.</p>
</blockquote></li>
<li><blockquote>
<p><strong>“VistA Package Size Analysis Manager - Package Statistics” Screen—</strong>When the <strong>RVQ</strong> action is run from this screen, the request sends the Parameter file used to create the displayed report to the remote VistA, so that an apples-to-apples size report is returned from the remote VistA. That is the same package parameters that are used to create the report.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR RPT WRT ACTION</td>
<td><strong>CTF—Create Text File</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D TEXTFILE^XTVSLR</strong></td>
<td><p>Prompts users to enter the following:</p>
<ul>
<li><blockquote>
<p>Directory to write the report file. The default is the VistA Package Size default directory.</p>
</blockquote></li>
<li><blockquote>
<p>Name of the host file that will contain the report. The default name is:</p>
</blockquote></li>
</ul>
<p><strong>VistAPkgSize_&lt;VA FileMan internal date/time&gt;.txt</strong></p></td>
</tr>
<tr class="even">
<td>XTVS PKG MGR SAVE PACKAGE PARM ACTION</td>
<td><strong>SPP—Save Package Parameter Changes</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D SAVPMPKG^XTVSLPDC</strong></td>
<td><p>Allows users to overwrite the displayed Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) or create a new Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>).</p>
<p>After the XTMPSIZE*.DAT file has been edited, this action prompts the user to indicate if s/he wants to create a new Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>). If the user selects to create a new Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>), the file is written to the <strong>XTMPSIZE*.DAT</strong> default directory with the following file name format:</p>
<p><strong>XTMPSIZE_&lt;user initials&gt;&lt;mm-dd-yy_hhmm&gt;.DAT</strong></p>
<p>If the user does <em>not</em> choose to create a new Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>), the currently displayed Package Parameter file (i.e., <strong>XTMPSIZE*.DAT</strong>) is overwritten.</p></td>
</tr>
<tr class="odd">
<td>XTVS PKG MGR VISTA SIZE RPT</td>
<td><strong>VSR—Display VistA Size Report</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D VSR^XTVSLM</strong></td>
<td>Reports VistA package size statistics.</td>
</tr>
<tr class="even">
<td>XTVS PKG QUERY REMOTE VISTA SIZE ACTION</td>
<td><strong>RVQ—Remote VistA Size Query</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D REMREQ^XTVSLM</strong></td>
<td><p>Prompts the user for a package and a VistA domain to request a size report for the selected package. A size report query message is sent to the selected VistA domain. These actions are available from the “<strong>VistA Package Size Analysis Manager</strong>” and the “<strong>VistA Package Size Analysis Manager - Package Statistics</strong>” screens:</p>
<ul>
<li><blockquote>
<p><strong>“VistA Package Size Analysis Manager” Screen—</strong>When the <strong>RVQ</strong> action is run from this screen, the request prompts the user to select a Package Parameter file and sends the request to the remote VistA, so the report can be created on the remote VistA.</p>
</blockquote></li>
</ul>
<p><strong>“VistA Package Size Analysis Manager - Package Statistics” Screen—</strong>When the <strong>RVQ</strong> action is run from this screen, the request sends the Parameter file used to create the displayed report to the remote VistA, so that an apples-to-apples size report is returned from the remote VistA. That is the same package parameters that are used to create the report.</p></td>
</tr>
<tr class="odd">
<td>XTVS PKG RPT SWAP HEADER ACTION</td>
<td><strong>SHD—Swap Header</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D SWAPHEAD^XTVSLR</strong></td>
<td>Changes the ListMan header section on the VistA Package Size Report for all packages to the alternate header. This action is only active when a user readable report for all packages is displayed. For example, this action is <em>not</em> active on a screen if the date headings are displayed next to the data on the VistA Size Report for a single package.</td>
</tr>
<tr class="even">
<td>XTVS SITE PARAMETERS</td>
<td><strong>CHD—Change Host Directory</strong></td>
<td>Action</td>
<td>ENTRY ACTION:<br />
<strong>D SP^XTVSLM</strong></td>
<td><p>Allows users to change the default host file directory retaining the following files:</p>
<ul>
<li><blockquote>
<p><strong>XTMPSIZE*.DAT</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>XTMPSIZE*.BAK</strong></p>
</blockquote></li>
<li><blockquote>
<p>VistA Size Statistic Report</p>
</blockquote></li>
</ul>
<p>This action is locked with the <strong>XTVS EDITOR</strong> security key.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref355083482" class="anchor"></span>Table : VPSRT—Security Keys

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* distribute or create any mail groups, alerts, or bulletins; however, similar to bulletins, VPSRT does send MailMan messages to users.

For example, VPSRT sends a MailMan message to a user to notify them of errors that occur or when a data change is made to accommodate package names that include quotation marks, such as “OUTPATIENT PHARMACY 4” LABEL”, as shown in <u>Figure 5</u>:

<span id="_Ref69717720" class="anchor"></span>Figure : Sample VPSRT MailMan Error Message

Subj: PACKAGE REPORT NOTICE (PATTRW) ; Report process warning. \[#160459\]

10/08/20@14:32 5 lines

From: VISTA PACKAGE SIZE ANALYSIS MANAGER In 'IN' basket. Page 1

--------------------------------------------------------------------------

Package Size Report warning for PATTRW.

The following package(s) are not found on this VistA.

(The number of protocols reported may be incorrect.)

\- GTS TEST

\- OUTPATIENT PHARMACY 4'' LABEL

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/018.png) REF: For other examples of VPSRT MailMan messages, see Section 3, “Appendix A—System MailMan Messages,” in the *VPSRT Kernel Toolkit Patch XT\*7.3\*143 User Guide*.

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes any public interfaces (e.g., Integration Control Registrations \[ICRs\], RPCs, Health Level Seven \[HL7\] messaging, application programming interfaces \[APIs,\] etc.) that are called by this software (i.e., subscriber), or that are made available by this software (i.e., custodian). It should include technical details as applicable, such as functions, entry points, required variables, parameters, any restrictions, etc.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* have any public interfaces as described.

## Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists any Integration Control Registrations (ICRs) created and/or used by the software or provide instructions for obtaining the information online. Categorize ICRs by the custodian or subscriber relationship to your software.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* have any public interfaces as described.

## Application Programming Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes any Application Programming Interfaces (APIs, aka callable routines) entry points, parameters, and variables created and/or used by the software.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* have any supported or controlled subscription APIs.

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes any remote procedure call (RPC) entry points and parameters created and/or used by the software.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* distribute any RPCs.

## HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes any Health Level 7 (HL7) messages sent or received by the software. It should include any subscriber protocols, HL7 application parameters, HL Logical Links, etc. It should also identify the software that relies on the HL7 messaging and what data is being moved.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* send or receive HL7 messages. VPSRT does *not* have any subscriber protocols, HL7 application parameters, or HL Logical Links associated with or used by the software.

## Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes any web services created and/or used by the software. For example, calls made from the VistA/M environment to an external server for retrieved results.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* create or use any web services.

# Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Standards and Conventions (SAC) document is a set of guidelines and standards that application developers *must* follow. Through a process of quality assurance, software is reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC).

The SACC may grant exemptions from compliance with a particular section of the SAC for a specified timeframe. Any SAC exemptions for this software should be described in this section.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* have any SAC exemptions.

## Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this section to specify any routines, files, or options within this software that cannot function independently. For example, does the functioning of a particular option assume that entry/exit logic of another option has already occurred? If so, list such options with their programming Standards and Conventions Committee (SACC) approval dates.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do not have any unique internal relationships with other VistA software.

## Software-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this section to provide a list of all software-wide variables (aka Public or Published Variables) that have received Standards and Conventions Committee (SACC) exemptions and approval dates.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* create any software-wide variables.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of VPSRT for *non*-VistA use should be referred to the VistA Infrastructure (VI) / VistA Kernel Team.

## Security Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* distribute any security-specific menus, options, or protocols.

## Security Keys and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 7</u> lists the security keys distributed with the VPSRT and Kernel Toolkit Patch XT\*7.3\*143:

| Security Key | Description                                                                                                                                                                                                    |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XTVS EDITOR  | This is the Package Management Editor security key. This security key is used to protect Kernel Toolkit Package Management ListMan protocols and actions from execution by unprivileged and misinformed users. |

<span id="_Ref37860726" class="anchor"></span>Table 8: VPSRT—Common Issues and Resolutions

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* distribute any files, so there are no additional file security requirements.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* use any electronic signatures for any software functions.

## Secure Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* require any additional secure data transmission capabilities, since VPSRT does *not* transmit data outside of the VA firewall.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this section to specify any data archiving capabilities of the software. Provide any necessary instructions or guidelines.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* require any special archiving capabilities.

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* have any *non*-standard or special cross-references.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this section to describe any anticipated problems, issues, or items that a user may need assistance with and provide guidance to the extent possible.

## Common Issues and Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 8</u> will be updated over time by the VistA Infrastructure (VI) / VistA Kernel Team with common issues observed with VPSRT and their resolutions, so that as they reoccur, consistent solutions can be applied.

| Issue | Common Resolution | Support Contact |
|-------|-------------------|-----------------|
|       |                   |                 |

<span id="_Toc67666586" class="anchor"></span>Table : Glossary of Terms, Acronyms, and Abbreviations

## Frequently Asked Questions (FAQs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section will be updated over time by the VistA Infrastructure (VI) / VistA Kernel Team based on frequently asked questions (FAQs) from users. It will provide answers to commonly asked questions, to assist users when configuring, maintaining, or troubleshooting VPSRT.

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this section to specify any recovery and error correction procedures, including error conditions that may be generated and corrective actions that may need to be taken.

VPSRT and Kernel Toolkit Patch XT\*7.3\*143 do *not* require any special recovery or error correction procedures be taken when running VPSRT.

## Enterprise Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enterprise support and other organizational points of contact (POCs):

- <u>VA Enterprise Service Desk</u>
- <u>Tier 2</u>

### VA Enterprise Service Desk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Information Technology (IT) support 24 hours a day, 365 days a year call the VA Enterprise Service Desk (ESD):

- Enter an Incident or Request ticket in ServiceNow (SNOW) system[^1] via the YourIT shortcut on your workstation. or call REDACTED or REDACTED
- Assign SNOW ticket to this ServiceNow Support Team: NTL MNT Infrastructure service support

### Tier 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contact the following Tier 2 support email distribution group to add appropriate members/roles to be notified when needed:

REDACTED

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term                                       | Definition                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| API                                        | Application Programming Interface.                                                                                                                                                                                                                                                                                     |
| COMMON MENU                                | Options that are available to all users. Entering two question marks (??) at the menu’s select prompt will display any SECONDARY MENU OPTIONS available to the signed-on user along with the common options available to all users.                                                                            |
| DIBRG                                      | Deployment, Installation, Back-Out, and Rollback Guide                                                                                                                                                                                                                                                                 |
| EPMO                                       | Enterprise Program Management Office.                                                                                                                                                                                                                                                                                  |
| FAQs                                       | frequently asked questions.                                                                                                                                                                                                                                                                                            |
| FILE ACCESS SECURITY SYSTEM                | Formerly known as Part 3 of the Kernel Inits. If the File Access Security conversion has been run, file-level security for VA FileMan files is controlled by Kernel’s File Access Security system, *not* by File Manager Access codes (i.e., FILE MANAGER ACCESS CODE field).                                      |
| HELP PROCESSOR                             | A Kernel module that provides a system for creating and displaying online documentation. It is integrated within the menu system so that help frames associated with options can be displayed with a standard query at the menu’s select prompt.                                                                       |
| HL7                                        | Health Level Seven.                                                                                                                                                                                                                                                                                                    |
| HOST FILE SERVER (HFS)                     | A procedure available on layered systems whereby a file on the host system can be identified to receive output. It is implemented by the Device Handler’s HFS device type.                                                                                                                                         |
| ICR                                        | Integration Control Registration.                                                                                                                                                                                                                                                                                      |
| ISO                                        | Information Security Officer.                                                                                                                                                                                                                                                                                          |
| ITSM                                       | Information Technology Service Management (see [SNOW](#snow)).                                                                                                                                                                                                                                                         |
| OIT                                        | Office of Information and Technology (OIT).                                                                                                                                                                                                                                                                            |
| OITFO                                      | Office of Information and Technology Field Office.                                                                                                                                                                                                                                                                     |
| PROTOCOL                                   | An entry in the PROTOCOL (#101) file.                                                                                                                                                                                                                                                                                  |
| PS                                         | Product Support.                                                                                                                                                                                                                                                                                                       |
| RPC                                        | Remote Procedure Call.                                                                                                                                                                                                                                                                                                 |
| SAC                                        | Standards and Conventions.                                                                                                                                                                                                                                                                                             |
| SACC                                       | Standards and Conventions Committee.                                                                                                                                                                                                                                                                                   |
| SECONDARY MENU OPTIONS                     | Options assigned to individual users to tailor their menu choices. If a user needs a few options in addition to those available on the primary menu, the options can be assigned as secondary options. To facilitate menu jumping, secondary menus should be specific activities, *not* elaborate and deep menu trees. |
| <span id="snow" class="anchor"></span>SNOW | ServiceNow.                                                                                                                                                                                                                                                                                                            |
| SYNONYM                                    | In VistA, a field in the OPTION (#19) file. Options can be selected by their menu text or synonym.                                                                                                                                                                                                                     |
| VI                                         | VistA Infrastructure.                                                                                                                                                                                                                                                                                                  |
| VISTA                                      | Veterans Health Information Systems and Technology Architecture.                                                                                                                                                                                                                                                       |
| VPSRT                                      | VistA Package Size Reporting Tool.                                                                                                                                                                                                                                                                                     |

![](vista-package-size-reporting-tool-vpsrt-technical-manual-xt-7-3-143/019.png) REF: For a list of commonly used terms and definitions, see the OIT Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.

[^1]: Information Technology Service Management (ITSM) Tool: REDACTED (use Google Chrome browser)