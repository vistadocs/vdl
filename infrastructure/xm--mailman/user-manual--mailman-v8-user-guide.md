---
title: MailMan Version 8 User Guide
doc_type: UG
doc_label: User Guide
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
menu_options: 1
description: The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.
audience: 
keywords: 
  - message
  - messages
  - mailman
  - mail
  - basket
  - action
  - xmuser
  - group
  - prompt
  - read
page_count: 0
word_count: 93822
section_count: 7
table_count: 556
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_userguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_userguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=15"
---

![](mailman-version-8-user-guide/001.png)

MAILMANUSER GUIDE

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
<td>Initial MailMan V. 8.0 software and documentation release. MailMan V. 8.0 was first released as "DNS-Aware MailMan" in a supplemental document released in August 2002; however, the remaining MailMan documentation set was never updated.</td>
<td>REDACTED</td>
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
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc93384736" class="anchor"></span>Table i. Documentation revision history

Patch Revisions

For a complete list of patches released with this software, please refer to the Patch Module on FORUM.

## Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This *MailMan User Guide* is intended for use in conjunction with Veterans Health Information Systems and Technology Architecture (VistA) MailMan. It outlines the MailMan user interface, the actions users can take with regard to their personal mail baskets, messages, etc., and gives guidelines on how the software is used within VistA.

The intended audience of this manual is all primary (key) stakeholders. The primary stakeholders include:

- All VistA MailMan end users.
- VistA Infrastructure and Security Services (ISS) Development Team.
- Other VistA project development teams and programmers.
- Information Resource Management (IRM) personnel responsible for maintaining MailMan.
- Enterprise VistA Support (EVS).

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of MailMan V. 8.0 and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products. This manual discusses the use of electronic network communication software and covers network features for sending and receiving transmissions, responding, and transmitting mail. Many user actions are available for completing specific tasks.

There are no special legal requirements involved in the use of MailMan.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                |                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                     | Description                                                                                                     |
| ![](mailman-version-8-user-guide/002.png) | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](mailman-version-8-user-guide/003.png)                                                              | CAUTION or DISCLAIMER: Used to inform the reader to take special notice of critical information.                |
| ![](mailman-version-8-user-guide/004.png)                                                              | TIP: Used to inform the reader of helpful tips or tricks they can use when working with the software.           |

<span id="_Toc147225735" class="anchor"></span>Table ii. Documentation symbol descriptions

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
| ![](mailman-version-8-user-guide/005.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

|                                                                                                                |                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/006.png) | NOTE: Unless otherwise noted, all sample screen captures/dialogue boxes in this manual are derived from using either MailMan's Detailed or Summary Full Screen message readers. |

- This manual refers in many places to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the M programming language, and M will be considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/007.png) | NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of the software.

In addition to the "question mark" help, you can use the Help (User/Group Info., etc.) menu option on the main MailMan Menu to access the MailMan Help Frames through the following options:

- New Features in MailMan
- General MailMan Information
- Questions and Answers on MailMan
- Manual for MailMan Users

|                                                                                                                |                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/008.png) | REF: For more information on obtaining MailMan online help, please refer to Chapter 12, "Online Help Information" in the *MailMan User Guide*. |

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/009.png) | REF: For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" topic of the *VA FileMan Advanced User Guide*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language

This manual provides an overall explanation of MailMan and the changes contained in MailMan V. 8.0.; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) and VA Intranet for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following Intranet Web address:

> <http://vista.med.va.gov/>

Reference Materials

Readers who wish to learn more about MailMan should consult the following:

- *MailMan Release Notes*
- *MailMan Installation Guide*
- *MailMan Getting Started Guide*
- *MailMan Developer's Guide*
- *MailMan User Guide* (this manual)
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
<td>![](mailman-version-8-user-guide/010.png)</td>
<td><p><strong>REF:</strong> For more information on the use of the Adobe Acrobat Reader, please refer to the "Adobe Acrobat Quick Guide" at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">REDACTED</a></p>
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
| ![](mailman-version-8-user-guide/011.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction—Managing Mail In Your MailMan Message Center


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Contents](#contents)
  - [Figures and Tables](#figures-and-tables)
  - [Orientation](#orientation)
- [Introduction—Managing Mail In Your MailMan Message Center](#introductionmanaging-mail-in-your-mailman-message-center)
    - [Menu Structure](#menu-structure)
- [Reading/Managing Messages—New Messages and Responses](#readingmanaging-messagesnew-messages-and-responses)
    - [NML—New Messages and Responses Option](#nmlnew-messages-and-responses-option)
    - [Read All of Your New Mail by Basket](#read-all-of-your-new-mail-by-basket)
    - [List All of Your Baskets with New Mail](#list-all-of-your-baskets-with-new-mail)
    - [List All of Your New Messages](#list-all-of-your-new-messages)
    - [List All of Your Priority Messages](#list-all-of-your-priority-messages)
    - [Print All of Your New Messages](#print-all-of-your-new-messages)
    - [Scan All of Your New Messages](#scan-all-of-your-new-messages)
    - [Quit—Exiting the New Messages Option](#quitexiting-the-new-messages-option)
    - [Stop Reading a Message—Exiting a Message with Unread (New) Responses](#stop-reading-a-messageexiting-a-message-with-unread-new-responses)
- [Reading/Managing Messages—In a Basket](#readingmanaging-messagesin-a-basket)
    - [RML—Read/Manage Messages Option](#rmlreadmanage-messages-option)
    - [Action Codes—Baskets](#action-codesbaskets)
    - [Message Number ("n") Action](#message-number-n-action)
    - [Message Selection Actions](#message-selection-actions)
    - [Change Basket Name ("C") Action](#change-basket-name-c-action)
    - [Change Detail ("CD") Action](#change-detail-cd-action)
    - [Delete Messages ("D") Action](#delete-messages-d-action)
    - [Forward Messages ("F") Action](#forward-messages-f-action)
    - [Filter Messages ("FI") Action](#filter-messages-fi-action)
    - [Headerless Print Messages ("H") Action](#headerless-print-messages-h-action)
    - [Later Messages ("L") Action](#later-messages-l-action)
    - [New Message List ("N") Action](#new-message-list-n-action)
    - [New Toggle ("NT") Action](#new-toggle-nt-action)
    - [Opposite Selection Toggle ("O") Action](#opposite-selection-toggle-o-action)
    - [Print Messages ("P") Action](#print-messages-p-action)
    - [Query (Search for) Messages in this Basket ("Q") Action](#query-search-for-messages-in-this-basket-q-action)
    - [Resequence Messages ("R") Action](#resequence-messages-r-action)
    - [Save Messages to Another Basket ("S") Action](#save-messages-to-another-basket-s-action)
    - [Terminate Messages ("T") Action](#terminate-messages-t-action)
    - [Vaporize Date Edit ("V") Action](#vaporize-date-edit-v-action)
    - [Zoom Selection Toggle ("Z") Action](#zoom-selection-toggle-z-action)
    - [Paging Actions](#paging-actions)
    - [Text String Search Actions](#text-string-search-actions)
    - [Caret ("^") Exit Action](#caret-exit-action)
- [Reading/Managing Messages—Individual Messages](#readingmanaging-messagesindividual-messages)
    - [Action Codes—Individual Messages](#action-codesindividual-messages)
    - [Answer ("A") Action](#answer-a-action)
    - [Backup ("B") Action](#backup-b-action)
    - [Print to Browser ("BR") Action](#print-to-browser-br-action)
    - [Copy ("C") Action](#copy-c-action)
    - [Delete ("D") Action](#delete-d-action)
    - [Edit ("E") Action](#edit-e-action)
    - [Forward ("F") Action](#forward-f-action)
    - [Headerless Print ("H") Action](#headerless-print-h-action)
    - [Help: Group Information ("HG") Action](#help-group-information-hg-action)
    - [Help:User Information ("HU") Action](#helpuser-information-hu-action)
    - [Ignore ("I") Action](#ignore-i-action)
    - [Include Message ("IM") Action](#include-message-im-action)
    - [Information Only ("IN") Action (Toggle)](#information-only-in-action-toggle)
    - [Priority Replies ("K") Action (Toggle)](#priority-replies-k-action-toggle)
    - [Later ("L") Action](#later-l-action)
    - [New/Un New ("N") Action (Toggle)](#newun-new-n-action-toggle)
    - [Print ("P") Action](#print-p-action)
    - [Query ("Q") Action](#query-q-action)
    - [Query Recipients ("Q xxx") Action](#query-recipients-q-xxx-action)
    - [Query Current ("QC") Action](#query-current-qc-action)
    - [Query Detailed ("QD") Action](#query-detailed-qd-action)
    - [Query Network ("QN") Action](#query-network-qn-action)
    - [Query Not Current ("QNC") Action](#query-not-current-qnc-action)
    - [Query Terminated ("QT") Action](#query-terminated-qt-action)
    - [Reply ("R") & Reply and Include responses ("RI") Actions](#reply-r-reply-and-include-responses-ri-actions)
    - [Save ("S") Action](#save-s-action)
    - [Terminate ("T") Action](#terminate-t-action)
    - [Vaporize Date Edit ("V") Action](#vaporize-date-edit-v-action-1)
    - [Write ("W") Action](#write-w-action)
    - [Extract KIDS or PackMan Messages ("X") Action](#extract-kids-or-packman-messages-x-action)
    - [Caret ("^") Exit Action](#caret-exit-action-1)
- [Sending Mail](#sending-mail)
    - [SML—Send a Message Option](#smlsend-a-message-option)
    - [Message Subjects](#message-subjects)
    - [Address Functionality](#address-functionality)
    - [Delivery Options—Immediate, Deferred, and/or Staggered](#delivery-optionsimmediate-deferred-andor-staggered)
    - [Later ("L:xxx") Prefix Code](#later-lxxx-prefix-code)
    - [Completing an Interrupted Message](#completing-an-interrupted-message)
    - [Sending Mail Using the P-MESSAGE Device](#sending-mail-using-the-p-message-device)
    - [Action Codes—Sending Messages](#action-codessending-messages)
    - [Backup ("B") Action](#backup-b-action-1)
    - [Confidential ("C") Action (Toggle)](#confidential-c-action-toggle)
    - [Delivery Basket Set ("D") Action](#delivery-basket-set-d-action)
    - [Edit Recipients ("ER") Action](#edit-recipients-er-action)
    - [Edit Subject ("ES") Action](#edit-subject-es-action)
    - [Edit Text ("ET") Action](#edit-text-et-action)
    - [Information Only ("I") Action (Toggle)](#information-only-i-action-toggle)
    - [Transmit Later ("L") Action](#transmit-later-l-action)
    - [Network Signature ("NS") Action](#network-signature-ns-action)
    - [Priority Delivery ("P") Action (Toggle)](#priority-delivery-p-action-toggle)
    - [Confirm Receipt ("R") Action (Toggle)](#confirm-receipt-r-action-toggle)
    - [Scramble ("S") Action](#scramble-s-action)
    - [Transmit Now ("T") Action](#transmit-now-t-action)
    - [Vaporize Date Set ("V") Action](#vaporize-date-set-v-action)
    - [Closed Message ("X") Action (Toggle)](#closed-message-x-action-toggle)
    - [Canceling a Message ("^")](#canceling-a-message)
- [Searching Mail](#searching-mail)
    - [Query/Search for Messages Option](#querysearch-for-messages-option)
    - [Where to Search](#where-to-search)
    - [Search Criteria](#search-criteria)
    - [Searching All Messages](#searching-all-messages)
    - [Searching Your Own Mailbox](#searching-your-own-mailbox)
- [Filtering Mail](#filtering-mail)
    - [Message Filter Edit Option](#message-filter-edit-option)
    - [Filtering Criteria](#filtering-criteria)
    - [Establishing Filter Order](#establishing-filter-order)
    - [Create a New Mail Filter](#create-a-new-mail-filter)
    - [Edit an Existing Mail Filter](#edit-an-existing-mail-filter)
    - [Modify a Mail Filter and Filter Messages in a Basket](#modify-a-mail-filter-and-filter-messages-in-a-basket)
    - [Delete a Mail Filter](#delete-a-mail-filter)
- [Mail Groups](#mail-groups)
    - [Mail Group Options](#mail-group-options)
    - [Enroll in Mail Groups](#enroll-in-mail-groups)
    - [Disenroll From Mail Groups](#disenroll-from-mail-groups)
    - [Personal Mail Groups](#personal-mail-groups)
- [Surrogates](#surrogates)
    - [Surrogate Options](#surrogate-options)
    - [Become a Surrogate](#become-a-surrogate)
    - [Designate a Surrogate](#designate-a-surrogate)
    - [Remove a Surrogate](#remove-a-surrogate)
- [Forwarding Mail](#forwarding-mail)
    - [Forwarding Address Edit Option](#forwarding-address-edit-option)
    - [Forwarding Address](#forwarding-address)
    - [Local Delivery Flag](#local-delivery-flag)
    - [Enter Your Forwarding Address](#enter-your-forwarding-address)
    - [Delete Your Forwarding Address](#delete-your-forwarding-address)
- [Reports and Lists](#reports-and-lists)
    - [Other MailMan Functions Option](#other-mailman-functions-option)
    - [Get a Report On "Latered" Messages in Your Mailbox](#get-a-report-on-latered-messages-in-your-mailbox)
    - [Change/Delete a Message's "Latered" Date and Time](#changedelete-a-messages-latered-date-and-time)
    - [Get a List of All Messages in Your Mailbox](#get-a-list-of-all-messages-in-your-mailbox)
- [Online Help/Information](#online-helpinformation)
    - [Help (User/Group Info., etc.) Option](#help-usergroup-info-etc-option)
    - [User Information](#user-information)
    - [Remote User Information](#remote-user-information)
    - [Mail Group Information](#mail-group-information)
    - [New Features in MailMan](#new-features-in-mailman)
    - [General MailMan Information](#general-mailman-information)
    - [Frequently Asked Questions About MailMan](#frequently-asked-questions-about-mailman)
    - [MailMan Users Manual (Online)](#mailman-users-manual-online)
  - [Glossary](#glossary)
  - [Index](#index)
This manual provides descriptive information and instructions on the use of the MailMan software within the VA's Veterans Health Information Systems and Technology Architecture (VistA) environment. This document is intended for all personnel who use VistA's MailMan software.
MailMan V. 8.0 not only modified existing options and functionality but added new options and functionality to the MailMan software. This manual has been created to assist you when working with the MailMan user interface. This manual discusses the various options provided by MailMan V. 8.0 that allow you to better manage your mail and maintain your MailMan Message Center. Both the new and existing functionality is described in the chapters that follow.
The topics covered in this manual include:
- Reading/Managing Messages—New Messages and Responses
- Reading/Managing Messages—In a Basket
- Reading/Managing Messages—Individual Messages
- Sending Mail
- Searching Mail
- Filtering Mail
- Mail Groups
- Surrogates
- Forwarding Mail
- Reports and Lists
- Online Help/Information

### Menu Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 58%" />
<col style="width: 41%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="mailman-menu" class="unnumbered">MailMan Menu</h4></td>
<td><strong>[XMUSER]</strong></td>
</tr>
</tbody>
</table>
The MailMan Menu \[XMUSER\] is the main MailMan user menu. It contains options that allow the MailMan user to fully manage their mailbox and messages. This menu contains the following options:
Select MailMan Menu Option:
NML New Messages and Responses \[XMNEW\]
RML Read/Manage Messages \[XMREAD\]
SML Send a Message \[XMSEND\]
Query/Search for Messages \[XMSEARCH\]
AML Become a Surrogate (SHARED,MAIL or Other) \[XMASSUME\]
Personal Preferences ... \[XM PERSONAL MENU\]
Other MailMan Functions ... \[XMOTHER\]
Help (User/Group Info., etc.) ... \[XMHELP\]
<span id="_Toc147225736" class="anchor"></span>Figure 1‑1. MailMan Menu \[XMUSER\] menu options

# Reading/Managing Messages—New Messages and Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter discusses the following topics:

- NML—New Messages and Responses Option
- Read All of Your New Mail by Basket
- List All of Your Baskets with New Mail
- List All of Your New Messages
- List All of Your Priority Messages
- Print All of Your New Messages
- Scan All of Your New Messages
- Quit—Exiting the New Messages Option
- Stop Reading a Message—Exiting a Message with Unread (New) Responses

The features and functionality associated with managing your *new* messages are described in greater detail in this chapter.

### NML—New Messages and Responses Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the New Messages and Responses option \[XMNEW; synonym NML\] when you specifically wish to process *new* mail in your mailbox.

It provides you with the following choices of how you choose to read your new mail:

- LB—List Baskets with new mail
- LN—List all New messages
- LP—List all Priority messages
- P—Print all new messages
- Q—Quit
- R—Read new mail by basket (default)
- S—Scan all new messages

The New Messages and Responses option \[XMNEW; synonym NML\] is available on the main MailMan menu, as shown below:

NML New Messages and Responses \[XMNEW\]

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: NML \<Enter\> New Messages and Responses

Select New mail option: Read new mail by basket// ?

Enter a code from the list.

Select one of the following:

LB List Baskets with new mail

LN List all New messages

LP List all Priority messages

P Print all new messages

Q Quit

R Read new mail by basket

S Scan all new messages

Select New mail option: Read new mail by basket//

<span id="_Ref449168505" class="anchor"></span>Figure 2‑1. NML—New Messages and Responses option

|                                                                                                                |                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/012.png) | NOTE: Besides the New Messages and Responses option \[XMNEW, synonym NML\], you can also use the Read/Manage Messages option \[XMREAD; synonym RML\] to read all of your messages in your mailbox, including the new messages. |

|                                                                                                                |                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/013.png) | REF: For more information on the Read/Manage Messages option \[XMREAD; synonym RML\], please refer to Chapter 3 and 4 in this manual. |

When listing new messages, all new message information is displayed in detail, regardless of the message reader you choose. Also, the list of messages will be displayed in the order you set when using the User Options Edit option to set your preferences.

|                                                                                                                |                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/014.png) | REF: For more information on setting your preferences, please refer to the *MailMan Getting Started Guide*. |

|                                                                                                                |                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/015.png) | NOTE: Some command actions are only available when using the Detailed or Summary Full Screen message readers. |

|                                                                                                                |                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/016.png) | REF: For a complete list and description of command action codes, please refer to the "Action Codes—Baskets" topic and Table 3‑1 in Chapter 3 in this manual. |

### Read All of Your New Mail by Basket

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can read all of your new mail basket by basket when you choose the Read new mail by basket option available with the New Messages and Responses option \[XMNEW; synonym NML\].

As the default, MailMan will start processing new mail in your "IN" basket, as shown below:

|                                                                                                                |                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/017.png) | NOTE: If you choose a basket other than "IN," MailMan "cycles" through all new mail in all baskets in basket name order (alphabetically). |

Select MailMan Menu Option: NML \<Enter\> New Messages and Responses

You have new mail in more than one basket.

Select New mail option: Read new mail by basket// \<Enter\>

Read NEW mail in MAIL BASKET: IN// ?

Answer with BASKET

Do you want the entire BASKET List? y \<Enter\> (Yes)

Choose from:

IN (14 messages, 8 new)

TEST (22 messages, 2 new)

Read NEW mail in MAIL BASKET: IN// TEST \<Enter\> (22 messages, 3 new)

Subj: test \[#1223222\] 08/04/98@08:14 1 line

From: XMUSER4,FOUR - Q... Continuum In 'TEST' basket. Page 1 \*New\*

---------------------------------------------------------

test

Enter message action (in TEST basket): IGNORE// \<Enter\>

.

.

.

Enter RETURN to continue or '^' to exit: \<Enter\>

Done with NEW mail in your 'TEST' Basket.

Read NEW mail in MAIL BASKET: IN//

<span id="_Ref427110261" class="anchor"></span>Figure 2‑2. Reading new mail by basket

In this example (Figure 2‑2), the user had new mail in more than one mail basket. Thus, when the user chose to read their new mail by basket, MailMan prompted her to choose from which basket she wanted to start reading her new mail. It defaulted to start with the "IN" basket.

By putting a question mark at the "Read NEW mail in MAIL BASKET: IN//" prompt, MailMan gave the user a list of all of her mail baskets with new mail. MailMan also tells you how many total messages reside in each of those baskets and how many of those messages are new. In this case, both the "IN" and "TEST" mail baskets contained new mail. For this example, the user chose to read from the "TEST" mail basket.

MailMan immediately began displaying the new mail in the "TEST" mail basket. MailMan will display each subsequent new message until all new messages have been read in that basket or you quit the option.

When you have read all your mail in one basket and still have new mail in other mail baskets, MailMan will prompt you to choose another mail basket to continue reading your new mail. If you only had new mail in one basket, MailMan would immediately begin displaying your first new message in that one basket. It would continue to display all subsequent new messages in that basket until all new messages have been read or you quit that option by entering a caret ("^") at the message action prompt.

|                                                                                                                |                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/018.png) | NOTE: If you use the Read new messages by basket option to read your mail, MailMan first displays any new priority mail before displaying other new mail. |

### List All of Your Baskets with New Mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can list all of your mail baskets with new mail in alphabetic order by choosing the List Baskets with new mail option available with the New Messages and Responses option \[XMNEW; synonym NML\], as shown below:

Select MailMan Menu Option: NML \<Enter\> New Messages and Responses

You have new mail in more than one basket.

Select New mail option: Read new mail by basket// LB \<Enter\> List Baskets with new mail

Choose from:

IN (8 New)

TEST (2 New)

Select New mail option: Read new mail by basket//

<span id="_Ref426855908" class="anchor"></span>Figure 2‑3. Listing baskets with new mail

As you can see from this example (Figure 2‑3), the user listed all of the baskets with new mail by choosing the List Baskets with new mail option.

MailMan displayed the list of all of the mail baskets with new mail in alphabetic order. In this case, both the "IN" and "TEST" mail baskets contain new mail.

MailMan also tells you how many new messages reside in each mail basket. With this information, you can choose another new mail option to read your new mail (e.g., Read new mail by basket option, previously described).

### List All of Your New Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can list all of your new mail in your mailbox, regardless of the mail basket, when you choose the List all New messages option available with the New Messages and Responses option \[XMNEW; synonym NML\], as shown below:

Select MailMan Menu Option: NML \<Enter\> New Messages and Responses

You have new mail in more than one basket.

Select New mail option: Read new mail by basket// LN \<Enter\> List all New messages

All Baskets, New messages: 10

\*=New/!=Priority...............Subject...............Lines.From.......Read/Rcvd

\* 1. IN \[1223232\] 08/04/98 Digest bat-list.v004.n 622 bat-list-errors@lists

\* 2. IN \[1223228\] 08/04/98 Stress management exerc 16 XMUSER4,FOUR

\* 3. IN \[1222979\] 08/02/98 Digest bat-list.v004.n 673 bat-list-errors@lists

\* 4. IN \[1222920\] 08/01/98 Digest bat-list.v004.n 673 bat-list-errors@lists

\* 5. IN \[1222838\] 07/31/98 Digest bat-list.v004.n 673 bat-list-errors@lists

\* 6. IN \[1222738\] 07/30/98 Digest bat-list.v004.n 673 bat-list-errors@lists

\* 7. IN \[1222669\] 07/30/98 Digest bat-list.v004.n 673 bat-list-errors@lists

\* 8. IN \[1222306\] 07/28/98 Sample Subject-1 10 XMUSER1,ONE 31/32

\* 9. TEST \[1223225\] 08/04/98 Sample Subject-2 10 XMUSER1,FOUR

\* 10. TEST \[1223223\] 08/04/98 Sample Subject-3 10 XMUSER1,FOUR

Enter message number or command

<span id="_Ref426861019" class="anchor"></span>Figure 2‑4. Listing all new mail

In this example (Figure 2‑4), the user chose the List all New messages option to list all of the new mail in the entire mailbox. From this list of messages you can see that eight of the new messages are in the "IN" mail basket and that two of the new messages are in the "TEST" mail basket.

In addition to totaling the number of new messages in all baskets, MailMan provides the following detailed information on each message:

- Flags—Any special flag associated with the message (e.g., Priority \["!"\] or New \["\*"\] flags).

|                                                                                                                |                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ![](mailman-version-8-user-guide/019.png) | NOTE: The priority flag is the exclamation point ("!"). |

- Message Number—The number associated with the message (meaningful for this list only).
- Basket—Basket containing the message (e.g., "IN").
- MailMan Internal Message Identification Number—The MailMan message number generated internally for the message (displayed in brackets).
- Message Sent Date—The date the message was sent (i.e., day, month, and year).
- Subject—Subject of the message.
- Lines—Number of lines of text in the message.
- From—The name of the person who sent the message.
- Read/Rcvd—Total number of responses read and received for that message. If there are no responses to a message, no totals will be indicated.

|                                                                                                                |                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/020.png) | NOTE: When listing new messages, all new message information is displayed in detail, regardless of the message reader you choose. Also, the list of messages will be displayed in the order you set when using the User Options Edit option to set your preferences. |

|                                                                                                                |                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/021.png) | REF: For more information on setting your preferences, please refer to the *MailMan Getting Started Guide*. |

After displaying the list of new messages, MailMan asks you to enter a message number or specific command at the "Enter message number or command:" prompt.

You can enter any of the following:

- Message Number—Enter a specific message number from the list.
- MailMan Internal Message Identification Number—Enter the MailMan internal message identification number for any message located on the system (i.e., the number in brackets).

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/022.png) | NOTE: The message does not have to be in the message list displayed or in your mailbox; however, it must still be on the system. |

- Action Code—Enter an action code to take action on any message(s) in the list of new messages.

|                                                                                                                |                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/023.png) | REF: For a complete list and description of command action codes, please refer to the "Action Codes—Baskets" topic and Table 3‑1 in Chapter 3 in this manual. |

- Caret ("^")—Enter a caret to quit the option.

### List All of Your Priority Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When MailMan delivers priority mail to your mailbox, you get a special notification, as shown below:

Select ISC OFFICE MENU OPTIONS Option: 4 \<ENTER\> MailMan Menu

All Baskets, New Priority messages: 3

\*=New/!=Priority............Subject..................Lines.From........Read/Rcvd

!23. IN \[1223285\] 08/04/98 Priority Three 1 XMUSER3,THREE

!22. IN \[1223283\] 08/04/98 Priority Two 1 XMUSER3,THREE

!21. IN \[1223282\] 08/04/98 Priority One 1 XMUSER3,THREE

VA MailMan 8.0 service for XMUSER1.ONE_E+@REDACTED.VA.GOV

You last used MailMan: 07/28/98@09:06

Your current banner: "Read the Manual....Please!"

You have 3 new messages.

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

You have 3 new messages. (Last arrival: 07/28/98@09:11)

There is PRIORITY Mail!

Select MailMan Menu Option:

<span id="_Ref426862683" class="anchor"></span>Figure 2‑5. MailMan highlights priority mail

Figure 2‑5 shows you how MailMan notifies you that you have priority mail prior to your executing any of the MailMan Menu options.

For example, when first entering the MailMan Menu, MailMan displays any new priority message(s) before displaying the MailMan Menu.

|                                                                                                                |                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/024.png) | NOTE: The priority message is indicated by an exclamation point ("!") next to each priority message. |

Also, MailMan displays the phrase "There is PRIORITY Mail!" following your MailMan Menu. As a further highlight, all priority messages displayed to you in a list will be preceded by an exclamation point.

You can list all of your priority mail in your mailbox, regardless of the mail basket, when you choose the List all Priority messages option available with the New Messages and Responses option \[XMNEW; synonym NML\], as shown below:

Select MailMan Menu Option: NML \<Enter\> New Messages and Responses

You have new mail in more than one basket.

Select New mail option: Read new mail by basket// LP \<Enter\> List all Priority messages

All Baskets, New Priority messages: 3

\*=New/!=Priority............Subject..................Lines.From........Read/Rcvd

! 1. IN \[1223285\] 08/04/98 Priority Three 1 XMUSER3,THREE

! 2. IN \[1223283\] 08/04/98 Priority Two 1 XMUSER3,THREE

! 3. IN \[1223282\] 08/04/98 Priority One 1 XMUSER3,THREE

Enter message number or command:

<span id="_Ref426872085" class="anchor"></span>Figure 2‑6. List of priority messages

As you can see from this example (Figure 2‑6), the user has three priority messages in the "IN" mail basket.

MailMan gives you detailed information on each message including:

- Priority Flag—Exclamation point ("!") preceding each message.

|                                                                                                                |                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ![](mailman-version-8-user-guide/025.png) | NOTE: The priority flag is the exclamation point ("!"). |

- Message Numbers—1, 2, and 3 (meaningful for this list only).
- Basket—"IN" mail basket.
- MailMan Internal Message Identification Number—Displayed in message display order (in brackets):
- Message \#1 \[1223285\]
- Message \#2 \[1223283\]
- Message \#3 \[1223282\]
- Message Sent Date—08/04/98 (all sent on the same date).
- Subject—The subject of each message includes:
- Message \#1 Priority Three
- Message \#2 Priority Two
- Message \#3 Priority One
- Lines (total number of lines of text in the message)—1 (all messages only have one line of text).
- From—XMUSER3,THREE (sent all three messages).
- Read/Rcvd (total number of responses read and received for the message)—In this case, no numbers are displayed, since none of these messages had any responses.

|                                                                                                                |                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/026.png) | NOTE: When listing new messages, all new message information is displayed in detail, regardless of the message reader you choose. Also, the list of messages will be displayed in the order you set when using the User Options Edit option to set your preferences. |

|                                                                                                                |                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/027.png) | REF: For more information on setting your preferences, please refer to the *MailMan Getting Started Guide*. |

After displaying the list of priority messages, MailMan asks you to enter a message number or specific command at the "Enter message number or command:" prompt.

You can do any of the following:

- Enter a specific message number from the list in order to read that message.
- Enter the MailMan internal message identification number for any message located on the system (does *not* have to be in the message list currently displayed).
- Enter an action code to take action on any message(s) in the list of new messages.
- Enter a caret ("^") to quit the option.

|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/028.png) | NOTE: Some command actions are only available when using the Detailed Full Screen or Summary Full Screen message readers. |

|                                                                                                                |                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/029.png) | REF: For a complete list and description of command action codes, please refer to the "Action Codes—Baskets" topic and Table 3‑1 in Chapter 3 in this manual. |

If you use the List all Priority messages option and you do not have any new priority messages, MailMan will let you know. For example:

Select MailMan Menu Option: NML \<Enter\> New Messages and Responses

You have new mail in more than one basket.

Select New mail option: Read new mail by basket// LP \<Enter\> List all Priority messages

You have no new Priority messages.

<span id="_Toc436461001" class="anchor"></span>Figure 2‑7. Display when you do not have priority mail

### Print All of Your New Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can print all of your new mail in your mailbox, regardless of the mail basket, when you choose the Print all new messages option available with the New Messages and Responses option \[XMNEW; synonym NML\], as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

You have 2 new messages. (Last arrival: 08/02/99@14:39)

Select MailMan Menu Option: nml \<Enter\> New Messages and Responses

Select New mail option: Read new mail by basket// p \<Enter\> Print all new messages

DEVICE: HOME// C6_AD_6FLR L16

Do you want your output QUEUED? NO// \<Enter\> (NO)

.

.

.

.

<span id="_Ref426876599" class="anchor"></span>Figure 2‑8. Printing all new mail

In this example (Figure 2‑8), the user used the Print all new messages option to print all of the new messages. MailMan asked her to choose where to print her messages (i.e., what device). In this case, the user chose to print the messages to a specific printer by entering the printer name (i.e., "C6_AD_6FLR L16") at the "DEVICE: HOME//" prompt.

MailMan then immediately printed all of the new messages.

|                                                                                                                |                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/030.png) | NOTE: If you want to print your message(s) to a different device, enter the appropriate device name at the "DEVICE: HOME//" prompt. |

MailMan displays the print information prior to the message header for each message, as shown below:

MailMan message for XMUSER1,ONE E. COMPUTER SPECIALIST

Printed at REDACTED.VA.GOV 08/02/99@14:41

<span id="_Ref448826603" class="anchor"></span>Figure 2‑9. Sample MailMan print information

This print information (Figure 2‑9) helps you differentiate:

- Who—For whom was the message printed (i.e., XMUSER1,ONE E. COMPUTER SPECIALIST).
- Where—At what location was the message printed (i.e., Printed at REDACTED.VA.GOV).
- When—When was the message printed (i.e., 08/02/99@14:41 as opposed to when the message was actually sent).

|                                                                                                                |                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/031.png) | NOTE: If you use the Print new messages by basket option to print all of your new mail, MailMan first prints any new priority mail in your mailbox before printing other new mail in your mailbox. |

### Scan All of Your New Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Scanning your new messages is similar to reading your new messages by basket; however, when scanning messages, you are not prompted between baskets. You automatically pass from reading new messages in one basket to reading the new messages in the next basket without any user prompts or user action required in between.

|                                                                                                                |                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/032.png) | REF: For more information on reading your new mail by basket, please refer to the "Read All of Your New Mail by Basket" topic previously described in this chapter. |

You can scan all of your new mail in your mailbox, regardless of the mail basket, when you choose the Scan all new messages option available with the New Messages and Responses option \[XMNEW; synonym NML\], as shown below:

Select MailMan Menu Option: NML\<Enter\> New Messages and Responses

You have new mail in more than one basket.

Select New mail option: Read new mail by basket// S \<Enter\> Scan all new messages

Subj: Digest bat-list.v004.n177 \[#1222920\]

Sat, 08/01/98@18:47:44 -0700 (PDT) 654 lines

From: bat-list-errors@lists.xxxx.com In 'IN' basket. Page

------------------------------------------------------------

.

.

.

Enter RETURN to continue or '^' to exit: \<Enter\>

<span id="_Ref427388609" class="anchor"></span>Figure 2‑10. Scanning your new mail

In the previous example (Figure 2‑10), the user chose to scan through the mail by choosing the Scan all new messages option at the "Select New mail option:" prompt. Scanning automatically begins displaying all new mail in each mail basket (mail baskets are scanned in alphabetic order). Unlike the Read new mail by basket option (Figure 2‑2), the Scan all new messages option will *not* prompt you when MailMan has displayed all the new mail in one basket and is ready to scan the new mail in the next mail basket.

As you continuously press the \<Enter\> key, MailMan automatically displays your new mail until there is no more new mail. If you want to quit scanning your new mail before reaching the end, simply enter the caret ("^") to exit the option.

|                                                                                                                |                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/033.png) | NOTE: If you use the Scan new messages by basket option to "scan" through all of your new mail, MailMan first displays any new priority mail in your mailbox before displaying the other new mail in your mailbox. |

### Quit—Exiting the New Messages Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As its name implies, you use the Quit option to "quit" processing your new mail, as shown below:

Select New mail option: Read new mail by basket// ?

Enter a code from the list.

Select one of the following:

LB List Baskets with new mail

LN List all New messages

LP List all Priority messages

P Print all new messages

Q Quit

R Read new mail by basket

S Scan all new messages

Select New mail option: Read new mail by basket// Q \<Enter\> Quit

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

<span id="_Ref427389391" class="anchor"></span>Figure 2‑11. Quit option

As you can see from this example (Figure 2‑11), the Quit option takes you immediately out of the New Messages and Responses option \[XMNEW; synonym NML\] and puts you back into the MailMan Menu (main menu).

|                                                                                                                |                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/034.png) | NOTE: Entering a caret ("^") has the same effect as Quit. |

### Stop Reading a Message—Exiting a Message with Unread (New) Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan does not force you to read an entire message or any of its responses. You can enter the caret ("^") at any point while reading a message in order to stop reading that message or any of its responses.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/035.png) | NOTE: If you use the caret to stop reading a new message without reading all responses and "ignore" that message, the message will *not* remain marked as "new," even though you have new (unread) responses. If you enter the caret at the "Enter message action" prompt, however, the message will remain marked as "new." |

After entering the caret, MailMan indicates the range of unread responses (if any) and gives you the chance to continue reading the responses, as shown below:

Subj: Test – Exiting a Message with Unread Responses \[#29408875\]

04/16/99@14:18 23 lines

From: XMUSER35,THIRTY5 - SYSTEMS ANALYST (Albany CIO Field Office)

0 of 3 responses read. In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

This is a test message with multiple responses.

.

.

.

Enter RETURN to continue or '^' to exit: ^

\>\> You haven't read responses 1-3. You may backup to see them. \<\<

Enter message action (in IN basket): IGNORE//

<span id="_Ref449168519" class="anchor"></span>Figure 2‑12. Example of exiting a message with unread responses

In this example (Figure 2‑12), the user began reading a message but chose to stop reading the entire message and any of its responses by entering a caret ("^") at the "Enter RETURN to continue or '^' to exit:" prompt.

MailMan notified the user that she had not read a range of responses (i.e., "\>\> You haven't read responses 1-3. You may backup to see them. \<\<") and presented her with the "Enter message action (in IN basket): IGNORE//" prompt. If the user entered a "B" (Backup) at this prompt, MailMan would back up to the first unread response.

|                                                                                                                |                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/036.png) | REF: For more information on the Backup action command or any other message action command, please refer to Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

# Reading/Managing Messages—In a Basket

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics to be discussed in this chapter:

- RML—Read/Manage Messages Option
- Action Codes—Baskets
- Message Number ("n") Action
- Message Selection Actions
- Change Basket Name ("C") Action
- Change Detail ("CD") Action
- Delete Messages ("D") Action
- Forward Messages ("F") Action
- Filter Messages ("FI") Action
- Headerless Print Messages ("H") Action
- Later Messages ("L") Action
- New Message List ("N") Action
- New Toggle ("NT") Action
- Opposite Selection Toggle ("O") Action
- Print Messages ("P") Action
- Query (Search for) Messages in this Basket ("Q") Action
- Resequence Messages ("R") Action
- Save Messages to Another Basket ("S") Action
- Terminate Messages ("T") Action
- Vaporize Date Edit ("V") Action
- Zoom Selection Toggle ("Z") Action
- Paging Actions
- Text String Search Actions
- Caret ("^") Exit Action

The features and functionality associated with managing *all* of your messages are described in greater detail in this chapter.

### RML—Read/Manage Messages Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Read/Manage Messages option \[XMREAD; synonym RML\] to better manage your e-mail. It allows you to perform numerous actions on both new and existing messages stored on the system (e.g., in a particular mail basket, mailbox, etc.).

|                                                                                                                |                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/037.png) | NOTE: The number of actions available to you depends on whether you are using the Detailed/Summary Full Screen message readers or the Classic message reader. |

As long as a message is still in the MESSAGE file (#3.9) and you are a recipient or sender of the message, it is available to you.

The Read/Manage Messages option \[XMREAD; synonym RML\] is available on the main MailMan Menu, as shown below:

NML New Messages and Responses

RML Read/Manage Messages \[XMREAD\]

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: RML \<Enter\> Read/Manage Messages

<span id="_Toc436461006" class="anchor"></span>Figure 3‑1. RML—Read/Manage Messages option

After selecting the Read/Manage Messages option \[XMREAD; synonym RML\], you can begin to manage your mail within each of your mail baskets, for example:

Select MailMan Menu Option: RML \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// MailMan \<Enter\> (5 messages)

MailMan Basket, 5 messages (1-5)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

5\. \[1225160\] 08/17/98 MailMan surprise 3 XMUSER43,FORTY3 1/1

4\. \[1190657\] 11/07/97 I'm so excited... 59 XMUSER2,TWO 733/733

3\. \[1182059\] 08/29/97 RFC 822 Sender 355 \<fjx@xxxxx.com\> 1/1

2\. \[1028185\] 04/02/96 MAILMAN CUSTOM HEADERS 20 XMUSER43,FORTY3 2/2

1\. \[1019674\] 03/15/96 imap.vs.pop (fwd) 717 \<fjx@xxxx.com\>

Enter message number or command:

<span id="_Ref428261584" class="anchor"></span>Figure 3‑2. Managing your mail in your mail baskets

In the previous example (Figure 3‑2), after selecting the Read/Manage Messages option (RML), MailMan prompted the user to choose a message reader. The user chose the Detailed Full Screen message reader (default) as the message reader by pressing the \<Enter\> key at the "Select message reader: Detailed Full Screen//" prompt.

MailMan then prompted the user to choose the mail basket. The user entered "MailMan" at the "Read mail in MAIL BASKET: IN//" prompt. Because the user chose the Detailed Full Screen message reader, MailMan displayed a detailed list of all new and existing messages in the "MailMan" mail basket. For this example, in this basket, the user did not have any new messages (no asterisk to the left of any message number).

At this point, the user can take any number of actions on any or all of the messages in this basket (e.g., read a message).

|                                                                                                                |                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/038.png) | REF: For a complete list and description of command action codes for baskets, please refer to the "Action Codes—Baskets" topic and Table 3‑1 that follows in this chapter. |

### Action Codes—Baskets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists *all* of the possible actions that you can perform after listing messages in a particular mail basket when using either the Detailed or Summary Full Screen message reader. Many, but not all, of these action codes are also available with MailMan's Classic message reader (exceptions are noted below):

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action Code</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>n</strong></td>
<td>Message Number ("<strong>n</strong>")—Enter the message number "<strong>n</strong>" from the list or the MailMan internal message identification number in order to read a specific message located anywhere on the system.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="even">
<td><strong>.n</strong></td>
<td>Select Message "<strong>n</strong>" (for subsequent action)—The decimal point ("<strong>.</strong>" period) before the message number ("<strong>n</strong>") tells MailMan to select the message for subsequent action.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="odd">
<td><strong>.-n</strong></td>
<td>Deselect Message "<strong>n</strong>"—The decimal point ("<strong>.</strong>" period) and minus sign<br />
("<strong>-</strong>" hyphen) before the message number ("<strong>n</strong>") tells MailMan to deselect a previously selected message.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="even">
<td><strong>.n-m,a,c-d</strong></td>
<td>Select a List of Messages (for subsequent group action)—The decimal point ("<strong>.</strong>" period) before the message numbers ("<strong>n-m,a,c-d</strong>") tells MailMan to select messages for subsequent group action.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="odd">
<td><strong>.-n-m,a,c-d</strong></td>
<td>Deselect a List of Messages—The decimal point ("<strong>.</strong>" period) and minus sign<br />
("<strong>-</strong>" hyphen) before the message numbers ("<strong>n-m,a,c-d</strong>") tells MailMan to deselect messages.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="even">
<td><strong>.*</strong></td>
<td>Select All Messages (for subsequent group action)—The decimal point ("<strong>.</strong>" period) before the asterisk ("<strong>*</strong>") tells MailMan to select <em>all</em> messages for subsequent group action.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="odd">
<td><strong>.-*</strong></td>
<td>Deselect All Messages—The decimal point ("<strong>.</strong>" period) and minus sign<br />
("<strong>-</strong>" hyphen) before the asterisk ("<strong>*</strong>") tells MailMan to deselect <em>all</em> messages previously selected.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="even">
<td><strong>C</strong></td>
<td>Change the Name of this Basket—Change the name of any mail basket in your mailbox except the "IN" and "WASTE" baskets.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="odd">
<td><strong>CD</strong></td>
<td>Change Detail—Switch between Summary and Detailed Full Screen displays.<br />
(<em>Not available with the Classic message reader; however, accomplishes what one or two question marks do at the message action prompt with the Classic message reader.</em>)</td>
</tr>
<tr class="even">
<td><strong>D</strong></td>
<td>Delete Messages—MailMan allows you to specify a range or list of messages for deletion from a basket. Moves messages to the "WASTE" basket. The messages are <em>not</em> permanently deleted from your mailbox or the system until all recipients delete or terminate the message.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="odd">
<td><strong>F</strong></td>
<td>Forward Messages—MailMan allows you to specify a range or list of messages to be forwarded from a basket. Sends messages to another individual or group of individuals specified at the "Forward mail to:" prompt.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="even">
<td><strong>FI</strong></td>
<td>Filter Messages—Filter messages in a basket based on mail filters you've previously established for your mailbox.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="odd">
<td><strong>H</strong></td>
<td>Headerless Print Messages—Print messages to any device that you choose <em>without</em> the print and header information. MailMan only prints the body of the message.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="even">
<td><strong>L</strong></td>
<td>Later Messages—MailMan allows you to specify a range or list of messages to be "latered" in a basket. Makes messages "new" for a specified later date and time; it can act as a reminder or tickler.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="odd">
<td><strong>N</strong></td>
<td>New Messages—MailMan displays all "new" messages in a basket (i.e., asterisk appears to the left of the message).<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="even">
<td><strong>NT</strong></td>
<td>New Toggle Messages—Use this toggle to make messages "new" or "not new."<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="odd">
<td><strong>O</strong></td>
<td>Opposite Selection Toggle (for subsequent group action)—Use this toggle to deselect previously selected messages and select previously unselected messages from a list of messages. This action code is only available when messages have been selected for subsequent group action.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="even">
<td><strong>P</strong></td>
<td>Print Messages—Print messages to any device you choose.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="odd">
<td><strong>Q</strong></td>
<td>Query (Search for) Messages in this Basket—Search for messages based on criteria you enter.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="even">
<td><strong>R</strong></td>
<td>Resequence Messages—Resequence the order of messages in a mail basket. All messages will be resequenced in the order of their MailMan internal message identification numbers.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="odd">
<td><strong>S</strong></td>
<td>Save Messages to Another Basket—Save messages to another existing mail basket or create a new mail basket.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="even">
<td><strong>T</strong></td>
<td>Terminate Messages—Move messages to the "WASTE" basket and permanently delete the messages from your mailbox. You will <em>not</em> receive further replies to those messages. Messages are not permanently deleted from the system until all recipients of the messages have deleted or terminated them.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="odd">
<td><strong>X</strong></td>
<td>Toggle the transmit priority in remote message queues.<br />
<em>(Postmaster Only)</em></td>
</tr>
<tr class="even">
<td><strong>Z</strong></td>
<td>Zoom Selection Toggle (for subsequent group action)—Use this toggle to zoom in and only display <em>selected</em> messages or zoom out and display <em>all</em> messages. This action code is only available when messages have been selected for subsequent group action.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="odd">
<td><strong>=</strong></td>
<td>Refresh Page—The equal sign ("<strong>=</strong>") tells MailMan to redisplay the basket message list page you were viewing ("refresh" the page/screen).<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="even">
<td><strong>+</strong></td>
<td>Next Page—The plus sign ("<strong>+</strong>") tells MailMan to go to the next page. This action code is only available when you have more than one "page" of messages when using the Detailed or Summary Full Screen message readers.<br />
<em>(Use the <strong>&lt;Enter&gt;</strong> key with the Classic message reader.</em>)</td>
</tr>
<tr class="odd">
<td><strong>+n</strong></td>
<td>Page Forward "<strong>n</strong>" Pages—The plus sign ("<strong>+</strong>") before a number ("<strong>n</strong>") tells MailMan to go forward "<strong>n</strong>" pages. This action code is only available when you have more than one "page" of messages when using the Detailed or Summary Full Screen message readers.<br />
<em>(Use the <strong>&lt;Enter&gt;</strong> key with the Classic message reader.</em>)</td>
</tr>
<tr class="even">
<td><strong>-</strong></td>
<td>Previous Page—The minus sign ("<strong>-</strong>" hyphen) tells MailMan to go to the previous page. This action code is only available when you have more than one "page" of messages.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="odd">
<td><strong>-n</strong></td>
<td>Page Back n Pages—The minus sign ("<strong>-</strong>" hyphen) before a number ("<strong>n</strong>") tells MailMan to go back "<strong>n</strong>" pages. This action code is only available when you have more than one "page" of messages.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="even">
<td><br />
<strong>0</strong></td>
<td>First Page—A zero tells MailMan to go to the first page. This action code is only available when you have more than one "page" of messages.<br />
(<em>Not available with the Classic message reader.</em>)</td>
</tr>
<tr class="odd">
<td><strong>?string</strong></td>
<td>Search for messages in the basket whose subject contains the string entered.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="even">
<td><strong>??string</strong></td>
<td>Search for messages anywhere on the system, which you ever sent or received, whose subject begins with the string entered.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
<tr class="odd">
<td><strong>^</strong></td>
<td>Exit the List (caret, "<strong>^</strong>")—Exit from the list of messages.<br />
(<em>Available with all message readers.</em>)</td>
</tr>
</tbody>
</table>

<span id="_Ref142975956" class="anchor"></span>Table 3‑1. Action Codes—Basket message lists

|                                                                                                                |                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/039.png) | NOTE: Please remember that not all action codes are available with every message list or with every message reader. Some action codes are only available when certain conditions exist. |

|                                                                                                                |                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/040.png) | NOTE: Each action code is described in greater detail in the topics that follow. |

### Message Number ("n") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), you can select any message from a list of messages by entering its basket message number ("n") at the "Enter message number or command:" prompt.

Also, you can enter the MailMan internal message identification number (i.e., the number generated by MailMan and placed in brackets, such as \[#1222162\]) for any message residing on the system, regardless of where it is located (e.g., another mail basket). As long as it is still stored in the MESSAGE file (#3.9) and you either sent or received the message, it will be located and displayed to you.

The following figure shows you how to display a message by entering the basket message number:

Select MailMan Menu Option: RML \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (7 messages, 2 new)

IN Basket, 7 messages (1-7), 2 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*7. \[1222389\] 07/28/98 NET-MEETING TRAINING ON NOIS 6 XMUSER10,TEN 3/4

\*6. \[1222306\] 07/28/98 Local: biweekly info exchange 2 POSTMASTER 11/12

5\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

4\. \[1221885\] 07/24/98 Here we come.... 55 Thirty5 Xmuser35 \<xtt@x

3\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50 "Xmuser41, Forty1" \<xmu

2\. \[1220526\] 07/14/98 Local: biweekly info exchang 2 POSTMASTER 23/23

1\. \[1208986\] 04/15/98 Halon replacement 2 XMUSER34,THIRTY4 22/22

Enter message number or command: 5

Subj: BLUE \[#1222162\] 07/27/98@09:59 1 line

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Test Message

Enter message action (in IN basket): IGNORE// \<Enter\>

IN Basket, 7 messages (1-7), 2 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*7. \[1222389\] 07/28/98 NET-MEETING TRAINING ON NOIS 6 XMUSER10,TEN 3/4

\*6. \[1222306\] 07/28/98 Local: biweekly info exchang 2 POSTMASTER 11/12

5\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

4\. \[1221885\] 07/24/98 Here we come.... 55 Thirty5 Xmuser35 \<xtt@x

3\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50 "Xmuser41, Forty1" \<xmu

2\. \[1220526\] 07/14/98 Local: biweekly info exchang 2 POSTMASTER 23/23

1\. \[1208986\] 04/15/98 Halon replacement 2 XMUSER34,THIRTY4 22/22

Enter message number or command:

<span id="_Hlt426343252" class="anchor"></span>Figure 3‑3. Displaying a message using the basket message number

As you can see from the previous example (Figure 3‑3), the user was reading mail in the "IN" mail basket and entered the basket message number (i.e., "5") of the message she wanted to read at the "Enter message number or command:" prompt. MailMan found the desired message and displayed it to her.

When the user was finished with the message, she pressed the \<Enter\> key to ignore the message and leave it in the "IN" basket.

MailMan then returned the user to the "IN" basket list of messages where she could take any additional actions on the list of messages in that basket.

The following figure (Figure 3‑4) shows you how to display a message by entering its MailMan internal message identification number:

Select MailMan Menu Option: read \<Enter\> /Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// TEST \<Enter\> (5 messages)

TEST Basket, 5 messages (1-5)

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

5\. \[1214467\] 06/02/98 Priority test \#1 1 XMUSER2,TWO M. 5/5

4\. \[1212175\] 05/12/98 New Test Message 3 XMUSER1,ONE E.

3\. \[1212173\] 05/12/98 Copy of: Test message 55 XMUSER1,ONE E.

2\. \[1212124\] 05/12/98 test 1 XMUSER1,ONE E.

1\. \[1211500\] 05/06/98 Test 1 XMUSER1,ONE E.

Enter message number or command: 1222162

Subj: BLUE \[#1222162\] 07/27/98@09:59 1 line

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

In 'IN' basket. Page 1

-----------------------------------------------------------

Test Message

Enter message action (in IN basket): IGNORE// \<Enter\>

TEST Basket, 5 messages (1-5)

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

5\. \[1214467\] 06/02/98 Priority test \#1 1 XMUSER2,TWO M. 5/5

4\. \[1212175\] 05/12/98 New Test Message 3 XMUSER1,ONE E.

3\. \[1212173\] 05/12/98 Copy of: Test message 55 XMUSER1,ONE E.

2\. \[1212124\] 05/12/98 test 1 XMUSER1,ONE E.

1\. \[1211500\] 05/06/98 Test 1 XMUSER1,ONE E.

Enter message number or command:

<span id="_Ref426341828" class="anchor"></span>Figure 3‑4. Displaying a message using the internal message identification number

As you can see from this example (Figure 3‑4), the user was reading mail in the "TEST" mail basket; however, she wanted to see a message in the "IN" basket. Thus, she entered the MailMan internal message identification number of that particular message in the "IN" basket (i.e., "1222162," Figure 3‑3) at the "Enter message number or command:" prompt. MailMan found the desired message and displayed it to the user.

When she was finished with the message, she pressed the \<Enter\> key to ignore the message and leave it in the "IN" basket.

MailMan then returned the user back to the "TEST" basket list of messages so she could make another choice.

This functionality allows you to easily retrieve a message from anywhere on the system without having to know where it is located. As long as it exists in the MESSAGE file (#3.9), you should be able to call it up.

### Message Selection Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can select messages in a list of messages for *subsequent* group actions.

You can select and deselect any combination of messages from a list of messages and then perform an action or actions on the selected group, such as:

- Delete the selected message(s)
- Filter the selected message(s)
- Forward the selected message(s)
- Later the selected message(s)
- Make the selected message(s) "New" or *not* "New"
- Print the selected message(s) to the screen or another device you choose
- Save the selected message(s) to another basket
- Terminate the selected message(s)

All message selection action codes begin with a decimal point ("." period) and you can do either of the following:

- Select Messages—When you want to *select* messages, you first enter the decimal point ("." period), followed by the message number ("n"), including ranges of messages ("n-m,a,c-d"), or all messages ("\*"). You can enter the message numbers in any order. The message selection action codes consist of the following:
- .n
- .n-m,a,c-d
- .\*
- Deselect Messages—When you want to *deselect* messages, you first enter the decimal point ("." period), then a minus sign ("-" or hyphen on the keyboard), followed by the message number ("n"), including ranges of messages ("n-m,a,c-d"), or all messages ("\*"). You can enter the message numbers in any order. The message selection action codes consist of the following:
- .-n
- .-n-m,a,c-d
- .-\*

|                                                                                                                |                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/041.png) | NOTE: All of the message selection action codes are described in greater detail in the topics that follow. |

The following action codes (described later on in this chapter) work in conjunction with the message selection action codes:

- The Opposite Selection Toggle—Toggling this action code deselects selected messages and selects unselected messages. You can toggle back and forth choosing which messages are selected or deselected.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/042.png) | TIP: At the "Enter message number or command" prompt, with one or more messages selected for subsequent group action, you can use the Opposite Selection Toggle ("O") action code to deselect all the selected messages and select all the unselected messages. This might be useful when you wish to take different actions on two groups of messages. |

- The Zoom Selection Toggle—Toggling this action code either zooms in on selected messages or zooms out to all messages. You can toggle back and forth to just view the selected messages or view the entire list of messages.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/043.png) | TIP: At the "Enter message number or command" prompt, with one or more messages selected for subsequent group action, you can use the Zoom Selection Toggle ("Z") action code to "zoom in on" (i.e., list) only those messages you've selected. This might be useful when you have several screens filled with messages. By using this tool, you can pare down the display to just list those selected messages. To restore the full list of messages (i.e., selected and not selected messages), toggle back by using the Zoom Selection Toggle again. |

|                                                                                                                |                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/044.png) | REF: For more information on the Opposite Selection Toggle and Zoom Selection toggles, please refer to the "Opposite Selection Toggle ("O") Action" and "Zoom Selection Toggle ("Z") Action" topics that follow in this chapter. |

Also, when you select messages in a mail basket, they will only remain selected while you continue processing messages in the same basket. Upon exiting that mail basket or quitting MailMan, those messages will automatically be deselected.

For example:

> 1\. You first use the message selection action codes to select a group of messages in your "IN" basket (the messages are now selected for subsequent group action).

> 2\. You then decide to go to your "TEST" mail basket to process other messages.

> 3\. You then return to your "IN" mail basket (where you originally selected the messages, Step 1). You'll see that those previously selected messages will no longer be selected.  

> Because you left and returned to the "IN" basket, those previously selected messages will no longer be selected. You would have to reselect the messages in the "IN" basket, if you still wanted to perform some group actions on those messages.

#### Selecting Messages

.n—Selecting One Message

As you can see from the list of action codes (Table 3‑1), to select a *single* message for subsequent action, you must first enter a decimal point ("." period) and then the number ("n") you wish to select from the list of messages (i.e., ".n").

When you have successfully selected messages, a right-angle bracket ("\>") is displayed to the left of the selected messages in the list, as shown below:

Select MailMan Menu Option: RML \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen//

Read mail in MAIL BASKET: IN// Trans \<Enter\> portation News (7 messages, 7 new)

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n183 750 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n183 797 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command: .4

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n183 750 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\>\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n183 797 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427133686" class="anchor"></span>Figure 3‑5. Selecting a single message for subsequent action

In this example (Figure 3‑5), the user selected message number 4 from the list of messages in the "Transportation News" mail basket by entering ".4" at the "Enter message number or command:" prompt. (Make sure you include the decimal point.)

MailMan then redisplays the list. You'll notice that a right-angle bracket ("\>") appears to the left of message number 4 in the list.

The user can now take any number of actions on this message.

  
.n-m,a,c-d—Selecting a Group of Messages

As you can see from the list of action codes (Table 3‑1), to select a *group* of messages for subsequent group action, you first enter a decimal point ("." period) and then any combination of message numbers and/or ranges separated by commas (no spaces) you wish to select from the list of messages (i.e., ".n-m,a,c-d"). You can enter the message numbers in any order. A hyphen ("-") between numbers indicates a range of message numbers.

When you have successfully selected messages, a right-angle bracket ("\>") is displayed to the left of the selected messages in the list, as shown below:

Select MailMan Menu Option: RML \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// Trans \<Enter\> portation News (7 messages, 7 new)

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject................... Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n192 600 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command: .1-3,6,7

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject................... Lines.From..........Read/Rcvd

\>\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n192 600 bat-list-errors@lists.x

\>\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\>\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427135087" class="anchor"></span>Figure 3‑6. Selecting a group of messages for subsequent group action

In this example (Figure 3‑6), the user selected message numbers 1 through 3, message number 6, and message number 7 from the list of messages in the "Transportation News" mail basket by entering ".1-3,6,7" at the "Enter message number or command:" prompt. The user could have entered the message numbers in any order. (Make sure you include the decimal point, hyphens, and commas where appropriate, omitting any spaces.)

MailMan then redisplays the list. You'll notice that right-angle brackets ("\>") appear to the left of the selected message numbers in the list (i.e., 1, 2, 3, 6, and 7).

The user can now take any number of group actions on these messages or make additional selections.

  
.\*—Selecting All Messages

As you can see from the list of action codes (Table 3‑1), to select *all* messages in a list for subsequent group action, you first enter a decimal point ("." period) and then an asterisk (i.e., ".\*").

When you have successfully selected all of the messages, a right-angle bracket ("\>") is displayed to the left of each message in the list, as shown below:

Select MailMan Menu Option: RML \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// Trans \<Enter\> portation News (7 messages, 7 new)

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject................... Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command: .\*

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject................... Lines.From..........Read/Rcvd

\>\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\>\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

<span id="_Ref427370518" class="anchor"></span>Figure 3‑7. Selecting all messages for action

In this example (Figure 3‑7), the user selected *all* messages (message numbers 1 through 7) from the list of messages in the "Transportation News" mail basket by entering ".\*" at the "Enter message number or command:" prompt. (Make sure you include the decimal point.)

MailMan then redisplays the list. You'll notice that right-angle brackets ("\>") appear to the left of every message number in the list.

The user can now take any number of group actions on these messages.

#### Deselecting Messages

.-n—Deselecting One Message

As you can see from the list of action codes (Table 3‑1), to deselect a previously selected message, you first enter a decimal point ("." period), followed by a minus sign ("-" or hyphen on the keyboard), and then the message number ("n") you wish to deselect from the list of messages (i.e., ".-n").

When you have successfully deselected messages, the right-angle bracket ("\>") is no longer displayed to the left of the previously selected messages in the list, as shown below:

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command: .-4

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n181 584 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427135623" class="anchor"></span>Figure 3‑8. Deselecting a single message

In this example (Figure 3‑8), the user deselected the previously selected message number 4 from the list of messages in the "Transportation News" mail basket by entering ".-4" at the "Enter message number or command:" prompt. (Make sure you include the decimal point and minus sign.)

MailMan then redisplays the list. You'll notice that the right-angle bracket ("\>") disappears from the left of message number 4 in the list. The message is no longer selected.

  
.-n-m,a,c-d—Deselecting a Group of Messages

As you can see from the list of action codes (Table 3‑1), to deselect a previously selected *group* of messages, you first enter a decimal point ("." period), followed by a minus sign ("-" or hyphen on the keyboard), and then any combination of message numbers and/or ranges separated by commas (no spaces) you wish to deselect from the list of messages (i.e., ".-n-m,a,c-d"). You can enter the message numbers in any order. A hyphen ("-") between numbers indicates a range of message numbers.

When you have successfully deselected the messages, the right-angle bracket ("\>") is no longer displayed to the left of the selected messages in the list, as shown below:

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\>\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command: .-2,6-7

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n178 954 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427136991" class="anchor"></span>Figure 3‑9. Deselecting a group of messages

In this example (Figure 3‑9), the user deselected message numbers 2 and message numbers 6 to 7 from the list of messages in the "Transportation News" mail basket by entering ".-2,6-7" at the "Enter message number or command:" prompt. The user could have entered the message numbers in any order. (Make sure you include the decimal point, minus sign/hyphens, and commas where appropriate, omitting any spaces.)

MailMan then redisplays the list. You'll notice that the right-angle bracket ("\>") disappears from the left of message numbers: 2, 6, and 7. Those messages are no longer selected; however, the right-angle bracket ("\>") remains next to message numbers 1 and 4 in the list. Those messages remain selected for subsequent group actions.

.\*—Deselecting All Messages

As you can see from the list of action codes (Table 3‑1), to deselect *all* messages in a list, you first enter a decimal point ("." period), followed by a minus sign ("-" or hyphen on the keyboard), and then an asterisk (i.e., ".-\*").

When you have successfully deselected all of the messages, the right-angle bracket ("\>") is no longer displayed to the left of each message in the list, as shown below:

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\>\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\>\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n178 584 bat-list-errors@lists.x

\>\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\>\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command: .-\*

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n178 554 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n181 584 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427371169" class="anchor"></span>Figure 3‑10. Deselecting all messages

In this example (Figure 3‑10), the user deselected all messages (message numbers 1 through 7) from the list of messages in the "Transportation News" mail basket by entering ".-\*" at the "Enter message number or command:" prompt. (Make sure you include the decimal point and minus sign prior to the asterisk.)

MailMan then redisplays the list. You'll notice that the right-angle brackets ("\>") disappear from the left of every message number in the list. The messages are no longer selected.

You do not have to have *all* messages selected in order to use ".-\*". The ".-\*" will deselect any messages you have previously selected.

### Change Basket Name ("C") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Change Basket action code (i.e., "C") allows you to rename the mail basket you are currently processing to any valid mail basket name. You are *not* allowed to change the "WASTE" or "IN" mail basket names, however.

|                                                                                                                |                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/045.png) | REF: For more information on naming your mail baskets, please refer to the "Name Your Mail Baskets" topic in Chapter 3 in the *MailMan Getting Started Guide*. |

To change a mail basket name, enter a "C" at the "Enter message number or command:" prompt, as shown below:

Read mail in MAIL BASKET: IN// Test Save\<Enter\> (1 message)

Test Save Basket, 1 message

\*=New/!=Priority........Subject...................Lines.From..........Read/Rcvd

2\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command: C

Enter a new basket name: Test Save// TEST II

TEST II Basket, 1 message

\*=New/!=Priority........Subject...................Lines.From..........Read/Rcvd

2\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command:

<span id="_Ref429466828" class="anchor"></span>Figure 3‑11. Changing a mail basket name

In this example (Figure 3‑11), the user wanted to rename the "Test Save" mail basket to "TEST II." From the Read/Mange Messages option, he entered "Test Save" at the "Read mail in MAIL BASKET: IN//" prompt. MailMan displayed the list of messages currently in the "Test Save" mail basket. In this case, the user only had one message in that basket.

In order to change this basket's name the user entered a "C" (Change Basket Name) at the "Enter message number or command:" prompt.

MailMan then asked the user for the new basket name. He entered "TEST II" at the "Enter a new basket name: Test Save//" prompt.

MailMan then redisplayed the basket with its new name indicated and placed the user at the message action prompt where he can take any additional actions on the list of message in that basket.

### Change Detail ("CD") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), when viewing a list of messages you can use the Change Detail ("CD") action code to toggle between the Summary and Detailed Full Screen message readers list of messages. Simply entering the Change Detail ("CD") command at the "Enter message number or command:" prompt causes the message reader to toggle.

Depending on which message reader you've selected (i.e., Detailed or Summary Full Screen), this command either: removes several columns from the display, giving the remaining columns space to display more information in a more streamlined fashion or adds several columns from the display, giving you more information about each message.

|                                                                                                                |                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/046.png) | NOTE: The Change Detail ("CD") command is similar to entering one question mark (for summary information) or two question marks (for detailed information) at the message action prompt when using the Classic message reader. |

The following columns of data are present in the Detailed Full Screen message reader and absent from the Summary Full Screen message reader:

- MailMan Internal Message Identification Number—The MailMan message number generated internally for each message (displayed in brackets).
- Message Sent Date—The date each message was sent (i.e., day, month, and year).
- Lines—The number of lines of text in each message.
- Read/Rcvd—The number of responses read and received for each message.

For example, by removing these columns (i.e., going from detailed information to summary information), the remaining message Subject and From columns have more room to display in the listing. Thus, you can see more of the pertinent data (i.e., subject title and who sent the message to you), all with a less cluttered view, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// Trans \<Enter\> portation News (7 messages, 7 new)

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject................... Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n185 626 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n186 514 bat-list-errors@lists.x

\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n187 563 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n181 584 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command: CD

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority.......Subject.........................From....................

\*7. Digest bat-list.v004.n184 bat-list-errors@lists.xxxx.c

\*6. Digest bat-list.v004.n185 bat-list-errors@lists.xxxx.c

\*5. Digest bat-list.v004.n186 bat-list-errors@lists.xxxx.c

\*4. Digest bat-list.v004.n187 bat-list-errors@lists.xxxx.c

\*3. Digest bat-list.v004.n181 bat-list-errors@lists.xxxx.c

\*2. Digest bat-list.v004.n183 bat-list-errors@lists.xxxx.c

\*1. Digest bat-list.v004.n182 bat-list-errors@lists.xxxx.c

Enter message number or command:

<span id="_Ref427373082" class="anchor"></span>Figure 3‑12. Changing from detailed information to summary information

In this example (Figure 3‑12), the user was using the Detailed Full Screen message reader to manage the mail in the "Transportation News" mail basket. When the user entered "CD" (Change Detail) at the "Enter message number or command:" prompt, the display changed from detailed information to summary information that only included:

- Flags—Any special flags associated with the messages in the basket (e.g., New \[\*\] flag).
- Message Numbers—The numbers associated with the messages in the mail basket.
- Subject—Subject of each message in the mail basket.
- From—The name of the person who sent each message in the mail basket.

|                                                                                                                |                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/047.png) | NOTE: Going from detailed information to summary information with the Detailed Full Screen message reader is equivalent to entering a single question mark after the message action prompt when using the Classic message reader. |

In the following example (Figure 3‑13), the user changed detail from summary information to detailed information, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// summary\<Enter\> Summary Full Screen

Read mail in MAIL BASKET: IN// Transportation News (7 messages, 7 new)

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority.......Subject.........................From........................

\*7. Digest bat-list.v004.n184 bat-list-errors@lists.xxxx.c

\*6. Digest bat-list.v004.n185 bat-list-errors@lists.xxxx.c

\*5. Digest bat-list.v004.n186 bat-list-errors@lists.xxxx.c

\*4. Digest bat-list.v004.n187 bat-list-errors@lists.xxxx.c

\*3. Digest bat-list.v004.n181 bat-list-errors@lists.xxxx.c

\*2. Digest bat-list.v004.n183 bat-list-errors@lists.xxxx.c

\*1. Digest bat-list.v004.n182 bat-list-errors@lists.xxxx.c

Enter message number or command: CD

Transportation News Basket, 7 messages (1-7), 7 new

\*=New/!=Priority........Subject................... Lines.From..........Read/Rcvd

\*7. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.x

\*6. \[1223638\] 08/06/98 Digest bat-list.v004.n185 626 bat-list-errors@lists.x

\*5. \[1223666\] 08/06/98 Digest bat-list.v004.n186 514 bat-list-errors@lists.x

\*4. \[1223680\] 08/06/98 Digest bat-list.v004.n187 563 bat-list-errors@lists.x

\*3. \[1223730\] 08/04/98 Digest bat-list.v004.n181 584 bat-list-errors@lists.x

\*2. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.x

\*1. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427373722" class="anchor"></span>Figure 3‑13. Changing from summary information to detailed information

In this example (Figure 3‑13), the user first selected the Summary Full Screen message reader to manage the mail in the "Transportation News" mail basket. MailMan displayed all of the messages in the mail basket and only included the message number, message subject, and message sender. When the user entered "CD" (Change Detail) at the "Enter message number or command:" prompt, the display changed from summary information to detailed information that included:

- Flags—Any special flags associated with the messages in the basket (e.g., New \[\*\] flag).
- Message Numbers—The numbers associated with the messages in the mail basket.
- MailMan Internal Message Identification Number—The MailMan message number generated internally for each message (displayed in brackets).
- Message Sent Date—The date each message was sent (i.e., day, month, and year).
- Subject—Subject of each message in the mail basket.
- Lines—The number of lines of text in each message in the mail basket.
- From—The name of the person who sent each message in the mail basket.
- Read/Rcvd—Total number of responses read and received for a message. If there are no responses to a message, no totals will be indicated.

|                                                                                                                |                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/048.png) | NOTE: Going from summary information to detailed information with the Summary Full Screen message reader is equivalent to entering two question marks after the message action prompt when using the Classic message reader. |

### Delete Messages ("D") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Delete action code (i.e., "D") allows you to delete messages from your mail baskets by moving them to the "WASTE" basket. MailMan allows you to delete any selection, range, or all messages in a mail basket.

Generally, a batch job is run nightly (determined by Information Resource Management \[IRM\] at your site) to remove messages from your "WASTE" basket, and thus, from your mailbox. You can immediately remove a message from your mailbox by, again, deleting the message from your "WASTE" basket; however, the message remains in the system until all recipients of the message have deleted it from their mailbox.

Unlike the Terminate action code, the Delete action code will *not* prevent responses to a "deleted" message from "resurrecting" or restoring a message back into your mailbox.

|                                                                                                                |                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/049.png) | REF: For more information on the Terminate action code, please refer to the "Terminate Messages ("T") Action" topic that follows in this chapter. |

To delete messages from a mail basket, enter a "D" at the "Enter message number or command:" prompt, as shown below:

IN Basket, 8 messages (1-8)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

8\. \[1224355\] 08/11/98 Priority message 1 XMUSER4,FOUR

7\. \[1224353\] 08/11/98 Priority Mail 1 XMUSER1,ONE E.

6\. \[1223228\] 08/04/98 Stress management exercise 16 XMUSER4,FOUR

5\. \[1222306\] 07/28/98 Local: biweekly info exchange 2 POSTMASTER 70/70

4\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

3\. \[1221643\] 07/22/98 Copy of: Deleting files 3/6 1

2\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50

1\. \[1220526\] 07/14/98 Local: biweekly info exchang 2

Enter message number or command: D

Delete which messages: (1-8): 1-3,7,8

Do you really want to delete these messages? No// y \<Enter\> YES

5 messages deleted.

Press RETURN to continue: \<Enter\>

IN Basket, 3 messages (4-6)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

6\. \[1223228\] 08/04/98 Stress management exercise 16 XMUSER4,FOUR

5\. \[1222306\] 07/28/98 Local: biweekly info exchang 2 POSTMASTER 70/70

4\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

Enter message number or command:

<span id="_Ref429467592" class="anchor"></span>Figure 3‑14. Deleting messages from a mail basket

In the previous example (Figure 3‑14), the user wanted to delete five messages from a mail basket. While in the "IN" basket, she entered "D" (Delete) at the "Enter message number or command:" prompt. MailMan asked the user which messages to delete. As a default, MailMan listed the entire range of messages in the basket (i.e., 1 through 8). For this example, the user entered "1-3,7,8" at the "Delete which messages: (1-8):" prompt. The user was telling MailMan that she wanted to delete message numbers 1 through 3, 7, and 8. She could have entered the message numbers in any order.

Before deleting those messages, MailMan wanted the user to verify that she really wanted to delete those messages. Since she did, she entered "Yes" at the "Do you really want to delete these messages? No//" prompt. MailMan confirmed that four messages had been deleted.

When the user pressed the \<Enter\> key, MailMan redisplayed the "IN" basket list of messages (minus the deleted messages) where she could take any additional actions on the list of remaining messages in that basket.

|                                                   |                                                                                                                                                                                                                                                 |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/050.png) | TIP: You can "un-delete" a message by going to your "WASTE" basket and saving the deleted message back to another mail basket. Thus, you can retrieve any message you deleted, if it's still on the system and you know the message number. |

#### How Do I Delete a Mail Basket?

You can only delete an empty mail basket. Thus, you first must delete all messages from a basket that you intend on deleting. Once the mail basket is empty and you try to enter it, MailMan will ask you if you want to now delete it, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: R \<Enter\> Read/Manage Messages

Read mail in MAIL BASKET: IN// Mail

1 MailMan (5 messages)

2 MailMan 2 (0 messages)

CHOOSE 1-2: 2 \<Enter\> MailMan 2 (0 messages)

No messages in basket.

Since the 'MailMan' basket is empty,

do you want to delete it? YES// \<Enter\>

Basket deleted.

<span id="_Ref429468479" class="anchor"></span>Figure 3‑15. Deleting an already empty mail basket

As you can see from this previous example (Figure 3‑15), using the Read/Manage Messages option (RML), the user selected an already empty mail basket (i.e., "MailMan 2"). MailMan notified the user that the mail basket was empty (i.e., "No messages in basket."). Because it was empty, MailMan immediately asked the user if he wanted to delete it. In this case, he did. Thus, he accepted the "Yes" response by pressing the \<Enter\> key at the "Since the 'MailMan' basket is empty, do you want to delete it? YES//" prompt. MailMan confirmed that the mail basket had been deleted.

In the following example (Figure 3‑16), the user wants to delete the "Transportation News" mail basket, however, it is not empty. Thus, the user must first delete all messages in that basket and then delete the basket itself, as shown below:

Select MailMan Menu Option: rml\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// Trans \<Enter\> portation News (5 messages)

Transportation News Basket, 5 messages (1-5)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

5\. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.x

4\. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

3\. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

2\. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

1\. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command: .1-5

Transportation News Basket, 5 messages (1-5)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\> 5. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.x

\> 4. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

\> 3. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

\> 2. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

\> 1. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command: d

Are you sure you want to delete the selected messages? NO// y \<Enter\> YES

5 messages deleted.

Press RETURN to continue: \<Enter\>

No messages in basket.

Since the 'Transportation News' basket is empty,

do you want to delete it? YES// \<Enter\>

Basket deleted.

Read mail in MAIL BASKET: IN// ^

<span id="_Ref429468922" class="anchor"></span>Figure 3‑16. Deleting a mail basket after deleting all messages from that basket

To delete the "Transportation News" basket, the user first had to delete all the messages currently resident in that basket. Thus, the user first grouped all five messages by entering ".1-5" at the "Enter message number or command:" prompt. MailMan redisplayed the list of messages indicating that they were now grouped (i.e., displayed "\>" to the left of each message).

|                                                                                                                |                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/051.png) | REF: For more information on grouping messages, please refer to the "Message Selection Actions" topic previously described in this chapter. |

After grouping the messages, the user deleted all five messages by entering a "D" (Delete) at the "Enter message number or command:" prompt.

MailMan asked the user to confirm the delete. He confirmed the delete request by entering "Yes" at the "Are you sure you want to delete the selected messages? NO//" prompt.

MailMan then notified the user that all five messages had been deleted and that the mail basket was now empty.

MailMan then automatically asked the user if he wanted to delete the empty mail basket. Since he did, he accepted the "Yes" default response by pressing the \<Enter\> key at the "Since the 'Transportation News' basket is empty, do you want to delete it? YES//" prompt. MailMan, again, confirmed that the basket had been deleted.

### Forward Messages ("F") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Forward action code (i.e., "F") allows you to send messages from your mailbox to other recipients currently not on the message. MailMan allows you to forward any selection, range, or all messages in a mail basket.

To forward a message in a mail basket, enter an "F" at the "Enter message number or command:" prompt, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// TEST II\<Enter\> (4 messages)

TEST II Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

2\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command: F

Forward which messages: (1-4): 2-4

Forward mail to: xmuser2 \<Enter\> ,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 07/30/98@14:54

On vacation 31 July through 16 August.

And Forward to: \<Enter\>

3 messages forwarded.

Press RETURN to continue: \<Enter\>

TEST II Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From.........Read/Rcvd

4\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

2\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command:

<span id="_Ref429469370" class="anchor"></span>Figure 3‑17. Forwarding messages from a mail basket

In this example (Figure 3‑17), the user wanted to forward three messages to another recipient. While in the "TEST II" basket, the user entered an "F" (Forward) at the "Enter message number or command:" prompt.

MailMan then asked the user which messages she wanted to forward. In this case, she wanted to forward message numbers 2, 3, and 4, so she entered "2-4" at the "Forward which messages: (1-4):" prompt. The user could have entered the message numbers in any order (e.g., "4-2" or "3,2,4").

MailMan then asked the user to enter the addressees. For this example, she decided to forward the message to Two Xmuser2 by entering "XMUSER2,TWO M." at the "Forward mail to:" prompt.

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/052.png) | REF: For more information on addressing a message, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

MailMan knew the user was finished forwarding the message when she pressed the \<Enter\> key at the "And Forward to:" prompt without entering another recipient's name.

MailMan confirmed that the three messages had been forwarded. After pressing the \<Enter\> key, MailMan redisplayed the "TEST II" basket list of messages where she could take any additional actions on the list of message in that basket.

### Filter Messages ("FI") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan V. 8.0 allows you to filter your mail. You can create any number of filters to automatically send your mail to any specified mail basket in your mailbox based on various filtering criteria:

- Subject
- Sender
- Addressee

Sometimes, when managing mail in your mail baskets, you may find old messages that came into your mailbox *prior* to your creation of mail filters. As you can see from the list of action codes (Table 3‑1), you can use the Filter messages action code (i.e., "FI") to filter these "old" messages and move them to the proper mail basket (determined by your mail filters). MailMan allows you to filter any selection, range, or all messages in a mail basket.

|                                                                                                                |                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/053.png) | REF: For more information on filtering your mail and setting up mail filters, please refer to Chapter 7, "Filtering Mail," in this manual. |

By entering the Filter messages ("FI") command at the "Enter message number or command:" prompt, you can process all of your messages in a mail basket through your established mail filters, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (15 messages, 11

IN Basket, 15 messages (1-15), 11 new

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

\*15. \[1223844\] 08/07/98 SVC-News: SVC SIG NEWS UPDA 57

\*14. \[1223740\] 08/05/98 SVC-News: TOUCHSTONE '98 NE 50

\*13. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.

\*12. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.

\*11. \[1223730\] 08/04/98 Digest bat-list.v004.n181 584 bat-list-errors@lists.

\*10. \[1223680\] 08/06/98 Digest bat-list.v004.n187 563 bat-list-errors@lists.

\* 9. \[1223666\] 08/06/98 Digest bat-list.v004.n186 514 bat-list-errors@lists.

\* 8. \[1223638\] 08/06/98 Digest bat-list.v004.n185 626 bat-list-errors@lists.

\* 7. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.

6\. \[1223228\] 08/04/98 Stress management exercise 16 XMUSER4,FOUR

\* 5. \[1222306\] 07/28/98 Local: biweekly info exchang 2 POSTMASTER 61/63

4\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

! 3. \[1221643\] 07/22/98 Copy of: Deleting files 3/6 11 XMUSER8,EIGHT 12/13

2\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50 "Xmuser41, Forty1" \<x

1\. \[1220526\] 07/14/98 Local: biweekly info exchang 2 POSTMASTER 23/23

Enter message number or command: FI

Filter which messages: (1-15): 1-15

15 messages filtered.

Press RETURN to continue:

<span id="_Ref427377573" class="anchor"></span>Figure 3‑18. Filtering messages

As you can see from the previous example (Figure 3‑18), the user was managing their mail in the "IN" basket. Of the total 15 messages in the mail basket, 7 messages were from the same sender and had similar subjects (i.e., message numbers 7 through 13, shown in boldface type). These messages were sent to the user prior to the creation of a new mail filter (process not shown). This new mail filter was created to filter all messages whose subject contains "Digest bat" to the "Transportation News" mail basket. Thus, the user wanted to filter these previously sent messages through the new mail filter by entering "FI" at the "Enter message number or command:" prompt.

MailMan then prompted the user to enter which messages from the list he wanted to filter. The user chose to send all the messages through the filters by entering "1-15" at the "Filter which messages: (1-15):" prompt.

After processing the messages, MailMan replied that all 15 of the messages had been filtered.

|                                                                                                                |                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/054.png) | NOTE: If any other of these messages had matched the filtering criteria on any of the other mail filters, they too would have been filtered from the "IN" basket. |

Pressing the \<Enter\> key redisplayed the list of messages in the "IN" basket after the user filtered the messages, as shown below:

IN Basket, 8 messages (1-15), 4 new

\*=New/!=Priority.........Subject....................Lines.From.......Read/Rcvd

\*15. \[1223844\] 08/07/98 SVC-News: SVC SIG NE

\*14. \[1223740\] 08/05/98 SVC-News: TOUCHSTONE

6\. \[1223228\] 08/04/98 Stress management ex

\* 5. \[1222306\] 07/28/98 Local: biweekly info 61/63

4\. \[1222162\] 07/27/98 BLUE

! 3. \[1221643\] 07/22/98 Copy of: Deleting file 12/13

2\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs Wh xmuse

1\. \[1220526\] 07/14/98 Local: biweekly info exchange 2 POSTMASTER 23/23

Enter message number or command:

<span id="_Ref427379614" class="anchor"></span>Figure 3‑19. Filtered messages removed from the "IN" basket

Here you see the "IN" basket messages redisplayed (Figure 3‑19). You'll notice that messages 7-13 are no longer in the "IN" basket (Figure 3‑18).

All the messages in the "IN" basket went through the mail filters. Because messages 7-13 had subjects containing the phrase "Digest bat," they were caught by one of the mail filters and redirected to the "Transportation News" mail basket, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// Trans \<Enter\> portation News (12 messages, 7 new)

Transportation News Basket, 12 messages (1-12), 7 new

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

\*12. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.

\*11. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.

\*10. \[1223730\] 08/04/98 Digest bat-list.v004.n181 584 bat-list-errors@lists.

\* 9. \[1223680\] 08/06/98 Digest bat-list.v004.n187 563 bat-list-errors@lists.

\* 8. \[1223666\] 08/06/98 Digest bat-list.v004.n186 514 bat-list-errors@lists.

\* 7. \[1223638\] 08/06/98 Digest bat-list.v004.n185 626 bat-list-errors@lists.

\* 6. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.

5\. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.

4\. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.

3\. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.

2\. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.

1\. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.

Enter message number or command:<span id="_Hlt449851545" class="anchor"></span>

Figure 3‑20. Filtered messages in the "Transportation News" basket

As you can see messages 7-13 in the "IN" basket (Figure 3‑18, shown in boldface type) were filtered to the "Transportation News" basket as messages 6-12 (Figure 3‑20, shown in boldface type).

### Headerless Print Messages ("H") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Headerless Print action code (i.e., "H") allows you to print messages in a mail basket without a header. Unlike the Print Messages action code, the Headerless Print Messages action code will *not* print any "Print" information or the "Subject" and "From" information (i.e., the header), only the text of the message (including responses, if any) is printed.

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/055.png) | REF: For more information on the Print Messages action code, please refer to the "Print Messages ("P") Action" topic that follows in this chapter. |

MailMan allows you to print any selection, range, or all messages in a mail basket. If you choose to print to the screen, MailMan will prompt you to press the \<Enter\> key after each message is printed.

Also, as with all print commands, you can specify any print device (e.g., the monitor/screen or a printer).

To print a message in a mail basket without a header (i.e., Headerless Print), enter an "H" at the "Enter message number or command:" prompt, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (4 messages)

IN Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1223228\] 08/04/98 Stress management exercise 16 XMUSER4,FOUR

3\. \[1222306\] 07/28/98 Local: biweekly info exchang 2 POSTMASTER 70/70

2\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

1\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50 "Xmuser41, Forty1" \<xmu

Enter message number or command: H

Print which messages without headers: (1-4): 2

Print recipient list? No// y\<Enter\> YES

Select one of the following:

D Detail

S Summary

Print Detail or Summary recipient chain: Summary// \<Enter\>

DEVICE: HOME// \<Enter\> Telnet terminal

Test message text.

Local Message-ID: 1222162@REDACTED.VA.GOV (2 Recipients)

This message was addressed as follows:

XMUSER2,TWO M.

XMUSER1,ONE E.

Enter RETURN to continue or '^' to exit: \<Enter\>

1 message printed.

Press RETURN to continue: \<Enter\>

<span id="_Ref430664187" class="anchor"></span>Figure 3‑21. Headerless print of a message in a mail basket

In this example (Figure 3‑21), the user wanted to print a single message *without* a header. While in the "IN" basket, the user entered an "H" (Headerless Print) at the "Enter message number or command:" prompt.

MailMan then asked the user which messages she wanted to print. In this case, she wanted to print message number 2, so she entered "2" at the "Print which messages without headers: (1-4):" prompt.

MailMan then asked the user if she wanted to print the recipient list. Since she did, she entered "Yes" at the "Print recipient list? No//" prompt.

The user was then given the choice of printing either a "Detail" or "Summary" list of recipients:

- Summary list (default)—The Summary list provides the same information you see when you do a query on a message (i.e., Query action code).

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/056.png) | REF: For more information on the Query action code, please refer to Table 4‑1 and the "Query ("Q") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

- Detail list—The Detail list provides the same information you see when you do a detailed query on a message (i.e., Query Detailed action code).

|                                                                                                                |                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/057.png) | REF: For more information on the Query action code, please refer to Table 4‑1 and the "Query Detailed ("QD") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

In this case, the user chose to print a Summary list (default). Thus, she accepted the default response by pressing the \<Enter\> key at the "Print Detail or Summary recipient chain: Summary//" prompt.

MailMan then asked the user to choose where to print the message (i.e., what device). In this case, the user chose to print the message to the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt.

|                                                                                                                |                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/058.png) | NOTE: If you want to print your message(s) to a different device (e.g., a printer), enter the appropriate device name at the "DEVICE: HOME//" prompt. |

MailMan immediately printed the message and recipient information to the screen (the device choice) and, after pressing the \<Enter\> key, MailMan informed the user that one message had been printed.

Because this was a "Headerless" print, MailMan did *not* print any "Print" information or the "Subject" and "From" information (i.e., the header), only the text of the message is printed. Also, since she wanted to print recipient information, a Summary list of recipients was included.

Pressing the \<Enter\> key, again, returned the user to the list of messages in the "IN" basket where she could take additional actions. If she had selected more than one message to print, pressing the \<Enter\> key would have printed the next message.

### Later Messages ("L") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Later action code (i.e., "L") makes messages "new" at a specified later date and time. If the messages already reside in your mailbox, they will simply be made "new" again. If the messages no longer reside in your mailbox, they will be redelivered to your mailbox as "new" messages. This can serve as a reminder to yourself. MailMan allows you to later any selection, range, or all messages in a mail basket.

MailMan also gives you the option to review (list) all messages with "latered" dates and times using the Report on Later'd Messages option and make any modifications to those dates and times using the Change/Delete Later'd Messages option.

|                                                                                                                |                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/059.png) | REF: For more information on the Report on Later'd Messages and Change/Delete Later'd Messages options, please refer to the "Get a Report On "Latered" Messages in Your Mailbox" and "Change/Delete a Message's "Latered" Date and Time" topics in Chapter 11, "Reports and Lists," in this manual. |

To "Later" messages in a mail basket, enter an "L" at the "Enter message number or command:" prompt, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// TEST II\<Enter\> (4 messages)

TEST II Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

2\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command: L

Later which messages: (1-4): 1-2

DATE MESSAGE WILL BE NEW: T+1// \<Enter\> (AUG 13, 1998)

2 messages latered.

Press RETURN to continue: \<Enter\>

TEST II Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

2\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command:

<span id="_Ref430745494" class="anchor"></span>Figure 3‑22. "Latering" messages in a basket

In the previous example (Figure 3‑22), the user wanted to make messages new at a later date and time ("Later" messages). While in the "TEST II" basket, the user entered an "L" (Later) at the "Enter message number or command:" prompt.

MailMan then asked the user which messages he wanted to "later." In this case, he wanted to later messages number 1 and 2, so he entered "1-2" at the "Later which messages: (1-4):" prompt.

MailMan then asked the user when he wanted the messages to be made new again. MailMan will set the default to be the next day (i.e., T+1, where T represents today's date). For this example, the user chose to accept the default by pressing the \<Enter\> key at the "DATE MESSAGE WILL BE NEW: T+1//" prompt. MailMan displayed the "later" date (i.e., "AUG 13, 1998") and informed the user that the two messages had been "latered."

Pressing the \<Enter\> key returned the user to the list of messages in the "TEST II" basket where he could take any additional actions on the list of message in that basket.

### New Message List ("N") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the New Message List action code (i.e., "N") will just display the new messages from a list of messages in a mail basket. This can be useful if you have a mail basket with a large number of messages and you just want to see/read the new messages.

To list just the new messages in a mail basket, enter an "N" at the "Enter message number or command:" prompt, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// Transportation News (10 messages, 5 new)

Transportation News Basket, 10 messages (1-10), 5 new

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

\*10. \[1224153\] 08/10/98 Digest bat-list.v004.n189 693 bat-list-errors@lists.

\* 9. \[1223785\] 08/07/98 Digest bat-list.v004.n188 625 bat-list-errors@lists.

\* 8. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.

\* 7. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.

\* 6. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.

5\. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.

4\. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.

3\. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.

2\. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.

1\. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.

Enter message number or command: N

Transportation News Basket, New messages: 5

\*=New/!=Priority........Subject....................Lines.From.........Read/Rcvd

\*1. \[1224153\] 08/10/98 Digest bat-list.v004.n189 693 bat-list-errors@lists.

\*2. \[1223785\] 08/07/98 Digest bat-list.v004.n188 625 bat-list-errors@lists.

\*3. \[1223733\] 08/04/98 Digest bat-list.v004.n182 954 bat-list-errors@lists.

\*4. \[1223731\] 08/06/98 Digest bat-list.v004.n183 738 bat-list-errors@lists.

\*5. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.

Enter message number or command:

<span id="_Ref430746185" class="anchor"></span>Figure 3‑23. New message list in a mail basket

In this example (Figure 3‑23), the user wanted to only list the new messages in the "Transportation News" mail basket. When the user first listed messages in the "Transportation News" basket she saw that she had 10 messages and that 5 of the messages were new. In order to just list the new messages, she entered an "N" at the "Enter message number or command:" prompt.

MailMan then redisplayed the list of messages in the "Transportation News" basket, however, this time only the five new messages were listed.

The user could now take any actions on the list of new messages.

### New Toggle ("NT") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), you can use the New Toggle action code (i.e., "NT") to:

- Make message(s) "new"—MailMan *adds* the new flag (i.e., "\*" asterisk) next to the message, as if it has not been opened/read yet.
- Make "new" message(s) *not* appear as "new"—MailMan *removes* the new flag (i.e., "\*" asterisk) next to the messages, as if they were already opened/read.

You can toggle between these two actions with this one action code. This can be useful when you want to make messages that you've already read appear as new again so that MailMan will indicate that you have new messages, acting as a reminder of important activities. Thus, MailMan becomes a personal reminder. Alternatively, you may have a mail basket with a number of "new" messages and you do not want them to be listed as "new" but indicated as if you have already read the messages (i.e., no asterisk displayed next to the message, "*not* new"). MailMan allows you to "new toggle" any selection, range, or all messages in a mail basket.

To toggle messages in a mail basket from "new" to "*not* new" or vice versa, enter an "NT" at the "Enter message number or command:" prompt, as shown below:

IN Basket, 5 messages (1-5), 3 new

\*=New/!=Priority............Subject.................Lines.From........Read/Rcvd

\* 1. IN \[100539\] 08/02/99 ASKDJF 1 XMUSER2,TWO

\* 2. IN \[100573\] 08/31/99 TEST 1 1 \<XMUSER2.TWO_M+@ISC-

\* 3. IN \[100600\] 09/09/99 test brodcast 1 XMUSER2,TWO

4\. IN \[100607\] 09/15/99 TEST WAIT 1 XMUSER2,TWO

5\. IN \[100648\] 10/28/99 TEST BCAST 1 XMUSER2,TWO

Enter message number or command: nt

New Toggle which messages: (1-5): 4-5

2 messages new toggled.

Press RETURN to continue: \<Enter\>

IN Basket, 5 messages (1-5), 5 new

\*=New/!=Priority............Subject.................Lines.From........Read/Rcvd

\* 1. IN \[100539\] 08/02/99 ASKDJF 1 XMUSER2,TWO

\* 2. IN \[100573\] 08/31/99 TEST 1 1 \<XMUSER2.TWO_M+@ISC-

\* 3. IN \[100600\] 09/09/99 test brodcast 1 XMUSER2,TWO

\* 4. IN \[100607\] 09/15/99 TEST WAIT 1 XMUSER2,TWO

\* 5. IN \[100648\] 10/28/99 TEST BCAST 1 XMUSER2,TWO

Enter message number or command:

<span id="_Ref106520249" class="anchor"></span>Figure 3‑24. Selecting messages to make "new" or "not new" using the New toggle

In this example (Figure 3‑24), the user wanted to make several messages appear as new messages, as if he had not read them yet, even though he had already opened/read them in the "IN" mail basket. When the user first listed messages in the "IN" basket he saw that he had five messages and that three of the messages were new (i.e., #1, \#2, and \#3, with the asterisk next to each number) and two messages that had already been opened/read (i.e., #4 and \#5). In order to make *all* messages appear as new, he entered an "NT" at the "Enter message number or command:" prompt.

MailMan then asked the user which messages he wanted to toggle, in this case the user chose to toggle messages \#4 and \#5 as new messages by entering "4-5" after the "New Toggle which messages: (1-5):" prompt. MailMan confirmed that two messages were toggled (i.e., "2 messages new toggled.").

After pressing the \<Enter\> key, MailMan redisplayed the list of messages in the "IN" basket, however, this time all five messages appeared as new (i.e., #1, \#2, \#3, \#4, and \#5 all had an asterisk next to their numbers).

The user could now take any actions on the list of new messages.

### Opposite Selection Toggle ("O") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), you can use the Opposite Selection Toggle action code (i.e., "O") to reverse or choose the opposite of your selected messages in a list of messages. Using this action code allows you to simply select unselected messages and deselect previously selected messages. This can be useful when you have a long list of messages and the majority of the messages will undergo the same action. It's easier to select a smaller group that will not be changing, and then, using the Opposite Selection Toggle, to reverse your selection and perform the action on the majority of the opposite messages in the message list.

In order to use the Opposite Selection Toggle, you must have first selected at least one message in the list of messages. When you have successfully selected messages, a right-angle bracket ("\>") is displayed to the left of the selected messages in the list.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/060.png) | REF: For more information on selecting messages for subsequent group actions, please refer to the "Message Selection Actions" topic previously described in this chapter. |

The following series of screen captures (Figure 3‑25, Figure 3‑26, and Figure 3‑27) better illustrates how the Opposite Selection Toggle works.

The user first must select some messages in the list of messages, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// Trans \<Enter\> portation News (8 messages, 1 new)

Transportation News Basket, 8 messages (1-8), 1 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*8. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.x

7\. \[1223267\] 08/04/98 Digest bat-list.v004.n180 619 bat-list-errors@lists.x

6\. \[1223232\] 08/04/98 Digest bat-list.v004.n179 622 bat-list-errors@lists.x

5\. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.x

4\. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

3\. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

2\. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

1\. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command: .1,3

Transportation News Basket, 8 messages (1-8), 1 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*8. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.x

7\. \[1223267\] 08/04/98 Digest bat-list.v004.n180 619 bat-list-errors@lists.x

6\. \[1223232\] 08/04/98 Digest bat-list.v004.n179 622 bat-list-errors@lists.x

5\. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.x

4\. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

\> 3. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

2\. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

\> 1. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427397170" class="anchor"></span>Figure 3‑25. Selecting messages to demonstrate the Opposite Selection toggle (1 of 3)

As you can see from the previous figure (Figure 3‑25), the user selected messages 1 and 3 in the list of messages in the "Transportation News" mail basket by entering ".1,3" at the "Enter message number or command:" prompt. Once the messages have been selected (indicated by the "\>"), MailMan allows the user to use the Opposite Selection Toggle action (Figure 3‑26).

To toggle from the selected messages to the unselected messages or vice versa, you enter "O" at the "Enter message number or command:" prompt, as shown below:

Enter message number or command: O

Transportation News Basket, 8 messages (1-8), 1 new

\*=New/!=Priority.........Subject............

\>\*8. \[1223634\] 08/06/98 Digest bat-list.v004.n179 622 bat-list-errors@lists.x

\> 7. \[1223267\] 08/04/98 Digest bat-list.v004.n179 622 bat-list-errors@lists.x

\> 6. \[1223232\] 08/04/98 Digest bat-list.v004.n179 622 bat-list-errors@lists.x

\> 5. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.x

\> 4. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

3\. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

\> 2. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

1\. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427397146" class="anchor"></span>Figure 3‑26. Using the Opposite Selection toggle action code to select the opposite messages (2 of 3)

In this example (Figure 3‑26), entering "O" at the "Enter message number or command:" prompt tells MailMan to deselect the original messages (i.e., 1 and 3) and to select the remaining messages (i.e., message number 2 and messages 4 through 8). Thus, MailMan selected the opposite set of messages and deselected the original set of selected messages.

Finally, the user used the Opposite Selection Toggle to toggle back to the original selection of messages, as shown below:

Enter message number or command: O

Transportation News Basket, 8 messages (1-8), 1 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*8. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.x

7\. \[1223267\] 08/04/98 Digest bat-list.v004.n180 619 bat-list-errors@lists.x

6\. \[1223232\] 08/04/98 Digest bat-list.v004.n179 622 bat-list-errors@lists.x

5\. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.x

4\. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

\> 3. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

2\. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

\> 1. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427398147" class="anchor"></span>Figure 3‑27. Using the Opposite Selection toggle action code to reselect the original messages (3 of 3)

In this last example of the series (Figure 3‑27), entering "O" again at the "Enter message number or command:" prompt tells MailMan to reselect the original messages (i.e., 1 and 3) and to deselect the remaining messages (i.e., message number 2 and messages 4 through 8). Thus, MailMan deselected the opposite set of messages and reselected the original set of messages. The display looks like it did when the user first selected the messages (Figure 3‑25).

### Print Messages ("P") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Print action code (i.e., "P") allows you to print messages in a mail basket. Unlike the Headerless Print Messages action code, the Print Messages action code will print the "Print" information and the "Subject" and "From" information (i.e., the header) as well as the text of the message (including responses, if any).

|                                                                                                                |                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/061.png) | REF: For more information on the Headerless Print Messages action code, please refer to the "Headerless Print Messages ("H") Action" topic previously described in this chapter. |

MailMan allows you to print any selection, range, or all messages in a mail basket. If you choose to print to the screen, MailMan will prompt you to press the \<Enter\> key after each message.

Also, as with all print commands, you can specify any print device (e.g., the monitor/screen or a printer).

To print messages in a mail basket, enter a "P" at the "Enter message number or command:" prompt, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// TEST II\<Enter\> (4 messages)

TEST II Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

2\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command: P

Print which messages: (1-4): 1

Print recipient list? No// \<Enter\> NO

DEVICE: HOME// \<Enter\> Telnet terminal

MailMan message for XMUSER1,ONE E. COMPUTER SPECIALIST

Printed at REDACTED.VA.GOV 08/12/98@14:30

Subj: test \[#1223222\] 08/04/98@08:14 1 line

From: XMUSER4,FOUR - Q... Continuum In 'TEST II' basket. Page 1

-------------------------------------------------------------------------------

test

Enter RETURN to continue or '^' to exit: \<Enter\>

1 message printed.

Press RETURN to continue: \<Enter\>

TEST II Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

2\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command:

<span id="_Ref431007779" class="anchor"></span>Figure 3‑28. Printing a message from a mail basket without recipient information

In this example (Figure 3‑28), the user wanted to print a message. While in the "TEST II" basket, she entered a "P" (Print) at the "Enter message number or command:" prompt.

MailMan then asked the user which messages she wanted to print. In this case, she wanted to print message number 1, so she entered "1" at the "Print which messages: (1-4):" prompt.

MailMan then asked the user if she wanted to print the recipient list. Since she did not, she accepted the default ("No") by pressing the \<Enter\> key after "Print recipient list? No//" prompt.

|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/062.png) | REF: For an example of printing a recipient list, please refer to the example that follows (Figure 3‑29) in this chapter. |

MailMan then asked the user to choose where to print the message (i.e., what device). In this case, the user chose to print the message to the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt.

|                                                                                                                |                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/063.png) | NOTE: If you want to print your message(s) to a different device (e.g., a printer), enter the appropriate device name at the "DEVICE: HOME//" prompt. |

MailMan immediately printed the message to the screen (the device choice) and, after pressing the \<Enter\> key, MailMan informed the user that one message had been printed.

Because this was a "normal" print, MailMan printed the "Print" information, the "Subject," and "From" information (i.e., the header) along with the text of the message.

Pressing the \<Enter\> key, again, returned the user to the list of messages in the "TEST II" basket where she could take additional actions. If the user had selected more than one message to be printed, pressing the \<Enter\> key would have printed the next message.

The following example (Figure 3‑29), illustrates printing a message with recipient information:

TEST II Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

2\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command: P

Print which messages: (1-4): 1

Print recipient list? No// y\<Enter\> YES

Select one of the following:

D Detail

S Summary

Print Detail or Summary recipient chain: Summary// \<Enter\>

DEVICE: HOME// \<Enter\> Telnet terminal

MailMan message for XMUSER1,ONE E. COMPUTER SPECIALIST

Printed at REDACTED.VA.GOV 08/12/98@14:31

Subj: test \[#1223222\] 08/04/98@08:14 1 line

From: XMUSER4,FOUR - Q... Continuum In 'TEST II' basket. Page 1

-------------------------------------------------------------------------------

test

Local Message-ID: 1223222@REDACTED.VA.GOV (2 Recipients) Delivery basket: chair

Message will be NEW on: Aug 13, 1998

This message was addressed as follows:

XMUSER1,ONE E.

XMUSER4,FOUR

Enter RETURN to continue or '^' to exit: \<Enter\>

1 message printed.

Press RETURN to continue: \<Enter\>

TEST II Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

2\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command:

<span id="_Ref431008974" class="anchor"></span>Figure 3‑29. Printing a message from a mail basket with recipient information

In this example (Figure 3‑29), the user wanted to print the same message along with the recipient information. While in the "TEST II" basket, he entered a "P" (Print) at the "Enter message number or command:" prompt.

MailMan then asked the user which messages he wanted to print. Again, he wanted to print message number 1, so he entered "1" at the "Print which messages: (1-4):" prompt.

MailMan then asked the user if he wanted to print the recipient list. In this case, he did, thus, he entered "Yes" at the "Print recipient list? No//" prompt.

The user was then given the choice of printing either a "Detail" or "Summary" list of recipients:

- Summary list (default)—The Summary list provides the same information you see when you do a query on a message (i.e., Query action code).

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/064.png) | REF: For more information on the Query action code, please refer to Table 4‑1 and the "Query ("Q") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

- Detail list—The Detail list provides the same information you see when you do a detailed query on a message (i.e., Query Detailed action code).

|                                                                                                                |                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/065.png) | REF: For more information on the Query action code, please refer to Table 4‑1 and the "Query Detailed ("QD") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

For this example, the user chose to print a Summary list (default). Thus, he accepted the default response by pressing the \<Enter\> key at the "Print Detail or Summary recipient chain: Summary//" prompt.

MailMan then asked the user to choose where to print the message (i.e., what device). In this case, the user chose to print the message to the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt.

|                                                                                                                |                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/066.png) | NOTE: If you want to print your message(s) to a different device (e.g., a printer), enter the appropriate device name at the "DEVICE: HOME//" prompt. |

MailMan immediately printed the message and recipient information to the screen (the device choice) and, after pressing the \<Enter\> key, MailMan informed the user that one message had been printed.

Because this was a "normal" print, MailMan printed the "Print" information, the "Subject," and "From" information (i.e., the header) along with the text of the message. Also, since the user wanted to print recipient information, a Summary list of recipients was included.

Pressing the \<Enter\> key, again, returned the user to the list of messages in the "TEST II" basket where he could take additional actions.

### Query (Search for) Messages in this Basket ("Q") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Query (Search for) action code (i.e., "Q") allows you to search for messages in a specific mail basket.

You can search for messages based on any combination of the following criteria:

- Subject contents—Enter a string from 3 to 30 characters in length (*not* case sensitive).
- Sender of the message—Enter the first portion of the sender's last name (*not* case sensitive) or their local DUZ (i.e., numeric user ID). If the sender is from a remote site, enter any part of the sender's name and/or site. You'll narrow your choices by entering more characters.
- Addressee/Recipient of the message—Enter any portion of the addressee's name or their local DUZ (i.e., numeric user ID). If the sender is from a remote site, enter any part of the sender's name and/or site. You'll narrow your choices by entering more characters.
- Approximately when the message was sent—Date sent range: on, before, or after the VA FileMan date you enter. (Do *not* enter a future date).
- Specific responder to a message—Enter the first portion of the responder's last name (*not* case sensitive) or their local DUZ (i.e., numeric user ID). If the sender is from a remote site, enter any part of the sender's name and/or site. You'll narrow your choices by entering more characters.
- Specific text in a message—Enter a string from 3 to 30 characters in length, you decide if the search is case sensitive and if you search just the message, just the responses or both.
- Length of a message—Specify the number of lines (or more) that the message contains.

|                                                                                                                |                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/067.png) | REF: For more information on entering names or DUZs, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

Each additional search criterion entered helps limit the search. Therefore, the more search criterion you choose, the more specific the search becomes resulting in a smaller list of messages from which to choose.

All criteria entered *must* be true in order to pass the search test. (This is similar to using the Boolean AND in Internet search engines or program code).

MailMan displays the entire list of search criteria you've selected. To cancel a single search criterion without having to start over, use the at-sign ("@") to delete the specific search criterion you no longer want.

When you have completed your search criteria, enter "G" ("Go search") to start the search. To end the query without searching, you can enter "Q" ("Quit) or enter the caret ("^") to get out of the query (search) option.

You are automatically placed in a "virtual basket" in a full-screen view to process any messages found from the search. You can take any action on the messages in this "virtual basket" that you can take in a "real" basket (e.g., read, delete, forward, save, etc.).

|                                                                                                                |                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/068.png) | REF: For more information on searching for messages, please refer to Chapter 6, "Searching Mail," in this manual. |

The following series of screen captures (Figure 3‑30, Figure 3‑31, and Figure 3‑32) better illustrates how the Query (Search) process works.

To search (query) for messages in a mail basket, enter a "Q" at the "Enter message number or command:" prompt, as shown below:

Select MailMan Menu Option: RML \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (6 messages, 1 new)

IN Basket, 6 messages (1-17), 1 new

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

\*17. \[1225128\] 08/17/98 Training by Zero XMuser0 5 XMUSER22,TWEN 18/20

16\. \[1224496\] 08/12/98 Message to Two but no me 1 XMUSER1,ONE E. 1/1

8\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

4\. \[1223228\] 08/04/98 Stress management exercise 16 XMUSER4,FOUR

2\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

1\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50 "Xmuser41, Forty1" \<xmu

Enter message number or command: Q

Current 'Mailbox' search criteria:

Search basket: IN

Select one of the following:

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Enter 'Subject contains' string//

<span id="_Ref427987121" class="anchor"></span>Figure 3‑30. Search for a message in a mail basket (1 of 3)

As you can see from this first example of the search series (Figure 3‑30), after the user entered "Q" at the "Enter message number or command:" prompt, MailMan displayed the current search criteria (i.e., search basket: "IN") and the list of search actions from which to choose.

At this point, the user can enter the search criteria and initiate a search, as shown in the next example (Figure 3‑31).

In the next example, the user entered the first search criteria:

Select search action: Enter 'Subject contains' string// \<Enter\>

Subject contains: message 1

Current 'Mailbox' search criteria:

Search basket: IN

Subject contains: message 1

Select one of the following:

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

G Go Search

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Change 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Go Search//

<span id="_Ref428064564" class="anchor"></span>Figure 3‑31. Entering search criteria (2 of 3)

In this second example of the series (Figure 3‑31), the user chose to search for messages in the "IN" basket by entering a portion of the message subject she is looking for by pressing the \<Enter\> key to accept the "S" (Subject contains) default at the "Select search action: Enter 'Subject contains' string//" prompt.

MailMan then asked the user to enter the subject string she was looking for at the "Subject contains:" prompt (i.e., "message 1").

After entering the subject contains string, MailMan immediately displayed the Current 'Mailbox' search criteria:

- Search basket—"IN"
- Subject contains—"message 1"

Also, again, the user is presented with the list of search actions from which to choose. Since she has not completed entering the search criteria, she has not started the search.

In the final example of the series, the user entered the second and last search criterion and ran the search:

Select search action: Go Search// DA\<Enter\> Enter 'Message sent on or after' date

Message sent on or after: 8/1/98 \<Enter\> (AUG 01, 1998)

Current 'Mailbox' search criteria:

Search basket: IN

Subject contains: message 1

Message sent on or after: 08/01/98

Select one of the following:

DA Change 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

G Go Search

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Change 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Go Search// \<Enter\>

Searching...

IN Basket

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

8\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

Search finished.

Enter message number or command:

<span id="_Ref428065626" class="anchor"></span>Figure 3‑32. All search criteria entered—Searching for the message (3 of 3)

In this final example of the series (Figure 3‑32), besides searching for messages based just on a subject string, the user also chose to search for messages based on the date they were sent. Thus, she entered a "DA" (Message sent on or after) at the "Select search action: Go Search//" prompt.

MailMan then asked the user to enter the date range she was looking for at the "Message sent on or after:" prompt (i.e., "8/1/98").

After entering the date, MailMan immediately displayed the search criteria:

- Search basket—"IN"
- Subject contains—"message 1"
- Message sent on or after—"08/01/98"

Also, again, the user is presented with the list of search actions from which to choose. Since she has now completed entering the search criteria, she pressed the \<Enter\> key to accept the "G" (Go search) default at the "Select search action: Go Search//" prompt. MailMan immediately began to search the "IN" mail basket and look for messages that matched the search criteria.

When MailMan found the messages in question, the user was informed the search had finished, and MailMan displayed the search results to the user in a "virtual basket."

At this point, the user could read the messages or perform any other message action on the messages found by the search.

To get back to the original "real" basket list of messages, you must enter the caret ("^") at the "Enter message number or command:" prompt and enter the caret again or enter "Q" (quit) at the "Select search action, or enter 'G' to start search:" prompt.

|                                                                                                                |                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/069.png) | REF: For more information on message action codes, please refer to the "Action Codes—Individual Messages" topic and Table 4‑1 in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

### Resequence Messages ("R") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Resequence action code (i.e., "R") allows you to renumber the message numbers in a list of messages in a mail basket. All messages will be resequenced in the order of their MailMan internal message identification numbers. This helps keep your mail basket messages more orderly by removing any "gaps" in message number sequence.

To resequence the message numbers for a group of messages in a mail basket, enter an "R" at the "Enter message number or command:" prompt, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (4 messages)

IN Basket, 4 messages (2-6)

\*=New/!=Priority........Subject....................Lines.From...

6\. \[1222162\] 07/27/98 BLUE 1 XMUSER2

5\. \[1223228\] 08/04/98 Stress management exercise 16 XMUSER4

4\. \[1222306\] 07/28/98 Local: biweekly info exchang 2 POSTMASTER

2\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50 "Xmuser41, Forty1

Enter message number or command: R

Resequencing ...

Resequenced from 1 to 4

Press RETURN to continue: \<Enter\>

IN Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1223228\] 08/04/98 Stress management exercise 16 XMUSER4,FOUR

3\. \[1222306\] 07/28/98 Local: biweekly info exchang 2 POSTMASTER 70/70

2\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

1\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50 "Xmuser41, Forty1" \<xmu

Enter message number or command:

<span id="_Ref431010775" class="anchor"></span>Figure 3‑33. Resequencing messages in a mail basket

In this example (Figure 3‑33), the user wanted to resequence messages in the "IN" mail basket. While in the "IN" basket, the user sees that he has a total of four messages; however, the message numbers range from 2 through 6 rather than 1 through 4 and have "gaps" between numbers (i.e., 2, 4, 5, and 6). Thus, to resequence the numbers and remove the gaps, the user entered an "R" (Resequence) at the "Enter message number or command:" prompt. MailMan informed the user that the message numbers were being resequenced.

When completed, MailMan displayed that the messages in the "IN" basket had been "Resequenced from 1 to 4."

Pressing the \<Enter\> key returned the user to the list of messages in the "IN" basket. The messages were reordered based on their MailMan internal message identification numbers and the messages now ranged from 1 through 4 and did *not* have any gaps (i.e., 1, 2, 3, and 4).

The user could now take any additional actions on the resequenced messages.

### Save Messages to Another Basket ("S") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Save action code (i.e., "S") allows you to save messages in a list of messages to another existing mail basket or create a new mail basket on the fly. This helps you sort your messages into the proper mail basket for easier reference. MailMan allows you to save any selection, range, or all messages in a mail basket.

To save messages from one mail basket to another, enter an "S" at the "Enter message number or command:" prompt, as shown below:

Select MailMan Menu Option: RML \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (5 messages)

IN Basket, 5 messages (2-7)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

7\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

6\. \[1223228\] 08/04/98 Stress management exercise 16 XMUSER4,FOUR

5\. \[1222306\] 07/28/98 Local: biweekly info exchang 2 POSTMASTER

4\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

2\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50 "Xmuser41, Forty1

Enter message number or command: S

Save which messages: (2-7): 7

Save messages to which basket? TEST II

1 message saved.

Press RETURN to continue: \<Enter\>

IN Basket, 4 messages (2-6)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

6\. \[1223228\] 08/04/98 Stress management exercise 16 XMUSER4,FOUR

5\. \[1222306\] 07/28/98 Local: biweekly info exchang 2 POSTMASTER 70/70

4\. \[1222162\] 07/27/98 BLUE 1 XMUSER2,TWO M.

2\. \[1220558\] 07/14/98 FW: Tribal Wisdom vs. Gover 50 "Xmuser41, Forty1" \<xmu

Enter message number or command:

<span id="_Ref431011493" class="anchor"></span>Figure 3‑34. Saving messages in a mail basket to another mail basket

In this example (Figure 3‑34), the user wanted to save (move) a message from one basket to another. While in the "IN" basket, she entered an "S" (Save) at the "Enter message number or command:" prompt.

MailMan then asked the user which messages she wanted to save. In this case, she wanted to save message number 7 from the "IN" basket into the "TEST II" basket. Thus, she entered "7" at the "Save which messages: (2-7):" and "TEST II" at the "Save messages to which basket?" prompts.

The user could have entered any or all message numbers in the "IN" basket (in any order) and chosen any new or existing mail basket. If the basket entered did *not* already exist in the user's mailbox, MailMan would give the user the chance to create the new mail basket on the fly or to choose another existing basket. In this case, the "TEST II" mail basket already existed, so the user did not have to create a new basket.

MailMan informed the user that one message had been saved.

Pressing the \<Enter\> key returned the user to the list of messages in the "IN" basket. The user could see that the message number 7 was no longer in the list of messages because it had been moved to the "TEST II" mail basket.

The user could now take any additional actions on the remaining messages.

### Terminate Messages ("T") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Terminate action code (i.e., "T") allows you to permanently delete messages from your mail baskets by moving them to the "WASTE" basket. MailMan allows you to terminate any selection, range, or all messages in a mail basket.

Generally, a batch job is run nightly (determined by IRM at your site) to remove messages from your "WASTE" basket, and thus, from your mailbox. You can immediately remove messages from your mailbox by, again, terminating the messages from your "WASTE" basket; however, the message remains in the system until all recipients of the message have deleted it from their mailbox.

Unlike the Delete action code, the Terminate action code will prevent responses to "terminated" messages from being "resurrected" or restored back into your mailbox.

|                                                                                                                |                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/070.png) | REF: For more information on the Delete action code, please refer to the "Delete Messages ("D") Action" topic previously described in this chapter. |

To terminate messages in a mail basket, enter a "T" at the "Enter message number or command:" prompt, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// TEST II\<Enter\> (4 messages)

TEST II Basket, 4 messages (1-4)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

4\. \[1224524\] 08/12/98 Forwarding a Message 2 1 XMUSER1,ONE E.

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

2\. \[1224523\] 08/12/98 Forward Message 1 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command: T

Terminate which messages: (1-4): 2,4

Do you really want to terminate these messages? No// y\<Enter\> YES

2 messages terminated.

You won't see future responses. (In WASTE basket)

Press RETURN to continue: \<Enter\>

TEST II Basket, 2 messages (1-3)

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

3\. \[1224525\] 08/12/98 Forwarding a message 3 1 XMUSER1,ONE E.

1\. \[1223222\] 08/04/98 test 1 XMUSER4,FOUR

Enter message number or command:

<span id="_Ref429470538" class="anchor"></span>Figure 3‑35. Terminating messages in a mail basket

In the previous example (Figure 3‑35), the user wanted to terminate a couple of messages from a mail basket. While in the "TEST II" basket, he entered "T" (Terminate) at the "Enter message number or command:" prompt. MailMan asked the user which messages to terminate. MailMan listed the entire range of messages in the basket (i.e., 1 through 4). For this example, the user entered "2,4" at the "Terminate which messages: (1-4):" prompt. The user was telling MailMan that he wanted to terminate messages number 2 and 4.

Before terminating those messages, MailMan wanted the user to verify that he really wanted to terminate them. Since he did, he entered "Yes" at the "Do you really want to terminate these messages? No//" prompt. MailMan confirmed that two messages had been terminated and sent to the "WASTE" basket. MailMan also informed the user that he would *not* see any future responses to those messages.

When the user pressed the \<Enter\> key, MailMan redisplayed the "TEST II" basket's list of messages (minus the terminated messages). The user could then take any additional actions on the list of remaining message in that basket.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/071.png)</td>
<td><p><strong>TIP:</strong> You can "un-terminate" a message by going to your "WASTE" basket and forwarding the terminated message back to yourself. Thus, you can retrieve any message you terminated, if it's still on the system and you know the message number. The message, however, will <em>not</em> appear as a "New" message.</p>
<p>If the message is no longer in your "WASTE" basket but you know another recipient of the message, you can ask that other recipient of the message to forward it to you. Again, the message will not appear as a "New" message in your mailbox. It would only appear as a "New" message when a new reply is sent.</p></td>
</tr>
</tbody>
</table>

### Vaporize Date Edit ("V") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 3‑1), you can use the Vaporize Date Edit action code (i.e., "V") to set a message or group of messages to be deleted from your mailbox at a specific date and time or to modify a Vaporize Date already set. You can move any messages set to vaporize to any of your mail baskets, including the "WASTE" basket, and *not* affect its vaporization date. Vaporize means automatically delete.

Vaporize dates set by you, or by MailMan during message delivery, remain with the message until the message is deleted or until you remove the vaporize date. The vaporize date remains in effect even if the message becomes new.

A message that is scheduled for vaporization, either by you or by MailMan during the IN-BASKET PURGE, will be deleted on the scheduled date without waiting for the scheduled IN BASKET PURGE process. You are free to modify or remove the AUTOMATIC DELETION DATE (i.e., vaporize date) at any time prior to the vaporization date.

Vaporize dates set by MailMan during the IN-BASKET PURGE remain with the message only as long as the message remains dormant or until the message is deleted. As soon as you read the message, save it to another basket, or it becomes new, the vaporize date will be removed.

#### Vaporizing Multiple Messages

To set a "vaporize" date for a group of messages in a basket, enter a "V" at the "Enter message number or command:" prompt, as shown below:

Kernel Basket, 3 messages (1-3)

\*=New/!=Priority........Subject...................Lines.From..........Read/Rcvd

3\. \[1407969\] 12/22/99 LOCAL KERNEL OPTIONS AT MAD 81 \<XMUSER.THREE@FORUM.VA.

2\. \[1390172\] 11/24/99 Patchs That Require A Quiet 31 XMUSER4,FOUR 10/10

1\. \[1377936\] 08/17/99 undocumented interfaces / X 13 XMUSER5,FIVE

Enter message number or command: v \<Enter\> Vaporize date set messages

Enter Vaporize Date: (8/21/2006 - 12/31/2699): 1/1/07 \<Enter\> (JAN 01, 2007)

Set the vaporize date for which messages: (1-3): 1-2

Do you really want to set the vaporize date for these messages? No// y \<Enter\> YES

2 messages vaporize date set.

Press RETURN to continue:

Kernel Basket, 3 messages (1-3)

\*=New/!=Priority........Subject...................Lines.From..........Read/Rcvd

3\. \[1407969\] 12/22/99 LOCAL KERNEL OPTIONS AT MAD 81 \<XMUSER.THREE@FORUM.VA.

2\. \[1390172\] 11/24/99 Patchs That Require A Quiet 31 XMUSER4,FOUR 10/10

1\. \[1377936\] 08/17/99 undocumented interfaces / X 13 XMUSER5,FIVE

Enter message number or command:

<span id="_Ref143923408" class="anchor"></span>Figure 3‑36. Vaporizing multiple messages

Users can also first select messages in the list of messages and then enter a "V" at the "Enter message number or command:" prompt. Once selected, a right-angle bracket ("\>") is displayed to the left of the selected messages in the list.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/072.png) | REF: For more information on selecting messages for subsequent group actions, please refer to the "Message Selection Actions" topic previously described in this chapter. |

In the previous example (Figure 3‑36), the user wanted to delete a group of messages at a specific date and time (vaporize). Thus, he entered a "V" at the "Enter message number or command:" prompt.

MailMan then asked the user to enter the "vaporize" date and time (i.e., AUTOMATIC DELETE DATE). In this case, the user chose to set a vaporize date of January1, 2007 by entering "1/1/07" at the "Enter Vaporize Date: (8/21/2006 - 12/31/2699): " prompt.

MailMan confirmed that the messages vaporize dates were set. The user can later remove or modify the vaporization dates before the messages get physically deleted from the user's mailbox.

|                                                                                                                |                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/073.png) | REF: For more information on removing a vaporize date from messages, please refer to the "Removing a Vaporization date" topic under the "Vaporize Date Edit ("V") Action" topic in Chapter 4,"Reading/Managing Messages—Individual Messages," in this manual. |

When the user pressed the \<Enter\> key, MailMan redisplayed the "kernel" basket's list of messages. The user could then take any additional actions on the list of message in that basket.

|                                                   |                                                                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/074.png) | TIP: If you know messages that will be obsolete or unnecessary after a period of time (e.g., messages advising you about a temporary event such as: system downtime, building fire alarm test, etc.) set the messages to "vaporize" after the prescribed time has passed. That way, you will not be cluttering your mailbox with extraneous mail. |

### Zoom Selection Toggle ("Z") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), the Zoom Selection Toggle is used to "zoom" in on a group of messages that have been selected for subsequent group action. Using this action code allows you to just display those selected messages and not the entire list of messages in the mail basket. This can be useful when you have a long list of messages and have selected messages throughout the entire list.

In order to use the Zoom Selection Toggle, you *must* have first selected at least one message in the list of messages. When you have selected messages, a right-angle bracket ("\>") is displayed to the left of the selected messages in the list.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/075.png) | REF: For more information on selecting messages for subsequent group actions, please refer to the "Message Selection Actions" topic previously described in this chapter. |

The following series of screen captures (Figure 3‑37, Figure 3‑38, and Figure 3‑39) better illustrates how the Zoom Selection Toggle works.

The user first *must* select some messages in the list of messages, as shown below:

Select MailMan Menu Option: RML\<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// Trans \<Enter\> portation News (8 messages, 1 new)

Transportation News Basket, 8 messages (1-8), 1 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*8. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.x

7\. \[1223267\] 08/04/98 Digest bat-list.v004.n180 619 bat-list-errors@lists.x

6\. \[1223232\] 08/04/98 Digest bat-list.v004.n179 622 bat-list-errors@lists.x

5\. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.x

4\. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

3\. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

2\. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

1\. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command: .1-4

Transportation News Basket, 8 messages (1-8), 1 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*8. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.x

7\. \[1223267\] 08/04/98 Digest bat-list.v004.n180 619 bat-list-errors@lists.x

6\. \[1223232\] 08/04/98 Digest bat-list.v004.n179 622 bat-list-errors@lists.x

5\. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.x

\> 4. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

\> 3. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

\> 2. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

\> 1. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427399004" class="anchor"></span>Figure 3‑37. Selecting messages to demonstrate the Zoom Selection toggle (1 of 3)

As you can see from the previous figure (Figure 3‑37), the user selected messages 1 through 4 in the list of messages in the "Transportation News" mail basket by entering ".1-4" at the "Enter message number or command:" prompt. Once the messages have been selected, MailMan allows the user to use the Zoom Selection Toggle action.

To zoom in on just the selected messages (and zoom out again), you enter "Z" at the "Enter message number or command:" prompt, as shown below:

Enter message number or command: Z

Transportation News Basket, 8 messages (1-8), 1 new

\*=New/!=Priority........Subject....................Lines.F

\> 4. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

\> 3. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

\> 2. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

\> 1. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command:

<span id="_Ref427455905" class="anchor"></span>Figure 3‑38. Using the Zoom Selection toggle action code to zoom in on selected messages (2 of 3)

In this example (Figure 3‑39), entering "Z" at the "Enter message number or command:" prompt tells MailMan to zoom in on and only display the selected messages (i.e., 1 through 4).

Finally, the user used the Zoom Selection Toggle to zoom back out to the original list of messages, as shown below:

Enter message number or command: Z

Transportation News Basket, 8 messages (1-8), 1 new

\*=New/!=Priority........Subject....................Lines.From..

\*8. \[1223634\] 08/06/98 Digest bat-list.v004.n184 579 bat-list-errors@lists.x

7\. \[1223267\] 08/04/98 Digest bat-list.v004.n180 619 bat-list-errors@lists.x

6\. \[1223232\] 08/04/98 Digest bat-list.v004.n179 622 bat-list-errors@lists.x

5\. \[1222979\] 08/02/98 Digest bat-list.v004.n178 673 bat-list-errors@lists.x

\> 4. \[1222920\] 08/01/98 Digest bat-list.v004.n177 654 bat-list-errors@lists.x

\> 3. \[1222838\] 07/31/98 Digest bat-list.v004.n176 705 bat-list-errors@lists.x

\> 2. \[1222738\] 07/30/98 Digest bat-list.v004.n175 647 bat-list-errors@lists.x

\> 1. \[1222669\] 07/30/98 Digest bat-list.v004.n174 599 bat-list-errors@lists.x

Enter message number or command:

<span id="_Hlt428151127" class="anchor"></span>Figure 3‑39. Using the Zoom Selection toggle action code to zoom back out to the entire list of messages  
(3 of 3)

In this last example of the series (Figure 3‑39), entering "Z" again at the "Enter message number or command:" prompt tells MailMan to zoom back out to the entire list of messages (i.e., 1 through 8). The display looks like it did when the user first selected the messages (Figure 3‑37).

### Paging Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Paging action codes allow you to navigate to different locations within long lists of messages when using either the Detailed or Summary Full Screen message readers. As you can see from the list of action codes (Table 3‑1), you can perform any of the following paging actions on long list of messages:

- Enter—Pressing the \<Enter\> key functions just like the "+" paging action by paging forward one page.
- Equal Sign ("=")—Enter an equal sign (i.e., "=" on the keyboard) at the "Enter message number or command:" prompt in order to redisplay the basket message list page (screen) you are viewing ("refresh" the page/screen).
- Plus Sign ("+")—Enter a plus sign (i.e., "+" on the keyboard) at the "Enter message number or command:" prompt in order to advance to the next page (screen) of messages, when a mail basket contains a large number of messages.
- Plus Number ("+n")—Enter a plus sign and a specific number (i.e., "+n") at the "Enter message number or command:" prompt in order to advance n pages (screens) of messages, when a mail basket contains a large number of messages.
- Minus Sign ("-")—Enter a minus sign (i.e., "-" or hyphen on the keyboard) at the "Enter message number or command:" prompt in order to return to the previous page (screen) of messages, when a mail basket contains a large number of messages and you are *not* on the first page of messages.
- Minus Number ("-n")—Enter a minus sign and a specific number (i.e., "-n") at the "Enter message number or command:" prompt in order to go back n pages (screens) of messages, when a mail basket contains a large number of messages and you are *not* on the first page of messages.
- Zero ("0")—Enter a zero (i.e., "0") at the "Enter message number or command:" prompt in order to return to the first page (screen) of messages, when a mail basket contains a large number of messages and you are *not* on the first page of messages.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/076.png) | NOTE: MailMan only displays these action codes in the list of action codes when the mail basket you are currently processing has more than one page (screen) of messages. |

|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/077.png) | NOTE: These paging action codes (except the \<Enter\> key) are *not* available with MailMan's Classic message reader. |

The paging action items in the Action List will appear as follows:

Press ENTER or + to go to the next page. Enter +n to page forward n pages.

Enter = to refresh this page; ^ to exit this list.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

.

.

.

.

.

.

Press ENTER or + to go to the next page. Enter +n to page forward n pages.

Enter - to go to the previous page. Enter -n to page back n pages.

Enter 0 to go to the first page; = to refresh this page; ^ to exit.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

.

.

.

.

Press ENTER or ^ to exit this list.

Enter - to go to the previous page. Enter -n to page back n pages.

Enter 0 to go to the first page; = to refresh this page.

<span id="_Toc436461045" class="anchor"></span>Figure 3‑40. MailMan paging action codes

When you have reached the end of a list of messages and press the \<Enter\> key or enter the plus sign ("+"), MailMan will ask you if you want to begin again, as shown below:

TEST Basket, 45 messages (1-45)

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

3\. \[1212173\] 05/12/98 Copy of: Test message 55 XMUSER1,ONE E.

2\. \[1212124\] 05/12/98 test 1 XMUSER1,ONE E.

1\. \[1211500\] 05/06/98 Test

Enter message number or command: \<Enter\>

End reached. Begin again? NO// ?

Enter 'Yes' if you wish to continue reading messages; 'No' if you don't.

End reached. Begin again? NO//

<span id="_Toc436461046" class="anchor"></span>Figure 3‑41. Reaching the end of a list of messages

If you enter "Yes" at the "End reached. Begin again? NO//" prompt, MailMan will redisplay the messages in the basket from the beginning (first page/screen). The order of the messages depends on the order you set in the "MESSAGE ORDER?" field when using the User Options Edit option on the Personal Preferences menu.

|                                                                                                                |                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/078.png) | REF: For more information on setting your message display order or the User Options Edit option, please refer to the "Choose Your Message Display Order" topic in Chapter 3 in the *MailMan Getting Started Guide*. |

### Text String Search Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), besides using the Query (Search for) Messages in this Basket ("Q") action code or the Query/Search for Messages option, MailMan V. 8.0 allows you two additional methods of searching for messages based on a text string found in a message subject:

- ?String—Search for messages in the basket whose subject contains the string entered.
- ??String—Search for messages anywhere on the system, which you ever sent or received, and whose subject begins with the string entered.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/079.png) | NOTE: The Text String Search actions are available with all three message readers (i.e., Classic message reader and the Summary or Detailed Full Screen message readers). |

After the search completes, you are automatically placed in a "virtual basket" in a full-screen view to process any messages found from the search. You can take any action on the messages in this "virtual basket" that you can take in a "real" basket (e.g., read, delete, forward, save, etc.).

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/080.png)</td>
<td><p><strong>REF:</strong> For more information on Query (Search for) Messages in this Basket ("Q") action code, please refer to the "Query (Search for) Messages in this Basket ("Q") Action" topic, previously described in this chapter.</p>
<p>For more information on the Query/Search for Messages option, please refer to the Chapter 6, "Searching Mail," in this manual.</p></td>
</tr>
</tbody>
</table>

?String

While in a basket, you can search for messages in the basket whose subject contains a specific string.

At the "Basket Message" prompt, enter the string preceded by a question mark ("?"). You will then be placed in a "virtual basket" in a full-screen view displaying a list of those messages that contain the specified string somewhere in their subject. From that list of messages, you can choose which you would like to read or take any other action.

For example, if you want to search for messages in a basket whose subject contains the word "SCHEDULE", you would enter "?SCHEDULE". This search is *not* case sensitive (uppercase and lowercase are treated identically). Thus, for example, "SCHEDULE" and "Schedule" would both be found with the search.

To search for messages in a basket based on specific subject text, enter a "?" and the search text at the "Basket Message" prompt, as shown below:

Select MailMan Menu Option: rml \<Enter\> Read/Manage Messages

Select message reader: Classic// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (20 messages, 15 new)

Last message number: 20 Messages in basket: 20 (15 new)

Enter ??? for help.

IN Basket Message: 1// ?later

IN Basket Search

\*=New/!=Priority.........Subject….................Lines.From.........Read/Rcvd

2\. \[100111\] 12/22/98 test later 1 XMUSER2,TWO 1/1

\*12. \[100252\] 02/16/99 TEST LATER 2 1 XMUSER2,TWO

\*13. \[100251\] 02/16/99 TEST LATER 1 XMUSER2,TWO 0/1

Search finished.

Enter message number or command:

<span id="_Toc147225791" class="anchor"></span>Figure 3‑42. Example of searching for messages in a basket *containing* a specific text string in the subject

After choosing the Read/Manage Messages option (RML) and using the Classic message reader, the user wanted to search for messages in the "IN" basket whose subject contained the word "later" in the subject. Thus, she entered "?later" (*not* case sensitive) at the "IN Basket Message: 1//" prompt.

When the search was finished, MailMan placed the user into a "virtual basket" in a full-screen view displaying all of the messages in the "IN" basket that contained the "later" string somewhere in the message subject where the user could take any additional actions on the list of messages.

|                                                                                                                |                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/081.png) | REF: For a complete list of action codes you can use, please refer to Table 3‑1 in this chapter. |

  
??String

While in a basket, you can search for messages anywhere on the system whose subject *begins* with a certain string.

At the "Basket Message" prompt, enter the string preceded by two question marks ("??"). You will then be placed in a "virtual basket" in a full-screen view displaying a list of those messages located anywhere on the system, which you ever sent or received, whose subject *begins* with that string. This search is case sensitive (uppercase and lowercase are *not* treated identically). From that list of messages, you can choose which you would like to read.

For example, if you want to search for messages whose subject begins with the words "Schedule Reports", you would enter "??Schedule Reports". Since this search is case sensitive, you must enter the string in the correct case. Thus, for example, "SCHEDULE REPORTS" and "Schedule Reports" are *not* considered by this search as being the same.

To search for messages located anywhere on the system, based on initial subject text, enter "??" and the search text at the "Basket Message" prompt, as shown below:

Select MailMan Menu Option: rml \<Enter\> Read/Manage Messages

Select message reader: Classic// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (20 messages, 15 new)

Last message number: 20 Messages in basket: 20 (15 new)

Enter ??? for help.

IN Basket Message: 1// ??TEST GROUP

All Messages Search

\*=New/!=Priority.....................Subject............Lines.From.....Read/Rcvd

\* 1. TEST \[100276\] 02/28/98 TEST GROUP 1 XMUSER2,TWO

\* 2. TEST \[100277\] 02/28/98 TEST GROUP 2 1 XMUSER2,TWO

\* 3. TEST \[100278\] 02/28/98 TEST GROUP 3 1 XMUSER2,TWO

Search finished.

Enter message number or command:

<span id="_Toc147225792" class="anchor"></span>Figure 3‑43. Example of searching for messages in a basket whose subject *begins* with a specific text string

After choosing the Read/Manage Messages option (RML) and using the Classic message reader, the user wanted to search for messages:

- Located anywhere on the system.
- Whose subject contained the word "later" in the subject.
- Sent or received by the user.

Thus, the user entered "??TEST GROUP" (case sensitive) at the "IN Basket Message: 1//" prompt.

When the search was finished, MailMan placed the user into a "virtual basket" in a full-screen view displaying all of the messages either sent by or received by the user whose subject began with the "TEST GROUP" text string where he could take any additional actions on the list of messages.

|                                                                                                                |                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/082.png) | REF: For a complete list of action codes you can use, please refer to Table 3‑1 in this chapter. |

### Caret ("^") Exit Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes (Table 3‑1), as with all VistA software, you can use the caret ("^") to exit a prompt or option without taking any other action, as shown below:

Select MailMan Menu Option: rml \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (5 messages, 2 new)

IN Basket, 5 messages (1-5), 2 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*5. \[1361007\] 04/19/99 Local: biweekly info exchange 2 XMUSER39,THIRTY9 1/5

!4. \[1360433\] 04/14/99 New Phone System Training 12 XMUSER38,THIRTY8 28/28

3\. \[1354489\] 02/25/99 CIO News - February 25, 1999 85 \<XMUSER36.THIRTY6@FORUM

2\. \[1354488\] 02/24/99 Minutes - Nat'l IRM Call - 496 \<XMUSER37.THIRTY7@FORUM

1\. \[1350198\] 02/01/99 FM22 account 6 XMUSER4,FOUR

Enter message number or command: ^

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option:

<span id="_Toc147225793" class="anchor"></span>Figure 3‑44. Example using the caret to exit a list of messages in a basket

# Reading/Managing Messages—Individual Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics to be discussed in this chapter:

- Action Codes—Individual Messages
- Answer ("A") Action
- Backup ("B") Action
- Print to Browser ("BR") Action
- Copy ("C") Action
- Delete ("D") Action
- Edit ("E") Action
- Forward ("F") Action
- Headerless Print ("H") Action
- Ignore ("I") Action
- Include Message ("IM") Action
- Information Only ("IN") Action (Toggle)
- Priority Replies ("K") Action (Toggle)
- Later ("L") Action
- New/Un New ("N") Action (Toggle)
- Print ("P") Action
- Query ("Q") Action
- Query Recipients ("Q xxx") Action
- Query Current ("QC") Action
- Query Detailed ("QD") Action
- Query Network ("QN") Action
- Query Not Current ("QNC") Action
- Query Terminated ("QT") Action
- Reply ("R") & Reply and Include responses ("RI") Actions
- Save ("S") Action
- Terminate ("T") Action
- Vaporize Date Edit ("V") Action
- Write ("W") Action
- Extract KIDS or PackMan Messages ("X") Action
- Caret ("^") Exit Action

You can use any of the following options to access a message in order to read it, reply to it, or to take any other available action on it:

- New Messages and Responses Option \[XMNEW; synonym NML\]

|                                                                                                                |                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/083.png) | REF: For more information on the New Messages and Responses option \[XMNEW\], please refer to Chapter 2, "Reading/Managing Messages—New Messages and Responses," in this manual. |

- Read/Manage Messages Option \[XMREAD; synonym RML\]

|                                                                                                                |                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/084.png) | REF: For more information on the Read/Manage Messages option \[RML\], please refer to Chapter 3, "Reading/Managing Messages—In a Basket," in this manual. |

- Query/Search for Messages Option \[XMSEARCH\]

|                                                                                                                |                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/085.png) | REF: For more information on the Query/Search for Messages option, please refer to Chapter 6, "Searching Mail," in this manual. |

|                                                                                                                |                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/086.png) | REF: For a complete list and description of command action codes for messages, please refer to the "Action Codes—Individual Messages" topic and Table 4‑1 that follows in this chapter. |

The features and functionality associated with managing your messages individually are described in greater detail in this chapter.

### Action Codes—Individual Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists all of the possible message action codes that you can perform after reading a particular message. All of these action codes are available when using any of the three message readers (i.e., the Detailed Full Screen, Summary Full Screen, or Classic message readers):

| Action Code | Description                                                                                                                                                   |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A           | Answer—The "Answer" command issues a *new* message to send to the sender of the original message.                                                                 |
| B           | Backup—Back up to the original text of the message or to a particular response.                                                                                   |
| BR          | Print to the Browser.                                                                                                                                             |
| C           | Copy—Create a copy of a message.                                                                                                                                  |
| D           | Delete—Delete a message by moving it to your "WASTE" basket.                                                                                                      |
| E           | Edit—Edit a message you sent.                                                                                                                                     |
| F           | Forward—Forward a message to different recipients.                                                                                                                |
| H           | Headerless Print—Print a message without print or header information (i.e., no Subject and From lines).                                                           |
| HG          | Help: Group Information                                                                                                                                           |
| HU          | Help: User Information                                                                                                                                            |
| I           | Ignore—Ignore the message and leave it in the current mail basket.                                                                                                |
| IM          | Include Message—Include any combination of responses from another message in the new message being created.                                                       |
| IN          | Information Only—Toggle whether a message, sent by you, is Information Only, depending on current setting. Recipients *cannot* respond to these messages.         |
| K           | Priority Replies Toggle—Toggle whether or not all future replies to this priority message are received as priority or ordinary, depending on the current setting. |
| L           | Later—Have the message made "new" in your mailbox at a specified later date and time.                                                                             |
| N           | New/Un New Toggle—Toggle a message to be new or *not* new, depending on the current setting.                                                                      |
| P           | Print—Print a message to a specified device.                                                                                                                      |
| Q           | Query—Obtain general recipient information on a message.                                                                                                          |
| Q xxx       | Query Recipient(s) xxx—Obtain information on a specified recipient of a message, where "xxx" represents the name of the recipient.                                |
| QC          | Query Current—Obtain information on local recipients who are current (i.e., read all of the responses) on a message.                                              |
| QD          | Query Detailed—Obtain detailed recipient information on a message.                                                                                                |
| QN          | Query Network—Obtain network and detailed recipient information on a message.                                                                                     |
| QNC         | Query Not Current—Obtain information on local recipients who are *not* current (i.e., have *not* read all of the responses) on a message.                         |
| QT          | Query Terminated—Obtain information on local recipients who have terminated from a message.                                                                       |
| R           | Reply—Compose and send a reply to a message.                                                                                                                      |
| RI          | Reply and Include responses—Compose and send a reply to a message with previous responses included in your reply.                                                 |
| S           | Save—Save a message to an existing mail basket or to a new basket that you create on the fly.                                                                     |
| T           | Terminate—Terminate a message by putting it in your "WASTE" basket and stop receiving any future replies to that message.                                         |
| V           | Vaporize Date Edit—Set a specified date and time to vaporize (delete) a message from your mail basket.                                                            |
| W           | Write—Send a *new* message while reading another message.                                                                                                         |
| X           | Extract KIDS or PackMan Messages—Provides a list of specific actions you can perform on these types of messages (for IRM personnel or developers).                |
| ^           | Exit the Message (caret, "^")—Acts like the Ignore action code.                                                                                               |

<span id="_Ref106607195" class="anchor"></span>Table 4‑1. Action Codes—Messages

|                                                                                                                |                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/087.png) | NOTE: Please remember that not all action codes are available with every message. Some action codes are only available when certain conditions exist. |

|                                                                                                                |                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/088.png) | NOTE: Each action code is described in greater detail in the topics that follow. |

### Answer ("A") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Answer action code (i.e., "A") to answer a message. While "Replying" to a message chains the new response to the original message, the "Answer" command issues a new message to send to the sender of the original message, a new message that will *not* be chained to the original message.

The new "Answer" message consists of three components in the following order:

> 1\. A copy of the message being answered

> 2\. The text of your answer

> 3\. The three lines of your Network Signature

When you answer a message the original message is copied *before* you are placed in the editor. Thus, "Answer" first copies the original message, adds your network signature, and then puts you into the editor. Once you're finished with your answer, it is sent as a separate message to the sender of the original message and any additional recipients you select.

In order to use the Answer command, you must have a Network Signature. If you do not have a Network Signature and try to "Answer" a message, MailMan will inform you of the requirement, as shown below:

Subj: BLUE \[#1222162\] 07/27/98@09:59 1 line

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

In 'IN' basket. Page 1

-------------------------------------------------------------

Test message.

Enter message action (in IN basket): IGNORE// A

You must have a Network Signature to Answer a message.

Would you like to create a Network Signature now? Yes// \<Enter\> YES

NETWORK SIGNATURE LINE 1 OF 3: One Xmuser1

NETWORK SIGNATURE LINE 2 OF 3: Technical Writer

NETWORK SIGNATURE LINE 3 OF 3: OI Field Office Oakland

.

.

.

.

<span id="_Ref427464656" class="anchor"></span>Figure 4‑1. Answering a message without a network signature

As you can see from this example (Figure 4‑1), MailMan would not let the user "Answer" this message because the user did *not* have a Network Signature. MailMan, however, immediately gave the user the opportunity to enter the Network Signature so that he could continue with the answer.

|                                                                                                                |                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/089.png) | NOTE: You can also use the User Options Edit option on the Personal Preferences menu to enter your Network Signature. |

|                                                                                                                |                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/090.png) | REF: For more information on entering Network Signatures, please refer to the "Network Signature" topic in Chapter 4 in the *MailMan Getting Started Guide*. |

You can "Answer" a message by entering an "A" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Test \[#1219990\] 07/09/98@13:46 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'TEST' basket. Page 1

-------------------------------------------------------------

here is a test

Enter message action (in TEST basket): IGNORE// A

Subject: Re: Test// \<Enter\>

Copying original message and network signature...

You may edit the text of the message...

==\[ WRAP \]==\[ INSERT \]==============\< Re: Test \>=============\[ \<PF1\>H=Help \]====

\>Original message: "TEST"

\>From: XMUSER1,ONE E.

\>Sent: 07/09/98@13:46

\>

\>here is a test

Here is some additional text added after the original message text.

---------------------------------------------------------------------------------

One Xmuser1

Technical Writer

OI Field Office Oakland

\<======T=======T=======T=======T=======T=======T=======T=======T=======T========\>

Addressing answer to sender: XMUSER1,ONE E.

...OK? Yes// \<Enter\> (Yes)

Select basket to send to: IN// \<Enter\>

And Send to: xmuser2 \<Enter\> ,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 07/30/98@14:54

On vacation 31 July through 16 August.

And Send to: \<Enter\>

Select Message option: Transmit now// \<Enter\> Sending \[1224304\]...

Sent

Finished with the 'Answer' command.

Now back to:

Subj: Test \[#1219990\] 07/09/98@13:46 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): Ignore//

<span id="_Ref427465486" class="anchor"></span>Figure 4‑2. Answering a message

As you can see from the previous example (Figure 4‑2), while reading a message, the user entered an "A" (Answer) at the "Enter message action (in TEST basket): IGNORE//" prompt to "Answer" the message. MailMan first asked the user if he wanted to change the subject text, in this case, he did not. Thus, he pressed the \<Enter\> key to accept the default response (i.e., "Re: Test").

Next, MailMan copied the message header information (i.e., subject, sender, and date sent), the original text of the message, and the Network Signature (displayed after a dashed line) before placing the user into the editor.

Once in the editor, the user added the answer by typing in the response following the original copy of the message. If the user wanted to, he could have deleted or moved any of the lines MailMan copied into the message, however, for clarity, he kept the copy of the original text right before the response. When he was through with the answer, he saved the text and closed the editor.

MailMan then prompted the user to address the message to whomever he wished. After completing the addressing of the message, he sent it off.

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/091.png) | REF: For more information on addressing a message, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

After sending the message, MailMan notified the user the "Answer" was completed (i.e., "Finished with the 'Answer' command."), redisplayed the original message header, and returned the user to the original message action prompt where the user could take any additional actions on this message.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/092.png) | TIP: Use the "Answer" command when you want to privately respond to a message and do not want your response chained to the message so others can see it (e.g., avoid all of those "Me Too's"). For example, if a message causes numerous recipients to respond by requesting the same information over and over (e.g., "Please send a copy of that document to me too."), you should use the "Answer" command rather than the "reply" command and avoid having to read all of those extraneous replies. |

### Backup ("B") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After a message has been read, replied to, and the reply has been read, MailMan will no longer display the message text automatically when you attempt to read the message. This is to avoid forcing you to read through text you've already seen; though, the text is still there. You can use the Backup action code ("B") to back up to any part of a message and read the message from that point on:

- Original message
- Any specific response (if any)

To back up to the original message or any specific response, enter a "B" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Priority test \#2 \[#1214469\] 06/02/98@07:44 1 line

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

7 of 7 responses read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// B

There are 7 responses. Response 0 is the original message. (?? shows index)

Backup to: Original message 0// 6

Subj: Priority test \#2 \[#1214469\] 06/02/98@07:44 1 line

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

7 of 7 responses read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

6\) XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

06/04/98@10:25 4 lines

Yes, that's right.

I think I've fixed it now, though.

Would you send me priority messages, and let me know?

7\) XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

06/04/98@15:57 1 line

will do.

Enter message action (in TEST basket): IGNORE//

<span id="_Ref431020637" class="anchor"></span>Figure 4‑3. Backing up in a message

In this example (Figure 4‑3), after reading a message, the user wanted to go back and reread a specific response. Thus, she entered a "B" (Backup) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan informed the user that there were seven responses to the original message As a default, MailMan asked the user if she wanted to back up to the original message.

|                                                                                                                |                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/093.png) | NOTE: If a message does not have any responses, MailMan will not ask this question. |

For this example, the user decided to back up to response number 6 of the message by entering "6" at the "Backup to: Original message 0//" prompt. Thus, MailMan displayed the message starting with Response 6.

After completing the backup, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

If the user had entered two question marks ("??") at the "Backup to: Original message 0//" prompt, MailMan would have displayed an index or list of respondents, as shown below:

Backup to: Original message 0// ??

There are 7 responses. Response 0 is the original message.

Response....From..........................................................Lines

7\) 06/04/98 XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland) 1

6\) 06/04/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 4

5\) 06/04/98 XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland) 1

4\) 06/03/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 2

3\) 06/03/98 XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland) 2

2\) 06/02/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 2

1\) 06/02/98 XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland) 1

0\) 06/02/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 1

There are 7 responses. Response 0 is the original message. (?? shows index)

Backup to: Original message 0//

<span id="_Toc436461051" class="anchor"></span>Figure 4‑4. Displaying an index for a message

The index shows that there were seven responses to the original message.

If you have already read all the responses of a message and you go back to the message later, only the message header is displayed and MailMan informs you that: "You are at the end of this message. Enter 'B' to Backup and review it."

### Print to Browser ("BR") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After reading a message, you can use the BR action code to print the message to the VA FileMan Browser. If your site manager has set up the output device called BROWSER, you can view any message in the BROWSER.

The advantages of printing a message to the Browser are that you can:

- Scroll both forward and backward through the message smoothly and easily—you will not lose part of it off the top of the screen as you do when you print to the HOME device.
- Go to any line, screen, or column of the message with a single command.
- Use the search feature to find and immediately jump to any text in the message.
- Copy text from the message and later paste it into another message or other document or WORD-PROCESSING-type field.

Using the BROWSER has the same effect as printing your message to the HOME device or to a printer except that you now have the benefit of being able to scroll up and down through an entire message on your screen. You can view (but not edit) any message. You may find that by viewing messages in the BROWSER, you can avoid having to print hard copies of some messages simply to be able to see the whole message.

In the example below (Figure 4‑5), you open a message and you are at response 229 (this is a very long message). You want to see a previous response. You could use the Backup command if you knew the number of the response you wanted or you could Print to the HOME device and read through all the responses, if you have time. The easiest thing to do and the option that gives you the most flexibility, however, is to use BR action code and print to the Browser.

Subj: I'm so excited... \[#1190657\] 11/07/97@09:24 59 lines

From: XMUSER2,TWO M - COMPUTER SPECIALIST (Oakland OI Field Office) 230 of 230 responses read.

In 'mailman' basket. Message will be NEW Later. Page 1

-------------------------------------------------------------------------------

229\) XMUSER17,SEVENTEEN - COMPUTER SPECIALIST (Oakland OI Field Office) 08/01/00@09:19 5 lines

I was hoping to do more than SELECT an option...... I will defer to you

folks. It is, at worse, a nuisance and, at best, unlikely to be

encountered much. And the work around is to navigate the old fashioned

way so I would hate to see anyone waste a lot of time on it. But I feel

compelled to report unexpected behavior.

230\) XMUSER2,TWO M - COMPUTER SPECIALIST (Oakland OI Field Office) 08/01/00@09:36 1 line

Then let's ignore it.

Enter message action (in MailMan basket): Ignore// BR

There are 230 responses. Response 0 is the original message. (?? shows index)

Select the responses to Print: 0-230// \<Enter\>

...one moment...

<span id="_Ref146958018" class="anchor"></span>Figure 4‑5. Enter BR to print this message to the Browser

Enter "BR" at the "Enter message action (in xxxx basket): Ignore//" prompt, where "xxxx" contains the name of the mail basket in which the message resides, as shown above.

When you press \<Enter\> to accept the default of 0-230 responses to print to the Browser, immediately your screen will change to display the beginning of the message as shown below:

\[#1190657\] I'm so excited...

MailMan message for XMUSER4,FOUR Tech Writer

Printed at REDACTED.VA.GOV 08/15/00@10:57

Subj: I'm so excited... \[#1190657\] 11/07/97@09:24 59 lines

From: XMUSER2,TWO M - COMPUTER SPECIALIST (Oakland OI Field Office) 230 of 230 responses read. In

-------------------------------------------------------------------------------

...and I just can't hide it!

What am I doing here on my day off? I can't wait! I've just got to tell you!

You've heard the rumors for months! You've read about it on FORUM for the past

week! On Wednesday, if I don't hose up the install, you'll enter a whole new

e-mail dimension!

I'm talking about MailMan Version 8.0! It'll change your life! Make you a

better person!

o It's got a whole new user interface!

o You can have your mail in date or reverse-date order, just set your

preference in the user options.

o You can set your default message lister (in edit user options) to the classic

(tired) one or the fabulous new full-screen message lister! Within it you can

. Col\> 1 \|\<PF1\>H=Help \<PF1\>E=Exit\| Line\> 22 of 10524 Screen\> 1 of 479

1(023,001)

<span id="_Toc147225800" class="anchor"></span>Figure 4‑6. Message as seen in the Browser.

You can see that the top or header line of the Browser screen shows the name of the current document. The bottom line of the screen shows you, from left to right: the leftmost column, keystroke reminders for accessing help and exiting, the current line and the total number of lines, the current screen, and the total number of screens.

Now that you are in the Browser, you have all of its capabilities at your fingertips. For a quick and thorough summary of the commands available to you, press \<PF1\>H for help while in the Browser.

|                                                                                                                |                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/094.png) | REF: For additional information about using features of the VA FileMan Browser, see Chapter 4 in the *VA FileMan Getting Started Guide*. |

### Copy ("C") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Copy action code (i.e., "C") to copy a message and optionally include a list of recipients. When you copy a message, you can copy the original message and/or *any* combination of responses.

To copy the original message and any responses, enter a "C" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Priority test \#1 \[#1214467\] 06/02/98@07:44 1

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

5 of 5 responses read. In 'TEST' basket. Page 1

------------------------------------------------------

Enter message action (in TEST basket): IGNORE// C

There are 5 responses. Response 0 is the original message. (?? shows index)

Select the responses to copy: 0// 0,1,3-4

List original recipients in text? NO// y \<Enter\> YES

Deliver to the same recipients? NO// \<Enter\>

Subject: Copy of: Priority test \#1 Replace Priority \<Enter\> With Copy \<Enter\>

Replace \<Enter\>

Copy of: Copy test \#1

Copying text...

Copying recipients into text...

You may edit the text of the message...

==\[ WRAP \]==\[ INSERT \]========\< Copy of: Copy test \#1 \>======\[ \<PF1\>H=Help \]====

Here is a copy of a previous message, I'm adding this text prior to the

copied portion.

Original message: "Priority test \#1" \[#1214467\]

From: XMUSER2,TWO M.@REDACTED.VA.GOV

Sent: 06/02/98@07:44

I am not sending this message to myself.

Response \#1: XMUSER1,ONE E. 06/02/98@11:35

Here is my reply.

Response \#3: XMUSER2,TWO M. 06/02/98@12:39

Please reply again.

Response \#4: XMUSER1,ONE E. 06/03/98@07:54

nag, nag, nag... here you go!

Original Recipients

-------------------

XMUSER2,TWO

XMUSER1,ONE

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

<span id="_Ref428084827" class="anchor"></span>Figure 4‑7. Copying a message (1 of 2)

Send mail to: XMUSER1,ONE E.// \<Enter\>

Select basket to send to: IN// \<Enter\>

And Send to: \<Enter\>

Select Message option: Transmit now// \<Enter\> Sending \[1225355\]

Sent

Finished with the 'Copy' command.

Now back to:

Subj: Priority test \#1 \[#1214467\] 06/02/98@07:44 1 line

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

5 of 5 responses read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in IN basket): Ignore//

<span id="_Toc147225802" class="anchor"></span>Figure 4‑8. Copying a message (2 of 2)

In this example (Figure 4‑2), the user wanted to copy a message he just read. Thus, he entered a "C" (Copy) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan asked the user to choose what portion of the message he wanted to copy (e.g., original message and/or any combination of responses). In this case, the user chose to copy the original message, response 1 of the message, and responses 3 to 4 of the message by entering "0,1,3-4" at the "Select the responses to copy: 0//" prompt.

|                                                                                                                |                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/095.png) | NOTE: If the message you are copying does not have any responses, MailMan will automatically copy the original message and not prompt you to choose any responses. |

If the user was unsure of the responses to include, MailMan lets you enter two question marks ("??") at the "Select the responses to copy: 0//" prompt in order to display an index of respondents to the message, for example:

Select the responses to copy: 0// ??

There are 5 responses.

Response....From...........................................................Lines

5\) 06/03/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 1

4\) 06/03/98 XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland) 1

3\) 06/02/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 1

2\) 06/02/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 1

1\) 06/02/98 XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland) 1

0\) 06/02/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 1

<span id="_Ref480604337" class="anchor"></span>Figure 4‑9. Copy action code index list of respondents

The previous index (Figure 4‑9) shows that there were five responses to the original message.

After the user chose the portion of the message he wanted to copy (Figure 4‑7), MailMan asked the user if he wanted to have a list of recipients included after the copied text. For this example, the user chose to list the original recipients by answering "Yes" at the "List original recipients in text? NO//" prompt.

Next, MailMan asked the user if he wanted to deliver this copy of the message to the same recipients from the original message. In this case, he did not, so he answered "No" at the "Deliver to the same recipients? NO//" prompt.

MailMan then asked the user if he wanted to modify the subject. In this case, he decided to change the Subject from "Copy of: Priority test \#1" to "Copy of: Copy test \#1." To do this, he entered the word "Priority" at the "Replace" prompt and entered the word "Copy" at the "With" prompt.

At this point, the user was finished with the changes and pressed the \<Enter\> key after the next "Replace" prompt without entering any text.

MailMan then displayed the modified subject to the user.

After copying the original text, the specified responses, and the list of recipients, MailMan automatically placed the user into the editor to add any additional text to the copied text.

After entering the text, the user saved it and closed the editor.

Finally, MailMan asked the user to address the modified copy of the message. In this case, the user just sent the copy to himself (i.e., XMUSER1,ONE E., default response) by pressing the \<Enter\> key at the "Send mail to: XMUSER1,ONE E.//" prompt.

The user also accepted the default basket (i.e., "IN") by pressing the \<Enter\> key at the "Select basket to send to: IN//" prompt.

MailMan knew the user was finished addressing the message when he pressed the \<Enter\> key at the "And Send to:" prompt without entering another recipient's name.

MailMan sent the message after he answered "Yes" at the "Select Message option: Transmit now//" prompt.

After sending the message copy, MailMan notified the user the "Copy" was completed (i.e., "Finished with the 'Copy' command."), redisplayed the original message header, and returned the user to the original message action prompt where he could take any additional actions on this message.

### Delete ("D") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Delete action code (i.e., "D") to delete a message from your mailbox. MailMan moves the deleted message to your "WASTE" mail basket for eventual removal from your mailbox. This allows you to better maintain your mail baskets by removing unnecessary or old messages ("clutter") from your mailbox.

Generally, a batch job is run nightly (determined by IRM at your site) to remove messages from your "WASTE" basket, and thus, from your mailbox. You can immediately remove a message from your mailbox by, again, deleting the message from your "WASTE" basket; however, the message remains in the system until all recipients of the message have deleted it from their mailbox.

Unlike the Terminate action code, the Delete action code will *not* prevent responses to a "deleted" message from "resurrecting" or restoring a message back into your mailbox.

|                                                                                                                |                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/096.png) | REF: For more information on the Terminate action code, please refer to the "Terminate Messages ("T") Action" topic that follows in this chapter. |

To delete a message, enter a "D" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: test3 \[#1223225\] 08/04/98@08:19 1 line

From: XMUSER4,FOUR - Q... Continuum In 'Test Save' basket. Page 1

-------------------------------------------------------------------------------

test3

Enter message action (in Test Save basket): IGNORE// D

Message deleted.

<span id="_Ref428088063" class="anchor"></span>Figure 4‑10. Deleting a message

After reading a message (Figure 4‑10), the user decided to delete it by entering a "D" (Delete) at the "Enter message action (in Test Save basket): IGNORE//" prompt.

MailMan automatically moved the message from the "Test Save" basket to the "WASTE" basket and confirmed the deletion. It will be purged from the user's mailbox when the nightly batch job is run.

If the user wanted to "un-delete" the message, she could go to the "WASTE" basket and save the message to another basket in the user's mailbox.

|                                                                                                                |                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/097.png) | NOTE: MailMan does not ask you to confirm the delete request. |

### Edit ("E") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Edit action code (i.e., "E") to edit any message created by you and not yet sent to other recipients.

You *cannot* edit a message, if you are *not* the sender of the message, as shown below:

Subj: test \[#1223222\] 08/04/98@08:14 1 line

From: XMUSER4,FOUR - Q... Continuum In 'Test Save' basket. Page 1

-------------------------------------------------------------------------------

test

Enter message action (in Test Save basket): IGNORE// E

You can't edit this message, because you didn't send it.

Enter message action (in Test Save basket): IGNORE//

<span id="_Ref427646704" class="anchor"></span>Figure 4‑11. Trying to edit a message not sent by you

In the previous example (Figure 4‑11), MailMan prevented the user from editing a message she did not send.

You also *cannot* edit a message, if you already *sent* the message to a recipient other than yourself, as shown below:

Subj: Priority Test from One \#1 \[#1214918\] 06/04/98@10:00

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (San Francis

3 of 3 responses read. In 'TEST' basket. Page 1

-------------------------------------------------------

Enter message action (in TEST basket): IGNORE// E

You can't edit this message, because you have already sent it to someone else.

You may toggle the 'information only' switch, if you wish.

Enter message action (in TEST basket): IGNORE//

<span id="_Ref427646961" class="anchor"></span>Figure 4‑12. Trying to edit a message already sent to recipients

In this example (Figure 4‑12), since the user obviously already sent this message to other recipients, MailMan will not allow the user to further edit the message.

MailMan informed the user, however, that she could prevent recipients from replying to the message by designating it as "Information Only," if the user did not originally send it out as "Information Only." Conversely, the user could allow recipients to reply to the message by not designating it as "Information Only," if the user originally sent it out as "Information Only."

|                                                                                                                |                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/098.png) | REF: For more information on the Information Only Toggle, please refer to the "Information Only ("IN") Action (Toggle)" topic that follows in this chapter. |

To edit a message, if you are the only recipient, enter an "E" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Test New Mail \[#1223214\] 08/04/98@07:56 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Testing new mail.

Enter message action (in TEST basket): IGNORE// E

Select Edit option: ?

Enter a code from the list.

Select one of the following:

C Confidential (surrogate can't read)

D Delivery basket set

ES Edit Subject

ET Edit Text

I Information only (recipients may not reply)

NS Add Network Signature

P Priority delivery

R Confirm Receipt

S Scramble text with password

V Vaporize date set

X Close (no forward allowed)

Select Edit option:

<span id="_Ref427647846" class="anchor"></span>Figure 4‑13. Editing a message

To get a list of possible edit actions, after reading a message, the user entered a question mark ("?") at the "Select Edit option:" prompt (Figure 4‑13). MailMan displayed the list and asked the user to choose an edit option.

The user can choose any or all of these edit options indicated when sending a message.

|                                                                                                                |                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/099.png) | REF: For specific information on each of these edit options, please refer to the "Action Codes—Sending Messages" topic and Table 5‑1 in Chapter 5, "Sending Mail," in this manual. |

### Forward ("F") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Forward action code (i.e., "F") to forward a message to different recipients.

To forward a message to another MailMan user, enter an "F" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Test Edit Capabilities \[#1223214\] 08/04/98@07:56 3 lines

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'TEST' basket.

Automatic Deletion Date: Sep 10, 1998 Page 1

-------------------------------------------------------------------------------

Testing new mail.

I've decided to enter more text to my message.

Enter message action (in TEST basket): IGNORE// F

Forward mail to: ?

Enter the name(s) of the recipient(s) of this message

in any of the following formats:

Lastname,first for a user at this site

Lastname,first@REMOTE-SITE for a user at another site

(note: DUZ may be used instead of Lastname,first)

G.\<group-name\> for a group of users

D.\<device-name\> for a device

\* for a limited broadcast or broadcast to all users

(must be Postmaster or XMSTAR key holder)

Prefix any user address with 'I:' to send Information only.

'C:' to send Carbon copy.

'L:' to send Later.

'-' to delete it.

Enter:

G.? for a list of groups

D.? for a list of devices

Enter '??' for detailed help.

Forward mail to: xmuser2 \<Enter\> ,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 07/30/98@14:54

On vacation 31 July through 16 August.

And Forward to: \<Enter\>

Message forwarded.

Enter message action (in TEST basket): IGNORE//

<span id="_Ref428088121" class="anchor"></span>Figure 4‑14. Forwarding a message

For this example (Figure 4‑14), the user wanted to forward this message to another MailMan user. Thus, he entered an "F" (Forward) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan then prompted the user to enter an addressee. As you can see from this example, he first chose to enter a question mark ("?") at the "Forward mail to:" prompt in order to display the options when entering an addressee. For this example, he decided to forward the message to Two Xmuser2 by entering the first portion of his last name (i.e., "XMUSER2") at the "Forward mail to:" prompt.

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/100.png) | REF: For more information on addressing a message, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

MailMan knew the user was finished forwarding the message when he pressed the \<Enter\> key at the "And Forward to:" prompt without entering another addressee.

MailMan then confirmed that the message had been forwarded.

After forwarding the message, MailMan returned the user to the message action prompt where he could take any additional actions on this message.

If you do a Query Detailed (i.e., "QD") on the message, MailMan will show that you forwarded the message to Two Xmuser2. If someone else later forwards the message to Two Xmuser2 again, MailMan will no longer show you as having forwarded the message, but will now show the name of the last user to forward the message. Only the information of the latest forward is kept, there is no forward history.

|                                                                                                                |                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/101.png) | REF: For more information on Query Detailed (i.e., "QD") action code, please refer to the "Query Detailed ("QD") Action" topic in this chapter. |

If a message is priority, you may or may not be able to forward the message to mail groups. You can forward a priority message to a mail group if your site is set up to do so. It is possible for IRM at your site to set the site parameters in the MAILMAN SITE PARAMETERS file (#4.3) to allow this action.

|                                                                                                                |                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/102.png) | REF: For more information on forwarding priority messages to a mail group, please refer to the "Managing MailMan, Management Features in Mailman" topic in the *MailMan Technical Manual*. |

### Headerless Print ("H") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (), you can use the Headerless Print action code (i.e., "H") to print a message without any header information. The default response will always be to print the original message and all responses; however, you can choose to print any combination of responses (single or ranges), with or without the original message. Also, for example, if you print responses "10-", MailMan understands that you mean print from response 10 through the last response.

To print a message without a header, enter an "H" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Test \[#1219990\] 07/09/98@13:46 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

1 of 1 response read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// H

Print recipient list? No// ?

Answer 'Yes' if you want the recipients printed at the end.

Print recipient list? No// y \<Enter\> YES

Select one of the following:

D Detail

S Summary

Print Detail or Summary recipient chain: Summary// \<Enter\>

There is 1 response. Response 0 is the original message. (?? shows index)

Select the responses to Print: 0-1// 0-1

DEVICE: HOME// \<Enter\> Telnet terminal

here is a test

1\) XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

08/11/98@11:41 2 lines

here is my response.

Local Message-ID: 1219990@REDACTED.VA.GOV (1 Recipient)

This message was addressed as follows:

XMUSER1,ONE E.

Enter message action (in TEST basket): IGNORE//

<span id="_Ref428088668" class="anchor"></span>Figure 4‑15. Headerless print of a message—Summary information

For this example (Figure 4‑15), the user wanted to print a message without a header or any print information. Thus, she entered an "H" (Headerless Print) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan then prompted the user to choose if she wanted to print the list of recipients as well as the text of the message. The user first entered a question mark ("?") at the "Print recipient list? No//" prompt in order to display the options. For this example, the user decided to include a list of recipients by entering "Yes" at the "Print recipient list? No//" prompt.

The user was then given the choice of printing either a "Detail" or "Summary" list of recipients:

- Summary list (default)—The Summary list provides the same information you see when you do a query on a message (i.e., Query action code).

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/103.png) | REF: For more information on the Query action code, please refer to the "Query ("Q") Action" topic that follows in this chapter. |

- Detail list—The Detail list provides the same information you see when you do a detailed query on a message (i.e., Query Detailed action code).

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/104.png) | REF: For more information on the Query action code, please refer to the "Query ("Q") Action" topic that follows in this chapter. |

For this example, the user chose to only print a Summary list by pressing the \<Enter\> key to accept the default response (i.e., Summary) at the "Print Detail or Summary recipient chain: Summary//" prompt.

MailMan then asked the user to choose what portion of the message she wanted to print (e.g., original message, original message plus any combination of responses. In this case, the user chose to print the original message and its only response by entering "0-1" at the "Select the responses to Print: 0-1//" prompt. The user also could have pressed the \<Enter\> key to accept the default of "0-1."

|                                                                                                                |                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/105.png) | NOTE: If the message you are printing does not have any responses, MailMan will not ask this question. |

MailMan then asked the user to choose where to print the message (i.e., what device). In this case, the user chose to print the message to the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt. MailMan immediately begins printing the message.

|                                                                                                                |                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/106.png) | NOTE: If you want to print your message(s) to a different device (e.g., a printer), enter the appropriate device name at the "DEVICE: HOME//" prompt. |

MailMan printed the message text and the response she requested without any print or header information. Also, in this example, the user chose to print a Summary list of recipient information. Thus, MailMan printed that information after the last response text of the message.

After printing the message, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

The following example demonstrates printing a message without a header and including *detailed* recipient information:

Subj: Test \[#1219990\] 07/09/98@13:46 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

1 of 1 response read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// H

Print recipient list? No// y \<Enter\> YES

Select one of the following:

D Detail

S Summary

Print Detail or Summary recipient chain: Summary// D \<Enter\> Detail

There is 1 response. Response 0 is the original message. (?? shows index)

Select the responses to Print: 0-1// 0-1

DEVICE: HOME// \<Enter\> Telnet terminal

here is a test

1\) XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

08/11/98@11:41 2 lines

here is my response.

Local Message-ID: 1219990@REDACTED.VA.GOV (1 Recipient)

XMUSER1,ONE E. Last read: 08/11/98@13:56 (1 of 1 response)

\[First read: 07/09/98@13:46\]

Enter message action (in TEST basket): IGNORE//

<span id="_Ref428091201" class="anchor"></span>Figure 4‑16. Headerless print of a message—Detailed information

In this example (Figure 4‑16), the user, again, chose to print a message without any print or header information. This time, however, she wanted to print a detailed list of recipient information. Thus, all entries are the same as in Figure 4‑15 except that the user entered a "D" (Detail) at the "Print Detail or Summary recipient chain: Summary//" prompt.

As you can see from this example, the recipient information printed more detail about the recipient when compared to the summary information in the previous example (Figure 4‑15).

After printing the message, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

### Help: Group Information ("HG") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Help:Group Information action to get information about a mail group. If you have read a message and want information about the mail group(s) to which the message has been sent, you can enter "HG" at the Action prompt to find that information.

Enter message action (in mailman basket): Ignore// HG \<Enter\> Help:Group Information

Select MAIL GROUP NAME: ISC STAFF

NAME: ISC STAFF TYPE: public

ALLOW SELF ENROLLMENT?: NO REFERENCE COUNT: 3296

LAST REFERENCED: AUG 11, 2000

DESCRIPTION: Members of the Oakland OIFO Staff

Includes all at 1301 Clay St., all Satellites and remote supervisors if they've

asked to be included.

Authorized Sender: XMUSER100,ONE-HUNDRED

Authorized Sender: XMUSER8,EIGHT

Authorized Sender: XMUSER14,FOURTEEN K

Authorized Sender: XMUSER6,SIX

Authorized Sender: XMUSER11,ELEVEN

<span id="_Toc147225811" class="anchor"></span>Figure 4‑17. Enter HG for Help:Group information

Help:Group (HG) gives you the following information about the mail group:

- Mail Group Name
- Type of Mail Group—Public or private
- Authorized Senders Indicator
- Allow Self Enrollment Indicator—Yes or No
- Reference Count—How many times the mail group has been sent a message
- Last Referenced Date—The last date and time the group was referenced
- Coordinator—The person responsible for maintaining the membership of the mail group),
- Description of the Mail Group
- Organizer—The person who set up the mail group
- Authorized Senders—The only users who are allowed to send mail to the group
- Members of the Group
- Member of Groups—A list of mail groups to which the mail group belongs

If you want information about the group but you do not know the group(s) to which the message has been sent, you can use the Query action to find out, as shown below:

Enter message action (in mailman basket): Ignore// Q \<Enter\> Query

Subj: I'm so excited... \[#1190657\] 11/07/97@09:24 59 lines

From: XMUSER2,TWO M - COMPUTER SPECIALIST (Oakland OI Field Office) 930 of 930 responses read.

In 'mailman' basket. Message will be NEW Later.

Local Message-ID: 1190657@REDACTED.VA.GOV (60 recipients)

Message will be NEW on: Jan 01, 2006

This message was addressed as follows:

G.ISC STAFF

XMUSER23,TWENTY3

test@HOTMAIL.COM

Enter message action (in mailman basket): Ignore//

<span id="_Toc147225812" class="anchor"></span>Figure 4‑18. Enter Q for Query

You can also get mail group information through the MailMan menu.

|                                                                                                                |                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/107.png) | REF: For more information about this option and the information it returns, please refer to the "Mail Group Information" topic in Chapter 12, "Online Help/Information." |

If you have been reading a mail message and want to get information about the mail group(s) to which the message was sent, the shortcut way to find that information is to use the HG Help:Group Information (or the HU Help:User Information) option at the message action prompt. This saves you the steps of getting out of the message and going back to the MailMan menu to get the same information.

### Help:User Information ("HU") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Help:User Information action to get information about a user who is a recipient of a message. If you have read a message and want information about the user(s) to whom the message has been sent, you can enter "HU" at the Action prompt to find that information.

Enter message action (in mailman basket): Ignore// HU \<Enter\> Help:User Information

User name: XMUSER23 \<Enter\> XMUSER23,TWENTY3 INFORMATION RESOURCES MGMT.

Last used MailMan: 08/15/00@10:05

XMUSER23,TWENTY3 - COMPUTER SPECIALIST (Oakland OI Field Office)

Last used MailMan: 08/15/00@10:05

Office phone: 304-626-7739

Introduction:

The answer is: 42

Private e-mail address: anonymous@xxxxxx.net

Mail Groups:

ISC STAFF (Public)

FILEMAN DEVELOPER (Public)

CLARKSBURG (Public)

TK73VER (Public)

FMTEAM (Public)

ISC SATELLITE (Public)

IMF (Public)

INFRASTRUCTURE (Public)

infra (Private)

MESSAGING TEAM (Public)

<span id="_Toc147225813" class="anchor"></span>Figure 4‑19. Enter HU for Help User information

Help:User (HU) gives you the following information about the user:

- MailMan user's name
- Banner—The user's current MailMan banner, if any has been entered using the User Options Edit option on the Personal Preferences menu
- Last date and time the user used MailMan and the status of messages in their mailbox
- Introduction—The user's introduction, if any has been entered using the User Options Edit option on the Personal Preferences menu
- User's office information, if any has been entered using the User Options Edit option on the Personal Preferences menu
- List of mail groups to which the user belongs
- List of the MailMan users for whom this user may act as surrogate, if any

If you want information about the user but you do not know the user(s) to whom the message has been sent, you can use the Query action to find out, as shown below:

Enter message action (in mailman basket): Ignore// Q \<Enter\> Query

Subj: I'm so excited... \[#1190657\] 11/07/97@09:24 59 lines

From: XMUSER2,TWO M - COMPUTER SPECIALIST (Oakland OI Field Office) 930 of 930 responses read.

In 'mailman' basket. Message will be NEW Later.

Local Message-ID: 1190657@REDACTED.VA.GOV (60 recipients)

Message will be NEW on: Jan 01, 2006

This message was addressed as follows:

G.ISC STAFF

XMUSER23,TWENTY3

test@HOTMAIL.COM

Enter message action (in mailman basket): Ignore//

<span id="_Toc147225814" class="anchor"></span>Figure 4‑20. Enter Q for Query

You can also get user information through the MailMan menu.

|                                                                                                                |                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/108.png) | REF: For more information about this option and the information it returns, please refer to the "User Information" topic in Chapter 12, "Online Help/Information." |

If you have been reading a mail message and want to get information about a user to whom the message was sent, the shortcut way to find that information is to use the HU Help:User Information option at the message action prompt. This saves you the steps of getting out of the message and going back to the MailMan menu to get the same information.

### Ignore ("I") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Ignore action code (i.e., "I") to "ignore" a message (take no action) and leave it in the current mail basket.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/109.png) | NOTE: If you use the caret ("^") to stop reading a new message without reading all responses and "ignore" that message, the message will *not* remain marked as "new," even though you have new (unread) responses. If you enter the caret at the "Enter message action" prompt, however, the message will remain marked as "new." |

To "ignore" a message and leave it in the same mail basket, either press the \<Enter\> key to accept the "IGNORE" default, if indicated, or enter an "I" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: TEST DELIVERY BASKET \[#1212448\] 05/14/98@07:10 2 lines

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

4 of 4 responses read. In '1 Mail Test' basket. Page 1

--------------------------------------------------------------------------------

Enter message action (in 1 Mail Test basket): IGNORE// \<Enter\>

1 Mail Test Basket, 1 message

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

1\. \[1212448\] 05/14/98 TEST DELIVERY BASKET 2 XMUSER2,TWO M. 4/4

Enter message number or command:

<span id="_Ref449433961" class="anchor"></span>Figure 4‑21. Ignoring a message

In this example (Figure 4‑21), the user "ignored" this message by pressing the \<Enter\> key at the "Enter message action (in 1 Mail Test basket): IGNORE//" prompt to accept the default response (i.e., "IGNORE"). The user also could have entered an "I" (Ignore) after the prompt.

|                                                                                                                |                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/110.png) | NOTE: The message action default response for the "IN" mail basket is set by you when entering your personal preferences with the User Options Edit option. |

|                                                                                                                |                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/111.png) | REF: For more information on setting your message action default for the "IN" mail basket or the User Options Edit option, please refer to the "Message Action Default" topic in Chapter 4 in the *MailMan Getting Started Guide*. |

In this case, ignoring the message simply keeps the message in the "1 Mail Test" mail basket.

After ignoring the message, MailMan returned the user to the message list action prompt where he could take any additional actions on the messages in the basket.

### Include Message ("IM") Action 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), when you are sending a message, you can use the Include Message action code ("IM") to include a response or any combination of responses from another message in the new message being created.

There are two ways you can use the Include Message action:

1.  Creating a New Message
2.  Replying to an Existing Message

#### Creating a New Message

You can include replies from another message when you originate a message using the Send a Message action from the MailMan menu. For example, suppose you wish to send a new message in which you refer to another message and to the responses to that message and you want to include some part(s) of that message. You want to start a new message, not simply add a reply to a previous message.

From the main MailMan menu, choose S for Send a Message, begin the message, then save the message text and close the editor. Next enter the addressees of the message. At the Transmit Now prompt, type "IM" for Include Message, as in the example below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: s \<Enter\> Send a Message

Subject: Include Message Example

You may enter the text of the message...

=\[ WRAP \]==\[ INSERT \]====\< Include Message Example \>===\[ \<PF1\>H=Help \]====

Here is the beginning of the message in which I wish to include part of another message.

\<======T======T======T=====T=====T=====T=====T=====T=====T\>=====

<span id="_Toc147225816" class="anchor"></span>Figure 4‑22. Creating a new message in which to include a message

This is what you see when you save the message text and close the editor. MailMan prompts you for the addressees of your message:

Send mail to: XMUSER4,FOUR// \<Enter\> XMUSER4,FOUR

Select basket to send to: IN// \<Enter\>

And Send to: 9999 \<Enter\> XMUSER2,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 09/02/00@12:28

If wishes were horses, beggars would ride.

...OK? Yes// \<Enter\> (Yes)

Select Message option: Transmit now// im \<Enter\> Include responses from another Message

Include responses from which message: (11630-1420279): 1419307 \<Enter\> Local: biweekly info exchange message \# 44

There are 4 responses. Response 0 is the original message. (?? shows index)

Select the responses to include: ??

There are 4 responses. Response 0 is the original message.

Response.....From....................................................Lines

0\) 09/18/00 POSTMASTER 2

1\) 09/18/00 XMUSER1,ONE – COMPUTER SPECIALIST OIREDACTED 4

2\) 09/26/00 XMUSER2,TWO M - COMPUTER SPECIALIST (Oakland OI Field Office) 2

3\) 09/26/00 XMUSER4,FOUR - Tech Writer (Vista Maintenance Team) 3

4\) 09/26/00 XMUSER23,TWENTY3 - COMPUTER SPECIALIST (Oakland OI Field Office) 1

Select the responses to include: 1

Copying...

You may edit the text of the message...

=\[ WRAP \]==\[ INSERT \]====\< Include Message Example \>====\[ \<PF1\>H=Help \]===

Here is the beginning of the message in which I wish to include part of another message.

In the message:

\>Subj: Local: biweekly info exchange message \# 44 \[#1419307\]

\>From: POSTMASTER

\>Sent: 09/18/00@06:00

On 09/18/00@12:08 (Response \#1) XMUSER1,ONE wrote:

\>We need to replace a housing in the Alpha disk drives. It's scheduled

\>tomorrow @ 4pm. I believe we have a way of doing it without taking down

\>the system but if it doesn't work, the system will be down for 45 min - 1

\>hr.

\<======T======T======T======T======T======T======T=======T=======T\>======

<span id="_Toc147225817" class="anchor"></span>Figure 4‑23. Including a message in a new message

When MailMan asks, "Include responses from which message," type the message number. MailMan returns the message subject and the number of responses, and tells you that ?? (double question marks) will display the message index. Type ?? and the index lists the responses and respondents in order. You need only select the responses to include and MailMan copies them to your message.

|                                                                                                                |                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/112.png) | NOTE: You can edit the text of the message you have copied into your message. |

#### Replying to an Existing Message

When you are answering a message, you can include responses from another message by using the Reply and Include responses ("RI") action code. The "RI" command enables you to include responses from one message when you are replying to another message. See the Reply and Include responses action code in this chapter for a detailed description and an example.

### Information Only ("IN") Action (Toggle)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Information Only Toggle action code (i.e., "IN") to make a message sent by you informational only and *not* allow any further replies or toggle an Information Only message and allow replies.

To make a message Information Only or not, enter an "IN" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Priority Test from One \#1 \[#1214918\] 06/04/98@15:58 2 lines

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

3 of 3 responses read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// IN

Message is now 'Information only'. No one may reply.

Enter message action (in TEST basket): IGNORE// IN

Message is no longer 'Information only'.

Enter message action (in TEST basket): IGNORE//

<span id="_Ref431026563" class="anchor"></span>Figure 4‑24. Toggling a message—Information only vs. not information only

In this example (Figure 4‑24), the user originally sent a message out allowing all recipients to respond (i.e., *not* Information Only). Later, the user decided to make the message Information Only, preventing the recipients from replying to the message, by entering an "IN" (Information Only) at the "Enter message action (in TEST basket): IGNORE//" prompt.

To allow all recipients to, once again, be able to respond to the message, the user simply had to toggle the message by entering another "IN" at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan accepted the latest entry and confirmed that the message was no longer "Information Only." Thus, all recipients could reply to the message, once again.

After toggling the Information Only action code, MailMan returned the user to the message action prompt where the user could take any additional actions on this message.

### Priority Replies ("K") Action (Toggle)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Priority Replies Toggle action code (i.e., "K") to switch from receiving responses to a priority message as priority or not depending on how you set your PRIORITY RESPONSES FLAG field in the User Options Edit option.

To toggle between "Responses are ORDINARY" and "Responses are PRIORITY", enter a "K" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Priority message \[#1224355\] 08/11/98@14:11 1 line

From: XMUSER4,FOUR - Q... Continuum In 'IN' basket. Page 1 !Priority!

-------------------------------------------------------------------------------

This is sent Priority!

Enter message action (in IN basket): IGNORE// K

Responses will be delivered as Priority Mail.

Enter message action (in IN basket): IGNORE// K

Responses will not be delivered as Priority Mail.

Enter message action (in IN basket): IGNORE//

<span id="_Ref427480628" class="anchor"></span>Figure 4‑25. Switching back and forth on how responses are received with a priority message

In this example (Figure 4‑25), by entering a "K" at the "Enter message action (in IN basket): IGNORE//" prompt, the user toggled how he wanted responses for this priority message to be delivered.

The user asked MailMan to switch from delivering responses as ordinary to delivering responses as priority (i.e., "Responses will be delivered as Priority Mail."). This also sets the default answer the next time the user would be presented with the "Deliver future responses to this message as Priority Mail?" prompt.

The user then toggled back to have all responses delivered as ordinary (i.e., "Responses will not be delivered as Priority Mail") by, again, entering "K" after the Enter message action (in IN basket): IGNORE//" prompt.

After toggling how priority responses will be received, MailMan returned the user to the message action prompt where he could take any additional actions on this message.

|                                                                                                                |                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/113.png) | REF: For more information on the priority prompt and the User Options Edit option, please refer to the "Priority Responses" topic in Chapter 4 in the *MailMan Getting Started Guide*. |

### Later ("L") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Later action code (i.e., "L") to have a message made "new" at a specified later date and time. If the message already resides in your mailbox, it will simply be made "new" again. If the message no longer resides in your mailbox, it will be redelivered to your mailbox as a "new" message.

If you later a message and then try to later the same message again, MailMan will notify you that the message has already been "latered" and then gives you the chance to:

- Add another "Later" date on which this message should appear new
- Change the current "Later" date
- Delete the current "Later" date

|                                                                                                                |                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/114.png) | NOTE: This feature of the Later action code is available with all message readers. |

Also, MailMan gives you the option to review (list) all messages with "latered" dates and times using the Report on Later'd Messages option and make any modifications to those dates and times using the Change/Delete Later'd Messages option.

|                                                                                                                |                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/115.png) | REF: For more information on the Report on Later'd Messages and Change/Delete Later'd Messages options, please refer to Chapter 11, "Reports and Lists," in this manual. |

To "Later" a message, enter an "L" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: test2 \[#1221443\] 07/21/98@15:20 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'TEST' basket. Page 1

---------------------------------------------------------

here is a test

Enter message action (in TEST basket): IGNORE// L

DATE MESSAGE WILL BE NEW: T+1// ?

Enter a date or date @ time on which you wish this message to be new.

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer assumes a date in the FUTURE.

You may omit the precise day, as: JAN, 1957

If only the time is entered, the current date is assumed.

Follow the date with a time, such as JAN 20@10, T@10AM, 10:30, etc.

You may enter a time, such as NOON, MIDNIGHT or NOW.

DATE MESSAGE WILL BE NEW: T+1// \<Enter\> (AUG 19, 1998)

Enter message action (in TEST basket): IGNORE//

<span id="_Ref428083289" class="anchor"></span>Figure 4‑26. "Latering" a message

In the previous example (Figure 4‑26), the user wanted to make a message new again by "latering" it for a future date and time. Thus, she entered an "L" (Later) at the "Enter message action (in TEST basket): IGNORE//" prompt.

When presented with the "DATE MESSAGE WILL BE NEW: T+1//" prompt, the user chose to enter a question mark ("?") to display the acceptable VA FileMan date and time formats one can enter.

The user chose to later the message for the next day by choosing the default response by pressing the \<Enter\> key at the "DATE MESSAGE WILL BE NEW: T+1//" prompt (i.e., T+1, where "T" equals today's date plus one day, which is the next day).

MailMan displayed the "later" date in parentheses as (i.e., "AUG 19, 1998).

After "latering" the message, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

The following example illustrates changing a previously set "Later" date:

Subj: test \[#1212124\] 05/12/98@08:47 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'TEST' basket. Message will be NEW Later. Page 1

-------------------------------------------------------------------------------

this is a test message.

Enter message action (in TEST basket): IGNORE// L

DATE MESSAGE WILL BE NEW: T+1// \<Enter\> (AUG 19, 1998)

Enter message action (in TEST basket): IGNORE// L

Message will be NEW on: 08/19/98

Select one of the following:

A Add another date on which this message should appear new

C Change this date

D Delete this date

Enter response: C \<Enter\> Change this date

DATE MESSAGE WILL BE NEW: AUG 19,1998// 8/20/98 \<Enter\> (AUG 20, 1998)

Enter message action (in TEST basket): IGNORE//

<span id="_Ref428082995" class="anchor"></span>Figure 4‑27. Changing a "Later" date

In the previous example (Figure 4‑27), the user wanted to make a message she just read appear as "new" at a later date and time. Thus, she entered an "L" (Later) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan then asked the user to enter the date and time to make the message new. For this example, the user chose to later the message for the next day by accepting the default response by pressing the \<Enter\> key at the "DATE MESSAGE WILL BE NEW: T+1//" prompt (i.e., T+1, where "T" equals today's date plus one day, which is the next day).

MailMan accepted the entry and displayed the "later" date in parentheses (i.e., "AUG 19, 1998").

Continuing with this example, the user, again, chose to "later" the same message by entering another "L" at the "Enter message action (in TEST basket): IGNORE//" prompt. This time MailMan notified the user that this message already had a "later" date by displaying "Message will be NEW on: 08/19/98" and presenting the user with a list of "latering" options.

At this point, the user decided to change the previous "later" date, so she entered "C" at the "Enter response:" prompt.

MailMan then asked the user to enter the new "later" date. In this case, she entered "8/20/98" at the "DATE MESSAGE WILL BE NEW: AUG 19,1998//" prompt.

Once again, MailMan displayed the changed "later" date in parentheses as "(AUG 20, 1998)".

### New/Un New ("N") Action (Toggle)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the New/Un New Toggle action code (i.e., "N") to:

- Make a message "new"—MailMan *adds* the new flag (i.e., "\*" asterisk) next to the message, as if it has not been opened/read yet.
- Make a "new" message *not* appear as "new"—MailMan *removes* the new flag (i.e., "\*" asterisk) next to the message, as if it was already opened/read.

You can toggle between these two actions with this one action code.

To toggle a message from "new" to "*not* new" or vice versa, enter an "N" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Test \[#1219990\] 07/09/98@13:46 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

1 of 1 response read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// N

Message will be new next time.

Enter message action (in TEST basket): IGNORE// N

Message will NOT be new next time.

Enter message action (in TEST basket): IGNORE//

<span id="_Ref431027517" class="anchor"></span>Figure 4‑28. Toggling a message—New vs. not new

In this example (Figure 4‑28), after reading a message, the user wanted to make it so it would appear as "new" the next time he read the mail. Thus, he entered an "N" (New) at the "Enter message action (in TEST basket): IGNORE//" prompt.

To *not* have the message appear as new the next time he read the mail (i.e., Un New), the user simply had to toggle the message by entering another "N" at the "Enter message action (in TEST basket): IGNORE//" prompt. MailMan accepted the latest entry and confirmed that the message would *not* appear as "new" the next time he read the mail.

After toggling the New/Un New action code, MailMan returned the user to the message action prompt where he could take any additional actions on this message.

### Print ("P") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Print action code (i.e., "P") to print a message to any specified device. The default response will always be to print the original message and all responses; however, you can now choose to print any combination of responses (single or ranges), with or without the original message. Also, for example, if you print responses "10-", MailMan understands that you mean print from response 10 through the last response.

|                                                                                                                |                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/116.png) | NOTE: When printing a KIDS or PackMan message, you will be given the choice of what to print, with the default being just the description. |

To print a message, enter a "P" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: Test \[#1219990\] 07/09/98@13:46 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

1 of 1 response read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// P

Print recipient list? No// YES

Select one of the following:

D Detail

S Summary

Print Detail or Summary recipient chain: Summary// \<Enter\>

There is 1 response. Response 0 is the original message. (?? shows index)

Select the responses to Print: 0-1// 0

DEVICE: HOME// \<Enter\> Telnet terminal

MailMan message for XMUSER1,ONE E. COMPUTER SPECIALIST

Printed at REDACTED.VA.GOV 08/11/98@14:49

Subj: Test \[#1219990\] 07/09/98@13:46 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

1 of 1 response read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

here is a test

Local Message-ID: 1219990@REDACTED.VA.GOV (1 Recipient)

This message was addressed as follows:

XMUSER1,ONE E.

Enter message action (in TEST basket): IGNORE//

<span id="_Ref449434018" class="anchor"></span>Figure 4‑29. Printing a message with recipient information

As the previous example shows (Figure 4‑29), to print a message, the user simply had to enter a "P" (Print) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan then prompted the user to choose if she wanted to print the list of recipients along with the message. For this example, the user decided to include a list of recipients by entering "Yes" at the "Print recipient list? No//" prompt.

The user was then given the choice of printing either a "Detail" or "Summary" list of recipients:

- Summary list (default)—The Summary list provides the same information you see when you do a query on a message (i.e., Query action code).

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/117.png) | REF: For more information on the Query action code, please refer to the "Query ("Q") Action" topic that follows in this chapter. |

- Detail list—The Detail list provides the same information you see when you do a detailed query on a message (i.e., Query Detailed action code).

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/118.png) | REF: For more information on the Query action code, please refer to the "Query ("Q") Action" topic that follows in this chapter. |

For this example, the user chose to only print a Summary list by pressing the \<Enter\> key to accept the default response (i.e., Summary) at the "Print Detail or Summary recipient chain: Summary//" prompt.

|                                                                                                                |                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/119.png) | REF: For an example of a Detail Summary list, please refer to the "Headerless Print ("H") Action" topic previously described in this chapter. |

MailMan then asked the user to choose what portion of the message she wanted to print (e.g., original message, original message plus any combination of responses). In this case, she just wanted to print the original message by entering "0" at the "Select the responses to Print: 0-1//" prompt.

|                                                                                                                |                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/120.png) | NOTE: If the message you are printing does not have any responses, MailMan will not ask this question. |

MailMan then asked the user to choose where to print the message (i.e., what device). In this case, the user chose to print the message to the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt. MailMan immediately begins printing the message.

|                                                                                                                |                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/121.png) | NOTE: If you want to print your message(s) to a different device (e.g., a printer), enter the appropriate device name at the "DEVICE: HOME//" prompt. |

MailMan printed the original message text the user requested preceded by the print and header information. Also, since the user chose to print a Summary list of recipient information, MailMan printed that information after the original message text.

After printing the message, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

The following figure demonstrates printing a message *without* recipient information:

Subj: Test \[#1219990\] 07/09/98@13:46 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (San Francisco

1 of 1 response read. In 'TEST' basket. Page 1

------------------------------------------------------

Enter message action (in TEST basket): IGNORE// P

Print recipient list? No// \<Enter\> NO

There is 1 response. Response 0 is the original message. (?? shows index)

Select the responses to Print: 0-1// 0

DEVICE: HOME// \<Enter\> Telnet terminal

MailMan message for XMUSER1,ONE E. COMPUTER SPECIALI

Printed at REDACTED.VA.GOV 08/11/98@14:51

Subj: Test \[#1219990\] 07/09/98@13:46 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (San Franc

1 of 1 response read. In 'TEST' basket. Page 1

------------------------------------------------------

here is a test

Enter message action (in TEST basket): IGNORE//

<span id="_Ref431088129" class="anchor"></span>Figure 4‑30. Printing a message without recipient information

In this example (Figure 4‑30), the user chose to print the same message but *without* any recipient information. Thus, she entered a "P" (Print) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan then prompted the user to choose if she wanted to print the list of recipients along with the message. For this example, since she did *not* want to include a list of recipients, she accepted the "No" default by pressing the \<Enter\> key at the "Print recipient list? No//" prompt.

Again, MailMan asked the user to choose what portion of the message she wanted to print (e.g., original message, original message plus any combination of responses. As before, the user just wanted to print the original message by entering "0" at the "Select the responses to Print: 0-1//" prompt.

MailMan then asked the user to choose where to print the message (i.e., what device). Once again, the user chose to print the message to the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt. MailMan immediately begins printing the message.

MailMan printed the original message text preceded by the print and header information *without* printing any recipient information.

After printing the message, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

### Query ("Q") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Query action code (i.e., "Q") to inquire about general address information on a message.

When doing a query on a message, MailMan will display the following information:

- Message Header—The message header includes the "Subject," and "From" information of the message.
- Local Message ID—This is the MailMan internal message identification number and MailMan location.
- Number of Recipients—This is the total number of recipients of the message (including the total number of members in any mail groups).
- List of Addressees—This is a list of the local and remote users and any mail groups that were addressees of the message.

To query a message for general recipient information, enter a "Q" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Enter message action (in IN basket): IGNORE// Q

Subj: FW: Tribal Wisdom vs. Government Policy \[#1220558\]

Tue, 07/14/98@11:00:33 -0700 50 lines

From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\> In 'IN' basket.

Local Message-ID: 1220558@REDACTED.VA.GOV (29 Recipients)

This message was addressed as follows:

G.HUMOR

XMUSER5,FIVE J.

xmuser4fs@xxx.COM

g.irm@SHERIDAN.VA.GOV

jlg@SEATTLE.VA.GOV

Enter message action (in IN basket): IGNORE//

<span id="_Ref431104623" class="anchor"></span>Figure 4‑31. Query a message—General information

In this example (Figure 4‑31), after reading a message, the user wanted to see to whom this message was addressed. Thus, to query a message for general addressee information, the user simply had to enter a "Q" (Query) at the "Enter message action (in IN basket): IGNORE//" prompt.

MailMan then displayed the following information:

- Message header:

> Subj: FW: Tribal Wisdom vs. Government Policy \[#1220558\]

> Tue, 07/14/98@11:00:33 -0700 50 lines

> From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\> In 'IN' basket.

- Local message ID—1220558@REDACTED.VA.GOV
- Number of recipients—29
- List of addressees—See below

As you can see in this example, the message was addressed to the following:

- G.HUMOR (mail group)
- XMUSER5,FIVE J. (local recipient)
- xmuser4fs@xxx.COM (remote recipient)
- g.irm@SHERIDAN.VA.GOV (remote recipient)
- jlg@SEATTLE.VA.GOV (remote recipient)

Though MailMan lists 5 addressees, you see that there are a total of 29 recipients. Since there are 4 individual recipients (local and remote) and 1 mail group (i.e., G.HUMOUR), you can conclude that the mail group must contain 25 members/recipients (i.e., 29 - 4 = 25).

After the query, MailMan returned the user to the message action prompt where he could take any additional actions on this message.

### Query Recipients ("Q xxx") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Query Recipients action code (i.e., "Q xxx"—where "xxx" represents the name of a person) to inquire about specific local and remote recipients of a message. MailMan will display *all* recipients who match your entry. The more characters entered (*not* case sensitive), the more closely MailMan can match your entry to the list of recipients.

When doing a query on a message for a specific person, regardless of a match, MailMan will always display the following information about the message:

- Message Header—The message header includes the "Subject," and "From" information of the message.
- Local Message ID—This is the MailMan internal message identification number and MailMan location.
- Number of Recipients—This is the total number of recipients of the message (including the total number of members in any mail groups).

If MailMan finds an addressee on the message who matches the person entered, MailMan will display the detailed information for that addressee.

If the addressee is a local recipient, MailMan provides the following information:

- Name—MailMan displays the name(s) of the local recipient(s) who match your entry.
- Status—This indicates the current status of the message in the local recipient's mailbox. For example, if and when the recipient read the message. This includes the following information:
- Not read—If the local recipient has not read the message, MailMan will display this message.
- First read date and time—The date and time the local recipient first read the message.
- Last read date and time—The date and time the local recipient last read the message. Associated with this date is the number of responses read. If the message has any responses, MailMan will indicate the total number of responses read (if any).
- Terminated date and time—If the local recipient has terminated the message, MailMan will display the date that they terminated the message.
- Forwarding Information—If the message was forwarded to the local recipient, MailMan will indicate the name of the person who forwarded the message and the date and time the message was forwarded.

If the addressee is a remote recipient, MailMan provides the following information:

- Name—MailMan displays the name(s) of the remote recipient(s) who match your entry.
- Sent—The date and time the message was sent over the network to the remote recipient.
- Time—This is the time (in seconds) it took to transmit the message over the network to the remote recipient.
- Remote Message ID—If sent to a remote MailMan user, MailMan will display the internal message identification number for the message and the remote user's MailMan location. This information is *not* displayed when the message was sent to a *non*-MailMan location.
- Forwarding Information—If the message was forwarded to the remote recipient, MailMan will indicate the name of the person who forwarded the message and the date and time the message was forwarded.

If MailMan *cannot* find a match, no recipient detailed information can be displayed; however, MailMan will still display information about the message itself (i.e., message header, local message ID, and the number of recipients).

To query a message for detailed information on a specific recipient, enter a "Q" and the recipient's name at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Enter message action (in IN basket): IGNORE// Q xmuser1

Subj: FW: Tribal Wisdom vs. Government Policy \[#1220558\]

Tue, 07/14/98@11:00:33 -0700 50 lines

From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\> In 'IN' basket.

Local Message-ID: 1220558@REDACTED.VA.GOV (29 Recipients)

Searching for recipients that match 'xmuser1'.

XMUSER1,ONE Last read: 08/11/98@14:57 \[First read: 07/15/98@08:30\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

Enter message action (in IN basket): IGNORE//

<span id="_Hlt431177979" class="anchor"></span>Figure 4‑32. Query a message—Specific recipient

In this example (Figure 4‑32), after reading a message, the user wanted to see if a specific person was a recipient of the message. Thus, to query a message for a specific recipient, One Xmuser1, he simply had to enter "Q xmuser1" (Query xxx) at the "Enter message action (in IN basket): IGNORE//" prompt. You can enter any amount of characters (*not* case sensitive), however, the more characters you enter enables MailMan to more closely match your entry to the list of recipients.

MailMan first displayed the following information about the message:

- Message header:

> Subj: FW: Tribal Wisdom vs. Government Policy \[#1220558\]

> Tue, 07/14/98@11:00:33 -0700 50 lines

> From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\> In 'IN' basket.

- Local message ID—1220558@REDACTED.VA.GOV
- Number of recipients—29

Also, MailMan found a matching recipient to the name the user entered and displayed detailed information on that user. This confirmed that the person was a recipient of this message.

The detailed information on the matching recipient included the following:

- Name—XMUSER1,ONE E.
- Last read date and time—08/11/98@14:57
- First read date and time—07/15/98@08:30
- Forwarded by—XMUSER5,FIVE J. 07/14/98@13:00

Based on the information displayed, you know that the recipient was a local user.

After the query, MailMan returned the user to the message action prompt where he could take any additional actions on this message.

If the user had entered a person who was *not* a recipient of a message, you would see the following:

Enter message action (in IN basket): IGNORE// q xxxxxx

Subj: FW: Tribal Wisdom vs. Government Policy \[#1220558\]

Tue, 07/14/98@11:00:33 -0700 50 lines

From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\> In 'IN' basket.

Local Message-ID: 1220558@REDACTED.VA.GOV (29 Recipients)

Searching for recipients that match 'xxxxxx'.

Enter message action (in IN basket): IGNORE//

<span id="_Toc436461071" class="anchor"></span>Figure 4‑33. Query a message—Specific recipient not found

### Query Current ("QC") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Query Current action code (i.e., "QC") to retrieve information for local recipients who are "current" (i.e., read all of the responses) on a message.

When doing a "current" query on a message, MailMan displays the following information:

- Message Header—The message header includes the "Subject," and "From" information of the message.
- Local Message ID—This is the MailMan internal message identification number and MailMan location.
- Number of Recipients—This is the total number of recipients of the message (including the total number of members in any mail groups).
- Addressee Information—MailMan displays addressee information for all local users who are recipients of the message and "current" on all responses (including all members of any mail groups).

> For each local recipient, MailMan provides the following information:

- Name—MailMan displays the name(s) of the local recipient(s).
- Status—This indicates the current status of the message in the local recipient's mailbox. For example, if and when the recipient read the message. This includes the following information:
- Last read date and time—The date and time the local recipient last read the message.
- First read date and time—The date and time the local recipient first read the message.
- Forward date and time—If the message was forwarded to the local recipient, MailMan indicates the date and time the message was forwarded.

To query a message for "current" recipient information, enter a "QC" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Enter message action (in IN basket): Ignore// qc \<Enter\> Query Current

Subj: XU\*8.0\*382 INSTALLATION \[#1696643\] 15 Nov 2005 06:07:47 -0700 (PDT)

10 lines

From: \<XMUSER.EIGHT@NXT.KERNEL.REDACTED.VA.GOV\> In 'IN' basket.

Local Message-ID: 1696643@REDACTED.VA.GOV (14 recipients)

XMUSER2,TWO Last read: 11/15/05@11:32 \[First read: 11/15/05@11:32\]

Forwarded on: 11/15/05@09:06

XMUSER3,THREE Last read: 11/16/05@22:58 \[First read: 11/16/05@22:58\]

Forwarded on: 11/15/05@09:06

XMUSER4,FOUR Last read: 11/16/05@05:23 \[First read: 11/16/05@05:23\]

Forwarded on: 11/15/05@09:06

XMUSER5,FIVE Last read: 11/17/05@07:10 \[First read: 11/17/05@07:10\]

Forwarded on: 11/15/05@09:06

XMUSER1,ONE Last read: 08/22/06@13:05 \[First read: 08/22/06@12:53\]

Forwarded on: 11/15/05@09:06

XMUSER6,SIX Last read: 11/16/05@16:41 \[First read: 11/16/05@16:41\]

Forwarded on: 11/15/05@09:06

Local recipients who are current: 6 of 12

Enter message action (in IN basket): Ignore//

<span id="_Ref144015922" class="anchor"></span>Figure 4‑34. Query a message—Information on local recipients that are current

In this example (Figure 4‑34), after reading a message, the user wanted to see information on all local recipients that have read all responses to the message (i.e., current on the message). Thus, to query a message for "current" information on recipients, she simply had to enter "QC" (Query Current) at the "Enter message action (in IN basket): IGNORE//" prompt.

MailMan first displayed the following information about the message:

- Message header:

> Subj: XU\*8.0\*382 INSTALLATION \[#1696643\] 15 Nov 2005 06:07:47 -0700 (PDT)

> 10 lines

> From: \<XMUSER.EIGHT@NXT.KERNEL.REDACTED.VA.GOV\> In 'IN' basket.

- Local message ID—1696643@REDACTED.VA.GOV
- Number of recipients—14 (12 local and 2 remote)

Also, MailMan listed and provided information on 6 of the 12 local recipients that had read all responses (Figure 4‑34). This message had both local and remote recipients.

For example, the information on a local recipient included the following:

- Name—XMUSER2,TWO
- Last read date and time—11/15/05@11:32
- First read date and time—11/15/05@11:32
- Forwarded on—11/15/05@09:06

After the query, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

### Query Detailed ("QD") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Query Detailed action code (i.e., "QD") to retrieve detailed information for each addressee (local and remote recipients) of a message.

When doing a detailed query on a message, MailMan displays the following information:

- Message Header—The message header includes the "Subject," and "From" information of the message.
- Local Message ID—This is the MailMan internal message identification number and MailMan location.
- Number of Recipients—This is the total number of recipients of the message (including the total number of members in any mail groups).
- Addressee Information—MailMan displays detailed addressee information for all local and remote users who are recipients of the message (including all members of any mail groups).

> For each *local* recipient, MailMan provides the following information:

- Name—MailMan displays the name(s) of the local recipient(s).
- Status—This indicates the current status of the message in the local recipient's mailbox. For example, if and when the recipient read the message. This includes the following information:
- Not read—If the local recipient has not read the message, MailMan will display this message.
- First read date and time—The date and time the local recipient first read the message.
- Last read date and time—The date and time the local recipient last read the message. Associated with this date is the number of responses read. If the message has any responses, MailMan will indicate the total number of responses read (if any).
- Terminated date and time—If the local recipient has terminated the message, MailMan will display the date that they terminated the message.
- Forward date and time—If the message was forwarded to the local recipient, MailMan will indicate the name of the person who forwarded the message and the date and time the message was forwarded.

|                                                                                                                |                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/122.png) | NOTE: MailMan also indicates when a surrogate has read a message. |

> For *remote* recipients, MailMan provides the following information:

- Name—MailMan displays the name(s) of the remote recipient(s).
- Sent—The date and time the message was sent over the network to the remote recipient(s).
- Time—This is the time (in seconds) it took to transmit the message over the network to the remote recipient(s).
- Remote Message ID—If sent to a remote MailMan user, MailMan will display the internal message identification number for the message and the remote user's MailMan location. This information is *not* displayed when the message is sent to a *non*-MailMan location.
- Forwarding Information—If the message was forwarded to the remote recipient, MailMan will indicate the name of the person who forwarded the message and the date and time the message was forwarded. This includes auto-forward and filter-forward information.

Also, when you do a detailed query on a message that was sent to you and you have your mail automatically forwarded to a remote address, the query clearly shows that you are the one who forwarded the message to that address.

|                                                                                                                |                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/123.png) | REF: For more information on having your mail automatically forwarded, please refer to Chapter 10, "Forward," in this manual. |

To query a message for detailed recipient information, enter a "QD" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Enter message action (in IN basket): IGNORE// QD

Subj: FW: Tribal Wisdom vs. Government Policy \[#1220558\]

Tue, 07/14/98@11:00:33 -0700 50 lines

From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\> In 'IN' basket.

Local Message-ID: 1220558@REDACTED.VA.GOV (29 Recipients)

XMUSER21,TWENTY1 Last read: 07/15/98@09:58 \[First read: 07/15/98@09:58\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER22,TWENTY2 Last read: 07/15/98@08:45 \[First read: 07/15/98@08:45\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER12,TWELVE Last read: 07/14/98@15:59 \[First read: 07/14/98@15:59\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER5,FIVE J. Last read: 07/14/98@13:00 \[First read: 07/14/98@13:00\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER2,TWO M. Last read: 07/14/98@15:27 \[First read: 07/14/98@15:27\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER1,ONE E. Last read: 08/11/98@15:03 \[First read: 07/15/98@08:30\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER50,FIFTY@PITTSBURGH.MED.VA.GOV Sent: 07/14/98@13:05 Time: 2 seconds

Message ID: 37513570@PITTSBURGH.MED.VA.GOV

Auto-Forwarded by: XMUSER50,FIFTY 07/14/98@13:05

xmuser4fs@xxx.COM Sent: 07/14/98@13:54 Time: 0 seconds

Forwarded by: XMUSER4,FOUR 07/14/98@13:54

g.irm@SHERIDAN.VA.GOV Sent: 07/28/98@14:10 Time: 7 seconds

Message ID: 2831665@SHERIDAN.VA.GOV

Forwarded by: XMUSER40,FORTY 07/28/98@14:09

xxx@SEATTLE.VA.GOV Sent: 07/15/98@10:00 Time: 4 seconds

Message ID: 22346886@SEATTLE.VA.GOV

Forwarded by: XMUSER21,TWENTY1 07/15/98@09:58

G.IRM@GRAND-JUNCT.MED.VA.GOV Sent: 08/30/98@10:06 Time: 2 seconds

Message ID: 10690582@GRAND-JUNCT.MED.VA.GOV

Filter-Forwarded by: XMUSER60,SIXTY 08/30/98@10:04.

.

.

.

Enter message action (in IN basket): IGNORE//

<span id="_Ref431177994" class="anchor"></span>Figure 4‑35. Query a message—Detailed recipient information

In this example (Figure 4‑35), after reading a message, the user wanted to see detailed information on all recipients of the message. Thus, to query a message for detailed information on recipients, she simply had to enter "QD" (Query Detailed) at the "Enter message action (in IN basket): IGNORE//" prompt.

MailMan first displayed the following information about the message:

- Message header:

> Subj: FW: Tribal Wisdom vs. Government Policy \[#1220558\]

> Tue, 07/14/98@11:00:33 -0700 50 lines

> From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\> In 'IN' basket.

- Local message ID—1220558@REDACTED.VA.GOV
- Number of recipients—29

Also, MailMan listed all 29 recipients (Figure 4‑35, list abbreviated for space considerations) with detailed information on each recipient. This message had both local and remote recipients.

For example, the detailed information on a local recipient included the following:

- Name—XMUSER21,TWENTY1
- Last read date and time—07/15/98@09:58
- First read date and time—07/15/98@09:58
- Forwarded by—XMUSER5,FIVE J. 07/14/98@13:00

For example, the detailed information on a remote recipient at another MailMan site included the following:

- Name—g.irm@SHERIDAN.VA.GOV
- Date sent over the network—07/28/98@14:10
- Transmission time over the network—7 seconds
- Remote MailMan message ID—2831665@SHERIDAN.VA.GOV
- Forwarded by—XMUSER12,TWELVE 07/28/98@14:09

For example, the detailed information on a remote recipient *not* at a MailMan site included the following:

- Name—xmuser4fs@xxx.COM
- Date sent over the network—07/14/98@13:54
- Transmission time over the network—0 seconds
- Forwarded by—XMUSER4,FOUR 07/14/98@13:54

After the query, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

### Query Network ("QN") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Query Network action code (i.e., "QN") to retrieve network/trace header information and detailed information about each addressee (local and remote recipients) of a message; however, it is primarily used as a diagnostic tool.

|                                                                                                                |                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/124.png) | REF: For a complete description of the detailed information displayed for local and remote recipients, please refer to the "Query Detailed ("QD") Action" topic previously described in this chapter. |

Also, when messages are received from a *non*-MailMan remote sites, MailMan captures the "From" address from the message header and *not* from the envelope. The "From" address from the envelope is captured and is displayed by the QN action code when it differs from the message header "From" address.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/125.png) | NOTE: The envelope contains the "From" and "To" address used by the mail transport system and is not part of the message itself. |

You will not notice a difference with messages from other MailMan systems; however, other *non*-MailMan systems sometimes include clear-text names in the "From" address, in addition to the e-mail address.

For example, MailMan captures the following information:

> "'Zero Xmuser0' \<xmuser0@anydomain.com\>"

To query a message for network and detailed recipient information, enter a "QN" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Enter message action (in IN basket): IGNORE// QN

Subj: FW: Tribal Wisdom vs. Government Policy \[#1220558\]

Tue, 07/14/98@11:00:33 -0700 50 lines

From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\> In 'IN' basket.

Local Message-ID: 1220558@REDACTED.VA.GOV (29 Recipients)

Network header:

Received: from deptvass-xx.va.gov by REDACTED.VA.GOV (MailMan/8.0 TCP/IP-MAILMAN)

id 1220558 ; 07/14/98@11:51:44 -0800 (PST)

Received: (from xxxx@localhost) by deptvass-xx.va.gov (8.6.12/8.6.11) id

OAA16983 for \<xmuser17@REDACTED.VA.GOV\>; Tue, 07/14/98@14:49:46 -

0400

Received: from proxy4.ba.xxxx.com by deptvass-xx.va.gov via smap (3.2)

id xma016974; Tue, 07/14/98@14:49:38 -0400

Received: from shell3.ba.xxxx.com (fjx@shell3.ba.xxxx.com \[206.184.139.134\])

by proxy4.ba.xxxx.com (8.9.0/8.9.0/best.out) with ESMTP id LAA26145;

Tue, 07/14/98@11:45:48 -0700 (PDT)

X-Received: from proxy2.ba.xxxx.com (root@proxy2.ba.xxxx.com \[206.184.139.13\])

by shell3.ba.xxxx.com (8.9.0/8.9.0/best.sh) with ESMTP id LAA14340

for \<fjx+XRCPT.676a7740776e6574632e636f6d@shell3.ba.xxxx.com\>; Tue,

07/1498@11:03:16 -0700 (PDT)

X-Received: from xxxxxexc2.army.mil (XXXXXEXC2.ARMY.MIL \[138.27.199.115\])

by proxy2.ba.xxxx.com (8.9.0/8.9.0/best.in) with ESMTP id LAA27077

for \<fjx@xxxxx.com\>; Tue, 07/14/98@11:01:05 -0700 (PDT)

X-Received: by XXXXXEXC2 with Internet Mail Service (5.0.1460.8)

id \<N7MM7GT1\>; Tue, 07/14/98@11:00:36 -0700

Message-ID: \<E1B12D3A67E2CF119F600020AFFBF43AC593CE@XXXXXEXC2\>

From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\>

To: Twelve Xmuser12 \<xmuser12@llnl.gov\>, Five \<fjx@xxxxx.com\>,

"Xmuser22, Twenty2" \<xmuser22@xxxxx.army.mil\>,

"Xmuser11, Eleven" \<xmuser11e@xxxxx.army.mil\>,

"Xmuser29, Twebty9 (Maj) ~U" \<xmuser29@xxxxxx.af.mil\>

Subject: FW: Tribal Wisdom vs. Government Policy

Date: Tue, 07/14/98@11:00:33 -0700

X-Mailer: Internet Mail Service (5.0.1460.8)

X-Rcpt-To: fjx@xxxxx.com

<span id="_Ref427985865" class="anchor"></span>Figure 4‑36. Query a message for network information (1 of 2)

ReSent-Date: Tue, 07/14/98@11:45:35 -0700 (PDT)

ReSent-From: "Five J. Xmuser5" \<fjx@xxxxx.com\>

ReSent-To: xmuser5@REDACTED.VA.GOV,

Five Xmuser5 \<five.xmuser5@med.va.gov\>

ReSent-Message-ID: \<Pine.BSF.3.96.980714114535.1192A@she

XMUSER21,TWENTY1 Last read: 07/15/98@09:58 \[First read: 07/15/98@09:58\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER22,TWENTY2 Last read: 07/15/98@08:45 \[First read: 07/15/98@08:45\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER12,TWELVE Last read: 07/14/98@15:59 \[First read: 07/14/98@15:59\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER5,FIVE J. Last read: 07/14/98@13:00 \[First read: 07/14/98@13:00\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER2,TWO M. Last read: 07/14/98@15:27 \[First read: 07/14/98@15:27\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER4,FOUR Last read: 07/14/98@13:53 \[First read: 07/14/98@13:53\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

XMUSER1,ONE E. Last read: 08/11/98@15:03 \[First read: 07/15/98@08:30\]

Forwarded by: XMUSER5,FIVE J. 07/14/98@13:00

xmuser4fs@xxx.COM Sent: 07/14/98@13:54 Time: 0 seconds

Forwarded by: XMUSER4,FOUR 07/14/98@13:54

g.irm@SHERIDAN.VA.GOV Sent: 07/28/98@14:10 Time: 7 seconds

Message ID: 2831665@SHERIDAN.VA.GOV

Forwarded by: XMUSER5,FIVE J. 07/28/98@14:09

jlg@SEATTLE.VA.GOV Sent: 07/15/98@10:00 Time: 4 seconds

Message ID: 22346886@SEATTLE.VA.GOV

Forwarded by: XMUSER21,TWENTY1 07/15/98@09:58

.

.

.

Enter message action (in IN basket): IGNORE//

<span id="_Hlt428156128" class="anchor"></span>Figure 4‑37. Query a message for network information (2 of 2)

In this example (Figure 4‑37), after reading a message, the user wanted to see both network header information and detailed information on all recipients of the message. Thus, he did a Network Query by entering "QN" at the "Enter message action (in IN basket): IGNORE//" prompt.

MailMan first displayed the following information about the message:

- Message header:

> Subj: FW: Tribal Wisdom vs. Government Policy \[#1220558\]

> Tue, 07/14/98@11:00:33 -0700 50 lines

> From: "Xmuser41, Forty1" \<xmuser41@xxxxx.army.mil\> In 'IN' basket.

- Local message ID—1220558@REDACTED.VA.GOV
- Number of recipients—29

MailMan then displayed all of the network/trace header information. This information includes all the different mail server relay information while the message passed from server to server to all of the remote addressees.

Also, once again, MailMan listed all 29 recipients (Figure 4‑37, list abbreviated for space considerations) with detailed information on each recipient. This message had both local and remote recipients.

|                                                                                                                |                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/126.png) | REF: For examples of the detailed information for local and remote recipients on a MailMan system as well as remote recipients on a non-MailMan system, please refer to the "Query Detailed ("QD") Action" topic and Figure 4‑35 previously described in this chapter. |

After the query, MailMan returned the user to the message action prompt where he could take any additional actions on this message.

If the message header "From" person differs from the message envelope "From" person, MailMan will display the envelope information, as shown below:

Enter message action (in IN basket): IGNORE// qn

Subj: RE: \[HH\] FileMan/Kernel questions \[#1235752\]

10/16/98@11:59:14 -0800 (PST) 21 lines

From: XMUSER8.EIGHT@REDACTED.VA.GOV In 'IN' basket.

Local Message-ID: 1235752@REDACTED.VA.GOV (3 Recipients)

Envelope From:\<hh-errors@lists.xxxx.com\>

Network header:

Received: from deptvass-bh.va.gov by REDACTED.VA.GOV (MailMan/8.0 TCP/IP-MAILMAN)

id 1235752 ; 10/16/98@12:09:57 -0800 (PST)

Received: (from uucp@localhost) by deptvass-bh.va.gov (8.6.12/8.6.11) id

PAA29295; Fri, 10/16/98@15:06:10 -0400

Received: from lists1.xxxx.com by deptvass-bh.va.gov via smap (3.2)

id xma029267; Fri, 10/16/98@15:05:43 -0400

Received: (from daemon@localhost)

by lists1.xxxx.com (8.9.0/8.9.0/best.ls) id LAA29720;

Fri, 10/16/98@11:56:41 -0700 (PDT)

Message-Id: \<199810161856.LAA29720@lists1.xxxx.com\>

From: XMUSER8.EIGHT@REDACTED.VA.GOV

Subject: RE: \[HH\] FileMan/Kernel questions

Date: 10/16/98@11:59:14 -0800 (PST)

XXXServHost: lists.xxxx.com

In-Reply-To: \<199810052047.NAA27028@lists1.xxxx.com\>

Sender: hh-errors@lists.xxxx.com

Errors-To: hh-errors@lists.xxxx.com

Reply-To: hh@lists.xxxx.com

To: hh@lists.xxxx.com

XMUSER8,EIGHT Last read: 10/19/98@09:37 \[First read: 10/19/98@09:37\]

Forwarded on: 10/16/98@12:10

XMUSER5,FIVE J. Last read: 10/21/98@13:19 \[First read: 10/16/98@12:14\]

Forwarded on: 10/16/98@12:10

XMUSER1,ONE E. Last read: 10/21/98@13:27 \[First read: 10/21/98@13:20\]

Forwarded by: XMUSER5,FIVE J. 10/21/98@13:19

Enter message action (in IN basket): IGNORE//

<span id="_Toc436461074" class="anchor"></span>Figure 4‑38. Envelope information displayed using the Query Network action code

If the message header "From" person is the same as the "From" person on the message envelope, MailMan will *not* display the envelope information when doing a network query on a message.

If a message was sent locally and *not* over the network, MailMan displays the following when using the Query Network ("QN") action code:

Enter message action (in IN basket): IGNORE// qn

Subj: Software Purchase Questions \[#1226116\] 08/24/98@10:44 34 lines

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'IN' basket.

Local Message-ID: 1226116@REDACTED.VA.GOV (4 Recipients)

This message originated locally. There is no network header.

XMUSER11,ELEVEN Last read: 08/24/98@17:31 \[First read: 08/24/98@17:31\]

XMUSER4,FOUR Not read.

XMUSER1,ONE E. Last read: 08/25/98@09:23 \[First read: 08/24/98@10:44\]

XMUSER34,THIRTY4 Last read: 08/25/98@07:39 \[First read: 08/25/98@07:39\]

Enter message action (in IN basket): IGNORE//

<span id="_Toc436461075" class="anchor"></span>Figure 4‑39. Query a message sent locally for network information

### Query Not Current ("QNC") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Query Not Current action code (i.e., "QNC") to retrieve information for local recipients who are "*not* current" (i.e., have *not* read all of the responses) on a message.

When doing a "*not* current" query on a message, MailMan displays the following information:

- Message Header—The message header includes the "Subject," and "From" information of the message.
- Local Message ID—This is the MailMan internal message identification number and MailMan location.
- Number of Recipients—This is the total number of recipients of the message (including the total number of members in any mail groups).
- Addressee Information—MailMan displays addressee information for all local users who are recipients of the message and "not current" on all responses (including all members of any mail groups).

> For each local recipient, MailMan provides the following information:

- Name—MailMan displays the name(s) of the local recipient(s).
- Status—This indicates the current status of the message in the local recipient's mailbox. For example, if the recipient had *not* read the message. This includes the following information:
- Not read—Confirms the local recipients listed have *not* read the message.
- Forward date and time—If the message was forwarded to the local recipient, MailMan indicates the date and time the message was forwarded.

To query a message for "*not* current" recipient information, enter a "QNC" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Enter message action (in IN basket): Ignore// qnc \<Enter\> Query Not Current

Subj: XU\*8.0\*382 INSTALLATION \[#1696643\] 15 Nov 2005 06:07:47 -0700 (PDT)

10 lines

From: \<XMUSER.EIGHT@NXT.KERNEL.REDACTED.VA.GOV\> In 'IN' basket.

Local Message-ID: 1696643@REDACTED.VA.GOV (14 recipients)

XMUSER7,SEVEN Not read. Forwarded on: 11/15/05@09:06

XMUSER9,NINE Not read. Forwarded on: 11/15/05@09:06

XMUSER10,TEN Not read. Forwarded on: 11/15/05@09:06

XMUSER11,ELEVEN Not read. Forwarded on: 11/15/05@09:06

XMUSER0,ZERO Not read. Forwarded on: 11/15/05@09:06

XMUSER12,TWELVE Not read. Forwarded on: 11/15/05@09:06

Local recipients who are current: 6 of 12

Enter message action (in IN basket): Ignore//

<span id="_Ref144018085" class="anchor"></span>Figure 4‑40. Query a message for information on local recipients that are *not* current

In this example (Figure 4‑40), after reading a message, the user wanted to see information on all local recipients that have *not* read all responses to the message (i.e., *not* current on the message). Thus, to query a message for "not current" information on recipients, she simply had to enter "QNC" (Query Not Current) at the "Enter message action (in IN basket): IGNORE//" prompt.

MailMan first displayed the following information about the message:

- Message header:

> Subj: XU\*8.0\*382 INSTALLATION \[#1696643\] 15 Nov 2005 06:07:47 -0700 (PDT)

> 10 lines

> From: \<XMUSER.EIGHT@NXT.KERNEL.REDACTED.VA.GOV\> In 'IN' basket.

- Local message ID—1696643@REDACTED.VA.GOV
- Number of recipients—14 (12 local and 2 remote)

Also, MailMan listed and provided information on 6 of the 12 local recipients that had *not* read all responses (Figure 4‑40). This message had both local and remote recipients.

For example, the information on a local recipient included the following:

- Name—XMUSER7,SEVEN
- Last read date and time—11/15/05@11:32
- First read date and time—11/15/05@11:32
- Forwarded on—11/15/05@09:06

After the query, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

### Query Terminated ("QT") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Query Terminated action code (i.e., "QT") to retrieve information for local recipients who have terminated from a message.

When doing a terminated query on a message, MailMan displays the following information:

- Message Header—The message header includes the "Subject," and "From" information of the message.
- Local Message ID—This is the MailMan internal message identification number and MailMan location.
- Number of Recipients—This is the total number of recipients of the message (including the total number of members in any mail groups).
- Addressee Information—MailMan displays detailed addressee information for all local and remote users who are recipients of the message (including all members of any mail groups).

> For each local recipient, MailMan provides the following information:

- Name—MailMan displays the name(s) of the local recipient(s).
- Status—This indicates the current status of the message in the local recipient's mailbox. For example, when the recipient terminated the message. This includes the following information:
- Not read—Confirms the local recipients listed have *not* read the message.
- Last read date and time—The date and time the local recipient last read the message.
- First read date and time—The date and time the local recipient first read the message.
- Terminated date—If the message was terminated by the local recipient, MailMan indicates the date the message was terminated.
- Forward date and time—If the message was forwarded to the local recipient, MailMan indicates the person who forwarded the message and the date and time the message was forwarded.

To query a message for terminated recipient information, enter a "QT" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Enter message action (in IN basket): Ignore// qt \<Enter\> Query Terminated

Subj: Esignature in a Delphi application. \[#43854802\] 08/08/06@14:04 6 lines

From: XMUSER13,THIRTEEN - IT SPECIALIST 1 of 1 response read. In 'IN' basket.

Local Message-ID: 43854802@FORUM.VA.GOV (575 recipients)

XMUSER2,TWO Last read: 08/09/06@11:39 (1 of 1 response)

\[First read: 08/09/06@11:39\] Terminated: 08/09/06

XMUSER3,THREE Last read: 08/08/06@14:27 (1 of 1 response)

\[First read: 08/08/06@14:27\] Terminated: 08/10/06

XMUSER4,FOUR Not read. Forwarded by: XMUSER,TEN 06/14/06@10:31

.

.

.

.

XMUSER14,FOURTEEN Last read: 08/14/06@15:43 (1 of 1 response)

\[First read: 08/14/06@15:43\] Terminated: 08/14/06

Local recipients who have terminated: 13 of 472

Enter message action (in IN basket): Ignore//

<span id="_Ref144024463" class="anchor"></span>Figure 4‑41. Query a message for information on local recipients that have terminated

In this example (Figure 4‑41), after reading a message, the user wanted to see information on all local recipients that have terminated from the message. Thus, to query a message for terminated information on recipients, she simply had to enter "QT" (Query Terminated) at the "Enter message action (in IN basket): IGNORE//" prompt.

MailMan first displayed the following information about the message:

- Message header:

> Subj: Esignature in a Delphi application. \[#43854802\] 08/08/06@14:04 6 lines

> From: XMUSER13,THIRTEEN - IT SPECIALIST 1 of 1 response read. In 'IN' basket.

- Local message ID—43854802@FORUM.VA.GOV (575 recipients)
- Number of recipients—575 (472 local and 103 remote)

Also, MailMan listed and provided information on 13 of the 472 local recipients that had terminated the message (Figure 4‑41). This message had both local and remote recipients.

For example, the information on a local recipient included the following:

- Name—XMUSER2,TWO
- Last read date and time——08/09/06@11:39
- First read date and time—08/09/06@11:39
- Terminated date—08/09/06

After the query, MailMan returned the user to the message action prompt where she could take any additional actions on this message.

### Reply ("R") & Reply and Include responses ("RI") Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Reply action code (i.e., "R") or the Reply and Include responses action code (i.e., "RI") to reply to a message.

"Reply" immediately attaches your reply to the response chain so everyone on the message sees your reply, making it instantly available to anyone currently reading the message. Previously, the response was not attached to the message until the Background Filer was about to deliver the response to the recipients. Now, the response is attached to the message when the user transmits the message. (The Background Filer still delivers the response to the recipients.) This helps facilitate "real-time" conversations among message recipients.

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/127.png) | NOTE: MailMan automatically adds the sender as a recipient, if he is not already one, when a reply is made to the message. |

Also, you are able to copy the original message and/or any combination of responses into your reply (i.e., "RI—Reply and Include responses"). Thus, with this feature, you can more easily respond to what someone wrote, point by point.

Further, the "RI" (Reply and Include responses) command also enables you to include responses from another message (see example below). At the "Enter message action" prompt, type RI. MailMan asks you the message from which you would like to include responses. When you type a message number (internal entry number), MailMan displays the number of responses for that message and tells you to enter two question marks (??) to see an index. When you enter two question marks, MailMan displays the index of responses and asks you to select the responses you wish included.

Enter message action (in IN basket): Ignore// ri \<Enter\> Reply and Include responses

Include responses from which message: This message// ?

Press Enter to include previous responses from this message,

or enter the internal entry number of a different message

(11630-1419789) to include any of its responses.

Include responses from which message: This message// 1419307 \<Enter\> Local: biweekly info exchange message \# 44

There are 4 responses. Response 0 is the original message. (?? shows index)

Select the responses to include: ??

There are 4 responses. Response 0 is the original message.

Response.....From....................................................Lines

0\) 09/18/00 POSTMASTER 2

1\) 09/18/00 XMUSER1,ONE – COMPUTER SPECIALIST OIREDACTED 4

2\) 09/26/00 XMUSER2,TWO M - PROGRAMMER (OIREDACTED) 2

3\) 09/26/00 XMUSER4,FOUR - Tech Writer (Vista Maintenance Team) 3

4\) 09/26/00 XMUSER23,TWENTY3 - PROGRAMMER (OIREDACTED) 1

There are 4 responses. Response 0 is the original message. (?? shows index)

Select the responses to include:

<span id="_Toc147225836" class="anchor"></span>Figure 4‑42. Using reply and include responses

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/128.png) | TIP: When a message has numerous responses and you want to reference an earlier response, include the text of that response with your reply by choosing the "RI—Reply and Include responses" action code. Previously, you could only point readers to the previous response number you were referencing. Now, the referenced response can be displayed within your own response. The other readers of the message will not have to back up and hunt for that previous response anymore, because you've provided them with the text. |

|                                                   |                                                                                                                                                                                                                                                              |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/129.png) | CAUTION: To avoid excessive overhead, please use the "RI—Reply and Include responses" feature sparingly. Also, when you do quote material, it is generally a good idea to edit the quoted material down to just the specific text to which you are replying. |

To review the recipients of a message before you make a response, use the "Query" action codes.

|                                                                                                                |                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/130.png) | REF: For more information on the "Query" action codes, please refer to Table 4‑1 and the "Query Action" topics previously described in this chapter. |

When you use the caret ("^") to skip reading all replies or inadvertently, MailMan will notify you of the range of unread responses, some of which could influence your own reply:

\>\> You haven't read responses n-n. You may backup to see them. \<\<

<span id="_Toc147225837" class="anchor"></span>Figure 4‑43. Notification that you have not read a range of responses

#### How do you Respond to a Message?

Once you have read a message and are presented with the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), you can reply to the message, as shown below:

Subj: TEST 1 \[#1229870\] 09/16/00@15:20 2 lines

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

3 of 3 responses read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// R

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]===============\< TEST 1 \>==============\[ \<PF1\>H=Help \]====

This is a test reply.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Select Message option: Transmit now// \<Enter\> Sending local reply...

Sent

Enter message action (in TEST basket): IGNORE//

<span id="_Ref427485453" class="anchor"></span>Figure 4‑44. Replying to a message without including previous responses

In the previous example (Figure 4‑44), the user was responding to message number 1229870 (as shown in the Subject line of the message). To initiate the reply, she entered "R" at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan automatically placed the user into the editor to add a response.

The user entered a reply, saved it, and closed the editor.

The user then sent the reply by choosing the "Transmit now" default response at the "Select Message option: Transmit now//" prompt, by pressing the \<Enter\> key.

Finally, MailMan indicated that the response had been sent locally (i.e., "Sending local reply..."). If the user had sent a reply over the network, MailMan would have displayed "Sending network reply..."

Also, if a reply to a message sent from a remote site stayed local, the message reply header would include the words "\<Local Reply\>," as shown below:

Subj: TEST MSSG \[#1409885\] 9 May 2000 12:57:18 -0700 (PDT) 1 line

From: \<XMUSER.ZERO@MAILMAN.CIOREDACTED.VA.GOV\> 1 of 2 responses read.

In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

2\) XMUSER1,ONE - COMPUTER SPECIALIST (Oakland OI Field Office)

08/21/06@14:14 1 line

\<Local Reply\>

Test

Enter message action (in TEST basket): Ignore//

<span id="_Toc147225839" class="anchor"></span>Figure 4‑45. Reply to a message header showing reply sent locally

You can also include the original message and any previous response(s) to a message in your reply. You may wish to do this so you can make a direct reference to the included text in your own reply, as shown below:

Subj: Test Later Delivery for Individual Recipients \[#1226242\]

08/25/98@09:20 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

7 of 7 responses read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// RI

There are 7 responses. Response 0 is the original message. (?? shows index)

Select the responses to include: ??

There are 7 responses. Response 0 is the original message.

Response....From..........................................................Lines

7\) 08/27/98 XMUSER4,FOUR - Q... Continuum 1

6\) 08/26/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 2

5\) 08/26/98 XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland) 12

4\) 08/26/98 XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland) 9

3\) 08/26/98 XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland) 2

2\) 08/26/98 XMUSER2,TWO M. - PROGRAMMER ( OI Field Office Oakland) 1

1\) 08/26/98 XMUSER4,FOUR - Q... Continuum 2

0\) 08/25/98 XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland) 1

There are 7 responses. Response 0 is the original message. (?? shows index)

Select the responses to include: 2

Copying...

You may edit the text of the message...

==\[ WRAP \]==\[ INSERT \]===\< Test Later Delivery for Indivi \>==\[ \<PF1\>H=Help \]====

On 08/26/98@06:47 (Response \#2) XMUSER2,TWO M. wrote:

\>I got your message.

Here is my additional response referencing this response.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Select Message option: Transmit now// \<Enter\> Sending local reply...

Sent

Enter message action (in TEST basket): IGNORE//

<span id="_Ref427486532" class="anchor"></span>Figure 4‑46. Replying to a message—Including one response

In the previous example (Figure 4‑46), the user was responding to message number 1226242 (as shown in the Subject line of the message). She wanted to include a response in the reply so the user chose the Reply and Include responses action by entering an "RI" at the "Enter message action (in TEST basket): IGNORE//" prompt.

After indicating the number of responses, MailMan gives you the opportunity of displaying an index of all responders to a message. By entering two question marks ("??") at the "Select the responses to include:" prompt, MailMan displays a summary list of response information for the message.

|                                                                                                                |                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/131.png) | NOTE: If you choose the "RI—Reply and Include responses" action code and there are not any responses to a message, MailMan will automatically copy the original message and place you in the editor. |

The information displayed for each response included:

- Response number
- Date response was sent
- Responder's name (includes their title and MailMan Institution, if space allows)
- Number of lines in each response

From this list, the user chose response number 2 by entering "2" at the "Select the responses to include:" prompt. MailMan automatically copied response number 2 and placed the user into the editor to add a reply. In this case, the user chose to add a response after the copied text; however, you are free to add the text anywhere you want (e.g., before the copied response, within the copied response, or after the copied response).

After the user entered a reply, she saved it and closed the editor.

The user then sent the reply by accepting the "Transmit now" default response at the "Select Message option: Transmit now//" prompt, by pressing the \<Enter\> key.

Finally, MailMan indicated that the response had been sent locally (i.e., "Sending local reply..."). If the user had sent a reply over the network, MailMan would have displayed "Sending network reply..."

You can also include any combination of previous responses to a message in your reply. You may wish to do this so you can make a direct reference to those responses in your own reply, as shown below:

Subj: Test Later Delivery for Individual Recipients \[#1226242\]

08/25/98@09:20 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

8 of 8 responses read. In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// RI

There are 8 responses. Response 0 is the original message. (?? shows index)

Select the responses to include: 5,2-3,1

Copying...

You may edit the text of the message...

==\[ WRAP \]==\[ INSERT \]===\< Test Later Delivery for Indivi \>==\[ \<PF1\>H=Help \]====

On 08/26/98@06:32 (Response \#1) XMUSER4,FOUR wrote:

\>Do you need to know when/if we received it?

\>Hi! How's things?

Here is my reference to response \#1

On 08/26/98@06:47 (Response \#2) XMUSER2,TWO M. wrote:

\>I got your message.

Here is my reference to response \#2

On 08/26/98@06:48 (Response \#3) XMUSER2,TWO M. wrote:

\>One, have you done a Q and a QD before the messages were delivered to

\>see what they tell you?

Here is my reference to response \#3

On 08/26/98@08:56 (Response \#5) XMUSER1,ONE E. wrote:

\>Two:

\>

\>Yes, thanks!

Here is my reference to response \#5

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Select Message option: Transmit now// \<Enter\> Sending local reply...

Sent

Enter message action (in TEST basket): IGNORE//

<span id="_Ref427544442" class="anchor"></span>Figure 4‑47. Replying to a message—Including multiple responses

In the previous example (Figure 4‑47), the user was, again, responding to message number 1226242 (as shown in the Subject line of the message). This time, the user wanted to include a combination of replies so she could reference them in his own reply. Thus, the user chose the Reply and Include responses action by entering an "RI" at the "Enter message action (in TEST basket): IGNORE//" prompt.

The user decided to include responses: 1, 2 to 3, and 5 in the reply by entering "5,2-3,1" at the "Select the responses to include:" prompt (notice the commas and no spaces between numbers). MailMan automatically copied all four responses and placed the user into the editor to add a reply referencing the copied text of each response.

The user entered a reply, saved it, and closed the editor.

The user then sent the reply by accepting the "Transmit now" default response at the "Select Message option: Transmit now//" prompt by pressing the \<Enter\> key.

Finally, MailMan indicated that the response had been sent locally (i.e., "Sending local reply..."). If the user had sent the reply over the network, MailMan would have displayed "Sending network reply..."

Other Actions at the Transmit Prompt When Replying to a Message

Prior to transmitting your reply, MailMan gives you other opportunities to review, edit, and add responses to your reply or query the message to which you are responding, as shown below:

Subj: TEST \[#100649\] 10/28/99@14:45 1 line

From: XMUSER2,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

TEST

Enter message action (in IN basket): Ignore// r

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]================\< TEST \>===============\[ \<PF1\>H=Help \]====

test

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Select Message option: Transmit now// ?

Enter a code from the list.

B Backup to review message

E Edit reply

I Include previous responses in reply

Q Query

Q xxx Query recipient(s) xxx

QC Query Current

QD Query Detailed

QN Query Network

QNC Query Not Current

QT Query Terminated

T Transmit now

Select Message option: Transmit now//

<span id="_Toc147225842" class="anchor"></span>Figure 4‑48. Other options before sending your reply

For example, if the user wanted to include additional responses in the reply she could use the "I" (Include previous responses in reply), as shown below:

Subj: TEST \[#100188\] 02/06/99@09:38 1 line

From: XMUSER2,TWO 2 of 2 responses read. In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in IN basket): Ignore// r

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]================\< TEST \>===============\[ \<PF1\>H=Help \]====

Here is a reply, since she did not use the "RI" action code, she will have to use

the "I" action code to add a response before this reply is sent.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Select Message option: Transmit now// i

Include responses from which message: This message// \<Enter\>

There are 2 responses. Response 0 is the original message. (?? shows index)

Select the responses to include: ??

There are 2 responses. Response 0 is the original message.

Response....From..........................................................Lines

2\) 04/27/99 XMUSER1,ONE - COMPUTER SPECIALIST (Oakland OI Field Office) 6

1\) 04/27/99 XMUSER1,ONE - COMPUTER SPECIALIST (Oakland OI Field Office) 1

0\) 02/06/99 XMUSER2,TWO - COMPUTER SPECIALIST (Oakland OI Field Office) 1

There are 2 responses. Response 0 is the original message. (?? shows index)

Select the responses to include: 1

Copying...

You may edit the text of the message...

==\[ WRAP \]==\[ INSERT \]================\< TEST \>===============\[ \<PF1\>H=Help \]====

Here is my reply, but I forgot to use the "RI" action code, so I will have

to add responses using the "I" action code before I send this message

reply.

On 04/27/99@08:17 (Response \#1) XMUSER1,ONE wrote:

\>test reply

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Select Message option: Transmit now// \<Enter\> Sending local reply...

Sent

Enter message action (in IN basket): Ignore//

<span id="_Ref106588310" class="anchor"></span>Figure 4‑49. Adding responses to your reply before sending it

As you can see from Figure 4‑49, the user first composed the reply but decided to include a response before sending the reply. Thus, she entered an "I" at the "Select Message option: Transmit now//" prompt.

Since there was more than one response from which to choose, the user entered two question marks ("??") at the "Select the responses to include:" prompt in order to display an index of responses.

After reviewing the list of respondents, the user chose to append response \#1 to the reply by entering "1" after the "Select the responses to include:" prompt. MailMan automatically copied the response and placed the user back into the editor to further edit the reply, if necessary.

Since the edits were now complete, the user saved the reply and closed the editor.

The user then sent the reply by accepting the "Transmit now" default response at the "Select Message option: Transmit now//" prompt by pressing the \<Enter\> key.

Finally, MailMan indicated that the response had been sent locally (i.e., "Sending local reply..."). If the user had sent a reply over the network, MailMan would have displayed "Sending network reply..."

|                                                                                                                |                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/132.png) | REF: For more information on the other reply-related actions (i.e., Backup, Edit, or Query functions), please refer to those specific action code topics previously described in this chapter. |

#### Responding to the Latest Response

Also, if while composing a reply to a message another reply comes in to the same message, you will be prompted with the following text when exiting the editor (prior to sending your reply):

\>\> Response n has arrived - you may backup to see it. \<\<

<span id="_Toc147225844" class="anchor"></span>Figure 4‑50. Notification of unread responses while composing a reply

When you are given the opportunity to back up to see new responses, you can enter a "B" (Backup) at the transmit prompt. The default will be to back up to this new, unseen response, instead of the original message (i.e., response 0). Thus, you can back up and read the latest response(s).

Since you have not transmitted your response yet, you may choose to revise your own reply based on that new response. You simply enter an "E" (Edit) at the Transmit now// prompt, and you are put back into the editor where you can modify your reply based on what you just read.

When your revisions are complete, you can transmit your reply. Previously, this prompt did not appear until *after* you had already sent your reply.

|                                                                                                                |                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/133.png) | REF: For more information on the Backup function, please refer to the "Backup ("B") Action" topic previously described in this chapter. |

#### Replying to a Message—"Reply To" Differs From the "From" Address

MailMan is aware of "Reply-To" addresses in the message header. If the "Reply-To" address differs from the "From" address, MailMan will let you know and ask you to which address your reply should go, as shown below:

Subj: Test Message \[#1227790\]

Fri, 09/04/98@08:54:44 -0700 (PDT) 17 lines

From: "Five J. Xmuser5" \<fjx@xxxxx.com\> In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

This is a test message.

Enter message action (in IN basket): IGNORE// R

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]===\< \[SL\] Admin: discussing Bible v \>==\[ \<PF1\>H=Help \]====

Thanks for sending this. I'm testing a reply.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

Select Message option: Transmit now// \<Enter\> Sending local reply...

Sent

Do you wish to send this reply across the network? No// y\<Enter\> YES

Subject: Re: Test Message// \<Enter\>

Select one of the following:

F 'FROM' "Five J. Xmuser5" \<fjx@xxxxx.com\>

R 'REPLY-TO' Test-l@lists.xxxx.com

This message has a 'reply-to' address which differs from the 'from' address.

Select the address to use: R// ?

Generally, we recommend that you use the 'reply-to' address.

The choice, however, is up to you.

Select F to use the 'from' address; R the 'reply-to'.

Select one of the following:

F 'FROM' "Five J. Xmuser5" \<fjx@xxxxx.com\>

R 'REPLY-TO' Test-l@lists.xxxx.com

This message has a 'reply-to' address which differs from the 'from' address.

Select the address to use: R// \<Enter\> 'REPLY-TO' Test-l@lists.xxxx.com

Addressing the reply to: Test-l@lists.xxxx.com GK.VA.GOV via GK.VA.GOV

Sending... Sent

Enter message action (in IN basket): IGNORE//

<span id="_Ref107126745" class="anchor"></span>Figure 4‑51. Choosing to reply to the "Reply To" address

In the previous figure (Figure 4‑51), the user received a message over the network where the "From" (sender of the message) differed from the "Reply To" of the message. Thus, when the user replied to the message she sent the reply, first, locally as usual.

MailMan then asked the user if she wanted to send the reply over the network. In this case, she did, so she entered "Yes" at the "Do you wish to send this reply across the network? No//" prompt.

After accepting the default subject (i.e., "Re: Test Message"), MailMan informed the user that the "From" and "Reply To" contained different addressees. The user entered a question mark ("?") at the "Select the address to use: R//" prompt in order to get Help on this prompt. For this example, the user decided to accept the default and send the message to the address found in the "Reply To" field (i.e., "Test-l@lists.xxxx.com").

MailMan confirmed the address and sent the message.

|                                                                                                                |                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/134.png) | NOTE: Use the Query Network action code to view network information on a message, including any "Reply To" and "From" information for a message sent over the network. |

|                                                                                                                |                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/135.png) | REF: For more information on the Query Network action code, please refer to the "Query Network ("QN") Action" topic previously described in this chapter. |

#### Completing an Interrupted Reply

Also, if you are in the middle of a replying to a message and are inadvertently logged off the system, MailMan will give you the opportunity to complete your reply when you re-enter MailMan, as shown below:

Select ISC OFFICE MENU OPTIONS Option: 4 \<Enter\> MailMan Menu

You have an unsent response remaining in your buffer.

You may continue to reply or delete the remaining text.

Do you want to delete the unsent response? No// ?

Enter 'Yes' to delete the unsent response.

Enter 'No' to continue with the response.

If in doubt, just press return. You will be able to edit

the response and delete it if you wish.

Do you want to delete the unsent response? No// \<Enter\> NO

<span id="_Ref431187802" class="anchor"></span>Figure 4‑52. MailMan notifies you when you have an unsent response

As you can see from the previous example (Figure 4‑52), before the main MailMan Menu is displayed, MailMan will inform you about any unsent response(s). You can choose to complete the response(s) by answering "No" (default) at the "Do you want to delete the unsent response? No//" prompt or deleting the unsent response by answering "Yes." If you answer "No" MailMan will place you back in the message with the unsent response at the "Select response action: Reply//" prompt. Thus, you can go into your editor and complete your response as usual.

### Save ("S") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Save action code (i.e., "S") to save (move) a message to a different existing mail basket or to a new mail basket you create on the fly.

To save a message to another mail basket, enter an "S" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: test3 \[#1223225\] 08/04/98@08:19 1 line

From: XMUSER4,FOUR - Q... Continuum In 'TEST' basket. Page

----------------------------------------------------------------

test3

Enter message action (in TEST basket): IGNORE// S

Save message into basket: Test Save

Are you adding 'Test Save' as a new BASKET (the 77TH for this MAILBOX)? No// y \<Enter\> (Yes)

Message saved.

<span id="_Ref431183333" class="anchor"></span>Figure 4‑53. Saving a message to a new mail basket

In this example (Figure 4‑53), the user wanted to save (move) a message he just read from one basket to another. Thus, he entered an "S" (Save) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan then asked the user into which basket he wanted to save the message. In this case, he wanted to save the message into the "Test Save" basket. Thus, he entered "Test Save" at the "Save message into basket:" prompt.

Since this mail basket did not already exist in the user's mailbox, MailMan asked the user if he wanted to create it as a new basket. In this case, he did, so he entered "Yes" at the "Are you adding 'Test Save' as a new BASKET (the 77TH for this MAILBOX)? No//" prompt. The user also could have saved the message to an existing mail basket.

MailMan informed the user that the message had been saved.

The following figure demonstrates saving a message to an existing mail basket:

Subj: test \[#1223222\] 08/04/98@08:14 1 line

From: XMUSER4,FOUR - Q... Continuum In 'TEST' basket. Page 1

----------------------------------------------------------------

test

Enter message action (in TEST basket): IGNORE// S

Save message into basket: Test Save

Message saved.

<span id="_Ref431183797" class="anchor"></span>Figure 4‑54. Saving a message to an existing mail basket

In this example (Figure 4‑54), the user, again, wanted to save (move) a message he just read from one basket to another. Thus, he entered an "S" (Save) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan then asked the user into which basket he wanted to save the message. In this case, the user wanted to save the message into the newly created "Test Save" basket (Figure 4‑53). Thus, he entered "Test Save" at the "Save message into basket:" prompt.

Since this mail basket already existed in the user's mailbox, MailMan saved (moved) the message to this basket and informed the user that the message had been saved.

### Terminate ("T") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Terminate action code (i.e., "T") to permanently delete a message by moving it to your "WASTE" mail basket. Terminating a message also stops any subsequent replies to that message from being delivered to you.

Generally, a batch job is run nightly (determined by IRM at your site) to remove messages from your "WASTE" basket, and thus, from your mailbox. You can immediately remove messages from your mailbox by, again, terminating the messages from your "WASTE" basket; however, the message remains in the system until all recipients of the message have deleted it from their mailbox.

Unlike the Delete action code, the Terminate action code will prevent responses to a "terminated" message from being "resurrected" or restored back into your mailbox.

|                                                                                                                |                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/136.png) | REF: For more information on the Delete action code, please refer to the "Delete ("D") Action" topic previously described in this chapter. |

To terminate a message, enter a "T" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: test2 \[#1223223\] 08/04/98@08:18 1 line

From: XMUSER4,FOUR - Q... Continuum In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

test2

Enter message action (in TEST basket): IGNORE// T

You won't see future replies. (In WASTE basket)

<span id="_Ref449434335" class="anchor"></span>Figure 4‑55. Terminating a message

In this example (Figure 4‑55), the user wanted to terminate (delete) a message she just read. Thus, she entered a "T" (Terminate) at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan immediately terminated the message (i.e., moved it to the "WASTE" basket for future removal from the user's mailbox) and informed the user that she would not see any future responses to the message.

If the user wanted to "un-terminate" the message, she could go to the "WASTE" basket and forward the message to another basket in her mailbox. If the message is no longer in the "WASTE" basket, the user could ask another recipient of the message to forward it to her.

|                                                                                                                |                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/137.png) | NOTE: MailMan does not ask you to confirm the terminate request. |

### Vaporize Date Edit ("V") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Vaporize Date Edit action code (i.e., "V") to set a message or group of messages to be deleted from your mailbox at a specific date and time or to modify a Vaporize Date already set. You can move any messages set to vaporize to any of your mail baskets, including the "WASTE" basket, and *not* affect its vaporization date. Vaporize means automatically delete.

Vaporize dates set by you, or by MailMan during message delivery, remain with the message until the message is deleted or until you remove the vaporize date. The vaporize date remains in effect even if the message becomes new.

A message that is scheduled for vaporization, either by you or by MailMan during the IN-BASKET PURGE, will be deleted on the scheduled date without waiting for the scheduled IN BASKET PURGE process. You are free to modify or remove the AUTOMATIC DELETION DATE (i.e., vaporize date) at any time prior to the vaporization date.

Vaporize dates set by MailMan during the IN-BASKET PURGE remain with the message only as long as the message remains dormant or until the message is deleted. As soon as you read the message, save it to another basket, or it becomes new, the vaporize date will be removed.

#### Vaporizing an Individual Message

To set a "vaporize" date for an individual message after reading it, enter a "V" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: September training \[#1223554\] 08/06/98@08:38 17 lines

From: XMUSER4,FOUR - Q... Continuum 21 of 21 responses read.

In 'Infrastructure' basket.

-----------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE// V \<Enter\> Vaporize date edit

AUTOMATIC DELETE DATE: ??

This is the date at which this message will be 'vaporized',

deleted from this mail basket for this user.

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer assumes a date in the FUTURE.

You may omit the precise day, as: JAN, 1957

If only the time is entered, the current date is assumed.

Follow the date with a time, such as JAN 20@10, T@10AM, 10:30, etc.

You may enter a time, such as NOON, MIDNIGHT or NOW.

You may enter NOW+3' (for current date and time Plus 3 minutes

\*Note--the Apostrophe following the number of minutes)

Seconds may be entered as 10:30:30 or 103030AM.

AUTOMATIC DELETE DATE: 10/1/98 \<Enter\> (OCT 01, 1998)

Enter message action (in TEST basket): IGNORE//

<span id="_Ref427629991" class="anchor"></span>Figure 4‑56. Vaporizing a message

In the previous example (Figure 4‑56), the user wanted to delete a message at a specific date and time (vaporize). Thus, he entered a "V" at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan then asked the user to enter the "vaporize" date and time (i.e., AUTOMATIC DELETE DATE). In order to display all of the acceptable VA FileMan date and time formats the user could enter, he entered a question mark ("?") at the "AUTOMATIC DELETE DATE:" prompt.

In this case, the user chose to set a vaporize date of October 1, 1998 by entering "10/1/98" at the "AUTOMATIC DELETE DATE:" prompt. MailMan confirmed that the message was set to vaporize on October 1, 1998. The user can later remove or modify the vaporization date before it gets physically deleted from the user's mailbox.

After "vaporizing" the message, MailMan returned the user to the message action prompt where he could take any additional actions on this message.

|                                                   |                                                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/138.png) | TIP: If you know a message will be obsolete or unnecessary after a period of time (e.g., messages advising you about a temporary event such as: system downtime, building fire alarm test, etc.) set the message to "vaporize" after the prescribed time has passed. That way, you will not be cluttering your mailbox with extraneous mail. |

#### Removing a Vaporization date

If you previously set a vaporization date for a message and now want to keep the message, you simply delete the vaporization date, as shown below:

Subj: September training \[#1223554\] 08/06/98@08:38 17 lines

From: XMUSER4,FOUR - Q... Continuum 21 of 21 responses read.

In 'Infrastructure' basket.

Automatic Deletion Date: Oct 1, 1998 Page 1

-------------------------------------------------------------------------------

Enter message action (in Infrastructure basket): IGNORE// V

AUTOMATIC DELETE DATE: OCT 1,1998// @

SURE YOU WANT TO DELETE? y\<Enter\> (Yes)

Enter message action (in Infrastructure basket): IGNORE//

<span id="_Ref427550873" class="anchor"></span>Figure 4‑57. Deleting the vaporization date

In this example (Figure 4‑57), the user wanted to remove (delete) a vaporization date she previously set (Figure 4‑56). Thus, the user opened the message that had a vaporization date set (i.e., AUTOMATIC DELETION DATE) and entered a "V" at the "Enter message action (in Infrastructure basket): IGNORE//" prompt.

Since this message had a vaporization date set, MailMan displayed the current vaporization date as the default (i.e., "OCT 1,1998") and prompted the user to make any changes to the vaporization date.

To delete the Vaporization Date, the user simply entered an at-sign ("@") after the AUTOMATIC DELETE DATE: OCT 1,1998//" prompt.

MailMan asked the user to confirm the delete request. She confirmed the delete by entering "Yes" at the "SURE YOU WANT TO DELETE?" prompt.

When the user went back in to read that message (Figure 4‑58), she saw that the "Automatic Deletion Date" was no longer indicated in the message header (compare to Figure 4‑57), as shown below:

Subj: September training \[#1223554\] 08/06/98@08:38 17 lines

From: XMUSER4,FOUR - Q... Continuum 21 of 21 responses read.

In 'Infrastructure' basket. Page 1

-----------------------------------------------------------------------------------

Enter message action (in Infrastructure basket): IGNORE//

<span id="_Ref427633869" class="anchor"></span>Figure 4‑58. Verifying a message is no longer set to vaporize

### Write ("W") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), you can use the Write action code (i.e., "W") to "write" (compose) a new message while reading a message. The steps of creating a message using the Write action code are the same as if you used the Send a Message option \[XMSEND; synonym SML\].

|                                                                                                                |                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/139.png) | REF: For more information on creating and sending a message or the Send a Message option \[XMSEND\], please refer Chapter 5, "Sending Mail," in this manual. |

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/140.png) | TIP: Use the Write action code ("W") to immediately send a message while reading another message. For example, if after reading a message, you suddenly remember that you need to send a message about an unrelated matter to somebody else. Rather than having to go through the Send a Message option \[XMSEND; synonym SML\], you could simply enter the Write action code. After composing and sending your message, MailMan will automatically return you to the original message where you can continue with your reading. |

To write and send a new message while reading another message, enter a "W" at the "Enter message action (in xxxx basket): IGNORE//" prompt (where "xxxx" contains the name of the actual mail basket in which the message resides), as shown below:

Subj: test \[#1223222\] 08/04/98@08:14 1 line

From: XMUSER4,FOUR - Q... Continuum In 'TEST' basket. Page 1

--------------------------------------------------------

test

Enter message action (in TEST basket): IGNORE// W

Subject: Write Test

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]=============\< Write Test \>============\[ \<PF1\>H=Help \]====

This is a new message created while reading another message. Just by

entering the Write command at the disposition prompt, I can type a new

message.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=======T

Send mail to: XMUSER1,ONE E.// \<Enter\>

Select basket to send to: IN// \<Enter\>

And Send to: \<Enter\>

Select Message option: Transmit now// \<Enter\> Sending \[1224329\]...

Sent

Finished with the 'Write' command.

Now back to:

Subj: test \[#1223222\] 08/04/98@08:14 1 line

From: XMUSER4,FOUR - Q... Continuum In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Enter message action (in TEST basket): IGNORE//

<span id="_Ref449434380" class="anchor"></span>Figure 4‑59. Writing a new message

In the previous example (Figure 4‑59), the user finished reading a message and wanted to send a new message without having to go through the Send a Message option. Thus, he entered a "W" at the "Enter message action (in TEST basket): IGNORE//" prompt.

MailMan then asked the user to enter the subject for the new message. For this example, he entered "Write Test" at the "Subject:" prompt.

MailMan then immediately placed the user into the editor where he could enter the text of the message. When the user had completed the entry, he saved the text and closed the editor.

MailMan then asked the user to address the message. In this case, he wanted to just send the message to himself so he pressed the \<Enter\> key at the "Send mail to: XMUSER1,ONE E.//" prompt.

The user accepted the default basket (i.e., "IN") by pressing the \<Enter\> key at the "Select basket to send to: IN//" prompt.

MailMan knew the user was done addressing the message when he pressed the \<Enter\> key at the "And Send to:" prompt without entering a name.

The user immediately sent the message by, again, pressing the \<Enter\> key at the "Select Message option: Transmit now//" prompt.

Finally, MailMan displayed the internal message identification number (in brackets) and indicated that the message had been sent.

After writing and sending the new message, MailMan notified the user the "Write" was completed (i.e., "Finished with the 'Write' command."), redisplayed the original message header, and returned the user to the original message action prompt where he could take any additional actions on this message.

### Extract KIDS or PackMan Messages ("X") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Programmers use PackMan and KIDS messages to store and transport data, packages, and routines via MailMan messages. It may not be used unless the proper key is held (i.e., XUPROGMODE security key).

As you can see from the list of message action codes (Table 4‑1), you can use the Extract KIDS or PackMan Messages Toggle action code (i.e., "X") when reading a KIDS or PackMan message to choose from a list of specific functions you can perform on these types of messages.

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/141.png) | REF: For more information on KIDS and PackMan messages, please refer to the "KIDS" section in the *Kernel Systems Manual*. |

### Caret ("^") Exit Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of message action codes (Table 4‑1), as with all VistA software, you can use the caret ("^") to exit a prompt or option without taking any other action, as shown below:

Select MailMan Menu Option: rml \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (5 messages, 2 new)

IN Basket, 5 messages (1-5), 2 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*5. \[1361007\] 04/19/99 Local: biweekly info exchange 2 XMUSER39,THIRTY9 1/5

!4. \[1360433\] 04/14/99 New Phone System Training 12 XMUSER38,THIRTY8 28/28

3\. \[1354489\] 02/25/99 CIO News - February 25, 1999 85 \<XMUSER36.THIRTY6@FORUM

2\. \[1354488\] 02/24/99 Minutes - Nat'l IRM Call - 496 \<XMUSER37.THIRTY7@FORUM

1\. \[1350198\] 02/01/99 FM22 account 6 XMUSER4,FOUR

Enter message number or command: 4

Subj: New Phone System Training \[#1360433\] 04/14/99@15:25 12 lines

From: XMUSER38,THIRTY8 - ADMIN OFFICER 28 of 28 responses read. In 'IN' basket.

Page 1 \*New\*

-------------------------------------------------------------------------------

Enter message action (in IN basket): IGNORE// ^

IN Basket, 5 messages (1-5), 1 new

\*=New/!=Priority........Subject....................Lines.From..........Read/Rcvd

\*5. \[1361007\] 04/19/99 Local: biweekly info exchange 2 XMUSER39,THIRTY9 1/5

4\. \[1360433\] 04/14/99 New Phone System Training 12 XMUSER38,THIRTY8 28/28

3\. \[1354489\] 02/25/99 CIO News - February 25, 1999 85 \<XMUSER36.THIRTY6@FORUM

2\. \[1354488\] 02/24/99 Minutes - Nat'l IRM Call - 496 \<XMUSER37.THIRTY7@FORUM

1\. \[1350198\] 02/01/99 FM22 account 6 XMUSER4,FOUR

Enter message number or command:

<span id="_Toc147225854" class="anchor"></span>Figure 4‑60. Example using the caret to exit a message

# Sending Mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics to be discussed in this chapter:

- SML—Send a Message Option
- Message Subjects
- Address Functionality
- Delivery Options—Immediate, Deferred, and/or Staggered
- Later ("L:xxx") Prefix Code
- Completing an Interrupted Message
- Sending Mail Using the P-MESSAGE Device
- Action Codes—Sending Messages
- Backup ("B") Action
- Confidential ("C") Action (Toggle)
- Delivery Basket Set ("D") Action
- Edit Recipients ("ER") Action
- Edit Subject ("ES") Action
- Edit Text ("ET") Action
- Information Only ("I") Action (Toggle)
- Transmit Later ("L") Action
- Network Signature ("NS") Action
- Priority Delivery ("P") Action (Toggle)
- Confirm Receipt ("R") Action (Toggle)
- Scramble ("S") Action
- Transmit Now ("T") Action
- Vaporize Date Set ("V") Action
- Closed Message ("X") Action (Toggle)
- Canceling a Message ("^")

Sending messages gives you the opportunity to obtain or disseminate information.

The features and functionality associated with sending messages are described in greater detail in this chapter.

### SML—Send a Message Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to replying to an existing message, you can use the Send a Message option \[XMSEND; synonym SML\] to send a new message to any number of recipients or mail groups.

The Send a Message option is the option you use when you wish to send new messages to any number of recipients. It is available on the MailMan Menu, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message \[XMSEND\]

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: SML \<Enter\> Send a Message

<span id="_Toc436461088" class="anchor"></span>Figure 5‑1. SML—Send a Message option

Once you select the Send a Message option, MailMan allows you to send new mail in four easy steps:

> 1\. Enter the subject of your message.

> 2\. Compose your message (i.e., enter the text of your message).

> 3\. Address your message (e.g., send it to individual recipients or a mail group).

> 4\. Send your message. You can further customize your message before sending it using various action codes (e.g., make it: priority, closed, confidential, information only, etc.).

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/142.png) | REF: For a complete list of message action codes when sending a message, please refer to Table 5‑1 that follows in this chapter. |

After you choose the Send a Message option \[XMSEND; synonym SML\], MailMan prompts you to enter the subject of the new message and then automatically places you in the editor to compose your new message, as shown below:

Select MailMan Menu Option: SML \<Enter\> Send a Message

Subject: Sending a Message

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]==========\< Sending a Message \>======

Here I am composing a message to send to several recipients

as a test.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

Send mail to: XMUSER1,ONE E.// \<Enter\>

Select basket to send to: IN// \<Enter\>

And Send to: 9999 \<Enter\> XMUSER2,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 09/02/98@12:28

If wishes were horses, beggars would ride.

...OK? Yes// \<Enter\> (Yes)

And Send to: xmuser3 \<Enter\> ,THREE VERIFICATION

Last used MailMan: 08/13/98@11:26

And Send to: xmuser4 \<Enter\> ,FOUR INFORMATION SYSTEMS CENTER

Last used MailMan: 08/13/98@14:22

And Send to: \<Enter\>

Select Message option: Transmit now// ?

Enter a code from the list.

Select one of the following:

B Backup to review message

C Confidential (surrogate can't read)

D Delivery basket set

ER Edit Recipients

ES Edit Subject

ET Edit Text

I Information only (recipients may not reply)

IM Include responses from another Message

L Transmit Later

NS Add Network Signature

P Priority delivery

R Confirm Receipt

S Scramble text with password

T Transmit now

V Vaporize date set

X Close (no forward allowed)

Select Message option: Transmit now//

<span id="_Hlt427984529" class="anchor"></span>Figure 5‑2. Message send options

As you can see from the previous example (Figure 5‑2), after the user chose the Send a Message option (SML), MailMan prompted the user to enter the message subject (i.e., "Sending a Message").

|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/143.png) | REF: For more information on message subjects, please refer to the "Message Subjects" topic that follows in this chapter. |

After entering the subject, MailMan automatically placed the user into the editor to compose the message. After typing in the text of the message, the user saved the text, and closed the editor.

MailMan next asked the user to address the message. As a default, MailMan will always let you send a message to yourself by automatically placing your name as the default response after the first "Send mail to:" prompt. As an addressee, you can query the message to see if or when the other recipients opened the message you sent. Whether you initially make yourself an addressee or not, you will receive all replies to the message.

|                                                                                                                |                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/144.png) | REF: For more information on querying a message, please refer to the "Query Action" code topics in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

Depending on how you've set the ASK BASKET field in your User Options Edit option, MailMan may then ask you to choose the mail basket in your mailbox to send your copy of the message. If you initially set your "ASK BASKET field to "No", MailMan will *not* prompt you to choose a mail basket. In this case, the ASK BASKET field is set to ask the user to choose the mail basket. The user accepted the default response (i.e., "IN" basket) by pressing the \<Enter\> key at the "Select basket to send to: IN//" prompt.

|                                                                                                                |                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/145.png) | REF: For more information on the "ASK BASKET" field or the User Options Edit option, please refer to the "Set Your Mail Basket Prompt" topic in Chapter 3 in the *MailMan Getting Started Guide*. |

MailMan then prompted the user to choose any other recipients for the message (address information). The user chose to send the message to three other people beside himself:

- XMUSER2,TWO M.
- XMUSER3,THREE
- XMUSER4,FOUR

The user addressed the message by entering each recipient's name at the "And Send to:" prompt.

|                                                                                                                |                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/146.png) | REF: For more information on addressing a message, please refer to the "Address Functionality" topic that follows in this chapter. |

MailMan knew the user had completed the addressing when he pressed the \<Enter\> key without entering another name at the "And Send to:" prompt.

Finally, MailMan presented the user with the "Select Message option: Transmit now//" prompt. At this prompt, MailMan allows you to further edit your message and include any delivery options prior to sending (transmitting) your message (e.g., make the message: priority, closed, confidential, information only, etc.). The default response was to simply "Transmit now" (send) the message. By entering a question mark ("?") at this prompt, MailMan presented the user with a list of additional action codes, which are described in greater detail on the following pages.

### Message Subjects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The subject of the message is shown whenever the message is displayed. It can be from 3 to 65 characters in length. The message subject cannot be blank. MailMan automatically deletes any leading and trailing blanks. Also, MailMan reduces any sequence of three or more blanks to two blanks.

If a user enters a blank or null subject, MailMan defaults the subject to "\* No Subject \*". When a message whose subject is "\* No Subject \*" is sent to a remote site, the subject transmitted (in the header record) is null. This is useful for sending a message to a list server (to join or drop a list, etc.) whose subject must be blank and whose text must contain the command to the list server.

### Address Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Entering User or Group Names

When entering a user or mail group name, MailMan only requires that you enter the first portion of the last name (user names are *not* case sensitive); MailMan will find the appropriate person or group based on your partial entry and automatically display the rest of the name to you. If more than one person or group is found based on your partial entry, MailMan will allow you to choose from a list; however, you can narrow your choices by entering more characters of the name.

#### Addressing Recipients Using Their DUZ

In addition to entering a user's name, MailMan also allows you to enter a person's local DUZ when performing the following functions:

- Addressing a message (including forwarding messages)
- Becoming a surrogate
- Filtering mail by sender and/or recipient
- Searching for messages by sender, recipient, and/or responder

The DUZ is a person's unique numeric user ID. Thus, if multiple addressees, for example, have similar names, you can enter their local DUZ instead of their name to choose the specific person.

|                                                                                                                |                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/147.png) | NOTE: You *cannot* substitute the DUZ for a name when creating members of a personal mail group or when creating a surrogate for yourself. |

MailMan can display a user's DUZ when doing any of the following:

- Addressing messages.
- Displaying user information with the User Information option available on the Help (User/Group Info., etc.) menu.

IRM controls whether or not a user's DUZ is displayed through the SHOW DUZ WHEN ADDRESS MESSAGE field (#7.3) in the MAILMAN SITE PARAMETERS file (#4.3).

|                                                                                                                |                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/148.png) | REF: For more information on the SHOW DUZ WHEN ADDRESS MESSAGE field (#7.3), please refer to the "Management Features in MailMan" topic in the "Implementation and Maintenance" section of the *MailMan Technical Manual*. |

#### Addressing Mail to Mail Groups

Mail groups can be classified as "large" (site-specified) and processed differently from "small-" to "medium-sized" mail groups. A mail group may be considered "large" when it has a large number of local and remote members, member groups, or distribution lists (nationwide mail groups). IRM sets the number used to indicate when a mail group is considered "large" (i.e., BIG GROUP SIZE field (#7.2) in the MAILMAN SITE PARAMETERS file (#4.3)).

|                                                                                                                |                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/149.png) | REF: For more information on the BIG GROUP SIZE field (#7.2), please refer to the "Management Features in MailMan" topic in the "Implementation and Maintenance" section of the *MailMan Technical Manual*. |

Now, if you address a message to a "large" mail group, MailMan gives you the opportunity to queue ("Later") the message for delivery to that group at a later date and time (background processing). Previously, MailMan did *not* give you this option and added every member to the recipient list in the foreground while you waited. MailMan would display a series of dots while processing those recipients. Depending on the size of the recipient list, this could take some time and prevented you from taking any other actions.

Addressing a message to a "small-" or "medium-sized" mail group is processed in the foreground as usual. Also, if you choose to "Later" a message to a "large" mail group, you will *not* be able to remove (minus) members from the group before sending the message. Thus, if you need to selectively remove (minus) members from the group, you should *not* "later" the delivery of the message to that group.

If the total number of members in a mail group is equal to or greater than the value in the BIG GROUP SIZE field, the mail group is considered to be a "large" mail group and treated accordingly. Conversely, if the total number of members in a mail group is less than this number, they will be treated as "small-" to "medium-sized" mail groups and processed in the foreground as usual.

The following examples illustrate addressing a message to a "small-" or "medium-sized" mail group and to a "large" mail group. For both examples, let's assume that IRM set the BIG GROUP SIZE field to 100. Thus, any mail group whose total number of members is equal to or greater than 100 will be considered a "large" mail group, otherwise it is considered to be a "small-" to "medium-sized" group. Also, for both examples, we will only show how the user addressed the message.

|                                                                                                                |                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/150.png) | NOTE: A mail group is also considered "large" if it contains another mail group or a distribution list. |

For the first example, the user addressed a message to a "small-" to "medium-sized" mail group, as shown below:

.

.

.

And Send to: g.isc \<Enter\> - SAN FRANCISCO BASED

44 Local:

XMUSER7,SEVEN XMUSER8,EIGHT XMUSER9.NINE Y., JR. XMUSER100,ONE-HUNDRED

XMUSER10,TEN XMUSER11,ELEVEN XMUSER12,TWELVE XMUSER13,THIRTEEN

XMUSER14,FOURTEEN K XMUSER15,FIFTEEN XMUSER16,SIXTEEN XMUSER17,SEVENTEEN

XMUSER18,EIGHTTEEN XMUSER19,NINETEEN XMUSER1,ONE E. XMUSER2,TWO M.

Do you want to see more members? No// \<Enter\> NO

And Send to: g.isc satellite

9 Local:

XMUSER20,TWENTY XMUSER21,TWENTY1 XMUSER22,TWENTY2 XMUSER14,FOURTEEN K

XMUSER17,SEVENTEEN XMUSER23,TWENTY3 XMUSER24,TWENTY4 XMUSER25,TWENTY5

XMUSER26,TWENTY6

And Send to: -xmuser7 \<Enter\> ,SEVEN DEVELOPMENT

Last used MailMan: 09/16/98@12:51

Messaging Developer Deleted.

And Send to: -g.isc satellite \<Enter\> Deleting Members ...

9 Local:

XMUSER20,TWENTY XMUSER21,TWENTY1 XMUSER22,TWENTY2 XMUSER14,FOURTEEN K

XMUSER17,SEVENTEEN XMUSER23,TWENTY3 XMUSER24,TWENTY4 XMUSER25,TWENTY5

XMUSER26,TWENTY6

Members Deleted..

.

.

.

<span id="_Ref429444419" class="anchor"></span>Figure 5‑3. Addressing mail to a "small-" or "medium-sized" mail group

In this example (Figure 5‑3), the user addressed the message to two groups:

- G.ISC - SAN FRANCISCO BASED
- G.ISC SATELLITE

At the first "And Send to:" prompt the user entered the first portion of the "G.ISC - SAN FRANCISCO BASED" mail group name.

MailMan indicated that this group consisted of 44 local members and then displayed the first 16 members of the group. Since the total number of members in this group did not exceed the site's BIG GROUP SIZE (i.e., not a "large" group, 40 \< 100), MailMan did *not* ask the user if she wanted to "Later" the message to the group; however, MailMan did give the user the option to list more of the members of the group. In this case, she did *not* want to see any more members in the list so she accepted the "No" default response by pressing the \<Enter\> key at the "Do you want to see more members? No//" prompt. If the user had answered "Yes," MailMan would have displayed the next block of names and, again, given the user the choice of continuing the list until all members of the group were listed or she answered "No" to displaying any more members.

At the next "And Send to:" prompt, the user entered the first portion of the "G.ISC SATELLITE" mail group name.

MailMan indicated that this group consisted of 9 local members and then displayed all nine members of the group. Since the total number of members in this group did not exceed the site's BIG GROUP SIZE (i.e., not a "large" group, 9 \< 100), MailMan did *not* ask the user if she wanted to "Later" the message to the group.

After entering the groups, the user decided to "minus" a member from the "G.ISC - SAN FRANCISCO BASED" group before sending the message. In this case, she entered "-XMUSER7,SEVEN" at the "And Send to:" prompt. MailMan confirmed that the member was "deleted" from the recipient list.

The user then decided to "minus" the entire second group (i.e., "G.ISC SATELLITE") by entering "-G.ISC SATELLITE" at the "And Send to:" prompt. MailMan confirmed that all the members in the mail group were "deleted" from the recipient list.

For the second example (shown in two parts), the user addressed a message to a "large" mail group, as shown below:

.

.

.

Send mail to: XMUSER1,ONE E.// \<Enter\>

Select basket to send to: IN// \<Enter\>

And Send to: g.fileman support

This group seems to be fairly big.

If you don't need to 'minus' anyone from it,

then you can save some time by queuing this group for 'Later' delivery.

Would you like to queue this group for later delivery? NO// ?

Answer NO if

\- You need to delete any group members from the message.

Answer YES if

\- You don't need to delete any group members from the message.

\- and you'd like to save a bit of time.

Would you like to queue this group for later delivery? NO// y \<Enter\> YES

Later Delivery must be at least 5 minutes from now.

When Later: (9/14/98 - 10/14/98): 09/14/98@15:34// \<Enter\> (SEP 14, 1998@15:34)

\>\> Remember, you won't be able to 'minus' anyone from the group. \<\<

3 Local, 1 Member Group(s):

XMUSER11,ELEVEN XMUSER31,THIRTY1 XMUSER32,THIRTY2

9 Local:

XMUSER11,ELEVEN XMUSER14,FOURTEEN K. XMUSER28,TWENTY8 XMUSER15,FIFTEEN

XMUSER16,SIXTEEN XMUSER30,THIRTY XMUSER27,TWENTY7 XMUSER29,TWENTY9

XMUSER23,TWENTY3

And Send to:

<span id="_Ref430596456" class="anchor"></span>Figure 5‑4. Latering delivery of a message to a "large" mail group

In Part 1 of addressing a message to a "large" mail group (Figure 5‑4), the user wanted to send the message to a mail group (i.e., "G.FILEMAN SUPPORT") as well as individual recipients. As the first addressee, she entered the first portion of the "G.FILEMAN SUPPORT" group name at the "And Send to:" prompt.

MailMan indicated that this was a "large" group. Although the total number of members did not exceed the site's BIG GROUP SIZE (i.e., 100), this group does have a member group and that is enough to have it considered as a "large" group. Because this was a "large" mail group, MailMan gave the user the option of "latering" the message to the mail group.

The user decided to display the online help by entering a question mark ("?") at the "Would you like to queue this group for later delivery? NO//" prompt. MailMan explained the options when "latering" the message to a group.

After reviewing the choices, knowing that she did not want to "minus" anyone from the group, she decided to "later" the message to the group by entering "Yes" at the "Would you like to queue this group for later delivery? NO//" prompt.

MailMan then asked the user to set the date and time to deliver the message to this group. For this example, the user chose the default (five minutes in the future) by pressing the \<Enter\> key at the "When Later: (9/14/98 - 10/14/98): 09/14/98@15:34//" prompt.

MailMan displayed the future delivery date (i.e., "SEP 14, 1998@15:34") and reaffirmed the fact that the user would not be able to "minus" anyone from the mail group. MailMan also listed the all members in the mail group.

MailMan then proceeded to prompt the user for any additional addressees.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/151.png) | REF: For more information on "latering" a message, please refer to the "Later ("L:xxx") Prefix Code" or "Transmit Later ("L") Action" topics that follow in this chapter. |

The next figure (Figure 5‑5) continues with this example:

And Send to: xmuser2 \<Enter\> ,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 09/17/98@07:43

If wishes were horses, beggars would ride.

And Send to: xmuser3 \<Enter\> ,THREE VERIFICATION

Last used MailMan: 09/16/98@16:09

And Send to: ??

Select one of the following:

U User information

G Mail Group information

D Domain information

R Remote user information

S Show current recipients of this message

M More help

Enter the kind of help you'd like: s\<Enter\> Show current recipients of this message

Current recipients are:

XMUSER2,TWO M.

XMUSER1,ONE E.

G.FILEMAN SUPPORT Deliver: 09/14/98@16:26

XMUSER3,THREE

Like more detail? YES// n \<Enter\> NO

Select one of the following:

U User information

G Mail Group information

D Domain information

R Remote user information

S Show current recipients of this message

M More help

Enter the kind of help you'd like: \<Enter\>

And Send to: -XMUSER3,THREE \<Enter\> VERIFICATION

Last used MailMan: 09/14/98@16:09

Deleted.

But message will still go to all members of the following later'd group(s):

G.FILEMAN SUPPORT

And Send to:

.

.

.

<span id="_Ref430597928" class="anchor"></span>Figure 5‑5. Verifying recipients of a message

In Part 2 of this example (Figure 5‑5), the user wanted to send the message to some additional recipients:

- XMUSER2,TWO M.
- XMUSER3,THREE

As with entering any local MailMan user's name, the user only had to enter the first portion of each person's last name (*not* case sensitive) or their local DUZs (i.e., numeric user ID) at the "And Send to:" prompt.

The user then entered two question marks ("??") at the next "And Send to:" prompt in order to display the online Help. MailMan gave the user several help options from which to choose. For this example, the user wanted to confirm the recipients for the message by entering an "S" (Show current recipients of this message) at the "Enter the kind of help you'd like:" prompt.

MailMan listed the current recipients:

- XMUSER2,TWO M.
- XMUSER1,ONE E.
- G.FILEMAN SUPPORT Deliver: 09/1498@16:26)
- XMUSER3,THREE

You'll notice that MailMan displayed the "later" delivery date for the G.FILEMAN SUPPORT mail group (i.e., Deliver: 09/1498@16:26) that the user previously set (Figure 5‑4). The user pressed the \<Enter\> key at the "Enter the kind of help you'd like:" prompt.

Though you cannot "minus" a member from the "latered" mail group, the user was able to "minus" one of the other recipients before sending the message. In this case, she entered "-XMUSER3,THREE" at the "And Send to:" prompt.

MailMan confirmed that the member was "deleted" from the recipient list. MailMan also reiterated that the message would still be delivered to *all* members of the G.FILEMAN SUPPORT mail group.

#### Addressee Unknown

If you send a message locally, MailMan will only allow you to enter or choose a valid user as a recipient. A valid user must have an Access code and a mailbox, as shown below:

Subj: Test \[#1236951\] 10/22/98@10:30 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'TEST' basket. Page 1

-------------------------------------------------------------------------------

Test!

Enter message action (in TEST basket): IGNORE// f

Forward mail to: xmuser42

If XMUSER42,FORTY2 is the person you're trying to address, you can't,

because XMUSER42,FORTY2 doesn't have an access code.

Message addressees must have an access code and a mailbox.

Checking for MAIL NAME: XMUSER42

Not a local user; checking Remote User Directory: XMUSER42 Not found.

Forward mail to:

<span id="_Toc436461093" class="anchor"></span>Figure 5‑6. Notification of an unknown addressee (1)

When addressing a message, if an addressee is not found in the local user file, MailMan asks, "Do you want to check the REMOTE USER DIRECTORY? No//." Also, if MailMan checks it and finds an entry, MailMan asks, "OK?" instead of simply selecting it. This will prevent unwanted addressees, because the REMOTE USER DIRECTORY entry might not be the addressee the sender wants.

Send mail to: XMUSER4,FOUR// \<Enter\> XMUSER4,FOUR

Select basket to send to: IN// \<Enter\>

And Send to: xmuser41,forty1\<Enter\> Not found in NEW PERSON file.

Checking for MAIL NAME: XMUSER41,FORTY1

Not a local user; want to check the Remote User Directory? No// y \<Enter\> YES

Checking Remote User Directory: XMUSER41,FORTY1 XMUSER41,FORTY1@KERNEL.REDACTED.VA.GOV XMUSER41,FORTY1

...OK? Yes// \<Enter\> (Yes)

Routing to Remote Address: XMUSER41,FORTY1@KERNEL.REDACTED.VA.GOV

And Send to:

<span id="_Toc147225861" class="anchor"></span>Figure 5‑7. Checking Remote User Directory for addressee unknown locally

Also, if you send a message to a remote recipient (e.g., someone on FORUM), MailMan cannot verify the remote user's name while you are addressing the message. If the user cannot be found on the remote system (e.g., invalid entry), MailMan will notify you with a message that your mail to that unknown addressee could not be delivered, as shown below:

Subj: Message not delivered to recipient \[#1227769\] 09/04/98@09:02

7 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

------------------------------------------------------

Your message \[#1227766\]

SUBJECT: Sending a Message to an Invalid Remote User

was not delivered to xxxxxx@FORUM.VA.GOV.

The error message was:

Recipient not found

\<XXXXXX@FORUM.VA.GOV\>

Enter message action (in IN basket): IGNORE//

<span id="_Toc436461094" class="anchor"></span>Figure 5‑8. Notification of an unknown addressee (2)

#### Recipient Prefix Codes

MailMan also allows you to further customize how you send a message to individual recipients by using a variety of prefix codes. To display the list of prefix options, enter a question mark ("?") at the "And Send to:" prompt, as shown below:

.

.

.

And Send to: ?

Enter the name(s) of the recipient(s) of this message

in any of the following formats:

Lastname,first for a user at this site

Lastname,first@REMOTE-SITE for a user at another site

(note: DUZ may be used instead of Lastname,first)

G.\<group-name\> for a group of users

D.\<device-name\> for a device

\* for a limited broadcast or broadcast to all users

(must be Postmaster or XMSTAR key holder)

Prefix any user address with 'I:' to send Information only.

'C:' to send Carbon copy.

'L:' to send Later.

'-' to delete it.

Enter:

G.? for a list of groups

D.? for a list of devices

Enter '??' for detailed help.

<span id="_Toc436461095" class="anchor"></span>Figure 5‑9. Recipient prefix codes

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/152.png) | REF: For more information on "latering" a message, please refer to the "Later ("L:xxx") Prefix Code" or "Transmit Later ("L") Action" topics that follow in this chapter. |

Each of the prefix options are briefly described below:

- Information Only—Send the message to an individual recipient as Information Only (i.e., "I:xxx," where "xxx" represents the recipient's name). Thus, the individual specified cannot reply to the message. Other recipients on the message, however, can still reply.

|                                                                                                                |                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/153.png) | NOTE: Please note that designating a recipient as "Information Only" is a MailMan-specific capability that is not recognized by other non-MailMan systems. Therefore, any "I:xxx" designation is ignored when sending a message to a non-MailMan system (e.g., Microsoft Exchange or Outlook). |

|                                                                                                                |                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/154.png) | REF: For more information on sending a message Information Only, please refer to the "Information Only ("IN") Action (Toggle)" topic that follows in this chapter. |

- Carbon Copy—Send a carbon copy of the message to a recipient (i.e., "C:xxx," where "xxx" represents the recipient's name).

|                                                                                                                |                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/155.png) | NOTE: This feature serves no other function than to highlight a recipient as receiving a carbon copy. The carbon copy recipient has the same capabilities as any other recipient to the message. |

> When doing a query on a message where a recipient was designated to receive a carbon copy, a "cc:" will precede their name, as shown below:

Subj: Carbon Copy Test \[#1226302\] 08/25/98@14:47 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (San Francisco ISC)

2 of 2 responses read. In 'TEST' basket. Page 1

--------------------------------------------------------

Enter message action (in TEST basket): IGNORE// qd

Subj: Carbon Copy Test \[#1226302\] 08/25/98@14:47 1 li

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (San Francisco ISC)

2 of 2 responses read. In 'TEST' basket.

Local Message-ID: 1226302@REDACTED.VA.GOV (3 Recipients)

cc: XMUSER3,THREE Last read: 08/25/98@14:50 (2 of 2 responses)

\[First read: 08/25/98@14:48\]

XMUSER2,TWO M. Not read.

XMUSER1,ONE E. Last read: 08/25/98@14:49 (2 of 2 responses)

\[First read: 08/25/98@14:47\]

<span id="_Toc436461096" class="anchor"></span>Figure 5‑10. Example showing a recipient received a carbon copy of the message

- Staggered Delivery—Send the message to a recipient at a future date and time (i.e., "L:xxx," where "xxx" represents the recipient's name).

|                                                                                                                |                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/156.png) | REF: For more information on the Later prefix code, please refer to the "Later ("L:xxx") Prefix Code" topic that follows in this chapter. |

- Remove Recipient—Remove (minus) a recipient from your list of recipients on a message before sending it (i.e., "-xxx," where "xxx" represents the recipient's name to be removed)

|                                                                                                                |                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/157.png) | REF: For an example using this prefix, please refer to the "Edit Recipients ("ER") Action" topic and Figure 5‑28 that follows in this chapter. |

#### Broadcast Messages

Broadcast messages are messages sent to *all* local users or a *subset* of local users on MailMan. These messages are used to inform (notify) users of general events that affect or involve all or select local users on MailMan. For example:

- System Messages (e.g., system shutdown notices, new hardware and software installs).
- Personnel Announcements (e.g., new policies and procedures, open season for health/life insurance changes, holiday and leave information).
- General Public Announcements (e.g., VA Secretary's daily message, VA-wide conference information)
- Site-specific Announcements (e.g., building alerts, local training sessions and seminars)

Users authorized to send Broadcast messages to *all* local MailMan users include:

- The Postmaster.
- Any holder of the XMSTAR security key.

Broadcast messages sent to all MailMan local users (including SHARED,MAIL) are automatically sent as "Information Only" (i.e., prevents all recipients from replying to the message).

In addition to Broadcast messages to *all* local users (including SHARED,MAIL), MailMan allows an authorized user to send "Limited" Broadcast messages to a *subset* of local users. A subset of local users might include all users who have a certain primary menu, users who belong to a certain division, users who hold a specific security key, or any other way that users in the NEW PERSON file (#200) might be categorized and specified by a site's IRM.

|                                                                                                                |                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/158.png) | REF: For more information on the broadcast categories, please refer to the "Broadcast Messages to a Subset of Users—LIMITED BROADCAST Multiple Field" topic in the "Managing MailMan" section in the *MailMan Technical Manual*. |

Users authorized to send Limited Broadcast messages to a *subset* of local MailMan users include:

- The Postmaster.
- Any holder of the XMSTAR security key.
- Any holder of the XMSTAR LIMITED security key.

Unlike Broadcast messages, Local Broadcast messages are *not* automatically "Information Only" (i.e., prevents all recipients from replying to your message). Prior to transmission of a Limited Broadcast message, the sender can toggle the message as "Information Only."

|                                                                                                                |                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/159.png) | REF: For more information on the Information Only Toggle, please refer to the "Information Only ("I") Action (Toggle)" topic that follows in this chapter. |

Sending a Broadcast Message When You Hold the XMSTAR Security Key

If you hold the XMSTAR security key, MailMan lets you send both "limited" and "regular" broadcast-type messages, as shown in the following examples (Figure 5‑11 and Figure 5‑12).

Broadcast Message to *All* Local Users

The following example illustrates sending a general Broadcast message to *all* local MailMan users (including SHARED,MAIL). For this example the sender holds the XMSTAR security key:

Select MailMan Menu Option: sml\<Enter\> Send a Message

Subject: Test All Broadcast

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]=========\< Test All Broadcast \>========\[ \<PF1\>H=Help \]====

I'm sending a Test Broadcast message to all users.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Send mail to: XMUSER1,ONE// ?

Enter the recipient(s) of this message in any of the following formats:

Lastname,first for a user at this site

Lastname,first@REMOTE-SITE for a user at another site

(note: DUZ may be used, instead of Lastname,first for local or remote users)

G.\<group-name\> for a mail group

D.\<device-name\> for a device

\* for a limited broadcast or broadcast to all users

(must be Postmaster or XMSTAR key holder)

Prefix any user address with 'I:' to send Information only.

'C:' to send Carbon Copy.

'L:' to send Later.

'-' to delete it.

Enter:

G.? for a list of mail groups

D.? for a list of devices

Enter '??' for detailed help.

Send mail to: XMUSER1,ONE// \*

Select one of the following:

B Broadcast to all local users

L Limited broadcast to local users

Broadcast type: Broadcast to all local users// B\<Enter\> Broadcast to all local users (Broadcast to all local users)

And Send to: \<Enter\>

Since you are broadcasting this message,

would you like to set a vaporize date? Yes// \<Enter\> YES

Enter Vaporize Date: 09/15/06// \<Enter\> (SEP 15, 2006)

Select Message option: Transmit now// \<Enter\> Sending \[100895\]...

Sent

<span id="_Ref144716765" class="anchor"></span>Figure 5‑11. Sending a broadcast message to all local users

As you can see in the previous example (Figure 5‑11), as holders of the XMSTAR security key, the user wanted to send a broadcast-type message to all local MailMan users. Thus, he first used the Send a Message option to compose the message to be broadcast.

After composing the message, MailMan asked the user to choose the recipients. He first entered a question mark ("?") after the "Send mail to: XMUSER1,ONE//" prompt in order to see all the valid types of recipient formats. MailMan displayed the choices; you can see that in order to send any type of Broadcast message users need to enter an asterisk ("\*"). Thus, since the user wanted to send (broadcast) this message to *all* users, he entered an asterisk after the "Send mail to: XMUSER1,ONE//" prompt.

Because the user holds the XMSTAR security key (in this example), MailMan gave him the option to broadcast the message to *all* users or a *subset* of local users (i.e., a Limited Broadcast). Again, the user wanted to broadcast to *all* users, so he entered a "B" (Broadcast to all local users) after the "Broadcast type: Broadcast to all local users//" prompt. He also could have pressed the \<Enter\> key to accept the default of "Broadcast to all local users."

MailMan knew the user was done addressing the message when he pressed the \<Enter\> key at the "And Send to:" prompt without entering a name.

MailMan asked the user if he wanted to set a vaporize date. Because the user did want to vaporize the message, he pressed the \<Enter\> key after the "Since you are broadcasting this message, would you like to set a vaporize date? Yes//" prompt and accepted the default vaporize date at the next prompt.

|                                                                                                                |                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/160.png) | NOTE: If you enter a caret ("^") at the "Since you are broadcasting this message, would you like to set a vaporize date? Yes//" prompt, the broadcast message process is aborted. |

To transmit the Broadcast message, the user pressed the \<Enter\> key at the "Select Message option: Transmit now//" prompt. MailMan then sent the Broadcast message to all local users, automatically making it "Information Only."

To verify that the Broadcast message was automatically sent as "Information Only," without any intervention by the user (the sender), the user opened the message and did a query, as shown below:

Subj: Test All Broadcast \[#100895\] 08/16/06@11:32 1 line

From: XMUSER1,ONE - COMPUTER SPECIALIST (Oakland OI Field Office)

In 'IN' basket. Automatic Deletion Date: Sep 15, 2006 Page 1

-------------------------------------------------------------------------------

I'm sending a Test Broadcast message to all users.

Enter message action (in IN basket): Ignore// Q

Subj: Test All Broadcast \[#100897\] 08/15/06@11:32 1 line

From: XMUSER1,ONE (SF CIOFO) In 'IN' basket.

Local Message-ID: 100897@REDACTED.VA.GOV (2 recipients)

'Information only' for all recipients.

This message was addressed as follows:

\* (Broadcast to all local users)

Enter message action (in IN basket): Ignore//

<span id="_Ref106590693" class="anchor"></span>Figure 5‑12. Verifying that the broadcast message was sent Information only

After reading the message (Figure 5‑12), the user entered a "Q" (Query) after the "Enter message action (in IN basket): Ignore//" prompt in order to confirm that this Broadcast message was sent to all users as "Information Only." MailMan confirmed this by displaying "'Information only' for all recipients" and "\* (Broadcast to all local users)" after displaying the message information.

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/161.png) | REF: For more information on the Query action code, please refer to Table 4‑1 and the "Query ("Q") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

Limited Broadcast to a *Subset* of Local Users

The following example illustrates sending a Limited Broadcast message to a *subset* of local MailMan users. For this example the sender holds the XMSTAR security key:

Select MailMan Menu Option: sml \<Enter\> Send a Message

Subject: Test Limited Broadcast

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]===========\< Test Broadcast \>==========\[ \<PF1\>H=Help \]====

Announcement to all holders of the XMSTAR LIMITED key.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Send mail to: XMUSER1,ONE// \*

Select one of the following:

B Broadcast to all local users

L Limited broadcast to local users

Broadcast type: Broadcast to all local users// L \<Enter\> Limited broadcast to local users

Select LIMITED BROADCAST: ?

Answer with LIMITED BROADCAST

Choose from:

DIVISION

KEY

PRIMARY MENU

SERVICE/SECTION

Select LIMITED BROADCAST: key \<Enter\>

Select Limited Broadcast KEY: XMSTAR LIMITED

Limited broadcast recipients:

XMUSER1,ONE

And Send to: \<Enter\>

Since you are broadcasting this message,

would you like to set a vaporize date? Yes// \<Enter\> YES

Enter Vaporize Date: 09/15/06// \<Enter\> (SEP 15, 2006)

Select Message option: Transmit now// \<Enter\> Sending \[100895\]...

Sent

<span id="_Ref106590808" class="anchor"></span>Figure 5‑13. Sending a limited broadcast message

As you can see in this example (Figure 5‑13), as holders of the XMSTAR security key, the user wanted to send a Limited Broadcast message to a subset of local MailMan users. Thus, he first used the Send a Message option to compose the message to be broadcast.

After composing the message, MailMan asked the user to choose the recipients. Since he wanted to send a Limited Broadcast message to a *subset* of local users, he entered an asterisk after the "Send mail to: XMUSER1,ONE//" prompt.

Because the user holds the XMSTAR security key (in this example), MailMan gave him the option to broadcast the message to *all* users or a *subset* of local users (i.e., a Limited Broadcast). Again, the user wanted to broadcast to a *subset* of users, so he entered an "L" (Limited broadcast to local users) after the "Broadcast type: Broadcast to all local users//" prompt.

|                                                                                                                |                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/162.png) | NOTE: If you only hold the XMSTAR LIMITED security key, MailMan will not give you the choice to send a Broadcast message to all local users. Instead, MailMan will choose "L" (Limited broadcast to local users). |

MailMan knew the user was done addressing the message when he pressed the \<Enter\> key at the "And Send to:" prompt without entering a name.

MailMan asked the user if he wanted to set a vaporize date. Because the user did want to vaporize the message, he pressed the \<Enter\> key after the "Since you are broadcasting this message, would you like to set a vaporize date? Yes//" prompt and accepted the default vaporize date at the next prompt.

To transmit the Broadcast message, the user pressed the \<Enter\> key at the "Select Message option: Transmit now//" prompt. MailMan then sent the Broadcast message to all local users.

|                                                                                                                |                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/163.png) | NOTE: Unlike the Broadcast message to all local users, if you want a Limited Broadcast message to be "Information Only" you have to specify it yourself. |

To verify the address information for the Limited Broadcast message, the user opened the message and did a query, as shown below:

Subj: Test Limited Broadcast \[#100895\] 08/16/06@14:42 1 line

From: XMUSER1,ONE - COMPUTER SPECIALIST (Oakland OI Field Office)

In 'IN' basket. Automatic Deletion Date: Sep 15, 2006 Page 1

-------------------------------------------------------------------------------

Announcement to all holders of the XMSTAR LIMITED key.

Enter message action (in IN basket): Ignore// Q

Subj: Test Limited Broadcast \[#100895\] 08/16/06@14:42 1 line

From: XMUSER1,ONE - COMPUTER SPECIALIST (Oakland OI Field Office)

In 'IN' basket. Automatic Deletion Date: Sep 15, 2006

Local Message-ID: 100895@REDACTED.VA.GOV (2 recipients)

This message was addressed as follows:

\*;KEY;XMSTAR LIMITED

Enter message action (in IN basket): Ignore//

<span id="_Ref107048002" class="anchor"></span>Figure 5‑14. Querying a limited broadcast message

After reading the Limited Broadcast message (Figure 5‑14, originally created in Figure 5‑11), the user entered a "Q" (Query) after the "Enter message action (in IN basket): Ignore//" prompt in order to display the address information for this message. As you can see, MailMan indicated that this was a Limited Broadcast message by displaying the three components of the address separated by semicolons (i.e., "\*;KEY;XMSTAR LIMITED").

The three components indicate the following:

- \* (Asterisk)—This is a broadcast-type message.
- KEY—The message is limited to local users that hold a specific security key.
- XMSTAR LIMITED—The message is limited to local users that hold the XMSTAR LIMITED security key.

|                                                                                                                |                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/164.png) | NOTE: Compare this query with the query done for the Broadcast message sent to all local users (i.e., Figure 5‑11). |

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/165.png) | REF: For more information on the Query action code, please refer to Table 4‑1 and the "Query ("Q") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

Trying to Send a Broadcast Message When You Do Not Hold the Proper Security Keys

The following example illustrates what happens when you try sending any type of Broadcast message (i.e., Broadcast or Limited Broadcast) when you (the sender) do not hold the proper security keys (i.e., XMSTAR or XMSTAR LIMITED):

Select MailMan Menu Option: sml \<Enter\> Send a Message

Subject: Test Broadcast, No Key

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]========\< Test Broadcast No Key \>======\[ \<PF1\>H=Help \]====

Test sending a Broadcast message without holding the proper security keys.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Send mail to: XMUSER1,ONE// \*

Only the Postmaster or XMSTAR key holders may broadcast messages.

Send mail to: XMUSER1,ONE// ^

Shall we forget the whole thing? No// y \<Enter\> YES

<span id="_Ref106590951" class="anchor"></span>Figure 5‑15. Trying to send a broadcast message without holding the proper security keys

In this example (Figure 5‑15), since the user does *not* hold the XMSTAR or XMSTAR LIMITED security keys, MailMan will *not* let him send a broadcast-type message of any kind, as evidenced by MailMan's response when the user entered an asterisk ("\*") at the "Send mail to: XMUSER1,ONE// " prompt.

### Delivery Options—Immediate, Deferred, and/or Staggered

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Besides sending a message immediately (Transmit Now), MailMan V. 8.0 allows you to send messages at different dates and times per recipient or per message. You can do any of the following:

- Transmit Now (default)—Using the Transmit Now action code, you can send the message to all recipients immediately.

|                                                                                                                |                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/166.png) | REF: For more information on the Transmit Now action code, please refer to the "Transmit Now ("T") Action" topic that follows in this chapter. |

- Deferred Send—Using the Transmit Later action code, you can specify a later delivery date and time (up to one year into the future) of a message for *all* recipients.

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/167.png) | REF: For more information on the Transmit Later action code, please refer to the "Transmit Later ("L") Action" topic that follows in this chapter. |

- Staggered Delivery—Using the Later prefix code, you can specify a different, later delivery date and time (from at least five minutes up to one month into the future) of a message for *each* recipient.

|                                                                                                                |                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/168.png) | REF: For more information on the Later prefix code, please refer to the "Later ("L:xxx") Prefix Code" topic that follows in this chapter. |

### Later ("L:xxx") Prefix Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "L:xxx" prefix code (where "xxx" represents the recipient's name) is an additional prefix code. It allows you to individually enter a specific delivery date and time (from at least five minutes into the future up to one month) for each recipient of a message. You can use this prefix code in conjunction with either the Transmit Now (send the message immediately) or the Deferred Send (send the message later) action codes.

For example, if you want a few recipients from the list of the recipients of your message to receive the message at a much later date and time, you could first use the staggered delivery function to specify the later delivery date and time for those specific recipients and then send the message using either the Transmit Now or Deferred Send action codes.

After the message with staggered delivery dates and times has been sent, and *before* it has been delivered to the staggered recipients, doing a query on the message will show the intended delivery dates and times for those recipients.

After the message with staggered delivery dates and times has actually been delivered to the recipients, doing a query on the message will indicate that the message was "forwarded" to the recipients.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/169.png) | TIP: It could be helpful to use staggered delivery of a message when working on a project or task that must be done in several steps and a different person must perform each step. You could send a message out to all the participants (recipients), staggering the delivery for each person so that they only receive the message when it was time for them to perform their step (after the previous person should have accomplished the prerequisite step). Finally, you could also later the message to yourself to be made new for you after the last step is completed. That way you could verify that all steps have been completed and the project is done. |

As with other prefix codes, you specify this when entering the recipient at the "And Send to:" prompt, as shown below:

Select MailMan Menu Option: sml\<Enter\> Send a Message

Subject: Staggered Delivery Test

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]===\< Another Late Delivery Test, Pl \>==\[ \<PF1\>H=Help \]====

Testing a message with staggered delivery dates.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

Send mail to: XMUSER1,ONE E.// ?

Enter the name(s) of the recipient(s) of this message

in any of the following formats:

Lastname,first for a user at this site

Lastname,first@REMOTE-SITE for a user at another site

(note: DUZ may be used instead of Lastname,first)

G.\<group-name\> for a group of users

D.\<device-name\> for a device

\* for a limited broadcast or broadcast to all users

(must be Postmaster or XMSTAR key holder)

Prefix any user address with 'I:' to send Information only.

'C:' to send Carbon copy.

'L:' to send Later.

'-' to delete it.

Enter:

G.? for a list of groups

D.? for a list of devices

Enter '??' for detailed help.

Send mail to: XMUSER1,ONE E.// l:xmuser1 \<Enter\> ,ONE E.

Select basket to send to: IN// \<Enter\>

Later Delivery must be at least 5 minutes from now.

When Later: (8/26/98 - 9/26/98): 08/26/98@08:05// 8/27/98@8:00a\<Enter\> (AUG 27, 1998@08:00)

<span id="_Ref428755354" class="anchor"></span>Figure 5‑16. Staggering the delivery of a message for each recipient (1 of 2)

And Send to: l:xmuser2 \<Enter\> ,TWO M. INFORMATION

Last used MailMan: 08/26/98@06:46

If wishes were horses, beggars would ride.

Later Delivery must be at least 5 minutes from now.

When Later: (8/26/98 - 9/26/98): 08/26/98@08:06// 8/27/98@6:00a\<Enter\> (AUG 27, 1998@06:00)

And Send to: L:xmuser4 \<Enter\> ,FOUR INFORMATION SYSTEMS CENTER

Last used MailMan: 08/26/98@06:30

Later Delivery must be at least 5 minutes from now.

When Later: (8/26/98 - 9/26/98): 08/26/98@08:07// 8/27/98@7:00a\<Enter\> (AUG 27, 1998@07:00)

And Send to: \<Enter\>

Select Message option: Transmit now// \<Enter\>

Sending \[1226401\] Sent

<span id="_Toc147225871" class="anchor"></span>Figure 5‑17. Staggering the delivery of a message for each recipient (2 of 2)

As you can see from the previous example (Figure 5‑16), during the addressing of the message, the user first entered a question mark ("?") at the "Send mail to: XMUSER1,ONE E.//" prompt in order to display the Help information for this prompt. MailMan indicated the valid name information and also displayed the prefix codes the user could use. He decided to stagger the delivery of this message to each recipient, including himself, using the "Later" prefix code prior to the recipient's name (i.e., "L:" prefix).

The user decided to "later" the message in the "IN" mail basket by first entering "l:xmuser1" at the "Send mail to: XMUSER1,ONE E.//" prompt.

The user accepted the default basket (i.e., "IN") by pressing the \<Enter\> key at the "Select basket to send to: IN//" prompt. Besides this "later" message, it will also be delivered to the "IN" basket immediately, as usual.

MailMan then prompted the user to enter the "Later" date and time to deliver the message to himself (i.e., make *New* again). He entered "8/27/98@8:00a" at the "When Later: (8/26/98 - 9/26/98): 08/26/98@08:05//" prompt and MailMan redisplayed the full date to the user (i.e., "AUG 27, 1998@08:00"). The default response will be five minutes into the future.

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/170.png) | NOTE: MailMan will not actually send another copy of the message to the user but will make the message New again on 8/27/98 at 8:00 a.m. If the user has deleted it, MailMan will redeliver it. |

For the first recipient (i.e., XMUSER2,TWO M.), the user wanted to send the message on 8/27/98 at 6:00 a.m. To do this he entered "l:xmuser2" at the "And Send to:" prompt.

MailMan then prompted the user to enter the "Later" date and time to deliver the message to this recipient. He entered "8/27/98@6:00a" at the "When Later: (8/26/98 - 9/26/98): 08/26/98@08:06//" prompt and MailMan redisplayed the full date to the user (i.e., "AUG 27, 1998@06:00").

For the second recipient (i.e., XMUSER4,FOUR), the user wanted to send the message on 8/27/98 at 7:00 a.m. To do this he entered "L:xmuser4" after the next "And Send to:" prompt. Again MailMan found the user and displayed the rest of her name to the user.

MailMan then prompted the user to enter the "Later" date and time to deliver the message to this recipient. He entered "8/27:98@7:00a" at the "When Later: (8/26/98 - 9/26/98): 08/26/98@08:07//" prompt and MailMan redisplayed the full date to the user (i.e., "AUG 27, 1998@07:00").

Even though MailMan indicates the message had been sent, it will *not* be delivered to the recipients with staggered delivery dates until the prescribed date and time is reached.

In all cases, MailMan only allowed the user to project a date within a prescribed period of time (from five minutes to one month in the future). For this example, the user could send the message from 08/26/98 (the date he was sending the message, at least five minutes into the future) through 09/26/98.

MailMan will deliver the message to the recipients at the specified dates and times indicated below:

|                         |                                       |
|-------------------------|---------------------------------------|
| Recipient Name      | Delivery Date & Time (Staggered)  |
| XMUSER1,ONE E. (Sender) | August 26, 1998, immediately          |
| XMUSER1,ONE E. (Sender) | August 27, 1998 at 8:00 a.m. (as New) |
| XMUSER2,TWO M.          | August 27, 1998 at 6:00 a.m.          |
| XMUSER4,FOUR            | August 27, 1998 at 7:00 a.m.          |

Doing a Query ("Q") on a message with staggered delivery shows the following information:

Subj: Staggered Delivery Test \[#1226401\] 08/26/98@08:02 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'IN' basket. Message will be NEW Later. Page 1

-----------------------------------------------------------------------------------

Testing a message with staggered delivery dates.

Enter message action (in TEST basket): IGNORE// q

Subj: Staggered Delivery Test \[#1226401\] 08/26/98@08:02 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'TEST' basket. Message will be NEW Later.

Local Message-ID: 1226401@REDACTED.VA.GOV (1 Recipient)

Message will be NEW on: 08/27/98@08:00

This message was addressed as follows:

XMUSER1,ONE E.

XMUSER2,TWO M. for delivery 08/27/98@06:00 by XMUSER1,ONE E.

XMUSER4,FOUR for delivery 08/27/98@07:00 by XMUSER1,ONE E.

Enter message action (in TEST basket): IGNORE//

<span id="_Toc436461098" class="anchor"></span>Figure 5‑18. Doing a query on a message with staggered delivery

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/171.png) | REF: For more information on the Query action code, please refer to Table 4‑1 and the "Query ("Q") Action" topic in Chapter4 in this manual. |

Doing a Query Detailed ("QD") on the message with staggered delivery, before the message is delivered to the recipients, shows the following information:

Subj: Staggered Delivery Test \[#1226401\] 08/26/98@08:02 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'IN' basket. Message will be NEW Later. Page 1

-----------------------------------------------------------------------------------

Testing a message with staggered delivery dates.

Enter message action (in TEST basket): IGNORE// qd

Subj: Staggered Delivery Test \[#1226401\] 08/26/98@08:02 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'IN' basket. Message will be NEW Later.

Local Message-ID: 1226401@REDACTED.VA.GOV (1 Recipient)

XMUSER1,ONE E. Last read: 08/26/98@08:02 \[First read: 08/26/98@08:02\]

Enter message action (in TEST basket): IGNORE//

<span id="_Toc436461099" class="anchor"></span>Figure 5‑19. Doing a Query Detail on a message with staggered delivery (1)

Doing another Query Detailed ("QD") on the message with staggered delivery, after the message has been delivered to the recipients, shows the following:

Subj: Staggered Delivery Test \[#1226401\] 08/26/98@08:02 2 lines

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'IN' basket. Message will be NEW Later. Page 1

Local Message-ID: 1226401@REDACTED.VA.GOV (3 Recipients)

XMUSER2,TWO M. Last read: 08/27/98@06:38 \[First read: 08/27/98@06:38\]

Forwarded by: XMUSER1,ONE E. 08/27/98@06:00

XMUSER4,FOUR Not read. Forwarded by: XMUSER1,ONE E. 08/27/98@07:00

XMUSER1,ONE E. Last read: 08/27/98@08:49 \[First read: 08/26/98@08:02\]

Enter message action (in TEST basket): IGNORE//

<span id="_Toc436461100" class="anchor"></span>Figure 5‑20. Doing a Query Detail on a message with staggered delivery (2)

|                                                                                                                |                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/172.png) | REF: For more information on the Query Detailed action code, please refer to Table 4‑1 and the "Query Detailed ("QD") Action" topic in Chapter 4 in this manual. |

### Completing an Interrupted Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are in the middle of composing or addressing a message and are inadvertently logged off the system, MailMan will automatically place you back into your editor to complete the message when you re-enter MailMan, as shown below:

Select ISC OFFICE MENU OPTIONS Option: 4 \<Enter\> MailMan Menu

You have an unsent message in your buffer.

Subj: Test

You may have lost some of the text.

You must re-enter recipients and any special handling instructions.

You may edit the text of the message...

==\[ WRAP \]==\[ INSERT \]================\< Test \>===============\[ \<PF1\>H=Help \]====

Here I'm entering my message text

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

.

.

.

<span id="_Toc436461101" class="anchor"></span>Figure 5‑21. MailMan notifies you when you have an unsent message

Before the main MailMan Menu is displayed, MailMan will inform you about any unsent message and automatically place you into your editor where you can complete your message as usual.

### Sending Mail Using the P-MESSAGE Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rather than printing information (e.g., a report or listing) to the screen or a printer, the P-MESSAGE device can be used to send a mail message to yourself and/or others that contains the information.

For example, you may want to keep a copy of a report by sending it to yourself in a mail message by directing the report to the P-MESSAGE device, as shown below:

Select MailMan Menu Option: other \<Enter\> MailMan Functions

Report on Later'd Messages

Change/Delete Later'd Messages

Mailbox Contents List

Select Other MailMan Functions Option: report on Later'd Messages

DEVICE: HOME// p-message\<Enter\> P-MESSAGE-HFS HFS FILE=\>MESSAGE

Moving text to MailMan message... (Creating now)

Subject: Latered Messages Report as of 2/11/99

.

End of file reached

Select one of the following:

M Me

P Postmaster

From whom: Me// ?

Answer 'Me' if the message should be from you.

If you send this to yourself, it will not be delivered new to you,

but you will be able to edit it, if you don't send it to anyone else.

Answer 'Postmaster' if the message should be from the Postmaster.

If you send this to yourself, it will be delivered new to you,

but you will not be able to edit it.

Select one of the following:

M Me

P Postmaster

From whom: Me// post \<Enter\> Postmaster

Send mail to: XMUSER1,ONE E.// \<Enter\>

Select basket to send to: IN// \<Enter\>

And Send to: \<Enter\>

Message subject: Latered Messages Report as of 10/21/98, Message number: 1236565

<span id="_Ref106615637" class="anchor"></span>Figure 5‑22. Using the P-MESSAGE device

For this example (Figure 5‑22), the user wanted to print a report on "latered" messages to an e-mail message that she would send to herself.

After choosing the Report on Later'd Messages option on the Other MailMan Functions menu, the user chose to print the report to the P-MESSAGE device by entering "P-MESSAGE" at the "DEVICE: HOME//" prompt.

When printing to the P-MESSAGE device, MailMan prompted the user to enter a subject for the message that would contain the report. In this case, she entered "Latered Messages Report as of 2/11/99" at the "Subject:" prompt.

MailMan gives you the choice of having the message come from yourself or the Postmaster, in this case, the default is to have messages sent to the P-MESSAGE device come from the user (i.e., "Me"). Since the user did *not* need to edit the message, she had it come from the Postmaster by entering "post" (i.e., Postmaster) after the "From whom: Me//" prompt. Thus, it would appear as "new" in the user's mailbox.

Also, the user chose to only address the message to herself. When the addressing was complete, MailMan indicated that the message had been sent.

|                                                                                                                |                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/173.png) | NOTE: You can use the User Options Edit option to set the P-MESSAGE FROM field default value. |

|                                                                                                                |                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/174.png) | REF: For more information on the P-MESSAGE FROM field, please refer to the "P-MESSAGE From" topic in Chapter 4 in the *MailMan Getting Started Guide*. |

When you look at this message you see that it came from the Postmaster rather than user, as shown below:

Subj: Latered Messages Report as of 2/11/98 \[#1236565\] 02/11/99@07:28 4 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Later'd Messages Report for: XMUSER1,ONE E. Page: 1

Date Basket Message Subject

-------------------------------------------------------------------------------

07/03/99 TEST 1229871 test 2

Enter message action (in IN basket): IGNORE//

<span id="_Toc436461103" class="anchor"></span>Figure 5‑23. Sample report printed to the P-MESSAGE device

Because the message came from the Postmaster, it was flagged as "new." Thus, the user knew when it had been delivered.

|                                                                                                                |                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/175.png) | NOTE: P-MESSAGE assumes that if there are more than 250 consecutive null lines in a printout, that the end of file (EOF) must have been reached. |

|                                                                                                                |                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/176.png) | REF: For more information on the Other MailMan Functions and Report on Later'd Messages options, please refer to Chapter 11, "Reports and Lists," in this manual. |

|                                                   |                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/177.png) | TIP: Let's say you are viewing a laboratory report online and want to show it to several other people. Rather than printing the report, photocopying it, and distributing it to all of the other people yourself, print the report to P-MESSAGE and let MailMan copy and distribute the report automatically via a mail message. |

### Action Codes—Sending Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists *all* of the possible actions that you can perform when sending a message:

| Action Code | Description                                                                                                                                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| B           | Backup—Back up to review the message you were just editing before you send it.                                                                                                                                     |
| C           | Confidential Toggle—Toggle whether or not a message can only be read by the designated recipient and *not* their surrogate(s), depending on the current setting.                                                   |
| D           | Delivery Basket Set—Specify the delivery basket to send the message for all recipients; however, each recipient controls how they actually will receive the mail.                                                  |
| ER          | Edit Recipients—Edit just the recipients of your message.                                                                                                                                                          |
| ES          | Edit Subject—Edit just the text in the subject of your message.                                                                                                                                                    |
| ET          | Edit Text—Edit just the text in the body of your message.                                                                                                                                                          |
| I           | Information Only Toggle—Toggle whether or not a message prevents recipients from replying, depending on the current setting.                                                                                       |
| IM          | Include Message—Include any combination of responses from another message in the new message being created.                                                                                                        |
| L           | Transmit later—Send your message to all addressees at a specified date and time.                                                                                                                                   |
| NS          | Network Signature—Append a Network Signature to the text of your message.                                                                                                                                          |
| P           | Priority Delivery Toggle—Toggle whether or not a message is sent as priority mail.                                                                                                                                 |
| R           | Confirm Receipt Toggle—Toggle whether or not a message will send you a notification message when a recipient has opened your message.                                                                              |
| S           | Scramble Text With Password—Scrambles your message text when passing sensitive or private information. Recipient(s) *must* be given a "Scramble Hint" to decipher the password to unscramble and read the message. |
| T           | Transmit Now—Immediately send your message to all addressees.                                                                                                                                                      |
| V           | Vaporize date set—Automatically set your message for deletion from all recipients' mailboxes at a specified date and time; however, recipients can edit this date for themselves.                                  |
| X           | Closed Message Toggle—Toggle whether or not a message prevents recipients from forwarding your message, depending on the current setting.                                                                          |
| ^           | Caret ("^")—Cancel your message before sending it. (Available at any prompt during the send process.)                                                                                                          |

<span id="_Ref106607972" class="anchor"></span>Table 5‑1. Action codes—Sending messages

|                                                                                                                |                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/178.png) | NOTE: Each action code is described in greater detail in the topics that follow. |

### Backup ("B") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Backup action code (i.e., "B") to review a message before you send it.

To review a message (i.e., back up) before sending it, enter a "B" at the "Select Message option: Transmit now//" prompt, as shown below:

Select Message option: Transmit now// B \<Enter\> Backup to review message

Subj: Sending a Message \[#1224707\] 1 line

From: In '' basket. Page 1

-------------------------------------------------------------------------------

Here I am composing a message to send to several recipients as a test.

Select Message option: Transmit now//

<span id="_Ref428676535" class="anchor"></span>Figure 5‑24. Reviewing a message before sending it

In this example (Figure 5‑24), the user entered a "B" at the "Select Message option: Transmit now//" prompt. MailMan immediately backed up to the top of the message, including the message header. You'll notice the message header is not complete. The "From:" portion of the header is missing the basket and sender's name, because this message has not been sent yet.

After completing the backup action (reviewing the message), MailMan returned the user to the send message action prompt where he could take any additional actions on this message before sending it (e.g., edit the text, edit the subject, or edit the recipients, make it a priority message, etc.).

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/179.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

### Confidential ("C") Action (Toggle)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Confidential action code (i.e., "C") to only allow the designated recipient(s) and *not* their surrogate(s) to read the message you are sending. This is a toggle action code. If you enter "C" again, the message will no longer be confidential.

To send a confidential message, enter a "C" at the "Select Message option: Transmit now//" prompt, as shown below:

Select Message option: Transmit now// C\<Enter\> Confidential (surrogate can't read)

Message flagged 'Confidential'

Select Message option: Transmit now//

<span id="_Ref428166566" class="anchor"></span>Figure 5‑25. Designating a message as confidential

Simply by entering a "C" at the "Select Message option: Transmit now//" prompt (Figure 5‑25), the user asked MailMan to make the message confidential so that only the recipient(s) can read this message and *not* their surrogate(s), unless a surrogate trying to read the message is the same surrogate who sent it. MailMan confirmed that the message was now confidential by displaying "Message flagged 'Confidential'."

After the user made the message confidential, MailMan returned her to the send message action prompt where she could take any additional actions on this message before sending it.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/180.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

If a surrogate tries to read a confidential message and they were not the surrogate who sent it, MailMan displays a message, as shown below:

Select MailMan Menu Option: aml \<Enter\> Become a Surrogate (SHARED,MAIL or Other)

Select NEW PERSON NAME: SHARED,MAIL// xmuser1 \<Enter\> ,ONE E. Read Privilege 19 New Msgs

VA MailMan 8.0 service for XMUSER1.ONE_E+@REDACTED.VA.GOV

(Surrogate: XMUSER4,FOUR)

XMUSER1,ONE E. last used MailMan: 08/19/98@13:13

XMUSER1,ONE E.'s current banner: "Read the Manual....Please!"

XMUSER1,ONE E. has 1 new message.

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

XMUSER1,ONE E. has 1 new message. (Last arrival: 08/19/98@13:17)

Select MailMan Menu Option: NML \<Enter\> New Messages and Responses

You have new mail in more than one basket.

Select New mail option: Read new mail by basket// LN \<Enter\> List all New messages

All Baskets, New messages: 1

\*=New/!=Priority....................Subject............Lines.From......Read/Rcvd

\* 1. IN \[1225525\] 08/19/98 Confidential 1 XMUSER2,TWO M.

Enter message number or command: 1

Surrogates may not read CONFIDENTIAL messages.

Press RETURN to continue:

<span id="_Toc436461106" class="anchor"></span>Figure 5‑26. Surrogates & confidential messages

|                                                                                                                |                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/181.png) | NOTE: Recipients of a confidential message can still forward the message; however, confidential messages *cannot* be sent or forwarded to SHARED,MAIL. |

|                                                                                                                |                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/182.png) | REF: For more information on SHARED,MAIL and surrogates, please refer to Chapter 9, "Surrogates," in this manual. |

### Delivery Basket Set ("D") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Delivery Basket Set action code (i.e., "D") to specify the *intended* delivery mail basket for all recipients of the message you are sending. Depending on how each recipient has set their delivery basket privileges using the Delivery Basket Edit option on the Personal Preferences menu, the message *may* or *may not* be delivered to the intended basket set by you. The message, however, is still delivered to each recipient's mailbox. The delivery basket specified remains in effect, even if a recipient forwards the message to another MailMan user.

|                                                                                                                |                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/183.png) | REF: For more information on the Delivery Basket Edit option or the Personal Preferences option, please refer to the "Set Your Delivery Basket Privileges" topic in Chapter 3 in the *MailMan Getting Started Guide*. |

Setting a delivery basket *overrides* any filters created by a recipient of the message. Also, if allowed by a recipient and the mail basket specified does *not* already exist, MailMan will create the new delivery mail basket for that recipient.

|                                                                                                                |                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/184.png) | REF: For more information on mail filters, please refer to Chapter 7, "Filtering Mail," in this manual. |

To set the delivery basket for a message, enter a "D" at the "Select Message option: Transmit now//" prompt, as shown below:

Select Message option: Transmit now// D\<Enter\> Delivery basket set

The delivery basket is the basket to which this message should be delivered

for all recipients (even future ones, should the message be forwarded).

Any message filters, which the recipient might have, are ignored.

If the basket does not exist, it will be created.

> **NOTE:** The recipients must have chosen to allow delivery baskets by setting

ACCEPT DELIVERY BASKET? under 'Personal Preferences\|Delivery Basket Edit'

to one of the following:

YES - If basket doesn't exist, create it, and deliver the message to it.

EXIST - If the basket already exists, then deliver the message to it.

Else, just deliver the message as usual.

SELECT - If the basket already exists AND accepts such messages,

then deliver the message to it.

Else, just deliver the message as usual.

If the recipient has not set this field or has set it to NO, then

the message would be delivered as usual.

Select delivery basket: ?

Answer with BASKET

Do you want the entire BASKET List? n \<Enter\> (No)

Select delivery basket: Test Messages

Are you adding 'Test Messages' as a new BASKET? No// y \<Enter\> (Yes)

Select Message option: Transmit now//

<span id="_Ref427973398" class="anchor"></span>Figure 5‑27. Sending a message to a specific delivery basket

For this example (Figure 5‑27), the user decided to specify the delivery basket he would like the message to be delivered to for each recipient of the message. Thus, he entered a "D" (Delivery Basket action code) at the "Select Message option: Transmit now//" prompt.

MailMan then displayed the description and restrictions of this option.

MailMan then asked the user to specify a delivery basket. Initially he entered a question mark ("?") at the "Select delivery basket:" prompt in order to find out what he should enter at this prompt. MailMan indicated to the user that he could enter any of his own existing mail baskets and gave him the option to display the current list of mail baskets. Since you generally send yourself a copy of your own message, MailMan asks you to choose a basket from your own list of mail baskets. In this case, the user declined displaying the basket list by entering "No" at the "Do you want the entire BASKET List?" prompt. In this example, the user decided to specify a new delivery basket (not currently in the list of mail baskets) by entering the new mail basket's name at the "Select delivery basket:" prompt (i.e., "Test Messages"). MailMan recognized this mail basket as being new and prompted the user to confirm that he intended on creating a new basket. Since he did, he entered "Yes" at the "Are you adding 'Test Messages' as a new BASKET? No//" prompt.

|                                                                                                                |                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/185.png) | NOTE: Though a delivery basket you specify may be new to your own list of mail baskets, it might not be new for the recipients of your message. |

After MailMan created the new delivery mail basket, MailMan returned the user to the send message action prompt where he could take any additional actions on this message before sending it.

When the user sends (transmits) this message (Figure 5‑27), it will be delivered according to the recipient's delivery basket privileges. Thus, if the recipient's delivery basket privileges are set to:

- YES, ACCEPT IT—The message will be delivered to the basket the user designated (i.e., "Test Messages"). If the recipient does not have a mail basket called "Test Messages," it will automatically be created and the message will be delivered to it. This setting allows senders to create a new mail basket in a recipient's mailbox.
- NO, DON'T ACCEPT IT—The message will *not* be delivered to the basket the user designated (i.e., "Test Messages"). If the recipient's mail filters do not automatically reroute the mail to another mail basket, it will be delivered to their "IN" basket. This setting does not allow senders to create a new mail basket in a recipient's mailbox.
- EXISTING BASKETS ONLY—If the recipient already has a mail basket called "Test Messages," the message will be delivered to it. If the recipient does not have a mail basket called "Test Messages" and the recipient's mail filters do not automatically reroute the mail to another mail basket, it will be delivered to their "IN" basket. This setting does not allow senders to create a new mail basket in a recipient's mailbox.
- SELECTED BASKETS ONLY—If the recipient already has a mail basket called "Test Messages" and they have chosen to allow delivery to that mail basket, the message will be delivered to it. If the recipient does not have a mail basket called "Test Messages" or allow delivery to that basket and the recipient's mail filters do not automatically reroute the mail to another mail basket, it will be delivered to their "IN" basket. This setting does not allow senders to create a new mail basket in a recipient's mailbox.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/186.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

### Edit Recipients ("ER") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Edit Recipients action code (i.e., "ER") to add or remove recipients from a message you intend on sending.

To edit the recipients of a message prior to sending it, enter an "ER" at the "Select Message option: Transmit now//" prompt, as shown below:

Select MailMan Menu Option: SML \<Enter\> Send a Message

Subject: Sending a Message

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]==========\< Sending a Message \>========\[ \<PF1\>H=Help \]====

Here I am composing a message to send to several recipients as a test.

\<======T=======T=======T=======T=======T=======T=======T=

Send mail to: XMUSER1,ONE E.// \<Enter\>

Select basket to send to: IN// \<Enter\>

And Send to: xmuser2 \<Enter\> ,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 07/30/98@14:54

On vacation 31 July through 16 August.

And Send to: xmuser3 \<Enter\> ,THREE VERIFICATION

Last used MailMan: 08/13/98@11:26

And Send to: xmuser4 \<Enter\> ,FOUR INFORMATION SYSTEMS CENTER

Last used MailMan: 08/13/98@14:22

And Send to: \<Enter\>

Select Message option: Transmit now// ER\<Enter\> Edit Recipients

And Send to: ??

Select one of the following:

U User information

G Mail Group information

D Domain information

R Remote user information

S Show current recipients of this message

M More help

Enter the kind of help you'd like: S\<Enter\> Show current recipients of this message

Current recipients are:

XMUSER2,TWO M.

XMUSER1,ONE E.

XMUSER4,FOUR

XMUSER3,THREE

Like more detail? YES// n\<Enter\> NO

<span id="_Ref428605027" class="anchor"></span>Figure 5‑28. Editing the recipients of a message (1 of 2)

After composing the subject and message (Figure 5‑28), the user decided to edit the recipients by entering an "ER" at the "Select Message option: Transmit now//" prompt.

MailMan then presented the user with the "And Send to:" prompt where she entered two question marks ("??") in order to display the list of options. In this case, the user wanted to see to whom she was sending this message. Thus, the user wanted MailMan to "show" the user a list of the current recipients of the message by entering an "S" at the "Enter the kind of help you'd like:" prompt.

After displaying the list of recipients, MailMan asked the user if she wanted any more details. For this example, the user only wanted to see a list of the recipients and did not need any other information. Thus, she entered "No" at the "Like more detail? YES//" prompt.

To exit the Help list, the user entered a caret ("^") at the "Enter the kind of help you'd like:" prompt.

Select one of the following:

U User information

G Mail Group information

D Domain information

R Remote user information

S Show current recipients of this message

M More help

Enter the kind of help you'd like: ^

And Send to: -xmuser3 \<Enter\> ,THREE VERIFICATION

Last used MailMan: 08/24/98@13:23

Deleted.

And Send to: \<Enter\>

Select Message option: Transmit now//

<span id="_Toc147225884" class="anchor"></span>Figure 5‑29. Editing the recipients of a message (2 of 2)

After selecting recipients, the user later decided to remove one of the recipients by first typing a minus sign (hyphen) followed by the first portion of the recipient's last name (i.e., "-XMUSER3") at the "And Send to:" prompt.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/187.png) | REF: For more information on entering names or DUZs, please refer to the "Address Functionality" topic previously described in this chapter. |

Since the user did not wish to make any other recipient changes, he pressed the \<Enter\> key after the next "And Send to:" prompt.

After editing the recipients of the message, MailMan returned the user to the send message action prompt where he could take any additional actions on this message before sending it.

### Edit Subject ("ES") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Edit Subject action code (i.e., "ES") to change the subject text of a message you intend on sending.

The subject of the message is shown whenever the message is displayed. It can be from 3 to 65 characters in length. The message subject cannot be blank. Any leading and trailing blanks are deleted. Also, any sequence of three or more blanks is reduced to two blanks. If a user enters a blank or null subject, the subject will default to "\* No Subject \*". When a message whose subject is "\* No Subject \*" is sent to a remote site, the subject transmitted (in the header record) is null. This is useful for sending a message to a list server (to join or drop a list, etc.) whose subject must be blank and whose text must contain the command to the list server.

To edit the subject of a message prior to sending it, enter an "ES" at the "Select Message option: Transmit now//" prompt, as shown below:

Select MailMan Menu Option: SML \<Enter\> Send a Message

Subject: Sending a Message

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]==========\< Sending a Message \>========\[ \<PF1\>H=Help \]====

Here I am composing a message to send to several recipients as a test.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

Send mail to: XMUSER1,ONE E.// \<Enter\>

Select basket to send to: IN// \<Enter\>

And Send to: xmuser2 \<Enter\> ,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 07/30/98@14:54

On vacation 31 July through 16 August.

And Send to: xmuser3 \<Enter\> ,THREE VERIFICATION

Last used MailMan: 08/13/98@11:26

And Send to: xmuser4 \<Enter\> ,FOUR INFORMATION SYSTEMS CENTER

Last used MailMan: 08/13/98@14:22

And Send to: \<Enter\>

Select Message option: Transmit now// ES \<Enter\> Edit Subject

Subject: Sending a Message// Sending a Test Message

Select Message option: Transmit now//

<span id="_Ref428609764" class="anchor"></span>Figure 5‑30. Editing the subject of a message

After composing the subject and message (Figure 5‑30), the user decided to edit the subject again by entering an "ES" at the "Select Message option: Transmit now//" prompt.

MailMan then presented the user with the "Subject: Sending a Message//" prompt where the current subject was shown as the default. In this case, she wanted to change the current subject "Sending a Message" to "Sending a Test Message." To do this, the user simply entered the new text at the "Subject: Sending a Message//" prompt.

After editing the subject of the message, MailMan returned the user to the send message action prompt where she could take any additional actions on this message before sending it.

### Edit Text ("ET") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Edit Text action code (i.e., "ET") to change the text (body) of the message you intend on sending. You can add to, modify, or delete any part of the text within the body of the message.

To edit the text of a message prior to sending it, enter an "ET" at the "Select Message option: Transmit now//" prompt, as shown below:

Select MailMan Menu Option: SML \<Enter\> Send a Message

Subject: Sending a Message

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]==========\< Sending a Message \>========\[ \<PF1\>H=Help \]====

Here I am composing a message to send to several recipients as a test.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

Send mail to: XMUSER1,ONE E.// \<Enter\>

Select basket to send to: IN// \<Enter\>

And Send to: xmuser2 \<Enter\>,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 07/30/98@14:54

On vacation 31 July through 16 August.

And Send to: xmuser3 \<Enter\> ,THREE VERIFICATION

Last used MailMan: 08/13/98@11:26

And Send to: xmuser4 \<Enter\> ,FOUR INFORMATION SYSTEMS CENTER

Last used MailMan: 08/13/98@14:22

And Send to: \<Enter\>

Select Message option: Transmit now// ET\<Enter\> Edit Text

You may edit the text of the message...

==\[ WRAP \]==\[ INSERT \]=======\< Sending a Test Message \>======\[ \<PF1\>H=Help \]====

Here I am composing a message to send to several recipients as a test.

I've decided to add more text.

\<======T=======T=======T=======T=======T=======T===

Select Message option: Transmit now//

<span id="_Ref428610248" class="anchor"></span>Figure 5‑31. Editing the text of a message

After composing the subject and message (Figure 5‑31), the user decided to edit the text again by entering an "ET" at the "Select Message option: Transmit now//" prompt.

MailMan automatically placed the user into the editor where she could modify the message text. After editing the text, the user saved the changes and closed the editor.

After editing the message text, MailMan returned the user to the send message action prompt where she could take any additional actions on this message before sending it.

### Information Only ("I") Action (Toggle)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Information Only action code (i.e., "I") to send a message as Information Only. Sending a message Information Only prevents all recipients from replying to your message. This is a toggle action code. If you enter "I" again, the message will no longer be Information Only.

|                                                                                                                |                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/188.png) | NOTE: Please note that designating a recipient as "Information Only" is a MailMan-specific capability that is not recognized by other non-MailMan systems. Therefore, any "Information Only" designation is ignored when sending a message to a non-MailMan system (e.g., Microsoft Exchange or Outlook). |

To send a message Information Only, enter an "I" at the "Select Message option: Transmit now//" prompt, as shown below:

Select Message option: Transmit now// I\<Enter\> Information only (recipients may not respond)

Message flagged 'Information only'

Select Message option: Transmit now//

<span id="_Ref428845733" class="anchor"></span>Figure 5‑32. Designating a message as Information Only

Simply by entering an "I" at the "Select Message option: Transmit now//" prompt (Figure 5‑32), the user asked MailMan to make the message Information Only so none of the recipient(s) can reply to this message.

MailMan confirmed that the message was now Information Only by displaying "Message flagged 'Information only'."

After designating the message as Information Only, MailMan returned the user to the send message action prompt where he could take any additional actions on this message before sending it.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/189.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

In addition to making the entire message Information Only, you can also send a message as Information Only to just one individual recipient. During the addressing portion of the message for a recipient, by specifying "I:xxx" (where "xxx" represents the recipient's name) at the "And Send to:" prompt, you are telling MailMan to deliver the message to this individual recipient as Information Only, as shown below:

And Send to: I:xmuser2 \<Enter\> ,TWO M. INFORMATION SYSTEMS CENTER

Last used MailMan: 08/25/98@11:19

If wishes were horses, beggars would ride.

And Send to:

Select Message option: Transmit now//

<span id="_Ref428679352" class="anchor"></span>Figure 5‑33. Sending a message to one recipient as Information Only

As you can see in this example (Figure 5‑33), during the addressing portion of the message, the user entered "I:xmuser2" at the "And Send to:" prompt. This tells MailMan that he wants to send the message to this particular recipient (i.e., "XMUSER2,TWO M.") as "Information Only." Thus, he will not be able to respond to this message; however, all other recipients will *not* receive this message as Information Only and will be able to respond to the message.

### Transmit Later ("L") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Transmit Later action code (i.e., "L") to send a message to all recipients at a later specified date and time (up to one year). This action code uses TaskMan to schedule the delivery of the "latered" or deferred message. You would use this action code *after* you've taken all other actions on your message.

To send a message at a later date and time, enter an "L" at the "Select Message option: Transmit now//" prompt, as shown below:

Select Message option: Transmit now// L \<Enter\> Transmit later

Enter Date@time at which to send this message: (8/13/98 - 8/13/99): ??

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses CURRENT YEAR. Two digit year

assumes no more than 20 years in the future, or 80 years in

the past.

If the date is omitted, the current date is assumed.

Follow the date with a time, such as JAN 20@10, T@10AM, 10:30, etc.

You may enter NOON, MIDNIGHT, or NOW to indicate

the time.

Enter Date@time at which to send this message: (8/13/98 - 8/13/99): 8/17/98@8:00AM \<Enter\> (AUG 17, 1998@08:00)

Latering ... Latered (Task \#1620213)

<span id="_Ref428774335" class="anchor"></span>Figure 5‑34. Sending a message at a later date and time

As you can see from this example (Figure 5‑34), the user wanted to defer the delivery of this message to all recipients by entering an "L" (transmit later) at the "Select Message option: Transmit now//" prompt.

The user then entered two question marks ("??") at the "Enter Date@time at which to send this message: (8/13/98 - 8/13/99):" prompt in order to see the valid VA FileMan date and time formats that can be entered.

You'll notice that the default response allows a date up to one year from the date and time you are sending this message (i.e., 8/13/98 - 8/13/99). In this case (Figure 5‑34), the user chose to have the message sent to all recipients on August 17, 1998 at 8:00 a.m. Thus, she entered "8/17/98@8:00AM" at the "Enter Date@time at which to send this message: (8/13/98 - 8/13/99):" prompt. MailMan accepted the date and displayed the date the message would be delivered to all recipients (i.e., AUG 17, 1998@08:00). MailMan also indicated the TaskMan task number that would process the message's later delivery (i.e., Task \#1620213).

The user does not see the MailMan internal message identification number (the number displayed in brackets when you send a message), because the message will not actually be created until the task runs on the date and time the user specified.

Before the task runs, the user can use the TaskMan options to change the task run date or time, and thus, the date and time the message would be delivered. Also, unlike the Post Office, the user can stop the task entirely, and thus, stop the message from being delivered to the recipients.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/190.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

In order to display information about the scheduled task, the user can use the Toolbox menu options (i.e., TBOX) by entering "tbox" at the "Select MailMan Menu Option:" prompt, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: tbox\<Enter\> User's Toolbox

Display User Characteristics

Edit User Characteristics

Electronic Signature code Edit

Menu Templates ...

Switch UCI

TaskMan User

User Help

Select User's Toolbox Option: taskman \<Enter\> User

Select TASK: 1620213\<Enter\> MailMan: Send Message Later

Taskman User Option

Display status.

Stop task.

Edit task.

Print task.

List own tasks.

Select another task.

Select Action (Task \# 1620213): disp\<Enter\> Display status.

1620213: LATER^XMXSEND, MailMan: Send Message Later. No device. ISC,ISC.

From TODAY at 14:11, By you. Scheduled for 8/17/98 at 8:00

<span id="_Ref433702065" class="anchor"></span>Figure 5‑35. Deferred send task information

Since the user wanted to display information about the scheduled task (Figure 5‑35), she needed to access the TaskMan User Option menu. Thus, after choosing the Toolbox menu, the user entered "taskman" at the "Select User's Toolbox Option:" prompt.

MailMan then asked the user to enter the task number. She entered the task number displayed when she "latered" the message (i.e., "1620213," Figure 5‑34).

MailMan displayed the TaskMan User Option menu. For this example, the user wanted to display information about the task so the user chose the Display status option. Thus she entered "disp" after the "Select Action (Task \# 1620213):" prompt.

MailMan indicated the scheduled date and time that the task would run. This matched the "latered" date and time the user had set to send the message (i.e., "8/17/98 at 8:00").

Before the task runs, the user can also modify the task through the TaskMan User Option menu, as shown below:

Taskman User Option

Display status.

Stop task.

Edit task.

Print task.

List own tasks.

Select another task.

Select Action (Task \# 1620213): edit \<Enter\> Edit task.

Before you edit the task I must unschedule it, is this okay? YES// \<Enter\>

Task ready for editing.

Currently, this task does not request an output device.

Do you want to change the output device for this task? NO// \<Enter\>

When should this task run?: AUG 17, 1998@08:00// 8/17/98@9:00\<Enter\> (AUG 17, 1998@09:00:00)

Task's purpose: MailMan: Send Message Later Replace \<Enter\>

1620213: MailMan: Send Message Later. No output device.

Next run time: AUG 17, 1998@09:00.

Shall I reschedule this task as shown? YES// \<Enter\>

Task rescheduled.

<span id="_Ref433703709" class="anchor"></span>Figure 5‑36. Modified the task run date and time

In this example (Figure 5‑36), the user used the Edit task option to change the task's run date and time from 8/17/98 at 8:00 a.m. to 8/17/98 at 9:00 a.m. (a difference of one hour). Thus, the message will now be delivered one hour later from the original time the user set when he "latered" the message (Figure 5‑34).

You'll notice that the user can also stop the task altogether via the Stop task option.

|                                                                                                                |                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/191.png) | REF: For more information on TaskMan and the Toolbox options, please refer to the *Kernel Systems Manual*. |

### Network Signature ("NS") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Network Signature action code (i.e., "NS") to append a Network Signature to a message before you send it. This is not a toggle, MailMan will add your network signature to the message every time you invoke the NS command.

To add a Network Signature to a message prior to sending it, enter an "NS" at the "Select Message option: Transmit now//" prompt, as shown below:

Select MailMan Menu Option: SML \<Enter\> Send a Message

Subject: Test NS Action Code

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]=========\< Test NS Action Code \>=======\[ \<PF1\>H=Help \]====

Testing NS action code.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Send mail to: XMUSER1,ONE// \<Enter\> XMUSER1,ONE

Select basket to send to: IN// \<Enter\>

And Send to: \<Enter\>

Select Message option: Transmit now// NS

Network Signature added.

Select Message option: Transmit now// \<Enter\> Sending \[100885\]...

Sent

<span id="_Ref106516995" class="anchor"></span>Figure 5‑37. Adding a network signature to a message before sending it

After composing the subject and message (Figure 5‑37), the user decided to add the Network Signature to the message text by entering an "NS" at the "Select Message option: Transmit now//" prompt.

MailMan automatically appended the Network Signature at the end of the text the user entered. It has been added to the bottom of the message separated by a dashed line. MailMan confirmed that the Network Signature was added by displaying "Network Signature added."

|                                                                                                                |                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/192.png) | NOTE: You can use the Edit Text command ("ET") to further edit the message and move the Network Signature to any location within the body of the message. For more information on the Edit Text command ("ET"), please refer to the "Edit Text ("ET") Action" topic previously described in this chapter. |

After editing the message text, MailMan returned the user to the send message action prompt where he could take any additional actions on this message before sending it. If the user entered another "NS" command at the send message action prompt, MailMan would add a second copy of the Network Signature.

To see how the message appears to the message recipient(s) after the Network Signature was added, the user opened/read the message, as shown below:

Subj: Test NS Action Code \[#100885\] 04/19/00@14:49 7 lines

From: XMUSER1,ONE (SF CIOFO) In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Testing NS action code.

-------------------------------------------------------------------------------

One Xmuser1

Oakland OI Field Office

Enter message action (in IN basket): Ignore//

<span id="_Ref106516967" class="anchor"></span>Figure 5‑38. Reviewing the appended network signature added to a message

As you can see in Figure 5‑38, the three-line Network Signature was added following the message text and was separated from the text by a dashed line (also generated by MailMan).

|                                                                                                                |                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/193.png) | REF: For more information on the Network Signature, please refer to the "Network Signature" topic in Chapter 4 in the *MailMan Getting Started Guide*. |

### Priority Delivery ("P") Action (Toggle)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Priority Delivery action code (i.e., "P") to send a message as priority. This is a toggle action code. If you enter "P" again, the message will *not* be sent as priority.

MailMan allows users to send a message as priority mail. By sending mail priority, the sender indicates the message is very important and should take precedence over any other mail in another recipient's mailbox. Because of that, MailMan notifies recipients when they have priority mail and highlights that mail in their list of messages (i.e., places an exclamation point to the left of each priority message).

|                                                                                                                |                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| ![](mailman-version-8-user-guide/194.png) | NOTE: The priority flag is the exclamation point ("!"). |

MailMan also provides recipients with the ability to control how responses to priority mail are handled through the PRIORITY RESPONSES FLAG and the PRIORITY RESPONSES PROMPT fields in the User Options Edit option.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/195.png)</td>
<td><p><strong>REF:</strong> For more information on priority messages, please refer to the "List All of Your Priority Messages" topic in Chapter 2 in this manual.</p>
<p>Also, for more information on the PRIORITY RESPONSES FLAG and the PRIORITY RESPONSES PROMPT fields in the User Options Edit option, please refer to the "Priority Responses" topic in Chapter 4 in the <em>MailMan Getting Started Guide</em>.</p></td>
</tr>
</tbody>
</table>

To send a priority message, enter a "P" at the "Select Message option: Transmit now//" prompt, as shown below:

Select Message option: Transmit now// P\<Enter\> Priority Delivery

Message flagged 'Priority'

Select Message option: Transmit now//

<span id="_Ref428846678" class="anchor"></span>Figure 5‑39. Sending a priority message

Simply by entering a "P" at the "Select Message option: Transmit now//" prompt (Figure 5‑39), the user asked MailMan to make the message priority. Thus, this message will be highlighted as a priority message in each recipient's mailbox.

MailMan confirmed that the message was now priority by displaying "Message flagged 'Priority'."

After designating the message as priority, MailMan returned the user to the send message action prompt where she could take any additional actions on this message before sending it.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/196.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

### Confirm Receipt ("R") Action (Toggle)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Confirm Receipt action code (i.e., "R") to have MailMan notify you (confirm) when each recipient has opened your message. You can request a Confirm Receipt from recipients at remote locations as well as from local recipients. Unfortunately, however, MailMan *cannot* guarantee that every recipient will actually *read* your message! This is a toggle action code. If you enter "R" again, you will *not* receive a confirm receipt.

Select Message option: Transmit now// R \<Enter\> Confirm receipt

Message flagged 'Confirm Receipt Requested'

Select Message option: Transmit now//

<span id="_Ref428846985" class="anchor"></span>Figure 5‑40. Requesting a confirmation when sending a message

Simply by entering an "R" at the "Select Message option: Transmit now//" prompt (Figure 5‑40), the user asked MailMan to send the user a confirmation when the message is opened/read by each recipient.

MailMan confirmed that the user wanted a message confirmation receipt by displaying "Message flagged 'Confirm Receipt Requested'."

After requesting a confirmation receipt, MailMan returned the user to the send message action prompt where he could take any additional actions on this message before sending it.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/197.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

The following figure (Figure 5‑41), shows you what a confirmation receipt looks like:

Subj: Confirmation of message \[#1225084\] 08/17/98@06:42 1 line

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

In 'IN' basket. Page 1 \*New\*

------------------------------------------------------------------

Your message 'Test' has been read by XMUSER2,TWO M..

Enter message action (in IN basket): IGNORE//

<span id="_Ref428847125" class="anchor"></span>Figure 5‑41. Sample confirmation message

### Scramble ("S") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Scramble action code (i.e., "S") to have MailMan scramble (encode) your message so only those recipients who know the password can unscramble (decode) your message. You may decide to send a message as scrambled for security or privacy reasons.

Simply by entering an "S" at the "Select Message option: Transmit now//" prompt (Figure 5‑42), the user asked MailMan to scramble (encode) the message to all recipients, as shown below:

Select Message option: Transmit now// S \<Enter\> Scramble text with password

Enter Scramble Password:

Enter Scramble Hint: the opposite of scramble

Select Message option: Transmit now//

<span id="_Ref428850042" class="anchor"></span>Figure 5‑42. Scramble a message when sending it

MailMan first prompted the user to enter the Scramble Password. For this example, the user entered a password of "unscramble" at the "Enter Scramble Password:" prompt. The password *must* be from 3 to 20 characters in length and it is *not* case sensitive. You must enter the password fairly quickly or MailMan will abort the process for security reasons. As with your Access and Verify codes when logging on to MailMan, MailMan did *not* display the password entry as it was typed.

MailMan then prompted the user to enter a "Scramble Hint" to help the recipient determine the password to unscramble the message. In this case, the user entered "the opposite of scramble" at the "Enter Scramble Hint:" prompt. The "Scramble Hint" *must* be from 1 to 40 characters in length. Thus, the "Scramble Hint" should help the recipient decipher the password so the user can unscramble the message.

After scrambling the message, MailMan returned the user to the send message action prompt where she could take any additional actions on this message before sending it.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/198.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

When the recipient receives a scrambled message, MailMan will prompt them for the password to unscramble the message so they can read it, as shown below:

All Baskets, New messages: 3

\*=New/!=Priority...................Subject............Lines.From.....Read/Rcvd

\*1. IN \[1226635\] 08/27/98 Scrambled Message 1 XMUSER1,ONE E.

\*2. BIWEEKLY I \[1222306\] 07/28/98 Local: biweekly info 2 POSTMASTER 84/86

\*3. BIWEEKLY I \[1226249\] 08/25/98 Local: biweekly info 2 POSTMASTER 5/8

Enter message number or command: 1

This message has been secured with a password:

Subj: Scrambled Message \[#1226635\]

From: XMUSER1,ONE E. - PROGRAMMER (OIFO Oakland)

The Scramble Hint is: 'Enter my name'

Enter Scramble Password:

Subj: Sending a Message Scrambled \[#1226635\] 08/27/98@10:26 1 line

From: XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Field Office Oakland)

In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------

I am sending this message scrambled. Can you read it?

Enter message action (in IN basket): IGNORE//

<span id="_Ref428849989" class="anchor"></span>Figure 5‑43. Unscrambling a message

The user sent a scrambled message (i.e., message \#1) to another recipient. When the recipient tried to read the scrambled message (Figure 5‑43), MailMan informed them that the message was scrambled and that they must enter the correct password in order to unscramble the message.

MailMan also displayed the "Scramble Hint" the sender entered when she originally created the scrambled message ("opposite of scramble" Figure 5‑42). In this case, the recipient was able to decipher the password from the "Scramble Hint" (i.e., "Enter my name = one"). Thus, they entered "one" at the "Enter Scramble Password:" prompt. As with your Access and Verify codes when logging on to MailMan, MailMan did *not* display the password entry as they typed.

MailMan accepted the password, unscrambled the message, and displayed it to the recipient.

If you enter an incorrect password, MailMan responds as follows: "Not the proper password. Strike 1." You have a total of three attempts to enter the correct password. After the third failed attempt, MailMan responds as follows: "Not the proper password. Strike 3. Yer out!" and redisplays the basket message list. Also, if you do not respond within a prescribed period, MailMan will not open the message and automatically redisplays the basket message list.

### Transmit Now ("T") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Transmit Now action code (i.e., "T") to have MailMan send your message to all recipients. You would use this action code *after* you've taken all other actions on your message.

To send the message now, enter a "T" or press the \<Enter\> key to accept the "Transmit now" default at the "Select Message option: Transmit now//" prompt, as shown below:

Select Message option: Transmit now// \<Enter\> Sending \[1224710\]...

Sent

<span id="_Ref428776365" class="anchor"></span>Figure 5‑44. Sending a message immediately

As you can see from this example (Figure 5‑44), to transmit your message to all recipients, you can do either of two things:

- Press the \<Enter\> key—Press the \<Enter\> key at the "Select Message option: Transmit now//" prompt to accept the "Transmit now" default response.
- Enter a "T"—Enter a "T" (Transmit) at the "Select Message option: Transmit now//" prompt.

MailMan automatically gives the message an internal message identification number and puts the message in the delivery queue to be delivered to the recipients.

MailMan will then notify you that the message has been sent.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/199.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

### Vaporize Date Set ("V") Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Vaporize Date Set action code (i.e., "V") to set a specified date and time for a message to be deleted ("vaporized") from each recipient's mailbox. MailMan V. 8.0 gives *all* senders of messages the ability to set a Vaporize Date for a message.

For example, set a Vaporize Date for a message, if you are sure that the message is only needed until a certain date. MailMan will automatically remove it from the basket it is in at that date. The earliest allowable vaporize date is 60 minutes from the current date and time.

As MailMan delivers the message with a Vaporize Date into each recipient's mail basket, MailMan sets the AUTOMATIC DELETION DATE (i.e., vaporize date) for the message. Recipients are free to edit the AUTOMATIC DELETION DATE, however.

Also, a message that is scheduled for vaporization (either by you or by MailMan during the IN-BASKET PURGE) will vaporize on the scheduled date. Previously, it would not vaporize until the IN BASKET PURGE ran again.

To set a "Vaporize Date" for a message, enter a "V" at the "Select Message option: Transmit now//" prompt, as shown below:

Select Message option: Transmit now// V \<Enter\> Vaporize date set

Enter Vaporize Date: 09/12/98// ?

Enter a date in the future when this message should be purged.

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses CURRENT YEAR. Two digit year

assumes no more than 20 years in the future, or 80 years in the past.

You may omit the precise day, as: JAN, 1957

Enter Vaporize Date: 09/12/98// 10/18/98 \<Enter\> (OCT 18, 1998)

Select Message option: Transmit now//

<span id="_Ref428851258" class="anchor"></span>Figure 5‑45. Sending a message with a vaporize date

After the user chose to set a vaporize date for the message, MailMan prompted the user to enter a date and/or time. In this case (Figure 5‑45), the user entered a question mark ("?") at the "Enter Vaporize Date: 09/12/98//" prompt in order to see the valid VA FileMan date and time formats that can be entered.

As a default, MailMan will set the Vaporize Date one month into the future. Since the user was sending this message on August 12, 1998, MailMan set the default Vaporize Date to September 12, 1998.

The user decided to set this message to automatically be deleted ("vaporized") from recipients' mailboxes on October 18, 1998 by entering "10/18/98" at the "Enter Vaporize Date: 09/12/98//" prompt. MailMan confirmed this date by displaying "OCT 18, 1998" after the entry.

After setting the message to vaporize, MailMan returned the user to the send message action prompt where he could take any additional actions on this message before sending it.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/200.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/201.png) | TIP: If you are sending a general message to all users advising them about a temporary event (e.g., system downtime, building fire alarm test, etc.), set the message to "vaporize" after the prescribed time has passed. That way, all recipients of your message who have not yet read their mail will not be bothered with an "old" message that is no longer pertinent, since it will have already been deleted (vaporized). |

### Closed Message ("X") Action (Toggle)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you can see from the list of action codes associated with sending a message (Table 5‑1), you can use the Closed Message action code (i.e., "X") to prevent recipients of your message from forwarding that message on to other recipients not originally included. This is a toggle action code. If you enter "X" again, the message will no longer be closed.

To make a message "closed," enter an "X" at the "Select Message option: Transmit now//" prompt, as shown below:

Select Message option: Transmit now// X \<Enter\> Closed Message (no forward allowed)

Message flagged 'Closed'

Select Message option: Transmit now//

<span id="_Ref428846289" class="anchor"></span>Figure 5‑46. Sending a closed message

Simply by entering an "X" at the "Select Message option: Transmit now//" prompt (Figure 5‑46), the user asked MailMan to make the message closed so that none of the recipient(s) can forward this message to others.

MailMan confirmed that the message was now closed by displaying "Message flagged 'Closed'."

After designating the message as closed, MailMan returned the user to the send message action prompt where she could take any additional actions on this message before sending it.

|                                                                                                                |                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/202.png) | REF: For the preliminary steps of creating a new message prior to the "Select Message option: Transmit now//" prompt (i.e., subject, message text, address information), please refer to the "SML—Send a Message Option" topic and Figure 5‑2 previously described in this chapter. |

### Canceling a Message ("^")

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can cancel a message before you send it by entering a caret ("^") at any of the following Send a Message option \[XMSEND; synonym SML\] prompts:

- Subject:—If you cancel at this prompt, MailMan returns you to the main MailMan Menu.
- Send mail to: xxx//(where xxx represents the sender's name, default)—If you cancel at this prompt, MailMan will ask you to confirm the cancellation. If you answer "Yes," MailMan returns you to the main MailMan Menu. If you answer "No," MailMan continues with the Send a Message option.
- And Send to:—If you cancel at this prompt, MailMan will ask you to confirm the cancellation. If you answer "Yes," MailMan returns you to the main MailMan Menu. If you answer "No," MailMan continues with the Send a Message option.
- Select Message option: Transmit now//—If you cancel at this prompt, MailMan returns you to the main MailMan Menu.

The following example shows you a sample cancellation while addressing a message:

Select MailMan Menu Option: sml\<Enter\> Send a Message

Subject: Canceling a New Message

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]======\< Canceling a New Message \>=====\[ \<PF1\>H=Help \]=====

I will cancel this message.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

Send mail to: XMUSER1,ONE E.// ^

Shall we forget the whole thing? No// \<Enter\> NO

Send mail to: XMUSER1,ONE E.// \<Enter\>

Select basket to send to: IN// \<Enter\>

And Send to: ^

Shall we forget the whole thing? No// y\<Enter\> YES

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option:

<span id="_Ref429535671" class="anchor"></span>Figure 5‑47. Canceling a message before sending it

In this example (Figure 5‑47), after choosing to send a message, the user created the subject and text of the message. When MailMan prompted the user to address the message, she thought about canceling the message by entering a caret ("^") at the "Send mail to: XMUSER1,ONE E.//" prompt.

MailMan then asked the user to confirm the cancellation. Upon second thought, she decided to continue with the addressing, so she answered "No" by pressing the \<Enter\> key to accept the default response at the "Shall we forget the whole thing? No//" prompt.

After the user sent the message to herself and accepted the "IN" mail basket, MailMan prompted the user to enter additional recipients. Here, again, she decided to cancel the message so she entered another caret at the "And Send to:" prompt.

Again, MailMan asked the user to confirm the cancellation. In this case, she verified that she did want to cancel the message by entering "Yes" at the "Shall we forget the whole thing? No//" prompt.

MailMan cancelled the message and put the user back at the main MailMan Menu for other actions, if any.

|                                                   |                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/203.png) | TIP: If you cannot complete a message but will want to continue it later, send the message to yourself. Later, you can use the Read/Manage Messages option \[XMREAD; synonym RML\] to select the unfinished message. You can then use the edit action codes to complete your message and then forward it on to your recipients. |

# Searching Mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics to be discussed in this chapter:

- Query/Search for Messages Option
- Where to Search
- Search Criteria
- Searching All Messages
- Searching Your Own Mailbox

The features and functionality associated with searching for messages are described in greater detail in this chapter.

### Query/Search for Messages Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Query/Search for Messages option gives you the capability to search for any messages that were either sent to you or sent by you. If the messages still reside on the system, MailMan can find them.

The Query/Search for Messages option \[XMSEARCH\] is located on the main MailMan Menu, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages \[XMSEARCH\]

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: q \<Enter\> uery/Search for Messages

Select one of the following:

A Search all messages by multiple criteria

M Search my Mailbox by multiple criteria

S Search all messages by subject only

Select message search method:

<span id="_Toc436461125" class="anchor"></span>Figure 6‑1. Query/Search for messages option

### Where to Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan V. 8.0 allows you to search for any messages you sent or that were sent to you in any of the following locations:

- Anywhere on the system (searches on subject string only, the search is case sensitive)—If the messages still exist anywhere on the system (i.e., if they are still stored in the MESSAGE file (#3.9)), MailMan searches for all messages whose subject *begins* with the string that you entered. Even if you've deleted the message from your own mailbox, if it still resides in the MESSAGE file (#3.9) and you entered a valid subject string in the correct case, MailMan can find it.
- Any mail basket in your mailbox (multiple search criteria allowed)—MailMan will look for the messages in every basket in your mailbox using the search criteria that you enter.

|                                                                                                                |                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/204.png) | NOTE: The search criteria are described in the topics that follow. |

- A specific mail basket in your mailbox (multiple search criteria allowed)—MailMan will look for the messages in a mail basket using the search criteria that you enter.

|                                                                                                                |                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/205.png) | NOTE: The search criteria are described in the topics that follow. |

### Search Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When searching for messages in your own mailbox, you can specify any combination of the following search criteria:

- Subject Contents—Enter the "S" ("Subject contains") search action code and then enter any portion of the subject string (*not* case sensitive). The string can be from 3 to 30 characters in length (including spaces, symbols, and punctuation marks).
- Sender of the Message—Enter the "F" ("Message from") search action code and then enter the first portion of the local sender's last name (*not* case sensitive) or their local DUZ (i.e., numeric user ID).

> For senders at a remote location (*not* located at your site), do any of the following:

- Enter any portion of the remote sender's name (*not* case sensitive) followed by the at-sign ("@", i.e., name@). The name string entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter any portion of the remote sender's name (*not* case sensitive), the at-sign ("@"), and any portion of their domain name (i.e., name@domain, *not* case sensitive). The name and domain name strings entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter the at-sign ("@") and any portion of their domain name (i.e., @domain, *not* case sensitive). The domain name string entered *must* be from 1 to 45 characters in length (*not* case sensitive).

|                                                                                                                |                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/206.png) | NOTE: The more characters you provide, the narrower the search will be. |

- Addressee of a Message—This includes messages addressed to a person or a mail group. MailMan will check the addressees that you see when you Query ("Q") the message. MailMan will *not* check the expanded list of addresses that you see when you use the Query Detailed ("QD") action code.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/207.png)</td>
<td><p><strong>REF:</strong> For more information on the Query action ("Q"), please refer to the "Query ("Q") Action" topic in Chapter 4 in this manual.</p>
<p>Also, for more information on the Query Detailed ("QD") action, please refer to the "Query Detailed ("QD") Action" in Chapter 4 in this manual.</p></td>
</tr>
</tbody>
</table>

> Enter the "T" ("Message to") search action code and then enter the first portion of the local recipient's last name (*not* case sensitive) or their local DUZ (i.e., numeric user ID).

> For addressees at a remote location (*not* located at your site), do any of the following:

- Enter any portion of the remote recipient's name (*not* case sensitive) followed by the at-sign ("@", i.e., name@). The name string entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter any portion of the remote recipient's name (*not* case sensitive), the at-sign ("@"), and any portion of their domain name (i.e., name@domain, *not* case sensitive). The name and domain name strings entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter the at-sign ("@") and any portion of their domain name (i.e., @domain, *not* case sensitive). The domain name string entered *must* be from 1 to 45 characters in length (*not* case sensitive).

|                                                                                                                |                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/208.png) | NOTE: The more characters you provide, the narrower the search will be. |

- Approximately When the Message was Sent—Enter the date the message was sent "on or after" and/or enter the date the message was sent "on or before":
- Enter the "DA" ("Message sent on or after") search action code and then enter a valid VA FileMan date (e.g., AUG 20 1998, 20 AUG 98, 8/20/98, T \[today\], T-1 \[yesterday\], T-3W \[for 3 weeks ago\].
- Enter the "DB" ("Message sent on or before") search action code and then enter a valid VA FileMan date (e.g., AUG 20 1998, 20 AUG 98, 8/20/98, T \[today\], T-1 \[yesterday\], T-3W \[for 3 weeks ago\].
- Specific Responder to a Message—Enter the "R" ("Response from") search action code and then enter the first portion of the local responder's last name (*not* case sensitive) or their local DUZ (i.e., numeric user ID).

> For responders at a remote location (*not* located at your site), do any of the following:

- Enter any portion of the remote responder's name (*not* case sensitive) followed by the at-sign ("@", i.e., name@). The name string entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter any portion of the remote responder's name (*not* case sensitive), the at-sign ("@"), and any portion of their domain name (i.e., name@domain, *not* case sensitive). The name and domain name strings entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter the at-sign ("@") and any portion of their domain name (i.e., @domain, *not* case sensitive). The domain name string entered *must* be from 1 to 45 characters in length (*not* case sensitive).

|                                                                                                                |                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/209.png) | NOTE: The more characters you provide, the narrower the search will be. |

- Specific Text in a Message—Enter the "X" ("Message contains") search action code and then enter any portion of the message text string. The string can be from 3 to 30 characters in length (including spaces, symbols, and punctuation marks). MailMan prompts you to decide if the text search should be case sensitive. MailMan also prompts you to decide if the search should include:
- Only the original message text
- Only the message responses text
- Both the original message and responses text

|                                                                                                                |                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/210.png) | NOTE: If the string you are searching for is not all on one line in the message/responses, the search will not be able to find it. |

- Minimum Number of Lines in a Message—Enter the "L" ("Minimum Lines of text") search action code. MailMan prompts you to decide the minimum number or lines.

|                                                                                                                |                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/211.png) | REF: For more information on entering names or DUZs, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

Each additional search criterion entered helps limit the search. Therefore, the more search criteria you choose, the more specific the search becomes, resulting in a smaller list of messages from which to choose. All criteria entered *must* be true in order to pass the search test. (This is similar to using the Boolean AND in Internet search engines or program code.)

MailMan displays the entire list of search criteria you've selected. To cancel a single search criterion without having to start over, use the at-sign ("@") to delete the specific search criterion you no longer want.

When you have completed your search criteria, enter "G" (Go search) to start the search.

You are automatically placed in a "virtual basket" in a full-screen view to process any messages found from the search. You can take any action on the messages in this "virtual basket" that you can take in a "real" basket (e.g., read, delete, forward, save, etc.).

To end the query without searching, you can enter "Q" (Quit) or enter the caret ("^") to get out of the Query/Search for Messages option.

Also, when you are using the Classic, Detailed Full Screen, or Summary Full Screen message readers, you can still use the "?string" feature for quick searches inside one basket or the "??string" feature for searching for messages anywhere on the system.

|                                                                                                                |                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/212.png) | REF: For more information on the "?string" or "??string" searches, please refer to the "Text String Search Actions" topic in Chapter 3 in this manual. |

Alternatively, when reading mail in any basket using any of the message readers, use the "Q" action code to query (search for) messages in that mail basket.

|                                                                                                                |                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/213.png) | REF: For more information on the Query (Search for) action code (i.e., "Q"), please refer to the "Query (Search for) Messages in this Basket ("Q") Action" topic in Chapter 3 in this manual. |

### Searching All Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the "Search all messages by subject only" action gives the user the option of searching all messages anywhere on the system by subject text; however, you *must* include the *first* few words of the subject rather than just a phrase contained within the subject text. Also, the search on subject text is case sensitive.

This search option does *not* allow any other search criteria, because the Search all messages by subject only option searches through every mail message stored in the MESSAGE file (#3.9). Thus, if it allowed any phrase contained in the subject or any additional search criteria, the search would be too cumbersome and take too long to complete.

The user will use MailMan to demonstrate searching for a messages located anywhere on the system. For this example, the specific message the user is looking for has the following characteristics:

- Subject—"I'm so excited..."
- Sender—XMUSER2,TWO M.
- Recipients—XMUSER1,ONE E. (and others)
- Responders—XMUSER1,ONE E. (and others)
- Message Sent—11/07/97
- Sample Text Phrase—"...and I just can't hide it!"
- Mail Basket—MailMan
- MailMan Internal Message Identification Number—1190657

The following example shows you how to search all messages in MailMan when looking for a specific message subject beginning with a particular phrase (string):

Select MailMan Menu Option: q \<Enter\> uery/Search for Messages

Select one of the following:

A Search all messages by multiple criteria

M Search my Mailbox by multiple criteria

S Search all messages by subject only

Select message search method: s\<Enter\> Search all messages by subject only

Enter the string that the subject starts with: I'm

Searching...

All Messages Search

\*=New/!=Priority.....................Subject............Lines.From.....Read/Rcvd

1\. \* N/A \* \[1052777\] 07/09/96 I'mmmmmmmm baaaaaa 11 XMUSER22,TWE 1/1

2\. MailMan \[1190657\] 11/07/97 I'm so excited... 59 XMUSER2,TW 736/736

3\. \* N/A \* \[812953\] 12/07/94 I'm bringing in le

4\. \* N/A \* \[944371\] 08/08/95 I'm a Semi-Real Pe

5\. \* N/A \* \[1061294\] 07/24/96 I'm Outta Here!

Search finished.

Enter message number or command:

<span id="_Ref428863714" class="anchor"></span>Figure 6‑2. Search all messages by subject only option

For this example (Figure 6‑2), After the user chose the Query/Search for messages option, the user entered an "S" (Search all messages by subject only) at the "Select message search method:" prompt.

MailMan then prompted the user to enter the first portion of the message subject for which he was searching. In this case, he entered "I'm" at the "Enter the string that the subject starts with:" prompt.

MailMan immediately began to search the entire system looking for all messages in the MESSAGE file (#3.9) whose subject begins with "I'm."

When the search was finished, MailMan placed the user into a "virtual basket" in a full-screen view displaying all of the messages that met the search criteria where he could take any additional actions on the list of messages.

|                                                                                                                |                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/214.png) | REF: For a complete list of action codes you could use, please refer to Table 3‑1 in Chapter 3 in this manual. |

As you can see, MailMan found five messages that all began with "I'm." Four of the messages do not specify a mail basket name (i.e., "N/A"). Those messages with "N/A" beside them are messages located on the system but *not* in any of the user's own mail baskets. Even though the user was a recipient of these other messages at one time, he no longer has them in his mailbox (e.g., he must have deleted or terminated the messages at some point), however, he can now retrieve them.

Based on the characteristic the user stated previously, he was specifically looking for message number 2 in the list. By just entering the first three characters of the subject, MailMan was able to find the message the user wanted and include it in the list of messages found in the search.

If the user had further refined the search by entering more of the subject (e.g., "I'm so"), MailMan would have just found the single message he wanted in the MailMan basket, as shown below:

Select MailMan Menu Option: query \<Enter\> /Search for Messages

Select one of the following:

A Search all messages by multiple criteria

M Search my Mailbox by multiple criteria

S Search all messages by subject only

Select message search method: s \<Enter\> Search all messages by subject only

Enter the string that the subject starts with: I'm so

Searching...

All Messages Search

\*=New/!=Priority.....................Subject............Lines.From.....Read/Rcvd

1\. MailMan \[1190657\] 11/07/97 I'm so excited... 59 XMUSER2,TW 736/736

Search finished.

Enter message number or command:

<span id="_Toc436461127" class="anchor"></span>Figure 6‑3. Search all messages by subject only option—Refining the search

By increasing the subject text from "I'm" to "I'm so" MailMan found the exact message the user was looking for.

### Searching Your Own Mailbox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the "Search my Mailbox only" action gives the user the option of searching all messages located in any of their own mail baskets. This search option gives you the opportunity to search for a message in either:

- All mail Baskets (default)
- Specific Mail Basket

You can use any combination or all of the following search criteria:

- Subject—Phrase contained in the Subject (any portion of the subject).
- Sender—Person who sent the message.
- Addressee/Recipient—Person to whom the message was sent.
- Dates—Choose individual dates or a date range to compare with the date the message was sent (approximately):
- Message sent on or after a certain date.
- Message sent on or before a certain date.
- Responder—Person who has responded to a message.
- Message Text—Phrase contained in the body of the message.

This example demonstrates how MailMan searches for a message that we know exists in one of the baskets in a user's mailbox. For this example, the specific message we are looking for has the following characteristics:

- Subject—"I'm so excited..."
- Sender—XMUSER2,TWO M.
- Recipients—XMUSER1,ONE E. (and others)
- Responders—XMUSER1,ONE E. (and others)
- Message Sent—11/07/97
- Sample Text Phrase—"...and I just can't hide it!"
- Mail Basket—MailMan
- MailMan Internal Message Identification Number—1190657

The following example shows you how to search for messages in any of your mail baskets based on the sender and a date range that the message was sent:

Select MailMan Menu Option: query \<Enter\>/Search for Messages

Select one of the following:

A Search all messages by multiple criteria

M Search my Mailbox by multiple criteria

S Search all messages by subject only

Select message search method: m\<Enter\> Search my Mailbox by multiple criteria

Current 'Mailbox' search criteria:

Search basket: All baskets

Select one of the following:

B Search one basket

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Enter 'Subject contains' string// f\<Enter\> Enter 'Message from' person

Message is from: xmuser2 \<Enter\> ,TWO M. TX PROGRAMMER

Current 'Mailbox' search criteria:

Search basket: All baskets

Message from: XMUSER2,TWO M.

Select one of the following:

B Search one basket

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Change 'Message from' person

G Go Search

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

<span id="_Hlt429361346" class="anchor"></span>Figure 6‑4. Search my Mailbox by multiple criteria option (1 of 2)

Select search action: Go Search// da\<Enter\> Enter 'Message sent on or after' date

Message sent on or after: 11/1/97\<Enter\> (NOV 01, 1997)

Current 'Mailbox' search criteria:

Search basket: All baskets

Message from: XMUSER2,TWO M.

Message sent on or after: 11/01/97

Select one of the following:

B Search one basket

DA Change 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Change 'Message from' person

G Go Search

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Go Search// db\<Enter\> Enter 'Message sent on or before' date

Message sent on or before: (11/1/97 - 8/27/98): 12/1/97\<Enter\> (DEC 01, 1997)

Current 'Mailbox' search criteria:

Search basket: All baskets

Message from: XMUSER2,TWO M.

Message sent on or after: 11/01/97

Message sent on or before: 12/01/97

Select one of the following:

B Search one basket

DA Change 'Message sent on or after' date

DB Change 'Message sent on or before' date

F Change 'Message from' person

G Go Search

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Go Search// \<Enter\>

Searching...

All Baskets Search

\*=New/!=Priority.................Subject..............Lines.From.......Read/Rcvd

1\. comedy \[1190523\] 11/06/97 You, too, can work for 57 XMUSER2,TWO M.

2\. MailMan \[1190657\] 11/07/97 I'm so excited... 59 XMUSER2,TWO 736/736

Search finished.

Enter message number or command:

<span id="_Toc147225907" class="anchor"></span>Figure 6‑5. Search my Mailbox by multiple criteria option (2 of 2)

For the previous example (Figure 6‑4), after the user chose the Query/Search for messages option, she entered an "M" (Search my Mailbox only) at the "Select message search method:" prompt.

MailMan then displayed the current search criteria (i.e., Searching basket: All baskets) and a list of other search criteria from which to choose. For this example, the user entered an "F" (message from) at the "Select search action: Enter 'Subject contains' string//" prompt.

MailMan then prompted the user to enter the sender's name. In this case, she entered "XMUSER2,TWO M." at the "Message is from:" prompt.

MailMan then redisplayed the Current 'Mailbox' search criteria:

- Searching basket: All baskets
- Message from: XMUSER2,TWO M.

MailMan also redisplayed the list of other search criteria from which to choose. The user decided to search for a message within a date range (i.e., 11/1/97 to 12/1/97). Thus, she first entered "DA" (message sent on or after) at the "Select search action: Go Search//" prompt. This would be the beginning date of the date range.

MailMan then prompted the user to enter a date the message was sent on or after. She entered "11/1/97" at the "Message sent on or after:" prompt.

MailMan then redisplayed the Current 'Mailbox' search criteria:

- Searching basket: All baskets
- Message from: XMUSER2,TWO M.
- Message sent on or after: 11/01/97

MailMan also redisplayed the list of other search criteria from which to choose.

Next the user entered "DB" (message sent on or before) at the "Select search action: Go Search//" prompt. This would be the ending date of the date range.

MailMan then prompted the user to enter a date the message was sent on or after. She entered "12/1/97" at the "Message sent on or before: (11/1/97 - 8/27/98):" prompt. MailMan automatically displayed the valid dates from which the user could choose based on the beginning date that she entered previously. The user could choose a date from November 1, 1997 (beginning date) to August 27, 1998 (present date).

Once again, MailMan displayed the Current 'Mailbox' search criteria:

- Searching basket: All baskets
- Message from: XMUSER2,TWO M.
- Message sent on or after: 11/01/97
- Message sent on or before: 12/01/97

At this point, the user had completed the search criteria entries and was ready to start the search. Thus, she pressed the \<Enter\> key to accept the "G" (Go search) default at the "Select search action: Go Search//" prompt and MailMan began searching for all messages that met the search criteria.

When the search was finished, MailMan placed the user into a "virtual basket" in a full-screen view displaying all of the messages that met the search criteria where the user could take any additional actions on the list of messages.

|                                                                                                                |                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/215.png) | REF: For a complete list of action codes you could use, please refer to Table 3‑1 in Chapter 3 in this manual. |

As you can see, MailMan found two messages that fit all of the search criteria.

Based on the characteristic stated previously, the user was specifically looking for message number 2 in the list. By entering the sender and a date range, MailMan was able to find the message the user wanted and include it in the list of messages found in the search.

When you complete your actions on the message(s), press the \<Enter\> key or enter the caret ("^") at the "Enter message number or command:" prompt to go back to the list of search options to further refine or modify your search.

To exit the search option altogether, press the \<Enter\> key to accept the "Q" (Quit) default or enter the caret ("^") at the "Select search action: Q//" prompt to return to the main MailMan Menu.

This example demonstrates how MailMan searches for a message we know exists in a particular mail basket.

For this example, the specific message we are looking for has the following characteristics:

- Subject—"New Test Message"
- Sender—XMUSER1,ONE E.
- Recipients—XMUSER1,ONE E. (and others)
- Responders—XMUSER1,ONE E.
- Message Sent—05/12/98
- Sample Text Phrase—"message created while reading another message"
- Mail Basket—TEST
- MailMan Internal Message Identification Number—1212175

The following example shows you how to search for messages in a specific mail basket based on the responder and a sample text phrase from the body of the message:

Select MailMan Menu Option: q \<Enter\> uery/Search for Messages

Select one of the following:

A Search all messages by multiple criteria

M Search my Mailbox by multiple criteria

S Search all messages by subject only

Select message search method: m\<Enter\> Search my Mailbox by multiple criteria

Current 'Mailbox' search criteria:

Search basket: All baskets

Select one of the following:

B Search one basket

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Enter 'Subject contains' string// b\<Enter\> Search one basket

Select basket to search: IN// TEST

Current 'Mailbox' search criteria:

Search basket: TEST

<span id="_Ref429360798" class="anchor"></span>Figure 6‑6. Search one basket option (1 of 3)

Select one of the following:

B Change Search basket

BA Search all baskets

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Enter 'Subject contains' string// r\<Enter\> Enter 'Response from' person

Response is from: xmuser1 \<Enter\>,ONE E. OX COMPUTER SPECIALIST

Current 'Mailbox' search criteria:

Search basket: TEST

Response from: XMUSER1,ONE E.

Select one of the following:

B Change Search basket

BA Search all baskets

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

G Go Search

L Enter 'Minimum Lines of text' number

Q Quit

R Change 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Go Search// x\<Enter\> Enter 'Message contains' string

Message contains: message created while reading another message

Enter the string to search for. It may be from 3 to 30 characters.

Note that if the string you are searching for is not all on one line

in the message, the search will not be able to find it.

Message contains: message created while reading

Should the search be case-sensitive? YES// ?

Your answer determines whether case (upper/lower) matters in the search.

It also affects the speed of the search.

A case-sensitive search (one in which case matters) is faster.

A case-insensitive search (one in which case does not matter) is slower,

but may find more matches.

Answer 'yes' for a faster search, when case matters.

Answer 'no' for a slower search, when case does not matter.

Should the search be case-sensitive? Yes// \<Enter\>

<span id="_Toc147225909" class="anchor"></span>Figure 6‑7. Search one basket option (2 of 3)

Select one of the following:

1 Message only

2 Message and Responses

3 Responses only

Where should we search: Message only// \<Enter\>

Current 'Mailbox' search criteria:

Search basket: TEST

Response from: XMUSER1,ONE E.

Message contains: message created while reading

Select one of the following:

B Change Search basket

BA Search all baskets

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

G Go Search

L Enter 'Minimum Lines of text' number

Q Quit

R Change 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Change 'Message contains' string

Select search action: Go Search// \<Enter\>

Searching...

TEST Basket Search

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

4\. \[1212175\] 05/12/98 New Test Message 3 XMUSER1,ONE E. 2/2

Search finished.

Enter message number or command: ^

<span id="_Ref106597626" class="anchor"></span>Figure 6‑8. Search one basket option (3 of 3)

For this example (Figure 6‑8), After the user chose the Query/Search for messages option, the user entered an "M" (Search my Mailbox by multiple criteria) at the "Select message search method:" prompt.

For this example, the user wanted to only search one mail basket so he entered "B" (Search one basket) at the "Select search action: Enter 'Subject contains' string//" prompt.

MailMan then prompted the user to choose the mail basket. In this case, he entered "TEST" at the "Select basket to search: IN//" prompt. As you can see, the "IN" basket is the default entry.

|                                                                                                                |                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/216.png) | NOTE: Once you've selected a specific mail basket to search, MailMan gives you the opportunity to later change the selected basket or search all mail baskets. |

MailMan then displayed the current search criteria (i.e., Search basket: TEST) and a list of other search criteria from which to choose.

For this example, the user next entered an "R" (Response from) at the "Select search action: Enter 'Subject contains' string//" prompt.

MailMan then prompted the user to enter the responder's name. In this case, he entered "XMUSER1,ONE E." at the "Response is from:" prompt.

MailMan then redisplayed the Current 'Mailbox' search criteria:

- Search basket: TEST
- Response from: XMUSER1,ONE E.

MailMan also redisplayed the list of other search criteria from which to choose.

The user decided to search for a specific text phrase in the body of the message. Thus, he first entered "X" (Message contains) at the "Select search action: Go Search//" prompt.

The user then entered the phrase "message created while reading another message" at the "Message contains:" prompt. MailMan then informed the user that the entry can only be from 3 to 30 characters in length. Since the entry was 45 characters, the user had to re-enter it (i.e., make it shorter); therefore, the user entered a shorter phrase: "message created while reading" (which is 29 characters in length, including spaces).

MailMan then asked the user if he wanted to make the search case sensitive. The user displayed the Help for this option, which explained that a case-sensitive search is faster. For this example, he decided to make the search case sensitive by accepting the default "Yes" response by pressing the \<Enter\> key at the "Should the search be case-sensitive? YES//" prompt.

Next, MailMan gave the user the opportunity to choose what part of the message should be searched for the text phrase.

You can choose to search for a phrase in any of these three locations:

> 1 Message only

> 2 Message and Responses

> 3 Responses only

For this example, the user chose only to look for the phrase in the body of the message by pressing the \<Enter\> key to accept the default response (i.e., Message only) at the "Where should we search: Message only//" prompt.

MailMan then redisplayed the Current 'Mailbox' search criteria:

- Search basket: TEST
- Response from: XMUSER1,ONE E.
- Message contains: message created while reading

At this point, the user had completed the search criteria entries and was ready to start the search. Thus, he pressed the \<Enter\> key to accept the "G" (Go search) default at the "Select search action: Go Search//" prompt and MailMan began searching for all messages that met the search criteria.

When the search was finished, MailMan placed the user into a "virtual basket" in a full-screen view displaying all of the messages that met the search criteria where the user could take any additional actions on the list of message in that basket.

|                                                                                                                |                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/217.png) | REF: For a complete list of action codes you could use, please refer to Table 3‑1 in Chapter 3 in this manual. |

As you can see, MailMan found only one message that fit all of the search criteria. It was the message the user was looking for based on the characteristic he stated previously. By entering the basket, responder, and a text phrase, MailMan was able to find the message the user wanted and include it in the list of messages found in the search.

When you complete your actions on the message(s), press the \<Enter\> key or enter the caret ("^") at the "Enter message number or command:" prompt to go back to the list of search options to further refine or modify your search.

To exit the search option altogether, press the \<Enter\> key to accept the "Q" (Quit) default or enter the caret ("^") at the "Select search action: Q//" prompt to return to the main MailMan Menu.

Again, this example demonstrates how MailMan searches for a message we know exists in a particular mail basket, however, this time, we will use different search criteria.

For this example, the specific message the user is looking for has the following characteristics:

- Subject—"XU8.0T20#46 MENUMAN: FIND USER ERROR"
- Sender—XMUSER44,FORTY4
- Recipients—G.KERNEL DEVELOPERS (and others)
- Responders—XMUSER44,FORTY4 (and others)
- Message Sent—05/18/95
- Sample Message Text Phrase—"This is very strange one."
- Mail Basket—Kernel
- MailMan Internal Message Identification Number—926007

The following example shows you how to search for messages in a specific mail basket based on the subject and to whom the message was sent:

Select MailMan Menu Option: query \<Enter\> /Search for Messages

Select one of the following:

A Search all messages by multiple criteria

M Search my Mailbox by multiple criteria

S Search all messages by subject only

Select message search method: m\<Enter\> Search my Mailbox by multiple criteria

Current 'Mailbox' search criteria:

Search basket: All baskets

Select one of the following:

B Search one basket

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Enter 'Subject contains' string// b\<Enter\> Search one basket

Select basket to search: IN// Kernel

Current 'Mailbox' search criteria:

Search basket: Kernel

Select one of the following:

B Change Search basket

BA Search all baskets

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Enter 'Message to' addressee

X Enter 'Message contains' string

Select search action: Enter 'Subject contains' string// t \<Enter\> Enter 'Message to' addressee

Message to: g.kernel \<Enter\> DEVELOPERS

Current 'Mailbox' search criteria:

Search basket: Kernel

Message to: G.KERNEL DEVELOPERS

<span id="_Ref429882948" class="anchor"></span>Figure 6‑9. Search one basket for mail sent to a group (1 of 2)

Select one of the following:

B Change Search basket

BA Search all baskets

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

G Go Search

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Change 'Message to' addressee

X Enter 'Message contains' string

Select search action: Go Search// s\<Enter\> Enter 'Subject contains' string

Subject contains: menuman

Current 'Mailbox' search criteria:

Search basket: Kernel

Subject contains: menuman

Message to: G.KERNEL DEVELOPERS

Select one of the following:

B Change Search basket

BA Search all baskets

DA Enter 'Message sent on or after' date

DB Enter 'Message sent on or before' date

F Enter 'Message from' person

G Go Search

L Enter 'Minimum Lines of text' number

Q Quit

R Enter 'Response from' person

S Enter 'Subject contains' string

T Change 'Message to' addressee

X Enter 'Message contains' string

Select search action: Go Search// \<Enter\> o search

Searching...

Kernel Basket Search

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

33\. \[930602\] 06/12/95 XU8.0T20#75 MENUMAN ERROR O 24 XMUSER44,FORTY4 7/7

27\. \[926007\] 05/18/95 XU8.0T20#46 MENUMAN: FIND U 80 XMUSER44,FORTY4 3/3

23\. \[924447\] 05/10/95 XU8.0T20#35 MENUMAN AND NON 65 XMUSER44,FORTY4 15/15

Search finished.

Enter message number or command:

<span id="_Ref106598048" class="anchor"></span>Figure 6‑10. Search one basket for mail sent to a group (2 of 2)

For this example (Figure 6‑10), After the user chose the Query/Search for messages option, the user entered an "M" (Search my Mailbox by multiple criteria) at the "Select message search method:" prompt.

In this case, the user wanted to only search one mail basket so she entered "B" (Search one basket) at the "Select search action: Enter 'Subject contains' string//" prompt.

MailMan then prompted the user to choose the mail basket. She entered "Kernel" at the "Select basket to search: IN//" prompt. As you can see (Figure 6‑9), the "IN" basket is the default entry. As with entering any MailMan user or group name, the user only has to enter the first portion of the mail basket name (*not* case sensitive); MailMan will find the appropriate basket based on the partial entry and automatically displayed the rest of the basket name to the user. If more than one basket is found based on that partial entry, MailMan would allow the user to choose from a list of basket names. You'll narrow your choices by entering more characters.

|                                                                                                                |                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/218.png) | NOTE: Once you've selected a specific mail basket to search, MailMan gives you the opportunity to later change the selected basket or search all mail baskets. |

MailMan then displayed the current search criteria (i.e., Search basket: Kernel) and a list of other search criteria from which to choose.

The user next entered a "T" (Message to) at the "Select search action: Enter 'Subject contains' string//" prompt and MailMan prompted her to enter the addressee's name. In this case, the user entered the first portion of the "G.KERNEL DEVELOPERS" group name at the "Message to:" prompt.

MailMan then redisplayed the Current 'Mailbox' search criteria:

- Search basket: Kernel
- Message to: G.KERNEL DEVELOPERS

MailMan also redisplayed the list of other search criteria from which to choose.

The user decided to also search for a specific text phrase in the subject of the message. Thus, she first entered "S" (Subject contains) at the "Select search action: Go Search//" prompt. She then entered "menuman" at the "Subject contains:" prompt. The subject search is *not* case sensitive.

MailMan then redisplayed the Current 'Mailbox' search criteria:

- Search basket: Kernel
- Subject contains: menuman
- Message to: G.KERNEL DEVELOPERS

At this point, the user had completed the search criteria entries and was ready to start the search. Thus, she pressed the \<Enter\> key to accept the "G" (Go search) default at the "Select search action: Go Search//" prompt and MailMan began searching for all messages that met the search criteria.

When the search was finished, MailMan placed the user into a "virtual basket" in a full-screen view displaying all of the messages that met the search criteria where she could take any additional actions on the list of message in that basket.

|                                                                                                                |                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/219.png) | REF: For a complete list of action codes you could use, please refer to Table 3‑1 in Chapter 3 in this manual. |

As you can see, MailMan found three messages that fit all of the search criteria. Based on the characteristic the user stated previously, she was specifically looking for message number 27 in the list. By entering the basket, addressee (group name), and a portion of the subject, MailMan was able to find the message the user wanted and include it in the list of messages found in the search.

When you complete your actions on the message(s), press the \<Enter\> key or enter the caret ("^") at the "Enter message number or command:" prompt to go back to the list of search options to further refine or modify your search.

To exit the search option altogether, press the \<Enter\> key to accept the "Q" (Quit) default or enter the caret ("^") at the "Select search action: Q//" prompt to return to the main MailMan Menu.

# Filtering Mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics to be discussed in this chapter:

- Message Filter Edit Option
- Filtering Criteria
- Establishing Filter Order
- Create a New Mail Filter
- Edit an Existing Mail Filter
- Modify a Mail Filter and Filter Messages in a Basket
- Delete a Mail Filter

MailMan V. 8.0 allows you to filter your mail. MailMan can use message filters, created by you, to assist you with organizing your mail.

You can think of MailMan and message filters as performing the duties of an "executive assistant," such as sorting through all of the incoming mail before it reaches your "desk." These filters screen and categorize your mail, directing it to mail baskets you specify based on certain criteria. They can also help you prioritize the relevant mail and discard your unwanted mail ("junk mail") by sending it directly to the "WASTE" basket or any other mail basket.

|                                                   |                                                                                                                                                                                                                              |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/220.png) | TIP: Use mail filters to help automatically "sort" your mail. For example, create a filter to automatically direct mail messages sent by any member of a project team to the appropriate project basket in your mailbox. |

The features and functionality associated with filtering messages are described in greater detail in this chapter.

### Message Filter Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan interface provides the Message Filter Edit option for you to create mail filters. It is located on the Personal Preferences menu, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: personal \<Enter\> Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit \[XM FILTER EDIT\]

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option:

<span id="_Toc436461131" class="anchor"></span>Figure 7‑1. Message Filter Edit option

Filtering takes place during message delivery. Filtering can also be selected as a basket action.

|                                                                                                                |                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/221.png) | REF: For more information on filtering messages as a basket action, please refer to the "Filter Messages ("FI") Action" topic in Chapter 3, "Reading/Managing Messages—In a Basket," in this manual. |

Also, when you create a mail filter and specify a mail basket that does *not* currently exist in your mailbox, MailMan will allow you to create it on the fly. Also, if you later delete a filter mail basket, MailMan will automatically recreate it for you when the filter is used (activated) and mail is directed to that basket.

|                                                                                                                |                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/222.png) | NOTE: MailMan will not allow you to designate "IN" as a filter basket, because that is the default delivery basket. |

In addition to setting the filtering criteria, when you want MailMan to use a specific filter, the following conditions *must* be met:

- FILTER MESSAGES?—Filtering *must* be turned on for your mailbox (i.e., FILTER MESSAGES? field set to "Yes").
- STATUS—The filter's status *must* be active (i.e., STATUS field set to "On").
- ORDER—The filter *must* be the *first* filter (i.e., controlled by the ORDER field) whose criteria matches the message characteristics (i.e., subject contents, sender of the message, and/or message addressee)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/223.png)</td>
<td><strong>REF:</strong> For more information on the Order field, please refer to the "Establishing Filter Order" topic that follows in this chapter.<br />
<br />
Also, for more information on filter criteria, please refer to the "Filtering Criteria" topic that follows in this chapter.</td>
</tr>
</tbody>
</table>

Mail filters are ignored during delivery under the following conditions:

- Message Already Exists—The message already exists in one of your mail baskets.
- Delivery Basket Specified—The message was sent with a delivery basket specified and you have set your delivery basket privileges to accept delivery to the specified basket (overrides your mail filters).

|                                                                                                                |                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/224.png) | REF: For more information on setting your delivery basket privileges, please refer to the "Set Your Delivery Basket Privileges" topic in Chapter 3 in the *MailMan Getting Started Guide*. |

- Message Sent by You—The message is from yourself, and you specified a basket (other than the "IN" basket) at the transmit prompt.

Even if you have created mail filters, you can turn filtering on or off at any time by, again, using the Message Filter Edit option located on the Personal Preferences menu. If you've turned filtering off, MailMan will ignore any mail filters and deliver your mail as usual.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/225.png) | CAUTION: MailMan's background processing checks active mail filters for *each* recipient, *prior* to delivery. This can be cumbersome for MailMan when a message has numerous recipients and each recipient has numerous *active* mail filters. Thus, to make the delivery process more efficient for everyone, we suggest you *limit* the number of *active* filters for your mailbox, use the least amount of filtering criteria necessary to positively identify the message, and prioritize each filter by using the ORDER field. Those filters that will be used the most should be given the highest priority (e.g., ORDER equals one, two, or three). |

### Filtering Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Filter Edit option allows you to set up standing instructions to MailMan as to which baskets you would like certain messages delivered. This can be based on *any* number of the following three criteria:

- Subject Contains—Subject of the message. The string *must* be from 3 to 25 characters in length and can appear anywhere in the subject (*not* case sensitive).
- From—The name of the person who sent the message (partial matching possible). If it is a local person, enter the first portion of the sender's last name (*not* case sensitive) or their local DUZ (i.e., numeric user ID).

> For senders at a remote location (*not* located at your site), do any of the following:

- Enter any portion of the remote sender's name followed by the at-sign ("@", i.e., name@). The name string entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter any portion of the remote sender's name, the at-sign ("@"), and any portion of their domain name (i.e., name@domain). The name and domain name strings entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter the at-sign ("@") and any portion of their domain name (i.e., @domain). The domain name strings entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Addressed To—Addressee of the message. This includes users and mail groups. MailMan will check the addressees that you see when you Query (Q) the message. MailMan will *not* check the expanded list of addresses that you see when you use the Query Detailed (QD) action code.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/226.png)</td>
<td><p><strong>REF:</strong> For more information on the Query action (Q), please refer to the "Query ("Q") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual.</p>
<p>Also, for more information on the Query Detailed ('QD') action, please refer to the "Query Detailed ("QD") Action" in Chapter 4 in this manual.</p></td>
</tr>
</tbody>
</table>

> If it is a local person, enter the first portion of the addressee's last name (*not* case sensitive) or their local DUZ (i.e., numeric user ID).

> For addressees at a remote location (*not* located at your site), do any of the following:

- Enter any portion of the remote addressee's name followed by the at-sign ("@", i.e., name@). The name string entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter any portion of the remote addressee's name, the at-sign ("@"), and any portion of their domain name (i.e., name@domain). The name and domain name strings entered *must* be from 1 to 45 characters in length (*not* case sensitive).
- Enter the at-sign ("@") and any portion of their domain name (i.e., @domain). The domain name strings entered *must* be from 1 to 45 characters in length (*not* case sensitive).

|                                                                                                                |                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/227.png) | NOTE: If any part of the subject matches your subject filter, the filter will be used (activated). The more characters you provide, the more precise the filter will be. MailMan automatically capitalizes your entries to these prompts in order to facilitate the filtering process. |

|                                                                                                                |                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/228.png) | REF: For more information on entering names or DUZs, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

For the filter to take effect, all criteria entered *must* be true (i.e., match the characteristics of the message). For example, if you specify the "SUBJECT CONTAINS" *and* "FROM," the filter takes effect only if the subject of the message contains the string you specified in the SUBJECT CONTAINS field *and* the message is from the person you specified in the FROM field.

If you wish the filter to take effect upon either "SUBJECT CONTAINS" *or* "FROM," you must create two *separate* filters: one with "SUBJECT CONTAINS" and another with "FROM" as your filter criteria.

### Establishing Filter Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A message may match several filters, depending on the conditions (filtering criteria) you have set. The ORDER field is used to determine in which order filters will be checked. It is here that you specify relative filter priority. The value entered *must* be a whole number between 1 and 999 (no decimal digits). All filters are checked in numeric order. If several filters have the same number, then the first one you entered receives priority.

For example, if you have more than one filter established with similar filtering conditions, the ORDER number tells MailMan which filter is checked first:

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Filter Name</strong></th>
<th><strong>Order</strong></th>
<th><strong>Basket</strong></th>
<th><strong>Status</strong></th>
<th><strong>Subject Contains</strong></th>
<th><strong>From</strong></th>
<th><strong>Addressed To</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Filter_1</td>
<td>1</td>
<td>Team 1</td>
<td>On</td>
<td><p>No Entry</p>
<p>(null)</p></td>
<td><p>No Entry</p>
<p>(null)</p></td>
<td>G.TEAM1</td>
</tr>
<tr class="even">
<td>Filter_2</td>
<td>2</td>
<td>Supervisor</td>
<td>On</td>
<td><p>No Entry</p>
<p>(null)</p></td>
<td>Name A (Supervisor)</td>
<td>G.TEAM1</td>
</tr>
</tbody>
</table>

<span id="_Ref106620355" class="anchor"></span>Table 7‑1. Comparison table showing filter order

For this example (Table 7‑1), let's assume the user belongs to the G.TEAM1 mail group, has turned filtering on, and has established two active mail filters (i.e., Filter_1 and Filter_2). As you can see here, the filters have very similar filtering conditions set. Both filters use the ADDRESSED TO criteria to filter mail. Also, one of the two filters (i.e., Filter_2) uses the FROM criteria (i.e., From Name A, Supervisor). When a message is sent to the G.TEAM1 mail group, MailMan will check the message characteristics against the active mail filters in numerical order and deliver the mail to the specified mail basket.

If the Supervisor (Name A) for Team 1 sends a message to the G.TEAM1 mail group, MailMan will use the Filter_1 filter instead of the Filter_2 filter, because Filter_1's ORDER number (i.e., "1") is higher than Filter_2's ORDER number (i.e., "2"). Thus, in this case, MailMan will deliver the message to the "Team 1" basket. In this case, since the message was from the Supervisor, it would have been more appropriate for the message to have gone through the Filter_2 filter to be delivered to the "Supervisor" basket. Filter_1 does not screen who sent the message, it automatically sends all messages addressed to the G.TEAM1 mail group to the Team 1 basket.

In this case, to fine-tune the filter criteria to appropriately deliver the Supervisor's message to the "Supervisor" basket, the user should reverse the ORDER number of the filters so that the filter expecting messages from the supervisors comes first. Thus, the user would demote Filter_1's ORDER from "1" to "2" and promote Filter_2's ORDER from "2" to "1."

### Create a New Mail Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the following example (Figure 7‑2), the user wanted to create a new mail filter called "Broadcast" that would automatically deliver all messages from the Postmaster with the word "broadcast" in the subject to a mail basket called "Broadcast" (e.g., Subject: 09/09/98 VACO BROADCAST, From: POSTMASTER.FORUM@FORUM.VA.GOV).

To create this new mail filter, use the Message Filter Edit option available on the Personal Preferences menu, as shown below:

Select MailMan Menu Option: personal \<Enter\> Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option: message \<Enter\> Filter Edit

FILTER MESSAGES?: YES// \<Enter\>

Select FILTER: Trans Assistant// Broadcast

Are you adding 'Broadcast' as a new FILTER (the 3RD for this MAILBOX)? No// y \<Enter\> (Yes)

ORDER: 3

BASKET: Broadcast

Are you adding 'Broadcast' as a new BASKET (the 78TH for this MAILBOX)? No// y \<Enter\> (Yes)

STATUS: 1\<Enter\> ON

SUBJECT CONTAINS: ??

If the subject contains the string you specify AND if the message matches

the other conditions (if any), then the message matches this filter.

The subject is capitalized automatically to facilitate filtering.

SUBJECT CONTAINS: broadcast

FROM: POSTMASTER.FORUM@FORUM.VA.GOV

ADDRESSED TO: \<Enter\>

VAPORIZE DAYS: \<Enter\>

DELIVER NEW?: \<Enter\>

Select FORWARD TO: ??

You may enter a new FORWARD TO, if you wish

Enter the person, group, device, or server to whom or to which the

message is to be forwarded. The message will be forwarded under

the following conditions, and you will be listed as the forwarder.

This will only apply when:

\- delivering a message to you for the first time.

This will not apply when:

\- you sent the message.

\- the message is already in your mailbox.

\- delivering replies.

\- the message is closed, confidential, or otherwise sensitive.

Select FORWARD TO: \<Enter\>

Select FILTER: \<Enter\>

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option:

<span id="_Ref429895364" class="anchor"></span>Figure 7‑2. Creating a new mail filter

After the user chose the Message Filter Edit option on the Personal Preferences menu (Figure 7‑2), MailMan asked the user if he wanted to filter the mail. Since he did, he accepted the "Yes" default by pressing the \<Enter\> key at the "FILTER MESSAGES?: YES//" prompt.

MailMan then asked the user to choose a message filter. Since he had previously established mail filters, MailMan displayed the last mail filter the user created as the default response (i.e., "Trans Assistant"). For this example, the user wanted to create a new filter called "Broadcast," thus, he entered "Broadcast" at the "Select FILTER: Trans Assistant//" prompt.

MailMan verified that this was a new filter and asked the user to confirm the entry. He confirmed the new filter name by entering "Yes" at the "Are you adding 'Broadcast' as a new FILTER (the 3RD for this MAILBOX)? No//" prompt.

MailMan then asked the user to choose the new mail filter's order (priority). Since this was the third filter, he decided to set its ORDER to three. Thus, he entered "3" at the "ORDER:" prompt.

MailMan then wanted the user to select the delivery basket to receive the mail that matched this filter's criteria. For this example, he wanted to send mail to a new mail basket called "Broadcast." After entering "Broadcast" at the "BASKET:" prompt, MailMan asked the user to confirm that he wanted to create a new mail basket. The user confirmed the new basket by entering "Yes" at the "Are you adding 'Broadcast' as a new BASKET (the 78TH for this MAILBOX)? No//" prompt.

MailMan then asked the user if he wanted to make the filter active (turned on). Since he did want this filter to be active, he entered a "1" at the "STATUS:" prompt. Alternatively, the user could have entered the word "On" (*not* case sensitive).

At this point, MailMan started prompting the user to enter the filtering criteria. The first filtering criterion is SUBJECT CONTAINS. The user displayed the Help for this prompt by entering two question marks ("??") at the "SUBJECT CONTAINS:" prompt. For this example, the user wanted to filter messages with the word "broadcast" in the subject so he entered "broadcast" at the "SUBJECT CONTAINS:" prompt. MailMan automatically converts the entry to all uppercase.

The next filtering criterion was the "FROM" field. For this example, he entered "POSTMASTER.FORUM@FORUM.VA.GOV" at the "FROM:" prompt.

The user pressed the \<Enter\> key at the "ADDRESSED TO:" prompt without entering any additional text.

The next selection was "VAPORIZE DAYS." You can set the message to automatically vaporize (be deleted from your mailbox) this many days after it is delivered to you. This date will override any vaporize date set by the sender. You will be able to change or delete the vaporize date at the message action prompt whenever you read the message. If this field is null, the filter will not set any vaporize date. This will only apply to new messages and responses that are put into your mailbox (including moving from the WASTE basket) as a result of delivery or latering. It will not to apply messages that are already in your mailbox.

Next MailMan asked "DELIVER NEW?" If you do not answer, or delete the answer, the default is YES.

- YES means that the message will be delivered as usual, and made new as usual.
- NO means that the message will be delivered as usual, but it will not be made new, so you will not know it has arrived unless you check.

This will only apply to new messages that you have *not* seen before. It will *not* apply to responses or forwarded messages with responses. Also, it will *not* apply when you filter messages that are already in your mailbox.

Next MailMan asked "Select FORWARD TO:" You may enter a new FORWARD TO, if you wish. Enter the person, group, device, or server to whom or to which the message is to be forwarded. The message will be forwarded under the following conditions, and you will be listed as the forwarder:

- This will only apply when delivering a message to you for the first time.
- This will *not* apply when:
- You sent the message.
- The message is already in your mailbox.
- Delivering replies.
- The message is closed, confidential, or otherwise sensitive..

Last, MailMan prompted the user to enter the next filter. Since he did not want to create another filter, he pressed the \<Enter\> key at the "Select FILTER:" prompt and MailMan returned the user to the Personal Preferences menu.

### Edit an Existing Mail Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit an existing mail filter, use the Message Filter Edit option available on the Personal Preferences menu, as shown below:

Select Personal Preferences Option: message \<Enter\> Filter Edit

FILTER MESSAGES?: YES// \<Enter\>

Select FILTER: Broadcast// \<Enter\>

FILTER: Broadcast// \<Enter\>

ORDER: 3// 999

BASKET: Broadcast// \<Enter\>

STATUS: ON// \<Enter\>

SUBJECT CONTAINS: BROADCAST// \<Enter\>

FROM: POSTMASTER.FORUM@FORUM.VA.GOV Replace \<Enter\>

ADDRESSED TO: xmuser1 \<Enter\> ,ONE E. OX COMPUTER SPECIALIST

VAPORIZE DAYS: \<Enter\>

DELIVER NEW?: \<Enter\>

Select FORWARD TO: \<Enter\>

Select FILTER: \<Enter\>

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option:

<span id="_Ref429905748" class="anchor"></span>Figure 7‑3. Editing an existing mail filter

In this example (Figure 7‑3), the user wanted to modify the "Broadcast" filter he just created (Figure 7‑2). In this case, he wanted to change the "Broadcast" filter's order and add to the filtering criteria (i.e., ADDRESSED TO).

The current filtering criteria for the "Broadcast" filter consisted of the following:

- SUBJECT CONTAINS: BROADCAST
- FROM: POSTMASTER.FORUM@FORUM.VA.GOV

After entering the Message Filter Edit option, the user pressed the \<Enter\> key accepting the default responses until he got to the ORDER prompt for the "Broadcast" filter. For this example, the user wanted to change the filter's order from the third filter to be checked to the last filter that was checked by entering "999" (maximum order number) at the "ORDER: 3//" prompt.

The user then continued to press the \<Enter\> key until he reached the "ADDRESSED TO:" prompt that followed the previous filter criteria. For this example, in addition to the previous filtering criteria, the user also wanted to filter messages that were addressed specifically to him and not a mail group. Thus, he entered the first portion of the last name (i.e., "xmuser1") at the "ADDRESSED TO:" prompt.

The new filtering criteria were as follows:

- SUBJECT CONTAINS: BROADCAST
- FROM: POSTMASTER.FORUM@FORUM.VA.GOV
- ADDRESSED TO: XMUSER1,ONE E.

The user then continued to press the \<Enter\> key until MailMan prompted him to enter the next filter, if any. Because the user did not want to modify or create another filter, he pressed the \<Enter\> key at the "Select FILTER:" prompt and MailMan returned the user to the Personal Preferences menu.

### Modify a Mail Filter and Filter Messages in a Basket

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following series of screen captures (Figure 7‑4, Figure 7‑5, and Figure 7‑6) better illustrates how to review and modify a filter based on a message's characteristics and then filter messages in a basket so they are passed through the modified filter.

Based on the filter the user created in Figure 7‑2 and modified in Figure 7‑3, he wanted MailMan to deliver all messages with the word "broadcast" in the subject to a new mail basket called "Broadcast" (e.g., Subject: 09/09/98 VACO BROADCAST, From: POSTMASTER.FORUM@FORUM.VA.GOV). The user, however, discovered that some messages did *not* seem to properly use that filter and were still being delivered to the "IN" basket, as shown below:

Select MailMan Menu Option: nml\<Enter\> New Messages and Responses

Select New mail option: Read new mail by basket// ln \<Enter\> List all New messages

All Baskets, New messages: 3

\*=New/!=Priority...........Subject..................Lines.From.........Read/Rcvd

\*1. IN \[1228357\] 09/09/98 09/09/98 VACO BROADCAST 14 \<POSTMASTER.FORUM@FORU

\*2. IN \[1228321\] 09/08/98 Changes to routines 6 \<POSTMASTER@NXT.KERNEL

\*3. IN \[1228261\] 09/08/98 NEW DESKTOP SUPPORT EMPLOY 7 XMUSER10,TEN 3/4

Enter message number or command: 1

Subj: 09/09/98 VACO BROADCAST \[#1228357\] 09/09/98@08:00 EDT 14 lines

From: \<POSTMASTER.FORUM@FORUM.VA.GOV\> In 'Broadcast' basket.

Automatic Deletion Date: Sep 16, 1998 Page 1 \*New\*

-----------------------------------------------------------------------------------

Enter message action (in IN basket): IGNORE// q

Subj: 09/09/98 VACO BROADCAST \[#1228357\] 09/09/98@08:09 EDT 14 lines

From: \<POSTMASTER.FORUM@FORUM.VA.GOV\> In 'IN' basket.

Automatic Deletion Date: Sep 16, 1998

Local Message-ID: 1228357@REDACTED.VA.GOV (2 Recipients) Closed.

'Information only' for all recipients. Automatic Deletion Date: Sep 16, 1998

This message was addressed as follows:

\* (Broadcast to all local users)

S.XMYB-BROADCAST-VA-WIDE

Enter message action (in Broadcast basket): IGNORE//

<span id="_Ref429962882" class="anchor"></span>Figure 7‑4. Determining why a message did not get filtered (1 of 3)

As you can see from this first example in the series (Figure 7‑4), the user first chose the New Messages and Responses option (NML) and listed the new messages in the "IN" basket by entering an "LN" at the "Select New mail option: Read new mail by basket//" prompt.

After MailMan displayed the list of new messages in the user's mailbox, he noticed that message number 1 in the "IN" basket has the word "BROADCAST" in its subject and is from the POSTMASTER.FORUM@FORUM.VA.GOV. Since the message was delivered to the "IN" basket and *not* the "Broadcast" basket he had intended, it must *not* have properly used the modified "Broadcast" filter.

The user previously modified the Broadcast filter to deliver messages to the "Broadcast" basket with the following filtering criteria (Figure 7‑3):

- SUBJECT CONTAINS: BROADCAST
- FROM: POSTMASTER.FORUM@FORUM.VA.GOV
- ADDRESSED TO: XMUSER1,ONE E.

The "ADDRESSED TO field had been changed from no entry (null) to XMUSER1,ONE E. Also, the filter's ORDER had been changed from 3 to 999. Since the change in the ADDRESSED TO field is one of the filtering criteria and the ORDER field is not, the user decided to verify to whom the message was being delivered. Thus, he first entered "1" at the "Enter message number or command:" prompt in order to select the message.

Once the message was displayed, he entered a "Q" (Query) at the "Enter message action (in IN basket): IGNORE//" prompt. MailMan displayed the summary address information of the message. Thus, the message characteristics were as follows:

- SUBJECT CONTAINS: BROADCAST
- FROM: POSTMASTER.FORUM@FORUM.VA.GOV
- ADDRESSED TO: \* (broadcast message to all local users)

The user noticed that the message was *not* specifically addressed to XMUSER1,ONE E. but to *all* local users ("\*"). Therefore, by modifying the filter to only look for messages addressed to XMUSER1,ONE E., the filter was *not* being used by MailMan to deliver the message to the "Broadcast" basket.

|                                                                                                                |                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/229.png) | REF: For more information on the Query action (Q), please refer to the "Query ("Q") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

To modify a mail filter to properly filter the "Broadcast" messages, the user, again, used the Message Filter Edit option available on the Personal Preferences menu, as shown below:

Select Personal Preferences Option: message \<Enter\> Filter Edit

FILTER MESSAGES?: YES// \<Enter\>

Select FILTER: Broadcast// \<Enter\>

FILTER: Broadcast// \<Enter\>

ORDER: 999// \<Enter\>

BASKET: Broadcast// \<Enter\>

STATUS: ON// \<Enter\>

SUBJECT CONTAINS: BROADCAST// \<Enter\>

FROM: POSTMASTER.FORUM@FORUM.VA.GOV Replace \<Enter\>

ADDRESSED TO: XMUSER1,ONE E.// @

SURE YOU WANT TO DELETE? y\<Enter\> (Yes)

VAPORIZE DAYS: \<Enter\>

DELIVER NEW?: \<Enter\>

Select FORWARD TO: \<Enter\>

Select FILTER: \<Enter\>

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option:

<span id="_Hlt429976294" class="anchor"></span>Figure 7‑5. Modifying a filter so it will properly deliver a message (2 of 3)

In this second example of the series (Figure 7‑5), the current filtering criteria for the "Broadcast" filter consisted of the following:

- SUBJECT CONTAINS: BROADCAST
- FROM: POSTMASTER.FORUM@FORUM.VA.GOV
- ADDRESSED TO: XMUSER1,ONE E.

After entering the Message Filter Edit option, the user pressed the \<Enter\> key accepting the default responses for the "Broadcast" filter until he got to the "ADDRESSED TO:" prompt that followed the previous filter criteria.

For this example, the user wanted to remove the ADDRESSED TO field from the filtering criteria for the "Broadcast" filter. Thus, the user entered an at-sign ("@") at the "ADDRESSED TO: XMUSER1,ONE E.//" prompt. MailMan asked him to confirm that he wanted to delete the value in this field. He confirmed the delete by entering "Yes" at the "SURE YOU WANT TO DELETE?" prompt.

Thus, the new filtering criteria are as follows:

- SUBJECT CONTAINS: BROADCAST
- FROM: POSTMASTER.FORUM@FORUM.VA.GOV

MailMan then prompted the user to enter the remaining filtering criteria, since the user did not want to change anything else, he continued to press the \<Enter\> key until he got to the "Select FILTER:" prompt. Because he did not want to modify or create another filter, he, again, pressed the \<Enter\> key and MailMan returned him to the Personal Preferences menu.

Now that the user has modified the "Broadcast" filter, he wants to pass the messages in his "IN" basket back through the updated filters. Thus, the "Broadcast" messages will be automatically moved to the "Broadcast" mail basket, as shown below:

Select MailMan Menu Option: nml\<Enter\> New Messages and Responses

Select New mail option: Read new mail by basket// ln \<Enter\> List all New messages

All Baskets, New messages: 3

\*=New/!=Priority...........Subject..................Lines.From.........Read/Rcvd

\*1. IN \[1228357\] 09/09/98 09/09/98 VACO BROADCAST 14 \<POSTMASTER.FORUM@FORU

\*2. IN \[1228321\] 09/08/98 Changes to routines 6 \<POSTMASTER@NXT.KERNEL

\*3. IN \[1228261\] 09/08/98 NEW DESKTOP SUPPORT EMPLOY 7 XMUSER10,TEN 3/4

Enter message number or command: fi

Filter which messages: (1-3): 1-3

3 messages filtered.

Press RETURN to continue: \<Enter\>

All Baskets, New messages: 3

\*=New/!=Priority...........Subject...................Lines.From.........Read/Rcvd

\*1. Br \[1228357\] 09/09/98 09/09/98 VACO BROADCAST 14 \<POSTMASTER.FORUM@FORU

\*2. IN \[1228321\] 09/08/98 Changes to routines 6 \<POSTMASTER@NXT.KERNEL

\*3. IN \[1228261\] 09/08/98 NEW DESKTOP SUPPORT EMPLOY 7 XMUSER10,TEN 3/4

Enter message number or command:

<span id="_Ref429965916" class="anchor"></span>Figure 7‑6. Using the basket filtering tool to properly filter messages (3 of 3)

As you can see from this third and final example in the series (Figure 7‑6), the user, again, chose the New Messages and Responses option (NML) and listed the new messages in their mailbox by entering an "LN" at the "Select New mail option: Read new mail by basket//" prompt.

MailMan displayed the list of the new messages. You'll notice that message number 1 is currently located in the "IN" basket. Since the user wanted to filter these messages, he entered "FI" (Filter) at the "Enter message number or command:" prompt.

MailMan asked the user which messages he wanted to pass through the filters. In this case, the user chose to pass all the *new* messages in their mailbox through the filters. Thus, he entered "1-3" at the "Filter which messages: (1-3):" prompt.

When finished, MailMan informed the user that the messages had been filtered. Pressing the \<Enter\> key told MailMan to redisplay the list of new messages in the user's mailbox after they had been passed through the filters.

The user previously modified the "Broadcast" filter to deliver messages to the "Broadcast" basket with the following filtering criteria (Figure 7‑5):

- SUBJECT CONTAINS: BROADCAST
- FROM: POSTMASTER.FORUM@FORUM.VA.GOV

Prior to the filtering, the first message in the list (#1) had the following characteristics:

- Mail Basket: "IN"
- Subject: "09/09/98 VACO BROADCAST"
- From: "POSTMASTER.FORUM@FORUM.VA.GOV"

After the filtering, the first message in the list (#1) now had the following characteristics:

- Mail Basket: "Br" (abbreviation for "Broadcast" due to space limitations)
- Subject: "09/09/98 VACO BROADCAST"
- From: "POSTMASTER.FORUM@FORUM.VA.GOV"

Thus, by adjusting the "Broadcast" filter and running the messages back through the filters, MailMan properly delivered (moved) the messages from the "IN" basket to the "Broadcast" basket.

|                                                                                                                |                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/230.png) | REF: For more information on filtering messages as a basket action, please refer to the "Filter Messages ("FI") Action" topic in Chapter 3 in this manual. |

### Delete a Mail Filter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To delete a mail filter, use the Message Filter Edit option available on the Personal Preferences menu and use the at-sign ("@"), as shown below:

Select Personal Preferences Option: message \<Enter\> Filter Edit

FILTER MESSAGES?: YES// \<Enter\>

Select FILTER: Broadcast// @

SURE YOU WANT TO DELETE THE ENTIRE 'Broadcast' FILTER? y\<Enter\> (Yes)

Select FILTER: ^

<span id="_Toc436461137" class="anchor"></span>Figure 7‑7. Deleting a mail filter

After entering the Message Filter Edit option, the user pressed the \<Enter\> key until he got to the "Select FILTER:" prompt. MailMan displayed the last filter edited as the default filter (i.e., "Broadcast").

For this example, the user wanted to delete the "Broadcast" filter. Thus, he entered an at-sign ("@") at the "Select FILTER: Broadcast//" prompt. MailMan asked the user to confirm that he wanted to delete the entire "Broadcast" filter. The user confirmed the delete by entering "Yes" at the "SURE YOU WANT TO DELETE THE ENTIRE 'Broadcast' FILTER?" prompt.

MailMan then prompted the user to choose another filter. Because the user did not want to modify, create, or delete another filter, he entered the caret ("^") at the "Select FILTER:" prompt.

|                                                   |                                                                                                                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/231.png) | TIP: You do not necessarily have to delete a filter, you can simply turn it off (i.e., STATUS = Off). Thus, if you want to use the filter again, you will not have to recreate it; you just have to turn it back on. |

# Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics to be discussed in this chapter:

- Mail Group Options
- Enroll in Mail Groups
- Disenroll From Mail Groups
- Personal Mail Groups

Mail groups consist of MailMan users (members) with similar interests in a particular topic. Mail groups provide a forum for group discussion where members can share ideas and concepts related to the group.

As a member of a mail group, you, along with other members, receive messages directed to that mail group. One can address a message to a group of recipients without having to specify them individually by name. Thus, whenever mail is repeatedly sent to the same list of recipients, users can save time by putting them in mail groups.

Members can be added or removed at any time. They can be local and remote users (including fax recipients), other mail groups, or distribution lists (nationwide mail groups).

|                                                                                                                |                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/232.png) | NOTE: Users *must* have an Access code and a mailbox in order to be added to a mail group. |

Mail groups can also be restricted to a limited set of Authorized Senders. Thus, only certain users are allowed to send mail to the mail group. If unspecified, then it is assumed that anyone can send mail to this group, if public, or only members can send to it, if private (i.e., personal mail group). If a user attempts to send mail to a group that has one or more Authorized Senders, and they are not one of them, they are shown a list of Authorized Senders. They can send the message to one of these users who can forward it to the group, if desired.

|                                                                                                                |                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/233.png) | NOTE: Remote users *cannot* send mail to any local group that has Authorized Senders. Any messages sent by a remote user to a group with Authorized Senders will be rejected. |

The features and functionality associated with managing mail groups are described in greater detail in this chapter.

### Mail Group Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan interface provides three options to manage mail groups:

- Help (User/Group Info., etc.) \[XMHELP\]—Use this option to get information on mail groups.

|                                                                                                                |                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/234.png) | REF: For more information on this option, please refer to the "Mail Group Information" topic in Chapter 12, "Online Help/Information," in this manual. |

- Enroll in (or Disenroll from) a Mail Group \[XMENROLL; synonym GML\]—Use this option to enroll in or disenroll from mail groups.
- Personal Mail Group Edit\[XMEDITPERSGROUP\]—Use this option to create your own personal mail groups.

The MailMan mail group options are available on the main MailMan Menu and the Personal Preferences menu, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ... \[XMHELP\]

Select MailMan Menu Option: personal \<Enter\> Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group \[XMENROLL\]

Personal Mail Group Edit \[XMEDITPERSGROUP\]

Forwarding Address Edit

Select Personal Preferences Option:

<span id="_Toc436461138" class="anchor"></span>Figure 8‑1. MailMan mail group options

MailMan gives you the opportunity to enroll in established mail groups using the Enroll in (or Disenroll from) a Mail Group option \[XMENROLL; synonym GML\]. You can also remove yourself (disenroll) from mail groups using the same option.

The operation of this option depends on your current membership status and the enrollment capability of the mail group:

- Enrolling—If you are *not* a member of a particular mail group and the mail group allows self-enrollment, MailMan will *enroll* you as a member in that mail group when you use the Enroll in (or Disenroll from) a Mail Group option \[XMENROLL; synonym GML\].
- Disenrolling—If you already are a member of a particular mail group and the mail group allows self-enrollment, MailMan will confirm your membership and ask you if you want to disenroll yourself from the mail group when you use the Enroll in (or Disenroll from) a Mail Group option \[XMENROLL; synonym GML\].

MailMan lets users enroll in or disenroll from a mail group when the group allows self-enrollment. If a mail group does *not* allow self-enrollment (i.e., MailMan indicates that "...Self Enrollment Not Allowed." after a mail group name, Figure 8‑3) and the DROP OUT OF RESTRICTED GROUP field (#22) in the MAILMAN SITE PARAMETERS file (#4.3) is set to "No," users *must* contact the Mail Group Coordinator or Organizer for that particular mail group and ask either to be enrolled in or disenrolled from the mail group.

|                                                                                                                |                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/235.png) | REF: For more information on the Mail Group Coordinator, Organizer, and general mail group information, please refer to the "Mail Group Information" topic in Chapter 12, "Online Help/Information," in this manual. |

The DROP OUT OF RESTRICTED GROUP field (#22) in the MAILMAN SITE PARAMETERS file (#4.3) is a site-configurable parameter and is used to allow users to drop out (disenroll) of non-self-enrolling mail groups:

- YES—Users are warned that this is a non-self-enrolling group, and that they will *not* be allowed to rejoin later; users will be asked to re-confirm the decision to drop out.
- NO (default)—Users will have to contact IRM or the mail group Coordinator or Organizer to ask to be dropped.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/236.png)</td>
<td><p><strong>TIP:</strong> If a mail group is <em>not</em> a self-enrolling mail group, then users <em>cannot</em> just join. They <em>must</em> be added by the mail group coordinator.</p>
<p>If a user no longer wishes to be a member of such a group, he/she must ask the group coordinator to drop them; however, what if the group coordinator has left the organization or is unresponsive? Then what? Then the user will have to ask IRM to help. This problem can be avoided by setting this field to YES.</p>
<p>Some would argue that the coordinator added the user to the group for a reason, and the user should <em>not</em> be allowed to drop out (e.g., perhaps the coordinator is the user's boss). They would argue that it is MailMan's job to prevent the user from dropping out (i.e., set the field to NO). Others would argue that it is not MailMan's job at all, but the boss's job to prevent the user from dropping out, and to discipline the user if he does (i.e., set the field to YES).</p></td>
</tr>
</tbody>
</table>

If self-enrollment is *not* allowed and the DROP OUT OF RESTRICTED GROUP field (#22) in the MAILMAN SITE PARAMETERS file (#4.3) is set to "No" or null, when users try to disenroll from the mail group, MailMan will display the following:

Select Personal Preferences Option: gml \<Enter\> Enroll in (or Disenroll from) a Mail Group

Select MAIL GROUP NAME: ISC - SAN FRANCISCO BASED Member...Self Enrollment Not Allowed.

Self enrollment is not allowed for this mail group.

Select MAIL GROUP NAME:

<span id="_Toc436461143" class="anchor"></span>Figure 8‑2. Trying to disenroll from a mail group when self-enrollment is *not* allowed

Users can also create personal (private) mail groups using the Personal Mail Group Edit option on the Personal Preferences menu.

|                                                                                                                |                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/237.png) | REF: For more information on personal (private) mail groups, please refer to the "Personal Mail Groups" topic that follows in this chapter. |

The following figure shows a sample list of mail groups:

Select Personal Preferences Option: gml \<Enter\> Enroll in (or Disenroll from) a Mail Group

Select MAIL GROUP NAME: ?

Answer with MAIL GROUP NAME

Do you want the entire MAIL GROUP List? y\<Enter\> (Yes)

Choose from:

AMIE

AMIE-TEST ...Self Enrollment Not Allowed.

AR 4.0 SITES ...Self Enrollment Not Allowed.

AR 4.5 SITES ...Self Enrollment Not Allowed.

BAYMUG

BIRD

BOISE ...Self Enrollment Not Allowed.

.

.

.

DOCUMENTERS Member ...Self Enrollment Not Allowed.

.

.

.

<span id="_Hlt430510655" class="anchor"></span>Figure 8‑3. Sample mail groups (abbreviated list)

You'll notice in this example (Figure 8‑3) that MailMan gave the user the opportunity to enter a specific mail group or choose from a list when she entered a question mark ("?") at the "Select MAIL GROUP NAME:" prompt.

For this example, the user chose to display the list (abbreviated) in order to see which groups allow self-enrollment by entering "Yes" at the "Do you want the entire MAIL GROUP List?" prompt. If you entered two question marks ("??") at the "Select MAIL GROUP NAME:" prompt, MailMan would automatically display the mail group list.

MailMan will indicate when you are already a member of a group in the list. The user can see from this example that she is a member of the DOCUMENTERS mail group.

|                                                                                                                |                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/238.png) | NOTE: The current functionality of the Enroll in (or Disenroll from) a Mail Group \[GML\] and the Personal Mail Group Edit options are described in greater detail in this chapter. |

### Enroll in Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Enroll in (or Disenroll from) a Mail Group option \[XMENROLL; synonym GML\] on the Personal Preferences menu \[XM PERSONAL MENU\] to enroll yourself in a mail group that allows self-enrollment, as shown below:

Select MailMan Menu Option: pers \<Enter\> onal Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option: gml \<Enter\> Enroll in (or Disenroll from) a Mail Group

Select MAIL GROUP NAME: ?

Answer with MAIL GROUP NAME

Do you want the entire MAIL GROUP List? n\<Enter\> (No)

Select MAIL GROUP NAME: BIRD

You are now a member.

Do you want past messages to this group to be forwarded to you? No// ?

Answer YES to forward past mail group messages.

You will be asked for a time frame to search,

and then MailMan will create a task to find and forward

existing mail group messages.

Do you want past messages to this group to be forwarded to you? No// y \<Enter\> YES

Select basket to send to: IN// \<Enter\>

You will now choose a date range for the messages to be searched

and forwarded. The oldest message is from 10/16/1986.

Message sent on or after: (10/16/1986 - 8/24/2006): 8/24/2005// 1/1/06 \<Enter\> (JAN 01, 2006)

Message sent on or before: (1/1/2006 - 8/24/2006): 8/24/2006// \<Enter\> (AUG 24, 2006)

Task \#2418061 will find and forward past messages.

Select MAIL GROUP NAME: \<Enter\>

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option:

<span id="_Ref430402391" class="anchor"></span>Figure 8‑4. Enrolling in a mail group

In the previous example (Figure 8‑4), after choosing the Enroll in (or Disenroll from) a Mail Group option (GML), MailMan prompted the user to enter the name of the mail group name she wanted to join. The user entered a question mark ("?") at the "Select MAIL GROUP NAME:" prompt to display the Help for this entry.

MailMan gives you the opportunity to list all mail groups (Figure 8‑3). In this case, the user knew the mail group she wanted to join (i.e., "BIRD"). It allows self-enrollment. Thus, the user entered "No" at the "Do you want the entire MAIL GROUP List?" prompt and entered "BIRD" at the "Select MAIL GROUP NAME:" prompt.

MailMan accepted the entry and immediately informed the user that she was now a member of that mail group. (It's that easy to become a member when a mail group allows self-enrollment!)

MailMan then gives you the option to get past messages sent to the group based on a date range you select. In this case the user answered "Yes" at the "" prompt. MailMan then prompted the user to enter the date range (i.e.., messages sent on or after and messages sent on or before). In this case the she wanted past messages from 01/01/06 through today, 08/24/06.

MailMan then redisplayed the Personal Preferences menu and placed the user back at the "Select Personal Preferences Option:" prompt where she could take another action.

If self-enrollment is *not* allowed and you try to enroll yourself as a member, MailMan will display the following:

Select MAIL GROUP NAME: THREE \<Enter\> ...Self Enrollment Not Allowed.

Self enrollment is not allowed for this mail group.

Select MAIL GROUP NAME:

<span id="_Toc436461141" class="anchor"></span>Figure 8‑5. Trying to enroll in a mail group when self-enrollment is *not* allowed

To enroll in this mail group, the user would have to contact the mail group Coordinator or Organizer. If someone other than the organizer or coordinator adds users to a public mail group, which doesn't allow self-enrollment, or to a private mail group, the XM GROUP EDIT NOTIFY bulletin is sent to the organizer and coordinator to let them know which users were added and who added them.

### Disenroll From Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Enroll in (or Disenroll from) a Mail Group option \[XMENROLL; synonym GML\] on the Personal Preferences menu \[XM PERSONAL MENU\] to disenroll yourself from a mail group that allows self-enrollment, as shown below:

Select MailMan Menu Option: pers \<Enter\> onal Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option: gml \<Enter\> Enroll in (or Disenroll from) a Mail Group

Select MAIL GROUP NAME: BIRD\<Enter\> Member

You are a member. Do you want to drop out? NO// y\<Enter\> YES

You are no longer a member.

Select MAIL GROUP NAME:

<span id="_Ref430404100" class="anchor"></span>Figure 8‑6. Disenrolling from a mail group

In the previous example (Figure 8‑6), after choosing the Enroll in (or Disenroll from) a Mail Group option (GML), MailMan prompted the user to enter the name of the mail group name. Since she wanted to disenroll from the "BIRD" mail group she previously joined (Figure 8‑4), she entered "BIRD" at the "Select MAIL GROUP NAME:" prompt.

MailMan confirmed that the user was a member of that mail group and asked her if she wanted to "drop out." In this case, she did, so she entered "Yes" at the "Do you want to drop out? NO//" prompt. MailMan accepted the entry and immediately informed the user that she was no longer a member of that mail group.

MailMan then placed the user back at the "Select MAIL GROUP NAME:" prompt where she could take another mail group action.

### Personal Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Personal mail groups are *private* mail groups you create and maintain for your *own* use. Only the creator of the mail group (i.e., Organizer) can address and send mail to this group. Other members cannot use this group; however, *both* the creator (i.e., Organizer) and members of the personal mail group can:

- Display Information—Use the Group Information option on the Help (User/Group Info., etc.) menu to display information on that group.
- List the Group—See the group listed in the MAIL GROUP List when you enter two question marks (i.e., "??"—online help) at the "Select MAIL GROUP NAME:" prompt (Figure 8‑3).

To create a new or edit an existing personal mail group, use the Personal Mail Group Edit option on the Personal Preferences menu. You can add or delete members at any time. You can also use this option to delete the entire personal mail group. Even though you are the Organizer of the group, you are *not* automatically made a member. Thus, you should also make yourself a member of the personal mail group.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/239.png) | TIP: Create a personal mail group for an assigned project. Include only the members of that project team in the mail group. Thus, when you need to discuss the project, update the status, perform administrative tasks, etc., you only have to address and send mail to the group and not to each individual member. This can save you time when using MailMan. |

#### Create a New Personal Mail Group

You can use the Personal Mail Group Edit option on the Personal Preferences menu to create a new personal mail group, as shown below:

Select MailMan Menu Option: pers \<Enter\> onal Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option: Pers \<Enter\> onal Mail Group Edit

Select MAIL GROUP NAME: INFRASTRUCTURE

Are you adding 'INFRASTRUCTURE' as a new MAIL GROUP? No// y \<Enter\> (Yes)

MAIL GROUP NAME: INFRASTRUCTURE// \<Enter\>

Select MEMBER: ?

Answer with MEMBER

You may enter a new MEMBER, if you wish

Enter a local user who should receive mail addressed to this group.

Answer with NEW PERSON NAME, or INITIAL, or SSN, or VERIFY CODE, or

NICK NAME, or KEY DELEGATION LEVEL, or DEA#, or VA#, or

SOCIAL WORKER ?, or POSITION/TITLE, or ALIAS

Do you want the entire 1554-Entry NEW PERSON List? n\<Enter\> (No)

Select MEMBER: xmuser1 \<Enter\>,ONE E. OX COMPUTER SPECIALIST

Are you adding 'XMUSER1,ONE E.' as a new MEMBER (the 1ST for this MAIL GROUP)?

No// y \<Enter\> (Yes)

Select MEMBER: xmuser2 \<Enter\> ,TWO M. TX PROGRAMMER

Are you adding 'XMUSER2,TWO M.' as a new MEMBER (the 2ND for this MAIL GROUP)? No// y \<Enter\> (Yes)

Select MEMBER: xmuser4 \<Enter\> ,FOUR FX 10BA6/ISC Q... Continuum

Are you adding 'XMUSER4,FOUR' as a new MEMBER (the 3RD for this MAIL GROUP)? No// y \<Enter\> (Yes)

Select MEMBER: \<Enter\>

Select REMOTE MEMBER: ?

Answer with MEMBERS - REMOTE REMOTE MEMBER

You may enter a new MEMBERS - REMOTE, if you wish

Enter a remote address (name@domain) or local device (D.device) or

local server (S.server).

Select REMOTE MEMBER: \<Enter\>

Select MAIL GROUP NAME:

<span id="_Ref430420553" class="anchor"></span>Figure 8‑7. Creating a new personal mail group

In the previous example (Figure 8‑7), after choosing the Personal Mail Group option, MailMan prompted the user to enter the name of the personal mail group. Since she wanted to create a new personal mail group called "INFRASTRUCTURE," she entered "INFRASTRUCTURE" at the "Select MAIL GROUP NAME:" prompt.

MailMan recognized that this was a new personal mail group and asked the user to confirm its creation. The user confirmed the entry by entering "Yes" at the "Are you adding 'INFRASTRUCTURE' as a new MAIL GROUP? No//" prompt.

MailMan then asked the user to enter the members of the group. She entered a question mark ("?") after the first "Select MEMBER:" prompt in order to display the online Help for entering local users.

For this example, the user wanted to include three local members in the personal mail group:

- XMUSER1,ONE E.
- XMUSER2,TWO M.
- XMUSER4,FOUR

As with entering any local MailMan user name, the user only had to enter the first portion of each person's last name (*not* case sensitive) at the "Select MEMBER:" prompt.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/240.png) | REF: For more information on entering names, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

MailMan asked the user to confirm each name by entering "Yes" at the "Are you adding 'name' as a new MEMBER (the n<sup>th</sup> for this MAIL GROUP)? No//" prompt (where name is the member name and n<sup>th</sup> is the number of the member in the group \[1<sup>st</sup>, 2<sup>nd</sup>, 3<sup>rd</sup>, 4<sup>th</sup>, etc.\]). MailMan knew the user was finished with adding local members to the group when she pressed the \<Enter\> key at the "Select MEMBER:" prompt without entering another name.

MailMan then prompted the user to enter any remote users as members. Again, she entered a question mark ("?") at the "Select REMOTE MEMBER:" prompt in order to display the online Help for entering remote users. Since she did not want to enter any remote users, she pressed the \<Enter\> key at the "Select REMOTE MEMBER:" prompt without entering a name.

At this point, the user had completed adding members to the personal mail group.

MailMan then placed the user back at the "Select MAIL GROUP NAME:" prompt where she could take another personal mail group action.

The user then used the Group Information option on the Help (User/Group Info., etc.) menu to display information on the newly created "INFRASTRUCTURE" personal mail group, as shown below:

Select MailMan Menu Option: help \<Enter\> (User/Group Info., etc.)

User Information

Group Information

Remote User Information

New Features in MailMan

General MailMan Information

Questions and Answers on MailMan

Manual for MailMan Users

Select Help (User/Group Info., etc.) Option: group \<Enter\> Information

Select MAIL GROUP NAME: INFRA \<Enter\> STRUCTURE

NAME: INFRASTRUCTURE TYPE: private

ALLOW SELF ENROLLMENT?: NO RESTRICTIONS: ORGANIZER ONLY

ORGANIZER: XMUSER1,ONE E.

Member Last Used MailMan

XMUSER1,ONE E. - COMPUTER SPECIALIST (OIFO 09/15/98@08:39

XMUSER2,TWO M. - PROGRAMMER (OIFO Oaklan 09/15/98@07:59

XMUSER4,FOUR - Q... Continuum 09/15/98@07:40

Select MAIL GROUP NAME: <span id="_Hlt431007359" class="anchor"></span>

Figure 8‑8. INFRASTRUCTURE personal mail group information

|                                                                                                                |                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/241.png) | REF: For more information on the Group Information option, please refer to the "Mail Group Information" topic in Chapter 12, "Online Help/Information," in this manual. |

MailMan will *not* allow you to create a personal mail group if a public mail group with that same name already exists, as shown below:

Select Personal Preferences Option: personal \<Enter\> Mail Group Edit

Select MAIL GROUP NAME: MAILMAN DEVELOPERS

Are you adding 'MAILMAN DEVELOPERS' as a new MAIL GROUP? No// y\<Enter\> (Yes)

Can't add it because public group 'MAILMAN DEVELOPERS' already exists. ??

Select MAIL GROUP NAME:

<span id="_Toc436461146" class="anchor"></span>Figure 8‑9. Trying to create a personal mail group when a public mail group already exists

#### Edit an Existing Personal Mail Group

You can use the Personal Mail Group Edit option on the Personal Preferences menu to edit an existing personal mail group, as shown below:

Select Personal Preferences Option: pers \<Enter\> onal Mail Group Edit

Select MAIL GROUP NAME: ??

Choose from:

INFRASTRUCTURE

MailMan

Test Group 2

The name of a mail group, i.e. a list of recipients who can

all be addressed at once by reference to this name.

Select MAIL GROUP NAME: INFRA \<Enter\> STRUCTURE

MAIL GROUP NAME: INFRASTRUCTURE// \<Enter\>

Select MEMBER: XMUSER4,FOUR// ?

Answer with MEMBER

Choose from:

XMUSER2,TWO M.

XMUSER4,FOUR

XMUSER1,ONE E.

You may enter a new MEMBER, if you wish

Enter a local user who should receive mail addressed to this group.

Answer with NEW PERSON NAME, or INITIAL, or SSN, or VERIFY CODE, or

NICK NAME, or KEY DELEGATION LEVEL, or DEA#, or VA#, or

SOCIAL WORKER ?, or POSITION/TITLE, or ALIAS

Do you want the entire 1554-Entry NEW PERSON List? n\<Enter\> (No)

Select MEMBER: XMUSER4,FOUR// @

SURE YOU WANT TO DELETE? y\<Enter\> (Yes)

Select MEMBER: XMUSER2,TWO M.// xmuser11 \<Enter\> ,ELEVEN EX ISC PROJECT MANAGER

Are you adding 'XMUSER11,ELEVEN' as a new MEMBER (the 3RD for this MAIL GROUP)?

No// y \<Enter\> (Yes)

Select MEMBER: \<Enter\>

Select REMOTE MEMBER: \<Enter\>

Select MAIL GROUP NAME:

<span id="_Ref430479517" class="anchor"></span>Figure 8‑10. Editing an existing personal mail group

In the previous example (Figure 8‑10), after choosing the Personal Mail Group option, MailMan prompted the user to enter the name of the personal mail group. In this case, the user wanted to edit an existing personal mail group.

The user first chose to get a list of all of the personal mail groups by entering two question marks ("??") at the "Select MAIL GROUP NAME:" prompt. From the list of mail groups, the user chose to edit the "INFRASTRUCTURE" personal mail group by entering the first portion of the "INFRASTRUCTURE" group name at the "Select MAIL GROUP NAME:" prompt.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/242.png) | REF: For more information on entering names, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

The user then confirmed the mail group by pressing the \<Enter\> key at the "MAIL GROUP NAME: INFRASTRUCTURE//" prompt.

MailMan then asked the user to edit the members of the group. She entered a question mark ("?") at the "Select MEMBER: XMUSER4,FOUR//" prompt in order to display the current list of members in the mail group and display the online help for this prompt.

Currently, the user had three local members in the personal mail group:

- XMUSER1,ONE E.
- XMUSER2,TWO M.
- XMUSER4,FOUR

For this example, the user wanted to remove XMUSER4,FOUR from the group and add XMUSER11,ELEVEN as a new member.

The user first deleted XMUSER4,FOUR by entering an at-sign ("@") at the "Select MEMBER: XMUSER4,FOUR//" prompt. She confirmed the deletion by entering "Yes" at the "SURE YOU WANT TO DELETE?" prompt.

MailMan then prompted the user to edit the next member. In this case, she wanted to add a new local member so she entered the first portion of the person's last name (i.e., "XMUSER11") at the "Select MEMBER: XMUSER2,TWO M.//" prompt.

MailMan asked the user to confirm the name by entering "Yes" at the "Are you adding 'XMUSER11,ELEVEN' as a new MEMBER (the 3RD for this MAIL GROUP)? No//" prompt.

MailMan knew the user was finished with adding local members to the group when she pressed the \<Enter\> key at the "Select MEMBER:" prompt without entering another name.

MailMan then prompted the user to enter any remote users as members. Since she did not want to enter any remote users, she pressed the \<Enter\> key at the "Select REMOTE MEMBER:" prompt without entering a name.

At this point, the user had completed modifying the personal mail group members.

The personal mail group now had the following three local members:

- XMUSER1,ONE E.
- XMUSER2,TWO M.
- XMUSER11,ELEVEN

MailMan then placed the user back at the "Select MAIL GROUP NAME:" prompt where she could take another personal mail group action.

The user then used the Group Information option on the Help (User/Group Info., etc.) menu to display information on the modified "INFRASTRUCTURE" personal mail group, as shown below:

Select MailMan Menu Option: help \<Enter\> (User/Group Info., etc.)

User Information

Group Information

Remote User Information

New Features in MailMan

General MailMan Information

Questions and Answers on MailMan

Manual for MailMan Users

Select Help (User/Group Info., etc.) Option: group \<Enter\> Information

Select MAIL GROUP NAME: INFRA \<Enter\> STRUCTURE

NAME: INFRASTRUCTURE TYPE: private

ALLOW SELF ENROLLMENT?: NO RESTRICTIONS: ORGANIZER ONLY

ORGANIZER: XMUSER1,ONE E.

Member Last Used MailMan

XMUSER1,ONE E. - COMPUTER SPECIALIST (OIFO 09/15/98@09:29

XMUSER2,TWO M. - PROGRAMMER (OIFO Oaklan 09/15/98@07:59

XMUSER11,ELEVEN - PROJECT MANAGER (OIFO Oak 09/14/98@14:47

Select MAIL GROUP NAME:

<span id="_Toc436461148" class="anchor"></span>Figure 8‑11. Modified INFRASTRUCTURE personal mail group information

|                                                                                                                |                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/243.png) | REF: For more information on the Group Information option, please refer to the "Mail Group Information" topic in Chapter 12, "Online Help/Information," in this manual. |

#### Delete a Personal Mail Group

You can use the Personal Mail Group Edit option on the Personal Preferences menu to delete a personal mail group, as shown below:

Select Personal Preferences Option: pers \<Enter\> onal Mail Group Edit

Select MAIL GROUP NAME: INFRA \<Enter\> STRUCTURE

MAIL GROUP NAME: INFRASTRUCTURE// @

SURE YOU WANT TO DELETE THE ENTIRE 'INFRASTRUCTURE' MAIL GROUP? y \<Enter\> (Yes)

Select MAIL GROUP NAME:

<span id="_Ref430487727" class="anchor"></span>Figure 8‑12. Deleting a personal mail group

In this example (Figure 8‑12), after choosing the Personal Mail Group option, MailMan prompted the user to enter the name of the personal mail group. Since the user wanted to delete the personal mail group called "INFRASTRUCTURE," she entered the first portion of the "INFRASTRUCTURE" group name at the "Select MAIL GROUP NAME:" prompt.

To delete the mail group the user entered an at-sign ("@") at the "MAIL GROUP NAME: INFRASTRUCTURE//" prompt. She confirmed the deletion by entering "Yes" at the "SURE YOU WANT TO DELETE THE ENTIRE 'INFRASTRUCTURE' MAIL GROUP?" prompt. Thus, the user had successfully deleted the "INFRASTRUCTURE" personal mail group.

MailMan then placed the user back at the "Select MAIL GROUP NAME:" prompt where she could take another personal mail group action.

# Surrogates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The topics to be discussed in this chapter:

- Surrogate Options
- Become a Surrogate
- Designate a Surrogate
- Remove a Surrogate

A surrogate is someone who substitutes for someone else. MailMan gives all users the opportunity to choose someone to act as their surrogate. It also allows all users to become a surrogate.

There are several occasions when you may wish to designate someone as your surrogate. For example, if you are going on vacation, you may ask someone to be a surrogate for you while you are out of the office. Specifically, a manager or project team member may ask their administrative assistant or co-worker to read their mail while they are out of the office so that critical or important messages can be read and responded to without delay.

Also, you may wish to become (act as) a surrogate in two different ways:

> 1\. Other Surrogate—Act as a surrogate for another user (i.e., Other) who has designated you as their surrogate and given you privileges to: read, reply to, and/or send messages.

> 2\. SHARED,MAIL Surrogate—Act as a "special user" surrogate (i.e., SHARED,MAIL) where you can read and reply to messages of general interest, however, you *cannot* send new mail.

For example, you may choose to become a surrogate, if you have been asked by someone else to act as their surrogate while they are out of the office. As their surrogate, you can check their mail. Also, you can become a surrogate of SHARED, MAIL in order to read about general information or special announcements available to all MailMan users.

Surrogates may be allowed the following privileges:

- Read—Users who give a surrogate this privilege allow the surrogate to:
- Delete messages in any mail basket.
- Forward messages in any mail basket to other recipients.
- Later messages in any mail basket.
- New/Un New messages in any mail basket.
- Read messages in any mail basket.
- Reply to messages in any mail basket.
- Save messages to any mail basket.
- Read & Write—Users who give a surrogate this privilege, in addition to all the privileges of Read access (shown above), allow the surrogate to:
- Answer messages.
- Copy messages.
- Edit messages.
- Send messages.
- Write messages.

The features and functionality associated with surrogates are described in greater detail in this chapter.

### Surrogate Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan interface provides two options with regards to surrogates:

- Become a Surrogate (SHARED,MAIL or Other) \[XMASSUME; synonym AML\]—Use this option to act as a surrogate for SHARED,MAIL or another MailMan user.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/244.png) | NOTE: The Assume the Identity of SHARED,MAIL (i.e., XMSHARE) and the Assume another identity as a surrogate (i.e., XMASSUME) options were combined into the Become a Surrogate (SHARED,MAIL or Other) option. The XMSHARE Option still exists, however, it is not attached to any menu. Thus, IRM can still place that option on the XUCOMMAND menu so users do not have to go into MailMan to go into SHARED,MAIL. |

- Surrogate Edit \[XMEDITSURR\]—Use this option to select another user to act as your surrogate.

The MailMan surrogate options are available on the main MailMan Menu and the Personal Preferences menu, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other) \[XMASSUME\]

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: personal Preferences

User Options Edit

Banner Edit

Surrogate Edit \[XMEDITSURR\]

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option:

<span id="_Toc436461150" class="anchor"></span>Figure 9‑1. MailMan surrogate options

### Become a Surrogate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All users of MailMan are given the option to act as a Surrogate for SHARED,MAIL. SHARED,MAIL allows you to read and reply to messages of general interest, however, you *cannot* send new mail. If you have been designated as a surrogate to another MailMan user, you are given the opportunity to choose either from SHARED,MAIL or the user who specified you as a surrogate (i.e., Other). When you act as a surrogate for another user, depending on your privileges, you may read, reply to, and/or send messages.

|                                                                                                                |                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/245.png) | NOTE: To designate your own surrogate to receive and/or send your e-mail, use the Surrogate Edit option on the Personal Preferences menu. For more information on this, please refer to the "Designate a Surrogate" topic that follows in this chapter. |

When acting as a surrogate for another user on MailMan, you will be using your own MailMan message center profile when reading and sending mail and *not* the other user's profile. For example, if you have set your message reader to use the Detailed Full Screen message reader and the user who designated you as the surrogate uses the Classic message reader, you will still view that user's messages in the Detailed full screen and *not* in the Classic message reader.

To become a surrogate, choose the Become a Surrogate (SHARED,MAIL or Other) option \[XMASSUME; synonym AML\] on the MailMan menu, as shown below:

VA MailMan 8.0 service for XMUSER1.ONE_E+@REDACTED.VA.GOV

You last used MailMan: 07/13/98@09:51

Your current banner: One Xmuser1, Technical Writer, OI Field Office Oakland

You have 2 new messages.

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: AML \<Enter\> Become a Surrogate (SHARED,MAIL or Other)

<span id="_Ref425828683" class="anchor"></span>Figure 9‑2. Becoming a surrogate

#### SHARED,MAIL Surrogates

After you choose the Become a Surrogate (SHARED,MAIL or Other) option \[XMASSUME; synonym AML\] (Figure 9‑2) and if another MailMan user has not designated you as a surrogate, you are automatically made a surrogate of SHARED,MAIL. If other MailMan users have designated you as a surrogate, MailMan displays the list of surrogates from which you can choose (including SHARED,MAIL) and sets SHARED,MAIL as the default response.

As a surrogate to SHARED,MAIL, the user is only allowed Read access privileges. Therefore, the surrogate is able to read any message in any SHARED,MAIL basket, and they can respond to any message:

VA MailMan 8.0 service for SHARED.MAIL@REDACTED.VA.GOV

(Surrogate: XMUSER1,ONE E.)

SHARED,MAIL has 130 new messages.

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// ?

Answer with BASKET

Do you want the entire 15-Entry BASKET List? y \<Enter\> (Yes)

Choose from:

AI LITERATURE (1 message)

DECSERVERS (1 message)

DIRECTIVES (1 message)

IN (3 messages, 2 new)

INTERNET (3 messages)

ITARG MINUTES (0 messages)

JOBS (208 messages, 128 new)

MODEMS (2 messages)

MUMPS-L (0 messages)

NBS PUBS (1 message)

PHONE (1 message)

STAR TREK (1 message)

SUGGESTION (0 messages)

UPLOAD/DOWNLOAD (1 message)

WASTE (0 messages)

Read mail in MAIL BASKET: IN// \<Enter\> (3 messages, 2 new)

IN Basket, 3 messages (17-19), 2 new

\*=New/!=Priority.........Subject....................Lines.From.........Read/Rcvd

\*19. \[1220163\] 07/10/98 PCTS==\> AMS Message Number: 71 POSTMASTER

\*18. \[1219463\] 07/07/98 PCTS==\> AMS Message Number: 69 POSTMASTER

17\. \[1216832\] 06/17/98 PCTS==\> AMS Message Number: 22 POSTMASTER

Enter message number or command: \<Enter\>

Read mail in MAIL BASKET: IN// ^

You are now yourself again.

<span id="_Toc436461152" class="anchor"></span>Figure 9‑3. Becoming a SHARED,MAIL surrogate

|                                                                                                                |                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/246.png) | NOTE: Only those users holding the XMMGR security key (e.g., IRM) or surrogates of the Postmaster can create new mail baskets for SHARED,MAIL. |

#### Other Surrogates

After you choose the Become a Surrogate (SHARED,MAIL or Other) option \[XMASSUME; synonym AML\] (Figure 9‑2) and if you have been designated as a surrogate by another MailMan user, you are given the choice of choosing which surrogate you wish to become (e.g., SHARED, MAIL or the other user). As a default, all users can be a SHARED,MAIL surrogate. For other users, MailMan displays your access privileges (i.e., Read or Read and Write) and if the person has any new mail (i.e., MailMan indicates the number of new messages, if any). MailMan displays the message information so the surrogate knows beforehand if the user has any new messages to process. If not, the surrogate can save himself or herself time and not bother to become a surrogate for that person.

In the following example, the user (One Xmuser1) was designated as a surrogate to someone else (Two Xmuser2), thus, he had another choice besides SHARED,MAIL when becoming a surrogate, as shown below:

VA MailMan 8.0 service for XMUSER1.ONE_E+@REDACTED.VA.GOV

You last used MailMan: 07/13/98@10:07

Your current banner: One Xmuser1, Technical Writer, OI Field Office Oakland

You have 2 new messages.

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: aml \<Enter\> Become a Surrogate (SHARED,MAIL or Other)

Choose from:

XMUSER2,TWO M. Read & Write Privileges 1 New Msgs

SHARED,MAIL Read Privilege

Select NEW PERSON NAME: SHARED,MAIL// xmuser2 \<Enter\> ,TWO M. Read & Write Privileges

1 New Msgs

VA MailMan 8.0 service for XMUSER2.TWO_M+@REDACTED.VA.GOV

(Surrogate: XMUSER1,ONE)

XMUSER2,TWO M. last used MailMan: 04/15/99@07:45 (Surrogate: XMUSER1,ONE E.)

XMUSER2,TWO M.'s current banner: On Jury Duty, starting 2/17.

XMUSER2,TWO M. has 1 new message.

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

XMUSER2,TWO M. has 1 new message. (Last arrival: 04/15/99@07:47)

Select MailMan Menu Option:

<span id="_Ref424973517" class="anchor"></span>Figure 9‑4. Becoming a user's surrogate

For this example (Figure 9‑4), after the user chose the Become a Surrogate (SHARED,MAIL or Other) option (AML), MailMan displayed a list of surrogates from which to choose. In this case, the user is designating surrogates for two MailMan users:

- XMUSER2,TWO M.
- SHARED,MAIL (default)

|                                                                                                                |                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/247.png) | NOTE: The list of surrogates is displayed in alphabetical order. |

As you can see, however, the default surrogate is always going to be SHARED, MAIL. MailMan also displays what privileges are available with each user (e.g., Read only or Read and Write privileges) and if the user has any new messages. In this case, Two Xmuser2 has given the user both Read and Write access to his mail and he has one new message (i.e., "1 New Msgs").

For this example (Figure 9‑4), the user chose to become the surrogate for XMUSER2,TWO M. As with entering any local MailMan user name, he only had to enter the first portion of his last name at the "Select NEW PERSON NAME: SHARED,MAIL//" prompt.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/248.png) | REF: For more information on entering names, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

After the user chose a surrogate from the list, he "became" that user. In this case, One Xmuser1 was now a surrogate for Two Xmuser2.

MailMan displays the surrogate information prior to the MailMan Menu:

- User's Name and MailMan Institution—VA MailMan 8.0 service for XMUSER2.TWO_M+@REDACTED.VA.GOV
- Surrogate Information—Surrogate: XMUSER1,ONE E.
- User's Last MailMan Use Statistics—XMUSER2,TWO M. last used MailMan: 04/15/99@07:45
- User's Banner—XMUSER2,TWO M.'s current banner: On Jury Duty, starting 2/17.
- Message indicator—XMUSER2,TWO M. has 1 new message.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/249.png) | NOTE: When acting as a surrogate for another user on MailMan, you will be using your own MailMan message center profile when reading and sending mail and not the other user's profile. For example, if you have set your message reader to use the Detailed Full Screen message reader and the user who designated you as the surrogate uses the Classic message reader, you will still view that user's messages in the Detailed full screen and not in the Classic message reader. |

#### Read Privileges

When a surrogate has Read access privileges, it means that they can both read and reply to any message in the other user's mail baskets, as shown below:

Select MailMan Menu Option: R \<Enter\> Read/Manage Messages

Select message reader: Detailed Full Screen// \<Enter\>

Read mail in MAIL BASKET: IN// \<Enter\> (65 messages)

IN Basket, 65 messages (1-3)

\*=New/!=Priority..........Subject...................Lines.From.........Read/Rcvd

1\. \[1220355\] 07/13/98 TEST CONFIRM 1 \<XMUSER0@MAILMAN.ISC-S

..2. \[1220344\] 07/13/98 your visit 16 XXXXXX.Dr.Xmuser@ 1/1

3\. \[1219335\] 07/06/98 RE: Hello 48 Xmuser41 Forty1 1/1

Enter message number or command: 1

Subj: TEST CONFIRM \[#1220355\] 07/13/98@09:15:43 -0700 (PDT) 1 line

From: \<XMUSER0@MAILMAN.REDACTED.VA.GOV\> In 'IN' basket. Page 1

-------------------------------------------------------------------------------

TEST CONFIRM

Enter message action (in IN basket): IGNORE// R

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]============\< TEST CONFIRM \>===========\[ \<PF1\>H=Help \]====

Here is a test reply as a surrogate

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

Select Message option: Transmit now// \<Enter\> Sending local reply...

Sent

Do you wish to send this reply across the network? No// \<Enter\> NO

Enter message action (in IN basket): IGNORE//

<span id="_Ref428170684" class="anchor"></span>Figure 9‑5. Replying to a message as a surrogate

When you are designated as a surrogate and only given Read access, you *cannot* send new e-mail under the other person's name, as demonstrated below:

VA MailMan 8.0 service for XMUSER2.TWO_M+@REDACTED.VA.GOV

(Surrogate: XMUSER1,ONE E.)

XMUSER2,TWO M. last used MailMan: 07/13/98@10:47

XMUSER2,TWO M.'s current banner: If wishes were horses, beggars would ride.

XMUSER2,TWO M. has no new messages.

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: s \<Enter\> Send a Message

You do not have 'write' privilege for XMUSER2,TWO M.

<span id="_Toc436461156" class="anchor"></span>Figure 9‑6. Read-only privileges prevent sending messages as a surrogate

#### Read and Write Privileges

When a surrogate has Read and Write access privileges, it means that they can both read and reply to any message in the other user's mail baskets as well as send out new messages, as shown below:

VA MailMan 8.0 service for XMUSER1.ONE_E+@REDACTED.VA.GOV

You last used MailMan: 07/13/98@10:07

Your current banner: One Xmuser1, Technical Writer, OI Field Office Oakland

You have 2 new messages.

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: aml \<Enter\> Become a Surrogate (SHARED,MAIL or Other)

Choose from:

XMUSER2,TWO M. Read & Write Privileges No New Msgs

SHARED,MAIL Read Privilege

Select NEW PERSON NAME: SHARED,MAIL// xmuser2 \<Enter\> ,TWO M. Read & Write Privileges

No New Msgs

VA MailMan 8.0 service for XMUSER2.TWO_M+@REDACTED.VA.GOV

(Surrogate: XMUSER1,ONE E.)

XMUSER2,TWO M. last used MailMan: 07/13/98@10:47

XMUSER2,TWO M.'s current banner: If wishes were horses, beggars would ride.

XMUSER2,TWO M. has no new messages.

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: s\<Enter\> Send a Message

Subject: Test Message

You may enter the text of the message...

==\[ WRAP \]==\[ INSERT \]============\< Test Message \>===========\[ \<PF1\>H=Help \]====

Testing a send as a surrogate.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

<span id="_Ref428171343" class="anchor"></span>Figure 9‑7. Read & Write privileges—Surrogate sending a message (1 of 2)

Send mail to: XMUSER2,TWO M.// \<Enter\> INFORMATION SYSTEMS CENTER

Last used MailMan: 07/13/98@09:49 (Surrogate: XMUSER1,ONE E.)

If wishes were horses, beggars would ride.

And Send to: xmuser1 \<Enter\> ,ONE E.

Select basket to send to: IN// \<Enter\>

And Send to: \<Enter\>

Select Message option: Transmit now// \<Enter\> Sending \[1220372\]...

Sent

<span id="_Toc147225940" class="anchor"></span>Figure 9‑8. Read & Write privileges—Surrogate sending a message (2 of 2)

If given the permission to send mail, a surrogate will be listed as the "Sender" of the message, while the message is "From" the original user, as shown below:

Subj: Test Message \[#1220372\] 07/13/98@09:50 1 line

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

(Sender: XMUSER1,ONE E. - COMPUTER SPECIALIST) In 'TEST' basket. Page 1

\*New\*

-------------------------------------------------------------------------------

Testing a send as a surrogate.

Enter message action (in TEST basket): IGNORE//

<span id="_Toc436461158" class="anchor"></span>Figure 9‑9. Sample message sent by a surrogate

MailMan indicates the surrogate information in the message header. In this case, the message is from Two Xmuser2 (i.e., "From: XMUSER2,TWO M."), but the user, as the surrogate, is the sender of the message (i.e., "Sender: XMUSER1,ONE E.").

### Designate a Surrogate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan provides you with the Surrogate Edit option for designating a surrogate to read and send your own e-mail. This option is available on the Personal Preferences menu, as shown below:

VA MailMan 8.0 service for XMUSER1.ONE_E+@REDACTED.VA.GOV

You last used MailMan: 07/13/98@09:47

Your current banner: One Xmuser1, Technical Writer, OI Field Office Oakland

You have 2 new messages.

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: personal \<Enter\> Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option: surrogate \<Enter\> Edit

<span id="_Ref424980082" class="anchor"></span>Figure 9‑10. Surrogate Edit option

You can use the Surrogate Edit option \[XMEDITSURR\] when you know you will not be able to read your mail for a period of time but still want your mail monitored and taken care of in a timely fashion.

In this example (Figure 9‑11), the user chose to designate a surrogate (i.e., Two Xmuser2) with Read access privileges only. After the user chose the Surrogate Edit option, he was prompted to enter the surrogate's information, as shown below:

Select SURROGATE: xmuser2 \<Enter\> ,TWO M. TX PROGRAMMER

Are you adding 'XMUSER2,TWO M.' as a new SURROGATE (the 1ST for this MAILBOX)? No// y \<Enter\> (Yes)

READ PRIVILEGE: ??

This flag controls whether the surrogate may read the mail of this user.

Choose from:

y YES

n NO

READ PRIVILEGE: y \<Enter\> YES

SEND PRIVILEGE: ??

This flag controls whether the surrogate may send messages while acting

as a surrogate of this user. If so, the surrogate is named as "sender".

Choose from:

y YES

n NO

SEND PRIVILEGE: n \<Enter\> NO

Select SURROGATE: \<Enter\>

<span id="_Ref424979231" class="anchor"></span>Figure 9‑11. Creating a surrogate

To designate a surrogate (Figure 9‑11), the user must first enter the person who will act as the surrogate. For this example, the user entered the first portion of his last name (i.e., "XMUSER2") at the "Select SURROGATE:" prompt.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/250.png) | REF: For more information on entering names, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

Next, MailMan wanted the user to enter the surrogate's privileges. In this case, he decided to give the surrogate Read privileges by entering "Yes" at the "READ PRIVILEGE:" prompt. Because the user did not want the surrogate to have Write privileges, he entered "No" at the "SEND PRIVILEGE:" prompt. Thus, this new surrogate has access to the mail and can read and reply to any of the messages in any of the mail baskets; however, the surrogate *cannot* send new mail while acting as the surrogate. MailMan knew the user was finished entering surrogates when he pressed the \<Enter\> key at the "Select SURROGATE:" prompt without entering another name.

In order for the newly designated surrogate to access your mail they must "become" you by choosing the Become a Surrogate (SHARED,MAIL or Other) option \[XMASSUME; synonym AML\] on the MailMan Menu. Once the surrogate has access, depending on their access privileges, they can read and/or write messages as you.

|                                                                                                                |                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/251.png) | REF: For more information on how to become a surrogate, please refer to the "Become a Surrogate" topic in this chapter. |

|                                                   |                                                                                                                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/252.png) | TIP: Make sure you notify the person who you designate as a surrogate, so they will know that they should check your mail. MailMan does not automatically notify users when they are surrogates. |

### Remove a Surrogate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you no longer wish to have someone act as your surrogate, you can delete him or her by using the Surrogate Edit option on the Personal Preferences menu, as shown below:

Select MailMan Menu Option: personal \<Enter\> Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option: surrogate \<Enter\> Edit

Select SURROGATE: XMUSER2,TWO M.// @

SURE YOU WANT TO DELETE THE ENTIRE SURROGATE? y \<Enter\> (Yes)

Select SURROGATE:

<span id="_Toc436461161" class="anchor"></span>Figure 9‑12. Deleting a surrogate

By entering the at-sign ("@") at the "Select SURROGATE: XMUSER2,TWO M.//" prompt, that user is now deleted from your surrogate list.

# Forwarding Mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics to be discussed in this chapter:

- Forwarding Address Edit Option
- Forwarding Address
- Local Delivery Flag
- Enter Your Forwarding Address
- Delete Your Forwarding Address

Previously, MailMan gave you the opportunity to have your e-mail automatically forwarded to any remote VA or *non*-VA e-mail addresses. MailMan Patch XM\*8.0\*18, however, limited the capability of automatically forwarding your mail to only VA-related e-mail addresses (i.e., e-mail addresses ending in "VA.GOV"). This requirement was based on a memorandum signed by Robert N. McFarland, Assistant Secretary for Information and Technology (005); Subject: Limits on the Use of Certain E-mail Features and Configurations (see Figure 10‑1). MailMan enforces this by checking auto-forward addresses each time they are used, and deletes any non-compliant addresses. MailMan also gives you the option to continue to receive e-mail at your local address as well.

|                                                                                                                |                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/253.png) | NOTE: Waivers to auto forward e-mail to restricted *non*-VA e-mail domains can be requested through your site Information Security Officer (ISO). |

The intent of the memorandum is to help ensure that sensitive VA information is not put at risk. This patch puts MailMan in compliance with the limits set forth by the memorandum.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/254.png)</td>
<td><p><strong>REF:</strong> The memorandum can be viewed at:</p>
<blockquote>
<p><a href="https://vaww.ocis.va.gov/portal/server.pt/gateway/PTARGS_0_2_19707_0_0_18/Limits%20on%20the%20Use%20of%20Certain%20E-mail%20Features%20and%20Configurations%20(EDMS%20209533)%20captured.pdf">REDACTED</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

As of MailMan Patch XM\*8.0\*18, the following fields were added to the MAILMAN SITE PARAMETERS file (#4.3) in support of this auto forward restriction:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 39%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Number</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>31</td>
<td>AUTO-FORWARD LIMITED?</td>
<td>This field is used for security and data privacy purposes. It is used to limit the e-mail domains (addresses) to which users can auto forward their e-mail. If this field is set to YES, only those approved e-mail domains in the AUTO-FORWARD APPROVED SITE Multiple field (#31.1) will be authorized to receive auto forwarded e-mail form a VA system.</td>
</tr>
<tr class="even">
<td>31.1</td>
<td>AUTO-FORWARD APPROVED SITE (Multiple)</td>
<td>This field is used for security and data privacy purposes. It is used to store only those VA approved e-mail domains authorized to receive auto forwarded e-mail from another VA system. Currently, the only authorized VA domains are those domains ending in "VA.GOV." Field values <em>must</em> be from 3 to 64 characters in length.</td>
</tr>
<tr class="odd">
<td>31.2</td>
<td>AUTO-FORWARD WAIVER SITE (Multiple)</td>
<td><p>This field is used for security and data privacy purposes. It is used to store only those VA approved e-mail domains with waivers authorized to receive auto forwarded e-mail from another VA system. Field values <em>must</em> be from 3 to 64 characters in length.</p>
<p>![](mailman-version-8-user-guide/255.png) <strong>NOTE:</strong> Holders of the XM AUTO-FORWARD WAIVER security key, can also auto-forward to the sites which are listed here, or which end in those which are listed here.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc147225945" class="anchor"></span>Table 10‑1. Auto forward-related site parameters

|                                                   |                                                                                                                                    |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/256.png) | CAUTION: VA sites should *not* alter the contents of these fields, or else the site will not be in compliance with the memorandum. |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/257.png) | NOTE: The option to forward e-mail may or may not be available to you. It depends on whether or not your site restricts access to this option to users holding the XMNET security key. For example, if your site requires users to hold the XMNET security key and you do not hold that key, you will not be able to use this option. |

The features and functionality associated with having your mail forwarded are described in greater detail in this chapter.

The following is the full text of the memorandum:

Memorandum

Date: MAY 24 2004

From: Assistant Secretary for Information and Technology (005)

Subj: Limits on the Use of Certain E-mail Features and Configurations

TO: Under Secretaries, Assistant Secretaries, and Other Key Officials

1\. To help ensure that sensitive VA information is not put at risk, limits

must be set on certain e-mail features and configurations. There are

currently a number of VA systems that allow users to send and receive e-mail. These systems include e-mail clients such as Microsoft Outlook and

Exchange, applications such as the Veterans Health information Systems

Technology Architecture (VistA), and the Burial Operations Support System.

2\. Some of these systems have configuration options that allow e-mail

messages to be automatically forwarded from one email address to another.

Such options are normally used as a convenient way for users to receive

work-related messages at another location while away from the office.

Because the forwarding is done automatically, the user loses the ability

to determine whether a specific message is appropriate for forwarding

outside VA boundaries and over the Internet.

3\. Auto-forwarding of e-mail messages to addressees outside VA may result in information intended for use within the VA network to be transmitted,

viewed, and/or stored on mail systems outside of VA's control. This is

clearly unacceptable and puts the Department at risk for Privacy Act or

Health Insurance Portability and Accountability Act (HIPAA) violations.

4\. Effective 30 days from the date of this memorandum, auto-forwarding of

e-mail messages to addressees outside the VA network shall be strictly

prohibited. Autoforwarding of e-mail inside the VA network (e.g.,

Blackberry) will continue to be authorized. The restriction shall be

enforced, whenever possible, through software modifications and/or

configuration changes at the e-mail gateways. In addition, auditing and/or

monitoring of e-mail traffic shall be employed to verify compliance with

this requirement. Once all Enterprise Cyber Security Infrastructure Program (ECSIP) gateways are operational and all Internet access has been

migrated to the four ECSIP gateway locations, the auditing requirement

will no longer be necessary.

5\. Waivers to the auto-forwarding provisions may be requested through the

respective facility information Security Officer (ISO). Requests deemed

appropriate by the facility IS0 will be forwarded for approval through the

appropriate cyber security chain of command. Waiver requests must include

documentation indicating why alternatives, such as remote access, cannot

be implemented or provide the required capabilities.

6\. In evaluating such waivers, the IS0 must ensure that all available

alternative methods to access e-mail have been sufficiently explored. For

waiver requests to auto-forward e-mail to appropriate partner agencies

such as associated hospitals or educational institutions, a copy of the

HlPAA Business Associate Agreement must be included in the request.

Waivers to auto-forward e-mail to commercial e-mail providers, such as

America Online or Hotmail, will require justification of extraordinary

circumstances to be approved. ISOs will retain waivers on file and

periodically validate accounts with auto-forward enabled.

7\. Some VA e-mail systems allow users to send automatic replies indicating

that they are unavailable during a particular timeframe (i.e.,

"out-of-office" notifications). It is important for VA e-mail users to

remember that these out-of-office notifications may be sent outside of the

VA network to anyone who sends a message to the user's address. Improperly

constructed out-of-office notifications may include sensitive or private VA

information that should not be shared with outside sources. A well

constructed out-of-office notification contains the minimum detail

necessary and should never include information that cannot be disclosed to

the public.

8\. Some VA e-mail distribution lists contain many addresses, including

some that are outside the VA network (i.e., "special recipients"). There

is no obvious indication when a distribution list contains outside

addresses. If a sender is not careful, sensitive or private information

may be sent outside the VA network to people who should not receive it, or

even to inappropriate recipients within the VA network. Senders must

examine distribution lists closely to ensure that they contain only

suitable recipients. In addition, it is important to note that e-mail

distribution lists may include other e-mail distribution lists (i.e.,

"nested lists"), and the members of each nested list must also be

examined.

9\. If there are any questions on this subject, please have a member of

your staff contact REDACTED

/sig./

REDACTED

<span id="_Ref139353122" class="anchor"></span>Figure 10‑1. Auto Forwarding Memorandum: Limits on the Use of Certain E-mail Features and Configurations

### Forwarding Address Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Forwarding Address Edit option allows you to have your mail forwarded to another address. It is located on the Personal Preferences menu, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: personal \<Enter\> Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option: message \<Enter\> Filter Edit

<span id="_Toc436461162" class="anchor"></span>Figure 10‑2. Forwarding Address Edit option

Specifically, the Forwarding Address Edit option asks you to enter the following information:

- Forwarding Address—To what remote address should the mail be routed?
- Local Delivery Flag—Should the mail be sent both remotely and locally or just remotely?

|                                                   |                                                                                                                                                                                                                                                                                                               |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/258.png) | TIP: Forward your e-mail to a remote address when you will be away from the office and will not have access to your local MailMan mailbox. For example, forward your mail to an Internet based e-mail service that can be accessed from any workstation or personal computer with access to the Internet. |

The current functionality of this option is described in greater detail in this chapter.

### Forwarding Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FORWARDING ADDRESS field contains the name of the remote address to which any MailMan messages addressed to you are routed. Only the *original* message gets forwarded, *replies to messages are not forwarded*.

|                                                                                                                |                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/259.png) | NOTE: Broadcast messages will be forwarded like any other messages sent to your mailbox; however, since the Secretary's daily broadcast message on FORUM is sent to all sites, it will not be forwarded from FORUM. |

The remote address must contain the remote name, an at-sign ("@"), and the remote domain name (i.e., name@domain). The entry can be up to 50 characters in length.

Besides routing your mail to a remote address (i.e., FORWARDING ADDRESS field), by setting the LOCAL DELIVERY FLAG field to "On," MailMan will continue to also send your mail to your local MailMan address (i.e., your mailbox). If you set the LOCAL DELIVERY FLAG field to "Off," MailMan will only deliver your mail to the remote address entered into the FORWARDING ADDRESS field and *not* to your local mailbox.

|                                                                                                                |                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/260.png) | REF: For more information on the LOCAL DELIVERY FLAG field, please refer to the "Local Delivery Flag" topic that follows in this chapter. |

Also, if you've set the LOCAL DELIVERY FLAG field to continue to receive mail locally, you may want to choose another MailMan user to act as your surrogate so that they can read your local mail.

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/261.png) | REF: For more information on surrogates, please refer to Chapter 9, "Surrogates," in this manual. |

### Local Delivery Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The value in the LOCAL DELIVERY FLAG field works in conjunction with the FORWARDING ADDRESS field. If the FORWARDING ADDRESS field contains a remote e-mail address, you should also set the LOCAL DELIVERY FLAG field.

MailMan gives you two possible entries for this field:

- No Local Delivery (default)—If you have a FORWARDING ADDRESS and you do *not* want your messages delivered locally, set the LOCAL DELIVERY FLAG field to "Off" (i.e., "0"). Your messages will only be delivered to your remote addresses.
- Local Delivery On—If you have a FORWARDING ADDRESS and you want your messages delivered locally as well as remotely, set the LOCAL DELIVERY FLAG field to "On" (i.e., "1"). Your messages will be delivered to *both* your local and remote addresses.

|                                                   |                                                                                                                                                                                                                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/262.png) | TIP: Since replies to messages are not forwarded, set the LOCAL DELIVERY FLAG field to "On" so that the original message and any replies will still be sent locally. Thus, the replies will not be lost completely and you can read them locally at a later date and time. |

### Enter Your Forwarding Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Forwarding Address Edit option on the Personal Preferences menu to enter a forwarding e-mail address, as shown below:

Select MailMan Menu Option: pers \<Enter\> onal Preferences

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option: forward \<Enter\> ding Address Edit

FORWARDING ADDRESS: xmuser1_one@xxxmail.com

LOCAL DELIVERY FLAG: ?

If this field is not set to 'ON' and the FORWARDING ADDRESS field is

filled in, then messages will only be forwarded, not delivered locally.

Choose from:

0 NO LOCAL DELIVERY

1 LOCAL DELIVERY ON

LOCAL DELIVERY FLAG: 1 \<Enter\> LOCAL DELIVERY ON

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option:

<span id="_Ref431872860" class="anchor"></span>Figure 10‑3. Entering a remote forwarding address

In this example (Figure 10‑3), the user decided to have the mail forward to a remote e-mail address as well as continue to receive the mail locally.

After choosing the Forwarding Address Edit option on the Personal Preferences option menu, MailMan asked the user to enter the remote forwarding address. For this example, the user chose to send the mail to a *non*-MailMan remote e-mail address. Thus, she entered "xmuser1_one@xxxmail.com" at the "FORWARDING ADDRESS:" prompt.

MailMan then prompted the user to choose if she wanted to receive the mail both locally and remotely or just remotely. In this case, the user first entered a question mark ("?") at the "LOCAL DELIVERY FLAG:" prompt in order to display the acceptable entries. After reviewing the choices, she decided to receive the mail both locally and remotely by setting the LOCAL DELIVERY FLAG field to "On." Thus, the user entered "1" ("On") at the "LOCAL DELIVERY FLAG:" prompt.

Since those were the only entries required to forward the mail, MailMan returned the user to the "Select Personal Preferences Option:" prompt where she could take any additional actions.

Also, when you do a detailed query ("QD" action code) on a message that was sent to you and you have forwarded your mail to a remote address, the query clearly shows that you are the one who forwarded the message to that address, as shown below:

Subj: Message Test \[#1233049\] Thu, 10/01/98@09:38:21 PDT

29 lines

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

This is the message text for this message.

Enter message action (in IN basket): IGNORE// qd

Subj: Message Test \[#1233049\] Thu, 10/01/98@09:38:21 PDT

29 lines

From: XMUSER2,TWO M. - PROGRAMMER (OI Field Office Oakland)

In 'IN' basket.

Local Message-ID: 1233049@REDACTED.VA.GOV (3 Recipients)

XMUSER2,TWO M. Last read: 10/01/98@09:44 \[First read: 10/01/98@09:44\]

Forwarded on: 10/01/98@09:42

XMUSER1,ONE E. Last read: 10/02/98@10:31 \[First read: 10/02/98@10:31\]

Forwarded by: XMUSER2,TWO M. 10/01/98@09:45

xmuser1_one@XXXMAIL.COM Sent: 10/01/98@09:45 Time: 0 seconds

Forwarded by: XMUSER1,ONE E. 10/01/98@09:45

Enter message action (in IN basket): IGNORE//

<span id="_Toc436461164" class="anchor"></span>Figure 10‑4. Querying a message that has been forwarded

|                                                                                                                |                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/263.png) | REF: For more information on the Query Detailed action code, please refer to the "Query Detailed ("QD") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

|                                                   |                                                                                                                                                                                                          |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/264.png) | CAUTION: Make sure you do *not* set up two mail systems with forwarding addresses to each other, otherwise you might have the same messages bouncing back and forth between systems in an infinite loop! |

### Delete Your Forwarding Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Forwarding Address Edit option on the Personal Preferences menu to delete a forwarding address, as shown below:

Select Personal Preferences Option: forw \<Enter\> arding Address Edit

FORWARDING ADDRESS: xmuser1_one@xxxmail.com// @

SURE YOU WANT TO DELETE? y\<Enter\> (Yes)

LOCAL DELIVERY FLAG: LOCAL DELIVERY ON// @

SURE YOU WANT TO DELETE? y\<Enter\> (Yes)

User Options Edit

Banner Edit

Surrogate Edit

Message Filter Edit

Delivery Basket Edit

GML Enroll in (or Disenroll from) a Mail Group

Personal Mail Group Edit

Forwarding Address Edit

Select Personal Preferences Option:

<span id="_Ref431874752" class="anchor"></span>Figure 10‑5. Deleting a forwarding address

In this example (Figure 10‑5), the user wanted to delete the forwarding address she previously entered (Figure 10‑3).

After choosing the Forwarding Address Edit option, MailMan prompted the user to enter the remote forwarding address. MailMan displayed the previous entry as the default response (i.e., "xmuser1_one@xxxmail.com").

Since the user wanted to delete the forwarding address, she entered an at-sign ("@") at the "FORWARDING ADDRESS: xmuser1_one@xxxmail.com//" prompt. The user confirmed the deletion by entering "Yes" at the "SURE YOU WANT TO DELETE?" prompt. Thus, the user had successfully deleted the forwarding address.

Since the user no longer was going to forward the mail, she also decided to delete the entry in the LOCAL DELIVERY FLAG field. Thus, the user, again, entered an at-sign ("@") at the "LOCAL DELIVERY FLAG: LOCAL DELIVERY ON//" prompt. Again, she confirmed the deletion by entering "Yes" at the "SURE YOU WANT TO DELETE?" prompt.

After completing the entries, MailMan returned the user to the "Select Personal Preferences Option:" prompt where the user could take any additional actions.

# Reports and Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics to be discussed in this chapter:

- Other MailMan Functions Option
- Get a Report On "Latered" Messages in Your Mailbox
- Change/Delete a Message's "Latered" Date and Time
- Get a List of All Messages in Your Mailbox

MailMan provides several options that give you the opportunity to produce reports (lists) regarding messages in your mailbox and make changes based on information in those reports.

The features and functionality associated with MailMan reports and lists on messages in your mailbox are described in greater detail in this chapter.

### Other MailMan Functions Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan interface provides three options on the Other MailMan Functions menu to report and act on messages in your mailbox:

- Report on Later'd Messages—The Report on Later'd Messages option produces a report that lists all messages in your mailbox that have been "latered" (set to be new again at a future date and time).
- Change/Delete Later'd Messages—You can use the Report on Later'd Messages to determine if any changes need to be made to the "latered" dates and times and make the changes using the Change/Delete Later'd Messages option.
- Mailbox Contents List—The Mailbox Contents List option produces a report that lists *all* messages in either a *single* mail basket or *all* mail baskets in your mailbox.

As stated before, these options are available on the Other MailMan Functions menu, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: other MailMan Functions

Report on Later'd Messages

Change/Delete Later'd Messages

Mailbox Contents List

Select Other MailMan Functions Option:

<span id="_Toc436461166" class="anchor"></span>Figure 11‑1. Other MailMan Functions option

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/265.png)</td>
<td><p><strong>TIP:</strong> Use the Other MailMan Functions option when you wish/need to perform housekeeping chores on your MailMan mailbox. For example, when you want to get an overall idea on how many messages and what mail baskets your mailbox currently contains, use the Mailbox Contents List option to print out a list of all of your mail baskets that includes a summary list of what messages reside in each mail basket. From this list, you may see ways of consolidating and/or eliminating certain baskets, etc.</p>
<p>Also, you can use the Report on Later'd Messages option to review all of your "latered" messages and make any necessary changes. For example, if a project's timeline has shifted and you previously had "latered" messages based on the old timeline, you may want to modify the "latered" dates for those specific messages, related to that project, based on the new timeline. To modify the "latered" dates you would use the Change/Delete Later'd Messages option.</p></td>
</tr>
</tbody>
</table>

Both the current and improved functionality of the Other MailMan Functions option are described in greater detail in this chapter.

### Get a Report On "Latered" Messages in Your Mailbox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Report on Later'd Messages option available on the Other MailMan Functions menu to display a list of messages that you've set to be new at a future date and time ("Latered").

The report provides the following information:

- Date—The date and time the message will be made new (i.e., "latered" date and time). The date includes a one or two-digit month, a one or two-digit day, and a four-digit year for greater clarity (e.g., 7/4/2000).
- Basket—The mailbox basket name where the "latered" message is located.
- Msg ID—The MailMan internal message identification number of the "latered" message.
- Subject—The subject of the "latered" message.

|                                                                                                                |                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/266.png) | REF: For more information on "Latering" messages, please refer to the "Later Messages ("L") Action" topic in Chapter 3, "Reading/Managing Messages—In a Basket," or "Later ("L") Action" topic in Chapter 4, "Reading/Managing Messages—Individual Messages," in this manual. |

To list your "Latered" messages, choose the Report on Later'd Messages option on the Other MailMan Functions menu, as shown below:

Select MailMan Menu Option: other \<Enter\> MailMan Functions

Report on Later'd Messages

Change/Delete Later'd Messages

Mailbox Contents List

Select Other MailMan Functions Option: report \<Enter\> on Later'd Messages

DEVICE: HOME// \<Enter\> Telnet terminal

Later'd Messages Report for: XMUSER1,ONE Page 1

Date Basket Msg ID Subject

-------------------------------------------------------------------------------

07/04/2000 IN 100681 Test2

05/14/2000 IN 100861 Copy Test

11/12/2000 IN 9978572 TEST CONFID

12/24/2000@12:01 IN 9978564 TEST FWD BCAST

Press RETURN to continue: \<Enter\>

Report on Later'd Messages

Change/Delete Later'd Messages

Mailbox Contents List

Select Other MailMan Functions Option:

<span id="_Ref431892807" class="anchor"></span>Figure 11‑2. Listing "latered" messages

As you can see from the previous example (Figure 11‑2), after the user chose the Report on Later'd Messages option, MailMan asked the user to choose where to display the report on "latered" messages (i.e., what device). In this case, the user chose to display the report on the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt.

MailMan then immediately displayed the "Latered" Messages Report. In this case, the user had four messages set to be "new" ("latered") at a future date and time.

|                                                                                                                |                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/267.png) | NOTE: If you want to print your "Latered" Message(s) Report to a different device (e.g., a printer), enter the appropriate device name at the "DEVICE: HOME//" prompt. |

The user can use this report to decide if he wants to modify any of these dates or delete any of the entries using the Change/Delete Later'd Messages option.

|                                                                                                                |                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/268.png) | REF: For more information on the Change/Delete Later'd Messages option, please refer to the "Change/Delete a Message's "Latered" Date and Time" topic that follows in this chapter. |

If you do not have any "latered" messages in your mailbox, MailMan will display the following:

Select Other MailMan Functions Option: report \<Enter\> on Later'd Messages

DEVICE: HOME// \<Enter\> Telnet terminal

Later'd Messages Report for: XMUSER1,ONE E. Page: 1

Date Basket Msg ID Subject

-------------------------------------------------------------------------------

No Later'd Messages

Press RETURN to continue:

Report on Later'd Messages

Change/Delete Later'd Messages

Mailbox Contents List

Select Other MailMan Functions Option:

<span id="_Toc436461168" class="anchor"></span>Figure 11‑3. Listing "latered" messages when you do not have any "latered" messages

### Change/Delete a Message's "Latered" Date and Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the Change/Delete Later'd Messages option available on the Other MailMan Functions menu to do the following to any message with a "latered" date and time:

- Change this Date—Modify the "latered" date and time so that the message will appear as "new" in your mailbox on that future date.
- Delete this Date—Delete the "latered" date and time so that the message will not appear as "new" in your mailbox.

#### Changing a "Latered" Date and Time

To change a "Latered" date and time for a message, choose the Change/Delete Later'd Messages option on the Other MailMan Functions menu, as shown below:

Select Other MailMan Functions Option: change \<Enter\> /Delete Later'd Messages

1 9-24-1998 test 1

2 9-24-1998 test 2

3 9-27-1998 Test Later Delivery for Individual Recipients

4 12-24-1998@12:01:00 test2

CHOOSE 1-4: 4\<Enter\> 12-24-1998@12:01:00 test2

Select one of the following:

C Change this date

D Delete this date

Enter response: c\<Enter\> Change this date

DATE MESSAGE WILL BE NEW: DEC 24,1998@12:01// 12/22/98@11:00a\<Enter\> (DEC 22, 1998@11:00)

Report on Later'd Messages

Change/Delete Later'd Messages

Mailbox Contents List

Select Other MailMan Functions Option:

<span id="_Ref431957425" class="anchor"></span>Figure 11‑4. Changing a message's "later" date and time

In this example (Figure 11‑4), after the user chose the Change/Delete Later'd Messages option, MailMan automatically displayed a numbered list of all messages with a "latered" date and time. In this case, the user had four messages with a "latered" date and time.

This list is similar to the report produced using the Report on Later'd Messages option (Figure 11‑2). This list only displays the following information:

- Date—The date and time the message will be made new (i.e., "latered" date and time).
- Subject—The subject of the "latered" message.

For a more detailed list of "latered" messages, you can use the Report on Later'd Messages option.

|                                                                                                                |                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/269.png) | REF: For more information on the Report on Later'd Messages option, please refer to the "Get a Report On "Latered" Messages in Your Mailbox" topic previously described in this chapter. |

After reviewing the list of "latered" messages, the user chose to modify the "latered" date and time for message number 4 in the list. Thus, the user entered "4" at the "CHOOSE 1-4:" prompt.

MailMan then presented the user with a list of options. Since he wanted to modify the "latered" date, he entered "C" (change) at the "Enter response:" prompt.

The user decided to make this message new again ("latered") for December 22, 1998 at 11:00 a.m. by entering "12/22/98@11:00a" at the "DATE MESSAGE WILL BE NEW: DEC 24,1998@12:01//" prompt.

MailMan confirmed the new date and placed the user back at the "Select Other MailMan Functions Option:" prompt where he could take any additional actions.

When the user redisplayed the list, he saw that the date had been successfully modified, as shown below:

Select Other MailMan Functions Option: change \<Enter\> /Delete Later'd Messages

1 9-24-1998 test 1

2 9-24-1998 test 2

3 9-27-1998 Test Later Delivery for Individual Recipients

4 12-22-1998@11:00:00 test2

CHOOSE 1-4:

<span id="_Toc436461170" class="anchor"></span>Figure 11‑5. List of "latered" messages after changing the date

#### Deleting a "Latered" Date and Time

To delete a "Latered" date and time for a message, choose the Change/Delete Later'd Messages option on the Other MailMan Functions menu, as shown below:

Select Other MailMan Functions Option: chan \<Enter\> ge/Delete Later'd Messages

1 9-24-1998 test 1

2 9-24-1998 test 2

3 9-27-1998 Test Later Delivery for Individual Recipients

4 12-22-1998@11:00:00 test2

CHOOSE 1-4: 1 \<Enter\> 9-24-1998 test1

Select one of the following:

C Change this date

D Delete this date

Enter response: d \<Enter\> Delete this date ... deleted.

Report on Later'd Messages

Change/Delete Later'd Messages

Mailbox Contents List

Select Other MailMan Functions Option: change \<Enter\> /Delete

1 9-24-1998 test 2

2 9-27-1998 Test Later Delivery for Individual Recipients

3 12-24-1998@12:01:00 test2

CHOOSE 1-3:

<span id="_Ref431974391" class="anchor"></span>Figure 11‑6. Deleting a message's "later" date and time

In this example (Figure 11‑6), after the user chose the Change/Delete Later'd Messages option, MailMan automatically displayed a numbered list of all messages with a "latered" date and time. As you can see, the user had four messages with a "latered" date and time.

After reviewing the list of "latered" messages, the user chose to delete the "latered" date and time for message number 1 in the list. Thus, the user entered "1" at the "CHOOSE 1-4:" prompt.

MailMan then presented the user with a list of options. Since he wanted to delete the "latered" date, he entered "D" (delete) at the "Enter response:" prompt.

MailMan confirmed the deletion and placed the user back at the "Select Other MailMan Functions Option:" prompt where he could take any additional actions.

After choosing the Change/Delete Later'd Messages option again, MailMan redisplayed the list and the user could see that the "latered" message he had previously deleted was no longer in the list. Only the "latered" date and time was deleted, the message itself was *not* deleted from the user's mailbox.

### Get a List of All Messages in Your Mailbox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan allows you to list your messages in one or all of your mail baskets in your mailbox through the Mailbox Contents List option on the Other MailMan Functions menu.

The report provides the following information:

- Basket—The mail basket name.
- Message Information—A summary list of information is provided for each message found in the basket. This information includes:
- Message number in that basket
- MailMan internal message identification number (in brackets)
- Date the message was sent
- Subject of the message

#### Listing Messages in *One* Basket

To list all of the messages in one mail basket, choose the Mailbox Contents List option on the Other MailMan Functions menu, as shown below:

Select Other MailMan Functions Option: mail \<Enter\> Box Contents List

Select one of the following:

A All Baskets

O One Basket

List contents of: All Baskets// o\<Enter\> One Basket

List contents of MAIL BASKET: IN// \<Enter\>

DEVICE: HOME// \<Enter\> Telnet terminal

Mailbox Content for XMUSER1,ONE E. - 09/23/98@15:38 Page: 1

-------------------------------------------------------------------------------

Basket: IN

8\. \[1223644\] 08/06/98@13:46 Released XU\*8\*69 SEQ \#74

7\. \[1226249\] 08/25/98@09:36 Local: biweekly info exchange message \# 125

6\. \[1229240\] 09/14/98@06:00 Overdue Equipment: XMUSER1,ONE E.

5\. \[1228792\] 09/10/98@16:41 Memory Walk 98 - Alzheimer's Association

4\. \[1227060\] 08/31/98@06:55 BRX-0898-11246 Server lock

3\. \[1226120\] 08/01/98@10:49 Version 8 Questions for Two (this is NOT a test)

2\. \[1223228\] 08/04/98@08:27 Stress management exercise

1\. \[1220558\] 07/14/98@10:00 FW: Tribal Wisdom vs. Government Policy

Press RETURN to continue: \<Enter\>

Report on Later'd Messages

Change/Delete Later'd Messages

Mailbox Contents List

Select Other MailMan Functions Option:

<span id="_Ref431975603" class="anchor"></span>Figure 11‑7. Listing all messages in one mail basket

In the previous example (Figure 11‑7), the user chose to get a report/list on all of the messages in the "IN" basket.

After choosing the Mailbox Contents List option, MailMan asked the user if he wanted to report on one or all baskets in his mailbox. Since the user only wanted a report on messages in the "IN" mail basket, he entered "O" (one) at the "List contents of: All Baskets//" prompt and pressed the \<Enter\> key at the "List contents of MAIL BASKET: IN//" prompt to accept the "IN" mail basket default.

MailMan then asked the user to choose where to display the "Mailbox Contents List" (i.e., what device). In this case, the user chose to display the list on the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt.

MailMan then displayed the "Mailbox Contents List" for the "IN" mail basket.

|                                                                                                                |                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/270.png) | NOTE: If you want to print your "Mailbox Contents List" to a different device (e.g., a printer), enter the appropriate device name at the "DEVICE: HOME//" prompt. |

After MailMan printed the list, the user pressed the \<Enter\> key and MailMan returned him to the "Select Other MailMan Functions Option:" prompt where he could take any additional actions.

#### Listing Messages in *All* Baskets

To list all of the messages in the user's mailbox, choose the Mailbox Contents List option on the Other MailMan Functions menu, as shown below. For the sake of brevity, let's assume the user only has five mail baskets and three (or fewer) messages in each basket:

Select Other MailMan Functions Option: mail \<Enter\> box Contents List

Select one of the following:

A All Baskets

O One Basket

List contents of: All Baskets// a\<Enter\> All Baskets

DEVICE: HOME// \<Enter\> Telnet terminal

Mailbox Content for XMUSER1,ONE E. - 09/23/98@15:59 Page: 1

-------------------------------------------------------------------------------

Basket: 1 Mail Test

1\. \[1212448\] 05/14/98@07:10 TEST DELIVERY BASKET

Basket: Broadcast

Basket: IN

3\. \[1226120\] 08/24/98@10:49 Patch 50 Questions for Two (this is NOT a

2\. \[1223228\] 08/04/98@08:27 Stress management exercise

1\. \[1220558\] 07/14/98@10:00 FW: Tribal Wisdom vs. Government Policy

Basket: Infrastructure

1\. \[1229971\] 09/17/98@06:16 IMF Team's Weekly Status Report -- 9/17/98

Basket: WASTE

3\. \[1226892\] 08/29/98@00:00 Staggered Delivery Message - Separate Days/

2\. \[1226472\] 08/26/98@13:32 Deferred Test Again

1\. \[1231089\] 09/22/98@09:36 Local: biweekly info exchange message \# 127

Press RETURN to continue: \<Enter\>

Report on Later'd Messages

Change/Delete Later'd Messages

Mailbox Contents List

Select Other MailMan Functions Option:

<span id="_Ref432226195" class="anchor"></span>Figure 11‑8. Listing all messages in all mail baskets

In this example (Figure 11‑8), the user chose to get a report/list on all of the messages in each mail basket in the user's mailbox.

After choosing the Mailbox Contents List option, MailMan asked the user if he wanted to report on one or all baskets in his mailbox. Since the user wanted a report on messages in all of the mail baskets, he entered an "A" (all) at the "List contents of: All Baskets//" prompt.

MailMan then asked the user to choose where to display the "Mailbox Contents List" (i.e., what device). In this case, the user chose to display the list on the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt.

MailMan then displayed the "Mailbox Contents List" for all the messages in each mail basket in the user's mailbox.

|                                                                                                                |                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/271.png) | NOTE: If you want to print your "Mailbox Contents List" to a different device (e.g., a printer), enter the appropriate device name at the "DEVICE: HOME//" prompt. |

As previously stated, the user only had five mail baskets and three (or fewer) messages in each basket.:

- 1 Mail Test—one message
- Broadcast—no messages
- IN—three messages
- Infrastructure—one message
- WASTE—three messages

The mail baskets are displayed in alphabetical order and the messages are listed in the order you specified through the User Options Edit option.

|                                                                                                                |                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/272.png) | REF: For more information on choosing your message display order, please refer to the "Choose Your Message Display Order" topic in Chapter 3 in the *MailMan Getting Started Guide*. |

After MailMan printed the list, the user pressed the \<Enter\> key and MailMan returned him to the "Select Other MailMan Functions Option:" prompt where he could take any additional actions.

# Online Help/Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Topics to be discussed in this chapter:

- Help (User/Group Info., etc.) Option
- User Information
- Remote User Information
- Mail Group Information
- New Features in MailMan
- General MailMan Information
- Frequently Asked Questions About MailMan
- MailMan User’s Manual (Online)

MailMan gives you the opportunity to access Help and other information online. Specifically, MailMan gives you the opportunity to obtain information in the following areas:

- Local and remote user information.
- Mail group information.
- General MailMan information (including an online User Guide).
- New features and functionality introduced with MailMan.
- Frequently asked questions about MailMan.

The features and functionality associated with MailMan Help and information available online are described in greater detail in this chapter.

### Help (User/Group Info., etc.) Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan interface provides seven options on the Help (User/Group Info., etc.) menu to provide information online:

- User Information—This option displays general information on an individual local MailMan user.
- Remote User Information—This option displays general information on an individual remote MailMan user.
- Group Information—This option displays general information on a MailMan mail group.
- New Features in MailMan—This option provides a brief description of new features and functionality introduced with MailMan V. 8.0.
- General MailMan Information—This option displays a general overview on the MailMan e-mail system.
- Questions and Answers on MailMan—This option provides a brief list of frequently asked question and answers with regards to MailMan V. 8.0.
- Manual for MailMan Users—This option provides a compilation of all MailMan help screens into an online User Guide that can be used in conjunction with this manual.

The MailMan Help and online information options previously listed are available on the Help (User/Group Info., etc.) menu, as shown below:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: help

User Information

Group Information

Remote User Information

New Features in MailMan

General MailMan Information

Questions and Answers on MailMan

Manual for MailMan Users

Select Help Option:

<span id="_Toc436461174" class="anchor"></span>Figure 12‑1. Help (User/Group Info., etc.) option

Also, the MailMan online Help system sometimes highlights key words within a block of text (paragraph) using "reverse video." Reverse video is the reversal of light and dark in the display of selected characters on a video screen. For example, if text is normally displayed as black letters on a white background, reverse video presents the text as white letters on a black background. These highlighted key words can be entered at the Help System Action prompt in order to get more information on a subject specific to that key word.

### User Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan gives you the opportunity to obtain information on a local MailMan user through the User Information option on the Help (User/Group Info., etc.) menu option located on the main MailMan Menu.

You can obtain the following local user information:

- Name—The MailMan user's name.
- Banner—The user's current MailMan banner, if any has been entered using the User Options Edit option located on the Personal Preferences menu.

|                                                                                                                |                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/273.png) | REF: For more information on the User Options Edit option and banners, please refer to the "Banners" topic in Chapter 4 in the *MailMan Getting Started Guide*. |

- General MailMan Information—The last date and time the user used MailMan and the status of messages in their mailbox.
- Introduction—The user's introduction, if any has been entered using the User Options Edit option located on the Personal Preferences menu.

|                                                                                                                |                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/274.png) | REF: For more information on the User Options Edit option and the introduction, please refer to the "Introduction" topic in Chapter 4 in the *MailMan Getting Started Guide*. |

- Contact Information—The user's contact information, if any has been entered using the User Options Edit option located on the Personal Preferences menu.

|                                                                                                                |                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/275.png) | REF: For more information on the User Options Edit option and the contact information, please refer to the "Contact Information" topic in Chapter 4 in the *MailMan Getting Started Guide*. |

- Mail Group Information—A list of the mail groups to which this user belongs, if any.

|                                                                                                                |                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/276.png) | REF: For more information on mail groups, please refer to Chapter 8, "Mail Groups," in this manual. |

- Surrogate Information—A list of the MailMan users for whom and in what capacity (i.e., privileges) this user may act as a surrogate, if any. Also, a list of MailMan users who can be surrogates for this user and in what capacity (i.e., privileges).

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/277.png) | REF: For more information on surrogates, please refer to Chapter 9, "Surrogates," in this manual. |

|                                                                                                                |                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/278.png) | NOTE: Only those fields that contain information (data) will be displayed. |

To display general information on a local MailMan user, choose the User Information option on the Help (User/Group Info., etc.) menu, as shown below:

Select Help (User/Group Info., etc.) Option: user \<Enter\> Information

User name: xmuser23,TWENTY3 INFORMATION RESOURCES MGMT.

Last used MailMan: 09/30/98@09:24

Life is made up of the Good, the Bad, and the Ugly - And All Are Interesting

XMUSER23,TWENTY3

Current Banner: Life is made up of the Good, the Bad, and the Ugly - And All Are Interesting

Last used MailMan: 09/30/98@09:24

This user has 3 NEW messages (3 in the IN basket)

Introduction:

The answer is: 42

Private e-mail address: xmuser23@xxx.com

Office phone: 111-555-7777

Mail Groups:

ISC STAFF (Public)

FILEMAN DEVELOPER (Public)

TK73VER (Public)

FMTEAM (Public)

ISC SATELLITE (Public)

INFRASTRUCTURE (Public)

infra (Private)

User name:

<span id="_Ref432233630" class="anchor"></span>Figure 12‑2. Obtaining general information on local MailMan users online

In this example (Figure 12‑2), the user wanted to display general information about a local MailMan user.

As you can see from the previous example, the user chose the User Information option on the Help (User/Group Info., etc.) menu. MailMan asked the user to enter the user's name.

In this case, the user entered the first portion of the user's last name (i.e., "XMUSER23") at the "User name:" prompt.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/279.png) | REF: For more information on entering names, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

MailMan proceeded to display the following information about this local user:

- Name—XMUSER23,TWENTY3
- Banner—"Life is made up of the Good, the Bad, and the Ugly - And All Are Interesting"
- General MailMan Information—
- Last used MailMan: 09/30/98@09:24
- This user has 3 NEW messages (3 in the IN basket)
- Introduction—"The answer is: 42" and "Private e-mail address: xmuser23@xxx.com"
- Contact Information—"Office phone: 111-555-7777"
- Mail Group Information—
- ISC STAFF (Public)
- FILEMAN DEVELOPER (Public)
- TK73VER (Public)
- FMTEAM (Public)
- ISC SATELLITE (Public)
- INFRASTRUCTURE (Public)
- infra (Private)

Since no surrogate information was displayed, the user can conclude that this person is not currently authorized to act as a surrogate for another MailMan user nor does this person have any surrogates authorized to act for him.

After displaying the user information, MailMan returned the user to the "User name:" prompt, where she could enter another user's name.

### Remote User Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan gives you the opportunity to obtain information on a remote MailMan user through the Remote User Information option on the Help (User/Group Info., etc.) menu option located on the main MailMan Menu.

Similar to the NEW PERSON file (#200), which is used to store information on local users, the REMOTE USER DIRECTORY file (#4.2997) is used to store information on remote users at other sites to whom messages can be sent. If they are stored in this file, rather than having to memorize a remote user's e-mail address, you can address them by their last name, first name, or location and MailMan will find them and retrieve their e-mail address for you.

|                                                                                                                |                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/280.png) | NOTE: Only IRM is able to add people to the REMOTE USER DIRECTORY file (#4.2997). |

You can obtain the following remote user information:

- Name—The remote user's name:
- Last Name
- First Name
- Network Address—The remote user's network address.
- Date Entered—The date the remote user was added to the system.
- Date Last Used—The last date and time this remote user's entry was referenced (sent a message from this site).

To display general information on a remote MailMan user, choose the Remote User Information option on the Help (User/Group Info., etc.) menu, as shown below:

Select Help (User/Group Info., etc.) Option: remote \<Enter\> User Information

Enter LASTNAME, Mail Code, or part of LOCATION (one word only): xmuser24 \<Enter\> TWENTY4

LAST NAME: XMUSER24 FIRST NAME: TWENTY4

NETWORK ADDRESS: XMUSER24.TWENTY4@KERNEL.REDACTED.VA.GOV

DATE ENTERED: JAN 18, 1996 DATE LAST USED: MAR 1997

Enter LASTNAME, Mail Code, or part of LOCATION (one word only):

<span id="_Ref432314130" class="anchor"></span>Figure 12‑3. Obtaining general information on remote MailMan users online

In this example (Figure 12‑3), the user wanted to display general information about a remote MailMan user.

As you can see from the previous example, the user chose the Remote User Information option on the Help (User/Group Info., etc.) menu. MailMan asked the user to enter the remote user's name.

In this case, she entered the first portion of the user's last name (i.e., "XMUSER24") at the "Enter LASTNAME, Mail Code, or part of LOCATION (one word only):" prompt.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/281.png) | REF: For more information on entering names, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

MailMan proceeded to display the following information about this remote user:

- Last Name—XMUSER24
- First Name—TWENTY4
- Network Address—XMUSER.TWENTY4@KERNEL.REDACTED.VA.GOV
- Date Entered—JAN 18, 1996
- Date Last Used—MAR 1997

After displaying the remote user information, MailMan returned the user to the "Enter LASTNAME, Mail Code, or part of LOCATION (one word only):" prompt, where she could enter another remote user's name.

### Mail Group Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan gives you the opportunity to obtain information on a mail group through the Group Information option on the Help (User/Group Info., etc.) menu option located on the main MailMan Menu.

You can obtain the following mail group information:

- Name—The name of the mail group. When addressing mail to this mail group name, all members of the mail group will automatically be recipients of the message.
- Type—The type of mail group determines who can send mail to it. Mail groups can be either of the following two types:
- Public
- Private (i.e., Personal Mail Group)

> Provided there are no Authorized Senders specified, anyone can send mail to a Public group and only its members can send mail to a Private group. If there are Authorized Senders specified, only those users can address the group.

|                                                                                                                |                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/282.png) | NOTE: Mail groups created through the Personal Mail Group Edit option are considered private mail groups. |

- Allow Self-Enrollment?—Is self-enrollment allowed ("Yes" or "No")? If "Yes," you can enroll yourself in or disenroll yourself from a mail group. If "No," you must request that the Coordinator or Organizer of the mail group either enroll you in or disenroll you from the group.
- Reference Count—How many times the mail group has been referenced (used).
- Last Referenced—The last date and time this group was referenced (sent a message).
- Restrictions—This field provides the opportunity for the Organizer of the mail group to establish a personal mailing list to use for sending mail in the "G.GROUPNAME" format. Possible values include: UNRESTRICTED, ORGANIZER ONLY, LOCAL, ORGANIZER/LOCAL, INDIVIDUALS, INDIV/ORGANIZER, INDIV/LOCAL, and INDIV/LOCAL/ORGANIZER. If set to "ORGANIZER ONLY," only the organizer is allowed to address the group. The members are simply recipients without any other privileges with respect to the group.
- Coordinator—The person responsible for maintaining the membership of the mail group.

|                                                                                                                |                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/283.png) | NOTE: In order to be a Coordinator, you must hold the XMMGR security key. |

- Description—Description of the mail group.
- Organizer—The organizer is the person who set up/created the mail group. An Organizer can add new members to a Private mail group.
- Authorized Senders—Authorized Senders are the only users who are allowed to send mail to the mail group. Thus, mail groups can have a limited set of senders. If unspecified, then it is assumed that anyone can send mail to this group, if Public, or only members can send to it, if Private. Remote users cannot send mail to any local group that has Authorized Senders. Any messages sent by a remote user to a group with Authorized Senders will be rejected.

|                                                                                                                |                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/284.png) | NOTE: If a user is not an authorized sender for a mail group and he attempts to send mail to the group, the user is shown a list of Authorized Senders. The user can send the message to one of these authorized senders who can forward it to the group, if desired. |

- Member(s)—List of members for the mail group. Members will receive all mail addressed to the group. Members can include any of the following:
- Local and remote users (including fax recipients)
- Other mail groups (local mail groups)
- Distribution lists (nationwide mail groups)

The group information can help you decide if you want to join a particular mail group (i.e., via the description). Also, if a mail group does not allow self-enrollment, you can find out who the Coordinator or Organizer of the group is and ask if you can be enrolled or disenrolled. Also, if a mail group has Authorized Senders, you'll know to whom you should send mail, if you want to address that particular mail group.

IRM may use the REFERENCED COUNT and LAST REFERENCED fields to determine if a mail group should be eliminated. For example, if a mail group has not been referenced (used) in a long time (e.g., LAST REFERENCED field = January 1 1995) or has only been referenced a very few times (i.e., REFERENCED COUNT = 2), they may decide that the mail group should be eliminated.

The following figure (Figure 12‑4) demonstrates how to obtain information on a mail group:

NML New Messages and Responses

RML Read/Manage Messages

SML Send a Message

Query/Search for Messages

AML Become a Surrogate (SHARED,MAIL or Other)

Personal Preferences ...

Other MailMan Functions ...

Help (User/Group Info., etc.) ...

Select MailMan Menu Option: help \<Enter\> (User/Group Info., etc.)

User Information

Group Information

Remote User Information

New Features in MailMan

General MailMan Information

Questions and Answers on MailMan

Manual for MailMan Users

Select Help (User/Group Info., etc.) Option: group \<Enter\> Information

Select MAIL GROUP NAME: TEN \<Enter\>TH FLOOR

NAME: TENTH FLOOR TYPE: public

ALLOW SELF ENROLLMENT?: NO REFERENCE COUNT: 45

LAST REFERENCED: JUL 11, 1997

DESCRIPTION: Mail group for ISC employees located on the 10th floor.

ORGANIZER: XMUSER29,TWENTY9

Member Last Used MailMan

XMUSER30,THIRTY (OI Field Office Oakland) 09/10/98@14:01

XMUSER4,FOUR - Q... Continuum 09/10/98@09:31

XMUSER5,FIVE J. (OI Field Office Oakland) 09/10/98@14:08

XMUSER1,ONE E. - COMPUTER SPECIALIST (OI Fie 09/10/98@14:10

Member of Group: VIRUS ALERT

Select MAIL GROUP NAME:

<span id="_Ref430072624" class="anchor"></span>Figure 12‑4. Obtaining mail group information online

In this example (Figure 12‑4), the user wanted to display general information about a mail group.

As you can see from the previous example, the user chose the Group Information option on the Help (User/Group Info., etc.) menu. MailMan asked the user to enter the mail group's name.

In this case, the user entered the first portion of the "TENTH FLOOR" mail group name at the "Select MAIL GROUP NAME:" prompt.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/285.png) | REF: For more information on entering names, please refer to the "Address Functionality" topic in Chapter 5, "Sending Mail," in this manual. |

After entering the group name, MailMan displayed all of the information about that mail group. You'll notice that the mail group TYPE field has a value of "public." If this mail group had been created as a personal mail group, it would have a value of "private." Also, the user can see that this group does *not* allow self-enrollment. Thus, if the user was not already a member of this group but wanted to join, she would have to contact the Mail Group Organizer (i.e., "XMUSER29,TWENTY9") and ask to be enrolled.

In addition, following the list of individuals in the mail group, MailMan displays the name(s) of any group(s) this mail group belongs to. In this case, you can see that the group is a member of the VIRUS ALERT mail group.

### New Features in MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to this manual, MailMan gives you the opportunity to read about the latest new features and functionality introduced with MailMan V. 8.0 through the New Features in MailMan option on the Help (User/Group Info., etc.) menu option located on the main MailMan Menu.

To display the new features and functionality online, choose the New Features in MailMan option on the Help (User/Group Info., etc.) menu, as shown below:

Select Help (User/Group Info., etc.) Option: new \<Enter\> Features in MailMan

NEW FEATURES AND FUNCTIONALITY IN MAILMAN V. 8.0

1\. MESSAGE READERS - Choose from the CLASSIC, DETAILED Full

Screen, or SUMMARY Full Screen message readers.

2\. FILTER Mail - Create filters to route delivery of your mail to

specific baskets based on the Subject, Sender, and/or Addressees.

3\. SEARCH for mail based on Subject Contents, Sender, Addressee,

Responder, Message Text, and/or Date Sent (e.g., date range).

4\. READING Mail -

\* Capability to make messages NEW or not new.

\* Improved message PRINT functionality.

\* Select messages for subsequent GROUP ACTIONS.

\* Improved ability when PAGING through a long list of messages.

MORE...

Select HELP SYSTEM action or \<return\>:

<span id="_Toc436461179" class="anchor"></span>Figure 12‑5. Displaying the new features and functionality in MailMan online

|                                                                                                                |                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/286.png) | NOTE: Enter the highlighted key words (in reverse video) at the "Select HELP SYSTEM action or \<return\>:" prompt to find out more about a specific topic. Pressing the \<Enter\> key without entering a key word returns you to the previous help topic or the Help options menu. |

### General MailMan Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to this manual, MailMan gives you the opportunity to obtain general information on using the VistA MailMan software through the General MailMan Information option on the Help (User/Group Info., etc.) menu option located on the main MailMan Menu.

To display general information on using MailMan online, choose the General MailMan Information option on the Help (User/Group Info., etc.) menu, as shown below:

Select Help (User/Group Info., etc.) Option: gen \<Enter\> eral MailMan Information

USING MAILMAN

MailMan is a general purpose electronic message system (e-mail). Messages

can be exchanged over communication lines, modems, and other networks. A

message is created with the SEND option. The message then appears in

each recipient's mailbox, to be READ after signon. Messages are tracked

electronically, so that each message's author and readers are identified.

After reading a message, a recipient can select from a variety of

MESSAGE ACTIONS, such as saving it into other mail baskets, deleting it,

forwarding it to others, or replying to it. REPLIES generate new

messages seen by all recipients, creating an ongoing dialog between the

recipients.

Users can FILTER their mail and SEARCH for specific messages. Also,

users can designate SURROGATES to manage mail for them. Users can

'introduce' themselves, provide contact information, and create a banner to

be displayed when a message is sent to them. Users can also choose a

message READER and further CUSTOMIZE the MailMan interface to suit

their needs. GROUPS of users may also be created.

MORE...

Select HELP SYSTEM action or \<return\>:

<span id="_Hlt439480804" class="anchor"></span>Figure 12‑6. Obtaining general MailMan information online

|                                                                                                                |                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/287.png) | NOTE: Enter the highlighted key words (in reverse video) at the "Select HELP SYSTEM action or \<return\>:" prompt to find out more about a specific topic. Pressing the \<Enter\> key without entering a key word returns you to the previous help topic or the Help options menu. |

### Frequently Asked Questions About MailMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan gives you the opportunity to display the frequently asked question and answers regarding MailMan through the Questions and Answers on MailMan option on the Help (User/Group Info., etc.) menu option located on the main MailMan Menu.

To display the frequently asked question and answers online, choose the Questions and Answers on MailMan option on the Help (User/Group Info., etc.) menu, as shown below:

Select Help (User/Group Info., etc.) Option: ques \<Enter\> tions and Answers on MailMan

FREQUENTLY ASKED QUESTIONS ABOUT MAILMAN

1\. RECALLING OR EDITING A MESSAGE AFTER TRANSMISSION

Is there a way to recall or edit a message once it's been sent?

2\. REMOVING A RECIPIENT FROM THE LIST

How can an accidentally chosen recipient be removed from the list?

3\. LOOKING UP A MESSAGE TO BE READ

Is there a way of finding a message if you cannot recall the number?

4\. DISAPPEARED MESSAGES WHICH HAVE NOT BEEN DELETED

Sometimes the read option will show only the message header without

the text. What happened to the original message?

5\. REPLIES TO MESSAGES FROM UNKNOWN RECIPIENTS

Why replies appear in a mailbox to a message which I didn't

originate?

6\. DELETED MESSAGES

Once a message is deleted, is it actually gone from the system?

7\. INTERRUPTED MESSAGES

Can a message be saved temporarily after an interruption?

8\. FILTERING MAIL

Can certain messages be automatically directed to specific baskets?

Select HELP SYSTEM action or \<return\>:

<span id="_Toc436461181" class="anchor"></span>Figure 12‑7. Displaying the Frequently Asked Questions and Answers About MailMan online

|                                                                                                                |                                                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/288.png) | NOTE: Enter the highlighted key words (in reverse video) at the "Select HELP SYSTEM action or \<return\>:" prompt to find out more about a specific topic. Pressing the \<Enter\> key without entering a key word returns you to the previous help topic or the Help options menu. |

### MailMan Users Manual (Online)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to this manual, MailMan gives you the opportunity to display an online User Guide (i.e., compilation of all online help frames) through the Manual for MailMan Users option on the Help (User/Group Info., etc.) menu option located on the main MailMan Menu.

To display this User Guide online, choose the Manual for MailMan Users option on the Help (User/Group Info., etc.) menu, as shown below:

Select Help (User/Group Info., etc.) Option: man \<Enter\> ual for MailMan Users

DEVICE: HOME// \<Enter\> Telnet terminal

DEC 29,1998 13:24 HELP FRAME LISTING i

THE ONLINE MAILMAN USER GUIDE

TABLE OF CONTENTS

-----------------

PAGE

THE ONLINE MAILMAN USER GUIDE ........................ 1

1 USING MAILMAN ......................................... 2

1.1 USING THE 'Send a message' OPTION ..................... 3

1.1.1 SENDING A MESSAGE - ADDRESSING ........................ 4

1.1.1.1 MAIL GROUPS ........................................... 5

1.1.1.1.1 MEMBERS OF MAIL GROUPS ................................ 6

1.1.1.1.2 MAILMAN MAIL GROUP COORDINATORS ....................... 7

Press return to continue or '^' to escape

<span id="_Ref432319081" class="anchor"></span>Figure 12‑8. Displaying the Online Manual User Guide

In this example (Figure 12‑8), the user used the Manual for MailMan Users option to view the Online MailMan User Guide.

MailMan first asked the user to choose where to display the User Guide (i.e., what device). In this case, the user chose to display it to the screen by choosing the default response (i.e., "HOME") by pressing the \<Enter\> key at the "DEVICE: HOME//" prompt.

MailMan then immediately began to display the MailMan User Guide beginning with the Table of Contents.

|                                                                                                                |                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-user-guide/289.png) | NOTE: If you want to display or print the User Guide to a different device (e.g., a printer), enter the appropriate device name at the "DEVICE: HOME//" prompt. |

You can page through the entire User Guide by pressing the \<Enter\> key.

To quit reading the online User Guide and return to the Help menu, enter the caret ("^").

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BANNER               | A line of text with a user's name and domain, which is displayed to everyone who sends mail to the user.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| BLOB                 | Binary Large Objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| BSCP                 | Block Mode Simple Communications Protocol. A procedure used for message transmission with error checking.                                                                                                                                                                                                                                                                                                                                                                                                          |
| BULLETIN             | Electronic mail messages that are automatically delivered by MailMan under certain conditions. For example, a bulletin can be set up to fire when database changes occur, such as adding a record to the file of users.                                                                                                                                                                                                                                                                                                            |
| DOMAIN               | A site for sending and receiving mail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| LOCAL                | The system to which a user is currently signed on.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MAIL BASKET          | Mail baskets provide a way of saving messages in a sorted fashion similar to a filing system. Mail baskets are created at the "message action" prompt by typing an "S" to save and then the name you wish to call the basket. If the basket already exists, the message will be put in it. If the basket does not exist, you will be asked if you want it created. Placing a message in a mail basket other than the "IN" or "WASTE" baskets protects the message from being automatically purged when the IN BASKET PURGE is run. |
| MAILMAN              | The VistA software that provides a mechanism for handling electronic communication, whether it is user-oriented mail messages, automatic firing of bulletins, or initiation of server-handled data transmissions.                                                                                                                                                                                                                                                                                                                  |
| MESSAGE-ID           | A message identifier which shows the message number and the domain name of the message.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MIME                 | Multipurpose Internet Mail Extension. A standard that allows you to create structured message bodies.                                                                                                                                                                                                                                                                                                                                                                                                              |
| MULTIMEDIA MAIL      | Multimedia Mail gives the capability of attaching Binary Large Objects (BLOBs) to electronic messages so that images, spreadsheets, graphs, and other operating system files that are not pure ASCII text, can be sent and received either locally or across the network.                                                                                                                                                                                                                                                          |
| PERIPHERAL DEVICE    | Any hardware device other than the computer itself (central processing unit plus internal memory). Typical examples include card readers, printers, CRT units, and disk drives.                                                                                                                                                                                                                                                                                                                                                    |
| PHYSICAL LINK DEVICE | Hardware used to establish outgoing communication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| "PLAYING A SCRIPT"   | A method of opening a transmission link for a message. It is used to force message transmission and testing.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| POLLER               | An option that opens the transmission line to all domains with "P" in the Flags field.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| POSTMASTER           | The basket where message queues are stored. Also, the person who manages this basket for a particular site.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PROTOCOL             | Code containing logic for opening and closing links, and for sending/receiving transmissions.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PURGE                | In VistA MailMan, a procedure used to delete messages or message pointers.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| QUEUE                | A list that stores messages destined for a given domain.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| QUEUING              | Requesting that a job be processed in the background rather than in the foreground within the current session. Jobs are processed sequentially (first-in, first-out). The Kernel's TaskMan handles the queuing of tasks.                                                                                                                                                                                                                                                                                                           |
| REMOTE               | Any system which a user is not signed on to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SCRIPT               | A set of MailMan commands and transmission scripts to a remote domain in the DOMAIN file (#4.2).                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SERVER               | In VistA MailMan, an automatic mail reader for internal messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SMTP                 | Simple Mail Transport Protocol. The primary transport protocol for MailMan                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SURROGATE            | A person who is authorized to read and/or send mail in another user's name.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| TRANSMISSION SCRIPT  | List of commands for directing a message stored in the TRANSMISSION SCRIPT field.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VALIDATION NUMBER    | A security check number that *must* be in both the sending and receiving sites' domains.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| WRAP-AROUND MODE     | Text that is fit into available column positions and automatically wraps to the next line, sometimes by splitting at word boundaries (spaces).                                                                                                                                                                                                                                                                                                                                                                                     |
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-user-guide/290.png)</td>
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

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Acronyms (ISS)
Home Page Web Address, Glossary, 3
Action Codes
Answer a Message, 4-5
Backup
When Sending Messages, 5-38
While Reading a Message, 4-9
Basket Message Lists, 3-5
Canceling Messages Before Sending, 5-65
Caret Exit
Baskets, 3-66
Messages, 4-86
Change Basket Name, 3-18
Change Detail, 3-19
Closed Message, 5-64
Confidential Messages, 5-39
Confirm Receipt, 5-58
Copy a Message, 4-13
Delete a Message, 4-16, 4-78
Delete Messages In a Basket, 3-23, 3-55
Delivery Basket Set, 5-41
Edit Message, 4-17
Edit Recipients, 5-44
Edit Subject, 5-46
Edit Text, 5-48
Extract KIDS or PackMan Messages, 4-85
Filter Messages, 7-15
Filter Messages In a Basket, 3-29
Forward a Message, 4-19
Forward Messages In a Basket, 3-27
Group Actions, Messages, 3-10
Headerless Print a Message, 4-21
Headerless Print Messages In a Basket, 3-32, 3-42
Ignore a Message, 4-28
Include Message, 4-29
Include Responses When Replying to a Message, 4-62
Information Only
For Messages Sent By You, 4-17, 4-32
When Sending Messages, 5-50
Later a Message, 4-34
Later Messages In a Basket, 3-34
Messages, 4-3
Network Signature
When Sending Messages, 5-55
New Message List, 3-36
New Toggle, 3-37
New/Un New a Message, 4-37
Opposite Selection Toggle, 3-39
Paging, 3-61
Print
To Browser, 4-11
Print Message, 4-38
Print Messages In a Basket, 3-32, 3-42
Priority Delivery, 5-57
Priority Replies, 4-33
Query
(Search for) Messages In a Basket, 3-46
Current, 4-46
Detailed, 4-49
Network, 4-52
Not Current, 4-57
Recipients, 4-43
Terminated, 4-59
Query Addressees to a Message, 4-41
Reply to a Message, 4-62
Resequence Messages In a Basket, 3-51
Save a Message, 4-76
Save Messages To Another Basket, 3-53
Scramble, 5-59
Sending Messages, 5-37
Terminate a Message, 4-16, 4-78
Terminate Messages In a Basket, 3-23, 3-55
Text String Search, 3-63
Transmit Later, 5-11, 5-26, 5-27, 5-52
Transmit Now, 5-26, 5-27, 5-61
Vaporize Date Edit, 3-57, 4-79
Vaporize Date Set, 5-62
Write a Message, 4-82
Zoom Selection Toggle, 3-59
Address, Forwarding Your Mail, 10-5, 10-6
Addressing
Broadcast Messages, 5-19
Editing, 5-44
Functionality, 5-7
Groups, 5-7, 5-8
Mail Groups, 5-7, 5-8
Prefix Codes, 5-16
Unknown Users (Local or Remote), 5-14
Users, 5-7
Using the DUZ, 5-7
Adobe Acrobat Quick Guide Web Address, xx
Adobe Home Page Web Address, xx
All Messages Search, 6-6
AML
Become a Surrogate (SHARED,MAIL or Other) Option, 9-3, 9-4, 9-5, 9-13
Answer a Message Action Code, 4-5
Answers and Questions About MailMan Online, 12-16
ASK BASKET Field, 5-5
Assumptions About the Reader, xix
Authorized Senders, 12-10
Authorized Senders of a Mail Group, 8-1, 12-10
AUTO-FORWARD APPROVED SITE Multiple Field (#31.1), 10-2
AUTO-FORWARD LIMITED? field (#31), 10-2
AUTO-FORWARD WAIVER SITE Multiple field (#31.2), 10-2
AUTOMATIC DELETION DATE Field, 3-57, 4-79, 5-62
B
Backup Action Code
When Sending Messages, 5-38
While Reading a Message, 4-9
Basket Message Number, 3-8
Baskets
Action Codes, 3-5
Caret Exit Action, 3-66
Change Basket Name, 3-18
Change Detail, 3-19
Create, 4-76
Delete Messages In a Basket, 3-23, 3-55
Deleting a Mail Basket, 3-24
Filter Messages, 7-15
Filter Messages In a Basket, 3-29
Forward Messages In a Basket, 3-27
Headerless Print Messages In a Basket, 3-32, 3-42
Later Messages In a Basket, 3-34
List Baskets With New Mail, 2-7
Listing Messages in All Baskets, 11-12
Listing Messages in One Basket, 11-11
Message List Action Codes, 3-5
Message Location, 2-9, 11-5, 11-10
New Message List, 3-36
New Toggle, 3-37
Opposite Selection Toggle, 3-39
Paging, 3-61
Print Messages In a Basket, 3-32, 3-42
Query
Messages In a Basket Action Code, 3-46
Read all Your New Mail, 2-5
Resequence Messages, 3-51
Save Messages To Another Basket, 3-53
Search for Messages In a Basket Action Code, 3-46
Searching for Messages in a Specific Basket, 6-13, 6-18
Searching for Messages in Your Mailbox, 6-9
Setting a Delivery Basket, 5-41
Terminate Messages In a Basket, 3-23, 3-55
Text String Search Actions, 3-63
Zoom Selection Toggle, 3-59
Become a Surrogate (SHARED,MAIL or Other) Option, 9-3, 9-4, 9-5, 9-13
Become a Surrogate, How to, 9-3
BIG GROUP SIZE Field, 5-8
BIG GROUP SIZE Field (#7.2), 5-8
Body of Message
Editing, 5-48
Boolean Expression, 3-46, 6-5
Broadcast Messages, 5-19
Bulletins
XM GROUP EDIT NOTIFY, 8-7
C
Callout Boxes, xviii
Canceling Messages Before Sending Action Code, 5-65
Carbon Copy Prefix Code, 5-17
Caret, 2-10, 2-13, 2-16, 2-17, 2-19, 3-7, 3-46, 3-50, 3-66, 4-4, 4-28, 4-63, 4-86, 5-37, 5-45, 5-66, 6-5, 6-13, 6-18, 6-22, 7-17, 12-18
Canceling Messages Before Sending, 5-65
Exit Action, 3-66, 4-86
Baskets, 3-66
Messages, 4-86
Exiting a Message with Unread Responses, 2-19
Quit Reading New Messages, 2-6
Change Detail Action Code, 3-19
Change/Delete Later'd Messages Option, 3-34, 4-34, 11-3, 11-6, 11-7, 11-9
Changing
Basket Name Action Code, 3-18
Later'd Dates, 11-7
Closed Message Action Code, 5-64
Command Action Codes
Basket Message Lists, 3-5
Messages, 4-3
Sending Messages, 5-37
Completing
Interrupted
Messages, 5-33
Replies, 4-75
Composing Messages, 5-3
Confidential Action Code, 5-39
Configure
Delivery Basket Edit Option, 5-41
User Options Edit Option, 3-62, 4-33, 5-57
Confirm Receipt Action Code, 5-58
Contents, v
Coordinator For a Mail Group, 8-3, 12-10, 12-11
Copy a Message Action Code, 4-13
Creating
Baskets, 4-76
Forwarding Address, 10-8
Mail Filters, 7-6
New Filters, How to, 7-6
Personal Mail Groups, 8-10
Creating and Sending Messages, 5-3
Criteria
Mail Filters, 7-4
Search for Messages, 6-3
D
Data Dictionary
Data Dictionary Utilities Menu, xix
Listings, xix
Decode Messages, 5-59
Deferred Send Action Code, 5-11, 5-26, 5-27, 5-52
Delete Message Action Code, 4-16, 4-78
Deleting
A Message's Latered Date and Time, 11-9, 11-10
Forwarding Address, 10-10
Later'd Dates, 11-7
Mail Baskets, 3-24
Mail Baskets, How to, 3-24
Mail Filters, 7-16
Messages in a Basket Action Code, 3-55
Messages In a Basket Action Code, 3-23
Personal Mail Groups, 8-16
Setting Vaporization Date for Individual Messages, 4-80
Setting Vaporization Date for Multiple Messages, 3-57
Surrogates, 9-14
Vaporization Date, 4-81
Deliver Message Later (Staggered), 5-18, 5-26, 5-27
Delivery Basket Edit Option, 5-41
Delivery Basket Set Action Code, 5-41
Delivery Options, 5-26
Deferred Send, 5-11, 5-26, 5-27, 5-52
Staggered Delivery, 5-18, 5-26, 5-27
Transmit Later, 5-11, 5-26, 5-27, 5-52
Transmit Now, 5-26, 5-27, 5-61
Description of a Mail Group, 12-10
Deselecting Messages, 3-15
Designating
Messages As Priority, 5-57
Surrogates, 9-12
Detail List of Recipients, 3-33, 3-45, 4-22, 4-39
Devices
Choosing, 2-14, 3-32, 3-33, 3-42, 3-43, 3-45, 4-22, 4-38, 4-39, 4-40, 11-6, 11-11, 11-12, 11-13, 12-17
P-MESSAGE, 5-34
Disenroll from a Mail Group, 8-2, 8-3, 8-6, 8-8
Disenroll From Mail Groups, 8-8
Documentation
History, iii
Symbols, xvii
DROP OUT OF RESTRICTED GROUP Field (#22), 8-3, 8-4
DUZ, Addressing Mail Using the, 5-7
E
Edit
Message Action Code, 4-17
Recipients Action Code, 5-44
Subject Action Code, 5-46
Task Option, 5-54
Text Action Code, 5-48
Editing
AUTOMATIC DELETION DATE Field, 5-62
Existing Filters, 7-10
Forwarding Address, 10-5, 10-8
Messages, 4-17
Personal Mail Groups, 8-2, 8-4, 8-9, 8-10, 8-13, 8-16, 12-10
Recipients, 5-44
Subject, 5-46
Text, 5-48
Vaporize Date, 3-57, 4-79, 5-62
Encode Messages, 5-59
Enroll in (or Disenroll from) a Mail Group Option, 8-2, 8-3, 8-6, 8-8
Enroll in Mail Groups, 8-6
Enter To Page Forward, 3-61
Establishing Filter Order, 7-5
EVS Anonymous Directories, xx
EXISTING BASKETS ONLY (Response For Delivery Basket Privileges), 5-43
Exit
How to
Quit the New Messages Option, 2-17
Exit Action, Caret
Baskets, 3-66
Messages, 4-86
Exiting a Message with Unread Responses, 2-19
Extract KIDS or PackMan Messages Action Code, 4-85
F
Features
New in MailMan, 12-14
Fields
AUTO-FORWARD APPROVED SITE Multiple (#31.1), 10-2
AUTO-FORWARD LIMITED? (#31), 10-2
AUTO-FORWARD WAIVER SITE Multiple (#31.2), 10-2
AUTOMATIC DELETION DATE, 3-57, 4-79
BIG GROUP SIZE Field (#7.2), 5-8
DROP OUT OF RESTRICTED GROUP (#22), 8-3, 8-4
IN-BASKET PURGE, 3-57, 4-79
SHOW DUZ WHEN ADDRESS MESSAGE (#7.3), 5-7, 5-8
Figures and Tables, xi
Files
MAILMAN SITE PARAMETERS (#4.3), 4-20, 5-7, 5-8, 8-3, 8-4, 10-2
MESSAGE (#3.9), 3-3, 3-8, 3-10, 6-2, 6-6, 6-7
NEW PERSON (#200), 5-19, 12-8
REMOTE USER DIRECTORY (#4.2997), 12-8
Filter Messages Action Code, 7-15
FILTER MESSAGES Field, 7-3
Filter Messages In a Basket Action Code, 3-29
Filtering Criteria, 3-29
Filtering Mail, 7-1
Criteria, 7-4
FILTER MESSAGES Field, 7-3
How to
Create New Filters, 7-6
Delete
Mail Filters, 7-16
Edit
Existing Filters, 7-10
Modify Mail Filters, 7-11
ORDER Field, 7-3, 7-5
Overridden, 7-3
STATUS Field, 7-3
Filters, 3-29, 5-41
Find Messages, 3-46, 6-1
In a Particular Basket, 6-18
In A Particular Basket, 6-13
Only In Your Mailbox, 6-9
Search All Messages, 6-6
Search Criteria, 6-3
Where, 6-2
Flags, 2-9, 3-20, 3-21, 5-57
Forward a Message Action Code, 4-19
Forward Messages In a Basket Action Code, 3-27
Forwarding
Address, 10-5, 10-6
How to
Delete
Your Forwarding Address, 10-10
Enter Your Forwarding Address, 10-8
Local Delivery Flag, 10-5, 10-7
Local Delivery On, 10-7
Mail, 10-1
No Local Delivery, 10-7
Forwarding Address Edit Option, 10-5, 10-8, 10-10
Frequently Asked Questions About MailMan, 12-16
From, 2-9, 3-20, 3-21, 3-29, 3-32, 3-42, 4-41, 4-43, 4-46, 4-49, 4-52, 4-55, 4-56, 4-57, 4-59, 4-73, 5-38, 7-4, 9-11
FTP, xx
G
Gaps, 3-51
General MailMan Information, 12-15
General MailMan Information Option, 12-15
Glossary, 1
ISS Home Page Web Address, Glossary, 3
GML
Disenroll from a Mail Group, 8-2, 8-3, 8-6, 8-8
Enroll in (or Disenroll from) a Mail Group Option, 8-2, 8-3, 8-6, 8-8
Group Actions, 3-10
Deselecting a Group of Messages, 3-16
Deselecting All Messages, 3-17
Deselecting One Message, 3-15
Selecting a Group of Messages, 3-13
Selecting All Messages, 3-14
Selecting One Message, 3-12
Group Information Option, 8-9, 8-12, 8-15, 12-10
Groups, 8-1
Addressing, 5-7, 5-8
Authorized Senders, 8-1, 12-10
Coordinator, 8-3, 12-10, 12-11
Description, 12-10
Entering Names, 5-7
How to
Create Personal Mail Groups, 8-10
Delete
Personal Mail Groups, 8-16
Disenroll, 8-8
Edit
Personal Mail Groups, 8-13
Enroll, 8-6
Obtain
Mail Group Information Online, 12-10
Last Referenced, 12-10
Members, 12-11
Organizer, 8-3, 8-9, 12-10, 12-11
Personal Mail Group Edit Option, 8-2, 8-4, 8-9, 8-10, 8-13, 8-16, 12-10
Personal Mail Groups Overview, 8-9
Reference Count, 12-10
Restrictions, 12-10
Self-Enrollment, 12-10
Type, 12-10
H
Having Your Mail Automatically Forwarded, 10-1
Header, 3-32, 3-42, 3-43, 3-45, 4-21, 4-22, 4-39, 4-41, 4-43, 4-44, 4-46, 4-49, 4-52, 4-57, 4-59, 4-73, 4-81, 5-21, 5-24, 5-38, 9-11
Network, 4-52
Trace, 4-52
Headerless Print a Message Action Code, 4-21
Headerless Print Messages In a Basket Action Code, 3-32, 3-42
Help
At Prompts, xviii
Online, xviii
Question Marks, xviii
Help (User/Group Info., etc.)
General MailMan Information Option, 12-15
Group Information Option, 8-9, 8-12, 8-15, 12-10
Manual for MailMan Users Option, 12-17
New Features in MailMan Option, 12-14
Questions and Answers on MailMan Option, 12-16
Remote User Information Option, 12-8
User Information Option, 12-5
Help (User/Group Info., etc.) Option, 8-2, 8-9, 8-12, 8-15, 12-3, 12-5, 12-6, 12-8, 12-10, 12-14, 12-15, 12-16, 12-17
Help/Information Online, 12-1
Frequently Asked Questions About MailMan, 12-16
How to
Obtain
General MailMan Information, 12-15
Mail Group Information, 12-10
Remote User Information, 12-8
User Information, 12-5
MailMan Users Manual, 12-17
New Features in MailMan, 12-14
Hint, Scramble, 5-59
History, Revisions to Documentation and Patches, iii
Home Pages
Adobe Acrobat Quick Guide Web Address, xx
Adobe Web Address, xx
HSD&D Home Page Web Address, xix
ISS
Acronyms Home Page Web Address, Glossary, 3
Glossary Home Page Web Address, Glossary, 3
MailMan Home Page Web Address, xx
VistA Documentation Library (VDL) Home Page Web Address, xx
How to
Become a Surrogate, 9-3
Change a Message's Latered Date and Time, 11-7
Change/Delete a Message's, 11-7
Create New Filters, 7-6
Create Personal Mail Groups, 8-10
Delete
Mail Baskets, 3-24
Mail Filters, 7-16
Message's Latered Date and Time, 11-9
Personal Mail Groups, 8-16
Your Forwarding Address, 10-10
Designate a Surrogate, 9-12
Disenroll From Mail Groups, 8-8
Edit
Existing Filters, 7-10
Personal Mail Groups, 8-13
Enroll in Mail Groups, 8-6
Enter Your Forwarding Address, 10-8
Exit a Message with Unread Responses, 2-19
Get a List of All Messages in Your Mailbox, 11-10
Get a Report On Latered Messages in Your Mailbox, 11-5
List All of Your Baskets with New Mail, 2-7
List All of Your New Messages, 2-9
List All of Your Priority Messages, 2-11
Modify Mail Filters, 7-11
Obtain
General MailMan Information, 12-15
Mail Group Information, 12-10
Remote User Information, 12-8
Technical Information Online, xviii
User Information, 12-5
Print All of Your New Messages, 2-14
Quit—Exiting the New Messages Option, 2-17
Read All of Your New Mail by Basket, 2-5
Remove a Surrogate, 9-14
Respond to a Message, 4-64
Scan All of Your New Messages, 2-16
Stop Reading a Message, 2-19
Use this Manual, xvii
View
Frequently Asked Questions About MailMan (Online), 12-16
MailMan Users Manual (Online), 12-17
New Features in MailMan (Online), 12-14
HSD&D
Home Page Web Address, xix
I
Ignore a Message Action Code, 4-28
IN-BASKET PURGE Field, 3-57, 4-79, 5-62
Include Message Action Codes, 4-29
Index of Respondents, 4-10, 4-14, 4-67
Information
Online, 12-1
Frequently Asked Questions About MailMan, 12-16
How to
Obtain
General MailMan Information, 12-15
Mail Group Information, 12-10
Remote User Information, 12-8
User Information, 12-5
MailMan Users Manual, 12-17
New Features in MailMan, 12-14
Information Only
Action Code
For Messages Sent By You, 4-17, 4-32
When Sending Messages, 5-50
Prefix Code, 5-17, 5-51
Internal Message Identification Number, 2-9, 2-10, 2-13, 3-5, 3-6, 3-8, 3-9, 3-19, 3-21, 3-51, 4-41, 4-43, 4-46, 4-49, 4-57, 4-59, 5-52, 11-5, 11-10
Interrupted
Messages, Completing, 5-33
Replies, Completing, 4-75
Introduction To MailMan User Manual, 1-1
IRM
BIG GROUP SIZE Field, 5-8
BIG GROUP SIZE Field (#7.2), 5-8
P-MESSAGE Device, 5-34
ISS
Acronyms
Home Page Web Address, Glossary, 3
Glossary
Home Page Web Address, Glossary, 3
L
LAST REFERENCED Field, 12-10, 12-11
Later
Message Action Code, 4-34
Messages In a Basket Action Code, 3-34
Prefix Code, 5-18, 5-26, 5-27
Lines, 2-9, 3-19, 3-21
List All of Your Baskets with New Mail, How to, 2-7
List All of Your New Messages, How to, 2-9
List All of Your Priority Messages, How to, 2-11
List File Attributes Option, xix
Lists and Reports, 11-1
How to
Change a Message's Latered Date and Time, 11-7
Change/Delete a Message's, 11-7
Delete
Message's Latered Date and Time, 11-9
Get a List of All Messages in Your Mailbox, 11-10
Get a Report On Latered Messages in Your Mailbox, 11-5
Local Delivery Flag, 10-5, 10-7
Local Delivery On (Response When Having Your Mail Forwarded), 10-7
Looking for Messages, 3-46, 6-1
In a Particular Basket, 6-18
In A Particular Basket, 6-13
Only In Your Mailbox, 6-9
Search All Messages, 6-6
Search Criteria, 6-3
Where, 6-2
M
Mail
Filtering, 7-1
Forwarding, 10-1
Searching, 6-1
Sending, 5-1
Mail Filters, 3-29, 5-41
Criteria, 7-4
FILTER MESSAGES Field, 7-3
How to
Create New Filters, 7-6
Delete
Mail Filters, 7-16
Edit
Existing Filters, 7-10
Modify Mail Filters, 7-11
ORDER Field, 7-3, 7-5
Overridden, 7-3
STATUS Field, 7-3
Mail Group Information Online, 12-10
Mail Group Options, 8-2
Mail Groups, 8-1
Addressing, 5-7, 5-8
Authorized Senders, 8-1, 12-10
Coordinator, 8-3, 12-10, 12-11
Description, 12-10
Enroll In or Disenroll from a Mail Group, 8-2, 8-3, 8-6, 8-8
Entering Names, 5-7
How to
Create Personal Mail Groups, 8-10
Delete
Personal Mail Groups, 8-16
Disenroll, 8-8
Edit
Personal Mail Groups, 8-13
Enroll, 8-6
Obtain
Mail Group Information Online, 12-10
Information Option, 8-9, 8-12, 8-15, 12-10
Last Referenced, 12-10
Members, 12-11
Organizer, 8-3, 8-9, 12-10, 12-11
Personal Mail Group Edit Option, 8-2, 8-4, 8-9, 8-10, 8-13, 8-16, 12-10
Personal Mail Groups Overview, 8-9
Reference Count, 12-10
Restrictions, 12-10
Self-Enrollment, 12-10
Type, 12-10
Mailbox
Get a Report On Latered Messages in Your Mailbox, 11-5
Mailbox Contents List Option, 11-3
Messages Search, 6-9
Mailbox Contents List Option, 11-3, 11-10, 11-11, 11-12
MailMan
Home Page Web Address, xx
Information Online, 12-15
Menu Structure, 1-2
Users Manual Online, 12-17
MailMan Menu, 1-2
MAILMAN SITE PARAMETERS File (#4.3), 4-20, 5-7, 5-8, 8-3, 8-4, 10-2
Managing
Individual Messages, 4-1
Mail In Your MailMan Message Center, 1-1
Messages in a Basket, 3-1
New Messages and Responses, 2-1
Manual for MailMan Users Option, 12-17
Members, Mail Groups, 12-11
Menus
Data Dictionary Utilities, xix
MailMan Menu, 1-2
MailMan Menu Structure, 1-2
XMUSER, 1-2
MESSAGE File (#3.9), 3-3, 3-8, 3-10, 6-2, 6-6, 6-7
Message Filter Edit Option, 7-2, 7-3, 7-4, 7-7, 7-10, 7-14, 7-16
Message Numbers, 2-9, 2-10, 2-13, 3-5, 3-8, 3-20, 3-21
MESSAGE ORDER Field, 3-62
Message Sent Date, 2-9, 3-19, 3-21
Messages
Action Codes, 4-3
Answer a Message, 4-5
Backup a Message, 4-9
Carbon Copy, 5-17
Caret Exit Action, 4-86
Copy a Message, 4-13
Delete a Message, 4-16, 4-78
Edit Message, 4-17
Exiting a Message with Unread Responses, How to, 2-19
Extract KIDS or PackMan Messages, 4-85
Forward a Message, 4-19
Group Actions, 3-10
Header, 3-32, 3-42, 3-43, 3-45, 4-21, 4-22, 4-39, 4-41, 4-43, 4-44, 4-46, 4-49, 4-52, 4-57, 4-59, 4-73, 4-81, 5-21, 5-24, 5-38, 9-11
Headerless Print a Message, 4-21
How to
List All Priority Messages, 2-11
List All Your New Messages, 2-9
Print All of Your New Messages, 2-14
Scan All of Your New Messages, 2-16
Ignore a Message, 4-28
Include Message, 4-29
Information Only Action Code
For Messages Sent By You, 4-17, 4-32
When Sending Messages, 5-50
Information Only Prefix Code, 5-17, 5-51
Later, 4-34
Make
New Again, 4-37
New at a Later Date and Time, 4-34
Un New, 4-37
Move, 4-76
New/Un New a Message, 4-37
Print
Message, 4-38
To Browser, 4-11
Priority Replies, 4-33
Query
Addressees to a Message, 4-41
Current, 4-46
Detailed, 4-49
Network, 4-52
Not Current, 4-57
Recipients, 4-43
Terminated, 4-59
Remove Recipient (Minus), 5-18
Reply to a Message, 4-62
Save a Message, 4-76
Search
All Messages, 6-6
Messages in Your Mailbox, 6-9
Sending Action Codes, 5-37
Staggered Delivery (Later), 5-18, 5-26, 5-27
Stop Reading a Message, 2-19
Subject, 2-9, 3-20, 3-21, 3-29, 3-32, 3-42, 3-46, 4-41, 4-43, 4-46, 4-49, 4-57, 4-59, 5-37, 6-2, 6-3, 6-9, 7-4, 11-5, 11-7, 11-10
Editing, 5-46
Terminate a Message, 4-16, 4-78
Vaporize Date Edit, 3-57, 4-79
Write a Message, 4-82
Minus
Number, 3-61
Recipients, 5-18
Sign, 3-61
Modifying
Mail Filters, 7-11
Move Messages, 4-76
N
Names
Addressing Users or Mail Groups, 5-7
Network
Header, 4-52
Information, 4-52
Signature, 4-5, 4-8, 5-55
Signature Action Code
When Sending Messages, 5-55
New Features in MailMan, 12-14
New Features in MailMan Option, 12-14
New Message List Action Code, 3-36
New Messages and Responses Option, 2-3, 2-5, 2-7, 2-9, 2-12, 2-14, 2-16, 2-17, 4-2
New Messages, How to List All, 2-9
NEW PERSON File (#200), 5-19, 12-8
New Toggle Action Code, 3-37
New/Un New a Message Action Code, 4-37
NML
New Messages and Responses Option, 2-12
New Messages and Responses Option, 2-3, 2-5, 2-7, 2-9
New Messages and Responses Option, 2-14
New Messages and Responses Option, 2-16
New Messages and Responses Option, 2-17
New Messages and Responses Option, 4-2
No Local Delivery (Default Response When Having Your Mail Forwarded), 10-7
NO, DON'T ACCEPT IT (Default Response For Delivery Basket Privileges), 5-43
O
Online
Documentation, xviii
Technical Information, How to Obtain, xviii
Online Help/Information, 12-1
Frequently Asked Questions About MailMan, 12-16
How to
Obtain, 12-15
Obtain
Mail Group Information, 12-10
Remote User Information, 12-8
User Information, 12-5
Manual for MailMan Users, 12-17
New Features in MailMan, 12-14
Opposite Selection Toggle Action Code, 3-11, 3-39
Options
Become a Surrogate (SHARED,MAIL or Other), 9-3, 9-4, 9-5, 9-13
Change/Delete Later'd Messages Option, 3-34, 4-34, 11-3, 11-6, 11-7, 11-9
Data Dictionary Utilities, xix
Delivery Basket Edit, 5-41
Enroll in (or Disenroll from) a Mail Group, 8-2, 8-3, 8-6, 8-8
Forwarding Address Edit, 10-5, 10-8, 10-10
General MailMan Information Option, 12-15
Group Information, 8-9, 8-12, 8-15, 12-10
Help (User/Group Info., etc.), 8-2, 8-9, 8-12, 8-15, 12-3, 12-5, 12-6, 12-8, 12-10, 12-14, 12-15, 12-16, 12-17
List File Attributes, xix
Mail Groups, 8-2
Mailbox Contents List Option, 11-3, 11-10, 11-11, 11-12
MailMan Menu, 1-2
MailMan Menu Structure, 1-2
Manual for MailMan Users Option, 12-17
Message Filter Edit, 7-2, 7-3, 7-4, 7-7, 7-10, 7-14, 7-16
New Features in MailMan, 12-14
New Messages and Responses, 2-3, 2-5, 2-7, 2-9, 2-12, 2-14, 2-16, 2-17, 4-2
Other MailMan Functions, 11-3, 11-5, 11-7, 11-9, 11-10, 11-11, 11-12
Personal Mail Group Edit, 8-2, 8-4, 8-9, 8-10, 8-13, 8-16, 12-10
Personal Preferences, 3-62, 5-41, 7-2, 7-3, 7-7, 7-10, 7-14, 7-16, 8-2, 8-4, 8-6, 8-8, 8-9, 8-10, 8-13, 8-16, 9-3, 9-12, 9-14, 10-5, 10-8, 10-10, 12-5
Query/Search for Messages, 4-2, 6-1, 6-5
Questions and Answers on MailMan Option, 12-16
Read/Manage Messages, 3-3, 4-2, 5-66
Remote User Information, 12-8
Report on Later'd Messages, 3-34, 4-34, 11-3, 11-5, 11-7
Send a Message, 4-82, 5-3, 5-4, 5-65
Surrogate Edit, 9-3, 9-4, 9-12, 9-14
Surrogates, 9-3
User Information Option, 12-5
User Options Edit, 3-62, 4-33, 5-57
XM PERSONAL MENU, 8-6, 8-8
XMASSUME, 9-3, 9-4, 9-5, 9-13
XMEDITPERSGROUP, 8-2
XMEDITSURR, 9-3, 9-12
XMENROLL, 8-2, 8-3, 8-6, 8-8
XMHELP, 8-2
XMNEW, 2-3, 2-5, 2-7, 2-9, 2-12, 2-14, 2-16, 2-17, 4-2
XMREAD, 3-3, 4-2, 5-66
XMSEARCH, 4-2, 6-1
XMSEND, 4-82, 5-3, 5-4, 5-65
XMUSER, 1-2
ORDER Field (Filters), 7-3, 7-5
Organizer For a Mail Group, 8-3, 8-9, 12-10, 12-11
Orientation, xvii
Other MailMan Functions
Change/Delete Later'd Messages Option, 3-34, 4-34, 11-3, 11-6, 11-7, 11-9
Mailbox Contents List Option, 11-3, 11-10, 11-11, 11-12
Report on Later'd Messages Option, 3-34, 4-34, 11-3, 11-5, 11-7
Other MailMan Functions Option, 11-3, 11-5, 11-7, 11-9, 11-10, 11-11, 11-12
Other Surrogates, 9-1, 9-5
P
Paging Action Codes, 3-61
Enter or Return, 3-61
Minus Number, 3-61
Minus Sign, 3-61
Plus Number, 3-61
Plus Sign, 3-61
Zero, 3-61
Password When Scrambling Messages, 5-59
Patches
History, iv
Personal Mail Group Edit Option, 8-2, 8-4, 8-9, 8-10, 8-13, 8-16, 12-10
Personal Mail Groups, 8-9
How to
Create, 8-10
Delete, 8-16
Edit, 8-13
Personal Preferences Option, 3-62, 5-41, 7-2, 7-3, 7-7, 7-10, 7-14, 7-16, 8-2, 8-4, 8-6, 8-8, 8-9, 8-10, 8-13, 8-16, 9-3, 9-12, 9-14, 10-5, 10-8, 10-10, 12-5
Delivery Basket Edit Option, 5-41
User Options Edit Option, 3-62, 4-33, 5-57
Plus
Number, 3-61
Sign, 3-61
P-MESSAGE Device, 5-34
Postmaster, 5-19
Preferences
Delivery Basket Edit Option, 5-41
User Options Edit Option, 3-62, 4-33, 5-57
Prefix Codes
Addressing, 5-16
Carbon Copy, 5-17
Information Only, 5-17, 5-51
Later, 5-18, 5-26, 5-27
Remove Recipient (Minus), 5-18
Print
All of Your New Messages, How to, 2-14
Information, 2-14, 2-15
Message Action Code, 4-38
Messages In a Basket Action Code, 3-32, 3-42
To Browser Action Code:, 4-11
Priority
Delivery Action Code, 5-57
Mail, 2-6, 2-9, 2-11, 2-12, 2-15, 2-16
Messages
How to List All, 2-11
Replies Action Code, 4-33
PRIORITY RESPONSES FLAG Field, 4-33, 5-57
PRIORITY RESPONSES PROMPT Field, 5-57
Privileges
Surrogates Read and Write Privileges, 9-2, 9-10
Surrogates Read Privileges, 9-1, 9-8
Q
Query
(Search for) Messages In a Basket, 3-46
Addressees to a Message Action Code, 4-41
Current Action Code, 4-46
Detailed Action Code, 4-49
Network Action Code, 4-52
Not Current Action Code, 4-57
Recipients Action Code, 4-43
Search for Messages, 6-1
Terminated Action Code, 4-59
Query/Search for Messages Option, 4-2, 6-1, 6-5
Question Mark Help, xviii
Questions and Answers
About MailMan Online, 12-16
Questions and Answers on MailMan Option, 12-16
Quit
How to
Exit the New Messages Option, 2-17
R
Read All of Your New Mail by Basket, How to, 2-5
Read/Manage Messages Option, 3-3, 4-2, 5-66
Read/Rcvd, 2-10, 3-19, 3-21
Reader, Assumptions About the, xix
Reading/Managing Messages
In a Basket, 3-1
Individual Messages, 4-1
New Messages and Responses, 2-1
Recipient Prefix Codes, 5-16
Recipients, Editing, 5-44
Reference Materials, xx
REFERENCED COUNT Field, 12-10, 12-11
REMOTE USER DIRECTORY File (#4.2997), 12-8
Remote User Information, 12-8
Remote User Information Option, 12-8
Removing
Recipient (Minus) Prefix Code, 5-18
Surrogates, 9-14
Vaporization Date
Individual Messages, 4-81
Replies
Interrupted, 4-75
Reply To
Differs From the From Address, 4-73
Replying
"Reply To" Differs From the "From" Address, 4-73
Message Action Code, 4-62
Include Message, 4-29
Messages, 4-5
Report on Later'd Messages Option, 3-34, 4-34, 11-3, 11-5, 11-7
Reports and Lists, 11-1
How to
Change a Message's Latered Date and Time, 11-7
Change/Delete a Message's, 11-7
Delete
Message's Latered Date and Time, 11-9
Get a List of All Messages in Your Mailbox, 11-10
Get a Report On Latered Messages in Your Mailbox, 11-5
Request Confirm Receipt Action Code, 5-58
Resequence Messages In a Basket Action Code, 3-51
Respond to a Message, How to, 4-64
Respondents Index, 4-10, 4-14, 4-67
Responding to the Latest Response, 4-72
Responses are
ORDINARY (Response For PRIORITY RESPONSES FLAG Field), 4-33
PRIORITY (Response For PRIORITY RESPONSES FLAG Field), 4-33
Restrictions of a Mail Group, 12-10
Review a Message, 5-38
Revision History, iii
Documentation, iii
Patches, iv
RML
Read/Manage Messages Option, 3-3, 4-2, 5-66
S
Save a Message Action Code, 4-76
Save Messages to Another Basket Action Code, 3-53
Scan All of Your New Messages, How to, 2-16
Scheduled Task, 5-53
Scramble
Action Code, 5-59
Hint, 5-59
Password, 5-59
Search
Messages, 3-46
In a Particular Basket, 6-18
In A Particular Basket, 6-13
Only In Your Mailbox, 6-9
Search All Messages, 6-6
Search Criteria, 6-3
Where, 6-2
Searching
Mail, 6-1
Security Keys
XM AUTO-FORWARD WAIVER, 10-2
XMMGR, 9-5, 12-10
XMNET, 10-2
XUPROGMODE, 4-85
SELECTED BASKETS ONLY (Response For Delivery Basket Privileges), 5-43
Selecting Messages, 3-12
Self-Enrollment, 8-3, 8-4, 8-6, 8-7, 8-8, 12-10, 12-11, 12-13
Send a Message Option, 4-82, 5-3, 5-4
Send Message Option, 5-65
Sending
Mail, 5-1
Messages
Action Codes, 5-37
Addressing With Prefix Codes, 5-16
Backup Action Code, 5-38
Canceling Before Sending, 5-65
Carbon Copy Prefix Code, 5-17
Closed Message Action Code, 5-64
Confidential Action Code, 5-39
Confirm Receipt Action Code, 5-58
Deferred Send Action Code, 5-11, 5-26, 5-27, 5-52
Delivery Basket Set Action Code, 5-41
Edit Recipients Action Code, 5-44
Edit Subject Action Code, 5-46
Edit Text Action Code, 5-48
Information Only
Prefix Code, 5-17, 5-51
Information Only Action Code, 5-50
Later Prefix Code, 5-18, 5-26, 5-27
Network Signature Action Code, 5-55
P-MESSAGE Device, 5-34
Prefix Codes, 5-16
Priority Delivery Action Code, 5-57
Remove a Recipient (Minus), 5-18
Scramble Action Code, 5-59
Staggered Delivery Prefix Code, 5-18, 5-26, 5-27
To a Group, 8-1
To Local Recipients, 5-14
To Remote Recipients, 5-15
To Yourself, 5-5
Transmit Later Action Code, 5-11, 5-26, 5-27, 5-52
Transmit Now Action Code, 5-26, 5-27, 5-61
Vaporize Date Set Action Code, 5-62
Write Action Code, 4-82
SHARED,MAIL, 5-40, 9-1, 9-3, 9-4, 9-5
SHOW DUZ WHEN ADDRESS MESSAGE Field (#7.3), 5-7, 5-8
SML
Send a Message Option, 4-82, 5-3, 5-4, 5-65
Stagger Delivery (Later) Prefix Code, 5-18, 5-26, 5-27
STATUS Field, 7-3
Stop Reading a Message,, 2-19
String Search Action Codes, 3-63
Subject, 5-7
Messages, 2-9, 3-20, 3-21, 3-29, 3-32, 3-42, 3-46, 4-41, 4-43, 4-46, 4-49, 4-57, 4-59, 5-37, 6-2, 6-3, 6-9, 7-4, 11-5, 11-7, 11-10
Editing, 5-46
Summary List of Recipients, 3-33, 3-45, 4-22, 4-39
Surrogate Edit Option, 9-3, 9-4, 9-12, 9-14
Surrogate Options, 9-3
Surrogates, 5-39, 5-40, 9-1
How to
Become One, 9-3
Designate, 9-12
Remove, 9-14
Other Surrogates, 9-1, 9-5
Read and Write Privileges, 9-2, 9-10
Read Privileges, 9-1, 9-8
SHARED,MAIL, 9-1, 9-3, 9-4, 9-5
Symbols
Found in the Documentation, xvii
T
Table of Contents, v
Tables and Figures, xi
TaskMan User Option menu, 5-53, 5-54
Tasks, Scheduled, 5-53
TBOX, 5-53
Terminate
Message Action Code, 4-16, 4-78
Messages In a Basket Action Code, 3-23, 3-55
Text
Editing, 5-48
Text String Search Action Codes, 3-63
Toggles
Change Detail Action Code, 3-19
Closed Message Action Code, 5-64
Confidential Action Code, 5-39
Confirm Receipt Action Code, 5-58
Extract KIDS or PackMan Messages Action Code, 4-85
Information Only Action Code
For Messages Sent By You, 4-32
When Sending Messages, 5-50
New/Un New a Message Action Code, 4-37
Opposite Selection Action Code, 3-11, 3-39
Priority Delivery Action Code, 5-57
Priority Replies Action Code, 4-33
Zoom Selection Action Code, 3-11, 3-59
Toolbox Menu Options, 5-53
Trace
Header, 4-52
Transmit Later Action Code, 5-11, 5-26, 5-27, 5-52
Transmit Now Action Code, 5-26, 5-27, 5-61
Type, 12-10
U
Un-Delete, 3-24
Unscramble, 5-59
Un-Terminate, 3-56
URLs
Adobe Acrobat Quick Guide Web Address, xx
Adobe Home Page Web Address, xx
HSD&D Home Page Web Address, xix
ISS
Acronyms Home Page Web Address, Glossary, 3
Glossary Home Page Web Address, Glossary, 3
MailMan Home Page Web Address, xx
VistA Documentation Library (VDL) Home Page Web Address, xx
Use this Manual, How to, xvii
User
Information, 12-5
Names, 5-7
User Information Option, 12-5
User Options Edit Option
MESSAGE ORDER Field, 3-62
PRIORITY RESPONSES FLAG Field, 4-33, 5-57
PRIORITY RESPONSES PROMPT Field, 5-57
V
Vaporization
Individual, 4-80
Multiple, 3-57
Vaporize Date
Edit Action Code, 3-57, 4-79
Remove from Individual Messages, 4-81
Set Action Code, 5-62
Setting Vaporization Date for Individual Messages, 4-80
Setting Vaporization Date for Multiple Messages, 3-57
VistA Documentation Library (VDL)
Home Page Web Address, xx
W
Web Pages
Adobe Acrobat Quick Guide Web Address, xx
Adobe Home Page Web Address, xx
HSD&D Home Page Web Address, xix
ISS
Acronyms Home Page Web Address, Glossary, 3
Glossary Home Page Web Address, Glossary, 3
MailMan Home Page Web Address, xx
VistA Documentation Library (VDL) Home Page Web Address, xx
Where to Search, 6-2
Write a Message Action Code, 4-82
X
XM AUTO-FORWARD WAIVER Security Key, 10-2
XM GROUP EDIT NOTIFY Bulletin, 8-7
XM PERSONAL MENU Option, 8-6, 8-8
XMASSUME Option, 9-3, 9-4, 9-5, 9-13
XMEDITPERSGROUP Option, 8-2
XMEDITSURR Option, 9-3, 9-12
XMENROLL Option, 8-2, 8-3, 8-6, 8-8
XMHELP Option, 8-2
XMMGR Security Key, 9-5, 12-10
XMNET Security Key, 10-2
XMNEW Option, 2-3, 2-5, 2-7, 2-9, 2-12, 2-14, 2-16, 2-17, 4-2
XMREAD Option, 3-3, 4-2, 5-66
XMSEARCH Option, 4-2, 6-1
XMSEND Option, 4-82, 5-3, 5-4, 5-65
XMSTAR LIMITED Security Key, 5-19
XMSTAR Security Key, 5-19
XMUSER Menu, 1-2
XUPROGMODE Security Key, 4-85
Y
YES, ACCEPT IT (Response For Delivery Basket Privileges), 5-43
Z
Zero, 3-61
Zoom Selection Toggle Action Code, 3-11, 3-59
