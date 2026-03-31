---
title: "Kernel 8.0 Developerâ€™s Guide: Server Options User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Server Options"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - server
  - guide
  - developer
  - table
  - kernel
  - bulletin
  - options
  - span
  - contents
  - request
page_count: 0
word_count: 1166
section_count: 5
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_server_options_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_server_options_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259523" class="anchor"></span>Server Options Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-server-options-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-server-options-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref502895428" class="anchor"></span>Table 1: Key Variable Setup—Server Options</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 29%" />
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
<td>08/28/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Server Options Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref502895428" class="anchor"></span>Table 1: Key Variable Setup—Server Options

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc234301876" class="anchor"></span>List of Figures

[Figure 1: XQSERVER—Default Bulletin [3](#_Ref503169872)](#_Ref503169872)

<span id="_Toc207255126" class="anchor"></span>List of Tables

[Table 1: Key Variable Setup—Server Options [2](#_Ref502895428)](#_Ref502895428)

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-server-options-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Developer Tools](#developer-tools)
  - [Tools for Processing Server Requests](#tools-for-processing-server-requests)
  - [Key Variables When a Server Option is Running](#key-variables-when-a-server-option-is-running)
  - [Appending Text to a Server Request Bulletin or MailMan Reply](#appending-text-to-a-server-request-bulletin-or-mailman-reply)
  - [Customizing a Server Request Bulletin](#customizing-a-server-request-bulletin)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Server Options Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Developer Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Tools for Processing Server Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a server option runs, it can call custom programs to perform server-related tasks such as responding to the sender of the server request or retrieving the actual text of the server request message. In this way, server requests can act *not* only as triggers, but also as message carriers. The server option can call custom programs through the following fields:

- ENTRY ACTION
- HEADER
- ROUTINE
- EXIT ACTION

![](kernel-8-0-developer-s-guide-server-options-user-guide/004.png) REF: For more information on server options, see the “Server Options” section in the [*Kernel 8.0 Systems Management: Menu Manager User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf).

![](kernel-8-0-developer-s-guide-server-options-user-guide/005.png) REF: For more information on the developer API for processing server requests, see the *MailMan Developer’s Guide*.

## Key Variables When a Server Option is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are key variables that are set up when a server option is running. You can reference these key variables during any routine run by the server option’s fields:

- ENTRY ACTION
- HEADER
- ROUTINE
- EXIT ACTION

<u>Table 1</u> lists the key variables setup for server options:

| Variable  | Description                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------|
| XQSOP | Server option name.                                                                                         |
| XQMSG | Server request message number.                                                                              |
| XQSND | DUZ of the sender if the request is local; network address of the sender if the request is *not* local. |
| XQSUB | Subject heading of the server request message.                                                              |

## Appending Text to a Server Request Bulletin or MailMan Reply

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Server options use bulletins and MailMan messages to communicate with the local system administrators when a server request is received, or with the sender of a server request, usually in the event of an error. These two kinds of documents look very similar and *must* contain certain key pieces of data. It is also possible, however, for the sender or the local system administrators to append other information to the bulletin or MailMan message by setting that information into the array XQSTXT (one line per node). For example, if the following array exists:

XQSTXT(0)="Please append these two lines of text"XQSTXT(1)="to the end of the bulletin XQSERVER."

The default bulletin, XQSERVER, would then look like <u>Figure 1</u>:

<span id="_Ref503169872" class="anchor"></span>Figure 1: XQSERVER—Default Bulletin

Subj: Server request notice

From: \<Postmaster\>

------------------------------------------------------------------

Dec. 21, 1989 3:08 PM

A request for execution of a server option was received.

Sender: \<Child,Your@HOME.VA.GOV\>

Option name: ZZUPDATECL

Subject: UPDATE CHRISTMAS LIST DATA BASE

Message \#: 136771

Menu system Action: No error(s) detected by the menu system.

Please append these two lines of text

to the end of the bulletin XQSERVER.

You can use the same method to append text to MailMan messages.

## Customizing a Server Request Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please note that the first six data elements in a server request bulletin are always:

1.  The date and time the request was received.
2.  The sender.
3.  The requested option’s name.
4.  The subject of the message of the server request.
5.  The requesting message’s number.
6.  A brief statement of the menu system’s action or an error message.

If you use a customized bulletin instead of XQSERVER, these data elements should always be printed first, followed by the contents of XQSTXT.

The easiest way to create a customized local bulletin is to use the VA FileMan copy function to copy the default bulletin XQSERVER to a bulletin of another name.

![](kernel-8-0-developer-s-guide-server-options-user-guide/006.png) NOTE: XQSERVER has a line of text in it that says:  
  
is the server request bulletin XQSERVER  
  
To avoid confusion, you should edit this line using the Bulletin Edit \[XMEDITBUL\] option to reflect the name of the new bulletin.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-server-options-user-guide/007.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-server-options-user-guide/008.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-server-options-user-guide/009.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.