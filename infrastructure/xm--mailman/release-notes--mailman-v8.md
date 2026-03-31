---
title: MailMan Version 8 Release Notes
doc_type: RN
doc_label: Release Notes
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
description: The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.
audience: 
keywords: 
  - mailman
  - table
  - strong
  - message
  - messages
  - date
  - contents
  - blockquote
  - style
  - width
page_count: 0
word_count: 1410
section_count: 2
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_releasenotes.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_releasenotes.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=15"
---

![](mailman-version-8-release-notes/001.png)

MAILMANRELEASE NOTES

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
<td>REDACTED and REDACTED Oakland, CA Office of Information Field Office (OIFO)</td>
</tr>
<tr class="even">
<td>09/21/06</td>
<td>2.0</td>
<td><p>MailMan V. 8.0 documentation reformatting/revision.</p>
<p>Reformatted document to follow the latest ISS styles and guidelines.</p>
<p>As of this date, all content updates have been completed for all released MailMan patches.</p>
<p><strong>PDF 508 Compliance—</strong>The final PDF document supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td><p>MailMan Development Team Oakland, CA Office of Information Field Office (OIFO):</p>
<ul>
<li><blockquote>
<p>Maintenance Project Manager—REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Project Planner—REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Developers—REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Technical Writer—REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

Table i: Documentation revision history

Patch Revisions

For a complete list of patches released with this software, please refer to the Patch Module on FORUM.

Contents

# MailMan Version 8.0 Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [MailMan Version 8.0 Release Notes](#mailman-version-80-release-notes)
    - [Why was MailMan V. 8.0 Created?](#why-was-mailman-v-80-created)
    - [What are the New Features and Improvements?](#what-are-the-new-features-and-improvements)
This document highlights the various new maintenance requirements, technical solutions, and the functionality improvements introduced with MailMan V. 8.0.
The topics covered in this document include:
- Why was MailMan V. 8.0 Created?
- What are the New Features and Improvements?

### Why was MailMan V. 8.0 Created?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan, part of the Veterans Health Information Systems and Technology Architecture (VistA), is over 20 years old now. It was one of the first VistA software applications implemented at field facilities. The code was compactly written, and variable names were kept to very few characters. However, over the years, as it grew and gained capabilities, MailMan has been continually patched, making it very difficult to maintain and was lacking certain functionality. Thus, a new version of MailMan was created in order to ease installation and maintenance and to introduce new functionality.

### What are the New Features and Improvements?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### MailMan V. 8.0 is DNS-Aware

MailMan V. 8.0 is now DNS-Aware. It uses Kernel's MAIL^XLFNSLK API to retrieve IP addresses. Thus, it is no longer necessary to manually update the IP addresses in the DOMAIN file (#4.2). The IP address fields still remain in File \#4.2 and MailMan continues to use them. However, if they don't work, MailMan uses the Kernel API to retrieve a list of valid IP addresses. When MailMan finds one that works, MailMan replaces the non-working IP address with the working one.
In order to activate DNS awareness, the new DNS AWARE field (#8.22) in the MAILMAN SITE PARAMETERS file (#4.3) *must* be set to Yes.
Also, routine ^XLFNSLK *must* exist, and the DNS IP field (#51) in the KERNEL SYSTEM PARAMETERS file (#8989.3) *must* be properly filled in with an IP address.

#### Transmission Scripts and TCP/IP Connections

For TCP/IP connections, MailMan can now build transmission scripts on the fly. For transmission scripts whose TYPE is "SMTP," "TCPCHAN," or null, if the transmission script has no records (in the TEXT field \[#2\], in the TRANSMISSION SCRIPT multiple) in the DOMAIN file (#4.2), MailMan creates the script if the following new fields in the MAILMAN SITE PARAMETERS file (#4.3) are filled in:
- TCP/IP COMMUNICATIONS PROTOCOL (#8.23)—MailMan uses this field to determine which protocol shall be used for TCP/IP. It points to the COMMUNICATIONS PROTOCOL file (#3.4).
- TCP/IP TRANSMISSION SCRIPT (#8.24)—MailMan uses this field to determine which script shall be used for TCP/IP. It points to the TRANSMISSION SCRIPT file (#4.6).

#### Transmission Priority Flexibility

Messages in transmit queues can now be designated as low priority, as well as high priority. If a message gets stuck in a transmit queue and is holding up the rest of the queue for whatever reason, MailMan will make that message a low priority message, so that all the other messages are transmitted ahead of it. The Postmaster can also make these priority changes. In the message queue, high-priority messages are now marked with "^", instead of "\$". Low priority messages are marked with "v". The Postmaster can now change the transmit priority at the message level (at the "Message action: Ignore//" prompt). As at the basket level, the command to use is "X".
|                                                   |                                                                                                                                                                                                                                                                      |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-release-notes/002.png) | CAUTION: In a user basket, the "X" at the message level is a command to unload a PackMan message or KIDS build. In a remote transmit queue, the "X" changes the transmit priority. The difference is the context, and writers of MailMan front-ends should take note |

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
Table 1. MailMan V. 8.0: New date/time format
This change is also carried through to all MailMan APIs that return date/time in MailMan format.
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mailman-version-8-release-notes/003.png)</td>
<td><p><strong>REF:</strong> For more information on this Kernel API, please refer to the $$FMTE^XLFDT Home Page at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/kernel/apis/x-fmte%5exlfdt.asp">http://vista.med.va.gov/kernel/apis/x-fmte^xlfdt.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>
|                                                                                                                |                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mailman-version-8-release-notes/004.png) | REF: For information on how to obtain a list of Integration Agreements (IAs) related to MailMan, please refer to the "Integration Agreements (IAs)" topic in the "External Relations" chapter in the *MailMan Technical Manual*. |

#### Reformatted Remote Message IDs

MailMan remote message IDs now include the message date, to ensure that if you are told that a message is a duplicate of a previously received message, it really is. Sites will no longer have problems sending messages from a production account to a test account that was created by "mirroring" the production account. The remote message ID is now the message number followed by a period, followed by the 7-digit VA FileMan message creation date. For example:
|                                            |                                            |
|--------------------------------------------|--------------------------------------------|
| MailMan V. 7.1 Remote Message ID (Old) | MailMan V. 8.0 Remote Message ID (New) |
| 34561234@FORUM.VA.GOV                      | 34561234.3020803@FORUM.VA.GOV              |
Table2. MailMan V. 8.0: New remote message ID format

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
Table 3. MailMan V. 8.0: New name field display format

#### Broadcast Messages with Responses

Messages with responses may no longer be forwarded to broadcast to all users. Such messages may have important information in the responses, and as we all know, responses are not auto-forwarded to remote sites for users with auto-forward addresses. Users who attempt to broadcast messages with responses will be encouraged to copy the message and its responses into a new message, which can be broadcast.

#### Message Line Restriction Override

Incoming PackMan and KIDS messages are no longer subject to the restriction of the NETWORK - MAX LINES RECEIVE field (#8.31) in the MAILMAN SITE PARAMETERS file (#4.3). However, other kinds of messages continue to be subject to that restriction.

#### Requeued Task Bug Fix

If a task transmitting messages to another site fails and has to be requeued, it really is requeued. Before, that wasn't true. Previously, the failing task queued up a new task to take its place, and then the failing task stopped.
