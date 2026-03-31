---
title: MailMan Version 8 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: XM
app_name: MailMan
section: INF
app_status: active
pkg_ns: XM
patch_ver: 8
patch_id: XM*8
group_key: "XM:XM:8"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this guide is to provide instructions for installing the Veterans Health Information Systems and Technology Architecture (VistA) Infrastructure & Security Service's (ISS) MailMan software, Version 8.0.
audience: 
keywords: 
  - mailman
  - strong
  - blockquote
  - table
  - installation
  - vista
  - class
  - guide
  - software
  - contents
page_count: 0
word_count: 3059
section_count: 5
table_count: 26
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_installguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_installguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=15"
---

![](mailman-version-8-installation-guide/001.png)

MAILMANINSTALLATION GUIDE

August 2002

VistA Health Systems Design & Development (HSD&D)

Infrastructure and Security Services (ISS)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation Revisions

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 41%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/23/02</td>
<td>1.0</td>
<td>Initial MailMan V. 8.0 software and documentation release. MailMan V. 8.0 was first released as "DNS-Aware MailMan" in a supplemental document released in August 2002. However, the remaining MailMan documentation set was never updated.</td>
<td>Thom Blom and Gary Beuschel Oakland, CA Office of Information Field Office (OIFO)</td>
</tr>
<tr class="even">
<td>09/21/06</td>
<td>2.0</td>
<td><p>MailMan V. 8.0 documentation reformatting/revision.</p>
<p>Reformatted document to follow the latest ISS styles and guidelines.</p>
<p>As of this date, all content updates have been completed for all released MailMan patches.</p>
<p>Also, reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: XMPATIENT,[N] or XMUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., XMPATIENT, ONE, XMPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td><p>MailMan Development Team Oakland, CA Office of Information Field Office (OIFO):</p>
<ul>
<li><blockquote>
<p>Maintenance Project Manager—Jack Schram</p>
</blockquote></li>
<li><blockquote>
<p>Project Planner—Laura Rowland</p>
</blockquote></li>
<li><blockquote>
<p>Developers—Gary Beuschel</p>
</blockquote></li>
<li><blockquote>
<p>Technical Writer—Thom Blom</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc93384736" class="anchor"></span>Table i. Documentation revision history

Patch Revisions

For a complete list of patches released with this software, please refer to the Patch Module on FORUM.

Contents

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Planning (CP) Service's MailMan Project Team consists of the following Development and Infrastructure Service (DaIS) personnel:

- REDACTED

The Capacity Planning Service's MailMan Project Team would like to thank the following sites/organizations/personnel for their assistance in reviewing and/or testing MailMan V. 8.0 software and documentation (sites are listed alphabetically):

- REDACTED

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This *MailMan Installation Guide* is intended for use in conjunction with Veterans Health Information Systems and Technology Architecture (VistA) MailMan. It acquaints system managers with the utilities, software structure and functionality of the MailMan system modules, including information about the routines, options, fields, and files that comprise MailMan and are used to implement and maintain MailMan. It also has information about MailMan's structure and recommendations regarding MailMan's efficient use. Additional information on installation, security, management features, and other requirements is also included. It does *not* describe the MailMan user interface nor does it detail its use in software development.

The intended audience of this manual is all primary (key) stakeholders. The primary stakeholders include:

- VistA Infrastructure and Security Services (ISS) Development Team.
- Other VistA project development teams and programmers.
- Information Resource Management (IRM) personnel responsible for installing, implementing, and maintaining MailMan.
- Enterprise VistA Support (EVS).

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of MailMan V. 8.0 and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products. This manual discusses the installation of MailMan V. 8.0.

There are no special legal requirements involved in the use of MailMan.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                |                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                     | Description                                                                                                     |
| ![](mailman-version-8-installation-guide/002.png) | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](mailman-version-8-installation-guide/003.png)                                                              | CAUTION or DISCLAIMER: Used to inform the reader to take special notice of critical information.                |

<span id="_Toc18213793" class="anchor"></span>Table ii. Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
  - Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., roll-and-scroll screen or character-based screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts will be boldface.
- References to "\<Enter\>" within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/004.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

|                                                                                                                |                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/005.png) | NOTE: Unless otherwise noted, all sample screen captures/dialogue boxes in this manual are derived from using either MailMan's Detailed or Summary Full Screen message readers. |

- This manual refers in many places to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS will be considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/006.png) | NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of the software.

In addition to the "question mark" help, you can use the Help (User/Group Info., etc.) menu option on the main MailMan Menu to access the MailMan Help Frames through the following options:

- New Features in MailMan
- General MailMan Information
- Questions and Answers on MailMan
- Manual for MailMan Users

|                                                                                                                |                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/007.png) | REF: For more information on obtaining MailMan online help, please refer to Chapter 12, "Online Help Information" in the *MailMan User Guide*. |

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/008.png) | REF: For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" topic of the *VA FileMan Advanced User Guide*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language

This manual provides an overall explanation of MailMan and the functionality contained in MailMan V. 8.0. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) and VA Intranet for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following Intranet Web address:

> <http://vista.med.va.gov/>

Reference Materials

Readers who wish to learn more about MailMan should consult the following:

- *MailMan Release Notes*
- *MailMan Installation Guide* (this manual)
- *MailMan Getting Started Guide*
- *MailMan Developer's Guide*
- *MailMan User Guide*
- *MailMan Network Reference Guide*
- *MailMan Package Security Guide*
- *MailMan Systems Management Guide*
- *MailMan Technical Manual*
- MailMan Home Page at the following Web address:

> <http://vista.med.va.gov/mailman/index.asp>

> This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-installation-guide/009.png)</td>
<td><p><strong>REF:</strong> For more information on the use of the Adobe Acrobat Reader, please refer to the "Adobe Acrobat Quick Guide" at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">http://vista.med.va.gov/iss/acrobat/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

VistA documentation can be downloaded from the Health Systems Design and Development (HSD&D) VistA Documentation Library (VDL) Web site:

> <http://www.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Enterprise VistA Support (EVS) anonymous directories:

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED
- Preferred Method REDACTED

> This method transmits the files from the first available FTP server.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/010.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Preliminary Consideration


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [Acknowledgements](#acknowledgements)
  - [Orientation](#orientation)
- [Preliminary Consideration](#preliminary-consideration)
    - [Purpose](#purpose)
    - [About the Installation Procedures](#about-the-installation-procedures)
    - [MailMan Distribution Files](#mailman-distribution-files)
    - [VistA M Server Requirements](#vista-m-server-requirements)
    - [Skills Needed for Installation](#skills-needed-for-installation)
- [VistA M Server Installation Instructions](#vista-m-server-installation-instructions)
    - [Version 8.0 Installation](#version-80-installation)

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for installing the Veterans Health Information Systems and Technology Architecture (VistA) Infrastructure & Security Service's (ISS) MailMan software, Version 8.0.

### About the Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We recommend sites take the following approach to installing the MailMan software:
> 1\. Obtain the MailMan V. 8.0 documentation.
|                                                                                                                |                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/011.png) | REF: For more information on the MailMan documentation, please refer to the "Error! Reference source not found." topic in the "Orientation" section in this manual. |
> 2\. Install the MailMan V. 8.0 server software in a Test account prior to installing it in a Production account.
> 3\. Obtain and install all released patches for the MailMan V. 8.0 software.
|                                                                                                                |                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/012.png) | REF: For the current patch history related to this software, please refer to the Patch Module on FORUM. |

### MailMan Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 9%" />
<col style="width: 65%" />
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
<td>XM8_0RN.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>Release Notes</strong></td>
</tr>
<tr class="even">
<td>XM8_0IG.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>Installation Guide</strong></td>
</tr>
<tr class="odd">
<td>XM8_0GS.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>Getting Started Guide</strong></td>
</tr>
<tr class="even">
<td>XM8_0UM.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>User Guide</strong></td>
</tr>
<tr class="odd">
<td>XM8_0PM.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>Developer's Guide</strong></td>
</tr>
<tr class="even">
<td>XM8_0SM.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>Systems Management Guide</strong></td>
</tr>
<tr class="odd">
<td>XM8_0NET.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>Network Reference Guide</strong></td>
</tr>
<tr class="even">
<td>XM8_0TM.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>Technical Manual</strong></td>
</tr>
<tr class="odd">
<td>XM8.KID (release)</td>
<td>ASCII</td>
<td><p><strong>KIDS Distribution.</strong> Required for all installations. Contains the MailMan V. 8.0 server software:</p>
<ul>
<li><blockquote>
<p>Globals and VA FileMan files</p>
</blockquote></li>
<li><blockquote>
<p>Server Routines</p>
</blockquote></li>
<li><blockquote>
<p>Options</p>
</blockquote></li>
<li><blockquote>
<p>Security Keys</p>
</blockquote></li>
<li><blockquote>
<p>Mail Groups</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>MailMan VistA M Server Patches</td>
<td>ASCII</td>
<td><strong>MailMan Patches.</strong> KIDS builds for MailMan patches. Follow normal procedures to obtain and install all MailMan patches (see FORUM).</td>
</tr>
</tbody>
</table>
<span id="_Hlt396118096" class="anchor"></span>Table 1‑1: MailMan-related software distribution files

### VistA M Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools and network configuration are required on the VistA M Server in order to install and use the MailMan software:
<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Minimum Software/Configuration</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Operating System Software</td>
<td><p>The following operating systems are supported:</p>
<ul>
<li><blockquote>
<p>InterSystems Caché operating system</p>
</blockquote></li>
<li><blockquote>
<p>Greystone Technology MUMPS (GT.M) on Linux</p>
</blockquote></li>
</ul>
<p>![](mailman-version-8-installation-guide/013.png) <strong>NOTE:</strong> The VistA M Server need not be an NT system.</p></td>
</tr>
<tr class="even">
<td>Fully Patched M Accounts</td>
<td><p>You should have both a development Test account and a Production account for the MailMan software.</p>
<p>The account(s) <em>must</em> contain the <em>fully</em> patched versions (except where noted) of the following software (listed alphabetically):</p>
<ul>
<li><blockquote>
<p>Kernel V. 8.0</p>
</blockquote></li>
</ul>
<p>![](mailman-version-8-installation-guide/014.png) CAUTION: MailMan V. 8.0 requires a site already have Kernel V. 8.0 installed and running, and that it is fully patched through at least Kernel Patch XU*8.0*216.</p>
<ul>
<li><blockquote>
<p>Kernel Toolkit V. 7.3</p>
</blockquote></li>
<li><blockquote>
<p>MailMan V. 7.1</p>
</blockquote></li>
</ul>
<p>![](mailman-version-8-installation-guide/015.png) CAUTION: MailMan V. 8.0 requires a site already have MailMan V. 7.1 installed and running, and that it is fully patched through at least MailMan Patch XM*7.1*198.</p>
<ul>
<li><blockquote>
<p>VA FileMan V. 22.0</p>
</blockquote></li>
</ul>
<p>![](mailman-version-8-installation-guide/016.png) CAUTION: MailMan V. 8.0 requires a site already have VA FileMan V. 22.0 installed and running, and that it is fully patched through at least VA FileMan Patch DI*22*68.</p>
<p>![](mailman-version-8-installation-guide/017.png) <strong>NOTE:</strong> These software packages <em>must</em> be properly installed and <em>fully</em> patched (except where noted) prior to installing the MailMan V. 8.0 software distribution. You can obtain all released VistA M server-side patches (including patch description and installation instructions) from the Patch module on FORUM or through normal procedures. Patches must be installed in published sequence.</p></td>
</tr>
<tr class="odd">
<td><p>Network Communications Software</p>
<p>![](mailman-version-8-installation-guide/018.png) <strong>REF:</strong> For more information on telecommunications support, please visit the VHA Communication Services Office (CSO) Home Page:</p>
<blockquote>
<p><a href="http://vaww.va.gov/cso/">REDACTED</a></p>
</blockquote></td>
<td>The VistA M Server needs to have TCP/IP running.</td>
</tr>
</tbody>
</table>
<span id="_Toc135121869" class="anchor"></span>Table 1‑2. VistA M Server minimum software/network tools/utilities required for MailMan V. 8.0

### Skills Needed for Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Skills required to perform the installation are listed below. Instructions for performing these functions are provided in vendor-supplied operating system manuals as well as VistA publications.
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-installation-guide/019.png)</td>
<td><p><strong>REF:</strong> Caché for NT and OpenVMS sites should refer to the AVANTI How-To Web site currently located at:</p>
<blockquote>
<p><a href="http://vaww.va.gov/custsvc/cssupp/avanti/How-to.HTM">REDACTED</a></p>
</blockquote></td>
</tr>
</tbody>
</table>
You need to know how to do the following:
- Back up the system
- Copy files using commands of the host file system
- Run a Kernel Installation & Distribution System (KIDS) installation
- Switch User Class Identification (UCI) accounts
- Enable/Disable routine mapping and journaling
- Manage globals, including global placement, protection, and translation
- Run a system status and restore a job

# VistA M Server Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan V. 8.0 should be installed with users off the system. The installation time should not take more than a few minutes.

The instructions in this section are applicable for the Test/Production accounts in the Caché environment. Any unique instructions for a specific environment will be notated within the procedure.

|                                                                                                                |                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/020.png) | NOTE: All Caché for Windows NT or Caché for OpenVMS sites should install this software. |

### Version 8.0 Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Retrieve the XM8.KID File *(required)*

> Obtain the XM8.KID file, which contains the MailMan V. 8.0 software, from the Enterprise VistA Support (EVS) ANONYMOUS.SOFTWARE directory located at:

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED
- VistA Download Site REDACTED

#### Verify KIDS Install Platform *(required)*

> Verify that the Kernel Installation and Distribution System (KIDS) platform on your system is ready to install VistA M Server patches.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-installation-guide/021.png)</td>
<td><p><strong>REF:</strong> For more information on KIDS, please refer to the KIDS section in the <em>Kernel Systems Manual</em> located on the VDL at the following Web address:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/Infrastructure.asp?appID=10">http://www.va.gov/vdl/Infrastructure.asp?appID=10</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

> a\. Verify Host File Server (HFS) Device in the DEVICE File (#3.5)—Verify that you have a Host File Server (HFS) device in the DEVICE file (#3.5) named "HFS". If you have performed KIDS installations on the VistA M Server before, you probably already have an appropriate HFS device set up. If you don't have an entry for this device, you *must* create one.

|                                                                                                                |                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/022.png) | REF: For information on how to create an HFS device, please refer to Chapter 18, "Host Files," in the *Kernel Systems Manual*. |

> b\. Verify Null Device in the DEVICE File (#3.5)—Verify that you have a Null device in the DEVICE file (#3.5) named "NULL" (or whose mnemonic is named "NULL").

> You can have other devices with similar names, but one device is needed whose name or mnemonic is "NULL." The subtype should be a "P-" subtype (e.g., P-OTHER), the margin should be a minimum of 80, and the page length should be a minimum of 60.

> Sample setups:

> Caché for OpenVMS Null Device Setup Example

> NAME: NULL \$I: \_NLA0:

> ASK DEVICE: NO ASK PARAMETERS: NO

> SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: Bit Bucket

> SUBTYPE: P-OTHER TYPE: TERMINAL

> Caché/NT Null Device Setup Example

> NAME: NULL \$I: //./nul

> ASK DEVICE: NO ASK PARAMETERS: NO

> SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: BIT BUCKIT

> SUBTYPE: P-OTHER TYPE: TERMINAL

> P-OTHER Terminal Type Setup Example

> NAME: P-OTHER RIGHT MARGIN: 132

> FORM FEED: \# PAGE LENGTH: 64

> BACK SPACE: \$C(8) DESCRIPTION: General prntr (132)

#### Load XM8.KID File *(required)*

> Use Kernel Installation & Distribution System (KIDS) to load the distribution. From the KIDS menu, select the Installation menu option. Invoke the Load a Distribution option to load the following software:

> XM8.KID

> The following is sample dialogue of a load of the MailMan V. 8.0 software done at the Oakland OIFO:

> Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 1 \<Enter\> Load a Distribution

> Enter a Host File: USR\$:\[ANONYMOUS\]XM8.KID;6

> KIDS Distribution saved on Mar 22, 2004@08:01:12

> Comment: MAILMAN 8.0

> This Distribution contains Transport Globals for the following Package(s):

> Build MAILMAN 8.0 has been loaded before, here is when:

> MAILMAN 8.0 Install Completed

> was loaded on July 23, 2002@09:15:33

> OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// \<Enter\>

> Loading Distribution...

> MAILMAN 8.0

> Use INSTALL NAME: MAILMAN 8.0 to install this Distribution.

<span id="_Toc44314852" class="anchor"></span>Figure 2‑1: Sample MailMan V. 8.0 distribution load

|                                                                                                                |                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/023.png) | NOTE: If you are prompted with "Want to RUN the Environment Check Routine? YES//", you should respond with YES. |

#### Install MailMan V. 8.0 Software *(required)*

> Use KIDS to Install the MailMan V. 8.0 software. Follow the KIDS installation prompts as you would any other KIDS installation. Specific prompts and suggested responses are notated below:

> a\. Users should be off the system during installation of this patch and software.

> b\. You do not need to stop TaskMan.

> c\. You may elect to use any of the following options within the KIDS Installation menu:

- Verify Checksums in Transport Global—This option allows you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global.
- Compare Transport Global to Current System—This option allows you to view all changes that will be made when the release is installed. It compares all components of the release (routines, DDs, templates, etc.).
- Backup a Transport Global—This option creates a backup message of any routines exported with this release. It will *not* back up any other changes such as DDs or templates.
- Install Package(s).

> d\. When prompted for the INSTALL NAME, enter the following:

> MAILMAN 8.0

> e\. When prompted to rebuild menu trees:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

> You can respond with NO and not rebuild the menus until the normal scheduled menu rebuild takes place or YES to rebuild the menus immediately after the installation.

> f\. When prompted to inhibit logons:

> Want KIDS to INHIBIT LOGONs during the install? YES//

> You can respond with NO.

> g\. When prompted to disable options and protocols:

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

> You can respond with NO.

> MailMan V. 8.0 Software Installation Sample

> The following is sample dialogue of an installation of the MailMan V. 8.0 software done at the Oakland OIFO:

> NAME: MAILMAN 8.0 PACKAGE FILE LINK: MAILMAN

> DATE LOADED: JUL 23, 2002@09:55:40 STARTING PACKAGE: MAILMAN 8.0

> INSTALL ORDER: 1 REQUIRED TO CONTINUE: NO

> SETNAME: 0MAILMAN 8.0 STATUS: Install Completed

> DISABLE OPTION DELAY: 0 INSTALLED BY: XMUSER,ZERO

> INSTALL START TIME: JUL 23, 2002@09:56:36

> ROUTINE INSTALL TIME: JUL 23, 2002@09:56:41

> INSTALL COMPLETE TIME: JUL 23, 2002@09:58:09

> DISTRIBUTION DATE: JUL 23, 2002

> FILE COMMENT: MailMan 8.0 7/24/2002 ;Created on Jul 23, 2002@09:41:26

> FILE: COMMUNICATIONS PROTOCOL

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:41

> FILE: BULLETIN

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:41

> FILE: MAILBOX

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:43

> FILE: MESSAGES TO BE NEW AT A LATER DATE

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:43

> FILE: MAIL GROUP

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:44

> FILE: DISTRIBUTION LIST

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:44

> FILE: MESSAGE

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:45

> FILE: DOMAIN

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:46

> FILE: INTER-UCI TRANSFER

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:46

> FILE: MAILMAN OUTSTANDING FTP TRANSACTIONS

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:46

> FILE: INTERNET SUFFIX

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:46

> FILE: REMOTE USER DIRECTORY

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:46

> FILE: MESSAGE DELIVERY STATS

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:47

> FILE: MESSAGE STATISTICS

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:47

> FILE: MAILMAN SITE PARAMETERS

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:48

> FILE: MAILMAN TIME ZONE

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:48

> FILE: NETWORK SENDERS REJECTED

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:48

> FILE: TRANSMISSION SCRIPT

> DATA DICTIONARY TIME: JUL 23, 2002@09:56:48

> PRE-INIT CHECK POINTS: XPD PREINSTALL COMPLETED

> COMPLETED TIME: JUL 23, 2002@09:56:41

> PRE-INIT CHECK POINTS: XPD PREINSTALL STARTED

> COMPLETED TIME: JUL 23, 2002@09:56:41

> CALLBACK: PRE^XMYPRE

> POST-INIT CHECK POINTS: XPD POSTINSTALL COMPLETED

> COMPLETED TIME: JUL 23, 2002@09:58:05

> POST-INIT CHECK POINTS: XPD POSTINSTALL STARTED

> COMPLETED TIME: JUL 23, 2002@09:58:05

> CALLBACK: POST^XMYPRE

> BUILD COMPONENT: PRINT TEMPLATE DATA TIME: JUL 23, 2002@09:57:08

> INSTALL ORDER: 5

> BUILD COMPONENT: SORT TEMPLATE DATA TIME: JUL 23, 2002@09:57:08

> INSTALL ORDER: 6

> BUILD COMPONENT: FUNCTION DATA TIME: JUL 23, 2002@09:57:08

> INSTALL ORDER: 4

> BUILD COMPONENT: DIALOG DATA TIME: JUL 23, 2002@09:57:46

> INSTALL ORDER: 9

> BUILD COMPONENT: BULLETIN DATA TIME: JUL 23, 2002@09:57:07

> INSTALL ORDER: 2

> BUILD COMPONENT: MAIL GROUP DATA TIME: JUL 23, 2002@09:57:46

> INSTALL ORDER: 11

> BUILD COMPONENT: HELP FRAME DATA TIME: JUL 23, 2002@09:57:07

> INSTALL ORDER: 1

> BUILD COMPONENT: OPTION DATA TIME: JUL 23, 2002@09:58:05

> INSTALL ORDER: 18

> BUILD COMPONENT: SECURITY KEY DATA TIME: JUL 23, 2002@09:57:08

> INSTALL ORDER: 3

> MESSAGES:

> Install Started for MAILMAN 8.0 :

> Jul 23, 2002@09:56:36

> Build Distribution Date: Jul 23, 2002

> Installing Routines:

> Jul 23, 2002@09:56:41

> Running Pre-Install Routine: PRE^XMYPRE

> Installing Data Dictionaries:

> Jul 23, 2002@09:56:49

> Installing PACKAGE COMPONENTS:

> Installing HELP FRAME

> Installing BULLETIN

> Installing SECURITY KEY

> Installing FUNCTION

> Installing PRINT TEMPLATE

> Installing SORT TEMPLATE

> Installing DIALOG

> Installing MAIL GROUP

> Installing OPTION

> Jul 23, 2002@09:58:05

> Running Post-Install Routine: POST^XMYPRE

> Updating Routine file...

> Updating KIDS files...

> MAILMAN 8.0 Installed.

> Jul 23, 2002@09:58:09

> Install Message sent \#1453166

> Call MENU rebuild

> NAME: XPM14#1 ANSWER: 230

> PROMPT: Enter the Coordinator for Mail Group 'XM SUPER SEARCH'

> EXTERNAL ANSWER: XMUSER,ISO

> NAME: XPO1 ANSWER: 1

> PROMPT: Want KIDS to Rebuild Menu Trees Upon Completion of Install

> EXTERNAL ANSWER: YES

> NAME: XPI1 ANSWER: 0

> PROMPT: Want KIDS to INHIBIT LOGONs during the install

> EXTERNAL ANSWER: NO

> NAME: XPZ1 ANSWER: 0

> PROMPT: Want to DISABLE Scheduled Options, Menu Options, and Protocols

> EXTERNAL ANSWER: NO

> ROUTINES: XM

> ROUTINES: XMA

> ROUTINES: XMA0

> ROUTINES: XMA03

> ROUTINES: XMA11

> ROUTINES: XMA11A

> ROUTINES: XMA1B

> ROUTINES: XMA1C

> ROUTINES: XMA2

> ROUTINES: XMA21

> ROUTINES: XMA21C

> ROUTINES: XMA2B

> ROUTINES: XMA2R

> ROUTINES: XMA3

> ROUTINES: XMA30

> ROUTINES: XMA32

> ROUTINES: XMA32A

> ROUTINES: XMA7

> ROUTINES: XMAD2

> ROUTINES: XMADGO

> ROUTINES: XMAFTP

> ROUTINES: XMAH

> ROUTINES: XMAH1

> ROUTINES: XMAI2

> ROUTINES: XMAPBLOB

> ROUTINES: XMAPHOST

> ROUTINES: XMASEC

> ROUTINES: XMB

> ROUTINES: XMBBLOB

> ROUTINES: XMBGRP

> ROUTINES: XMC

> ROUTINES: XMC1

> ROUTINES: XMC11

> ROUTINES: XMC1A

> ROUTINES: XMC1B

> ROUTINES: XMCB

> ROUTINES: XMCD

> ROUTINES: XMCDNT

> ROUTINES: XMCE

> ROUTINES: XMCP

> ROUTINES: XMCQ

> ROUTINES: XMCQA

> ROUTINES: XMCQH

> ROUTINES: XMCSIZE

> ROUTINES: XMCTLK

> ROUTINES: XMCTRAP

> ROUTINES: XMCU1

> ROUTINES: XMCX

> ROUTINES: XMCXT

> ROUTINES: XMCXU

> ROUTINES: XMD

> ROUTINES: XMDIR1

> ROUTINES: XMDIR1A

> ROUTINES: XMDIR1B

> ROUTINES: XMDIRQST

> ROUTINES: XMDIRRCV

> ROUTINES: XMDIRSND

> ROUTINES: XMFAX

> ROUTINES: XMGAPI0

> ROUTINES: XMGAPI1

> ROUTINES: XMGAPI2

> ROUTINES: XMGAPI3

> ROUTINES: XMGAPI4

> ROUTINES: XMHIG

> ROUTINES: XMHIU

> ROUTINES: XMJBL

> ROUTINES: XMJBM

> ROUTINES: XMJBM1

> ROUTINES: XMJBN

> ROUTINES: XMJBN1

> ROUTINES: XMJBU

> ROUTINES: XMJDIR

> ROUTINES: XMJERR

> ROUTINES: XMJMA

> ROUTINES: XMJMBULL

> ROUTINES: XMJMC

> ROUTINES: XMJMCODE

> ROUTINES: XMJMD

> ROUTINES: XMJMF

> ROUTINES: XMJMF1

> ROUTINES: XMJMF2

> ROUTINES: XMJMFA

> ROUTINES: XMJMFB

> ROUTINES: XMJMFC

> ROUTINES: XMJML

> ROUTINES: XMJMLN

> ROUTINES: XMJMLR

> ROUTINES: XMJMLR1

> ROUTINES: XMJMOI

> ROUTINES: XMJMOI1

> ROUTINES: XMJMOIE

> ROUTINES: XMJMOR

> ROUTINES: XMJMORX

> ROUTINES: XMJMORX1

> ROUTINES: XMJMP

> ROUTINES: XMJMP1

> ROUTINES: XMJMP2

> ROUTINES: XMJMQ

> ROUTINES: XMJMQ1

> ROUTINES: XMJMR

> ROUTINES: XMJMR1

> ROUTINES: XMJMRO

> ROUTINES: XMJMS

> ROUTINES: XMJMSA

> ROUTINES: XMJMSO

> ROUTINES: XMJMT

> ROUTINES: XMKP

> ROUTINES: XMKP1

> ROUTINES: XMKPL

> ROUTINES: XMKPLQ

> ROUTINES: XMKPO

> ROUTINES: XMKPR

> ROUTINES: XMKPR1

> ROUTINES: XMKPRD

> ROUTINES: XML

> ROUTINES: XML1CRC

> ROUTINES: XML4CRC

> ROUTINES: XML4CRC1

> ROUTINES: XMLPC

> ROUTINES: XMLSWP

> ROUTINES: XMLSWP0

> ROUTINES: XMLSWP2

> ROUTINES: XMLTCP

> ROUTINES: XMM1

> ROUTINES: XMM2

> ROUTINES: XMNTEG

> ROUTINES: XMNTEG0

> ROUTINES: XMP

> ROUTINES: XMP2

> ROUTINES: XMP2A

> ROUTINES: XMP3

> ROUTINES: XMPC

> ROUTINES: XMPG

> ROUTINES: XMPH

> ROUTINES: XMPSEC

> ROUTINES: XMR

> ROUTINES: XMR0BLOB

> ROUTINES: XMR1

> ROUTINES: XMR2

> ROUTINES: XMR3

> ROUTINES: XMR3A

> ROUTINES: XMR4

> ROUTINES: XMRENT

> ROUTINES: XMRFTP

> ROUTINES: XMRFTPUX

> ROUTINES: XMRINETD

> ROUTINES: XMRMSM

> ROUTINES: XMRONT

> ROUTINES: XMRPCTS

> ROUTINES: XMRPCTS0

> ROUTINES: XMRPCTS1

> ROUTINES: XMRPCTSA

> ROUTINES: XMRPOP

> ROUTINES: XMRTCP

> ROUTINES: XMRTCPGO

> ROUTINES: XMRUCX

> ROUTINES: XMS

> ROUTINES: XMS0BLOB

> ROUTINES: XMS1

> ROUTINES: XMS2

> ROUTINES: XMS3

> ROUTINES: XMSFTP

> ROUTINES: XMSFTPUX

> ROUTINES: XMTDF

> ROUTINES: XMTDL

> ROUTINES: XMTDL1

> ROUTINES: XMTDL2

> ROUTINES: XMTDO

> ROUTINES: XMTDR

> ROUTINES: XMTDT

> ROUTINES: XMUCXPOP

> ROUTINES: XMUDCHK

> ROUTINES: XMUDCHR

> ROUTINES: XMUDNC

> ROUTINES: XMUDTOP

> ROUTINES: XMUPIN

> ROUTINES: XMUT1

> ROUTINES: XMUT1A

> ROUTINES: XMUT2

> ROUTINES: XMUT4

> ROUTINES: XMUT41

> ROUTINES: XMUT4A

> ROUTINES: XMUT4C

> ROUTINES: XMUT5

> ROUTINES: XMUT5B

> ROUTINES: XMUT5C

> ROUTINES: XMUT5G

> ROUTINES: XMUT5Q

> ROUTINES: XMUT5Q1

> ROUTINES: XMUT5R1

> ROUTINES: XMUT5R2

> ROUTINES: XMUT6

> ROUTINES: XMUT7

> ROUTINES: XMUTCOM1

> ROUTINES: XMUTERM

> ROUTINES: XMUTERM1

> ROUTINES: XMUTERM2

> ROUTINES: XMUTPUR0

> ROUTINES: XMVGROUP

> ROUTINES: XMVGRP

> ROUTINES: XMVSURR

> ROUTINES: XMVVITA

> ROUTINES: XMVVITAE

> ROUTINES: XMXADDR

> ROUTINES: XMXADDR1

> ROUTINES: XMXADDR2

> ROUTINES: XMXADDR3

> ROUTINES: XMXADDR4

> ROUTINES: XMXADDRD

> ROUTINES: XMXADDRG

> ROUTINES: XMXANSER

> ROUTINES: XMXAPI

> ROUTINES: XMXAPIB

> ROUTINES: XMXAPIG

> ROUTINES: XMXAPIU

> ROUTINES: XMXBSKT

> ROUTINES: XMXBULL

> ROUTINES: XMXEDIT

> ROUTINES: XMXGRP

> ROUTINES: XMXGRP1

> ROUTINES: XMXLIST

> ROUTINES: XMXLIST1

> ROUTINES: XMXLIST2

> ROUTINES: XMXMBOX

> ROUTINES: XMXMSGS

> ROUTINES: XMXMSGS1

> ROUTINES: XMXMSGS2

> ROUTINES: XMXPARM

> ROUTINES: XMXPARM1

> ROUTINES: XMXPARMB

> ROUTINES: XMXPRT

> ROUTINES: XMXREPLY

> ROUTINES: XMXSEC

> ROUTINES: XMXSEC1

> ROUTINES: XMXSEC2

> ROUTINES: XMXSEC3

> ROUTINES: XMXSEND

> ROUTINES: XMXTO

> ROUTINES: XMXUTIL

> ROUTINES: XMXUTIL1

> ROUTINES: XMXUTIL2

> ROUTINES: XMXUTIL3

> ROUTINES: XMXUTIL4

> ROUTINES: XMYPRE

<span id="_Toc44314854" class="anchor"></span>Figure 2‑2: Sample MailMan V. 8.0 installation

#### Post Installation Routine *(required)*

> IRM personnel at all sites should invoke VA FileMan using D Q^DI to review/modify the following field in the MAILMAN SITE PARAMETERS file (#4.3):

- DNS AWARE (#8.22)—IRM should set this field to Yes to make MailMan DNS-Aware. MailMan will use the IP addresses in the domain scripts, but if they fail or do not exist, MailMan will use DNS to ascertain other IP addresses to try. MailMan will replace failed script IP address with the successful DNS IP address.

#### Install All Released Patches *(required)*

> At the time of publication of this manual, several VistA M Server-side patches have been released with the MailMan V. 8.0 software.

> a\. Obtain all released MailMan patches. Follow the normal procedures to obtain released patches from the Patch Module on FORUM.

> b\. All VistA M Server patches are distributed in Kernel V. 8.0 KIDS format. Using KIDS, load and install the MailMan-related VistA M Server patches.

> c\. Follow the instructions under the "Installation Instructions" section in the patch description in order to install each patch.

#### Review MailMan Site Parameters *(recommended)*

> Use the MailMan Site Parameters option \[XMKSP\] under the Manage MailMan menu \[XMMGR\] to review the MailMan site parameters and change appropriate field values for your site.

|                                                                                                                |                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-installation-guide/024.png) | REF: For more information on the MailMan Site Parameters option \[XMKSP\], please refer to the "Manage MailMan" topic in Chapter 2, "Implementation and Maintenance," in the *MailMan Systems Management Guide*. |