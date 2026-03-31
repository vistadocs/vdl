---
title: XT*7.3*98 VistA Patch Monitor, Supplement to Patch Desc
doc_type: SUP
doc_label: Supplement
doc_layer: patch
doc_subject: VistA Patch Monitor, Supplement to Patch Desc
app_code: XT
app_name: Kernel Toolkit
section: INF
app_status: active
pkg_ns: XT
patch_ver: 7.3
patch_id: XT*7.3*98
group_key: "XT:XT:7.3"
file_numbers: 
  - 9
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patch
  - monitor
  - xtpm
  - class
  - table
  - patches
  - date
  - span
  - kids
  - contents
page_count: 0
word_count: 13150
section_count: 9
table_count: 79
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Toolkit/xt7_3p98sp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Toolkit/xt7_3p98sp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=12"
---

![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/001.png)

VISTA PATCH MONITOR

SUPPLEMENT TO PATCH DESCRIPTION

Kernel Toolkit Patch XT\*7.3\*98

September 2005

VistA Health Systems Design & Development (HSD&D)

Infrastructure and Security Services (ISS)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation History

The following table displays the revision history for this document. Revisions to the documentation are based on continuous dialog with Infrastructure and Security Services (ISS) Technical Writers and evolving industry standards and styles.

| Date | Description                                                                        | Author |
|----------|----------------------------------------------------------------------------------------|------------|
| Aug 2005 | Documentation released with Kernel Toolkit Patch XT\*7.3\*98, the VistA Patch Monitor. | REDACTED   |
| Jan 2006 | Updates to documentation resulting from Remedy Ticket \# 115143.                       | REACTED    |

<span id="_Toc104264382" class="anchor"></span>Table i: Documentation History

Patch History

For the current patch history related to this software, please refer to the Patch Module on FORUM.

Contents

## Tables and Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel Toolkit Patch XT\*7.3\*98 project team consists of the following Infrastructure & Security Services (ISS) personnel:

- REDACTED

Infrastructure & Security Services would like to thank REDACTED, Carl Vinson VA Medical Center - VAMCSITE, GA, the original developer of the VistA Patch Monitor, Version 2.1. In addition, REDACTED would like to thank REDACTED of the Atlanta VA Medical Center (VAMC) for their dedication to this project and their invaluable assistance to him in the testing of the package.

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This supplemental documentation is intended for use in conjunction with the release of the VistA Patch Monitor, Kernel Toolkit Patch XT\*7.3\*98. It outlines the details of the work involved in this patch for VA facilities. It is organized into the following major parts:

1.  Introduction
2.  Package Installation
3.  Menu Options
4.  Setting Up a New Installation or Recovering Patches
5.  Implementation and Maintenance (Technical Manual Information)

How to Use this Manual

This manual uses several methods to highlight different aspects of the material. The following symbols are used in the manual to alert the reader about special information:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table describes these symbols:

|                                                   |                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Symbol                                        | Description                                                                                      |
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/002.png) | Used to inform the reader of general information including references to additional reading material |
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/003.png) | Used to caution the reader to take special notice of critical information                        |

<span id="_Toc6197364" class="anchor"></span>Table ii: Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font). "Snapshots" of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a non-proportional font.
- User's responses to online prompts are highlighted in bold typeface.
- The "\<Enter\>" found within these snapshots indicates that the user should press the Enter key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                   |                                                                                                                                  |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666."
- Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document, located on the \[web site\] and where "N" represents the first name as a number spelled out and incremented with each new entry.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/005.png)</td>
<td><p>The list of Approved Application Abbreviations can be found at the following Web site:</p>
<blockquote>
<p><u>http://vista.med.va.gov/iss/strategic_docs.asp#sop</u></p>
</blockquote></td>
</tr>
</tbody>
</table>

Who Should Read this Manual?

The intended audience for this documentation is all key stakeholders. The primary stakeholder is Health Systems Implementation Training and Enterprise Support (HSITES). Additional stakeholders include Infrastructure & Security Service (ISS), Development & Infrastructure Support (DaIS), Health Systems Design and Development (HSD&D), all Veterans Health Information Systems and Technology Architecture (VistA) sites, and Veterans Affairs Medical Centers (VAMC). This documentation is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- VA FileMan data structures and terminology
- M programming language

No attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following web address:

> <http://vista.med.va.gov/>

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

|                                                   |                                                                                                                            |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/006.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA software has online help and commonly used system default prompts. In character-based mode, users are encouraged to enter question marks at any response prompt. Help messages are often provided showing lists of acceptable responses or format requirements. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in VistA character-based software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A, while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

|                                                   |                                                                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/007.png) | Help messages may not be available for every prompt. If you enter "?" or "??" at a prompt and it does not have a Help message, the system will simply repeat the prompt. |

Obtaining Data Dictionary Listings

Technical information about files and their associated fields is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                   |                                                                                                                                                                                                              |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/008.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the "VA FileMan Advanced User Manual." |

VistA Documentation

VistA documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/009.png)</td>
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

- Preferred Method REDACTED
- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/010.png)</td>
<td><blockquote>
<p>This method transmits the files from the first available FTP server.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/011.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Tables and Figures](#tables-and-figures)
  - [Acknowledgements](#acknowledgements)
  - [Orientation](#orientation)
- [Introduction](#introduction)
  - [Package Operation](#package-operation)
    - [A Note About Test Patches](#a-note-about-test-patches)
- [Package Installation](#package-installation)
    - [Pre-Installation Procedure](#pre-installation-procedure)
    - [Installation Procedure](#installation-procedure)
    - [Post-Installation Procedure](#post-installation-procedure)
- [Menu Options](#menu-options)
- [Setting Up a New Installation or Recovering Patches](#setting-up-a-new-installation-or-recovering-patches)
- [Implementation and Maintenance (Technical Manual Information)](#implementation-and-maintenance-technical-manual-information)
    - [Software Dependencies](#software-dependencies)
    - [Scheduled Options/Background Jobs](#scheduled-optionsbackground-jobs)
    - [Routines](#routines)
    - [Data Dictionaries Exported with XT\7.3\98 for New VistA Files](#data-dictionaries-exported-with-xt7398-for-new-vista-files)
    - [Options Exported with Kernel Toolkit Patch XT\7.3\98](#options-exported-with-kernel-toolkit-patch-xt7398)
    - [VA FileMan Templates](#va-fileman-templates)
    - [Archiving](#archiving)
    - [Callable Routines](#callable-routines)
    - [External Interfaces](#external-interfaces)
    - [Mail Groups](#mail-groups)
    - [External Relations](#external-relations)
    - [Internal Relations](#internal-relations)
    - [Namespace](#namespace)
    - [Software-wide Variables](#software-wide-variables)
  - [Software Security](#software-security)
    - [Mail Groups](#mail-groups-1)
    - [Remote Systems](#remote-systems)
    - [Archiving](#archiving-1)
    - [Interfaces](#interfaces)
    - [Electronic Signatures](#electronic-signatures)
    - [Menus](#menus)
    - [Security Key](#security-key)
    - [File Security](#file-security)
  - [Glossary](#glossary)
  - [Index](#index)
The VistA Patch Monitor is being released in Kernel Toolkit Patch XT\*7.3\*98. This package is designed to assist package support and management personnel in keeping up with VistA patch requirements. It monitors patches as they arrive in the VistA MailMan, records pertinent data and then monitors them on a daily basis through automated processing.
This package will track only patches that are released from the National Patch Module on Forum. It will not track Class III patches, test patches or hand-entered patches from other sources due to its link with the Kernel Installation and Distribution System (KIDS) INSTALL file (#9.7).
Package support and management personnel have a various reporting programs they may use on a daily basis, as well as automatic daily options which report anything from past due to uninstalled patches.

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches are usually sent to the G.PATCHES mail group, which should be standard at all sites. If this mail group does not exist at a site, any mail group that receives national patches may be used.

In this mail group, a server option, S.XTPM PATCH SERVER, is added as a "remote user." When Mailman delivers the message, the server option receives the message, examines it line by line and extracts certain information. This message data then is stored in the PATCH MONITOR file (#9.9).

Upon arrival, a patch message is examined to see if it contains the text “\*\*INSTALL NAME\*\*” as a line in the message. If it does not, then the message is flagged as “non-KIDS” when first entered. This does not mean it is not really a KIDS patch but rather that there is no KIDS install included in the patch message. This may be because of one of the following two things:

1.  The patch may require a host file to be downloaded and installed into the distribution global
2.  The patch may not yet be loaded into the distribution global from the MailMan message

At night, a TaskMan option, XTPM NIGHTLY PATCH MONITOR, runs after midnight, reviews the PATCH MONITOR file (#9.9) and takes certain actions:

1.  If any patch is not installed and the current date is not past the compliance date, nothing is done.
2.  If the job finds a matching entry in the INSTALL file (#9.7), the patch type is set to be a “KIDS” patch. Otherwise, it continues to remain a non-KIDS patch until such a record is found.
3.  If the patch is a KIDS patch and there is no installation date in the INSTALL file (#9.7) and the current date is past the compliance date, it is added to the mail bulletin that reports all past due patches to the XTPM PATCH MONITOR mail group.
4.  If the patch is a non-KIDS patch and there is no completion date in the PATCH MONITOR file (#9.9) and the current date is past the compliance date, it also is added to the mail bulletin that reports all past due patches to the XTPM PATCH MONITOR mail group.
5.  Any patch record, whether KIDS or non-KIDS, that has either a completed installation record or a completion date, respectively, will be purged from the PATCH MONITOR file (#9.9) if it is so designated in the PATCH MONITOR PARAMETER file (#9.95).

|                                                   |                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/012.png) | If completed patches are not set to be deleted, they will accumulate up to the number of days designated in the PATCH MONITOR PARAMETER file (#9.95), or 30 days if no limit is set. See the PATCH MONITOR PARAMETER file (#9.95) setup for further explanation about data retention and purging of data. |

### A Note About Test Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are many sites that regularly participate as test sites and consequently they receive many test patches. The VistA Patch Monitor totally ignores these types of patches and they are not entered into the PATCH MONITOR file (#9.9). However, because they are actual KIDS installs, they can cause problems with date calculations from the INSTALL when the actual patch comes in. Because of this, INSTALL file (#9.7) records for test and COMPLETED/UNRELEASED patches are also ignored for reports, editing and inquiries. For example, if a released patch comes in and it is the fifth installation in the INSTALL file (#9.7) (due to multiple test releases) these previous installation records are ignored and the patch truly appears as uninstalled until installed with the true released KIDS patch.

# Package Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*98 is distributed as a Kernel Installation and Distribution (KIDS) file in a regular MailMan (PackMan) message. The installation instructions for Patch XT\*7.3\*98 are organized and described in this chapter as follows:

> I. Pre-Installation Procedure—Actions to be taken before sites install the software.

> II\. Installation Procedure—Basic step-by-step instructions for installing the software and sample installation screen capture.

> III\. Post-Installation Procedure—Actions to be taken after sites install the software.

|                                                   |                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/013.png) | Detailed installation instructions can be found in the Kernel Toolkit Patch XT\*7.3\*98 patch description on FORUM. |

### Pre-Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site has previously installed the VistA Patch Monitor Class III software, the following steps must be taken into consideration before installing Patch XT\*7.3\*98.

Step 1. If the options listed below are installed at your site, use VA TaskMan to unschedule them as shown in Figure 2‑1.

- \[AWB NIGHTLY PATCH MONITOR\]
- \[AWB UNINSTALLED PATCH BULLETIN\]

Select Taskman Management Option: Schedule/Unschedule Options

Select OPTION to schedule or reschedule: AWB NIGHTLY PATCH MONITOR \<Enter\> Nightly Patch Monitor

...OK? Yes// \<Enter\> (Yes)

\(R\)

Edit Option Schedule

Option Name: @

Menu Text: Nightly Patch Monitor TASK ID: 626046

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: AUG 23,2005@24:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> **WARNING:** DELETIONS ARE DONE IMMEDIATELY!

(EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)

Are you sure you want to delete this entire record (Y/N)? y

Select OPTION to schedule or reschedule: UNINSTALLED PATCH BULLETIN \<Enter\> Uninstalled Patch Bulletin

...OK? Yes// \<Enter\> (Yes)

\(R\)

Edit Option Schedule

Option Name: @

Menu Text: Uninstalled Patch Bulletin TASK ID: 626047

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: AUG 23,2005@24:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> **WARNING:** DELETIONS ARE DONE IMMEDIATELY!

(EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)

Are you sure you want to delete this entire record (Y/N)? y

<span id="_Ref112559104" class="anchor"></span>Figure ‑: Unschedule \[AWB NIGHTLY PATCH MONITOR\] and \[AWB UNINSTALLED PATCH BULLETIN\]

Step 2. The pre-install routine MERGE^XT73P98 copies data from the existing Class III VistA Patch Monitor V. 2.0 files to the new Class I files, as shown in Table 2‑1.

| Class III File Name and Number | Class I File Name and Number |
|------------------------------------|----------------------------------|
| PATCH MONITOR \#177100.6           | PATCH MONITOR \#9.9              |
| PATCH MONITOR PARAMETER \#177100.7 | PATCH MONITOR PARAMETER 9.95     |

<span id="_Ref112563888" class="anchor"></span>Table ‑: Moving Class III data into Class I files

|                                                   |                                                                                                                                                       |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/014.png) | The post-install routine EN^XT73P98 removes all old files, options, and routines originally exported with the VistA Patch Monitor Class III software. |

|                                                   |                                                                                                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/015.png) | For more information on the post-installation for Patch XT\*7.3\*98, see the section titled: "Post-Installation Procedure" in this documentation. |

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are the steps to install and use this package. They assume that the installer is familiar with a KIDS installation.

> Step 1. Unload the PackMan mail message into the distribution global.

> Step 2. Use option 2 to verify the checksums in the package.

> Step 3. There will be no need to back up previous VistA Patch Monitor packages.

> Step 4. Use option 6 to install the package.

Figure 2‑2 shows a sample installation of Patch XT\*7.3\*98, the VistA PATCH MONITOR.

Select Installation Option: 6 \<Enter\> Install Package(s)

Select INSTALL NAME: XT\*7.3\*98\<Enter\> Loaded from Distribution 2/29/04@16:53:34

=\> XT\*7.3\*98

This Distribution was loaded on Feb 29, 2004@16:53:34 with header of XT\*7.3\*98

It consisted of the following Install(s):

XT\*7.3\*98

Checking Install for Package XT\*7.3\*98

Install Questions for XT\*7.3\*98

Incoming Files:

9.9 PATCH MONITOR

9.95 PATCH MONITOR PARAMETER

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'XTPM PATCH MONITOR': KTUSER, ONE

KO IRM COMPUTER SPECIALIST

Enter the Coordinator for Mail Group 'XTPM PATCH MONITOR USER': KTUSER,ONE

KO IRM COMPUTER SPECIALIST

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// Y\<Enter\> YES

Want KIDS to INHIBIT LOGONs during the install? YES// N NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// N \<Enter\> NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: \<Enter\> HOME// \<Enter\>

<span id="_Ref111526936" class="anchor"></span>Figure ‑: Kernel Toolkit Patch XT\*7.3\*98 installation example

### Post-Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/016.png) | The Kernel Toolkit Patch XT\*7.3\*98 post init routine XT73P98 deletes all existing Class III VistA Patch Monitor Version 2.0 files (i.e., Files \#177100.6 and 177100.7), options, and routines in the AWB namespace. Patch XT\*7.3\*98 exports and installs all options and files comprising the Class I version of the VistA Patch Monitor in the XTPM namespace. |

Once the installation is finished, perform the following tasks in the following order:

> Step 1. Give the security key XTPM PATCH MONITOR MGR to the person designated as package manager. This key is necessary to schedule the Nightly Patch Monitor option because if the person who schedules the option does not have it, the option <u>will not</u> run.

> Step 2. Give the XTPM PATCH MONITOR MAIN MENU to the persons designated as patch support personnel.

> Step 3. If S.XTPM PATCH SERVER@your_facility_domain exists as a remote member of the PATCHES mail group, edit S.XTPM PATCH SERVER@your_facility_domain to S.XTPM PATCH SERVER@your_facility_domain. Or, add S.XTPM PATCH SERVER@your_facility_domain as a remote member of the G.PATCHES mail group. If there is another group at your site that receives patches, you may substitute that group name. If this is not added correctly, no patches will be captured and entered into the PATCH MONITOR file (#9.9). For example, use VA FileManager to add the server option as a remote recipient in the G.PATCHES mail group, Figure 2‑3. This is Field \#12 in the MAIL GROUP file (#3.8).

| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/017.png) | It is recommended that sites only use one central mail group for patches. |
|---------------------------------------------------|-------------------------------------------------------------------------------|

Select VA FileMan Option: Enter or Edit File Entries

INPUT TO WHAT FILE: MAIL GROUP//

EDIT WHICH FIELD: ALL// 12\<Enter\> MEMBERS - REMOTE (multiple)

EDIT WHICH MEMBERS - REMOTE SUB-FIELD: ALL//

THEN EDIT FIELD:

Select MAIL GROUP NAME: PATCHES

Select REMOTE MEMBER: S.XTPM PATCH SERVER@VAMCSITE.MED.VA.GOV

<span id="_Ref112561193" class="anchor"></span>Figure ‑: Add server option as a remote recipient in the G.PATCHES mail group

> Step 4. Optionally, follow the instructions in Figure 2‑4 to delete any existing mail groups in the AWB namespace.

Select MAIL GROUP NAME: AWB PATCH MONITOR USER

NAME: AWB PATCH MONITOR USER Replace @

SURE YOU WANT TO DELETE THE ENTIRE 'AWB PATCH MONITOR USER' MAIL GROUP? Y \<Enter\> (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'BULLETIN' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// \<Enter\> (No)

Select MAIL GROUP NAME: AWB PATCH MONITOR

NAME: AWB PATCH MONITOR// @

SURE YOU WANT TO DELETE THE ENTIRE 'AWB PATCH MONITOR' MAIL GROUP? Y \<Enter\> (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'BULLETIN' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// \<Enter\> (No)

<span id="_Ref112724682" class="anchor"></span>Figure ‑: Delete mail groups in the AWB namespace

> Step 5. Set up the following two mail groups that come with this package:

1.  XTPM PATCH MONITOR—This mail group is for management personnel (Veterans Integrated Service Network \[VISN\], Chief Information Offices \[CIOs\], Information Resource Management \[IRM\], Risk Management chiefs etc.) to receive the delinquent patch bulletin.
2.  XTPM PATCH MONITOR USER—This mail group is for package management personnel to receive the daily uninstalled patch bulletin. The average package support person and any VistA managers or supervisors would be included in this mail group.

> Step 6. Set up your site in the PATCH MONITOR PARAMETER file (#9.95) using the information shown in Table 2‑2.

| Prompt                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "Select PATCH MONITOR PARAMETER SITE NAME:" | Enter the name of your facility. This is a free-text entry of up to 35 characters.                                                                                                                                                                                                                                                                                                                                                                   |
| "Select MAIL GROUPS:"                       | Enter the mail group or groups that will receive the daily monitor bulletins about uninstalled patches. These are *not* the groups to receive the delinquent patch bulletins. This field points to the MAIL GROUP file (#3.8) and all groups entered here must already exist in the MAIL GROUP file (#3.8).                                                                                                                                          |
| "NUMBER OF DAYS TO KEEP DATA:"              | Enter the number of days to keep completed patch data on file. This field is overridden by the field “Delete installed patches." If the field is “Delete Installed Patches” is YES then any number entered in this field is ignored. If the field “Delete Installed Patches” is NO then data will retained for the amount of days entered here. If no value is entered, 30 days are automatically kept. See note below explaining data retention.    |
| "DELETE INSTALLED PATCHES?:"                | Enter Y to allow the nightly job to delete all installed patches if they are completed or N to retain them the number of days specified in the field “Number of days to keep data." This field overrides the “Number of days to keep data” field. If this field is NO the number of days of patches are kept is determined by the field “Number of Days to Keep Data," or 30 days is kept if no there is no entry in the field. See note as follows. |

<span id="_Ref110680220" class="anchor"></span>Table ‑: Site setup in the PATCH MONITOR PARAMETER file (#9.95)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/018.png)</td>
<td><h3 id="explanatory-note-about-data-retention" class="unnumbered">Explanatory Note About Data Retention</h3>
<p>It is entirely up to a site whether or not patch installation data is retained for statistical reporting purposes. A site may wish to retain data and have a full compliment of reporting for statistics on past periods or it may wish to simply keep up with the current patching scenario and only make sure patches are installed on a timely basis and nothing more.</p>
<p>The site should weigh this decision carefully so as not to delete data unless it realizes the ramifications of it.</p></td>
</tr>
</tbody>
</table>

|                                                   |                                                                               |
|---------------------------------------------------|-------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/019.png) | You may go to item 6 unless you wish to set up Reporting Groups at this time. |

| Prompt (continued…)   | Description (continued…)                 |
|---------------------------|----------------------------------------------|
| "Select REPORTING GROUP:" | Enter a free text name of a reporting group. |

<span id="_Toc125282461" class="anchor"></span>Table ‑: Site setup in the PATCH MONITOR PARAMETER file (#9.95) (continued…)

> Figure 2‑5 shows an example of a reporting group that has already been set up:

REPORTING GROUP: KERNEL//

Select NAME SPACE: XT

Are you adding 'TOOLKIT' as a new NAME SPACE (the 2ND for this REPORTING GROUP)? No// YES

<span id="_Ref112564522" class="anchor"></span>Figure ‑: Example of a reporting group that has already been set up

> You may add as many name spaces as you wish. It should be noted that this field is a “free text” pointer to the PACKAGE file (#9.4) so the packages must exist in that file or they cannot be added. Any mixture of name spaces may be added.

> Step 7. Use VA TaskMan to set up the following options with the following parameters:

- XTPM NIGHTLY PATCH MONITOR:
  - Time: 05:00
  - Rescheduling Frequency: 1D

|                                                   |                                                                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/020.png) | The person scheduling the XTPM NIGHTLY PATCH MONITOR option must have the XTPM PATCH MONITOR MGR security key or the option will not run. This is the intended function. |

- XTPM UNINSTALLED PATCH BULLETI:
- Time: 08:00
- Rescheduling Frequency: D@0800 (weekdays at 8 AM)

> An example of setting up the TaskMan parameters for both options is shown in Figure 2‑6.

Option Name: XTPM NIGHTLY PATCH MONITOR

Menu Text: Nightly Patch Monitor TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: FEB 29, 2004 05:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

============================================================================

Option Name: XTPM UNINSTALLED PATCH BULLETI

Menu Text: Uninstalled Patch Bulletin TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: FEB 29, 2004 08:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: D@0800

TASK PARAMETERS:

SPECIAL QUEUEING:

<span id="_Ref112564655" class="anchor"></span>Figure ‑: Set up scheduling frequency for XTPM NIGHTLY PATCH MONITOR and XTPM UNINSTALLED PATCH BULLETI

The following is a sample Uninstalled Patch Report MailMan message, which is the bulletin sent to the site listing what patches are uninstalled.

Subj: Uninstalled Patch Report for TEST.VAMCSITE.MED.VA.GOV for JAN 11,\[#616\]

01/11/06@08:54 16 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

The following patches are uninstalled at this site:

Patch \# Subject Priority Recpt Date Compliance Date

------- ------- -------- ----- ---- ----------

OR\*3\*50 Unsigned Orders Sear Mandatory JAN 3,2006 JAN 31,2006

XU\*8.0\*391 Limit %ZIS page leng Mandatory JAN 9,2006 JAN 11,2006

XU\*8.0\*393 HF routine checksums Mandatory JAN 3,2006 JAN 31,2006

Total: 3

<span id="_Toc125282464" class="anchor"></span>Figure ‑: Sample Uninstalled Patch Report MailMan message

Subj: Patch Monitor Report for TROY ISC SUPPORT ACCOUNT for JAN 13,2006

\[#184380\] 01/13/06@05:00 4 lines

From: POSTMASTER In 'WASTE' basket. Page 1

-------------------------------------------------------------------------------

No Delinquent Patches were found.

Enter message action (in WASTE basket): Ignore//

<span id="_Toc125282465" class="anchor"></span>Figure ‑: Sample "No Delinquent Patches were found" MailMan message

# Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Patch Monitor is comprised of sixteen menu options, organized into the following four menus:

Patch Monitor Main Menu \[XTPM PATCH MONITOR MAIN MENU\]

1.  Patch Processing … \[XTPM PATCH PROCESSING\]
2.  Patch Report … \[XTPM PATCH REPORTS\]
3.  Patch Monitor Management … \[XTPM PATCH MANAGEMENT\]

Patch Processing \[XTPM PATCH PROCESSING\]

1.  Patch Inquiry \[XTPM PATCH INQUIRY\]
2.  Edit Patch Information \[XTPM EDIT PATCH\]
3.  Mark a Non-KIDS Patch as Complete \[XTPM COMPLETE A NON-KIDS PATCH\]

Patch Reports \[XTPM PATCH REPORTS\]

> 1 Complete Patch Installation History \[XTPM COMPLETE PATCH HISTORY\]

> 2 Uninstalled Patches by Compliance Date \[XTPM UNINSTALLED BY COMPLIANCE\]

> 3 Uninstalled Patch Listing - Alphabetical \[XTPM UNINSTALLED PATCHES\]

> 4 Patches Due in the Next Seven Days \[XTPM PATCHES DUE NEXT 7 DAYS\]

> 5 Past Due Patch Report \[XTPM PAST DUE PATCH REPORT\]

> 6 Patch Statistics by Reporting Group \[XTPM PATCH STATISTICS\]

> 7 Patch Statistics by Compliance Date \[XTPM PATCH STATS BY COMPLIANCE\]

Patch Monitor Management \[XTPM PATCH MANAGEMENT\]

> 1 Edit the Patch Monitor Parameter File \[XTPM EDIT PATCH MONITOR PARAMS\]

> 2 Rerun the Nightly Patch Monitor \[XTPM RERUN NIGHTLY\]

\*\*\> Locked with XTPM PATCH MONITOR MGR  
<span id="_Toc65841319" class="anchor"></span>

|                  |                           |
|------------------|---------------------------|
| Patch Processing | \[XTPM PATCH PROCESSING\] |

The Patch Processing menu holds all options necessary to do additional patch processing.

Select Patch Monitor Main Menu Option: 1 \<Enter\> Patch Processing

1 Patch Inquiry

2 Edit Patch Information

3 Mark a Non-Kids Patch as Complete

Select Patch Processing Option:

<span id="_Toc125282466" class="anchor"></span>Figure ‑: Patch Processing menu

|                   |                            |
|-------------------|----------------------------|
| Patch Inquiry | \[XTPM PATCH INQUIRY\] |

This option provides a view of all information on a patch record, which is all the information from the PATCH MONITOR file (#9.9) , including the computed fields:

- DATE INSTALLED (#9)
- INSTALLED BY (#10)

Table 3‑1 lists the prompt used for interacting with this option along with its description.

| Prompt          | Description                                                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| "Enter Patch Name:" | Enter the name of the patch. This is usually same as the install name. The patch name may be ONC\*1\*23 but the install name may be ONC\*1.0\*23. |

<span id="_Ref110678195" class="anchor"></span>Table ‑: Patch Inquiry option—prompt and description

Figure 3‑2 shows and example of the output from the Patch Inquiry option. The inquiry is sent only to the screen.

Patch Inquiry for VAMCSITE, GA.

-----------------------------------------------------------------------

PATCH NAME: ONC\*2.11\*38 DATE OF RECEIPT: FEB 24, 2004

PRIORITY: MANDATORY PARENT PACKAGE: ONC - ONCOLOGY

SEQUENCE NUMBER: 38 PACKAGE VERSION: 2.11

PATCH SUBJECT: DATE OF FIRST CONTACT INSTALL NAME: ONC\*2.11\*38

COMPLIANCE DATE: MAR 25, 2004

DATE INSTALLED (c): FEB 28,2004 INSTALLED BY (c): REDACTED

-----------------------------------------------------------------------

<span id="_Ref110678379" class="anchor"></span>Figure ‑: Patch Inquiry option—output

|                            |                         |
|----------------------------|-------------------------|
| Edit Patch Information | \[XTPM EDIT PATCH\] |

This option allows you to edit the fields of a patch record that were extracted from the mail message. These are items that may need to be changed for various reasons.

Table 3‑2 lists the prompts used for interacting with this option along with a description of each.

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Prompt</strong></th>
<th><strong>Description</strong></th>
</tr>
<tr class="odd">
<th>"Select PATCH MONITOR PATCH NAME:"</th>
<th>Enter the patch name to edit.</th>
</tr>
<tr class="header">
<th>"COMPLIANCE DATE:"</th>
<th><p>Enter the compliance date assigned to the patch.</p>
<p>NOTE: This date would normally be changed only if the compliance date was changed nationally.</p></th>
</tr>
<tr class="odd">
<th>"NON-KIDS PATCH?"</th>
<th><p>Enter 1 or Y if it is a non-KIDS patch or zero or N if not.</p>
<p>NOTE: This field is not normally changed unless indicated for some type of problem.</p>
<p>If it is really a KIDS patch, and the field is already set to YES, you may enter an @ to remove the YES.</p></th>
</tr>
<tr class="header">
<th>"DATE COMPLETED"</th>
<th>This is the date a NON-KIDS patch was completed. This date affects reports only on non-KIDS patches. If inadvertently changed on a KIDS patch, there will be no effects. This field will only be asked if the field “NON-KIDS PATCH?” is set to YES.</th>
</tr>
<tr class="odd">
<th>"NON-KIDS PATCH COMPLETED BY"</th>
<th><p>This is the name of the person who completed the non-KIDS patch. When no value is present, the automatic default is the user who is performing the edits.</p>
<p>NOTE: It should be noted that if the field NON-KIDS PATCH is YES and that answer is deleted by entering an @ sign, then the fields DATE COMPLETED and NON-KIDS PATCH COMPLETED BY will be deleted automatically. This is the way it was intended to work.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref110678616" class="anchor"></span>Table ‑: Edit Patch Information option—prompts and description of each

|                                       |                                        |
|---------------------------------------|----------------------------------------|
| Mark a Non-Kids Patch as Complete | \[XTPM COMPLETE A NON-KIDS PATCH\] |

Using this option will allow you to complete a non-KIDS patch. KIDS patches have a computed field link to the INSTALL file (#9.7) but non-KIDS patches will never have an install record because they do not get processed in the usual manner a KIDS patch is processed. This must be done manually by entering a completion date. After this date is entered, all reports will reflect this date.

Table 3‑3 lists the prompts used for interacting with this option along with a description of each.

| Prompt                         | Description                                                        |
|------------------------------------|------------------------------------------------------------------------|
| "Select PATCH MONITOR PATCH NAME:" | Enter the install name of the patch.                                   |
| "NON-KIDS INSTALL DATE:"           | Enter the date the patch was completed by hand. Time is not permitted. |

<span id="_Ref110678724" class="anchor"></span>Table ‑: Mark a Non-KIDS Patch as Complete option—prompts and description of each

|                                                              |                        |
|--------------------------------------------------------------|------------------------|
| <span id="_Toc125282423" class="anchor"></span>Patch Reports | \[XTPM PATCH REPORTS\] |

This menu has the reports that comprise a large part of the VistA Patch Monitor.

Select Patch Monitor Main Menu Option: 2 \<Enter\> Patch Reports

1 Complete Patch Installation History

2 Uninstalled Patches by Compliance Date

3 Uninstalled Patch Listing - Alphabetical

4 Patches Due in the Next Seven Days

5 Past Due Patch Report

6 Patch Statistics by Reporting Group

7 Patch Statistics by Compliance Date

Select Patch Reports Option:

<span id="_Toc125282471" class="anchor"></span>Figure ‑: Patch Reports menu

|                                         |                                     |
|-----------------------------------------|-------------------------------------|
| Complete Patch Installation History | \[XTPM COMPLETE PATCH HISTORY\] |

This option gives a report of all patches currently in the PATCH MONITOR file (#9.9) and their associated installation history. The output is grouped by compliance date.

Table 3‑4 lists the prompt used for interacting with this option along with its description.

| Prompt       | Description                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| "DEVICE: HOME//" | Enter the device for the output of the report. It may be either to any printer or to the user’s workstation screen. |

<span id="_Ref110679006" class="anchor"></span>Table ‑: Complete Patch Installation History option—prompt and description

COMPLETE PATCH INSTALLATION HISTORY FEB 29,2004 15:59 PAGE 1

COMPLIANCE DATE

DATE INSTALLED PATCH NAME SUBJECT

--------------------------------------------------------------------------------

12/07/03 12/02/03 PSO\*7\*153 TPB PROJECT - HL7 FIX/FAX \#/PROVIDER ERR

12/07/03 12/04/03 SD\*5.3\*318 Transitional Pharmacy Benefit Deferred A

12/11/03 12/11/03 PRS\*4\*88 DECEMBER 26,2003 HOLIDAY

12/15/03 12/10/03 OR\*3\*206 CPRS GUI Version 22.16

12/17/03 12/02/03 PSX\*2\*49 NTE\|5 SEGMENTS CORRECTION

12/18/03 12/17/03 PRS\*4\*86 SR 03-634 FLEXIBLE SPENDING ACCOUNTS

12/19/03 12/04/03 EAS\*1\*40 LTC COPAYMENT PHASE IV

. . . . . . .

. . . . . . .

. . . . . . .

02/04/03 02/02/04 IB\*2\*215 OIG/IVM 60-DAY BILL DROP

03/20/04 02/26/04 OR\*3\*208 ADD PCE OUTPATIENT ENCOUNTERS TO DOD REP

03/20/04 02/24/04 PSD\*3\*44 MODIFICATION OF 'DR' STRING IN ROUTINE P

03/20/04 02/24/04 TIU\*1\*176 TIU E-SIG DISPLAY ENHANCEMENTS

---------------

COUNT 126

(Note: This only a partial report display, due to the actual length of the report.)

<span id="_Toc125282473" class="anchor"></span>Figure ‑: Complete Patch Installation History option—output

|                                            |                                        |
|--------------------------------------------|----------------------------------------|
| Uninstalled Patches by Compliance Date | \[XTPM UNINSTALLED BY COMPLIANCE\] |

This option will give a total view of all uninstalled patches, listed and grouped by compliance date.

Table 3‑5 lists the prompt used for interacting with this option along with its description.

| Prompt  | Description                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------|
| "DEVICE://" | Enter the output device to receive the output. This may be any printer or the workstation screen. |

<span id="_Ref110679194" class="anchor"></span>Table ‑: Uninstalled Patches by Compliance Date option—prompt and description

UNINSTALLED PATCHES BY COMPLIANCE DATE FEB 29,2004 15:49 PAGE 1

COMPLIANCE

DATE PATCH NUMBER DATE RCV PATCH SUBJECT

--------------------------------------------------------------------------------

03/08/04 RMIM\*1\*2 02/06/04 FIX FOR COMPLETING CONSULTS AND MULTIPLE

03/08/04 RMIM\*1\*1 10/08/03 FIM GUI UPDATE 1

03/12/04 HL\*1.6\*84 02/10/04 CACHE/VMS MULTILISTENER & REMOVE TASK FR

03/13/04 IB\*2\*252 02/11/04 MODIFICATIONS TO IB\*2\*184

03/13/04 IVM\*2\*93 02/11/04 INTERIM ADDRESS ENHANCEMENTS FOLLOW UP

03/15/04 DG\*5.3\*560 02/13/04 INTERIM ADDRESS ENHANCEMENTS FOLLOW UP

03/19/04 LA\*5.2\*69 02/17/04 Lab Utility API's

03/20/04 EAS\*1\*44 02/18/04 1010EZ WEB PROCESSING VET SELECTION

03/22/04 HL\*1.6\*109 02/20/04 Improve Performance and Monitoring of HL

03/26/04 SD\*5.3\*324 02/24/04 UNDEF VAR ERROR IN TREND OF FACILITIES R

04/10/04 OR\*3\*176 02/26/04 FILE UPDATES FOR NON-VA MEDS PROJECT

---------------

COUNT 11

<span id="_Toc125282475" class="anchor"></span>Figure ‑: Uninstalled Patches by Compliance Date option—output

|                                              |                                  |
|----------------------------------------------|----------------------------------|
| Uninstalled Patch Listing - Alphabetical | \[XTPM UNINSTALLED PATCHES\] |

This option will output a complete listing of all uninstalled patches in alphabetical order by patch name.

Table 3‑6 lists the prompt used for interacting with this option along with its description.

| Prompt  | Description                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------|
| "DEVICE://" | Enter the output device to receive the output. This may be any printer or the workstation screen. |

<span id="_Ref110679618" class="anchor"></span>Table ‑: Uninstalled Patch Listing - Alphabetical option—prompt and description

Uninstalled Patch Report for VAMCSITE, GA. for FEB 29,2004 Page: 1

Compliance

Patch \# Subject Priority Recpt Date Date

------- ------- -------- ----- ---- ----------

DG\*5.3\*560 INTERIM ADDRESS ENHA Mandatory FEB 13,2004 MAR 15,2004

EAS\*1\*44 1010EZ WEB PROCESSIN Mandatory FEB 18,2004 MAR 20,2004

HL\*1.6\*109 Improve Performance Mandatory FEB 20,2004 MAR 22,2004

HL\*1.6\*84 CACHE/VMS MULTILISTE Mandatory FEB 10,2004 MAR 12,2004

IB\*2\*252 MODIFICATIONS TO IB\* Mandatory FEB 11,2004 MAR 13,2004

IVM\*2\*93 INTERIM ADDRESS ENHA Mandatory FEB 11,2004 MAR 13,2004

LA\*5.2\*69 Lab Utility API's Mandatory FEB 17,2004 MAR 19,2004

OR\*3\*176 FILE UPDATES FOR NON Mandatory FEB 26,2004 APR 10,2004

SD\*5.3\*324 UNDEF VAR ERROR IN T Mandatory FEB 24,2004 MAR 26,2004

Total: 9

<span id="_Toc125282477" class="anchor"></span>Figure ‑: Uninstalled Patch Listing - Alphabetical option—output

|                                        |                                      |
|----------------------------------------|--------------------------------------|
| Patches Due in the Next Seven Days | \[XTPM PATCHES DUE NEXT 7 DAYS\] |

This option will allow package support personnel to look all patches, which will be due within the next seven days.

Table 3‑7 lists the prompt used for interacting with this option along with its description.

| Prompt  | Description                                                                                   |
|-------------|---------------------------------------------------------------------------------------------------|
| "Device://" | Enter the output device to receive the output. This may be any printer or the workstation screen. |

<span id="_Ref110679925" class="anchor"></span>Table ‑: Patches Due in the Next Seven Days option—prompt and description

UNINSTALLED PATCHES DUE IN THE NEXT SEVEN DAYS

FEB 29,2004 15:44 PAGE 1

COMPLIANCE

DATE PATCH NUMBER DATE RCV PATCH SUBJECT

--------------------------------------------------------------------------------

03/03/04 XU\*8.0\*504 02/03/04 Test patch entry

(Note: This is not a real patch)

<span id="_Toc125282479" class="anchor"></span>Figure ‑: Patches Due in the Next Seven Days option—output

|                           |                                    |
|---------------------------|------------------------------------|
| Past Due Patch Report | \[XTPM PAST DUE PATCH REPORT\] |

This option gives a report of all patches that are past the assigned compliance date.

Table 3‑8 lists the prompt used for interacting with this option along with its description.

| Prompt       | Description                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------|
| "DEVICE: HOME//" | Enter the device for the output of the report. It may be either to any printer or to the user’s workstation screen. |

<span id="_Ref110680030" class="anchor"></span>Table ‑: Past Due Patch Report option—prompt and description

Past Due Patch Report for VAMCSITE, GA. for MAR 04,2004 Page: 1

Compliance

Patch \# Subject Priority Recpt Date Date

------- ------- -------- ----- ---- ----------

LA\*5.2\*369 Lab Program API's Mandatory FEB 17,2004 MAR 1,2004

(Note: This is not a real patch)

<span id="_Toc125282481" class="anchor"></span>Figure ‑: Past Due Patch Report option—output

|                                         |                               |
|-----------------------------------------|-------------------------------|
| Patch Statistics by Reporting Group | \[XTPM PATCH STATISTICS\] |

The Patch Statistics program reports installation statistics for any group of packages previously set up in the PATCH MONITOR PARAMETER file (#9.95) as reporting groups. The displayed information is grouped by package namespace.

Table 3‑9 lists the prompts used for interacting with this option along with a description of each.

| Prompt                                                      | Description                                                                                                                                                            |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "Select REPORTING GROUP:"                                       | Enter the name of the group you wish to report. You may use a ? to show what groups are currently defined.                                                                 |
| "Do you want a new form/screen between REPORTING GROUPS? Yes//" | Enter Yes to have each group reported on a separate screen (workstations) or page (printers). Enter No to have them print one after the other, with no spacing in between. |
| "Enter BEGINNING Compliance date:"                              | Enter the beginning compliance date to report.                                                                                                                             |
| "and ENDING Compliance date:"                                   | Enter the ending compliance date to report.                                                                                                                                |
| "DEVICE: HOME//"                                                | Enter the output device, either a workstation screen or a printer.                                                                                                         |

<span id="_Ref110680319" class="anchor"></span>Table ‑: Patch Statistics By Reporting Group option—prompts and description of each

See output example on the next page.

Patch Statistics Output example:

FEB 29,2004 Patch Statistical Report for VAMCSITE, GA. Page: 1

Date range: FEB 1,2004 to FEB 29,2004

Compliance Patch Release Install \# Days

Date Number Date Date Priority Delinquent

------------------------------------------------------------------------------

Report group: KERNEL

FEB 27,2004 DI\*22\*123 JAN 27,2004 JAN 30,2004 Mandatory

FEB 12,2004 XT\*7.3\*75 JAN 12,2004 JAN 14,2004 Mandatory

FEB 22,2004 XT\*7.3\*68 JAN 22,2004 JAN 29,2004 Mandatory

FEB 11,2004 XU\*8\*335 FEB 9,2004 FEB 11,2004 Emergency

FEB 13,2004 XU\*8\*270 JAN 13,2004 JAN 14,2004 Mandatory

FEB 13,2004 XU\*8\*294 JAN 13,2004 JAN 14,2004 Mandatory

Totals patches received for date range: 6

Total patches installed past compliance date: 0

Delinquent patch % : 0.00 %

Compliance % : 100.00 %

<span id="_Toc125282483" class="anchor"></span>Figure ‑: Patch Statistics By Reporting Group option—output

|                                         |                                        |
|-----------------------------------------|----------------------------------------|
| Patch Statistics by Compliance Date | \[XTPM PATCH STATS BY COMPLIANCE\] |

The statistics program reports installation statistics for any compliance date range. It is similar to the previous option that reported by report group. There is no special grouping on this report but by compliance date.

Table 3‑10 lists the prompts used for interacting with this option along with a description of each.

| Prompt                         | Description                                                    |
|------------------------------------|--------------------------------------------------------------------|
| "Enter BEGINNING Compliance date:" | Enter the beginning compliance date to report.                     |
| "and ENDING Compliance date:"      | Enter the ending compliance date to report.                        |
| "DEVICE: HOME//"                   | Enter the output device, either a workstation screen or a printer. |

<span id="_Ref110680474" class="anchor"></span>Table ‑: Patch Statistics By Compliance Date option—prompts and description of each

See output example on the next page.

Patch Statistics By Compliance Date Output example:

FEB 29,2004 Patch Statistical Report for VAMCSITE, GA. Page: 1

By Compliance Date

Date range: FEB 1,2004 to FEB 29,2004

Compliance Patch Release Install \# Days

Date Number Date Date Priority Delinquent

------------------------------------------------------------------------------

FEB 27,2004 DI\*22\*123 JAN 27,2004 JAN 30,2004 Mandatory

FEB 12,2004 XT\*7.3\*75 JAN 12,2004 JAN 14,2004 Mandatory

FEB 22,2004 XT\*7.3\*68 JAN 22,2004 JAN 29,2004 Mandatory

FEB 11,2004 XU\*8\*335 FEB 9,2004 FEB 11,2004 Emergency

FEB 13,2004 XU\*8\*270 JAN 13,2004 JAN 14,2004 Mandatory

FEB 13,2004 XU\*8\*294 JAN 13,2004 JAN 14,2004 Mandatory

Totals patches received for date range: 6

Total patches installed past compliance date: 0

Delinquent patch % : 0.00 %

Compliance % : 100.00 %

<span id="_Toc125282485" class="anchor"></span>Figure ‑: Patch Statistics By Compliance Date option—output

|                                                                         |                           |
|-------------------------------------------------------------------------|---------------------------|
| <span id="_Toc125282424" class="anchor"></span>Patch Monitor Management | \[XTPM PATCH MANAGEMENT\] |

This menu has the management options for the application.

Select Patch Monitor Management Option: 3 \<Enter\> Patch Monitor Management

1 Edit the Patch Monitor Parameter File \[XTPM EDIT PATCH MONITOR PARAMS\]

2 Rerun the Nightly Patch Monitor \[XTPM RERUN NIGHTLY\]

\*\*\> Locked with XTPM PATCH MONITOR MGR

Select Patch Monitor Management Option:

<span id="_Toc125282486" class="anchor"></span>Figure ‑: Patch Monitor Management menu

|                                           |                                        |
|-------------------------------------------|----------------------------------------|
| Edit the Patch Monitor Parameter File | \[XTPM EDIT PATCH MONITOR PARAMS\] |

This option allows the package manager to edit various parameters that control parts of this package. Each is described below.

Table 3‑11 lists the prompts used for interacting with this option along with a description of each.

| Prompt                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "Select PATCH MONITOR PARAMETER SITE NAME:" | Enter the name of your facility. This is a free-text entry of up to 35 characters.                                                                                                                                                                                                                                                                                                                                                                |
| "Select MAIL GROUPS:"                       | Enter the mail group or groups that will receive the daily monitor bulletins about uninstalled patches. These are *not* the groups to receive the delinquent patch bulletins. This field points to the MAIL GROUP file (#3.8) and all groups entered here must already exist in the MAIL GROUP file (#3.8).                                                                                                                                       |
| "NUMBER OF DAYS TO KEEP DATA:"              | Enter the number of days to keep completed patch data on file. This field is overridden by the field “Delete installed patches.” If the field is “Delete Installed Patches” is YES then any number entered in this field is ignored. If the field “Delete Installed Patches” is NO then data will retained for the amount of days entered here. If no value is entered, 30 days are automatically kept. See note below explaining data retention. |
| "DELETE INSTALLED PATCHES?:"                | Enter Y to allow the nightly job to delete all installed patches if they are completed or N to retain them the number of days specified in the field “Number of days to keep data." This field overrides that field. If this field is NO the number of days of patches are kept is determined by the field “Number of Days to Keep Data," or 30 days is kept if no there is no entry in the field. See note below.                                |

<span id="_Ref110680673" class="anchor"></span>Table ‑: Edit the Patch Monitor Parameter File option—prompts and description of each

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/021.png)</td>
<td><h3 id="explanatory-note-about-data-retention-1" class="unnumbered">Explanatory Note About Data Retention</h3>
<p>It is entirely up to a site whether or not patch installation data is retained for statistical reporting purposes. A site may wish to retain data and have a full compliment of reporting for statistics on past periods or it may wish to simply keep up with the current patching scenario and only make sure patches are installed on a timely basis and nothing more.</p>
<p>The site should weigh this decision carefully so as not to delete data unless it realizes the ramifications of it.</p></td>
</tr>
</tbody>
</table>

|                                     |                            |
|-------------------------------------|----------------------------|
| Rerun the Nightly Patch Monitor | \[XTPM RERUN NIGHTLY\] |

This option is the user version of the regular nightly job. It is used to rerun a failed job or it may be run at any time that is deemed necessary. It will update all patch installation information and produce a bulletin sent to designated mail groups. Any reports may then be run with the confidence that they will be up to date.

This manual option is locked with the XTPM PATCH MONITOR MGR security key

There are no prompts and no output.

# Setting Up a New Installation or Recovering Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a site installs the patch monitor for the first time, it may wish to go back and have past patches entered into the PATCH MONITOR file (#9.9). In addition, a site may wish to recover patches for some reason. This is easily accomplished.

A user who receives patches on a regular basis and who has VistA MailMan patches on file for the time period desired, may simply forward the patches (any range or number) to the server option S.XTPM PATCH SERVER. The following example assumes the user is familiar with the VistA Mailman.

1.  Identify the patches to be sent to the file by their sequence number in the VistA MailMan.
2.  Use the Forward command to send the range of messages. Example: 1-5,6,7,10-20,23,5,31. At the “and send to:” prompt, enter S.XTPM PATCH SERVER.

The patches process at a very fast rate and will appear in the file in a few moments.

If a user recovers patches in this manner, it should be understood that:

1.  This should be done during a work day.
2.  KIDS patches will be processed in the normal fashion when the nightly job runs.

|                                                   |                                                                                                                                                 |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/022.png) | Important!! Non-KIDS patches must be completed manually before the nightly job runs or they will be reported as delinquent and cause confusion. |

# Implementation and Maintenance (Technical Manual Information)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*98 is a Kernel Installation and Distribution System (KIDS) software release.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/023.png)</td>
<td><p>For installation and site setup instructions, see the VistA Patch Monitor, Kernel Toolkit Patch XT*7.3*98 located on the VistA Documentation Library at:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/Infrastructure.asp?appID=12">http://www.va.gov/vdl/Infrastructure.asp?appID=12</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Software Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*98 requires a standard VistA operating environment in order to function correctly. Check your VistA environment for software and versions installed.

### Scheduled Options/Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option Name</strong></th>
<th>XTPM NIGHTLY PATCH MONITOR</th>
</tr>
<tr class="odd">
<th><strong>Menu Text</strong></th>
<th>Nightly Patch Monitor</th>
</tr>
<tr class="header">
<th><strong>Description</strong></th>
<th><p>This option is the user version of the regular nightly job. It is used to rerun a failed job or it may be run at any time that is deemed necessary, It will update all patch installation information and produce a bulletin sent to designated mail groups. Any reports may then be run with the confidence that they will be totally up to date. Recommended scheduling frequency is daily (1D at 05:00 – weekdays at 5 AM).</p>
<p>This manual option is locked with the XTPM PATCH MONITOR MGR security key. Personnel scheduling the XTPM NIGHTLY PATCH MONITOR option must have the XTPM PATCH MONITOR MGR security key or the option will not run.</p>
<p>There are no prompts and no output.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc125282488" class="anchor"></span>Table ‑: Scheduled background job—XTPM NIGHTLY PATCH MONITOR

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option Name</strong></th>
<th>XTPM UNINSTALLED PATCH BULLETI</th>
</tr>
<tr class="odd">
<th><strong>Menu Text</strong></th>
<th>Uninstalled Patch Bulletin</th>
</tr>
<tr class="header">
<th><strong>Description</strong></th>
<th><p>This is a run routine option that creates a daily bulletin for IRM to keep up-to-date on uninstalled patches. Recommended scheduling frequency is daily (i.e., D@0800 -- weekdays at 8 AM).</p>
<p><strong>NOTE:</strong> If there are no uninstalled patches, no bulletin will be sent.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc125282489" class="anchor"></span>Table ‑: Scheduled background job—XTPM UNINSTALLED PATCH BULLETI

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are exported with Kernel Toolkit Patch XT\*7.3\*98 in the XTPM namespace:

- XTPMKPCF—Computed fields and other oddities for Patch Monitor
- XTPMKPP—Patch Monitor purging.
- XTPMKPTC—Patch Monitor functions
- XTPMNEX7—Patches due in next 7 days
- XTPMSTA2—Print patch statistics by compliance date
- XTPMSTAT—Print patch statistics by report group

Second line of all routines looks like this:

> ;;7.3;TOOLKIT;\*\*98\*\*; Apr 25, 1995

### Data Dictionaries Exported with XT\*7.3\*98 for New VistA Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| VistA File and Number | Global Location | Data? |
|---------------------------|---------------------|-----------|
| PATCH MONITOR (#9.9)      | ^XPD(9.9            | No        |

STANDARD DATA DICTIONARY \#9.9 -- PATCH MONITOR FILE

AUG 26,2005@19:55:10 PAGE 1

STORED IN ^XPD(9.9, (57 ENTRIES) SITE: SF CIOFO, KERNEL PATCH ACCOUNT UCI:

NXT,KDE (VERSION 7.3)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

This file contains VistA patch information which is stored by a server option

when a patch arrives to G.PATCHES at a site. The server extracts certain

information and stores it here.

A night-time program will then check the file, match it against the install

file. If the current date is past the compliance date for patch installation

(typically 30 days for regular patches, three days for emergency patches) it

will do one of two things:

1\. If the patch has been installed since last run and the parameter

file is set in field 3 to delete installed patches, it will delete the entry

from this file, regardless of the number of days in field 2. If the parameter

file is set to leave patches, it is not deleted.

2\. If the patch has NOT been installed, its information will be saved

and reported via a mail message to a group.

The person(s) who are in charge of monitoring patches at the site or perhaps

for the VISN will be responsible for following up on delinquent patches.

DD ACCESS: @

RD ACCESS: \#

WR ACCESS: @

DEL ACCESS: @

LAYGO ACCESS: @

AUDIT ACCESS: \#

CROSS

REFERENCED BY: PATCH NAME(B), DATE OF RECEIPT(C), COMPLIANCE DATE(D),

NON-KIDS INSTALL DATE(E)

CREATED ON: JUL 21,2005 by TRAN,BA

9.9,.01 PATCH NAME 0;1 FREE TEXT (Required)

INPUT TRANSFORM: K:\$L(X)\>20!(\$L(X)\<3)!'(X'?1P.E) X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Answer must be 3-20 characters in length.

DESCRIPTION: This is the name of the patch as it comes in

the mail message.

Examples: RMIM\*1\*1

DG\*5.3\*211

CROSS-REFERENCE: 9.9^B

1)= S ^XPD(9.9,"B",\$E(X,1,30),DA)=""

2)= K ^XPD(9.9,"B",\$E(X,1,30),DA)

9.9,1 DATE OF RECEIPT 0;2 DATE

INPUT TRANSFORM: S %DT="EX" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: The date the patch was received in-house.

DESCRIPTION: This is the date the patch was received

in-house.

CROSS-REFERENCE: 9.9^C

1)= S ^XPD(9.9,"C",\$E(X,1,30),DA)=""

2)= K ^XPD(9.9,"C",\$E(X,1,30),DA)

Index by Date of Receipt.

9.9,2 PRIORITY 0;3 SET

'm' FOR MANDATORY;

'e' FOR EMERGENCY;

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Enter the priority of the patch. Type ? for

help.

DESCRIPTION: The priority assigned to this patch. Typical

is "mandatory".

9.9,3 PARENT PACKAGE 0;4 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>35!(\$L(X)\<3) X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: The parent package of the patch.

DESCRIPTION: This is the package for which the patch was

issued.

This field must be free text because of the

possibility of having a patch issued for a new

package without the package having been

installed yet.

9.9,4 SEQUENCE NUMBER 0;5 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>999999999999)!(X\<1)!(X?.E1"."1N.N) X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: The sequence number of the patch.

DESCRIPTION: This is the sequence number assigned to the

patch by the National Patch Module.

9.9,5 PACKAGE VERSION 0;6 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>10!(\$L(X)\<1) X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: The version assignment of the parent package.

DESCRIPTION: This is the version of the parent package for

which a patch is sent. It is determined from

the patch information in the message.

9.9,6 PATCH SUBJECT 0;7 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>50!(\$L(X)\<3) X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Answer must be 3-50 characters in length.

DESCRIPTION:

This is the subject of the patch.

9.9,7 INSTALL NAME 0;8 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>35!(\$L(X)\<3) X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Answer must be 3-35 characters in length.

DESCRIPTION: The installation information may or may not be

in the INSTALL file for a patch. This may be

because of:

a\. The package is new and may not yet

be loaded

but already has patches issued.

b\. The patch is a non-kids patch for

executables, etc.

9.9,8 COMPLIANCE DATE 0;9 DATE

INPUT TRANSFORM: S %DT="EX" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: This is the date the patch must be installed

by.

DESCRIPTION: This is the date by which the patch must be

installed.

CROSS-REFERENCE: 9.9^D

1)= S ^XPD(9.9,"D",\$E(X,1,30),DA)=""

2)= K ^XPD(9.9,"D",\$E(X,1,30),DA)

Index by Compliance Date.

9.9,9 DATE INSTALLED ; COMPUTED

MUMPS CODE: D ^XTPMKPCF

ALGORITHM: D ^XTPMKPCF

LAST EDITED: AUG 02, 2005

DESCRIPTION: This is a computed field, driven by a mumps

routine AWBCKPCF. This is a special routine to

calculate the date installed from the INSTALL

file. It reads the index backwards to find the

last installed version by taking the

\$O(^XPD(9.7,"B",\[INSTALL NAME\],9999999999),-1)

This is done because there may be several test

versions on file in INSTALL file which may

affect the true installation date determination

9.9,10 INSTALLED BY ; COMPUTED

MUMPS CODE: D WHO^XTPMKPCF

ALGORITHM: D WHO^XTPMKPCF

LAST EDITED: AUG 02, 2005

DESCRIPTION: This is a computed field driven also by the

routine AWBCKPCF at entry point WHO. It tells

who installed the patch.

9.9,11 NON-KIDS PATCH? 0;10 SET

'1' FOR YES;

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Enter 1 if a Non-KIDS patch.

DESCRIPTION: This field determines what happens in various

areas of the package. A patch can be KIDs or

non-KIDs. The data on a patch record can be

either NULL (KIDs patch) or 1 (Non-KIDs patch).

The field can actually be only set to a 1 or

the information deleted (NULL).

9.9,12 NON-KIDS INSTALL DATE 0;11 DATE

INPUT TRANSFORM: S %DT="EX" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Enter the date this NON-KIDS patch was

completed.

DESCRIPTION: Non-KIDs patches are those which do not have an

accompanying KIDs install in the Packman

message because:

o It may have an accompanying host

file (too large for a mail

message) or

o It may be a patch message referring

to a .zip, .exe or other

file which will not put an entry

into the INSTALL file.

Because of this, there is no install record to

extract the install date and it must be entered

(i.e., completed) by filling in this field.

CROSS-REFERENCE: 9.9^E

1)= S ^XPD(9.9,"E",\$E(X,1,30),DA)=""

2)= K ^XPD(9.9,"E",\$E(X,1,30),DA)

ndex by Non-Kids Install Date.

9.9,13 NON-KIDS PATCH COMPLETED BY 0;12 POINTER TO NEW PERSON FILE (#200

)

LAST EDITED: JUL 21, 2005

HELP-PROMPT: This is the name of the person who completed

the non-KIDs patch.

DESCRIPTION: This is a pointer to file 200 to record who

completed the non-KIDs patch.

FILES POINTED TO FIELDS

NEW PERSON (#200) NON-KIDS PATCH COMPLETED BY (#13)

INPUT TEMPLATE(S):

XTPM COMPLETE NON-KIDS PATCH JUL 21, 2005@06:43 USER \#0

XTPM EDIT PATCH JUL 21, 2005@07:57 USER \#0

PRINT TEMPLATE(S):

CAPTIONED USER \#0

XTPM COMPLETE PATCH HISTORY JUL 21, 2005@08:06 USER \#0

COMPLETE PATCH INSTALLATION HISTORY

XTPM UNINSTALLED BY COMPLIANCEJUL 21, 2005@09:30 USER \#0

UNINSTALLED PATCHES BY COMPLIANCE DATE

SORT TEMPLATE(S):

XTPM COMPLETE PATCH HISTORY JUL 21, 2005@08:02 USER \#0

SORT BY: @COMPLIANCE DATE;S1// (COMPLIANCE DATE not null)

WITHIN COMPLIANCE DATE, SORT BY: PATCH NAME// (PATCH NAME not null)

Prints a complete patch installation history.

XTPM UNINSTALLED BY COMPLIANCEJUL 21, 2005@09:27 USER \#0

SORT BY: @COMPLIANCE DATE;S// (COMPLIANCE DATE from Jan 1,1901 to Dec 31,2499@24

:00)

WITHIN COMPLIANCE DATE, SORT BY: PATCH NAME// (PATCH NAME not null)

WITHIN PATCH NAME, SORT BY: \$S(NON-KIDS PATCH?="YES":NON-KIDS INSTALL DATE,1

:DATE INSTALLED)="";L1// (\$S(NON-KIDS PATCH?=""YES"":NON-KIDS INSTALL DATE,1:DAT

E INSTALLED)="""")

Uninstalled patches by compliance date.

FORM(S)/BLOCK(S):

<span id="_Toc125282490" class="anchor"></span>Table ‑: Data dictionary (new PATCH MONITOR file \#9.9)

| VistA File and Number       | Global Location | Data? |
|---------------------------------|---------------------|-----------|
| PATCH MONITOR PARAMETER (#9.95) | ^XPD(9.95           | No        |

STANDARD DATA DICTIONARY \#9.95 -- PATCH MONITOR PARAMETER FILE

AUG 26,2005@19:55:25 PAGE 1

STORED IN ^XPD(9.95, (2 ENTRIES) SITE: SF CIOFO, KERNEL PATCH ACCOUNT UCI:

NXT,KDE (VERSION 7.3)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

This is the parameter file that controls certain functions of the Patch Monitor

software:

.01 SITE NAME

1 MAIL GROUPS (multiple)

2 NUMBER OF DAYS TO KEEP DATA

3 DELETE INSTALLED PATCHES?

Site name: Free text name of the facility.

Mail groups: groups that wish to receive the uninstalled bulletin.

Number of days to keep data: number of days to allow data to remain, provided

field 3 is answered NO. If field 3 is answered YES, this field is ignored.

Delete installed patches? - YES allows the nightly job to remove patches shown

as installed. NO does not remove them. If this field is answered YES, field 2

is ignored.

DD ACCESS: @

RD ACCESS: \#

WR ACCESS: @

DEL ACCESS: @

LAYGO ACCESS: @

AUDIT ACCESS: \#

CROSS

REFERENCED BY: SITE NAME(B)

CREATED ON: JUL 21,2005 by TRAN,BA

9.95,.01 SITE NAME 0;1 FREE TEXT (Required)

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<3)!'(X'?1P.E) X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Enter the name of your site.

DESCRIPTION: The free text name of the facility that is

tracking the patches.

CROSS-REFERENCE: 9.95^B

1)= S ^XPD(9.95,"B",\$E(X,1,30),DA)=""

2)= K ^XPD(9.95,"B",\$E(X,1,30),DA)

9.95,1 MAIL GROUPS 1;0 POINTER Multiple \#9.951

DESCRIPTION: This is a multiple field that has all the mail

groups you wish to send an uninstalled patch

bulletin to.

9.951,.01 MAIL GROUPS 0;1 POINTER TO MAIL GROUP FILE (#3.8)

(Multiply asked)

LAST EDITED: JUL 21, 2005

DESCRIPTION: The name of a mail group that wishes to

receive uninstalled patch bulletins.

CROSS-REFERENCE: 9.951^B

1)= S ^XPD(9.95,DA(1),1,"B",\$E(X,1,30),DA)=""

2)= K ^XPD(9.95,DA(1),1,"B",\$E(X,1,30),DA)

9.95,2 NUMBER OF DAYS TO KEEP DATA 0;2 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>99999)!(X\<7)!(X?.E1"."1N.N) X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Enter a number from 7 to 99999 for the number

of days to keep data, if you are not deleting

when patches are installed.

DESCRIPTION: If the site wishes to keep the data recording

patch installations on file, this field keeps

the number of days the site wishes to keep on

file. This field is not used if field 3,

DELETE INSTALLED PATCHES? is answered 1 or YES.

9.95,3 DELETE INSTALLED PATCHES? 0;3 SET

'0' FOR No;

'1' FOR Yes;

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Enter 1 or YES to allow the night-time job to

remove installed patches, or 0 or NO to leave

them for future tracking.

DESCRIPTION: If the site wishes, patches that are installed

may be deleted by the night time job. This is

only if they wish NOT to track timely

installation.

If this field is answered 1 or YES, field 2,

NUMBER OF DAYS TO KEEP DATA is ignored.

9.95,4 REPORTING GROUP 2;0 Multiple \#9.954

9.954,.01 REPORTING GROUP 0;1 FREE TEXT (Multiply asked)

INPUT TRANSFORM: K:\$L(X)\>15!(\$L(X)\<3) X

LAST EDITED: JUL 21, 2005

HELP-PROMPT: Enter the name of a reporting group for

statistics. \[3-15 characters\]

DESCRIPTION:

Statistical reporting group name.

CROSS-REFERENCE: 9.954^B

1)= S ^XPD(9.95,DA(1),2,"B",\$E(X,1,30),DA)=""

2)= K ^XPD(9.95,DA(1),2,"B",\$E(X,1,30),DA)

9.954,1 NAME SPACE 1;0 Multiple \#9.9541

9.9541,.01 NAME SPACE 0;1 FREE TEXT (Multiply asked)

INPUT TRANSFORM:K:\$L(X)\>4!(\$L(X)\<2) X D:\$D(X) PKGLOOK^XTPMKPC

F

LAST EDITED: AUG 02, 2005

HELP-PROMPT: Enter the name space to report. This is

cross-checked against the Package file (#9.4).

\[2-4 characters\]

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE:9.9541^B

1)= S ^XPD(9.95,DA(2),2,DA(1),1,"B",\$E(X,1,30),

DA)=""

2)= K ^XPD(9.95,DA(2),2,DA(1),1,"B",\$E(X,1,30),

DA)

FILES POINTED TO FIELDS

MAIL GROUP (#3.8) MAIL GROUPS:MAIL GROUPS (#.01)

INPUT TEMPLATE(S):

XTPM EDIT PATCH MONITOR PARAMSJUL 21, 2005@11:46 USER \#0

PRINT TEMPLATE(S):

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

<span id="_Toc125282491" class="anchor"></span>Table ‑: Data dictionary (new PATCH MONITOR PARAMETER file \#9.95)

### Options Exported with Kernel Toolkit Patch XT\*7.3\*98

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option and Menu Text</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>XTPM COMPLETE A NON-KIDS PATCH</p>
<p>Mark a Non-Kids Patch as Complete</p></td>
<td>This option allows the completion of a non-kids patch, which is defined as not having any KIDS installs, but rather a .ZIP, .EXE, or other type patch (e.g., a DBA patch).</td>
</tr>
<tr class="even">
<td><p>XTPM COMPLETE PATCH HISTORY</p>
<p>Complete Patch Installation History</p></td>
<td>Provides a complete patch installation history.</td>
</tr>
<tr class="odd">
<td><p>XTPM EDIT PATCH</p>
<p>Edit Patch Information</p></td>
<td><p>This option will allow you to edit the fields:</p>
<ul>
<li><p>COMPLIANCE DATE (#8)</p></li>
<li><p>NON-KIDS PATCH? (#11)</p></li>
<li><p>NON-KIDS INSTALL DATE (#12)</p></li>
</ul>
<p>The only fields that may be edited are ones that are not:</p>
<ul>
<li><p>extracted from the patch message</p></li>
<li><p>computed fields may be edited.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>XTPM EDIT PATCH MONITOR PARAMS</p>
<p>Edit the Patch Monitor Parameter File</p></td>
<td>Edits the parameter file for the Patch Monitor.</td>
</tr>
<tr class="odd">
<td><p>XTPM NIGHTLY PATCH MONITOR</p>
<p>Nightly Patch Monitor</p></td>
<td>This background job is a Taskman routine that checks File #9.9 for delinquent patches. It generates a mail message to the mail group G.PATCH MONITOR.</td>
</tr>
<tr class="even">
<td><p>XTPM PAST DUE PATCH REPORT</p>
<p>Past Due Patch Report</p></td>
<td>Provides a quick report for delinquent patches for a site.</td>
</tr>
<tr class="odd">
<td><p>XTPM PATCH INQUIRY</p>
<p>Patch Inquiry</p></td>
<td>Provides an inquiry from the PATCH MONITOR File (#9.9), including computed fields.</td>
</tr>
<tr class="even">
<td><p>XTPM PATCH MANAGEMENT</p>
<p>Patch Monitor Management</p></td>
<td>Patch monitor management menu.</td>
</tr>
<tr class="odd">
<td><p>XTPM PATCH MONITOR MAIN MENU</p>
<p>Patch Monitor Main Menu</p></td>
<td>This is the main menu comprising all the options for the VistA Patch Monitor. This nightly job is locked with the XTPM PATCH MONITOR MGR key.</td>
</tr>
<tr class="even">
<td><p>XTPM PATCH PROCESSING</p>
<p>Patch Processing</p></td>
<td>Patch processing menu. Has all necessary to process patches.</td>
</tr>
<tr class="odd">
<td><p>XTPM PATCH REPORTS</p>
<p>Patch Report</p></td>
<td>Patch monitor reporting menu.</td>
</tr>
<tr class="even">
<td><p>XTPM PATCH SERVER</p>
<p>Patch Monitor Server</p></td>
<td>This is a server option to unload patch messages into the PATCH MONITOR file (#9.9).</td>
</tr>
<tr class="odd">
<td><p>XTPM PATCH STATISTICS</p>
<p>Patch Statistics by Reporting Group</p></td>
<td>This is a statistical report that gives information about patch installation timeliness. It is activated by setting up groups of packages to monitor in the PARAMETER file.</td>
</tr>
<tr class="even">
<td><p>XTPM PATCH STATS BY COMPLIANCE</p>
<p>Patch Statistics by Compliance Date</p></td>
<td>Prints statistics by compliance date.</td>
</tr>
<tr class="odd">
<td><p>XTPM PATCHES DUE NEXT 7 DAYS</p>
<p>Patches Due in the Next Seven Days</p></td>
<td>Uninstalled patches, due within the next seven days.</td>
</tr>
<tr class="even">
<td><p>XTPM RERUN NIGHTLY</p>
<p>Rerun the Nightly Patch Monitor</p></td>
<td><p>This is a TaskMan routine that checks File #9.9 for delinquent patches. It generates a mail message to the mail group G.PATCH MONITOR.</p>
<p>This option is locked with XTPM PATCH MONITOR MGR</p></td>
</tr>
<tr class="odd">
<td><p>XTPM UNINSTALLED BY COMPLIANCE</p>
<p>Uninstalled Patches by Compliance Date</p></td>
<td>Uninstalled patches by compliance date.</td>
</tr>
<tr class="even">
<td><p>XTPM UNINSTALLED PATCH BULLETI</p>
<p>Uninstalled Patch Bulletin</p></td>
<td><p>Daily bulletin for IRM to keep up-to-date on uninstalled patches.</p>
<p><strong>NOTE:</strong> If there are no uninstalled patches, no bulletin is sent.</p></td>
</tr>
<tr class="odd">
<td><p>XTPM UNINSTALLED PATCHES</p>
<p>Uninstalled Patch Listing - Alphabetical</p></td>
<td>Provides a list of all uninstalled patches for a site.</td>
</tr>
</tbody>
</table>

<span id="_Toc104264430" class="anchor"></span>Table ‑: Options exported with Kernel Toolkit Patch XT\*7.3\*98

#### Menu Diagram

Patch Monitor Main Menu (XTPM PATCH MONITOR MAIN MENU)

\|

\|

----1 Patch Processing \[XTPM PATCH ---------1 Patch Inquiry \[XTPM PATCH

PROCESSING\] INQUIRY\]

\|

\|---------------------------------2 Edit Patch Information \[XTPM

\| EDIT PATCH\]

\| \*\*EXIT ACTION:

\| W @IOF,!

\|

\|---------------------------------3 Mark a Non-Kids Patch as

Complete \[XTPM COMPLETE A

NON-KIDS PATCH\]

----2 Patch Reports \[XTPM PATCH ------------1 Complete Patch Installation

REPORTS\] History \[XTPM COMPLETE PATCH

\| HISTORY\]

\| \*\*EXIT ACTION:

\| W \$C(7),!!,"Press ENTER to end

\| " R XTBANS:DTIME K XTBANS

\|

\|---------------------------------2 Uninstalled Patches by

\| Compliance Date \[XTPM

\| UNINSTALLED BY COMPLIANCE\]

\| \*\*EXIT ACTION:

\| W \$C(7),!!,"Press RETURN to

\| continue " R ANS:DTIME K ANS

\|

\|---------------------------------3 Uninstalled Patch Listing -

\| Alphabetical \[XTPM UNINSTALLED

\| PATCHES\]

\| \*\*EXIT ACTION:

\| W \$C(7),!!,"Press ENTER to end

\| " R XTBANS:DTIME K XTBANS

\|

\|---------------------------------4 Patches Due in the Next Seven

\| Days \[XTPM PATCHES DUE NEXT 7

\| DAYS\]

\|

\|---------------------------------5 Past Due Patch Report \[XTPM

\| PAST DUE PATCH REPORT\]

\| \*\*EXIT ACTION:

\| W \$C(7),!!,"Press ENTER to end

\| " R XTBANS:DTIME K XTBANS

\|

\|---------------------------------6 Patch Statistics by Reporting

\| Group \[XTPM PATCH STATISTICS\]

\|

\|---------------------------------7 Patch Statistics by Compliance

Date \[XTPM PATCH STATS BY

COMPLIANCE\]

----3 Patch Monitor Management \[XTPM -------1 Edit the Patch Monitor

PATCH MANAGEMENT\] Parameter File \[XTPM EDIT

\| PATCH MONITOR PARAMS\]

\| \*\*ENTRY ACTION:

\| W @IOF,!,"Edit the Patch

\| Monitor Parameter File",!!!!

\| \*\*EXIT ACTION:

\| W @IOF,!!

\|

\|---------------------------------2 Rerun the Nightly Patch

Monitor \[XTPM RERUN NIGHTLY\]

\*\*LOCKED: XTPM PATCH MONITOR

MGR\*\*

<span id="_Toc125282493" class="anchor"></span>Figure ‑: Menu diagram

### VA FileMan Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Print Templates

The following print templates, including file name and number, are exported with Kernel Toolkit Patch XT\*7.3\*98:

| Print Template             | RD | WR | File Name and Number |
|--------------------------------|--------|--------|--------------------------|
| XTPM COMPLETE PATCH HISTORY    | @      | @      | PATCH MONITOR (#9.9)     |
| XTPM UNINSTALLED BY COMPLIANCE | @      | @      | PATCH MONITOR (#9.9)     |

<span id="_Toc104264434" class="anchor"></span>Table ‑: VA FileMan print templates exported with Kernel Toolkit Patch XT\*7.3\*98

#### Sort Templates

The following sort templates, including file name and number and description, are exported with Kernel Toolkit Patch XT\*7.3\*98:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sort Template</strong></th>
<th><strong>RD</strong></th>
<th><strong>WR</strong></th>
<th><strong>File Name and Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XTPM COMPLETE PATCH HISTORY</td>
<td>@</td>
<td>@</td>
<td>PATCH MONITOR (#9.9)</td>
<td><p>SORT BY: @COMPLIANCE DATE;S1// (COMPLIANCE DATE not null)</p>
<p>WITHIN COMPLIANCE DATE, SORT BY: PATCH NAME// (PATCH NAME not null)</p>
<p>Prints a complete patch installation history.</p></td>
</tr>
<tr class="even">
<td>XTPM UNINSTALLED BY COMPLIANCE</td>
<td>@</td>
<td>@</td>
<td>PATCH MONITOR (#9.9)</td>
<td><p>SORT BY: @COMPLIANCE DATE;S1// (COMPLIANCE DATE from Jan 1,1901 to Dec 31,2499@24:00)</p>
<p>WITHIN COMPLIANCE DATE, SORT BY: PATCH NAME// (PATCH NAME not null)</p>
<p>WITHIN PATCH NAME, SORT BY: $S(NON-KIDS PATCH?="YES":NON-KIDS INSTALL DATE,1:DATE INSTALLED)="";L1// ($S(NON-KIDS PATCH?=""YES"":NON-KIDS INSTALL DATE,1:DATE INSTALLED)="""")</p>
<p>Uninstalled patches by compliance date.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc104264435" class="anchor"></span>Table ‑: VA FileMan sort templates exported with Kernel Toolkit Patch XT\*7.3\*98

#### Input Templates

The following input templates, including file name and number, are exported with Kernel Toolkit Patch XT\*7.3\*98:

| Input Template             | RD | WR | File Name and Number        |
|--------------------------------|--------|--------|---------------------------------|
| XTPM COMPLETE NON-KIDS PATCH   | @      | @      | PATCH MONITOR (#9.9)            |
| XTPM EDIT PATCH                | @      | @      | PATCH MONITOR (#9.9)            |
| XTPM EDIT PATCH MONITOR PARAMS | @      | @      | PATCH MONITOR PARAMETER (#9.95) |

<span id="_Toc125282496" class="anchor"></span>Table ‑: VA FileMan input templates exported with Kernel Toolkit Patch XT\*7.3\*98

### Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no application-specific archiving procedures or recommendations for the Kernel Toolkit Patch XT\*7.3\*98.

### Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines exported with Kernel Toolkit Patch XT\*7.3\*98.

### External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no external interfaces exported with Kernel Toolkit Patch XT\*7.3\*98.

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Mail Group Name     | Description                                                                                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XTPM PATCH MONITOR      | This is a public mail group that receives the delinquent patch notices. Members of this group should be personnel installing patches and who use the Patch Monitor. |
| XTPM PATCH MONITOR USER | This is a public and unrestricted mail group. Members of this group should be personnel using the Patch Monitor.                                                    |

<span id="_Toc104264436" class="anchor"></span>Table ‑: Mail group exported with Kernel Toolkit Patch XT\*7.3\*98

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/024.png)</td>
<td><p>Patches are usually sent to the <strong>G.PATCHES</strong> mail group, which should be standard at all sites. If this mail group does not exist at a site, any mail group that receives national patches may be used.</p>
<p>In this mail group, a server option, S.XTPM PATCH SERVER, is added as a "remote user." When Mailman delivers the message, the server option receives the message, examines it line by line and extracts certain information. This message data then is stored in the PATCH MONITOR file (#9.9).</p></td>
</tr>
</tbody>
</table>

### External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software Dependencies

Kernel Toolkit Patch XT\*7.3\*98 requires a standard VistA operating environment in order to function correctly. Check your VistA environment for software and versions installed.

### Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*98 uses the XTPM and XPD namespaces.

  
File Numbers

Kernel Toolkit Patch XT\*7.3\*98 file numbers and global locations are listed as follows:

| File \# | Global |
|-------------|------------|
| 9.9         | ^XPD(9.9   |
| 9.95        | ^XPD(9.95  |

<span id="_Toc104264437" class="anchor"></span>Table ‑: File list

### Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*98 contains no software-wide variables.

## Software Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no software-specific mail groups release with Kernel Toolkit Patch XT\*7.3\*98 of interest to Information Security Officers (ISO).

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no remote systems involved with the release with Kernel Toolkit Patch XT\*7.3\*98.

### Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no software-specific archiving procedures or recommendations for Kernel Toolkit Patch XT\*7.3\*98.

### Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specialized (*not* VA produced) products (hardware and/or software) embedded within or required by Kernel Toolkit Patch XT\*7.3\*98.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no electronic signatures used in Kernel Toolkit Patch XT\*7.3\*98.

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no options of particular interest to Information Security Officers (ISOs) in Kernel Toolkit Patch XT\*7.3\*98.

### Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Toolkit Patch XT\*7.3\*98 export the XTPM PATCH MONITOR MGR security key. Give the security key XTPM PATCH MONITOR MGR to the person designated as package manager. This key is necessary to schedule the Nightly Patch Monitor option because if the person who schedules the option does not have it, the option *will not* run

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 36%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File #</strong></th>
<th><strong>File Name</strong></th>
<th><strong>DD</strong></th>
<th><strong>RD</strong></th>
<th><strong>WR</strong></th>
<th><strong>DEL</strong></th>
<th><strong>LAYGO</strong></th>
<th><strong>AUDIT</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>9.9</p>
</blockquote></td>
<td><blockquote>
<p>PATCH MONITOR</p>
</blockquote></td>
<td>@</td>
<td><strong>#</strong></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><strong>#</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9.95</p>
</blockquote></td>
<td><blockquote>
<p>PATCH MONITOR PARAMETER</p>
</blockquote></td>
<td>@</td>
<td><strong>#</strong></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><strong>#</strong></td>
</tr>
</tbody>
</table>

<span id="_Toc477786052" class="anchor"></span>Table ‑: File security

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td>API</td>
<td>VistA Application Program Interfaces (APIs) are units of programming code provided by a custodial development domain to permit developers outside the custodial domain to accomplish a specified purpose. APIs in VistA may be defined as extrinsic functions, extrinsic special variables, or label references to routines. They allow programmers to carry out standard computing activities without needing to duplicate utilities in their own software. APIs also further DBA goals of system integration by channeling activities, such as adding new users, through a limited number of callable entry points.</td>
</tr>
<tr class="even">
<td>CAVHCS</td>
<td>Central Alabama Veterans Health Care System</td>
</tr>
<tr class="odd">
<td>CIO</td>
<td>Chief Information Office</td>
</tr>
<tr class="even">
<td>Class III Software</td>
<td>VistA software that is not released nationally through Enterprise VistA Support (EVS) and not publicly available through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="odd">
<td>DaIS</td>
<td>Development &amp; Infrastructure Support</td>
</tr>
<tr class="even">
<td>Data Dictionary (DD)</td>
<td><p>The Data Dictionary is a global containing a description of what kind of data is stored in the global corresponding to a particular file. The data is used internally by VA FileMan for interpreting and processing files.</p>
<p>A Data Dictionary contains the definitions of a file's elements (fields or data attributes), relationships to other files, and structure or design. Users generally review the definitions of a file's elements or data attributes; programmers review the definitions of a file's internal structure.</p></td>
</tr>
<tr class="odd">
<td>EVS</td>
<td>Enterprise VistA Support</td>
</tr>
<tr class="even">
<td>FORUM</td>
<td>The central E-mail system within VistA. It is used by developers to communicate at a national level about programming and other issues. FORUM is located at the Chief Information Office (CIO) Field Office—Washington, DC (162-2).</td>
</tr>
<tr class="odd">
<td>FTP</td>
<td>File Transfer Protocol</td>
</tr>
<tr class="even">
<td>HSD&amp;D</td>
<td>Health Systems Design &amp; Development</td>
</tr>
<tr class="odd">
<td>HSITES</td>
<td>Health Systems Implementation Training and Enterprise Support</td>
</tr>
<tr class="even">
<td>IEN</td>
<td>Internal Entry Number</td>
</tr>
<tr class="odd">
<td>ISS</td>
<td>Infrastructure &amp; Security Services</td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>Set of VistA software routines that function as an intermediary between the host operating system and the VistA application packages such as Laboratory, Pharmacy, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying M implementation.</td>
</tr>
<tr class="odd">
<td>KIDS</td>
<td>Kernel Installation and Distribution System</td>
</tr>
<tr class="even">
<td>M (ANSI Standard)</td>
<td>A programming language recognized by the American National Standards Institute (ANSI). The acronym M (formerly MUMPS) stands for Massachusetts General Hospital Utility Multi-programming System.</td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td>VistA software that provides a mechanism for handling electronic communication, whether it’s user-oriented mail messages, automatic firing of bulletins or initiation of server-handled data transmissions.</td>
</tr>
<tr class="even">
<td>Namespacing</td>
<td>Convention for naming VistA package elements. The database administrator (DBA) assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.</td>
</tr>
<tr class="odd">
<td>OIFO</td>
<td>Office of Information Field Office</td>
</tr>
<tr class="even">
<td>Option</td>
<td>An entry in the OPTION file (#19). As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by Task Manager.</td>
</tr>
<tr class="odd">
<td>OS</td>
<td>Operating System</td>
</tr>
<tr class="even">
<td>Programmer Access</td>
<td>Programmer access in VistA is defined as DUZ(0)="@." It grants the privilege to become a programmer in VistA. Referred to as "having the at-sign ('<strong>@</strong>')" because the at-sign is the DUZ(0) value that grants programmer access. Programmer access allows you to work outside many of the security controls enforced by the XUPROGMODE Security key, enables access to all VA FileMan files, access to modify data dictionaries, etc. It is important to proceed with caution when having access to the system in this way.</td>
</tr>
<tr class="odd">
<td>Routine</td>
<td>Program or a sequence of instructions called by a program that may have some general or frequent use. M (previously referred to as MUMPS) routines are groups of program lines, which are saved, loaded, and called as a single unit via a specific name.</td>
</tr>
<tr class="even">
<td>SDD</td>
<td>Software Design Document</td>
</tr>
<tr class="odd">
<td>Security Key</td>
<td>The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="even">
<td>Servant Site</td>
<td>Servant Sites receive the MailMan messages containing patch installations sent by the Master Site for remote automated installation.</td>
</tr>
<tr class="odd">
<td>SRS</td>
<td>Software Requirements Specification</td>
</tr>
<tr class="even">
<td>TCP/IP</td>
<td>Transmission Control Protocol/Internet Protocol</td>
</tr>
<tr class="odd">
<td>Template</td>
<td>Means of storing report formats, data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use later. Edit sequences are stored in the INPUT TEMPLATE file (#.402), print specifications are stored in the PRINT TEMPLATE file (#.4), and search or sort specifications are stored in the SORT TEMPLATE file (#.401).</td>
</tr>
<tr class="even">
<td>VA</td>
<td>The Department of Veterans Affairs, formerly called the Veterans Administration.</td>
</tr>
<tr class="odd">
<td>VAMC</td>
<td>Veterans Affairs Medical Center</td>
</tr>
<tr class="even">
<td>VAPU</td>
<td>VistA Auto Patch Utility</td>
</tr>
<tr class="odd">
<td>Variable</td>
<td>Character or group of characters, that refers to a value. M (previously referred to as MUMPS) recognizes three types of variables: local variables, global variables, and special variables. Local variables exist in a partition of main memory and disappear at sign-off. A global variable is stored on disk, potentially available to any user. Global variables usually exist as parts of global arrays. The term "global" may refer to either a global variable or a global array. A special variable is defined by systems operations (e.g., $TEST).</td>
</tr>
<tr class="even">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="odd">
<td>VISN</td>
<td>Veterans Integrated Service Network</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture (VistA) of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). VistA software, developed by VA, is used to support clinical and administrative functions at VA Medical Centers nationwide. It is written in M, and, via the Kernel runs on all major M implementations regardless of vendor. VistA is composed of packages, which undergo a verification process to ensure conformity with namespacing and other VistA standards and conventions.</td>
</tr>
<tr class="odd">
<td>VistA Auto Patch Utility (VAPU)</td>
<td>Class III software developed in response to the VHA VistA Challenge, reclassified as Class I and released nationally as Kernel Patch XU*8*345. The VistA Auto Patch Utility software automates the Kernel Installation and Distribution System (KIDS) installation steps, giving the VAMCs the ability to automate patch installations.</td>
</tr>
<tr class="even">
<td>VistA Patch Monitor</td>
<td><p>The VistA Patch Monitor is a package designed to assist package support and management personnel in keeping up with VistA patch requirements. It monitors patches as they arrive in the VistA MailMan, records pertinent data and then monitors them on a daily basis through automated processing.</p>
<p>This package will track only patches that are released from the National Patch Module on Forum. It will not track Class III patches, test patches or hand-entered patches from other sources due to its link with the KIDS INSTALL file (#9.7).</p>
<p>Package support and management personnel have a various reporting programs they may use on a daily basis, as well as automatic daily options which report anything from past due to uninstalled patches.</p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](xt-7-3-98-vista-patch-monitor-supplement-to-patch-desc/025.png)</td>
<td><p>For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the ISS Glossary Web page at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/glossary.asp">http://vista.med.va.gov/iss/glossary.asp</a></p>
</blockquote>
<p>For a list of commonly used acronyms, please visit the ISS Acronyms Web site at the following Web address:</p>
<blockquote>
<p><a href="http://vista/med/va/gov/iss/acronyms/index.asp">http://vista/med/va/gov/iss/acronyms/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Acknowledgements
REDACTED, ix
Acronyms (ISS)
Home Page Web Address, Glossary, 4
Adobe
Home Page Web Address, xiii
Adobe Acrobat Quick Guide
Home Page Web Address, xiv
Anonymous Directories, xiv
Archiving, 5-15
B
Background Jobs
XTPM NIGHTLY PATCH MONITOR, 5-1
XTPM UNINSTALLED PATCH BULLETIN, 5-1
bulletin, 1-1
C
Callable Routines, 5-15
Class III patches, 1-1
complete a non-KIDS patch, 3-4
Complete Patch Installation History option
prompt description, 3-5
completed installation record
purged, 1-1
completed patches
data retention, 1-2
purged, 1-2
COMPLETED/UNRELEASED patches, 1-2
INSTALL file (#9.7), 1-2
completion date
purged, 1-1
compliance date, past, 1-1
Contents, v
D
Data Dictionaries
PATCH MONITOR (#9.9), 5-3
PATCH MONITOR PARAMETER (#9.95), 5-8
Data Dictionary, 1
Data Dictionary Utilities Menu, xiii
Listings, xiii
data retention, 2-7, 3-14
completed patches, 1-2
DATE INSTALLED (#9), 3-2
delete data, 2-7, 3-14
Documentation
History, iii
Symbols, xi
E
Edit Patch Information option
prompt descriptions, 3-3
Edit the Patch Monitor Parameter File option
prompt descriptions, 3-13
EN^XT73P98 routine
removes Class III, 2-3
EVS Anonymous Directories, xiv
External Interfaces, 5-15
External Relations, 5-16
F
Figures and Tables, vii
File Numbers, 5-17
File Security, 5-20
files
INSTALL (#9.7), 1-1, 1-2
PACKAGE (#9.4), 2-7
PATCH MONITOR (#9.9), 1-1, 1-2, 3-2, 3-5, 4-1, 5-3, 5-14, 5-15
PATCH MONITOR PARAMETER (#9.95), 1-2, 2-6, 3-10, 5-8, 5-15
FTP directories, xiv
G
G.PATCHES mail group, 1-1, 2-5, 5-16
Glossary, 1
Glossary (ISS)
Home Page Web Address, Glossary, 4
H
Help
At Prompts, xiii
Online, xiii
history, installation, 3-5
History, Revisions to Documentation and Patches, iii
Home Pages
Adobe Acrobat Quick Guide Home Page Web Address, xiv
Adobe Home Page Web Address, xiii
Health Systems Design and Development Web Address, xii
ISS Acronyms Home Page Web Address, Glossary, 4
ISS Glossary Home Page Web Address, Glossary, 4
VistA Documentation Library (VDL) Home Page Web Address, xiv
How to
Obtain Technical Information Online, xii
Use this Manual, xi
I
Implementation and Maintenance (Technical Manual Information), 5-1
Infrastructure & Security Services (ISS), ix
Input Templates
XTPM COMPLETE NON-KIDS PATCH, 5-15
XTPM EDIT PATCH, 5-15
XTPM EDIT PATCH MONITOR PARAMS, 5-15
INSTALL file (#9.7), 1-1
COMPLETED/UNRELEASED patches, 1-2
multiple test releases, 1-2
no installation date, 1-1
past compliance date, 1-1
test patches, 1-2
installation history, 3-5
\*\*INSTALL NAME\*\*, 1-1
Installation of Patch XT\*7.3\*98
Class III to Class I, 2-1
installation procedure, 2-3
Kernel Installation and Distribution (KIDS), 2-1
MERGE^XT73P98 routine, 2-3
Packman message, 2-1
Patch XT\*7.3\*98, 2-1
post-installation procedure, 2-4
pre-installation procedure, 2-1
Unschedule \[AWB NIGHTLY PATCH MONITOR\] and \[AWB UNINSTALLED PATCH BULLETIN\], 2-1
Unschedule Class III options, 2-1
INSTALLED BY (#10), 3-2
Internal Relations, 5-16
Introduction
Package Operation, 1-1
ISS Acronyms
Home Page Web Address, Glossary, 4
ISS Glossary
Home Page Web Address, Glossary, 4
K
Kernel Installation and Distribution (KIDS), 2-1
key, security, 5-19
KIDS patch, 1-1
no installation date, 1-1
L
List File Attributes Option, xiii
M
mail groups
delete AWB PATCH MONITOR, 2-5
delete AWB PATCH MONITOR USER, 2-5
G.PATCHES, 1-1, 2-5
MailMan, 1-1
remote user, 1-1, 5-16
S.XTPM PATCH SERVER, 1-1
server option, 1-1
set up XTPM PATCH MONITOR, 2-6
set up XTPM PATCH MONITOR USER, 2-6
XTPM PATCH MONITOR, 1-1, 5-16
XTPM PATCH MONITOR USER, 5-16
MailMan, 1-1, 4-1, 5-16
\*\*INSTALL NAME\*\*, 1-1
edit field extracted from message, 3-3
non-KIDS message, 1-1
PackMan message, 2-1
Mark a Non-KIDS Patch as Complete option
prompt descriptions, 3-4
Menu Diagram, 5-13
Menu Options, 3-1
menu text
Patch Monitor Main Menu, 3-1
Patch Monitor Management, 3-13
Edit the Patch Monitor Parameter File, 3-13
Rerun the Nightly Patch Monitor
locked with XTPM PATCH MONITOR MGR, 3-14
Patch Processing, 3-2
Edit Patch Information, 3-3
Mark a Non-KIDS Patch as Complete, 3-4
Patch Inquiry, 3-2
Patch Reports, 3-5
Complete Patch Installation History, 3-5
Past Due Patch Report, 3-9
Patch Statistics by Compliance Date, 3-11
Patch Statistics by Reporting Group, 3-10
Patches Due in the Next Seven Days, 3-8
Uninstalled Patch Listing - Alphabetical, 3-7
Uninstalled Patches by Compliance Date, 3-6
MERGE^XT73P98 routine, 2-3
multiple test releases
COMPLETED/UNRELEASED patches, 1-2
test patches, 1-2
N
Namespace, 5-16
National Patch Module, 1-1
"No Delinquent Patches were found" MailMan message, 2-9
non-KIDS patch, 1-1
complete, 3-4
completed manually, 4-1
message, 1-1
no completion date, 1-1
O
Online
Documentation, xiii
Help Frames, xiii
Technical Information, How to Obtain, xii
options
Data Dictionary Utilities, xiii
List File Attributes, xiii
S.XTPM PATCH SERVER, 1-1, 2-5, 4-1, 5-16
XTPM COMPLETE A NON-KIDS PATCH, 3-4, 5-11
XTPM COMPLETE PATCH HISTORY, 3-5, 5-11
XTPM EDIT PATCH, 3-3, 5-11
XTPM EDIT PATCH MONITOR PARAMS, 3-13, 5-11
XTPM NIGHTLY PATCH MONITOR, 5-11
XTPM PAST DUE PATCH REPORT, 3-9, 5-11
XTPM PATCH INQUIRY, 3-2, 5-11
XTPM PATCH MANAGEMENT, 3-13, 5-11
XTPM PATCH MONITOR MAIN MENU, 3-1, 5-11
XTPM PATCH PROCESSING, 3-2, 5-11
XTPM PATCH REPORTS, 3-5, 5-11
XTPM PATCH SERVER, 5-11
XTPM PATCH STATISTICS, 3-10, 5-11
XTPM PATCH STATS BY COMPLIANCE, 3-11, 5-12
XTPM PATCHES DUE NEXT 7 DAYS, 3-8, 5-12
XTPM RERUN NIGHTLY, 3-14, 5-12
XTPM UNINSTALLED BY COMPLIANCE, 3-6, 5-12
XTPM UNINSTALLED PATCH BULLETIN, 5-12
XTPM UNINSTALLED PATCHES, 3-7, 5-12
Orientation
conventions for displaying TEST data, xii
Data Dictionary
Listings, xiii
EVS Anonymous Directories, xiv
How to Use this Manual, xi
obtaining online technical info, xii
Symbols Found in the Documentation, xi
VistA Documentation, xiii
Who Should Read this Manual?, xii
P
PACKAGE file (#9.4), 2-7
Package Operation
G.PATCHES mail group, 1-1
remote user, 1-1
S.XTPM PATCH SERVER, 1-1
TaskMan, 1-1
PackMan message, 2-1
parameters, edit, 3-13
Past Due Patch Report option
prompt description, 3-9
past due patches, 1-1
patch history, 3-5
Patch History, iii
Patch Inquiry
prompt descriptions, 3-2
PATCH MONITOR file (#9.9), 1-1, 3-2, 3-5, 4-1, 5-3
COMPLETED/UNRELEASED patches, 1-2
Input Template, 5-15
no completion date, 1-1
Print Template, 5-14
purged patch record, 1-1
Sort Template, 5-14
test patches, 1-2
PATCH MONITOR PARAMETER file (#9.95), 3-10, 5-8
completed patches, 1-2
Input Template, 5-15
setup, 1-2
Patch Statistics by Compliance Date option
prompt descriptions, 3-11
Patch Statistics by Reporting Group option
prompt descriptions, 3-10
Patch XT\*7.3\*98, 2-1
Patches Due in the Next Seven Days option
prompt description, 3-8
patches not installed, 1-1
patient & user names
test data, xii
post-installation procedure
delete existing mail groups in AWB namespace, 2-5
EN^XT73P98 routine, 2-3, 2-4
G.PATCHES mail group, 2-5
PATCH MONITOR PARAMETER file (#9.95), 2-6
S.XTPM PATCH SERVER, 2-5
Sample, 2-9
Sample Uninstalled Patch Report MailMan message, 2-9
schedule Class I background jobs, 2-7
security key XTPM PATCH MONITOR MGR, 2-4
setup mail groups, 2-6
TaskMan, 2-7
XTPM NIGHTLY PATCH MONITOR, 2-8
XTPM PATCH MONITOR, 2-6
XTPM PATCH MONITOR MAIN MENU, 2-5
XTPM PATCH MONITOR MGR security key, 2-7
XTPM PATCH MONITOR USER, 2-6
XTPM UNINSTALLED PATCH BULLETI, 2-8
pre-installation procedure, 2-1
Print Templates
XTPM COMPLETE PATCH HISTORY, 5-14
XTPM UNINSTALLED BY COMPLIANCE, 5-14
Q
Question Mark Help, xiii
R
recover patches, 4-1
retain data, 2-7, 3-14
Revision History, iii
Routines, 5-2
S
Sample Uninstalled Patch Report MailMan message, 2-9
Scheduled Options
XTPM NIGHTLY PATCH MONITOR, 5-1
XTPM UNINSTALLED PATCH BULLETIN, 5-1
Security Key, 5-19
security key XTPM PATCH MONITOR MGR, 2-4, 2-7, 3-14
server option
S.XTPM PATCH SERVER, 2-5, 4-1, 5-16
server option S.XTPM PATCH SERVER, 1-1
Setting Up a New Installation or Recovering Patches, 4-1
seven days, patches due in, 3-8
Social Security Numbers
test data, xii
Software Dependencies, 5-1, 5-16
Software Security
Archiving, 5-19
Electronic Signatures, 5-19
File Security, 5-20
Interfaces, 5-19
Mail Groups, 5-19
Menus, 5-19
Remote Systems, 5-19
Security Key, 5-19
Software-wide Variables, 5-17
Sort Templates
XTPM COMPLETE PATCH HISTORY, 5-14
XTPM UNINSTALLED BY COMPLIANCE, 5-14
Symbols Found in the Documentation, xi
T
Tables and Figures, vii
TaskMan
completed installation record, 1-1
completion date, 1-1
INSTALL file (#9.7), 1-1
KIDS patch, 1-1
non-KIDS patch, 1-1
PATCH MONITOR file (#9.9), 1-1
patches not installed, 1-1
XTPM NIGHTLY PATCH MONITOR, 1-1
TaskMan setup
XTPM NIGHTLY PATCH MONITOR, 2-8
XTPM UNINSTALLED PATCH BULLETI, 2-8
test data
patient & user names, xii
Social Security Numbers, xii
test patches, 1-1
INSTALL file (#9.7), 1-2
PATCH MONITOR file (#9.9), 1-2
test sites, 1-2
test sites, 1-2
REDACTED, Acknowledgements, ix
tracking patches
Class III patches, 1-1
INSTALL file (#9.7), 1-1
National Patch Module, 1-1
test patches, 1-1
U
Uninstalled Patch Listing - Alphabetical option
prompt description, 3-7
uninstalled patches
by compliance date, 3-6
in alphabetical order, 3-7
Uninstalled Patches by Compliance Date option
prompt description, 3-6
Unschedule \[AWB NIGHTLY PATCH MONITOR\] and \[AWB UNINSTALLED PATCH BULLETIN\], 2-1
Unschedule Class III options, 2-1
URLs
Health Systems Design and Development Home Page Web Address, xii
V
Variables, 5-17
VistA Documentation Library (VDL)
Home Page Web Address, xiv
W
Web Pages
Adobe Acrobat Quick Guide Home Page Web Address, xiv
Adobe Home Page Web Address, xiii
Health Systems Design and Development Home Page Web Address, xii
ISS Acronyms Home Page Web Address, Glossary, 4
ISS Glossary Home Page Web Address, Glossary, 4
VistA Documentation Library (VDL) Home Page Web Address, xiv
Who Should Read this Manual?, xii
X
XT\*7.3\*98, 2-1
XTPM COMPLETE A NON-KIDS PATCH, 3-4, 5-11
prompt descriptions, 3-4
XTPM COMPLETE NON-KIDS PATCH Input Template, 5-15
XTPM COMPLETE PATCH HISTORY, 3-5, 5-11
prompt description, 3-5
XTPM COMPLETE PATCH HISTORY Print Template, 5-14
XTPM COMPLETE PATCH HISTORY Sort Template, 5-14
XTPM EDIT PATCH, 3-3, 5-11
prompt descriptions, 3-3
XTPM EDIT PATCH Input Template, 5-15
XTPM EDIT PATCH MONITOR PARAMS, 3-13, 5-11
XTPM EDIT PATCH MONITOR PARAMS Input Template, 5-15
XTPM EDIT PATCH MONITOR PARAMS option
prompt descriptions, 3-13
XTPM NIGHTLY PATCH MONITOR, 1-1, 2-8, 5-11
completed installation record, 1-1
completion date, 1-1
INSTALL file (#9.7), 1-1
KIDS patch, 1-1
non-KIDS patch, 1-1
PATCH MONITOR file (#9.9), 1-1
patches not installed, 1-1
XTPM PAST DUE PATCH REPORT, 3-9, 5-11
prompt description, 3-9
XTPM PATCH INQUIRY, 5-11
prompt descriptions, 3-2
XTPM PATCH MANAGEMENT, 3-13, 5-11
XTPM PATCH MONITOR
bulletin, 1-1
KIDS patch, 1-1
mail group, 1-1
past due patches, 1-1
XTPM PATCH MONITOR mail group, 5-16
XTPM PATCH MONITOR MAIN MENU, 3-1, 5-11
XTPM PATCH MONITOR MGR, 3-14
XTPM PATCH MONITOR USER mail group, 5-16
XTPM PATCH MONITOR USER, set up, 2-6
XTPM PATCH MONITOR, set up, 2-6
XTPM PATCH PROCESSING, 3-2, 5-11
XTPM PATCH REPORTS, 3-5, 5-11
XTPM PATCH SERVER, 5-11
XTPM PATCH STATISTICS, 3-10
prompt descriptions, 3-10
XTPM PATCH STATS BY COMPLIANCE, 3-11, 5-12
prompt descriptions, 3-11
XTPM PATCHES DUE NEXT 7 DAYS, 3-8, 5-12
prompt description, 3-8
XTPM RERUN NIGHTLY, 3-14, 5-12
XTPM UNINSTALLED BY COMPLIANCE, 3-6, 5-12
prompt description, 3-6
XTPM UNINSTALLED BY COMPLIANCE Print Template, 5-14
XTPM UNINSTALLED BY COMPLIANCE Sort Template, 5-14
XTPM UNINSTALLED PATCH BULLETI, 2-8
XTPM UNINSTALLED PATCH BULLETIN, 5-12
XTPM UNINSTALLED PATCHES, 3-7, 5-12
prompt description, 3-7
