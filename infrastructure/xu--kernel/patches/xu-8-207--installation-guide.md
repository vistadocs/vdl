---
title: XU*8*207 KDC Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: KDC
app_code: XU
app_name: Kernel Delphi Components (KDC)
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8
patch_id: XU*8*207
group_key: "XU:XU:8"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this guide is to provide instructions for installing the Veterans Health Information Systems and Technology Architecture (VISTA) Kernel Delphi Components (KDC) Version 1.0 (Kernel Patch XU\8\207). This version of the Kernel Delphi Components provides programmers with the capability to
audience: 
keywords: 
  - table
  - delphi
  - kernel
  - installation
  - contents
  - components
  - strong
  - blockquote
  - class
  - style
page_count: 0
word_count: 3597
section_count: 2
table_count: 40
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Delphi_Components/kdc1_0ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Delphi_Components/kdc1_0ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=127"
---

![](xu-8-207-kdc-installation-guide/001.png)

KERNEL DELPHI COMPONENTS (KDC)INSTALLATION GUIDE

Patch XU\*8\*207

June 2002

V*IST*A System Design & Development (SD&D)

Information Infrastructure Service (IIS)

Document Revision History

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<caption><p><span id="_Toc92517464" class="anchor"></span>Table 1: Documentation symbol descriptions</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 41%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>04/19/02</td>
<td>1.0</td>
<td>Initial Kernel Delphi Components (KDC) software release.</td>
<td>REDACTED, Oakland OIFO</td>
</tr>
<tr class="odd">
<td>06/10/02</td>
<td>1.1</td>
<td>Updated File Distribution lists to eliminate references to the Technical Manual and separate KIDS file other than Kernel Patch XU*8*207.</td>
<td>REDACTED, Oakland OIFO</td>
</tr>
<tr class="even">
<td>12/20/04</td>
<td>2.0</td>
<td><p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>REDACTED, Bay Pines OIFO</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc92517464" class="anchor"></span>Table 1: Documentation symbol descriptions

Contents

Figures

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### How to Use this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this manual, advice and instructions are offered regarding the use of the RPC Broker V. 1.1 and the functionality it provides for Veterans Health Information Systems and Technology Architecture (V*IST*A) and commercial off-the-shelf (COTS) software products.

There are no special legal requirements involved in the use of the RPC Broker Interface.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                                            |                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                                                 | Description                                                                                      |
| ![](xu-8-207-kdc-installation-guide/002.png)                             | Used to inform the reader of general information including references to additional reading material |
| ![](xu-8-207-kdc-installation-guide/003.png)                                                                                          | Used to caution the reader to take special notice of critical information                            |
| ![](xu-8-207-kdc-installation-guide/004.png) | Used to denote Virgin installation instructions only.                                                |

<span id="_Hlt396118096" class="anchor"></span>Table 2: Kernel Delphi Components Path XU\*8\*207 distribution files

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
- Patient and user names will be formatted as follows: \[Kernel Delphi Components\]PATIENT,\[N\] and \[Kernel Delphi Components\]USER,\[N\] respectively, where "Kernel Delphi Components" is defined in the Approved Application Abbreviations document, located on the Application Abbreviations web site and where "N" represents the first name as a number spelled out and incremented with each new entry. For example, in KDC test patient and user names would be documented as follows: KDCPATIENT,ONE; KDCPATIENT,TWO; KDCPATIENT,10; etc.

<table>
<caption><p><span id="_Toc92517466" class="anchor"></span>Table 3: Kernel Delphi Components Programmer Workstation installation distribution files</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xu-8-207-kdc-installation-guide/005.png)</td>
<td><p>The list of Approved Application Abbreviations can be found at the following Web site:</p>
<p><a href="http://vista.med.va.gov/iss/strategic_docs.asp#sop"><u>http://vista.med.va.gov/iss/strategic_docs.asp#sop</u></a></p></td>
</tr>
</tbody>
</table>

<span id="_Toc92517466" class="anchor"></span>Table 3: Kernel Delphi Components Programmer Workstation installation distribution files

- "Snapshots" of computer online displays (i.e., roll-and-scroll screen captures/dialogs) and computer source code are shown in a *non*-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogs or forms).
- User's responses to online prompts will be boldface type.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter or Return key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/006.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

<span id="_Toc92517468" class="anchor"></span>Table 4: Kernel Delphi Components V*IST*A M Server installation distribution files

- Object Pascal code uses a combination of upper- and lowercase characters. All Object Pascal reserved words are in boldface type.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

### How to Obtain Technical Information Online

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/007.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at PromptsV*IST*A software has online help and commonly used system default prompts. In roll-and-scroll mode users are strongly encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of V*IST*A software.

To retrieve online documentation in the form of Help in V*IST*A roll-and-scroll software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. You can use the List File Attributes option submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/008.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the "VA FileMan Advanced User Manual." |

### Assumptions About the Reader

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual is written with the assumption that the reader is familiar with the following:

- V*IST*A computing environment (e.g., Kernel Installation and Distribution System \[KIDS\])
- VA FileMan data structures and terminology
- Microsoft Windows
- M programming language

No attempt is made to explain how the overall V*IST*A programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web for a general orientation to V*IST*A. For example, go to the System Design & Development (SD&D) Home Page at the following web address:

> <http://vista.med.va.gov/>

### Reference Materials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Readers who wish to learn more about the RPC Broker should consult the following:

- "Kernel Delphi Components Developer's Guide" (i.e., KDC.HLP, the online help file designed for programmers, distributed with the KDC)
- Kernel Delphi Components Home Page at the following web address:

> http://vista.med.va.gov/kdc/index.asp

> This site provides announcements, Frequently Asked Questions (FAQs), advisories, documentation links, software downloads, and archives (e.g., earlier versions of documentation, software downloads, and FAQs).

Kernel Delphi Components documentation is made available online, on paper, and in Adobe Acrobat Portable Document Format (.PDF). The .PDF documents must be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xu-8-207-kdc-installation-guide/009.png)</td>
<td><p>For more information on the use of the Adobe Acrobat Reader, please refer to the "Adobe Acrobat Quick Guide" at the following web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">http://vista.med.va.gov/iss/acrobat/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/010.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Health Administration (VHA) of this Web site or the information, products, or services contained therein. The VHA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VHA Intranet Service. |

# Preliminary Considerations


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Orientation](#orientation)
    - [How to Use this Manual](#how-to-use-this-manual)
    - [How to Obtain Technical Information Online](#how-to-obtain-technical-information-online)
    - [Assumptions About the Reader](#assumptions-about-the-reader)
    - [Reference Materials](#reference-materials)
- [Preliminary Considerations](#preliminary-considerations)
    - [Purpose](#purpose)
    - [About the Installation Procedures](#about-the-installation-procedures)
    - [Kernel Delphi Components Distribution Files](#kernel-delphi-components-distribution-files)
    - [Programmer Client Workstation Requirements](#programmer-client-workstation-requirements)
    - [VISTA M Server Requirements](#vista-m-server-requirements)
    - [Skills Needed for Installation](#skills-needed-for-installation)
- [Programmer Workstation Delphi V. 6, 5, and 4 Instructions](#programmer-workstation-delphi-v-6-5-and-4-instructions)
    - [Considerations Before Installing the KDC](#considerations-before-installing-the-kdc)
    - [Confirm Distribution Files](#confirm-distribution-files)
    - [Delphi V. 4 Only: Install Updated Delphi V. 4 Help System (recommended)](#delphi-v-4-only-install-updated-delphi-v-4-help-system-recommended)
    - [De-Install Any Previous Kernel Delphi Components Installed for Delphi V. 4, 5, or 6 (required)](#de-install-any-previous-kernel-delphi-components-installed-for-delphi-v-4-5-or-6-required)
    - [Run the Kernel Delphi Components Installation Program (required)](#run-the-kernel-delphi-components-installation-program-required)
    - [Verify the Installation of the Kernel Delphi Components (recommended)](#verify-the-installation-of-the-kernel-delphi-components-recommended)
- [VISTA M Server Installation Instructions](#vista-m-server-installation-instructions)
    - [Confirm Distribution Files](#confirm-distribution-files-1)
    - [Save KDC Routines and Files as a Safeguard before the Installation (optional)](#save-kdc-routines-and-files-as-a-safeguard-before-the-installation-optional)
    - [Do Not Run any Client/Server Software during the Installation (required)](#do-not-run-any-clientserver-software-during-the-installation-required)
    - [Verify You Have an HFS Device and a Null Device (required)](#verify-you-have-an-hfs-device-and-a-null-device-required)
    - [Using KIDS, Install KDC Routines and Remote Procedures (required)](#using-kids-install-kdc-routines-and-remote-procedures-required)
    - [Verify the Client/Server Installation of the Kernel Delphi Components (recommended)](#verify-the-clientserver-installation-of-the-kernel-delphi-components-recommended)

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for installing the Veterans Health Information Systems and Technology Architecture (V*IST*A) Kernel Delphi Components (KDC) Version 1.0 (Kernel Patch XU\*8\*207).
This version of the Kernel Delphi Components provides programmers with the capability to develop and deploy new V*IST*A client/server software using the Kernel Delphi Components in the 32-bit environment.
Please note that multiple installation procedures are provided in this guide. The Kernel Delphi Components have separate installations for the following target environments:
- Programmer Client Workstations
- V*IST*A M Servers

### About the Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the Kernel Delphi Components is a *multi-part* process. Separate installation procedures are provided in this guide for:
- Programmer Client Workstations
- V*IST*A M Servers
*For Programmer Client Workstations*, the installation program provides the ability to select for installation of the components for Delphi V. 4, Delphi V. 5, and/or Delphi V. 6 as appropriate for the system. Before running the installation program:
1.  Close any open Delphi programs (this will prevent having to restart your system).
2.  Run the installation program selecting the version(s) of Delphi to be installed.
3.  Following the installation, open Delphi and the components will be available on the Kernel palette tab.
*For first-time field deployments*, we strongly recommend the following approach to installing the Kernel Delphi Components:
> 1\. Obtain the Kernel Delphi Components documentation. It is available in Acrobat PDF format, and can be downloaded from the National V*IST*A Support (NVS) anonymous directories or from the System Design and Development (SD&D) V*IST*A Documentation Library (VDL) web site:
> <http://vista.med.va.gov/vdl/>
> 2\. Install the server software in a Test account prior to installing it in a Production account.

### Kernel Delphi Components Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 9%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KDC1_0RM.TXT</td>
<td>ASCII</td>
<td><strong>Readme Text File</strong>. Provides any last minute changes, new instructions, and additional information to supplement the manuals. Read all sections of this file prior to workstation installations.</td>
</tr>
<tr class="even">
<td>KDC1_0IG.PDF</td>
<td>Binary</td>
<td><strong>Installation Guide</strong> (manual). Use in conjunction with the KDC1_0RM.TXT Readme text file.</td>
</tr>
<tr class="odd">
<td>KDC1_0PG.EXE</td>
<td>Binary</td>
<td><p><strong>Programmer Client Workstation Software</strong>, self-installing executable. Contains:</p>
<ul>
<li><blockquote>
<p>Kernel Delphi Components (KDC).</p>
</blockquote></li>
<li><blockquote>
<p>KDC.HLP. The complete online reference to the KDC.</p>
</blockquote></li>
<li><blockquote>
<p>Sample applications using the KDC (e.g., Alert Handler Interface, Alert Button Test, Calendar Demonstration).</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Kernel Patch:</p>
<blockquote>
<p>XU*8.0*207</p>
</blockquote></td>
<td>ASCII</td>
<td><p><strong>KIDS Distribution.</strong> Patch that contains the Kernel Delphi Components (KDC)-related <strong>V</strong><em>IST</em><strong>A</strong> M Server software:</p>
<ul>
<li><blockquote>
<p>Modified ALERT file (#8992) and ALERT TRACKING file (#8992.1)—New GUID and LONGTEXT fields added.</p>
</blockquote></li>
<li><blockquote>
<p>Server Routines.</p>
</blockquote></li>
<li><blockquote>
<p>Kernel Options and Remote Procedure Calls.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

### Programmer Client Workstation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum hardware and software tools are required on your programmer client workstation in order to install and use the Kernel Delphi Components:
 Hardware
> 80x86-based client workstation
 Operating System
> One of the following 32-bit operating systems:
- Microsoft Windows 2000
- Microsoft Windows NT Workstation V. 3.51 or greater
- Microsoft Windows 98
- Microsoft Windows 95
|                                                                                                                |                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/011.png) | The VA has made the decision to go to a 32-bit Microsoft Windows environment. Therefore, this version of the Broker does not operate on Microsoft Windows 3.1 or Windows 3.1 with WIN32S. |
 Network communications software
> The KDC alert components (i.e., TXUALert, TXUAlertButton, and TXUAlertSurrogate) require networked client workstations running Microsoft's native TCP/IP stack with connectivity to the M V*IST*A Server provided by the RPC Broker.
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xu-8-207-kdc-installation-guide/012.png)</td>
<td><p>For more information on the RPC Broker, please consult the RPC Broker documentation located at:</p>
<blockquote>
<p><a href="http://vaww.va.gov/cso/">http://vista.med.va.gov/vdl/#App23</a></p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xu-8-207-kdc-installation-guide/013.png)</td>
<td><p>For more information on telecommunications support, please visit the Telecommunications Support Office Home Page:</p>
<blockquote>
<p><a href="http://vaww.va.gov/cso/">http://vaww.va.gov/cso/</a></p>
</blockquote></td>
</tr>
</tbody>
</table>
 Delphi V. 6, 5, or 4 Software (required for the KDC)
> This version does NOT support Delphi V. 1, Delphi V. 2 or Delphi V. 3. A version of Delphi V. 4 or above is required to use these components.
|                                                   |                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/014.png) | This statement defines the extent of support relative to use of Delphi. The Office of Information (OI) will support the Kernel Delphi Components (KDC) running in the currently offered version of Delphi and the immediately previous version of Delphi. This level of support became effective 06/12/2000. |

### V*IST*A M Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools are required on your V*IST*A M Server in order to install and use the Kernel Delphi Components:
 Server Operating System.
> One of the following operating systems:
- Digital Standard M (DSM) V6.3-031 for OpenVMS AXP or greater
- InterSystems Caché for NT and OpenVMS
 Fully Patched M Accounts.
> You should have both a development Test account and a Production account for the Kernel Delphi Components software.
> The account(s) must contain the *fully* patched versions of the following software:
- Kernel V. 8.0
|                                                   |                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/015.png) | Kernel Patch XU\*8\*174 must be installed prior to the installation of the Kernel Delphi Components. |
- Kernel Toolkit V. 7.3
- RPC Broker V. 1.1
- FileMan Delphi Components (FMDC) V. 1.0
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xu-8-207-kdc-installation-guide/016.png)</td>
<td><p>The FMDC Readme.TXT file has been edited to include updated instructions on installing the FMDC into Delphi V. 4, 5, and 6, necessary before installing the KDC. This document is available at:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/vdl/#App6">http://vista.med.va.gov/vdl/#App6</a></p>
</blockquote></td>
</tr>
</tbody>
</table>
- VA FileMan V. 22.0
> These packages must be properly installed and *fully* patched prior to installing the Kernel Delphi Components server software distribution. Patches must be installed in published sequence.
 Network communications software
> The KDC alert components (i.e., TXUALert, TXUAlertButton, and TXUAlertSurrogate) require that the M V*IST*A Server have TCP/IP running.

### Skills Needed for Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Skills required to perform the installation are listed below. Instructions for performing these functions are provided in vendor-supplied operating system manuals as well as V*IST*A publications.
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xu-8-207-kdc-installation-guide/017.png)</td>
<td><p>DSM for OpenVMS sites should refer to the most recent Computer Operations Management and Procedures for AXP Systems (COMPAS) manual. Please refer to the AXP team's web site at:</p>
<blockquote>
<p><a href="http://vaww.va.gov/custsvc/cssupp/axp/axphome.asp">http://vaww.va.gov/custsvc/cssupp/axp/axphome.asp</a></p>
</blockquote>
<p>Caché for NT and OpenVMS sites should refer to the AVANTI How-To web site currently located at:</p>
<blockquote>
<p><a href="http://vaww.va.gov/custsvc/cssupp/avanti/How-to.HTM">http://vaww.va.gov/custsvc/cssupp/avanti/How-to.HTM</a></p>
</blockquote></td>
</tr>
</tbody>
</table>
You need to know how to do the following:
- Back up the system
> *\[both the VISTA M Server and Programmer Client Workstations\]*
- Create directories on the host file system
> *\[Programmer Client Workstation only\]*
- Copy files using commands of the host file system
> *\[both the VISTA M Server and Programmer Client Workstations\]*
- Run a KIDS installation
> *\[VISTA M Server only\]*
- Switch User Class Identification (UCI) accounts
> *\[VISTA M Server only\]*
- Enable/Disable routine mapping and journaling
> *\[VISTA M Server only\]*
- Manage globals, including global placement, protection, and translation
> *\[VISTA M Server only\]*
- Run a system status and restore a job
> *\[VISTA M Server only\]*

# Programmer Workstation Delphi V. 6, 5, and 4 Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Considerations Before Installing the KDC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Source Code—The release of the source code does not affect how a developer uses the Kernel Delphi Components (KDC).

|                                                   |                                                                                   |
|---------------------------------------------------|-----------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/018.png) | Modified KDC source code should *not* be used to create V*IST*A GUI applications. |

|                                                                                                                |                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/019.png) | Suggestions for changes to the KDC should be done via NOIS (for bugs) or E3R (for enhancements) for review and possible inclusion in another patch. |

- Design-time and Run-time Packages—The KDC has separate run-time and design-time packages. The packages are KDC\_Dxx and KDC\_Rxx, where "D" means Design-time, "R" means Run-time, and "xx" is the two-digit number indicating the version of Delphi with which it should be used (e.g., KDC_D50 is the design-time package for Delphi V. 5.0). The run-time package should not be used to create executables that depend on a separate KDC_Rxx.bpl installed on client workstations. There is no procedure in place at this time to reliably install the correct version of the run-time bpl on client workstations.

|                                                   |                                                                                                                                                                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/020.png) | Do *not* compile your project so that it relies on dynamic linking with the Kernel Delphi Components' run-time package; that is, do *not* check the "Build with runtime packages" box on the Packages tab of the Project Options dialog. |

- Package Dependencies—A Package may have been defined to *require* the KDC package. If you try to install a package into the Delphi IDE that requires the KDC, you may receive an error message like:

> Can't load package \<Package1\>.

> One of the library files needed to run this package cannot be found.

> To resolve this problem, Open the DPK file associated with that package; delete the reference to the old version of the KDC in the Requires section; add a reference to the new run-time KDC package (KDC_Rxx) into the Requires section; recompile and install the package.

- Component Dependencies—Some VA-developed components may reference the Kernel Delphi Components. If you develop applications using such components, be aware that installing a newer version of the KDC may cause incompatibilities, until the KDC-dependent components have been recompiled with the new version of the Kernel Delphi Components. Any such incompatibilities would show up as a compilation error:

> Unit \<Unit1\> was compiled with a different version of \<Unit2\>

> To resolve this problem, you need to either:

> A. Recompile the KDC components with the included source code.

> OR

> B. Obtain a compiled version of their component that was compiled with the same version of the KDC you are using.

- Delphi V. 5 Standard Edition. Delphi V. 5 comes in three flavors: Standard, Professional, and Enterprise. The Standard edition of Delphi V. 5 is targeted mainly at students, and as such leaves out many features. The Standard Edition does not ship with Delphi's OpenHelp help system. This makes it difficult to integrate the KDC help with Delphi V. 5, Standard Edition. We do *not* recommend using the Standard Edition of Delphi V. 5 for Kernel Delphi Components development at this time.

### Confirm Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the following files to install the KDC for Delphi V. 6, 5, or 4:

|               |          |                                                                                                                                                                                                                                   |
|---------------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| File Name | Type | Description                                                                                                                                                                                                                   |
| KDC1_0RM.TXT  | ASCII    | Readme Text File. Provides any pre-installation instructions, last minute changes, new instructions, and additional information to supplement the manuals. Read all sections of this file prior to workstation installations. |
| KDC1_0IG.PDF  | Binary   | Installation Guide. Use in conjunction with the KDC1_0RM.TXT Readme text file.                                                                                                                                                |
| KDC1_0PG.EXE  | Binary   | Programmer Client Workstation self-installing executable. Installs the Kernel Delphi Components Development Kit (KDC).                                                                                                        |

### Delphi V. 4 Only: Install Updated Delphi V. 4 Help System *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There is an update from Inprise to the Delphi V. 4 help system, for the originally released version of Delphi V. 4. This update enables Delphi V. 4's new "OpenHelp" system, which makes 3<sup>rd</sup> party help (e.g., the Kernel Delphi Components help) easier to integrate.

> For Delphi V. 4 only, to install this update:

> A. Exit Delphi V. 4, if it is open.

> B. Go to Inprise's Delphi Documentation update web page, and download the "DELPHI4.HLP" update. At the time of publication of this manual, the name of the file to download is DEL4HLP.ZIP, and the file is located at:

> <ftp://ftp.inprise.com/pub/delphi/techpubs/delphi4/del4hlp.zip>

> C. Unzip DEL4HLP.ZIP, placing the four resulting files (DELPHI4.CNT, DELPHI4.HLP, DELPHI4.OHC, DELPHI4.OHI) into the following directory (overwriting the existing versions of these four Delphi4 help files):

> ...\DELPHI4\HELP

### De-Install Any Previous Kernel Delphi Components Installed for Delphi V. 4, 5, or 6 *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                                                 |                                                                                         |
|-------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/021.png) | If this is a virgin installation for your version of Delphi proceed directly to Step 5. |

> A. Start Delphi V. 6, 5, or 4 and close any open projects.

> B. From the Delphi menu, select *Component \| Install Packages*.

> C. Remove any previous version of the Kernel Delphi Components from the Design Packages listing. To do this:

> i\. Scroll through the listing of installed design packages until you find the entries for the previous versions of the KDC. We will refer to the name of any previous version as YourOldKDC for the remainder of this section.

> ii\. Select (highlight) this entry.

> iii\. Click Remove.

> iv\. Delphi presents one of two confirmation windows, which says one of the following:

> Confirm 1:

> Remove 'c:\program files\\..\YourOldKDC.bpl' from the design package list?

> If Delphi presents this confirmation window, click Yes.

> Confirm 2:

> Package(s) xxx will also be uninstalled because they require package YourOldKDC. Continue Uninstall?

> If this is OK, click Yes. Any packages dependent on the KDC are also uninstalled. You will need to re-install them after you install or update the KDC. If you click No, you will not be able to de-install the previous KDC software.

> v\. If you chose to remove any packages, Delphi may also present a Remove Runtime Packages window, saying:

> The package names in the following list are not used by any installed packages. Remove the selected names from the runtime packages list?

> If Delphi presents this window, click Yes.

> vi\. Click OK in the "Project Options" dialog box to finish the de-installation.

> D. Close Delphi V. 6, 5, or 4, answer No if you are prompted to save changes to any projects.

### Run the Kernel Delphi Components Installation Program *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                                                  |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/022.png) | Prior to installing the Kernel Delphi Components, make sure that you exit/close *all* versions of Delphi running on your system. |

> To start the programmer client workstation installation setup program, run KDC1_0PG.EXE. Follow the procedures on how to run a program as described in your operating system's Systems Manual.

|                                                                                                                |                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/023.png) | There is no "silent" installation for the KDC. |

> For example, in Windows NT:

> A. Go to the Start menu.

> B. Select the Run option.

> C. Click Browse to locate KDC1_0PG.EXE.

> D. Click OK to run KDC1_0PG.EXE.

> During the installation, various dialog boxes are presented to you. Follow the online instructions. The directory location you choose to install the KDC files will be referred to in these instructions as the "KDC files directory." In addition to placing files in the subdirectories of the KDC files directory, some files will be placed in certain Delphi subdirectories.

> The KDC installation supports several different versions of Delphi, which at the current time includes V. 6, 5, and 4. During the installation you are given the opportunity to include the necessary files for development under one or more of these environments. The KDC source code will be placed in a directory directly descendent from the Kernel directory:

> Kernel\Source

> The installation will determine what version(s) of Delphi you have loaded on your system. It will then check the appropriate Delphi version(s) during the installation. For example:

![](xu-8-207-kdc-installation-guide/024.png)

<span id="_Toc92517467" class="anchor"></span>Figure 1: Kernel Components Dialogue Box

### Verify the Installation of the Kernel Delphi Components *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A. Start Delphi V. 6, 5, or 4.

> B. Scroll through the Delphi palette tabs using the arrow buttons located in the upper right of the palette (![](xu-8-207-kdc-installation-guide/025.png)) until you see the tab marked "Kernel."

> C. Move your mouse pointer over the Kernel tab and click to select it.

> D. If the Kernel Delphi Components installed correctly, you should see the TXUViewPropButton (![](xu-8-207-kdc-installation-guide/026.png)), TXUAlert (![](xu-8-207-kdc-installation-guide/027.png)), TXUAlertButton (![](xu-8-207-kdc-installation-guide/028.png)), TXUAlertSurrogate (![](xu-8-207-kdc-installation-guide/029.png)), TXUMonthCalendar (![](xu-8-207-kdc-installation-guide/030.png)), TXUDateTimeSelect (![](xu-8-207-kdc-installation-guide/031.png)), and TXU_NameRules (![](xu-8-207-kdc-installation-guide/032.png)) components on the Kernel Tab, as shown below:

> ![](xu-8-207-kdc-installation-guide/033.png)

> E. Verify that the Kernel Delphi Components context-sensitive help has been successfully integrated with Delphi's help.

> i\. On a blank form, add any one of the Kernel Delphi Components.

> ii\. Select the component on your form and press F1 for help. If the Kernel Delphi Components help comes up, you are all set.

> iii\. Press the *Help Topics* button while in any Kernel Delphi Components or Delphi help topic. You should see the "Kernel Delphi Components V. 1.0 Developer's Guide" manual listed along with the regular Delphi manuals.

|                                                                                                                |                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/034.png) | Kernel Delphi Components' topics should be available in the Delphi help index and full text search tabs as well. |

|                                                   |                                                                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/035.png) | You will now need to re-install any packages that were removed when you de-installed the previous KDC (Step 4). |

\*\*\* You have now completed the installation of the Kernel Delphi Components in Delphi V. 4, 5, and/or 6 on the Programmer Client Workstation \*\*\*

# VISTA M Server Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xu-8-207-kdc-installation-guide/036.png)</td>
<td><p>Do <em>not</em> use the instructions in this section, if you are installing a server-side Kernel Delphi Components patch. Instead, follow the installation instructions included with the patch.</p>
<p>Only use the instructions in this section if you are performing a VIRGIN server installation, or UPGRADING VERSIONS of the Kernel Delphi Components on the server.</p></td>
</tr>
</tbody>
</table>

The instructions in this section are applicable for the Test/Production accounts in the DSM or Caché environments.

### Confirm Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the following files to install the V*IST*A M Server routines:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File Name</strong></td>
<td><strong>Type</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>KDC1_0RM.TXT</td>
<td>ASCII</td>
<td><strong>Readme Text File</strong>. Provides any pre-installation instructions, last minute changes, new instructions, and additional information to supplement the manuals. Read all sections of this file prior to workstation installations.</td>
</tr>
<tr class="odd">
<td>KDC1_0IG.PDF</td>
<td>Binary</td>
<td><strong>Installation Guide</strong>. Use in conjunction with the KDC1_0RM.TXT Readme text file.</td>
</tr>
<tr class="even">
<td><p>Kernel Patch:</p>
<blockquote>
<p>XU*8.0*207</p>
</blockquote></td>
<td>ASCII</td>
<td><p><strong>KIDS Distribution.</strong> Patch that contains the Kernel Delphi Components (KDC)-related <strong>V</strong><em>IST</em><strong>A</strong> M Server software:</p>
<ul>
<li><blockquote>
<p>Modified ALERT file (#8992) and ALERT TRACKING file (#8992.1)—New GUID and LONGTEXT fields added.</p>
</blockquote></li>
<li><blockquote>
<p>Server Routines.</p>
</blockquote></li>
<li><blockquote>
<p>Kernel Options and Remote Procedure Calls.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

### Save KDC Routines and Files as a Safeguard before the Installation *(optional)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                                                 |                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/037.png) | If this is a virgin installation proceed directly to Step 3. |

> If you are running a prior version of the Kernel Delphi Components, you should save the existing KDC routines and global (i.e., KDC namespace) on the V*IST*A M Server prior to performing the main Kernel Delphi Components installation. It is best to save the KDC routines and global immediately prior to performing the Kernel Delphi Components main installation.

### Do *Not* Run any Client/Server Software during the Installation *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No KDC-based client/server software should be running while the KDC installation on the server is taking place.

### Verify You Have an HFS Device and a Null Device (required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A. Verify you have a Host File Server (HFS) device in the DEVICE file (#3.5) named "HFS". If you have performed KIDS installations on your server before, you probably already have an appropriate HFS device set up. If you don't have an entry for this device, you must create one.

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/038.png) | For information on how to create an HFS device, please refer to "Chapter 18 Host Files" in the "Kernel V. 8.0 Systems Manual." |

> B. Verify you have a Null device in the DEVICE file (#3.5) named "NULL" (or whose mnemonic is named "NULL"). You can have other devices with similar names, but one device is needed whose name or mnemonic is "NULL". The subtype should be a "P-" subtype (e.g., P-OTHER), the margin should be a minimum of 80, and the page length should be a minimum of 60. Sample setups:

> DSM for OpenVMS Null Device Setup Example

> NAME: NULL \$I: \_NLA0:

> ASK DEVICE: NO ASK PARAMETERS: NO

> SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: Bit Bucket

> SUBTYPE: P-OTHER TYPE: TERMINAL

> Caché Null Device Setup Example

> NAME: NULL \$I: //./nul

> ASK DEVICE: NO ASK PARAMETERS: NO

> SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: BIT BUCKIT

> SUBTYPE: P-OTHER TYPE: TERMINAL

> P-OTHER Terminal Type Setup Example

> NAME: P-OTHER RIGHT MARGIN: 132

> FORM FEED: \# PAGE LENGTH: 64

> BACK SPACE: \$C(8) DESCRIPTION: General prntr (132)

### Using KIDS, Install KDC Routines and Remote Procedures *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the PACKAGE file (#9.4), verify the NAME field (#.01) for any package with the XU namespace. The NAME should be KERNEL. If the NAME is incorrect, you must change it to read KERNEL. If no entry exists, the KIDS install will create the entry for you.

> Using KIDS, load and install the KDC routines and remote procedures. Make sure you have installed *all* of the RPC Broker, Kernel, VA FileMan, and Kernel Toolkit patches. Follow the instructions under the "Installation Instructions" section in Patch XU\*8\*207 in the Patch module on FORUM.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xu-8-207-kdc-installation-guide/039.png)</td>
<td><p>For more information on KIDS, please refer to the KIDS documentation in HTML format on the Kernel Home Page at the following web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/vdl/#App11">http://vista.med.va.gov/vdl/#App11</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Verify the Client/Server Installation of the Kernel Delphi Components *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the server installation is complete, verify that everything was installed correctly.

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![](xu-8-207-kdc-installation-guide/040.png) | Follow the procedures on how to run a program as described in your operating system's Systems Manual. |

\*\*\* You have now completed the Kernel Delphi Components installation on the V*ISTA* M server \*\*\*

> Upon completing the installation of the Kernel Delphi Component (KDC) software on both the V*IST*A M Server *and* client workstation(s), you are now ready to work with the KDC and install V*IST*A GUI applications that use the Kernel Delphi Components.