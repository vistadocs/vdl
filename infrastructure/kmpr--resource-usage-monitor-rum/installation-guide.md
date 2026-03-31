---
title: KMPR Version 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: KMPR
app_name: Resource Usage Monitor (RUM)
section: INF
app_status: active
pkg_ns: KMPR
patch_ver: 2
patch_id: KMPR*2
group_key: "KMPR:KMPR:2"
file_numbers: []
security_keys: []
menu_options: 2
description: The purpose of this guide is to provide instructions for installing the Veterans Health Information Systems and Technology Architecture (VistA) Capacity Planning (CP) Services' Resource Usage Monitor (RUM) software, version 2.0.
audience: 
keywords: 
  - table
  - installation
  - software
  - kmpr
  - strong
  - contents
  - class
  - global
  - blockquote
  - monitor
page_count: 0
word_count: 3737
section_count: 4
table_count: 46
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Resource_Usage_Mon/kmpr2_0ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Resource_Usage_Mon/kmpr2_0ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=130"
---

![](kmpr-version-2-installation-guide/001.png)

RESOURCE USAGE MONITOR (RUM)RELEASE NOTES &  
INSTALLATION GUIDE

June 2003

VistA Health Systems Design & Development (HSD&D)

Development and Infrastructure Support (DaIS)

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
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>06/27/03</td>
<td>1.0</td>
<td>Initial Resource Usage Monitor V. 2.0 software documentation creation.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/17/03</td>
<td>1.1</td>
<td>Updated documentation for format and minor miscellaneous edits (no change pages issued)</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>01/12/05</td>
<td>1.2</td>
<td><p>Re-titled document to from "Installation Guide" to "Release Notes &amp; Installation Guide."</p>
<p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: KMPDPATIENT,[N] or KMPDUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., KMPDPATIENT, ONE, KMPDPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
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

<span id="_Toc56819157" class="anchor"></span>Table i: Documentation revision history

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

Contents

Figures and Tables

## Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Planning (CP) Services' Resource Usage Monitor (RUM) Project Team consists of the following Development and Infrastructure Service (DaIS) personnel:

- REDACTED

Capacity Planning (CP) Services' RUM Project Team would like to thank the following sites/organizations/personnel for their assistance in reviewing and/or testing the RUM V. 2.0 software and documentation (names within teams are listed alphabetically):

- REDACTED

## ## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of Resource Usage Monitor (RUM) software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                                     |                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                                          | Description                                                                                               |
| ![](kmpr-version-2-installation-guide/002.png)                      | Used to inform the reader of general information including references to additional reading material.         |
| ![](kmpr-version-2-installation-guide/003.png)                                                                                   | Used to caution the reader to take special notice of critical information.                                    |
| ![](kmpr-version-2-installation-guide/004.png) | Used to denote special installation instructions only (e.g. virgin installations or platform-specific steps). |

<span id="_Ref345831418" class="anchor"></span>Table ii: Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) will be in the "000" or "666."
  - Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- HL7 messages, "snapshots" of computer online displays (i.e., roll-and-scroll screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts will be boldface type. The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

> Select Primary Menu option: ??

- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/005.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/006.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. Please refer to the *Resource Usage Monitor (RUM) Technical Manual* for further information. |

Help at Prompts

VistA software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in any VistA character-based product:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/007.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment (e.g., Kernel Installation and Distribution System \[KIDS\])
- VA FileMan data structures and terminology
- Microsoft Windows
- M programming language

It provides an overall explanation of configuring the Resource Usage Monitor (RUM) interface and the changes contained in Resource Usage Monitor (RUM) Version 2.0. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following Web address:

> <http://vista.med.va.gov/>

Reference Materials

Readers who wish to learn more about the Resource Usage Monitor (RUM) software should consult the following:

- *Resource Usage Monitor (RUM) Release Notes & Installation Guide* (this manual)
- *Resource Usage Monitor (RUM) User Manual*
- *Resource Usage Monitor (RUM) Technical Manual*
- Capacity Planning (CP) Services' Home Page (for more information on Capacity Planning) at the following temporary Web address:

> [<http://vista.med.va.gov/capman/default.htm>](http://vista.med.va.gov/capman/index.html)

> This site contains additional information and documentation.

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-installation-guide/008.png)</td>
<td><p>For more information on the use of the Adobe Acrobat Reader, please refer to the <em>Adobe Acrobat Quick Guide</em> at the following Web address:</p>
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
- Salt Lake City OIFO [REDACTED](ftp://ftp.fo-slc.med.va.gov)
- Preferred Method REDACTED

> This method transmits the files from the first available FTP server.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/009.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Acknowledgements](#acknowledgements)
  - [## Orientation](#orientation)
- [Release Notes](#release-notes)
- [Preliminary Consideration](#preliminary-consideration)
    - [Purpose](#purpose)
    - [About the Installation Procedures](#about-the-installation-procedures)
    - [Resource Usage Monitor (RUM) Distribution Files](#resource-usage-monitor-rum-distribution-files)
    - [VistA M Server Requirements](#vista-m-server-requirements)
    - [Skills Needed for Installation](#skills-needed-for-installation)
- [VistA M Installation Instructions](#vista-m-installation-instructions)
    - [Virgin Installations](#virgin-installations)
    - [Upgrade Installations](#upgrade-installations)
The Veterans Health Information Systems and Technology Architecture (VistA) Resource Usage Monitor (RUM) Version 2.0 software is now available. This enhanced RUM software has the following new features:
- Increased Efficiency—Reduces global hits by 2/3, thereby increasing software efficiency.
- Increased Speed—Most indirection has been removed from the DAILY and WEEKLY Application Program Interfaces (APIs) for increased speed.
- Timely Information—Software collects hourly counts for each option, protocol, and RPC.
- Enhanced Data:
- Distinguishes between prime time, non-prime time, weekend, and workweek data.
- Weekly data subject is separated by a tilde (~) for easier parsing of the data.
- New Option—The Print Hourly Occurrence Distribution option \[KMPR PRINT HOURLY OCCURRENCE\] is a new option. It prints a report listing the hourly occurrence of the specified option or task by system node, as well as the total amounts and number of users for a given time period.
- Enhanced Option—The Status of RUM Collection option \[KMPR STATUS COLLECTION\] has been enhanced. It is more informative for easier problem analysis, routine version/patch checking, and file data information.
- Expanded Report—The RUM Data for an Option option \[KMPR PRINT OPTION DATA\] has been expanded. It searches for Option/Task, Protocol, or RPC.
|                                                                                                                |                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/010.png) | For more information on specific options/reports, please refer to Chapter 3, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

# Preliminary Consideration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for installing the Veterans Health Information Systems and Technology Architecture (VistA) Capacity Planning (CP) Services' Resource Usage Monitor (RUM) software, version 2.0.

### About the Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Separate installation procedures are provided in this guide based on the installation type:

- Virgin Installations—Software never installed
- Upgrade Installation—Upgrade from existing software

We recommend sites take the following approach to installing the RUM software:

> 1\. Obtain the RUM V. 2.0 documentation.

|                                                                                                                |                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/011.png) | For more information on the RUM documentation, please refer to the "Reference Materials" topic in the "Orientation" section in this manual. |

> 2\. Install the server software in a Test account prior to installing it in a Production account.

There are no special legal requirements involved in the use of Resource Usage Monitor (RUM)'s interface.

### Resource Usage Monitor (RUM) Distribution Files

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
<td>KMPR2_0IG.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>Release Notes &amp; Installation Guide</strong>.</td>
</tr>
<tr class="even">
<td>KMPR2_0UM.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>User Manual</strong>.</td>
</tr>
<tr class="odd">
<td>KMPR2_0TM.PDF<br />
(documentation)</td>
<td>Binary</td>
<td><strong>Technical Manual</strong>.</td>
</tr>
<tr class="even">
<td>KMPR2_0.KID<br />
(release)</td>
<td>ASCII</td>
<td><p><strong>Kernel Installation &amp; Distribution System (KIDS) Distribution. Contains the following:</strong></p>
<ul>
<li><blockquote>
<p>Kernel Patch XU*8.0*186.</p>
</blockquote></li>
<li><blockquote>
<p>RUM V. 2.0 server software:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Globals (^KMPR, ^KMPTMP["KMPR"]) and VA FileMan files.</p>
</blockquote></li>
<li><blockquote>
<p>Server Routines.</p>
</blockquote></li>
<li><blockquote>
<p>Resource Usage Monitor (RUM) Options.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>KMPD1_0.KID (release)</td>
<td>ASCII</td>
<td><p><strong>KIDS Distribution.</strong> Required for Virgin installations. Contains the Capacity Management Tools V. 1.0 server software:</p>
<ul>
<li><blockquote>
<p>Global (^KMPD) and VA FileMan files.</p>
</blockquote></li>
<li><blockquote>
<p>Server Routines.</p>
</blockquote></li>
<li><blockquote>
<p>Capacity Planning Options.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>KMPD*1.0*1<br />
(patch)</td>
<td>ASCII</td>
<td><p><strong>KIDS Distribution.</strong> Required for all installations. Contains the following:</p>
<ul>
<li><blockquote>
<p>Server Routines (e.g., APIs).</p>
</blockquote></li>
<li><blockquote>
<p>Capacity Planning Options.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>HL*1.6*103<br />
(patch)</td>
<td>ASCII</td>
<td><strong>KIDS Distribution.</strong> Required for all installations. Contains an API (i.e., $$CM2^HLUCM) to calculate the volume of HL7 activity over a period of time.</td>
</tr>
</tbody>
</table>

<span id="_Hlt396118096" class="anchor"></span>Table 2‑1: RUM-related software distribution files

### VistA M Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools are required on your VistA M Server in order to install and use the RUM software:

 Server Operating System

> One of the following operating systems:

- Digital Standard M (DSM) for OpenVMS AXP V6.3-031 or greater
- InterSystems Caché for NT and OpenVMS

 Fully Patched M Accounts

> You should have both a development Test account and a Production account for the RUM software.

> The account(s) must contain the *fully* patched versions of the following software (listed alphabetically):

- Capacity Management Tools V. 1.0

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-installation-guide/012.png)</td>
<td><p>For virgin installations, <em>before</em> you install the RUM V. 2.0 software:</p>
<p>1. Install the Capacity Management Tools V. 1.0 software (i.e., KMPD1_0.KID)</p>
<p>2. Install the Capacity Management Tools Patch #1 (i.e., KMPD*1.0*1).</p></td>
</tr>
</tbody>
</table>

- Health Level Seven (HL7) V. 1.6

|                                                   |                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/013.png) | For all installations, install HL7 Patch \#103 (i.e., HL\*1.6\*103) *before* you install the RUM V. 2.0 software. |

- Kernel V. 8.0

|                                                   |                                                                                                                                                       |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/014.png) | For all installations, Kernel Patch \#186 (i.e., XU\*8.0\*186) is included in the KMPR2_0.KID file and is installed *before* the RUM V. 2.0 software. |

- Kernel Toolkit V. 7.3
- MailMan V. 8.0
- VA FileMan V. 22.0

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/015.png) | These software packages must be properly installed and *fully* patched prior to installing the RUM V. 2.0 software distribution. Patches must be installed in published sequence. You can obtain all released VistA M server-side patches (including patch description and installation instructions), from the Patch module on FORUM or through normal procedures. |

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
<td>![](kmpr-version-2-installation-guide/016.png)</td>
<td><p>DSM for OpenVMS sites should refer to the most recent Computer Operations Management and Procedures for AXP Systems (COMPAS) manual. Please refer to the AXP Team's Web site at:</p>
<p>REDACTED</p>
<p>Caché for NT and OpenVMS sites should refer to the AVANTI How-To Web site currently located at:</p>
<p>REDACTED</p></td>
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

# VistA M Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of Resource Usage Monitor (RUM) Version 2.0 software only affects the RUM options. Therefore, this installation can be performed at any time of the day with minimal disruption. Aside from implementing any of the applicable items that are listed below, installation should take approximately 10-15 minutes.

The instructions in this section are applicable for the Test/Production accounts in the DSM or Caché environments. Any unique instructions for a specific environment will be notated within the procedure.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-installation-guide/017.png)</td>
<td>All DSM for OpenVMS and Caché for Windows NT sites should install this software.<br />
<br />
Kernel Patch XU*8.0*186 updates the RUM %ZOSVKR routine and must be installed before installing the RUM V. 2.0 software. Patch XU*8.0*186 is bundled with the RUM V. 2.0 KIDS build (i.e., KMPR2_0.KID).</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/018.png) | All sites should ensure that the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is not currently running. |

This installation creates the ^KMPR global to store the RESOURCE USAGE MONITOR file (#8971.1) information. This global will automatically be trimmed (records deleted) to contain a maximum of 21 days of data by the RUM Background Driver option.

This installation also creates the ^KMPTMP("KMPR") global to store temporary RUM data. This global will contain one day's worth of data at maximum. The temporary ^KMPTMP("KMPR") global will be purged automatically by the RUM Background Driver option \[KMPR BACKGROUND DRIVER\]. This option is scheduled to run every night at 1 a.m. Testing has shown that a site's ^KMPTMP("KMPR") global contains approximately 117,760,000 bytes (i.e., 115,000 DSM blocks or 57,500 Caché blocks) before it is purged every night.

|                                                   |                                                        |
|---------------------------------------------------|--------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/019.png) | The ^KMPTMP("KMPR") global should *not* be journalled! |

### Virgin Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-installation-guide/020.png)</td>
<td>The following procedures are only required for virgin installations of the RUM software. Sites installing the Capacity Management Tools V. 1.0 and Resource Usage Monitor (RUM) software for the first time must follow the procedures in this section. When you have completed Steps #1 - 4 below, please proceed to the "<br />
Upgrade Installations" topic in this guide to complete the RUM V. 2.0 software installation.</td>
</tr>
</tbody>
</table>

#### Review Translation Table Settings *(required)*

> Capacity Planning (CP) Services' has been given the KMP\* namespace for both routines and global(s). Therefore, you should review your translation table setting(s) to determine the proper placement for the KMP\* global namespace.

> Capacity Planning (CP) Services' advises that sites should locate this global on a volume set that has a lesser overall level of activity. There are a couple of approaches by which the degree of activity can be ascertained:

- Monitor Global Growth—All sites can review CM's Top Globals Display option under the SAGG Trending menu options via FORUM. This option displays the top 10 globals in terms of growth over a selected time period. There is a very high correlation between the activity rate of a global and the corresponding rate of growth. This approach will yield many of the usual highly accessed globals with which the ^KMPTMP("KMPR") global should *not* be placed. These highly accessed globals include: ^OR, ^TIU, ^XMB, ^ECX, ^LRO, ^PSB, ^PSRX, ^HL, ^LR, ^PRCA, and DIA.
- Monitor Global Accesses—DSM sites can utilize the \*PMF utility on the cluster during several small (15 minutes) snapshots. The results will show global accesses per second for all globals across all volume sets. The benefit of this approach is that the results are not tied necessarily to global growth and will include others candidates to avoid placement along with ^KMPTMP("KMPR"), such as DIC and ^DD.

> In terms of allocating the necessary disk space to accommodate the size and expected growth of ^KMPTMP("KMPR"), this value will vary somewhat depending on the size and overall workload level at the medical center. In general, sites should allow approximately 117,760,000 bytes (i.e., 115,000 DSM blocks or 57,500 Caché blocks) for ^KMPTMP("KMPR") and ensure that an appropriate reference entry for this global exists in the translation table.

#### Retrieve the KMPD1_0.KID File *(required)*

> Obtain the KMPD1_0.KID file from the Enterprise VistA Support (EVS) ANONYMOUS.SOFTWARE directory located at Albany, Hines, or Salt Lake City. This file contains the Capacity Management Tools V. 1.0 software required with RUM V. 2.0

#### Load KMPD1_0.KID File *(required)*

> Use Kernel Installation & Distribution System (KIDS) to load the distribution. From the KIDS menu, select the Installation menu option. Invoke the Load a Distribution option to load the following software:

> KMPD1_0.KID

> The following is sample dialogue of a load of the CM Tools V. 1.0 software done at the Oakland OIFO:

> Select Kernel Installation & Distribution System Option: INS \<Enter\> tallation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> You've got PRIORITY mail!

> Select Installation Option: 1 \<Enter\> Load a Distribution

> Enter a Host File: USR\$:\[ANONYMOUS\]KMPD1_0.KID;1

> KIDS Distribution saved on Mar 11, 2002@15:20:50

> Comment: CM TOOLS 1.0

> This Distribution contains Transport Globals for the following Package(s):

> Build CM TOOLS 1.0 has been loaded before, here is when:

> CM TOOLS 1.0 Install Completed

> was loaded on Oct 31, 2002@14:16:08

> OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// \<Enter\>

> Loading Distribution...

> CM TOOLS 1.0

> Use INSTALL NAME: CM TOOLS 1.0 to install this Distribution.

<span id="_Toc56819160" class="anchor"></span>Figure 3‑1: Sample CM Tools V. 1.0 distribution load

|                                                                                                                |                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/021.png) | If you are prompted with "Want to RUN the Environment Check Routine? YES//", you should respond with YES. |

#### Install CM Tools V. 1.0 Software *(required)*

> Use KIDS to Install the CM Tools V. 1.0 software. Follow the KIDS installation prompts as you would any other KIDS installation. Specific prompts and suggested responses are notated below:

> a\. Users can be on the system during installation of this patch and software. However, this software should be installed during off-hours, when a minimal number of users are on the system.

> b\. You do not need to stop TaskMan.

> c\. You may elect to use any of the following options within the KIDS Installation menu:

- Verify Checksums in Transport Global—This option allows you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global
- Compare Transport Global to Current System—This option allows you to view all changes that will be made when the release is installed. It compares all components of the release (routines, DDs, templates, etc.).
- Backup a Transport Global—This option creates a backup message of any routines exported with this release. It will *not* back up any other changes such as DDs or templates.
- Install Package(s)

> d\. When prompted for the INSTALL NAME, enter the following:

> CM TOOLS 1.0

> e\. When prompted to rebuild menu trees:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

> You can respond with NO and not rebuild the menus until the normal scheduled menu rebuild takes place or YES to rebuild the menus immediately after the installation.

> f\. When prompted to inhibit logons:

> Want KIDS to INHIBIT LOGONs during the install? YES//

> You can respond with NO.

> g\. When prompted to disable options and protocols:

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

> You can respond with NO.

> The following is sample dialogue of an installation of the CM Tools V. 1.0 software done at the Oakland OIFO:

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 6\<Enter\> Install Package(s)

> Select INSTALL NAME: CM TOOLS 1.0 \<Enter\> Loaded from Distribution 11/6/02@14:48:32

> =\> CM TOOLS 1.0 ;Created on Mar 11, 2002@15:20:50

> This Distribution was loaded on Nov 06, 2002@14:48:32 with header of

> CM TOOLS 1.0 ;Created on Mar 11, 2002@15:20:50

> It consisted of the following Install(s):

> CM TOOLS 1.0

> Checking Install for Package CM TOOLS 1.0

> Install Questions for CM TOOLS 1.0

> Incoming Files:

> 8973.1 CM HL7 DATA

> Note: You already have the 'CM HL7 DATA' File.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// YES

> Want KIDS to INHIBIT LOGONs during the install? YES// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// \<Enter\> Telnet terminal

<span id="_Toc56819161" class="anchor"></span>Figure 3‑2: Sample CM Tools V. 1.0 installation (1 of 2)

> Install Started for CM TOOLS 1.0 :

> Nov 06, 2002@14:50:06

> Build Distribution Date: Mar 11, 2002

> Installing Routines:

> Nov 06, 2002@14:50:06

> Installing Data Dictionaries:

> Nov 06, 2002@14:50:07

> Installing PACKAGE COMPONENTS:

> Installing OPTION

> Nov 06, 2002@14:50:08

> Running Post-Install Routine: ^KMPDPOST

> Queueing \[KMPD BACKGROUND DRIVER\] to run each day at 1:30am...

> Complete!

> Updating Routine file...

> Updating KIDS files...

> CM TOOLS 1.0 Installed.

> Nov 06, 2002@14:50:08

> Install Message sent \#1457430

> ┌────────────────────────────────────────────────────────────┐

> 100% │ 25 50 75 │

> Complete └────────────────────────────────────────────────────────────┘

> Install Completed

<span id="_Toc56819162" class="anchor"></span>Figure 3‑3: Sample CM Tools V. 1.0 installation (2 of 2)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-installation-guide/022.png)</td>
<td>After completing Steps #1 - 4, follow the steps under the "<br />
Upgrade Installations" topic in this guide in order to complete the installation of the RUM V. 2.0 software.</td>
</tr>
</tbody>
</table>

### Upgrade Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps are to be performed by those sites upgrading from Version 1.0 of the Resource Usage Monitor (RUM) software. If this is a virgin install please make sure that you have completed Steps \#1 - 6 under the "Virgin Installations" topic in this guide.

#### DSM Sites: Review Your Mapped Set *(required)*

|                                                                                                                                     |                                            |
|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| ![](kmpr-version-2-installation-guide/023.png) | If you are a Caché site, skip to Step \#2. |

> If any DSM beta test sites have mapped the KMPR\* routines, they should be removed from the mapped set at this time.

#### Install Health HL7 Patch HL\*1.6\*103 *(required)*

> Use Kernel Installation & Distribution System (KIDS) to install the Health Level Seven (HL7) Patch HL\*1.6\*103. Follow the patch installation instruction in the Patch Module on FORUM.

#### Install CM Tools Patch KMPD\*1.0\*1 *(required)*

> Use KIDS to install the Capacity Management Tools Patch KMPD\*1.0\*1. Follow the patch installation instruction in the Patch Module on FORUM.

#### Stop RUM Collection *(required)*

> Use the Stop RUM Collection option \[KMPR STOP COLLECTION\] to stop collection of Resource Usage Monitor (RUM) data.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/024.png) | The KMPR STOP COLLECTION option is located on the RUM Manager Menu \[KMPR RUM MANAGER MENU\], which is located under the Capacity Management menu \[XTCM MAIN\]. For more information on the Stop RUM Collection option \[KMPR STOP COLLECTION\], please refer to Chapter 3, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### Retrieve the KMPR2_0.KID File *(required)*

> Obtain the KMPR2_0.KID file from the Enterprise VistA Support (EVS) ANONYMOUS.SOFTWARE directory located at Albany, Hines, or Salt Lake City.

#### Load KMPR2_0.KID File *(required)*

> Use Kernel Installation & Distribution System (KIDS) to load the distribution. From the KIDS menu, select the Installation menu option. Invoke the Load a Distribution option to load the following software (combined in one KIDS build):

- XU\*8.0\*186
- CAPACITY MANAGEMENT - RUM 2.0

> The following is sample dialogue of a load of Kernel Patch XU\*8.0\*186 and the RUM V. 2.0 software done at the Oakland OIFO:

> Select Kernel Installation & Distribution System Option: INS \<Enter\> tallation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 1 \<Enter\> Load a Distribution

> Enter a Host File: USR\$:\[ANONYMOUS\]KMPR2_0.KID;1

> KIDS Distribution saved on Feb 06, 2003@09:48:47

> Comment: CAPACITY MANAGEMENT - RUM 2.0

> This Distribution contains Transport Globals for the following Package(s):

> CAPACITY MANAGEMENT - RUM 2.0

> Build XU\*8.0\*186 has been loaded before, here is when:

> XU\*8.0\*186 Install Completed

> was loaded on Nov 07, 2002@10:01:37

> OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// \<Enter\>

> Loading Distribution...

> CAPACITY MANAGEMENT - RUM 2.0

> XU\*8.0\*186

> Use INSTALL NAME: CAPACITY MANAGEMENT - RUM 2.0 to install this Distribution.

<span id="_Toc56819163" class="anchor"></span>Figure 3‑4: Sample XU\*8.0\*186 and RUM V. 2.0 distribution load

|                                                                                                                |                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/025.png) | If you are prompted with "Want to RUN the Environment Check Routine? YES//", you should respond with YES. |

#### Install Kernel Patch XU\*8.0\*186 and RUM V. 2.0 Software *(required)*

> Use KIDS to Install Kernel Patch XU\*8.0\*186 and the RUM V. 2.0 software. Follow the KIDS installation prompts as you would any other KIDS installation. Specific prompts and suggested responses are notated below:

|                                                   |                                                                                       |
|---------------------------------------------------|---------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/026.png) | Kernel Patch XU\*8.0\*186 is installed *prior* to installing the RUM V. 2.0 software. |

> a\. Users can be on the system during installation of this patch and software. However, this software should be installed during off-hours, when a minimal number of users are on the system.

> b\. You do not need to stop TaskMan.

> c\. You may elect to use any of the following options within the KIDS Installation menu:

- Verify Checksums in Transport Global—This option allows you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global
- Compare Transport Global to Current System—This option allows you to view all changes that will be made when the release is installed. It compares all components of the release (routines, DDs, templates, etc.).
- Backup a Transport Global—This option creates a backup message of any routines exported with this release. It will *not* back up any other changes such as DDs or templates.
- Install Package(s)

> d\. When prompted for the INSTALL NAME, enter the following:

> CAPACITY MANAGEMENT - RUM 2.0

> e\. When prompted to rebuild menu trees:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

> You can respond with NO and not rebuild the menus until the normal scheduled menu rebuild takes place or YES to rebuild the menus immediately after the installation.

> f\. When prompted to inhibit logons:

> Want KIDS to INHIBIT LOGONs during the install? YES//

> You can respond with NO.

> g\. When prompted to disable options and protocols:

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//

> You can respond with NO.

> The following is sample dialogue of an installation of Kernel Patch XU\*8.0\*186 and the RUM V. 2.0 software done at the Oakland OIFO:

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 6\<Enter\> Install Package(s)

> Select INSTALL NAME: CAPA \<Enter\> CITY MANAGEMENT - RUM 2.0 Loaded from Distribution 2/6/03@14:51:02

> =\> CAPACITY MANAGEMENT - RUM 2.0 ;Created on Feb 06, 2003@09:48:47

> This Distribution was loaded on Feb 06, 2003@14:51:02 with header of

> CAPACITY MANAGEMENT - RUM 2.0 ;Created on Feb 06, 2003@09:48:47

> It consisted of the following Install(s):

> CAPACITY MANAGEMENT - RUM 2.0 XU\*8.0\*186

> Checking Install for Package CAPACITY MANAGEMENT - RUM 2.0

> Install Questions for CAPACITY MANAGEMENT - RUM 2.0

> Incoming Files:

> 8971.1 RESOURCE USAGE MONITOR

> Note: You already have the 'RESOURCE USAGE MONITOR' File.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

> Checking Install for Package XU\*8.0\*186

> Install Questions for XU\*8.0\*186

> Want KIDS to INHIBIT LOGONs during the install? YES// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// \<Enter\> Telnet terminal

<span id="_Toc56819164" class="anchor"></span>Figure 3‑5: Sample XU\*8.0\*186 and RUM V. 2.0 installation (1 of 2)

> Install Started for CAPACITY MANAGEMENT - RUM 2.0 :

> Feb 06, 2003@14:53:35

> Build Distribution Date: Feb 06, 2003

> Feb 06, 2003@14:53:36 Installing Data Dictionaries:

> Installing Routines:

> Feb 06, 2003@14:53:38

> Installing PACKAGE COMPONENTS:

> Installing OPTION

> Feb 06, 2003@14:53:40

> Running Post-Install Routine: ^KMPRPOST

> Begin Post-Install...

> Removing data from ^XTMP("KMPR")...

> Cleaning up ^KMPTMP("KMPR","BACKGROUND")...

> Checking RUM Background Job...

> Cleaning up "B" xref in RESOURCE USAGE MONITOR file...

> Post-Install complete!

> Updating Routine file...

> Updating KIDS files...

> CAPACITY MANAGEMENT - RUM 2.0 Installed.

> Feb 06, 2003@14:53:42

> Install Message sent \#1461421

> Install Started for XU\*8.0\*186 :

> Feb 06, 2003@14:53:42

> Build Distribution Date: Feb 06, 2003

> Installing Routines:

> Feb 06, 2003@14:53:42

> Updating Routine file...

> Updating KIDS files...

> XU\*8.0\*186 Installed.

> Feb 06, 2003@14:53:43

> Install Message sent \#1461422

> ┌────────────────────────────────────────────────────────────┐

> 100% │ 25 50 75 │

> Complete └────────────────────────────────────────────────────────────┘

> Install Completed

<span id="_Toc56819165" class="anchor"></span>Figure 3‑6: Sample XU\*8.0\*186 and RUM V. 2.0 installation (2 of 2)

#### DSM Sites: Move ZOSVKR\* Routines *(required)*

|                                                                                                                                     |                                            |
|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| ![](kmpr-version-2-installation-guide/027.png) | If you are a Caché site, skip to Step \#8. |

> After the installation, DSM sites should move the ZOSVKR\* routines to the MGR account.

#### DO RELOAD^ZTMGRSET *(required)*

> After the installation, *both* DSM and Caché sites should do the following:

> a\. At the programmer prompt, do the following:

> \>D RELOAD^ZTMGRSET

> b\. Select Kernel Patch 186.

#### Post Installation Routine *(required)*

> The following are examples of informational messages that you may receive while the post-installation routine is running.

#### Obsolete Data

> Removing data from ^XTMP("KMPR")...

> Cleaning up ^KMPTMP("KMPR","BACKGROUND")...

> <span id="_Toc56819166" class="anchor"></span>Figure 3‑7: Informational Message—Deleting obsolete RUM data

> This informational message indicates that the post-installation routine is deleting data from the temporary ^XTMP("KMPR") and cleaning up the ^KMPTMP("KMPR","BACKGROUND") globals (test sites only). These globals were used by previous versions of the RUM software. The post-installation routine will run this cleanup code at every site, regardless of existence of earlier versions of the software.

#### Background Job Check

> Checking RUM Background Job...

> <span id="_Toc56819167" class="anchor"></span>Figure 3‑8: Informational Message—Background job check

> This informational message indicates that the post-installation routine is determining whether the KMPR BACKGROUND DRIVER option exists.

#### Cross-reference Check

> Cleaning up "B" xref in RESOURCE USAGE MONITOR file...

> Post-Install complete!

> <span id="_Toc56819168" class="anchor"></span>Figure 3‑9: Informational Message—Cross-reference check

> This informational message indicates that the post-installation routine is cleaning up any "B"-type cross-references in the RESOURCE USAGE MONITOR file (#8971.1).

#### Post-Installation Complete

> Post-Install complete!

> <span id="_Toc56819169" class="anchor"></span>Figure 3‑10: Informational Message—Post-installation complete

> This informational message indicates that the post-installation routine has completed.

#### DSM Sites: Delete Any Unmapped Routines *(recommended)*

|                                                                                                                                     |                                             |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|
| ![](kmpr-version-2-installation-guide/028.png) | If you are a Caché site, skip to Step \#11. |

> If routines were unmapped as part of Step \#1, they should be deleted from the mapped set once the installation has been run to completion.

|                                                                                                                |                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/029.png) | The KMPR\* and %ZOSVKR\* namespaced routines are *not* recommended to be mapped. |

#### Start RUM Collection *(required)*

> Use the Start RUM Collection option \[KMPR START COLLECTION\] to start collection of Resource Usage Monitor (RUM) data.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/030.png) | The KMPR START COLLECTION option is located on the RUM Manager Menu \[KMPR RUM MANAGER MENU\], which is located under the Capacity Management menu \[XTCM MAIN\]. For more information on the Start RUM Collection option \[KMPR START COLLECTION\], please refer to Chapter 3, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### Review RUM Settings *(recommended)*

> 1\. Schedule Background Driver—Invoke the Status of RUM Collection option \[KMPR STATUS COLLECTION\] to ensure that the RUM Background Driver \[KMPR BACKGROUND DRIVER\] is scheduled to run every day at 1 a.m. Review the other items in the status display for their accuracy. Specifically:

- STATUS = Running
- RUM BACKGROUND DRIVER = KMPR BACKGROUND DRIVER
- QUEUED TO RUN AT = TOMORROW@01:00 (or the appropriate time for your site)
- RESCHEDULING FREQUENCY = 1D
- TASK ID = TaskMan ID number is present
- QUEUED BY = An active user
- Temporary collection global = ^KMPTMP("KMPR" global is present
- RUM routines displays no problems

> Version 2.0

> Status......................: Running

> RUM Background Driver.......: KMPR BACKGROUND DRIVER

> QUEUED TO RUN AT............: May 17, 2003@01:00

> RESCHEDULING FREQUENCY......: 1D

> TASK ID.....................: 13938

> QUEUED BY...................: KMPDUSER,ONE A (Active)

> Daily Background last start.: 5/16/03@01:00:04

> Daily Background last stop..: 5/16/03@02:16:32

> Daily Background total time.: 01:16:28

> Weekly Background last start: 5/11/03@01:16:03

> Weekly Background last stop.: 5/11/03@02:08:21

> Weekly Background total time: 00:52:18

> Temporary collection global

> ^KMPTMP("KMPR").............: Present

> Press RETURN to continue or '^' to exit: \<Enter\>

> RUM Environment

> Version 2.0T20

> \# of Oldest Recent

> File Entries Date Date

> ------------------------------------ ------- ------ ------

> 8971.1 - RESOURCE USAGE MONITOR 230,740 4/27/03 5/15/03

> RUM routines...........: No Problems

> <span id="_Toc56819170" class="anchor"></span>Figure 3‑11: Sample output from the Status of RUM Collection option \[KMPR STATUS COLLECTION\]

|                                                                                                                |                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/031.png) | For more information on the Status of RUM Collection option \[KMPR STATUS COLLECTION\] and the RUM Background Driver \[KMPR BACKGROUND DRIVER\], please refer to Chapter 3, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

> If the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is not shown as being scheduled to run in the future, use the Schedule/Unschedule Options option \[XUTM SCHEDULE\] located under the Taskman Management menu \[XUTM MGR\] to schedule the KMPR BACKGROUND DRIVER option \[KMPR BACKGROUND DRIVER\] to run every day at 1 a.m.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-installation-guide/032.png)</td>
<td>Capacity Planning (CP) Services <em>strongly</em> recommends that the RUM Background Driver option [KMPR BACKGROUND DRIVER] be scheduled to run every day at 1 a.m., because this background driver is the main mechanism by which the ^KMPTMP("KMPR") temporary collection global is purged nightly and the RESOURCE USAGE MONITOR file (#8971.1) is trimmed (records deleted) to contain a maximum of 21 days of data every Sunday night.<br />
<br />
Modification of the frequency and time may have adverse effects on the size of the ^KMPTMP("KMPR") temporary collection global and on the number of entries within the RESOURCE USAGE MONITOR file.</td>
</tr>
</tbody>
</table>

> 2\. Mail Groups—Use the Capacity Management Mail Group Edit option \[KMP MAIL GROUP EDIT\], located under the Capacity Management menu \[XTCM MAIN\] that is located on the Eve menu, to review the KMP-CAPMAN mail group membership. You should ensure that the group contains the IRM staff responsible for receiving messages pertaining to capacity planning issues.

|                                                                                                                |                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| ![](kmpr-version-2-installation-guide/033.png) | The KMP-CAPMAN mail group is included and installed with RUM V. 2.0 software. |