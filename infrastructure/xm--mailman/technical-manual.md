---
title: MailMan Version 8 Technical Manual
doc_type: TM
doc_label: Technical Manual
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
file_numbers: 
  - 8930
security_keys: 
  - XUPROG
menu_options: 2
description: 
audience: 
keywords: 
  - blockquote
  - class
  - message
  - mailman
  - xmmgr
  - routine
  - messages
  - mail
  - strong
  - even
page_count: 0
word_count: 47192
section_count: 7
table_count: 184
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_techman.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_techman.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=15"
---

![](mailman-version-8-technical-manual/001.png)

MAILMANTechnical Manual

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
<td><p>MailMan Development Team Oakland, CA Office of Information Field Office (OIFO):</p>
<ul>
<li><blockquote>
<p>REDACTED, REDACTED, REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>09/28/06</td>
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
<p>REDACTED, REDACTED, REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>03/14/07</td>
<td>2.1</td>
<td>Updated MailMan global and file export lists.</td>
<td><p>MailMan Development Team Oakland, CA Office of Information Field Office (OIFO):</p>
<ul>
<li><blockquote>
<p>REDACTED, REDACTED</p>
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

[Figure 2‑6. Local Delivery Management \[XMMGR-MESSAGE-DELIVERY-MGT\] menu  
options [2-22](#_Toc161642803)](#_Toc161642803)

[Figure 5‑4. Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]  
options [5-29](#_Toc142203709)](#_Toc142203709)

[Figure 5‑5. Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]  
options [5-30](#_Toc142203710)](#_Toc142203710)

[Figure 5‑6. Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]  
options [5-32](#_Toc142203711)](#_Toc142203711)

[Figure 5‑7. Network Management menu \[XMNET\] options [5-38](#_Toc142203712)](#_Toc142203712)

[Figure 5‑8. Queue Management menu \[XMNET-QUEUE-MANAGEMENT\] options [5-38](#_Toc142203713)](#_Toc142203713)

[Figure 5‑9. Transmission Management menu \[XMNET-TRANSMISSION-MANAGEMENT\]  
options [5-39](#_Toc142203714)](#_Toc142203714)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This *MailMan Technical Manual* is intended for use in conjunction with Veterans Health Information Systems and Technology Architecture (VistA) MailMan. It outlines the technical aspects (e.g., files, fields, routines, options, security keys, etc.) and system implementation and maintenance guidelines for the VistA MailMan software and gives guidelines on how the software is used within VistA.

The intended audience of this manual is all primary (key) stakeholders. The primary stakeholders include:

- VistA Infrastructure and Security Services (ISS) Development Team.
- Other VistA project development teams and programmers.
- Information Resource Management (IRM) personnel responsible for installing, implementing, and maintaining MailMan.
- Enterprise VistA Support (EVS).

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of MailMan V. 8.0 and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products. This manual discusses the use of electronic network communication software and covers network features for sending and receiving transmissions, responding, and transmitting mail. Many user actions are available for completing specific tasks.

There are no special legal requirements involved in the use of MailMan.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                |                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                     | Description                                                                                                     |
| ![](mailman-version-8-technical-manual/002.png) | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](mailman-version-8-technical-manual/003.png)                                                              | CAUTION or DISCLAIMER: Used to inform the reader to take special notice of critical information.                |

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
| ![](mailman-version-8-technical-manual/004.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

|                                                                                                                |                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/005.png) | NOTE: Unless otherwise noted, all sample screen captures/dialogue boxes in this manual are derived from using either MailMan's Detailed or Summary Full Screen message readers. |

- This manual refers in many places to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the M programming language, and M will be considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

How to Obtain Technical Information Online

Exported VistA M Server-based file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/006.png) | NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of the software.

In addition to the "question mark" help, you can use the Help (User/Group Info., etc.) menu \[XMHELP\] on the main MailMan Menu to access the MailMan Help Frames through the following options:

- New Features in MailMan
- General MailMan Information
- Questions and Answers on MailMan
- Manual for MailMan Users

|                                                                                                                |                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/007.png) | REF: For more information on obtaining MailMan online help, please refer to Chapter 12, "Online Help Information" in the *MailMan User Guide*. |

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/008.png) | REF: For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" topic of the *VA FileMan Advanced User Guide*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language

This manual provides an overall explanation of MailMan and the changes contained in MailMan V. 8.0. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) and VA Intranet for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following Intranet Web address:

> <http://vista.med.va.gov/>

Reference Materials

Readers who wish to learn more about MailMan should consult the following:

- *MailMan Release Notes*
- *MailMan Installation Guide*
- *MailMan Getting Started Guide*
- *MailMan Developer's Guide*
- *MailMan User Guide*
- *MailMan Network Reference Guide*
- *MailMan Package Security Guide*
- *MailMan Systems Management Guide*
- *MailMan Technical Manual* (this manual)
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
<td>![](mailman-version-8-technical-manual/009.png)</td>
<td><p><strong>REF:</strong> For more information on the use of the Adobe Acrobat Reader, please refer to the "Adobe Acrobat Quick Guide" at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">http://vista.med.va.gov/iss/acrobat/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

VistA documentation can be downloaded from the Health Systems Design and Development (HSD&D) Veterans Health Administration (VHA) Documentation Library (VDL) Web site:

> <http://www.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Enterprise VistA Support (EVS) anonymous directories:

- Preferred Method REDACTED

> This method transmits the files from the first available FTP server.

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/010.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [Orientation](#orientation)
- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
    - [Implementation](#implementation)
    - [Maintenance](#maintenance)
    - [Managing MailMan](#managing-mailman)
- [Routines](#routines)
- [Files](#files)
    - [Globals](#globals)
    - [Files](#files-1)
- [Exported Options](#exported-options)
    - [Menu Diagram](#menu-diagram)
    - [Options—Without Parents](#optionswithout-parents)
    - [Options—Listed Alphabetically by Name](#optionslisted-alphabetically-by-name)
- [Archiving and Purging](#archiving-and-purging)
    - [Archiving](#archiving)
    - [Purging](#purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
    - [Integration Agreements (IA<span class="smallcaps">s)</span>](#integration-agreements-iaspan-classsmallcapssspan)
- [Internal Relations](#internal-relations)
    - [Namespace](#namespace)
    - [File Numbers](#file-numbers)
    - [Pointer Relationships](#pointer-relationships)
    - [Templates](#templates)
    - [Help Frames](#help-frames)
- [Software-wide Variables](#software-wide-variables)
    - [Standards and Conventions (SAC) Exemptions](#standards-and-conventions-sac-exemptions)
- [Software Product Security](#software-product-security)
    - [Mail Groups and Alerts](#mail-groups-and-alerts)
    - [Remote Systems](#remote-systems)
    - [Archiving and Purging](#archiving-and-purging-1)
    - [Interfacing](#interfacing)
    - [Electronic Signatures](#electronic-signatures)
    - [Menus/Options](#menusoptions)
    - [Security Keys](#security-keys)
    - [File Security](#file-security)
    - [References](#references)
    - [Official Policies](#official-policies)
  - [Glossary](#glossary)
  - [Appendix A—Help Frames](#appendix-ahelp-frames)
  - [Index](#index)
This manual provides descriptive information and instructions on the implementation and maintenance of the MailMan software within the VA's Veterans Health Information Systems and Technology Architecture (VistA) environment. This document is intended for systems managers—Information Resource Management (IRM) personnel who are responsible for implementing and maintaining MailMan, application programmers, and developers. It acquaints system managers with the utilities, software structure, and functionality of the MailMan system modules, including information about the routines and files that comprise MailMan. It also has information about MailMan's structure and recommendations regarding MailMan's efficient use (e.g., routine mapping). However, it does *not* describe how MailMan is used nor does it detail its use in software development. Additional information on installation, security, management features, and other requirements is also included specifically related to VistA application Programmers and IRM.
MailMan, the Department of Veterans Affairs (VA) electronic mail system, is a communications tool that provides electronic communication among users sharing computing facilities. A communications link can be made with cables, telephone lines, or satellite connections. In this manner, the networking of electronic mail on a large scale is made possible.
MailMan provides teleconferencing via chained responses. MailMan is the transport vehicle for most Veterans Health Information Systems and Technology Architecture (VistA) applications. MailMan is also used to preserve copies of software and data. MailMan also has the ability to include non-textual data in messages (i.e., Multimedia). Network features allow users to construct dialogues for logging onto remote systems for mail delivery. Message actions allow users great flexibility in managing personal mail. Users can address mail to individuals and groups at local and remote sites, with the tedium of waiting for process completion being reduced by the system's background filer. In addition, the system has extensive online documentation, which can be printed to create a manual.
MailMan is designed to allow users to send and receive mail from individuals or groups. A message can take the form of a personal letter or a formal bulletin extracting data from VA FileMan. The text of messages is not difficult to edit, and the context can be made confidential in several ways. Surrogates can be appointed to read mail. Mail groups can be set up to allow each member to respond to a message and to view the replies, as in an informal committee meeting. Mail can be sorted, deleted, forwarded, queried, copied, revised, or printed. In addition, MailMan cross-references messages by subject and message number.
MailMan allows users to send, receive, copy, respond to, and organize electronic mail. It has entry points to allow other applications to trigger bulletins or send messages without user intervention. There is a communications facility (i.e., TalkMan) to allow users to automatically hook into the VA Wide Area Network (WAN) or modems. This feature connects the user to a remote domain, playing the script to that domain without displaying it to the user. It then informs the user that the connection was successful, and can capture whatever has been displayed to the user's terminal into a message called DIALOGUE CAPTURE.
An extended search for messages can be invoked at the "Message Action" prompt or as a stand-alone option. The extended search includes filters on the subject, sender, recipient, responder, the date sent, and text contents.
MailMan informs users of network delivery failures and their causes. Message characteristics including Closed, Confidential, Confirmation Requests, Information, and Scrambling can be carried across the network. Software security information for PackMan can also be conveyed on the network.
MailMan allows the transfer of any word-processing text from any VA FileMan file or message into a message or response. New documents are placed in a user's "IN" basket or to any other designated basket (e.g., based on mail filters).
This manual provides information on the following topics:
- Implementation and Maintenance
- MailMan site parameters
- System manager menus and options
- Routines
- Files
- Exported Options
- Archiving and Purging
- Callable Routines
- External Relations
- Internal Relations
- Software-wide Variables
- Software Product Security
These sections provide pertinent information, along with examples, that allow system managers and programmers to effectively implement, support, and maintain MailMan Version 8.0.
|                                                                                                                |                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/011.png) | REF: For more information on MailMan system management, please refer to the *MailMan Systems Management Guide*. |

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Recommendations for Routine Mapping

Routine mapping is at the discretion of the systems manager. The RTHIST routines provide a method for each site to determine the extent to which certain routines are utilized.

DSM Sites: If your site maps routines, then rebuild your map set. As of MailMan V. 8.0, Many routines have become obsolete and should be removed from the map set. The following is the *recommended* list of routines to map, should your site choose to map routines:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Minimum List</strong></td>
<td><strong>Additional List</strong></td>
</tr>
<tr class="even">
<td>XM<br />
XMC1<br />
XMJ*<br />
XMR<br />
XMS</td>
<td>XMC1A,XMC1B<br />
XMK*<br />
XML<br />
XMR1,XMR2,XMR3*<br />
XMS1,XMS2,XMS3<br />
XMT*<br />
XMVVITAE<br />
XMXADDR*<br />
XMXSEC*<br />
XMXUTIL*</td>
</tr>
</tbody>
</table>

<span id="_Toc161642791" class="anchor"></span>Table 2‑1. Routine mapping recommendations for MailMan V. 8.0

#### Controlled Procedures

All files, fields, and routines in this software are considered to perform controlled procedures and *cannot* be modified.

#### Menu Structure

MailMan is accessed from three sets of menus:

- XMMGR—The Manage Mailman menu includes options and utilities that are useful for system management. The options for maintaining the local mail system are also contained here.

|                                                                                                                |                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/012.png) | REF: For more information on the XMMGR menu options, please refer to the "Managing MailMan" topic that follows in this section of the manual. |

- XMNET—This menu includes options that are used for managing the network side of MailMan. While the local system requires only some initial setup, the network side must be periodically monitored. The options for displaying the queues in various fashions on the XMNET menu are useful for this purpose. The network sometimes needs to be flushed; options for polling and queuing are provided for this purpose. Sometimes, non-delivery of network mail requires investigation; the options for testing a network device and playing scripts are useful in these instances.

|                                                                                                                |                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/013.png) | REF: For more information on the XMNET menu options, please refer to the *MailMan Network Management Reference Guide*. |

- XMUSER—This menu includes the commonly used functions of electronic mail. It also contains some very powerful tools for the individual using MailMan. The most commonly used functions are at the top of the hierarchical structure. Help features are contained in a separate submenu, as are the tools. XMUSER can be used independently and can be installed on menus of other software applications for distribution.

|                                                                                                                |                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/014.png) | REF: For more information on the XMUSER menu options, please refer to the *MailMan Getting Started Guide* and the *MailMan User Guide*. |

|                                                                                                                |                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/015.png) | REF: In order to acquire a good idea of the various functions and their power, users should also consult the *MailMan Developer's Guide*. In addition, online Help Frames are also available. |

#### Postmaster

The MailMan installation automatically creates a special user (DUZ=.5) called Postmaster and Postmaster mail baskets. Persons assigned to the management of MailMan and Network mail at a site *must* be entered in the MAILBOX file (#3.7) as surrogates of the Postmaster and given READ and WRITE access privileges.

|                                                                                                                |                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/016.png) | REF: For more information on the management and maintenance of the Postmaster, please refer to the "Postmaster" topic under the "Maintenance" topic that follows in this chapter. |

#### Memory Constraints

There are no special memory constraints, other than sites having sufficient space to allow for normal global growth.

#### Special Operations

MailMan V. 8.0 does not require any special operations other than the normal backup and recovery operations.

### Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### System Maintenance

There are several ways to keep the amount of messages stored at a minimum. MailMan provides the Disk Space Management menu options for this purpose under the Manage MailMan main menu.

#### Disk Space Management

What areas in MailMan can be investigated to improve disk space management?

1\. The tools available to IRM to help manage disk space are located under the Disk Space Management menu option \[XMMGR-DISK-SPACE-MANAGEMENT\], which is located on the Manage Mailman menu \[XMMGR\], as shown below:

> Select Manage Mailman Option: Disk Space Management

> AI x-Ref Purge of Received Network Messages

> Ask users with many messages to do maintenance

> Clean out waste baskets

> IN Basket Purge

> Large Message Report

> Message statistics

> Purge a message

> Purge Messages by Origination Date

> Purge Unreferenced Messages

> Recover Messages into User's IN Basket ...

> Terminate mail user suggestions

> Terminate many mail users

> Terminate one mail user

> Select Disk Space Management Option:

<span id="_Toc141000961" class="anchor"></span>Figure 2‑1. Disk Space Management menu options

> The following describes the Disk Space Management tools (options).

|                                                                                                                |                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/017.png) | REF: For more information on the following options, please refer to the "Options—Listed Alphabetically by Name" topic in Chapter 5, "Exported Options," in this manual or the individual option descriptions in the OPTION file (#19). |

> a\. AI x-Ref Purge of Received Network Messages option \[XMMGR-PURGE-AI-XREF\]—The AI cross-reference exists to track messages received from remote sites. It is used to attach replies from remote sites to the correct local message. It prevents the receipt of duplicate messages from remote sites. There is one entry per message. As per MailMan Patch XM\*8.0\*38, this option should be run interactively at least once a year to reduce its size; otherwise, it continues to grow.

> b\. Ask users with many messages to do maintenance option \[XMMGR-DISK-MANY-MESSAGE-MAINT\]—This option looks for users with lots of messages in their mailbox and sends them a message suggesting that they might want to consider pruning some of them. Some users might not respond to the suggestion, but others might. This option should be scheduled to run every few months if disk space is a problem.

> c\. Clean out waste baskets option \[XMCLEAN\]—This option deletes messages from users' wastebaskets. This option should be scheduled to run every day, before the XMAUTOPURGE option.

> d\. IN Basket Purge option \[XMMGR-IN-BASKET-PURGE\]—This option targets for later deletion, messages that have not been read in a while. It targets messages in the "IN" basket or in all baskets, depending on how it's run. Users receive a message with a list of the messages that are targeted for deletion, and what they can do to avoid deletion. This option should be scheduled to run once a month if disk space is a problem.

> e\. Large Message Report option \[XMMGR-LARGE-MESSAGE-REPORT\]—This option reports on large (over a certain number of lines) messages. It does not say who owns them, just says that they exist. This option should be used on an as-needed basis if disk space is a problem. Its effectiveness depends upon the zeal with which IRM uses the report to investigate and purge large unnecessary messages.

> f\. Message statistics option \[XMSTAT\]—This option reports how many messages each user has in his mailbox. This option should be used on an as-needed basis if disk space is a problem. Its effectiveness depends upon the zeal with which IRM uses the report to confront message hoarders and encourage them to prune their messages.

> g\. Purge a message option \[XMMGR-PURGE-MESSAGE\]—This option purges one message. Can be used to purge offensive messages or large messages identified by the 'Large Message Report'. This option should be used on an as-needed basis.

> h\. Purge Messages by Origination Date option \[XMPURGE-BY-DATE\]—This option purges messages older than a certain date. This option should be used on an as-needed basis if disk space is a problem. This option is extremely effective in reducing the size of the MESSAGE file (#3.9).

> i\. Purge Unreferenced Messages option \[XMPURGE\]——This option purges messages that are not in anyone's mailbox. This option may be run interactively, but it should not be scheduled.

> j\. Automatic Purge of MailMan Messages option \[XMAUTOPURGE\]——This option automatically purges unreferenced MailMan. It deletes from the MESSAGE file (#3.9) any messages that are not in anyone's basket.

|                                                   |                                                                                                               |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/018.png) | CAUTION: It is *strongly* recommended that this option be scheduled to run daily, right after option XMCLEAN. |

|                                                                                                                |                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| ![](mailman-version-8-technical-manual/019.png) | NOTE: This option is not located on any menu. |

|                                                                                                                |                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/020.png) | REF: For more information on this option, please refer to the "XMAUTOPURGE" topic in Chapter 5, "Exported Options," in this manual. |

> k\. Terminate mail user suggestions option \[XMMGR-TERMINATE-SUGGEST\]—This option reports on users who *perhaps* should have their mail access terminated. Users are included in the report if they were terminated but allowed to keep their mailbox, or have not signed on in a while. This option should be run at least once a year. This report will probably turn up many users who should not have mailboxes. It is likely that these users have new messages. New messages are only deleted by the 'Purge Messages by Origination Date' option. The report page-breaks on Service/Section. If sites regularly ran this report and gave service/section heads the part of the report applicable to their service/section, it is expected that users (and their many messages) would be identified for deletion.

> l\. Terminate many mail users option \[XMMGR-TERMINATE-MANY\]—This option goes through the MAILBOX global and removes any mailbox if the user:

- Is not in the NEW PERSON file (#200).
- Has no Access code and was not terminated.
- Has no Access code and was terminated without mailbox retention.
- Has an access code, but no primary menu.
- Has an Access code and primary menu, but no Verify code, AND:
- Has never signed on or used mail since being added before a cutoff date.  
  >   
  > OR
- Last signed on or used mail before a cutoff date.

> However, if the user meets one of the last two conditions above, but has a forwarding address, the user's mailbox will not be removed. The fact will be noted on the report, and the user should be investigated further.

> m\. Terminate one mail user option \[XMMGR-TERMINATE-ONE\]—This option manually terminates users suggested by the Terminate mail user suggestions option or otherwise. This option should be used on an as-needed basis.

> n\. Check MailMan Files for Errors option \[XMUT-CHKFIL\]—This option checks both the MAILBOX file (#3.7) and MESSAGE file (#3.9) for errors and fixes most errors that it finds. This option should be scheduled to run once a month, on a weekend, at a time when neither the XMCLEAN nor XMAUTOPURGE options are running.

2\. From time-to-time, a Remedy ticket will be entered on MailMan complaining about the number of messages in a server basket. Such complaints are always referred to the VistA software application that "owns" the server. The software that owns the server is responsible for deleting messages from its server basket, because there is no way for MailMan to know when a server message has been processed and is no longer needed. Anyone interested in checking whether a software application is cleaning up after itself should assume the identity of the Postmaster, and list the contents of baskets beginning with "S." By looking at the dates and/or quantity of the messages, one should be able to tell whether the software owning the server is cleaning up after itself.

3\. Are there other areas of MailMan that should be considered when trying to reduce the size of globals? Here are some ideas:

> a\. Perform a VA FileMan search to identify mail groups that have not been used in a while. The DATE 'LAST REFERENCED' field can be used for this purpose. Consider deleting them.

> b\. Messages belonging to SHARED,MAIL are never deleted by MailMan. All of the purges ignore them. It is probably a good idea to go through the messages belonging to SHARED,MAIL once a year to delete the ones which are no longer needed. However, this is easier said than done!

The following tables show mandatory and suggested system management tasks for proper maintenance of MailMan. These tasks increase utilization of software functionality and system response time. They also reduce the amount of disk space used and minimize system errors.

#### Mandatory Task Requirements

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 34%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task</strong></p>
</blockquote></th>
<th><strong>Scheduled Time</strong></th>
<th><strong>Frequency</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>XMCLEAN</p>
</blockquote></td>
<td>Off Hours</td>
<td>Daily</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMAUTOPURGE</p>
</blockquote></td>
<td>One Hour After XMCLEAN</td>
<td>Daily</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMUT-CHKFIL</p>
</blockquote></td>
<td>Off Hours</td>
<td>Monthly</td>
</tr>
</tbody>
</table>

<span id="_Toc161642793" class="anchor"></span>Table 2‑2. Task requirements: Mandatory maintenance timetable

The XMAUTOPURGE option is generally run after the XMCLEAN option (the "WASTE" basket cleaner) for automatic purging (see the XMAUTOPURGE option). It purges messages that are not pointed to by any message recipients or senders. The XMPURGE-BY-DATE option can also be run to purge messages that have an origination date older than the date used to initiate the process (see the XMAUTOPURGE option). Users are notified by a Postmaster bulletin of the proposed purging date, so that they can save important messages. These are the only options that actually KILL entries in the MESSAGE file (#3.9).

#### Suggested Task Requirements

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 34%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task</strong></p>
</blockquote></th>
<th><strong>Scheduled Time</strong></th>
<th><strong>Frequency</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>XMPURGE-BY-DATE</p>
</blockquote></td>
<td>Off Hours</td>
<td>According to Site Policy</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMMGR-LARGE-MESSAGE-REPORT</p>
</blockquote></td>
<td>Off Hours</td>
<td>Monthly</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMMGR-DISK-MANY-MESSAGE-MAINT</p>
</blockquote></td>
<td>Off Hours</td>
<td>Monthly</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMMGR-PURGE-AI-XREF</p>
</blockquote></td>
<td>Off Hours</td>
<td>Quarterly</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMMGR-RESPONSE-TIME-COMPILER</p>
</blockquote></td>
<td>Off Hours</td>
<td>Daily</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMMGR-RESPONSE-TIME-TOGGLER</p>
</blockquote></td>
<td></td>
<td>Daily</td>
</tr>
</tbody>
</table>

<span id="_Toc161642794" class="anchor"></span>Table 2‑3. Task requirements: Suggested maintenance timetable

#### Postmaster

Persons performing Postmaster management tasks should first sign on as themselves and then assume the Postmaster's identity.

- Mail Baskets—The Postmaster has mail baskets and can send and receive messages like any other user. In addition to the "IN" and "WASTE" baskets, the "ARRIVING" basket is also automatically created for the Postmaster. All mail for a site automatically comes to the "ARRIVING" basket from which it is then routed to the individual recipients. The Postmaster can examine the header information of messages but *cannot* read the text of the message.
- Network Transmission Failures—Network transmission failures are reported to the Postmaster via bulletins to the Postmaster's "IN" basket. These bulletins should be purged once the problems have been resolved.
- Domain Baskets—The Postmaster has special Domain baskets (e.g., Birmingham, Oakland, etc.), which are numbered greater than 1000 (1000 + IEN of the Domain in the DOMAIN file \[#4.2\]) and are used for the transmission of Network Mail. Network Mail to a site goes to the appropriate Domain basket (queue) prior to transmission. Occasionally, the Postmaster may need to stop networked message from going out. This is done by:

> 1\. Deleting the message number from the Postmaster's Domain basket. If a message is deleted from a basket, it is deleted from a queue.

> 2\. Using TaskMan to kill the job scheduled to transmit the message to the Domain.

- Broadcast Messages—The Postmaster also may need to broadcast messages to users. To do this:

> 1\. Send the message to the Postmaster.

> 2\. Assume the identity of the Postmaster.

> 3\. Copy the message into a new message and edit any information that is not appropriate for broadcasting.

> 4\. At the "Send to:" prompt, enter an asterisk ("\*").

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-technical-manual/021.png)</td>
<td><strong>NOTE:</strong> The XMSTAR security key gives users the ability to broadcast messages to all local mail users by entering an asterisk ("<strong>*</strong>") at the "Send to:" prompt.<br />
<br />
The XMSTAR LIMITED security key gives users the ability to broadcast messages to a subset of local mail users by entering an asterisk ("<strong>*</strong>") at the "Send to:" prompt.</td>
</tr>
</tbody>
</table>

#### Bulletins

MailMan V. 8.0 generates the following Bulletins.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Bulletin</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XM BANNER MESSAGE</td>
<td>This bulletin is a notification message. It might be generated when a user changes his banner.</td>
</tr>
<tr class="even">
<td>XM DATE PURGE WARNING</td>
<td>This bulletin is a warning message. It is broadcast to all users whenever the XMPURGE-BY-DATE option is used to purge messages older than a certain date.</td>
</tr>
<tr class="odd">
<td>XM DOMAIN ADDED</td>
<td>This bulletin is a notification message. It is sent to alert IRM of a new domain.</td>
</tr>
<tr class="even">
<td>XM FILTER FWD ADDRESS DELETE</td>
<td>This bulletin is a notification message. It is sent when MailMan notices that a user has an invalid "forward to" address in one of the filters. The "forward to" address is deleted, and the user is notified.</td>
</tr>
<tr class="odd">
<td>XM FWD ADDRESS CHANGE</td>
<td>This bulletin is a notification message. It is generated when a user's forwarding address changes. It should be sent to IRM or anyone with a need to know about a user's forwarding address.</td>
</tr>
<tr class="even">
<td>XM FWD ADDRESS CHECK</td>
<td>This bulletin is a notification message. It is sent when a user's forwarding address changes. It is sent to the forwarding address. If it gets through, fine. If it does not, then the sender of the bulletin is notified. The sender is the Postmaster. Field #7.01 in the MAILMAN SITE PARAMETERS file (#4.3) controls whether the message is also sent to the Postmaster.</td>
</tr>
<tr class="odd">
<td>XM FWD ADDRESS DELETE</td>
<td>This bulletin is a notification message. It is sent when MailMan notices that a user has an invalid forwarding address. The forwarding address is deleted, and the user is notified.</td>
</tr>
<tr class="even">
<td>XM GROUP EDIT NOTIFY</td>
<td><p>This bulletin is a notification message. It is sent to a mail group's organizer and coordinator whenever someone other than themselves adds users to:</p>
<ul>
<li><blockquote>
<p>A public mail group that does not allow users to self-enroll.</p>
</blockquote></li>
<li><blockquote>
<p>Any private mail group.</p>
</blockquote></li>
</ul>
<p>The purpose is to let them know of the change.</p></td>
</tr>
<tr class="odd">
<td>XM GROUP ERROR</td>
<td><p>This bulletin is an error message. It notifies selected users of problems with a mail group. For example, such problems may include:</p>
<ul>
<li><p>Group contains a circular reference to a group.</p></li>
<li><p>Local member should not be receiving mail (no access code).</p></li>
<li><p>Remote member has invalid or ambiguous or closed domain.</p></li>
<li><p>Distribution list domain is invalid or ambiguous or closed.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XM IN BASKET PURGE REQUEST</td>
<td>This bulletin is a notification message. It is sent by TEST^XMUPIN.</td>
</tr>
<tr class="odd">
<td>XM IN BASKET PURGE WARNING</td>
<td>This bulletin is a warning message sent by the XMMGR-IN-BASKET-PURGE option.</td>
</tr>
<tr class="even">
<td>XM RELAY ATTEMPTED</td>
<td><p>This bullet is a warning message sent to the Postmaster any time MailMan refuses to relay a message from one outside site to another outside site. You are encouraged to add a mail group to the bulletin to notify additional responsible persons. The subject of the bulletin is "Potential SPAM or VIRUS stopped." The actual bulletin MESSAGE TEXT is as follows:</p>
<blockquote>
<p>A site calling itself |1| attempted to relay a message from: |3| to: |2| through this site.</p>
<p>This attempt was denied.</p>
<p>By far the most important thing that a service provider can do to reduce spam or viruses is to ensure that any mail servers in operation accept only outgoing mail from machines within their own domains. This prohibits SMTP relaying, denying spammers and virus propagators a necessary component of anonymity.</p>
</blockquote>
<ul>
<li><blockquote>
<p>PARAMETER: 1—The name of the site attempting to relay the message through this site.</p>
</blockquote></li>
<li><blockquote>
<p>PARAMETER: 2—The intended recipient of the message.</p>
</blockquote></li>
<li><blockquote>
<p>PARAMETER: 3—The envelope from of the message.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>XM SEND ERR MSG</td>
<td>This bulletin is a notification message. It is sent to the message originator when a remote site rejects an entire message for whatever reason (e.g., too many lines).</td>
</tr>
<tr class="even">
<td>XM SEND ERR RECIPIENT</td>
<td>This bulletin is an error message. The MailMan network processor issues this bulletin when the remote node rejects a message recipient. The rejection message of the remote node is included in the bulletin.</td>
</tr>
<tr class="odd">
<td>XM SEND ERR REMOTE MSG ID</td>
<td>This bulletin is an error message. It is sent when a remote message ID node is not in a message (i.e., INCOMING MESSAGE ID field [#9] in the MESSAGE file [#3.9]). For example, while trying to send a response to a message that originated from a remote site, we noticed that the "remote message id" is missing from the original message. Without this ID, we cannot tell the site to which message we are responding.</td>
</tr>
<tr class="even">
<td>XM SEND ERR SERVER MSG</td>
<td>This bulletin is an error message. It is fired when a task tries to send a message to a server, but the message is not in the MESSAGE global.</td>
</tr>
<tr class="odd">
<td>XM SEND ERR TRANSMISSION</td>
<td>This bulletin is an error message. It is sent when MailMan is unable to transmit to a site after it has tried all of the available scripts.</td>
</tr>
<tr class="even">
<td>XM SUPER SEARCH</td>
<td><p>This bulletin is a notification message. Every time a super search is conducted, this bulletin is sent to alert those responsible for ensuring that the capability is <em>not</em> misused.</p>
<p>![](mailman-version-8-technical-manual/022.png) <strong>REF:</strong> For more information on the Super Search functionality, please refer to the XM SUPER SEARCH option in the "Options—" topic in this chapter.</p></td>
</tr>
<tr class="odd">
<td>XM TOO MANY MESSAGES</td>
<td>This bulletin is a notification message. It is sent by the XMMGR-DISK-MANY-MESSAGE-MAINT option to ask users to terminate excess messages.</td>
</tr>
<tr class="even">
<td>XMNEWUSER</td>
<td>This bulletin is a notification message. It is sent whenever a new user is added to the NEW PERSON file (#200). This bulletin is used by Kernel, <em>not</em> by MailMan.</td>
</tr>
<tr class="odd">
<td>XMRDACK</td>
<td>This bulletin is a notification message. It informs the sender of a message that a recipient has read the message. The sender of the message must have set the CONFIRMATION REQUESTED flag to ON when the message was created.</td>
</tr>
<tr class="even">
<td>XMVALBAD</td>
<td>This bulletin is a notification message. It is fired whenever a remote MailMan domain attempts to establish a connection with this domain and the validation numbers do not properly match.</td>
</tr>
<tr class="odd">
<td>XM_TRANSMISSION_ERROR</td>
<td>This bulletin is an error message. It is fired off when the background delivery process detects an error. The message or response it is supposed to deliver does not exist. MailMan just moves on to the next message.</td>
</tr>
</tbody>
</table>

<span id="_Toc161642795" class="anchor"></span>Table 2‑4. Bulletins exported with MailMan V. 8.0

|                                                                                                                |                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/023.png) | NOTE: Bulletins will be set to vaporize based on the number of retention days indicated in the RETENTION DAYS Field (#5) in the BULLETIN file (#3.6) from the date the bulletin was sent. |

### Managing MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Management Features in MailMan V. 8.0

This topic describes the various maintenance requirements, technical solutions, and the following improvements introduced with MailMan V. 8.0.

This information is directed mainly at the site's Information Resource Management (IRM) personnel.

#### MailMan V. 8.0 is DNS-Aware

MailMan V. 8.0 is now DNS-Aware. It uses Kernel's MAIL^XLFNSLK API to retrieve IP addresses. Thus, it is no longer necessary to manually update the IP addresses in the DOMAIN file (#4.2). The IP address fields still remain in the DOMAIN file (#4.2) and MailMan continues to use them. However, if they do not work, MailMan uses the Kernel API to retrieve a list of valid IP addresses. When MailMan finds one that works, MailMan replaces the non-working IP address with the working one.

In order to activate DNS awareness, the new DNS AWARE field (#8.22) in the MAILMAN SITE PARAMETERS file (#4.3) must be set to Yes.

Also, routine ^XLFNSLK must exist, and the DNS IP field (#51) in the KERNEL SYSTEM PARAMETERS file (#8989.3) must be properly filled in with an IP address.

#### Transmission Scripts and TCP/IP Connections

For TCP/IP connections, MailMan can now build transmission scripts on the fly. For transmission scripts whose TYPE is "SMTP," "TCPCHAN," or null, if the transmission script has no records (in the TEXT field \[#2\], in the TRANSMISSION SCRIPT multiple) in the DOMAIN file (#4.2), MailMan creates the script if the following new fields in the MAILMAN SITE PARAMETERS file (#4.3) are filled in:

- TCP/IP COMMUNICATIONS PROTOCOL (#8.23)—MailMan uses this field to determine which protocol shall be used for TCP/IP. It points to the COMMUNICATIONS PROTOCOL file (#3.4).
- TCP/IP TRANSMISSION SCRIPT (#8.24)—MailMan uses this field to determine which script shall be used for TCP/IP. It points to the TRANSMISSION SCRIPT file (#4.6).

#### Transmission Priority Flexibility

Messages in transmit queues can now be designated as low priority, as well as high priority. If a message gets stuck in a transmit queue and is holding up the rest of the queue for whatever reason, MailMan will make that message a low priority message, so that all the other messages are transmitted ahead of it. The Postmaster can also make these priority changes. In the message queue, high-priority messages are now marked with "^", instead of "\$". Low priority messages are marked with "v". The Postmaster can now change the transmit priority at the message level (at the "Message action: Ignore//" prompt). As at the basket level, the command to use is "X".

|                                                   |                                                                                                                                                                                                                                                                      |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/024.png) | CAUTION: In a user basket, the "X" at the message level is a command to unload a PackMan message or KIDS build. In a remote transmit queue, the "X" changes the transmit priority. The difference is the context, and writers of MailMan front-ends should take note |

#### Reformatted Date/Times

MailMan date/times are now in a standard format, produced by Kernel's \$\$FMTE^XLFDT(datetime,"2Z") API. This call is a Supported IA. For example:

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 40%" />
<col style="width: 40%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><br />
Date/Time Data</strong></td>
<td><strong>MailMan V. 7.1 Date/Time Format<br />
(Old)</strong></td>
<td><strong>MailMan V. 8.0 Date/Time Format (New)</strong></td>
</tr>
<tr class="even">
<td>3020803.153204</td>
<td>03 Aug 02 15:32</td>
<td>08/03/02@15:32</td>
</tr>
</tbody>
</table>

<span id="_Toc161642796" class="anchor"></span>Table 2‑5. MailMan V. 8.0: New date/time format

This change is also carried through to all MailMan APIs that return date/time in MailMan format.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-technical-manual/025.png)</td>
<td><p><strong>REF:</strong> For more information on this Kernel API, please refer to the $$FMTE^XLFDT Home Page at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/kernel/apis/x-fmte%5exlfdt.asp">http://vista.med.va.gov/kernel/apis/x-fmte^xlfdt.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/026.png) | REF: For information on how to obtain a list of Integration Agreements (IAs) related to MailMan, please refer to the "Integration Agreements (IA<span class="smallcaps">s)</span>" topic in Chapter 8, "External Relations," in this manual. |

#### Reformatted Remote Message IDs

MailMan remote message IDs now include the message date, to ensure that if you are told that a message is a duplicate of a previously received message, it really is. Sites will no longer have problems sending messages from a production account to a test account that was created by "mirroring" the production account. The remote message ID is now the message number followed by a period, followed by the 7-digit VA FileMan message creation date. For example:

|                                            |                                            |
|--------------------------------------------|--------------------------------------------|
| MailMan V. 7.1 Remote Message ID (Old) | MailMan V. 8.0 Remote Message ID (New) |
| 34561234@FORUM.VA.GOV                      | 34561234.3020803@FORUM.VA.GOV              |

<span id="_Toc161642797" class="anchor"></span>Table 2‑6. MailMan V. 8.0: New remote message ID format

#### Enhanced Routines

The ^XMC\*, ^XMR\*, ^XMS\* suite of routines, which are responsible for scheduling, transmitting to, and receiving messages from remote sites, have been completely overhauled to make them easier to understand and easier to maintain.

#### Improved Name Field Display

MailMan will no longer display user names by taking them directly from the .01 field of the NEW PERSON file (#200). The Name Standardization \$\$NAMEFMT^XLFNAME API is used instead. Thus, the names of people whose last names, for example, contain periods, apostrophes, or spaces, are properly displayed. For example:

|                                             |                                             |
|---------------------------------------------|---------------------------------------------|
| MailMan V. 7.1 Name Field Display (Old) | MailMan V. 8.0 Name Field Display (New) |
| STIVES                                      | ST. IVES                                    |
| OMALLEY                                     | O'MALLEY                                    |
| VANDYKE                                     | VAN DYKE                                    |

<span id="_Toc161642798" class="anchor"></span>Table 2‑7. MailMan V. 8.0: New name field display format

#### Broadcast Messages with Responses

Messages with responses may no longer be forwarded to broadcast to all users. Such messages may have important information in the responses, and as we all know, responses are not auto-forwarded to remote sites for users with auto-forward addresses. Users who attempt to broadcast messages with responses will be encouraged to copy the message and its responses into a new message, which can be broadcast.

#### Message Line Restriction Override

Incoming PackMan and KIDS messages are no longer subject to the restriction of the NETWORK - MAX LINES RECEIVE field (#8.31) in the MAILMAN SITE PARAMETERS file (#4.3). However, other kinds of messages continue to be subject to that restriction.

#### Requeued Task Bug Fix

If a task transmitting messages to another site fails and has to be requeued, it really is requeued. Before, that was not true. Previously, the failing task queued up a new task to take its place, and then the failing task stopped.

#### Manage MailMan Options

#### Manage Mailman \[XMMGR\]

The Manage Mailman menu \[XMMGR\] contains options that allow the system manager to fully implement and manage the MailMan system by manipulating the BULLETIN (#3.6), MAILBOX (#3.7), MAIL GROUP (#3.8), and MESSAGE (#3.9) files.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/027.png) | REF: The Manage Mailman menu options \[XMMGR\] are briefly described below, for a more detailed description of these options, please refer to the *MailMan Systems Management Guide*. Network Management options reached from this menu are discussed in depth in the *MailMan Network Reference Guide*. User options are discussed in the *MailMan Getting Started Guide* and *MailMan User Guide*. |

Select Manage Mailman Option:

Check MailMan Files for Errors \[XMUT-CHKFIL\]

\*\*\> Locked with XUPROG

Create a Mailbox for a user \[XMMGR-NEW-MAIL-BOX\]

Disk Space Management ... \[XMMGR-DISK-SPACE-MANAGEMENT\]

Group/Distribution Management ... \[XMMGR-GROUP-MAINTENANCE\]

Local Delivery Management ... \[XMMGR-MESSAGE-DELIVERY-MGT\]

MailMan Site Parameters \[XMKSP\]

Network Management ... \[XMNET\]

New Features for Managing MailMan \[XMMGR-HELP\]

Remote MailLink Directory Menu ... \[XMMGR-DIRECTORY-MAIN\]

\*\*\> Locked with XMMGR

Super Search Message File \[XM SUPER SEARCH\]

\*\*\> Locked with XM SUPER SEARCH

<span id="_Toc161642799" class="anchor"></span>Figure 2‑2. Manage Mailman menu options

Check MailMan Files for Errors \[XMUT-CHKFIL\]

The XMUT-CHKFIL option is located on the Manage Mailman Menu \[XMMGR\]. It is locked with the XUPROG security key.

This option checks for and corrects errors in the MAILBOX (#3.7) and MESSAGE (#3.9) files. It checks important fields and cross references.

It is recommended that this option be run monthly or every few months, or whenever there seems to be a database problem.

It produces a report of the errors detected, and what, if anything, it did to fix them. If it did not fix the errors, it tells you what you can do to fix them.

Although the system will not fail because of errors detected, users may inquire about the problems they experience. This utility allows you to detect any errors first and correct them before anyone else encounters an error.

Create a Mailbox for a user \[XMMGR-NEW-MAIL-BOX\]

This option is only meant to be used on systems where Kernel V. 6.0 or later is *not* running or when a repair must be made to the MAILBOX file (#3.7). Since a mailbox is created for each new or reinstated user through the Kernel software, this routine only needs to be run when an error occurs while setting up the user or if there is a file degradation problem. Using this option for a user whose mailbox is wholly or partially set up will not cause data to be lost. A mailbox can be created or repaired using this option.

Disk Space Management \[XMMGR-DISK-SPACE-MANAGEMENT\]

This option provides a submenu under the XMMGR main menu. It contains options for managing disk space. All reports are 80 columns wide.

The following options can be found on the Disk Space Management menu:

Select Disk Space Management Option

AI x-Ref Purge of Received Network Messages \[XMMGR-PURGE-AI-XREF\]

Ask users with many messages to do maintenance

\[XMMGR-DISK-MANY-MESSAGE-MAINT\]

Clean out waste baskets \[XMCLEAN\]

IN Basket Purge \[XMMGR-IN-BASKET-PURGE\]

Large Message Report \[XMMGR-LARGE-MESSAGE-REPORT\]

Message statistics \[XMSTAT\]

Purge a message \[XMMGR-PURGE-MESSAGE\]

Purge Messages by Origination Date \[XMPURGE-BY-DATE\]

\*\*\> Locked with XMMGR

Purge Unreferenced Messages \[XMPURGE\]

Recover Messages into User's IN Basket ... \[XMUT-REC-MENU\]

\*\*\> Locked with XUPROG

Terminate mail user suggestions \[XMMGR-TERMINATE-SUGGEST\]

Terminate many mail users \[XMMGR-TERMINATE-MANY\]

Terminate one mail user \[XMMGR-TERMINATE-ONE\]

<span id="_Toc161642800" class="anchor"></span>Figure 2‑3. Disk space Management menu options

- AI x-Ref Purge of Received Network Messages \[XMMGR-PURGE-AI‑XREF\]

> This option maintains the "AI" cross-reference of mail messages. This is the cross-reference of messages received across the network and it prevents duplicate messages from being received again. The default number of days kept is 730 (2 years is the number of days messages can exist before being purged on FORUM). As per MailMan Patch XM\*8.0\*38, this option should be run interactively at least once a year to reduce its size; otherwise, it continues to grow.

- Ask users with many messages to do maintenance \[XMMGR-DISK-MANY-MESSAGE-MAINT\]

> This option is used to send out a message to users with many messages and instructs them to eliminate excess messages.

- Clean out waste baskets \[XMCLEAN\]

> This option deletes all messages in users' WASTE baskets in the MAILBOX file (#3.7). It does *not* delete the messages in the MESSAGE file (#3.9). It is recommended that this option be scheduled to run daily, immediately before the XMAUTOPURGE option.

- IN Basket Purge \[XMMGR-IN-BASKET-PURGE\]

> This option purges the "IN" mail basket in two steps:

|                                                   |                                              |
|---------------------------------------------------|----------------------------------------------|
| ![](mailman-version-8-technical-manual/028.png) | CAUTION: This option can be run via TaskMan! |

> 1\. In the first step, a message is sent to users.

> a\. The message contains a list of messages to be purged in Step 2.

> b\. The message contains a list of actions that will prevent the purging of the listed messages.

> c\. The message will state the number of days before the listed messages will be purged unless the action is taken on a message by message basis.

> d\. The messages listed will *not* have been referenced for 30 days or the number of days in the MESSAGE RETENTION DAYS field in the MAILMAN SITE PARAMETERS file (#4.3), if it is *not* null.

> 2\. In the second step, the messages listed in the message from Step 1 will be purged (*not* less than 30 days later) unless they:

> a\. Have been saved into a basket other than the "IN" basket

> b\. Have been referenced (read or printed)

> c\. Are marked as NEW

- Large Message Report \[XMMGR-LARGE-MESSAGE-REPORT\]

> This option generates a list of messages that are:

- Longer than a specified number of lines (see the LARGE MESSAGE REPORT LINES field \[#8.14\] in the MAILMAN SITE PARAMETERS file \[#4.3\]).
- Messages that have no owner or only one owner.
- Messages that have no text or subject.
- Message statistics \[XMSTAT\]

> This option displays information about the MESSAGE (#3.9) and MAILBOX (#3.7) files. It displays a history of messages kept and purged by the XMAUTOPURGE option. You can delete unwanted dates through VA FileMan. The XMAUTOPURGE option enters new data when it successfully completes a purge.

> The option also displays statistics about the total number of messages in a user's mailbox. This portion of the report can be aborted when displayed on the terminal.

- Purge a message \[XMMGR-PURGE-MESSAGE\]

> This option removes a message from users' mail baskets and deletes it, along with any responses chained to it.

- Purge Messages by Origination Date \[XMPURGE-BY-DATE\]

> This option removes messages from users' mail baskets then deletes them along with any responses chained to them. It will do this for a range of messages based upon user input. The user enters the range of internal message numbers that will be processed and the date against which they will be checked. This option is locked with the XMMGR security key.

- Purge Unreferenced Messages \[XMPURGE\]

> This option purges the mail system of all messages that are no longer needed.

- Recover Messages into User's IN Basket \[XMUT-REC-MENU\]

> This option provides a submenu under the XMMGR-DISK-SPACE-MANAGEMENT menu. It contains options for recovering messages for a user. It will recover all messages a user has ever received as long as the user has not terminated from them.

> The following options can be found on the Recover Messages into User's IN Basket menu:

> Select Recover Messages into User's IN Basket Option:

> DEL Delete Found Messages from Found Messages List \[XMUT-REC-DELETE\]

> DRM Deliver Found Messages into User's IN Basket \[XMUT-REC-DELIVER\]

> FRM Find Messages for User \[XMUT-REC-FIND\]

> LRM List Messages Found \[XMUT-REC-RPT\]

<span id="_Toc161642801" class="anchor"></span>Figure 2‑4. Recover Messages into User's IN Basket menu options

- Delete Found Messages from Found Messages List \[XMUT-REC‑DELETE\]

> This option \[synonym DEL\] deletes the temporary storage of a list of messages found when the Find Messages for User option \[XMUT-REC-FIND\] is used by a user.

- Deliver Found Messages into User's IN Basket \[XMUT-REC‑DELIVER\]

> This option \[synonym DRM\] delivers messages found with the Find Messages for Users option \[XMUT-REC-FIND option\]. The messages found will be placed into the user's "IN" basket as long as they are not already in another basket.

- Find Messages for User \[XMUT-REC-FIND\]

> This option \[synonym FRM\] finds all messages that a user has ever had and has not terminated from. This list of messages can be used as input into two other processes:

- Deliver Found Messages into User's IN Basket
- List Messages Found
- List Messages Found \[XMUT-REC-RPT\]

> This option \[synonym LRM\] lists messages found for users with the Find Messages for User option \[XMUT-REC-FIND\].

- Terminate mail user suggestions \[XMMGR-TERMINATE-SUGGEST\]

> This option goes through the MAILBOX file (#3.7) and reports on users who perhaps should have their mail access terminated. Users are included in the report if:

- The user was terminated before a manager-supplied cutoff date and allowed to keep a mailbox.
- The user has an Access Code, Verify Code, and primary menu, but last signed on before a manager-supplied cutoff date.

> This option does not terminate mail access. The report page breaks on Service/Section and includes the following information:

- User's DUZ and name.
- Whether the user has an Access Code, a Verify Code, and a primary menu.
- When the user last signed on.
- When the user was terminated (if applicable).
- If the user was terminated, then whether the site manager chose to delete the user's mailbox. (Remember, you should usually answer "yes" to this question, unless the user is coming back and needs to have his mail retained.)
- How many new messages the user has. (New messages are never purged, except during purge-by-date purges.)

> Finally there are two blank columns:

- "Term User Mbox" (Terminate user mailbox)
- "Deact VISTA Access" (Deactivate VISTA Access).

> Besides being of interest to the site manager, this report is also designed to be submitted to other services. The intent is that the other services would check one of the columns for each user in the report and return the report to the site manager for action.

- Terminate many mail users \[XMMGR-TERMINATE-MANY\]

> This option goes through the MAILBOX file (#3.7) and removes any mailbox if the user:

- Is not in the NEW PERSON file (#200).
- Has no Access code and was not terminated.
- Has no Access code and was terminated without mailbox retention.
- Has an access code, but no primary menu.
- Has an Access code and primary menu, but no Verify code, *and*:
- Has never signed on or used mail since being added before a cutoff date.

> OR

- Last signed on or used mail before a cutoff date.

> However, if the user meets one of the last two conditions above, but has a forwarding address, the user's mailbox will *not* be removed. The fact will be noted on the report, and the user should be investigated further.

> Remove means:

- Delete user's private mail groups.
- Remove user from membership in all groups.
- Remove user as an authorized sender from all groups.
- Remove user from anyone's list of surrogates.
- Delete user's latered-messages list.
- Delete user's mailbox.

> As a result, the user will not receive any mail.

> This option can be run in "test" or "real" mode.

> The report lists, in DUZ order:

- The user's DUZ and name.
- Whether the user has an Access code, Verify code, and primary menu.
- When the user was added to the NEW PERSON file (#200).
- When the user last signed on or used mail.
- When the user was terminated (if applicable).
- If the user was terminated, then whether the site manager chose to delete the user's mailbox. (It's generally a good idea to go ahead and delete the mailbox upon termination.)
- If the user has an Access code and a forwarding address, the user is marked with "\*\*\*," and the forwarding address is shown. (Again, the mailbox is not deleted in this case, but the user should be investigated further.)
- Terminate one mail user \[XMMGR-TERMINATE-ONE\]

> This option lets you remove the mailbox of any user who meets the criteria of either the XMMGR-TERMINATE-MANY or the XMMGR-TERMINATE-SUGGEST options. Remove means:

- Delete user's private mail groups.
- Remove user from membership in all groups.
- Remove user as an authorized sender from all groups.
- Remove user from anyone's list of surrogates.
- Delete user's latered-messages list.
- Delete user's mailbox.

> As a result, the user will not receive any mail.

> Remember:

- Whenever you give a user a new Access code, the system gives the user a mailbox, if he does not already have one.
- Whenever a user logs on, the system gives the user a mailbox if he does not already have one.

Group/Distribution Management \[XMMGR-GROUP-MAINTENANCE\]

This is a submenu under XMMGR.

The following options can be found on the Group/Distribution Management menu:

Select Group/Distribution Management Option:

Bulletin edit \[XMEDITBUL\]

Edit Distribution List \[XMEDITDIST\]

Enroll in (or Disenroll from) a Mail Group \[XMENROLL\]

Mail Group Coordinator's Edit \[XMMGR-MAIL-GRP-COORDINATOR\]

Mail Group Coordinator's Edit W/Remotes \[XMMGR-MAIL-GRP-COORD-W/REMOTES\]

Mail Group Edit \[XMEDITMG\]

<span id="_Toc161642802" class="anchor"></span>Figure 2‑5. Group/Distribution Management menu options

- Bulletin edit \[XMEDITBUL\]

> This option allows management to enter/edit a MailMan bulletin, change the routing information, and document a bulletin.

- Edit Distribution List \[XMEDITDIST\]

> This option is used to edit a Distribution List. The name of a Distribution List is the name of a position such as Postmaster or group name such as G.IRM. A list primarily contains a set of domain names that are concatenated to the Distribution List name to create additional recipients for a message. A recipient with the same name as the list name is presumed to exist at each different domain.

> For example, if the Distribution List name is G.SUPPORT and the Domains are FORUM.VA.GOV and EXAMPLEVAMC.MED.VA.GOV, the message will be sent to:

- G.SUPPORT@FORUM.VA.GOV
- G.SUPPORT@EXAMPLEVAMC.MED.VA.GOV

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/029.png) | NOTE: A Distribution List can be in more than one mail group. Each mail group can include more than one distribution list. |

- Enroll in (or Disenroll from) a Mail Group \[XMENROLL\]

> This option allows a MailMan user to join mail groups for which the "SELF ENROLLMENT ALLOWED?" flag is set to "yes". If the user is already a member of a group, then this option allows the user to leave the group. The user will only be able to join or rejoin public groups for which self-enrollment is allowed.

- Mail Group Coordinator's Edit \[XMMGR-MAIL-GRP-COORDINATOR\]

> This option allows mail group coordinators to edit the membership of mail groups that he is the coordinator of (and no other). It does not allow editing of remote recipients, but limits the responsibility for problems of delivering to incorrect addresses.

- Mail Group Coordinator's Edit W/Remotes \[XMMGR-MAIL-GRP-COORD-W/REMOTES\]

> This option allows mail group coordinators to edit the membership of mail groups that he/she is the coordinator of (and no other). It allows editing of local and remote recipients.

- Mail Group Edit \[XMEDITMG\]

> This option edits all fields in the MAIL GROUP file (#3.8).

Local Delivery Management \[XMMGR-MESSAGE-DELIVERY-MGT\]

This submenu contains options for the background filer. All reports are 132 columns wide.

The following options can be found on the Local Delivery Management menu:

Select Local Delivery Management Option:

Active Users/Deliveries Report \[XMMGR-BKFILER-ACT\]

CHECK background filer \[XMMGR-CHECK-BACKGROUND-FILER\]

Compile Response Time Statistics \[XMMGR-RESPONSE-TIME-COMPILER\]

Deliveries by Group \[XMMGR-BKFILER-GROUP\]

Delivery Queue Statistics Collection \[XMMGR-DELIVERY-STATS-COLL\]

Edit numbers to Normalize Reports \[XMMGR-BKFILER-EDIT-NORMALIZED\]

Graphics Download (TAB separators) \[XMMGR-BKFILER-TABBED-STATS\]

Log Response Time Toggler \[XMMGR-RESPONSE-TIME-TOGGLER\]

Mail Delivery Statistics Report \[XMMGR-BKFILER-STAT\]

New Messages and Logon Statistics \[XMMGR-NEWMESS/LOGON-STATS\]

START background filer \[XMMGR-START-BACKGROUND-FILER\]

STOP background filer \[XMMGR-STOP-BACKGROUND-FILER\]

<span id="_Toc161642803" class="anchor"></span>Figure 2‑6. Local Delivery Management \[XMMGR-MESSAGE-DELIVERY-MGT\] menu options

- Active Users/Deliveries Report \[XMMGR-BKFILER-ACT\]

> This option generates a report that lists active users and message deliveries made from previously filed information in half-hour intervals.

- CHECK background filer \[XMMGR-CHECK-BACKGROUND-FILER\]

> This option tells you if the background filer is running and tells how many recipients need delivery for each of the messages/responses in the queue.

- Compile Response Time Statistics \[XMMGR-RESPONSE-TIME-COMPILER\]

> This option should be used as a background job, scheduled daily to collect statistics on the previous day's response time. The data is put into the MESSAGE DELIVERY STATS file (#4.2998). It will then KILL associated %ZTRL global nodes.

- Deliveries by Group \[XMMGR-BKFILER-GROUP\]

> This option produces a list of deliveries made for each distinct delivery queue in half-hour intervals.

- Delivery Queue Statistics Collection \[XMMGR-DELIVERY-STATS-COLL\]

> This option collects delivery queue statistics.

- Edit numbers to Normalize Reports \[XMMGR-BKFILER-EDIT-NORMALIZED\]

> This option allows the user to customize the Normalized Report.

- Graphics Download (TAB separators) \[XMMGR- BKFILER-TABBED-STATS\]

> This option can be used to capture a report and then use the captured file in a graphics software application (e.g., Microsoft Excel). The data has tabs between the fields as delimiters.

- Log Response Time Toggler \[XMMGR-RESPONSE-TIME-TOGGLER\]

> This option turns on Kernel's system parameters for response time logging, a little after each half-hour.

> It will then schedule another task to turn off the Kernel system parameters for response time logging, unless the time is between 4:00 p.m. and 8:00 a.m. During these hours, response time logging will remain on unless site management interferes, by canceling the tasks associated with this phenomenon and edits the LOG RESPONSE TIME field for the appropriate VOLUME SET to be "OFF."

- Mail Delivery Statistics Report \[XMMGR-BKFILER-STAT\]

> This option generates reports showing a list of active users, queue waits, average response time, number of lines displayed to users, etc., in half-hour intervals.

- New Messages and Logon Statistics \[XMMGR-NEWMESS/LOGON-STATS\]

> This option prints the number of new messages created and logons with logon minutes for a specified time period.

- START background filer \[XMMGR-START-BACKGROUND-FILER\]

> This option reverses the action of the STOP background filer option, if it has been run. It also restarts the background filer if it disappears from the system status report. In order for this option to be effective, TaskMan (ZTM) must be running.

- STOP background filer \[XMMGR-STOP-BACKGROUND-FILER\]

> This option stops the background filer at the *end* of a delivery and *before* it starts to deliver any further messages. This only stops local delivery operations.

> *All local mail delivery will stop* until the START background filer option is run.

|                                                                                                                |                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/030.png) | NOTE: This option stops delivery of local mail, gracefully. |

MailMan Site Parameters \[XMKSP\]

This option allows system managers to edit the fields in the MAILMAN SITE PARAMETERS file (#4.3) that do not have to do with christening. To christen a domain, use the Christen a domain option. The Christen a domain option also allows you to change fields set during the original christening if they are set incorrectly. You can use VA FileMan to edit the TRANSMISSION SCRIPT file (#4.6), if the scripts for Austin or the Mini engine need to be changed.

Network Management \[XMNET\]

The Network Management menu \[XMNET\] is the main MailMan network management menu. It contains all of the options that are used for managing the network side of MailMan. This menu contains the following options:

Select Network Management Option:

Christen a domain \[XMCHRIS\]

Compare Domains in System Against Released List \[XMQDOMAINS\]

Network Help \[XMNETHELP\]

Queue Management ... \[XMNET-QUEUE-MANAGEMENT\]

Site Parameters \[XMSITE\]

Transmission Management ... \[XMNET-TRANSMISSION-MANAGEMENT\]

<span id="_Toc161642804" class="anchor"></span>Figure 2‑7. Network Management menu options

|                                                                                                                |                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/031.png) | REF: The options found on the Network Management menu \[XMNET\] are described in the *MailMan Network Reference Guide*. |

New Features for Managing MailMan \[XMMGR-HELP\]

This option provides help for site management.

Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]

This menu provides options that allow the site manager to manage the remote MailLink Directory by loading the VACO, WANG/NOAVA, and REMOTE DOMAIN USER Directories into the REMOTE USER DIRECTORY file, ^XMD(4.2997). This option is locked with the XMMGR security key.

The following options can be found on the Remote MailLink Directory Menu:

Select Remote MailLink Directory Menu Option:

Enter/Edit Directory Request Flags by Group \[XMMGR-DIRECTORY-EDITGRP\]

Enter/Edit Remote User \[XMEDIT-REMOTE-USER\]

Group eMail Directory Request \[XMMGR-DIRECTORY-GROUP\]

List eMail Directory Request by Groups \[XMMGR-DIRECTORY-LISTGRP\]

Load Remote VACO (Wang/Noava) Directory \[XMMGR-DIRECTORY-VACO\]

Remote Directory from all Domains \[XMMGR-DIRECTORY-ALL\]

Request Mail Directory From a Single Domain Server

\[XMMGR-DIRECTORY-SINGLE\]

<span id="_Toc140480726" class="anchor"></span>Figure 2‑8. Remote MailLink Directory Menu options

- Enter/Edit Directory Request Flags by Group \[XMMGR-DIRECTORY-EDITGRP\]

> This option allows site management to control groups of Domains from which directories are requested.

- Enter/Edit Remote User \[XMEDIT-REMOTE-USER\]

> This option allows a single person's remote address to be put into the REMOTE USER DIRECTORY, so messages can be automatically addressed to him.

- Group eMail Directory Request \[XMMGR-DIRECTORY-GROUP\]

> This option allows site management to request directories from all the Domains in a group of Domains as defined in the Enter/Edit Directory Request Flags by Group option \[XMMGR-DIRECTORY-EDITGRP\].

- List eMail Directory Request by Groups \[XMMGR-DIRECTORY-LISTGRP\]

> This option lists groups created by the Group eMail Directory Request option \[XMMGR-DIRECTORY-EDITGRP\].

- Load Remote VACO (Wang/Noava) Directory \[XMMGR-DIRECTORY-VACO\]

> This option loads a file from the Host File Server. The user has the choice of whether to run this task interactively or to schedule a batch job to update the MailLink Directory.

- Remote Directory from all Domains \[XMMGR-DIRECTORY-ALL\]

> This option schedules tasks to run in the background to update the MailLink Directory, ^XMD(4.2997).

|                                                   |                                                                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/032.png) | CAUTION: Use this option cautiously, because it sends requests to all the Domains for soliciting REMOTE USER Directories. |

- Request Mail Directory From a Single Domain Server \[XMMGR-DIRECTORY-SINGLE\]

> This option schedules a task to run in the background to update the MailLink Directory, ^XMD(4.2997), from a single Domain server.

MailMan Menu \[XMUSER\]

The options located on the MailMan Menu are discussed in depth in the *MailMan Getting Started Guide* and the *MailMan User Guide*.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All MailMan routines are prefixed with the namespace XM. This section provides information related to all executable XM\* routines exported in MailMan Version 8.0. Do *not* delete any XM\* routines with the exception of any XM initialization routines, which *can* be deleted *after* installation.

|                                                                                                                |                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/033.png) | NOTE: All routines have been modified or are new with MailMan V. 8.0. |

The second line of these routines looks like:

> \<tab\>;;8.0;MailMan;;Jun 28, 2002

|                                                                                                                |                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/034.png) | NOTE: Other routine information, such as the Routine Size Histogram, the Routine %Index, etc., can be generated through the use of Kernel Utilities. |

| Routine | Description                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------|
| XM          | MailMan Main Driver (top level).                                                                                              |
| XMA         | Read Mail Application Program Interface (API).                                                                                |
| XMA0        | Print Message APIs.                                                                                                           |
| XMA03       | Resequence Messages API.                                                                                                      |
| XMA11       | Edit Message "Information Only" API.                                                                                          |
| XMA11A      | Send/Answer a Message API.                                                                                                    |
| XMA1B       | Save/Delete Message APIs.                                                                                                     |
| XMA1C       | Server Basket APIs.                                                                                                           |
| XMA2        | Create Message Stub API.                                                                                                      |
| XMA21       | Address Lookup APIs.                                                                                                          |
| XMA21C      | Input Transform (3.7, .3) Mail Name.                                                                                          |
| XMA2B       | Send Binary Large Object (BLOB).                                                                                              |
| XMA2R       | Reply to/Answer a Message API.                                                                                                |
| XMA3        | Purge Unreferenced Messages (XMCLEAN, XMAUTOPURGE).                                                                           |
| XMA30       | XMA3 (continued).                                                                                                             |
| XMA32       | Purge Messages by Date.                                                                                                       |
| XMA32A      | XMA32 (continued).                                                                                                            |
| XMA7        | User Information.                                                                                                             |
| XMAD2       | Basket Lookup/Create API.                                                                                                     |
| XMADGO      | Start Background Message Delivery.                                                                                            |
| XMAFTP      | TCPIP-FTP Options.                                                                                                            |
| XMAH        | List Message Responses API.                                                                                                   |
| XMAH1       | Reply to a Message API.                                                                                                       |
| XMAI2       | Send a Message if too Many Messages.                                                                                          |
| XMAPBLOB    | Display BLOBs.                                                                                                                |
| XMAPHOST    | Print to Message (P-MESSAGE).                                                                                                 |
| XMASEC      | Secure PackMan Message.                                                                                                       |
| XMB         | Send Bulletin APIs.                                                                                                           |
| XMBBLOB     | Add BLOBs to Bulletin.                                                                                                        |
| XMBGRP      | Mail Group APIs.                                                                                                              |
| XMC         | Network Programmer Options Menu.                                                                                              |
| XMC1        | Script Interpreter.                                                                                                           |
| XMC11       | DECNET Communications Protocol Tools.                                                                                         |
| XMC1A       | Script Interpreter (Look).                                                                                                    |
| XMC1B       | Script Interpreter (Open/Close). This routine is new with MailMan V. 8.0.                                                     |
| XMCB        | Batch Message Transmission. This routine is new with MailMan V. 8.0.                                                          |
| XMCD        | Communications Diagnostics.                                                                                                   |
| XMCDNT      | NT communications diagnostics/testing routine (shareware).                                                                    |
| XMCE        | Edit Scripts. This routine is new with MailMan V. 8.0.                                                                        |
| XMCP        | Poll Domains. This routine is new with MailMan V. 8.0.                                                                        |
| XMCQ        | Transmit Queue Status Report. This routine is new with MailMan V. 8.0.                                                        |
| XMCQA       | Transmit Queue Status Report (others). This routine is new with MailMan V. 8.0.                                               |
| XMCQH       | Transmit Queue History. This routine is new with MailMan V. 8.0.                                                              |
| XMCSIZE     | Message Statistics Tool (shareware).                                                                                          |
| XMCTLK      | TalkMan.                                                                                                                      |
| XMCTRAP     | Error Trap.                                                                                                                   |
| XMCU1       | Encode/Decode String APIs.                                                                                                    |
| XMCX        | Play a Script/Queue Transmit Task. This routine is new with MailMan V. 8.0.                                                   |
| XMCXT       | View Transcripts. This routine is new with MailMan V. 8.0.                                                                    |
| XMCXU       | Select Domains/Scripts. This routine is new with MailMan V. 8.0.                                                              |
| XMD         | Send/Forward/Add Text to a Message APIs.                                                                                      |
| XMDIR1      | Load Veterans Affairs Central Office (VACO) Directories.                                                                      |
| XMDIR1A     | Load VACO Directories (WANG).                                                                                                 |
| XMDIR1B     | Load VACO Directories (Nationwide Office Automation for Veterans Affairs \[NOAVA\]).                                          |
| XMDIRQST    | Request Email Directory.                                                                                                      |
| XMDIRRCV    | Receive Email Directory.                                                                                                      |
| XMDIRSND    | Send Email Directory.                                                                                                         |
| XMFAX       | Fax.                                                                                                                          |
| XMGAPI0     | This routine provides the APIs to validate/get a message subject (IA \#1142).                                                 |
| XMGAPI1     | This routine provides the API to get next line of a message (IA \#1048).                                                      |
| XMGAPI2     | This routine provides the API to get message header information (IA \#1144).                                                  |
| XMGAPI3     | This routine provides the server API to deliver a broadcast message and mark the message for vaporization (server; no IA \#). |
| XMGAPI4     | This routine provides the private API to get new message information (private; IA \#1142).                                    |
| XMHIG       | Mail Group Information.                                                                                                       |
| XMHIU       | User Information.                                                                                                             |
| XMJBL       | List Contents of User's Mailbox.                                                                                              |
| XMJBM       | Manage Mail in Mailbox.                                                                                                       |
| XMJBM1      | XMJBM (continued).                                                                                                            |
| XMJBN       | Access New Mail in Mailbox.                                                                                                   |
| XMJBN1      | XMJBN (continued).                                                                                                            |
| XMJBU       | Basket Utilities.                                                                                                             |
| XMJDIR      | MailMan's DIR.                                                                                                                |
| XMJERR      | Error Handling.                                                                                                               |
| XMJMA       | Interactive Answer.                                                                                                           |
| XMJMBULL    | Manual Bulletin.                                                                                                              |
| XMJMC       | Copy Message.                                                                                                                 |
| XMJMCODE    | Message Encryption/Decryption.                                                                                                |
| XMJMD       | Later Messages.                                                                                                               |
| XMJMF       | Find Messages Based on Criteria.                                                                                              |
| XMJMF1      | XMJMF (continued).                                                                                                            |
| XMJMF2      | XMJMF (continued).                                                                                                            |
| XMJMFA      | Find Message: Subject Starts with.                                                                                            |
| XMJMFB      | Find Message: Multiple Conditions.                                                                                            |
| XMJMFC      | Find message in the MESSAGE file (#3.9).                                                                                      |
| XMJML       | List Messages in Basket (cannot read).                                                                                        |
| XMJMLN      | List/Read New Messages.                                                                                                       |
| XMJMLR      | List/Read Messages in Basket.                                                                                                 |
| XMJMLR1     | XMJMLR (continued).                                                                                                           |
| XMJMOI      | Options at Ignore Prompt.                                                                                                     |
| XMJMOI1     | XMJMOI (continued).                                                                                                           |
| XMJMOIE     | Edit Message that User has Sent to Self.                                                                                      |
| XMJMOR      | Message Range Actions.                                                                                                        |
| XMJMORX     | Message Range Actions for ^TMP Message Lists.                                                                                 |
| XMJMORX1    | XMJMORX (continued).                                                                                                          |
| XMJMP       | Print, Back Up Messages.                                                                                                      |
| XMJMP1      | XMJMP (continued).                                                                                                            |
| XMJMP2      | XMJMP (continued).                                                                                                            |
| XMJMQ       | Query Recipients (Q, QD, and QN).                                                                                             |
| XMJMQ1      | XMJMQ (continued).                                                                                                            |
| XMJMR       | Interactive Reply.                                                                                                            |
| XMJMR1      | XMJMR (continued).                                                                                                            |
| XMJMRO      | Options at "reply" Transmit Prompt.                                                                                           |
| XMJMS       | Interactive Send.                                                                                                             |
| XMJMSA      | Send Anonymous User Suggestion Message.                                                                                       |
| XMJMSO      | Options at "send" Transmit Prompt.                                                                                            |
| XMJMT       | Interactive Send to Whom.                                                                                                     |
| XMKP        | Address and Post Message.                                                                                                     |
| XMKP1       | XMKP (continued).                                                                                                             |
| XMKPL       | Manage the Local Mail Posting Process.                                                                                        |
| XMKPLQ      | Post Local Messages to Correct Queues.                                                                                        |
| XMKPO       | Post, Other Messages.                                                                                                         |
| XMKPR       | Post, Remote-network Messages. This routine is new with MailMan V. 8.0.                                                       |
| XMKPR1      | XMKPR (continued). This routine is new with MailMan V. 8.0.                                                                   |
| XMKPRD      | DNS Interface. This routine is new with MailMan V. 8.0.                                                                       |
| XML         | MailMan Physical Link.                                                                                                        |
| XML1CRC     | Operating System (OS) Check Sum.                                                                                              |
| XML4CRC     | Block Mode Protocol.                                                                                                          |
| XML4CRC1    | XML4CRC (continued).                                                                                                          |
| XMLPC       | Protocol for PC Platforms.                                                                                                    |
| XMLSWP      | Sliding Window Protocol.                                                                                                      |
| XMLSWP0     | XMLSWP (continued).                                                                                                           |
| XMLSWP2     | XMLSWP (continued).                                                                                                           |
| XMLTCP      | TCP/IP to MailMan.                                                                                                            |
| XMM1        | Modem Control for VADIC 3451, MICROCOM PCS.                                                                                   |
| XMM2        | Modem Control for CERMATEK INFO MATE 212A.                                                                                    |
| XMNTEG      | XTSUMBLD KERNEL—Package Checksum Checker.                                                                                     |
| XMNTEG0     | XMNTEG (continued).                                                                                                           |
| XMP         | PackMan.                                                                                                                      |
| XMP2        | PackMan Print/Install/Summarize/Compare.                                                                                      |
| XMP2A       | PackMan Install.                                                                                                              |
| XMP3        | PackMan Build Backup Message.                                                                                                 |
| XMPC        | PackMan Compare.                                                                                                              |
| XMPG        | PackMan Global List/Load.                                                                                                     |
| XMPH        | PackMan Load Routines/Print Message.                                                                                          |
| XMPSEC      | PackMan Security.                                                                                                             |
| XMR         | Simple Mail Transfer Protocol (SMTP) Receiver (RFC 821).                                                                      |
| XMR0BLOB    | BLOB Receive.                                                                                                                 |
| XMR1        | SMTP Receiver HELO/MAIL/RCPT (RFC 821).                                                                                       |
| XMR2        | SMTP Receiver (non-standard).                                                                                                 |
| XMR3        | SMTP Receiver (RFC 822).                                                                                                      |
| XMR3A       | XMR3 (continued). This routine is new with MailMan V. 8.0.                                                                    |
| XMR4        | SMTP Help. This routine is new with MailMan V. 8.0.                                                                           |
| XMRENT      | Message Network Header Information API.                                                                                       |
| XMRFTP      | SMTP Receiver (RFC 821).                                                                                                      |
| XMRFTPUX    | SMTP Receiver (RFC 821).                                                                                                      |
| XMRINETD    | Process MSM-NT TCP Request.                                                                                                   |
| XMRMSM      | MSM TCP/IP Front End.                                                                                                         |
| XMRONT      | OpenM-NT TCP/IP INETD and Front End.                                                                                          |
| XMRPCTS     | Steal TWIXs from PCTS Host \[RCVR\].                                                                                          |
| XMRPCTS0    | Send TWIXs to PCTS Host \[XMTR\] 2.                                                                                           |
| XMRPCTS1    | Simple PCTS Front End to MailMan.                                                                                             |
| XMRPCTSA    | Steal TWIXs from PCTS Host \[RCVR\].                                                                                          |
| XMRPOP      | POP3 Server (RFC 1939).                                                                                                       |
| XMRTCP      | SMTP Receiver.                                                                                                                |
| XMRTCPGO    | Start XMRTCP.                                                                                                                 |
| XMRUCX      | SMTP Receiver (RFC 821) for UCX.                                                                                              |
| XMS         | SMTP Send.                                                                                                                    |
| XMS0BLOB    | Send BLOBs (other body parts).                                                                                                |
| XMS1        | SMTP Send (RFC 821).                                                                                                          |
| XMS2        | SMTP Send (non-standard).                                                                                                     |
| XMS3        | SMTP Send (RFC 822).                                                                                                          |
| XMSFTP      | TCP/IP-FTP Sender.                                                                                                            |
| XMSFTPUX    | TCP/IP-FTP Sender.                                                                                                            |
| XMTDF       | Filter Message: Multiple Conditions.                                                                                          |
| XMTDL       | Deliver Local Mail to Mailbox.                                                                                                |
| XMTDL1      | XMTDL (continued).                                                                                                            |
| XMTDL2      | XMTDL (continued).                                                                                                            |
| XMTDO       | Deliver Other (server, device).                                                                                               |
| XMTDR       | Transmit Messages in a Queue. This routine is new with MailMan V. 8.0.                                                        |
| XMTDT       | Deliver Latered Messages and Delete Inactive Messages.                                                                        |
| XMUCXPOP    | POP3 Server for UCX (RFC 1939).                                                                                               |
| XMUDCHK     | Validate DOMAIN file (#4.2)). This routine is new with MailMan V. 8.0.                                                        |
| XMUDCHR     | Christen Site. This routine is new with MailMan V. 8.0.                                                                       |
| XMUDNC      | Domain Name Change.                                                                                                           |
| XMUDTOP     | Top-Level Domain Names. This routine is new with MailMan V. 8.0.                                                              |
| XMUPIN      | IN Basket Purge.                                                                                                              |
| XMUT1       | Recover Messages for a User.                                                                                                  |
| XMUT1A      | XMUT1 (continued).                                                                                                            |
| XMUT2       | Large Message Report.                                                                                                         |
| XMUT4       | Integrity Checker for the MAILBOX file (#3.7) and MESSAGE file (#3.9).                                                        |
| XMUT41      | XMUT4 (continued).                                                                                                            |
| XMUT4A      | Integrity Checker for the MAILBOX file (#3.7).                                                                                |
| XMUT4C      | Integrity Checker for the MESSAGE file (#3.9).                                                                                |
| XMUT5       | Check Background Filer (local delivery queues).                                                                               |
| XMUT5B      | Gather Delivery Queue Data.                                                                                                   |
| XMUT5C      | Response Time Logger/Purge.                                                                                                   |
| XMUT5G      | Validate Mail Group Members.                                                                                                  |
| XMUT5Q      | Delivery Queue Analysis.                                                                                                      |
| XMUT5Q1     | Delivery Queue Analysis (start/init).                                                                                         |
| XMUT5R1     | Mail Statistics Report.                                                                                                       |
| XMUT5R2     | Daily Reports on Mail Deliveries.                                                                                             |
| XMUT6       | Check Delivery Queue.                                                                                                         |
| XMUT7       | Send Message to Forwarding Address.                                                                                           |
| XMUTCOM1    | XMUSRCNT.COM Count Users (shareware).                                                                                         |
| XMUTERM     | Delete Mailbox/Delete Message.                                                                                                |
| XMUTERM1    | XMUTERM (continued).                                                                                                          |
| XMUTERM2    | XMUTERM (continued).                                                                                                          |
| XMUTPUR0    | Purge "AI" Cross-reference.                                                                                                   |
| XMVGROUP    | Group Creation/Enrollment.                                                                                                    |
| XMVGRP      | Group Creation/Enrollment.                                                                                                    |
| XMVSURR     | Surrogate Management.                                                                                                         |
| XMVVITA     | Edit User's MailMan Variables.                                                                                                |
| XMVVITAE    | Initialize User's MailMan Variables.                                                                                          |
| XMXADDR     | Address Checker.                                                                                                              |
| XMXADDR1    | XMXADDR (continued).                                                                                                          |
| XMXADDR2    | XMXADDR (continued).                                                                                                          |
| XMXADDR3    | XMXADDR (continued).                                                                                                          |
| XMXADDR4    | XMXADDRG (continued).                                                                                                         |
| XMXADDRD    | Domain Name Lookup.                                                                                                           |
| XMXADDRG    | Expand Group.                                                                                                                 |
| XMXANSER    | Answer a Message.                                                                                                             |
| XMXAPI      | Message APIs.                                                                                                                 |
| XMXAPIB     | Mailbox and Mail Basket APIs.                                                                                                 |
| XMXAPIG     | Mail Group APIs.                                                                                                              |
| XMXAPIU     | Interactive User APIs.                                                                                                        |
| XMXBSKT     | Basket APIs.                                                                                                                  |
| XMXBULL     | Send Bulletin.                                                                                                                |
| XMXEDIT     | Edit Message that User has Sent to Self.                                                                                      |
| XMXGRP      | Group Creation/Enrollment.                                                                                                    |
| XMXGRP1     | XMXGRP (continued).                                                                                                           |
| XMXLIST     | List Message: Multiple Conditions.                                                                                            |
| XMXLIST1    | XMXLIST (continued).                                                                                                          |
| XMXLIST2    | XMXLIST (continued).                                                                                                          |
| XMXMBOX     | Mailbox APIs.                                                                                                                 |
| XMXMSGS     | Message APIs.                                                                                                                 |
| XMXMSGS1    | XMXMSGS (continued).                                                                                                          |
| XMXMSGS2    | XMXMSGS (continued).                                                                                                          |
| XMXPARM     | Parameter Check.                                                                                                              |
| XMXPARM1    | XMXPARM (continued).                                                                                                          |
| XMXPARMB    | Parameter Check for XMXAPIB.                                                                                                  |
| XMXPRT      | Print Messages.                                                                                                               |
| XMXREPLY    | Reply to a Message.                                                                                                           |
| XMXSEC      | Message Security and Restrictions.                                                                                            |
| XMXSEC1     | XMXSEC (continued).                                                                                                           |
| XMXSEC2     | XMXSEC (continued).                                                                                                           |
| XMXSEC3     | XMXSEC (continued).                                                                                                           |
| XMXSEND     | Send a Message.                                                                                                               |
| XMXTO       | Address a Message.                                                                                                            |
| XMXUTIL     | Message & Mailbox Utilities.                                                                                                  |
| XMXUTIL1    | Date and String Utilities.                                                                                                    |
| XMXUTIL2    | Message information.                                                                                                          |
| XMXUTIL3    | List Addressees, Recipients, Message Network Header.                                                                          |
| XMXUTIL4    | XMXUTIL3 (continued).                                                                                                         |
| XMYP18      | MailMan Patch XM\*8.0\*18 post init routine.                                                                                  |
| XMYP24      | MailMan Patch XM\*8.0\*24 post init routine.                                                                                  |
| XMYPRE      | Pre- and Post- Initialization.                                                                                                |
| XMYPRE1     | Pre- and Post- Initialization.                                                                                                |

<span id="_Toc161642806" class="anchor"></span>Table 3‑1. Routines exported with MailMan V. 8.0 and subsequent patches

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter contains information on all files and globals distributed with MailMan and references to some MailMan-related files. The file information includes: file numbers, file names, global location, and brief file descriptions. MailMan file numbers range from \#3.4 to \#4.6, with some intermediary files exported by Kernel.

|                                                                                                                |                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/035.png) | REF: For a detailed list of the files exported with MailMan, please refer to Table 4‑1. |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-technical-manual/036.png)</td>
<td><p><strong>REF:</strong> Files security access is described in the "File Security" topic in Chapter 11, "Software Product Security," in this manual.</p>
<p>Other pertinent file information, such as data dictionaries and relations with other files, can be generated online through the use of VA FileMan utilities.</p></td>
</tr>
</tbody>
</table>

|                                                   |                                                                                                                               |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/037.png) | CAUTION: All files, fields, and routines in MailMan are considered to perform controlled procedures and *cannot* be modified. |

### Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following MailMan namespaced globals are exported with MailMan:

- ^XMB
- ^XMBPOST
- ^XMBS
- ^XMBX
- ^XMD
- ^XMZ

MailMan does not export but stores data in the following globals:

- ^DIC (VA FileMan)
- ^%ZISL (Kernel)

|                                                   |                                            |
|---------------------------------------------------|--------------------------------------------|
| ![](mailman-version-8-technical-manual/038.png) | CAUTION: Journaling is highly recommended. |

|                                                   |                                                                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/039.png) | CAUTION: Your translation table *must* be set up properly in order to translate the ^XMB\* globals and the ^DIC global in all UCIs. |

|                                                                                                                |                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/040.png) | REF: All of these globals are used to store the data contained in the MailMan files referenced in the "Files" topic that follows in this chapter. |

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are files distributed with MailMan:

|                                                                                                                |                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/041.png) | NOTE: None of the files listed below come with any data. |

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 23%" />
<col style="width: 17%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File #</strong></th>
<th><strong>File Name</strong></th>
<th><strong>Global Location</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3.4</td>
<td>COMMUNICATIONS PROTOCOL</td>
<td>^DIC(3.4,</td>
<td><p>This file stores the definitions of all the communications protocols known to Kernel. A protocol has executable M code for sending, receiving, opening, and closing a link.</p>
<p>![](mailman-version-8-technical-manual/042.png) CAUTION: This file should only be edited by someone with intimate knowledge of Network MailMan.</p></td>
</tr>
<tr class="even">
<td>3.51</td>
<td>SPOOL DOCUMENT</td>
<td>^XMB(3.51,</td>
<td>This file stores the name of spool documents created by the Kernel spooler (i.e., %ZIS4) for all operating systems. It does <em>not</em> hold the text of the documents themselves. That text is first spooled to spool space, then moved into the <strong>^XMB</strong> global as a mail message. This file does, however, provide the mechanism for securing spool space for and during spooling. It is cross-referenced by NAME, USER, OTHER AUTHORIZED USERS, SPOOL DATA, and SPOOL NUMBER.</td>
</tr>
<tr class="odd">
<td>3.519</td>
<td>SPOOL DATA</td>
<td>^XMBS(3.519,</td>
<td>This is the holding file for spool documents until moved to a mail message or deleted.</td>
</tr>
<tr class="even">
<td>3.6</td>
<td>BULLETIN</td>
<td>^XMB(3.6,</td>
<td><p>This file stores bulletins. Bulletins are "Super" messages. Each Bulletin has a text and a subject just like a normal message. However, embedded within the subject and/or the text can be variable fields that can be filled in with parameters. There is also a standard set of recipients in the form of a mail group that is associated with the bulletin.</p>
<p>MailMan processes bulletins either because of a special cross-reference type of VA FileMan or because of a direct call in a routine. The interface for the direct call is described in the documentation on programmer entry points (APIs). VA FileMan sets up code that will issue a bulletin automatically when the special cross-reference type is created. In either case, the parameters merged into the text and/or the subject normally make each bulletin instance unique.</p></td>
</tr>
<tr class="odd">
<td>3.7</td>
<td>MAILBOX</td>
<td>^XMB(3.7,</td>
<td><p>This file stores pointers to the MESSAGE file (#3.9), according to users. Each MAILBOX file (#3.7) entry corresponds to a user. The Postmaster is a special user who controls the network communications queues. Each user is automatically given two baskets: "IN" and "WASTE." All incoming messages are delivered either to a user's "IN" basket or to another basket based on mail filters established by the user. When the user deletes messages, they are temporarily stored in the "WASTE" basket. Users can create new baskets and filter mail as they wish.</p>
<p>![](mailman-version-8-technical-manual/043.png) <strong>NOTE:</strong> This file was modified with MailMan V. 8.0 software. The following fields were modified:</p>
<ul>
<li><blockquote>
<p>FORWARDING ADDRESS (#2)—The bulletin cross-reference was changed.</p>
</blockquote></li>
<li><blockquote>
<p>NETWORK PRIORITY TRANSMISSION (#6)—Expanded the SET OF CODES to add low priority and changed the cross-reference.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>3.73</td>
<td>MESSAGES TO BE NEW AT A LATER DATE</td>
<td>^XMB(3.73,</td>
<td>This file stores pointers to the MESSAGE file (#3.9), pointing to messages to be new at a later date and time. The background filer processes entries in this file. The messages pointed at become new at the date and time requested.</td>
</tr>
<tr class="odd">
<td>3.8</td>
<td>MAIL GROUP</td>
<td>^XMB(3.8,</td>
<td><p>This file stores the names of all mail groups known to MailMan and their members.</p>
<p>![](mailman-version-8-technical-manual/044.png) <strong>NOTE:</strong> This file was modified with MailMan V. 8.0 software. The NAME field (#.01) was modified to add a trigger to populate the COORDINATOR field (#5.1).</p></td>
</tr>
<tr class="even">
<td>3.816</td>
<td>DISTRIBUTION LIST</td>
<td>^XMB(3.816,</td>
<td><p>This file stores names of Distribution Lists. A Distribution List is interpreted as a name to which the message will be delivered at each of the associated Domains in the list. Each name is associated with one or more Domains. When a Distribution List is entered into a mail group, MailMan delivers a message to all the entities it has linked to it.</p>
<p>For example, a Distribution List whose name is G.SUPPORT and whose associated domains are FORUM.VA.GOV, EXAMPLEVAMC.VA.GOV, and EXAMPLEOIFO.VA.GOV will be sent (in addition to all other entities attached to the mail group) to:</p>
<ul>
<li><blockquote>
<p>G.SUPPORT@FORUM.VA.GOV</p>
</blockquote></li>
<li><blockquote>
<p>G.SUPPORT@EXAMPLEVAMC.VA.GOV</p>
</blockquote></li>
<li><blockquote>
<p>G.SUPPORT@EXAMPLEOIFO.VA.GOV</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>3.9</td>
<td>MESSAGE</td>
<td>^XMB(3.9,</td>
<td>This file stores all MailMan messages.</td>
</tr>
<tr class="even">
<td>4.2</td>
<td>DOMAIN</td>
<td>^DIC(4.2,</td>
<td><p>This file stores the names of all nodes to which MailMan messages can be routed (i.e., Domains). Each name in this file corresponds to the right side of a MailMan address following the at-sign ("<strong>@</strong>").</p>
<p>Domains can have synonyms, allowing users to name sites with one name, while MailMan uses the more formal Domain naming conventions.</p>
<p>This file also controls whether messages are queued for immediate transmission and into what queue they are dropped.</p>
<p>Any Domain can have a Relay Domain, which controls the routing as follows:</p>
<ul>
<li><blockquote>
<p>If a Domain has a named Relay Domain, the message is put in the queue for the Relay Domain.</p>
</blockquote></li>
<li><blockquote>
<p>If a Domain does not have a named Relay Domain and the Domain has a TRANSMISSION SCRIPT, the message is put in the queue for that Domain.</p>
</blockquote></li>
<li><blockquote>
<p>If a Domain does not have a named Relay Domain and also does not have a TRANSMISSION SCRIPT, the message is put in the queue for the Parent Domain, as defined at MailMan initialization time.</p>
</blockquote></li>
</ul>
<p>![](mailman-version-8-technical-manual/045.png) <strong>NOTE:</strong> This file was modified with MailMan V. 8.0.</p>
<p>![](mailman-version-8-technical-manual/046.png) <strong>NOTE:</strong> If for some reason your site needs a copy of the DOMAIN file (#4.2), it is recommended that you call another site nearby or your supporting OI Field Office.</p></td>
</tr>
<tr class="odd">
<td>4.281</td>
<td>INTER-UCI TRANSFER</td>
<td>^%ZISL(4.281,</td>
<td><p>The file is used by MailMan to do <em>non</em>-interactive transmissions and receptions of messages to and from UCIs that share the %ZISL file either because they are on the same machine or because they are on the same local area network (LAN) and use DDP translation techniques for the %ZISL global.</p>
<p>![](mailman-version-8-technical-manual/047.png) <strong>NOTE:</strong> This file was modified with the MailMan V. 8.0 software. The following Multiple fields were modified:</p>
<ul>
<li><blockquote>
<p>FROM DOMAIN (#.01):</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Increase length of field from 30 to 64.</p>
</blockquote></li>
<li><blockquote>
<p>Increase length of B cross-reference from 30 to 64.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>TO DOMAIN (#1):</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Increase length of field from 50 to 64.</p>
</blockquote></li>
<li><blockquote>
<p>Increase length of C cross-reference from 30 to 64.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>4.2995</td>
<td>MAILMAN OUTSTANDING FTP TRANSACTIONS</td>
<td>^XMBX(4.2995,</td>
<td>This file stores entries that describe file transfers that will be controlled by the TCP/IP Poller.</td>
</tr>
<tr class="odd">
<td>4.2996</td>
<td>INTERNET SUFFIX</td>
<td>^DIC(4.2996,</td>
<td><p>This file stores Internet-reserved names that cannot be used under certain circumstances:</p>
<ul>
<li><p>Domain names <em>cannot</em> partially match the Internet-reserved name.</p></li>
<li><p>Domain names <em>cannot</em> match the Internet-reserved name.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>4.2997</td>
<td>REMOTE USER DIRECTORY</td>
<td>^XMD(4.2997,</td>
<td>This files stores users with known off-system electronic mail addresses.</td>
</tr>
<tr class="odd">
<td>4.2998</td>
<td>MESSAGE DELIVERY STATS</td>
<td>^XMBX(4.2998,</td>
<td>This file stores statistics about local message deliveries, response time, and numbers of active user processes.</td>
</tr>
<tr class="even">
<td>4.2999</td>
<td>MESSAGE STATISTICS</td>
<td>^XMBS(4.2999,</td>
<td><p>This file is stores <em>non</em>-static information about network mail transmissions.</p>
<p>![](mailman-version-8-technical-manual/048.png) <strong>NOTE:</strong> This file was modified with the DNS-Aware MailMan V. 8.0 software. The following fields were modified:</p>
<ul>
<li><blockquote>
<p>NAME (#.01)—Changed the title and description.</p>
</blockquote></li>
<li><blockquote>
<p>MESSAGE IN TRANSIT (#2)—Changed to a pointer and changed the help prompt.</p>
</blockquote></li>
<li><blockquote>
<p>MESSAGES RECEIVED (#103))—Corrected the spelling of "included".</p>
</blockquote></li>
<li><blockquote>
<p>CHARACTERS SENT (#104)—Increased the length of this field.</p>
</blockquote></li>
<li><blockquote>
<p>CHARACTERS RECEIVED (#105)—Increased the length of this field.</p>
</blockquote></li>
<li><blockquote>
<p>LINES SENT (#106)—Increased the length of this field.</p>
</blockquote></li>
<li><blockquote>
<p>LINES RECEIVED (#107)—Increased the length of this field.</p>
</blockquote></li>
</ul>
<blockquote>
<p>The following fields were added:</p>
</blockquote>
<ul>
<li><blockquote>
<p>DIRECTION (#8))—This field is used to report whether, at any given time, we are sending messages to, or receiving messages from, the site.</p>
</blockquote></li>
<li><blockquote>
<p>XMIT IP ADDRESSES TRIED (#48)—This is a list of IP addresses, separated by commas, which have already been used in attempting to connect with the site.</p>
</blockquote></li>
<li><blockquote>
<p>XMIT AUDIT IP ADDRESS (#60,3)—This is the IP address used for this attempt.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>4.3</td>
<td>MAILMAN SITE PARAMETERS</td>
<td>^XMB(1,</td>
<td><p>This file stores the MailMan site parameters. It has only one entry—the Domain name of the installation site. The system manager defines some parameters during the installation process. These include: TIME ZONE, UCI ASSOCIATION TABLE (VOLUME SET Multiple), and specification of the account where XMAD, the MailMan background filer, should run. Other entries can be edited subsequent to installation. The PARENT DOMAIN, set to FORUM during initialization, can be changed. TaskMan, spooling, response time, and audit parameters can also be established. Priorities can be set for interactive users and for TaskMan. Defaults for fields such as: TIMED READ, AUTO MENU, and ASK DEVICE are defined for use when not otherwise specified for a user or device. Cross-references include: TIME ZONE, DOMAIN NAME, PARENT, and LINKED UCI.</p>
<p>![](mailman-version-8-technical-manual/049.png) <strong>NOTE:</strong> This file was modified with MailMan V. 8.0. The following fields were added:</p>
<ul>
<li><blockquote>
<p>DNS AWARE (#8.22)—MailMan uses this field to determine if it should use DNS to look up IP addresses.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>If "NO," MailMan will use the IP addresses in the Domain scripts.</p>
</blockquote></li>
<li><blockquote>
<p>If "YES," will use the IP addresses in the domain scripts, but if they fail, or do not exist, MailMan will use DNS to ascertain other IP addresses to try. MailMan will replace failed script IP address with the successful DNS IP address.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>TCP/IP COMMUNICATIONS PROTOCOL (#8.23)—MailMan uses this field to determine which protocol shall be used for TCP/IP. It points to the COMMUNICATIONS PROTOCOL file (#3.4).</p>
</blockquote></li>
<li><blockquote>
<p>TCP/IP TRANSMISSION SCRIPT (#8.24)—MailMan uses this field to determine which script shall be used for TCP/IP. It points to the TRANSMISSION SCRIPT file (#4.6).</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>4.4</td>
<td>MAILMAN TIME ZONE</td>
<td>^XMB(4.4,</td>
<td>This file stores MailMan time zones. MailMan time zones are used to calculate the time in the time zone of the receiving Domain for a message coming in from a different time zone; therefore, times can be expressed in EST (Eastern Standard Time), even if they were originally formed in PST (Pacific Standard Time).</td>
</tr>
<tr class="odd">
<td>4.5</td>
<td>NETWORK TRANSACTION</td>
<td>^XMBX(4.5,</td>
<td>This file is not currently in use by MailMan. It is still distributed because there may be local sites that have software that uses it.</td>
</tr>
<tr class="even">
<td>4.501</td>
<td>NETWORK SENDERS REJECTED</td>
<td>^XMBX(4.501,</td>
<td>This file stores names of network addresses. The system manager can input partial or full matches to network addresses into this file. When Network MailMan receives a message from a sender that contains the string input, that sender will be rejected. This can be used to prevent large messages or large quantities of messages from coming into a system from a remote site.</td>
</tr>
<tr class="odd">
<td>4.6</td>
<td>TRANSMISSION SCRIPT</td>
<td>^XMB(4.6,</td>
<td>This file stores transmission scripts. Transmission scripts are lists of script commands that are executed by the script processor for Network Mail transmissions, in order, when they are invoked. The command in a script that invokes a transmission script is the CALL (C); therefore, "C KERNEL" invokes a script that interfaces with the Simple Mail Transfer Protocol (SMTP) process using the Simple Communications Protocol (SCP). Transmission scripts are used most often to invoke a portion of a longer script that is used in many different domains.</td>
</tr>
</tbody>
</table>

<span id="_Ref161620205" class="anchor"></span>Table 4‑1. Files exported with MailMan

Multimedia MailMan-related Files

In order for Multimedia MailMan to work properly, sites must also have access to the following files:

| File \# | File Name    | Description                                                                      |
|-------------|------------------|--------------------------------------------------------------------------------------|
| 2005        | IMAGE            | This file stores pointers to files and related data so that they can be displayed.   |
| 2005.2      | NETWORK LOCATION | This file stores the logical name of the physical location where an image is stored. |

<span id="_Toc161642808" class="anchor"></span>Table 4‑2. Multimedia MailMan-related files

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan Master Menu

The following menu diagram was generated using the Map Pointer Relations option (i.e., DI DDMAP) on the Programmer Options menu (i.e., XUPROG):

MailMan Master Menu (XMMASTER)

\*\*LOCKED: XMTALK\*\*

\|

\|

--XMM Manage ---------------------------------------------------- Check

Mailman MailMan

\[XMMGR\] Files for

\| Errors

\| \[XMUT-CHKFIL\]

\| \*\*LOCKED:

\| XUPROG\*\*

\|

\|------------------------------------------------------ Create a

\| Mailbox

\| for a user

\| \[XMMGR-NEW-

\| MAIL-BOX\]

\|

\|-------------- Disk Space ---------------------------- AI x-Ref

\| Management Purge of

\| \[XMMGR-DISK- Received

\| SPACE-MANAGEMENT\] Network

\| \| Messages

\| \| \[XMMGR-PURGE-

\| \| AI-XREF\]

\| \|

\| \|---------------------------------- Ask users

\| \| with many

\| \| messages

\| \| to do

\| \| maintenance

\| \| \[XMMGR-DISK-MANY-

\| \| MESSAGE-MAINT\]

\| \|

\| \|---------------------------------- Clean out

\| \| waste

\| \| baskets

\| \| \[XMCLEAN\]

\| \|

\| \|---------------------------------- IN Basket

\| \| Purge

\| \| \[XMMGR-IN-

\| \| BASKET-PURGE\]

\| \|

\| \|---------------------------------- Large

\| \| Message

\| \| Report

\| \| \[XMMGR-LARGE-

\| \| MESSAGE-REPORT\]

\| \|

\| \|---------------------------------- Message

\| \| statistics

\| \| \[XMSTAT\]

\| \|

\| \|---------------------------------- Purge a

\| \| message

\| \| \[XMMGR-PURGE-

\| \| MESSAGE\]

\| \|

\| \|---------------------------------- Purge

\| \| Messages

\| \| by

\| \| Origination

\| \| Date

\| \| \[XMPURGE-BY-

\| \| DATE\]

\| \| \*\*LOCKED: XMMGR\*\*

\| \|

\| \|---------------------------------- Purge

\| \| Unreferenced

\| \| Messages

\| \| \[XMPURGE\]

\| \|

\| \|-------------- Recover --------DEL Delete

\| \| Messages Found

\| \| into Messages

\| \| User's IN from Found

\| \| Basket Messages

\| \| \[XMUT-REC- List

\| \| MENU\] \[XMUT-REC-

\| \| \*\*LOCKED: DELETE\]

\| \| XUPROG\*\*

\| \| \|

\| \| \|-----------DRM Deliver

\| \| \| Found

\| \| \| Messages

\| \| \| into

\| \| \| User's IN

\| \| \| Basket

\| \| \| \[XMUT-REC-

\| \| \| DELIVER\]

\| \| \|

\| \| \|-----------FRM Find

\| \| \| Messages

\| \| \| for User

\| \| \| \[XMUT-REC-FIND\]

\| \| \|

\| \| \|-----------LRM List

\| \| Messages

\| \| Found

\| \| \[XMUT-REC-RPT\]

\| \|

\| \|

\| \|---------------------------------- Terminate

\| \| mail user

\| \| suggestions

\| \| \[XMMGR-TERMINATE-

\| \| SUGGEST\]

\| \|

\| \|---------------------------------- Terminate

\| \| many mail

\| \| users

\| \| \[XMMGR-TER

\| \| MINATE-MANY\]

\| \|

\| \|---------------------------------- Terminate

\| one mail user

\| \[XMMGR-TERMINATE-

\| ONE\]

\|

\|

\|-------------- Group/Distribution--------------------- Bulletin edit

\| Management \[XMEDITBUL}

\| \[XMMGR-GROUP-

\| MAINTENANCE\]

\| \|

\| \|---------------------------------- Edit

\| \| Distribution

\| \| List

\| \| \[XMEDITDIST\]

\| \|

\| \|---------------------------------- Enroll in (or

\| \| Disenroll

\| \| from) a

\| \| Mail Group

\| \| \[XMENROLL\]

\| \|

\| \|---------------------------------- Mail Group

\| \| Coordinator's

\| \| Edit

\| \| \[XMMGR-MAIL-GRP-

\| \| COORDINATOR\]

\| \|

\| \|---------------------------------- Mail Group

\| \| Coordinator's

\| \| Edit

\| \| W/Remotes

\| \| \[XMMGR-MAIL-GRP-

\| \| COORD-W/REMOTES\]

\| \|

\| \|---------------------------------- Mail Group

\| Edit

\| \[XMEDITMG\]

\|

\|

\|-------------- Local --------------------------------- Active

\| Delivery Users/Deliveries

\| Management Report

\| \[XMMGR-MESSAGE- \[XMMGR-BKFILER-

\| DELIVERY-MGT\] ACT\]

\| \|

\| \|---------------------------------- CHECK

\| \| background filer

\| \| \[XMMGR-CHECK-

\| \| BACKGROUND-FILER\]

\| \|

\| \|---------------------------------- Compile

\| \| Response Time

\| \| Statistics

\| \| \[XMMGR-RESPONSE-

\| \| TIME-COMPILER\]

\| \|

\| \|---------------------------------- Deliveries

\| \| by Group

\| \| \[XMMGR-BKFILER-

\| \| GROUP\]

\| \|

\| \|---------------------------------- Delivery

\| \| Queue

\| \| Statistics

\| \| Collection

\| \| \[XMMGR-DELIVERY-

\| \| STATS-COLL\]

\| \|

\| \|---------------------------------- Edit

\| \| numbers to

\| \| Normalize

\| \| Reports

\| \| \[XMMGR-BKFILER-

\| \| EDIT-NORMALIZED\]

\| \|

\| \|---------------------------------- Graphics

\| \| Download

\| \| (TAB separators)

\| \| \[XMMGR-BKFILER-

\| \| TABBED-STATS\]

\| \|

\| \|---------------------------------- Log

\| \| Response

\| \| Time Toggler

\| \| \[XMMGR-RESPONSE-

\| \| TIME-TOGGLER\]

\| \|

\| \|---------------------------------- Mail

\| \| Delivery

\| \| Statistics

\| \| Report

\| \| \[XMMGR-BKFILER-

\| \| STAT\]

\| \|

\| \|---------------------------------- New

\| \| Messages

\| \| and Logon

\| \| Statistics

\| \| \[XMMGR-NEW

\| \| MESS/LOGON-STATS\]

\| \|

\| \|---------------------------------- START

\| \| background filer

\| \| \[XMMGR-START-

\| \| BACKGROUND-FILER\]

\| \|

\| \|---------------------------------- STOP

\| background filer

\| \[XMMGR-STOP-

\| BACKGROUND-FILER\]

\|

\|

\|------------------------------------------------------ MailMan

\| Site

\| Parameters

\| \[XMKSP\]

\|

\|-------------- Network ------------------------------- Christen a

\| Management domain

\| \[XMNET\] \[XMCHRIS\]

\| \|

\| \|---------------------------------- Compare

\| \| Domains in

\| \| System

\| \| Against

\| \| Released

\| \| List

\| \| \[XMQDOMAINS\]

\| \|

\| \|---------------------------------- Network

\| \| Help

\| \| \[XMNETHELP\]

\| \|

\| \|-------------- Queue ------------- Actively

\| \| Management Transmitting/

\| \| \[XMNET-QUEUE- Receiving

\| \| MANAGEMENT\] Queues Report

\| \| \| \[XMQACTIVE\]

\| \| \|

\| \| \|-------------- Display

\| \| \| Active &

\| \| \| Inactive

\| \| \| Message

\| \| \| Queues

\| \| \| \[XMQDISP\]

\| \| \| \*\*LOCKED:

\| \| \| XUPROGMODE\*\*

\| \| \|

\| \| \|-------------- Historical

\| \| \| Queue

\| \| \| Data/Stats

\| \| \| Report

\| \| \| \[XMQHIST\]

\| \| \|

\| \| \|-------------- List a

\| \| \| transcript

\| \| \| \[XMLIST\]

\| \| \|

\| \| \|-------------- Queues

\| \| \| with

\| \| \| Messages

\| \| \| to Transmit

\| \| \| Report

\| \| \| \[XMQUEUED\]

\| \| \|

\| \| \|-------------- Show a queue

\| \| \| \[XMQSHOW\]

\| \| \|

\| \| \|-------------- Transmit a

\| \| \| Single Queue

\| \| \| \[XMSTARTQUE\]

\| \| \|

\| \| \|-------------- Transmit

\| \| All Queues

\| \| \[XMSTARTQUE-ALL\]

\| \|

\| \|

\| \|---------------------------------- Site

\| \| Parameters

\| \| \[XMSITE\]

\| \|

\| \|-------------- Transmission------- Edit a

\| Management script

\| \[XMNET- \[XMSCRIPTEDIT\]

\| TRANSMISSION-

\| MANAGEMENT\]

\| \|

\| \|-------------- Play a script

\| \| \[XMSCRIPTPLAY\]

\| \|

\| \|-------------- Receive

\| \| Messages

\| \| from Another UCI

\| \| \[XMR-UCI-RCV\]

\| \|

\| \|-------------- Send

\| \| Messages

\| \| to Another UCI

\| \| \[XMR-UCI-SEND\]

\| \|

\| \|-------------- Sequential

\| \| Media

\| \| Message

\| \| Reception

\| \| \[XMR-SEQ-RECEIVE\]

\| \|

\| \|-------------- Sequential

\| \| Media

\| \| Queue

\| \| Transmission

\| \| \[XMS-SEQ-

\| \| TRANSMIT\]

\| \|

\| \|-------------- Subroutine

\| \| editor

\| \| \[XMSUBEDIT\]

\| \|

\| \|-------------- Toggle a

\| \| script out

\| \| of service

\| \| \[XMSCRIPTOUT\]

\| \|

\| \|-------------- Validation

\| Number

\| Edit

\| \[XMEDIT-DOMAIN-

\| VALIDATION#\]

\|

\|

\|

\|------------------------------------------------------ New

\| Features

\| for

\| Managing

\| MailMan

\| \[XMMGR-HELP\]

\|

\|-------------- Remote -------------------------------- Enter/Edit

\| MailLink Directory

\| Directory Request

\| Menu Flags by

\| \[XMMGR-DIRECTORY-MAIN\] Group

\| \*\*LOCKED: XMMGR\*\* \[XMMGR-DIRECTORY-

\| \| EDITGRP\]

\| \|

\| \|---------------------------------- Enter/Edit

\| \| Remote

\| \| User

\| \| \[XMEDIT-REMOTE-

\| \| USER\]

\| \|

\| \|---------------------------------- Group eMail

\| \| Directory

\| \| Request

\| \| \[XMMGR-DIRECTORY-

\| \| GROUP\]

\| \|

\| \|---------------------------------- List eMail

\| \| Directory

\| \| Request by

\| \| Groups

\| \| \[XMMGR-DIRECTORY-

\| \| LISTGRP\]

\| \|

\| \|---------------------------------- Load Remote VACO

\| \| (Wang/Noava)

\| \| Directory

\| \| \[XMMGR-DIRECTORY-

\| \| VACO\]

\| \|

\| \|---------------------------------- Remote

\| \| Directory

\| \| from all

\| \| Domains

\| \| \[XMMGR-DIRECTORY-

\| \| ALL\]

\| \|

\| \|---------------------------------- Request

\| Mail

\| Directory

\| From a Single

\| Domain Server

\| \[XMMGR-DIRECTORY-

\| SINGLE\]

\|

\|

\|------------------------------------------------------ Super Search

Message File

\[XM SUPER SEARCH\]

\*\*LOCKED:

XM SUPER SEARCH\*\*

--XMN Network Management

\[XMNET\]

--XMU MailMan ------------------------------------------------NML New

Menu Messages

\[XMUSER\] and Responses

\| \[XMNEW\]

\|

\|---------------------------------------------------RML Read/Manage

\| Messages

\| \[XMREAD\]

\|

\|---------------------------------------------------SML Send a Message

\| \[XMSEND\]

\|

\|------------------------------------------------------ Query/Search

\| for

\| Messages

\| \[XMSEARCH\]

\|

\|---------------------------------------------------AML Become a

\| Surrogate

\| (SHARED,MAIL

\| or Other)

\| \[XMASSUME\]

\|

\|-------------- Personal ------------------------------ User

\| Preferences Options

\| \[XM Edit

\| PERSONAL \[XMEDITUSER\]

\| MENU\]

\| \|

\| \|---------------------------------- Banner Edit

\| \| \[XMBANNER\]

\| \|

\| \|---------------------------------- Surrogate Edit

\| \| \[XMEDITSURR\]

\| \|

\| \|---------------------------------- Message Filter

\| \| Edit

\| \| \[XM FILTER EDIT\]

\| \|

\| \|---------------------------------- Delivery

\| \| Basket

\| \| Edit

\| \| \[XM DELIVERY

\| \| BASKET EDIT\]

\| \|

\| \|-------------------------------GML Enroll in (or

\| \| Disenroll

\| \| from) a

\| \| Mail Group

\| \| \[XMENROLL\]

\| \|

\| \|---------------------------------- Personal

\| \| Mail Group Edit

\| \| \[XMEDITPERSGROUP\]

\| \|

\| \|---------------------------------- Forwarding

\| Address

\| Edit

\| \[XMEDITFWD\]

\|

\|

\|-------------- Other --------------------------------- Report on

\| MailMan Latered

\| Functions Messages

\| \[XMOTHER\] \[XMLATER-REPORT\]

\| \|

\| \|---------------------------------- Change/Delete

\| \| Latered

\| \| Messages

\| \| \[XMLATER-EDIT\]

\| \|

\| \|---------------------------------- Mailbox

\| \| Contents List

\| \| \[XMBASKLIST\]

\| \|

\| \|-------------------------------LML Load PackMan

\| Message

\| \[XMPACK\]

\| \*\*LOCKED:

\| XUPROGMODE\*\*

\|

\|

\|-------------- Help ---------------------------------- User

(User/Group Information

Info., etc.) \[XMHELPUSER\]

\[XMHELP\]

\|

\|---------------------------------- Group

\| Information

\| \[XMHELPGROUP\]

\|

\|---------------------------------- Remote User

\| Information

\| \[XMHELPLNK\]

\|

\|---------------------------------- New Features

\| in MailMan

\| \[XM-NEW-FEATURES\]

\|

\|---------------------------------- General MailMan

\| Information

\| \[XMHELPALL\]

\|

\|---------------------------------- Questions and

\| Answers on

\| MailMan

\| \[XMHELPQUEST\]

\|

\|---------------------------------- Manual for

MailMan Users

\[XMHELP-ON-

LINE-USER_MANUAL\]

<span id="_Hlt450982330" class="anchor"></span>Figure 5‑1. MailMan Master Menu (XMMASTER) diagram

### Options—*Without* Parents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following MailMan options are *not* assigned to any menu when the MailMan software is exported. They can be assigned at the discretion of the system manager, if appropriate:

|                                                                                                                |                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/050.png) | NOTE: The XMDX, XMPRECV, and XMPSEND options *cannot* be independently invoked or are for developer/support debugging only. The XMPRECV and XMPSEND menu options are used as PackMan options and are used from the menus executed from ^DOPT("XMP"). |

| Option             | Description                                                       |
|------------------------|-----------------------------------------------------------------------|
| XMAUTOPURGE            | Purge unreferenced messages.                                          |
| XMBLOBSEND             | Send multimedia messages (Imaging software).                          |
| XMDX                   | Diagnostics menu.                                                     |
| XMMASTER               | Master menu.                                                          |
| XMMGR-BACKGROUND-FILER | Background filer submenu.                                             |
| XMMGR-BKFILER-WAIT     | Runs Delivery Queues Wait Report.                                     |
| XMMGR-DIRECTORY-RECV   | Server—Receives a directory.                                          |
| XMMGR-DIRECTORY-SEND   | Server—Sends a directory.                                             |
| XMMGR-PURGE-MESSAGE    | Purge a message.                                                      |
| XMNET-TWIX-SEND        | Sends a TWIX via PCTS.                                                |
| XMNET-TWIX-TRANSMIT    | Transmits a TWIX over the network.                                    |
| XMOTHER-COMMUNICATIONS | Send and receive files.                                               |
| XMPOLL                 | Play scripts.                                                         |
| XMPRECV                | PackMan menu to print, compare, and load PackMan messages.            |
| XMPSEND                | PackMan menu to load routines, files, globals, and data dictionaries. |
| XMR-BROADCAST-VA-WIDE  | Server for messages broadcast to SHARED,MAIL.                         |
| XMRONT                 | TCP/IP Listener for MailMan.                                          |
| XMSCRIPTRES            | Resume processing a script.                                           |
| XMSHARE                | Assume the identity of SHARED,MAIL.                                   |
| XMSUGGESTION           | Send anonymous mail to the SUGGESTION BOX of SHARED,MAIL.             |
| XMTALK                 | TalkMan communications tool.                                          |
| XMYB-BROADCAST-VA-WIDE | Server for message broadcast to all users.                            |

<span id="_Toc161642810" class="anchor"></span>Table 5‑1. MailMan options without parents

### Options—Listed Alphabetically by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following MailMan options are distributed with the MailMan software (listed alphabetically).Each option includes the following information: name, locks (if any), type, routine, entry action, exit action, menu text, and description.

|                                                                                                                |                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/051.png) | NOTE: The XMDX, XMPRECV, and XMPSEND options *cannot* be independently invoked or are for developer/support debugging only. The XMPRECV and XMPSEND menu options are used as PackMan options and are used from the menus executed from ^DOPT("XMP"). |

#### XM DELIVERY BASKET EDIT

Type: run routine Routine: BASKET^XMVVITA

Menu Text: Delivery Basket Edit

The XM DELIVERY BASKET EDIT option is located on the Personal Preferences menu \[XM PERSONAL MENU\]. The sender of a message may specify the basket to which the message should be delivered for all recipients. Using the XM DELIVERY BASKET EDIT option, you indicate whether or not you accept such target basket delivery, and if you do, to what degree you accept it.

#### XM FILTER EDIT

Type: run routine Routine: FILTER^XMVVITA

Menu Text: Message Filter Edit

The XM FILTER EDIT option is located on the Personal Preferences menu \[XM PERSONAL MENU\]. It allows users to edit their message filters. MailMan uses filters to determine into which basket to place a message. Messages can be filtered based on up to three criteria, which all can be considered together as connected by an "and" statement:

- Subject contains
- Message is from
- Message is to

For example, if you specify "subject contains" and "message is from," the filter takes effect only if the subject contains the string you specify *and* the message is from the person you specify. If you wish the filter to take effect upon "subject contains" *or* "message is from" you *must* create two filters, one with "subject contains," and the other with "message is from."

#### XM PERSONAL MENU

Type: menu

Menu Text: Personal Preferences

The XM PERSONAL MENU is a submenu located on the MailMan Menu \[XMUSER\]. It provides various options that let users configure MailMan to their liking.

#### XM SUPER SEARCH

Type: run routine Routine: SUPER^XMJMF

Menu Text: Super Search Message File

Lock: XM SUPER SEARCH

The XM SUPER SEARCH option is located on the Manage Mailman Menu \[XMMGR\]. It lets the authorized user (i.e., anyone holding the XM SUPER SEARCH security key) search the MESSAGE file (#3.9) for messages meeting any number of criteria, no matter who sent the messages.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-technical-manual/052.png)</td>
<td><p>CAUTION: This option should <em>not</em> be used lightly. One example in which usage is justified would be the search for evidence in an Equal Employment Opportunity (EEO) harassment case.</p>
<p>This option should be audited to track whoever uses it.</p></td>
</tr>
</tbody>
</table>

Every search triggers the sending of the XM SUPER SEARCH bulletin to the XM SUPER SEARCH mail group. The bulletin will record who (i.e., DUZ) conducted the search and what criteria were used. It will *not* record the results of the search.

The XM SUPER SEARCH mail group *must* have at least two active local users in it who have logged on recently. If it does not, the search will not be performed. Members of this mail group should be anyone whose responsibility it is to ensure that security is maintained and privileges are not abused. The mail group coordinator should be the site's Information Security Officer (ISO) or another responsible individual.

#### XM-FTP-GET

Type: run routine Routine: GET^XMAFTP

Menu Text: GET (Retrieve) File from Remote System

The XM-FTP-GET option allows a user to GET a file from another system using the File Transfer Protocol (FTP) protocol. The user supplies all the information about where the file is located and MailMan creates a file that, when executed, will do the retrieval. The actual process of getting the file is handled in the background. This is the converse procedure to the Send (Put) File to Remote Location (i.e., XM-FTP-PUT).

#### XM-FTP-PUT

Type: run routine Routine: PUT^XMAFTP

Menu Text: Send (Put) File to Remote Location

The XM-FTP-PUT option allows a user to PUT a file on another system using the FTP protocol. The user supplies all the information about where the file should go and MailMan creates a file that when executed will do the sending. The actual process of putting the file is handled in the background. This is the converse procedure to the GET (Retrieve) File from Remote System (i.e., XM-FTP-GET)

#### XM-NEW-FEATURES

Type: action

Menu Text: New Features in MailMan

Entry Action: S XQH="XM-NEW-FEATURES" D EN^XQH

The XM-NEW-FEATURES option is located on the Help (User/Group Info., etc.) menu \[XMHELP\]. It displays a Help Frame that lists and describes features found in MailMan V. 8.0. Many users do not get MailMan manuals. Therefore, it is very important that this sort of documentation be available online.

#### XMASSUME

Type: run routine Routine: ASSUME^XMVSURR

Menu Text: Become a Surrogate (SHARED,MAIL or Other)

Synonym: AML

Entry Action: D CHECKIN^XM

Exit Action: D CHECKOUT^XM

The XMASSUME option is located on the MailMan Menu \[XMUSER\]. It allows the user to act as a surrogate for another user or for SHARED,MAIL. Before you can act as a surrogate for another user, that user *must* indicate permission by granting you surrogate privileges through his USER OPTIONS EDIT. You will then be able to read, answer, and send mail for that user, depending on the level of access (READ/WRITE) that you were granted.

You may assume the identity of a special user, "SHARED,MAIL," to read messages of general interest. You will be able to read and respond to messages there, but you will not be able to send any. If you have been given the XMNOPRIV key, you will not be able to access "SHARED,MAIL."

SHARED,MAIL is a place to send messages of general interest. Almost all users may access this area. When you send messages to SHARED,MAIL, you *must* indicate a BASKET to deliver the messages to so that helps others find yours. Do not create new BASKETS unless it is really necessary. Try to fit your message into a basket that already exists. SHARED, MAIL is a LIBRARY, *not* a repository for trivial or personal communications. Please respect your privilege to be SHARED,MAIL surrogate. The PRIVILEGE to be a SURROGATE of SHARED,MAIL can be taken away.

#### XMAUTOPURGE

Type: run routine Routine: EN^XMA3

Menu Text: Automatic Purge of MailMan Messages

The XMAUTOPURGE option automatically purges unreferenced MailMan messages, that is, it deletes from the MESSAGE file (#3.9) any messages which are not in anyone's basket.

|                                                   |                                                                                                               |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/053.png) | CAUTION: It is *strongly* recommended that this option be scheduled to run daily, right after option XMCLEAN. |

The following messages are considered "referenced" and are not purged:

- Messages in user baskets
- Messages in transit (arriving or being sent)
- Server messages
- Messages being edited (including aborted edits)
- Messages which have been latered

The following fields in the MAILMAN SITE PARAMETERS file (#4.3), influence the behavior of this option:

- NO-PURGE DAYS BUFFER (#4.301)—MailMan does not purge any messages created or received in the last few days. Users choose how many days. The default is 2.
- NO-PURGE DAYS BUFFER (LOCAL) (#142)—MailMan does not purge local messages created in the last few days. Users choose how many days. The default is 7.
- WEEKDAY DAYS TO PURGE (#4.304)—On Saturdays, MailMan goes through the entire MESSAGE file (#3.9) looking for messages to purge. On the other days of the week, however, MailMan has the option of only looking at messages created or received recently. Users choose how many days. The default is to go through the entire MESSAGE file (#3.9).

|                                                   |                                                                                                                                                                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/054.png) | CAUTION: It is *strongly* recommended that you set this field to something reasonable (e.g., 30 to 60 days. But, only if you follow the recommendation to schedule this option to run daily; otherwise, leave this field blank. |

- AUTOMATIC INTEGRITY CHECK (#4.303)—MailMan gives users the option of running the MAILBOX file (#3.7) portion of the integrity checker (i.e., XMUT-CHKFIL option) before it actually purges the unreferenced messages. The MUMPS cross-reference on the MAILBOX file (#3.7) is used to determine whether a message is referenced (in someone's basket) or not. If the MUMPS cross-reference is incorrect, then the purge could delete messages it should not, or leave messages that it should delete. The integrity checker ensures that the MUMPS cross-reference is correct. Users choose whether to run it or not. The default is to run it. The recommendation is to run it; however, if you find that it is simply taking too long, you can choose not to run it. If you choose not to run it, then it is recommended that you schedule the XMUT-CHKFIL option to run monthly, because globals can and do become corrupted.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/055.png) | NOTE: This option is *not* assigned to a menu. |

#### XMBANNER

Type: run routine Routine: BANNER^XMVVITA

Menu Text: Banner Edit

The XMBANNER option is located on the Personal Preferences menu \[XM PERSONAL MENU\]. It enables a user to edit his "banner" message for MailMan. When messages are addressed to users with banners, their banners may be displayed.

#### XMBASKLIST

Type: run routine Routine: LISTMBOX^XMJBL

Menu Text: Mailbox Contents List

The XMBASKLIST option is located on the Other MailMan Functions menu \[XMOTHER\]. It prints/displays a list of all messages in all/one of your mail baskets. The list is sorted by basket name, and within basket, by message index number.

#### XMBLOBSEND

Type: run routine Routine: BLOB^XMA2B

Menu Text: Send Multimedia Message

Entry Action: K XMLOAD,XMDF S XMMENU(0)="XMUSER" D LOCK^XM

Exit Action: D UNLOCK^XM K XMMENU

Lock: XMBLOB

The XMBLOBSEND option is used to send MailMan multimedia messages (i.e., VistA Imaging software). Messages can be sent to other users or groups of users. The sender of the message may request a confirmation message to be sent when each recipient reads the message. This option is locked with the XMBLOB security key.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/056.png) | NOTE: This option is *not* assigned to a menu. |

#### XMCHRIS

Type: run routine Routine: CHRISTEN^XMUCHRIS

Menu Text: Christen a domain

The XMCHRIS option is located on the Network Management menu \[XMNET\]. It is used to christen a domain, which is required before that domain can send or receive networked mail. The subordinate domain *must* first be initialized with the "initialize site" option at the local domain. Then this option *must* be selected in order to establish the network relationship.

#### XMCLEAN

Type: run routine Routine: CLEAN^XMA3

Menu Text: Clean out waste baskets

The XMCLEAN option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It deletes all messages in users' WASTE baskets in the MAILBOX file (#3.7). It does *not* delete the messages in the MESSAGE file (#3.9). It is recommended that this option be scheduled to run daily, immediately before the XMAUTOPURGE option.

#### XMDX

Type: menu

Menu Text: Diagnostics

The XMDX menu contains diagnostic options, allowing the testing of various components of the MailMan system. It contains the following options:

- XMDXNAME
- XMDXSMTP
- XMDXPROT
- XMDXSCRIPT
- XMPOST
- XMDXMODEM

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/057.png) | NOTE: This option is *not* assigned to a menu. |

|                                                                                                                |                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/058.png) | NOTE: The XMDX option *cannot* be independently invoked and is for developer/support debugging only. |

#### XMDXMODEM

Type: run routine Routine: DIALER^XMCD

Menu Text: Modem Autodialer test

The XMDXMODEM option is located on the Diagnostics menu \[XMDX\]. It tests the modem, allowing the user to dial and hang up the modem to insure that the DEVICE and TERMINAL TYPE entries are correct.

#### XMDXNAME

Type: run routine Routine: DX^XMA21

Menu Text: Name Server

The XMDXNAME option is located on the Diagnostics menu \[XMDX\]. It tests the MailMan Name Server, allowing the user to repeatedly enter recipient names, after which the option will show the resolution of the name.

#### XMDXPROT

Type: action Routine: C^XML

Menu Text: Physical link protocol

Entry Action: Q

The XMDXPROT option is located on the Diagnostics menu \[XMDX\]. It sends a line of text to the terminal, allowing the user to respond with the appropriate response.

#### XMDXSCRIPT

Type: run routine Routine: TRAN^XMCD

Menu Text: Script processor

The XMDXSCRIPT option is located on the Diagnostics menu \[XMDX\]. It tests a script by sending a "dummy" message and measuring error rates and transmission speeds.

#### XMDXSMTP

Type: run routine Routine: SMTP^XMCD

Menu Text: Simple Mail Transfer Protocol

The XMDXSMTP option is located on the Diagnostics menu \[XMDX\]. It allows the user to enter information directly into the Simple Mail Transfer Protocol (SMTP) receiver from the keyboard. See the "ARPA" manual for further description of the protocol, or enter "HELP" during the protocol.

#### XMEDIT-DOMAIN-VALIDATION#

Type: run routine Routine: VAL^XMCE

Menu Text: Validation Number Edit

The XMEDIT-DOMAIN-VALIDATION# option is located on the Transmission Management Menu \[XMNET-TRANSMISSION-MANAGEMENT\]. It allows sites to edit the validation numbers so that they can be synchronized. The sender and the receiver *must* edit the numbers concurrently. At S1.MED.VA.GOV they edit S2.MED.VA.GOV's validation number. At S2.MED.VA.GOV they edit S1.MED.VA.GOV's validation number. The same number is used for input at both sites.

#### XMEDIT-REMOTE-USER

Type: run routine Routine: REMOTES^XMDIR1B

Menu Text: Enter/Edit Remote User

The XMEDIT-REMOTE-USER option is located on the Remote MailLink Directory Menu \[XMMGR-DIRECTORY MAIN\]. It allows a single person's remote address to be put into the Remote User Directory so messages can be automatically addressed to him or her.

#### XMEDITBUL

Type: edit

Menu Text: Bulletin edit

The XMEDITBUL option is located on the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. It allows a user to interactively enter/edit a MailMan bulletin, change the routing information, and document the bulletin.

#### XMEDITDIST

Type: edit

Menu Text: Edit Distribution List

The XMEDITDIST option is located on the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. It is used to edit a Distribution list. Distribution lists can be entered as part of the delivery list for messages in mail groups. They consist of a name and a list of domains that are concatenated to the name for delivery of a message to multiple mailboxes, each of which has the same name that exists at different domains.

For example, if the name is G.SUPPORT (it could be Postmaster) and the domains are FORUM.VA.GOV and EXAMPLEVAMC.MED.VA.GOV, the message will be delivered to:

- G.SUPPORT@FORUM.VA.GOV
- G.SUPPORT@EXAMPLEVAMC.MED.VA.GOV

Each distribution list can be added to more than one mail group. Each mail group can point at more than one distribution list.

#### XMEDITFWD

Type: run routine Routine: FORWARD^XMVVITA

Menu Text: Forwarding Address Edit

The XMEDITFWD option is located on the Personal Preferences menu \[XM PERSONAL MENU\]. It enables the user to edit his forwarding address.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/059.png) | NOTE: This option may or may not be available to users. It depends on whether or not the site restricts access to this option to users holding the XMNET security key. For example, if the site requires users to hold the XMNET security key and a user does *not* hold that key, they will *not* be able to use this option. |

#### XMEDITMG

Type: edit

Menu Text: Mail Group Edit

The XMEDITMG option is located on the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. It is used to edit the MAIL GROUP file (#3.8), which controls the distribution of messages to groups of users.

#### XMEDITPERSGROUP

Type: run routine Routine: PERSONAL^XMVGROUP

Menu Text: Personal Mail Group Edit

The XMEDITPERSGROUP option is located on the Personal Preferences menu \[XM PERSONAL MENU\]. It allows the user to create or edit a personal mail group. A personal mail group is a group that only the user can access, to use in addressing mail. Members *cannot* remove themselves. The difference between a personal mail group and a private mail group is that the personal mail group is restricted in its use and joining.

#### XMEDITSURR

Type: run routine Routine: SURR^XMVVITA

Menu Text: Surrogate Edit

The XMEDITSURR option is located on the Personal Preferences menu \[XM PERSONAL MENU\]. It enables you to edit your surrogate list, that is, to choose who may act as a surrogate for you in MailMan, and which privileges (READ and/or SEND) you wish to grant them.

#### XMEDITUSER

Type: run routine Routine: EDIT^XMVVITA

Menu Text: User Options Edit

The XMEDITUSER option is located on the Personal Preferences menu \[XM PERSONAL MENU\]. It enables the user to edit various fields, which identify the user and specify their MailMan preferences. The following preference field settings are included:

- Banner
- Message Display Order (Oldest/Newest First)
- Message Reader (Classic/Full Screen)
- Message Reader Prompt (ask/use default)
- Show Message Preview (used in conjunction with the Classic message reader)
- Message Action Default (Ignore/Delete)
- Ask Basket
- Show Titles
- Priority Responses Flag
- Priority Responses Prompt
- P-MESSAGE from
- MailMan Institution
- Network Signature (three lines)
- Introduction
- Preferred Editor
- Address (line one, line two, line three, city, state, and zip code)
- Phone
- Fax
- Pager
- Additional Phones

#### XMENROLL

Type: run routine Routine: ENROLL^XMVGROUP

Menu Text: Enroll in (or Disenroll from) a Mail Group

Synonym: GML

The XMENROLL option is located on both the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\] and the Personal Preferences menu \[XM PERSONAL MENU\].

The Enroll in (or Disenroll from) a Mail Group option \[XMENROLL \] allows a MailMan user to enroll in (join) or disenroll from a mail group when the group allows self-enrollment (i.e., the "SELF ENROLLMENT ALLOWED?" flag is set to "Yes"). If the user is already a member of a group, then this option allows the user to leave the group.

If a mail group does *not* allow self-enrollment (i.e., MailMan indicates that "...Self Enrollment Not Allowed." after a mail group name) and the DROP OUT OF RESTRICTED GROUP field (#22) in the MAILMAN SITE PARAMETERS file (#4.3) is set to "No," users *must* contact the Mail Group Coordinator or Organizer for that particular mail group and ask either to be enrolled in or disenrolled from the mail group.

|                                                                                                                |                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/060.png) | REF: For more information on the Mail Group Coordinator, Organizer, and general mail group information, please refer to the "How to Obtain Mail Group Information" topic in Chapter 12, "Online Help/Information," in the *MailMan User Guide*. |

The DROP OUT OF RESTRICTED GROUP field (#22) in the MAILMAN SITE PARAMETERS file (#4.3) is a site-configurable parameter and is used to allow users to drop out (disenroll) of non-self-enrolling mail groups:

- YES—Users are warned that this is a non-self-enrolling group, and that they will *not* be allowed to rejoin later; users will be asked to re-confirm the decision to drop out.
- NO (default)—Users will have to contact IRM or the mail group Coordinator or Organizer to ask to be dropped.

#### XMHELP

Type: menu

Menu Text: Help (User/Group Info., etc.)

The XMHELP menu is a submenu located on the MailMan Menu \[XMUSER\]. It includes the following help options for users:

- XMHELPUSER
- XMHELPGROUP
- XMHELPLNK
- XM-NEW-FEATURES
- XMHELPALL
- XMHELPQUEST
- XMHELP-ON-LINE-USER_MANUAL

#### XMHELP-ON-LINE-USER_MANUAL

Type: action

Menu Text: Manual for MailMan Users

Entry Action: S XQHFY="XMHELP-MANUAL" D ACTION^XQH4

The XMHELP-ON-LINE-USER_MANUAL option is located on the Help (User/Group Info., etc.) menu \[XMHELP\]. It displays the MailMan online User Guide.

#### XMHELPALL

Type: action

Menu Text: General MailMan Information

Entry Action: S XQH="XMHELP" D EN^XQH

The XMHELPALL option is located on the Help (User/Group Info., etc.) menu \[XMHELP\]. It is a general Help Frame that provides a brief description about what MailMan is and does. It is a good starting point for the beginner MailMan user.

#### XMHELPGROUP

Type: run routine Routine: HELP^XMHIG

Menu Text: Group Information

The XMHELPGROUP option is located on the Help (User/Group Info., etc.) menu \[XMHELP\]. It enables the user to get detailed information about mail groups.

#### XMHELPLNK

Type: run routine Routine: R^XMJMT

Menu Text: Remote User Information

The XMHELPLNK option is located on the Help (User/Group Info., etc.) menu \[XMHELP\]. It enables the user to inquire into the REMOTE USER DIRECTORY file (#4.2997).

#### XMHELPQUEST

Type: action

Menu Text: Questions and Answers on MailMan

Entry Action: S XQH="XM-U-H-QUESTIONS" D EN^XQH

The XMHELPQUEST option is located on the Help (User/Group Info., etc.) menu \[XMHELP\]. It poses and answers frequently asked questions concerning MailMan.

#### XMHELPUSER

Type: run routine Routine: HELP^XMHIU

Menu Text: User Information

The XMHELPUSER option is located on the Help (User/Group Info., etc.) menu \[XMHELP\]. It enables the user to get detailed information about other MailMan users.

#### XMKSP

Type: edit

Menu Text: MailMan Site Parameters

The XMKSP option is located on the Manage Mailman Menu \[XMMGR\]. It allows a site manager to edit the fields in the MAILMAN SITE PARAMETERS file (#4.3) that do not have to do with christening. To christen a domain, use the Christen a domain option (i.e., XMCHRIS). XMCHRIS also allows you to change fields set during the original christening if they are wrong. You can also use VA FileMan to edit the TRANSMISSION SCRIPT file (#4.6), if the scripts for Austin or the MINI engine need to be changed.

#### XMLATER-EDIT

Type: run routine Routine: EDIT^XMJMD

Menu Text: Change/Delete Latered Messages

The XMLATER-EDIT option is located on the Other MailMan Functions menu \[XMOTHER\]. It enables the user to delete or change the date/time that a message is scheduled to become new.

#### XMLATER-REPORT

Type: run routine Routine: REPORT^XMJMD

Menu Text: Report on Latered Messages

The XMLATER-REPORT option is located on the Other MailMan Functions menu \[XMOTHER\]. It prints/displays an overview of all of the user's "latered" messages.

#### XMLIST

Type: run routine Routine: LIST^XMCXT

Menu Text: List a transcript

The XMLIST option is located on the Queue Management menu \[XMNET-QUEUE-MANAGEMENT\]. It lists the transcript for a previously played script.

#### XMMASTER

Type: menu

Menu Text: MailMan Master Menu

The XMMASTER menu is the MailMan menu with all the addressable options:

- Manage Mailman (Utilities)—XMMGR
- Network Management—XMNET
- User Options—XMUSER

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/061.png) | NOTE: This option is *not* assigned to a menu. |

#### XMMGR

Type: menu

Menu Text: Manage Mailman

Entry Action: D CHECKIN^XM S XMMENU(0)="XMUSER"

Exit Action: K XMMENU D CHECKOUT^XM

The XMMGR menu is located on the MailMan Master Menu \[XMMASTER\]. It provides options that allow the site manager to manage the MailMan system, by manipulating the MESSAGE (#3.9), MAIL GROUP (#3.8), BULLETIN (#3.6), and MAILBOX (#3.7) files. It includes the following options:

Select Systems Manager Menu Option: Manage Mailman

Check MailMan Files for Errors \[XMUT-CHKFIL\]

Create a Mailbox for a user \[XMMGR-NEW-MAIL-BOX\]

Disk Space Management ... \[XMMGR-DISK-SPACE-MANAGEMENT\]

Group/Distribution Management ... \[XMMGR-GROUP-MAINTENANCE\]

Local Delivery Management ... \[XMMGR-MESSAGE-DELIVERY-MGT\]

MailMan Site Parameters \[XMKSP\]

Network Management ... \[XMNET\]

New Features for Managing MailMan \[XMMGR-HELP\]

Remote MailLink Directory Menu ... \[XMMGR-DIRECTORY-MAIN\]

Super Search Message File \[XM SUPER SEARCH\]

<span id="_Toc142203707" class="anchor"></span>Figure 5‑2. Manage Mailman menu \[XMMGR\] options

#### XMMGR-BACKGROUND-FILER

Type: menu

Menu Text: Background Filer (XMAD)

XMMGR-BACKGROUND-FILER option is a submenu of options for the background filer. It includes the following options:

- XMMGR-START-BACKGROUND-FILER
- XMMGR-STOP-BACKGROUND-FILER
- XMMGR-CHECK-BACKGROUND-FILER
- XMSTAT

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/062.png) | NOTE: This option is *not* assigned to a menu. |

#### XMMGR-BKFILER-ACT

Type: run routine Routine: ACT^XMUT5R2

Menu Text: Active Users/Deliveries Report

The XMMGR-BKFILER-ACT option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It generates a report that lists, in half-hour intervals (that is what is in the file), active users and message deliveries made. The information comes from the MESSAGE DELIVERY STATS file (#4.2998).

#### XMMGR-BKFILER-EDIT-NORMALIZED

Type: run routine Routine: ASK^XMUT5R2

Menu Text: Edit numbers to Normalize Reports

The XMMGR-BKFILER-EDIT-NORMALIZED option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It allows the user to customize the normalized report.

#### XMMGR-BKFILER-GROUP

Type: run routine Routine: GROUP^XMUT5R2

Menu Text: Deliveries by Group

The XMMGR-BKFILER-GROUP option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It generates a report that lists, in half-hour intervals, deliveries made for each distinct delivery queue.

#### XMMGR-BKFILER-STAT

Type: run routine Routine: STAT^XMUT5R2

Menu Text: Mail Delivery Statistics Report

The XMMGR-BKFILER-STAT option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It generates a report that lists, in half-hour intervals, active users, queue waits, average response time, number of lines displayed to users, etc.

#### XMMGR-BKFILER-TABBED-STATS

Type: run routine Routine: TAB^XMUT5R2

Menu Text: Graphics Download (TAB separators)

The XMMGR-BKFILER-TABBED-STATS option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It can be used to capture a report and use the captured file in a graphics/spreadsheet software (e.g., Microsoft Excel). The data has tabs between the fields as delimiters.

#### XMMGR-BKFILER-WAIT

Type: run routine Routine: WAIT^XMUT5R2

Menu Text: Delivery Queues Wait Report

The XMMGR-BKFILER-WAIT option produces a report that lists, in half-hour intervals, the seconds that the oldest entry in a particular queue has been there. It is used to check how long it is taking to deliver messages.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/063.png) | NOTE: This option is *not* assigned to a menu. |

#### XMMGR-CHECK-BACKGROUND-FILER

Type: run routine Routine: CHECK^XMUT5

Menu Text: CHECK background filer

The XMMGR-CHECK-BACKGROUND-FILER option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It tells you if the background filer is running, and it tells how many recipients need delivery for each of the messages/responses in the queue.

#### XMMGR-DELIVERY-STATS-COLL

Type: run routine Routine: OPTION^XMUT5Q1

Menu Text: Delivery Queue Statistics Collection

The XMMGR-DELIVERY-STATS-COLL option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It collects delivery queue statistics. Schedule it through TaskMan, entering the initial time to start. Do *not* enter data in the remainder of the fields. The option will requeue itself automatically every half-hour. All data collected is stored in the MESSAGE DELIVERY STATS file (#4.2998).

#### XMMGR-DIRECTORY-ALL

Type: run routine Routine: ALL^XMDIRQST

Menu Text: Remote Directory from all Domains

The XMMGR-DIRECTORY-ALL option is located on the Remote MailLink Directory Menu \[XMMGR-DIRECTORY MAIN\]. It schedules tasks to run in the background to update the MailLink Directory, ^XMD(4.2997).

|                                                   |                                                                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/064.png) | CAUTION: Use this option cautiously, because it sends requests to all the domains for soliciting remote user directories. |

#### XMMGR-DIRECTORY-EDITGRP

Type: run routine Routine: EDIT^XMDIRQST

Menu Text: Enter/Edit Directory Request Flags by Group

The XMMGR-DIRECTORY-EDITGRP option is located on the Remote MailLink Directory Menu \[XMMGR-DIRECTORY MAIN\]. It allows the site management to control groups of Domains from which directories are requested.

#### XMMGR-DIRECTORY-GROUP

Type: run routine Routine: GROUP^XMDIRQST

Menu Text: Group eMail Directory Request

The XMMGR-DIRECTORY-GROUP option is located on the Remote MailLink Directory Menu \[XMMGR-DIRECTORY MAIN\]. It allows site management to request directories from all the Domains in a group of Domains as defined in Enter/Edit Directory Request Flags by Group option (i.e., XMMGR-DIRECTORY-EDITGRP).

#### XMMGR-DIRECTORY-LISTGRP

Type: run routine Routine: LISTGRP^XMDIRQST

Menu Text: List eMail Directory Request by Groups

The XMMGR-DIRECTORY-LISTGRP option is located on the Remote MailLink Directory Menu \[XMMGR-DIRECTORY MAIN\]. It allows the site manager to list groups created by the Group eMail Directory Request option (i.e., XMMGR-DIRECTORY-EDITGRP).

#### XMMGR-DIRECTORY-MAIN

Type: menu

Menu Text: Remote MailLink Directory Menu

Lock: XMMGR

The XMMGR-DIRECTORY-MAIN menu is located on the Manage Mailman menu \[XMMGR\]. It allows the site manager to manage the remote MailLink Directory by loading the WANG/NOAVA and the REMOTE DOMAIN USER Directories into the REMOTE USER DIRECTORY file (#4.2997). This menu is locked with the XMMGR security key.

The following options can be found on the Remote MailLink Directory Menu:

Select Manage Mailman Option: Remote MailLink Directory Menu

Enter/Edit Directory Request Flags by Group \[XMMGR-DIRECTORY-EDITGRP\]

Enter/Edit Remote User \[XMEDIT-REMOTE-USER\]

Group eMail Directory Request \[XMMGR-DIRECTORY-GROUP\]

List eMail Directory Request by Groups \[XMMGR-DIRECTORY-LISTGRP\]

Load Remote VACO (Wang/Noava) Directory \[XMMGR-DIRECTORY-VACO\]

Remote Directory from all Domains \[XMMGR-DIRECTORY-ALL\]

Request Mail Directory From a Single Domain Server \[XMMGR-DIRECTORY-SINGLE\]

<span id="_Toc142203708" class="anchor"></span>Figure 5‑3. MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\] options

This menu is locked with the XMMGR security key.

#### XMMGR-DIRECTORY-RECV

Type: server Routine: XMDIRRCV

Text: RECEIVE E-MAIL DIRECTORY FROM OTHER SITE

The XMMGR-DIRECTORY-RECV option is a server that receives a directory from another Domain and puts the entries into the REMOTE USER DIRECTORY file (#4.2997).

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/065.png) | NOTE: This option is *not* assigned to a menu. |

#### XMMGR-DIRECTORY-SEND

Type: server Routine: XMDIRSND

Menu Text: Send a Directory to requesting site

The XMMGR-DIRECTORY-SEND option is a server that sends a directory to a requesting site.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/066.png) | NOTE: This option is *not* assigned to a menu. |

#### XMMGR-DIRECTORY-SINGLE

Type: run routine Routine: SINGLE^XMDIRQST

Menu Text: Request Mail Directory From a Single Domain Server

The XMMGR-DIRECTORY-SINGLE option is located on the Remote MailLink Directory Menu \[XMMGR-DIRECTORY MAIN\]. It schedules a task to run in the background to update the MailLink Directory, ^XMD(4.2997), from a single Domain server.

#### XMMGR-DIRECTORY-VACO

Type: run routine Routine: OPTION^XMDIR1

Menu Text: Load Remote VACO (Wang/Noava) Directory

The XMMGR-DIRECTORY-VACO option is located on the Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]. It loads a file from the Host File Server (HFS). The user has the choice of running this task interactively or scheduling a batch job to update the MailLink Directory, ^XMD(4.2997),.

#### XMMGR-DISK-MANY-MESSAGE-MAINT

Type: run routine Routine: ENTER^XMAI2

Menu Text: Ask users with many messages to do maintenance

The XMMGR-DISK-MANY-MESSAGE-MAINT option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It sends messages asking users to clean out mailboxes if they have too many messages.

#### XMMGR-DISK-SPACE-MANAGEMENT

Type: menu

Menu Text: Disk Space Management

The XMMGR-DISK-SPACE-MANAGEMENT menu is a submenu located on the Manage Mailman menu (i.e., XMMGR). It contains options for managing disk space. All reports are 80 columns wide.

The following options can be found on the Disk Space Management menu:

Select Manage Mailman Option: Disk Space Management

AI x-Ref Purge of Received Network Messages \[XMMGR-PURGE-AI-XREF\]

Ask users with many messages to do maintenance \[XMMGR-DISK-MANY-MESSAGE-MAINT\]

Clean out waste baskets \[XMCLEAN\]

IN Basket Purge \[XMMGR-IN-BASKET-PURGE\]

Large Message Report \[XMMGR-LARGE-MESSAGE-REPORT\]

Message statistics \[XMSTAT\]

Purge a message \[XMMGR-PURGE-MESSAGE\]

Purge Messages by Origination Date \[XMPURGE-BY-DATE\]

Purge Unreferenced Messages \[XMPURGE\]

Recover Messages into User's IN Basket ... \[XMUT-REC-MENU\]

Terminate mail user suggestions \[XMMGR-TERMINATE-SUGGEST\]

Terminate many mail users \[XMMGR-TERMINATE-MANY\]

Terminate one mail user \[XMMGR-TERMINATE-ONE\]

<span id="_Toc142203709" class="anchor"></span>Figure 5‑4. Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\] options

#### XMMGR-GROUP-MAINTENANCE

Type: menu

Menu Text: Group/Distribution Management

The XMMGR-GROUP-MAINTENANCE menu is a submenu located on the Manage Mailman menu \[XMMGR\].

The following options can be found on the Group/Distribution Management menu:

Select Manage Mailman Option: Group/Distribution Management

Bulletin edit \[XMEDITBUL\]

Edit Distribution List \[XMEDITDIST\]

Enroll in (or Disenroll from) a Mail Group \[XMENROLL\]

Mail Group Coordinator's Edit \[XMMGR-MAIL-GRP-COORDINATOR\]

Mail Group Coordinator's Edit W/Remotes \[XMMGR-MAIL-GRP-COORD-W/REMOTES\]

Mail Group Edit \[XMEDITMG\]

Select Group/Distribution Management Option:

<span id="_Toc142203710" class="anchor"></span>Figure 5‑5. Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\] options

#### XMMGR-HELP

Type: action

Menu Text: New Features for Managing MailMan

Entry Action: S XQH="XMMG-NEW-FEATURES" D EN^XQH

The XMMGR-HELP option is located on the Manage Mailman Menu \[XMMGR\]. It provides help for site management.

#### XMMGR-IN-BASKET-PURGE

Type: run routine Routine: ENTER^XMUPIN

Menu Text: IN Basket Purge

The XMMGR-IN-BASKET-PURGE option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It purges "IN" baskets in two steps:

> 1\. In the first step messages are sent to users

> a\. Message will contain a list of messages to be purged in Step 2.

> b\. Message will contain list of actions that will prevent the purging of the listed messages.

> c\. Message will state how many days later listed messages will be purged unless the action is taken on a message-by-message basis.

> d\. The messages listed will *not* have been referenced for 30 days or the number of days in the MAILMAN SITE PARAMETERS file ("4.3), IN-BASKET-PURGE DAYS field, if it is not null.

> 2\. In the second step, the messages listed in the message from Step 1 will be purged *not* less than 30 days later unless they:

> a\. Have been saved into a basket other than the "IN" basket.

> b\. Have been referenced (read or printed) otherwise.

> c\. Are marked as NEW.

|                                                                                                                |                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| ![](mailman-version-8-technical-manual/067.png) | NOTE: This option can be run via TaskMan. |

#### XMMGR-LARGE-MESSAGE-REPORT

Type: run routine Routine: ENTER^XMUT2

Menu Text: Large Message Report

The XMMGR-LARGE-MESSAGE-REPORT option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It produces a report that lists messages that have any of the following characteristics:

- Message longer than a specified number of lines (see the LARGE MESSAGE REPORT LINES field (#8.14) in the MAILMAN SITE PARAMETERS file \[#4.3\])
- Message without an owner or only one owner.
- Messages without any text.
- Messages without any subject.

Messages on this list are of interest to site management.

#### XMMGR-MAIL-GRP-COORD-W/REMOTES

Type: run routine Routine: RCOORD^XMVGROUP

Menu Text: Mail Group Coordinator's Edit W/Remotes

The XMMGR-MAIL-GRP-COORD-W/REMOTES option is located on the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. It allows a mail group coordinator to edit the mail groups that he or she is the coordinator of (and no others). It allows edit of remote recipients.

Most mail group coordinators should be given the corresponding XMMGR-MAIL-GRP-COORDINATOR option, which does *not* allow them to edit remote recipients in the mail group to limit the responsibility for problems delivering to incorrect addresses.

#### XMMGR-MAIL-GRP-COORDINATOR

Type: run routine Routine: LCOORD^XMVGROUP

Menu Text: Mail Group Coordinator's Edit

The XMMGR-MAIL-GRP-COORDINATOR option is located on the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. It allows a mail group coordinator to edit the mail groups that he or she is the coordinator of (and no others). It does *not* allow edit of remote recipients.

Some mail group coordinators might be given the corresponding option, XMMGR-MAIL-GRP-COORD-W/REMOTES.

#### XMMGR-MESSAGE-DELIVERY-MGT

Type: menu

Menu Text: Local Delivery Management

The XMMGR-MESSAGE-DELIVERY-MGT menu is a submenu located on the Manage Mailman menu (i.e., XMMGR). It includes options for the background filer. All reports are 132 columns wide.

The following options can be found on the Local Delivery Management menu:

Select Manage Mailman Option: Local Delivery Management

Active Users/Deliveries Report \[XMMGR-BKFILER-ACT\]

CHECK background filer \[XMMGR-CHECK-BACKGROUND-FILER\]

Compile Response Time Statistics \[XMMGR-RESPONSE-TIME-COMPILER\]

Deliveries by Group \[XMMGR-BKFILER-GROUP\]

Delivery Queue Statistics Collection \[XMMGR-DELIVERY-STATS-COLL\]

Edit numbers to Normalize Reports \[XMMGR-BKFILER-EDIT-NORMALIZED\]

Graphics Download (TAB separators) \[XMMGR-BKFILER-TABBED-STATS\]

Log Response Time Toggler \[XMMGR-RESPONSE-TIME-TOGGLER\]

Mail Delivery Statistics Report \[XMMGR-BKFILER-STAT\]

New Messages and Logon Statistics \[XMMGR-NEWMESS/LOGON-STATS\]

START background filer \[XMMGR-START-BACKGROUND-FILER\]

STOP background filer \[XMMGR-STOP-BACKGROUND-FILER\]

<span id="_Toc142203711" class="anchor"></span>Figure 5‑6. Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\] options

#### XMMGR-NEW-MAIL-BOX

Type: run routine Routine: NEWMBOX^XM

Menu Text: Create a Mailbox for a user

The XMMGR-NEW-MAIL-BOX option is located on the Manage Mailman Menu \[XMMGR\]. It is only meant to be used on systems where Kernel V. 6.0 or later is *not* running (or when a repair must be made to the MAILBOX file \[#3.7\]). A mailbox is created for each new or reinstated user from Kernel V. 6.0 or later so there should be no need to use this routine unless there was an error setting up the user or there was a file degradation problem. Using this option for a user whose mailbox is partially or wholly set up will *not* cause data to be lost.

A *mailbox* can be *created* or *repaired* using this option.

#### XMMGR-NEWMESS/LOGON-STATS

Type: run routine Routine: XMUT5R1

Menu Text: New Messages and Logon Statistics

The XMMGR-NEWMESS/LOGON-STATS option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It prints the number of new messages created, logons, and logon minutes for a specified time period.

#### XMMGR-PURGE-AI-XREF

Type: run routine Routine: XMUTPUR0

Menu Text: AI x-Ref Purge of Received Network Messages

The XMMGR-PURGE-AI-XREF option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It maintains the "AI" cross-reference of mail messages. This is the cross-reference of messages received across the network and it prevents duplicate messages from being received again. The default number of days kept is 730 (2 years—the amount of days messages can exist before being purged on FORUM). As per MailMan Patch XM\*8.0\*38, this option should be run interactively at least once a year to reduce its size; otherwise, it continues to grow.

#### XMMGR-PURGE-MESSAGE

Type: run routine Routine: MESSAGE^XMUTERM

Menu Text: Purge a message

The MMGR-PURGE-MESSAGE option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It enables you to purge any message. Purge means:

- Delete the message from all user mailboxes.
- Delete the message from the MESSAGE file, ^XMB(3.9,.
- Delete all responses from the MESSAGE file, ^XMB(3.9,.
- Delete the message from the MESSAGES TO BE NEW AT A LATER DATE file (#3.73).

|                                                   |                                                                  |
|---------------------------------------------------|------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/068.png) | CAUTION: Purge is *not* reversible. The message is gone forever. |

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/069.png) | NOTE: This option is *not* assigned to a menu. |

#### XMMGR-RESPONSE-TIME-COMPILER

Type: run routine Routine: GO^XMUT5C

Menu Text: Compile Response Time Statistics

The XMMGR-RESPONSE-TIME-COMPILER option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It is used as a background job scheduled every day to collect statistics on the previous day's response time and put the data into the MESSAGE DELIVERY STATS file (#4.2998). It will then KILL off the associated %ZRTL global nodes.

#### XMMGR-RESPONSE-TIME-TOGGLER

Type: run routine Routine: LOGON^XMUT5C

Menu Text: Log Response Time Toggler

The XMMGR-RESPONSE-TIME-TOGGLER option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It does the following:

> 1\. Turns *on* the Kernel system parameter for response time logging shortly after each half-hour.

> 2\. Schedules another task to turn *off* the Kernel system parameter for response time logging, unless the time is between 4:00 p.m. and 8:00 a.m. During these hours, response time logging remains "on" unless site management intercedes by canceling the tasks associated with this phenomenon and edits the LOG RESPONSE TIME field for the appropriate VOLUME SET to be "off."

#### XMMGR-START-BACKGROUND-FILER

Type: run routine Routine: START^XMKPL

Menu Text: START background filer

The XMMGR-START-BACKGROUND-FILER option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It reverses the action that was taken when the converse procedure (i.e., XMMGR-STOP-BACKGROUND-FILER option) has been run. It also will restart the background filer, if it disappears from the system status report. In order for this option to be effective, TaskMan (ZTM) *must* be running.

#### XMMGR-STOP-BACKGROUND-FILER

Type: run routine Routine: STOP^XMKPL

Menu Text: STOP background filer

The XMMGR-STOP-BACKGROUND-FILER option is located on the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. It is used to *stop* the background filer "gently" at the *end* of a delivery *before* it starts to deliver any further messages. This only stops local delivery operations. This is the converse procedure to the START background filer option (i.e., XMMGR-START-BACKGROUND-FILER).

|                                                   |                                                                                                                                                       |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/070.png) | CAUTION: All local mail delivery will stop until the XMMGR-START-BACKGROUND-FILER option is run. This option stops delivery of local mail gracefully. |

#### XMMGR-TERMINATE-MANY

Type: run routine Routine: ALL1^XMUTERM

Menu Text: Terminate many mail users

The XMMGR-TERMINATE-MANY option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It goes through the MAILBOX file (#3.7) and removes any mailbox if the user:

- Is not in the NEW PERSON file (#200).
- Has no Access code and was *not* terminated.
- Has no Access code and was terminated without mailbox retention.
- Has an Access code, but no primary menu.
- Has an Access code and primary menu, but no Verify code, *and*:
- Has never signed on or used mail since being added before a cutoff date.

> OR

- Last signed on or used mail before a cutoff date.

However, if the user meets one of the last two conditions above, but has a forwarding address, the user's mailbox will *not* be removed. The fact will be noted on the report, and the user should be investigated further.

Remove means:

- Delete user's private mail groups.
- Remove user from membership in all groups.
- Remove user as an authorized sender from all groups.
- Remove user from anyone's list of surrogates.
- Delete user's latered-messages list.
- Delete user's mailbox.

As a result, the user will not receive any mail.

This option can be run in "test" or "real" mode.

The report lists, in DUZ order:

- The user's DUZ and name.
- Whether the user has an Access code, Verify code, and primary menu.
- When the user was added to the NEW PERSON file (#200).
- When the user last signed on or used mail.
- When the user was terminated (if applicable).
- If the user was terminated, then whether the site manager chose to delete the user's mailbox. (It's generally a good idea to go ahead and delete the mailbox upon termination.)
- If the user has an access code and a forwarding address, the user is marked with "\*\*\*," and the forwarding address is shown. (Again, the mailbox is not deleted in this case, but the user should be investigated further.)

#### XMMGR-TERMINATE-ONE

Type: run routine Routine: CHOOSE^XMUTERM

Menu Text: Terminate one mail user

The XMMGR-TERMINATE-ONE option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It lets you remove the mailbox of any user who meets the criteria of either the XMMGR-TERMINATE-MANY option or the XMMGR-TERMINATE-SUGGEST option.

Remove means:

- Delete user's private mail groups.
- Remove user from membership in all groups.
- Remove user as an authorized sender from all groups.
- Remove user from anyone's list of surrogates.
- Delete user's "latered"-messages list.
- Delete user's mailbox.

As a result, the user will not receive any mail.

Remember:

- Whenever you give a user a new Access code, the system gives the user a mailbox, if he does not already have one.
- Whenever a user logs on, the system gives the user a mailbox, if he does not already have one.

#### XMMGR-TERMINATE-SUGGEST

Type: run routine Routine: ALL2^XMUTERM

Menu Text: Terminate mail user suggestions

The XMMGR-TERMINATE-SUGGEST option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It goes through the MAILBOX file (#3.7) and reports on users who *perhaps* should have their mail access terminated.

Users are included in the report if:

- The user was terminated before a manager-supplied cutoff date and allowed to keep a mailbox.
- The user has an access code, verify code, and primary menu, but last signed on before a manager-supplied cutoff date.

This option does *not* terminate mail access.

The report page breaks on Service/Section and includes the following information:

- User's DUZ and name.
- Whether the user has an Access code, a Verify code, and a primary menu.
- When the user last signed on or used mail.
- When the user was terminated (if applicable).
- If the user was terminated, then whether the site manager chose to delete the user's mailbox. (Remember, you should usually answer "Yes" to this question, unless the user is coming back and needs to have his mail retained.)
- Whether the user was DISUSER'd.
- How many new messages the user has. (New messages are never purged, except during purge-by-date purges.)
- If the user has any surrogates, the first surrogate is shown.
- If the user has an access code and a forwarding address, the forwarding address is shown.

Besides being of interest to the site manager, this report is also designed to be submitted to other services. The intent is that the other services would check each of their users listed in the report, annotate whether MailMan or VistA access should be terminated, and return the report to the site manager for action.

#### XMNET

Type: menu

Menu Text: Network Management

Entry Action: D CHECKIN^XM

Exit Action: D CHECKOUT^XM

The XMNET menu is a submenu located on the MailMan Master Menu \[XMMASTER\] and Manage Mailman Menu \[XMMGR\]. It allows the user to control the network: editing/playing/listing scripts, managing domains, christening subordinate domains, and controlling pollers.

The following options can be found on the Network Management menu:

Select Manage Mailman Option: Network Management

Christen a domain \[XMCHRIS\]

Compare Domains in System Against Released List \[XMQDOMAINS\]

Network Help \[XMNETHELP\]

Queue Management ... \[XMNET-QUEUE-MANAGEMENT\]

Site Parameters \[XMSITE\]

Transmission Management ... \[XMNET-TRANSMISSION-MANAGEMENT\]

<span id="_Toc142203712" class="anchor"></span>Figure 5‑7. Network Management menu \[XMNET\] options

|                                                                                                                |                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/071.png) | REF: The options located on the Network Management menu are discussed in depth in the *MailMan Network Reference Guide*. |

#### XMNET-QUEUE-MANAGEMENT

Type: menu

Menu Text: Queue Management

The XMNET-QUEUE-MANAGEMENT menu is a submenu located on the Network Management menu \[XMNET\]. It is used for queue management. It includes the following options:

Select Queue Management Option:

Actively Transmitting/Receiving Queues Report \[XMQACTIVE\]

Display Active & Inactive Message Queues \[XMQDISP\]

\*\*\> Locked with XUPROGMODE

Historical Queue Data/Stats Report \[XMQHIST\]

List a transcript \[XMLIST\]

Queues with Messages to Transmit Report \[XMQUEUED\]

Show a queue \[XMQSHOW\]

Transmit a Single Queue \[XMSTARTQUE\]

Transmit All Queues \[XMSTARTQUE-ALL\]

<span id="_Toc142203713" class="anchor"></span>Figure 5‑8. Queue Management menu \[XMNET-QUEUE-MANAGEMENT\] options

#### XMNET-TRANSMISSION-MANAGEMENT

Type: menu

Menu Text: Transmission Management

The XMNET-TRANSMISSION-MANAGEMENT menu is a submenu located on the Network Management menu \[XMNET\]. It includes the following options having to do with network transmissions:

Select Transmission Management Option:

Edit a script \[XMSCRIPTEDIT\]

Play a script \[XMSCRIPTPLAY\]

Receive Messages from Another UCI \[XMR-UCI-RCV\]

Send Messages to Another UCI \[XMR-UCI-SEND\]

Sequential Media Message Reception \[XMR-SEQ-RECEIVE\]

Sequential Media Queue Transmission \[XMS-SEQ-TRANSMIT\]

Subroutine editor \[XMSUBEDIT\]

Toggle a script out of service \[XMSCRIPTOUT\]

Validation Number Edit \[XMEDIT-DOMAIN-VALIDATION#\]

<span id="_Toc142203714" class="anchor"></span>Figure 5‑9. Transmission Management menu \[XMNET-TRANSMISSION-MANAGEMENT\] options

#### XMNET-TWIX-SEND

Type: run routine Routine: XMRPCTS

Menu Text: Send a TWIX via PCTS

The XMNET-TWIX-SEND option is to be used to send messages formatted especially as TWIXs to be sent via the PCTS system.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/072.png) | NOTE: This option is *not* assigned to a menu. |

#### XMNET-TWIX-TRANSMIT

Type: run routine Routine: RQ^XMRPCTS0

Menu Text: Transmit TWIX's

The XMNET-TWIX-TRANSMIT option can be run interactively or scheduled as a task to run in the background to transmit TWIXs (PCTS messages) over the network.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/073.png) | NOTE: This option is *not* assigned to a menu. |

#### XMNETHELP

Type: action

Menu Text: Network Help

Entry Action: S XQH="XMNETWORK\*" D EN^XQH

The XMNETHELP option is located on the Network Management menu \[XMNET\]. It displays all network-related help frames.

#### XMNEW

Type: run routine Routine: NEW^XMJBN

Menu Text: New Messages and Responses

Synonym: NML

Entry Action: D CHECKIN^XM

Exit Action: D CHECKOUT^XM

The XMNEW option is located on the MailMan Menu \[XMUSER\]. It enables you to scan your mailbox for messages which are either new, or have had some unseen response.

#### XMOTHER

Type: menu

Menu Text: Other MailMan Functions

The XMOTHER menu is a submenu located on the MailMan Menu \[XMUSER\]. It contains other MailMan functions for special user activities. It includes the following options:

Select Other MailMan Functions Option:

Report on Latered Messages \[XMLATER-REPORT\]

Change/Delete Latered Messages \[XMLATER-EDIT\]

Mailbox Contents List \[XMBASKLIST\]

LML Load PackMan Message \[XMPACK\]

\*\*\> Locked with XUPROGMODE

<span id="_Toc161642819" class="anchor"></span>Figure 5‑10. Other MailMan Functions menu \[XMOTHER\] options

#### XMOTHER-COMMUNICATIONS

Type: Menu

Menu Text: Communications

Lock: XMNET

The XMOTHER-COMMUNICATIONS menu is a submenu that contains options that allow users to send and receive data that is not necessarily in an electronic mail message form. FTP options to get and put files are here. It includes the following options:

- XM-FTP-GET
- XM-FTP-PUT

This option is locked with the XMNET security key.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/074.png) | NOTE: This option is *not* assigned to a menu. |

#### XMPACK

Type: run routine Routine: PAKMAN^XMJMS

Menu Text: Load PackMan Message

Synonym: LML

Entry Action: D CHECKIN^XM

Exit Action: D CHECKOUT^XM

Lock: XUPROGMODE

The XMPACK option is located on the Other MailMan Functions menu \[XMOTHER\]. It enables the user to create a PackMan message. This option is locked with the XUPROGMODE security key. It provides the following functions:

- ROUTINE LOAD
- GLOBAL LOAD
- PACKAGE LOAD
- SUMMARIZE MESSAGE
- PRINT MESSAGE
- INSTALL/CHECK MESSAGE
- INSTALL SELECTED ROUTINE(S)
- TEXT PRINT/DISPLAY
- COMPARE MESSAGE

#### XMPCOM

Type: run routine Routine: XC^XMP2

Menu Text: Compare message

The XMPCOM option compares the message with the currently installed version of the software, informing the user of the differences on a line-by-line basis.

#### XMPGLO

Type: run routine Routine: LOAD^XMPG

Menu Text: Global load

The XMPGLO option loads data into the message from the global subtree indicated.

#### XMPINS

Type: run routine Routine: XI^XMP2

Menu Text: Install Package & Run Inits

The XMPINS option installs the software (package) contained in the message into the active area. It permanently updates the routines, globals, and files in doing so.

#### XMPOLL

Type: run routine Routine: POLL^XMCP

Menu Text: POLL REMOTE NODES

The XMPOLL option plays the scripts to Domains whose flags contain a "P."

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/075.png) | NOTE: This option is *not* assigned to a menu. |

#### XMPOST

Type: run routine Routine: BULLETIN^XMJMBULL

Menu Text: Post a bulletin

The XMPOST option is located on the Diagnostics menu \[XMDX\]. It allows a user to manually post a bulletin to test its operation.

#### XMPPRT

Type: run routine Routine: XP^XMP2

Menu Text: Print message (formatted)

The XMPPRT option prints the message in a neatly formatted form. Global data is preceded by its subscript; routines are wrapped around and fitted one per page.

#### XMPRECV

Type: menu

Menu Text: Package received

The XMPRECV menu lets users print, compare, and load a PackMan message. It includes the following options (listed alphabetically):

- XMPCOM
- XMPINS
- XMPPRT
- XMPSUM

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/076.png) | NOTE: This option is *not* assigned to a menu. |

|                                                                                                                |                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/077.png) | NOTE: The XMPRECV option *cannot* be independently invoked. These menu options are used as PackMan options and are used from the menus executed from ^DOPT("XMP"). |

#### XMPROU

Type: run routine Routine: LOAD^XMPH

Menu Text: Routine load

The XMPROU option loads routines from the routine library to the message. Routines can be named individually, or with the traditional asterisk ("\*") notation.

#### XMPSEND

Type: menu

Menu Text: Send Package transfer (PackMan)

Lock: XUPROG

The XMPSEND menu option allows the user to use PackMan functions: load routines, globals, files, and data dictionaries. It includes the following options:

- XMPROU
- XMPGLO
- XMPSUM
- XMPPRT
- XMPCOM

It is locked with the XUPROG security key.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/078.png) | NOTE: This option is *not* assigned to a menu. |

|                                                                                                                |                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/079.png) | NOTE: The XMPSEND option *cannot* be independently invoked. These menu options are used as PackMan options and are used from the menus executed from ^DOPT("XMP"). |

#### XMPSUM

Type: run routine Routine: XS^XMP2

Menu Text: Summarize message

The XMPSUM option summarizes the message, listing each packet in the software, along with its line number. It does not list the contents in each packet; the Print option does that.

#### XMPURGE

Type: action

Menu Text: Purge Unreferenced Messages

Entry Action: D SCAN^XMA3

The XMPURGE option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It behaves as follows depending on how it is run:

- Scheduled—This option, if scheduled, does exactly what the XMAUTOPURGE option does, and then stops.
- Interactive—This option, if run interactively, does exactly what the XMAUTOPURGE option does, and then it does exactly what the XMSTAT option does, and then it stops.

|                                                   |                                                 |
|---------------------------------------------------|-------------------------------------------------|
| ![](mailman-version-8-technical-manual/080.png) | CAUTION: You should *not* schedule this option. |

#### XMPURGE-BY-DATE

Type: run routine Routine: XMA32

Menu Text: Purge Messages by Origination Date

Lock: XMMGR

The XMPURGE-BY-DATE option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It removes messages from users' mail baskets then deletes them along with any responses chained to them. It will do this for a range of messages based upon user input. The user enters the range of internal message numbers that will be processed and the date against which they will be checked. This option is locked with the XMMGR security key.

|                                                                                                                |                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/081.png) | NOTE: Any messages in the Transmit queues or the Server baskets are exempt from the date purge (i.e., XMPURGE-BY-DATE option. |

#### XMQACTIVE

Type: run routine Routine: ACTIVE^XMCQA

Menu Text: Actively Transmitting/Receiving Queues Report

The XMQACTIVE option is located on the Queue Management menu \[XMNET-QUEUE-MANAGEMENT\]. It runs a report that shows only those queues that are currently (right now) transmitting or receiving messages. It states the message numbers and the approximate line number in progress and the characters per second.

#### XMQDISP

Type: run routine Routine: STATUS^XMCQ

Menu Text: Display Active & Inactive Message Queues

The XMQDISP option is located on the Queue Management menu \[XMNET-QUEUE-MANAGEMENT\]. It reports on every active queue and every queue with messages. This option is locked with the XUPROGMODE security key.

For active queues, it shows much the same information as option XMQACTIVE (Actively transmitting queues), except that instead of the task number, it shows the date/time that the information was last updated.

For inactive queues that have messages, it shows whether or not there's a task scheduled. If there is, it tells you what time it's scheduled for. If there is not, it shows you the FLAGS field for that domain in the DOMAIN file (#4.2). By looking at the FLAGS field, you should be able to tell whether a task needs to be created to transmit the queue. Generally, if the FLAGS field contains an "S" (for SEND), and there is no task scheduled, you probably ought to schedule one, using either the XMSTARTQUE-ALL (for all queues) or XMSTARTQUE (for a queue of your choice) options.

#### XMQDOMAINS

Type: run routine Routine: VALID8^XMUDCHK

Menu Text: Compare Domains in System Against Released List

The XMQDOMAINS option is located on the Network Management menu \[XMNET\]. It compares the domains in the DOMAIN file (#4.2) with the list of domains in the XMUDCHK routine, and generates a report of domains in XMUDCHK that are not in the DOMAIN file (#4.2). Site managers should consider whether the missing domains should be added to the DOMAIN file (#4.2).

#### XMQHIST

Type: run routine Routine: ENTER^XMCQH

Menu Text: Historical Queue Data/Stats Report

The XMQHIST option is located on the Queue Management menu \[XMNET-QUEUE-MANAGEMENT\]. It reports on network transmission queues. It includes every domain in the DOMAIN file (#4.2) that has ever had any activity. It includes the total number of messages ever received from or sent to each domain, as well as the number of messages that are currently queued to be transmitted to each domain.

#### XMQSHOW

Type: run routine Routine: SHOWQ^XMCQ

Menu Text: Show a queue

The XMQSHOW option is located on the Queue Management menu \[XMNET-QUEUE-MANAGEMENT\]. It shows all of the messages awaiting transmission for a given queue.

#### XMQUEUED

Type: run routine Routine: ALL^XMCQA

Menu Text: Queues with Messages to Transmit Report

The XMQUEUED option is located on the Queue Management menu \[XMNET-QUEUE-MANAGEMENT\]. It produces a report of all those queues that have messages to go out. The list does *not* say whether there is or is not a task scheduled to send them. Requeuing them is okay, even if there is already a task to go out.

#### XMR-BROADCAST-VA-WIDE

Type: Server Routine: ENT^XMGAPI3(.6)

Menu Text: Server / not for a menu

The XMR-BROADCAST-VA-WIDE option is set up as a server. When a message is addressed to this server (i.e., S.XMR-BROADCAST-VA-WIDE), it runs routine ENT^XMGAPI3 to send the message to SHARED,MAIL. The message is marked "closed" (*cannot* forward) and "information only" (*cannot* reply). The message is marked with a vaporization date of 30 days from date of receipt.

|                                                                                                                |                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/082.png) | NOTE: The XMYB-BROADCAST-VA-WIDE server option is similar to this option, except that it sends the message to all users. |

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/083.png) | NOTE: This option is *not* assigned to a menu. |

#### XMR-SEQ-RECEIVE

Type: run routine Routine: TAPEIN^XMCB

Menu Text: Sequential Media Message Reception

Entry Action: D EN^XM

Exit Action: D CHECKOUT^XM

The XMR-SEQ-RECEIVE option is located on the Transmission Management Menu \[XMNET-TRANSMISSION-MANAGEMENT\]. It allows the receipt of a queue of messages onto sequential media. The messages are "read" into the VistA MailMan system. This is the converse procedure to the Sequential Media Queue Transmission option \[XMS-SEQ-TRANSMIT\].

#### XMR-UCI-RCV

Type: run routine Routine: GLBIN^XMCB

Menu Text: Receive Messages from Another UCI

The XMR-UCI-RCV option is located on the Transmission Management Menu \[XMNET-TRANSMISSION-MANAGEMENT\]. It reads messages from the %ZTSK global. This is the converse procedure to the Send Messages to Another UCI option \[XMR-UCI-SEND\].

To use:

> 1\. Log onto the UCI from which you wish to transmit messages.

> 2\. Use the SEND option. It will load all the messages for a particular Domain into ^%ZTSK.

> 3\. Log onto the UCI into which you wish to receive messages.

> 4\. Use this option. It will read through the %ZTSK global looking for a message to receive (do not worry, it only checks the first line of each potential message/task) and creates a message for them.

Requirements:

> 1\. The RECEIVE side needs to have been set up as a Domain.

> 2\. You *must* execute the RECEIVE option before the %ZTSK global gets cleaned out.

#### XMR-UCI-SEND

Type: run routine Routine: GLBOUT^XMCB

Menu Text: Send Messages to Another UCI

The XMR-UCI-SEND option is located on the Transmission Management Menu \[XMNET-TRANSMISSION-MANAGEMENT\]. It loads messages into the %ZTSK global. This is the converse procedure to the Receive Messages from Another UCI option \[XMR-UCI-RCV\].

#### XMREAD

Type: run routine Routine: MANAGE^XMJBM

Menu Text: Read/Manage Messages

Synonym: RML

Entry Action: D CHECKIN^XM

Exit Action: D CHECKOUT^XM

The XMREAD option is located on the MailMan Menu \[XMUSER\]. It is used to read and manage MailMan messages. The user will be asked for a mail basket, which is normally the "IN" basket. You can see deleted messages by reading the "WASTE" basket. Once read, messages can be deleted, saved into other mail baskets, forwarded to other users, edited, or queried for information regarding other recipients of the message.

#### XMRONT

Type: run routine Routine: XMRONT

Menu Text: Start XMRONT TCP Listener

The XMRONT option is the TCP/IP Listener for MailMan. This option should *not* be on any Menu and should *not* be run directly. It *must* be scheduled to start every time the system is rebooted. You can schedule this option by using the Schedule/Unschedule Options option located on the Taskman Management menu. You *must* specify the XMRONT option and then enter "STARTUP'" in the SPECIAL QUEUING field.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/084.png) | NOTE: This option is *not* assigned to a menu. |

#### XMS-SEQ-TRANSMIT

Type: run routine Routine: TAPEOUT^XMCB

Menu Text: Sequential Media Queue Transmission

Entry Action: D EN^XM

Exit Action: D CHECKOUT^XM

The XMS-SEQ-TRANSMIT option is located on the Transmission Management Menu \[XMNET-TRANSMISSION-MANAGEMENT\]. It allows the recording of a queue of messages onto sequential media. The messages so recorded can be "read" into another VistA MailMan system. This is the converse procedure to the Sequential Media Message Reception option \[XMR-SEQ-RECEIVE\].

This option has been developed specifically for emergency transmission of messages when the wide area network is not available. It can also be used for archiving.

For example, say a bulldozer knocked out your T1 line to the Wide Area Network (WAN) in front of your computer room. It will be three weeks until the system is reconnected to the network. You know that a sister installation 10 miles down the road is still on line. You must get your payroll information to Austin. The messages are ready to be sent (in the queue to REDACTED). Quick, mount a tape! Use this procedure to "transmit" the queue onto the tape. Have the tape delivered to your sister site (keeping it away from all magnetic fields—those messages are no longer in the queue). At your sister site the tape is delivered. They mount it and read in the messages. The messages are queued up for REDACTED and delivered as though they were "relayed" through this site. You could also have sent the tape directly to REDACTED where they could have been received.

#### XMSCRIPTEDIT

Type: run routine Routine: EDITSCR^XMCE

Menu Text: Edit a script

The XMSCRIPTEDIT option is located on the Transmission Management Menu \[XMNET-TRANSMISSION-MANAGEMENT\]. It allows the creation of a script for a given Domain.

#### XMSCRIPTOUT

Type: run routine Routine: OUT^XMCE

Menu Text: Toggle a script out of service

The XMSCRIPTOUT option is located on the Transmission Management Menu \[XMNET-TRANSMISSION-MANAGEMENT\]. It lets you edit the OUT OF SERVICE field for a Transmission Script in the DOMAIN file (#4.2). You can also requeue the Domain for transmission from this option.

#### XMSCRIPTPLAY

Type: run routine Routine: PLAY^XMCX

Menu Text: Play a script

The XMSCRIPTPLAY option is located on the Transmission Management Menu \[XMNET-TRANSMISSION-MANAGEMENT\]. It interprets the chosen script.

#### XMSCRIPTRES

Type: run routine Routine: RESUME^XMC1

Menu Text: Resume processing a script

The XMSCRIPTRES option allows the user to resume the interpretation of a script, with manual intervention.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/085.png) | NOTE: This option is *not* assigned to a menu. |

#### XMSEARCH

Type: run routine Routine: FIND^XMJMF

Menu Text: Query/Search for Messages

Entry Action: D CHECKIN^XM

Exit Action: D CHECKOUT^XM

The XMSEARCH option is located on the MailMan Menu \[XMUSER\]. It enables you to find messages sent by you or sent to you, based on various criteria. You may search the entire database of existing messages, regardless of whether they are in one of your baskets or not, or whether you have terminated them or not. Such a search may only be made based upon "Subject start with" a string. Your search options vastly increase if you confine your search to messages existing in one (or all) of your baskets. Such a search may be based upon any combination of the following:

- "Subject contains"
- "Sender is"
- "Message sent on or after a certain date"
- "Message sent on or before' a certain date"
- "Message sent to a certain user"

#### XMSEND

Type: run routine Routine: SEND^XMJMS

Menu Text: Send a Message

Synonym: SML

Entry Action: D CHECKIN^XM

Exit Action: D CHECKOUT^XM

The XMSEND option is located on the MailMan Menu \[XMUSER\]. It enables users to send MailMan messages. Messages can be sent to other users or groups of users. The message sender can request a confirmation message to be sent to him or her when each recipient reads the message.

#### XMSHARE

Type: run routine Routine: SHARE^XMVSURR

Menu Text: Assume the Identity of SHARED,MAIL

Entry Action: D CHECKIN^XM

Exit Action: D CHECKOUT^XM

Reverse/Negative Lock: XMNOPRIV

Use the XMSHARE option to assume the identity of a special user, SHARED,MAIL, so that you can read mail sent to the general public. Users who hold the XMNOPRIV security key *cannot* do this. SHARED,MAIL is a place to send messages of general interest. Almost all users may access this area. You *must* indicate a basket to deliver the messages to so that it helps others find your message. Do *not* create new baskets unless it is really necessary. Try to fit your message into a basket that already exists. SHARED, MAIL is a Library, *not* a repository for trivial or personal communications. Please respect your privilege to be a SHARED,MAIL surrogate. The privilege of being a surrogate of SHARED,MAIL can be taken away.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/086.png) | NOTE: This option is *not* assigned to a menu. |

#### XMSITE

Type: action

Menu Text: Site Parameters

Entry Action: S DR=".01;1;3;5;5.11:5.13;7;8.2",DIE="^XMB(1,",DA=1 D ^DIE W !!,"Editing Postmaster information" S DR="4;4.5;8",DIE="^XMB(3.7,",DA=.5 D ^DIE K DIE,DR,DA

The XMSITE option is located on the Network Management menu \[XMNET\]. It allows the network manager to control local site parameters, names, time zone, etc.

#### XMSTARTQUE

Type: run routine Routine: Q1^XMCX

Menu Text: Transmit a Single Queue

The XMSTARTQUE option is located on the Queue Management menu \[XMNET-QUEUE-MANAGEMENT\]. It attempts to send queued messages in the Postmaster's mailbox for a given Domain by creating a TaskMan job that will deliver the messages for the Domain requested. Messages can be sitting in a queue for a variety of reasons (e.g., transmission failure, waiting for Poller to run, etc.).

#### XMSTARTQUE-ALL

Type: run routine Routine: QALL^XMCX

Menu Text: Transmit All Queues

The XMSTARTQUE-ALL option is located on the Queue Management menu \[XMNET-QUEUE-MANAGEMENT\]. It creates TaskMan jobs that will transmit queued messages in the Postmaster's baskets for a number of Domains throughout the network. A Domain's queue will *not* be requeued, however, if it is already set up as a scheduled TaskMan job. Nor will it be requeued if it is empty or in the process of transmitting.

#### XMSTAT

Type: run routine Routine: STAT^XMA3

Menu Text: Message statistics

The XMSTAT option is located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. This interactive option displays information about past purges. It displays the following information:

1.  Types and results of the last 20 purges of the MESSAGE file (#3.9). It provides the following details:
- If the purge was an unreferenced message purge (XMPURGE or XMAUTOPURGE options) or a date purge (XMPURGE-BY-DATE option)
- When it started
- When it ended
- How long it took
- How many messages were purged
- How many were left
2.  Information about each user in the MAILBOX file (#3.7). It provides the following details:
- How many messages they have in their mailboxes
- When the user last logged on
- When the user last used MailMan

#### XMSUBEDIT

Type: run routine Routine: EDITSUB^XMCE

Menu Text: Subroutine editor

Entry Action: D EDITSC^XMC11

The XMSUBEDIT option is located on the Transmission Management Menu \[XMNET-TRANSMISSION-MANAGEMENT\]. It edits transmission script subroutines.

#### XMSUGGESTION

Type: run routine Routine: SEND^XMJMSA

Menu Text: Suggestion Box

The XMSUGGESTION option enables a user to send an anonymous message to the SUGGESTION BOX basket of SHARED,MAIL. If the basket does not exist, it will be created. MailMan carefully fails to record the actual identity of the sender. The option allows users to voice complaints and concerns anonymously.

To use this option, put the XMSUGGESTION option onto the appropriate menu. To stop a particular user from using it, put a "Reverse/negative Lock" onto the XMSUGGESTION option and assign that key to the user.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/087.png) | NOTE: This option is *not* assigned to a menu. |

#### XMTALK

Type: run routine Routine: TALK^XMCTLK

Menu Text: TalkMan

Lock: XMTALK

The XMTALK option allows the user to communicate with another Domain through the script processing ability of VistA MailMan. Since the Script Processing mode is transparent, the user need not know any security passwords. He only needs to know the name of the Domain and have access to the option. In addition, the script for the Domain *must* have a "T" command and the FLAGS field *must* also contain a "T". This option is locked with the XMTALK security key.

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/088.png) | NOTE: This option is *not* assigned to a menu. |

#### XMUSER

Type: menu

Menu Text: MailMan Menu

Entry Action: S XMMENU(0)="XMUSER" D EN^XM

Exit Action: K XMMENU D CHECKOUT^XM

The XMUSER menu is located on the MailMan Master Menu \[XMMASTER\]. It is the main MailMan menu for normal user interaction. It allows the user to send and receive messages, as well as manage his/her baskets.

The following options can be found on the MailMan Menu:

NML New Messages and Responses \[XMNEW\]

RML Read/Manage Messages \[XMREAD\]

SML Send a Message \[XMSEND\]

Query/Search for Messages \[XMSEARCH\]

AML Become a Surrogate (SHARED,MAIL or Other) \[XMASSUME\]

Personal Preferences ... \[XM PERSONAL MENU\]

Other MailMan Functions ... \[XMOTHER\]

Help (User/Group Info., etc.) ... \[XMHELP\]

Select MailMan Menu Option:

<span id="_Toc142203716" class="anchor"></span>Figure 5‑11. Mailman Menu \[XMUSER\] options

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/089.png) | REF: The options located on the MailMan Menu are discussed in depth in the *MailMan Getting Started Guide* and the *MailMan User Guide* and will *not* be discussed here. |

#### XMUT-CHKFIL

Type: run routine Routine: CHKFILES^XMUT4

Menu Text: Check MailMan Files for Errors

Lock: XUPROG

The XMUT-CHKFIL option is located on the Manage Mailman Menu \[XMMGR\]. It is locked with the XUPROG security key.

This option checks for and corrects errors in the MAILBOX (#3.7) and MESSAGE (#3.9) files. It checks important fields and cross references.

It is recommended that this option be run monthly or every few months, or whenever there seems to be a database problem.

It produces a report of the errors detected, and what, if anything, it did to fix them. If it did not fix the errors, it tells you what you can do to fix them.

Although the system will not fail because of errors detected, users may inquire about the problems they experience. This utility allows you to detect any errors first and correct them before anyone else encounters an error.

#### XMUT-REC-DELETE

Type: run routine Routine: DEL^XMUT1A

Menu Text: Delete Found Messages from Found Messages List

Synonym: DEL

The XMUT-REC-DELETE option is located on the Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\]. It deletes the temporary storage of a list of messages found when the user uses the Find Messages for User option \[XMUT-REC-FIND\].

#### XMUT-REC-DELIVER

Type: run routine Routine: G^XMUT1

Menu Text: Deliver Found Messages into User's IN Basket

Synonym: DRM

The XMUT-REC-DELIVER option is located on the Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\]. It is used to deliver the messages found with the Find Messages for User option \[XMUT-REC-FIND\]. The messages found with that option will be placed into the user's "IN" basket, but only if they are not already in another basket.

#### XMUT-REC-FIND

Type: run routine Routine: A^XMUT1

Menu Text: Find Messages for User

Synonym: FRM

The XMUT-REC-FIND option is located on the Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\]. It is used to find all the messages that a user has ever had and has not terminated from.

This list of messages can be used as input into two other processes:

- Deliver Found Messages into User's IN Basket option \[XMUT-REC-DELIVER\].
- List Messages Found option \[XMUT-REC-RPT\].

#### XMUT-REC-MENU

Type: menu

Menu Text: Recover Messages into User's IN Basket

The XMUT-REC-MENU option is a submenu located on the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. It lets you recover messages that have inadvertently been lost. It recovers all the messages a user has ever received and is not terminated from. The steps are reviewed in the Help documentation. (Enter "?HELP" to see the HELP documentation.).

The following options can be found on the Recover Messages into User's IN Basket menu:

Select Disk Space Management Option: Recover Messages into User's IN Basket

DEL Delete Found Messages from Found Messages List \[XMUT-REC-DELETE\]

DRM Deliver Found Messages into User's IN Basket \[XMUT-REC-DELIVER\]

FRM Find Messages for User \[XMUT-REC-FIND\]

LRM List Messages Found \[XMUT-REC-RPT\]

<span id="_Toc161642821" class="anchor"></span>Figure 5‑12. Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\] options

#### XMUT-REC-RPT

Type: run routine Routine: LIST^XMUT1A

Menu Text: List Messages Found

Synonym: LRM

The XMUT-REC-RPT option is located on the Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\]. It is used to list the messages found for users with the Find Messages for User option \[XMUT-REC-FIND\].

#### XMYB-BROADCAST-VA-WIDE

Type: Server Routine: ENT^XMGAPI3("\*")

Menu Text: Server / not for a menu

The XMYB-BROADCAST-VA-WIDE option is set up as a server. When a message is addressed to this server (i.e., S.XMYB-BROADCAST-VA-WIDE), it runs the ENT^XMGAPI3 routine to send the message to all users. The message is marked "closed" (*cannot* forward) and "information only" (*cannot* reply). To prevent broadcast messages from being delivered to a user, assign the user the XM NO BROADCASTS security key.

The message is marked with a vaporization date of seven days from the date of receipt.

|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/090.png) | NOTE: The XMR-BROADCAST-VA-WIDE server option is similar to this option, except that it sends the message to SHARED,MAIL. |

|                                                                                                                |                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-technical-manual/091.png) | NOTE: This option is *not* assigned to a menu. |

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no application-specific archiving procedures or recommendations for MailMan V. 8.0.

### Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MESSAGE file (#3.9) has the potential to grow in size over time.

The Disk Space Management menu) located under the Manage Mailman menu facilitates purging of MailMan files and the cleanup of MailMan globals.

|                                                                                                                |                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/092.png) | REF: For more information on these options, please refer to the "Manage MailMan Options" topic under the "Managing MailMan" topic in Chapter 2, "Implementation and Maintenance," in this manual. |

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the MailMan APIs. It includes the Routine name, tag entry point, Integration Agreement (IA) number, if any, and a brief description.

|                                                                                                                |                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/093.png) | NOTE: Those APIs released prior to MailMan Version 7.0 Patch XM\*7.1\*50 are notated with the word "Classic" for reference purposes only. |

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 8%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine</strong></th>
<th><strong>Entry</strong></th>
<th><strong>DBIA</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XM</td>
<td></td>
<td>10064</td>
<td>(Classic) Programmer entry point into MailMan.</td>
</tr>
<tr class="even">
<td>XM</td>
<td>CHECKIN</td>
<td>10064</td>
<td>Meant to be the entry action of any subordinate MailMan option.</td>
</tr>
<tr class="odd">
<td>XM</td>
<td>CHECKOUT</td>
<td>10064</td>
<td>Meant to be the exit action of every MailMan option.</td>
</tr>
<tr class="even">
<td>XM</td>
<td>EN</td>
<td>10064</td>
<td>(Classic) Meant to be the entry action of the primary MailMan option. It sets up the user's MailMan environment and calls the HEADER^XM API to greet the user.</td>
</tr>
<tr class="odd">
<td>XM</td>
<td>HEADER</td>
<td>10064</td>
<td>Meant to be part of the entry action of the primary MailMan option, whether called by itself or as part of another call (e.g., EN^XM). It displays a greeting to the user.</td>
</tr>
<tr class="even">
<td>XM</td>
<td>KILL</td>
<td>10064</td>
<td>(Classic) KILLs any MailMan variables that may be left over from previous calls.</td>
</tr>
<tr class="odd">
<td>XM</td>
<td>N1</td>
<td>10064</td>
<td><p>(Classic) Creates a mailbox for a user.</p>
<p>![](mailman-version-8-technical-manual/094.png) <strong>REF:</strong> See also: CRE8MBOX^XMXAPIB.</p></td>
</tr>
<tr class="even">
<td>XM</td>
<td>NEW</td>
<td>10064</td>
<td><p>(Classic) Creates a mailbox for a user.</p>
<p>![](mailman-version-8-technical-manual/095.png) <strong>REF:</strong> See also: CRE8MBOX^XMXAPIB.</p></td>
</tr>
<tr class="odd">
<td>XM</td>
<td>$$NU</td>
<td>10064</td>
<td><p>(Classic) Returns the number of new messages the user has, and it may display a message to the user telling how many.</p>
<p>![](mailman-version-8-technical-manual/096.png) <strong>REF:</strong> See also: QMBOX^XMXAPIB, QBSKT^XMXAPIB, $$BNMSGCT^XMXUTIL, $$TNMSGCT^XMXUTIL, $$NEWS^XMXUTIL.</p></td>
</tr>
<tr class="even">
<td>XMA</td>
<td>REC</td>
<td>1284</td>
<td><p>(Classic) Interactive: Read/Manage messages.</p>
<p>![](mailman-version-8-technical-manual/097.png) <strong>NOTE:</strong> Identical to the Read/Manage Messages option [XMREAD].</p>
<p>![](mailman-version-8-technical-manual/098.png) <strong>REF:</strong> See also: READ^XMXAPIU.</p></td>
</tr>
<tr class="odd">
<td>XMA0</td>
<td>ENTPRT</td>
<td>1230</td>
<td>(Classic) Interactive: Print a message.</td>
</tr>
<tr class="even">
<td>XMA0</td>
<td>HDR</td>
<td>1230</td>
<td>(Classic) Headerless print a message.</td>
</tr>
<tr class="odd">
<td>XMA0</td>
<td>PR2</td>
<td>1230</td>
<td><p>(Classic) Print a message.</p>
<p>![](mailman-version-8-technical-manual/099.png) <strong>REF:</strong> See also: PRTMSG^XMXAPI.</p></td>
</tr>
<tr class="even">
<td>XMA03</td>
<td>$$REN</td>
<td>1150</td>
<td><p>(Classic) Performs an integrity check on a user's basket, resequences messages in a user's basket, and returns a string.</p>
<p>![](mailman-version-8-technical-manual/100.png) <strong>REF:</strong> See also: RSEQBSKT^XMXAPIB.</p></td>
</tr>
<tr class="odd">
<td>XMA11</td>
<td>$$INFO</td>
<td></td>
<td>(Classic) Interactive: Allows the user to edit the message "Information Only" field.</td>
</tr>
<tr class="even">
<td>XMA11A</td>
<td>WRITE</td>
<td>1233</td>
<td><p>(Classic) Interactive: Sends/Answers a message.</p>
<p>![](mailman-version-8-technical-manual/101.png) <strong>NOTE:</strong> Identical to the Send a Message option (XMSEND). It is similar to ENT^XMD; however, it does not display the MailMan greeting.</p></td>
</tr>
<tr class="odd">
<td>XMA1B</td>
<td>KL</td>
<td>10065</td>
<td>(Classic) Delete a message from a basket.</td>
</tr>
<tr class="even">
<td>XMA1B</td>
<td>KLQ</td>
<td>10065</td>
<td><p>(Classic) Delete a message from a basket and put it in the "WASTE" basket.</p>
<p>![](mailman-version-8-technical-manual/102.png) <strong>REF:</strong> See also: DELMSG^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMA1B</td>
<td>S2</td>
<td>10065</td>
<td><p>(Classic) Put a message in a basket.</p>
<p>![](mailman-version-8-technical-manual/103.png) <strong>REF:</strong> See also: MOVEMSG^XMXAPI.</p></td>
</tr>
<tr class="even">
<td>XMA1C</td>
<td>REMSBMSG</td>
<td>10072</td>
<td><p>(Classic) Delete a message from a Postmaster server basket.</p>
<p>![](mailman-version-8-technical-manual/104.png) <strong>REF:</strong> See also: ZAPSERV^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMA1C</td>
<td>SETSB</td>
<td>10072</td>
<td><p>(Classic) Put a message into a Postmaster server basket.</p>
<p>![](mailman-version-8-technical-manual/105.png) <strong>REF:</strong> See also: PUTSERV^XMXAPI.</p></td>
</tr>
<tr class="even">
<td>XMA2</td>
<td>GET</td>
<td>10066</td>
<td><p>(Classic) Creates a new message stub in the MESSAGE file (#3.9). Unlike XMZ^XMA2, however, if the stub creation fails, your process will halt.</p>
<p>![](mailman-version-8-technical-manual/106.png) <strong>NOTE:</strong> Recommend you use XMZ^XMA2 or CRE8XMZ^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMA2</td>
<td>XMZ</td>
<td>10066</td>
<td><p>(Classic) Creates a new message stub in the MESSAGE file (#3.9).</p>
<p>![](mailman-version-8-technical-manual/107.png) <strong>REF:</strong> See also: CRE8XMZ^XMXAPI.</p></td>
</tr>
<tr class="even">
<td>XMA21</td>
<td>CHK</td>
<td>10067</td>
<td>(Classic) Checks to see if a user is a member of a mail group.</td>
</tr>
<tr class="odd">
<td>XMA21</td>
<td>DES</td>
<td>10067</td>
<td><p>(Classic) Interactive: Addressing with the <em>next</em> default recipient set.</p>
<p>![](mailman-version-8-technical-manual/108.png) <strong>REF:</strong> See also: TOWHOM^XMXAPI (interactive).</p></td>
</tr>
<tr class="even">
<td>XMA21</td>
<td>DEST</td>
<td>10067</td>
<td><p>(Classic) Interactive: Addressing with the <em>first</em> default recipient set.</p>
<p>![](mailman-version-8-technical-manual/109.png) <strong>REF:</strong> See also: TOWHOM^XMXAPI (interactive).</p></td>
</tr>
<tr class="odd">
<td>XMA21</td>
<td>INST</td>
<td>10067</td>
<td><p>(Classic) Non-interactive: Addressing.</p>
<p>![](mailman-version-8-technical-manual/110.png) <strong>REF:</strong> See also: TOWHOM^XMXAPI.</p></td>
</tr>
<tr class="even">
<td>XMA21</td>
<td>WHO</td>
<td>10067</td>
<td><p>(Classic) Non-interactive: Addressing.</p>
<p>![](mailman-version-8-technical-manual/111.png) <strong>REF:</strong> See also: TOWHOM^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMA2R</td>
<td>$$ENT</td>
<td>1145</td>
<td><p>(Classic) Creates and sends a reply to a message and returns the message number of the reply.</p>
<p>![](mailman-version-8-technical-manual/112.png) <strong>REF:</strong> See also: REPLYMSG^XMXAPI.</p></td>
</tr>
<tr class="even">
<td>XMA2R</td>
<td>$$ENTA</td>
<td>1145</td>
<td><p>(Classic) Creates and sends an answer to a message and returns the message number of the answer.</p>
<p>![](mailman-version-8-technical-manual/113.png) <strong>REF:</strong> See also: ANSRMSG^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMAD2</td>
<td>$$BSKT</td>
<td>1147</td>
<td><p>(Classic) Given a basket name and a user's DUZ, look up the basket. If it does not exist, create it, and return its IEN. If it does exist, return its IEN. If there is an error, return an error message.</p>
<p>![](mailman-version-8-technical-manual/114.png) <strong>REF:</strong> See also: CRE8BSKT^XMXAPIB, QBSKT^XMXAPIB.</p></td>
</tr>
<tr class="even">
<td>XMADGO</td>
<td>ZTSK</td>
<td>10068</td>
<td>(Classic) Starts tasks to deliver messages in local delivery queues.</td>
</tr>
<tr class="odd">
<td>XMAH</td>
<td>ENT8</td>
<td>1040</td>
<td>(Classic) Interactive: Display a list of all responses to a message.</td>
</tr>
<tr class="even">
<td>XMAH1</td>
<td></td>
<td>1232</td>
<td>(Classic) Interactive create and send a reply to a message.</td>
</tr>
<tr class="odd">
<td>XMAH1</td>
<td>ENTA</td>
<td>1232</td>
<td><blockquote>
<p>(Classic) Interactive create and send a reply to a message.</p>
</blockquote>
<p>![](mailman-version-8-technical-manual/115.png) <strong>NOTE:</strong> Identical to ^XMAH1.</p></td>
</tr>
<tr class="even">
<td>XMB</td>
<td></td>
<td>10069</td>
<td><p>(Classic) Create and send a bulletin in the background.</p>
<p>![](mailman-version-8-technical-manual/116.png) <strong>REF:</strong> See also: TASKBULL^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMB</td>
<td>BULL</td>
<td>10069</td>
<td>(Classic) Interactive: Create and send a bulletin.</td>
</tr>
<tr class="even">
<td>XMB</td>
<td>EN</td>
<td>10069</td>
<td><p>(Classic) Create and send a bulletin in the foreground.</p>
<p>![](mailman-version-8-technical-manual/117.png) <strong>REF:</strong> See also: SENDBULL^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMBGRP</td>
<td>$$DM</td>
<td>1146</td>
<td>(Classic) Deletes local members from a mail group.</td>
</tr>
<tr class="even">
<td>XMBGRP</td>
<td>$$MG</td>
<td>1146</td>
<td>(Classic) Creates a new mail group or adds members to an existing mail group.</td>
</tr>
<tr class="odd">
<td>XMCTLK</td>
<td>GO</td>
<td>1148</td>
<td>(Classic) Interactive use device.</td>
</tr>
<tr class="even">
<td>XMCU1</td>
<td>$$DECODEUP</td>
<td>1136</td>
<td><p>(Classic) Takes a string, converts <strong>~U~</strong> to <strong>^</strong>, and returns the result.</p>
<p>![](mailman-version-8-technical-manual/118.png) <strong>REF:</strong> See also: $$DECODEUP^XMXUTIL1.</p></td>
</tr>
<tr class="odd">
<td>XMCU1</td>
<td>$$ENCODEUP</td>
<td>1136</td>
<td><p>(Classic) Takes a string, converts <strong>^</strong> to <strong>~U~</strong>, and returns the result.</p>
<p>![](mailman-version-8-technical-manual/119.png) <strong>REF:</strong> See also: $$ENCODEUP^XMXUTIL1.</p></td>
</tr>
<tr class="even">
<td>XMCU1</td>
<td>$$RTRAN</td>
<td>1136</td>
<td>(Classic) Undoes the conversion of a string previously converted by $$STRAN^XMCU1 and returns the result.</td>
</tr>
<tr class="odd">
<td>XMCU1</td>
<td>$$STRAN</td>
<td>1136</td>
<td>(Classic) Takes a string, converts any control characters to printable characters, and returns the result.</td>
</tr>
<tr class="even">
<td>XMD</td>
<td></td>
<td>10070</td>
<td><p>(Classic) Creates and sends a message.</p>
<p>![](mailman-version-8-technical-manual/120.png) <strong>REF:</strong> See also: SENDMSG^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMD</td>
<td>EN1</td>
<td>10070</td>
<td>(Classic) Adds text to a message, addresses it, and sends it.</td>
</tr>
<tr class="even">
<td>XMD</td>
<td>ENL</td>
<td>10070</td>
<td>(Classic) Adds text to a message.</td>
</tr>
<tr class="odd">
<td>XMD</td>
<td>ENT</td>
<td>10070</td>
<td><p>(Classic) Interactive: Sends a message.</p>
<p>![](mailman-version-8-technical-manual/121.png) <strong>NOTE:</strong> Identical to the Send a Message option (XMSEND).</p>
<p>![](mailman-version-8-technical-manual/122.png) <strong>REF:</strong> See also: SEND^XMXAPIU.</p></td>
</tr>
<tr class="even">
<td>XMD</td>
<td>ENT1</td>
<td>10070</td>
<td><p>(Classic) Forwards a message. Addressing restrictions are waived.</p>
<p>![](mailman-version-8-technical-manual/123.png) <strong>REF:</strong> See also: FWDMSG^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMD</td>
<td>ENT2</td>
<td>10070</td>
<td>(Classic) Forward a message. If <strong>'</strong>$D(ZTQUEUED), prompt for additional recipients, whether or not any are already defined.</td>
</tr>
<tr class="even">
<td>XMGAPI0</td>
<td>$$SUBCHK</td>
<td>1142</td>
<td><p>(Classic) Validates the message subject and returns the valid subject or an error message.</p>
<p>![](mailman-version-8-technical-manual/124.png) <strong>REF:</strong> See also: VSUBJ^XMXAPI.</p></td>
</tr>
<tr class="odd">
<td>XMGAPI0</td>
<td>$$SUBGET</td>
<td>1142</td>
<td><p>(Classic) Returns the subject of a message.</p>
<p>![](mailman-version-8-technical-manual/125.png) <strong>REF:</strong> See also: $$SUBJ^XMXUTIL2.</p></td>
</tr>
<tr class="even">
<td>XMGAPI1</td>
<td>$$READ</td>
<td>1048</td>
<td>(Classic) Returns a line of text from a message.</td>
</tr>
<tr class="odd">
<td>XMGAPI2</td>
<td>$$HDR</td>
<td>1144</td>
<td><p>(Classic) Sets up an array of information about a message.</p>
<p>![](mailman-version-8-technical-manual/126.png) <strong>REF:</strong> See also: INMSG^XMXUTIL2, INMSG1^XMXUTIL2, INMSG2^XMXUTIL2, INRESPS^XMXUTIL2.</p></td>
</tr>
<tr class="even">
<td>XML</td>
<td>GET</td>
<td>1283</td>
<td>(Classic) Set up an executable variable, which, when executed, retrieves the next line of text from a message.</td>
</tr>
<tr class="odd">
<td>XMPG</td>
<td>ENT</td>
<td>10071</td>
<td>(Classic) Creates and sends a PackMan message with globals in it.</td>
</tr>
<tr class="even">
<td>XMRENT</td>
<td>$$NET</td>
<td>1143</td>
<td>(Classic) Returns an <strong>^</strong>-delimited string of information about a message.</td>
</tr>
<tr class="odd">
<td>XMS1</td>
<td>$$SRVTIME</td>
<td>1151</td>
<td>(Classic) Sets the LAST READ DATE/TIME (#2) and STATUS (#5) fields of a (server) message recipient in the RECIPIENT Multiple field of a message in the MESSAGE file (#3.9).</td>
</tr>
<tr class="even">
<td>XMS1</td>
<td>$$STATUS</td>
<td>1151</td>
<td>(Classic) Returns the STATUS field (#5) of a (server) message recipient from the RECIPIENT Multiple field of a message in the MESSAGE file (#3.9).</td>
</tr>
<tr class="odd">
<td>XMS3</td>
<td>REC</td>
<td>10073</td>
<td>(Classic) Get a line of text from a message.</td>
</tr>
<tr class="even">
<td>XMUT7</td>
<td>ENT</td>
<td>1132</td>
<td>(Classic) Sends a test message to a user's forwarding address and the Postmaster.</td>
</tr>
<tr class="odd">
<td>XMVVITAE</td>
<td>INIT</td>
<td>2728</td>
<td>Sets up vital user information and should <em>not</em> be used for any other purpose.</td>
</tr>
<tr class="even">
<td>XMVVITAE</td>
<td>OTHER</td>
<td>2728</td>
<td>Change certain MailMan settings when the user becomes a surrogate.</td>
</tr>
<tr class="odd">
<td>XMVVITAE</td>
<td>SELF</td>
<td>2728</td>
<td>Restore certain MailMan settings when the user becomes himself or herself again, after having been a surrogate.</td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>ADDRNSND</td>
<td>2729</td>
<td>Address and send a message (does <em>not</em> handle message body).</td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>ANSRMSG</td>
<td>2729</td>
<td><p>Answer a message (Send a new message, with a copy of the original message to the sender of the original message).</p>
<p>![](mailman-version-8-technical-manual/127.png) <strong>REF:</strong> See also: $$ENTA^XMA2R.</p></td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>CRE8XMZ</td>
<td>2729</td>
<td><p>Create a new message stub in the MESSAGE file (#3.9).</p>
<p>![](mailman-version-8-technical-manual/128.png) <strong>REF:</strong> See also: GET^XMA2, XMZ^XMA2.</p></td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>DELMSG</td>
<td>2729</td>
<td><p>Delete messages from a basket.</p>
<p>![](mailman-version-8-technical-manual/129.png) <strong>REF:</strong> See also: KLQ^XMA1B.</p></td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>FLTRMSG</td>
<td>2729</td>
<td>Filter messages in a basket.</td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>FWDMSG</td>
<td>2729</td>
<td><p>Forward messages from a basket.</p>
<p>![](mailman-version-8-technical-manual/130.png) <strong>REF:</strong> See also: ENT1^XMD.</p></td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>LATERMSG</td>
<td>2729</td>
<td>"Later" messages in a basket.</td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>MOVEMSG</td>
<td>2729</td>
<td><p>Move messages (from one basket) to another basket.</p>
<p>![](mailman-version-8-technical-manual/131.png) <strong>REF:</strong> See also: S2^XMA1B.</p></td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>PRTMSG</td>
<td>2729</td>
<td><p>Print messages.</p>
<p>![](mailman-version-8-technical-manual/132.png) <strong>REF:</strong> See also: PR2^XMA0.</p></td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>PUTSERV</td>
<td>2729</td>
<td><p>Put a message in a server basket.</p>
<p>![](mailman-version-8-technical-manual/133.png) <strong>REF:</strong> See also: SETSB^XMA1C.</p></td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>REPLYMSG</td>
<td>2729</td>
<td><p>Reply to message (attach reply to original message).</p>
<p>![](mailman-version-8-technical-manual/134.png) <strong>REF:</strong> See also: $$ENT^XMA2R.</p></td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>SENDBULL</td>
<td>2729</td>
<td><p>Send a bulletin (returns XMZ).</p>
<p>![](mailman-version-8-technical-manual/135.png) <strong>REF:</strong> See also: EN^XMB.</p></td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>SENDMSG</td>
<td>2729</td>
<td><p>Send a message.</p>
<p>![](mailman-version-8-technical-manual/136.png) <strong>REF:</strong> See also: ^XMD.</p></td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>TASKBULL</td>
<td>2729</td>
<td><p>Send a bulletin (quicker than SENDBULL, but does <em>not</em> return XMZ).</p>
<p>![](mailman-version-8-technical-manual/137.png) <strong>REF:</strong> See also: ^XMB.</p></td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>TERMMSG</td>
<td>2729</td>
<td>Terminate messages, possibly from a basket.</td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>TOWHOM</td>
<td>2729</td>
<td><p>Check one message addressee.</p>
<p>![](mailman-version-8-technical-manual/138.png) <strong>REF:</strong> See also: INST^XMA21, WHO^XMA21.</p></td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>VAPORMSG</td>
<td>2729</td>
<td>Set vaporize date for a message.</td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>VSUBJ</td>
<td>2729</td>
<td><p>Validate a subject.</p>
<p>![](mailman-version-8-technical-manual/139.png) <strong>REF:</strong> See also: $$SUBCHK^XMGAPI0.</p></td>
</tr>
<tr class="even">
<td>XMXAPI</td>
<td>ZAPSERV</td>
<td>2729</td>
<td><p>Delete a message from a server basket.</p>
<p>![](mailman-version-8-technical-manual/140.png) <strong>REF:</strong> See also: REMSBMSG^XMA1C.</p></td>
</tr>
<tr class="odd">
<td>XMXAPIB</td>
<td>CRE8BSKT</td>
<td>2723</td>
<td><p>Create a basket.</p>
<p>![](mailman-version-8-technical-manual/141.png) <strong>REF:</strong> See also: $$BSKT^XMAD2.</p></td>
</tr>
<tr class="even">
<td>XMXAPIB</td>
<td>CRE8MBOX</td>
<td>2723</td>
<td><p>Create a mailbox for a user.</p>
<p>![](mailman-version-8-technical-manual/142.png) <strong>REF:</strong> See also: N1^XM, NEW^XM.</p></td>
</tr>
<tr class="odd">
<td>XMXAPIB</td>
<td>DELBSKT</td>
<td>2723</td>
<td>Delete a user's basket.</td>
</tr>
<tr class="even">
<td>XMXAPIB</td>
<td>FLTRBSKT</td>
<td>2723</td>
<td>Filter messages in a basket.</td>
</tr>
<tr class="odd">
<td>XMXAPIB</td>
<td>FLTRMBOX</td>
<td>2723</td>
<td>Filter all messages in a user's mailbox.</td>
</tr>
<tr class="even">
<td>XMXAPIB</td>
<td>LISTBSKT</td>
<td>2723</td>
<td>Get a list of baskets in a mailbox.</td>
</tr>
<tr class="odd">
<td>XMXAPIB</td>
<td>LISTMSGS</td>
<td>2723</td>
<td>Get a list of messages in one or all baskets in a mailbox; search criteria can be used.</td>
</tr>
<tr class="even">
<td>XMXAPIB</td>
<td>NAMEBSKT</td>
<td>2723</td>
<td>Change the name of a basket.</td>
</tr>
<tr class="odd">
<td>XMXAPIB</td>
<td>QBSKT</td>
<td>2723</td>
<td>Get information on a basket.</td>
</tr>
<tr class="even">
<td>XMXAPIB</td>
<td>QMBOX</td>
<td>2723</td>
<td><p>Query a mailbox for new messages.</p>
<p>![](mailman-version-8-technical-manual/143.png) <strong>REF:</strong> See also: $$NU^XM, $$NU^XMGAPI4.</p></td>
</tr>
<tr class="odd">
<td>XMXAPIB</td>
<td>RSEQBSKT</td>
<td>2723</td>
<td><p>Resequence messages in a basket.</p>
<p>![](mailman-version-8-technical-manual/144.png) <strong>REF:</strong> See also: $$REN^XMA03.</p></td>
</tr>
<tr class="even">
<td>XMXAPIB</td>
<td>TERMMBOX</td>
<td>2723</td>
<td>Remove all traces of a user from MailMan globals.</td>
</tr>
<tr class="odd">
<td>XMXAPIG</td>
<td>ADDMBRS</td>
<td>3006</td>
<td>Add members to mail groups. Optionally, forward past mail group messages.</td>
</tr>
<tr class="even">
<td>XMXAPIG</td>
<td>DROP</td>
<td>3006</td>
<td>Enable user to drop from a mail group.</td>
</tr>
<tr class="odd">
<td>XMXAPIG</td>
<td>$$GOTLOCAL</td>
<td>3006</td>
<td>Determine if a mail group has <em>active</em> local members.</td>
</tr>
<tr class="even">
<td>XMXAPIG</td>
<td>JOIN</td>
<td>3006</td>
<td>Enable user to enroll in (join) a mail group. Optionally, forward past mail group messages.</td>
</tr>
<tr class="odd">
<td>XMXAPIU</td>
<td>READ</td>
<td>2774</td>
<td><p>Read/Manage messages in your mailbox.</p>
<p>![](mailman-version-8-technical-manual/145.png) <strong>REF:</strong> See also: REC^XMA.</p></td>
</tr>
<tr class="even">
<td>XMXAPIU</td>
<td>READNEW</td>
<td>2774</td>
<td>Read new messages in your mailbox.</td>
</tr>
<tr class="odd">
<td>XMXAPIU</td>
<td>SEND</td>
<td>2774</td>
<td><p>Send a message.</p>
<p>![](mailman-version-8-technical-manual/146.png) <strong>REF:</strong> See also: ENT^XMD.</p></td>
</tr>
<tr class="even">
<td>XMXAPIU</td>
<td>TOWHOM</td>
<td>2774</td>
<td><p>Ask user for message addressees.</p>
<p>![](mailman-version-8-technical-manual/147.png) <strong>REF:</strong> See also: DES^XMA21, DEST^XMA21.</p></td>
</tr>
<tr class="odd">
<td>XMXEDIT</td>
<td>CLOSED</td>
<td>2730</td>
<td>Toggle the message's "closed" flag.</td>
</tr>
<tr class="even">
<td>XMXEDIT</td>
<td>CONFID</td>
<td>2730</td>
<td>Toggle the message's "confidential" flag.</td>
</tr>
<tr class="odd">
<td>XMXEDIT</td>
<td>CONFIRM</td>
<td>2730</td>
<td>Toggle the message's "confirm receipt requested" flag.</td>
</tr>
<tr class="even">
<td>XMXEDIT</td>
<td>DELIVER</td>
<td>2730</td>
<td>Set/Delete the message delivery basket for all users.</td>
</tr>
<tr class="odd">
<td>XMXEDIT</td>
<td>INFO</td>
<td>2730</td>
<td>Toggle the message's "information only" flag.</td>
</tr>
<tr class="even">
<td>XMXEDIT</td>
<td>PRIORITY</td>
<td>2730</td>
<td>Toggle the message's "priority" flag.</td>
</tr>
<tr class="odd">
<td>XMXEDIT</td>
<td>SUBJ</td>
<td>2730</td>
<td>Change the message subject.</td>
</tr>
<tr class="even">
<td>XMXEDIT</td>
<td>TEXT</td>
<td>2730</td>
<td>Replace the message text.</td>
</tr>
<tr class="odd">
<td>XMXEDIT</td>
<td>VAPOR</td>
<td>2730</td>
<td>Set/Delete the message vaporize date.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$ACCESS</td>
<td>2731</td>
<td>Returns a value that indicates if the user can access a message.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$ANSWER</td>
<td>2731</td>
<td>Returns a value that indicates if the user can answer a message.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$BCAST</td>
<td>2731</td>
<td>Returns a value that indicates if a message was broadcast.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$CLOSED</td>
<td>2731</td>
<td>Returns a value that indicates if a message is closed.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$CONFID</td>
<td>2731</td>
<td>Returns a value that indicates if a message is confidential.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$CONFIRM</td>
<td>2731</td>
<td>Returns a value that indicates if a message is confirm receipt requested.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$COPY</td>
<td>2731</td>
<td>Returns a value that indicates if the user can copy a message.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$DELETE</td>
<td>2731</td>
<td>Returns a value that indicates if the user can delete or terminate a message.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$FORWARD</td>
<td>2731</td>
<td>Returns a value that indicates if the user can forward a message.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$INFO</td>
<td>2731</td>
<td>Returns a value that indicates if a message is information only.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$LATER</td>
<td>2731</td>
<td>Returns a value that indicates if a user can later a message.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$MOVE</td>
<td>2731</td>
<td>Returns a value that indicates if the user can save or filter a message.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$ORIGIN8R</td>
<td>2731</td>
<td>Returns a value that indicates if the user (XMDUZ or DUZ) sent the message (sender or surrogate).</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$POSTPRIV</td>
<td>2731</td>
<td>Returns a value that indicates if the user has Postmaster privileges, including if the user can perform group message actions in SHARED,MAIL.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$PRIORITY</td>
<td>2731</td>
<td>Returns a value that indicates if a message is priority.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$READ</td>
<td>2731</td>
<td>Returns a value that indicates if the user can read a message.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$REPLY</td>
<td>2731</td>
<td>Returns a value that indicates if the user can reply to a message.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$RPRIV</td>
<td>2731</td>
<td>Returns a value that indicates if the surrogate has READ privileges.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$RWPRIV</td>
<td>2731</td>
<td>Returns a value that indicates if the surrogate has READ or WRITE privileges.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$SEND</td>
<td>2731</td>
<td>Returns a value that indicates if the user can send a message.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$SURRACC</td>
<td>2731</td>
<td>Returns a value that indicates if the surrogate can access a message.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$SURRCONF</td>
<td>2731</td>
<td>Returns a value that indicates if a message is confidential, and if it is, whether the surrogate can access it.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$WPRIV</td>
<td>2731</td>
<td>Returns a value that indicates if the surrogate has WRITE privileges.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$ZCLOSED</td>
<td>2731</td>
<td>Returns a value that indicates if a message is closed.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$ZCONFID</td>
<td>2731</td>
<td>Returns a value that indicates if a message is confidential.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$ZCONFIRM</td>
<td>2731</td>
<td>Returns a value that indicates if a message is confirm receipt requested.</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$ZINFO</td>
<td>2731</td>
<td>Returns a value that indicates if a message is information only.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$ZORIGIN8</td>
<td>2731</td>
<td>Returns a value that indicates if the user (XMDUZ or DUZ) sent the message (sender or surrogate).</td>
</tr>
<tr class="even">
<td>XMXSEC</td>
<td>$$ZPOSTPRV</td>
<td>2731</td>
<td>Returns a value that indicates if the user has Postmaster privileges, including whether the user can perform group message actions in SHARED,MAIL.</td>
</tr>
<tr class="odd">
<td>XMXSEC</td>
<td>$$ZPRI</td>
<td>2731</td>
<td>Returns a value that indicates if a message is priority.</td>
</tr>
<tr class="even">
<td>XMXSEC1</td>
<td>CHKLINES</td>
<td>2732</td>
<td>Checks a value that indicates if the message is too long to be sent to a remote site.</td>
</tr>
<tr class="odd">
<td>XMXSEC1</td>
<td>CHKMSG</td>
<td>2732</td>
<td>Checks if a message is located where the calling routine says it is and if the user can access it.</td>
</tr>
<tr class="even">
<td>XMXSEC1</td>
<td>$$COPYAMT</td>
<td>2732</td>
<td>When copying a message, this function checks the total number of lines and responses to be copied.</td>
</tr>
<tr class="odd">
<td>XMXSEC1</td>
<td>$$COPYLIMS</td>
<td>2732</td>
<td>When copying a message, this function returns the sites message copy limits.</td>
</tr>
<tr class="even">
<td>XMXSEC1</td>
<td>$$COPYRECP</td>
<td>2732</td>
<td>When copying a message, this function checks the total number of recipients on the message to see if it's "OK" to list them in the copy text and also send the copy to them.</td>
</tr>
<tr class="odd">
<td>XMXSEC1</td>
<td>GETRESTR</td>
<td>2732</td>
<td>Returns assorted restrictions, if any, on sending or forwarding the message.</td>
</tr>
<tr class="even">
<td>XMXSEC1</td>
<td>OPTGRP</td>
<td>2732</td>
<td>Determines what the user may do at the basket or message group level.</td>
</tr>
<tr class="odd">
<td>XMXSEC1</td>
<td>$$PAKMAN</td>
<td>2732</td>
<td>Returns a value that indicates if a message is a PackMan message.</td>
</tr>
<tr class="even">
<td>XMXSEC1</td>
<td>$$SSPRIV</td>
<td>2732</td>
<td>Returns a value that indicates if a user is authorized to conduct a Super Search. If not, it also sets XMERR and ^TMP("XMERR",$J).</td>
</tr>
<tr class="odd">
<td>XMXSEC1</td>
<td>$$ZSSPRIV</td>
<td>2732</td>
<td>Returns a value that indicates if a user is authorized to conduct a Super Search. If not, it does <em>not</em> set XMERR and ^TMP("XMERR",$J).</td>
</tr>
<tr class="even">
<td>XMXSEC2</td>
<td>$$EDIT</td>
<td>2733</td>
<td>Returns a value that indicates if the user can edit a message.</td>
</tr>
<tr class="odd">
<td>XMXSEC2</td>
<td>OPTEDIT</td>
<td>2733</td>
<td>If OPTMSG^XMXSEC2 determines that the user may edit the message, then this routine details what exactly the user may and may not edit.</td>
</tr>
<tr class="even">
<td>XMXSEC2</td>
<td>OPTMSG</td>
<td>2733</td>
<td>Determines what the user may do with the message.</td>
</tr>
<tr class="odd">
<td>XMXUTIL</td>
<td>$$BMSGCT</td>
<td>2734</td>
<td>Returns the number of messages in a user's basket.</td>
</tr>
<tr class="even">
<td>XMXUTIL</td>
<td>$$BNMSGCT</td>
<td>2734</td>
<td>Returns the number of new messages in a user's basket.</td>
</tr>
<tr class="odd">
<td>XMXUTIL</td>
<td>$$BPMSGCT</td>
<td>2734</td>
<td>Returns the number of new priority messages in a user's basket.</td>
</tr>
<tr class="even">
<td>XMXUTIL</td>
<td>$$BSKTNAME</td>
<td>2734</td>
<td>Returns the name of a user's basket.</td>
</tr>
<tr class="odd">
<td>XMXUTIL</td>
<td>KVAPOR</td>
<td>2734</td>
<td>Sets/Removes a message vaporize date in a user's basket.</td>
</tr>
<tr class="even">
<td>XMXUTIL</td>
<td>LASTACC</td>
<td>2734</td>
<td>Records that the user has read the message.</td>
</tr>
<tr class="odd">
<td>XMXUTIL</td>
<td>MAKENEW</td>
<td>2734</td>
<td>Makes a message new and updates the new message counts.</td>
</tr>
<tr class="even">
<td>XMXUTIL</td>
<td>$$NAME</td>
<td>2734</td>
<td>Returns the name of the user by looking up XMDUZ in the NEW PERSON file (#200). Optionally, it may also return the user's title and/or institution.</td>
</tr>
<tr class="odd">
<td>XMXUTIL</td>
<td>$$NETNAME</td>
<td>2734</td>
<td>Returns the network name of a user, including the <strong>@</strong>site name.</td>
</tr>
<tr class="even">
<td>XMXUTIL</td>
<td>$$NEWS</td>
<td>2734</td>
<td><p>Returns the information on new messages in a user's mailbox.</p>
<p>![](mailman-version-8-technical-manual/148.png) <strong>REF:</strong> See also: $$NU^XMGAPI4, $$NU^XM.</p></td>
</tr>
<tr class="odd">
<td>XMXUTIL</td>
<td>NONEW</td>
<td>2734</td>
<td>Makes a message <em>not</em> new and updates the new message counts.</td>
</tr>
<tr class="even">
<td>XMXUTIL</td>
<td>PAGE</td>
<td>2734</td>
<td>Displays to the user: "Enter RETURN to continue or '^' to exit:" and waits until the user presses a key.</td>
</tr>
<tr class="odd">
<td>XMXUTIL</td>
<td>$$TMSGCT</td>
<td>2734</td>
<td>Returns the total number of messages in a user's mailbox.</td>
</tr>
<tr class="even">
<td>XMXUTIL</td>
<td>$$TNMSGCT</td>
<td>2734</td>
<td>Returns the total number of new messages in a user's mailbox.</td>
</tr>
<tr class="odd">
<td>XMXUTIL</td>
<td>$$TPMSGCT</td>
<td>2734</td>
<td>Returns the total number of new priority messages in a user's mailbox.</td>
</tr>
<tr class="even">
<td>XMXUTIL</td>
<td>WAIT</td>
<td>2734</td>
<td>Displays to the user: "Press RETURN to continue:" and waits until the user presses a key.</td>
</tr>
<tr class="odd">
<td>XMXUTIL1</td>
<td>$$CONVERT</td>
<td>2735</td>
<td>Given the Internet date/time string, it returns the VA FileMan date/time.</td>
</tr>
<tr class="even">
<td>XMXUTIL1</td>
<td>$$CTRL</td>
<td>2735</td>
<td>Strips the control characters from a string.</td>
</tr>
<tr class="odd">
<td>XMXUTIL1</td>
<td>$$DECODEUP</td>
<td>2735</td>
<td><p>Change all <strong>~U~</strong> to <strong>^</strong> in a string.</p>
<p>![](mailman-version-8-technical-manual/149.png) <strong>REF:</strong> See also: $$DECODEUP^XMCU1.</p></td>
</tr>
<tr class="even">
<td>XMXUTIL1</td>
<td>$$ENCODEUP</td>
<td>2735</td>
<td><p>Change all <strong>^</strong> to <strong>~U~</strong> in a string.</p>
<p>![](mailman-version-8-technical-manual/150.png) <strong>REF:</strong> See also: $$ENCODEUP^XMCU1.</p></td>
</tr>
<tr class="odd">
<td>XMXUTIL1</td>
<td>$$GMTDIFF</td>
<td>2735</td>
<td>Given the time zone, it returns <strong>+-hhmm</strong> difference from Greenwich Mean Time (GMT).</td>
</tr>
<tr class="even">
<td>XMXUTIL1</td>
<td>$$INDT</td>
<td>2735</td>
<td>Given the VA FileMan date/time, it returns the Internet date/time string: <strong>dd mm yyy</strong> <strong>hh:mm:ss +-hhmm (time zone)</strong>.</td>
</tr>
<tr class="odd">
<td>XMXUTIL1</td>
<td>$$MAXBLANK</td>
<td>2735</td>
<td>Reduce all three or more consecutive spaces in a string to two.</td>
</tr>
<tr class="even">
<td>XMXUTIL1</td>
<td>$$MELD</td>
<td>2735</td>
<td>Combine a string and a number to form a new string of a given length.</td>
</tr>
<tr class="odd">
<td>XMXUTIL1</td>
<td>$$MMDT</td>
<td>2735</td>
<td>Given the VA FileMan date/time, it returns the string: <strong>dd mmm yy hh:mm</strong>.</td>
</tr>
<tr class="even">
<td>XMXUTIL1</td>
<td>$$SCRUB</td>
<td>2735</td>
<td>Strips the control characters and leading/trailing spaces from a string.</td>
</tr>
<tr class="odd">
<td>XMXUTIL1</td>
<td>$$STRIP</td>
<td>2735</td>
<td>Strips the leading/trailing spaces from a string.</td>
</tr>
<tr class="even">
<td>XMXUTIL1</td>
<td>$$TIMEDIFF</td>
<td>2735</td>
<td>Given the decimal time difference, it returns <strong>+-hhmm</strong> (e.g. -2.5 equates to –0230).</td>
</tr>
<tr class="odd">
<td>XMXUTIL1</td>
<td>$$TSTAMP</td>
<td>2735</td>
<td>Returns a timestamp (<strong>$H</strong> expressed in seconds).</td>
</tr>
<tr class="even">
<td>XMXUTIL1</td>
<td>ZONEDIFF</td>
<td>2735</td>
<td>Given the time zone (or time difference <strong>+-hhmm</strong> from GMT), it returns the number of hours and minutes difference between that and the local time zone.</td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>$$BSKT</td>
<td>2736</td>
<td>Returns in which basket a message is located for a user.</td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>$$DATE</td>
<td>2736</td>
<td>Returns the message sent date in external format: <strong>DD MMM YY HHJ:MM</strong>.</td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>$$FROM</td>
<td>2736</td>
<td>Returns the message from in external format.</td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>INMSG</td>
<td>2736</td>
<td><p>Message information.</p>
<p>![](mailman-version-8-technical-manual/151.png) <strong>NOTE:</strong> Should only be called for messages, not for responses.</p>
<p>![](mailman-version-8-technical-manual/152.png) <strong>REF:</strong> See also: $$HDR^XMGAPI2.</p></td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>INMSG1</td>
<td>2736</td>
<td><p>Message information, Part 1.</p>
<p>![](mailman-version-8-technical-manual/153.png) <strong>NOTE:</strong> Should only be called for messages, not for responses.</p>
<p>![](mailman-version-8-technical-manual/154.png) <strong>REF:</strong> See also: $$HDR^XMGAPI2.</p></td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>INMSG2</td>
<td>2736</td>
<td><p>Message information, Part 2.</p>
<p>![](mailman-version-8-technical-manual/155.png) <strong>NOTE:</strong> Should only be called for messages, not for responses.</p>
<p>![](mailman-version-8-technical-manual/156.png) <strong>REF:</strong> See also: $$HDR^XMGAPI2.</p></td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>INRESP</td>
<td>2736</td>
<td><p>Response information.</p>
<p>![](mailman-version-8-technical-manual/157.png) <strong>NOTE:</strong> Should only be called for responses, not for messages.</p>
<p>![](mailman-version-8-technical-manual/158.png) <strong>REF:</strong> See also: $$HDR^XMGAPI2.</p></td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>INRESPS</td>
<td>2736</td>
<td><p>Get the message response count and responses read information.</p>
<p>![](mailman-version-8-technical-manual/159.png) <strong>REF:</strong> See also: $$HDR^XMGAPI2.</p></td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>$$KSEQN</td>
<td>2736</td>
<td>Returns the sequence number for a message in this user's basket.</td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>$$LINE</td>
<td>2736</td>
<td>How many lines are in the message?</td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>$$NEW</td>
<td>2736</td>
<td>Returns a value that indicates if the message is new for this user in this basket.</td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>$$PRI</td>
<td>2736</td>
<td>Returns a value that indicates if the message is priority.</td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>$$QRESP</td>
<td>2736</td>
<td>Returns a value that indicates if a message is a response.</td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>$$RESP</td>
<td>2736</td>
<td>Returns the number of responses to a message.</td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>$$SUBJ</td>
<td>2736</td>
<td>Returns the message subject in external format.</td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>$$ZDATE</td>
<td>2736</td>
<td>Returns the message sent date in external format: <strong>DD MMM YY HHJ:MM</strong>.</td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>$$ZFROM</td>
<td>2736</td>
<td>Returns the message from in external format.</td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>$$ZNODE</td>
<td>2736</td>
<td>Returns the message zero node: <strong>^XMB(3.9,XMZ,0)</strong>.</td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>$$ZPRI</td>
<td>2736</td>
<td>Returns a value that indicates if the message is priority.</td>
</tr>
<tr class="even">
<td>XMXUTIL2</td>
<td>$$ZREAD</td>
<td>2736</td>
<td>Returns the number of responses to a message this user has read.</td>
</tr>
<tr class="odd">
<td>XMXUTIL2</td>
<td>$$ZSUBJ</td>
<td>2736</td>
<td>Returns the message subject in external format.</td>
</tr>
<tr class="even">
<td>XMXUTIL3</td>
<td>Q</td>
<td>2737</td>
<td>Lists/Finds message addressees.</td>
</tr>
<tr class="odd">
<td>XMXUTIL3</td>
<td>QD</td>
<td>2737</td>
<td>Lists/Finds message recipients.</td>
</tr>
<tr class="even">
<td>XMXUTIL3</td>
<td>QL</td>
<td>2737</td>
<td>Lists/Finds "latered" message addressees.</td>
</tr>
<tr class="odd">
<td>XMXUTIL3</td>
<td>QN</td>
<td>2737</td>
<td>Get the network header records from a message that originated at a remote site.</td>
</tr>
<tr class="even">
<td>XMXUTIL3</td>
<td>QX</td>
<td>2737</td>
<td><p>This API performs the following actions:</p>
<ul>
<li><blockquote>
<p>Show all users who are current on a message (i.e., read all responses).</p>
</blockquote></li>
<li><blockquote>
<p>Show all users who are <em>not</em> current on a message (i.e., have <em>not</em> read all responses).</p>
</blockquote></li>
<li><blockquote>
<p>Show all users who have terminated from a message.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc161642822" class="anchor"></span>Table 7‑1. MailMan APIs (with cross-references to either Classic or New/Replacement APIs)

|                                                                                                                |                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/160.png) | REF: For a complete list and description of all MailMan V. 8.0 APIs, please refer to the *MailMan Developer's Guide*. |

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only users of MailMan with TCP/IP and Multimedia MailMan need mandatory resources available in order for these features to be properly implemented, used, and maintained. Check the appropriate appendices in this manual for prerequisites.

In order for Multimedia MailMan to work properly, sites must also have access to the IMAGE file (#2005), the NETWORK LOCATION file (#2005.2), and the VistA Radiology software.

### Integration Agreements (IA<span class="smallcaps">s)</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Supported References

MailMan V. 8.0 software has a Supported Integration Agreement (IA) with Kernel to use the DNS Lookup API (MAIL^XLFNSLK). It is recorded as Supported in the IA database on FORUM (IA \#3056). Permission to use it is granted by the custodian software (Kernel).

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-technical-manual/161.png)</td>
<td><p>For more information on the Kernel DNS Lookup API, please refer to the MAIL^XLFNSLK Home Page at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/kernel/apis/mail%5exlfnslk.htm">http://vista.med.va.gov/kernel/apis/mail^xlfnslk.htm</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

General Instructions for Obtaining Integration Agreements

The Database Administrator (DBA) maintains a list of Integration Agreements (IAs) or mutual agreements between software developers allowing the use of internal entry points or other software-specific features that are not available to the general programming public.

To obtain the current list of IAs to which MailMan is a custodian:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Custodial Package Menu option \[DBA IA CUSTODIAL MENU\].

> 5\. Choose the ACTIVE by Custodial Package option \[DBA IA CUSTODIAL\].

> 6\. When this option prompts you for a package, enter XXXX—Where XXXX equals: XM or MailMan.

> 7\. All current IAs to which the software is a custodian are listed.

To obtain detailed information on a specific integration agreement:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Inquire option \[DBA IA INQUIRY\].

> 5\. When prompted for "INTEGRATION REFERENCES," enter the specific integration agreement number of the IA you would like to display.

> 6\. The option then lists the full text of the IA you requested.

To obtain the current list of IAs to which MailMan is a subscriber:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Subscriber Package Menu option \[DBA IA SUBSCRIBER MENU\].

> 5\. Choose the Print ACTIVE by Subscribing Package option \[DBA IA SUBSCRIBER\].

> 6\. When prompted with "START WITH SUBSCRIBING PACKAGE," enter XXXX (in uppercase). When prompted with "GO TO SUBSCRIBING PACKAGE," enter XXXX (in uppercase)—Where "XXXX" equals: XM.

> 7\. All current IAs to which the software is a subscriber are listed.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace for VistA MailMan is XM. All routines and globals used in MailMan V. 8.0 start with XM, except for some that are shared and located in the DI and XU namespaces.

### File Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This topic contains a list of all VistA MailMan files (data dictionaries) that are exported with MailMan V. 8.0. The list includes file numbers, global locations, and file names as follows:

| File \# | Global    | Name                             |
|-------------|---------------|--------------------------------------|
| 3.4         | ^DIC(3.4,     | COMMUNICATIONS PROTOCOL              |
| 3.51        | ^XMB(3.51,    | SPOOL DOCUMENT                       |
| 3.519       | ^XMB(3.519,   | SPOOL DATA                           |
| 3.6         | ^XMB(3.6,     | BULLETIN                             |
| 3.7         | ^XMB(3.7,     | MAILBOX                              |
| 3.73        | ^XMB(3.73,    | MESSAGES TO BE NEW AT A LATER DATE   |
| 3.8         | ^XMB(3.8,     | MAIL GROUP                           |
| 3.816       | ^XMB(3.816,   | DISTRIBUTION LIST                    |
| 3.9         | ^XMB(3.9,     | MESSAGE                              |
| 4.2         | ^DIC(4.2,     | DOMAIN                               |
| 4.281       | ^%ZISL(4.281, | INTER-UCI TRANSFER                   |
| 4.2995      | ^XMBX(4.2995, | MAILMAN OUTSTANDING FTP TRANSACTIONS |
| 4.2996      | ^DIC(4.2996,  | INTERNET SUFFIX                      |
| 4.2997      | ^XMD(4.2997,  | REMOTE USER DIRECTORY                |
| 4.2998      | ^XMBX(4.2998, | MESSAGE DELIVERY STATS               |
| 4.2999      | ^XMBS(4.2999, | MESSAGE STATISTICS                   |
| 4.3         | ^XMB(1,       | MAILMAN SITE PARAMETERS              |
| 4.4         | ^XMB(4.4,     | MAILMAN TIME ZONE                    |
| 4.5         | ^XMB(4.5,     | NETWORK TRANSACTION                  |
| 4.501       | ^XMBX(4.501,  | NETWORK SENDERS REJECTED             |
| 4.6         | ^XMB(4.6,     | TRANSMISSION SCRIPT                  |

<span id="_Toc161642823" class="anchor"></span>Table 9‑1. Files and globals exported with MailMan V. 8.0

### Pointer Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pointer Relationship Map is a diagram of the pointer relationships between fields in MailMan V. 8.0 files. As files are added to a system, new pointer relationships can be created; thus, the actual map for an operational system may differ.

The following diagram was created using the Map Pointer Relations option \[DI DDMAP\] on the VA FileMan Data Dictionary Utilities menu \[DI DDU\].

|                                                                                                                |                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/162.png) | REF: For a list of MailMan files included in this diagram, please refer to Chapter 4, "Files," in this manual. |

File/Package: MAILMAN Date: JUL 13,2006

FILE (#) POINTER (#) FILE

POINTER FIELD TYPE POINTER FIELD FILE POINTED TO

--------------------------------------------------------------------------------

L=Laygo S=File not in set N=Normal Ref. C=Xref.

\*=Truncated m=Multiple v=Variable Pointer

---------------------

MAILMAN SITE PARAMET (#4.3) \| \|

TCP/IP COMMUNICATIONS \* (N )-\> \| 3.4 COMMUNICATI\* \|

---------------------

---------------------

OPTION (#19) \| \|

SERVER BULLETIN ...... (N S L)-\> \| 3.6 BULLETIN \|

\| m MAIL G:MAIL G\* \|-\> MAIL GROUP

---------------------

---------------------

\| 3.7 MAILBOX \|

\| NAME \|-\> NEW PERSON

\| LAST MAILMAN A\* \|-\> NEW PERSON

\| MESSAGE BEING \* \|-\> MESSAGE

\| MESSAGE BEING \* \|-\> MESSAGE

\| BASK:MESS:MESS\* \|-\> MESSAGE

\| m SURROG:SURROG\* \|-\> NEW PERSON

---------------------

---------------------

\| 3.73 MESSAGES T\* \|

\| USER \|-\> NEW PERSON

\| MESSAGE \|-\> MESSAGE

---------------------

---------------------

BULLETIN (#3.62) \| \|

MAIL GROUP ........... (N L)-\> \| 3.8 MAIL GROUP \|

MAIL GROUP (#3.811) \| \|

MEMBER GR:MEMBER GROU\* (N C )-\> \| ORGANIZER \|-\> NEW PERSON

MASTER FILE PARAMETE (#4.001) \| \|

MAIL GROUP ........... (N S L)-\> \| COORDINATOR \|-\> NEW PERSON

PACKAGE (#9.4) \| \|

MAIL GROUP ........... (N S )-\> \| m AUTHOR:AUTHOR\* \|-\> NEW PERSON

VAPU SITE PARAMETERS (#9.72) \| \|

INFORMATIONAL MAIL GRO\* (N S )-\> \| m MEMBER:MEMBER \|-\> NEW PERSON

PATCH MONITOR PARAME (#9.951) \| \|

MAIL GROUPS .......... (N S C )-\> \| m MEMBER:MEMBER\* \|-\> MAIL GROUP

DUPLICATE RESOLUTION (#15.1) \| \|

DUPLICATE MANAGER MAIL\* (N S )-\> \| m DISTRI:DISTRI\* \|-\> DISTRIBUTION LI\*

VERIFIED DUPLICATE MAI\* (N S )-\> \| m FAX RE:FAX RE\* \|-\> \*\*\* NONEXISTENT\*

MERGE MAIL GROUP ..... (N S )-\> \| m FAX GR:FAX GR\* \|-\> \*\*\* NONEXISTENT\*

ANCILLARY:MAIL GROUP\* (N S )-\> \| \|

OPTION (#19) \| \|

SERVER MAIL GROUP .... (N S L)-\> \| \|

MCCR SITE BUNDLING P (#466.1) \| \|

MAIL GROUP REC'G MM BU\* (N S L)-\> \| \|

QUALITY ASSURANCE SI (#740) \| \|

EWS LOCAL MAIL GROUP . (N S )-\> \| \|

MAILGROUP (QAN) ...... (N S )-\> \| \|

HL7 NON-DHCP APPLICA (#770) \| \|

MAIL GROUP ........... (N S )-\> \| \|

HL7 APPLICATION PARA (#771) \| \|

MAIL GROUP ........... (N S )-\> \| \|

HL7 MONITOR (#776.106) \| \|

MAIL GROUPS .......... (N S C )-\> \| \|

HL LOWER LEVEL PROTO (#869.2) \| \|

MAIL GROUP ........... (N S )-\> \| \|

HL COMMUNICATION SER (#869.3) \| \|

MAIL GROUP ........... (N S L)-\> \| \|

HL LOGICAL LINK (#870) \| \|

MAIL GROUP ........... (N S L)-\> \| \|

FS TRACKMAN PARAMETE (#7000.1) \| \|

TOP PRIORITY NOTIFICAT\* (N S )-\> \| \|

CM SITE PARAMETERS (#8986.095) \| \|

MAILGROUP FOR REPORTS/\* (N S L)-\> \| \|

MAILGROUP FOR REMOTE X\* (N S L)-\> \| \|

RPC BROKER SITE PARA (#8994.1) \| \|

MAIL GROUP FOR ALERTS (N S )-\> \| \|

(#177100.71) \| \|

MAIL GROUPS .......... (N S )-\> \| \|

VISTA AUTOPATCH SITE (#619066) \| \|

INFORMATIONAL MAIL GRO\* (N S )-\> \| \|

TWX ROUTER (#11000100.02) \| \|

MAIL GROUP(S) ........ (N S )-\> \| \|

SERVICE:MAIL GROUP ... (N S )-\> \| \|

---------------------

---------------------

MAIL GROUP (#3.813) \| \|

DISTRIBUTION LIST .... (N C L)-\> \| 3.816 DISTRIBUT\* \|

\| m DOMAIN:DOMAIN \|-\> DOMAIN

---------------------

---------------------

(#1.12) \| \|

MESSAGE .............. (N S )-\> \| 3.9 MESSAGE \|

MAILBOX (#3.7) \| \|

MESSAGE BEING EDITED . (N C L)-\> \| ORIGINAL MESSA\* \|-\> MESSAGE

MESSAGE BEING RESPONDE\* (N L)-\> \| m RESPON:RESPON\* \|-\> MESSAGE

BASKET:MESSAGE ....... (N )-\> \| RECIPIENT:PATH \|-\> DOMAIN

MESSAGES TO BE NEW A (#3.73) \| \|

MESSAGE .............. (N )-\> \| RECIPI:FORWAR\* \|-\> NEW PERSON

MESSAGE (#3.9) \| \|

ORIGINAL MESSAGE ..... (N )-\> \| RECIPI:FAX RE\* \|-\> \*\*\* NONEXISTENT\*

RESPONSE ............. (N )-\> \| LATER :BY WHO\* \|-\> NEW PERSON

MESSAGE STATISTICS (#4.2999) \| \|

MESSAGE IN TRANSIT ... (N )-\> \| m OBJECT:OBJECT\* \|-\> \*\*\* NONEXISTENT\*

VAPU INSTALL MODIFIE (#9.74) \| \|

KIDS MailMan Distribut\* (N S )-\> \| \|

XPD PATCHING (#9.76) \| \|

NAME v .................(N S L)-\> \| \|

A6AJIM (#16100) \| \|

NAME ................. (N S C )-\> \| \|

AAK PATCHING (#405850) \| \|

NAME v .................(N S C L)-\> \| \|

VISTA AUTOPATCH INST (#619070) \| \|

KIDS MailMan Distribut\* (N S )-\> \| \|

---------------------

---------------------

DISTRIBUTION LIST (#3.8161) \| \|

DOMAIN ............... (N C )-\> \| 4.2 DOMAIN \|

MESSAGE (#3.91) \| \|

RECIPIENT:PATH ....... (N )-\> \| RELAY DOMAIN \|-\> DOMAIN

INSTITUTION (#4) \| \|

DOMAIN ............... (N S )-\> \| \|

DOMAIN (#4.2) \| \|

RELAY DOMAIN ......... (N L)-\> \| \|

MESSAGE STATISTICS (#4.2999) \| \|

NAME ................. (N C )-\> \| \|

MAILMAN SITE PARAMET (#4.3) \| \|

DOMAIN NAME .......... (N C )-\> \| \|

PARENT ............... (N C )-\> \| \|

SUBORDINATE DOMAIN ... (N )-\> \| \|

XPD PATCHING (#9.7602) \| \|

COMMUNICA:TO SERVANT\* (N S C )-\> \| \|

COMMUNICA:FROM SERVAN\* (N S C )-\> \| \|

XPD PATCHING SERVITU (#9.77) \| \|

SERVANT OF WHICH DOMAI\* (N S )-\> \| \|

MASTERSHIP:DOMAIN? ... (N S )-\> \| \|

FOUNDATIONS SITE PAR (#18.01) \| \|

DOMAIN NAME .......... (N S )-\> \| \|

SUBSCRIPTION CONTROL (#774.01) \| \|

DESTINATION:DOMAIN ... (N S C )-\> \| \|

HL7 MONITOR EVENT TY (#776.32) \| \|

SERVER LOCATIONS:DOMAIN (N S )-\> \| \|

HL COMMUNICATION SER (#869.3) \| \|

DOMAIN ............... (N S )-\> \| \|

HL LOGICAL LINK (#870) \| \|

MAILMAN DOMAIN ....... (N S C )-\> \| \|

FS TRACKMAN PARAMETE (#7000.1) \| \|

SITE ................. (N S C )-\> \| \|

FS TRACKMAN SITE/SER (#7006) \| \|

DOMAIN ............... (N S C )-\> \| \|

PACKAGE INSTALLATION (#8982) \| \|

DOMAIN ............... (N S C L)-\> \| \|

KERNEL SYSTEM PARAME (#8989.3) \| \|

DOMAIN NAME .......... (N S C )-\> \| \|

PARAMETERS (#8989.5) \| \|

ENTITY v ...............(N S C L)-\> \| \|

RPC BROKER SITE PARA (#8994.1) \| \|

DOMAIN NAME .......... (N S C )-\> \| \|

NVS SYS MONITOR PARA (#18000) \| \|

SITE ................. (N S C )-\> \| \|

AAK PATCHING (#405850.02) \| \|

COMMUNICA:TO SERVANT\* (N S )-\> \| \|

COMMUNICA:FROM SERVAN\* (N S )-\> \| \|

AAK PATCHING SERVITU (#405851) \| \|

SERVANT OF WHICH DOMAI\* (N S )-\> \| \|

MASTERSHIP:DOMAIN? ... (N S )-\> \| \|

TWX ROUTER (#11000100.04) \| \|

REMOTE MA:DOMAIN\* .... (N S )-\> \| \|

REMOTE USERS:DOMAIN .. (N S )-\> \| \|

---------------------

---------------------

\| 4.2995 MAILMAN \* \|

\| USER \|-\> NEW PERSON

\| IMAGE \|-\> \*\*\* NONEXISTENT\*

---------------------

---------------------

\| 4.2999 MESSAGE \* \|

\| NAME \|-\> DOMAIN

\| MESSAGE IN TRA\* \|-\> MESSAGE

---------------------

---------------------

\| 4.3 MAILMAN SIT\* \|

\| DOMAIN NAME \|-\> DOMAIN

\| TIME ZONE \|-\> MAILMAN TIME ZO\*

\| PARENT \|-\> DOMAIN

\| TCP/IP COMMUNI\* \|-\> COMMUNICATIONS \*

\| TCP/IP TRANSMI\* \|-\> TRANSMISSION SC\*

\| DEFAULT INSTIT\* \|-\> INSTITUTION

\| m SUBORD:SUBORD\* \|-\> DOMAIN

\| SUBORD:CHRIST\* \|-\> NEW PERSON

\| LIMITE:POINTE\* \|-\> FILE

---------------------

---------------------

MAILMAN SITE PARAMET (#4.3) \| \|

TIME ZONE ............ (N C )-\> \| 4.4 MAILMAN TIM\* \|

---------------------

---------------------

MAILMAN SITE PARAMET (#4.3) \| \|

TCP/IP TRANSMISSION SC\* (N )-\> \| 4.6 TRANSMISSIO\* \|

---------------------

<span id="_Toc161642824" class="anchor"></span>Figure 9‑1. MailMan V. 8.0 Pointer Relationship Map

|                                                                                                                |                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/163.png) | REF: For more information about creating and reading this map, please refer to the "Map Pointer Relations option" topic in the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User’s Manual*. |

### Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### SORT Templates

The following SORT templates are distributed with MailMan V. 8.0:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SORT Template Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File (Name &amp; Number)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>XMMGR-BKFILER-DAY@23:30</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>MESSAGE DELIVERY STATS (#4.2998)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMMGR-BKFILER-TIME_PER_DATE</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc161642825" class="anchor"></span>Table 9‑2. SORT templates distributed with MailMan V. 8.0

XMMGR-BKFILER-DAY@23:30

NAME: XMMGR-BKFILER-DAY@23:30 DATE CREATED: FEB 14, 1992@12:12

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template is used to produce a report that lists the number

of messages that were created in a month, a day at a time.

SORT BY: DATE/TIME// (User is asked range)

WITHIN DATE/TIME, SORT BY: '\$E(\$P(INTERNAL(DATE/TIME),".",2),1,3)=233;L1//

From '0' To '1' COMPILED (c): NO

<span id="_Toc161642826" class="anchor"></span>Table 9‑3. SORT Templates: XMMGR-BKFILER-DAY@23\\30 (File \#4.2998)

XMMGR-BKFILER-TIME_PER_DATE

NAME: XMMGR-BKFILER-TIME_PER_DATE DATE CREATED: JUN 11, 1992@09:10

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template allows information in a time-oriented file to be

output from a beginning time to an ending time.

SORT BY: @DATE/TIME// (User is asked range)

WITHIN DATE/TIME, SORT BY: @\$E(\$P(INTERNAL(DATE/TIME),".",2),1,3)// (User is asked range) COMPILED (c): NO

<span id="_Toc161642827" class="anchor"></span>Figure 9‑2. SORT Templates: XMMGR-BKFILER-TIME_PER_DATE (File \#4.2998)

#### PRINT Templates

The following PRINT templates are distributed with MailMan V. 8.0:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>PRINT Template Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File (Name &amp; Number)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>XMHOSTLIST</p>
</blockquote></td>
<td><blockquote>
<p>DOMAIN (#4.2)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMMGR-BKFILER-ACTIVE_USERS/DEL</p>
</blockquote></td>
<td rowspan="9"><blockquote>
<p>MESSAGE DELIVERY STATS (#4.2998)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMMGR-BKFILER-DEL_BY_GROUP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMMGR-BKFILER-LENGTH_OF_QUEUES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMMGR-BKFILER-LONGTERM-STATS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMMGR-BKFILER-OLD_STATS/TABBED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMMGR-BKFILER-QUEUE-WAIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMMGR-BKFILER-STATS-PLUS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMMGR-BKFILER-STATS/TABBED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMMGR-BKFILER-TABBED-RT</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc161642828" class="anchor"></span>Table 9‑4. PRINT templates distributed with MailMan V. 8.0

XMHOSTLIST

NAME: XMHOSTLIST DATE CREATED: APR 09, 1987

FILE: DOMAIN

DESCRIPTION: This template may be used to produce a list of domains with

pertinent network routing information.

HEADER (c): DOMAIN HOST LIST

FIRST PRINT FIELD: NAME;L10//

THEN PRINT FIELD: STATION;"STATION";R5//

THEN PRINT FIELD: DHCP ROUTING INDICATOR;"DHCP";L6//

THEN PRINT FIELD: MAILMAN HOST;"HOST";R8//

THEN PRINT FIELD: MCTS ROUTING INDICATOR;"MCST";L6//

COMPILED (c): NO

<span id="_Toc161642829" class="anchor"></span>Figure 9‑3. PRINT Templates: XMHOSTLIST (File \#4.2)

XMMGR-BKFILER-ACTIVE_USERS/DEL

NAME: XMMGR-BKFILER-ACTIVE_USERS/DEL DATE CREATED: OCT 17, 1993@18:30

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template is used to display active users and message

delivery information.

HEADER (c): ACTIVE USERS VERSES DELIVERIES

FIRST PRINT FIELD: DATE/TIME//

THEN PRINT FIELD: ACTIVE USERS#//

THEN PRINT FIELD: TOTAL QUEUE LENGTH#//

THEN PRINT FIELD: MESSAGE DELIVERIES MADE#//

THEN PRINT FIELD: RESPONSE DELIVERIES MADE#//

THEN PRINT FIELD: MESSAGE DELIVERIES IN QUEUE#//

THEN PRINT FIELD: RESPONSE DELIVERIES IN QUEUE#//

COMPILED (c): NO

<span id="_Toc161642830" class="anchor"></span>Figure 9‑4. PRINT Templates: XMMGR-BKFILER-ACTIVE_USERS/DEL (File \#4.2998)

XMMGR-BKFILER-DEL_BY_GROUP

NAME: XMMGR-BKFILER-DEL_BY_GROUP DATE CREATED: OCT 17, 1993@18:30

FILE: MESSAGE DELIVERY STATS DATE LAST USED: NOV 18, 1997

DESCRIPTION: This template is used to output mail deliveries by delivery

group. It will output two message delivery groups and three response delivery

groups.

HEADER (c): DELIVERIES BY GROUP

FIRST PRINT FIELD: DATE/TIME//

THEN PRINT FIELD: QUEUED DELIVERIES MESSAGE G1#//

THEN PRINT FIELD: QUEUED DELIVERIES MESSAGE G2#//

THEN PRINT FIELD: QUEUED DELIVERIES RESPONSE G1#//

THEN PRINT FIELD: QUEUED DELIVERIES RESPONSE G2#//

THEN PRINT FIELD: QUEUED DELIVERIES RESPONSE G3#//

COMPILED (c): NO

<span id="_Toc161642831" class="anchor"></span>Figure 9‑5. PRINT Templates: XMMGR-BKFILER-DEL_BY_GROUP (File \#4.2998)

XMMGR-BKFILER-LENGTH_OF_QUEUES

NAME: XMMGR-BKFILER-LENGTH_OF_QUEUES DATE CREATED: OCT 17, 1993@18:31

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template is used to output the length of mail delivery

queues. Each queue is a column and two message and three response columns are

displayed.

HEADER (c): QUEUE LENGTH REPORT

FIRST PRINT FIELD: DATE/TIME//

THEN PRINT FIELD: TOTAL QUEUE LENGTH#//

THEN PRINT FIELD: MESSAGE NUMBER GROUP1#//

THEN PRINT FIELD: MESSAGE NUMBER GROUP2#//

THEN PRINT FIELD: RESPONSE NUMBER GROUP1#//

THEN PRINT FIELD: RESPONSE NUMBER GROUP2#//

THEN PRINT FIELD: RESPONSE NUMBER GROUP3#//

COMPILED (c): NO

<span id="_Toc161642832" class="anchor"></span>Figure 9‑6. PRINT Templates: XMMGR-BKFILER-LENGTH_OF_QUEUES (File \#4.2998)

XMMGR-BKFILER-LONGTERM-STATS

NAME: XMMGR-BKFILER-LONGTERM-STATS DATE CREATED: MAY 06, 1994@14:10

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template is used to output statistics of mail deliveries

by month.

HEADER (c): MESSAGE & RESPONSE CREATION HISTORY

FIRST PRINT FIELD: DATE/TIME//

THEN PRINT FIELD: MESSAGE NUMBER LAST ASSIGNED//

THEN PRINT FIELD: W:\$S('\$D(XMLAST):0,\$P(X,U,11)-XMLAST\>999999:0,\$P(X,U,11)-XMLAS

T\>0:1,1:0) \$P(X,U,11)-XMLAST S XMLAST=\$P(X,U,11);"New Messages"//

COMPILED (c): NO

<span id="_Toc161642833" class="anchor"></span>Figure 9‑7. PRINT Templates: XMMGR-BKFILER-LONGTERM-STATS (File \#4.2998)

XMMGR-BKFILER-OLD_STATS/TABBED

NAME: XMMGR-BKFILER-OLD_STATS/TABBED DATE CREATED: OCT 17, 1993@18:32

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template will produce a report just like the

XMMGR-BKFILER-STATS-PLUS template, except that the output is formatted for

capture into a file that can then easily be converted into a graphical

display.

HEADER (c): TABBED STATISTICS

FIRST PRINT FIELD: DATE(#.01);L12//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: TIME(#.01)//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: S %XMNORMAL=\$S(\$D(^XMB(1,1,120001)):^(120001),1:"");X//

THEN PRINT FIELD: ACTIVE USERS;L6//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: W \$J(\$S('\$D(X):.1,X=0:.1,1:X)/%XMNORMAL,4,2);X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: LINES OUTPUT;R6//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: W \$J(\$S('\$D(X):.1,X=0:.1,1:X)/\$P(%XMNORMAL,",",2),8,2);X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: MESSAGE DELIVERIES MADE;R10//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: S XMTEMP=X;X//

THEN PRINT FIELD: RESPONSE DELIVERIES MADE;R10//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: S Y=X+XMTEMP W \$J(\$S('\$D(Y):.1,Y=0:.1,1:Y)/\$P(%XMNORMAL,",",3)

,7,2);X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: MESSAGE DELIVERIES IN QUEUE;R10//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: S XMTEMP=X;X//

THEN PRINT FIELD: RESPONSE DELIVERIES IN QUEUE;R10//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: S Y=X+XMTEMP W \$J(\$S('\$D(Y):.1,Y=0:.1,1:Y)/\$P(%XMNORMAL,",",4)

,7,2);X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: RESPONSE TIME - AVERAGE;R8//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: W \$J(\$S('\$D(X):.1,X=0:.1,1:X)/\$P(%XMNORMAL,",",5),4,2);X//

THEN PRINT FIELD: K %XMNORMAL;X//

COMPILED (c): NO

<span id="_Toc161642834" class="anchor"></span>Figure 9‑8. PRINT Templates: XMMGR-BKFILER-OLD_STATS/TABBED (File \#4.2998)

XMMGR-BKFILER-QUEUE-WAIT

NAME: XMMGR-BKFILER-QUEUE-WAIT DATE CREATED: OCT 17, 1993@18:33

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template is used to output the time messages are waiting

to be delivered in the mail delivery queues. Each queue is a column and two

message and three response columns are displayed.

HEADER (c): DELIVERY WAIT BY QUEUE

FIRST PRINT FIELD: DATE/TIME//

THEN PRINT FIELD: TOTAL QUEUE LENGTH#//

THEN PRINT FIELD: MESSAGE AGE GROUP1#//

THEN PRINT FIELD: MESSAGE AGE GROUP2#//

THEN PRINT FIELD: RESPONSE AGE GROUP1#//

THEN PRINT FIELD: RESPONSE AGE GROUP2#//

THEN PRINT FIELD: RESPONSE AGE GROUP3#//

COMPILED (c): NO

<span id="_Toc161642835" class="anchor"></span>Figure 9‑9. PRINT Templates: XMMGR-BKFILER-QUEUE-WAIT (File \#4.2998)

XMMGR-BKFILER-STATS-PLUS

NAME: XMMGR-BKFILER-STATS-PLUS DATE CREATED: OCT 17, 1993@18:33

FILE: MESSAGE DELIVERY STATS DATE LAST USED: SEP 25, 2004

DESCRIPTION: This template gives important daily delivery statistics.

HEADER (c): MESSAGE DELIVERY STATS LIST

FIRST PRINT FIELD: DATE/TIME//

THEN PRINT FIELD: ACTIVE USERS#//

THEN PRINT FIELD: LINES OUTPUT#//

THEN PRINT FIELD: MESSAGE DELIVERIES MADE#//

THEN PRINT FIELD: RESPONSE DELIVERIES MADE#//

THEN PRINT FIELD: MESSAGE AGE GROUP1#//

THEN PRINT FIELD: RESPONSE AGE GROUP1#//

THEN PRINT FIELD: MESSAGE DELIVERIES IN QUEUE#//

THEN PRINT FIELD: RESPONSE DELIVERIES IN QUEUE#//

THEN PRINT FIELD: RESPONSE TIME - AVERAGE#//

COMPILED (c): NO

<span id="_Toc161642836" class="anchor"></span>Figure 9‑10. PRINT Templates: XMMGR-BKFILER-STATS-PLUS (File \#4.2998)

XMMGR-BKFILER-STATS/TABBED

NAME: XMMGR-BKFILER-STATS/TABBED DATE CREATED: FEB 11, 1994@15:22

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template will produce a report just like the

XMMGR-BKFILER-STATS-PLUS template, except that the output is formatted for

capture into a file that can then easily be converted into a graphical

display.

HEADER (c): TABBED STATISTICS

FIRST PRINT FIELD: DATE(#.01);L12//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: TIME(#.01)//

THEN PRINT FIELD: S XMTEMP=\$P(X,U,21) W \$C(9);X//

THEN PRINT FIELD: S %XMNORMAL=\$S(\$D(^XMB(1,1,120001)):^(120001),1:"");X//

THEN PRINT FIELD: ACTIVE USERS;L6//

THEN PRINT FIELD: S Y=\$P(X,U,21) W "A"\_\$C(9)\_\$S(+%XMNORMAL=0:0,1:\$J(\$S('\$D(Y):.1

,Y=0:.1,1:Y)/%XMNORMAL,4,2));X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: LINES OUTPUT;R6//

THEN PRINT FIELD: W "L"\_\$C(9)\_\$S(+\$P(%XMNORMAL,",",2)=0:0,1:\$J(\$S('\$D(Y):.1,Y=0:

.1,1:Y)/\$P(%XMNORMAL,",",2),8,2));X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: MESSAGE DELIVERIES MADE;R10//

THEN PRINT FIELD: S XMTEMP=Y;X//

THEN PRINT FIELD: RESPONSE DELIVERIES MADE;R10//

THEN PRINT FIELD: S Y=Y+XMTEMP W "R"\_\$C(9)\_\$S(+\$P(%XMNORMAL,",",3)=0:0,1:\$J(\$S('

\$D(Y):.1,Y=0:.1,1:Y)/\$P(%XMNORMAL,",",3),7,2));X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: MESSAGE DELIVERIES IN QUEUE;R10//

THEN PRINT FIELD: S XMTEMP=Y;X//

THEN PRINT FIELD: RESPONSE DELIVERIES IN QUEUE;R10//

THEN PRINT FIELD: S Y=Y+XMTEMP W "Q"\_\$C(9)\_\$S(+\$P(%XMNORMAL,",",4)=0:0,1:\$J(\$S('

\$D(Y):.1,Y=0:.1,1:Y)/\$P(%XMNORMAL,",",4),7,2));X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: RESPONSE TIME - AVERAGE;R8//

THEN PRINT FIELD: W "T"\_\$C(9)\_\$S(+\$P(%XMNORMAL,",",5)=0:0,1:\$J(\$S('\$D(Y):.1,Y=0:

.1,1:Y)/\$P(%XMNORMAL,",",5),4,2));X//

THEN PRINT FIELD: K %XMNORMAL;X//

COMPILED (c): NO

NAME: XMMGR-BKFILER-TABBED-RT DATE CREATED: OCT 17, 1993@18:35

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template provides information about daily response time.

HEADER (c): MESSAGE DELIVERY STATS LIST

FIRST PRINT FIELD: DATE/TIME;X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: RESPONSE TIME - AVERAGE//

COMPILED (c): NO

<span id="_Toc161642837" class="anchor"></span>Figure 9‑11. PRINT Templates: XMMGR-BKFILER-STATS/TABBED (File \#4.2998)

XMMGR-BKFILER-TABBED-RT

NAME: XMMGR-BKFILER-TABBED-RT DATE CREATED: OCT 17, 1993@18:35

FILE: MESSAGE DELIVERY STATS

DESCRIPTION: This template provides information about daily response time.

HEADER (c): MESSAGE DELIVERY STATS LIST

FIRST PRINT FIELD: DATE/TIME;X//

THEN PRINT FIELD: \$C(9);X//

THEN PRINT FIELD: RESPONSE TIME - AVERAGE//

COMPILED (c): NO

<span id="_Toc161642838" class="anchor"></span>Figure 9‑12. PRINT Templates: XMMGR-BKFILER-TABBED-RT (File \#4.2998)

### Help Frames

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An extensive set of MailMan Help Frames have been created and updated for MailMan V. 8.0.

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/164.png) | REF: For a complete list of Help Frames, please refer to "Appendix A—Help Frames" in this manual. |

# Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Standards and Conventions (SAC) Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software-wide variables have received Standards and Conventions Committee (SACC) exemptions.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 24%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SAC Standard Section</strong></th>
<th><strong>Variables</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">2A</td>
<td>B,J,V,Z,$V,$Z</td>
<td><ul>
<li><blockquote>
<p>Beginning December 14, 1989, MailMan, by virtue of being defined as part of Kernel, can use non-standard <strong>$Z</strong> functions and non-standard <strong>$Z</strong> special variables.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Beginning April 27, 1995, MailMan has an exemption to use <strong>$ZV</strong> in the <strong>XML*</strong> series of routines that are used for reading and writing data across the network for Patch XM*7.1*8.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>OPEN, CLOSE device</td>
<td><p>Beginning October 25, 1990, MailMan is exempted from using the device handler to open and close synchronous communications channels to support electronic communications until such time that the VA device handler provides the needed functionality.</p>
<p>Also involved are scripts distributed in the DOMAIN file (#4.2) or the TRANSMISSION SCRIPT file (#4.6). This exemption allows MailMan to set the appropriate IO* variables as needed.</p></td>
</tr>
<tr class="odd">
<td>2D2</td>
<td>* &amp; # READs</td>
<td>Beginning March 26, 1990, the following MailMan routines can use <strong>*</strong> or <strong>#</strong> READs: XMC1, XMCTLK, XLM, XML1CRC, and XML4CRC*.</td>
</tr>
<tr class="even">
<td>4B</td>
<td>Package-wide variables</td>
<td>Beginning February 9, 1989, XMDUN, XMDUNO, XMDUZ, and XMPRIV are package-wide variables for use in MailMan.</td>
</tr>
<tr class="odd">
<td>6D</td>
<td>FM compatibility</td>
<td><ul>
<li><blockquote>
<p>Beginning February 3, 1993, the global ^XMBPOST is exempted from VA FileMan compatibility in Version 7.1 of MailMan and later. This global will be used to store information concerning mail messages to be posted by MailMan's background filer. It will also temporarily store statistical data concerning mail messages.</p>
</blockquote></li>
</ul>
<blockquote>
<p>![](mailman-version-8-technical-manual/165.png) <strong>NOTE:</strong> MailMan no longer uses the following globals referenced in this exemption:</p>
</blockquote>
<ul>
<li><blockquote>
<p>The global XMB("NOP", is exempted from VA FileMan compatibility. It is a temporary list of messages that should <em>not</em> be purged.</p>
</blockquote></li>
<li><blockquote>
<p>The global XMB("POST", is exempted from VA FileMan compatibility. It is a temporary list of messages to be posted by MailMan's background filer. This exemption is for Version 7.0 or earlier of MailMan.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Beginning August 10, 1989, the global XMB("PURGE" is exempt from VA FileMan compatibility.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc161642839" class="anchor"></span>Table 10‑1. SAC Exemption for software-wide variables

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan V. 8.0 provides the capability to create and use mail groups. MailMan does *not* generate alerts.

MailMan distributes the following mail group:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Mail Group Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>XM SUPER SEARCH</p>
</blockquote></td>
<td><blockquote>
<p>This mail group is sent a bulletin whenever someone conducts a Super Search using the XM SUPER SEARCH menu. The bulletin tells who conducted the search and what search criteria were used.</p>
<p>Members of this mail group should be anyone who ought to be notified whenever a Super Search is conducted. At an absolute minimum, the site Information Security Officer (ISO) and alternate ISO(s) should be members. There should be enough responsible members of the group so that a certain level of comfort is achieved that the Super Searches will only be conducted for just cause. The more people there are, who are aware that a Super Search has been conducted, the less likely it is that the capability will be abused.</p>
<p>The site ISO should be the coordinator of this mail group.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc161642840" class="anchor"></span>Table 11‑1. Mail groups

|                                                                                                                |                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/166.png) | REF: For more information on the Super Search functionality, please refer to the XM SUPER SEARCH option in the "Exported Options" topic in Chapter 5, "Exported Options," in this manual. |

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA MailMan software itself transmits data and provides the capability to transmit data to remote systems, facilities, and databases. Numerous routines have been modified and modularized with MailMan V. 8.0. This modularization was necessary for maintainability.

|                                                                                                                |                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/167.png) | REF: For a list of all routines distributed with MailMan V. 8.0, please refer to the Chapter 3, "Routines," in this manual. |

### Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no application-specific archiving procedures or recommendations for MailMan V. 8.0.

The MESSAGE file (#3.9) has the potential to grow in size over time.

### Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No non-VA products are embedded in or required by MailMan V. 8.0, other than those provided by the underlying operating systems.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic signatures are *not* used within MailMan V. 8.0.

### Menus/Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of all VistA MailMan menu options exported with MailMan V. 8.0 of particular interest to Information Security Officers (ISOs):

- XM SUPER SEARCH

|                                                                                                                |                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/168.png) | REF: For a description of this option and to view a more detailed list of all options exported with MailMan V. 8.0, please refer to the "Options—Listed Alphabetically by Name" topic in Chapter 5, "Exported Options," in this manual. |

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following security keys are exported/distributed with MailMan V. 8.0:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Security Key</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XM AUTO-FORWARD WAIVER</td>
<td><p>As of MailMan Patch XM*8.0*18, if the AUTO-FORWARD LIMITED? field (#31) in the MAILMAN SITE PARAMETERS file (#4.3) is set to YES, auto-forward addresses are limited to sites in the AUTO-FORWARD APPROVED SITE Multiple field (#31.1) in the MAILMAN SITE PARAMETERS file (#4.3). Any user who has been assigned this security key, however, can also auto-forward to the sites that are listed in the AUTO-FORWARD WAIVER SITE Multiple field (#31.2) in the MAILMAN SITE PARAMETERS file (#4.3).</p>
<p>To obtain this security key, the user <em>must</em> submit a request for a waiver through the site Information Security Officer (ISO). Only after the waiver has been granted may the user be assigned this key.</p>
<p>![](mailman-version-8-technical-manual/169.png) <strong>NOTE:</strong> Check with the ISO for details on the requirements for the waiver.</p></td>
</tr>
<tr class="even">
<td>XM CAC ADPAC</td>
<td><p>This key allows users, such as Clinical Application Coordinators (CACs) and Automated Data Processing Application Coordinators (ADPACs) to edit other users' mail groups. Users holding this key can edit any mail group, except personal mail groups. (Personal mail groups are those mail groups that only the organizer may edit or use.)</p>
<p>![](mailman-version-8-technical-manual/170.png) <strong>NOTE:</strong> Holders of the XMMGR security key should <em>not</em> be given this key, because they already possess the privilege this key grants.</p></td>
</tr>
<tr class="odd">
<td>XM GROUP EDIT MASTER</td>
<td><p>This key allows users to edit other users' mail groups. Users holding this key can edit and add new users to any other users' mail groups except personal mail groups. (Personal mail groups are those mail groups that only the organizer may edit or use.)</p>
<p>The following users should <em>not</em> be given this key, because they already possess the privilege this key grants:</p>
<ul>
<li><p>Holders of the XMMGR security key.</p></li>
<li><p>Clinical Application Coordinators, as identified in File #8930, USR Class, belonging to the Text Integration Utility (TIU) software.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>XM GROUP PRIORITY</td>
<td>This key allows users to forward priority mail to groups. Without this key, only the sender of a priority message can forward it to groups.</td>
</tr>
<tr class="odd">
<td>XM NO BROADCASTS</td>
<td>This key is used to prevent broadcast messages from being delivered to the user.</td>
</tr>
<tr class="even">
<td>XM SUPER SEARCH</td>
<td><p>This key allows users to run the Super Search Message File option [XM SUPER SEARCH], which performs a search for messages in the MESSAGE file (#3.9) based on multiple criteria.</p>
<p>This key should be given, on a time-limited basis, to trusted individuals who have a valid need to research messages in the MESSAGE file (#3.9). For example, in sexual or other harassment cases, in which the harassment is in the form of MailMan messages.</p>
<p>![](mailman-version-8-technical-manual/171.png) <strong>REF:</strong> For more information on the Super Search functionality, please refer to the XM SUPER SEARCH option in the "<strong>Options—</strong>" topic in this chapter.</p></td>
</tr>
<tr class="odd">
<td>XMMGR</td>
<td>This key is required for options that can remove data from the MailMan system or for options that require most trusted employee status and are used for managing MailMan. This key is also used to control privileges in SHARED,MAIL.</td>
</tr>
<tr class="even">
<td>XMNET</td>
<td>This key is used to control options that require special privileges for use of network mail. Also, this key can be used to control the ability for users to have and change their forwarding address.</td>
</tr>
<tr class="odd">
<td>XMNOPRIV</td>
<td>This key is used to control privileges in SHARED,MAIL. Without this key, users <em>cannot</em> assume the identity of SHARED,MAIL.</td>
</tr>
<tr class="even">
<td>XMQ- (DOMAIN file Keys)</td>
<td>There are domains in the DOMAIN file (#4.2) whose names begin with "<strong>Q-</strong>". These are referred to as "Queue Domains." Each has a security key. Each security key begins with "<strong>XMQ-</strong>". For example, if the Domain name is Q-CLM.VA.GOV, the corresponding security key is named "XMQ-CLM". Since these domains are used to send data to central collection points, this security key prevents users from sending personal messages. Any domain containing REDACTED or Q- should have keys.</td>
</tr>
<tr class="odd">
<td>XMSTAR</td>
<td>This key gives users the ability to broadcast messages to <em>all</em> local mail users by entering an asterisk/star ("<strong>*</strong>") at the "Send to:" prompt.</td>
</tr>
<tr class="even">
<td>XMSTAR LIMITED</td>
<td>This key gives users the ability to broadcast messages to a <em>subset</em> of local mail users by entering an asterisk/star ("<strong>*</strong>") at the "Send to:" prompt.</td>
</tr>
<tr class="odd">
<td>XMTALK</td>
<td>This key is used to control access to the TalkMan options, which allow users to connect to remote computers via Network Mail scripts.</td>
</tr>
</tbody>
</table>

<span id="_Toc161642841" class="anchor"></span>Table 11‑2. Security keys distributed with MailMan V. 8.0

The following security keys are not exported/distributed with MailMan V. 8.0 but are required for certain functionality:

| Security Key | Description                                          |
|------------------|----------------------------------------------------------|
| XUPROG           | This key is used to allow access to the PackMan options. |
| XUPROGMODE       | This key is used to allow access to the PackMan options. |

<span id="_Toc161642842" class="anchor"></span>Table 11‑3. Security keys required for certain functionality within MailMan V. 8.0

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan has two levels of VA FileMan file security. MailMan files contain data that are prepared according to VA policy and procedures and therefore require a high level of protection regarding WRITE, DELETE, and LAYGO access.

The following file security is established with MailMan V. 8.0 files. The definitions for each security key attached to these files are AS FOLLOWS:

- \#—System Manager access
- @—Programmer access
- ^—No access
- Null—Full access

| File \# | File Name                        | DD | RD | WR | DEL | LAYGO | AUDIT |
|-------------|--------------------------------------|--------|--------|--------|---------|-----------|-----------|
| 3.4         | COMMUNICATIONS PROTOCOL              | \# | @  | \# | \#  | \#    | \#    |
| 3.51        | SPOOL DOCUMENT                       | @  | @  | @  | @   | @     | @     |
| 3.519       | SPOOL DATA                           |        |        |        |         |           |           |
| 3.6         | BULLETIN                             | \# |        | \# | \#  |           | \#    |
| 3.7         | MAILBOX                              | \# |        | \# | \#  | \#    | \#    |
| 3.73        | MESSAGES TO BE NEW AT A LATER DATE   | @  | \# | \# | \#  | \#    | @     |
| 3.8         | MAIL GROUP                           | \# |        | \# | \#  |           | \#    |
| 3.816       | DISTRIBUTION LIST                    |        |        |        |         |           |           |
| 3.9         | MESSAGE                              | ^  | ^  | ^  | ^   | \#    | ^     |
| 4.2         | DOMAIN                               | \# | \# | \# | \#  | \#    | \#    |
| 4.281       | INTER-UCI TRANSFER                   |        |        |        |         |           |           |
| 4.2995      | MAILMAN OUTSTANDING FTP TRANSACTIONS |        |        |        |         |           |           |
| 4.2996      | INTERNET SUFFIX                      |        |        |        |         |           |           |
| 4.2997      | REMOTE USER DIRECTORY                |        |        |        |         |           |           |
| 4.2998      | MESSAGE DELIVERY STATS               |        |        |        |         |           |           |
| 4.2999      | MESSAGE STATISTICS                   |        |        |        |         |           |           |
| 4.3         | MAILMAN SITE PARAMETERS              | @  | \# | \# | \#  | \#    | @     |
| 4.4         | MAILMAN TIME ZONE                    |        |        |        |         |           |           |
| 4.5         | NETWORK TRANSACTION                  |        |        |        |         |           |           |
| 4.501       | NETWORK SENDERS REJECTED             |        |        |        |         |           |           |
| 4.6         | TRANSMISSION SCRIPT                  |        |        |        |         |           |           |

<span id="_Toc161642843" class="anchor"></span>Table 11‑4. File security for MailMan V. 8.0 software

|                                                                                                                |                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/172.png) | REF: For more information on the files exported with MailMan V. 8.0, please refer to the "Files" topic in Chapter 5, "Exported Options," in this manual. |

|                                                                                                                |                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| ![](mailman-version-8-technical-manual/173.png) | NOTE: Site-specific parameters can be set in the MAILMAN SITE PARAMETERS file (#4.3). |

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan V. 8.0 has been developed in accordance with all VA regulations. The following directive specifies the data archiving and purging process with MailMan:
> VHA Directive 10-95-094

### Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional legal requirements are imposed by MailMan V. 8.0 on VistA users, nor does MailMan V. 8.0 relieve users of any previously established requirements.

Distribution of the MailMan software is unrestricted.

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BANNER               | A line of text with a user's name and domain, which is displayed to everyone who sends mail to the user.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| BSCP                 | Block Mode Simple Communications Protocol, a procedure used for message transmission with error checking.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| BULLETIN             | A form letter often triggered by a VA FileMan field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DEVICE               | A terminal, printer, modem, or other type of hardware or equipment associated with a computer. A host file of an underlying operating system may be treated like a device in that it may be written to (e.g., for spooling).                                                                                                                                                                                                                                                                                                   |
| DOMAIN               | A site for sending and receiving mail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| INITIALIZATION       | The process of setting variables in a program to their starting value.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| INPUT TRANSFORM      | An executable string of M code that is used to check the validity of input and converts it into an internal form for storage.                                                                                                                                                                                                                                                                                                                                                                                                  |
| KEYWORD              | A reference name that calls a help frame when entered at a message prompt.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| LINE EDITOR          | This is VA FileMan's special line-oriented text editor. This editor is used for the word-processing data type.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| LOCAL                | The system that a user is currently signed on to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| LOG IN/ON            | The process of gaining access to a computer system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| LOG OUT/OFF          | The process of exiting from a computer system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MAIL BASKET          | Mail baskets provide a way of saving messages in a sorted fashion similar to a filing system. Mail baskets are created at the "Message action" prompt by typing in "S" to save, then the name you wish to call the basket. If the basket already exists, the message will be sent to it. If the basket does *not* exist, you will be asked if you want it created. Placing a message in a mail basket other than the IN or Waste baskets protects the message from being automatically purged when the IN BASKET PURGE is run. |
| MESSAGE-ID           | A message identifier that shows the time of transmission, the message number, and the domain name of the message.                                                                                                                                                                                                                                                                                                                                                                                                              |
| MULTIMEDIA MAIL      | Multimedia Mail gives the capability of attaching Binary Large OBjects (BLOBs) to electronic messages so that images, spreadsheets, graphs, and other operating system files that are not pure ASCII text, may be sent and received either locally or across the network.                                                                                                                                                                                                                                                      |
| PHYSICAL LINK DEVICE | Hardware used to establish outgoing communication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| "PLAYING A SCRIPT"   | A method of opening a transmission link for a message, used to force message transmission of message and testing.                                                                                                                                                                                                                                                                                                                                                                                                              |
| POLLER               | An option that opens the transmission line to all domains with "P" in the Flags field.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| POSTMASTER           | The basket where message queues are stored. Also, the person who manages this basket for a particular site.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PROTOCOL             | Code containing logic for opening and closing links, and for sending/receiving transmissions.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PURGE                | A procedure used to delete messages or message pointers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| QUEUE                | A list that stores messages destined for a given domain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| REMOTE               | Any system that a user is not signed on to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SCRIPT               | A set of MailMan commands and transmission scripts to a remote domain in the DOMAIN file (#4.2).                                                                                                                                                                                                                                                                                                                                                                                                                               |
| SERVER               | An automatic mail reader for internal messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SMTP                 | Simple Mail Transport Protocol. The primary transport protocol for MailMan.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SWP                  | Sliding Window Protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TRANSMISSION SCRIPT  | List of commands for directing a message stored in the TRANSMISSION SCRIPT field.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VALIDATION NUMBER    | A security check number that must be in the domains of both the sending and receiving sites.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| WRAP-AROUND MODE     | Text that is fit into available column positions and automatically wraps to the next line, sometimes by splitting at word boundaries (spaces).                                                                                                                                                                                                                                                                                                                                                                                 |
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-technical-manual/174.png)</td>
<td><p><strong>REF:</strong> For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the ISS Glossary Web page at the following Web address:</p>
<blockquote>
<p><a href="http://vaww.vista.med.va.gov/iss/glossary.asp">REDACTED</a></p>
</blockquote>
<p>For a comprehensive list of acronyms, please visit the ISS Acronyms Web site at the following Web address:</p>
<blockquote>
<p><a href="http://vaww.vista.med.va.gov/iss/acronyms/index.asp">REDACTED</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix A—Help Frames

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix contains the Help Frames available with MailMan Version 8.0.

The following Help Frame prefix naming conventions are used in MailMan V. 8.0 (listed alphabetically):

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Help F</strong><strong>rame Prefix</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XM-I</strong></td>
<td><strong>IRM-related Help Frames</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-C</p>
</blockquote></td>
<td>Communicate</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-D</p>
</blockquote></td>
<td>Disk</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N</p>
</blockquote></td>
<td>Network</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-S-</p>
</blockquote></td>
<td>Site Parameters</td>
</tr>
<tr class="even">
<td><strong>XM-U-</strong></td>
<td><strong>User-related Help Frames</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-A-</p>
</blockquote></td>
<td>Address-related Help Frames.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-</p>
</blockquote></td>
<td>Basket–related Help Frames.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-BO-</p>
</blockquote></td>
<td>Basket Options-related Help Frames</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-H-</p>
</blockquote></td>
<td>Help Option-related Help Frames.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-H-Q</p>
</blockquote></td>
<td>Frequently Asked Questions-related Help Frames.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-I-</p>
</blockquote></td>
<td>Information-related Help Frames.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-K-</p>
</blockquote></td>
<td>KIDS/PackMan-related Help Frames.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-</p>
</blockquote></td>
<td>Message–related Help Frames.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-MO-</p>
</blockquote></td>
<td>Message Options-related Help Frames.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-NEW-</p>
</blockquote></td>
<td>New features in MailMan Version 8.0-related Help Frames</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-</p>
</blockquote></td>
<td>Personal Preferences-related Help Frames.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-Q-</p>
</blockquote></td>
<td>Query/Searching/Lookup-related Help Frames.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-R-</p>
</blockquote></td>
<td>Reading and Managing Mail-related Help Frames (including New Mail).</td>
</tr>
</tbody>
</table>

<span id="_Toc161642844" class="anchor"></span>Table A-1. MailMan help frame prefixes

The following Help Frames are distributed with MailMan Version 8.0 (listed alphabetically):

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Help Frame Name</strong></p>
</blockquote></th>
<th><strong>Help Frame Title</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>XMHELP</p>
</blockquote></td>
<td>USING MAILMAN</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMHELP-MANUAL</p>
</blockquote></td>
<td>THE ONLINE MAILMAN USER GUIDE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-C-TALKMAN</p>
</blockquote></td>
<td>TALKMAN</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-C-TALKMAN CAPTURE</p>
</blockquote></td>
<td>CAPTURING A TALKMAN SESSION</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-C-TALKMAN END</p>
</blockquote></td>
<td>ENDING A TALKMAN SESSION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-D-RECOVER MSGS</p>
</blockquote></td>
<td>RECOVER MESSAGES FOR A USER</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-D-RECOVER MSGS-FIND</p>
</blockquote></td>
<td>RECOVER MESSAGES FOR A USER - FIND THEM</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-D-RECOVER MSGS-LIST</p>
</blockquote></td>
<td>RECOVER MESSAGES FOR A USER - LIST THEM</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-D-RECOVER MSGS-PUT</p>
</blockquote></td>
<td>RECOVER MESSAGES FOR A USER - PUT IN USER'S MAILBOX</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-BULLETINS</p>
</blockquote></td>
<td>BULLETINS SIGNALING TROUBLE IN NETWORK TRANSMISSION</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-N-DOMAIN FILE</p>
</blockquote></td>
<td>DOMAIN FILE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-DOMAIN FILE-ADDRESSING</p>
</blockquote></td>
<td>DOMAIN FILE FIELDS INVOLVED IN ADDRESSING</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-N-DOMAIN FILE-CONNECT</p>
</blockquote></td>
<td>DOMAIN FILE FIELDS USED TO CONNECT TO A SITE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-DOMAIN FILE-CONNECT-2</p>
</blockquote></td>
<td>DOMAIN FILE FIELDS USED TO CONNECT TO A SITE (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-N-DOMAIN FILE-FLAGS</p>
</blockquote></td>
<td>DOMAIN FILE - FLAGS FIELD</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-DOMAIN FILE-SESSION</p>
</blockquote></td>
<td>DOMAIN FILE FIELDS USED WHILE TRANSMITTING</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-N-DOMAIN FILE-TURN</p>
</blockquote></td>
<td>DOMAIN FILE - DISABLE TURN COMMAND FIELD</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-DOMAIN FILE-VALIDATE</p>
</blockquote></td>
<td>DOMAIN FILE - VALIDATION NUMBER FIELD</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-NEW FEATURES</p>
</blockquote></td>
<td>NEW FEATURES FOR SITE MANAGERS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-NETWORK</p>
</blockquote></td>
<td>NETWORK OVERVIEW</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-N-XMIT PLAY</p>
</blockquote></td>
<td>TRANSMIT - PLAY A SCRIPT</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-XMIT POLL</p>
</blockquote></td>
<td>POLL A SITE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-N-XMIT QUEUES</p>
</blockquote></td>
<td>TRANSMIT QUEUES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-XMIT SCHEDULE TASK</p>
</blockquote></td>
<td>TRANSMIT - SCHEDULE A TASK</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-N-XMIT TAPE</p>
</blockquote></td>
<td>TRANSMIT VIA TAPE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-XMIT TASK</p>
</blockquote></td>
<td>TRANSMIT TASK</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-N-XMIT TASK-2</p>
</blockquote></td>
<td>TRANSMIT TASK (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-N-XMIT UCI</p>
</blockquote></td>
<td>TRANSMIT BETWEEN UCI'S VIA A GLOBAL</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-S-BIG GROUP SIZE</p>
</blockquote></td>
<td>BIG GROUP SIZE FIELD</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-S-MAX DIGITS FOR MSG NUM</p>
</blockquote></td>
<td>MAX DIGITS FOR MESSAGE NUMBER FD</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-S-MESSAGE LINE LIMIT</p>
</blockquote></td>
<td>P-MESSAGE LINE LIMIT FIELD</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-S-SITE PARAMETERS</p>
</blockquote></td>
<td>MAILMAN SITE PARAMETERS FILE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-S-SITE PARAMETERS-DISK</p>
</blockquote></td>
<td>SITE PARAMETERS AFFECTING DISK SPACE MANAGEMENT</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-S-SITE PARAMETERS-ID</p>
</blockquote></td>
<td>SITE PARAMETERS AFFECTING THE SITE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-S-SITE PARAMETERS-LOCAL</p>
</blockquote></td>
<td>SITE PARAMETERS AFFECTING LOCAL MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-S-SITE PARAMETERS-REMOTE</p>
</blockquote></td>
<td>SITE PARAMETERS AFFECTING REMOTE MESSAGING</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-I-S-SITE PARAMETERS-USER</p>
</blockquote></td>
<td>SITE PARAMETERS AFFECTING USERS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-I-S-SITE PARAMETERS-USER-2</p>
</blockquote></td>
<td>SITE PARAMETERS AFFECTING USERS (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-MASTER</p>
</blockquote></td>
<td>VA ELECTRONIC MAIL SYSTEM</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMNET-BLOB-HARDWARE</p>
</blockquote></td>
<td>BLOBs (Binary Large Objects) Message</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMNET-BLOB-NETWORK</p>
</blockquote></td>
<td>Sending and Receiving BLOBs across a Network</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMNET-FTP-COMPONENTS</p>
</blockquote></td>
<td>Basic components in setting up the Multimedia MailMan</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMNET-FTP-REC-NETWORK-LOCATION</p>
</blockquote></td>
<td>FTP Receive Network Location</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMNET-MULTIMEDIA</p>
</blockquote></td>
<td>HOW MULTIMEDIA MAILMAN WORKS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XMNET-MULTIMEDIA-HARDWARE</p>
</blockquote></td>
<td>The relationships of Multimedia hardware</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XMNET-MULTIMEDIA-OVERVIEW</p>
</blockquote></td>
<td>Multimedia Technical Overview</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-A-ADDRESS</p>
</blockquote></td>
<td>SENDING A MESSAGE - ADDRESSING</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-A-CC</p>
</blockquote></td>
<td>ADDRESSING A RECIPIENT AS 'CARBON COPY'</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-A-GROUP LARGE</p>
</blockquote></td>
<td>ADDRESSING MAIL TO LARGE MAIL GROUPS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-A-GROUP LARGE-2</p>
</blockquote></td>
<td>ADDRESSING MAIL TO LARGE MAIL GROUPS (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-A-INFO ONLY</p>
</blockquote></td>
<td>ADDRESSING A RECIPIENT AS INFORMATION ONLY</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-A-LOCAL USER NAME</p>
</blockquote></td>
<td>ENTERING A LOCAL USER'S NAME IN MAILMAN</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-A-LOCAL USER NAME-2</p>
</blockquote></td>
<td>ENTERING A LOCAL USER'S NAME (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-A-STAGGER DELIVERY</p>
</blockquote></td>
<td>STAGGER DELIVERY OF A MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-A-STAGGER DELIVERY-2</p>
</blockquote></td>
<td>STAGGER DELIVERY OF A MESSAGE (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-BASKET CONTENTS LIST</p>
</blockquote></td>
<td>DIRECTORY OF BASKETS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-BASKET NAME</p>
</blockquote></td>
<td>NAMING BASKETS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-BASKET NAME CHANGE</p>
</blockquote></td>
<td>CHANGE A MAIL BASKET NAME</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-BASKET SELECT</p>
</blockquote></td>
<td>RESPONDING TO THE 'MAIL BASKET' PROMPT</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-CHANGE DETAIL</p>
</blockquote></td>
<td>CHANGE DETAIL</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-FILTER</p>
</blockquote></td>
<td>FILTERING MESSAGES - BASKET ACTION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-NAVIGATE CLASSIC</p>
</blockquote></td>
<td>READING A MESSAGE AND NAVIGATING IN THE CLASSIC READER</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-NAVIGATE FULL SCREEN</p>
</blockquote></td>
<td>READING A MESSAGE AND NAVIGATING IN THE FULL SCREEN READER</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-NEW MAIL LIST</p>
</blockquote></td>
<td>LIST OF NEW MESSAGES IN A BASKET</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-BO-CLASSIC</p>
</blockquote></td>
<td>CLASSIC READER BASKET MESSAGE ACTIONS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-BO-CLASSIC-2</p>
</blockquote></td>
<td>CLASSIC READER BASKET MESSAGE ACTIONS (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-BO-FULL SCREEN</p>
</blockquote></td>
<td>FULL SCREEN READER BASKET MESSAGE ACTIONS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-BO-FULL SCREEN LIST</p>
</blockquote></td>
<td>FULL SCREEN READER MESSAGE LIST ACTIONS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-BO-FULL SCREEN-2</p>
</blockquote></td>
<td>FULL SCREEN READER BASKET MESSAGE ACTIONS (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-OPPOSITE TOGGLE</p>
</blockquote></td>
<td>OPPOSITE SELECTION TOGGLE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-READER</p>
</blockquote></td>
<td>MAILMAN MESSAGE READERS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-READER CLASSIC</p>
</blockquote></td>
<td>CLASSIC MESSAGE READER</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-READER DETAILED</p>
</blockquote></td>
<td>DETAILED MESSAGE INFORMATION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-READER DETAILED LIST</p>
</blockquote></td>
<td>DETAILED INFORMATION DISPLAYED WITH MESSAGE LISTS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-READER DIFF</p>
</blockquote></td>
<td>BASKET ACTION CODES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-READER DIFF-2</p>
</blockquote></td>
<td>BASKET ACTION CODES (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-READER DIFF-3</p>
</blockquote></td>
<td>BASKET ACTION CODES (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-READER FULL SCREEN</p>
</blockquote></td>
<td>FULL SCREEN MESSAGE READER</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-READER SUMMARY</p>
</blockquote></td>
<td>SUMMARY MESSAGE INFORMATION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-RESEQUENCE MESSAGES</p>
</blockquote></td>
<td>RESEQUENCING MESSAGE NUMBERS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-XMIT PRIORITY TOGGLE</p>
</blockquote></td>
<td>TOGGLING MESSAGE TRANSMISSION PRIORITY</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-B-XMIT PRIORITY TOGGLE-2</p>
</blockquote></td>
<td>TOGGLING MESSAGE TRANSMISSION PRIORITY (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-B-ZOOM TOGGLE</p>
</blockquote></td>
<td>ZOOM SELECTION TOGGLE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-H-GROUP</p>
</blockquote></td>
<td>MAIL GROUP INFORMATION</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-H-GROUP-2</p>
</blockquote></td>
<td>MAIL GROUP INFORMATION (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-H-GROUP-3</p>
</blockquote></td>
<td>MAIL GROUP INFORMATION (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-H-GROUP-4</p>
</blockquote></td>
<td>MAIL GROUP INFORMATION (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-H-Q DELETE</p>
</blockquote></td>
<td>DELETED MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-H-Q DISAPPEARED</p>
</blockquote></td>
<td>'DISAPPEARED' MESSAGES WHICH HAVE NOT BEEN DELETED</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-H-Q INTERRUPT</p>
</blockquote></td>
<td>INTERRUPTED MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-H-Q LOOKUP</p>
</blockquote></td>
<td>LOOKING UP A MESSAGE TO BE READ</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-H-Q RECALL</p>
</blockquote></td>
<td>RECALLING OR EDITING A MESSAGE AFTER TRANSMISION</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-H-Q REMOVE</p>
</blockquote></td>
<td>REMOVING A RECIPIENT FROM THE LIST</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-H-Q REPLIES</p>
</blockquote></td>
<td>REPLIES TO A MESSAGE FROM AN UNKNOWN RECIPIENT</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-H-QUESTIONS</p>
</blockquote></td>
<td>FREQUENTLY ASKED QUESTIONS ABOUT MAILMAN</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-H-USER</p>
</blockquote></td>
<td>USER INFORMATION</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-I-EDITOR FM LINE</p>
</blockquote></td>
<td>VA FILEMAN LINE EDITOR</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-I-EDITOR FM SCREEN</p>
</blockquote></td>
<td>VA FILEMAN SCREEN EDITOR</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-I-GROUP</p>
</blockquote></td>
<td>MAIL GROUPS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-I-GROUP COORDINATOR</p>
</blockquote></td>
<td>MAILMAN MAIL GROUP COORDINATORS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-I-GROUP MEMBER</p>
</blockquote></td>
<td>MEMBERS OF MAIL GROUPS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-I-GROUP-2</p>
</blockquote></td>
<td>MAIL GROUPS (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-I-SHARED MAIL</p>
</blockquote></td>
<td>SHARED,MAIL - A LIBRARY OF MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-I-SURROGATE</p>
</blockquote></td>
<td>MAILMAN SURROGATES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-I-SURROGATE BECOME</p>
</blockquote></td>
<td>BECOMING A SURROGATE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-I-SURROGATE-2</p>
</blockquote></td>
<td>MAILMAN SURROGATES (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-I-SURROGATE-3</p>
</blockquote></td>
<td>MAILMAN SURROGATES (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-I-SURROGATE-4</p>
</blockquote></td>
<td>MAILMAN SURROGATES (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-K-PACKMAN</p>
</blockquote></td>
<td>PACKMAN - MOVING ROUTINES AND DATA IN MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-K-PACKMAN COMPARE</p>
</blockquote></td>
<td>COMPARE PACKMAN MESSAGE ROUTINES AGAINST THOSE INSTALLED NOW</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-K-PACKMAN INSTALL</p>
</blockquote></td>
<td>INSTALLING A PACKMAN MESSAGE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-K-PACKMAN LOAD GLOBALS</p>
</blockquote></td>
<td>LOADING GLOBAL DATA INTO A PACKMAN MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-K-PACKMAN LOAD PACKAGE</p>
</blockquote></td>
<td>LOADING AN ENTIRE PACKAGE INTO A PACKMAN MESSAGE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-K-PACKMAN LOAD ROUTINES</p>
</blockquote></td>
<td>LOADING ROUTINES INTO PACKMAN MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-K-PACKMAN PRINT</p>
</blockquote></td>
<td>PRINTING PACKMAN MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-K-PACKMAN SUMMARIZE</p>
</blockquote></td>
<td>SUMMARIZE PACKMAN MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-ANSWER</p>
</blockquote></td>
<td>ANSWERING A MESSAGE (INTERNET STYLE)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-BACKUP</p>
</blockquote></td>
<td>BACKING UP THE MESSAGE DISPLAY</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-BACKUP BEFORE SENDING</p>
</blockquote></td>
<td>BACKUP A MESSAGE TO REVIEW BEFORE SENDING</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-BROWSER</p>
</blockquote></td>
<td>PRINTING TO THE BROWSER</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-CHOOSE RANGE</p>
</blockquote></td>
<td>SPECIFYING A LIST OR RANGE OF MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-CHOOSE RESPONSES</p>
</blockquote></td>
<td>SPECIFYING A LIST OR RANGE OF RESPONSES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-CHOOSE SELECT</p>
</blockquote></td>
<td>SELECTING MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-CHOOSE SELECT-2</p>
</blockquote></td>
<td>SELECTING MESSAGES (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-CLOSED</p>
</blockquote></td>
<td>CLOSED MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-CONFIDENTIAL</p>
</blockquote></td>
<td>MAKING A MESSAGE CONFIDENTIAL</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-CONFIRM RECEIPT</p>
</blockquote></td>
<td>REQUESTING CONFIRMATION BEFORE SENDING A MESSAGE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-COPY</p>
</blockquote></td>
<td>COPYING A MESSAGE INTO A NEW MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-COPY-2</p>
</blockquote></td>
<td>RESPONSES TO THE COPY OPTION PROMPTS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-DELETE</p>
</blockquote></td>
<td>DELETING MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-DELETE-2</p>
</blockquote></td>
<td>DELETING MESSAGES (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-DELETE-3</p>
</blockquote></td>
<td>DELETING MESSAGES (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-DELIVERY BASKET SET</p>
</blockquote></td>
<td>DELIVERY BASKET SET OPTION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-EDIT RECIPIENTS</p>
</blockquote></td>
<td>EDIT RECIPIENTS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-EDIT SUBJECT</p>
</blockquote></td>
<td>EDIT THE SUBJECT OF A MESSAGE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-EDIT TEXT</p>
</blockquote></td>
<td>EDIT THE TEXT OF A MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-FORWARD</p>
</blockquote></td>
<td>FORWARDING MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-FORWARD-2</p>
</blockquote></td>
<td>FORWARDING MESSAGES (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-INCLUDE MESSAGE</p>
</blockquote></td>
<td>INCLUDING A MESSAGE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-INFO ONLY</p>
</blockquote></td>
<td>MESSAGES MARKED AS INFORMATION ONLY</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-LATER</p>
</blockquote></td>
<td>MAKE MESSAGES NEW LATER</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-LATER-2</p>
</blockquote></td>
<td>MAKE MESSAGES NEW LATER (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-LATER-3</p>
</blockquote></td>
<td>MAKE MESSAGES NEW LATER (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-LATERED MESSAGE CHANGE</p>
</blockquote></td>
<td>CHANGE/DELETE LATERED MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-LATERED MESSAGE REPORT</p>
</blockquote></td>
<td>REPORT ON LATERED MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-MESSAGE HEADER</p>
</blockquote></td>
<td>WHAT APPEARS IN THE MESSAGE HEADER</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-NETWORK SIGNATURE</p>
</blockquote></td>
<td>ADD YOUR NETWORK SIGNATURE TO A MESSAGE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-NEW</p>
</blockquote></td>
<td>FORCING A MESSAGE TO APPEAR AS NEW</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-NEW-2</p>
</blockquote></td>
<td>MAKE NEW MESSAGES NOT NEW AND VICE VERSA (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-MO-EDIT</p>
</blockquote></td>
<td>EDITING A MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-MO-READ</p>
</blockquote></td>
<td>READING A MESSAGE - OPTIONS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-MO-READ-2</p>
</blockquote></td>
<td>READING A MESSAGE - OPTIONS (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-MO-REPLY</p>
</blockquote></td>
<td>REPLYING TO A MESSAGE - OPTIONS AT THE 'Transmit' PROMPT</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-MO-SEND</p>
</blockquote></td>
<td>SENDING A MESSAGE - OPTIONS AT THE 'Transmit' PROMPT</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-MO-SEND-2</p>
</blockquote></td>
<td>MORE MESSAGE OPTIONS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-PRINT</p>
</blockquote></td>
<td>PRINTING MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-PRINT DEVICE P-MESSAGE</p>
</blockquote></td>
<td>P-MESSAGE DEVICE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-PRINT HEADER</p>
</blockquote></td>
<td>IDENTIFYING YOUR MESSAGE PRINTOUT</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-PRINT NO HEADER</p>
</blockquote></td>
<td>HEADERLESS PRINTING</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-PRINT NO HEADER-2</p>
</blockquote></td>
<td>HEADERLESS PRINTING (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-PRINT-2</p>
</blockquote></td>
<td>PRINTING MESSAGES (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-PRIORITY SEND</p>
</blockquote></td>
<td>SENDING MESSAGES WITH A PRIORITY STATUS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-PRIORITY TOGGLE</p>
</blockquote></td>
<td>PRIORITY REPLIES TOGGLE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-QUERY</p>
</blockquote></td>
<td>QUERYING A MESSAGE FOR ITS STATUS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-QUERY DETAILED</p>
</blockquote></td>
<td>DETAILED QUERY ON A MESSAGE</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-QUERY GENERAL</p>
</blockquote></td>
<td>GENERAL QUERY ON A MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-QUERY INFO BASIC</p>
</blockquote></td>
<td>BASIC QUERY INFORMATION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-QUERY INFO LOCAL</p>
</blockquote></td>
<td>LOCAL USER QUERY INFORMATION</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-QUERY INFO REMOTE</p>
</blockquote></td>
<td>REMOTE USER QUERY INFORMATION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-QUERY NETWORK</p>
</blockquote></td>
<td>NETWORK QUERY ON A MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-QUERY NETWORK-2</p>
</blockquote></td>
<td>NETWORK QUERY ON A MESSAGE (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-QUERY SPECIFIC</p>
</blockquote></td>
<td>SPECIFIC QUERY ON A MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-QUERY-2</p>
</blockquote></td>
<td>QUERYING A MESSAGE FOR ITS STATUS (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-REPLY</p>
</blockquote></td>
<td>REPLYING TO A MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-REPLY INCLUDE</p>
</blockquote></td>
<td>INCLUDE PREVIOUS RESPONSES IN YOUR REPLY</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-REPLY-2</p>
</blockquote></td>
<td>REPLYING TO A MESSAGE (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-SAVE</p>
</blockquote></td>
<td>SAVING MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-SCRAMBLE</p>
</blockquote></td>
<td>SCRAMBLING A MESSAGE BEFORE SENDING</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-SCRAMBLE HINT</p>
</blockquote></td>
<td>RESPONDING TO 'Enter Scramble Hint'</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-SCRAMBLE PASSWORD</p>
</blockquote></td>
<td>RESPONDING TO 'Enter Scramble Password'</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-SEND</p>
</blockquote></td>
<td>USING THE 'Send a message' OPTION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-TERMINATE</p>
</blockquote></td>
<td>TERMINATING MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-TERMINATE-2</p>
</blockquote></td>
<td>TERMINATING MESSAGES (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-TRANSMIT LATER</p>
</blockquote></td>
<td>SEND A MESSAGE LATER (DEFER)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-TRANSMIT NOW</p>
</blockquote></td>
<td>SEND A MESSAGE NOW ('Transmit Now')</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-VAPORIZE DATE EDIT</p>
</blockquote></td>
<td>VAPORIZE MESSAGE WITH AUTOMATIC DELETION DATE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-VAPORIZE DATE EDIT-2</p>
</blockquote></td>
<td>VAPORIZE DATES (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-VAPORIZE DATE SEND</p>
</blockquote></td>
<td>SET A VAPORIZE DATE WHEN SENDING A MESSAGE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-M-WRITE</p>
</blockquote></td>
<td>SENDING A NEW MESSAGE INSTEAD OF A REPLY</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-M-WRITE-2</p>
</blockquote></td>
<td>SENDING A NEW MESSAGE INSTEAD OF A REPLY (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-NEW FEATURES</p>
</blockquote></td>
<td>NEW FEATURES AND FUNCTIONALITY</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-ASK BASKET</p>
</blockquote></td>
<td>THE 'ASK BASKET' PROMPT</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-BANNER</p>
</blockquote></td>
<td>THE MAILMAN BANNER</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-DELIVERY BASKET PRIV</p>
</blockquote></td>
<td>DELIVERY BASKET PRIVILEGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-EDITOR</p>
</blockquote></td>
<td>PREFERRED EDITOR</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-FILTER</p>
</blockquote></td>
<td>FILTERING MAIL</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-FILTER ACTIONS</p>
</blockquote></td>
<td>FILTERING MAIL ACTIONS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-FILTER CRITERIA</p>
</blockquote></td>
<td>FILTERING MAIL CRITERIA</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-FILTER CRITERIA-2</p>
</blockquote></td>
<td>FILTERING MAIL CRITERIA (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-FILTER ORDER</p>
</blockquote></td>
<td>FILTERING MAIL - ORDER FIELD</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-FILTER-2</p>
</blockquote></td>
<td>FILTERING MAIL (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-FILTER-3</p>
</blockquote></td>
<td>FILTERING MAIL (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-FORWARDING ADDRESS</p>
</blockquote></td>
<td>HOW TO USE THE FORWARDING ADDRESS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-GROUP ENROLL</p>
</blockquote></td>
<td>PUBLIC MAIL GROUPS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-GROUP ENROLL-2</p>
</blockquote></td>
<td>PUBLIC MAIL GROUPS (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-GROUP PERSONAL</p>
</blockquote></td>
<td>PERSONAL MAIL GROUPS</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-GROUP PERSONAL-2</p>
</blockquote></td>
<td>PERSONAL MAIL GROUPS (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-INSTITUTION</p>
</blockquote></td>
<td>MAILMAN INSTITUTION</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-INTRODUCTION</p>
</blockquote></td>
<td>INTRODUCING YOURSELF IN MAILMAN</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-MESSAGE ACTION DEFAULT</p>
</blockquote></td>
<td>MESSAGE ACTION DEFAULT</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-MESSAGE ORDER</p>
</blockquote></td>
<td>MESSAGE LIST ORDER</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-NETWORK SIGNATURE</p>
</blockquote></td>
<td>NETWORK SIGNATURE</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-NEW MESSAGES OPTION</p>
</blockquote></td>
<td>NEW MESSAGES DEFAULT OPTION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-NEW MESSAGES READ ORDER</p>
</blockquote></td>
<td>NEW MESSAGES READ ORDER</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-OFFICE INFO</p>
</blockquote></td>
<td>CONTACT INFORMATION</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-OPTIONS</p>
</blockquote></td>
<td>PERSONAL PREFERENCES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-OPTIONS-2</p>
</blockquote></td>
<td>PERSONAL PREFERENCES (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-OPTIONS-3</p>
</blockquote></td>
<td>PERSONAL PREFERENCES (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-OPTIONS-4</p>
</blockquote></td>
<td>PERSONAL PREFERENCES (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-PERSONAL PREFERENCES</p>
</blockquote></td>
<td>PERSONAL PREFERENCES MENU</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-P-MESSAGE FROM</p>
</blockquote></td>
<td>P-MESSAGE FROM</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-PRIORITY FLAG</p>
</blockquote></td>
<td>PRIORITY RESPONSES FLAG</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-PRIORITY PROMPT</p>
</blockquote></td>
<td>PRIORITY RESPONSES PROMPT</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-PRIORITY PROMPT-2</p>
</blockquote></td>
<td>PRIORITY RESPONSES PROMPT (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-READ NEW MSGS BSKT</p>
</blockquote></td>
<td>READ NEW MESSAGES BASKET PRIORITY</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-READER DEFAULT</p>
</blockquote></td>
<td>DEFAULT MESSAGE READER</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-READER PROMPT</p>
</blockquote></td>
<td>MESSAGE READER PROMPT</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-SHOW MESSAGE PREVIEW</p>
</blockquote></td>
<td>SHOW MESSAGE PREVIEW</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-SHOW TITLES</p>
</blockquote></td>
<td>SHOW TITLES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-SURROGATE EDIT</p>
</blockquote></td>
<td>SURROGATES - DESIGNATING SURROGATES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-P-SURROGATE READ PRIV</p>
</blockquote></td>
<td>SURROGATES - READ PRIVILEGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-P-SURROGATE WRITE PRIV</p>
</blockquote></td>
<td>SURROGATES - WRITE PRIVILEGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-Q-CLASSIC LOOKUP ?</p>
</blockquote></td>
<td>LOOKING FOR MESSAGES WHOSE SUBJECT CONTAINS A SPECIFIC STRING</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-Q-CLASSIC LOOKUP ??</p>
</blockquote></td>
<td>LOOKING FOR MESSAGES WHOSE SUBJECT BEGINS WITH A SPECIFIC STRING</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-Q-REMOTE USER NAME</p>
</blockquote></td>
<td>ENTERING A REMOTE USER'S NAME WHEN FILTERING OR SEARCHING MAIL</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-Q-SEARCH</p>
</blockquote></td>
<td>SEARCHING FOR MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-Q-SEARCH CRITERIA</p>
</blockquote></td>
<td>SEARCHING FOR MESSAGES - SEARCH CRITERIA</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-Q-SEARCH CRITERIA DATE</p>
</blockquote></td>
<td>SEARCH CRITERIA - DATE SENT</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-Q-SEARCH CRITERIA TEXT</p>
</blockquote></td>
<td>SEARCH CRITERIA - TEXT CONTENTS</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-Q-SEARCH CRITERIA USERS</p>
</blockquote></td>
<td>SEARCH CRITERIA - SENDERS AND ADDRESSEES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-Q-SEARCH CRITERIA-2</p>
</blockquote></td>
<td>SEARCH CRITERIA (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-Q-SEARCH MAILBOX</p>
</blockquote></td>
<td>SEARCHING FOR MESSAGES - SEARCHING YOUR MAILBOX</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-Q-SEARCH SYSTEM</p>
</blockquote></td>
<td>SEARCHING FOR MESSAGES - ANYWHERE ON THE SYSTEM</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-R-NEW LIST ALL</p>
</blockquote></td>
<td>LIST ALL NEW MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-R-NEW LIST BASKETS</p>
</blockquote></td>
<td>LIST BASKETS WITH NEW MAIL</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-R-NEW LIST PRIORITY</p>
</blockquote></td>
<td>LIST ALL PRIORITY MESSAGES</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-R-NEW PRINT</p>
</blockquote></td>
<td>PRINT ALL NEW MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-R-NEW READ</p>
</blockquote></td>
<td>READ NEW MAIL BY BASKET</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-R-NEW SCAN</p>
</blockquote></td>
<td>SCAN ALL NEW MESSAGES</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-R-READ</p>
</blockquote></td>
<td>READING AND MANAGING YOUR MAIL</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-R-READ NEW</p>
</blockquote></td>
<td>PROCESSING NEW MAIL</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-R-READ NEW-2</p>
</blockquote></td>
<td>PROCESSING NEW MAIL (CONTINUED)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XM-U-R-READ-2</p>
</blockquote></td>
<td>READING AND MANAGING YOUR MAIL (CONTINUED)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>XM-U-R-READ-3</p>
</blockquote></td>
<td>READING AND MANAGING YOUR MAIL (CONTINUED)</td>
</tr>
</tbody>
</table>

<span id="_Hlt448223095" class="anchor"></span>Table A-2. MailMan help frames

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$
\$\$ACCESS^XMXSEC, 7-8
\$\$ANSWER^XMXSEC, 7-8
\$\$BCAST^XMXSEC, 7-8
\$\$BMSGCT^XMXUTIL, 7-10
\$\$BNMSGCT^XMXUTIL, 7-10
\$\$BPMSGCT^XMXUTIL, 7-10
\$\$BSKT^XMAD2, 7-3
\$\$BSKT^XMXUTIL2, 7-12
\$\$BSKTNAME^XMXUTIL, 7-10
\$\$CLOSED^XMXSEC, 7-8
\$\$CONFID^XMXSEC, 7-8
\$\$CONFIRM^XMXSEC, 7-8
\$\$CONVERT^XMXUTIL1, 7-11
\$\$COPY^XMXSEC, 7-8
\$\$COPYAMT^XMXSEC1, 7-10
\$\$COPYLIMS^XMXSEC1, 7-10
\$\$COPYRECP^XMXSEC1, 7-10
\$\$CTRL^XMXUTIL1, 7-11
\$\$DATE^XMXUTIL2, 7-12
\$\$DECODEUP^XMCU1 API, 7-4
\$\$DECODEUP^XMXUTIL1, 7-11
\$\$DELETE^XMXSEC, 7-9
\$\$DM^XMBGRP, 7-4
\$\$EDIT^XMXSEC2, 7-10
\$\$ENCODEUP^XMCU1 API, 7-4
\$\$ENCODEUP^XMXUTIL1, 7-11
\$\$ENT^XMA2R, 7-3
\$\$ENTA^XMA2R, 7-3
\$\$FORWARD^XMXSEC, 7-9
\$\$FROM^XMXUTIL2, 7-12
\$\$GMTDIFF^XMXUTIL1, 7-11
\$\$GOTLOCAL^XMXAPIG, 7-8
\$\$HDR^XMGAPI2, 7-5
\$\$INDT^XMXUTIL1, 7-11
\$\$INFO^XMA11 API, 7-2
\$\$INFO^XMXSEC, 7-9
\$\$KSEQN^XMXUTIL2, 7-13
\$\$LATER^XMXSEC, 7-9
\$\$LINE^XMXUTIL2, 7-13
\$\$MAXBLANK^XMXUTIL1, 7-11
\$\$MELD^XMXUTIL1, 7-12
\$\$MG^XMBGRP, 7-4
\$\$MMDT^XMXUTIL1, 7-12
\$\$MOVE^XMXSEC, 7-9
\$\$NAME^XMXUTIL, 7-11
\$\$NAMEFMT^XLFNAME API, 2-13
\$\$NET^XMRENT, 7-5
\$\$NETNAME^XMXUTIL, 7-11
\$\$NEW^XMXUTIL2, 7-13
\$\$NEWS^XMXUTIL, 7-11
\$\$NU^XM, 7-1
\$\$ORIGIN8R^XMXSEC, 7-9
\$\$PAKMAN^XMXSEC1, 7-10
\$\$POSTPRIV^XMXSEC, 7-9
\$\$PRI^XMXUTIL2, 7-13
\$\$PRIORITY^XMXSEC, 7-9
\$\$QRESP^XMXUTIL2, 7-13
\$\$READ^XMGAPI1, 7-5
\$\$READ^XMXSEC, 7-9
\$\$REN^XMA03, 7-2
\$\$REPLY^XMXSEC, 7-9
\$\$RESP^XMXUTIL2, 7-13
\$\$RPRIV^XMXSEC, 7-9
\$\$RTRAN^XMCU1 API, 7-4
\$\$RWPRIV^XMXSEC, 7-9
\$\$SCRUB^XMXUTIL1, 7-12
\$\$SEND^XMXSEC, 7-9
\$\$SRVTIME^XMS1, 7-5
\$\$SSPRIV^XMXSEC1, 7-10
\$\$STATUS^XMS1, 7-5
\$\$STRAN^XMCU1 API, 7-4
\$\$STRIP^XMXUTIL1, 7-12
\$\$SUBCHK^XMGAPI0 API, 7-5
\$\$SUBGET^XMGAPI0, 7-5
\$\$SUBJ^XMXUTIL2, 7-13
\$\$SURRACC^XMXSEC, 7-9
\$\$SURRCONF^XMXSEC, 7-9
\$\$TIMEDIFF^XMXUTIL1, 7-12
\$\$TMSGCT^XMXUTIL, 7-11
\$\$TNMSGCT^XMXUTIL, 7-11
\$\$TPMSGCT^XMXUTIL, 7-11
\$\$TSTAMP^XMXUTIL1, 7-12
\$\$WPRIV^XMXSEC, 7-9
\$\$ZCLOSED^XMXSEC, 7-9
\$\$ZCONFID^XMXSEC, 7-9
\$\$ZCONFIRM^XMXSEC, 7-9
\$\$ZDATE^XMXUTIL2, 7-13
\$\$ZFROM^XMXUTIL2, 7-13
\$\$ZINFO^XMXSEC, 7-9
\$\$ZNODE^XMXUTIL2, 7-13
\$\$ZORIGIN8^XMXSEC, 7-9
\$\$ZPOSTPRV^XMXSEC, 7-10
\$\$ZPRI^XMXSEC, 7-10
\$\$ZPRI^XMXUTIL2, 7-13
\$\$ZREAD^XMXUTIL2, 7-13
\$\$ZSSPRIV^XMXSEC1, 7-10
\$\$ZSUBJ^XMXUTIL2, 7-13
%
%ZISL Global, 4-5
%ZTSK Global, 5-48, 5-49
^
^XM API, 7-1
^XMAH1 API, 7-3
^XMB, 7-4
^XMD API, 7-4
A
Acronyms (ISS)
Home Page Web Address, Glossary, 2
ACTIVE by Custodial Package Option, 8-1
Active Users/Deliveries Report Option, 2-22, 5-25
Actively Transmitting/Receiving Queues Report Option, 5-46
ADDMBRS^XMXAPIG, 7-8
ADDRNSND^XMXAPI, 7-6
Adobe Acrobat Quick Guide Web Address, xii
Adobe Home Page Web Address, xii
AI x-Ref Purge of Received Network Messages Option, 2-3, 2-15, 5-34
Alerts, 11-1
AML
Become a Surrogate (SHARED,MAIL or Other) Option, 5-13
ANSRMSG^XMXAPI, 7-6
APIs, 7-1
\$\$ACCESS^XMXSEC, 7-8
\$\$ANSWER^XMXSEC, 7-8
\$\$BCAST^XMXSEC, 7-8
\$\$BMSGCT^XMXUTIL, 7-10
\$\$BNMSGCT^XMXUTIL, 7-10
\$\$BPMSGCT^XMXUTIL, 7-10
\$\$BSKT^XMAD2, 7-3
\$\$BSKT^XMXUTIL2, 7-12
\$\$BSKTNAME^XMXUTIL, 7-10
\$\$CLOSED^XMXSEC, 7-8
\$\$CONFID^XMXSEC, 7-8
\$\$CONFIRM^XMXSEC, 7-8
\$\$CONVERT^XMXUTIL1, 7-11
\$\$COPY^XMXSEC, 7-8
\$\$COPYAMT^XMXSEC1, 7-10
\$\$COPYLIMS^XMXSEC1, 7-10
\$\$COPYRECP^XMXSEC1, 7-10
\$\$CTRL^XMXUTIL1, 7-11
\$\$DATE^XMXUTIL2, 7-12
\$\$DECODEUP^XMCU1, 7-4
\$\$DECODEUP^XMXUTIL1, 7-11
\$\$DELETE^XMXSEC, 7-9
\$\$DM^XMBGRP, 7-4
\$\$EDIT^XMXSEC2, 7-10
\$\$ENCODEUP^XMCU1, 7-4
\$\$ENCODEUP^XMXUTIL1, 7-11
\$\$ENT^XMA2R, 7-3
\$\$ENTA^XMA2R, 7-3
\$\$FMTE^XLFDT (Date/Time Format API), 2-12
\$\$FORWARD^XMXSEC, 7-9
\$\$FROM^XMXUTIL2, 7-12
\$\$GMTDIFF^XMXUTIL1, 7-11
\$\$GOTLOCAL^XMXAPIG, 7-8
\$\$HDR^XMGAPI2, 7-5
\$\$INDT^XMXUTIL1, 7-11
\$\$INFO^XMA11, 7-2
\$\$INFO^XMXSEC, 7-9
\$\$KSEQN^XMXUTIL2, 7-13
\$\$LATER^XMXSEC, 7-9
\$\$LINE^XMXUTIL2, 7-13
\$\$MAXBLANK^XMXUTIL1, 7-11
\$\$MELD^XMXUTIL1, 7-12
\$\$MG^XMBGRP, 7-4
\$\$MMDT^XMXUTIL1, 7-12
\$\$MOVE^XMXSEC, 7-9
\$\$NAME^XMXUTIL, 7-11
\$\$NAMEFMT^XLFNAME API, 2-13
\$\$NET^XMRENT, 7-5
\$\$NETNAME^XMXUTIL, 7-11
\$\$NEW^XMXUTIL2, 7-13
\$\$NEWS^XMXUTIL, 7-11
\$\$NU^XM, 7-1
\$\$ORIGIN8R^XMXSEC, 7-9
\$\$PAKMAN^XMXSEC1, 7-10
\$\$POSTPRIV^XMXSEC, 7-9
\$\$PRI^XMXUTIL2, 7-13
\$\$PRIORITY^XMXSEC, 7-9
\$\$QRESP^XMXUTIL2, 7-13
\$\$READ^XMGAPI1, 7-5
\$\$READ^XMXSEC, 7-9
\$\$REN^XMA03, 7-2
\$\$REPLY^XMXSEC, 7-9
\$\$RESP^XMXUTIL2, 7-13
\$\$RPRIV^XMXSEC, 7-9
\$\$RTRAN^XMCU1, 7-4
\$\$RWPRIV^XMXSEC, 7-9
\$\$SCRUB^XMXUTIL1, 7-12
\$\$SEND^XMXSEC, 7-9
\$\$SRVTIME^XMS1, 7-5
\$\$SSPRIV^XMXSEC1, 7-10
\$\$STATUS^XMS1, 7-5
\$\$STRAN^XMCU1, 7-4
\$\$STRIP^XMXUTIL1, 7-12
\$\$SUBCHK^XMGAPI0, 7-5
\$\$SUBGET^XMGAPI0, 7-5
\$\$SUBJ^XMXUTIL2, 7-13
\$\$SURRACC^XMXSEC, 7-9
\$\$SURRCONF^XMXSEC, 7-9
\$\$TIMEDIFF^XMXUTIL1, 7-12
\$\$TMSGCT^XMXUTIL, 7-11
\$\$TNMSGCT^XMXUTIL, 7-11
\$\$TPMSGCT^XMXUTIL, 7-11
\$\$TSTAMP^XMXUTIL1, 7-12
\$\$WPRIV^XMXSEC, 7-9
\$\$ZCLOSED^XMXSEC, 7-9
\$\$ZCONFID^XMXSEC, 7-9
\$\$ZCONFIRM^XMXSEC, 7-9
\$\$ZDATE^XMXUTIL2, 7-13
\$\$ZFROM^XMXUTIL2, 7-13
\$\$ZINFO^XMXSEC, 7-9
\$\$ZNODE^XMXUTIL2, 7-13
\$\$ZORIGIN8^XMXSEC, 7-9
\$\$ZPOSTPRV^XMXSEC, 7-10
\$\$ZPRI^XMXSEC, 7-10
\$\$ZPRI^XMXUTIL2, 7-13
\$\$ZREAD^XMXUTIL2, 7-13
\$\$ZSSPRIV^XMXSEC1, 7-10
\$\$ZSUBJ^XMXUTIL2, 7-13
^XM, 7-1
^XMB, 7-4
^XMD, 7-4
ADDMBRS^XMXAPIG, 7-8
ADDRNSND^XMXAPI, 7-6
ANSRMSG^XMXAPI, 7-6
BULL^XMB, 7-4
CHECKIN^XM, 7-1
CHECKOUT^XM, 7-1
CHK^XMA21, 7-3
CHKLINES^XMXSEC1, 7-10
CHKMSG^XMXSEC1, 7-10
CLOSED^XMXEDIT, 7-8
CONFID^XMXEDIT, 7-8
CONFIRM^XMXEDIT, 7-8
CRE8BSKT^XMXAPIB, 7-7
CRE8MBOX^XMXAPIB, 7-7
CRE8XMZ^XMXAPI, 7-6
DELBSKT^XMXAPIB, 7-7
DELIVER^XMXEDIT, 7-8
DELMSG^XMXAPI, 7-6
DES^XMA21, 7-3
DEST^XMA21, 7-3
DROP^XMXAPIG, 7-8
EN^XM, 7-1
EN^XMB, 7-4
EN1^XMD, 7-4
ENL^XMD, 7-4
ENT^XMD, 7-4
ENT^XMPG, 7-5
ENT^XMUT7, 7-5
ENT1^XMD, 7-5
ENT2^XMD, 7-5
ENT8^XMAH, 7-3
ENTA^XMAH1, 7-4
ENTPRT^XMA0, 7-1
FLTRBSKT^XMXAPIB, 7-7
FLTRMBOX^XMXAPIB, 7-7
FLTRMSG^XMXAPI, 7-6
FWDMSG^XMXAPI, 7-6
GET^XMA2, 7-2
GET^XML, 7-5
GETRESTR^XMXSEC1, 7-10
GO^XMCTLK, 7-4
HDR^XMA0, 7-2
HEADER^XM, 7-1
INFO^XMXEDIT, 7-8
INIT^XMVVITAE, 7-5
INMSG^XMXUTIL2, 7-12
INMSG1^XMXUTIL2, 7-12
INMSG2^XMXUTIL2, 7-12
INRESP^XMXUTIL2, 7-13
INRESPS^XMXUTIL2, 7-13
INST^XMA21, 7-3
JOIN^XMXAPIG, 7-8
KILL^XM, 7-1
KL^XMA1B, 7-2
KLQ^XMA1B, 7-2
KVAPOR^XMXUTIL, 7-10
LASTACC^XMXUTIL, 7-11
LATERMSG^XMXAPI, 7-6
LISTBSKT^XMXAPIB, 7-7
LISTMSGS^XMXAPIB, 7-7
MAIL^XLFNSLK (DNS Lookup API), 2-11
MAKENEW^XMXUTIL, 7-11
MOVEMSG^XMXAPI, 7-6
N1^XM, 7-1
NAMEBSKT^XMXAPIB, 7-7
NEW^XM, 7-1
NONEW^XMXUTIL, 7-11
OPTEDIT^XMXSEC2, 7-10
OPTGRP^XMXSEC1, 7-10
OPTMSG^XMXSEC2, 7-10
OTHER^XMVVITAE, 7-5
PAGE^XMXUTIL, 7-11
PR2^XMA0, 7-2
PRIORITY^XMXEDIT, 7-8
PRTMSG^XMXAPI, 7-6
PUTSERV^XMXAPI, 7-6
Q^XMXUTIL3, 7-13
QBSKT^XMXAPIB, 7-7
QD^XMXUTIL3, 7-13
QL^XMXUTIL3, 7-13
QMBOX^XMXAPIB, 7-7
QN^XMXUTIL3, 7-14
QX^XMXUTIL3, 7-14
READ^XMXAPIU, 7-8
READNEW^XMXAPIU, 7-8
REC^XMA, 7-1
REC^XMS3, 7-5
REMSBMSG^XMA1C, 7-2
REPLYMSG^XMXAPI, 7-6
RSEQBSKT^XMXAPIB, 7-7
S2^XMA1B, 7-2
SELF^XMVVITAE, 7-6
SEND^XMXAPIU, 7-8
SENDBULL^XMXAPI, 7-6
SENDMSG^XMXAPI, 7-6
SETSB^XMA1C, 7-2
SUBJ^XMXEDIT, 7-8
TASKBULL^XMXAPI, 7-7
TERMMBOX^XMXAPIB, 7-7
TERMMSG^XMXAPI, 7-7
TEST^XMUPIN, 2-9
TEXT^XMXEDIT, 7-8
TOWHOM^XMXAPI, 7-7
TOWHOM^XMXAPIU, 7-8
VAPOR^XMXEDIT, 7-8
VAPORMSG^XMXAPI, 7-7
VSUBJ^XMXAPI, 7-7
WAIT^XMXUTIL, 7-11
WHO^XMA21, 7-3
WRITE^XMA11A, 7-2
XMAH1, 7-3
XMZ^XMA2, 7-3
ZAPSERV^XMXAPI, 7-7
ZONEDIFF^XMXUTIL1, 7-12
ZTSK^XMADGO, 7-3
Appendix A—Help Frames, 1
Application Entry Points, 7-1
Archiving, 6-1, 11-2
ARRIVING Basket, 2-7
Ask users with many messages to do maintenance Option, 2-3, 2-15, 5-29
Assume the Identity of SHARED,MAIL Option, 5-52
Assumptions About the Reader, xi
AUTO-FORWARD APPROVED SITE Multiple Field (#31.1), 11-3
AUTO-FORWARD LIMITED? field (#31), 11-3
AUTO-FORWARD WAIVER SITE Multiple field (#31.2), 11-3
AUTOMATIC INTEGRITY CHECK Field (#4.303), 5-14
Automatic Purge of MailMan Messages Option, 2-4, 5-14
B
Background Filer, 2-24, 5-35
Background Filer (XMAD) Option, 5-25
Banner Edit Option, 5-15
Become a Surrogate (SHARED,MAIL or Other) Option, 5-13
Broadcast Messages
Postmaster, 2-7
With Responses, 2-13
BULL^XMB, 7-4
Bulletin edit Option, 2-21, 5-18
BULLETIN File (#3.6), 2-10, 2-14, 4-2, 5-24, 9-1
Security, 11-5
Bulletins, 1-1, 2-8
Post a bulletin Option, 5-43
XM BANNER MESSAGE, 2-8
XM DATE PURGE WARNING, 2-8
XM DOMAIN ADDED, 2-8
XM FILTER FWD ADDRESS DELETE, 2-8
XM FWD ADDRESS CHANGE, 2-8
XM FWD ADDRESS CHECK, 2-8
XM FWD ADDRESS DELETE, 2-8
XM GROUP EDIT NOTIFY, 2-8
XM GROUP ERROR, 2-8
XM IN BASKET PURGE REQUEST, 2-9
XM IN BASKET PURGE WARNING, 2-9
XM RELAY ATTEMPTED, 2-9
XM SEND ERR MSG, 2-9
XM SEND ERR RECIPIENT, 2-9
XM SEND ERR REMOTE MSG ID, 2-9
XM SEND ERR SERVER MSG, 2-9
XM SEND ERR TRANSMISSION, 2-9
XM SUPER SEARCH, 2-10, 5-12
XM TOO MANY MESSAGES, 2-10
XM_TRANSMISSION_ERROR, 2-10
XMNEWUSER, 2-10
XMRDACK, 2-10
XMVALBAD, 2-10
C
Callable Routines, 7-1
Callout Boxes, x
Capture, 1-1
Change/Delete Later'd Messages Option, 5-23
CHARACTERS RECEIVED Field (#105), 4-6
CHARACTERS SENT Field (#104), 4-6
CHECK background filer Option, 2-22, 5-26
Check MailMan Files for Errors Option, 2-5, 2-14, 5-55
CHECKIN^XM, 7-1
CHECKOUT^XM, 7-1
CHK^XMA21, 7-3
CHKLINES^XMXSEC1, 7-10
CHKMSG^XMXSEC1, 7-10
Christen a domain Option, 2-24, 5-15, 5-23
Clean out waste baskets Option, 2-4, 2-16, 5-16
CLOSED^XMXEDIT, 7-8
Communications Option, 5-42
COMMUNICATIONS PROTOCOL File (#3.4), 2-11, 4-2, 4-7, 9-1
Security, 11-5
Communications Protocols, 4-2
Compare Domains in System Against Released List Option, 5-47
Compare message Option, 5-43
Compile Response Time Statistics Option, 2-23, 5-34
CONFID^XMXEDIT, 7-8
CONFIRM^XMXEDIT, 7-8
Contents, v
Controlled Procedures, 2-1
COORDINATOR Field (#5.1), 4-3
Coordinator For a Mail Group, 5-21
CRE8BSKT^XMXAPIB, 7-7
CRE8MBOX^XMXAPIB, 7-7
CRE8XMZ^XMXAPI, 7-6
Create a Mailbox for a user Option, 2-15, 5-33
Cross-reference
AI, 2-15
Custodial Package Menu, 8-1
D
Data Dictionary
Data Dictionary Utilities Menu, xi
Listings, xi
Data Dictionary Utilities Menu, 9-2
DATE 'LAST REFERENCED' Field, 2-6
Date/Times
Format API
\$\$FMTE^XLFDT, 2-12
Reformatted, 2-12
DBA IA CUSTODIAL MENU, 8-1
DBA IA CUSTODIAL Option, 8-1
DBA IA INQUIRY Option, 8-2
DBA IA ISC Menu, 8-1, 8-2
DBA IA SUBSCRIBER MENU, 8-2
DBA IA SUBSCRIBER Option, 8-2
DBA Menu, 8-1, 8-2
DELBSKT^XMXAPIB, 7-7
Delete Found Messages from Found Messages List Option, 2-18, 5-56
Deliver Found Messages into User's IN Basket Option, 2-18, 5-56
DELIVER^XMXEDIT, 7-8
Deliveries by Group Option, 2-23, 5-25
Delivery Basket Edit Option, 5-11
Delivery Queue Statistics Collection Option, 2-23, 5-27
Delivery Queues Wait Report Option, 5-26
DELMSG^XMXAPI, 7-6
DES^XMA21, 7-3
DEST^XMA21, 7-3
DI DDMAP Option, 5-1, 9-2
DI DDU, 9-2
Diagnostics Menu, 5-16, 5-17, 5-43
Diagram
Menus, 5-1
DIALOGUE CAPTURE, 1-1
DIRECTION Field (#8), 4-6
Directives, 11-6
10-93-142, 11-6
Disk Space Management, 2-3
Disk Space Management Menu, 2-3, 2-15, 5-16, 5-29, 5-30, 5-31, 5-32, 5-34, 5-36, 5-37, 5-38, 5-45, 5-46, 5-53, 5-57, 6-1
Display Active & Inactive Message Queues Option, 5-46
DISTRIBUTION LIST File (#3.816), 4-3, 9-1
Security, 11-6
DNS AWARE Field (#8.22), 2-11, 4-7
DNS IP Field (#51), 2-11
DNS-Aware MailMan, 2-11
Namespace, 9-1
Documentation
History, iii
Symbols, ix
Domain, 1-1
Baskets, Postmaster, 2-7
DOMAIN File (#4.2), 2-7, 2-11, 3-6, 4-4, 5-46, 5-47, 5-50, 9-1, 10-1, 11-4
Glossary, 2
Security, 11-6
Security Keys, 11-4
DROP OUT OF RESTRICTED GROUP Field (#22), 5-21
DROP^XMXAPIG, 7-8
DUZ=.5, 2-2
E
Edit a script Option, 5-50
Edit Distribution List Option, 2-21, 5-18
Edit numbers to Normalize Reports Option, 2-23, 5-25
Electronic Signatures, 11-2
EN^XM, 7-1
EN^XMB, 7-4
EN1^XMD API, 7-4
Enhanced Routines, 2-13
ENL^XMD API, 7-4
Enroll in (or Disenroll from) a Mail Group Option, 2-21, 5-20
ENT^XMD API, 7-4
ENT^XMPG API, 7-5
ENT^XMUT7 API, 7-5
ENT1^XMD API, 7-5
ENT2^XMD API, 7-5
ENT8^XMAH, 7-3
ENTA^XMAH1, 7-4
Enter/Edit Directory Request Flags by Group Option, 2-25, 5-27
Enter/Edit Remote User Option, 2-25, 5-18
ENTPRT^XMA0, 7-1
Entry Points, 7-1
EVS Anonymous Directories, xiii
Exported Options, 5-1
Extended Search, 1-1
External Relations, 8-1
F
Features, 2-11
Fields
AUTO-FORWARD APPROVED SITE Multiple (#31.1), 11-3
AUTO-FORWARD LIMITED? (#31), 11-3
AUTO-FORWARD WAIVER SITE Multiple (#31.2), 11-3
AUTOMATIC INTEGRITY CHECK (#4.303), 5-14
CHARACTERS RECEIVED (#105), 4-6
CHARACTERS SENT (#104), 4-6
COORDINATOR (#5.1), 4-3
DATE 'LAST REFERENCED', 2-6
DIRECTION (#8), 4-6
DNS AWARE (#8.22), 2-11, 4-7
DNS IP (#51), 2-11
DROP OUT OF RESTRICTED GROUP (#22), 5-21
FORWARDING ADDRESS (#2), 4-3
FROM DOMAIN (#.01), 4-5
IN-BASKET-PURGE DAYS, 5-31
INCOMING MESSAGE ID (#9), 2-9
LARGE MESSAGE REPORT LINES (#8.14), 2-16, 5-32
LAST READ DATE/TIME (#2), 7-5
LINES RECEIVED (#107), 4-6
LINES SENT (#106), 4-6
LOG RESPONSE TIME, 2-23, 5-35
MESSAGE IN TRANSIT (#2), 4-5
MESSAGE RETENTION DAYS, 2-16
MESSAGES RECEIVED (#103), 4-6
NAME (#.01)
MAIL GROUP File (#3.8), 4-3
MESSAGE STATISTICS File (#4.2999), 4-5
NETWORK - MAX LINES RECEIVE (#8.31), 2-13
NETWORK PRIORITY TRANSMISSION (#6), 4-3
NO-PURGE DAYS BUFFER (#4.301), 5-14
NO-PURGE DAYS BUFFER (LOCAL) (#142), 5-14
OUT OF SERVICE, 5-50
RECIPIENT Multiple, 7-5
RETENTION DAYS (#5), 2-10
SPECIAL QUEUING, 5-49
STATUS (#5), 7-5
TCP/IP COMMUNICATIONS PROTOCOL (#8.23), 2-11, 4-7
TCP/IP TRANSMISSION SCRIPT (#8.24), 2-11, 4-7
TO DOMAIN (#1), 4-5
WEEKDAY DAYS TO PURGE (#4.304), 5-14
XMIT AUDIT IP ADDRESSES (#60,3), 4-6
XMIT IP ADDRESSES TRIED (#48), 4-6
Figures and Tables, vii
FileMan File Security, 11-5
Files, 4-1
BULLETIN (#3.6), 2-10, 2-14, 4-2, 5-24, 9-1
Security, 11-5
COMMUNICATIONS PROTOCOL (#3.4), 2-11, 4-2, 4-7, 9-1
Security, 11-5
Descriptions, 4-2
DISTRIBUTION LIST (#3.816), 4-3, 9-1
Security, 11-6
DOMAIN (#4.2), 2-7, 2-11, 3-6, 4-4, 5-46, 5-47, 5-50, 9-1, 10-1, 11-4
Glossary, 2
Security, 11-6
IMAGE (#2005), 4-8, 8-1
INTERNET SUFFIX (#4.2996), 4-5, 9-1
Security, 11-6
INTER-UCI TRANSFER (#4.281), 4-4, 9-1
Security, 11-6
KERNEL SYSTEM PARAMETERS (#8989.3), 2-11
MAIL GROUP (#3.8), 2-14, 2-22, 4-3, 5-19, 5-24, 9-1
Security, 11-6
MAILBOX (#3.7), 2-2, 2-5, 2-14, 2-15, 2-16, 2-18, 2-19, 3-6, 4-3, 5-14, 5-16, 5-24, 5-33, 5-36, 5-53, 5-55, 9-1
MUMPS Cross-reference, 5-14
Security, 11-5
MAILMAN OUTSTANDING FTP TRANSACTIONS (#4.2995), 4-5, 9-1, 11-6
MAILMAN SITE PARAMETERS (#4.3), 2-8, 2-11, 2-13, 2-16, 2-24, 4-6, 5-14, 5-21, 5-23, 5-31, 5-32, 9-1, 11-3, 11-6
Security, 11-6
MAILMAN TIME ZONE (#4.4), 4-7, 9-1
Security, 11-6
MESSAGE (#3.9), 4-4
MESSAGE (#3.9), 2-4, 2-5, 2-6, 2-9, 2-14, 2-16, 2-23, 3-3, 3-6, 4-3
MESSAGE (#3.9), 5-12
MESSAGE (#3.9), 5-14
MESSAGE (#3.9), 5-14
MESSAGE (#3.9), 5-14
MESSAGE (#3.9), 5-16
MESSAGE (#3.9), 5-24
MESSAGE (#3.9), 5-34
MESSAGE (#3.9), 5-34
MESSAGE (#3.9), 5-53
MESSAGE (#3.9), 5-55
MESSAGE (#3.9), 6-1
MESSAGE (#3.9), 7-2
MESSAGE (#3.9), 7-3
MESSAGE (#3.9), 7-5
MESSAGE (#3.9), 7-5
MESSAGE (#3.9), 7-6
MESSAGE (#3.9), 9-1
MESSAGE (#3.9), 11-2
MESSAGE (#3.9), 11-4
MESSAGE (#3.9), 11-4
MESSAGE (#3.9), 11-6
MESSAGE DELIVERY STATS (#4.2998), 4-5, 5-25, 5-27, 5-34, 9-1
Security, 11-6
MESSAGE STATISTICS (#4.2999), 4-5, 9-1
Security, 11-6
MESSAGES TO BE NEW AT A LATER DATE (#3.73), 4-3, 5-34, 9-1
Security, 11-6
NETWORK LOCATION (#2005.2), 4-8, 8-1
NETWORK SENDERS REJECTED (#4.501), 4-7, 9-1
Security, 11-6
NETWORK TRANSACTION (#4.5), 4-7
Security, 9-1, 11-6
NEW PERSON (#200), 2-5, 2-10, 2-13, 2-19, 2-20, 5-36, 7-11
Numbers, 9-1
OPTION (#19), 2-3
REMOTE USER DIRECTORY (#4.2997), 2-25, 4-5, 5-22, 5-28, 9-1
Security, 11-6
Security, 11-5
SPOOL DATA (#3.519), 4-2, 9-1
Security, 11-5
SPOOL DOCUMENT (#3.51), 4-2, 9-1
Security, 11-5
TRANSMISSION SCRIPT (#4.6), 2-11, 2-24, 4-7, 4-8, 5-23, 9-1, 10-1
Security, 11-6
Find Messages for User Option, 2-18, 5-56, 5-57
FLTRBSKT^XMXAPIB, 7-7
FLTRMBOX^XMXAPIB, 7-7
FLTRMSG^XMXAPI, 7-6
Forwarding Address Edit Option, 5-19
FORWARDING ADDRESS Field (#2), 4-3
FROM DOMAIN Field (#.01), 4-5
FTP, xiii
FWDMSG^XMXAPI, 7-6
G
General Instructions for Obtaining IAs on FORUM, 8-1
General MailMan Information Option, 5-22
GET (Retrieve) File from Remote System Option, 5-12, 5-13
GET^XMA2 API, 7-2
GET^XML, 7-5
GETRESTR^XMXSEC1, 7-10
Global load Option, 5-43
Globals, 4-1
%ZISL, 4-5
%ZTSK, 5-48, 5-49
Locations, 9-1
Glossary, 1
ISS Home Page Web Address, Glossary, 2
GML
Enroll in (or Disenroll from) a Mail Group Option, 5-20
GO^XMCTLK API, 7-4
Graphics Download (TAB separators) Option, 2-23, 5-26
Group eMail Directory Request Option, 2-25, 2-26, 5-27, 5-28
Group Information Option, 5-22
Group/Distribution Management Menu, 2-20, 5-18, 5-19, 5-20, 5-30, 5-32
Groups
Coordinator, 5-21
Organizer, 5-21
H
HDR^XMA0, 7-2
HEADER^XM, 7-1
Help
At Prompts, xi
Online, xi
Question Marks, xi
Help (User/Group Info., etc.) Menu, xi, 5-13, 5-21, 5-22, 5-23
Help Frames, 9-14, 1
Historical Queue Data/Stats Report Option, 5-47
History, Revisions to Documentation and Patches, iii
Home Pages
\$\$FMTE^XLFDT Web Address, 2-12
Adobe Acrobat Quick Guide Web Address, xii
Adobe Web Address, xii
HSD&D Home Page Web Address, xii
ISS
Acronyms Home Page Web Address, Glossary, 2
Glossary Home Page Web Address, Glossary, 2
MAIL^XLFNSLK Web Address, 8-1
MailMan Home Page Web Address, xii
VHA Documentation Library (VDL) Home Page Web Address, xii
Host File Server, 2-26, 5-29
How to
Obtain
Technical Information Online, x
Use this Manual, ix
HSD&D
Home Page Web Address, xii
I
IMAGE File (#2005), 4-8, 8-1
Imaging
Software, 5-10, 5-15
Implementation, 2-1
Improved Name Field Display, 2-13
IN Basket Purge Option, 2-4, 2-16, 5-31
IN-BASKET-PURGE DAYS Field, 5-31
INCOMING MESSAGE ID Field (#9), 2-9
INFO^XMXEDIT, 7-8
INIT^XMVVITAE, 7-5
INMSG^XMXUTIL2, 7-12
INMSG1^XMXUTIL2, 7-12
INMSG2^XMXUTIL2, 7-12
Inquire Option, 8-2
INRESP^XMXUTIL2, 7-13
INRESPS^XMXUTIL2, 7-13
INST^XMA21, 7-3
Install Package & Run Inits Option, 5-43
Integration Agreements (IAs), 8-1
General Instructions for Obtaining IAs from FORUM, 8-1
Supported References, 8-1
Integration Agreements Menu Option, 8-1, 8-2
Interfacing, 11-2
Internal Relations, 9-1
Pointer Relationships, 9-2
Map, 9-2
Templates, 9-6
INTERNET SUFFIX File (#4.2996), 4-5, 9-1
Security, 11-6
INTER-UCI TRANSFER File (#4.281), 4-4, 9-1
Security, 11-6
Introduction to MailMan Technical Manual, 1-1
ISS
Acronyms
Home Page Web Address, Glossary, 2
Glossary
Home Page Web Address, Glossary, 2
J
JOIN^XMXAPIG, 7-8
K
KERNEL SYSTEM PARAMETERS File (#8989.3), 2-11
Kill Transmission Job, 2-7
KILL^XM API, 7-1
KL^XMA1B, 7-2
KLQ^XMA1B, 7-2
KVAPOR^XMXUTIL, 7-10
L
LARGE MESSAGE REPORT LINES Field (#8.14), 2-16, 5-32
Large Message Report Option, 2-4, 2-16, 5-32
LAST READ DATE/TIME Field (#2), 7-5
LASTACC^XMXUTIL, 7-11
LATERMSG^XMXAPI, 7-6
Line Restriction Override, 2-13
LINES RECEIVED Field (#107), 4-6
LINES SENT Field (#106), 4-6
List a transcript Option, 5-23
List eMail Directory Request by Groups Option, 2-26, 5-28
List File Attributes Option, xi
List Messages Found Option, 2-18, 5-56, 5-57
LISTBSKT^XMXAPIB, 7-7
LISTMSGS^XMXAPIB, 7-7
Load PackMan Message Option, 5-42
Load Remote VACO (Wang/Noava) Directory Option, 2-26, 5-29
Local Delivery Management Menu, 2-22, 5-25, 5-26, 5-27, 5-33, 5-34, 5-35
LOG RESPONSE TIME Field, 2-23, 5-35
Log Response Time Toggler Option, 2-23, 5-35
M
Mail Baskets, Postmaster, 2-7
Mail Delivery Statistics Report Option, 2-23, 5-26
Mail Group Coordinator's Edit Option, 2-22, 5-32
Mail Group Coordinator's Edit W/Remotes Option, 2-22, 5-32
Mail Group Edit Option, 2-22, 5-19
MAIL GROUP File (#3.8), 2-14, 2-22, 4-3, 5-19, 5-24, 9-1
Security, 11-6
Mail Groups, 11-1
Coordinator, 5-21, 5-32
Organizer, 5-21
XM SUPER SEARCH, 5-12, 11-1
MAIL^XLFNSLK, 2-11
Mailbox Contents List Option, 5-15
MAILBOX File (#3.7), 2-2, 2-5, 2-14, 2-15, 2-16, 2-18, 2-19, 3-6, 4-3, 5-14, 5-16, 5-24, 5-33, 5-36, 5-53, 5-55, 9-1
MUMPS Cross-reference, 5-14
Security, 11-5
MailLink Directory, 2-25, 2-26, 5-27, 5-28, 5-29
MailMan
DNS-Aware, 2-11
Home Page Web Address, xii
Master Menu, 5-24, 5-39, 5-55
Namespace, 9-1
Security, 11-1
MailMan Master Menu, 5-1
MailMan Menu, 2-26, 5-12, 5-13, 5-21, 5-41, 5-49, 5-51, 5-52, 5-55
MAILMAN OUTSTANDING FTP TRANSACTIONS File (#4.2995), 4-5, 9-1, 11-6
MAILMAN SITE PARAMETERS File (#4.3), 2-8, 2-11, 2-13, 2-16, 2-24, 4-6, 5-14, 5-21, 5-23, 5-31, 5-32, 9-1, 11-3, 11-6
Security, 11-6
MailMan Site Parameters Option, 2-24, 5-23
MAILMAN TIME ZONE File (#4.4), 4-7, 9-1
Security, 11-6
Maintenance, 2-1, 2-3
Ask users with many messages to do maintenance Option, 5-29
Disk Space Management, 2-3
Task Requirements Timetable
Mandatory, 2-6
Suggested, 2-6
MAKENEW^XMXUTIL, 7-11
Manage MailMan
Options, 2-14
Manage Mailman Menu, 2-1, 2-3, 2-14, 5-12, 5-23, 5-24, 5-28, 5-30, 5-31, 5-33, 5-39, 5-55, 6-1
Management Features, 2-11
Managing MailMan, 2-11
Manual for MailMan Users Option, 5-22
Map Pointer Relations Option, 5-1, 9-2
Mapping Routines, 2-1
Maps
Pointer Relationships, 9-2
Memory Constraints
Implementation, 2-2
Menu Structure, 2-1
Menus
Background Filer (XMAD), 5-25
Communications, 5-42
Custodial Package Menu, 8-1
Data Dictionary Utilities, xi, 9-2
DBA, 8-1, 8-2
DBA IA CUSTODIAL MENU, 8-1
DBA IA ISC, 8-1, 8-2
DBA IA SUBSCRIBER MENU, 8-2
DBA Option, 8-1, 8-2
DI DDU, 9-2
Diagnostics, 5-16, 5-17, 5-43
Diagram, 5-1
Disk Space Management, 2-3, 2-15, 5-16, 5-29, 5-30, 5-31, 5-32, 5-34, 5-36, 5-37, 5-38, 5-45, 5-46, 5-53, 5-57, 6-1
Group/Distribution Management, 2-20, 5-18, 5-19, 5-20, 5-30, 5-32
Help (User/Group Info., etc.), xi, 5-13, 5-21, 5-22, 5-23
Integration Agreements Menu, 8-1, 8-2
Local Delivery Management, 2-22, 5-25, 5-26, 5-27, 5-33, 5-34, 5-35
MailMan Master Menu, 5-1, 5-24, 5-39, 5-55
MailMan Menu, 2-26, 5-12, 5-13, 5-21, 5-41, 5-49, 5-51, 5-52, 5-55
Manage Mailman, 2-1, 2-3, 2-14, 5-12, 5-23, 5-24, 5-28, 5-30, 5-31, 5-33, 5-39, 5-55, 6-1
Network Management, 2-24, 2-25, 5-15, 5-39, 5-40, 5-41, 5-47, 5-52
Other MailMan Functions, 5-15, 5-23, 5-41, 5-42
Package received, 5-44
Personal Preferences, 5-11, 5-12, 5-15, 5-19, 5-20
Programmer Options, 5-1
Queue Management, 5-23, 5-39, 5-46, 5-47, 5-53
Recover Messages into User's IN Basket, 2-17, 5-56, 5-57
Remote MailLink Directory Menu, 2-25, 5-18, 5-27, 5-28, 5-29
Security, 11-2
Send Package transfer (PackMan), 5-45
Subscriber Package Menu, 8-2
Taskman Management Menu, 5-49
Transmission Management, 5-17, 5-40, 5-48, 5-49, 5-50, 5-51, 5-54
User Options Edit, 5-20
XM PERSONAL MENU, 5-11, 5-12, 5-15, 5-19, 5-20
XM SUPER SEARCH, 11-1, 11-2
XMDX, 5-16, 5-17, 5-43
XMHELP, xi, 5-13, 5-21, 5-22, 5-23
XMMASTER, 5-1, 5-10, 5-24, 5-39, 5-55
XMMGR, 2-1, 2-3, 2-14, 5-12, 5-23, 5-24, 5-28, 5-30, 5-31, 5-33, 5-39, 5-55
XMMGR-BACKGROUND-FILER, 5-25
XMMGR-DIRECTORY-MAIN, 2-25, 5-18, 5-27, 5-28, 5-29
XMMGR-DISK-SPACE-MANAGEMENT, 2-3, 2-15, 5-16, 5-29, 5-30, 5-31, 5-32, 5-34, 5-36, 5-37, 5-38, 5-45, 5-46, 5-53, 5-57
XMMGR-GROUP-MAINTENANCE, 2-20, 5-18, 5-19, 5-20, 5-30, 5-32
XMMGR-MESSAGE-DELIVERY-MGT, 2-22, 5-25, 5-26, 5-27, 5-33, 5-34, 5-35
XMNET, 2-1, 2-24, 2-25, 5-15, 5-39, 5-40, 5-41, 5-47, 5-52
XMNET-QUEUE-MANAGEMENT, 5-23, 5-39, 5-46, 5-47, 5-53
XMNET-TRANSMISSION-MANAGEMENT, 5-17, 5-40, 5-48, 5-49, 5-50, 5-51, 5-54
XMOTHER, 5-15, 5-23, 5-41, 5-42
XMOTHER-COMMUNICATIONS, 5-10, 5-42
XMPRECV, 5-44
XMPSEND, 5-45
XMUSER, 2-2, 2-26, 5-12, 5-13, 5-21, 5-41, 5-49, 5-51, 5-52, 5-55
XMUT-REC-MENU, 2-17, 5-56, 5-57
XUPROG, 5-1
MESSAGE DELIVERY STATS File (#4.2998), 2-23, 4-5, 5-25, 5-27, 5-34, 9-1
Security, 11-6
MESSAGE File (#3.9), 2-4, 2-5, 2-6, 2-9, 2-14, 2-16, 3-3, 3-6, 4-3, 4-4, 5-12, 5-14, 5-16, 5-24, 5-34, 5-53, 5-55, 6-1, 7-2, 7-3, 7-5, 7-6, 9-1, 11-2, 11-4, 11-6
Message Filter Edit Option, 5-11
MESSAGE IN TRANSIT Field (#2), 4-5
Message Line Restriction Override, 2-13
MESSAGE RETENTION DAYS Field, 2-16
MESSAGE STATISTICS File (#4.2999), 4-5, 9-1
Security, 11-6
Message statistics Option, 2-4, 2-16, 5-53
MESSAGES RECEIVED Field (#103), 4-6
MESSAGES TO BE NEW AT A LATER DATE File (#3.73), 4-3, 5-34, 9-1
Security, 11-6
Messages with Responses
Broadcasting, 2-13
Modem Autodialer test Option, 5-16
Modems, 1
MOVEMSG^XMXAPI, 7-6
Multimedia, 1-1
MailMan, 4-8, 5-10, 8-1, 3
N
N1^XM API, 7-1
NAME Field (#.01)
MESSAGE STATISTICS File (#4.2999), 4-5
Name Field Display Improved, 2-13
NAME Field(#.01)
MAIL GROUP File (#3.8), 4-3
Name Server Option, 5-17
NAMEBSKT^XMXAPIB, 7-7
Namespace, 9-1
Network, 1-1, 1-2
NETWORK - MAX LINES RECEIVE Field (#8.31), 2-13
Network Help Option, 5-41
NETWORK LOCATION File (#2005.2), 4-8, 8-1
Network Management, 2-1
Network Management Menu, 2-24, 2-25, 5-15, 5-39, 5-40, 5-41, 5-47, 5-52
NETWORK PRIORITY TRANSMISSION Field (#6), 4-3
NETWORK SENDERS REJECTED File (#4.501), 4-7, 9-1
Security, 11-6
NETWORK TRANSACTION File (#4.5), 4-7
Security, 9-1, 11-6
Network Transmission Failures, Postmaster, 2-7
New Features for Managing MailMan Option, 2-25, 5-31
New Features in MailMan Option, 5-13
New Messages and Logon Statistics Option, 2-24, 5-33
New Messages and Responses Option, 5-41
NEW PERSON File (#200), 2-5, 2-10, 2-13, 2-19, 2-20, 5-36, 7-11
NEW^XM API, 7-1
NML
New Messages and Responses Option, 5-41
NONEW^XMXUTIL, 7-11
NO-PURGE DAYS BUFFER (LOCAL) Field (#142), 5-14
NO-PURGE DAYS BUFFER Field (#4.301), 5-14
Normalized Reports, 2-23, 5-25
O
Official Policies, 11-6
Online
Documentation, xi
Technical Information, How to Obtain, x
Operations
Implementation, 2-2
OPTEDIT^XMXSEC2, 7-10
OPTGRP^XMXSEC1, 7-10
OPTION File (#19), 2-3
Options
ACTIVE by Custodial Package, 8-1
Active Users/Deliveries Report, 2-22, 5-25
Actively Transmitting/Receiving Queues Report, 5-46
AI x-Ref Purge of Received Network Messages, 2-3, 2-15, 5-34
Ask users with many messages to do maintenance, 2-3, 2-15, 5-29
Assume the Identity of SHARED,MAIL, 5-52
Automatic Purge of MailMan Messages, 2-4, 5-14
Background Filer (XMAD) Menu, 5-25
Banner Edit, 5-15
Become a Surrogate (SHARED,MAIL or Other), 5-13
Bulletin edit, 2-21, 5-18
Change/Delete Later'd Messages, 5-23
CHECK background filer, 2-22, 5-26
Check MailMan Files for Errors, 2-5, 2-14, 5-55
Christen a domain, 2-24, 5-15, 5-23
Clean out waste baskets, 2-4, 2-16, 5-16
Communications Menu, 5-42
Compare Domains in System Against Released List, 5-47
Compare message, 5-43
Compile Response Time Statistics, 2-23, 5-34
Create a Mailbox for a user, 2-15, 5-33
Custodial Package Menu, 8-1
Data Dictionary Utilities, xi, 9-2
DBA, 8-1, 8-2
DBA IA CUSTODIAL, 8-1
DBA IA CUSTODIAL MENU, 8-1
DBA IA INQUIRY, 8-2
DBA IA ISC, 8-1, 8-2
DBA IA SUBSCRIBER MENU, 8-2
DBA IA SUBSCRIBER Option, 8-2
DBA Option, 8-1, 8-2
Delete Found Messages from Found Messages List, 2-18, 5-56
Deliver Found Messages into User's IN Basket, 2-18, 5-56
Deliveries by Group, 2-23, 5-25
Delivery Basket Edit, 5-11
Delivery Queue Statistics Collection, 2-23, 5-27
Delivery Queues Wait Report, 5-26
DI DDMAP, 5-1, 9-2
DI DDU, 9-2
Diagnostics Menu, 5-16, 5-17, 5-43
Disk Space Management, 2-3, 2-15, 5-16, 5-29, 5-30, 5-31, 5-32, 5-34, 5-36, 5-37, 5-38, 5-45, 5-46, 5-53, 5-57, 6-1
Display Active & Inactive Message Queues, 5-46
Edit a script, 5-50
Edit Distribution List, 2-21, 5-18
Edit numbers to Normalize Reports, 2-23, 5-25
Enroll in (or Disenroll from) a Mail Group, 2-21, 5-20
Enter/Edit Directory Request Flags by Group, 2-25, 5-27
Enter/Edit Remote User, 2-25, 5-18
Exported, 5-1
Find Messages for User, 2-18, 5-56, 5-57
Forwarding Address Edit, 5-19
General MailMan Information, 5-22
GET (Retrieve) File from Remote System, 5-12, 5-13
Global load, 5-43
Graphics Download (TAB separators), 2-23, 5-26
Group eMail Directory Request, 2-25, 2-26, 5-27, 5-28
Group Information, 5-22
Group/Distribution Management, 2-20, 5-18, 5-19, 5-20, 5-30, 5-32
Help (User/Group Info., etc.), xi, 5-13, 5-21, 5-22, 5-23
Historical Queue Data/Stats Report, 5-47
IN Basket Purge, 2-4, 2-16, 5-31
Inquire, 8-2
Install Package & Run Inits, 5-43
Integration Agreements Menu, 8-1, 8-2
Large Message Report, 2-4, 2-16, 5-32
List a transcript, 5-23
List eMail Directory Request by Groups, 2-26, 5-28
List File Attributes, xi
List Messages Found, 2-18, 5-56, 5-57
Load PackMan Message, 5-42
Load Remote VACO (Wang/Noava) Directory, 2-26, 5-29
Local Delivery Management, 2-22, 5-25, 5-26, 5-27, 5-33, 5-34, 5-35
Log Response Time Toggler, 2-23, 5-35
Mail Delivery Statistics Report, 2-23, 5-26
Mail Group Coordinator's Edit, 2-22, 5-32
Mail Group Coordinator's Edit W/Remotes, 2-22, 5-32
Mail Group Edit, 2-22, 5-19
Mailbox Contents List, 5-15
MailMan Master Menu, 5-1, 5-24, 5-39, 5-55
MailMan Menu, 2-26, 5-12, 5-13, 5-21, 5-41, 5-49, 5-51, 5-52, 5-55
MailMan Site Parameters, 2-24, 5-23
Manage Mailman, 2-1, 2-3, 2-14, 5-12, 5-23, 5-24, 5-30, 5-31, 5-33, 5-39, 5-55, 6-1
Manage MailMan, 2-14
Manage Mailman Menu, 5-28
Manual for MailMan Users, 5-22
Map Pointer Relations, 5-1, 9-2
Message Filter Edit, 5-11
Message statistics, 2-4, 2-16, 5-53
Modem Autodialer test, 5-16
Name Server, 5-17
Network Help, 5-41
Network Management, 2-25, 5-15, 5-39, 5-40, 5-41, 5-47, 5-52
Network Management Menu, 2-24, 5-39
New Features for Managing MailMan, 2-25, 5-31
New Features in MailMan, 5-13
New Messages and Logon Statistics, 2-24, 5-33
New Messages and Responses, 5-41
Options Listed Alphabetically by Name, 5-11
Other MailMan Functions, 5-15, 5-23, 5-41, 5-42
Package received Menu, 5-44
Personal Mail Group Edit, 5-19
Personal Preferences, 5-11, 5-12, 5-15, 5-19, 5-20
Physical link protocol, 5-17
Play a script, 5-51
POLL REMOTE NODES, 5-43
Post a bulletin, 5-43
Print ACTIVE by Subscribing Package, 8-2
Print message (formatted), 5-44
Programmer, 5-1
Purge a message, 2-4, 2-17, 5-34
Purge Messages by Origination Date, 2-4, 2-17, 5-46
Purge Unreferenced Messages, 2-4, 2-17, 5-45
Query/Search for Messages, 5-51
Questions and Answers on MailMan, 5-22
Queue Management, 5-23, 5-39, 5-46, 5-47, 5-53
Queues with Messages to Transmit Report, 5-47
Read/Manage Messages, 5-49, 7-1
RECEIVE E-MAIL DIRECTORY FROM OTHER SITE Option, 5-28
Receive Messages from Another UCI, 5-48, 5-49
Recover Messages into User's IN Basket, 2-17, 5-56, 5-57
Remote Directory from all Domains, 2-26, 5-27
Remote MailLink Directory Menu, 2-25, 5-18, 5-27, 5-28, 5-29
Remote User Information, 5-22
Report on Later'd Messages, 5-23
Request Mail Directory From a Single Domain Server, 2-26, 5-29
Resume processing a script, 5-51
Routine load, 5-44
Schedule/Unschedule Options, 5-49
Script processor, 5-17
Security, 11-2
Send (Put) File to Remote Location, 5-12, 5-13
Send a Directory to requesting site, 5-29
Send a Message, 5-52
Send a TWIX via PCTS, 5-40
Send Messages to Another UCI, 5-48, 5-49
Send Multimedia Message, 5-15
Send Package transfer (PackMan), 5-45
Sequential Media Message Reception, 5-48, 5-50
Sequential Media Queue Transmission, 5-48, 5-50
Show a queue, 5-47
Simple Mail Transfer Protocol, 5-17
Site Parameters, 5-52
START background filer, 2-24, 5-35
Start XMRONT TCP Listener, 5-49
STOP background filer, 2-24, 5-35
Subroutine editor, 5-54
Subscriber Package Menu, 8-2
Suggestion Box, 5-54
Summarize message, 5-45
Super Search Message File, 5-12, 11-4
Surrogate Edit, 5-19
TalkMan, 5-54
Taskman Management Menu, 5-49
Terminate mail user suggestions, 2-4, 2-18, 5-38
Terminate many mail users, 2-5, 2-19, 5-36
Terminate one mail user, 2-5, 2-20, 5-37
Toggle a script out of service, 5-50
Transmission Management, 5-17, 5-48, 5-49, 5-50, 5-51, 5-54
Transmission Management Menu, 5-40
Transmit a Single Queue, 5-53
Transmit All Queues, 5-53
Transmit TWIX's, 5-40
User Information, 5-23
User Options Edit, 5-20
Validation Number Edit, 5-17
*Without* Parents, 5-10
XM DELIVERY BASKET EDIT, 5-11
XM FILTER EDIT, 5-11
XM PERSONAL MENU, 5-11, 5-12, 5-15, 5-19, 5-20
XM SUPER SEARCH, 5-12, 11-1, 11-2, 11-4
XMASSUME, 5-13
XMAUTOPURGE, 2-4, 2-5, 2-6, 2-16, 2-17, 3-1, 5-10, 5-14, 5-16, 5-45, 5-53
XMBANNER, 5-15
XMBASKLIST, 5-15
XMBLOBSEND, 5-10, 5-15
XMCHRIS, 5-15, 5-23
XMCLEAN, 2-4, 2-5, 2-6, 2-16, 3-1, 5-16
XMDX, 5-10, 5-16, 5-17, 5-43
XMDXMODEM, 5-16
XMDXNAME, 5-17
XMDXPROT, 5-17
XMDXSCRIPT, 5-17
XMDXSMTP, 5-17
XMEDITBUL, 2-21, 5-18
XMEDITDIST, 5-18
XMEDITDIST, 2-21
XMEDIT-DOMAIN-VALIDATION#, 5-17
XMEDITFWD, 5-19
XMEDITMG, 2-22, 5-19
XMEDITPERSGROUP, 5-19
XMEDIT-REMOTE-USER, 2-25, 5-18
XMEDITSURR, 5-19
XMEDITUSER, 5-20
XMENROLL, 2-21, 5-20
XM-FTP-GET, 5-12, 5-13
XM-FTP-PUT, 5-12, 5-13
XMHELP, xi, 5-13, 5-21, 5-22, 5-23
XMHELPALL, 5-22
XMHELPGROUP, 5-22
XMHELPLNK, 5-22
XMHELP-ON-LINE-USER_MANUAL, 5-22
XMHELPQUEST, 5-22
XMHELPUSER, 5-23
XMKSP, 2-24, 5-23
XMLATER-EDIT, 5-23
XMLATER-REPORT, 5-23
XMLIST, 5-23
XMMASTER, 5-1, 5-10, 5-24, 5-39, 5-55
XMMGR, 2-1, 2-3, 2-14, 5-12, 5-23, 5-24, 5-28, 5-30, 5-31, 5-33, 5-39, 5-55
XMMGR- BKFILER-TABBED-STATS, 2-23
XMMGR-BACKGROUND-FILER, 5-10
XMMGR-BACKGROUND-FILER, 5-25
XMMGR-BKFILER-ACT, 2-22, 5-25
XMMGR-BKFILER-EDIT-NORMALIZED, 2-23, 5-25
XMMGR-BKFILER-GROUP, 2-23, 5-25
XMMGR-BKFILER-STAT, 2-23, 5-26
XMMGR-BKFILER-TABBED-STATS Option, 5-26
XMMGR-BKFILER-WAIT, 5-10, 5-26
XMMGR-CHECK-BACKGROUND-FILER, 2-22, 5-26
XMMGR-DELIVERY-STATS-COLL, 2-23, 5-27
XMMGR-DIRECTORY-ALL, 2-26, 5-27
XMMGR-DIRECTORY-EDITGRP, 2-25, 2-26, 5-27, 5-28
XMMGR-DIRECTORY-GROUP, 2-25, 5-27
XMMGR-DIRECTORY-LISTGRP, 2-26, 5-28
XMMGR-DIRECTORY-MAIN, 2-25, 5-18, 5-27, 5-28, 5-29
XMMGR-DIRECTORY-RECV, 5-10, 5-28
XMMGR-DIRECTORY-SEND, 5-10, 5-29
XMMGR-DIRECTORY-SINGLE, 2-26, 5-29
XMMGR-DIRECTORY-VACO, 2-26, 5-29
XMMGR-DISK-MANY-MESSAGE-MAINT, 2-3, 2-6, 2-10, 2-15, 5-29
XMMGR-DISK-SPACE-MANAGEMENT, 2-3, 2-15, 5-16, 5-29, 5-30, 5-31, 5-32, 5-34, 5-36, 5-37, 5-38, 5-45, 5-46, 5-53, 5-57
XMMGR-GROUP-MAINTENANCE, 2-20, 5-18, 5-19, 5-20, 5-25, 5-26, 5-27, 5-30, 5-32, 5-33, 5-34, 5-35
XMMGR-HELP, 2-25, 5-31
XMMGR-IN-BASKET-PURGE, 2-4, 2-9, 2-16, 5-31
XMMGR-LARGE-MESSAGE-REPORT, 2-4, 2-6, 2-16, 5-32
XMMGR-MAIL-GRP-COORDINATOR, 2-22, 5-32
XMMGR-MAIL-GRP-COORD-W/REMOTES, 2-22, 5-32
XMMGR-MESSAGE-DELIVERY-MGT, 2-22, 5-33
XMMGR-NEW-MAIL-BOX, 2-15, 5-33
XMMGR-NEWMESS/LOGON-STATS, 2-24, 5-33
XMMGR-PURGE-AI-XREF, 2-3, 2-6, 2-15, 5-34
XMMGR-PURGE-MESSAGE, 2-4, 2-17, 5-10, 5-34
XMMGR-RESPONSE-TIME-COMPILER, 2-6, 2-23, 5-34
XMMGR-RESPONSE-TIME-TOGGLER, 2-7, 2-23, 5-35
XMMGR-START-BACKGROUND-FILER, 2-24, 5-35
XMMGR-STOP-BACKGROUND-FILER, 2-24, 5-35
XMMGR-TERMINATE-MANY, 2-5, 2-19, 2-20, 5-36, 5-37
XMMGR-TERMINATE-ONE, 2-5, 2-20, 5-37
XMMGR-TERMINATE-SUGGEST, 2-4, 2-18, 2-20, 5-37, 5-38
XMNET, 2-1, 2-24, 2-25, 5-15, 5-39, 5-40, 5-41, 5-47, 5-52
XMNETHELP, 5-41
XMNET-QUEUE-MANAGEMENT, 5-23, 5-39, 5-46, 5-47, 5-53
XMNET-TRANSMISSION-MANAGEMENT, 5-17, 5-40, 5-48, 5-49, 5-50, 5-51, 5-54
XMNET-TWIX-SEND, 5-10, 5-40
XMNET-TWIX-TRANSMIT, 5-10, 5-40
XMNEW, 5-41
XM-NEW-FEATURES, 5-13
XMOTHER, 5-15, 5-23, 5-41, 5-42
XMOTHER-COMMUNICATIONS, 5-10, 5-42
XMPACK, 5-42
XMPCOM, 5-43
XMPGLO, 5-43
XMPINS, 5-43
XMPOLL, 5-10, 5-43
XMPOST, 5-43
XMPPRT, 5-44
XMPRECV, 5-10, 5-44
XMPROU, 5-44
XMPSEND, 5-10, 5-45
XMPSUM, 5-45
XMPURGE, 2-4, 2-17, 5-45, 5-53
XMPURGE-BY-DATE, 2-4, 2-6, 2-8, 2-17, 5-46, 5-53
XMQACTIVE, 5-46
XMQDISP, 5-46
XMQDOMAINS, 5-47
XMQHIST, 5-47
XMQSHOW, 5-47
XMQUEUED, 5-47
XMR-BROADCAST-VA-WIDE, 5-10, 5-48, 5-57
XMREAD, 5-49, 7-1
XMRONT, 5-10, 5-49
XMR-SEQ-RECEIVE, 5-48, 5-50
XMR-UCI-RCV, 5-48, 5-49
XMR-UCI-SEND, 5-48, 5-49
XMSCRIPTEDIT, 5-50
XMSCRIPTOUT, 5-50
XMSCRIPTPLAY, 5-51
XMSCRIPTRES, 5-10, 5-51
XMSEARCH, 5-51
XMSEND, 5-52
XMSHARE, 5-10, 5-52
XMSITE, 5-52
XMS-SEQ-TRANSMIT, 5-48, 5-50
XMSTARTQUE, 5-47, 5-53
XMSTARTQUE-ALL, 5-47, 5-53
XMSTAT, 2-4, 2-16, 5-45, 5-53
XMSUBEDIT, 5-54
XMSUGGESTION, 5-10, 5-54
XMTALK, 5-10, 5-54
XMUSER, 2-2, 2-26, 5-12, 5-13, 5-21, 5-41, 5-49, 5-51, 5-52, 5-55
XMUT-CHKFIL, 2-5, 2-6, 2-14, 5-14, 5-55
XMUT-REC‑DELETE, 2-18, 5-56
XMUT-REC‑DELIVER, 2-18, 5-56
XMUT-REC-FIND, 2-18, 5-56, 5-57
XMUT-REC-MENU, 2-17, 5-56, 5-57
XMUT-REC-RPT, 2-18, 5-56, 5-57
XMYB-BROADCAST-VA-WIDE, 5-10, 5-48, 5-57
XUPROG, 5-1
OPTMSG^XMXSEC2, 7-10
Organizer For a Mail Group, 5-21
Orientation, ix
Other MailMan Functions Menu, 5-15, 5-23, 5-41, 5-42
OTHER^XMVVITAE, 7-5
OUT OF SERVICE Field, 5-50
P
Package received Option, 5-44
PackMan, 1-2, 5-10, 5-11, 5-42, 5-44, 5-45
PAGE^XMXUTIL, 7-11
Patches
History, iv
PCTS, 5-40
Personal Mail Group Edit Option, 5-19
Personal Preferences Menu, 5-11, 5-12, 5-15, 5-19, 5-20
Physical link protocol Option, 5-17
Play a script Option, 5-51
Pointer Relationships, 9-2
Map, 9-2
Policies, Official, 11-6
POLL REMOTE NODES Option, 5-43
Pollers, 5-39, 5-53
Post a bulletin Option, 5-43
Postmaster, 2-2, 2-6, 2-21, 4-3, 7-2, 7-5, 7-9, 7-10
Broadcast Messages, 2-7
Domain Baskets, 2-7
Implementation, 2-2
Kill Transmission Job, 2-7
Mail Baskets, 2-7
Maintenance, 2-7
Network Transmission Failures, 2-7
Stop Network Messages, 2-7
PR2^XMA0, 7-2
Print ACTIVE by Subscribing Package Option, 8-2
Print message (formatted) Option, 5-44
PRINT Templates, 9-7
XMHOSTLIST, 9-7
XMMGR-BKFILER-ACTIVE_USERS/DEL, 9-8
XMMGR-BKFILER-DEL_BY_GROUP, 9-8
XMMGR-BKFILER-LENGTH_OF_QUEUES, 9-8
XMMGR-BKFILER-LONGTERM-STATS, 9-9
XMMGR-BKFILER-OLD_STATS/TABBED, 9-10
XMMGR-BKFILER-QUEUE-WAIT, 9-11
XMMGR-BKFILER-STATS/TABBED, 9-12
XMMGR-BKFILER-STATS-PLUS, 9-11
XMMGR-BKFILER-TABBED-RT, 9-13
Priority Transmission Flexibility, 2-11
PRIORITY^XMXEDIT, 7-8
Procedures
Controlled, 2-1
Product Security, 11-1
Programmer Options Menu, 5-1
PRTMSG^XMXAPI, 7-6
Purge a message Option, 2-4, 2-17, 5-34
Purge Messages by Origination Date Option, 2-4, 2-17, 5-46
Purge Unreferenced Messages Option, 2-4, 2-17, 5-45
Purging, 6-1, 11-2
PUTSERV^XMXAPI, 7-6
Q
Q^XMXUTIL3, 7-13
QBSKT^XMXAPIB, 7-7
QD^XMXUTIL3, 7-13
QL^XMXUTIL3, 7-13
QMBOX^XMXAPIB, 7-7
QN^XMXUTIL3, 7-14
Query/Search for Messages Option, 5-51
Question Mark Help, xi
Questions and Answers on MailMan Option, 5-22
Queue Management Menu, 5-23, 5-39, 5-46, 5-47, 5-53
Queues with Messages to Transmit Report Option, 5-47
QX^XMXUTIL3, 7-14
R
Read/Manage Messages Option, 5-49, 7-1
READ^XMXAPIU, 7-8
Reader, Assumptions About the, xi
READNEW^XMXAPIU, 7-8
REC^XMA, 7-1
REC^XMS3, 7-5
RECEIVE E-MAIL DIRECTORY FROM OTHER SITE Option, 5-28
Receive Messages from Another UCI Option, 5-48, 5-49
RECIPIENT Multiple Field, 7-5
Recover Messages into User's IN Basket Menu, 2-17, 5-56, 5-57
Reference Materials, xii
References, 11-6
General Instructions for Obtaining IAs from FORUM, 8-1
Supported, 8-1
Reformatted Date/Times, 2-12
Reformatted Remote Message IDs, 2-12
Remote
Message IDs, Reformatted, 2-12
Systems, 11-1
Remote Directory from all Domains Option, 2-26, 5-27
Remote MailLink Directory Menu, 2-25, 5-18, 5-27, 5-28, 5-29
REMOTE USER DIRECTORY File (#4.2997), 2-25, 4-5, 5-22, 5-28, 9-1
Security, 11-6
Remote User Information Option, 5-22
REMSBMSG^XMA1C, 7-2
REPLYMSG^XMXAPI, 7-6
Report on Later'd Messages Option, 5-23
Request Mail Directory From a Single Domain Server Option, 2-26, 5-29
Requeued Task Bug Fix, 2-13
Response Time Logging, 5-35
Resume processing a script Option, 5-51
RETENTION DAYS field (#5), 2-10
Revision History, iii
Documentation, iii
Patches, iv
RML
Read/Manage Messages Option, 5-49
Routine load Option, 5-44
Routine Mapping, 2-1
Routines, 3-1
Enhanced, 2-13
XM, 3-1
XMA, 3-1
XMA0, 3-1
XMA03, 3-1
XMA11, 3-1
XMA11A, 3-1
XMA1B, 3-1
XMA1C, 3-1
XMA2, 3-1
XMA21, 3-1
XMA21C, 3-1
XMA2B, 3-1
XMA2R, 3-1
XMA3, 3-1
XMA30, 3-1
XMA32, 3-1
XMA32A, 3-1
XMA7, 3-1
XMAD2, 3-1
XMADGO, 3-1
XMAFTP, 3-1
XMAH, 3-2
XMAH1, 3-2
XMAI2, 3-2
XMAPBLOB, 3-2
XMAPHOST, 3-2
XMASEC, 3-2
XMB, 3-2
XMBBLOB, 3-2
XMBGRP, 3-2
XMC, 3-2
XMC1, 3-2
XMC11, 3-2
XMC1A, 3-2
XMC1B, 3-2
XMCB, 3-2
XMCD, 3-2
XMCDNT, 3-2
XMCE, 3-2
XMCP, 3-2
XMCQ, 3-2
XMCQA, 3-2
XMCQH, 3-2
XMCSIZE, 3-2
XMCTLK, 3-2
XMCTRAP, 3-2
XMCU1, 3-2
XMCX, 3-2
XMCXT, 3-2
XMCXU, 3-2
XMD, 3-2
XMDIR1, 3-2
XMDIR1A, 3-2
XMDIR1B, 3-2
XMDIRQST, 3-3
XMDIRRCV, 3-3
XMDIRSND, 3-3
XMFAX, 3-3
XMGAPI0, 3-3
XMGAPI1, 3-3
XMGAPI2, 3-3
XMGAPI3, 3-3
XMGAPI4, 3-3
XMHIG, 3-3
XMHIU, 3-3
XMJBL, 3-3
XMJBM, 3-3
XMJBM1, 3-3
XMJBN, 3-3
XMJBN1, 3-3
XMJBU, 3-3
XMJBULL, 3-3
XMJDIR, 3-3
XMJERR, 3-3
XMJMA, 3-3
XMJMC, 3-3
XMJMCODE, 3-3
XMJMD, 3-3
XMJMF, 3-3
XMJMF1, 3-3
XMJMF2, 3-3
XMJMFA, 3-3
XMJMFB, 3-3
XMJMFC, 3-3
XMJML, 3-3
XMJMLN, 3-3
XMJMLR, 3-3
XMJMLR1, 3-4
XMJMOI, 3-4
XMJMOI1, 3-4
XMJMOIE, 3-4
XMJMOR, 3-4
XMJMORX, 3-4
XMJMORX1, 3-4
XMJMP, 3-4
XMJMP1, 3-4
XMJMP2, 3-4
XMJMQ, 3-4
XMJMQ1, 3-4
XMJMR, 3-4
XMJMR1, 3-4
XMJMRO, 3-4
XMJMS, 3-4
XMJMSA, 3-4
XMJMSO, 3-4
XMJMT, 3-4
XMKP, 3-4
XMKP1, 3-4
XMKPL, 3-4
XMKPLQ, 3-4
XMKPO, 3-4
XMKPR, 3-4
XMKPR1, 3-4
XMKPRD, 3-4
XML, 3-4
XML1CRC, 3-4
XML4CRC, 3-4
XML4CRC1, 3-4
XMLPC, 3-4
XMLSWP, 3-4
XMLSWP0, 3-4
XMLSWP2, 3-4
XMLTCP, 3-5
XMM1, 3-5
XMM2, 3-5
XMNTEG, 3-5
XMNTEG0, 3-5
XMP, 3-5
XMP2, 3-5
XMP2A, 3-5
XMP3, 3-5
XMPC, 3-5
XMPG, 3-5
XMPH, 3-5
XMPSEC, 3-5
XMR, 3-5
XMR0BLOB, 3-5
XMR1, 3-5
XMR2, 3-5
XMR3, 3-5
XMR3A, 3-5
XMR4, 3-5
XMRENT, 3-5
XMRFTP, 3-5
XMRFTPUX, 3-5
XMRINETD, 3-5
XMRMSM, 3-5
XMRONT, 3-5
XMRPCTS, 3-5
XMRPCTS0, 3-5
XMRPCTS1, 3-5
XMRPCTSA, 3-5
XMRPOP, 3-5
XMRTCP, 3-5
XMRTCPGO, 3-5
XMRUCX, 3-5
XMS, 3-5
XMS0BLOB, 3-6
XMS1, 3-6
XMS2, 3-6
XMS3, 3-6
XMSFTP, 3-6
XMSFTPUX, 3-6
XMTDF, 3-6
XMTDL, 3-6
XMTDL1, 3-6
XMTDL2, 3-6
XMTDO, 3-6
XMTDR, 3-6
XMTDT, 3-6
XMUCXPOP, 3-6
XMUDCHK, 3-6, 5-47
XMUDCHR, 3-6
XMUDNC, 3-6
XMUDTOP, 3-6
XMUPIN, 3-6
XMUT1, 3-6
XMUT1A, 3-6
XMUT2, 3-6
XMUT4, 3-6
XMUT41, 3-6
XMUT4A, 3-6
XMUT4C, 3-6
XMUT5, 3-6
XMUT5B, 3-6
XMUT5C, 3-6
XMUT5G, 3-6
XMUT5Q, 3-6
XMUT5Q1, 3-6
XMUT5R1, 3-6
XMUT5R2, 3-6
XMUT6, 3-6
XMUT7, 3-7
XMUTCOM1, 3-7
XMUTERM, 3-7
XMUTERM1, 3-7
XMUTERM2, 3-7
XMUTPUR0, 3-7
XMVGROUP, 3-7
XMVGRP, 3-7
XMVSURR, 3-7
XMVVITA, 3-7
XMVVITAE, 3-7
XMXADDR, 3-7
XMXADDR1, 3-7
XMXADDR2, 3-7
XMXADDR3, 3-7
XMXADDR4, 3-7
XMXADDRD, 3-7
XMXADDRG, 3-7
XMXANSER, 3-7
XMXAPI, 3-7
XMXAPIB, 3-7
XMXAPIG, 3-7
XMXAPIU, 3-7
XMXBSKT, 3-7
XMXBULL, 3-7
XMXEDIT, 3-7
XMXGRP, 3-7
XMXGRP1, 3-7
XMXLIST, 3-7
XMXLIST1, 3-7
XMXLIST2, 3-7
XMXMBOX, 3-7
XMXMSGS, 3-7
XMXMSGS1, 3-7
XMXMSGS2, 3-7
XMXPARM, 3-8
XMXPARM1, 3-8
XMXPARMB, 3-8
XMXPRT, 3-8
XMXREPLY, 3-8
XMXSEC, 3-8
XMXSEC1, 3-8
XMXSEC2, 3-8
XMXSEC3, 3-8
XMXSEND, 3-8
XMXTO, 3-8
XMXUTIL, 3-8
XMXUTIL1, 3-8
XMXUTIL2, 3-8
XMXUTIL3, 3-8
XMXUTIL4, 3-8
XMYP18, 3-8
XMYP24, 3-8
XMYPRE, 3-8
RSEQBSKT^XMXAPIB, 7-7
RTHIST, 2-1
S
S2^XMA1B, 7-2
SACC Exemptions, 10-1
Schedule/Unschedule Options Option, 5-49
Script processor Option, 5-17
Security, 11-1
Archiving, 11-2
Electronic Signatures, 11-2
Interfacing, 11-2
Keys, 11-3
Menus, 11-2
Official Policies, 11-6
Options, 11-2
Purging, 11-2
References, 11-6
Remote Systems, 11-1
Security Keys
DOMAIN File, 11-4
XM AUTO-FORWARD WAIVER, 11-3
XM CAC ADPAC, 11-3
XM GROUP EDIT MASTER, 11-3
XM GROUP PRIORITY, 11-4
XM NO BROADCASTS, 5-57, 11-4
XM SUPER SEARCH, 5-12, 11-4
XMBLOB, 5-15
XMMGR, 2-17, 2-25, 5-28, 5-46, 11-3, 11-4
XMNET, 5-19, 5-42, 11-4
XMNOPRIV, 5-52, 11-4
XMQ-, 11-4
XMSTAR, 2-7, 11-4
XMSTAR LIMITED, 2-7, 11-4
XMTALK, 5-54, 11-5
XUPROG, 2-14, 5-45, 5-55, 11-5
XUPROGMODE, 5-42, 5-46, 11-5
SELF^XMVVITAE, 7-6
Self-Enrollment, 5-21
Send (Put) File to Remote Location Option, 5-12, 5-13
Send a Directory to requesting site Option, 5-29
Send a Message Option, 5-52
Send a TWIX via PCTS Option, 5-40
Send Messages to Another UCI Option, 5-48, 5-49
Send Multimedia Message Option, 5-15
Send Package transfer (PackMan) Option, 5-45
SEND^XMXAPIU, 7-8
SENDBULL^XMXAPI, 7-6
SENDMSG^XMXAPI, 7-6
Sequential Media Message Reception Option, 5-48, 5-50
Sequential Media Queue Transmission Option, 5-48, 5-50
SETSB^XMA1C, 7-2
SHARED,MAIL, 2-6, 5-13, 5-48, 5-52, 5-54, 5-57, 7-9, 7-10, 11-4
Show a queue Option, 5-47
Simple Mail Transfer Protocol Option, 5-17
Site Parameters, 2-16, 11-6
Site Parameters Option, 5-52
SML
Send a Message Option, 5-52
Software Product Security, 11-1
Software-wide Variables, 10-1
SORT Templates, 9-6
XMMGR-BKFILER-DAY@23:30, 9-6
XMMGR-BKFILER-TIME_PER_DATE, 9-6
Special Operations
Implementation, 2-2
SPECIAL QUEUING Field, 5-49
SPOOL DATA File (#3.519), 4-2, 9-1
Security, 11-5
SPOOL DOCUMENT File (#3.51), 4-2, 9-1
Security, 11-5
START background filer Option, 2-24, 5-35
Start XMRONT TCP Listener Option, 5-49
STATUS Field (#5), 7-5
STOP background filer Option, 2-24, 5-35
SUBJ^XMXEDIT, 7-8
Subroutine editor Option, 5-54
Subscriber Package Menu Option, 8-2
Suggestion Box Option, 5-54
Summarize message Option, 5-45
Super Search Message File Option, 5-12, 11-4
Supported
Integration Agreements, 2-12
References, 8-1
Surrogate Edit Option, 5-19
Surrogates, 5-13
Symbols
Found in the Documentation, ix
System
Maintenance, 2-3
Management
Options, 2-1
T
Table of Contents, v
Tables and Figures, vii
TalkMan, 1-1, 11-5
TalkMan Option, 5-54
Task Requirements
Maintenance Timetable
Mandatory, 2-6
Suggested, 2-6
TASKBULL^XMXAPI, 7-7
TaskMan, 2-7, 2-16, 5-31, 5-35, 5-53
Taskman Management Menu, 5-49
Tasks Requeued Bug Fix, 2-13
TCP/IP, 8-1
TCP/IP COMMUNICATIONS PROTOCOL Field (#8.23), 2-11, 4-7
TCP/IP Connections and Transmission Scripts, 2-11
TCP/IP Listener, 5-49
TCP/IP TRANSMISSION SCRIPT Field (#8.24), 2-11, 4-7
Templates, 9-6
PRINT, 9-7
XMHOSTLIST, 9-7
XMMGR-BKFILER-ACTIVE_USERS/DEL, 9-8
XMMGR-BKFILER-DEL_BY_GROUP, 9-8
XMMGR-BKFILER-LENGTH_OF_QUEUES, 9-8
XMMGR-BKFILER-LONGTERM-STATS, 9-9
XMMGR-BKFILER-OLD_STATS/TABBED, 9-10
XMMGR-BKFILER-QUEUE-WAIT, 9-11
XMMGR-BKFILER-STATS/TABBED, 9-12
XMMGR-BKFILER-STATS-PLUS, 9-11
XMMGR-BKFILER-TABBED-RT, 9-13
SORT, 9-6
XMMGR-BKFILER-DAY@23:30, 9-6
XMMGR-BKFILER-TIME_PER_DATE, 9-6
Terminate mail user suggestions Option, 2-4, 2-18, 5-38
Terminate many mail users Option, 2-5, 2-19, 5-36
Terminate one mail user Option, 2-5, 2-20, 5-37
TERMMBOX^XMXAPIB, 7-7
TERMMSG^XMXAPI, 7-7
TEST^XMUPIN API, 2-9
TEXT^XMXEDIT, 7-8
TO DOMAIN Field (#1), 4-5
Toggle a script out of service Option, 5-50
TOWHOM^XMXAPI, 7-7
TOWHOM^XMXAPIU, 7-8
Transmission
Failures, 2-7
Priority Flexibility, 2-11
Script, 5-50
Scripts and TCP/IP Connections, 2-11
Transmission Management Menu, 5-17, 5-40, 5-48, 5-49, 5-50, 5-51, 5-54
TRANSMISSION SCRIPT File (#4.6), 2-11, 2-24, 4-7, 4-8, 5-23, 9-1, 10-1
Security, 11-6
Transmit a Single Queue Option, 5-53
Transmit All Queues Option, 5-53
Transmit TWIX's Option, 5-40
TWIX, 5-40
U
URLs
\$\$FMTE^XLFDT Home Page Web Address, 2-12
Adobe Acrobat Quick Guide Web Address, xii
Adobe Home Page Web Address, xii
HSD&D Home Page Web Address, xii
ISS
Acronyms Home Page Web Address, Glossary, 2
Glossary Home Page Web Address, Glossary, 2
MAIL^XLFNSLK Home Page Web Address, 8-1
MailMan Home Page Web Address, xii
VHA Documentation Library (VDL) Home Page Web Address, xii
Use this Manual, How to, ix
User Information Option, 5-23
User Options Edit Option, 5-20
V
VA FileMan File Security, 11-5
Validation Number Edit Option, 5-17
VAPOR^XMXEDIT, 7-8
VAPORMSG^XMXAPI, 7-7
Variables
Software-wide, 10-1
VHA Directives
10-93-142, 11-6
VHA Documentation Library (VDL)
Home Page Web Address, xii
VOLUME SET, 5-35
VSUBJ^XMXAPI, 7-7
W
WAIT^XMXUTIL, 7-11
Web Pages
\$\$FMTE^XLFDT Home Page Web Address, 2-12
Adobe Acrobat Quick Guide Web Address, xii
Adobe Home Page Web Address, xii
HSD&D Home Page Web Address, xii
ISS
Acronyms Home Page Web Address, Glossary, 2
Glossary Home Page Web Address, Glossary, 2
MAIL^XLFNSLK Home Page Web Address, 8-1
MailMan Home Page Web Address, xii
VHA Documentation Library (VDL) Home Page Web Address, xii
WEEKDAY DAYS TO PURGE Field (#4.304), 5-14
WHO^XMA21, 7-3
WRITE^XMA11A, 7-2
X
XM
\$\$NU^XM, 7-1
^XM API, 7-1
CHECKIN^XM, 7-1
CHECKOUT^XM, 7-1
EN^XM, 7-1
HEADER^XM, 7-1
KILL^XM API, 7-1
N1^XM API, 7-1
NEW^XM API, 7-1
Routine, 3-1
XM AUTO-FORWARD WAIVER Security Key, 11-3
XM BANNER MESSAGE Bulletin, 2-8
XM CAC ADPAC Security Key, 11-3
XM DATE PURGE WARNING Bulletin, 2-8
XM DELIVERY BASKET EDIT Option, 5-11
XM DOMAIN ADDED Bulletin, 2-8
XM FILTER EDIT Option, 5-11
XM FILTER FWD ADDRESS DELETE Bulletin, 2-8
XM FWD ADDRESS CHANGE Bulletin, 2-8
XM FWD ADDRESS CHECK Bulletin, 2-8
XM FWD ADDRESS DELETE Bulletin, 2-8
XM GROUP EDIT MASTER Security Key, 11-3
XM GROUP EDIT NOTIFY Bulletin, 2-8
XM GROUP ERROR Bulletin, 2-8
XM GROUP PRIORITY Security Key, 11-4
XM IN BASKET PURGE REQUEST Bulletin, 2-9
XM IN BASKET PURGE WARNING Bulletin, 2-9
XM NO BROADCASTS Security Key, 5-57, 11-4
XM PERSONAL MENU, 5-11, 5-12, 5-15, 5-19, 5-20
XM RELAY ATTEMPTED Bulletin, 2-9
XM SEND ERR MSG Bulletin, 2-9
XM SEND ERR RECIPIENT Bulletin, 2-9
XM SEND ERR REMOTE MSG ID Bulletin, 2-9
XM SEND ERR SERVER MSG Bulletin, 2-9
XM SEND ERR TRANSMISSION Bulletin, 2-9
XM SUPER SEARCH
Bulletin, 2-10, 5-12
Mail Group, 5-12, 11-1
Menu, 11-1, 11-2
Option, 5-12, 11-4
Security Key, 5-12, 11-4
XM TOO MANY MESSAGES Bulletin, 2-10
XM_TRANSMISSION_ERROR Bulletin, 2-10
XMA
REC^XMA, 7-1
Routine, 3-1
XMA0
ENTPRT^XMA0, 7-1
HDR^XMA0, 7-2
PR2^XMA0, 7-2
Routine, 3-1
XMA03
\$\$REN^XMA03, 7-2
Routine, 3-1
XMA11
\$\$INFO^XMA11, 7-2
Routine, 3-1
XMA11A
Routine, 3-1
WRITE^XMA11A, 7-2
XMA1B
KL^XMA1B, 7-2
KLQ^XMA1B, 7-2
Routine, 3-1
S2^XMA1B, 7-2
XMA1C
REMSBMSG^XMA1C, 7-2
Routine, 3-1
SETSB^XMA1C, 7-2
XMA2
GET^XMA2, 7-2
Routine, 3-1
XMZ^XMA2, 7-3
XMA21
CHK^XMA21, 7-3
DES^XMA21, 7-3
DEST^XMA21, 7-3
INST^XMA21, 7-3
Routine, 3-1
WHO^XMA21, 7-3
XMA21C
Routine, 3-1
XMA2B
Routine, 3-1
XMA2R
\$\$ENT^XMA2R, 7-3
\$\$ENTA^XMA2R, 7-3
Routine, 3-1
XMA3
Routine, 3-1
XMA30
Routine, 3-1
XMA32
Routine, 3-1
XMA32A
Routine, 3-1
XMA7
Routine, 3-1
XMAD2
\$\$BSKT^XMAD2, 7-3
Routine, 3-1
XMADGO
Routine, 3-1
ZTSK^XMADGO API, 7-3
XMAFTP
Routine, 3-1
XMAH
ENT8^XMAH, 7-3
Routine, 3-2
XMAH1
^XMAH1 API, 7-3
ENTA^XMAH1, 7-4
Routine, 3-2
XMAI2
Routine, 3-2
XMAPBLOB
Routine, 3-2
XMAPHOST
Routine, 3-2
XMASEC
Routine, 3-2
XMASSUME Option, 5-13
XMAUTOPURGE Option, 2-4, 2-5, 2-6, 2-16, 2-17, 3-1, 5-10, 5-14, 5-16, 5-45, 5-53
XMB
^XMB, 7-4
BULL^XMB, 7-4
EN^XMB, 7-4
Routine, 3-2
XMBANNER Option, 5-15
XMBASKLIST Option, 5-15
XMBBLOB
Routine, 3-2
XMBGRP
\$\$DM^XMBGRP, 7-4
\$\$MG^XMBGRP, 7-4
Routine, 3-2
XMBLOB Security Key, 5-15
XMBLOBSEND Option, 5-10, 5-15
XMC
Routine, 3-2
XMC1
Routine, 3-2
XMC11
Routine, 3-2
XMC1A
Routine, 3-2
XMC1B
Routine, 3-2
XMCB
Routine, 3-2
XMCD
Routine, 3-2
XMCDNT
Routine, 3-2
XMCE
Routine, 3-2
XMCHRIS Option, 5-15, 5-23
XMCLEAN Option, 2-4, 2-5, 2-6, 2-16, 3-1, 5-16
XMCP
Routine, 3-2
XMCQ
Routine, 3-2
XMCQA
Routine, 3-2
XMCQH
Routine, 3-2
XMCSIZE
Routine, 3-2
XMCTLK
GO^XMCTLK API, 7-4
Routine, 3-2
XMCTRAP
Routine, 3-2
XMCU1, 7-4
\$\$DECODEUP^XMCU1, 7-4
\$\$ENCODEUP^XMCU1, 7-4
\$\$RTRAN^XMCU1, 7-4
\$\$STRAN^XMCU1 API, 7-4
Routine, 3-2
XMCX
Routine, 3-2
XMCXT
Routine, 3-2
XMCXU
Routine, 3-2
XMD
^XMD API, 7-4
EN1^XMD, 7-4
ENL^XMD, 7-4
ENT^XMD, 7-4
ENT1^XMD, 7-5
ENT2^XMD, 7-5
Routine, 3-2
XMDIR1
Routine, 3-2
XMDIR1A
Routine, 3-2
XMDIR1B
Routine, 3-2
XMDIRQST
Routine, 3-3
XMDIRRCV
Routine, 3-3
XMDIRSND
Routine, 3-3
XMDX Option, 5-16, 5-17, 5-43
XMDX Option, 5-10
XMDXMODEM Options, 5-16
XMDXNAME Option, 5-17
XMDXPROT Option, 5-17
XMDXSCRIPT Option, 5-17
XMDXSMTP Option, 5-17
XMEDITBUL Option, 2-21, 5-18
XMEDITDIST Option, 2-21, 5-18
XMEDIT-DOMAIN-VALIDATION# Option, 5-17
XMEDITFWD Option, 5-19
XMEDITMG Option, 2-22, 5-19
XMEDITPERSGROUP Option, 5-19
XMEDIT-REMOTE-USER Option, 2-25, 5-18
XMEDITSURR Option, 5-19
XMEDITUSER Option, 5-20
XMENROLL Option, 2-21, 5-20
XMFAX
Routine, 3-3
XM-FTP-GET Option, 5-12, 5-13
XM-FTP-PUT Option, 5-12, 5-13
XMGAPI0
\$\$SUBCHK^XMGAPI0, 7-5
\$\$SUBGET^XMGAPI0, 7-5
Routine, 3-3
XMGAPI0s
\$\$HDR^XMGAPI2, 7-5
XMGAPI1
\$\$READ^XMGAPI1, 7-5
Routine, 3-3
XMGAPI2
Routine, 3-3
XMGAPI3
Routine, 3-3
XMGAPI4
Routine, 3-3
XMHELP Menu, xi, 5-13, 5-21, 5-22, 5-23
XMHELPALL Option, 5-22
XMHELPGROUP Option, 5-22
XMHELPLNK Option, 5-22
XMHELP-ON-LINE-USER_MANUAL Option, 5-22
XMHELPQUEST Option, 5-22
XMHELPUSER Option, 5-23
XMHIG
Routine, 3-3
XMHIU
Routine, 3-3
XMHOSTLIST PRINT Template, 9-7
XMIT IAUDIT IP ADDRESS Field (#60,3), 4-6
XMIT IP ADDRESSES TRIED Field (#48), 4-6
XMJBL
Routine, 3-3
XMJBM
Routine, 3-3
XMJBM1
Routine, 3-3
XMJBN
Routine, 3-3
XMJBN1
Routine, 3-3
XMJBU
Routine, 3-3
XMJBULL
Routine, 3-3
XMJDIR
Routine, 3-3
XMJERR
Routine, 3-3
XMJMA
Routine, 3-3
XMJMC
Routine, 3-3
XMJMCODE
Routine, 3-3
XMJMD
Routine, 3-3
XMJMF
Routine, 3-3
XMJMF1
Routine, 3-3
XMJMF2
Routine, 3-3
XMJMFA
Routine, 3-3
XMJMFB
Routine, 3-3
XMJMFC
Routine, 3-3
XMJML
Routine, 3-3
XMJMLN
Routine, 3-3
XMJMLR
Routine, 3-3
XMJMLR1
Routine, 3-4
XMJMOI
Routine, 3-4
XMJMOI1
Routine, 3-4
XMJMOIE
Routine, 3-4
XMJMOR
Routine, 3-4
XMJMORX
Routine, 3-4
XMJMORX1
Routine, 3-4
XMJMP
Routine, 3-4
XMJMP1
Routine, 3-4
XMJMP2
Routine, 3-4
XMJMQ
Routine, 3-4
XMJMQ1
Routine, 3-4
XMJMR
Routine, 3-4
XMJMR1
Routine, 3-4
XMJMRO
Routine, 3-4
XMJMS
Routine, 3-4
XMJMSA
Routine, 3-4
XMJMSO
Routine, 3-4
XMJMT
Routine, 3-4
XMKP
Routine, 3-4
XMKP1
Routine, 3-4
XMKPL
Routine, 3-4
XMKPLQ
Routine, 3-4
XMKPO
Routine, 3-4
XMKPR
Routine, 3-4
XMKPR1
Routine, 3-4
XMKPRD
Routine, 3-4
XMKSP Option, 2-24, 5-23
XML
GET^XML, 7-5
Routine, 3-4
XML1CRC
Routine, 3-4
XML4CRC
Routine, 3-4
XML4CRC1
Routine, 3-4
XMLATER-EDIT Option, 5-23
XMLATER-REPORT Option, 5-23
XMLIST Option, 5-23
XMLPC
Routine, 3-4
XMLSWP
Routine, 3-4
XMLSWP0
Routine, 3-4
XMLSWP2
Routine, 3-4
XMLTCP
Routine, 3-5
XMM1
Routine, 3-5
XMM2
Routine, 3-5
XMMASTER Menu, 5-1, 5-10, 5-24, 5-39, 5-55
XMMGR
Menu, 2-1, 2-3, 5-24, 5-30, 5-33
Security Key, 5-28, 5-46, 11-3, 11-4
XMMGR- BKFILER-TABBED-STATS Option, 2-23
XMMGR Menu, 2-14, 5-12, 5-23, 5-28, 5-31, 5-33, 5-39, 5-55
XMMGR Security Key, 2-17, 2-25, 5-28
XMMGR-BACKGROUND-FILER Option, 5-10, 5-25
XMMGR-BKFILER-ACT Option, 2-22, 5-25
XMMGR-BKFILER-ACTIVE_USERS/DEL PRINT Template, 9-8
XMMGR-BKFILER-DAY@23:30 SORT Template, 9-6
XMMGR-BKFILER-DEL_BY_GROUP PRINT Template, 9-8
XMMGR-BKFILER-EDIT-NORMALIZED Option, 2-23, 5-25
XMMGR-BKFILER-GROUP Option, 2-23, 5-25
XMMGR-BKFILER-LENGTH_OF_QUEUES PRINT Template, 9-8
XMMGR-BKFILER-LONGTERM-STATS PRINT Template, 9-9
XMMGR-BKFILER-OLD_STATS/TABBED PRINT Template, 9-10
XMMGR-BKFILER-QUEUE-WAIT PRINT Template, 9-11
XMMGR-BKFILER-STAT Option, 2-23, 5-26
XMMGR-BKFILER-STATS/TABBED PRINT Template, 9-12
XMMGR-BKFILER-STATS-PLUS PRINT Template, 9-11
XMMGR-BKFILER-TABBED-RT PRINT Template, 9-13
XMMGR-BKFILER-TABBED-STATS Option, 5-26
XMMGR-BKFILER-TIME_PER_DATE SORT Template, 9-6
XMMGR-BKFILER-WAIT Option, 5-10, 5-26
XMMGR-CHECK-BACKGROUND-FILER Option, 2-22, 5-26
XMMGR-DELIVERY-STATS-COLL Option, 2-23, 5-27
XMMGR-DIRECTORY-ALL Option, 2-26, 5-27
XMMGR-DIRECTORY-EDITGRP Option, 2-25, 2-26, 5-27, 5-28
XMMGR-DIRECTORY-GROUP Option, 2-25, 5-27
XMMGR-DIRECTORY-LISTGRP Option, 2-26, 5-28
XMMGR-DIRECTORY-MAIN Menu, 2-25, 5-18, 5-27, 5-28, 5-29
XMMGR-DIRECTORY-RECV Option, 5-10, 5-28
XMMGR-DIRECTORY-SEND Option, 5-10, 5-29
XMMGR-DIRECTORY-SINGLE Option, 2-26, 5-29
XMMGR-DIRECTORY-VACO Option, 2-26, 5-29
XMMGR-DISK-MANY-MESSAGE-MAINT Option, 2-3, 2-6, 2-10, 2-15, 5-29
XMMGR-DISK-SPACE-MANAGEMENT Menu, 2-3, 2-15, 2-17, 5-16, 5-29, 5-30, 5-31, 5-32, 5-34, 5-36, 5-37, 5-38, 5-45, 5-46, 5-53, 5-57
XMMGR-GROUP-MAINTENANCE Menu, 2-20, 5-18, 5-19, 5-20, 5-30, 5-32
XMMGR-HELP Option, 2-25, 5-31
XMMGR-IN-BASKET-PURGE Option, 2-4, 2-9, 2-16, 5-31
XMMGR-LARGE-MESSAGE-REPORT Option, 2-4, 2-6, 2-16, 5-32
XMMGR-MAIL-GRP-COORDINATOR Option, 2-22, 5-32
XMMGR-MAIL-GRP-COORD-W/REMOTES Option, 2-22, 5-32
XMMGR-MESSAGE-DELIVERY-MGT Menu, 2-22, 5-25, 5-26, 5-27, 5-33, 5-34, 5-35
XMMGR-NEW-MAIL-BOX Option, 2-15, 5-33
XMMGR-NEWMESS/LOGON-STATS Option, 2-24, 5-33
XMMGR-PURGE-AI-XREF Option, 2-3, 2-6, 2-15, 5-34
XMMGR-PURGE-MESSAGE Option, 2-4, 2-17, 5-10, 5-34
XMMGR-RESPONSE-TIME-COMPILER Option, 2-6, 2-23, 5-34
XMMGR-RESPONSE-TIME-TOGGLER Option, 2-7, 2-23, 5-35
XMMGR-START-BACKGROUND-FILER Option, 2-24, 5-35
XMMGR-STOP-BACKGROUND-FILER Option, 2-24, 5-35
XMMGR-TERMINATE-MANY Option, 2-5, 2-19, 2-20, 5-36, 5-37
XMMGR-TERMINATE-ONE Option, 2-5, 2-20, 5-37
XMMGR-TERMINATE-SUGGEST Option, 2-4, 2-18, 2-20, 5-37, 5-38
XMNET
Menu, 5-39
Security Key, 5-19, 5-42, 11-4
XMNET Menu, 2-1, 2-24, 2-25, 5-15, 5-39, 5-40, 5-41, 5-47, 5-52
XMNETHELP Option, 5-41
XMNET-QUEUE-MANAGEMENT Menu, 5-23, 5-39, 5-46, 5-47, 5-53
XMNET-TRANSMISSION-MANAGEMENT Menu, 5-17, 5-40, 5-48, 5-49, 5-50, 5-51, 5-54
XMNET-TWIX-SEND Option, 5-10, 5-40
XMNET-TWIX-TRANSMIT Option, 5-10, 5-40
XMNEW Option, 5-41
XM-NEW-FEATURES Option, 5-13
XMNEWUSER Bulletin, 2-10
XMNOPRIV Security Key, 5-52, 11-4
XMNTEG
Routine, 3-5
XMNTEG0
Routine, 3-5
XMOTHER Menu, 5-15, 5-23, 5-41, 5-42
XMOTHER-COMMUNICATIONS Menu, 5-10, 5-42
XMP
Routine, 3-5
XMP2
Routine, 3-5
XMP2A
Routine, 3-5
XMP3
Routine, 3-5
XMPACK Option, 5-42
XMPC
Routine, 3-5
XMPCOM Option, 5-43
XMPG
ENT^XMPG, 7-5
Routine, 3-5
XMPGLO Option, 5-43
XMPH
Routine, 3-5
XMPINS Option, 5-43
XMPOLL Option, 5-10, 5-43
XMPOST Option, 5-43
XMPPRT Option, 5-44
XMPRECV Menu, 5-44
XMPRECV Option, 5-10
XMPROU Option, 5-44
XMPSEC
Routine, 3-5
XMPSEND Option, 5-10, 5-45
XMPSUM Option, 5-45
XMPURGE Option, 2-4, 2-17, 5-45, 5-53
XMPURGE-BY-DATE Option, 2-4, 2-6, 2-8, 2-17, 5-46, 5-53
XMQ- Security Keys, 11-4
XMQACTIVE Option, 5-46
XMQDISP Option, 5-46
XMQDOMAINS Option, 5-47
XMQHIST Option, 5-47
XMQSHOW Option, 5-47
XMQUEUED Option, 5-47
XMR
Routine, 3-5
XMR0BLOB
Routine, 3-5
XMR1
Routine, 3-5
XMR2
Routine, 3-5
XMR3
Routine, 3-5
XMR3A
Routine, 3-5
XMR4
Routine, 3-5
XMR-BROADCAST-VA-WIDE Option, 5-10, 5-48, 5-57
XMRDACK Bulletin, 2-10
XMREAD Option, 5-49, 7-1
XMRENT
\$\$NET^XMRENT, 7-5
Routine, 3-5
XMRFTP
Routine, 3-5
XMRFTPUX
Routine, 3-5
XMRINETD
Routine, 3-5
XMRMSM
Routine, 3-5
XMRONT
Option, 5-49
Routine, 3-5
XMRONT Option, 5-10
XMRPCTS
Routine, 3-5
XMRPCTS0
Routine, 3-5
XMRPCTS1
Routine, 3-5
XMRPCTSA
Routine, 3-5
XMRPOP
Routine, 3-5
XMR-SEQ-RECEIVE Option, 5-48, 5-50
XMRTCP
Routine, 3-5
XMRTCPGO
Routine, 3-5
XMR-UCI-RCV Option, 5-48, 5-49
XMR-UCI-SEND Option, 5-48, 5-49
XMRUCX
Routine, 3-5
XMS
Routine, 3-5
XMS0BLOB
Routine, 3-6
XMS1
\$\$SRVTIME^XMS1, 7-5
\$\$STATUS^XMS1, 7-5
Routine, 3-6
XMS2
Routine, 3-6
XMS3
REC^XMS3, 7-5
Routine, 3-6
XMSCRIPTEDIT Option, 5-50
XMSCRIPTOUT Option, 5-50
XMSCRIPTPLAY Option, 5-51
XMSCRIPTRES Option, 5-10, 5-51
XMSEARCH Option, 5-51
XMSEND Option, 5-52
XMSFTP
Routine, 3-6
XMSFTPUX
Routine, 3-6
XMSHARE Option, 5-10, 5-52
XMSITE Option, 5-52
XMS-SEQ-TRANSMIT Option, 5-48, 5-50
XMSTAR LIMITED Security Key, 2-7, 11-4
XMSTAR Security Key, 2-7, 11-4
XMSTARTQUE Option, 5-47, 5-53
XMSTARTQUE-ALL Option, 5-47, 5-53
XMSTAT Option, 2-4, 2-16, 5-45, 5-53
XMSUBEDIT Option, 5-54
XMSUGGESTION Option, 5-10, 5-54
XMTALK
Option, 5-54
Security Key, 5-54, 11-5
XMTALK Option, 5-10
XMTDF
Routine, 3-6
XMTDL
Routine, 3-6
XMTDL1
Routine, 3-6
XMTDL2
Routine, 3-6
XMTDO
Routine, 3-6
XMTDR
Routine, 3-6
XMTDT
Routine, 3-6
XMUCXPOP
Routine, 3-6
XMUDCHK
Routine, 3-6, 5-47
XMUDCHR
Routine, 3-6
XMUDNC
Routine, 3-6
XMUDTOP
Routine, 3-6
XMUPIN
Routine, 3-6
XMUSER Menu, 2-2, 2-26, 5-12, 5-13, 5-21, 5-41, 5-49, 5-51, 5-52, 5-55
XMUT1
Routine, 3-6
XMUT1A
Routine, 3-6
XMUT2
Routine, 3-6
XMUT4
Routine, 3-6
XMUT41
Routine, 3-6
XMUT4A
Routine, 3-6
XMUT4C
Routine, 3-6
XMUT5
Routine, 3-6
XMUT5B
Routine, 3-6
XMUT5C
Routine, 3-6
XMUT5G
Routine, 3-6
XMUT5Q
Routine, 3-6
XMUT5Q1
Routine, 3-6
XMUT5R1
Routine, 3-6
XMUT5R2
Routine, 3-6
XMUT6
Routine, 3-6
XMUT7
ENT^XMUT7, 7-5
Routine, 3-7
XMUT-CHKFIL Option, 2-5, 2-6, 2-14, 5-14, 5-55
XMUTCOM1
Routine, 3-7
XMUTERM
Routine, 3-7
XMUTERM1
Routine, 3-7
XMUTERM2
Routine, 3-7
XMUTPUR0
Routine, 3-7
XMUT-REC‑DELETE Option, 2-18, 5-56
XMUT-REC‑DELIVER Option, 2-18, 5-56
XMUT-REC-FIND Option, 2-18, 5-56, 5-57
XMUT-REC-MENU Menu, 2-17, 5-56, 5-57
XMUT-REC-RPT Option, 2-18, 5-56, 5-57
XMVALBAD Bulletin, 2-10
XMVGROUP
Routine, 3-7
XMVGRP
Routine, 3-7
XMVSURR
Routine, 3-7
XMVVITA
Routine, 3-7
XMVVITAE
INIT^XMVVITAE, 7-5
OTHER^XMVVITAE, 7-5
Routine, 3-7
SELF^XMVVITAE, 7-6
XMXADDR
Routine, 3-7
XMXADDR1
Routine, 3-7
XMXADDR2
Routine, 3-7
XMXADDR3
Routine, 3-7
XMXADDR4
Routine, 3-7
XMXADDRD
Routine, 3-7
XMXADDRG
Routine, 3-7
XMXANSER
Routine, 3-7
XMXAPI
ADDRNSND^XMXAPI, 7-6
ANSRMSG^XMXAPI, 7-6
CRE8XMZ^XMXAPI, 7-6
DELMSG^XMXAPI, 7-6
FLTRMSG^XMXAPI, 7-6
FWDMSG^XMXAPI, 7-6
LATERMSG^XMXAPI, 7-6
MOVEMSG^XMXAPI, 7-6
PRTMSG^XMXAPI, 7-6
PUTSERV^XMXAPI, 7-6
REPLYMSG^XMXAPI, 7-6
Routine, 3-7
SENDBULL^XMXAPI, 7-6
SENDMSG^XMXAPI, 7-6
TASKBULL^XMXAPI, 7-7
TERMMSG^XMXAPI, 7-7
TOWHOM^XMXAPI, 7-7
VAPORMSG^XMXAPI, 7-7
VSUBJ^XMXAPI, 7-7
ZAPSERV^XMXAPI, 7-7
XMXAPIB
CRE8BSKT^XMXAPIB, 7-7
CRE8MBOX^XMXAPIB, 7-7
DELBSKT^XMXAPIB, 7-7
FLTRBSKT^XMXAPIB, 7-7
FLTRMBOX^XMXAPIB, 7-7
LISTBSKT^XMXAPIB, 7-7
LISTMSGS^XMXAPIB, 7-7
NAMEBSKT^XMXAPIB, 7-7
QBSKT^XMXAPIB, 7-7
QMBOX^XMXAPIB, 7-7
Routine, 3-7
RSEQBSKT^XMXAPIB, 7-7
TERMMBOX^XMXAPIB, 7-7
XMXAPIG
\$\$GOTLOCAL^XMXAPIG, 7-8
ADDMBRS^XMXAPIG, 7-8
DROP^XMXAPIG, 7-8
JOIN^XMXAPIG, 7-8
Routine, 3-7
XMXAPIU
READ^XMXAPIU, 7-8
READNEW^XMXAPIU, 7-8
Routine, 3-7
SEND^XMXAPIU, 7-8
TOWHOM^XMXAPIU, 7-8
XMXBSKT
Routine, 3-7
XMXBULL
Routine, 3-7
XMXEDIT
CLOSED^XMXEDIT, 7-8
CONFID^XMXEDIT, 7-8
CONFIRM^XMXEDIT, 7-8
DELIVER^XMXEDIT, 7-8
INFO^XMXEDIT, 7-8
PRIORITY^XMXEDIT, 7-8
Routine, 3-7
SUBJ^XMXEDIT, 7-8
TEXT^XMXEDIT, 7-8
VAPOR^XMXEDIT, 7-8
XMXGRP
Routine, 3-7
XMXGRP1
Routine, 3-7
XMXLIST
Routine, 3-7
XMXLIST1
Routine, 3-7
XMXLIST2
Routine, 3-7
XMXMBOX
Routine, 3-7
XMXMSGS
Routine, 3-7
XMXMSGS1
Routine, 3-7
XMXMSGS2
Routine, 3-7
XMXPARM
Routine, 3-8
XMXPARM1
Routine, 3-8
XMXPARMB
Routine, 3-8
XMXPRT
Routine, 3-8
XMXREPLY
Routine, 3-8
XMXSEC
\$\$ACCESS^XMXSEC, 7-8
\$\$ANSWER^XMXSEC, 7-8
\$\$BCAST^XMXSEC, 7-8
\$\$CLOSED^XMXSEC, 7-8
\$\$CONFID^XMXSEC, 7-8
\$\$CONFIRM^XMXSEC, 7-8
\$\$COPY^XMXSEC, 7-8
\$\$DELETE^XMXSEC, 7-9
\$\$FORWARD^XMXSEC, 7-9
\$\$INFO^XMXSEC, 7-9
\$\$LATER^XMXSEC, 7-9
\$\$MOVE^XMXSEC, 7-9
\$\$ORIGIN8R^XMXSEC, 7-9
\$\$POSTPRIV^XMXSEC, 7-9
\$\$PRIORITY^XMXSEC, 7-9
\$\$READ^XMXSEC, 7-9
\$\$REPLY^XMXSEC, 7-9
\$\$RPRIV^XMXSEC, 7-9
\$\$RWPRIV^XMXSEC, 7-9
\$\$SEND^XMXSEC, 7-9
\$\$SURRACC^XMXSEC, 7-9
\$\$SURRCONF^XMXSEC, 7-9
\$\$WPRIV^XMXSEC, 7-9
\$\$ZCLOSED^XMXSEC, 7-9
\$\$ZCONFID^XMXSEC, 7-9
\$\$ZCONFIRM^XMXSEC, 7-9
\$\$ZINFO^XMXSEC, 7-9
\$\$ZORIGIN8^XMXSEC, 7-9
\$\$ZPOSTPRV^XMXSEC, 7-10
\$\$ZPRI^XMXSEC, 7-10
Routine, 3-8
XMXSEC1
\$\$COPYAMT^XMXSEC1, 7-10
\$\$COPYLIMS^XMXSEC1, 7-10
\$\$COPYRECP^XMXSEC1, 7-10
\$\$PAKMAN^XMXSEC1, 7-10
\$\$SSPRIV^XMXSEC1, 7-10
\$\$ZSSPRIV^XMXSEC1, 7-10
CHKLINES^XMXSEC1, 7-10
CHKMSG^XMXSEC1, 7-10
GETRESTR^XMXSEC1, 7-10
OPTGRP^XMXSEC1, 7-10
Routine, 3-8
XMXSEC2
\$\$EDIT^XMXSEC2, 7-10
OPTEDIT^XMXSEC2, 7-10
OPTMSG^XMXSEC2, 7-10
Routine, 3-8
XMXSEC3
Routine, 3-8
XMXSEND
Routine, 3-8
XMXTO
Routine, 3-8
XMXUTIL
\$\$BMSGCT^XMXUTIL, 7-10
\$\$BNMSGCT^XMXUTIL, 7-10
\$\$BPMSGCT^XMXUTIL, 7-10
\$\$BSKTNAME^XMXUTIL, 7-10
\$\$NAME^XMXUTIL, 7-11
\$\$NETNAME^XMXUTIL, 7-11
\$\$NEWS^XMXUTIL, 7-11
\$\$TMSGCT^XMXUTIL, 7-11
\$\$TNMSGCT^XMXUTIL, 7-11
\$\$TPMSGCT^XMXUTIL, 7-11
KVAPOR^XMXUTIL, 7-10
LASTACC^XMXUTIL, 7-11
MAKENEW^XMXUTIL, 7-11
NONEW^XMXUTIL, 7-11
PAGE^XMXUTIL, 7-11
Routine, 3-8
WAIT^XMXUTIL, 7-11
XMXUTIL1
\$\$CONVERT^XMXUTIL1, 7-11
\$\$CTRL^XMXUTIL1, 7-11
\$\$DECODEUP^XMXUTIL1, 7-11
\$\$ENCODEUP^XMXUTIL1, 7-11
\$\$GMTDIFF^XMXUTIL1, 7-11
\$\$INDT^XMXUTIL1, 7-11
\$\$MAXBLANK^XMXUTIL1, 7-11
\$\$MELD^XMXUTIL1, 7-12
\$\$MMDT^XMXUTIL1, 7-12
\$\$SCRUB^XMXUTIL1, 7-12
\$\$STRIP^XMXUTIL1, 7-12
\$\$TIMEDIFF^XMXUTIL1, 7-12
\$\$TSTAMP^XMXUTIL1, 7-12
Routine, 3-8
ZONEDIFF^XMXUTIL1, 7-12
XMXUTIL2
\$\$BSKT^XMXUTIL2, 7-12
\$\$DATE^XMXUTIL2, 7-12
\$\$FROM^XMXUTIL2, 7-12
\$\$KSEQN^XMXUTIL2, 7-13
\$\$LINE^XMXUTIL2, 7-13
\$\$NEW^XMXUTIL2, 7-13
\$\$PRI^XMXUTIL2, 7-13
\$\$QRESP^XMXUTIL2, 7-13
\$\$RESP^XMXUTIL2, 7-13
\$\$SUBJ^XMXUTIL2, 7-13
\$\$ZDATE^XMXUTIL2, 7-13
\$\$ZFROM^XMXUTIL2, 7-13
\$\$ZNODE^XMXUTIL2, 7-13
\$\$ZPRI^XMXUTIL2, 7-13
\$\$ZREAD^XMXUTIL2, 7-13
\$\$ZSUBJ^XMXUTIL2, 7-13
INMSG^XMXUTIL2, 7-12
INMSG1^XMXUTIL2, 7-12
INMSG2^XMXUTIL2, 7-12
INRESP^XMXUTIL2, 7-13
INRESPS^XMXUTIL2, 7-13
Routine, 3-8
XMXUTIL3
Q^XMXUTIL3, 7-13
QD^XMXUTIL3, 7-13
QL^XMXUTIL3, 7-13
QN^XMXUTIL3, 7-14
QX^XMXUTIL3, 7-14
Routine, 3-8
XMXUTIL4
Routine, 3-8
XMYB-BROADCAST-VA-WIDE Option, 5-10, 5-48, 5-57
XMYP18
Routine, 3-8
XMYP24
Routine, 3-8
XMYPRE
Routine, 3-8
XMZ^XMA2 API, 7-3
XUPROG
Menu, 5-1
Security Key, 2-14, 5-45, 5-55, 11-5
XUPROGMODE Security Key, 5-42, 5-46, 11-5
Z
ZAPSERV^XMXAPI, 7-7
ZONEDIFF^XMXUTIL1, 7-12
ZTSK^XMADGO API, 7-3
