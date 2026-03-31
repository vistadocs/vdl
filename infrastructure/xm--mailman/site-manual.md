---
title: MailMan Version 8 Systems Management Guide
doc_type: SM
doc_label: Site Manual / Systems Management Guide
doc_layer: anchor
doc_subject: Systems Management Guide
app_code: XM
app_name: MailMan
section: INF
app_status: active
pkg_ns: XM
patch_ver: 8
patch_id: XM*8
group_key: "XM:XM:8"
file_numbers: 
  - 200
security_keys: []
menu_options: 3
description: 
audience: 
keywords: 
  - span
  - message
  - class
  - mailman
  - messages
  - mark
  - mail
  - table
  - xmmgr
  - contents
page_count: 0
word_count: 35345
section_count: 38
table_count: 220
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_sysmgmtguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_sysmgmtguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=15"
---

![](mailman-version-8-systems-management-guide/001.png)

MAILMAN

SYSTEMS MANAGEMENT GUIDE

August 2002

Department of Veterans Affairs (VA)

Office of Information & Technology (OIT)

Product Development (PD)

<span id="_Toc137534701" class="anchor"></span>Revision History

|                                                   |                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/002.png) | NOTE: The following table displays the revision history for this document. |

<span id="_Toc142974632" class="anchor"></span>Table 1. Files and globals exported with MailMan 8.0

Table i. Documentation revision history

<table>
<caption><p><span id="_Toc323122286" class="anchor"></span>Table 2. Multimedia MailMan-related files</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 28%" />
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
<td>04/25/2012</td>
<td>4.0</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated the "Troubleshooting MailMan" section based on Remedy Ticket #HD0000000605239. Now reference the Create a Mailbox for a user option [XMMGR-NEW-MAIL-BOX] rather than calling the API.</p></li>
<li><p>Updated the "Orientation" section.</p></li>
<li><p>Updated the overall document for current national documentation standards and style guides. For example:</p></li>
</ul>
<ul>
<li><p>Changed all Heading <em>n</em> styles to use Arial font.</p></li>
<li><p>Changed all Heading <em>n</em> styles to be left justified.</p></li>
<li><p>Changed all chapter-numbering to sequential page numbering throughout.</p></li>
<li><p>Changed all Figure and Table chapter-numbering in captions to sequential numbering throughout.</p></li>
</ul></td>
<td>Tech Writer—REDACTED</td>
</tr>
<tr class="even">
<td>09/28/2006</td>
<td>3.0</td>
<td><p>MailMan 8.0 documentation reformatting/revision.</p>
<ul>
<li><p>Reformatted document to follow the latest ISS styles and guidelines. This is the initial complete reformatting of this manual since its original release with MailMan 7.1 in June 1994.</p></li>
<li><p>As of this date, all content updates have been completed for all released MailMan patches.</p></li>
<li><p>Also, reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p></li>
</ul>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to standards and conventions as indicated below:</p>
<ul>
<li><p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p></li>
<li><p>Patient or user names are formatted as follows: XMPATIENT,[N] or XMUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., XMPATIENT, ONE, XMPATIENT, TWO, etc.).</p></li>
<li><p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td><p>MailMan Development Team REDACTED, CA Office of Information Field Office (OIFO):</p>
<ul>
<li><p>REDACTED</p></li>
<li><p>Technical Writer—REDACTED</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>07/23/2002</td>
<td>2.0</td>
<td>Initial MailMan 8.0 software and documentation release. MailMan 8.0 was first released as "DNS-Aware MailMan" in a supplemental document released in August 2002. However, the remaining MailMan documentation set was never updated.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>June 1994</td>
<td>1.0</td>
<td>Initial creation of the <em>MailMan Systems Management Guide</em>.</td>
<td><p>MailMan Development Team REDACTED, CA Office of Information Field Office (OIFO):</p>
<ul>
<li><p>REDACTED</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc323122286" class="anchor"></span>Table 2. Multimedia MailMan-related files

Patch Revisions

For the current patch history related to this software, please refer to the Patch Module on FORUM.

Contents

[1.1.2.4 GO^XMTDL (task)—Deliver Messages for Specific Group and  
Queue [5](#goxmtdl-taskdeliver-messages-for-specific-group-and-queue)](#goxmtdl-taskdeliver-messages-for-specific-group-and-queue)

<span id="_Toc323122415" class="anchor"></span>Figures and Tables

Figures

[Figure 5. Forward message: Code performed to set nodes containing DUZ of forwarded mail  
recipients [4](#_Toc147217274)](#_Toc147217274)

Tables

<span id="_Hlt448198621" class="anchor"></span>Orientation

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of MailMan 8.0 and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

This manual discusses the use of electronic network communication software and covers network features for sending and receiving transmissions, responding, and transmitting mail. Many user actions are available for completing specific tasks.

It acquaints system managers with the utilities, software structure and functionality of the MailMan system modules, including information about the routines, options, fields, and files that comprise MailMan and are used to implement and maintain MailMan. It also has information about MailMan's structure and recommendations regarding MailMan's efficient use. Additional information on security, management features, and other requirements is also included. This manual does *not* describe the MailMan user interface nor does it detail its use in software development.

Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Information Resource Management (IRM)—System administrators at Department of Veterans Affairs (VA) sites who are responsible for implementing and maintaining MailMan.
- Product Development (PD)—VistA legacy development teams.
- Product Support (PS).

Legal Requirements

<table>
<caption><p><span id="_Toc142974576" class="anchor"></span>Table 3. Routine mapping recommendations for MailMan 8.0</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-systems-management-guide/003.png)</td>
<td><p>CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of MailMan for non-VistA use should be referred to the VistA site's local Office of Information Field Office (OIFO).</p>
<p>Otherwise, there are no special legal requirements involved in the use of MailMan.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc142974576" class="anchor"></span>Table 3. Routine mapping recommendations for MailMan 8.0

Disclaimers

This manual provides an overall explanation of the MailMan software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the Internet and VA Intranet for a general orientation to VistA. For example, go to the Office of Information and Technology (OIT) VistA Development Intranet Website: http://vista.med.va.gov

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/004.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

<span id="_Toc147217297" class="anchor"></span>Table 4. Task requirements: Mandatory maintenance timetable

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

Table ii. Documentation symbol descriptions

|                                                   |                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Symbol                                            | Description                                                                                                         |
| ![](mailman-version-8-systems-management-guide/005.png) | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](mailman-version-8-systems-management-guide/006.png) | CAUTION/RECOMMENDATION/DISCLAIMER: Used to caution the reader to take special notice of critical information.   |

<span id="_Toc147217298" class="anchor"></span>Table 5. Task requirements: Suggested maintenance timetable

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
- Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in MailMan (XM) test patient and user names would be documented as follows: XMPATIENT,ONE; XMPATIENT,TWO; XMPATIENT,THREE; etc.
- "Snapshots" of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.
- User's responses to online prompts will be bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box will be bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words will be bold typeface with alternate color font.
- References to "\<Enter\>" within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                   |                                                                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/007.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

<span id="_Toc142974581" class="anchor"></span>Table 6. MailMan 8.0: New date/time format

|                                                   |                                                                                                                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/008.png) | NOTE: Unless otherwise noted, all sample screen captures/dialogue boxes in this manual are derived from using either MailMan's Detailed or Summary Full Screen message readers. |

<span id="_Toc142974582" class="anchor"></span>Table 7. MailMan 8.0: New remote message ID format

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS will be considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

Documentation Navigation

This document uses Microsoft® Word's built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word 2007 (not the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the drop-down arrow in the "Choose commands from:" box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Click/Highlight the Back command and press the Add button to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Click/Highlight the Forward command and press the Add button to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

|                                                   |                                                                                                                                       |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/009.png) | NOTE: This is a one-time setup and will automatically be available in any other Word document once you install it on the Toolbar. |

<span id="_Toc142974583" class="anchor"></span>Table 8. MailMan 8.0: New name field display format

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                   |                                                                                                                                      |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/010.png) | NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

<span id="_Toc147217310" class="anchor"></span>Table 9. PackMan menu functions

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

In addition to the "question mark" help, you can use the Help (User/Group Info., etc.) menu option on the main MailMan Menu to access the MailMan Help Frames through the following options:

- New Features in MailMan
- General MailMan Information
- Questions and Answers on MailMan
- Manual for MailMan Users

|                                                   |                                                                                                                                                    |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/011.png) | REF: For more information on obtaining MailMan online help, please refer to Chapter 12, "Online Help Information" in the *MailMan User Guide*. |

<span id="_Toc323122294" class="anchor"></span>Table 10. Escape functions

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                   |                                                                                                                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/012.png) | REF: For details about obtaining data dictionaries and about the formats available, see the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

<span id="_Toc147217313" class="anchor"></span>Table 11. Advantages and disadvantages of using TalkMan and IDCU

Assumptions about the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about MailMan should consult the following:

- *MailMan Release Notes*
- *MailMan Installation Guide*
- *MailMan Getting Started Guide*
- *MailMan Developer's Guide*
- *MailMan User Guide*
- *MailMan Network Reference Guide*
- *MailMan Package Security Guide*
- *MailMan Systems Management Guide (this manual)*
- *MailMan Technical Manual*
- MailMan Home Page at the following VA Intranet website: http://vista.med.va.gov/mailman/index.asp

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at the following Website: <http://www.adobe.com/>

VistA documentation can be downloaded from the VHA Software Document Library (VDL) Website: <http://www.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Product Support (PS) anonymous directories:

- Preferred Method REDACTED

|                                                   |                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/013.png) | NOTE: This method transmits the files from the first available FTP server. |

<span id="_Toc323122296" class="anchor"></span>Table 12. Error Type dictionary

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [What Happens When You Send a Message?](#what-happens-when-you-send-a-message)
    - [Messages to Local Users—Overview](#messages-to-local-usersoverview)
    - [Messages to Local Users—Detail](#messages-to-local-usersdetail)
    - [Messages to Devices, Servers, and Remote Sites—Detail](#messages-to-devices-servers-and-remote-sitesdetail)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Software Management](#software-management)
    - [Postmaster](#postmaster)
    - [Maintenance](#maintenance)
    - [Namespace](#namespace)
    - [Controlled Procedures](#controlled-procedures)
    - [Legal Requirements](#legal-requirements)
    - [Files](#files)
    - [Routines](#routines)
    - [System Maintenance](#system-maintenance)
    - [Bulletins](#bulletins)
  - [Manage MailMan](#manage-mailman)
    - [Management Features in MailMan 8.0](#management-features-in-mailman-80)
  - [Menu Structure](#menu-structure)
    - [XMMGR](#xmmgr)
    - [XMNET](#xmnet)
    - [XMUSER](#xmuser)
    - [Manage MailMan \[XMMGR\]](#manage-mailman-xmmgr)
- [Troubleshooting MailMan](#troubleshooting-mailman)
- [DNS-Aware MailMan](#dns-aware-mailman)
- [PackMan](#packman)
  - [PackMan Functions](#packman-functions)
  - [Loading Routines into PackMan Messages](#loading-routines-into-packman-messages)
  - [Loading Global Data into a PackMan Message](#loading-global-data-into-a-packman-message)
    - [Compare PackMan Message Routines against those Installed](#compare-packman-message-routines-against-those-installed)
  - [Installing a PackMan Message](#installing-a-packman-message)
  - [Summarize PackMan Message](#summarize-packman-message)
  - [Loading an Entire Software Package into a PackMan Message](#loading-an-entire-software-package-into-a-packman-message)
  - [Printing PackMan Messages](#printing-packman-messages)
  - [Editing PackMan Messages](#editing-packman-messages)
  - [Why Editing PackMan Messages Can Cause Problems](#why-editing-packman-messages-can-cause-problems)
  - [Ways to Ensure Integrity of PackMan Messages](#ways-to-ensure-integrity-of-packman-messages)
  - [Security of PackMan Messages](#security-of-packman-messages)
  - [Installing PackMan Messages into a Second Account](#installing-packman-messages-into-a-second-account)
- [TalkMan](#talkman)
  - [TalkMan—Communications Tool](#talkmancommunications-tool)
  - [How to Capture a Session into a MailMan Message](#how-to-capture-a-session-into-a-mailman-message)
    - [How to End a TalkMan Session](#how-to-end-a-talkman-session)
    - [How to Continue a TalkMan Session](#how-to-continue-a-talkman-session)
    - [Advantages and Disadvantages of Using TalkMan and IDCU](#advantages-and-disadvantages-of-using-talkman-and-idcu)
- [MailMan Site Parameters](#mailman-site-parameters)
- [MailMan Integrity Checker (XMUT-CHKFIL)](#mailman-integrity-checker-xmut-chkfil)
  - [Error Displays](#error-displays)
  - [Error Type Dictionary](#error-type-dictionary)
- [Fine Tuning MailMan](#fine-tuning-mailman)
  - [Capacity](#capacity)
  - [Background Filers](#background-filers)
    - [Mapped Routines](#mapped-routines)
- [MailLink Program](#maillink-program)
- [Multimedia MailMan](#multimedia-mailman)
  - [Introduction](#introduction-1)
    - [Historical Background](#historical-background)
    - [Analysis of Requirements](#analysis-of-requirements)
  - [Overview](#overview)
    - [Non-textual BLOBs in Messages](#non-textual-blobs-in-messages)
    - [Sending and Receiving BLOBs Across a Network](#sending-and-receiving-blobs-across-a-network)
  - [Requirements](#requirements)
    - [Local Mail Reading](#local-mail-reading)
    - [Network Transmissions (Sending and Receiving)](#network-transmissions-sending-and-receiving)
  - [Setup](#setup)
    - [Configuration](#configuration)
    - [Site Parameters](#site-parameters)
  - [Installation of the Imaging Software on the Workstation](#installation-of-the-imaging-software-on-the-workstation)
    - [How to Install the Network File System (NFS)](#how-to-install-the-network-file-system-nfs)
- [MailMan Script Processor](#mailman-script-processor)
  - [Generalized Device Control and Communication Utility](#generalized-device-control-and-communication-utility)
  - [How to Invoke the Script Processor](#how-to-invoke-the-script-processor)
    - [Example Call](#example-call)
    - [Mini out Subroutine](#mini-out-subroutine)
- [MailMan Distribution List](#mailman-distribution-list)
  - [Mail Groups](#mail-groups)
    - [Members of Mail Groups](#members-of-mail-groups)
    - [Creating a Distribution List](#creating-a-distribution-list)
    - [Editing a Distribution List](#editing-a-distribution-list)
- [MailMan Validation Numbers](#mailman-validation-numbers)
- [Statistics in MailMan](#statistics-in-mailman)
  - [Local Statistics](#local-statistics)
  - [Network Mail Statistics](#network-mail-statistics)
    - [VMS Systems](#vms-systems)
  - [Network Statistics](#network-statistics)
- [P-Message Device Setup](#p-message-device-setup)
  - [P-Message Definitions for the Workstation Environment Running MSM](#p-message-definitions-for-the-workstation-environment-running-msm)
- [Intercepting Twix from the PCTS System](#intercepting-twix-from-the-pcts-system)
  - [Overview](#overview-1)
    - [PCTS System Setup and Use](#pcts-system-setup-and-use)
    - [How the VistA PCTS Twix Interceptor Works](#how-the-vista-pcts-twix-interceptor-works)
  - [Setup Instructions](#setup-instructions)
  - [Setting Up the VHA.DMIA Domain](#setting-up-the-vhadmia-domain)
    - [Schedule Option for Transmitting Queue to Run Periodically](#schedule-option-for-transmitting-queue-to-run-periodically)
    - [Option for Users to Use to Send a Twix](#option-for-users-to-use-to-send-a-twix)
MailMan, the Department of Veterans Affairs (VA) electronic mail system, is a communications tool that provides electronic communication among users sharing computing facilities. A communications link can be made with cables, telephone lines, or satellite connections. In this manner, the networking of electronic mail on a large scale is made possible.
MailMan provides teleconferencing via chained responses. MailMan has become the transport vehicle for all Veterans Health Information Systems and Technology Architecture (VistA) applications. MailMan is also used to preserve copies of software and data. MailMan also has the ability to include non-textual data in messages. Network features; allow users to construct dialogues for logging on to remote systems for mail delivery. Message actions allow users great flexibility in managing personal mail. Users can address mail to individuals and groups at local and remote sites, with the tedium of waiting for process completion being reduced by the system's background filer. In addition, the system has extensive online documentation, which can be printed to create a manual.
MailMan is designed to allow users to send and receive mail from individuals or groups. A message can take the form of a personal letter or a formal bulletin extracting data from VA FileMan. The text of messages is not difficult to edit, and the context can be made confidential in several ways. Surrogates can be appointed to read mail. Mail groups can be set up to allow each member to respond to a message and to view the replies, as in an informal committee meeting. Mail can be sorted, deleted, forwarded, queried, copied, revised, or printed. In addition, MailMan cross-references messages by subject, message number, sender, and date.
The *MailMan Systems Management Guide* provides chapters on the following topics:
- Implementation and Maintenance
- Troubleshooting MailMan
- PackMan
- TalkMan
- MailMan Site Parameters
- MailMan Integrity Checker (XMUT-CHKFIL)
- Fine Tuning MailMan
- MailLink Program (including the Remote User Directory)
- Multimedia MailMan
- MailMan Script Processor
- MailMan Distribution List
- MailMan Validation Numbers
- Statistics in MailMan
- P-Message Device Setup
- Intercepting Twix from the PCTS System
These chapters provide pertinent information, along with examples, that allows system managers and developers to effectively implement, support, and maintain MailMan.

## What Happens When You Send a Message?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Messages to Local Users—Overview
- Messages to Local Users—Detail
- Messages to Devices, Servers, and Remote Sites—Detail

### Messages to Local Users—Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you send a message to local users, MailMan calls the ^XMKP routine to enter the message into a queue called ^XMBPOST("BOX".

|                                                   |                                                           |
|---------------------------------------------------|-----------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/014.png) | NOTE: Think of it as putting a letter into a mailbox. |

<span id="_Toc147217322" class="anchor"></span>Table 13. Multimedia MailMan—Site parameters

All messages (new ones, forwards, and responses) are put into ^XMBPOST("BOX" with timestamps on them so MailMan can deal with them on a first come, first served basis.

MailMan then calls CHECK^XMKPL to make sure that the background filers are running. If the background filers are *not* running, they will be started (unless they were deliberately stopped).

|                                                   |                                                                                                                                                                                                                                  |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/015.png) | NOTE: Think of it as calling the post office to see if they're open. However, the post office analogy breaks down here, because if they're not working today, they're not going to start just because you asked them nicely. |

<span id="_Toc147217325" class="anchor"></span>Table 14. Variable to process a script

The background filer we are interested in is GO^XMKPLQ. It is also known as the "mover." (The other filer, GO^XMTDT, a.k.a. the "tickler", is responsible for delivering "latered" messages and deleting inactive messages that were previously marked for deletion.) GO^XMKPLQ is constantly running and checking ^XMBPOST("BOX" to see if any messages have been put into it.

|                                                   |                                                                                                                       |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/016.png) | NOTE: Think of the mail carrier making her rounds picking up letters from the mailbox at certain times every day. |

<span id="_Toc147217330" class="anchor"></span>Table 15. Mail group user prompts

If there are messages in ^XMBPOST("BOX", GO^XMKPLQ will first read the queue definition from the MAILMAN SITE PARAMETERS file (#4.3), ^XMB(1. The queue definition tells how many queues there should be for new and forwarded messages and how many queues there should be for responses. Each queue is defined to take messages with a certain range of addressees. Then GO^XMKPLQ will go through the messages according to their timestamp and put them into their correct delivery queue, based on whether they are new or forwarded messages or responses and how many addressees they have.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/017.png) | NOTE: Think of a clerk in a post office sorting mail onto the correct delivery truck. Now imagine that there is more than one truck per route. One of the trucks would handle personal mail, like from your mom, and another would handle mass mailings, like from Publisher's Clearing House ("you may already have won..."), and there could be other trucks for other types of mail. Anyway, the letter from your mom would be delivered right to you, while the letter from Publisher's Clearing House would take forever to be delivered because it's going to every person in your neighborhood. In real life, of course, there's just one truck. MailMan can have up to 10 trucks, or queues, for responses, and 10 for new and forwarded messages, so your message to your boss does not have to be mixed in with a broadcast message about the scheduled shutdown next Saturday evening. |

<span id="_Toc147217331" class="anchor"></span>Table 16. Types of members in mail groups

Every 30 seconds, GO^XMKPLQ stops sorting messages into delivery queues long enough to check each queue to make sure there is a task assigned to that queue to deliver its messages. If there is no task running for a delivery queue that has messages in it, GO^XMKPLQ will start one up.

|                                                   |                                                                                                                                                         |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/018.png) | NOTE: Think of a supervisor at a post office making sure that there is a mail carrier for each route and calling in substitutes, if any is missing. |

GO^XMKPLQ tasks GO^XMTDL to deliver messages for a particular group (new or forwarded messages are in one group, "M", and responses are in another group, "R") and queue (1 through 10, based on your site definition in ^XMB(1,). GO^XMTDL goes through a particular group/queue and delivers its messages, according to timestamp, to their addressees.

### Messages to Local Users—Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ^XMKP

- Populates the message's "addressed to" and "recipient" multiples
- Attaches replies to the original messages
- Creates the ^XMBPOST("BOX" nodes

Definitions:

- timestamp—\$H\*86400+\$P(\$H,",",2)
- xmz—IEN of the message in ^XMB(3,9
- xmduz—DUZ of the user who sent/forwarded/responded
- bskt—Basket number (usually) or basket name

#### New Message

<span id="_Toc147217270" class="anchor"></span>Figure 1. New message: Local—Broadcast

S ^XMBPOST("BOX",timestamp,"M",xmz)=# users in xmb(3.7

\_"^"\_bskt for self

\_"^"\_bskt for shared,mail\_"^"\_delete date for shared,mail\_"^\*"

The asterisk at the very end signifies a local broadcast.

<span id="_Toc147217271" class="anchor"></span>Figure 2. New message: Local—*Not* Broadcast

S ^XMBPOST("BOX",timestamp,"M",xmz)=# addressees\_"^"\_ bskt for self

\_"^"\_bskt for shared,mail\_"^"\_delete date for shared,mail

#### Forward Message

<span id="_Toc147217272" class="anchor"></span>Figure 3. Forward message: Local—Broadcast

S ^XMBPOST("BOX",timestamp,"M",xmz\_"^"\_xmduz\_"^"\_\$J)=# users in xmb(3.7

\_"^"\_bskt for self

\_"^"\_bskt for shared,mail\_"^"\_delete date for shared,mail\_"^\*"

The asterisk at the very end signifies a local broadcast.

<span id="_Toc147217273" class="anchor"></span>Figure 4. Forward message: Local—*Not* Broadcast

S ^XMBPOST("BOX",timestamp,"M",xmz\_"^"\_xmduz\_"^"\_\$J)=# users forwarded to

\_"^"\_bskt for self

\_"^"\_bskt for shared,mail\_"^"\_delete date for shared,mail

The following nodes contain the DUZs of the users to whom the message is forwarded. They have a maximum length of 245:

<span id="_Toc147217274" class="anchor"></span>Figure 5. Forward message: Code performed to set nodes containing DUZ of forwarded mail recipients

S ^XMBPOST("FWD",xmz\_"^"\_xmduz\_"^"\_\$J\_"^"\_timestamp,1)=duz 1\_"^"\_...\_"^"\_duz j

. . .

S ^XMBPOST("FWD",xmz\_"^"\_xmduz\_"^"\_\$J\_"^"\_timestamp,#)=duz r\_"^"\_...\_"^"\_duz z

MailMan puts them in ^XMBPOST("FWD" so they do not have to be transferred from ^XMBPOST("BOX" to the ^XMBPOST("M",queue. Thus, MailMan saves processing time.

#### Reply to Message

<span id="_Toc147217275" class="anchor"></span>Figure 6. Reply to message: Code performed

S ^XMBPOST("BOX",timestamp,"R",original xmz\_"^"\_reply xmz)=#addressees

\_"^"\_xmduz (xmduz="NR" if network reply from remote site)

#### CHECK^XMKPL—Manage the Local Message Delivery Process

If the "tickler" and "mover" processes are *not* running, task them:

- GO^XMTDT (task): "Tickler"—Deliver latered messages.
- GO^XMKPLQ (task): "Mover"—Put local messages into local delivery queues.

#### GO^XMKPLQ—Define Number of Queues for Each Message/Reply Group

- S group="R" if message is a reply; "M" otherwise.
- S queue=one of the queues depending on number of addressees.

Place messages in appropriate group/queue. If the process handling the group/queue is *not* running, task it:

#### GO^XMTDL (task)—Deliver Messages for Specific Group and Queue

#### New Message

<span id="_Toc147217276" class="anchor"></span>Figure 7. New message: Code performed

S ^XMBPOST("M",queue,timestamp,xmz)= ^XMBPOST("BOX",timestamp,"M",xmz)

K ^XMBPOST("BOX",timestamp,"M",xmz)

Increment the queue "to do" counter:

<span id="_Toc147217277" class="anchor"></span>Figure 8. New message: Code performed to increment the queue "to do" counter

S ^XMBPOST("M",queue)=# messages+1

\_"^"\_# addressees+# addressees for this message

When you check the local message delivery status, this is where the information comes from on messages waiting to be delivered.

#### Forward Message

<span id="_Toc147217278" class="anchor"></span>Figure 9. Forward message: Code performed

S ^XMBPOST("M",queue,timestamp,xmz\_"^"\_xmduz\_"^"\_\$J)=

^XMBPOST("BOX",timestamp,"M",xmz\_"^"\_xmduz\_"^"\_\$J)

K ^XMBPOST("BOX",timestamp,"M",xmz\_"^"\_xmduz\_"^"\_\$J)

Increment the queue "to do" counter:

<span id="_Toc147217279" class="anchor"></span>Figure 10. Forward message: Code performed to increment the queue "to do" counter

S ^XMBPOST("M",queue)=# messages+1

\_"^"\_# addressees+# addressees for this message

#### Reply to Message

If a reply for this message is already in the queue, then file this new reply right next to it:

<span id="_Toc147217280" class="anchor"></span>Figure 11. Reply to message: Code performed when a message is already in the queue

S oldtimestamp=\$O(^XMBPOST("R",queue,"B",original xmz,0))

I oldtimestamp exists S timestamp=oldtimestamp

E S ^XMBPOST("R",queue,"B",original xmz,timestamp)=""

If replies to a message are coming in fast and furious, MailMan groups them all under the same timestamp so they can be delivered all at once. This saves processing time.

File the new reply:

<span id="_Toc147217281" class="anchor"></span>Figure 12. Reply to message: Code performed to file the new reply

S ^XMBPOST("R",queue,timestamp,original xmz,reply xmz)=^XMBPOST("BOX",timestamp,"R",original xmz\_"^"\_reply xmz)

K ^XMBPOST("BOX",timestamp,"R",original xmz\_"^"\_reply xmz)

Increment the queue "to do" counter:

<span id="_Toc147217282" class="anchor"></span>Figure 13. Reply to message: Code performed to increment the queue "to do" counter

S ^XMBPOST("R",queue)=# messages+1\_"^"\_# addressees+# addressees for this message

#### GO^XMTDL—Deliver the Messages for a Group/Queue

#### DELIVER^XMTDL1—Deliver a Message to a Recipient

The messages in the particular group/queue are delivered to each recipient. Filters, if any, will direct the message to the correct basket. Messages may be added to the group/queue while the task is running. If the queue remains without messages in it for 15 minutes, the task stops.

#### New Message

After a message is delivered, MailMan does the following:

<span id="_Toc147217283" class="anchor"></span>Figure 14. New message: Code performed to KILL ^XMBPOST

K ^XMBPOST("M",queue,timestamp,xmz)

Decrement the queue "to do" counter:

<span id="_Toc147217284" class="anchor"></span>Figure 15. New Message: Code performed to decrement the queue "to do" counter

S ^XMBPOST("M",queue)=# messages-1\_"^"\_# addressees-# addressees for this message

Increment the delivery statistics counter:

<span id="_Toc147217285" class="anchor"></span>Figure 16. New Message: Code performed to increment the delivery statistics counter

S ^XMBPOST("STATS","M")=# actual deliveries+# actual deliveries for this message

#### Forward Message

After a message is delivered, MailMan does the following:

<span id="_Toc147217286" class="anchor"></span>Figure 17. Forward message: Code performed after MailMan delivers a message

K ^XMBPOST("M",queue,timestamp,xmz\_"^"\_xmduz\_"^"\_\$J)

K ^XMBPOST("FWD",xmz\_"^"\_xmduz\_"^"\_\$J\_"^"\_timestamp)

Decrement the queue "to do" counter:

<span id="_Toc147217287" class="anchor"></span>Figure 18. Forward message: Code to decrement the queue "to do" counter

S ^XMBPOST("M",queue)=# messages-1\_"^"\_# addressees-# addressees for this message

Increment the delivery statistics counter:

<span id="_Toc147217288" class="anchor"></span>Figure 19. Forward message: Code to increment the delivery statistics counter

S ^XMBPOST("STATS","M")=# actual deliveries+# actual deliveries for this message

#### Reply to Message

Before MailMan starts delivering a reply, MailMan does the following:

<span id="_Toc147217289" class="anchor"></span>Figure 20. Reply to a message: Code performed before MailMan delivers a reply

K ^XMBPOST("R",queue,"B",original xmz,timestamp)=""

By doing so, MailMan signals that no more replies will be accepted for this message for this particular delivery.

|                                                   |                                                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/019.png) | NOTE: Think of like the mail truck has left the post office to begin delivering. Any further letters will have to go on the next truck. |

MailMan delivers the reply to each recipient on the original message.

After a reply is delivered, MailMan does the following:

<span id="_Toc147217290" class="anchor"></span>Figure 21. Reply to a message: Code performed after a reply is delivered

K ^XMBPOST("R",queue,timestamp,original xmz,reply xmz)

Decrement the queue "to do" counter:

<span id="_Toc147217291" class="anchor"></span>Figure 22. Reply to a message: Code performed to decrement the queue "to do" counter

S ^XMBPOST("R",queue)=# messages-1\_"^"\_# addressees-# addressees for this message

Increment the delivery statistics counter:

<span id="_Toc147217292" class="anchor"></span>Figure 23. Reply to a message: Code performed to increment the delivery statistics counter

S ^XMBPOST("STATS","R")=# actual deliveries+# actual deliveries for this message

### Messages to Devices, Servers, and Remote Sites—Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ^XMKP

- Populates the message's "addressed to" and "recipient" multiples
- Attaches replies to the original messages

For each remote, device, and server recipient, immediately:

#### REMOTE^XMKPO (remote)—Put message in the Postmaster's Mailbox in the Site's Basket

<span id="_Toc147217293" class="anchor"></span>Figure 24. Code performed to put message in the Postmaster's mailbox in the site's basket

S ^XMB(3.7,.5,2,1000+site \#,xmz,0)=xmz

If a task for that site is not already running, then task it:

^XMBPOST—Select transmission method and script.

ZTSK^XMB (task)—Send the messages in the queue.

#### DEVICE^XMKPO (device)—Set up, then

DEVICE^XMTDO (task)—Send the message to the device.

#### SERVER^XMKPO (server)—Set up, then

SERVER^XMTDO (task)—Send the message to the server.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Software Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan allows users to perform the following mail functions and more:

- Send messages
- Receive messages
- Respond to messages
- Copy messages
- Search messages
- Organize messages

MailMan has various entry points (i.e., Application Program Interfaces \[APIs\]) to allow other applications to trigger bulletins or send messages without user intervention. There is a communications facility (i.e., TalkMan) to allow users to automatically hook into the VA Wide Area Network; (WAN) or modems. This feature connects the user to a remote domain, playing the script to that domain without displaying it to the user. It then informs the user that the connection was successful, and can capture whatever has been displayed to the user's terminal into a message called DIALOGUE CAPTURE.

An extended search for messages can be invoked at the "Message Action" prompt, or as a stand-alone option. The extended search includes filters on the sender and the date sent.

MailMan informs users of network delivery failures and their causes. Message characteristics including Closed, Confidential, Confirmation Requests, Information, and Scrambling can be carried across the network. Software security information for PackMan can also be conveyed on the network.

MailMan allows the transfer of any word-processing text from any VA FileMan file or message into a message or response. New documents are placed in a user's "IN" basket.

### Postmaster

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan installation automatically creates a special user (DUZ=.5) called Postmaster, and Postmaster mail baskets. Persons assigned to the management of MailMan and Network mail at a site *must* be entered in the MAILMAN SITE PARAMETERS file (#4.3) as surrogates of the Postmaster and given Read and Send privileges. A person *must* sign on as him or herself and then assume the Postmaster's identity for performing Postmaster management tasks.

The Postmaster has mail baskets, and can send and receive messages like any other user. In addition to the "IN" basket and "WASTE" basket, the "ARRIVING" basket is also automatically created for the Postmaster. All mail for a site automatically comes to the Arriving basket from which it is then routed to the individual recipients. The Postmaster can examine the header information of messages, but cannot read the text of the message.

Network transmission failures are reported to the Postmaster via bulletins to the Postmaster's "IN" basket. These bulletins should be purged once the problems have been resolved. The Postmaster also needs to check the "ARRIVING" basket for purging.

The Postmaster has special domain baskets (e.g., Bay Pines, FL; Birmingham, AL; REDACTED, CA; etc.) that are numbered greater than 1000 and are used for the transmission of network mail. Network mail from a site goes to the appropriate domain basket (queue) prior to transmission. Occasionally, the Postmaster may need to stop networked message from going out. This is done by:

1.  Deleting the message number from the Postmaster's domain basket. If a message is deleted from a basket, it is deleted from a queue.
10. Using the RJD Kill off User's Job option to kill transmission of the message to the domain.

The Postmaster also may need to broadcast messages to users. To do this:

1.  Send the message to the Postmaster.
11. Assume the identity of the Postmaster.
12. Copy the message into a new message and edit any information that is not appropriate for broadcasting.
13. At the "Send to:" prompt, enter \*.

### Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several ways to keep the amount of messages stored at a minimum. MailMan provides the Disk Space Management Menu options for this purpose under the Manage MailMan main menu.

The XMAUTOPURGE option automatically purges unreferenced MailMan messages; it deletes any messages that are not in anyone's basket from the MESSAGE file (#3.9).

|                                                   |                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/020.png) | CAUTION: It is *strongly* recommended that this option be scheduled to run daily, right after the XMCLEAN option. |

The following messages are considered "referenced" and are not purged:

- Messages in user baskets
- Messages in transit (arriving or being sent)
- Server messages
- Messages being edited (including aborted edits)
- Messages that have been latered

The following fields in the MAILMAN SITE PARAMETERS file (#4.3) influence the behavior of this option:

- NO-PURGE DAYS BUFFER (#4.301)—MailMan does not purge any messages created or received in the last few days. Users choose how many days. The default is 2.
- NO-PURGE DAYS BUFFER (LOCAL) (#142)—MailMan does not purge local messages created in the last few days. Users choose how many days. The default is 7.
- WEEKDAY DAYS TO PURGE (#4.304)—On Saturdays, MailMan goes through the entire MESSAGE file (#3.9) looking for messages to purge. On the other days of the week, however, MailMan has the option of only looking at messages created or received recently. Users choose how many days. The default is to go through the entire MESSAGE file (#3.9).

|                                                   |                                                                                                                                                                                                                               |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/021.png) | CAUTION: It is strongly recommended that you set this field to something reasonable (e.g., 30 to 60 days. But, only if you follow the recommendation to schedule this option to run daily; otherwise, leave this field blank. |

- AUTOMATIC INTEGRITY CHECK (#4.303)—MailMan gives users the option of running the MAILBOX file (#3.7) portion of the integrity checker (i.e., XMUT-CHKFIL option) before it actually purges the unreferenced messages. The MUMPS cross-reference on the MAILBOX file (#3.7) is used to determine whether a message is referenced (in someone's basket) or not. If the MUMPS cross-reference is incorrect, then the purge could delete messages it should not, or leave messages that it should delete. The integrity checker ensures that the MUMPS cross-reference is correct. Users choose whether to run it or not. The default is to run it. The recommendation is to run it; however, if you find that it is simply taking too long, you can choose not to run it. If you choose not to run it, then it is recommended that you schedule the XMUT-CHKFIL option to run monthly, because globals can and do become corrupted.

|                                                   |                                                    |
|---------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/022.png) | NOTE: This option is *not* assigned to a menu. |

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace for VistA MailMan is XM. All routines and globals used in MailMan 8.0 start with XM, except for some that are shared and located in the DI and XU namespaces.

|                                                   |                                                                                                                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/023.png) | REF: For more information regarding variables used homogeneously throughout the MailMan software and a list of Application Program Interfaces (APIs), please refer to the *MailMan Developer's Guide*. |

### Controlled Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All files, fields and routines in this software are considered to perform controlled procedures and *cannot* be modified.

### Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special legal requirements involved in the use of MailMan.

Distribution of the MailMan software is unrestricted.

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This topic contains a list of all VistA MailMan files (data dictionaries) that are exported with MailMan 8.0. The list includes file numbers, global locations, and file names as follows:

| File \# | Global        | Name                                 |
|---------|---------------|--------------------------------------|
| 3.4     | ^DIC(3.4,     | COMMUNICATIONS PROTOCOL              |
| 3.51    | ^XMB(3.51,    | SPOOL DOCUMENT                       |
| 3.519   | ^XMB(3.519,   | SPOOL DATA                           |
| 3.54    | ^XMB(3.54,    | RESOURCE                             |
| 3.6     | ^XMB(3.6,     | BULLETIN                             |
| 3.7     | ^XMB(3.7,     | MAILBOX                              |
| 3.73    | ^XMB(3.73,    | MESSAGES TO BE NEW AT A LATER DATE   |
| 3.8     | ^XMB(3.8,     | MAIL GROUP                           |
| 3.816   | ^XMB(3.816,   | DISTRIBUTION LIST                    |
| 3.9     | ^XMB(3.9,     | MESSAGE                              |
| 4.2     | ^DIC(4.2,     | DOMAIN                               |
| 4.281   | ^%ZISL(4.281, | INTER-UCI TRANSFER                   |
| 4.2995  | ^XMBX(4.2995, | MAILMAN OUTSTANDING FTP TRANSACTIONS |
| 4.2996  | ^DIC(4.2996,  | INTERNET SUFFIX                      |
| 4.2997  | ^XMD(4.2997,  | REMOTE USER DIRECTORY                |
| 4.2998  | ^XMBX(4.2998, | MESSAGE DELIVERY STATS               |
| 4.2999  | ^XMBS(4.2999, | MESSAGE STATISTICS                   |
| 4.3     | ^XMB(1,       | MAILMAN SITE PARAMETERS              |
| 4.4     | ^XMB(4.4,     | MAILMAN TIME ZONE                    |
| 4.5     | ^XMB(4.5,     | NETWORK TRANSACTION                  |
| 4.501   | ^XMBX(4.501,  | NETWORK SENDERS REJECTED             |
| 4.6     | ^XMB(4.6,     | TRANSMISSION SCRIPT                  |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-systems-management-guide/024.png)</td>
<td><p><strong>REF:</strong> For descriptions of these files, please refer to the "Files" chapter in the <em>MailMan Technical Manual</em>.</p>
<p>Other pertinent file information (e.g., data dictionaries and relations with other files), can also be generated online through the use of VA FileMan utilities.</p></td>
</tr>
</tbody>
</table>

Multimedia MailMan-related Files

In order for Multimedia MailMan to work properly, sites must also have access to the following files:

| File \# | File Name        | Description                                                                          |
|---------|------------------|--------------------------------------------------------------------------------------|
| 2005    | IMAGE            | This file stores pointers to files and related data so that they can be displayed.   |
| 2005.2  | NETWORK LOCATION | This file stores the logical name of the physical location where an image is stored. |

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All MailMan routines are prefixed with the namespace XM. MailMan 8.0 is composed of and exports approximately 249 executable routines.

|                                                   |                                                                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/025.png) | REF: For a complete listing of MailMan routines with brief descriptions, please refer to the "Routines" chapter in the *MailMan Technical Manual*. |

Initialization routines can be deleted after the installation is successfully completed. Other routine information, such as the Routine Size Histogram, the Routine %Index, etc., can be generated through the use of Kernel Utilities.

#### Recommendations for Routine Mapping

Routine mapping is at the discretion of the systems manager. The RTHIST routines provide a method for each site to determine the extent to which certain routines are utilized.

DSM Sites: If your site maps routines, then rebuild your map set. As of MailMan 8.0, many routines have become obsolete and should be removed from the map set. The following is the *recommended* list of routines to map, should your site choose to map routines:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Minimum List</td>
<td>Additional List</td>
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

### System Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following chart shows mandatory and suggested system management tasks for proper maintenance of MailMan. These tasks increase utilization of software functionality and system response time. They also reduce the amount of disk space used and minimize system errors.

#### Mandatory Task Requirements

| Task        | Scheduled Time         | Frequency |
|-------------|------------------------|-----------|
| XMCLEAN     | Off Hours              | Daily     |
| XMAUTOPURGE | One Hour After XMCLEAN | Daily     |
| XMUT-CHKFIL | Off Hours              | Monthly   |

The XMAUTOPURGE option is generally run after the XMCLEAN option (the "WASTE" basket cleaner) for automatic purging (see the Clean out waste baskets \[XMCLEAN\] option). It purges messages that are not pointed to by any message recipients or senders. The XMPURGE-BY-DATE option can also be run to purge messages that have an origination date older than the date used to initiate the process (see the Purge Messages by Origination Date \[XMPURGE-BY-DATE\] option). Users are notified by a Postmaster bulletin of the proposed purging date, so that they can save important messages. These are the only options that actually KILL entries in the MESSAGE file (#3.9).

#### Suggested Task Requirements

| Task                          | Scheduled Time | Frequency                |
|-------------------------------|----------------|--------------------------|
| XMPURGE-BY-DATE               | Off Hours      | According to Site Policy |
| XMMGR-LARGE-MESSAGE-REPORT    | Off Hours      | Monthly                  |
| XMMGR-DISK-MANY-MESSAGE-MAINT | Off Hours      | Monthly                  |
| XMMGR-PURGE-AI-XREF           | Off Hours      | Quarterly                |
| XMMGR-RESPONSE-TIME-COMPILER  | Off Hours      | Daily                    |
| XMMGR-RESPONSE-TIME-TOGGLER   |                | Daily                    |

### Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All MailMan bulletins are prefixed with the namespace XM. MailMan 8.0 is composed of and exports approximately 23 bulletins.

|                                                   |                                                                                                                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/026.png) | REF: For a complete listing of MailMan bulletins with brief descriptions, please refer to the "Bulletins" topic in the "Implementation and Maintenance" chapter in the *MailMan Technical Manual*. |

|                                                   |                                                                                                                                                                                               |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/027.png) | NOTE: Bulletins will be set to vaporize based on the number of retention days indicated in the RETENTION DAYS Field (#5) in the BULLETIN file (#3.6) from the date the bulletin was sent. |

## Manage MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Management Features in MailMan 8.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This topic describes the various maintenance requirements, technical solutions, and the following improvements introduced with MailMan 8.0.

This information is directed mainly at the site's Information Resource Management (IRM) personnel.

#### MailMan 8.0 is DNS-Aware

MailMan 8.0 is now DNS-Aware. It uses Kernel's MAIL^XLFNSLK API to retrieve IP addresses. Thus, it is no longer necessary to manually update the IP addresses in the DOMAIN file (#4.2). The IP address fields still remain in the DOMAIN file (#4.2) and MailMan continues to use them. However, if they do not work, MailMan uses the Kernel API to retrieve a list of valid IP addresses. When MailMan finds one that works, MailMan replaces the non-working IP address with the working one.

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
| ![](mailman-version-8-systems-management-guide/028.png) | CAUTION: In a user basket, the "X" at the message level is a command to unload a PackMan message or KIDS build. In a remote transmit queue, the "X" changes the transmit priority. The difference is the context, and writers of MailMan front-ends should take note |

#### Reformatted Date/Times

MailMan date/times are now in a standard format, produced by Kernel's \$\$FMTE^XLFDT(datetime,"2Z") API. This call is a Supported IA. For example:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 41%" />
<col style="width: 40%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date/Time Data</td>
<td>MailMan 7.1 Date/Time Format<br />
(Old)</td>
<td>MailMan 8.0 Date/Time Format (New)</td>
</tr>
<tr class="even">
<td>3020803.153204</td>
<td>03 Aug 02 15:32</td>
<td>08/03/02@15:32</td>
</tr>
</tbody>
</table>

This change is also carried through to all MailMan APIs that return date/time in MailMan format.

|                                                   |                                                                                                                                                                                           |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/029.png) | REF: For more information on this Kernel API, please refer to the \$\$FMTE^XLFDT Home Page at the following VA Intranet website: http://vista.med.va.gov/kernel/apis/x-fmte^xlfdt.asp |

|                                                   |                                                                                                                                                                                                                                    |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/030.png) | REF: For information on how to obtain a list of Integration Agreements (IAs) related to MailMan, please refer to the "Integration Agreements (IAs)" topic in Chapter 8, "External Relations," in the MailMan Technical Manual. |

#### Reformatted Remote Message IDs

MailMan remote message IDs now include the message date, to ensure that if you are told that a message is a duplicate of a previously received message, it really is. Sites will no longer have problems sending messages from a production account to a test account that was created by "mirroring" the production account. The remote message ID is now the message number followed by a period, followed by the 7-digit VA FileMan message creation date. For example:

|                                     |                                     |
|-------------------------------------|-------------------------------------|
| MailMan 7.1 Remote Message ID (Old) | MailMan 8.0 Remote Message ID (New) |
| 34561234@FORUM.VA.GOV               | 34561234.3020803@FORUM.VA.GOV       |

#### Enhanced Routines

The ^XMC\*, ^XMR\*, ^XMS\* suite of routines, which are responsible for scheduling, transmitting to, and receiving messages from remote sites, have been completely overhauled to make them easier to understand and easier to maintain.

#### Improved Name Field Display

MailMan will no longer display user names by taking them directly from the .01 field of the NEW PERSON file (#200). The Name Standardization \$\$NAMEFMT^XLFNAME API is used instead. Thus, the names of people whose last names, for example, contain periods, apostrophes, or spaces, are properly displayed. For example:

|                                      |                                      |
|--------------------------------------|--------------------------------------|
| MailMan 7.1 Name Field Display (Old) | MailMan 8.0 Name Field Display (New) |
| STIVES                               | ST. IVES                             |
| OMALLEY                              | O'MALLEY                             |
| VANDYKE                              | VAN DYKE                             |

#### Broadcast Messages with Responses

Messages with responses may no longer be forwarded to broadcast to all users. Such messages may have important information in the responses, and as we all know, responses are not auto-forwarded to remote sites for users with auto-forward addresses. Users who attempt to broadcast messages with responses will be encouraged to copy the message and its responses into a new message, which can be broadcast.

#### Message Line Restriction Override

Incoming PackMan and KIDS messages are no longer subject to the restriction of the NETWORK - MAX LINES RECEIVE field (#8.31) in the MAILMAN SITE PARAMETERS file (#4.3). However, other kinds of messages continue to be subject to that restriction.

#### Requeued Task Bug Fix

If a task transmitting messages to another site fails and has to be requeued, it really is requeued. Before, that was not true. Previously, the failing task queued up a new task to take its place, and then the failing task stopped.

## Menu Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan is accessed from three sets of menus:

- XMMGR—Manage MailMan Menu
- XMNET—Network Management Menu
- XMUSER—MailMan Menu (i.e., user interface)

### XMMGR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Manage MailMan menu \[XMMGR\] is the main MailMan system manger menu. It includes options and utilities that are useful for system management. The options for maintaining the local mail system are contained here.

|                                                   |                                                                                                                                         |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/031.png) | REF: The Manage MailMan menu \[XMMGR\] and its subordinate options are discussed in depth in the topics that follow in this manual. |

### XMNET

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Network Management menu \[XMNET\] is the main MailMan network management menu. It contains options that are used for managing the network-side of MailMan. While the local system requires only some initial setup, the network-side *must* be periodically monitored. The options under the XMNET menu for displaying the queues in various fashions are useful for this purpose. The MailMan network sometimes needs to be flushed. Options for polling and queuing are provided for this purpose. Sometimes, non-delivery of network mail requires investigation. The options for testing a network device and playing scripts are useful in these instances.

|                                                   |                                                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/032.png) | REF: The Network Management menu \[XMNET\] and its subordinate options are discussed in depth in the *MailMan Network Reference Guide*. |

### XMUSER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan Menu \[XMUSER\] is the main MailMan user menu. It includes the commonly used functions of MailMan. It also contains some very powerful tools for the individual using MailMan. The most commonly used functions are at the top of the hierarchical structure. Help features are contained in a separate submenu, as are the tools. XMUSER can be used independently and can be installed on menus of other software applications for distribution.

|                                                   |                                                                                                                      |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/033.png) | REF: The MailMan Menu \[XMUSER\] and its subordinate options are discussed in depth in the *MailMan User Guide*. |

### Manage MailMan \[XMMGR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Manage MailMan menu \[XMMGR\] is the main MailMan system manger menu. It contains options that allow the system manager to fully implement and manage the MailMan software by manipulating the BULLETIN (#3.6), MAILBOX file (#3.7), MAIL GROUP (#3.8), and MESSAGE (#3.9) files. This menu contains the following options:

<span id="_Toc323122249" class="anchor"></span>Figure 25. Manage MailMan \[XMMGR\] menu options

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

|                                                   |                                                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/034.png) | REF: The Network Management menu \[XMNET\] and its subordinate options are discussed in depth in the *MailMan Network Reference Guide*. |

#### Check MailMan Files for Errors \[XMUT-CHKFIL\]

The Check MailMan Files for Errors option \[XMUT-CHKFIL\] checks for and corrects errors in the MAILBOX (#3.7) and MESSAGE (#3.9) files. It checks important fields and cross references.

It is recommended that this option be run monthly or every few months, or whenever there seems to be a database problem.

It produces a report of the errors detected, and what, if anything, it did to fix them. If it did not fix the errors, it tells you what you can do to fix them.

Although the system will not fail because of errors detected, users may inquire about the problems they experience. This utility allows you to detect any errors first and correct them before anyone else encounters an error.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-systems-management-guide/035.png)</td>
<td><p><strong>NOTE:</strong> This option is located under the Manage MailMan menu [XMMGR].</p>
<p>This option is locked with the XUPROG security key.</p></td>
</tr>
</tbody>
</table>

#### Create a Mailbox for a user \[XMMGR-NEW-MAIL-BOX\]

The Create a Mailbox for a user option \[XMMGR-NEW-MAIL-BOX\] is only meant to be used on systems where Kernel 6.0 or higher is *not* running or when a repair *must* be made to the MAILBOX file (#3.7). Since a mailbox is created for each new or reinstated user through the Kernel software, this routine only needs to be run when an error occurs while setting up the user or if there is a file degradation problem. Using this option for a user whose mailbox is wholly or partially set up will *not* cause data to be lost. A mailbox can be created or repaired using this option.

|                                                   |                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/036.png) | NOTE: This option is located under the Manage MailMan menu \[XMMGR\]. |

#### Disk Space Management \[XMMGR-DISK-SPACE-MANAGEMENT\]

The Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\] contains options for managing disk space. All reports are 80 columns wide. This menu contains the following options:

<span id="_Toc147217303" class="anchor"></span>Figure 26. Disk Space Management menu options

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

|                                                   |                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/037.png) | NOTE: This option is located under the Manage MailMan menu \[XMMGR\]. |

#### AI x-Ref Purge of Received Network Messages \[XMMGR-PURGE-AI‑XREF\]

The AI x-Ref Purge of Received Network Messages option \[XMMGR-PURGE-AI‑XREF\] maintains the "AI" cross-reference of mail messages. This is the cross-reference of messages received across the network and it prevents duplicate messages from being received again. The default number of days kept is 730 (2 years is the number of days messages can exist before being purged on FORUM).

|                                                   |                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/038.png) | NOTE: This option is located under the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. |

#### Ask users with many messages to do maintenance \[XMMGR-DISK-MANY-MESSAGE-MAINT\]

The Ask users with many messages to do maintenance option \[XMMGR-DISK-MANY-MESSAGE-MAINT\] sends messages asking users with too many messages to clean out their mailboxes.

|                                                   |                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/039.png) | NOTE: This option is located under the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. |

#### Clean out waste baskets \[XMCLEAN\]

The Clean out waste baskets option \[XMCLEAN\] deletes all messages in users' WASTE baskets in the MAILBOX file (#3.7). It does *not* delete the messages in the MESSAGE file (#3.9). It is recommended that this option be scheduled to run daily, immediately before the XMAUTOPURGE option.

|                                                   |                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/040.png) | NOTE: This option is located under the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. |

#### IN Basket Purge \[XMMGR-IN-BASKET-PURGE\]

The IN Basket Purge option \[XMMGR-IN-BASKET-PURGE\] purges the "IN" mail basket.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-systems-management-guide/041.png)</td>
<td><p><strong>NOTE:</strong> This option is located under the Disk Space Management menu [XMMGR-DISK-SPACE-MANAGEMENT].</p>
<p>This option can be run via TaskMan.</p></td>
</tr>
</tbody>
</table>

Purging messages in the "IN" mail basket occurs in two steps:

1.  A message is first sent to users notifying them that certain messages may be purged. This message includes the following information:
- List of messages to be purged in Step \#2.
- List of actions that will prevent the purging of the listed messages.
- Number of days before the listed messages will be purged unless action is taken on a message-by-message basis.
- Messages listed will *not* have been referenced for 30 days or the number of days indicated in the MESSAGE RETENTION DAYS field in the MAILMAN SITE PARAMETERS file (#4.3), if it is *not* null.
14. Messages listed in the message from Step \#1 will be purged (*not* less than 30 days later) unless the user has taken any of the following actions:
- Saved messages into a basket other than the "IN" basket.
- Referenced the messages (read or printed).
- Marked the messages as NEW.

#### Large Message Report \[XMMGR-LARGE-MESSAGE-REPORT\]

The Large Message Report option \[XMMGR-LARGE-MESSAGE-REPORT\] generates a list of messages that are:

- Longer than a specified number of lines (see Field \#8.14 in the MAILMAN SITE PARAMETERS file \[#4.3\]).
- Messages that have no owner or only one owner.
- Messages that have no text or subject.

|                                                   |                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/042.png) | NOTE: This option is located under the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. |

#### Message Statistics \[XMSTAT\]

The Message Statistics option \[XMSTAT\] is an interactive option that displays information about past purges. It displays the following information:

- Types and results of the last 20 purges of the MESSAGE file (#3.9). It provides the following details:
- If the purge was an unreferenced message purge (XMPURGE or XMAUTOPURGE options) or a date purge (XMPURGE-BY-DATE option)
- When it started
- When it ended
- How long it took
- How many messages were purged
- How many were left
- Information about each user in the MAILBOX file (#3.7). It provides the following details:
- How many messages they have in their mailboxes
- When the user last logged on
- When the user last used MailMan

|                                                   |                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/043.png) | NOTE: This option is located under the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. |

#### Purge a message \[XMMGR-PURGE-MESSAGE\]

The Purge a message option \[XMMGR-PURGE-MESSAGE\] removes a message from users' mail baskets and deletes it, along with any responses chained to it.

|                                                   |                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/044.png) | NOTE: This option is located under the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. |

#### Purge Messages by Origination Date \[XMPURGE-BY-DATE\]

The Purge Messages by Origination Date option \[XMPURGE-BY-DATE\] (a.k.a. date purge) removes messages from users' mail baskets and deletes them, along with any responses chained to them. It will do this for a range of messages based upon user input. The user enters the range of internal message numbers to be processed and the date against which they will be checked.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-systems-management-guide/045.png)</td>
<td><p><strong>NOTE:</strong> This option is located under the Disk Space Management menu [XMMGR-DISK-SPACE-MANAGEMENT].</p>
<p>This option is locked with the XMMGR security key.</p></td>
</tr>
</tbody>
</table>

The XMPURGE-BY-DATE option deletes all (see note below) messages originating before a cutoff date. It deletes those messages from users' mailboxes, and then deletes them from the MESSAGE file (#3.9), along with any responses chained to them.

|                                                   |                                                                                                                                                                                                                                       |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/046.png) | NOTE: Any messages in SHARED,MAIL's mailbox and messages in the Postmaster's remote Transmit queues and Server baskets (including released patch messages on FORUM) are exempt from the date purge (i.e., XMPURGE-BY-DATE option. |

This option is very flexible and provides the following (optional) capabilities:

- Run interactively or scheduled to run on a recurring basis
- Control cutoff date
- Send a warning bulletin to warn users of the purge ahead of time.
- Produce a report to show how many messages and responses it deleted.

Interactive

When the option is run interactively, the option does the following:

1.  Asks for the cutoff date. The default is based on the DATE PURGE CUTOFF DAYS field (#10.03) in the MAILMAN SITE PARAMETERS File (#4.3). If that field is null, it defaults to 730 days (2 years) in the past.
2.  Asks whether to run the option in Test mode. In Test mode, the option does not purge any messages, it just reports how many and which messages would have been purged.
3.  Asks for the output device on which to print the report. The purge and report can be queued here to run later.
15. If it's queued more than three days in the future, the option immediately broadcasts the XM DATE PURGE WARNING bulletin to all users to notify them of the upcoming purge and give them a chance to save off old messages beforehand.
16. If it's queued less than three days in the future, or is not queued, no bulletin is sent.

Scheduled

When the option is scheduled, the option does the following:

1.  Runs at the scheduled time, as specified by the QUEUED TO RUN AT WHAT TIME field (#2) of the OPTION SCHEDULING file (#19.2).
2.  Scheduled to run repeatedly, if the RESCHEDULING FREQUENCY field (#6) in the OPTION SCHEDULING file (#19.2) is set.
3.  Uses the DATE PURGE CUTOFF DAYS field (#10.03) in the MAILMAN SITE PARAMETERS File (#4.3), or the default of 730 days if it's empty, to calculate the cutoff date.
4.  Does not run in Test mode.
5.  Run time varies based on the value of the DATE PURGE GRACE PERIOD field (#10.04) in the MAILMAN SITE PARAMETERS File (#4.3):
- Empty/Null—Runs at the time for which the option is scheduled.
- Value Exists—Runs at the scheduled time the option only broadcasts the XM DATE PURGE WARNING bulletin to all users and queues a second task to perform the date purge GRACE PERIOD number of days later.
6.  Report printing depends on the value of the DEVICE FOR QUEUED JOB OUTPUT field (#3) in the OPTION SCHEDULING file (#19.2):
- Empty/Null—The purge runs without printing a report.
- Value Exists—The purge runs and prints the report on the selected device.

The following is the XM DATE PURGE WARNING bulletin:

<span id="_Toc147217304" class="anchor"></span>Figure 27. XM DATE PURGE WARNING bulletin

NAME: XM DATE PURGE WARNING SUBJECT: Date Purge Scheduled for \|1\|

PRIORITY?: YES

MESSAGE: Attention! On \|1\|, all\* messages (and their responses) sent on

or before \|2\| will be deleted from the system. They will be gone forever.

You can find out if this will affect any messages in your mailbox and take

appropriate measures.

From the main MailMan menu, respond to the prompts as follows:

Select MailMan Menu Option: Query/Search for Messages

=

Select message search method: M Search my Mailbox by multiple criteria

=

Select search action: Enter 'Subject contains' string// DB Enter 'Message

sent on or before' date ==

Message sent on or before: \|2\|

\|3\|

This search will find all of your messages which will be deleted.

\* Messages in SHARED,MAIL's mailbox, and messages in the POSTMASTER's remote transmit queues and server baskets (includes released patches on FORUM) are exempt from the purge.

DESCRIPTION: This is the warning bulletin that is broadcast to all users whenever option XMPURGE-BY-DATE is used to purge messages older than a certain date. See that option for more information.

PARAMETER: 1

DESCRIPTION: The date that the date purge will run.

PARAMETER: 2

DESCRIPTION: All messages this date and older will be purged.

PARAMETER: 3

DESCRIPTION: A line of '=' as long as parameter 2

#### Purge Unreferenced Messages \[XMPURGE\]

The Purge Unreferenced Messages option \[XMPURGE\] behaves as follows depending on how it is run:

- Scheduled—This option, if scheduled, does exactly what the XMAUTOPURGE option does, and then stops.
- Interactive—This option, if run interactively, does exactly what the XMAUTOPURGE option does, and then it does exactly what the XMSTAT option does, and then it stops.

|                                                   |                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/047.png) | NOTE: This option is located under the Disk Space Management menu \[XMMGR-DISK-SPACE-MANAGEMENT\]. |

|                                                   |                                                 |
|---------------------------------------------------|-------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/048.png) | CAUTION: You should *not* schedule this option. |

#### Recover Messages into User's IN Basket \[XMUT-REC-MENU\]

The Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\] contains options for recovering messages for a user. It will recover all messages a user has ever received as long as the user has not terminated from them. This menu contains the following options:

<span id="_Toc147217305" class="anchor"></span>Figure 28. Recover Messages into User's IN Basket menu options

Select Recover Messages into User's IN Basket Option:

DEL Delete Found Messages from Found Messages List \[XMUT-REC-DELETE\]

DRM Deliver Found Messages into User's IN Basket \[XMUT-REC-DELIVER\]

FRM Find Messages for User \[XMUT-REC-FIND\]

LRM List Messages Found \[XMUT-REC-RPT\]

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-systems-management-guide/049.png)</td>
<td><p><strong>NOTE:</strong> This option is located under the Disk Space Management menu [XMMGR-DISK-SPACE-MANAGEMENT].</p>
<p>This option is locked with the XUPROG security key.</p></td>
</tr>
</tbody>
</table>

#### Delete Found Messages from Found Messages List \[XMUT-REC‑DELETE\]

The Delete Found Messages from Found Messages List option \[XMUT-REC‑DELETE\] deletes the temporary storage of a list of messages found when the Find Messages for User option is used by a user.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/050.png) | NOTE: This option is located under the Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\]. |

#### Deliver Found Messages into User's IN Basket \[XMUT-REC‑DELIVER\]

The Deliver Found Messages into User's IN Basket option \[XMUT-REC‑DELIVER\] delivers messages found with the Find Messages for User option \[XMUT-REC-FIND\]. The messages found will be placed into the user's "IN" basket as long as they are not already in another basket.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/051.png) | NOTE: This option is located under the Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\]. |

#### Find Messages for User \[XMUT-REC-FIND\]

The Find Messages for User option \[XMUT-REC-FIND\] finds all messages that a user has ever had and has not terminated from. This list of messages can be used as input into two other processes:

- Deliver Found Messages into User's IN Basket option \[XMUT-REC‑DELIVER\]
- List Messages Found option \[XMUT-REC-RPT\]

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/052.png) | NOTE: This option is located under the Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\]. |

#### List Messages Found \[XMUT-REC-RPT\]

The List Messages Found option \[XMUT-REC-RPT\] lists messages found for users with the Find Messages for User menu option.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/053.png) | NOTE: This option is located under the Recover Messages into User's IN Basket menu \[XMUT-REC-MENU\]. |

#### Group/Distribution Management \[XMMGR-GROUP-MAINTENANCE\]

The Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\] contains options to edit bulletins and manage distribution lists and mail groups. This menu contains the following options:

<span id="_Toc147217306" class="anchor"></span>Figure 29. Group/Distribution Management menu options

Select Group/Distribution Management Option:

Bulletin edit \[XMEDITBUL\]

Edit Distribution List \[XMEDITDIST\]

Enroll in (or Disenroll from) a Mail Group \[XMENROLL\]

Mail Group Coordinator's Edit \[XMMGR-MAIL-GRP-COORDINATOR\]

Mail Group Coordinator's Edit W/Remotes \[XMMGR-MAIL-GRP-COORD-W/REMOTES\]

Mail Group Edit \[XMEDITMG\]

|                                                   |                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/054.png) | NOTE: This option is located under the Manage MailMan menu \[XMMGR\]. |

#### Bulletin edit \[XMEDITBUL\]

The Bulletin edit option \[XMEDITBUL\] allows management to enter/edit a MailMan bulletin, change the routing information, and document a bulletin.

|                                                   |                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/055.png) | NOTE: This option is located under the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. |

#### Edit Distribution List \[XMEDITDIST\]

The Edit Distribution List option \[XMEDITDIST\] is used to edit a distribution list. The name of a Distribution List is the name of a position such as Postmaster or group name such as G.IRM. A list primarily contains a set of domain names that are concatenated to the distribution list name to create additional recipients for a message. A recipient with the same name as the list name is presumed to exist at each different domain.

If the name is G.SUPPORT, and the domains are FORUM.VA.GOV & EXAMPLEVAMC.VA.GOV, the message will be sent to the following groups:

- G.SUPPORT@FORUM.VA.GOV
- G.SUPPORT@EXAMPLEVAMC.VA.GOV

A distribution list can be in more than one mail group. Each mail group can include more than one distribution list.

|                                                   |                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/056.png) | NOTE: This option is located under the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. |

#### Enroll in (or Disenroll from) a Mail Group \[XMENROLL\]

The Enroll in (or Disenroll from) a Mail Group option \[XMENROLL\] allows a MailMan user to enroll in (join) or disenroll from a mail group when the group allows self-enrollment (i.e., the "SELF ENROLLMENT ALLOWED?" flag is set to "Yes"). If the user is already a member of a group, then this option allows the user to leave the group.

If a mail group does *not* allow self-enrollment (i.e., MailMan indicates that "...Self Enrollment Not Allowed." after a mail group name) and the DROP OUT OF RESTRICTED GROUP field (#22) in the MAILMAN SITE PARAMETERS file (#4.3) is set to "No," users *must* contact the Mail Group Coordinator or Organizer for that particular mail group and ask either to be enrolled in or disenrolled from the mail group.

|                                                   |                                                                                                                                                                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/057.png) | REF: For more information on the Mail Group Coordinator, Organizer, and general mail group information, please refer to the "How to Obtain Mail Group Information" topic in Chapter 12, "Online Help/Information," in the *MailMan User Guide*. |

The DROP OUT OF RESTRICTED GROUP field (#22) in the MAILMAN SITE PARAMETERS file (#4.3) is a site-configurable parameter and is used to allow users to drop out (disenroll) of non-self-enrolling mail groups:

- YES—Users are warned that this is a non-self-enrolling group, and that they will *not* be allowed to rejoin later; users will be asked to re-confirm the decision to drop out.
- NO (default)—Users will have to contact IRM or the mail group Coordinator or Organizer to ask to be dropped.

|                                                   |                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/058.png) | NOTE: This option is located under the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. |

#### Mail Group Coordinator's Edit \[XMMGR-MAIL-GRP-COORDINATOR\]

The Mail Group Coordinator's Edit option \[XMMGR-MAIL-GRP-COORDINATOR\] allows mail group coordinators to edit the membership of mail groups that he is the coordinator of (and no other). It does not allow editing of remote recipients, but limits the responsibility for problems of delivering to incorrect addresses.

|                                                   |                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/059.png) | NOTE: This option is located under the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. |

#### Mail Group Coordinator's Edit W/Remotes \[XMMGR-MAIL-GRP-COORD-W/REMOTES\]

The Mail Group Coordinator's Edit W/Remotes option \[XMMGR-MAIL-GRP-COORD-W/REMOTES\] allows mail group coordinators to edit the membership of mail groups that he/she is the coordinator of (and no other). It allows editing of local and remote recipients.

|                                                   |                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/060.png) | NOTE: This option is located under the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. |

#### Mail Group Edit \[XMEDITMG\]

Use the Mail Group Edit option \[XMEDITMG\] to edit all parameters in the MAIL GROUP file (#3.8).

|                                                   |                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/061.png) | NOTE: This option is located under the Group/Distribution Management menu \[XMMGR-GROUP-MAINTENANCE\]. |

#### Local Delivery Management \[XMMGR-MESSAGE-DELIVERY-MGT\]

The Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\] contains options for the background filer. All reports are 132 columns wide. This menu contains the following options:

<span id="_Toc147217307" class="anchor"></span>Figure 30. Local Delivery Management \[XMMGR-MESSAGE-DELIVERY-MGT\] menu options

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

|                                                   |                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/062.png) | NOTE: This option is located under the Manage MailMan menu \[XMMGR\]. |

#### Active Users/Deliveries Report \[XMMGR-BKFILER-ACT\]

The Active Users/Deliveries Report option \[XMMGR-BKFILER-ACT\] generates a report that lists in half-hour intervals active users and message deliveries made from previously filed information.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/063.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### CHECK background filer \[XMMGR-CHECK-BACKGROUND-FILER\]

The CHECK background filer option (XMAD) \[XMMGR-CHECK-BACKGROUND-FILER\] tells you if the background filer is running and tells how many recipients need delivery for each of the messages/responses in the queue.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/064.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### Compile Response Time Statistic \[XMMGR-RESPONSE-TIME-COMPILER\]

Use the Compile Response Time Statistic option \[XMMGR-RESPONSE-TIME-COMPILER\] as a background job, scheduled daily to collect statistics on the previous day's response time. The data is put into the MESSAGE DELIVERY STATS file (#4.2998). It will then "kill off" associated %ZTRL global nodes.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/065.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### Deliveries by Group \[XMMGR-BKFILER-GROUP\]

The Deliveries by Group option \[XMMGR-BKFILER-GROUP\] produces a list of deliveries made for each distinct delivery queue, in half-hour intervals.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/066.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### Delivery Queue Statistics Collection \[XMMGR-DELIVERY-STATS-COLL\]

The Delivery Queue Statistics Collection option \[XMMGR-DELIVERY-STATS-COLL\] collects delivery queue statistics.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/067.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### Edit numbers to Normalize Reports \[XMMGR-BKFILER-EDIT-NORMALIZED\]

The Edit numbers to Normalize Reports option \[XMMGR-BKFILER-EDIT-NORMALIZED\] option allows the user to customize the normalized report.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/068.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### Graphics Download to Graphics (TAB Separators) \[XMMGR- BKFILER-TABBED-STATS\]

The Graphics Download to Graphics (TAB Separators) option \[XMMGR- BKFILER-TABBED-STATS\] can be used to capture a report and then use the captured file in a graphics or spreadsheet software (e.g., Microsoft Excel). The data has TABs between the fields as delimiters.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/069.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### Log Response Time Toggler \[XMMGR-RESPONSE-TIME-TOGGLER\]

The Log Response Time Toggler option \[ XMMGR-RESPONSE-TIME-TOGGLER\] will turn on the Kernel system parameters for response time logging, a little after each half-hour.

It will then schedule another task to turn off the Kernel system parameters for response time logging, unless the time is between 4:00 p.m. and 8:00 a.m. During these hours, response time logging will remain on unless site management interferes, by canceling the tasks associated with this phenomenon and edits the Log Response Time field for the appropriate Volume Set to be "off".

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/070.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### Mail Delivery Statistics Report \[XMMGR-BKFILER-STAT\]

Use the Mail Delivery Statistics Report option \[XMMGR-BKFILER-STAT\] to generate reports showing a list of active users, queue waits, average response time, number of lines displayed to users, etc., in half-hour intervals.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/071.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### New Messages and Logon Statistics \[XMMGR-NEWMESS/LOGON-STATS\]

The New Messages and Logon Statistics option \[XMMGR-NEWMESS/LOGON-STATS\] prints the number of new messages created and logons with logon minutes for a specified time period.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/072.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### START background filer \[XMMGR-START-BACKGROUND-FILER\]

The START background filer option (XMAD) \[XMMGR-START-BACKGROUND-FILER\] reverses the action of the STOP background filer \[XMMGR-STOP-BACKGROUND-FILER\] has been run. It will also restart the background filer if it disappears from the system status report. In order for this option to be effective, the TaskMan (ZTM) *must* be running.

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/073.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### STOP background filer \[XMMGR-START-BACKGROUND-FILER\]

Use the STOP background filer option (XMAD) \[XMMGR-STOP-BACKGROUND-FILER\] to stop the background filer gently at the end of a delivery before it starts to deliver any further messages. This only stops local delivery operations. All local mail delivery will stop until the START background filer option \[XMMGR-START-BACKGROUND-FILER\] is run.

|                                                   |                                                    |
|---------------------------------------------------|----------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/074.png) | NOTE: Stops delivery of local mail gracefully, |

|                                                   |                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/075.png) | NOTE: This option is located under the Local Delivery Management menu \[XMMGR-MESSAGE-DELIVERY-MGT\]. |

#### MailMan Site Parameters \[XMKSP\]

The MailMan Site Parameters option \[XMKSP\] allows system managers to edit the fields in the MAILMAN SITE PARAMETERS file (#4.3) that do *not* have to do with christening.

|                                                   |                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/076.png) | NOTE: This option is located under the Manage MailMan menu \[XMMGR\]. |

To christen a domain, use the Christen a domain option located under the Network Management menu \[XMNET\].The Christen a domain option will also allow you to change fields set during the original christening, if they are set incorrectly. You can use VA FileMan to edit the TRANSMISSION SCRIPT File (#4.6), if the scripts for REDACTED or the Mini engine need to be changed.

|                                                   |                                                                                                                             |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/077.png) | REF: The options found on the Network Management menu \[XMNET\] are described in the *MailMan Network Reference Guide*. |

#### Network Management \[XMNET\]

The Network Management menu \[XMNET\] is the main MailMan network management menu. It contains all of the options that are used for managing the network side of MailMan. This menu contains the following options:

<span id="_Toc147217308" class="anchor"></span>Figure 31. Network Management menu options

Select Network Management Option:

Christen a domain \[XMCHRIS\]

Compare Domains in System Against Released List \[XMQDOMAINS\]

Network Help \[XMNETHELP\]

Queue Management ... \[XMNET-QUEUE-MANAGEMENT\]

Site Parameters \[XMSITE\]

Transmission Management ... \[XMNET-TRANSMISSION-MANAGEMENT\]

|                                                   |                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/078.png) | NOTE: This option is located under the Manage MailMan menu \[XMMGR\]. |

|                                                   |                                                                                                                             |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/079.png) | REF: The options found on the Network Management menu \[XMNET\] are described in the *MailMan Network Reference Guide*. |

#### New Features for Managing MailMan \[XMMGR-HELP\]

The New Features for Managing MailMan option \[XMMGR-HELP\] offers help for site management.

|                                                   |                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/080.png) | NOTE: This option is located under the Manage MailMan menu \[XMMGR\]. |

#### Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]

The Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\] allows the site manager to manage the remote MailLink Directory, by loading the VACO directory, WANG/NOAVA directory and remote domain user directories into the REMOTE USER DIRECTORY file, ^XMD(4.2997). This menu contains the following options:

<span id="_Toc147217309" class="anchor"></span>Figure 32. Remote MailLink Directory Menu options

Select Remote MailLink Directory Menu Option:

Enter/Edit Directory Request Flags by Group \[XMMGR-DIRECTORY-EDITGRP\]

Enter/Edit Remote User \[XMEDIT-REMOTE-USER\]

Group eMail Directory Request \[XMMGR-DIRECTORY-GROUP\]

List eMail Directory Request by Groups \[XMMGR-DIRECTORY-LISTGRP\]

Load Remote VACO (Wang/Noava) Directory \[XMMGR-DIRECTORY-VACO\]

Remote Directory from all Domains \[XMMGR-DIRECTORY-ALL\]

Request Mail Directory From a Single Domain Server

\[XMMGR-DIRECTORY-SINGLE\]

|                                                   |                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/081.png) | NOTE: This option is located under the Manage MailMan menu \[XMMGR\]. |

#### Enter/Edit Directory Request Flags by Group \[XMMGR-DIRECTORY-EDITGRP\]

The Enter/Edit Directory Request Flags by Group option \[XMMGR-DIRECTORY-EDITGRP\] allows site management to control groups of domains from which directories are requested.

|                                                   |                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/082.png) | NOTE: This option is located under the Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]. |

#### Enter/Edit Remote User \[XMEDIT-REMOTE-USER\]

The Enter/Edit Remote User option \[XMEDIT-REMOTE-USER\] allows a single person's remote address to be put into the Remote User Directory so that messages can be automatically addressed to him.

|                                                   |                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/083.png) | NOTE: This option is located under the Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]. |

#### Group eMail Directory Request \[XMMGR-DIRECTORY-GROUP\]

The Group eMail Directory Request option \[XMMGR-DIRECTORY-GROUP\] allows site management to request directories from all the domains in a group of domains as defined in the Enter/Edit Directory Request Flags by Group option \[XMMGR-DIRECTORY-EDITGRP\].

|                                                   |                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/084.png) | NOTE: This option is located under the Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]. |

#### List eMail Directory Request by Groups \[XMMGR-DIRECTORY-LISTGRP\]

List eMail Directory Request by Groups option \[XMMGR-DIRECTORY-LISTGRP\] lists groups created by the Enter/Edit Directory Request Flags by Group option \[XMMGR-DIRECTORY-EDITGRP\].

|                                                   |                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/085.png) | NOTE: This option is located under the Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]. |

#### Load Remote VACO (Wang/Noava) Directory \[XMMGR-DIRECTORY-VACO\]

The Load Remote VACO (Wang/Noava) Directory option \[XMMGR-DIRECTORY-VACO\] loads a file from the Host File Server. The user has the choice of whether to run this task interactively or to schedule a batch job to update the MailLink directory.

|                                                   |                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/086.png) | NOTE: This option is located under the Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]. |

#### Remote Directory from all Domains \[XMMGR-DIRECTORY-ALL\]

The Remote Directory from all Domains option \[XMMGR-DIRECTORY-ALL\] schedules tasks to run in the background to update the MailLink directory ^XMD(4.2997).

|                                                   |                                                                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/087.png) | CAUTION: Use this option cautiously, because it sends requests to all the domains for soliciting remote user directories. |

|                                                   |                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/088.png) | NOTE: This option is located under the Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]. |

#### Request Mail Directory From a Single Domain Server \[XMMGR-DIRECTORY-SINGLE\]

The Request Mail Directory From a Single Domain Server option \[XMMGR-DIRECTORY-SINGLE\] schedules a task to run in the background to update the MailLink directory ^XMD(4.2997) from a single domain server.

|                                                   |                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/089.png) | NOTE: This option is located under the Remote MailLink Directory Menu \[XMMGR-DIRECTORY-MAIN\]. |

# Troubleshooting MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem: User has No Mailbox!

There are a number of symptoms that are caused by the simple fact that a user has no mailbox. They are not always intuitively evident so here are a few examples:

- Mail cannot be addressed to a user.
- A user received no responses to messages that he was a recipient of or originally sent.
- A user gets a message when entering a MailMan option that states that mail will not be delivered to him because he has no mailbox.
- An \<UNDEF\> error occurs when the MAILBOX file (#3.7) is accessed.
- The background filer will not deliver messages or messages do not seem to be delivered (check Mailboxes of all message recipients).

In all cases, the problem is easily remedied. Use the Create a Mailbox for a user option \[XMMGR-NEW-MAIL-BOX\] to create or repair a user's mailbox. The mailbox is an entry in the MAILBOX file (#3.7) that contains a pointer to the NEW PERSON file (#200) where introductory text, some mail system parameters for an individual's mail basket and other information are stored.

|                                                   |                                                                                                                                                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/090.png) | REF: For more information on the Create a Mailbox for a user option \[XMMGR-NEW-MAIL-BOX\], see Section 2.3.4.1.2 "Create a Mailbox for a user \[XMMGR-NEW-MAIL-BOX\]," topic in this manual. |

# DNS-Aware MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan 8.0 software includes Domain Name Service (DNS) functionality.

In the current environment, Internet Protocol (IP) addresses within the VA are in constant flux. Static mappings in VistA files have made IP changes difficult, since the changes had to be manually implemented at each site. VistA has a tool that can resolve domain names to IP addresses via DNS.

DNS is an Internet standard (RFC 1034), a well-established method for mapping computer names to Internet Protocol (IP) addresses. The national VHA DNS system is already in place, providing name resolution support for services such as Web browsers. It is supported and maintained by the national VHA OI DNS Administrators.

Advantages of DNS:

- DNS removes the need to change static mappings by hand.
- Sites only need to update one DNS Server to get the change out to other sites, because a change in the DNS will automatically be communicated to all DNS Servers.
- DNS handles address changes effortlessly. Updates to IP address mappings can be made much more easily.
- DNS provides quick universal access to changed and new addresses.
- DNS offers dynamic translation of domain names to IP addresses.

|                                                   |                                                                                                                                                                                               |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/091.png) | REF: For more information on DNS, please refer to the *National DNS Support in VistA* document at the following VA Intranet website: http://vista.med.va.gov/iss/docs/dns/DNSandVista.asp |

DNS-Aware MailMan 8.0 enhances support and saves person-hours as follows:

- Creates automatic replication of IP address changes to every VistA MailMan system as a result of only one central database edit (i.e., performs DNS lookups). This architecture is currently used to update both Intranet and Internet addresses throughout the world within a matter of hours.
- Enhancements save person-hours for the IRM staff at every VA site, since they will no longer have to manually maintain the IP address in the DOMAIN file (#4.2).

DNS-Aware functionality available with MailMan 8.0 software uses the Kernel DNS Lookup API (MAIL^XLFNSLK) provided in Kernel Patch XU\*8.0\*142. This M-based Kernel API calls a DNS to convert the domain name into an IP address. The IP address of the DNS is in the DNS IP field (#51) in the KERNEL SYSTEM PARAMETERS file (#8989.3). This call is a Supported IA.

|                                                   |                                                                                                                                                                                           |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/092.png) | REF: For more information on this Kernel API, please refer to the MAIL^XLFNSLK Web page at the following VA Intranet website : http://vista.med.va.gov/kernel/apis/mail^xlfnslk.shtml |

# PackMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PackMan allows messages to be stored and data, such as software globals and routines, to be transported. It *cannot* be used unless the user holds the XUPROGMODE security key. In addition, PackMan messages can be secured, in which case, the user needs to know the SCRAMBLE HINT.

PackMan includes the ability for users to add and edit description text into a PackMan message before loading routine and global data using the Load PackMan Message option.

## PackMan Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| PackMan Menu Function       | Description                                                                                                               |
|-----------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ROUTINE LOAD                | Loads routines into a message.                                                                                            |
| GLOBAL LOAD                 | Loads global information into a message.                                                                                  |
| PACKAGE LOAD                | Loads a software package as defined in the PACKAGE file (#9.4).                                                           |
| SUMMARIZE MESSAGE           | Summarizes the message content.                                                                                           |
| PRINT MESSAGE               | Prints message, but recognizes content and sets it into a more readable format than the standard message print.           |
| INSTALL/CHECK MESSAGE       | Checks the message for changes prior to installation.                                                                     |
| INSTALL SELECTED ROUTINE(S) | Installs the routines and globals. Creates a backup message of any routines that will be over-written, if you request it. |
| TEXT PRINT/DISPLAY          | Prints or displays the text.                                                                                              |
| COMPARE                     | Compares routines in a PackMan message to those that are currently in use.                                                |

## Loading Routines into PackMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routines can be loaded into a PackMan message. Once the routines are in a message, the print function in PackMan does a good job of formatting the output.

## Loading Global Data into a PackMan Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan allows global data to be loaded into a message and saved there to be transported via Network mail. The data *must* conform to VistA standards in order to insure that this option will work properly. When the global data is loaded in, the address is put onto one line and the data for that address onto a second line. Global data can be secured, but not scrambled. It can be reinstalled. Do not expect MailMan to be able to make a back-up message properly when installing a global.

### Compare PackMan Message Routines against those Installed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Compare option is available as a PackMan option. This option will check the data in the PackMan message against the routines, globals, and data dictionaries on disk and list all differences.

## Installing a PackMan Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installing a message will replace the data on disk, but a backup message can be created before the installation takes place. Automatic backup is prompted for before installation is allowed.

If a message is secured, a security check takes place at the installation of the message. The message is checked against previously calculated sums and any changes will be considered as non-installable.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/093.png) | NOTE: If a message is installed that contains certain XM\* routines (among them XMP2 and XMA1) a "clobber error," "cannot return to source code," or similar error will result as you are writing over the routine you are installing. This is quite normal. It happens after the routine is written over. If the routine is at the beginning of the PackMan message, a consecutive install will proceed without the error, installing the rest of the parts of the message. |

## Summarize PackMan Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PackMan option for displaying a summary of a PackMan message does just that. Software applications and their parts (e.g., routines, globals, and anything else that can be loaded) will be listed as being in the message when this option is chosen.

## Loading an Entire Software Package into a PackMan Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can load an entire software package into a PackMan message through MailMan. This is an option given to the creator of a set of INITS during a DIFROM. This is a somewhat complex option, but the programmer need only answer that he wants the set of information he is compiling via a DIFROM to be loaded into a message. He or she will then be prompted for a Subject for the message and asked whether or not to secure the message. In this way a message can be created, secured and sent as a part of a DIFROM and the creator need never invoke a separate MailMan process.

There are these advantages in storing a DIFROM directly into a message:

- The message can be sent over the network faster because it is shorter.
- The message can be secured.
- The security is checked at installation.
- The installation goes directly from the message into the INIT saving steps for the installer.
- The installer need never be in programming mode since the install does not require any direct mode code.

## Printing PackMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a special option for printing PackMan messages. This feature is particularly useful for routines that are reformatted so that the tags and lines of code are functionally aligned. The header of the PackMan printouts includes the following information:

- Subject
- Message number
- Who sent it
- When it was sent

## Editing PackMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/094.png) | CAUTION: Be very careful when editing these messages! It is important that you understand the reasoning for editing PackMan messages. It is particularly important since it is a mandatory requirement that verified patches released as PackMan messages include information from the patch as text in the message to facilitate patch installation. |

Editing PackMan messages allows you to create a message of global or routine data, and then edit it. It can be used to:

- Load up global data, and then change the global name.
- Load up global data and change every occurrence of a string.
- Load up routines and change every occurrence of a string (you can convert routines from one namespace to another).
- Add text explaining the name and purpose of the PackMan message.

|                                                   |                                                                                                                                                                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/095.png) | RECOMMENDATION: It is recommended that global data *not* be included in a PackMan message that is being distributed as a patch. This is because the facilities of PackMan that are used to check any edits of the message cannot detect many problems. |

|                                                   |                                                                                                                                                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/096.png) | CAUTION: Always test the installation of all patches after editing. Users can check that the edit probably did not affect the integrity of the parts of the PackMan message, however, an actual installation of the message is final proof. |

## Why Editing PackMan Messages Can Cause Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PackMan utilities depend on the format of the message to determine content. Special character strings that begin with \$ denote the beginning and ending points of sections of the message. The reason that \$s are used is that it is not possible for a line of M code to begin with the \$ character. All lines that do not begin with a tag *must* begin with a line-start character, which is always a control character or a space character. The \$ is not a valid tag. Therefore, any edit of a PackMan message that leaves lines beginning with a \$ character may cause a problem.

- All lines that begin with the \$ character have special format. If any one is changed, the integrity of the message is compromised.
- All routines and globals in the PackMan message have a special format. Inserting a line, or changing a character in the wrong place can create a situation in which the message will not be installable at all. Partial installation may occur, leaving a partially updated functionality in place. This could cause problems.

## Ways to Ensure Integrity of PackMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Create the PackMan Message, call it \#1 and edit it appropriately.
- Create the PackMan Message, call it \#2 with the same routines. \*\*Do not edit this message.
- Read Message \#1 and check for the following and compare it to Message \#2:
- No lines should have been added that have the \$ character as the first character. (Check questions against Message \#2.)
- All changes should have occurred after the first line of a message segment that begins with "\$TXT" and the second line of a message segment that begins "\$ROU". (Check questions against Message \#2.)
- Use the PackMan Compare Utility to check Message \#1 against the routines originally loaded. Differences indicate a problem and *must* be checked. If there are differences, restart this process and correct procedures so that problems do not recur.
- Use the PackMan install utility to install Message \#1. There should not be any warnings and the message should not cause any M errors. If it does, restart this process and correct procedures so that problems do not reoccur. To restart the process, it will be necessary to install Message \#2. Message \#2 serves as a backup of the original routines.
- Use the PackMan Compare Utility to check Message \#2 against the routines that are now on the disk (should now be from Message \#1). If there are differences, restart this process and correct procedures so that the differences do not recur.

When saving a copy of a routine that has *not* been edited, you can answer "YES" to the question "Do you wish to secure this message? NO// ". At this point, you will be asked to enter a scramble hint and the message will be inaccessible to anyone that does not know the password. If the message is changed, it will be noticed upon using the INSTALL/CHECK option under the XMPACK menu. You can check it by sending it to a user without any privileges. When that user tries to install it, integrity checking will be performed but no installation will take place.

<span id="_Toc147217311" class="anchor"></span>Figure 33. PackMan-related message options—Sample user prompts and message

Select MailMan Menu Option: <span class="mark">OTHER \<Enter\></span> MailMan Functions

BML List Contents of All Baskets

CLD Change/Delete LATERED Messages

EML Edit user options

FWD Forwarding Address Edit

GML Group membership

LML Load PackMan Message

MML Message Search by Sender/Date

PML Personal Group Enter/Edit

RLM Report on LATERED Messages

TML TalkMan

Select Other MailMan Functions Option: <span class="mark">LOAD \<Enter\></span> PackMan Message

Subject: XMPACK Documentation Test 11/3

Please enter description of PACKMAN Message

or press Return Key to exit.

1\>This is a test.

2\>\<Enter\>

EDIT Option: <span class="mark">\<Enter\></span>

Created by XMUSER,ONE at TCP1.BIG-SITE.VA.GOV on WEDNESDAY, 11/03/93 at 13:14

Select PackMan function: <span class="mark">ROUTINE LOAD</span>

routine(s) ? \> <span class="mark">XMA0</span>

routine(s) ? \> <span class="mark">\<Enter\></span>

Loading XMA0

Select PackMan function: <span class="mark">\<Enter\></span>

Send mail to: XMUSER,ONE// <span class="mark">\<Enter\></span>

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And send to: <span class="mark">\<Enter\></span>

Do you wish to secure this message? NO// <span class="mark">\<Enter\></span> (NO)

Select TRANSMIT option: Transmit now// <span class="mark">\<Enter\></span>

Delivering \[31983\]... .

Sent

Select Other MailMan Functions Option: <span class="mark">\<Enter\></span>

AML Assume another identity as a surrogate

HML MailMan Help ...

NML New messages and responses

OML Other MailMan Functions ...

RML Read a message

SML Send a Message

Select MailMan Menu Option: <span class="mark">READ \<Enter\></span> a message

Read MAIL BASKET: IN// <span class="mark">\<Enter\></span>

LAST Message Number: 18 Messages in BASKET: 6 (2 NEW)

IN Basket Message: 12// <span class="mark">31983</span>

Subj: XMPACK Documentation Test 11/3 \[#31983\] 03 Nov 93 13:13 108 Lines

From: PARKER,ROSELYN in 'IN' basket. Page 1

------------------------------------------------------------------------

\$TXT Created by PARKER,ROSELYN at TCP1.BIG-SITE.VA.GOV on WEDNESDAY, 11/03/93 at 13:14

This is a test.

\$END TXT

\$ROU XMS5A

XMS5A ;(WASH ISC)/CAP/AML/RJ-Query into message queues ;4/12/93 17:34 ;

;8.0T;MailMan-Test;Oct 05, 1993

D ^%ZIS Q:POP U IO

D NOW^%DTC K %I,%H S A=\$E(%,6,7)\_" "\_\$P("Jan^Feb^Mar^Apr^May^Jun^Jul^Aug^Sep^Oct^Nov^Dec",U,\$E(%,4,5))\_" "\_\$E(%,2,3)

I %\1'=% S %=\$P(%,".",2)\_"0000",A=A\_" "\_\$E(%,1,2)\_":"\_\$E(%,3,4)

S XMD0=A K DIR S (XMF0,XMF0("PG"),XMC0,XME0)=0,DIR(0)="E"

Q S XMF0=\$O(^DIC(4.2,"B",XMF0)) I XMF0="" G END

S XMG0=\$O(^DIC(4.2,"B",XMF0,0)) I '\$D(^XMBS(4.2999,XMG0)) G Q

S XMB0=\$S(\$D(^XMBS(4.2999,XMG0,3))#2:^(3),1:""),XMB=\$E(XMF0,1,16)

S XMA=0 D M G:XMA\<1 Q:XMB0=""

I +XMB0=0 S XMA0="" G W

S %H=\$P(XMB0,"^",1) D TT^%DTC S %=\$P(%H,",",2),%=%#3600\60/100+(%\3600)/100,%=X\_\$S(%:%,1:""),Y=% X ^DD("DD") S Y=\$P(Y,",",1)\_" "\_\$P(Y,"@",2)

S XMA0=Y\_"^"\_\$P(XMB0,"^",2,6)

W ;write results

I \$Y+5\>IOSL!'XMF0("PG") S X="" D:'\$D(ZTQUEUED)&XMF0("PG") ^DIR:IOST?1"C-".E K DIRUT D HD G END:X=U

S XMC0=XMC0+1 I \$P(XMA0,U,4)\<0 S \$P(XMA0,U,4)=0

W!,XMB,?18,\$J(XMA,6),?25,\$P(XMA0,"^",1),?40,\$P(XMA0,"^",2),?48,\$P(XMA0,"^",3),?54,\$J(\$P(XMA0,"^",4),4),?59,\$J(\$P(XMA0,"^",5)\1,4),?68,\$P(XMA0,"^",6)

G Q

M ;number in queue

S XMA=\$S(\$D(^XMB(3.7,.5,2,XMG0+1000,0)):\$P(^(0),U,5),1:0) Q

HD S XMF0("PG")=XMF0("PG")+1 W @IOF,!,"TRANSMISSION QUEUE STATUS REPORT",?79-\$L(XMD0),XMD0,!,"At "\_^XMB("NETNAME"),?70,"Page: "\_XMF0("PG"),!

W !,"Domain",?18,"Queued",?25,"Updated",?40,"Msg \# Line Errors Rate IO",!

Q

END I \$D(XMC0),XMC0\<1 D HD:IOST'?1"C".E&'XMF0("PG") W !,"No messages queued or in active transmission.",!

K %,%H,%I,DIR,I,X,XMC0,XMB,XME0,XMB0,XMA0,XMA,XMG0,XMF0,Y

D ^%ZISC

Q

CONT ;CONTINUOUS DISPLAY

D XMS5A R !,X:10 Q:\$T G CONT

GO W !! G XMS5A

\>

\$END ROU XMS5A

Select MESSAGE Action: IGNORE (in IN basket)// <span class="mark">\<Enter\></span> Ignored

## Security of PackMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan security check involves comparing a message with what is on the disk and ensuring that the message security has *not* been altered. The security check of a message against its checksums is part of the installation process. DUZ(0)="@" is not necessary to compare, summarize, or "pretty print" a PackMan message. DUZ(0)="@" is necessary for the routine and global load process and to do an installation (after the security check).

The installer and the security checker both resolve the install/check functions using the same option, however, the security checker does not get to do the installation. To access PackMan, a user must hold the XUPROGMODE key. DUZ(0) must equal "@" (i.e., at-sign) in order for PackMan messages to be created or installed.

## Installing PackMan Messages into a Second Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several suggestions follow for installing a PackMan message in a different account from the one in which it was received. This is often necessary when patches or new versions of programs arrive in MailMan on a production account and need to be installed in a test account that does not have MailMan installed:

1.  Install MailMan in the test account and then forward the message. As PackMan messages come into your production account they can automatically be forwarded to the test account.
1.  You can add an entry to the DOMAIN file (#4.2) for TRN.YOUR. You can forward the PackMan message to that domain from VAH.
2.  Establish INTER-UCI Network Mail using a subordinate domain and port-to-port Equinox connections. You can receive mail in production and forward it to the test account as new mail.
3.  Play a script from TRN when you are ready to receive the patch.

Alternatively, you can also use Inter UCI options.

17. Kernel Toolkit provides an option to load a Host file into a mail message. Therefore you can try the following:
1.  Headerless Print your PackMan message to your HFS device from production.
2.  In your test system, use Kernel Toolkit to move the Host file back into MailMan. The routine can then be unpacked.
18. If you are a VAX site and the XMB global is translated to your test UCI, you can login from the VMS level with the following:

\$ DSM/UCI=VAH/VOL=ROU/ROUTINES=\[TST,ROU\]

Then you would access MailMan and load in the routine message. The routines would go directly into TST, but you would be using the globals in VAH.

# TalkMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## TalkMan—Communications Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TalkMan \[XMTALK\] allows users to share communication capabilities outside the facility. It is simply a rudimentary script processor/language. TalkMan is "dumb" in the sense that it does *not* know what kind of device with which it is communicating; the user *must* know. A new domain *must* be set up first.

In setting up a TalkMan domain, you specify the following to TalkMan:

- Script(s) you would like to play.
- Specific Port/Hunt Group as its physical link device to open.
- Transmission protocol to use.

You *must* also enter the "T" character in the FLAGS field of the DOMAIN file (#4.2) for the TalkMan domain you are creating.

|                                                   |                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/097.png) | NOTE: If you follow the IDCU naming convention, everyone should use the "VAMCxxx" as the destination address. |

In the script(s) you create for the TalkMan domain, you *must* also enter the commands and words for TalkMan to send to the other system or look for from the connected system.

When you press the \<ESC\> key, there will be an opportunity to do the following:

| Escape Function | Description                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------|
| RETURN          | Return to user TalkMan session (Press the \<Enter\> key);                                                               |
| CAPTURE         | Capture user session into a Message. The SUBJECT is \[If your name is Last,First\], "LAST,FIRST CAPTURE @ \<date & time\>"; |
| END             | End the TalkMan session.                                                                                                    |

## How to Capture a Session into a MailMan Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the user enters TalkMan, the Capture feature is in an off state. Activate Capture by pressing the \<ESC\> key and answering "C" to the command prompt.

When Capture is on, a message is being delivered into the user's "IN" basket. The message contains the text (minus control characters) of the interaction during the TalkMan session. Since TalkMan does *not* know the content, TalkMan separates it into lines of 75 characters or less.

|                                                   |                                                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/098.png) | CAUTION: It may be very inappropriate to turn TalkMan on during a session when users are working with software that does screen management. |

When viewers are ready to stop the Capture, they can do so by pressing the \<ESC\> key and entering "E" to End your session, or "S" to Stop the text capture.

### How to End a TalkMan Session

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While a TalkMan session is in progress, users can press the \<CTRL A\> key at any time. This takes the viewer to the command line. A prompt appears for the user to enter a command. Entering an "E" (End) as the response will end the TalkMan session. The user will then be back on the machine from which TalkMan was invoked.

### How to Continue a TalkMan Session

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a viewer were using TalkMan and pressed the \<ESC\> key, he/she might find himself/herself at the command line. Pressing the \<Enter\> key will return you to the TalkMan session.

### Advantages and Disadvantages of Using TalkMan and IDCU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The advantages and disadvantages of implementing the TalkMan utilities are shown below:

| Advantages                                                                                                                                                                                                         | Disadvantages                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| Users can access IDCU and FORUM via the TalkMan utilities in MailMan. This allows for greater security, control, and ease of use.                                                                                  | More data gets stored in the ^XMB global. |
| TalkMan's dialogue capture is useful.                                                                                                                                                                              |                                           |
| TalkMan can be used extensively for all communications outside the facility, without additional passwords.                                                                                                         |                                           |
| When properly set up, the TalkMan domain will have your rotary ports as the address and not the network address.                                                                                                   |                                           |
| This procedure can be used to leave a message on a printer or to connect with another system via WAN/dial-up modem/direct lines. Any computer devices that are addressable directly by M can be used with TalkMan. |                                           |
| No noticeable system degradation.                                                                                                                                                                                  |                                           |
| Simple set up and easy system management.                                                                                                                                                                          |                                           |

# MailMan Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes editing of the MAILMAN SITE PARAMETERS file (#4.3) to specifically name the system installed at your site. It is the name of this installation of the MailMan software, as it is known to the rest of the network and it *must* appear in the DOMAIN file (#4.2).

Use the MailMan Site Parameters option \[XMKSP\] located on the Manage MailMan menu \[XMMGR\] to edit entries in the MAILMAN SITE PARAMETERS file (#4.3) (see Figure 34).

The example that follows shows actual system prompts, helpful field descriptions, and file data. Review this example to properly edit the MailMan site parameters in the MAILMAN SITE PARAMETERS file (#4.3) on your system.

|                                                   |                                                                                                                                   |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/099.png) | NOTE: Entering two question marks ("??") at the field prompts displays a full description of data required to be entered. |

<span id="_Ref140454974" class="anchor"></span>Figure 34. MailMan Site Parameters option—User dialogue with help information

MailMan 8.0 service for XMUSER,ONE@BIG-SITE.MED.VA.GOV

You last used MailMan: DD MM YY HH:MM

Check MailMan Files for Errors

Create a Mailbox for a user

Disk Space Management ...

Group/Distribution Management ...

Local Delivery Management ...

MailMan Site Parameters

Network Management ...

New Features for Managing MailMan

Remote MailLink Directory Menu ...

Select Manage MailMan Option: <span class="mark">MAILMAN \<Enter\></span> Site Parameters

Select MAILMAN SITE PARAMETERS DOMAIN NAME: <span class="mark">??</span>

1 BIG-SITE.MED.VA.GOV

You may enter a new MAILMAN SITE PARAMETERS, if you wish

This is the name of this installation of MailMan, as it is known

to the rest of the network. It must appear in the DOMAIN file.

This name applies to all CPUs or Volume sets which access this ^XMB

global.

Choose from:

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTEDVA.GOV

'^' TO STOP: <span class="mark">^</span>

Select MAILMAN SITE PARAMETERS DOMAIN NAME: <span class="mark">1 \<Enter\></span> BIG-SITE.MED.VA.GOV

TIME ZONE: PDT// <span class="mark">??</span>

This field defines the timezone in which this domain is located.

Note that Standard and Daylight savings times are considered two

different timezones, requiring that the timezone be changed with

the changing of daylight savings. The timezones are located in the

MailMan timezone file. The values of the cross references on this

field are appended to message dates as they are sent over the network.

Choose from:

ADT ATLANTIC DAYLIGHT

AST ATLANTIC STANDARD

BDT BERING DAYLIGHT

BST BERING STANDARD

CDT CENTRAL DAYLIGHT

CST CENTRAL STANDARD

EDT EASTERN DAYLIGHT

EST EASTERN STANDARD

HDT ALASKA-HAWAII DAYLIGHT

HST ALASKA-HAWAII STANDARD

MDT MOUNTAIN DAYLIGHT

MST MOUNTAIN STANDARD

NDT NEWFOUNDLAND DAYLIGHT

NST NEWFOUNDLAND STANDARD

PDT PACIFIC DAYLIGHT

PST PACIFIC STANDARD

YDT YUKON DAYLIGHT

YST YUKON STANDARD

TIME ZONE: PDT// <span class="mark">\<Enter\></span>

PARENT: BIG-SITE.MED.VA.GOV// <span class="mark">??</span>

This field holds the name of the domain which is considered the

parent of this domain. The parent domain's subordinate domain

list will contain this domain, also.

Parent domains are used for routing messages when a subordinate

domain does not know a direct path to the selected domain.

Domains are connected to their parents as follows:

1\. The local domain is named.

2\. The parent is named at the local site.

3\. A script from the parent to the subordinate domain is created.

4\. A christening operation is performed by the parent domain.

When the subordinate domain is christened, the domain is connected

to the network. (Mail may be addressed to remote domains)

Choose from:

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTED.VA.GOV

REDACTEDVA.GOV

'^' TO STOP: <span class="mark">^</span>

PARENT: BIG-SITE.MED.VA.GOV// <span class="mark">\<Enter\></span>

REQUIRE INTRODUCTIONS?: NO// <span class="mark">??</span>

If this is turned on, then users must introduce themselves when they

first log in to MailMan. This forces users to describe themselves,

and enter their phone numbers and addresses for others to query with

the HELP options in MailMan.

Choose from:

y YES

n NO

REQUIRE INTRODUCTIONS?: NO// <span class="mark">\<Enter\></span>

SHOW INSTITUTION IN MAILMAN?: YES// <span class="mark">??</span>

This field controls whether mailman will show the user's organization

after his name. This is useful when MailMan has many remote users,

who may not know each other's location or affiliation.

Choose from:

y YES

n NOSHOW INSTITUTION IN MAILMAN?: YES// <span class="mark">\<Enter\></span>

SHOW DUZ WHEN ADDRESS MESSAGE: <span class="mark">??</span>

When someone addresses a message to a local user, should the DUZ of the

local user be displayed?

(If this field is null, the default answer is "no".)

Disadvantages:

\- Your site's DUZs may be SSNs. They should not be displayed.

\- Users may be confused by the display.

Advantages:

\- A DUZ is unique, whereas some users may share the same or very similar

name. If a user knows the addressee's DUZ, the DUZ may be used to

address a message, instead of the name.

Choose from:

0 NO

1 YES

SHOW DUZ WHEN ADDRESS MESSAGE: <span class="mark">0 \<Enter\></span> NO

SHOW ADDRESS ON USER LOOKUP: <span class="mark">??</span>

Option XMHELPUSER displays user information. Among the items displayed

are the address fields (.111 through .116) from the NEW PERSON file.

Some sites have home address information in these fields, which should not

be displayed.

If the address fields should be displayed, answer YES; otherwise, answer

NO. If this field is null, the default answer is NO.

Choose from:

0 NO

1 YES

SHOW ADDRESS ON USER LOOKUP: <span class="mark">0 \<Enter\></span> NO

MESSAGE ACTION DEFAULT: DELETE// <span class="mark">??</span>

This is the default for the user prompt, "Message Action". The user may

over-ride this default by selecting his own under "Edit User Options".

Choose from:

I IGNORE

D DELETEMESSAGE ACTION DEFAULT: DELETE// <span class="mark">IGNORE \<Enter\></span> IGNORE

FORWARD PRIORITY MAIL TO GROUP: <span class="mark">??</span>

Enter YES if you wish to allow users to forward priority messages

to mail groups.

Enter NO if you don't. (This is the default, if this field is null.)

Then only the message originator or anyone with the XM GROUP PRIORITY

key may forward priority messages to mail groups.

Choose from:

0 NO

1 YES

FORWARD PRIORITY MAIL TO GROUP: <span class="mark">0 \<Enter\></span> NO

DROP OUT OF RESTRICTED GROUP: <span class="mark">??</span>

Enter YES if you wish to allow users to drop out of non-self-enrolling

mail groups. The user will be warned that this is a non-self-enrolling

group, and that they won't be allowed to rejoin later, and then they

will be asked to re-confirm the decision to drop out.

Enter NO if you don't. (This is the default if this field is null.)

Then users will have to contact IRM or the mail group coordinator to

ask to be dropped.

Choose from:

0 NO

1 YES

DROP OUT OF RESTRICTED GROUP: <span class="mark">0 \<Enter\></span> NO

TITLE SOURCE: <span class="mark">??</span>

Where in the NEW PERSON file should the user's title come from?

Enter 'S' if the user's title should come from field 20.3,

SIGNATURE BLOCK TITLE. If that field is empty, then we'll try

field 8, TITLE.

Enter 'T' if the user's title should come from field 8, TITLE.

If that field is empty, we won't show any title.

The default is 'T', if this field is not filled in.

Choose from:

S SIGNATURE BLOCK TITLE

T TITLE

TITLE SOURCE: <span class="mark">T \<Enter\></span> TITLE

COPY LIMIT - RECIPIENTS: <span class="mark">??</span>

This field enables site management to control whether a message with more

than a certain number of recipients may be copied. A user may not copy a

message which has more than this number of recipients. If this field is

null, then the limit is 2999.

COPY LIMIT - RECIPIENTS: <span class="mark">\<Enter\></span>

COPY LIMIT - RESPONSES: <span class="mark">??</span>

This field enables site management to limit the number of responses to

a message that may be copied. A user may not copy more than this number

of responses to a message. If this field is null, then the limit is 99.

COPY LIMIT - RESPONSES: <span class="mark">\<Enter\></span>

COPY LIMIT - LINES: 30000// <span class="mark">??</span>

This field enables site management to limit the number of lines that may be

copied from a message and its responses. A user may not copy more than

this number of message lines. If this field is null, then the limit is

3999\.

COPY LIMIT - LINES: 30000// <span class="mark">\<Enter\></span>

P-MESSAGE LINE LIMIT: <span class="mark">??</span>

This field enables site management to limit the number of lines which may

be printed to P-MESSAGE. If this field is null, there is no limit.

P-MESSAGE LINE LIMIT: <span class="mark">\<Enter\></span>

BIG GROUP SIZE: 100// <span class="mark">??</span>

During message addressing, when a user addresses a message to a mail group

with a lot of members, it can seem to take forever to process the group.

(Dots of death!) This field, BIG GROUP SIZE, can help.

IF you enter a number in this field, AND

\- If the group contains member groups

or - If the group contains distribution lists

or - If the number of local members plus the number of remote members

exceeds or equals the BIG GROUP SIZE boundary

THEN the user is asked whether s/he wants to queue the group for later

delivery, and avoid waiting while the group is processed.

The user is also warned that if s/he chooses to queue delivery, then

recipients may not be 'minus'ed from the group.

If the user chooses not to queue delivery, then processing proceeds in the

foreground, as usual.

If the user chooses to queue delivery, then s/he is asked when the delivery

should take place. The group is then queued for processing and delivery

at the specified time (by the same background job which 'news' messages).

There is no default. (If BIG GROUP SIZE equates to zero, then groups are

processed in the foreground as usual.)

BIG GROUP SIZE: 100// <span class="mark">\<Enter\></span>

FWD TEST MESSAGE TO POSTMASTER: <span class="mark">??</span>

Messages are sent automatically to a user's forwarding address if he

changes it. If you want these messages to be sent to the Postmaster,

also, so that he is aware that the forwarding addresses are proper

mark this field with "YES".

Choose from:

1 NO

0 YES

FWD TEST MESSAGE TO POSTMASTER: <span class="mark">Y \<Enter\></span> YES

FAX ENABLED: <span class="mark">??</span>

Your site is fax enabled if you have the suite of fax software and files

(^AKF) and fax capability and you choose to allow faxes to be sent via

MailMan.

To send faxes via MailMan, Mail groups (file 3.8) must first be populated

in the fax recipient and fax group multiples. Then, when a user sends a

message to a mail group, the message is also faxed to any fax recipients in

that mail group. Responses to the message are not faxed.

Choose from:

0 no

1 yes

FAX ENABLED: <span class="mark">0 \<Enter\></span> no

LARGE MESSAGE REPORT LINES: 999// <span class="mark">??</span>

This field is used by the large message report.

Any message with more than this many lines is included in the report.

If this field is null, the default is 100.

LARGE MESSAGE REPORT LINES: 999// <span class="mark">\<Enter\></span>

Select LIMITED BROADCAST: SERVICE/SECTION// <span class="mark">??</span>

Choose from:

DIVISION

KEY

PRIMARY MENU

SERVICE/SECTION

You may enter a new LIMITED BROADCAST, if you wish

This is the name of the associated field in the NEW PERSON file.

Select LIMITED BROADCAST: SERVICE/SECTION// <span class="mark">\<Enter\></span>

LIMITED BROADCAST: SERVICE/SECTION// <span class="mark">??</span>

This is the name of the associated field in the NEW PERSON file.

LIMITED BROADCAST: SERVICE/SECTION// <span class="mark">\<Enter\></span>

POINTED TO FILE: SERVICE/SECTION// <span class="mark">?</span>

Answer with FILE NUMBER, or NAME

Answer with FILE NUMBER, or NAME

Do you want the entire 798-Entry FILE List? <span class="mark">N \<Enter\></span> (No)

POINTED TO FILE: SERVICE/SECTION// <span class="mark">\<Enter\></span>

NEW PERSON FILE XREF: E// <span class="mark">??</span>

This is the name of the (whole file) cross reference on the associated

field in the NEW PERSON file.

NEW PERSON FILE XREF: E// <span class="mark">\<Enter\></span>

Select LIMITED BROADCAST: <span class="mark">??</span>

Choose from:

DIVISION

KEY

PRIMARY MENU

SERVICE/SECTION

You may enter a new LIMITED BROADCAST, if you wish

This is the name of the associated field in the NEW PERSON file.

Select LIMITED BROADCAST: <span class="mark">\<Enter\></span>

LIMITED BROADCAST DEFAULT: DIVISION// <span class="mark">\<Enter\></span>

MAX DIGITS FOR MESSAGE NUMBER: 7// <span class="mark">??</span>

This field is used to control the size of the message number in

^XMB(3.9, the MESSAGE file. If this field is null, its default

will be 8 digits. If the message number becomes greater

than this many digits, the message numbers will recycle back to

the next vacant message number after 999999. In this way, message

numbers will cease being too ungainly in size.

So message numbers will be re-used.

If MailMan is not able to find a vacant message number less than

this number of digits, then MailMan will take the next available

message number, no matter how many digits it has, AND MailMan will

change this field to reflect the new maximum.

It is very important that the unreferenced messages purge and/or

the date purge be run on a regular basis to free up message numbers

for re-use.

MAX DIGITS FOR MESSAGE NUMBER: 7// <span class="mark">\<Enter\></span>

BACKGROUND MESSAGE DELIVERERS: 10,50,100// <span class="mark">??</span>

You determine the number of delivery queues (10 max.) by what you enter in

this field. Each number designates a queue boundary and a boundary of the

number of recipients per message which a queue may handle.

By creating more than one delivery queue, messages with approximately the

same number of recipients will queue up together. Each delivery queue is

handled by a separate task. In this way, a message with many recipients

won't hold up the delivery of a message with few recipients.

For example:

A null entry means there will be one queue into which all messages are placed.

If you enter '10' it means that there will be two queues.

The first will deliver messages with fewer than 10 recipients.

The second will deliver messages with 10 or more recipients.

If you enter '50,100,200' there will be four (4) queues.

The first will deliver messages with fewer than 50 recipients.

The second will deliver messages with from 50 to 99 recipients.

The third will deliver messages with from 100 to 199 recipients.

The fourth will deliver messages with 200 or more recipients.

This field is used by the background filer to determine how many message

delivery queues (and tasks) there should be and how to separate them.

BACKGROUND MESSAGE DELIVERERS: 10,50,100// <span class="mark">\<Enter\></span>

BACKGROUND RESPONSE DELIVERERS: 10,50,100// <span class="mark">\<Enter\></span>

BACKGROUND FILER HANG TIME: <span class="mark">??</span>

This field is used by the background filer when it is started up to

determine the amount of time it will hang between deliveries of messages.

Since mail is not delivered, even to the sender, unless the background

filer delivers it, it should not be too long a period so that your users

are inconvenienced. If this field is not filled in the background filer

will hang for 5 seconds

between deliveries. 5 to 15 seconds is the recommended range.

BACKGROUND FILER HANG TIME: <span class="mark">5</span>

BACKGROUND FILER RUN FLAG: <span class="mark">??</span>

The background filer checks this field every time it is about to

deliver a message or response. If it is set to 1, it stops running, and

will not restart until it is set to null or zero. If it is null or zero,

and is already running, it continues. If it is null or zero, and is not

running, a background task will be created to restart it.

Choose from:

1 STOP RUNNING

0 OKAY TO RUN

BACKGROUND FILER RUN FLAG: <span class="mark">\<Enter\></span>

BACKGROUND FILER RUN PRIORITY: <span class="mark">??</span>

This field is used by the background filer to set its priority at runtime.

BACKGROUND FILER RUN PRIORITY: <span class="mark">\<Enter\></span>

CPU (UCI,VOL) FOR FILER TO RUN: <span class="mark">??</span>

Enter the UCI,VOL of where you want the background filer routines to run.

It is recommended that the XMB global also reside in this location.

If you are unsure what to enter, leave this field blank.

CPU (UCI,VOL) FOR FILER TO RUN: <span class="mark">\<Enter\></span>

NO-PURGE DAYS BUFFER: <span class="mark">??</span>

This field is used by the unreferenced messages purge to avoid purging

the last few days worth of messages in the message file. It should be

a number sufficiently high so as to avoid purging messages which are

in danger of being purged before they can be delivered. This includes

incoming network mail messages.

The minimum (and default if this field is null) is two days.

For example, if this field is 2, then messages up to and including those

whose local create date is 2 days ago are subject to possible purge.

NO-PURGE DAYS BUFFER: <span class="mark">\<Enter\></span>

NO-PURGE DAYS BUFFER (LOCAL): <span class="mark">??</span>

This field is used during the un-referenced-messages purge to avoid

purging the last few messages in the message file, according to

their local create date.

We subtract the NO-PURGE DAYS BUFFER (LOCAL) from today's date, giving

a 'no-purge date'. Local messages which were created on or after that

date and which were sent to remote sites are not subject to purge.

Other messages are not affected by this buffer.

If this field is not filled in, it defaults to 7 days. This is the

recommended value.

It should not be less than the NO-PURGE DAYS BUFFER (field 4.301)

or it will have no effect.

One situation in which this buffer may be useful is in the case of a

message sent only to a remote site. Such a message is unreferenced

and would otherwise be subject to purge. If a reply came from the

remote site after the original message had been purged, the sender

would have access only to the reply and not to the original message.

The NO-PURGE DAYS BUFFER (LOCAL) could be set to a reasonable number

of days to allow for a reply.

NO-PURGE DAYS BUFFER (LOCAL): <span class="mark">\<Enter\></span>

AUTOMATIC INTEGRITY CHECK: NO// <span class="mark">??</span>

XMAUTOPURGE is generally run at least once a week at most sites. It is

the process that purges messages that are no longer referenced. Before it

is run, XMCLEAN is generally run. XMCLEAN removes messages from WASTE

baskets so that they will be unreferenced when XMAUTOPURGE comes along.

XMAUTOPURGE kicks off the part of XMUTCHECKFILE that checks the Mail Box

file. XMUTCHECKFILE also resets and cleans up the x-refs of this file.

If your system has had fairly clean runs of XMUTCHECKFILE or if the entire

XMUTCHECKFILE process is run regularly as a separate process, it is not

necessary for XMAUTOPURGE to run any part of it again.

Choose from:

0 YES

1 NO

AUTOMATIC INTEGRITY CHECK: NO// <span class="mark">\<Enter\></span>

WEEKDAY DAYS TO PURGE: 30// <span class="mark">??</span>

When the unreferenced messages purge runs, it purges messages from

the message file, ^XMB(3.9, which are no longer referenced, meaning

they aren't in anyone's mailbox.

If this field is null, OR if the purge is run on Saturday, the purge

starts at the beginning of the message file.

If this field has a value, AND the purge is run on Sunday through

Friday, the purge starts at the message create date calculated by

subtracting the number of days from today's date.

So, if this number is 45, the unreferenced message purge would start

with messages created 45 days ago, and work from there forward.

WEEKDAY DAYS TO PURGE: 30// <span class="mark">\<Enter\></span>

IN-BASKET-PURGE DAYS: 120// <span class="mark">??</span>

This field is used by the IN BASKET PURGE to identify inactive messages and

mark them for purging.

A message is considered inactive if it has not been accessed in the past

number of days specified here. The default is 30 days.

The IN BASKET PURGE sends a message to each user listing all messages which

it has marked for purging and stating that they will be purged in an

additional 30 days if they remain in the 'IN' basket and are not accessed

again.

IN-BASKET-PURGE DAYS: 120// <span class="mark">\<Enter\></span>

IN-BASKET-PURGE TYPE: <span class="mark">??</span>

This field controls the extent of the IN-BASKET-PURGE.

If it is not filled in the effect on the IN-BASKET-PURGE

is the same as it would be if the value of the field is zero.

The field can have the following values:

0 or null = The IN-BASKET-PURGE will affect user IN baskets only.

1 = The IN-BASKET-PURGE will affect all user baskets. (This is not

the normal way for this process to be run. It is recommended that you

discuss this with site management and get user input before doing this.)

In either case the users will be sent the now familiar message listing

the messages that will be deleted from their baskets in 30 days. In

either case the field 'IN-BASKET-PURGE DAYS' will control how long a

message can remain inactive in a basket before it is considered okay

to put on the list of messages to be considered for deletion.

Choose from:

0 IN BASKET ONLY

1 ALL BASKETS

IN-BASKET-PURGE TYPE: <span class="mark">\<Enter\></span>

DATE PURGE CUTOFF DAYS: <span class="mark">??</span>

This field is used by the option XMPURGE-BY-DATE. When this option

is run, the date purge will be set to purge all messages originating

this many days ago and before.

If this field is null, the default will be 730 days (2 years).

DATE PURGE CUTOFF DAYS: <span class="mark">\<Enter\></span>

DATE PURGE GRACE PERIOD: <span class="mark">??</span>

This is the number of days' warning the users get before the date

purge, XMPURGE-BY-DATE, is run.

This field is used by the option XMPURGE-BY-DATE only if that

option is scheduled, not if it is run interactively.

At the scheduled date/time, the bulletin, XM DATE PURGE WARNING,

is broadcast to all users to warn them of the coming date purge,

and the actual date purge is then queued to run this many days

later.

If this field is null, the date purge will run at the scheduled

date/time, and no bulletin will be sent.

DATE PURGE GRACE PERIOD: <span class="mark">\<Enter\></span>

PREVENT MESSAGE RELAY?: YES// <span class="mark">??</span>

Answer YES if you want to prevent outside sites from sending mail through

your site to other outside sites. Spammers and Virus propagators use this

technique to disguise the source of their mail, and to make it appear to

come from a trusted source, namely your site.

Answer NO if you want your site to act as a relay site for anyone.

It is strongly recommended that you answer YES to prevent your site from

unwittingly relaying destructive mail.

If you answer YES, you should define your "inside" sites in the MY DOMAIN

(field \#41) multiple, so that MailMan can distinguish them from outside

sites.

> **NOTE:** This does NOT prevent users from receiving mail from outside sites.

It also does NOT prevent users from forwarding mail to outside sites.

Such actions are perfectly acceptable.

Choose from:

1 YES

0 NO

PREVENT MESSAGE RELAY?: YES// <span class="mark">\<Enter\></span>

Select MY DOMAINS: .VA.GOV// <span class="mark">??</span>

.VA.GOV

You may enter a new MY DOMAINS, if you wish

If you answered YES to PREVENT MESSAGE RELAYING? (field \#40), to stop

your site from relaying messages from outside sites through your site to

other outside sites, you may add entries here, in order to define what is

an "inside" site, or sites whose messages your site is willing to relay.

For example, if your site is a VA site, then other VA sites are "inside"

sites, and your site should relay mail for them. So, any site whose domain

name ends in ".VA.GOV" is an "inside" site. So VA sites should have only

one record in this multiple, and it should be ".VA.GOV".

The default, if there are no entries in this multiple, is your site's

domain name.

MailMan will check the site name of any site which connects to it, and

identifies itself in the SMTP HELO \<sitename\> command. If the sitename

ends in any of the entries in this multiple, then any mail coming from

that site through your site to other sites, will be accepted and relayed

onward.

If the sitename does not end in any of the entries in this multiple, then

messages will only be accepted that are addressed to recipients whose

sitenames end in one of the entries in this multiple. Otherwise, the site

will receive an error message telling it that relaying is denied, and

messages will not be accepted for relaying onward.

Select MY DOMAINS: .VA.GOV// <span class="mark">\<Enter\></span>

NETWORK - MAX LINES SEND: 99999// <span class="mark">??</span>

This field enables site management to limit the number of lines which

a message may have when it is addressed to a remote recipient. A user

may not send a message across the network with more than this number of

lines. If this field is null, there is no limit.

NETWORK - MAX LINES SEND: 99999// <span class="mark">\<Enter\></span>

NETWORK - MAX LINES RECEIVE: 99999// <span class="mark">\<Enter\></span>

NETWORK - BLOCK SIZE RECEIVE: <span class="mark">??</span>

\*\*\* This field is reserved for future use. Not currently used. \*\*\*

This is the maximum number of characters to read at a time when

receiving incoming transmissions. Default is 255.

Limiting factors are:

\- Maximum string length on the system.

\- Maximum global length on the system. In particular, maximum

(desirable) length of a line of message text in the MESSAGE file:

S ^XMB(3.9,xmz,2,x,0)=\<line of message text\>

You may also wish to consider the maximum string length that the

system's various editors can handle. See the Technical Description

for more information.

Choose from:

A 255

B 512

NETWORK - BLOCK SIZE RECEIVE: <span class="mark">\<Enter\></span>

TCP CHANNEL - MAXIMUM TO USE: <span class="mark">??</span>

This field contains a value that is checked before starting a process

to transmit mail via a TCP/IP channel. If there are already as many

processes running as is in this field, no process is started.

TCP CHANNEL - MAXIMUM TO USE: <span class="mark">\<Enter\></span>

TCP/IP POLLER RUN FLAG: <span class="mark">??</span>

This field is checked every time the background tcp poller, XMRTCP,

starts to process poller request. If it is set to 1, XMRTCP stops

running. If it is null or zero, XMRTCP processes the next entry. If

XMRTCP is not running it will not be restarted if the field is set to 1.

If it is null or 0, and XMRTCP is not running, a background task will be

created to restart it.

Choose from:

1 STOP RUNNING

0 OKAY TO RUN

TCP/IP POLLER RUN FLAG: <span class="mark">\<Enter\></span>

RECORD NETMAIL TRANSCRIPT?: <span class="mark">??</span>

This field allows the site manager to turn on and off (toggle) whether or

not MailMan records all script transcripts in background. The send portion

of scripts played (using the 'Play Script' option) will not be recorded.

Choose from:

1 YES

0 NO

RECORD NETMAIL TRANSCRIPT?: <span class="mark">\<Enter\></span>

XMITS TILL ERROR MESSAGE: <span class="mark">??</span>

How many times will a transmission be attempted before a message is

sent to the Postmaster indicating that there have been multiple,

unsuccessful transmissions to a domain.

XMITS TILL ERROR MESSAGE: <span class="mark">\<Enter\></span>

DNS AWARE: YES// <span class="mark">??</span>

In order for MailMan to be DNS aware, the site must have installed the

requisite Kernel patches for DNS.

\- DNS IP (field 51 in file 8989.3) must contain an IP address

for a DNS server.

\- Routine ^XLFNSLK must exist.

If you answer 'no', MailMan will use the IP addresses in the domain

scripts.

If you answer 'yes', MailMan will use the IP addresses in the domain

scripts, but if they fail, or don't exist, MailMan will use DNS to

ascertain other IP addresses to try. MailMan will replace failed script

IP address with the successful DNS IP address.

Choose from:

0 NO

1 YES

DNS AWARE: YES// <span class="mark">\<Enter\></span>

TCP/IP COMMUNICATIONS PROTOCOL: TCP/IP-MAILMAN// <span class="mark">??</span>

For TCP/IP connections, the scripts (the TEXT field, 2, in the TRANSMISSION

SCRIPT multiple, 4, of the DOMAIN file, 4.2) can be built on-the-fly, if

they don't exist, and if both this field and field 8.24 are filled in.

We identify the TCP/IP transmission scripts in file 4.2 by the TYPE field,

1.2, within the TRANSMISSION SCRIPT multiple. Those whose TYPE is 'SMTP',

'TCPCHAN', or null are considered TCP/IP transmission scripts.

We can build the scripts, because they are standard.

Here's an example of one for FORUM:

O H=FORUM.VA.GOV,P=TCP/IP-MAILMAN

C TCPCHAN-SOCKET25

In this script, the TCP/IP-MAILMAN refers to the communications protocol

to use. This field should point to the communications protocol in file 3.4

that should be used for TCP/IP connections.

Choose from:

1SCP

2BSCP

3BSCP

BCP

BCX

BSCP

CHECKED

DECNET

DIAL OUT

DIRECT

MINI

MINIFORUM

NO-LF

PC1

R-GLOBAL

S-GLOBAL

SCP

SERVER

SPEC

<span class="mark">^</span>

TCP/IP COMMUNICATIONS PROTOCOL: TCP/IP-MAILMAN// <span class="mark">\<Enter\></span>

TCP/IP TRANSMISSION SCRIPT: TCPCHAN-SOCKET25// <span class="mark">?</span>

Which script shall be used for TCP/IP?

Answer with TRANSMISSION SCRIPT NAME

Do you want the entire 55-Entry TRANSMISSION SCRIPT List? <span class="mark">N \<Enter\></span> (No)

TCP/IP TRANSMISSION SCRIPT: TCPCHAN-SOCKET25// <span class="mark">\<Enter\></span>

TCP/IP DEVICE: <span class="mark">??</span>

For TCP/IP connections, the physical link/device to be used is usually

standard - some sort of NULL device. This field is a free-text pointer

to that device in the DEVICE (#3.5) file.

The device pointed to by this field will be used for a TCP/IP connection

if, in the DOMAIN (#4.2) file, the device field is null in both of the

following fields:

\- PHYSICAL LINK / DEVICE (#1.3) field of the TRANSMISSION SCRIPT (#4)

multiple

\- PHYSICAL LINK DEVICE (#17) field

For more information, see the PHYSICAL LINK DEVICE (#17) field in the

DOMAIN (#4.2) file.

TCP/IP DEVICE: <span class="mark">\<Enter\></span>

STATS NORMALIZATION: <span class="mark">??</span>

This option allows the user to customize the normalized report.

STATS NORMALIZATION: <span class="mark">\<Enter\></span>

DIRECTORY REQUEST FLAG: Requests will be granted.

// <span class="mark">??</span>

This field controls whether or not the XMMGR-DIRECTORY-RECV option will

grant request from remote site to send domain user directory information

.

If the value is null or zero, request is rejected. If the value is

one, a request is granted and domain user directory will

be made available to the remote site.

Choose from:

0 Requests will NOT be granted.

1 Requests will be granted.

DIRECTORY REQUEST FLAG: Requests will be granted.

// <span class="mark">\<Enter\></span>

FTP ADDRESS FOR BLOB \<GET\>: <span class="mark">??</span>

If your images are on a network that is available via FTP from your

main node and you have no other way of accessing those message to get

them onto you main node so that you can FTP them to other sites, put

the IP address of the machine that you will GET your images from

into this field.

FTP ADDRESS FOR BLOB \<GET\>: <span class="mark">\<Enter\></span>

FTP RECEIVE DIRECTORY: <span class="mark">??</span>

This field is used to store the path for BLOBs to be received in.

It is communicated to the transmitter of messages containing BLOBS so

that they can be FTP'd to the correct directory once the disk has

been designated with field 7.711.

If the receiving system is a DOS system the disk portion of the path

is in the field 'FTP RECEIVE DISK'.

FTP RECEIVE DIRECTORY: <span class="mark">\<Enter\></span>

FTP RECEIVE NETWORK LOCATION: <span class="mark">??</span>

This field should be the name of an entry in your 2005.2 file (Network

Location). It maps where incoming BLOBs will be placed and is the

logical equivalent of field 7.7.

FTP RECEIVE NETWORK LOCATION: <span class="mark">\<Enter\></span>

FTP RECEIVE DISK: <span class="mark">??</span>

This field contains the name of the physical disk that the FTP Receive

Network Location is on if the receiving system is a DOS system.

FTP RECEIVE DISK: <span class="mark">\<Enter\></span>

FTP ADDRESS FOR BLOB RECEIVE: <span class="mark">??</span>

This is the IP address that you will advertise to other sites that wish

to send you images that attach to Multimedia messages.

FTP ADDRESS FOR BLOB RECEIVE: <span class="mark">\<Enter\></span>

FTP USERNAME: <span class="mark">??</span>

This is the VMS username that the sender will be told to use when he

FTP's BLOBs to this domain.

FTP USERNAME: <span class="mark">\<Enter\></span>

FTP PASSWORD: <span class="mark">??</span>

This is the password if any that a BLOB sender needs to have when he FTPs

into the system.

FTP PASSWORD: <span class="mark">\<Enter\></span>

FTP NOTES:

No existing text

Edit? NO// <span class="mark">\<Enter\></span>

Select MAILMAN SITE PARAMETERS DOMAIN NAME:

|                                                   |                                                                                                                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/100.png) | Ref: For more information on setting up TCP/IP service for MailMan, please refer to the "TCP/IP Service for Mailman" document on the VDL at <http://www.va.gov/vdl/Infrastructure.asp?appID=15> |

# MailMan Integrity Checker (XMUT-CHKFIL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan Integrity Checker module is intended to automatically identify and correct some errors that may occur. It is used as part of the XMAUTOPURGE option sequence. It makes sure that the MUMPS cross-reference of MAILBOX file (#3.7) has all the required entries. It can also be run standalone. The integrity checker allows the system manager to look for potential problems that appear in the B-Tree disk structure. Some errors can be ignored or placed on a higher or lower priority list because of how they can affect your system. The information below will help you to decipher that list.

## Error Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Errors are listed in a general format. Important pieces of data are listed along with the error. This way, the programmer can relate the errors to the appropriate file.

- XMDUZ—DUZ: The .01 field of the MAILBOX file (#3.7), ^XMB(3.7,XMDUZ,... .
- Basket—The message basket in which the error occurred, ^XMB(3.7,XMDUZ,2,basket... .
- XMZ or SEQ#—The message number that the error applies to. Either: ^XMB(3.7,XMDUZ,2,1,XMZ,0 or ^XMZ(3.9,XMZ... .

Each error has a TYPE label. This is a number associated with a description:

TYPE: 10 \<\< IN 'M' \> \> \>\>\> \*\* XMDUZ=3,BASKET=1 XMZ=999

The TYPEs are numbered so that a summary of the errors can be listed at the bottom of the report. If the report is left running unsupervised, it can print out a lot of characters that indicate it is progressing through the files. At the end of each report, the number of errors reported is listed.

The string "\<\<\< IN 'M' \> 1 \>\>\>" describes the error. This is shorthand for:

"The message was in the "M" cross-reference of the MAILBOX file (#3.7) for one user more than one time."

This usually means that the user has the message in more than one basket. This is not an error you need to correct. It will *not* cause any large problems. However, it may cause a user to see the same message as "New" multiple times (as many are in the "M" cross-reference).

The rest of the string describes the "M" cross-reference subscripts. You should find an entry elsewhere in the listing that has the same XMDUZ and XMZ, but different basket numbers. It is in multiple baskets.

## Error Type Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some errors are automatically corrected by the MailMan Integrity Checker and some are not. For instance, Error TYPE: 3 causes the integrity checker to renumber the mail basket in question. Each error that is automatically corrected is so flagged.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 42%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>TYPE</th>
<th>String</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td><strong>&lt;&lt;&lt; BSKT SEQ#, NO 'C' X-REF &gt;&gt;&gt;<br />
*NOT CORRECTED AUTOMATICALLY*</strong></td>
<td>This error means that a message in a mail basket has a sequence number, but it is not in the "C" cross-reference for that basket. When this occurs, it can easily be corrected by signing on as the user and reading the affected basket, ordering it to be renumbered. A user with this problem would not see the message listed unless he did a search.</td>
</tr>
<tr class="even">
<td>3</td>
<td><strong>&lt;&lt;&lt; 'M' X-REF, NOT MLBX-FIXED &gt;&gt;&gt;<br />
*CORRECTED AUTOMATICALLY*</strong></td>
<td>This error means that a message was found in the "M" cross-reference, but not in the mail basket it was pointing to. If it were the only "M" cross-reference entry, the message would not be purged when it should be. The message is removed from the "M" cross-reference.</td>
</tr>
<tr class="odd">
<td>4</td>
<td><strong>TYPE: &lt;&lt;&lt; MESSAGE - NO SEQ# &gt;&gt;&gt;<br />
*CORRECTED AUTOMATICALLY*</strong></td>
<td>This error means that a message in a mail basket has no sequence number. This error is corrected by renumbering the mail basket.</td>
</tr>
<tr class="even">
<td>6</td>
<td><strong>&lt;&lt;&lt; BSKT ENTRY NO MSG - FIXED &gt;&gt;&gt;<br />
*CORRECTED AUTOMATICALLY*</strong></td>
<td>This error means that a message in a basket has no text associated with it. There is no entry for the message in the MESSAGE file (#3.9). The message is removed using KL^XMA1B.</td>
</tr>
<tr class="odd">
<td>9</td>
<td><strong>&lt;&lt;&lt; BAD/NO 0 NODE &gt;&gt;&gt;<br />
*NOT AUTOMATICALLY CORRECTED*</strong></td>
<td>This error means that an entry in the MESSAGE file (#3.9) exists with no zero node [^XMB(3.9,XMZ,0)]. A message of this kind usually is not owned by anyone and can be deleted. Entries like this can be created by Network Mail. The site received a message where the transmission did not end gracefully before MailMan could recognize this and kill off the incomplete transmission.</td>
</tr>
<tr class="even">
<td>12</td>
<td><strong>&lt;&lt;&lt; RECPT iii OF nnnn W/NO OR BAD 0 NODE &gt;&gt;&gt;<br />
*CORRECTED AUTOMATICALLY*</strong></td>
<td><p>This error means that there is a recipient of message (XMZ=<em>nnnn</em>) whose zero node is undefined or does not have correct information. The correction is to create a new zero node:</p>
<p>S ^XMB(3.9,XMZ,1,III,0)=Pointer in File #200</p>
<p>This error is sometimes found with a corresponding TYPE:13 error, (see below).</p></td>
</tr>
<tr class="odd">
<td>13</td>
<td><strong>&lt;&lt;&lt; MESS#nnnnRECPTiii/jjj IN 'C' REF/NO RECPT,0 NODE &gt;&gt;&gt;<br />
*CORRECTED AUTOMATICALLY*</strong></td>
<td><p>This error means that there is a recipient of message (XMZ=nnnn) whose zero node is undefined or does not have correct information. The correction is to create a new zero node:</p>
<p>S ^XMB(3.9,XMZ,1,III,0)=Pointer to File #200</p>
<p>The difference between this error and the TYPE: 12 error is that this error was found while passing the "C" cross-reference of the message recipients; and TYPE: 12 errors were found while parsing the data nodes.</p></td>
</tr>
<tr class="even">
<td>14</td>
<td><strong>&lt;&lt;&lt; NO BKT 0 NODE - FIXED &gt;&gt;&gt;<br />
*CORRECTED AUTOMATICALLY*</strong></td>
<td>This error means that the mail basket in question has no zero node, but it does have messages or data that looks like messages. Correcting this error type requires some knowledge of MailMan. The easiest way to correct this error is to create a zero node for the basket, checking the cross-reference [^XMB(3.7,XMDUZ,2,"B")] to see if it is already pointing to it. If so, set the node with the same text as the cross-reference indicates. The correct number of messages flagged as "New" is set.</td>
</tr>
<tr class="odd">
<td>17</td>
<td><strong>&lt;&lt;&lt; NOT IN 'M' X REF - FIXED &gt;&gt;&gt;<br />
*CORRECTED AUTOMATICALLY*</strong></td>
<td>This error means that a message was found in a basket that did not have an "M" cross-reference. This could be a bad error because it may allow a message that only this user kept in a basket to be purged. An "M" cross-reference for the message is then created.</td>
</tr>
<tr class="even">
<td>18</td>
<td><strong>&lt;&lt;&lt; NEW,NOT IN BASKET &gt;&gt;&gt;<br />
*NOT CORRECTED AUTOMATICALLY*</strong></td>
<td>This error means that a message exists in the "N0" cross-reference of the MAILBOX file (#3.7), but is not in the user's mail basket. It can be corrected while the user is reading new mail.</td>
</tr>
<tr class="odd">
<td>19</td>
<td><strong>&lt;&lt;&lt; NEW,NO MESSAGE TEXT - FIXED &gt;&gt;&gt;<br />
*CORRECTED AUTOMATICALLY*</strong></td>
<td>This error means a message exists in the "N0" cross-reference of the MAILBOX file (#3.7), but has no text and is not in the user's mail basket and there is no entry into MESSAGE file (#3.9). The message is removed using KL^XMA1B.</td>
</tr>
<tr class="even">
<td>20</td>
<td><strong>&lt;&lt;&lt; MESSAGE - NO SUBJECT &gt;&gt;&gt;<br />
*NOT CORRECTED AUTOMATICALLY*</strong></td>
<td>This error is corrected when the user attempts to read the message and the entry is removed from the mailbox.</td>
</tr>
<tr class="odd">
<td>21</td>
<td><strong>&lt;&lt;&lt; MESSAGE - BAD SUBJECT &gt;&gt;&gt;<br />
*NOT CORRECTED AUTOMATICALLY*</strong></td>
<td>Most of the TYPE: 21 errors were created by versions of earlier versions of MailMan and do no harm. MailMan does <em>not</em> allow messages with the subject text less than three characters or more than 65 characters in length. Leading and trailing blanks are removed.</td>
</tr>
<tr class="even">
<td>22</td>
<td><strong>&lt;&lt;&lt; MESSAGE - NO SENDER &gt;&gt;&gt;<br />
*NOT CORRECTED AUTOMATICALLY*</strong></td>
<td>This error would not cause any problems and should not be corrected.</td>
</tr>
<tr class="odd">
<td>23</td>
<td><strong>&lt;&lt;&lt; MESSAGE - NO DATE &amp; TIME &gt;&gt;&gt;<br />
*NOT CORRECTED AUTOMATICALLY*</strong></td>
<td>This error would not cause any problems and should not be corrected.</td>
</tr>
<tr class="even">
<td>24</td>
<td><strong>&lt;&lt;&lt; MESSAGE - SENDER NOT RECIPIENT &gt;&gt;&gt;</strong></td>
<td>This is not really an error. It is for informational purposes only.</td>
</tr>
<tr class="odd">
<td>25</td>
<td><strong>&lt;&lt;&lt; MESSAGE - NO MESSAGE <em>nnnn</em> FOR RESPONSE <em>rrrr</em> &gt;&gt;&gt;<br />
*NOT CORRECTED AUTOMATICALLY*</strong></td>
<td><p>Each response is associated with a message. Usually, this is done by placing the response into the RESPONSE Multiple field of the message and automatically naming it with a Subject, whose first letter is an "R" and whose second through 99th digits are numbers (e.g., R1233 points to and is a response to message number 1233). Users are not allowed to use this syntax for message titles, in order to avoid contradictions in the database; this was not true in earlier versions of MailMan.</p>
<p>This error can be caused by a naming convention problem (last paragraph), a message that was purged without purging the associated responses, or of a message that was lost during a database degrade. Regardless of how it occurs, this is a tricky issue to resolve because a user may be in the middle of a response that is not yet filed.</p>
<p>A real message will usually have recipients [^XMB(3.9,XMZ,1...], and be pointed to from ^XMB(3.7,"M",XMZ,...</p>
<p>A real response will not have responses and will not have recipients.</p>
<p>The best way to resolve these errors is to figure out if the entry in the MESSAGE file (#3.9) is really a message. If not, change the name to something that the purge will recognize as other than a response and to let the XMAUTOPURGE option handle them.</p>
<p>The worst problem that can arise as a result of these errors is ineffective use of disk space.</p></td>
</tr>
</tbody>
</table>

# Fine Tuning MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan impacts site disk space and CPU. Disk space is generally used for message storage and can be very extensive. The XMB globals should be placed with this in mind. CPU is used mostly for message transmissions. The kind of activity differs depending on the kind of site. Some sites transmit data to central data collectors. Others distribute software or transmit personal messages. The recommendation is that sites have at least two ports set aside for outgoing network mail traffic. One port should be used exclusively for transmissions to REDACTED.VA.GOV. The others should be put into a HUNT device so they can be shared by all the other domains. Transmitting messages across the network can be a very CPU intensive task and consideration should be taken to put the network mail activity onto a CPU that can handle this level of activity.

## Background Filers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When MailMan is installed, there are two delivery queues and two processes that deliver all messages as a default. Delivery activity can be monitored (routine XMUT5). If the delivery queue(s) seem to get clogged up and mail deliveries take a long time, it may be time to consider increasing the number of queues used for local mail deliveries. This is done by changing Fields \#241 and \#242 in the MAILMAN SITE PARAMETERS file (#4.3). This can be done dynamically and the filers will adjust themselves to the new parameters without the system being stopped (this may take a while). You can monitor the background filer activity with XMUT5.

### Mapped Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Recommendations for Routine Mapping is covered in Chapter 2, "Implementation and Maintenance," in this manual. Since each system is different, here are some hints for getting a set of mapped routines that more closely matches a site's needs.

- Run a process that reports on system activity if possible and use this report as a guide. Make sure you run it over a long enough time period to get a representative sample.
- If you know that you have a lot of network activity try mapping more XMC\*, XML\*, XMR\*, and XMS\* routines. If you are running TCP/IP MailMan the most important network mail routines to map are XMLTCP and XMRTCP.
- If you have a lot of message and response deliveries, map XMAD\*.
- If you have a lot of applications that call MailMan, map XMB\*, XMD\*, and XMG\*.

# MailLink Program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The REMOTE USER DIRECTORY file (#4.2997) contains a list of names and addresses of remote users. Input to this file is originated from a NOAVA or a WANG e-mail system file. WANG e-mail consists of most VA Central Office users, VBA users and NCS field station users. The NOAVA e-mail system is UNIPLEX. UNIPLEX is a UNIX server-based e-mail system and currently has approximately 1400 users in VACO.

When the NOAVA or WANG e-mail directories have updates, the new updated file is sent to FORUM system users. Upon receiving the updated file, the MailLink program is then invoked to convert the NOAVA/WANG directory into the REMOTE USER DIRECTORY file (#4.2997).

The steps for setting up the system to convert the NOAVA/WANG directory and update the REMOTE USER DIRECTORY file (#4.2997) are:

1.  Set Up Host File Server Entries.

Use the following information to set up Host File Server entries in the DEVICE file (#3.5).

> <span id="_Toc147217315" class="anchor"></span>Figure 35. NOAVA/WANG directory: Sample Host File Server entries in the DEVICE file (#3.5)

NAME: HFS-NOAVA-DIR \$I: NOAVA.DIRECTORY

ASK HOST FILE: <span class="mark">NO</span> ASK HSF I/O OPERATION: <span class="mark">NO</span>

MARGIN WIDTH: <span class="mark">0</span> FORM FEED: <span class="mark">\#</span>

PAGE LENGTH: <span class="mark">99999</span> BACK SPACE: <span class="mark">\$C(8)</span>

SUBTYPE: C-OTHER TYPE: HOST FILE SERVER

FORCED QUEUING: <span class="mark">NO</span>

NAME: HFS-WANG-DIR \$I: WANG.DIRECTORY

ASK HOST FILE: <span class="mark">NO</span> ASK HFS I/O OPERATION: <span class="mark">NO</span>

MARGIN WIDTH: <span class="mark">0</span> FORM FEED: <span class="mark">\#</span>

PAGE LENGTH: <span class="mark">99999</span> BACK SPACE: <span class="mark">\$C(8)</span>

SUBTYPE: C-OTHER TYPE: HOST FILE SERVER

FORCED QUEUING: <span class="mark">NO</span>

19. Load the Remote NOAVA/WANG directory.

Start the Remote MailLink Program and run the Load Remote VACO (Wang/Noava) Directory option, as shown below:

> <span id="_Toc147217316" class="anchor"></span>Figure 36. NOAVA/WANG directory: Start the Remote MailLink Program

Setting up programmer environment

Terminal Type set to: <span class="mark">C-VT100</span>

Select OPTION NAME: <span class="mark">XMMGR-DIRECTORY-MAIN \<Enter\></span> remote MailLink Directory Menu

Select Remote MailLink Directory Menu Option: <span class="mark">?</span>

Enter/Edit Directory Request Flags by Group

Group Mail Directory Request

List Mail Directory Request Flags by Group

Load Remote VACO (Wang/Noava) Directory

Remote Directory from all Domain

Request Mail Directory from a Single Domain Server

Enter ?? for more options, ??? for brief descriptions,

?OPTION for help text.

Select Remote MailLink Directory Menu Option: <span class="mark">LOAD \<Enter\></span> Remote VACO (Wang/Noava) Directory

You are about to load a file containing a list of names and addresses into your Remote User Directory (file \#4.2997). This file originated either from a Noava System or a Wang System. Choose the correct file. We will check it some for format.

Enter either HFS-WANG-DIR or HFS-NOAVA-DIR: HFS-NOAVA-DIR// <span class="mark">\<Enter\></span>

Do you want your job queued? (Answer YES or NO) NO// <span class="mark">\<Enter\></span>

Before the update occurs entries older than 90 days in the directory are deleted if they were automatically filed by this procedure. Manually entered entries are deleted if they haven't been used for at least 2 years.

Users are informed that an update is occurring if they are using MailLink Help Options, but are allowed to continue.

Are you sure you want to do this (Answer 'YES/NO'): NO// <span class="mark">Y</span>

Answer 'YES' if you mean "YES". All other responses mean 'NO'.

The first file to be processed is for the KERN7\$:\[XMUSER\]NOAVA.DIRECTORY.

Enter '^' to skip this portion of the process.

The following string was read from the line of KERN7\$:\[XMUSER\]NOAVA.DIRECTORY

Is this correct ? NO// <span class="mark">Y</span>

Killing off old AUTOMATIC entries for this code (1B).

. . . . . . . . . . . . . . . . . . . . . .

Starting load

. . . . . . . . . . . . . . . . . . . . . .

Task Complete . . . . .

Select Remote MailLink Directory Menu Option: <span class="mark">\<Enter\></span>

20. Obtain Remote User Information.

The Remote User Directory is now updated and ready for mail access. The following is a captured session of how to obtain remote user information via user's location, mail code, or last name at MailMan's "Send mail to:" prompt:

> <span id="_Toc147217317" class="anchor"></span>Figure 37. NOAVA/WANG directory: Obtaining remote user information

Send mail to: <span class="mark">?</span>

Enter the name(s) of the recipient(s) of this message in any of the following formats:

Lastname,first for a user at this site

LASTNAME,FIRST@REMOTE-SITE for a user at another site

G.\<GROUP-NAME\> for a group of users

Prefix any user address with; I: to send Information Only

C: to send Carbon Copy

PLEASE ENTER '??' FOR DETAILED HELP

Want user information? NO// <span class="mark">\<Enter\></span>

Want Mail Group information? NO// <span class="mark">\<Enter\></span>

Want Domain information? NO// <span class="mark">\<Enter\></span>

The following example shows that a "YES" answer at the "Want MailLink Help? NO//" prompt allows you to enter the remote user's location:

> <span id="_Toc147217318" class="anchor"></span>Figure 38. NOAVA/WANG directory: Entering remote user's location

Want MailLink Help? NO// <span class="mark">Y</span>

Enter LASTNAME, Mail Code or part of LOCATION (one word only): <span class="mark">VBA</span>

1 VBA LYST

2 VBA XMUSER ONE VBA DETROIT

3 VBA XMUSER TWO VBA SAN JUAN

4 VBA XMUSER THREE C.USER VBA MANILLA

5 VBA XMUSER FORU VBA CLEVELAND

6 VBA XMUSER FIVE VBA TECHWORLD

TYPE '^', TO STOP, OR

CHOOSE 1-6: <span class="mark">4</span>

LAST NAME: XMUSER FIRST NAME: THREE

REST OF NAME: C.USER MAIL CODE: 055A

EXTENDED MAIL CODE: SECT CHIEF AUTH LOCATION: VBA MANILLA

NETWORK ADDRESS: THREE.C.USER.XMUSER@VACOWMAIL.VA.GOV

DATE ENTERED:55752 DATE LAST USED: AUG 1991

Want MailLink Help ? NO// <span class="mark">Y</span>

> <span id="_Toc147217319" class="anchor"></span>Figure 39. NOAVA/WANG directory: Example showing only the mail code being entered for a remote user

Enter LASTNAME, Mail Code or part of LOCATION (one word only): <span class="mark">05</span>

1 055A XMUSER SIX Y VACO

2 05A2AN XMUSER SEVEN A VACO

CHOOSE 1-2: <span class="mark">1</span>

LAST NAME: XMUSER FIRST NAME: SIX

REST OF NAME: Y MAIL CODE: 055A

EXTENDED MAIL CODE: 055A LOCATION: VACO

NETWORK ADDRESS: SIX.XMUSER@VACOWMAIL.VA.GOV

DATE ENTERED:55752 DATE LAST USED: AUG 1991

Want MailLink Help ? NO// <span class="mark">Y</span>

> <span id="_Toc147217320" class="anchor"></span>Figure 40. NOAVA/WANG directory: Example displaying information using the user's last name

Enter LASTNAME, Mail Code or part of LOCATION (one word only): <span class="mark">XMUSER</span>

1 VBA XMUSER ONE VBA DETROIT

2 VBA XMUSER TWO VBA SAN JUAN

3 VBA XMUSER THREE C.USER VBA MANILLA

4 VBA XMUSER FORU VBA CLEVELAND

5 VBA XMUSER FIVE VBA TECHWORLD

CHOOSE 1-2: <span class="mark">5</span>

LAST NAME: XMUSER FIRST NAME: FIVEA

MAIL CODE: 20M21D EXTENDED MAIL CODE: 20M21D

LOCATION: VBA TECHWORLD

NETWORK ADDRESS: FIVE.XMUSER@VACOWMAIL.VA.GOV

DATE ENTERED:55752 DATE LAST USED: AUG 1991

Want MailLink Help? NO// <span class="mark">\<Enter\></span>

Send mail to: <span class="mark">XMUSER</span>

1 VBA XMUSER ONE VBA DETROIT

2 VBA XMUSER TWO VBA SAN JUAN

3 VBA XMUSER THREE C.USER VBA MANILLA

4 VBA XMUSER FORU VBA CLEVELAND

5 VBA XMUSER FIVE VBA TECHWORLD

CHOOSE 1-2: <span class="mark">4 \<Enter\></span> via VACOWMAIL.VA.GOV (Queued)

And send to: ..<span class="mark">\<Enter\></span>

Mail forwarded

Select MESSAGE Action: <span class="mark">IGNORE</span> (in IN basket)// <span class="mark">\<Enter\></span>

# Multimedia MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan only exports MailMan options, routines, and files that allow it to interface with the Veterans Health Information Systems and Technology Architecture (VistA) Imaging Software; however, MailMan does *not* export the VistA Imaging software. Therefore, do *not* attempt to use the Imaging features in MailMan unless your facility has fully implemented the Imaging software.

### Historical Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An experiment was tried to see if we could deliver a text message and point it at entries in the Imaging software, the results were successful. We used a workstation running FTP, connected to the Novell File Server.

We sent a mail message across the network using the normal channel. We added two new Message Protocol Data Units (MPDUs) to the normal set. In the first MPDU the sender indicated to the receiver that there was a Binary Large OBject (BLOB). In the second MPDU the receiver indicated acceptance of the BLOB and gave directions on how to deliver the BLOB. The BLOB was delivered via a separate background process that accessed the BLOB from the Novell File Server via an FTP get transaction, and then did an FTP put transaction to send the file to the remote VAX.

This was successful but there were a couple of problems with it. The first problem was that the PC-FTP software would frequently get hung up and require manual intervention before it would work properly again. A user would have to reset or reboot the PC from its console. Another problem has been that the process forked off on the VAX to deliver the BLOBs in background never "saw" an error occur, especially with the initial FTP get transaction. The solution to this problem had to be tested.

We then established our first alpha test site for Multimedia Mail and had consistent problems with this set up. We investigated the alternative of using some feature of the Novell software instead of using FTP to get files from the Novell File Server. NFS quickly came up and seemed to have the right mix of features.

### Analysis of Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ultimately, the process needs to do one thing. It needs to take a file on one system and send it to another system. The file's location should be transparent to the process. The process we are currently using was used because we had it and it worked under the limited circumstances.

The idea of having to FTP to a system that is on our Local Area Network (LAN) means that the process becomes more complex from the standpoint of both software and management. Both machines *must* be configured to be able to contact each other. The actual files *must* be moved twice, first from the file server on the LAN into the VAX, then they *must* be FTP'd again to the remote system. Another step is also required; the deleting of the file from the local VAX's temporary storage location where it was stored after the FTP "get" to the Novell server.

The idea that attracted the most attention was the idea of using NFS. This was attractive for a number of reasons. There is a high degree of probability that NFS will be running at all PC sites and is not a high extra cost additional capability for Novell LANs. It is a solution that will be workable at all VistA sites, VAXs and PCs. The plan is to acquire TCP/IP capability for 486 sites, which will probably be in the form of a TISC box running Ultrix. NFS is something of an industry standard. For the VAX systems, it offers the ability to access disks that are actually located on Novell servers transparently (as though they are actually on disks mounted on the VAX itself). Compare the scenarios below with the description of how things worked with the prototype:

This part is the same.

We sent a mail message across the network using normal channels. To the normal set of MPDUs we added new ones. In the first MPDU, the sender indicated to the receiver that there was a BLOB. In the second MPDU, the receiver indicated acceptance of the BLOB and gave directions on how to deliver the BLOB.

This part is much simpler—about 60% less work (only one FTP and no files deleted).

The BLOB was delivered via a separate background process that does an FTP put transaction to send the file to a VAX at the remote location the message was sent to.

In addition to the elegance of the second solution compared to the first, and the status of NFS as an industry standard, there is the additional feature that the second solution is possible on the configurations being tested for the 486 sites, so that they can have TCP/IP capability. It is also better because it offers some compatibility to the NOAVA systems that may be put in sites, as NOAVA Gateways systems running NFS.

It is also attractive because it can allow file sharing from the VAX. For instance, development and support staff could store only current versions of VistA software on a Juke Box on the Novell server.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When using an imaging workstation, a user can view images that are linked to a mail message on a second screen. This works using standard calls to the Application Programmer Interface (API) of the Imaging software. Images are brought off of a file server on the Local Area Network (LAN) via Ethernet and displayed. Network transmissions of messages are performed from a platform that has both CFS capabilities and TCP/IP. Images are delivered off of the file server that is on the LAN into a directory that is mounted (via NFS) onto this platform, again by a call to the Imaging Application Programmer Interface (API).

The hardware relationships are:

- Each is DPP'd to the same M database. At least one directory that is known on the network platform (if it is a VAX) as NFA0: is mounted via NFS client software onto it from the file server, which is running NFS server software. This directory appears as a logical device. It has two subdirectories that MailMan uses during network transmissions. The first is called NFA0:\[export.mail\] and is where the Imaging API places files that MailMan has indicated via a call that it needs to send to a remote system. The second, called NFA0:\[import.mail\], is where files are received.
- The network transmission works by sending a message first. During the exchange of message protocol data units, information is exchanged about the Binary Large OBject (BLOB) that is going to be sent via FTP. The receiver indicates the IP address to send the message to and the directory to put it in. The sender then constructs a series of commands that will access the FTP software running on that machine and stores it in a file that can be executed. A background process in M (XMRTCP), polls this file every few seconds and when it sees an entry, it makes a request to the imaging API to move the appropriate image into the export directory. When the image is in the export directory, the aforementioned file is executed and the image is FTP'd to the receiver of the mail message. The process that starts XMRTCP *must* have the correct UIC and access privileges.

There are two basic parts to a message as defined in the TCP/IP SMTP standard:

- Header—Includes the addresses of the recipients, subject, date originated, and other qualities of the message
- Body—Originally, the body of the message had only one part, the text; however, as electronic mail evolved, the need to make the body of the message more flexible was realized. The body of a message can contain more than one body part. Multimedia Electronic Mail has the ability to include body parts other than text in a message. Any bit-mapped data part can exist in the message body. It is referred to as a Binary Large OBject (BLOB).

### Non-textual BLOBs in Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BLOBs exist in messages as pointers to the IMAGE file (#2005). In order to attach a BLOB to a message, it *must* first exist in this file. Each entry in the IMAGE file (#2005) *must* have the data necessary for it to be found and used by the system. MailMan uses calls to the VistA Imaging software in order to manipulate these non-textual body parts. Entries in the IMAGE file (#2005) are looked up, displayed, and moved to a disk drive where they can be transmitted using FTP by calls to the VistA Imaging software.

As implemented in MailMan Version 8.0, BLOBs can be attached to a message. To do this, an entry is found or created in the imaging database for the BLOB part of the message body. The context of the entry includes the software that can be used to display it. It is therefore very object oriented in the classical sense. The Imaging database is being tested concurrently with MailMan. It can also be distributed, but agreements have not yet been established. These BLOBs are stored on any file server that DOS talks with on the local area network.

A message with a BLOB attachment can be sent to any user but the BLOB parts cannot be read unless the user is at the correct terminal. He is then informed of the viewable BLOB part and is told to read it from a terminal that he can display them on. The standard terminal for imaging, which is also the one required in this case, consists of two PCs. One runs MSM (displaying the message header and text). The other is a display device off the network with a high resolution VHF monitor.

A message with a BLOB is created using a special option that is locked with a key that will be assigned only to some users. The user sends the message as if he were using the normal Send option of MailMan. However, he is first queried for BLOBs, which *must* already exist in the appropriate Imaging database file. He then finishes the message by adding text to it, addressing it, and transmitting it.

### Sending and Receiving BLOBs Across a Network

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a network capability is added, complexity increases. Images have been transmitted across a standard X.25 network. They usually take from 7 to 15 minutes to be sent this way. Adding a very high speed channel that is capable of transmitting images in less than a minute makes the system really impressive. In both cases, it is necessary to make the system as efficient as possible. Our second pass at making this work included a Network File System (NFS) capability. This allowed us to perform only one FTP to get an image from Site A to Site B. The first scenario tested required at least two, one to get the file off of the LAN and a second to put the file onto the remote machine. NFS uses half the time it took to deliver images previously.

During the sending process of a message, a system check is made to see if it already exists and if so, the message is not retransmitted. The same occurs for BLOBs. If a BLOB is already on file, it is not retransmitted. The transmission of the BLOB takes place separately from the message header and the text. If a user tries to read the message before the BLOB(s) has been attached to it, he is told that this is the case and that he should re-read it later. At an imaging workstation the user is asked which BLOB to view.

MailMan Version 8.0 is also able to send a file, whether image, sound, or graphic, without attaching it to a mail massage. This is done using the TCP/IP service called FTP. As long as the file is accessible to MailMan, the user will be able to send it to a particular Internet Protocol (IP) address.

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following *must* be running for Multimedia MailMan to function properly:

- Local Mail Reading
- Network Transmissions (Sending and Receiving)

### Local Mail Reading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Imaging *must* be installed on both the PC workstation and the main machine.
- The Novell server *must* be operational.
- The C-IMPC terminal type *must* be associated with the PC workstation at signon.
- MailMan *must* be installed on both the PC workstation and the mail machine.
- Globals *must* be translated properly from the mail machine to the PC workstation.
- DDP *must* be running between the PC workstation and the main machine.

### Network Transmissions (Sending and Receiving)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The NFS drive *must* be mounted.
- TCP/IP *must* be running on the correct node.
- MailMan *must* be enabled for TCP/IP sending and receiving.
- The destination *must* be "reachable" by TCP/IP for both mail delivery and FTP.
- Secondary network protocol stack (e.g., Frame Relay) *must* be operational, if used.
- The M routine XMRTCP *must* be running on the TCP/IP node.
- Imaging *must* be moving images onto the export/mail directory of the NFS drive.
- The DOMAIN file (#4.2) of the remote domain *must* be set up for TCP/IP transmissions.
- The MAILMAN SITE PARAMETERS file of the receiving site *must* have the correct data in the following fields.
- FTP ADDRESS FOR BLOB RECEIVE
- FTP PASSWORD
- FTP USERNAME
- FTP RECEIVE NETWORK LOCATION (FREE TEXT pointer to the NETWORK LOCATION file \[#2005.2\])
- FTP RECEIVE DIRECTORY

## Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use Multimedia MailMan, you *must* install the VistA Imaging software.

### Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan running across TCP/IP channels as a peer to other SMTP mail systems has been described in an article presented by the author in the 1993 M Technology Association meeting in Washington D.C. and published in the proceedings to that meeting. An addendum to that article that describes how to obtain the software on VAX hardware is available from the author. That addendum has been used by both the VA and the Smithsonian Institute to establish TCP/IP mail connectivity to the Internet.

MailMan *must* send and receive mail on a TCP/IP channel in order to operate in Multimedia mode.

After the directory and subdirectory are established, entries should be made in the NETWORK LOCATION file (#2005.2) for the Import directory. This will be where the IMAGE file (#2005) will be located first (before it is moved to a permanent location). The Imaging API needs to know this because the objects in the IMAGE file (#2005) will point at this NETWORK LOCATION file (#2005.2). If it is *not* properly set up, the BLOBs will *not* be displayed.

The following are examples of how to set up both network locations in the NETWORK LOCATION file (#2005.2). The physical reference should be the name of the Novell disk that is mounted via NFS on the VAX, as it would be referenced from DOS as U:IMPORT\MAIL. This may vary from site to site.

<span id="_Toc147217321" class="anchor"></span>Figure 41. Multimedia MailMan—Setting up network locations in the NETWORK LOCATION file (#2005.2)

NETWORK LOCATION: <span class="mark">IMPORTMAIL</span> PHYSICAL REFERENCE: <span class="mark">U:\IMPORT\MAIL</span>

TOTAL SPACE IN KB: <span class="mark">9999999</span> SPACE USED IN KB: <span class="mark">1111111</span>

FREE SPACE IN KB: <span class="mark">8888888</span> OPERATIONAL STATUS: <span class="mark">ONLINE</span>

STORAGE TYPE: <span class="mark">MAGNETIC</span>

NETWORK LOCATION: <span class="mark">EXPORTMAIL</span> PHYSICAL REFERENCE: <span class="mark">U:\EXPORT\MAIL</span>

TOTAL SPACE IN KB: <span class="mark">9999999</span> SPACE USED IN KB: <span class="mark">1111111</span>

FREE SPACE IN KB: <span class="mark">8888888</span> OPERATIONAL STATUS: <span class="mark">ONLINE</span>

STORAGE TYPE: <span class="mark">MAGNETIC</span>

### Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data used by the sender and receiver *must* be recorded in the MAILMAN SITE PARAMETERS file (#4.3).

| Field Name                   | Description                                                                                                                                                                                                                      |
|------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FTP RECEIVE DIRECTORY        | This field stores the information passed from the receiver to the sender about where to put the file that is coming. The receiver can dynamically control where the images will be received.                                     |
| FTP ADDRESS FOR BLOB RECEIVE | This field contains an IP address so the receiver can dynamically control the machine that the sender will connect to when it sends the image.                                                                                   |
| FTP RECEIVE NETWORK LOCATION | This field contains the name of the entry in the NETWORK LOCATION file that corresponds to the FTP RECEIVE DIRECTORY field so that the entry that is created in the IMAGE file to represent the BLOB can be found and displayed. |
| FTP USERNAME                 | This is a string that represents the username that the FTP process uses in order to log into this system.                                                                                                                        |
| FTP PASSWORD                 | This is the string that represents the login that the sender will have to use in order to log into the system via FTP. The receiver can change security usernames and passwords at will.                                         |

## Installation of the Imaging Software on the Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                        |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/101.png) | NOTE: The VistA Radiology software *must* be installed on your system to store the scanned images. |

- You will need to use the SYSGEN option to set up the translation tables correctly. The XMULTI configuration is a good starting point. You need to translate the following globals to your VistA M Server: D\*, M\*, R\*, X\*, %ZIS\*
- You will need to edit the translation tables to change the "translation to" for data and locks to your VistA system. Your workstation's volume set name is "ITA", so you will not need to change the "translation from".
- With the globals translated, you will need to edit your Kernel system parameters to include ITA as a volume set name. You will need to add ITA to the DEVICE file (#3.5). You will also need to have a device type IMP and subtype C-IMPC. These can be taken care of in the MailMan inits.
- You will need to run MAGINIT to initialize the imaging globals on the server.
- We will have to send you the Radiology inits for imaging separately. This is needed to run the scanner, not to test Multimedia MailMan.
- You *must* edit the MAILMAN SITE PARAMETERS file (#4.3), MAILMAN RECEIVE DISK/VOL field to contain the driver letter used by your FTP server to address your Novell server, for example, U:.
- You *must* edit the FTP BLOB DIRECTORY field in the DOMAIN file (#4.2) to contain the directory name where images will be stored on your Novell File Server (e.g., IMAGE). You *must* be sure that this directory exists and is accessible (READ, WRITE, MODIFY, DELETE, etc.) by the FTP server.
- You *must* edit the FTP BLOB IP ADDRESS field in the DOMAIN file (#4.2) to contain the Internet Protocol (IP) address of your FTP server. Format is: xx.x.x.xx
- You may have to set up an option for Multimedia Message Send under the XMUSER menu, ITEM: XMBLOB.
- You will need to set the IMAGING SITE PARAMETERS NAME field to BIRMISC, and the INITIAL LOCATION to A.
- Imaging Workstation M software can be started with DEMO2.BAT.
- You will need to edit the NETWORK LOCATION file (#2005.2). In the .01 field, you will need the logical name of the Novell directory containing Image files. We usually use MAG1, MAG2, etc. You will need one entry for each drive and directory. The Physical Location field contains the full PATH to the directory and ends with a slash, For example:

U:\IMAGE\\

- You will need to edit the NETWORK LOCATION file (#2005.2) to point to the above NETWORK LOCATION file (#2005.2).

### How to Install the Network File System (NFS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for files from the Novell File Server to be sent from the CPU with the FTP service across the IDCU, a directory is mounted onto that CPU using NFS. After it is NFS mounted, the Novell directory is seen as though it is on this CPU. Instructions for mounting an NFS drive differ from implementation to implementation. A sample setup is shown in Figure 42.

On the File Server—A directory *must* be created that will be NFS mounted onto the FTP capable host. This directory should have the following subdirectories. The U drive is used as an example:

u:\import\mail

u:\export\mail

On the FTP capable node of the host, where XMRTCP will be started—The following needs to be completed:

- A file needs to be set up that maps VMS users on the foreign system:

NFS GENERIC.UIDS FILE FOR *nnn*VA *mm*/*dd*/*yyinitials*

- Define symbolic names for UIDs and GIDs on the remote server:

VistA symbolic for user on the remote server

IRM symbolic for group on the remote server

- Define UIDs and GIDs for the VMS UICs and account names.

Each VMS account can be assigned a single UIC and up to 10 GIDs. VistA and DSMIMAGE are VMS usernames being mapped to the symbolic UID above.

|                                                   |                                                   |
|---------------------------------------------------|---------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/102.png) | CAUTION: Be careful! These may be case sensitive. |

- An NFS drive *must* be mounted. VMS commands to mount the NFS file.

|                                                   |                                                                                                                                                 |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/103.png) | NOTE: Some parameters are case-sensitive (e.g., the directory on the remote disk). All lowercase is more likely to work than all uppercase. |

In the example below, "IMAGES" is a logical name assigned to the UIDS file (IMAGES.UIDS) and to the TCP/IP address (nnn.nnn.nnn.mmn). If you use the generic UIDS file, substitute the real IP address for IMAGES:

<span id="_Ref138565135" class="anchor"></span>Figure 42. Multimedia MailMan—Sample script for mounting an NFS drive on a VAX system

SET PROC/PRIV=ALL

SET PROC/PRIV=NOBYPASS

SET COMMAND twg\$tcp:\[nfsclient\]\*.cld

NFSMOUNT NFA0: IMAGES "/sys/imagenfs"

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/104.png) | NOTE: Using NFS on a VAX means that files are *not* allowed to be written on top of an already existing file, and so there will *not* be version number problems with files saved on the NFS drive. If the file already existed in DOS, NFS would try to rename it. Therefore, before installing the new routines, delete the file that is to be replaced to prevent naming problems. |

#### Set up Example for VMS Users

The example displays proper set up for VMS users so that a remote site can send Images/BLOBs by FTP to your site. To properly complete this setup for VMS Users, username and password *must* be entered into the MAILMAN SITE PARAMETERS file (#4.3).

|                                                   |                                                                                                                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/105.png) | NOTE: UIC and Default values *must* be the same as DSMMGR where \[61,n\] is the case. Privileges are very restricted. There are no access restrictions from the remote FTP. |

<span id="_Toc147217324" class="anchor"></span>Figure 43. Multimedia MailMan—Sample Setup for VMS Users

Username: MAILIMAGE Owner:

Account: UIC: <span class="mark">\[61,4\]</span> (\[MAILIMAGE\])

CLI: <span class="mark">DCL</span> TABLES: <span class="mark">DCLTABLES</span>

Default: KERN7\$:\[KERN7SUR\]

LGICMD: MAILIMAGE_LOGIN.COM

Flags: DisCtlY DisWelcome DisMail DisReport

Primary days: Mon Tue Wed Thu Fri

Secondary days: <span class="mark">Sat Sun</span>

No access restrictions

Expiration: (none) Pwdminmum: <span class="mark">6</span> Login Fails: <span class="mark">3</span>

Pwdlifetime: (none) Pwchange: (pre-expired)

Last Login: 27-APR-1993 15:49 (non-interactive)

Maxjobs: <span class="mark">0</span> Fillm: <span class="mark">150</span> BYTLM: <span class="mark">40960</span>

Maxaccjobs: <span class="mark">0</span> Shrfillm: <span class="mark">0</span> Pbytlm: <span class="mark">0</span>

Maxdetach: <span class="mark">0</span> BIOlm: <span class="mark">18</span> JTquota: <span class="mark">1024</span>

Prclm: <span class="mark">2</span> DIOlm: <span class="mark">18</span> WSdef: <span class="mark">600</span>

Prio: <span class="mark">4</span> ASTlm: <span class="mark">300</span> WSquo: <span class="mark">1000</span>

Queprio: <span class="mark">0</span> TQElm: <span class="mark">10</span> WSextent: <span class="mark">1500</span>

CPU: (none)

Authorized Priviledges:

GRPNAM GROUP TMPMBX NETMBX

Default Priviledges:

GRPNAM GROUP TMPMBX NETMBX

# MailMan Script Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Generalized Device Control and Communication Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are times when it is desirable or necessary for processes to talk to devices. Sometimes these devices have software running on them and sometimes they do not.

Sometimes software needs to make decisions on-the-fly about what processes to perform, and in what order. MailMan provides a utility called the MailMan Script Processor that allows users to state a series of actions to take and to have them acted upon in a controlled fashion. It allows for events to be sensed and actions to take place. Also, for the first time there is a way for programmers to define their own scripts and to have them played out. This is an opportunity to define a series of actions that make up a process and to then invoke them as the opportunity offers itself.

## How to Invoke the Script Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set up the following variables in order to process a script:

| Variable | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| XMDIC    | The root of the array (of file) in which the script is located. |
| XMSCR    | Index number to the script to be played.                        |
| XMSCRN   | Name (FREE TEXT) of the script to be played.                    |

### Example Call

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The alert below (see Figure 44) is set up only if the lab device being examined has data for the user. It is queried by sending a string of 5 question marks and a checksum, and responds with either NAK (no data to transmit) or ACK (Yes, I have data). The device has been opened by the process before the code below. The script has been set up as one of many in advance.

There is also a script that similarly is invoked to pull in the data when the user is ready for it:

<span id="_Ref138565941" class="anchor"></span>Figure 44. Sample script—Code setting variables

;The script is set up in a FileMan compatible word processing field

;and we have moved it into a temporary global array for this event

S XMDIC="^TMP(""NAMESPACE"",\$J,"

;The particular index is entry number 22

;The name of the script is "Lab data is ready!"

S XMSCR=22,XMSCRN="Lab data is ready!"

;The script processor is called

;An alert is sent to the user if the lab data is ready

;ZZGET-LABDATA is an option that invokes the script that receives

; the data into the user's PC database.

D SCRIPT^XMC1 I ER W:'\$D(ZTQUEUED) !!,\*7,"Lab data is not ready!",!!

Q

The device takes a while to wake-up after it is opened; therefore, the first line of the script forces a 20 second wait.

The second line of the script is the request for the data.

The third line looks for the acknowledgment. If no acknowledgment comes within 15 seconds, it is assumed that the script is done and the script processor will quit with ER=1.

The fourth through seventh lines will then invoke the appropriate alert.

The script looks like this:

<span id="_Toc147217327" class="anchor"></span>Figure 45. Sample script—Alert

^TMP("NMSP",\$J,22,1,0)= W 20

^TMP("NMSP",\$J,22,2,0)= S "?????"\_NMSPSUM

^TMP("NMSP",\$J,22,3,0)= L \|ACK\|:15

^TMP("NMSP",\$J,22,4,0)= X S XQA(DUZ)=""

^TMP("NMSP",\$J,22,5,0)= X S XQAMSG="LAB data is ready!"

^TMP("NMSP",\$J,22,6,0)= X S XQAOPT="ZZGET-LABDATA"

^TMP("NMSP",\$J,22,7,0)= X D SETUP^XQALERT

### Mini out Subroutine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Transmission scripts are lists of script commands that are executed by the script processor for Network Mail transmissions in order when they are invoked. The command in a script that invokes a transmission script is the CALL; therefore, "C KERNEL" invokes a script that interfaces with the SMTP (Simple Mail Transfer Protocol) process using the Simple Communications Protocol (SCP). Transmission scripts are used most often to invoke a portion of a longer script that is used in many different domains.

The XMSUBEDIT option allows editing of the transmission script subroutine.

<span id="_Toc147217328" class="anchor"></span>Figure 46. Running the XMSUBEDIT option to edit a transmission script subroutine

1 W 1

2 S

3 Look UserID?

4 ISCDEV

5 L PASSWORD

6 S PROGRAM

7 L DESTINATION

8 X W XMHOST,\*13

9 LOOK \|CONNECTED\| LINE \|1DISCON \|

0 S

# MailMan Distribution List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan's DISTRIBUTION LIST file (#3.816) has entries that consist of names. Each name is associated with one or more domains. When a distribution list is entered into a mail group, MailMan delivers the message to all the entries it has linked to it. A distribution list is interpreted as a name to which the message will be delivered, at each of the associated domains in the established list.

For example, a distribution list whose name is G.SUPPORT and whose associated domains are FORUM.VA.GOV, EXAMPLEVAMC.VA.GOV and OIFO-REDACTED.VA.GOV will be sent (in addition to all other entities attached to the mail group) to the following:

<span id="_Toc147217329" class="anchor"></span>Figure 47. Sample distribution list (G.SUPPORT)

G.SUPPORT@FORUM.VA.GOV

G.SUPPORT@EXAMPLEVAMC.VA.GOV

G.SUPPORT@OIFO-REDACTED.VA.GOV

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A mail group allows you to send messages to a group of recipients without having to specify them individually by name. Whenever mail is repeatedly sent to the same list of recipients, users can save time by putting them in mail groups.

Users can set up a new mail group or add members to an existing group using the Mail Group Edit option, found under the Manage MailMan menu \[XMMGR\]. The user will be prompted for the following information:

| Prompt               | Usage                                                                                                                                                                         |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name and Description | Identifies this newly set up mail group.                                                                                                                                      |
| Member               | Member that will receive all mail addressed to the established mail group. Members can also be local and remote users, other mail groups or an established distribution list. |
| Type                 | Mail groups can be public, private or open.                                                                                                                                   |
| Organizer            | The organizer of a mail group is the user who set up the group.                                                                                                               |

### Members of Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Usage</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Local</td>
<td>Members that are individuals that use the local mail system.</td>
</tr>
<tr class="even">
<td>Member Group</td>
<td><p>A mail group can also be established as a member of other mail groups. More than one mail group can concurrently be members of the same mail group.</p>
<p>![](mailman-version-8-systems-management-guide/106.png) <strong>CAUTION: You can create an infinite loop by making a mail group a member of a mail group, if the first mail group is also a member of the second.</strong></p></td>
</tr>
<tr class="odd">
<td>Distribution List</td>
<td><p>Distribution Lists can be set up through the use of VA FileMan. A Distribution List has a name and a list of domains. If a Distribution List is a member of a mail group, and more than one may be, then the expansion of it will cause the message to be sent to the Distribution List Name at each of the domains in the list.</p>
<p>![](mailman-version-8-systems-management-guide/107.png) <strong>NOTE:</strong> Private Mail Groups <em>cannot</em> contain Distribution Lists.</p></td>
</tr>
<tr class="even">
<td>Remote</td>
<td>Members that are in none of the other categories.</td>
</tr>
</tbody>
</table>

Figure 48 and Figure 49 shows you how to create a MailMan distribution list and each domain within the list. It further displays the establishment and editing of mail groups, as well as adding new members using the Edit Distribution List option under the Manage MailMan menu \[XMMGR\]. This display shows actual system dialogue that can be used as a guide when establishing your own distribution lists.

### Creating a Distribution List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Group/Distribution Management menu is used to create a MailMan distribution list, as shown below:

<span id="_Ref138568820" class="anchor"></span>Figure 48. Using the Group/Distribution Management menu option—Sample user prompts

Select Manage MailMan Option: Group/Distribution Management

Select DISTRIBUTION LIST NAME: <span class="mark">PATCH DIST</span>

ARE YOU ADDING 'PATCH DIST' AS A NEW DISTRIBUTION LIST (THE 4TH)? <span class="mark">Y \<Enter\></span> (YES)

Select DOMAIN: GOLD.BIG-SITE.VA.GOV

ARE YOU ADDING 'GOLD.BIG-SITE.VA.GOV' AS A NEW DOMAIN (THE 1ST FOR THIS DISTRIBUTION LIST)? <span class="mark">Y \<Enter\></span> (YES)

Select DOMAIN: <span class="mark">BIG-SITE.VA.GOV</span>

ARE YOU ADDING 'FORUM.VA.GOV' AS A NEW DOMAIN (THE 3RD FOR THIS DISTRIBUTION LIST)? <span class="mark">Y \<Enter\></span> (YES)

Select DOMAIN: <span class="mark">DEMO.VA.GOV</span>

ARE YOU ADDING 'DEMO.BIG-SITE.VA.GOV' AS A NEW DOMAIN (THE 4TH FOR THIS DISTRIBUTION LIST)? <span class="mark">Y \<Enter\></span> (YES)

Select DOMAIN: <span class="mark">\<Enter\></span>

Select DISTRIBUTION LIST NAME: <span class="mark">\<Enter\></span>

### Editing a Distribution List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The distribution list can be edited using the Edit Distribution List option, as shown below:

<span id="_Ref138569369" class="anchor"></span>Figure 49. Using the Edit Distribution List option—Sample user prompts

Select Manage MailMan Option: <span class="mark">EDIT DISTRIBUTION LIST</span>

Select DISTRIBUTION LIST NAME: <span class="mark">PATCH DIST</span>

NAME: PATCH DIST// <span class="mark">\<Enter\></span>

Select DOMAIN: DEMO.BIG-SITE.VA.GOV// <span class="mark">REDACTED, MD \<Enter\></span> REDACTED.VA.GOV

ARE YOU ADDING 'REDACTED.VA.GOV' AS A NEW DOMAIN (THE 5TH FOR THIS DISTRIBUTION LIST)? <span class="mark">Y \<Enter\></span> (YES)

Select DOMAIN: <span class="mark">\<Enter\></span>

Select DISTRIBUTION LIST NAME: <span class="mark">\<Enter\></span>

The Mail Group Edit option allows you to enter or edit mail group members:

<span id="_Toc147217334" class="anchor"></span>Figure 50. Using the Mail Group edit option—Sample user prompts

Select Manage Mailman Option: <span class="mark">MAIL GROUP EDIT</span>

Select MAIL GROUP NAME: <span class="mark">ISC2 DIST</span>

ARE YOU ADDING 'ISC2 DIST ' AS A NEW MAIL GROUP? <span class="mark">Y \<Enter\></span> (YES)

NAME: ISC2 DIST // <span class="mark">\<Enter\></span>

Select MEMBER: <span class="mark">XMUSER,ONE</span>

ARE YOU ADDING 'XMUSER,ONE' AS A NEW MEM (THE 1ST FOR THIS MAIL GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Select MEMBER: <span class="mark">XMUSER,TWO</span>

ARE YOU ADDING 'XMUSER,TWO' AS A NEW MEM (THE 2ND FOR THIS MAIL GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Select MEMBER: <span class="mark">XMUSER,THREE</span>

ARE YOU ADDING 'XMUSER,THREE' AS A NEW MEM (THE 3RD FOR THIS MAIL GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Select MEMBER: <span class="mark">XMUSER,FOUR</span>

ARE YOU ADDING 'XMUSER,FOUR Y' AS A NEW MEM (THE 4TH FOR THIS MAIL GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Select MEMBER: <span class="mark">\<Enter\></span>

DESCRIPTION:

1\>THIS GROUP IS TIED TO THE DISTRIBUTION LIST.

2\>\<Enter\>

EDIT Option: <span class="mark">\<Enter\></span>

TYPE: <span class="mark">PU \<Enter\></span> public

ORGANIZER: XMUSER,ONE

Select AUTHORIZED SENDER: <span class="mark">\<Enter\></span>

ALLOW SELF ENROLLMENT?: NO <span class="mark">\<Enter\></span>

Select MEMBER GROUP NAME: <span class="mark">\<Enter\></span>

Select REMOTE MEMBERS: <span class="mark">XMUSER,FIVE@EXAMPLEVAMC</span>

ARE YOU ADDING 'XMUSER,FIVE@EXAMPLEVAMC' AS

A NEW MEMBERS - REMOTE (THE 1ST FOR THIS MAIL GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Select REMOTE MEMBERS: <span class="mark">\<Enter\></span>

Select DISTRIBUTION LIST: <span class="mark">PATCH DIST</span>

ARE YOU ADDING 'PATCH DIST' AS A NEW DISTRIBUTION LIST (THE 1ST FOR THIS MAIL GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Select DISTRIBUTION LIST: <span class="mark">\<Enter\></span>

You are now ready to send a message.

<span id="_Ref138492869" class="anchor"></span>Figure 51. Sending a message: Sample user dialogue

Select MailMan Menu Option: <span class="mark">S \<Enter\></span> Send a Message

Subject: TEST FOR THE DIST LIST

Enter the text of the message

1\><span class="mark">THIS IS A TEST.</span>

2\><span class="mark">\<Enter\></span>

EDIT Option: <span class="mark">\<Enter\></span>

Send mail to: XMUSER,ONE// <span class="mark">\<Enter\></span>

Select basket to send to: IN// <span class="mark">\<Enter\></span>

Send mail to: <span class="mark">ISC - SAN FRANCISCO BASED \<Enter\></span> 5 Local 1 Other Members 1 Distribution Lists:

XMUSER,ONE XMUSER,TWO XMUSERR,THREE XMUSER,FOUR XMUSER,FIVE Distribution List PATCH DIST

G.PATCH DIST@GOLD.BIG-SITE.VA.GOV

G.PATCH DIST@VER.GOLD.BIG-SITE.VA.GOV

G.PATCH DIST@FORUM.VA.GOV

G.PATCH DIST@DEMO.BIG-SITE.VA.GOV

G.PATCH DIST@REDACTED.VA.GOV

And send to: <span class="mark">\<Enter\></span>

Mail forwarded

Select MESSAGE Action: IGNORE (in IN basket)// <span class="mark">\<Enter\></span> Ignored

End of basket.

The DISTRIBUTION LIST file (#3.816) has entries that consist of names. Each name is associated with one or more domains. These domains are concatenated to the Distribution List names to form addresses of remote recipients (see Figure 51).

The following is an actual printout from FORUM of a Distribution List:

<span id="_Toc147217336" class="anchor"></span>Figure 52. Sample FORUM distribution list

NAME DOMAIN

----------------------------------------------------------------------

IRM EXAMPLEVAMC.VA.GOV

BALTIMORE.VA.GOV

BECKLEY.VA.GOV

BUTLER.VA.GOV

CLARKSBURG.VA.GOV

COATESVILLE.VA.GOV

# MailMan Validation Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VALIDATION NUMBER field in the DOMAIN file (#4.2) is used to make communications via Network Mail Transmissions more secure.

The VALIDATION NUMBER field is embedded with an initial value. To use this feature with a particular domain, proceed as follows:

<span id="_Ref138493289" class="anchor"></span>Figure 53. Sample validation numbers

Your Site = Domain "A" Other Site = Domain "B"

At Domain A At Domain B

DOMAIN NAME: DOMAINB DOMAIN NAME: DOMAINA

VALIDATION NUMBER: 98765432 VALIDATION NUMBER: 98765432

In this example (Figure 53), DomainA and DomainB agree on an input value in the VALIDATION NUMBER field of the DOMAIN file (#4.2), such as 98765432. At DomainA, this value is forced into the VALIDATION NUMBER field of the DOMAIN file (#4.2) at DomainB. Similarly at DomainB, the entry for DomainA is forced to contain the number 98765432 in the VALIDATION NUMBER field.

The field values *must* be coordinated to be entered at the same time. Otherwise, the values could cause either side to think a security violation has occurred.

|                                                   |                                                                                                                                                                                       |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/108.png) | NOTE: If either domain starts a transmission while only one site has entered a value in the VALIDATION NUMBER field of their DOMAIN file (#4.2), a security violation will occur. |

On each transmission, the validation numbers are exchanged and checked. If they are synchronized, the transmission will continue. If they are different, the sender, the receiver, or both will trigger the XMVALBAD bulletin. This bulletin will be sent to the members of the mail group(s) associated with the transmission attempt.

|                                                   |                                                                                                                                                          |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/109.png) | NOTE: Please be sure to establish that the XMVALBAD bulletin is associated with a mail group and that the mail group has at least one active member. |

Once validation numbers are checked and are synchronized, the receiver randomly generates a new validation number. This value is then passed to the sender. Both the sender and the receiver enter this new value into the VALIDATION NUMBER field of their respective DOMAIN files (#4.2).

Suppose DomainA receives a successful communication with a domain that has the correct validation number value, but is not really DomainB. The VALIDATION NUMBER field will be different on the actual DomainB. They will no longer have synchronization of their VALIDATION NUMBER fields and will not be able to transmit or receive messages from each other. Management is notified immediately that there has been a security violation. The sites will have to resynchronize the values in the VALIDATION NUMBER fields.

It is very unlikely that a validation number will be guessed, since they are eight digits in length and are constantly changing. It would take another mail system (specially contrived) to try and retry the connection.

|                                                   |                                                                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/110.png) | NOTE: The only other way for security to be compromised would be for an insider to "steal" and immediately use the stolen code. |

# Statistics in MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan Version 8.0 has the capability to record statistics that can help a systems manager to see how work is being done on his system and how good response time is for system users. There are statistics available for both local events and deliveries of Network Mail.

## Local Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Statistics are kept in half-hour intervals on those events most important in an electronic mail system.

- Deliveries of messages and responses made
- Number of messages and responses that remain undelivered
- Average response time (measured as how long it takes to delete or terminate a message)
- The last message number assigned during the interval
- The longest time any item has been waiting to be delivered
- The number of lines of a message and response text displayed or printed in half-hour intervals

In order to have these statistics recorded in the MESSAGE DELIVERY STATS file (#4.2998), they are recorded by the XMMGR-DELIVERY-STATS-COLL option that you *must* schedule once and only once. It reschedules itself to run every 30 minutes.

Average response times are recorded by making use of the Kernel Response Time Logging functionality. Response Time Logging *must* be turned on either by editing the MAILMAN SITE PARAMETERS file (#4.3) or by running MailMan's XMMGR-RESPONSE-TIME-TOGGLER option. This option turns on Response Time Logging and schedules a job 5 minutes later to turn off Response Time Logging. If you do *not* want to record everyone's response time constantly, running this option periodically (e.g., every half-hour or hour) will record response times for a random sample of users and is quite effective. In addition, the XMMGR-RESPONSE-TIME-COMPILER option *must* be run. It compiles the data from the %ZRTL global into half-hour intervals and places the results into the MESSAGE DELIVERY STATS file (#4.2998).

All of this can be reported using the options listed under the Local Delivery Management menu located under the Manage MailMan menu \[XMMGR\]. The options that contain the word "tabbed" in the title creates output that can be captured and used in a spreadsheet (e.g., Microsoft Excel).

## Network Mail Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On VMS systems, the following routine can be used to count users for statistics. It *must* be converted into a VMS COM file first, as shown below:

<span id="_Toc147217338" class="anchor"></span>Figure 54. Network Mail Statistics on VMS systems—USERS.COM file

S X="USERS.COM" O X UX

F I=0:0 S X=\$T(ZZZ^XMUSTCOM1+I) Q:I="" W X,!

C X

<span id="_Toc147217339" class="anchor"></span>Figure 55. Network Mail Statistics on VMS systems—XMUTCOM1 routine

\><span class="mark">ZP</span>

XMUTCOM1 ;(WASH ISC)/CAP-XMUSRCNT.COM / COUNT USERS ;12/4/93 11:48

;8.0T;MailMan-Test;Oct 05, 2002

ZZZ ;\$!USERS.COM

;\$! milt's special

;\$ set noon

;\$ ANS="N"

;\$ pur/nolog leeuser.log

;\$! del/nolog u1\*.tmp.\*,u2\*.tmp.\*

;\$! say " Scanning VMS interactive users..............."

;\$ SH USER/INTER/full/OUTPUT=U1.TMP

;\$! say " Scanning VMS batch users (ZSLOT) ............"

;\$ SH USER/BATCH/full/OUTPUT=U2.TMP

;\$ search/output=u11.tmp u1.tmp forum

;\$ search/output=u22.tmp u2.tmp bf

;\$ search/output=u222.tmp u22.tmp op\_/match=nor

;\$ APPEND U222.TMP U11.TMP

;\$ cnt=0

;\$ bfcnt=0

;\$ open/read a U11.TMP

;\$READ_LOOP: !read USERS.tmp and start extracting what we need

;\$ read/end=eof/error=error a line

;\$ if f\$extract(0,1,ans) .nes. "" then goto next_step

;\$! say line

;\$ next_step:

;\$ if f\$extract(1,2,line) .eqs. "BF" then bfcnt=bfcnt+1

;\$ cnt=cnt+1

;\$ goto read_loop

;\$ next_one:

;\$EOF: !end of file

;\$ close a

;\$ set ver

;\$ open/append a XMUSRCNT.sav

;\$ vmscnt=cnt-bfcnt

;\$ time_stamp=f\$time()

;\$ scnt=f\$string(cnt)

;\$ svmscnt=f\$string(vmscnt)

;\$ sbfcnt=f\$string(bfcnt)

;\$ usercnt="''scnt',''sbfcnt',''svmscnt',''time_stamp'"

;\$ write a "\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*"

;\$ write a time_stamp

;\$ write a " VMS logins = "'VMSCNT'"."

;\$ write a " VMS Batch jobs running = "'bfcnt'"."

;\$ write a " TOTAL Interactive and Batch users = "'CNT'"."

;\$ write a ''usercnt'

;\$ close a

;\$ purge/nolog leeuser.sav

;\$ delete/nolog U1\*.TMP.\*,U2\*.TMP.\*

;\$ dsm/envir=mgrmail/data="''usercnt'" ENUSER^XMUT5Q

;\$! submit/que=forum7_batch XMUSRCNT.COM

;\$ set nover

;\$ exit

;\$ERROR:

;\$ say "Error has occurred during processing."

;\$ SAY " "

;\$! goto eof

;\$exit

\>

## Network Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Mail statistics are much simpler. In the MESSAGE STATISTICS file (#4.2999), statistics are kept on a monthly basis. The data recorded there includes the number of characters, lines, and messages that have been sent and received.

# P-Message Device Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter shows you how to define devices that can be used to redirect reports and other outputs into mail messages instead of printers.

## P-Message Definitions for the Workstation Environment Running MSM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the regular P_Message Device and Terminal Type that needs to be defined on the VAX for use by VistA terminals, another set has to be defined for use by workstations running MSM.

<span id="_Toc147217340" class="anchor"></span>Figure 56. Terminal Type: For Operating from a Workstation Running MSM or a VAX

NAME: <span class="mark">P-MESSAGE-HFS (MSM)</span> RIGHT MARGIN: <span class="mark">255</span>

FORM FEED: <span class="mark">\#</span> PAGE LENGTH: <span class="mark">256</span>

BACK SPACE: <span class="mark">\$C(8)</span>

OPEN EXECUTE: S XMREC="R X#255:1"

CLOSE EXECUTE: U IO:(::0) D ^XMAPHOST,READ^XMAPHOST S X=\$ZOS(2,"XM"\_DUZ\_".DAT") K XMIO Q

DESCRIPTION: Special Terminal Type used only for device: P-MESSAGE-HFS

<span id="_Toc147217341" class="anchor"></span>Figure 57. Device: For operating from a Workstation running MSM or a VAX

NAME: <span class="mark">P-MESSAGE-HFS (MSM)</span> \$I: <span class="mark">51</span>

ASK DEVICE: <span class="mark">YES</span> ASK PARAMETERS: <span class="mark">NO</span>

FORCED QUEUING: <span class="mark">NO</span>

LOCATION OF TERMINAL: HFS (MSM) FILE =\> MESSAGE

LOCAL SYNONYM: <span class="mark">MAIL MESSAGE</span> MARGIN WIDTH: <span class="mark">255</span>

FORM FEED: <span class="mark">\#</span> PAGE LENGTH: <span class="mark">256</span>

BACK SPACE: <span class="mark">\$C(8)</span> OPEN PARAMETERS: <span class="mark">("XM"\_DUZ\_".DAT":"M")</span>

SUBTYPE: <span class="mark">P-MESSAGE-HFS</span> TYPE: <span class="mark">HOST FILE SERVER</span>

The Terminal Type and Device described below permits printing to mail messages on a VAX using a VistA terminal.

<span id="_Toc147217342" class="anchor"></span>Figure 58. Terminal Type: VAX only

NAME: <span class="mark">P-MESSAGE-HFS</span> RIGHT MARGIN: <span class="mark">255</span>

FORM FEED: <span class="mark">\#</span> PAGE LENGTH: <span class="mark">256</span>

BACK SPACE: <span class="mark">\$C(8)</span>

CLOSE EXECUTE: S XMREC="R X#255:1" U IO:DISCONNECT D ^XMAHOST,READ^XMAPHOST K XMIO Q

DESCRIPTION: Special Terminal Type used only for P-MESSAGE-HFS device.

<span id="_Toc147217343" class="anchor"></span>Figure 59. Device: VAX only

NAME: P-MESSAGE-HFS \$I: XMHFS.DAT

ASK DEVICE: <span class="mark">YES</span> ASK PARAMETERS: <span class="mark">NO</span>

FORCED QUEUING: <span class="mark">NO</span> LOCATION OF TERMINAL: <span class="mark">HFS FILE =\>MESSAGE</span>

LOCAL SYNONYM: <span class="mark">MAIL MESSAGE</span> MARGIN WIDTH: <span class="mark">256</span>

FORM FEED: <span class="mark">\#</span> PAGE LENGTH: <span class="mark">256</span>

BACK SPACE: <span class="mark">\$C(8)</span> SUBTYPE: <span class="mark">P-MESSAGE-HFS</span>

TYPE: HOST FILE SERVER

|                                                   |                                                                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/111.png) | NOTE: P-MESSAGE assumes that if there are more than 250 consecutive null lines in a printout, that the end of file (EOF) must have been reached. |

# Intercepting Twix from the PCTS System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PCTS System Setup and Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Personal Computer Terminal System (PCTS) allows direct, immediate communications between VA Central Office (VACO) and field stations, including medical centers, OIFOs, and other facilities. PCTS is usually set up so that communications come in to the facility and are immediately printed. They are sent out from the facility similarly arriving elsewhere. A 486 PC is normally used for this purpose and it runs software that is used exclusively for this purpose.

A large number of users can be supported with such a powerful machine but the printed word is not as efficiently distributed as electronic mail. MailMan 8.0 allows an M System running MailMan to intercept this communication data and put it into mail messages. Conversely, messages can be routed into the PCTS system simply by addressing them to a user at the VHA.DMIA domain (which is a dummy name) exclusively set up for this purpose. Now the extra PC can be used more effectively and efficiently while a very small load is placed on a node of the VistA System.

### How the VistA PCTS Twix Interceptor Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two parts to MailMan that allow VistA to send and receive Twix(s).

1.  The XM option guides the user through the process of constructing an appropriately formatted mail message.
2.  A Sender/Receiver is queued from TaskMan to run periodically (e.g., half-hour to every hour).

This XM option guides the user through the process of constructing an appropriately formatted mail message in a structured format. The Sender will be able to use this structured format to extract data fields that are needed when it sends the message (the Twix). The user of this option *must* be somewhat familiar with the terminology and values of the data fields that are requested, such as the Destination RI (routing indicator) and Destination to Line fields.

The Receiver functions by continuously running a process that looks for data coming down the line to it. When data is detected, the line is opened and each Protocol Data Unit (PDU) is interpreted, and messages are exchanged.

The Sender is invoked by the Receiver when it receives a PDU that indicates that the other side is ready to receive data. When this occurs, the Sender checks the queue for the VAH.DMIA domain. If any messages are in the queue for the VHA.DMIA domain, those messages are transmitted.

## Setup Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The overview of the setup is as follows:

- Set up the VHA.DMIA domain
- Set up option for transmitting queue and schedule it to run periodically
- Set up option for users to send a Twix
- Start receiver (add to start up procedure)

## Setting Up the VHA.DMIA Domain

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When setting up the VHA.DMIA domain, the line of the script text that says X W "PCTS RUCHxxx" should be edited so that RUCHxxx is your local routing indicator.

|                                                   |                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------|
| ![](mailman-version-8-systems-management-guide/112.png) | REF: The local routing indicator can be looked up in the *PCTS User Guide*. |

<span id="_Toc147217344" class="anchor"></span>Figure 60. Setting up the VHA.DMIA domain: Sample user dialogue and entries

NAME: <span class="mark">VHA.DMIA</span> FLAGS: <span class="mark">Q</span> PHYSICAL LINK DEVICE: MINIOUT

TRANSMISSION SCRIPT: <span class="mark">CONNECT</span>

TYPE: Simple Mail Transfer Protocol

PHYSICAL LINK / DEVICE: <span class="mark">MINIOUT</span>

NETWORK ADDRESS (MAILMAN HOST): <span class="mark">VHA.DM</span>

TEXT:

O H=VHA.DMIA,P=SCP

C MINI

L ogin:

S pcts

L CODE:

X W "PCTS RUCHxxx"

X D ^XMRPCTS

NOTES:

This script is used to connect up to the PCTS system to send and receive messages.

NETWORK NOTES:

This domain is used for PCTS communications.

### Schedule Option for Transmitting Queue to Run Periodically

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XMNET-TWIX-TRANSMIT option is queued to run periodically to transmit Twix(s). It should be scheduled to run every half-hour or every hour.

### Option for Users to Use to Send a Twix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XMNET-TWIX-SEND option is distributed with MailMan but it is *not* placed on a user's menu. It is up to the site manager to assign this option to those employees that he/she thinks should have this capability. If the ability is for site management, it should be put it on the XMMGR menu.

<span id="_Hlt448198183" class="anchor"></span>Glossary

|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BANNER               | A line of text with a user's name and domain, which is displayed to everyone who sends mail to the user.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| BSCP                 | Block Mode Simple Communications Protocol, a procedure used for message transmission with error checking.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| BULLETIN             | A form letter often triggered by a VA FileMan field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DEVICE               | A terminal, printer, modem, or other type of hardware or equipment associated with a computer. A host file of an underlying operating system may be treated like a device in that it may be written to (e.g., for spooling).                                                                                                                                                                                                                                                                                                 |
| DOMAIN               | A site for sending and receiving mail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| INITIALIZATION       | The process of setting variables in a program to their starting value.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| INPUT TRANSFORM      | An executable string of M code that is used to check the validity of input and converts it into an internal form for storage.                                                                                                                                                                                                                                                                                                                                                                                                |
| KEYWORD              | A reference name that calls a help frame when entered at a message prompt.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| LINE EDITOR          | This is VA FileMan's special line-oriented text editor. This editor is used for the word-processing data type.                                                                                                                                                                                                                                                                                                                                                                                                               |
| LOCAL                | The system that a user is currently signed on to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| LOG IN/ON            | The process of gaining access to a computer system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| LOG OUT/OFF          | The process of exiting from a computer system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MAIL BASKET          | Mail baskets provide a way of saving messages in a sorted fashion similar to a filing system. Mail baskets are created at the "Message action" prompt by typing in "S" to save, then the name you wish to call the basket. If the basket already exists, the message will be sent to it. If the basket does not exist, you will be asked if you want it created. Placing a message in a mail basket other than the IN or Waste baskets protects the message from being automatically purged when the IN BASKET PURGE is run. |
| MESSAGE-ID           | A message identifier that shows the time of transmission, the message number and the domain name of the message.                                                                                                                                                                                                                                                                                                                                                                                                             |
| MULTIMEDIA MAIL      | Multimedia Mail gives the capability of attaching Binary Large OBjects (BLOBs) to electronic messages so that images, spreadsheets, graphs, and other operating system files that are not pure ASCII text, may be sent and received either locally or across the network.                                                                                                                                                                                                                                                    |
| PHYSICAL LINK DEVICE | Hardware used to establish outgoing communication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| "PLAYING A SCRIPT"   | A method of opening a transmission link for a message, used to force message transmission of message and testing.                                                                                                                                                                                                                                                                                                                                                                                                            |
| POLLER               | An option that opens the transmission line to all domains with "P" in the Flags field.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| POSTMASTER           | The basket where message queues are stored. Also, the person who manages this basket for a particular site.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PROTOCOL             | Code containing logic for opening and closing links, and for sending/receiving transmissions.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PURGE                | A procedure used to delete messages or message pointers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| QUEUE                | A list that stores messages destined for a given domain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| REMOTE               | Any system that a user is not signed on to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SCRIPT               | A set of MailMan commands and transmission scripts to a remote domain in the DOMAIN file (#4.2).                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SERVER               | An automatic mail reader for internal messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SMTP                 | Simple Mail Transport Protocol. The primary transport protocol for MailMan.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SWP                  | Sliding Window Protocol.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| TRANSMISSION SCRIPT  | List of commands for directing a message stored in the TRANSMISSION SCRIPT field.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VALIDATION NUMBER    | A security check number that *must* be in the domains of both the sending and receiving sites.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| WRAP-AROUND MODE     | Text that is fit into available column positions and automatically wraps to the next line, sometimes by splitting at word boundaries (spaces).                                                                                                                                                                                                                                                                                                                                                                               |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-systems-management-guide/113.png)</td>
<td><p><strong>REF:</strong> For a list of commonly used terms and definitions, see the OIT Master Glossary VA Intranet Website: REDACTED</p>
<p>For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website: REDACTED</p></td>
</tr>
</tbody>
</table>

<span id="_Hlt448199958" class="anchor"></span>Index

\$

\$\$NAMEFMT^XLFNAME API, 19

%

%ZRTL Global, 102

%ZTRL Global, 34

^

^XMBPOST("BOX" Queue, 2

A

ACK, 91

Acronyms

Intranet Website, 114

Active Users/Deliveries Report Option, 33

AI Cross-reference, 22

AI x-Ref Purge of Received Network Messages Option, 22

Analysis of Requirements

Multimedia MailMan, 80

APIs

\$\$FMTE^XLFDT (Date/Time Format API), 18

\$\$NAMEFMT^XLFNAME API, 19

MAIL^XLFNSLK (DNS Lookup API), 17, 42

ARRIVING Basket, 10, 11

Ask users with many messages to do maintenance Option, 23

Assumptions

About the Reader, xvii

AUTOMATIC INTEGRITY CHECK Field (#4.303), 12

B

Background Filers, 35, 36, 74

Baskets

ARRIVING, 10, 11

IN, 10, 11

WASTE, 10

Binary Large OBject, 80, 81, 82, 83, 84, 85, 86, 87, 89

BLOB, 80, 81, 82, 83, 84, 85, 86, 87, 89

Broadcast Messages, 11

With Responses, 19

Bulletin edit Option, 30

BULLETIN File (#3.6), 13, 16, 21

Bulletins, 10, 16

XMVALBAD, 100

C

Callout Boxes, xv

Capacity, 74

Capture a Session, 52

CHECK background filer Option, 33

Check MailMan Files for Errors Option, 21

CHECK^XMKPL, 2, 5

Checksums, 51

Christen a domain Option, 36

Clean out waste baskets Option, 23

COMMUNICATIONS PROTOCOL File (#3.4), 13, 17

Communications Tool

TalkMan, 52

COMPARE Option, 44

Compare PackMan Message Routines Option, 45

Compile Response Time Statistic Option, 34

Configuration

Multimedia MailMan, 85

Contents, v

Continue a TalkMan Session, 53

Controlled Procedures, 12

Coordinator For a Mail Group, 31

Create a Mailbox for a user Option, 22

Cross-references

AI, 22

D

Data Dictionary

Data Dictionary Utilities Menu, xvii

Listings, xvii

DATE PURGE CUTOFF DAYS Field (#10.03), 26, 27

DATE PURGE GRACE PERIOD Field (#10.04), 27

Date/Times

Format API

\$\$FMTE^XLFDT, 18

Reformatted, 18

Delete Found Messages from Found Messages List Option, 29

Deliver Found Messages into User's IN Basket Option, 29, 30

DELIVER^XMTDL1, 7

Deliveries by Group Option, 34

Delivery Queue Statistics Collection Option, 34

DEVICE File (#3.5), 76, 87

DEVICE FOR QUEUED JOB OUTPUT Field (#3), 27

DEVICE^XMKPO, 9

Devices

Messages To, 9

P-Message Device Setup, 106

DIALOGUE CAPTURE Message, 10

Directories

MailLink, 37, 38, 39

VACO, 37

WANG/NOAVA, 37

Disclaimers, xiv

Disk Space Management Menu, 11, 22, 23, 24, 25, 28, 29

Distribution List, 94

Creating, 96

Editing, 96

DISTRIBUTION LIST File (#3.816), 13, 94, 98

DNS AWARE Field (#8.22), 17

DNS IP Field (#51), 17, 42

DNS Lookup API

MAIL^XLFNSLK, 42

DNS-Aware MailMan, 17, 42

APIs

MAIL^XLFNSLK (DNS Lookup API), 42

Namespace, 12

Documentation

Symbols, xiv

Documentation Conventions, xiv

Documentation Navigation, xv

DOMAIN File (#4.2), 13, 17, 42, 51, 52, 56, 84, 87, 100

Glossary, 113

Domains

Playing Scripts, 10

Remote, 10

VHA.DMIA, 108, 109

DROP OUT OF RESTRICTED GROUP Field (#22), 31

DUZ=.5, 10

E

Edit Distribution List Option, 31, 96

Edit numbers to Normalize Reports Option, 34

Editing PackMan Messages Option, 47

End a TalkMan Session, 53

Enhanced Routines, 18

Enroll in (or Disenroll from) a Mail Group Option, 31

Enter/Edit Directory Request Flags by Group Option, 37, 38

Enter/Edit Remote User Option, 38

Error Displays, 70

Error Type Dictionary, 71

Extended Search, 10

F

Features, 16

Fields

AUTOMATIC INTEGRITY CHECK (#4.303), 12

DATE PURGE CUTOFF DAYS (#10.03), 26, 27

DATE PURGE GRACE PERIOD (#10.04), 27

DEVICE FOR QUEUED JOB OUTPUT (#3), 27

DNS AWARE (#8.22), 17

DNS IP (#51), 17, 42

DROP OUT OF RESTRICTED GROUP (#22), 31

FLAGS, 52

FTP ADDRESS FOR BLOB RECEIVE, 84, 86

FTP BLOB IP ADDRESS, 87

FTP PASSWORD, 84, 86

FTP RECEIVE DIRECTORY, 84, 86

FTP RECEIVE NETWORK LOCATION, 84, 86

FTP USERNAME, 84, 86

IMAGING SITE PARAMETERS NAME, 87

MESSAGE RETENTION DAYS, 24

NETWORK - MAX LINES RECEIVE (#8.31), 19

NO-PURGE DAYS BUFFER (#4.301), 12

NO-PURGE DAYS BUFFER (LOCAL) (#142), 12

RESPONSE Multiple, 72

RETENTION DAYS (#5), 16

TCP/IP COMMUNICATIONS PROTOCOL (#8.23), 17

TCP/IP TRANSMISSION SCRIPT (#8.24), 17

VALIDATION NUMBER, 100

WEEKDAY DAYS TO PURGE (#4.304), 12

Figures, ix

Files, 13

BULLETIN (#3.6), 13, 16, 21

COMMUNICATIONS PROTOCOL (#3.4), 13, 17

DEVICE (#3.5), 76, 87

DISTRIBUTION LIST (#3.816), 13, 94, 98

DOMAIN (#4.2), 13, 17, 42, 51, 52, 56, 87, 100

Glossary, 113

IMAGE (#2005), 14, 83, 85

INTERNET SUFFIX (#4.2996), 13

INTER-UCI TRANSFER (#4.281), 13

KERNEL SYSTEM PARAMETERS (#8989.3), 17, 42

MAIL GROUP (#3.8), 13, 21

MAILBOX (#3.7), 12, 13, 21, 22, 23, 25, 40, 70, 72

MUMPS Cross-reference, 12

MAILMAN OUTSTANDING FTP TRANSACTIONS (#4.2995), 13

MAILMAN SITE PARAMETERS (#4.3), 2, 10, 12, 13, 17, 19, 24, 26, 27, 31, 36, 56, 74, 86, 87, 89, 102

MAILMAN TIME ZONE (#4.4), 13

MESSAGE (#3.9), 11, 12, 13, 15, 21, 23, 25, 26, 71, 72

MESSAGE DELIVERY STATS (#4.2998), 13, 34, 102

MESSAGE STATISTICS (#4.2999), 13, 105

MESSAGES TO BE NEW AT A LATER DATE (#3.73), 13

NETWORK LOCATION (#2005.2), 14, 84, 85, 87

NETWORK SENDERS REJECTED (#4.501), 13

NETWORK TRANSACTION (#4.5)

Security, 13

NEW PERSON (#200), 19, 40

OPTION SCHEDULING (#19.2), 27

PACKAGE (#9.4), 44

REMOTE USER DIRECTORY (#4.2997), 13, 37, 76

RESOURCE (#3.54), 13

SPOOL DATA (#3.519), 13

SPOOL DOCUMENT (#3.51), 13

TRANSMISSION SCRIPT (#4.6), 13, 17, 36

USERS.COM, 103

Find Messages for User Option, 29, 30

Fine Tuning MailMan, 74

FLAGS Field, 52

FORUM, iv, 22, 31, 53, 76, 94, 96, 98

FTP, 80, 81, 82, 83, 84, 86, 87, 88, 89

FTP ADDRESS FOR BLOB RECEIVE Field, 84, 86

FTP BLOB DIRECTORY, 87

FTP BLOB IP ADDRESS, 87

FTP PASSWORD Field, 84, 86

FTP RECEIVE DIRECTORY Field, 84, 86

FTP RECEIVE NETWORK LOCATION Field, 84, 86

FTP USERNAME Field, 84, 86

Functions

PackMan, 44

G

Generalized Device Control and Communication Utility, 90

Getting Started

Multimedia MailMan, 85

GLOBAL LOAD, 44

Globals

%ZRTL, 102

%ZTRL, 34

Locations, 13

Glossary, 112

Intranet Website, 114

GO^XMKPLQ, 2, 3, 5

GO^XMTDL, 3, 5, 7

Graphics Download to Graphics (TAB Separators) Option, 34

Group eMail Directory Request Option, 38

Group/Distribution Management Menu, 30, 31, 32, 96

Groups

Coordinator, 31

Organizer, 31

H

Help

At Prompts, xvi

Online, xvi

Question Marks, xvi

Historical Background

Multimedia MailMan, 80

History, Revisions to Documentation and Patches, iii

Home Pages

\$\$FMTE^XLFDT Web Address, 18

Acronyms Intranet Website, 114

Adobe Website, xviii

DNS and VistA White Paper Web Address, 42

Glossary Intranet Website, 114

MAIL^XLFNSLK Web Address, 42

MailMan Home Page, xvii

VHA Software Document Library (VDL) Website, xviii

VistA Development Website, xiv

VistA Documentation Library (VDL)

MailMan, 69

Host File Server, 38

How the VistA PCTS Twix Interceptor Works, 108

How to

Install the Network File System (NFS)

Multimedia MailMan, 88

Invoke the Script Processor, 90

Obtain Technical Information Online, xvi

Use this Manual, xiii

I

IMAGE File (#2005), 14, 83, 85

Imaging

Software

Installation of the Imaging Software on the Workstation

Multimedia MailMan, 87

IMAGING SITE PARAMETERS NAME Field, 87

Implementation, 10

Improved Name Field Display, 19

IN Basket, 10, 11

IN Basket Purge Option, 23

INSTALL SELECTED ROUTINE(S) Option, 44

INSTALL/CHECK MESSAGE Option, 44

Installation of the Imaging Software on the Workstation

Multimedia MailMan, 87

Installing a PackMan Message Option, 45

Installing PackMan Messages into a Second Account, 51

Integrity Checker, 70

XMUT-CHKFIL, 70

Intended Audience, xiii

Intercepting Twix from the PCTS System, 108

Overview, 108

Setup Instructions, 109

INTERNET SUFFIX File (#4.2996), 13

INTER-UCI TRANSFER File (#4.281), 13

Introduction

MailMan Systems Management Guide, 1

Multimedia MailMan, 80

Invoking the Script Processor, 90

IRM

Manage MailMan, 16

Messages to Devices, Servers, and Remote Sites (Detail), 9

Messages to Local Users

Detail, 3

Overview, 2

Send a Message, What Happens, 2

K

KERNEL SYSTEM PARAMETERS File (#8989.3), 17, 42

Kill Transmission, 11

L

Large Message Report Option, 24

Legal Requirements, xiii, 13

Line Restriction Override, 19

List eMail Directory Request by Groups Option, 38

List File Attributes Option, xvii

List Messages Found Option, 30

Load Remote VACO (Wang/Noava) Directory Option, 38, 77

Loading an Entire Software Package into a PackMan Message Option, 46

Loading Global Data Option, 44

Loading Routines into PackMan Messages Option, 44

Local Delivery Management Menu, 33, 34, 35, 36, 103

Local Statistics, 102

Log Response Time Toggler Option, 35

M

Mail Delivery Statistics Report Option, 35

Mail Group Coordinator's Edit Option, 32

Mail Group Coordinator's Edit W/Remotes Option, 32

Mail Group Edit Option, 32, 94, 97

MAIL GROUP File (#3.8), 13, 21

Mail Groups, 94

Coordinator, 31

Organizer, 31

MAIL^XLFNSLK, 17

MAILBOX File (#3.7), 12, 13, 21, 22, 23, 25, 40, 70, 72

MUMPS Cross-reference, 12

MailLink Directory, 37, 38, 39

MailLink Program, 76

MailMan

APIs for the DNS-Aware MailMan

MAIL^XLFNSLK (DNS Lookup API), 42

Distribution List, 94

DNS-Aware, 17, 42

Fine Tuning, 74

Integrity Checker (XMUT-CHKFIL), 70

Menu Structure, 20

Namespace, 12

Script Processor, 90

Statistics, 102

Validation Numbers, 100

MailMan Menu, 20

MAILMAN OUTSTANDING FTP TRANSACTIONS File (#4.2995), 13

MailMan Site Parameters, 56

MAILMAN SITE PARAMETERS File (#4.3), 2, 10, 12, 13, 17, 19, 24, 26, 27, 31, 36, 56, 74, 86, 87, 89, 102

MailMan Site Parameters Option, 36, 56

MAILMAN TIME ZONE File (#4.4), 13

MailMan Website, xvii

Maintenance, 10, 11

Task Requirements Timetable

Mandatory, 15

Suggested, 16

Manage MailMan, 16

Manage MailMan Menu, 11, 20, 21, 22, 30, 33, 36, 37, 56, 94, 95, 103

Management Features, 16

Mapping

Routines, 14

Mapping Routines, 74

Menus

Data Dictionary Utilities, xvii

Disk Space Management, 11, 22, 23, 24, 25, 28, 29

Group/Distribution Management, 30, 31, 32, 96

Local Delivery Management, 33, 34, 35, 36, 103

MailMan Menu, 20

MailMan Menu Structure, 20

Manage MailMan, 11, 20, 21, 22, 30, 33, 36, 37, 56, 94, 95, 103

Network Management, 20, 36, 37

PackMan, 44

Recover Messages into User's IN Basket, 29, 30

Remote MailLink Directory Menu, 37, 38, 39

XMMGR, 20, 21, 22, 30, 33, 36, 37, 56, 94, 95, 103, 110

XMMGR-DIRECTORY-MAIN, 37, 38, 39

XMMGR-DISK-SPACE-MANAGEMENT, 22, 23, 24, 25, 28, 29

XMMGR-GROUP-MAINTENANCE, 30, 31, 32

XMMGR-MESSAGE-DELIVERY-MGT, 33, 34, 35, 36

XMNET, 20, 36, 37

XMUSER, 20, 87

XMUT-REC-MENU, 29, 30

MESSAGE (#3.9), 21

MESSAGE DELIVERY STATS File (#4.2998), 13, 34, 102

MESSAGE File (#3.9), 11, 12, 13, 15, 21, 23, 25, 26, 71, 72

Message Line Restriction Override, 19

Message Protocol Data Units, 80

MESSAGE RETENTION DAYS Field, 24

MESSAGE STATISTICS File (#4.2999), 13, 105

Message Statistics Option, 25

Messages

Broadcast, 11

DIALOGUE CAPTURE, 10

Local Users

Overview, 2

MESSAGES TO BE NEW AT A LATER DATE File (#3.73), 13

Messages with Responses

Broadcasting, 19

Mini out Subroutine, 92

Modems, 112

MPDU, 80, 81

Multimedia MailMan, 14, 80, 84, 85

Analysis of Requirements, 80

Configuration, 85

Getting Started, 85

Historical Background, 80

How to Install the Network File System (NFS), 88

Installation of the Imaging Software on the Workstation, 87

Introduction, 80

Non-textual BLOBs in Messages, 83

Overview, 82

Requirements, 84

Sending and Receiving BLOBs Across a Network, 83

Setup, 85

Site Parameters, 86

N

NAK, 91

Name Field Display Improved, 19

Namespace, 12

Network, 1

File System, 83, 88

Mail Statistics, 103

VMS Systems, 103

Statistics, 105

NETWORK - MAX LINES RECEIVE Field (#8.31), 19

NETWORK LOCATION File (#2005.2), 14, 84, 85, 87

Network Management Menu, 20, 36, 37

NETWORK SENDERS REJECTED File (#4.501), 13

NETWORK TRANSACTION File (#4.5)

Security, 13

New Features for Managing MailMan Option, 37

New Messages and Logon Statistics Option, 35

NEW PERSON File (#200), 19, 40

NFS, 80, 81, 82, 83, 84, 85, 88, 89

Non-textual BLOBs in Messages

Multimedia MailMan, 83

NO-PURGE DAYS BUFFER (LOCAL) Field (#142), 12

NO-PURGE DAYS BUFFER Field (#4.301), 12

O

Obtaining

Data Dictionary Listings, xvii

Online

Documentation, xvi

Technical Information, How to Obtain, xvi

Option for Users to Use to Send a Twix, 110

OPTION SCHEDULING File (#19.2), 27

Options

Active Users/Deliveries Report, 33

AI x-Ref Purge of Received Network Messages, 22

Ask users with many messages to do maintenance, 23

Bulletin edit, 30

CHECK background filer, 33

Check MailMan Files for Errors, 21

Christen a domain, 36

Clean out waste baskets, 23

COMPARE, 44

Compile Response Time Statistic, 34

Create a Mailbox for a user, 22

Data Dictionary Utilities, xvii

Delete Found Messages from Found Messages List, 29

Deliver Found Messages into User's IN Basket, 29, 30

Deliveries by Group, 34

Delivery Queue Statistics Collection, 34

Disk Space Management, 11, 22, 23, 24, 25, 28, 29

Edit Distribution List, 31, 96

Edit numbers to Normalize Reports, 34

Enroll in (or Disenroll from) a Mail Group, 31

Enter/Edit Directory Request Flags by Group, 37, 38

Enter/Edit Remote User, 38

Find Messages for User, 29, 30

Graphics Download to Graphics (TAB Separators), 34

Group eMail Directory Request, 38

Group/Distribution Management, 30, 31, 32, 96

IN Basket Purge, 23

INSTALL SELECTED ROUTINE(S), 44

INSTALL/CHECK MESSAGE, 44

Large Message Report, 24

List eMail Directory Request by Groups, 38

List File Attributes, xvii

List Messages Found, 30

Load Remote VACO (Wang/Noava) Directory, 38, 77

Local Delivery Management, 33, 34, 35, 36, 103

Log Response Time Toggler, 35

Mail Delivery Statistics Report, 35

Mail Group Coordinator's Edit, 32

Mail Group Coordinator's Edit W/Remotes, 32

Mail Group Edit, 32, 94, 97

MailMan Menu, 20

MailMan Menu Structure, 20

MailMan Site Parameters, 36, 56

Manage MailMan, 11, 20, 21, 22, 30, 33, 36, 37, 56, 94, 95, 103

Message Statistics, 25

Network Management, 20, 36, 37

New Features for Managing MailMan, 37

New Messages and Logon Statistics, 35

PACKAGE LOAD, 44

PackMan, 44

PRINT MESSAGE, 44

Purge a message, 25

Purge Messages by Origination Date, 25

Purge Unreferenced Messages, 28

Recover Messages into User's IN Basket, 29, 30

Remote Directory from all Domains, 38

Remote MailLink Directory Menu, 37, 38, 39

Request Mail Directory From a Single Domain Server, 39

ROUTINE LOAD, 44

START background filer, 35, 36

STOP background filer, 35, 36

SUMMARIZE MESSAGE, 44

SYSGEN, 87

TEXT PRINT/DISPLAY, 44

XMAUTOPURGE, 15, 23, 25, 28, 70, 72

XMCLEAN, 15, 23

XMEDITBUL, 30

XMEDITDIST, 31

XMEDITMG, 32

XMEDIT-REMOTE-USER, 38

XMENROLL, 31

XMKSP, 36, 56

XMMGR, 20, 21, 22, 30, 33, 36, 37, 56, 94, 95, 103, 110

XMMGR- BKFILER-TABBED-STATS, 34

XMMGR-BKFILER-ACT, 33

XMMGR-BKFILER-EDIT-NORMALIZED, 34

XMMGR-BKFILER-GROUP, 34

XMMGR-BKFILER-STAT, 35

XMMGR-CHECK-BACKGROUND-FILER, 33

XMMGR-DELIVERY-STATS-COLL, 34, 102

XMMGR-DIRECTORY-ALL, 38

XMMGR-DIRECTORY-EDITGRP, 37, 38

XMMGR-DIRECTORY-GROUP, 38

XMMGR-DIRECTORY-LISTGRP, 38

XMMGR-DIRECTORY-MAIN, 37, 38, 39

XMMGR-DIRECTORY-SINGLE, 39

XMMGR-DIRECTORY-VACO, 38

XMMGR-DISK-MANY-MESSAGE-MAINT, 16, 23

XMMGR-DISK-SPACE-MANAGEMENT, 22, 23, 24, 25, 28, 29

XMMGR-GROUP-MAINTENANCE, 30, 31, 32

XMMGR-HELP, 37

XMMGR-IN-BASKET-PURGE, 23

XMMGR-LARGE-MESSAGE-REPORT, 16, 24

XMMGR-MAIL-GRP-COORDINATOR, 32

XMMGR-MAIL-GRP-COORD-W/REMOTES, 32

XMMGR-MESSAGE-DELIVERY-MGT, 33, 34, 35, 36

XMMGR-NEW-MAIL-BOX, 22

XMMGR-NEWMESS/LOGON-STATS, 35

XMMGR-PURGE-AI-XREF, 16, 22

XMMGR-PURGE-MESSAGE, 25

XMMGR-RESPONSE-TIME-COMPILER, 16, 34, 102

XMMGR-RESPONSE-TIME-TOGGLER, 16, 35, 102

XMMGR-START-BACKGROUND-FILER, 35, 36

XMMGR-STOP-BACKGROUND-FILER, 35, 36

XMNET, 20, 36, 37

XMNET-TWIX-SEND, 110

XMNET-TWIX-TRANSMIT, 109

XMPURGE, 25, 28

XMPURGE-BY-DATE, 15, 16, 25, 26

XMSTAT, 25, 28

XMSUBEDIT, 92

XMUSER, 20, 87

XMUT-CHKFIL, 12, 15, 21, 70

XMUT-REC‑DELETE, 29

XMUT-REC‑DELIVER, 29, 30

XMUT-REC-FIND, 29, 30

XMUT-REC-MENU, 29, 30

XMUT-REC-RPT, 30

Organizer For a Mail Group, 31

Orientation, xiii

Overview

Intercepting Twix from the PCTS System, 108

Multimedia MailMan, 82

P

PACKAGE File (#9.4), 44

PACKAGE LOAD Option, 44

PackMan, 10, 44, 51

COMPARE Option, 44

Compare PackMan Message Routines Option, 45

Editing PackMan Messages Option, 47

INSTALL SELECTED ROUTINE(S) Option, 44

INSTALL/CHECK MESSAGE Option, 44

Installing a PackMan Message Option, 45

Installing PackMan Messages into a Second Account, 51

Loading an Entire Software Package into a PackMan Message Option, 46

Loading Global Data Option, 44

Loading Routines into PackMan Messages Option, 44

Menu Functions, 44

PACKAGE LOAD Option, 44

PRINT MESSAGE Option, 44

Printing PackMan Messages Option, 46

ROUTINE LOAD Option, 44

Security, 51

SUMMARIZE MESSAGE Option, 44

Summarize PackMan Message Option, 45

TEXT PRINT/DISPLAY Option, 44

Ways to Ensure Integrity of PackMan Messages, 48

Why Editing PackMan Messages Can Cause Problems, 47

Patches

Revisions, iv

PCTS, 108

How the VistA PCTS Twix Interceptor Works, 108

Overview, 108

System Setup and Use, 108

P-Message

Definitions for the Workstation Environment Running MSM, 106

Device Setup, 106

Postmaster, 10, 11, 15, 31

DUZ=.5, 10

Management, 10

PRINT MESSAGE Option, 44

Printing PackMan Messages Option, 46

Priority Transmission Flexibility, 17

Procedures

Controlled, 12

Programs

MailLink, 76

Protocols

SCP, 92

PS Anonymous Directories, xviii

Purge a message Option, 25

Purge Messages by Origination Date Option, 25

Purge Unreferenced Messages Option, 28

Q

Question Mark Help, xvi

Queues

^XMBPOST("BOX", 2

R

Reader, Assumptions about the, xvii

Recover Messages into User's IN Basket Menu, 29, 30

Reference Materials, xvii

Reformatted

Date/Times, 18

Remote Message IDs, 18

Remote Directory from all Domains Option, 38

Remote MailLink Directory Menu, 37, 38, 39

Remote MailLink Program, 77

Remote Message IDs, Reformatted, 18

REMOTE USER DIRECTORY File (#4.2997), 13, 37, 76

REMOTE^XMKPO, 9

Request Mail Directory From a Single Domain Server Option, 39

Requeued Task Bug Fix, 19

Requirements

Legal, xiii

Multimedia MailMan, 84

RESOURCE File (#3.54), 13

RESPONSE Multiple Field, 72

Response Time Logging, 102

RETENTION DAYS field (#5), 16

Revision History, iii

Patches, iv

ROUTINE LOAD Option, 44

Routines, 14

Enhanced, 18

Mapping, 14

XMBPOST, 9

XMKP, 2, 3, 9

XMUTCOM1, 104

RTHIST, 14

S

Schedule Option for Transmitting Queue to Run Periodically, 109

SCP Protocol, 92

Script Processor, 90

Generalized Device Control and Communication Utility, 90

Invoking, 90

Security

PackMan, 51

Security Check, 51

Security Keys

XMMGR, 25

XUPROG, 21, 29

Self-Enrollment, 31

Send a Message

IRM

What Happens, 2

Sending and Receiving BLOBs Across a Network

Multimedia MailMan, 83

SERVER^XMKPO, 9

SERVER^XMTDO, 9

Setting Up the VHA.DMIA Domain, 109

Setup

Instructions

Intercepting Twix from the PCTS System, 109

Multimedia MailMan, 85

PCTS System Setup and Use, 108

SHARED,MAIL, 26

Site Parameters, 24

Multimedia MailMan, 86

SMTP, 82, 85, 92

Software

Maintenance, 11

Management, 10

SPOOL DATA File (#3.519), 13

SPOOL DOCUMENT File (#3.51), 13

START background filer Option, 35, 36

Statistics, 102

Local, 102

MailMan, 102

Network, 105

Network Mail, 103

VMS Systems, 103

STOP background filer Option, 35, 36

SUMMARIZE MESSAGE Option, 44

Summarize PackMan Message Option, 45

Supported

Integration Agreements, 18, 42

Symbols

Found in the Documentation, xiv

SYSGEN Option, 87

System Maintenance, 15

System Management, 20

T

Table of Contents, v

Tables, xi

TalkMan, 10, 52

Communications Tool, 52

TalkMan and IDCU, 53

Task Requirements

Maintenance Timetable

Mandatory, 15

Suggested, 16

TaskMan, 23, 108

Tasks Requeued Bug Fix, 19

TCP/IP, 74, 81, 82, 83, 84, 85, 88

TCP/IP COMMUNICATIONS PROTOCOL Field (#8.23), 17

TCP/IP Connections and Transmission Scripts, 17

TCP/IP TRANSMISSION SCRIPT Field (#8.24), 17

TEXT PRINT/DISPLAY Option, 44

Transmission

Failures, 11

Priority Flexibility, 17

Scripts and TCP/IP Connections, 17

TRANSMISSION SCRIPT File (#4.6), 13, 17, 36

Troubleshooting

MailMan, 40

Twix, 108, 109

How the VistA PCTS Twix Interceptor Works, 108

Option for Users to Use to Send a Twix, 110

Overview, 108

U

URLs

\$\$FMTE^XLFDT Home Page Web Address, 18

Acronyms Intranet Website, 114

Adobe Website, xviii

DNS and VistA White Paper Web Address, 42

Glossary Intranet Website, 114

MAIL^XLFNSLK Home Page Web Address, 42

MailMan Home Page, xvii

VHA Software Document Library (VDL) Website, xviii

VistA Development Website, xiv

VistA Documentation Library (VDL)

MailMan, 69

Use this Manual, How to, xiii

USERS.COM File, 103

V

VACO Directory, 37

VALIDATION NUMBER Field, 100

Validation Numbers, 100, 101

Variables

XMDIC, 90

XMSCR, 90

XMSCRN, 90

VHA Software Document Library (VDL)

Website, xviii

VHA.DMIA Domain, 108, 109

VistA Documentation Library (VDL)

MailMan, 69

W

WANG/NOAVA Directory, 37

WASTE Basket, 10

Ways to Ensure Integrity of PackMan Messages, 48

Web Pages

\$\$FMTE^XLFDT Home Page Web Address, 18

DNS and VistA White Paper Web Address, 42

MAIL^XLFNSLK Home Page Web Address, 42

MailMan Home Page, xvii

VistA Documentation Library (VDL)

MailMan, 69

Websites

Acronyms Intranet Website, 114

Adobe Website, xviii

Glossary Intranet Website, 114

VHA Software Document Library (VDL) Website, xviii

VistA Development Website, xiv

WEEKDAY DAYS TO PURGE Field (#4.304), 12

What Happens When You Send a Message?, 2

Why Editing PackMan Messages Can Cause Problems, 47

X

XM Bulletins

DATE PURGE WARNING, 26, 27, 28

XM DATE PURGE WARNING Bulletin, 26, 27, 28

XMAUTOPURGE Option, 15, 23, 25, 28, 70, 72

XMBPOST Routine, 9

XMCLEAN Option, 15, 23

XMDIC Variable, 90

XMEDITBUL Option, 30

XMEDITDIST Option, 31

XMEDITMG Option, 32

XMEDIT-REMOTE-USER Option, 38

XMENROLL Option, 31

XMKP Routine, 2, 3, 9

XMKSP Option, 36, 56

XMMGR- BKFILER-TABBED-STATS Options, 34

XMMGR Menu, 20, 21, 22, 30, 33, 36, 37, 56, 94, 95, 103, 110

XMMGR Security Key, 25

XMMGR-BKFILER-ACT Options, 33

XMMGR-BKFILER-EDIT-NORMALIZED Option, 34

XMMGR-BKFILER-GROUP Option, 34

XMMGR-BKFILER-STAT Option, 35

XMMGR-CHECK-BACKGROUND-FILER Option, 33

XMMGR-DELIVERY-STATS-COLL Option, 34, 102

XMMGR-DIRECTORY-ALL Option, 38

XMMGR-DIRECTORY-EDITGRP Option, 37, 38

XMMGR-DIRECTORY-GROUP Option, 38

XMMGR-DIRECTORY-LISTGRP Option, 38

XMMGR-DIRECTORY-MAIN, 37, 38, 39

XMMGR-DIRECTORY-SINGLE Option, 39

XMMGR-DIRECTORY-VACO Option, 38

XMMGR-DISK-MANY-MESSAGE-MAINT Option, 16, 23

XMMGR-DISK-SPACE-MANAGEMENT Menu, 22, 23, 24, 25, 28, 29

XMMGR-GROUP-MAINTENANCE Menu, 30, 31, 32

XMMGR-HELP Option, 37

XMMGR-IN-BASKET-PURGE Option, 23

XMMGR-LARGE-MESSAGE-REPORT Option, 16, 24

XMMGR-MAIL-GRP-COORDINATOR Option, 32

XMMGR-MAIL-GRP-COORD-W/REMOTES Option, 32

XMMGR-MESSAGE-DELIVERY-MGT Menu, 33, 34, 35, 36

XMMGR-NEW-MAIL-BOX Option, 22

XMMGR-NEWMESS/LOGON-STATS Option, 35

XMMGR-PURGE-AI-XREF Option, 16, 22

XMMGR-PURGE-MESSAGE Option, 25

XMMGR-RESPONSE-TIME-COMPILER Option, 16, 34, 102

XMMGR-RESPONSE-TIME-TOGGLER Option, 16, 35, 102

XMMGR-START-BACKGROUND-FILER Option, 35, 36

XMMGR-STOP-BACKGROUND-FILER Option, 35, 36

XMNET Menu, 20, 36, 37

XMNET-TWIX-SEND Option, 110

XMNET-TWIX-TRANSMIT Option, 109

XMPURGE Option, 25, 28

XMPURGE-BY-DATE Option, 15, 16, 25, 26

XMSCR Variable, 90

XMSCRN Variable, 90

XMSTAT Option, 25, 28

XMSUBEDIT Option, 92

XMTALK, 52

XMUSER Menu, 20, 87

XMUT-CHKFIL Option, 12, 15, 21, 70

XMUTCOM1 Routine, 104

XMUT-REC‑DELETE Option, 29

XMUT-REC‑DELIVER Option, 29, 30

XMUT-REC-FIND Option, 29, 30

XMUT-REC-MENU Menu, 29, 30

XMUT-REC-RPT Option, 30

XMVALBAD Bulletin, 100

XUPROG Security Key, 21, 29